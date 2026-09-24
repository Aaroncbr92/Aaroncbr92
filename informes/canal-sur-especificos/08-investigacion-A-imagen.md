# Investigación · Cámara Operador (08) · bloque A-imagen (temas 1, 2, 5, 9, 15)

Fase 1. Fecha de trabajo y de lectura de todas las fuentes: **24-09-2026** (salvo que se diga otra).
Sólo lo que falta sobre lo reutilizable de RTVE (informacion-grafica/03, 04, 08, 10, 01, 07, 02, 05;
realizacion/06, 08; realizacion-tv/12, 13, 14). Cita literal entre comillas; en inglés tal cual la fuente.

## Fuentes leídas (24-09-2026)

- EBU R 103 v3.0, *Video Signal Tolerance in Digital Television Systems*, Ginebra, mayo 2020. https://tech.ebu.ch/docs/r/r103.pdf
- EBU R 118 v2, *Tiering of Cameras for use in Television Production*, Ginebra, abril 2017. https://tech.ebu.ch/docs/r/r118.pdf
- EBU Tech 3335, *Methods of measuring the imaging performance of television cameras for the purposes of characterisation and setting*, Ginebra, agosto 2014. https://tech.ebu.ch/docs/tech/tech3335.pdf

---

## Tema 9 · Calidad técnica de imagen (lo que falta: norma de niveles, clasificación de cámaras, medida de ruido, sensibilidad, latitud, aliasing, obturador)

### 9.1 Niveles de señal legales · EBU R 103 v3.0 (mayo 2020)

- Recomendación: «the RGB components and the corresponding Luminance (Y) signal should not normally exceed the "Preferred Minimum/Maximum" range of digital sample levels in Table 1» (R 103, Annex 1).
- Tabla 1 (valores de código), literal:

| Bits | Nominal Video Range | Preferred Min./Max. | Total Video Signal Range |
|---|---|---|---|
| 8-bit | 16 - 235 | 5 - 246 | 1 - 254 |
| 10-bit | 64 - 940 | 20 - 984 | 4 - 1019 |
| 12-bit | 256 - 3760 | 80 - 3936 | 16 - 4079 |
| 16-bit | 4096 - 60160 | 1280 - 62976 | 256 - 65279 |

- Fuera de gama: «Any signals outside the "Preferred Minimum/Maximum" range are described as having a gamut error (or as being out-of-gamut). Signals shall not exceed the "Total Video Signal Range", overshoots that attempt to "exceed" these values may clip.»
- Aviso: «measuring equipment should indicate an "Out-of-Gamut" occurrence only after the error exceeds 1% of the image».
- Para cámara en directo: «Care should be taken with live productions, especially those with uncontrolled lighting, to prevent clipping of highlights during temporary excursions to extremes of code values, i.e. camera clippers should be set to Preferred Range limits (as per this document). For pre-produced and colour graded material, the nominal limits contained in this document should be followed closely.»
- Cada primaria «should lie between 0 and 100% of the narrow video range between black level and the nominal peak level (R and G and B)».
- Rango «extended»: «not formally defined but is sometimes used for the range 64 – 1019 (10-bit), so including super-whites, whilst maintaining sub-blacks».
- Legalizadores: «colour gamut "legalisers" should be used with caution as they may create artefacts in the picture that are more disturbing than the gamut errors they are attempting to correct».
- Por qué se recorta mal: el recorte «can cause harmonic distortion and alias artefacts in the video signal, which manifests as compression artefacts and the potential for increased data rates».
- Analógico: «In analogue video the normal range corresponds to 0 mV to 700 mV luminance amplitude» (Annex 2). Denominaciones: «"Video Range", "Limited Range", "SMPTE Range" or "Narrow Range"» frente a «"Full Range"».
- Negros: «clipping of sub-blacks prevents the alignment of monitors with the PLUGE signal» (Annex 2).
- NOTA para el redactor: los porcentajes −1 %/103 % que circulan en manuales como «norma EBU» no aparecen en R 103 v3.0; la versión vigente se expresa en valores de código. No usar porcentajes atribuyéndolos a R 103.

### 9.2 Clasificación de cámaras por calidad · EBU R 118 v2 (abril 2017)

- Objeto: «a practical approach be taken to the grading, or Tiering of cameras according to their technical specifications and their measured quality based on the results of tests that are specified in EBU Tech 3335». Finalidad: «Knowing which quality Tier a camera corresponds to will enable its targeting to programme genres and applications [...] and, in the case of News, to balance speed of delivery against quality.»
- Supuesto: «these guidelines assume Standard Dynamic Range production. The broadcaster must be consulted if High Dynamic Range (as described in ITU-R BT.2100) images are required».
- Cinco criterios (más el códec): «Codec [...] Noise · Sensitivity · Exposure Range · Spatial Resolution · Spatial Alias artefacts»; «Apart from spatial aliasing, each factor can be measured using the procedures of EBU Tech 3335.» (Recuento: la lista literal tiene seis viñetas contando el códec; el texto dice «five areas», el códec «does not apply to system cameras unless on-board recording in used».)
- Niveles (§ 1.2), literal: UHD2 Tier 1 (7680 x 4320), UHD2 Tier 2 (≥ 5430 x 3054), UHD1 Tier 1 (3840 x 2160), UHD1 Tier 2 (≥ 2715 x 1527), «Tier SP: Specialist or special effects cameras (broadcaster approval required before use)», «HD Tier 1: Shoulder mounted or handheld single or 3 sensor professional cameras», «HD Tier 2L: (Long-form) professional cameras», «HD Tier 2J: (Journalism) professional cameras», «HD Tier 3: Small, high quality semi-professional for production use», «HD Tier 4: Small consumer HD cameras (broadcaster approval required before use)».
- Tamaño de sensor recomendado (tabla 2): HD Tier 1 «1 x 2/3”» (un sensor) o «3 x 1/2"»; HD Tier 2L «1 x 1/2"» o «3 x 1/3”»; HD Tier 2J «1 x 1/3”» o «3 x 1/4"»; UHD1 Tier 1 «1 x 1”» o «3 x 2/3”». HD Tier 1: «10-bit», «4:2:2». HD Tier 2L/2J: «8-bit (10-bit preferred)».
- 2J: «a relaxation of some of the criteria to take account of the balance between speed to air and quality that News programmes may have to make».
- Tier 3: «Broadcasters will usually limit the amount of Tier 3 material allowed in an HD programme to around 33%».
- Tier SP: «specialist or special effects cameras including very high frame rate camera, minicams, macro cameras etc.» (útil para T15: cámaras de alta velocidad y minicámaras).
- Advertencia sobre el códec: «Although a camera can meet the requirements of a Tier, it may be let down (or even be downgraded by the on-board codec.»
- Categorías de códec (§ 1.3.1): RAW, «Intra Frame (I-Frame). I-Frame codecs do not employ temporal compression, meaning each frame is processed alone», «Inter Frame (Long GoP). Long GoP codecs offer most bit rate reduction for a given quality by looking and processing across multiple frames».
- Tasas mínimas (tabla 1, 25 fps / 50 fps, Mbit/s): Intra HD 2L y superior 100 / 200; Intra HD 2J e inferior 50 / 75; H.264 (AVC) HD 2L y superior (GoP variable) 25 / 35; H.264 HD 2J e inferior (GoP variable) «15/12» / 25; MPEG-2 «Not to be used» en UHD. Nota: «The bit rates given are the MINIMUM for general-purpose 10-bit Standard Dynamic Range content». (La tabla es compleja; si el redactor la usa, que la copie sólo en las filas HD Intra y H.264 comprobadas aquí.)
- Relación señal/ruido (tabla 6): HD Tier 1 «Better than -48 dB @ 0db gain»; HD Tier 2L «Better than -44 dB»; HD Tier 2J y Tier 3 «Better than -40 dB». «Noise should be rated by its impact and visibility as well as by measurement.» Y: «Some camera menus allow negative gain settings (with respect to the published 0 dB). It is therefore possible to improve the S/N ratio using a negative (lower) gain setting.»
- Sensibilidad (§ 3.1.2): «Measure the exposure lens aperture, at 2000-lux illumination level and 0 dB gain (or the recommended nominal gain setting), at which the white side of a Kodak Gray card produces peak white signal level (100%).» «the exposure figure should match the manufacturer’s specification (normally taken for a white card with 89.9% reflectance)». Explica el dato de catálogo «F11 a 2000 lx» (el valor concreto de cada cámara, en su ficha; no se ha comprobado ninguna aquí).
- Por qué UHD es menos sensible: «for a given sensor size, the pixels of a HDTV camera are much smaller than those of a SDTV camera and similarly the pixels of a UHDTV camera are smaller than an HDTV camera».
- Latitud (§ 3.1.3): «It is limited at the low end by noise levels, and at the high end by the clipping level.»
- Resolución (§ 3.1.4): «The sensor pixel count is not an acceptable measure of a camera’s actual resolution.»
- Aliasing (§ 3.1.5): «Aliasing is also highly distracting in a finished programme as it tends to move in the opposite direction to the movement of the camera»; «Aliasing causes motion-dependent video compression to fail in the extreme».

### 9.3 Medida de la imagen · EBU Tech 3335 (agosto 2014)

- Apartados de medida (índice): «Opto-Electronic transfer curve (Gamma)», «Noise levels and noise distribution», «Sensitivity», «Exposure range», «Colour rendering», «Infrared response», «Spatial resolution, detail settings & aliasing», «Lens/optical effects», «Temporal/shutter effects».
- Latitud: «There are two separate parameters which define the exposure range of a camera: the maximum exposure level (Lmax) [...] and the noise level which defines the minimum exposure level (Lmin)»; margen sobre blanco: «This ‘headroom’ varies in cameras between about 1 stop and 3 stops.»
- Cámaras Log: si no se alcanza el 100 %, se busca el diafragma que da «exactly 50% signal level [...] with 2000 lux illumination of a 90% grey card. This exposure level is typically 2 stops below peak exposure for a conventional gamma curve».
- Rango dinámico y ruido (§ 4.4): «A typical broadcast camera with video noise levels of about -50dB can capture about 7.5 stops, with the controls set to factory settings.» «the effective dynamic range will be reduced by about 1 stop per 6dB of video noise level increase.» «most cameras [...] can be set to capture at least 1 extra photographic stop by manipulation of the gamma curve and/or knee. In some extreme cases, cameras can capture up to 3 extra stops, and effectively handle 12 to 13 stops».
- Obturador de persiana (rolling shutter) (§ 2.9): «Cameras with CCD sensors usually exhibit no odd temporal effects, but cameras with one or more CMOS sensor can produce visible effects from the use of a ‘rolling shutter’. The effect is identical to that seen in focal plane film stills cameras; leaning verticals, distorted edges, and jelly-like images from rapid motion.» Obturación nominal: «1/50 second for 50 Hz, 1/60 for 59.94 Hz, or 180 degrees for either».
- Estilo de detalle (§ 4): «Moderate overshooting on high-contrast edges is acceptable, it is a signature of the ‘videolook’».

### 9.4 Parámetros UIT-R vigentes (ediciones comprobadas en itu.int el 24-09-2026)

- Ediciones en vigor: **BT.709-6 (06/2015)**, **BT.2020-2 (10/2015)**, **BT.2100-3 (02/2025)**. AVISO al redactor: el tema RTVE informacion-grafica/02 declara verificada la BT.2100-1; la vigente es la **-3**. Lo que se reutilice de la BT.2100 hay que citarlo por la -3 (los datos de abajo están leídos en la -3). También vigente el Informe **BT.2408-9 (03/2026)**, «Guidelines for operational practices in high dynamic range television production» (no se pudo descargar el PDF; sólo título y fecha).
- BT.709-6: primarias R (0.640, 0.330), G (0.300, 0.600), B (0.150, 0.060); blanco «D65» (0.3127, 0.3290); «Conceptual non-linear pre-correction of primary signals» γ = 0.45; imagen 1 920 × 1 080, 16:9, píxel cuadrado; «Linear 8 or 10 bits/component»; cuantificación 8 bits: negro 16, pico nominal 235, croma 16 y 240, acromático 128; 10 bits: 64, 940, 64 y 960, 512. Frecuencias: «The following picture rates are specified: 60 Hz, 50 Hz, 30 Hz, 25 Hz and 24 Hz. For the 60, 30 and 24 Hz systems, picture rates having those values divided by 1.001 are also specified.» Captura «progressive (P)» e «interlace (I)», transporte P, PsF o I. Nota de práctica: «In typical production practice the encoding function of image sources is adjusted so that the final picture has the desired look, as viewed on a reference monitor having the reference decoding function of Recommendation ITU-R BT.1886».
- BT.2020-2: primarias R (0.708, 0.292), G (0.170, 0.797), B (0.131, 0.046), blanco D65; frecuencias «120, 120/1.001, 100, 60, 60/1.001, 50, 30, 30/1.001, 25, 24, 24/1.001»; «Scan mode Progressive»; «Coding format 10 or 12 bits per component». Sobre la elección de frecuencia: «The choice of frame frequency may be influenced by the frequency of the mains power and the type of scene lighting in use» (útil para parpadeo, T5/T9).
- BT.2100-3: «the Perceptual Quantization (PQ) or Hybrid Log-Gamma (HLG) specifications described in this Recommendation should be used». «The HLG specification offers a degree of compatibility with legacy displays by more closely matching the previously established television transfer curves.» Contenedor 16:9; 7 680 × 4 320, 3 840 × 2 160, 1 920 × 1 080; «Image Format Progressive»; mismas frecuencias que BT.2020; mismas primarias que BT.2020 (tabla 2). Nota 1b: «producing in a higher resolution format, and then electronically down-sampling for distribution, yields superior quality than producing at the resolution used for distribution».
- Blanco de referencia HDR (nota 10a, BT.2100-3): «HDR Reference White is the nominal signal level obtained from an HDR camera and a 100% reflectance white card resulting in a nominal luminance of 203 cd/m2 on a PQ display or on an HLG display that has a nominal peak luminance capability of 1 000 cd/m2.»
- Monitor de referencia HDR (tabla 3): pico «≥ 1 000 cd/m2», negro «≤ 0.005 cd/m2»; en HLG el negro se ajusta con PLUGE «specified in Recommendation ITU-R BT.814».
- NO CONFIRMADO: el nivel de señal HLG del blanco de referencia en porcentaje (el «75 %» que se cita en oficio) está en el Informe BT.2408, que no se pudo leer. No afirmarlo.

### 9.5 Estabilidad: parpadeo y alta frecuencia (fabricante)

- Blackmagic, *URSA Broadcast G2 Installation and Operation Manual*, noviembre 2021: «Artificial light sources such as tungsten, fluorescent and LED may introduce some flicker to your images. You may not see these flicker issues when previewing the scene on your LCD and SDI feed or while recording, so it’s important to perform a test shoot with the lights you plan to use». «Your shutter setting can also affect the visibility of flicker when shooting under lights».

---

## Tema 1 · La cámara (lo que falta: ayudas al enfoque y a la exposición, autofoco, ND variable, sensibilidad de catálogo, clasificación de sensores)

### 1.1 Ayudas al enfoque

- Sony, *PXW-FS5/FS5K Operating Guide* (4-581-849-11(1)). Peaking: «You can display an image on the LCD screen with its outlines enhanced. This function helps you to adjust the focus.» Opciones: «COLOR [...] WHITE, RED, YELLOW»; «LEVEL You can select the peaking sensitivity. HIGH, MIDDLE, LOW». «The enhanced outlines will not be recorded on the memory card.» «You can focus more easily using this function in combination with the focus magnifier function».
- Lupa de enfoque (mismo manual): «The selected area on the LCD screen is magnified and displayed. This is useful when adjusting the focus.» «Even though the image appears expanded on the LCD screen, the recorded image is not expanded.»
- Detección de caras (mismo manual): «The camcorder detects faces and focuses on one of them (the default setting is [OFF]). You can use this function when the FOCUS (AUTO/MAN) switch A is set to “AUTO.”» Limitación: «Faces may not be detected depending on the recording environment, the condition of the subject or the settings.»
- Blackmagic URSA Broadcast G2 (manual nov. 2021): «The optimum level of focus assistance varies shot by shot. When focusing on actors, for example, a higher level of focus assistance can help resolve edge detail in faces. A shot of foliage or brickwork, on the other hand, may show distracting amounts of focus information at higher settings.» Dos modos: «‘peaking’ and ‘colored lines’». Botón por defecto: «F1 is set to toggle ‘focus zoom’».
- Canon XF605, *Instruction Manual* (PUB. DIE-0559-000B, firmware 1.0.1.1), especificaciones: «Manual focus, autofocus (AF-boosted MF, continuous AF, Face AF); face detection and subject tracking available»; «AF type: Dual Pixel CMOS AF, contrast-detection AF». Salidas de ayuda: «peaking, zebra pattern, magnification, B&W display, waveform monitor, false color».
- NO CONFIRMADO: el funcionamiento del Dual Pixel CMOS AF (dos fotodiodos por píxel, detección de fase en todo el sensor). Las páginas de Canon (canon-europe.com, usa.canon.com, snapshot.canon-asia.com) devolvieron 403 o se cargan por JavaScript; sólo se vio en resúmenes de buscador. No afirmarlo sin fuente leída; sí se puede decir que Canon distingue «Dual Pixel CMOS AF» de «contrast-detection AF» (ficha XF605).

### 1.2 Ayudas a la exposición

- Cebra (Sony FS5): «You can display a zebra pattern as a guide for adjusting brightness»; «LEVEL You can select the brightness level. 70 to 100, or 100+»; «The zebra pattern is a stripe pattern that appears in areas of brightness equal to or exceeding the brightness level you have set.» «Zebra is not recorded onto the memory card.»
- Cebra (Blackmagic): «Zebra displays diagonal lines over areas of your image that exceed a set exposure level. For example, setting zebra to 100% shows which areas are completely overexposed.» Preajustes: «middle gray and middle gray plus one stop, then in five percent increments from 75 to 100 percent exposure». «If you’re shooting in variable light such as outdoors on a partly overcast day, setting your zebra level lower than 100 can warn you of potential overexposure.»
- Falso color (Blackmagic): «False color overlays different colors onto your image that represent exposure values for different elements in your image. For example, pink represents optimum exposure for lighter skin tones, while green is a good match to darker skin tones.» «when elements in your image change from yellow to red, that means they are now over exposed.» Leyenda: «95%WC White clipping · 80%WC Near white clipping · MG+1 One stop over middle gray · 18%MG Middle gray · NBDL Near black detail loss · BDL Black detail loss». (Es la escala de ese fabricante; los colores no están normalizados.)
- Canon XF605: «ISO200 to ISO12800»; «Gain: –6 dB to 21.0 dB»; «Iris Manual (1/3-stop increments, 1/4-stop increments, fine adjustment available), push auto iris, automatic aperture»; «Shutter Speed Automatic, speed [...], angle, clear scan, slow, off»; «Exposure AE shift, light metering modes (standard, spotlight, backlight)». Sensibilidad: «(2000 lux, 89.9% reflection, [High Sensitivity Mode] set to [On]) [...] 50.00 Hz: F13 (at 50.00P)» (enlaza con el método EBU de 9.2).

### 1.3 Filtros ND y difracción

- Sony FS5: ND fijo «CLEAR: No ND filter», preajustes por defecto «1/4», «1/16», «1/64»; modo variable: «Adjust the filter density in the range 1/4 to 1/128». Difracción: «When shooting a bright subject, diffraction (a common phenomenon in video cameras, caused by closing the iris too much) may result in poor focusing. Using the ND FILTER dial A suppresses this phenomenon for better shooting images.» Aviso: «If you switch ND FILTER dial A during recording, the image or sound may become distorted.»
- Canon XF605: «ND Filter Built-in (Off,1/4, 1/16, 1/64), motor operated».
- Balance de blancos XF605: preajustes «daylight, 5,600 K» y «tungsten lamp, 3,200 K»; «color temperature setting (2,000 K to 15,000 K)»; nota: «Color temperatures are approximate and given only as a reference.»

### 1.4 Sensores y ópticas en cifras (fichas y EBU)

- Canon XF605: «Type 1.0 (1.0 in.) single-plate CMOS sensor»; «f=8.3 – 124.5 mm, F/2.8 – 4.5, 15x optical zoom, 9-bladed iris diaphragm»; «35mm equivalent focal length: approx. [...] 25.5 – 382.5 mm (other IS modes)»; estabilizador «Optical-shift image stabilizer + digital compensation (Standard IS, Dynamic IS, Powered IS)».
- Tamaños de sensor que la EBU asocia a cada nivel: ver 9.2 (2/3", 1/2", 1/3", 1/4", 1").

---

## Tema 5 · Iluminación para cámara (lo que falta: índice de consistencia TLCI y parpadeo)

- EBU Tech 3355, *Method for the assessment of the colorimetric properties of luminaires. The Television Lighting Consistency Index (TLCI-2012) and the Television Luminaire Matching Factor (TLMF-2013)*, Ginebra, marzo 2017. https://tech.ebu.ch/docs/tech/tech3355.pdf
  - «The formulation for Qa was constrained to produce a value of 50 for a typical daylight fluorescent tube, and this number appears to represent the watershed separating luminaires into those which are correctable for television use, and those which are not.»
  - «Neither the CRI nor the original work of Sproson and Taylor on the TLCI give any meaning to the computed value for Ra or Qa.»
  - Dos escalas de lectura: producción tipo cine («drama, wildlife and any production where significant post-processing is involved») y «Live multi-camera production [...] such as sport and news where pictures have no post-processing and the pictures are required only to be credible». «these opinions do not form hard definitions; there is considerable overlap».
  - NO CONFIRMADO: los umbrales por tramos de la figura 4 (p. ej. «≥ 85» o «≥ 75») están en una imagen del PDF que no se pudo leer como texto. No darlos.
- Parpadeo con LED, fluorescente y tungsteno: ver 9.5 (Blackmagic) y la frase de BT.2020-2 sobre red eléctrica e iluminación (9.4).
- Frecuencia alta y luz (Blackmagic): «if you switch from 25 to 50 frames per second, the amount of light reaching the sensor will be halved. To maintain your exposure you need to compensate for this change by opening up your lens an extra stop, by opening up your shutter angle from 180º to 360º or by adding some extra lighting».

---

## Tema 15 · Creatividad visual (lo que falta: cámara lenta, time lapse, cámaras especiales, multicámara en calidad)

### 15.1 Cámara lenta y rápida (sobre/infravelocidad)

- Blackmagic (manual nov. 2021): «let your delivery format guide your choice. Your camera’s project frame rate should be set to this, and your sensor frame should be set to match. This means your clips will play back at the same speed the event happened in real life. If you are looking to create an interesting effect, for example slow motion, then you can set the sensor frame rate to a higher setting. The higher the sensor frame rate compared to the project frame rate, the slower the playback speed.» Ejemplo: «If you record a clip with your sensor frame rate set to 60 frames per second, your clips will play back in slow motion» (con proyecto a 24). Europa: «25 frames per second for Europe»; deporte «50 frames per second in Europe». Botón HFR: «Use the HFR or high frame rate button to toggle off speed frame rates».
- Sony FS5 (Slow & Quick Motion): con sistema 50i, «1fps, 2fps, 3fps, 6fps, 12fps, 25fps, 50fps» (50 fps no en QFHD). Tabla para 2160/25p: 12 fps → «208% quick», 6 → «417% quick», 1 → «2500% quick». Super Slow Motion: «By recording with a frame rate much higher than the playback frame rate, you can record images to be played back as super slow motion images. Images recorded with the Super Slow Motion function will appear smoother than slow playback of images recorded at normal speed.» En 50i: «100 fps, 200 fps, 400 fps, 800 fps». Limitaciones: la cámara «may continue recording for some time (approximately 6 minutes at most) after you press the record button to stop recording»; «Super Slow Motion recording is not supported in XAVC QFHD»; la cebra «Cannot be displayed when Super Slow Motion mode is set».
- Canon XF605 (manual, p. 105, leído en manualslib mediante extracto automático: el verificador debe cotejar la cita): «The camera can record using a progressive frame rate (shooting frame rate) that is different from the playback frame rate.» «Sound is not recorded with the clip, but it can be recorded separately as a WAV file.» (Las cadencias concretas por formato están en tablas no confirmadas literalmente.)
- EBU R 118: las cámaras de muy alta velocidad son «Tier SP» («very high frame rate camera, minicams, macro cameras etc.»), con «restrictions on the amount used in a programmes but this content does not usually count against any percentage of lower resolution material».

### 15.2 Time lapse (grabación por intervalos)

- Canon XF605 (manual, p. 108, leído en manualslib mediante extracto automático: cotejar): modo de grabación por intervalos; se fija «Time Interval» y cuadros; «Interval recording cannot be used when the frame rate is set to 59.94i or 50.00i»; «The interval and the number of frames recorded cannot be changed while recording»; «Sound is not recorded in this mode»; incompatible con «slow & fast motion recording, pre-recording, frame recording or continuous recording»; indicadores «[INT STBY]» y «[INT REC]».
- Canon XF605 (p. 107): grabación de cuadros: «Set the number of frames in advance»; pregrabación: «the camera starts recording continuously onto a temporary memory (approx. 3 seconds)».
- NO CONFIRMADO: cálculo tipo del time lapse (intervalo × cuadros = duración); es oficio, no hay fuente leída. Se puede razonar aritméticamente en el tema diciendo que es cálculo, no norma.

### 15.3 Multicámara y homogeneidad

- EBU Tech 3355: escala del TLCI propia de «Live multi-camera production» (ver T5).
- EBU R 118: aconseja fijar el nivel de la cámara según el género; Tier 3 limitado a «around 33%» del programa HD (mezclar cámaras de distinto nivel).
- NO CONFIRMADO: procedimiento de igualación de cámaras (matching con CCU, carta de grises, pintado). Tech 3335 trae métodos de ajuste por estilo pero no se ha leído el apartado de igualación; es oficio.

---

## Tema 2 · Lenguaje visual

- Nada nuevo que investigar: RTVE cubre el 90 %. Único apoyo técnico útil de fuente: guías de marco y zona segura del visor (Sony FS5: «ASPECT [...] 4:3, 13:9, 14:9, 15:9, 1.66:1, 1.85:1, 2.35:1 Displays markers at boundaries of display area defined by the aspect ratio»; «SAFETY ZONE [...] 80%, 90%»; «CENTER [...] Displays a marker at the center of the LCD screen»).
- La nota de EBU R 118 sobre aliasing que se mueve contra la cámara (9.2) sirve para panorámicas sobre texturas finas.

---

## Lo que no se pudo confirmar (resumen)

1. Funcionamiento del Dual Pixel CMOS AF (páginas de Canon bloqueadas, 403/JS).
2. Nivel HLG del blanco de referencia en % (Informe BT.2408-9 no descargable).
3. Umbrales por tramos del TLCI (figura de Tech 3355 no legible).
4. Cadencias concretas de slow & fast del XF605 (tablas no leídas literalmente).
5. Porcentajes −1 %/103 % atribuidos a EBU R 103: no están en la v3.0 vigente.
6. Igualación multicámara con CCU: sin fuente leída; tratar como oficio.
7. Obturador global en cámaras de estudio (Sony HDC-3500 y similares): web de Sony devolvió 403.

## Fuentes de fabricante (leídas 24-09-2026)

- Sony, *PXW-FS5/FS5K Operating Guide*, 4-581-849-11(1). Copia en https://ats.emory.edu/_includes/documents/studios/manuals/Sony%20PXW%20FS5%20Manual.pdf
- Blackmagic Design, *URSA Broadcast G2 Installation and Operation Manual*, noviembre 2021. https://www.markertek.com/attachments/manuals/blackmagic/Blackmagic-URSA-Broadcast-G2-Manual.pdf
- Canon, *XF605 Instruction Manual* (PUB. DIE-0559-000B), especificaciones en https://global.canon/ja/c-museum/wp-content/uploads/2022/09/dhc898_en.pdf; pp. 105, 107, 108 en https://www.manualslib.com/manual/2427154/Canon-Xf605.html
- UIT-R BT.709-6, BT.2020-2, BT.2100-3, PDF de itu.int (dms_pubrec).
- EBU Tech 3355 (marzo 2017).
- Sin Panasonic: no se buscó; lo cubierto por Sony, Canon y Blackmagic basta para el enunciado.
