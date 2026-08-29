#!/usr/bin/env python3
"""Separa las opciones de una pregunta de test, con los dos maquetados del BOE.

Los cuadernillos vienen en dos formas:

  1. **Intercalada**: «a) texto  b) texto  c) texto  d) texto».
  2. **Agrupada**: «a) b) c) d)» y después los cuatro textos seguidos, que es
     como salen los PDF a dos columnas. Emparejar cada letra con lo que va justo
     detrás da la respuesta equivocada, y ya ha provocado tres falsas alarmas:
     el Tribunal de Cuentas, la aportación del artículo 6 de la Ley 8/2009 y las
     vacaciones del artículo 60 del convenio.

Uso:  opciones.py <fichero del banco> "<texto que identifique la pregunta>"
"""
import re
import sys


def separa(cuerpo):
    """Devuelve (enunciado, {letra: texto}, aviso).

    Si el maquetado está agrupado y no se puede repartir con seguridad, no se
    inventa: se devuelve un aviso para que se mire el PDF. Emparejar mal es peor
    que no emparejar.
    """
    c = re.sub(r"\s+", " ", cuerpo).strip()
    marcas = [(m.group(1), m.start(), m.end()) for m in re.finditer(r"\b([a-d])\)", c)]
    vistas, limpio = set(), []
    for l, i, f in marcas:
        if l not in vistas:
            vistas.add(l)
            limpio.append((l, i, f))
    if len(limpio) < 2:
        return c, {}, "no se localizan las opciones"

    enunciado = c[:limpio[0][1]].strip()
    huecos = []
    for k, (l, i, f) in enumerate(limpio):
        fin = limpio[k + 1][1] if k + 1 < len(limpio) else len(c)
        huecos.append((l, c[f:fin].strip()))

    vacios = [l for l, t in huecos if len(t) < 3]
    if not vacios:
        return enunciado, dict(huecos), ""

    # maquetado agrupado: las letras van juntas y los textos detrás
    cola = huecos[-1][1] if huecos[-1][1] else ""
    for l, t in huecos:
        if t and len(t) > 3:
            cola = t
            break
    trozos = [x.strip() for x in
              re.split(r"(?<=[.\)])\s+(?=[A-ZÁÉÍÓÚÑ¿«])", cola) if x.strip()]
    if len(trozos) == len(limpio):
        return enunciado, dict(zip([l for l, _ in huecos], trozos)), ""
    return enunciado, {}, ("maquetado agrupado (%d letras juntas, %d textos "
                           "sueltos): mira el PDF antes de fiarte"
                           % (len(vacios), len(trozos)))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    texto = open(sys.argv[1], encoding="utf-8").read()
    aguja = sys.argv[2].lower()
    patron = r"\*\*([^*]+?) · nº (\d+) · respuesta: (\w+)\*\*\n\n```\n(.*?)\n```"
    for m in re.finditer(patron, texto, re.S):
        cuerpo = m.group(4)
        if aguja not in re.sub(r"\s+", " ", cuerpo).lower():
            continue
        enunciado, ops, aviso = separa(cuerpo)
        print("%s · nº%s" % (m.group(1), m.group(2)))
        print("  %s" % enunciado[:300])
        if aviso:
            print("    !! %s" % aviso)
            print("    %s" % re.sub(r"\s+", " ", cuerpo)[:600])
        for l in sorted(ops):
            marca = " <-- OFICIAL" if l == m.group(3) else ""
            print("    %s) %s%s" % (l, ops[l][:200], marca))
        print()


if __name__ == "__main__":
    main()
