#!/usr/bin/env python3
"""Lo que es cuerpo del tema y lo que es envoltorio.

La portada y el índice que genera `indice.py` van en negrita y llevan cifras
—la extensión medida, el número del punto del programa—, así que las lentes los
tomaban por afirmaciones del tema y los contrastaban contra la fuente. Ocho
falsos «no literales» y una cifra huérfana por tema, que no dan error: engordan
la lista que hay que repasar a mano hasta que uno deja de repasarla.

Una sola función, importada por las cuatro lentes y por el propio generador, para
que no haya dos ideas distintas de dónde empieza el tema.
"""
import re

MARCAS = (("<!-- portada -->", "<!-- /portada -->"),
          ("<!-- indice -->", "<!-- /indice -->"))


def cuerpo(texto):
    """El tema sin portada ni índice."""
    for ini, fin in MARCAS:
        texto = re.sub(re.escape(ini) + r".*?" + re.escape(fin), "", texto, flags=re.S)
    return texto
