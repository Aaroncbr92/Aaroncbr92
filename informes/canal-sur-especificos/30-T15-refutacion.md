# Puesto 30 · Tema 15 · Refutación (fase 4)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/15-organizacion-nomenclatura-trazabilidad-colaboracion.md`.
Excluido de la exactitud: lo «Copiado del común» (LE 6.1 y «Tres reglas obligatorias») y lo
«Copiado de RTVE sin cambios» (tabla de vistas; fragmento de separación proyecto/material), según
`30-T15-redaccion.md`. La cobertura mira el tema entero.

## Fuentes releídas (25-09-2026)

Avid *User's Guide* R8.0 1999 (txt local; pp. 33-36, 41, 72-74, 126-127, 261, 269-270); *What's New*
v2023.3 (txt, p. 2); *Audio-Video Editing Workflows* 2010 (txt; pp. 11, 18, 19, 25); Avid KB en275293
y ELEMENTS (HTML descargado, pasado a texto); SMPTE ST 377-1:2019 (frontal); EBU Tech 3293 v1.10;
Libro de Estilo 2004 (3.17.1.5, 5.3.3, 6.1.1, 6.1.2); X Convenio, BOJA 240, ficha 5212206 (p. 190).
Además, para cobertura: DaVinci Resolve 21, extractos locales `collab.txt` y `projects.txt`.

## Lente 1 · Exactitud

Las citas en negrita largas se buscaron por script en los volcados (comillas, guiones, ligaduras y
espacios normalizados): todas están; las tres que no casaban cruzan un salto de página (*Attic*,
pp. 35-36; mayúsculas, pp. 126-127; LE 6.1.2, pp. 88-89) y están, comprobadas a mano. Páginas,
fechas (KB 11-08-2023; ELEMENTS 24-01-2023; EBU abril de 2020, Ginebra; ST 377-1 de 28-11-2019),
recuentos (ocho tareas, cinco precauciones, tres juegos, cuatro *bins*, tres vistas, cinco operaciones),
la remisión a ST 330:2011, los requisitos de licencia de ELEMENTS, el fichero .log, la ubicación de
la opción «Use Windows compatible File Names» (General Settings) y el ajuste del guardado automático
(Bin settings): correctos.

### Graves

Ninguno.

### Menores

1. **Error 6, salvedad omitida (4, «Compartir entre versiones», precaución 1).** La KB, en «Check
   version compatibility», añade: «ensure the media is captured or transcoded into a format that is
   shared between the two respective versions» (y remite a la documentación de novedades de cada
   versión). El tema da sólo la frase de cambios de formato. Propuesta: añadir esa instrucción,
   citada.
2. **Precisión (3, «El código de tiempo», 3.17.1.5).** En el Libro de Estilo, el párrafo de «dos o más
   cámaras ENG independientes» se refiere a la entrevista realizada fuera de los estudios **«pero
   pensada para su emisión íntegra»** (3.17.1.5, p. 61), y lo que prevé el realizador es que los
   planos sean compatibles. El tema dice «la entrevista grabada fuera del estudio» sin ese matiz.
   Propuesta: acotarlo así.

## Lente 2 · Cobertura

Los cuatro elementos del enunciado (organización de proyectos, nomenclatura, trazabilidad, buenas
prácticas colaborativas) tienen epígrafe propio, en su orden, más un supuesto práctico. 15 preguntas en
`30-T15-preguntas.md`: **13 enteras, 1 a medias (14), 1 no (15)**.

### Laguna

1. **Colaboración y copias automáticas en un programa de montaje actual.** El tema apoya el trabajo
   compartido y las copias de seguridad en Media Composer: la guía de 1999, una nota de versión de 2023
   y un blog de terceros. Declara que no da «cómo hace hoy» las copias ni otros programas «porque no se
   ha leído su documentación». Pero en el repositorio está la documentación vigente de DaVinci Resolve
   21, con el trabajo colaborativo (cap. 197: bloqueo de *bins*, líneas de tiempo y clips «first come,
   first served»; insignia de color; liberación y *check-in* al seleccionar otro elemento; Live Save
   activado y «Auto conform missing clips» desactivado al activar la colaboración; chat) y la gestión
   de proyectos (cap. 3: *project libraries*, .drp, Live Save, *Project Backups*, *Timeline Backups*).
   Pregunta 15, «no». Propuesta: ampliar 4 (y 1, copias) con un bloque breve de Resolve 21, citado,
   y ajustar la advertencia y «Lo que este tema no da». No se sabe qué programa usa CSRTV: eso sigue
   declarado.

## Lentes automáticas

Tema técnico sin norma legal: sólo proceden `refutar_prosa.py` e `indice.py`, ya pasados por el
verificador (0 hallazgos; índice sin cambios). No se repiten.

## Resumen

Graves 0 · menores 2 · lagunas 1.

## Ficheros tocados

Creados: `30-T15-preguntas.md` y este informe. El tema no se ha tocado. Temporales sólo en el
scratchpad.
