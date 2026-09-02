#!/usr/bin/env python3
"""Lector de normas de la Unión Europea publicadas en el BOE.

`boe.py` sirve para la legislación española consolidada: pide a la API el
árbol de bloques de una norma y elige, precepto a precepto, la redacción
vigente a una fecha. Un reglamento europeo no está ahí. El BOE lo publica en
su sección del Diario Oficial de la Unión Europea, con identificador propio
—el Reglamento general de protección de datos es `DOUE-L-2016-80807`—, pero
**en su texto original y sin consolidar**: las correcciones de errores son
documentos aparte y nadie las incorpora.

Así que este lector hace dos cosas y avisa de la tercera:

  · **Trocea el articulado** con la misma forma que espera `boe.py`
    (`## [aN] Artículo N`), para que las cuatro lentes de refutación puedan
    trabajar sobre el reglamento igual que sobre una ley española.
  · **Recoge las correcciones de errores** que el propio BOE enlaza en el
    bloque de «referencias posteriores», y las guarda al lado, enteras.
  · **Dice en la cabecera que el texto no está consolidado**, y qué
    correcciones hay que leer junto a él. Un volcado que se presentase como
    consolidado sin serlo es peor que no tenerlo: se lee como definitivo.

Uso:  doue.py DOUE-L-2016-80807 fuentes/corte-20221221/
"""
import html
import os
import re
import subprocess
import sys

WEB = "https://www.boe.es/buscar/doc.php?id="


def traer(url):
    r = subprocess.run(["curl", "-sSL", "--max-time", "120", url],
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("error de red: %s" % r.stderr.strip())
    return r.stdout


def texto_plano(bruto):
    t = re.sub(r"(?s)<script.*?</script>|<style.*?</style>", "", bruto)
    t = re.sub(r"(?i)<(p|div|li|h[1-6]|tr|br)[^>]*>", "\n", t)
    t = re.sub(r"(?i)</(p|div|li|h[1-6]|tr)>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    # el DOUE separa el número del artículo con espacio duro y el ordinal del
    # apartado con un cuadratín: «Artículo\xa02.\u2003Ámbito». Sin normalizarlos
    # el patrón no reconoce ni un artículo y el volcado sale vacío sin dar error
    t = t.translate({0xa0: " ", 0x2002: " ", 0x2003: " ", 0x2009: " ",
                     0x202f: " ", 0x3000: " "})
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n[ \t]*", "\n", t)
    return re.sub(r"\n{2,}", "\n", t)


def cabecera(t):
    """(título, publicado en) del documento."""
    # el rótulo «Documento DOUE-...» sale dos veces seguidas —migas de pan y
    # encabezado— y un patrón anclado en él se comía la segunda al consumir la
    # primera. El título es la línea que va justo antes de «Publicado en:», que
    # es una sola y no se repite
    m = re.search(r"(?m)^(.+)\nPublicado en:$", t)
    titulo = m.group(1).strip() if m else ""
    m = re.search(r"Publicado en:\s*\n(.+)", t)
    return titulo, (m.group(1).strip() if m else "")


def correcciones(t):
    """Los identificadores de las correcciones de errores que enlaza el BOE."""
    trozo = t[t.find("Referencias posteriores"):t.find("Referencias posteriores") + 4000]
    fuera = []
    for m in re.finditer(r"en (DOUE [^(]+)\(Ref\.\s*(DOUE-[\w-]+)", trozo):
        fuera.append((m.group(2), re.sub(r"\s+", " ", m.group(1)).strip()))
    return fuera


def articulado(t):
    """[(nº, título, cuerpo)] del articulado."""
    ini = t.find("TEXTO ORIGINAL")
    t = t[ini:] if ini > 0 else t
    marcas = list(re.finditer(r"(?m)^Artículo (\d+)\.\s*(.*)$", t))
    fuera = []
    for i, m in enumerate(marcas):
        fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(t)
        fuera.append((m.group(1), m.group(2).strip(), t[m.end():fin].strip()))
    return fuera


def main(ident, destino):
    t = texto_plano(traer(WEB + ident))
    titulo, publicado = cabecera(t)
    corr = correcciones(t)
    arts = articulado(t)
    if not arts:
        raise SystemExit("no se ha reconocido ningún artículo: revisa el volcado")

    os.makedirs(destino, exist_ok=True)
    ruta = os.path.join(destino, "%s.md" % ident)
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("# %s — %s\n\n" % (ident, titulo))
        fh.write("Publicado en %s.\n\n" % publicado)
        fh.write("**Este texto NO está consolidado.** El BOE publica el "
                 "documento tal como salió en el Diario Oficial de la Unión "
                 "Europea; las correcciones de errores son documentos aparte y "
                 "no se incorporan al texto. Hay que leerlas al lado:\n\n")
        for ref, donde in corr:
            fh.write("- `%s` — %s\n" % (ref, donde))
        if not corr:
            fh.write("- Ninguna registrada.\n")
        fh.write("\nVolcado con `herramientas/doue.py`. No se edita a mano.\n\n")
        for n, tit, cuerpo in arts:
            fh.write("## [a%s] Artículo %s\n\n" % (n, n))
            fh.write("_Texto original, sin consolidar. Contrástalo con las "
                     "correcciones de errores listadas arriba._\n\n")
            fh.write("Artículo %s. %s\n%s\n\n" % (n, tit, cuerpo))
    print("%s · %d artículos · %d correcciones de errores"
          % (ruta, len(arts), len(corr)))

    for ref, _ in corr:
        c = texto_plano(traer(WEB + ref))
        i, j = c.find("TEXTO ORIGINAL"), c.find("Referencias posteriores")
        rc = os.path.join(destino, "%s.md" % ref)
        with open(rc, "w", encoding="utf-8") as fh:
            fh.write("# %s — corrección de errores de %s\n\n" % (ref, ident))
            fh.write(c[i:j if j > i else len(c)].strip() + "\n")
        print("  · %s" % rc)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
