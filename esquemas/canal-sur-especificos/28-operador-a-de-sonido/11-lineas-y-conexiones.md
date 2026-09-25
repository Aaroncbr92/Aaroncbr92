# Tema 11 del específico de Operador/a de Sonido · Líneas y conexiones

**Siglas**: RTVA; CSRTV; XLR; TRS; TS; BNC; AES; UER/EBU; SMPTE; AES3 (AES/EBU); MADI (AES10); ADAT; TOSLINK; SDI; HANC; Dante; AES67; IP; UDP; TCP; RTP; PTP (IEEE 1588); IEEE; PCM; SRC; S/MUX; RJ45; UI; Mbit/s; mVpp; µm; nm; DC; EMI; DI/DO; DS; FDDI; SC; ST; SGRP; FAQ; dBu; dBFS; N-1.

Esqueleto para repasar, no resumen: recorta prosa, nunca un dato.

<!-- indice -->
<!-- /indice -->

## Líneas y conexiones
- (oficio) tres familias: analógica (XLR/jack), digital dedicada (AES/EBU, MADI, ADAT, SDI), red (Dante/AES67).
- (EBU Tech 3250) AES/EBU sobre XLR: 110 Ω, par balanceado.
- (SMPTE 276M) AES/EBU coaxial, MADI coaxial y SDI: 75 Ω, BNC.
- (oficio) panel: normalizado corta los dos lados; seminormalizado corta sólo en la fila inferior, copia en la superior sin cortar; no normalizado sin conexión interna.
- (oficio) splitter pasivo: sólo una mesa debe dar phantom; la carga baja la impedancia que ve el micro; usar transformadores de aislamiento.
- (oficio) matriz: entrada/salida/nivel/panel/salvado; clases analógica, digital, sobre IP (ésta suscribe, no conmuta).

## XLR
- (EBU Tech 3250, 6.4) conector circular de 3 pines con bloqueo, IEC 60268-12.
- (Rane, RaneNote 151) convenio AES «pin 2 is hot»: pin 1 masa, pin 2 vivo, pin 3 retorno.
- (EBU Tech 3250, 6.4) en digital pin 1 malla, pines 2 y 3 señal; polaridad 2/3 indiferente por el código bifase.
- (EBU Tech 3250, 6.4) salida: pines macho/carcasa hembra en el equipo; entrada: pines hembra/carcasa macho; rotular DI/DO.
- (oficio) por un XLR: micro, línea analógica, AES/EBU, o alimentación A-B de 12 V (temas 2 y 3).

## Jack
- (Crown, FAQ) TRS: punta hot, anillo low, cuerpo ground; TS sin retorno, desbalanceado.
- (Rane, RaneNote 102) línea balanceada: punta +, anillo −, cuerpo masa; auriculares: punta izq., anillo dcha., cuerpo común.
- (Soundcraft, Guide to Mixing) punto de inserción: punta envío, anillo retorno, cable en Y.
- (Shure, Wireless Microphone Systems) jack 1/8" TRS en videocámaras y en monitores IEM, señal desbalanceada.

## BNC
- (SMPTE 276M, cl. 8) mecánica IEC 169-8, admite 75 Ω.
- (SMPTE 276M) AES/EBU coaxial: no balanceado, 75 Ω, 1 V ± 10 % pp, frente a 110 Ω/2-7 Vpp de la versión XLR.
- (RME) MADI coaxial: BNC, 75 Ω, AES10-1991.
- (oficio) SDI: coaxial 75 Ω con BNC; capa física no leída.

## Dante/AES67
- (Audinate) Dante: red propietaria de Audinate sobre Ethernet; encaminamiento por suscripción Rx-Tx; canales identificados por nombre, no por número.
- (Audinate) unicast: punto a punto, típicamente 4 canales de audio por flujo, por defecto; multicast: uno a muchos, consume ancho de banda aunque no haya receptores.
- (Audinate) suscripción sólo entre canales del mismo formato; error típico si emisor y receptor tienen distinta frecuencia de muestreo.
- (Audinate) latencia por defecto 1 ms; mínimo 150 µs en redes sólo gigabit; si difieren, se usa la mayor de las dos.
- (Audinate) reloj PTP (IEEE 1588); PTPv1 por defecto, PTPv2 con RTP; AES67 y ST 2110-30 exigen PTPv2.
- (Audinate) redundancia: dos redes físicamente separadas, mismo tipo de equipos que no la soportan sólo a la red primaria.
- (SMPTE ST 2110-10:2022, 6.2) los flujos RTP van sobre UDP.
- (cálculo) 48 kHz × 24 bits = 1,152 Mbps/canal; 32 canales = 36,9 Mbps; bidireccional ×2 = 73,7 Mbps.
- (Audinate; SMPTE ST 2110-30:2025) AES67 es norma abierta; ST 2110-30 se apoya en ella, sólo PCM.
- (ST 2110-30, 6.1) 48 kHz obligatoria; 44,1 y 96 kHz recomendadas.
- (ST 2110-30, tabla 2) niveles A/AX/B/BX/C/CX por frecuencia, tiempo de paquete y canales; nivel A obligatorio como mínimo.

## MADI
- (RME) MADI = AES10; 28 señales AES/EBU en serie = 56 canales; tope 100 Mbit/s.
- (RME) modo de 64 canales: hasta 48 kHz + 1 %, o 32 canales a 96 kHz; tasa efectiva 125 Mbit/s.
- (RME; DiGiCo) coaxial BNC 75 Ω hasta 100 m; fibra multimodo SC hasta ~2 km, luz de 1.300 nm.
- (DiGiCo, TN294) diferencia de masa mayor de 0,25 V corta el enlace coaxial.
- (RME; DiGiCo) incompatibilidad entre equipos: 56 frente a 64 canales; S-MUX (48K) frente a Hi-Speed (96K), no compatibles entre sí.
- (DiGiCo) protección: puertos redundantes (1A/1B); el MADI no usa PTP ni topología conmutada.

## AES/EBU
- (EBU Tech 3250) dos canales, hasta unos cientos de metros; 48 kHz recomendada en radiodifusión.
- (EBU Tech 3250) subtrama de 32 intervalos; trama = 2 subtramas; bloque = 192 tramas.
- (EBU Tech 3250) intervalos 0-3 preámbulo; 4-27 muestra (24 bits); 28 validez; 29 usuario; 30 estado de canal; 31 paridad.
- (EBU Tech 3250) mensaje de estado de canal: 192 bits, 24 bytes.
- (EBU Tech 3250, cap. 6) eléctricas: base V.11, 110 Ω, 2-7 Vpp, Vmin 200 mV, jitter propio <0,025 UI.
- (EBU Tech 3250) un solo receptor por línea; ecualización sólo permitida en el receptor.
- (EBU Tech 3250, apéndice 2) por cat. 5 UTP: hasta 400 m sin ecualizar u 800 m ecualizado; pines RJ45 4 y 5 para el par principal.

## ADAT
- (RME) óptico TOSLINK, especificación de Alesis; 8 canales a 48 kHz, 4 a 96 kHz (S/MUX), 2 a 192 kHz (S/MUX4); cable hasta ~10 m.
- (RME) el S/MUX no lleva codificación que lo identifique: hay que fijar el modo a mano en los dos extremos.

## SDI
- (SMPTE 272M-2004) SD: 2 a 16 canales (4 como máximo en compuesto), 20 bits por defecto, 24 opcional.
- (SMPTE ST 299-1:2009) HD: hasta 16 canales a 32/44,1/48 kHz, hasta 8 a 96 kHz, 24 bits.
- (SMPTE ST 299-2:2010) interfaz de 3 Gb/s: canales 17 a 32 adicionales, hasta 32 canales en total.
- (SMPTE 272M) grupos de 4 canales: grupo 1 = canales 1-4, grupo 2 = 5-8, etc.; cada par AES/EBU son 2 canales.
- (SMPTE ST 299-1, 1.4) datos de audio en el HANC del Cb/Cr; control en el HANC del Y.
- (SMPTE 272M; ST 299-1) reloj preferido: 48/96 kHz síncrono con el vídeo.
- (SMPTE ST 299-1, anexo A) datos SMPTE 337 (no PCM, p. ej. Dolby E): prohibida la conversión de frecuencia y cualquier procesado PCM.

## Embebido y desembebido
- (SMPTE ST 299-1) embeber = multiplexar audio en el vídeo; desembeber = demultiplexarlo.
- (oficio) no es matriz ni multiplexor de transporte: mueve audio dentro de la señal, no entre sitios.
- (oficio) puntos: cámaras y exteriores llegan con audio ya embebido; a la entrada del control se desembebe; a la salida se embebe; en el central se reordena.
- (oficio) conversión AES3 ↔ SDI: el reloj va atado a la referencia de vídeo del centro.
- (oficio) supuesto: 16 canales HD-SDI, desembeber en 4 grupos/8 pares AES/EBU, comprobar reparto de pistas y reloj con el emisor, Dolby E sin convertir ni procesar, medir sonoridad antes de dar paso (tema 13).

## Trazabilidad
- fuentes leídas el 25/09/2026: EBU Tech 3250, 3.ª ed. 2004; SMPTE 276M-1995; SMPTE 272M-2004; ST 299-1:2009; ST 299-2:2010; ST 2110-10:2022; ST 2110-30:2025; Audinate, Dante Controller User Guide 4.18 (6-5-2026); RME, MADI Converter y ADI-648; DiGiCo, TN294 rev. 3; Crown, FAQ; Rane, RaneNote 151 y 102; Soundcraft, Guide to Mixing; Shure, Wireless Microphone Systems.
- no leídas, de pago o no descargadas: AES3, AES10, AES67, AES3-id, IEC 60268-12, IEC 169-8, SMPTE 259M y 292, SMPTE 425, norma de cableado estructurado.
