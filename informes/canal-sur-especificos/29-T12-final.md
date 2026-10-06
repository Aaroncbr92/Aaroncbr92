# Puesto 29 · Tema 12 · Revisión de lo rematado (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/12-bases-de-datos-y-lenguaje-sql.md`.
Alcance: sólo los pasajes que lista `29-T12-remate.md`.

## Fuentes releídas (06-10-2026)

Volcados en `fuentes/canal-sur/informatico/web/`: `q-pgconf` (l. 195), `q-pgdatatype` (tabla 8.1 y
l. 569), `q-pgselect` (l. 345-351, 386-389, 403, 502, 875), `q-pgsubq` (l. 166-224), `q-pgbegin`,
`q-pgstarttrans`, `q-pgunion` (cap. 7.4).

## Pasajes revisados

| Pasaje | Resultado |
|---|---|
| § 3, Core (frase de entrada y cita 177/170, «at the time of writing») | Correcto, literal |
| § 5, tabla de tipos | Literal; «(epígrafe 3)» remite a la lista de tipos de «La norma y los dialectos»: antecedente correcto; «con o sin zona horaria» responde a las dos filas de `time`/`timestamp` |
| § 6, `START TRANSACTION`/`BEGIN` | Literal; `BEGIN TRANSACTION` de SQL Server lo sostiene la cita de Microsoft del mismo epígrafe |
| § 7, `GROUP BY`: dependencia funcional | Literal, pero **salvedad omitida (error 6)**: la definición citada es la de PostgreSQL y `q-pgselect` l. 875 dice que la norma fija más casos. **Corregido**: se añade esa cita con traducción |
| § 7, `USING`/`NATURAL` y caso práctico | Literal; las tablas del tema comparten `id_dep` y `nombre`: el caso es correcto |
| § 7, `ANY`/`SOME`/`ALL`/`NOT IN` y nulos | Literal; el ejemplo `NOT IN` es correcto (`id_dep` admite nulos). **Salvedad omitida**: el nulo con `ALL` (l. 216). **Corregido**: se añade la cita |
| § 7, operaciones de conjuntos | Literal (cap. 7.4); ejemplos coherentes con la condición. «No se exige que lean la misma tabla…» es deducción de la definición, no cita |
| Portada, «Qué se puede preguntar», Trazabilidad | Correctos; fila de referencia de PostgreSQL ampliada con «y lo que la norma añade»; Extensión 13.300 → 13.400 (`indice.py`: 13.370) |

Antecedentes: «esa dependencia», «Esa definición», «esa cita», «(epígrafe 3)», «(epígrafe 4)» tienen
delante su referente. Las dos citas nuevas se cotejaron de forma automática con los volcados: literales.

## Lentes

`refutar_prosa.py` → 0 hallazgos; `indice.py` → 54 epígrafes, sin cambios de índice.

## Ficheros tocados

El tema y este informe.
