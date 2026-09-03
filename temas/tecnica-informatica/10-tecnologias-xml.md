# Tema 10 del específico de Técnica Informática · El lenguaje de marcado extensible y su familia

Las siglas de este tema, presentadas de entrada: el lenguaje de marcado extensible (**XML**,
*extensible markup language*); la definición de tipo de documento (**DTD**, *document type
definition*); el lenguaje de hojas de estilo extensible (**XSL**) y su parte de transformación
(**XSLT**); el lenguaje de rutas de XML (**XPath**) y el de consulta (**XQuery**); la notación de
objetos de JavaScript (**JSON**, *JavaScript Object Notation*); el lenguaje de marcado de hipertexto
(**HTML**); y el formato de documento portátil (**PDF**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 12):
> «Tecnologías XML: XSL, DTD, Schema, XPATH, X-QUERY, JSON etc.»

**Cuatro preguntas.** **Y las cuatro son de vocabulario**: **qué es cada pieza de la familia y para
qué sirve.**

**El punto tiene una virtud para el opositor**: **es cerrado.** **La familia son seis nombres, cada
uno hace una cosa distinta y ninguno se solapa con otro.** **Con una tabla se contestan las cuatro.**

<!-- indice -->

## Índice

- [1. Qué es XML y qué gana con serlo](#1-qué-es-xml-y-qué-gana-con-serlo)
- [2. La familia entera, en una tabla](#2-la-familia-entera-en-una-tabla)
- [3. JSON](#3-json)
- [4. Los datos que el examen ha preguntado](#4-los-datos-que-el-examen-ha-preguntado)
- [5. Trazabilidad](#5-trazabilidad)

<!-- /indice -->

## 1. Qué es XML y qué gana con serlo

**La pregunta 1 es negativa**: **de las enumeradas, la que NO es una ventaja de utilizar XML es que
tenga una sintaxis muy rígida y poco flexible.** Ésa es la respuesta oficial.

---

**Y es la pregunta más fácil del punto si se lee despacio**: **las otras tres opciones son elogios y
la marcada es un defecto.** **No hace falta saber nada de XML: basta ver que «rígida y poco flexible»
no es una ventaja de nada.**

**Lo que sí conviene tener claro, porque el matiz existe**: **XML es estricto en su sintaxis** —toda
etiqueta se cierra, todo atributo va entrecomillado— **y a la vez extensible en su vocabulario**:
**las etiquetas las inventa quien lo usa.** **Esa combinación es lo que la respuesta oficial llama
mal «rígida», y lo que las opciones a, b y d llaman bien «entendible», «intercambiable» y
«extensible».**

**Las tres ventajas reales, que son las tres opciones falsas de la pregunta:**

| Ventaja | Por qué |
|---|---|
| **Legible por máquinas y personas** | **Es texto plano con etiquetas con nombre** |
| **Facilita el intercambio entre sistemas** | **No depende de plataforma ni de lenguaje** |
| **Extensible y personalizable** | **Cada dominio define su propio vocabulario de etiquetas** |

## 2. La familia entera, en una tabla

**Ésta es la tabla que contesta el punto:**

| Tecnología | Qué hace |
|---|---|
| **DTD** | **Define la estructura permitida** de un documento, con sintaxis propia ✔ |
| **Schema (XSD)** | **Define la estructura permitida**, con sintaxis XML y con tipos de dato |
| **XPath** | **Consulta y selecciona nodos** dentro de un documento ✔ |
| **XQuery** | **Consulta como un lenguaje completo**, y construye resultados nuevos |
| **XSL / XSLT** | **Transforma** un documento XML en otro formato: HTML, PDF, otro XML |
| **JSON** | **No es de la familia**: es un formato de datos alternativo, más ligero |

**La pregunta 89**: **un DTD en XML es una definición de tipo de documento.** Ésa es la respuesta
oficial.

**La pregunta 78**: **la función principal de XPath es consultar y seleccionar nodos dentro de un
documento XML.** Ésa es la respuesta oficial.

---

**Las dos se contestan con la tabla, y sus opciones falsas son las filas vecinas**: **la opción a de
la 78 es lo que hace XSLT y la d es lo que hacen DTD y Schema.** **El examen construye los
distractores repartiendo las funciones de la familia**, y por eso la tabla entera es la preparación
del punto.

**La diferencia entre DTD y Schema, que es lo preguntable de lo que no ha caído:**

| | **DTD** | **Schema** |
|---|---|---|
| **En qué está escrito** | **Sintaxis propia**, distinta de XML | **En XML** |
| **Tipos de dato** | **No los tiene** | **Sí: número, fecha, cadena con restricciones** |
| **Espacios de nombres** | **No los admite** | **Sí** |
| **Cuál se usa hoy** | **El heredado** | **El recomendado** |

## 3. JSON

**La pregunta 48**: **JSON es el acrónimo de *JavaScript Object Notation*.** Ésa es la respuesta
oficial.

---

**Y las tres opciones falsas son la misma expresión con una palabra cambiada** —*Java's*, *Online*,
*Nomination*—, **lo que convierte la pregunta en memoria literal.** **El único apoyo es que las tres
palabras correctas son las obvias: JavaScript, objeto y notación.**

**Y una precisión que conviene tener aunque no la pregunten**: **JSON nació de la sintaxis de objetos
de JavaScript pero no depende de él.** **Hoy lo leen y escriben todos los lenguajes**, igual que XML.

**Los dos formatos, uno frente a otro, porque el enunciado los mete en el mismo punto:**

| | **XML** | **JSON** |
|---|---|---|
| **Cómo marca** | **Con etiquetas de apertura y cierre** | **Con llaves, corchetes y pares de nombre y valor** |
| **Tamaño** | **Mayor**: cada dato lleva su etiqueta dos veces | **Menor** |
| **Validación** | **DTD y Schema, maduros** | **JSON Schema, más reciente** |
| **Comentarios** | **Sí** | **No los admite** |
| **Dónde manda hoy** | **Documentos, configuración, intercambio entre empresas** | **Interfaces web y aplicaciones** |

**La regla que resume la comparación**: **XML describe documentos y JSON transporta datos.** **Los dos
sirven para lo mismo y cada uno se defiende mejor en su terreno.**

## 4. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 1 | Cuál NO es una ventaja de utilizar XML | c) Tiene una sintaxis muy rígida y poco flexible ✔ |
| 48 | De qué es acrónimo JSON | d) *JavaScript Object Notation* ✔ |
| 78 | Función principal de XPath | b) Consultar y seleccionar nodos de un documento XML ✔ |
| 89 | Qué es un DTD en XML | b) Una definición de tipo de documento ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **la tabla del epígrafe 2 es el punto entero.** **Seis filas, y con ellas se
contestan dos preguntas y se reconocen los distractores de las otras dos.**

## 5. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Tres declaraciones expresas:**

1. **Las recomendaciones del consorcio que publica XML, XSLT, XPath, XQuery y Schema no se han
   consultado.** **Lo que cada una hace es de uso universal**, y **coincide con las respuestas
   oficiales de las preguntas 78 y 89.**
2. **La forma larga de JSON procede de la propia respuesta oficial de la pregunta 48**, reproducida
   de ella.
3. **La comparación entre XML y JSON del epígrafe 3 es oficio.** **Ninguna pregunta depende de
   ella**, y **el temario no atribuye esas afirmaciones a ninguna fuente.**

**El resto del tema va como oficio y así se declara**: la observación de que la pregunta 1 se contesta
sin saber XML, la precisión sobre en qué es estricto y en qué es extensible, la tabla que enfrenta DTD
con Schema y la regla de que XML describe documentos y JSON transporta datos. **Nada de eso está en un
boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
