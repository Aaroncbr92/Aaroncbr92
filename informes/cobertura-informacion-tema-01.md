# Cobertura del tema 1 del específico de Información y Contenidos

**Prueba del apartado 7 del manual**: se contestan las preguntas reales con el tema delante, y donde
el tema no llegue **se amplía el tema, nunca se recorta la pregunta**.

- **Tema**: Actualidad nacional e internacional: política, economía, sociedad, cultura y deportes.
- **Preguntas de la materia**: **121**. Es **el punto más preguntado de todo el proyecto**: dos de
  cada tres preguntas del bloque específico de la ocupación, y más que ningún tema de Producción o de
  Documentación.
- **Contestadas con el tema delante**: **121**.
- **Preguntas verificadas en la fuente**: **20 de 121** —quince en el BOE y cinco en la fuente oficial
  del dato—, de las cuales **tres sólo en parte**.
- **Preguntas apoyadas sólo en la plantilla**: **101**, listadas una a una en el propio tema.
- **Preguntas cuya fuente contradice a la plantilla**: **1**.

## Qué se hizo con ciento veintiuna preguntas sin temario

El enunciado del punto 1 termina en **puntos suspensivos**: «Actualidad nacional e internacional:
Política, Economía, Sociedad, Cultura y Deportes…». No hay nada que resumir. Lo que se hizo fue lo
mismo que en el tema 6 de Documentación —**tratar cada pregunta como un dato a comprobar**— pero con
tres veces más preguntas y con **una herramienta nueva**, que es el hallazgo de método de este tema.

## El hallazgo: una parte de la «actualidad» se publica en el BOE

**Diez de las quince respuestas atadas al BOE no parecen, leyendo el enunciado, preguntas de
derecho.** Son premios y nombramientos:

| Clase de dato | Dónde se publica | Preguntas que resuelve |
|---|---|---|
| **Premios nacionales de cultura** | Orden del Ministerio de Cultura | Poesía 2024, Fotografía 2023, Periodismo Cultural 2024, Diseño de Moda 2024 |
| **Supresión de un premio nacional** | Orden que modifica la de 22/06/1995 | Tauromaquia 2024 |
| **Premios nacionales de investigación** | Orden del Ministerio de Ciencia | «Julio Rey Pastor» 2023 |
| **Composición del Gobierno** | Real decreto de nombramiento | Partidos de la coalición *(parcial)* |
| **Presidencias autonómicas** | Real decreto de nombramiento | Investidura de Illa *(parcial)* |
| **Zonas de alquiler tensionado** | Resolución trimestral del Ministerio de Vivienda | Cuántas comunidades, y cuál fue la primera *(tres preguntas)* |
| **Sedes de conferencias internacionales** | Acuerdo internacional publicado | La 4.ª Conferencia de Financiación para el Desarrollo |

**Y tres preguntas más son de norma sin decirlo**: las exclusiones de la ley de bienestar animal
(art. 1.3), las exclusiones de la ley de amnistía (art. 2) y la fecha de su entrada en vigor
(disposición final tercera).

**Ese mapa es reutilizable**, y por eso queda escrito: la próxima convocatoria preguntará por otros
premios y otros nombramientos, pero **se publicarán en el mismo sitio**.

## La herramienta que faltaba

Para llegar a esos documentos hubo que construir `herramientas/boe_buscar.py`, **búsqueda por título
en el BOE**. El proyecto tenía dos entradas al Boletín y **entre las dos quedaba fuera el caso más
frecuente de un temario de actualidad**: saber qué se busca y no saber ni el identificador ni el día.

- `boe.py` lee una norma **cuando ya se conoce su identificador**.
- La API de sumarios da el boletín **cuando ya se conoce la fecha**.
- `boe_buscar.py` da el identificador **a partir del título**, con rango de fechas opcional.

Va razonado en `ESTADO.md`, con la trampa del formulario que lo hacía devolver cero resultados sin
dar ningún error.

## Las lagunas que quedan, y por qué

**Ciento una preguntas se apoyan sólo en la plantilla**, y la razón no es la misma en todos los
grupos:

- **Las veinticinco de política internacional** son hechos de prensa extranjera de 2024 —un debate
  electoral, un tiroteo, un resultado en un *land*—. **No producen documento oficial español**, que
  es el corpus con el que este proyecto trabaja, y buscarles fuente sería buscarles una noticia. Una
  noticia no es ninguno de los cinco niveles de la jerarquía del método.
- **Las veintiuna de cultura** son títulos de obras, premios privados y festivales extranjeros. Los
  premios **públicos** se publican en el BOE —y por eso los seis que sí lo son están verificados—;
  el Goya, el Óscar, el Emmy, el Donostia y la Concha de Oro, no.
- **Las diecisiete de deportes** las publican federaciones y comités, cuyas páginas **son actuales**:
  la del Comité Paralímpico Español se consultó y no da el medallero de París 2024, porque muestra la
  actualidad de 2026. **Una página institucional sirve para lo que está hoy en ella**, y el proyecto
  ya se dio esa regla en el tema 6 de Documentación.
- **Las once de sociedad, diez de economía y trece de ciencia y medios** son cifras de informes
  privados —Exceltur, Brand Finance, Barlovento—, hechos judiciales y datos de audiencia.

**Ninguna de las ciento una se dio por perdida sin intentarlo**: la búsqueda por título en el BOE se
corrió sobre las que podían tener documento —premios, nombramientos, normas citadas— y **las que
aparecieron están todas en la lista de verificadas**.

## Lo que este tema añade al proyecto

1. **`boe_buscar.py`**, que sirve a cualquier tema futuro.
2. **El mapa de qué clases de «actualidad» se publican en el BOE**, arriba.
3. **Una discrepancia con la plantilla oficial documentada**: la tasa de paro del segundo trimestre
   de 2024. Es la primera vez en el proyecto que **una fuente estadística** —y no una norma—
   desmiente una respuesta oficial.
4. **Dos enunciados con las opciones descolocadas en el papel**, que no cambian la respuesta pero
   hacen ilegible la pregunta.
