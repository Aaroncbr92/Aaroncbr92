# Tema 7 del específico de Operador/a de Sonido · Sonido en radio

**Siglas**: RTVA, CSRTV, UER/EBU, AES, UIT/ITU, IETF/RFC, RDSI/ISDN, ACIP, N-1 (mix-minus), PFL, DIM, IFB, RTP/RTCP, UDP/TCP, FEC, SIP/SDP/SAP, DiffServ/QoS/DSCP, PCM, MPEG (AAC-LC/LD/HE), DSL, FTTH, LUFS/LKFS, LU, dBTP, RIAA, HLS, OTT.

Esqueleto para repasar, no resumen: cada línea manda a su epígrafe del tema; ninguna sustituye leerlo.

<!-- indice -->
<!-- /indice -->

## Sonido en radio

- Oficio: sin imagen, todo va en el sonido (más ambiente, ráfagas, ident. verbal); cadena pensada para voz (micro cerca, compresión, EQ de presencia); escucha mala (coche, móvil) → dinámica muy comprimida; directo es la norma, no la excepción.
- Oficio: locutorio (locutores) / control (técnico, mesa, híbridos, códecs); cristal entre ambos; señas no normalizadas; autocontrol frecuente.
- Oficio: contribución (hacia la emisora, máxima calidad) / distribución (entre centros) / emisión (hacia el público). Regla: comprimir lo menos posible en contribución.

## Microfonía

- Tipos, patrones, sensibilidad, proximidad → tema 3; aquí sólo lo propio de radio.
- Oficio: locutorio con varios micrófonos abiertos a poca distancia.
- DPA: filtro en peine = suma de la señal consigo misma con retardo < 25 ms, si niveles a <10 dB.
- DPA: dos causas — reflexiones, o más de un micro abierto captando la misma señal.
- DPA: remedio, atenuar el retrasado ≥10 dB; regla 3:1 (20·log(1/3)≈-10 dB); en línea, 4,5:1 en teoría, factor 3 con direccionales; tratar reflexiones o usar micro de frontera.
- Oficio: en tertulia, abrir sólo quien habla o bajar el resto; sentar lejos del vecino.

## Mesa

- Estructura, entradas/salidas, auxiliares, PFL, DIM → tema 4; aquí, fuentes propias de radio.
- Oficio: servidor/automatización (línea, arranque por orden) — fuente principal.
- Oficio: reproductores físicos; giradiscos con previo RIAA de nivel bajo.
- Oficio: ordenador de redacción/invitado — caja de inyección o línea desbalanceada, más ruido de masa.
- Oficio: teléfono/híbrido y códec de contribución — cada uno con su N-1 propio.
- Oficio: N-1 = a cada línea exterior se le manda todo menos su propia señal.
- Oficio: motivo, el retardo del enlace; bajar volumen no sirve, hay que quitar la señal propia. No son N-1 — restar el primer canal cualquiera; mandar retorno de programa completo; «evitar retardo entre codificadores».
- Oficio: retorno de programa (ST, todo, si el oyente NO está en antena) vs N-1 (si SÍ está).
- Yamaha CL: Mix Minus quita un canal concreto de los buses MIX/MATRIX para monitor de intérprete; envíos previos al fader, independientes de su posición — para monitores y N-1.
- Oficio: caso dos líneas (principal + reserva) — cada retorno N-1 excluye la propia Y la otra línea, si no la voz vuelve por la que no se restó.
- Yamaha: Talkback envía el mic del jack TALKBACK al bus deseado, para instrucciones del técnico; su DIM baja la escucha salvo la propia señal de órdenes.
- Oficio: órdenes metidas en el bus del N-1 se oyen fuera sin salir al aire. Intercom/IFB → tema 8.

## Híbridos

- Clear-Com: híbrido convierte dos hilos (línea telefónica, ida+vuelta juntas) en cuatro hilos (envío/recepción separados); también como interfaz de intercom a red telefónica.
- Clear-Com: analógicos con transformador/op-amp; digitales con DSP, los más comunes.
- Clear-Com: pérdida transhíbrida = aislamiento envío/recepción en el lado de 4 hilos; más pérdida es mejor; se logra imitando la impedancia de línea en red equilibrada (difícil por sus variaciones).
- Clear-Com: cancelación = copia de polaridad inversa del envío sumada a la recepción, misma amplitud.
- Clear-Com: nulo = ajuste para más pérdida transhíbrida; híbridos digitales, autonulo.
- Oficio: híbrido es el N-1 de una sola línea; aislamiento imperfecto = eco.
- Clear-Com: mucha ganancia envío-recepción + acoplo acústico/eléctrico → oscilación (pitido).
- Oficio, caso oyente con eco: 1) comprobar que el bus del híbrido es N-1; 2) si lo es, rehacer nulo o bajar nivel de envío; 3) si pita, bajar ganancia.

## RDSI/IP

- UIT-T I.412: interfaz básica 2B+D; canal D de 16 kbit/s (señalización); canal B de 64 kbit/s, usable independiente; norma de 11/1988, en vigor.
- Oficio: RDSI 20 años como enlace de contribución — llamada con ancho garantizado, retardo bajo y constante, funciona con línea telefónica.
- EBU Tech 3326 §1.1: se pasa a IP por banda ancha y por retirada de RDSI en varios países. Oficio: IP más barato y flexible pero red compartida no garantiza nada — retardo, pérdida, desorden.
- EBU Tech 3326: ~15-20 fabricantes con equipos ISDN/IP, hace falta interoperabilidad → nace ACIP.
- EBU Tech 3326 (Rev.4, 11/2014): mínimo de interoperabilidad para contribución de audio sobre IP; buenas prácticas, en Tech 3329 (no leída).
- EBU Tech 3326: MUST/SHALL = obligatorio; SHOULD/RECOMMENDED = recomendado; MAY/OPTIONAL = opcional.
- EBU Tech 3326 §1.2: unidireccional sin retorno (satélite); bidireccional banda estrecha de paso (fútbol, retardo no importa); bidireccional banda ancha (entrevista, retardo importa).
- EBU Tech 3326 §1.3: equipo general vs portátil (voz mono a baja tasa, requisitos menos exigentes). §1.4: cuatro áreas — transporte IP, códecs, encapsulado, señalización.
- EBU Tech 3326 §2: IPv4 obligatorio; IPv6 recomendado; multidifusión recomendada; RTP sobre UDP obligatorio; RTCP recomendado; puertos 5004/5005 recomendados; TCP opcional.
- EBU Tech 3326 §2.2.6-7: FEC (RFC5109, puerto 5006) recomendada si hace falta, RFC2733 opcional; retransmisión RFC4588 opcional.
- EBU Tech 3326 §4: SDP obligatorio; SAPv1 recomendado en multidifusión unidireccional; SIP obligatorio en bidireccional (INVITE/ACK/BYE/OPTIONS/REGISTER), puerto 5060; negociación RFC3264; reconfiguración de códec recomendada, con nuevo INVITE+ACK.
- EBU Tech 3368 (v1.0, 11/2014) §1: perfil = parámetros preconfigurados para no fijarlos a mano en la calle.
- EBU Tech 3368 §2: perfil = parámetros de transmisión/recepción/decodificación; almacenables en el equipo; atributo SDP a=ebuacip (v0): jb, jbdef, plength, qosrec, protp.
- EBU Tech 3368 §2.1: perfil asimétrico (ej. DSL con poca subida) con a=sendonly/recvonly.
- EBU Tech 3368 §3.4.4.1: sin acuerdo de opciones, respuesta SIP 488 Not Acceptable Here.
- EBU Tech 3368 §3.4: búfer pequeño = pérdida de paquetes; búfer grande = retardo alto, problemático en bidireccional.
- EBU Tech 3368 §3.4.1-2: adaptativo (min/máx) o estático. §3.4.3: caso hotel — búfer fijo de 6 ms desde red corporativa falla en wifi pública.
- EBU Tech 3368 §3.6: DiffServ (RFC2474) obligatorio; salvedad, sólo sirve si la red del destinatario no ignora/borra el DSCP. §3.7.2: protecciones — duplicación de flujo, FEC, multiplexado protegido.
- Oficio: bidireccional decide el enlace — DAB es difusión, sin retorno; fibra/3G-4G-5G/satélite BGAN-Thuraya-Ka, sí bidireccionales.

## Códecs

- EBU Tech 3326 §3.3.5: todo códec necesita formato RTP registrado en IETF.
- EBU Tech 3326 §3.1 obligatorios: G.711 (64 kbit/s, PCMA/PCMU, 20 ms por defecto); G.722 (64 kbit/s); MPEG-1/2 capa II (reloj RTP 90 kHz); PCM lineal L16 (32/48 kHz, 4 ms; opcional en portátiles); PCM 12/20/24 bits (12 bits opcional).
- EBU Tech 3326: G.722 muestrea a 16 kHz pero su reloj RTP se fija a 8 kHz por error histórico de RFC1890.
- EBU Tech 3326: tabla MPEG capa II, 32-384 kbit/s; negrita = obligatorio; †=192/256/384 kbit/s opcional en portátiles.
- EBU Tech 3326 §3.2 recomendados: AAC-LC, AAC-LD (RFC3640, AAC-hbr obligatorio si se usa); APT-X estándar/mejorado (ADPCM, RFC7310).
- EBU Tech 3326 §3.3 opcionales: MPEG capa III; HE-AACv2; Opus (RFC6716, 6-510 kbit/s); AMR-WB/AMR-WB+.
- Oficio: Dante no es códec — transporte sin comprimir en red local, no cruza internet pública; se estudia en temas 11 y 15.
- Oficio: elegir códec — calidad/ancho de banda (comprimir lo menos posible); retardo (AAC-LD y búfer corto si hay ida y vuelta); compatibilidad (obligatorios de la norma); voz vs música (portátil=voz mono, concierto=general estéreo).

## Telefonía

- Oficio: entra por híbrido (2↔4 hilos) o por códec IP (SIP); en ambos, la mesa devuelve un N-1.
- UIT-T I.412: canal B puede llevar G.711 o G.722.
- UIT-T G.722 (09/2012): banda ancha 50-7.000 Hz, ancho nominal a 3 dB.
- UIT-T G.712 (11/2001): banda estrecha de G.711, exigencias entre 300-3.400 Hz.
- EBU Tech 3326: G.711 con paquetes de 20 ms por defecto, por compatibilidad con VoIP.
- Oficio: móvil (3G/4G/5G) como enlace — perfil asimétrico y búfer adaptativo por red cambiante.

## Streaming

- Oficio: streaming = distribución continua, se consume mientras llega; frente a descarga, descarga progresiva y difusión (TDT).
- Oficio: para directo, transmisión por secuencias (adapta calidad a la red); descarga progresiva no sirve.
- RFC 8216 (08/2017): HLS entrega continua fiable por HTTP; múltiples renditions (p.ej. traducciones de audio); Media/Master Playlist en UTF-8; cliente cambia de variant stream según la red; segmentos en orden.
- RFC 8216: documento informativo (Independent Submission), no estándar IETF; versión 7 del protocolo.
- AES TD1008.1.21-9 (24-09-2021, sustituye TD1004): pico máximo -1 dBTP a la entrada del codificador.
- AES TD1008 tabla 1: variado con voz medible -18 LUFS (+1 LU); sin voz medible -18 LUFS (+2 LU); música por pista -16 LUFS; música pista más alta -14 LUFS; interstitial -18 LUFS; asistente virtual -18 LUFS. Tolerancia no es objetivo.
- AES TD1008: «variado» incluye radio-style streams, conciertos, pódcast con voz/música/efectos.
- AES TD1008 tabla 2 (sin separar voz/música): News/Talk -18; pop -16; mixto -17; deportes -17; ficción -18. Fórmula: -16-[2×(%voz/100)] LUFS.
- AES TD1008: música 2-3 LU más alta que la voz; 1 LU ≈ diferencia perceptible mínima.
- AES TD1008: recomienda revisión futura a -23/-24 LUFS (armoniza con EBU R128, ATSC A/85, ANSI/CTA-2075, AES71-2018); archivar a -24 LUFS o menos y remasterizar. LUFS=LKFS (ITU-R BS.1770).
- Tema 13: EBU R128 remite a suplementos R128 s2 (streaming) y s3 (radio) y a Tech 3401; no leídos.
- Contrato-programa 2024-2026, cláus. 3.5 pto. 46: «Canal Sur Media» coordina OTT, pódcast, portales, redes, apps móviles. Pto. 45: prioridad de «Canal Sur Más» (streaming OTT) y plataforma propia de pódcast.
- Contrato-programa cláus. 3.19 pto. 103: «Canal Sur Más» 24h/día, todo dispositivo, alcance mundial sujeto a derechos.

## Podcast

- Oficio: sin definición normativa; fichero a la carta, corregible entero antes de publicar.
- Contrato-programa: pódcast en plataforma digital propia, bajo «Canal Sur Media».
- AES TD1008: pódcast entra en «variado» -18 LUFS (+1 LU), pico -1 dBTP.
- Apple Podcasts (requisito de plataforma, no norma): sonoridad en torno a -16 LKFS ±1 dB; pico verdadero ≤-1 dBFS; BS.1770-5; preacondicionar ANTES de codificar (el codificador no corrige sonoridad y puede recortar).
- Apple: acepta WAV/FLAC/MP3 para subir; WAV/FLAC no admite mono, fuente mono duplicada a 2 canales idénticos; si hay estéreo, se usa.
- Apple: MP3 mono mín. 44,1 kHz/32 kbps, recomendado 44,1-48 kHz/96-128 kbps; MP3 estéreo mín. 64 kbps, recomendado 128-256 kbps. RSS acepta MP3 o AAC; AAC mejor calidad a igual tasa, recomendado sobre MP3; tabla de tasas igual para ambos (mono/estéreo × 22,05-24/44,1-48 kHz).
- Apple: metadatos de sonoridad/pico en ID3 (MP3) o cabecera MP4.
- Oficio, caso emisión→pódcast: partir de máster a -24 LUFS o menos; subir ganancia al objetivo del destino (-18 o -16 LKFS); medir/ajustar antes de codificar; exportar con metadatos si es posible.

## Lo que este tema no da, y dónde está

- Equipos, procedimientos y nivel objetivo de sonoridad de CSRTV en radio e internet: sin fuente publicada localizada.
- Lenguaje de señas control-locutorio: no normalizado.
- EBU Tech 3329, R128 s2/s3, Tech 3401: no leídos.
- SRT, RIST, RTMP para radio: no leídos (SRT/RTMP en tema 13 del específico de Cámara).
- Definición normativa de pódcast; cuña/ráfaga/sintonía/careta: sin fuente; continuidad en tema 9.
- Micro/proximidad → tema 3; mesa/PFL/DIM → tema 4; proceso de voz → tema 5; intercom/IFB/TV → tema 8; Dante/AES67 → temas 11 y 15; R128/sonoridad → tema 13.
