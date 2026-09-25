# Tema 3 del específico de Operador/a Montador/a de Vídeo · Sistemas de edición no lineal

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Montador/a de Vídeo · punto 3 |
| Sirve para | Operador/a Montador/a de Vídeo de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Documentación de fabricante: Avid (*Media Composer User's Guide*, 1999; *What's New for Media Composer v2022.10* y *v2023.3*; *Avid DNxHD Technology*, 2012), Blackmagic Design (*DaVinci Resolve 21 Reference Manual*) y Adobe (ayuda de Premiere, páginas de 2025 y 2026). Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las versiones citadas, leídas el 25-09-2026; el temario no nombra programa y la ficha del puesto tampoco |
| Extensión | 9.200 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); sistema de edición no lineal (NLE, *non-linear editor*, como lo escriben
los fabricantes); código de tiempo (TC, *timecode*); lista de decisiones de edición (EDL, *edit
decision list*); formato avanzado de autoría (AAF, *Advanced Authoring Format*); formato de medios
abiertos de Avid (OMF, *Open Media Framework*); lenguaje de marcado extensible (XML), en el que
Premiere y Final Cut Pro exportan sus proyectos; formato abierto de línea de tiempo (OTIO,
*OpenTimelineIO*); formato de intercambio de material (MXF, *Material eXchange Format*) y los otros contenedores
que se nombran, AVI (*audio video interleave*), MP4 y MKV (de Matroska); paquete de cine digital
(DCP, *Digital Cinema Package*); formato
maestro interoperable (IMF, *Interoperable Master Format*); Society of Motion Picture and Television
Engineers (SMPTE); formato de vídeo QuickTime de Apple (MOV); códecs de Avid DNxHD y DNxHR y de Apple
ProRes; codificación avanzada de vídeo (H.264) y de alta eficiencia (H.265 o HEVC, *High Efficiency
Video Coding*); grupo de imágenes (GOP, *group of pictures*); definición estándar (SD), alta definición (HD) y ultra alta
definición (UHD); los formatos de vídeo digital DV y HDV y el de cinta HD HDCAM, que Avid usa como
término de comparación; alto rango dinámico (HDR); espacio de color de luminancia y diferencias de color
(YCbCr) y de primarios rojo, verde y azul (RGB); megabits por segundo (Mb/s, que Avid escribe Mbps); gestión de activos de medios (MAM, *media
asset management*) y de activos de producción (PAM, *production asset management*); formato de
imagen JPEG 2000 (JPEG2K en el manual de Resolve). LB y XQ no son siglas que se desarrollen aquí: son los nombres de variante que
dan los fabricantes (DNxHR LB, ProRes 4444 XQ).
En los nombres de órdenes y ventanas se conserva el rótulo inglés de cada programa, en cursiva la
primera vez: *bin* (carpeta de clips), *timeline* (línea de tiempo), *proxy* (copia ligera), *relink*
(reenlazar), *master clip* (clip maestro), *render* (cálculo de efectos).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.30, punto 3): «Sistemas de edición no
> lineal: proyectos, bins, timeline, códecs, proxies, conformado y exportación.»

Qué se puede preguntar: qué distingue la edición lineal de la no lineal; por qué el proyecto y el
material van separados y qué pasa cuando se pierde el enlace («Media Offline»); qué se fija al crear
un proyecto o una secuencia y qué no se puede cambiar después; cómo se llama el *bin* por defecto de
Resolve, qué muestra la *Media Tool* de Avid y cómo se localizan en un *bin* los clips sin material;
qué es un *master clip* y un *subclip*; qué es el *render* y cuándo hace falta; qué distingue formato
de codificación, códec y contenedor; qué es un códec intermedio o de masterizado (DNxHD, ProRes) y
para qué sirve DNxHD 36; qué es un *proxy*, en qué se diferencia de los medios optimizados de Resolve
y con qué material sale la exportación final; qué es el *offline* y el *online*; qué es conformar,
con qué ficheros se hace (EDL, AAF, XML) y qué datos usa el sistema para reenlazar (nombre de cinta o
bobina, código de tiempo, canales); qué hacen *Decompose* y *Consolidate* y para qué sirven las colas (*handles*); qué
distingue exportar el montaje (un fichero) de exportar el proyecto (AAF, EDL, XML); qué diferencia
hay entre la exportación directa y la cola de Media Encoder en Premiere, y entre *Single clip* e
*Individual clips* en Resolve. En la prueba práctica: crear el proyecto y la secuencia con los
parámetros del material, organizar los *bins*, montar con *proxies*, reenlazar material perdido y
exportar la pieza con el ajuste de entrega.

<!-- indice -->

## Índice

- [1. La edición no lineal](#1-la-edición-no-lineal)
  - [Lineal y no lineal](#lineal-y-no-lineal)
  - [Tres programas y una idea común](#tres-programas-y-una-idea-común)
- [2. Proyectos](#2-proyectos)
  - [Qué se decide al abrir un proyecto](#qué-se-decide-al-abrir-un-proyecto)
  - [Un proyecto por pieza o por programa](#un-proyecto-por-pieza-o-por-programa)
  - [Los parámetros del material mandan](#los-parámetros-del-material-mandan)
- [3. Bins](#3-bins)
  - [Qué es un *bin*](#qué-es-un-bin)
  - [En cada programa](#en-cada-programa)
  - [Encontrar lo que falta y lo que sobra](#encontrar-lo-que-falta-y-lo-que-sobra)
- [4. Timeline](#4-timeline)
  - [Qué es](#qué-es)
  - [Qué se fija al crearla](#qué-se-fija-al-crearla)
  - [Lo que la línea de tiempo avisa](#lo-que-la-línea-de-tiempo-avisa)
  - [El *render*](#el-render)
- [5. Códecs](#5-códecs)
  - [Formato de codificación, códec y contenedor](#formato-de-codificación-códec-y-contenedor)
  - [Códec de cámara, códec de montaje y códec de entrega](#códec-de-cámara-códec-de-montaje-y-códec-de-entrega)
  - [La familia DNxHD](#la-familia-dnxhd)
  - [Qué códecs ofrece un programa para *proxies* y medios optimizados](#qué-códecs-ofrece-un-programa-para-proxies-y-medios-optimizados)
  - [Por qué pesan los códecs de cámara al montar](#por-qué-pesan-los-códecs-de-cámara-al-montar)
- [6. Proxies](#6-proxies)
  - [Offline y online](#offline-y-online)
  - [Qué es un *proxy*](#qué-es-un-proxy)
  - [En cada programa](#en-cada-programa-1)
  - [*Proxies*, medios optimizados y caché: tres cosas distintas](#proxies-medios-optimizados-y-caché-tres-cosas-distintas)
  - [Para qué sirven en una redacción (oficio)](#para-qué-sirven-en-una-redacción-oficio)
- [7. Conformado](#7-conformado)
  - [Qué es conformar](#qué-es-conformar)
  - [Con qué datos se reconoce cada clip](#con-qué-datos-se-reconoce-cada-clip)
  - [Preparar el montaje antes de conformar](#preparar-el-montaje-antes-de-conformar)
  - [Volver a capturar: *Redigitize* y *Decompose* en Avid](#volver-a-capturar-redigitize-y-decompose-en-avid)
  - [Consolidar en Avid](#consolidar-en-avid)
  - [Reenlazar](#reenlazar)
  - [Antes de dar el conformado por bueno (oficio)](#antes-de-dar-el-conformado-por-bueno-oficio)
- [8. Exportación](#8-exportación)
  - [Dos cosas distintas que se llaman igual](#dos-cosas-distintas-que-se-llaman-igual)
  - [Premiere: exportación directa o cola de Media Encoder](#premiere-exportación-directa-o-cola-de-media-encoder)
  - [Resolve: la página *Deliver*](#resolve-la-página-deliver)
  - [Antes de exportar (oficio)](#antes-de-exportar-oficio)
- [Aplicación práctica: una pieza de principio a fin](#aplicación-práctica-una-pieza-de-principio-a-fin)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. La edición no lineal

### Lineal y no lineal

| | Edición lineal | Edición no lineal |
|---|---|---|
| Soporte | Cintas físicas | Archivos digitales |
| Cómo se monta | Copiando de una cinta a otra, en orden | Ordenando referencias a los archivos |
| Cambiar algo del medio | Obliga a rehacer desde ahí | No afecta a nada más |
| Acceso | Secuencial: hay que rebobinar | Aleatorio: cualquier fotograma, al instante |
| Generaciones | Cada copia pierde calidad | Ninguna pérdida: no se copia, se referencia |

La edición lineal utiliza cintas físicas, mientras que la no lineal se basa en archivos digitales:
es la diferencia de raíz, y todas las demás salen de ella. La palabra «lineal» no se refiere a la
duración ni al relato: se refiere al acceso. Una cinta se recorre en línea; un disco, no.

La fila de las generaciones tiene una salvedad: no se copia mientras se monta, pero sí se recodifica
cuando se calcula un efecto o se exporta la pieza (epígrafes 4 y 8), y por eso importa con qué códec
se trabaja (epígrafe 5).

### Tres programas y una idea común

El enunciado no nombra programa, ni la ficha del puesto tampoco, y qué sistema usa CSRTV no consta
en un documento publicado. El tema toma los tres cuya documentación se ha leído —Avid Media Composer,
DaVinci Resolve de Blackmagic Design y Adobe Premiere (Premiere Pro en las páginas de ayuda de 2025)— y se queda con lo que los
tres comparten. Cada uno llama a las cosas a su manera:

| Pieza | Media Composer | Resolve | Premiere |
|---|---|---|---|
| El trabajo guardado | Proyecto | Proyecto (.drp) | Proyecto |
| Carpeta de clips | *Bin* | *Bin* del *Media Pool* | *Bin* del panel Proyecto |
| El montaje | Secuencia | *Timeline* | Secuencia |
| El clip original | *Master clip* | Clip del *Media Pool* | Clip |
| Salida | *Export* | Página *Deliver* | *Export* / Media Encoder |

La idea común es que el proyecto y el material están separados. En Avid, el proyecto guarda
decisiones; el material vive aparte, en carpetas gestionadas por el programa. Resolve lo dice de su
página de material: **«It's central to the way DaVinci Resolve works that the source media used by a
project is organized separately from the project data that you import and manage in the Edit
page.»** (el material de origen se organiza aparte de los datos del proyecto; *Reference Manual*,
p. 21). Y la guía de Avid presenta su herramienta de material, la *Media Tool*, como la otra cara de
los *bins*: **«The Media tool is your window into the digitized video and audio data files stored on
your media drives. As an important counterpart to the bins, the Media tool provides similar database
tools for manipulating digital media files in tandem with your organization of clips and
sequences.»** (p. 321).

De esa separación salen casi todas las operaciones del tema: el clip del *bin* es una referencia;
si el fichero se mueve o se borra, la referencia queda sin material («Media Offline», epígrafe 7);
un *proxy* es otro fichero enlazado al mismo clip (epígrafe 6); conformar es rehacer esos enlaces
contra el material bueno (epígrafe 7); y un AAF o una EDL son las decisiones sin el material
(epígrafe 8).

## 2. Proyectos

### Qué se decide al abrir un proyecto

Lo primero que fija un proyecto es el formato de trabajo: tamaño de imagen y cadencia. Lo que se fija
aquí gobierna todo el montaje y, en los tres programas, no se cambia a mitad sin coste.

- Media Composer. Al crear un proyecto se eligen el *raster* (el tamaño de imagen) y la *edit
  rate* (la cadencia de montaje). Desde la versión 2022.10 hay una casilla «Choose For Me» para
  quien empieza: **«When this check box is selected, the project will not have a final Raster or Edit
  Rate set by default. Instead, when you add your first clip to the Timeline, Media Composer will
  prompt you with a "Project Properties" window and will automatically select settings that match
  your clip.»** (el proyecto no fija de entrada ni tamaño ni cadencia, y los toma del primer clip que
  se lleva a la línea de tiempo). Con esa opción el programa crea además dos *bins*: **«The green bin
  (representing the source side) is intended for clips, and the blue bin (representing the record
  side) is for storing your sequences.»** (el verde, lado de fuente, para los clips; el azul, lado de
  grabación, para las secuencias; *What's New v2022.10*, p. 17).
- Resolve. Los proyectos se crean y se ordenan dentro del propio programa, no en las carpetas
  del sistema: **«Ordinarily, the Project Manager is the first window you'll see when DaVinci Resolve
  starts up.»** y **«DaVinci Resolve requires you to do most project organization in the Project
  Manager.»** (p. 76). Para llevar un proyecto a otro equipo: **«DaVinci Resolve projects are saved
  with the file extension .drp and enable you to exchange files with other DaVinci Resolve users.»**
  (p. 78). La cadencia se fija con el material: al importar puede aparecer un aviso que ofrece
  adaptar el proyecto al material, y **«Once clips have been imported into the Media Pool, the frame rate
  cannot be changed again, so choose carefully.»** (una vez importados los clips, la cadencia ya no
  se puede cambiar; p. 375).
- Premiere. Lo que se fija es la secuencia (epígrafe 4). El proyecto la contiene, y puede
  contener varias: **«A single project can contain multiple sequences with different settings.»**
  (ayuda de Adobe, «Sequence presets and settings», actualizada el 22-08-2025).

### Un proyecto por pieza o por programa

La guía de Avid aconseja limitar las secuencias de cada proyecto y, como ejemplo, abrir uno por
programa, episodio, anuncio o escena (guía de 1999, p. 72); cómo se ordenan dentro sus *bins* está en el tema 15. En una redacción de
informativos esto se traduce, como costumbre de oficio, en proyectos de vida corta (uno por día o
por edición del informativo) y proyectos largos para los programas con continuidad. Lo que se decida
debe ser igual en todas las salas, para que cualquier compañero abra el proyecto de otro y encuentre
el material donde espera.

### Los parámetros del material mandan

El formato del proyecto se toma del material principal y del formato de emisión, no al revés. Adobe
lo explica así: **«Premiere Pro performs best when the settings for a sequence match the parameters
of most of the assets used in that sequence.»** Y enumera lo que hay que saber del material antes de
crear la secuencia: formato de grabación, formato de fichero, **«Frame aspect ratio»** (relación de
aspecto del cuadro), **«Pixel aspect ratio»** (del píxel), **«Frame rate»** (cadencia), **«Time
base»** (base de tiempo), **«Fields (for example, progressive or interlaced)»** (campos: progresivo
o entrelazado), la frecuencia de muestreo del audio y los códecs de vídeo y de audio. Todos esos
conceptos se estudian en los temas 2 y 4.

Material de otro formato puede convivir en el mismo montaje: Avid lo decía ya de sus sistemas de
montaje, en el documento de su códec DNxHD: **«Avid editing systems are designed for flexibility. They can handle HD, HDV, SD, and DV media at mixed frame rates in the same timeline, all playable
in real time.»** (*Avid DNxHD Technology*, 2012, apartado «Avid DNxHD mixed in the timeline»). Pero lo que no coincide con el proyecto se
convierte al vuelo o se calcula, y eso cuesta rendimiento y, a veces, calidad (oficio).

## 3. Bins

### Qué es un *bin*

El *bin* es la carpeta donde viven los clips y las secuencias. Lo que guarda no es el material sino
las referencias a él (epígrafe 1), con sus metadatos: nombre, código de tiempo de entrada y salida,
duración, cinta o fichero de origen, pistas, comentarios.

Dentro del *bin* hay dos clases de clip que la guía de Avid distingue así (p. 232):

- **«Master clips are linked to entire media files and serve as sources for subclips and
  sequences.»** El *master clip* está enlazado al fichero entero y es la fuente de los *subclips* y
  de las secuencias.
- **«Subclips are smaller sections of master clips.»** El *subclip* es un trozo del *master clip*:
  apunta al mismo material, acotado.

Por eso un cambio en el *master clip* alcanza a todo lo que sale de él (la misma página: si se
vuelve a capturar un *master clip* con otra compresión o con otros niveles, cambian todos sus
*subclips* y secuencias).

### En cada programa

- Media Composer. Los *bins* cuelgan de la ventana del proyecto, se agrupan en carpetas y se
  ven en tres vistas (*Text*, *Frame* y *Script*); la estructura aconsejada, las vistas y el bloqueo
  de *bins* compartidos se estudian en el tema 15. La *Media Tool* muestra el material en disco
  con los mismos recursos: **«The three display options in the Media tool function like those in
  bins: Frame view, Script view, and Text view.»** (p. 321).
- Resolve. Los *bins* están en el *Media Pool*: **«The Media Pool contains all of the video,
  audio, and still image media that you import into the current project. […] Ordinarily, all media
  imported into a project goes into the Master bin. However, your media pool can be organized into as
  many user-definable bins as you like, depending on your needs.»** (todo lo importado va al *bin*
  maestro, *Master*, y se reparte en tantos *bins* propios como se quiera). El mismo *Media Pool*
  **«also appears on the Edit, Fusion, Color, and Fairlight pages»** (aparece también en las páginas
  de montaje, composición, color y sonido; p. 23). Las líneas de tiempo también se guardan en un
  *bin*: **«Timelines you create are stored in the currently selected Media Pool bin.»** (p. 860).
- Premiere. Los *bins* están en el panel Proyecto: **«To add a new bin, right-click on the
  Project panel and select New Bin from the context menu, or Control + / (Windows) or command + /
  (macOS).»** Y se borran seleccionándolos y pulsando la tecla de borrar (ayuda de Adobe, «Add and
  delete bins», actualizada el 22-08-2025).

### Encontrar lo que falta y lo que sobra

Los *bins* de Avid tienen órdenes para saber qué material usa cada cosa (guía de 1999, pp. 285-287):

| Orden (menú *Bin*) | Qué hace |
|---|---|
| *Select Offline Items* | Marca los objetos sin material. **«Offline items are clips, subclips, or sequences that are missing some or all of their original media files or have never been digitized.»** (clips, *subclips* o secuencias a los que les falta todo o parte de su material, o que nunca se capturaron) |
| *Select Media Relatives* | Marca todo lo enlazado al clip elegido: sus *subclips* y las secuencias que lo usan |
| *Select Sources* | Marca todas las fuentes de un objeto: **«every master clip, subclip, tape, and media file that is a source for that sequence»** (cada *master clip*, *subclip*, cinta y fichero de los que sale la secuencia) |
| *Select Unreferenced Clips* | Marca los clips a los que no remite ningún clip ni secuencia de los *bins* abiertos: lo contrario de *Select Media Relatives* |

Sirven para dos tareas del día a día (oficio): antes de entregar, comprobar que ninguna secuencia
tiene material *offline*; y al cerrar un proyecto, saber qué material no se usó para no archivarlo
o para borrarlo.

## 4. Timeline

### Qué es

La línea de tiempo es la representación gráfica del montaje: pistas de vídeo arriba y de audio
debajo, con cada clip dibujado a lo largo del tiempo. La guía de Avid la presenta así: **«Your Avid
system represents each edit and effect in a graphical timeline structure to help you track and
manipulate the elements of your sequence. The Timeline continuously updates as you work»** (cada
corte y cada efecto se representan en una estructura gráfica que se actualiza mientras se trabaja;
p. 462). Lo que se guarda en el *bin* es la secuencia (Avid, Premiere) o el *timeline* (Resolve):
el mismo objeto con otro nombre.

### Qué se fija al crearla

- Premiere fija los parámetros al crear la secuencia, y algunos ya no se tocan: **«The sequence
  settings must be correct when you create the sequence. Sequence settings like time base are locked
  once the sequence is created.»** (los ajustes deben ser correctos al crearla; la base de tiempo,
  entre otros, queda bloqueada). Si hace falta otra base, la salida que da Adobe es crear una
  secuencia nueva con los ajustes buenos y pasar a ella el contenido. Para no equivocarse hay
  preajustes por formato de cámara (AVC-Intra, DVCPRO, XDCAM, entre otros) y se pueden guardar
  preajustes propios.
- Resolve hace que cada *timeline* copie los ajustes del proyecto: **«by default it will mirror
  the current project-wide timeline settings for resolution, frame rate, and other format and
  monitoring parameters.»** Pero admite *timelines* con ajustes propios de formato, monitorado,
  escalado de salida y color **«for situations where you need to set up multiple timelines to create
  multiple deliverables with different resolutions, pixel aspect ratios, frame rates»** (cuando hay
  que sacar varias entregas con distinta resolución, relación de aspecto del píxel o cadencia;
  p. 860). Es la vía para montar a la vez la versión horizontal y la vertical de una pieza (tema 12).
- Media Composer, desde la versión 2022.10, crea cada secuencia a partir de una plantilla:
  **«Whenever a new sequence is created, a sequence template will be used to configure the number and
  type of tracks, custom track names, and starting Timecode.»** (número y tipo de pistas, nombres de
  pista y código de tiempo de arranque; *What's New v2022.10*, p. 15). El código de tiempo inicial ya
  no está en los ajustes generales: **«Default Starting TC has been removed from General Settings and
  must now be configured in the Sequence Template.»** Una plantilla común para la sala deja todas las
  piezas con las mismas pistas y el mismo arranque (oficio).

### Lo que la línea de tiempo avisa

La línea de tiempo señala con color el material que falta. En Avid: **«You can choose to highlight
the clips in the Timeline that have offline media. The clips appear red, indicating their media is
offline.»** (los clips sin material se pintan de rojo; p. 470), aunque el material que falta esté
anidado muchas capas por debajo (p. 471). En Resolve, cuando se trabaja con *proxies* y falta el original,
**«a purple line on your timeline indicates the original media is missing»** (una línea morada
indica que falta el material original; p. 220).

### El *render*

Hacer *render* es el cálculo que el sistema de edición no lineal tiene que hacer en los efectos para
hacerlos visibles y utilizables.

Por qué hace falta. Un montaje sin efectos se reproduce leyendo los archivos y cortando entre ellos:
eso el ordenador lo hace al vuelo. Pero una transición, un rótulo, una corrección de color o una
composición no existen como archivo: hay que calcular cada fotograma. Cuando el cálculo no da tiempo
a hacerse mientras se reproduce, hay que hacerlo antes y guardarlo. Eso es renderizar.

Resolve lo organiza como caché de *render* con dos modos. El inteligente: **«Choosing Smart triggers
a variety of automatic caching behaviors designed to optimize playback in DaVinci Resolve by
rendering clip formats, grading operations, and timeline effects that are known to be
performance-intensive»** (calcula por su cuenta los formatos, correcciones y efectos que se sabe que
pesan); el de usuario, que **«does not automatically cache clips in processor-intensive formats»**
y deja al montador marcar qué se calcula (p. 209). Y separa la caché de los *proxies*: la caché
**«is designed to improve the real time performance of clips that have enough computationally
intensive effects […] to slow playback»** y **«only works with the project it was made for»** (sólo
sirve al proyecto para el que se hizo; p. 222). El *render* es, por tanto, material desechable: se
puede borrar y rehacer, y no se archiva como si fuera material de origen (oficio).

## 5. Códecs

### Formato de codificación, códec y contenedor

Tres cosas que se confunden y conviene separar:

| Concepto | Qué es | Ejemplos |
|---|---|---|
| Formato de codificación | El estándar que fija las reglas y operaciones matemáticas del algoritmo de compresión | H.264, HEVC, AV1, MPEG-2 |
| Códec | La implementación concreta de ese estándar en un programa que codifica y descodifica | x264, x265, el codificador de una cámara |
| Contenedor | El estándar para distribuir o almacenar el contenido: qué pistas hay, en qué orden, con qué metadatos | AVI, MOV, MP4, MXF, MKV |

Un formato contenedor es un estándar para la distribución o el almacenamiento de un determinado
contenido multimedia. Un formato de codificación es el estándar desarrollado que indica las reglas y
operaciones matemáticas que realiza un algoritmo de compresión. El resumen que hay que llevarse: el
estándar dice qué hay que hacer, el códec lo hace y el contenedor lo guarda.

En el lenguaje de la sala «códec» se usa también para la familia comercial (DNxHD, ProRes), que
reúne formato y codificador de un fabricante. Resolución, cadencia, muestreo, profundidad de bits,
compresión intra e inter, flujo binario y contenedores de entrega son materia del tema 4; aquí
interesa qué códec conviene en cada fase del montaje.

### Códec de cámara, códec de montaje y códec de entrega

Un mismo material pasa por códecs distintos según la fase, y cada uno responde a una necesidad
distinta (oficio):

| Fase | Qué se pide al códec | Ejemplos citados en este tema |
|---|---|---|
| Captación | Mucha calidad en poco espacio de tarjeta | Los formatos de cámara (AVC-Intra, XDCAM, H.264/H.265 de cámara) |
| Montaje y acabado | Aguantar decodificación rápida, efectos y varias generaciones sin degradarse | DNxHD y DNxHR, ProRes, sin comprimir |
| Montaje ligero | Poco flujo para reproducir con fluidez | DNxHD 36, ProRes Proxy, DNxHR LB, H.264 de *proxy* |
| Entrega | Lo que pida el destino: emisión, archivo o plataforma | Tema 4 y epígrafe 8 |

Avid explica así por qué no basta el códec de cámara: **«HD camera compression formats are
efficient, but simply aren't engineered to maintain quality during complex postproduction effects
processing. Uncompressed HD delivers superior image quality, but data rates and file sizes can stop a
workflow dead in its tracks.»** (los formatos de cámara son eficientes pero no están pensados para
mantener la calidad en una posproducción con efectos; el HD sin comprimir tiene la mejor imagen, pero
su flujo y el tamaño de los ficheros atascan el trabajo). Su respuesta es un códec intermedio pensado
para editar: **«Avid DNxHD encoding is specifically designed for nonlinear editing and complex
multi-generation compositing common in today's collaborative post production and broadcast news
environments.»** (*Avid DNxHD Technology*, 2012).

### La familia DNxHD

Datos del mismo documento de Avid (2012):

- Es de 8 y 10 bits y conserva el cuadro HD entero: **«Preserves the full raster of the original HD
  frame»**. Otros formatos comprimidos, como HDCAM y DVCPRO HD, submuestrean la trama horizontal
  (1.440 o 1.280 muestras en lugar de 1.920).
- Está normalizado: **«Codified by SMPTE as VC-3 standard»** (codificado por la SMPTE como norma
  VC-3).
- Sus variantes, de más a menos flujo:

| Variante | Para qué la da Avid |
|---|---|
| DNxHD 444 | 10 bits, muestreo 4:4:4 RGB, para acabado y masterizado de proyectos 1920x1080 progresivos |
| DNxHD 220x | 10 bits en YCbCr: 220 Mb/s en 1080 entrelazado a 30 cuadros; 175 Mb/s en progresivo a 24 |
| DNxHD 220 | La máxima calidad de imagen con fuentes de 8 bits; mismos flujos por cadencia que la 220x |
| DNxHD 145 | Masterizado de fuentes de 8 bits y flujo menor, como HDCAM y DVCPRO; a 25 cuadros progresivos, 120 Mb/s |
| DNxHD 100 | Donde pesan la velocidad y el espacio; submuestrea la trama (de 1.920 a 1.440 o de 1.280 a 960) |
| DNxHD 36 | **«High-quality offline editing of HD progressive sources only.»** Montaje *offline* de fuentes HD progresivas (epígrafe 6) |

El flujo depende de la cadencia: por eso el documento da cifras distintas a 24, 25 y 30 cuadros.
De DNxHR sólo consta aquí que Resolve lo ofrece como códec de trabajo (abajo); su documentación de
Avid no se ha leído.

### Qué códecs ofrece un programa para *proxies* y medios optimizados

Resolve 21 da el menú de códecs de trabajo en dos listas (pp. 213 y 202-203):

- Para *proxies*: **«There are several ProRes and DNxHR varieties to chose from, as well as H.264 and
  H.265 options. Which format you chose will be determined by the bandwidth and quality tradeoffs that
  you need for a particular project.»** (varias variantes de ProRes y DNxHR, y H.264 y H.265: se elige
  según el equilibrio entre flujo y calidad que pida el proyecto).
- Para medios optimizados: **«Options include Uncompressed 10-bit, and Uncompressed 16-bit float for
  maximum quality. Other options include ProRes Proxy through 4444 XQ, and DNxHR LB through 444.»**
  Y avisa de que no todos guardan lo mismo: para corregir color sin recortar, sobre todo en HDR,
  **«You should use 16-bit float, ProRes 4444, ProRes 4444 XQ, or DNxHR 444»** (p. 202); en la
  página siguiente, en cambio, el manual nombra sólo tres, sin DNxHR 444: **«any of these three codecs
  are appropriate optimized formats for HDR grading»** (16-bit float, ProRes 4444 y ProRes 4444 XQ;
  p. 203). Sólo algunos conservan el canal alfa (sin comprimir de 10 y 16 bits, ProRes 4444, 4444 XQ
  y DNxHR 444).

### Por qué pesan los códecs de cámara al montar

Los códecs de entrega y de muchas cámaras (H.264, H.265) comprimen entre cuadros (GOP largo): para
mostrar un cuadro hay que descodificar otros, y eso frena la reproducción y el salto de un punto a
otro de la línea de tiempo (oficio; el GOP se estudia en el tema 4). Resolve lo reconoce al dejar que
su caché inteligente calcule de antemano precisamente esos formatos: **«First, H.264, H.265, DCP,
JPEG2K, or camera raw clips that have been edited into a timeline are cached.»** (p. 209). De ahí las
dos salidas del epígrafe siguiente: transcodificar a un códec de montaje o montar con *proxies*.

## 6. Proxies

### Offline y online

La idea de los *proxies* es antigua y tiene nombre propio en el oficio: *offline* y *online*.

| Fase | Qué es | Con qué material |
|---|---|---|
| *Offline* | El montaje: decidir qué va, en qué orden y con qué duración | Material de baja resolución, ligero y rápido |
| *Online* | El acabado: efectos, grafismo, etalonaje y salida | El material de resolución completa |

Por qué existió la separación: cuando el disco era caro y lento, montar con material ligero era la
única forma de trabajar, y al final se reconformaba la secuencia contra el material bueno. Hoy la
separación se mantiene en producciones grandes, no por el disco, sino porque el montaje se hace en
una sala y el acabado en otra.

Avid diseñó para ese flujo una variante de su códec: **«The Avid DNxHD 36 resolution is targeted
specifically at the creative editorial workflow.»**; está disponible **«for 1080p/23.976, 1080p/24,
1080p/25, and 1080p/29.97 projects»** (sólo progresivo) y, entre sus ventajas, deja una calidad
**«high enough quality to screen directly without the additional cost and time of a conform step»**
(suficiente para visionar sin tener que conformar antes; *Avid DNxHD Technology*, 2012).

«Offline» tiene además un segundo sentido en todos los programas: un clip *offline* es el que ha
perdido su material (epígrafe 3). Conviene no mezclar los dos.

### Qué es un *proxy*

Un *proxy* es una copia ligera del material, enlazada al original, con la que se monta en su lugar:

- Adobe: **«Proxy workflows in Premiere involve creating lower-resolution, lightweight copies of your
  high-resolution video files. These lower-resolution copies, known as proxy files, are used for
  editing instead of the original high-res files.»** (copias ligeras y de menor resolución que se usan
  para montar en lugar de los originales; «Ingest and Proxy workflow», actualizada el 07-01-2026).
- Blackmagic: **«Proxy Media is essentially more highly compressed (and potentially lower resolution)
  versions of your source media that are linked to your source media in DaVinci Resolve via
  metadata.»** (versiones más comprimidas, y quizá de menor resolución, enlazadas al original por
  metadatos; p. 213).

La diferencia con el *offline* clásico es que el enlace no se pierde: el programa sabe en todo
momento qué original corresponde a cada *proxy* y cambia de uno a otro con un botón, sin conformar.
Resolve lo resume: permite usar *proxies* **«for increased real-time effects performance and full
speed playback while editing, while easily reverting back to more bandwidth and processor-intensive
source media for color correction, finishing, and final output»** (para montar con fluidez y volver
al original para el color, el acabado y la salida; p. 213).

### En cada programa

Premiere. El orden es crear, montar y volver: **«When working with proxies, you first create
proxy files, edit these proxies, and then convert to full resolution media when you need the full
resolution files.»** Los *proxies* pueden venir de fuera: **«You can also work with proxies that are
created outside of Premiere (for example, proxies created using other applications, or cameras). In
this case, you need to attach proxies to the full resolution media files»** (los hechos por otras
aplicaciones o por la cámara hay que asociarlos, *attach*, al original). Al acabar, **«you can switch back to the
original media for final export.»** La ingesta y los *proxies* se pueden combinar: copiar el original
como respaldo y crear *proxies* para montar. La misma página da cuatro funciones no admitidas con
*proxies*: **«The proxy functionality in Premiere is not compatible with the proxy functionality in
After Effects.»**; **«Dynamic Link is not supported for After Effects compositions or projects.»**
(el enlace dinámico con composiciones o proyectos de After Effects); **«Editing audio in Adobe
Audition is also not supported for proxy workflows.»**; y **«The option to modify audio channels and
interpret footage isn't supported.»** (ni modificar los canales de audio ni interpretar el
material).

Resolve. Al crearlos se elige la resolución (**«Original»**, o reducirla a **«Half, Quarter,
Eighth, or Sixteenth»**, o **«Choose Automatically»**, que sólo reduce lo que supera la resolución
del *timeline*) y el códec (epígrafe 5; p. 213). Para reproducir, en la página *Edit* se elige
*Playback > Proxy Handling* (en la página *Cut*, con el icono del visor), con tres modos (p. 219):
*Disable All Proxies*, **«forces the original media playback only»** (sólo el original; si falta,
el clip se sustituye por el gráfico «Media Offline»); *Prefer Proxies* (el *proxy*; si el clip no lo
tiene, el original; si falta el original, el *proxy*, con la línea morada del epígrafe 4); y
*Prefer Camera Originals* (el original; si falta, el *proxy*, también con la línea morada). La salida
no los usa salvo que se pida: **«By default, the Deliver page always reverts proxies to the original source media for
final output to ensure the highest quality render.»** (la página de entrega vuelve siempre al
original para la salida final). La casilla «Use proxy media» lo cambia, y hay que marcarla también
**«if you are editing with proxies and do not have access to the original source media»** (si se
monta con *proxies* sin acceso al original; p. 220).

Media Composer. Desde la versión 2022.10 crea *proxies* en la edición Enterprise: se seleccionan
en el *bin* los *master clips*, *subclips*, grupos o secuencias y se elige *Create Proxies*;
**«The proxy media appears in the bin with an orange clip icon.»** (el *proxy* aparece con icono
naranja). Para reproducir hay tres modos en el botón de *play*: **«High-Resolution Only»**, **«Proxy
Preferred»** (el *proxy* si existe; si no, el original) y **«High-Resolution Preferred»** (el original
si existe; si no, el *proxy*); en modo *proxy* el botón se vuelve naranja (*What's New v2022.10*,
pp. 9-10). Una salvedad de la misma nota: el audio de 48,048 kHz, como el que resulta de un proceso
de *pulldown*, no se admite al crear *proxies* (p. 4).

### *Proxies*, medios optimizados y caché: tres cosas distintas

Resolve tiene tres ayudas al rendimiento que conviene no confundir (pp. 201, 204 y 222):

| Qué | Qué es | Se puede mover o exportar |
|---|---|---|
| *Proxy Media* | Ficheros ligeros independientes, enlazados al original | Sí: **«Proxy Media is independent and portable (you can move clips wherever you want; you just have to relink them afterward)»** |
| Medios optimizados | Copias ligeras que gestiona el programa; se activan y desactivan con **«Playback > Use Optimized Media if Available»** (p. 202) | No: **«Optimized Media is managed internally by DaVinci Resolve, cannot be exported, and is not user accessible.»** Tampoco entran en la gestión de medios ni en el archivo del proyecto |
| Caché de *render* | Efectos calculados (epígrafe 4) | No: sólo sirve al proyecto que la creó |

Y un cuarto nombre que despista: el *Timeline Proxy Mode* no crea ficheros, sólo baja al vuelo la
resolución de la reproducción; el manual insiste en que **«The two functions, Timeline Proxy Mode and
Proxy Media, have no relation to each other.»** (p. 201).

### Para qué sirven en una redacción (oficio)

Los *proxies* resuelven tres situaciones del puesto: montar material pesado (UHD, HDR, formatos de
cámara de GOP largo) en un equipo que no lo mueve en tiempo real; montar en remoto o desde un portátil
sin llevarse el material original; y empezar a montar mientras el original todavía se copia. El
riesgo está al final: exportar con *proxies* por error, o que falte el original al entregar. La
comprobación es siempre la misma: antes de la salida, volver al original y revisar que no queda
ningún aviso de material ausente.

## 7. Conformado

### Qué es conformar

Conformar es reconstruir un montaje contra el material bueno. Blackmagic lo define así: **«Generally
speaking, "conforming" a project describes the process of importing a project exchange file from
another post-production application, and automatically relinking each clip in the imported timeline
to the high-quality media files each clip corresponds to.»** (importar el fichero de intercambio de
un proyecto hecho en otra aplicación y reenlazar cada clip de la línea de tiempo con su material de
calidad; p. 476). El fichero de intercambio puede ser **«EDL, AAF, or XML»** (p. 476). El mismo
capítulo da otro caso, dentro de un solo programa: **«you may choose to edit using transcoded
versions of camera raw media files, and later switch to the original camera media for grading and
finishing»** (montar con copias transcodificadas y pasar después al original para color y acabado;
p. 492).

Conformar y reenlazar son la misma operación vista desde dos sitios: conformar es el paso del
*offline* al *online*, o de un programa a otro; reenlazar (*relink*) es la orden que rehace, clip a
clip, el enlace con el fichero (oficio).

### Con qué datos se reconoce cada clip

El programa no reconoce el material por la imagen, sino por sus metadatos. Avid lo detalla en su
orden de reenlace: **«The system compares information such as source tape name, timecode
information, and channels digitized.»** (compara el nombre de la cinta de origen, el código de tiempo
y los canales capturados); y **«The system disregards capture rate and audio resolution when
matching media files.»** (no tiene en cuenta la resolución de captura ni la del audio; guía de 1999,
pp. 336-337). En Resolve, una EDL crea una línea de tiempo **«that attempts to conform itself to the
media pool clips using reel name and timecode information»** (que se conforma con los clips del
*Media Pool* por nombre de bobina y código de tiempo; p. 492).

De ahí la regla de oficio más importante del epígrafe: el nombre de cinta o bobina y el código de
tiempo de origen no se tocan. Si un fichero se renombra a mano o se recodifica sin sus metadatos, ya
no se le puede reenlazar (sobre nombres y trazabilidad, tema 15).

### Preparar el montaje antes de conformar

Entre los consejos del manual de Resolve para el montaje que llega de otro programa hay dos que tocan
al montador (p. 479):

- Bajar a la pista V1 todos los clips que no estén superpuestos para una composición: las pistas
  múltiples son cómodas **«for offline editorial»**, pero **«less convenient when you're trying to
  conform, grade, finish, and render»**.
- Exportar desde el montaje *offline* una película de referencia y cargarla junto al proyecto:
  **«After project conform, you can compare the project as seen in the Record Viewer with the
  synchronized offline movie as seen in the Source Viewer set to Offline mode.»** Sirve para
  recorrer el montaje y comprobar que cada clip ha entrado bien y en sincronía.

### Volver a capturar: *Redigitize* y *Decompose* en Avid

La guía de Avid de 1999, escrita para cinta, llama al paso del *offline* al *online* volver a
capturar: **«Redigitizing is the process of capturing previously digitized source footage based on
existing clips and sequences.»** No exige volver a registrar el material, porque la información de
pistas, códigos de tiempo y compresión ya está en el *bin*. Entre los casos que da (p. 231):
**«You can redigitize low-resolution clips at a higher resolution setting after they have been
edited into a sequence.»** (recapturar a más resolución lo que se montó en baja). Y un aviso:
**«Redigitizing requires your original source footage.»** (hace falta el material original; p. 232).

Para no recapturar cintas enteras está *Decompose* (pp. 233-235):

- **«Decompose allows you to create new, shorter master clips based only on the material you have
  edited and included in your sequence, which saves system disk space.»** Crea *master clips* nuevos,
  más cortos, sólo con lo usado en la secuencia.
- Se elige la longitud de las colas, **«the number of additional frames you want to digitize at the
  heads and tails of the new master clips. This provides enough overlap for trimming and adding
  transition effects.»** (los cuadros de más al principio y al final de cada clip, para poder
  retocar cortes y poner transiciones). Si después se retoca o se pone
  un efecto sin colas, el sistema avisa de que no hay material suficiente.
- **«Decompose breaks any links to the original source clips»** (rompe el enlace con los clips de
  origen). Para conservar la primera versión de la secuencia, la guía propone duplicarla antes y, si
  se quiere (paso opcional), pasar la copia a un *bin* nuevo: **«Avid recommends this method if you
  intend to use the Decompose feature.»** (pp. 233-234).

### Consolidar en Avid

*Consolidate* copia el material a otro disco sin volver a capturarlo (a diferencia de *Decompose*,
que prepara la recaptura): **«When you consolidate media files, the system finds the media files or
portions of media files associated with selected clips, subclips, or sequences. It then makes copies
of them, and saves the copies on a target drive that you specify.»** *Subclips* y secuencias se
consolidan desde el *bin*, porque la *Media Tool* sólo muestra *master clips*; en el *bin* se pueden
consolidar los tres (guía de 1999, pp. 327-328). Actúa distinto según el
objeto (pp. 328-330):

- *Master clip*: **«the system creates exact copies of the media files»**. Si el *master clip*
  original se enlaza a los ficheros nuevos, queda otro con extensión **.old** enlazado a los viejos;
  si conserva el enlace con los viejos, se crea uno **.new** enlazado a los nuevos, numerados desde
  **.01**. **«Consolidating master clips does not save storage space»** (copia el fichero entero).
- *Subclip*: **«the system copies only the portion of the media files represented in the subclip,
  and creates a new master clip that is the duration of the subclip and a new subclip»**, con
  extensión .new.
- Secuencia: copia sólo lo montado, crea *master clips* nuevos (.new) por plano, y la secuencia, sin
  cambiar de nombre, **«is automatically relinked to the new media files»**. Por eso la guía aconseja
  duplicarla cada vez si se quieren conservar los enlaces con los ficheros originales.

Al consolidar *subclips* o secuencias se fija la longitud de las colas de los clips nuevos o se
acepta la que viene dada: **«60 frames (NTSC) or 50 frames (PAL)»** (p. 332).

Para qué se consolidan las secuencias terminadas, según la guía: **«Create backup files»**
(copias de seguridad), **«Preserve only the digitized media required for playback, and delete the
rest to use less storage space»** (quedarse sólo con lo usado) y **«Gather dispersed media onto one
drive for storage or transfer to another system»** (reunir en un disco el material disperso para
guardarlo o pasarlo a otro sistema).

Con ficheros la cinta ya no está, pero la lógica sigue: se transcodifica o se consolida sólo lo usado
más unas colas, y se conserva la secuencia original (oficio).

### Reenlazar

Media Composer. Un clip sin enlace lo dice: **«When a clip becomes unlinked, it displays the
message "Media Offline." If appropriate media exists online, you can use the Relink command to
reestablish the link.»** (guía de 1999, p. 336). A veces pasa, dice la misma guía, **«after you consolidate
or move material between systems»**. Se seleccionan los objetos en el *bin*, se elige *Relink* y se
indica dónde buscar (todos los discos o uno concreto). Si se quieren conservar los ajustes de
captura originales, la guía manda recapturar (*Batch Digitize*) y no reenlazar (p. 337). Antes de reenlazar conviene
cargar la base de datos de material: si los *master clips* se recapturaron o consolidaron con el
*bin* de secuencias cerrado, al volver a abrirlo **«the sequences might appear to be offline»**, y
la orden *Load Media Database* lo corrige (pp. 333-334).

La versión 2022.10 cambió el menú: **«The Relink menu now includes two options»**: **«Managed Media, opens the old
Relink dialog»** y **«Linked Media, opens the new Linked Media dialog»** (material gestionado por
Avid, con el diálogo de siempre; material enlazado, con uno nuevo en el que los clips sin enlace
salen en rojo y se reenlazan con *Locate Media*, señalando la carpeta donde está el material; *What's
New v2022.10*, pp. 13-14). Desde la 2023.3 se puede señalar un fichero o una carpeta entera:
**«Choosing a folder is a quick method to relink files more easily.»** (*What's New v2023.3*, p. 3).

Resolve. Reenlaza desde el *Media Pool*: **«use the Relink Media, Relink Selected Clips, or Relink
Clips in Selected Bins commands to relink clips to the corresponding source media on whatever storage
volume it's on. At the same time, any timeline instances of those clips are automatically updated.»**
(reenlaza los clips y, con ellos, todas sus apariciones en las líneas de tiempo). La orden **«searches
all subfolders in the selected directory»** y sirve también para forzar el enlace a otro material
(p. 495).

Premiere. Intenta primero reenlazar solo, por dos vías: **«Historical path tracking»** (las rutas
por las que pasó el fichero) y **«Automated search logic»** (búsqueda automática). En un proyecto
normal guarda **«The current file path»** y **«Up to two historical paths»**; en los proyectos de
equipo, rutas históricas sin límite. La búsqueda automática mira primero la carpeta del proyecto y sus
subcarpetas, y después la carpeta que la contiene; **«If both passes fail, Premiere opens the Link
Media dialog box for manual relinking»** (si fallan las dos pasadas, abre el diálogo *Link Media*
para reenlazar a mano). La página de ayuda «Relink media in Premiere» (actualizada el 15-04-2026)
pone cuatro casos en que el reenlace automático puede fallar y hay que
usar *Link Media*: ficheros o carpetas renombrados después de importarlos; cambios grandes en la
estructura de carpetas (el material pasa a un árbol que no cuelga de la carpeta del proyecto ni de
la que la contiene); discos externos desconectados; y cambio de formato del fichero, **«(for example, .mov
to .mp4)»**: si el material se ha transcodificado, **«unchecking the File Extension option in the
Match File Properties section of the linking dialog box should enable linking to the new files.»**
(desmarcar *File Extension* en *Match File Properties* del diálogo).

### Antes de dar el conformado por bueno (oficio)

Tras conformar o reenlazar: buscar clips *offline* (rojos en Avid, morados en Resolve si faltan
originales), comparar con la referencia *offline*, revisar que cada corte cae en el mismo cuadro y
que el audio sigue en sincronía, y comprobar en la secuencia que se trabaja ya con el material de
resolución completa y no con el *proxy*.

## 8. Exportación

### Dos cosas distintas que se llaman igual

Exportar puede significar dos cosas (oficio):

| Se exporta | Qué sale | Para qué |
|---|---|---|
| La pieza | Un fichero de vídeo y audio calculado, con el códec y el contenedor de entrega | Emisión, archivo, web y redes |
| El proyecto | Las decisiones de montaje sin el material, o con él: EDL, AAF, XML, OTIO, OMF | Llevar el montaje a otro programa: acabado, color, sonido |

La guía de Avid de 1999 ya daba las razones para sacar material del sistema: **«You can export audio
files for audio sweetening in compatible applications.»** (audio para su tratamiento en otra
aplicación) y **«You can export video files for touching up or creating special effects in
third-party applications or other Avid applications.»** (vídeo para retoques o efectos fuera), entre
otras; y los ajustes de exportación se guardan como plantillas para no repetirlos cada vez (pp.
716-717). Qué lleva un AAF u OMF, y por qué Avid recomienda AAF para sonido, se estudia en el tema 15.

### Premiere: exportación directa o cola de Media Encoder

Premiere ofrece dos caminos para la pieza («Export options in Premiere», actualizada el 18-08-2026):
**«Direct export generates files immediately from within Premiere»** (el fichero se genera desde el
propio programa) y **«Exporting through Adobe Media Encoder sends your asset to the Media Encoder
queue, where you can continue editing in Premiere while the file is being rendered.»** (la cola de
Media Encoder permite seguir montando mientras se calcula). De Media Encoder: **«Adobe Media Encoder
lets you queue multiple exports, use custom presets, and render files without interrupting your
editing workflow.»** Se llega por **«File > Export > Send to Adobe Media Encoder»**, y Adobe lo
recomienda **«for longer exports or when you need to create multiple delivery versions»** (para
exportaciones largas o varias versiones de entrega; «Export directly to Adobe Media Encoder»,
actualizada el 01-04-2026).

Para el proyecto: **«Premiere supports exporting to AAF, which can be imported into various
third-party editing systems»**; la misma ayuda tiene páginas para exportar EDL, XML de Final Cut Pro
y OMF para Pro Tools.

### Resolve: la página *Deliver*

Resolve concentra la salida en su página de entrega. El flujo que describe: se define el formato, se
elige el tramo y se añade el trabajo a la cola de *render*; se pueden encolar tantos trabajos como se
quiera, cada uno con su formato, y se calculan todos con *Start Render* (p. 4185). Arriba de los
ajustes hay preajustes para las salidas habituales, que **«automatically sets up what you need and
locks you out of settings that are not necessary»** (p. 4186).

Hay dos modos de salida (p. 4196):

- *Single clip*: **«all clips in the session are output together, as a single media file in
  whatever format you choose»**: un solo fichero, MXF o QuickTime, o una secuencia de imágenes. Es la
  salida normal de una pieza terminada. El código de tiempo lo da el ajuste «Start timeline timecode
  at» de la línea de tiempo; con cadencias mezcladas, **«rendering to a single clip converts every
  clip in the entire session to the project frame rate»** (todo pasa a la cadencia del proyecto), y
  la mayoría de los efectos quedan incorporados en el fichero.
- *Individual clips*: **«each clip is rendered as an individual media file»**: un fichero por clip.
  Y **«The timecode written to each clip is cloned from the original source media, making it easy to
  reconform media for projects being passed between DaVinci Resolve and NLEs.»** (el código de tiempo
  de cada clip se copia del original, para poder conformar de vuelta en otro programa). Con
  cadencias mezcladas, cada clip sale a la suya; los efectos de la línea de tiempo se incorporan o no según la casilla
  «Render Timeline Effects», y la resolución es la del *timeline* o la de origen según «Render at
  Source Resolution».

Para llevar un montaje ya corregido a otro programa, el manual pide las dos cosas a la vez: calcular
los clips como individuales y exportar la línea de tiempo como EDL, AAF, XML u OTIO, porque así
**«the reel name and timecode metadata of each rendered clip is mirrored by the exported project
file»** (el nombre de bobina y el código de tiempo de cada clip calculado coinciden con los del
fichero de proyecto; p. 4241). Es el conformado del epígrafe 7 hecho al revés.

Dos avisos de la misma página de entrega: sale del material original aunque se haya montado con
*proxies* (epígrafe 6); y la versión Studio puede exportar en IMF, **«the SMPTE ST.2067 Interoperable
Master Format (IMF) for tapeless deliverables to networks and distributors»** (el formato maestro
para entregar sin cinta a cadenas y distribuidores; p. 4219). Qué es IMF y los demás estándares de
entrega, en el tema 4.

### Antes de exportar (oficio)

La exportación es el último control del montador, y en una pieza informativa no hay tiempo para
repetirla. Lo que se comprueba:

1. Que se exporta la secuencia buena, la última versión, con entrada y salida bien marcadas (o sin
   marcas, si sale entera).
2. Que no hay material *offline* ni efectos sin calcular que vayan a salir en negro o con aviso.
3. Que se trabaja con el material original y no con *proxies*, salvo que se quiera lo contrario.
4. Que el preajuste es el del destino: códec, contenedor, resolución, cadencia, pistas y canales
   de audio, y nivel de sonoridad (temas 2 y 4).
5. Que el nombre del fichero sigue la convención de la casa (tema 15).
6. Que el fichero exportado se revisa: se reproduce entero, o al menos el principio, los cambios de
   plano críticos y el final.

## Aplicación práctica: una pieza de principio a fin

Supuesto: llega material de una cámara en H.265 UHD para una pieza de informativo de HD 1080 a 25
cuadros, que además hay que entregar en versión vertical para redes. El recorrido, con lo estudiado
(los pasos son de oficio; los datos, de los epígrafes citados):

1. Proyecto (epígrafe 2): tamaño y cadencia del formato de emisión, fijados antes de importar;
   en Resolve, la cadencia no se cambia después de importar el primer clip.
2. Bins (epígrafe 3 y tema 15): uno por origen (tarjeta o cámara), uno por tipo de material
   (totales, recursos, archivo, grafismo) y uno para las secuencias.
3. Códec y proxies (epígrafes 5 y 6): el H.265 es de GOP largo y pesa al montar; se crean
   *proxies* (o se transcodifica a un códec de montaje como DNxHD o ProRes) y se monta con ellos.
4. Timeline (epígrafe 4): secuencia HD a 25 cuadros con la plantilla de pistas de la casa; una
   segunda secuencia o *timeline* vertical con sus propios ajustes para la versión de redes.
5. Render (epígrafe 4): se calculan los efectos que no se reproducen en tiempo real.
6. Conformado (epígrafe 7): antes de salir se vuelve al original; si algo sale *offline*
   (rojo en Avid) se reenlaza: Avid y Resolve reconocen el clip por nombre de cinta o bobina y
   código de tiempo; Premiere lo busca por sus rutas (epígrafe 7).
7. Exportación (epígrafe 8): preajuste de emisión para la pieza y otro para redes, en la cola
   (Media Encoder o la de Resolve) para seguir trabajando; revisión del fichero final.

Si la pieza pasa después a sonido o a otra sala de acabado, se exporta además el proyecto (AAF, o EDL
o XML según el destino) y, en Resolve, los clips como individuales para que conserven bobina y código
de tiempo.

## Lo que este tema no da, y dónde está

- Qué sistema de edición, qué almacenamiento compartido y qué preajustes de entrega usa CSRTV:
  no consta en un documento publicado. El tema usa los tres programas cuya documentación se ha leído.
- Guía vigente de Media Composer: sólo se han leído la guía de 1999 (para cinta), las notas de
  novedades 2022.10 y 2023.3 y el documento de DNxHD de 2012. Lo que diga hoy la ayuda del programa
  sobre *bins*, exportación o *Dynamic Relink* no se ha comprobado en la documentación de Avid.
- DNxHR y ProRes: sus variantes y flujos no se han leído en documentación de Avid ni de Apple;
  aquí sólo constan como opciones de Resolve.
- Resolución, cadencia, muestreo, bits, compresión, GOP, contenedores, HDR y estándares de entrega
  (IMF, y AS-11, familia de especificaciones de
  formatos MXF acotados para entregar piezas terminadas a una cadena o a quien las
  publique): temas 2 y 4.
- Corrección de color, efectos, transiciones y colas en transiciones, grafismo, subtítulos y
  limpieza de audio: tema 7.
- Ingesta, copia verificada, metadatos y archivo: tema 8.
- Versiones para redes y plataformas: tema 12.
- Plantillas, automatización, MAM/PAM y sistemas de redacción: tema 13.
- Organización de *bins*, vistas del *bin*, copias automáticas (*Attic*), bloqueo de *bins*
  compartidos, nomenclatura, AAF y OMF: tema 15.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| Avid Technology, *Avid Media Composer User's Guide*, Release 8.0 for the Macintosh, mayo de 1999: p. 72 (un proyecto por programa), pp. 231-235 (*Redigitize*, *Decompose*, colas), 285-287 (órdenes de selección del *bin*), 321 (*Media Tool*), 327-330 y 332 (*Consolidate*, colas), 333-337 (base de datos de material, *Relink*), 462 y 470-471 (*Timeline*, clips *offline* en rojo), 716-717 (exportación) | Epígrafes 1, 3, 4, 7 y 8 | 25-09-2026 |
| Avid Technology, *What's New for Avid Media Composer v2022.10*: pp. 4 y 9-10 (*proxies*), 13-14 (menú *Relink*), 15 (plantillas de secuencia), 16-17 (*Choose For Me*) | Epígrafes 2, 4, 6 y 7 | 25-09-2026 |
| Avid Technology, *What's New for Avid Media Composer v2023.3*, p. 3 | Reenlace por fichero o carpeta | 25-09-2026 |
| Avid Technology, *Avid DNxHD Technology* (libro blanco, 2012) | Códec de montaje, familia DNxHD, VC-3, DNxHD 36 *offline*, formatos mezclados en los sistemas Avid | 25-09-2026 |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual*: pp. 21 y 23 (páginas y *Media Pool*), 76 y 78 (*Project Manager*, .drp), 201-222 (cap. 8: *proxies*, medios optimizados, caché), 375 (cadencia al importar), 476, 479, 492 y 495 (cap. 22: conformado y reenlace), 860 (cap. 41: *timelines*), 4185-4196 (cap. 187: *Deliver*), 4219 (IMF), 4241 (cap. 190: exportar líneas de tiempo) | Epígrafes 1 a 8 | 25-09-2026 |
| Adobe, ayuda de Premiere (copias de Wayback Machine, porque helpx.adobe.com rechaza la descarga directa): «Add and delete bins» y «Sequence presets and settings» (act. 22-08-2025), «Ingest and Proxy workflow» (act. 07-01-2026), «Relink media in Premiere» (act. 15-04-2026), «Export directly to Adobe Media Encoder» (act. 01-04-2026), «Export options in Premiere» (act. 18-08-2026) | Epígrafes 2, 3, 4, 6, 7 y 8 | 25-09-2026 |
| AMWA, página «AS-11: Media Contribution File Formats» | Qué es AS-11 | 25-09-2026 |
| Oficio | Comparación lineal/no lineal, *offline*/*online*, formato de codificación, códec y contenedor, definición de *render*, fases de códec, usos de los *proxies*, comprobaciones antes de exportar y supuesto práctico | — |
