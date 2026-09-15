#!/usr/bin/env python3
"""Caza el nueve leído como cuatro **cuando la cifra correcta es posible**.

**El problema que `correos_cifras.py` no puede resolver.** Aquella herramienta
descarta lo imposible: un año 1478, una norma «N/1447». Pero el tema 3 del
documento de Correos es un catálogo de productos, y sus cifras son pesos,
medidas, plazos y porcentajes: **«43 %» es tan posible como «93 %»**, y
**«4x14 cm» tan posible como «9x14 cm»**. Ahí no hay rango que valga.

**Lo que sí hay es repetición.** Un catálogo describe decenas de productos con
los mismos campos, y **la misma medida vuelve a aparecer a las pocas páginas**.
Cuando el volcado trae **«14x9 cm» trece veces y «14x4 cm» una**, la rara es la
sospechosa; cuando trae «93 %» y «43 %» del mismo plazo de entrega, igual.

Esta herramienta busca **parejas gemelas**: dos cifras del volcado que se
diferencian **sólo en que un 4 de una es un 9 en la otra**. Cuando las dos
aparecen, imprime las dos con su recuento, **y la menos frecuente encabeza la
sospecha**. No corrige nada: **una gemela no prueba nada por sí sola** —«24» y
«29» son dos números legítimos y distintos—; lo que hace es **poner delante las
pocas que merecen un viaje a la página impresa**, en vez de las miles que no.

Uso:
    python3 herramientas/correos_gemelas.py fuentes/correos-referencia/tema-03.txt
"""
import collections
import re
import sys

# Sólo cifras de dos a seis dígitos: las de un dígito dan ruido puro («4» y «9»
# aparecen en cualquier página) y las más largas son códigos, no medidas.
CIFRA = re.compile(r"(?<![\d.,])(\d{2,6})(?![\d])")


def gemelas(n):
    """Todas las variantes de `n` con un 4 cambiado por un 9."""
    return {n[:i] + "9" + n[i + 1:] for i, c in enumerate(n) if c == "4"}


def revisa(fichero):
    cuenta = collections.Counter()
    donde = collections.defaultdict(list)
    pagina = "?"
    for num, linea in enumerate(open(fichero, encoding="utf-8"), 1):
        m = re.match(r"\[\[ página (\d+) de", linea)
        if m:
            pagina = m.group(1)
            continue
        for mm in CIFRA.finditer(linea):
            c = mm.group(1)
            cuenta[c] += 1
            if len(donde[c]) < 4:
                donde[c].append((pagina, num, linea.strip()[:70]))
    salida = []
    for con4 in sorted(cuenta):
        if "4" not in con4:
            continue
        for con9 in gemelas(con4):
            if con9 in cuenta:
                salida.append((cuenta[con4], con4, cuenta[con9], con9))
    return salida, donde


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for f in sys.argv[1:]:
        pares, donde = revisa(f)
        # la más sospechosa primero: la que aparece una vez frente a una gemela
        # que aparece muchas
        pares.sort(key=lambda p: (p[0], -p[2]))
        print("== %s" % f.split("/")[-1])
        for n4, c4, n9, c9 in pares:
            print("   %-8s %3d  ·  %-8s %3d" % (c4, n4, c9, n9))
            for pagina, linea, texto in donde[c4]:
                print("        pág %-4s renglón %-6d %s" % (pagina, linea, texto))
        print("\nparejas gemelas: %d" % len(pares))


if __name__ == "__main__":
    main()
