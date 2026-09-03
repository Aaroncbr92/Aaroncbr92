# Refutación · Realización Televisión, los veintidós temas

**Las cuatro lentes del proyecto pasadas sobre los veintidós temas del específico de Realización
Televisión**, y lo que sale de la comprobación cruzada entre los dos cuadernillos y sus fuentes.

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **Aplicable en un solo tema, el 22.** **43 negritas comprobadas, 0 no literales** |
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los veintidós temas |
| `refutar_prosa` | Relleno, frases repetidas y siglas sin presentar | **Cero hallazgos** en los veintidós temas |
| `refutar_documento` | Cada negrita contra el documento no articulado | **No aplicable como lente completa**, y se explica más abajo |

**Veintiuno de los veintidós temas no se apoyan en una norma articulada**, así que la lente de
exactitud **devolvería «0 comprobadas, 0 no literales» en los veintiuno**, y **ese cero no dice nada
sobre el tema**. Es exactamente el aviso del apartado 10 del manual, y por eso la verificación de este
bloque se ha hecho por otros caminos, que este informe documenta uno a uno.

## El único tema con norma articulada: el 22

**El tema de derechos de autor cita dos artículos del texto refundido de la Ley de Propiedad
Intelectual**, y **es el único de la ocupación al que la lente de exactitud se le puede pasar
entera:**

```
refutar_exactitud.py temas/realizacion-tv/22-…md fuentes/corte-20221221/BOE-A-1996-8930.md
negritas comprobadas: 43 ; no literales: 0
```

**Las dos citas, verificadas palabra por palabra contra la norma consolidada vigente el 21 de
diciembre de 2022:**

| Artículo | Cita | Resultado |
|---|---|---|
| **26** | «Los derechos de explotación de la obra durarán toda la vida del autor y setenta años después de su muerte o declaración de fallecimiento.» | **Literal** |
| **127** | «Los derechos de explotación reconocidos a las entidades de radiodifusión durarán cincuenta años, computados desde el día 1 de enero del año siguiente al de la realización por vez primera de una emisión o transmisión.» | **Literal** |

**Y una comprobación de redacciones**: **ninguno de los dos artículos ha sido reformado desde 1996.**
**La redacción vigente al corte es la original**, así que **no hay reforma cruzada que dirimir** —el
apartado 2.2 del manual—.

**Nota de método sobre esta lente y este tema.** **La primera pasada devolvió 41 negritas no
literales**, y **ninguna era un error de cita**: **eran comentario en negrita dentro del bloque
anclado en cada artículo.** **Dentro de un bloque anclado, la negrita promete literalidad**, así que
**la corrección no fue debilitar la lente sino cerrar cada bloque con una raya después de la cita** y
**dejar el comentario fuera.** **Con eso, cero no literales sin tocar una sola palabra de las dos
citas.**

## Las normas que no son articuladas: los reales decretos con anexos y cuadros

**Tres preguntas se apoyan en normas del BOE cuya materia no está en artículos sino en cuadros y
anexos**, y **ahí la lente de exactitud no sirve: se ha sustituido el instrumento**, que es lo que
manda el apartado 5 del manual.

**Cada cita se ha comprobado a mano, buscando la cadena exacta en el volcado de la norma
consolidada:**

| Cita | Fuente | Resultado |
|---|---|---|
| **«luminancia»**, **«Lv»**, **«candela por metro cuadrado»**, **«cd/m2»** | **RD 2032/2009**, cuadro de unidades derivadas | **Las cuatro celdas, literales** |
| **«flujo luminoso»**, **«lumen»**, **«lm»** | **RD 2032/2009**, cuadro de unidades derivadas | **Las tres celdas, literales** |
| **«iluminancia»**, **«lux»**, **«lx»**, **«lm/m2»** | **RD 2032/2009**, cuadro de unidades derivadas | **Las cuatro celdas, literales** |
| **«La candela, símbolo cd, es la unidad SI de intensidad luminosa en una dirección dada.»** | **RD 2032/2009**, apartado 2.7 | **Literal** |
| **«Las barandillas serán de materiales rígidos, tendrán una altura mínima de 90 centímetros y dispondrán de una protección que impida el paso o deslizamiento por debajo de las mismas o la caída de objetos sobre personas.»** | **RD 486/1997**, anexo I, apartado 3.3.º | **Literal** |
| **«La protección no será obligatoria, sin embargo, si la altura de caída es inferior a 2 metros.»** | **RD 486/1997**, anexo I, apartado 3.2.º b) | **Literal** |
| **«2 metros cuadrados de superficie libre por trabajador.»** | **RD 486/1997**, anexo I, apartado 2.1.º b) | **Literal** |

**Una declaración expresa sobre cómo se citan los cuadros.** **Una fila de un cuadro no admite
entrecomillado corrido sin dejar de ser literal**, así que **los temas la citan celda a celda,
separadas por puntos, y lo advierten en el propio texto.** **La frase de la candela, en cambio, es una
cita corrida y va como tal.**

## El hallazgo que ha reordenado dos temas

**Las unidades fotométricas son unidades LEGALES de medida.** **Por tanto están en el Boletín Oficial
del Estado**, y **tres preguntas que este proyecto iba a declarar como oficio se contestan con el
cuadro de un real decreto delante.**

**Se volcó el Real Decreto 2032/2009 en su redacción vigente a la fecha de corte** —con la
modificación del RD 493/2020 ya incorporada, y sin ninguna reforma cruzada detectada— y **se
reescribieron dos temas:**

| Tema | Pregunta | Antes | Ahora |
|---|---|---|---|
| **11** | **55**, el nit | **Oficio** | **Primer nivel: cuadro del RD 2032/2009** |
| **16** | **96**, la luminancia | **Oficio** | **Primer nivel: cuadro del RD 2032/2009** |
| **16** | **111**, el lux | **Oficio** | **Primer nivel: cuadro del RD 2032/2009** |

**El tema 16 pasa a ser, con ese cambio, el único tema de la ocupación del que puede decirse que
NINGUNA de sus nueve respuestas descansa sólo en la plantilla.**

**La lección de método, y vale para todo el proyecto**: **antes de declarar una materia técnica como
oficio, conviene preguntarse si sus magnitudes tienen unidad legal.** **Si la tienen, hay un real
decreto que las define.**

## Lo que se ha verificado con documentación no articulada

**Cinco fuentes de tercer y cuarto nivel, con la cita comprobada literal en cada caso:**

| Cita | Fuente | Nivel | Resultado |
|---|---|---|---|
| **«Una macro es una secuencia de instrucciones que se llevan a cabo automáticamente al presionar un botón.»** | **Manual en español del ATEM de Blackmagic Design** | Cuarto | **Literal** |
| **«Titan LED Engine (RGBMintAmber)»**, **«indoor or outdoor, AC-powered or on battery»**, **«Max. 20h»**, **«on the go with the AsteraApp, with wired or wireless DMX»** | **Ficha del Astera Titan Tube** | Cuarto | **Las cuatro, literales** |
| **«the unit combines up to six IP connections: 4 cellular, WiFi and LAN»** | **Ficha del LiveU LU300S** | Cuarto | **Literal** |
| **«…combine ‘absolute’ marker-based tracking (StarTracker)… to deliver accurate, real-time tracking. Supporting AR graphics workflows and in-camera VFX…»** | **Mo-Sys, «Camera Tracking»** | Cuarto | **Literal** |
| **«Ceiling, wall or floor mounted retro-reflective stickers or digital LED wall markers»** | **Ficha del Mo-Sys StarTracker Max** | Cuarto | **Literal** |
| **«La Federación de Organismos o Entidades de Radio y Televisión Autonómicos»** | **FORTA, «Quiénes somos»** | Tercero | **Literal** |

**Tres de estas fuentes están en inglés y así se citan.** **Lo que se sostiene con ellas son
características que la respuesta oficial enumera, nunca cifras de rendimiento que el temario no
necesita.**

## Por qué `refutar_documento` no cierra este bloque

**La lente de documento compara cada negrita del tema con el texto de un documento no articulado.**
**En veintiuno de los veintidós temas de esta ocupación, ese documento no existe**: la materia es
oficio. **Pasarla devuelve, correctamente, que todas las negritas son no literales**, porque **no hay
fuente contra la que serlo.**

**Ese resultado no es un hallazgo: es la constatación de que el tema va como oficio**, y **así se
declara en cada trazabilidad.** **La lente se ha pasado igualmente sobre los temas con fuente**, y
**las citas comprobadas están en las dos tablas anteriores.**

## Los hallazgos que sí ha habido, y qué se hizo con ellos

**Cuatro, y ninguno se resolvió recortando el tema:**

1. **`refutar_prosa` señaló cinco palabras castellanas en mayúsculas en el tema 13** —AVISAR, FINITO,
   MIRADA, NEUTRO, REPITE— **tomadas por siglas sin presentar.** **Se corrigió el tema**, poniéndolas en
   caja baja, **y se normalizó de paso la capitalización de dos tablas** que mezclaban estilos.
2. **`refutar_prosa` señaló nombres comerciales en mayúsculas en el tema 15** —AVID PROGRAM MIXER,
   PRIME TV, QE PILOT, LIVE EDIT, SGO, IPF—. **Se corrigió el tema**, escribiéndolos con su grafía
   corriente y presentándolos en la cabecera. **Y se hizo una comprobación extra**: **el temario NO les
   atribuye ningún desarrollo de siglas, porque no lo ha verificado**, y **lo dice.**
3. **`refutar_prosa` señaló «en síntesis» en el tema 16 como tejido conectivo.** **Aquí el que detectó
   se equivocó** —apartado 5 del manual—: **«en síntesis aditiva» es el nombre de una mezcla de
   colores, no un conector de discurso.** **Se corrigió LA LENTE**, con una salvedad para «aditiva»,
   «sustractiva» y «cromática», **y se pasó de nuevo sobre los ciento setenta y tres temas del
   proyecto: cero hallazgos.** **Sin la salvedad, el aviso saltaba en todos los temas de color y
   enterraba el relleno que sí lo es.**
4. **`refutar_exactitud` devolvió 41 negritas no literales en el tema 22.** **Ninguna era un error de
   cita**: eran comentario dentro del bloque anclado. **Se cerró cada bloque con una raya después de la
   cita y el comentario quedó fuera.** **Las dos citas no se tocaron.**

## Las trece preguntas que ninguna lente puede refutar

**Trece de las doscientas veintinueve dependen de una imagen que el temario no tiene delante**, y
**sobre ellas ninguna lente puede pronunciarse**: no hay texto que comparar.

**El método que este proyecto aplica, y que aquí se aplica trece veces:**

1. **Declarar que la respuesta descansa en la plantilla oficial.**
2. **NO describir la imagen.** **Describir lo que no se ha visto es inventarlo**, y **un temario que
   inventa una descripción es peor que uno que declara una laguna.**
3. **Aportar la regla de la familia** que hace legible cualquier pregunta de ese tipo: cómo se lee una
   planta acotada, cómo se reconoce un conector, qué comprueba una continuidad, cómo se distingue una
   realidad mixta de una aumentada.

**El tema 13 lleva un epígrafe entero dedicado a las cinco suyas** —«Las cinco preguntas que dependen
de una imagen»—, **que no existía en ningún otro tema del proyecto.**

## Las dos preguntas defectuosas y cómo se han tratado

| Pregunta | El defecto | Qué hace el temario |
|---|---|---|
| **33 (1.er llam.)** | **TRES respuestas igualmente correctas**: *Ben-Hur*, *Titanic* y *El señor de los anillos: el retorno del rey* comparten el récord de once Óscar, **y tres de las cuatro opciones son esas tres películas** | **Manda marcar la de la plantilla sabiendo que está marcada por la plantilla y no por el enunciado**, y **la señala como impugnable.** **Undécima costura del proyecto**, y **no errata de plantilla**: *Ben-Hur* es correcta, sólo que no es la única |
| **67 (1.er llam.)** | **El enunciado pide qué NO se incluye en un magazine y la respuesta afirma que cualquier temática puede incluirse**: **materialmente cierta y no contesta a lo que se pregunta** | **Manda marcarla igual** y **explica que se acierta reconociendo la intención del redactor, no la lógica del enunciado** |

**Ninguna de las dos es errata de plantilla**: **la plantilla es coherente con lo que el redactor
quiso preguntar.** **Las dos son defectos de construcción del enunciado.**

## La contradicción entre dos cuadernillos del mismo proceso

**La pregunta 38 de este cuadernillo y la 28 del de Información Gráfica ordenan las fases del guion de
dos maneras incompatibles**, y **las dos respuestas oficiales son correctas dentro de su propio
examen.**

**No es una errata.** **La terminología del guion no está normalizada**, y **los manuales colocan la
sinopsis y el argumento en órdenes distintos según la escuela.** **Este proyecto sigue en cada
ocupación la convención de SU enunciado y declara la discrepancia en los dos temas**, en lugar de
elegir una y callar la otra.

**Es la tercera vez que este proyecto documenta una divergencia terminológica entre cuadernillos del
mismo proceso selectivo.** **Las otras dos**: **«escena» y «secuencia» frente a «secuencia mecánica» y
«secuencia dramática»**, entre esta ocupación y Edición y Montaje; **y la clasificación de los géneros
informativos**, entre Información y Contenidos y Producción.

## El resultado

**Cero hallazgos de modo y cero de prosa en los veintidós temas.** **Cero negritas no literales en el
único tema con norma articulada.** **Quince entradas de cita comprobadas literales una a una, de
siete fuentes distintas de primer, tercer y cuarto nivel.**

**Y veintinueve afirmaciones que descansan sólo en la plantilla oficial, declaradas una a una en la
trazabilidad de su tema**: **trece dependientes de una imagen, siete de actualidad de premios y
programación, y nueve de producto de fabricante o de término no normalizado.**

**El 87,3 % de las respuestas oficiales de esta ocupación se sostiene con algo más que la plantilla.**
