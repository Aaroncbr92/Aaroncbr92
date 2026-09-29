# Realizador/a (puesto 33) · Tema 14 · Fase 2, redacción

Fecha de trabajo: 24-09-2026 (encargo); fuentes leídas el 29-09-2026 (fecha del sistema). Tema:
`temas/canal-sur-especificos/33-realizador-a/14-formatos-video-resolucion-compresion-hdr-codecs-entregables.md`
(19.547 palabras según `indice.py`, 74 epígrafes; índice generado con `indice.py`).

Enunciado: «Formatos de vídeo, resolución, compresión, HD, UHD, HDR, códecs, archivos y entregables.»
Epígrafes en ese orden: 1 Formatos de vídeo · 2 Resolución · 3 Compresión · 4 HD y UHD · 5 HDR ·
6 Códecs · 7 Archivos · 8 Entregables · Aplicación práctica.

Redactado por partes en el scratchpad (`r33t14/p00..p10.md` para lo propio; `s01..s08.sh` para cada
epígrafe) y ensamblado con un guion que inserta los pasajes copiados por número de línea desde su
fichero de origen (`cp.py`, que registra cada inserción en `log.tsv`): lo copiado es literal por
construcción. A lo de RTVE sólo se le quitan las negritas de énfasis.

## Decisiones

- Base: el tema 4 cerrado de Operador/a Montador/a de Vídeo (30/04), que cubre casi todo el
  enunciado. Se ha dejado fuera su § 11 (SDI/IP: no lo pide este enunciado; remitido al tema 15 y al
  temario de Operador/a Montador/a) y su aplicación práctica (del montador). Numeración ajustada para
  que los «§ 1» a «§ 6» copiados sigan valiendo: 1 formatos, 2 resolución, 3 compresión, 4 HD y UHD,
  5 HDR, 6 códecs. La cadencia (30/04 § 7) va dentro del § 1; la tasa y las generaciones (30/04 §§ 8 y
  10), dentro del § 3; los contenedores (30/04 § 9), en el § 7; la entrega (30/04 § 12), en el § 8.
- Recortes de 30/04 por no ser del realizador (no son datos que el enunciado pida): el párrafo del
  MPEG HD de la Sony X400 (30/04, 221-231) y la cifra de Panasonic sobre minutos por tarjeta P2
  (786-796). La tabla de variantes de DNxHD se conserva porque de ella salen las cuentas de 121 Mb/s.
- El tema 8 del puesto (ya redactado) remite a éste «los niveles de la señal de vídeo (EBU R 103)…
  las curvas logarítmicas y el HDR»: se han copiado de 30/02 los límites de la R 103, la gamma y la
  curva logarítmica y el monitor HDR.
- De RTVE `realizacion-tv/12` no se copia nada: su *proxy*, código de tiempo, aritmética, soportes y
  RAID están ya en el tema cerrado 07 de Cámara Operador/a (08/07), con fuente de fabricante y sin
  respuestas de examen; se copia de ahí (común cerrado, no se reverifica). De RTVE `realizacion/05`
  se toman sólo pasajes técnicos sin examen (rango dinámico, relación de aspecto, redundancia y
  entropía, clasificación de códecs). Se descartan de RTVE 05, por no tener fuente (error 9): la
  tabla de códecs con años y resoluciones máximas, «el HEVC es el códec estándar de la emisión UHD en
  España» y la «mitad de tasa» del HEVC.
- Lo nuevo sobre el material reutilizado (sí se verifica): § 1, «Qué decide el realizador sobre el
  formato» (Conv. ficha 5351000; RD 1680/2011 0910 RA 4 e, RA 5 d; 0906 RA 2 c); § 2, párrafo del
  reencuadre y «Qué hace el realizador con un material de otra forma» (con el ítem 0001F de la EBU);
  § 3, croma y submuestreo, y reparto de márgenes de la R 103; § 4, «Lo que emite Canal Sur»
  (Contrato-programa, puntos 85 y 101 y parte expositiva); § 5, «El HDR en la realización»; § 7,
  introducción, uso del *proxy* por el realizador y el párrafo de los modos de código de tiempo
  (paráfrasis de las citas de la Z200 del tema 08/07, que se quitaron por largas); § 8 entero salvo
  lo copiado (RD 0905 RA 1 f, 0907 RA 5 f y h, RA 6 a-d, contenidos, 0910 RA 5 e, RA 7 a; LE
  3.17.1.5 pp. 61-62; EBU *Quality Control* 2015 y 10 ítems del catálogo; YouTube 2853702); aplicación
  práctica; cierre.
- **Discrepancia en la fuente**: el Contrato-programa dice en la parte expositiva (p. 11) que el
  RD 16/2023 «modifica el artículo 7.1» del RD 391/2019, y en el punto 101 y en la cláusula quinta,
  «artículo 7.2». El tema no da el número de artículo y no lee el RD 16/2023 (lo declara).
- LE 3.17.1.5: la cita del máster empieza en p. 61 y sigue en p. 62 (salto de página entre «(sin
  interrupciones)» y «y sólo»); `negritas.py` no la encuentra por la cabecera de página: comprobada a
  mano en el volcado, líneas 2075-2082.
- Fuentes leídas directamente el 29-09-2026: RD 1680/2011 (BOE-A-2011-19599, volcado local),
  Convenio (p. 196), Contrato-programa (pp. 11, 42, 47), LE (pp. 61-62, 81), EBU *Quality Control*
  (PDF descargado de tech.ebu.ch), catálogo QC (API de qc.ebu.io, volcado del 29-09-2026) y YouTube
  Help 2853702 (descargada de nuevo).

Lentes: `refutar_prosa.py`, 4 hallazgos: DVD sin presentar (corregido en siglas); HD, UHD y HDR en el
título, que es el enunciado literal (se presentan en las siglas de entrada; no se toca el título).
`negritas.py` contra RD 1680/2011, Convenio, Contrato-programa, LE, EBU QC, catálogo QC y YouTube: de
las negritas propias sólo falta la del LE partida por página (arriba); el resto de «no están» son
pasajes copiados del común, cuyas fuentes no se pasaron.

Ficheros tocados: el tema y este informe. Nada más.

## Copiado del común

Temas cerrados y verificados de Canal Sur, insertados por número de línea (literales al carácter). La
verificación y la refutación los saltan.

`30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`:
- 152-196 y 198-220: «Esencia, códec, contenedor…», «Qué define un formato de grabación», «Cómo se
  lee el nombre de un formato» (sin el párrafo de la X400) (§ 1).
- 679-722: «Las cadencias normalizadas», «La cadencia en el montaje», «El código de tiempo y la
  cadencia» (§ 1).
- 233-268 y 270-279: «2. Resolución», «Resolución y relación de aspecto», «Producir en alta y entregar
  en baja» (§ 2).
- 283-299, 300-319, 323-336: «Qué es un códec y qué se pierde», «El muestreo cromático», «La
  profundidad de bits» (§ 3).
- 728-731, 733-759, 761-785, 797-804: la tasa de bits, la tasa sin comprimir y la capacidad (§ 3).
- 872-874, 876-903, 905-909: «Dónde se comprime y cuánto», «Las generaciones», «Transcodificar» (§ 3).
- 340-405: «4. HD y UHD», «El HD: la BT.709», «El UHD: la BT.2020 y la BT.2100» (§ 4).
- 406-413, 417-441, 443-450, 452-466, 470-505: HDR (qué es, tabla PQ/HLG, metadatos, señalización,
  niveles, conversiones) (§ 5).
- 506-676: «6. Códecs» entero (§ 6).
- 807-846 y 850-869: contenedores de vídeo; WAV y BWF (§ 7).
- 1039-1050, 1052-1129, 1132-1143: estándar de entrega, MXF, AS-11, IMF, pistas R 123, sonoridad
  R 128 (§ 8).

`30-operador-a-montador-a-de-video/02-senal-de-video-y-audio.md`:
- 441-485: «Los límites de la señal según la EBU» (R 103 v3.0) (§ 3).
- 201-212 y 215-226: «La gamma y la curva logarítmica» (§ 5).
- 549-558: monitor HDR (BT.2100-3, tabla 3) y gama frente a rango dinámico (§ 5).

`08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`:
- 275-276, 279-286: «Los formatos de proyecto» (tabla EDL, AAF, XML) (§ 7).
- 290-306: «El *proxy*», con las citas de la Z200 (§ 7).
- 693-706, 715-716, 719-734: «El código de tiempo» (LTC/VITC, 80 bits, Free Run, DF/NDF, LE 5.3.3),
  sin la tabla de menús de la Z200 ni la viñeta Rec Run (§ 7).
- 742-758: «La aritmética del código de tiempo» (§ 7).
- 508-524: «Los soportes de estado sólido» (§ 7).
- 919-943: «Lo que no es una copia de seguridad: el RAID» y «El archivo a largo plazo: la LTO» (§ 7).

`08-camara-operador/03-captacion-eng-estudio-exteriores-um-directos.md`:
- 254-272: «Dos o más cámaras ENG» (LE 3.17.1.5, p. 61, y tabla de oficio) (§ 7).

Adaptado del común (sí se verifica: sólo el cambio indicado):
- 30/04, 197: «El tema 2 explica qué se nota en la imagen.» → «El § 3 lo desarrolla.»
- 30/04, 723: remisión al tema 2 → «…su forma y su aritmética están en el § 7.»
- 30/04, 269: «que el montador aplica» → «que se aplica».
- 30/04, 320: «(el tema 7 trata su uso)» → «tema 12»; quitada la frase de la ST 2110-20 «ALPHA» (§ 11).
- 30/04, 337-338: «están en el tema 2» → «son los del apartado siguiente».
- 30/04, 727: título «Qué es y cómo se expresa» → «La tasa de bits: qué es y cómo se expresa».
- 30/04, 732: «(§ 1)» → «(Sony, *PXW-X400 Operating Instructions*, «Specifications», p. 144)», porque
  el párrafo de la X400 del § 1 no se copia (la referencia es la que 30/04 daba en su § 1).
- 30/04, 760: «(§ 11; la diferencia es oficio)» → cita de la SMPTE ST 292-1 (**«The total data rate
  shall be either 1.485 Gb/s or 1.485/1.001 Gb/s»**, la que 30/04 daba en su § 11).
- 30/04, 875: «los §§ 6 y 8» → «del § 6 y de este epígrafe».
- 30/04, 904: «*proxies* (tema 3)» → «(§ 7)».
- 30/04, 414-416: quitada la remisión al tema 2; «cómo se nombra, cómo se señala, qué niveles usa y
  cómo se mezcla».
- 30/04, 442: «ST 2110-20 (§ 11)» → «(tema 15)».
- 30/04, 451: título «Los niveles que el montador necesita» → «Los niveles del HDR».
- 30/04, 467-468: quitada la frase «La tabla completa… está en el tema 2».
- 30/04, 1051: «citada en el § 9» → «§ 7».
- 30/04, 1130-1131: «Para el montador (oficio)» → «En la sala de montaje (oficio)».
- 30/04, 1144: remisiones a los temas 2 y 7 → «La mezcla y la revisión final, en el tema 13.»
- 30/02, 213-214: quitado «(véase «La colorimetría de referencia»)».
- 30/02, 227-228: «se ven en «El alto rango dinámico»» → «son las de este epígrafe».
- 30/02, 486-488: «Para el montador la frase que manda» → «Para la pieza montada la frase que manda».
- 08/07, 277-278: «al cámara le llegan cuando el material que graba se monta» → «al realizador le
  importan cuando su programa se monta».
- 08/07, 287-288: «(véase «Metadatos»)» → «(véase «El código de tiempo»)».
- 08/07, 307-308: quitado «(véase «Ingesta»)».
- 08/07, 944-945: quitado «no los decide el cámara».

## Copiado de RTVE sin cambios

Sólo quitadas las negritas de énfasis. Insertado por número de línea. El verificador comprueba sólo
que es literal.

`temas/realizacion/05-la-tecnologia-en-la-realizacion.md`:
- 310-317: definición del rango dinámico y «Un mayor rango dinámico…» (§ 5, «Qué es y qué
  recomendación lo fija»).
- 393-401: definición de la relación de aspecto y «Ni la distancia focal…» (§ 2).
- 404-410: tabla de relaciones (4:3, 16:9, 1,85:1, 2,39:1) (§ 2).
- 413-419: *letterboxing* y *pillarboxing* (§ 2).
- 436-442: «Comprimir es quitar lo que sobra»: redundancia y entropía (§ 3).
- 449-457: «Las cuatro maneras de clasificar un códec» y su tabla (§ 3).
- 458-461: intraframe e interframe (§ 3).

Adaptado de RTVE (sí se verifica): 05, 411: «Es aritmética, y esa pregunta se responde dividiendo.»
→ «Es aritmética.» Línea propia de enlace antes de la tabla: «Las relaciones más usadas, escritas de
las dos formas:» (RTVE decía «Las relaciones que el examen maneja…»).

De `temas/realizacion-tv/12-formatos-y-procesos-de-registro.md`: nada (véase «Decisiones»).

## Diez preguntas tipo test (comprobación de cobertura)

Repartidas por las rúbricas del enunciado; contestadas sólo con el tema.

1. (Formatos) Cuando se habla de MXF se habla de: a) Un códec sin pérdida. b) Un contenedor. c) Un
   códec con pérdida y canal alfa. d) Un formato de proyecto como el AAF. — b) · Entera: § 7, «Los
   contenedores de vídeo» («El MXF es un contenedor, no un códec») y § 1, tabla de esencia, códec,
   contenedor y proyecto.
2. (Resolución) El UHD o 4K de televisión es: a) 4.096 × 2.160, 17:9. b) 3.840 × 2.160, 16:9. c)
   7.680 × 4.800, 16:9. d) 5.120 × 4.096. — b) · Entera: § 2, tabla; § 1, la aclaración del 4K DCI con
   la cuenta 1,777 y 1,896.
3. (Compresión, práctica) ¿Cuántos minutos caben, aproximadamente, en una tarjeta de 128 GB con un
   formato de 200 Mb/s? a) 34. b) 64. c) 85. d) 128. — c) · Entera: § 3, «La tasa y la capacidad»
   (1.024.000 ÷ 200 = 5.120 s).
4. (HD) 1080i50 significa: a) 50 cuadros progresivos. b) 50 campos por segundo, 25 cuadros
   entrelazados. c) 25 cuadros transportados en segmentos. d) 50 cuadros entrelazados. — b) · Entera:
   § 4, «El HD: la BT.709» («50i no son 50 cuadros, son 50 campos y 25 cuadros»).
5. (UHD, casa) Según el Contrato-programa 2024-2026, desde el 14 de febrero de 2024 la TDT de Canal
   Sur emite: a) En UHD 4K. b) En HD como único sistema. c) En SD y HD simultáneamente. d) En HD y
   UHD. — b) · Entera: § 4, «Lo que emite Canal Sur» (punto 85; UHD sólo como cooperación).
6. (HDR) En una producción HLG, el blanco de un rótulo va al: a) 100 %. b) 75 %. c) 58 %. d) 38 %. —
   b) · Entera: § 5, «Los niveles del HDR» (203 cd/m², 75 % HLG, 58 % PQ).
7. (HDR, práctica) En un directo HDR con alguna cámara SDR, la conversión que el Informe BT.2408
   describe para igualar cámaras es: a) Por luz de pantalla. b) Por luz de escena. c) Expansión sin
   más. d) Ninguna: no se pueden mezclar. — b) · Entera: § 5, «Mezclar SDR y HDR» (cita de
   *scene-referred mapping*) y «El HDR en la realización».
8. (Códecs) ¿Cuál de estos formatos es intracuadro? a) XAVC S Long. b) AVC-Intra 100. c) XAVC HS. d)
   XAVC Long. — b) · Entera: § 6, «AVC-Intra (Panasonic)» y tabla de XAVC (Long y HS son GOP largo).
9. (Archivos, práctica) Un vídeo a 25 fps empieza en 00:47:17:23 y termina en 01:23:54:00; su
   duración por resta pura es: a) 00:35:36:01. b) 00:36:36:02. c) 00:36:42:01. d) 00:35:35:00. — b) ·
   Entera: § 7, «La aritmética del código de tiempo» (y 00:36:36:03 si se cuenta inclusiva).
10. (Entregables) Según el RD 1680/2011, las señales de la realización televisiva que se determinan
    para grabar son: a) Sólo el máster. b) Máster, señal sin incrustaciones y cámaras dobladas o
    masterizadas. c) Máster y previo. d) Programa y auxiliares. — b) · Entera: § 8, «Qué se graba en un
    directo» (0905, RA 1, f), con tabla de para qué sirve cada una).

Resultado: las 10 enteras; no hizo falta ampliar el tema.
