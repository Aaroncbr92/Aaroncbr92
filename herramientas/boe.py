#!/usr/bin/env python3
"""Lector de legislación consolidada del BOE.

Resuelve las tres trampas del apartado 2 del manual:

  2.1  Un precepto trae encadenadas todas sus redacciones. Aquí se elige la
       vigente (última fecha de vigencia ya cumplida) y se enseña la cadena.
  2.2  Reformas cruzadas: si la redacción elegida por fecha de vigencia no es
       también la publicada más tarde, se avisa, porque ahí es donde una
       reforma se come a otra.
  2.3  Identificadores irregulares: el bloque se resuelve contra el índice
       real de la norma, nunca por analogía.

Uso:
  boe.py indice   BOE-A-1978-31229
  boe.py buscar   BOE-A-1978-31229 "artículo 24"
  boe.py precepto BOE-A-1978-31229 a24
  boe.py precepto BOE-A-1978-31229 --buscar "artículo 24"
"""

import re
import subprocess
import sys
import unicodedata
import xml.etree.ElementTree as ET
from datetime import date

API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id"
WEB = "https://www.boe.es/buscar/act.php?id="


def traer(url):
    r = subprocess.run(
        ["curl", "-sSL", "--max-time", "60", "-H", "Accept: application/xml", url],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        sys.exit("error de red: %s" % r.stderr.strip())
    try:
        raiz = ET.fromstring(r.stdout)
    except ET.ParseError:
        sys.exit("respuesta no es XML:\n%s" % r.stdout[:400])
    codigo = raiz.findtext("status/code", "")
    if codigo != "200":
        sys.exit("el BOE responde %s: %s" % (codigo, raiz.findtext("status/text", "")))
    return raiz


def normalizar(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


def indice(norma):
    raiz = traer("%s/%s/texto/indice" % (API, norma))
    # el índice devuelve el id como elemento hijo y el bloque suelto como
    # atributo: el BOE no es coherente ni consigo mismo (manual, 2.3)
    return [((b.get("id") or b.findtext("id") or "").strip(),
             (b.findtext("titulo") or "").strip())
            for b in raiz.iter("bloque")]


def cmd_indice(norma):
    for bid, titulo in indice(norma):
        print("%-16s %s" % (bid, titulo))


def cmd_buscar(norma, texto):
    objetivo = normalizar(texto)
    hits = [(b, t) for b, t in indice(norma)
            if objetivo in normalizar(t) or objetivo == normalizar(b)]
    if not hits:
        print("sin coincidencias para %r. Revisa el índice completo:" % texto)
        print("  boe.py indice %s" % norma)
        sys.exit(1)
    for bid, titulo in hits:
        print("%-16s %s" % (bid, titulo))
    return hits


# el BOE mete en el mismo bloque el texto y sus notas al pie; las notas son
# justamente donde avisa de nulidades y de normas no convalidadas (manual, 2.2)
CLASES_NOTA = ("nota_pie", "nota_pie_2")
ALARMAS = ("inconstitucional", "nulidad", "no convalidad", "derogación",
           "deroga", "suspende", "caducidad")


def texto_version(v):
    """Devuelve (texto normativo, notas del BOE)."""
    texto, notas = [], []
    for p in v.iter("p"):
        t = "".join(p.itertext()).strip()
        if not t:
            continue
        (notas if p.get("class") in CLASES_NOTA else texto).append(t)
    return "\n".join(texto), notas


def fecha(v, attr):
    return v.get(attr) or ""


def cmd_precepto(norma, bloque):
    raiz = traer("%s/%s/texto/bloque/%s" % (API, norma, bloque))
    b = next(raiz.iter("bloque"), None)
    if b is None or not list(b.iter("version")):
        sys.exit("el bloque %s no existe en %s. Resuélvelo contra el índice." % (bloque, norma))
    versiones = list(b.iter("version"))
    hoy = date.today().strftime("%Y%m%d")

    print("Norma    : %s" % norma)
    print("Bloque   : %s  (%s)" % (b.get("id"), b.get("titulo") or ""))
    print("Fuente   : %s%s" % (WEB, norma))
    print("Redacciones: %d" % len(versiones))
    print()

    print("Cadena de redacciones (vigencia / publicación / norma que la introduce):")
    for v in sorted(versiones, key=lambda v: fecha(v, "fecha_vigencia")):
        futura = " [AÚN NO VIGENTE]" if fecha(v, "fecha_vigencia") > hoy else ""
        print("  vig %s  pub %s  %s%s" % (
            fecha(v, "fecha_vigencia") or "????????",
            fecha(v, "fecha_publicacion") or "????????",
            v.get("id_norma") or "?", futura))
    print()

    aplicables = [v for v in versiones if fecha(v, "fecha_vigencia") <= hoy]
    if not aplicables:
        sys.exit("AVISO: ninguna redacción ha entrado en vigor todavía. No lo cites como vigente.")
    elegida = max(aplicables, key=lambda v: fecha(v, "fecha_vigencia"))

    pub_max = max(fecha(v, "fecha_publicacion") for v in aplicables)
    if fecha(elegida, "fecha_publicacion") < pub_max:
        print("*** POSIBLE REFORMA CRUZADA ***")
        print("La redacción con la vigencia más alta (vig %s, pub %s) no es la publicada"
              % (fecha(elegida, "fecha_vigencia"), fecha(elegida, "fecha_publicacion")))
        print("más tarde (pub %s). Ahí es donde una reforma se come a otra: contrasta esta"
              % pub_max)
        print("redacción con la página consolidada antes de darla por buena.")
        print("  %s%s" % (WEB, norma))
        print()

    if len(versiones) > 1:
        print("Este precepto tiene %d redacciones: léelas enteras antes de citar." % len(versiones))
        print()

    todas_notas = []
    for v in versiones:
        todas_notas.extend(texto_version(v)[1])
    alarmas = [n for n in dict.fromkeys(todas_notas)
               if any(a in n.lower() for a in ALARMAS)]
    if alarmas:
        print("Notas del BOE que hay que leer antes de citar esto:")
        for n in alarmas:
            print("  ! %s" % n)
        print()

    texto, _ = texto_version(elegida)
    print("REDACCIÓN VIGENTE (vigencia %s, publicada %s, por %s)" % (
        fecha(elegida, "fecha_vigencia"), fecha(elegida, "fecha_publicacion"),
        elegida.get("id_norma")))
    print("-" * 72)
    print(texto)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd, norma = sys.argv[1], sys.argv[2]
    resto = sys.argv[3:]
    if cmd == "indice":
        cmd_indice(norma)
    elif cmd == "buscar":
        if not resto:
            sys.exit("falta el texto a buscar")
        cmd_buscar(norma, " ".join(resto))
    elif cmd == "precepto":
        if resto and resto[0] == "--buscar":
            hits = cmd_buscar(norma, " ".join(resto[1:]))
            if len(hits) > 1:
                sys.exit("\nvarias coincidencias: elige un identificador y repite con él")
            print()
            cmd_precepto(norma, hits[0][0])
        elif resto:
            cmd_precepto(norma, resto[0])
        else:
            sys.exit("falta el identificador del bloque")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:  # al pasar la salida por head
        pass
