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
    y la extensión medida. Los cuatro primeros
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
import glob
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
    """La ficha de cabecera del tema.

    **No cita ficheros del proyecto.** La ficha la lee quien estudia, y a quien
    estudia no le dice nada dónde está guardado el esquema ni cómo se llama el
    informe que verificó el tema. Esas dos filas estaban aquí y se quitaron; el
    rastro de la verificación vive en los informes, que es donde toca.
    """
    # el bloque común lo estudian las tres ocupaciones tipo; un tema del
    # específico, solo la suya. La columna «sirve» lo dice cuando hace falta y
    # se queda vacía cuando vale el reparto de siempre
    filas = [
        ("Bloque", fila["bloque"]),
        ("Sirve para", fila.get("sirve") or
                       "**Producción (Asistencia)** · **Documentación** · "
                       "**Información y Contenidos**"),
        ("Fuente", fila["norma"]),
        ("Identificador", fila["identificador"]),
        ("Redacción que se estudia", fila["redaccion"]),
    ]
    # un tema puede apoyarse en una segunda norma que el enunciado no cita; la
    # columna «extra» añade esas filas sin tener que tocar este código otra vez
    for par in (fila.get("extra") or "").split(" | "):
        if "=" in par:
            k, _, v = par.partition("=")
            filas.append((k.strip(), v.strip()))
    filas.append(
        ("Extensión", "**%s palabras**" % format(palabras, ",d").replace(",", "."))
    )
    # y se comprueba que no se cuele ninguna ruta del proyecto en lo que el
    # opositor va a leer
    for k, v in filas:
        if re.search(r"(?:esquemas|informes|fuentes|herramientas|banco)/", str(v)):
            print("  ! %s: la fila «%s» cita una ruta del proyecto" % (ruta, k))

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


def mete(texto, bloque, ini, fin, delante_del_primer_epigrafe=False):
    """Sustituye el bloque si ya está; si no, lo coloca donde toca.

    Dos sitios, y la diferencia importa:

    · La **portada** va **pegada al título**: es la ficha del tema y lo primero
      que hay que ver.
    · El **índice** va **justo antes del primer epígrafe**. Todo lo que hay entre
      el título y ese epígrafe es preámbulo —la entradilla del esquema, el
      enunciado de la convocatoria en el tema— y enterrarlo bajo veinte líneas de
      índice empeora la primera pantalla. La regla es esa y no «saltar la
      entradilla»: hay esquemas cuyo cuerpo son párrafos corridos, y saltarlos
      mandaba el índice a la mitad del documento.
    """
    if ini in texto and fin in texto:
        return re.sub(re.escape(ini) + r".*?" + re.escape(fin), lambda _: bloque,
                      texto, flags=re.S)
    if delante_del_primer_epigrafe:
        m = re.search(r"(?m)^## ", texto)
        if m:
            return texto[:m.start()] + bloque + "\n\n" + texto[m.start():]
    m = re.search(r"(?m)^# .+?$\n", texto)
    if not m:
        sys.exit("el fichero no empieza por un título de primer nivel")
    return texto[:m.end()] + "\n" + bloque + "\n" + texto[m.end():]


def main():
    filas = {}
    with open(DATOS, encoding="utf-8") as f:
        cab = f.readline().rstrip("\n").split("\t")
        for linea in f:
            if linea.strip():
                v = linea.rstrip("\n").split("\t")
                filas[v[0]] = dict(zip(cab, v))

    # sin argumentos: los temas del .tsv y todos los esquemas. El esquema no
    # lleva portada —la ficha de la norma está en su tema y repetirla sería
    # ruido—, pero sí índice: son de cien a doscientas líneas de telegrama y sin
    # índice no se salta a un epígrafe
    rutas = sys.argv[1:] or list(filas) + sorted(glob.glob("esquemas/*/*.md"))
    for ruta in rutas:
        texto = open(ruta, encoding="utf-8").read()
        palabras = len(cuerpo(texto).split())
        # el índice va antes del primer epígrafe y la portada pegada al título
        texto = mete(texto, indice(texto), I_INI, I_FIN,
                     delante_del_primer_epigrafe=True)
        if ruta in filas:
            texto = mete(texto, portada(ruta, filas[ruta], palabras), P_INI, P_FIN)
        open(ruta, "w", encoding="utf-8").write(texto)
        print("· %-42s %5d palabras · %2d epígrafes%s"
              % (ruta, palabras, len(epigrafes(texto)),
                 "" if ruta in filas else "  (sin portada: es un esquema)"))


if __name__ == "__main__":
    main()
