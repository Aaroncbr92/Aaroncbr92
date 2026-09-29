# Grafista (15) · Tema 7 · Revisión del remate (fase 5 bis)

Tema: `temas/canal-sur-especificos/15-grafista/07-flujos-trabajo-realizacion-edicion-produccion-documentacion-continuidad.md`.
Alcance: sólo los pasajes 1-9 de `15-T07-remate.md`. Fecha del encargo: 24-09-2026; fuentes releídas el
29-09-2026 (fecha de sistema). Ficheros tocados: el tema y este informe.

## Cotejo con la fuente (29-09-2026)

| Pasaje | Fuente | Resultado |
|---|---|---|
| 1 Qué se puede preguntar (Locutor de Continuidad) | X Convenio, ficha 5323001 | Correcto |
| 2 Mapa de fichas, fila Locutor (5323001, B04, p. 182) | Convenio txt l. 6603-6622 (cabecera siguiente «página 183»); art. 45.1, p. 74, NIVEL B04 | Literal y datos correctos. La afirmación previa «la del Editor es la única ficha que habla del diseño de elementos de continuidad» sigue siendo cierta (grep: «diseño» sólo en 5302010) |
| 3 §1 Breves, «No aparece firma.» | Libro de Estilo 3.8, p. 52 | Literal (ligadura «ﬁ» en el txt) |
| 4 §4 Rótulos de archivo: 9.9.1 (p. 166), 3.2.2 (p. 46), 9.2.12.3 (p. 130) | Libro de Estilo txt l. 6241-6247, 1431-1438, 4686-4700; índice l. 321, 497, 571 | Literales y páginas correctos; «este capítulo» = cap. 9, antecedente presente |
| 5 §5 Fichas: Editor (función, tareas, «Decidir…»), Locutor (función y tres tareas), tabla del reparto | Convenio l. 5088-5111 (p. 125) y 6603-6617 (p. 182); art. 45.1 p. 74 (Editor B03, Locutor B04) | Literales correctos; B03 del Editor confirmado |
| 6 §5 Módulo 0904, cinco contenidos | RD 1680/2011 (BOE-A-2011-19599), texto l. 607-612 | Lista completa y en orden |
| 7 Aplicación práctica, dos filas | 3.2.2; ficha 5302010 | Cita literal correcta; ver corrección 2 |
| 8 Normativa y Trazabilidad | Convenio | Ficha 5323001 (p. 182) y fecha añadidas; correcto |
| 9 Portada 8.900 palabras | `indice.py` | 8.950 palabras medidas; correcto |

## Correcciones aplicadas (comprobadas en la fuente)

1. §5, Editor de Continuidad: «Es la tarea que resuelve qué se emite cuando una pieza gráfica falla…» es
   inferencia, no dice eso la ficha → se marca «(lectura propia)» (error 9).
2. Aplicación práctica, fila del accidente simulado: «en sucesos con muertos o heridos graves» omitía
   parte de la salvedad de 3.2.2 («muerte, heridas graves, suicidios o situaciones de abuso») → «en
   sucesos con muertes, heridas graves, suicidios o abusos» (error 6).

## Antecedentes

«el mismo apartado» (3.8), «este capítulo» (9.9.1, dentro de cita), «Es la tarea que…», «esta ficha»,
«esa decisión» y «esos elementos» (módulo 0904) tienen su antecedente inmediatamente delante.

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 8.950 palabras, 37 epígrafes.

## Resultado

Remate correcto en datos; dos retoques menores. Tema cerrado.
