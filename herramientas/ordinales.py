#!/usr/bin/env python3
"""Reescribe con cifras los artículos que el BOE numera con letras.

Hay normas —la Ley 16/1985 del Patrimonio Histórico, por ejemplo— cuyos
artículos se titulan «Artículo cuarenta y nueve» y cuyo identificador de bloque
es `acuarentaynueve`. Las lentes por artículo buscan «Artículo <cifra>», así que
sobre esas normas devuelven «0 comprobadas, 0 no literales»: un tema sin revisar
que se lee como impecable, que es el fallo del apartado 10 del manual.

Antes que renunciar a la lente o darla por pasada, se construye la fuente: este
script copia el volcado cambiando sólo el rótulo del encabezado, de «Artículo
cuarenta y nueve» a «Artículo 49». No toca el cuerpo del artículo, de modo que
las citas se siguen comprobando contra el texto tal como lo publicó el BOE.

Uso:  ordinales.py <norma.md> > <norma.cifras.md>
"""
import re
import sys

UNIDADES = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6,
            "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
            "dieciseis": 16, "diecisiete": 17, "dieciocho": 18,
            "diecinueve": 19, "veinte": 20, "veintiuno": 21, "veintidos": 22,
            "veintitres": 23, "veinticuatro": 24, "veinticinco": 25,
            "veintiseis": 26, "veintisiete": 27, "veintiocho": 28,
            "veintinueve": 29, "primero": 1, "segundo": 2, "tercero": 3,
            "cuarto": 4, "quinto": 5, "sexto": 6, "septimo": 7, "octavo": 8,
            "noveno": 9, "decimo": 10}
DECENAS = {"treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60,
           "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100,
           "ciento": 100}


def limpia(s):
    tabla = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
    return s.translate(tabla).lower().strip()


def cifra(letras):
    """«cuarenta y nueve» -> 49.  Devuelve None si no sabe leerlo."""
    piezas = [p for p in limpia(letras).split() if p != "y"]
    if not piezas:
        return None
    total = 0
    for p in piezas:
        if p in DECENAS:
            total += DECENAS[p]
        elif p in UNIDADES:
            total += UNIDADES[p]
        else:
            return None
    return total


def main():
    fuente = open(sys.argv[1], encoding="utf-8").read()

    def cambia(m):
        n = cifra(m.group(2))
        return m.group(0) if n is None else "## [%s] Artículo %d" % (m.group(1), n)

    salida, cuantos = re.subn(r"^## \[([^\]]+)\] Artículo ([A-Za-zÁÉÍÓÚáéíóú ]+)$",
                              cambia, fuente, flags=re.M)
    sys.stderr.write("artículos reescritos con cifra: %d\n" % cuantos)
    sys.stdout.write(salida)


if __name__ == "__main__":
    main()
