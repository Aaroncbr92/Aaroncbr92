# Tema 13 del específico de Cámara Operador · Producción móvil y transmisión: mochilas, enlaces, *streaming*, señales IP y coordinación con control

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Cámara Operador · punto 13 |
| **Sirve para** | Puesto 2.8, Cámara Operador (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Sin norma jurídica. Lo propio de la casa: *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, 1.ª ed., marzo de 2004) y Contrato-programa 2024-2026 entre el Consejo de Gobierno de la Junta de Andalucía y la RTVA. Normas técnicas: SMPTE ST 2110-10:2022, ST 2110-20:2022 y ST 2110-30:2025; Recomendación UIT-R SNG.770-2 (01/2012). Especificaciones y documentación técnica: AMWA NMOS; SRT (repositorio de referencia e *Internet-Draft* draft-sharabayko-srt-01); documentación de NDI. Norma europea ETSI EN 300 744 V1.6.2 (2015-10), sólo su cláusula 4.1. RFC 8216 (HLS, informativa) y especificación de RTMP de Adobe (2012). Documentación de fabricante: ficha web de la mochila LiveU LU800, manual en español de los mezcladores ATEM de Blackmagic Design (diciembre de 2024), libro blanco sobre COFDM y ficha del transmisor Sapphire-BTX de Domo Broadcast Systems, y ayuda de YouTube sobre emisión con codificador. Lo demás, oficio |
| **Redacción que se estudia** | Las normas SMPTE en las ediciones citadas, vigentes el 24/09/2026 según la biblioteca de la SMPTE; UIT-R SNG.770-2 en su edición de enero de 2012; las especificaciones y fichas web, en la fecha en que se leyeron (24/09/2026); el Libro de estilo en su primera edición (marzo de 2004), que es la leída |
| **Extensión** | 8.900 palabras aproximadamente |

<!-- /portada -->

Siglas que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Canal Sur Televisión, que el Libro de
estilo abrevia **CSTV**; protocolo de Internet (**IP**); red inalámbrica local (**wifi**); tarjeta de abonado de telefonía
móvil (**SIM**, *subscriber identity module*); redes móviles de quinta y cuarta generación
(**5G/4G**); resolución de unos 4.000 píxeles horizontales (**4K**, que la ficha escribe «4Kp60»
para 60 imágenes por segundo en progresivo);
protocolo de transferencia de ficheros (**FTP**, *file transfer protocol*); codificación de vídeo
de alta eficiencia (**HEVC**, *high efficiency video coding*, también H.265) y codificación de vídeo
avanzada (**AVC**, *advanced video coding*, también H.264); alto rango dinámico (**HDR**, *high
dynamic range*); unidad móvil (**UM**); unidad de control de cámara (**CCU**, *camera control
unit*); cámara panorámica-inclinable-zoom (**PTZ**, *pan-tilt-zoom*); interfaz digital serie
(**SDI**, *serial digital interface*); retorno de programa sin la propia fuente (**N-1**);
periodismo electrónico por satélite (**SNG**, *satellite news gathering*) y su versión digital
(**DSNG**); acceso por fibra hasta el hogar (**FTTH**, *fiber to the home*); Sector de
Radiocomunicaciones de la Unión Internacional de Telecomunicaciones (**UIT-R**); Society of Motion
Picture and Television Engineers (**SMPTE**); Audio Engineering Society (**AES**), cuya norma de
audio sobre IP es la **AES67**; Advanced Media Workflow Association (**AMWA**), que publica las
especificaciones **NMOS** (*Networked Media Open Specifications*, nombre de familia; el tema cita
su definición); Video Services Forum (**VSF**); Internet Engineering Task Force (**IETF**), que
publica los borradores *Internet-Draft* y las normas definitivas de Internet, las **RFC**
(*Request for Comments*); protocolo de tiempo real (**RTP**, *real-time transport
protocol*); protocolo de datagramas de usuario (**UDP**, *user datagram protocol*) y protocolo de
control de transmisión (**TCP**, *transmission control protocol*); protocolo de descripción de
sesión (**SDP**, *session description protocol*); protocolo de tiempo de precisión (**PTP**,
*precision time protocol*), definido en la norma **IEEE 1588** del Institute of Electrical and
Electronics Engineers (**IEEE**); modulación por impulsos codificados (**PCM**, *pulse-code
modulation*), el audio digital sin comprimir; petición automática de repetición (**ARQ**,
*automatic repeat request*); norma de cifrado avanzado (**AES** en criptografía, *advanced
encryption standard*: no confundir con la Audio Engineering Society); transporte seguro y fiable
(**SRT**, *secure reliable transport*); interfaz de dispositivos en red (**NDI**, *network device
interface*); descubrimiento por DNS de multidifusión (**mDNS**, *multicast domain name system*);
servicio de vídeo por Internet directo al usuario (**OTT**, *over the top*); imágenes por segundo
(**fps**, *frames per second*) y milisegundo (**ms**); megabit por segundo (**Mbps**);
multiplexación por división en frecuencias ortogonales (**OFDM**, *orthogonal frequency division
multiplexing*) y su versión codificada (**COFDM**, *coded*…); European Telecommunications Standards
Institute (**ETSI**); televisión digital terrestre del proyecto Digital Video Broadcasting (**DVB-T**,
norma ETSI EN 300 744); localizador uniforme de recursos (**URL**, *uniform resource locator*), la
dirección de un servidor; protocolo de mensajería en tiempo real (**RTMP**, *real time messaging
protocol*) y su versión segura (**RTMPS**), cifrada con seguridad de la capa de transporte
(**TLS/SSL**, *transport layer security* / *secure sockets layer*); *streaming* en directo por HTTP
(**HLS**, *HTTP live streaming*), donde **HTTP** es el protocolo de transferencia de hipertexto de la
web.

Los rótulos de panel y de menú se escriben tal como los imprime el fabricante (***CUT***,
***CALL***): son rótulos de la máquina, no siglas.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.8, punto 13):
>
> Producción móvil y transmisión: mochilas, enlaces, streaming, señales IP y coordinación con
> control.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué es una mochila de transmisión y por qué introduce retardo; qué
promete y qué no promete; por qué vías se conecta; en qué se diferencian el directo y el envío de
ficheros; qué vías de enlace hay para sacar la señal de una localización y qué ventaja y qué límite
tiene cada una; qué dice la UIT-R del DSNG; qué modulación usa el enlace inalámbrico de cámara y por qué; qué es
el *streaming* y en qué se distingue de la descarga y de la descarga progresiva; qué datos pide una
plataforma para emitir (URL y clave), qué son RTMP y HLS y cuál tiene más latencia; qué es SRT y si
es una norma; qué es la familia SMPTE ST 2110,
qué parte transporta el vídeo, cuál el audio y cuál la sincronía; qué es PTP; qué tamaño de paquete
fija ST 2110-10 y si admite excepción; qué es NMOS y cuál de
sus especificaciones lleva el piloto; qué es NDI; qué es la contribución y qué la distribución;
cuántos milisegundos son dos imágenes a 25 fps; qué es un retorno N-1; quién forma, según el Libro
de estilo de Canal Sur, el equipo que prepara un directo y a quién se comunica un retraso. En la
prueba práctica: preparar y probar un directo con mochila, o explicar qué comprobar con el control
antes de salir en antena.

<!-- indice -->

## Índice

- [Producción móvil y transmisión](#producción-móvil-y-transmisión)
  - [Directo o diferido: la distinción que ordena el tema](#directo-o-diferido-la-distinción-que-ordena-el-tema)
  - [Qué pide la casa: producción prevé, el equipo se comunica](#qué-pide-la-casa-producción-prevé-el-equipo-se-comunica)
- [Mochilas](#mochilas)
  - [Qué es una mochila de transmisión](#qué-es-una-mochila-de-transmisión)
  - [Lo que una mochila no promete](#lo-que-una-mochila-no-promete)
  - [Por dónde se conecta una mochila](#por-dónde-se-conecta-una-mochila)
  - [Un ejemplo documentado: la LiveU LU800](#un-ejemplo-documentado-la-liveu-lu800)
  - [El retardo de la mochila y cómo se trabaja con él](#el-retardo-de-la-mochila-y-cómo-se-trabaja-con-él)
- [Enlaces](#enlaces)
  - [Las vías de la contribución](#las-vías-de-la-contribución)
  - [Lo que la UIT-R pide al equipo de satélite](#lo-que-la-uit-r-pide-al-equipo-de-satélite)
  - [Contribución, distribución y control central](#contribución-distribución-y-control-central)
  - [La unidad móvil como punto de enlace](#la-unidad-móvil-como-punto-de-enlace)
  - [El enlace inalámbrico de cámara](#el-enlace-inalámbrico-de-cámara)
- [*Streaming*](#streaming)
  - [Qué es el *streaming*](#qué-es-el-streaming)
  - [Dos usos del *streaming*: contribuir y distribuir](#dos-usos-del-streaming-contribuir-y-distribuir)
  - [Emitir hacia una plataforma: URL, clave, RTMP y HLS](#emitir-hacia-una-plataforma-url-clave-rtmp-y-hls)
  - [SRT, un protocolo de contribución por Internet](#srt-un-protocolo-de-contribución-por-internet)
  - [El *streaming* en Canal Sur: Canal Sur Más](#el-streaming-en-canal-sur-canal-sur-más)
- [Señales IP](#señales-ip)
  - [Por qué IP: de un cable por señal a una red](#por-qué-ip-de-un-cable-por-señal-a-una-red)
  - [La familia SMPTE ST 2110](#la-familia-smpte-st-2110)
  - [El reloj común: PTP](#el-reloj-común-ptp)
  - [Redundancia y límites de paquete](#redundancia-y-límites-de-paquete)
  - [NMOS: descubrir, conectar y dar piloto en la red](#nmos-descubrir-conectar-y-dar-piloto-en-la-red)
  - [NDI](#ndi)
  - [Comparación](#comparación)
- [Coordinación con control](#coordinación-con-control)
  - [Quién coordina y qué dice el Libro de estilo](#quién-coordina-y-qué-dice-el-libro-de-estilo)
  - [Los canales entre el cámara y el control](#los-canales-entre-el-cámara-y-el-control)
  - [El procedimiento: antes, durante y después](#el-procedimiento-antes-durante-y-después)
  - [Un supuesto práctico](#un-supuesto-práctico)
- [Normas técnicas que el tema cita](#normas-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Producción móvil y transmisión

### Directo o diferido: la distinción que ordena el tema

Producción móvil es la que se hace fuera del centro de producción con equipos que se desplazan: el
equipo ligero de cámara y periodista, la mochila, la unidad móvil. Transmisión es la forma de
llevar lo captado hasta el centro. La distinción que ordena todo el tema es directo o diferido. Un
directo necesita caudal garantizado en ese instante; un envío de fichero puede tardar y reintentar.
De ahí que la mochila sea la máquina del directo y la transferencia de ficheros la del diferido
(oficio).

Las formas de sacar la señal de una localización (oficio):

| Camino | Qué es | Cuándo se usa |
|---|---|---|
| Radioenlace de microondas | Punto a punto, con antena parabólica apuntada | Directo con línea de vista y calidad garantizada |
| Satélite | Unidad con antena orientable | Donde no hay nada más: exteriores remotos |
| Fibra contratada | Línea dedicada | Eventos previstos con antelación |
| Mochila de agregación celular | Varias tarjetas de telefonía sumadas | Directo desde donde hay cobertura móvil |
| Transferencia de ficheros | El material grabado se envía como fichero | Cuando no hace falta directo: la mayoría de las piezas |
| Difusión continua por Internet (*streaming*) | Emisión hacia un servidor | Canales propios y redes |

Las vías de enlace se desarrollan en «Enlaces»; la mochila, en «Mochilas»; el *streaming*, en su
epígrafe.

### Qué pide la casa: producción prevé, el equipo se comunica

Lo propio de Canal Sur sobre transmisión está en su Libro de estilo, que es de 2004 y se define como
**«un conjunto de recomendaciones periodísticas y una selección de métodos de trabajo»**, aunque
advierte que **«hay casos en los que se marca una conducta obligatoria o se señala un comportamiento
inaceptable. En estos casos no hay elección posible»** (Introducción). No consta un manual
operativo publicado de CSRTV sobre mochilas, enlaces o redes IP.

La planificación de transmisiones y enlaces es de producción. El productor es responsable de
**«la planiﬁcación y asignación ordenada de recursos para las grabaciones en exteriores y en plató,
transmisiones y enlaces, intercambios y asistencias a otras televisiones, contratación de bienes o
servicios, edición y postproducción...»** (4.4). Y para
gestionarlo, producción **«tiene que disponer de un desglose detallado del asunto que se atiende,
el espacio o espacios para los que hay que trabajar y en qué formatos: directos, enlaces,
asistencias, aportaciones a desconexión, pactos con otras televisiones... La eﬁcacia es más
probable si se sabe pronto y exactamente lo que se quiere.»** (4.4.4, paso 2).

El equipo desplazado, por su parte, avisa: **«Ante una eventualidad, los equipos desplazados tienen
que comunicarse con productores y editores por si hay nuevas instrucciones o cambios sobre la
planiﬁcación inicial.»** (4.4.1) y **«Cualquier retraso en el trabajo que un equipo realice fuera
del centro de producción debe ser comunicado a los editores para que tomen una decisión.»** (5.6).
Un enlace que no llega, una mochila sin cobertura o un retardo mayor del previsto son exactamente
eso: una eventualidad que se comunica.

## Mochilas

### Qué es una mochila de transmisión

Una mochila de transmisión es un equipo portátil que envía vídeo y audio por las redes de telefonía
móvil, sumando el caudal de varias tarjetas a la vez para conseguir el ancho de banda que una sola
no daría (oficio). Lo que permite:

1. Aprovechar la capacidad disponible en las redes de telefonía móvil para enviar una señal de vídeo
   y audio.
2. En zonas de cobertura de telefonía móvil, llegar al lugar de la noticia, conectar la cámara a la
   mochila, encender el equipo y emitir en directo.
3. Evitar configuraciones complejas de transmisión, reducir costes de producción y conseguir
   presupuestos más ajustados.

### Lo que una mochila no promete

Una mochila no da transmisiones cien por cien estables, sin retardo, en zonas con poca cobertura
móvil. Los tres motivos, cada uno suficiente (oficio):

| Lo que no puede prometer | Por qué no |
|---|---|
| Estabilidad total | Ninguna transmisión celular lo es. El caudal disponible depende de cuánta gente use la misma célula, y en un acontecimiento con público la red se satura precisamente donde está la noticia |
| Ausencia de retardo | La agregación celular introduce siempre un retardo: la mochila almacena, reparte entre las tarjetas, reordena y entrega. Es su forma de funcionar, no un defecto |
| Funcionar con poca cobertura | Es lo contrario de su condición de uso. Sin cobertura no hay caudal |

Cualquier afirmación que prometa perfección sobre una red compartida («cien por cien», «sin
retardos») es falsa por construcción.

### Por dónde se conecta una mochila

Un equipo de transmisión con una mochila se puede conectar para enviar señal mediante tarjetas de
telefonía, wifi y cable de red (oficio):

| Vía | Cuándo se usa |
|---|---|
| Tarjetas de telefonía | La habitual: varias a la vez, de operadores distintos, sumando caudal |
| Red inalámbrica local (wifi) | Cuando hay una red disponible en el sitio: un hotel, un pabellón, una sede |
| Cable de red | Cuando hay línea fija: es la más estable de las tres |

La lógica de la máquina: la mochila no es un transmisor de radio, es un agregador de enlaces de
datos. Le da igual de dónde venga el caudal: reparte el flujo entre todos los caminos disponibles y
lo reconstruye al otro lado. Por eso admite las tres vías y puede usarlas a la vez. No son vías de
conexión de una mochila el radioenlace de microondas (otra tecnología, con su antena y su licencia)
ni las «ondas hertzianas» en general (cualquier transmisión de radio).

### Un ejemplo documentado: la LiveU LU800

No consta en un documento publicado qué modelo de mochila usa CSRTV. Como ejemplo de lo que hoy
declara un fabricante, la ficha web de la LiveU LU800 dice:

- Agregación: **«The LU800 bonds up to 14 connections with up to eight 5G/4G internal dual SIM
  modems; supporting up to 60Mbps, based on LiveU’s award-winning, patented HEVC technology.»** Es
  decir, suma hasta catorce conexiones, con hasta ocho módems internos 5G/4G de doble tarjeta, y
  comprime en HEVC.
- Calidad: **«up to 4Kp60 10-bit HDR transmission for optimal color depth and richness, as well as
  up to 16 audio channels.»**
- Varias cámaras: **«Up to four high-res, fully frame-synced feeds from a single portable unit.»**,
  con licencia multicámara (**«PRO2/PRO4 multi-cam license»**).
- Ficheros: además del directo, la mochila envía material editado: **«Easily upload edited files
  directly from your laptop to the station using the LU800 high speed bonded file transfer.»**
- Producción remota: **«Reduce costs by producing multi-camera live events from a centralized studio
  control room instead of on-site production and satellite trucks.»**

Las cifras son del fabricante, cambian con cada modelo y no son una norma. La ficha no da una cifra
de retardo: sólo dice **«the lowest latency»**, que es reclamo comercial. Las funciones de piloto,
retorno, intercomunicación y control remoto que la misma ficha declara se ven en «Coordinación con
control».

### El retardo de la mochila y cómo se trabaja con él

El retardo de una mochila es lo que obliga a que el presentador de estudio espere después de dar
paso, y es la razón de los silencios incómodos en los directos. No es un fallo del equipo: es cómo
funciona (oficio). Tres consecuencias para el cámara:

1. Se mide y se avisa. En la prueba previa se comprueba cuánto tarda la señal en llegar y se le dice
   al control, para que el presentador y el realizador lo tengan en cuenta.
2. El retorno de audio va sin la propia voz. Si el periodista oyera por el retorno su propia voz
   con retraso, no podría hablar. Por eso el retorno se da en N-1: todo el programa
   menos la propia fuente. El manual en español de los mezcladores ATEM lo describe así: **«Esta
   modalidad disponible en las salidas SDI permite silenciar el audio de una entrada específica en
   la señal de retorno. Por ejemplo, al realizar coberturas en directo, la demora en el audio de
   retorno podría provocar que el presentador se distraiga al escuchar su voz con retraso.»**
3. Se graba siempre en la cámara. La tarjeta de la cámara es la única copia si el enlace se cae.

Las cuentas del retardo se hacen en imágenes y en milisegundos. A 25 imágenes por segundo, una
imagen dura 40 ms, porque 1.000 ÷ 25 = 40; dos imágenes son 80 ms y cuatro son 160 ms. A 50 imágenes
por segundo, una imagen dura 20 ms. La regla de oficio para casar señales con retardos distintos
es que todo lo que llega antes se retrasa hasta el más lento, y el sonido se retrasa con él: nunca
se adelanta nada. El retardo de una mochila, en cambio, no se compensa en el
mezclador: se gestiona con la conversación (el presentador espera) y con el retorno en N-1.

## Enlaces

### Las vías de la contribución

Un enlace es el camino por el que la señal viaja desde el lugar de los hechos hasta el centro de
producción. Ese transporte hacia el centro es la contribución; el que va hacia el espectador es la
distribución. Las vías de contribución, como costumbre de oficio:

| Vía | Cómo funciona | Ventaja | Límite |
|---|---|---|---|
| Fibra óptica | Circuito contratado o instalado hasta el recinto | Capacidad y calidad; retardo mínimo | Hay que tenerla puesta: no vale para lo imprevisto |
| Enlace de microondas | Vano de radio hasta un repetidor o hasta el centro | Rápido de montar | Necesita visión directa y coordinación de frecuencias |
| Satélite (DSNG) | Antena en el vehículo, ascendente al satélite y descendente al centro | Llega desde cualquier sitio | Coste, licencia y retardo |
| Agregación de redes móviles | Varias tarjetas de telefonía sumadas en una mochila | Ligerísimo y barato | Depende de la cobertura; latencia variable |
| Redes de datos (FTTH, líneas dedicadas) | Transporte sobre red de datos, con protocolos de contribución | Barato donde hay red | Depende de la red de un tercero |

- *Satélite.* El tramo de subida al satélite es el enlace ascendente (en la jerga, *uplink*); el de
  bajada, el descendente (*downlink*). La Recomendación UIT-R SNG.770-2 (01/2012), de procedimientos
  operacionales uniformes para el DSNG, parte de **«que el SNG es temporal y ocasional, y que a menudo
  su activación no puede determinarse con gran antelación»** (considerando c) y lo define como
  transmisión **«con escaso tiempo de aviso»** mediante **«estaciones terrenas de enlace ascendente
  portátiles o fácilmente transportables»** (anexo 1, 1.1).
- *Mochila.* Una mochila de agregación suma varias conexiones de telefonía móvil para conseguir un
  canal estable. Sus dos límites son los de la red que usa: la cobertura, que no se controla, y la
  latencia, que varía con la carga de la red.

### Lo que la UIT-R pide al equipo de satélite

La misma Recomendación UIT-R SNG.770-2 da cuatro datos que afectan al equipo desplazado:

- Tamaño del equipo humano: el equipo DSNG **«debe poderse ajustar y manejar por un equipo de no más
  de dos (2) personas en un tiempo razonablemente corto (por ejemplo, 1 h)»** (anexo 1, 1.1).
- Comunicación con el otro extremo: recomienda **«que antes de efectuar transmisiones del DSNG y
  durante las mismas, se disponga de circuitos de radiocomunicaciones bidireccionales»**
  (recomienda 8). Y reconoce que **«para apoyar a los operadores del SNG, es posible que se
  requieran servicios de comunicaciones adicionales, como microondas punto a punto, sistemas de
  comunicaciones telefónicas, micrófonos inalámbricos símplex/dúplex bidireccionales y terminales
  móviles de satélite para voz y datos»** (considerando g). Es la coordinación con control llevada a
  una recomendación: contar, antes y durante la transmisión, con un canal de ida y vuelta con quien recibe.
- Cobertura: **«Es necesario que la zona de servicio del enlace descendente incluya el lugar de
  recepción previsto.»** (anexo 1, 2.2.1).
- Autorización: recomienda **«que para los transportes de satélite cuya cobertura regional abarque
  varios países, sólo se requiera la autorización del país a que corresponda el enlace ascendente
  apropiado»** (recomienda 9). Que la activación de una estación de DSNG necesita autorización lo da por supuesto
  la propia Recomendación, que pide que esa autorización sea **«expeditiva»** (considerando e).

### Contribución, distribución y control central

| | Contribución | Distribución o emisión |
|---|---|---|
| Qué es | El transporte de la señal hacia el centro de producción, para trabajar con ella | El transporte de la señal hacia el espectador |
| De dónde a dónde | Del acontecimiento al centro; de un centro a otro | Del centro emisor a la red de difusión o a Internet |
| Calidad | Alta: la señal se va a seguir manipulando | La que el sistema de emisión permita |
| Retardo | El menor posible | Menos crítico |

Toda señal que entra desde fuera (una unidad móvil, un centro territorial, una agencia, un equipo
con mochila) entra por el control central, que es la matriz de conmutación del centro de
producción: encamina las señales, las sincroniza con la casa, convierte formatos, corrige niveles y
las vigila antes de entregarlas a un control de realización. Una señal de fuera llega sin
sincronizar con la casa, a veces con el nivel mal y a veces en otro formato; el mezclador no puede
conmutarla así (oficio). Por eso, para el cámara en la calle, «el control» es a la vez el control
central que recibe su enlace y el control de realización que lo pone en antena.

### La unidad móvil como punto de enlace

Una unidad móvil es un control de realización montado sobre ruedas; produce en el sitio y necesita
su propio enlace de salida (fibra, microondas, satélite o red de datos) para llevar el programa al
centro. Sus cámaras cuelgan de las CCU por cable (triax o fibra híbrida) y reciben por él retorno,
intercomunicación y piloto (oficio). La unidad móvil, su montaje y el cable de cámara se estudian en
el tema 3. Lo que este tema añade es la alternativa que ya ofrecen los fabricantes de mochilas: la
producción remota, en la que las cámaras envían su señal al centro y la realización se hace desde un
control fijo, sin unidad móvil en el lugar (epígrafe «Mochilas»).

### El enlace inalámbrico de cámara

Cuando la cámara no puede ir atada por cable a la unidad móvil (la cámara al hombro que sigue la
acción por una banda, un circuito o una calle), lleva en la parte trasera un transmisor de radio que
envía su señal a un receptor en la unidad móvil o en el control (oficio). No es una mochila: no
agrega redes de telefonía, sino que establece su propio enlace de radio entre transmisor y receptor.

La modulación característica de estos enlaces es la COFDM, multiplexación por división en
frecuencias ortogonales codificada: así la titula un fabricante de estos equipos, Domo Broadcast Systems, en su libro blanco
**«Coded Orthogonal Frequency-Division Multiplexing (COFDM)»**. Es la misma técnica de la
televisión digital terrestre DVB-T, cuya norma europea (ETSI EN 300 744, V1.6.2,
2015-10) especifica la transmisión **«Orthogonal Frequency Division Multiplexing (OFDM)»** y, para
proteger la señal, **«an OFDM system with concatenated error correcting coding»** (4.1): la «C»
de COFDM es esa codificación.

Por qué se usa en la cámara inalámbrica, según ese libro blanco: en lugar de una sola portadora, los
datos se reparten entre muchas; como cada portadora está en una frecuencia algo distinta, una señal
reflejada sólo anula unas pocas, y lo que se pierde se recupera con la corrección de errores. Y
añade: **«These principles are equally applicable to wireless camera systems. Until the advent of
COFDM, these systems used analogue or single-carrier waveforms which were plagued by multi-path
(ghosting) and picture break-up as the transmitter moved around, particularly in areas with no
direct line of sight to the receiver. The introduction of COFDM technology revolutionised the way
newsgathering and sporting events were covered.»** Es decir: un transmisor que se mueve y sin visión
directa del receptor, justo el caso del cámara, es donde COFDM aguanta y la portadora única no.

Como ejemplo de lo que declara hoy un fabricante, la ficha del transmisor de trasera de cámara
Sapphire-BTX de Domo dice que **«integrates a true 4K HEVC encoder with a COFDM modulator, creating a
single, compact package suitable for camera-back mounting.»**; que admite **«camera control and
Tally interfaces»** (interfaces de control de cámara y de piloto; el control de cámara bidireccional
es una opción de hardware) y audio analógico con
alimentación **«for direct microphone connection»**; y da una latencia típica de codificación de
**«35mS input to output»**. Como las de la LU800, son cifras del fabricante, no de norma.

Las frecuencias en que trabajan estos transmisores y su régimen de uso no se estudian aquí (ver «Lo
que este tema no da»).

## *Streaming*

### Qué es el *streaming*

El *streaming* es la distribución de contenido multimedia de forma continua, de manera que el
usuario consume el producto al mismo tiempo que se descarga, sin necesidad de descargarlo
previamente. Su rasgo definitorio es la simultaneidad: se ve mientras llega (oficio).

Hay que distinguirlo de sus vecinos:

| Modo | Cómo funciona | Se puede ver antes de terminar |
|---|---|---|
| Descarga | El fichero se descarga entero y luego se abre | No |
| Descarga progresiva | El fichero se descarga en orden y se puede empezar a ver antes de que acabe | Sí, pero se descarga entero igual, y no se puede adaptar a la red |
| Transmisión por secuencias (*streaming* propiamente dicho) | El contenido se trocea en segmentos que se piden y se consumen sobre la marcha | Sí, y se adapta: si la red baja, se pide un segmento de menos calidad |
| Difusión digital (televisión digital terrestre) | Se emite por ondas y se recibe con antena | Sí, pero no es por red informática |

Para un directo, la forma adecuada es la transmisión por secuencias: la descarga progresiva no
sirve, porque un directo no es un fichero terminado que se pueda ir descargando en orden; lo que va
a venir aún no existe (oficio).

### Dos usos del *streaming*: contribuir y distribuir

La palabra se usa para dos cosas que conviene separar (oficio):

| | *Streaming* de contribución | *Streaming* de distribución |
|---|---|---|
| Para qué | Llevar la señal de la localización al centro | Llevar el programa al espectador por Internet |
| Quién recibe | El control central | El público, en su dispositivo |
| Qué importa | Latencia baja y constante, y que no se pierdan paquetes | Llegar a muchos a la vez y adaptarse a la red de cada uno |
| Ejemplo | Una mochila o un codificador enviando por Internet con un protocolo de contribución como SRT | La plataforma OTT de la cadena |

Para el cámara, el primero es su herramienta; el segundo es uno de los destinos de lo que graba.

### Emitir hacia una plataforma: URL, clave, RTMP y HLS

Cuando el directo no va al control sino a una plataforma de vídeo o a una red social, el codificador
(o la mochila, si lo permite) se configura con dos datos que da la plataforma. La ayuda de YouTube lo
dice así: **«Para iniciar la emisión en directo, introduce la URL del servidor y la clave de emisión
de YouTube Live en el codificador.»** Y del campo del servidor: **«Probablemente esta sección tenga un
nombre parecido a "servidor RTMP".»** La URL que YouTube muestra **«de forma predeterminada es la de
RTMP»**; ofrece también RTMPS, **«una versión segura de RTMP, que ofrece cifrado y conexión de
seguridad en la capa de transporte (TLS/SSL)»**, y la ingesta por HLS.

| Protocolo | Qué es, según su fuente | Estatus |
|---|---|---|
| RTMP | **«Adobe’s Real Time Messaging Protocol (RTMP) provides a bidirectional message multiplex service over a reliable stream transport, such as TCP [RFC0793], intended to carry parallel streams of video, audio, and data messages, with associated timing information, between a pair of communicating peers.»** | Especificación de una empresa (Adobe, 21 de diciembre de 2012); no es norma ni RFC |
| HLS | **«This document describes a protocol for transferring unbounded streams of multimedia data.»** (RFC 8216, resumen) | RFC 8216 (agosto de 2017), **«Category: Informational»**, presentada por la vía independiente: **«This document is not an Internet Standards Track specification; it is published for informational purposes.»** |

Lo que el cámara tiene que saber de cada uno:

- RTMP va sobre un transporte fiable como TCP, y el emisor entrega su señal con la orden de
  publicar: **«The client sends the publish command to publish a named stream to the server.»** En
  un directo, el tipo de publicación es «live»: **«Live data is published without recording it in a
  file.»** (especificación de Adobe, 7.2.2.6).
- HLS trocea: **«A Media Playlist contains a list of Media Segments, which, when played sequentially,
  will play the multimedia presentation.»**, y permite al receptor **«adapt the bit rate of the media
  to the current network conditions in order to maintain uninterrupted playback at the best possible
  quality.»** (RFC 8216, 1 y 2). Es la base documentada de la «transmisión por secuencias» y su
  adaptación a la red de la tabla de «Qué es el *streaming*». La RFC describe **«version 7 of this protocol»**; su
  revisión está en curso como borrador (draft-pantos-hls-rfc8216bis), que no la sustituye todavía.
- La contrapartida, en palabras de la ayuda de YouTube: **«HLS tiene una latencia superior porque
  envía segmentos de vídeo, en vez de una emisión continua como sucede con el protocolo RTMP.»** Y
  cuándo se elige HLS para ingesta: **«si quieres emitir vídeos de alto rango dinámico (HDR) o si
  utilizas códecs que no sean compatibles con el protocolo de mensajería en tiempo real (RTMP)»**.

Qué protocolo y qué plataformas usa Canal Sur para su distribución no consta en un documento
publicado.

### SRT, un protocolo de contribución por Internet

El repositorio de referencia de SRT lo define así: **«Secure Reliable Transport (SRT) is a transport
protocol for ultra low (sub-second) latency live video and audio streaming, as well as for generic
bulk data transfer.»** Es decir, un protocolo de transporte para vídeo y audio en directo con
latencia inferior al segundo, que sirve también para transferir datos. Sus rasgos, según el
borrador publicado en la IETF (draft-sharabayko-srt-01, de 7 de septiembre de 2021):

- Va sobre UDP: **«SRT is a user-level protocol over User Datagram Protocol and provides reliability
  and security optimized for low latency live video streaming, as well as generic bulk data
  transfer.»** (resumen).
- Recupera lo perdido: usa UDP **«but assures more reliable delivery using Automatic Repeat Request
  (ARQ), packet acknowledgments, end-to-end latency management, etc.»** (sección 1.1). El receptor
  pide que se repitan los paquetes que no llegan; para darles tiempo, trabaja con un colchón de
  latencia fijo.
- Se conecta como TCP: **«Like TCP, SRT employs a listener/caller model.»** (sección 1.2): un
  extremo escucha (*listener*) y el otro llama (*caller*); existe además un modo de encuentro
  (*rendezvous*).
- Cifra: admite AES de 128, 192 y 256 bits (tabla de cifrado del borrador). En la biblioteca de
  referencia, la contraseña (`SRTO_PASSPHRASE`) va de 10 a 80 caracteres y la latencia por defecto
  (`SRTO_LATENCY`) es de 120 ms, valor que la propia tabla marca con asterisco porque puede variar
  según el modo de transmisión.

El estatus importa en un test: SRT es un protocolo abierto, con código público, pero no es una norma
de la IETF. El borrador draft-sharabayko-srt-01 declara como estado previsto **«Informational»**
(informativo) y fija su propia caducidad (**«Expires: 11 March 2022»**); en el registro de
documentos de la IETF figura como expirado y presentado por la vía independiente. No es un RFC.

### El *streaming* en Canal Sur: Canal Sur Más

El Contrato-programa 2024-2026 entre el Consejo de Gobierno de la Junta de Andalucía y la RTVA trata la distribución por Internet en su
cláusula tercera, apartado 3.5 («Innovación tecnológica para la expansión multiplataforma»).
Quién lo organiza: según el punto 46 del mismo apartado, la producción y distribución de servicios y
contenidos digitales y su coordinación con la radio y la televisión corresponde a «**una dirección
organizativa específica, ‘Canal Sur Media’**», encargada, entre otras cosas, de las plataformas OTT,
el pódcast, los portales en internet, los canales web, la «**presencia y contribución en redes
sociales**» y el «**desarrollo de aplicaciones para dispositivos móviles**». Y según el punto 45, será
prioritaria la actuación de Canal Sur a través de «**su propia plataforma digital en sistema
streaming, ‘Canal Sur Más’**», disponible mediante aplicaciones para todo tipo de dispositivo
(televisores conectados, móviles, tabletas, ordenadores, videoconsolas), y «**en el ámbito del audio
digital a través de su propia plataforma digital de servicios Podcast**», cuyos contenidos se ponen
también a disposición de plataformas de terceros mediante acuerdos.

El mismo Contrato-programa, en su apartado 3.19 («Compromisos de cobertura por ondas hertzianas
terrestres y de distribución de servicios nuevos»), fija el horario: **«Se producirá y distribuirá 24 horas/día la prestación de la
plataforma de servicios audiovisuales digitales en sistema streaming (OTT) ‘Canal Sur Más’ basada en
protocolos de Internet accesible en aplicaciones de todo dispositivo digital con la oferta
audiovisual de las programaciones lineales sonoras y televisivas, y servicios ‘a petición’ sobre programas, espacios y
contenidos audiovisuales, y con ámbito geográfico de distribución mundial conforme a la posesión de
derechos de difusión pública sobre los programas, espacios y contenidos audiovisuales.»** (punto 103).
La difusión mundial queda, pues, sujeta a tener los derechos.

Lo que eso significa para el cámara: lo que graba y lo que transmite en directo no acaba sólo en la
emisión lineal; también se distribuye por *streaming* en la plataforma propia y en redes.

## Señales IP

### Por qué IP: de un cable por señal a una red

En la instalación clásica cada señal va por su cable (SDI para el vídeo, con el audio embebido) y
se conmuta en una matriz. En una instalación IP las señales viajan como paquetes por una red de
datos y se conmutan con equipos de red. La introducción de SMPTE ST 2110-10:2022 lo explica así:
**«The capability and capacity of IP networking equipment has improved steadily, enabling the use of
IP switching and routing technology to transport and switch video, audio, and metadata essence within
television facilities. This new work encapsulates each production element separately into IP.»**

La idea examinable está en la última frase: en ST 2110 cada esencia (vídeo, audio, datos) viaja
por separado, en su propio flujo, y no metida en una sola señal como en SDI. Y la base declarada:
**«This family of SMPTE standards builds on the work of VSF TR-03 and TR-04, and of AES67»**.

Para el cámara, IP aparece en tres sitios: dentro del centro (cámaras de estudio y controles en red
ST 2110), en la calle (la mochila y los protocolos de contribución por Internet, como SRT) y en
producciones ligeras (NDI en red local). Qué usa CSRTV en cada caso no consta en un documento
publicado.

### La familia SMPTE ST 2110

Título común de la familia: **«Professional Media Over Managed IP Networks»** (medios profesionales
sobre redes IP gestionadas). Las partes publicadas, según el índice oficial de la SMPTE:

| Parte | Título oficial | Qué cubre |
|---|---|---|
| ST 2110-10 | **«System Timing and Definitions»** | El sistema, el modelo de tiempo y lo común a todos los flujos |
| ST 2110-20 | **«Uncompressed Active Video»** | Vídeo sin comprimir |
| ST 2110-21 | **«Traffic Shaping and Delivery Timing for Video»** | Cómo se reparte en el tiempo el envío de los paquetes de vídeo |
| ST 2110-22 | **«Constant Bit-Rate Compressed Video»** | Vídeo comprimido a caudal constante |
| ST 2110-30 | **«PCM Digital Audio»** | Audio PCM |
| ST 2110-31 | **«AES3 Transparent Transport»** | Transporte transparente de AES3 |
| ST 2110-40 | **«SMPTE ST 291-1 Ancillary Data»** | Datos auxiliares |
| ST 2110-41 | **«Fast Metadata Framework»** | Metadatos |
| ST 2110-43 | **«Timed Text Markup Language for Captions and Subtitles»** | Subtítulos |

La columna «Qué cubre» es la traducción del título; de las partes 21, 22, 31, 40, 41 y 43 sólo se
ha leído el título. No existe una parte «ST 2110-50». Completan la familia una hoja de ruta
(OV 2110-0) y tres prácticas recomendadas (RP 2110-23, 24 y 25).

Lo que dicen las tres partes leídas:

- ST 2110-10:2022, alcance (cláusula 1): **«This standard is part of a family of engineering
  documents that define an extensible system of RTP-based essence streams referenced to a common
  reference clock, in a manner which specifies their timing relationships.»** y **«This standard
  specifies the system timing model and the requirements common to all of the essence streams, and
  defines timestamping methods for video streams and audio streams such that time alignment across
  essence is possible.»** Es decir: los flujos van en RTP, referidos a un reloj común, con marcas de
  tiempo que permiten volver a alinear vídeo y audio en el receptor.
- ST 2110-20:2022, alcance: **«This standard specifies the real-time, RTP-based transport of
  uncompressed active video essence over IP networks. An SDP-based signaling method is defined for
  image technical metadata necessary to receive and interpret the stream.»** El receptor sabe cómo
  es la imagen (resolución, muestreo) por una descripción SDP.
- ST 2110-30:2025, alcance: **«This standard specifies the real-time, RTP-based transport of PCM
  digital audio streams over IP networks by reference to AES67.»** Y el límite: **«Non-PCM digital
  audio signals including compressed audio signals are outside the scope of this standard.»** La
  edición vigente de esta parte es la de 2025, que revisa la de 2017.

### El reloj común: PTP

Si vídeo y audio viajan por separado, hace falta un reloj común para volver a juntarlos. ST 2110-10
lo resuelve con PTP (cláusula 7.2, «Distribution of the Common Reference Clock via PTP»):

- **«A Common Reference Clock, potentially derived from a traceable time source, should be provided
  and distributed on the network using IEEE Std 1588-2008 Precision Time Protocol (PTP).»**
- **«All Devices conforming to this standard shall support a Common Reference Clock delivered via
  IEEE Std 1588-2008 using any message rates allowed by the SMPTE ST 2059-2 PTP Profile.»**

Ojo al verbo: proveer el reloj en la red es un «should» (debería, recomendación); que todo
dispositivo conforme lo admita es un «shall» (deberá, obligación). El perfil de uso de PTP en
radiodifusión es la norma SMPTE ST 2059-2, que este tema no ha leído. PTP hace en la red IP lo que
el generador de sincronismos hace en una instalación SDI: que todo vaya al mismo compás.

### Redundancia y límites de paquete

- Redundancia (ST 2110-10, cláusula 8.5): **«Duplicate RTP streams meeting the requirements of SMPTE
  ST 2022-7 may be used for redundant transmission to achieve higher system availability.»** Es
  decir, se puede enviar cada flujo dos veces por caminos distintos, de modo que si uno falla el
  receptor sigue con el otro. Es un «may» (podrá): opción, no obligación.
- Tamaño de paquete (cláusula 6.3): **«The Standard UDP Size Limit shall be 1460 octets.»** No es un
  tope absoluto: la misma cláusula prohíbe superarlo **«unless operating conformant to the optional
  Extended UDP Size Limit specified in section 6.4»**, y ese límite extendido es de 8960 octetos
  (**«The Extended UDP Size Limit shall be 8960 octets.»**, cláusula 6.4). Usarlo es opción: los
  emisores **«may transmit»** hasta él, y los receptores sólo están obligados a recibir hasta el
  límite estándar (**«All Receivers shall be capable of receiving UDP packets up to the Standard UDP
  Size Limit.»**, cláusula 6.3).

### NMOS: descubrir, conectar y dar piloto en la red

ST 2110 dice cómo viajan las señales, no cómo se encuentran y se conectan los equipos. De eso se
ocupa NMOS. La AMWA lo define: **«NMOS is a family name for specifications produced by the Advanced
Media Workflow Association related to networked media for professional applications.»** Y la
propia ST 2110-10 remite a ella: **«The AMWA has developed an interface specification, AMWA IS-05,
for managing connections of the streams defined in this standard.»**

| Especificación | Título | Para qué sirve |
|---|---|---|
| IS-04 | **«Discovery & Registration»** | Que los equipos se anuncien y se encuentren en la red |
| IS-05 | **«Device Connection Management»** | Conectar un emisor con un receptor: el «cruce» de la matriz en IP |
| IS-07 | **«Event & Tally»** | Eventos y piloto por la red |
| IS-08 | **«Audio Channel Mapping»** | Asignar canales de audio |

Para el cámara, IS-07 es la que toca de cerca: en una instalación IP, el piloto de su cámara también
viaja por la red.

### NDI

La documentación de NDI lo presenta así: **«NDI stands for Network Device Interface.»** **«It is a
widely adopted video connectivity standard based on proprietary IP networking specifications.»** Es
decir, se basa en especificaciones propietarias: «standard» aquí tiene sentido comercial, no de
norma de un organismo de normalización. Y precisa: **«NDI is not a codec.»**; admite varios, entre
ellos **«our proprietary SpeedHQ, found on the NDI High Bandwidth format, AVC (H.264) and HEVC
(H.265), found on the NDI HX formats.»** Los equipos se encuentran solos: **«NDI offers two different
options for a zero-configuration discovery and registration: mDNS and Discovery Service.»**

### Comparación

| | SMPTE ST 2110 | SRT | NDI |
|---|---|---|---|
| Quién lo publica | SMPTE, organismo de normalización: es norma | Haivision y la comunidad SRT: código abierto y borrador IETF expirado; no es norma | La empresa de NDI: especificación propietaria |
| Dónde se usa | Red gestionada de la instalación (**«Managed IP Networks»**) | Contribución por redes no gestionadas, como Internet | Redes de producción ligeras; su descubrimiento por mDNS es propio de una red local |
| Compresión | -20 sin comprimir; -22 comprimido a caudal constante | Transporta lo que se le entregue | SpeedHQ, H.264 o HEVC |
| Cómo se sincroniza o protege | Reloj común PTP; flujos duplicados (ST 2022-7) | Latencia fija con repetición de paquetes (ARQ); cifrado AES | No se ha leído |

## Coordinación con control

### Quién coordina y qué dice el Libro de estilo

El Libro de estilo de Canal Sur no deja el directo a la inspiración: **«La improvisación no tiene
cabida como elemento de trabajo. Hasta donde sea posible, el equipo coordinado de producción,
realización, enlaces e informativos debe prever todo lo que pueda planiﬁcarse, sin olvidar
cualquier eventualidad: desde un aguacero hasta la interrupción del sonido de retorno. Lo
inesperado, en esencia, no puede ser previsto pero hay que estar preparado para resolverlo con
eﬁcacia y celeridad»** (8.3). Son cuatro áreas coordinadas (producción, realización, enlaces e
informativos), y la interrupción del retorno es el ejemplo de eventualidad técnica que el propio
texto pone.

El pacto va antes que el directo, y el cámara está nombrado en él: **«Los términos de cada
aparición en directo deben ser pactados entre todos los profesionales involucrados: productor,
cámara, técnicos de enlace, presentador en plató, equipo de edición, realizador... que deben estar
al tanto de los detalles y asumir por completo los de su competencia. A partir de ellos, el
reportero se someterá a lo acordado sin dar lugar a sorpresas y menos aún provocarlas. Siempre se
intentará plasmar todos los extremos en la escaleta.»** (8.1, punto 6).

Y el cierre también está pautado: **«Terminado el directo, en la despedida sólo habla el
presentador.»** (8.3.2). El cámara mantiene el plano y la conexión hasta que el control da la
conexión por terminada (oficio).

### Los canales entre el cámara y el control

El cámara en la calle necesita lo mismo que en un plató (oficio):

| Canal | Para qué | Cómo llega en la calle |
|---|---|---|
| Piloto (*tally*) | Saber si su señal está en antena | Por la mochila o por el cable de cámara |
| Retorno de programa | Ver y oír lo que se emite; oír el paso del presentador | Por la mochila, por un receptor aparte o por teléfono; el audio, en N-1 |
| Intercomunicación | Recibir órdenes y confirmar | Por la mochila, por el cable de cámara o por teléfono |
| Control remoto | Que el control ajuste la cámara | Por red, en equipos que lo permitan |

El manual en español de los mezcladores ATEM describe el piloto: la señal **«se utiliza
generalmente para encender una luz roja sobre la cámara o el monitor, de forma que el operador sepa
que está al aire.»** Y la llamada: **«Manteniendo presionado el botón CALL, la luz piloto de las
cámaras conectadas comenzará a parpadear. Esta es una manera muy útil de llamar la atención de los
camarógrafos o de indicarles que la señal va a ser emitida al aire.»** El detalle del piloto (el
verde de anticipo, que ese fabricante describe para sus cámaras y no es norma común) está en el
tema 3.

La ficha de la LiveU LU800 declara que esos canales viajan por la propia mochila:

- Piloto: **«LiveU’s Tally Light enables field reporters and camera operators to know instantly when
  they’re live on air.»**
- Retorno: **«LiveU Video Return enables field crews to see current program feeds and/or receive
  teleprompting information during live sessions.»**
- Comunicación: **«LiveU Audio Connect offers high-quality and reliable cloud-based audio solutions,
  enabling news anchors and producers in the station to communicate easily with camera operators and
  talents in the field.»**
- Control remoto: **«LiveU IP Pipe lets you gain remote control over a wide variety of
  network-based equipment, including robotic and PTZ cameras, Camera Control Units (CCUs), and
  IP-based intercom.»**

En una instalación IP con NMOS, el piloto viaja por la red mediante IS-07 («Event & Tally»,
epígrafe «Señales IP»).

### El procedimiento: antes, durante y después

No hay norma que regule la coordinación del cámara con el control en un directo. Lo que sigue es
costumbre de oficio, salvo lo que se atribuye al Libro de estilo:

| Momento | Qué hace el cámara |
|---|---|
| Antes de salir | Conoce el pacto del directo (8.1, punto 6): hora, duración, a qué programa entra, quién da paso. Comprueba baterías de cámara y mochila, tarjetas de telefonía y tarjetas de grabación |
| Al llegar | Busca el emplazamiento: cobertura móvil suficiente o línea fija, y un encuadre que permita reconocer el lugar. Monta, enciende y conecta la mochila |
| Prueba | Con el control central: llega la imagen, llega el audio con nivel correcto, funcionan el retorno (en N-1) y la intercomunicación, se enciende el piloto. Se mide el retardo y se comunica |
| Espera | Mantiene la señal enviada y la cámara grabando; vigila cobertura, batería y niveles; confirma por intercomunicación cada aviso del control |
| En antena | Piloto en aire: no corrige salvo lo imprescindible y de forma suave |
| Incidencia | Si cae la señal o el retorno, avisa al control por la vía de reserva (teléfono) y sigue grabando. Si hay retraso, lo comunica a los editores (5.6) |
| Después | Mantiene hasta que el control da la conexión por terminada; si se pide, envía lo grabado como fichero |

### Un supuesto práctico

Conexión en directo con mochila desde una plaza, para el informativo de mediodía. Qué hace el
cámara, en orden, y por qué (oficio, con las fuentes que se citan):

1. Llega con tiempo y elige el emplazamiento por dos criterios: que haya cobertura y que el
   encuadre deje reconocer el lugar. El Libro de estilo pide que un enviado especial se coloque
   **«en un punto que permita al espectador reconocer sin diﬁcultad el lugar donde se encuentra y
   desde el que informa»** (8.3.2).
2. Conecta la cámara a la mochila y la mochila a la red: las tarjetas de telefonía; si hay wifi o
   línea fija disponible en el sitio, la añade.
3. Llama al control central y prueba: imagen, audio, retorno en N-1, intercomunicación y piloto.
   Pregunta el retardo y confirma que el estudio lo conoce.
4. Graba en la tarjeta de la cámara durante todo el directo.
5. Si la plaza se llena y la red se satura, la calidad baja o la señal se corta: avisa al control
   y, si el directo no es viable, se decide en el centro (producción y editores), no en la calle.
6. Terminado el directo, sólo habla el presentador; el cámara mantiene el plano hasta que el control
   da la conexión por terminada.

## Normas técnicas que el tema cita

| Norma | Qué es | Edición |
|---|---|---|
| SMPTE ST 2110-10 | «Professional Media over Managed IP Networks: System Timing and Definitions» | 2022, aprobada el 28 de marzo de 2022; revisa la de 2017 |
| SMPTE ST 2110-20 | «… Uncompressed Active Video» | 2022, aprobada el 14 de diciembre de 2022; revisa la de 2017 |
| SMPTE ST 2110-30 | «… PCM Digital Audio» | 2025, aprobada el 1 de octubre de 2025; revisa la de 2017 |
| Recomendación UIT-R SNG.770-2 | «Procedimientos operacionales uniformes para el periodismo electrónico digital por satélite (DSNG)» | Enero de 2012 |
| ETSI EN 300 744 | «Digital Video Broadcasting (DVB); Framing structure, channel coding and modulation for digital terrestrial television» (sólo la cláusula 4.1) | V1.6.2 (2015-10) |

Citadas sólo por su título o por referencia, sin leer: SMPTE ST 2110-21, -22, -31, -40, -41 y -43;
SMPTE ST 2059-2 (perfil PTP); SMPTE ST 2022-7 (conmutación de protección con flujos duplicados);
IEEE 1588-2008 (PTP); AES67.

No son normas, y así se tratan: las especificaciones NMOS de la AMWA (especificaciones de una
asociación del sector); SRT (protocolo de código abierto con un borrador IETF expirado); NDI
(especificación propietaria); HLS (RFC 8216, informativa, fuera de la vía de normas de Internet);
RTMP (especificación de Adobe); la ficha de la LU800, el manual ATEM, el libro blanco y la ficha de
Domo y la ayuda de YouTube (documentación de fabricante o de plataforma).
El Libro de estilo de Canal Sur y el Contrato-programa 2024-2026 son documentos de la casa.

## Lo que este tema no da, y dónde está

- Qué mochilas, enlaces y redes usa CSRTV, y si sus instalaciones son SDI, ST 2110 o NDI, o si
  contribuye con SRT: no consta en un documento publicado localizado. No se ha localizado un manual
  operativo publicado de CSRTV sobre transmisiones.
- La latencia de una mochila, de un satélite o de NDI: no hay cifra de fuente leída.
- El perfil PTP SMPTE ST 2059-2 y el texto de las partes de ST 2110 distintas de la 10, la 20 y la
  30: no se han leído; sólo su título.
- De los protocolos de *streaming* de distribución, sólo se han leído el resumen y las secciones 1 y 2
  de la RFC 8216 (HLS) y la introducción y la orden *publish* de la especificación de RTMP; otros
  protocolos de distribución no se han leído.
- La norma ETSI EN 300 744, más allá de su cláusula 4.1; el detalle técnico de COFDM (portadoras,
  intervalo de guarda, modos). Las bandas de frecuencia de los enlaces inalámbricos de cámara y de
  microondas, y el régimen jurídico de su uso: no se han leído.
- La unidad móvil, su montaje, el cable de cámara, la señal *pool* y el detalle del piloto y la
  intercomunicación en plató, en el tema 3; los formatos, la ingesta y la entrega de ficheros, en el
  tema 7; la relación con redacción y realización, en el tema 8; la seguridad y el transporte del
  equipo, en el tema 11; la prevención de riesgos en exteriores, en el tema 14.

## Trazabilidad

| Fuente | Leída | Qué sostiene |
|---|---|---|
| *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004: Introducción, 4.4, 4.4.1, 4.4.4, 5.6, 8.1 (punto 6), 8.3, 8.3.2 | 24/09/2026 | Valor del Libro, planificación de transmisiones y enlaces por producción, comunicación de eventualidades y retrasos, pacto del directo, equipo coordinado, retorno, emplazamiento, despedida |
| Contrato-programa 2024-2026 entre el Consejo de Gobierno de la Junta de Andalucía y la RTVA (BOJA núm. 245, de 26 de diciembre de 2023), cláusula tercera, apartado 3.5, puntos 45 y 46, y apartado 3.19, punto 103 | 24/09/2026 | Canal Sur Media y la plataforma Canal Sur Más; distribución 24 horas al día |
| Recomendación UIT-R SNG.770-2 (01/2012), en español: considerandos c), e) y g), recomienda 8 y 9, anexo 1, 1.1 y 2.2.1 | 24/09/2026 | Carácter del DSNG, equipo de dos personas, comunicaciones bidireccionales, zona de servicio, autorización |
| SMPTE ST 2110-10:2022 (introducción, cláusulas 1, 6.3, 6.4, 7.2 y 8.5), ST 2110-20:2022 (cláusula 1), ST 2110-30:2025 (cláusula 1), textos de la biblioteca abierta de la SMPTE | 24/09/2026 | Esencias separadas, RTP, reloj común PTP, redundancia, tamaño UDP estándar y extendido, vídeo sin comprimir, audio PCM; fechas de aprobación y ediciones revisadas |
| SMPTE, índice oficial de la familia ST 2110 (`pub.smpte.org/doc/2110/`) | 24/09/2026 (índice y fichas de versiones de las partes 10, 20 y 30) | Títulos de las partes; edición activa de las partes 10 (2022), 20 (2022) y 30 (2025) |
| AMWA, índice de especificaciones NMOS (`specs.amwa.tv/nmos/`) | 24/09/2026 | Definición de NMOS; IS-04, IS-05, IS-07, IS-08 |
| SRT: README del repositorio de referencia (`github.com/Haivision/srt`), `docs/API/API-socket-options.md` y draft-sharabayko-srt-01 (IETF, 7 de septiembre de 2021) | 24/09/2026 | Definición, UDP, ARQ, modelo *listener/caller*, cifrado, contraseña, latencia por defecto, estatus |
| NDI, documentación en línea («What is NDI», «Discovery & Registration») | 24/09/2026 | Definición, carácter propietario, códecs, descubrimiento |
| LiveU, ficha web de la LU800 (descargada el 03/09/2026) | 24/09/2026 | Agregación, calidad, multicámara, envío de ficheros, producción remota, piloto, retorno, comunicación, control remoto |
| Blackmagic Design, *Manual de instalación y funcionamiento de los ATEM Live Production Switchers*, español, diciembre de 2024: «Ajustes del modo N-1», señalización de piloto, «Botón de llamada» | 24/09/2026 | N-1, piloto rojo, llamada |
| ETSI EN 300 744 V1.6.2 (2015-10), cláusula 4.1 («General considerations») | 24/09/2026 | OFDM con codificación de corrección de errores en la TDT |
| Domo Broadcast Systems, libro blanco «Coded Orthogonal Frequency-Division Multiplexing (COFDM)» (págs. 1-3) y ficha web del Sapphire-BTX Camera Back Transmitter | 24/09/2026 | Nombre de COFDM, por qué resiste el multitrayecto, uso en cámaras inalámbricas; codificador HEVC con modulador COFDM, piloto y control de cámara, latencia declarada |
| RFC 8216, *HTTP Live Streaming* (agosto de 2017): cabecera, resumen, estado, secciones 1 y 2; ficha de la RFC en el RFC Editor (sin RFC que la sustituya) y registro de la IETF de draft-pantos-hls-rfc8216bis (borrador activo) | 24/09/2026 | Definición de HLS, segmentos, adaptación de caudal, versión 7, estatus |
| Adobe, *Adobe’s Real Time Messaging Protocol* (H. Parmar y M. Thornburgh, 21 de diciembre de 2012): resumen, introducción y 7.2.2.6 | 24/09/2026 | Definición de RTMP, transporte fiable (TCP), orden *publish* y tipo «live» |
| Ayuda de YouTube: «Crear una emisión en directo de YouTube con un codificador», «Emitir en directo con el protocolo HLS» y «Cifrar emisiones en directo con RTMPS» (en español) | 24/09/2026 | URL del servidor y clave de emisión, servidor RTMP, RTMP por defecto, RTMPS, cuándo HLS y su mayor latencia |

Oficio sin norma detrás, y así se declara: la distinción entre directo y diferido y la tabla de
caminos; qué permite y qué no una mochila, sus vías de conexión y su retardo; la aritmética de
imágenes y milisegundos; la tabla de vías de contribución; contribución, distribución y control
central; la producción remota como alternativa a la unidad móvil; el transmisor a la espalda de la
cámara como alternativa al cable; los modos de distribución por red y los dos usos del *streaming*; la comparación ST 2110, SRT y NDI en lo que no se atribuye a su
fuente; los canales entre cámara y control; el procedimiento y el supuesto práctico.
