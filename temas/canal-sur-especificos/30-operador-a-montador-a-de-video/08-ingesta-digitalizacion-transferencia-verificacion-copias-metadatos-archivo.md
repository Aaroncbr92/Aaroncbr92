# Tema 8 del específico de Operador/a Montador/a de Vídeo · Ingesta, digitalización, transferencia, verificación, copias de seguridad, metadatos y archivo

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Montador/a de Vídeo · punto 8 |
| Sirve para | Operador/a Montador/a de Vídeo de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Lo propio de la casa: X Convenio Colectivo de la RTVA (BOJA núm. 240, de 10-XII-2014), ficha del puesto 5212206; *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, 1.ª ed., marzo de 2004). Recomendaciones técnicas: EBU Tech 3293 (EBUCore, v. 1.10, 2020); CCSDS 650.0-M-3 (modelo OAIS, 2024). Documentación de fabricante y de organismos: Blackmagic Design (*DaVinci Resolve 21 Reference Manual*), Adobe (ayuda de Premiere, 2026, y documentación de XMP), Sony (*PXW-Z200/HXR-NX800 Help Guide*, 2024), programa LTO (lto.org), Digital Preservation Coalition, INCIBE. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las ediciones citadas, leídas el 24 y el 25-09-2026; el Libro de estilo en su única edición publicada; el convenio en su texto publicado de 2014 |
| Extensión | 11.000 palabras aproximadamente |

<!-- /portada -->

Siglas que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA);
Canal Sur Radio y Televisión, S.A. (CSRTV); Unión Europea de Radiodifusión (EBU, *European
Broadcasting Union*); Sociedad de Ingenieros de Cine y Televisión (SMPTE, *Society of Motion Picture
and Television Engineers*); Comité Consultivo de Sistemas de Datos Espaciales (CCSDS, *Consultative
Committee for Space Data Systems*), que publica el modelo de referencia de sistema abierto de
información de archivo (OAIS, *Open Archival Information System*), con sus paquetes de información
de entrega (SIP, *Submission Information Package*), de archivo (AIP, *Archival Information Package*)
y de difusión (DIP, *Dissemination Information Package*) y su información de descripción para la
conservación (PDI, *Preservation Description Information*); Organización Internacional de
Normalización (ISO); formato de intercambio de material (MXF, *material exchange format*), con su
patrón operacional OP-Atom; identificador único de material (UMID, *unique material identifier*);
formato avanzado de autoría (AAF, *advanced authoring format*) y lista de decisiones de edición
(EDL, *edit decision list*); fichero de intercambio de registros de Avid (ALE, *Avid Log Exchange*)
y valores separados por comas (CSV, *comma-separated values*); formato de imagen de cine digital
en secuencia (DPX, *Digital Picture Exchange*) y contenedor QuickTime de Apple (MOV); luminancia y diferencias de color (YUV) y rojo, verde y azul
(RGB); código de
tiempo (TC, *timecode*); magnetoscopio (VTR, *video tape recorder*); tarjeta de memoria digital
segura (SD, *secure digital*) y disco de estado sólido (SSD, *solid-state drive*); conjunto
redundante de discos independientes (RAID, *redundant array of independent disks*); almacenamiento
conectado a la red (NAS, *network attached storage*) y red de área de almacenamiento (SAN, *storage
area network*); cinta lineal abierta (LTO, *linear tape open*) y su sistema de ficheros (LTFS,
*Linear Tape File System*); bus serie universal (USB); interfaz digital serie (SDI) y protocolo de internet (IP); fichero de
sonido Broadcast WAVE (BWF, *Broadcast Wave Format*); protocolo de transferencia de ficheros (FTP) y
su variante cifrada en modo explícito (FTPES, también FTPS); gestión de activos de medios (MAM,
*media asset management*) y de activos digitales (DAM, *digital asset management*); sistema
informático de redacción (NRCS, *newsroom computer system*); comprobación de redundancia cíclica
(CRC, *cyclic redundancy check*); resúmenes criptográficos MD5 y SHA (*secure hash algorithm*), en
sus variantes SHA-256 y SHA-512, y el resumen rápido XXHASH64; Instituto Nacional de Ciberseguridad
(INCIBE); megabits por segundo (Mb/s), megabytes por segundo (MB/s), gigabyte (GB) y terabyte (TB);
formato maestro interoperable (IMF, *Interoperable Master Format*); número internacional normalizado
del libro (ISBN).

Los rótulos de programa y de menú se escriben como los imprime el fabricante (*Clone Tool*,
*Capture Now*, *Media Pool*, *Smart Bin*, ***[Update Media]***). «Z200» es la cámara Sony
PXW-Z200, cuyo manual público sirve de ejemplo; «P2» es el nombre comercial de las tarjetas de
Panasonic. *Proxy* es la copia ligera de un clip (tema 3); *checksum*, la suma de verificación.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.30, punto 8): «Ingesta, digitalización,
> transferencia, verificación, copias de seguridad, metadatos y archivo.»

Qué se puede preguntar. No hay exámenes anteriores de este puesto. Por el enunciado, un tribunal
puede preguntar: qué es la ingesta y qué formas tiene (de fichero, en directo, programada); por qué
la ingesta en directo es la crítica; qué pasos lleva la ingesta de una tarjeta y por qué se copia la
tarjeta entera; qué es un bloqueador de escritura; qué hace el modo de captura de un programa de
edición con un magnetoscopio y qué métodos tiene (captura inmediata, captura registrada, captura por
lotes desde una EDL); por qué el nombre de cinta importa al digitalizar; en qué se diferencian un NAS
y una SAN; por qué FTP no es seguro para enviar material; qué es una suma de verificación y qué
algoritmos hay (CRC32, MD5, SHA, XXHASH64) y cuál es más rápido o más seguro; qué es la fijeza y la
cadena de custodia; qué es la regla 3-2-1; si un RAID es una copia de seguridad, qué nivel es el
espejo y cuántos discos pide un RAID 5; qué metadatos pone la cámara y cuáles el montador; qué es
XMP y dónde guarda Premiere los metadatos de fichero; qué es EBUCore y en qué se basa; qué es el modelo OAIS y qué son SIP, AIP y DIP; qué capacidad tiene una
LTO-10 y si lee cintas de generaciones anteriores; qué es la LTFS; qué dice la ficha del puesto sobre
el archivo. En la prueba práctica: ingestar una tarjeta con copia verificada a dos destinos,
digitalizar un fragmento de cinta, poner metadatos útiles al material y preparar lo que va al
archivo.

<!-- indice -->

## Índice

- [El punto en la ficha del puesto](#el-punto-en-la-ficha-del-puesto)
- [1. Ingesta](#1-ingesta)
  - [Qué es la ingesta](#qué-es-la-ingesta)
  - [La ingesta en el flujo de la redacción](#la-ingesta-en-el-flujo-de-la-redacción)
  - [La ingesta de una tarjeta, paso a paso](#la-ingesta-de-una-tarjeta-paso-a-paso)
  - [La ingesta en el programa de edición](#la-ingesta-en-el-programa-de-edición)
- [2. Digitalización](#2-digitalización)
  - [Qué es digitalizar](#qué-es-digitalizar)
  - [La captura desde cinta en un programa de edición](#la-captura-desde-cinta-en-un-programa-de-edición)
  - [Por qué el nombre de cinta y el código de tiempo lo son todo](#por-qué-el-nombre-de-cinta-y-el-código-de-tiempo-lo-son-todo)
  - [Lo que se revisa al digitalizar (oficio)](#lo-que-se-revisa-al-digitalizar-oficio)
- [3. Transferencia](#3-transferencia)
  - [El envío desde el lugar](#el-envío-desde-el-lugar)
  - [Cuánto tarda una transferencia (cálculo)](#cuánto-tarda-una-transferencia-cálculo)
  - [Dónde vive el material en la casa: local, NAS y SAN](#dónde-vive-el-material-en-la-casa-local-nas-y-san)
  - [Las redes de una redacción](#las-redes-de-una-redacción)
- [4. Verificación](#4-verificación)
  - [La copia comprobada: la suma de verificación](#la-copia-comprobada-la-suma-de-verificación)
  - [Los algoritmos: velocidad frente a seguridad](#los-algoritmos-velocidad-frente-a-seguridad)
  - [La verificación en el archivo](#la-verificación-en-el-archivo)
  - [La verificación del contenido (oficio)](#la-verificación-del-contenido-oficio)
- [5. Copias de seguridad](#5-copias-de-seguridad)
  - [Por qué](#por-qué)
  - [La regla 3-2-1](#la-regla-3-2-1)
  - [Qué se copia, además del material](#qué-se-copia-además-del-material)
  - [Lo que no es una copia de seguridad: el RAID](#lo-que-no-es-una-copia-de-seguridad-el-raid)
- [6. Metadatos](#6-metadatos)
  - [Qué son y quién los pone](#qué-son-y-quién-los-pone)
  - [Los metadatos dentro del fichero](#los-metadatos-dentro-del-fichero)
  - [Los metadatos en el programa de edición](#los-metadatos-en-el-programa-de-edición)
  - [Los metadatos de fichero de Adobe: XMP](#los-metadatos-de-fichero-de-adobe-xmp)
  - [Los metadatos en el sistema de la casa](#los-metadatos-en-el-sistema-de-la-casa)
  - [La norma del sector: EBUCore](#la-norma-del-sector-ebucore)
- [7. Archivo](#7-archivo)
  - [Qué le toca al montador](#qué-le-toca-al-montador)
  - [Material de trabajo y material de archivo](#material-de-trabajo-y-material-de-archivo)
  - [El modelo de referencia: OAIS](#el-modelo-de-referencia-oais)
  - [La cinta de archivo: la LTO](#la-cinta-de-archivo-la-lto)
  - [La LTFS: la cinta como un disco](#la-ltfs-la-cinta-como-un-disco)
  - [El material de archivo en el montaje](#el-material-de-archivo-en-el-montaje)
- [Aplicación práctica: del material que llega al material que se archiva](#aplicación-práctica-del-material-que-llega-al-material-que-se-archiva)
- [Documentos técnicos que el tema cita](#documentos-técnicos-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## El punto en la ficha del puesto

El X Convenio Colectivo de la RTVA define el puesto en su anexo III (código 5212206, BOJA núm. 240,
p. 190). Su **«OBJETO O FUNCIÓN BÁSICA DEL PUESTO»** es **«Realizar todo tipo de procesos de
grabación, reproducción, manipulación, edición y postproducción de la señal de audio y video con
criterios técnicos y artísticos, en coordinación con otras áreas.»** Cinco de sus ocho **«TAREAS
MÁS SIGNIFICATIVAS DEL PUESTO»** tocan este tema:

| Tarea de la ficha (literal) | Rúbrica del enunciado |
|---|---|
| **«Configurar sistemas de edición y preparar los materiales a utilizar.»** | Ingesta, verificación, metadatos |
| **«Recibir y enviar enlaces.»** | Ingesta en directo y transferencia |
| **«Compactar para el archivo de material audiovisual.»** | Archivo |
| **«Repicar cintas orientadas a la producción, emisión y comercialización.»** | Digitalización y copia |
| **«Realizar el control técnico de calidad y corregir video y audio para su emisión y/o venta.»** | Verificación del contenido (la medida y la corrección, en los temas 2 y 7) |

Una sexta roza los metadatos, **«Etiquetar, grabar e introducir en base de datos, la información para
la emisión automatizada de programas y bloques publicitarios.»**, pero su objeto es la emisión
automatizada: está en el tema 13.

La ficha es de 2014 y habla de cintas; el convenio no define «compactar» ni «repicar». Lo que el
tema da sobre esas tareas en un flujo de ficheros es técnica y oficio, no interpretación del
convenio. Quién hace en CSRTV cada paso (un técnico de ingesta, el montador, documentación) y con
qué sistema no consta en un documento publicado. El reparto de las fichas entre montador, ayudante
de archivo y documentalista está en el tema 9.

## 1. Ingesta

### Qué es la ingesta

Ingestar es meter el material en el sistema donde se va a trabajar: el servidor de la redacción o
de edición. En una casa de televisión no es sólo copiar ficheros: es un proceso con metadatos,
comprobación y, a menudo, conversión al formato de la casa (oficio). Tiene tres formas:

| Forma | Qué es |
|---|---|
| Ingesta de fichero | Copiar material que ya viene en fichero (una tarjeta, un disco, un envío) con su comprobación de integridad |
| Ingesta en directo (*crash record*) | Grabar una señal que entra ahora: un enlace, una señal de agencia, una cámara en directo |
| Ingesta programada | Grabar automáticamente en un horario previsto, sin nadie delante, con recurrencia (diaria, semanal, mensual) |

Por dónde entra el material, que es otra forma de ordenar lo mismo:

| Tipo | De dónde entra | Rasgo |
|---|---|---|
| En directo, desde señal | Una entrada de vídeo: agencia, satélite, unidad móvil | Ocurre en tiempo real y no se puede repetir |
| Desde soporte | Una tarjeta o un disco de cámara | Va más deprisa que en tiempo real |
| Desde fichero | Una entrega por red o por transferencia | La más rápida, y la que más problemas de formato da |

Y la razón por la que la ingesta en directo es la crítica: es la única que no se puede repetir. Si
falla la grabación de una señal de agencia mientras ocurre, no hay segunda oportunidad, y por eso se
graba por partida doble en dos sistemas independientes.

Al montador le llegan las tres. La ficha nombra expresamente la de señal (**«Recibir y enviar
enlaces.»**); la grabación de un directo mientras se emite está en el tema 14.

### La ingesta en el flujo de la redacción

| Etapa | Qué hace | Quién trabaja ahí |
|---|---|---|
| Ingesta | Meter el material en el sistema: grabar señales de entrada y volcar tarjetas | Operadores de ingesta |
| Gestión | Catalogar, buscar y controlar el material y sus versiones | Documentación y todos los demás |
| Edición | Montar las piezas | Redactores y montadores |
| Emisión | Poner la pieza en antena en el momento previsto | Control de emisión |

Y el archivo atraviesa las cuatro, no es una quinta: lo que se conserva se decide en la primera y se
ejecuta después.

La regla que ordena el punto: cada etapa mete el material en un sitio y las demás lo encuentran por
sus datos descriptivos, no por su nombre de fichero. Ésa es toda la diferencia entre un sistema de
redacción y una carpeta compartida.

Es un esquema general de oficio; cómo reparte esas etapas CSRTV no consta publicado. El sistema de
redacción, el MAM y la automatización están en el tema 13.

### La ingesta de una tarjeta, paso a paso

Es oficio, salvo donde se cita:

1. Proteger el original. Bloquear la tarjeta (conmutador **«LOCK»** de una SD) antes de meterla
   en el lector. La guía de conservación digital lo recomienda en su segundo nivel: **«Use
   write-blockers when working with original media»**, para **«prevent write access to media that
   digital materials might be on prior to being copied»** (Digital Preservation Coalition, *Digital
   Preservation Handbook*, «Fixity and checksums»). Con salvedades: **«Write blockers also don't
   exist for all types of media»**, y **«some organisations might consider use of write blockers to
   be unnecessary or a level 3 or level 4 step»**. Un ordenador que escribe en la tarjeta (índices, papeleras,
   «¿desea formatear?») puede estropearla.
2. Copiar la tarjeta entera, con su estructura de carpetas, no sólo los ficheros de vídeo. En la
   Z200 el *proxy* va en una carpeta distinta del original (**«/PRIVATE/M4ROOT/SUB»**, p. 161); en una
   P2, el audio va en ficheros separados del vídeo (OP-Atom); y los ficheros de gestión de la cámara
   van aparte. Los programas de edición y de ingesta reconocen la tarjeta por esa estructura.
3. Comprobar la copia, con suma de verificación o, como mínimo, comparando tamaños y abriendo los
   clips (véase «Verificación»). La guía citada recomienda **«Check fixity on all ingests»** y
   **«Virus-check high risk content»** (las dos, en el segundo de sus cuatro niveles).
4. Revisar lo que ha llegado: número de clips, clips partidos por la grabación en relevo (que la
   Z200 **«cannot be played back seamlessly»**, p. 98), clips sin sonido.
5. Anotar y entregar (véase «Metadatos»). Sólo después, y con la copia comprobada, la
   tarjeta vuelve a la cámara para formatearse allí.

La grabación en relevo es la que la cámara continúa en la segunda tarjeta cuando se llena la
primera; por eso un plano largo puede llegar partido en dos clips (oficio).

### La ingesta en el programa de edición

Los programas de edición hacen la ingesta de fichero ellos mismos, con copia y comprobación:

- Premiere (ayuda de Adobe, «Ingest and proxy workflows in Premiere», actualizada el 7-1-2026):
  **«Ingesting in Premiere refers to the process of copying and transcoding media files from your
  source storage (such as memory cards, external hard drives, or network drives) to your project's
  local storage or designated media cache location.»** Al ingestar se puede transcodificar a un
  formato más fácil de editar y consolidar el material en el almacenamiento del proyecto, y
  **«Premiere verifies to ensure that there is no data corruption or loss while copying media.»** La
  página no dice con qué algoritmo comprueba; el tema no lo da.
- Para qué usar la ingesta, según la misma página: **«Use the ingest workflow when you want to keep
  a copy of the original media in its highest quality but still need to optimize it for editing.»**
  Y se puede combinar con los *proxies*: **«Ingest the original media for backup and create proxy
  files for smoother editing»**.
- DaVinci Resolve copia las tarjetas con su *Clone Tool*, desde la página *Media*, con una suma de
  verificación a elegir entre seis (véase «Verificación»), antes de añadir el material al *Media
  Pool*: clonar el original a varios volúmenes es, según el manual, **«One of the few things you may
  want to do before you add media to your project»** (cap. 17, p. 373); el manual lo propone, no lo
  impone.

Ingestar no es lo mismo que importar (oficio): importar sólo enlaza el proyecto con ficheros que
siguen donde estaban (la tarjeta, un disco externo); si ese soporte se retira, el clip queda sin
material. Por eso el material de una tarjeta se copia primero a un almacenamiento de trabajo y
después se importa desde allí. Qué pasa cuando se pierde el enlace y cómo se reenlaza está en el
tema 3.

## 2. Digitalización

### Qué es digitalizar

Digitalizar es convertir en fichero un material que está en un soporte que no lo es: una cinta de
vídeo o de audio, analógica o digital, reproducida en un magnetoscopio y grabada en el sistema
(oficio). Si la cinta es analógica, la señal se convierte además de analógica a digital. La
conversión analógico-digital, en una frase: se mide la señal muchas veces por segundo (muestreo) y
cada medida se anota con un número de niveles limitado (cuantificación). De la primera depende qué
frecuencias se conservan; de la segunda, cuántos matices. Muestreo y cuantificación de la señal de
vídeo y de audio están en el tema 2.

Al revés que la ingesta de una tarjeta, digitalizar va en tiempo real: una hora de cinta es una hora
de captura, y lo que no se registra bien al pasar hay que volver a pasarlo (oficio). La ficha del
puesto conserva la tarea de **«Repicar cintas orientadas a la producción, emisión y
comercialización.»**; en un archivo de televisión la cinta sigue existiendo como fondo, y se
digitaliza cuando se necesita (oficio; qué parte del fondo de la RTVA está digitalizada no consta
publicado).

### La captura desde cinta en un programa de edición

El manual de DaVinci Resolve 21 lo describe en su capítulo 24, «Ingesting From Tape» (pp. 558-564),
y sirve de modelo de lo que hace cualquier programa con captura:

- Qué hace falta: **«DaVinci Resolve is capable of capturing media from tape using a compatible video
  input device, such as a Blackmagic Design UltraStudio or DeckLink card. Device control is
  supported.»** (p. 558). Es decir, una tarjeta o caja de entrada de vídeo y un magnetoscopio que el
  programa pueda gobernar: **«you can use the Media page in Capture mode to capture from any
  device-controllable deck via a compatible video interface.»** (p. 559).
- Qué cambia en pantalla: en modo captura los controles de transporte gobiernan el magnetoscopio
  (**«now work to control the VTR»**), y **«the Audio panel is replaced by a dedicated set of capture
  metadata and controls to help you track the resulting clips.»** (p. 559). Los metadatos se ponen
  antes de capturar, no después.
- Qué se ajusta antes (p. 561): si se captura vídeo y audio o sólo vídeo; el formato del fichero
  (**«When capturing from tape, the available options are DPX and QuickTime.»**); el códec (**«the
  various type of Apple ProRes, 8- and 10-bit YUV 422, 10-bit RGB, and the various types of
  DNxHD»**); la carpeta de destino, que debe estar en un volumen **«fast enough to accommodate the
  data rate of the media format you're capturing»**; cómo se escribe el nombre de cinta (**«Apply
  reel number to»**: en el nombre del fichero y/o en su cabecera); un prefijo para el nombre; y
  cuántas pistas de audio se capturan, **«from 2 to 16»**.
- Lo mínimo: **«Once you've set up all relevant settings in the Project Settings window, including
  at minimum "Video Capture and Playback," "Capture Clips Saved to," and Apply Reel Name to"
  settings, then you're ready to start capturing.»** (p. 562; las comillas desparejadas están en el
  original).

Los tres métodos de captura (p. 562-563):

| Método | Cómo se hace | Para qué |
|---|---|---|
| *Capture Now* | Se pone la cinta en reproducción y se pulsa *Capture Now* al empezar y al terminar | **«If you simply need to capture a section of tape quickly»** |
| Registrar y capturar un clip | Se marcan entrada y salida en la cinta, se rellenan los metadatos y se pulsa *Capture Clip*; el programa gobierna el magnetoscopio y captura ese tramo | Un tramo exacto de la cinta |
| Registrar varios clips y capturarlos por lotes | Se marcan varios tramos, de una o varias cintas, con *Log Clip*; quedan en el *Media Pool* como clips de cinta sin material, y después se capturan todos juntos | **«For efficiency's sake»**; se pueden ordenar por número de cinta para capturar cinta a cinta |

Y un camino más, **«Batch Capture Via EDL»** (p. 563): **«You can also use an EDL to create offline
tape clips, one for each event in the EDL, with which to batch capture all the media necessary to
conform a project from tape.»** Es volver a capturar los tramos que usa un montaje a partir de su
EDL; si ya hay en el *Media Pool* clips con el mismo nombre de cinta y el mismo código de tiempo de
inicio que un evento, el programa no crea otro (p. 564).

### Por qué el nombre de cinta y el código de tiempo lo son todo

Un clip capturado se reconoce después por dos datos: de qué cinta sale y en qué código de tiempo
empieza y acaba (oficio). Si la cinta no lleva nombre o dos cintas se llaman igual, la captura por
lotes y el reconformado desde una EDL no saben qué cinta pedir. Por eso el nombre de cinta se pone
antes de capturar y es único. Resolve, en la captura inmediata, incluso nombra el clip con el
código de tiempo convertido en número de cuadros según la cadencia de captura (**«based on the ingest
frame rate»**): **«For example, 00086400.dpx is the file name of a clip captured at timecode
01:00:00:00.»** (p. 562). Cómo se reconoce y se reenlaza un clip por nombre de cinta y código de tiempo, y el
*Redigitize* de Avid, están en el tema 3.

### Lo que se revisa al digitalizar (oficio)

- La cinta antes de ponerla: estado físico, que sea la que dice la etiqueta, protección contra
  grabación puesta.
- El magnetoscopio: limpio, y con el control remoto funcionando; sin control no hay captura
  registrada ni por lotes, sólo *Capture Now*.
- La señal durante la captura: niveles de vídeo y de audio en los monitores de forma de onda y de
  audio (tema 2); cortes, cuadros congelados o ruido que vengan de la cinta.
- El fichero al terminar: duración, número de pistas de audio y que empieza y acaba donde debía.

## 3. Transferencia

Transferir es mover material de un sitio a otro: de la calle a la casa, de un centro a otro, del
almacenamiento de ingesta a la sala, de la sala a emisión o al archivo (oficio). Hay dos maneras de
hacerlo, y la ficha del puesto nombra la primera (**«Recibir y enviar enlaces.»**):

| Manera | Qué viaja | Rasgo |
|---|---|---|
| Como señal (enlace) | Vídeo y audio en tiempo real, que en destino se graba (ingesta en directo) | Dura lo que dura el material; lo que no se graba al pasar se pierde |
| Como fichero | El fichero entero, por red | Puede ir más deprisa o más despacio que el tiempo real, según la red; se comprueba al llegar |

Los enlaces y el directo, desde el lado de la sala, están en el tema 14; la señal SDI y el vídeo
sobre IP, en el tema 4.

### El envío desde el lugar

Cuando no hay tiempo de llevar la tarjeta, se envía el material por red desde la cámara o desde un
ordenador (oficio). Lo habitual es enviar primero el *proxy*, que pesa poco, y el original después
o nunca.

Cuando el material viaja por internet, el protocolo importa. El manual de la Z200 lo dice sin
rodeos: **«In FTP, the contents, user name, and password are not encrypted. For secure data transfer,
use FTPES (FTPS).»**; y **«You can transfer files with encryption using FTPS in Explicit mode (FTPES)
for the connection with the file transfer destination server.»** (p. 196). Con FTP sin cifrar, quien
intercepte la conexión ve el material y la contraseña del servidor de la casa (oficio).

Precauciones del envío, del lado de quien recibe (oficio): comprobar que el fichero ha llegado
entero (tamaño, duración, que se abre y se reproduce hasta el final) antes de avisar de que está
disponible; y que quien lo envió no borre ni formatee nada hasta que se confirme.

### Cuánto tarda una transferencia (cálculo)

El tiempo es el tamaño dividido por la velocidad, con cuidado de las unidades: las redes se miden en
bits por segundo y los ficheros en bytes, y un byte son ocho bits. Un clip de 12 GB por una línea
de 100 Mb/s: 12 × 8 = 96 gigabits; 96.000 megabits ÷ 100 Mb/s = 960 segundos, 16 minutos como
mínimo, sin contar lo que la red pierda por el camino. El mismo clip en *proxy*, a una fracción de la
tasa, tarda esa misma fracción del tiempo: por eso se manda primero el *proxy*.

### Dónde vive el material en la casa: local, NAS y SAN

Dentro de la casa la transferencia es, sobre todo, leer y escribir en el almacenamiento compartido.
Dónde vive el material determina cómo se monta, y el vocabulario aparece en los enunciados:

| Sistema | Qué es | Dónde se usa |
|---|---|---|
| Almacenamiento local | Discos dentro de la estación de edición | Proyectos de una sola sala |
| NAS | Un armario de discos que sirve ficheros por la red, con su propio sistema de ficheros | Trabajo compartido ligero, archivo |
| SAN | Una red dedicada que ofrece a cada estación bloques de disco, como si fueran suyos | Edición compartida en tiempo real: informativos, deportes |

La diferencia que importa al montador: en un NAS se pide un fichero; en una SAN se pide un bloque de
disco. Por eso la SAN da el caudal sostenido que la reproducción de vídeo necesita y es la que se
monta donde varias salas trabajan sobre el mismo material.

Y en cualquiera de los tres, debajo hay un RAID. No son alternativas al RAID: son maneras de
presentar el RAID a las estaciones.

El RAID está en «Copias de seguridad». Qué almacenamiento compartido usa CSRTV no consta en un
documento publicado.

### Las redes de una redacción

Las tres redes que conviven en una redacción:

| Red | Qué lleva | Por qué va separada |
|---|---|---|
| De señal | Vídeo y audio en tiempo real | Caudal enorme y sensible al retardo |
| De producción | Ficheros, baja resolución, control del sistema | Caudal alto a ráfagas |
| Ofimática | Correo, navegación, gestión | Es la que está expuesta a internet |

Y la razón de la separación, dicha sin rodeos: la red ofimática es la que recibe el correo con el
adjunto malicioso. Si la producción cuelga de ella, un incidente de seguridad puede parar la emisión.

Lo que el montador necesita saber de la red: el vídeo por red no perdona la congestión. Una sala de
edición sobre red compartida da cortes en la reproducción cuando otro tráfico satura el enlace, y por
eso la red de producción va separada de la ofimática.

Es arquitectura habitual, de oficio; la red de CSRTV no consta publicada. Consecuencia práctica para
la sala (oficio): un fichero que llega de fuera (una memoria USB, una descarga, un envío de un
colaborador) no se copia directamente al almacenamiento de producción sin pasar antes por el
procedimiento de la casa para material externo.

## 4. Verificación

Verificar tiene dos sentidos, y los dos le tocan al montador (oficio): que la copia es idéntica al
original (verificación de datos) y que el material es lo que dice ser y se puede usar (verificación
de contenido).

### La copia comprobada: la suma de verificación

Copiar no basta: hay que saber que la copia es idéntica. La herramienta es la suma de verificación
(*checksum*). La guía de conservación digital la define así:

- **«Fixity, in the preservation sense, means the assurance that a digital file has remained
  unchanged, i.e. fixed.»** (cita de Bailey, 2014), y **«fixity of files can established and
  monitored through the use of checksums.»**
- **«A checksum on a file is a ‘digital fingerprint’ whereby even the smallest change to the file
  will cause the checksum to change completely.»**; pero **«they do not tell you where in the file
  that the change has occurred.»**
- Para qué: **«To know that a file has been correctly received from a content owner or source and
  then transferred successfully to preservation storage»**. **«This allows a ‘chain of custody’ to be
  established between those who produce or supply the digital materials, those responsible for its
  ongoing storage, and those who need to use the digital material that has been stored.»**
- Qué algoritmo: **«There are several different checksum algorithms, e.g. MD5 and SHA-256 that can
  be used to generate checksums of increasing strength.»** Y **«if checksums are being used to detect
  accidental loss or damage to files, for example due to a storage failure, then MD5 is sufficient
  and has the advantage of being well supported in tools and is quick to calculate.»**
- Con varias copias, la suma dice cuál está bien: **«if one of the copies has changed then one of the
  other copies can be used to create a known good replacement»**; comprobarlo periódicamente se
  llama **«‘data scrubbing’»**.

(Digital Preservation Coalition, *Digital Preservation Handbook*, «Fixity and checksums».)

### Los algoritmos: velocidad frente a seguridad

El manual de DaVinci Resolve 21 da las seis opciones de su *Clone Tool* y lo que cuesta cada una
(cap. 17, pp. 373-374): **«Each option is a tradeoff between the speed of your file copy operation and
the security of the verification process. Greater security generally means a slower copy
operation.»** Antes define la palabra clave: **«"Collision resistance" refers to whether two files (or
a file and an incorrectly duplicated file) may coincidentally have the same comparison value (be it
file size, an error-detecting code, or a hash).»**

| Opción | Qué compara | Lo que dice el manual |
|---|---|---|
| None | Nada | **«Disables data verification, sacrificing safety for speed.»** |
| File Size | El tamaño del fichero | **«Fast, but minimal data verification.»**; **«minimally collision resistant»** |
| CRC 32 | Un código de detección de errores, no un resumen (*hash*) | **«Faster than MD5, but less secure.»**; **«significantly less collision resistant»** |
| MD5 | Un resumen de 128 bits | **«This is the default setting. A reasonable tradeoff between speed and security.»** |
| SHA 256, SHA 512 | Resúmenes de 256 y 512 bits | **«Slower, but more secure.»**; el de 512 **«even more collision resistant than 256»** |
| XXHASH64 | Un resumen rápido | **«This is by far the fastest checksum method and also provides good collision protection.»** |

Del MD5 dice: **«A hash function generates a 128-bit value that's unique to a particular file; Data
integrity is checked by comparing the hash value generated by the original file to that generated by
the copied file.»**, y que, aunque resiste menos las colisiones que los SHA, **«the probability of such
collisions in conventional film and video workflows is probably small.»** Coincide con la guía
de conservación digital citada arriba: para detectar pérdidas o daños accidentales, el MD5 basta.
Del XXHASH64 añade: **«This speed is very welcome when verifying terabytes of data.»**

La herramienta deja el resultado por escrito: copia **«to multiple destinations, with a checksum
report (based on a choice of six checksum options) written to the root of each destination volume
that verifies the absolute accuracy of the duplicate media saved to each destination.»** (p. 373).
Ese informe es la prueba de la copia: se guarda con ella (oficio).

Tres reglas que salen de ahí (oficio):

1. Comparar sólo el tamaño no es verificar: dos ficheros del mismo tamaño pueden ser distintos.
2. La suma se calcula sobre el original y sobre cada copia, y se comparan; guardada, sirve para
   comprobar la copia años después, en el archivo (véase «Archivo»: la «fijeza» del modelo OAIS).
3. La suma dice que un fichero ha cambiado, pero no dónde: la reparación sale de otra copia buena.

### La verificación en el archivo

El modelo OAIS pone la misma comprobación en la puerta del archivo. Su función de control de calidad
en la ingesta **«validates (QA results) the successful transfer of the SIP to the temporary storage
area. For digital submissions, these mechanisms might include Cyclic Redundancy Checks (CRCs) or
checksums associated with each data file, or the use of system log files to record and identify any
file transfer or media read/write errors.»** (CCSDS 650.0-M-3, § 4.2.3.3). Y dentro del archivo, una
función de comprobación de errores (*Error Checking*) **«provides statistically acceptable assurance
that no components of the AIP are corrupted in Archival Storage or during any internal Archival
Storage data transfer.»** (§ 4.2.3.4). Qué son SIP y AIP se explica en «Archivo».

### La verificación del contenido (oficio)

Una copia idéntica de un material defectuoso sigue siendo defectuosa. Antes de dar el material por
bueno para montar se revisa:

- Que está todo: número de clips, clips partidos, pistas de audio esperadas.
- Que es lo que dice ser: formato, resolución, cadencia y código de tiempo coinciden con lo
  anunciado (tema 4); el contenido corresponde a la noticia o al encargo.
- Que se ve y se oye: sin cortes, cuadros congelados, bloques de compresión, canales mudos o con
  ruido. Los niveles y la calidad técnica se miden como dice el tema 2; la ficha del puesto incluye
  **«Realizar el control técnico de calidad y corregir video y audio para su emisión y/o venta.»**
- Que se puede usar: procedencia y derechos del material de terceros (tema 10); imágenes sensibles.

El Libro de estilo de Canal Sur pide revisar la grabación en el propio lugar: **«Otra norma
elemental de prudencia es revisar la grabación en el mismo lugar de la misma para comprobar que es
correcta desde la perspectiva de la imagen y del sonido.»** (5.3.3, p. 82). Lo que no se detectó
allí se detecta en la ingesta; lo que no se detecta en la ingesta aparece en el montaje, o en
emisión.

## 5. Copias de seguridad

### Por qué

Hasta que el material está copiado, existe en un solo sitio: una tarjeta que se puede perder,
romper, borrar o formatear por error. Un fabricante lo dice en una línea: **«Be sure to back up the
data for protection.»** (Sony, *Help Guide ILCE-1*, «Notes on memory card»). La copia de seguridad
no es un trámite de archivo: es la protección de la jornada de trabajo (oficio).

El manual de DaVinci Resolve lo propone antes incluso de añadir el material al proyecto: **«clone all camera
original media onto a safe set of backup volumes, for redundancy in case any one volume fails.
Additionally, you should consider cloning all media to an off-site backup as well.»** (cap. 17,
p. 373).

### La regla 3-2-1

INCIBE la formula así: la regla 3-2-1 **«se refiere a disponer siempre de tres copias de seguridad de
un mismo tipo de información, en dos dispositivos distintos y, una de ellas, almacenarla en un lugar
diferente a los demás»** (INCIBE, «Definiendo mi estrategia de copias de seguridad», 29-09-2021).

Traducida a la sala (oficio, y cada casa tiene su procedimiento): el original (la tarjeta o el disco
recibido) hasta que haya dos copias comprobadas; una copia en el almacenamiento de trabajo, donde se
monta; y otra en un soporte o un sitio distinto (un disco que no está en la sala, el sistema de la
casa, el archivo). El *Clone Tool* de Resolve hace las dos copias a la vez, porque admite varios
destinos en un mismo trabajo (**«You can have more than one destination.»**, p. 373).

### Qué se copia, además del material

- El proyecto: guarda las decisiones de montaje, no el material, y se pierde o se corrompe como
  cualquier fichero. Las copias automáticas del proyecto (la carpeta *Attic* de Avid) están en el
  tema 15.
- Los metadatos que se han escrito a mano: Resolve permite exportarlos del *Media Pool* a un fichero
  **«.csv file that can be viewed and/or edited in any spreadsheet application, or an Avid Log
  Exchange (.ale) file if you need compatibility with Avid Media Composer.»** y volver a importarlos
  (cap. 18, p. 434).
- Los informes de suma de verificación y las listas de entrega: sin ellos no se puede demostrar
  después qué se copió y cuándo (oficio).

### Lo que no es una copia de seguridad: el RAID

Un RAID es un conjunto de discos que el sistema ve como uno solo (oficio):

| Nivel | Cómo escribe | Qué gana | Qué pierde |
|---|---|---|---|
| RAID 0 | *Striping*: distribuye los datos entre discos, sin redundancia | Velocidad y toda la capacidad | Ninguna seguridad: si cae un disco, se pierde todo |
| RAID 1 | *Mirroring*: duplica los datos de un disco en otro | Seguridad: aguanta la caída de un disco | La mitad de la capacidad |
| RAID 5 | *Striping* con paridad distribuida entre todos los discos | Velocidad y tolerancia a fallo con poca pérdida de capacidad | Necesita tres discos como mínimo; la reconstrucción es lenta |
| RAID 6 | Como el 5, con doble paridad | Aguanta la caída de dos discos | Más pérdida de capacidad y de velocidad de escritura |
| RAID 10 | Espejos agrupados en *striping* | Velocidad y seguridad juntas | La mitad de la capacidad, y hacen falta cuatro discos |

El número del nivel no es el número de discos: el RAID 1 necesita dos, porque el espejo necesita un
disco donde escribir y otro donde copiar. Y el RAID protege del fallo de un disco (de dos, en el
RAID 6), no de un borrado,
de un fichero corrupto que se copia a los dos lados ni de un robo o un incendio. Un RAID 0 ni
siquiera protege: si falla un disco, se pierde todo. No es una copia de seguridad; es lo que mantiene
vivo el trabajo mientras se hace (oficio).

Las siglas: *redundant array of independent disks*, conjunto redundante de discos independientes. Las
tres palabras dicen lo esencial: redundante —hay información de más, para poder reconstruir—,
conjunto —varios discos vistos como uno— e independientes —cada disco es una unidad completa—.

Cómo lo consigue el RAID 5: la paridad. El RAID 5 reparte los datos entre todos los discos, como el
RAID 0, pero añade en cada franja un bloque de paridad, calculado a partir de los demás y guardado en
un disco distinto cada vez. Si un disco cae, el sistema reconstruye lo que había en él a partir de
los otros y de la paridad.

| | Con tres discos |
|---|---|
| Capacidad útil | Dos discos de tres: se pierde el equivalente a uno en paridad |
| Discos que puede perder | Uno |
| Velocidad de lectura | Alta: lee de varios discos a la vez |
| Velocidad de escritura | Menor que la de lectura: hay que calcular la paridad |

La regla mnemotécnica que no falla: RAID 0, cero seguridad. RAID 1, un disco copiado en otro.

Mientras un RAID 5 reconstruye un disco caído trabaja sin protección: si cae otro antes de terminar,
se pierde todo (oficio, por la tabla: el RAID 5 sólo aguanta uno). Es el momento de no dar el
material por seguro y de tener la copia aparte al día.

## 6. Metadatos

### Qué son y quién los pone

Metadatos son los datos sobre el material: cuándo se grabó, con qué cámara y formato, qué código de
tiempo tiene cada cuadro, cómo se llama el clip, si es bueno o malo (oficio). Unos los pone la
cámara sola (fecha, formato, ajustes); otros dependen de lo que el operador haya configurado antes
(nombre, código de tiempo, bits de usuario); y otros los pone el operador mientras graba (marcas y
banderas). Los primeros no cuestan nada; los otros son los que ahorran tiempo en la redacción y en
el montaje, y los que se pierden si no se hacen en el momento.

En la sala se suman los del montador (oficio): la descripción del contenido, las palabras clave, el
nombre de cinta al digitalizar, las marcas en los clips y, sobre todo, el nombre y el estado de lo
que entrega. El manual de EBUCore resume por qué: **«"If you can't find it, you don't have it!"»**
(EBU Tech 3293, v. 1.10, p. 7).

### Los metadatos dentro del fichero

Los metadatos van con el material si se copia entero. Los contenedores profesionales los llevan
dentro (**«AVC-Intra supports MXF metadata.»**, Panasonic), y las cámaras guardan además ficheros de
gestión y el *proxy* en otras carpetas de la tarjeta (el menú ***[Update Media]*** de la Z200
**«Updates the management file on memory cards»**, p. 252). Copiar sólo el fichero de vídeo pierde
parte de esa información (véase «Ingesta»).

El nombre del fichero se puede cambiar y repetir; el identificador único que el formato MXF da a cada
paquete de material (el UMID) no: está en el tema 15, con la norma que lo define. El código de tiempo,
que es el metadato que numera cada cuadro, está en los temas 2 y 15.

### Los metadatos en el programa de edición

El manual de DaVinci Resolve 21 dedica al asunto su capítulo 18, «Using Clip Metadata», y lo abre
así: **«Once your metadata house is in order, you can use this metadata in the Cut, Edit, Color, and
Fairlight pages to find, sort, and organize the clips in your project, so you can work faster.»**
(p. 417). Lo que enseña, aplicado a la sala:

- Unos llegan solos: **«In many instances, metadata is also imported along with the media you've
  added to the Media Pool.»**; por ejemplo, los ficheros de sonido Broadcast WAVE **«can have quite a
  bit of metadata entered at the time of recording, such as scene and take numbers and channel names
  describing each microphone.»** (p. 418).
- Otros se escriben en el editor de metadatos: **«add information to each clip such as a Description,
  Shot and Scene designations, Take information, and possibly some useful keywords»** (p. 418).
- Para qué: **«the more metadata you associate with each clip, the more methods you have at your
  disposal for creating custom Smart Bins (for editing) and Smart Filters (for grading) with which to
  zero in on the clips you need for any given situation.»** (p. 418). Un *Smart Bin* es un *bin* que se
  llena solo con los clips que cumplen un criterio (tema 3).
- Las palabras clave se escogen de una lista para no escribirlas cada vez de una manera: el campo
  funciona así **«to facilitate consistency with keyword spelling by making it easy to reference both a
  built-in list of standardized keywords, as well as other keywords that you've already entered to
  other clips.»** (p. 420).
- Varios clips a la vez: se seleccionan en el *Media Pool* y se rellenan los campos una sola vez
  (p. 420).
- Y viajan: se exportan a CSV o a ALE y se importan en otro proyecto, **«automatically matching the
  relevant metadata to each corresponding clip.»** (p. 434).

Premiere y Avid tienen herramientas equivalentes (columnas de metadatos en el panel de proyecto y en
el *bin*); su organización está en los temas 3 y 15.

### Los metadatos de fichero de Adobe: XMP

La plataforma de metadatos de fichero de Adobe es XMP (*Extensible Metadata Platform*), y su
documentación nombra a Premiere como el programa desde el que se fija una de sus propiedades (el
nombre de cinta alternativo, más abajo). Lo que dice Adobe de ella (documentación de XMP, developer.adobe.com):

- Qué es: **«Adobe’s Extensible Metadata Platform (XMP) is a file labeling technology that lets you
  embed metadata into files themselves during the content creation process.»** Es decir, el dato va
  dentro del propio fichero.
- Qué recoge: **«meaningful information about a project (such as titles and descriptions, searchable
  keywords, and up-to-date author and copyright information)»**.
- Es norma: **«Since early 2012, XMP is also an ISO standard (16684-1).»**
- Admite otros esquemas: **«XMP is extensible — it can accommodate existing metadata schemas, so
  systems don’t need to be rebuilt from scratch.»**

Dentro de XMP, las propiedades se agrupan en espacios de nombres. Dos le importan al montador:

| Espacio de nombres (prefijo) | Qué recoge (literal de Adobe) |
|---|---|
| Dublin Core (`dc`) | **«The Dublin Core namespace provides a set of commonly used properties.»**, con los nombres y el uso que fija la iniciativa Dublin Core (DCMI) |
| Medios dinámicos (`xmpDM`) | **«This namespace specifies properties used by the Adobe dynamic media group.»** |

El Dublin Core es también la base de EBUCore (véase «La norma del sector: EBUCore»): EBUCore se
define como extensión del Dublin Core, y el espacio `dc` de XMP toma de él sus nombres y su uso. Del
espacio de medios dinámicos,
las propiedades que tocan la ingesta y la digitalización de este tema:

- `xmpDM:tapeName`: **«The name of the tape from which the clip was captured, as set during the
  capture process.»**
- `xmpDM:altTapeName`: **«An alternative tape name, set via the project window or timecode dialog in
  Premiere.»**
- `xmpDM:startTimecode`: **«The timecode of the first frame of video in the file, as obtained from the
  device control.»**
- `xmpDM:good`: **«A checkbox for tracking whether a shot is a keeper.»**
- `xmpDM:logComment`: **«User’s log comments.»**
- `xmpDM:scene` y `xmpDM:shotName`: **«The name of the scene.»** y **«The name of the shot or
  take.»**

La consecuencia en la sala (oficio): lo que se escribe en el XMP del fichero viaja con él a otro
proyecto y a cualquier programa que lea XMP; lo que sólo se anota en el proyecto se queda en el
proyecto. Qué campos del panel de metadatos de Premiere van al fichero y cuáles se quedan en el
proyecto lo explica la ayuda del programa, que no se ha podido leer (véase «Lo que este tema no da»).

### Los metadatos en el sistema de la casa

Los tres datos que se capturan en la ingesta y que deciden si el material se encontrará después:
quién lo trae, de qué es y qué derechos tiene. Un material sin esos tres datos está dentro del
sistema y está perdido.

Es oficio, y el sistema los guarda en su catálogo. Qué hace un sistema de gestión de activos de
medios (MAM) con ellos, en cinco funciones:

| Función | Qué resuelve |
|---|---|
| Catálogo | Que cada material tenga sus datos descriptivos y se pueda buscar |
| Versiones | Que se sepa cuál es la buena y de dónde sale cada una |
| Baja resolución | Que se pueda ver y marcar el material sin mover el fichero grande |
| Ciclo de vida | Cuánto se guarda cada cosa y cuándo se borra o se archiva |
| Permisos | Quién puede ver, usar y borrar qué |

La gestión de activos digitales (DAM) es el término general —vale para fotos, documentos y audio—;
la de activos de medios (MAM) es la especializada en audiovisual, con lo que eso añade: código de
tiempo, subclips, versiones de montaje y derechos por ventana de explotación. El MAM y su flujo, en
el tema 13. Qué sistema y qué campos usa CSRTV no consta en un documento publicado.

### La norma del sector: EBUCore

Para que los metadatos sirvan fuera de la casa que los escribe hace falta un vocabulario común. En
televisión europea es EBUCore, de la EBU (EBU Tech 3293, *EBU Core Metadata Set*, v. 1.10, Ginebra,
abril de 2020):

- Qué es: **«EBUCore is a collection of basic descriptive and technical/structural metadata elements
  used to describe audiovisual content as an extension of the Dublin Core.»** Y en una línea:
  **«EBUCore is the Dublin Core for media.»** (§ 2.1).
- Para qué: **«EBUCore has been designed to describe audio, video and other resources for a wide
  range of broadcasting applications including archives, exchange and production in the context of a
  Service Oriented Architecture.»** (introducción, p. 3). **«This specification addresses the
  creation, management, and preservation of audiovisual material.»** (p. 7).
- Por qué el Dublin Core: **«EBUCore is based on the Dublin Core to maximise interoperability with
  the community of Dublin Core users such as the European Digital Library 'Europeana'.»** (p. 3). El
  Dublin Core, según la misma especificación, **«is being used as a core metadata set by librarians and
  museums in cultural heritage projects.»** (p. 7).
- Qué exige: **«Metadata is the glue between production operations particularly when moving towards
  Service Oriented Architecture and file-based production. Documenting audiovisual resources with
  EBUCore information is a minimum requirement corresponding to fundamental investment with
  guaranteed return.»** (p. 7).
- No es sólo de archivo: **«The EBUCore is recommended when describing and providing access to
  audiovisual content and is not limited to archives.»** (p. 7). Y la versión 1.10 declara que
  **«EBUCore is fully compatible with IMF in its different representation formats, for static or
  dynamic metadata.»** (§ 2.3); el IMF, formato de entrega, está en el tema 4.

Dos avisos. La especificación se presenta como **«a living specification. It is actively maintained
and enriched.»** (§ 2.1): el tema cita la versión 1.10 sin afirmar que sea la última. Y el diccionario
de elementos de metadatos de la SMPTE (RP 210) figura como retirado en el catálogo de la SMPTE: no se
cita como vigente.

Metadatos descriptivos y técnicos, la distinción de EBUCore, aplicada a un clip (oficio):

| Clase | Qué dice | Ejemplos | Quién lo pone |
|---|---|---|---|
| Descriptivos | De qué es el material | Título, descripción, lugar, personas, palabras clave, derechos | Redacción, montador, documentación |
| Técnicos | Cómo es el fichero | Formato, códec, resolución, cadencia, pistas de audio, duración, código de tiempo | La cámara y el sistema, solos |

## 7. Archivo

### Qué le toca al montador

La ficha del puesto le da **«Compactar para el archivo de material audiovisual.»**; la catalogación
es de documentación (tema 9). El convenio no define «compactar». En un flujo de ficheros se entiende
como oficio: reducir lo que se guarda a lo que merece guardarse (la pieza emitida y el bruto útil,
sin los duplicados, las pruebas ni los ficheros intermedios) y entregarlo identificado, completo y
comprobado. Qué conserva CSRTV del bruto, con qué formato y con qué plazos no consta en un documento
publicado.

### Material de trabajo y material de archivo

Los dos almacenamientos de una redacción, y por qué son dos:

| | Almacenamiento de producción | Almacenamiento de archivo |
|---|---|---|
| Qué guarda | Lo que está en uso | Lo que se conserva |
| Cómo se accede | Inmediato, por red de bloques | Diferido: puede estar en cinta |
| Coste por terabyte | Alto | Bajo |
| Qué lo dimensiona | Cuánto material vivo hay a la vez | Cuánto hay que conservar y cuánto tiempo |

Es un esquema de oficio. La consecuencia para la sala: lo que se deja en el almacenamiento de
trabajo no está archivado, y lo que está archivado no se monta directamente; se recupera antes.

### El modelo de referencia: OAIS

El modelo con el que se describe un archivo digital es el OAIS. Lo publica el CCSDS como práctica
recomendada (CCSDS 650.0-M-3, *Reference Model for an Open Archival Information System (OAIS)*,
«Magenta Book», diciembre de 2024), y su objeto es **«to define the CCSDS and International
Organization for Standardization (ISO) Reference Model for an Open Archival Information System
(OAIS).»** (§ 1.1). Es un modelo, no un producto ni una norma de televisión; sirve para entender qué
tiene que hacer cualquier archivo.

- Qué es un OAIS: **«An OAIS is an Archive system consisting of hardware, software, information, and
  policy-based processes and procedures put in place and operated by an organization and its staff.
  The organization has accepted the responsibility to preserve information and make it available for
  a Designated Community.»** (§ 1.1). La comunidad designada es el grupo de usuarios que tiene que
  poder entender la información; en una televisión, sus redactores, montadores y documentalistas
  (aplicación de oficio).
- Qué significa «abierto»: **«The term 'Open' in OAIS is used to imply that this Recommended
  Practice, as well as future related Recommended Practices and standards, are developed in open
  forums, and it does not imply that access to the Archive is unrestricted.»** (§ 1.1).
- Qué es largo plazo: **«A period of time long enough for there to be concern about the impacts of
  changing technologies, including support for new media and data formats, and of a changing
  Designated Community or changes to the Designated Community's Knowledge Base, on the information
  being held in an OAIS. This period extends into the indefinite future.»** (§ 1.6.2, terminología).
- Qué abarca: **«a full range of archival information preservation functions including ingest,
  archival storage, data management, access, and dissemination. It also addresses the migration of
  digital information to new media and forms»** (§ 1.1).

Los tres paquetes de información, que es lo más preguntable (terminología del § 1.6.2):

| Paquete | Definición literal | En una televisión (oficio) |
|---|---|---|
| SIP, de entrega | **«An Information Package that is delivered by the Producer to the OAIS for use in the construction or update of one or more AIPs and/or the associated Descriptive Information.»** | Lo que la sala entrega al archivo: la pieza, el bruto seleccionado y sus datos |
| AIP, de archivo | **«An Information Package, consisting of the Content Information and the associated Preservation Description Information (PDI), which is preserved within an OAIS.»** | Lo que el archivo guarda, con lo necesario para conservarlo |
| DIP, de difusión | **«An Information Package, derived from one or more AIPs, and sent by Archives to the Consumer in response to a request to the OAIS.»** | Lo que el archivo devuelve a quien lo pide: una copia para montar |

La PDI se compone de cinco clases de información: **«Provenance Information, Context Information,
Reference Information, Fixity Information, and Access Rights Information.»** (§ 1.6.2). Tres de ellas
le suenan al montador:

- Procedencia: **«The information that documents the history of the Content Data Object. This
  information tells the origin or source of the Content Data Object, any changes that may have taken
  place since it was originated, and who has had custody of it since it was originated.»**
- Referencia: **«The information that is used as an identifier for the Content Data Object.»**; el
  ejemplo del modelo es el ISBN de un libro.
- Fijeza: **«The information which documents the mechanisms that ensure that the Content Data Object
  has not been altered in an undocumented manner.»** Es la suma de verificación de «Verificación»,
  guardada con el material.

El modelo divide el archivo en **«six functional entities»** (§ 4.2.2), que son, por los rótulos del
§ 4.2.3: ingesta (*Ingest*), almacenamiento de archivo (*Archival Storage*), gestión de datos (*Data
Management*), administración (*Administration*), planificación de la conservación (*Preservation
Planning*) y acceso (*Access*). Dentro del almacenamiento, dos funciones conectan con las copias de
seguridad:

- Renovar soportes: **«The Replace Media function provides the capability to reproduce the AIPs over
  time.»**; en ella, dice el modelo, la información de contenido y la PDI **«should not be
  altered»** (§ 4.2.3.4). Es la migración: el material pasa de un soporte
  que envejece a otro nuevo.
- Recuperar ante desastres: **«The Disaster Recovery function provides a mechanism for duplicating the
  digital contents of the Archive collection and, for example, storing the duplicate in a physically
  separate facility.»** (§ 4.2.3.4). Es la copia en otro sitio de la regla 3-2-1.

### La cinta de archivo: la LTO

Lo que ya no se toca pasa al archivo. La LTO es una tecnología de almacenamiento en cinta magnética
de alta capacidad, escalable y regrabable; «abierta» porque es una norma abierta, fabricada por
varias casas (oficio). Sus ventajas: el coste por terabyte más bajo en volúmenes grandes; una cinta
guardada no consume energía; dura décadas en condiciones de archivo; y, fuera de la biblioteca, no
está en la red. Su desventaja fija su uso: el acceso es secuencial y lento. No es almacenamiento de
trabajo, es archivo (oficio).

Lo que dice hoy el programa LTO (página «LTO Technology Roadmap», lto.org, leída el 25-09-2026):

- Qué es: **«It's a powerful, scalable and adaptable tape format that helps address the growing
  demands of data protection. It's also an open format, licensed by some of the most prominent names
  in the storage industry to ensure a broad range of compatible tape drives and cartridges.»**
- Generación vigente: **«LTO technology is currently in its 10th generation»**.
- Capacidad: **«LTO-10 specifications support tape cartridge storage with a compressed capacity of up
  to 100 TB.»** La cifra es comprimida; la capacidad nativa no la da la página en texto. La de
  compatibilidad entre generaciones («LTO Generation Compatibility Details») da dos tamaños de
  cartucho: **«LTO-10 drives can only read and write to LTO-10 media. But they support both 30 TB and
  40 TB LTO-10 media interchangeably.»**; no dice si esas cifras son nativas. El vídeo ya
  comprimido apenas se vuelve a comprimir, así que para material audiovisual la cifra útil se acerca
  más a la nativa que a la comprimida (oficio).
- Velocidad: **«the newest LTO-10 tape drives support data transfer rates of up to 1200 MB/s»**; la
  frase lleva una llamada a la nota **«Assuming a 2.5:1 compression»**, es decir, también es una
  cifra con compresión.
- Compatibilidad hacia atrás, que cambia con las generaciones:

| Generaciones | Qué admite la unidad (literal) |
|---|---|
| Hasta la 7.ª | **«support writing back one generation and reading back two generations»** |
| 8.ª y 9.ª | **«are able to write back and read back one generation»** |
| 10.ª | **«does not support backwards compatibility due to a redesign of the drive head to eliminate the need for initialization»** |

La consecuencia para un archivo (oficio): cada cambio de generación obliga a planificar la migración
de las cintas viejas mientras quede una unidad que las lea. Es la función de renovar soportes del
modelo OAIS.

### La LTFS: la cinta como un disco

La LTFS permite leer una LTO como si fuera un disco, con sus ficheros y carpetas (página «Linear Tape
File System», lto.org, leída el 25-09-2026):

- **«The Linear Tape File System (LTFS) makes it easy to quickly and precisely locate and retrieve any
  item of data stored on an LTO Ultrium tape cartridge.»**; está **«included with all generations
  since LTO-5»**.
- Cómo: **«LTFS partitioning allows a portion of the tape to be reserved for indexing, which tells the
  drive precisely where in the tape a file is stored. The second partition holds the actual file.»**
- Para el usuario: el índice se presenta **«in a simple, easy-to-use format that allows for
  drag-and-drop capabilities.»**

La cinta sigue siendo secuencial: la LTFS dice dónde está cada fichero, pero la unidad tiene que
llegar hasta él (oficio).

### El material de archivo en el montaje

Lo que sale del archivo vuelve a la sala como un material más, con dos reglas del Libro de estilo que
están en los temas 1, 7 y 9: la armonía con el material nuevo y el rótulo. La del rótulo: **«En
rotulación debe hacerse constar claramente que es material de ‘Archivo’ durante todo el tiempo en que
la imagen permanezca en pantalla, al menos con suficiente margen como para ser leído sin apremio por
el espectador.»** (9.9.1, p. 166). Con su salvedad de contexto: está en el capítulo 9 («Asuntos
comprometidos»), apartado 9.9 («Material objetable»), en el mismo párrafo que manda «tratar» en la
edición el archivo **«cuando sirvan para ilustrar reportajes sobre delincuencia, malos tratos, asuntos
judiciales o cualquier variante reflejada en este capítulo»**; rotular siempre el archivo, fuera de
esos reportajes, es costumbre de oficio, no regla escrita en ese pasaje. Los derechos de uso del material de archivo y de
terceros, en el tema 10.

## Aplicación práctica: del material que llega al material que se archiva

Un reportaje para un programa semanal: llegan dos tarjetas de cámara de una grabación de tres días,
una cinta de archivo con imágenes de hace veinte años y un clip que envía un corresponsal por red. Qué
hace el montador (oficio, con los datos del tema):

| Momento | Qué hace | Por qué |
|---|---|---|
| Tarjetas | Las bloquea; las clona enteras, con su estructura de carpetas, a dos destinos a la vez (almacenamiento de trabajo y un segundo soporte), con MD5 o XXHASH64; guarda el informe de sumas | Proteger el original; copia comprobada; regla 3-2-1 |
| Revisión | Cuenta clips, busca clips partidos y pistas mudas, comprueba formato, cadencia y código de tiempo | Una copia idéntica de un material defectuoso sigue siendo defectuosa |
| Tarjetas, después | No las devuelve para formatear hasta tener dos copias comprobadas | Formatear es borrar |
| Cinta | La digitaliza con captura registrada: nombre de cinta único, entradas y salidas de los tramos útiles, metadatos antes de capturar; captura por lotes | Poder reconformar después; saber de dónde sale cada clip |
| Clip del corresponsal | Comprueba que ha llegado entero (se abre y se reproduce hasta el final) antes de confirmar la recepción; si viene por FTP sin cifrar, lo avisa | Transferencia comprobada; seguridad del envío |
| Metadatos | Descripción, lugar, personas, palabras clave de la lista común, origen y derechos del material de archivo y del corresponsal | Encontrar el material; saber qué se puede usar |
| Montaje | Monta desde el almacenamiento de trabajo, no desde la tarjeta ni desde un disco externo; rotula como archivo las imágenes de archivo | Que no se pierda el enlace; Libro de estilo 9.9.1 (escrito para reportajes de sucesos; fuera de ellos, oficio) |
| Cierre | Compacta: la pieza emitida y el bruto útil, identificados, con sus metadatos y sus sumas, al procedimiento de archivo de la casa; limpia el almacenamiento de trabajo sólo cuando el archivo confirma | Ficha del puesto; paquete de entrega (SIP) completo y comprobado |

## Documentos técnicos que el tema cita

| Documento | Qué se toma |
|---|---|
| X Convenio Colectivo de la RTVA, BOJA núm. 240, de 10-XII-2014, anexo III, ficha 5212206 (p. 190) | Objeto del puesto y tareas: configurar y preparar materiales, enlaces, compactar para el archivo, control de calidad, repicar cintas |
| *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía*, 2004 | Revisar la grabación en el lugar (5.3.3, p. 82); rótulo de archivo (9.9.1, p. 166) |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual* | *Clone Tool* y sumas de verificación (cap. 17, pp. 373-374); metadatos de clip (cap. 18, pp. 417-420 y 434); captura desde cinta (cap. 24, pp. 558-564) |
| Adobe, «Ingest and proxy workflows in Premiere» (actualizada el 7-1-2026) | Qué es la ingesta en Premiere; verificación al copiar; ingesta y *proxy* combinados |
| Adobe, documentación de XMP (developer.adobe.com/xmp/docs) y espacios de nombres «Dublin Core namespace» y «XMP Dynamic Media namespace» | Qué es XMP, norma ISO 16684-1, extensibilidad; propiedades `dc` y `xmpDM` |
| EBU Tech 3293, *EBU Core Metadata Set (EBUCore)*, v. 1.10, abril de 2020 | Qué es EBUCore, su base en el Dublin Core, su alcance y su compatibilidad con IMF |
| CCSDS 650.0-M-3, *Reference Model for an Open Archival Information System (OAIS)*, diciembre de 2024 | Definición de OAIS, «abierto», largo plazo, SIP, AIP, DIP, PDI y sus componentes, seis entidades funcionales, control de calidad en la ingesta, comprobación de errores, renovación de soportes, recuperación ante desastres |
| LTO Program, «LTO Technology Roadmap», «LTO Generation Compatibility Details» y «Linear Tape File System» (lto.org) | Definición de LTO, generación vigente, capacidad y velocidad de la LTO-10, cartuchos de 30 y 40 TB, compatibilidad hacia atrás; LTFS |
| Catálogo de la SMPTE, RP 210 | Retirada |

Del tema cerrado de Cámara Operador (tema 7) vienen, con sus fuentes: Sony, *PXW-Z200/HXR-NX800
Help Guide* (2024) y *Help Guide ILCE-1*; Panasonic, *AVC-Intra FAQ*; Digital Preservation
Coalition, *Digital Preservation Handbook*, «Fixity and checksums»; INCIBE, «Definiendo mi estrategia
de copias de seguridad» (29-09-2021).

## Lo que este tema no da, y dónde está

- Qué sistema de ingesta, almacenamiento compartido, MAM y archivo usa CSRTV; quién ingesta; qué se
  conserva del bruto, con qué formato y durante cuánto tiempo; qué procedimiento sigue el material
  externo: no constan en un documento publicado localizado.
- Qué significan hoy «compactar» y «repicar» en la ficha del puesto: el convenio no los define.
- La capacidad nativa de la LTO-10: las páginas del programa LTO leídas dan 100 TB comprimidos y
  cartuchos de 30 TB y 40 TB, sin decir si estas son nativas.
- Qué campos del panel de metadatos de Premiere se escriben en el XMP del fichero y cuáles se quedan
  en el proyecto, y cómo se enlazan: la ayuda de Premiere que lo explica no se ha podido leer (el
  servidor de Adobe rechazó la descarga).
- La edición ISO equivalente del modelo OAIS (ISO 14721) y su año: no se ha confirmado; se cita el
  documento del CCSDS.
- Si hay una versión de EBUCore posterior a la 1.10, y la lista de elementos del Dublin Core: no se han
  leído.
- Con qué algoritmo verifica Premiere la copia al ingestar: la página de Adobe no lo dice.
- Los proxies, el reenlace y el *Redigitize*, en el tema 3; formatos, códecs, contenedores, MXF y
  SDI/IP, en el tema 4; la señal, sus niveles y el código de tiempo, en el tema 2; el control de
  calidad y la corrección, en los temas 2 y 7; el reparto con documentación y el archivo en el
  convenio, en el tema 9; los derechos del material de archivo y de terceros, en el tema 10; el MAM,
  el sistema de redacción y la automatización, en el tema 13; el directo y los enlaces, en el tema 14;
  la organización de proyectos, la nomenclatura, el UMID y la carpeta *Attic*, en el tema 15.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| X Convenio Colectivo de la RTVA, BOJA núm. 240, de 10-XII-2014, anexo III, ficha 5212206, p. 190 | «El punto en la ficha del puesto»; tareas citadas en 1, 2, 3, 4 y 7 | 25-09-2026 |
| *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004 | Revisar en el lugar (5.3.3, p. 82); rótulo de archivo (9.9.1, p. 166) | 25-09-2026 |
| *DaVinci Resolve 21 Reference Manual*, cap. 17 (pp. 373-374), cap. 18 (pp. 417-420, 434) y cap. 24 (pp. 558-564) | Ingesta en el programa; captura desde cinta; algoritmos de verificación; copia a varios destinos y fuera de la casa; metadatos de clip y su exportación | 25-09-2026 |
| Adobe, «Ingest and proxy workflows in Premiere», actualizada el 7-1-2026 | Ingesta en Premiere y su verificación | 25-09-2026 |
| Adobe, «XMP (Extensible Metadata Platform)» (developer.adobe.com/xmp/docs) y, en el repositorio adobe/xmp-docs, «Dublin Core namespace» y «XMP Dynamic Media namespace» | Los metadatos de fichero de Adobe: XMP | 25-09-2026 |
| EBU Tech 3293 v. 1.10 (abril de 2020), pp. 3, 7 y 8 | EBUCore | 25-09-2026 |
| CCSDS 650.0-M-3 (diciembre de 2024), §§ 1.1, 1.6.2, 4.2.2, 4.2.3.3 y 4.2.3.4 | Modelo OAIS | 25-09-2026 |
| lto.org, «LTO Technology Roadmap», «LTO Generation Compatibility Details» y «Linear Tape File System» | LTO-10 y LTFS | 25-09-2026 |
| Catálogo de documentos de la SMPTE, RP 210 | Retirada | 25-09-2026 |
| Tema 7 del específico de Cámara Operador (cerrado) y sus fuentes | Pasajes copiados: qué es la ingesta, ingesta de una tarjeta, envío desde el lugar y por FTPES, suma de verificación, por qué copiar, regla 3-2-1, RAID, qué son los metadatos y los metadatos en el fichero, LTO | 24-09-2026 (lectura del tema cerrado) |

Oficio sin norma detrás, y así se declara: el sentido técnico de «compactar» y «repicar»; las etapas
del flujo de una redacción y la regla de los datos descriptivos; los tipos de ingesta por origen y la
grabación por partida doble del directo; la diferencia entre ingestar e importar; lo que se revisa al
digitalizar; el papel del nombre de cinta; las dos maneras de transferir; NAS y SAN; las tres redes y
su separación; la verificación de contenido; la regla 3-2-1 aplicada a la sala; los niveles de RAID,
la paridad y el riesgo de la reconstrucción; los tres datos que se capturan en la ingesta; las
funciones de un MAM y la distinción entre DAM y MAM; la tabla de metadatos descriptivos y técnicos; los dos espacios de nombres de XMP que importan al montador y lo que viaja con el fichero frente a lo que se queda en el proyecto;
los dos almacenamientos; la lectura de la LTO para vídeo ya comprimido; el supuesto práctico. Es
cálculo, y se puede rehacer: el tiempo de una transferencia.
