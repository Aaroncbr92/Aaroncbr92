# Puesto 29 · Tema 12 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/12-bases-de-datos-y-lenguaje-sql.md`.
Entrada: `29-T12-refutacion.md` (2 hallazgos menores, 5 lagunas) y `29-T12-preguntas.md` (10 / 1 / 4).

## Fuentes

- Releídas el 06-10-2026 en sus volcados (descargados el 05-10-2026): `q-pgselect` (l. 349-351, 389,
  502), `q-pgsubq` (§ 9.24.3 a 9.24.5), `q-pgdatatype` (tabla 8.1).
- Descargadas y leídas el 06-10-2026 (nuevas, en `fuentes/canal-sur/informatico/web/`):
  `q-pgbegin.txt` (PostgreSQL 18, `BEGIN`), `q-pgstarttrans.txt` (PostgreSQL 18,
  `START TRANSACTION`) y `q-pgunion.txt` (PostgreSQL 18, cap. 7.4 «Combining Queries»). La tercera
  se bajó porque `q-pgselect` l. 502 da la condición de compatibilidad sólo para `UNION`; el cap. 7.4
  la da para las tres operaciones.

Todas las citas nuevas en negrita se han cotejado de forma automática con los volcados: literales las
30. Ninguna corrección del informe resultó equivocada.

## Hallazgos de exactitud

| # | Pasaje cambiado | Antes | Después |
|---|---|---|---|
| 1 | § 7, «`GROUP BY` y `HAVING`», último párrafo | Regla del `SELECT` tajante y «de oficio»; sólo cita del `HAVING` | Regla «con una salvedad» y cita literal de PostgreSQL para la lista del `SELECT` (dependencia funcional) con su definición; ejemplo `GROUP BY id_emp` frente a `GROUP BY id_dep`; la cita del `HAVING` queda como «Lo mismo vale para el `HAVING`» |
| 1 | Trazabilidad, lista de oficio | «la regla de que toda columna no agregada del `SELECT` debe figurar en el `GROUP BY`» | Suprimido (ya tiene fuente) |
| 2 | § 3, «Niveles de conformidad y funciones Core», frase de entrada | «Ningún gestor declara cumplir siquiera el Core entero.» | «Cuando PostgreSQL escribió su página, ningún gestor declaraba cumplir siquiera el Core de SQL:2023 entero.» |
| 2 | Trazabilidad, fila «Appendix D» | «ningún gestor declara el Core entero» | «ningún gestor declaraba, al escribirse la página, el Core de SQL:2023 entero» |

## Lagunas (se amplía el tema)

| # | Pasaje añadido | Contenido |
|---|---|---|
| L3 | § 5, «CREATE TABLE», tras el ejemplo | Tabla de tipos con la descripción literal de PostgreSQL: `char`/`varchar` (fija/variable), enteros de 2/4/8 bytes, `numeric`/`decimal`, `real`/`double precision`, `boolean`, `date`, `time`, `timestamp`, `interval` |
| L4 | § 6, «Las transacciones (TCL)», tabla y párrafo tras `COMMIT`/`ROLLBACK` | Fila «`START TRANSACTION` (en la norma); `BEGIN` en PostgreSQL, `BEGIN TRANSACTION` en SQL Server»; citas: `BEGIN` extensión equivalente a `START TRANSACTION`; misma funcionalidad; en la norma cualquier sentencia abre implícitamente la transacción |
| L5 | § 7, «Combinaciones (JOIN)», tras la cita de las tres condiciones | Traducción de esa cita; tabla `USING` y `NATURAL` con citas literales; caso práctico: con las tablas del tema `NATURAL JOIN` emparejaría también por `nombre`; `USING (id_dep)` sí |
| L2 | § 7, «Subconsultas», al final | Tabla `ANY`/`SOME`, `ALL`, `NOT IN` con citas (`SOME` sinónimo, `IN` = `= ANY`, `NOT IN` = `<> ALL`); ejemplos `> ALL` y `> ANY`; trampa del nulo en `NOT IN` (con ejemplo) y en `ANY` |
| L1 | § 7, «Operaciones de conjuntos», al final | Cita de «union compatible» (mismo número de columnas y tipos compatibles), para las tres operaciones; ejemplos válido y erróneo |

## Otros pasajes tocados

- Portada, «Extensión»: 11.500 → 13.300 palabras (medida de `indice.py`: 13.263).
- «Qué se puede preguntar»: añade `ANY`/`SOME`, `ALL`, `NOT IN`, tipos, `START TRANSACTION`,
  `USING`/`NATURAL` y la condición de las operaciones de conjuntos.
- Trazabilidad: frase de fechas (tres páginas leídas el 06-10-2026); fila de referencia de PostgreSQL
  ampliada; dos filas nuevas (`BEGIN` y `START TRANSACTION`; cap. 7.4).
- La cita de condiciones de combinación se reparte en línea de otro modo (`ON join_condition` en una
  sola línea), sin cambiar su texto, para que la lente de negritas no la lea partida.

Antecedentes revisados: «(epígrafe 3)» en la tabla de tipos remite a «La norma y los dialectos»;
«esa dependencia» y «esa cita» tienen delante su antecedente.

## Lentes

Tema técnico sin norma: `refutar_prosa.py` → 0 hallazgos (un primer paso dio una paridad de negritas
por un código partido en dos líneas; corregido). `indice.py` → 54 epígrafes, sin epígrafes nuevos;
índice intacto. Las preguntas 11 a 15 tienen ya respuesta entera en el tema.

## Ficheros tocados

El tema; este informe; tres volcados nuevos en `fuentes/canal-sur/informatico/web/` (`q-pgbegin.txt`,
`q-pgstarttrans.txt`, `q-pgunion.txt`). Copia previa del tema en el scratchpad de la sesión.
Se amplió contenido nuevo: procede la fase 5 bis.
