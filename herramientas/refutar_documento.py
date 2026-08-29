#!/usr/bin/env python3
"""Refutación para temas cuya fuente no es articulado.

Las otras dos lentes trocean el tema por artículos y contrastan cada trozo con
su precepto. Eso no sirve cuando la fuente es un documento sin artículos —un
plan, una guía, un manual—: no hay nada que trocear, y las lentes devuelven
«0 comprobadas, 0 no literales», que se lee como un tema impecable y en realidad
es un tema sin revisar. Es el fallo del apartado 10 del manual.

Esta lente hace lo que sí se puede hacer con un documento suelto:

  · **Negritas.** Cada fragmento en negrita del tema, contra el texto completo
    de las fuentes. Lo que no aparece se imprime para mirarlo a mano.
  · **Cifras.** Toda cifra que el tema pone en negrita tiene que aparecer en
    alguna fuente. Una cifra inventada es el error más caro y el más fácil de
    cometer al resumir.

Uso:  refutar_documento.py <tema.md> <fuente.txt> [<fuente.txt> ...]
"""
import re
import sys
import unicodedata

# los PDF meten guiones de corte, espacios duros y ligaduras; sin normalizarlos
# la comparación falla por motivos tipográficos y no por el contenido
DUROS = "              　"


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    for c in DUROS:
        s = s.replace(c, " ")
    s = s.replace("«", '"').replace("»", '"')
    s = re.sub(r"[‐-―]", " ", s)          # guiones de todo tipo
    s = re.sub(r"[^a-z0-9ñ%€ ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def negritas(tema):
    """Fragmentos en negrita, sin los rótulos de tabla ni los de una palabra."""
    fuera = []
    for m in re.finditer(r"\*\*(.+?)\*\*", tema, re.S):
        t = limpia(m.group(1))
        if len(t.split()) >= 2:
            fuera.append((m.group(1).strip(), t))
    return fuera


def main():
    tema = open(sys.argv[1], encoding="utf-8").read()
    fuente = " ".join(limpia(open(f, encoding="utf-8").read()) for f in sys.argv[2:])

    neg = negritas(tema)
    fuera = [(bruto, t) for bruto, t in neg if t not in fuente]

    print("## Negritas que no son literales de la fuente\n")
    for bruto, _ in fuera:
        print("  · " + " ".join(bruto.split())[:110])

    # las cifras se comprueban aparte: da igual que la frase sea paráfrasis, el
    # número tiene que estar en el documento
    print("\n## Cifras en negrita que no aparecen en ninguna fuente\n")
    huerfanas = 0
    for bruto, t in neg:
        for c in re.findall(r"\d+(?:[.,]\d+)?", t):
            if re.search(r"(?<![\d,.])" + re.escape(c) + r"(?![\d,.])", fuente):
                continue
            # ¿está escrita con letra?  se comprueban las que el examen usa
            print(f"  · «{c}» en: {' '.join(bruto.split())[:90]}")
            huerfanas += 1

    print()
    print("negritas comprobadas: %d ; no literales: %d ; cifras huérfanas: %d"
          % (len(neg), len(fuera), huerfanas))


if __name__ == "__main__":
    main()
