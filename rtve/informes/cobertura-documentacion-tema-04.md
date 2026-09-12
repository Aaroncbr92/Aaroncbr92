# Cobertura del tema 4 del específico de Documentación

**Siglas de este informe**: el Instituto Nacional de Normas y Tecnología de los Estados Unidos
(**NIST**).

**Prueba del apartado 7 del manual**: se contestan las preguntas reales con el tema delante, y
donde el tema no llegue **se amplía el tema, nunca se recorta la pregunta**.

- **Tema**: Inteligencia artificial aplicada a contenidos sonoros y audiovisuales.
- **Preguntas de la materia**: **4**.
- **Contestadas con el tema delante**: **4**.
- **Lagunas que hubo que cerrar**: **una**, la de la diarización.
- **Preguntas verificadas en la fuente**: **2 de 4**. Es **la proporción más baja del bloque**, y el
  informe de refutación explica por qué no es descuido.

## Una por una

| Cuadernillo · nº | Respuesta | Qué la sostiene | Nivel de la fuente | Epígrafe |
|---|---|---|---|---|
| 09 · 36 | b | Sólo la plantilla oficial | **Plantilla** | 1.1 |
| 09 · 37 | c | Sólo la plantilla oficial | **Plantilla** | 2.1 |
| 09 · 79 | b | «"Who Spoke When" speaker diarization» | **NIST**, evaluaciones de transcripción enriquecida | 1.2 |
| 09 · 88 | a | «Bidirectional Encoder Representations from Transformers» / «looking at the words that come before and after it» | **Google**, anuncio oficial | 2.2 |

## La laguna que se cerró, y con qué

**La diarización no tiene definición normativa en español.** No está en el BOE, no está en las normas
de documentación reunidas para el tema anterior y no está en el vocabulario de ninguna de las
recomendaciones internacionales del proyecto.

La ruta que funcionó fue **un programa público de evaluación**: el instituto nacional de normas y
tecnología de los Estados Unidos lleva desde 2002 midiendo sistemas de transcripción enriquecida, y
para medirlos **tuvo que nombrar las tareas**. La suya se llama, literalmente, «**"Who Spoke When"
speaker diarization**».

**Y esa fórmula de tres palabras vale más que una definición**, porque contiene las dos mitades del
problema: **quién** —agrupar los segmentos de un mismo hablante, sin saber su nombre— y **cuándo**
—marcar los tramos—. Es exactamente lo que dice la respuesta correcta del examen.

**La misma página regaló la pieza que completa el cuadro**: en las mismas evaluaciones aparece
«**"Who Said What" speaker diarization**», que ya no sólo separa hablantes sino que **les atribuye
sus palabras**. Tener las dos juntas es lo que evita confundir diarización con transcripción.

## Dónde el tema tuvo que ampliarse

**Las dos preguntas sin fuente se contestaban con la plantilla, y contestar no es explicar.**

- **El módulo generativo prosódico.** El tema no se limita a decir «síntesis de voz»: separa las
  cuatro opciones en **las que analizan un sonido que ya existe** —reconocimiento, verificación— y
  **la que lo fabrica**, y explica **por qué la prosodia sólo hay que generarla al hablar**: al
  escuchar, la entonación **ya viene en la señal**; al leer un texto en voz alta, **no está en
  ninguna parte** y hay que decidirla. La palabra que resuelve la pregunta es **«generativo»**. Y
  añade que el **sistema de respuesta vocal** es **de otra categoría**: no es una tecnología del
  habla, es un servicio que las usa.
- **El recuento de palabras.** El tema da la regla —**token es ocurrencia, tipo es forma**— y
  después el razonamiento que basta para acertar sin saberla: **de los cuatro recuentos, sólo el de
  tokens puede devolver el mismo número que entró**, porque es el único que **no agrupa ni
  descarta**. Y coloca los otros dos como lo que son: **palabras vacías y significativas son
  complementarias**, y su suma es el texto entero.

## La parte del temario que el examen no tocó

El punto tiene **tres apartados** y el examen preguntó por dos. El tercero es **la visión
artificial**, y es el que más afecta a un archivo audiovisual. El tema lo desarrolla señalando que
sus tres tecnologías —**reconocimiento facial, de lugares y de escenas**— forman **una escalera de
dificultad**: una cara es un objeto delimitado, un lugar exige reconocer un conjunto, una escena
exige interpretar qué pasa. Y que en un archivo sirven para lo mismo: **generar automáticamente los
puntos de entrada que un documentalista marcaría a mano**.

También aclara **las tres tecnologías del habla del primer apartado**, que suelen confundirse:
**reconocimiento** es señal a palabras, **transcripción** es ese resultado puesto en documento, y
**diarización** es quién habló cuándo.

## Lo que este tema deja dicho que no puede sostener

- **Dos de las cuatro respuestas se apoyan sólo en la plantilla.** No hay norma que describa los
  módulos de un sintetizador ni que defina «palabra token»; se ha buscado en todo el corpus.
- **La biblioteca de recomendaciones de la unión internacional de telecomunicaciones no respondió**
  a ninguna de las tres consultas de ese día, cuando sí había respondido en el bloque de Producción.
  Se hace constar por si en otra sesión vuelve a estar en pie.
- **De los tres nombres falsos de la última pregunta no se ha verificado ninguno.**

## Lo que no se ha preguntado y conviene no descuidar

Que la diarización tiene **dos variedades** en las evaluaciones oficiales; que **tipos y tokens miden
la riqueza léxica**; que lo **bidireccional** del modelo de Google es **mirar las palabras de antes y
las de después**, frente a leer de izquierda a derecha; y que el propio anuncio cifra su efecto en
**una de cada diez búsquedas** y lo atribuye sobre todo a **las preposiciones**, que es justo lo que
un buscador antiguo tiraba a la basura.
