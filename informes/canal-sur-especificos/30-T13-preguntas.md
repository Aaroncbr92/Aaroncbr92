# Puesto 30 · Tema 13 · Preguntas tipo test (fase 4, segunda pasada)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`,
en su estado tras el remate y la revisión 5 bis. Contestadas sólo con el tema. Respuesta correcta en
cursiva. Las 15 de la primera pasada (13 enteras, 1 a medias, 1 no) quedan en git (commit b08a902);
éstas son nuevas y cargan sobre los pasajes ampliados.

| Nº | Tipo | Pregunta | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Teoría | ¿Cuál de estas tareas NO figura en la ficha 5212206 del convenio? a) Recibir y enviar enlaces; b) Repicar cintas orientadas a la producción, emisión y comercialización; c) Compactar para el archivo de material audiovisual; d) *Programar la automatización de continuidad* | Entera (§ 5, tabla y frase siguiente) |
| 2 | Teoría | El Blackmagic Proxy Generator escribe las copias *proxy*: a) en la carpeta de caché de Resolve; b) *en una subcarpeta «Proxy» al mismo nivel que el original*; c) en el disco de sistema; d) en la biblioteca de proyectos | Entera (§ 1) |
| 3 | Teoría | En el Proxy Generator, una carpeta vigilada en estado *Waiting*: a) está vacía; b) *tiene clips sin convertir y espera al arranque o a otra carpeta de la cola*; c) ha terminado; d) tiene un error de formato | Entera (§ 1) |
| 4 | Teoría | En el Proxy Generator, *Start* y *Stop* se alternan con: a) Intro; b) *la barra espaciadora*; c) Ctrl+R; d) no se pueden alternar | Entera (§ 1) |
| 5 | Teoría | Entre las tareas que Resolve permite mandar al segundo plano están: a) el etalonaje y la mezcla; b) *la transcripción y la generación de proxies*; c) la ingesta de cinta; d) la captura SDI | Entera (§ 1) |
| 6 | Práctica | Una estación con Resolve gratuito intenta mandar un trabajo de *render* remoto a otra con Studio: a) funciona con marca de agua; b) *no funciona: las dos deben tener Studio*; c) funciona si comparten biblioteca; d) funciona si el volumen se llama igual | Entera (§ 1) |
| 7 | Teoría | Un fichero .mogrt puede crearse en: a) sólo After Effects; b) *Premiere o After Effects*; c) sólo Media Encoder; d) Resolve | Entera (§ 2) |
| 8 | Práctica | En Premiere se intenta exportar como plantilla un gráfico que llegó como .mogrt de After Effects: a) se exporta normalmente; b) *la opción no está disponible*; c) se exporta sin animación; d) se exporta como .xml | Entera (§ 2) |
| 9 | Teoría | Las plantillas .mogrt alimentadas por datos admiten: a) sólo texto; b) *texto, color y números*; c) texto e imágenes; d) cualquier tipo, cambiable en Premiere | Entera (§ 2) |
| 10 | Teoría | Una plantilla guardada en una biblioteca de Creative Cloud: a) hay que instalarla en *My Templates*; b) *está disponible en Premiere sin instalarla*; c) sólo funciona en After Effects; d) exige Media Encoder | Entera (§ 2) |
| 11 | Teoría | En Resolve, si el campo de metadatos que referencia una variable está vacío: a) aparece «%»; b) aparece «N/A»; c) *no aparece ningún carácter*; d) da error al renombrar | Entera (§ 2) |
| 12 | Teoría | Según la FAQ de MOS, de la creación, modificación y borrado de los objetos de medios y sus metadatos responde, en general: a) el NCS; b) *el MOS*; c) la automatización; d) el MAM | Entera (§ 4) |
| 13 | Teoría | ¿Qué mensaje MOS usa el servidor para «empujar» a la redacción información descriptiva y punteros? a) *Playlist Exchange*; b) *Status Exchange*; c) *Descriptive Data for Media Objects* (correcta); d) *Running Order* | Entera (§ 4) |
| 14 | Práctica | Cae el sistema de redacción a media hora del informativo. Según la tabla de degradación del tema: a) se suspende la emisión; b) *escaleta en papel y operación manual: se pierde automatismo, no la emisión*; c) se pasa a un estudio alternativo; d) se emite desde archivo | Entera (§ 5) |
| 15 | Teoría | Los mensajes del protocolo MOS se codifican en: a) XML; b) JSON; c) SDP; d) binario MXF. Clave sin fijar: la FAQ leída sólo dice «tagged text unicode format», y el formato concreto de los mensajes está en la especificación, no leída (no se da la clave de memoria) | A medias: el tema da el objetivo literal «tagged text unicode format», pero no nombra el formato y declara no leída la estructura de los mensajes (§ 4 y «no da») |

Resultado: 14 enteras, 1 a medias, 0 no.

## Tras el remate (segunda pasada, 25-09-2026)

15: entera. Clave fijada con la especificación MOS 2.8.5 y 4.0: *a) XML* (§ 4, «En qué va escrito cada
mensaje»). Pregunta 1: además, la frase siguiente a la tabla del § 5 da ahora la salvedad de lista no
cerrada. Resultado: 15 enteras.
