#!/usr/bin/env python3
"""Arma el banco de preguntas del bloque **específico**, a mano y con acta.

El bloque común se clasifica por palabras clave: las materias son siete leyes y
cada una tiene un vocabulario propio. El específico no se deja: sus preguntas
hablan de *beauty shot*, tronera, semoviente, SMPTE 2110 o carné ATA, y muchas
podrían caer en dos temas a la vez —una pregunta sobre el desglose de un guion
toca el tema 3 y el 4—. Clasificar eso por expresiones regulares no da un
reparto discutible: da un reparto **falso que nadie va a revisar**.

Así que aquí el reparto se escribe a mano, pregunta a pregunta, en
`banco/especifico-<ocupacion>.tsv`, con una columna de motivo. Este script solo
lo aplica. Y avisa de dos cosas que, si no se avisan, no dan ningún error:

  · **Filas huérfanas**: una fila que ya no casa con ninguna pregunta es una
    clasificación que dejó de aplicarse sin que nadie se entere.
  · **Preguntas sin fila**: las que están en el cuadernillo, dentro del rango
    del bloque específico, y todavía no se han repartido. Ésa es la cuenta de
    lo que falta, y es la que no aparece sola.

Uso:  banco_especifico.py produccion_asist
      banco_especifico.py documentacion
      banco_especifico.py informacion
"""
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calibrar import preguntas, clasifica, MATERIAS
from banco import plantilla, sin_pie, sin_ecos, reclasificadas

DIR = "convocatoria/examenes"
SALIDA = "banco"

# La ocupación no siempre se llama en el fichero como se llama en el temario:
# los cuadernillos de Información y Contenidos se nombran `..._preguntas_iyc...`
# y el acta y el banco, `informacion`. Sin esta tabla la ocupación no casa con
# ningún cuadernillo y el script no falla: reparte cero preguntas y lo dice sin
# alarma, que es la forma más silenciosa de dar un bloque por hecho
MARCA = {"informacion": "iyc", "gestion-administrativa": "gea",
         "produccion-asistencia": "produccion_asist"}

# **Y lo mismo pasa con «Realización»**: los cuadernillos `66_preguntas_realizacion_a`
# y `68_..._b` son de la ocupación tipo de **Realización**, que tiene su propio
# Anexo 2 y no está en este proyecto; los de **Realización (Asistencia)** son el
# `60` y el `62`. Sin la regla, el banco de esta última se llevaba las 240
# preguntas de aquélla y las contaba como pendientes: decía «209 repartidas de
# 439, quedan 230 sin clasificar» y no faltaba ninguna.
#
# **Dos ocupaciones tipo se llaman «Producción».** Una es *Producción
# (Asistencia)*, con sus cuadernillos `77_preguntas_produccion_asist` y
# `78_..._2_llamamiento`; la otra es *Producción* a secas, con el
# `81_preguntas_produccion`. Buscar por subcadena no las separa: «produccion»
# está en los tres nombres, así que el banco de la primera se llevaba también
# las sesenta y seis preguntas de la segunda **y las contaba como pendientes**,
# sin dar ningún error. Cuando el nombre no basta, la ocupación dice **qué
# cuadernillos son suyos**, por su nombre exacto.
SOLO = {"produccion": ("81_preguntas_produccion",),
        "realizacion": ("60_preguntas_realizacion_asist",
                        "62_preguntas_realizacion_asist_2_llamamiento"),
        # Realización a secas —Realización Televisión— tiene sus dos propios
        # llamamientos, el `66` y el `68`, y su Anexo 2 es otro
        "realizacion-tv": ("66_preguntas_realizacion_a",
                           "68_preguntas_realizacion_b"),
        "informacion-grafica": ("29_preguntas_igyciys",),
        "edicion-montaje": ("11_preguntas_emypa",),
        "montaje-equipos": ("58_preguntas_mont_equip_audio",),
        "sonido": ("85_preguntas_sonido",),
        # TESE trae **dos cuadernillos de tamaño muy distinto**: el `70`, de 96
        # preguntas, y el `71`, que sus propias instrucciones describen como
        # «30 preguntas (25 principales más 5 de reserva)». No es un fallo de
        # extracción: es un examen más corto, y se lee entero
        "tese": ("70_preguntas_tese_a", "71_preguntas_tese_b")}


def reparto(ocupacion):
    """{(origen, nº): (tema, motivo)} leído del acta de clasificación."""
    ruta = os.path.join(SALIDA, "especifico-%s.tsv" % ocupacion)
    fuera, enteros = {}, {}
    for linea in open(ruta, encoding="utf-8"):
        if linea.startswith("#") or not linea.strip():
            continue
        c = linea.rstrip("\n").split("\t")
        if c[0] == "origen":
            continue
        motivo = c[3] if len(c) > 3 else ""
        # un `*` en el número descarta el cuadernillo entero. Hay cuadernillos
        # que llevan la marca de la ocupación en el nombre y no son de este
        # temario —el de Radio Clásica, con la ocupación en el nombre y el
        # temario de otro Anexo 2—, y descartarlos pregunta a pregunta sería
        # llenar el acta de cien filas iguales. Descartarlos en el script, en
        # cambio, dejaría el motivo fuera del acta, que es donde se busca
        if c[1].strip() == "*":
            enteros[c[0]] = motivo
            continue
        fuera[(c[0], int(c[1]))] = (c[2], motivo)
    return fuera, enteros


def cuadernillos(ocupacion):
    """[(cuadernillo, plantilla)] de la ocupación, por el nombre del fichero."""
    ocupacion = MARCA.get(ocupacion, ocupacion)
    fuera = []
    for f in sorted(os.listdir(DIR)):
        if not f.endswith(".txt") or "_preguntas_" not in f:
            continue
        if ocupacion in SOLO:
            if re.sub(r"\.ocr$", "", f[:-4]) not in SOLO[ocupacion]:
                continue
        elif ocupacion not in f:
            continue
        # un cuadernillo con la fuente incrustada sin tabla de caracteres tiene
        # **dos ficheros**: el `.txt` ilegible —«(cid:12)(cid:13)…»— y la
        # transcripción por OCR al lado. Leer los dos cuenta el mismo examen dos
        # veces, y lo hace **sin dar ningún error**: el ilegible aporta unas
        # cuantas «preguntas» que no casan con ninguna fila del acta y engordan
        # la cifra de pendientes. Le pasó a Gestión, que daba 63 sin clasificar
        # sobre un cuadernillo de 108. Vale la misma regla que en `banco.py`:
        # donde hay OCR, el original no se lee
        if not f.endswith(".ocr.txt") and os.path.exists(
                os.path.join(DIR, f[:-4] + ".ocr.txt")):
            continue
        base = f[:-4]
        # la plantilla es el fichero siguiente por número: 77 -> 79 aquí no vale,
        # así que se busca por el sufijo del nombre, que es el que las empareja
        # y la cola se calcula **sin el sufijo `.ocr`**: la plantilla se llama
        # `16_plantilla_de_respuestas_gestion` y el cuadernillo leído por OCR,
        # `15_preguntas_gestion.ocr`. Sin quitarlo no casaban, y el banco entero
        # de Gestión salía con «sin plantilla» en las 81 preguntas —**sin dar
        # ningún error**, que es como se pierde un examen completo—
        cola = re.sub(r"\.ocr$", "", base).split("_preguntas_", 1)[1]
        plant = [g for g in sorted(os.listdir(DIR))
                 if g.endswith(".txt") and "respuestas" in g
                 and g.split("respuestas_", 1)[-1][:-4] == cola]
        fuera.append((os.path.join(DIR, f),
                      os.path.join(DIR, plant[0]) if plant else None))
    return fuera


def main(ocupacion, titulos):
    # el acta se nombra por la ocupación corta: los ficheros dicen
    # «produccion_asist» y el acta, «produccion»
    corta = ocupacion.split("_")[0]
    filas, enteros = reparto(corta)
    comun = reclasificadas()
    portema = defaultdict(list)
    usadas, sinfila, descartados = set(), [], []
    for cuad, plant in cuadernillos(ocupacion):
        # el acta nombra el cuadernillo, no el fichero: `17_preguntas_...` y no
        # `17_preguntas_....ocr`. Sin quitar el sufijo, un cuadernillo leído por
        # OCR no casaba con su fila de descarte y **volvía a entrar entero**
        nombre = re.sub(r"\.ocr$", "", os.path.basename(cuad)[:-4])
        if nombre in enteros:
            descartados.append(nombre)
            continue
        respuestas = plantilla(plant) if plant else {}
        origen = re.sub(r"\.ocr$", "", os.path.basename(cuad)[:-4])
        for n, cuerpo in preguntas(open(cuad, encoding="utf-8").read()):
            clave = (origen, n)
            if clave not in filas:
                # las del bloque común no son de este banco: van en el del
                # temario general, y contarlas aquí como pendientes daría una
                # cifra de trabajo que no existe. Ojo: no basta con la
                # clasificación por palabras clave. Una pregunta del bloque
                # común repartida **a mano** en `reclasificadas.tsv` no la
                # reconoce ninguna palabra clave, así que seguía contando como
                # pendiente del específico: trabajo que ya estaba hecho y que
                # esta cuenta pedía dos veces
                if clasifica(cuerpo, MATERIAS) is None and clave not in comun:
                    sinfila.append(clave)
                continue
            usadas.add(clave)
            tema = filas[clave][0]
            cuerpo = "".join(c for c in cuerpo if c == "\n" or c >= " ")
            cuerpo = re.sub(r"\n{2,}", "\n", sin_ecos(sin_pie(cuerpo))).strip()
            portema[tema].append((origen, n, respuestas.get(n), cuerpo))

    total = 0
    for tema, items in sorted(portema.items()):
        ruta = os.path.join(SALIDA, "%s-%s.md" % (corta, tema))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("# %s\n\n" % titulos.get(tema, tema))
            fh.write("%d preguntas reales sacadas de los cuadernillos de octubre y "
                     "noviembre de 2024.\nLa respuesta es la de la plantilla oficial; "
                     "donde pone «sin plantilla» es que\nno se pudo emparejar.\n\n"
                     % len(items))
            for origen, n, letra, cuerpo in items:
                fh.write("---\n\n**%s · nº %d · respuesta: %s**\n\n```\n%s\n```\n\n"
                         % (origen, n, letra or "sin plantilla", cuerpo))
        print("%-46s %3d preguntas -> %s" % (titulos.get(tema, tema), len(items), ruta))
        total += len(items)

    print()
    print("del bloque específico: %d repartidas de %d; quedan %d sin clasificar"
          % (total, total + len(sinfila), len(sinfila)))
    for d in descartados:
        print("  · cuadernillo descartado entero: %s (%s)" % (d, enteros[d]))
    huerfanas = sorted(set(filas) - usadas)
    huerfanas = [h for h in huerfanas if h[0] not in enteros]
    if huerfanas:
        print()
        print("! %d filas del acta no casan con ninguna pregunta:" % len(huerfanas))
        for h in huerfanas:
            print("  ! %s nº %d" % h)


# Los títulos con los que se encabeza cada fichero del banco. Uno por ocupación,
# porque el reparto es distinto y los temas no se llaman igual.
TITULOS = {
 "sonido": {
    "01": "Sonido · Tema 1 · Electricidad y electrónica básicas",
    "02": "Sonido · Tema 2 · Principios físicos del sonido y la audición",
    "03": "Sonido · Tema 3 · Música, instrumentos e historia de la música",
    "04": "Sonido · Tema 4 · Acústica arquitectónica",
    "05": "Sonido · Tema 5 · Micrófonos, soportes y accesorios",
    "06": "Sonido · Tema 6 · Señales de contribución",
    "07": "Sonido · Tema 7 · Mezcla y tratamiento del sonido",
    "08": "Sonido · Tema 8 · Postproducción, efectos sonoros y estación de\n          trabajo",
    "09": "Sonido · Tema 9 · Grabación de sonido",
    "10": "Sonido · Tema 10 · Sonorización: altavoces y amplificadores",
    "11": "Sonido · Tema 11 · Líneas y conexiones",
    "12": "Sonido · Tema 12 · El sonido en la radio y la televisión",
    "13": "Sonido · Tema 13 · Radiofrecuencia",
    "14": "Sonido · Tema 14 · Medición y sonoridad",
    "15": "Sonido · Tema 15 · Audio multicanal",
    "16": "Sonido · Tema 16 · El audio sobre redes de datos",
    "17": "Sonido · Tema 17 · Audio sobre protocolos digitales",
 },
 "tese": {
    "01": "TESE · Tema 1 · Conceptos básicos de electricidad",
    "02": "TESE · Tema 2 · Componentes electrónicos",
    "03": "TESE · Tema 3 · Electrónica de potencia",
    "04": "TESE · Tema 4 · Amplificadores operacionales",
    "05": "TESE · Tema 5 · Electrónica digital",
    "06": "TESE · Tema 6 · Circuitos integrados y secuenciales",
    "07": "TESE · Tema 7 · Memorias, lógica programable y microprocesadores",
    "08": "TESE · Tema 8 · La señal audiovisual y sus sincronismos",
    "09": "TESE · Tema 9 · La señal audiovisual sobre redes",
    "10": "TESE · Tema 10 · Equipos utilizados en televisión y radio",
    "11": "TESE · Tema 11 · Control de iluminación escénica",
    "12": "TESE · Tema 12 · Comunicaciones y redes",
    "13": "TESE · Tema 13 · Equipos de medida y control",
    "14": "TESE · Tema 14 · Medidas de la señal de vídeo, audio y RF",
    "15": "TESE · Tema 15 · Mantenimiento preventivo y correctivo",
    "16": "TESE · Tema 16 · Mantenimiento en televisión",
    "17": "TESE · Tema 17 · Seguridad en instalaciones técnicas",
 },
 "realizacion-tv": {
    "01": "Realización · Tema 1 · La música",
    "02": "Realización · Tema 2 · Las artes escénicas",
    "03": "Realización · Tema 3 · La literatura",
    "04": "Realización · Tema 4 · Las artes plásticas y la fotografía",
    "05": "Realización · Tema 5 · El cine",
    "06": "Realización · Tema 6 · La televisión: historia, cadenas y programas",
    "07": "Realización · Tema 7 · Géneros y formatos televisivos",
    "08": "Realización · Tema 8 · El guion",
    "09": "Realización · Tema 9 · Organización general de la producción",
    "10": "Realización · Tema 10 · Funciones del realizador y los puestos "
          "técnico-artísticos",
    "11": "Realización · Tema 11 · Conocimientos básicos de televisión: la "
          "señal y su control",
    "12": "Realización · Tema 12 · Formatos y procesos de registro, captación y "
          "reproducción",
    "13": "Realización · Tema 13 · Lenguaje técnico y narrativo",
    "14": "Realización · Tema 14 · La cámara: accesorios y posibilidades",
    "15": "Realización · Tema 15 · El mezclador",
    "16": "Realización · Tema 16 · La iluminación",
    "17": "Realización · Tema 17 · El sonido",
    "18": "Realización · Tema 18 · Producción de programas directos y grabados",
    "19": "Realización · Tema 19 · La puesta en escena",
    "20": "Realización · Tema 20 · Postproducción",
    "21": "Realización · Tema 21 · Producción y realización online. Transmedia",
    "22": "Realización · Tema 22 · Derechos de autor y propiedad intelectual",
 },
 "informacion-grafica": {
    "01": "Información Gráfica · Tema 1 · Principios básicos: la luz, el color "
          "y la percepción visual",
    "02": "Información Gráfica · Tema 2 · Señales y formatos: de la señal a la "
          "medida",
    "03": "Información Gráfica · Tema 3 · La cámara de vídeo y el sensor",
    "04": "Información Gráfica · Tema 4 · Los objetivos, los filtros y los "
          "accesorios",
    "05": "Información Gráfica · Tema 5 · Soportes de cámara y estabilización",
    "06": "Información Gráfica · Tema 6 · El sonido en reportaje (ENG) y "
          "producción ligera",
    "07": "Información Gráfica · Tema 7 · La iluminación en ENG y producción "
          "ligera",
    "08": "Información Gráfica · Tema 8 · Control de cámara y ajuste de imagen",
    "09": "Información Gráfica · Tema 9 · Envíos, directos y cámaras "
          "robotizadas",
    "10": "Información Gráfica · Tema 10 · Lenguaje audiovisual",
    "11": "Información Gráfica · Tema 11 · Teoría de la información "
          "audiovisual",
 },
 "edicion-montaje": {
    "01": "Edición, Montaje y Procesos Audiovisuales · Tema 1 · Conocimientos "
          "básicos de electrónica e informática aplicadas",
    "02": "Edición, Montaje y Procesos Audiovisuales · Tema 2 · Colorimetría y "
          "el color en televisión",
    "03": "Edición, Montaje y Procesos Audiovisuales · Tema 3 · Conceptos "
          "básicos de sonido",
    "04": "Edición, Montaje y Procesos Audiovisuales · Tema 4 · Tratamiento "
          "digital de la señal de televisión",
    "05": "Edición, Montaje y Procesos Audiovisuales · Tema 5 · Soportes, "
          "formatos, grabación e ingesta",
    "06": "Edición, Montaje y Procesos Audiovisuales · Tema 6 · Equipos de "
          "medida y control",
    "07": "Edición, Montaje y Procesos Audiovisuales · Tema 7 · Edición de "
          "vídeo: Avid Media Composer",
    "08": "Edición, Montaje y Procesos Audiovisuales · Tema 8 · Edición en "
          "directo y retransmisiones (EVS)",
    "09": "Edición, Montaje y Procesos Audiovisuales · Tema 9 · Incrustaciones, "
          "grafismo y postproducción",
    "10": "Edición, Montaje y Procesos Audiovisuales · Tema 10 · Lenguaje "
          "audiovisual y teoría del montaje",
 },
 "montaje-equipos": {
    "01": "Montaje de Equipos Audiovisuales · Tema 1 · Instalaciones de "
          "televisión y unidades móviles",
    "02": "Montaje de Equipos Audiovisuales · Tema 2 · Profesionales, roles y "
          "operativa de una grabación",
    "03": "Montaje de Equipos Audiovisuales · Tema 3 · Las cámaras: tipos, "
          "elementos externos y manejo seguro",
    "04": "Montaje de Equipos Audiovisuales · Tema 4 · Cabezas de cámara y "
          "soportes: instalación y nivelado",
    "05": "Montaje de Equipos Audiovisuales · Tema 5 · Conectores, cables y "
          "elementos de conexión",
    "06": "Montaje de Equipos Audiovisuales · Tema 6 · Sonido: micrófonos, "
          "altavoces y soportes",
    "07": "Montaje de Equipos Audiovisuales · Tema 7 · Maquinaria para el "
          "movimiento de cámaras",
    "08": "Montaje de Equipos Audiovisuales · Tema 8 · La cabeza caliente",
    "09": "Montaje de Equipos Audiovisuales · Tema 9 · Montaje de equipos en "
          "estudios y exteriores",
    "10": "Montaje de Equipos Audiovisuales · Tema 10 · Asistencia a la "
          "operación de cámara",
 },
 "realizacion": {
    "01": "Realización (Asistencia) · Tema 1 · Géneros y formatos televisivos",
    "02": "Realización (Asistencia) · Tema 2 · El guion",
    "03": "Realización (Asistencia) · Tema 3 · Organización general de la producción",
    "04": "Realización (Asistencia) · Tema 4 · Decorados: interpretación de planos "
          "y perspectivas",
    "05": "Realización (Asistencia) · Tema 5 · La tecnología en el ámbito de la "
          "realización",
    "06": "Realización (Asistencia) · Tema 6 · Lenguaje técnico y narrativo",
    "07": "Realización (Asistencia) · Tema 7 · La cámara, accesorios y posibilidades",
    "08": "Realización (Asistencia) · Tema 8 · La iluminación",
    "09": "Realización (Asistencia) · Tema 9 · El sonido",
    "10": "Realización (Asistencia) · Tema 10 · El mezclador de vídeo",
    "11": "Realización (Asistencia) · Tema 11 · El estudio: controles y plató",
    "12": "Realización (Asistencia) · Tema 12 · Las unidades móviles",
    "13": "Realización (Asistencia) · Tema 13 · La asistencia en grabación",
    "14": "Realización (Asistencia) · Tema 14 · La retransmisión",
    "15": "Realización (Asistencia) · Tema 15 · La emisión: pantallas, servidores "
          "y grafismo",
    "16": "Realización (Asistencia) · Tema 16 · Realidad aumentada, decorados "
          "virtuales y producción online",
    "17": "Realización (Asistencia) · Tema 17 · La asistencia en plató. Regiduría",
    "18": "Realización (Asistencia) · Tema 18 · Canales online",
    "19": "Realización (Asistencia) · Tema 19 · La puesta en escena",
    "20": "Realización (Asistencia) · Tema 20 · Postproducción",
    "21": "Realización (Asistencia) · Tema 21 · Prevención de riesgos laborales",
 },
 "produccion": {
    "01": "Producción · Tema 1 · La producción: plan de trabajo, organización y fases",
    "02": "Producción · Tema 2 · Ley de Propiedad Intelectual",
    "03": "Producción · Tema 3 · La escaleta y el guion. Desglose",
    "04": "Producción · Tema 4 · Géneros y formatos audiovisuales",
    "05": "Producción · Tema 5 · Equipos humanos",
    "06": "Producción · Tema 6 · Captación de imagen y sonido",
    "07": "Producción · Tema 7 · El estudio de televisión",
    "08": "Producción · Tema 8 · Producción en exteriores",
    "09": "Producción · Tema 9 · Escenografía e iluminación. Diseño de producción",
    "10": "Producción · Tema 10 · Medios artísticos",
    "11": "Producción · Tema 11 · Tratamiento de imagen y sonido. Postproducción",
    "12": "Producción · Tema 12 · Transporte de la señal",
    "13": "Producción · Tema 13 · Control central",
    "14": "Producción · Tema 14 · El presupuesto",
    "15": "Producción · Tema 15 · Organismos nacionales e internacionales de televisión",
    "16": "Producción · Tema 16 · Aspectos jurídicos de la producción",
 },
 "produccion-asistencia": {
    "01": "Producción (Asistencia) · Tema 1 · La producción: sistemas y métodos. "
          "Organización de la producción",
    "02": "Producción (Asistencia) · Tema 2 · Derechos de autor. "
          "Ley de Propiedad Intelectual. Redes sociales",
    "03": "Producción (Asistencia) · Tema 3 · El guion",
    "04": "Producción (Asistencia) · Tema 4 · El desglose",
    "05": "Producción (Asistencia) · Tema 5 · Localización",
    "06": "Producción (Asistencia) · Tema 6 · Organización de la producción, "
          "plan de trabajo y orden de trabajo",
    "07": "Producción (Asistencia) · Tema 7 · Equipos humanos: equipos técnicos "
          "y artísticos",
    "08": "Producción (Asistencia) · Tema 8 · Formatos y soportes",
    "09": "Producción (Asistencia) · Tema 9 · Escenografía e iluminación. "
          "Nuevas tendencias",
    "10": "Producción (Asistencia) · Tema 10 · Imagen y sonido: captación y "
          "tratamiento",
    "11": "Producción (Asistencia) · Tema 11 · Medios de transmisión de señal, "
          "envío de imágenes y comunicaciones",
    "12": "Producción (Asistencia) · Tema 12 · El estudio de televisión",
    "13": "Producción (Asistencia) · Tema 13 · Equipos técnicos de exteriores",
    "14": "Producción (Asistencia) · Tema 14 · Documentación internacional para "
          "desplazamientos de equipos técnicos y humanos",
    "15": "Producción (Asistencia) · Tema 15 · Organismos nacionales e "
          "internacionales de televisión",
    "16": "Producción (Asistencia) · Tema 16 · Gestión de servicios varios. "
          "Agencias, proveedores, particulares",
    "17": "Producción (Asistencia) · Tema 17 · Ley de Protección de Datos",
 },
 "documentacion": {
    "01": "Documentación · Tema 1 · Historia de RTVE: orígenes, desarrollo y "
          "estructura territorial",
    "02": "Documentación · Tema 2 · Documentación y tecnologías de la información",
    "03": "Documentación · Tema 3 · Internet",
    "04": "Documentación · Tema 4 · Inteligencia artificial aplicada a contenidos "
          "sonoros y audiovisuales",
    "05": "Documentación · Tema 5 · Centros de documentación en medios de "
          "comunicación audiovisual",
    "06": "Documentación · Tema 6 · Cultura y actualidad nacional e internacional",
 },
 "gestion": {
    "03": "Gestión · Tema 3 · Los convenios colectivos de trabajo",
    "04": "Gestión · Tema 4 · El contrato de trabajo",
    "05": "Gestión · Tema 5 · Modificación de las condiciones del contrato",
    "06": "Gestión · Tema 6 · Tiempo de trabajo",
    "07": "Gestión · Tema 7 · El salario",
    "08": "Gestión · Tema 8 · Derechos y deberes de empresarios y trabajadores",
    "09": "Gestión · Tema 9 · Protección de datos personales y garantía de los "
          "derechos digitales",
    "11": "Gestión · Tema 11 · El modelo contable español y el Plan General de "
          "Contabilidad",
    "12": "Gestión · Tema 12 · El proceso contable y las cuentas anuales",
    "13": "Gestión · Tema 13 · El patrimonio y el balance de situación",
    "14": "Gestión · Tema 14 · Gastos e ingresos, tesorería, existencias y "
          "acreedores",
    "15": "Gestión · Tema 15 · El inmovilizado material y su amortización",
    "17": "Gestión · Tema 17 · Los costes de producción y la contabilidad de costes",
    "18": "Gestión · Tema 18 · La función de tesorería en la empresa",
    "19": "Gestión · Tema 19 · La información financiera de las empresas",
    "20": "Gestión · Tema 20 · Impuesto sobre el Valor Añadido",
    "21": "Gestión · Tema 21 · Planificación estratégica y control de gestión",
    "22": "Gestión · Tema 22 · Seguridad Social",
    "24": "Gestión · Tema 24 · Nómina",
    "25": "Gestión · Tema 25 · La empresa como organización",
    "26": "Gestión · Tema 26 · La gestión por competencias",
    "27": "Gestión · Tema 27 · El proceso de producción en televisión",
    "28": "Gestión · Tema 28 · Matemática financiera",
    "29": "Gestión · Tema 29 · Estadística descriptiva básica",
 },
 "gestion-administrativa": {
    "01": "Gestión Administrativa · Tema 1 · Gestión administrativa: documento, "
          "acto administrativo, registro y archivo",
    "02": "Gestión Administrativa · Tema 2 · El contrato de trabajo",
    "03": "Gestión Administrativa · Tema 3 · Seguridad Social",
    "04": "Gestión Administrativa · Tema 4 · Nóminas",
    "05": "Gestión Administrativa · Tema 5 · Contabilidad y Plan General de "
          "Contabilidad",
    "06": "Gestión Administrativa · Tema 6 · Matemática financiera básica",
    "07": "Gestión Administrativa · Tema 7 · Probabilidad y estadística",
    "08": "Gestión Administrativa · Tema 8 · Ofimática y proceso de la información",
    "09": "Gestión Administrativa · Tema 9 · El entorno Microsoft Windows 10",
    "10": "Gestión Administrativa · Tema 10 · La red Internet",
    "11": "Gestión Administrativa · Tema 11 · Herramientas Microsoft Office 2019",
    "12": "Gestión Administrativa · Tema 12 · Microsoft Teams",
 },
 "informacion": {
    "01": "Información y Contenidos · Tema 1 · Actualidad nacional e "
          "internacional: política, economía, sociedad, cultura y deportes",
    "02": "Información y Contenidos · Tema 2 · La Unión Europea y sus "
          "instituciones",
    "03": "Información y Contenidos · Tema 3 · Instituciones y poderes del "
          "Estado, instituciones y organismos internacionales",
    "04": "Información y Contenidos · Tema 4 · Código de autorregulación para "
          "la defensa de los derechos del menor de RTVE",
    "05": "Información y Contenidos · Tema 5 · Real Decreto-ley 4/2018: "
          "designación del Consejo de Administración de la CRTVE",
    "06": "Información y Contenidos · Tema 6 · Manual de estilo de RTVE",
    "07": "Información y Contenidos · Tema 7 · Directiva (UE) 2018/1808 de "
          "servicios de comunicación audiovisual",
    "08": "Información y Contenidos · Tema 8 · Resolución del Parlamento "
          "Europeo de 25 de noviembre de 2020",
    "09": "Información y Contenidos · Tema 9 · Informe mundial de la UNESCO "
          "2021/2022 sobre libertad de expresión",
    "10": "Información y Contenidos · Tema 10 · Carta ética mundial para "
          "periodistas de la FIP",
 },
}

if __name__ == "__main__":
    ocupacion = sys.argv[1] if len(sys.argv) > 1 else "produccion_asist"
    main(ocupacion, TITULOS[ocupacion.split("_")[0]])
