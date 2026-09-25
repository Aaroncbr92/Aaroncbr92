# Tema 13 del específico de Operador/a Montador/a de Vídeo · Automatización, plantillas, MAM/PAM, newsroom y flujos de producción integrados

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Montador/a de Vídeo · punto 13 |
| Sirve para | Operador/a Montador/a de Vídeo de Canal Sur (grupo B04) y la prueba práctica del puesto |
| Fuente | Sin norma. X Convenio Colectivo de la RTVA (anexo III, fichas del puesto y del encargado); Libro de estilo de Canal Sur Televisión (2004), cap. 6, para la escaleta; Manfredi (2010) para el sistema de redacción en Canal Sur; especificación del protocolo MOS en su web oficial (mosprotocol.com); EBU Tech 3293 (EBUCore) para los metadatos; documentación de fabricante (Avid, Blackmagic Design, Adobe) para los productos que se citan como ejemplo; lo demás, oficio declarado como tal |
| Redacción que se estudia | X Convenio Colectivo de la RTVA (BOJA núm. 240, de 10-XII-2014); páginas del proyecto MOS (versiones vigentes 4.0, 2.8.5 y 3.8.4) y especificaciones 2.8.5 y 4.0; EBU Tech 3293 v1.10 (abril de 2020); manual de DaVinci Resolve 21; páginas de ayuda de Adobe Premiere y de producto de Avid; todo leído el 25-09-2026. Libro de estilo de Canal Sur (1.ª ed., marzo de 2004) y Manfredi (2010), leídos el 24-09-2026 |
| Extensión | 9.300 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Corporación de Radio y Televisión Española (RTVE); Boletín Oficial de la
Junta de Andalucía (BOJA); Unión Internacional de Telecomunicaciones (UIT); Unión Europea de Radiodifusión (EBU, *European Broadcasting Union*); gestión de activos de medios (MAM, *media asset management*); gestión de activos de
producción (PAM, *production asset management*); gestión de activos digitales
(DAM); sistema informático de redacción (NRCS, *newsroom computer system*, que la
especificación MOS abrevia NCS); protocolo de comunicaciones con servidores de objetos de medios
(MOS, *Media Object Server Communications Protocol*; «un MOS» es también el propio servidor);
generador de caracteres (CG, *character generator*), el equipo que compone los rótulos; la familia de
protocolos de internet (TCP/IP); lenguaje de marcas extensible (XML), el
formato de los ficheros de ajustes que se intercambian; interfaz de programación de aplicaciones
(API). Palabras en inglés que el tema usa porque así las rotula el programa o la fuente: *newsroom*
(la redacción y, por extensión, su sistema informático), *rundown* (escaleta), *playlist* (lista de
reproducción), *running order* (orden de emisión), *proxy* (copia ligera de trabajo), *preset* (ajuste
guardado), *watch folder* (carpeta vigilada), *render* (cálculo y escritura del fichero de salida),
*plugin* (módulo que se añade a un programa). AP, ENPS, FLOW, NEXIS y Cloud UX son nombres de empresa o de
producto que aparecen dentro de citas de fabricante y que el tema no desarrolla. «El convenio» es el X Convenio Colectivo de la RTVA; «el
Libro de estilo», el de Canal Sur Televisión de 2004.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.30, punto 13): «Automatización,
> plantillas, MAM/PAM, newsroom y flujos de producción integrados.»

Qué se puede preguntar: qué tarea del convenio liga al Operador/a Montador/a con la emisión
automatizada y qué hace el encargado antes de ella; qué pieza ejecuta la escaleta en la emisión y por
qué la emisión se separa del resto; qué automatiza el propio sistema de edición (carpetas vigiladas,
tareas en segundo plano, cola de *render*, *render* remoto, integraciones por *scripts*) y qué no
automatiza; qué es una plantilla de rótulo, de exportación o de nombre, qué es un fichero .mogrt, en qué formato se exportan los
*presets* de Resolve y qué *preset* aplica por defecto Media Encoder; qué es una variable de metadatos;
qué funciones tiene un MAM, qué diferencia un MAM de un DAM y qué se entiende por PAM (y si hay
definición normalizada); para qué sirve la copia de baja resolución; qué dice EBUCore de los
metadatos; qué contiene un sistema de redacción y qué hace útil su escaleta; qué es MOS, entre quién
se habla, qué tres tipos de mensajes intercambia, en qué formato van y por qué puertos, quién lo desarrolla, si es norma oficial y cuáles
son sus versiones vigentes; qué dice el Libro de estilo de la escaleta y de su nombre; qué sistema
consta en Canal Sur y con qué fecha; qué tareas da la ficha del puesto y si son lista cerrada; cuáles son las etapas del flujo integrado y qué atraviesa
todas; qué vías de ingesta hay y qué exige cada una; por qué la edición de informativos se hace sobre
copia ligera y qué es editar mientras se ingesta; qué es el conformado; qué almacenamientos y redes
conviven y por qué se separan; cómo se degrada un flujo cuando falla una pieza. En la prueba práctica:
seguir una pieza de la ingesta a la emisión y resolver un cambio de escaleta con el flujo integrado.

<!-- indice -->

## Índice

- [De dónde sale este tema](#de-dónde-sale-este-tema)
- [1. Automatización](#1-automatización)
  - [Qué dice el convenio](#qué-dice-el-convenio)
  - [La emisión automatizada](#la-emisión-automatizada)
  - [Qué automatiza el propio sistema de edición](#qué-automatiza-el-propio-sistema-de-edición)
- [2. Plantillas](#2-plantillas)
  - [Qué es una plantilla](#qué-es-una-plantilla)
  - [Plantillas de rótulo](#plantillas-de-rótulo)
  - [Plantillas de salida: los *presets*](#plantillas-de-salida-los-presets)
  - [Plantillas de nombre: las variables de metadatos](#plantillas-de-nombre-las-variables-de-metadatos)
- [3. MAM/PAM](#3-mampam)
  - [Qué son, y qué no hay](#qué-son-y-qué-no-hay)
  - [Qué hace un MAM](#qué-hace-un-mam)
  - [MAM y PAM: la diferencia es de oficio](#mam-y-pam-la-diferencia-es-de-oficio)
  - [La copia de baja resolución](#la-copia-de-baja-resolución)
  - [Los metadatos, el pegamento del sistema](#los-metadatos-el-pegamento-del-sistema)
  - [El MAM desde la sala de edición](#el-mam-desde-la-sala-de-edición)
  - [Dónde vive el material](#dónde-vive-el-material)
- [4. Newsroom](#4-newsroom)
  - [El sistema de redacción](#el-sistema-de-redacción)
  - [El protocolo MOS](#el-protocolo-mos)
  - [Un sistema de redacción de mercado](#un-sistema-de-redacción-de-mercado)
  - [El sistema de redacción en Canal Sur](#el-sistema-de-redacción-en-canal-sur)
  - [La edición dentro de la redacción](#la-edición-dentro-de-la-redacción)
- [5. Flujos de producción integrados](#5-flujos-de-producción-integrados)
  - [Qué es un flujo integrado](#qué-es-un-flujo-integrado)
  - [La entrada: vías de ingesta](#la-entrada-vías-de-ingesta)
  - [Las redes que sostienen el flujo](#las-redes-que-sostienen-el-flujo)
  - [Cuando algo falla](#cuando-algo-falla)
  - [El montador en el flujo integrado](#el-montador-en-el-flujo-integrado)
- [Aplicación práctica](#aplicación-práctica)
  - [Una pieza de la ingesta a la emisión](#una-pieza-de-la-ingesta-a-la-emisión)
  - [Un cambio de escaleta con el flujo integrado](#un-cambio-de-escaleta-con-el-flujo-integrado)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## De dónde sale este tema

Ninguna norma legal regula cómo se integran la redacción, la gestión de medios, la edición y la
emisión de una televisión. Lo publicado por la casa es poco: el convenio pone en la ficha del puesto
una tarea de emisión automatizada; el Libro de estilo fija qué es la escaleta y cómo se cambia; y un
capítulo universitario de 2010 nombra el sistema de redacción que entonces usaba Canal Sur. Lo técnico
sale de fuentes publicadas que se citan una a una: la especificación del protocolo MOS en la web de
su proyecto, la especificación EBUCore de la EBU y la documentación de los fabricantes, que describe
sus propios productos y se cita como ejemplo, no como regla del sector. El resto es costumbre de
oficio, y así se dice en cada caso.

Una advertencia de vocabulario: MAM, PAM y *newsroom* son palabras de la industria, no términos
definidos por un organismo de normalización. No se ha encontrado una definición de la UIT, la EBU o la
SMPTE (Society of Motion Picture and Television Engineers) para PAM ni para MAM; donde el tema las
distingue, lo hace como oficio.

## 1. Automatización

### Qué dice el convenio

Automatizar es encargar a un sistema una operación que se repite, para que la ejecute sin que nadie
la haga a mano cada vez (definición de oficio). En la ficha del Operador/a Montador/a de Vídeo
(código 5212206, anexo III del convenio, BOJA núm. 240, p. 190) hay una tarea que lo liga directamente
con la emisión automatizada:

> **«Etiquetar, grabar e introducir en base de datos, la información para la emisión automatizada de
> programas y bloques publicitarios.»**

Y la ficha del encargado del área, **«ENCARGADO OPERACIÓN Y MONTAJE VIDEO»** (código 5212204, p. 127),
tiene entre sus tareas **«Realizar todas las operaciones necesarias previas para la posterior emisión
automatizada de la programación.»**

El convenio no dice qué sistema de automatización usa la casa ni qué campos lleva esa base de datos.
Lo que la tarea sí deja claro es el reparto: la máquina emite; el montador prepara lo que la máquina
necesita para emitir bien, que es el material grabado, su etiqueta y sus datos en la base de datos.
Si el dato está mal, la automatización lo ejecuta mal con toda exactitud.

### La emisión automatizada

Cómo funciona, como oficio (el pasaje sale de un temario de RTVE que no cita fuente):

| Pieza | Qué hace |
|---|---|
| Escaleta de emisión | Dice qué sale y en qué orden, y viene del sistema de redacción |
| Servidor de emisión | Reproduce las piezas en el instante previsto |
| Automatización | Ejecuta la escaleta: dispara servidor, grafismo y conmutación |

El principio de diseño que gobierna esa parte: la emisión se separa de todo lo demás. Sus
servidores son propios, su almacenamiento es propio y su red es propia, porque es el único punto
del sistema donde un fallo se ve en antena.

Lo que eso pide a la sala de montaje (oficio): que la pieza tenga exactamente el nombre o el
identificador que la escaleta espera, porque la automatización la busca por él (en Canal Sur el nombre
de un vídeo en escaleta no se cambia: epígrafe 4); que su duración real sea la anunciada, porque la
escaleta cronometra con ella; y que esté terminada y en el servidor antes de su hora, porque la
automatización no espera. El vídeo que llega tarde al servidor no sale aunque esté montado.

### Qué automatiza el propio sistema de edición

La automatización no es sólo la de emisión. Los programas de edición y sus aplicaciones auxiliares
automatizan tareas repetidas de la sala. Lo que sigue es lo documentado por los fabricantes en los
productos leídos:

- **Carpetas vigiladas.** El Blackmagic Proxy Generator, programa auxiliar de DaVinci Resolve,
  **«can automatically generate proxy media from master video files placed in a watch folder»**
  (genera automáticamente copias *proxy* de los ficheros que se dejan en una carpeta vigilada). Esas
  carpetas **«are constantly monitored»**: cuando entra un fichero nuevo, el programa **«automatically
  transcodes those new files into proxy media, without any additional human interaction needed»**. Se
  pueden tener tantas como se quiera, con una condición: que el disco tenga sitio para el original y
  para la copia. Las copias se escriben en una subcarpeta llamada «Proxy» junto al original, y por eso
  ninguna carpeta vigilada puede llamarse así (manual de Resolve 21, cap. 8, p. 215). Nada de eso
  ocurre hasta que el programa se pone en marcha: configuradas la carpeta y el formato de la copia, se
  pulsa *Start* en el panel *Processing* para **«automatically transcode and monitor your watch
  folders»**, y *Stop* lo detiene en cualquier momento (la barra espaciadora alterna uno y otro). Una
  carpeta con clips aún sin convertir figura como *Waiting*, **«waiting for the Blackmagic Proxy Generator to be
  started or for a folder ahead of it in the queue to be finished»** (cap. 8, pp. 216-217).
- **Tareas en segundo plano.** Resolve **«supports background rendering for certain computationally
  intensive operations, including background renders, quick exports, and proxy generation»**; entre
  las tareas que se pueden mandar al segundo plano están la transcripción y la generación de *proxies*.
  Quien monta sigue trabajando mientras la máquina calcula. Con una salvedad: como consume muchos
  recursos, el segundo plano **«is disabled by default»** (cap. 8, p. 198).
- **Cola de *render*.** En la página *Deliver* de Resolve se definen los ajustes de salida, se elige
  qué se va a exportar y se añade un trabajo a la cola: **«You can queue up as many different render
  jobs as you like, each with different formats, output options, and ranges of clips»**; al final se
  pulsa *Start Render* (cap. 187, p. 4185). En Premiere, la cola la lleva Adobe Media Encoder, que
  **«lets you queue multiple exports, use custom presets, and render files without interrupting your
  editing workflow»**, y Adobe lo recomienda **«for longer exports or when you need to create multiple
  delivery versions»** (ayuda de Premiere, «Export directly to Adobe Media Encoder»).
- ***Render* remoto.** Con varias estaciones Resolve en la misma red, un trabajo de la cola se puede
  mandar desde la estación en la que se trabaja a otra que esté libre, **«while you continue working
  on your main workstation»**. El manual pone tres condiciones: la versión Studio en las dos máquinas
  (con la gratuita no funciona); una biblioteca de proyectos a la que lleguen las dos (la misma
  biblioteca compartida en red, otra biblioteca Postgres conectada a una de ellas o un servidor de
  bibliotecas dedicado); y acceso de las dos al mismo material, en los mismos volúmenes o en volúmenes
  con el mismo nombre (cap. 187, p. 4215). Es un ejemplo claro de flujo integrado: sin acceso común al
  mismo material no hay *render* remoto.
- **Integraciones por *scripts*.** En la versión Studio, Resolve permite que terceros creen módulos
  de interfaz propios **«using scripting languages»**, y el usuario puede escribir su propio
  *Workflow Integration Plugin* **«(an Electron app), using Resolve Javascript's API, and Python or Lua
  scripts»** (cap. 201, p. 4418). Es la vía por la que un MAM se conecta al programa de edición
  (epígrafe 3).

Lo que la automatización no hace, como oficio: no mira el contenido. Una carpeta vigilada transcodifica
cualquier fichero que caiga en ella, sea el bueno o no; una cola de *render* exporta la secuencia que se
le dio aunque sea la versión equivocada; la emisión automatizada lanza la pieza que responde al nombre
aunque dentro esté otra. Por eso lo automatizado se revisa al final: se abre el fichero exportado, se
comprueba el nombre y la duración, y se mira el principio y el final antes de darlo por entregado.

## 2. Plantillas

### Qué es una plantilla

Una plantilla es un elemento o un ajuste preparado de antemano que se reutiliza para que cada pieza
salga igual sin rehacerlo (definición de oficio). En una sala de montaje hay tres clases: plantillas
de rótulo (el diseño del rótulo ya hecho, al que sólo se cambia el texto), plantillas de salida (los
ajustes de exportación guardados) y plantillas de nombre (reglas que componen el nombre de un clip o
de un fichero a partir de sus datos). Las tres persiguen lo mismo: que la imagen de marca, los formatos
de entrega y los nombres no dependan de quién esté en la cabina ese día.

### Plantillas de rótulo

Resolve trae generadores de rótulos con la composición ya resuelta. Tres ejemplos del manual (cap. 56,
p. 1215):

- Los rótulos inferiores (*Lower 3rd*) izquierdo, central y derecho: el central, por ejemplo,
  **«Automatically positions two lines of text at the bottom middle of title safe»**, cada línea con
  sus propios controles de estilo, posición, tamaño y giro. Es la forma del rótulo de identificación
  de un total: dos líneas, nombre y cargo, en la parte baja del cuadro.
- *Text+*: **«An advanced title generator»** con muchas más opciones de estilo y animación, pero en el
  que **«all title text shares a single style»**.
- *Fusion Titles*: **«A variety of pre-built title templates assembled in Fusion. DaVinci Resolve
  comes with a library of pre-assembled Fusion titles, but you can also create your own to appear in
  this category of the Effects browser.»** Es la plantilla propiamente dicha: la casa diseña su rótulo
  una vez y queda en la biblioteca de efectos de cada puesto.

En Premiere la plantilla de rótulo tiene formato propio: **«A Motion Graphics template is a file type
(.mogrt) that can be created in Adobe Premiere or Adobe After Effects.»** Se empaqueta con controles
sencillos pensados para ajustarse en Premiere y sirve para **«titles, lower thirds, and buttons»**; se
gestiona en el panel *Graphics Templates*, y puede llegar desde una carpeta local de plantillas, desde
las bibliotecas de Creative Cloud o desde Adobe Stock (ayuda de Premiere, «Overview of Motion Graphics
templates»). Al instalar un fichero .mogrt, la plantilla queda en la pestaña *My Templates* de ese
panel; se pueden instalar varias a la vez arrastrándolas a esa pestaña, y la que está en una biblioteca
de Creative Cloud **«is automatically available for use in Premiere. It doesn't need to be installed.»**
(«Install Motion Graphics templates»). Se usa arrastrándola a una pista de vídeo de la secuencia y
cambiando después su aspecto en la pestaña *Edit* del panel *Properties*; si pide fuentes que no están
instaladas, se pueden resolver las que faltan («Add Motion Graphic templates to a sequence»). Un gráfico hecho en
Premiere se exporta como plantilla con *Graphics and Titles > Export Motion Graphics template* o con el
botón derecho sobre el clip, pero **«This export feature is only available for graphics created in
Premiere, not for .mogrt files that were originally created in After Effects»**, y la opción no está
disponible si hay dos o más gráficos seleccionados («Export graphic as a Motion Graphics template»).
Hay además plantillas alimentadas por datos, para gráficos de barras, de líneas y otros, que admiten tres
tipos de dato (texto, color y números), fijados por su autor en After Effects y no modificables en
Premiere («Use data-driven Motion Graphics templates»). Todas esas páginas llevan fecha de 7-I-2026.

La otra vía, cuando el rótulo no lo compone el montador, es que lo componga el grafismo desde la
escaleta: el sistema de redacción manda el texto y el generador de caracteres lo pone sobre su propia
plantilla en el momento de la emisión. En iNews, según Manfredi (2010), cuyo ejemplo es el sistema
entonces instalado en Canal Sur (epígrafe 4), los rótulos que el periodista inserta en su texto **«irán
directamente a la emisión»**. Qué rótulos
se incrustan en la pieza y cuáles se lanzan en directo es decisión de la casa, que no consta publicada
(oficio: los que pueden cambiar a última hora, mejor en directo).

### Plantillas de salida: los *presets*

Un *preset* de exportación guarda todos los ajustes de salida (formato, códec, resolución, audio,
nombre y destino) con un nombre, y se aplica de un clic.

- En Resolve, se eligen los ajustes y se guarda con *Save as New Preset*; al pulsar un *preset*
  **«Every setting in the Render Settings pane updates to reflect the preset you selected»**. Se pueden
  actualizar y borrar, y también exportar e importar: **«Presets are saved in .xml files that can be
  easily sent to other users or workstations to ensure the exact same delivery methods are used between
  machines.»** Los *presets* nuevos aparecen además en el menú *Add to Render Queue Using* al pulsar
  con el botón derecho sobre una línea de tiempo (cap. 187, pp. 4193-4194).
- En Premiere, al enviar una secuencia a Media Encoder se aplica por defecto el *preset* **«H.264
  Match Source - Adaptive High Bitrate»**, salvo que la secuencia se haya abierto antes en el modo de
  exportación o en la exportación rápida, en cuyo caso **«the last-used export setting is applied
  instead»**; en Media Encoder se puede elegir otro o cambiar los ajustes (ayuda de Premiere, «Export
  directly to Adobe Media Encoder»). La consecuencia práctica: no conviene fiarse de lo que salga por
  defecto; se elige el *preset* de la casa cada vez.

Que el *preset* se pueda mandar a otros puestos es lo que convierte un ajuste personal en una norma
de la sala: todas las cabinas entregan el mismo formato porque cargan el mismo fichero. Los formatos
de entrega, en el tema 4; la exportación, en el tema 3.

### Plantillas de nombre: las variables de metadatos

Resolve permite escribir **«metadata variables»** en los campos de texto que las admiten, para que
el programa rellene el nombre con los datos del propio clip. Se escribe el signo de porcentaje (%) y
aparece la lista de variables disponibles. El ejemplo del manual: con las variables de escena, plano y
toma separadas por guiones bajos, un clip con escena «12», plano «A» y toma «3» se muestra como
«12_A_3». Si el campo de origen está vacío, en su lugar no aparece nada (cap. 15, p. 345).

Dónde se pueden usar, según el manual, entre otros sitios: en el nombre de los clips del *Media Pool*;
en otros campos del editor de metadatos; en el rótulo automático de las imágenes fijas de la galería;
en el texto sobreimpreso de la paleta *Data Burn*; y en el nombre de fichero de los ajustes de *render*
de la página *Deliver*, **«especially useful when you want to generate specific file names when
rendering individual source clips»** (p. 345). Hay además variables de fecha y hora (%date, %time) que
toman **«the actual date and time as of the output, rather than the date and time a clip was shot»**
(p. 346).

La aplicación al puesto es la nomenclatura (tema 15): si la casa fija una regla de nombres, una
variable la aplica sin errores de tecleo. Pero el nombre del vídeo que manda es el de la escaleta, y
ése no lo inventa la máquina: se copia de la escaleta (epígrafe 4).

## 3. MAM/PAM

### Qué son, y qué no hay

Las dos siglas nombran sistemas informáticos que guardan, catalogan y reparten el material
audiovisual de una casa. MAM es la gestión de activos de medios (*media asset management*); PAM, la
gestión de activos de producción (*production asset management*, como lo nombra la industria). Ninguna de las dos tiene una
definición de un organismo de normalización (UIT, EBU, SMPTE) que se haya podido encontrar; son nombres
de la industria, y cada fabricante los usa a su manera.

### Qué hace un MAM

Qué hace, en cinco funciones, como oficio (el cuadro sale de un temario de RTVE que no cita fuente):

| Función | Qué resuelve |
|---|---|
| Catálogo | Que cada material tenga sus datos descriptivos y se pueda buscar |
| Versiones | Que se sepa cuál es la buena y de dónde sale cada una |
| Baja resolución | Que se pueda ver y marcar el material sin mover el fichero grande |
| Ciclo de vida | Cuánto se guarda cada cosa y cuándo se borra o se archiva |
| Permisos | Quién puede ver, usar y borrar qué |

Del mismo origen, la diferencia con el DAM:

Y la distinción de vocabulario que conviene tener: la gestión de activos DIGITALES es el término
general —vale para fotos, documentos y audio—; la de activos de MEDIOS es la especializada en
audiovisual, con lo que eso añade: código de tiempo, subclips, versiones de montaje y derechos por
ventana de explotación.

### MAM y PAM: la diferencia es de oficio

La costumbre del sector reserva PAM para el sistema que gestiona el material mientras se produce
(brutos, *proxies*, secuencias en curso, varias personas trabajando a la vez sobre lo mismo) y MAM para
el que gestiona el material terminado y su archivo. Es una distinción de oficio: ninguna fuente
consultada la define, y hay fabricantes que llaman MAM a todo el sistema.

Un ejemplo de producto la ilustra. Avid presenta con página propia la capa de producción de su
plataforma MediaCentral, llamada *Production Management*, que describe así (página de producto, leída el
25-09-2026):

- Seguimiento del material de principio a fin: **«Take control of your valuable media assets, tracking
  them from ingest to archive and every step in-between. From single resolution to multi-resolution»**.
- Muchas personas sobre el mismo material: **«From journalists working on news packages to researchers
  putting together roughcuts to craft editors delivering the final edit, scale up to hundreds of users
  working together»**.
- Permisos: **«From no access to having administrative rights, Production Management delivers highly
  sophisticated permissions management»**.
- Servicios automáticos: **«integrated media services such as transcoding, archiving, restoring, and
  more to automate manual processes»**.
- Almacenamiento compartido: **«Production Management is driven by Avid NEXIS shared storage»**.
- Búsqueda por metadatos desde los programas de edición: **«system and user generated metadata for
  ultra-fast searching across connected clients such as Media Composer, Adobe Premiere Pro and the
  web-based MediaCentral | Cloud UX.»**

Es la descripción comercial de un producto, no una norma, y así se estudia: sirve para ver qué
funciones reúne un PAM en la práctica (ingesta, varias resoluciones, permisos, transcodificación,
archivo y restauración automáticos, almacenamiento compartido y búsqueda desde el editor).

### La copia de baja resolución

La pieza que hace posible el trabajo compartido sobre el MAM, como oficio (RTVE):

Cada material se transcodifica al entrar a una versión ligera, y es esa versión la
que viaja por la red ofimática, se ve en el navegador y se marca. El fichero grande no se mueve
hasta el conformado final. Sin esa pieza, una redacción de doscientas personas necesitaría una red
de vídeo en cada mesa.

La misma idea, vista desde el programa de edición, es la del *proxy* del tema 3: se monta sobre la
copia ligera y se vuelve al original para la salida. Adobe lo resume así: **«you first create proxy
files, edit these proxies, and then convert to full resolution media when you need the full resolution
files»** (ayuda de Premiere, «Ingest and proxy workflows in Premiere»).

### Los metadatos, el pegamento del sistema

Un MAM sólo encuentra lo que está bien descrito. La especificación de metadatos de la EBU, EBUCore
(EBU Tech 3293, v1.10, abril de 2020, p. 7), empieza por ahí: **«"If you can't find it, you don't have
it!" This should not happen in modern IT-based production environments. Metadata is the glue between
production operations particularly when moving towards Service Oriented Architecture and file-based
production.»** Y añade que documentar el material con EBUCore **«is a minimum requirement»**. La misma
especificación se define como **«the Dublin Core for media»** (p. 8): un juego básico de elementos
descriptivos y técnicos para describir contenidos audiovisuales, construido sobre el juego de metadatos
Dublin Core que usan bibliotecas y museos. Los campos concretos de EBUCore y la catalogación, en el tema
8.

### El MAM desde la sala de edición

Para el montador, el MAM puede no ser otra pantalla, sino algo que ve dentro de su programa (oficio),
cuando el MAM tiene módulo para ese programa. El manual de Resolve lo recoge: **«There are several Media Asset Management (MAM) systems that can now directly be
accessed through DaVinci Resolve using the Workflow Integration Plugins.»** Su ejemplo es el de
EditShare, cuyo módulo permite **«comment, search, and preview media in FLOW without leaving DaVinci
Resolve»** y también **«upload revisions, manage proxy media, and maintain full metadata support»**
(cap. 201, p. 4418). En Avid, como se ha visto, la búsqueda del PAM llega a Media Composer, a Premiere y
al navegador.

Qué hace el montador con el MAM, como oficio: busca el material por sus datos y no por el nombre del
fichero; lo trae a su proyecto; monta; y devuelve al sistema la pieza terminada con sus metadatos
completos, para que la encuentren emisión, las otras ediciones y el archivo. Una pieza exportada a un
disco local y no devuelta al sistema existe para la cabina y no para la casa.

### Dónde vive el material

Los dos almacenamientos de una redacción, como oficio (RTVE):

| | Almacenamiento de producción | Almacenamiento de archivo |
|---|---|---|
| Qué guarda | Lo que está en uso | Lo que se conserva |
| Cómo se accede | Inmediato, por red de bloques | Diferido: puede estar en cinta |
| Coste por terabyte | Alto | Bajo |
| Qué lo dimensiona | Cuánto material vivo hay a la vez | Cuánto hay que conservar y cuánto tiempo |

Y un aviso del mismo origen: la ingesta es donde el almacenamiento se llena. Un
sistema sin política de borrado y de archivo se para solo al cabo de unos meses, y la política hay
que escribirla antes, no cuando el disco está lleno.

## 4. Newsroom

### El sistema de redacción

*Newsroom* es la redacción, y en el oficio se llama así también a su sistema informático, el NRCS.
Qué es y qué contiene, como oficio (el pasaje sale de un temario de RTVE que no cita fuente):

Qué es: la herramienta donde se escribe, se ordena y se cronometra el informativo, y el punto
desde el que se manda a todo lo demás.

| Elemento | Qué es |
|---|---|
| ESCALETA | La lista ordenada de piezas, con su duración, su fuente y su estado |
| Guion de cada pieza | Texto para el apuntador, con sus marcas de entrada y salida |
| Referencias al material | Qué vídeo, qué rótulo y qué audio lleva cada pieza |
| CRONOMETRÍA | Duración prevista, duración real y desviación acumulada |
| Estados | Escrita, grabada, revisada, lista, emitida |
| Agenda y teletipos | Lo que entra de agencias y de la previsión |

Y la idea que ordena el punto: en un sistema de redacción, la ESCALETA es la base de datos y todo
lo demás cuelga de ella. El texto, el vídeo, los rótulos, el orden y los tiempos no son ficheros
sueltos: son campos de la misma escaleta, y eso es lo que permite que un cambio de última hora se
propague solo a la emisión, al apuntador y al grafismo.

Dos de las tres cosas que hacen útil ese sistema, del mismo origen:

1. Cronometra en TIEMPO REAL. La escaleta sabe cuánto dura lo escrito y cuánto queda de
   informativo, y avisa cuando no cabe. Sin eso, un informativo se sale o se queda corto en
   antena.
2. Es el ÚNICO sitio donde se cambia algo. Una pieza que se cae se cae en la escaleta, y el
   cambio llega solo a la emisión, al apuntador y al grafismo. Un sistema donde hay que cambiar
   las cosas en tres sitios pierde informativos.

La tercera es que habla con los demás equipos por un protocolo de comunicación, que es lo que permite
que la escaleta mande sobre los servidores, el grafismo y el apuntador. Uno de ellos, con
especificación publicada, es MOS.

### El protocolo MOS

La web del proyecto MOS lo define así: **«Media Object Server Communications Protocol (MOS): An
evolving protocol for communications between Newsroom Computer Systems (NCS) and Media Object Servers
(MOS) such as Video Servers, Audio Servers, Still Stores, and Character Generators.»** Es decir, un
protocolo, en evolución, para que el sistema de redacción hable con los servidores de objetos de medios:
servidores de vídeo, de audio, almacenes de imágenes fijas y generadores de caracteres. Su finalidad,
en la misma fuente: **«allows integration of diverse NCS and MOS equipment»**.

Lo que hay que saber de él (portada, «Current Versions» y FAQ de mosprotocol.com, leídas el
25-09-2026):

- **El problema que resuelve.** La FAQ lo plantea con una pregunta: **«How do I get my brand-X
  computer system to communicate with my brand-Y media server?»**. MOS es la respuesta común para que
  el sistema de redacción de un fabricante hable con el servidor de otro.
- **Qué es «un MOS».** **«A Media Object Server (MOS) is any device capable of storing Media Objects.»**
  Los objetos de medios son **«CGs (Character Generator Objects), Audio, Still Store, Video»**, y la
  lista puede crecer. Se da por supuesto, **«though not a requirement»**, que se guardan en un equipo no
  lineal.
- **El reparto de papeles.** En general (**«In General»**, dice la FAQ), **«the Newsroom Computer System is responsible for the creation,
  modification, and deletion of editorial information, including playlists»**; **«the Media Object
  Server is responsible for the creation, modification, and deletion of media objects and their
  associated meta-data»**. La redacción manda en el orden y en el texto; el servidor, en el material y
  sus datos.
- **Los tres tipos de mensajes.** *Descriptive Data for Media Objects*: el servidor **«"pushes"
  descriptive information and pointers to the NCS as objects are created, modified, or deleted»**, de
  modo que la redacción sabe qué hay en él y puede buscarlo. *Playlist Exchange*: la redacción construye
  y envía la lista de reproducción al servidor, lo que **«allows the NCS to control the sequence that
  media objects are played or presented by the MOS»**. *Status Exchange*: el servidor informa a la
  redacción del estado de cada clip o de todo el sistema, y la redacción informa al servidor del estado
  de los elementos de la lista o de los órdenes de emisión (*running orders*).
- **Cómo viaja.** Entre sus objetivos: **«Common implementation of the protocol will be over a TCP/IP
  network via socket communication»**; los mensajes **«will make use of a tagged text unicode format»**;
  y **«Each new version of the protocol will be a "super set" of the previous version»**, para que una
  máquina antigua siga hablando con una nueva con un vocabulario más reducido.
- **En qué va escrito cada mensaje.** La especificación (versiones 2.8.5 y 4.0, apartado «General
  Explanation of MOS message format and construction») concreta ese «tagged text»: **«The MOS Protocol
  is fundamentally a tagged text data stream»**, cuyos campos van delimitados **«using Extensible
  Markup Language (XML™) tags defined in the MOS Data Type Definition (DTD)»**; en las versiones 1.x el
  formato era propio. Los mensajes **«must be well formed XML, but are not required to be valid»**, y
  cada uno **«begins with the root tag ("mos")»**, seguido de los identificadores del servidor y de la
  redacción (**«"mosID" and "ncsID"»**) y del tipo de mensaje. La codificación es **«ISO 10646
  (Unicode) in UCS-2»**, con el byte de mayor peso primero (*big endian*). En la versión 2.8.5 la
  redacción escucha por defecto en el puerto TCP/IP 10540 (**«"Media Object Metadata" port»**) y el
  servidor en el 10541 (**«"Running Order" port»**); son números de ejemplo, porque desde la versión 2.5
  los puertos **«are vendor selectable but site specific»**, y las búsquedas de objetos
  (*mosReqObjList*) van aparte, por el 10542. La 4.0 pasa a *web sockets* y, según la especificación,
  conserva la lógica de los dos puertos: cada conexión lleva un canal, **«mom = MOS Lower (10540)»**,
  **«ro = MOS Upper (10541)»** y **«aux = MOS Obj Req (10542)»**.
- **Versiones vigentes.** La página de versiones actuales da tres: **«MOS Version 4.0 was published on
  June 7th, 2019»** (*Secure Web Sockets*); **«MOS Version 2.8.5 was published on September 7, 2017»**
  (*Socket*); y **«MOS Version 3.8.4 was published on February 11, 2011»** (*Web Services*).
- **Quién lo hace.** Lo desarrollan en colaboración **«equipment vendors, software vendors and end
  users»**. La primera reunión fue **«in Orlando, Florida during the late summer of 1998 at the AP's
  ENPS developer's conference»**, y **«As of 2021 more than 150 companies participate»**.
- **No es una norma oficial.** La FAQ dice que el protocolo **«will be presented to appropriate
  standards bodies at a later date»**, y que su desarrollo no se frenará a la espera de **«the official
  "blessing" of a standards body»**. No es, por tanto, una norma de la SMPTE, de la EBU ni de otro
  organismo de normalización: es un protocolo de la industria con especificación pública.

Una salvedad de siglas: la especificación MOS llama al sistema de redacción NCS; los fabricantes y el
oficio lo llaman también NRCS (por ejemplo, Avid, más abajo). Son lo mismo.

Qué supone MOS para el montador, como oficio: la pieza que entrega queda enlazada a su línea de la
escaleta por un objeto del servidor, y la redacción ve su estado (si ya está, si está lista) sin
preguntar a la cabina. Por eso el nombre y el sitio de entrega no se improvisan: si la pieza no llega
al servidor que la escaleta espera, para la redacción no existe.

### Un sistema de redacción de mercado

Como ejemplo de producto, Avid presenta *MediaCentral | Newsroom Management*, también llamado iNEWS,
como **«the newsroom computer system (NRCS) you need to break stories on-air faster»**. Dos frases de
su página de producto (leída el 25-09-2026) describen lo que se espera hoy de un NRCS: **«Build
rundowns, adjust timing, go live and make real-time changes—even on-air»** (construir escaletas,
ajustar tiempos y cambiar en directo, incluso en antena) y **«Streamline your control room operations
by integrating your rundown with studio automation, teleprompters, graphics, and video playout
servers»** (la escaleta integrada con la automatización del estudio, el apuntador, el grafismo y los
servidores de emisión). Es publicidad de un fabricante, no una norma.

### El sistema de redacción en Canal Sur

La escaleta, en el Libro de estilo:

**«La escaleta es el documento básico en el que se plasma y ordena el contenido de un programa.
Expresa el hecho noticioso concreto, formato, número o clave por el que se identiﬁca cada uno, tiempo
asignado, tiempo real, autor, procedencia (elaborado in situ o de otro origen), identiﬁcación del
presentador y cualquier otra acotación técnica que sea precisa (vídeo o colas, gráﬁco, línea de
lanzadera, plano y cámara del presentador, movimientos de cámara, elementos visibles de plató...).»**
(6.1, p. 88)

**«La mayor parte de estos elementos se reﬂejan en los partes de emisión, que contemplan además las
vías de sonido, coleo del vídeo, rótulos, observaciones y el pie del texto de la noticia.»** (p. 88)

La escaleta cambia: **«Cualquier cambio del contenido de la escaleta debe comunicarse, desde el origen de
la decisión, inmediata y simultáneamente, a todas las personas y departamentos afectados.»** (6.1, p. 88).
Lo que no cambia es el nombre: **«Son inadmisibles los cambios en la identiﬁcación de un vídeo [...] El
nombre de una noticia en escaleta debe respetarse por obligación.»** La única excepción: un vídeo
terminado antes de hacerse la escaleta, cuyo nombre traslada a ella el equipo de edición (6.1.1, p. 88). El redactor fija en ella **«sus textos deﬁnitivos (incluidos los rótulos con su orden y
ubicación precisa)»** (6.1.2, p. 89).

Lo que el redactor deja en la escaleta es de todo el equipo: **«El redactor ha de ﬁjar siempre en
escaleta sus textos deﬁnitivos (incluidos los rótulos con su orden y ubicación precisa) y los pasos de
locutor que le hayan sido asignados. Así quedan disponibles para el resto del equipo del programa y para
posteriores ediciones de informativos.»** (6.1.2, p. 89). El Libro de estilo no describe un formato de
guion concreto ni nombra el programa informático que usa CSRTV.

Qué sistema consta:

Un capítulo de Antonio Manfredi (2010), en una obra colectiva de periodismo publicada en Sevilla,
describe el guion tal como se trabaja en los sistemas de redacción digitales. Su ejemplo es Avid, cuyos equipos, según el autor, estaban instalados **«en
todos los Servicios Informativos de RTVE y, en el caso de Andalucía, en Canal Sur»** (p. 138); es un dato
de 2010, y no consta en documento publicado que siga siendo así hoy.

- El periodista empieza su trabajo en iNews, de Avid, **«un sistema de escritura de noticias»** con acceso a las agencias, a los textos de la
  redacción y a **«las escaletas de todos los informativos»**. El periodista recibe un mensaje cuando se le
  adjudica una noticia y **«conoce la duración exigida y el lugar de emisión»**; empieza entonces a
  **«componer el texto de la noticia e insertar ya los rótulos de la información (totales y localizadores
  temporales o espaciales) que no tienen ya que ser compuestos por ningún otro profesional e irán
  directamente a la emisión»** (pp. 139-140).
- iNews Instinct, que Avid lanzó en 2005 para que el periodista monte piezas con texto y vídeo sin una
  aplicación profesional de edición, tiene en su espacio de trabajo **«un sencillo modo de edición para
  video y el guión»**, y el usuario puede **«ajustar el audio y el minutado»** (p. 139).

Ningún documento publicado leído dice qué sistema de redacción, qué MAM ni qué servidores de emisión
usa CSRTV hoy.

### La edición dentro de la redacción

Cómo se reparte la edición en una redacción integrada, como oficio (RTVE):

| Nivel | Quién lo usa | Sobre qué material |
|---|---|---|
| Edición ligera, en el propio puesto | El redactor | La copia de baja resolución |
| Edición completa, en sala | El montador | El material de alta resolución |

Y el conformado es la operación que une los dos: la lista de decisiones tomada sobre la copia
ligera se aplica al material grande. Es automático, y es donde aparecen los fallos si los códigos
de tiempo no coinciden.

Qué distingue la edición de informativos de la postproducción, del mismo origen:

| | Edición de informativos | Postproducción |
|---|---|---|
| Tiempo | Minutos | Días |
| Quién edita | El redactor, a menudo | Un montador |
| Herramienta | Sencilla, integrada en la redacción | Completa y especializada |
| Resultado | Una pieza que se emite hoy | Un programa |
| Prioridad | Que esté a tiempo | Que esté bien |

Y las dos consecuencias técnicas de esa columna izquierda:

1. La edición tiene que estar DONDE está el redactor. De ahí los puestos de edición ligera en la
   propia redacción, y de ahí la copia de trabajo: no se puede pedir a cincuenta puestos que
   muevan material de alta tasa.
2. El material se edita MIENTRAS SE INGESTA. Poder empezar a montar una señal que todavía se
   está grabando —edición sobre material creciente— es la prestación que decide si un sistema sirve
   para informativos. Sin ella, un directo de una hora no se puede montar hasta que acaba.

La edición sobre material que todavía se graba, con sus límites, se ve en el tema 14; el conformado,
en el tema 3.

Y la observación de arquitectura con la que cierra ese temario de RTVE, también de oficio:

Y la observación de arquitectura que cierra el punto: el sistema de redacción es la pieza más
integrada de una casa y por eso la más difícil de cambiar. Habla con el almacenamiento, con la
edición, con el grafismo, con la emisión y con el archivo, y sustituirlo obliga a rehacer todas
esas conversaciones. Por eso se elige por sus INTERFACES tanto como por sus prestaciones.

## 5. Flujos de producción integrados

### Qué es un flujo integrado

Un flujo de producción es integrado cuando todas sus etapas trabajan sobre el mismo material y los
mismos datos, sin copias sueltas ni pasos a mano entre una y otra (definición de oficio). El esquema,
como oficio (el pasaje sale de un temario de RTVE que no cita fuente):

| Etapa | Qué hace | Quién trabaja ahí |
|---|---|---|
| Ingesta | Meter el material en el sistema: grabar señales de entrada y volcar tarjetas | Operadores de ingesta |
| Gestión | Catalogar, buscar y controlar el material y sus versiones | Documentación y todos los demás |
| Edición | Montar las piezas | Redactores y montadores |
| Emisión | Poner la pieza en antena en el momento previsto | Control de emisión |

Y el archivo atraviesa las cuatro, no es una quinta: lo que se conserva se decide en la primera y
se ejecuta después.

La regla que ordena el punto: cada etapa mete el material en un sitio y las demás lo encuentran
por sus DATOS DESCRIPTIVOS, no por su nombre de fichero. Ésa es toda la diferencia entre un
sistema de redacción y una carpeta compartida.

Los cuatro epígrafes anteriores son las piezas de ese flujo: el MAM o el PAM guarda el material y sus
datos (epígrafe 3); el sistema de redacción manda en el orden, el texto y los tiempos (epígrafe 4); el
protocolo MOS lleva los datos entre la redacción y los servidores (epígrafe 4); las plantillas hacen
que cada puesto entregue lo mismo (epígrafe 2); y la automatización ejecuta lo repetido (epígrafe 1).

### La entrada: vías de ingesta

Cómo entra el material, como oficio (RTVE):

| Vía | Qué llega | Qué exige |
|---|---|---|
| De TARJETA o de cámara | Ficheros ya grabados | Copia y verificación: es transferencia, no captura |
| En TIEMPO REAL, desde una señal | Una señal en directo que hay que grabar | Un canal de ingesta ocupado durante todo el acto |
| De AGENCIA o intercambio | Material de fuera, con sus metadatos | Normalización de formato y de metadatos |
| Desde el ARCHIVO | Material antiguo | Restauración desde el soporte de conservación |

Las reglas de la ingesta, del mismo origen:

1. Se ingesta con METADATOS o no se ingesta. Un fichero sin título, sin fecha, sin origen y sin
   derechos es un fichero perdido en cuanto haya diez mil. La ingesta es el único momento en que
   esos datos se pueden capturar barato.
2. Se genera la COPIA LIGERA al ingestar. Montar sobre la copia y conformar al final es lo que
   permite que veinte redactores trabajen a la vez sin saturar el almacenamiento.
3. La ingesta en tiempo real ocupa un recurso entero. Un canal de ingesta grabando un pleno de tres
   horas no está disponible para otra cosa, y por eso el número de canales es una decisión de
   dimensionado, no un detalle.

Y la razón por la que la ingesta en directo es la crítica: es la única que no se puede
repetir. Si falla la grabación de una señal de agencia mientras ocurre, no hay segunda
oportunidad, y por eso se graba por partida doble en dos sistemas independientes.

Los tres datos que se capturan en la ingesta y que deciden si el material se encontrará después:
quién lo trae, de qué es y qué derechos tiene. Un material sin esos tres datos está dentro del
sistema y está perdido.

La digitalización desde cinta, la copia verificada con sumas de comprobación, los metadatos y el
archivo, en el tema 8.

### Las redes que sostienen el flujo

Como oficio (RTVE):

| Red | Qué lleva | Por qué va separada |
|---|---|---|
| De señal | Vídeo y audio en tiempo real | Caudal enorme y sensible al retardo |
| De producción | Ficheros, baja resolución, control del sistema | Caudal alto a ráfagas |
| Ofimática | Correo, navegación, gestión | Es la que está expuesta a internet |

Y la razón de la separación, dicha sin rodeos: la red ofimática es la que recibe el correo con
el adjunto malicioso. Si la producción cuelga de ella, un incidente de seguridad puede parar la
emisión.

### Cuando algo falla

Un flujo integrado tiene una debilidad: si falla una pieza central, se paran todas las que dependen de
ella. Cómo se sigue emitiendo, como oficio (RTVE):

| Qué falla | Cómo se sigue emitiendo |
|---|---|
| El sistema de redacción | Escaleta en papel y operación manual: se pierde automatismo, no la emisión |
| El servidor de emisión | Un segundo servidor con las mismas piezas, replicadas |
| El almacenamiento | Redundancia de la propia cabina y copia de lo del día |
| La red | Doble camino |
| El estudio entero | Un estudio alternativo con escaleta cargada |
| La energía | Sistema ininterrumpido y grupo |

Y las dos reglas que hay que llevar aprendidas:

1. La redundancia se prueba. Un servidor de reserva que nadie ha usado nunca no es una reserva:
   es una suposición.
2. La degradación tiene que ser ORDENADA y ENSAYADA. Que el equipo sepa qué hacer cuando la
   escaleta no responde es más valioso que un equipo de reserva que nadie sabe conmutar.

Para la sala de montaje eso se traduce en una costumbre (oficio): tener localizado dónde queda cada
pieza terminada y cómo se entrega por otra vía si la habitual no responde, y avisar a la redacción y a
emisión en cuanto una entrega falla, sin esperar a que la echen en falta.

### El montador en el flujo integrado

Dónde entra el Operador/a Montador/a en cada etapa, leyendo las tareas de su ficha del convenio sobre
el esquema anterior (la lectura es de oficio; las tareas, literales, son las de la ficha 5212206, p.
190):

| Etapa | Tarea de la ficha | Qué hace en un flujo integrado (oficio) |
|---|---|---|
| Ingesta | **«Recibir y enviar enlaces.»** **«Configurar sistemas de edición y preparar los materiales a utilizar.»** | Graba lo que entra por señal, trae el material del sistema a su proyecto y comprueba que llega con sus datos |
| Edición | **«Editar y postproducir material audiovisual con criterios de narrativa audiovisual.»** | Monta sobre la copia ligera o el original, con las plantillas de rótulo de la casa |
| Control | **«Realizar el control técnico de calidad y corregir video y audio para su emisión y/o venta.»** | Revisa la pieza exportada: nombre, duración, principio y final, audio |
| Emisión | **«Etiquetar, grabar e introducir en base de datos, la información para la emisión automatizada de programas y bloques publicitarios.»** | Entrega al servidor con el nombre de la escaleta y deja sus datos donde la automatización los lee |
| Archivo | **«Compactar para el archivo de material audiovisual.»** | Devuelve al sistema la pieza terminada con sus metadatos y lo seleccionado para conservar |

La tabla elige las tareas que tocan el flujo; la ficha tiene otras dos: **«Grabar, emitir y reproducir
videos para programas en todo tipo de eventos y producciones con selección alternativa a la
realización»**, la más cercana a la emisión, y **«Repicar cintas orientadas a la producción, emisión y
comercialización»**. Y la ficha advierte que su definición **«no constituye una lista cerrada de funciones»**:
el trabajador debe realizar además **«todas aquellas tareas que, de acuerdo a su cualificación profesional, le
sean encomendadas por su inmediato superior»**. El convenio no define «compactar» ni dice qué base de datos ni qué sistema de automatización usa la
casa; la columna de la derecha es costumbre de oficio, no descripción de Canal Sur.

## Aplicación práctica

### Una pieza de la ingesta a la emisión

Supuesto: una noticia de mediodía con imágenes de cámara propia, una declaración que llega por señal de
un centro territorial y un rótulo de identificación. Los pasos, como oficio, con la fuente de cada regla
entre paréntesis cuando la hay:

1. La pieza nace en la escaleta con su nombre, su duración asignada y su redactor (Libro de estilo,
   6.1). Ese nombre es el que llevará todo lo demás, y no se cambia (6.1.1).
2. La tarjeta de la cámara se copia con verificación, y la señal del centro territorial se graba en
   ingesta mientras llega: es la vía que no se puede repetir. Las dos entradas se registran con quién
   las trae, de qué son y qué derechos tienen (epígrafe 5).
3. Al entrar, el sistema genera la copia ligera; si la casa usa carpetas vigiladas y el generador está
   en marcha, la generación es automática (epígrafe 1).
4. En la cabina, el montador busca el material en el MAM o el PAM por sus datos y lo trae a su
   proyecto (epígrafe 3). Monta con la escaleta de planos (Libro de estilo, 6.3: **«La edición debe acometerse
   siempre con una escaleta de planos»**) y con el texto que el redactor dejó en la escaleta (6.1.2).
5. El rótulo de identificación del total va con la plantilla de la casa, o lo lanza el grafismo desde
   la escaleta si así se trabaja (epígrafe 2).
6. Exporta con el *preset* de la casa, no con el que salga por defecto, y nombra el fichero como la
   escaleta (epígrafe 2).
7. Revisa el fichero exportado: nombre, duración, principio, final y audio (tarea de control técnico de
   calidad de su ficha).
8. Lo entrega al servidor que la escaleta espera y deja sus datos para la emisión automatizada (tarea
   de la ficha). Con MOS, la redacción ve el estado de la pieza en su escaleta sin preguntar (epígrafe
   4).
9. Tras la emisión, la pieza vuelve al sistema con sus metadatos para otras ediciones y para el
   archivo (epígrafe 3).

### Un cambio de escaleta con el flujo integrado

Supuesto: a veinte minutos del informativo, la edición decide recortar la pieza de 1:30 a 1:00 y
moverla de bloque.

- El cambio se hace en la escaleta y se comunica desde su origen a todos los afectados (Libro de
  estilo, 6.1). El orden y la duración nuevos llegan solos a la emisión, al apuntador y al grafismo si
  el sistema está integrado (epígrafe 4).
- El nombre del vídeo no cambia aunque cambie su sitio (6.1.1).
- En la cabina se duplica la secuencia antes de recortar, se recorta, se exporta con el mismo *preset*
  y se revisa la duración real, porque la escaleta cronometra con ella (oficio; el versionado, en el
  tema 14).
- La nueva versión sustituye a la anterior en el servidor con el mismo nombre, y se avisa a emisión de
  que la pieza ha cambiado (oficio).

## Lo que este tema no da, y dónde está

- Qué sistema de redacción, qué MAM o PAM, qué servidores de emisión y qué sistema de automatización
  usa CSRTV hoy: no consta en documento publicado leído. El dato de Avid en Canal Sur es de 2010.
- Qué campos lleva la base de datos de la emisión automatizada que cita la ficha del convenio, y qué
  significa «compactar»: el convenio no lo dice.
- Una definición normalizada de MAM y PAM: no se ha encontrado; la distinción entre ellos es costumbre
  de oficio.
- De las especificaciones MOS se da sólo el formato general de los mensajes, su codificación y los
  puertos o canales; el catálogo de mensajes uno a uno, sus etiquetas y los esquemas de metadatos, no.
- Las carpetas vigiladas de Adobe Media Encoder: su documentación no se pudo leer y el tema no dice
  nada de ellas. De las plantillas .mogrt se da lo que dice la ayuda de Premiere; cómo se diseñan en
  After Effects, no.
- La página de Avid sobre su módulo de gestión de material terminado (*Asset Management*): no se pudo
  leer, y por eso el tema no la cita.
- Buena parte del tema va como oficio: los pasajes tomados de temarios de RTVE (etapas del flujo,
  funciones del MAM, copia ligera, almacenamientos, redes, sistema de redacción, edición de
  informativos, degradación) no citan fuente y así se presentan.
- Otras materias: sistemas de edición, *proxies*, conformado y exportación, tema 3; formatos de
  entrega, tema 4; montaje de noticias, tema 5; grafismo y rótulos en postproducción, tema 7; ingesta,
  verificación, metadatos y archivo, tema 8; coordinación con redacción, realización, grafismo y
  emisión, tema 9; versiones para plataformas, tema 12; edición durante la ingesta, urgencia y
  versionado, tema 14; nomenclatura y trazabilidad, tema 15.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| X Convenio Colectivo de la RTVA y sociedades filiales (BOJA núm. 240, de 10-XII-2014), anexo III, fichas 5212206 (p. 190) y 5212204 (p. 127) | Tareas del Operador/a Montador/a (emisión automatizada, enlaces, control de calidad, compactar para archivo); tarea del encargado sobre la emisión automatizada | 25-09-2026 |
| Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía, RTVA, coord. José María Allas Llorente y Luis Carlos Díaz Salgado, 1.ª ed., marzo 2004, ISBN 84-609-0453-9: 6.1, 6.1.1, 6.1.2 y 6.3 (p. 91) | Escaleta, partes de emisión, cambios, nombre del vídeo, textos del redactor; escaleta de planos para editar | 24-09-2026 (pasajes copiados del tema 7 del específico de Redactor/a); 6.3, 25-09-2026 |
| Antonio Manfredi Díaz, «Escribir para televisión. La imagen manda», en R. Reig García (ed.), *La dinámica periodística: perspectiva, contexto, métodos y técnicas*, Sevilla, Asociación Universitaria Comunicación y Cultura, 2010, pp. 129-145, ISBN 9788493760007 | iNews de Avid en Canal Sur (2010); rótulos que van directamente a la emisión | 24-09-2026 (pasaje copiado del tema 7 del específico de Redactor/a) |
| MOS Project, mosprotocol.com: portada, «Current Versions» y «MOS FAQ» | Definición de MOS, objetos de medios, reparto NCS/MOS, tres tipos de mensajes, objetivos, versiones vigentes, origen y carácter no oficial | 25-09-2026 |
| *Media Object Server (MOS) Protocol* v2.8.5 (rev. 558, 7-IX-2017; PDF pp. 11, 13, 14, 35 y 58) y v4.0 (rev. 560, 7-VI-2019; PDF pp. 9 y 18), mosprotocol.com | Formato XML de los mensajes, etiqueta raíz, codificación UCS-2, puertos 10540/10541/10542 (por defecto, seleccionables) y canales de la 4.0 | 25-09-2026 |
| EBU Tech 3293, *EBUCore Metadata Set*, v1.10, abril de 2020, § 1 (p. 7) y § 2.1 (p. 8) | Los metadatos como «glue»; requisito mínimo; «Dublin Core for media» | 25-09-2026 |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual*: cap. 8 (pp. 198, 215-217), cap. 15 (pp. 345-346), cap. 56 (p. 1215), cap. 187 (pp. 4185, 4193-4194, 4215), cap. 201 (p. 4418) | Tareas en segundo plano, carpetas vigiladas del Proxy Generator, variables de metadatos, plantillas de rótulos, cola de *render*, *presets* en .xml, *render* remoto, integraciones y acceso a MAM | 25-09-2026 |
| Adobe, ayuda de Premiere: «Export directly to Adobe Media Encoder» e «Ingest and proxy workflows in Premiere» | Cola de Media Encoder y *preset* por defecto; flujo de *proxies* | 25-09-2026 |
| Adobe, ayuda de Premiere (helpx.adobe.com, páginas de 7-I-2026): «Overview of Motion Graphics templates», «Install Motion Graphics templates», «Add Motion Graphic templates to a sequence», «Export graphic as a Motion Graphics template», «Use data-driven Motion Graphics templates» | Plantillas .mogrt: qué son, procedencia, instalación, uso, exportación y su salvedad, plantillas con datos | 25-09-2026 |
| Avid, páginas de producto de *MediaCentral \| Newsroom Management* y *MediaCentral \| Production Management* (avid.com) | Ejemplo de NRCS y de capa de gestión de producción | 25-09-2026 |

Va como oficio, y así se declara: los pasajes tomados de los temarios de RTVE de Ingeniería Técnica
(sistemas de redacción digital) y de Ingeniería Superior (sistemas de redacción e informativos) de
Telecomunicación, que no citan fuente; las definiciones de automatización, plantilla y flujo integrado;
la distinción entre MAM y PAM; lo que la emisión automatizada y MOS piden a la sala; los límites de la
automatización; la lectura de las tareas de la ficha sobre el flujo; y los pasos de la aplicación
práctica que no llevan fuente entre paréntesis.
