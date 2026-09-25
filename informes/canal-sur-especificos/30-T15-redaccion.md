# Puesto 30 · Tema 15 · Redacción (fase 2)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Se escribe según avanza.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/15-organizacion-nomenclatura-trazabilidad-colaboracion.md`.
Material: `30-investigacion-B-montaje.md` (§ Tema 15; y 5.2 y 14.3 para código de tiempo y versiones).
Común: Redactor/a T03 (cerrado). RTVE: `canal-sur-reuso/realizacion.tsv`, fila 30/15:
`edicion-montaje/07-avid-media-composer.md`, 10 %, actualizar «no», «Sólo organización de bins».

## Progreso

- Parte 1 guardada: portada, siglas, enunciado, preguntas, advertencia, ficha del puesto.
- Parte 2 guardada: 1 Organización de proyectos. Parte 3 guardada: 2 Nomenclatura.
- Parte 4 guardada: 3 Trazabilidad.
- Parte 5 guardada: 4 Buenas prácticas colaborativas.
- Parte 6 guardada: aplicación práctica, normativa, lo que no da, trazabilidad.
- Índice generado con `indice.py` (28 epígrafes, 6.523 palabras de cuerpo). `refutar_prosa.py`: 0 hallazgos.

## Fuentes releídas y fecha

Todas leídas el 25-09-2026 en su texto (local o web), no en el resumen de la investigación.

| Fuente | Qué se releyó |
|---|---|
| Avid *MC User's Guide* R8.0, 1999 (txt local) | pp. 35-36 (Attic), 41 (caracteres prohibidos), 72-74 (Managing Folders and Bins; guardado automático y manual), 88-89 (Naming Settings, no usado), 126-127 (Naming Tapes; esquema de nombres; truncado EDL), 261, 269-270 (vistas) |
| Avid *What's New* 2023.3 (txt local) | p. 2, Protect Project Bin |
| Avid *What's New* 2022.10 (txt local) | nota de refresco del candado en NEXIS EDGE: leída, no usada (detalle de versión) |
| Avid *Audio-Video Editing Workflows* 2010 (txt local) | pp. 11, 18, 19, 25 |
| Avid KB en275293 (descargada con curl) | texto completo |
| ELEMENTS blog, 24-01-2023 (descargado con curl) | «How does Bin Locking Work?», «The Backend», «Bin Locking Requirements» |
| SMPTE ST 377-1:2019 (txt local, frontal) | definiciones Package ID y UMID con su nota; referencia a ST 330:2011 |
| EBU Tech 3293 v1.10 (txt local) | 3.5, pp. 18-19 |
| Libro de Estilo CSTV 2004 (txt local) | 3.17.1.5 (p. 61), 5.3.3 (p. 81), 6.1, 6.1.1, 6.1.2 (pp. 88-89) |
| X Convenio, BOJA 240/2014 (txt local) | ficha 5212206, p. 190 |

## Correcciones y matices a la investigación

- ELEMENTS y Avid KB se releyeron en su HTML (la investigación los tenía por WebFetch). Cita de la KB:
  el original es «always create a backup of your projects and bins», con minúscula y precedida de
  «Before attempting any sharing or migration,»; no «Always create…».
- SMPTE: la definición de Package ID sigue «, or a value of 32 zero bytes used to terminate a reference
  chain»; se cita entera. Se añade la nota del UMID extendido de 64 bytes.
- Código de tiempo común con varias cámaras: 3.17.1.5, p. 61, sólo para la entrevista fuera de
  estudio con «dos o más cámaras ENG independientes»; el tema lo acota así.
- Material nuevo sobre la investigación (guía de 1999): caracteres prohibidos (p. 41), convención de
  mayúsculas, esquema de nombres, truncado en EDL y límite de 32 caracteres (pp. 126-127); guardado
  automático y manual (pp. 73-74); «Save these files as a template» (p. 73); cap. 9, p. 261; texto de
  las tres vistas (pp. 269-270). Ficha 5212206: tareas «Configurar sistemas…» y «Etiquetar…».
- Páginas de la guía de 1999: el número impreso en el txt marca el comienzo de página; comprobado
  contra el índice (Attic, p. 35).
- En el comentario del cierre de la copia de caracteres prohibidos, el txt da «|when» sin espacio; se
  respeta.

## Copiado del común

Pasajes copiados literal, byte a byte (comprobado con `diff`), de Redactor/a T03
(`temas/canal-sur-especificos/34-redactor-a/03-organizacion-redaccion-audiovisual.md`, cerrado). No se
re-verifican.

| Pasaje en T03 (líneas) | Dónde va en este tema |
|---|---|
| «Qué es, en el Libro de Estilo» (escaleta), cuerpo completo del epígrafe (270-278), sin su rótulo | 2 · «La escaleta, donde se fija el nombre de cada vídeo» |
| «Tres reglas obligatorias», cuerpo completo del epígrafe (282-293); rótulo igual | 2 · «Tres reglas obligatorias» |

Lo que sigue a esos bloques (frase «Si un vídeo se llama…», excepción de 6.1.1 en su letra, 6.1.2
primera frase) es nuevo y se verifica.

## Copiado de RTVE sin cambios

De `temas/edicion-montaje/07-avid-media-composer.md` (fila 30/15, actualizar «no»). Palabras sin tocar;
**sólo se han quitado las negritas** (allí marcaban la plantilla, aquí negrita = literal de fuente y
esos pasajes son oficio). El verificador comprueba sólo que es literal.

| Pasaje en RTVE (líneas) | Dónde va en este tema |
|---|---|
| Tabla de vistas del bin, Text / Frame / Script, con sus tres columnas (111-115) | 1 · «Las vistas del *bin*» |
| Fragmento «en Avid el proyecto y el material están separados. El proyecto guarda decisiones; el material vive aparte, en carpetas gestionadas por el programa.» (83-85) | 1 · «Qué guarda un proyecto y qué el material», tras una entrada propia |

## Adaptado de RTVE (sí se verifica)

- Tabla de vocabulario (RTVE 73-79): filas *Bin*, Secuencia, *Master clip*, *Subclip*, *Media*, con
  las dos primeras columnas literales; **se quitan** la columna «Cómo se llama en otros programas»
  (afirmaciones sobre otros programas sin fuente) y las filas *Settings* y *Command Palette* (no son
  organización de bins).
- No se copia lo propio de RTVE: respuestas oficiales y números de pregunta, distractores, plantilla,
  «cuadernillo», Dynamic Relink, Match Frame.

## Para el verificador

Todo lo demás es nuevo: citas de Avid (1999, 2010, 2023.3, KB), ELEMENTS, SMPTE ST 377-1, EBUCore,
Libro de Estilo (3.17.1.5, 5.3.3, 6.1.1 frase final y excepción, 6.1.2) y ficha 5212206. Lo marcado
«oficio» no tiene fuente y se dice. Ligaduras ﬁ del Libro de Estilo normalizadas a «fi».

## Ficheros tocados

- Creado: el tema 15 y este informe. Nada más.

## Preguntas tipo test (comprobación de cobertura antes de entregar)

Contestadas sólo con el tema. Las diez, **enteras**; no ha hecho falta ampliar.

1. (Organización, teoría) Según la guía de usuario de Media Composer, para limitar el número y la
   complejidad de los clips, los *bins* de un proyecto se organizan en tres juegos, que son los de:
   a) vídeo, audio y grafismo; b) **ingesta (digitalización), organización del proyecto y montaje** ✔;
   c) bruto, montaje y emisión; d) usuario, proyecto y sistema. → Epígrafe 1, «Los tres juegos». Entera.
2. (Organización, teoría) En la carpeta *Attic*, ¿cuál es la copia más reciente de un *bin*? a) La de
   extensión .lck; b) la de nombre sin número; c) **la de número de versión más alto** ✔; d) la de
   número más bajo. → 1, «Copias de seguridad». Entera.
3. (Nomenclatura, teoría) Según el Libro de Estilo, el nombre de un vídeo en escaleta: a) puede
   adaptarlo el montador si lo avisa; b) **debe respetarse por obligación, salvo que el vídeo se
   terminara antes de la escaleta, en cuyo caso el equipo de edición traslada a ella el nombre del
   autor o lo adapta** ✔; c) lo fija siempre el realizador; d) puede cambiarse en cada edición. → 2.
   Entera.
4. (Nomenclatura, aplicación) Un vídeo emitido en desconexión provincial con un nombre particular se
   pide para el informativo en cadena. El envío a los Servicios Centrales se identifica: a) con el
   nombre de la desconexión; b) con el nombre del fichero original; c) **con el nombre de la escaleta
   de cadena** ✔; d) con el que elija el centro. → 2, «El nombre en los informativos en cadena». Entera.
5. (Nomenclatura, teoría) Si el mismo nombre de cinta se teclea como TAPE, Tape y tape: a) el sistema
   los unifica; b) **aparecen como tres cintas distintas, con problemas para seguir la pista de los
   clips; hay que fijar una convención de mayúsculas** ✔; c) el sistema rechaza los dos últimos;
   d) sólo afecta a la EDL. → 2, «Reglas técnicas», regla 2. Entera.
6. (Trazabilidad, teoría) En MXF (SMPTE ST 377-1), cuando el UMID se usa como identificador de
   paquete: a) se usa el extendido de 64 bytes; b) **sólo el UMID básico de 32 bytes** ✔; c) uno de
   16 bytes; d) el nombre del fichero. ¿Qué norma define el UMID? SMPTE ST 330. → 3, UMID. Entera.
7. (Trazabilidad, teoría) Según el Libro de Estilo, cuando el material va a ser usado por terceras
   personas, la referencia de código de tiempo generalmente mejor es: a) el código de tiempo real;
   b) **poner el marcador a 00:00:00 al principio de la cinta** ✔; c) la hora de emisión; d) ninguna.
   → 3, «El código de tiempo». Entera.
8. (Trazabilidad, teoría) Según EBUCore (EBU Tech 3293), la mejor forma de identificar versiones de un
   programa es: a) añadir «final» al título; b) **usar relaciones como hasVersion o hasSource** ✔;
   c) cambiar el UMID; d) un fichero por soporte. → 3, «Las versiones». Entera.
9. (Colaboración, teoría) En un proyecto compartido con bloqueo de *bins*, el segundo usuario que abre
   un *bin* ya abierto: a) puede escribir y se fusionan los cambios; b) **lo abre en sólo lectura,
   con candado rojo, tal como estaba en el último guardado** ✔; c) no puede abrirlo; d) bloquea al
   primero. Y «Protect Project Bin» lo deja en sólo lectura para todos, incluido quien lo protege.
   → 4, bloqueo de *bins*. Entera.
10. (Aplicación práctica) Emitida la pieza del mediodía, hay que sacar una versión corta para la
    noche. Lo correcto es: a) recortar la secuencia emitida y guardarla encima; b) **duplicar la
    secuencia, darle nombre propio con su versión y dejar la emitida intacta en el *bin* de archivo** ✔;
    c) exportar un OMF; d) pedir el material de nuevo a documentación. → Aplicación práctica, paso 6;
    3, «Las versiones»; 1, *bin* de archivo. Entera.
