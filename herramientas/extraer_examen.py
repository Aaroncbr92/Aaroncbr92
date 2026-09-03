#!/usr/bin/env python3
"""Extrae el texto de un cuadernillo de examen en PDF.

**Por qué no vale `page.get_text()` a secas.** Varios cuadernillos de RTVE
llevan bloques que repiten trozos ya impresos: fragmentos de la mitad derecha
de líneas anteriores, a veces duplicados entre sí, colocados al final de la
página. En el texto plano aparecen pegados detrás de la última pregunta y el
banco los recoge como si fueran opciones. El caso extremo es el segundo
llamamiento de Realización (Asistencia): **252 fragmentos** repartidos por
veinte páginas.

**La regla que los quita.** Un fragmento sobrante está siempre *a la altura de
la línea que copia* —comparten la misma `y`— y su texto está contenido en el de
esa línea. Así que se recorre la página en orden y se descarta el trozo que
cumple las dos cosas a la vez: **misma altura que un trozo anterior y texto
contenido en él**.

**Por qué no se corta la página por el pie.** Es tentador —el pie «Página N de
M» es lo último que se imprime— y está mal: en `29_preguntas_igyciys` el pie
sale en el PDF *antes* que las preguntas, porque el orden de los bloques no es
el orden de lectura. Cortar ahí borraría seis preguntas enteras. La regla de la
altura no depende del orden de la maqueta.

La última costura une la letra de la opción con su texto, que el PDF pone en
bloques distintos.
"""
import sys

import pymupdf


def texto(ruta):
    doc = pymupdf.open(ruta)
    salida = []
    for pagina in doc:
        vistos = {}          # altura redondeada -> trozos ya emitidos en ella
        for bloque in pagina.get_text("dict")["blocks"]:
            if bloque.get("type") != 0:
                continue
            for linea in bloque["lines"]:
                trozos = []
                for tramo in linea["spans"]:
                    t = tramo["text"]
                    altura = round(tramo["bbox"][1], 1)
                    limpio = t.strip()
                    anteriores = vistos.setdefault(altura, [])
                    if len(limpio) >= 3 and any(limpio in a for a in anteriores):
                        continue          # fragmento repetido de esta misma línea
                    anteriores.append(limpio)
                    trozos.append(t)
                if trozos:
                    salida.append("".join(trozos))
            salida.append("")
    t = "\n".join(salida)
    import re
    return re.sub(r"(?m)^([a-d]\))\s*\n\s*", r"\1 ", t)


if __name__ == "__main__":
    for ruta in sys.argv[1:]:
        destino = ruta.rsplit(".", 1)[0] + ".txt"
        with open(destino, "w") as f:
            f.write(texto(ruta))
        print(destino)
