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

Uso:  banco_especifico.py produccion
"""
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calibrar import preguntas, clasifica, MATERIAS
from banco import plantilla, sin_pie, sin_ecos

DIR = "convocatoria/examenes"
SALIDA = "banco"


def reparto(ocupacion):
    """{(origen, nº): (tema, motivo)} leído del acta de clasificación."""
    ruta = os.path.join(SALIDA, "especifico-%s.tsv" % ocupacion)
    fuera = {}
    for linea in open(ruta, encoding="utf-8"):
        if linea.startswith("#") or not linea.strip():
            continue
        c = linea.rstrip("\n").split("\t")
        if c[0] == "origen":
            continue
        fuera[(c[0], int(c[1]))] = (c[2], c[3] if len(c) > 3 else "")
    return fuera


def cuadernillos(ocupacion):
    """[(cuadernillo, plantilla)] de la ocupación, por el nombre del fichero."""
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
    filas = reparto(corta)
    portema = defaultdict(list)
    usadas, sinfila = set(), []
    for cuad, plant in cuadernillos(ocupacion):
        respuestas = plantilla(plant) if plant else {}
        origen = re.sub(r"\.ocr$", "", os.path.basename(cuad)[:-4])
        for n, cuerpo in preguntas(open(cuad, encoding="utf-8").read()):
            clave = (origen, n)
            if clave not in filas:
                # las del bloque común no son de este banco: van en el del
                # temario general, y contarlas aquí como pendientes daría una
                # cifra de trabajo que no existe
                if clasifica(cuerpo, MATERIAS) is None:
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
    huerfanas = sorted(set(filas) - usadas)
    if huerfanas:
        print()
        print("! %d filas del acta no casan con ninguna pregunta:" % len(huerfanas))
        for h in huerfanas:
            print("  ! %s nº %d" % h)


TITULOS = {
    "02": "Producción (Asistencia) · Tema 2 · Derechos de autor. "
          "Ley de Propiedad Intelectual. Redes sociales",
}

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "produccion_asist", TITULOS)
