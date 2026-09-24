#!/usr/bin/env python3
"""Agrupa los temas repetidos de los temarios específicos de Canal Sur.

Un tema que aparece en varios puestos se escribe una vez: lo escribe el primer
puesto en el orden de trabajo (más plazas primero) y los demás lo reutilizan.

  · idénticos: mismo enunciado, sin tildes, mayúsculas ni puntuación;
  · parecidos: coincidencia de palabras (Jaccard) ≥ el umbral (0,5 por defecto; medido: por debajo empiezan temas distintos).
    Los parecidos NO se reutilizan sin más: el agente compara los dos
    enunciados y amplía el tema escrito con lo que el nuevo pida de más.

Uso:  agrupar_especificos.py [umbral]
Escribe informes/canal-sur-especificos/AGRUPACION.tsv y ORDEN.md.
"""
import csv, glob, os, re, sys, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESP = os.path.join(RAIZ, "convocatoria/canal-sur/especificos")
OUT = os.path.join(RAIZ, "informes/canal-sur-especificos")
VACIAS = set("de la el los las y en a del o con su sus para por al e u sobre un una".split())


def norma(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9ñ ]+", " ", s)).strip()


def main():
    umbral = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    filas = list(csv.DictReader(open(os.path.join(RAIZ, "convocatoria/canal-sur/ocupaciones.tsv")), delimiter="\t"))
    orden = sorted(filas, key=lambda f: (-int(f["plazas"]), int(f["puesto"])))
    rango = {int(f["puesto"]): i for i, f in enumerate(orden)}
    temas = []  # (rango, puesto, n, texto, normalizado, palabras)
    for f in glob.glob(os.path.join(ESP, "[0-9][0-9]-*.md")):
        p = int(os.path.basename(f)[:2])
        for m in re.finditer(r"(?m)^(\d+)\. (.+)$", open(f, encoding="utf-8").read()):
            n = norma(m.group(2))
            temas.append((rango[p], p, int(m.group(1)), m.group(2), n, set(n.split()) - VACIAS))
    temas.sort()
    grupo, origen = {}, []  # índice -> (tipo, índice del original)
    for i, t in enumerate(temas):
        mejor = None
        for j in origen:
            o = temas[j]
            if o[1] == t[1]:
                continue
            if o[4] == t[4]:
                mejor = ("identico", j, 1.0)
                break
            jac = len(t[5] & o[5]) / max(1, len(t[5] | o[5]))
            if jac >= umbral and (not mejor or jac > mejor[2]):
                mejor = ("parecido", j, jac)
        if mejor:
            grupo[i] = mejor
        else:
            origen.append(i)
    with open(os.path.join(OUT, "AGRUPACION.tsv"), "w", encoding="utf-8") as w:
        w.write("puesto\ttema\ttipo\tescrito_en_puesto\tescrito_en_tema\tsemejanza\tenunciado\n")
        for i, t in enumerate(temas):
            g = grupo.get(i)
            o = temas[g[1]] if g else None
            w.write("%d\t%d\t%s\t%s\t%s\t%s\t%s\n" % (t[1], t[2], g[0] if g else "nuevo",
                    o[1] if o else "", o[2] if o else "", "%.2f" % g[2] if g else "", t[3]))
    nombres = {int(f["puesto"]): f for f in filas}
    lin = ["# Orden de trabajo de los específicos (más plazas primero)", "",
           "Generado por `herramientas/agrupar_especificos.py` (umbral %.2f). " % umbral +
           "«Nuevos» se escriben; «idénticos» se reutilizan tal cual (con su cabecera "
           "reescrita); «parecidos» se reutilizan ampliando lo que el enunciado pida de más.", "",
           "| Orden | Puesto | Plazas | Temas | Nuevos | Idénticos | Parecidos |", "|---:|---|---:|---:|---:|---:|---:|"]
    tot = [0, 0, 0, 0]
    for k, f in enumerate(orden, 1):
        p = int(f["puesto"])
        mios = [i for i, t in enumerate(temas) if t[1] == p]
        c = [sum(1 for i in mios if grupo.get(i, ("nuevo",))[0] == x) for x in ("nuevo", "identico", "parecido")]
        tot = [a + b for a, b in zip(tot, [len(mios)] + c)]
        lin.append("| %d | %02d %s | %s | %d | %d | %d | %d |" % (k, p, f["nombre"], f["plazas"], len(mios), *c))
    lin.append("| | **Total** | 228 | %d | %d | %d | %d |" % tuple(tot))
    open(os.path.join(OUT, "ORDEN.md"), "w", encoding="utf-8").write("\n".join(lin) + "\n")
    print("temas %d · nuevos %d · idénticos %d · parecidos %d" % tuple(tot))


if __name__ == "__main__":
    main()
