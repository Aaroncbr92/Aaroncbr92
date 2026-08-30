#!/usr/bin/env python3
"""Lee las plantillas de respuestas cuyo PDF no tiene tabla de caracteres.

Tres plantillas de 2024 —Gestión, Gestión-Abogado/A e Iluminación— llevan la
fuente incrustada **sin tabla de caracteres**, así que extraer su texto devuelve
códigos de control y no letras. Sus 65 preguntas entraban en el banco como «sin
plantilla».

**Pasarles OCR a la hoja entera no sirve**: son tablas de dos columnas y el
lector pierde la columna de letras a partir de la segunda página, o confunde los
bordes de las celdas con caracteres. Se probaron cuatro modos de segmentación y
ninguno la recupera entera.

Lo que sí sirve es no leer la hoja, sino **la celda**:

1. **La geometría sale del propio PDF.** Los bordes de la tabla son dibujos
   vectoriales, así que `get_drawings()` da el rectángulo exacto de cada celda.
   No hay que adivinar dónde empieza una fila.
2. **Los códigos de la fuente son consistentes.** No sabemos qué letra es cada
   código, pero **la misma letra lleva siempre el mismo código**. En la columna
   de respuestas hay exactamente **cuatro códigos distintos**, que son las cuatro
   opciones. **Consistentes dentro de cada página, no del documento**: en la
   plantilla de Iluminación cada página incrusta su propia fuente y los mismos
   códigos significan cosas distintas en la 2 y en la 3. Por eso el reparto se
   hace **página a página**, que es lo que aguanta los tres ficheros.
3. **Solo hace falta OCR para nombrar esos cuatro**, y se hace sobre la celda
   recortada por dentro de sus bordes, ampliada y con margen blanco alrededor.
   Se leen varias celdas de cada código y se decide por mayoría: no se decide una
   letra por una lectura suelta.

Y se comprueba lo que se puede comprobar: que los cuatro códigos dan cuatro
letras **distintas**, que la columna de números lee **1..N sin huecos**, y que el
número de filas coincide con el de preguntas del cuadernillo.

Uso:  plantilla_ocr.py <plantilla.pdf> [...]      escribe <plantilla>.respuestas.tsv
"""
import collections
import os
import subprocess
import sys

import pymupdf
from PIL import Image, ImageOps

TMP = os.environ.get("TMPDIR", "/tmp")
LETRAS = {"a": "a", "@": "a", "b": "b", "c": "c", "C": "c", "d": "d", "D": "d"}


def filas(pdf):
    """[(página, celda del número, celda de la letra)] en orden de lectura."""
    doc = pymupdf.open(pdf)
    fuera = []
    for pag in doc:
        porfila = {}
        for dibujo in pag.get_drawings():
            r = dibujo["rect"]
            if r.width > 20 and r.height > 5:
                porfila.setdefault(round(r.y0, 1), []).append(r)
        for y in sorted(porfila):
            cols = sorted(porfila[y], key=lambda r: r.x0)
            if len(cols) == 2:
                fuera.append((pag, cols[0], cols[1]))
    return doc, fuera


def glifos(pag):
    fuera = []
    for b in pag.get_text("rawdict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                for c in s["chars"]:
                    fuera.append((c["bbox"], c["c"]))
    return fuera


def dentro(bbox, r):
    x, y = (bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2
    return r.x0 <= x <= r.x1 and r.y0 <= y <= r.y1


def lee_celda(pag, r, cache):
    if pag.number not in cache:
        cache[pag.number] = glifos(pag)
    return "".join(c for bb, c in cache[pag.number] if dentro(bb, r))


def ocr(pag, r, dpi=900, margen=3.2, borde=120):
    """OCR de una celda: recortada por dentro de sus bordes y con marco blanco."""
    caja = pymupdf.Rect(r.x0 + margen, r.y0 + margen, r.x1 - margen, r.y1 - margen)
    png = os.path.join(TMP, "celda.png")
    pag.get_pixmap(dpi=dpi, clip=caja).save(png)
    ImageOps.expand(Image.open(png).convert("L"), border=borde, fill=255).save(png)
    subprocess.run(["tesseract", png, os.path.join(TMP, "celda"), "--psm", "10"],
                   capture_output=True)
    return open(os.path.join(TMP, "celda.txt"), encoding="utf-8").read().strip()


def respuestas(pdf, muestras=6):
    doc, fs = filas(pdf)
    cache = {}
    leidas = [(lee_celda(p, rn, cache), lee_celda(p, rl, cache), p, rl)
              for p, rn, rl in fs]
    # la fila de cabecera («Pregunta | Respuesta») trae varios glifos en la celda
    datos = [x for x in leidas if len(x[1]) == 1]

    porcodigo = collections.defaultdict(list)
    for _, cod, p, r in datos:
        porcodigo[(p.number, cod)].append((p, r))
    for pag in {k[0] for k in porcodigo}:
        cuantos = len([k for k in porcodigo if k[0] == pag])
        if cuantos > 4:
            sys.exit("%s: la página %d tiene %d códigos de respuesta y no puede "
                     "tener más de cuatro"
                     % (os.path.basename(pdf), pag + 1, cuantos))

    mapa = {}
    for clave, celdas in porcodigo.items():
        votos = collections.Counter()
        for p, r in celdas[:muestras]:
            letra = LETRAS.get(ocr(p, r))
            if letra:
                votos[letra] += 1
        if votos:
            mapa[clave] = votos.most_common(1)[0][0]
    # una letra que el lector no acierte se deduce por descarte, pero solo cuando
    # la página trae las cuatro y falta exactamente una: adivinar dos sería inventar
    for pag in sorted({k[0] for k in porcodigo}):
        dela = [k for k in porcodigo if k[0] == pag]
        faltan = [k for k in dela if k not in mapa]
        sobran = [l for l in "abcd" if l not in {mapa[k] for k in dela if k in mapa}]
        if len(dela) == 4 and len(faltan) == 1 and len(sobran) == 1:
            mapa[faltan[0]] = sobran[0]
        sin = [k for k in dela if k not in mapa]
        if sin:
            sys.exit("%s: en la página %d hay %d códigos que no se dejan leer"
                     % (os.path.basename(pdf), pag + 1, len(sin)))
        letras = [mapa[k] for k in dela]
        if len(set(letras)) != len(letras):
            sys.exit("%s: en la página %d dos códigos distintos dan la misma letra (%r)"
                     % (os.path.basename(pdf), pag + 1, sorted(letras)))

    # los números: la fila n es la pregunta n, y con eso se leen los dígitos. Como
    # las letras, van por página, porque la fuente cambia de una a otra
    digitos = {}
    for i, (num, _, pag, _) in enumerate(datos, 1):
        for cod, d in zip(num, str(i)):
            digitos.setdefault((pag.number, cod), d)
    numeros = ["".join(digitos.get((pag.number, c), "?") for c in num)
               for num, _, pag, _ in datos]
    esperados = [str(i) for i in range(1, len(datos) + 1)]
    if numeros != esperados:
        malas = [(a, b) for a, b in zip(numeros, esperados) if a != b][:5]
        sys.exit("%s: la columna de números no lee 1..%d (%r)"
                 % (os.path.basename(pdf), len(datos), malas))

    return ([(i, mapa[(p.number, cod)]) for i, (_, cod, p, _) in enumerate(datos, 1)],
            mapa)


def main():
    for pdf in sys.argv[1:]:
        rs, mapa = respuestas(pdf)
        salida = pdf[:-4] + ".respuestas.tsv"
        with open(salida, "w", encoding="utf-8") as fh:
            fh.write("# Respuestas leídas celda a celda de %s\n"
                     "# El PDF no lleva tabla de caracteres: la geometría sale de los\n"
                     "# bordes de la tabla y las cuatro letras se nombran por OCR de la\n"
                     "# celda, por mayoría. Reparto de códigos: %s\n"
                     % (os.path.basename(pdf),
                        ", ".join("p%d:%r=%s" % (pag + 1, c, l)
                                  for (pag, c), l in sorted(mapa.items()))))
            for n, l in rs:
                fh.write("%d\t%s\n" % (n, l))
        print("· %-52s %3d respuestas -> %s"
              % (os.path.basename(pdf), len(rs), os.path.basename(salida)))


if __name__ == "__main__":
    main()
