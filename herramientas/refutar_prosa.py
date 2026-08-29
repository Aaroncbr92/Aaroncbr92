#!/usr/bin/env python3
"""Refutación por prosa y forma: relleno, repeticiones y siglas sin presentar."""
import re
import sys
import unicodedata
from collections import Counter

RELLENO = [r"como hemos visto", r"como ya se ha dicho", r"en s[íi]ntesis",
           r"cabe destacar", r"es importante se[ñn]alar", r"conviene recordar",
           r"en definitiva", r"por [úu]ltimo,? cabe", r"no hay que olvidar",
           r"resulta evidente", r"a modo de resumen", r"dicho esto"]


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9ñ ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def main():
    tema = open(sys.argv[1], encoding="utf-8").read()
    hallazgos = 0

    print("## Tejido conectivo y relleno")
    for pat in RELLENO:
        for m in re.finditer(pat, tema, re.I):
            print("  · %s" % re.sub(r"\s+", " ", tema[max(0, m.start()-60):m.end()+60]))
            hallazgos += 1
    print("  (ninguno)" if not hallazgos else "")

    print()
    print("## Frases repetidas entre epígrafes")
    frases = [limpia(f) for f in re.split(r"(?<=[.;:])\s", tema)]
    frases = [f for f in frases if len(f.split()) >= 8]
    repes = [(f, c) for f, c in Counter(frases).items() if c > 1]
    for f, c in sorted(repes, key=lambda x: -x[1]):
        print("  · x%d  %s" % (c, f[:120]))
        hallazgos += 1
    if not repes:
        print("  (ninguna)")

    print()
    print("## Siglas sin presentar la primera vez")
    # los números romanos de los títulos no son siglas
    ROMANOS = re.compile(r"^[IVXLC]+$")
    CONOCIDAS = ("BOE", "RTVE", "TVE", "RNE")
    for sigla in sorted(set(re.findall(r"\b([A-Z]{2,6})\b", tema))):
        if ROMANOS.match(sigla) or sigla in CONOCIDAS:
            continue
        i = tema.find(sigla)
        antes = tema[max(0, i - 130):i]
        if "(" not in antes:
            print("  · %-6s primera aparición: ...%s%s..."
                  % (sigla, re.sub(r"\s+", " ", antes[-70:]), sigla))
            hallazgos += 1

    print()
    print("hallazgos de prosa: %d" % hallazgos)


if __name__ == "__main__":
    main()
