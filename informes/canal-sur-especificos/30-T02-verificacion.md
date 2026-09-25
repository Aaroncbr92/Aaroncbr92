# Puesto 30 · Tema 2 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/02-senal-de-video-y-audio.md`.

## Fuentes releídas y fecha

Todas leídas el 25-09-2026, en los `.txt` ya guardados:

| Fuente | Qué se releyó |
|---|---|
| UIT-R BT.709-6 (06/2015) | Puntos 1.2-1.4 y nota (1), 2.1-2.5, 3.1-3.3, 4.1-4.7, 5 (5.2-5.9 y nota 2), parte 2 (tabla de combinaciones), anexo 2 (nota 1, §§ 1-3) |
| UIT-R BT.2020-2 (10/2015) | Tablas 1-5, notas 2-3 al cuadro 4, párrafo de la red eléctrica |
| UIT-R BT.2100-3 (02/2025) | «recommends» y NOTE de PQ/HLG, tabla 1 y nota 1b, tabla 3 y notas 3c-3d, párrafo NCL/CI, tabla 8 (submuestreo), párrafo narrow/full, tabla 9, ecuación PQ (10000) |
| Informe UIT-R BT.2408-9 (03/2026) | §§ 2.1-2.2, tabla 1 y sus notas |
| EBU R 68-2000 | Texto completo y notas 1-2 |
| EBU R 128-2023 | Recomendaciones e) y g)-v), nota 1, definición de «Programme» |
| EBU Tech 3250, 3.ª ed., 2004 | § 1 (alcance, 48 kHz) |
| SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023 y fichas del catálogo (ST 259, 292-1, 424, 2082-1, 2084) | Velocidades, NRZI, atenuación, BNC 75 Ω, impedancia de salida, estado en el catálogo, título de la ST 2084 |

## Lo copiado: sólo literalidad

Script de comparación (párrafos, filas de tabla y viñetas del tema buscados en los temas de origen
normalizados; RTVE sin negritas). Resultado:

- **Copiado del común** (08-09 y 28-11): todos los pasajes listados aparecen literales. No se
  re-verifican.
- **Copiado de RTVE sin cambios** (R02, R03, R04): todos los pasajes listados aparecen literales. No
  se re-verifican.
- Lo que el script marca como parcial o nuevo coincide con lo que el informe de redacción declara
  como adaptado o propio: se verificó entero.

## Hallazgos y correcciones aplicadas

| Nº | Error (de los nueve) | Pasaje | Qué decía | Fuente | Corrección |
|---|---|---|---|---|---|
| 1 | 9 afirmación sin fuente (y falsa) | § 3 «El código de tiempo», adaptado de R04 | «el código de tiempo se adelanta al reloj unos tres segundos y medio por hora» | Cálculo sobre BT.709-6 5.3 (30/1.001): a 29,97 cuadros/s, en una hora real pasan 107.892 cuadros y el código de 30 en 30 marca 59:56;12; el código llega a 01:00:00:00 a los 3.603,6 s. Va **por detrás** | «se queda atrás del reloj» |
| 2 | 8 artículo mal | § 1 «El barrido» | «1 125» y «1 080» atribuidos a la tabla del punto 5 | BT.709-6: 1 125 en 5.2; 1 080 en 2.4 (no está en el punto 5) | «(punto 5.2)» y «(punto 2.4)» |
| 3 | 8 artículo mal | § 1 «El muestreo de la señal» | Cita «CB, CR sampling frequency is half…» colgada del punto 5.8 | BT.709-6: es la nota (2) del punto 5.9 | «(punto 5.9 y su nota 2)» |
| 4 | 8 (precisión) | Ídem | «co-sited… alternate Y samples» sin punto | BT.709-6, punto 4.3 | «(punto 4.3)» |
| 5 | 9 afirmación sin fuente | § 1 «El muestreo», adaptado de R04 | «La cuarta cifra… es siempre el canal alfa, y sólo puede ser 4 o 0» | Sin fuente; ni la BT.2100 ni la BT.709 definen una cuarta cifra | Quitado el absoluto: «Cuando un muestreo lleva cuarta cifra, ésa es la del canal alfa (oficio).» |
| 6 | 6 salvedad omitida | § 2 «Del sonido analógico al digital» | 16 bits como mínimo (R 68), sin su nota | R 68, nota 1: «16-bit recordings may not meet the requirements of some organizations…» | Añadida la nota 1 literal |
| 7 | 6 salvedad omitida | § 2 «La sonoridad», viñeta «Pico» | −1 dBTP sin salvedad | R 128, m): «Permitted Maximum True Peak Levels may be lower for different distribution systems and data reduction rates.» | Añadida literal |
| 8 | 4 (matiz de modo) | § 2 «La sonoridad», «Para el montador» | «pico verdadero por debajo de −1 dBTP» | R 128, m): «shall not exceed −1 dBTP» (−1 está permitido) | «sin pasar de −1 dBTP» |
| 9 | 9 (declaración) | § 1 «Las cadencias» | «que vienen de la televisión norteamericana» sin marca | Ninguna recomendación leída lo dice | Añadido «(oficio)» |
| 10 | 5 siglas sin presentar | Siglas | IP y BOJA usadas sin presentar | — | Añadidas a la lista de siglas |
| 11 | 1 cita cruzada (Trazabilidad) | Trazabilidad | BT.709 «5.1-5.8»; BT.2100 sin tablas 7 y 8; BT.2408 «§ 2.1 y tabla 1» | La nota 2 es del 5.9; CI en tabla 7, submuestreo en tabla 8; la tabla 1 está en § 2.2 | «5.1-5.9»; «tablas 1, 3, 4, 6, 7, 8, 9»; «§§ 2.1 y 2.2, tabla 1»; filas de R 68 y R 128 de la tabla de normas, con la nota 1 y la salvedad |

Cada corrección se comprobó en la fuente antes de aplicarla. Se releyeron los pasajes cambiados: no
queda ningún «ese punto» ni «dicha recomendación» sin antecedente.

## Lo que se confirmó sin cambios (resumen)

- BT.709-6: fórmula del punto 1.2 y exponente 0.45 (3.1); primarios y D65; 4.1 «R, G, B or Y, CB, CR»;
  3.2 «Derivation of luminance signal»; 4.4 (1 920/960); 4.5 «Linear 8 or 10 bits/component»; tabla
  de niveles 4.6-4.7 (16/64, 235/940, 128/512, 16 and 240/64 and 960, 1 through 254/4 through 1 019,
  0 and 255/0-3 and 1 020-1 023); 5.3-5.5 del 50/I (campo 50, 2:1, imagen 25); 5.6 (2 640); 5.8
  (148.5 y 74.25); cadencias de la parte 2; «25 interlace»; P/I/PsF; las tres citas del anexo 2 y la
  de 24 a 25 Hz; BT.1886 en la nota (1).
- BT.2020-2: tabla 1 (16:9, 7 680 × 4 320, 3 840 × 2 160); tabla 2 (cadencias, «Progressive»); red
  eléctrica; notas 2 y 3 al cuadro 4; «10 or 12 bits per component».
- BT.2100-3: NOTE de PQ y HLG; tabla 1 (tres formatos, píxel cuadrado, cadencias, «Image Format
  Progressive», nota 1b); tabla 3 (≥ 1 000, ≤ 0.005, nota 3c «small area highlights»); NCL/CI;
  submuestreo 4:4:4/4:2:2/4:2:0; rango estrecho y completo (64/256, 940/3 760; 0, 1 023/4 095) y su
  cita; «n = 10, 12 bits per component»; el 10000 de la ecuación PQ.
- BT.2408-9: cita del Graphics White, tabla 1 (26/38/38; 162/56/71; 179/57/73; 203/58/75) y sus dos
  notas.
- R 68, R 128 y Tech 3250: todas las citas, literales.
- SMPTE: las cuatro velocidades, NRZI (ST 424 y ST 259), BNC 75 Ω e IEC 61169-8, 75 ohmios de salida,
  atenuaciones 20-30/30/40 dB; catálogo: ST 259, 292-1 y 424 «stabilized», ST 2082-1 «active»; título
  de la ST 2084.
- Cálculos rehechos: 2 640 × 1 125 × 50 = 148,5 M; 74,25 × 2 × 10 = 1 485; 2 970; 11 880; 24/25 = 0,96;
  1,152 × 2 = 2,304 y × 16 = 18,4 Mb/s; 64 × 48 000 = 3,072 M; 3 600 × 30/1,001 ≈ 107 892, diferencia
  108 cuadros = 3,6 s; 48 000/25 = 1 920 y /50 = 960.
- Remisiones a los temas 4, 7 y 8: comprobadas contra el enunciado y contra los temas ya escritos
  (ST 2110 y AES67 en el 4; *ducking*, ecualización, mezcla y LUT en el 7).

## Lentes

Tema técnico sin norma jurídica: `refutar_prosa.py` (1 hallazgo, el mismo falso positivo «BC»
dentro de la cita «Y'C'BC'R» de la BT.2020) e `indice.py` (10.810 palabras, 28 epígrafes, índice
correcto). No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Discrepancias con la fuente (manda la fuente)

- El error del *drop frame* (hallazgo 1) viene de RTVE R04 § 10, que dice «se adelanta». El tema
  RTVE sigue con esa redacción; no se ha tocado (queda fuera de este encargo).
- La regla «la cuarta cifra sólo puede ser 4 o 0» viene de R04 § 3; tampoco se tocó el tema de RTVE.

## Ficheros tocados

- Editado: el tema 02 (los pasajes de la tabla de hallazgos).
- Creado: este informe.
- Ningún otro.
