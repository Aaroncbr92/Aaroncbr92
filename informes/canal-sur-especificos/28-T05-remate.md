# Puesto 28 · Operador/a de Sonido · Tema 5 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/05-procesamiento-de-audio.md`.
Entrada: `28-T05-refutacion.md` (3 menores, 2 lagunas, 2 a medias) y `28-T05-preguntas.md`.
Fecha de trabajo y de lectura de fuentes: 25-09-2026 («hoy» del encargo: 24-09-2026).

**Resultado: se amplió contenido nuevo** (dos lagunas cerradas y una a medias resuelta, con tres
RaneNotes nuevas). Procede la fase 5 bis sobre los pasajes listados abajo.

## Fuentes releídas o leídas por primera vez

| Fuente | Cómo | Fecha |
|---|---|---|
| Rane, RaneNote 155 (Jeffs, Holden, Bohn, 2005) | Texto de ranecommercial.com/legacy/note155.html ya descargado en la sesión; cotejo de cada cita | 25-09-2026 |
| Rane, RaneNote 160, «Linkwitz-Riley Crossovers: A Primer» (Bohn, octubre de 2005) | ranecommercial.com/legacy/note160.html, descargada y pasada a texto | 25-09-2026 |
| Rane, RaneNote 101, «Constant-Q Graphic Equalizers» (Bohn; 1982 y 1987, rev. 11/2005) | ranecommercial.com/legacy/note101.html | 25-09-2026 |
| Rane, RaneNote 122, «Operator Adjustable Equalizers: An Overview» (Bohn) | ranecommercial.com/legacy/note122.html | 25-09-2026 |

## Correcciones de la refutación, comprobadas en la fuente

1. **Menor 1 (VCA el más rápido)**: ninguna fuente leída compara la velocidad de las tecnologías.
   Aplicada la segunda vía de la refutación: se mantiene la frase (es la respuesta de la pregunta
   tipo test del redactor y de la tabla copiada de RTVE sin cambios) y se marca expresamente como
   oficio, con lo único que Rane dice: **«VCAs dominate»** en analógico. La velocidad de las
   tecnologías pasa a «Lo que este tema no da».
2. **Menor 2 (ataque de compresores y voz)**: confirmado en RN155, literal: «Attack times for
   compressors generally range between 25 ms and 500 ms» y la tabla «Suggested Compressor
   Settings» («Vocals 25 ms to 100 ms 100 ms to 500 ms 2:1 to 4:1 Soft»). Aplicada; hueco corregido.
3. **Menor 3 (salvedad de la relajación)**: confirmado en RN155, literal, con la fórmula y el
   ejemplo (5 dB, mando a 1 s → 0,5 s). Aplicada.

## Lagunas

1. **Ataque de compresores (pregunta 5)**: cerrada con el menor 2. Ahora «entera».
2. **Pendiente por orden (pregunta 12)**: confirmada en RN160: «each order, or degree, of a filter
   increases the slopes by 6 dB/octave or 20 dB/decade» y el ejemplo de cuarto orden (24 dB/octava,
   80 dB/década). 12 dB/octava para segundo orden y 18 para tercero son cálculo de la regla (RN160
   nombra además el Butterworth de 18 dB/octava). Ahora «entera».
3. **A medias, pregunta 13 (bandas del gráfico de tercio)**: RN122 da el gráfico de realce y corte
   **«with 10 to 31 bands on octave to 1/3-octave spacing»**; RN101, que dominan los de **«30 band
   1/3-octave»**. Añadidas las dos. Aviso: la fuente no respalda «31» como número único del gráfico
   de tercio (RN101 dice 30); la pregunta no se recorta, pero su clave c) debe leerse con esa
   salvedad (el tema da 31 como tope y 30 como grupo dominante).
4. **A medias, pregunta 15 (codo para voz)**: resuelta con el menor 2 («Soft»). Ahora «entera».

## Pasajes cambiados

| Lugar | Cambio |
|---|---|
| Ficha, «Fuente» | Añadidas RN160, RN101 y RN122; «compresor» en la lista de RN155 |
| Ficha, «Extensión» | 7.950 → 8.530 palabras (`indice.py`: 8.527) |
| Siglas de entrada | Añadida ISO |
| «Qué se puede preguntar» | Márgenes de ataque y relajación del fabricante; pendiente por orden |
| «Los tipos de ecualizador», párrafo del gráfico | Bandas según RN122 y RN101 |
| «Qué hace un compresor y sus mandos», párrafo de Rane | Ataque de compresores 25-500 ms; nuevo párrafo con la salvedad de la relajación, fórmula y ejemplo |
| «Las tecnologías de compresor», frase del VCA | Marcada como oficio; «VCAs dominate» |
| «La compresión en la práctica», entrada y primer punto | Puntos de partida de Rane para voz; el primer punto remite a ese margen |
| «Los filtros de corte», párrafo de la pendiente | Regla de 6 dB/octava por orden y valores de 1.º a 4.º orden |
| «Lo que este tema no da» | Quitado el hueco de la pendiente; el de compresores reescrito (otras fuentes que no son voz; velocidad de las tecnologías) |
| «Trazabilidad» | Fila de RN155 ampliada; filas nuevas de RN160, RN101 y RN122; en el oficio, quitada la pendiente y acotada la compresión de la voz |

Relectura de los pasajes cambiados: «ese margen» remite a la relajación de la frase anterior;
«ver «Los parámetros de la puerta»» existe y da 0-250 ms; «la regla» y «Rane» tienen antecedente.

## Lentes

- `indice.py`: 8.527 palabras, 40 epígrafes, índice sin cambios (el tema no está en
  `portadas.tsv`; la extensión de la ficha se puso a mano).
- `refutar_prosa.py`: 0 hallazgos.
- Tema técnico sin norma legal: no aplican `negritas.py`, `refutar_exactitud.py` ni
  `refutar_modo.py`. Cotejo por script de cada cita nueva en negrita contra el texto de RN155,
  RN160, RN101 y RN122: todas son subcadena literal.

## Otros ficheros tocados

Sólo el tema 5 y este informe.
