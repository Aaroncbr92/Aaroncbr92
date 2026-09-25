# Tema 4 del específico de Operador/a Montador/a de Vídeo · Formatos de vídeo y audio

**Siglas**: RTVA; CSRTV; UIT-R (UHDTV); EBU; SMPTE (ST); AMWA; LOC; ENG; SD, HD, UHD; DCI; SDR, HDR; PQ, HLG; cd/m² (nit); fps; DF/NDF; RGB, YCbCr; GOP; AVC/H.264, HEVC/H.265; MPEG; MXF (OP1a, OP-Atom); MOV, AVI; AAF, EDL, XML; IMF (CPL, OPL); RDD; PCM/LPCM; WAV, BWF; VBR, CBR; PSNR; Mb/s, Gb/s, GB; SDI (SD/HD/3G/12G); BNC; IP; RTP; SDP; AES (AES3, AES67); PTP (IEEE 1588); LUFS, LU, dBTP; LFE; UMID.

Esqueleto para repasar, no resumen: cada línea remite a un dato del tema; se repasa releyendo el tema, no memorizando esto.

<!-- indice -->
<!-- /indice -->

## Formatos: esencia, códec, contenedor, proyecto

- Esencia = imágenes/sonido · códec = cómo se comprime · contenedor = cómo se empaqueta (MXF, MOV, MP4) · proyecto = qué se hizo (AAF, EDL, XML) — oficio
- Un contenedor admite códecs distintos y viceversa: «MXF»/«MP4» no dicen la calidad — oficio
- Formato de grabación = resolución + cadencia + barrido + muestreo + profundidad + códec/tasa + audio + contenedor — oficio
- Nombre de cámara (ej. XAVC S Long 422 3840×2160P 50P): familia + compresión + muestreo + resolución + cadencia — Sony PXW-Z200
- UHD televisión (3.840×2.160, 16:9) ≠ 4K cine DCI (4.096×2.160, ~17:9) — BT.2020-2/oficio

## Resolución

- SD: 720 muestras/línea activa, 360 por diferencia de color; 4:3 o 16:9 — BT.601-7
- HD (Full HD): 1.920×1.080, 16:9 — BT.709-6
- UHD/4K TV: 3.840×2.160; 8K: 7.680×4.320; ambos 16:9, píxel cuadrado 1:1 — BT.2020-2, BT.2100-3
- UHD = 4× píxeles de HD (8.294.400 vs 2.073.600); 8K = ×4 más — cálculo
- Producir en la resolución más alta practicable, entregar en la que toque (down-sample mejora calidad) — BT.2100-3, nota 1b

## Compresión: principio, muestreo, profundidad

- Códec con pérdida: recuantifica coeficientes de la DCT, descarta altas frecuencias — oficio
- Audio de cámara sin comprimir, en LPCM — oficio; Sony PXW-Z200: LPCM 24-bit, 48 kHz, 4 canales
- 4:4:4 sin submuestreo; 4:2:2 mitad en horizontal; 4:2:0 mitad horizontal y vertical — BT.2100-3
- 4:4:4:4 = RGB sin submuestreo + canal alfa (transparencia) — oficio; ST 2110-20 tiene colorimetría «ALPHA» para señales de clave
- UHD: 10 o 12 bits/componente (1.024 o 4.096 niveles) — BT.2020-2, BT.2100-3
- Rango estrecho: negro=64, blanco=940 (10 bits); rango completo 0-1.023 sólo si hay acuerdo — BT.2100-3, tabla 9

## HD y UHD

- BT.709-6: cadencias 60/50/30/25/24 Hz y las de 60/30/24 entre 1,001; admite P, PsF e I — BT.709-6
- 1080i50 = 25 cuadros/50 campos; 1080PsF25 = progresivo segmentado; 1080p = progresivo — oficio sobre BT.709
- BT.2020-2: 3.840×2.160 y 7.680×4.320, 16:9; cadencias hasta 120 Hz; sólo progresivo, sin entrelazado — BT.2020-2
- UHD suma 5 ejes: resolución, cadencia, rango dinámico, cuantificación (bits), gama de color — BT.2020-2/BT.2100-3
- BT.2100-3 cubre HD a 8K con HDR: un HD con HDR es de la BT.2100, no de la BT.709 — BT.2100-3, tabla 1

## HDR

- HDR amplía el recorrido de brillo negro-blanco, no la resolución — oficio
- Dos curvas: PQ (referencia absoluta, hasta 10.000 cd/m², ST 2084) y HLG (relativa al pico de pantalla) — BT.2100-3
- Metadatos de masterizado del monitor: ST 2086 (título sólo, contenido no leído)
- HDR10, HDR10+, Dolby Vision: sin fuente normativa leída — declarado
- Señalización: cada flujo declara colorimetría y TCS (SDR/PQ/HLG); si no se declara, se asume SDR (salvo señal de clave) — ST 2110-20
- Blanco de referencia HDR y del grafismo: 203 cd/m² = 58 % PQ / 75 % HLG; gris 18 % = 26 cd/m² = 38 %/38 % — Informe BT.2408-9, tabla 1
- SDR→HDR: mapeo directo (preserva aspecto) o expansión/up-mapping (usa más rango); por luz de pantalla o de escena — Informe BT.2408-9
- Regla: convertir una vez al entrar, no encadenar SDR-HDR-SDR — Informe BT.2408-9 («no universal approach»)

## Códecs

- Intracuadro: comprime cada cuadro solo, mejor para editar, ficheros mayores — Sony ILCE-1
- GOP largo (intercuadro): comprime varios cuadros, mejor eficiencia, sufre con manipulación — Panasonic AVC-Intra FAQ
- H.264/AVC y H.265/HEVC: normas de compresión; XAVC S usa H.264, XAVC HS usa H.265 (10 bits) — Sony ILCE-7SM3
- H.264 admite perfiles intracuadro (AVC-Intra) — no es sinónimo de GOP largo
- XAVC (Sony): familia, no códec; S/HS Long en MP4, S-I intra en MP4, XAVC Long/I en MXF
- ProRes (Apple): familia intermedia con pérdida, intracuadro, 4:2:2 10 bits VBR; familias 422 y 4444; contenedor MOV (también MXF desde FCP 10.3) — LOC fdd000389
- DNxHD (Avid, SMPTE VC-3): 8/10 bits, variantes de 36 a 440 Mb/s; mapeo MXF por ST 2019-4 — Avid, 2012
- AVC-Intra (Panasonic): perfiles H.264 intracuadro, 50 y 100 Mb/s, 4:2:2 10 bits (el 100), MXF OP-Atom — Panasonic AVC-Intra FAQ
- Audio: sin pérdida (FLAC…) vs con pérdida (AAC, Opus, AC-3, MP3); contribución se graba/edita en PCM, códec con pérdida sólo al final — oficio

## Frame rate

- BT.709: 60/50/30/25/24 Hz + entre 1,001; BT.2020/BT.2100: hasta 120 Hz, sólo progresivo — citas
- Familia europea 25 (y múltiplos); familia americana entre 1,001 (23,98/29,97/59,94) por la introducción del color — oficio
- Secuencia a cadencia de entrega; material de otra cadencia se convierte (pierde/mezcla cuadros si no son múltiplo) — oficio
- Cámara lenta: grabar a más cadencia, reproducir a la de emisión — oficio
- Código de tiempo NDF (cadencias enteras) vs DF (cadencias no enteras, salta números no cuadros) — oficio

## Bitrate

- CBR: tasa constante; VBR: tasa variable según complejidad (máximo o media) — Sony X400, LOC fdd000389
- Tasa sólo compara dentro del mismo códec — oficio
- Tasa sin comprimir = píxeles × muestras/píxel × bits × fps — cálculo; HD 1080p25 4:2:2 10b ≈1.037 Mb/s; UHD 2160p50 ≈8.294 Mb/s
- Minutos = capacidad(bits) ÷ tasa ÷ 60 — cálculo; cifras de fabricante pueden diferir de la nominal (Panasonic AVC-Intra)

## Contenedores

- MXF (SMPTE): contenedor profesional de TV; «equivalente digital de la cinta» — LOC fdd000013, ST 377-1
- OP1a: todo en un fichero (ST 378); OP-Atom: un fichero por pista, Avid/P2 (ST 390) — LOC fdd000013
- MOV (Apple, habitual de ProRes); MP4 (familia MPEG, cámaras ligeras); AVI (Microsoft, poco en TV) — oficio
- Código de tiempo en MXF: EBU R122 (no leída) — LOC fdd000013
- WAV/BWF: BWF = WAV + bloque «bext» de la EBU, sonido/radiodifusión — EBU Tech 3285
- Cambiar de contenedor sin tocar la esencia no es transcodificar, no pierde calidad — oficio

## SDI/IP

- SD-SDI ≈270 Mb/s; HD-SDI 1,485 Gb/s; 3G-SDI 2,970 Gb/s; 12G-SDI 11,88 Gb/s; conector BNC 75 Ω — ST 259, ST 292-1, ST 424, ST 2082-1
- 1080i50/1080p25→HD-SDI; 1080p50→3G-SDI; 2160p50→12G-SDI — cálculo
- ST 2110: familia IP, cada elemento por separado, reloj común — ST 2110-10
- ST 2110-20 vídeo sin comprimir + metadatos SDP; ST 2110-30 audio PCM (48 kHz obligatorio) — citas
- PTP (IEEE 1588) reparte el reloj común (grandmaster) — ST 2059-2
- ST 2022-7: redundancia, dos flujos idénticos, conmutación sin corte (redes «roja/azul», convenio) — ST 2022-7, ST 2110-10 §8.5

## Estándares de entrega

- Sin ficha técnica publicada de RTVA/CSRTV: se dan normas de referencia del sector — declarado
- AS-11 (AMWA): MXF restringido para entrega a emisora/editor, por destinatario; ampliado a UHD/HDR y formatos cortos — AMWA
- IMF (ST 2067-2): un máster, varias versiones (CPL) y perfiles de salida (OPL); RDD 59-1 para TV sobre BT.2100 — SMPTE
- Configuraciones de audio: mono/estéreo/multicanal 5.1 (L, R, C, LFE, L Sur, R Sur); LFE excluido de la medida de sonoridad — EBU R 123, EBU Tech 3343-2023
- Orden de pistas pactado, hasta 16 canales (tabla 1, ej. asignaciones 8a/8b) — EBU R 123
- Downmix por defecto Lo/Ro — EBU Tech 3343-2023 §7.1
- Sonoridad: −23,0 LUFS (±1,0 LU en directos), medida del programa entero, pico verdadero ≤−1 dBTP — EBU R 128-2023

## Aplicación práctica

- Identificar formato de cada clip (resolución, cadencia, barrido, códec, muestreo, profundidad, curva, audio) — § tema
- Secuencia a la cadencia/resolución de entrega; UHD se usa escalado; material a otra cadencia se convierte o transcodifica
- Archivo SD se sube a HD (bandas o reencuadre); HDR ajeno se convierte por luz de pantalla si la pieza es SDR
- Audio: PCM 48 kHz, normalizar a −23 LUFS, pico ≤−1 dBTP; exportar máster y derivar versiones (una generación menos)
