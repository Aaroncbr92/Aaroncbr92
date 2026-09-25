# Puesto 28 · Operador/a de Sonido · Tema 11 · Fase 5 bis, revisión del remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/11-lineas-y-conexiones.md`. Entrada:
`28-T11-remate.md` (ocho pasajes cambiados). Fecha de trabajo y de lectura de todas las fuentes:
25-09-2026 (el encargo fija «hoy» en 24-09-2026).

**Resultado: 4 correcciones** (una salvedad omitida, un dato sin fuente, una salvedad de «most» y
una regla de la ST 2110-30 parafraseada con una inferencia que la norma no hace). El resto del remate,
confirmado.

## Pasaje a pasaje

| Pasaje del remate | Fuente releída | Veredicto |
|---|---|---|
| 1 Portada (Fuente, Extensión) | — | Correcto. Extensión real tras esta fase: 11.594 palabras (≈ 11.500) |
| 2 Siglas dBu, dBFS, N-1 | Temas 2, 4 y 8 del puesto | Glosas idénticas. N-1 tiene uso en el tema (l. 991, 1031). Correcto |
| 3 Resumen: fila MADI | RME MADI Converter 7.1: «48 kHz + ca. 1%», «32 channels at 96 kHz» | Correcto |
| 3 Resumen: fila SDI | SMPTE 272M-2004, l. 30: «four channels maximum for composite digital» | Correcto |
| 4 MADI, fila de 56 canales | RME: «can still even vary by +/-12.5%»; DiGiCo TN294 l. 82-84: «Connecting Standard MADI at 48K … that is a 56 channel MADI connection» | Correcto |
| 5 Nota de receptores ST 2110-30 | ST 2110-30:2025, cap. 7 y tablas 2 y 3 | **Corregido** (ver 4) |
| 6 Jack TRS/TS (ampliación) | Rane 102; Rane 151; Soundcraft *Guide to Mixing*, sec. 7, p. 31; Shure *Wireless Microphone Systems* | **Corregido** (ver 1 a 3). Citas de Rane 151 y Soundcraft literales; la sección 7 está bien atribuida (índice: «SECTION 7: WIRING UP & CONNECTORS … 31») |
| 7 «Lo que este tema no da» (TRRS) | — | Correcto; cuadra con la corrección 2 |
| 8 Trazabilidad | — | Filas nuevas correctas (Rane 102 © 1982). Se añade al oficio el nombre «3,5 mm» |

## Correcciones aplicadas (cada una comprobada en la fuente)

1. **Salvedad omitida (error 6), Rane 102.** La tabla de contactos no es norma general: Rane la da
   **«On Rane equipment outfitted with input/output phone jacks»**, y la de auriculares, para salidas
   **«designed exclusively for headphone use»**. Se añade delante de la tabla.
2. **Dato sin fuente (error 9), 3,5 mm.** El tema decía «jack pequeño de 3,5 mm (1/8")»; Shure sólo da
   1/8" (que además no son 3,5 mm exactos), y el propio tema declara «las medidas del jack pequeño
   (3,5 mm) … sin fuente leída». Queda: «que Shure mide en 1/8" (en el oficio se le llama de 3,5 mm)»,
   y «el nombre de 3,5 mm» se lista como oficio en «Trazabilidad».
3. **Salvedad «most» (error 6), Shure IEM.** «apta para entradas de línea» → «apta para la mayoría de
   las entradas de línea (**«suitable for most line level input devices»**)».
4. **Paráfrasis inexacta, ST 2110-30.** «cada nivel debe admitir también los formatos de los
   inferiores» no está en la norma (el C no admite los formatos de 96 kHz de AX y BX). Se sustituye por
   la regla literal: emisores, **«at least one channel count»**; receptores, **«all possible
   combinations»** de la tabla 3. El ejemplo del nivel C (1 to 8 a 1.000 µs; 1 to 64 a 125 µs) se
   mantiene: literal.

## Antecedentes

«La tabla es la de los emisores» sigue a la tabla 2; «Soundcraft (abajo)» remite al párrafo inmediato;
«Shure lo cita» tiene delante «que Shure mide»; «la de auriculares» remite a la fila de la tabla que
sigue. Correctos.

## Lentes

- `refutar_prosa.py`: 0 hallazgos. `indice.py`: 11.594 palabras, 55 epígrafes.
- `negritas.py` con Rane 102 y 151, Soundcraft, Shure, ST 2110-30 y DiGiCo: todas las negritas del
  remate y de esta fase, literales, salvo «tip-ring-sleeve»: el .txt dice «tip-ringsleeve»; el PDF
  (pypdf) da «tip-ring-\nsleeve». Guion de compuesto, no de corte (Rane 102 escribe igual
  «tip-ring-sleeve»): literal.

Otros ficheros tocados: ninguno salvo el tema y este informe.
