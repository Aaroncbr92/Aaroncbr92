# Esquema · Tema 9 del específico de Técnica de Equipos y Sistemas Electrónicos · La señal audiovisual sobre redes

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de redes de vídeo · `[norma]` =
índice público de una norma de organismo técnico. **Siglas**: el protocolo de internet (**IP**) y el de
datagramas de usuario (**UDP**); las familias de la Sociedad de Ingenieros de Cine y Televisión
(**SMPTE ST 2110** y **SMPTE ST 2022**); la norma de audio en red de la Sociedad de Ingeniería de Audio
(**AES67**); la modulación por impulsos codificados (**PCM**); el transporte seguro y fiable (**SRT**);
la petición automática de repetición (**ARQ**); la corrección de errores hacia delante (**FEC**); las
interfaces del tema 8 (**SDI** y **MADI**); el protocolo de tiempo de precisión (**PTP**); y los bits
por segundo (**bps**).

**Cabecera.** Enunciado: punto 11 del anexo · **7 preguntas** · **ninguna lleva figura** · **es el
punto donde esta ocupación se encuentra con el futuro de las instalaciones.**

<!-- indice -->

## Índice

- [La familia SMPTE ST 2110](#la-familia-smpte-st-2110)
- [La redundancia: SMPTE ST 2022-7](#la-redundancia-smpte-st-2022-7)
- [Los conceptos de red](#los-conceptos-de-red)
- [La corrección de errores y el transporte seguro](#la-corrección-de-errores-y-el-transporte-seguro)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La familia SMPTE ST 2110

- **LA IDEA**: **descompone la señal audiovisual en flujos separados** —vídeo por un lado, audio por
  otro, datos por otro— **y los vuelve a juntar con un reloj común.**
- **LA DIFERENCIA CON EL SDI**: **en SDI todo va incrustado en la misma trama; en 2110 cada esencia va
  por su camino.**
- **PREGUNTA 41** · `[norma]` · **El estándar que regula la transmisión basada en AES67 es el SMPTE
  2110-30.**
- **VERIFICADO EN EL ÍNDICE PÚBLICO DE LA SMPTE**: **el título oficial de esa parte es «PCM Digital
  Audio»**, y **es la única de las cuatro opciones que trata de audio.** **La respuesta NO descansa en
  la plantilla.**

## La redundancia: SMPTE ST 2022-7

- **PREGUNTA 38** · `[of]` · **El objetivo de la 2022-7 es proporcionar conmutación sin interrupciones
  entre rutas redundantes.**
- **CÓMO FUNCIONA**: **el emisor manda *dos copias idénticas* del mismo flujo por *dos caminos
  distintos*, y el receptor toma de cada uno los paquetes que le llegan bien.** **Si un camino se cae,
  no hay que conmutar nada.**
- **EL CONTRASTE CON EL TEMA 8, QUE ORDENA LAS DOS MANERAS DE PROTEGERSE:**

| Tecnología | Cómo se protege |
|---|---|
| **MADI y SDI** | **Duplicando el *cable***: dos caminos físicos y un conmutador |
| **ST 2110 sobre IP** | **Duplicando el *flujo***: la 2022-7, sin conmutador y sin corte |

## Los conceptos de red

- **PREGUNTA 19** · `[of]` · **La latencia en directo es el retraso entre la captura y la
  visualización.**
- **PREGUNTA 30** · `[of]` · **El bit rate describe los bits transmitidos por unidad de tiempo.**
- **PREGUNTA 75** · `[of]` · **El rango de direcciones del envío a varios destinos es 224.0.0.0/4.**
- **CÓMO SE RECUERDA EL RANGO**: **es el bloque que empieza en 224 y llega hasta 239**, y **`/4`
  significa que sólo los cuatro primeros bits están fijados.**

## La corrección de errores y el transporte seguro

- **PREGUNTA 90** · `[of]` · **El FEC es la corrección de errores hacia delante: añade bits para
  corregir sin retransmitir.**
- **LA PALABRA QUE LO DEFINE ES «HACIA DELANTE»**: **el receptor corrige *sin pedir nada*.**
- **LAS DOS MANERAS DE SOBREVIVIR A LA PÉRDIDA DE PAQUETES:**

| Mecanismo | Cómo recupera | Coste |
|---|---|---|
| **FEC** | **Con redundancia enviada por adelantado** | **Más ancho de banda, latencia *fija*** |
| **ARQ** | **Pidiendo la retransmisión** | **Menos ancho de banda, latencia *variable*** |

- **PREGUNTA 14** · `[of]` · **La característica que NO es del SRT es que sea de alta latencia.**
- **POR QUÉ**: **el SRT existe precisamente para dar baja latencia sobre internet.** **Decir que es de
  alta latencia es negar su razón de ser.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 14 | Cuál NO es característica del protocolo SRT | a) Que sea de alta latencia ✔ |
| 19 | Qué significa latencia en directo | b) El retraso entre captura y visualización ✔ |
| 30 | Qué describe el término bit rate | b) Bits transmitidos por unidad de tiempo ✔ |
| 38 | Objetivo del estándar SMPTE 2022-7 | c) Conmutación sin interrupciones entre rutas redundantes ✔ |
| 41 | Qué estándar regula la transmisión basada en AES67 | b) SMPTE 2110-30 ✔ **·** verificado en la SMPTE |
| 75 | Rango de direcciones del multicast | d) 224.0.0.0/4 ✔ |
| 90 | Qué es el FEC | b) Corrección de errores hacia delante ✔ |

**Las siete oficiales son correctas** y **ninguna descansa sólo en la plantilla.** · **Aviso de
estudio**: **el cuadro que enfrenta FEC y ARQ y el que enfrenta duplicar cable con duplicar flujo son
las dos ideas del punto.** **Con ellas se contestan tres preguntas y se entiende el resto.**
