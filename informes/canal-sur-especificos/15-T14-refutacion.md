# Grafista (puesto 15) · Tema 14 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/15-grafista/14-gestion-proyectos-graficos-briefing-propuesta-revision-aprobacion-calidad.md`.
Encargo fechado el 24-09-2026; lectura de fuentes el 29-09-2026 (fecha del sistema). No se corrige el tema.

## Alcance

- **Exactitud**: todo lo que no está listado en `15-T14-redaccion.md` como «Copiado del común» (viñetas de
  Montador 09; bloque UER de Realizador 13) ni como «Copiado de RTVE sin cambios».
- **Cobertura**: el tema entero contra el enunciado (BOJA 186/2026, Anexo V, puesto 2.15, punto 14:
  «Gestión de proyectos gráficos: briefing, propuesta, revisión, aprobación y control de calidad.»).

## Fuentes releídas (29-09-2026)

| Fuente | Cómo |
|---|---|
| Design Council, «The Double Diamond» y «Framework for Innovation» (copias descargadas por el verificador) | Cotejo automático de todas las negritas + grep de fases |
| *The Client Brief* (PDF, texto extraído) | Cotejo automático; a mano las dos citas de maquetación a dos columnas (tres razones; ocho apartados) y el apartado 7 |
| Frame.io V4, artículos 9105311, 9105251, 9101068 y 9952618 | Cotejo automático + contexto de cada cita |
| Libro de Estilo (volcado en `fuentes/canal-sur/documentos/`) | 3.6.1, 4.4, 4.4.3, 4.4.4 con marcadores de página |
| X Convenio (volcado en `fuentes/canal-sur/documentos/`) | Fichas 5301010, 5302010, 5351000 con cabecera de página |

Resultado del cotejo: todas las negritas no copiadas son literales (las 11 que no casan son las de la UER, copiadas
del común y fuera de alcance). Páginas del LE (50, 75, 77) y del convenio (125, 196, 201) confirmadas.

## Hallazgos

### Graves

**G1 · Error 1/8 (atribución cruzada) · «Revisar sobre la pieza», viñeta «Comparar versiones» (líneas 373-376).**
El tema dice que la función «Pixel Difference» resalta los píxeles que cambian, «con una condición: **«Static assets
must have the same dimensions to use this feature.»**». En el artículo 9952618 esa nota pertenece a la vista
**Overlay** (deslizador), no a la de diferencias: «Overlay view When comparing two similar images, click Show/Hide
Slider … Note: Static assets must have the same dimensions to use this feature. Pixel difference view When
selecting the Show/Hide Differences option…». La cita es literal, pero está pegada a otra función. Corrección
propuesta: atribuir la condición a la vista de superposición (Overlay, con deslizador) y describir Pixel Difference
aparte (**«it will highlight the pixel differences between the two assets»**), sin condición. La pregunta 11 lo
prueba.

### Menores

**M1 · Error 9 · «El Doble Diamante», tabla de fases, columna «Diamante».** Las páginas del Design Council no
asignan a cada fase «divergente» o «convergente»; sólo dicen que los dos diamantes representan explorar
(divergente) y luego actuar (convergente). El reparto Discover/Develop divergentes y Define/Deliver convergentes es
una lectura razonable, pero se presenta sin marcar. Propuesta: añadir «(reparto propio a partir de la cita)» en la
entradilla de la tabla, junto a «traducción de los nombres, propia».

**M2 · Error 9 · Siglas (líneas 17-18).** Los nombres desarrollados «Institute of Practitioners in Advertising» e
«Incorporated Society of British Advertisers» no aparecen en el PDF leído de *The Client Brief* (sólo las siglas,
webs y direcciones). O se confirman en una fuente leída (webs de IPA e ISBA) y se citan en «Trazabilidad», o se
dejan sólo las siglas con «asociaciones británicas de agencias y de anunciantes», como ya dice el epígrafe 1.

Sin más hallazgos: 4.4 «salvo urgencia extrema» y las fichas del convenio se recogen con su salvedad y su modo
verbal; «dos veces» (control de calidad) y el reparto productor/realizador/grafista están marcados como lectura
propia; las remisiones a los temas 2, 7, 8, 9, 12, 13 y 17 existen (el tema 8 contiene EBU R 95, SMPTE ST 2046-1 y
AS-11 DPP; el tema 7, escaleta técnica y relación de rótulos).

## Cobertura del enunciado

Las cinco palabras (briefing, propuesta, revisión, aprobación, control de calidad) tienen epígrafe propio y
aplicación práctica. **Laguna L1: la «gestión de proyectos» en sentido estricto.** El tema trata el proceso de
diseño y sus hitos de decisión, pero no la planificación del proyecto: calendario e hitos, diagrama de Gantt,
estimación de plazos y recursos, reparto de responsabilidades, alcance-plazo-coste, seguimiento y riesgos. El
propio tema declara no haber leído ISO 21500/21502. Las preguntas 6 y 15 no se pueden contestar. Propuesta para el
remate (Opus, amplía): un epígrafe corto «Planificar el proyecto» con fuente publicada (ISO 21502:2020 en su
resumen oficial, o un manual universitario de gestión de proyectos), aplicado al calendario de una cabecera
(hitos de *brief*, propuesta, revisión, aprobación, QC, entrega), enlazado con TIMINGS de *The Client Brief* y con
4.4.1 del LE (puntualidad y tiempos asignados), que ya está en la fuente leída.

## Preguntas

`15-T14-preguntas.md`: 15 preguntas; entera 11, a medias 1 (zonas seguras, remitidas al tema 8, aceptable),
no 3 (6 y 15 por L1; 11 por G1).

## Lentes

Tema técnico que cita convenio y LE por fichas y puntos, sin articulado del BOE: `refutar_exactitud.py` y
`refutar_modo.py` no aplican; se ha hecho cotejo literal por script propio en el directorio temporal (todas las
negritas contra la unión de las fuentes) y revisión manual de modo y salvedades.

## Ficheros tocados

- `informes/canal-sur-especificos/15-T14-preguntas.md` (nuevo).
- Este informe (nuevo).
- Un script de cotejo en el directorio temporal de la sesión, fuera del repositorio.
