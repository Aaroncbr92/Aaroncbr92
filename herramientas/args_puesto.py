#!/usr/bin/env python3
"""Datos de reutilización de un puesto de Canal Sur, en JSON, para el workflow.

Por cada tema: los ficheros de RTVE aprovechables con su porcentaje y nota
(informes/canal-sur-reuso/*.tsv) y, si el tema repite otro ya escrito por un
puesto anterior, cuál (informes/canal-sur-especificos/AGRUPACION.tsv).
Así el agente no busca qué reutilizar: se lo dan hecho.

Uso:  args_puesto.py <puesto>
"""
import csv, glob, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = sys.argv[1].lstrip("0")
fich = glob.glob(os.path.join(RAIZ, "convocatoria/canal-sur/especificos/%02d-*.md" % int(p)))[0]
temas = {}
for f in glob.glob(os.path.join(RAIZ, "informes/canal-sur-reuso/*.tsv")):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
        if r["puesto"] == p and r["rtve"] not in ("", "-"):
            temas.setdefault(r["tema"], {})["rtve"] = {"ficheros": r["rtve"].split(";"), "pct": int(r["pct"] or 0),
                                                       "actualizar": r["actualizar"], "nota": r["nota"]}
for r in csv.DictReader(open(os.path.join(RAIZ, "informes/canal-sur-especificos/AGRUPACION.tsv"), encoding="utf-8"), delimiter="\t"):
    if r["puesto"] == p and r["tipo"] != "nuevo":
        # «aplicada al puesto»: mismo enunciado, pero los riesgos o funciones del
        # puesto cambian; se copia y se amplía, nunca se copia sin más
        tipo = "parecido" if "del puesto" in r["enunciado"] or "al puesto" in r["enunciado"] else r["tipo"]
        temas.setdefault(r["tema"], {})["repite"] = {"tipo": tipo, "puesto": r["escrito_en_puesto"], "tema": r["escrito_en_tema"]}
print(json.dumps({"puesto": p.zfill(2), "slug": os.path.basename(fich)[:-3], "temas": temas}, ensure_ascii=False))
