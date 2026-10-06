# Tema 12 del específico de Operador/a Informático · Bases de datos y lenguaje SQL

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 12 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. La norma técnica del lenguaje, ISO/IEC 9075, es de pago y no se ha leído: se cita a través de la documentación oficial de tres gestores que la describen (PostgreSQL 18, Oracle AI Database 23 y SQL Server en Microsoft Learn, en castellano) |
| Redacción que se estudia | SQL:2023 (ISO/IEC 9075:2023), la edición vigente según la documentación de PostgreSQL; documentación en línea el 05-10-2026 y leída ese día |
| Extensión | 13.400 palabras aproximadamente (con los ejemplos de código) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); sistema de gestión de bases
de datos (SGBD; en inglés DBMS, *database management system*) y su variante relacional (RDBMS,
*relational database management system*); el lenguaje de consulta estructurado (SQL, *Structured
Query Language*) y sus familias de sentencias —el lenguaje de definición de datos (DDL, *data
definition language*), el de manipulación (DML, *data manipulation language*), el de consulta (DQL,
*data query language*), el de control (DCL, *data control language*) y el de control de transacciones
(TCL, *transaction control language*)—; el Instituto Nacional Estadounidense de Normalización (ANSI,
*American National Standards Institute*), la Organización Internacional de Normalización (ISO,
*International Organization for Standardization*) y la Comisión Electrotécnica Internacional (IEC,
*International Electrotechnical Commission*); la ACM, cuya revista *Communications of the ACM* publicó en 1970 el artículo de Codd sobre el modelo
relacional (Oracle desarrolla la sigla como «Association of Computer Machinery»); el conjunto de
propiedades de una transacción: atomicidad, coherencia, aislamiento y durabilidad (ACID); Transact-SQL
(T-SQL), el dialecto de SQL de Microsoft SQL Server, y PL/SQL, la extensión procedimental de Oracle;
Oracle AI Database, nombre con el que Oracle titula la documentación de su gestor publicada como
versión 23 (la documentación leída no desarrolla «AI»); BASIC, lenguaje de programación de propósito
general que Oracle cita junto a C; y el lenguaje de marcas extensible (XML, *eXtensible Markup
Language*), que da nombre a una parte de la norma.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 12): «Bases de datos y
> lenguaje SQL: lenguaje de interrogación de bases de datos, estándar ANSI SQL, lenguaje de
> definición de datos —DDL—, lenguaje de manipulación de datos —DML— y lenguaje de consulta de datos
> —DQL.»

Qué se puede preguntar: qué es una base de datos y qué es un SGBD; qué es una relación, una tupla y
un atributo, y cómo se llaman en lenguaje corriente; qué es una clave primaria y una clave ajena; qué
significa que SQL sea declarativo y que trabaje con conjuntos; quién propuso el modelo relacional y de
qué lenguaje procede SQL; qué organismos publican la norma, cómo se llama formalmente
(ISO/IEC 9075), cuál es su edición vigente y qué son las funciones «Core»; a qué familia pertenece
cada sentencia (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`,
`SELECT`, `GRANT`, `REVOKE`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`) y por qué unos fabricantes separan el
DQL y otros no; qué diferencia `DROP`, `DELETE` y `TRUNCATE`; qué restricciones se declaran al crear
una tabla y qué hace `ON DELETE CASCADE`; en qué orden se escriben y se procesan las cláusulas de un
`SELECT`; qué diferencia `WHERE` de `HAVING`; qué devuelven `COUNT(*)`, `COUNT(columna)`, `SUM`,
`AVG`, `MAX` y `MIN`, y qué pasa con los nulos; cómo se compara con `NULL`; qué hacen `LIKE`, `IN`,
`BETWEEN`, `EXISTS`, `ANY`/`SOME`, `ALL` y `NOT IN`; qué guardan `char`, `varchar` y los tipos
numéricos y de fecha; qué sentencia de la norma abre una transacción; qué diferencia una combinación
interna de una externa y qué hacen `USING` y `NATURAL`; qué hacen `UNION`, `INTERSECT` y `EXCEPT` y
qué deben cumplir las dos consultas; y qué cláusula limita el número de filas en la norma y en cada gestor. En la
aplicación práctica: leer una sentencia y decir qué devuelve o qué error tiene, escoger la sentencia
que resuelve una tarea, o completar una consulta con agrupación.

<!-- indice -->

## Índice

- [1. Bases de datos: lo que el lenguaje presupone](#1-bases-de-datos-lo-que-el-lenguaje-presupone)
  - [Base de datos y sistema gestor](#base-de-datos-y-sistema-gestor)
  - [Antes del modelo relacional](#antes-del-modelo-relacional)
  - [El modelo relacional y su terminología](#el-modelo-relacional-y-su-terminología)
  - [Las claves](#las-claves)
  - [Lógico y físico](#lógico-y-físico)
  - [La normalización](#la-normalización)
  - [Bases de datos no relacionales](#bases-de-datos-no-relacionales)
- [2. El lenguaje de interrogación de bases de datos: SQL](#2-el-lenguaje-de-interrogación-de-bases-de-datos-sql)
  - [Qué es SQL](#qué-es-sql)
  - [Para qué sirve](#para-qué-sirve)
  - [De dónde viene](#de-dónde-viene)
- [3. El estándar ANSI SQL](#3-el-estándar-ansi-sql)
  - [Quién lo publica y cómo se llama](#quién-lo-publica-y-cómo-se-llama)
  - [Las ediciones](#las-ediciones)
  - [Niveles de conformidad y funciones Core](#niveles-de-conformidad-y-funciones-core)
  - [Las partes de la norma](#las-partes-de-la-norma)
  - [La norma y los dialectos](#la-norma-y-los-dialectos)
- [4. Las familias de sentencias: DDL, DML, DQL y las demás](#4-las-familias-de-sentencias-ddl-dml-dql-y-las-demás)
  - [La clasificación del enunciado](#la-clasificación-del-enunciado)
  - [Cómo clasifica Oracle](#cómo-clasifica-oracle)
  - [Cómo clasifica Microsoft (SQL Server)](#cómo-clasifica-microsoft-sql-server)
  - [Cuadro comparado](#cuadro-comparado)
- [5. Lenguaje de definición de datos (DDL)](#5-lenguaje-de-definición-de-datos-ddl)
  - [CREATE TABLE](#create-table)
  - [Las restricciones](#las-restricciones)
  - [Qué pasa al borrar la fila referenciada](#qué-pasa-al-borrar-la-fila-referenciada)
  - [ALTER TABLE](#alter-table)
  - [DROP, DELETE y TRUNCATE](#drop-delete-y-truncate)
  - [Vistas e índices](#vistas-e-índices)
  - [Permisos: GRANT y REVOKE (DCL)](#permisos-grant-y-revoke-dcl)
- [6. Lenguaje de manipulación de datos (DML)](#6-lenguaje-de-manipulación-de-datos-dml)
  - [INSERT](#insert)
  - [UPDATE](#update)
  - [DELETE](#delete)
  - [MERGE](#merge)
  - [Las transacciones (TCL)](#las-transacciones-tcl)
- [7. Lenguaje de consulta de datos (DQL): SELECT](#7-lenguaje-de-consulta-de-datos-dql-select)
  - [La consulta mínima](#la-consulta-mínima)
  - [Las cláusulas, en el orden en que se escriben](#las-cláusulas-en-el-orden-en-que-se-escriben)
  - [Y en el orden en que se procesan](#y-en-el-orden-en-que-se-procesan)
  - [`WHERE`: las condiciones de fila](#where-las-condiciones-de-fila)
  - [Las funciones de agregación](#las-funciones-de-agregación)
  - [`GROUP BY` y `HAVING`](#group-by-y-having)
  - [`ORDER BY` y la limitación de filas](#order-by-y-la-limitación-de-filas)
  - [Consultas sobre varias tablas: las combinaciones (JOIN)](#consultas-sobre-varias-tablas-las-combinaciones-join)
  - [Subconsultas](#subconsultas)
  - [Operaciones de conjuntos](#operaciones-de-conjuntos)
- [8. Aplicación práctica](#8-aplicación-práctica)
  - [Leer una consulta y decir qué falla](#leer-una-consulta-y-decir-qué-falla)
  - [Escoger la sentencia](#escoger-la-sentencia)
  - [Completar una consulta con agrupación](#completar-una-consulta-con-agrupación)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Bases de datos: lo que el lenguaje presupone

### Base de datos y sistema gestor

La documentación de Oracle define la base de datos: **«A database is an organized collection of
information treated as a unit. The purpose of a database is to collect, store, and retrieve related
information for use by database applications.»** (una base de datos es una colección organizada de
información tratada como una unidad; su fin es reunir, guardar y recuperar información relacionada
para que la usen las aplicaciones). Y el programa que la maneja: **«A database management system
(DBMS) is software that controls the storage, organization, and retrieval of data.»** (un SGBD es el
software que controla el almacenamiento, la organización y la recuperación de los datos).

Los dos términos se confunden en la conversación y el examen los separa:

| Término | Qué es |
|---|---|
| Base de datos | El conjunto de datos, estructurado y almacenado |
| Sistema de gestión de bases de datos | El programa que la crea, la consulta y la protege |

Un SGBD suele tener, según Oracle (**«Typically»**), tres elementos: el código del núcleo, que **«manages memory and storage
for the DBMS»** (gestiona la memoria y el almacenamiento); el repositorio de metadatos, que **«is
usually called a data dictionary»** (suele llamarse diccionario de datos); y el lenguaje de consulta:
el lenguaje de consulta, **«This language enables applications to access the data.»** (el que permite
a las aplicaciones acceder a los datos). Ese tercer elemento es el «lenguaje de interrogación» del
enunciado, y en los sistemas relacionales es SQL (epígrafe 2).

### Antes del modelo relacional

Oracle cuenta dos tipos en la primera generación de gestores. El jerárquico: **«A hierarchical
database organizes data in a tree structure. Each parent record has one or more child records,
similar to the structure of a file system.»** (organiza los datos en árbol: cada registro padre tiene
uno o varios hijos, como un sistema de ficheros). Y el de red: **«A network database is similar to a
hierarchical database, except records have a many-to-many rather than a one-to-many relationship.»**
(como el jerárquico, pero con relaciones de muchos a muchos en vez de uno a muchos).

Su defecto es el que explica por qué existen el DDL y el lenguaje de consulta: **«The preceding
database management systems stored data in rigid, predetermined relationships. Because no data
definition language existed, changing the structure of the data was difficult. Also, these systems
lacked a simple query language, which hindered application development.»** (guardaban los datos en
relaciones rígidas y predeterminadas; al no existir un lenguaje de definición de datos, cambiar la
estructura era difícil, y la falta de un lenguaje de consulta sencillo entorpecía el desarrollo).

### El modelo relacional y su terminología

El modelo lo formuló Codd en 1970: **«In his seminal 1970 paper "A Relational Model of Data for Large
Shared Data Banks," E. F. Codd defined a relational model based on mathematical set theory. Today,
the most widely accepted database model is the relational model.»** (en su artículo de 1970, Codd
definió un modelo relacional basado en la teoría matemática de conjuntos; hoy es el modelo de base de
datos más aceptado).

Sus piezas, en la definición de Oracle: **«A relational database stores data in a set of simple
relations. A relation is a set of tuples. A tuple is an unordered set of attribute values.»** (una
base de datos relacional guarda los datos en relaciones; una relación es un conjunto de tuplas; una
tupla, un conjunto no ordenado de valores de atributos). Y su forma visible: **«A table is a
two-dimensional representation of a relation in the form of rows (tuples) and columns (attributes).
Each row in a table has the same set of columns.»** (una tabla es la representación bidimensional de
una relación en filas, que son las tuplas, y columnas, que son los atributos; todas las filas tienen
las mismas columnas). PostgreSQL lo dice en una línea: **«Relation is essentially a mathematical term
for table.»** (relación es, en esencia, el término matemático de tabla).

El modelo relacional organiza los datos en tablas, y cada palabra tiene nombre formal y nombre
corriente, que el examen mezcla:

| Nombre corriente | Nombre formal | Qué es |
|---|---|---|
| Tabla | Relación | El conjunto de datos de una misma clase |
| Fila o registro | Tupla | Un elemento concreto de esa clase |
| Columna o campo | Atributo | Una propiedad de esa clase |

Dos consecuencias que se preguntan. Cada columna tiene un tipo: **«Each row of a given table has the
same set of named columns, and each column is of a specific data type.»** (cada fila tiene las mismas
columnas con nombre, y cada columna es de un tipo de datos concreto). Y las filas no tienen orden:
**«it is important to remember that SQL does not guarantee the order of the rows within the table in
any way (although they can be explicitly sorted for display)»** (SQL no garantiza en modo alguno el
orden de las filas de una tabla, aunque pueden ordenarse expresamente para mostrarlas); por eso existe
`ORDER BY` (epígrafe 7).

### Las claves

- Clave primaria: el atributo o conjunto de atributos que identifica sin ambigüedad cada fila. No
  puede repetirse ni quedar vacía. En la documentación de PostgreSQL: **«A primary key constraint
  indicates that a column, or group of columns, can be used as a unique identifier for rows in the
  table. This requires that the values be both unique and not null.»** (la clave primaria indica que
  una columna o grupo de columnas sirve de identificador único de las filas; exige valores únicos y no
  nulos). Y **«A table can have at most one primary key.»** (una tabla tiene como máximo una clave
  primaria), aunque puede tener cualquier número de restricciones de unicidad.
- Clave ajena: el atributo que apunta a la clave primaria de otra tabla. Es lo que crea la relación.
  PostgreSQL: **«A foreign key constraint specifies that the values in a column (or a group of
  columns) must match the values appearing in some row of another table. We say this maintains the
  referential integrity between two related tables.»** (la clave ajena exige que los valores de una
  columna coincidan con los que aparecen en alguna fila de otra tabla; así se mantiene la integridad
  referencial entre las dos). Lo referenciado no tiene que ser por fuerza la clave primaria: **«A
  foreign key must reference columns that either are a primary key or form a unique constraint, or
  are columns from a non-partial unique index.»** (también columnas con restricción o índice de
  unicidad), y la «otra tabla» puede ser la misma (clave ajena autorreferenciada). Cómo se declaran
  las dos, en el epígrafe 5.

### Lógico y físico

Oracle pone como rasgo del gestor relacional la separación entre lo que se pide y cómo se guarda:
**«One characteristic of an RDBMS is the independence of physical data storage from logical data
structures.»** (la independencia entre el almacenamiento físico de los datos y las estructuras
lógicas). Por eso distingue las operaciones lógicas, en las que **«an application specifies what
content is required»** (la aplicación dice qué contenido quiere), de las físicas, en las que **«the
RDBMS determines how things should be done and carries out the operation»** (el gestor decide cómo
hacerlo y lo hace).

El diseño en dos pasos sigue esa misma línea: el diseño lógico decide qué tablas hay y cómo se
relacionan, sin mirar el gestor; el diseño físico decide cómo se guardan en disco: tipos concretos,
índices, particiones. El primero es independiente del producto y el segundo no.

### La normalización

La normalización ordena el diseño lógico. Se da como teoría de oficio, sin fuente leída:

| Forma normal | Qué exige |
|---|---|
| Primera | Que ningún campo contenga varios valores: nada de listas dentro de una celda |
| Segunda | Primera, y además que todo campo dependa de la clave primaria entera, no de una parte |
| Tercera | Segunda, y además que ningún campo dependa de otro campo que no sea la clave |

Para qué sirve, en una línea: evitar que el mismo dato esté escrito en dos sitios, porque cuando
está en dos sitios, tarde o temprano dice dos cosas distintas.

### Bases de datos no relacionales

El modelo relacional no es el único. PostgreSQL lo advierte: **«there are a number of other ways of
organizing databases. Files and directories on Unix-like operating systems form an example of a
hierarchical database. A more modern development is the object-oriented database.»** (hay otras
formas de organizar bases de datos: los ficheros y directorios de los sistemas tipo Unix son un ejemplo
de base de datos jerárquica, y un desarrollo más moderno es la base de datos orientada a objetos). Y
Oracle llama objeto-relacional al gestor relacional que añade **«user-defined types, inheritance, and
polymorphism»** (tipos definidos por el usuario, herencia y polimorfismo).

Las familias que hoy se agrupan como no relacionales, con un ejemplo corriente de cada una (oficio:
no se ha leído la documentación de esos productos):

| Familia | Cómo guarda los datos | Ejemplos |
|---|---|---|
| Relacional | En tablas con filas y columnas, con relaciones entre ellas y esquema fijo | MySQL, MariaDB, PostgreSQL, Oracle, SQL Server, H2 |
| Documental | En documentos, cada uno con su propia estructura | MongoDB |
| Clave-valor | En pares de clave y valor | Redis |
| De grafos | En nodos y aristas | Neo4j |

Las tres últimas familias se agrupan bajo el nombre común de no relacionales, y lo que las une no es
una tecnología: es que ninguna obliga a un esquema fijo de tablas. El enunciado no las pide más allá
de saber que existen: el lenguaje SQL es el de las relacionales.

## 2. El lenguaje de interrogación de bases de datos: SQL

### Qué es SQL

«Lenguaje de interrogación» es el lenguaje de consulta (*query language*) que Oracle cuenta entre los
elementos de todo SGBD (epígrafe 1). En las bases de datos relacionales ese lenguaje es SQL, que
Oracle define así: **«SQL is a set-based declarative language that provides an interface to an
RDBMS»** (un lenguaje declarativo, basado en conjuntos, que sirve de interfaz con un gestor
relacional).

Las dos palabras de la definición son las que se preguntan:

- Declarativo: **«Procedural languages such as C describe how things should be done. SQL is
  nonprocedural and describes what should be done.»** (los lenguajes procedimentales, como C,
  describen cómo hacer las cosas; SQL no es procedimental y describe qué hay que hacer). Dicho de
  otro modo: **«Users specify the result that they want (for example, the names of employees), not how
  to derive it.»** (el usuario indica el resultado que quiere, no cómo obtenerlo). El cómo lo decide el
  optimizador: **«All SQL statements use the optimizer, a part of Oracle AI Database that determines
  the most efficient means of accessing the specified data.»** (todas las sentencias pasan por el
  optimizador, la parte del gestor que decide el modo más eficiente de acceder a los datos).
- Basado en conjuntos: **«It processes sets of data as groups rather than as individual units.»**
  (procesa los datos como grupos, no unidad a unidad). Una condición de filtro recupera de una vez
  todas las filas que la cumplen: **«You need not deal with the rows one by one, nor do you have to
  worry about how they are physically stored or retrieved.»** (no hay que tratar las filas una a una
  ni preocuparse de cómo se guardan o se recuperan físicamente).

Oracle añade que **«Technically speaking, SQL is a data sublanguage.»** (técnicamente, SQL es un
sublenguaje de datos): **«all SQL statements are instructions to the database. In this SQL differs
from general-purpose programming languages like C and BASIC.»** (todas sus sentencias son
instrucciones a la base de datos, y en eso se distingue de los lenguajes de propósito general). Las
estructuras de control (bloques, condicionales, bucles, excepciones) no formaban parte de SQL: **«Flow-control
statements, such as begin-end, if-then-else, loops, and exception condition handling, were initially
not part of SQL and the SQL standard, but they can now be found in ISO/IEC 9075-4 - Persistent Stored
Modules (SQL/PSM). The PL/SQL extension to Oracle SQL is similar to PSM.»** (hoy están en la parte 4
de la norma, SQL/PSM; la extensión PL/SQL de Oracle es parecida).

Microsoft, en castellano, describe la unidad del lenguaje, la instrucción: **«Una instrucción SQL es
una unidad atómica de trabajo y, o bien tiene éxito o falla por completo.»**

### Para qué sirve

Oracle enumera las tareas que cubre SQL: **«Querying data»** (consultar datos), **«Inserting,
updating, and deleting rows in a table»** (insertar, actualizar y borrar filas), **«Creating,
replacing, altering, and dropping objects»** (crear, sustituir, modificar y eliminar objetos),
**«Controlling access to the database and its objects»** (controlar el acceso a la base de datos y a
sus objetos) y **«Guaranteeing database consistency and integrity»** (garantizar la coherencia y la
integridad), y concluye: **«SQL unifies all of the preceding tasks in one consistent language.»** (SQL
reúne todas esas tareas en un solo lenguaje coherente).

Cada tarea corresponde a una de las familias de sentencias del epígrafe 4. La correspondencia es del
tema, no de Oracle:

| Tarea | Familia | Sentencias típicas |
|---|---|---|
| Consultar datos | DQL | `SELECT` |
| Insertar, actualizar y borrar filas | DML | `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| Crear, modificar y eliminar objetos | DDL | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| Controlar el acceso | DCL | `GRANT`, `REVOKE` |
| Garantizar la coherencia (transacciones) | TCL | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

Y el mismo lenguaje vale en todos los gestores relacionales: **«All major relational database
management systems support SQL, so you can transfer all skills you have gained with SQL from one
database to another. In addition, all programs written in SQL are portable. They can often be moved
from one database to another with very little modification.»** (todos los grandes gestores
relacionales admiten SQL; lo aprendido sirve en cualquiera, y los programas pueden pasarse de uno a
otro, a menudo con muy pocos cambios). El «muy pocos cambios» es la distancia entre la norma y cada
dialecto (epígrafe 3).

### De dónde viene

Oracle resume la historia: **«Dr. E. F. Codd published the paper, "A Relational Model of Data for
Large Shared Data Banks", in June 1970 in the Association of Computer Machinery (ACM) journal,
Communications of the ACM.»** (Codd publicó el artículo en junio de 1970 en la revista de la ACM,
*Communications of the ACM*). Después, **«The language, Structured English Query Language (SEQUEL)
was developed by IBM Corporation, Inc., to use Codd's model. SEQUEL later became SQL (still
pronounced "sequel").»** (IBM desarrolló el lenguaje SEQUEL para usar el modelo de Codd; SEQUEL pasó a
ser SQL, que se sigue pronunciando «sequel»). Y la primera implantación comercial: **«In 1979,
Relational Software, Inc. (now Oracle) introduced the first commercially available implementation of
SQL.»** (en 1979, Relational Software, hoy Oracle, lanzó la primera implantación comercial de SQL).

## 3. El estándar ANSI SQL

### Quién lo publica y cómo se llama

El enunciado habla de «estándar ANSI SQL», que es como se le conoce en el oficio. La norma la
publican dos organismos a la vez. Oracle: **«Industry-accepted committees are the American National
Standards Institute (ANSI) and the International Organization for Standardization (ISO), which is
affiliated with the International Electrotechnical Commission (IEC). Both ANSI and the ISO/IEC have
accepted SQL as the standard language for relational databases. When a new SQL standard is
simultaneously published by these organizations, the names of the standards conform to conventions
used by the organization, but the standards are technically identical.»** (los comités reconocidos
son ANSI e ISO, asociada a la IEC; ambos han aceptado SQL como lenguaje normalizado de las bases de
datos relacionales, y cuando publican a la vez una nueva norma, cada uno le da el nombre según sus
convenciones, pero técnicamente son idénticas). De ahí que «SQL ANSI» y «SQL ISO» sean la misma cosa.
Oracle lo dice también así: **«SQL is the ANSI standard language for relational databases.»**

El nombre formal, según PostgreSQL: **«The formal name of the SQL standard is ISO/IEC 9075 "Database
Language SQL". A revised version of the standard is released from time to time; the most recent
update appearing in 2023. The 2023 version is referred to as ISO/IEC 9075:2023, or simply as
SQL:2023.»** (el nombre formal es ISO/IEC 9075 «Database Language SQL»; la última revisión es de
2023, ISO/IEC 9075:2023 o, abreviado, SQL:2023).

### Las ediciones

**«The versions prior to that were SQL:2016, SQL:2011, SQL:2008, SQL:2006, SQL:2003, SQL:1999, and
SQL-92. Each version replaces the previous one, so claims of conformance to earlier versions have no
official merit.»** (las anteriores fueron SQL:2016, SQL:2011, SQL:2008, SQL:2006, SQL:2003, SQL:1999 y
SQL-92; cada una sustituye a la anterior, y declarar conformidad con una versión anterior no tiene
valor oficial).

Contadas: ocho ediciones en esa lista, de SQL-92 a SQL:2023. Fíjese en la grafía: SQL-92 lleva guion
y las posteriores, dos puntos.

### Niveles de conformidad y funciones Core

SQL-92 se cumplía por niveles: **«SQL-92 defined three feature sets for conformance: Entry,
Intermediate, and Full. Most database management systems claiming SQL standard conformance were
conforming at only the Entry level, since the entire set of features in the Intermediate and Full
levels was either too voluminous or in conflict with legacy behaviors.»** (tres niveles: de entrada,
intermedio y completo; la mayoría de los gestores sólo cumplía el de entrada, porque los otros dos
eran demasiado voluminosos o chocaban con comportamientos heredados).

Desde SQL:1999 el sistema es otro: **«Starting with SQL:1999, the SQL standard defines a large set of
individual features rather than the ineffectively broad three levels found in SQL-92. A large subset
of these features represents the "Core" features, which every conforming SQL implementation must
supply. The rest of the features are purely optional.»** (la norma define un gran conjunto de
funciones sueltas; un subconjunto amplio son las funciones «Core», que toda implantación conforme debe
ofrecer, y el resto son opcionales).

Cuando PostgreSQL escribió su página, ningún gestor declaraba cumplir siquiera el Core de SQL:2023 entero. PostgreSQL de sí mismo: **«Out of 177 mandatory features required for
full Core conformance, PostgreSQL conforms to at least 170.»** (de las 177 funciones obligatorias del
Core, cumple al menos 170). Y de todos: **«at the time of writing, no current version of any database
management system claims full conformance to Core SQL:2023.»** (en el momento de escribirse esa
página, ninguna versión actual de ningún gestor declaraba cumplir el Core de SQL:2023 entero).

### Las partes de la norma

La norma no es un solo documento. PostgreSQL enumera estas partes:

| Parte | Nombre | Abreviatura |
|---|---|---|
| ISO/IEC 9075-1 | **Framework** | **SQL/Framework** |
| ISO/IEC 9075-2 | **Foundation** | **SQL/Foundation** |
| ISO/IEC 9075-3 | **Call Level Interface** | **SQL/CLI** |
| ISO/IEC 9075-4 | **Persistent Stored Modules** | **SQL/PSM** |
| ISO/IEC 9075-9 | **Management of External Data** | **SQL/MED** |
| ISO/IEC 9075-10 | **Object Language Bindings** | **SQL/OLB** |
| ISO/IEC 9075-11 | **Information and Definition Schemas** | **SQL/Schemata** |
| ISO/IEC 9075-13 | **Routines and Types using the Java Language** | **SQL/JRT** |
| ISO/IEC 9075-14 | **XML-related specifications** | **SQL/XML** |
| ISO/IEC 9075-15 | **Multi-dimensional arrays** | **SQL/MDA** |
| ISO/IEC 9075-16 | **Property Graph Queries** | **SQL/PGQ** |

Son once partes listadas, y la numeración tiene huecos: **«Note that some part numbers are not (or no
longer) used.»** (algunos números de parte no se usan o han dejado de usarse). Las que más se citan:
la 2, *Foundation*, que contiene el núcleo del lenguaje (la descripción es del tema, por su nombre:
la norma no se ha leído), y la 4, *PSM*, la de los bloques procedimentales (epígrafe 2).

### La norma y los dialectos

Cada fabricante implanta la norma y la amplía. Oracle: **«Oracle SQL is an implementation of the ANSI
standard. Oracle SQL supports numerous features that extend beyond standard SQL.»** (Oracle SQL es
una implantación de la norma ANSI y admite numerosas funciones que van más allá del SQL normalizado).
El dialecto de Microsoft se llama Transact-SQL. PostgreSQL avisa de lo mismo: **«You should be aware
that some PostgreSQL language features are extensions to the standard.»** (algunas funciones de su
lenguaje son extensiones de la norma).

Las diferencias que se preguntan, todas de la documentación de los gestores:

| Asunto | Norma | Dialectos |
|---|---|---|
| Limitar las filas devueltas | **«SQL:2008 introduced a different syntax to achieve the same result»**: `OFFSET … FETCH FIRST n ROWS ONLY` | **«The clauses `LIMIT` and `OFFSET` are PostgreSQL-specific syntax, also used by MySQL.»** SQL Server tiene `TOP` y también `OFFSET` y `FETCH` en la cláusula `ORDER BY`. La sintaxis de la norma **«is also used by IBM DB2»** |
| Vaciar una tabla | **«The SQL:2008 standard includes a `TRUNCATE` command with the syntax `TRUNCATE TABLE tablename`.»** | PostgreSQL admite además `TRUNCATE` sin `TABLE` |
| Borrar tablas | **«the standard only allows one table to be dropped per command»** | En PostgreSQL, varias a la vez, y `IF EXISTS` es **«a PostgreSQL extension»** |
| Insertar o actualizar si ya existe | `MERGE` | `INSERT … ON CONFLICT` en PostgreSQL: **«If you prefer a more SQL standard conforming statement than `ON CONFLICT`, see `MERGE`.»** |
| Sustituir una vista | — | **«`CREATE OR REPLACE VIEW` is a PostgreSQL language extension.»** |
| Lógica procedimental | SQL/PSM (parte 4) | PL/SQL en Oracle, **«similar to PSM»** |

Los tipos de datos también son de la norma o del fabricante. PostgreSQL enumera los que fija la norma:
**«The following types (or spellings thereof) are specified by SQL: `bigint`, `bit`, `bit varying`,
`boolean`, `char`, `character varying`, `character`, `varchar`, `date`, `double precision`,
`integer`, `interval`, `numeric`, `decimal`, `real`, `smallint`, `time` (with or without time zone),
`timestamp` (with or without time zone), `xml`.»** Otros son propios de PostgreSQL: la misma página
pone como ejemplo los trazados geométricos (**«geometric paths»**).

La regla práctica que sale de todo ello (oficio): para que una sentencia funcione en cualquier gestor,
se escribe en la forma de la norma (`FETCH FIRST` en vez de `LIMIT` o `TOP`, `MERGE` en vez de las
variantes propias, los tipos de la lista anterior), y se consulta la documentación del gestor antes
de usar una extensión.

## 4. Las familias de sentencias: DDL, DML, DQL y las demás

### La clasificación del enunciado

El enunciado reparte SQL en tres familias —definición (DDL), manipulación (DML) y consulta (DQL)— y
el oficio suele añadir otras dos, control de acceso (DCL) y control de transacciones (TCL). Es una
clasificación didáctica: no se ha podido confirmar que la norma ISO/IEC 9075 use esos rótulos (la
norma no se ha leído), y los dos fabricantes leídos clasifican de otro modo (cuadro de este epígrafe).

| Familia | Para qué | Sentencias |
|---|---|---|
| DDL, de definición | Crear y modificar la estructura: tablas, índices, vistas | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| DML, de manipulación | Trabajar con los datos que hay dentro | `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| DQL, de consulta | Leer los datos sin cambiarlos | `SELECT` |
| DCL, de control | Dar y quitar permisos | `GRANT`, `REVOKE` |
| TCL, de transacciones | Confirmar o deshacer un conjunto de cambios | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

La regla que separa las dos primeras es de una línea: si la sentencia toca la ESTRUCTURA, es DDL; si
toca los DATOS, es DML. `CREATE` crea una tabla; `DELETE` borra filas de una tabla que ya existe. Y la
que separa el DQL del DML: `SELECT` lee y no cambia nada.

### Cómo clasifica Oracle

Oracle divide sus sentencias en seis categorías: **«Data Definition Language (DDL) Statements»**,
**«Data Manipulation Language (DML) Statements»**, **«Transaction Control Statements»**, **«Session
Control Statements»**, **«System Control Statements»** y **«Embedded SQL Statements»** (definición de
datos, manipulación de datos, control de transacciones, control de sesión, control del sistema y SQL
incrustado). No tiene DQL ni
DCL:

- `SELECT` está en el DML. Oracle cierra la definición con **«The data manipulation language
  statements are:»** y da esta lista: `CALL`, `DELETE`, `EXPLAIN PLAN`, `INSERT`, `LOCK TABLE`,
  `MERGE`, `SELECT` y `UPDATE`. Pero Oracle reconoce que es un
  DML distinto, y esa es la razón de que otros lo separen como DQL: **«The `SELECT` statement is a
  limited form of DML statement in that it can only access data in the database. It cannot manipulate
  data stored in the database, although it can manipulate the accessed data before returning the
  results of the query.»** (`SELECT` es una forma limitada de DML, porque sólo puede acceder a los
  datos; no puede modificar los datos guardados, aunque sí transformar los que lee antes de devolver el
  resultado).
- `GRANT` y `REVOKE` están en el DDL. El DDL de Oracle sirve para **«Create, alter, and drop schema
  objects»**, **«Grant and revoke privileges and roles»**, **«Analyze information on a table, index,
  or cluster»**, **«Establish auditing options»** y **«Add comments to the data dictionary»** (crear,
  modificar y eliminar objetos del esquema; conceder y revocar privilegios y roles; analizar tablas,
  índices o *clusters*; fijar opciones de auditoría; y añadir comentarios al diccionario de datos).
- Las transacciones tienen categoría propia: **«Transaction control statements manage changes made by
  DML statements.»** (gestionan los cambios hechos por las sentencias DML). Son `COMMIT`, `ROLLBACK`,
  `SAVEPOINT`, `SET TRANSACTION` y `SET CONSTRAINT`.

Hay una diferencia de comportamiento entre DDL y DML que se pregunta. En Oracle, **«The database
implicitly commits the current transaction before and after every DDL statement.»** (el gestor
confirma implícitamente la transacción en curso antes y después de cada sentencia DDL), mientras que
las DML **«do not implicitly commit the current transaction»** (no la confirman). De ahí se sigue que, en
Oracle, un `CREATE` o un `TRUNCATE` no se deshacen con `ROLLBACK` y un `DELETE` sí (la deducción es
del tema). Es comportamiento de Oracle: no se ha leído que la norma lo imponga a todos los gestores.

### Cómo clasifica Microsoft (SQL Server)

Microsoft, en castellano, define las dos familias del enunciado: **«Las instrucciones del lenguaje de
definición de datos (DDL) definen estructuras de datos. Use estas instrucciones para crear, modificar
o quitar estructuras de datos en una base de datos.»** y **«El lenguaje de manipulación de datos (DML)
afecta a la información almacenada en la base de datos. Use estas instrucciones para insertar,
actualizar y cambiar las filas de la base de datos.»** En su DDL incluye `ALTER`, `CREATE`, `DROP`,
`RENAME` y `TRUNCATE TABLE`, entre otras; en su DML, **«`BULK INSERT`»**, `DELETE`, `INSERT`, `SELECT`,
`UPDATE` y `MERGE`. Los permisos van aparte, como **«Instrucciones de permisos»**, que **«determinan
qué usuarios e inicios de sesión pueden tener acceso a datos y realizar operaciones»**.

Microsoft también destaca `SELECT` sobre las demás: **«Hay muchos tipos de instrucciones. Quizá lo más
importante es la instrucción `SELECT` que recupera filas de la base de datos y habilita la selección de
una o varias filas o columnas de una o varias tablas en SQL Server.»**

### Cuadro comparado

| Sentencia | Clasificación del enunciado y del oficio | Oracle | SQL Server |
|---|---|---|---|
| `CREATE`, `ALTER`, `DROP` | DDL | DDL | DDL |
| `TRUNCATE` | DDL | DDL | DDL (`TRUNCATE TABLE`) |
| `INSERT`, `UPDATE`, `DELETE`, `MERGE` | DML | DML | DML |
| `SELECT` | DQL | DML (forma limitada) | DML |
| `GRANT`, `REVOKE` | DCL | DDL | Instrucciones de permisos |
| `COMMIT`, `ROLLBACK`, `SAVEPOINT` | TCL | Control de transacciones | No figuran en esa página |

En el test (oficio): si entre las opciones aparece DQL, `SELECT` es DQL; si no aparece, `SELECT` es
DML. `TRUNCATE` es DDL en los dos fabricantes leídos, aunque vacíe datos.

## 5. Lenguaje de definición de datos (DDL)

El DDL crea, modifica y elimina los objetos de la base de datos: tablas, vistas, índices, esquemas.
Sus verbos son `CREATE`, `ALTER` y `DROP`, más `TRUNCATE`. Los ejemplos de código en inglés son de la
documentación de PostgreSQL; los de nombres en castellano, del tema.

### CREATE TABLE

**«`CREATE TABLE` will create a new, initially empty table in the current database. The table will be
owned by the user issuing the command.»** (crea una tabla nueva y vacía en la base de datos actual,
propiedad del usuario que la crea). Cada columna lleva nombre y tipo, y puede llevar restricciones:

```sql
CREATE TABLE departamentos (
    id_dep    integer PRIMARY KEY,
    nombre    varchar(50) NOT NULL UNIQUE
);

CREATE TABLE empleados (
    id_emp    integer PRIMARY KEY,
    nombre    varchar(100) NOT NULL,
    salario   numeric CHECK (salario > 0),
    alta      date DEFAULT CURRENT_DATE,
    id_dep    integer REFERENCES departamentos (id_dep) ON DELETE RESTRICT
);
```

El tipo de cada columna se escoge entre los de la norma (epígrafe 3). Qué es cada uno, según la tabla
de tipos de PostgreSQL:

| Tipo | Qué guarda |
|---|---|
| `character (n)` o `char (n)` | **«fixed-length character string»** (cadena de longitud fija) |
| `character varying (n)` o `varchar (n)` | **«variable-length character string»** (cadena de longitud variable) |
| `smallint`, `integer`, `bigint` | **«signed two-byte integer»**, **«signed four-byte integer»**, **«signed eight-byte integer»** (enteros con signo de dos, cuatro y ocho bytes) |
| `numeric (p, s)` o `decimal (p, s)` | **«exact numeric of selectable precision»** (numérico exacto de precisión elegible) |
| `real` y `double precision` | **«single precision floating-point number (4 bytes)»** y **«double precision floating-point number (8 bytes)»** (coma flotante de precisión simple y doble) |
| `boolean` | **«logical Boolean (true/false)»** (lógico: verdadero o falso) |
| `date` | **«calendar date (year, month, day)»** (fecha: año, mes y día) |
| `time` | **«time of day»** (hora del día, con o sin zona horaria) |
| `timestamp` | **«date and time»** (fecha y hora, con o sin zona horaria) |
| `interval` | **«time span»** (intervalo de tiempo) |

### Las restricciones

**«SQL allows you to define constraints on columns and tables. Constraints give you as much control over
the data in your tables as you wish. If a user attempts to store data in a column that would violate a
constraint, an error is raised.»** (SQL permite definir restricciones sobre columnas y tablas; si se
intenta guardar un dato que viola una, se produce un error).

| Restricción | Qué exige, según PostgreSQL |
|---|---|
| `NOT NULL` | **«A not-null constraint simply specifies that a column must not assume the null value.»** (la columna no puede quedar nula) |
| `UNIQUE` | **«Unique constraints ensure that the data contained in a column, or a group of columns, is unique among all the rows in the table.»** (el valor no se repite en ninguna fila) |
| `PRIMARY KEY` | Identificador único de las filas: **«This requires that the values be both unique and not null.»** Una sola por tabla (epígrafe 1) |
| `FOREIGN KEY` / `REFERENCES` | Los valores deben existir en otra tabla: integridad referencial (epígrafe 1) |
| `CHECK` | **«It allows you to specify that the value in a certain column must satisfy a Boolean (truth-value) expression.»** (el valor debe cumplir una expresión lógica) |

`DEFAULT` no es una restricción: da el valor que toma la columna si no se indica otro.

El ejemplo de PostgreSQL con clave ajena:

```sql
CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_no integer REFERENCES products (product_no),
    quantity integer
);
```

Y su efecto: **«Now it is impossible to create orders with non-NULL `product_no` entries that do not
appear in the products table.»** (ya no se pueden crear pedidos con un número de producto no nulo que
no exista en la tabla de productos; un número nulo sí se admite).

### Qué pasa al borrar la fila referenciada

La clave ajena decide qué ocurre si se borra la fila a la que apunta (`ON DELETE`):

| Acción | Efecto, según PostgreSQL |
|---|---|
| `NO ACTION` (por defecto) | **«The default `ON DELETE` action is `ON DELETE NO ACTION`»**: el borrado sigue adelante, pero la clave ajena debe seguir cumpliéndose, así que **«this operation will usually result in an error»** (normalmente acaba en error) |
| `RESTRICT` | **«It prevents deletion of a referenced row.»** (impide borrar la fila referenciada), sin poder aplazar la comprobación |
| `CASCADE` | **«`CASCADE` specifies that when a referenced row is deleted, row(s) referencing it should be automatically deleted as well.»** (borra también las filas que la referencian) |
| `SET NULL` / `SET DEFAULT` | Ponen a nulo o a su valor por defecto la columna de las filas que la referenciaban |

Cuándo conviene cada una: **«When the referencing table represents something that is a component of
what is represented by the referenced table and cannot exist independently, then `CASCADE` could be
appropriate. If the two tables represent independent objects, then `RESTRICT` or `NO ACTION` is more
appropriate»** (`CASCADE`, cuando la fila que referencia es parte de la referenciada y no puede existir
sin ella; `RESTRICT` o `NO ACTION`, cuando son objetos independientes). En el ejemplo, borrar un
departamento con empleados da error por el `RESTRICT`.

### ALTER TABLE

**«`ALTER TABLE` changes the definition of an existing table.»** (cambia la definición de una tabla
existente). Sus formas más usadas, en la sintaxis de PostgreSQL:

```sql
ALTER TABLE empleados ADD COLUMN telefono varchar(20);    -- añade una columna
ALTER TABLE empleados ALTER COLUMN telefono TYPE varchar(30); -- cambia su tipo
ALTER TABLE empleados RENAME COLUMN telefono TO movil;    -- la renombra
ALTER TABLE empleados DROP COLUMN movil;                  -- la elimina
```

De la columna añadida, PostgreSQL dice que se escribe **«using the same syntax as `CREATE TABLE`»**
(con la misma sintaxis que en `CREATE TABLE`). Las cuatro órdenes siguen la sintaxis de PostgreSQL; la de otros gestores no se ha leído, y la
costumbre de oficio es consultar la documentación del gestor antes de alterar una tabla.

### DROP, DELETE y TRUNCATE

**«`DROP TABLE` removes tables from the database.»** (elimina tablas de la base de datos), y con
ellas **«any indexes, rules, triggers, and constraints that exist for the target table»** (sus
índices, reglas, disparadores y restricciones). Si otra tabla la referencia con una clave ajena, o una
vista depende de ella, hace falta `CASCADE`.

**«`TRUNCATE` quickly removes all rows from a set of tables. It has the same effect as an unqualified
`DELETE` on each table, but since it does not actually scan the tables it is faster.»** (quita
rápidamente todas las filas; tiene el mismo efecto que un `DELETE` sin `WHERE`, pero es más rápido
porque no recorre las tablas). Microsoft, entre las ventajas de `TRUNCATE TABLE`, explica por qué
gasta menos registro de transacciones: **«La `DELETE` instrucción quita las filas una
a la vez y registra una entrada en el registro de transacciones para cada fila eliminada.»**, mientras
que **«`TRUNCATE TABLE` quita los datos desasignando las páginas de datos usadas para almacenar la
tabla y los datos de índice y registra solo las desasignaciones de página en el registro de
transacciones.»**

`DELETE` (epígrafe 6) borra filas: **«If the `WHERE` clause is absent, the effect is to delete all rows
in the table. The result is a valid, but empty table.»** (sin `WHERE` borra todas las filas y deja una
tabla válida, pero vacía).

El matiz que a veces despista: `DROP` y `DELETE` parecen lo mismo y no lo son. `DROP` elimina la
tabla entera, con su estructura, y es DDL; `DELETE` borra filas y deja la tabla vacía en pie, y es
DML. `TRUNCATE` vacía la tabla sin borrar su estructura y se clasifica como DDL, porque no opera
fila a fila.

| | `DROP TABLE` | `TRUNCATE` | `DELETE` |
|---|---|---|---|
| Familia | DDL | DDL | DML |
| Qué quita | La tabla, con su estructura | Todas las filas | Las filas que cumplen el `WHERE` (todas, si no lo hay) |
| La tabla queda | No existe | Vacía | Vacía o con las filas no borradas |
| Admite `WHERE` | No | No | Sí |

PostgreSQL lo resume: **«To empty a table of rows without destroying the table, use `DELETE` or
`TRUNCATE`.»** (para vaciar una tabla sin destruirla, `DELETE` o `TRUNCATE`).

### Vistas e índices

**«`CREATE VIEW` defines a view of a query. The view is not physically materialized. Instead, the query
is run every time the view is referenced in a query.»** (una vista es una consulta con nombre; no se
guarda físicamente, sino que la consulta se ejecuta cada vez que se usa la vista).

```sql
CREATE VIEW empleados_ventas AS
    SELECT id_emp, nombre FROM empleados WHERE id_dep = 3;
```

**«`CREATE INDEX` constructs an index on the specified column(s) of the specified relation»** (crea un
índice sobre una o varias columnas). **«Indexes are primarily used to enhance database performance
(though inappropriate use can result in slower performance).»** (sirven sobre todo para mejorar el
rendimiento, aunque un uso inadecuado puede empeorarlo). Con `UNIQUE`, el índice además impide
duplicados: **«Attempts to insert or update data which would result in duplicate entries will
generate an error.»**

```sql
CREATE UNIQUE INDEX title_idx ON films (title);
```

### Permisos: GRANT y REVOKE (DCL)

El oficio los llama DCL; Oracle los pone en el DDL y Microsoft en las instrucciones de permisos
(epígrafe 4). Microsoft resume `GRANT`: **«Concede permisos sobre un elemento protegible a una entidad
de seguridad. El concepto general es para `GRANT &lt;some permission&gt; ON &lt;some object&gt; TO <some user,
login, or group>`.»** Y PostgreSQL, `REVOKE`: **«The `REVOKE` command revokes previously granted
privileges from one or more roles.»** (retira privilegios concedidos antes).

Ejemplos de PostgreSQL: **«Grant insert privilege to all users on table `films`:»**

```sql
GRANT INSERT ON films TO PUBLIC;
GRANT ALL PRIVILEGES ON kinds TO manuel;
REVOKE INSERT ON films FROM PUBLIC;
```

Dos detalles. La opción de reconceder: **«If `WITH GRANT OPTION` is specified, the recipient of the
privilege can in turn grant it to others.»** (quien recibe el privilegio puede a su vez concederlo).
Y la trampa de `PUBLIC`: un usuario suma los privilegios recibidos directamente, por sus roles y por
`PUBLIC`, de modo que **«revoking `SELECT` privilege from `PUBLIC` does not necessarily mean that all
roles have lost `SELECT` privilege on the object»** (quitar `SELECT` a `PUBLIC` no significa que todos
lo hayan perdido).

## 6. Lenguaje de manipulación de datos (DML)

El DML trabaja con las filas de las tablas que ya existen: las inserta (`INSERT`), las cambia
(`UPDATE`), las borra (`DELETE`) o hace las tres cosas según el caso (`MERGE`). En la definición de
Oracle, **«Data manipulation language (DML) statements access and manipulate data in existing schema
objects.»** (acceden a los datos de objetos ya existentes y los manipulan).

### INSERT

La forma básica nombra la tabla, las columnas y los valores:

```sql
INSERT INTO empleados (id_emp, nombre, salario, id_dep)
VALUES (1, 'Ana Ruiz', 2100, 3);

INSERT INTO empleados (id_emp, nombre, salario, id_dep)
VALUES (2, 'Luis Gil', 1900, 3),
       (3, 'Eva Sanz', 2300, 4);           -- varias filas en una sentencia

INSERT INTO historico (id_emp, nombre)
SELECT id_emp, nombre FROM empleados WHERE id_dep = 4;   -- filas que salen de una consulta
```

La sintaxis de PostgreSQL admite las tres formas: **«`DEFAULT VALUES` | `VALUES` ( { `expression` |
`DEFAULT` } [, ...] ) [, ...] | `query`»** (valores por defecto, una o varias listas de valores, o una
consulta). La columna que no se nombra toma su valor por defecto o queda nula: **«Each column not present in
the explicit or implicit column list will be filled with a default value, either its declared default
value or null if there is none.»** Sin lista de columnas, **«the default is all the columns of the
table in their declared order»** (se entienden todas, en el orden en que se declararon). PostgreSQL
admite omitir la lista aunque falten valores al final, pero la norma no: **«the case in which a column name list is omitted, but not all the columns are
filled from the `VALUES` clause or `query`, is disallowed by the standard.»**

### UPDATE

**«`UPDATE` changes the values of the specified columns in all rows that satisfy the condition. Only the
columns to be modified need be mentioned in the `SET` clause; columns not explicitly modified retain
their previous values.»** (cambia las columnas indicadas en todas las filas que cumplen la condición;
sólo se nombran en `SET` las que cambian, y las demás conservan su valor). El ejemplo de PostgreSQL:
**«Change the word `Drama` to `Dramatic` in the column `kind` of the table `films`:»**

```sql
UPDATE films SET kind = 'Dramatic' WHERE kind = 'Drama';
UPDATE empleados SET salario = salario * 1.02 WHERE id_dep = 3;   -- valor calculado
```

El peligro es olvidar el `WHERE`. Microsoft lo muestra con ejemplos: **«En los ejemplos siguientes se
muestra cómo se pueden ver afectadas todas las filas cuando no se usa una cláusula `WHERE` para
especificar la fila (o filas) que se van a actualizar.»**

### DELETE

**«`DELETE` deletes rows that satisfy the `WHERE` clause from the specified table.»** (borra las filas
que cumplen el `WHERE`), y sin `WHERE` las borra todas (epígrafe 5). Los ejemplos de PostgreSQL:
**«Delete all films but musicals:»** y **«Clear the table `films`:»**

```sql
DELETE FROM films WHERE kind <> 'Musical';
DELETE FROM films;
```

Si otra tabla tiene una clave ajena hacia la fila borrada, se aplica la acción `ON DELETE` de esa
clave (epígrafe 5): con `RESTRICT` o `NO ACTION`, error; con `CASCADE`, se borran también las filas
que la referencian.

### MERGE

**«`MERGE` provides a single SQL statement that can conditionally `INSERT`, `UPDATE` or `DELETE` rows, a
task that would otherwise require multiple procedural language statements.»** (en una sola sentencia
inserta, actualiza o borra filas según una condición, lo que de otro modo exigiría varias sentencias
procedimentales). Primero combina el origen de datos con la tabla de destino y, para cada fila,
aplica la primera cláusula `WHEN` que se cumpla. Es sentencia de la norma: **«This command conforms to
the SQL standard.»**, aunque PostgreSQL le añade extensiones (entre ellas `WHEN NOT MATCHED BY SOURCE`,
`DO NOTHING` y `RETURNING`). Un ejemplo con la estructura de la sintaxis de PostgreSQL:

```sql
MERGE INTO empleados e
USING altas a ON e.id_emp = a.id_emp
WHEN MATCHED THEN
    UPDATE SET salario = a.salario
WHEN NOT MATCHED THEN
    INSERT (id_emp, nombre, salario) VALUES (a.id_emp, a.nombre, a.salario);
```

### Las transacciones (TCL)

Los cambios del DML se agrupan en transacciones. Microsoft, en castellano: **«Una transacción es una
unidad única de trabajo. Si una transacción tiene éxito, todas las modificaciones de los datos
realizadas durante la transacción se confirman y se convierten en una parte permanente de la base de
datos. Si una transacción encuentra errores y debe cancelarse o revertirse, se borran todas las
modificaciones de los datos.»**

Sus cuatro propiedades, ACID, en la guía de Microsoft: **«Una unidad lógica de trabajo debe exhibir
cuatro propiedades, conocidas como propiedades de atomicidad, coherencia, aislamiento y durabilidad
(ACID), para ser calificada como transacción.»**

| Propiedad | Qué exige |
|---|---|
| Atomicidad | **«Una transacción debe ser una unidad atómica de trabajo, tanto si se realizan todas sus modificaciones en los datos, como si no se realiza ninguna de ellas.»** |
| Coherencia | **«Cuando finaliza, una transacción debe dejar todos los datos en un estado coherente.»** |
| Aislamiento | **«Las modificaciones realizadas por transacciones simultáneas se deben aislar de las modificaciones llevadas a cabo por otras transacciones simultáneas.»** |
| Durabilidad | **«Una vez concluida una transacción totalmente durable, sus efectos son permanentes en el sistema. Las modificaciones persisten aún en el caso de producirse un error del sistema.»** |

Las sentencias, con la descripción de PostgreSQL:

| Sentencia | Qué hace |
|---|---|
| `START TRANSACTION` (en la norma); `BEGIN` en PostgreSQL, `BEGIN TRANSACTION` en SQL Server | Abre la transacción |
| `COMMIT` | **«`COMMIT` commits the current transaction. All changes made by the transaction become visible to others and are guaranteed to be durable if a crash occurs.»** (confirma: los cambios se hacen visibles a los demás y duraderos aunque el sistema caiga) |
| `ROLLBACK` | **«`ROLLBACK` rolls back the current transaction and causes all the updates made by the transaction to be discarded.»** (deshace: descarta todos los cambios de la transacción) |
| `SAVEPOINT` | **«`SAVEPOINT` establishes a new savepoint within the current transaction.»**: **«A savepoint is a special mark inside a transaction that allows all commands that are executed after it was established to be rolled back, restoring the transaction state to what it was at the time of the savepoint.»** (una marca dentro de la transacción a la que se puede volver deshaciendo lo posterior) |
| `ROLLBACK TO` | Vuelve al punto de guardado: **«All the transaction's database changes between defining the savepoint and rolling back to it are discarded, but changes earlier than the savepoint are kept.»** (se descarta lo posterior al punto y se conserva lo anterior) |

`COMMIT` y `ROLLBACK` son de la norma: **«The command `COMMIT` conforms to the SQL standard.»** y
**«The command `ROLLBACK` conforms to the SQL standard.»** (las formas `COMMIT TRANSACTION` y
`ROLLBACK TRANSACTION` son extensiones de PostgreSQL). Para abrirla, en cambio, la sentencia de la
norma es `START TRANSACTION`, y `BEGIN` es una extensión: **«`BEGIN` is a PostgreSQL language
extension. It is equivalent to the SQL-standard command `START TRANSACTION`»** (`BEGIN` es una
extensión de PostgreSQL, equivalente a la sentencia de la norma `START TRANSACTION`). PostgreSQL
admite las dos: **«`START TRANSACTION` has the same functionality as `BEGIN`.»** La norma ni siquiera
obliga a usarla: **«In the standard, it is not necessary to issue `START TRANSACTION` to start a
transaction block: any SQL command implicitly begins a block.»** (en la norma no hace falta
`START TRANSACTION`: cualquier sentencia abre implícitamente la transacción).

Un ejemplo:

```sql
BEGIN;
UPDATE cuentas SET saldo = saldo - 100 WHERE titular = 'Ana';
SAVEPOINT tras_cargo;
UPDATE cuentas SET saldo = saldo + 100 WHERE titular = 'Luis';
ROLLBACK TO tras_cargo;        -- se deshace el abono a Luis; el cargo a Ana sigue
UPDATE cuentas SET saldo = saldo + 100 WHERE titular = 'Eva';
COMMIT;                        -- se confirman el cargo a Ana y el abono a Eva
```

Si no se abre una transacción, cada sentencia es una por sí sola. PostgreSQL: **«If you do not issue a
`BEGIN` command, then each individual statement has an implicit `BEGIN` and (if successful) `COMMIT`
wrapped around it.»** (cada sentencia lleva un `BEGIN` implícito y, si sale bien, un `COMMIT`). SQL
Server distingue cuatro modos; los tres generales son **«Transacciones de confirmación automática»**, en que **«Cada
instrucción individual es una transacción.»**; **«Transacciones explícitas»**, en que **«Cada
transacción se inicia explícitamente con la `BEGIN TRANSACTION` instrucción y finaliza explícitamente
con una `COMMIT` instrucción o `ROLLBACK` .»** [sic]; y **«Transacciones implícitas»**, en que **«Una
nueva transacción se inicia implícitamente cuando se completa la transacción anterior, pero cada
transacción se completa explícitamente con una `COMMIT` instrucción o `ROLLBACK` .»** [sic]. El cuarto,
las transacciones con ámbito por lotes, sólo se aplica a las sesiones de conjuntos de resultados
activos múltiples (MARS, sigla que la página da sin desarrollar en inglés).

Recuérdese lo dicho del DDL en Oracle (epígrafe 4): confirma implícitamente la transacción en curso,
de modo que un `CREATE` en medio de una transacción confirma también los cambios DML anteriores.

## 7. Lenguaje de consulta de datos (DQL): SELECT

El DQL es una sola sentencia, `SELECT`: **«`SELECT` retrieves rows from zero or more tables.»**
(recupera filas de cero o más tablas). Para usarla hace falta permiso: **«You must have `SELECT`
privilege on each column used in a `SELECT` command.»** (privilegio `SELECT` sobre cada columna que
se use).

### La consulta mínima

```sql
SELECT * FROM empleados;                      -- todas las filas y todas las columnas
SELECT nombre, salario FROM empleados;        -- sólo dos columnas
SELECT nombre, salario * 14 AS anual FROM empleados;   -- columna calculada con alias
SELECT DISTINCT id_dep FROM empleados;        -- cada departamento, una vez
```

El asterisco significa «todas las columnas»: **«Instead of an expression, `*` can be written in the
output list as a shorthand for all the columns of the selected rows.»** (en lugar de una expresión,
`*` abrevia todas las columnas de las filas seleccionadas). `AS` da nombre a una columna de salida.
`DISTINCT` quita repetidos: **«`SELECT DISTINCT` eliminates duplicate rows from the result.»**, y
**«`SELECT ALL` (the default) will return all candidate rows, including duplicates.»** (`ALL`, el
valor por defecto, devuelve todas, repetidas incluidas).

### Las cláusulas, en el orden en que se escriben

La estructura completa de una consulta, por orden, que es lo que conviene llevar memorizado:

```
SELECT columnas
FROM tabla
WHERE condición de fila
GROUP BY columnas de agrupación
HAVING condición de grupo
ORDER BY columnas de ordenación
```

A la que se añade, al final, la limitación de filas (`OFFSET … FETCH FIRST` en la norma; epígrafe
3). Es el orden de la sinopsis de PostgreSQL: `SELECT` … `FROM` … `WHERE` … `GROUP BY` … `HAVING` …
`ORDER BY` … `OFFSET` … `FETCH`.

### Y en el orden en que se procesan

El orden de escritura no es el de ejecución. Microsoft da el orden de procesamiento lógico: `FROM`,
`ON`, `JOIN`, `WHERE`, `GROUP BY`, `WITH CUBE` o `WITH ROLLUP`, `HAVING`, `SELECT`, `DISTINCT`,
`ORDER BY` y `TOP`. Y la consecuencia: **«dado que la cláusula es el `SELECT` paso 8, no se puede hacer
referencia a ningún alias de columna o columnas derivadas definidas en esa cláusula mediante cláusulas
anteriores. Sin embargo, las cláusulas posteriores pueden hacer referencia a ellas, como la `ORDER BY`
cláusula .»** [sic]. Dicho de otro modo: un alias definido en el `SELECT` se puede usar en el
`ORDER BY`, pero no en el `WHERE`. Microsoft advierte de que es un orden lógico: **«El procesador de
consultas determina la ejecución física real de la instrucción y el orden puede variar de esta
lista.»**

PostgreSQL describe el mismo recorrido: se calculan los elementos del `FROM`; **«If the `WHERE` clause
is specified, all rows that do not satisfy the condition are eliminated from the output.»** (el
`WHERE` elimina las filas que no cumplen la condición); después se agrupa y se calculan los agregados,
y **«If the `HAVING` clause is present, it eliminates groups that do not satisfy the given
condition.»** (el `HAVING` elimina los grupos que no cumplen la suya); luego se calculan las columnas
de salida, se quitan repetidos, se ordena y se limita.

### `WHERE`: las condiciones de fila

Los operadores de comparación son los habituales: `<`, `>`, `<=`, `>=`, `=` y, para «distinto», `<>`:
**«`<>` is the standard SQL notation for "not equal". `!=` is an alias»** (`<>` es la notación de la
norma; `!=` es un alias que PostgreSQL admite). Se combinan con `AND`, `OR` y `NOT`. Y los
predicados que más se preguntan:

| Predicado | Qué hace | Ejemplo |
|---|---|---|
| `BETWEEN … AND …` | Rango, con los extremos incluidos: **«Notice that `BETWEEN` treats the endpoint values as included in the range.»** | `salario BETWEEN 1500 AND 2500` |
| `IN (…)` | Pertenencia a una lista o al resultado de una subconsulta: es cierto **«if any equal subquery row is found»** (si alguna fila es igual) | `id_dep IN (3, 4)` |
| `LIKE` | Patrón de texto: **«An underscore (`_`) in `pattern` stands for (matches) any single character; a percent sign (`%`) matches any sequence of zero or more characters.»** (`_`, un carácter cualquiera; `%`, cualquier secuencia de cero o más caracteres) | `nombre LIKE 'A%'` |
| `IS NULL` / `IS NOT NULL` | Comprueba si el valor es nulo | `id_dep IS NULL` |
| `EXISTS (subconsulta)` | Cierto si la subconsulta devuelve alguna fila: **«If it returns at least one row, the result of `EXISTS` is "true"; if the subquery returns no rows, the result of `EXISTS` is "false".»** | ver más abajo |

`LIKE` compara la cadena entera: **«`LIKE` pattern matching always covers the entire string. Therefore,
if it's desired to match a sequence anywhere within a string, the pattern must start and end with a
percent sign.»** (para buscar un trozo en cualquier parte, el patrón empieza y acaba en `%`:
`'%Ruiz%'`).

El nulo merece aparte, porque es la trampa más corriente. SQL usa tres valores lógicos: **«SQL uses a
three-valued logic system with true, false, and `null`, which represents "unknown".»** (verdadero,
falso y nulo, que significa «desconocido»). Por eso no se compara con `=`: **«Ordinary comparison
operators yield null (signifying "unknown"), not true or false, when either input is null. For
example, `7 = NULL` yields null, as does `7 <> NULL`.»** (si un operando es nulo, la comparación da
nulo, no verdadero ni falso). `WHERE id_dep = NULL` no devuelve ninguna fila; lo correcto es
`WHERE id_dep IS NULL`.

### Las funciones de agregación

**«An aggregate function computes a single result from multiple input rows.»** (una función de
agregación calcula un solo resultado a partir de varias filas). Las cinco que se preguntan:

| Función | Qué devuelve, según PostgreSQL |
|---|---|
| `COUNT(*)` | **«Computes the number of input rows.»** (cuántas filas) |
| `COUNT(expresión)` | **«Computes the number of input rows in which the input value is not null.»** (cuántas filas tienen ese valor no nulo) |
| `SUM` | **«Computes the sum of the non-null input values.»** (la suma de los valores no nulos) |
| `AVG` | **«Computes the average (arithmetic mean) of all the non-null input values.»** (la media aritmética de los no nulos) |
| `MAX` y `MIN` | **«Computes the maximum of the non-null input values.»** y **«Computes the minimum of the non-null input values.»** (el mayor y el menor de los no nulos) |

Dos consecuencias. `COUNT(*)` y `COUNT(columna)` no dan lo mismo si la columna tiene nulos. Y una tabla
vacía no da cero salvo en `COUNT`: **«It should be noted that except for `count`, these functions
return a null value when no rows are selected. In particular, `sum` of no rows returns null, not zero
as one might expect»** (salvo `count`, devuelven nulo cuando no hay filas; `sum` de ninguna fila da
nulo, no cero).

```sql
SELECT COUNT(*) FROM empleados;                    -- número de filas de la tabla
SELECT COUNT(id_dep) FROM empleados;               -- filas con departamento no nulo
SELECT AVG(salario), MAX(salario) FROM empleados;
```

### `GROUP BY` y `HAVING`

`GROUP BY` forma grupos de filas con el mismo valor y calcula los agregados de cada grupo:
**«which gives us one output row per city. Each aggregate result is computed over the table rows
matching that city.»** (una fila de salida por ciudad, con los agregados calculados sobre las filas de
esa ciudad), en el ejemplo de PostgreSQL. `HAVING` filtra esos grupos.

La distinción entre `WHERE` y `HAVING` es la que más se pregunta en esta familia: `WHERE` filtra
filas antes de agrupar y `HAVING` filtra grupos después. PostgreSQL: **«The fundamental difference
between `WHERE` and `HAVING` is this: `WHERE` selects input rows before groups and aggregates are
computed (thus, it controls which rows go into the aggregate computation), whereas `HAVING` selects
group rows after groups and aggregates are computed. Thus, the `WHERE` clause must not contain
aggregate functions»** (`WHERE` escoge las filas antes de agrupar y decide cuáles entran en el
cálculo; `HAVING` escoge grupos después; por eso el `WHERE` no puede llevar funciones de agregación).

El ejemplo de PostgreSQL, completo: ciudades, cuántas lecturas tiene cada una y la mínima más alta,
sólo para las ciudades cuyo nombre empieza por S:

```sql
SELECT city, count(*), max(temp_lo)
    FROM weather
    WHERE city LIKE 'S%'
    GROUP BY city;
```

Y con `HAVING`, sólo los grupos cuyo máximo no llega a 40:

```sql
SELECT city, count(*), max(temp_lo)
    FROM weather
    GROUP BY city
    HAVING max(temp_lo) < 40;
```

Poner en el `WHERE` una condición que no necesita agregado es además más eficiente: **«This is more
efficient than adding the restriction to `HAVING`, because we avoid doing the grouping and aggregate
calculations for all rows that fail the `WHERE` check.»**

Una columna del `SELECT` que no esté en un agregado tiene que estar en el `GROUP BY`, con una
salvedad. PostgreSQL: **«When `GROUP BY` is present, or any aggregate functions are present, it is not
valid for the `SELECT` list expressions to refer to ungrouped columns except within aggregate functions
or when the ungrouped column is functionally dependent on the grouped columns, since there would
otherwise be more than one possible value to return for an ungrouped column.»** (con `GROUP BY` o con
agregados, la lista del `SELECT` no puede citar columnas no agrupadas, salvo dentro de un agregado o
cuando dependen funcionalmente de las agrupadas, porque habría más de un valor posible que devolver).
Y define esa dependencia: **«A functional dependency exists if the grouped columns (or a subset
thereof) are the primary key of the table containing the ungrouped column.»** (existe cuando las
columnas agrupadas, o parte de ellas, son la clave primaria de la tabla de la columna no agrupada).
Esa definición es la de PostgreSQL; la norma va más allá: **«PostgreSQL recognizes functional
dependency (allowing columns to be omitted from `GROUP BY`) only when a table's primary key is
included in the `GROUP BY` list. The SQL standard specifies additional conditions that should be
recognized.»** (PostgreSQL sólo reconoce la dependencia cuando la clave primaria está en el
`GROUP BY`; la norma fija más casos). Así, `GROUP BY id_emp` permite poner `nombre` en el `SELECT`, porque `id_emp` es la clave primaria de
`empleados`; `GROUP BY id_dep` no lo permite. Lo mismo vale para el `HAVING`: **«Each column
referenced in `condition` must unambiguously reference a grouping column, unless the reference appears
within an aggregate function or the ungrouped column is functionally dependent on the grouping
columns.»** (cada columna citada debe ser de agrupación, salvo que esté dentro de un agregado o
dependa funcionalmente de las de agrupación).

### `ORDER BY` y la limitación de filas

**«If the `ORDER BY` clause is specified, the returned rows are sorted in the specified order. If
`ORDER BY` is not given, the rows are returned in whatever order the system finds fastest to
produce.»** (sin `ORDER BY`, las filas salen en el orden que al sistema le resulte más rápido). La
dirección: **«Optionally one can add the key word `ASC` (ascending) or `DESC` (descending) after any
expression in the `ORDER BY` clause. If not specified, `ASC` is assumed by default.»** (ascendente por
defecto).

Para quedarse con las primeras filas, la forma de la norma es `FETCH FIRST`; `LIMIT` es de PostgreSQL
y MySQL, y `TOP`, de SQL Server (epígrafe 3). Las tres, con un orden fijado, porque sin él el resultado
no es determinista: **«SQL does not promise to deliver the results of a query in any particular order
unless `ORDER BY` is used to constrain the order.»**

```sql
SELECT nombre, salario FROM empleados ORDER BY salario DESC
    FETCH FIRST 3 ROWS ONLY;                       -- norma (SQL:2008 y posteriores)
SELECT nombre, salario FROM empleados ORDER BY salario DESC LIMIT 3;      -- PostgreSQL, MySQL
SELECT TOP (3) nombre, salario FROM empleados ORDER BY salario DESC;      -- SQL Server
```

En SQL Server, los paréntesis de `TOP` son opcionales con una constante entera, pero Microsoft los
recomienda: **«Se recomienda usar siempre paréntesis para `TOP` en instrucciones `SELECT`.»**

### Consultas sobre varias tablas: las combinaciones (JOIN)

**«Queries that access multiple tables (or multiple instances of the same table) at one time are
called join queries. They combine rows from one table with rows from a second table, with an
expression specifying which rows are to be paired.»** (las consultas que acceden a varias tablas a la
vez se llaman combinaciones; unen filas de una tabla con filas de otra, con una expresión que dice qué
filas se emparejan).

| Combinación | Qué devuelve, según PostgreSQL |
|---|---|
| `[INNER] JOIN` | Sólo las filas que casan en las dos tablas (las combinaciones vistas hasta la externa **«are inner joins»**) |
| `LEFT [OUTER] JOIN` | Las que casan, más **«one copy of each row in the left-hand table for which there was no right-hand row that passed the join condition»**, completadas con nulos a la derecha |
| `RIGHT [OUTER] JOIN` | **«all the joined rows, plus one row for each unmatched right-hand row (extended with nulls on the left)»** |
| `FULL [OUTER] JOIN` | **«all the joined rows, plus one row for each unmatched left-hand row (extended with nulls on the right), plus one row for each unmatched right-hand row (extended with nulls on the left)»** |
| `CROSS JOIN` | El producto cartesiano: **«`CROSS JOIN` is equivalent to `INNER JOIN ON (TRUE)`, that is, no rows are removed by qualification.»** |

`INNER` y `OUTER` son opcionales. Las combinaciones internas y externas necesitan condición: **«For
the `INNER` and `OUTER` join types, a join condition must be specified, namely exactly one of
`ON join_condition`, `USING (join_column [, ...])`, or `NATURAL`.»** (exactamente una de tres: `ON` con
una condición, `USING` con una lista de columnas, o `NATURAL`).

Las dos últimas abrevian la primera:

| Forma | Qué hace, según PostgreSQL |
|---|---|
| `USING (a, b, …)` | **«A clause of the form `USING ( a, b, ... )` is shorthand for `ON left_table.a = right_table.a AND left_table.b = right_table.b ...`. Also, `USING` implies that only one of each pair of equivalent columns will be included in the join output, not both.»** (equivale a igualar esas columnas en el `ON`, y cada par de columnas iguales sale una sola vez en el resultado) |
| `NATURAL` | **«`NATURAL` is shorthand for a `USING` list that mentions all columns in the two tables that have matching names. If there are no common column names, `NATURAL` is equivalent to `ON TRUE`.»** (un `USING` con todas las columnas que se llaman igual en las dos tablas; si no hay ninguna, equivale a `ON TRUE`, es decir, al producto cartesiano) |

Con las tablas del tema, `NATURAL JOIN` no daría lo esperado: `empleados` y `departamentos` comparten
`id_dep`, pero también `nombre`, así que emparejaría los empleados cuyo nombre coincide con el del
departamento. `JOIN departamentos USING (id_dep)` sí une sólo por el departamento.

```sql
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
JOIN departamentos d ON e.id_dep = d.id_dep;          -- sólo empleados con departamento

SELECT e.nombre, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.id_dep = d.id_dep;     -- todos los empleados; nulo si no tienen
```

Los alias de tabla (`e`, `d`) abrevian, y una vez puestos sustituyen al nombre: **«When an alias is
provided, it completely hides the actual name of the table or function»**. Y es buena práctica
cualificar las columnas: **«It is widely considered good style to qualify all column names in a join
query, so that the query won't fail if a duplicate column name is later added to one of the
tables.»**

### Subconsultas

Una consulta puede ir dentro de otra. El ejemplo de PostgreSQL: como un agregado no puede ir en el
`WHERE`, la ciudad con la mínima más alta se busca con una subconsulta, que **«is an independent
computation that computes its own aggregate separately from what is happening in the outer
query»** (es un cálculo independiente que obtiene su propio agregado):

```sql
SELECT city FROM weather
    WHERE temp_lo = (SELECT max(temp_lo) FROM weather);
```

Con `IN` y `EXISTS`:

```sql
SELECT nombre FROM empleados
WHERE id_dep IN (SELECT id_dep FROM departamentos WHERE nombre = 'Sistemas');

SELECT d.nombre FROM departamentos d
WHERE EXISTS (SELECT 1 FROM empleados e WHERE e.id_dep = d.id_dep);   -- departamentos con empleados
```

Una subconsulta de una columna también se compara con un operador seguido de `ANY` (o `SOME`) o de
`ALL`. PostgreSQL:

| Predicado | Qué hace |
|---|---|
| `expresión operador ANY (subconsulta)` | **«The result of `ANY` is "true" if any true result is obtained. The result is "false" if no true result is found (including the case where the subquery returns no rows).»** (cierto si la comparación sale cierta con alguna fila; falso si con ninguna, también cuando la subconsulta no devuelve filas). Y: **«`SOME` is a synonym for `ANY`. `IN` is equivalent to `= ANY`.»** (`SOME` es sinónimo de `ANY`; `IN` equivale a `= ANY`) |
| `expresión operador ALL (subconsulta)` | **«The result of `ALL` is "true" if all rows yield true (including the case where the subquery returns no rows). The result is "false" if any false result is found.»** (cierto si la comparación sale cierta con todas las filas, también cuando la subconsulta no devuelve ninguna; falso si sale falsa con alguna) |
| `expresión NOT IN (subconsulta)` | **«The result of `NOT IN` is "true" if only unequal subquery rows are found (including the case where the subquery returns no rows). The result is "false" if any equal row is found.»** (cierto si ninguna fila es igual; falso si alguna lo es). Y: **«`NOT IN` is equivalent to `<> ALL`.»** |

```sql
SELECT nombre FROM empleados
WHERE salario > ALL (SELECT salario FROM empleados WHERE id_dep = 3);   -- más que todos los del 3

SELECT nombre FROM empleados
WHERE salario > ANY (SELECT salario FROM empleados WHERE id_dep = 3);   -- más que alguno del 3
```

El nulo vuelve a ser la trampa, sobre todo con `NOT IN`: **«Note that if the left-hand expression
yields null, or if there are no equal right-hand values and at least one right-hand row yields null,
the result of the `NOT IN` construct will be null, not true.»** (si la expresión de la izquierda es
nula, o si ningún valor es igual pero alguna fila de la subconsulta es nula, el resultado es nulo, no
verdadero). Así, esta consulta, que busca los departamentos sin empleados, no devuelve ninguna fila
en cuanto un solo empleado tenga `id_dep` nulo:

```sql
SELECT nombre FROM departamentos
WHERE id_dep NOT IN (SELECT id_dep FROM empleados);
```

Con `ANY` pasa lo mismo: **«if there are no successes and
at least one right-hand row yields null for the operator's result, the result of the `ANY` construct
will be null, not false.»** (si ninguna comparación sale cierta y alguna da nulo, el resultado es nulo,
no falso). Y con `ALL`: **«The result is NULL if no comparison with a subquery row returns false, and
at least one comparison returns NULL.»** (si ninguna comparación sale falsa y alguna da nulo, el
resultado es nulo).

### Operaciones de conjuntos

| Operador | Qué devuelve, según PostgreSQL |
|---|---|
| `UNION` | **«The `UNION` operator returns all rows that are in one or both of the result sets.»** (las filas de uno o de los dos resultados) |
| `INTERSECT` | **«The `INTERSECT` operator returns all rows that are strictly in both result sets.»** (las que están en los dos) |
| `EXCEPT` | **«The `EXCEPT` operator returns the rows that are in the first result set but not in the second.»** (las del primero que no están en el segundo) |

Los repetidos: **«In all three cases, duplicate rows are eliminated unless `ALL` is specified.»** (se
eliminan salvo con `ALL`). Por eso **«`UNION ALL` is usually significantly quicker than `UNION`»**.

Las dos consultas tienen que encajar: **«In order to calculate the union, intersection, or difference
of two queries, the two queries must be "union compatible", which means that they return the same
number of columns and the corresponding columns have compatible data types»** (para la unión, la
intersección o la diferencia, las dos consultas deben ser «compatibles para la unión»: el mismo número
de columnas y, columna a columna, tipos de datos compatibles). No se exige que lean la misma tabla ni
que devuelvan el mismo número de filas:

```sql
SELECT nombre FROM empleados UNION SELECT nombre FROM departamentos;          -- válida: una columna de texto a cada lado
SELECT id_emp, nombre FROM empleados UNION SELECT nombre FROM departamentos;  -- error: dos columnas frente a una
```

## 8. Aplicación práctica

Casos de oficio, resueltos con lo dicho en los epígrafes anteriores. Las tablas son las del tema:
`departamentos (id_dep, nombre)` y `empleados (id_emp, nombre, salario, alta, id_dep)`.

### Leer una consulta y decir qué falla

| Sentencia | Qué pasa | Por qué |
|---|---|---|
| `SELECT nombre FROM empleados WHERE salario = MAX(salario);` | Error | Un agregado no puede ir en el `WHERE` (epígrafe 7); se resuelve con una subconsulta: `WHERE salario = (SELECT MAX(salario) FROM empleados)` |
| `SELECT nombre FROM empleados WHERE id_dep = NULL;` | No devuelve ninguna fila | La comparación con nulo da nulo, no verdadero; lo correcto es `IS NULL` |
| `SELECT id_dep, COUNT(*) FROM empleados WHERE COUNT(*) > 5 GROUP BY id_dep;` | Error | La condición sobre el grupo va en `HAVING COUNT(*) > 5`, después del `GROUP BY` |
| `SELECT salario * 14 AS anual FROM empleados WHERE anual > 30000;` | Error | El alias se define en el `SELECT`, que se procesa después del `WHERE`; sí podría usarse en el `ORDER BY` |
| `UPDATE empleados SET salario = 2000;` | Cambia el salario de todos | Falta el `WHERE` |
| `DELETE FROM departamentos WHERE id_dep = 3;` con empleados en ese departamento y la clave ajena con `ON DELETE RESTRICT` | Error | `RESTRICT` impide borrar la fila referenciada; con `CASCADE` se borrarían también esos empleados |

### Escoger la sentencia

| Tarea | Sentencia | Familia |
|---|---|---|
| Añadir la columna `email` a `empleados` | `ALTER TABLE empleados ADD COLUMN email varchar(100);` | DDL |
| Vaciar una tabla de registros de pruebas sin borrarla | `TRUNCATE TABLE pruebas;` (o `DELETE FROM pruebas;`) | DDL (o DML) |
| Eliminar la tabla y su estructura | `DROP TABLE pruebas;` | DDL |
| Subir un 2 % el salario del departamento 3 | `UPDATE empleados SET salario = salario * 1.02 WHERE id_dep = 3;` | DML |
| Permitir a un usuario consultar `empleados` sin modificarla | `GRANT SELECT ON empleados TO usuario;` | DCL |
| Retirarle ese permiso | `REVOKE SELECT ON empleados FROM usuario;` | DCL |
| Deshacer los cambios aún no confirmados | `ROLLBACK;` | TCL |
| Saber cuántos empleados hay | `SELECT COUNT(*) FROM empleados;` | DQL |

### Completar una consulta con agrupación

Enunciado: los departamentos con más de cinco empleados y su salario medio, del más alto al más
bajo, contando sólo a los dados de alta desde 2020.

```sql
SELECT d.nombre, COUNT(*) AS plantilla, AVG(e.salario) AS media
FROM empleados e
JOIN departamentos d ON e.id_dep = d.id_dep
WHERE e.alta >= DATE '2020-01-01'          -- filtro de filas: antes de agrupar
GROUP BY d.nombre
HAVING COUNT(*) > 5                        -- filtro de grupos: después de agrupar
ORDER BY media DESC;                       -- el alias sí vale en ORDER BY
```

Cada pieza responde a una parte del enunciado: la fecha es una condición de fila (`WHERE`); «más de
cinco empleados» es una condición de grupo (`HAVING`); el salario medio es un agregado (`AVG`); el
orden, `ORDER BY … DESC`. Un `LEFT JOIN` no cambiaría el resultado aquí, porque el `HAVING` exige
empleados; sí lo cambiaría si se pidieran también los departamentos sin empleados, que con `LEFT JOIN`
desde `departamentos` saldrían con `COUNT(e.id_emp)` igual a cero (con `COUNT(*)` contarían una fila,
la completada con nulos), siempre que la condición de fecha pase al `ON`: en el `WHERE`, `e.alta` nulo
da nulo y esas filas se eliminan.

## Lo que este tema no da, y dónde está

- El texto de la norma ISO/IEC 9075: es de pago y no se ha leído. Lo que el tema dice de ella procede
  de la documentación de PostgreSQL, Oracle y Microsoft. Por eso no se dan las fechas de la primera
  norma ANSI ni de la primera ISO, ni la edición vigente de cada parte en el catálogo de ISO, ni si la
  norma usa los rótulos DDL, DML o DQL.
- El nombre completo de la ACM: Oracle la llama «Association of Computer Machinery», y la página de la
  asociación no se pudo leer (acceso bloqueado).
- La administración de un gestor concreto (instalación, copias de seguridad, usuarios, ajuste del
  rendimiento) y los lenguajes procedimentales (PL/SQL, Transact-SQL, SQL/PSM) más allá de su mención:
  el enunciado no los pide. Las copias de seguridad en general están en el tema 3.
- Las bases de datos no relacionales: sólo se nombran sus familias, como oficio.
- La normalización más allá de la tercera forma normal y el diseño entidad-relación: el enunciado no
  los pide; las tres formas normales se dan como teoría de oficio, sin fuente leída.
- Funciones de ventana, consultas recursivas (`WITH RECURSIVE`), tipos y funciones de fecha y de texto
  de cada gestor: no se desarrollan.
- La seguridad de las bases de datos frente a ataques (inyección de SQL, cifrado): tema 14.
- Qué gestores de bases de datos usa la RTVA o CSRTV: no consta en ningún documento publicado.

## Trazabilidad

Todas las páginas se leyeron el 05-10-2026, en su versión en línea de ese día, salvo las tres de PostgreSQL 18 que se marcan como leídas el 06-10-2026.

| Fuente | Qué sostiene |
|---|---|
| PostgreSQL 18, «Appendix D. SQL Conformance» (postgresql.org/docs/current/features.html) | Nombre formal ISO/IEC 9075, SQL:2023, ediciones anteriores, niveles de SQL-92, funciones Core, partes de la norma, 177/170, ningún gestor declaraba, al escribirse la página, el Core de SQL:2023 entero |
| Oracle AI Database 23, *SQL Language Reference*: «SQL Standards», «History of SQL», «Types of SQL Statements» (docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/) | ANSI e ISO/IEC, normas técnicamente idénticas; SQL como sublenguaje de datos, por conjuntos, optimizador, SQL/PSM y PL/SQL, tareas, portabilidad; Codd, SEQUEL, 1979; las seis categorías de Oracle, DDL con `GRANT`/`REVOKE`, `SELECT` como forma limitada de DML, control de transacciones, confirmación implícita del DDL |
| Oracle AI Database 23, *Concepts*, cap. 1 «Introduction to Oracle AI Database» | Base de datos, SGBD y sus elementos, primera generación, modelo relacional, relación/tupla/atributo, independencia lógica y física, objeto-relacional, SQL declarativo, «ANSI standard language» |
| PostgreSQL 18, tutorial: «Concepts», «Introduction», «Joins Between Tables», «Aggregate Functions», «Transactions» | Relación y tabla, columnas tipadas, filas sin orden, otras organizaciones; extensiones de la norma; combinaciones internas y externas; agregados, `WHERE` frente a `HAVING`, subconsulta; transacciones, `BEGIN` implícito, puntos de guardado |
| PostgreSQL 18, referencia: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`, `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `TRUNCATE`, `CREATE VIEW`, `CREATE INDEX`, `GRANT`, `REVOKE`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`; cap. 5.5 «Constraints»; cap. 8 «Data Types»; cap. 9 «Comparison», «Logical Operators», «Pattern Matching», «Aggregate Functions», «Subquery Expressions», «Date/Time Functions» | Sintaxis, descripción y compatibilidad con la norma de cada sentencia; restricciones y acciones `ON DELETE`; tipos de la norma y qué guarda cada uno; operadores, `BETWEEN`, `LIKE`, nulos y lógica de tres valores, agregados, `IN`, `EXISTS`, `ANY`/`SOME`, `ALL` y `NOT IN`; dependencia funcional en `GROUP BY` y lo que la norma añade; `USING` y `NATURAL`; `CURRENT_DATE` |
| PostgreSQL 18, referencia: `BEGIN` y `START TRANSACTION` (leídas el 06-10-2026) | `START TRANSACTION` como sentencia de la norma, `BEGIN` como extensión equivalente, inicio implícito de la transacción en la norma |
| PostgreSQL 18, cap. 7.4 «Combining Queries (`UNION`, `INTERSECT`, `EXCEPT`)» (leído el 06-10-2026) | Compatibilidad para la unión: mismo número de columnas y tipos compatibles |
| Microsoft Learn, en castellano: «Transact-SQL declaraciones», «SELECT (Transact-SQL)», «TOP (Transact-SQL)», «TRUNCATE TABLE (Transact-SQL)», «UPDATE (Transact-SQL)», «GRANT (Transact-SQL)», «Transacciones (Transact-SQL)», «Guía de versiones de fila y bloqueo de transacciones» (learn.microsoft.com/es-es/sql/…, versión `sql-server-ver17` de la documentación) | DDL y DML en castellano, instrucciones de permisos; orden lógico de procesamiento del `SELECT` y alias; `TOP` y su paréntesis; `TRUNCATE` frente a `DELETE` en el registro; `UPDATE` sin `WHERE`; `GRANT`; modos de transacción; ACID |

La traducción automática de Microsoft trae erratas (palabras desordenadas, espacios antes del punto);
se citan tal cual con [sic]. Las citas en inglés llevan detrás, en redonda, la traducción del tema.

Oficio sin fuente detrás, y así se declara: la clasificación didáctica en cinco familias (DDL, DML,
DQL, DCL y TCL) y su cuadro; la tabla que separa base de datos y sistema gestor; la regla «estructura, DDL; datos, DML» y el consejo para el test sobre
`SELECT`; la correspondencia entre las tareas de Oracle y las familias; la tabla de nombres corrientes
y formales del modelo relacional; la distinción entre diseño lógico y físico; las tres formas
normales; la tabla de familias no relacionales y sus ejemplos; el cuadro `DROP`/`TRUNCATE`/`DELETE`; la regla de
escribir en la forma de la norma para que la sentencia sea portable; y los ejemplos con nombres en
castellano (`empleados`, `departamentos`, `cuentas`), que no se han ejecutado en ningún gestor. Los
ejemplos con nombres en inglés (`films`, `weather`, `orders`) son de la documentación de PostgreSQL.
