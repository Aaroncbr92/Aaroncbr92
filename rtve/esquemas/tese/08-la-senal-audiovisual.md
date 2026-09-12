# Esquema · Tema 8 del específico de Técnica de Equipos y Sistemas Electrónicos · La señal audiovisual y sus sincronismos

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalación · `[norma]` =
presentación pública de una norma de organismo técnico. **Siglas**: la interfaz digital serie (**SDI**)
y su versión de alta definición (**HD-SDI**); la Sociedad de Ingenieros de Cine y Televisión
(**SMPTE**); la interfaz digital multicanal de audio (**MADI**) y las normas de la Sociedad de
Ingeniería de Audio (**AES3**, **AES-10** y **AES11**); el final y el comienzo de vídeo activo
(**EAV** y **SAV**); los identificadores de número de línea (**LN0** y **LN1**); la palabra de estado
de una interfaz digital (**XYZ**); el protocolo de tiempo de precisión (**PTP**) y el de red (**NTP**);
los megabits por segundo (**Mbps**); y el negro compuesto (*black burst*, **BB**).

**Cabecera.** Enunciado: punto 10 del anexo · **10 preguntas: el segundo banco de la ocupación** ·
**ninguna lleva figura, y es el punto grande más limpio del volumen.**

<!-- indice -->

## Índice

- [Las tres normas del SDI](#las-tres-normas-del-sdi)
- [Los patrones EAV y SAV](#los-patrones-eav-y-sav)
- [El audio digital y sus caudales](#el-audio-digital-y-sus-caudales)
- [Los sincronismos](#los-sincronismos)
- [La avería del distribuidor](#la-avería-del-distribuidor)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las tres normas del SDI

| Norma | Caudal | Para qué |
|---|---|---|
| **SMPTE 259M** | **270 Mbps** | **Definición estándar** |
| **SMPTE 292M** | **1,485 Gbps** | **Alta definición** |
| **SMPTE 424M** | **2,97 Gbps** | **1080p a 50 y 60 cuadros** |

- **LA IDEA QUE LAS UNE**: **cada generación dobla aproximadamente el caudal de la anterior.**

## Los patrones EAV y SAV

- **PREGUNTA 84** · `[of]` · **El orden de las cuatro palabras es 3FF – 000 – 000 – XYZ.**
- **POR QUÉ 3FF Y 000**: **son valores reservados que no puede tomar ninguna muestra de imagen**, de
  modo que su aparición sólo puede significar «aquí empieza una marca».
- **PREGUNTA 42** · `[of]` · **Los bits P3 a P0 de la palabra XYZ son bits de protección.**
- **CUATRO BITS PROTEGEN A TRES**: **es redundancia suficiente para corregir un error y detectar dos.**
- **PREGUNTA 67** · `[of]` · **El HD-SDI informa del número de línea tras el EAV, con LN0 y LN1.**

## El audio digital y sus caudales

- **PREGUNTA 71** · `[of]` · **Una señal AES3 a 48 kHz da 3,072 Mbps.** **Dos canales × 48.000 × 32
  bits por subcuadro.**
- **PREGUNTA 8 del segundo llamamiento** · `[of]` · **Una señal AES-10 a 48.000 muestras da 125 Mbps.**
- **PREGUNTA 91** · `[norma]` · **El MADI transporta 64 canales en un cable.**
- **PREGUNTA 81** · `[norma]` · **El estándar que define el MADI es la AES-10.** **Verificado en la
  presentación pública de normas de la Sociedad de Ingeniería de Audio**, donde consta además que la
  AES12 no figura en su relación.

## Los sincronismos

| Señal | Qué sincroniza |
|---|---|
| **Negro compuesto y trinivel** | **El cuadro y la línea del vídeo** |
| **Word clock y AES11** | **La frecuencia de muestreo del audio** |
| **Código de tiempo** | **La posición temporal** |
| **PTP** | **Relojes de una red, con precisión de microsegundos** ✔ |
| **NTP** | **Relojes por internet, con precisión de milisegundos** |

- **PREGUNTA 45** · `[of]` · **El PTP se usa para sincronismo de relojes.**
- **PREGUNTA 92** · `[of]` · **El NTP es un protocolo de internet para sincronizar relojes.**
- **CÓMO NO CONFUNDIRLOS**: **los dos sincronizan relojes; el PTP es el fino y el de instalación, y el
  NTP es el basto y el de internet.**

## La avería del distribuidor

- **PREGUNTA 20 del segundo llamamiento** · `[of]` · **El distribuidor que sustituye al de código de
  tiempo es el de audio analógico.**
- **POR QUÉ**: **el código de tiempo longitudinal es, eléctricamente, una señal de audio.** **Un
  distribuidor de audio analógico la reparte sin enterarse de que es otra cosa.**
- **LO QUE ESTA PREGUNTA ENSEÑA**: **conocer la naturaleza eléctrica de una señal permite improvisar
  con lo que hay**, que es la mitad del oficio en un directo.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
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

**Las diez oficiales son correctas** y **ninguna descansa sólo en la plantilla.** · **Aviso de
estudio**: **cuatro de las diez son cifras que hay que memorizar** —3,072 Mbps, 125 Mbps, 64 canales y
los cuatro bits de protección— **y las otras seis se razonan.**
