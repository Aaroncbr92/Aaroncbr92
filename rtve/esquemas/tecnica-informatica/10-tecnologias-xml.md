# Esquema · Tema 10 del específico de Técnica Informática · El lenguaje de marcado extensible y su familia

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de tratamiento de datos ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: el lenguaje de marcado extensible (**XML**);
la definición de tipo de documento (**DTD**); el lenguaje de hojas de estilo extensible (**XSL**) y su
parte de transformación (**XSLT**); el lenguaje de rutas de XML (**XPath**) y el de consulta
(**XQuery**); la notación de objetos de JavaScript (**JSON**); el lenguaje de marcado de hipertexto
(**HTML**); y el formato de documento portátil (**PDF**).

**Cabecera.** Enunciado: punto 12 del anexo · **4 preguntas** · **ninguna lleva figura** · **las
cuatro son de vocabulario** · **la virtud del punto es que es cerrado**: **seis nombres, cada uno hace
una cosa distinta y ninguno se solapa con otro.**

<!-- indice -->

## Índice

- [Qué es XML](#qué-es-xml)
- [La familia entera](#la-familia-entera)
- [JSON](#json)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es XML

- **PREGUNTA 1** · `[exam]` · **La que NO es ventaja de XML es tener una sintaxis muy rígida y poco
  flexible.**
- **ES LA MÁS FÁCIL DEL PUNTO SI SE LEE DESPACIO**: **las otras tres son elogios y la marcada es un
  defecto.** **No hace falta saber nada de XML.**
- **EL MATIZ QUE SÍ EXISTE**: **XML es estricto en su sintaxis** —toda etiqueta cerrada, todo atributo
  entrecomillado— **y extensible en su vocabulario**: **las etiquetas las inventa quien lo usa.**

| Ventaja | Por qué |
|---|---|
| **Legible por máquinas y personas** | **Es texto plano con etiquetas con nombre** |
| **Facilita el intercambio entre sistemas** | **No depende de plataforma ni de lenguaje** |
| **Extensible y personalizable** | **Cada dominio define su vocabulario** |

## La familia entera

| Tecnología | Qué hace |
|---|---|
| **DTD** | **Define la estructura permitida**, con sintaxis propia ✔ |
| **Schema (XSD)** | **Define la estructura permitida**, en XML y con tipos de dato |
| **XPath** | **Consulta y selecciona nodos** dentro del documento ✔ |
| **XQuery** | **Consulta como lenguaje completo**, y construye resultados nuevos |
| **XSL / XSLT** | **Transforma** el documento en otro formato: HTML, PDF, otro XML |
| **JSON** | **No es de la familia**: formato alternativo, más ligero |

- **PREGUNTA 89** · `[exam]` · **Un DTD es una definición de tipo de documento.**
- **PREGUNTA 78** · `[exam]` · **La función de XPath es consultar y seleccionar nodos.**
- **LOS DISTRACTORES SON LAS FILAS VECINAS**: **en la 78, una opción es lo que hace XSLT y otra lo que
  hacen DTD y Schema.** **El examen reparte las funciones de la familia**, y por eso la tabla entera
  es la preparación del punto.

| | **DTD** | **Schema** |
|---|---|---|
| **En qué está escrito** | **Sintaxis propia** | **En XML** |
| **Tipos de dato** | **No** | **Sí**: número, fecha, cadena con restricciones |
| **Espacios de nombres** | **No** | **Sí** |
| **Cuál se usa hoy** | **El heredado** | **El recomendado** |

## JSON

- **PREGUNTA 48** · `[exam]` · **JSON es el acrónimo de *JavaScript Object Notation*.**
- **LAS TRES FALSAS SON LA MISMA EXPRESIÓN CON UNA PALABRA CAMBIADA** —*Java's*, *Online*,
  *Nomination*—: **memoria literal.** **El único apoyo es que las tres palabras correctas son las
  obvias.**
- **LA PRECISIÓN**: **JSON nació de la sintaxis de objetos de JavaScript pero no depende de él.**
  **Hoy lo leen y escriben todos los lenguajes**, igual que XML.

| | **XML** | **JSON** |
|---|---|---|
| **Cómo marca** | **Etiquetas de apertura y cierre** | **Llaves, corchetes y pares de nombre y valor** |
| **Tamaño** | **Mayor**: cada dato lleva su etiqueta dos veces | **Menor** |
| **Validación** | **DTD y Schema, maduros** | **JSON Schema, más reciente** |
| **Comentarios** | **Sí** | **No los admite** |
| **Dónde manda hoy** | **Documentos, configuración, intercambio entre empresas** | **Interfaces web y aplicaciones** |

- **LA REGLA QUE RESUME LA COMPARACIÓN**: **XML describe documentos y JSON transporta datos.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 1 | Cuál NO es ventaja de XML | c) Sintaxis muy rígida y poco flexible ✔ |
| 48 | De qué es acrónimo JSON | d) *JavaScript Object Notation* ✔ |
| 78 | Función principal de XPath | b) Consultar y seleccionar nodos ✔ |
| 89 | Qué es un DTD | b) Definición de tipo de documento ✔ |

**Las cuatro oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**la tabla de la familia es el punto entero.** **Seis filas: contestan dos preguntas y descubren los
distractores de las otras dos.**
