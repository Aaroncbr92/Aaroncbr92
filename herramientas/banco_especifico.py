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
MARCA = {"informacion": "iyc"}


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
        if ocupacion not in f:
            continue
        base = f[:-4]
        # la plantilla es el fichero siguiente por número: 77 -> 79 aquí no vale,
        # así que se busca por el sufijo del nombre, que es el que las empareja
        cola = base.split("_preguntas_", 1)[1]
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
        if os.path.basename(cuad)[:-4] in enteros:
            descartados.append(os.path.basename(cuad)[:-4])
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
 "produccion": {
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
