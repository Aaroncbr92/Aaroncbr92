#!/usr/bin/env python3
"""Suma los TSV del cruce Canal Sur ↔ RTVE y escribe el resumen por puesto y ocupación.

Porcentaje de un puesto = media de `pct` sobre TODOS sus temas (los 10 comunes más
los específicos), cada tema con el mismo peso. Se da también por separado.
"""
import csv, glob, collections, sys
D = 'informes/canal-sur-reuso/'
occ = list(csv.DictReader(open('convocatoria/canal-sur/ocupaciones.tsv'), delimiter='\t'))
rows = {}
for f in sorted(glob.glob(D + '*.tsv')):
    for r in csv.DictReader(open(f), delimiter='\t'):
        k = (int(r['puesto']), int(r['tema']))
        if k in rows: sys.exit(f'duplicada {k} en {f}')
        rows[k] = r
com = [rows.get((0, t)) for t in range(1, 11)]
falta = [t for t, r in zip(range(1, 11), com) if r is None]
for o in occ:
    p, n = int(o['puesto']), int(o['temas'])
    falta += [(p, t) for t in range(1, n + 1) if (p, t) not in rows]
if falta: print('FALTAN', len(falta), falta[:20])
extra = [k for k in rows if k[0] and k[1] > int(occ[k[0]-1]['temas'])]
if extra: print('SOBRAN', extra)
pc = lambda r: float(r['pct']) if r else 0.0
comun = sum(pc(r) for r in com) / 10
res = []
for o in occ:
    p, n = int(o['puesto']), int(o['temas'])
    esp = [pc(rows.get((p, t))) for t in range(1, n + 1)]
    act = sum(1 for t in range(1, n + 1) if rows.get((p, t)) and rows[(p, t)]['actualizar'].startswith('s') and pc(rows[(p, t)]) > 0)
    tot = (comun * 10 + sum(esp)) / (10 + n)
    res.append(dict(o, esp=sum(esp) / n, tot=tot, casi=sum(1 for x in esp if x >= 80), nada=sum(1 for x in esp if x == 0), act=act))
print(f'comun {comun:.1f}')
for r in res: print(f"{r['puesto']:>2} {r['nombre'][:34]:34} esp {r['esp']:5.1f} tot {r['tot']:5.1f} ≥80:{r['casi']:>2} cero:{r['nada']:>2} plazas {r['plazas']}")
by = collections.defaultdict(list)
for r in res: by[r['ocupacion']].append(r)
print()
for k, v in sorted(by.items(), key=lambda kv: -sum(int(r['plazas']) for r in kv[1])):
    nt = sum(10 + int(r['temas']) for r in v)
    print(f"{k[:45]:45} plazas {sum(int(r['plazas']) for r in v):>3} tot {sum(r['tot']*(10+int(r['temas'])) for r in v)/nt:5.1f}")
