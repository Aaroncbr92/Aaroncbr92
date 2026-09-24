#!/usr/bin/env python3
"""Construye el banco del Administrativo C1 desde el acta y los cuadernillos.

El acta —`banco/especifico-administrativo.tsv`— es un reparto **hecho a mano**:
dice a qué tema del programa va cada pregunta, y no se deduce de nada. Este
guion la lee, va a buscar cada pregunta a su cuadernillo, le pone al lado la
respuesta de la plantilla y escribe un fichero por tema en `banco/`.

Dos cosas que este guion canta en vez de callar, porque son las dos formas de
que el banco mienta sin que se note:

  * **filas del acta que no casan con ninguna pregunta** —un número mal
    apuntado deja la fila colgando y la pregunta fuera del volumen—, y
  * **preguntas del cuadernillo que ninguna fila reparte**, que es lo mismo al
    revés.

Las **once preguntas anuladas** por el tribunal se escriben con su enunciado y
con la palabra «anulada» donde va la letra. El enunciado sigue sirviendo para
estudiar; la respuesta, no, y quien lo lea tiene que saberlo.

Uso:  banco_administrativo.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from administrativo_examen import parejas, casar, identidad   # noqa: E402

EXAMENES = "convocatoria/administrativo/examenes"
ACTA = "banco/especifico-administrativo.tsv"
PROGRAMA = "convocatoria/administrativo/PROGRAMA-ADMINISTRATIVO.md"
SALIDA = "banco"

ROMANO = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6}


def programa():
    """{'IV.5': 'Provisión de puestos de trabajo…'} con el título entero."""
    out, bloque = {}, None
    for l in open(PROGRAMA, encoding="utf-8"):
        m = re.match(r"^## ([IVX]+)\. ", l.strip())
        if m:
            bloque = m.group(1)
            continue
        m = re.match(r"^(\d{1,2})\. (.*)$", l.strip())
        if m and bloque:
            out["%s.%s" % (bloque, m.group(1))] = m.group(2)
    return out


def acta():
    """{(origen, seccion, numero): (tema, epigrafe)}."""
    out = {}
    for l in open(ACTA, encoding="utf-8"):
        if l.startswith("#") or l.startswith("origen") or not l.strip():
            continue
        org, sec, num, tema, _motivo, epi = l.rstrip("\n").split("\t")
        out[(org, sec, int(num))] = (tema, epi.strip())
    return out


def remite(epigrafe):
    epigrafe = (epigrafe or "").strip()
    if not epigrafe or epigrafe == "--":
        return ""
    if epigrafe.startswith("!"):
        return "El tema no la contesta: %s" % epigrafe[1:].strip()
    return "La contesta el epígrafe %s." % epigrafe


def orden(tema):
    b, n = tema.split(".")
    return (ROMANO[b], int(n))


def main():
    titulos, rep = programa(), acta()
    portema, usadas, sinfila = {}, set(), []
    vistas = set()

    for cu, pl, tag in sorted(parejas(EXAMENES), key=lambda x: x[2]):
        org = os.path.basename(cu)[:-4]
        for sec, n, enun, opts, pre, letra, txt, nota in casar(cu, pl):
            k = identidad(enun, opts)
            if k in vistas:                 # el modelo B repite el examen del A
                continue
            vistas.add(k)
            clave = (org, sec, n)
            if clave not in rep:
                sinfila.append(clave)
                continue
            usadas.add(clave)
            tema, epi = rep[clave]
            cuerpo = "%s\n\n%s" % (enun, "\n".join(
                "%s) %s" % (x, opts[x]) for x in "abcd"))
            portema.setdefault(tema, []).append(
                (org, sec, n, letra, nota, cuerpo, pre, remite(epi)))

    total = 0
    for tema in sorted(portema, key=orden):
        items = portema[tema]
        anul = sum(1 for x in items if x[3] is None)
        ruta = os.path.join(SALIDA, "administrativo-%s.md" % tema.replace(".", "-"))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("# %s\n\n" % titulos[tema])
            fh.write("%d preguntas reales de los ejercicios del Cuerpo General "
                     "Administrativo\ndel Estado, ingreso libre: la convocatoria de 2025 "
                     "y la OEP 2023-2024. La\nrespuesta es la de la plantilla oficial.\n\n"
                     % len(items))
            if anul:
                fh.write("**%d de estas preguntas están anuladas por el tribunal.** Su "
                         "enunciado salió\ndel temario y sigue sirviendo para estudiar; "
                         "su respuesta, no.\n\n" % anul)
            for org, sec, n, letra, nota, cuerpo, pre, rem in items:
                resp = "anulada" if letra is None else letra.lower()
                fh.write("---\n\n**%s · %s · nº %d · respuesta: %s**\n\n"
                         % (org, sec.lower(), n, resp))
                if pre:
                    fh.write("> %s\n\n" % pre)
                fh.write("```\n%s\n```\n\n" % cuerpo)
                if rem:
                    fh.write("*%s*\n\n" % rem)
        print("%-6s %-58s %3d preguntas%s"
              % (tema, titulos[tema][:58], len(items),
                 "  (%d anuladas)" % anul if anul else ""))
        total += len(items)

    print()
    print("repartidas: %d de %d preguntas distintas" % (total, len(vistas)))
    if sinfila:
        print("\n! %d preguntas que el acta no reparte:" % len(sinfila))
        for c in sinfila[:20]:
            print("  ! %s · %s · nº %d" % c)
    sueltas = sorted(set(rep) - usadas)
    if sueltas:
        print("\n! %d filas del acta que no casan con ninguna pregunta:" % len(sueltas))
        for h in sueltas[:20]:
            print("  ! %s · %s · nº %d" % h)
    return 1 if (sinfila or sueltas) else 0


if __name__ == "__main__":
    sys.exit(main())
