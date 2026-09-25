# Puesto 28 · Operador/a de Sonido · Tema 11 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/11-lineas-y-conexiones.md`. Fecha de lectura de
todas las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Otros ficheros tocados: ninguno fuera del
tema y este informe.

## Método

- **Citas en inglés (152 negritas «…»)**: cotejo por script (espacios, comillas y guiones de fin de línea
  normalizados) contra los volcados de EBU Tech 3250, SMPTE 276M, 272M, ST 299-1, ST 299-2, ST 2110-10:2022,
  ST 2110-30:2025, Audinate DC 4.18, RME MADI Converter, RME ADI-648 y DiGiCo TN294. Todas aparecen. Los
  «fallos» del script eran sólo el carácter Ω (U+2126 en el volcado de la EBU, U+03A9 en el tema) y cortes de
  palabra con guion; revisados a mano uno por uno.
- **Crown y Rane**: no tenían volcado. Leídos hoy en la fuente primaria (páginas web del fabricante,
  https://www.crownaudio.com/en-US/faq_categories/1 y https://www.ranecommercial.com/legacy/note151.html):
  las tres citas son literales.
- **Contexto de cada cita** (apartado, salvedad, «shall/should»): releído en el volcado, con los nueve errores
  delante.
- **Estado de las normas SMPTE**: leído hoy en pub.smpte.org (276M, 272M y 299-2 «stabilized»; 299-1,
  2110-10 y 2110-30 «active»).
- **Copiado del común** (1 pasaje, ST 2110-30:2025 del tema 13 de Cámara Operador): literal, comprobado por
  script. No se re-verifica.
- **Copiado de RTVE sin cambios** (13 bloques del informe de redacción): comprobados por script, quitados `**`,
  ✔ y espacios; todos son subcadena de su tema RTVE. Sólo difieren en la mayúscula inicial «El MADI…» y «Una
  interfaz…» (en RTVE, minúscula tras «Por qué:»), y el redactor añadió «(oficio)» tras «segundo camino
  físico». No se re-verifican.
- **Adaptado de RTVE y oficio**: verificado (ver abajo).

## Correcciones aplicadas

| # | Error | Dónde | Qué decía | Qué dice ahora | Fuente |
|---|---|---|---|---|---|
| 1 | 8 / 9 | Resumen de formatos; tabla de normas del SDI; epígrafe «El audio embebido en SDI»; tabla de normas; Trazabilidad | La ST 299-2 amplía a 32 canales el SDI de **alta definición (SMPTE 292)** | La ST 299-2 es para **interfaces de 3 Gb/s** (nivel A); el HD a 1,5 Gb/s (SMPTE 292) se queda en 16. Se añaden la cita del título, la de «3 Gb/s Level A» y los 16 canales a 96 kHz | ST 299-2:2010, título, introducción y 1 |
| 2 | 4 | «Audio no PCM embebido» | «La norma pone dos límites que … tiene que respetar»; procesado PCM «debe desactivarse» | Son recomendaciones («should»), en parte en un anexo informativo; «la norma recomienda desactivarlo» | ST 299-1, nota de 4 y anexo A (informativo) |
| 3 | 6 | «El XLR en audio digital» | DI/DO «si no hay sitio en el panel» | Cuando falte sitio **y** el conector pueda confundirse con uno analógico | Tech 3250, 6.4 |
| 4 | 6 | MADI, tabla coaxial/fibra y resumen de formatos | 100 m por coaxial como dato general («unos 100 m») | Hasta 100 m en un equipo de RME, que lo atribuye a la ecualización y a sus entradas de alta sensibilidad | RME MADI Converter, cap. 1 |
| 5 | 3 | MADI, masa | Diferencia de masa «de un cuarto de voltio» | «De más de un cuarto de voltio» («over 0.25V») | DiGiCo TN294 |
| 6 | 9 | Siglas | FDDI desarrollada como *fiber distributed data interface*; ADAT «de la casa Alesis que la estrenó» | Sin desarrollo (RME no la da); ADAT «marca de la casa Alesis, que la especifica» | RME MADI Converter; RME ADI-648 («according to Alesis specification», marca de Alesis) |
| 7 | 5 | Siglas | MIDI, SDP, Cat5 y Cat6 presentadas y no usadas en el tema | Quitadas; se presenta Gb/s, que ahora se usa | — |
| 8 | 9 | «Por qué UDP…» | «(oficio; la ST 2110-10 fija sus límites de tamaño de paquete UDP)» | Se cita la ST 2110-10:2022, 6.2: «All RTP Streams shall be transported on UDP…»; la tabla TCP/UDP queda como oficio. ST 2110-10 añadida a la ficha, a «Normas técnicas» y a Trazabilidad | ST 2110-10:2022, 6.2 |
| 9 | 9 | BNC | «La IEC 169-8 describe el BNC de 50 Ω» | Según el título con que la cita la 276M, con la cita del título | 276M, 2 |
| 10 | 9 | «Qué puede ir por un XLR» | A-B «daña los dinámicos» | «Puede dañar un dinámico», como el tema 2 (verificado) | Tema 2 del puesto 28, 7.5 |
| 11 | 9 | Jack TRS | Patillaje «lo da Crown» | «Para las entradas de sus etapas de potencia»: la respuesta de Crown es sobre sus equipos | Crown FAQ |
| 12 | — | AES/EBU, «Qué es» | «fija la frecuencia de la radiodifusión» | «señala la frecuencia de trabajo» («it is intended … primarily used at 48 kHz») | Tech 3250, 1 |
| 13 | — | Dolby E | «que viaja en un par AES/EBU» | «audio con reducción de caudal que viaja en un par AES/EBU» (liga con «compressed (bit-rate reduced) audio» de la cita anterior) | Informe A § 14.4 (EBU Technical Review, RDD 19) |
| 14 | — | Tabla de normas y Trazabilidad | ST 299-2 sin estado; Crown y Rane «a través del informe» | «Aprobada el 21-7-2010; stabilized»; Crown y Rane con su URL, leídos directamente | pub.smpte.org; páginas del fabricante |

Añadida a «Se nombran sin haberlas leído» la SMPTE 425 (interfaz de 3 Gb/s). Extensión de la ficha: 11.000
palabras (10.978 según `indice.py`).

## Comprobado y correcto (sin cambios)

- EBU Tech 3250: 6.4 (XLR, IEC 60268-12, macho/hembra, pines, polaridad), 2.3 (bifase), 1 (alcance, 48 kHz,
  CCIR 646), 2.2 (modos y estéreo A/B), 2.2.1 (32 intervalos, 24 y 20 bits, auxiliares 4-7, V/U/C/P), 2.2.2
  (trama, tasa = muestreo, Z cada 192), 2.1.11 (bloque), 4 (contenido del estado del canal, «92-bit», 24
  bytes), apéndice 1 («192 bits»), 6.1-6.3 (V.11, 110 Ω, ±20 %, 2-7 Vpp, 200 mV, 7 V de modo común, 0,025
  UI «less then», un receptor por línea, ecualización y 100 m), apéndice 2 (Cat5, 400/800 m, pines 4-5 y
  3-6, XLR 2→RJ45 5 y 3→4).
- SMPTE 276M: alcance, 4.1.1, 4.2, 5.3, 6, 7, 8, anexo A (1 V, 110/75 Ω, AES 3ID); aprobada el 1-12-1995.
- SMPTE 272M: 1.1-1.4 (259M/344M, 20 y 24 bits, 2 a 16 canales, 4 en compuesto, grupos, 48 kHz síncrono,
  32-48 kHz opcional), numeración de grupos.
- ST 299-1: 1.1-1.4, nota de 4 (SRC y SMPTE 337; «multiplexing (embedding) and demultiplexing
  (receiving)»), anexo A; aprobada el 29-5-2009, renumerada el 21-7-2010; antes 299M.
- ST 2110-30:2025: 6.1 (48 kHz «shall», 44,1/96 «should»), 6.2.1 (AES67), AES67-2023, cláusula 7 (nivel A),
  tabla 2 (seis niveles, frecuencias, tiempos y canales cotejados celda a celda), SGRP, nota SDI; aprobada el
  1-10-2025, revisa la de 2017.
- Audinate DC 4.18 (publicada el 6-5-2026): suscripción, nombres, flujos (4 canales «typically» en unicast),
  formatos, tres mensajes de error, latencia (1 ms, 150 µs, 1 ms en 100 Mbps, la mayor de las dos), PTP y
  elección del *leader*, PTPv1/v2, redundancia y misma velocidad, EEE y enlaces saturados (factores que
  desestabilizan el reloj seguidor), DSCP, AES67/ST 2110-30.
- RME MADI Converter (7.1 «MADI Basics» y especificaciones), RME ADI-648 y DiGiCo TN294 (rev. 3, 27-2-2013):
  todas las cifras y citas del epígrafe MADI y ADAT; la discrepancia 2001 frente a 2003/2008 está bien
  declarada.
- Cálculos: 56 = 28 × 2; 4 + 4 + 2; 48.000 × 24 = 1,152 Mbps; ×32 = 36,9; ×2 = 73,7; 64 × 48.000 = 3,072 M;
  24 × 8 = 192; 16 canales = 8 pares.
- Adaptado de RTVE: pin 2 vivo (Rane, Crown), seminormalizado, vocabulario, *splitter* pasivo, fila «Sobre
  red», definición de Dante (oficio declarado), conmutador (oficio), UDP (ahora con norma), tres flujos,
  caudal en crudo, MADI sin soluciones de red, tabla del embebedor, instalación mixta: sin datos que
  contradigan una fuente; lo que no tiene fuente está marcado como oficio.

## Lentes

- `refutar_prosa.py`: 0 hallazgos tras las correcciones.
- `indice.py`: índice regenerado, 55 epígrafes.
- El tema no cita normas legales: `negritas.py`, `refutar_exactitud.py` y `refutar_modo.py` no tocan (el cotejo
  de negritas contra las normas técnicas se ha hecho por script, arriba).

## Para refutación

- Crown y Rane siguen sin volcado local (leídos en la web); si la refutación no tiene red, que se fíe de este
  informe.
- «Level A» sale en dos sentidos distintos en el tema: el nivel A de conformidad de la ST 2110-30 y el
  «3 Gb/s Level A» de la ST 299-2 (cita literal). No se confunden en el texto, pero pueden confundir en un test.
