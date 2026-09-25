# Tema 9 del específico de Operador/a de Sonido · Grabación, edición y postproducción

**Siglas**: RTVA, CSRTV, UER/EBU, AES, SMPTE, DAW, PCM, WAV, BWF, UMID, FLAC, AAC, dBFS, dBTP, LUFS, LU, LRA, TC, LTC, VITC, DF/NDF, EDL, VCA, MIDI, ADR, M&E, HVAC, GPIO, QC.

Esqueleto para repasar, no resumen: cada línea remite a un dato del tema; el razonamiento y la cita completa están en el tema.

<!-- indice -->
<!-- /indice -->

## Grabación, edición y postproducción

- (oficio) Postproducción: volcado, montaje, grafismo, VFX, etalonaje, montaje/mezcla de sonido, máster. Cadena de sonido: montaje de diálogos, ADR/looping, Foley, efectos de biblioteca, ambientes, ambientación musical, mezcla, pista internacional.
- (J. O. Smith, Stanford) Teorema del muestreo: reconstrucción sin error si no hay contenido a la mitad de la frecuencia de muestreo o por encima; si lo hay, *aliasing*.
- (oficio/tema 1) 3 parámetros: frecuencia de muestreo (44,1/48/96/192 kHz), bits (16/24/32 flotante), canales; ~6 dB/bit.
- (cálculo) Estéreo/min: 44,1 kHz/16 b ~10,6 MB; 48 kHz/24 b ~17,3 MB; 96 kHz/24 b ~34,6 MB.
- (oficio) Sin pérdida: FLAC, Apple Lossless, WavPack. Con pérdida: AAC distribución, Opus tiempo real, AC-3 Dolby/cine/TV, MP3.
- (oficio) Contribución en PCM (WAV/BWF); códec con pérdida sólo en distribución final.
- (oficio) Equipos: grabador de mano, multipista de campo, estación con interfaz, estado sólido de emisora.
- (oficio, EBU R 68, temas 4-5) Para postproducción: fuente en su pista, 24 bits, 48 kHz en TV, −18 dBFS de alineación, TC de imagen, nombre y datos identificables.

## Músicas

- (oficio) Ambientador: sintonía, ráfagas, fondos, cortes musicales; decide en preproducción, coloca en postproducción. No es suyo: etalonaje (imagen), lanzar piezas (continuidad), decidir/contratar música (preproducción).
- (oficio) Piezas: sintonía (única), careta (entrada), ráfaga (separa bloques), fondo (bajo la voz), corte musical (primer plano). Fondo baja con la voz, sube en huecos; a mano o con *ducker* (tema 5). Edición: corte a compás y cierre de frase; recorte de fragmento entero; final con cadencia o fundido, nunca corte seco.
- (AES TD1008) «normalizing music 2 or 3 LU higher than speech» — sólo internet, no emisión (R 128 mide el programa entero, tema 13).
- Derechos: se gestionan en preproducción; gestión propia de CSRTV sin fuente.

## Cuñas, ráfagas y continuidad

- (oficio) Cuña (anuncio), ráfaga (identidad), careta (entrada), promoción (propio), indicativo (emisora); sin definición normativa.
- (EBU R 128 s1) UER: «advertisements (commercials) and promos»; muy breves: «interstitials, stingers, bumpers».
- (EBU R 128 s1) Fin: límite de Maximum Short-term Loudness junto a Programme Loudness y True Peak, contra piezas «overly dynamic».
- (EBU R 128 s1) Corto: «up to approximately 2 minutes, typically shorter than 30 seconds»; cada pieza es «a programme»; vale «audio-visual or audio-only».
- (EBU R 128 s1, b/c/d/f/g) Target −23,0 LUFS ±0,2 LU; por debajo sólo declarado a propósito; Short-term ≤−18,0 LUFS (+5,0 LU) +0,2 LU; programa entero sin énfasis por elemento; True Peak ≤−1 dBTP ±0,3 dB. LRA no se especifica en contenido corto.
- (EBU R 128 s1) Versiones: 2014 1ª ed.; 2016 V2 quita límite alternativo de Momentary; ago-2020 V3 añade tolerancias QC/True-peak, vigente.
- (cálculo) Cuña −23,1/−1,5 dBTP/−15,5 corto plazo: integrada y pico cumplen, corto plazo excede 2,5 LU; bajar entera sacaría la integrada de tolerancia; reducir dinámica del pasaje fuerte y remedir.
- (AES TD1008, tabla 1, «Interstitial») Internet: −18 LUFS, +0,2 LU; no es la emisión (R 128 s1, −23 LUFS).
- (EBU Tech 3343 §2.4) Señalización a salida: procesador a *Bypass* o sólo limitador de pico verdadero, vía GPIO o red de control.
- (oficio) Antes de continuidad: comprobar integrada, corto plazo, pico; sin silencio de más; duración/nombre según pauta. Sistema CSRTV sin fuente.

## DAW

- (oficio) DAW = ordenador + programa + interfaz; organización tipo mesa (tema 4): pistas, envíos, buses, inserciones, bus, línea de tiempo. Edición no destructiva: cortar/mover/fundir no cambia el fichero; sólo un proceso aplicado o la exportación.
- (cálculo) Latencia ms = muestras × 1.000 ÷ Hz. 128/44.100 = 2,9 ms.
- (cálculo, 44,1 kHz) 64 = 1,5 ms (monitor DAW); 128 = 2,9 ms (grabación); 512 = 11,6 ms (mezcla); 2.048 = 46 ms (mezcla cargada).
- (cálculo, 48 kHz) 64=1,33; 128=2,67; 256=5,33; 512=10,67; 1.024=21,33 ms.
- (oficio) Buffer pequeño graba, grande mezcla; insuficiente da chasquidos. Latencia real > buffer: suma conversores y proceso; *look-ahead* compensado retrasando otras pistas.
- (oficio) Corte en silencio/cruce por cero; fundido limpia entrada/salida; encadenado con fundidos solapados; ajuste de nivel iguala tomas. Voz: cortar en pausas sin quitar todas las respiraciones; el ambiente bajo el corte tapa la unión (tema 6).
- (Manual de estilo RTVE, cap. 3 RNE, referencia de oficio) Duración del corte: «el tiempo imprescindible [...] resulte radiofónicamente aceptable». Modo: «debe evitarse cortar un testimonio en alto»; bajar el sonido cuando el oyente ya se hizo idea; entenderse cada voz.
- (oficio) EDL: fuente, TC entrada/salida, posición, transición; sin color, niveles, rótulos ni efectos; recompone cortes, no la mezcla. Automatización (tema 4): nivel/panorama/silencios/envíos/procesos sobre la línea de tiempo; modos Off/Read/Write/Touch/Latch/Trim (Pro Tools).

## Pistas

- (oficio) 5 capas: diálogos, ambientes, Foley, efectos de biblioteca, música; tema 6 las agrupa en 4. Separar por capas: razón comercial, permite banda internacional (M&E) para doblar sin remontar.
- (oficio, tema 6) Una fuente, una pista; agrupadas por capa con bus propio; fuente mono en pista mono; nombre y orden fijo de sesión.
- (Pro Tools Reference Guide) Tipos: audio (graba/reproduce ficheros), auxiliar (envíos/submezclas), máster (nivel general de ruta), VCA (agrupa/desplaza niveles, «do not pass audio»), MIDI (datos, no audio), instrumento (MIDI+audio), carpeta (contenedor; encaminamiento sí pasa audio), vídeo (referencia de imagen).
- (Pro Tools Reference Guide) Mono/estéreo/multicanal (3-8 canales, Ultimate/Studio) en audio, auxiliar, encaminamiento, máster e instrumento. Máster terminado: pistas según destino, mezcla/internacional/audiodescripción (oficio); reparto de CSRTV sin fuente.

## Sincronía

- (oficio) POSICIÓN: TC/MTC (si falla, no cuadran). VELOCIDAD: word clock/vídeo (si falla, deriva lenta). MUESTRA: word clock (si falla, chasquidos). El TC no sincroniza el reloj de muestreo. Deriva de 0,01 %/h → 0,36 s/h = 9 cuadros a 25 fps (cálculo).
- (oficio) TC = HH:MM:SS:CC. LTC: señal de audio entre equipos. VITC: dentro del vídeo. Palabra LTC: 80 bits/cuadro, 32 de usuario (norma SMPTE no leída). DF/NDF sólo en 29,97/59,94 fps; a 25/50 no hace falta.
- (cálculo) Resta de TC de derecha a izquierda con acarreo según cadencia; ej. 00:47:17:23 a 01:23:54:00 = 00:36:36:02 (o :03 inclusiva). 13.440 muestras/48.000 Hz = 0,28 s ×25 fps = 7 cuadros; atajo, 1.920 muestras/cuadro a 48 kHz-25 fps. Muestras/cuadro a 48 kHz: 24 fps=2.000; 30 fps=1.600; 29,97 no entero; 50 fps=960. 1 cuadro a 25 fps = 40 ms.
- (EBU Tech 3285, TimeReference) BWF guarda las muestras desde medianoche, no HH:MM. Ej.: 10:00:00 a 48 kHz = 1.728.000.000 muestras.

## Doblaje

- (oficio) ADR = sustitución de diálogo en sincronía labial, en sala viendo la imagen (*automated dialogue replacement*; *looping*, del bucle de película). Usos: diálogo mal grabado, cambiar interpretación, añadir diálogo no rodado. No es ADR: combinar pistas (mezcla), entorno visto (ambiente), ventana cronológica (línea de tiempo).
- (oficio) Doblaje a otro idioma: actor de doblaje; requiere banda internacional (mezcla menos la voz a sustituir). En documental, pista internacional lleva músicas/ambientes/totales originales, fuera la voz en off (tema 6).
- (oficio) Sesión ADR/doblaje: sala seca, micro a distancia fija; tipo y distancia parecidos al directo si casa; cada toma en su pista con TC. En mezcla, voz al plano de imagen (EQ/reverb) con ambiente debajo; sincronía labial referida al cuadro (40 ms a 25 fps); desfase máximo tolerable sin fuente.

## Limpieza

- (oficio) Limpiar: quitar lo que sobra sin tocar lo que sirve. Ruido constante → reducción por perfil; zumbido de red → filtro de ranura/reductor; chasquidos → reductor/edición; recorte → reconstrucción (grave, sin arreglo); oclusivas → paso alto/reductor; sibilantes → reductor (tema 5); viento/roces → paso alto/reductores/edición; reverberación → reductor con límites. Lo no grabado no se limpia; lo recortado no se recupera. Módulos iZotope RX 11: De-click, De-clip, De-crackle, De-ess, De-hum, De-plosive, De-reverb, De-rustle, De-wind, Spectral De-noise (nombres comerciales).
- (iZotope RX 11) Spectral De-noise: aprende perfil del ruido y lo resta; sirve para cinta, HVAC, exteriores, red, bucles de masa, motores, ventiladores, viento, zumbido complejo. Paso 1: trozo de ruido más largo, pocos segundos; de ahí grabar un minuto de ambiente sin nadie (tema 6). Perfil manual: ruido constante; adaptativo: ruido cambiante (tráfico, olas).
- (iZotope RX 11) Umbral más alto reduce más ruido pero suprime señal de bajo nivel; reducción distinta en partes tonales y aleatorias; aplicar sólo la supresión necesaria. Artefactos: fuerte → sonido «chirpy or watery»; puerta ancha → ráfagas de ruido tras callar la señal (*Artifact Control*).
- (oficio) Evitar artefactos: reducir poco en varias pasadas, comparar con el original a igual nivel. Orden en diálogo: edición, paso alto, zumbido, reducción por perfil suave, sibilantes/oclusivas, luego EQ/compresión (tema 5); bajo el corte sigue el ambiente.

## Mezcla

- (oficio) Sobre material grabado: repetible, automatizable, medible entero antes de entregar (frente al directo, tema 8). Orden: 1) diálogos (referencia); 2) ambientes; 3) efectos; 4) música (deja sitio a la voz); 5) conjunto: bus de salida, sonoridad, pico.
- (EBU Tech 3343) Mezclar «only by ear», con nivel de escucha fijo (nivel de referencia, tema 8).
- (EBU Tech 3343 §3.1) Postproducción: ±0,2 LU sobre −23 LUFS (directo ±1 LU, tema 13). §3.2 Fuera de tolerancia: corrección de ganancia estática; medidores fuera de línea miden y corrigen.
- (tema 13, cálculo) X dB de ganancia mueve integrada X LU y pico X dB. −21,4/−2,5 dBTP, bajar 1,6 dB → −23,0/−4,1 dBTP: cumple. −24,5/−1,8 dBTP, subir 1,5 dB → −23,0 pero −0,3 dBTP: no cumple; limitar antes ≥0,7 dB y remedir.
- (oficio, tema 13) Revisión: integrada −23 LUFS (±0,2 LU); corto plazo ≤−18 LUFS en piezas cortas; pico ≤−1 dBTP; voz entendible; fase (suma mono no pierde voz); sin chasquidos/silencios digitales/saltos de ambiente; sincronía al principio y al final.

## Entrega

- (oficio) Máster por especificaciones: formato/códec, resolución/cadencia, color/niveles, pistas de audio, sonoridad, estructura (barras/tono, claqueta, cuenta atrás), subtítulos; uno por destino (emisión, plataforma, internacional).
- (oficio, EBU R 68, temas 4/13) Al técnico de sonido: pistas, sonoridad −23 LUFS en emisión, tono de cabecera a −18 dBFS. Especificaciones de CSRTV sin fuente.
- (Pro Tools Reference Guide) *Dither*: minimiza artefactos de cuantificación al reducir bits (24→16), notable en pasajes suaves/fundidos; añade ruido aleatorio de muy bajo nivel; *noise shaping* aparta el ruido de 4 kHz. Siempre al bajar a 16 bits en el output principal; no en submezcla interna, destino de 24 bits o analógico de 24 bits, ni escucha normal. Último proceso, en la pista máster. Sin él, *Bounce Mix* trunca; exportación de fragmentos e importación a sesión de menos bits sí lo aplican.
- (Pro Tools Reference Guide) SRC: 5 calidades, de Low a Tweak Head (más calidad, más lento). Orden fijo: primero SRC manteniendo el bit depth alto, luego reducir a menos bits con dither. Ej.: 48 kHz-24 bits → CD 44,1 kHz-16 bits: SRC a 44,1 kHz con 24 bits, luego 16 bits con dither al final.
- (EBU Tech 3285) BWF: WAVE + bloque «Broadcast Audio Extension»; intercambio entre entornos y plataformas; PCM normal, admite MPEG con bloque propio. V0 (1997); V1 (64 de 254 bytes reservados = UMID SMPTE); V2 (metadatos de sonoridad R 128), compatible hacia atrás.
- (EBU Tech 3285) Campos bext: Description (≤256), Originator (≤32), OriginatorReference (≤32), OriginationDate, OriginationTime, TimeReference, Version, UMID (64 B), LoudnessValue, LoudnessRange, MaxTruePeakLevel, MaxMomentaryLoudness, MaxShortTermLoudness, CodingHistory. Sonoridad ×100: −23,0 LUFS = −2300. CodingHistory: cada codificación añade una línea nueva.
- (oficio, tema 13) Metadatos deben coincidir con la sonoridad real; material externo se remide. Archivo de futuro (AES TD1008): «at a loudness of -24 LUFS or lower and then remastered for distribution».
- (oficio) Se archiva: mezcla, pista internacional, capas separadas, sesión con originales. Cuña 30 s, 48 kHz-24 bits estéreo (cálculo): −23 LUFS (±0,2 LU), corto plazo ≤−18 LUFS (+0,2 LU), pico ≤−1 dBTP, sin LRA; PCM/BWF; bext con −2300 si −23,0 LUFS; tamaño 288.000×30 = 8.640.000 B ≈ 8,6 MB + cabecera.
- Ninguna norma legal (ley/reglamento) regula grabación/edición/postproducción: sólo documentación de fabricante, recomendaciones técnicas, oficio y cálculo.
