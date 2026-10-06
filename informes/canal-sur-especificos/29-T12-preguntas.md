# Puesto 29 · Tema 12 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026. Quince preguntas tipo test de cuatro opciones, contestadas **sólo con el tema**
(`temas/canal-sur-especificos/29-operador-a-informatico/12-bases-de-datos-y-lenguaje-sql.md`).
(T) = teoría; (AP) = aplicación práctica. Resultado: entera / a medias / no.

1. (T, bases de datos) El modelo relacional lo formuló: a) IBM con SEQUEL en 1979; b) E. F. Codd en
   1970; c) ANSI en SQL-92; d) Oracle en 1979. → **b**. § 1, «El modelo relacional…», y § 2, «De
   dónde viene». **Entera.**
2. (T, lenguaje) SEQUEL, del que procede SQL, lo desarrolló: a) Relational Software; b) Microsoft;
   c) IBM; d) la ACM. → **c**. § 2, «De dónde viene». **Entera.**
3. (T, estándar) Según la documentación de PostgreSQL, de las funciones obligatorias del Core:
   a) son 170 y PostgreSQL cumple 177; b) son 177 y PostgreSQL cumple al menos 170; c) son opcionales;
   d) sólo existen en SQL-92. → **b**. § 3, «Niveles de conformidad y funciones Core». **Entera.**
4. (T, estándar) Los bloques procedimentales (bucles, condicionales) están en la parte de ISO/IEC 9075:
   a) 2, Foundation; b) 4, SQL/PSM; c) 11, SQL/Schemata; d) 14, SQL/XML. → **b**. § 2 y § 3.
   **Entera.**
5. (AP, DDL/TCL) En Oracle se ejecuta `DELETE FROM t;`, después `CREATE TABLE u (a integer);` y
   después `ROLLBACK;`. Las filas de `t`: a) vuelven; b) siguen borradas, porque el DDL confirmó la
   transacción; c) vuelven y `u` desaparece; d) da error el `ROLLBACK`. → **b**. § 4, «Cómo clasifica
   Oracle», y § 6, final de «Las transacciones». **Entera.**
6. (AP, DDL) Clave ajena con `ON DELETE SET NULL`; se borra la fila referenciada: a) error; b) se borran
   las filas que la referencian; c) la columna de clave ajena de esas filas pasa a nulo; d) toma su
   valor por defecto. → **c**. § 5, «Qué pasa al borrar la fila referenciada». **Entera.**
7. (T, DML) En `INSERT` sin lista de columnas, se entienden: a) sólo las de la clave primaria; b) todas,
   en el orden en que se declararon; c) todas, en orden alfabético; d) ninguna: es error en todos los
   gestores. → **b**. § 6, «INSERT». **Entera.**
8. (AP, DQL) `nombre LIKE '_a%'` selecciona los nombres: a) que empiezan por «a»; b) cuya segunda letra
   es «a»; c) que contienen «_a»; d) que acaban en «a». → **b**. § 7, `WHERE`, cuadro de predicados.
   **Entera.**
9. (AP, DQL) Sobre una tabla vacía, `SELECT COUNT(*), SUM(salario) FROM empleados;` devuelve: a) 0 y 0;
   b) nulo y nulo; c) 0 y nulo; d) error. → **c**. § 7, «Las funciones de agregación». **Entera.**
10. (AP, DQL) `SELECT id_dep, nombre, COUNT(*) FROM empleados GROUP BY id_dep;` (clave primaria
    `id_emp`): a) correcta; b) error, porque `nombre` no está agrupado ni en un agregado; c) devuelve
    una fila por empleado; d) error por falta de `HAVING`. → **b**. § 7, «`GROUP BY` y `HAVING`».
    **Entera.**
11. (T, DQL) Para que `SELECT … UNION SELECT …` sea válida, las dos consultas deben: a) leer la misma
    tabla; b) devolver el mismo número de columnas, de tipos compatibles; c) llevar `ORDER BY`;
    d) tener el mismo número de filas. → **b**. El tema explica qué devuelven `UNION`, `INTERSECT`
    y `EXCEPT` y los repetidos, pero no la condición de compatibilidad. **No.**
12. (AP, DQL) `WHERE salario > ALL (SELECT salario FROM empleados WHERE id_dep = 3)` devuelve los
    empleados que ganan: a) más que alguno del departamento 3; b) más que todos los del
    departamento 3; c) lo mismo que alguno; d) es error de sintaxis. → **b**. El tema no trata
    `ANY`/`SOME`/`ALL` (sólo `IN` y `EXISTS`). **No.**
13. (T, DDL) La diferencia entre `char(n)` y `varchar(n)`: a) ninguna; b) `char` es de longitud fija y
    `varchar` de longitud variable; c) `varchar` sólo admite números; d) `char` no es de la norma.
    → **b**. El tema enumera ambos tipos entre los de la norma, pero no dice qué es cada uno.
    **No.**
14. (T, estándar/TCL) La sentencia de la norma para iniciar una transacción explícita es: a) `BEGIN
    TRANSACTION`; b) `START TRANSACTION`; c) `OPEN TRANSACTION`; d) `SET TRANSACTION`. → **b**. El tema
    sólo da `BEGIN` (PostgreSQL) y `BEGIN TRANSACTION` (SQL Server); con él se marcaría a). **No.**
15. (T, DQL) `NATURAL JOIN` combina dos tablas: a) por todas las columnas que tienen el mismo nombre en
    las dos; b) por la clave primaria; c) sin condición, como `CROSS JOIN`; d) sólo por las columnas
    indicadas en `USING`. → **a**. El tema nombra `NATURAL` como una de las tres formas de condición,
    junto a `ON` y `USING`, pero no dice qué hace. **A medias.**

Recuento: 10 enteras, 1 a medias, 4 no.
