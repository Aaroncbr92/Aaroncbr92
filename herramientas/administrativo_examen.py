#!/usr/bin/env python3
"""Lee los cuadernillos y las plantillas del Cuerpo General Administrativo (C1).

Los PDF del INAP **llevan capa de texto propia**, así que aquí no hay
reconocimiento óptico ni, por tanto, el problema que arrastró el volumen de
Correos: lo que dice el PDF es lo que imprimió el tribunal. Lo que estorba es
sólo la maquetación, y son cuatro cosas, todas encontradas sobre los seis
cuadernillos reales y ninguna inventada:

  1. La cabecera («2025 - ADVO-L – MODELO A») y el pie («Página N de M») se
     cuelan **en mitad de un enunciado** que cruza el salto de página.
  2. Una opción queda pegada al final de la anterior («…Internacional. d)»),
     a veces con dos espacios y **a veces con uno**.
  3. Una opción que acaba en cifra («…son 30.000.000 KB.») **se traga el número
     de la pregunta siguiente**, que queda a media línea. Por eso el número se
     busca en toda la línea y se exige que detrás venga principio de enunciado.
  4. Hay preguntas cuyas **cuatro opciones son literalmente «1.», «2.», «3.» y
     «4.»**: un «4.» suelto es contenido de opción, no pregunta nueva.

El corte de pregunta nueva va por **número correlativo**, no por «ya tengo la
d)», porque un cuadernillo real se salta números: **el modelo B de 2025 no
imprime ninguna pregunta 65, imprime dos veces el 66**, y su propia plantilla
lo reconoce en una nota al margen.

La comprobación fuerte la da el propio examen. Los modelos A y B **barajan las
mismas preguntas y también las opciones dentro de cada una**, de modo que una
misma pregunta tiene dos plantillas independientes. Si las dos son buenas,
tienen que señalar **el mismo texto de opción**, aunque la letra sea distinta.
`cruzar()` lo comprueba. Y la pregunta se identifica por **enunciado más las
cuatro opciones**, nunca por el enunciado solo: hay dos preguntas distintas de
exámenes distintos que comparten el enunciado «¿Cuál de las siguientes
afirmaciones es verdadera?», y tomarlas por una sola daba una discrepancia
falsa.

Uso:
  administrativo_examen.py trocear  <cuadernillo.pdf>
  administrativo_examen.py claves   <plantilla.pdf>
  administrativo_examen.py casar    <cuadernillo.pdf> <plantilla.pdf>
  administrativo_examen.py cruzar   <dir de examenes>
"""
import re
import sys
import unicodedata

import pymupdf

CABECERA = re.compile(r"(?m)^\s*20\d\d\s*-\s*ADVO-[A-Z]+\b.*$")
PIE = re.compile(r"(?m)^\s*P[áa]gina \d+ de \d+\s*$")
SECCION = re.compile(r"^(PRIMERA PARTE|SEGUNDA PARTE|SUPUESTO\s+[IVX]+)\b.*$")
OPCION = re.compile(r"^([a-d])\)\s*(.*)$")
NUMERO = re.compile(r"(?:^|(?<=\s))(\d{1,3})\.\s+(?=[¿¡A-ZÁÉÍÓÚÜÑ«\"(])"
                    r"|^(\d{1,3})\.\s*$")

ROTULO = re.compile(r"^(Primera parte|Segunda parte|Supuesto\s+[IVX]+"
                    r"|Preguntas de reserva)\b", re.I)
# «23. Anulada», «10. c», «5.» con la letra en la línea siguiente, y
# «65. c (en el cuestionario aparece como pregunta 66)».
ENTRADA = re.compile(r"^(\d{1,3})\.\s*(Anulada|[a-d])?\s*(\(.*\))?\s*$", re.I)


# ------------------------------------------------------------------ cuadernillo

def texto(f):
    return "\n".join(pg.get_text() for pg in pymupdf.open(f))


def limpia(t):
    return PIE.sub("", CABECERA.sub("", t))


def arranque(linea, esperado):
    """(numero, cola_previa, resto) si la línea abre pregunta; si no, None."""
    cands = [(int(m.group(1) or m.group(2)), m.start(), m.end())
             for m in NUMERO.finditer(linea)]
    if not cands:
        return None
    for num, ini, fin in cands:
        if num == esperado:
            return num, linea[:ini].strip(), linea[fin:].strip()
    num, ini, fin = cands[0]
    return num, linea[:ini].strip(), linea[fin:].strip()


def trocea(t):
    """[(seccion, numero, enunciado, {a,b,c,d}, preambulo)] en orden de examen.

    El `preambulo` es el enunciado del supuesto práctico —de 225 a 532 palabras
    en los seis cuadernillos— y va repetido en las veinticinco preguntas de su
    supuesto, porque sin él ninguna de las veinticinco se entiende.
    """
    t = limpia(t)
    t = re.sub(r"(?<=[\.\:\?\)»])\s+([a-d]\)\s)", r"\n\1", t)
    out, sec, pre = [], "?", []
    n = esperado = None
    enun, opts, letra = [], {}, None

    def cierra():
        if n is not None:
            out.append((sec, n, " ".join(" ".join(enun).split()),
                        {k: " ".join(v.split()) for k, v in opts.items()},
                        " ".join(" ".join(pre).split())))

    for linea in t.split("\n"):
        s = linea.strip()
        if not s:
            continue
        m = SECCION.match(s)
        if m:
            cierra()
            sec, pre = m.group(1), []
            n, esperado, enun, opts, letra = None, 1, [], {}, None
            continue
        if letra is not None and not opts.get(letra, "").strip():
            opts[letra] = s
            continue
        a = arranque(s, esperado)
        if a and (a[0] == esperado or len(opts) == 4):
            num, cola, resto = a
            if cola and letra:
                opts[letra] += " " + cola
            elif cola and n is None:
                pre.append(cola)
            cierra()
            n, esperado = num, num + 1
            enun, opts, letra = ([resto] if resto else []), {}, None
            continue
        m = OPCION.match(s)
        if m and n is not None:
            letra = m.group(1)
            opts[letra] = m.group(2)
            continue
        if letra:
            opts[letra] += " " + s
        elif n is not None:
            enun.append(s)
        else:
            pre.append(s)
    cierra()
    return out


# -------------------------------------------------------------------- plantilla

def claves(f):
    """[(numero, letra_o_None, nota)] en el orden de la plantilla.

    `letra` viene a None cuando el tribunal **anuló** la pregunta. Las
    plantillas definitivas de 2024 anulan once preguntas del corpus, y eso no
    es un estorbo: es un registro de preguntas defectuosas firmado por quien
    puso el examen.
    """
    out = []
    for linea in "\n".join(p.get_text() for p in pymupdf.open(f)).split("\n"):
        s = linea.strip()
        if not s or ROTULO.match(s):
            continue
        m = ENTRADA.match(s)
        if m:
            v = (m.group(2) or "").lower()
            out.append([int(m.group(1)),
                        None if v in ("", "anulada") else v,
                        ("anulada" if v == "anulada" else "") + (m.group(3) or "")])
            continue
        if out and out[-1][1] is None and not out[-1][2] and re.fullmatch(r"[a-d]", s):
            out[-1][1] = s
    return [tuple(x) for x in out]


def casar(cuad, plant):
    """[(seccion, numero, enunciado, opciones, preambulo, letra, texto, nota)].

    La plantilla no repite el enunciado: es una lista de letras en el mismo
    orden que las preguntas del cuadernillo. Casarlas por posición es, por
    tanto, lo correcto, y el descuadre se canta en vez de pasarse por alto.
    """
    pr, cl = trocea(texto(cuad)), claves(plant)
    if len(pr) != len(cl):
        sys.exit("descuadre en %s: %d preguntas contra %d claves"
                 % (cuad, len(pr), len(cl)))
    return [(sec, n, e, o, pre, letra, (o[letra] if letra else None), nota)
            for (sec, n, e, o, pre), (_, letra, nota) in zip(pr, cl)]


def normalizar(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def identidad(enunciado, opciones):
    """Enunciado **más las cuatro opciones**: ver la cabecera del módulo."""
    return normalizar(enunciado) + "|" + "|".join(
        normalizar(opciones.get(k, "")) for k in "abcd")


# ------------------------------------------------------------------------ orden

def parejas(d):
    """[(cuadernillo, plantilla, etiqueta)] de un directorio de exámenes."""
    import glob
    import os
    out = []
    for c in sorted(glob.glob(os.path.join(d, "*-cuestionario-*.pdf"))):
        b = os.path.basename(c)[:-4]
        anno, _, cual = b.split("-", 2)
        for p in sorted(glob.glob(os.path.join(d, "%s-plantilla-*.pdf" % anno))):
            if os.path.basename(p)[:-4].split("-")[-1] == cual.split("-")[-1]:
                out.append((c, p, "%s-%s" % (anno, cual.split("-")[-1])))
                break
    return out


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    orden, arg = sys.argv[1], sys.argv[2]

    if orden == "trocear":
        pr = trocea(texto(arg))
        for sec, n, e, o, pre in pr:
            print("[%s %s] %s" % (sec, n, e[:100]))
            for k in "abcd":
                print("    %s) %s" % (k, o.get(k, "")[:92]))
        print("\npreguntas: %d   incompletas: %d"
              % (len(pr), sum(1 for _, _, e, o, _ in pr if len(o) != 4 or not e)))

    elif orden == "claves":
        cl = claves(arg)
        print(" ".join("%d:%s" % (n, l or "ANULADA") for n, l, _ in cl))
        print("\nclaves: %d   anuladas: %d"
              % (len(cl), sum(1 for _, l, _ in cl if l is None)))

    elif orden == "casar":
        for sec, n, e, o, pre, letra, txt, nota in casar(arg, sys.argv[3]):
            print("[%s %s] %s\n    -> %s %s" % (sec, n, e[:92], letra or "ANULADA",
                                                (txt or "")[:76]))

    elif orden == "cruzar":
        banco = {}
        anul = 0
        for cu, pl, tag in parejas(arg):
            fila = casar(cu, pl)
            anul += sum(1 for f in fila if f[5] is None)
            print("%-28s %3d preguntas  %d anuladas"
                  % (tag, len(fila), sum(1 for f in fila if f[5] is None)))
            for sec, n, e, o, pre, letra, txt, nota in fila:
                banco.setdefault(identidad(e, o), {})[tag] = txt
        dobles = {k: v for k, v in banco.items() if len(v) > 1}
        malas = [(k, v) for k, v in dobles.items()
                 if len({normalizar(x) for x in v.values() if x is not None}) > 1]
        print("\npreguntas distintas       : %d" % len(banco))
        print("con dos claves o más      : %d" % len(dobles))
        print("anuladas por el tribunal  : %d" % anul)
        print("DISCREPANCIAS entre claves: %d" % len(malas))
        for k, v in malas:
            print("\n  ? %s" % k[:110])
            for t, o in v.items():
                print("     %-10s %s" % (t, (o or "ANULADA")[:88]))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
