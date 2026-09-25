# Puesto 30 · Tema 2 · Refutación (fase 4)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/02-senal-de-video-y-audio.md`
(961 líneas, 28 epígrafes). No se corrige nada: se informa.

## Alcance

- Exactitud: todo lo que no figura como «Copiado del común» ni «Copiado de RTVE sin cambios» en
  `30-T02-redaccion.md`. Lo adaptado de RTVE y lo propio, contra la fuente.
- Cobertura: el tema entero contra el enunciado («Conocimientos y fundamentos de la señal de vídeo y
  audio»). Preguntas en `30-T02-preguntas.md`.

## Fuentes releídas (todas el 25-09-2026)

| Fuente | Qué se cotejó |
|---|---|
| UIT-R BT.709-6 (txt) | Introducción de la parte 2 (cadencias, P/I/PsF, «25 interlace»); 1.2-1.4 y nota (1); 2.1-2.5; 3.1-3.3; 4.1-4.7 y nota (1); 5.2-5.9 y nota (2); parte 6 (sincronismo de tres niveles); anexo 2 (nota 1, §§ 1-2) |
| UIT-R BT.2020-2 (txt) | Notas (2) y (3) al cuadro 4; tabla 2 (cadencias, «Progressive»); red eléctrica; «10 or 12 bits per component»; 16:9 y formatos |
| UIT-R BT.2100-3 (txt) | «recommends» y NOTE PQ/HLG; tabla 1 y nota 1b; tabla 3 y notas 3c-3d; párrafo NCL/CI; tabla 7 (submuestreo); párrafo narrow/full; tabla 9 |
| Informe UIT-R BT.2408-9 (txt) | § 2.2, cita del Graphics White, tabla 1 y notas (1)-(2); fecha 03/2026 |
| EBU R 68-2000 (txt) | Texto completo, notas 1 y 2 |
| EBU R 128-2023 (txt) | Recomendaciones g)-v), nota 1, definición de «Programme» |
| EBU Tech 3250 (txt de `sonido/`) | § 1 (alcance y 48 kHz) |
| SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023 y catálogo (ST 259, 292-1, 424, 2082-1, 2084) | Velocidades, BNC 75 Ω / IEC 61169-8, 75 ohmios, NRZI, atenuaciones, estado, título ST 2084; ST 292-1 tabla 3 (*jitter*) |

## Exactitud

Confirmado sin reparos: coeficientes y fórmula de transferencia (1.2, 0.45 en 3.1), «R, G, B or Y,
CB, CR» (4.1), 1 125 (5.2) y 1 080 (2.4), 50/I (campo 50, 2:1, imagen 25), todas las citas de P/I/PsF
y del paso de 24 a 25 Hz, cadencias de la BT.709 y la BT.2020 (y la de la BT.2100, igual), 148.5 y
74.25 (5.8) con su reparto por sistemas, nota (2) del 5.9, 1 920/960 (4.4), «co-sited…» (4.3; el
original lleva la llamada «alternate(1)»), 2 640 (5.6), tabla de niveles 4.6-4.7, «Linear 8 or 10
bits/component», las citas de la BT.2020 sobre CL/NCL, de la BT.2100 (NCL/CI, 4:4:4/4:2:2/4:2:0,
narrow/full con 64/256, 940/3 760, 1 023/4 095, «n = 10, 12», nota 1b, PQ y HLG, 1 000 y 0.005 con la
nota 3c), la tabla y las notas de la BT.2408-9, las citas de la R 68, de la R 128 y de la Tech 3250,
las velocidades y las citas de las cuatro SMPTE (el BNC «as defined in IEC 61169-8» está en la ST
292-1, 8.2.1, como dice el tema), el estado en el catálogo y el título de la ST 2084. Cálculos
rehechos (148,5 M; 1 485/2 970/11 880; 1,152 y 2,304 Mb/s; 3,072 M; 107 892 y 108 cuadros = 3,6 s,
con el código **por detrás** del reloj; 1 920 y 960 muestras por cuadro; 0,96): cuadran.

Hallazgos:

| Nº | Gravedad | Error (de los nueve) | Pasaje | Qué dice | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|---|
| 1 | Menor | 6 salvedad omitida | § 2 «La sonoridad: EBU R 128» | Da el objetivo −23,0 LUFS y la tolerancia ±1,0 LU de h), y el −1 dBTP de m), sin más tolerancias ni excepciones | R 128-2023, i): «**a tolerance of ±0.2 LU is allowed in order to take account of measurement errors**» (control de calidad); j): el objetivo puede normalizarse «**lower than −23.0 LUFS on purpose**», indicándolo claramente; m): «**The measurement tolerance is ±0.3 dB**» | Añadir i), j) y la tolerancia de medida de m), literales. Hace fallar la pregunta 13 |
| 2 | Menor | 4 modo («se hace» por «should») | § 2 «Del sonido analógico al digital», párrafo «Lo que tiene norma leída…» | «los 16 bits como mínimo, la EBU R 68: las grabaciones se hacen «with linear coding…»» | La frase es un considerando, no la parte dispositiva: «**It is of the opinion that recordings should be made with linear coding using no pre-emphasis and with a resolution of at least 16 bits…**»; lo que la R 68 «recommends» es el nivel de alineación | «La EBU, en la R 68, es de la opinión de que las grabaciones deben hacerse…», con la cita |

Sin hallazgos en lo demás. Observación sin propuesta: el «Para el montador» de la R 128 aplica el
−23 LUFS a una promoción; es correcto (la promo es programa por definición), y el propio tema avisa
de que la R 128 s1, a la que remite q) para las piezas cortas, no se ha leído.

## Cobertura

El tema recorre vídeo (color, colorimetría, luminancia y CL/NCL, gamma y log, compuesto/componentes,
barrido y PsF, cadencias, resolución, muestreo, cuantificación y niveles, límites EBU, HDR, medida,
SDI), audio (cualidades, digitalización, niveles, sonoridad, AES/EBU, embebido) y vídeo con audio
(código de tiempo, sincronía). Preguntas: **12 enteras, 1 a medias, 2 no**.

Lagunas:

| Nº | Qué falta | Pregunta | Fuente ya disponible | Propuesta |
|---|---|---|---|---|
| L1 | La referencia de sincronismo de vídeo: la señal de tres niveles (*tri-level*) de la HD y para qué sirve (enganchar los equipos a una referencia común). El tema sólo habla del reloj del audio embebido | 11 (no) | BT.709-6, parte 6: «**The tri level sync signal may be used as a reference signal for synchronization of devices operating on this Recommendation.**» y su tabla | Un párrafo en § 1 (tras «Medir la señal» o en «La interfaz digital serie») con la cita y sus parámetros leídos; *genlock* y *black burst*, sólo si se encuentran en fuente, si no, como oficio declarado |
| L2 | El *jitter* se explica sin su medida: unidad (UI) y los dos tipos que especifica la ST 292-1 (temporización, 1 UI; alineación, 0,2 UI) | 10 (a medias) | ST 292-1:2018, 8.1.8 y tabla 3 | Una frase y una fila de tabla en «La interfaz digital serie (SDI)» |

La pregunta 13 (no) se resuelve con el hallazgo 1.

## Lentes

Tema técnico sin norma jurídica: no se pasan `negritas.py`, `refutar_exactitud.py` ni
`refutar_modo.py`. No se han vuelto a pasar `refutar_prosa.py` ni `indice.py` (ya pasadas en fases 2 y
3, sin cambios posteriores del tema).

## Resumen

- Graves: 0.
- Menores: 2 (salvedades de la R 128; modo de la R 68).
- Lagunas: 2 (sincronismo *tri-level*; medida del *jitter*).
- El remate amplía (L1 y L2): procede la fase 5 bis sobre los pasajes nuevos.

## Ficheros tocados

- Creados: `informes/canal-sur-especificos/30-T02-preguntas.md` y este informe.
- El tema no se ha tocado. Ningún otro.
