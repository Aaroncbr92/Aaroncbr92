# Tema 14 del específico de Realizador/a · Formatos de vídeo, resolución, compresión, HD, UHD, HDR, códecs, archivos y entregables

**Siglas**: RTVA, CSRTV, RD, RA, UIT-R, EBU, SMPTE, AMWA, DPP, NABA, LOC, DCI, PQ, HLG, TC, LTC, VITC, DF, NDF, PsF, GOP, MXF, OP1a, OP-Atom, AAF, EDL, IMF, CPL, OPL, LPCM, BWF, VBR, CBR, RAID, LTO, ENG, CCU, LUFS, LU, dBTP, LFE, QC, AFD, PPD.

Esqueleto para repasar, no resumen: cada línea lleva su fuente; «of.» = oficio.

<!-- indice -->

## Índice

- [1. Formatos de vídeo](#1-formatos-de-vídeo)
- [2. Resolución](#2-resolución)
- [3. Compresión](#3-compresión)
- [4. HD y UHD](#4-hd-y-uhd)
- [5. HDR](#5-hdr)
- [6. Códecs](#6-códecs)
- [7. Archivos](#7-archivos)
- [8. Entregables](#8-entregables)
- [Lo que el tema no da](#lo-que-el-tema-no-da)

<!-- /indice -->

## 1. Formatos de vídeo

- Convenio X RTVA, anexo III, ficha 5351000 (p. 196): «Diseñar y coordinar todos los elementos técnicos-artísticos… controlar la calidad y duración»; «Dirigir las tareas de montaje, postproducción y mezclas». Sin formatos. RD 1680/2011: 0910 RA 4 e), RA 5 d); 0906 RA 2 c).
- Esencia / códec / contenedor (MXF, MOV, MP4, AVI) / metadatos / proyecto (AAF, EDL, XML) (of.). Formato = resolución, cadencia, barrido, muestreo, profundidad, códec y tasa, audio, contenedor.
- 29,97: proporción 1.000/1.001 (29,97, 59,94, 23,98). Europa 25 y 50. 10 bits = 1.024 niveles; 8 = 256.
- Z200 (Sony p. 336): MP4 = XAVC HS Long, XAVC S Long, XAVC S-I; MXF = XAVC Long, XAVC I, MPEG HD 422. Audio LPCM 24-bit, 48 kHz.
- Cadencias: BT.709-6 60, 50, 30, 25, 24 Hz (60, 30, 24 también /1,001); BT.2020-2 y BT.2100-3 120, 120/1,001, 100, 60, 60/1,001, 50, 30, 30/1,001, 25, 24, 24/1,001, progresivo.
- 29,97 en secuencia a 25 pierde unos 5 cuadros de cada 30. Lenta: 100 cuadros a 25 = 4 veces. 50i se desentrelaza; PsF no. NDF (24, 25, 30, 50) cuenta todos los cuadros; DF (29,97, 59,94) salta números, no imágenes.

## 2. Resolución

- SD: BT.601-7, 720 muestras de luminancia, 360 por diferencia de color. HD 1.280×720: no BT.709. HD 1.920×1.080 (BT.709-6). UHD 3.840×2.160 y 8K 7.680×4.320 (BT.2020-2, 16:9). DCI 4.096×2.160 (of.). BT.2100-3: «Pixel aspect ratio 1:1 (square pixels)».
- UHD = 4 veces HD (8.294.400 frente a 2.073.600); 8K = 4 veces UHD. BT.2100-3 nota 1b: «Productions should use the highest resolution image format that is practical».
- Relación = horizontal ÷ vertical: 4:3 = 1,33; 16:9 = 1,77; 1,85:1 y 2,39:1 cine. Ni focal, objetivo ni sensor la fijan.
- Letterbox: franjas arriba y abajo. Pillarbox: laterales (4:3 en ancha). No estirar (of.). EBU QC 0001F: AFD, «aspect ratio of the active picture». Zonas seguras (R 95): tema 12.

## 3. Compresión

- Casi todo con pérdida; transformada discreta del coseno. Redundancia: repetido o predecible. Entropía: lo nuevo.
- Ejes: sin/con pérdidas; intraframe (cada fotograma solo) / interframe (referencia más diferencias); producción/distribución; tasa constante/variable.
- BT.2100-3: 4:4:4 «same number of horizontal samples»; 4:2:2 «subsampled by a factor of two» horizontal; 4:2:0 horizontal y vertical. 4:4:4:4 = RGB más canal alfa (transparencia). Croma: 4:2:2 mínimo (tema 9).
- BT.2020-2 «10 or 12 bits per component»; BT.2100-3 «n = 10, 12» (4.096 con 12).
- BT.2100-3 tabla 9: rango estrecho negro 64, pico 940 (10 bits); 256 y 3.760 (12). Rango completo «should not be used for programme exchange unless all parties agree».
- EBU R 103 v3.0 tabla 1 (nominal / preferente / total): 8 bits 16-235 / 5-246 / 1-254; 10 bits 64-940 / 20-984 / 4-1019; 12 bits 256-3760 / 80-3936 / 16-4079; 16 bits 4096-60160 / 1280-62976 / 256-65279.
- R 103: fuera del preferido, error de gama; no exceder el total (recorta); aviso si supera el 1 % de la imagen. Directo: recortadores de cámara en preferentes (CCU, tema 4); pieza etalonada: nominales. Sub-negros: PLUGE. Analógico 0 a 700 mV. «−1 %» y «103 %» no son de R 103 v3.0.
- CBR fija (X400 «CBR, 50 Mbps»); VBR es máximo o media («VBR, 35 Mbps (max)»). Tasa sólo compara dentro del mismo códec. ProRes 422 HQ frente a Proxy: «nearly five times the data rate», PSNR 15-20 dB mayor.
- Sin comprimir = píxeles × muestras/píxel × bits × cuadros/s. 1080p25 4:2:2 10 bits: 1.920×1.080×2×10×25 = unos 1.037 Mb/s. HD-SDI ST 292-1: 1,485 Gb/s o 1,485/1,001. UHD 2160p50: unos 8.294 Mb/s.
- Relación: 50 Mb/s = unas 20 veces; 100 Mb/s, unas 10; DNxHD 121 Mb/s sobre 829 = unas 7.
- Minutos = capacidad en bits ÷ tasa ÷ 60. 128 GB a 200 Mb/s = 5.120 s, unos 85 min; a 500 Mb/s = unos 34 min. Hora a 121 Mb/s = 54.450 MB. Seis señales, una hora, 100 Mb/s = unos 270 GB.
- Captación: tarjeta. Montaje y máster: intracuadro. Emisión: GOP largo, que degrada con cualquier proceso. Versiones desde el máster. Transcodificar = recodificar; cambiar de contenedor no lo es.

## 4. HD y UHD

- BT.709-6: conserva entrelazado; captación P o I; progresivo con transporte P o PsF; entrelazado con transporte I. BT.601 «entrelazada».
- 1080i50 = «50/I», captación «25 interlace»: 50 campos, 25 cuadros. 1080PsF25 = «25/PsF»: dos segmentos del mismo instante; se monta como progresivo.
- BT.2020-2: «Scan mode Progressive»; sin entrelazado en UHD. Cinco ejes: resolución espacial, temporal, rango dinámico, cuantificación, espacio de color. HD con HDR = BT.2100.
- 601 estándar; 709 alta; 2020 ultra alta y gama amplia (SDR); 2100 alto rango dinámico.
- Contrato-programa RTVA 2024-2026 (BOJA 245, 26/12/2023), punto 85 (p. 42): HD «único sistema técnico de difusión televisiva por ondas hertzianas terrestres» desde el 14-02-2024; cooperar en UHD 4K. Punto 101 (p. 47): «artículo segundo del Real Decreto 16/2023, de 17 de enero».
- Formato HD concreto, códec, UHD o HDR de CSRTV: no consta.

## 5. HDR

- BT.2100-3 (02/2025): PQ o HLG. PQ: absoluta, hasta 10.000 cd/m²; ST 2084 «stabilized» (16-08-2014). HLG: «degree of compatibility with legacy displays»; relativa al pico.
- BT.709-6 punto 1.2: V = 1,099 L^0,45 − 0,099 (1 ≥ L ≥ 0,018); V = 4,500 L (0,018 > L ≥ 0); exponente 0,45; pantalla BT.1886. Curva logarítmica: de rodaje, exige etalonaje (of.).
- ST 2086: volumen de color del monitor de masterizado (2014-10-13, 2018-04-09; «stabilized»): estáticos.
- DaVinci Resolve 21 (jul. 2026): Dolby Vision, HDR10, HDR10+, HDR Vivid, HLG; los cuatro primeros PQ.
- HDR10: «no special metadata»; BDA: 3.840×2.160, «Up to the Rec. 2020 gamut», «1000 nits»; MaxCLL y MaxFALL; en 500 cd/m², «501–1000 will be clipped».
- HDR10+: Samsung; «per clip»; «SMPTE ST 2094 App4, Version 1, HDR10+ Profile B»; sidecar .json; HEVC «Main10». ST 2094-40 «Dynamic Metadata for Color Volume Transform — Application #4» (2016-08-24, 2020-04-09; «stabilized»).
- Dolby Vision: nivel 0 global; 1 análisis; 2 y 8 trims; 5 relación de aspecto; 6 MaxCLL y MaxFALL. Trims: licencia de Dolby. Entrega: XML, IMF o H.265.
- HLG: «without additional metadata»; BBC y NHK. Plano a plano: HDR10+ y Dolby Vision; HDR10 los del máster; HLG ninguno (of.).
- BT.2408-9 (03/2026): HDR Reference White = 203 cd/m² (PQ, o HLG de 1.000 cd/m²); Graphics White igual. Tabla 1: gris 18 % = 26 cd/m², 38 % PQ y HLG; blanco 203, 58 % PQ, 75 % HLG.
- BT.2100-3 tabla 3, monitor: «≥ 1 000 cd/m2» (áreas pequeñas), negro «≤ 0.005 cd/m2».
- BT.2408-9: SDR entra por mapeo directo o expansión. Luz de pantalla: conservar lo visto en SDR; luz de escena: igualar cámaras SDR y HDR (directo). Bajar a SDR: display-light, «usually preferred». «Currently, there is no universal approach.»
- RD 1680/2011 no nombra el HDR. No consta HDR en CSRTV.

## 6. Códecs

- Sony ILCE-1: intra por cuadro, GOP largo varios; intra mejor al editar, GOP largo mejor eficiencia. Editar intracuadro; distribuir intercuadro.
- XAVC = familia. XAVC S Long: H.264, MP4. XAVC HS Long: H.265, 10 bits, MP4. XAVC S-I: H.264 intra, MP4. XAVC Long / I: MXF. H.265: «some receivers may not support playback correctly» (Z200 p. 202).
- ProRes (LOC fdd000389): «proprietary, lossy… intermediate codecs»; 422 (Proxy, LT, 422, HQ) y 4444 (4444 XQ); 4:2:2, 10 bits, intracuadro, VBR; MOV, y MXF desde Final Cut Pro 10.3 (27-10-2016).
- DNxHD (Avid 2012): SMPTE VC-3; SMPTE 2019-4 (en MXF); 8 o 10 bits. 444 = 10 bits 4:4:4 440 Mb/s; 220x y 220 = 220 (1080i 30 cuadros; 24p 175); 145 = 8 bits (24p 115, 25p 120); 100 (1.920 a 1.440); 36 (offline).
- 1080i/50: 185x y 185 = 184 Mb/s; 120 = 121; 85 = 84. 1080p/25: esas más 365x (367) y 36.
- AVC-Intra (Panasonic FAQ 1, 4, 12, 13): 50 y 100 Mb/s; High 10 Intra y High 422 Intra de H.264; el 100 es 4:2:2, 10-bit; MXF OP-Atom en P2. H.264 no implica GOP largo.
- Audio sin pérdida: FLAC, Apple Lossless, WavPack. Con pérdida: AAC (distribución), Opus (tiempo real), AC-3, MP3; garantiza caudal. Editar y mezclar en PCM (WAV, BWF).

## 7. Archivos

- LOC fdd000013: MXF «wraps video, audio, and other bitstreams»; «digital equivalent of videotape»; ST 377-1:2011 (vigente «active», 2019-11-28). Contenedor, no códec.
- OP1a: ST 378:2004, «Single Item, Single Package», todo en un fichero. OP-Atom: ST 390:2011, un fichero por pista; Avid y P2. EBU R 122-2010: TC en MXF.
- EDL: cortes con TC, una pista. AAF: el más completo. XML: variante de fabricante (of.).
- EBU Tech 3285: BWF = WAVE más «Broadcast Audio Extension» («bext»); PCM, admite audio MPEG (of.).
- Proxy: copia ligera con TC (of.). Z200 pp. 160-161: simultáneo, «.mp4», sufijo «S03».
- LTC: como audio, entre equipos; 80 bits por cuadro, 32 de usuario (of.). VITC: en el intervalo vertical. Z200: Preset, Regen, Clock; Rec Run, Free Run.
- Libro de Estilo 5.3.3 (p. 81): TC «un acuerdo básico entre periodista y cámara»; 3.17.1.5 (p. 61): dos o más cámaras ENG, planos «técnicamente compatibles y uniformes», TC «idéntico».
- Resta a 25 fps, 00:47:17:23 a 01:23:54:00: cuadros 25−23 = 2; segundos 53−17 = 36; minutos 83−47 = 36; horas 0 = 00:36:36:02; inclusiva 00:36:36:03.
- Soportes (of.): SxS (Sony y SanDisk); P2 (Panasonic); XDCAM (Sony, disco óptico). Z200 p. 67: CFexpress Type A o SDXC.
- RAID (of.): 0 (2 discos, sin redundancia); 1 (espejo, 2); 5 (3, paridad); 6 (4, doble paridad); no es copia de seguridad. LTO (of.): cinta abierta, acceso secuencial lento. Archivo de CSRTV: no consta.

## 8. Entregables

- RD 1680/2011, 0907 RA 6: a) ventanas de explotación; b) copias; c) formato de masterización; d) documentación técnica. 0910 RA 5 e): EDL, off-line y on-line; RA 7 a): TDT, IPTV, satélite, cable, streaming, podcast, telefonía móvil.
- 0905 RA 1 f): «master, señal sin incrustaciones y cámaras dobladas o masterizadas»; mismo TC (of.).
- LE 3.17.1.5 (pp. 61-62): entrevista en unidad móvil, «falso directo»; máster sólo para «defectos técnicos de fácil resolución».
- Ficha de entrega de RTVA o CSRTV: no consta. 0907 RA 5 h): normas PPD, claquetas y pistas; RA 5 f): niveles, pistas.
- AMWA AS-11: «constrained media file formats (based on MXF)»; AS-11 UK DPP HD & SD; ampliaciones: Nordic, Australia, Nueva Zelanda, NABA, DPP; UHD y HDR; formato corto.
- IMF: «multiple territories and platforms»; ST 2067-2 (2013, 2016, 2020-04-07; «active»). CPL: una versión. OPL: «transformation of selected virtual tracks… into deliverables». RDD 59-1 Application DPP (ProRes): DPP y NABA, BT.2100.
- EBU R 123 (jul. 2009): Ⓜ Mono, Ⓢ Stereo, MCA Multichannel Audio. 5.1: L, R, C, LFE, L Sur, R Sur. Hasta 16 canales. «48 kHz, 24 bit». 8a: 1-2 Ⓢ; 3-8 MCA. 8b: 1-6 MCA; 7-8 Ⓢ. Tech 3343-2023: § 4.2 LFE excluido de la sonoridad; § 7.1 downmix Lo/Ro.
- R 128 (11/2023): −23,0 LUFS; ±1,0 LU en directo; pico −1 dBTP en producción; puede ser menor según distribución. Tema 13.
- EBU *Quality Control* (01-09-2015): plantilla por destino; Automated QC, File Package Compliance, Manual QC, File Structure Analysis.
- Catálogo QC (CC-BY 4.0; letras B, F, W sin interpretar): 0051B niveles de vídeo; 0010B sonoridad; 0021B destellos (tema 13); 0044B congelado; 0078B silencio; 0026F TC; 0082W duración; 0119B claqueta; 0248B subtítulos ausentes; 0001F AFD.
- YouTube (ejemplo): RTMP/RTMPS; H.264, H.265, AV1; hasta 60 fps; fotograma clave 2 s, máximo 4; CBR; AAC o MP3; «Rec. 709 for SDR»; 10 bits HDR con H.265, no AV1.

## Lo que el tema no da

- CSRTV: ficha de producción y entrega, cámaras e ingesta, archivo, UHD, HDR: no constan.
- No leídos: RD 16/2023; Plan Técnico Nacional de la TDT; especificaciones HDR10, HDR10+, Dolby Vision, HDR Vivid; ST 2094-40, 2086, 2084 (sólo fichas); MaxCLL y MaxFALL (siglas); DCI; H.264 y H.265; tasas de ProRes; DNxHR; XAVC en MXF; norma del LTC; AS-11; ST 2067-2; Tech 3363; R 122.
