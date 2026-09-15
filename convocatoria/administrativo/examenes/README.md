# Los seis exámenes del Cuerpo General Administrativo (C1)

Descargados de la sede electrónica del INAP el 15 de septiembre de 2026. Cada
cuadernillo va con su volcado en texto, hecho con la capa de texto propia del
PDF: **estos PDF no necesitan reconocimiento óptico**, y por eso este bloque no
arrastra el problema de nueves leídos como cuatros que recorre el de Correos.

| Fichero | Qué es | Plantilla |
|---|---|---|
| `2025-cuestionario-modelo-A` | Ejercicio único del **23 de mayo de 2026** | **provisional** |
| `2025-cuestionario-modelo-B` | El mismo examen, barajado | **provisional** |
| `2025-cuestionario-extraordinario` | Llamamiento extraordinario del **27 de julio de 2026** | **provisional** |
| `2024-cuestionario-modelo-A` | Ejercicio único de la **OEP 2023-2024** | **definitiva** |
| `2024-cuestionario-modelo-B` | El mismo examen, barajado | **definitiva** |
| `2024-cuestionario-extraordinario` | Llamamiento extraordinario de esa convocatoria | **definitiva** |

**Cada cuadernillo trae 125 preguntas**: 70 de la primera parte más 5 de
reserva, y 20 más 5 de reserva por cada uno de los dos supuestos prácticos.
**750 huecos en total, 505 preguntas distintas.** Ninguna se repite de una
convocatoria a otra.

## Lo que hay que saber antes de usarlos

**Los modelos A y B son el mismo examen barajado**, y barajan también las
opciones dentro de cada pregunta. En 2025 son idénticos; en 2024 casi, con dos
preguntas propias de cada modelo y alguna diferencia de redacción. De ahí sale
la comprobación fuerte de este bloque: **245 preguntas tienen dos plantillas
independientes**, y las dos tienen que señalar el mismo texto de opción aunque
la letra sea distinta. `herramientas/administrativo_examen.py cruzar` lo
comprueba: **245 de 245, cero discrepancias**.

**El modelo B de 2025 no imprime ninguna pregunta 65: imprime dos veces el 66.**
Su propia plantilla lo reconoce con una nota al margen de la respuesta 65. Cuál
es cuál lo resuelve el cruce con el modelo A, que las numera bien.

**Las plantillas de 2024 anulan once preguntas** del corpus. Eso no es un
estorbo: es un registro de preguntas defectuosas firmado por quien puso el
examen.

**Las plantillas de 2025 son provisionales.** El plazo de alegaciones se cerró
el 28 de mayo de 2026 —`2025-nota-informativa-alegaciones`— y la Comisión
Permanente de Selección dijo que contestaría publicando las definitivas. A 15 de
septiembre de 2026 siguen sin aparecer. **Hay que volver a mirar la sede antes de
dar por buenas las 375 preguntas de 2025.**
