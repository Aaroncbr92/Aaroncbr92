# Tema 9 del específico de Sonido · Grabación de sonido

Las siglas y unidades de este tema, presentadas de entrada: la modulación por impulsos codificados
(**PCM**), que el tema 6 ya presentó; el formato de fichero de onda (**WAV**) y su versión con
metadatos de difusión (**BWF**, *broadcast wave format*); el códec libre de compresión sin pérdida
(**FLAC**, *free lossless audio codec*); la codificación avanzada de audio (**AAC**, *advanced audio
coding*); el códec **Opus**; el sistema de codificación **AC-3** de Dolby; el bit y el byte (**b** y
**B**), y el megabyte (**MB**); los fotogramas por segundo (**fps**); y el decibelio a escala completa
(**dBFS**), que el tema 7 ya presentó.

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 7):
> «GRABACIÓN DE SONIDO. Equipamiento: Tipos, características y funcionalidad. Estándares, Soportes y
> formatos.»

**Cuatro preguntas**, y **las cuatro son de audio digital**: **ninguna pregunta por un equipo, un
soporte o una marca.** **Lo que el examen mide aquí es si el opositor sabe de qué está hecho un
fichero de audio.**

**Y tres de las cuatro son cuentas**, lo que las hace de las más seguras del cuadernillo: **se
calculan, no se recuerdan.**

<!-- indice -->

## Índice

- [1. De qué está hecho un fichero de audio](#1-de-qué-está-hecho-un-fichero-de-audio)
- [2. La cuenta del tamaño](#2-la-cuenta-del-tamaño)
- [3. El rango dinámico y los bits](#3-el-rango-dinámico-y-los-bits)
- [4. Con pérdida y sin pérdida](#4-con-pérdida-y-sin-pérdida)
- [5. Muestras, segundos y fotogramas](#5-muestras-segundos-y-fotogramas)
- [6. Equipamiento, soportes y formatos](#6-equipamiento-soportes-y-formatos)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. De qué está hecho un fichero de audio

**Tres números definen un audio digital sin comprimir, y de ellos sale todo lo demás:**

| Parámetro | Qué fija | Valores corrientes |
|---|---|---|
| **Frecuencia de muestreo** | **Cuántas veces por segundo se mide la señal** | **44,1 kHz** —disco compacto—, **48 kHz** —vídeo y difusión—, 96 y 192 kHz |
| **Profundidad de bits** | **Con cuánta finura se mide cada muestra** | **16 bits** —disco—, **24 bits** —producción—, 32 en coma flotante |
| **Canales** | **Cuántas señales paralelas** | **1** mono, **2** estéreo, más en multicanal |

**Y las dos reglas que los gobiernan:**

1. **El teorema del muestreo**: **para reproducir una frecuencia hay que muestrear a más del doble.**
   **De ahí que 44,1 kHz cubra hasta algo más de 20 kHz**, que es el límite del oído del tema 2.
   **Muestrear por debajo produce aliasing: frecuencias que no estaban aparecen donde no deben.**
2. **Cada bit añade unos 6 decibelios de rango dinámico**, que es el epígrafe 3.

## 2. La cuenta del tamaño

**Un archivo de audio estéreo a 44,1 kHz, 16 bits y 5 minutos ocupa aproximadamente 50 megabytes.**
Ésa es la respuesta oficial a la pregunta 92.

**La cuenta, y conviene hacerla siempre en el mismo orden:**

1. **Bytes por muestra y canal**: **16 bits son 2 bytes.**
2. **Bytes por segundo**: **44.100 × 2 × 2 canales = 176.400.**
3. **Segundos**: **5 minutos son 300.**
4. **Total**: **176.400 × 300 = 52.920.000 bytes**, que **son unos 53 megabytes.**

**De las cuatro opciones, la más próxima es «aproximadamente 50 MB».**

**Y el atajo que conviene tener en la cabeza para no hacer la cuenta entera**: **un minuto de estéreo
a 44,1 kHz y 16 bits ocupa unos 10 megabytes.** **Cinco minutos, unos 50.** **Con ese solo dato la
pregunta se contesta de memoria.**

| Formato | Un minuto de estéreo |
|---|---|
| **44,1 kHz · 16 bits** | **≈ 10 MB** |
| **48 kHz · 24 bits** | **≈ 17 MB** |
| **96 kHz · 24 bits** | **≈ 33 MB** |

## 3. El rango dinámico y los bits

**El rango dinámico teórico máximo de una señal de audio digital de 16 bits es de 96 dB.** Ésa es la
respuesta oficial a la pregunta 68.

**La cuenta es la misma regla del tema 2 aplicada a los bits**: **cada bit dobla el número de niveles
disponibles, y doblar la amplitud son 6 decibelios.** **Dieciséis bits por seis son 96.**

| Profundidad | Rango dinámico teórico |
|---|---|
| **8 bits** | **48 dB** |
| **16 bits** | **96 dB** |
| **20 bits** | **120 dB** |
| **24 bits** | **144 dB** |

**Y las cuatro opciones de la pregunta son exactamente esos cuatro valores**, lo que **la convierte en
una pregunta de tabla: quien tenga la serie acierta sin calcular.**

**La palabra «teórico» de la respuesta importa, y el temario la sostiene**: **96 decibelios es lo que
la cuantificación permite.** **El rango real de un sistema es menor**, porque **el ruido de los
conversores y de la electrónica analógica se come parte del margen.** **Ningún conversor de 24 bits
entrega 144 decibelios reales.**

## 4. Con pérdida y sin pérdida

**El códec con el que el audio no sufre pérdida de calidad es FLAC.** Ésa es la respuesta oficial a la
pregunta 83.

**Las dos familias, y qué hace cada una:**

| Familia | Qué hace | Ejemplos |
|---|---|---|
| **Sin pérdida** ✔ | **Comprime como un fichero comprimido cualquiera**: al descomprimir sale el original bit a bit | **FLAC**, Apple Lossless, WavPack |
| **Con pérdida** | **DESCARTA lo que el oído no va a notar**, apoyándose en el enmascaramiento del tema 2 | **AAC**, **Opus**, **AC-3**, MP3 |

**Las tres opciones falsas son los tres códecs con pérdida de la lista**, y **cada uno tiene su
terreno**: **AAC es el sucesor del MP3 y el estándar de la distribución; Opus es el de las
comunicaciones en tiempo real por red; AC-3 es el de Dolby Digital, el del cine y la televisión
multicanal.**

**La regla de familia que hace la pregunta contestable sin conocer los cuatro**: **un códec sin
pérdida no puede garantizar el caudal de datos.** **Comprime lo que el material le deje —entre la
mitad y dos tercios— y el resultado varía con la música.** **Un códec con pérdida sí garantiza el
caudal, porque tira lo que haga falta para cumplirlo.** **Si el nombre lleva asociada una cifra de
kilobits por segundo, es con pérdida.**

**Y la consecuencia de oficio, que enlaza con el tema 6**: **una señal de contribución no se comprime
con pérdida si se puede evitar**, porque **todavía va a pasar por más procesos.** **Las pérdidas se
acumulan y no se recuperan.**

## 5. Muestras, segundos y fotogramas

**13.440 muestras en un sistema que trabaja a 48 kHz con una frecuencia de vídeo de 25 fotogramas por
segundo duran 7 fotogramas.** Ésa es la respuesta oficial a la pregunta 8.

**La cuenta, en dos pasos y sin atajos:**

1. **De muestras a segundos**: **13.440 ÷ 48.000 = 0,28 segundos.**
2. **De segundos a fotogramas**: **0,28 × 25 = 7.**

**Y el atajo que conviene ver, porque es el que el examen premia**: **a 48 kHz y 25 fotogramas por
segundo, cada fotograma dura exactamente 1.920 muestras.** **13.440 ÷ 1.920 = 7.**

| Cadencia | Muestras por fotograma a 48 kHz |
|---|---|
| **25 fps** —Europa— | **1.920** |
| **24 fps** —cine— | **2.000** |
| **30 fps** | **1.600** |
| **29,97 fps**, la cadencia del sistema americano | **No es entero**: de ahí el código de tiempo con salto |

**Ese último renglón es el que explica media docena de problemas de sincronismo del tema 17**: **en
Europa las cuentas salen redondas y en el sistema americano no.**

## 6. Equipamiento, soportes y formatos

**El enunciado del punto pide expresamente equipamiento y soportes y el examen no pregunta por
ninguno.** **El tema los cubre porque el programa los pide.**

| Equipo | Para qué |
|---|---|
| **Grabador de mano** | **Ambientes, efectos, entrevistas rápidas**: autonomía y micrófonos incorporados |
| **Grabador multipista de campo** | **Sonido directo de rodaje**: entradas con previo de calidad, código de tiempo y alimentación fantasma |
| **Estación de trabajo con interfaz** | **Estudio**: el tema 8 |
| **Grabador de estado sólido de emisora** | **Continuidad y archivo**: redundancia y arranque por orden |

**Y el formato que hay que conocer aunque no se pregunte**: **el fichero de onda de difusión, el
BWF.** **Es un WAV con una cabecera añadida que lleva la marca de tiempo de la grabación, el nombre
del proyecto y las notas de la toma.** **Esa marca de tiempo es lo que permite que un montador
sincronice sonido e imagen sin claqueta**, y **por eso es el formato de entrega del sonido directo.**

## 7. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 8 | Duración en fotogramas de 13.440 muestras a 48 kHz | b) 7 ✔ |
| 68 | Rango dinámico teórico de 16 bits | c) 96 dB ✔ |
| 83 | Códec sin pérdida de calidad | d) FLAC ✔ |
| 92 | Tamaño de un estéreo de 44,1 kHz, 16 bits y 5 minutos | c) Aproximadamente 50 MB ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Y el aviso de estudio**: **tres de las cuatro son cuentas y la cuarta es una clasificación.** **Con
la regla de los 6 decibelios por bit, el atajo de los 10 megabytes por minuto y las 1.920 muestras por
fotograma se contesta el punto entero.**

## 8. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es la grabación de sonido, sus formatos y sus
soportes, y **va entera como oficio.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema** | Las cuatro **van como oficio** |

**Tres declaraciones expresas:**

1. **La regla de los 6 decibelios por bit es una aproximación y el tema la presenta como tal.** **La
   expresión exacta del rango dinámico de un cuantificador ideal añade una constante**, y **la cifra
   que resulta para 16 bits es algo mayor que 96.** **La respuesta oficial usa la aproximación
   corriente del sector**, que **es la que las cuatro opciones de la pregunta presuponen.**
2. **Las cifras de tamaño de fichero del epígrafe 2 están calculadas por este temario** y **usan el
   megabyte de un millón de bytes.** **Con el megabyte binario de 1.048.576 bytes el resultado sería
   algo menor**, y **en las dos convenciones la opción más próxima sigue siendo la misma.**
3. **La documentación de los códecs nombrados no se ha consultado.** **Lo que el tema sostiene de ellos
   es a qué familia pertenecen y para qué se usan**, que **es lo que la pregunta 83 mide.** **Ninguna
   cifra de rendimiento se atribuye a ninguno.**

**El resto del tema va como oficio y así se declara**: los tres parámetros de un audio digital y el
teorema del muestreo, la cuenta del tamaño y su atajo, la serie de rango dinámico por profundidad, la
distinción entre códecs con y sin pérdida, la equivalencia entre muestras y fotogramas y la tabla de
equipamiento. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y
el tema no lo presenta como si lo estuviera.
