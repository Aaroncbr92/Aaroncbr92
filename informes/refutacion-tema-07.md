# Refutación del tema 7 del general

**Siglas de este informe**: conformidad europea (**CE**); Comisión Nacional de los Mercados y la
Competencia (**CNMC**); **DEBER** (palabra citada como ejemplo); con sus modalidades de salto de
cuadro (**DF**).

Ley 13/2022, General de Comunicación Audiovisual. Vuelve a ser legislación consolidada, así
que `boe.py` sirve otra vez, pero el tema trajo **dos problemas nuevos**: uno en la fuente y
otro, más grave, en las lentes.

## 0 · Lo que dijo la fuente

Volcada la norma entera —**229 bloques**— en dos versiones, la **vigente hoy** y la **de la
fecha de corte**:

- **La ley no ha sido modificada desde su publicación.** Todos los bloques tienen **una sola
  redacción** y el volcado **no detecta ninguna reforma cruzada**. El texto al corte y el de
  hoy son idénticos. Coincide con lo que dice el propio programa al citar **«texto inicial
  publicado el 08/07/2022»**.
- **Pero quince bloques no estaban en vigor el 21 de diciembre de 2022**: los artículos
  **101 a 109**, **114 a 116** y **140**, más los rótulos que los agrupan. La **disposición
  final novena** escalona la entrada en vigor en ocho reglas distintas.

Eso creó un problema práctico: **el volcado a la fecha de corte omitía esos quince bloques
por completo** —sin rótulo, sin aviso, sin nada—, y el rastro quedaba solo en el
`.redacciones.tsv`. Quien leyera el `.md` vería el artículo 100 seguido del 110 sin señal de
que faltaba algo. **Y el examen pregunta por dos de los omitidos, el 102 y el 115.**

Corregido `boe.py`: cuando un bloque existe en el texto publicado pero su vacatio no ha
vencido a la fecha leída, **el volcado deja el rótulo con el aviso y la fecha de entrada en
vigor**, y el resumen final los enumera aparte. Un hueco en la fuente ya no es invisible.

## 1 · Las lentes devolvieron «0 comprobadas, 0 hallazgos»

Primera pasada sobre el tema: **«negritas comprobadas: 0 ; no literales: 0»** y **«hallazgos:
0»**. Es la firma del apartado 10 del manual, y ya es la tercera vez que aparece en este
temario.

La causa: **el índice de esta ley devuelve los rótulos con espacio duro** —`Artículo\xa02`—,
de modo que el patrón `## \[id\] Artículo (\d+)` no reconocía **ni un solo artículo**. Un
tema de 166 artículos habría pasado la verificación sin que se mirara una línea.

Arreglado eso, la lente empezó a funcionar y destapó **cuatro fallos más, todos suyos**, que
fueron apareciendo en cascada:

| Fallo de la lente | Qué escondía |
| --- | --- |
| No reconocía **«art.» en minúscula** | El tema escribe «art. 98» tanto como «Art. 98»; esos artículos no abrían bloque y su texto se acumulaba en el anterior |
| No reconocía el marcador cerrado en negrita: **`**Art. 22**:`** | Tras el número venía `*`, que no estaba entre los cierres admitidos. **Arts. 22, 27, 29 y muchos más no abrían bloque** |
| El patrón **DEBER** no incluía **«están obligados»** ni **«debiendo»** | Daba por impuesto por el tema lo que la norma sí impone (arts. 98 y 62) |
| Las remisiones **a artículos de otras leyes** abrían bloque | «El **artículo 4** de la Ley 17/2006» abría un bloque que se tragaba el resto del tema |
| **«149.1.27.ª»** abría bloque como si fuera el artículo 27 | Contaminaba el bloque del artículo 27 del tema 1 |

Cada arreglo destapaba el siguiente. El resultado final: de **0 negritas comprobadas** a
**261**, y de **0 hallazgos** a los que se cuentan abajo.

## 2 · Hallazgos reales del tema

| Art. | Qué faltaba o estaba mal |
| --- | --- |
| **1** | El tema solo recogía el apartado 1. Falta el **2**: la ley **fija las normas básicas** de lo autonómico y local, **sin perjuicio de sus competencias**. Es lo que ancla la DF sexta en el art. 149.1.27.ª CE |
| **4** | Faltaba **«en los términos y sin perjuicio de lo previsto en el Código Penal»** |
| **15** | El tema daba **tres** características de los códigos de conducta; **son seis**, y falta el fomento de **códigos de ámbito europeo** |
| **36** | Faltaban los apartados 3 y 4: **no es emisión en cadena** lo coproducido o sindicado **con sindicación mínima del 12 %**, y todo ello **sin perjuicio de la competencia autonómica** |
| **68** | **El tema no recogía la reserva de espectro**: **máximo 25 % del espacio radioeléctrico de televisión estatal y máximo 35 % del radiofónico**. Es uno de los tres artículos de la ley que nombran a RTVE |
| **69** | Tampoco recogía que **los contratos-programa los elabora RTVE y los aprueba el Consejo de Ministros** previo informe de la CNMC y de la Comisión Delegada, ni que **la CNMC supervisa el cumplimiento de la misión de servicio público** |
| **79** | Faltaba **«sin perjuicio de las obligaciones legales o concesionales»** y la salvedad competencial |
| **95** | Faltaba que el tratamiento de datos de menores **queda en todo caso sometido a la normativa de protección de datos** |
| **117** | Faltaba que **en las coproducciones no se contabiliza la aportación del productor independiente** y la regla de cómputo del Fondo, **«salvo indicación en contrario o que la cantidad exceda la inversión»** |
| **123** | **El hallazgo de más peso.** El tema daba la prohibición del alcohol solo por el contenido del mensaje. Faltaban **los apartados 4 y 5**: **más de veinte grados, prohibida salvo entre la 1:00 y las 5:00**; **veinte grados o menos, salvo entre las 20:30 y las 5:00** |

Los tres que más pueden costar una pregunta son **el 68.3** (las dos reservas de espectro,
25 % y 35 %), **el 69** (quién elabora y quién aprueba el contrato-programa) y **el 123.4 y
123.5** (las dos franjas del alcohol por graduación).

## 3 · Cifras

**Ninguna cifra en negrita del tema falta de la ley.** Las cinco que la comprobación numérica
señala son metadatos —la fecha de publicación citada del programa y el recuento de bloques
del volcado—, no afirmaciones sobre el contenido.

## 4 · Lo que la lente sigue marcando, y por qué no se corrige

Quedan **once hallazgos**, todos del mismo tipo: **salvedades de artículos que el tema
resume en una línea**. Son los artículos 26, 31, 37 a 42, 49, 80 a 85, 88 a 91, 93, 141, 142,
143 y 147-148.

**No es un descuido, es una decisión de alcance, y se dice para que se pueda discutir**: la
ley tiene **166 artículos** y el tema desarrolla en detalle los que el examen toca —unos
sesenta— y enumera el resto por su rúbrica. Reproducir las salvedades de los ciento y pico
restantes multiplicaría el tema sin ganar una sola respuesta. Si en una convocatoria futura
el tribunal empezara a preguntar por esos artículos, el arreglo es desarrollarlos, no
silenciar la lente.

## 5 · Prosa

Cero relleno y cero frases repetidas. Una sigla desarrollada (**CNMC**). Los tres avisos
restantes son ruido del detector: **API**, y las palabras **ANUAL** y **SALVO** escritas en
mayúscula por énfasis.

## 6 · Efecto sobre lo ya cerrado

Los arreglos de las lentes obligaban a repasar los cinco temas anteriores. Resultado:

- **Temas 2 y 4**: siguen en **cero hallazgos**, ahora con más negritas comprobadas (176→183
  y 67→67).
- **Tema 5**: los mismos **tres falsos positivos** conocidos, con 499 negritas comprobadas.
- **Tema 1**: **cuatro falsos positivos**, uno más que antes. El nuevo es del artículo 27:
  el bloque del tema se prolonga hasta la cita del **artículo 149.1.27.ª de la Constitución**
  —«sin perjuicio de las **facultades** que en su desarrollo y ejecución correspondan a las
  Comunidades Autónomas»— y la lente lee ahí un cambio de modo verbal que no existe. **No se
  toca el texto**; queda anotado como los otros tres.
- **Ninguno de los arreglos destapó un error de fondo en un tema cerrado**, a diferencia de
  lo ocurrido con el tema 2 al cerrar el 5.

## Resumen

| | Hallazgos | Estado |
|---|---|---|
| Fuente incompleta al corte | **15 bloques omitidos sin aviso** | `boe.py` corregido; ahora deja rótulo y aviso |
| Lentes ciegas | **5 fallos** (espacio duro, «art.» minúscula, marcador en negrita, patrón DEBER, remisiones a otras leyes) | corregidos |
| Hallazgos de fondo en el tema | **10** | corregidos |
| Cifras inventadas | **0** | — |
| Salvedades de artículos resumidos | **11** | límite de alcance, declarado |
| Regresiones en temas cerrados | **0 errores**; 1 falso positivo nuevo en el tema 1 | documentado |
