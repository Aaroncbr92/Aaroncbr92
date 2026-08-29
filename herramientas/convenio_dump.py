#!/usr/bin/env python3
"""Convierte el III Convenio Colectivo en un volcado con la forma que esperan
las lentes de refutación (## [id] Artículo N).

El convenio no es legislación consolidada: el BOE no publica texto refundido,
así que la redacción en vigor hay que reconstruirla superponiendo el texto de
2020 y el acuerdo de modificación de 2022. Este script hace justo eso, y deja
constancia en cada artículo de qué documento viene su redacción.

Se queda solo con el articulado del convenio (hasta el anexo 1): los anexos
tienen numeración propia —el anexo 4 vuelve a empezar en el artículo 1— y
mezclarlos haría que la comprobación contrastase negritas contra el artículo
equivocado, que es peor que no comprobar nada.

Uso:  convenio_dump.py > fuentes/convenio/CONVENIO.md
"""
import re
import sys

BASE = "fuentes/convenio/BOE-A-2020-16744.txt"
MOD = "fuentes/convenio/BOE-A-2022-20256.txt"
CORTE_BASE = " ANEXO 1"       # a partir de aquí empieza otra numeración
CORTE_MOD = " ANEXO VIII"


def articulos(ruta, corte):
    t = open(ruta, encoding="utf-8").read()
    # el acuerdo de 2022 llega con espacios duros y "em space" dentro de los
    # rótulos ("Artículo\xa063.\u2003Retribuciones"): sin normalizarlos, el
    # patrón no encuentra ningún artículo y el volcado sale con la redacción
    # de 2020 sin avisar de nada
    t = re.sub(r"[\u00a0\u2000-\u200a\u202f\u205f\u3000]", " ", t)
    pos = t.find("\n" + corte)
    if pos > 0:
        t = t[:pos]
    marcas = list(re.finditer(r"(?m)^ Artículo (\d+)\.?\s*(.*)$", t))
    fuera = {}
    for i, m in enumerate(marcas):
        fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(t)
        cuerpo = t[m.end():fin]
        # las tablas del BOE llegan como filas de "|" sueltas: no son texto
        cuerpo = "\n".join(l for l in cuerpo.splitlines()
                           if l.strip() and not l.strip().startswith("|"))
        fuera[int(m.group(1))] = (m.group(2).strip(), cuerpo.strip())
    return fuera


def main():
    base = articulos(BASE, CORTE_BASE)
    mod = articulos(MOD, CORTE_MOD)
    print("# III Convenio Colectivo de la Corporación RTVE — articulado\n")
    print("Reconstruido a 21/12/2022 superponiendo BOE-A-2022-20256 sobre "
          "BOE-A-2020-16744. No existe versión consolidada oficial.\n")
    for n in sorted(set(base) | set(mod)):
        if n in mod:
            titulo, cuerpo = mod[n]
            origen = "BOE-A-2022-20256"
        else:
            titulo, cuerpo = base[n]
            origen = "BOE-A-2020-16744"
        print(f"## [{origen}] Artículo {n}\n")
        print(f"_{titulo}_\n")
        print(cuerpo + "\n")
    sust = sorted(mod)
    print(f"<!-- artículos con redacción de 2022: {sust} -->", file=sys.stderr)


main()
