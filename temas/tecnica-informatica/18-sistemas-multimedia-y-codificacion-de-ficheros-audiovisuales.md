# Tema 18 del específico de Técnica Informática · Sistemas multimedia y codificación de ficheros audiovisuales

Las siglas de este tema, presentadas de entrada: la modulación por impulsos codificados (**PCM**,
*pulse code modulation*); el códec libre de audio sin pérdida (**FLAC**) y el equivalente de Apple
(**ALAC**); la interfaz visual digital (**DVI**), la interfaz multimedia de alta definición (**HDMI**)
y el **DisplayPort**; la codificación avanzada de audio (**AAC**) y la capa 3 del estándar del grupo de
expertos en imágenes en movimiento (**MP3**); el códec de vídeo de alta eficiencia (**HEVC**); los
formatos de fichero y contenedores, que se nombran por su extensión (**WAV**, **AIFF**, **MP4**,
**MKV**, **MOV** y **AVI**) y de los que el temario no desarrolla las iniciales; el kilohercio
(**kHz**); y la relación de aspecto, que se escribe con dos
números separados por dos puntos.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 21):
> «Sistemas Multimedia. Arquitectura. Codificación de ficheros de A/V.»

**Cuatro preguntas.** **Y son el punto donde la informática de esta ocupación se cruza con el oficio
audiovisual de la casa**: **dos son de audio digital, una de vídeo y una de conectores.**

**Ese cruce merece una advertencia de método**: **las cuatro preguntas de este punto se contestan con
material que este proyecto ya tiene escrito** para Sonido, para Edición y Montaje y para Técnica de
Equipos y Sistemas Electrónicos. **Lo que aquí se hace es reunirlo desde la mirada del informático.**

<!-- indice -->

## Índice

- [1. La relación de aspecto](#1-la-relación-de-aspecto)
- [2. El audio digital y el teorema del muestreo](#2-el-audio-digital-y-el-teorema-del-muestreo)
- [3. La compresión de audio](#3-la-compresión-de-audio)
- [4. Las interfaces de vídeo](#4-las-interfaces-de-vídeo)
- [5. La arquitectura de un sistema multimedia](#5-la-arquitectura-de-un-sistema-multimedia)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. La relación de aspecto

**La pregunta 27**: **la relación de aspecto de vídeo que se considera panorámica y se utiliza en la
mayoría de pantallas modernas es 16:9.** Ésa es la respuesta oficial.

---

**Las cuatro relaciones de la pregunta, con lo que fue cada una:**

| Relación | Qué es |
|---|---|
| **4:3** | **La de la televisión analógica y los monitores antiguos** |
| **1:1** | **Cuadrada**: formatos de red social, no de televisión |
| **16:9** | **La panorámica de la televisión digital y de casi toda pantalla actual** ✔ |
| **5:4** | **Una variante de monitor informático antiguo**, casi cuadrada |

**Cómo se lee la notación**: **el primer número es el ancho y el segundo el alto**, en la misma
unidad. **16:9 significa que por cada dieciséis de ancho hay nueve de alto.**

**Y el dato que las relaciona, porque explica por qué la transición fue dolorosa**: **16:9 es
aproximadamente 1,78 y 4:3 es 1,33.** **Ni una cabe dentro de la otra**, y de ahí las bandas negras
laterales o superiores cuando se mezcla material de las dos épocas.

## 2. El audio digital y el teorema del muestreo

**La pregunta 44**: **en un fichero de audio codificado en PCM lineal con una frecuencia de muestreo de
48 kHz, el límite superior de las frecuencias que puede contener es 24 kHz.** Ésa es la respuesta
oficial.

---

**Y es aplicación directa del teorema del muestreo**: **para representar una señal hay que muestrear a
más del doble de su frecuencia más alta.** **Al revés: la frecuencia más alta representable es la
mitad de la de muestreo.** **48 dividido entre 2 son 24.**

**Ese límite tiene nombre propio**: **frecuencia de Nyquist**, y **es la mitad de la frecuencia de
muestreo.**

**Las tres opciones falsas y su porqué:**

| Opción | De dónde sale |
|---|---|
| **a) 48 kHz** | **Confundir la frecuencia de muestreo con el límite** |
| **b) 96 kHz** | **Multiplicar por dos en vez de dividir** |
| **d) Depende de la resolución de cuantificación** | **Confunde los dos ejes**: los bits por muestra fijan el rango dinámico, no el ancho de banda |

**Y la opción d merece detenerse, porque es la buena trampa**: **un fichero de audio tiene dos
parámetros independientes**, y **cada uno gobierna una cosa distinta:**

| Parámetro | Qué determina | Regla |
|---|---|---|
| **Frecuencia de muestreo** | **Hasta qué frecuencia llega el sonido** | **La mitad de ella** ✔ |
| **Bits por muestra** | **Cuánto rango dinámico hay** | **Unos 6 decibelios por bit** |

**Las frecuencias de muestreo corrientes, para situar la de la pregunta**: **44,1 kHz en el disco
compacto, 48 kHz en el vídeo profesional, 96 y 192 kHz en producción de alta resolución.**

## 3. La compresión de audio

**La pregunta 64**: **en la codificación de los formatos de audio FLAC y ALAC se utiliza compresión sin
pérdida.** Ésa es la respuesta oficial.

---

**Las tres familias, que es el cuadro que hay que llevar:**

| Familia | Qué hace | Ejemplos |
|---|---|---|
| **Sin comprimir** | **Guarda las muestras tal cual** | **WAV**, **AIFF** |
| **Comprimida sin pérdida** | **Comprime y devuelve el original bit a bit** | **FLAC**, **ALAC** ✔ |
| **Comprimida con pérdida** | **Descarta lo que el oído no va a notar y no lo devuelve** | **MP3**, **AAC** |

**Lo que delata la respuesta está en el propio nombre**: **la primera letra de FLAC es de *free* y la
segunda de *lossless*, sin pérdida.** **ALAC es el equivalente de la casa Apple, con la misma
palabra.**

**Y las dos opciones falsas que nombran técnicas reales:**

- **La codificación perceptual es la de la compresión CON pérdida**: **aprovecha el enmascaramiento
  del oído para tirar lo que no se va a oír.** **Es lo que hacen MP3 y AAC**, no FLAC.
- **La compresión de dinámica no es compresión de datos**: **es un proceso de sonido** que reduce la
  diferencia entre lo fuerte y lo flojo. **El mismo término significa dos cosas distintas en
  informática y en audio**, y **ésa es exactamente la trampa de la opción.**

**El aviso de vocabulario que este tema deja**: **«comprimir» significa una cosa en un fichero y otra
en una mesa de sonido.** **Es el falso amigo más frecuente entre el informático y el técnico de
sonido de la misma casa.**

## 4. Las interfaces de vídeo

**La pregunta 69 es negativa**: **de las afirmaciones sobre interfaces de vídeo, la incorrecta es que
HDMI pueda transportar señal de vídeo tanto analógica como digital.** Ésa es la respuesta oficial.

---

**Las tres interfaces de la pregunta, frente a frente:**

| Interfaz | Vídeo | Audio | Rasgo |
|---|---|---|---|
| **DVI** | **Analógico y digital**, según la variante | **No** | **Nació en la transición**, y por eso hay variantes de un tipo, del otro y de los dos |
| **HDMI** | **Sólo digital** ✔ | **Sí** | **El estándar del equipo doméstico** |
| **DisplayPort** | **Sólo digital** | **Sí** | **El del mundo informático**, con retención mecánica en el conector de tamaño completo |

**Y de ahí sale la respuesta**: **la que es falsa es la de HDMI, porque nunca llevó vídeo analógico.**
**Las variantes de DVI sí**: **DVI-A es analógica, DVI-D digital y DVI-I las dos.**

**Las otras dos opciones son ciertas y conviene saber por qué**: **HDMI sí lleva audio**, que es
precisamente lo que lo impuso frente a DVI en el salón; **y el conector grande de DisplayPort sí suele
llevar un pestillo de retención**, que es su rasgo distintivo frente al de HDMI.

## 5. La arquitectura de un sistema multimedia

**El enunciado pide «arquitectura» y el examen no ha entrado.** **Las cuatro capas de cualquier
sistema de este tipo:**

| Capa | Qué hace |
|---|---|
| **Captación y digitalización** | **Convierte el mundo en muestras**: muestreo y cuantificación |
| **Codificación** | **Reduce el tamaño**, con o sin pérdida |
| **Contenedor** | **Empaqueta vídeo, audio, subtítulos y metadatos en un fichero** |
| **Transporte y reproducción** | **Lleva el fichero al reproductor y lo descodifica** |

**Y la distinción que más se confunde en este punto**: **códec no es lo mismo que contenedor.**

| | **Códec** | **Contenedor** |
|---|---|---|
| **Qué es** | **El algoritmo que comprime y descomprime** | **El formato de fichero que lo envuelve todo** |
| **Ejemplos** | **H.264**, **HEVC**, **AAC**, **FLAC** | **MP4**, **MKV**, **MOV**, **AVI** |

**El error corriente que esa distinción evita**: **un fichero con extensión `.mp4` no dice qué códec
lleva dentro.** **Dos ficheros con la misma extensión pueden necesitar descodificadores distintos**, y
**ésa es la causa de la mitad de los «no me reproduce» de una redacción.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 27 | Relación de aspecto panorámica de las pantallas modernas | c) 16:9 ✔ |
| 44 | Límite superior de frecuencias con muestreo a 48 kHz | c) 24 kHz ✔ |
| 64 | Qué se usa en la codificación de FLAC y ALAC | d) Compresión sin pérdida ✔ |
| 69 | Afirmación incorrecta sobre interfaces de vídeo | b) Que HDMI transporte vídeo analógico ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **una de las cuatro es cálculo** —la mitad de la frecuencia de muestreo— **y
las otras tres son tablas.** **La de familias de compresión de audio y la de interfaces de vídeo
contestan dos preguntas y caben en diez líneas.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **El teorema del muestreo es un resultado clásico del tratamiento de señales**, presentado como
   conocimiento común. **El cálculo de la pregunta 44 no se toma de ninguna fuente: se hace**, y su
   resultado coincide con la respuesta oficial.
2. **Las especificaciones de DVI, HDMI y DisplayPort no se han consultado.** **Lo que el tema afirma
   de cada una —qué señales lleva y qué rasgo la distingue— es de uso universal**, y **coincide con
   la respuesta oficial de la pregunta 69**, cuyas tres opciones verdaderas proceden del propio
   enunciado.
3. **FLAC, ALAC, MP3, AAC, WAV, AIFF y los contenedores citados son nombres de formato**, referidos
   por su categoría. **No se ha consultado la especificación de ninguno**, y **la clasificación en
   tres familias es de uso universal.**
4. **La equivalencia de unos seis decibelios de rango dinámico por bit es un orden de magnitud
   corriente**, dado como referencia. **Ninguna pregunta depende de ella**, y **el tema 9 del
   específico de Sonido la desarrolla.**
5. **Las frecuencias de muestreo corrientes del epígrafe 2 son de uso universal**, dadas para situar
   la del enunciado.

**El resto del tema va como oficio y así se declara**: la lectura de la notación de relación de
aspecto, la explicación de por qué 4:3 y 16:9 no encajan, el desmontaje de las opciones falsas de la
pregunta 44, el aviso sobre el doble sentido de la palabra «comprimir», la tabla de capas de un
sistema multimedia y la distinción entre códec y contenedor. **Nada de eso está en un boletín oficial
ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
