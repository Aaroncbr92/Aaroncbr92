#!/usr/bin/env python3
"""Refutación por modo verbal y salvedades (errores 4 y 6 del manual).

Dos comprobaciones por artículo:

  · **Modo verbal.** Si la norma dice «podrá» y el tema dice «deberá», o al revés,
    cambia la respuesta y no se ve leyendo por encima.
  · **Salvedades.** Si el artículo tiene un «salvo», «excepto» o «sin perjuicio» y
    el tema no lo recoge, se ha convertido en absoluta una regla que no lo es.
    Es el error que más puntos cuesta.
"""
import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tema import cuerpo as sin_envoltorio
import unicodedata

# el subjuntivo cuenta: «cuando no pueda compensar» es tan potestativo como «podrá»,
# y sin él la lente daba por cambiado el modo verbal donde no lo estaba
PODER = r"\b(podr[áa]n?|puede[n]?|pueda[n]?|pudiera[n]?|potestativ\w+|facultad\w*)\b"
# "están obligados a" es tan imperativo como "deberán", y sin él la lente daba
# por impuesto lo que la norma sí impone (art. 98 de la Ley 13/2022)
# "habrán de informar" es tan imperativo como "deberán", y el patrón solo traía
# el singular "habrá de": el artículo 89.1 de la LO 3/2018 usa el plural y la
# lente daba por cambiado el modo verbal donde el tema decía justo lo que dice
# la norma. Un falso positivo constante enseña a no mirar la lista (manual, 10)
DEBER = (r"\b(deber[áa]n?|debe[n]?|deba[n]?|debiendo|obligator\w+|obligad[oa]s?"
         r"|exigir[áa]n?|requerir[áa]n?|habr[áa]n? de|ha de|han de|hubieran? de)\b")
SALVO = r"\b(salvo|excepto|a excepci[oó]n|sin perjuicio|no obstante)\b"


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s.lower())


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


def bloques(tema):
    # dos formas que la lente no reconocía y que dejaban artículos sin mirar:
    # la abreviatura ("Art. 104") y los rótulos de rango ("Artículos 53 a 56"),
    # de los que solo se comprobaba el primero. Un artículo no comprobado sale
    # impecable, que es peor que salir con hallazgos.
    marcas = list(re.finditer(
        r"(?:\*\*|(?m:^)#{2,4} )(?:[Aa]rtículos?|[Aa]rts?\.) ?(\d+)(?!\.\d|\.[ºª])"
        r"( bis| ter| quáter| quinquies)?(?: y (\d+))?(?: a (\d+))?[.,: *]", tema))
    cortes = [m.start() for m in re.finditer(r"(?m)^#{2,4} |^---$", tema)]
    fuera = {}
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
        # un epígrafe que cubre varios artículos se contrasta con los textos de
        # todos ellos juntos, no con cada uno por separado: si no, lo que dice
        # del primero sale como hallazgo contra los demás
        clave = tuple(nums)
        fuera.setdefault(clave, "")
        fuera[clave] += " " + limpia(tema[m.start():fin])
    # un epígrafe de rango ("Artículos 67 a 70") seguido de una viñeta por
    # artículo ("**Art. 67.**") se queda con el rótulo y nada más: comprobarlo
    # contra el texto de los cuatro artículos da hallazgos que en realidad
    # están resueltos en las viñetas
    sueltos = {n for c in fuera if len(c) == 1 for n in c}
    for c in list(fuera):
        if len(c) > 1 and set(c) <= sueltos:
            del fuera[c]
    return fuera


def main():
    # fuera la portada y el índice: son envoltorio, no afirmaciones del tema
    tema = sin_envoltorio(open(sys.argv[1], encoding="utf-8").read())
    arts = articulos(open(sys.argv[2], encoding="utf-8").read())
    hallazgos = 0
    for nums, texto in sorted(bloques(tema).items()):
        fuente = " ".join(arts[n] for n in nums if n in arts)
        if not fuente:
            continue
        n = ",".join(nums)
        f_poder, f_deber = bool(re.search(PODER, fuente)), bool(re.search(DEBER, fuente))
        t_poder, t_deber = bool(re.search(PODER, texto)), bool(re.search(DEBER, texto))
        if t_deber and not f_deber and not f_poder:
            print("art. %-8s el tema impone («%s») donde la norma no usa deber ni poder"
                  % (n, re.search(DEBER, texto).group(0)))
            hallazgos += 1
        if t_deber and f_poder and not f_deber:
            print("art. %-8s la norma solo dice «%s» y el tema dice «%s»"
                  % (n, re.search(PODER, fuente).group(0), re.search(DEBER, texto).group(0)))
            hallazgos += 1
        if t_poder and f_deber and not f_poder:
            print("art. %-8s la norma solo dice «%s» y el tema dice «%s»"
                  % (n, re.search(DEBER, fuente).group(0), re.search(PODER, texto).group(0)))
            hallazgos += 1
        if re.search(SALVO, fuente) and not re.search(SALVO, texto):
            m = re.search(r".{0,70}" + SALVO + r".{0,90}", fuente)
            print("art. %-8s salvedad de la norma que el tema no recoge: ...%s..."
                  % (n, m.group(0).strip()))
            hallazgos += 1
    print()
    print("hallazgos: %d" % hallazgos)


if __name__ == "__main__":
    main()
