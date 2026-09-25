# Tema 15 del específico de Operador/a Montador/a de Vídeo · Organización de proyectos, nomenclatura, trazabilidad y buenas prácticas colaborativas

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Montador/a de Vídeo · punto 15 |
| Sirve para | Operador/a Montador/a de Vídeo de Canal Sur (grupo B04) y la prueba práctica del puesto |
| Fuente | Documentación de Avid Technology sobre Media Composer (*User's Guide* de 1999, *What's New* de la versión 2023.3, *Audio-Video Editing Workflows* de 2010 y un artículo de su base de conocimiento de 2023); Blackmagic Design, *DaVinci Resolve 21 Reference Manual* (2026), caps. 3 y 197; SMPTE ST 377-1:2019 (MXF); EBU Tech 3293, EBUCore v1.10 (2020); *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004; X Convenio Colectivo de la RTVA (BOJA núm. 240, de 10/12/2014), anexo III. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Documentos técnicos y de la casa en la edición indicada, leídos el 25-09-2026. No hay norma legal que regule la materia |
| Extensión | 8.000 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); Society of Motion Picture
and Television Engineers, Sociedad de Ingenieros de Cine y Televisión (SMPTE); European Broadcasting
Union, Unión Europea de Radiodifusión (EBU, UER en español); Material Exchange Format, formato de
intercambio de material (MXF); Unique Material Identifier, identificador único de material (UMID);
Advanced Authoring Format (AAF) y Open Media Framework (OMF), los dos formatos de intercambio de
composiciones; lista de decisiones de edición (EDL, *edit decision list*); código de tiempo (TC,
*timecode*); captación electrónica de noticias (ENG, *electronic news gathering*), la cámara
portátil de informativos; gestión de activos de medios (MAM, *media asset management*); red de área local (LAN, *local area
network*) y red de almacenamiento (SAN, *storage area network*), como las escribe Blackmagic.
Palabras que el tema usa en inglés porque así las rotula el programa: *bin* (la carpeta del proyecto
donde se guardan clips y secuencias), *master clip*, *subclip*, *settings*, *Attic*. «El Libro de
Estilo» es el de Canal Sur Televisión de 2004; «el convenio», el X Convenio Colectivo de la RTVA.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.30, punto 15): «Organización de
> proyectos, nomenclatura, trazabilidad y buenas prácticas colaborativas.»

Qué se puede preguntar: qué tareas de la ficha del puesto tocan la organización del material; qué
guarda un proyecto y qué el material en disco; cuántos proyectos conviene abrir y en qué tres juegos
de *bins* se organiza un proyecto según Avid; para qué sirven el *bin* de montaje en curso, el de
archivo, el de selección y el de cortes con formato; cuáles son las tres vistas de un *bin*; qué es la
carpeta *Attic*, qué extensión llevan sus copias y cuál es la más reciente; qué dice el Libro de Estilo
del nombre de un vídeo en escaleta y cuál es su única excepción; con qué nombre se envía a cadena un
vídeo emitido en desconexión; qué caracteres no deben usarse en nombres de proyectos y *bins*, por qué
hay que fijar una convención de mayúsculas y qué pasa con los nombres largos de cinta en una EDL; qué
es el UMID, cuántos bytes tiene el básico y qué norma lo define; qué lleva un fichero AAF y en qué se
diferencia de OMF; cómo describe EBUCore una versión; qué acuerdo de código de tiempo pide el Libro de
Estilo y por qué; cómo funciona el bloqueo de *bins* (quién escribe, colores del candado, fichero
.lck, requisitos de almacenamiento); qué hace «Protect Project Bin»; qué precauciones pide Avid al
compartir proyectos entre versiones; cómo se prepara una secuencia para sonido; y, en DaVinci Resolve 21, qué son las bibliotecas de
proyectos, qué hacen Live Save y las copias automáticas de proyecto y de *timeline*, qué pide y cómo
funciona el trabajo colaborativo (bloqueo de *bins*, *timelines* y clips, refresco, chat). En la prueba práctica:
organizar el proyecto de una pieza o de un programa, nombrar y versionar sus secuencias y entregarlas
sin perder la pista del material.

<!-- indice -->

## Índice

- [El punto en la ficha del puesto](#el-punto-en-la-ficha-del-puesto)
- [1. Organización de proyectos](#1-organización-de-proyectos)
  - [Qué guarda un proyecto y qué el material](#qué-guarda-un-proyecto-y-qué-el-material)
  - [Un proyecto por programa, episodio o pieza](#un-proyecto-por-programa-episodio-o-pieza)
  - [Los tres juegos de *bins*](#los-tres-juegos-de-bins)
  - [Las vistas del *bin*](#las-vistas-del-bin)
  - [Copias de seguridad del proyecto: la carpeta *Attic*](#copias-de-seguridad-del-proyecto-la-carpeta-attic)
  - [Lo mismo en un programa actual: DaVinci Resolve 21](#lo-mismo-en-un-programa-actual-davinci-resolve-21)
- [2. Nomenclatura](#2-nomenclatura)
  - [La escaleta, donde se fija el nombre de cada vídeo](#la-escaleta-donde-se-fija-el-nombre-de-cada-vídeo)
  - [Tres reglas obligatorias](#tres-reglas-obligatorias)
  - [El nombre en los informativos en cadena](#el-nombre-en-los-informativos-en-cadena)
  - [Reglas técnicas de nombres](#reglas-técnicas-de-nombres)
  - [Una convención para la sala (oficio)](#una-convención-para-la-sala-oficio)
- [3. Trazabilidad](#3-trazabilidad)
  - [El código de tiempo, referencia compartida](#el-código-de-tiempo-referencia-compartida)
  - [El identificador único del material: el UMID](#el-identificador-único-del-material-el-umid)
  - [Los metadatos de la secuencia: AAF y OMF](#los-metadatos-de-la-secuencia-aaf-y-omf)
  - [Las versiones y su origen](#las-versiones-y-su-origen)
- [4. Buenas prácticas colaborativas](#4-buenas-prácticas-colaborativas)
  - [Trabajar varios sobre el mismo proyecto: el bloqueo de *bins*](#trabajar-varios-sobre-el-mismo-proyecto-el-bloqueo-de-bins)
  - [El trabajo colaborativo en DaVinci Resolve 21](#el-trabajo-colaborativo-en-davinci-resolve-21)
  - [Compartir entre versiones del programa](#compartir-entre-versiones-del-programa)
  - [Entregar a sonido](#entregar-a-sonido)
  - [Avisar de los cambios](#avisar-de-los-cambios)
  - [Resumen de buenas prácticas](#resumen-de-buenas-prácticas)
- [Aplicación práctica: organizar una pieza de informativo](#aplicación-práctica-organizar-una-pieza-de-informativo)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

**Advertencia sobre las fuentes.** No hay norma legal sobre esta materia ni un documento publicado de
la RTVA que diga qué sistema de edición usa CSRTV, cómo se organizan sus proyectos o qué convención de
nombres de ficheros sigue. Lo que hay es de tres clases: la documentación de un fabricante de programas de
montaje, Avid, sobre su Media Composer (su guía de usuario completa es de 1999, y de ella se toman
los principios de organización, no los menús), completada con el manual vigente de otro programa,
DaVinci Resolve 21 de Blackmagic Design, para las copias automáticas y el trabajo colaborativo;
normas técnicas de la SMPTE y de la EBU para identificar material y
versiones; y el Libro de Estilo de 2004 y el convenio, que sí fijan reglas de la casa sobre el nombre
de los vídeos, el código de tiempo y las tareas del puesto. Otros programas de montaje organizan el
trabajo con piezas equivalentes con otros nombres (proyecto, carpeta, secuencia); este tema no los
cita porque no se ha leído su documentación. Qué programa usa CSRTV no consta. Lo que el tema dice como consecuencia práctica sin fuente
detrás va marcado como oficio.

## El punto en la ficha del puesto

La ficha del puesto (convenio, anexo III, código 5212206, BOJA núm. 240, p. 190) no usa las palabras
del enunciado, pero dos de sus ocho tareas son exactamente organización y nomenclatura:

- **«Configurar sistemas de edición y preparar los materiales a utilizar.»**
- **«Etiquetar, grabar e introducir en base de datos, la información para la emisión automatizada de
  programas y bloques publicitarios.»**

Y la coordinación está en su objeto: **«Realizar todo tipo de procesos de grabación, reproducción,
manipulación, edición y postproducción de la señal de audio y video con criterios técnicos y
artísticos, en coordinación con otras áreas.»** Preparar el material, etiquetarlo y trabajar con
otros sobre él son, por tanto, tareas del puesto, no un añadido (la ficha completa y el reparto con
las demás áreas, en el tema 9).

## 1. Organización de proyectos

### Qué guarda un proyecto y qué el material

Las piezas con que trabaja Media Composer, con el nombre que les da el programa (la guía de usuario
de 1999 dice que el *bin* contiene los *master clips*, enlazados a los ficheros de material, y las
secuencias y *subclips*, p. 66; que el *subclip* es un trozo marcado de un *master clip*, p. 211; y que
la carpeta del proyecto se guarda separada de los ficheros de material, p. 33):

| En Avid | Qué es |
|---|---|
| *Bin* | La carpeta donde viven los clips y las secuencias |
| Secuencia | El montaje: la línea de tiempo guardada como objeto |
| *Master clip* | El clip original vinculado a su material |
| *Subclip* | Un trozo marcado de un master clip |
| *Media* | El material en disco, separado del proyecto |

La idea que ordena todo lo demás: en Avid el proyecto y el material están separados. El proyecto guarda decisiones; el material vive aparte, en carpetas gestionadas por el programa.

Por eso organizar un proyecto es, sobre todo, organizar sus *bins*: el material no se mueve, lo que
se ordena son las referencias a él (oficio, a partir de esa separación).

### Un proyecto por programa, episodio o pieza

La guía de usuario de Media Composer (*User's Guide*, release 8.0, 1999, «Managing Folders and Bins»,
p. 72) plantea la organización así: **«You can use the Project window to create hierarchies of
folders and bins that reflect the specific workflow of the current project. This structure should
provide both simplicity and backup security.»** Es decir: la ventana del proyecto permite crear
jerarquías de carpetas y *bins* que reflejen el flujo de trabajo concreto de ese proyecto, y esa
estructura debe dar a la vez sencillez y seguridad de respaldo. Añade que los detalles **«can vary
depending upon your production needs and habits»** (varían según las necesidades y los hábitos de
cada producción), y da unos principios básicos.

El primero, limitar las secuencias de cada proyecto: **«Limit the number of sequences you create in
each project. For instance, consider creating one new project for each show, episode, spot, or
scene.»** Un proyecto nuevo por cada programa, episodio, anuncio o escena.

### Los tres juegos de *bins*

El segundo principio (pp. 72-73): **«Limit the number and complexity of clips in each bin by creating
and organizing bins in three groups»**, limitar el número y la complejidad de los clips de cada *bin*
repartiéndolos en tres grupos:

| Juego | Lo que dice la guía | Ejemplo que da |
|---|---|---|
| 1. Ingesta | **«Create a set of bins for the digitizing stage.»** | **«one bin for each source tape to be digitized to avoid slowing the system with large bins and causing confusion between tapes»**: un *bin* por cada cinta de origen, para no ralentizar el sistema con *bins* grandes ni confundir cintas |
| 2. Organización | **«Create a second set of bins for organizing your project.»** | **«a separate bin for each segment of a video project, depending upon the preferences of the editor»**: un *bin* por cada segmento o bloque, según las preferencias del montador |
| 3. Montaje | **«Create a third set of bins for the editing stage»** | Cuatro *bins*, en la tabla siguiente |

Los cuatro *bins* de la fase de montaje (p. 73):

| *Bin* | Texto de la guía | Para qué |
|---|---|---|
| De montaje en curso | **«A current cut bin for storing each work in progress (sequence)»** | Cada secuencia en elaboración |
| De archivo | **«An archive bin for keeping the original version of each cut (sequence)»** | La versión original de cada montaje |
| De selección | **«A selects or storyboard bin for screening selected clips or cuts gathered from the source bins»** | Visionar los clips o cortes elegidos de los *bins* de origen |
| De cortes con formato | **«A format cuts bin for storing the final cuts with added format elements such as segment breaks, color bars and tone, slate, or countdown»** | Los montajes finales con los elementos de formato: cortes de bloque, barras y tono, claqueta o cuenta atrás |

La guía cierra con dos consejos más y la razón de todo (p. 73): crear, si se quiere, carpetas
adicionales, y **«Save these files as a template for future productions of a similar nature.»**
(guardar la estructura como plantilla para producciones parecidas). **«This hierarchy allows you to
have one set of bins available in the Project window during the digitizing and organizing phase, and
another set of bins available during editing to reduce clutter.»**: una jerarquía así permite tener a
mano un juego de *bins* en la fase de ingesta y organización, y otro durante el montaje, para reducir
el desorden.

**Aplicado a la sala de hoy (oficio).** La guía habla de cintas; con ficheros, el primer juego se
organiza igual por su origen: un *bin* por tarjeta, por cámara, por enlace o por envío de agencia. El
segundo, por bloques del programa o, en una pieza informativa, por tipo de material (totales,
recursos, archivo, grafismo). El tercero separa lo que se está montando de lo ya entregado: la
secuencia en curso, las versiones anteriores sin tocar, la selección y la versión de emisión. Una
plantilla de proyecto con esa estructura vacía, igual para todas las salas, hace que cualquier
compañero encuentre las cosas en el mismo sitio.

### Las vistas del *bin*

La misma guía dedica un capítulo entero a organizar con *bins* («Organizing with Bins», cap. 9) y
empieza por ahí: **«You can view bins in three different display views. You can rename, sort, sift,
duplicate, and delete clips and sequences.»** (p. 261): tres vistas y cinco operaciones con clips y
secuencias (renombrar, ordenar, filtrar, duplicar y borrar). Las tres vistas son **«Text view, Frame
view, and Script view»** (p. 269):

| Vista | Qué muestra | Para qué sirve |
|---|---|---|
| Text | Una tabla: una fila por clip y una columna por dato | Ordenar, buscar y ver metadatos: código de tiempo, duración, cámara |
| Frame | Un fotograma de cada clip, como contactos | Reconocer material de un vistazo |
| Script | Los fotogramas con espacio para escribir texto al lado | Montaje de ficción con guion: se anota qué dice cada toma |

Lo que dice de cada una la guía (pp. 269-270): en Text **«clips are displayed in a database text
format, using columns and rows»**, y las disposiciones de columnas se pueden guardar como vistas
propias; en Frame **«each clip is represented by a single picture frame, with the name of the
clip»**, y los fotogramas se pueden reordenar dentro del *bin*; en Script **«the system combines the
features of Text view with Frame view, and adds space for typing notes or script»**.

Para organizar, la vista de texto es la que más rinde (oficio): sus columnas (código de tiempo,
duración, cinta o fichero de origen, comentarios) permiten ordenar y filtrar, y una vista de columnas
guardada y común a toda la sala hace que todos lean los *bins* igual.

### Copias de seguridad del proyecto: la carpeta *Attic*

La guía de 1999 describe dos protecciones automáticas del trabajo:

- **Guardado automático** («Saving Bins Automatically», pp. 73-74): **«The Avid system automatically
  saves changes to your work on a regular basis during each session.»** La frecuencia se ajusta en
  los *settings* de *bin*. Cuando salta, **«Any open bins are updated with changes made since the last
  autosave»** y **«Copies of these bins are placed in the Attic folder as backup.»**
- **La carpeta *Attic*** («Retrieving Bin Files from the Attic Folder», pp. 35-36): **«The Attic
  folder, located at the top level of the Avid drive, contains backup files of each bin in a
  project.»** Contiene una carpeta por proyecto; **«The system adds the file name extension .bak plus
  a version number to the bin name. The bin file with the highest version number represents the
  latest copy of the bin file.»** (la copia más reciente es la de número de versión más alto).

Se recurre a ella en dos casos: **«When you want to replace current changes to a sequence or clip
with a previous version»** (volver a una versión anterior de una secuencia o clip) y **«When the
current bin file becomes corrupt»** (cuando el fichero del *bin* se corrompe). Y la guía aconseja el
guardado manual como refuerzo: **«You can manually save bins for added security — for example,
immediately after an important edit.»** (p. 74).

Salvedad: ubicación de la carpeta, extensión y número de copias son de la versión de 1999; cómo lo
hace la versión actual del programa no se ha comprobado en su documentación. El principio (copias
automáticas y numeradas de cada *bin*, además del guardado manual tras un cambio importante) es lo
que se estudia.

### Lo mismo en un programa actual: DaVinci Resolve 21

El manual vigente de DaVinci Resolve (*DaVinci Resolve 21 Reference Manual*, Blackmagic Design, 2026,
cap. 3, «Managing Projects and Project Libraries») da una organización y unas copias automáticas que
siguen los mismos principios con otras piezas.

**Bibliotecas de proyectos** (p. 82). Resolve no guarda cada proyecto como fichero suelto donde quiera
el usuario: **«DaVinci Resolve takes a more centrally organized approach to project management, using
project libraries.»** Se pueden crear varias, y el manual sugiere criterios: **«you might create one
project library each for each year in which you work. If you work on series television, you could
create multiple project libraries for each program you work on. Or, you could create separate project
libraries for each client you do work for.»**, aunque **«There's no hard and fast rule»**. Hay tres
tipos: local, en el propio equipo; de red, en otro ordenador de la red local, **«best for a facility
composed of multiple workstations in the same building working on the same material»**; y en la nube
(Blackmagic Cloud), para trabajar desde lugares distintos. Para pasar un proyecto a otro usuario se
exporta como fichero .drp (p. 78; el detalle, en el tema 3).

**Tres protecciones automáticas** (pp. 89-93), que se activan en las preferencias de usuario:

| Protección | Qué hace | Cómo se recupera |
|---|---|---|
| Live Save | **«incrementally save changes as you make changes to your project, with no user intervention required»**; viene activado por defecto y el manual lo recomienda (p. 90) | Es el propio proyecto, guardado al momento |
| *Project Backups* | Copias completas del proyecto a intervalos, con un esquema **«analogous to a GFS (grandfather father son) backup scheme»** (abuelo-padre-hijo: copias recientes, horarias y diarias que se descartan por orden de llegada); cada copia es un proyecto completo **«excluding stills and LUTs»** (p. 90) | Desde el gestor de proyectos; **«project backups are always opened as independent projects»**: no sobrescriben el original (pp. 90-91) |
| *Timeline Backups* | Copias periódicas de cada *timeline*, con el mismo esquema (p. 92) | **«Restoring a timeline backup does not overwrite your current timeline»**: vuelve como *timeline* nuevo con «Backup» añadido al nombre (p. 92) |

Por defecto se hace una copia cada 10 minutos, **«resulting in six backups within the last hour»**
(pp. 90 y 93); las copias van a una carpeta «ProjectBackup» del disco de trabajo, que se puede
cambiar a un volumen **«that better fits into your data backup methodology»** (p. 91). El número de
copias horarias y diarias que se guardan por defecto no se da aquí: el manual dice ocho y cinco en las
pp. 90-91 y dos y dos en la p. 93.

Y el guardado a mano sigue contando: cuando hay cambios sin guardar aparece la palabra «Edited» junto
al nombre del proyecto, que se vuelve amarilla pasados 15 minutos y roja pasados 30 (p. 89). Antes de un
cambio radical en un *timeline*, el manual aconseja fijar un punto de retorno: **«This can be done by
duplicating the timeline (which is generally the safest), or you can also manually set a backup point»**
(p. 92). Es el mismo consejo que la guía de Avid de 1999: copias automáticas, más guardado o duplicado
a mano en los momentos importantes.

## 2. Nomenclatura

### La escaleta, donde se fija el nombre de cada vídeo

Las reglas de nombres que la casa tiene publicadas están en el Libro de Estilo, dentro de la
escaleta (6.1, p. 88).

«**La escaleta es el documento básico en el que se plasma y ordena el contenido de un programa.
Expresa el hecho noticioso concreto, formato, número o clave por el que se identifica cada uno,
tiempo asignado, tiempo real, autor, procedencia (elaborado in situ o de otro origen),
identificación del presentador y cualquier otra acotación técnica que sea precisa (vídeo o colas,
gráfico, línea de lanzadera, plano y cámara del presentador, movimientos de cámara, elementos
visibles de plató...).**» (6.1).

«**La mayor parte de estos elementos se reflejan en los partes de emisión, que contemplan además
las vías de sonido, coleo del vídeo, rótulos, observaciones y el pie del texto de la noticia.**»

### Tres reglas obligatorias

1. **Los cambios se comunican a todos**: «**Cualquier cambio del contenido de la escaleta debe
   comunicarse, desde el origen de la decisión, inmediata y simultáneamente, a todas las personas
   y departamentos afectados.**»
2. **El nombre del vídeo no se toca** (6.1.1): «**Son inadmisibles los cambios en la
   identificación de un vídeo por la confusión y los errores que causan. El nombre de una noticia
   en escaleta debe respetarse por obligación.**» Única excepción: el vídeo terminado antes de
   elaborarse la escaleta, en cuyo caso es el equipo de edición quien traslada a ella el nombre
   que le dio el autor o lo adapta.
3. **El redactor deja su texto en la escaleta** (6.1.2): «**El redactor ha de fijar siempre en
   escaleta sus textos definitivos (incluidos los rótulos con su orden y ubicación precisa) y los
   pasos de locutor que le hayan sido asignados. Así quedan disponibles para el resto del equipo
   del programa y para posteriores ediciones de informativos.**»

La regla 2 tiene una frase más en el Libro de Estilo, que es la que más obliga al montador: **«Si un
vídeo se llama de un modo concreto, no podrá modificarse su denominación aleatoriamente.»** (6.1.1,
p. 88). Y la excepción, en su letra: **«La única excepción es si un vídeo ha sido terminado antes de
la elaboración de la escaleta, en cuyo caso es el equipo de edición quien está obligado a trasladar a
la misma el nombre asignado por el autor del trabajo o, en su caso, adaptarlo.»** El Libro de Estilo
da la razón de la regla, **«por la confusión y los errores que causan»** los cambios: el nombre es lo
que une el vídeo montado con su línea de escaleta, su parte de emisión y sus rótulos.

### El nombre en los informativos en cadena

Cuando un vídeo de un centro territorial va a los informativos en cadena, la nomenclatura la fija la
escaleta de cadena (6.1.2, pp. 88-89): **«Los centros territoriales deben ceñirse escrupulosamente a
la nomenclatura fijada en escaleta para los vídeos que se soliciten como aportación a los informativos
en cadena. Si se trata del mismo vídeo emitido previamente en desconexión, en idéntico soporte y con
un nombre particular, el envío a los Servicios Centrales debe identificarse con el nombre de la
escaleta de cadena, independientemente del método interno que se use para ello.»**

Dos consecuencias para la sala (oficio, a partir de ese texto): un mismo vídeo puede tener un nombre
en la desconexión y otro en la cadena, y lo que viaja a los Servicios Centrales lleva el de cadena;
y el «método interno» (cómo se nombran ficheros y secuencias dentro de cada centro) es libre, pero el
nombre que ve la cadena, no.

### Reglas técnicas de nombres

La documentación de Avid da cuatro reglas que valen para cualquier convención:

1. **Caracteres que no se deben usar.** Si se van a mover *bins* y proyectos de una plataforma a
   otra, en los nombres de proyectos, *bins* y usuarios: **«do not use the following characters /
   \ : * ? “ < > |when naming projects, bins, and users.»** (*User's Guide*, 1999, p. 41). El
   programa tiene una opción para impedirlos, **«Use Windows® compatible File Names»**, en los
   *settings* generales.
2. **Una sola convención de mayúsculas.** Al nombrar cintas, **«It is possible to have a single tape
   listed as several different tapes if you alter the case of the letters»**: si el mismo nombre se
   escribe TAPE, Tape y tape, aparecen tres cintas, y eso causa **«significant problems in keeping
   track of clips when batch digitizing, redigitizing, and generating an EDL. Choose a case convention
   and maintain it throughout a project.»** (pp. 126-127): problemas serios para seguir la pista de
   los clips al digitalizar por lotes, redigitalizar o generar una EDL. Elegir una convención y
   mantenerla en todo el proyecto.
3. **Un esquema de nombres pensado de antemano.** **«It is important that you devise a naming scheme
   for your tapes.»** Los nombres parecidos se ordenan juntos en el *bin*, pero cuesta distinguirlos
   cuando hay muchos; **«Name tapes based upon the amount and complexity of your source material.»**
   (p. 127).
4. **Nombres que sobrevivan al intercambio.** Si se va a generar una EDL para otro equipo, hay que
   comprobar antes sus especificaciones, porque **«Some edit controllers will truncate source tape
   names to as few as six characters»**, y eso puede hacer que el sistema identifique igual cintas
   distintas de nombre parecido, **«causing you to lose track of source material»** (p. 127).

La guía de 1999 pone además límites al nombre de cinta en la herramienta de digitalización:
**«Tape names must be alphanumeric characters (A to Z, 0 to 9). They can include uppercase and
lowercase characters. The maximum length of a name is 32 characters.»** (p. 126). Es un dato de esa
versión y de ese campo, no una regla general de nombres de fichero.

Para las secuencias, el ejemplo de Avid al preparar una mezcla de sonido es duplicarla y darle un
nombre que diga para qué es: **«Duplicate the finished video sequence and name it appropriately. For
example, Sequence_ForMix.»** (*Audio-Video Editing Workflows*, 2010, p. 25).

### Una convención para la sala (oficio)

No consta que CSRTV tenga publicada una convención de nombres de ficheros, clips o secuencias. Lo
que el oficio recomienda, y lo que se puede proponer en la prueba práctica si la piden, se deduce de
las reglas anteriores:

- El nombre de la pieza es el de la escaleta, sin variantes (regla de la casa).
- Un orden fijo de campos, del más general al más particular: fecha, programa o edición, nombre de la
  pieza, versión. La fecha en forma año-mes-día hace que el orden alfabético sea también el
  cronológico.
- Sin espacios, tildes ni los caracteres que el sistema rechaza; guiones o guiones bajos como
  separadores; una sola convención de mayúsculas.
- La versión, al final y numerada (v01, v02…) o con su destino (corta, sin locución, redes,
  subtitulada), nunca «final», «definitiva» o «buena», que dejan de ser ciertas en cuanto hay otra.
- El nombre del material de origen no se cambia: es la referencia que lo une a su fichero y a su
  archivo.

## 3. Trazabilidad

Trazabilidad, en montaje (definición de oficio, no de norma): poder reconstruir, de cualquier plano
emitido, de qué material sale, quién lo tocó y en qué versión se emitió; y, de cualquier material,
dónde se ha usado. Se apoya en cuatro cosas: el código de tiempo, los identificadores del material,
los metadatos de la secuencia y la relación entre versiones.

### El código de tiempo, referencia compartida

El Libro de Estilo lo trata como un acuerdo entre quien graba y quien va a montar (5.3.3, p. 81):
**«En cada grabación el código de tiempo es un acuerdo básico entre periodista y cámara, especialmente
cuando van a estar físicamente separados durante la cobertura y cuando hay poco margen para la
posterior elaboración del correspondiente vídeo. En este caso puede usarse un código de tiempo real
previamente acotado, aunque también puede ser recomendable es el TC poniendo el marcador a 00:00:00 al
principio de la cinta. Esta referencia es generalmente mejor, sobre todo cuando el material va a ser
usado por terceras personas.»** (la errata «recomendable es» está en el original). Y para la entrevista
**«realizada fuera de los estudios pero pensada para su emisión íntegra»**, si se graba con **«dos o
más cámaras ENG independientes»**, el realizador prevé que los planos sean compatibles, y el código de tiempo
es común (3.17.1.5, p. 61): **«El código de tiempo que se aplicará será
idéntico para facilitar el montaje final.»**

Para la sala (oficio): el código de tiempo es la dirección de cada cuadro. Una nota de un redactor
(«el total, de 00:03:12 a 00:03:40»), una lista de planos o una EDL sólo sirven si ese código es el
del material que tiene el montador; por eso no se regraba ni se recodifica el material sin conservar
su código original.

### El identificador único del material: el UMID

En el formato MXF, cada paquete de material se identifica con un UMID. La norma del formato, SMPTE ST
377-1:2019 (cláusula de definiciones), dice: **«UMID: Unique Material ID according to SMPTE ST 330.
When used as a Package ID, only the 32-byte long Basic UMID shall be used.»**, y define el
identificador de paquete como **«Package ID: A basic UMID to uniquely identify a Package, or a value
of 32 zero bytes used to terminate a reference chain.»** Añade en nota que **«Other MXF
specifications may also use the 64-byte long extended UMID, which consists of a 32-byte long basic
UMID and 32 bytes of metadata.»**

Lo que hay que retener:

| Dato | Valor |
|---|---|
| Qué es | Identificador único de material |
| Norma que lo define | SMPTE ST 330 (la ST 377-1 remite a su edición de 2011) |
| Norma que lo usa como identificador de paquete | SMPTE ST 377-1, formato MXF |
| UMID básico | 32 bytes; es el único que vale como identificador de paquete |
| UMID extendido | 64 bytes: el básico más 32 bytes de metadatos |

El contenido interno del UMID (cómo se forman sus campos) está en la SMPTE ST 330, que no se ha
leído; el tema no lo da. Para el montador la consecuencia es de oficio: el nombre de un fichero se
puede cambiar y repetir; el identificador que el sistema asigna al material, no, y es el que permite
reencontrarlo aunque el nombre cambie.

### Los metadatos de la secuencia: AAF y OMF

Una secuencia montada es, sobre todo, una lista de decisiones sobre el material. Así lo explica Avid
(*Audio-Video Editing Workflows*, 2010, p. 18): **«AAF (Advanced Authoring Format) and OMF (Open Media
Framework) are the two main industry-standard formats that you can use to exchange compositions and
media between different applications and platforms.»** El fichero exportado **«contains the editing
information (metadata) for the selected sequence, along with the video and audio media files for the
master clips within the sequence»**, y los ficheros de material **«can either be embedded or linked
with the AAF or OMF file»** (incrustados o enlazados). La imagen que usa el fabricante: **«media files
are the pieces of a puzzle and metadata is the set of instructions for assembling the puzzle.»** (los
ficheros son las piezas del puzle y los metadatos, las instrucciones para montarlo).

Entre los dos, Avid prefiere AAF (p. 19): **«AAF is a more comprehensive standard of exchange and
amongst many other media formats, it can also embed/refer to MXF media files which the OMF format
cannot.»** Y para el intercambio con sonido: **«The key to maintaining a high level of
interoperability between Media Composer and Pro Tools is to use an AAF file.»** (p. 11).

Para la trazabilidad (oficio): mientras el material conserve su identificación, la secuencia exportada
lleva la cuenta exacta de qué trozo de qué fichero se usó; perdida esa identificación (material
renombrado a mano, recodificado sin sus metadatos), la secuencia ya no sabe reconstruirse.

### Las versiones y su origen

La EBU, en su conjunto de metadatos EBUCore (EBU Tech 3293, v1.10, Ginebra, abril de 2020, 3.5
«How can I describe versions of programmes?», pp. 18-19), explica por qué un programa es versión de
otro: **«There can be many reasons why a programme is declared to be a version of a particular source
(e.g. a shorter version, a different language, with or without captioning, but also available on
different mediums such as a file, a tape, a disk).»** (una versión más corta, en otra lengua, con o
sin subtítulos, o en otro soporte). Y cómo se identifican: **«The best approach to identify versions
is to use relations such as hasVersion or hasSource. The relation links two instances and their
respective descriptions highlighting differences such as given above as examples.»** Las relaciones
*hasVersion* («tiene versión») y *hasSource* («tiene fuente») enlazan las dos piezas y sus
descripciones, y señalan en qué se diferencian.

En la sala, eso se traduce así (oficio, apoyado en las fuentes citadas):

- La versión original no se sobrescribe: Avid la guarda en su *bin* de archivo, **«for keeping the
  original version of each cut»** (1999, p. 73), y para una entrega distinta duplica la secuencia y
  la nombra por su destino (**«Sequence_ForMix»**, 2010, p. 25).
- Cada versión (corta, sin locución, subtitulada, para desconexión, para redes) es una secuencia
  distinta, con nombre propio y ligada a la que la originó.
- Lo que va a cadena se nombra como la escaleta de cadena (6.1.2, epígrafe 2).
- Los metadatos de la pieza (título, versión, autor, fecha, destino) se introducen en la base de datos
  del sistema, que es la tarea de la ficha **«Etiquetar, grabar e introducir en base de datos»**; el
  sistema de gestión de activos y su flujo, en el tema 13; los metadatos de archivo, en el tema 8.

## 4. Buenas prácticas colaborativas

### Trabajar varios sobre el mismo proyecto: el bloqueo de *bins*

Cuando varias salas comparten un proyecto en almacenamiento común, el riesgo es que dos personas
modifiquen a la vez la misma secuencia y una sobrescriba a la otra. Media Composer lo resuelve
bloqueando *bins*. La mecánica la explica un fabricante de almacenamiento compatible (ELEMENTS, «Bin
Locking Overview and Troubleshooting in Avid Media Composer», Filip Milovanovic, 24-01-2023; fuente
secundaria, de un tercero):

- **«Avid Bin Locking functions work on a first come, first served basis. The first user that opens a
  bin in Media Composer will be granted write access.»** El primero que abre el *bin* puede escribir.
- **«A green padlock symbol inside the bin indicates that the user has write access.»** Si un segundo
  usuario abre el mismo *bin*, **«they will receive read-only access indicated by a red padlock»**, y
  lo ve **«as it was when it was last saved»** (como estaba en el último guardado).
- El bloqueo se apoya en ficheros auxiliares en la carpeta del proyecto, con el mismo nombre que el
  *bin*: **«The .lck file is created when a bin is opened.»**, y un fichero .log con la lista de
  modificaciones.
- Requisito: **«To use Avid Bin Locking, the storage that the project and the media files are stored
  on must support this feature.»** El bloqueo no lo da el programa solo: lo da el programa sobre un
  almacenamiento que lo admita. Y no todas las licencias lo incluyen: según el mismo artículo (de
  2023), lo tienen Media Composer Ultimate, Enterprise y Media Composer con licencia perpetua, y no
  Media Composer First ni la suscripción más extendida.

La documentación de Avid (*What's New for Avid Media Composer v2023.3*, p. 2) confirma el principio y
añade una orden: **«When you lock a shared project bin in Media Composer, it prevents other users from
making changes to that bin. With the new “Protect Project Bin” command, which is accessed by
right-clicking on a shared bin icon in the Bin Container, the bin is made read only for all users,
even for the user protecting it. Owners of a locked bin (“Lock Project Bin”) see a green bin icon.
However, when a user chooses to “Protect Project Bin”, it will appear red, even for that user, and
will always open as locked. Once the bin is closed, the user who originated the “Protect Project Bin”
command can choose to “Unlock Project Bin” using the same context menu.»**

| Orden | Efecto | Color para su dueño |
|---|---|---|
| «Lock Project Bin» | Impide que los demás cambien el *bin* | Verde |
| «Protect Project Bin» | Sólo lectura para todos, también para quien lo protege; siempre se abre bloqueado | Rojo |
| «Unlock Project Bin» | Quien lo protegió lo libera, con el *bin* cerrado | — |

Lo que se deduce para el trabajo diario (oficio): cada montador trabaja en sus propios *bins* y abre
los compartidos sólo para leer o coger material; la versión emitida o entregada se protege para que
nadie la toque por error; y un *bin* abierto innecesariamente bloquea a los compañeros.

### El trabajo colaborativo en DaVinci Resolve 21

Resolve resuelve el mismo problema con la misma idea, y lo documenta en su manual vigente
(*DaVinci Resolve 21 Reference Manual*, cap. 197, «Collaborative Workflow», pp. 4327-4339).

**Requisitos** (p. 4329). Todos trabajan sobre un proyecto guardado **«either in the Blackmagic Cloud,
or on a properly configured remote project library server»**; ese servidor debe estar en un ordenador
**«that is never shut down or put to sleep»**; todos los equipos en red, en la misma LAN o en subredes
distintas; y el material, idealmente, en
una SAN a la que estén conectados todos, **«so that every workstation that's connected to the project
being collaborated on has direct access to the same media»**.

**Activación** (p. 4330). Con el proyecto abierto, **«choose File > Multiple User Collaboration»**.
Aparecen dos botones nuevos, el del chat de colaboración y el de la lista de colaboradores. Y el
programa cambia dos ajustes por su cuenta: desactiva la opción «Auto conform missing clips as media is
added to Media Pool», **«as it interferes with collaborative workflow»**, y activa Live Save **«to ensure
that all collaborators' work is saved regularly to avoid conflicts between collaborators»**; con la
colaboración activa, Live Save no se puede desactivar (cap. 3, p. 90). Los proyectos colaborativos
llevan una insignia en su miniatura del gestor de proyectos (p. 4331).

**Cómo funciona** (p. 4332): **«collaborative workflow uses a "first come, first served" model»**.
Quien primero selecciona un *bin*, abre un *timeline* o selecciona un clip en las páginas Fusion o
Color obtiene el bloqueo; los demás lo ven, marcado con una insignia de color del colaborador,
**«but they cannot make changes. This prevents versioning conflicts from occurring.»**

| Pieza | Cómo se bloquea | Qué pueden hacer los demás |
|---|---|---|
| *Bin* | Al abrirlo o seleccionarlo; se libera al seleccionar otro *bin* o *timeline* (pp. 4332-4333) | Ver su contenido, sin cambios de organización ni de montaje; sí composiciones en Fusion y correcciones de color (p. 4333) |
| *Timeline* | Al abrirlo (p. 4335) | Verlo; sí pueden cambiar el *bin* donde está (p. 4335) |
| Clip, en Fusion o en Color | Al seleccionarlo; se libera y se registra al seleccionar otro (p. 4335) | Un compositor y un colorista a la vez sobre el mismo clip, porque los bloqueos son separados (p. 4335) |

Al liberarse, los cambios **«are "checked in" and made available to all collaborators once they
refresh their project»**, pulsando un icono circular de refresco junto al *bin* o en el visor. Todo se
guarda automáticamente, pero cada uno decide cuándo refrescar, para no ver cambiar el trabajo mientras
trabaja (p. 4332).

**Bloqueos a mano** (pp. 4334-4335). «Lock Bins» mantiene bloqueados los *bins* elegidos aunque se
deje de seleccionarlos, hasta «Unlock Bins». Al revés, Opción-clic abre un *bin* en sólo lectura (una
insignia con un ojo): se mira sin bloquear a nadie. Y los *timelines* se bloquean o desbloquean con
«Lock Timeline» y «Unlock Timeline».

**Organización para varios montadores** (pp. 4338-4339). Como sólo quien abrió primero un *timeline*
puede cambiar su montaje, el manual aconseja dividir el programa en «reels»: **«each reel of a project
is a separate timeline in a separate bin»**. Si dos montadores deben tocar el mismo *timeline*, uno lo
duplica en un *bin* propio, trabaja otra parte, avisa por el chat, y el otro compara con «Compare With
Current Timeline» y acepta los cambios. Y ayudantes y montadores se reparten los *bins*: **«your
project should be organized so that an editor can lock the contents of the bins they need to work
with at a given point in time, while the assistants can work on additional timelines and media within
other bins in that project.»**

Lo que coincide con Media Composer (oficio, de comparar las dos fuentes): el primero que llega
escribe, los demás leen; y cada montador trabaja en sus propios *bins*.

### Compartir entre versiones del programa

La base de conocimiento de Avid («Precautions when sharing projects and bins between different
versions of Avid Media Composer», actualizada el 11-08-2023) pide cinco precauciones antes de pasar
un proyecto o un *bin* de una versión del programa a otra:

1. Comprobar la compatibilidad de versiones: **«Different versions of Media Composer might have
   changes in file formats, features, and settings.»** Y, con formatos nuevos saliendo constantemente:
   **«ensure the media is captured or transcoded into a format that is shared between the two
   respective versions.»** (capturar o transcodificar el material en un formato que tengan las dos
   versiones).
2. Complementos de terceros: que estén instalados en los dos equipos, y atención también a sus versiones.
3. Efectos: limitar los que la versión más antigua pueda no tener.
4. Material disponible: **«Users will need to have access to all of the media files that are used in
   the project.»** Si no, **«the project or bin may not open properly»**; incluye el material local de
   un equipo, las transcodificaciones, el material enlazado y las plantillas de títulos propias.
5. Copia de seguridad: **«Before attempting any sharing or migration, always create a backup of your
   projects and bins.»**

El mismo artículo recuerda que en una secuencia sólo de cortes la información
de clips, *subclips* y secuencia **«are nearly identical between versions»**: lo delicado son
efectos, complementos y material.

### Entregar a sonido

El flujo de Avid para pasar un montaje a la mezcla de sonido (*Audio-Video Editing Workflows*, 2010,
p. 25) resume tres buenas prácticas de entrega:

- Carpetas de intercambio con sentido: **«We recommend that you create at least two folders for the
  exported sequence files—for example, one labeled ‘To Audio Editor’ and the other ‘From Audio
  Editor’.»** (una «hacia sonido» y otra «desde sonido»).
- La secuencia que se entrega es un duplicado con nombre propio (**«Sequence_ForMix»**, epígrafe 2),
  no la de trabajo.
- El intercambio se hace con AAF (epígrafe 3).

### Avisar de los cambios

La regla de la casa sobre cambios (Libro de Estilo, 6.1, copiada en el epígrafe 2) vale también para
la sala: un cambio se comunica **«desde el origen de la decisión, inmediata y simultáneamente, a todas
las personas y departamentos afectados»**. Con quién se coordina el montador y por qué canal, en el
tema 9.

### Resumen de buenas prácticas

| Práctica | Apoyo |
|---|---|
| Un proyecto por programa, episodio o pieza | Avid, 1999, p. 72 |
| *Bins* en tres juegos: ingesta, organización, montaje | Avid, 1999, pp. 72-73 |
| Estructura guardada como plantilla | Avid, 1999, p. 73 |
| Guardar a mano tras un cambio importante; copias automáticas | Avid, 1999, p. 74 |
| No cambiar el nombre del vídeo fijado en escaleta | Libro de Estilo, 6.1.1 |
| En cadena, el nombre de la escaleta de cadena | Libro de Estilo, 6.1.2 |
| Sin caracteres prohibidos y con una sola convención de mayúsculas | Avid, 1999, pp. 41 y 126-127 |
| Código de tiempo acordado y común | Libro de Estilo, 5.3.3 y 3.17.1.5 |
| La versión original no se toca; cada versión, secuencia propia | Avid, 1999, p. 73; 2010, p. 25; EBUCore 3.5 |
| Intercambio con AAF | Avid, 2010, pp. 11 y 19 |
| Trabajar en *bins* propios; proteger lo entregado | Avid, 2023.3, p. 2 (oficio en la aplicación) |
| Copia de seguridad antes de compartir o migrar | Avid, base de conocimiento, 2023 |
| Material en un formato común a las versiones que lo comparten | Avid, base de conocimiento, 2023 |
| Copias automáticas del proyecto y del *timeline*; duplicar antes de un cambio radical | Resolve 21, cap. 3, pp. 90-92 |
| Un *timeline* por «reel» en su propio *bin*; refrescar para ver los cambios ajenos | Resolve 21, cap. 197, pp. 4332 y 4338 |
| Avisar de los cambios a todos los afectados | Libro de Estilo, 6.1 |

## Aplicación práctica: organizar una pieza de informativo

Supuesto (oficio): llega a la sala el material de una noticia —dos tarjetas de cámara, una entrevista
y archivo— para el informativo del mediodía, con versión corta para la edición de la noche y un clip
para redes. Cómo se organiza de principio a fin, aplicando lo anterior:

| Paso | Qué se hace | Por qué |
|---|---|---|
| 1 | Abrir el proyecto del programa o de la pieza desde la plantilla de la sala | Un proyecto por programa o pieza; misma estructura para todos |
| 2 | Un *bin* por origen: tarjeta 1, tarjeta 2, archivo | Primer juego de *bins*; no mezclar orígenes |
| 3 | Un *bin* de selección con los totales y recursos elegidos | Juego de montaje: *bin* de selección |
| 4 | La secuencia con el nombre de la escaleta, sin variantes | Libro de Estilo, 6.1.1 |
| 5 | Guardar a mano después de cada cambio importante | Guía de Avid; copias en *Attic* |
| 6 | Entregada la versión de emisión, duplicarla para la versión corta y para redes, cada una con su nombre y su versión; la emitida, al *bin* de archivo y protegida | Versiones como piezas distintas ligadas a su fuente (EBUCore); no sobrescribir la original |
| 7 | Si la pieza va a cadena, el envío con el nombre de la escaleta de cadena | Libro de Estilo, 6.1.2 |
| 8 | Si hay mezcla de sonido, duplicado «para mezcla» exportado en AAF a la carpeta de intercambio | Flujo de Avid |
| 9 | Introducir título, versión, autor y destino en la base de datos | Tarea de la ficha del puesto |
| 10 | Avisar de cualquier cambio de nombre, duración o versión a quien lo reciba | Libro de Estilo, 6.1 |

Errores típicos que un supuesto puede plantear (oficio): una secuencia llamada «final» de la que hay
tres; un vídeo renombrado en la sala que ya no casa con su línea de escaleta; material regrabado sin
su código de tiempo; dos montadores sobre el mismo *bin* sin bloqueo; una versión corta hecha
recortando la secuencia emitida en lugar de un duplicado.

## Normativa que el tema invoca

No hay norma legal. Normas técnicas citadas:

- SMPTE ST 377-1:2019, *Material Exchange Format (MXF) — File Format Specification*: definición del
  UMID y del identificador de paquete. Remite a SMPTE ST 330:2011, *Unique Material Identifier
  (UMID)*, no leída.
- EBU Tech 3293, *EBUCore Metadata Set*, v1.10 (abril de 2020): descripción de versiones.

## Lo que este tema no da, y dónde está

- **Qué sistema de edición y de almacenamiento compartido usa CSRTV**, y si tiene una convención de
  nombres, una plantilla de proyecto o un protocolo de trabajo compartido: no consta en un documento
  publicado. El tema usa Media Composer porque es el programa cuya documentación se ha leído.
- **Cómo hace hoy Media Composer las copias automáticas** (ubicación de *Attic*, extensión, número de
  copias): la guía leída es de 1999; la guía vigente del programa no se ha localizado. Las copias
  automáticas de un programa actual se dan con DaVinci Resolve 21.
- **Menús y órdenes de otros programas de montaje** (Adobe Premiere y otros): no se ha leído su
  documentación para este tema. De Resolve sólo se dan los capítulos 3 (proyectos y copias) y 197
  (colaboración); la configuración del servidor de bibliotecas de proyectos y de Blackmagic Cloud,
  no.
- **La estructura interna del UMID**: SMPTE ST 330, no leída.
- **Proyectos, *bins*, *timeline*, códecs, *proxies*, conformado y exportación**: tema 3.
- **Ingesta, verificación, copias de seguridad del material, metadatos y archivo**: tema 8.
- **Coordinación con las demás áreas**: tema 9.
- **Automatización, plantillas, MAM y sistemas de redacción**: tema 13.
- **Urgencia y versionado bajo presión**: tema 14.
- **El Libro de Estilo es de 2004** y habla de cinta; si ha sido sustituido por otro criterio de la
  casa, no consta en un documento publicado leído.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| Avid Technology, *Avid Media Composer User's Guide*, Release 8.0 for the Macintosh, Part 0130-04015-01 Rev. A, mayo de 1999: pp. 33, 66 y 211 (proyecto, *bin*, *subclip*), 35-36 (*Attic*), 41 (caracteres), 72-74 («Managing Folders and Bins», guardado automático y manual), 126-127 (nombres de cinta), 261 y 269-270 (cap. 9, vistas del *bin*) | Organización del proyecto y de los *bins*, vistas, copias de seguridad, reglas de nombres | 25-09-2026 |
| Avid Technology, *What's New for Avid Media Composer v2023.3*, p. 2 | «Lock», «Protect» y «Unlock Project Bin» | 25-09-2026 |
| Avid Technology, *Avid Audio-Video Editing Workflows*, 2010: pp. 11, 18, 19 y 25 | AAF y OMF, metadatos de la secuencia, carpetas de intercambio, duplicado «Sequence_ForMix» | 25-09-2026 |
| Avid Knowledge Base, «Precautions when sharing projects and bins between different versions of Avid Media Composer», act. 11-08-2023, https://kb.avid.com/pkb/articles/en_US/user_guide/en275293 | Precauciones al compartir entre versiones | 25-09-2026 |
| ELEMENTS, «Bin Locking Overview and Troubleshooting in Avid Media Composer», Filip Milovanovic, 24-01-2023, https://elements.tv/blog/bin-locking-overview-and-troubleshooting-in-avid-media-composer/ (fuente secundaria) | Mecánica del bloqueo: primero en llegar, candados, .lck, requisitos de almacenamiento y de licencia | 25-09-2026 |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual* (PDF de julio de 2026): cap. 3, pp. 78, 82 y 89-93 (fichero .drp, bibliotecas de proyectos, Live Save, *Project Backups*, *Timeline Backups*); cap. 197, pp. 4327-4339 («Collaborative Workflow») | Bibliotecas de proyectos, copias automáticas y trabajo colaborativo en un programa actual | 25-09-2026 |
| SMPTE ST 377-1:2019, cláusula de definiciones y referencias normativas | UMID e identificador de paquete | 25-09-2026 |
| EBU Tech 3293, EBUCore v1.10, Ginebra, abril de 2020, 3.5 (pp. 18-19) | Versiones, *hasVersion* y *hasSource* | 25-09-2026 |
| *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004, ISBN 84-609-0453-9: 3.17.1.5 (p. 61), 5.3.3 (p. 81), 6.1, 6.1.1 y 6.1.2 (pp. 88-89) | Código de tiempo; escaleta y nombre del vídeo; nombre en cadena | 25-09-2026 (lo copiado del tema 3 de Redactor/a, leído allí el 24-09-2026) |
| X Convenio Colectivo de la RTVA, BOJA núm. 240, de 10/12/2014, anexo III, ficha 5212206 (p. 190) | Objeto y tareas del puesto | 25-09-2026 |
| Oficio | Aplicación a la sala, convención de nombres propuesta, definición de trazabilidad, supuesto práctico | — |
