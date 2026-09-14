# Examen de Correos del 7 de mayo de 2023

**Los seis ficheros los publica la propia Correos**, en el mismo almacenamiento
desde el que sirve las bases de la convocatoria
(`cswetwebcorsta01.blob.core.windows.net`). Descargados el 2026-09-14. De cada uno
hay el PDF y su transcripción `.txt` al lado, sacada de la capa de texto con
`pymupdf`: **los seis la traen limpia** y ninguno ha hecho falta reconocerlo
ópticamente.

| Fichero | Qué es | Páginas |
|---|---|---:|
| `Cuestionario-REP_A_07052023` | Cuadernillo de **Reparto y Agente de Clasificación**, modelo A | 15 |
| `Cuestionario-REP_B_07052023` | El mismo, modelo B | 15 |
| `Cuestionario-ATC_A_07052023` | Cuadernillo de **Atención al Cliente**, modelo A | 16 |
| `Cuestionario-ATC_B_07052023` | El mismo, modelo B | 16 |
| `Plantilla-Respuestas-Reparto-y-Agente` | Respuestas oficiales de los dos modelos de Reparto | 1 |
| `Plantilla-Respuestas-Atencion-al-cliente` | Respuestas oficiales de los dos modelos de Atención al Cliente | 1 |

## Lo que hay dentro, y por qué importa

**Cada cuadernillo trae 110 preguntas: 100 principales y 10 de reserva.** Cuatro
cuadernillos por 110 son 440 papeletas, **pero el banco no son 440 preguntas**, y
contarlas así sería inflar la cifra al doble.

**Dos cuadernillos por puesto, no dos exámenes.** Los modelos A y B de un mismo
puesto llevan **casi las mismas preguntas en distinto orden**, que es como Correos
evita la copia en una prueba de 55.000 personas simultáneas. Medido sobre los
enunciados de Reparto: **104 de 106 son comunes a los dos modelos**, y **sólo 13
caen con el mismo número**.

**Y entre puestos no se repite ni una.** Comparados los enunciados de Reparto con
los de Atención al Cliente, **la coincidencia literal es cero**: Correos no montó
un tronco común con preguntas específicas encima, sino **dos exámenes enteramente
distintos** sobre el mismo temario.

**El banco real, por tanto:**

| | Preguntas únicas |
|---|---:|
| Reparto y Agente de Clasificación (A ∪ B) | **108** |
| Atención al Cliente (A ∪ B) | **110** |
| Comunes a los dos puestos | **0** |
| **Total del banco** | **218** |

De ellas, **unas siete son psicotécnicas** —series de figuras— y **no son materia
del programa**, así que el banco aprovechable para el temario ronda las **211
preguntas**.

## Las preguntas anuladas, sacadas de la propia plantilla

**La plantilla escribe «Anulada» en la celda de la respuesta**, de modo que la lista
sale del documento oficial y no de ninguna fuente de segunda mano. Se ha comprobado
además a la vista sobre la hoja, porque las celdas van sombreadas y convenía
descartar que el sombreado dijera algo que el texto no dice. **Dice lo mismo.**

**Correos anuló siete preguntas y las sustituyó por las de reserva**, por su número
de orden:

| Cuadernillo | Anulada | Sustituida por |
|---|---|---|
| Reparto, modelo A | 13 | 101 |
| Reparto, modelo A | 69 | 102 |
| Reparto, modelo B | 13 | 101 |
| Reparto, modelo B | 47 | 102 |
| Reparto, modelo B | 70 | 103 |
| Atención al Cliente, modelo A | 12 | 101 |
| Atención al Cliente, modelo B | 14 | 101 |

**Son siete y no seis**: el modelo B de Reparto anuló tres, no dos. La tercera, la
47, se perdía al extraer el cuadernillo porque **las psicotécnicas no tienen
opciones de texto** —son figuras— y el extractor las descartaba en silencio. Está
arreglado en `herramientas/correos_examen.py`, y la cuenta cuadra ahora con la
plantilla: **2, 3, 1 y 1**.

**Una pregunta anulada sigue siendo material de estudio**, porque su enunciado
salió del temario aunque la pregunta fallara. **Pero no sirve para calibrar la
respuesta oficial**, y por eso va marcada.

## Dos hallazgos en los cuadernillos

**Primero, y explica una de las anulaciones.** La **pregunta 47 del modelo B de
Reparto** —una psicotécnica de series de figuras— **pide elegir «entre las figuras
inferiores (A, B, o D)»**: nombra tres opciones donde hay cuatro, y **se salta la
C**. Comprobado a la vista sobre la página 7 del cuadernillo. **Es exactamente la
pregunta que Correos anuló**, y el motivo está impreso en su enunciado.

**Segundo: la errata está en la respuesta buena.** La **pregunta 2 del modelo A de
Reparto** escribe **«Conta» por «Consta»** en dos de sus cuatro opciones, la B y la
D. Lo llamativo no es la errata: es que **la opción correcta según la plantilla es
la B**, es decir, **una de las dos mal escritas**. Quien descartara una opción por
estar mal escrita habría descartado la buena.

**Este proyecto cita los enunciados como están impresos**, con sus erratas, y las
declara al lado.

## El examen, cruzado y citable

`herramientas/correos_examen.py` cruza cada cuadernillo con su plantilla y escribe
`examen-REP-A.md`, `examen-REP-B.md`, `examen-ATC-A.md` y `examen-ATC-B.md`: **la
pregunta entera, sus cuatro opciones y la respuesta oficial señalada**, con las
anuladas y las psicotécnicas dichas.

**La respuesta va por número de pregunta dentro de su modelo.** Cruzar el enunciado
del modelo A con la letra del modelo B daría un examen falso de principio a fin, y
es un error fácil de cometer porque las preguntas son casi las mismas.
