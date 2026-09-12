# Refutación · Enfermería de Empresa, los veinticinco temas del específico

**Siglas de este informe**: el Instituto Nacional de Seguridad y Salud en el Trabajo (**INSST**), que
hasta 2019 se llamó Instituto Nacional de Seguridad e Higiene en el Trabajo (**INSHT**); sus notas
técnicas de prevención (**NTP**); y la prevención de riesgos laborales (**PRL**).

**Las cinco lentes del proyecto pasadas sobre los veinticinco temas y sus veinticinco esquemas**, y lo
que sale de la comprobación contra las fuentes.

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **Aplicable en veinte temas.** **223 negritas comprobadas, 0 no literales** |
| `refutar_citas` | Cada tramo en negrita dentro de un bloque de cita, como subcadena literal del volcado | **Aplicable en los veinticinco.** **724 tramos comprobados, 0 no literales** |
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los veinticinco temas y en los veinticinco esquemas |
| `refutar_prosa` | Relleno, frases repetidas y siglas sin presentar | **Cero hallazgos** en los veinticinco temas y en los veinticinco esquemas |
| `refutar_documento` | Cada negrita contra un documento no articulado, y cada cifra en negrita contra el conjunto de fuentes | **7.699 negritas comprobadas.** **Cero cifras huérfanas** en los veinticinco temas |

**Los cinco temas en que la lente de exactitud no encuentra ancla —el 3, el 12, el 13, el 14 y el 23—
son los que no citan articulado**: se apoyan en documentos del Instituto o del Ministerio, que no
numeran por artículos. **Ese cero no significa «todo correcto»: significa «no he mirado nada»**, y por
eso los cinco quedan cubiertos por la lente de citas, que en ellos comprueba 153 tramos.

## Dos lentes hubo que arreglarlas por el camino

**Los PDF del Instituto parten las palabras al final del renglón con un guion blando, U+00AD**, que es
invisible y que la extracción de texto conserva. **Una cita copiada literalmente salía marcada como no
literal por un motivo puramente tipográfico**, y eso adiestra a no mirar la lista, que es donde se
esconde el hallazgo de verdad. **Se enseñó a `refutar_citas` y a `refutar_documento` a coserlo**, igual
que ya cosían el guion normal. **La regresión se comprobó sobre los temas 8, 23 y 24, cerrados antes
del cambio: sin variación.**

**Y hay un límite conocido de la lente de exactitud que este volumen volvió a encontrar**: **ancla en
marcadores del tipo «Artículo N» y descarta expresamente las remisiones a normas ajenas** —«el artículo
20 de la Ley…»—, para no comprobar una negrita contra el artículo equivocado. **La consecuencia es que
un tema escrito enteramente con remisiones nombradas devuelve cero.** El tema 25 lo hizo, y se
reescribieron sus entradillas para que la lente tuviera dónde anclar.

## Trece hallazgos en las fuentes

**Todos comprobados a ojo sobre el documento original**, ampliando la página en el propio archivo, para
descartar que fueran un fallo de la extracción automática. **Ninguno lo es: están impresos así.**

| Tema | Fuente | Qué se ha encontrado |
|---:|---|---|
| 8 | **NTP** 218 | **Cinco resultados de sus ejemplos resueltos no salen de sus fórmulas**: una errata de signo, un descuido de transcripción, un rótulo repetido y **dos valores teóricos, 85.00 y 3.02, que no salen de ninguna manera** —la fórmula da 79.87 y 3.82, y la propia tabla de la nota calculó su porcentaje con 3.82— |
| 8 | **NTP** 218 | **Se fecha en 1995 y es de 1988** |
| 9 | Cuadro de enfermedades profesionales | **El texto consolidado escribe «plumón» donde debe decir «pulmón»**, en la entrada del amianto. Quien busque «pulmón» no encontrará esa entrada |
| 12 | «Indicadores de salud 2020» | **Su texto y su propia tabla 3.5.1 no dan las mismas cifras** del índice de frecuencia: 2,00 frente a 22,0, y 32,1 frente a 32,2 |
| 14 | Material docente del Instituto | **La tabla 2, la de casos y controles, imprime «b+c» como total de una columna que contiene b y d.** Es la tabla con la que se calcula la razón de posibilidades |
| 16 | Real Decreto 664/1997 | **Dos erratas del texto consolidado**: «un **seno** peligro» por «un serio peligro», y «**corno** consecuencia» por «como consecuencia» |
| 25 | **NTP** 458 | **Su figura, rotulada como los mínimos del anexo VI del Real Decreto 486/1997, imprime, en mayúsculas, «gases estériles» donde la norma dice «gasas estériles»** |
| 25 | **NTP** 458 | **Se fecha en 1995 y cita el Real Decreto 1627/1997, de 24 de octubre** |
| 25 | **NTP** 467 | **Se fecha en 1995**, su número de publicación oficial es de 1998 y su bibliografía cita un libro de 1998 |
| 25 | **NTP** 469 | **Se fecha en 1995**; la **NTP** 546 la cita como de 1997 y el catálogo del Instituto también |
| 25 | **NTP** 546 | **Imprime «Año: 0...»**: el campo del año no llegó a componerse, y así lleva veinticinco años |
| 25 | **NTP** 524 | **Imprime «ducha durante 2030 minutos»** donde el resto del documento escribe «20-30 minutos» |
| 25 | Real Decreto 365/2009 | **Su artículo 7, titulado «Garantías de mantenimiento», cierra con un párrafo sin numerar que establece el régimen sancionador.** Es la única mención a infracciones de toda la norma |

**Dos observaciones sobre esa lista.**

**La primera**: **seis de los trece son fechas mal impresas**, y no es una pedantería. **La advertencia
que todas esas notas llevan estampada dice que, para valorar la pertinencia de sus recomendaciones, «es
conveniente tener en cuenta su fecha de edición».** **La fuente pide que se mire un dato que ella misma
da mal.**

**La segunda**: **ninguna de las erratas de transcripción se corrige dentro de la cita.** Una
transcripción no corrige a su fuente. Lo que hace el temario es citarlas tal como están, decir lo que
evidentemente quieren decir, y **fuera de la cita escribir la palabra correcta**.

## Tres divergencias entre fuentes oficiales, declaradas

Son de otra clase que las erratas: **aquí no hay nada mal impreso; hay dos documentos oficiales que no
dicen lo mismo**, y el temario tiene que elegir y declarar por qué.

1. **El torniquete.** La **NTP** 469 admite dos supuestos —que fallen los otros métodos, o **que haya
   más de un accidentado y el socorrista esté solo**—; la guía de socorrismo laboral de 2014 conserva
   sólo el primero. **El tema 25 sigue a la nota por ser el documento monográfico y declara la
   divergencia**, porque el segundo supuesto es un criterio de triaje y no de hemostasia.
2. **La profilaxis antitetánica.** El criterio de la **NTP** 568, de 2000, **quedó desplazado por la
   tabla 3 de «Recomendaciones de Vacunación en Población Adulta»** del Ministerio de Sanidad, que
   distingue por número de dosis recibidas y **exige inmunoglobulina en heridas de alto riesgo con
   independencia de la historia vacunal**, cosa que la nota ni menciona. **El tema 25 da la tabla
   vigente y explica las tres diferencias.**
3. **La reanimación.** El catálogo del propio Instituto marca la **NTP** 605, de 2001, como
   **actualizada por la 1.062**, de 2015. **El tema 25 sigue sólo a la 1.062** y **cita la 605
   únicamente para decir que sus ritmos y su comprobación del pulso carotídeo ya no rigen.** Ninguno de
   sus datos se reproduce como vigente.

## Y una comprobación que salió bien

**No todo lo que se comprueba sale mal, y decirlo forma parte de comprobar.**

- **La cita del apartado 1 del artículo 195 del Código Penal** que hace la guía de socorrismo laboral
  se contrastó con el texto consolidado del boletín en la redacción vigente a la fecha de corte:
  **coincide palabra por palabra**.
- **La regla de los nueve de Wallace** de la **NTP** 524 se sumó entera: **da exactamente cien**, y sus
  dos desgloses internos —el de la extremidad superior y el de la inferior— también cuadran.
- **Las constantes de los índices de siniestralidad** que el tema 13 toma de la **NTP** 1.211
  coinciden con las fichas técnicas de los indicadores del Sistema Nacional de Salud que usa el tema
  12, en los dos índices que ambas fuentes publican.

## Estado final

**Cinco lentes a cero en los veinticinco temas y en los veinticinco esquemas.** **Cero cifras
huérfanas.** **Trece hallazgos y tres divergencias declarados en el cuerpo de los temas donde
aparecen**, no escondidos en este informe.
