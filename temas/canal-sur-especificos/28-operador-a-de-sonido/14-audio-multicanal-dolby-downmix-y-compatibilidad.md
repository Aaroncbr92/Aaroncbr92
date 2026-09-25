# Tema 14 del específico de Operador/a de Sonido · Audio multicanal, Dolby, 5.1, estéreo, mono, downmix y compatibilidad

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 14 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Recomendaciones técnicas: UIT-R BS.775 (sistema de sonido estereofónico multicanal), EBU Tech 3343 (guía de producción con R 128), UIT-R BS.1770 (medida de sonoridad), SMPTE RDD 19 (Dolby E con vídeo de más de 30 Hz, documento registrado, no norma). Documentación técnica publicada: EBU Technical Review 2009-Q1 (Dolby E y retardos en alta definición). Documentación de fabricante: Dolby (Dolby ED2; guía del Dolby Atmos Renderer) y RTW (correlación de fase). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | La vigente el 24/09/2026: UIT-R BS.775-4 (diciembre de 2022); EBU Tech 3343-2023 (versión 4, noviembre de 2023); UIT-R BS.1770-5 (noviembre de 2023); SMPTE RDD 19-2011. La guía del Dolby Atmos Renderer, en su versión 3.0 (2018) |
| **Extensión** | 11.000 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Internacional de
Telecomunicaciones (**UIT**, en inglés **ITU**) y su sector de radiocomunicaciones (**UIT-R**);
Unión Europea de Radiodifusión (**UER**, en inglés **EBU**, *European Broadcasting Union*), que
publica recomendaciones (**R**) y documentos técnicos (**Tech**); Sociedad de Ingenieros de Cine y
Televisión (**SMPTE**, *Society of Motion Picture and Television Engineers*) y sus documentos
registrados (**RDD**, *registered disclosure document*); Sociedad de Ingeniería de Audio (**AES**,
*Audio Engineering Society*), cuya norma **AES3** es el par de audio digital de dos canales;
interfaz digital serie de vídeo (**SDI**, *serial digital interface*); modulación por impulsos
codificados (**PCM**, *pulse code modulation*), el audio digital sin comprimir; televisión de alta
definición (**HDTV**); los canales del sistema envolvente: izquierdo (**L**, *left*), derecho
(**R**, *right*), central (**C**, *centre*), envolvente izquierdo (**LS**, *left surround*) y
envolvente derecho (**RS**, *right surround*), y el envolvente mono (**MS**, *mono surround*); el
canal de efectos de baja frecuencia (**LFE**, *low frequency effects*), que es el «.1» del 5.1; el
subgrave (*subwoofer*) y la gestión de graves (*bass management*); la mezcla reducida (*downmix*)
y la ampliada (*upmix*), y los dos métodos de reducción a dos canales: «sólo izquierdo / sólo
derecho» (**Lo/Ro**, *left only / right only*) y «izquierdo total / derecho total» (**Lt/Rt**,
*left total / right total*); la codificación de transporte **Dolby E** y su extensión **Dolby
ED2**; el sistema de emisión **Dolby Digital** (**AC-3**), el **Dolby Digital Plus** y el
**Dolby AC-4**, y el **Dolby TrueHD**, sin pérdidas; los metadatos del Dolby Digital *dialnorm*
(normalización de diálogo) y *dynrng* (rango dinámico), y su información ampliada del flujo
(**Extended BSI**, *extended bitstream information*); el sistema de sonido basado en objetos **Dolby
Atmos**, con su cama de canales (*bed*) y sus objetos; la estación de trabajo de audio digital
(**DAW**, *digital audio workstation*); la radiodifusión de vídeo digital (**DVB**, *Digital Video
Broadcasting*); unidad de sonoridad (**LU**, *loudness unit*) y unidades de sonoridad referidas a
la escala completa (**LUFS**); disco compacto (**CD**) y disco versátil digital (**DVD**), en
los nombres de los soportes DVD-Audio y Super Audio CD; grupo de expertos en imágenes en movimiento
(**MPEG**, *Moving Picture Experts Group*), que da nombre a una familia de codificadores; interfaz
digital de audio multicanal (**MADI**, *multichannel audio digital interface*); protocolo de
internet (**IP**). Los fabricantes se citan por su nombre comercial: Dolby
Laboratories y RTW.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 14):
>
> Audio multicanal, Dolby, 5.1, estéreo, mono, downmix y compatibilidad.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué recomendación de la UIT define el sistema 5.1 y cuál es su versión
vigente; qué significan las notaciones 3/2, 2/0 o 1/0 y las de tres cifras como 7.1.2 o 5.1.4;
cuáles son las seis señales del 5.1; a qué ángulos se colocan los altavoces frontales y los
envolventes; qué es el LFE, hasta qué frecuencia llega, con qué desplazamiento de nivel se graba y
por qué no es lo mismo que el subgrave; qué diferencia hay entre audio basado en canales y en
objetos; qué es la cama de Dolby Atmos y cuántos objetos admite su renderizador; qué es el Dolby E,
cuántos canales lleva y en qué soporte, para qué sirve y para qué no, qué retardo introduce y qué no
se le puede hacer a una señal codificada; qué añade el Dolby ED2; qué metadatos lleva el Dolby
Digital; cuáles son los coeficientes de downmix de la UIT a estéreo y a mono; en qué se diferencian
Lo/Ro y Lt/Rt y cuál recomienda la UER por defecto; por qué la sonoridad de un downmix no coincide
con la de la mezcla envolvente; qué dice la UER del upmix y qué pautas da la UIT para la conversión ascendente; qué exige la
compatibilidad descendente y qué métodos da la BS.775 para no dejar fuera los receptores existentes
(*simulcast* y matrices); con qué códecs llega al público el audio inmersivo.
En la aplicación práctica y en la prueba del puesto: colocar, calibrar y comprobar una escucha 5.1, LFE incluido; decidir
qué va al central y qué al LFE; comprobar que una mezcla envolvente sobrevive al estéreo y al mono;
pasar un 5.1 por un equipo de un solo par AES3; insertar una voz en off sobre un programa con Dolby
E; revisar los metadatos de una entrega.

<!-- indice -->

## Índice

- [Audio multicanal](#audio-multicanal)
  - [Qué es un sistema multicanal: la jerarquía compatible](#qué-es-un-sistema-multicanal-la-jerarquía-compatible)
  - [Cómo se nombra un formato](#cómo-se-nombra-un-formato)
  - [Canales frente a objetos](#canales-frente-a-objetos)
  - [La cama y los objetos de Dolby Atmos](#la-cama-y-los-objetos-de-dolby-atmos)
- [Dolby](#dolby)
  - [Qué problema resuelve el Dolby E](#qué-problema-resuelve-el-dolby-e)
  - [Tramas, banda de guarda y conmutación](#tramas-banda-de-guarda-y-conmutación)
  - [El retardo de un cuadro](#el-retardo-de-un-cuadro)
  - [Lo que no se le puede hacer a una señal Dolby E](#lo-que-no-se-le-puede-hacer-a-una-señal-dolby-e)
  - [Dolby E y Dolby Digital: los metadatos](#dolby-e-y-dolby-digital-los-metadatos)
  - [Dolby ED2: el Dolby E inmersivo](#dolby-ed2-el-dolby-e-inmersivo)
- [5.1](#51)
  - [Las seis señales](#las-seis-señales)
  - [La colocación de los altavoces](#la-colocación-de-los-altavoces)
  - [El canal LFE](#el-canal-lfe)
  - [El LFE no es el subgrave](#el-lfe-no-es-el-subgrave)
- [Estéreo](#estéreo)
  - [El estéreo dentro de la jerarquía](#el-estéreo-dentro-de-la-jerarquía)
  - [El estéreo en el control](#el-estéreo-en-el-control)
- [Mono](#mono)
  - [El mono y el envolvente mono](#el-mono-y-el-envolvente-mono)
  - [La suma a mono y la fase](#la-suma-a-mono-y-la-fase)
- [Downmix](#downmix)
  - [Qué es y dónde se hace](#qué-es-y-dónde-se-hace)
  - [Los coeficientes de la UIT](#los-coeficientes-de-la-uit)
  - [Lo/Ro y Lt/Rt](#loro-y-ltrt)
  - [Por qué la UER recomienda Lo/Ro](#por-qué-la-uer-recomienda-loro)
  - [El downmix y la sonoridad](#el-downmix-y-la-sonoridad)
  - [Los coeficientes en Dolby Digital](#los-coeficientes-en-dolby-digital)
  - [La saturación del downmix y el upmix](#la-saturación-del-downmix-y-el-upmix)
- [Compatibilidad](#compatibilidad)
  - [La compatibilidad descendente como requisito](#la-compatibilidad-descendente-como-requisito)
  - [Cómo se comprueba](#cómo-se-comprueba)
  - [Producir una señal multicanal compatible](#producir-una-señal-multicanal-compatible)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Audio multicanal

### Qué es un sistema multicanal: la jerarquía compatible

Audio multicanal es el que se produce, transporta y reproduce con más de dos canales para rodear
al oyente. La referencia internacional es la recomendación UIT-R BS.775, cuya versión vigente es
la BS.775-4, de diciembre de 2022, titulada **«Multichannel stereophonic sound system with and
without accompanying picture»** (sistema de sonido estereofónico multicanal con y sin imagen). Las
versiones −0 (1992), −1 (1994), −2 (2006) y −3 (2012) están sustituidas.

Su resumen dice lo que recomienda: **«one universal multichannel stereophonic sound system with
three front channels and two rear/side channels together with an optional low frequency effects
(LFE) channel»**. Es decir, un único sistema universal de tres canales delanteros y dos traseros o
laterales, con un canal de efectos de baja frecuencia opcional. Es el 5.1.

La BS.775 no nace como un formato aislado, sino como el techo de una escala. Entre sus
considerandos, que la televisión de alta definición **«should be capable of giving … compatibility
with two-channel stereophonic and monophonic listening»** (debe ser compatible con la escucha
estereofónica de dos canales y con la monofónica), y **«that a hierarchy of compatible sound
systems for broadcasting, cinema and recordings is useful for programme exchange and up- and
down-mixing»** (que una jerarquía de sistemas compatibles para radiodifusión, cine y grabaciones es
útil para el intercambio de programas y para las mezclas ampliadas y reducidas). Por eso el
enunciado junta en una línea el 5.1, el estéreo, el mono, el downmix y la compatibilidad: son los
peldaños de una misma escalera.

### Cómo se nombra un formato

La BS.775 usa una notación de dos cifras, **canales delanteros / canales traseros**. Sus palabras
clave son **«5.1, 2/0 channel format, 3/2 channel format»**, y su tabla 2 recorre los formatos
reducidos **«1/0; 2/0; 3/0; 2/1; 3/1; 2/2»**. Así, el mono es 1/0; el estéreo, 2/0; tres canales
delanteros sin traseros, 3/0; y el 5.1 completo es un 3/2 más el LFE.

| Notación UIT | Delanteros | Traseros o laterales | Qué es |
|---|---|---|---|
| 1/0 | 1 | 0 | Mono |
| 2/0 | 2 (L, R) | 0 | Estéreo |
| 3/0 | 3 (L, C, R) | 0 | Tres frontales |
| 2/1 | 2 | 1 (envolvente mono) | |
| 3/1 | 3 | 1 (envolvente mono) | |
| 2/2 | 2 | 2 | |
| 3/2 | 3 | 2 (LS, RS) | El 5.1 sin su LFE; con él, 5.1 |

La otra notación, la de uso corriente, cuenta canales con puntos: 2.0, 5.1, 7.1. Con los formatos
inmersivos, que añaden altavoces por encima del oyente, se le suma una tercera cifra, y se lee
siempre igual: canales del plano horizontal · canales de baja frecuencia · canales de altura. La
documentación de Dolby la emplea (una cama **«7.1.2»**). Esta lectura de las tres cifras es
convención de oficio, no una cifra de la BS.775.

| Formato | Horizontal | Baja frecuencia | Altura |
|---|---|---|---|
| 2.0 | 2 | — | — |
| 5.1 | 5 | 1 | — |
| 7.1 | 7 | 1 | — |
| 7.1.2 | 7 | 1 | 2 |
| 5.1.4 | 5 | 1 | 4 |

Aplicación práctica: una escucha 5.1.4 son cinco altavoces en el plano horizontal —tres delante y
dos envolventes—, un canal de baja frecuencia y cuatro altavoces de altura. Los cuatro últimos
están encima, no detrás; y son canales, no objetos (la diferencia es la del epígrafe siguiente).
Las configuraciones de más canales de la UIT están en otra recomendación, la UIT-R BS.2051, que la
BS.1770-5 cita al remitir a **«the channel configurations specified in Recommendation ITU-R
BS.2051»**; su contenido no se desarrolla aquí.

### Canales frente a objetos

En un formato basado en canales, cada señal está destinada a un altavoz concreto: la mezcla fija
qué sale por cada uno. En uno basado en objetos, cada sonido viaja con unos metadatos que dicen
dónde debe sonar, y es el reproductor el que calcula el reparto entre los altavoces de que
disponga.

| | Basado en CANALES | Basado en OBJETOS |
|---|---|---|
| Qué se manda | Una señal POR ALTAVOZ | Una señal MÁS SUS COORDENADAS |
| Quién decide dónde suena | El mezclador, al mezclar | El decodificador de cada sala, al reproducir |
| Si la sala tiene otro número de altavoces | Hay que hacer otra mezcla | La misma mezcla se adapta |

Una mezcla basada en objetos se reproduce en instalaciones muy distintas, de una sala de cine a
un equipo doméstico. No porque se degrade con gracia, sino porque el decodificador RECALCULA el
reparto con los altavoces que hay.

La UIT también mide ya este audio: la BS.1770-5 aplica su algoritmo de sonoridad, en su anexo 4,
a las **«object-based audio signals or combination of channel- and object-based audio signals»**
(señales de audio basado en objetos o combinación de audio basado en canales y en objetos). La
medida de la sonoridad es materia del tema 13.

### La cama y los objetos de Dolby Atmos

Dolby Atmos es el sistema de Dolby Laboratories que combina los dos enfoques. Su rasgo distintivo
frente a los formatos envolventes clásicos es el uso de objetos, que se sitúan y se mueven en el
espacio tridimensional, también por encima del oyente.

La cama (*bed*) responde a una idea práctica: una mezcla basada en objetos no renuncia del todo a
los canales. Lo que no se mueve —el ambiente, la música, a menudo el diálogo— se pone en una CAMA
de canales fijos, y sólo lo que tiene que viajar por la sala se hace objeto.

La guía del Dolby Atmos Renderer (versión 3.0 del programa, 2018) lo define así: **«Bed tracks
are audio tracks with bed material. In a basic Dolby Atmos setup, this is a 7.1.2 multichannel
track»** (las pistas de cama llevan material de cama; en una configuración básica de Dolby Atmos,
es una pista multicanal 7.1.2), y **«Object tracks are audio tracks with object audio»** (las
pistas de objeto llevan audio de objeto). Cada una se posiciona de un modo: **«Positioning for
beds is based on the width of the multichannel bed in the DAW. Positioning for objects is based on
Dolby Atmos metadata»** (la cama se posiciona por la anchura de la pista multicanal en la
estación de trabajo; los objetos, por los metadatos de Dolby Atmos).

Las cifras de esa guía:

| Dato | Guía del Dolby Atmos Renderer v3.0 |
|---|---|
| Cama de la configuración básica | **«a 7.1.2 multichannel track»**: siete horizontales, uno de baja frecuencia y dos de altura, diez canales |
| Objetos | **«up to 118 mono objects, or a combination of mono and stereo objects totaling up to 118 object channel paths»** |
| Entradas de la estación de trabajo | **«up to 128 input audio tracks»**; el Renderer admite 128 canales de entrada a 48 kHz y 64 a 96 kHz |
| Plantilla | **«one 7.1.2 bed and up to 118 mono objects»**, **«depending on the template»** |

La suma cuadra: los diez canales de una cama 7.1.2 más 118 objetos son 128 entradas (cálculo
sobre las cifras de la guía, trabajando a 48 kHz). No hay que confundir las dos cifras: 7.1.2 es la cama; 118, los
objetos. Las cifras son las de la versión 3.0 de la guía; no se ha comprobado si versiones
posteriores del renderizador las cambian, así que se estudian como «las de la guía del
Renderer», no como un máximo absoluto del sistema.

## Dolby

«Dolby» no es un formato, sino una familia de sistemas de Dolby Laboratories. En una instalación
de televisión conviven dos papeles distintos que no hay que mezclar: el Dolby E, para el
transporte interno en producción, y el Dolby Digital (AC-3), para la emisión al público. A ellos
se suman el Dolby ED2, extensión inmersiva del Dolby E, y el Dolby Atmos, ya visto.

### Qué problema resuelve el Dolby E

Cuál es el problema: una instalación de televisión transporta audio en pares AES3, dos canales
por par. Un 5.1 son seis canales: tres pares. Y en el momento en que hay que pasar por un equipo
que sólo lleva un par —un enlace, un servidor antiguo, una matriz— el 5.1 no cabe.

Qué hace el Dolby E: empaqueta hasta ocho canales de audio, con sus metadatos, DENTRO de un solo
par AES3, y lo hace troceado en fotogramas de vídeo, de modo que se puede editar y conmutar en los
cortes de imagen sin producir ruido.

La definición de la UER, en su *Technical Review* de 2009: **«Dolby E is a data-stream, designed
by Dolby Laboratories, which carries up to eight channels of digital audio within a standard
stereo channel (AES3), as well as transporting metadata which describes the audio and its
reproduction. It is a professional data-stream, designed for use within production and broadcast
infrastructures – but not for use as an emission codec or by consumers. It employs light data-rate
reduction, ensuring that multiple encode-decode cycles are possible»**. Es decir: un flujo de datos
profesional que lleva hasta ocho canales de audio digital en un canal estéreo normal AES3, con
metadatos que describen el audio y su reproducción; pensado para las infraestructuras de
producción y radiodifusión, no como códec de emisión ni para el consumidor; y con una reducción de
datos ligera, que permite varios ciclos de codificación y decodificación.

Cuántos ciclos: el documento SMPTE RDD 19-2011 lo describe como **«a method of reducing the data
rate of PCM (baseband) audio signals while preserving the subjective quality of the audio through
up to ten encode – decode cycles»** (conserva la calidad subjetiva a lo largo de hasta diez ciclos
de codificación y decodificación), y confirma que **«The data rate reduction ratio allows up to
eight audio signals to be carried in a single AES3 digital audio stream»**. El RDD 19 es un
documento registrado de la SMPTE, no una norma: así lo dice su portada.

Y ésa es su virtud y su límite: está pensado para PRODUCCIÓN y contribución, no para emisión al
público. Es una codificación de transporte interno. Lo que sale al aire va en el sistema de emisión
que corresponda.

| | Dolby E | Dolby Digital (AC-3) |
|---|---|---|
| Para qué | Producción y contribución | Emisión al público |
| Canales | Hasta 8 en un par AES3 | **«up to six»** |
| Reducción de datos | Ligera: conserva la calidad subjetiva hasta 10 ciclos | La fuente no la cuantifica |
| Metadatos | Describen el audio y su reproducción; lleva los del consumidor que usará el Dolby Digital | Los del consumidor |

### Tramas, banda de guarda y conmutación

La conmutación limpia se debe a cómo se organiza la señal. La *Technical Review* lo explica:
**«Dolby E divides audio into frames at a rate aligned with the associated video»** (divide el
audio en tramas a un ritmo alineado con el vídeo al que acompaña). **«Each frame is slightly
shorter than a video frame, allowing a guard band to be used … The switching point used by mixers
and routers falls in this guard band, allowing switching between video sources without the
corruption of the embedded Dolby E»**: cada trama es algo más corta que un cuadro de vídeo, y el
hueco que queda, la banda de guarda, es donde caen los puntos de conmutación de mezcladores y
matrices. Así se puede cortar entre fuentes de vídeo sin romper el Dolby E embebido. El RDD 19 lo
formula igual: **«The guard bands between blocks are co-located with the Vertical Interval Switch
points of the associated video signal»** (las bandas de guarda coinciden con los puntos de
conmutación del intervalo vertical del vídeo).

Una salvedad con el vídeo progresivo de 50 o 60 cuadros por segundo. Según el RDD 19, **«Dolby E
encoders generate data blocks that are synchronized with video frame rates of up to 30 frames per
second»**; con progresivo a 50 o 60, **«the Dolby E data stream may only be switched on a
Progressive frame … boundary that occurs during the Dolby E guard band intervals, or in other
words, on every second P Frame boundary»**. Es decir, sólo se puede conmutar en uno de cada dos
cuadros progresivos: en el que coincide con la banda de guarda.

### El retardo de un cuadro

Codificar y decodificar cuesta tiempo. La *Technical Review*: **«Dolby E encode and decode cycles
each incur a fixed delay of 1 video frame (e.g. 40 ms in a 25 Hz system)»**. Cada codificación y
cada decodificación añaden un retardo fijo de un cuadro de vídeo: 40 ms a 25 cuadros por segundo.
Un paso completo, codificar y decodificar, son dos cuadros (cálculo sobre la cifra de la fuente).

Para compensarlo, la misma fuente describe dos formas de entregar el audio codificado: **«In-Sync
Encoded»**, en sincronía con el vídeo, en cuyo caso **«The decode delay must be compensated for at
the decode site by the use of an equivalent video delay»** (el retardo de decodificación se
compensa donde se decodifica, con un retardo de vídeo equivalente), y **«Advanced (decode-compensated) – The encoded audio
appears one frame ahead of the video, meaning that after the decode delay, the audio is in
sync»**: adelantado un cuadro, para que tras el retardo del decodificador quede en sincronía.

Y un aviso que en la práctica produce desincronías: hay equipos **«Dolby-E-aware»** que
**«"helpfully" include a frame of video delay to compensate for the audio decoding delay. Such
devices include de-embedders, MPEG video encoders»**. Es decir, algunos desembebedores y
codificadores de vídeo retrasan el vídeo un cuadro por su cuenta para compensar la decodificación.
La fuente pone el ejemplo: si un desembebedor tiene activado su cuadro de retardo y además se usa un
retardo de cuadro aparte, **«the video will be double-delayed and hence out of sync with the
audio»**: el vídeo se retrasa dos veces y queda fuera de sincronía con el audio. Aplicación práctica: ante un programa con Dolby E que llega fuera de
sincronía por un cuadro, lo primero es saber si se entregó en sincronía o adelantado y qué equipos
de la cadena compensan por su cuenta. Si llegó en sincronía, la compensación corresponde al punto
donde se decodifica, retrasando el vídeo; si llegó adelantado, no hay que retrasar nada.

### Lo que no se le puede hacer a una señal Dolby E

Una señal Dolby E parece un par de audio, pero son datos. La *Technical Review* es tajante:
**«A Dolby E frame may not be split or modified in any way – such as gain adjustment, sample-rate
conversion or equalisation. An incomplete or corrupt frame will not reproduce the intended audio,
but will likely cause a mute for the duration of the frame or be interpreted as PCM audio, causing
a loud audible "splat" in the output»**.

| Qué no se hace sobre el par codificado | Qué pasa si se hace |
|---|---|
| Cambiar la ganancia | La trama se corrompe |
| Convertir la frecuencia de muestreo | La trama se corrompe |
| Ecualizar | La trama se corrompe |
| Partir una trama | La trama queda incompleta |
| Resultado de una trama incompleta o corrupta | Silencio durante la trama, o un chasquido fuerte si se interpreta como audio PCM |

Consecuencia para el operador: el par que lleva Dolby E no se abre en la mesa como si fuera audio,
ni se le pasa por un ecualizador o un conversor de muestreo. Cortar sí se puede, en la banda de
guarda; mezclar no. La fuente lo dice: **«while Dolby E's frame-synchronous nature allows cut
transitions without decoding, actions such as mixing audio and adding voiceovers requires careful
implementation of a decode-process-encode cycle»**. Aplicación práctica: para insertar una voz en
off sobre un programa que llega en Dolby E hay que decodificar, mezclar en PCM y volver a
codificar; y cada paso suma su cuadro de retardo.

### Dolby E y Dolby Digital: los metadatos

Los dos sistemas trabajan en cadena. La *Technical Review*: **«Dolby E is often used in
conjunction with Dolby Digital, which is a consumer data-stream, also carrying multiple channels
of audio (up to six) and associated metadata, and is used as the emission codec by many
broadcasters. The consumer metadata used in a Dolby Digital stream is carried by the Dolby E
stream … allowing metadata continuity from studio to home»**. El Dolby Digital es el flujo del
consumidor, con hasta seis canales y metadatos, y el códec de emisión de muchos radiodifusores; el
Dolby E transporta los metadatos que luego usará el Dolby Digital, de modo que no se pierden entre
el estudio y el hogar.

Qué metadatos. La Tech 3343 de la UER: **«in the Dolby AC-3 Metadata system, these parameters are
called dialnorm (dialogue normalisation), dynrng (dynamic range) and Centre/Surround Downmix
Level»**: la normalización de diálogo, el rango dinámico y los niveles de downmix del central y de
los envolventes. Estos últimos son los que el receptor usa para hacer la mezcla reducida
(epígrafe «Downmix»).

Y dos valores que deben poner en guardia: **«−27 (the factory default for dialnorm in the
Dolby-Digital system) or −31 (the lowest possible value in that system)»**. Un −27 es el valor de
fábrica y un −31 el mínimo del sistema; según la guía, los metadatos de sonoridad que indiquen
cualquiera de los dos **«are likely to raise special awareness, as chances are that Metadata have
either not been looked at or been abused for the programme to appear (much) louder when replayed at
the consumer's side»**: deben mirarse con especial atención, porque probablemente nadie los revisó
o se han manipulado para que el programa suene (mucho) más fuerte en casa. La guía recomienda
además **«to discard Loudness and Dynamic Range Control Metadata for external sources except where
the source can be fully trusted»**: desechar los metadatos de sonoridad y de control de rango
dinámico de fuentes externas salvo que sean plenamente fiables. La revisión de metadatos de
sonoridad se desarrolla en el tema 13.

### Dolby ED2: el Dolby E inmersivo

El Dolby E se queda corto para el audio inmersivo. El documento técnico de Dolby sobre el Dolby
ED2 lo reconoce: **«While Dolby E supports surround sound audio and the carriage of multiple
streams, it does not have the extensions necessary to carry Dolby Atmos audio, loudness
information, and other important metadata»** (no tiene las extensiones necesarias para llevar
audio Dolby Atmos, información de sonoridad y otros metadatos importantes).

La solución: **«Dolby ED2 is an extension to the Dolby E codec to support immersive audio»**.
Sus rasgos, según el mismo documento:

- **«Backward compatible with Dolby E pass-through and decoding products»**: compatible hacia
  atrás con los equipos que dejan pasar y decodifican Dolby E.
- **«Supports up to 16 audio channels with 8 channels carried per Dolby ED2 substream on a single
  AES3/SDI audio pair»**: hasta 16 canales, 8 por cada subflujo, cada uno en un par de audio AES3
  o SDI. Es decir, dos pares para los 16 (cálculo sobre las cifras de la fuente).

El Dolby ED2, como el Dolby E, no es el códec de emisión. El mismo documento: **«For emission,
Dolby ED2 can be transcoded into a next-generation audio format such as Dolby Digital Plus with
Dolby Atmos or Dolby AC-4 for efficient consumer delivery»** (para la emisión, se transcodifica a
un formato de audio de nueva generación, como Dolby Digital Plus con Dolby Atmos o Dolby AC-4).

La guía del Dolby Atmos Renderer da los códecs con los que la mezcla llega al consumidor
(**«Supported delivery codecs»**) y cómo conserva la compatibilidad con los decodificadores
antiguos:

| Códec de entrega | Qué dice la guía |
|---|---|
| Dolby TrueHD | Sin pérdidas: **«the spatially coded objects are losslessly delivered»**; lleva además una versión 7.1 y mezclas reducidas 5.1 y 2.0, compatibles con los decodificadores TrueHD antiguos |
| Dolby Digital Plus | Los objetos se renderizan a **«a backwards compatible 5.1 or 7.1 core mix»**, con metadatos para extraerlos; ese núcleo **«can be played back directly by older Dolby Digital Plus decoders»**. Es un proceso con pérdidas |

Y el downmix también está dentro: con núcleo 7.1, la capa 5.1 se genera **«using Dolby Pro Logic
IIx or Lo/Ro downmix rules»**, y el estéreo se obtiene de la capa 5.1 **«according to standard two-channel
downmixing equations»**. Es la misma jerarquía compatible de la BS.775, aplicada al audio
inmersivo: el receptor que no entiende los objetos reproduce el núcleo de canales.

## 5.1

### Las seis señales

Y los cinco canales del 5.1, que hay que saber nombrar: izquierdo, central, derecho, envolvente
izquierdo y envolvente derecho, más el LFE.

La BS.775 los nombra así en su punto 3 de lo que recomienda: **«five reference
recording/transmission signals for left (L), right (R), centre (C), channels for the front, and
left surround (LS) and right surround (RS) channels for the side/rear. Additionally the system may
include a low frequency effects signal …»**. Cinco señales de referencia de grabación y
transmisión —L, R y C delante; LS y RS a los lados o detrás— y, además, una señal opcional de
efectos de baja frecuencia. El «5» son los cinco canales de banda completa; el «.1», el LFE.

La BS.775 admite reducir los envolventes cuando lo imponen la capacidad de transmisión u otras
limitaciones (**«In circumstances where transmission capacity or other constraints apply»**):
**«the LS and RS signals can be combined with one (mono
surround, MS) or zero rear/side signals»**. Es decir, LS y RS pueden fundirse en un único
envolvente mono (MS), o suprimirse. De ahí salen los formatos 3/1 y 3/0 de la tabla del epígrafe
«Cómo se nombra un formato».

Y dos requisitos de su anexo 2 que definen el espíritu del sistema: **«Downward compatibility with
sound systems providing lower number of channels (down to stereophonic and monophonic sound
systems) shall be maintained»** (se mantendrá la compatibilidad descendente con los sistemas de
menos canales, hasta el estéreo y el mono) y **«Real-time mixing for live broadcast shall be
practicable»** (la mezcla en tiempo real para el directo será practicable).

### La colocación de los altavoces

La BS.775 fija la escucha de referencia en su punto 2 de lo que recomienda:

| Altavoces | Qué dice la BS.775-4 | En la práctica |
|---|---|---|
| Frontales izquierdo y derecho | **«placed at the extremities of an arc subtending 60° at the reference listening point»** | A ±30° del centro, vistos desde el punto de escucha |
| Central | Entre los dos frontales. Si la base frontal es recta y no un arco, **«it may be necessary to introduce compensating time delays in the signal feed of the centre loudspeaker»** | Al frente (0°); si está más cerca que los laterales, se le mete retardo |
| Envolventes | **«within the sectors from 100° to 120° from the centre front reference. Precise location is not necessary»** | Entre 100° y 120° a cada lado; no hace falta precisión |
| Distancia de los envolventes | **«no closer to the listener than the frontal loudspeakers, unless compensating time delay is introduced»** | No más cerca que los frontales, salvo compensación con retardo |
| Altura de los frontales | **«the acoustic centre of frontal loudspeakers should ideally be at a height approximately equal to that of the listener's ears. This implies an acoustically transparent screen»** | El centro acústico, a la altura de los oídos, lo que supone una pantalla que deja pasar el sonido |
| Central con pantalla no transparente | **«Where a non-acoustically transparent screen is used, the centre loudspeaker should be placed immediately above or below the picture»** | El central, justo encima o debajo de la imagen |
| Altura de los envolventes | **«The height of side/rear loudspeakers is less critical»** | Menos crítica que la de los frontales |
| Más de dos traseros (nota 4) | **«disposed symmetrically and at equal intervals on the arc which measures from 60° to 150°»** | Simétricos y equiespaciados entre 60° y 150° |
| Señal de más de dos traseros (nota 5) | **«the LS signal should be fed to each of the side/rear loudspeakers on the left side of the room and the RS signal should be fed to each of the side/rear loudspeakers on the right side of the room»**, reduciendo la ganancia para que la potencia total sea la de un solo altavoz | LS a todos los de la izquierda y RS a todos los de la derecha, con menos ganancia en cada uno |

Todos los ángulos se miden desde el frente del punto de escucha. Aplicación práctica: al montar
una escucha 5.1 en un control, los frontales a ±30°, el central al frente y a la misma distancia
—o con retardo si queda más cerca—, los envolventes entre 100° y 120° y nunca más cerca que los
frontales sin compensar, y todos calibrados en nivel. En un control de televisión, donde el
central no puede ir detrás de un monitor, se pone justo encima o debajo de la imagen.

### El canal LFE

El LFE es un canal de banda limitada. La BS.775 (puntos 4 y 5 de lo que recomienda) lo pide para
el intercambio internacional de programas (**«in the international exchange of audio or television
programmes»**): **«the LFE channel should be band-limited to its nominal frequency band (up to 120
Hz)»**, y para la emisión de televisión: **«broadcast of
any television programme that contains an LFE channel should not transmit any information on that
channel above the nominal 120 Hz cutoff frequency»**. Su anexo 7 precisa el margen: **«The LFE
channel should be capable of handling signals in the range of 20-120 Hz»**. El límite de 120 Hz
es, pues, cifra de la recomendación, no un orden de magnitud.

Su nivel se graba con un desplazamiento. El anexo 7: **«The LFE channel is recorded with a level
offset of −10 dB for the recording and exchange of multichannel sound programme material. This
offset is compensated for in the reproduction system, where the LFE loudspeaker has an acoustic
output (within its low frequency passband) of +10 dB with respect to the other channels»**. Se
graba 10 dB por debajo y la reproducción le devuelve esos 10 dB. La propia recomendación anota una
excepción: **«the music industry, such as DVD-Audio or Super Audio CD, is currently coding the LFE
channel such that zero offset gain is required on reproduction»** (en DVD-Audio o Super Audio CD
se codifica sin desplazamiento).

Para qué sirve. La BS.775 insiste en que es un complemento: **«The LFE channel should not,
however, be used for the entire low frequency content»**; **«The LFE channel is often not included
in a 2-channel downmix. The main channels must contain all the essential programme elements
necessary for the audience»**; **«it is better to think of it only as an enhancement – and
definitely not as an essential component of the audio programme»**. Y sobre la televisión: **«As
most television programmes do not need to convey very high levels of low frequency energy, in
general the LFE channel does not need to be employed»**. Nota de nombre: **«Although LFE stands
for "low frequency effects" in this Recommendation, in other standards it may be described as "low
frequency enhancement"»**.

Resumido: el LFE no lleva todo el grave del programa; a menudo no entra en el downmix a estéreo,
así que nada esencial puede ir sólo por él; y en televisión, en general, no hace falta usarlo.

La Tech 3343 añade dos datos que lo conectan con la sonoridad: **«the LFE channel of a 5.1
Surround Sound mix is excluded from the loudness measurement»** (el LFE no cuenta en la medida de
sonoridad), y, por el riesgo de ese canal y de su ganancia de +10 dB en banda, una solución es
**«not to use it at all ('5.0' Surround Sound) if there is no need for extra headroom in the low
frequency region»**: no usarlo, y quedarse en 5.0, si no hace falta margen adicional en graves.
Y añade: **«This is typically the case for the majority of broadcast content with the notable
exception of mainly action movies»** (es el caso de la mayoría de los contenidos de emisión, con la
notable excepción, sobre todo, de las películas de acción).

Cómo se calibra. El anexo 7 de la BS.775 da el procedimiento con ruido rosa: **«The pink noise test
signal is intended to be reproduced at an acoustic sound pressure level (within the LFE channel
< 120 Hz passband) of +10 dB relative to any of the other individual channels»**. Y avisa de una
trampa de medida: **«due to the limited bandwidth of the LFE channel, if the acoustic level produced
by the LFE pink noise is measured with a wideband sound pressure level meter, the reading will not
measure +10 dB with respect to the other channels. The acoustic level of the LFE channel should
measure +10 dB within its < 120 Hz bandwidth when measured with a frequency selective meter»**. Para
la radiodifusión, cuando los niveles de señal cumplen esas especificaciones (**«For broadcasting
applications where signal levels are compliant with these specifications»**): **«the level of LFE channel should be reproduced with positive offset gain of 10 dB
relative to the main channels on reproduction»**.

Aplicación práctica: al calibrar una escucha 5.1, si el sonómetro de banda ancha no marca +10 dB en
el LFE, no hay que subirlo hasta que lo marque; los +10 dB se miden dentro de su banda, por debajo
de 120 Hz, con un medidor selectivo en frecuencia.

### El LFE no es el subgrave

El LFE merece una precisión que casi nadie hace: no es «el altavoz de graves». Los graves de los
otros cinco canales no van por ahí: van por sus propios canales, y es el sistema de reproducción el
que decide si los redirige al subgrave.

La BS.775 lo aclara en el apéndice 1 de su anexo 7: **«There is often considerable
misunderstanding about the use of the ".1" in surround sound, and how it relates to
subwoofers»**. Y separa los conceptos: **«The purpose of a subwoofer is to extend to lower
frequencies the response of a loudspeaker»**; en las instalaciones domésticas se usa gestión de
graves (**«domestic installations, where bass management is used …»**), que desvía al subgrave los
graves de los canales principales. Del Dolby AC-3 dice: **«it has a limited bandwidth, of only 120
Hz, and it has 10 dB of gain applied on reproduction. The five normal channels in Dolby AC-3 are
full band-width»**.

El mismo apéndice avisa de un riesgo entre los dos sistemas Dolby: **«The frequency response of the
LFE channel in Dolby E is not the same as that of Dolby AC-3»**; el Dolby E admite en el LFE más
contenido de alta frecuencia del que pasa por el codificador AC-3, de modo que **«a wide-band signal
put into a Dolby E LFE channel will be low-pass filtered by the time it reaches the audience»** (una
señal de banda ancha metida en el LFE del Dolby E llegará al público filtrada paso bajo). Y con el
paso del Dolby E al PCM lineal, donde el canal del LFE es de banda completa, **«the scope for
incompatible LFE channel signals to be produced is even greater»**. Aplicación práctica: lo que se
mete en el LFE se limita en producción a su banda; que el Dolby E lo deje pasar no significa que
llegue a casa.

| | Canal LFE | Subgrave |
|---|---|---|
| Qué es | Un CANAL de la mezcla, con su propia señal | Un ALTAVOZ |
| Banda | Hasta 120 Hz | Extiende hacia abajo la respuesta de otro altavoz |
| Qué lleva | Efectos de baja frecuencia, como realce | El LFE y, con gestión de graves, los graves de los demás canales |

Por eso se llama «.1»: no es un sexto canal de banda completa, sino uno limitado a los graves.

## Estéreo

### El estéreo dentro de la jerarquía

El estéreo de dos canales, izquierdo y derecho, es el formato 2/0 de la BS.775. Es el peldaño que
la recomendación exige conservar: la HDTV debe ser compatible con la **«two-channel stereophonic
[listening]»**, y la compatibilidad descendente se mantiene **«down to stereophonic and monophonic
sound systems»**. En la disposición de referencia de la BS.775, la pareja frontal izquierda y
derecha está en los extremos de un arco de 60°, a ±30° del centro.

El estéreo importa por una razón práctica: aunque se produzca en 5.1, una parte del público oirá
el programa en dos canales. El estéreo que llega a ese oyente puede ser una mezcla estéreo hecha
aparte o un downmix del 5.1 hecho por su receptor; en el segundo caso, lo que oye depende de los
coeficientes y del método de downmix (epígrafe «Downmix»).

En un 5.1, el central lleva lo que en estéreo es el centro fantasma, la imagen que se forma entre
los dos altavoces cuando ambos reproducen la misma señal. Al bajar a estéreo, la BS.775 reparte el
central a los dos canales con un coeficiente de 0,7071 en cada uno (−3 dB), para que la imagen
central vuelva a formarse entre los dos altavoces. El reparto de los coeficientes es de la
recomendación; la explicación del centro fantasma, de oficio.

La captación estéreo (parejas de micrófonos y sus técnicas) es materia del tema 3.

### El estéreo en el control

Para comprobar un estéreo, la herramienta es el correlador de fase, que se explica en los temas 1 y
13. El fabricante de medidores RTW resume su uso: **«Mostly, phase correlation is used to determine
the mono compatibility of a stereo signal, but depending on where you use it, it can also reveal
other things, such as bad microphone placement»**. Su escala va **«from -1 (switched polarity) over
0 (unrelated) to 1 (identical)»**: en +1 los dos canales son idénticos; en 0 no guardan relación;
en −1 uno es el otro con la polaridad invertida. Como orientación de fabricante, no de norma,
**«Normal stereo mixes usually show correlation values between 0.3 and 0.7»**.

## Mono

### El mono y el envolvente mono

El mono es el formato 1/0 de la BS.775: un solo canal. Es el último peldaño de la jerarquía, y la
recomendación lo nombra expresamente: compatibilidad con la **«monophonic listening»** y
compatibilidad descendente **«down to stereophonic and monophonic sound systems»**.

La palabra «mono» aparece en el tema en dos sentidos que no hay que confundir:

| | Qué es | Formato |
|---|---|---|
| Mono (1/0) | Todo el programa en un único canal | 1/0 |
| Envolvente mono (MS) | Los dos envolventes, LS y RS, fundidos en una sola señal trasera, que se reproduce por los dos altavoces envolventes | 2/1, 3/1 |

La BS.775 (punto 3 de lo que recomienda) dice cómo se reproduce el envolvente mono: **«In the case
of mono surround, the MS signal is fed to both LS and RS loudspeakers»** (la señal MS se envía a los
dos altavoces, LS y RS). Una señal, dos altavoces. Y para obtenerla desde un 3/2, la tabla 2 la
calcula como S = 0,7071 LS + 0,7071 RS (epígrafe «Los coeficientes de la UIT»).

Para bajar un 5.1 a mono, la BS.775 da en su tabla 2 (anexo 4) los coeficientes, que leídos como
ecuación son: C = 0,7071 L + 0,7071 R + 1,0000 C + 0,5000 LS + 0,5000 RS. El central entra entero; los frontales izquierdo y derecho,
a 0,7071 (−3 dB); los envolventes, a 0,5 (−6 dB). Las equivalencias en decibelios son cálculo, no
texto de la recomendación: 20·log10(0,7071) ≈ −3 dB y 20·log10(0,5) ≈ −6 dB. El LFE no figura en
la ecuación.

### La suma a mono y la fase

Sumar a mono es sumar señales, y dos señales en contrafase se restan. Lo que en estéreo suena
ancho puede debilitarse o desaparecer en mono si los dos canales llevan componentes con la
polaridad invertida o muy desfasadas: en el correlador, las lecturas hacia −1 avisan de ello. La
física de la fase, la polaridad y el filtro en peine se desarrolla en el tema 1.

Aplicación práctica: antes de dar por buena una mezcla estéreo, se escucha en mono con el botón de
la mesa y se mira el correlador. Si al pulsar mono se pierde una voz, un instrumento o el ambiente,
hay un problema de fase o de polaridad (un cable con los hilos cruzados, dos micrófonos a
distancias que producen filtro en peine) que hay que resolver en origen, no con ecualización.

## Downmix

### Qué es y dónde se hace

El downmix es la mezcla reducida: obtener, a partir de un programa de más canales, uno de menos
—de 5.1 a estéreo o a mono, típicamente—. Se puede hacer en producción, como mezcla aparte, o
dejarlo al receptor del espectador, que lo calcula con unos coeficientes. La Tech 3343 recoge las
dos vías: el downmix se hace **«during production as a dedicated manual process to derive a
'custom' 2.0-Stereo signal and/or during transmission in the home receiver of the consumer
according to the Downmix Metadata sent within the bitstream»**. La BS.775 lo dice en su punto 7 de
lo que recomienda: capacidad de downmix **«if required, for reduction of the number of channels,
either prior to transmission or at the receiver, by employing the down-mixing equations given in
Table 2»** (si se necesita, antes de la transmisión o en el receptor, con las ecuaciones de su tabla
2). Y los coeficientes
pueden viajar como metadatos con el programa: en el sistema de Dolby AC-3, los **«Centre/Surround
Downmix Level»** del epígrafe «Dolby E y Dolby Digital: los metadatos».

### Los coeficientes de la UIT

La tabla 2 de la BS.775 (anexo 4), **«Downward mixing equations for 3/2 source material»**, da
los coeficientes para bajar un 3/2. La tabla es una matriz de coeficientes; aquí se escribe como
ecuación, sin los términos a 0,0000:

| Destino | Coeficientes de la BS.775-4, escritos como ecuación |
|---|---|
| Mono (1/0) | C = 0,7071 L + 0,7071 R + 1,0000 C + 0,5000 LS + 0,5000 RS |
| Estéreo (2/0) | L = 1,0000 L + 0,7071 C + 0,7071 LS; R = 1,0000 R + 0,7071 C + 0,7071 RS |
| Tres frontales (3/0) | L = 1,0000 L + 0,7071 LS; R = 1,0000 R + 0,7071 RS; C = 1,0000 C |
| Tres canales (2/1) | L = 1,0000 L + 0,7071 C; R = 1,0000 R + 0,7071 C; S = 0,7071 LS + 0,7071 RS |
| Cuatro canales (3/1) | L = 1,0000 L; R = 1,0000 R; C = 1,0000 C; S = 0,7071 LS + 0,7071 RS |
| Cuatro canales (2/2) | L = 1,0000 L + 0,7071 C; R = 1,0000 R + 0,7071 C; LS = 1,0000 LS; RS = 1,0000 RS |

Reglas que se leen en la tabla: el central, cuando no hay altavoz central (2/0, 2/1, 2/2), va a L y
a R a 0,7071; los envolventes, cuando no hay traseros (2/0, 3/0), van cada uno a su lado a 0,7071;
cuando hay un solo trasero (2/1, 3/1), se suman en la señal S, cada uno a 0,7071.
La recomendación advierte que el efecto total de estas ecuaciones **«will depend on other factors,
such as the panning equations and microphone characteristics»** (dependerá de otros factores, como
las leyes de panorámica y las características de los micrófonos).

Leída en decibelios (cálculo: 0,7071 ≈ −3 dB; 0,5 ≈ −6 dB): para el estéreo, cada frontal pasa
entero a su lado; el central va a los dos lados a −3 dB; cada envolvente, a su lado a −3 dB. El LFE
no aparece en ninguna ecuación, coherente con lo que dice la propia recomendación de que **«The LFE
channel is often not included in a 2-channel downmix»**.

La UER toma esos valores como punto de partida cuando faltan los metadatos. La Tech 3343: **«In
the case of missing or unreliable Downmix Metadata, a good starting point is to look at the
coefficients described in ITU-R BS.775-2: L, R front: 0 dB; C, LS, RS: −3 dB»**. La Tech 3343 cita
la edición −2 de la BS.775; los coeficientes a estéreo de la −4 vigente son los mismos de la tabla.

Aplicación práctica, con cálculo propio sobre los coeficientes: un diálogo que va sólo por el
central a un nivel dado llega a cada canal del downmix estéreo 3 dB más bajo; como sale por los dos
altavoces a la vez, en la escucha se recompone como imagen central.

### Lo/Ro y Lt/Rt

Hay dos maneras de bajar un multicanal a dos canales, y no son intercambiables. La Tech 3343:
**«There exist two different Downmix methods in a receiver: Lo/Ro (Left only/Right only) which
directly combines the channels according to the downmix coefficients, and Lt/Rt (Left total/Right
total) which applies ±90° phase shifting to a Mono-sum of the surround channels in order to
achieve better compatibility with matrix-surround playback systems (for example, Dolby
ProLogic)»**.

| Downmix | Qué hace | Para qué |
|---|---|---|
| Lo/Ro | Combina los canales DIRECTAMENTE, con los coeficientes de downmix | Un estéreo convencional |
| Lt/Rt | Suma a mono los envolventes y los introduce con un desplazamiento de fase de ±90° | Mejor compatibilidad con los sistemas de reproducción envolvente por MATRIZ, como el Dolby ProLogic |

La diferencia práctica: el Lo/Ro combina los canales directamente; el Lt/Rt se hace pensando en
los sistemas de reproducción envolvente por matriz. El funcionamiento interno de la matriz y de su
decodificador no se desarrolla aquí.

Aplicación práctica: si el destino es un sistema de reproducción envolvente por matriz, Lt/Rt; si
no, Lo/Ro, que es además el que la UER recomienda por defecto (epígrafe siguiente).

### Por qué la UER recomienda Lo/Ro

El Lt/Rt tiene un precio. La Tech 3343: **«Mainly due to the artefacts of Matrix-Surround systems,
an Lt/Rt-Downmix is even more unpredictable as far as the resulting Loudness Level is concerned.
Together with the general sonic alterations, this is the reason why the EBU recommends the Downmix
method Lo/Ro as the default setting for the relevant Metadata parameter ("Preferred Downmix
Method")»**.

Es decir: por los artefactos de los sistemas de matriz, la sonoridad de un Lt/Rt es todavía menos
predecible, y altera además el sonido. Por eso la UER recomienda Lo/Ro como valor por defecto del
metadato «método de downmix preferido».

### El downmix y la sonoridad

Un programa normalizado en 5.1 no queda necesariamente normalizado al bajarlo a estéreo. La Tech
3343 enumera de qué depende la sonoridad del downmix: **«The chosen Downmixing method (Lo/Ro or
Lt/Rt)»**; **«The actual downmix coefficients themselves»**; **«The programme content in the Centre
and surround channels»**; **«The correlation between the channels»**, y **«Potential
safety-limiting to avoid overload»**. Cinco factores: el método, los coeficientes, lo que lleven el central y los
envolventes, la correlación entre canales y la limitación de seguridad que se aplique para evitar
la saturación. Entre los coeficientes posibles, la guía menciona valores de +3, +1,5, 0, −1,5, −3,
−4,5 y −6 dB.

Y por qué la diferencia es sistemática en los envolventes: **«The weighting of the two surround
signals is +1.5 dB in the algorithm specified in ITU-R BS.1770, but the default downmix
coefficient for these signals is −3 dB! As a result, the difference in loudness terms regarding
the surround signals of the two mixes is 4.5 dB by default!»**. El medidor de sonoridad pesa los
envolventes +1,5 dB en la mezcla 5.1 (tema 13), y el downmix por defecto los baja 3 dB: entre las
dos mezclas, la contribución de los envolventes a la sonoridad difiere 4,5 dB. La guía señala
otra diferencia sistemática, la de la divergencia (el reparto de una señal del central hacia
izquierda y derecha): con divergencia total, cuando la señal suena igual por los tres altavoces
frontales, **«the Stereo-downmix of such a Surround-Sound mix can have an up to 3 LU higher
loudness level!»**: el downmix estéreo puede tener una sonoridad hasta 3 LU mayor que la mezcla
envolvente de la que sale.

Aplicación práctica: un programa 5.1 medido a −23 LUFS no garantiza que su downmix estéreo esté a
−23 LUFS; hay que medir también el downmix.

### Los coeficientes en Dolby Digital

En el Dolby Digital, los coeficientes de downmix viajan como metadatos, y su resolución ha
cambiado. La Tech 3343: **«Initially, when there was only one profile, the parameters were
coarser, with −3/−4.5/−6 dB for the Centre»**, y valores también gruesos —entre ellos −3 y −6 dB—
para los envolventes. **«Now, Extended Bitstream Information (Extended BSI) provides the finer
intermediate steps …; also DVB TS 101 154 downmix coefficients offer the same resolution»**: la
información ampliada del flujo (Extended BSI) permite pasos intermedios más finos, y los
coeficientes de la especificación DVB TS 101 154 ofrecen la misma resolución. Pero los
decodificadores antiguos **«would fall back to the fewer and coarser coefficients of profile
1»**: vuelven a los coeficientes gruesos del primer perfil. El mismo programa, por tanto, puede
bajar a estéreo de forma distinta según el receptor.

### La saturación del downmix y el upmix

Al sumar canales, el downmix puede saturar. La Tech 3343: **«Care should also be taken to avoid
overload of the downmixed signal. This can be achieved with a dynamics processor upstream. Static
scaling (overall level reduction) should be avoided»**. Se evita con un procesador de dinámica
antes del downmix, no bajando el nivel de todo de forma fija.

El camino inverso, el upmix, genera un multicanal a partir de un programa de menos canales (de
estéreo a 5.1, por ejemplo). La UER le pone un límite claro: **«An Upmix should never replace an
original discrete multichannel audio mix, though»**. Un upmix nunca debe sustituir a una mezcla
multicanal discreta original.

La BS.775 también prevé la conversión ascendente (punto 8 de lo que recomienda), **«either prior to
transmission or at the receiver»**, con las técnicas de su anexo 5, que la define como necesaria
cuando el número de canales de producción es menor que el de reproducción (**«A typical example is
a 2-channel stereo programme (2/0) that is to be presented over a 3/2 reproduction system»**). Sus
pautas:

| Caso | Pauta del anexo 5 de la BS.775-4 |
|---|---|
| Mono con tres frontales | **«the mono signal should be presented over the centre loudspeaker only»** |
| Mono con sólo dos frontales | Por el izquierdo y el derecho **«with an attenuation of 3 dB»** |
| Estéreo con tres frontales | L y R **«respectively over the left and right loudspeakers only»**: el central no se usa |
| Programa sin señal envolvente | **«surround loudspeakers should not be activated»** |
| Una señal envolvente por varios altavoces | Decorrelación entre ellos y atenuación, para igualar el nivel de un solo altavoz frontal |
| Canal de datos | Se transmite periódicamente información del modo de transmisión (número y tipo de canales), necesaria para la conversión en los receptores |

Las pautas son una referencia para quien produce: **«These guidelines do not exclude the
possibility, for receiver manufacturers, of the implementation of more sophisticated
techniques»** (no impiden que los fabricantes de receptores apliquen técnicas más elaboradas).

## Compatibilidad

### La compatibilidad descendente como requisito

Compatibilidad, en este tema, es que un programa hecho con más canales siga funcionando cuando se
escucha con menos. En la BS.775 no es una recomendación blanda: su anexo 2 dice que la
compatibilidad descendente **«shall be maintained»**, hasta el estéreo y el mono. Y la jerarquía de
sistemas compatibles es, según sus considerandos, lo que permite el intercambio de programas y las
mezclas ampliadas y reducidas.

El punto 6 de lo que recomienda pide **«compatibility, if required, with existing and low cost
receivers by using one of the methods given in Annex 3»**. El anexo 3 da esos métodos:

| Problema | Método del anexo 3 | Ventaja o condición |
|---|---|---|
| Un servicio 2/0 existente pasa a 3/2 sin dejar fuera los receptores existentes | *Simulcast*: se sigue emitiendo el servicio 2/0 y se añade el 3/2 (**«simulcasting operation»**) | **«the existing 2/0 service could be discontinued at some point in the future»** |
| El mismo caso | Matrices de compatibilidad (**«compatibility matrices»**): los canales izquierdo y derecho existentes llevan las señales compatibles A y B, y canales adicionales llevan las señales T, Q1 y Q2 | **«less additional data capacity is required to add the new service»** |
| Receptores de bajo coste | Con la matriz, el receptor sólo necesita los canales A y B, como en un 2/0 | |
| Receptores de bajo coste | En el sistema 3/2 discreto, combinar las señales con las ecuaciones del anexo 4 (la tabla 2); con codificación de baja velocidad, el downmix puede hacerse antes de la síntesis del decodificador, donde está el grueso de la complejidad | |

Hay compatibilidades en tres planos, y cada una tiene su herramienta:

| Plano | Qué se comprueba | Con qué |
|---|---|---|
| Canales | Que el 5.1 sobreviva al estéreo y el estéreo al mono | Downmix, escucha en estéreo y en mono, correlador |
| Sistemas de transporte | Que la señal atraviese la cadena sin romperse | Dolby E en un par AES3; en inmersivo, Dolby ED2, compatible hacia atrás con los equipos Dolby E |
| Receptores | Que cada receptor reproduzca lo previsto | Metadatos de downmix y sonoridad correctos; tener en cuenta que un decodificador antiguo usa los coeficientes gruesos del primer perfil |

### Cómo se comprueba

La comprobación es de escucha y de medida. RTW describe su correlador multicanal como **«a very
useful tool when you work with surround sound and wanting to make sure that your surround mix also
sounds great when down mixed to stereo or even mono»**: sirve para asegurarse de que la mezcla
envolvente suena bien también reducida a estéreo o a mono. En estéreo, el correlador de fase
convencional (epígrafe «El estéreo en el control»).

Y la sonoridad se mide en cada versión que se entregue, porque la de la mezcla 5.1 no garantiza la
del downmix (epígrafe «El downmix y la sonoridad»).

### Producir una señal multicanal compatible

Los requisitos de oficio de una producción multicanal, ordenados, con lo que la fuente respalda:

1. Monitorización correcta. No se puede mezclar en 5.1 sin cinco altavoces bien colocados y
   calibrados en nivel. La colocación es la de la BS.775 (epígrafe «La colocación de los
   altavoces»).
2. Decidir qué va al central. En televisión, el diálogo. Un central mal usado descoloca todo lo
   demás.
3. Gestionar el LFE con criterio. Nada esencial va sólo por el LFE, porque a menudo no entra en el
   downmix; en televisión, en general, no hace falta; y si no se necesita margen extra en graves,
   la UER admite prescindir de él y quedarse en 5.0.
4. Comprobar el downmix. La mayoría del público oirá la mezcla en estéreo o en una barra, así que
   la mezcla tiene que sobrevivir a la reducción. Se escucha en estéreo y en mono, se mira el
   correlador y se mide la sonoridad del downmix.
5. Cuidar los metadatos. La normalización de diálogo, el rango dinámico, los niveles de downmix
   del central y los envolventes y el método de downmix preferido viajan como metadatos; la UER
   recomienda Lo/Ro por defecto, y los valores −27 y −31 de *dialnorm* piden revisión.
6. Respetar el transporte. Si la señal va en Dolby E, no se toca su ganancia, su muestreo ni su
   ecualización; para mezclar hay que decodificar y volver a codificar, y cada paso suma un cuadro
   de retardo que hay que compensar una sola vez.
7. No sustituir el original. Un upmix nunca reemplaza a una mezcla multicanal discreta original.

## Recomendaciones técnicas que el tema cita

- UIT-R BS.775-4 (12/2022), *Multichannel stereophonic sound system with and without accompanying
  picture*.
- UIT-R BS.1770-5 (11/2023), *Algorithms to measure audio programme loudness and true-peak audio
  level*.
- EBU Tech 3343-2023 (versión 4, noviembre de 2023), *Guidelines for Production of Programmes in
  accordance with EBU R 128*.
- SMPTE RDD 19-2011, *Guidelines on the Use of Dolby E with Video Signals at Frame Rates Higher than
  30 Hz* (documento registrado, no norma).
- Citadas sin desarrollar: UIT-R BS.2051 (configuraciones de más canales), UIT-R BS.2127
  (renderizador ADM de la UIT) y DVB TS 101 154 (coeficientes de downmix).

## Lo que este tema no da, y dónde está

- La UIT-R BS.2051 (configuraciones de canales avanzadas, con altura) y la UIT-R BS.2127, que
  especifica el renderizador ADM de la UIT (**«ITU-R ADM Renderer (IAR)»**): no se han leído; sólo
  consta su existencia por la cita de la BS.1770-5. La lectura de las tres cifras (7.1.2, 5.1.4) se da como convención de oficio.
- Los modos de cuantificación del Dolby E (16, 20 o 24 bits) y el número de canales en cada uno:
  sólo se encontraron en fuentes de terceros, no en documentación de Dolby; no se dan.
- Las cifras de Dolby Atmos (cama 7.1.2, 118 objetos, 128 entradas) son las de la guía del
  Renderer versión 3.0 (2018); no se ha comprobado si versiones posteriores las cambian.
- Los coeficientes internos de la matriz del Lt/Rt y del decodificador (por ejemplo, Dolby
  ProLogic): no se han leído en su especificación; el tema da sólo lo que dice la Tech 3343.
- La lista completa de valores de coeficientes de downmix de la Tech 3343 y de los perfiles de
  Dolby Digital: el texto extraído de la guía pierde un símbolo al final de cada serie; el tema da
  sólo los valores legibles.
- La especificación DVB TS 101 154: citada por la Tech 3343, no leída.
- Las especificaciones de Dolby Digital Plus, Dolby AC-4 y Dolby TrueHD (canales, velocidades,
  metadatos) y las normas de emisión que los recogen: el tema sólo da lo que dicen de ellos el
  documento del Dolby ED2 y la guía del Renderer; no se han leído en su especificación.
- Las ecuaciones de la tabla 1 del anexo 3 de la BS.775 (codificación y decodificación de las
  matrices de compatibilidad): el tema da el método, no los coeficientes.
- El sistema de emisión de CSRTV (si emite en estéreo o en 5.1, con qué códec y con qué metadatos)
  y sus criterios internos de entrega multicanal: no constan en un documento publicado localizado.
- La fase, la polaridad y el filtro en peine, en el tema 1; la captación estéreo con parejas de
  micrófonos, en el tema 3; los medidores de sonoridad y de correlación, la ponderación de canales y
  los metadatos de sonoridad, en el tema 13; el transporte AES3, SDI embebido, MADI y Dante, en el
  tema 11; el audio sobre IP y la sincronía, en el tema 15.

## Trazabilidad

Fuentes leídas el 25/09/2026 (redacción, a través del material de investigación del bloque) y
releídas en el documento original el 25/09/2026 (verificación); las recomendaciones, en su versión
vigente ese día (BS.775-4 y BS.1770-5, «In force» en la página de la UIT).

| Fuente | Qué sostiene |
|---|---|
| UIT-R BS.775-4 (12/2022), *Multichannel stereophonic sound system with and without accompanying picture* | Sistema universal 3/2 con LFE opcional; compatibilidad con estéreo y mono; jerarquía de sistemas compatibles; notación 3/2, 2/0 y formatos de la tabla 2; las cinco señales y el LFE; envolvente mono; requisitos de compatibilidad descendente y mezcla en tiempo real (anexo 2); colocación de altavoces (±30°, 100°-120°, distancia, altura, retardo del central, 60°-150°); LFE hasta 120 Hz, 20-120 Hz, −10 dB de grabación y +10 dB de reproducción, excepción musical, realce y no componente esencial, a menudo fuera del downmix, innecesario en general en televisión, «effects» o «enhancement» (anexo 7); LFE frente a subgrave y gestión de graves; AC-3 con LFE de 120 Hz y cinco canales de banda completa; coeficientes de downmix a 1/0, 2/0, 3/0, 2/1, 3/1 y 2/2 (tabla 2, anexo 4) y su dependencia de otros factores; pantalla no transparente, central encima o debajo de la imagen y altura de los envolventes (punto 2); envolvente mono a LS y RS (punto 3); señal de más de dos traseros (nota 5); compatibilidad con receptores existentes y de bajo coste: *simulcast* y matrices (punto 6, anexo 3); downmix antes de la transmisión o en el receptor (punto 7); conversión ascendente y sus pautas (punto 8, anexo 5); calibración del LFE con medidor selectivo y +10 dB en emisión (anexo 7); LFE de Dolby E frente a AC-3 y PCM lineal (apéndice 1 del anexo 7, § 6); intercambio internacional como ámbito del límite de 120 Hz; condición de capacidad para el envolvente mono |
| UIT-R BS.1770-5 (11/2023), *Algorithms to measure audio programme loudness and true-peak audio level* | Remisión a la BS.2051 para más canales; medida de audio basado en objetos (anexo 4); cita de la BS.2127 (renderizador ADM de la UIT, apéndice 1 del anexo 4) |
| EBU Tech 3343-2023 (V4, noviembre de 2023), *Guidelines for Production of Programmes in accordance with EBU R 128* | LFE excluido de la medida de sonoridad y opción 5.0, típica de la emisión salvo películas de acción (§ 4.2); metadatos AC-3 *dialnorm*, *dynrng* y niveles de downmix, −27 y −31 y su motivo, descarte de metadatos externos (§ 6); downmix en producción o en el receptor; coeficientes por defecto; Lo/Ro y Lt/Rt con ±90°; preferencia Lo/Ro; factores de la sonoridad del downmix; +1,5 frente a −3 dB y 4,5 dB; hasta 3 LU con divergencia total; perfiles de Dolby Digital, Extended BSI, DVB TS 101 154 y decodificadores antiguos; saturación del downmix (§ 7.1); upmix (§ 7.2) |
| SMPTE RDD 19-2011, *Guidelines on the Use of Dolby E with Video Signals at Frame Rates Higher than 30 Hz* (documento registrado, «NOT a Standard») | Hasta diez ciclos; hasta ocho señales en un AES3; bandas de guarda en los puntos de conmutación del intervalo vertical; sincronía con vídeo hasta 30 cuadros; conmutación cada dos cuadros progresivos a 50/60 |
| EBU Technical Review 2009-Q1, R. De Pomerai (BBC), «HD production · audio delays» | Definición del Dolby E (ocho canales en AES3, metadatos, producción y no emisión, reducción ligera); relación con Dolby Digital (hasta seis canales, emisión, continuidad de metadatos); tramas alineadas con el vídeo y banda de guarda; tramas no modificables y sus efectos; retardo de un cuadro (40 ms a 25 Hz); entrega en sincronía (compensada con retardo de vídeo donde se decodifica) y adelantada; equipos que compensan por su cuenta y doble retardo del vídeo; mezcla con ciclo decodificar-procesar-codificar |
| Dolby, *Technology Brief · Dolby ED2 · Next Generation Audio Mezzanine Codec* (sin fecha) | Límites del Dolby E; Dolby ED2 como extensión inmersiva; compatibilidad hacia atrás; 16 canales, 8 por subflujo en un par AES3/SDI; transcodificación a Dolby Digital Plus con Dolby Atmos o Dolby AC-4 para la emisión |
| Dolby, *Dolby Atmos Renderer Guide*, versión 3.0 del programa (2-VIII-2018) | Pistas de cama y de objeto; cama 7.1.2 de la configuración básica; 118 objetos; 128 entradas (64 a 96 kHz); plantilla; posicionamiento de cama y de objetos; códecs de entrega (Dolby TrueHD y Dolby Digital Plus), núcleo compatible y reglas de downmix Pro Logic IIx o Lo/Ro |
| RTW, «Focus: The Multi Correlator», T. Valter (9-VIII-2019) | Uso del correlador de fase y del correlador multicanal; escala de −1 a +1; valores habituales de 0,3 a 0,7 (orientación de fabricante) |

Oficio sin norma detrás, y así se declara: la notación de tres cifras y su lectura; la
diferencia entre audio basado en canales y en objetos (tabla) y que el decodificador recalcula el
reparto; el rasgo distintivo de Dolby Atmos; la idea de cama frente a objeto; el problema que
resuelve el Dolby E con los pares AES3 y los equipos de un solo par; «transporte interno»; que el
par con Dolby E no se abre en la mesa; que el LFE se llama «.1» por no ser de banda completa; los
nombres de los cinco canales en castellano; el centro fantasma; la escucha en mono con el botón de
la mesa y las causas de un fallo de fase; los tres planos de la compatibilidad; los siete requisitos de producción, salvo en lo
que remiten a la BS.775 y a la Tech 3343. Es cálculo, y se puede rehacer: 0,7071 ≈ −3 dB y 0,5 ≈ −6 dB; 10 + 118 =
128; dos cuadros de retardo por ciclo completo de Dolby E; dos pares para los 16 canales del Dolby
ED2; el diálogo del central a −3 dB en cada canal del downmix.
