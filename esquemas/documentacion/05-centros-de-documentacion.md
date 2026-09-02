# Esquema · Tema 5 del específico de Documentación · Centros de documentación audiovisual

Telegrama. **Cada línea lleva delante de dónde sale**: `[377-1]` = SMPTE ST 377-1:2019 · `[3285]` =
EBU Tech 3285 v2.0 · `[319]` = norma ECMA-319 · `[IASA]` = IASA-TC 03, 4.ª ed. · `[LoC]` = Biblioteca
del Congreso de los Estados Unidos · `[Dalet]` = página del fabricante · `[RTVE]` = artículo de la
responsable del Fondo Documental · `[CE]` = portal audiovisual de la Comisión Europea.

**Cabecera.** **10 preguntas** · **las 10 verificadas en documento**. **Es el único tema del bloque
sin ninguna respuesta apoyada sólo en la plantilla.** A cambio, **ninguna fuente está en el BOE**.

<!-- indice -->

## Índice

- [Lo que hay que llevar sabido](#lo-que-hay-que-llevar-sabido)
- [Soportes](#soportes)
- [Formatos](#formatos)
- [Preservación](#preservación)
- [Sistemas y archivo](#sistemas-y-archivo)
- [El servicio audiovisual de la Unión](#el-servicio-audiovisual-de-la-unión)

<!-- /indice -->

## Lo que hay que llevar sabido

| Pregunta | Respuesta | De dónde |
|---|---|---|
| MXF | **Contenedor de vídeo y audio con metadatos** | `[377-1]` |
| AAC | **Audio, con pérdidas** | `[LoC]` + `[IASA]` |
| Sticky Shed Syndrome | **Cinta magnética** | `[LoC]` |
| LTO | **Cinta magnética** | `[319]` |
| Metadatos dentro del fichero de audio | **BWF** | `[3285]` |
| Principal desafío de los archivos | **Obsolescencia de formatos, físicos y digitales** | `[IASA]` §4 |
| Criterio de la mejor copia | **Calidad de señal y estado físico** | `[IASA]` §6 |
| Dalet Galaxy | **Televisión, radio, digital y social** | `[Dalet]` |
| Modelo de datos único del Archivo RTVE | **2011** | `[RTVE]` |
| Servicio audiovisual de la Unión Europea | **EBS** | `[CE]` |

## Soportes

- `[LoC]` · **STICKY SHED = CINTA MAGNÉTICA.** «**Describes the problems, the likely causes, and a
  proposed solution to the sticky-shed problem with magnetic tape**».
- `[LoC]` · **La causa**: «**the deterioration of the polyurethane binder used to hold the magnetic
  material onto the tape base, probably caused by hydrolysis**». Y el efecto: las cintas «**are very
  difficult to run and may, in serious cases, jam in the recorder**».
- **POR QUÉ SÓLO LA CINTA**: es la única con **capa magnética pegada** con **aglutinante**. **Cera,
  pizarra y papel perforado no tienen pegamento**, luego no hay nada que se descomponga. Y **al
  despegarse el aglutinante se lleva el óxido**, o sea **la grabación**.
- `[319]` · **LTO = CINTA MAGNÉTICA**, y está en el título de la norma: «**Data Interchange on 12,7 mm
  384-Track Magnetic Tape Cartridges – Ultrium-1 Format**».
- **AVISO**: la norma **usa** las siglas —«**LTO Cartridge Memory (LTO CM)**»— pero **no las
  desarrolla**. El desarrollo del enunciado es del enunciado.
- `[IASA]` · **Por qué la cinta no es lo viejo**: se recomienda «**discrete data carriers such as data
  tapes or HDDs for offline storage**». **Se guarda sin corriente y cuesta poco por dato.**
- **LAS DOS CINTAS NO SON LA MISMA**: la **analógica de audio con aglutinante** es el problema; el
  **cartucho de datos** es la solución.

## Formatos

- `[377-1]` · **MXF = ESTRUCTURA DE DATOS, NO CÓDEC**: «**This document defines the data structure of
  the Material Exchange Format (MXF) for the interchange of audio-visual material**».
- `[377-1]` · **La estructura**: «**An MXF file starts with a File Header, is followed by a File Body
  and is completed by a File Footer**»; «**The File Body can contain one or more Essence
  Containers**».
- **VOCABULARIO**: **esencia = el material** (imagen, sonido, datos) · **metadatos = lo que se dice de
  él**, y son de dos clases, **estructurales** y **descriptivos**.
- `[377-1]` · **Y no define ni la esencia ni los metadatos descriptivos**: «**The document does not
  define either the Essence Container or the Descriptive Metadata**» → **por eso es contenedor y no
  códec**.
- `[3285]` · **BWF = WAVE + METADATOS**: «**As well as the audio data, a BWF file contains the minimum
  information – or metadata – which is considered necessary for all broadcast applications**»;
  «**The Broadcast Wave Format is based on the Microsoft WAVE audio file format, to which the EBU has
  added a "Broadcast Audio Extension" chunk**».
- **Falsos**: **WAVE** = **la base sin el bloque añadido**; es el fino · **PCM** = **no es formato de
  fichero**, es la codificación —«**the Broadcast Wave Format for PCM audio data**»— · **AAC** = audio
  **con pérdidas**.
- **Gratis**: v2 (**mayo de 2011**) añade **metadatos de sonoridad**; v1 usaba **64 de los 254 bytes
  reservados**; las tres versiones son **compatibles**.
- `[LoC]` · **AAC ES AUDIO**, y está en la designación: «**ISO/IEC 14496-3:2001** […] **Part 3:
  Audio**». Y es **perceptual**: «**Perceptual audio encoding format**».
- `[IASA]` · **PERCEPTUAL = CON PÉRDIDAS**: «**Such so-called "lossy codecs" based on perceptual coding
  result in the irretrievable loss of parts of the primary information**».
- `[IASA]` · **Regla de archivo**: no usar reducción de datos; **la compresión sin pérdidas sí**, pero
  con reservas: «**there is no objection in principle to the use of lossless (fully reversible)
  compression**».

## Preservación

- `[IASA]` §4 · **EL DESAFÍO**: «**No format, whether carrier-based or file-based, will be playable
  forever, and for some the end is in sight**». **«Carrier-based or file-based» = «físicos y
  digitales».**
- `[IASA]` §4 · **La consecuencia**: «**the window of opportunity for digitally preserving
  carrier-based content is finite**», porque «**the maintenance of obsolete replay systems will become
  unaffordable**».
- **Falsos, y son verdad los tres**: **personal cualificado** y **coste** son **efectos** de la
  obsolescencia, no la causa · la **falta de estándares** es **falsa**: la propia recomendación que
  cita la pregunta **es** el estándar.
- `[IASA]` §6 · **LA MEJOR COPIA**: «**While the archival master** […] **may often be in better
  physical condition, it may be of inferior signal quality** […] **Consequently, the signal quality of
  the various available copies must be compared**».
- **Las dos cosas a la vez: SEÑAL + ESTADO FÍSICO**, y **suelen ir en direcciones contrarias**.
- **Falsos**: «más antiguas mejores» → **no**; «formato original siempre» → **no**, hay que
  **comparar**; «cuantas más copias» → confunde **cantidad con criterio**. Lo que sí dice es que puede
  convenir «**extend the search for the best copies to other collections on a national or even
  international scale**».
- `[IASA]` §6 · **Dos avisos**: limpiar y restaurar «**can significantly improve signal retrieval**»,
  pero **hay que sopesar el riesgo**; y «**It is good practice to minimise the handling of carriers at
  all times**».

## Sistemas y archivo

- **MAM / PAM / DAM**: **de medios** = cataloga y sirve **lo ya hecho** · **de producción** = acompaña
  **lo que se está haciendo** · **digitales** = **cualquier fichero**, no sólo audiovisual. **La
  diferencia es el momento.**
- `[Dalet]` · «**Dalet Galaxy five is a fully integrated, collaborative news system that meets the
  challenge of media convergence. Manage end-to-end television, radio, digital and social news
  production within a single system with unified planning**».
- **Falsos**: editor doméstico y aplicación móvil **no son sistemas de gestión** · la que lo limita a **la producción de noticias de radio en una sola cadena** = **el fino**: acierta la familia y **falla el alcance**.
- `[RTVE]` · **2010 ≠ 2011.** «**2010 es el año de la sustitución de SIRTEX por** […] **un nuevo gestor
  documental, ARCA** […] **y, 2011, supone la integración del sistema de gestión de cintas (GMS) en
  ARCA y el punto y final de la migración de las cerca de 40 bases de datos documentales que, con
  estructuras distintas y criterios de selección, análisis e indización dispares habían coexistido
  hasta el momento**».
- **2010 = GESTOR NUEVO · 2011 = MODELO DE DATOS ÚNICO.** La cifra que lo explica: **cerca de 40 bases
  de datos** con criterios **dispares**.

## El servicio audiovisual de la Unión

- `[CE]` · «**The European Broadcasting Service (EBS), the European Union's TV information service,
  together with the AV Portal, provides EU-related audiovisual material free of charge to media
  professionals**».
- **LA TRAMPA**: **UER y EBU son la misma organización en dos idiomas** → **ninguna puede ser la
  respuesta**, porque serían dos correctas. **TUE** es un tratado.
- **Y el fondo**: la unión de radiodifusión **no es un organismo de la Unión Europea**; es una
  asociación de radiodifusores con miembros de fuera. **El servicio de la Unión es el de la
  Comisión.**
