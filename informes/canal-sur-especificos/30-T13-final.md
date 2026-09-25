# Puesto 30 · Tema 13 · Revisión final (fase 5 bis, segunda pasada)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`.
Alcance: sólo los 6 pasajes que lista `30-T13-remate.md` (segunda pasada). La revisión final de la
primera pasada (10 pasajes) queda en git, commit b08a902.

## Fuentes releídas (todas el 25-09-2026)

- `fuentes/canal-sur/montador/web/mos-protocol-2.8.5.txt` y `mos-protocol-4.0.txt`.
- Para las páginas: los PDF bajados de nuevo hoy de mosprotocol.com (enlaces de «Current Version»:
  `MOS_Protocol_Version_2.8.5.pdf`, 281 pp., y `MOS-Protocol-Version-4.0.pdf`, 252 pp.), buscando cada
  literal página a página.
- X Convenio RTVA, `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt`, ficha 5212206
  (BOJA 240/2014, p. 190).

## Pasaje por pasaje

| Nº | Pasaje | Resultado |
|---|---|---|
| 1 | § 4, viñeta «En qué va escrito cada mensaje» | Todos los literales, exactos en ambas versiones (rótulo «General Explanation of MOS message format and construction»; XML/DTD; v1.x «proprietary»; «well formed… not required to be valid»; raíz «mos»; «mosID»/«ncsID»; UCS-2 *big endian*; 2.8.5 PDF p. 11; 4.0 PDF p. 18). Reparto 10540 redacción / 10541 servidor, correcto. **Corregido (error 6, salvedad omitida)**: la fuente da esos puertos como **«default»** y dice que desde la 2.5 **«these ports are vendor selectable but site specific»**, con 10540/10541 **«used as examples»** (PDF p. 14); se añade «por defecto» y la salvedad. **Corregido (error 3, recuento)**: el tema daba dos puertos en la 2.8.5 y tres canales en la 4.0 como si el tercero fuera nuevo; la 2.8.5 ya lleva *mosReqObjList* por el 10542 (PDF pp. 35 y 58). Se menciona y se reescribe «conserva esa lógica» como «conserva la lógica de los dos puertos», que es lo que dice la 4.0 («preserves the logic of MOS 2.x, in that the two-port logic doesn't fundamentally change», PDF p. 9). «ese "tagged text"» tiene antecedente en la viñeta anterior. |
| 2 | § 5, cláusula de lista abierta | Literales exactos (ficha 5212206, p. 190). **Corregido (error 4)**: «el trabajador hace además» → «debe realizar además»; la fuente dice «debiendo realizar». «la ficha» y «su definición» con antecedente. |
| 3 | «Qué se puede preguntar» | Correcto. |
| 4 | «Lo que este tema no da» | Coherente con lo añadido. |
| 5 | Trazabilidad | **Corregido**: la 2.8.5 citaba PDF pp. 11 y 13, pero **«"Running Order" port»** está en la p. 14; queda «pp. 11, 13, 14, 35 y 58» (las dos últimas por el 10542). 4.0 pp. 9 y 18, correctas. Se precisa la columna: «puertos 10540/10541/10542 (por defecto, seleccionables)». |
| 6 | Ficha | «y especificaciones 2.8.5 y 4.0», correcto. Extensión 9.200 → 9.300 (`indice.py`: 9.270 palabras, 35 epígrafes). |

El remate no se equivocó en lo que citó; los ajustes son una salvedad omitida, un recuento, un
«deberá» y una página.

## Lentes

- `negritas.py` contra las dos especificaciones y el convenio: todas las negritas de los pasajes 1 y
  2, incluida la nueva («are vendor selectable but site specific»), se encuentran. Las «no están» son de
  fuentes no pasadas en esta corrida (Resolve, Adobe, Manfredi), fuera de alcance.
- `refutar_prosa.py`: 1 hallazgo, el falso positivo de siempre (MAM en el título).
- `indice.py`: índice regenerado.

## Ficheros tocados

El tema 13 (pasajes 1, 2, 5 y 6) y este informe. Los PDF de MOS, sólo en el directorio temporal.
