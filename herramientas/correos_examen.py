#!/usr/bin/env python3
"""Cruza un cuadernillo de Correos con su plantilla y saca el examen citable.

**Por qué hace falta.** Correos publica el cuadernillo y la plantilla por
separado, y ninguno de los dos sirve solo: **el cuadernillo no dice cuál es la
respuesta y la plantilla es una columna de letras sin enunciado**. Lo que el
método necesita para calibrar —apartado 3.2— es la pregunta entera con su
respuesta oficial al lado.

**Lo que hay que saber de estos cuadernillos.** Son cuatro, dos por puesto, y los
modelos A y B de un mismo puesto llevan **casi las mismas preguntas en distinto
orden**. Así que **la respuesta va por número de pregunta DENTRO de su modelo**, y
cruzar el enunciado del modelo A con la letra del modelo B da un examen falso de
principio a fin.

**Las anuladas van marcadas y no llevan letra.** La plantilla escribe «Anulada» en
la celda de la respuesta, de modo que salen del propio volcado y no hay que
tomarlas de ninguna fuente de segunda mano. **Una pregunta anulada sigue siendo
material de estudio** —su enunciado salió del temario— **pero no sirve para
calibrar la respuesta oficial**, y por eso se distingue.

Uso:
    python3 herramientas/correos_examen.py <cuadernillo.txt> <plantilla.txt> <modelo> <salida.md>
donde <modelo> es `A` o `B`.
"""
import re
import sys


def plantilla(fichero):
    """Devuelve los dos diccionarios de respuestas, modelo A y modelo B.

    La hoja va a cuatro columnas de pares: las dos primeras son el modelo A
    —preguntas 1 a 55 y 56 a 110— y las dos siguientes, el modelo B. Se lee de
    ocho en ocho porque ése es el ancho de una fila entera.
    """
    toks = [x for x in (l.strip() for l in
                        open(fichero, encoding="utf-8").read().split("\n")) if x]
    j = max(k for k, v in enumerate(toks) if v == "Respuesta")
    d = toks[j + 1:]
    A, B = {}, {}
    i = 0
    while i + 7 < len(d):
        n1, r1, n2, r2, n3, r3, n4, r4 = d[i:i + 8]
        if not all(x.isdigit() for x in (n1, n2, n3, n4)):
            break
        A[int(n1)] = r1
        A[int(n2)] = r2
        B[int(n3)] = r3
        B[int(n4)] = r4
        i += 8
    return A, B


def preguntas(fichero):
    """Enunciado y cuatro opciones de cada pregunta del cuadernillo."""
    t = open(fichero, encoding="utf-8").read()
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{2,}", "\n", t)
    # El enunciado va de «N.» hasta la opción A, y cada opción hasta la
    # siguiente letra o hasta el enunciado que empieza la pregunta de después.
    out = {}
    # **El número de pregunta no siempre empieza la línea.** En el modelo B de
    # Atención al Cliente la 21 va sangrada —« 21. »— y su enunciado baja al
    # renglón siguiente; cortar sólo en «\n» seguido de dígito se la saltaba y
    # el cuadernillo salía con 109 preguntas de 110 sin decir cuál faltaba.
    bloques = re.split(r"\n(?=[ \t]*\d{1,3}\.[ \t\n])", t)
    for b in bloques:
        m = re.match(r"\s*(\d{1,3})\.\s(.+?)(?=\n\s*A\.\s)", b, re.S)
        if not m:
            # **Las psicotécnicas no tienen opciones de texto: son figuras.**
            # Exigir que aparezca una opción «A.» las descarta en silencio, y
            # con ellas se iba una pregunta ANULADA del modelo B de Reparto,
            # de modo que la cuenta de anuladas salía corta sin avisar.
            mp = re.match(r"\s*(\d{1,3})\.\s(.+?)(?=\n\s*\d{1,3}\.\s|\Z)", b, re.S)
            if not mp:
                continue
            n = int(mp.group(1))
            out[n] = (re.sub(r"\s+", " ", mp.group(2)).strip(), {})
            continue
        n = int(m.group(1))
        enun = re.sub(r"\s+", " ", m.group(2)).strip()
        ops = {}
        for letra in "ABCD":
            mo = re.search(r"\n\s*%s\.\s(.+?)(?=\n\s*[A-D]\.\s|\Z)" % letra, b, re.S)
            if mo:
                ops[letra] = re.sub(r"\s+", " ", mo.group(1)).strip()
        out[n] = (enun, ops)
    return out


def main():
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    cuad, plant, modelo, salida = sys.argv[1:5]
    A, B = plantilla(plant)
    resp = A if modelo.upper() == "A" else B
    pre = preguntas(cuad)

    lineas = ["# Examen de Correos del 7 de mayo de 2023 · modelo %s" % modelo.upper(),
              "",
              "Cuadernillo `%s` cruzado con su plantilla oficial." % cuad.split("/")[-1],
              "**Las anuladas van dichas**: su enunciado es material de estudio, pero su",
              "respuesta no calibra nada.",
              ""]
    anuladas = 0
    for n in sorted(pre):
        enun, ops = pre[n]
        r = resp.get(n, "")
        marca = ""
        if "nulad" in r:
            marca = " · **ANULADA**"
            anuladas += 1
            r = ""
        if not ops:
            marca += " · **psicotécnica, opciones en figura**"
        lineas.append("**%d.** %s%s" % (n, enun, marca))
        for letra in "ABCD":
            if letra in ops:
                bien = " ←" if letra == r else ""
                lineas.append("- **%s.** %s%s" % (letra, ops[letra], bien))
        lineas.append("")
    open(salida, "w", encoding="utf-8").write("\n".join(lineas) + "\n")
    print("· %s · %d preguntas · %d anuladas" % (salida, len(pre), anuladas))


if __name__ == "__main__":
    main()
