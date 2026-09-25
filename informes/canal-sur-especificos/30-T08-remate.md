# Puesto 30 · Tema 8 · Remate (fase 5, segunda ronda)

Fecha: 25-09-2026 (encargo fechado 24-09-2026).
Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/08-ingesta-digitalizacion-transferencia-verificacion-copias-metadatos-archivo.md`.
Entradas: `30-T08-refutacion.md` (segunda ronda: graves 0, menores 1, laguna 1) y `30-T08-preguntas.md`
(13 E, 1 M, 1 N). El remate de la primera ronda (XMP, LTO 30/40 TB, sexta tarea) queda en git
(commit b08a902).

**Amplía contenido nuevo: sí** (subepígrafe «El formato de conservación: códecs sin pérdidas», § 7).
Procede la fase 5 bis sobre los pasajes 1 y 2.

## Fuentes leídas en el remate (25-09-2026)

| Fuente | Cómo | Guardada en |
|---|---|---|
| IETF, RFC 9043, *FFV1 Video Coding Format Versions 0, 1, and 3* (agosto de 2021): resumen y § 1 | curl, texto de rfc-editor.org | `fuentes/canal-sur/montador/web/rfc9043.txt` |
| IETF, RFC 9559, *Matroska Media Container Format Specification* (octubre de 2024): resumen | curl, texto | `.../web/rfc9559.txt` |
| Library of Congress, *Sustainability of Digital Formats*, fdd000341 (FFV1, act. 2023-10-10) | curl, HTML a texto | `.../web/loc-fdd000341.txt` |
| Library of Congress, fdd000206 (MXF OP1a, JPEG 2000 sin pérdidas, act. 2025-05-22) | curl, HTML a texto | `.../web/loc-fdd000206.txt` |
| Library of Congress, fdd000351 (vídeo sin comprimir YCbCr) | curl; leída, no citada | `.../web/loc-fdd000351.txt` |
| jpeg.org, «About JPEG» | curl, HTML a texto | `.../web/jpeg-about.txt` |
| Resolve 21, p. 562 (regla y ejemplo de *Capture Now*) | ya citada en el tema | — |

**No leídos** (y así lo dice el tema): IASA-TC 06, SMPTE RDD 48 y SMPTE ST 422; lo que el tema dice
de ellos va atribuido a las fichas de la Biblioteca del Congreso. Las siete negritas nuevas se
cotejaron por programa contra los ficheros guardados: todas literales.

## Decisiones sobre la refutación

1. **Menor (sexta tarea en «Documentos técnicos»)**: comprobada en el tema (la cita literal ya está
   en «El punto en la ficha del puesto»); aplicada tal como se proponía.
2. **Laguna, pregunta 15 (formatos de conservación)**: aplicada ampliando el tema, sin tocar la
   pregunta. Con el tema nuevo la pregunta queda **entera** (b, FFV1 o JPEG 2000 sin pérdidas).
3. **Pregunta 6 (a medias, opcional)**: aplicada una frase de cálculo. 3.600 × 24 = 86.400 cuadra con
   el ejemplo del manual; el manual no da la cadencia del ejemplo, y así se dice. La pregunta queda
   **entera** (b, 00090000).

## Pasajes cambiados (texto nuevo)

1. **§ 7, subepígrafe nuevo «El formato de conservación: códecs sin pérdidas»** (tras «La LTFS: la
   cinta como un disco»): qué es un códec sin pérdidas y por qué el vídeo de trabajo con pérdidas no es
   máster de conservación (oficio); FFV1 en Matroska con tres citas del RFC 9043 (sin pérdidas,
   intra; compresión, fijeza y autodescripción; CRC de la versión 3), una del RFC 9559 y la
   clasificación de la Biblioteca del Congreso («preferred»), más IASA-TC 06 según la ficha de la
   Biblioteca; JPEG 2000 sin pérdidas en MXF OP1a con la cita de RDD 48 recogida por la Biblioteca y
   ST 422 como no leída; tercera vía sin comprimir; consecuencia para la sala (máster frente a copia
   de trabajo, DIP); hueco de CSRTV. Entrada nueva en el índice.
2. **§ 2, «Por qué el nombre de cinta y el código de tiempo lo son todo»**: tras la cita de
   00086400.dpx, «El número es el código de tiempo pasado a cuadros: una hora son 3.600 s, y
   3.600 × 24 = 86.400, así que el ejemplo corresponde a 24 cuadros por segundo; a 25, el mismo
   código daría 00090000 (cálculo: el manual no dice la cadencia del ejemplo).»
3. **Siglas**: IETF, RFC, IASA y JPEG (esta, con jpeg.org).
4. **Portada**: Fuente añade IETF y la Biblioteca del Congreso; Extensión 11.000 → 12.000 palabras.
5. **«Qué se puede preguntar»**: añade el formato sin pérdidas de conservación.
6. **«Documentos técnicos que el tema cita»**: fila del convenio con «etiquetar para la emisión
   automatizada (remitida al tema 13)»; filas nuevas de RFC 9043/9559, Biblioteca del Congreso y
   jpeg.org.
7. **«Lo que este tema no da»**: IASA-TC 06, RDD 48 y ST 422 no leídos; formato de conservación de
   CSRTV no publicado.
8. **«Trazabilidad»**: tres filas nuevas (25-09-2026); la lista de oficio añade «por qué el máster de
   conservación no es el fichero de trabajo», y el cálculo añade el nombre del clip en *Capture Now*.

Relectura de antecedentes: «su misma ficha» (→ la de la Biblioteca del Congreso, frase anterior),
«lo» en «lo define el RFC 9559» (→ el contenedor Matroska), «ella» en «es con ella con la que el RFC
9043 compara» (→ guardar sin comprimir, misma frase), «el ejemplo», «el mismo código» (→ la cita de
la p. 562 inmediatamente antes): todos con su antecedente delante.

## Lentes

- `indice.py`: 11.815 palabras, 45 epígrafes; índice al día. (El aviso «sin portada: es un esquema»
  sale también con la versión de b08a902: la herramienta sólo reconoce las portadas de los temas del
  .tsv.)
- `refutar_prosa.py`: 1 hallazgo, previo al remate (la referencia del convenio en «Documentos
  técnicos» y «Trazabilidad», que es su sitio); siglas y negritas limpias.
- Sin norma jurídica citada: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

El tema; este informe (sustituye al remate de la primera ronda); nuevos en
`fuentes/canal-sur/montador/web/`: `rfc9043.txt`, `rfc9559.txt`, `loc-fdd000341.txt`,
`loc-fdd000206.txt`, `loc-fdd000351.txt`, `jpeg-about.txt`.
