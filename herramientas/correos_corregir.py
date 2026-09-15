#!/usr/bin/env python3
"""Aplica al volcado de Correos las correcciones comprobadas a la vista.

**Por qué el volcado se corrige y no se deja como está.** El reconocedor lee el
**9** de este documento como un **4**, de modo que el volcado dice «Real Decreto
1829/1499» donde la página dice «1829/1999». Y **ninguna lente del proyecto puede
verlo**: `refutar_documento` comprueba que la cifra del tema esté en la fuente, y si
el tema copia la cifra corrupta, **está**. La fuente corrupta valida la copia
corrupta.

**Cómo se corrige, que es lo que lo hace legítimo.** Sólo se aplica lo que está en
`correcciones.tsv`, y cada línea de ese fichero dice **cómo se comprobó**: a la
vista sobre la página, o por el nombre de la norma, que el reconocedor sí acierta
—«Ley Orgánica 11/1385, de 2 de agosto, **de Libertad Sindical**» sólo puede ser la
11/1985—. **Nada se corrige por parecido ni por conjetura.**

El fichero de correcciones queda versionado al lado del volcado: es el registro de
qué se tocó y por qué, y permite rehacer el volcado desde cero y volver a aplicarlo.

Uso:
    python3 herramientas/correos_corregir.py [tema ...]
"""
import os
import sys

BASE = "fuentes/correos-referencia"


def main():
    temas = sys.argv[1:]
    filas = []
    with open(os.path.join(BASE, "correcciones.tsv"), encoding="utf-8") as fh:
        next(fh)
        for l in fh:
            if l.strip():
                filas.append(l.rstrip("\n").split("\t"))

    porTema = {}
    for tema, volcado, documento, _ in filas:
        porTema.setdefault(tema, []).append((volcado, documento))

    for tema in sorted(porTema):
        if temas and tema not in temas:
            continue
        ruta = os.path.join(BASE, "tema-%s.txt" % tema)
        if not os.path.exists(ruta):
            print("  ! no está %s" % ruta)
            continue
        t = open(ruta, encoding="utf-8").read()
        hechas = 0
        for volcado, documento in porTema[tema]:
            n = t.count(volcado)
            if n:
                t = t.replace(volcado, documento)
                hechas += n
        open(ruta, "w", encoding="utf-8").write(t)
        print("· tema %s · %d sustitución(es)" % (tema, hechas))


if __name__ == "__main__":
    main()
