# Esquema · Tema 6 del específico de Cámara Operador · Captación de sonido asociada a cámara

**Siglas**: EBU (Unión Europea de Radiodifusión); UIT-R; AES; ENG; DSLR; dB; dBFS; dBTP (pico verdadero); dBu (ref. 0,775 V); LU/LUFS (equiv. LKFS); LRA; QPPM; PML; AGC; PCM/LPCM; TC; XLR; EMI; CMRR; SPL.

Esqueleto para repasar. Todo desarrollado y verificado en el tema. Se quita explicación, nunca el dato.

<!-- indice -->

## Índice

- [Por qué el sonido es del operador](#por-qué-el-sonido-es-del-operador)
- [Magnitudes y margen audible](#magnitudes-y-margen-audible)
- [Transductores y cadena de audio](#transductores-y-cadena-de-audio)
- [XLR y línea balanceada](#xlr-y-línea-balanceada)
- [Microfonía](#microfonía)
- [Inalámbricos](#inalámbricos)
- [Niveles](#niveles)
- [Sincronía](#sincronía)
- [Ambiente](#ambiente)
- [Criterios básicos y errores](#criterios-básicos-y-errores)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)

<!-- /indice -->

## Por qué el sonido es del operador

- Libro de estilo CS (3.17.1, p. 59): equipo entrevista lleva **«auriculares, antorcha, equipo básico de iluminación, filtros, micrófonos...»**.
- Oficio: decisión sin repetir toma; inalámbricos de memoria; saber cuándo grabar aparte (cámara sin 2 receptores o sin entrada profesional).

## Magnitudes y margen audible

- Oficio: frecuencia (Hz); periodo (s, inverso); longitud de onda (m); amplitud (Pa o dB). Tono←frecuencia; intensidad←amplitud; timbre←armónicos.
- Margen audible: **20 Hz–20.000 Hz** (oído joven/sano). Zonas de oficio: infrasonidos <20 Hz; graves 20-250; medios 250-4.000 (inteligibilidad voz); agudos 4.000-20.000 (brillo); ultrasonidos >20.000. Se estrecha con la edad, por arriba.
- Aviso: µm es longitud, no frecuencia. Margen de frecuencias ≠ margen dinámico (dB). Sony PXW-Z200: entradas XLR, **«20 Hz to 20 kHz (±3 dB or less)»** (p. 337).

## Transductores y cadena de audio

- Oficio: micrófono = acústico→mecánico→eléctrico (presión→corriente); altavoz = eléctrico→mecánico→acústico. Amplificador y ecualizador no transducen; antena transduce corriente↔onda EM, no acústica.
- Sony PXW-Z200: INPUT1/2 XLR 3 pines, **LINE/MIC/MIC+48V** (p. 338); INPUT3 minijack (p. 338); micro interno **«Omnidirectional stereo electret condenser»** (p. 338); grabación **«LPCM 24-bit, 48 kHz, 4-channel»** (p. 336); escucha con **[Monitor CH]** (p. 99).
- Oficio: cadena = micro→cable/enlace→entrada (preamp+conmutador)→control nivel→A/D→tarjeta, en paralelo auriculares y medidor. Calidad la limita el eslabón más débil. XLR: norma AES14 (no desarrollada).

## XLR y línea balanceada

- DPA: línea balanceada, **«two conductors of the same type and equal impedance to ground... minimizes interference pickup»**; XLR, **«pin 1... shielding... should never carry the signal. Pins 2 and 3 carry the signal»**.
- DPA: no balanceada, **«the cable shield is a part of the circuit... does not provide sufficient isolation»**; balanceada, **«induced voltage has the same polarity... input will only accept a signal if oppositely phased... noise... is rejected»** = **CMRR**, **«expresses the suppression of induced EMI noise... possible only if you use balanced lines»**; exige impedancia igual pin2/pin3-masa en emisor, cable y receptor.
- DPA: sin equilibrio, **«Phantom power cannot be supplied»**; **«unbalanced cabling should be kept as short as possible»**; alejar de **«power transformers... lighting cables, power cables, speaker cables»**.

## Microfonía

- Transductor: dinámico (bobina móvil, sin alimentación); cinta (lámina, sin alim. salvo activos); condensador (fantasma 48 V o pila); electret (poca alimentación).
- Sony PXW-Z200, conmutador entrada: **«LINE: External audio device»**; **«MIC: Dynamic microphone, battery-operated microphone»**; **«MIC+48V: +48V phantom power microphone»** (p. 136). Aviso: **«may damage the connected device. Check the setting before connecting»** (p. 136); vacías→LINE (p. 136). Ref. MIC **«−30 dBu to −80 dBu»** (p. 338), fábrica −50 dB (p. 260); LINE **«+4dB/0dB/−3dB/[EBUL]»**, fábrica +4 dB (p. 260).
- Patrón/uso ENG: omnidireccional (corbata, ambiente); cardioide (mano reportero); supercardioide (directo con ruido); hipercardioide (lejanos/ruido, lóbulo muy estrecho, rechaza más el fondo); cañón (pértiga/sobre cámara); bidireccional/ocho (cara a cara). Micro interno Z200 omnidireccional estéreo (p. 338).
- Oficio: fuentes dispersas/ambiente fiel→omni; varias cercanas en movimiento→cardioide/omni; patrón estrecho castiga movimiento, mal apuntado suena peor que cardioide bien puesto.
- Efecto de proximidad (DPA): **«more bass by getting closer»**; sólo gradiente (cardioide…ocho), no omnidireccional (**«do not exhibit proximity»**); <1 m sí, >1 m **«practically no proximity effect»**; máximo on-axis, en cardioide desaparece a **«exactly 90 degrees»**. Oficio: mano cardioide pegado engorda voz; corbata omni sin efecto.
- Formas: lavalier/corbata (omni casi siempre); mano; cañón; diadema; solapa inalámbrico.
- Libro de estilo CS: corbata en entrevista fuera de plató (3.17.1, p. 59); mano no se cede al entrevistado (3.17.1.3, p. 60); directo, vertical sobre esternón, o corbata en interior habilitado (8.3.2, p. 117).
- Soportes: pie suelo/trípode; pie mesa; pértiga/jirafa; suspensión elástica; paravientos/peluca/cortavientos; pinza. Micro nunca rígido sobre soporte. Z200: **[CH1 Wind Filter]**, fábrica off (p. 260). Libro de estilo (8.6.1, p. 122): telas brillantes/satenes/sedas dan ruido de roce con corbata.

## Inalámbricos

- Niveles: banda (margen RF); grupo (canales sin interferirse, del fabricante); canal (frecuencia dentro del grupo).
- Regla: dos emisores van en el **mismo grupo** (contraintuitivo); grupos distintos o extremos, sin garantía.
- Oficio antes de grabar: pilas; misma banda/grupo/canal o emparejar; canal libre; sensibilidad a la voz; auriculares; cable de reserva.
- Dos inalámbricos en una cámara: sí, mismo grupo, cada emisor a su canal/receptor, pistas separadas (mejor que mezclar en cámara, irreversible). Sony PXW-Z200: hasta 4 canales XLR con **XLR-K2M/XLR-K3M** (p. 139); fábrica los 4 en **[Internal MIC]** (p. 260).

## Niveles

- Margen dinámico = techo (máx. sin distorsión) − suelo (ruido propio). Cálculo: 6 dB/bit (20·log2≈6,02 dB): 16 bits≈96 dB; 24 bits≈144 dB (por eso 24 bits en producción). Oído: ~120 dB (otra magnitud).
- EBU R 68: **«at least 16 bits»** (BS.646); nota 1: **«16-bit recordings may not meet the requirements... depending on... A/D and D/A converters»**. Sony PXW-Z200: **«MIC mode: 80 dB (typical)»**, **«LINE mode: 90 dB (typical)»** (p. 337): lo fija la electrónica, no los bits.
- Alineación digital: 0 dBFS = techo. R 68: **«18 dB below the maximum possible coding level... irrespective of... bits»** (nota 2: ratio 1:8, 18,06 dB). Tech 3343 §8.1: tono 1 kHz a **−18 dBFS**. Z200 de fábrica trae tono a −20 dB (origen no consta).
- Por qué 18 dB: R 68, alineación 9 (u 8) dB bajo PML; picos reales hasta 3 dB sobre el medidor, con error de operación hasta 6 → **15 dB** sobre alineación; 18 dB de reserva los cubre. PML −9 dBFS **obsoleto** con sonoridad (Tech 3343 §8.1); alineación **no cambia**.
- EBU R 128 (v5, nov. 2023): objetivo **−23,0 LUFS**, tolerancia **±1,0 LU** en directo, medida **±0,2 LU**; pico verdadero **≤−1 dBTP** en producción, ±0,3 dB (≤20 kHz); medidor según BS.1770/Tech 3341; LRA según Tech 3342, no recomendado <1 min. LUFS=LKFS; 1 LU=1 dB (Tech 3341 §2.4).
- Tech 3341: ventanas M **0,4 s** sin puerta; S **3 s** sin puerta; I con puerta (BS.1770).
- Sonoridad y cámara: alineación sigue en −18 dBFS/1 kHz, lee −18 LUFS con tono en fase en ambos canales; EBU recomienda **medidor de pico** para alinear. Margen 1 dB bajo 0 dBFS cubre infralectura ~0,5 dB (4x oversampling, 48 kHz); **−2 dBTP** para MPEG-1 L2 y AC-3. Más margen favorece ambiente; comentaristas deporte ~**−24 LUFS** (Tech 3343 §3.5.1).
- Mandos Z200: **AUTO/MAN** (p. 16); ruedas **AUDIO LEVEL** en manual (p. 138); **[Limiter Mode]** Off/−6/−9/−12/−15/−17 dB, fábrica Off (p. 261); **[CH1&2 AGC Mode]** Mono/Stereo, fábrica Stereo (p. 261); **[Reference Level]** −20/−18/−16/−12/[EBUL], fábrica −20 dB (p. 260); **[1kHz Tone on Color Bars]** fábrica Off, con On tono también en CH3/4 (p. 261); **[CH1 Wind Filter]** fábrica Off (p. 260).
- Oficio: fábrica −20 dB, para R 68 pasar a −18 dB; EBUL sin explicar en manual; AGC sube ruido en pausas, se usa en imprevisto, no en entrevista; estéreo enlazado, un golpe baja ambos canales; limitador sólo en manual, red de seguridad.
- Ajuste práctico (oficio, 7 pasos): conmutador+fuente de canal; manual; prueba de voz real; medidor de pico (voz sobre referencia, picos lejos de 0 dBFS); limitador puesto; auriculares continuos; revisión in situ. Libro de estilo (5.4, p. 82): nivel **«con rigor»**; revisar **«en el mismo lugar»**.

## Sincronía

- Sistema único (imagen+sonido mismo fichero, sincronía automática) vs doble sistema (grabador aparte, sincronía manual). ENG casi siempre único.
- DSLR/sin espejo: entrada 3,5 mm consumo, sin fantasma, preamp ruidoso → sonido aparte a grabador externo + claqueta + sincronizar en posproducción. No sirven: adaptador a 6,35 mm (sigue por preamp de cámara), XLR a DSLR (no hay entrada), ni «cable para sincronizar» (no sincroniza).
- Claqueta: marca visible+audible; si falta, palmada. Delante del objetivo, encuadrada, con las 2 grabaciones en marcha; si empieza sin claqueta, se da al final invertida.
- TC: etiqueta h:m:s:cuadro por fotograma. Libro de estilo (5.3.3, p. 81): TC **«acuerdo básico entre periodista y cámara»**, mejor a 00:00:00 al inicio (texto de 2004/cinta, idea vale para tarjeta). Sony Z200 (p. 298): sincroniza por **TC IN/OUT**, enclava (**«EXT-LK»**), tras ~10 s se mantiene sin cable; **«do not start recording immediately»**; misma frecuencia de cuadro; puede derivar **«one frame per hour»**; modos **Free Run/Clock**. Bits de usuario: 8 hex por clip (p. 99), sin regla CSRTV.
- Rompe sincronía: cámara lenta (Z200, **«Audio is not recorded in Slow & Quick Motion mode»**, p. 136, suelta el TC); frecuencia distinta; retardo de receptor digital/red en directo (se compensa en control, tema 13); plano sin claqueta/TC común.

## Ambiente

- Libro de estilo (5.4, p. 82): **«El sonido ambiente tiene que ser registrado siempre y en cualquier circunstancia, incluso aquellas en las que su ausencia sea casi absoluta»**; **«El canal 2 recoge el sonido ambiente, captado a través del micrófono de la cámara»**.
- Sonido-noticia (5.4, p. 82): grabación **«específica, continuada y suficiente... incluso por los canales 1 y 2 simultáneamente»**, imagen subordinada; si importa tanto como la imagen, canal 1 de mesa de sonido.
- Ambientes ruidosos (5.4, p. 82): **«han de evitarse... para la grabación de declaraciones»**, salvo que el sonido sea la información. DPA: **«SPL from point sources drops by 6 dB/doubling of distance»** (40→20 cm ≈+6 dB; 40→10 cm ≈+12 dB, fuente puntual aprox.).
- No se falsea (3.2.2, p. 46): **«La música o el falseamiento del sonido ambiente... procedimiento reprobable»**; si falta, sólo **«sonidos idénticos... o lo más parecidos»**.
- Raccord (6.4, p. 92): **«El nivel de las voces, el sonido ambiente y el ruido de fondo tienen que permanecer... sin alteraciones»**.

## Criterios básicos y errores

- Reparto de canales, Libro de estilo (5.4, p. 82): **«el sonido directo de declaraciones, ruedas de prensa o el del periodista ante cámara se registra por el canal 1»**; canal 2 ambiente. Oficio: declaración/entrevista→corbata/mano; rueda prensa→mesa LINE o atril; periodista ante cámara→su micro; musical/discurso→mesa (o los 2 canales si es noticia); recursos→micro cámara en ambos si cabe.
- Antes de grabar (oficio): pilas+repuesto; banda/grupo/canal; conmutadores+fuente; manual+limitador+filtro viento+paravientos; tono a −18 dB si R68, con barras; TC acordado/enclavado; prueba de voz+escucha. Libro de estilo (p. 82): regla de barras/noticia por cinta, sin regla vigente en tarjeta.
- Mientras se graba: auriculares siempre; nivel **«con rigor»**; ambiente siempre; no pisar diálogo; margen antes/después de cada declaración. Después: revisar in situ **«desde la perspectiva de la imagen y del sonido»**; avisar a redacción de fallos.
- Errores típicos: condensador en MIC sin pila→no suena; no compatible en MIC+48V→daño; mesa en MIC→satura; automático en entrevista→sube ruido en pausas; picos a 0 dBFS→distorsión; grupos distintos→interferencia; corbata rozando ropa→ruido; sin auriculares→fallo tardío; canal de fábrica en Internal MIC→no graba lo conectado; cámara lenta→sin sonido.

## Recomendaciones técnicas que el tema cita

- EBU R 68-2000, R 128-2023 (V5), Tech 3341-2023, Tech 3343-2023: cifras arriba, en «Niveles».
- Citadas sin texto leído: UIT-R BS.1770, BS.645, BS.646, EBU Tech 3342, AES14.

## Lo que este tema no da, y dónde está

- Cámaras/micros/inalámbricos propios de CSRTV, canales 3-4, tono/barras en tarjeta: no consta.
- Nivel de voz en dBFS fijado por norma; origen del −20 dB de fábrica; [EBUL] en la Z200: no consta.
- Bandas de frecuencia para inalámbricos en España: Cuadro Nacional de Atribución, no leído.
- Formatos/entrega: tema 7. Redacción/entrevista: tema 8. Calidad técnica: tema 9. Directo: 3 y 13. Cámara lenta: 15. Ruido, riesgo laboral: 14 y 17.
