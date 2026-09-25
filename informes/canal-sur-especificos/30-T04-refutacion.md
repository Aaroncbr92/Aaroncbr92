# Puesto 30 · Tema 4 · Refutación (fase 4, segunda pasada)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`
(14.291 palabras, 62 epígrafes), en su estado tras el remate y la revisión 5 bis. No se corrige
nada: sólo se informa. La primera refutación (anterior al remate: 1 grave, 4 menores, 1 laguna, todo
aplicado según `30-T04-remate.md` y `30-T04-final.md`) queda en el historial de git (commit b08a902).

Exactitud: se saltan «Copiado del común» y «Copiado de RTVE sin cambios» (lista en
`30-T04-redaccion.md`). Cobertura: el tema entero.

## Fuentes releídas (25-09-2026, sólo el pasaje)

- UIT-R BT.2100-3: cabecera (02/2025), tabla 1 (cadencias, «Progressive»), valor 10000 de la EOTF PQ.
- Informe UIT-R BT.2408-9: cabecera (03/2026).
- UIT-R BT.601-7: «entrelazada» (lín. 112).
- SMPTE ST 2110-20:2022, 7.4.1-7.4.2 (muestreo, KEY, «ALPHA»; profundidades 8, 10, 12, 16, 16f).
- SMPTE ST 2110-30:2025, lín. 154 (48 kHz obligatorio; 44,1 o 96 kHz recomendables).
- SMPTE ST 2110-10:2022, 8.5 (señalización de flujos duplicados).
- EBU R 123: §§ 1-2 (lín. 63-74), tabla 1 (8a, 8b), clave, notas generales, notas 1, 2, 3 y 5,
  anexo 2.3.1 (definición SMPTE del sonido internacional).
- EBU Tech 3343-2023: § 4.2 (lín. 730-735), § 7.1 (lín. 923).
- EBU R 128-2023: fecha y apartados h), l) y m).
- AMWA AS-11 (ampliaciones) y página IMF de la SMPTE (RDD 59-1, DPP y NABA, BT.2100).

## Hallazgos

| Nº | Gravedad | Error (de los nueve) | Pasaje | Qué dice el tema | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|---|
| 1 | Menor | 3 recuento / 9 | § 8, «La tasa sin comprimir y la relación de compresión», último párrafo | «un DNxHD a 121 Mb/s en 1080i/50, unas 8,5 veces (cálculo, sobre las tasas de § 6)» | Cálculo: la tasa sin comprimir de referencia (1.037 Mb/s) es de 10 bits, y el DNxHD de 121 Mb/s en 1080i/50 es la 120, de 8 bits (sucesora a 25 de la 145, que el § 6 da como 8 bits). Comparado con 10 bits da 8,57 («unas 8,6», no 8,5); con la profundidad propia, 1.920 × 1.080 × 2 × 8 × 25 = 829 Mb/s ÷ 121 ≈ 6,9 | «un DNxHD de 8 bits a 121 Mb/s en 1080i/50, unas 7 veces (829 ÷ 121; la imagen de 8 bits sin comprimir son unos 829 Mb/s)» |

Todo lo demás del texto adaptado y nuevo que se releyó se confirmó: fechas de BT.2100-3 y BT.2408-9;
cadencias y barrido de la BT.2100-3 iguales a las de la BT.2020-2; 10.000 cd/m² en la EOTF PQ;
profundidades de la ST 2110-20 (8, 10, 12 y 16 enteros; 16f); KEY sin TCS y con «ALPHA»; 48 kHz
obligatorio en la ST 2110-30; ST 2110-10, 8.5; citas de la R 123 (inequívoca, 16 canales, salvedad
del acuerdo previo, 48 kHz/24 bits, «clearly indicated», notas 1, 2 y 5 y «compatability» [sic]),
pistas de 8a y 8b; Tech 3343 (LFE fuera de la medida, 5.0, Lo/Ro); R 128 h), l), m) y su salvedad;
AS-11 y RDD 59-1. Cálculos rehechos: 1.037, 2.074 y 8.294 Mb/s; 20,7; 85 y 34 min; 1.280 s;
54.450 MB; unos 5 cuadros de cada 30 al pasar de 29,97 a 25. Los antecedentes de «esa pérdida
típica», «la misma recomendación», «En las dos» y «nota 1» están delante.

## Cobertura del enunciado

Las doce rúbricas tienen epígrafe propio en el orden del enunciado (la segunda «compresión», como
compresión en la cadena, § 10). La laguna de la primera pasada (configuraciones de canales y orden
de pistas) está cubierta por el nuevo epígrafe «Las pistas de audio: configuraciones y orden (EBU
R 123)». «Qué se puede preguntar» no promete nada que el tema no dé.

Preguntas (`30-T04-preguntas.md`): 13 enteras, 1 a medias, 1 no.

- Pregunta 15 (a medias): consecuencia del hallazgo 1, no laguna.
- Pregunta 14 (no): HDR10/HDR10+/Dolby Vision están declarados en «Lo que este tema no da» por falta
  de fuente normativa leída. Hueco declarado; no se cuenta como laguna. Si en el remate se lee una
  fuente publicada (p. ej. la ficha de la ST 2086 completa o una especificación de plataforma), podría
  ampliarse; si no, se deja como está.

Lagunas: ninguna.

## Lentes

Tema técnico sin norma jurídica: `refutar_prosa.py` (0 hallazgos) e `indice.py` (14.291 palabras,
62 epígrafes), ejecutados el 25-09-2026 sobre el tema actual.

## Resumen

Graves: 0 · Menores: 1 · Lagunas: 0.

Ficheros tocados: reescritos `30-T04-preguntas.md` y este informe (la versión anterior de ambos está
en git). El tema no se ha modificado.
