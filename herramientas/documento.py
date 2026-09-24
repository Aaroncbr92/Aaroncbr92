#!/usr/bin/env python3
"""Documentos que no son volcados del BOE (PDF del BOJA, convenios, cartas…):
pasarlos a texto limpio una vez, y sacar sólo el trozo que se necesita.

Leer un documento entero para comprobar un artículo gasta diez o cien veces más
que leer ese artículo. Esto hace con cualquier PDF lo que `boe.py precepto` hace
con el BOE.

  documento.py texto <fichero.pdf>          # escribe <fichero>.txt limpio (sin cabecera
                                            # ni pie del BOJA, sin guiones de fin de línea)
  documento.py indice <fichero.pdf|.txt>    # lista artículos, capítulos y anexos con su línea
  documento.py seccion <fichero> <rótulo>   # imprime sólo esa sección: «33», «Artículo 33»,
                                            # «Disposición transitoria tercera», «Anexo II»
"""
import os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from negritas import prepara  # noqa: E402  (limpieza de cabecera y pie del BOJA)

ROTULO = re.compile(r"(?im)^\s*((?:art[íi]culo|art\.)\s+\d+[\w.º]*(?:\s+(?:bis|ter))?|"
                    r"(?:t[íi]tulo|cap[íi]tulo|secci[óo]n)\s+[\wÍÁÉÓÚ.]+|"
                    r"disposici[óo]n\s+(?:adicional|transitoria|derogatoria|final)\s*\w*|"
                    r"anexo\s*[\wIVXL]*)\b")


def llano(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"\s+", " ", "".join(c for c in s if unicodedata.category(c) != "Mn")).strip()


def texto(ruta):
    if ruta.endswith(".pdf"):
        txt = ruta[:-4] + ".txt"
        if not os.path.exists(txt) or os.path.getmtime(txt) < os.path.getmtime(ruta):
            import fitz
            crudo = "\n".join(p.get_text() for p in fitz.open(ruta))
            open(txt, "w", encoding="utf-8").write(prepara(crudo))
        ruta = txt
    return open(ruta, encoding="utf-8").read()


def rotulos(t):
    lineas = t.split("\n")
    return [(i, m.group(1).strip()) for i, l in enumerate(lineas) for m in [ROTULO.match(l)] if m], lineas


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    orden, ruta = sys.argv[1], sys.argv[2]
    t = texto(ruta)
    if orden == "texto":
        print("%s: %d palabras" % (ruta[:-4] + ".txt" if ruta.endswith(".pdf") else ruta, len(t.split())))
    elif orden == "indice":
        for i, r in rotulos(t)[0]:
            print("%6d  %s" % (i + 1, r))
    elif orden == "seccion":
        buscado = llano(" ".join(sys.argv[3:]))
        if re.fullmatch(r"\d+\w*", buscado):
            buscado = "articulo " + buscado
        rs, lineas = rotulos(t)
        trozos = []  # el sumario repite los rótulos: se queda el trozo más largo
        for k, (i, r) in enumerate(rs):
            r2 = llano(r).replace("art.", "articulo").rstrip(".º")
            if r2 == buscado or r2.startswith(buscado + " ") or r2 == buscado.rstrip(".º"):
                fin = rs[k + 1][0] if k + 1 < len(rs) else len(lineas)
                trozos.append("\n".join(lineas[i:fin]).strip())
        if trozos:
            print(max(trozos, key=len))
            return
        sys.exit("No encuentro «%s». Mira `documento.py indice %s`." % (" ".join(sys.argv[3:]), ruta))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
