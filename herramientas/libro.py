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

El mismo armazón sirve para los cuatro bloques —el general y los específicos de
Producción (Asistencia), Documentación e Información y Contenidos—, que se
diferencian en qué temas llevan, de qué carpeta salen y qué avisos hay que
imprimir con las respuestas. Todo eso está en
`BLOQUES`, y **no se duplica el código**: un volumen escrito dos veces se
desincroniza a la primera corrección.

Uso:  libro.py [general|produccion|documentacion|informacion] [salida.html]
      python3 herramientas/libro.py general     && python3 herramientas/pdf.py libro-general.html
      python3 herramientas/libro.py informacion && python3 herramientas/pdf.py libro-informacion.html
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

# Los cuatro bloques. Cada uno dice **de dónde salen sus temas**, **cómo se
# presenta el volumen** y **qué avisos van con las respuestas**. Cuando entre
# otra ocupación tipo, se añade una entrada aquí y no se toca nada más —los tres
# específicos que hay se dieron de alta así, sin tocar el armazón—.
#
# Un tema **puede no tener banco**: en Información y Contenidos, el del Real
# Decreto-ley 4/2018 y el de la Carta ética de la FIP no tienen ni una pregunta
# de examen. Se escribe `None` y el volumen los imprime sin juego, igual que el
# tema 2 del general, que comparte el suyo con el 3.
#
# En el general, los temas 2 y 3 comparten banco de preguntas, así que el juego
# va detrás del 3, que es el corto y el que depende del 2.
#
# «avisos» recoge lo que hay que imprimir junto a la respuesta de una pregunta
# concreta. En el general son **erratas de la plantilla oficial**: respuestas
# dadas por buenas que la norma desmiente. En el específico no hay ninguna
# errata de respuesta, pero sí **enunciados defectuosos**, que engañan igual y
# se avisan igual. Un volumen que copia la plantilla sin avisar enseña mal justo
# lo que el opositor va a memorizar.

ERRATAS_GENERAL = {
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

AVISOS_PRODUCCION = {
    "77_preguntas_produccion_asist · nº 78":
        "<b>El enunciado tiene los términos invertidos.</b> Pide la tecnología de «superponer una "
        "imagen real sobre el entorno virtual», y la realidad aumentada superpone <b>lo virtual "
        "sobre lo real</b>. La respuesta oficial es la única posible entre las cuatro opciones; "
        "quien intente razonar el enunciado al pie de la letra se bloquea.",
    "78_preguntas_produccion_asist_2_llamamiento · nº 29":
        "<b>El enunciado mezcla cine y televisión.</b> Pide lo que «la DCI 4K estandariza para "
        "televisión», y la iniciativa de cine digital estandariza <b>cine</b>: su 4K es "
        "<b>4 096 × 2 160</b>. El 4K de televisión es <b>3 840 × 2 160</b>, que es lo que el "
        "propio enunciado remata pidiendo, «en UHD 16:9».",
    "77_preguntas_produccion_asist · nº 61":
        "<b>El distractor c) no es falso.</b> La Recomendación UIT-R BT.2100-1 incluye <b>24</b> "
        "y 24/1,001 entre sus frecuencias de trama de televisión. Lo que decide la pregunta es la "
        "palabra <b>«tradicionalmente»</b>: las 24 imágenes por segundo vienen del cine "
        "fotoquímico.",
    "77_preguntas_produccion_asist · nº 81":
        "<b>El enunciado fecha mal una ley y cita otra derogada.</b> La ley de televisión privada "
        "es la <b>Ley 10/1988, de 3 de mayo</b> —el día y el mes del enunciado coinciden; el año, "
        "no—; y la <b>Ley 7/2010</b> está derogada por la disposición derogatoria única de la "
        "Ley 13/2022.",
    "77_preguntas_produccion_asist · nº 44":
        "<b>La opción correcta dice «marca comercial alemana».</b> Lo alemán está comprobado: el "
        "informe de ensayo de seguridad fotobiológica del Titan Tube identifica al solicitante "
        "como <b>Astera LED Technology GmbH, de Múnich</b>.",
}

AVISOS_DOCUMENTACION = {
    "09_preguntas_documentacion · nº 11":
        "<b>La opción correcta empieza un día tarde.</b> El Real Decreto 1673/2010 se publicó en el "
        "«BOE» núm. 295, de <b>4 de diciembre de 2010</b>, y entró en vigor «en el instante de su "
        "publicación»: el estado de alarma corrió desde <b>el 4</b>, no desde el 5. La fecha final "
        "sí es literal —el Real Decreto 1717/2010 lo prorroga «hasta las 24 horas del día 15 de "
        "enero de 2011»—, y la opción sigue siendo la única posible de las cuatro.",
    "09_preguntas_documentacion · nº 47":
        "<b>El enunciado desarrolla las siglas y la norma no.</b> La norma ECMA-319, que es la que "
        "define el formato, se titula «Data Interchange on 12,7 mm 384-Track <b>Magnetic Tape "
        "Cartridges</b> – Ultrium-1 Format» y usa las siglas sin explicarlas. El desarrollo entre "
        "paréntesis es del tribunal; lo que la norma sí dice es que es <b>cinta magnética</b>.",
}


AVISOS_INFORMACION = {
    "31_preguntas_iyc · nº 77":
        "<b>La respuesta oficial y el INE no dicen lo mismo.</b> La plantilla da <b>11,4 %</b>; la "
        "nota de prensa de la EPA del segundo trimestre de 2024, de 26 de julio, publica "
        "<b>11,27 %</b>, y se comprueba sola: «11,27 % este trimestre, 1,02 puntos menos que en el "
        "anterior», y 11,27 + 1,02 = 12,29, la tasa del primer trimestre. <b>De las cuatro "
        "opciones, la de la plantilla sigue siendo la única cercana</b>; el temario enseña la "
        "cifra del INE y deja dicho que la oficial es otra.",
    "33_preguntas_iyc_2_llamamiento · nº 6":
        "<b>El enunciado nombra mal el organismo.</b> Dice «Centro de Investigaciones Científicas "
        "(CIS)». El CIS es el <b>Centro de Investigaciones Sociológicas</b>; el de Investigaciones "
        "Científicas es el <b>CSIC</b>, otro organismo con otra adscripción. No cambia la "
        "respuesta —las siglas sólo pueden ser el Sociológico—.",
    "31_preguntas_iyc · nº 20":
        "<b>El enunciado llama al documento por el título de otro.</b> Dice «Código de "
        "Autorregulación sobre contenidos televisivos e infancia», que es el <b>acuerdo sectorial "
        "de 9 de diciembre de 2004</b>. El documento del Anexo 2 es el <b>de RTVE, de 23 de julio "
        "de 2010</b>, que cita a aquél como «el más directo precedente de las presentes normas». "
        "<b>La respuesta no depende de cuál se lea</b>: la cifra está en el de RTVE con esas "
        "mismas palabras.",
    "31_preguntas_iyc · nº 57":
        "<b>Mismo defecto que en la otra pregunta del tema</b>: el enunciado usa el título del "
        "acuerdo sectorial de 2004 para preguntar por el código de RTVE de 2010. La respuesta se "
        "verifica en el documento que el programa manda estudiar.",
    "33_preguntas_iyc_2_llamamiento · nº 63":
        "<b>La cifra de la respuesta no está en la directiva</b>, y el programa la fecha mal. La "
        "norma dice <b>20 % del período</b>; los 144 minutos son esa proporción sobre doce horas, "
        "así que quien busque «144» en el texto no lo encontrará. Y el Anexo 2 fecha la directiva "
        "el <b>28 de noviembre de 2018</b>, que es la fecha del <b>Diario Oficial</b>: la "
        "directiva es de <b>14 de noviembre</b>.",
    "33_preguntas_iyc_2_llamamiento · nº 82":
        "<b>La respuesta era correcta en 2024 y hoy no lo sería.</b> La plantilla da <b>siete</b> "
        "países de la Unión sin el euro, y así era cuando se examinó; <b>la página oficial de hoy "
        "dice seis</b>, porque la zona del euro ha crecido desde entonces. Se estudia la de 2024 "
        "y se sabe por qué cambia.",
}


BLOQUES = {
    "general": dict(
        carpeta="general",
        rotulo="Temario general",
        titulo="Temario general",
        subtitulo="Los ocho temas comunes a Producción (Asistencia),<br>"
                  "Documentación e Información y Contenidos",
        pie="Oposiciones RTVE – Temario General",
        avisos=ERRATAS_GENERAL,
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[
            ("01-constitucion-espanola", "g1"),
            ("02-ley-17-2006", None),
            ("03-ley-5-2017", "g2-g3"),
            ("04-ley-8-2009", "g4"),
            ("05-convenio-colectivo", "g5"),
            ("06-igualdad", "g6"),
            ("07-ley-13-2022", "g7"),
            ("08-ley-31-1995", "g8"),
        ],
        aviso_respuestas="<b>Tres respuestas oficiales están mal</b> y van avisadas debajo de su "
                         "tabla: el volumen enseña la norma, no la plantilla.",
        aviso_portada="<p><b>Tres respuestas oficiales de 2024 están mal.</b> Van marcadas una a "
                      "una en el apéndice, con el precepto que las desmiente. El temario enseña "
                      "la norma, no la plantilla.</p>",
    ),
    "produccion": dict(
        carpeta="produccion",
        rotulo="Temario específico · Producción (Asistencia)",
        titulo="Temario específico",
        subtitulo="Los diecisiete temas de <b>Producción (Asistencia)</b>",
        pie="Oposiciones RTVE – Producción (Asistencia)",
        avisos=AVISOS_PRODUCCION,
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "produccion-%02d" % n) for n, base in [
            (1, "la-produccion"), (2, "propiedad-intelectual"), (3, "el-guion"),
            (4, "el-desglose"), (5, "localizacion"), (6, "plan-y-orden-de-trabajo"),
            (7, "equipos-humanos"), (8, "formatos-y-soportes"),
            (9, "escenografia-e-iluminacion"), (10, "imagen-y-sonido"),
            (11, "transmision-de-senal"), (12, "el-estudio"),
            (13, "equipos-de-exteriores"), (14, "documentacion-internacional"),
            (15, "organismos"), (16, "gestion-de-servicios"),
            (17, "proteccion-de-datos"),
        ]],
        aviso_respuestas="<b>Ninguna respuesta oficial de este bloque está mal</b>, pero "
                         "<b>cinco enunciados sí lo están</b> —uno con los términos invertidos, "
                         "otro que mezcla cine y televisión, otro con una ley mal fechada—: van "
                         "avisados debajo de su tabla.",
        aviso_portada="<p><b>Ninguna respuesta oficial de este bloque está mal, pero cinco "
                      "enunciados sí.</b> Uno invierte los términos, otro mezcla cine y "
                      "televisión, otro fecha mal una ley y cita otra derogada, y en otro el "
                      "distractor descartado <i>no es falso</i>. Van marcados uno a uno en el "
                      "apéndice. El temario contesta lo que corrige el tribunal <b>y dice dónde "
                      "está la costura</b>.</p>",
    ),
    "documentacion": dict(
        carpeta="documentacion",
        rotulo="Temario específico · Documentación",
        titulo="Temario específico",
        subtitulo="Los seis temas de <b>Documentación</b>",
        pie="Oposiciones RTVE – Documentación",
        avisos=AVISOS_DOCUMENTACION,
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), "documentacion-%02d" % n) for n, base in [
            (1, "historia-de-rtve"), (2, "documentacion-y-tecnologias"),
            (3, "internet"), (4, "inteligencia-artificial"),
            (5, "centros-de-documentacion"), (6, "cultura-y-actualidad"),
        ]],
        aviso_respuestas="<b>Ninguna respuesta oficial de este bloque está mal</b>, pero "
                         "<b>dos enunciados cojean</b> —uno fecha el estado de alarma un día "
                         "tarde, otro desarrolla unas siglas que la norma no desarrolla—: van "
                         "avisados debajo de su tabla.",
        aviso_portada="<p><b>Ninguna respuesta oficial de este bloque está mal.</b> Lo que sí "
                      "hay es <b>desigualdad de fuentes</b>, y el temario la dice: hay un tema "
                      "con las diez preguntas verificadas en documento y otro con cuarenta "
                      "preguntas de las que <b>quince</b> tienen documento y <b>veinticinco</b> "
                      "se apoyan sólo en la plantilla. Cada respuesta lleva <b>el nivel de su "
                      "fuente</b> escrito al lado.</p>",
    ),
    "informacion": dict(
        carpeta="informacion",
        rotulo="Temario específico · Información y Contenidos",
        titulo="Temario específico",
        subtitulo="Los diez temas de <b>Información y Contenidos</b>",
        pie="Oposiciones RTVE – Información y Contenidos",
        avisos=AVISOS_INFORMACION,
        clase_aviso="errata",
        rotulo_aviso="Ojo con la",
        temas=[("%02d-%s" % (n, base), banco) for n, base, banco in [
            (1, "actualidad", "informacion-01"),
            (2, "union-europea", "informacion-02"),
            (3, "instituciones", "informacion-03"),
            (4, "codigo-menores", "informacion-04"),
            (5, "rdl-4-2018", None),
            (6, "manual-de-estilo", "informacion-06"),
            (7, "directiva-2018-1808", "informacion-07"),
            (8, "resolucion-parlamento-europeo", "informacion-08"),
            (9, "informe-unesco", "informacion-09"),
            (10, "carta-etica-fip", None),
        ]],
        aviso_respuestas="<b>Ninguna respuesta oficial de este bloque se puede dar por mal "
                         "contestada</b>, pero <b>una discrepa de su fuente estadística</b> y "
                         "<b>cuatro enunciados están defectuosos</b> —uno nombra mal un "
                         "organismo, dos nombran mal el documento, otro apoya la respuesta en una "
                         "cifra que la norma no escribe—: van avisados debajo de su tabla.",
        aviso_portada="<p><b>Este bloque tiene dos temas sin una sola pregunta de examen</b> —el "
                      "del Real Decreto-ley 4/2018 y el de la Carta ética de la FIP—, y se "
                      "escriben igual, contra la norma y el documento, porque el programa los "
                      "manda. <b>Y tiene el tema más preguntado del proyecto</b>: ciento "
                      "veintiuna preguntas de actualidad, que no se estudian en una norma sino "
                      "que se comprueban dato a dato. <b>Cada respuesta lleva el nivel de su "
                      "fuente al lado</b>, y las que sólo se apoyan en la plantilla lo dicen. "
                      "<b>Ocho enunciados salen descolocados en el papel</b> —las cuatro letras "
                      "seguidas y después los textos—: es de la maquetación de los cuadernillos, "
                      "no cambia ninguna respuesta, y aquí las opciones van en su orden.</p>",
    ),
}

# La portada dice «Ocho temas», no «8 temas»: en una portada las cifras bajas se
# escriben con letra. Con dos bloques hay que generarlo, y no hace falta más que
# los números que este temario puede tener.
LETRA = {2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete",
         8: "Ocho", 9: "Nueve", 10: "Diez", 11: "Once", 17: "Diecisiete"}


def con_letra(n):
    return LETRA.get(n, str(n))


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
    argv = sys.argv[1:]
    clave = argv[0] if argv and argv[0] in BLOQUES else "general"
    argv = argv[1:] if argv and argv[0] in BLOQUES else argv
    B = BLOQUES[clave]
    salida = argv[0] if argv else "libro-%s.html" % clave
    TEMAS = [list(x) for x in B["temas"]]

    partes, indice_gral, total_preg = [], [], 0
    for i, (base, banco) in enumerate(B["temas"], 1):
        crudo = sin_marcas(lee("temas/%s/%s.md" % (B["carpeta"], base)))
        titulo = re.search(r"(?m)^# (.+)$", crudo).group(1)
        cuerpo = re.sub(r"(?m)^# .+$\n", "", crudo, count=1)
        # fuera el índice del propio tema: el volumen lleva el suyo
        cuerpo = re.sub(r"## Índice\n.*?(?=\n## )", "", cuerpo, flags=re.S)
        ficha, resto = "", cuerpo
        mt = re.match(r"\s*(\|.*?\|)\n\n", cuerpo, re.S)
        if mt:
            ficha = md.render(mt.group(1))
            resto = cuerpo[mt.end():]

        esquema = sin_marcas(lee("esquemas/%s/%s.md" % (B["carpeta"], base)))
        esquema = re.sub(r"(?m)^# .+$\n", "", esquema, count=1)
        esquema = re.sub(r"## Índice\n.*?(?=\n## )", "", esquema, flags=re.S)

        resto, entradas = numera(resto, i)
        indice_gral.append((i, titulo, entradas))

        bloque = ['<section class="tema" id="tema-%d">' % i]
        bloque.append('<p class="rotulo">%s</p>' % html.escape(B["rotulo"]))
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
            TEMAS[i - 1] = [base, banco, ps]
        bloque.append("</section>")
        partes.append("\n".join(bloque))

    # ── apéndice de respuestas ────────────────────────────────────────────────
    resp = ['<section class="tema"><p class="rotulo">Apéndice</p>'
            '<h1>Respuestas oficiales</h1>',
            "<p>La respuesta es la de la <b>plantilla oficial</b> del examen, y el número "
            "es el que la pregunta lleva impreso en su tema. "
            + B["aviso_respuestas"] + "</p>"]
    for i, t in enumerate(TEMAS, 1):
        if len(t) < 3:
            continue
        base, banco, ps = t
        rot = "Temas 2 y 3" if banco == "g2-g3" else "Tema %d" % i
        resp.append("<h2>%s</h2>" % rot)
        # la respuesta se busca por el número con el que la pregunta está impresa;
        # el cuadernillo del que salió ya no se imprime, que al opositor no le dice nada
        sueltas = [(n, r) for n, (_, _, r) in enumerate(ps, 1)]
        erratas = [(n, B["avisos"][ident]) for n, (ident, _, _) in enumerate(ps, 1)
                   if ident in B["avisos"]]
        filas, POR_FILA = [], 10
        for a in range(0, len(sueltas), POR_FILA):
            trozo = sueltas[a:a + POR_FILA]
            filas.append("<tr>%s</tr><tr>%s</tr>"
                         % ("".join("<th>%d</th>" % n for n, _ in trozo),
                            "".join("<td>%s</td>" % html.escape(r) for _, r in trozo)))
        resp.append('<table class="claves">%s</table>' % "".join(filas))
        for n, texto in erratas:
            resp.append('<div class="%s"><b>%s %d:</b> %s</div>'
                        % (B["clase_aviso"], B["rotulo_aviso"], n, texto))
    resp.append("</section>")

    ig = []
    for i, t, entradas in indice_gral:
        ig.append(linea_indice(0, "TEMA %d –" % i, t.split("·", 1)[-1].strip(),
                               "tema-%d" % i))
        for nivel, numero, titulo, ancla in entradas:
            ig.append(linea_indice(nivel, numero, titulo, ancla))

    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<!-- pie: {B["pie"]} -->
<title>{B["titulo"]} · Oposiciones RTVE</title><style>{CSS}</style></head><body>
<section class="portada-vol">
  <p class="rotulo">Oposiciones RTVE · convocatorias 1/2022 y 3/2022</p>
  <h1>{B["titulo"]}</h1>
  <p class="sub">{B["subtitulo"]}</p>
  <div class="meta">
    Redacción vigente a <b>{CORTE}</b><br>
    {con_letra(len(TEMAS))} temas · {con_letra(len(TEMAS)).lower()} esquemas de repaso · <b>{total_preg}</b> preguntas reales de examen<br>
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
{B["aviso_portada"]}
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
    sueltas = set(B["avisos"]) - {i for t in TEMAS if len(t) > 2 for i, _, _ in t[2]}
    if sueltas:
        print("  ! erratas sin pregunta a la que pegarse: %s" % ", ".join(sorted(sueltas)))

    ruta = os.path.join(RAIZ, salida)
    open(ruta, "w", encoding="utf-8").write(doc)
    print("· %s · %d KB · %d temas · %d preguntas"
          % (salida, len(doc) // 1024, len(TEMAS), total_preg))


if __name__ == "__main__":
    main()
