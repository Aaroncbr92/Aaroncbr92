#!/usr/bin/env python3
"""Refutación por exactitud: cada negrita del tema, contra su artículo.

El tema pone en negrita lo que es literal de la norma o casi. Este script troceo
el tema por artículos, saca las negritas de cada trozo y busca cada una en el
texto del artículo correspondiente. Lo que no aparece se imprime para mirarlo a
mano: puede ser una paráfrasis legítima, o puede ser una invención.

Uso:  refutar_exactitud.py <tema.md> <fuente.md>
"""
import re
import sys
import unicodedata


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("«", '"').replace("»", '"').replace("—", " ").replace("–", " ")
    s = re.sub(r"[^a-z0-9ñ ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def articulos(fuente):
    fuera = {}
    patron = r"^## \[[^\]]+\] Artículo (\d+)$\n\n_.*?_\n\n(.*?)(?=\n## |\Z)"
    for m in re.finditer(patron, fuente, re.S | re.M):
        fuera[int(m.group(1))] = limpia(m.group(2))
    return fuera


def trozos(tema):
    """Devuelve [(nº de artículo, texto del tema que habla de él)]."""
    # el tema marca los artículos en negrita o como encabezado: si solo se busca
    # una de las dos formas, la comprobación no mira nada y no se queja
    # "Art. 104" cuenta igual que "Artículo 104": si solo se reconoce la forma
    # larga, los artículos abreviados no abren bloque y sus negritas se
    # comprueban contra el artículo anterior, que es el error de atribución
    marcas = list(re.finditer(
        r"(?:\*\*|(?m:^)#{2,4} )(?:Artículos?|Arts?\.) ?(\d+)"
        r"(?: y (\d+))?(?: a (\d+))?[.,: ]", tema))
    # el bloque de un artículo termina en el siguiente artículo, en el siguiente
    # encabezado o en la siguiente raya: si no se acota, el último artículo se
    # traga el resto del tema y todo lo de después sale marcado como suyo
    cortes = [m.start() for m in re.finditer(r"(?m)^#{2,4} |^---$", tema)]
    fuera = []
    for i, m in enumerate(marcas):
        candidatos = [c for c in cortes if c > m.start()]
        fin = min([marcas[i + 1].start()] if i + 1 < len(marcas) else [len(tema)]
                  + ([candidatos[0]] if candidatos else []))
        if candidatos and i + 1 < len(marcas):
            fin = min(marcas[i + 1].start(), candidatos[0])
        nums = [int(g) for g in m.groups() if g]
        if len(nums) == 2 and m.group(3):
            nums = list(range(nums[0], nums[1] + 1))
        fuera.append((nums, tema[m.start():fin]))
    return fuera


def main():
    tema = open(sys.argv[1], encoding="utf-8").read()
    fuente = open(sys.argv[2], encoding="utf-8").read()
    arts = articulos(fuente)

    total = sospechosas = 0
    for nums, bloque in trozos(tema):
        cuerpo = " ".join(arts.get(n, "") for n in nums)
        if not cuerpo:
            continue
        for negrita in re.findall(r"\*\*(.+?)\*\*", bloque):
            frag = limpia(negrita)
            if len(frag.split()) < 3:       # una o dos palabras no dice nada
                continue
            if frag.startswith("articulo"):  # el propio encabezado
                continue
            total += 1
            if frag not in cuerpo:
                sospechosas += 1
                print("art. %-14s %s" % (",".join(str(n) for n in nums), negrita))
    print()
    print("negritas comprobadas: %d ; no literales: %d" % (total, sospechosas))


if __name__ == "__main__":
    main()
