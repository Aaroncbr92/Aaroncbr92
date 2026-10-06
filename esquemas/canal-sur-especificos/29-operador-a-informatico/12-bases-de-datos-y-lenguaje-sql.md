# Tema 12 del específico de Operador/a Informático · Bases de datos y lenguaje SQL

**Siglas**: RTVA, CSRTV, BOJA; SGBD/DBMS, RDBMS; SQL; DDL, DML, DQL, DCL, TCL; ANSI, ISO, IEC; ACM; ACID; T-SQL; PL/SQL; XML.

Esqueleto para repasar, no resumen: el detalle y las citas literales están en el tema.

<!-- indice -->
1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · No da
<!-- /indice -->

## 1. Bases de datos
- Oracle: BD = colección organizada de información tratada como unidad. SGBD = software que controla almacenamiento, organización y recuperación; «Typically» núcleo, diccionario de datos (metadatos), lenguaje de consulta.
- Oracle, 1.ª generación: jerárquico (árbol, uno a muchos); red (muchos a muchos); rígidos, sin DDL.
- Oracle: Codd 1970, teoría de conjuntos. Relación = conjunto de tuplas; tupla = conjunto no ordenado de valores de atributos; tabla = filas (tuplas) y columnas (atributos), mismas columnas en todas las filas. PostgreSQL: relación = término matemático de tabla; columna de un tipo; SQL no garantiza orden de filas.
- PostgreSQL, PK: única y no nula; máximo una por tabla (UNIQUE, varias). FK: valores coinciden con fila de otra tabla (integridad referencial); referencia PK, UNIQUE o índice único no parcial; puede autorreferenciarse.
- Oracle: independencia entre almacenamiento físico y estructuras lógicas; la aplicación dice qué, el gestor cómo. Oficio: diseño lógico y físico (tipos, índices, particiones).
- Normalización (oficio, sin fuente): 1FN sin valores múltiples en celda; 2FN todo campo depende de la PK entera; 3FN ningún campo depende de otro no clave.
- PostgreSQL: otras (ficheros Unix jerárquica; orientada a objetos). Oracle: objeto-relacional = tipos definidos por usuario, herencia, polimorfismo.
- Oficio: documental (MongoDB), clave-valor (Redis), grafos (Neo4j).

## 2. Lenguaje de interrogación: SQL
- «Lenguaje de interrogación» = lenguaje de consulta del SGBD; en relacionales, SQL.
- Oracle: SQL = lenguaje declarativo, basado en conjuntos, interfaz con un RDBMS. Declarativo: qué, no cómo (C, procedimental); el optimizador elige el acceso. Conjuntos: no filas una a una. Sublenguaje de datos.
- Oracle: control de flujo no era SQL; hoy ISO/IEC 9075-4 SQL/PSM; PL/SQL similar. Microsoft: instrucción SQL = unidad atómica, éxito o fallo completo.
- Oracle, tareas: consultar; insertar, actualizar, borrar filas; crear, sustituir, modificar, eliminar objetos; controlar acceso; garantizar coherencia e integridad.
- Oracle: todos los grandes gestores relacionales admiten SQL; portables con pocos cambios.
- Oracle, historia: Codd, junio 1970, Communications of the ACM (Oracle: «Association of Computer Machinery»); IBM, SEQUEL (Structured English Query Language) → SQL («sequel»); 1979, Relational Software, Inc. (hoy Oracle), primera implantación comercial.

## 3. Estándar ANSI SQL
- Oracle: ANSI e ISO (asociada a IEC) aceptan SQL; publicación simultánea = normas técnicamente idénticas.
- PostgreSQL: ISO/IEC 9075 «Database Language SQL»; última revisión 2023 = ISO/IEC 9075:2023 = SQL:2023. Anteriores: SQL:2016, 2011, 2008, 2006, 2003, 1999, SQL-92 (ocho ediciones).
- SQL-92: niveles Entry, Intermediate, Full (la mayoría, Entry). Desde SQL:1999: funciones sueltas; «Core» obligatorio, resto opcional. PostgreSQL: 177 obligatorias del Core, cumple al menos 170; ninguno declaraba Core de SQL:2023 entero.
- Partes (PostgreSQL; once, con huecos): 1 Framework; 2 Foundation; 3 CLI (Call Level Interface); 4 PSM (Persistent Stored Modules); 9 MED (Management of External Data); 10 OLB (Object Language Bindings); 11 Schemata (Information and Definition Schemas); 13 JRT (Routines and Types using the Java Language); 14 XML; 15 MDA (Multi-dimensional arrays); 16 PGQ (Property Graph Queries).
- Oracle SQL implementa la norma y la amplía; Microsoft, T-SQL; PostgreSQL: extensiones.
- Limitar filas: norma SQL:2008 `OFFSET … FETCH FIRST n ROWS ONLY` (también IBM DB2); `LIMIT`/`OFFSET` PostgreSQL y MySQL; SQL Server `TOP` y `OFFSET`/`FETCH` en ORDER BY.
- TRUNCATE: SQL:2008 `TRUNCATE TABLE`; PostgreSQL admite sin TABLE. DROP: norma, una tabla por comando; PostgreSQL varias, `IF EXISTS` extensión. `MERGE` norma; PostgreSQL `INSERT … ON CONFLICT`. `CREATE OR REPLACE VIEW` extensión PostgreSQL. PL/SQL «similar to PSM».
- Tipos de la norma: bigint, bit, bit varying, boolean, char, character varying, character, varchar, date, double precision, integer, interval, numeric, decimal, real, smallint, time y timestamp (con o sin zona), xml. Propios: geometric paths.

## 4. Familias de sentencias
- Enunciado: DDL, DML, DQL; oficio añade DCL, TCL. No confirmado que ISO/IEC 9075 use los rótulos.
- Oficio: DDL=CREATE, ALTER, DROP, TRUNCATE; DML=INSERT, UPDATE, DELETE, MERGE; DQL=SELECT; DCL=GRANT, REVOKE; TCL=COMMIT, ROLLBACK, SAVEPOINT.
- Oracle, seis categorías: DDL, DML, control de transacciones, de sesión, del sistema, SQL incrustado. Sin DQL ni DCL.
- Oracle DML: CALL, DELETE, EXPLAIN PLAN, INSERT, LOCK TABLE, MERGE, SELECT, UPDATE; SELECT = «forma limitada de DML». Oracle DDL incluye conceder y revocar privilegios y roles.
- Oracle, transacciones: COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION, SET CONSTRAINT. Confirma implícitamente antes y después de cada DDL; DML no. Deducción del tema: CREATE/TRUNCATE no se deshacen con ROLLBACK, DELETE sí (comportamiento de Oracle, no de la norma).
- Microsoft: DDL (ALTER, CREATE, DROP, RENAME, TRUNCATE TABLE); DML (BULK INSERT, DELETE, INSERT, SELECT, UPDATE, MERGE); permisos aparte.
- SELECT = DQL (oficio) / DML (Oracle, SQL Server); GRANT/REVOKE = DCL / DDL (Oracle) / permisos (Microsoft); TRUNCATE = DDL en ambos. Test: con DQL entre opciones, SELECT es DQL; si no, DML.

## 5. DDL
- PostgreSQL CREATE TABLE: tabla nueva y vacía en la BD actual, propiedad de quien la crea.
- Tipos: char(n) fija; varchar(n) variable; smallint/integer/bigint enteros con signo de 2/4/8 bytes; numeric(p,s)/decimal exacto; real 4 bytes y double precision 8 bytes; boolean; date (año, mes, día); time; timestamp (fecha y hora); interval.
- Restricción violada = error. NOT NULL; UNIQUE único entre todas las filas; PRIMARY KEY único y no nulo, una por tabla; FOREIGN KEY/REFERENCES integridad referencial; CHECK expresión lógica. DEFAULT no es restricción.
- ON DELETE: NO ACTION (defecto; normalmente error); RESTRICT (impide borrar la referenciada); CASCADE (borra las que referencian); SET NULL / SET DEFAULT. CASCADE si es componente que no existe sola; RESTRICT o NO ACTION si independientes.
- ALTER TABLE cambia la definición: ADD COLUMN, ALTER COLUMN … TYPE, RENAME COLUMN … TO, DROP COLUMN (sintaxis PostgreSQL).
- DROP TABLE: quita tabla con índices, reglas, disparadores, restricciones; con FK o vista dependiente, CASCADE.
- TRUNCATE: quita todas las filas, como DELETE sin WHERE, más rápido (no recorre). Microsoft: DELETE registra cada fila; TRUNCATE desasigna páginas y registra sólo eso. DELETE sin WHERE: tabla válida pero vacía.
- DROP=DDL, tabla entera, sin WHERE; TRUNCATE=DDL, filas, sin WHERE; DELETE=DML, filas con WHERE (todas sin él).
- CREATE VIEW: consulta con nombre, no materializada, se ejecuta en cada uso. CREATE INDEX: mejora rendimiento (mal usado, empeora); UNIQUE impide duplicados con error.
- GRANT (Microsoft): `GRANT permiso ON objeto TO usuario, login o grupo`. REVOKE (PostgreSQL): retira privilegios concedidos. `WITH GRANT OPTION`: reconceder. Quitar SELECT a PUBLIC no implica que todos lo pierdan (privilegios directos, roles y PUBLIC se suman).

## 6. DML
- INSERT (PostgreSQL): `DEFAULT VALUES`, `VALUES` (una o varias listas) o `query`. Columna no nombrada = defecto o nulo. Sin lista de columnas = todas en orden de declaración; omitirla sin llenar todas lo prohíbe la norma, PostgreSQL lo admite.
- UPDATE: cambia las columnas de SET en filas que cumplen la condición; el resto conserva valor. Sin WHERE, todas (Microsoft). DELETE: filas que cumplen WHERE, sin él todas; con FK aplica ON DELETE.
- MERGE: una sentencia que inserta, actualiza o borra según condición; aplica la primera WHEN que se cumpla; conforme a la norma; extensiones PostgreSQL: WHEN NOT MATCHED BY SOURCE, DO NOTHING, RETURNING.
- Transacción (Microsoft): unidad única de trabajo; éxito = permanente; error = se revierte todo. ACID: atomicidad (todo o nada); coherencia (estado coherente al acabar); aislamiento (simultáneas aisladas); durabilidad (permanente, aun con error del sistema).
- Abrir: `START TRANSACTION` (norma); `BEGIN` extensión PostgreSQL equivalente; `BEGIN TRANSACTION` SQL Server. En la norma cualquier sentencia abre bloque implícito.
- COMMIT: confirma, visible y duradero; ROLLBACK: deshace todo; conformes a la norma (`… TRANSACTION` extensión PostgreSQL). SAVEPOINT: marca; ROLLBACK TO descarta lo posterior, conserva lo anterior.
- PostgreSQL: sin BEGIN, cada sentencia lleva BEGIN y COMMIT implícitos. SQL Server: confirmación automática (cada instrucción una transacción); explícitas (BEGIN TRANSACTION … COMMIT o ROLLBACK); implícitas (nueva al completarse la anterior); cuarta, ámbito por lotes (MARS).

## 7. DQL: SELECT
- PostgreSQL: SELECT recupera filas de cero o más tablas; privilegio SELECT sobre cada columna. `*` todas; `AS` nombre de salida; `DISTINCT` quita repetidos; `ALL` (defecto) los deja.
- Escritura: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, OFFSET … FETCH.
- Orden lógico (Microsoft): FROM, ON, JOIN, WHERE, GROUP BY, WITH CUBE/ROLLUP, HAVING, SELECT (paso 8), DISTINCT, ORDER BY, TOP. Alias vale en ORDER BY, no en WHERE. PostgreSQL: WHERE elimina filas; HAVING, grupos.
- Operadores: `< > <= >= =`; distinto `<>` (norma), `!=` alias; AND, OR, NOT. BETWEEN extremos incluidos. IN lista o subconsulta. LIKE: `_` un carácter, `%` cero o más; cadena entera (`'%Ruiz%'`). IS [NOT] NULL. EXISTS cierto si hay al menos una fila.
- Tres valores: true, false, null («unknown»). `7 = NULL` y `7 <> NULL` dan nulo; usar IS NULL.
- Agregados: COUNT(*) filas; COUNT(expr) no nulos; SUM, AVG, MAX, MIN sobre no nulos. Sin filas, nulo salvo COUNT (SUM de nada = nulo, no cero).
- WHERE filtra filas antes de agrupar, sin agregados; HAVING filtra grupos después. Condición sin agregado, mejor en WHERE. GROUP BY: una fila por grupo.
- Columnas del SELECT: agrupadas, en agregado o dependientes funcionalmente (PK en el GROUP BY); PostgreSQL sólo PK, la norma más casos. `GROUP BY id_emp` permite `nombre`; `GROUP BY id_dep`, no.
- ORDER BY: sin él, orden más rápido; ASC por defecto, DESC. Limitar: `FETCH FIRST` (norma), `LIMIT` (PostgreSQL, MySQL), `TOP (n)` (SQL Server; paréntesis recomendados).
- JOIN: INNER (sólo casan); LEFT (+ izquierdas sin pareja, nulos a la derecha); RIGHT (simétrico); FULL (ambas); CROSS = INNER JOIN ON (TRUE). INNER y OUTER opcionales; exigen exactamente una de ON, USING o NATURAL.
- USING (a, b) = ON igualando esas columnas; cada par sale una vez. NATURAL = USING con todas las homónimas; sin comunes = ON TRUE. Con las tablas del tema, NATURAL empareja también por `nombre`: no vale; `USING (id_dep)` sí.
- ANY/SOME: cierto si alguna fila lo da; falso si ninguna; `IN` = `= ANY`. ALL: cierto si todas; falso si alguna falsa. NOT IN: cierto si sólo hay distintas; falso si alguna igual; = `<> ALL`. Subconsulta vacía: ANY falso; ALL y NOT IN ciertos.
- Nulos: NOT IN da nulo si el izquierdo es nulo o, sin iguales, alguna derecha es nula; ANY da nulo (no falso) sin éxitos y con algún nulo; ALL da nulo si ninguna falsa y alguna nula. Con NOT IN, ningún departamento sin empleados si algún `id_dep` es nulo.
- Conjuntos: UNION (uno o ambos); INTERSECT (ambos); EXCEPT (primero y no segundo). Sin ALL quitan repetidos; UNION ALL más rápido. Compatibles: mismo número de columnas y tipos compatibles.

## 8. Aplicación práctica
- `WHERE salario = MAX(salario)`: error; subconsulta. `WHERE id_dep = NULL`: ninguna fila; `IS NULL`. `WHERE COUNT(*) > 5`: error; `HAVING`. Alias en WHERE: error; vale en ORDER BY.
- `UPDATE … SET salario = 2000;` sin WHERE: cambia a todos. `DELETE` de departamento con empleados y `ON DELETE RESTRICT`: error; CASCADE borra también los empleados.
- Escoger: añadir columna `ALTER TABLE … ADD COLUMN` (DDL); vaciar `TRUNCATE TABLE` o `DELETE` (DDL o DML); eliminar `DROP TABLE`; subir salario `UPDATE … WHERE` (DML); permiso `GRANT SELECT … TO` (DCL); retirar `REVOKE SELECT … FROM`; deshacer `ROLLBACK` (TCL); contar `SELECT COUNT(*)` (DQL).
- Agrupación: fecha en WHERE; «más de cinco» en HAVING; AVG; ORDER BY media DESC. LEFT JOIN desde departamentos: COUNT(e.id_emp)=0 (COUNT(*) contaría 1); fecha en el ON, no en WHERE (e.alta nulo la elimina).

## Lo que el tema no da
- ISO/IEC 9075 (de pago): sin fechas de primera norma ANSI/ISO, ni edición vigente por parte, ni si usa rótulos DDL/DML/DQL. Nombre completo de la ACM (página bloqueada).
- Administración de un gestor y lenguajes procedimentales; copias de seguridad, tema 3. No relacionales (sólo familias); normalización más allá de 3FN, entidad-relación; ventana, WITH RECURSIVE, funciones de fecha y texto. Inyección de SQL y cifrado: tema 14. Gestores de RTVA/CSRTV: no consta.
