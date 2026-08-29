#!/usr/bin/env python3
"""Arma el banco de preguntas del bloque común a partir de los exámenes.

El temario general es el mismo para todas las ocupaciones tipo, y los exámenes
comparten preguntas entre ocupaciones. Así que las preguntas de Constitución,
Ley 17/2006, Convenio, Igualdad, Ley 13/2022, Ley 8/2009 y prevención de riesgos
de cualquiera de los 87 cuadernillos valen para los tres temarios.

Empareja cada cuadernillo con su plantilla, saca la letra correcta de cada
pregunta, clasifica por materia y escribe un fichero por materia.
"""
import glob
import os
import re
import sys
import unicodedata
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calibrar import preguntas, clasifica, MATERIAS

DIR = "convocatoria/examenes"
SALIDA = "banco"


def plantilla(ruta):
    """Devuelve {nº de pregunta: letra}.

    La plantilla imprime, por bloques, una columna de números y debajo la
    columna de letras que les corresponde. Antes se troceaba por páginas, y
    bastaba con que el pie dijera «Fecha de publicación» en vez de «Fecha de la
    publicación» para que un bloque se pegara al siguiente y todas las
    respuestas de esa página salieran corridas un lugar. Ahora se recorre la
    secuencia y se empareja cada racha de números con la racha de letras que va
    detrás, que es como está impresa.
    """
    t = open(ruta, encoding="utf-8").read().replace("\x0c", "\n")
    fichas = []
    for linea in t.splitlines():
        linea = linea.strip()
        if re.fullmatch(r"\d{1,3}", linea):
            fichas.append(("n", int(linea)))
        elif re.fullmatch(r"[a-dA-D]", linea):
            fichas.append(("l", linea.lower()))

    fuera = {}
    i = 0
    while i < len(fichas):
        nums = []
        while i < len(fichas) and fichas[i][0] == "n":
            nums.append(fichas[i][1])
            i += 1
        letras = []
        while i < len(fichas) and fichas[i][0] == "l":
            letras.append(fichas[i][1])
            i += 1
        for n, l in zip(nums, letras):
            fuera.setdefault(n, l)
        if not nums and not letras:
            i += 1
    return fuera


def parejas():
    """Empareja cuadernillo y plantilla por el nombre de la ocupación, no por
    el orden: en Producción (Asistencia) la plantilla no va detrás del
    cuadernillo, sino dos posiciones más allá."""
    def clave(base):
        b = re.sub(r"^\d+_", "", base[:-4])
        b = re.sub(r"^(preguntas|plantilla_de_respuestas|plantilla|respuestas)_", "", b)
        return re.sub(r"_(de_respuestas|respuestas)_", "_", b)

    cuadernillos, plantillas = {}, {}
    for f in sorted(glob.glob(os.path.join(DIR, "*.txt"))):
        base = os.path.basename(f)
        cuerpo = re.sub(r"^\d+_", "", base)
        if cuerpo.startswith("preguntas"):
            cuadernillos[clave(base)] = f
        elif cuerpo.startswith(("plantilla", "respuestas")):
            plantillas[clave(base)] = f
    return [(f, plantillas.get(k)) for k, f in sorted(cuadernillos.items())]


def main():
    os.makedirs(SALIDA, exist_ok=True)
    pormateria = defaultdict(list)
    con, sin = 0, 0
    sospechosas = []
    for cuad, plant in parejas():
        respuestas = plantilla(plant) if plant else {}
        # una plantilla bien leída numera de 1 a N sin huecos; si no, se avisa
        if respuestas:
            alto = max(respuestas)
            faltan = [n for n in range(1, alto + 1) if n not in respuestas]
            if faltan:
                sospechosas.append("%s: faltan %d de %d (%s...)"
                                   % (os.path.basename(plant), len(faltan), alto,
                                      ", ".join(str(n) for n in faltan[:6])))
        texto = open(cuad, encoding="utf-8").read()
        origen = os.path.basename(cuad)[:-4]
        for n, cuerpo in preguntas(texto):
            materia = clasifica(cuerpo, MATERIAS)
            if not materia:
                continue
            letra = respuestas.get(n)
            if letra:
                con += 1
            else:
                sin += 1
            # el OCR deja caracteres de control que hacen ilegible el fichero
            cuerpo = "".join(c for c in cuerpo if c == "\n" or c >= " ")
            cuerpo = re.sub(r"\n{2,}", "\n", cuerpo).strip()
            pormateria[materia].append((origen, n, letra, cuerpo))

    total = 0
    for materia, items in sorted(pormateria.items()):
        nombre = unicodedata.normalize("NFD", materia.split("·")[0].strip())
        nombre = "".join(c for c in nombre if unicodedata.category(c) != "Mn")
        nombre = re.sub(r"[^A-Za-z0-9]+", "-", nombre).strip("-").lower()
        ruta = os.path.join(SALIDA, "%s.md" % nombre)
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("# %s\n\n" % materia)
            fh.write("%d preguntas reales sacadas de los cuadernillos de octubre y "
                     "noviembre de 2024.\nLa respuesta es la de la plantilla oficial; "
                     "donde pone «sin plantilla» es que\nno se pudo emparejar.\n\n"
                     % len(items))
            for origen, n, letra, cuerpo in items:
                fh.write("---\n\n**%s · nº %d · respuesta: %s**\n\n```\n%s\n```\n\n"
                         % (origen, n, letra or "sin plantilla", cuerpo))
        total += len(items)
        print("%-50s %4d preguntas -> %s" % (materia, len(items), ruta))
    print()
    print("total %d preguntas del bloque común; con respuesta oficial %d, sin ella %d"
          % (total, con, sin))
    if sospechosas:
        print()
        print("Plantillas con huecos, revisar a mano antes de fiarse de ellas:")
        for x in sospechosas:
            print("  ! %s" % x)


if __name__ == "__main__":
    main()
