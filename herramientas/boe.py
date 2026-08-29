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
  boe.py norma    BOE-A-2006-9958 fuentes/
  boe.py --fecha 20221221 precepto BOE-A-2006-9958 a11   # como estaba ese día
"""

import re
import subprocess
import sys
import unicodedata
import xml.etree.ElementTree as ET
from datetime import date

API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id"
WEB = "https://www.boe.es/buscar/act.php?id="

# Fecha a la que se lee la ley. Por defecto hoy; con --fecha AAAAMMDD se lee la
# redacción que estaba en vigor ese día, que es lo que pide una convocatoria
# cuando congela el temario a la fecha de sus bases.
CORTE = [None]


def corte():
    return CORTE[0] or date.today().strftime("%Y%m%d")


def etiqueta_corte():
    return "vigente hoy" if not CORTE[0] else "vigente a %s" % CORTE[0]


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
    hoy = corte()

    print("Norma    : %s" % norma)
    print("Bloque   : %s  (%s)" % (b.get("id"), b.get("titulo") or ""))
    print("Fuente   : %s%s" % (WEB, norma))
    print("Leído    : %s" % etiqueta_corte())
    print("Redacciones: %d" % len(versiones))
    print()

    print("Cadena de redacciones (vigencia / publicación / norma que la introduce):")
    for v in sorted(versiones, key=lambda v: fecha(v, "fecha_vigencia")):
        futura = " [POSTERIOR AL CORTE]" if fecha(v, "fecha_vigencia") > hoy else ""
        print("  vig %s  pub %s  %s%s" % (
            fecha(v, "fecha_vigencia") or "????????",
            fecha(v, "fecha_publicacion") or "????????",
            v.get("id_norma") or "?", futura))
    print()

    aplicables = [v for v in versiones if fecha(v, "fecha_vigencia") <= hoy]
    if not aplicables:
        sys.exit("AVISO: ninguna redacción estaba en vigor a esa fecha. No lo cites.")
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
    print("REDACCIÓN APLICABLE, %s (vigencia %s, publicada %s, por %s)" % (
        etiqueta_corte(),
        fecha(elegida, "fecha_vigencia"), fecha(elegida, "fecha_publicacion"),
        elegida.get("id_norma")))
    print("-" * 72)
    print(texto)


def cmd_norma(norma, destino):
    """Vuelca la norma entera en su redacción vigente, más el parte de redacciones."""
    import os
    os.makedirs(destino, exist_ok=True)
    hoy = corte()
    bloques = indice(norma)
    cuerpo = ["# %s — texto consolidado, redacción %s" % (norma, etiqueta_corte()),
              "",
              "Volcado con `herramientas/boe.py norma` el %s desde la API de"
              % date.today().isoformat(),
              "legislación consolidada del BOE. Fuente: %s%s" % (WEB, norma),
              "",
              "No se edita a mano. Si hace falta refrescarlo, se vuelve a volcar.",
              ""]
    parte = ["bloque\ttitulo\tredacciones\tvigencia\tpublicacion\tnorma\taviso"]
    avisos, multiples, alarmas, vacatio = [], [], [], []

    for bid, titulo in bloques:
        if not bid:
            continue
        raiz = traer("%s/%s/texto/bloque/%s" % (API, norma, bid))
        b = next(raiz.iter("bloque"), None)
        versiones = list(b.iter("version")) if b is not None else []
        if not versiones:
            parte.append("%s\t%s\t0\t\t\t\tSIN TEXTO" % (bid, titulo))
            continue
        aplicables = [v for v in versiones if fecha(v, "fecha_vigencia") <= hoy]
        if not aplicables:
            parte.append("%s\t%s\t%d\t\t\t\tNINGUNA EN VIGOR AL CORTE"
                         % (bid, titulo, len(versiones)))
            # el bloque existe en el texto publicado pero su vacatio no ha
            # vencido al corte. Si solo se anota en el parte, el volcado que se
            # lee queda con un hueco invisible justo donde puede haber pregunta:
            # se deja el rótulo con el aviso y la fecha en que entra en vigor
            entra = min(fecha(v, "fecha_vigencia") for v in versiones)
            cuerpo.append("## [%s] %s" % (bid, titulo))
            cuerpo.append("")
            cuerpo.append("_**No estaba en vigor a la fecha leída (%s).** El texto "
                          "existe en la norma publicada, pero su entrada en vigor es "
                          "el %s. Léelo en el volcado de la redacción vigente._"
                          % (corte(), entra))
            cuerpo.append("")
            vacatio.append("%s (%s): entra en vigor el %s" % (bid, titulo, entra))
            continue
        elegida = max(aplicables, key=lambda v: fecha(v, "fecha_vigencia"))
        pub_max = max(fecha(v, "fecha_publicacion") for v in aplicables)
        aviso = ""
        if fecha(elegida, "fecha_publicacion") < pub_max:
            aviso = "POSIBLE REFORMA CRUZADA"
            avisos.append("%s (%s)" % (bid, titulo))
        if len(versiones) > 1:
            multiples.append("%s (%s): %d" % (bid, titulo, len(versiones)))

        texto, notas = texto_version(elegida)
        for n in dict.fromkeys(notas):
            if any(a in n.lower() for a in ALARMAS):
                alarmas.append("%s (%s): %s" % (bid, titulo, n))

        parte.append("%s\t%s\t%d\t%s\t%s\t%s\t%s" % (
            bid, titulo, len(versiones), fecha(elegida, "fecha_vigencia"),
            fecha(elegida, "fecha_publicacion"), elegida.get("id_norma") or "", aviso))

        cuerpo.append("## [%s] %s" % (bid, titulo or "(sin título)"))
        cuerpo.append("")
        cuerpo.append("_Redacción aplicable desde %s, publicada %s, por %s. %d redacción(es) en total._"
                      % (fecha(elegida, "fecha_vigencia"),
                         fecha(elegida, "fecha_publicacion"),
                         elegida.get("id_norma") or "?", len(versiones)))
        cuerpo.append("")
        cuerpo.append(texto)
        cuerpo.append("")

    f_texto = os.path.join(destino, "%s.md" % norma)
    f_parte = os.path.join(destino, "%s.redacciones.tsv" % norma)
    open(f_texto, "w", encoding="utf-8").write("\n".join(cuerpo))
    open(f_parte, "w", encoding="utf-8").write("\n".join(parte) + "\n")

    print("bloques volcados : %d" % (len(parte) - 1))
    print("texto            : %s" % f_texto)
    print("parte             : %s" % f_parte)
    print()
    if vacatio:
        print()
        print("*** %d bloques NO estaban en vigor a la fecha leída ***" % len(vacatio))
        print("    Están en el texto publicado, pero su vacatio no había vencido.")
        print("    En el volcado va el rótulo con el aviso, no el texto.")
        for x in vacatio:
            print("  ! %s" % x)
        print()
    print("Preceptos con más de una redacción (%d): léelos enteros." % len(multiples))
    for m in multiples:
        print("  - %s" % m)
    print()
    if avisos:
        print("*** POSIBLE REFORMA CRUZADA en %d preceptos: contrástalos a mano ***" % len(avisos))
        for a in avisos:
            print("  ! %s" % a)
    else:
        print("Ninguna reforma cruzada detectada.")
    if alarmas:
        print()
        print("Notas del BOE sobre nulidad, derogación o convalidación (%d):" % len(alarmas))
        for a in dict.fromkeys(alarmas):
            print("  ! %s" % a)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    argv = list(sys.argv[1:])
    if "--fecha" in argv:
        i = argv.index("--fecha")
        try:
            CORTE[0] = argv[i + 1]
        except IndexError:
            sys.exit("--fecha necesita una fecha AAAAMMDD")
        if not re.fullmatch(r"\d{8}", CORTE[0]):
            sys.exit("--fecha se escribe AAAAMMDD, por ejemplo 20221221")
        del argv[i:i + 2]
    if len(argv) < 2:
        sys.exit(__doc__)
    cmd, norma = argv[0], argv[1]
    resto = argv[2:]
    if cmd == "indice":
        cmd_indice(norma)
    elif cmd == "buscar":
        if not resto:
            sys.exit("falta el texto a buscar")
        cmd_buscar(norma, " ".join(resto))
    elif cmd == "norma":
        destino = resto[0] if resto else "fuentes"
        cmd_norma(norma, destino)
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
