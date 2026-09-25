# Puesto 30 · Tema 4 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`.

## Fuentes releídas y fecha

Todas leídas el 25-09-2026, en los `.txt` ya guardados, sólo en el pasaje citado:

| Fuente | Qué se releyó |
|---|---|
| UIT-R BT.601-7 (03/2011, texto en español) | Cometido («entrelazada»), 4:3 y 16:9, punto 6 (720 y 360 muestras por línea activa digital) |
| UIT-R BT.709-6 (06/2015) | Introducción de la parte 2: cadencias y 1/1.001, P/PsF/I y tabla de combinaciones (50/P, 25/P, 25/PsF, 50/I «25 interlace») |
| UIT-R BT.2020-2 (10/2015) | Tabla 1 (16:9, 3 840 × 2 160, 7 680 × 4 320) y su nota 1; párrafo de la elección de cadencia; tabla 2 (cadencias, «Progressive»); «10 or 12 bits per component» |
| UIT-R BT.2100-3 (02/2025) | «recommends» y NOTE de PQ/HLG; tabla 1 (tres formatos, 1:1, cadencias, «Progressive», nota 1b); tabla 8 (4:4:4, 4:2:2, 4:2:0); párrafo narrow/full; tabla 9 (64/256, 940/3 760, 0 y 1 023) |
| Informe UIT-R BT.2408-9 (03/2026) | § 2.1 (HDR Reference White, Graphics White), tabla 1 (26/38/38; 203/58/75), § 5.1 (direct-mapping, up-mapping, display-/scene-referred, «no universal approach»), § 5.1.x (escalado a 203 cd/m²), § 5.2 (down-mapping), § 7.1.3 («round-trip») |
| SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023 y fichas de catálogo | Velocidades, BNC 75 Ω e IEC 61169-8, pérdidas 20-30/30/40 dB; «stabilized» (259, 292-1, 424) y «active» (2082-1) |
| SMPTE ST 2110-10:2022, -20:2022, -30:2025; índice de la familia; ficha de catálogo de la -10 | Introducción y cl. 1 de la -10, apartado 8.5 y frase de ST 2022-7; cl. 1 y 7.4-7.6 de la -20 (muestreo, profundidad, colorimetría, ALPHA, TCS); cl. 1 y 6 de la -30 (48 kHz; 44,1/96 kHz); títulos de las partes -10 a -43 |
| Catálogo SMPTE: ST 2084, ST 2086, ST 377-1, ST 2067-2 | Títulos, fechas (2014-08-16; 2014-10-13 y 2018-04-09; 2019-11-28; 2013, 2016, 2020-04-07) y estado |
| SMPTE, página IMF; AMWA, página AS-11 | Todas las citas de § 12 (IMF, CPL, OPL, RDD 59-1; AS-11 y sus ampliaciones) |
| EBU R 128-2023 | Recomendaciones h), l) y m) y fecha (noviembre de 2023) |
| EBU Tech 3285 v2.0 | Campos de «bext», UMID (v1) y sonoridad (v2), MPEG (tabla de contenedores del § 9) |
| Library of Congress, fdd000389 | Cita de G. Adcock (VBR) |

## Lo copiado: sólo literalidad

Script de comparación (párrafos, filas y viñetas del tema buscados en los temas de origen
normalizados; en RTVE, sin negritas y sin mayúsculas de énfasis):

- **Copiado del común** (08-07, 28-09, 28-15): todos los pasajes listados aparecen literales. Las dos
  frases que el informe de redacción declaró cambiadas («El tema 2 explica qué se nota en la imagen»;
  «Los defectos que produce son bloques, contornos sucios y detalle que «hierve» (oficio)») se
  comprobaron: el tema 2 trata muestreo y bits. Sin cambios.
- Añadido no declarado dentro de «H.264 y H.265»: «Que H.264 no es sinónimo de GOP largo lo muestra
  el AVC-Intra (más abajo).» Se verificó contra el pasaje copiado del AVC-Intra: correcto.
- **Copiado de RTVE sin cambios** (edicion-montaje/04, realizacion-tv/12, ing-tec-teleco/07):
  tabla de muestreos, frase del 4:4:4:4, «50i no son 50 cuadros…», cadena mnemotécnica, tabla NDF/DF
  y el párrafo del malentendido, tabla de los cinco ejes, tabla de garantías del coaxial: literales.
  No se re-verifican. Las frases añadidas tras el párrafo del *drop frame* («A 25 fps se usa, por
  tanto, código NDF»; remisión al tema 2) se verificaron.
- Lo adaptado y lo nuevo se verificó entero.

## Hallazgos y correcciones aplicadas

| Nº | Error (de los nueve) | Pasaje | Qué decía | Fuente | Corrección |
|---|---|---|---|---|---|
| 1 | 9 afirmación sin fuente (y falsa) | § 4 «El HD: la BT.709» | «Y es la única de las recomendaciones actuales que conserva el entrelazado» | BT.601-7, Cometido: imagen de televisión digital **«entrelazada»**; la BT.601 está vigente | «Y, a diferencia de la BT.2020 y la BT.2100, conserva el entrelazado (la BT.601 de la definición estándar también es «entrelazada»)» |
| 2 | 6 salvedad omitida | § 5 «Cómo se señala el HDR» | «If the TCS value is not specified, receivers shall assume the value SDR» | ST 2110-20:2022, 7.6: sigue «unless the sampling keyword indicates the signal is a KEY signal, in which case the TCS value is not meaningful» | Cita completada |
| 3 | 6 salvedad omitida | § 12 «La sonoridad de entrega» | −1 dBTP «during production» sin más | R 128-2023, m): «during production (linear audio)» y «Permitted Maximum True Peak Levels may be lower for different distribution systems and data reduction rates.» | Añadidas literales; fila de R 128 de la tabla de normas ajustada |
| 4 | 6 salvedad omitida (cita cortada) | § 2 «Resolución y relación de aspecto» | Cita de la BT.2020-2 cerrada en «1.5 metres or more» | BT.2020-2, nota 1 al cuadro 1: la frase sigue «and for large screen (LSDI) presentations in theatres, halls and other venues such as sports venues or theme parks.» | Cita completada, con la sigla explicada |
| 5 | 9 (literalidad de la cita) | § 5 «Mezclar SDR y HDR» | «'round-trip'» | BT.2408-9, § 7.1.3: «‘round-trip’» | Comillas de la fuente |
| 6 | 9 (literalidad de la cita) | § 12 «IMF» | «("Core Constraints")» | Página SMPTE de IMF: «(“Core Constraints”)» | Comillas de la fuente |
| 7 | 9 (precisión) | § 11, viñeta de la ST 2110-20 | «profundidad (8, 10, 12 o 16 bits)» | ST 2110-20:2022, 7.4.2: 8, 10, 12, 16 enteros y **16f** (coma flotante) | «8, 10, 12 o 16 bits enteros, o 16 en coma flotante» |
| 8 | 5 siglas sin presentar | Siglas | RDD usado (§ 12 y tabla de normas) sin presentar | Página SMPTE de IMF: «SMPTE Registered Disclosure Document» | Añadida: «documento de divulgación registrado de la SMPTE (RDD, *Registered Disclosure Document*)» |

Cada corrección se comprobó en la fuente antes de aplicarla. Se releyeron los pasajes cambiados: no
queda ningún «esa recomendación» ni «dicha norma» sin antecedente.

## Lo que se confirmó sin cambios (resumen)

- BT.601-7: 720 y 360 muestras; 4:3 y 16:9. BT.709-6: cita de cadencias y de P/PsF/I; 50/I con
  «25 interlace» y 25/PsF; no hay 1 280 × 720 en la recomendación.
- BT.2020-2: tabla 1, tabla 2, «Scan mode Progressive», párrafo de la elección de cadencia, «10 or 12
  bits per component».
- BT.2100-3: NOTE de PQ y HLG (literales), tabla 1 y nota 1b (literal), definiciones de 4:4:4, 4:2:2 y
  4:2:0, «n = 10, 12 bits per component», rango estrecho por defecto y full range «should not be used
  for programme exchange unless all parties agree», 64/940 y 256/3 760; 10000 en la ecuación PQ; fecha
  02/2025.
- BT.2408-9: todas las citas del § 5 del tema, literales; tabla 1 (26/38/38; 203/58/75); fecha 03/2026.
- SMPTE: las cuatro velocidades, BNC e IEC 61169-8, pérdidas, estados de catálogo; ST 2110-10 (tres
  citas y la de la ST 2022-7 con el 8.5, que regula la señalización de flujos duplicados); ST 2110-20
  (alcance, muestreos, colorimetrías con ALPHA «for key signals», SDR/PQ/HLG); ST 2110-30 (alcance,
  48 kHz obligatorio, 44,1 y 96 kHz recomendables); títulos del índice ST 2110; ST 2084, ST 2086,
  ST 377-1 y ST 2067-2 (títulos, fechas y estado).
- AMWA AS-11 e IMF: todas las citas literales, incluidas CPL, OPL y RDD 59-1.
- R 128: h) y l) literales; noviembre de 2023.
- Tech 3285: UMID en la versión 1, sonoridad en la versión 2, formato PCM/MPEG (fila BWF de la tabla).
- LOC fdd000389: cita de Adcock, literal.
- Cálculos rehechos: 1.920 × 1.080 × 2 × 10 × 25 = 1.036.800.000; × 50 = 2.073.600.000; UHD p50 =
  8.294.400.000; 1.037/50 ≈ 20,7; 1.037/121 ≈ 8,6; 121 × 3.600/8 = 54.450 MB; 2.074 > 1.485 (3G) y
  8.294 > 2.970 (12G a 11.880); 8.294.400 = 4 × 2.073.600; 16 × 8 × 1.000/100 = 1.280 s.
- Remisiones a los temas 2, 3, 7, 8, 11 y 12: comprobadas en los temas ya escritos (límites EBU R 103,
  SDI, audio embebido y medidores en el 2; EDL/AAF en el 3; canal alfa en el 7; suma de verificación
  en el 8).

## Lentes

Tema técnico sin norma jurídica: `refutar_prosa.py` (0 hallazgos) e `indice.py` (13.282 palabras, 61
epígrafes). No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Discrepancias con la fuente (manda la fuente)

- El texto de la BT.601-7 guardado dice «525 ó 565 líneas» en el Cometido (probable errata del texto
  o de la extracción: el sistema es de 625). El tema no da la cifra; sólo cita «entrelazada».
- La frase «de las cinco, la que menos se nota […] es la resolución» (adaptada de RTVE) no tiene
  fuente; el tema ya la marca como oficio y se deja así.

## Ficheros tocados

- Editado: el tema 04 (los pasajes de la tabla de hallazgos).
- Creado: este informe.
- Copia previa del tema en el scratchpad de la sesión. Ningún otro fichero.
