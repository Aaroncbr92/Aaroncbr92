#!/usr/bin/env python3
"""Refutación por exactitud: cada negrita del tema, contra su artículo.

El tema pone en negrita lo que es literal de la norma o casi. Este script troceo
el tema por artículos, saca las negritas de cada trozo y busca cada una en el
texto del artículo correspondiente. Lo que no aparece se imprime para mirarlo a
mano: puede ser una paráfrasis legítima, o puede ser una invención.

Uso:  refutar_exactitud.py <tema.md> <fuente.md>
"""
import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tema import cuerpo as sin_envoltorio
import unicodedata


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("«", '"').replace("»", '"').replace("—", " ").replace("–", " ")
    s = re.sub(r"[^a-z0-9ñ ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def articulos(fuente):
    fuera = {}
    # el índice del BOE devuelve a veces "Artículo\xa02" con espacio duro.
    # Si no se normaliza, el patrón no reconoce ni un artículo y la lente
    # devuelve "0 comprobadas, 0 no literales": un tema sin revisar que se
    # lee como impecable (manual, apartado 10)
    fuente = re.sub(r"[\u00a0\u2002\u2003\u2009\u202f\u3000]", " ", fuente)
    # "Artículo 32 bis" no acaba en dígito: con un patrón anclado en \d+$ ese
    # artículo no entra en el diccionario, no se comprueba nunca y además su
    # texto en el tema se contrasta contra el artículo 32, que dice otra cosa.
    # Un artículo que no se mira sale impecable (manual, apartado 10)
    patron = (r"^## \[[^\]]+\] Artículo (\d+(?: bis| ter| quáter| quinquies)?)$"
              r"\n\n_.*?_\n\n(.*?)(?=\n## |\Z)")
    # un tratado con anexos numera desde 1 dentro de cada anexo, así que
    # "Artículo 1" aparece muchas veces. Con un diccionario que sobrescribe,
    # sólo sobrevive el último y todo lo demás se contrasta **contra el
    # artículo equivocado sin dar ningún error** (manual, apartado 10). Se
    # guardan todas las versiones juntas y se avisa: así una cita literal de
    # cualquiera de ellas cuenta como encontrada, y quien lea el informe sabe
    # que la atribución por número no es fiable en esta fuente
    for m in re.finditer(patron, fuente, re.S | re.M):
        fuera.setdefault(m.group(1), []).append(limpia(m.group(2)))
    repes = sorted((n for n, v in fuera.items() if len(v) > 1), key=len)
    if repes:
        print("AVISO: la fuente repite estos números de artículo —%s—."
              % ", ".join(repes))
        print("       Numera desde 1 en cada anexo o parte, así que **la"
              " atribución por número no es fiable**:")
        print("       se comprueba contra la suma de todas las versiones y no"
              " contra una sola. Para esta fuente, la lente de documento dice"
              " más.")
        print()
    return {n: " ".join(v) for n, v in fuera.items()}

def abre_bloque(tema, i):
    """¿El marcador de la posición i abre epígrafe, o va dentro de una frase?

    Abre epígrafe el que empieza párrafo, encabezado, viñeta, fila de tabla o
    cita. No basta con mirar el renglón: el tema va partido por ancho de columna
    y una remisión cae a veces justo al principio de un renglón.
    """
    ini = tema.rfind("\n\n", 0, i) + 2
    trozo = tema[ini:i]
    ult = trozo.rfind("\n")
    # la viñeta pide espacio detrás: sin él, «**artículos 7 y 8**» al empezar
    # renglón se leería como viñeta y volvería a abrir epígrafe
    if ult != -1 and re.match(r"[-*+>]\s|\||\d+[.)]\s", trozo[ult + 1:]):
        trozo = trozo[ult + 1:]
    return re.fullmatch(r"[-*+>|#\s]*(?:\d+[.)]\s*)?", trozo) is not None


def limites(tema, marcas, cortes):
    """Dónde acaba el bloque de cada marcador.

    Hay dos clases de marcador y confundirlas cuesta caro en las dos
    direcciones:

    · El que **abre epígrafe** manda sobre todo su párrafo. Si una remisión
      interior se lo cortara, la explicación posterior se comprobaría contra el
      artículo citado y no contra el que se explica: no da error, atribuye mal.
    · El que va **dentro de una frase** puede ser una remisión («conoce las
      actuaciones de los artículos 7, 8, 9 y 11») o una mención con contenido
      («cierran el capítulo el art. 139, el art. 140…»). Como no se distinguen
      por la forma, se le da **solo su frase**: así la mención se comprueba y la
      remisión apenas arrastra ruido. Descartarlos a todos dejaba sin mirar los
      artículos descritos en una línea, que es peor.
    """
    fines = []
    aperturas = [m.start() for m in marcas if abre_bloque(tema, m.start())]
    for i, m in enumerate(marcas):
        tope = [c for c in cortes if c > m.start()]
        fin = tope[0] if tope else len(tema)
        if m.start() in aperturas:
            sig = [a for a in aperturas if a > m.start()]
            if sig:
                fin = min(fin, sig[0])
        else:
            sig = [x.start() for x in marcas[i + 1:]]
            if sig:
                fin = min(fin, sig[0])
            frase = re.search(r"[.:](?=\s)", tema[m.end():])
            if frase:
                fin = min(fin, m.end() + frase.end())
        fines.append(fin)
    return fines


def trozos(tema):
    """Devuelve [(nº de artículo, texto del tema que habla de él)]."""
    # el tema marca los artículos en negrita o como encabezado: si solo se busca
    # una de las dos formas, la comprobación no mira nada y no se queja
    # "Art. 104" cuenta igual que "Artículo 104": si solo se reconoce la forma
    # larga, los artículos abreviados no abren bloque y sus negritas se
    # comprueban contra el artículo anterior, que es el error de atribución
    marcas = list(re.finditer(
        r"(?:\*\*|(?m:^)#{2,4} )(?:[Aa]rtículos?|[Aa]rts?\.) ?(\d+)(?!\.\d|\.[ºª])"
        r"( bis| ter| quáter| quinquies)?(?: y (\d+))?(?: a (\d+))?[.,: *]", tema))
    # el bloque de un artículo termina en el siguiente artículo, en el siguiente
    # encabezado o en la siguiente raya: si no se acota, el último artículo se
    # traga el resto del tema y todo lo de después sale marcado como suyo
    cortes = [m.start() for m in re.finditer(r"(?m)^#{2,4} |^---$", tema)]
    fuera = []
    # un tema cita artículos de otras normas ("el artículo 4 de la Ley 17/2006").
    # Si esas remisiones abren bloque, el bloque se llena con texto ajeno y la
    # comprobación se hace contra el artículo equivocado
    marcas = [m for m in marcas
              if not re.match(r"[^.]{0,40}?\bde la [Ll]ey\b", tema[m.end():m.end() + 60])]
    for m, fin in zip(marcas, limites(tema, marcas, cortes)):
        # las claves son cadenas porque "32 bis" es un artículo y no un número
        if m.group(4):
            nums = [str(n) for n in range(int(m.group(1)), int(m.group(4)) + 1)]
        elif m.group(3):
            nums = [m.group(1), m.group(3)]
        else:
            nums = [m.group(1) + (m.group(2) or "")]
        fuera.append((nums, tema[m.start():fin]))
    return fuera


def main():
    # fuera la portada y el índice: son envoltorio, no afirmaciones del tema
    tema = sin_envoltorio(open(sys.argv[1], encoding="utf-8").read())
    fuente = open(sys.argv[2], encoding="utf-8").read()
    arts = articulos(fuente)

    total = sospechosas = 0
    for nums, bloque in trozos(tema):
        cuerpo = " ".join(arts.get(n, "") for n in nums)
        if not cuerpo:
            continue
        # sin re.S el punto no cruza el salto de línea, y una cita en negrita
        # repartida en dos renglones —que es lo normal cuando el tema va a
        # ancho de columna— no la ve nadie: no sale como no literal, sale como
        # si no existiera. Un tema con las citas largas sin comprobar da un
        # recuento bajo y limpio, que es el fallo del apartado 10 del manual
        for negrita in re.findall(r"\*\*(.+?)\*\*", bloque, re.S):
            frag = limpia(negrita)
            if len(frag.split()) < 3:       # una o dos palabras no dice nada
                continue
            if frag.startswith("articulo"):  # el propio encabezado
                continue
            total += 1
            if frag not in cuerpo:
                sospechosas += 1
                print("art. %-14s %s" % (",".join(nums), negrita))
    print()
    print("negritas comprobadas: %d ; no literales: %d" % (total, sospechosas))


if __name__ == "__main__":
    main()
