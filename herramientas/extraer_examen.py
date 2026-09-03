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
import re
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


MOBILIARIO = re.compile(r"^(?:\d?[ºo]?\s*Llamamiento|2[ºo]\s*Llamamiento|"
                        r"P.gina:?\s*\d+\s*de\s*\d+|"
                        r"Fecha de publicaci[óo]n:.*)$", re.I)


def texto_por_alturas(ruta):
    """Reconstruye las líneas por su altura, no por los bloques del PDF.

    **Hay cuadernillos maquetados como una tabla de tres columnas**: el número
    de la pregunta a la izquierda, la letra de la opción en medio y el texto a
    la derecha. `81_preguntas_produccion` es así. En esa maqueta los bloques del
    PDF **agrupan por columna**, de modo que la extracción normal saca primero
    las cuatro letras juntas —«a) b) c) d)»— y detrás los cuatro textos
    seguidos: las opciones llegan al banco **separadas de su letra**, y en
    algunas preguntas **desordenadas**, sin que nada dé error.

    La maqueta sí dice la verdad en la coordenada vertical: **la letra y su
    texto están a la misma altura**. Así que aquí se agrupan los trozos por
    altura y se ordenan por su posición horizontal, con lo que cada renglón
    vuelve a leerse como se imprimió.

    No sustituye a `texto()`: se usa donde la otra falla, y el que llama lo
    decide mirando si quedan letras de opción sueltas.
    """
    doc = pymupdf.open(ruta)
    salida = []
    for pagina in doc:
        renglones = {}
        # el mobiliario de la página —marca de agua, pie y fecha— está a la
        # altura de un renglón de texto en algunos cuadernillos, y al agrupar
        # por altura se cuela **delante** de la letra de la opción: la línea
        # deja de empezar por «c)» y esa opción se pierde. Se descarta aquí
        for bloque in pagina.get_text("dict")["blocks"]:
            if bloque.get("type") != 0:
                continue
            for linea in bloque["lines"]:
                for tramo in linea["spans"]:
                    if not tramo["text"].strip():
                        continue
                    if MOBILIARIO.match(tramo["text"].strip()):
                        continue
                    altura = round(tramo["bbox"][1] / 2) * 2
                    renglones.setdefault(altura, []).append(
                        (tramo["bbox"][0], tramo["text"].strip()))
        for altura in sorted(renglones):
            trozos = [t for _, t in sorted(renglones[altura])]
            salida.append(" ".join(trozos))
        salida.append("")
    return "\n".join(salida)


def sueltas(t):
    """¿Cuántas letras de opción se han quedado sin su texto?

    No basta con mirar las que están solas en su renglón: la costura que une la
    letra con la línea siguiente ya ha pegado unas con otras, y lo que queda es
    un renglón con **dos letras seguidas** —«a) b)»— o una letra al final del
    texto. Las dos formas se cuentan aquí.
    """
    return len(re.findall(r"(?m)^[a-d]\)\s*(?:[a-d]\)|$)", t))


if __name__ == "__main__":
    for ruta in sys.argv[1:]:
        destino = ruta.rsplit(".", 1)[0] + ".txt"
        t = texto(ruta)
        # si la maqueta es de tres columnas, la extracción normal deja las
        # letras de opción huérfanas. Se reintenta por alturas y se queda la
        # que menos deje sueltas
        if sueltas(t) > 4:
            otra = texto_por_alturas(ruta)
            if sueltas(otra) < sueltas(t):
                t = otra
        with open(destino, "w") as f:
            f.write(t)
        print("%s  (letras sueltas: %d)" % (destino, sueltas(t)))
