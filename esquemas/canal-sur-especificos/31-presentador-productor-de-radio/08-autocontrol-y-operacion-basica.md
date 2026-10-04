# Tema 8 del específico de Presentador Productor de Radio · Autocontrol y operación básica

**Siglas**: RTVA, CSRTV, RTVE, RNE; UER/EBU (R, Tech); UIT-R BS.1770; dB, dBu, dBFS, dBTP; LUFS, LU; M/S/I; LRA; PPM; PFL, AFL, SIP; DIM; HPF; EQ; DCA; LCR; DAW; QC; GPIO; N-1; AES.

Esqueleto para repasar, no resumen: sin norma legal; fuente delante de cada línea.

<!-- indice -->

- [Autocontrol y operación básica](#autocontrol-y-operación-básica)
- [Niveles](#niveles)
- [Entradas](#entradas)
- [Salidas](#salidas)
- [Cuñas](#cuñas)
- [Músicas](#músicas)
- [Ráfagas](#ráfagas)
- [Continuidad](#continuidad)

<!-- /indice -->

## Autocontrol y operación básica

- Oficio: autocontrol = locutor opera su mesa; el técnico prepara, mantiene, resuelve. López Vigil: locutor integral «manejar la consola». Otro autocontrol (dominio ante micrófono) = tema 4.
- Oficio, mesa: amplificar, procesar, mezclar, encaminar, monitorizar; bloques: previo, EQ, dinámica, envíos, buses, matriz, monitorado.
- Audioarts AIR 1, AIR 4, D&R AIRENCE-USB (no consta que sean las de CSRTV): micrófono abierto corta altavoces (feedback); AIR 1 tally automático, contacto «TALLY output», la mesa no enciende la lámpara; AIRENCE «Mute by Mic» + relé luz roja, «Mute-Act» atenúa 20 dB.
- AIR 4: tecla ON arranca equipos externos e híbrido. AIRENCE: arranque por fader (sólo si el conector está cableado).
- Oficio: auriculares antes de abrir micrófono; no subir «para probar» el fader de pieza grabada.

## Niveles

- Yamaha CL: «DIGITAL GAIN» distinta de la analógica del previo; la que fija señal/ruido es la analógica.
- PFL = antes del fader, va a la escucha, no al bus principal. AFL = después del fader (Soundcraft: con Aux Masters). Yamaha: PFL, AFL o POST PAN; PFL tras EQ.
- Soundcraft SIP: canal con efectos silenciando las demás entradas; PFL «very useful for setting proper input preamp levels»; SIP «less good for level setting».
- Soundcraft: señal lo más alta posible con margen = headroom. Procedimiento: PFL, ganancia hasta zona amarilla (cifras Soundcraft), soltar, repetir. «EQ affects gains settings».
- Oficio: ganancia con fuente real, no «probando». Soundcraft: faders en torno a 0 (escala logarítmica), masters a 0.
- Cálculo: dB se suman: −3 + x = 1, fader +4; 40 + 3 − 5 = 38.
- R 68: alineación 18 dB bajo el máximo de codificación, cualquier nº de bits; 1:8 (18,06 dB). Tech 3343 § 8.1: 1 kHz a −18 dBFS. Equivalencia en dBu: no está en R 68 ni Tech 3343. Yamaha: oscilador senoide o ruido rosa.
- Oficio: 0 dBFS máximo. Headroom = nominal → saturación; rango dinámico = suelo de ruido → saturación; no son headroom masterización ni dB SPL.
- Rane: elemento de ganancia + cadena lateral (detector, calculador); clave externa. Oficio: compresor/limitador sobre el umbral; expansor/puerta bajo él.
- Oficio, compresor: umbral, relación (4:1), ataque, relajación, codo, make-up (el compresor sólo baja; el «más fuerte» lo da el make-up).
- Rane, voz: ataque 25–100 ms, relajación 100–500 ms, 2:1 a 4:1, codo blando. Oficio: comprimir sube el ruido; la sonoridad la mide el medidor.
- Oficio, limitador: ≥10:1, ataque muy rápido. Rane: evita recorte, protege altavoces, evita overs y sobremodulación.
- R 128 V5 (nov. 2023), UER, no AES. h): −23,0 LUFS; directo ±1,0 LU; la desviación no debe ser práctica habitual. i): ±0,2 LU de medida.
- R 128 m): ≤ −1 dBTP «during production (linear audio)», ±0,3 dB (20 kHz); otros sistemas más bajo (Tech 3344). j): objetivo más bajo a propósito, indicado, sin compensar.
- R 128 k): medidor UIT-R BS.1770 (puerta, ecuación 7) y Tech 3341. l): programa entero, sin énfasis en voz/música/efectos. n): LRA (Tech 3342) no recomendado en menos de 1 minuto. o): máximos M y S. p): metadatos con la sonoridad real.
- R 128: publicidad, tráiler, promo = programa.
- Cálculo: directo = −24 a −22 LUFS; se trabaja con S e I. Tech 3343 § 3.5.1: comentaristas deportes p. ej. −24 LUFS. Ficha de R 128: ±0,5 LU (2014), no en el articulado de 2023; manda el articulado.
- Oficio: −1 dBTP y no 0: el pico real entre muestras supera el de muestras. LUFS absoluta; LU relativa; 1 LU = 1 dB.
- Tech 3341: M 400 ms; S 3 s; I programa entero. Puerta sólo en I: absoluto −70 LUFS; relativo 10 LU bajo la sonoridad con puerta absoluta (§ 2.3); bloques 400 ms, solape 75 %.
- Oficio, medidores: vúmetro (promedio, 300 ms, no protege del recorte); PPM (no llega al pico real, no dice cómo suena); pico de muestra dBFS; pico real dBTP; sonoridad LUFS.
- Cálculo, magazine: I = −24,6, 1,6 LU bajo objetivo, fuera de margen; resto algo más fuerte que −23; subir voces en faders, no ganancia. Medidor a cero al empezar; se mira S.

## Entradas

- Yamaha CL (ejemplo): canal de entrada recibe de I/O, tomas traseras o slots 1-3 y envía a STEREO, MONO, MIX, MATRIX.
- Cadena Yamaha, 10 bloques: 1 INPUT PATCH; 2 Ø (polaridad); 3 DIGITAL GAIN; 4 HPF; 5 4 BAND EQ (HIGH, HIGH MID, LOW MID, LOW); 6 DYNAMICS 1 (puerta, ducking, expansor, compresor); 7 DYNAMICS 2 (compresor, compansor, de-esser); 8 INPUT DELAY (1000 ms); 9 LEVEL/DCA 1-16; 10 ON.
- Ø no retrasa, el retardo corrige desfase; HPF antes de EQ y dinámica.
- Yamaha ON: «If this is off, the corresponding channel will be muted»; PFL comprueba antes.
- Soundcraft MUTE GROUPS: on/off de varios canales en un botón. Yamaha CL: 8 grupos, entradas y salidas, un canal en varios.
- Oficio, locutorio: locutor (voz real, HPF, compresión moderada); invitados (ganancia al llegar, abiertos al intervenir); música, cuñas, ráfagas (línea, normalizadas, sin retocar); teléfono con mezcla menos.

## Salidas

- Soundcraft BUS: conductores con estéreo, grupos, PFL, envíos aux. Yamaha: canal de salida con EQ y dinámica; MIX (a puerto, MATRIX, STEREO, MONO), STEREO y MONO (C) (LCR, los tres), MATRIX (de entradas, MIX y STEREO/MONO; sólo a puertos).
- Oficio: escucha del control no va al programa. DIM atenúa una cantidad fija y conocida, no toca el programa; mute de canal sí lo quita; solo = sólo el seleccionado.
- Yamaha talkback: micrófono TALKBACK al bus elegido, instrucciones; oficio: nunca al programa. Con talkback, talkback dimmer baja los monitores.
- Soundcraft: EFFECTS SEND = aux post-fade; FOLDBACK SEND = aux pre-fade, monitor independiente.
- Soundcraft/Yamaha: pre-fader independiente del fader (monitores, grabación, mezclas independientes); post-fader sigue al fader (reverb, delay, subgraves por aux). Oficio: reverb en pre suena con fader cerrado; retorno en post cambia con cada fader, acople.
- Yamaha Mix Minus: quita el canal de una persona de lo enviado a MIX/MATRIX. Oficio: a mano, aux con todas las fuentes menos la suya. Autocontrol: la que el locutor devuelve a teléfono o línea exterior. N-1, híbrido = tema 7.

## Cuñas

- Manual RTVE 7.5: «Montaje breve» para vender (publicitaria) o captar audiencia (promocional); cuña de contenido o «píldora».
- López Vigil cap. 10: «Un mensaje breve y repetido que pretende vender algo»; nombre del taco de carpintería. Clases: comercial; promocional (promo); educativa o de servicio público. Duración media 30 s o menos (observación, no norma). Cuatro C: Corta, Concreta, Completa, Creativa. Viñeta = texto comercial leído en directo.
- R 128 s1: «advertisements (commercials) and promos (as well as interstitials etc.)»; «interstitials, stingers, bumpers and similar very short items».
- Manual RTVE 7.5: indicativo = montaje muy breve que identifica la emisora; punto = lo mismo para un espacio concreto.
- R 128 s1 V3 (ago. 2020), motivo: máxima a corto plazo además de sonoridad y pico; evitar piezas «overly dynamic». Contenido corto: hasta aprox. 2 minutos, típicamente menos de 30 s; cada pieza = programa; «audio-visual or audio-only».
- R 128 s1 b): −23,0 LUFS, ±0,2 LU. c): más bajo a propósito, indicado, sin compensar. d): corto plazo (Tech 3341) ≤ −18,0 LUFS (+5,0 LU), +0,2 LU de tolerancia. f): programa entero. g): ≤ −1 dBTP (Tech 3344), ±0,3 dB.
- Tres cifras de una cuña: −23 LUFS integrada; −18 LUFS máx. corto plazo (S = 3 s); −1 dBTP. LRA «not useful for short-form content», sin máximo ni mínimo.
- R 128 s1, versiones: nov. 2014; V2 ene. 2016 quitó el límite momentáneo; V3 ago. 2020 añadió tolerancias (QC y true-peak); vigente V3.
- Cálculo, cuña 20 s: −23,1 LUFS, −1,5 dBTP, máx. corto plazo −15,5: excede 2,5 LU (2,3 con tolerancia, −17,8); bajar 2,5 dB deja −25,6, fuera de ±0,2; reducir dinámica del pasaje fuerte y remedir.
- López Vigil cap. 3: bache = «un silencio inesperado, no previsto». Oficio, autocontrol: lanzar sin pisar ni bache; no retocar si viene normalizada; cerrar micrófonos mientras suena; si suena distinta, avisar para medir.

## Músicas

- Oficio: sintonía, careta, ráfaga, fondo (bajo la voz), corte musical.
- Manual RTVE 7.5: sintonía = señal sonora, generalmente melodía, que marca comienzo y final de un espacio; careta = sobre sintonía o fondo, créditos, títulos fijos y otros textos. Funciones de la música = tema 1.
- Oficio: manda la voz; fader, automatización del DAW o ducker.
- AES TD1008 (internet): música 2 o 3 LU sobre la voz, si es viable. En emisión R 128 mide el programa entero.
- López Vigil cap. 6, fondos: sobriedad («como el azúcar»); entrada discreta; cerrar con la frase musical, no con el reloj.
- Rane, ducker: «works the opposite of a gate»; atenúa cuando la clave externa supera el umbral; ataque, hold, profundidad 0 a −80 dB; usos: paging, «talkover». Oficio: radio/TV = música por el camino principal, voz por la clave externa; baja también con tos o ruido; profundidad y hold deciden si «bombea».
- Derechos y archivo = tema 10; gestión de CSRTV: no consta.

## Ráfagas

- Manual RTVE 7.5, cortinilla («también llamada ráfaga»): separa secciones, noticias o párrafos; «en determinadas ocasiones» 4 s = punto y seguido, 8 s = punto y aparte; ni norma técnica ni de Canal Sur.
- López Vigil cap. 6: cortina (más de 20 s larga; menos de 8 no separa escenas); ráfaga musical (menos segundos que la cortina, música ágil); puente musical (transición simple); música de telón (larga, rematada, final del programa).
- Para RTVE cortinilla = ráfaga; para López Vigil la ráfaga es más corta; no trasladar segundos. López Vigil: las frases musicales «no deben truncarse» por la norma de 8 o 10 s.
- Manual RTVE 7.5, golpe: efecto sonoro que acentúa un instante concreto.
- Cálculo sobre R 128 s1: ráfaga ≈ «stingers, bumpers»; cifras de la cuña (−23 LUFS, −18 LUFS corto plazo, −1 dBTP); sin LRA.
- Oficio, autocontrol: lanzar en el hueco de la voz sin bache; abrir micrófono al acabar o sobre su cola; normalizada, fader en su sitio, si no corregir la pieza; misma ráfaga, mismo cambio.

## Continuidad

- Tres sentidos: de la emisora (oficio: indicativos, promociones, cuñas, sintonías); guion de continuidad (Manual RTVE 7.5); hablada (Manual RTVE 3.2.1.1, RNE).
- Manual RTVE 7.5, guion de continuidad: contenido completo con textos del presentador, fuentes externas, recursos sonoros, instrucciones técnicas para el control; en autocontrol, para el locutor. Escaleta, pauta, guion = tema 2.
- Manual RTVE 3.2.1.1: entradillas, transiciones o continuidades = lazos entre informaciones; sólo con nexos, si no «continuidad forzada»; riesgo de muletillas. 3.2.1: boletín horario = «el eje de la continuidad informativa».
- Tech 3343 § 2.4: el sistema de emisión señala material conforme al procesador de sonoridad (GPIO o red); el procesador pasa a Bypass o a sólo limitación de seguridad de pico verdadero.
- Oficio, antes de cargar: integrada, máx. corto plazo, pico verdadero; sin silencio de más.
- Oficio, paso en autocontrol: despedir al invitado y cerrar su micrófono (o grupo); ráfaga de salida sin bache; cuñas normalizadas sin tocar faders; PFL de lo siguiente con fader cerrado; careta o ráfaga y abrir micrófono sobre su final; vigilar I en margen y S sin saltos.
- No consta: estudios, mesas, emisión, nivel objetivo, procesadores y entrega de publicidad de CSRTV; libro de estilo de Canal Sur Radio; duración normativa de cuña, ráfaga o cortinilla. No leídas: R 128 s3, Tech 3401.
- Remisiones: temas 1, 2, 4, 7, 10, 14, 15.
