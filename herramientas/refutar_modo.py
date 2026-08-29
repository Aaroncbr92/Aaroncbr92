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
import unicodedata

# el subjuntivo cuenta: «cuando no pueda compensar» es tan potestativo como «podrá»,
# y sin él la lente daba por cambiado el modo verbal donde no lo estaba
PODER = r"\b(podr[áa]n?|puede[n]?|pueda[n]?|pudiera[n]?|potestativ\w+|facultad\w*)\b"
DEBER = r"\b(deber[áa]n?|debe[n]?|deba[n]?|obligator\w+|exigir[áa]|requerir[áa]|habr[áa] de|ha de|han de)\b"
SALVO = r"\b(salvo|excepto|a excepci[oó]n|sin perjuicio|no obstante)\b"


def limpia(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s.lower())


def articulos(fuente):
    fuera = {}
    for m in re.finditer(r"^## \[[^\]]+\] Artículo (\d+)$\n\n_.*?_\n\n(.*?)(?=\n## |\Z)",
                         fuente, re.S | re.M):
        fuera[int(m.group(1))] = limpia(m.group(2))
    return fuera


def bloques(tema):
    # dos formas que la lente no reconocía y que dejaban artículos sin mirar:
    # la abreviatura ("Art. 104") y los rótulos de rango ("Artículos 53 a 56"),
    # de los que solo se comprobaba el primero. Un artículo no comprobado sale
    # impecable, que es peor que salir con hallazgos.
    marcas = list(re.finditer(
        r"(?:\*\*|(?m:^)#{2,4} )(?:Artículos?|Arts?\.) ?(\d+)"
        r"(?: y (\d+))?(?: a (\d+))?[.,: ]", tema))
    cortes = [m.start() for m in re.finditer(r"(?m)^#{2,4} |^---$", tema)]
    fuera = {}
    for i, m in enumerate(marcas):
        sig = marcas[i + 1].start() if i + 1 < len(marcas) else len(tema)
        cand = [c for c in cortes if c > m.start()]
        fin = min(sig, cand[0]) if cand else sig
        nums = [int(g) for g in m.groups() if g]
        if m.group(3):
            nums = list(range(int(m.group(1)), int(m.group(3)) + 1))
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
    tema = open(sys.argv[1], encoding="utf-8").read()
    arts = articulos(open(sys.argv[2], encoding="utf-8").read())
    hallazgos = 0
    for nums, texto in sorted(bloques(tema).items()):
        fuente = " ".join(arts[n] for n in nums if n in arts)
        if not fuente:
            continue
        n = ",".join(str(x) for x in nums)
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
