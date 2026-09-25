# Puesto 28 · Operador/a de Sonido · Tema 11 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/11-lineas-y-conexiones.md`. Fecha de trabajo y
de lectura de las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Entrada: `28-T11-refutacion.md`
y `28-T11-preguntas.md`.

**Resultado: se amplió contenido nuevo** (jack: tabla de contactos por uso, inserción, jack de 3,5 mm; nota
de receptores de la ST 2110-30). Procede la fase 5 bis sobre los pasajes 1, 6 y 7.

Otros ficheros tocados: `fuentes/canal-sur/sonido/fabricantes/rane-note102.pdf` y `.txt` (descargado de
https://www.ranecommercial.com/legacy/pdf/old/note102.pdf el 25-09-2026 y pasado a texto con
`documento.py texto`). Ningún otro tema.

## Comprobación de cada propuesta en la fuente

| Propuesta | Fuente releída | Veredicto |
|---|---|---|
| Menor 1 (MADI 56 a 48 kHz) | RME MADI Converter 7.1: sólo «the sample rate can still even vary by +/-12.5%», sin base. DiGiCo TN294: «Connecting Standard MADI at 48K … that is a 56 channel MADI connection» | Acertada. Se corrige atribuyendo: RME sin base; DiGiCo a 48 kHz |
| Menor 2 (SDI resumen) | SMPTE 272M-2004, l. 30: «four channels maximum for composite digital» | Acertada. Aplicada |
| Menor 3 (dBu, dBFS, N-1) | Glosas de los temas 2, 4 y 8 del mismo puesto | Aplicada en las siglas de entrada (misma glosa que el tema 8 para N-1) |
| Observación (receptores ST 2110-30) | ST 2110-30:2025, tabla 3: C = 1 to 8 a 1000 µs y 1 to 64 a 125 µs | Correcta. Aplicada como nota |
| Laguna P5 (jack estéreo, inserción, 3,5 mm) | Rane Note 102 (TRS, TS, auriculares); Soundcraft *Guide to Mixing* sec. 7 (inserción, TRS con fuente desbalanceada); Shure *Wireless Microphone Systems* (1/8" TRS) ; Rane Note 151 (usos del ¼" estéreo) | Confirmada: se amplía. La masa del inserto no la da Soundcraft en texto: se marca como oficio |

## Pasajes cambiados

1. **Portada, «Fuente»**: «Crown y Rane» → «Crown, Rane, Soundcraft y Shure (patillaje de XLR y jack)».
   «Extensión»: 11.000 → 11.500 palabras.
2. **Siglas**: se añaden dBu, dBFS y N-1 (*mix-minus*).
3. **«Resumen de formatos»**, fila MADI: «56 o 64 (el modo de 64, hasta 48 kHz + 1 %); 32 a 96 kHz en modo
   de 64 canales». Fila SDI: «Hasta 16 (SD y HD a 1,5 Gb/s; 4 como máximo en SD compuesto)…».
4. **«Qué es el MADI»**, tabla de modos, fila de 56: «RME no da frecuencia base: dice que puede variar
   ±12,5 %; DiGiCo lo trabaja a 48 kHz (**«Standard MADI at 48K»**)».
5. **«AES67 y la ST 2110-30»**, tras la tabla de niveles (pasaje copiado del común; sólo se añade detrás):
   nota de que es la de emisores y que el receptor C admite **«1 to 8»** a 1.000 µs y **«1 to 64»** a 125 µs.
6. **«El jack TRS y el TS»** (ampliación): cita de Rane 151 sobre los usos del ¼" estéreo; tabla de
   contactos por uso (balanceado, auriculares estéreo: punta izquierdo, anillo derecho, cuerpo común;
   inserción: punta envío, anillo retorno), TS de Rane 102; inserción de Soundcraft (jack conmutado, cable
   en Y); fuente desbalanceada en entrada TRS (malla a anillo y cuerpo); aviso de variación entre
   fabricantes; jack de 3,5 mm TRS estéreo (Shure: videocámaras y receptores de intraauriculares).
7. **«Lo que este tema no da»**: se añade que el reparto de contactos del TRRS no se da.
8. **«Trazabilidad»**: tres filas nuevas (Rane 102, Soundcraft, Shure); fila Rane 151 ampliada; en «oficio»,
   «el uso del jack TRS para señales no balanceadas» pasa a «la masa del punto de inserción».

Relectura de antecedentes: «la tabla es la de los emisores» sigue a la tabla de niveles; «abajo» en la
fila de inserción remite al párrafo de Soundcraft inmediato. Correcto.

## Lentes

- `indice.py` sobre el tema: 11.512 palabras, 55 epígrafes (índice regenerado sin cambios de rúbricas).
- `refutar_prosa.py`: 0 hallazgos (siglas presentadas, sin negritas rotas).
- `negritas.py` con Rane 102, Soundcraft, Shure, Rane 151, DiGiCo y ST 2110-30: todas las negritas nuevas
  literales salvo «tip-ring-sleeve», que en el .txt sale unido por el corte de línea («tip-ring-\nsleeve»
  en el PDF, comprobado): literal.
- Sin normas legales: `refutar_exactitud.py` y `refutar_modo.py` no tocan.

## Preguntas

P5 pasa a entera. P6 sigue a medias (remite al tema 2, correcto). P15: el resumen ya no contradice la tabla.
