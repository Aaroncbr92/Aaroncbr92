# Puesto 28 · Operador/a de Sonido · Tema 5 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/05-procesamiento-de-audio.md`.
Fecha de trabajo y de lectura de fuentes: 25-09-2026 («hoy» del encargo: 24-09-2026). No se
corrige el tema.

## Fuentes releídas

| Fuente | Cómo | Fecha |
|---|---|---|
| Rane, RaneNote 155 (Jeffs, Holden, Bohn, 2005) | Texto de la página original, bajado por el verificador al directorio de trabajo de la sesión | 25-09-2026 |
| EBU R 128-2023 (V5) | `fuentes/normas-tecnicas/EBU_R128-2023.txt` | 25-09-2026 |
| EBU Tech 3343-2023 (V4) y EBU R 68-2000 | `fuentes/normas-tecnicas/` (sólo cotejo de citas) | 25-09-2026 |

Exentos de la lente de exactitud: lo listado como «Copiado del común» y «Copiado de RTVE sin
cambios» en `28-T05-redaccion.md` (la verificación ya comprobó que es literal).

## Lente 1 · Exactitud

Cotejo por script de todas las citas en negrita entre comillas: todas casan con Rane, R 128 o
Tech 3343, salvo las tres de R 68/Tech 3343 del común (artefactos de PDF, ya vistos a mano en
verificación). Cálculos rehechos: Q por N octavas; campana 707-1.414 Hz; 4:1 → −17 dBFS / 9 dB;
2:1 → −14 dBFS / 6 dB. Contexto de cada cifra de Rane comprobado (umbral −40/+20 dBu de
compresores; −60 dBu de expansores; ataque 0-250 ms «For expanders (with ducking & gate
features)»; *hold* 0-3 s; profundidad 0/−80 dB; ejemplo del expansor: escalón −10 dB → −20 dB,
mejora de 10 dB). Correctos.

### Graves

Ninguno.

### Menores (3)

1. **Superlativo sin fuente (error 9)**, «Las tecnologías de compresor», l. 343 (adaptado de
   RTVE, no exento): «De las cuatro, la de respuesta más rápida es el VCA». Ninguna fuente leída
   compara tecnologías (Rane sólo dice que en analógico «VCAs dominate»), y es un dato
   directamente preguntable en test. La verificación lo dejó como oficio, pero el tema lo
   afirma en seco, sin la etiqueta de oficio junto al dato (la nota de l. 352 habla de
   «clasificación» y «caracteres sonoros», no de la velocidad). Remate: buscar fuente de
   fabricante o manual; si no aparece, quitar el superlativo o marcarlo expresamente como oficio.
2. **Hueco mal declarado y oficio que sí tiene fuente (error 9 inverso)**, «Lo que este tema no
   da», l. 729-732, y «La compresión en la práctica», l. 369: el tema dice que los márgenes de
   compresor «más allá de los de Rane (relaciones, ataques)» no se han leído en fuente, y da la
   compresión de voz como oficio. Rane sí los da: **«Attack times for compressors generally range
   between 25 ms and 500 ms»**, y su tabla «Suggested Compressor Settings»: «Vocals 25 ms to 100 ms
   [ataque] 100 ms to 500 ms [relajación] 2:1 to 4:1 [relación] Soft [codo]». Remate (Opus, amplía):
   añadir el ataque de compresores junto a la relajación (l. 304-306) y apoyar en Rane la
   compresión de voz; corregir el hueco.
3. **Salvedad omitida (error 6)**, «Qué hace un compresor y sus mandos», l. 304-306 y tabla
   l. 299: el tema presenta la relajación como «cuánto tarda en soltar» y cita el margen de Rane
   de 25 ms a 2 s como si fuera ese tiempo. Rane advierte que es el valor del mando, que no hay
   norma común y que él lo define como el tiempo de un cambio de 10 dB: **«There is no industry
   standard and different manufacturers define this control differently. Rane defines this
   control, in a compressor for example, as how long it takes for the gain to change by 10 dB,
   not how long it takes to return to unity gain»**, con la fórmula «Release Time = (Gain
   Reduction x Release Setting) / 10 dB». Remate: añadir la salvedad en una frase (y, si cabe,
   el ejemplo de Rane: 5 dB con mando a 1 s → 0,5 s).

## Lente 2 · Cobertura del enunciado

Las ocho materias del enunciado (ecualización, dinámica, compresión, limitación, puertas,
filtros, reverberación y efectos) tienen rúbrica propia y en su orden. Preguntas en
`28-T05-preguntas.md`: **entera 11 · a medias 2 · no 2**.

### Lagunas (2) · se amplía el tema

1. **Ataque de compresores** (pregunta 5, «no»): el dato está en Rane y el tema no lo da; se
   cierra con el menor 2.
2. **Pendiente de los filtros por orden** (pregunta 12, «no»): 6 dB/octava por orden es una
   pregunta de test esperable en «Filtros»; el tema lo declara hueco. Remate (Opus): buscarlo en
   fuente técnica (manual universitario o nota de fabricante; Rane tiene notas de filtros) y
   añadirlo con la cita; si no se confirma, se queda como hueco declarado.

### A medias (2, no obligan)

- Pregunta 13: número de bandas de un gráfico de tercio de octava (típicamente 31); sólo con
  fuente.
- Pregunta 15: codo blando para voz; se resuelve con el menor 2.

## Lentes automáticas

Tema técnico sin norma legal: no aplican `negritas.py`, `refutar_exactitud.py` ni
`refutar_modo.py`. El cotejo de citas se hizo por script contra las fuentes técnicas.

## Otros ficheros tocados

`informes/canal-sur-especificos/28-T05-preguntas.md` (nuevo) y este informe. Ningún tema.
