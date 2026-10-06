# Puesto 29 · Tema 12 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en sus volcados de
`fuentes/canal-sur/informatico/web/q-*.txt` (42 ficheros, descargados el 05-10-2026 con URL y fecha
en cabecera); no se descargó nada nuevo.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/12-bases-de-datos-y-lenguaje-sql.md`.

## Método

- Copiado del común: nada (según `29-T12-redaccion.md`).
- Copiado de RTVE sin cambios: comprobado sólo que es literal, por script contra
  `temas/tecnica-informatica/01-bases-de-datos-y-el-modelo-relacional.md` (sin negritas): las dos
  frases de entrada y las tablas Término/Qué es y Nombre corriente/Nombre formal, la clave primaria,
  la tabla de formas normales y su «Para qué sirve», el matiz DROP/DELETE/TRUNCATE, el bloque de
  cláusulas y su entrada, y la distinción WHERE/HAVING. Todo literal. No se ha re-verificado.
- Adaptado de RTVE (sí verificado): clave ajena, diseño lógico y físico, tabla de familias no
  relacionales, cuadro de familias y regla estructura/datos, frase del asterisco. Las cinco frases
  RTVE que se dicen literales lo son.
- Todo lo demás: cada una de las 218 negritas se buscó **en la fuente a la que el tema la atribuye**
  (script que dice en qué fichero aparece cada cita), y se leyó el contexto de cada página para las
  salvedades y lo dicho en redonda, con los nueve errores delante.
- Lentes (tema técnico sin norma): `refutar_prosa.py` 0 hallazgos; `indice.py` 54 epígrafes, el
  índice no cambia. No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.
  Literalidad tras las correcciones: 221 citas, 0 no halladas.

## Hallazgos y correcciones (todas aplicadas, cada una comprobada en su fuente)

| # | Error | Dónde | Qué pasaba | Corrección |
|---|---|---|---|---|
| 1 | 9 sin fuente | Siglas, ACM | «asociación profesional» y «en la que nació el modelo» sin apoyo (acm.org no se leyó) | La revista publicó en 1970 el artículo de Codd; se da el desarrollo que escribe Oracle |
| 2 | 9 | Siglas, Oracle AI Database | «nombre comercial de la versión 23» y «AI abrevia *artificial intelligence*»: ninguna página lo dice (la misma documentación menciona «Oracle 26ai») | Nombre con que Oracle titula la documentación publicada como versión 23; «AI» sin desarrollar |
| 3 | 6 salvedad | § 1, elementos del SGBD | Oracle dice **«Typically»**; el tema daba los tres elementos como fijos | «suele tener» |
| 4 | — forma | § 1, idem | La negrita pegaba el rótulo «Query language» a la frase | Cita sólo la frase |
| 5 | 6 | § 1, clave ajena (adaptado de RTVE) | «apunta a la clave primaria de otra tabla»: PostgreSQL admite también columnas únicas, y la otra tabla puede ser la misma | Añadida la cita de PostgreSQL y la clave autorreferenciada |
| 6 | 9 / 6 | § 3, funciones Core | «Ningún gestor la cumple entera»: la fuente habla de declarar el Core, no la norma entera, y «at the time of writing» | Corregido en el texto, la traducción y la Trazabilidad |
| 7 | 9 | § 3, tipos de datos | «El resto (… tipos geométricos o de direcciones de red) son propios de PostgreSQL»: la página dice que varios tipos son únicos o tienen varios formatos, con el ejemplo de los trazados geométricos | «Otros son propios…», con la cita |
| 8 | 6 | § 5, clave ajena de `orders` | La traducción quitaba «non-NULL» | Añadido; un nulo sí se admite |
| 9 | 1 cita cruzada | § 5, `TRUNCATE` | «Microsoft explica por qué [es más rápido]»: la página lo da como razón de que gaste menos registro de transacciones | Atribuido a esa ventaja |
| 10 | 6 | § 6, `MERGE` | «conforms to the SQL standard» sin la frase siguiente: `WITH`, `BY SOURCE`/`BY TARGET`, `DO NOTHING` y `RETURNING` son extensiones | Añadido |
| 11 | 6 | § 6, `COMMIT`/`ROLLBACK` | Faltaba que `COMMIT TRANSACTION` y `ROLLBACK TRANSACTION` son extensiones de PostgreSQL | Añadido |
| 12 | 3 recuento | § 6, modos de SQL Server | «tres modos»: la página da cuatro (el cuarto, con ámbito por lotes, sólo MARS) | «cuatro», con el cuarto explicado; sigla MARS presentada en castellano, como la da la página |
| 13 | 3 | § 7, orden lógico de Microsoft | `WITH CUBE`/`WITH ROLLUP` metido dentro de `GROUP BY`, con lo que `SELECT` no salía «paso 8» como dice la cita | Paso propio |
| 14 | 9 | § 8, agrupación con `LEFT JOIN` | Los departamentos sin empleados «saldrían con cero», pero con la fecha en el `WHERE` el `e.alta` nulo los elimina (comparación con nulo da nulo; el `WHERE` sólo deja lo verdadero) | Precisado: la condición de fecha ha de pasar al `ON` |
| 15 | 9 | Trazabilidad, Microsoft | «SQL Server 2025»: ninguna página leída identifica `ver17` con esa versión | Quitado; queda «versión `sql-server-ver17` de la documentación» |
| 16 | — | Trazabilidad, oficio | La tabla base de datos / sistema gestor (de RTVE, sin fuente) no figuraba en la lista de oficio | Añadida |

## Confirmado sin cambios (muestra)

Definiciones de Oracle (base de datos, SGBD, primera generación, Codd 1970, relación/tupla/tabla,
operaciones lógicas y físicas, ORDBMS, SQL declarativo y por conjuntos, sublenguaje, PSM, tareas,
portabilidad, SEQUEL, 1979, ANSI/ISO/IEC); las seis categorías de Oracle, sus listas DDL y DML,
`SELECT` como DML limitado, las cinco sentencias de control de transacciones y la confirmación
implícita del DDL; ISO/IEC 9075, SQL:2023, las ocho ediciones y la grafía, niveles de SQL-92, Core,
177/170, las once partes; las listas DDL/DML de Microsoft y «No figuran en esa página»; `LIMIT`,
`FETCH FIRST`, DB2, `TOP` con `OFFSET`/`FETCH`, paréntesis de `TOP`; `DROP TABLE` con `CASCADE`;
acciones `ON DELETE` y la salvedad de aplazamiento de `RESTRICT`; sintaxis de `ALTER TABLE`;
ejemplos de `GRANT`/`REVOKE` (`kinds` es una vista en la fuente, sin efecto en el tema); `PUBLIC`;
`INSERT` y la regla de la norma; ACID y modos de Microsoft; orden de proceso de PostgreSQL;
predicados, nulos, agregados, `HAVING`, combinaciones, subconsultas y conjuntos. La errata de Oracle
«Association of Computer Machinery» se mantiene citada tal cual (manda la fuente; aviso).

## Otros ficheros tocados

Ninguno, salvo el tema y este informe. Copia previa en el scratchpad (`t12v/antes.md`).
