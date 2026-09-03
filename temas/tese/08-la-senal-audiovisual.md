# Tema 8 del específico de Técnica de Equipos y Sistemas Electrónicos · La señal audiovisual y sus sincronismos

Las siglas de este tema, presentadas de entrada: la interfaz digital serie de vídeo (**SDI**) y su
versión de alta definición (**HD-SDI**), definidas por las normas de la Sociedad de Ingenieros de Cine
y Televisión (**SMPTE**) **259M**, **292M** y **424M**; las normas de audio de la Sociedad de
Ingeniería de Audio (**AES**) —la **AES3** de dos canales, la **AES10** o **MADI** y la **AES11** de
sincronismo—; los patrones de referencia temporal de fin y de comienzo de vídeo activo (**EAV** y
**SAV**) y su palabra de estado (**XYZ**); las banderas de campo, de borrado vertical y de borrado
horizontal (**F**, **V** y **H**) y los cuatro bits de protección (**P3** a **P0**); el número de línea
(**LN0** y **LN1**); la señal de negro compuesto (*black burst*, **BB**); el reloj de palabra (*word
clock*); el código de tiempo longitudinal (**LTC**); el protocolo de tiempo de precisión (**PTP**,
definido por el estándar **IEEE 1588**) y el protocolo de tiempo de red (**NTP**); el protocolo de red
(**IP**), que el tema 9 desarrolla; y el megabit por segundo (**Mbps**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 10):
> «SEÑAL AUDIOVISUAL: Señal video digital serie SDI: normativas SMPTE 259M, 292M y 424M. Señal de
> audio analógico y señal de audio digital AES. Protocolo MADI. Señales de sincronización: BB,
> TRILEVEL, AES11, Word clock, etc.»

**Diez preguntas: el segundo banco de esta ocupación.** **Y el punto que más se parece a un examen de
televisión y menos a uno de electrónica**: **aquí se pregunta por el interior de las tramas que
recorren una instalación.**

**Su reparto**: **cuatro preguntas son de SDI, tres de audio digital y MADI, y tres de sincronismo.**
**Ninguna lleva figura**, lo que **convierte a este punto en el más contestable de los grandes.**

<!-- indice -->

## Índice

- [1. Las tres normas del SDI](#1-las-tres-normas-del-sdi)
- [2. Los patrones EAV y SAV](#2-los-patrones-eav-y-sav)
- [3. El audio digital y sus caudales](#3-el-audio-digital-y-sus-caudales)
- [4. Los sincronismos](#4-los-sincronismos)
- [5. La avería del distribuidor de código de tiempo](#5-la-avería-del-distribuidor-de-código-de-tiempo)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Las tres normas del SDI

**El enunciado nombra tres y cada una corresponde a una generación:**

| Norma | Caudal | Para qué |
|---|---|---|
| **SMPTE 259M** | **270 Mbps** en su modo corriente | **Definición estándar** |
| **SMPTE 292M** | **1,485 Gbps** | **Alta definición**: es el HD-SDI |
| **SMPTE 424M** | **2,97 Gbps** | **3G-SDI**: 1080p a 50 y 60 cuadros |

**Y lo que las tres comparten, que es lo que el examen pregunta**: **la estructura de la trama.**
**Todas transportan palabras de 10 bits y todas marcan el principio y el final del vídeo activo con
los mismos dos patrones.**

## 2. Los patrones EAV y SAV

**Dos preguntas del cuadernillo van de aquí, y son las más técnicas del punto.**

**La pregunta 84**: **los patrones de referencia temporal EAV y SAV están formados por cuatro palabras
de 10 bits cuyo orden es 3FF – 000 – 000 – XYZ.** Ésa es la respuesta oficial.

**Cómo se lee esa secuencia:**

| Palabra | Valor | Para qué |
|---|---|---|
| **Primera** | **3FF** —todo unos— | **Es un valor PROHIBIDO para el vídeo**: por eso sirve de marca |
| **Segunda y tercera** | **000** —todo ceros— | **También prohibidos**: refuerzan la marca |
| **Cuarta** | **XYZ** | **La palabra de estado**: dice de qué patrón se trata |

**Y la razón de que las tres primeras sean esos valores y no otros es la clave del diseño**: **en SDI,
los valores 000 y 3FF están RESERVADOS y nunca aparecen en el vídeo activo.** **La señal se codifica
dejando esos extremos libres precisamente para que la secuencia de sincronismo sea inconfundible.**
**Ningún fotograma puede imitarla por accidente.**

**La pregunta 42**: **en la palabra XYZ, formada por los bits 1FVHP3P2P1P000, los bits P3, P2, P1 y P0
son bits de protección.** Ésa es la respuesta oficial.

**El desglose completo de esa palabra de 10 bits:**

| Bits | Qué son |
|---|---|
| **El primero, siempre 1** | **Marca fija** |
| **F** | **Bandera de campo**: primer o segundo campo |
| **V** | **Borrado vertical**: dice si la línea está dentro del intervalo vertical |
| **H** | **Borrado horizontal**: distingue EAV de SAV |
| **P3, P2, P1, P0** ✔ | **Cuatro bits de PROTECCIÓN**, calculados sobre F, V y H |
| **Los dos últimos, siempre 0** | **Relleno** |

**Por qué hacen falta cuatro bits de protección para tres de información**: **porque no se trata sólo
de detectar un error, sino de CORREGIRLO.** **Con esa redundancia, un receptor que reciba la palabra
con un bit cambiado puede reconstruir F, V y H sin pedir nada.** **Y eso importa porque son los bits
que dicen dónde empieza cada línea y cada campo: un error ahí desbarata la imagen entera.**

**La pregunta 67**: **en el HD-SDI, el número de línea dentro del cuadro se informa a continuación del
patrón EAV, mediante dos palabras de 10 bits —LN0 y LN1— que combinadas forman un contador binario de
11 bits.** Ésa es la respuesta oficial.

**Dos detalles que la pregunta mide y conviene fijar:**

1. **Va después del EAV, no del SAV.** **Es decir, al FINAL de la línea activa, no al principio.**
2. **Once bits de contador dan hasta 2.048 líneas**, que **cubre de sobra los 1.125 totales de un
   cuadro de alta definición.**

**Y la diferencia con la definición estándar**: **el número de línea es una aportación del HD-SDI.**
**La 259M no lo lleva.** **Por eso la pregunta especifica «en el interface de alta definición».**

## 3. El audio digital y sus caudales

**Dos preguntas piden calcular un caudal y las dos se contestan con la misma idea, aplicada al revés.**

**La pregunta 71**: **una señal de audio AES3 a 48 kHz tiene un bit rate de 3,072 Mbps.** Ésa es la
respuesta oficial.

**La cuenta**: **el AES3 transporta DOS canales, y cada muestra ocupa un subcuadro de 32 bits** —24
para el audio y 8 para estado de canal, validez, usuario y paridad—. **Por tanto:**

> **48.000 × 32 × 2 = 3.072.000 bits por segundo.**

**Y el dato que conviene retener es que el AES3 gasta 32 bits por muestra aunque el audio sea de 16 o
de 20**: **el subcuadro es de tamaño fijo.**

**La pregunta 8 del segundo llamamiento, que es la misma pregunta para el MADI y tiene la respuesta
contraria**: **el bitrate de una señal AES-10 que transporta audio muestreado a 48.000 muestras por
segundo es 125 Mbps.** Ésa es la respuesta oficial.

**Y aquí está la enseñanza del par**: **el caudal del MADI NO depende de cuántos canales lleve ni de
la profundidad de cada uno.** **Su trama es de tamaño fijo y su velocidad de línea también.** **Se
transmitan 64 canales o dos, el cable va a 125 megabits por segundo.**

| | **AES3** | **AES10 (MADI)** |
|---|---|---|
| **Canales** | **2** | **Hasta 64** |
| **¿El caudal depende del contenido?** | **Sí**: crece con la frecuencia de muestreo | **No**: velocidad de línea fija |
| **Caudal a 48 kHz** | **3,072 Mbps** | **125 Mbps** |

**Por eso las opciones falsas de la pregunta 8 —«depende de la profundidad de muestra» y «depende del
número de canales»— están tan bien puestas**: **son verdad para el AES3 y mentira para el MADI.**

**La pregunta 91**: **el protocolo MADI puede transportar hasta 64 canales en un solo cable.** Ésa es
la respuesta oficial, **y es el mismo dato que el temario de Sonido verifica en su tema 17.**

**La pregunta 81**: **el estándar que define el protocolo comúnmente conocido como MADI es la AES-10.**
Ésa es la respuesta oficial.

**Y esto sí está documentado.** **La presentación pública de las normas de la Sociedad de Ingeniería
de Audio, que este proyecto tiene volcada, lo dice literalmente:**

> «AES3 (2-channel digital audio), **AES10 (MADI)**, AES14 (analog XLR pin-out), AES67 (networked
> audio) — AES Standards have contributed to your operations, making your work more successful,
> improved your workflow, and saved your production, more times than you realize.»

---

**De esa frase salen, además de la respuesta a la 81, las tres opciones falsas explicadas**: **la
AES3 es la de dos canales, la AES11 es la de sincronismo —que el propio enunciado del anexo nombra— y
la AES12 no aparece en la relación.** **El texto interno de estas normas está tras un muro de pago y
no se ha leído**, así que **ninguna cifra de este tema se atribuye a su articulado.**

## 4. Los sincronismos

**Tres preguntas van de sincronizar, y la primera es de vocabulario.**

**La pregunta 45**: **el protocolo PTP, definido por el estándar IEEE 1588, se utiliza para
sincronismo de relojes.** Ésa es la respuesta oficial.

**La pregunta 92**: **el protocolo NTP es un protocolo de internet para sincronizar los relojes de los
sistemas informáticos.** Ésa es la respuesta oficial.

**Los dos sincronizan relojes y no son intercambiables**, y **la diferencia es de tres órdenes de
magnitud:**

| Protocolo | Precisión | Para qué |
|---|---|---|
| **NTP** | **Milisegundos** | **Poner en hora un ordenador** |
| **PTP (IEEE 1588)** | **Sub-microsegundo** | **Alinear muestras y cuadros** de audio y vídeo |

**Y las señales de sincronismo clásicas, que el enunciado enumera:**

| Señal | Qué distribuye | A quién |
|---|---|---|
| **Black burst** | **La referencia de CUADRO** de definición estándar | **Toda la instalación de vídeo** |
| **Trilevel** | **Lo mismo para alta definición**: pulso de tres niveles | **Instalaciones de alta definición** |
| **Word clock** | **El instante de cada MUESTRA de audio** | **Equipos de audio digital** |
| **AES11** | **La norma que define cómo se distribuye esa referencia** en audio profesional | |
| **PTP** | **Todo lo anterior, por red** | **Instalaciones sobre IP**: es el tema 9 |

**Y la distinción que el temario de Sonido también hace y que aquí conviene repetir**: **el código de
tiempo NO sincroniza.** **Dice POSICIÓN, no velocidad.** **Dos equipos con el mismo código de tiempo y
relojes distintos derivan igual.**

## 5. La avería del distribuidor de código de tiempo

**Ésta es la mejor pregunta del punto, porque es de razonar y no de recordar.**

**La pregunta 20 del segundo llamamiento**: **si en una unidad móvil se avería el distribuidor de
código de tiempo LTC y hay disponibles distribuidores de referencia de negro compuesto, de audio
analógico, de SDI y de AES3, el que se puede usar para solucionar la avería es el de AUDIO
ANALÓGICO.** Ésa es la respuesta oficial.

**El razonamiento tiene una sola clave y está en el nombre**: **el código de tiempo longitudinal es
una señal de AUDIO.** **Se modula como audio, ocupa la banda de audio —del orden de un par de
kilohercios—, viaja por cable de audio y se graba en pistas de audio.** **Un distribuidor de audio
analógico no sabe que lo que le entra es código de tiempo, y no le hace falta saberlo: reparte una
señal analógica en su banda.**

**Y las tres opciones falsas se caen cada una por su motivo:**

| Opción | Por qué no |
|---|---|
| **Negro compuesto** | **Es un distribuidor de VÍDEO**: espera una señal de vídeo compuesto y su ancho de banda y sus niveles son otros |
| **SDI** | **Es DIGITAL SERIE a cientos de megabits**: reclockea y no dejará pasar una señal de audio |
| **AES3** | **También digital**: espera una trama de audio digital, no una señal analógica |

**La lección que deja, y sirve para todo el tema 15**: **una avería se resuelve sabiendo qué clase de
señal es la que falta, no qué etiqueta lleva el conector.**

## 6. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 42 | Función de los bits P3 a P0 de la palabra XYZ | c) Bits de protección ✔ |
| 45 | Para qué se usa el protocolo PTP | d) Sincronismo de relojes ✔ |
| 67 | Dónde informa el HD-SDI del número de línea | b) Tras el EAV, con LN0 y LN1 ✔ |
| 71 | Bit rate de una señal AES3 a 48 kHz | b) 3,072 Mbps ✔ |
| 81 | Qué estándar define el MADI | b) AES-10 ✔ **·** verificado en la AES |
| 84 | Orden de las cuatro palabras de EAV y SAV | b) 3FF – 000 – 000 – XYZ ✔ |
| 91 | Canales que transporta el MADI en un cable | c) 64 ✔ |
| 92 | Qué es el protocolo NTP | a) Protocolo de internet para sincronizar relojes ✔ |
| 8 (2.º llam.) | Bitrate de una señal AES-10 a 48.000 muestras | a) 125 Mbps ✔ |
| 20 (2.º llam.) | Qué distribuidor sustituye al de código de tiempo | b) El de audio analógico ✔ |

**Las diez respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Es el punto grande más limpio de la ocupación**, y **la razón es la misma que en el tema 6: ninguna
de sus diez preguntas lleva figura.**

**Y el aviso de estudio**: **cuatro de las diez son cifras que hay que memorizar** —3,072 Mbps, 125
Mbps, 64 canales, 11 bits de contador— **y las otras seis se razonan.**

## 7. Trazabilidad

**Este tema no cita ninguna norma articulada**, y **cita la presentación pública de las normas de la
AES.**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Segundo: organismo de normalización** | **Presentación de las normas de la Audio Engineering Society** (`fuentes/normas-tecnicas/AES-normas-de-audio.md`) | **Que el MADI es la AES10, que la AES3 es la de dos canales y que la AES12 no figura en su relación**, citado literal. **Nada de su contenido interno** |

**Cuatro declaraciones expresas:**

1. **El texto de las normas AES3, AES10 y AES11 está tras un muro de pago y no se ha leído**, y **así
   consta ya en `fuentes/normas-tecnicas/AES-normas-de-audio.md`.** **Las cifras de este tema —32 bits
   por subcuadro, 3,072 Mbps, 125 Mbps, 64 canales— coinciden con las respuestas oficiales y con el
   uso universal del sector**, y **el temario NO las atribuye a un apartado de esas normas.**
2. **Las normas SMPTE 259M, 292M y 424M tampoco se han consultado.** **Este proyecto tiene volcado el
   índice de la familia SMPTE ST 2110 con los títulos oficiales de cada parte**, no estas tres. **La
   estructura de los patrones EAV y SAV, el desglose de la palabra XYZ y la ubicación del número de
   línea que este tema describe coinciden con las respuestas oficiales y son de uso universal**, y **se
   presentan como conocimiento común de la materia.**
3. **Los caudales de las tres normas del epígrafe 1 son los nominales de cada generación**, dados como
   orden de magnitud. **Ninguna pregunta depende de ellos.**
4. **La precisión del PTP y la del NTP son órdenes de magnitud de uso corriente.** **El estándar IEEE
   1588 no se ha consultado**, y **lo que las preguntas 45 y 92 miden es para qué sirve cada uno, que
   es inequívoco.**

**El resto del tema va como oficio y así se declara**: la razón de que 000 y 3FF sean valores
reservados, por qué cuatro bits protegen a tres, la diferencia entre un caudal que depende del
contenido y uno de velocidad de línea fija, la tabla de señales de sincronismo y el razonamiento de la
avería del distribuidor. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
