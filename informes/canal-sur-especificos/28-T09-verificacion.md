# Puesto 28 · Operador/a de Sonido · Tema 9 · Fase 3, verificación

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema verificado:
`temas/canal-sur-especificos/28-operador-a-de-sonido/09-grabacion-edicion-y-postproduccion.md`.
Ficheros tocados: el tema y este informe. Fuentes descargadas en el scratchpad (`t09v/`).

## Fuentes releídas (todas el 25-09-2026)

| Fuente | Cómo |
|---|---|
| EBU R 128 s1 V3 (agosto 2020) | Descargada de tech.ebu.ch (`r128s1.pdf`, 4 págs.), leída entera |
| EBU Tech 3343-2023 | `fuentes/normas-tecnicas/EBU_Tech3343-2023.txt`, §§ 2.3, 2.4, 3.1, 3.2 |
| EBU Tech 3285 v2.0 (mayo 2011) | `fuentes/archivos/EBU_Tech3285_BWF.txt`: resumen, § 1, 1.1, campos de «bext» |
| EBU R 128-2023, R 68-2000 | Volcados de `fuentes/normas-tecnicas/` (nota del LRA < 1 min, punto p, alineación −18 dBFS) |
| AES TD1008.1.21-9 | Descargado de aes.org, tabla 1, notas, «Speech vs. Music», archivo a −24 LUFS |
| iZotope RX 11, Spectral De-noise | Página del manual descargada; índice de módulos |
| J. O. Smith, *Mathematics of the DFT*, CCRMA Stanford, «Sampling Theorem» | Nueva, para el teorema del muestreo |

## Copiado del común y de RTVE sin cambios: sólo literalidad

Script (normaliza espacios, quita `**` y ✔) contra `produccion/11`, `sonido/08`, `sonido/09`,
Cámara T07 y Redactor/a T08: los 14 pasajes RTVE y los 3 del común son subcadena literal de su
origen. Las frases de enlace no listadas (p. ej. «Cada códec con pérdida tiene su terreno:», «La
fórmula, por tanto: …») se trataron como nuevas y se verificaron. No se re-verificó el contenido
de lo copiado.

## Correcciones aplicadas

| # | Error | Pasaje | Qué se cambió |
|---|---|---|---|
| 1 | 1 cita cruzada / 9 | Grabación: «Las dos reglas… desarrolladas en el tema 1» | El tema 1 sólo da los 6 dB por bit; el teorema del muestreo no está en ningún tema del puesto. Se sostiene ahora con J. O. Smith (Stanford) y se cita en la trazabilidad y la ficha |
| 2 | 3 recuento | Caso del programa de 30 min + cuatro pistas mono | «el total se duplica» → se triplica (518,4 + 1.036,8 ≈ 1.555 MB) |
| 3 | 3 / 9 | «ocupa exactamente lo que dicen sus tres números» | Contradecía «más la cabecera» del caso de la cuña: «sin contar la cabecera» |
| 4 | 3 | Segundo caso de corrección de sonoridad | «tiene que rebajar al menos 0,8 dB» era falso: basta 0,5 dB (−2,3 → −1,0 dBTP); 0,8 queda como margen |
| 5 | 6 salvedad | AES, música 2-3 LU sobre la voz | Añadido «if operationally workable» y el motivo (la voz se percibe 2-3 dB más fuerte) |
| 6 | 6 salvedad | R 128 s1 b) y d) | Las tolerancias son para flujos de trabajo/control de calidad y errores de medida |
| 7 | 6 salvedad | R 128 s1 g) | −1 dBTP «for linear audio» (remisión a Tech 3344); ±0,3 dB para banda limitada a 20 kHz |
| 8 | 9 negrita no literal | AES «Interstitial: -18 / +0.2» | No es texto del documento sino una fila de tabla: pasa a redonda, con la palabra «Interstitial» en negrita |
| 9 | 6 / 9 | Tech 3343 § 2.4, glosa | «se aparta… y sólo queda un limitador» → *bypass* **o** sólo limitador de pico verdadero |
| 10 | 9 | «Canal Sur no tiene publicado un libro de estilo de radio» | El común (Redactor/a) dice «no se ha localizado»: se dice así |
| 11 | 9 | «el error de concepto más común» | Superlativo sin fuente: «un error de concepto que hay que evitar» |
| 12 | 9 negrita no literal | Tech 3285, «TimeReference: These…» y «CodingHistory: [...] Each…» | Los dos puntos no están en la fuente: el nombre del campo sale de la cita |
| 13 | 9 / 6 | «Un BWF es un WAV —el audio va en PCM, sin comprimir—» | La Tech 3285 admite también MPEG (bloque propio): «de ordinario en PCM»; MPEG presentada |
| 14 | 9 negrita | Versión 2 de la Tech 3285 | La cita omitía la llamada «[2]»: «EBU R 128 [...]» |
| 15 | 3 | «El valor de sonoridad va multiplicado por 100» | Los cinco campos de sonoridad van ×100 según la especificación |
| 16 | 4 podrá/deberá | AES, archivar a −24 LUFS | No «recomienda»: dice que las producciones «can be future-proofed»; y «a sonoridad de emisión o por debajo» era inexacto (−24 < −23): «a −24 LUFS o menos» |
| 17 | 6 salvedad | Tech 3343 ±0,2 LU | Añadido el motivo (suma de tolerancias de medida) y que dentro de tolerancia no se corrige |
| 18 | 8 apartado mal | Trazabilidad Tech 3343 | «§ 3.1 mezclar de oído» → § 2.3 y recuadro de la p. 10; § 3.1 tolerancia y medidores fuera de línea |
| 19 | — | Trazabilidad | Fecha: fuentes releídas en su texto original el 25-09-2026. Extensión de la ficha: 10.500 |

## Confirmado sin cambios

R 128 s1: motivo, fin, definición de *short-form content* y de programa («audio-only»), c), f),
LRA no aplicable, 3 s, versiones 2014/2016/2020 (la cita de la V2 y la V3 es literal de la ficha
de revisiones: aviso del redactor resuelto). R 128-2023: LRA desaconsejado por debajo de 1 min;
metadatos que digan la verdad. R 68: alineación 18 dB bajo el máximo. Tech 3343: § 2.4 literal,
«only by ear» literal, ±1 LU en directo. Tech 3285: definición, base WAVE, versiones 0/1/2,
compatibilidad, campos; «hasta 256» y «hasta 32» caracteres constan literales («maximum 256
characters», «maximum 32 characters»: aviso resuelto). TD1008: definición de *Interstitial
Content*, −18/+0,2. iZotope: las nueve citas literales y los nueve módulos. Cálculos rehechos:
tamaños, latencias a 44,1 y 48 kHz, cuña que no pasa, deriva 0,36 s/9 cuadros, 1.920/2.000/1.600/960
muestras, 40 ms, 1.728.000.000 muestras, −2300, 8.640.000 B, primera corrección. Remisiones a los
temas 4, 5, 6, 7, 8, 13 y 15 comprobadas por grep.

## Lentes

Tema técnico sin norma legal: `refutar_prosa.py` 0 hallazgos (tras presentar MPEG); `indice.py`
10.498 palabras, 58 epígrafes.

## Queda para refutación

La tabla de términos de continuidad sigue como vocabulario de oficio sin fuente (declarado en el
tema). No se leyó ninguna norma SMPTE del código de tiempo (declarado).
