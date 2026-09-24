#!/usr/bin/env python3
"""Cotejo de negritas: cada negrita del tema, contra **todas** sus fuentes.

La negrita es una promesa de literalidad. Las lentes de exactitud y de
documento anclan cada negrita en un artículo o miran una sola fuente, y en los
temas del común de Canal Sur —que citan «**texto**» (art. N) y mezclan leyes,
reglamentos, acuerdos y documentos sin articulado— cada verificador acababa
escribiendo su propio guion para hacer lo mismo: buscar cada negrita en todas
las fuentes y decir dónde está. Éste es ese guion, una vez y para todos.

Qué hace, negrita a negrita (tres palabras o más):

  · la busca, normalizada (sin tildes, sin puntuación, sin cortes de línea ni
    guiones de fin de renglón, sin la cabecera y el pie de página del BOJA),
    en el texto entero de cada fuente;
  · si la fuente es un volcado del BOE, dice **en qué artículo** aparece
    (también los numerados con palabras: «Artículo primero»);
  · si el tema la atribuye a un artículo —(art. N), «el art. N dice…»— y la
    negrita está en la fuente pero **no en ese artículo**, lo avisa aparte:
    es el error 1 del catálogo, la cita cruzada.

Salida: las no encontradas, las mal atribuidas y el recuento. Los rótulos
(ficha, tablas, siglas) salen como no encontrados; se reconocen a simple vista.

Uso:  negritas.py <tema.md> <fuente> [<fuente> ...]
      (fuentes .md del BOE o .txt de documentos, en cualquier número)
      negritas.py --todas <tema.md> <fuente> ...   # lista también las encontradas
"""
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tema import cuerpo as sin_envoltorio  # noqa: E402

ORD = {"primero": 1, "segundo": 2, "tercero": 3, "cuarto": 4, "quinto": 5,
       "sexto": 6, "septimo": 7, "octavo": 8, "noveno": 9, "decimo": 10,
       "undecimo": 11, "duodecimo": 12, "unico": 1}
DECENAS = {"decimo": 10, "vigesimo": 20, "trigesimo": 30, "cuadragesimo": 40,
           "quincuagesimo": 50, "sexagesimo": 60, "septuagesimo": 70,
           "octogesimo": 80, "nonagesimo": 90}


def sin_tildes(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def limpia(s):
    s = sin_tildes(s).lower()
    s = s.replace("«", " ").replace("»", " ").replace("—", " ").replace("–", " ")
    s = re.sub(r"[^a-z0-9ñ ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def ordinal(palabra):
    """«primero» -> 1, «decimotercero» -> 13, «vigésimo primero» -> 21."""
    p = sin_tildes(palabra).lower().replace(" ", "")
    if p in ORD:
        return ORD[p]
    for pref, n in DECENAS.items():
        if p.startswith(pref):
            resto = p[len(pref):]
            if not resto:
                return n
            if resto in ORD:
                return n + ORD[resto]
    return None


def prepara(texto):
    """Quita lo que parte las citas en los PDF: guiones de fin de renglón y
    la cabecera y el pie de cada página del BOJA."""
    texto = re.sub(r"[     　]", " ", texto)
    texto = re.sub(r"(?m)^\s*(\d{8}|Número \d+ - .*|página \d+(/\d+)?|"
                   r"Boletín Oficial de la Junta de Andalucía|BOJA|"
                   r"Depósito Legal:.*|https?://www\.juntadeandalucia\.es/eboja.*)\s*$",
                   " ", texto)
    return re.sub(r"(\w)-\n(\w)", r"\1\2", texto)


def articulos(texto):
    """{número: texto limpio} de un volcado del BOE; admite ordinales."""
    fuera = {}
    for m in re.finditer(r"(?ms)^## \[[^\]]+\] Art(?:ículo|\.)? "
                         r"([^\n.]+?)(?:\.[^\n]*)?$\n(.*?)(?=^## |\Z)", texto):
        clave = m.group(1).strip()
        num = re.match(r"(\d+(?: bis| ter| quáter| quinquies)?)", clave)
        if num:
            clave = num.group(1)
        else:
            n = ordinal(clave)
            if n is None:
                continue
            clave = str(n)
        fuera.setdefault(clave, []).append(limpia(m.group(2)))
    return {k: " ".join(v) for k, v in fuera.items()}


def atribucion(tema, ini, fin):
    """El artículo al que el tema atribuye la negrita, o None."""
    cola = tema[fin:fin + 200]
    corte = re.search(r"\.\s|\n\n", cola)
    cola = cola[:corte.start() + 1] if corte else cola
    p = re.search(r"\((?:[^()]*?\s)?(?:(?:[Aa]rts?\.|[Aa]rtículos?) ?(\d{1,3})"
                  r"( bis| ter)?|(\d{1,3})(?=\.\d))[^()]*\)", cola)
    if p:
        return (p.group(1) or p.group(3)) + (p.group(2) or "")
    cabeza = tema[max(tema.rfind(". ", 0, ini), tema.rfind("\n\n", 0, ini)) + 1:ini]
    q = list(re.finditer(r"(?:[Aa]rtículos?|[Aa]rts?\.) (\d{1,3})( bis| ter)?", cabeza))
    return q[-1].group(1) + (q[-1].group(2) or "") if q else None


def main():
    args = sys.argv[1:]
    todas = "--todas" in args
    args = [a for a in args if a != "--todas"]
    if len(args) < 2:
        sys.exit(__doc__)
    tema = sin_envoltorio(open(args[0], encoding="utf-8").read())
    fuentes = []
    for f in args[1:]:
        t = prepara(open(f, encoding="utf-8").read())
        fuentes.append((os.path.basename(f), limpia(t), articulos(t)))

    total = no = cruzadas = 0
    for m in re.finditer(r"\*\*(.+?)\*\*", tema, re.S):
        frag = limpia(m.group(1))
        if len(frag.split()) < 3:
            continue
        total += 1
        donde = [(nom, arts) for nom, entero, arts in fuentes if frag in entero]
        corto = re.sub(r"\s+", " ", m.group(1))[:110]
        if not donde:
            no += 1
            print("NO ESTÁ       %s" % corto)
            continue
        en_art = [n for _, arts in donde for n, t in arts.items() if frag in t]
        atr = atribucion(tema, m.start(), m.end())
        hay_arts = any(arts for _, arts in donde)
        if atr and hay_arts and en_art and atr not in en_art:
            cruzadas += 1
            print("¿ART. %-7s? %s  → está en art. %s" % (atr, corto, ", ".join(sorted(set(en_art)))))
        elif todas:
            print("ok  %-20s %s" % (",".join(n for n, _ in donde)[:20], corto))
    print()
    print("negritas cotejadas: %d ; no están en ninguna fuente: %d ; "
          "literales pero atribuidas a otro artículo: %d" % (total, no, cruzadas))


if __name__ == "__main__":
    main()
