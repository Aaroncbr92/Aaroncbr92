# Esquema · Tema 1 del específico de Técnica Informática · Bases de datos y el modelo relacional

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de bases de datos · `[exam]` =
opciones del propio cuadernillo. **Siglas**: el sistema de gestión de bases de datos (**SGBD**); el
lenguaje de consulta estructurado (**SQL**) y sus cuatro sublenguajes —definición (**DDL**),
manipulación (**DML**), control (**DCL**) y control de transacciones (**TCL**)—; y las propiedades de
una transacción: atomicidad, consistencia, aislamiento y durabilidad (**ACID**).

**Cabecera.** Enunciado: puntos 1 y 2 del anexo · **7 preguntas** · **ninguna lleva figura** ·
**las siete se contestan con vocabulario: ninguna pide diseñar nada.**

<!-- indice -->

## Índice

- [Base de datos y gestor no son lo mismo](#base-de-datos-y-gestor-no-son-lo-mismo)
- [Relacional y no relacional](#relacional-y-no-relacional)
- [El vocabulario del modelo relacional](#el-vocabulario-del-modelo-relacional)
- [Normalización y diseño](#normalización-y-diseño)
- [Los cuatro sublenguajes](#los-cuatro-sublenguajes)
- [La sintaxis que el examen pide](#la-sintaxis-que-el-examen-pide)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Base de datos y gestor no son lo mismo

| Término | Qué es |
|---|---|
| **Base de datos** | **El conjunto de datos**, estructurado y almacenado |
| **Sistema de gestión de bases de datos** | **El programa que la crea, la consulta y la protege** |

- **PREGUNTA 7** · `[exam]` · **El que NO es un sistema de gestión de bases de datos es Apache
  TomCat.**
- **POR QUÉ** · `[of]` · **TomCat es un contenedor de aplicaciones web** —ejecuta páginas y servicios
  escritos en Java, y vuelve en el tema 9—; **MySQL, MariaDB y PostgreSQL son gestores relacionales.**
- **LA REGLA QUE RESUELVE ESTA FAMILIA**: **si de cuatro nombres tres son claramente hermanos, el
  cuarto es la respuesta.** **No hace falta saber qué es TomCat.**

## Relacional y no relacional

- **PREGUNTA 10** · `[exam]` · **La que NO es relacional es MongoDB.**

| Familia | Cómo guarda | Ejemplos |
|---|---|---|
| **Relacional** | **Tablas con filas y columnas**, esquema fijo | **MySQL**, **MariaDB**, **PostgreSQL**, **Oracle**, **SQL Server**, **H2** |
| **Documental** | **Documentos**, cada uno con su estructura | **MongoDB** ✔ |
| **Clave-valor** | **Pares de clave y valor** | **Redis** |
| **Columnar** | **Por columnas**, para analítica | **Cassandra** |
| **De grafos** | **Nodos y aristas** | **Neo4j** |

- **LO QUE UNE A LAS NO RELACIONALES NO ES UNA TECNOLOGÍA**: **es que ninguna obliga a un esquema fijo
  de tablas.**
- **EL AVISO**: **H2 despista por poco conocido y es relacional** —escrito en Java, se usa embebido y
  en pruebas—. **MongoDB gana porque es la única documental de las cuatro.**

## El vocabulario del modelo relacional

| Corriente | Formal | Qué es |
|---|---|---|
| **Tabla** | **Relación** | **El conjunto de datos de una misma clase** |
| **Fila o registro** | **Tupla** | **Un elemento concreto** |
| **Columna o campo** | **Atributo** | **Una propiedad** |

- **PREGUNTA 17** · `[exam]` · **Lo que se ingresa dentro de una tabla son los registros.**
- **LAS TRES FALSAS —«datos», «informaciones», «textos»— NO SON TÉRMINOS DEL MODELO**: son palabras
  corrientes. **La pregunta mide vocabulario técnico.**
- **CLAVE PRIMARIA**: **identifica sin ambigüedad cada fila; ni se repite ni queda vacía.**
- **CLAVE AJENA**: **apunta a la clave primaria de otra tabla.** **Es lo que crea la relación.**

## Normalización y diseño

| Forma normal | Qué exige |
|---|---|
| **Primera** | **Ningún campo con varios valores**: nada de listas en una celda |
| **Segunda** | **Primera + todo campo depende de la clave primaria entera** |
| **Tercera** | **Segunda + ningún campo depende de otro que no sea la clave** |

- **PARA QUÉ SIRVE, EN UNA LÍNEA**: **evitar que el mismo dato esté escrito en dos sitios**, porque
  **cuando está en dos sitios acaba diciendo dos cosas distintas.**
- **DISEÑO LÓGICO**: **qué tablas hay y cómo se relacionan, sin mirar el gestor.**
- **DISEÑO FÍSICO**: **cómo se guardan en disco: tipos, índices, particiones.** **El primero es
  independiente del producto; el segundo no.**
- **NO SE HA PREGUNTADO**, y va porque el anexo la nombra.

## Los cuatro sublenguajes

| Sublenguaje | Para qué | Sentencias |
|---|---|---|
| **DDL** | **Crear y modificar la estructura** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | **Trabajar con los datos de dentro** | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | **Dar y quitar permisos** | `GRANT`, `REVOKE` |
| **TCL** | **Confirmar o deshacer cambios** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

- **PREGUNTA 12** · `[exam]` · **La sentencia de la categoría DDL es `CREATE`.**
- **PREGUNTA 47** · `[exam]` · **`SELECT`, `INSERT`, `UPDATE` y `DELETE` son las básicas del DML.**
- **SON LA MISMA PREGUNTA CON LA RESPUESTA CAMBIADA DE SITIO**, y **una línea las contesta las dos**:
  **si toca la ESTRUCTURA es DDL; si toca los DATOS es DML.**
- **EL MATIZ QUE DESPISTA**: **`DROP` elimina la tabla entera con su estructura y es DDL; `DELETE`
  borra filas y deja la tabla en pie y es DML; `TRUNCATE` la vacía sin borrar su estructura y se
  clasifica como DDL**, porque no opera fila a fila.

## La sintaxis que el examen pide

- **PREGUNTA 13** · `[exam]` · **`SELECT * FROM nombreTabla;`**
- **PREGUNTA 24** · `[exam]` · **`SELECT COUNT(*) FROM tabla`**
- **EL ASTERISCO SIGNIFICA «TODAS LAS COLUMNAS»**, y **`COUNT` cuenta filas.**

| Función | Qué devuelve |
|---|---|
| **`COUNT`** | **Cuántas filas** ✔ |
| **`SUM`** | **La suma de una columna numérica** |
| **`AVG`** | **La media** |
| **`MAX`** y **`MIN`** | **El mayor y el menor** |

- **DE AHÍ SALEN SOLAS LAS FALSAS DE LA 24**: **`SUM(*)` y `MAX(*)` no significan nada** y **`ROWS()`
  no existe.**
- **EL ORDEN DE UNA CONSULTA, PARA LLEVARLO MEMORIZADO:**

```
SELECT columnas
FROM tabla
WHERE condición de fila
GROUP BY columnas de agrupación
HAVING condición de grupo
ORDER BY columnas de ordenación
```

- **LA DISTINCIÓN MÁS PREGUNTABLE DE LA FAMILIA**: **`WHERE` filtra filas antes de agrupar; `HAVING`
  filtra grupos después.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 7 | Cuál NO es un gestor de bases de datos | a) Apache TomCat ✔ |
| 10 | Cuál no es relacional | d) MongoDB ✔ |
| 12 | Sentencia de la categoría DDL | b) `CREATE` ✔ |
| 13 | Cómo se seleccionan todos los registros | a) `SELECT * FROM nombreTabla;` ✔ |
| 17 | Cómo se llama lo que se ingresa en una tabla | d) Registros ✔ |
| 24 | Instrucción para contar registros | a) `SELECT COUNT(*) FROM tabla` ✔ |
| 47 | Sublenguaje de `SELECT`, `INSERT`, `UPDATE`, `DELETE` | a) DML ✔ |

**Las siete oficiales son correctas** · **ninguna descansa en la plantilla** · **ninguna sale de una
norma: este punto es oficio y vocabulario.** · **Aviso de estudio**: **el cuadro de los cuatro
sublenguajes contesta dos preguntas enteras y ayuda en dos más.** **Es lo más rentable del punto.**
