#!/usr/bin/env python3
"""Arma el banco de preguntas del bloque común a partir de los exámenes.

El temario general es el mismo para todas las ocupaciones tipo, y los exámenes
comparten preguntas entre ocupaciones. Así que las preguntas de Constitución,
Ley 17/2006, Convenio, Igualdad, Ley 13/2022, Ley 8/2009 y prevención de riesgos
de cualquiera de los 87 cuadernillos valen para los tres temarios.

Empareja cada cuadernillo con su plantilla, saca la letra correcta de cada
pregunta, clasifica por materia y escribe un fichero por materia.
"""
import glob
import os
import re
import sys
import unicodedata
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calibrar import preguntas, clasifica, MATERIAS

DIR = "convocatoria/examenes"
SALIDA = "banco"
RECLASIFICADAS = "banco/reclasificadas.tsv"

# El tema de prevención del específico no lo distingue ninguna palabra clave del
# tema 8 del general: hablan de la misma materia. Se separa a mano, en el
# fichero de reclasificadas, y tiene aquí su propio cajón.
PRL_ESPECIFICO = ("PRL específico · Prevención en el temario específico "
                  "(Producción (Asistencia) 18 · Producción 17 · "
                  "Realización (Asistencia) 21 · Gestión Administrativa 13 · "
                  "Gestión 31 · Documentación 7 · Información y Contenidos 11 · "
                  "Montaje de Equipos 7)")


def plantilla(ruta):
    """Devuelve {nº de pregunta: letra}.

    Si al lado hay un `.respuestas.tsv`, se usa ése: son las tres plantillas cuyo
    PDF no lleva tabla de caracteres, leídas celda a celda por
    `herramientas/plantilla_ocr.py`.

    La plantilla imprime, por bloques, una columna de números y debajo la
    columna de letras que les corresponde. Antes se troceaba por páginas, y
    bastaba con que el pie dijera «Fecha de publicación» en vez de «Fecha de la
    publicación» para que un bloque se pegara al siguiente y todas las
    respuestas de esa página salieran corridas un lugar. Ahora se recorre la
    secuencia y se empareja cada racha de números con la racha de letras que va
    detrás, que es como está impresa.
    """
    leidas = ruta[:-4] + ".respuestas.tsv"
    if os.path.exists(leidas):
        return {int(n): l for n, l in
                (x.split() for x in open(leidas, encoding="utf-8")
                 if not x.startswith("#") and x.strip())}

    t = open(ruta, encoding="utf-8").read().replace("\x0c", "\n")
    fichas = []
    for linea in t.splitlines():
        linea = linea.strip()
        if re.fullmatch(r"\d{1,3}", linea):
            fichas.append(("n", int(linea)))
        elif re.fullmatch(r"[a-dA-D]", linea):
            fichas.append(("l", linea.lower()))

    fuera = {}
    i = 0
    while i < len(fichas):
        nums = []
        while i < len(fichas) and fichas[i][0] == "n":
            nums.append(fichas[i][1])
            i += 1
        letras = []
        while i < len(fichas) and fichas[i][0] == "l":
            letras.append(fichas[i][1])
            i += 1
        for n, l in zip(nums, letras):
            fuera.setdefault(n, l)
        if not nums and not letras:
            i += 1
    return fuera


def parejas():
    """Empareja cuadernillo y plantilla por el nombre de la ocupación, no por
    el orden: en Producción (Asistencia) la plantilla no va detrás del
    cuadernillo, sino dos posiciones más allá."""
    def clave(base):
        b = re.sub(r"^\d+_", "", base[:-4])
        b = re.sub(r"^(preguntas|plantilla_de_respuestas|plantilla|respuestas)_", "", b)
        return re.sub(r"_(de_respuestas|respuestas)_", "_", b)

    cuadernillos, plantillas = {}, {}
    for f in sorted(glob.glob(os.path.join(DIR, "*.txt"))):
        base = os.path.basename(f)
        if base.endswith(".ocr.txt"):
            continue  # se elige más abajo, junto a su cuadernillo
        cuerpo = re.sub(r"^\d+_", "", base)
        if cuerpo.startswith("preguntas"):
            cuadernillos[clave(base)] = mejor_lectura(f)
        elif cuerpo.startswith(("plantilla", "respuestas")):
            plantillas[clave(base)] = f
    fuera = []
    for k, f in sorted(cuadernillos.items()):
        fuera.append((f, plantillas.get(k) or por_parecido(k, plantillas)))
    return fuera


def por_parecido(clave, plantillas):
    """Rescata la plantilla cuando el nombre del fichero trae una errata.

    La de Ingeniero Superior Industrial se llama `plantilla_de_respuestas_iing_
    sup_industrial`, con una i de más. Emparejar por nombre exacto la dejaba
    fuera y sus **diez preguntas** del bloque común entraban sin respuesta. Se
    acepta la más parecida cuando el parecido es alto y **no hay empate**: si dos
    plantillas se parecen lo mismo, no se elige ninguna.
    """
    import difflib
    puntos = sorted(((difflib.SequenceMatcher(None, clave, k).ratio(), k)
                     for k in plantillas), reverse=True)
    if not puntos or puntos[0][0] < 0.9:
        return None
    if len(puntos) > 1 and puntos[1][0] >= puntos[0][0]:
        return None
    return plantillas[puntos[0][1]]


def mejor_lectura(txt):
    """Prefiere la transcripción por OCR cuando la hay.

    Cinco cuadernillos llevan la fuente incrustada sin tabla de caracteres, así
    que extraer su texto devuelve «(cid:12)(cid:13)…» y no una sola letra. No
    daba error: simplemente no aportaban ninguna pregunta al banco, que es la
    manera silenciosa de perder cinco exámenes enteros. Se han vuelto a leer
    rasterizando la página y pasándole Tesseract en español, y la lectura buena
    se guarda al lado como `.ocr.txt`.
    """
    ocr = txt[:-4] + ".ocr.txt"
    return ocr if os.path.exists(ocr) else txt


def clave(materia):
    """`G2/G3 · Ley 17/2006 y Ley 5/2017` -> `g2-g3`, que es el nombre del fichero."""
    n = unicodedata.normalize("NFD", materia.split("·")[0].strip())
    n = "".join(c for c in n if unicodedata.category(c) != "Mn")
    return re.sub(r"[^A-Za-z0-9]+", "-", n).strip("-").lower()


DESTINOS = dict([(clave(n), n) for n, _ in MATERIAS]
                + [(clave(PRL_ESPECIFICO), PRL_ESPECIFICO), ("fuera", None)])


def reclasificadas():
    """{(cuadernillo, nº): (materia o None, motivo)} del fichero verificado."""
    fuera = {}
    for linea in open(RECLASIFICADAS, encoding="utf-8"):
        linea = linea.split("#")[0].strip() if linea.startswith("#") else linea.rstrip("\n")
        if not linea.strip():
            continue
        campos = linea.split("\t")
        if len(campos) < 3:
            continue
        origen, numero, destino = campos[0].strip(), campos[1].strip(), campos[2].strip()
        motivo = campos[3].strip() if len(campos) > 3 else ""
        if destino not in DESTINOS:
            sys.exit("%s: destino desconocido %r" % (RECLASIFICADAS, destino))
        fuera[(origen, int(numero))] = (DESTINOS[destino], motivo)
    return fuera


PIE = re.compile(r"""(?mx)
    ^ [\ \t]* (?:
        [A-Za-z0-9]?[\ \t]* P[áa]gina:? [\ \t]* \d+ [\ \t]* de [\ \t]* \d+   # pie de página
      | \d+ º [\ \t]+ Llamamiento                                          # cabecera
      | Fecha \ de \ (?:la\ )? publicaci[óo]n: .*
      | Ocupaci[óo]n \ tipo
    ) [\ \t]* $ \n?
""")


def sin_ecos(cuerpo):
    """Quita los renglones que el PDF imprime más de una vez.

    El cuadernillo de Realización (Asistencia), 2.º llamamiento dibuja **cada
    renglón tres veces**: el texto suelto, el mismo texto con su letra de opción
    delante, y el texto suelto otra vez. Son 193 renglones repetidos de 1.450.
    Al componer, eso hacía que **cada opción se llevara pegado el texto de la
    siguiente**, y el opositor leía opciones que no son las del examen.

    Se quita el renglón cuyo texto repite el de un vecino, mirando el contenido
    **sin la letra de opción**: así se conserva el que la lleva, que es el bueno,
    y caen los ecos.
    """
    lineas = cuerpo.split("\n")

    def nucleo(l):
        return re.sub(r"^\s*[a-d]\)\s*", "", l).strip()

    def suelta(l):
        return not re.match(r"^\s*[a-d]\)", l)

    fuera = []
    for i, l in enumerate(lineas):
        n = nucleo(l)
        if len(n) > 12:
            # el eco que va justo delante de la opción con su letra: gana la letra
            if suelta(l) and i + 1 < len(lineas) and not suelta(lineas[i + 1]) \
                    and nucleo(lineas[i + 1]) == n:
                continue
            # y el que va detrás de lo ya escrito. Solo se quitan renglones
            # **sueltos**: dos opciones con su letra y el mismo texto no son un
            # eco, son una errata del examen —el cuadernillo de Gestión repite
            # el texto en la b) y la c)— y borrar una cambia lo que se lee
            if suelta(l) and fuera and nucleo(fuera[-1]) == n:
                continue
        fuera.append(l)
    return "\n".join(fuera)


def sin_pie(cuerpo):
    """Quita del cuerpo de la pregunta los renglones de la propia página.

    Al deshacer el pegado por salto de página, el pie y la cabecera dejan de
    caer dentro de la pregunta siguiente y caen al final de la anterior. No
    estorban para responder, pero son ruido dentro de la cita, y el volumen
    imprimible tenía que limpiarlos otra vez al maquetar.
    """
    return PIE.sub("", cuerpo)


def main():
    os.makedirs(SALIDA, exist_ok=True)
    pormateria = defaultdict(list)
    con, sin = 0, 0
    sospechosas = []
    manual = reclasificadas()
    usadas = set()
    for cuad, plant in parejas():
        respuestas = plantilla(plant) if plant else {}
        # una plantilla bien leída numera de 1 a N sin huecos; si no, se avisa
        if respuestas:
            alto = max(respuestas)
            faltan = [n for n in range(1, alto + 1) if n not in respuestas]
            if faltan:
                sospechosas.append("%s: faltan %d de %d (%s...)"
                                   % (os.path.basename(plant), len(faltan), alto,
                                      ", ".join(str(n) for n in faltan[:6])))
        texto = open(cuad, encoding="utf-8").read()
        # el identificador nombra el cuadernillo, no la transcripción: si
        # mañana se relee mejor, las referencias de `reclasificadas.tsv` y las
        # erratas anotadas siguen apuntando a la misma pregunta
        origen = re.sub(r"\.ocr$", "", os.path.basename(cuad)[:-4])
        sacadas = preguntas(texto)
        # un cuadernillo del que no sale ninguna pregunta no da ningún error:
        # simplemente no aporta nada al banco y nadie lo echa de menos. Por eso
        # se avisa, y se avisa también si salen menos de las que numera la
        # plantilla, que es la única cuenta independiente que tenemos
        if not sacadas:
            sospechosas.append("%s: no se saca ninguna pregunta%s"
                               % (origen, " ((cid:n): el PDF no lleva tabla de "
                                  "caracteres)" if "(cid:" in texto[:2000] else ""))
        elif respuestas and max(sacadas)[0] < max(respuestas):
            sospechosas.append("%s: %d preguntas para una plantilla de %d"
                               % (origen, len(sacadas), max(respuestas)))
        for n, cuerpo in sacadas:
            materia = clasifica(cuerpo, MATERIAS)
            if (origen, n) in manual:
                materia = manual[(origen, n)][0]
                usadas.add((origen, n))
            if not materia:
                continue
            letra = respuestas.get(n)
            if letra:
                con += 1
            else:
                sin += 1
            # el OCR deja caracteres de control que hacen ilegible el fichero
            cuerpo = "".join(c for c in cuerpo if c == "\n" or c >= " ")
            cuerpo = sin_ecos(sin_pie(cuerpo))
            cuerpo = re.sub(r"\n{2,}", "\n", cuerpo).strip()
            pormateria[materia].append((origen, n, letra, cuerpo))

    # una fila que ya no casa con ninguna entrada es una corrección que dejó de
    # aplicarse sin que nadie se entere, que es como se pierden las revisiones
    huerfanas = sorted(set(manual) - usadas)
    if huerfanas:
        sospechosas.append("%s: %d filas no casan con ninguna pregunta (%s)"
                           % (RECLASIFICADAS, len(huerfanas),
                              "; ".join("%s nº %d" % h for h in huerfanas[:4])))

    total = 0
    for materia, items in sorted(pormateria.items()):
        ruta = os.path.join(SALIDA, "%s.md" % clave(materia))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("# %s\n\n" % materia)
            fh.write("%d preguntas reales sacadas de los cuadernillos de octubre y "
                     "noviembre de 2024.\nLa respuesta es la de la plantilla oficial; "
                     "donde pone «sin plantilla» es que\nno se pudo emparejar.\n\n"
                     % len(items))
            for origen, n, letra, cuerpo in items:
                fh.write("---\n\n**%s · nº %d · respuesta: %s**\n\n```\n%s\n```\n\n"
                         % (origen, n, letra or "sin plantilla", cuerpo))
        total += len(items)
        print("%-50s %4d preguntas -> %s" % (materia, len(items), ruta))
    print()
    print("total %d preguntas del bloque común; con respuesta oficial %d, sin ella %d"
          % (total, con, sin))
    if sospechosas:
        print()
        print("Avisos, revisar a mano antes de fiarse de la cuenta:")
        for x in sospechosas:
            print("  ! %s" % x)


if __name__ == "__main__":
    main()
