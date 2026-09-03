# Tema 8 del específico de Sonido · Postproducción, efectos sonoros y estación de trabajo

Los términos y siglas de este tema, presentados de entrada: la estación de trabajo de audio digital
(**DAW**, *digital audio workstation*); el tamaño de la memoria intermedia de la interfaz, medido en
muestras (*buffer*); los pulsos por minuto (**BPM**), que el tema 3 ya presentó; el retardo (*delay*);
la reverberación (*reverb*); los efectos de sonido creados en sala (*Foley*); la banda internacional
sin diálogos (**M&E**, *music and effects*); y el ajuste de un efecto en unidades musicales, que el
oficio llama «a tempo».

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, puntos 6 y 16):
> «POSTPRODUCCIÓN Y EFECTOS SONOROS. Postproducción de sonido. Efectos de sonido y mezcla de pistas
> adicionales. Doblaje de contenidos de ficción, documentales.»
> «OPERACIÓN DAW (ESTACIÓN DE TRABAJO AUDIO DIGITAL). Grabación; edición; sincronización; efectos;
> mezclas.»

**Dos preguntas, y este tema junta dos puntos del anexo** —el 6 y el 16— **porque el examen los trata
como uno solo: sus dos preguntas son cálculos que se hacen dentro de una estación de trabajo.**

**Las dos son de aritmética**, y **eso las hace las más rentables del cuadernillo**: **no hay nada que
memorizar, sólo dos fórmulas.**

<!-- indice -->

## Índice

- [1. El delay a tempo](#1-el-delay-a-tempo)
- [2. La latencia de una estación de trabajo](#2-la-latencia-de-una-estación-de-trabajo)
- [3. La cadena de postproducción de sonido](#3-la-cadena-de-postproducción-de-sonido)
- [4. Los efectos y sus familias](#4-los-efectos-y-sus-familias)
- [5. La sincronización](#5-la-sincronización)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. El delay a tempo

**En una actuación, para un delay de duración de corchea en un tema de 4/4 a 102 pulsos por minuto, la
duración más aproximada del efecto es 294 milisegundos.** Ésa es la respuesta oficial a la pregunta
15.

**La cuenta, en dos pasos:**

1. **La negra dura 60.000 dividido entre los pulsos por minuto.** **60.000 ÷ 102 = 588 milisegundos.**
2. **La corchea vale media negra.** **588 ÷ 2 = 294.**

**Y las cuatro opciones están construidas sobre esos mismos dos números**, que es lo que hace la
pregunta buena:

| Opción | De dónde sale |
|---|---|
| **920** | **No sale de ningún paso**: es el distractor suelto |
| **294** ✔ | **La corchea**: la respuesta |
| **588** | **La NEGRA**: acierta la cuenta y no divide entre dos |
| **204** | **Cifras de 102 barajadas**: el distractor por parecido numérico |

**El aviso de lectura, y es el mismo del tema 1**: **la trampa no está en la fórmula, está en la
figura que se pide.** **Quien calcule la negra y no lea «corchea» marca la c) y se queda a un paso.**

**La tabla que evita la cuenta, para las figuras corrientes a este tempo:**

| Figura | A 102 BPM |
|---|---|
| **Blanca** | **1.176 ms** |
| **Negra** | **588 ms** |
| **Corchea** | **294 ms** |
| **Semicorchea** | **147 ms** |

**Y el porqué de que esto se pregunte en un examen de sonido**: **un delay que no va a tempo se oye
como un error.** **Ajustarlo de oído en un directo no es viable**, así que **se calcula.** **Lo mismo
vale para el tiempo de relajación de un compresor sobre material rítmico y para la predemora de una
reverberación.**

## 2. La latencia de una estación de trabajo

**Si un DAW tiene una configuración de latencia de 128 muestras y la frecuencia de muestreo es de 44,1
kHz, la latencia total en milisegundos se obtiene multiplicando las muestras por mil y dividiendo por
la frecuencia de muestreo.** Ésa es la respuesta oficial a la pregunta 36, **que ofrece fórmulas y no
resultados.**

**El razonamiento**: **la latencia en segundos es el número de muestras dividido entre las muestras
por segundo.** **128 ÷ 44.100 = 0,0029 segundos.** **Para pasarlo a milisegundos se multiplica por
mil: 2,9 milisegundos.**

**Y aquí hay que hacer una precisión que la pregunta no hace, y el temario sí**: **la fórmula marcada
sólo da el resultado correcto si la frecuencia de muestreo se pone en HERCIOS.** **El enunciado la
escribe como «44,1», que son kilohercios**, y **con ese número la fórmula marcada da 2.902 en lugar de
2,9.** **Lo que la pregunta mide es la estructura de la fórmula —dividir por la frecuencia y
multiplicar por mil—, y ésa es la de la opción marcada.** **La notación de la frecuencia es
inconsistente y el temario lo declara.**

**La comprobación que despeja cualquier duda es el orden de magnitud**: **una memoria intermedia de
128 muestras es la configuración de trabajo de baja latencia de cualquier estación.** **Su latencia
son unos pocos milisegundos, no casi tres segundos.**

| Buffer | Latencia a 44,1 kHz | Cuándo se usa |
|---|---|---|
| **64 muestras** | **1,5 ms** | **Grabar con monitorización por el DAW**: lo más ajustado |
| **128 muestras** | **2,9 ms** | **Trabajo normal de grabación** |
| **512 muestras** | **11,6 ms** | **Mezcla**: no hay que tocar en directo |
| **2.048 muestras** | **46 ms** | **Mezclas muy cargadas de proceso** |

**La regla de oficio**: **buffer pequeño para grabar, buffer grande para mezclar.** **Y el umbral
práctico está en torno a los diez milisegundos**: **por encima de ahí, un músico que se oye por el
sistema nota el retraso y no puede tocar.**

## 3. La cadena de postproducción de sonido

**El punto 6 del anexo no tiene ninguna pregunta y el tema lo desarrolla porque el programa lo pide.**

**Las cinco capas de una banda sonora de ficción, que son las que se montan por separado y se mezclan
al final:**

| Capa | Qué contiene |
|---|---|
| **Diálogos** | **La voz de los actores**: directo, y lo que haya que sustituir en sala |
| **Ambientes** | **El fondo del lugar**: la calle, el bar, el bosque |
| **Efectos de sala (*Foley*)** | **Lo que los cuerpos hacen**: pasos, ropa, objetos, todo grabado mirando la imagen |
| **Efectos de biblioteca** | **Lo que no se puede hacer en sala**: disparos, motores, explosiones |
| **Música** | **Original y no original** |

**Y la razón de que se separen no es estética: es comercial.** **Manteniendo los diálogos en su propia
capa, la mezcla puede entregarse también sin ellos** —es la banda internacional, la **M&E**— **y con
ella se dobla la obra a cualquier idioma sin volver a montar nada.** **El doblaje que el enunciado
nombra depende enteramente de que esa separación se haya respetado.**

## 4. Los efectos y sus familias

| Familia | Qué hace | Ejemplos |
|---|---|---|
| **Basados en TIEMPO** | **Repiten o prolongan la señal** | **Delay, reverberación, eco** |
| **Basados en MODULACIÓN** | **Varían un parámetro cíclicamente** | **Chorus, flanger, phaser, trémolo, vibrato** |
| **Basados en DINÁMICA** | **Alteran la relación entre fuerte y flojo** | **Compresor, puerta, expansor** —el tema 7— |
| **Basados en FRECUENCIA** | **Cambian el reparto espectral** | **Ecualizadores y filtros** —el tema 7— |
| **De altura** | **Cambian el tono** | **Afinador, armonizador, cambio de formantes** |

**El delay de la pregunta 15 pertenece a la primera familia**, y **su pariente mayor es la
reverberación**: **una reverberación es, en el fondo, miles de retardos con distinta duración y
distinta atenuación.**

**Los tres parámetros de una reverberación que hay que saber leer:**

1. **Tiempo de reverberación**: **cuánto tarda la cola en caer.** **Es el mismo RT60 del tema 4**,
   aquí puesto a mano en vez de medido en una sala.
2. **Predemora**: **cuánto tarda en empezar la cola.** **Es lo que separa la fuente de la sala**: sin
   predemora, la voz suena metida dentro del muro.
3. **Mezcla seco/húmedo**: **cuánta señal procesada se suma a la original.**

## 5. La sincronización

**El enunciado del punto 16 nombra expresamente la sincronización**, y **es lo que conecta este tema
con el 17.**

**Las tres cosas que una estación de trabajo tiene que sincronizar, y que no son la misma:**

| Qué se sincroniza | Con qué | Si falla |
|---|---|---|
| **La POSICIÓN**: por dónde va | **Código de tiempo (LTC o MTC)** | **La imagen y el sonido no cuadran** |
| **La VELOCIDAD**: a qué ritmo avanza | **Word clock o referencia de vídeo** | **Deriva lenta**: cuadra al principio y no al final |
| **La MUESTRA**: cuándo cae cada una | **Word clock** | **Chasquidos y ruido digital** |

**Y el error de concepto más común, que el tema 17 desarrolla**: **el código de tiempo NO sincroniza
el reloj de muestreo.** **Dice en qué punto se está, no a qué velocidad se avanza.** **Un montaje que
lleve código de tiempo y no lleve reloj común deriva igualmente.**

## 6. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 15 | Duración de un delay de corchea a 102 BPM | b) 294 ms ✔ |
| 36 | Fórmula de la latencia de un buffer de 128 muestras | b) Muestras × 1.000 ÷ frecuencia ✔ **·** con la salvedad del epígrafe 2 |

**Las dos respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Y el aviso de estudio del tema, que es también su mejor argumento**: **dos preguntas y dos fórmulas.**
**60.000 dividido entre los pulsos por minuto, y las muestras divididas entre la frecuencia por mil.**
**No hay un tercer dato que aprender en este punto.**

## 7. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es la postproducción de sonido, los efectos y la
operación de una estación de trabajo, y **va entera como oficio.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema** | Las dos **van como oficio** |

**Tres declaraciones expresas:**

1. **La fórmula de la pregunta 36 es correcta en su estructura y su enunciado escribe la frecuencia de
   muestreo de forma inconsistente.** **Con la frecuencia en hercios la fórmula marcada da 2,9
   milisegundos, que es el resultado bueno; con el «44,1» que el enunciado escribe, daría 2.902.**
   **El temario declara la inconsistencia y sostiene la respuesta oficial, porque es la única de las
   cuatro cuya estructura es la correcta.**
2. **Las latencias de la tabla del epígrafe 2 están calculadas por este temario a 44,1 kHz** y **no
   proceden de ninguna especificación de fabricante.** **La latencia real de un sistema es mayor que
   la del búfer**: hay que sumar la de los conversores y la del proceso, y **el tema no la incluye
   porque la pregunta no la pide.**
3. **Las cinco capas de una banda sonora y las familias de efectos son clasificaciones asentadas de la
   postproducción**, no normalizadas. **El tema las presenta como conocimiento común de la materia.**

**El resto del tema va como oficio y así se declara**: la conversión de tempo a milisegundos, la
regla de buffer pequeño para grabar y grande para mezclar, la separación de capas y su razón
comercial, los tres parámetros de una reverberación y la distinción entre sincronizar posición,
velocidad y muestra. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
