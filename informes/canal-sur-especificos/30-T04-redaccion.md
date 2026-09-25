# Puesto 30 · Tema 4 · Redacción (fase 2)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Se escribe según avanza.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`.
Material: `30-investigacion-A-tecnica.md` (§§ 2.1-2.3 y 4); tema cerrado 08-07 (Cámara); temas
cerrados del puesto 28 (09 y 15); RTVE `edicion-montaje/04` y `05`, `realizacion-tv/12`,
`ing-tec-teleco/07` (`informes/canal-sur-reuso/realizacion.tsv`: 85 %, «actualizar: no»).

## Avance
- Portada, siglas, enunciado, preguntas, índice y § 1: guardado.
- §§ 2 Resolución, 3 Compresión: el principio, 4 HD y UHD: guardado.
- §§ 5 HDR y 6 Códecs: guardado.
- §§ 7 Frame rate, 8 Bitrate, 9 Contenedores, 10 Compresión en la cadena: guardado.
- §§ 11 SDI/IP, 12 Estándares de entrega, aplicación práctica, normas, lo que no da y trazabilidad: guardado.
- Siglas completadas tras `refutar_prosa.py` (0 hallazgos) e `indice.py` (61 epígrafes, ~13.100 palabras).

Extensión: unas 13.300 palabras (el enunciado tiene doce rúbricas; algo más de un tercio es texto
copiado de temas cerrados).

## Estructura
§ 1 Qué es un formato · § 2 Resolución · § 3 Compresión: el principio (códec, muestreo, profundidad) ·
§ 4 HD y UHD · § 5 HDR (curvas, ST 2084/2086, señalización, niveles BT.2408, conversiones SDR-HDR) ·
§ 6 Códecs (vídeo y audio) · § 7 Frame rate (cadencias, montaje, DF/NDF) · § 8 Bitrate (CBR/VBR, tasa sin
comprimir, capacidad) · § 9 Contenedores (MXF, WAV/BWF) · § 10 Compresión en la cadena (generaciones,
transcodificación: la segunda «compresión» del enunciado) · § 11 SDI/IP · § 12 Estándares de entrega
(MXF, AS-11, IMF, R 128) · aplicación práctica · normas · lo que no da · trazabilidad.

Reparto con el tema 2 (sugerencia de la investigación, aviso 4): colorimetría, curvas en detalle,
límites EBU, SDI por dentro, audio embebido y R 128 en profundidad quedan en el tema 2; aquí SDI por
velocidades y formatos, HDR como formato y entrega. Hay solapes breves (velocidades SDI, tabla BT.2408
reducida) con las mismas citas que el tema 2.

## Copiado del común
(Temas ya cerrados de Canal Sur; no se re-verifican.)

Del tema 7 de Cámara Operador (`08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`):
- «Esencia, códec, contenedor, metadatos y proyecto» (líneas 156-169), literal.
- «Qué define un formato de grabación» (173-199), literal salvo la última frase: «El tema 9 explica
  qué se nota en la imagen» → «El tema 2 explica qué se nota en la imagen» (remisión al tema de este
  puesto). **El verificador debe mirar sólo esa frase.**
- «Cómo se lee el nombre de un formato» (203-233), literal.
- «Qué es un códec y qué se pierde», párrafos 1-2 (347-355) y 3 (358-360), literal salvo el final del
  párrafo 2: «(bloques, contornos sucios, detalle que «hierve») y cómo el operador los evita están en
  el tema 9» → «son bloques, contornos sucios y detalle que «hierve» (oficio)». **Verificar esa frase.**
- «Intracuadro y GOP largo» (364-385), «H.264 y H.265» (389-400), «XAVC (Sony)» (404-422), «Apple
  ProRes» (426-444), «Avid DNxHD (SMPTE VC-3)» (448-476), «AVC-Intra (Panasonic)» (480-487), «Cuadro
  resumen» (491-499): literales.
- «La tasa y la capacidad» (312-341), literal.
- «Los contenedores» (237-273), literal.

Del tema 9 de Operador/a de Sonido (`28-operador-a-de-sonido/09-grabacion-edicion-y-postproduccion.md`):
- Códecs de audio con y sin pérdida (226-244), literal salvo la frase final suprimida («Por qué tras un
  códec con pérdida hace falta un techo de pico más bajo se explica en el tema 13»: remisión a otro
  puesto).
- «El fichero de entrega de audio: el BWF», primer párrafo (951-959), literal.

Del tema 15 de Operador/a de Sonido (`28-operador-a-de-sonido/15-audio-sobre-ip-...md`):
- «Qué es el PTP», primer párrafo (549-556), literal.
- «La redundancia sin cortes de la SMPTE: ST 2022-7», párrafo y viñetas (685-699), literal.

## Copiado de RTVE sin cambios
(Pasajes técnicos de temas RTVE marcados «actualizar: no» en `realizacion.tsv`; palabras sin tocar,
sólo se quitan las negritas de énfasis de RTVE —en Canal Sur la negrita marca cita literal— y, en la
tabla de realizacion-tv/12, las mayúsculas de énfasis. Comprobado por script: cada pasaje está en la
fuente RTVE y en el tema.)
- `edicion-montaje/04`, § 3: tabla de muestreos 4:4:4, 4:2:2, 4:2:0, 4:1:1 (con «Dónde se usa»); frase
  «Y una cuarta cifra puede aparecer. Un archivo de vídeo con muestreo cromático 4:4:4:4 significa que
  tiene una señal de vídeo RGB sin submuestreo de color más información del canal alfa.»
- `edicion-montaje/04`, § 4: «50i no son 50 cuadros, son 50 campos y 25 cuadros. Si fueran cuadros la
  notación sería 1080p50.»
- `edicion-montaje/04`, § 5: «La cadena mnemotécnica: 601 estándar · 709 alta · 2020 ultra alta · 2100
  alto rango dinámico.»
- `edicion-montaje/04`, § 10: tabla NDF/DF y el párrafo «El malentendido más común… lo que cambia es la
  etiqueta.»
- `realizacion-tv/12`, § 2: tabla de los cinco ejes del UHD.
- `ing-tec-teleco/07`, § 1: tabla «Garantía que el coaxial daba sola / Cómo se recupera en la red».

## Adaptado de RTVE (sí se verifica)
- `edicion-montaje/04` § 1, primera frase (resolución y relación de aspecto) con «el examen puede
  preguntar»; «Lo que UHD multiplica es el número de píxeles, no la forma de la pantalla».
- `edicion-montaje/04` § 3, párrafo del canal alfa: literal hasta «sin recortarlo a mano»; se quita la
  referencia al anexo de RTVE y se añade la remisión al tema 7 y el valor «ALPHA» de la ST 2110-20.
- `edicion-montaje/04` § 5: tabla de recomendaciones rehecha (BT.709 SDR, BT.2020 con gama amplia,
  BT.2100 HDR en HD y UHD).
- `edicion-montaje/04` § 8: «para editar, intracuadro; para distribuir, intercuadro».
- `realizacion-tv/12` § 2: «no es sólo más píxeles» y la idea de lo que se percibe (puntuación
  cambiada); se añade qué recomendación sostiene cada eje.
- `ing-tec-teleco/07` § 2: tabla SDI frente a ST 2110, sin la marca ✔ de respuesta de examen; § 4:
  redes roja y azul «convenio de instalación, no de norma».
- Quitado de RTVE por propio de RTVE o sin fuente: respuestas oficiales y opciones falsas; la «fase 1»
  de UHD; SMPTE 274M/296M (plantilla); «H.265 ahorra hasta un 50 %» (plantilla, sin fuente); JPEG 2000
  como códec del cine digital y DNxHR intracuadro (no leídos); la tabla de partes de ST 2022 (no leída)
  y las cifras «1,5 Gb/s» de ing-tec-teleco/07 (sustituidas por cálculo sobre la ST 292-1).

## Escrito nuevo (se verifica entero)
§ 2 (BT.601-7, BT.2100-3 tabla 1 y nota 1b, BT.2020-2 nota de aplicación); § 3 muestreo (BT.2100-3) y
profundidad y rangos (BT.2020-2, BT.2100-3 tabla 9); § 4 (BT.709-6: cadencias, P/PsF/I, sistemas 50/I
y 25/PsF; BT.2020-2 tabla 2; BT.2100-3); § 5 entero (BT.2100-3, catálogo ST 2084/2086, ST 2110-20 cl.
7.5-7.6, BT.2408-9 §§ 2, 5.1, 5.2 y 7.1.3); § 7 (BT.2020-2 elección de cadencia); § 8 (LOC fdd000389,
cita de G. Adcock; cálculos); § 10; § 11 (SMPTE ST 259, 292-1, 424, 2082-1 y catálogo; índice ST 2110;
ST 2110-10 intro y cl. 1; ST 2110-20 cl. 1 y 7.4-7.6; ST 2110-30 cl. 1 y 6); § 12 (catálogo ST 377-1 y
ST 2067-2; AMWA AS-11; SMPTE IMF; EBU R 128-2023 h, l, m); aplicación práctica.

## Fuentes y fecha de lectura
Todas releídas en su pasaje citado el 25-09-2026: `fuentes/canal-sur/montador/itu/` (bt709, bt2020,
bt2100, bt2408), `fuentes/normas-tecnicas/UIT-R_BT.601-7.txt`, `fuentes/canal-sur/montador/smpte/`
(ST 259, 292-1, 424, 2082-1 y catálogos), `fuentes/normas-tecnicas/SMPTE_ST-2110-10-2022.txt`,
`SMPTE_ST-2110-20-2022.txt`, `SMPTE_ST-2110-30-2025.txt`, `SMPTE-ST-2110-indice.md` (índice volcado el
02-09-2026), `fuentes/canal-sur/montador/ebu/r128.txt`, `fuentes/canal-sur/montador/web/amwa-as11.txt` e
`imf.txt`, `fuentes/normas-tecnicas/LOC_fdd000389_ProRes422.txt`.

## Discrepancias y avisos
- BT.709-6: la investigación llama al entrelazado europeo «25 interlace»; la recomendación lo lista
  como sistema **«50/I»** con captación «25 interlace». El tema da las dos cosas.
- ST 377-1: el tema cerrado de Cámara (vía LOC) nombra la edición de 2011; el catálogo SMPTE da la de
  2019-11-28 como vigente. El tema lo dice en el § 12; el pasaje copiado de Cámara se deja literal.
- RTVE ing-tec-teleco/07 declaraba no haber leído ninguna ST 2110; aquí se leen la -10, -20 y -30.
- No consta ficha técnica de entrega de RTVA/CSRTV: va a «Lo que este tema no da».

Ficheros tocados: el tema 04 (nuevo) y este informe. Borradores en el scratchpad de la sesión.

## Diez preguntas tipo test (comprobación antes de entregar)

Contestadas sólo con el tema: E = entera.

1. (Contenedores / entrega) Las especificaciones AMWA AS-11 definen ficheros de entrega basados en:
   a) MOV · b) MXF · c) IMF · d) MP4. → b (§ 12: «constrained media file formats (based on MXF)»). E
2. (Resolución / UHD) Resolución del UHD de televisión según la UIT-R BT.2020-2: a) 4.096 × 2.160 ·
   b) 3.840 × 2.160 · c) 7.680 × 4.800 · d) 2.560 × 1.440. → b (§§ 1, 2, 4). E
3. (HD / frame rate) En un 1080i50 hay: a) 50 cuadros · b) 50 campos y 25 cuadros · c) 25 campos ·
   d) 100 campos. → b (§ 4). E
4. (HDR, aplicación práctica) Nivel de señal del blanco de un rótulo en una pieza HLG según el Informe
   BT.2408: a) 100 % · b) 58 % · c) 75 % · d) 38 %. → c (§ 5). E
5. (HDR) Norma SMPTE que publica la curva PQ: a) ST 2086 · b) ST 2084 · c) ST 2110-20 · d) ST 377-1.
   → b (§ 5). E
6. (Códecs / compresión) Es códec sólo intracuadro: a) XAVC S Long · b) XAVC HS · c) MPEG HD422 · d)
   ProRes 422. → d (§ 6: «intrafame (I-frame) only»; XAVC S/HS Long y MPEG-2 Long GOP). E
7. (UHD / frame rate) En la BT.2100-3 el barrido admitido es: a) sólo progresivo · b) progresivo y
   entrelazado · c) sólo PsF · d) entrelazado a 50 Hz. → a (§§ 4, 7). E
8. (Bitrate, aplicación práctica) Tarjeta de 128 GB con un formato de 200 Mb/s, cuenta nominal: a) 34 min
   · b) 85 min · c) 170 min · d) 21 min. → b (§ 8, pasaje copiado de Cámara). E
9. (Compresión en la cadena, práctica) Un clip H.264 a 8 Mb/s transcodificado a ProRes 422 HQ: a) recupera
   la calidad original · b) pesa más y no recupera nada de lo perdido · c) pierde el código de tiempo ·
   d) pasa a 4:4:4. → b (§ 10, regla 3). E
10. (SDI/IP) Señale la correcta: a) la ST 2110-20 transporta vídeo comprimido · b) un 1080p50 cabe en un
    HD-SDI de 1,485 Gb/s · c) la ST 2110 lleva vídeo, audio y datos en flujos separados, alineados por
    un reloj común · d) el 12G-SDI va a 2,970 Gb/s. → c (§ 11). E

Rúbricas cubiertas: resolución (2), compresión (6, 9), HD (3), UHD (2, 7), HDR (4, 5), códecs (6),
frame rate (3, 7), bitrate (8), contenedores (1), SDI/IP (10), entrega (1). La sonoridad de entrega
(R 128: −23,0 LUFS ±1,0 LU, −1 dBTP) también está en el § 12. Las diez, enteras: no hizo falta ampliar.
