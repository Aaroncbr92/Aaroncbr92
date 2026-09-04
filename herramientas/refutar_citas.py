#!/usr/bin/env python3
"""Quinta lente: las citas EN BLOQUE, contra el volcado, como subcadena literal.

Nace de la ocupación de Técnica de Equipos, Instalaciones y Sistemas Eléctricos,
cuyo Anexo 2 nombra el reglamento electrotécnico para baja tensión **y sus
cincuenta y dos instrucciones técnicas complementarias**. Y ahí la lente de
exactitud se queda corta por una razón de formato, no de fondo:
`refutar_exactitud.py` ancla cada comprobación en un marcador del tipo
«**Artículo N**», y **una instrucción técnica no numera por artículos**: numera
por apartados —1.1, 3.5, 4.2.1—. La lente no encuentra marcador, no abre bloque
y devuelve cero. **Y ese cero no dice que las citas estén bien: dice que no ha
mirado ninguna**, que es exactamente el aviso del apartado 10 del manual.

Esta lente no ancla en nada. Toma **cada bloque de cita del tema** —lo que va en
`> ` seguido, sin la línea de atribución que empieza por `> —`— y comprueba
**cada tramo en negrita, uno a uno**, contra el volcado entero. Uno a uno y no
todo junto, porque el temario tiene dos formas de citar: **la cita entera en
negrita** y **la cita en redonda con las frases que deciden en negrita**, y
concatenar los tramos de la segunda daría un texto que no existe en ninguna
norma. Normaliza sólo lo que el propio volcado cambia al extraerse: los espacios
en blanco, las comillas angulares del temario y los guiones que un PDF reparte
como quiere.

**No comprueba el bloque del enunciado de la convocatoria**, que también va en
`> ` y **no es una cita de la norma**: es el programa, y su fuente es el Anexo 2.
**Ni los tramos muy cortos**, que casan por casualidad.

**Lo que sí marca y no debería, y hay que saberlo antes de correrla**: el
temario usa el bloque `> ` para dos cosas, para citar y para **encuadrar una
fórmula o un enunciado propios** —«Caudal de un canal = frecuencia de muestreo ×
profundidad de bits»—. Eso no es una cita y no está en ninguna norma, así que la
lente lo marca. **No es un hallazgo: es el precio de no anclar en nada.** Al
leer su salida, un tramo que el temario declara como suyo se descarta a mano; lo
que hay que mirar son **los tramos que el tema presenta como palabras de una
fuente**.

No sustituye a `refutar_exactitud`: aquélla comprueba **negrita a negrita dentro
del artículo que la cita dice**, que es más fino. Ésta comprueba **el bloque
entero contra la norma entera**, que es más grueso y **funciona donde la otra no
llega**. Donde las dos aplican, se pasan las dos.

Uso:  refutar_citas.py <tema.md> <fuente.md> [<fuente.md> ...]
"""
import re
import sys


MINIMO = 25   # caracteres: por debajo, un tramo casa por casualidad


def limpia(s):
    """Normaliza lo que la extracción del volcado cambia, y nada más.

    Las COMILLAS se quitan todas —angulares, inglesas rectas y tipográficas—
    porque una misma norma sale del boletín con unas y del temario con otras, y
    esa diferencia no es una falta de literalidad: es tipografía. Los guiones
    largos y medios se igualan por la misma razón.
    """
    for c in "«»\u201c\u201d\u2018\u2019\"":
        s = s.replace(c, "")
    s = s.replace("–", "-").replace("—", "-")
    # el guion blando U+00AD es invisible: los PDF del Instituto lo meten en el
    # punto donde parten la palabra, de modo que el volcado trae "actuacio\xad\nnes".
    # No es un guion de la frase, es el punto de corte, así que se quita entero.
    s = re.sub("\u00ad\\s*\\n\\s*", "", s).replace("\u00ad", "")
    # un PDF a dos columnas parte las palabras al final del renglón:
    # "acciden-\ntes", "contribu-\nyente". Si esa palabra se deja rota, una
    # cita copiada literalmente sale marcada como «no literal» por un motivo
    # tipográfico, y eso adiestra a no mirar la lista, que es donde se esconde
    # el hallazgo de verdad (manual, apartado 10). Se cose antes de colapsar
    # los espacios, porque después ya no se distingue el corte de renglón.
    # La lente de documento hace lo mismo y por la misma razón.
    s = re.sub(r"[-‐-―]\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def bloques_de_cita(texto):
    """Cada tramo seguido de líneas `> `, sin la atribución que abre con `> —`."""
    fuera, actual = [], []
    for linea in texto.split("\n"):
        if linea.startswith(">"):
            cuerpo = linea[1:].lstrip()
            # la línea de atribución no es cita: es la firma del temario
            if cuerpo.startswith("—"):
                continue
            actual.append(cuerpo)
        else:
            if actual:
                fuera.append("\n".join(actual))
                actual = []
    if actual:
        fuera.append("\n".join(actual))
    return fuera


def main(tema, fuentes):
    texto = open(tema, encoding="utf-8").read()
    volcado = " ".join(limpia(open(f, encoding="utf-8").read()) for f in fuentes)

    ok, malas = 0, 0
    for b in bloques_de_cita(texto):
        if "**" not in b:
            # un bloque en `>` sin negrita no es una cita literal de este método
            continue
        if b.lstrip().lstrip("*").startswith("Enunciado"):
            # el enunciado de la convocatoria no es cita de la norma: es el programa
            continue
        for tramo in re.findall(r"\*\*(.+?)\*\*", b, re.S):
            c = limpia(tramo)
            # los tramos muy cortos casan por casualidad y no dicen nada
            if len(c) < MINIMO:
                continue
            if c in volcado:
                ok += 1
            else:
                malas += 1
                print("  ! no literal: %s" % (c[:160] + ("..." if len(c) > 160 else "")))
    print("tramos de cita comprobados: %d ; no literales: %d" % (ok, malas))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2:]))
