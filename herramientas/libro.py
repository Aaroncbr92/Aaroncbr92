#!/usr/bin/env python3
"""Arma el bloque general en un volumen imprimible.

Un tema en pantalla y un tema impreso no se ordenan igual. En pantalla se salta
con el índice; en papel hay que decidir un orden y sostenerlo. El de aquí:

  1. Portada del volumen y aviso de uso, con la **fecha de corte** delante,
     porque es lo que decide qué redacción vale.
  2. Índice general.
  3. Cada tema, en el **orden del programa oficial** —no en el orden en que se
     escribieron—, y dentro de cada uno: **ficha, índice, cuerpo, esquema y
     preguntas reales**. El esquema **detrás** del cuerpo y no delante: es para
     repasar, y puesto antes invita a leer el esqueleto y saltarse la carne.
  4. Las **respuestas, al final del volumen**. Si van junto a la pregunta no hay
     autoevaluación posible; y separadas caben las advertencias sobre las
     plantillas oficiales que están mal, que en la misma página serían ruido.

Uso:  libro.py [salida.html]
      python3 herramientas/libro.py && python3 herramientas/pdf.py
"""
import glob
import html
import os
import re
import sys
from datetime import date

from markdown_it import MarkdownIt

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORTE = "21 de diciembre de 2022"

# Orden del programa oficial. Los temas 2 y 3 comparten banco de preguntas, así
# que el juego va detrás del 3, que es el corto y el que depende del 2.
TEMAS = [
    ("01-constitucion-espanola", "g1"),
    ("02-ley-17-2006", None),
    ("03-ley-5-2017", "g2-g3"),
    ("04-ley-8-2009", "g4"),
    ("05-convenio-colectivo", "g5"),
    ("06-igualdad", "g6"),
    ("07-ley-13-2022", "g7"),
    ("08-ley-31-1995", "g8"),
]

# Erratas comprobadas de las plantillas oficiales, documentadas en PENDIENTES.md.
# Se imprimen con la pregunta y con la respuesta, porque un volumen que copia la
# plantilla sin avisar enseña mal justo lo que el opositor va a memorizar.
ERRATAS = {
    "81_preguntas_produccion · nº 32":
        "La plantilla da <b>b) Título segundo</b>. Es <b>a) Título primero</b>: los derechos y "
        "deberes fundamentales son el Título I (arts. 10 a 55); el Título II es el de la Corona.",
    "77_preguntas_produccion_asist · nº 51":
        "La plantilla da <b>a) Tres</b>. Son <b>b) Dos</b>: los tres los designa el Consejo "
        "Económico y Social (art. 23.2 de la Ley 17/2006).",
    "62_preguntas_realizacion_asist_2_llamamiento · nº 77":
        "La plantilla da <b>c) 4</b>. Son <b>b) 3</b>: el art. 35.2 de la Ley 31/1995 asigna "
        "3 Delegados de 101 a 500 trabajadores; el 4 es el tramo de 501 a 1.000.",
}

md = MarkdownIt("commonmark").enable("table").enable("strikethrough")


def lee(ruta):
    return open(os.path.join(RAIZ, ruta), encoding="utf-8").read()


def sin_marcas(texto):
    """Quita las marcas HTML del generador de índices, no su contenido."""
    return texto.replace("<!-- portada -->", "").replace("<!-- /portada -->", "") \
                .replace("<!-- indice -->", "").replace("<!-- /indice -->", "")


def baja_titulos(texto, saltos=1):
    """Baja los encabezados N niveles: en el volumen el # es el tema."""
    return re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" * (len(m.group(1)) + saltos) + " ", texto)


def numera(texto, raiz):
    """Numera los epígrafes del tema y devuelve (texto, entradas del índice).

    Los temas traen la numeración escrita a mano y solo a veces: «1. Elaboración»
    la lleva y «Artículo 1. Estado, soberanía» no. Para que el índice y el cuerpo
    digan lo mismo se **quita la que venga escrita y se genera entera**, con el
    número del tema como raíz: 1, 1.1, 1.1.1. Cada epígrafe se queda además con
    un ancla, que es lo que hace el índice navegable y lo que luego permite saber
    en qué página ha caído.
    """
    cuenta = [0, 0, 0]
    entradas = []
    fuera = []
    for linea in texto.split("\n"):
        m = re.match(r"^(#{2,4}) (.+?)\s*$", linea)
        if not m:
            fuera.append(linea)
            continue
        nivel = len(m.group(1)) - 1          # h2 -> 1, h3 -> 2, h4 -> 3
        titulo = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", m.group(2))
        cuenta[nivel - 1] += 1
        for i in range(nivel, 3):
            cuenta[i] = 0
        numero = ".".join(str(x) for x in [raiz] + cuenta[:nivel] if True)
        ancla = "e" + numero.replace(".", "-")
        entradas.append((nivel, numero, titulo, ancla))
        fuera.append('%s <a id="%s"></a>%s %s' % (m.group(1), ancla, numero, titulo))
    return "\n".join(fuera), entradas


def preguntas(banco):
    """[(id, enunciado, respuesta)] del fichero del banco."""
    fuera = []
    for bloque in re.split(r"\n---\n", lee("banco/%s.md" % banco)):
        m = re.search(r"\*\*([^*]+?) · nº (\d+) · respuesta: ([^*]+)\*\*", bloque)
        if not m:
            continue
        ident = "%s · nº %s" % (m.group(1).strip(), m.group(2))
        cuerpo = re.search(r"```\n(.*?)```", bloque, re.S)
        if not cuerpo:
            continue
        fuera.append((ident, cuerpo.group(1).strip(), m.group(3).strip()))
    return fuera


CIERRA = re.compile(r"[.:;?!)]\s*$")


def ordena_opciones(enunciado):
    """Separa el enunciado de sus opciones: (enunciado, opciones, sin_texto).

    Al extraer el PDF las letras de opción quedan sueltas en su renglón. A veces
    cada una va justo encima de su texto; en otros cuadernillos salen **las
    cuatro seguidas y detrás los cuatro textos**, y además cada texto puede
    ocupar varios renglones. Pegar cada letra con el renglón siguiente juntaba
    «a) b)» y mandaba las respuestas al enunciado.

    Se lleva una cola de letras pendientes: un renglón **continúa** la opción
    abierta mientras esa opción no haya cerrado frase, y **abre** la siguiente
    cuando sí. De 504 preguntas, 502 salen con sus cuatro opciones. En las dos
    que no —opciones que el cuadernillo corta sin punto final— se devuelven las
    letras que se quedaron sin texto en vez de repartir a ojo, porque adivinar
    qué texto va con qué letra es enseñar mal justo lo que se va a memorizar.
    """
    lineas = [l.strip() for l in enunciado.split("\n") if l.strip()]
    if lineas and re.match(r"^\d+[.,\-]", lineas[0]):
        lineas[0] = re.sub(r"^\d+[.,\-]+\s*", "", lineas[0])
    cabeza, pendientes, opciones, abierta = [], [], [], False
    for linea in lineas:
        # el OCR dibuja la «c)» de doce preguntas como «Cc)», y con la letra sin
        # reconocer esa opción se fundía con la anterior
        if linea.startswith("Cc)") and [x[0] for x in opciones] == ["a", "b"]:
            linea = linea[1:]
        suelta = re.fullmatch(r"([a-d])\)", linea)
        pegada = re.match(r"^([a-d])\)\s+(.*)$", linea)
        if suelta:
            pendientes.append(suelta.group(1))
            abierta = False
            continue
        if pegada and not pendientes:
            opciones.append("%s) %s" % pegada.groups())
        elif abierta and opciones:
            opciones[-1] += " " + linea
        elif pendientes:
            opciones.append("%s) %s" % (pendientes.pop(0), linea))
        elif opciones:
            opciones[-1] += " " + linea
        else:
            cabeza.append(linea)
            continue
        abierta = not CIERRA.search(linea)
    return " ".join(cabeza).strip(), opciones, pendientes


def linea_indice(nivel, numero, titulo, ancla):
    """Un renglón del índice: número, título, línea de puntos y hueco de página.

    El hueco lo rellena `pdf.py` en una segunda pasada, cuando ya sabe en qué
    página ha caído cada ancla: el motor que compone el PDF no sabe contar
    páginas desde el documento, así que hay que componerlo, mirarlo y volver a
    componerlo.
    """
    return ('<div class="ii n%d"><a href="#%s"><span class="it">%s %s</span>'
            '<span class="pun"></span><span class="ip" data-ref="%s"></span></a></div>'
            % (nivel, ancla, numero, html.escape(titulo), ancla))


def pinta_pregunta(n, enunciado):
    cabeza, opciones, sin_texto = ordena_opciones(enunciado)
    cuerpo = "<b>%s</b>" % html.escape(cabeza) if cabeza else ""
    for o in opciones:
        cuerpo += '<div class="opcion">%s</div>' % html.escape(o)
    if sin_texto:
        cuerpo += ('<div class="suelta">El cuadernillo corta estas opciones sin punto '
                   'final, así que la transcripción no marca dónde acaba cada una y '
                   '<b>%s se queda sin texto</b>. Se imprime como salió: repartirlo a ojo '
                   'sería inventar.</div>'
                   % ", ".join("la %s)" % l for l in sin_texto))
    return ('<div class="pregunta"><div class="pnum">%d</div>'
            '<div class="ptexto">%s</div></div>' % (n, cuerpo))


CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.5 "Georgia","Times New Roman",serif; color:#111; margin:0;
       hyphens:auto; -webkit-hyphens:auto; text-align:justify; }
h1,h2,h3,h4,h5,th,td,.pnum,.rotulo { text-align:left; }
.portada-vol, .portada-vol h1, .portada-vol .rotulo, .portada-vol .sub,
.portada-vol .meta { text-align:center; }
h1,h2,h3,h4,h5 { font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; line-height:1.25;
                 page-break-after:avoid; break-after:avoid; }
h1 { font-size:20pt; margin:0 0 .2em; }
h2 { font-size:14pt; margin:1.6em 0 .5em; padding-bottom:.15em; border-bottom:1.5px solid #111; }
h3 { font-size:11.5pt; margin:1.2em 0 .35em; }
h4 { font-size:10.5pt; margin:1em 0 .3em; font-style:italic; }
p, li { orphans:3; widows:3; }
ul,ol { padding-left:1.3em; margin:.4em 0; }
li { margin:.15em 0; }
table { border-collapse:collapse; width:100%; margin:.7em 0; font-size:9pt;
        page-break-inside:avoid; break-inside:avoid; }
th,td { border:.5px solid #999; padding:3px 5px; text-align:left; vertical-align:top; }
th { background:#e4e4e4; }
/* la primera fila de toda tabla va en gris, lleve cabecera o no */
table tr:first-child > td { background:#e4e4e4; }
code { font-family:"SF Mono",Menlo,Consolas,monospace; font-size:8.5pt; background:#f2f2f2;
       padding:0 2px; }
blockquote { margin:.8em 0; padding:.5em .9em; border-left:3px solid #888; background:#f7f7f7;
             font-size:9.5pt; }
blockquote p { margin:.3em 0; }
hr { border:0; border-top:.5px solid #bbb; margin:1.4em 0; }

.portada-vol { height:245mm; display:flex; flex-direction:column; justify-content:center;
               text-align:center; page-break-after:always; }
.portada-vol h1 { font-size:30pt; border:0; margin-bottom:.1em; }
.portada-vol .sub { font-size:13pt; color:#444; margin-bottom:2.5em; }
.portada-vol .meta { font-size:10pt; color:#333; line-height:2; }
.aviso { page-break-after:always; }
.aviso .caja { border:1.5px solid #111; padding:12px 16px; margin:1.2em 0; }
.indice-gral { page-break-after:always; }
.indice-gral a { color:inherit; text-decoration:none; display:block; }
.ii { display:block; margin:0; }
.ii a { display:flex; align-items:baseline; }
.ii .it { flex:0 1 auto; }
.ii .pun { flex:1 1 auto; border-bottom:1px dotted #bbb; margin:0 .4em .18em .4em;
           min-width:1.2em; }
.ii .ip { flex:0 0 auto; font-variant-numeric:tabular-nums; color:#333; }
.ii.n0 { font-weight:bold; font-size:11pt; margin:.75em 0 .15em; page-break-after:avoid; }
.ii.n1 { font-size:9.8pt; margin-left:1.1em; }
.ii.n2 { font-size:9.2pt; margin-left:2.4em; color:#444; }
.ii.n3 { font-size:8.8pt; margin-left:3.7em; color:#666; }

.tema { page-break-before:always; }
.tema > h1 { border-bottom:3px solid #111; padding-bottom:.25em; margin-bottom:.8em; }
.rotulo { font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; font-size:8.5pt;
          letter-spacing:.12em; text-transform:uppercase; color:#666; margin:0 0 .3em; }
.ficha table { font-size:8.5pt; }
.ficha th, .ficha td { border:0; border-bottom:.5px solid #ddd; }
.parte { page-break-before:always; }
.parte h2 { border-bottom:3px double #111; font-size:16pt; }
.esquema { font-size:9.5pt; }
.esquema h2 { font-size:12pt; }
.esquema h3 { font-size:10pt; }

.pregunta { display:flex; gap:8px; margin:.55em 0; page-break-inside:avoid;
            break-inside:avoid; font-size:9.5pt; }
.pnum { flex:0 0 26px; font-family:Helvetica,Arial,sans-serif; font-weight:bold;
        font-size:9pt; color:#fff; background:#111; height:20px; text-align:center;
        line-height:20px; }
.ptexto { flex:1; }
.suelta { border-left:3px solid #999; padding:3px 8px; margin-top:4px; font-size:8pt;
          color:#555; font-style:italic; text-align:left; }
.errata { border-left:3px solid #111; background:#f0f0f0; padding:5px 9px; margin:6px 0;
          font-size:9pt; }
/* el solucionario alterna: fila de números en gris, fila de letras en blanco */
table.claves { font-size:10pt; margin:.4em 0 1.2em; }
table.claves th, table.claves td { text-align:center; width:10%; }
table.claves th { background:#e4e4e4; font-weight:bold; }
table.claves td { background:#fff; font-weight:bold; }
.opcion { margin-left:1.1em; text-indent:-1.1em; }
@media screen { body { max-width:190mm; margin:0 auto; padding:16mm 10mm; background:#fff; } }
"""


def main():
    salida = sys.argv[1] if len(sys.argv) > 1 else "libro-general.html"

    partes, indice_gral, total_preg = [], [], 0
    for i, (base, banco) in enumerate(TEMAS, 1):
        crudo = sin_marcas(lee("temas/general/%s.md" % base))
        titulo = re.search(r"(?m)^# (.+)$", crudo).group(1)
        cuerpo = re.sub(r"(?m)^# .+$\n", "", crudo, count=1)
        # fuera el índice del propio tema: el volumen lleva el suyo
        cuerpo = re.sub(r"## Índice\n.*?(?=\n## )", "", cuerpo, flags=re.S)
        ficha, resto = "", cuerpo
        mt = re.match(r"\s*(\|.*?\|)\n\n", cuerpo, re.S)
        if mt:
            ficha = md.render(mt.group(1))
            resto = cuerpo[mt.end():]

        esquema = sin_marcas(lee("esquemas/general/%s.md" % base))
        esquema = re.sub(r"(?m)^# .+$\n", "", esquema, count=1)
        esquema = re.sub(r"## Índice\n.*?(?=\n## )", "", esquema, flags=re.S)

        resto, entradas = numera(resto, i)
        indice_gral.append((i, titulo, entradas))

        bloque = ['<section class="tema" id="tema-%d">' % i]
        bloque.append('<p class="rotulo">Temario general</p>')
        bloque.append("<h1>TEMA %d – %s</h1>"
                      % (i, html.escape(titulo.split("·", 1)[-1].strip())))
        if ficha:
            bloque.append('<div class="ficha">%s</div>' % ficha)
        bloque.append(md.render(baja_titulos(resto, 0)))
        bloque.append('<section class="parte esquema"><h2>Esquema de repaso · tema %d</h2>%s</section>'
                      % (i, md.render(esquema)))
        if banco:
            ps = preguntas(banco)
            total_preg += len(ps)
            rot = ("Preguntas reales de examen · temas 2 y 3" if banco == "g2-g3"
                   else "Preguntas reales de examen · tema %d" % i)
            bloque.append('<section class="parte"><h2>%s</h2>' % rot)
            bloque.append("<p><i>%d preguntas de los cuadernillos de 2024. "
                          "Las respuestas, al final del volumen.</i></p>" % len(ps))
            bloque.append("".join(pinta_pregunta(n, e)
                                  for n, (_, e, _) in enumerate(ps, 1)))
            bloque.append("</section>")
            TEMAS[i - 1] = (base, banco, ps)
        bloque.append("</section>")
        partes.append("\n".join(bloque))

    # ── apéndice de respuestas ────────────────────────────────────────────────
    resp = ['<section class="tema"><p class="rotulo">Apéndice</p>'
            '<h1>Respuestas oficiales</h1>',
            "<p>La respuesta es la de la <b>plantilla oficial</b> del examen, y el número "
            "es el que la pregunta lleva impreso en su tema. "
            "<b>Tres respuestas oficiales están mal</b> y van avisadas debajo de su tabla: "
            "el volumen enseña la norma, no la plantilla.</p>"]
    for i, t in enumerate(TEMAS, 1):
        if len(t) < 3:
            continue
        base, banco, ps = t
        rot = "Temas 2 y 3" if banco == "g2-g3" else "Tema %d" % i
        resp.append("<h2>%s</h2>" % rot)
        # la respuesta se busca por el número con el que la pregunta está impresa;
        # el cuadernillo del que salió ya no se imprime, que al opositor no le dice nada
        sueltas = [(n, r) for n, (_, _, r) in enumerate(ps, 1)]
        erratas = [(n, ERRATAS[ident]) for n, (ident, _, _) in enumerate(ps, 1)
                   if ident in ERRATAS]
        filas, POR_FILA = [], 10
        for a in range(0, len(sueltas), POR_FILA):
            trozo = sueltas[a:a + POR_FILA]
            filas.append("<tr>%s</tr><tr>%s</tr>"
                         % ("".join("<th>%d</th>" % n for n, _ in trozo),
                            "".join("<td>%s</td>" % html.escape(r) for _, r in trozo)))
        resp.append('<table class="claves">%s</table>' % "".join(filas))
        for n, texto in erratas:
            resp.append('<div class="errata"><b>Ojo con la %d:</b> %s</div>' % (n, texto))
    resp.append("</section>")

    ig = []
    for i, t, entradas in indice_gral:
        ig.append(linea_indice(0, "TEMA %d –" % i, t.split("·", 1)[-1].strip(),
                               "tema-%d" % i))
        for nivel, numero, titulo, ancla in entradas:
            ig.append(linea_indice(nivel, numero, titulo, ancla))

    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>Temario general · Oposiciones RTVE</title><style>{CSS}</style></head><body>
<section class="portada-vol">
  <p class="rotulo">Oposiciones RTVE · convocatorias 1/2022 y 3/2022</p>
  <h1>Temario general</h1>
  <p class="sub">Los ocho temas comunes a Producción (Asistencia),<br>
     Documentación e Información y Contenidos</p>
  <div class="meta">
    Redacción vigente a <b>{CORTE}</b><br>
    Ocho temas · ocho esquemas de repaso · <b>{total_preg}</b> preguntas reales de examen<br>
    Generado el {date.today().strftime('%d/%m/%Y')}
  </div>
</section>

<section class="aviso">
<h1>Cómo usar este volumen</h1>
<div class="caja">
<p><b>La redacción que vale es la del {CORTE}</b>, que es la fecha de corte que
imponen las bases: «las pruebas se realizarán sobre su texto vigente a fecha de la primera
publicación de las Bases Generales». Lo que cambió después está en el tema, en apartados
marcados como <i>notas de actualización</i>, y <b>no es materia examinable</b>.</p>
</div>
<p><b>Cada tema trae tres partes.</b> El <b>cuerpo</b>, para leer; el <b>esquema</b>, para
repasar, que va detrás y no delante a propósito; y las <b>preguntas reales</b> de los
cuadernillos de 2024, para comprobar si el tema se sostiene. <b>Las respuestas están al final
del volumen</b>, no junto a la pregunta: con la respuesta a la vista no hay autoevaluación.</p>
<p><b>Tres respuestas oficiales de 2024 están mal.</b> Van marcadas una a una en el apéndice,
con el precepto que las desmiente. El temario enseña la norma, no la plantilla.</p>
<p><b>Las preguntas se imprimen tal como salieron del examen</b>, sin más limpieza que
quitarles el pie de página. Son transcripciones de los cuadernillos oficiales y traen sus
costuras: alguna arrastra una letra mal reconocida. <b>Están leídas una a una</b> y colocadas
en el tema que les toca, comprobando cada una contra la norma.</p>
<p><b>Nada de aquí se ha escrito de memoria.</b> Cada dato se ha leído en el texto consolidado
del BOE en su redacción a la fecha de corte, o en la fuente oficial que se cita en la
trazabilidad de cada tema.</p>
</section>

<section class="indice-gral"><h1>Índice general</h1><ol>{''.join(ig)}</ol></section>

{''.join(partes)}
{''.join(resp)}
</body></html>"""

    # si una errata deja de casar con su pregunta, desaparece del apéndice sin
    # decir nada: el volumen volvería a dar por buena una plantilla que está mal
    sueltas = set(ERRATAS) - {i for t in TEMAS if len(t) > 2 for i, _, _ in t[2]}
    if sueltas:
        print("  ! erratas sin pregunta a la que pegarse: %s" % ", ".join(sorted(sueltas)))

    ruta = os.path.join(RAIZ, salida)
    open(ruta, "w", encoding="utf-8").write(doc)
    print("· %s · %d KB · %d temas · %d preguntas"
          % (salida, len(doc) // 1024, len(TEMAS), total_preg))


if __name__ == "__main__":
    main()
