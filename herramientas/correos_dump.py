#!/usr/bin/env python3
"""Volcado del «documento de referencia» de Correos, que va sin capa de texto.

**Por qué existe.** El temario de Correos no se estudia en el BOE: se estudia en
el documento que la propia empresa publica, mil trescientas treinta y cuatro
páginas repartidas en doce PDF. Y ese documento **está compuesto como dibujo
vectorial**: sus letras son trazos, no caracteres, de modo que `pymupdf` devuelve
la página vacía y **las lentes del proyecto se quedan sin nada contra lo que
contrastar**. Un temario escrito sobre una fuente que no se puede citar es
exactamente lo que el apartado 10 del manual llama el fallo que no da error.

**Lo que hace.** Página a página, y en este orden:

  1. **Si la página trae capa de texto**, se toma tal cual. Son 225 de las 1.334,
     y salen mejor que cualquier reconocimiento óptico.
  2. **Si no la trae**, se rasteriza a 300 puntos por pulgada y se pasa por
     `tesseract -l spa`. A esa resolución la tipografía del documento —limpia,
     de buen contraste y a una o dos columnas— se lee sin dificultad. **Se
     midieron 350, 300 y 250**: entre 300 y 350 no cambia ni un carácter del
     resultado y el reconocimiento tarda la mitad, así que 300 es el punto
     donde deja de valer la pena subir.

**Cada página va rotulada en el volcado** con su número dentro del PDF y con el
origen del texto, `texto` o `ocr`. No es decoración: **un tema que cite este
documento tiene que poder decir de qué página sale cada cita**, y quien repase
un pasaje reconocido ópticamente necesita saber que lo es antes de fiarse.

**Lo que este volcado NO es.** No es el documento. El reconocimiento óptico se
equivoca, y se equivoca más en las tablas, en los rótulos sobre fondo de color y
en las cifras sueltas. **Todo dato que un tema tome de una página `ocr` se
comprueba a la vista sobre la página original antes de escribirlo**, que es la
misma regla que el proyecto aplicó a las plantillas ilegibles y a la página 59
del consenso de sensibilidad química múltiple.

Uso:
    python3 herramientas/correos_dump.py <entrada.pdf> <salida.txt> [--dpi 350]
"""
import os
import subprocess
import sys
import tempfile

import pymupdf

# Por debajo de este número de caracteres la página se considera sin capa de
# texto. No se pone en cero porque **muchas páginas traen sólo el número de
# página o el rótulo de copyright como texto de verdad** y todo lo demás como
# dibujo: darlas por buenas dejaría el cuerpo fuera del volcado sin avisar.
MINIMO_TEXTO = 200


def ocr(pagina, dpi):
    """Reconoce una página rasterizándola a `dpi`."""
    pix = pagina.get_pixmap(dpi=dpi)
    with tempfile.TemporaryDirectory() as tmp:
        png = os.path.join(tmp, "p.png")
        pix.save(png)
        # --psm 3 es la segmentación automática con detección de columnas: el
        # documento alterna página a una columna con página a dos, y fijar
        # --psm 6 —«un bloque uniforme»— pega los renglones de las dos columnas
        # en una sola línea y destroza las frases.
        r = subprocess.run(["tesseract", png, "-", "-l", "spa", "--psm", "3"],
                           capture_output=True, text=True)
        return r.stdout


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    entrada, salida = sys.argv[1], sys.argv[2]
    dpi = 300
    if "--dpi" in sys.argv:
        dpi = int(sys.argv[sys.argv.index("--dpi") + 1])

    doc = pymupdf.open(entrada)
    trozos = [
        "# Volcado de %s" % os.path.basename(entrada),
        "",
        "Generado con `herramientas/correos_dump.py`. **El documento original va sin",
        "capa de texto en la mayor parte de sus páginas**, así que lo que sigue es en",
        "parte una transcripción y en parte un **reconocimiento óptico a %d puntos por"
        % dpi,
        "pulgada**. Cada página dice de cuál de las dos cosas viene.",
        "",
        "**Lo reconocido ópticamente no es el documento.** Todo dato que un tema tome de",
        "una página marcada `ocr` se comprueba a la vista sobre la página original antes",
        "de escribirlo.",
        "",
    ]
    n_ocr = n_txt = 0
    for i in range(doc.page_count):
        pagina = doc[i]
        t = pagina.get_text().strip()
        if len(t) >= MINIMO_TEXTO:
            origen = "texto"
            n_txt += 1
        else:
            t = ocr(pagina, dpi).strip()
            origen = "ocr"
            n_ocr += 1
        trozos.append("\n[[ página %d de %d · %s ]]\n" % (i + 1, doc.page_count, origen))
        trozos.append(t)
        if (i + 1) % 25 == 0:
            print("  ... %d/%d" % (i + 1, doc.page_count), flush=True)

    with open(salida, "w", encoding="utf-8") as fh:
        fh.write("\n".join(trozos) + "\n")
    print("· %s · %d páginas (%d de texto, %d reconocidas) · %d KB"
          % (salida, doc.page_count, n_txt, n_ocr,
             os.path.getsize(salida) // 1024))


if __name__ == "__main__":
    main()
