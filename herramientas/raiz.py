#!/usr/bin/env python3
"""Sobre qué oposición se está trabajando.

El repositorio sirve a varias oposiciones —RTVE, Correos y Auxiliar de la AGE—
con **el mismo método y las mismas herramientas**. Lo que cambia de una a otra
son los datos: su convocatoria, sus temas, sus esquemas, sus fuentes, su banco
de preguntas y su catálogo de volúmenes. Cada una vive en su carpeta, y esa
carpeta es la **raíz de trabajo**: las herramientas resuelven contra ella todas
las rutas del proyecto y así ninguna necesita saber de las demás.

Una carpeta es una oposición cuando lleva un `OPOSICION.md`. Se elige en este
orden:

  1. La variable de entorno `OPO`, que la nombra:
     `OPO=correos python3 herramientas/banco.py`
  2. La carpeta actual, o la primera por encima de ella que lleve la marca:
     `cd rtve && python3 ../herramientas/banco.py`

Y si no hay ninguna de las dos, la herramienta se para y enseña las que hay.
**No hay oposición por defecto, y es a propósito.** Cuando sólo había una, la
raíz era la del repositorio y no había nada que elegir. Con tres, equivocarse
no da error: escribe el banco de preguntas de una encima del de otra, deja el
fichero con buena pinta y el fallo aparece semanas después, dentro de un
volumen. Más vale pararse.
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARCA = "OPOSICION.md"

_raiz = None


def oposiciones():
    """Las carpetas del repositorio que llevan la marca."""
    return sorted(n for n in os.listdir(REPO)
                  if os.path.isfile(os.path.join(REPO, n, MARCA)))


def _para(recado):
    print("herramientas: %s" % recado, file=sys.stderr)
    hay = oposiciones()
    if hay:
        print("  Oposiciones del repositorio: %s" % " · ".join(hay), file=sys.stderr)
        print("  Se elige con «OPO=%s ...» o entrando en su carpeta." % hay[0],
              file=sys.stderr)
    sys.exit(2)


def raiz():
    """La carpeta de la oposición sobre la que se trabaja."""
    global _raiz
    if _raiz:
        return _raiz

    opo = os.environ.get("OPO")
    if opo:
        destino = opo if os.path.isabs(opo) else os.path.join(REPO, opo)
        if not os.path.isfile(os.path.join(destino, MARCA)):
            _para("OPO=%s no es una oposición: no encuentro su %s." % (opo, MARCA))
        _raiz = os.path.abspath(destino)
        return _raiz

    # Se sube desde la carpeta actual. Así vale tanto estar en la raíz de la
    # oposición como dentro de `temas/general/`, que es donde se está cuando se
    # escribe un tema.
    subiendo = os.path.abspath(os.getcwd())
    while True:
        if os.path.isfile(os.path.join(subiendo, MARCA)):
            _raiz = subiendo
            return _raiz
        padre = os.path.dirname(subiendo)
        if padre == subiendo:
            break
        subiendo = padre

    _para("no sé sobre qué oposición trabajo.")


def ruta(*partes):
    """Una ruta del proyecto, resuelta contra la raíz de la oposición."""
    return os.path.join(raiz(), *partes)


def desde_aqui(camino):
    """Un camino escrito en la línea de órdenes.

    Se admite tal cual si existe —el uso normal, trabajando dentro de la carpeta
    de la oposición—; y si no existe, se busca dentro de la raíz, que es lo que
    hace falta cuando se manda `OPO=rtve` desde la raíz del repositorio. Si no
    está en ninguno de los dos sitios se devuelve como vino, para que el error
    lo dé quien lo abre y lo diga con el nombre que se escribió.
    """
    if os.path.exists(camino):
        return camino
    dentro = os.path.join(raiz(), camino)
    return dentro if os.path.exists(dentro) else camino


def relativo(camino):
    """El mismo camino, dicho desde la raíz de la oposición.

    Es como se nombra un tema en `portadas.tsv` y en `bloques.py`: `temas/…`,
    sin la carpeta de la oposición delante. Un camino de fuera de la raíz se
    devuelve tal cual, porque relativizarlo daría una ristra de `../`.
    """
    entero = os.path.abspath(camino)
    if entero.startswith(raiz() + os.sep):
        return os.path.relpath(entero, raiz())
    return camino


def catalogo():
    """El `bloques.py` de la oposición: su fecha de corte y sus volúmenes.

    Es lo único que `libro.py` no puede llevar dentro, porque es distinto en
    cada oposición: qué volúmenes se arman, de qué temas y con qué avisos. El
    armazón —portada, índice, maquetación, respuestas al final— es común y vive
    en la herramienta.
    """
    import importlib.util
    fichero = ruta("bloques.py")
    if not os.path.isfile(fichero):
        _para("%s no tiene todavía catálogo de volúmenes (falta su bloques.py)."
              % os.path.basename(raiz()))
    spec = importlib.util.spec_from_file_location("bloques", fichero)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


if __name__ == "__main__":
    print(raiz())
