# Tema 4 del específico de Documentación · Inteligencia artificial aplicada a contenidos sonoros y audiovisuales

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Documentación · punto 4 |
| **Sirve para** | **Documentación** |
| **Fuente** | **Sin norma en el enunciado, y sin norma en el BOE.** Las dos preguntas que tienen fuente se apoyan en el **instituto nacional de normas y tecnología de los Estados Unidos**, que define la tarea de diarización en sus evaluaciones, y en el **blog oficial de Google**, que anunció el modelo de lenguaje que la otra pregunta nombra |
| **Identificador** | Evaluación **Rich Transcription** del **NIST** · anuncio oficial de **Google** de 25/10/2019 · artículo **arXiv 1810.04805** |
| **Redacción que se estudia** | Las páginas y documentos **tal como estaban el 02/09/2026** |
| **Aviso sobre las fuentes** | **Es el tema con menos respaldo documental del bloque, y el más corto.** De sus **4 preguntas**, **2 tienen documento detrás**; las **2 restantes** —el módulo generativo prosódico y el recuento de palabras— se apoyan **sólo en la plantilla oficial**, y van marcadas. **No hay norma publicada** que defina estos términos: se ha buscado en todo el corpus del proyecto |
| **Extensión** | **2.664 palabras** |

<!-- /portada -->

> **Enunciado de la convocatoria (Anexo 2, temario específico de Documentación, punto 4):**
> «INTELIGENCIA ARTIFICIAL APLICADA A CONTENIDOS SONOROS Y AUDIOVISUALES: 4.1. Tecnologías del
> lenguaje: reconocimiento automático de voz, diarización, transcripción de voz a texto · 4.2. Visión
> artificial: reconocimiento facial, de lugares y de escenas · 4.3. Procesamiento del lenguaje
> natural: clasificación automática, reconocimiento de entidades y palabras clave, resumen automático
> de textos.»

**Cuatro preguntas**, y **el tema peor servido de fuentes de todo el bloque**. Conviene decir por qué,
porque no es descuido: **la inteligencia artificial aplicada a los medios no tiene todavía norma
publicada**. No hay ley en el BOE que defina la diarización, ni recomendación internacional que diga
qué módulos tiene un sintetizador de voz. Lo que sí hay son **dos clases de documento fiable**: los
**programas de evaluación de organismos públicos de normalización**, que definen las tareas porque
tienen que medirlas, y los **anuncios técnicos de quien construye los sistemas**.

**Las siglas del tema, presentadas antes de empezar** (el enunciado no las trae, pero el examen sí):
el procesamiento del lenguaje natural (**PLN**), y el modelo de lenguaje por el que se pregunta,
**BERT**, que sus autores desarrollan como se verá más abajo.

| Nivel | Qué sostiene en este tema |
|---|---|
| **2 · Organismo de normalización** | El **instituto nacional de normas y tecnología de los Estados Unidos**, cuyas evaluaciones de transcripción enriquecida definen la **diarización** con una fórmula de tres palabras |
| **4 · Documentación de quien lo fabrica** | El **anuncio oficial de Google**, que explica qué hace su modelo de lenguaje en el buscador, y **la ficha del artículo científico** donde el modelo se presentó |
| **5 · La plantilla oficial** | El **módulo generativo prosódico** y el **recuento de palabras**. Van marcados |

---

<!-- indice -->

## Índice

- [1. Tecnologías del habla](#1-tecnologías-del-habla)
  - [1.1 Quién genera y quién sólo analiza](#11-quién-genera-y-quién-sólo-analiza)
  - [1.2 La diarización](#12-la-diarización)
- [2. Procesamiento del lenguaje natural](#2-procesamiento-del-lenguaje-natural)
  - [2.1 Palabras tipo y palabras token](#21-palabras-tipo-y-palabras-token)
  - [2.2 El modelo de lenguaje del buscador](#22-el-modelo-de-lenguaje-del-buscador)
- [3. Lo que el temario pide y el examen no preguntó](#3-lo-que-el-temario-pide-y-el-examen-no-preguntó)
- [4. Los datos que el examen ha preguntado](#4-los-datos-que-el-examen-ha-preguntado)
- [5. Trazabilidad](#5-trazabilidad)

<!-- /indice -->

## 1. Tecnologías del habla

### 1.1 Quién genera y quién sólo analiza

**La respuesta oficial**: la tecnología del habla que tiene un **módulo generativo prosódico** es la
**síntesis de voz**.

**La pregunta se resuelve con una sola distinción, y hay que verla antes que el vocabulario**: de las
cuatro tecnologías que ofrece, **tres analizan un sonido que ya existe y una lo fabrica**.

| Tecnología | Qué hace con el sonido |
|---|---|
| **Reconocimiento de voz** | **Lo analiza**: entra audio, sale texto |
| **Verificación del locutor** | **Lo analiza**: entra audio, sale un sí o un no sobre quién habla |
| **Sistema de respuesta vocal** | **Lo usa**: es una aplicación completa —un contestador automático que atiende llamadas—, no una tecnología del habla elemental |
| **Síntesis de voz** | **Lo fabrica**: entra texto, sale audio |

**Y la prosodia es algo que sólo hace falta fabricar.** La prosodia es lo que no está en las letras:
**la entonación, el acento, el ritmo y las pausas**. Cuando una máquina **escucha**, la prosodia ya
viene dada en la señal —puede medirla, pero no tiene que inventarla—. Cuando una máquina **habla** a
partir de un texto escrito, **la prosodia no está en ninguna parte** y hay que decidirla: dónde sube
el tono, dónde se acentúa, dónde se calla. **Ese es el módulo generativo prosódico**, y por eso sólo
puede estar en el sintetizador.

**La palabra que resuelve la pregunta es «generativo».** Los tres distractores tienen módulos, y
algunos incluso analizan prosodia; pero **generar prosodia** es una tarea que sólo tiene sentido en
el sistema que produce voz.

**El tercer distractor merece una nota**, porque es de otra categoría: un **sistema de respuesta
vocal** no es una tecnología del habla, es **un servicio que las usa** —normalmente reconocimiento y
síntesis a la vez—. Quien lo elija está eligiendo el conjunto en vez de la pieza.

**Nivel de la fuente**: **plantilla oficial**. La arquitectura interna de un sintetizador de voz **no
está normalizada en ninguna de las fuentes reunidas**, y las que podrían tenerla no se han podido
consultar: la biblioteca de recomendaciones de la unión internacional de telecomunicaciones **no
respondió a ninguna de las tres consultas** hechas ese día —la misma biblioteca de la que sí se
descargaron otras recomendaciones para el bloque de Producción—, y la recomendación del consorcio de
la web sobre marcado de síntesis de voz responde «prohibido», igual que el resto de su sitio.
Comprobado con agente de usuario de navegador.

### 1.2 La diarización

**La respuesta oficial**: la diarización es **el proceso de dividir un audio en segmentos
correspondientes a cada hablante**.

**Y hay una fórmula oficial de tres palabras que la define mejor que cualquier definición**: el
instituto nacional de normas y tecnología de los Estados Unidos, que lleva desde 2002 evaluando
sistemas de transcripción enriquecida, llama a esa tarea «**"Who Spoke When" speaker diarization**»
—diarización de locutores, «quién habló cuándo»—.

**Léase la fórmula despacio, porque contiene las dos mitades del problema**: «**quién**» —agrupar los
segmentos de un mismo hablante, aunque el sistema no sepa su nombre— y «**cuándo**» —marcar en qué
tramos del audio habla cada uno—. Es exactamente lo que dice la respuesta correcta.

La misma fuente da **la pieza que completa el cuadro**, y que conviene no confundir con ésta: en sus
evaluaciones aparece también la tarea «**"Who Said What" speaker diarization**» —quién dijo qué—, que
ya no sólo separa hablantes sino que **atribuye a cada uno sus palabras**. **Quién habló cuándo
separa; quién dijo qué transcribe y atribuye.**

Las tres opciones falsas, y qué son en realidad:

| Opción falsa | Qué describe |
|---|---|
| «Registrar eventos pasados o futuros **en un diario**» | **Juega con el sonido de la palabra.** «Diarización» no viene de *diario*: viene de repartir el audio por turnos de palabra. **Es el distractor bueno**, porque la etimología aparente engaña |
| «Mejorar **la calidad del sonido**» | Es **restauración o realce de audio**, otro proceso |
| «Reconocer automáticamente **el idioma de un texto**» | Es **identificación de idioma**, y además sobre texto, no sobre audio |

**Por qué esto importa en un archivo de televisión.** Porque la diarización es **lo que convierte una
transcripción en un documento consultable**: sin ella, la transcripción automática de una tertulia es
un muro de texto; con ella, cada intervención queda separada y se puede buscar **quién dijo cada
cosa**. Es el paso previo a poder indizar por interviniente.

---

## 2. Procesamiento del lenguaje natural

### 2.1 Palabras tipo y palabras token

**La respuesta oficial**: si al procesar un texto de 3.000 palabras se recuperan **esas mismas 3.000
palabras**, el recuento realizado es de **palabras tokens**.

**La pregunta es una definición disfrazada de aritmética**, y se resuelve viendo que **el número no
ha cambiado**:

| Recuento | Qué cuenta | Qué habría pasado con las 3.000 |
|---|---|---|
| **Palabras token** | **Cada aparición**, una por una. Si «de» sale 200 veces, cuenta 200 | **Salen 3.000**, porque no se ha descartado ni agrupado nada |
| **Palabras tipo** | **Cada forma distinta**, una sola vez. Si «de» sale 200 veces, cuenta 1 | Saldrían **muchas menos**: las formas distintas de un texto son una fracción de sus apariciones |
| **Palabras vacías** | Sólo las que **no aportan significado** —artículos, preposiciones, conjunciones— | Saldría **un subconjunto**, no el total |
| **Palabras significativas** | Sólo las que **sí aportan significado**: el texto menos las vacías | Saldría **otro subconjunto** |

**La regla, y es la que hay que llevar**: **token es ocurrencia, tipo es forma**. Y de las cuatro
opciones, **sólo el recuento de tokens puede devolver el mismo número que entró**, porque es el único
que no agrupa ni descarta.

**Las otras dos van en pareja y conviene tenerlas juntas**: **palabras vacías** y **palabras
significativas** son **complementarias** —el texto entero es la suma de las dos—, y la operación de
quitar las primeras es el filtrado que precede a casi todo análisis. La relación entre tipos y tokens
es, además, **la medida clásica de riqueza léxica** de un texto: cuantos más tipos por token, más
variado el vocabulario.

**Nivel de la fuente**: **plantilla oficial**. Los cuatro términos se han buscado en todo el corpus
del proyecto —incluidas las normas de vocabulario documental reunidas para el tema anterior, que sí
definen *indización*, *término preferente* o *concepto*— y **ninguno aparece**. La norma de
vocabulario fundamental de información y documentación se vende **sin muestra utilizable**, y su
catálogo responde «prohibido». Comprobado con agente de usuario de navegador.

### 2.2 El modelo de lenguaje del buscador

**La respuesta oficial**: el modelo de lenguaje desarrollado por Google para comprender mejor las
búsquedas, analizando el contexto en que aparecen los términos dentro de una oración, es **BERT**.

**El enunciado del examen es casi una traducción del anuncio oficial.** Google lo publicó el **25 de
octubre de 2019** con el título «Understanding searches better than ever before», y allí escribe:
«**Last year, we introduced and open-sourced a neural network-based technique for natural language
processing (NLP) pre-training called Bidirectional Encoder Representations from Transformers, or as
we call it--BERT, for short**».

**Y explica exactamente lo que el enunciado llama «analizar el contexto»**: «**This breakthrough was
the result of Google research on transformers: models that process words in relation to all the other
words in a sentence, rather than one-by-one in order**», de modo que «**BERT models can therefore
consider the full context of a word by looking at the words that come before and after it**».

**Las palabras que come antes y después.** Ésa es la palabra «bidireccional» del nombre, y es lo que
distingue a este modelo de los anteriores: no lee la frase de izquierda a derecha, **la lee entera**.
La ficha del artículo donde se presentó lo dice con los mismos términos: «**We introduce a new
language representation model called BERT, which stands for Bidirectional Encoder Representations
from Transformers**», diseñado «**by jointly conditioning on both left and right context in all
layers**».

**Y el propio anuncio dice para qué sirve en el buscador**, que es lo que la pregunta describe:
«**when it comes to ranking results, BERT will help Search better understand one in 10 searches in
the U.S. in English**», sobre todo en «**longer, more conversational queries, or searches where
prepositions like "for" and "to" matter a lot to the meaning**».

**Ahí está la clave de por qué un modelo así cambia una búsqueda**: las preposiciones. Antes, un
buscador podía tratarlas como ruido; con un modelo que mira la frase entera, **un «para» o un «desde»
cambian el resultado**, que es como funciona el lenguaje de verdad.

Las tres opciones falsas son **nombres del mundo de los buscadores**, y ahí está su gracia: ninguna
es un disparate. Dos de ellas son apodos de cambios del algoritmo de búsqueda, del tipo que la
industria bautiza y que la propia empresa rara vez confirma; y la tercera es **el nombre de un
sistema de indexación**, no de un modelo de lenguaje. **Lo que ninguna de las tres es, es un modelo
de lenguaje**, y ésa es la distinción que la pregunta mide.

**Nivel de la fuente**: **documentación de quien lo fabrica** —el anuncio oficial de la empresa— y
**ficha del artículo científico** donde el modelo se presentó. **De los tres nombres falsos no se ha
verificado ninguno**: lo que este tema dice de ellos es uso profesional, y va marcado.

---

## 3. Lo que el temario pide y el examen no preguntó

El punto 4 tiene **tres apartados** y el examen tocó **dos**. El tercero —la **visión artificial**—
no salió, y conviene tenerlo porque es el que más directamente afecta a un archivo audiovisual.

**Lo que el enunciado enumera es una escalera de dificultad**: **reconocimiento facial**, **de
lugares** y **de escenas**. La escalera va de lo concreto a lo abstracto —una cara es un objeto
delimitado; un lugar exige reconocer un conjunto; una escena exige interpretar qué está pasando—, y
en un archivo se usan para lo mismo: **generar automáticamente los puntos de entrada que un
documentalista tendría que marcar a mano**.

**Y el primer apartado también da más de lo que el examen preguntó.** Sus tres tecnologías —
**reconocimiento automático de voz**, **diarización** y **transcripción de voz a texto**— **no son
sinónimos y suelen confundirse**:

- **Reconocimiento automático de voz**: convertir señal en palabras.
- **Transcripción de voz a texto**: el producto de lo anterior **puesto en forma de documento**, con
  su puntuación y su formato.
- **Diarización**: **quién habló cuándo**, que es lo que las otras dos no hacen.

**Las tres juntas son lo que convierte un fondo sonoro en un fondo buscable**, y ése es el uso que
justifica que este punto esté en un temario de documentación y no en uno de ingeniería.

---

## 4. Los datos que el examen ha preguntado

Cuatro preguntas. Todas se contestan con el tema delante:

| Materia | Dato preguntado | Nivel |
|---|---|---|
| Tecnologías del habla | El módulo generativo prosódico es de la **síntesis de voz** | Plantilla oficial |
| Procesamiento del lenguaje | Recuperar las mismas palabras es contar **tokens** | Plantilla oficial |
| Tecnologías del habla | **Diarización** = dividir el audio por hablante | **Instituto de normas de los Estados Unidos**, evaluaciones de transcripción enriquecida |
| Procesamiento del lenguaje | El modelo de Google es **BERT** | **Google**, anuncio oficial |

**Lo que no se ha preguntado y sale gratis del mismo tema**: que la diarización tiene **dos
variedades** en las evaluaciones oficiales —**quién habló cuándo** y **quién dijo qué**—; que
**token es ocurrencia y tipo es forma**, y que su relación mide **la riqueza léxica**; que **palabras
vacías y significativas son complementarias**; que las siglas del modelo de Google significan
**representaciones bidireccionales de codificador a partir de transformadores**, y que lo
bidireccional es **mirar las palabras de antes y las de después**; y que el propio anuncio cifra su
efecto en «**one in 10 searches**».

---

## 5. Trazabilidad

- **«Rich Transcription Evaluation»**, del instituto nacional de normas y tecnología de los Estados
  Unidos, grupo de información multimodal, leída el **3 de septiembre de 2026**: la serie de
  evaluaciones desde 2002 y las dos tareas de diarización, «**Who Spoke When**» y «**Who Said
  What**».
- **«Understanding searches better than ever before»**, blog oficial de Google, publicado el **25 de
  octubre de 2019** y leído el **3 de septiembre de 2026**: el desarrollo de las siglas del modelo,
  la explicación de los transformadores y del contexto bidireccional, y su efecto declarado en el
  buscador.
- **Ficha del artículo «BERT: Pre-training of Deep Bidirectional Transformers for Language
  Understanding»**, arXiv 1810.04805, leída el **3 de septiembre de 2026**: el resumen, con el
  desarrollo de las siglas y la descripción del condicionamiento conjunto por contexto izquierdo y
  derecho.

**Lo que este tema no puede sostener, y por eso lo dice:**

- **La arquitectura del sintetizador de voz se apoya sólo en la plantilla.** No hay norma reunida que
  describa sus módulos. La biblioteca de recomendaciones de la unión internacional de
  telecomunicaciones **no respondió a ninguna de las tres consultas** de ese día, y la recomendación
  del consorcio de la web sobre marcado de síntesis de voz responde «prohibido». Lo que el tema
  explica —qué es la prosodia y por qué sólo hay que generarla al hablar— es **razonamiento**.
- **El recuento de palabras se apoya sólo en la plantilla.** Los cuatro términos se han buscado en
  todo el corpus del proyecto y ninguno aparece; la norma de vocabulario fundamental de información y
  documentación se vende **sin muestra utilizable**.
- **De los tres nombres falsos de la última pregunta no se ha verificado ninguno.** Lo que el tema
  dice de ellos es uso profesional.
- **Este es el tema con menos respaldo documental del bloque**, y no por descuido: **la materia no
  tiene todavía norma publicada**. Las dos fuentes que sí hay son **un programa público de evaluación**
  y **el anuncio de quien construyó el sistema**, y las dos se citan con la fecha en que se leyeron.
