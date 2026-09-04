#!/usr/bin/env python3
"""Comprueba a dónde apunta cada remisión interna de un volumen.

**Ninguna de las cinco lentes mira esto.** Un tema puede decir «los agentes
químicos, en el tema 16» con toda corrección formal y estar mandando al lector
a los agentes biológicos: no hay cita que falle, no hay cifra huérfana y no hay
negrita rota. Se descubrió en el volumen de Enfermería, donde convivieron dos
numeraciones distintas del mismo programa, y **volvió a aparecer después en una
tabla que la primera revisión no tocó**.

Esta herramienta no decide: **imprime cada remisión con el título del tema al
que apunta**, para leerlas de una vez y ver la que no encaja. Es una lista para
mirar, no un veredicto.

Uso:  remisiones.py temas/enfermeria
"""
import os
import re
import sys


def main():
    carpeta = sys.argv[1] if len(sys.argv) > 1 else "temas/enfermeria"
    ficheros = sorted(f for f in os.listdir(carpeta) if f.endswith(".md"))
    titulos = {}
    for f in ficheros:
        n = int(f.split("-", 1)[0])
        cab = open(os.path.join(carpeta, f), encoding="utf-8").readline()
        titulos[n] = cab.split("·", 1)[-1].strip()
    total = 0
    for f in ficheros:
        propio = int(f.split("-", 1)[0])
        texto = open(os.path.join(carpeta, f), encoding="utf-8").read()
        # se salta la primera línea: «# Tema N del específico…» no es remisión
        texto = texto.split("\n", 1)[1]
        vistas = []
        for m in re.finditer(r"\b[Tt]emas?\s+((?:\d+)(?:\s*(?:,|y)\s*\d+)*)", texto):
            for num in re.findall(r"\d+", m.group(1)):
                n = int(num)
                if n == propio:
                    continue
                ctx = re.sub(r"\s+", " ", texto[max(0, m.start() - 70):m.start()])[-70:]
                vistas.append((n, ctx))
        if not vistas:
            continue
        print("== %s" % f)
        for n, ctx in vistas:
            total += 1
            print("   tema %2d → %-62s  ← …%s" % (n, titulos.get(n, "¡NO EXISTE!"), ctx))
    print("\nremisiones listadas: %d" % total)


if __name__ == "__main__":
    main()
