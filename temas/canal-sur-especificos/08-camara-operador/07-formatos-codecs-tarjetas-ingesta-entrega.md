# Tema 7 del específico de Cámara Operador · Formatos de grabación, códecs, tarjetas, metadatos, ingesta, copia de seguridad y entrega de material

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Cámara Operador · punto 7 |
| **Sirve para** | Puesto 2.8, Cámara Operador (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Sin norma jurídica. Lo propio de la casa: *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, 1.ª ed., marzo de 2004). Normas y recomendaciones técnicas: UIT-R BT.709-6 y BT.2020-2 (formato de imagen). Documentación de fabricante: Sony, *PXW-Z200/HXR-NX800 Help Guide* (5-060-574-13(1), 2024), *PXW-X400 Operating Instructions* (2015) y guías de formatos de otras cámaras Sony; Avid, *Avid DNxHD Technology* (2012); Panasonic, *AVC-Intra Frequently Asked Questions*. Organismos de conservación y seguridad: Library of Congress (fichas de MXF y de ProRes 422), Digital Preservation Coalition (*Digital Preservation Handbook*), INCIBE, SD Association (página «Speed Class» y libro blanco de la clase de vídeo, 2016). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | Las ediciones vigentes el 24/09/2026 de cada documento citado; el Libro de estilo en su única edición publicada |
| **Extensión** | 12.000 palabras aproximadamente |

<!-- /portada -->

Siglas que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Sector de Radiocomunicaciones de la
Unión Internacional de Telecomunicaciones (**UIT-R**); Unión Europea de Radiodifusión (**EBU**,
*European Broadcasting Union*); Sociedad de Ingenieros de Cine y Televisión (**SMPTE**, *Society of
Motion Picture and Television Engineers*); captación electrónica de noticias (**ENG**, *electronic
news gathering*); alta definición (**HD**) y ultra alta definición (**UHD**); cuadros por segundo
(**fps**); rojo, verde y azul (**RGB**); progresivo (**p**) y entrelazado (**i**); megabits por segundo (**Mb/s**), gigabyte
(**GB**) y terabyte (**TB**); grupo de imágenes (**GOP**, *group of pictures*; el «GOP largo» es el
*Long GOP*); codificación avanzada de vídeo (**AVC**, *advanced video coding*, la norma H.264) y
codificación de vídeo de alta eficiencia (**HEVC**, *high efficiency video coding*, la norma
H.265); formato de intercambio de material (**MXF**, *material exchange format*), con sus patrones
operacionales **OP1a** y **OP-Atom**; contenedores de Apple (**MOV**, QuickTime), de la familia MPEG
(**MP4**) y de Microsoft (**AVI**); formato avanzado de autoría (**AAF**, *advanced authoring
format*), lista de decisiones de edición (**EDL**, *edit decision list*) y lenguaje de marcado
extensible (**XML**); modulación por impulsos codificados (**PCM**, *pulse-code modulation*), y en su forma
lineal (**LPCM**, *linear pulse-code modulation*); tasa de bits variable (**VBR**, *variable bit rate*) y
constante (**CBR**, *constant bit rate*); relación señal/ruido de pico (**PSNR**, *peak
signal-to-noise ratio*); código de tiempo (**TC**, *timecode*), longitudinal (**LTC**) y en el intervalo
vertical (**VITC**); salto de cuadro (**DF**, *drop frame*) y sin salto (**NDF**, *non-drop
frame*); tarjeta de memoria digital segura (**SD**, *secure digital*) y su variante de capacidad extendida
(**SDXC**, *secure digital extended capacity*); tarjeta **CFexpress** y su clasificación **VPG** (se nombra como la imprime el manual de la
cámara; su fuente no se ha leído, y no se desarrolla);
bus serie universal (**USB**); clase de velocidad de alta velocidad (**UHS**, *ultra high speed*) y de
vídeo (**V**); sistema de ficheros **exFAT**; conjunto redundante de discos independientes
(**RAID**); cinta lineal abierta (**LTO**, *linear tape open*); protocolo de transferencia de
ficheros (**FTP**) y su variante cifrada en modo explícito (**FTPES**); resumen criptográfico
**MD5** y **SHA-256**; Instituto Nacional de Ciberseguridad (**INCIBE**).

Los nombres de formato y los rótulos de menú se escriben como los imprime el fabricante (**XAVC
HS**, **DVC Pro**, ***[Simul Rec]***, ***[Clip Flag OK]***…): son marcas o rótulos de la máquina, no siglas que se
desarrollen. Lo mismo vale para las referencias de modelo (**PXW-Z200**, **ILCE-1**) y los
sufijos de las variantes de ProRes (**LT**, **HQ**, **XQ**). También los rótulos de perfil y nivel de
MPEG-2 que imprime el manual de la PXW-X400 (**422P@HL**, **MP@HL**): su desarrollo no se ha leído en
fuente y no se da.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.8, punto 7):
>
> Formatos de grabación, códecs, tarjetas, metadatos, ingesta, copia de seguridad y entrega de
> material.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué diferencia hay entre códec y contenedor, y si MXF es una cosa o la
otra; qué resolución tiene el HD y el UHD de televisión y quién la fija; qué significa 4:2:2 y 10
bits; qué diferencia hay entre compresión intracuadro y de GOP largo y cuál conviene para editar;
qué códec usan XAVC S, XAVC HS y XAVC S-I; qué son ProRes, DNxHD (y su norma SMPTE, la VC-3) y
AVC-Intra; qué es el MPEG HD 422; qué es un *proxy* y por qué lleva código de tiempo; cuánto material cabe en una
tarjeta a una tasa dada; qué indican las clases de velocidad de una tarjeta SD y cuántos MB/s garantiza cada una; qué pasa si se saca
una tarjeta con el piloto de acceso encendido; qué diferencia hay entre formateo completo y rápido,
y dónde se formatea una tarjeta; qué son la grabación en relevo y la simultánea; qué modos de código
de tiempo hay y qué son los bits de usuario; qué metadatos pone el cámara (nombre de clip, marcas,
banderas); qué es la ingesta y qué formas tiene; qué es una suma de verificación y para qué sirve;
qué es la regla 3-2-1; si un RAID es una copia de seguridad; por qué FTP no es seguro para enviar
material; qué decía el Libro de estilo de Canal Sur sobre el código de tiempo y las barras. En la
prueba práctica: elegir formato y tarjeta para un encargo, preparar las tarjetas, poner el código
de tiempo, marcar los clips buenos, hacer una copia verificada, enviar un *proxy* desde el lugar y
entregar el material con sus avisos.

<!-- indice -->

## Índice

- [Formatos de grabación](#formatos-de-grabación)
  - [De la cinta al fichero](#de-la-cinta-al-fichero)
  - [Esencia, códec, contenedor, metadatos y proyecto](#esencia-códec-contenedor-metadatos-y-proyecto)
  - [Qué define un formato de grabación](#qué-define-un-formato-de-grabación)
  - [Cómo se lee el nombre de un formato](#cómo-se-lee-el-nombre-de-un-formato)
  - [Los contenedores](#los-contenedores)
  - [Los formatos de proyecto](#los-formatos-de-proyecto)
  - [El *proxy*](#el-proxy)
  - [La tasa y la capacidad](#la-tasa-y-la-capacidad)
- [Códecs](#códecs)
  - [Qué es un códec y qué se pierde](#qué-es-un-códec-y-qué-se-pierde)
  - [Intracuadro y GOP largo](#intracuadro-y-gop-largo)
  - [H.264 y H.265](#h264-y-h265)
  - [XAVC (Sony)](#xavc-sony)
  - [Apple ProRes](#apple-prores)
  - [Avid DNxHD (SMPTE VC-3)](#avid-dnxhd-smpte-vc-3)
  - [AVC-Intra (Panasonic)](#avc-intra-panasonic)
  - [Cuadro resumen](#cuadro-resumen)
- [Tarjetas](#tarjetas)
  - [Los soportes de estado sólido](#los-soportes-de-estado-sólido)
  - [Las clases de velocidad](#las-clases-de-velocidad)
  - [Dos ranuras: relevo y grabación simultánea](#dos-ranuras-relevo-y-grabación-simultánea)
  - [Sacar la tarjeta](#sacar-la-tarjeta)
  - [Formatear](#formatear)
  - [Proteger y cuidar la tarjeta](#proteger-y-cuidar-la-tarjeta)
  - [Los avisos de la tarjeta](#los-avisos-de-la-tarjeta)
- [Metadatos](#metadatos)
  - [Qué son y quién los pone](#qué-son-y-quién-los-pone)
  - [El clip y su nombre](#el-clip-y-su-nombre)
  - [El código de tiempo](#el-código-de-tiempo)
  - [Los bits de usuario](#los-bits-de-usuario)
  - [La aritmética del código de tiempo](#la-aritmética-del-código-de-tiempo)
  - [Sincronizar el código de dos equipos](#sincronizar-el-código-de-dos-equipos)
  - [Marcas y banderas](#marcas-y-banderas)
  - [Los metadatos dentro del fichero](#los-metadatos-dentro-del-fichero)
- [Ingesta](#ingesta)
  - [Qué es la ingesta](#qué-es-la-ingesta)
  - [La ingesta de una tarjeta, paso a paso](#la-ingesta-de-una-tarjeta-paso-a-paso)
  - [La ingesta desde el lugar](#la-ingesta-desde-el-lugar)
- [Copia de seguridad](#copia-de-seguridad)
  - [Por qué](#por-qué)
  - [La primera copia: en la cámara](#la-primera-copia-en-la-cámara)
  - [La copia comprobada: suma de verificación](#la-copia-comprobada-suma-de-verificación)
  - [La regla 3-2-1](#la-regla-3-2-1)
  - [Lo que no es una copia de seguridad: el RAID](#lo-que-no-es-una-copia-de-seguridad-el-raid)
  - [El archivo a largo plazo: la LTO](#el-archivo-a-largo-plazo-la-lto)
- [Entrega de material](#entrega-de-material)
  - [Lo que recomendaba el Libro de estilo](#lo-que-recomendaba-el-libro-de-estilo)
  - [Qué se entrega](#qué-se-entrega)
  - [El envío por red](#el-envío-por-red)
  - [Un supuesto práctico](#un-supuesto-práctico)
- [Documentos técnicos que el tema cita](#documentos-técnicos-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Formatos de grabación

### De la cinta al fichero

Durante décadas la cámara de informativos grabó en cinta, y el Libro de estilo de Canal Sur (2004)
está escrito para ella: habla de barras al principio de cada cinta, de una noticia por cinta y del
código de tiempo puesto a cero «al principio de la cinta» (5.3.3, pp. 81-82; véase «Entrega de
material»). Esas reglas son históricas: hoy la cámara graba ficheros en tarjetas de memoria.

Entre la cinta y la tarjeta hubo un paso intermedio, el disco óptico profesional de Sony
(XDCAM), con dos ventajas sobre la cinta que son las mismas que tiene hoy la tarjeta (oficio):

1. Acceso no lineal: se salta a cualquier punto sin rebobinar.
2. Ficheros, no señal: lo que hay en el soporte ya es un fichero con sus metadatos, así que la
   ingesta es una copia y no un volcado en tiempo real.

La consecuencia para el operador es que su trabajo no termina al parar de grabar: el material es
un conjunto de ficheros que hay que nombrar, marcar, copiar, comprobar y entregar. De eso trata
este tema.

### Esencia, códec, contenedor, metadatos y proyecto

Ésta es la distinción que ordena todo el tema (oficio):

| Concepto | Qué es | Ejemplos |
|---|---|---|
| Esencia | El material en sí: las imágenes y el sonido | Los cuadros y las muestras |
| Códec | Cómo se comprime la esencia | H.264, H.265, ProRes, DNxHD, PCM |
| Contenedor o encapsulado | Cómo se empaqueta la esencia con sus metadatos | MXF, MOV, MP4, AVI |
| Metadatos | Los datos sobre el material: código de tiempo, nombre, fecha, cámara | Van dentro del contenedor o junto a él |
| Proyecto | Las decisiones de montaje, que no contienen esencia | AAF, EDL, XML |

La regla que las separa: el códec dice cómo se comprime, el contenedor cómo se empaqueta y el
proyecto qué se hizo con ello. Un mismo contenedor puede llevar códecs distintos, y un mismo códec
puede ir en contenedores distintos: por eso «MXF» o «MP4» no dicen, por sí solos, con qué calidad
está grabado un fichero.

### Qué define un formato de grabación

Un formato de grabación es la combinación de todos estos parámetros (oficio, salvo donde se cita):

| Parámetro | Qué dice | Valores de televisión |
|---|---|---|
| Resolución | Cuántos píxeles tiene la imagen | HD: 1.920 × 1.080 (UIT-R BT.709-6, **«Muestras por línea activa 1920»**, **«Líneas activas por imagen 1 080»**). UHD: **«7 680 × 4 320»** y **«3 840 × 2 160»**, con **«Formato de imagen 16:9»** (UIT-R BT.2020-2, cuadro 1) |
| Cadencia | Cuántas imágenes por segundo | Europa: 25 y 50; sistemas americanos: 29,97 y 59,94; cine: 24 y 23,98 |
| Barrido | Progresivo (p) o entrelazado (i) | 1080i a 50 campos; 1080p y 2160p progresivos |
| Muestreo cromático | Cuántas muestras de color por cada muestra de luminancia | 4:2:2 en producción; 4:2:0 en distribución |
| Profundidad | Con cuántos bits se anota cada muestra | 8 o 10 bits |
| Códec y tasa | Cómo se comprime y cuántos datos por segundo | Intracuadro o GOP largo; en Mb/s |
| Audio | Canales y codificación | En cámara, sin comprimir (LPCM) |
| Contenedor | Cómo se empaqueta | MXF, MP4, MOV |

Tres aclaraciones que se preguntan:

- El UHD de televisión (3.840 × 2.160, 16:9) no es el 4K de cine: el de la iniciativa de cine
  digital (DCI) es de 4.096 × 2.160, con una relación de aspecto cercana a 17:9. La comprobación
  es una cuenta: 3.840 ÷ 2.160 = 1,777…, que es 16/9; 4.096 ÷ 2.160 = 1,896…
- El 29,97 no es un redondeo de 30: el sistema americano en blanco y negro iba a 30 cuadros
  exactos, y al añadir el color la cadencia se bajó en una proporción de 1.000 a 1.001. De ahí salen
  29,97, 59,94 y 23,98 (24 con la misma corrección). En Europa se trabaja a 25 y 50, y una cámara
  vendida para todo el mundo ofrece las dos familias, así que comprobar la cadencia es parte de
  preparar la cámara (oficio).
- En el muestreo cromático la primera cifra es la referencia de luminancia y las otras dos cuentan
  las muestras de color: 4:4:4 no tiene submuestreo; 4:2:2 guarda la mitad de color en horizontal;
  4:2:0, la mitad en horizontal y la mitad en vertical. Diez bits dan 1.024 niveles por muestra y
  ocho bits, 256 (cálculo: 2 elevado al número de bits). El tema 9 explica qué se nota en la imagen.

### Cómo se lee el nombre de un formato

Una cámara actual muestra el formato como una cadena de parámetros. Por ejemplo, en una videocámara
Sony PXW-Z200 (2024), que se toma aquí como ejemplo documentado y no como el equipo de Canal
Sur, que no consta publicado, el manual lista (p. 336):

- Vídeo (**«Recording format (video)»**): en contenedor MP4, **«XAVC HS Long 422/420»**, **«XAVC S
  Long 422/420»** y **«XAVC S-I Intra»**; en MXF (**«PXW-Z200 only»**), **«XAVC Long 422/420»**,
  **«XAVC I Intra»** y **«MPEG HD 422 (license required)»**.
- **«Recording format (audio) LPCM 24-bit, 48 kHz, 4-channel»**.
- Cadencias, por ejemplo **«XAVC S Long 422 3840×2160P/119.88P*, 100P*, 59.94P, 50P, 29.97P, 25P,
  23.98P»** y, en MXF, **«XAVC Long 422 1920×1080P/59.94P, 50P, 29.97P, 25P, 23.98P
  1920×1080i/59.94i, 50i»**. El asterisco remite a una nota del manual: **«119.88P and 100P cannot be
  used when Slow & Quick Motion is turned on.»**

Leído por partes, «XAVC S Long 422, 3840×2160P, 50P» es: la familia de formato del fabricante
(XAVC S), la compresión (GOP largo), el muestreo (4:2:2), la resolución (UHD progresivo) y la
cadencia (50 cuadros). El contenedor lo da la familia: en esa cámara, los XAVC S y HS van en MP4 y
los XAVC «a secas», en MXF. Otra cámara Sony expresa además la tasa y la profundidad, por ejemplo
**«200M 4:2:2 10bit»** a **«50p (PAL)»** en XAVC S 4K (Sony, ILCE-7SM3, «Characteristics of each
file format»).

El MPEG HD de la lista es el único formato de la Z200 que no pertenece a la familia XAVC; el manual
lo da sólo en HD (1.920 × 1.080 a 50i, 25p y otras cadencias; 1.280 × 720 a 50p y 59,94p) y no
explica su compresión (p. 336). Lo hace el manual de otra cámara ENG de Sony, la PXW-X400 (2015), que
agrupa sus formatos MPEG bajo **«MPEG-2 Long GOP»** y describe el de 4:2:2 así: **«MPEG HD422 mode:
CBR, 50 Mbps, MPEG-2 422P@HL»**, y el de 4:2:0, **«MPEG HD420 HQ mode: VBR, 35 Mbps (max), MPEG-2
MP@HL»** (Sony, *PXW-X400 Operating Instructions*, «Specifications», p. 144). Es decir: compresión
MPEG-2 en GOP largo, a tasa constante (CBR) de 50 Mb/s en el 4:2:2 y variable (VBR) de hasta 35 Mb/s
en el 4:2:0. Que el MPEG HD 422 de la Z200 sea ese mismo formato se deduce del nombre y del fabricante,
no lo dice su manual. En la misma lista de la X400, el XAVC Long va en **«MPEG-4 AVC/H.264»**
(**«XAVC-L 50 mode: VBR, 50 Mbps (max)»**): la misma cifra de 50 Mb/s, pero como máximo de una tasa
variable y con H.264 en lugar de MPEG-2.

### Los contenedores

| Contenedor | Quién lo desarrolló | Dónde se ve |
|---|---|---|
| MXF | Normalizado por la SMPTE | El contenedor profesional de televisión: cámaras de broadcast, servidores, intercambio y archivo |
| MOV | Apple (QuickTime) | Posproducción; el habitual de ProRes |
| MP4 | La familia de normas MPEG | Cámaras de gama media y ligeras; distribución |
| AVI | Microsoft | Informática doméstica; poco en televisión |

(Quién desarrolló cada uno: oficio.)

El MXF es el que más se pregunta. La Biblioteca del Congreso de Estados Unidos lo describe así:
**«Object-based file format that wraps video, audio, and other bitstreams ("essences"), optimized for
content interchange or archiving by creators and/or distributors, and intended for implementation
in devices ranging from cameras and video recorders to computer systems.»** Recoge que **«most
commentators say "MXF should be seen as the 'digital equivalent of videotape,'"»**, y que **«The
central specification is SMPTE ST 377-1:2011, Material Exchange Format (MXF) -- File Format
Specification»** (Library of Congress, *Sustainability of Digital Formats*, fdd000013).

El MXF es un contenedor, no un códec: no dice nada sobre cómo está comprimido lo que lleva dentro, y
puede envolver material de casi cualquier códec. Lo que distingue unos MXF de otros es el patrón
operacional, que dice cómo se reparten las pistas dentro del fichero:

| Patrón | Norma | Cómo empaqueta | Dónde se usa |
|---|---|---|---|
| OP1a | **«SMPTE ST 378:2004 (Archived 2010) … Operational Pattern 1a (Single Item, Single Package)»** | Todo en un solo fichero: vídeo y todas las pistas de audio juntas | El fichero autónomo: emisión, intercambio y gran parte de las cámaras |
| OP-Atom | **«SMPTE ST 390:2011 … Specialized Operational Pattern "Atom" (Simplified Representation of a Single Item)»** | Un fichero por pista: uno de vídeo y uno por cada canal de audio | El entorno de edición de Avid; y las cámaras P2 de Panasonic |

(Normas: LOC, fdd000013; el reparto de usos es oficio.) Que hay cámaras que graban OP-Atom lo dicen
la misma ficha, **«Panasonic P2 digital video cameras can output MXF OP-Atom files with DVC Pro
encodings»**, y el
fabricante: **«AVC-Intra is recorded as MXF … The MXF operating pattern is OP-ATOM»** (Panasonic,
*AVC-Intra FAQ*, pregunta 12). Por eso una tarjeta P2 no se entiende copiando sólo «el fichero de
vídeo»: el sonido va en ficheros aparte.

El código de tiempo también tiene su sitio en el MXF: la ficha recoge que la EBU ha fijado una
implementación en su **«Recommendation R122-2010»**, **«Material Exchange Format - Timecode
Implementation»**, y que **«This recommendation defines an encoding of source timecode into MXF
files.»** (LOC, fdd000013; la R 122 no se ha leído).

### Los formatos de proyecto

No llevan esencia, sino decisiones; al cámara le llegan cuando el material que graba se monta
fuera o se intercambia entre programas (oficio):

| Formato | Qué lleva | Limitación |
|---|---|---|
| EDL | Sólo la lista de cortes, con códigos de tiempo | Una sola pista de vídeo; ni efectos ni audio complejo |
| AAF | Cortes, pistas, niveles, efectos y metadatos, y puede llevar la esencia | El más completo |
| XML | Lo mismo que el AAF, en la variante de cada fabricante | No es universal |

Las tres dependen del código de tiempo del material: si dos clips de la misma cámara comparten
código, la lista no sabe cuál es cuál. Es una razón más para cuidar el código de tiempo y los
nombres (véase «Metadatos»).

### El *proxy*

Un *proxy* de vídeo es una copia de menor resolución de la imagen y el sonido originales, muy
comprimida, que incluye código de tiempo y algunos otros metadatos básicos (oficio).

Para qué sirve: para trabajar sin mover el material pesado. Se envía por una línea estrecha, se
visiona en la redacción y se monta con él; al final, el montaje se reconforma contra el original. Es
el flujo *offline*-*online*. El código de tiempo es imprescindible porque es lo que permite que las
decisiones tomadas sobre el *proxy* se apliquen al original: un *proxy* sin código de tiempo sirve
para ver, no para montar.

Lo hace la propia cámara, a la vez que graba. En la Z200 (pp. 160-161): **«This function allows you
to simultaneously record a low-resolution proxy clip at the same time as recording a high-resolution
original clip when recording to a memory card.»**; **«The file name extension is “.mp4”.»**; **«The
timecode is also recorded simultaneously.»**; **«The file name consists of the clip name recorded on
the memory card + “S03” suffix.»**; y **«A proxy clip can be subdivided into chunks automatically at
short intervals and the files can be transferred before the end of recording.»** El *proxy* se
guarda en una carpeta propia de la tarjeta (en MP4, **«/PRIVATE/M4ROOT/SUB»** en una SDXC), no junto
al original: dato que importa al copiar la tarjeta (véase «Ingesta»).

### La tasa y la capacidad

La regla que gobierna la capacidad de cualquier soporte (cálculo):

> minutos de grabación = capacidad en bits ÷ tasa en bits por segundo ÷ 60

Recordatorio de unidades: un byte son 8 bits; la tasa de vídeo se da en megabits por segundo (Mb/s)
y la capacidad de la tarjeta en gigabytes (GB). A mitad de tasa, el doble de minutos: por eso una
tabla de capacidades siempre dice para qué formato está hecha.

Dos cuentas de ejemplo (cálculo nominal, sin descontar audio ni metadatos):

- Una tarjeta de 128 GB con un formato de 200 Mb/s: 128 × 8 = 1.024 gigabits = 1.024.000 megabits;
  ÷ 200 = 5.120 segundos, unos 85 minutos.
- La misma tarjeta a 500 Mb/s (el **«500M 4:2:2 10bit»** a 50p del XAVC S-I 4K de la ILCE-7SM3):
  1.024.000 ÷ 500 = 2.048 segundos, unos 34 minutos.

La cifra que da el fabricante puede quedar bastante por debajo de la cuenta nominal. Panasonic, con
su tarjeta de 16 GB: **«approximately 16 minutes of content in AVC-Intra 100 and 32 minutes of
content in AVC-Intra 50, per 16GB P2 card»** en 1080 a 50i, 25p y otras cadencias; y, en 1080 a
23,98p, **«approximately 20 minutes of content in AVC-Intra 100 and 40 minutes of content in
AVC-Intra 50»** (Panasonic, *AVC-Intra FAQ*, pregunta 10). La cuenta nominal a 100 Mb/s daría unos
21 minutos (16 × 8 × 1.000 ÷ 100 = 1.280 s): los 16 del fabricante son una cuarta parte menos. La fuente
no explica la diferencia; que con la misma tarjeta los minutos cambien con la cadencia indica que la
tasa real no es la misma en todas. Que el audio, los metadatos, el *proxy* y el sistema de ficheros
ocupan también sitio en la tarjeta es oficio. Para trabajar, vale la cifra del fabricante o la que
muestra la cámara.

La cámara hace esta cuenta por el operador: la Z200 dice que **«The remaining recording time is
calculated from the remaining capacity of the memory card in each slot and the currently configured
recording format, and is displayed in units of minutes.»** (p. 97). Si se cambia de formato, cambia
el tiempo que queda.

## Códecs

### Qué es un códec y qué se pierde

Códec es la contracción de codificador-decodificador: el procedimiento que reduce los datos de la
esencia al grabar y los reconstruye al reproducir. Casi todo lo que graba una cámara de televisión
está comprimido con pérdida: lo reconstruido no es idéntico al original, y la diferencia se
concentra en lo que el ojo nota menos (oficio).

La mayoría de los códecs de vídeo se apoyan en la transformada discreta del coseno: convierte cada
bloque de píxeles en coeficientes de frecuencia, y la compresión está en recuantificar esos
coeficientes, desechando sobre todo la información de altas frecuencias, el detalle muy fino. Esa
recuantificación es lo que introduce la pérdida. Los defectos que produce (bloques, contornos
sucios, detalle que «hierve») y cómo el operador los evita están en el tema 9.

El audio de cámara, en cambio, no se comprime: se graba en LPCM (véase la Z200 en «Cómo se lee el
nombre de un formato»), porque va a pasar por mezcla y tratamiento, y cada paso sobre audio ya
comprimido acumula defectos; la compresión de audio se hace al final de la cadena (oficio).

### Intracuadro y GOP largo

Es la distinción que más importa al elegir un códec. Un fabricante la resume así: **«Intra/Long GOP
is a movie compression format. Intra compresses the movie by frame, and Long GOP compresses multiple
frames. Intra compression has better response and flexibility when editing, but Long GOP compression
has better compression efficiency.»** (Sony, *Help Guide ILCE-1*, «File Format (movie)»).

Otro fabricante lo explica por sus efectos: el GOP largo **«is usually used for content delivery and
packaged media»**, pero **«any image manipulation or processing will severely degrade the image
quality in long GOP compression schemes»**; en cambio, **«Intra frame compression processes the
entire image within the boundaries of each video field or frame. There is zero interaction between
adjacent frames, so its image quality stands up well to motion and editing.»** (Panasonic, *AVC-Intra
FAQ*, pregunta 2; es documentación comercial de quien vende un códec intracuadro, y así se lee).

| | Intracuadro | GOP largo |
|---|---|---|
| Qué comprime | Cada cuadro por separado | Varios cuadros juntos, aprovechando lo que se repite |
| Tasa para una calidad dada | Mayor | Menor |
| Ficheros | Más grandes | Más pequeños |
| Montaje | Más ligero para el ordenador; corte en cualquier cuadro | Más carga; sufre con cada nueva codificación |
| Movimiento rápido | Lo aguanta bien | Lo sufre |
| Uso típico | Producción, material que se va a montar mucho | Informativos con prisa, envíos, larga duración, distribución |

(Tabla de oficio a partir de las dos citas.)

### H.264 y H.265

Son las dos normas de compresión más extendidas, y las usan muchos formatos de cámara con nombre
propio. Una guía de Sony las presenta así: el XAVC S **«records movies in the widely used MPEG-4
AVC/H.264 codec and therefore enables you to view and edit movies on various compatible devices»**; el
XAVC HS **«records high image quality movies with rich gradations and smaller file sizes using the
MPEG-H HEVC/H.265 codec with 10-bit color sampling»** (Sony, ILCE-7SM3, «Characteristics of each file
format»). El H.265 comprime más a igual calidad, a cambio de más cálculo al decodificar: la misma
guía pide editarlo con **«a video editing software compatible with MPEG-H HEVC/H.265 codec»** y
**«a computer with high processing capability»**.

La compatibilidad es su punto débil también en la transmisión: al elegir el códec de *streaming*,
el manual de la Z200 avisa de que **«When [Codec] is set to [H.265/HEVC], some receivers may not
support playback correctly.»** (p. 202).

### XAVC (Sony)

XAVC es el nombre de una familia de formatos de Sony, no de un códec. Lo que dicen las guías de
fabricante leídas:

| Formato | Códec y compresión | Contenedor en la Z200 |
|---|---|---|
| XAVC S (Long) | H.264, GOP largo | MP4 |
| XAVC HS (Long) | H.265 (HEVC), GOP largo: **«The XAVC HS format uses the HEVC codec, which has high compression efficiency.»**; **«Long GOP compression is used for movies.»** | MP4 |
| XAVC S-I | H.264 intracuadro: **«The XAVC S-I format uses Intra compression for movies. This format is more suitable for editing than Long GOP compression.»** | MP4 |
| XAVC Long / XAVC I (Intra) | GOP largo / intracuadro | MXF |

(Fuentes: Sony, *Help Guide ILCE-1*, «File Format (movie)»; Sony, ILCE-7SM3, que dice que XAVC S-I
graba **«in the widely used MPEG-4 AVC/H.264 codec»**; Z200, p. 336, para los contenedores.) La norma
de compresión de los XAVC en MXF no la nombra el manual de la Z200, y no se ha leído en otra fuente
de Sony.

Para editar, la misma casa recomienda: **«We recommend setting Record Setting to 10-bit 4:2:2 for
editing movies since this setting assures rich gradation.»**, y avisa de que el intracuadro da
**«less load on a computer when editing»**, pero **«the recorded file sizes will be larger than the
files recorded with Long GOP compression»** (ILCE-7SM3).

### Apple ProRes

**«Apple ProRes is a family of proprietary, lossy compressed, high quality video intermediate codecs
primarily supported by the Final Cut Pro (FCP) suite of post-production and editing software
programs.»** (LOC, fdd000389). Es un códec «intermedio», pensado para la posproducción: **«ProRes was
designed to be a high quality intermediate codec that keeps post-production workflow data at 10-bit
quality»**.

- Dos ramas: **«the Apple ProRes 422 Codec Family (described here) and the Apple ProRes 4444 Codec
  Family»**. La 422 tiene cuatro miembros: **«Apple ProRes 422 Proxy»**, **«Apple ProRes 422 LT»**,
  ProRes 422 y **«Apple ProRes 422 HQ»**; la 4444 incluye el **«4444 XQ»**.
- Rasgos de la familia 422: **«4:2:2 source material»**, **«10-bit sample depth»**, **«intrafame
  (I-frame) only»** [sic] y **«variable bit rate»**.
- Contenedor: **«ProRes codecs are usually contained within the QuickTime "mov" wrapper but starting
  with Final Cut Pro 10.3 released on October 27, 2016, the option for using ProRes in the MXF
  Generic Container was added as an option for broadcast delivery.»**
- Calidad frente a tasa, citando a Apple: **«PSNR for Apple ProRes 422 HQ is 15–20 dB higher than
  that for Apple ProRes 422 Proxy, but the Apple ProRes 422 HQ stream has nearly five times the data
  rate of the Apple ProRes 422 Proxy stream.»**

Las tasas de cada variante no se dan: no se ha leído el documento de Apple que las fija.

### Avid DNxHD (SMPTE VC-3)

**«Avid DNxHD is a revolutionary 10 and 8-bit HD encoding technology that significantly reduces
storage and bandwidth requirements while providing mastering-quality HD media.»** Está
**«Codified by SMPTE as VC-3 standard»**; su norma de mapeo en MXF es la **«SMPTE 2019-4 Mapping
VC-3 Coding Units into the MXF Generic Container»**, y **«Avid applications store Avid DNxHD material
natively inside industry-standard MXF files»** (Avid, *Avid DNxHD Technology*, 2012).

El códec **«offers a choice of 8 or 10-bit sampling»** y seis tasas a elegir. La tabla de calidad
del mismo documento («Avid DNxHD encoding quality») da, para cada variante, profundidad, muestreo y
tasa («Bandwidth»); la tabla no dice a qué cadencia. En la 220x, la 220 y la 145, el texto precisa
que el número es la tasa a 1080 entrelazado a 30 cuadros (60 campos), no a 25. En la 444 el número
no es la tasa: la tabla le da **«440 Mb/sec»**.

| Variante | Bits, muestreo y tasa (tabla de Avid) | Qué dice Avid |
|---|---|---|
| DNxHD 444 | 10 bits; 4:4:4; 440 Mb/s | **«10-bit 4:4:4 RGB video sampling»** |
| DNxHD 220x | (la tabla agrupa la 220 y la 220x: 8 y 10 bits; 4:2:2; 220 Mb/s) | **«For superior quality image in a YCbCr-color space for 10-bit sources»**; **«220Mbps is the data rate for 1920 x 1080 30fps interlace sources (60 fields) while progressive sources at 24fps will be 175Mbps»** |
| DNxHD 220 | Ídem | **«For highest quality image when using 8-bit color sources»** |
| DNxHD 145 | 8 bits; 4:2:2; 145 Mb/s | **«145Mbps is the data rate for 1920 x 1080 30fps interlaced sources (60 fields). Progressive sources at 24fps will be 115Mbps and at 25fps will be 120Mbps.»** |
| DNxHD 100 | 8 bits; 4:2:2; 100 Mb/s | **«Sub-samples the video raster from 1920 to 1440 or from 1280 to 960»** |
| DNxHD 36 | 8 bits; 4:2:2; 36 Mb/s | **«High-quality offline editing of HD progressive sources only.»** |

Como el nombre sigue a la tasa, a 25 cuadros las variantes cambian de número. La tabla de
resoluciones del mismo documento («Avid DNxHD family of mastering resolutions») da, para 1080i/50,
la 185x (10 bits) y la 185 (8 bits), las dos a 184 Mb/s; la 120, a 121 Mb/s; y la 85, a 84 Mb/s,
esta con la imagen reducida a 1.440 × 1.080 (**«Sub-sampled to 1440x1080»**). Para 1080p/25 repite
esas cuatro y añade la 365x (10 bits, 4:4:4, 367 Mb/s) y la 36, a 36 Mb/s. Todas son 4:2:2 salvo la
365x.

Su sucesor para resoluciones mayores que HD (DNxHR) no se ha leído en fuente de Avid.

### AVC-Intra (Panasonic)

**«AVC-Intra … is a professional intra-frame video codec with bit rates of 50 and 100Mb/s, utilizing
the High 10 Intra and High 422 Intra profiles of H.264 respectively.»** Tiene **«two modes: AVC-Intra
100 … and AVC-Intra 50»**; el de 100 es **«4:2:2, 10-bit Intra-frame coding»** y **«records the full
1920x1080 raster»** (Panasonic, *AVC-Intra FAQ*, preguntas 1 y 4). Se graba en MXF OP-Atom en
tarjetas P2 y **«AVC-Intra supports MXF metadata.»** (preguntas 12 y 13).

Es un ejemplo de que «H.264» no es sinónimo de GOP largo: la norma tiene perfiles intracuadro, y
AVC-Intra usa esos.

### Cuadro resumen

| Nombre | Qué es | Compresión | Contenedor habitual |
|---|---|---|---|
| H.264 (AVC) | Norma de compresión | GOP largo o intracuadro, según perfil | MP4, MXF, MOV |
| H.265 (HEVC) | Norma de compresión, más eficiente | En cámara, GOP largo | MP4 |
| XAVC | Familia de formatos de Sony | H.264 o H.265; intra o GOP largo | MP4 o MXF |
| AVC-Intra | Códec de Panasonic sobre H.264 | Intracuadro, 50 y 100 Mb/s | MXF OP-Atom |
| ProRes | Familia de códecs intermedios de Apple | Intracuadro, tasa variable | MOV (también MXF) |
| DNxHD | Códec de Avid, norma SMPTE VC-3 | De 36 a 440 Mb/s según variante; el tipo de compresión no lo desarrolla el documento de Avid leído | MXF (también MOV) |
| LPCM | Audio sin comprimir | — | Dentro del fichero de vídeo |

Qué códec elige el cámara: casi nunca lo decide en cada toma; lo fija la casa o el encargo. Lo que
sí le toca es comprobar que la cámara está en el formato pedido (resolución, cadencia, códec, tasa)
antes de empezar, y avisar si cambia algo (oficio). Las tasas mínimas que la EBU recomienda por
nivel de cámara están en el tema 9.

## Tarjetas

### Los soportes de estado sólido

Las cámaras profesionales graban en tarjetas de memoria de estado sólido. Las propias de cada
fabricante (oficio, salvo donde se cita):

| Soporte | Qué es | De quién |
|---|---|---|
| Tarjeta SxS | Tarjeta de memoria de estado sólido para cámara profesional | Sony y SanDisk |
| Tarjeta P2 | Tarjeta de memoria profesional; graba MXF OP-Atom (*AVC-Intra FAQ*) | Panasonic |
| Disco XDCAM | Disco óptico profesional, ya en retirada | Sony |

Y, cada vez más, tarjetas de uso general. La Z200 es un ejemplo: **«The unit records audio and video
on CFexpress Type A memory cards (available separately) or SDXC memory cards (available separately)
inserted in the card slots. The memory cards are also used for proxy recording and storing/loading
settings, and when upgrading (software update).»** (p. 67). La tarjeta, por tanto, no sólo guarda el
material: guarda también el *proxy* y los ajustes de la cámara.

### Las clases de velocidad

Una tarjeta tiene que escribir al menos tan rápido como la tasa del formato; si no, la grabación se
corta. La SD Association define tres familias de clases: **«The Speed Classes defined by the SD
Association are Class 2, 4, 6 and 10.»**; **«The UHS Speed Classes defined by the SD Association are
UHS Speed Class 1 (U1) and UHS Speed Class 3 (U3).»**; **«The Video Speed Classes defined by the SD
Association are V6, 10, 30, 60 and 90.»** Y lo que significa el número: **«Speed Class symbols with a
number indicate minimum writing speed»** (SD Association, «Speed Class»).

Las cifras las da la propia SD Association en su libro blanco sobre la clase de vídeo, en un cuadro
(«Figure 1», leído sobre la imagen) cuya primera columna es la «Minimum Sequential Write Speed», es decir, la velocidad
mínima de escritura secuencial, en megabytes por segundo (MB/s):

| Escritura mínima | Clase de velocidad | Clase UHS | Clase de vídeo |
|---|---|---|---|
| 90 MB/s | — | — | V90 |
| 60 MB/s | — | — | V60 |
| 30 MB/s | — | U3 | V30 |
| 10 MB/s | Class 10 | U1 | V10 |
| 6 MB/s | Class 6 | — | V6 |
| 4 MB/s | Class 4 | — | — |
| 2 MB/s | Class 2 | — | — |

Es decir, el número de la clase de vídeo y de la clase de velocidad es la escritura mínima en MB/s,
y el de la UHS no (U1 son 10 MB/s y U3, 30 MB/s). El documento resume las tres familias: **«Speed
Class (C2, C4, C6 and C10), UHS Speed Class (U1 and U3) and now Video Speed Class (V6, V10, V30, V60
and V90)»**, y dice que la clase de vídeo **«adds new capture rates of 60 MB/s and 90 MB/s»** (SD
Association, *Video Speed Class: The new capture protocol of SD 5.0*, febrero de 2016, p. 4).

Dos salvedades del mismo documento. La primera: cada familia mide con su propio método, y una
tarjeta puede cumplir una y no su equivalente de otra: **«an SD memory card may meet V30
requirements, by supporting 30 MB/s capture using the Video Speed Class protocol, yet only meet C10
requirements, supporting 10 MB/s capture with the Speed Class protocol»** (p. 5). Lo que cuenta es el
símbolo que pide la cámara. La segunda, la regla de uso: **«match the SD memory card to your
specific application’s requirements»**, y **«A guide to help consumers select the right memory card
will be provided in device owner’s manuals.»** (p. 5).

Para elegir, la tasa del formato se pasa de megabits a megabytes, dividiendo entre 8 (cálculo), y se
busca una clase cuya escritura mínima la iguale o la supere. Un formato de 200 Mb/s son 25 MB/s: le
basta una V30 o una U3 (30 MB/s) y no le basta una V10, una U1 ni una Class 10 (10 MB/s). Uno de
500 Mb/s son 62,5 MB/s: supera la V60 y pide la V90. La tabla del manual de la cámara manda sobre
esta cuenta.

Las tarjetas CFexpress usan otra clasificación: el manual de la Z200 las agrupa como **«VPG200»** y
**«VPG400»** (p. 68); qué garantiza cada una no se ha leído en la fuente que la define.

La regla práctica la da el fabricante: **«The guaranteed operating conditions will vary depending on
the [Rec Format] and recording settings.»** (Z200, p. 68). Qué tarjeta vale para qué formato se mira
en la tabla de tarjetas recomendadas del manual de la cámara, formato por formato; no se deduce de la
capacidad, porque una tarjeta grande puede ser lenta (oficio). Y, si se graba en relevo con
tarjetas SD, **«use SD cards of the same type»** (Z200, p. 99).

### Dos ranuras: relevo y grabación simultánea

Las cámaras de dos ranuras permiten dos formas de usarlas:

- Grabación en relevo, para no parar: **«When memory cards are inserted in both card slots A and
  B, recording automatically switches to the second memory card just before the remaining capacity
  on the first card reduces to zero (relay recording).»** Se puede seguir indefinidamente cambiando
  la tarjeta llena, pero **«only change memory cards in card slots for which the access indicator is
  off»**. Y un aviso: **«Video created using the relay recording function of the unit cannot be
  played back seamlessly on the unit.»** (Z200, p. 98). Un plano largo queda partido entre dos
  tarjetas, y quien lo ingesta tiene que saberlo (oficio).
- Grabación simultánea, para tener copia desde el origen: **«You can record to both memory card A
  and memory card B simultaneously by setting [Simul Rec]»**; **«In 2-slot simultaneous recording, the
  generated clip will have the same clip name on both media.»** (Z200, p. 153). Es la primera copia
  de seguridad, hecha en la cámara (véase «Copia de seguridad»).

Las dos no se hacen a la vez con las mismas dos ranuras: o una tarjeta sigue a la otra, o las dos
graban lo mismo (oficio).

### Sacar la tarjeta

**«If the unit is turned off or the memory card is removed while the memory card is being accessed,
the integrity of data on the card cannot be guaranteed. All data recorded on the card may be
discarded. Always make sure the access indicator is green or off before turning off the unit or
removing the memory card.»** Y un dato que evita un parte de avería innecesario: **«When removing a
memory card immediately after recording is finished, the memory card may be hot, but this does not
indicate a problem.»** (Z200, p. 95). Otro manual añade el cable y la batería a la lista: **«Do not
remove the battery pack or the memory card, disconnect the USB cable, or turn the camera off while
the access lamp is lit up.»** (Sony, *Help Guide ILCE-1*, «Notes on memory card»).

### Formatear

**«Formatting a memory card erases all data, including recorded video data and setup files.»** La
Z200 ofrece dos modos: **«[Full Format]: Initializes the memory card completely, including the data
region and data management information. [Quick Format]: Initializes the data management information
of the memory card only.»** Si en la tarjeta quedan ficheros pendientes de envío, avisa con un
mensaje del tipo **«A transfer target file exists.»** (p. 96).

Tres reglas de fabricante sobre dónde y cuándo se formatea:

1. En la cámara que va a grabar: **«Memory card formatted with a computer is not guaranteed to
   operate with the product. Be sure to format the memory card using this product.»** (ILCE-1). Y, al
   pasar una tarjeta de una cámara a otra: **«First, make a backup of the card, then reformat the
   card in the device to be used.»** (Z200, p. 96).
2. Nunca porque lo pida un equipo que no la reconoce: **«If you connect your camera to an
   incompatible device, you may be prompted to format the card. Never format the card in response to
   this prompt, as doing so will erase all data on the card.»** Ese equipo suele ser uno que no lee
   el sistema de ficheros: **«exFAT is the file system used on SDXC memory cards or CFexpress Type A
   memory cards.»** (ILCE-1).
3. Cuando la tarjeta se ha fragmentado de tanto grabar y borrar: **«movie recording may be
   interrupted in the middle of shooting. If this happens, save your images to a computer or other
   storage location, then execute [Format] using this camera.»** (ILCE-1).

Y la regla de oficio que las resume: una tarjeta no se formatea hasta que su contenido está copiado
y la copia comprobada (véase «Copia de seguridad»). Formatear es borrar.

### Proteger y cuidar la tarjeta

- Protección contra escritura: en una SD, con el conmutador en **«LOCK»** **«you cannot record or
  delete images»** (ILCE-1); la Z200 muestra un icono **«(Protected)»** si la tarjeta está protegida
  (p. 31). Es útil al revés: una tarjeta ya grabada, bloqueada antes de ingestarla, no se puede
  borrar por error (véase «Ingesta»).
- Cuidado físico: **«Do not expose the memory card to water. Do not strike, bend or drop the memory
  card.»**; **«Do not touch the terminal section of the memory card with your hand or a metal
  object.»**; **«Do not attach a label on the memory card itself nor on a memory card adaptor.»**
  (ILCE-1), porque **«You may not be able to remove the memory card.»**; el mismo manual sí contempla
  escribir en el espacio de notas de la tarjeta, sin apretar (**«Do not press down hard when writing in
  the memo space on the memory card.»**). Lo demás se anota en su funda o caja (oficio).
- Calor: **«The temperature of the CFexpress card is high. Replace the card or allow it to cool down
  before using it again.»** (mensaje ***[Media Temperature High]***, Z200, p. 310).

### Los avisos de la tarjeta

| Mensaje (Z200) | Qué dice el manual |
|---|---|
| ***[Media Near Full]*** | **«The remaining capacity on the memory card is getting low. Replace at the earliest convenience.»**; salta cuando entre las dos tarjetas quedan menos de 5 minutos (p. 97) |
| ***[Media Full]*** | **«Clips could not be recorded or copied because there is no remaining capacity on the memory card. Replace immediately.»** |
| ***[Clips Near Full]*** / ***[Clips Full]*** | Se acerca o se alcanza el número máximo de clips de la tarjeta |
| ***[Media(A) Life Near End]*** / ***[Media(A) Life End]*** | **«The memory card is approaching the end of its life.»** / **«has reached the end of its life. Replace immediately.»** |
| ***[Media Temperature High]*** | Tarjeta CFexpress caliente |

(Z200, pp. 310-311.) El número de clips también se agota: **«Up to approximately 9999 clips in XAVC
S format or 600 clips in XAVC format (PXW-Z200 only) can be recorded on one memory card.»** (p. 97).
Las tarjetas tienen vida útil: una que avisa de fin de vida se retira y se comunica (tema 11).

## Metadatos

### Qué son y quién los pone

Metadatos son los datos sobre el material: cuándo se grabó, con qué cámara y formato, qué código de
tiempo tiene cada cuadro, cómo se llama el clip, si es bueno o malo (oficio). Unos los pone la
cámara sola (fecha, formato, ajustes); otros dependen de lo que el operador haya configurado antes
(nombre, código de tiempo, bits de usuario); y otros los pone el operador mientras graba (marcas y
banderas). Los primeros no cuestan nada; los otros son los que ahorran tiempo en la redacción y en
el montaje, y los que se pierden si no se hacen en el momento.

### El clip y su nombre

**«When you stop recording, the video, audio, and accompanying data from the start to the end of
the recording are saved as a single “clip” on a memory card.»**; **«Each clip recorded by the unit is
automatically assigned a name using the naming format set using [TC/Media] – [Clip Name Format]»**
(Z200, p. 99).

En la Z200 el nombre se compone de un título y un número (p. 252): el título se escribe en
***[Title Prefix]*** o ***[Title Name Settings]***, y el número de cuatro cifras se fija en
***[Number Set]***, de **«0001 to 9999»**; ***[Title Prefix]*** y ***[Number Set]*** son sólo del
PXW-Z200 y sólo se configuran al grabar en MXF. La numeración puede seguir un contador de la cámara
(***[Series]***, que salta al número más alto de la tarjeta si éste es mayor) o empezar por el número
más alto que haya en la tarjeta (***[Reset]***). Poner en el título algo que identifique la cámara o el
encargo, y no repetir números entre tarjetas, evita que dos clips distintos se llamen igual en el
servidor (oficio).

Un clip tampoco es ilimitado: **«The maximum recording duration of a clip in XAVC S format is 13
hours, at which point recording stops automatically. In XAVC format (PXW-Z200 only), the maximum is
24 hours»** (Z200, p. 99).

### El código de tiempo

El código de tiempo es la etiqueta que numera cada cuadro en horas, minutos, segundos y cuadros
(HH:MM:SS:CC), y es el instrumento de sincronización de toda la cadena (oficio). Viaja de dos
formas:

| Forma | Cómo viaja | Dónde se usa |
|---|---|---|
| LTC, longitudinal | Como una señal de audio, por un cable o canal propio | Entre equipos: cámara, grabador de sonido, generador |
| VITC, vertical | Dentro de la propia señal de vídeo, en el intervalo vertical | Dentro de la cadena de vídeo |

Una palabra de LTC ocupa 80 bits por cuadro; de ellos, 32 son bits de usuario (oficio; la norma
SMPTE que lo fija no se ha leído).

Cómo corre el código se decide con dos ajustes. En la Z200 (menú ***[TC/Media] – [Timecode]***, p. 251):

| Ajuste | Opciones (fábrica en cursiva) | Qué hace |
|---|---|---|
| ***[Mode]*** | *[Preset]* / [Regen] / [Clock] | **«[Preset]: Starts running from a preset value.»**; **«[Regen]: Starts running from the timecode of the end of the previous clip.»**; **«[Clock]: Uses the internal clock as the timecode.»** |
| ***[Run]*** | *[Rec Run]* / [Free Run] | **«[Rec Run]: Runs only when recording.»**; **«[Free Run]: Always running, regardless of recording operation.»** |
| ***[TC Format]*** | *[DF]* / [NDF] | **«[DF]: Drop Frame»**; **«[NDF]: Non-Drop Frame»** |

Qué elegir (oficio):

- Rec Run con Regen: el código es continuo de un clip al siguiente, como en una cinta; no hay dos
  clips con el mismo código en la misma tarjeta.
- Free Run o Clock: el código dice la hora a la que pasó algo. Es lo que se necesita para
  sincronizar varias cámaras o una cámara con un grabador de sonido, y para localizar un hecho por
  la hora. La pregrabación lo impone: **«When Picture Cache Rec is turned on, the timecode is recorded
  in [Free Run] mode even if set to [Regen] or [Rec Run].»** (Z200, p. 151).
- DF o NDF sólo importa a 29,97 y 59,94: como esa cadencia no es entera, un código que cuente 30
  cuadros por segundo se adelanta al reloj, y el *drop frame* salta números de cuadro para
  corregirlo (no salta imágenes). A 25 y 50 cuadros no hay nada que corregir.

El Libro de estilo de Canal Sur lo trata como un pacto: **«En cada grabación el código de tiempo es
un acuerdo básico entre periodista y cámara, especialmente cuando van a estar físicamente separados
durante la cobertura y cuando hay poco margen para la posterior elaboración del correspondiente
vídeo. En este caso puede usarse un código de tiempo real previamente acotado, aunque también puede
ser recomendable es el TC poniendo el marcador a 00:00:00 al principio de la cinta. Esta referencia
es generalmente mejor, sobre todo cuando el material va a ser usado por terceras personas.»** (5.3.3,
p. 81; el «es» que sobra está en el original). El pacto sigue valiendo; la referencia a la cinta es de 2004.

### Los bits de usuario

**«You can add an 8-digit hexadecimal number to a clip as user bits. You can also set the user bits
to the current time.»** (Z200, p. 99). En el menú, ***[Fix]*** usa un valor fijo y ***[Time]*** la
hora, minuto y segundo actuales (p. 251). Ocho cifras hexadecimales son 32 bits (8 × 4). Sirven para
anotar lo que el código no dice: la fecha, el número de cámara o de tarjeta (oficio).

### La aritmética del código de tiempo

La duración entre dos códigos se calcula restando campo a campo, de derecha a izquierda, con
acarreos, y sabiendo a qué cadencia va el material (cálculo). Ejemplo a 25 cuadros por segundo, de
00:47:17:23 a 01:23:54:00:

| Campo | Operación | Resultado |
|---|---|---|
| Cuadros | 00 − 23 no se puede: se toma prestado un segundo (25 cuadros) | 25 − 23 = 2 |
| Segundos | 54 − 1 prestado = 53; 53 − 17 | 36 |
| Minutos | 23 − 47 no se puede: se toma prestada una hora | 83 − 47 = 36 |
| Horas | 1 − 1 prestada = 0; 0 − 0 | 0 |

La resta da 00:36:36:02. Si el último código se cuenta como parte del plano (duración inclusiva), se
suma un cuadro: 00:36:36:03. A 24 o a 30 cuadros el campo de cuadros saldría distinto, porque el
préstamo es de 24 o de 30.

### Sincronizar el código de dos equipos

La Z200 puede recibir el código de otro equipo o darlo; la función es sólo del PXW-Z200, no del
HXR-NX800 (p. 298). Para esclavizarla: modo
***[Preset]*** con ***[Free Run]***, conmutador TC IN/OUT en IN y código de referencia en el conector;
**«The timecode generator of the unit acquires lock with the reference timecode, and “EXT-LK” is
displayed on the screen.»**, y **«Once about ten seconds have elapsed after the timecode locks, the
external lock state is maintained even if the external reference timecode source is
disconnected.»**

Los avisos del manual: **«do not start recording immediately. Wait for a few seconds until the
timecode generator stabilizes before recording.»**; **«If the frequency of the reference timecode
and the frame frequency on the unit are not the same, lock cannot be acquired»**; y **«The timecode
may shift by one frame per hour with respect to the reference timecode.»** Por eso, en una jornada
larga, se vuelve a sincronizar de vez en cuando (oficio). Para que la cámara dé el código a otro
equipo, la fuente tiene que estar en un modo que corra siempre, **«([Free Run] or [Clock])»**.

Cómo se sincroniza el sonido grabado aparte está en el tema 6; el trabajo con varias cámaras, en el
tema 15.

### Marcas y banderas

La cámara permite señalar lo importante mientras se graba, con botones asignables (Z200, p. 242):
**«[Shot Mark1]: Adds shot mark1 to the currently recording or playing clip.»** (y lo mismo
***[Shot Mark2]***), y las banderas ***[Clip Flag OK]***, ***[Clip Flag NG]*** y ***[Clip Flag
Keep]***. **«You can add an [OK] clip flag to a clip being recorded or just recorded»**, y **«The
thumbnail screen can be displayed sorted by clip flag type»** (p. 160).

Para qué sirven (oficio): la marca señala un instante dentro de un clip (la frase buena de una
declaración, el momento en que sale alguien de un edificio); la bandera califica el clip entero (OK,
no vale, guardar). Con cinco minutos para el cierre, el redactor que recibe cuarenta clips agradece
saber cuáles son los tres buenos. Si el sistema de la casa lee esas marcas al ingestar es cosa suya;
no consta cómo lo hace CSRTV.

### Los metadatos dentro del fichero

Los metadatos van con el material si se copia entero. Los contenedores profesionales los llevan
dentro (**«AVC-Intra supports MXF metadata.»**, Panasonic), y las cámaras guardan además ficheros de
gestión y el *proxy* en otras carpetas de la tarjeta (el menú ***[Update Media]*** de la Z200
**«Updates the management file on memory cards»**, p. 252). Copiar sólo el fichero de vídeo pierde
parte de esa información (véase «Ingesta»). Los identificadores únicos de material y los metadatos
de planificación que algunas cámaras admiten no se han leído en su fuente y no se tratan.

## Ingesta

### Qué es la ingesta

Ingestar es meter el material en el sistema donde se va a trabajar: el servidor de la redacción o
de edición. En una casa de televisión no es sólo copiar ficheros: es un proceso con metadatos,
comprobación y, a menudo, conversión al formato de la casa (oficio). Tiene tres formas:

| Forma | Qué es |
|---|---|
| Ingesta de fichero | Copiar material que ya viene en fichero (una tarjeta, un disco, un envío) con su comprobación de integridad |
| Ingesta en directo (*crash record*) | Grabar una señal que entra ahora: un enlace, una señal de agencia, una cámara en directo |
| Ingesta programada | Grabar automáticamente en un horario previsto, sin nadie delante, con recurrencia (diaria, semanal, mensual) |

Al cámara le toca sobre todo la primera, y la segunda cuando envía en directo (tema 13). Quién
ingesta en CSRTV —el propio cámara, un técnico de ingesta o la redacción— y con qué sistema no consta
en un documento publicado.

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
   clips (véase «Copia de seguridad»). La guía citada recomienda **«Check fixity on all ingests»** y
   **«Virus-check high risk content»** (las dos, en el segundo de sus cuatro niveles).
4. Revisar lo que ha llegado: número de clips, clips partidos por la grabación en relevo (que la
   Z200 **«cannot be played back seamlessly»**, p. 98), clips sin sonido (cámara lenta, tema 15).
5. Anotar y entregar (véase «Entrega de material»). Sólo después, y con la copia comprobada, la
   tarjeta vuelve a la cámara para formatearse allí.

### La ingesta desde el lugar

Cuando no hay tiempo de llevar la tarjeta, se envía el material por red desde la cámara o desde un
ordenador (oficio). Lo habitual es enviar primero el *proxy*, que pesa poco, y el original después
o nunca.

La Z200 lo hace mientras graba: con ***[Auto Upload (Proxy)]*** en ***[Chunk]***, el *proxy* se graba
en trozos y **«the proxy clip can be uploaded while the main recording is in progress»**; el trozo
es de **«[30s]»** por defecto, o de 1 o 2 minutos (p. 163). Tiene un precio: **«The media in slot B
is dedicated to recording proxy clips in chunks, hence relay recording and 2-slot simultaneous
recording are not supported.»** (p. 163). Enviar mientras se graba cuesta la copia simultánea.

Otras incompatibilidades del mismo manual que conviene conocer antes de salir: el *proxy* no
funciona con la cámara lenta (**«Proxy recording cannot be set to [On] at the same time as Slow &
Quick Motion.»**, p. 162); y la pregrabación **«cannot be used in combination with Interval Rec,
2-slot simultaneous recording, or proxy recording»** (p. 151). Cada función de la cámara que ocupa
una ranura o el *proxy* excluye a otras: el cámara decide cuál necesita para cada encargo.

Cómo se envía (seguridad del envío, FTP y FTPES) está en «Entrega de material».

## Copia de seguridad

### Por qué

Hasta que el material está copiado, existe en un solo sitio: una tarjeta que se puede perder,
romper, borrar o formatear por error. Un fabricante lo dice en una línea: **«Be sure to back up the
data for protection.»** (Sony, *Help Guide ILCE-1*, «Notes on memory card»). La copia de seguridad
no es un trámite de archivo: es la protección de la jornada de trabajo (oficio).

### La primera copia: en la cámara

La grabación simultánea en dos tarjetas (***[Simul Rec]***, véase «Tarjetas») da dos originales
idénticos desde el primer segundo, con el mismo nombre de clip. Es la única copia que existe antes de
llegar a un ordenador (oficio). Sus límites están en el mismo manual: no es compatible con la
pregrabación ni con el envío del *proxy* por trozos (Z200, pp. 151 y 163).

### La copia comprobada: suma de verificación

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

Aplicado al cámara (oficio): se copia con un programa que calcula la suma del original y de la
copia y las compara; si coinciden, la copia es idéntica. Comparar sólo el tamaño de los ficheros no
lo garantiza.

### La regla 3-2-1

INCIBE la formula así: la regla 3-2-1 **«se refiere a disponer siempre de tres copias de seguridad de
un mismo tipo de información, en dos dispositivos distintos y, una de ellas, almacenarla en un lugar
diferente a los demás»** (INCIBE, «Definiendo mi estrategia de copias de seguridad», 29-09-2021).

Traducida a una jornada de cámara (oficio, y cada casa tiene su procedimiento): el original en la
tarjeta, una copia en un disco del equipo y otra ya enviada al servidor de la casa; o dos discos que
viajan por separado. Mientras no haya dos copias comprobadas, la tarjeta no se formatea.

### Lo que no es una copia de seguridad: el RAID

Un RAID es un conjunto de discos que el sistema ve como uno solo (oficio):

| Nivel | Cómo escribe | Mínimo de discos |
|---|---|---|
| RAID 0 | Reparte los datos, sin redundancia | 2 |
| RAID 1 | Espejo: escribe lo mismo en dos discos | 2 |
| RAID 5 | Reparte con paridad distribuida | 3 |
| RAID 6 | Reparte con doble paridad | 4 |

El número del nivel no es el número de discos: el RAID 1 necesita dos, porque el espejo necesita un
disco donde escribir y otro donde copiar. Y el RAID protege del fallo de un disco (de dos, en el
RAID 6), no de un borrado,
de un fichero corrupto que se copia a los dos lados ni de un robo o un incendio. Un RAID 0 ni
siquiera protege: si falla un disco, se pierde todo. No es una copia de seguridad; es lo que mantiene
vivo el trabajo mientras se hace (oficio).

### El archivo a largo plazo: la LTO

Lo que ya no se toca pasa al archivo. La LTO es una tecnología de almacenamiento en cinta magnética
de alta capacidad, escalable y regrabable; «abierta» porque es una norma abierta, fabricada por
varias casas (oficio). Sus ventajas: el coste por terabyte más bajo en volúmenes grandes; una cinta
guardada no consume energía; dura décadas en condiciones de archivo; y, fuera de la biblioteca, no
está en la red. Su desventaja fija su uso: el acceso es secuencial y lento. No es almacenamiento de
trabajo, es archivo (oficio). El archivo de CSRTV, su sistema y sus plazos no los decide el cámara, y
no constan en un documento publicado.

## Entrega de material

### Lo que recomendaba el Libro de estilo

El Libro de estilo de Canal Sur (2004) recomendaba una forma de entregar en cinta, y hacía obligatoria
la separación entre noticias: **«Es conveniente
mantener la norma de registrar una sola noticia por cinta, después de un mínimo de treinta segundos
de barras al principio de la misma. Si hay dos noticias en el mismo soporte deben separarse con un
minuto de barras.»** (5.3.3, p. 82). Es una regla del soporte de cinta y hoy es histórica: con
tarjetas, cada clip ya es un fichero separado, y qué se graba al principio lo decide cada casa. No
consta una regla vigente de CSRTV que la sustituya.

Sigue valiendo, en cambio, la comprobación antes de irse: **«Otra norma elemental de prudencia es
revisar la grabación en el mismo lugar de la misma para comprobar que es correcta desde la
perspectiva de la imagen y del sonido.»** (5.3.3, p. 82). Con fichero se hace igual: la Z200 tiene un
modo de revisión del último clip (***[Rec Review]***, p. 99).

### Qué se entrega

No consta publicado un protocolo de entrega de material de CSRTV (nomenclatura, carpetas, formato de
la casa, sistema de envío). Lo que sigue es oficio, y así se da:

1. El material completo: la tarjeta o la copia entera, con su estructura, no una selección.
   Seleccionar es trabajo de la redacción; el cámara señala (marcas y banderas), no descarta.
2. Identificado: tarjetas en su funda con el encargo y la fecha; clips con un nombre que diga de
   qué cámara son; si hay varias tarjetas, su orden.
3. Con sus datos: qué formato y cadencia, qué código de tiempo se usó (hora real o desde cero,
   según el acuerdo con el periodista), dónde están las declaraciones y los momentos clave (códigos
   de tiempo o marcas).
4. Con sus avisos: lo que falta o falla (un canal con ruido, un plano en cámara lenta sin sonido,
   un clip partido entre dos tarjetas, una imagen que puede afectar a un menor o a una víctima, tema
   12). Un aviso a tiempo evita que el defecto llegue a emisión.
5. Con la copia hecha: quien entrega sabe si queda otra copia comprobada y dónde, y no formatea
   hasta confirmarlo.

### El envío por red

Cuando el material viaja por internet, el protocolo importa. El manual de la Z200 lo dice sin
rodeos: **«In FTP, the contents, user name, and password are not encrypted. For secure data transfer,
use FTPES (FTPS).»**; y **«You can transfer files with encryption using FTPS in Explicit mode (FTPES)
for the connection with the file transfer destination server.»** (p. 196). Con FTP sin cifrar, quien
intercepte la conexión ve el material y la contraseña del servidor de la casa (oficio).

Las otras precauciones del envío (oficio): mandar primero el *proxy* o lo más urgente; comprobar que
el fichero ha llegado entero antes de borrar nada; no formatear una tarjeta que tiene envíos
pendientes (la Z200 lo advierte al formatear, véase «Tarjetas»). Las mochilas, los enlaces y el
*streaming* están en el tema 13.

### Un supuesto práctico

Un equipo ENG cubre una rueda de prensa y una declaración a la salida, con envío urgente para el
informativo de mediodía y la pieza larga por la tarde. Qué hace el cámara (oficio, con los datos del
tema):

| Momento | Qué hace | Por qué |
|---|---|---|
| Antes de salir | Comprueba formato y cadencia pedidos (por ejemplo, HD 1080 a 50 cuadros); formatea en la cámara las tarjetas ya copiadas; pone nombre de clip y código de tiempo | Formato de la casa; tarjetas limpias; clips identificables |
| En el lugar | Acuerda con el periodista el código de tiempo (hora real si hay más de una cámara); decide entre copia simultánea o *proxy* por trozos, porque en la Z200 no se pueden tener los dos | Sincronía; la cámara obliga a elegir |
| Mientras graba | Marca la frase buena; bandera OK a los clips útiles; vigila el aviso de tarjeta llena | La redacción encuentra lo bueno sin visionar todo |
| Tras la declaración | Revisa en el sitio imagen y sonido; envía por FTPES el *proxy* o el clip de la declaración | Libro de estilo; envío seguro |
| En la redacción | Bloquea la tarjeta, copia entera con suma de verificación a dos destinos, revisa los clips, entrega con sus avisos | Copia comprobada y cadena de custodia |
| Al final | Formatea la tarjeta en la cámara sólo cuando hay dos copias comprobadas | Formatear es borrar |

## Documentos técnicos que el tema cita

| Documento | Qué se toma |
|---|---|
| UIT-R BT.709-6 | 1.920 muestras por línea activa y 1.080 líneas activas (HD) |
| UIT-R BT.2020-2, cuadro 1 | 7.680 × 4.320 y 3.840 × 2.160, formato 16:9 (UHD) |
| Library of Congress, fdd000013 (MXF) | Definición del MXF, «equivalente digital de la cinta», SMPTE ST 377-1, ST 378 (OP1a), ST 390 (OP-Atom), EBU R 122, cámaras P2 en OP-Atom |
| Library of Congress, fdd000389 (ProRes 422) | Definición, ramas y miembros, rasgos, contenedor MOV y MXF, relación calidad-tasa |
| Avid, *Avid DNxHD Technology* (2012) | Definición, VC-3 y SMPTE 2019-4, MXF, variantes; bits, muestreo y tasa de cada una (tabla de calidad); variantes a 1080i/50 y 1080p/25 (tabla de resoluciones) |
| Panasonic, *AVC-Intra FAQ* | Tasas y perfiles H.264, 4:2:2 10 bits, MXF OP-Atom, metadatos, minutos por tarjeta de 16 GB según cadencia, intracuadro y GOP largo |
| Sony, *PXW-Z200/HXR-NX800 Help Guide* (2024) | Formatos y audio, tarjetas y avisos, relevo, simultánea, formateo, *proxy* y envío por trozos, nombre de clip, código de tiempo, bits de usuario, marcas y banderas, FTPES |
| Sony, *Help Guide ILCE-1* y ILCE-7SM3 («Characteristics of each file format») | XAVC S, HS y S-I; intracuadro y GOP largo; recomendación de 10 bits 4:2:2; notas de tarjeta |
| SD Association, «Speed Class» | Clases de velocidad, UHS y de vídeo; el número indica la escritura mínima |
| SD Association, *Video Speed Class: The new capture protocol of SD 5.0* (2016) | Escritura mínima en MB/s de cada clase (Figure 1); una tarjeta puede cumplir V30 y sólo C10; ajustar la tarjeta a lo que pide el equipo |
| Sony, *PXW-X400 Operating Instructions* (2015) | MPEG HD422 y HD420 (MPEG-2 GOP largo, tasas, perfiles) y XAVC-L 50 en H.264 |
| Digital Preservation Coalition, «Fixity and checksums» | Fijeza, suma de verificación, cadena de custodia, MD5 y SHA-256, *data scrubbing*, bloqueo de escritura y sus salvedades, niveles |
| INCIBE, 29-09-2021 | Regla 3-2-1 |
| Libro de estilo de Canal Sur, 2004, 5.3.3 | Código de tiempo como acuerdo; una noticia por cinta y barras (histórico); revisar en el lugar |

Las normas SMPTE (ST 377-1, 378, 390, 2019-x, RDD 36 y 44), la EBU R 122 y las normas H.264 y H.265
se nombran como las citan esas fuentes; su texto no se ha leído.

## Lo que este tema no da, y dónde está

- Qué cámaras, formatos de la casa, códec de ingesta, sistema de ingesta y protocolo de entrega usa
  CSRTV: no constan en un documento publicado localizado. Los ejemplos son de cámaras Sony con
  manual público, no del equipo de Canal Sur.
- Una regla vigente de CSRTV sobre barras, tono o claqueta al principio de cada tarjeta: el Libro de
  estilo sólo trata la cinta.
- Lo que garantizan las clases VPG de las CFexpress: no se ha leído en la fuente que las define.
  Tampoco se ha leído el texto de la especificación SD: las cifras de cada clase se toman del libro
  blanco de la SD Association.
- Las tasas de cada variante de ProRes y el año de su lanzamiento; el DNxHR; la norma de compresión
  de los XAVC en MXF: no se han leído en fuente del fabricante.
- El reparto interno de los 80 bits de la palabra de código de tiempo y la norma SMPTE que lo fija;
  los identificadores únicos de material (UMID) y los metadatos de planificación: no leídos.
- La definición del 4K de cine (DCI) se da como oficio: la especificación de la DCI no se ha leído.
- La compresión, sus defectos y las tasas mínimas de la EBU, en el tema 9; el sonido y su
  sincronía, en el tema 6; el envío en directo, mochilas y *streaming*, en el tema 13; la cámara
  lenta y el trabajo multicámara, en el tema 15; el cuidado del equipo, las baterías y los partes de
  incidencias, en el tema 11; las imágenes sensibles y los derechos, en el tema 12; la protección de
  datos personales en el material, en el tema 10 del común.

## Trazabilidad

Todas las fuentes se leyeron el 24/09/2026.

| Fuente | Qué sostiene |
|---|---|
| *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004 | Código de tiempo como acuerdo y a cero al principio de la cinta (5.3.3, p. 81); una noticia por cinta, barras y revisión en el lugar (p. 82) |
| UIT-R BT.709-6 (puntos 2.2 y 2.4) y BT.2020-2 (cuadro 1) | Resoluciones HD y UHD y formato 16:9 |
| Sony, *PXW-Z200/HXR-NX800 Help Guide*, 5-060-574-13(1), 2024 | Protección (p. 31); tarjetas (pp. 67-68); extracción (p. 95); formateo (p. 96); tiempo restante, aviso de 5 minutos y número de clips (p. 97); relevo (p. 98); clips, nombre, duración máxima, bits de usuario, revisión, SD del mismo tipo (p. 99); pregrabación y código (p. 151); simultánea (p. 153); banderas (p. 160); *proxy* y carpetas (p. 161); *proxy* y cámara lenta (p. 162); *proxy* por trozos y ranura B (p. 163); FTPES (p. 196); códec de *streaming* (p. 202); botones de marca (p. 242); menú de código de tiempo y de bits de usuario (p. 251); nombre de clip y ficheros de gestión (p. 252); sincronización de código (p. 298); avisos (pp. 310-311); formatos, audio y cadencias (p. 336) |
| Sony, *Help Guide ILCE-1*: «File Format (movie)», «Notes on memory card» | XAVC HS y S-I; intracuadro y GOP largo; tarjetas: acceso, copia, fragmentación, formateo en la cámara, exFAT, LOCK, cuidado físico |
| Sony, ILCE-7SM3 (firmware 3.00 o posterior), «(Movie) Characteristics of each file format» | XAVC S y S-I en H.264, XAVC HS en H.265; 10 bits 4:2:2 para editar; tasas de ejemplo; edición de HEVC |
| Library of Congress, *Sustainability of Digital Formats*, fdd000013 (MXF) y fdd000389 (ProRes 422), revisión significativa 09-05-2024 | Véase «Documentos técnicos que el tema cita» |
| Avid, *Avid DNxHD Technology*, 2012 | Ídem |
| Panasonic, *AVC-Intra Frequently Asked Questions* (documento comercial sin fecha) | Ídem |
| SD Association, «Speed Class» (web, leída con extractor) | Clases de velocidad |
| SD Association, *Video Speed Class: The new capture protocol of SD 5.0*, libro blanco, febrero de 2016 (pp. 4-5; la tabla de la p. 4 es una figura, leída sobre la imagen) | Escritura mínima de cada clase; salvedades |
| Sony, *PXW-X400 Operating Instructions*, 4-587-873-13(1), 2015 («Specifications», p. 144) | Compresión y tasa del MPEG HD422 y HD420 y del XAVC-L 50 |
| Digital Preservation Coalition, *Digital Preservation Handbook*, «Fixity and checksums» | Suma de verificación y bloqueo de escritura |
| INCIBE, «Definiendo mi estrategia de copias de seguridad», 29-09-2021 (web, leída con extractor) | Regla 3-2-1 |

Oficio sin norma detrás, y así se declara: el paso de la cinta al fichero y las ventajas del disco y
la tarjeta; la distinción entre esencia, códec, contenedor, metadatos y proyecto; quién desarrolló
cada contenedor; el uso de cada patrón MXF; EDL, AAF y XML; el 4K de cine; el origen del 29,97 y del
*drop frame*; la notación del muestreo cromático; el *proxy* y el flujo *offline*-*online*; la
transformada del coseno; el audio sin comprimir en cámara; la tabla de intracuadro y GOP largo; las
tarjetas SxS, P2 y XDCAM y sus fabricantes; la elección de tarjeta por formato, salvo lo que cita la SD Association; el LTC y el VITC y
sus 80 bits; la elección del modo de código de tiempo; el uso de marcas y banderas; las formas de
ingesta y sus pasos; la copia con suma de verificación aplicada al cámara; la regla 3-2-1 aplicada a
la jornada; los niveles de RAID; la LTO; la lista de entrega; los riesgos del FTP sin cifrar; el
supuesto práctico. Es cálculo, y se puede rehacer: las relaciones de aspecto (3.840 ÷ 2.160 y
4.096 ÷ 2.160), los niveles por bit (2⁸ y 2¹⁰), la capacidad en minutos de una tarjeta, el paso de Mb/s a MB/s, los 32 bits
de ocho cifras hexadecimales y la resta de códigos de tiempo.
