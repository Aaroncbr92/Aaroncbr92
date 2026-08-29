#!/usr/bin/env python3
"""Busca preguntas repetidas o casi repetidas entre exámenes distintos.

Trocea cada cuadernillo en preguntas, se queda con el enunciado (lo anterior a
la primera opción) y compara todos contra todos por trozos de cuatro palabras.
Solo compara preguntas de exámenes distintos.

Uso:  repetidas.py [umbral]        # umbral de parecido, 0 a 1; por defecto 0.6
"""
import glob
import os
import re
import sys
import unicodedata
from collections import defaultdict

RUTAS = ["convocatoria/examenes/*.txt", "convocatoria/examenes-antiguos/*.txt"]
CORTE_OPCION = re.compile(r"(?m)^\s*a\s*[).\-]")


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9ñ ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def enunciados(texto):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from calibrar import preguntas
    fuera = []
    for n, cuerpo in preguntas(texto):
        cuerpo = re.sub(r"(?m)^\s*\d{1,3}\s*[.\-–]{1,2}\s", "", cuerpo, count=1)
        m = CORTE_OPCION.search(cuerpo)
        enunciado = cuerpo[:m.start()] if m else cuerpo
        e = limpia(enunciado)
        if len(e.split()) >= 6:
            fuera.append((n, e))
    return fuera


def trozos(e, k=4):
    p = e.split()
    return {" ".join(p[i:i + k]) for i in range(max(1, len(p) - k + 1))}


def main():
    umbral = float(sys.argv[1]) if len(sys.argv) > 1 else 0.6
    corpus = []
    for patron in RUTAS:
        for f in sorted(glob.glob(patron)):
            nombre = os.path.basename(f)[:-4]
            for n, e in enunciados(open(f, encoding="utf-8").read()):
                corpus.append((nombre, n, e, trozos(e)))
    print("preguntas comparadas: %d de %d exámenes"
          % (len(corpus), len({c[0] for c in corpus})))

    indice = defaultdict(list)
    for i, (_, _, _, ts) in enumerate(corpus):
        for t in ts:
            indice[t].append(i)

    vistos, parejas = set(), []
    for t, ids in indice.items():
        if len(ids) > 40:      # muletillas tipo "segun la ley de"
            continue
        for a in range(len(ids)):
            for b in range(a + 1, len(ids)):
                i, j = ids[a], ids[b]
                if corpus[i][0] == corpus[j][0] or (i, j) in vistos:
                    continue
                vistos.add((i, j))
                ti, tj = corpus[i][3], corpus[j][3]
                jac = len(ti & tj) / float(len(ti | tj))
                if jac >= umbral:
                    parejas.append((jac, i, j))

    parejas.sort(reverse=True)
    print("parejas por encima de %.2f: %d" % (umbral, len(parejas)))
    print()
    for jac, i, j in parejas:
        print("%.2f  %s nº%s  ·  %s nº%s" % (jac, corpus[i][0], corpus[i][1],
                                             corpus[j][0], corpus[j][1]))
        print("      %s" % corpus[i][2][:150])
        print("      %s" % corpus[j][2][:150])
        print()


if __name__ == "__main__":
    main()
