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


def preguntas(banco, excluir=()):
    """[(id, enunciado, respuesta)] del fichero del banco."""
    fuera = []
    for bloque in re.split(r"\n---\n", lee("banco/%s.md" % banco)):
        m = re.search(r"\*\*([^*]+?) · nº (\d+) · respuesta: ([^*]+)\*\*", bloque)
        if not m:
            continue
        ident = "%s · nº %s" % (m.group(1).strip(), m.group(2))
        if ident in excluir:
            continue
        cuerpo = re.search(r"```\n(.*?)```", bloque, re.S)
        if not cuerpo:
            continue
        fuera.append((ident, cuerpo.group(1).strip(), m.group(3).strip()))
    return fuera


def pinta_pregunta(n, ident, enunciado, con_respuesta=None):
    texto = html.escape(enunciado)
    # el enunciado viene del PDF del cuadernillo: las letras de opción quedan
    # sueltas en su renglón y se vuelven a pegar aquí para que se lea
    texto = re.sub(r"(?m)^([a-d])\)\s*$\n", r"\1) ", texto)
    lineas = [l for l in texto.split("\n") if l.strip()]
    # el pie del cuadernillo («Página: 11 de 20») se cuela en la transcripción y
    # no es parte de la pregunta. Es lo único que se quita: intentar además
    # cortar donde parece empezar otra pregunta destrozaba las buenas, porque
    # una opción como «d) 199.» tiene exactamente esa forma
    lineas = [l for l in lineas if not re.match(r"\s*Página:?\s*\d+\s*de\s*\d+\s*$", l)]
    if lineas and re.match(r"^\d+[.\-]", lineas[0]):
        lineas[0] = re.sub(r"^\d+[.\-]+\s*", "", lineas[0])
    pegada = any(re.search(r"\d+º\s*Llamamiento", l) for l in lineas)
    cuerpo = "<br>".join(lineas)
    if pegada:
        cuerpo += ('<div class="pegada">La transcripción del cuadernillo dejó aquí '
                   '<b>dos preguntas seguidas</b>. Se imprime tal cual: recortarla a ojo '
                   'sería inventar dónde acaba una y empieza la otra.</div>')
    extra = ""
    if con_respuesta:
        extra = '<div class="resp">Respuesta oficial: <b>%s</b></div>' % html.escape(con_respuesta)
    return ('<div class="pregunta"><div class="pnum">%d</div>'
            '<div class="ptexto">%s<div class="pfuente">%s</div>%s</div></div>'
            % (n, cuerpo, html.escape(ident), extra))


CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
@page { @bottom-center { content: counter(page); } }
* { box-sizing: border-box; }
body { font: 10.5pt/1.5 "Georgia","Times New Roman",serif; color:#111; margin:0;
       hyphens:auto; -webkit-hyphens:auto; }
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
th { background:#eee; }
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
.indice-gral ol { list-style:none; padding-left:0; }
.indice-gral > ol > li { margin:.5em 0; font-weight:bold; font-size:11pt; }
.indice-gral ul { list-style:none; padding-left:1.2em; font-weight:normal; font-size:9.5pt;
                  color:#444; }

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
.pfuente { font-size:7.5pt; color:#888; font-family:Helvetica,Arial,sans-serif; margin-top:2px; }
.resp { font-size:9pt; margin-top:3px; }
.errata { border-left:3px solid #111; background:#f0f0f0; padding:4px 8px; margin-top:4px;
          font-size:8.5pt; }
.pegada { border-left:3px solid #999; padding:3px 8px; margin-top:4px; font-size:8pt;
          color:#555; font-style:italic; }
@media screen { body { max-width:190mm; margin:0 auto; padding:16mm 10mm; background:#fff; } }
"""


def main():
    salida = sys.argv[1] if len(sys.argv) > 1 else "libro-general.html"
    excluir = {l.strip() for l in lee("banco/g8-especifico.txt").split("\n")
               if l.strip() and not l.startswith("#") and " · nº " in l}

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

        sub = re.findall(r"(?m)^## (.+)$", resto)
        indice_gral.append((i, titulo, sub))

        bloque = ['<section class="tema" id="tema-%d">' % i]
        bloque.append('<p class="rotulo">Tema %d del temario general</p>' % i)
        bloque.append("<h1>%s</h1>" % html.escape(titulo.split("·", 1)[-1].strip()))
        if ficha:
            bloque.append('<div class="ficha">%s</div>' % ficha)
        bloque.append(md.render(baja_titulos(resto, 0)))
        bloque.append('<section class="parte esquema"><h2>Esquema de repaso · tema %d</h2>%s</section>'
                      % (i, md.render(esquema)))
        if banco:
            ps = preguntas(banco, excluir)
            total_preg += len(ps)
            rot = ("Preguntas reales de examen · temas 2 y 3" if banco == "g2-g3"
                   else "Preguntas reales de examen · tema %d" % i)
            bloque.append('<section class="parte"><h2>%s</h2>' % rot)
            bloque.append("<p><i>%d preguntas de los cuadernillos de 2024. "
                          "Las respuestas, al final del volumen.</i></p>" % len(ps))
            bloque.append("".join(pinta_pregunta(n, i_, e)
                                  for n, (i_, e, _) in enumerate(ps, 1)))
            bloque.append("</section>")
            TEMAS[i - 1] = (base, banco, ps)
        bloque.append("</section>")
        partes.append("\n".join(bloque))

    # ── apéndice de respuestas ────────────────────────────────────────────────
    resp = ['<section class="tema"><p class="rotulo">Apéndice</p>'
            '<h1>Respuestas oficiales</h1>',
            "<p>La respuesta es la de la <b>plantilla oficial</b> de cada cuadernillo. "
            "Donde pone «sin plantilla» es que no se pudo emparejar. "
            "<b>Tres respuestas oficiales están mal</b> y van marcadas: el volumen enseña "
            "la norma, no la plantilla.</p>"]
    for i, t in enumerate(TEMAS, 1):
        if len(t) < 3:
            continue
        base, banco, ps = t
        rot = "Temas 2 y 3" if banco == "g2-g3" else "Tema %d" % i
        resp.append("<h2>%s</h2>" % rot)
        filas = []
        for n, (ident, _, r) in enumerate(ps, 1):
            aviso = ('<div class="errata"><b>Ojo:</b> %s</div>' % ERRATAS[ident]) if ident in ERRATAS else ""
            filas.append("<tr><td><b>%d</b></td><td><b>%s</b></td><td>%s%s</td></tr>"
                         % (n, html.escape(r), html.escape(ident), aviso))
        resp.append("<table><tr><th>N.º</th><th>Resp.</th><th>Cuadernillo</th></tr>%s</table>"
                    % "".join(filas))
    resp.append("</section>")

    ig = ["<li>%d. %s<ul>%s</ul></li>"
          % (i, html.escape(t.split("·", 1)[-1].strip()),
             "".join("<li>%s</li>" % html.escape(s) for s in sub[:14]))
          for i, t, sub in indice_gral]

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
<p><b>Las preguntas se imprimen tal como salieron del cuadernillo.</b> Son transcripciones de
PDF y traen sus costuras: en <b>33 de las 425</b> la transcripción dejó dos preguntas seguidas,
y van señaladas. No se recortan a ojo porque adivinar dónde acaba una y empieza la otra sería
inventar. Alguna, además, está clasificada en el tema que no le toca: la clasificación del banco
es por palabras clave y así está advertido en <code>banco/README.md</code>.</p>
<p><b>Nada de aquí se ha escrito de memoria.</b> Cada dato se ha leído en el texto consolidado
del BOE en su redacción a la fecha de corte, o en la fuente oficial que se cita en la
trazabilidad de cada tema.</p>
</section>

<section class="indice-gral"><h1>Índice general</h1><ol>{''.join(ig)}</ol></section>

{''.join(partes)}
{''.join(resp)}
</body></html>"""

    ruta = os.path.join(RAIZ, salida)
    open(ruta, "w", encoding="utf-8").write(doc)
    print("· %s · %d KB · %d temas · %d preguntas"
          % (salida, len(doc) // 1024, len(TEMAS), total_preg))


if __name__ == "__main__":
    main()
