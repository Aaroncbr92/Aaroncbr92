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
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tema import cuerpo as sin_envoltorio
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
    # el guion blando U+00AD es invisible y marca el punto en que el PDF parte
    # la palabra: se quita entero, igual que hace la lente de citas
    s = re.sub("\u00ad\\s*\\n\\s*", "", s).replace("\u00ad", "")
    # un PDF parte las palabras al final del renglón: "distancias vi-\nsuales".
    # Si el guion se cambia por un espacio, esa palabra queda rota y una cita
    # copiada literalmente sale marcada como "no literal". Eso adiestra a no
    # mirar la lista, que es donde se esconde el hallazgo de verdad: primero se
    # cose la palabra partida y luego se tratan los demás guiones
    # ojo con la clase: "[‐-―]" es el rango U+2010..U+2015 y NO incluye el guion
    # normal U+002D, que es justo el que usan los PDF para partir palabras
    s = re.sub(r"[-‐-―]\s*\n\s*", "", s)
    s = re.sub(r"[-‐-―]", " ", s)         # los guiones que quedan, separadores
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
    # fuera la portada y el índice: son envoltorio, no afirmaciones del tema
    tema = sin_envoltorio(open(sys.argv[1], encoding="utf-8").read())
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
