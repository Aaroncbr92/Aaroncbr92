# Tema 6 del específico de Edición, Montaje y Procesos Audiovisuales · Equipos de medida y control

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 6 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los instrumentos de medida de vídeo y de audio y las matrices de conmutación, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Advertencia** | **Dos de las tres preguntas de este punto son la misma**: la 57 y la 61 se diferencian en tres letras del enunciado y tienen las mismas cuatro opciones. **Una sola respuesta vale dos preguntas de noventa y seis** |
| **Extensión** | **2.013 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: los cuadros por segundo (**fps**, *frames per
second*); el decibelio referido a la escala completa digital (**dBFS**, *decibels relative to full
scale*) y el decibelio de unidad (**dBu**); las unidades de volumen (**VU**); la sonoridad referida a
la escala completa (**LUFS**, *loudness units relative to full scale*); la Unión Europea de
Radiodifusión (**UER**, o **EBU** en su sigla inglesa), autora de la recomendación **R 128**; la
Sociedad de Ingenieros de Cine y Televisión (**SMPTE**); el vídeo por componentes con luminancia y
diferencias de color (**YCbCr**); los tres primarios (**RGB**); el instituto de reglaje del reloj de
la imagen (**IRE**, por la antigua *Institute of Radio Engineers*), que da nombre a la unidad de la
escala de vídeo; y la interfaz digital serie (**SDI**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, punto 3):
> «Equipos de Medida y control.»
> «3.1. Equipos de medida y control de la señal de video.»
> «3.2. Equipos de medida y control de la señal de audio.»
> «3.3. Matrices de conmutación y conectividad.»

**Tres preguntas**, y **dos de las tres son la misma pregunta con una palabra de diferencia**: la 57
pregunta por «la tasa de grabación original» y la 61 por «la tasa fps de grabación original», **con
las mismas cuatro opciones y la misma respuesta**. **Es la única repetición de este cuadernillo**, y
vale dos preguntas de noventa y seis.

<!-- indice -->

## Índice

- [1. Por qué se mide](#1-por-qué-se-mide)
- [2. Los instrumentos de vídeo](#2-los-instrumentos-de-vídeo)
- [3. Los instrumentos de audio](#3-los-instrumentos-de-audio)
- [4. El 0 dBFS y la escala digital](#4-el-0-dbfs-y-la-escala-digital)
- [5. La cadencia de grabación y la reproducción](#5-la-cadencia-de-grabación-y-la-reproducción)
- [6. Las matrices de conmutación](#6-las-matrices-de-conmutación)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Por qué se mide

**Un monitor y un altavoz no sirven para decidir si una señal es correcta.** Cada monitor tiene su
brillo, cada sala su acústica y cada oído su costumbre. **Lo que sirve es un instrumento**, y por eso
el temario dedica un punto entero a ellos.

**Las tres cosas que la medida garantiza:**

1. **Que la señal esté dentro de los límites técnicos de emisión**: ni luminancia por encima del
   blanco de referencia, ni picos de audio por encima del máximo digital.
2. **Que el material sea homogéneo**: que un plano no salte de nivel respecto del siguiente, ni un
   bloque de programa respecto del anterior.
3. **Que el defecto se pueda localizar**: **un instrumento dice dónde está el problema**, y el ojo
   sólo dice que algo se ve raro.

## 2. Los instrumentos de vídeo

| Instrumento | Qué mide | Qué se ve en él |
|---|---|---|
| **Monitor de forma de onda** | **La luminancia**, línea a línea | Un perfil del brillo de la imagen, con el nivel de negro y el de blanco |
| **Vectorscopio** | **La crominancia**: tono y saturación | Un diagrama polar con **las cajas de los seis colores de barras** |
| **Monitor de referencia** | Lo que se ve, calibrado | La imagen, con el color y el brillo que la norma fija |
| **Histograma** | **El reparto estadístico de los niveles** | Cuántos píxeles hay en cada nivel de brillo |
| **Analizador de errores** | La integridad de la señal digital | Errores de comprobación, *jitter*, cumplimiento de la interfaz |

**Las dos referencias que hay que conocer**: **la señal de barras**, que es el patrón con el que se
ajusta la cadena de vídeo, y **la escala IRE**, en la que el negro está en 0 y el blanco de referencia
en 100.

**La regla de oficio**: **la forma de onda dice si la exposición está bien; el vectorscopio dice si el
color está bien.** Son dos preguntas distintas y **hacen falta los dos instrumentos**.

## 3. Los instrumentos de audio

| Instrumento | Qué mide |
|---|---|
| **Medidor de pico** | **El valor instantáneo más alto**, para no rebasar el máximo digital |
| **Medidor VU** | **Un valor promediado**, más cercano a cómo se percibe el volumen |
| **Medidor de sonoridad** | **La sonoridad integrada** en LUFS, según la recomendación R 128 de la Unión Europea de Radiodifusión |
| **Fasímetro** o correlador | **La relación de fase entre canales**: avisa de que un estéreo se anula al sumarlo a mono |
| **Analizador de espectro** | **El reparto de energía por frecuencias** |

**La distinción que este epígrafe fija**: **el pico dice si algo va a distorsionar; la sonoridad dice
si algo suena fuerte o flojo.** **No son lo mismo**, y una señal muy comprimida puede tener el mismo
pico que otra y sonar mucho más alta.

**Y de ahí sale la norma de emisión europea**: **se normaliza por sonoridad y no por pico**, para que
el espectador no tenga que tocar el mando entre un programa y el anuncio siguiente.

## 4. El 0 dBFS y la escala digital

**En una escala de medición de un medidor digital de audio, un valor de 0 dBFS representa la máxima
amplitud que puede tener la señal.** Ésa es la respuesta oficial a la pregunta 9.

**Qué significan las siglas, que es lo que resuelve la pregunta**: **dBFS** es *decibels relative to
full scale*, **decibelios respecto de la escala completa**. **La escala completa es el valor más alto
que los bits disponibles pueden representar**, y **por convenio ese valor es el cero**.

**La consecuencia, y es lo que la hace distinta de una escala analógica:**

| Escala | Dónde está el cero | Qué hay por encima |
|---|---|---|
| **Analógica**, en dBu o VU | **En el nivel de referencia de trabajo** | **Margen de sobrecarga**: se puede pasar del cero sin distorsionar |
| **Digital**, en dBFS | **En el máximo absoluto** | **Nada. No hay nada por encima del cero** |

**Por eso todos los valores de una escala digital son negativos**: **−6 dBFS, −18 dBFS, −20 dBFS**.
**Rebasar el cero no da un poco de saturación agradable: da recorte**, porque el convertidor no tiene
más números.

**Las tres opciones falsas de la pregunta 9 y su error:**

| Opción | Por qué no |
|---|---|
| «La mínima amplitud que puede tener la señal» | **Es lo contrario**: la mínima está en el extremo negativo de la escala |
| «La inexistencia de señal de entrada» | **Confunde el cero de la escala con el silencio.** El silencio es **−∞ dBFS** |
| «Un error en la lectura» | **El 0 dBFS es un valor legítimo**, no un aviso de fallo |

**La opción b) es la trampa buena**, porque **en cualquier otra escala un cero sí significaría
«nada»**. **En dBFS el cero es el techo, no el suelo**, y ésa es toda la pregunta.

**La regla de trabajo que sale de aquí**: **en producción se trabaja con margen**, dejando los picos
del programa **bastante por debajo del cero** —los niveles de referencia habituales están entre −18 y
−20 dBFS—, **precisamente porque por encima del cero no hay sitio.**

## 5. La cadencia de grabación y la reproducción

**La tasa de grabación original —la cadencia de cuadros por segundo con que se grabó— determina la
fluidez y la velocidad del vídeo.** Ésa es la respuesta oficial a la pregunta 57 **y también a la
pregunta 61**, que es la misma con «fps» añadido al enunciado.

**Las dos cosas que la cadencia determina**, y conviene verlas por separado porque la respuesta las
nombra las dos:

| Efecto | En qué consiste |
|---|---|
| **Fluidez** | **Cuantas más imágenes por segundo, más suave se percibe el movimiento.** A 25 el movimiento es fluido; a 12 se ve a saltos |
| **Velocidad** | **Si se graba a más cadencia de la que se reproduce, la acción sale a cámara lenta**; si se graba a menos, sale acelerada |

**El segundo efecto es el que da sentido a la palabra «velocidad» de la respuesta oficial**, y es
oficio puro: **grabar a 100 cuadros por segundo y reproducir a 25 da una cámara lenta de cuatro veces,
sin repetir ni inventar cuadros**. **Ésa es la única cámara lenta que no degrada**, y es la razón de
que las cámaras de deportes graben a cadencia alta.

**Las tres opciones falsas, idénticas en las dos preguntas:**

| Opción | Por qué no |
|---|---|
| «Sólo afecta al tamaño del archivo» | **Sí lo afecta, pero no «sólo»**: la palabra que la hunde es «sólo» |
| «Sólo afecta a la calidad del audio» | **La cadencia de vídeo no toca el audio** |
| «No tiene ningún impacto» | **Es la negación de la respuesta** |

**El aviso de estudio**: **la 57 y la 61 son la misma pregunta**, con la misma respuesta y las mismas
opciones. **Una sola respuesta vale dos preguntas de noventa y seis**, y es la única repetición de
este cuadernillo.

## 6. Las matrices de conmutación

**Una matriz de conmutación es el aparato que encamina cualquiera de sus entradas a cualquiera de sus
salidas**, y es lo que hace posible que una casa de televisión reparta señales sin recablear.

| Concepto | Qué es |
|---|---|
| **Entradas y salidas** | **El tamaño de la matriz se da como «entradas × salidas»**: 64 × 64, 128 × 128 |
| **Punto de cruce** | **Cada conexión posible entre una entrada y una salida** |
| **Nivel** | **Cada tipo de señal que se conmuta a la vez**: vídeo, audio, datos. **Se conmutan juntos o por separado** |
| **Conmutación en el intervalo vertical** | **El cambio se hace en el hueco entre dos imágenes**, para que no se vea el salto |
| **Panel de control** | Desde donde se ordena la conmutación |

**Por qué importa al montador**: **la sala de edición recibe sus fuentes y entrega su salida a través
de la matriz**, y **una fuente que no aparece suele ser un problema de encaminamiento y no de la
sala**. **Saber leer un panel de matriz es lo que separa una avería resuelta en un minuto de una
llamada al técnico.**

**Y la regla que evita el error más visible**: **la conmutación se hace en el intervalo vertical**. Un
cambio hecho en mitad de una imagen **parte el cuadro en dos**, y eso se ve en antena.

## 7. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 9 | Qué amplitud representa un valor de 0 dBFS | c) La máxima amplitud que puede tener la señal ✔ |
| 57 | Cómo afecta la tasa de grabación original a la reproducción | a) Determina la fluidez y velocidad del vídeo ✔ |
| 61 | Cómo afecta la tasa fps de grabación original a la reproducción | a) Determina la fluidez y velocidad del vídeo ✔ **·** repetida de la 57 |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla**.

**El aviso de estudio**: **la 57 y la 61 son la misma pregunta**, con enunciados que sólo se
diferencian en tres letras y con **las mismas cuatro opciones en el mismo orden**. **Es la única
repetición literal de este cuadernillo**, y conviene saberla porque **vale dos preguntas**.

**El aviso de reparto**: **el punto 3 del anexo tiene tres subpuntos y sólo dos materias
preguntadas**, ninguna de ellas la de matrices de conmutación. **El tema la desarrolla igual porque el
programa la manda**, y porque su vocabulario aparece en las salas.

## 8. Trazabilidad

**Este tema no cita ninguna norma del BOE.** Su materia son instrumentos de medida y encaminamiento de
señal, y **va entera como oficio**.

**Ninguna de sus tres respuestas descansa sólo en la plantilla.** El significado de dBFS y la relación
entre cadencia de grabación y reproducción **son definiciones asentadas**, verificables en cualquier
manual de audio digital o de cámara.

**Lo que se menciona y no se ha consultado**: **la recomendación R 128 de la Unión Europea de
Radiodifusión**, sobre normalización de sonoridad, **se cita por su existencia y su objeto**, no por su
contenido articulado. **Ninguna pregunta de este cuadernillo depende de ella**, y el tema no le
atribuye ninguna cifra.
