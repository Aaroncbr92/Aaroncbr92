# Grafista (15) · Tema 7 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/07-flujos-trabajo-realizacion-edicion-produccion-documentacion-continuidad.md`.
Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema). Entradas:
`15-T07-refutacion.md` y `15-T07-preguntas.md`. Ficheros tocados: el tema y este informe.

## Fuentes releídas para cada corrección (29-09-2026)

| Corrección | Fuente | Resultado |
|---|---|---|
| M1 | Libro de Estilo CSTV 2004, 9.9.1 (p. 166) | Confirmado: el rótulo «Archivo» se enmarca en «delincuencia, malos tratos, asuntos judiciales o cualquier variante reflejada en este capítulo», y la duración lleva «al menos con suficiente margen como para ser leído sin apremio por el espectador» |
| M2 | Libro de Estilo, 3.2.2 (p. 46) | Confirmado: «imprescindibles para la comprensión de una noticia importante» y la frase de sucesos («muy escrupulosos con este método») |
| Pregunta 13 | Libro de Estilo, 3.8 (p. 52) | Confirmado: «No aparece firma.» cierra el apartado |
| L1 | X Convenio, ficha 5302010 (p. 125) | Confirmado literal: «Decidir (en caso de ausencia de superior y ante situaciones imprevistas)…» |
| L2 | X Convenio, ficha 5323001 (p. 182); art. 45.1 (p. 74, nivel B04, «LOCUTOR/A DE CONTINUIDAD») | Confirmado; la ficha tiene una tercera tarea que el informe no citaba («Colaborar en la continuidad de la programación en los casos en que existan circunstancias no ordinarias que lo requieran.»), añadida también |
| Fuera de alcance (módulo 0904) | RD 1680/2011, BOE-A-2011-19599, contenidos del módulo 0904 | Confirmado que faltaba «Operaciones de finales de edición sobre programas y piezas que hay que emitir.»; como se tocaba §5, se añade el punto literal en su orden (mejor que «entre ellos:») |

Ninguna corrección del informe resultó equivocada.

## Pasajes cambiados

1. **Qué se puede preguntar**: la lista de fichas que tocan el grafismo añade «Locutor de Continuidad».
2. **Mapa de fichas** (epígrafe del puesto): fila nueva «Continuidad (locución) | Locutor de Continuidad (5323001, B04, p. 182)» con la tarea de adaptación del guion.
3. **§1 Piezas gráficas del informativo, breves**: se añade «y el mismo apartado cierra: **«No aparece firma.»**».
4. **§4 Los rótulos que obliga a poner el uso de archivo**: entrada reescrita («Cuando se usa imagen de archivo en los asuntos del capítulo 9 del Libro de Estilo (delincuencia, malos tratos, asuntos judiciales…) o una reconstrucción…»); la cita de 3.2.2 se completa con la frase de sucesos; el cierre añade la salvedad de 9.9.1 («al menos con suficiente margen…»).
5. **§5 Las fichas**: rúbrica ahora «Editor de Continuidad, Secretario de Emisiones y Locutor de Continuidad» (índice regenerado); viñeta nueva en el Editor de Continuidad («Decidir (en caso de ausencia de superior…)» y una frase de aplicación); párrafo nuevo del Locutor de Continuidad (función y tres tareas, literales); fila del Editor en la tabla del reparto ampliada con esa decisión; fila nueva del Locutor.
6. **§5 Del departamento gráfico a la emisión**: la lista de contenidos del módulo 0904 incluye «Operaciones de finales de edición sobre programas y piezas que hay que emitir.».
7. **Aplicación práctica**: fila del accidente simulado («Sólo si es imprescindible para comprender una noticia importante; en sucesos con muertos o heridos graves, con especial escrúpulo»); fila de la promoción con horario cambiado (si no llega a tiempo y falta el superior, decide el Editor de Continuidad, ficha 5302010, cita literal).
8. **Normativa que el tema invoca** y **Trazabilidad**: se añade la ficha del Locutor de Continuidad (5323001, p. 182) y su fecha de lectura.
9. **Portada**: extensión 8.400 → 8.900 palabras (cuerpo medido: 8.946).

Relectura de antecedentes: «el mismo apartado» (3.8), «esa decisión», «esta ficha» y «Es la tarea que…» tienen el antecedente inmediatamente delante.

## Lentes

- `indice.py`: índice regenerado; 8.946 palabras, 37 epígrafes, sin rutas del proyecto en el cuerpo.
- `negritas.py` (convenio, Libro de Estilo, IMS077_3, RD 1680/2011): todas las negritas nuevas casan, salvo «No aparece firma.» y «…suficiente margen…», que fallan sólo por la ligadura «ﬁ» del txt del Libro de Estilo (cotejadas a mano: literales). Los demás «NO ESTÁ» son previos (ligaduras, rótulos de viñeta, pasajes copiados) y no se tocan.
- `refutar_prosa.py`: 0 hallazgos.

## Resultado

Menores M1 y M2 corregidos; pregunta 13 cubierta; lagunas L1 y L2 ampliadas. **Amplió contenido nuevo**:
toca fase 5 bis sobre los pasajes 2, 5 y 7 (y 6).
