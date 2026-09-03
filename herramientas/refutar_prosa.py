#!/usr/bin/env python3
"""Refutación por prosa y forma: relleno, repeticiones y siglas sin presentar."""
import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tema import cuerpo as sin_envoltorio
import unicodedata
from collections import Counter

RELLENO = [r"como hemos visto", r"como ya se ha dicho", r"en s[íi]ntesis",
           r"cabe destacar", r"es importante se[ñn]alar", r"conviene recordar",
           r"en definitiva", r"por [úu]ltimo,? cabe", r"no hay que olvidar",
           r"resulta evidente", r"a modo de resumen", r"dicho esto"]


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9ñ ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def main():
    # fuera la portada y el índice: son envoltorio, no afirmaciones del tema
    tema = sin_envoltorio(open(sys.argv[1], encoding="utf-8").read())
    hallazgos = 0

    print("## Tejido conectivo y relleno")
    for pat in RELLENO:
        for m in re.finditer(pat, tema, re.I):
            print("  · %s" % re.sub(r"\s+", " ", tema[max(0, m.start()-60):m.end()+60]))
            hallazgos += 1
    print("  (ninguno)" if not hallazgos else "")

    print()
    print("## Frases repetidas entre epígrafes")
    # una frase que se repite **dentro de comillas latinas las dos veces** no
    # es relleno del tema: es la fuente que se repite a sí misma. La
    # Constitución dice de los partidos y de los sindicatos, con las mismas
    # palabras, que «su estructura interna y funcionamiento deberán ser
    # democráticos», y recortar una de las dos citas para callar el aviso
    # sería recortar la norma. Se miran sólo los trozos que quedan fuera de
    # las comillas.
    def fuera_de_comillas(texto):
        # ni los renglones citados con «>» ni los rótulos de epígrafe son prosa
        # del tema: el enunciado de la convocatoria se transcribe una vez por
        # ocupación cuando el tema sirve a varias, y el título de un epígrafe
        # vuelve a salir en su encabezado. Contarlos como repetición es contar
        # dos veces lo mismo.
        texto = "\n".join(l for l in texto.splitlines()
                          if not l.lstrip().startswith((">", "#")))
        return re.sub(r"«[^»]*»", " ", texto)
    frases = [limpia(f) for f in re.split(r"(?<=[.;:])\s", fuera_de_comillas(tema))]
    frases = [f for f in frases if len(f.split()) >= 8]
    repes = [(f, c) for f, c in Counter(frases).items() if c > 1]
    for f, c in sorted(repes, key=lambda x: -x[1]):
        print("  · x%d  %s" % (c, f[:120]))
        hallazgos += 1
    if not repes:
        print("  (ninguna)")

    print()
    print("## Siglas sin presentar la primera vez")
    # Lo que va entre acentos graves no es prosa: es código, un nombre de
    # función, un identificador. Un tema de hoja de cálculo lo tiene a
    # docenas —`BUSCARV`, `SUMAR.SI`, `#¡DIV/0!`— y todos ellos van en
    # mayúsculas, así que sin excluirlos la lista de siglas sale llena de
    # avisos que no son siglas y **entierra los que sí lo son**, que es el
    # único motivo por el que se mira esta lista. Se sustituye por espacios
    # en lugar de borrarse para no juntar palabras vecinas.
    tema = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), tema)
    # los números romanos de los títulos no son siglas
    ROMANOS = re.compile(r"^[IVXLC]+$")
    CONOCIDAS = ("BOE", "RTVE", "TVE", "RNE", "PDF", "HTML", "URL", "TV")
    # palabras escritas en mayúsculas que no son siglas. Unas son castellanas
    # y van en mayúsculas por énfasis —el examen las usa a docenas: «¿Cuál NO
    # es válido?»—; otras son palabras inglesas que el oficio escribe así
    # aunque no abrevien nada: RAW es «crudo», LOG es «logarítmico».
    PALABRAS = ("NO", "SI", "UNA", "UNO", "TODO", "TODAS", "SOLO", "NUNCA",
                "SIEMPRE", "MENOS", "MAS", "CIERTA", "FALSA",
                "ANUAL", "SALVO", "ANTES", "DESPUES", "MENOR", "MAYOR",
                "TRES", "DOS", "ES", "PUEDE", "SOLAMENTE",
                "RAW", "LOG", "LUT", "MIX")
    # rótulos de botones y de menús, tal como están serigrafiados en el
    # aparato. No abrevian nada: son el nombre que el operador lee y pulsa, y
    # el tema los escribe en mayúsculas justamente para que se reconozcan en
    # el panel. Y nombres de marca y de modelo, que tampoco son siglas.
    ROTULOS = ("CUT", "AUTO", "WIPE", "NAM", "FAM", "CLEAN", "EDIT", "PREVIO",
               "SHOW", "KEY", "FILL", "SIZE", "CROP", "MENU", "PGM", "PVW",
               "ATEM", "MOTU", "XVS", "AV", "HS",
               # órdenes y rótulos de los programas de edición y de los
               # mandos de repetición, que el examen escribe en mayúsculas
               # porque así están rotulados. Tampoco abrevian nada
               "MATCH", "FRAME", "AUDIO", "MIXER", "SET", "PAN", "LEVEL",
               "GLOBAL", "IN", "OUT", "EQ", "TAKE", "PRV", "CAM", "AUX",
               "LINK", "GANG", "TWICE", "DUAL", "PLAYLIST", "TIMELINE",
               "TBAR", "VGA", "VDR", "REC", "MODE")
    # «SI(C2 = 1» no es una sigla: es una llamada a función. Un paréntesis
    # pegado al nombre lo delata, y sin esta salvedad un tema de hoja de
    # cálculo llena la lista de falsos avisos aunque el nombre vaya dentro de
    # una cita literal, donde no se le pueden poner acentos graves sin tocar
    # la cita.
    llamadas = set(re.findall(r"\b([A-Z]{2,6})\(", tema))
    # «CC.AA.» y «NO-DO» son una sola abreviatura, no dos. Con `\b` a secas la
    # lente las parte y avisa de «AA» y de «DO», que no son siglas de nada y
    # **entierran los avisos que sí lo son**. Se descartan los trozos que sólo
    # aparecen pegados a otro grupo de mayúsculas por un punto o un guion.
    trozos = set()
    for m in re.finditer(r"\b[A-Z]{2,6}(?:[.-][A-Z]{2,6})+\.?", tema):
        partes = re.findall(r"[A-Z]{2,6}", m.group(0))
        trozos.update(partes)
    enteras = set(re.findall(r"(?<![A-Z.-])\b([A-Z]{2,6})\b(?![.-][A-Z])", tema))
    for sigla in sorted(set(re.findall(r"\b([A-Z]{2,6})\b", tema))):
        if sigla in trozos and sigla not in enteras:
            continue
        if ROMANOS.match(sigla) or sigla in CONOCIDAS or sigla in llamadas:
            continue
        if sigla in PALABRAS or sigla in ROTULOS:
            continue
        # «BT.601-7», «EN 300 744», «ST 2110»: la serie de una norma no es una
        # sigla que el tema tenga que presentar, es la mitad de su nombre. Se
        # reconoce porque **todas** sus apariciones llevan pegado un número.
        apariciones = list(re.finditer(r"\b%s\b" % re.escape(sigla), tema))
        if apariciones and all(
                re.match(r"[.\s-]\s?\d", tema[m.end():m.end() + 3] or " ")
                for m in apariciones):
            continue
        # una sigla que sólo sale dentro de una cita literal no es del tema:
        # es de la fuente citada, y no se le puede meter la presentación
        # dentro de las comillas sin dejar de ser literal.
        lineas = tema.splitlines()
        fuera_de_cita = [l for l in lineas
                         if re.search(r"\b%s\b" % re.escape(sigla), l)
                         and not l.lstrip().startswith(">")]
        if apariciones and not fuera_de_cita:
            continue
        # buscar la sigla como palabra, no como trozo: `find` la encuentra dentro
        # de otra palabra —«RD» dentro de «BORDER», «SI» dentro de «MÚSICA»— y
        # entonces se comprueba la presentación en un sitio del tema donde la
        # sigla no está, de modo que un aviso correcto se vuelve incorregible
        m = re.search(r"\b%s\b" % re.escape(sigla), tema)
        i = m.start() if m else -1
        # «Directiva 2007/65/CE» no es una sigla del tema: es el nombre de la norma
        while i > 0 and tema[i - 1] == "/":
            m = re.search(r"\b%s\b" % re.escape(sigla), tema[i + 1:])
            i = i + 1 + m.start() if m else -1
        if i < 0:
            continue
        antes = tema[max(0, i - 130):i]
        # se presenta de las dos maneras y las dos valen: «Unión General de
        # Trabajadores (UGT)» y «UGT (Unión General de Trabajadores)». Mirando
        # sólo hacia atrás, la segunda salía como sigla sin presentar aunque
        # llevara la explicación pegada detrás.
        despues = tema[i + len(sigla):i + len(sigla) + 3]
        if "(" not in antes and not re.match(r"\s?\(", despues):
            print("  · %-6s primera aparición: ...%s%s..."
                  % (sigla, re.sub(r"\s+", " ", antes[-70:]), sigla))
            hallazgos += 1

    print()
    print("hallazgos de prosa: %d" % hallazgos)


if __name__ == "__main__":
    main()
