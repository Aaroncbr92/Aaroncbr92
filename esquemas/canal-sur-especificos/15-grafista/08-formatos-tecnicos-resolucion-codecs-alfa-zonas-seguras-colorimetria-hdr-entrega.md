# Tema 8 del específico de Grafista · Formatos técnicos: resolución, códecs, alfa, safe areas, colorimetría, HDR/SDR y entrega para emisión

**Siglas**: RTVA, CSRTV, UIT-R, EBU, SMPTE, AMWA, LOC, SD, HD, UHD, SDR, HDR, PQ, HLG, GOP, QC, DSK, TCS, CICP.

Esqueleto para repasar, no resumen: lo que no está aquí se estudia en el tema.

<!-- indice -->
<!-- /indice -->

## 1. Resolución
- BT.601-7: SD 720 muestras luma/línea, 360 por diferencia de color; 4:3 o 16:9
- BT.709-6: HD 1.920×1.080. 720p 1.280×720 no es de la BT.709 (Z200: 50p, 59,94p)
- BT.2020-2 y BT.2100-3: UHD 3.840×2.160; 8K 7.680×4.320; 16:9. 4K cine DCI 4.096×2.160 (oficio, DCI no leída)
- BT.2100-3 tabla 1: píxel cuadrado 1:1. UHD = 4× píxeles de HD (8.294.400 / 2.073.600)
- BT.2100-3 nota 1b: producir en la mayor resolución práctica y bajar; ampliar ablanda
- Aspecto = ancho/alto con píxel cuadrado; 4:3=1,33; 16:9=1,77; 1,85; 2,39
- Letterbox: franjas arriba/abajo; pillarbox: laterales; grafismo se recompone
- QC 0001F AFD: relación de aspecto de la imagen activa y zonas de recorte seguras
- BT.709-6 cadencias 60, 50, 30, 25, 24 Hz (÷1,001 en 60, 30, 24); captación P o I; P transporta P o PsF; sistemas 50/I y 25/PsF
- 1080i50 = 50 campos, 25 cuadros; PsF como progresivo; filetes finos parpadean en entrelazado
- Contrato-programa 2024-2026 (BOJA 245, 26/12/2023) punto 85 (p. 42): HD único sistema terrestre TDT desde 14-02-2024; UHD 4K y TDT móvil, cooperación
- Punto 101 (p. 47): art. 2 RD 16/2023, 17 enero (modifica RD 391/2019); p. 11: actualizar producción, edición y emisión
- No consta: formato HD, códec, UHD o HDR de CSRTV
- Sin comprimir = píxeles × bytes: 1080 RGB 6.220.800 B; RGBA 8.294.400; 2160 RGBA 33.177.600; TGA alfa 25 fps ~207 MB/s, ~12,4 GB/min

## 2. Códecs
- Códec con pérdida (DCT; bloques, contornos, detalle que «hierve»); redundancia vs entropía
- Ejes: lossless/lossy; intra/inter; producción/distribución; tasa constante/variable
- 4:4:4 grafismo, croma; 4:2:2 producción; 4:2:0 distribución; 4:1:1 SD antiguo; cuarta cifra = alfa (Apple 4:4:4:4: Y'CbCrA o RGBA)
- Croma: 4:2:2 mínimo, mejor 4:4:4; texto rojo fino sobre azul, peor caso
- Bits: 8→256; 10→1.024; 12→4.096; banding. BT.709-6 8 o 10; BT.2020-2 10 o 12; BT.2100-3 10, 12 (tabla 9)
- BT.709-6 (8/10 bits): negro 16/64; blanco 235/940; CB, CR acromático 128/512, extremos 16 y 240/64 y 960; datos 1-254/4-1.019; sincronismo 0 y 255/0-3 y 1.020-1.023
- BT.2100-3: rango estrecho por defecto (negro 64 o 256, pico 940 o 3.760); completo (0-1.023 o 4.095) no en intercambio sin acuerdo
- Diseño 0-255; TV 16-235; Viz 5.4 «Downscale Luma» 0-255→16-235, Active
- EBU R 103 v3.0 tabla 1, nominal / preferente / total: 8 bits 16-235 / 5-246 / 1-254; 10 bits 64-940 / 20-984 / 4-1019; 12 bits 256-3760 / 80-3936 / 16-4079; 16 bits 4096-60160 / 1280-62976 / 256-65279
- Fuera del preferente = gamut error; sin exceder el total; aviso tras >1 % de imagen; directo: cámaras al preferente; preproducido: nominal
- Recorte: distorsión armónica, alias, más tasa; legalizadores con cuidado; sub-negros no (PLUGE, Anexo 2); analógico 0-700 mV; «−1 %» y «103 %» no son de R 103 v3.0
- Viz «Allow Super White» Inactive; «Allow Chroma Clipping»
- Sony: intra mejor al editar, GOP largo más eficiencia; Panasonic FAQ 2 (comercial): GOP largo para distribución, manipular degrada. Editar intra; distribuir GOP largo
- H.264 XAVC S; H.265 XAVC HS 10 bits; Z200 p. 202: H.265 en streaming, receptores pueden fallar; H.264 no es sinónimo de GOP largo
- ProRes (LOC fdd000389): propietario, con pérdida, intermedio, 10 bits; 422 Proxy, LT, 422, HQ; 4444, 4444 XQ; 422 4:2:2, intra, tasa variable; MOV y MXF (Final Cut Pro 10.3, 27-10-2016); PSNR HQ +15-20 dB sobre Proxy, ~5× tasa
- ProRes 4444: 4:4:4:4, alfa sin pérdida hasta 16 bits; XQ hasta 12 bits/canal
- Tasas Apple (abril 2022, 1080, 29,97 fps): 4444 XQ ~500 Mb/s; 4444 ~330; 422 HQ ~220; 422 ~147; LT ~102; Proxy ~45
- Únicos ProRes con alfa: 4444 XQ y 4444. 1 min 4444: 330×60÷8 = 2.475 MB vs ~12,4 GB TGA
- DNxHD (Avid 2012): 8 y 10 bits; VC-3; MXF SMPTE 2019-4; 444 4:4:4 440 Mb/s; 220x (10 bits) y 220 (8 bits) 220 Mb/s a 1080i/30 (175 a 24p); 145: 145 (115 a 24p; 120 a 25p); 100 (1920→1440); 36 offline progresivo
- DNxHD 1080i/50: 185x y 185 184 Mb/s; 120 121; 85 84 (1.440×1.080); 1080p/25 añade 365x (10 bits, 4:4:4, 367) y 36
- DNxHR no leído; alfa en DNxHD: no consta
- AVC-Intra (Panasonic FAQ): intra 50 y 100 Mb/s; High 10 Intra y High 422 Intra; 100 = 4:2:2, 10 bits, 1920×1080; MXF OP-Atom (P2)
- Contenedores: MXF (SMPTE), MOV (Apple), MP4 (MPEG), AVI (Microsoft). ProRes MOV y MXF; DNxHD MXF y MOV; XAVC MP4 o MXF
- MXF contenedor, no códec (LOC fdd000013; ST 377-1:2011). OP1a (ST 378:2004): un fichero; OP-Atom (ST 390:2011): un fichero por pista
- Extensión no dice si hay alfa: nombrar el códec

## 3. Alfa
- Alfa = cuarto canal de opacidad: 0 transparente; máximo opaco; grises = borde suave; ProRes 4444 hasta 16 bits
- JPG nunca; PNG 32 bits; TIF 32 o más; TGA 32 (24 sin alfa). Gráficos: bits por píxel; vídeo: por componente
- PSD y AI nativos; TIFF artes gráficas; PNG web; TGA secuencias; GIF 256 colores, alfa de un valor; SVG web; EPS imprenta, según caso
- Straight (Resolve 21, cap. 77, p. 1726): RGB sin alterar por el alfa; Photoshop, Gimp, PNG, BMP, TARGA (Blender 5.2)
- Premultiplied: canales × alfa antes de componer; salida de motores de render; OpenEXR; el alfa no se multiplica (p. 1727)
- Reglas p. 1728: Merge con premultiplicadas; corregir color solo sin premultiplicar; filtrar y transformar premultiplicadas; nunca doble premultiplicado. Error: halo; conversión con posible pérdida
- Directo: relleno (fill) + llave (key); Viz 5.2 Dual Channel; Viz 5.4: Contains Alpha, Invert Luma, Watchdog Key Opaque; mismo H-delay
- ATEM: DSK sobre la transición; panel multimedia guarda alfa
- ST 2110-20:2022 § 7.4.1: key con colorimetría «ALPHA», sin TCS; § 7.6: sin TCS, SDR salvo key
- Errores: sin alfa (fondo negro); directo/premultiplicado; ProRes 422; fill/key desfasados o key invertida

## 4. Zonas seguras (safe areas)
- SMPTE ST 2046-1:2009 (23-11-2009; «active»; revisa RP 218-2002): acción tolera distorsión; título no. Antecesoras RP 218, RP 27.3 (CRT). Pantallas pueden mostrar todo el cuadro (§ 5 nota)
- EBU R 95 v1.1 (junio 2017, 16:9), nota 5: acción 3,5 % y grafismo 5 % por borde (93 % y 90 % centrales); 576i, 720p, 1080i/psf, 1080p, 2160p, 4320p (figuras 1 a 6); grafismo en Graphics Safe; el centro no se desplaza
- R 95 1080p (fig. 4): acción 67 px lados, 38 arriba/abajo: 1786, líneas 80-1083; grafismo 96 y 54: 1728, líneas 96-1067 (activas 42-1121 de 1125). 1080i/psf (fig. 3) mismos anchos
- R 95 2160p (fig. 5): acción 134 y 76: 3572×2008; grafismo 192 y 108: 3456×1944; 4:3 central 1296 px en 1080, 2592 en 2160
- ST 2046-1 § 1: 1920×1080, 1280×720, 720×576, 720×480; sin 2160; mismo aspecto adquirido y mostrado; RP 2046-2 no leída
- §§ 4.3-4.5: Production Aperture = imagen activa; áreas concéntricas
- § 5 «shall»: 1080 acción 93 % (1786×1004), título 90 % (1728×972); 720 (1190×670) y (1152×648); 576 (670×536) y (648×518); 480 (670×446) y (648×432)
- Redondeo al entero más próximo (1.785,6→1.786; 1.004,4→1.004). 480 líneas (§ 5.4): RP 218 acción 90 % (648×432), título 80 % (576×384). 576 (§ 5.3): UIT-R (BT.1379-2, no leída)
- Graphics Safe Area (EBU) = Safe Title Area (SMPTE); en 1080 mismas cajas
- Cuentas: 1080 96 px y 54 líneas, 1.728×972; 2160 192 y 108, 3.456×1.944; 720 64 y 36, 1.152×648
- Oficio: mosca, reloj, marcador, textos legales en zona de grafismo; probar rótulo más largo

## 5. Colorimetría
- Síntesis aditiva: tres conos, primera ley de Grassmann. RGB pantalla, CMYK tinta; PNG sin CMYK; PSD, JPG, TIFF sí
- Primarios (x, y), CIE 1931. BT.709-6: R 0.640, 0.330; G 0.300, 0.600; B 0.150, 0.060; D65 0.3127, 0.3290
- BT.2020-2 (tabla 3) y BT.2100-3 (tabla 2; 630, 532, 467 nm): R 0.708, 0.292; G 0.170, 0.797; B 0.131, 0.046; D65. BT.2408-9 § 5.1: BT.709 «may be placed in a BT.2020 container»
- Luminancia (R, G, B): BT.601 0,299, 0,587, 0,114; BT.709 0,2126, 0,7152, 0,0722 (3.2); BT.2020 0,2627, 0,6780, 0,0593 (tabla 4)
- CL: Y del RGB lineal, luego gamma; NCL: gamma, luego Y'. BT.2020-2 admite ambas. BT.2100-3: NCL por defecto (tabla 6); CI ICtCp (tabla 7): I = 0.5L' + 0.5M', CT, CP; CI no en intercambio sin acuerdo
- BT.709-6 (1.2): V = 1,099 L^0,45 − 0,099 (1 ≥ L ≥ 0,018); V = 4,500 L (0,018 > L ≥ 0); 0.45 ≈ inversa de 2,2; BT.1886 en pantalla
- BT.2408-9 § 9: fijas RGB en rango completo; CICP (UIT-T H.273) señala primarios, transferencia, matriz y rango; PNG, TIFF, AVIF, HEIF
- sRGB (IEC 61966-2-1:1999, no leída): primarios y D65 de BT.709 (PNG 3.ª ed., 24-06-2025, tabla 17); luminancia WCAG 2.2 (12-12-2024) como BT.709; curva R = RsRGB/12.92 si ≤ 0.04045, si no ((RsRGB+0.055)/1.055)^2.4; PNG gamma 45455; rango completo. Difiere de BT.709 en curva y rango
- LUT: técnica o creativa; 1D o 3D; no sustituye la conversión BT.2408

## 6. HDR/SDR
- BT.2100-3 (febrero 2025): PQ o HLG
- PQ: «very wide range of brightness levels for a given bit depth»; absoluta, hasta 10.000 cd/m². HLG: «a degree of compatibility with legacy displays»; relativa. ST 2084 (16-08-2014; stabilized)
- Formato HDR: 10 o 12 bits, BT.2020/2100, PQ o HLG; HD con HDR posible
- ST 2086 (2014-10-13, 2018-04-09; stabilized): volumen de color del monitor de masterizado
- Resolve 21 (julio 2026): Dolby Vision, HDR10, HDR10+, HDR Vivid (PQ), HLG (sin metadatos). ST 2094-40 «Dynamic Metadata… Application #4» (2016-08-24, 2020-04-09; stabilized): dinámicos en HDR10+ y Dolby Vision; HDR10 solo máster (oficio)
- ST 2110-20: BT709, BT2020, BT2100; TCS SDR, PQ, HLG; sin TCS, SDR
- BT.2408-9 (marzo 2026) tabla 1: blanco de referencia y del grafismo 203 cd/m² (PQ, o HLG de pico 1.000) = 58 % PQ, 75 % HLG
- Monitor BT.2100-3 (tabla 3): pico ≥1.000 cd/m², negro ≤0.005; SDR ~100 nits (oficio)
- SDR a HDR: mapeo directo (como BT.709 en BT.2020) o up-mapping; por luz de pantalla (SDR etalonado en programa HDR; 100 % SDR ≈ 203 cd/m²) o de escena (cámaras SDR y HDR en directo)
- HDR a SDR: display-light, preferido; scene-light cambia gráficos incrustados; «round-trip» pérdidas; «no universal approach»
- § 9: SDR graphics directo a Graphics White (75 % HLG, 58 % PQ); color corporativo: display-light; cartel de escena (marcador): scene-light
- Oficio: fijas HDR con CICP; degradados ≥10 bits

## 7. Entrega para emisión
- Estándar de entrega: ficha del receptor (imagen, códec, tasa, contenedor, pistas, sonoridad, TC). No consta ficha de RTVA/CSRTV
- ST 377-1 vigente 2019-11-28. AMWA AS-11: MXF restringidos para entregar a broadcaster; origen UK DPP; Nordic, Australia y Nueva Zelanda, NABA; UHD y HDR; formato corto
- EBU Quality Control (01-09-2015): plantilla por destino: Automated QC, File Package Compliance (AS11 DPP), Manual QC, File Structure Analysis
- qc.ebu.io (CC-BY 4.0): 0051B Video Signal Levels; 0010B Loudness; 0021B Flashing Video (epilepsia); 0044B Video Freeze; 0078B Audio Silence; 0026F Timecode; 0082W Audio/Video Duration Match; 0119B Slate Details; 0248B Missing Captions/Subtitles; 0001F AFD. Cierre: firma («sign-off»)
- EBU R 128 (noviembre 2023): −23.0 LUFS; ±1.0 LU si no practicable (directo); True Peak máx. −1 dBTP en producción, menor según distribución
- Entrega (oficio): pieza cerrada; con transparencia (ProRes 4444, TGA, PNG, EXR); fija (PNG o TIF con alfa); plantilla (relleno-llave; tema 9)
- Comprobar: aspecto; cadencia y barrido; códec con alfa, 10 bits; R 103; alfa sin halos; zonas seguras; vectorscopio; HDR 75 % HLG o 58 % PQ y versión SDR; 0021B; R 128; ficha

## Lo que este tema no da
- Formato, códec, ficha, UHD, HDR de CSRTV: no consta. No leídas: RP 2046-2, BT.1379, IEC 61966-2-1, DCI, DNxHR
- Otros temas: 2, 5, 6, 9, 10, 13
