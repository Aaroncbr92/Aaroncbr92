#!/usr/bin/env python3
"""Portada e índice de cada tema, generados y regenerables.

Un tema de quince o veinte mil palabras no se navega sin índice, y el opositor
que lo abre necesita saber en la primera pantalla **qué norma es, en qué
redacción y para qué ocupación sirve**. Las dos cosas se generan aquí y no se
escriben a mano, porque un índice escrito a mano se queda viejo al primer
epígrafe que se añade —y un índice viejo no da error: lleva a otro sitio.

Qué hace:

  · **Portada.** Una tabla con el bloque del programa, la norma, su
    identificador, la redacción sobre la que se estudia, la extensión medida y
    dónde están el esquema y los informes de verificación. Los cuatro primeros
    campos salen de `herramientas/portadas.tsv`, que se rellena leyendo la
    trazabilidad de cada tema; la extensión y las rutas se calculan aquí, así
    que no se quedan viejas.
  · **Índice.** Los epígrafes `##` y `###` del tema, con enlace. Los anclajes se
    construyen con la regla de GitHub: minúsculas, fuera todo lo que no sea
    letra, cifra, guion o espacio, y los espacios a guiones. Los repetidos
    llevan sufijo, como hace GitHub.

Ambos bloques van entre marcas HTML, así que **volver a pasar el script
sustituye lo anterior** en vez de duplicarlo. Se puede correr las veces que haga
falta.

Uso:  indice.py                     # todos los temas del .tsv
      indice.py temas/general/01-*.md
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tema import cuerpo   # una sola idea de dónde empieza el tema

DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portadas.tsv")
P_INI, P_FIN = "<!-- portada -->", "<!-- /portada -->"
I_INI, I_FIN = "<!-- indice -->", "<!-- /indice -->"


def ancla(texto, vistos):
    """Anclaje al estilo de GitHub, con el sufijo de los repetidos."""
    a = texto.strip().lower()
    a = a.replace("`", "")
    # se conservan las letras acentuadas, que GitHub sí conserva; se van los
    # signos (·, «», puntos, paréntesis) y los espacios pasan a guiones
    a = "".join(c for c in a if c.isalnum() or c in " -_")
    # GitHub cambia cada espacio por un guion **sin juntarlos**: si el rótulo
    # llevaba un "·" entre dos espacios, al quitarlo quedan dos guiones seguidos
    # en el anclaje. Colapsarlos aquí rompería justo ese enlace y solo ése, que
    # es la clase de fallo que no se ve hasta que alguien lo pulsa
    a = a.strip().replace(" ", "-")
    n = vistos.get(a, 0)
    vistos[a] = n + 1
    return a if n == 0 else "%s-%d" % (a, n)


def epigrafes(tema):
    fuera, vistos = [], {}
    for m in re.finditer(r"(?m)^(#{2,3}) +(.+?)\s*$", cuerpo(tema)):
        titulo = m.group(2).strip()
        if titulo.lower() in ("índice", "indice"):
            continue
        fuera.append((len(m.group(1)), titulo, ancla(titulo, vistos)))
    return fuera


def limpia_negritas(s):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", s)


def portada(ruta, fila, palabras):
    base = os.path.splitext(os.path.basename(ruta))[0]
    carpeta = "general" if "/general/" in ruta else "prl"
    esquema = "esquemas/%s/%s.md" % (carpeta, base)
    informes = fila["informes"]
    filas = [
        ("Bloque", fila["bloque"]),
        ("Sirve para", "**Producción (Asistencia)** · **Documentación** · "
                       "**Información y Contenidos**"),
        ("Fuente", fila["norma"]),
        ("Identificador", fila["identificador"]),
        ("Redacción que se estudia", fila["redaccion"]),
        ("Extensión", "**%s palabras**" % format(palabras, ",d").replace(",", ".")),
        ("Esquema de repaso", "`%s`" % esquema),
        ("Verificación", informes),
    ]
    # una portada que cita un fichero que no existe no da error: manda al opositor
    # a una ruta muerta. Los temas 2 y 3 citaban un informe de refutación que
    # nunca se había escrito, y así se descubrió
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for _, v in filas:
        for r in re.findall(r"`((?:esquemas|informes|fuentes)/[^`]+)`", str(v)):
            if not os.path.exists(os.path.join(raiz, r)):
                print("  ! %s cita una ruta que no existe: %s" % (ruta, r))

    salida = [P_INI, "", "|  |  |", "| --- | --- |"]
    salida += ["| **%s** | %s |" % (k, v) for k, v in filas]
    salida += ["", P_FIN]
    return "\n".join(salida)


def indice(tema):
    salida = [I_INI, "", "## Índice", ""]
    for nivel, titulo, a in epigrafes(tema):
        sangria = "" if nivel == 2 else "  "
        salida.append("%s- [%s](#%s)" % (sangria, limpia_negritas(titulo), a))
    salida += ["", I_FIN]
    return "\n".join(salida)


def mete(tema, bloque, ini, fin):
    """Sustituye el bloque si ya está; si no, lo pone detrás del título."""
    if ini in tema and fin in tema:
        return re.sub(re.escape(ini) + r".*?" + re.escape(fin), lambda _: bloque,
                      tema, flags=re.S)
    m = re.search(r"(?m)^# .+?$\n", tema)
    if not m:
        sys.exit("el fichero no empieza por un título de primer nivel")
    return tema[:m.end()] + "\n" + bloque + "\n" + tema[m.end():]


def main():
    filas = {}
    with open(DATOS, encoding="utf-8") as f:
        cab = f.readline().rstrip("\n").split("\t")
        for linea in f:
            if linea.strip():
                v = linea.rstrip("\n").split("\t")
                filas[v[0]] = dict(zip(cab, v))

    rutas = sys.argv[1:] or list(filas)
    for ruta in rutas:
        if ruta not in filas:
            print("· %s: sin ficha en portadas.tsv, se salta" % ruta)
            continue
        tema = open(ruta, encoding="utf-8").read()
        palabras = len(cuerpo(tema).split())
        # el índice primero y la portada después: las dos se meten detrás del
        # título, así que la última en entrar es la que queda arriba
        tema = mete(tema, indice(tema), I_INI, I_FIN)
        tema = mete(tema, portada(ruta, filas[ruta], palabras), P_INI, P_FIN)
        open(ruta, "w", encoding="utf-8").write(tema)
        print("· %-42s %5d palabras · %2d epígrafes"
              % (ruta, palabras, len(epigrafes(tema))))


if __name__ == "__main__":
    main()
