# Productor/a (puesto 32) · Tema 9 · Remate

Fase 5. Tema: `temas/canal-sur-especificos/32-productor-a/09-produccion-de-contenidos-grabados-directos-y-multiplataforma.md`.
Entrada: `32-T09-refutacion.md` (0 graves, 3 menores, 1 laguna) y `32-T09-preguntas.md` (13 enteras,
1 a medias, 1 no). **El remate amplía contenido nuevo** (laguna 1: sonoridad de la radio), así que
toca fase 5 bis sobre los pasajes 1 y 6.

Fuentes leídas el 25-09-2026 («hoy» del encargo: 24-09-2026):
- EBU R 128 s3-2023, *Loudness in Radio* (Ginebra, noviembre de 2023; 1.ª ed. junio de 2021),
  descargada de tech.ebu.ch/docs/r/r128s3.pdf y pasada a texto con `documento.py` (scratchpad
  `t09r/r128s3.txt`): texto de contexto, considerandos, recomendaciones g) a s).
- EBU Tech 3401 (noviembre de 2023), tech.ebu.ch/docs/tech/tech3401.pdf: **sólo portada e
  historial** (título). Su contenido no se ha leído y así lo dice el tema.
- Ley 11/2023: título oficial en la API de legislación consolidada del BOE (BOE-A-2023-11022; el
  mismo título consta en `fuentes/canal-sur/BOE-A-2023-11022.md`, l. 2223).
- Carta 2024-2029 (`carta-servicio-publico-2024-2029-boja-247-2023.txt`), artículo 7 (l. 473-563)
  y artículo 13.9 (l. 793-795).
- Siglas URL, SSL y TLS: desarrollo como en temas ya cerrados del repositorio; UMH, como en el tema
  6 del específico de Operador/a Montador/a de Vídeo (l. 17: «Universidad Miguel Hernández de
  Elche (UMH)»).

## Correcciones: todas comprobadas y aplicadas

| Hallazgo | Comprobación | Resultado |
|---|---|---|
| Menor 1 · URL, TLS/SSL y UMH sin presentar | Aparecen en «Emitir en directo…» (cita de YouTube), «El vídeo interactivo» y Trazabilidad; no estaban en las siglas | Aplicado (pasaje 2) |
| Menor 2 · Fila de la Carta en Trazabilidad | 7.1 (pódcast, l. 486), 7.2 (redes, plataformas de intercambio, Ley 13/2022), 7.6 y 7.7 («podrán ser instadas») y 13.9 (subtitulado de informativos) releídos en el BOJA: el tema los usa | Aplicado, sin «por remisión» porque se han releído (pasaje 5) |
| Menor 3 · Ley 11/2023 sin fecha ni título | Título leído en el BOE | Aplicado en «Normativa que el tema invoca» (pasaje 4) |
| Laguna 1 · sonoridad de la radio | R 128 s3 leída y pública | Ampliado (pasajes 1, 3, 6 y 7) |

Ninguna corrección del informe resultó equivocada.

## Pasajes cambiados

1. **«Radio» › «La radio más allá de las ondas», último párrafo** (antes: «documentos que no se han
   leído… Sus cifras no se dan aquí»). Ahora: R 128 s3 con fecha; cita del «key concept»
   (producción/distribución); recomendaciones h) (−23,0 LUFS, −1 dBTP, tolerancias a la R 128) e i)
   (intercambio interno y externo) para la producción; k) (−23,0 LUFS por defecto), n) (−20,0 a
   −16,0 LUFS si se aparta), p) (*streaming* de radio por la R 128 s2) y s) (remisión a Tech 3401,
   con título, contenido no desarrollado) para la distribución; y una aplicación al puesto (entrega a
   −23 LUFS y −1 dBTP, se produzca dentro o fuera; el nivel de distribución de Canal Sur Radio no
   consta publicado). Las elisiones «[...]» quitan las llamadas [3], [4] y la nota 1 de la fuente.
2. **Siglas de entrada**: añadidos URL, SSL y TLS (tras HTTP) y UMH (tras FAST).
3. **«Lo que este tema no da»**: la viñeta de sonoridad pasa a «La sonoridad que aplica Canal Sur a
   su *streaming*, a su pódcast y a su radio: no publicada. El desarrollo de la EBU Tech 3401…: no
   leído.»
4. **«Normativa que el tema invoca»**: Ley 11/2023 con fecha y título oficial completo.
5. **Trazabilidad, fila de la Carta**: «Artículo 7.1 (…), 7.2 (…), 7.6 (…) y 7.7 (…); 13.9 (…)».
6. **Trazabilidad**: fila nueva de la EBU R 128 s3-2023 y de la portada de Tech 3401
   (recomendaciones h, i, k, n, p y s).
7. **Portada**: «Fuente» cita «EBU R 128-2023 y sus suplementos R 128 s2-2023 y R 128 s3-2023»;
   «Extensión», de 15.800 a 16.300 palabras.

Relectura de antecedentes: «la referencia [1]» tiene delante la cita de h); «el suplemento del
*streaming*» remite al epígrafe nombrado; «recomendación s) del suplemento» se refiere a la R 128
s3 nombrada en el mismo párrafo; «(recomendaciones h e i)» tiene las dos delante. Correcto.

## Lentes

- `negritas.py` contra `r128s3.txt` y `tech3401.txt`: las negritas nuevas sin elisión, «ok»; las dos
  con «[...]» (h y k) dan «NO ESTÁ» por la elisión y se comprobaron a mano, enteras, en el texto
  plano de la fuente (1 coincidencia cada una). El título de Tech 3401 está en su portada.
- `refutar_prosa.py`: 0 hallazgos.
- `indice.py`: 16.274 palabras, 66 epígrafes, sin cambios de estructura (el tema no está en
  `portadas.tsv`, así que la portada no la regenera; se ajustó a mano).
- `refutar_exactitud.py` y `refutar_modo.py`: no se corren; ningún pasaje cambiado cita un
  artículo de norma ni un verbo de mandato de una ley.

## Preguntas

La 7 pasa de **no** a **entera**: el tema da ahora el documento (R 128 s3) y su nivel objetivo
(−23,0 LUFS en producción y, por defecto, en distribución). La pregunta no se ha tocado. La 15 sigue
a medias por remisión declarada. Nuevo resultado: **14 enteras, 1 a medias, 0 no.**

Ficheros tocados: el tema 9 y este informe. Observación sin tocar: la extensión (16.300) sigue por
encima de la del tema 7; queda a juicio del coordinador.
