# Esquema · Tema 18 del específico de Técnica Informática · Sistemas multimedia y codificación de ficheros audiovisuales

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio audiovisual · `[exam]` =
opciones del propio cuadernillo. **Siglas**: la modulación por impulsos codificados (**PCM**); el
códec libre de audio sin pérdida (**FLAC**) y el equivalente de Apple (**ALAC**); la interfaz visual
digital (**DVI**), la interfaz multimedia de alta definición (**HDMI**) y el **DisplayPort**; la
codificación avanzada de audio (**AAC**) y la capa 3 del estándar del grupo de expertos en imágenes en
movimiento (**MP3**); el códec de vídeo de alta eficiencia (**HEVC**); los formatos y contenedores que
se nombran por su extensión (**WAV**, **AIFF**, **MP4**, **MKV**, **MOV**, **AVI**); y el kilohercio
(**kHz**).

**Cabecera.** Enunciado: punto 21 del anexo · **4 preguntas** · **ninguna lleva figura** · **es el
punto donde la informática de esta ocupación se cruza con el oficio audiovisual de la casa**: **dos de
audio digital, una de vídeo y una de conectores.**

<!-- indice -->

## Índice

- [Relación de aspecto](#relación-de-aspecto)
- [Muestreo](#muestreo)
- [Compresión de audio](#compresión-de-audio)
- [Interfaces de vídeo](#interfaces-de-vídeo)
- [Arquitectura de un sistema multimedia](#arquitectura-de-un-sistema-multimedia)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Relación de aspecto

- **PREGUNTA 27** · `[exam]` · **La panorámica de las pantallas modernas es 16:9.**

| Relación | Qué es |
|---|---|
| **4:3** | **La de la televisión analógica y los monitores antiguos** |
| **1:1** | **Cuadrada**: red social, no televisión |
| **16:9** | **La panorámica de la televisión digital** ✔ |
| **5:4** | **Monitor informático antiguo**, casi cuadrado |

- **CÓMO SE LEE**: **el primer número es el ancho y el segundo el alto**, en la misma unidad.
- **POR QUÉ LA TRANSICIÓN FUE DOLOROSA**: **16:9 es aproximadamente 1,78 y 4:3 es 1,33.** **Ni una
  cabe dentro de la otra**, y de ahí las bandas negras al mezclar material de las dos épocas.

## Muestreo

- **PREGUNTA 44** · `[exam]` · **Con muestreo a 48 kHz el límite superior es 24 kHz.**
- **ES APLICACIÓN DIRECTA DEL TEOREMA DEL MUESTREO**: **hay que muestrear a más del doble de la
  frecuencia más alta**; **al revés, la más alta representable es la mitad de la de muestreo.** **48
  entre 2 son 24.** **Ese límite tiene nombre: frecuencia de Nyquist.**

| Opción falsa | De dónde sale |
|---|---|
| **48 kHz** | **Confundir la frecuencia de muestreo con el límite** |
| **96 kHz** | **Multiplicar por dos en vez de dividir** |
| **Depende de la resolución de cuantificación** | **Confunde los dos ejes**: los bits por muestra fijan el rango dinámico, no el ancho de banda |

| Parámetro | Qué determina | Regla |
|---|---|---|
| **Frecuencia de muestreo** | **Hasta qué frecuencia llega el sonido** | **La mitad de ella** ✔ |
| **Bits por muestra** | **Cuánto rango dinámico hay** | **Unos 6 decibelios por bit** |

- **LAS CORRIENTES, PARA SITUAR LA DEL ENUNCIADO**: **44,1 kHz en el disco compacto, 48 kHz en vídeo
  profesional, 96 y 192 kHz en alta resolución.**

## Compresión de audio

- **PREGUNTA 64** · `[exam]` · **FLAC y ALAC usan compresión sin pérdida.**

| Familia | Qué hace | Ejemplos |
|---|---|---|
| **Sin comprimir** | **Guarda las muestras tal cual** | **WAV**, **AIFF** |
| **Sin pérdida** | **Comprime y devuelve el original bit a bit** | **FLAC**, **ALAC** ✔ |
| **Con pérdida** | **Descarta lo que el oído no va a notar** | **MP3**, **AAC** |

- **LO QUE DELATA LA RESPUESTA ESTÁ EN EL NOMBRE**: **la primera letra de FLAC es de *free* y la
  segunda de *lossless*, sin pérdida.** **ALAC es el equivalente de la casa Apple.**
- **LAS DOS FALSAS QUE NOMBRAN TÉCNICAS REALES**: **la codificación perceptual es la de la compresión
  CON pérdida** —aprovecha el enmascaramiento del oído—; **y la compresión de dinámica no es
  compresión de datos: es un proceso de sonido** que reduce la diferencia entre lo fuerte y lo flojo.
- **EL AVISO DE VOCABULARIO QUE ESTE PUNTO DEJA**: **«comprimir» significa una cosa en un fichero y
  otra en una mesa de sonido.** **Es el falso amigo más frecuente entre el informático y el técnico de
  sonido de la misma casa.**

## Interfaces de vídeo

- **PREGUNTA 69** · `[exam]` · **La afirmación incorrecta es que HDMI transporte vídeo analógico.**

| Interfaz | Vídeo | Audio | Rasgo |
|---|---|---|---|
| **DVI** | **Analógico y digital**, según variante | **No** | **Nació en la transición**: DVI-A analógica, DVI-D digital, DVI-I las dos |
| **HDMI** | **Sólo digital** ✔ | **Sí** | **El estándar del equipo doméstico** |
| **DisplayPort** | **Sólo digital** | **Sí** | **El del mundo informático**, con retención mecánica en el conector grande |

- **LAS OTRAS DOS OPCIONES SON CIERTAS**: **HDMI sí lleva audio** —lo que lo impuso frente a DVI en el
  salón— **y el conector grande de DisplayPort sí suele llevar pestillo.**

## Arquitectura de un sistema multimedia

| Capa | Qué hace |
|---|---|
| **Captación y digitalización** | **Convierte el mundo en muestras** |
| **Codificación** | **Reduce el tamaño**, con o sin pérdida |
| **Contenedor** | **Empaqueta vídeo, audio, subtítulos y metadatos** |
| **Transporte y reproducción** | **Lleva el fichero al reproductor y lo descodifica** |

| | **Códec** | **Contenedor** |
|---|---|---|
| **Qué es** | **El algoritmo que comprime y descomprime** | **El formato de fichero que lo envuelve todo** |
| **Ejemplos** | **H.264**, **HEVC**, **AAC**, **FLAC** | **MP4**, **MKV**, **MOV**, **AVI** |

- **EL ERROR CORRIENTE QUE ESA DISTINCIÓN EVITA**: **un fichero con extensión `.mp4` no dice qué códec
  lleva dentro.** **Dos ficheros con la misma extensión pueden necesitar descodificadores distintos**,
  y **ésa es la causa de la mitad de los «no me reproduce» de una redacción.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 27 | Relación de aspecto panorámica | c) 16:9 ✔ |
| 44 | Límite superior con muestreo a 48 kHz | c) 24 kHz ✔ |
| 64 | Codificación de FLAC y ALAC | d) Compresión sin pérdida ✔ |
| 69 | Afirmación incorrecta sobre interfaces | b) Que HDMI transporte vídeo analógico ✔ |

**Las cuatro oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**una es cálculo —la mitad de la frecuencia de muestreo— y las otras tres son tablas.** **La de
familias de compresión y la de interfaces contestan dos preguntas y caben en diez líneas.**
