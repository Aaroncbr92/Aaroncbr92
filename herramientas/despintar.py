#!/usr/bin/env python3
"""Quita la negrita de lo que **no** es cita literal de ninguna fuente.

La regla del proyecto es que **la negrita es una promesa de literalidad**: si un
fragmento va en negrita, tiene que estar, palabra por palabra, en alguna de las
fuentes del tema. Escribiendo, la costumbre tira de poner en negrita también el
énfasis propio —«tres familias, y las tres se preguntan»—, y eso convierte la
lente de exactitud en un listado de decenas de avisos donde los hallazgos de
verdad se pierden entre el ruido.

Esta herramienta hace **una sola cosa y de forma conservadora**: recorre las
negritas del tema y quita la marca **sólo a las que no aparecen en ninguna de las
fuentes que se le pasan**. Lo que sí aparece se queda en negrita, aunque la lente
lo hubiera marcado por un problema de atribución de artículo; ésos hay que
mirarlos a mano, porque la lente puede estar comparando contra el artículo
equivocado y quitarles la negrita sería **borrar una cita buena**.

No decide si el énfasis está bien puesto: sólo retira una promesa que el texto no
cumple. Lo que quede sin negrita y merezca destacarse, se pone en cursiva a mano.

Uso:  despintar.py <tema.md> <fuente.md> [<fuente2.md> ...]
      despintar.py --ver <tema.md> <fuente.md> ...   (sólo lista, no toca nada)
      despintar.py --cursiva <tema.md> <fuente.md> ...

Con `--cursiva` la marca no se borra: se rebaja a cursiva, que es lo que la
convención del proyecto reserva para los rótulos propios del tema. Se rebaja
sólo lo que ya se iba a despintar, y se deja en texto llano —sin cursiva— lo
que lleve dentro otro énfasis, porque anidar asteriscos rompe el marcado.
"""
import re
import sys
import unicodedata


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("«", '"').replace("»", '"').replace("—", " ").replace("–", " ")
    s = re.sub(r"[^a-z0-9ñ ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def cuerpo_sin_envoltorio(texto):
    """Fuera la portada y el índice: son envoltorio del generador, no del autor."""
    texto = re.sub(r"(?s)<!-- portada -->.*?<!-- /portada -->", "", texto)
    return re.sub(r"(?s)<!-- indice -->.*?<!-- /indice -->", "", texto)


def main():
    ver = "--ver" in sys.argv
    cursiva = "--cursiva" in sys.argv
    args = [a for a in sys.argv[1:] if a not in ("--ver", "--cursiva")]
    ruta, fuentes = args[0], args[1:]
    texto = open(ruta, encoding="utf-8").read()
    corpus = " ".join(limpia(open(f, encoding="utf-8").read()) for f in fuentes)

    quitadas = []

    def decide(m):
        dentro = m.group(1)
        frag = limpia(dentro)
        # una o dos palabras no prometen nada: un rótulo de tabla, un número
        if len(frag.split()) < 3:
            return m.group(0)
        if frag in corpus:
            return m.group(0)
        quitadas.append(dentro)
        if cursiva and "*" not in dentro:
            return "*%s*" % dentro
        return dentro

    # la portada y el índice se dejan como están: son del generador
    cabeza, cola = "", texto
    m = re.search(r"(?s)^(.*?<!-- /indice -->\n)", texto)
    if m:
        cabeza, cola = m.group(1), texto[m.end():]
    nuevo = re.sub(r"\*\*(.+?)\*\*", decide, cola, flags=re.S)

    for q in quitadas:
        print("  – %s" % re.sub(r"\s+", " ", q)[:100])
    print("%s: %d negritas %s por no estar en ninguna fuente"
          % (ruta, len(quitadas), "rebajadas a cursiva" if cursiva else "retiradas"))
    if not ver and quitadas:
        open(ruta, "w", encoding="utf-8").write(cabeza + nuevo)


if __name__ == "__main__":
    main()
