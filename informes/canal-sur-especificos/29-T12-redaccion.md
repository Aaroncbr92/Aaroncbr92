# Puesto 29 · Tema 12 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real,
como en la investigación y en los temas 5 a 10). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/12-bases-de-datos-y-lenguaje-sql.md`.
Material: `29-investigacion-C-datos-redes-seguridad.md` (§ Tema 12). `AGRUPACION.tsv`: tema 12
«nuevo». Fila de `informes/canal-sur-reuso/informatica.tsv`: RTVE `tecnica-informatica/01`, 35 %,
«actualizar: no».

## Avance

- Ficha, siglas, enunciado, «qué se puede preguntar» y epígrafe 1 (base de datos y SGBD, primera generación, modelo relacional y terminología, claves, lógico y físico, normalización, no relacionales) guardados. Literalidad: 22 citas, todas halladas.
- Epígrafes 2 (SQL como lenguaje de interrogación: declarativo, de conjuntos, sublenguaje, tareas, historia) y 3 (ANSI/ISO, ISO/IEC 9075, ediciones, niveles y Core, partes, dialectos) guardados. Literalidad: 85 citas acumuladas, todas halladas.
- Epígrafes 4 (clasificación didáctica frente a Oracle y SQL Server) y 5 (DDL: CREATE TABLE, restricciones, ON DELETE, ALTER, DROP/TRUNCATE/DELETE, vistas e índices, GRANT/REVOKE) guardados. Primera pasada: 4 citas de listas fallaban por los guiones de lista de la fuente; partidas en citas sueltas. Literalidad: 137, todas halladas.
- Epígrafe 6 (DML: INSERT, UPDATE, DELETE, MERGE; transacciones y ACID) guardado. Literalidad: 170, todas halladas.
- Epígrafe 7 (DQL: SELECT, orden de escritura y de proceso, WHERE y predicados, nulos, agregados, GROUP BY/HAVING, ORDER BY y limitación, JOIN, subconsultas, operaciones de conjuntos) guardado. Literalidad: 218, todas halladas.
- Epígrafe 8 (aplicación práctica: errores, elección de sentencia, consulta con agrupación), «Lo que este tema no da» y «Trazabilidad» guardados. Índice generado con `indice.py` (54 epígrafes). Literalidad final: 218 citas en negrita, todas halladas. Extensión: 11.716 palabras.

## Fuentes leídas y fecha

Todas el 05-10-2026, descargadas como texto con URL y fecha en cabecera en
`fuentes/canal-sur/informatico/web/` (nuevas, prefijo `q-`, 42 ficheros):

- PostgreSQL 18 (postgresql.org/docs/current/…): `q-pgconf` (Appendix D), `q-pgconcepts`,
  `q-pgintro`, `q-pgjoin`, `q-pgagg`, `q-pgtrans` (tutorial); `q-pgselect`, `q-pginsert`,
  `q-pgupdate`, `q-pgdelete`, `q-pgmerge`, `q-pgcreatetable`, `q-pgaltertable`, `q-pgdroptable`,
  `q-pgtrunc`, `q-pgcreateview`, `q-pgcreateindex`, `q-pggrant`, `q-pgrevoke`, `q-pgcommit`,
  `q-pgrollback`, `q-pgsavepoint` (referencia); `q-pgconstr`, `q-pgdatatype`, `q-pgnull`,
  `q-pglogical`, `q-pglike`, `q-pgaggfunc`, `q-pgsubq`, `q-pgdatetime`.
- Oracle AI Database 23: `q-orastd`, `q-orahist`, `q-oratypes` (SQL Language Reference),
  `q-oradbconcepts` (Concepts, cap. 1).
- Microsoft Learn en castellano (SQL Server, `sql-server-ver17`): `q-mstsql`, `q-msselect`,
  `q-mstop`, `q-mstrunc`, `q-msupdate`, `q-msgrant`, `q-mstran`, `q-mslock`.

Las cinco citas de Oracle y PostgreSQL que traía la investigación (§ 12.1 y 12.2) se releyeron en
sus páginas: coinciden. Descargas fallidas o sin uso, borradas: página «About ACM» de acm.org y la
de *Communications of the ACM* (bloqueo de Cloudflare), compatibilidad de MySQL 8.4 (sólo menú), y
cuatro páginas de PostgreSQL leídas y no citadas.

Comprobación de literalidad por script (`scratchpad/t12check.py`, el de T10 con las fuentes `q-*`;
normaliza espacios, comillas, apóstrofos y acentos graves): 218 citas, 0 no halladas. En la primera
pasada fallaron 4 citas que unían elementos de lista de Oracle; se partieron en citas sueltas.
`refutar_prosa.py`: 8 siglas sin presentar (AI, BASIC, XML, y palabras clave de SQL fuera de código:
BULK, HAVING, MERGE, SELECT, WHERE); presentadas las tres primeras en las siglas y puestas las demás
en formato de código; 0 hallazgos. Tema técnico sin norma: no proceden `negritas.py`,
`refutar_exactitud.py` ni `refutar_modo.py`. Ficha escrita a mano (el tema no está en `portadas.tsv`).

## Qué se hizo

Ocho epígrafes: 1 bases de datos (lo que el enunciado presupone con «Bases de datos»: base de datos y
SGBD, primera generación, modelo relacional, claves, lógico y físico, normalización, no relacionales);
2 lenguaje de interrogación (SQL declarativo y de conjuntos, sublenguaje, tareas, portabilidad,
historia); 3 estándar ANSI SQL (ANSI/ISO/IEC, ISO/IEC 9075, ocho ediciones, niveles de SQL-92 y
Core, once partes, norma frente a dialectos con ejemplos leídos); 4 familias de sentencias (cuadro
didáctico de cinco familias frente a Oracle y SQL Server, confirmación implícita del DDL en Oracle);
5 DDL (con DCL al final); 6 DML (con TCL y ACID al final); 7 DQL (`SELECT` completo); 8 aplicación
práctica.

Decisiones:

- DQL: el enunciado lo separa; la investigación no pudo confirmar que la norma use los rótulos. Se
  presenta como clasificación didáctica, con la frase de Oracle que lo justifica («limited form of
  DML») y el cuadro de cómo clasifica cada fabricante. Consejo para el test, como oficio.
- DCL y TCL no están en el enunciado; se tratan dentro de DDL y DML porque Oracle pone `GRANT`/`REVOKE`
  en DDL y describe el control de transacciones como el que gestiona los cambios del DML.
- «Estándar ANSI SQL»: se explica que ANSI e ISO/IEC publican una norma técnicamente idéntica, con el
  nombre formal ISO/IEC 9075; no se dan fechas de 1986/1987 (no confirmadas).
- ACM: Oracle escribe «Association of Computer Machinery»; el desarrollo oficial no se pudo leer
  (acm.org bloqueado). Se cita a Oracle tal cual y en las siglas no se desarrolla; se declara en «Lo
  que este tema no da».
- Fecha de lectura (05-10-2026) posterior a la del encargo (24-09-2026), como en los temas 5 a 10.
  No se ha comprobado si alguna página cambió entre ambas fechas; las de Microsoft leídas marcan su
  última actualización antes del 24-09-2026 (por ejemplo, «Transacciones», 21-07-2026; «Transact-SQL
  declaraciones», 21-09-2026).

Salvedad de fuente (manda la fuente; aviso): Oracle llama a la ACM «Association of Computer
Machinery» en «History of SQL»; se cita literal.

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata bases de datos ni SQL.

## Copiado de RTVE sin cambios

El tema de RTVE `tecnica-informatica/01` está marcado «actualizar: no». Pasajes técnicos copiados
literal, sin cambiar una palabra; único cambio, de formato: quitada la negrita, porque RTVE no citaba
fuente y en este tema negrita es cita. Comprobado por script que cada pasaje está en RTVE y en el tema.
Se declaran como oficio en la Trazabilidad del tema.

| Pasaje en RTVE (`tecnica-informatica/01`) | Dónde va en el tema |
|---|---|
| § 1: «Los dos términos se confunden en la conversación y el examen los separa:» y la tabla «Término / Qué es» entera (dos filas) | § 1, «Base de datos y sistema gestor» |
| § 3: «El modelo relacional organiza los datos en tablas, y cada palabra tiene nombre formal y nombre corriente, que el examen mezcla:» y la tabla «Nombre corriente / Nombre formal / Qué es» entera (tres filas) | § 1, «El modelo relacional y su terminología» |
| § 3: «Clave primaria: el atributo o conjunto de atributos que identifica sin ambigüedad cada fila. No puede repetirse ni quedar vacía.» | § 1, «Las claves» |
| § 4: la tabla «Forma normal / Qué exige» entera (tres filas) y «Para qué sirve, en una línea: evitar que el mismo dato esté escrito en dos sitios, porque cuando está en dos sitios, tarde o temprano dice dos cosas distintas.» | § 1, «La normalización» |
| § 5: «El matiz que a veces despista: `DROP` y `DELETE` parecen lo mismo y no lo son. `DROP` elimina la tabla entera, con su estructura, y es DDL; `DELETE` borra filas y deja la tabla vacía en pie, y es DML. `TRUNCATE` vacía la tabla sin borrar su estructura y se clasifica como DDL, porque no opera fila a fila.» | § 5, «DROP, DELETE y TRUNCATE» |
| § 6: «La estructura completa de una consulta, por orden, que es lo que conviene llevar memorizado:» y el bloque de código de seis líneas | § 7, «Las cláusulas, en el orden en que se escriben» |
| § 6: «La distinción entre `WHERE` y `HAVING` es la que más se pregunta en esta familia: `WHERE` filtra filas antes de agrupar y `HAVING` filtra grupos después.» | § 7, «`GROUP BY` y `HAVING`» |

Adaptado de RTVE (no entra en «sin cambios»; lo debe verificar la fase 3):

- § 3 RTVE, clave ajena: «Clave ajena: el atributo que apunta a la clave primaria de otra tabla. Es
  lo que crea la relación.»: se quitó «, y de ahí el nombre del modelo», porque «relacional» viene de
  relación (tabla), como dicen Oracle y PostgreSQL, no del vínculo entre tablas.
- § 4 RTVE, diseño lógico y físico: frase de entrada cambiada («El diseño en dos pasos sigue esa misma
  línea:»); el resto, literal.
- § 2 RTVE, tabla de familias: quitada la fila «Columnar / Por columnas, para consultas analíticas /
  Cassandra» (no confirmada, y la descripción no casa con el ejemplo); en consecuencia «Las cuatro
  últimas familias» pasa a «Las tres últimas familias».
- § 5 RTVE, cuadro de sublenguajes: añadida la fila DQL, `SELECT` pasado del DML al DQL y `MERGE`
  añadido al DML; filas DDL, DCL y TCL literales. La regla «si la sentencia toca la ESTRUCTURA, es
  DDL; si toca los DATOS, es DML. `CREATE` crea una tabla; `DELETE` borra filas de una tabla que ya
  existe.» es literal; cambia la frase que la introduce.
- § 6 RTVE: «El asterisco significa «todas las columnas»» es literal, pero va seguido de una cita de
  PostgreSQL en lugar de la frase de RTVE sobre `COUNT`.

Quitado por propio de RTVE: la entradilla de las «siete preguntas» y su reparto, todos los párrafos
«La pregunta N… Ésa es la respuesta oficial», el razonamiento sobre Apache TomCat y H2 como opciones
de examen, la frase sobre las opciones falsas de la pregunta 24 (`SUM(*)`, `MAX(*)`, `ROWS()`), la
tabla de respuestas oficiales (§ 7), el aviso de estudio y la Trazabilidad de RTVE («Este tema no
cita ninguna fuente de forma literal»), que aquí ya no vale. La tabla de funciones de agregación de
RTVE se sustituyó por la de PostgreSQL, con fuente y con `COUNT(expresión)`.

## Otros ficheros tocados

- `fuentes/canal-sur/informatico/web/q-*.txt` (42 volcados nuevos). Ningún fichero existente
  modificado.
- Ningún otro tema ni informe.

## Diez preguntas tipo test (comprobación de cobertura)

Repartidas por las rúbricas del enunciado; (AP) = aplicación práctica. Todas se contestan enteras
con el tema; no ha hecho falta ampliarlo.

1. (Bases de datos) En el modelo relacional, una tupla es: a) una columna de la tabla; b) una fila de
   la tabla; c) la tabla entera; d) la clave primaria. → **b** (relación = tabla, atributo = columna).
   § 1, «El modelo relacional y su terminología». Entera.
2. (Lenguaje de interrogación) SQL es un lenguaje: a) procedimental, que describe cómo obtener los
   datos fila a fila; b) declarativo y basado en conjuntos, que describe qué resultado se quiere; c) de
   propósito general, como C; d) exclusivo de Oracle. → **b**. § 2, «Qué es SQL» y «Para qué sirve».
   Entera.
3. (Estándar ANSI) El nombre formal de la norma de SQL y su edición vigente son: a) ANSI X3.135 y
   SQL-92; b) ISO/IEC 9075 y SQL:2023; c) ISO/IEC 27001 y SQL:2016; d) ISO/IEC 9075 y SQL:2016. → **b**.
   § 3, «Quién lo publica y cómo se llama». Entera.
4. (Estándar ANSI) Desde SQL:1999, la conformidad con la norma se organiza en: a) tres niveles, Entry,
   Intermediate y Full; b) un conjunto de funciones «Core» obligatorias y el resto opcionales; c) cinco
   familias de sentencias; d) once niveles, uno por parte. → **b** (los tres niveles son de SQL-92).
   § 3, «Niveles de conformidad y funciones Core». Entera.
5. (Estándar ANSI, AP) Para devolver sólo las 10 primeras filas de una consulta de forma conforme a la
   norma se usa: a) `LIMIT 10`; b) `TOP (10)`; c) `FETCH FIRST 10 ROWS ONLY`; d) `ROWNUM <= 10`. → **c**
   (`LIMIT` es de PostgreSQL y MySQL; `TOP`, de SQL Server). § 3, «La norma y los dialectos», y § 7,
   «`ORDER BY` y la limitación de filas». Entera.
6. (DDL) Sobre `TRUNCATE`, es correcto: a) es DML y admite `WHERE`; b) elimina la tabla y su
   estructura; c) es DDL, quita todas las filas y deja la tabla, y es más rápido que `DELETE` sin
   `WHERE`; d) sólo existe en SQL Server. → **c**. § 4, cuadro comparado; § 5, «DROP, DELETE y
   TRUNCATE». Entera.
7. (DDL, AP) La tabla `pedidos` tiene una clave ajena hacia `clientes` declarada con
   `ON DELETE CASCADE`. Al borrar un cliente con pedidos: a) se produce un error; b) se borran también
   sus pedidos; c) la clave ajena de sus pedidos queda nula; d) no pasa nada en `pedidos`. → **b** (a
   sería `RESTRICT` o `NO ACTION`; c, `SET NULL`). § 5, «Qué pasa al borrar la fila referenciada».
   Entera.
8. (DML) La sentencia `UPDATE empleados SET salario = 2000;`: a) da error por faltar el `WHERE`; b)
   cambia el salario de todas las filas; c) sólo cambia la primera fila; d) es DDL. → **b**. § 6,
   «UPDATE», y § 8. Entera.
9. (DQL) ¿Cuál es correcta? a) `WHERE` filtra grupos y `HAVING` filtra filas; b) `WHERE` puede
   contener `MAX()`; c) `WHERE` filtra filas antes de agrupar y `HAVING` filtra grupos después; d)
   `HAVING` se escribe antes de `GROUP BY`. → **c**. § 7, «Las cláusulas…» y «`GROUP BY` y `HAVING`».
   Entera.
10. (DQL, AP) La tabla `t` tiene 10 filas y su columna `c` es nula en 3 de ellas. `SELECT COUNT(*),
    COUNT(c) FROM t;` devuelve: a) 10 y 10; b) 7 y 7; c) 10 y 7; d) 10 y nulo. → **c** (`COUNT(*)`
    cuenta filas; `COUNT(c)`, filas con `c` no nulo). § 7, «Las funciones de agregación». Entera.
