# 34 · T11 · Revisión del remate (fase 5 bis)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/11-materias-sensibles.md`.
Alcance: sólo los pasajes que lista `34-T11-remate.md` (G1, M1-M4, L1-L6, «Qué se puede preguntar»,
ficha, Normativa, «Lo que no da», Trazabilidad).

## Fuentes releídas (todas el 24-09-2026)

- Libro de estilo (`fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`): 3.2.2 (l. 1430-1437);
  9.2.10-9.2.11.1 (l. 4574-4590); 9.2.12.2-9.2.12.4 (l. 4671-4718); 9.3.3.1-9.3.4.1 (l. 4991-5055);
  9.4.2-9.4.2.2 (l. 5462-5563); 9.5.4.1 (l. 5715-5741); 9.6.1.2-9.6.2.2 (l. 5789-5932);
  9.7-9.7.2.3 (l. 6022-6135); 9.9-9.9.2 (l. 6203-6269).
- LGCA (BOE-A-2022-11311): art. 7 (l. 190-193); rúbrica del título IV (l. 1052-1053); art. 83
  (l. 1132-1134); título VI y su capítulo I (l. 1270-1280); arts. 95 y 96 (l. 1284, 1293).
- CE (`boe.py precepto BOE-A-1978-31229 a20`): art. 20.4.

## Resultado

Todos los literales en negrita de los pasajes nuevos coinciden con su fuente; las atribuciones de
epígrafe son correctas (el resumen de cinco puntos, al final del 9.6.2.2; «sospechoso» y suicidio,
en el 9.5.4.1; el ardid y los rostros «cubiertos o tramados», en el 9.9). La salvedad de «tregua»
está dicha como en la fuente. Antecedentes comprobados: «En el mismo epígrafe» (§3 → 9.4.2.2;
§7 → 9.5.4.1), «El mismo 9.9» (§9), «Los arts. 95 y 96» (§3), «que el 3.2.2 prohíbe» (§6),
«su presencia» (§4 → personas con discapacidad): todos tienen delante su antecedente.

## Correcciones aplicadas (comprobadas en la fuente)

| Id | Pasaje | Antes | Ahora | Fuente |
| --- | --- | --- | --- | --- |
| C1 | §3, Libro 9.4.2 | «Si el menor es familiar de un delincuente» | «familiar o allegado de un delincuente» | 9.4.2: «Si el menor es familiar o allegado de un delincuente» (salvedad omitida, error 6) |
| C2 | §3, Libro 9.4.2 | «padres, tutores o parientes» | «padres, tutores, allegados o parientes» | 9.4.2: «padres, tutores, allegados o parientes» |
| C3 | §3, LGCA 83.2 | «en noticiarios» | «en noticiarios y programas informativos de actualidad» | 83.2: «en noticiarios y los programas de contenido informativo de actualidad» |
| C4 | Trazabilidad, fila LGCA | Epígrafes 1, 2, 3, 4, 10, 12 | añade 11 | el §11 cita el art. 4.2 |
| C5 | Ficha, Extensión | 7.171 palabras | 7.180 palabras | `indice.py` tras C1-C3 |

Sin hallazgos graves. Ningún dato quitado.

## Lentes

- `indice.py`: 24 epígrafes, 7.180 palabras.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py`, `refutar_exactitud.py`, `refutar_modo.py`: no se corren de nuevo; las correcciones
  no tocan negritas ni pasajes de ley en redonda salvo la paráfrasis del 83.2, cotejada a mano.

Ficheros tocados: el tema y este informe.
