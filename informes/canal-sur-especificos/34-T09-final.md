# 34 · T09 · Revisión de los pasajes rematados (fase 5 bis)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/09-presentacion-locucion-comunicacion-oral.md`.
Alcance: sólo los nueve pasajes que lista `34-T09-remate.md` (comprobados con `git diff` del tema).

## Fuentes releídas (24-09-2026)

- Libro de estilo de Canal Sur, `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`: 3.14 (l. 1816-1848), 8.3-8.3.2 (l. 4124-4200), 8.6 (l. 4330-4345).
- Manual de estilo de RTVE, `fuentes/informacion/RTVE_manual-de-estilo_el-lenguaje.txt`, 6.3.1 (l. 111-115).
- Portada de Autocue, `fuentes/fabricantes/Autocue_portada.txt` (captura del 02-09-2026), l. 5 y 106.

## Pasaje por pasaje

| # | Pasaje | Resultado |
|---|---|---|
| 1 | §4, 8.3 «hasta donde sea posible» / «todo lo que pueda planificarse» | Correcto y literal (la fuente escribe «planiﬁcarse» con ligadura). |
| 2 | §6 Qué es, cita de Autocue | Cita literal. **Corregido**: la traducción quitaba «We believe» y traducía «more connected audiences» como «acercan al público»; ahora «cree que los teleprompters hacen más felices a los presentadores y dan audiencias más conectadas». |
| 3 | §6 Qué es, «autocue» como costumbre de oficio | Correcto; declarado como costumbre y en Trazabilidad. |
| 4 | §6 Cómo se usa, paso imprescindible (3.14) | Negrita literal. **Corregido** el antecedente: «Por eso» colgaba de «el redactor escribe a menudo un texto que leerá otra voz», pero en 3.14 la razón («Por esta razón») es la revisión por presentador y editores; ahora «Por esa revisión, dice el libro, ...». |
| 5 | §6 Cómo se usa, atenuar la formalidad (3.14) | Negritas literales («mas» sin tilde, como la fuente). **Corregido** (error 6, salvedad omitida): se añade el porqué de la prudencia, **«suele tener, a la larga, efectos perniciosos»** generar gran expectativa en una información banal. |
| 6 | §8 El presentador, 8.6 «Por encima de las normas...» | Correcto y literal; «Y añade» tiene antecedente (8.6). |
| 7 | §8 La conexión en directo (8.3.2) | Las cinco negritas son literales y están en 8.3.2. **Corregido**: «lugar habilitado» → «lugar especialmente habilitado», como dice la fuente. |
| 8 | §2 Ritmo, advertencia de ME-RTVE 6.3.1 | Literal y en 6.3.1; «Y advierte» → el Manual de RTVE. Sólo se reajustó el salto de línea que dejaba una línea larga. |
| 9 | Portada, preguntas, índice, Trazabilidad | Correctos. Extensión recalculada con `indice.py`: 3.115 palabras (antes 3.088), puesta a mano en la ficha porque el tema no está en `portadas.tsv`. |

## Lentes tras las correcciones

- `indice.py`: 3.115 palabras, 21 epígrafes.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (Libro de estilo, los ocho ficheros del Manual de RTVE, Autocue): 86 cotejadas, 14 «no están», las mismas 14 del remate, todas por la ligadura «ﬁ/ﬂ» o por saltos de página del volcado; las de los pasajes revisados («planificarse», «eficacia», «fluidos») se comprobaron a mano. La negrita nueva («suele tener...») sí aparece.

## Resultado

Nueve pasajes revisados: cinco sin cambios y cuatro corregidos (traducción de Autocue, antecedente de «Por eso», salvedad de 3.14 y «especialmente habilitado»), además del salto de línea y la extensión. No hay datos sin fuente. El tema queda cerrado.

Ficheros tocados: el tema y este informe.
