# Tema 1 del específico de Técnica Informática · Bases de datos y el modelo relacional

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · puntos 1 y 2 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia son las bases de datos y el lenguaje de consulta, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Extensión** | **1.876 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el sistema de gestión de bases de datos (**SGBD**);
el lenguaje de consulta estructurado (**SQL**, *structured query language*) y sus cuatro sublenguajes
—el de definición de datos (**DDL**, *data definition language*), el de manipulación (**DML**, *data
manipulation language*), el de control (**DCL**, *data control language*) y el de control de
transacciones (**TCL**, *transaction control language*)—; y el conjunto de propiedades de una
transacción: atomicidad, consistencia, aislamiento y durabilidad (**ACID**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, puntos 1 y 2):
> «1. Bases de datos: Terminología, conceptos y tipos.»
>
> «2. Administración y gestión de bases de datos relacionales. El Modelo Relacional. Normalización,
> diseños lógico y físico. El Lenguaje SQL.»

**Siete preguntas.** **Y las siete se contestan con vocabulario**: **ninguna pide diseñar nada, y
todas piden saber cómo se llama cada cosa.**

**Su reparto**: **cuatro son de lenguaje SQL**, **dos son de reconocer un producto que no es lo que
la pregunta dice** y **una es de terminología del modelo relacional.**

<!-- indice -->

## Índice

- [1. Qué es una base de datos y qué es un gestor](#1-qué-es-una-base-de-datos-y-qué-es-un-gestor)
- [2. Los tipos de base de datos](#2-los-tipos-de-base-de-datos)
- [3. El modelo relacional y su terminología](#3-el-modelo-relacional-y-su-terminología)
- [4. La normalización](#4-la-normalización)
- [5. El lenguaje SQL y sus cuatro sublenguajes](#5-el-lenguaje-sql-y-sus-cuatro-sublenguajes)
- [6. La sintaxis que el examen pide](#6-la-sintaxis-que-el-examen-pide)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Qué es una base de datos y qué es un gestor

**Los dos términos se confunden en la conversación y el examen los separa:**

| Término | Qué es |
|---|---|
| **Base de datos** | **El conjunto de datos**, estructurado y almacenado |
| **Sistema de gestión de bases de datos** | **El programa que la crea, la consulta y la protege** |

**La pregunta 7 mide exactamente esa distinción, y por eliminación**: **de las cuatro opciones, la que
NO es un sistema de gestión de bases de datos es Apache TomCat.** Ésa es la respuesta oficial.

---

**Por qué**: **TomCat es un contenedor de aplicaciones web**, es decir, **el programa que ejecuta
páginas y servicios escritos en Java**, y aparecerá otra vez en el tema 9. **MySQL, MariaDB y
PostgreSQL son los tres gestores relacionales libres más extendidos.**

**La regla que resuelve esta familia de preguntas**: **si de cuatro nombres tres pertenecen
claramente a la misma categoría, el cuarto es la respuesta.** **No hace falta saber qué es TomCat: basta
con reconocer que los otros tres son hermanos.**

## 2. Los tipos de base de datos

**La pregunta 10**: **de las enumeradas, la base de datos que NO es relacional es MongoDB.** Ésa es la
respuesta oficial.

---

**La división que hay detrás, que es la del punto 1 del anexo:**

| Familia | Cómo guarda los datos | Ejemplos |
|---|---|---|
| **Relacional** | **En tablas con filas y columnas**, con relaciones entre ellas y esquema fijo | **MySQL**, **MariaDB**, **PostgreSQL**, **Oracle**, **SQL Server**, **H2** |
| **Documental** | **En documentos**, cada uno con su propia estructura | **MongoDB** |
| **Clave-valor** | **En pares de clave y valor** | **Redis** |
| **Columnar** | **Por columnas**, para consultas analíticas | **Cassandra** |
| **De grafos** | **En nodos y aristas** | **Neo4j** |

**Las cuatro últimas familias se agrupan bajo el nombre común de no relacionales**, y **lo que las une
no es una tecnología: es que ninguna obliga a un esquema fijo de tablas.**

**El aviso que hay que llevar**: **H2 despista porque es poco conocido**, y **es relacional**: un
gestor escrito en Java que suele usarse embebido en la propia aplicación y en pruebas. **La respuesta
correcta es MongoDB porque es la única documental de las cuatro.**

## 3. El modelo relacional y su terminología

**El modelo relacional organiza los datos en tablas**, y **cada palabra tiene nombre formal y nombre
corriente**, que el examen mezcla:

| Nombre corriente | Nombre formal | Qué es |
|---|---|---|
| **Tabla** | **Relación** | **El conjunto de datos de una misma clase** |
| **Fila o registro** | **Tupla** | **Un elemento concreto de esa clase** |
| **Columna o campo** | **Atributo** | **Una propiedad de esa clase** |

**La pregunta 17**: **el conjunto de datos o información que se ingresa dentro de una tabla son los
registros.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas —«datos», «informaciones» y «textos»— no son términos del modelo**:
**son palabras del lenguaje corriente.** **La pregunta mide si se conoce el vocabulario técnico, y la
única de las cuatro que lo es, es «registros».**

**Las dos claves que ordenan una tabla, porque el examen puede pedirlas:**

- **Clave primaria**: **el atributo o conjunto de atributos que identifica sin ambigüedad cada fila.**
  **No puede repetirse ni quedar vacía.**
- **Clave ajena**: **el atributo que apunta a la clave primaria de otra tabla.** **Es lo que crea la
  relación**, y de ahí el nombre del modelo.

## 4. La normalización

**El anexo la nombra y el examen no la ha preguntado**, y **conviene tenerla vista porque es la teoría
del punto 2:**

| Forma normal | Qué exige |
|---|---|
| **Primera** | **Que ningún campo contenga varios valores**: nada de listas dentro de una celda |
| **Segunda** | **Primera, y además que todo campo dependa de la clave primaria entera**, no de una parte |
| **Tercera** | **Segunda, y además que ningún campo dependa de otro campo que no sea la clave** |

**Para qué sirve, en una línea**: **evitar que el mismo dato esté escrito en dos sitios**, porque
**cuando está en dos sitios, tarde o temprano dice dos cosas distintas.**

**Y el diseño en dos pasos que el anexo también nombra**: **el diseño lógico decide qué tablas hay y
cómo se relacionan, sin mirar el gestor**; **el diseño físico decide cómo se guardan en disco: tipos
concretos, índices, particiones.** **El primero es independiente del producto y el segundo no.**

## 5. El lenguaje SQL y sus cuatro sublenguajes

**Cuatro de las siete preguntas son de aquí**, y **todas se contestan con este cuadro:**

| Sublenguaje | Para qué | Sentencias |
|---|---|---|
| **DDL, de definición** | **Crear y modificar la estructura**: tablas, índices, vistas | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML, de manipulación** | **Trabajar con los datos que hay dentro** | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL, de control** | **Dar y quitar permisos** | `GRANT`, `REVOKE` |
| **TCL, de transacciones** | **Confirmar o deshacer un conjunto de cambios** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

**La pregunta 12**: **de las enumeradas, la sentencia SQL que pertenece a la categoría DDL es
`CREATE`.** Ésa es la respuesta oficial.

**La pregunta 47**: **`SELECT`, `INSERT`, `UPDATE` y `DELETE` son las sentencias básicas del DML.** Ésa es la
respuesta oficial.

---

**Las dos preguntas son la misma con la respuesta cambiada de sitio**, y **la regla que las contesta
las dos es de una línea**: **si la sentencia toca la ESTRUCTURA, es DDL; si toca los DATOS, es DML.**
**`CREATE` crea una tabla; `DELETE` borra filas de una tabla que ya existe.**

**El matiz que a veces despista**: **`DROP` y `DELETE` parecen lo mismo y no lo son.** **`DROP` elimina la
tabla entera, con su estructura, y es DDL; `DELETE` borra filas y deja la tabla vacía en pie, y es
DML.** **`TRUNCATE` vacía la tabla sin borrar su estructura y se clasifica como DDL**, porque no opera
fila a fila.

## 6. La sintaxis que el examen pide

**La pregunta 13**: **en SQL, todos los registros de una tabla se seleccionan con
`SELECT * FROM nombreTabla;`.** Ésa es la respuesta oficial.

**La pregunta 24**: **el número de registros de una tabla se cuenta con
`SELECT COUNT(*) FROM tabla`.** Ésa es la respuesta oficial.

---

**Las dos piden lo mismo: reconocer la forma de una consulta.** **El asterisco significa «todas las
columnas»**, y **`COUNT` es la función de agregación que cuenta filas.**

**Las funciones de agregación que el examen puede pedir, porque las opciones falsas las mezclan:**

| Función | Qué devuelve |
|---|---|
| **`COUNT`** | **Cuántas filas** ✔ |
| **`SUM`** | **La suma de una columna numérica** |
| **`AVG`** | **La media** |
| **`MAX`** y **`MIN`** | **El mayor y el menor valor** |

**Y de ahí salen solas las opciones falsas de la 24**: **`SUM(*)` y `MAX(*)` no tienen sentido**
—sumar o maximizar «todas las columnas» no significa nada—, **y `ROWS()` no existe.**

**La estructura completa de una consulta, por orden, que es lo que conviene llevar memorizado:**

```
SELECT columnas
FROM tabla
WHERE condición de fila
GROUP BY columnas de agrupación
HAVING condición de grupo
ORDER BY columnas de ordenación
```

**La distinción entre `WHERE` y `HAVING` es la que más se pregunta en esta familia**: **`WHERE` filtra
filas antes de agrupar y `HAVING` filtra grupos después.**

## 7. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 7 | Cuál NO es un sistema de gestión de bases de datos | a) Apache TomCat ✔ |
| 10 | Cuál de las bases de datos no es relacional | d) MongoDB ✔ |
| 12 | Sentencia SQL de la categoría DDL | b) `CREATE` ✔ |
| 13 | Cómo se seleccionan todos los registros de una tabla | a) `SELECT * FROM nombreTabla;` ✔ |
| 17 | Cómo se llama lo que se ingresa dentro de una tabla | d) Registros ✔ |
| 24 | Instrucción para contar los registros de una tabla | a) `SELECT COUNT(*) FROM tabla` ✔ |
| 47 | De qué sublenguaje son `SELECT`, `INSERT`, `UPDATE` y `DELETE` | a) DML ✔ |

**Las siete respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **el cuadro de los cuatro sublenguajes de SQL contesta dos preguntas enteras
y ayuda en dos más.** **Es lo más rentable del punto, y se aprende en cinco minutos.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **La norma internacional que define el lenguaje SQL no se ha consultado**: su texto está tras un
   muro de pago. **La clasificación en cuatro sublenguajes, la sintaxis de las consultas y las
   funciones de agregación son de uso universal**, y **coinciden con las respuestas oficiales.**
2. **Los nombres de producto que el tema cita —MySQL, MariaDB, PostgreSQL, H2, MongoDB, Redis,
   Cassandra, Neo4j y Apache TomCat— se reproducen de las opciones del examen o se nombran como
   ejemplos corrientes de su familia.** **No se ha consultado la documentación de ninguno**, y **el
   temario no les atribuye ninguna característica que no sea la de su categoría.**
3. **Las tres formas normales del epígrafe 4 son teoría clásica del modelo relacional**, presentada
   como conocimiento común. **Ninguna pregunta depende de ellas**, y así consta.
4. **La distinción entre diseño lógico y físico procede del propio enunciado del anexo**, que los
   nombra, y **se desarrolla como oficio.**

**El resto del tema va como oficio y así se declara**: la distinción entre base de datos y gestor, la
regla de que tres nombres hermanos delatan al cuarto, la tabla de familias de bases de datos, el
vocabulario formal del modelo relacional, la diferencia entre `DROP`, `DELETE` y `TRUNCATE` y la que separa
`WHERE` de `HAVING`. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
