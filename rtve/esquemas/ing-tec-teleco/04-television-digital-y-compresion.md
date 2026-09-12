# Esquema · Tema 4 del específico de Ingeniería Técnica · Telecomunicación · Televisión digital y compresión

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de televisión · `[exam]` =
opciones del propio cuadernillo · `[norma]` = norma técnica nombrada, sin cita literal. **Siglas**: la
difusión de vídeo digital (**DVB**) y sus variantes **DVB-T**, **DVB-S**, **DVB-C**, **DVB-H** y
**DVB-IP**; el grupo de expertos en imágenes en movimiento (**MPEG**), con **MPEG-2** y **MPEG-4**; la
codificación de vídeo avanzada (**AVC**) y la de alta eficiencia (**HEVC**); la norma del año 2000 del
grupo conjunto de expertos en fotografía (**JPEG2000**); la modulación por impulsos codificados
(**PCM**); la guía electrónica de programación (**EPG**); y las interfaces digitales serie de
definición estándar y alta definición (**SD/HD-SDI**).

**Cabecera.** Enunciado: puntos 4 del anexo · **4 preguntas** · **las cuatro de compresión y de familia
de normas** · **de servicios interactivos, acceso condicional y televisión móvil no ha caído ninguna.**

<!-- indice -->

## Índice

- [Las tres cadenas](#las-tres-cadenas)
- [La familia de normas](#la-familia-de-normas)
- [Los estándares de compresión](#los-estándares-de-compresión)
- [La asimetría de la compresión](#la-asimetría-de-la-compresión)
- [Acceso condicional e interactivos](#acceso-condicional-e-interactivos)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las tres cadenas

| Cadena | De dónde a dónde | Qué prima | Compresión |
|---|---|---|---|
| **Contribución** | **Del lugar de la noticia al centro** | **Calidad y latencia baja** | **Poca o ninguna** |
| **Distribución** | **Del centro a emisores o cabeceras** | **Fiabilidad** | **Media** |
| **Difusión** | **Del emisor al espectador** | **Muchos con poco ancho de banda** | **Mucha** |

- **LA REGLA** · `[of]` · **Cuanto más cerca del espectador, más compresión.**
- **LO QUE SE DERIVA** · `[of]` · **Cada recodificación degrada.** **Comprimir, descomprimir, editar y
  volver a comprimir acumula pérdidas**: **las cadenas serias comprimen una sola vez, lo más tarde
  posible.**

## La familia de normas

| Variante | Medio |
|---|---|
| **DVB-S** y **DVB-S2** · `[norma]` | **Satélite** |
| **DVB-T** y **DVB-T2** · `[norma]` | **Terrestre** |
| **DVB-C** y **DVB-C2** · `[norma]` | **Cable** |
| **DVB-H** · `[norma]` | **Portátil**, televisión móvil |
| **DVB-IP** · `[norma]` | **Red de datos** |
| **DVB-A** | **No existe** ✔ |

- **PREGUNTA 60, NEGATIVA** · `[exam]` · **El que NO está soportado es DVB-A.**
- **LA REGLA SIN CONOCER LA FAMILIA** · `[of]` · **Las letras nombran MEDIOS.** **Satélite, terrestre y
  cable son medios; la letra «a» no nombra ninguno.**
- **LA TELEVISIÓN MÓVIL DEL ENUNCIADO** · `[of]` · **La variante portátil se normalizó y apenas se
  desplegó**: **el vídeo en el móvil acabó yendo por la red de datos.** **Norma correcta que el mercado
  no adoptó.**

## Los estándares de compresión

| Opción | Qué es |
|---|---|
| **PCM-2** | **No existe**: la modulación por impulsos codificados es de audio y no lleva versión |
| **MPEG-2** | **Compresión de vídeo** ✔ |
| **AES3id** | **Audio digital por coaxial** |
| **SD/HD-SDI** | **Transporte SIN comprimir** |

- **PREGUNTA 79** · `[exam]` · **El estándar de compresión de vídeo de televisión digital es MPEG-2.**

| Norma | Generación | Dónde |
|---|---|---|
| **MPEG-2** | **Primera de difusión** | **Terrestre de primera generación, disco de vídeo digital** ✔ |
| **MPEG-4 AVC** | **Segunda** | **Terrestre de segunda generación, alta definición, internet** ✔ |
| **HEVC** | **Tercera** | **Ultraalta definición** |
| **JPEG2000** | **Intracuadro** | **Contribución y archivo** ✔ |

- **PREGUNTA 44** · `[exam]` · **El formato de vídeo de la terrestre de segunda generación es MPEG-4
  AVC.** **La trampa moderna es marcar la tercera generación**, que se usa en ultraalta definición pero
  no es lo que esa norma fija.
- **PREGUNTA 40** · `[exam]` · **El formato que trabaja con menos retardo es JPEG2000.**

| | **Intracuadro** | **Intercuadro** |
|---|---|---|
| **Qué comprime** | **Cada imagen por separado** | **Las diferencias entre imágenes** |
| **Retardo** | **Muy bajo** ✔ | **Alto: necesita un grupo** |
| **Eficiencia** | **Menor** | **Mucho mayor** |
| **Editar un fotograma** | **Directo** | **Hay que reconstruir el grupo** |
| **Ejemplos** | **JPEG2000** | **MPEG-2, AVC, HEVC** |

| Tipo de imagen | De qué depende |
|---|---|
| **Intra** | **De nada: se descodifica sola** |
| **Predicha** | **De la anterior** |
| **Bidireccional** | **De la anterior Y de la siguiente** ✔ |

- **DE DÓNDE SALE EL RETARDO** · `[of]` · **Para descodificar la bidireccional hay que tener ya la
  siguiente.** **Grupo largo: comprime mejor y retarda más.**
- **EL ENLACE CON LAS TRES CADENAS** · `[of]` · **La contribución paga caudal para no pagar retardo.**

## La asimetría de la compresión

- **PREGUNTA 71** · `[exam]` · **La carga computacional es muy superior al comprimir que al
  descomprimir.**
- **POR QUÉ** · `[of]` · **Comprimir exige BUSCAR** —particiones, modos de predicción, vectores de
  movimiento—; **descomprimir sólo exige EJECUTAR lo que el codificador ya decidió**, porque **las
  decisiones vienen escritas en el flujo.**
- **POR QUÉ ES DELIBERADO** · `[of]` · **Hay un codificador y millones de descodificadores.** **El
  trabajo caro se pone donde sólo hay una máquina.**
- **LAS FALSAS** · `[exam]` · **«Simétrica»**: no lo es en ningún códec de difusión. **«Depende del
  algoritmo»**: la asimetría es de diseño. **«Superior al descomprimir»**: al revés.
- **LO QUE SE DERIVA** · `[of]` · **Un equipo puede reproducir lo que no puede grabar en tiempo real.**
  **Por eso una tableta reproduce ultraalta definición y no la codifica.**

## Acceso condicional e interactivos

| Pieza | Qué hace |
|---|---|
| **Aleatorizador** | **Cifra el flujo con una palabra de control que cambia cada pocos segundos** |
| **Mensajes de derechos** | **Dicen a qué tiene derecho cada abonado** |
| **Tarjeta o módulo** | **Descifra la palabra de control si hay derecho** |

- **LA IDEA QUE LO HACE ROBUSTO** · `[of]` · **Romper una palabra de control sirve para unos segundos y
  para nada más.**

| Servicio | Qué es |
|---|---|
| **Guía electrónica de programación** | **La parrilla, transmitida en el propio flujo** |
| **Teletexto digital y aplicaciones** | **Contenido navegable sobre la emisión** |
| **Televisión híbrida** | **Emisión combinada con contenido de internet** |

- **LA OBSERVACIÓN** · `[of]` · **Lo interactivo de verdad llegó por la red y no por la difusión.** **La
  norma preveía un canal de retorno; el espectador ya tenía otro mejor en el mismo salón.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 40 | Compresión con menos retardo | **JPEG2000** ✔ |
| 60 | Cuál NO está soportado por la norma | **DVB-A** ✔ |
| 71 | Carga computacional de comprimir frente a descomprimir | **Muy superior al comprimir** ✔ |
| 79 | Estándar de compresión de vídeo | **MPEG-2** ✔ |
