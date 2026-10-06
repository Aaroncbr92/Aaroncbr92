# Puesto 29 · Tema 12 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en sus volcados
`fuentes/canal-sur/informatico/web/q-*.txt` (descargados el 05-10-2026); no se descargó nada.
No se corrige el tema: sólo se informa.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/12-bases-de-datos-y-lenguaje-sql.md`
(12.337 palabras con código).

## Alcance

- Exactitud: todo salvo lo «Copiado de RTVE sin cambios» que lista `29-T12-redaccion.md` (tablas
  base de datos/SGBD y nombres corrientes/formales, definición de clave primaria, formas normales,
  matiz `DROP`/`DELETE`/`TRUNCATE`, bloque de cláusulas, distinción `WHERE`/`HAVING`). Copiado del
  común: nada.
- Cobertura: el tema entero frente al enunciado (BOJA núm. 186, Anexo V, puesto 2.29, punto 12).
- Lentes: tema técnico sin norma; no proceden `negritas.py`, `refutar_exactitud.py` ni
  `refutar_modo.py`. La verificación ya pasó `refutar_prosa.py` e `indice.py`.

## Lente 1 · Exactitud

Comprobado contra la fuente (muestra dirigida a lo más preguntable y a lo que la verificación no
listó): `SQL:2008 introduced…` e IBM DB2 (q-pgselect l. 581 y 879); paréntesis de `TOP` y
`OFFSET`/`FETCH` (q-mstop l. 63, 71, 150); listas DDL/DML/permisos de Microsoft, con `RENAME` y
`BULK INSERT` (q-mstsql); orden lógico y «paso 8» (q-msselect l. 115-131); categorías y control de
transacciones de Oracle con `SET TRANSACTION` y `SET CONSTRAINT` (q-oratypes l. 178-200); `COMMIT` y
`ROLLBACK` y sus extensiones (q-pgcommit, q-pgrollback l. 167); `BEGIN` implícito y `ROLLBACK TO`
(q-pgtrans); `RESTRICT` sin aplazamiento (q-pgconstr l. 493); Core 177/170 y «at the time of
writing» (q-pgconf l. 195); `WITH GRANT OPTION` (q-pggrant l. 233); «Typically» (q-oradbconcepts
l. 52); y la atribución de trece citas sueltas (`LEFT JOIN`, alias, estilo, subconsulta, `NATURAL`,
`HAVING`, `BETWEEN`, `LIKE`, `INSERT`, privilegio `SELECT`, columnas tipadas). Todo coincide.

| # | Error | Dónde | Qué pasa | Gravedad |
|---|---|---|---|---|
| 1 | 9 / 6 | § 7, «`GROUP BY` y `HAVING`», último párrafo; Trazabilidad, lista de oficio | La regla «Una columna del `SELECT` que no esté en un agregado tiene que estar en el `GROUP BY`» se da tajante y se declara «de oficio», pero PostgreSQL la dice literal para la lista del `SELECT`, con su salvedad: **«it is not valid for the `SELECT` list expressions to refer to ungrouped columns except within aggregate functions or when the ungrouped column is functionally dependent on the grouped columns»**, y define la dependencia funcional (**«if the grouped columns (or a subset thereof) are the primary key of the table containing the ungrouped column»**) (q-pgselect l. 389). Se cita la variante del `HAVING` y se deja la del `SELECT` sin fuente ni salvedad | Menor |
| 2 | 6 | § 3, «Niveles de conformidad…», frase de entrada («Ningún gestor declara cumplir siquiera el Core entero») y Trazabilidad («ningún gestor declara el Core entero») | Afirmación absoluta. La fuente la limita a **«at the time of writing»** y a **«Core SQL:2023»**. La cita que sigue sí lo dice, pero la frase del tema y la Trazabilidad no | Menor |

Sin errores graves. No se hallaron citas mal atribuidas, recuentos que no cuadren ni redacciones
superadas.

## Lente 2 · Cobertura del enunciado

Las cinco rúbricas (lenguaje de interrogación, estándar ANSI SQL, DDL, DML, DQL) tienen epígrafe
propio y en su orden; «Bases de datos» se desarrolla en el § 1. Preguntas en `29-T12-preguntas.md`:
**10 enteras, 1 a medias, 4 no**. Lagunas (se amplía el tema, con fuentes ya descargadas salvo la 4):

| # | Rúbrica | Qué falta | Fuente |
|---|---|---|---|
| L1 | DQL | Condición de las operaciones de conjuntos: mismo número de columnas y tipos compatibles (pregunta 11) | q-pgselect l. 502 |
| L2 | DQL | Predicados `ANY`/`SOME` y `ALL` con subconsulta, y `NOT IN` (con su trampa de los nulos) (pregunta 12) | q-pgsubq § 9.24.3 a 9.24.5 |
| L3 | DDL | Qué son los tipos básicos que el tema enumera: longitud fija (`char`) frente a variable (`varchar`), numéricos, fecha (pregunta 13) | q-pgdatatype (l. 355 y 361) |
| L4 | Estándar / transacciones | `START TRANSACTION` como forma de la norma frente a `BEGIN` / `BEGIN TRANSACTION` (pregunta 14) | Página `START TRANSACTION` o `BEGIN` de PostgreSQL 18, apartado «Compatibility» (no descargada) |
| L5 | DQL | Qué hace `NATURAL` (y `USING`) en una combinación: sólo se nombra (pregunta 15) | q-pgselect l. 349-351 |

## Recuento

- Graves: 0.
- Menores: 2 (hallazgos 1 y 2).
- Lagunas: 5 (L1 a L5; la L5 es a medias).

## Otros ficheros tocados

Sólo `informes/canal-sur-especificos/29-T12-preguntas.md` y este informe. El tema no se ha tocado.
