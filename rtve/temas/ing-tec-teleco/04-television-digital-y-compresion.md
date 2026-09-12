# Tema 4 del específico de Ingeniería Técnica · Telecomunicación · Televisión digital y compresión

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 4 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son las familias de difusión y de compresión, **de acceso restringido**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Desajuste declarado** | **El enunciado pide servicios interactivos, acceso condicional y televisión móvil**, y **el examen ha entrado sólo por compresión y familia de normas** |
| **Extensión** | **1.893 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la difusión de vídeo digital (**DVB**) y sus
variantes terrestre (**DVB-T**), por satélite (**DVB-S**), por cable (**DVB-C**) y por red
(**DVB-IP**); el grupo de expertos en imágenes en movimiento (**MPEG**) y sus normas segunda y cuarta
(**MPEG-2** y **MPEG-4**); la codificación de vídeo avanzada (**AVC**) y la de alta eficiencia
(**HEVC**); el grupo conjunto de expertos en fotografía y su norma del año 2000 (**JPEG2000**); la
modulación por impulsos codificados (**PCM**); el acceso condicional (**CA**); la guía electrónica de
programación (**EPG**); y el flujo de transporte (**TS**, *transport stream*); y las
interfaces digitales serie de definición estándar y de alta definición (**SD/HD-SDI**), del
tema 3.

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 4):
> «Señal Televisión Digital. Sistemas de contribución, distribución y difusión. Servicios interactivos
> y acceso condicional. Estándar DVB. Estándares de TV móvil.»

**Cuatro preguntas.** **Y las cuatro son de compresión y de familia de normas**: **de servicios
interactivos, de acceso condicional y de televisión móvil no ha caído ninguna.**

<!-- indice -->

## Índice

- [1. Las tres cadenas: contribución, distribución y difusión](#1-las-tres-cadenas-contribución-distribución-y-difusión)
- [2. La familia de normas](#2-la-familia-de-normas)
- [3. Los estándares de compresión](#3-los-estándares-de-compresión)
- [4. La asimetría de la compresión](#4-la-asimetría-de-la-compresión)
- [5. El acceso condicional y los servicios interactivos](#5-el-acceso-condicional-y-los-servicios-interactivos)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Las tres cadenas: contribución, distribución y difusión

**El enunciado las nombra en ese orden y son tres cosas distintas**, con exigencias opuestas:

| Cadena | De dónde a dónde | Qué prima | Compresión |
|---|---|---|---|
| **Contribución** | **Del lugar de la noticia al centro de producción** | **Calidad y latencia baja** | **Poca o ninguna** |
| **Distribución** | **Del centro a los emisores o a las cabeceras** | **Fiabilidad** | **Media** |
| **Difusión** | **Del emisor al espectador** | **Alcanzar a muchos con poco ancho de banda** | **Mucha** |

**La regla que las ordena y que un examen puede pedir**: **cuanto más cerca del espectador, más
compresión.** **Y al revés: una señal muy comprimida no se puede volver a procesar sin que se note**,
y por eso la contribución conserva calidad aunque cueste caudal.

**El concepto que se deriva y que conviene tener claro**: **cada recodificación degrada.** **Una señal
que se comprime, se descomprime, se edita y se vuelve a comprimir acumula pérdidas**, y **por eso las
cadenas serias intentan comprimir una sola vez, lo más tarde posible.**

## 2. La familia de normas

**La pregunta 60 es negativa**: **de los sistemas enumerados, el que NO está soportado por la norma
DVB es DVB-A.** Ésa es la respuesta oficial.

---

**Y la familia entera se nombra por el medio, con una letra:**

| Variante | Medio |
|---|---|
| **DVB-S** y **DVB-S2** | **Satélite** |
| **DVB-T** y **DVB-T2** | **Terrestre** ✔ |
| **DVB-C** y **DVB-C2** | **Cable** |
| **DVB-H** | **Portátil**, para televisión móvil |
| **DVB-IP** | **Red de datos** |
| **DVB-A** | **No existe** ✔ |

**La regla que la contesta sin conocer la familia**: **las letras de la familia nombran MEDIOS de
transmisión.** **Satélite, terrestre y cable son medios; la letra «a» no nombra ninguno.**

**Y la observación que conviene añadir**: **la televisión móvil que el enunciado pide se corresponde
con la variante portátil**, que **se normalizó y apenas se desplegó**: **el vídeo en el móvil acabó
yendo por la red de datos y no por difusión.** **Es un caso de norma técnica correcta que el mercado
no adoptó**, y merece saberse porque el enunciado la nombra.

## 3. Los estándares de compresión

**La pregunta 79**: **de los enumerados, el estándar de compresión de vídeo utilizado en televisión
digital es MPEG-2.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son de otras materias**, lo que **convierte la pregunta en un ejercicio
de reconocer a qué familia pertenece cada nombre:**

| Opción | Qué es |
|---|---|
| **PCM-2** | **No existe**: la modulación por impulsos codificados es de audio y no lleva versión |
| **MPEG-2** | **Compresión de vídeo** ✔ |
| **AES3id** | **Audio digital por coaxial**, del tema 3 |
| **SD/HD-SDI** | **Interfaces de transporte SIN comprimir**, del tema 3 |

**La generación de cada norma y dónde se usa, que es lo que la pregunta 44 pide:**

| Norma | Generación | Dónde |
|---|---|---|
| **MPEG-2** | **Primera de difusión** | **Televisión digital terrestre de primera generación, disco de vídeo digital** ✔ |
| **MPEG-4 AVC**, o H.264 | **Segunda** | **Televisión digital terrestre de segunda generación, disco de alta definición, internet** ✔ |
| **HEVC**, o H.265 | **Tercera** | **Ultraalta definición** |
| **JPEG2000** | **Intracuadro** | **Contribución y archivo** ✔ |

**La pregunta 44**: **el formato de vídeo de la televisión digital terrestre bajo el estándar DVB-T2 es
MPEG-4 AVC.** Ésa es la respuesta oficial.

---

**Y conviene ver la pareja completa, porque es la que se pregunta**: **la primera generación terrestre
lleva MPEG-2 y la segunda lleva MPEG-4 AVC.** **La opción de la tercera generación es la trampa
moderna**: **es la que se usa en ultraalta definición, no la que la norma de segunda generación fija
como formato de vídeo.**

**La pregunta 40**: **el formato de compresión que trabaja con menos retardo es JPEG2000.** Ésa es la
respuesta oficial.

---

**Y la razón está en cómo comprime cada uno**, que es la distinción central del punto:

| | **Compresión intracuadro** | **Compresión intercuadro** |
|---|---|---|
| **Qué comprime** | **Cada imagen por separado** | **Las diferencias entre imágenes** |
| **Retardo** | **Muy bajo: no espera a las siguientes** ✔ | **Alto: necesita un grupo de imágenes** |
| **Eficiencia** | **Menor** | **Mucho mayor** |
| **Editar un fotograma** | **Directo** | **Hay que reconstruir el grupo** |
| **Ejemplos** | **JPEG2000** | **MPEG-2, AVC, HEVC** |

**Por eso la contribución usa la primera y la difusión la segunda**, que es exactamente lo que el
epígrafe 1 anticipaba: **la contribución paga caudal para no pagar retardo.**

**El grupo de imágenes, que conviene entender porque explica el retardo:**

| Tipo de imagen | De qué depende |
|---|---|
| **Intra** | **De nada: se descodifica sola** |
| **Predicha** | **De la anterior** |
| **Bidireccional** | **De la anterior Y de la siguiente** ✔ |

**La última es la que introduce el retardo**: **para descodificarla hay que tener ya la siguiente**,
y **eso obliga a esperar.** **Un grupo largo comprime mejor y retarda más.**

## 4. La asimetría de la compresión

**La pregunta 71**: **la carga computacional es muy superior al comprimir la señal de vídeo que al
descomprimirla.** Ésa es la respuesta oficial.

---

**Y es una de las mejores preguntas del examen**, porque **pide entender un principio de diseño y no
recordar un dato.**

**Por qué es así**: **comprimir exige BUSCAR.** **El codificador prueba particiones, modos de
predicción y vectores de movimiento, y elige el que menos bits gasta.** **Descomprimir sólo exige
EJECUTAR lo que el codificador ya decidió**, porque **las decisiones vienen escritas en el propio
flujo.**

**Y la razón por la que esa asimetría es DELIBERADA**: **hay un codificador y millones de
descodificadores.** **Conviene poner el trabajo caro donde sólo hay una máquina.**

**Las tres opciones falsas y por qué caen:**

| Opción | Por qué es falsa |
|---|---|
| **La carga es simétrica** | **No lo es en ninguno de los códecs de difusión** |
| **Depende de que sea el mismo algoritmo** | **La asimetría no depende de eso: es del diseño** |
| **Es muy superior al descomprimir** | **Es exactamente al revés** |

**El aviso práctico que se deriva**: **un equipo puede reproducir sin problema un formato que no puede
grabar en tiempo real.** **Es la razón de que una tableta reproduzca ultraalta definición y no pueda
codificarla.**

## 5. El acceso condicional y los servicios interactivos

**El enunciado los nombra y el examen no ha entrado.** **Lo mínimo que conviene llevar visto:**

**El acceso condicional, en tres piezas:**

| Pieza | Qué hace |
|---|---|
| **Aleatorizador** | **Cifra el flujo con una palabra de control que cambia cada pocos segundos** |
| **Mensajes de derechos** | **Dicen a qué tiene derecho cada abonado** |
| **Tarjeta o módulo del abonado** | **Descifra la palabra de control si el abonado tiene derecho** |

**La idea que lo hace robusto**: **lo que viaja cifrado con una clave que cambia cada pocos segundos
es el contenido; lo que identifica al abonado va por otro camino.** **Romper una palabra de control
sirve para unos segundos y para nada más.**

**Los servicios interactivos que la familia de normas define:**

| Servicio | Qué es |
|---|---|
| **Guía electrónica de programación** | **La parrilla que el receptor muestra, transmitida en el propio flujo** |
| **Teletexto digital y aplicaciones** | **Contenido navegable sobre la emisión** |
| **Televisión híbrida** | **Aplicaciones que combinan la emisión con contenido de internet** |

**Y la observación que ordena el epígrafe**: **lo interactivo de verdad llegó por la red y no por la
difusión.** **La norma preveía un canal de retorno; lo que ocurrió es que el espectador ya tenía otro
mucho mejor en el mismo salón.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 40 | Qué formato de compresión trabaja con menos retardo | d) JPEG2000 ✔ |
| 60 | Cuál NO está soportado por la norma DVB | c) DVB-A ✔ |
| 71 | Cómo es la carga computacional al descomprimir | b) Muy superior al comprimir que al descomprimir ✔ |
| 79 | Cuál es un estándar de compresión de vídeo | b) MPEG-2 ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **la distinción entre compresión intracuadro e intercuadro contesta una
pregunta y explica la otra.** **Y la tabla de la familia de normas se aprende en un minuto: las letras
son medios.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Las normas de la familia de difusión de vídeo digital y las de compresión no se han
   consultado**: su texto está tras un muro de pago o en organismos de normalización de acceso
   restringido. **Lo que el tema afirma de cada una es de uso universal en el sector**, y **coincide
   con las respuestas oficiales.**
2. **La asimetría entre codificar y descodificar se razona en el tema, no se toma de ninguna
   fuente**: **queda escrito por qué comprimir exige buscar y descomprimir sólo ejecutar.**
3. **La estructura del acceso condicional y la lista de servicios interactivos son de uso corriente en
   el sector**, y **ninguna respuesta oficial depende de ellas**: el examen no ha entrado por ahí.
4. **La observación sobre la variante portátil de la familia —norma correcta que el mercado no
   adoptó— es del temario**, y **ninguna respuesta depende de ella.**

**El resto del tema va como oficio y así se declara**: la regla de que a más cerca del espectador más
compresión, el aviso sobre la acumulación de pérdidas en recodificaciones sucesivas, la explicación
del grupo de imágenes y del retardo que introduce la imagen bidireccional, la razón de diseño de la
asimetría y la observación sobre el canal de retorno. **Nada de eso está en un boletín oficial ni en
una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
