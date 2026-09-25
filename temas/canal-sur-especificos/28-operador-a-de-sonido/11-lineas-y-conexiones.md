# Tema 11 del específico de Operador/a de Sonido · Líneas y conexiones

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 11 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Sin norma legal. Normas técnicas: EBU Tech 3250, 3.ª ed., 2004 (interfaz AES/EBU); ANSI/SMPTE 276M-1995 (AES/EBU por coaxial); SMPTE 272M-2004, ST 299-1:2009 y ST 299-2:2010 (audio embebido en SDI); SMPTE ST 2110-10:2022 (transporte sobre UDP) y ST 2110-30:2025 (audio PCM sobre IP, con referencia a AES67). Documentación de fabricante: Audinate, *Dante Controller User Guide* 4.18 (2026); RME, manuales del MADI Converter y del ADI-648; DiGiCo, nota técnica TN294 (MADI); Crown, Rane, Soundcraft y Shure (patillaje de XLR y jack). Lo demás, oficio |
| **Redacción que se estudia** | Las normas técnicas en las ediciones citadas, leídas el 25/09/2026; la guía de Audinate en su versión publicada el 6 de mayo de 2026 |
| **Extensión** | 11.500 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); conector circular de tres
polos con anillo de bloqueo (**XLR**); jack de punta, anillo y cuerpo (**TRS**, *tip, ring,
sleeve*) y de sólo punta y cuerpo (**TS**); conector coaxial de bayoneta (**BNC**); Audio
Engineering Society (**AES**), Unión Europea de Radiodifusión (**UER**, que firma en inglés como
**EBU**, *European Broadcasting Union*) y Society of Motion Picture and Television Engineers
(**SMPTE**); la interfaz de audio digital de dos canales **AES3**, que el sector y la propia EBU
llaman **AES/EBU**; interfaz digital de audio multicanal (**MADI**, *multichannel audio digital
interface*), que es la norma **AES10**; la interfaz óptica de ocho canales **ADAT** (marca de la casa
Alesis, que la especifica) y el conector óptico **TOSLINK**; interfaz digital serie
de vídeo (**SDI**, *serial digital interface*), en definición estándar (**SD**) y alta (**HD**);
espacio de datos auxiliares horizontal (**HANC**, *horizontal ancillary data space*); **Dante**,
nombre comercial del sistema de audio en red de la casa Audinate; la norma de interoperabilidad de
audio sobre red **AES67**; protocolo de internet (**IP**); protocolo de datagramas de usuario
(**UDP**) y de control de transmisión (**TCP**); protocolo de tiempo real (**RTP**); protocolo de tiempo de precisión (**PTP**, *precision time
protocol*), definido en la norma **IEEE 1588** del Institute of Electrical and Electronics
Engineers (**IEEE**); modulación por impulsos codificados (**PCM**), el audio digital lineal sin
comprimir; conversión de frecuencia de muestreo (**SRC**, *sample rate conversion*); el formato
que reparte cada canal de 96 o 192 kHz en varios canales de 48 kHz (**S/MUX**, que RME llama
*Sample Split*); el conector de red **RJ45**; intervalo unitario (**UI**, *unit interval*), la duración de un
símbolo, en que se mide la fluctuación de fase (*jitter*); megabit por segundo (**Mbit/s** o
**Mbps**) y gigabit por segundo (**Gb/s**); milivoltio pico a pico (**mVpp**); micra (**µm**) y nanómetro (**nm**); corriente
continua (**DC**, en las citas en inglés); interferencia electromagnética (**EMI**); las
abreviaturas **DI** y **DO** (*digital input*, *digital output*) con que la EBU pide rotular las
entradas y salidas digitales; el modo de doble velocidad de muestreo (**DS**, *double speed*); el
módulo óptico **FDDI**, que el MADI óptico toma de la técnica de redes de ordenadores (RME no
desarrolla la sigla), y los conectores de fibra **SC** y **ST**; el prefijo **ST** con que la
SMPTE numera hoy sus normas (ST 299-1, ST 2110-30); los niveles de conformidad **A**, **AX**, **B**,
**BX**, **C** y **CX** de la ST 2110-30 y su símbolo **SGRP** (un grupo de audio SDI); las preguntas
frecuentes de un fabricante (**FAQ**, *frequently asked questions*); decibelios referidos a 0,775 voltios
(**dBu**) y a la escala completa digital (**dBFS**, *decibels relative to full scale*); retorno de
programa sin la propia fuente (**N-1**, en inglés *mix-minus*).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 11):
>
> Líneas y conexiones: XLR, jack, BNC, Dante/AES67, MADI, AES/EBU, ADAT, SDI, embebido y
> desembebido.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué lleva cada pin de un XLR y cada contacto de un jack TRS, qué jack es
desbalanceado y qué pasa al cruzar los pines 2 y 3; qué impedancia tiene el cable AES/EBU (110 Ω) y
el coaxial (75 Ω), qué conector usa cada uno, cuál es la amplitud de salida de cada versión, qué
distancia alcanza y dónde se ecualiza; cuántos canales lleva una trama AES/EBU, cuántos bits tiene
una subtrama, cuántas tramas hay en un bloque y a qué frecuencia se trabaja en radiodifusión; si
importa la polaridad de los pines 2 y 3 en digital; cuántos canales lleva el MADI a 48 y a 96 kHz,
a qué distancia llega por coaxial y por fibra, qué fibra y qué conector usa, por qué dos equipos
MADI pueden no entenderse (56 frente a 64 canales, S/MUX frente a alta velocidad) y cómo se protege
un enlace; cuántos canales lleva el ADAT a 48, 96 y 192 kHz, por qué cable y hasta qué distancia;
cuántos canales de audio caben embebidos en SDI en SD y en HD, en qué grupos y en qué espacio de la
señal; qué hace un embebedor y un desembebedor y por qué no se debe convertir la frecuencia de
muestreo de una señal no PCM embebida; qué es Dante, qué es una suscripción, cuántos canales lleva
un flujo unicast, qué latencia tiene por defecto, qué versión de PTP usa y cómo funciona su
redundancia; qué es AES67 y qué relación tiene con la ST 2110-30, qué frecuencia de muestreo es
obligatoria y qué es el nivel A; qué diseño de panel de conexiones permite escuchar sin cortar; qué
es un *splitter* y qué se comparte en uno pasivo. En la prueba práctica: cablear una entrada
analógica y una digital, elegir cable y conector para cada formato, localizar por qué no llega una
señal AES/EBU o MADI, sacar el audio de una cámara por SDI a la mesa y reordenar sus pistas, o
calcular el caudal de unos canales en red.

<!-- indice -->

## Índice

- [Líneas y conexiones](#líneas-y-conexiones)
  - [Qué es una línea y qué cambia del analógico al digital](#qué-es-una-línea-y-qué-cambia-del-analógico-al-digital)
  - [Los cables y sus impedancias](#los-cables-y-sus-impedancias)
  - [Resumen de formatos](#resumen-de-formatos)
  - [El panel de conexiones](#el-panel-de-conexiones)
  - [El *splitter*](#el-splitter)
  - [Las matrices de conmutación](#las-matrices-de-conmutación)
- [XLR](#xlr)
  - [El conector y su patillaje](#el-conector-y-su-patillaje)
  - [Por qué el XLR va balanceado](#por-qué-el-xlr-va-balanceado)
  - [El XLR en audio digital: la AES/EBU](#el-xlr-en-audio-digital-la-aesebu)
  - [Qué puede ir por un XLR](#qué-puede-ir-por-un-xlr)
- [Jack](#jack)
  - [El jack TRS y el TS](#el-jack-trs-y-el-ts)
- [BNC](#bnc)
  - [El conector BNC y los 75 ohmios](#el-conector-bnc-y-los-75-ohmios)
  - [La AES/EBU por coaxial (SMPTE 276M)](#la-aesebu-por-coaxial-smpte-276m)
  - [El BNC en MADI y en SDI](#el-bnc-en-madi-y-en-sdi)
- [Dante/AES67](#danteaes67)
  - [De la matriz a la red](#de-la-matriz-a-la-red)
  - [Qué es Dante](#qué-es-dante)
  - [Flujos: unicast y multicast](#flujos-unicast-y-multicast)
  - [Qué se puede conectar con qué](#qué-se-puede-conectar-con-qué)
  - [La latencia](#la-latencia)
  - [El reloj y la redundancia, en lo que tocan a la conexión](#el-reloj-y-la-redundancia-en-lo-que-tocan-a-la-conexión)
  - [El cable y el conmutador](#el-cable-y-el-conmutador)
  - [Por qué UDP y cuánto ocupa un canal](#por-qué-udp-y-cuánto-ocupa-un-canal)
  - [AES67 y la ST 2110-30](#aes67-y-la-st-2110-30)
- [MADI](#madi)
  - [Qué es el MADI](#qué-es-el-madi)
  - [Por coaxial y por fibra](#por-coaxial-y-por-fibra)
  - [Por qué dos equipos MADI pueden no entenderse](#por-qué-dos-equipos-madi-pueden-no-entenderse)
  - [Cómo se protege un enlace MADI](#cómo-se-protege-un-enlace-madi)
- [AES/EBU](#aesebu)
  - [Qué es](#qué-es)
  - [La estructura: subtrama, trama y bloque](#la-estructura-subtrama-trama-y-bloque)
  - [Las características eléctricas](#las-características-eléctricas)
  - [AES/EBU por cable de red](#aesebu-por-cable-de-red)
- [ADAT](#adat)
  - [Qué lleva y por dónde](#qué-lleva-y-por-dónde)
  - [El aviso práctico: el S/MUX no se detecta solo](#el-aviso-práctico-el-smux-no-se-detecta-solo)
- [SDI](#sdi)
  - [El audio embebido en SDI](#el-audio-embebido-en-sdi)
  - [Grupos, pares y espacio auxiliar](#grupos-pares-y-espacio-auxiliar)
  - [El reloj del audio embebido](#el-reloj-del-audio-embebido)
  - [Audio no PCM embebido](#audio-no-pcm-embebido)
  - [Del SDI a la red](#del-sdi-a-la-red)
- [Embebido y desembebido](#embebido-y-desembebido)
  - [Qué es embeber y desembeber](#qué-es-embeber-y-desembeber)
  - [Dónde se embebe y se desembebe](#dónde-se-embebe-y-se-desembebe)
  - [Conversiones y compatibilidad](#conversiones-y-compatibilidad)
  - [Un supuesto práctico](#un-supuesto-práctico)
- [Normas técnicas que el tema cita](#normas-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Líneas y conexiones

### Qué es una línea y qué cambia del analógico al digital

Una línea es el camino físico de una señal entre dos equipos: el cable, sus conectores y los paneles
y matrices por los que pasa. El enunciado junta en un solo tema tres familias que en una
instalación conviven (oficio):

| Familia | Qué viaja por el cable | Conectores del tema |
|---|---|---|
| Analógica | Una tensión que copia la onda sonora; un canal por par | XLR, jack |
| Digital dedicada | Muestras en serie, con un número fijo de canales por cable | XLR y BNC (AES/EBU), BNC y fibra (MADI), óptico (ADAT), BNC (SDI con audio embebido) |
| Red | Paquetes de datos; los canales los decide el ancho de banda | RJ45 y fibra de red (Dante, AES67) |

En analógico, la línea se juzga por el ruido que recoge; de ahí la conexión balanceada del XLR y del
jack TRS (tema 2). En digital, la línea se juzga por si los bits llegan enteros, y eso depende de que
el cable tenga la impedancia del sistema:

Por qué importa: una señal digital tiene flancos muy rápidos y se comporta como radiofrecuencia. Si
la impedancia del cable no es la del sistema, hay reflexiones, y las reflexiones producen errores de
bit. Un cable de micrófono lleva AES3 unos metros y falla a partir de cierta longitud, sin previo
aviso y de forma intermitente: es una de las averías más difíciles de encontrar.

### Los cables y sus impedancias

Un cable de micrófono y un cable AES/EBU pueden llevar el mismo conector y no ser el mismo cable:

| Cable | Impedancia | Para qué |
|---|---|---|
| De micrófono | No está especificada: es audio analógico y la impedancia característica no interviene | Audio analógico balanceado |
| AES3 sobre XLR | 110 ohmios | Audio digital de dos canales |
| AES3 sobre coaxial (AES3id) | 75 ohmios | Audio digital sobre infraestructura de vídeo |

Las dos cifras digitales tienen norma leída: 110 Ω para el par balanceado (EBU Tech 3250, epígrafe
«AES/EBU») y 75 Ω para el coaxial (SMPTE 276M, epígrafe «BNC»). El MADI por coaxial también es de 75
Ω (RME, epígrafe «MADI»). El vídeo SDI va igualmente por coaxial de 75 Ω con BNC, pero la norma de
su capa física no se ha leído: se da como oficio.

### Resumen de formatos

| Formato | Canales por cable | Soporte y conector | Fuente |
|---|---|---|---|
| AES/EBU (AES3) | 2 | Par balanceado de 110 Ω con XLR, o coaxial de 75 Ω con BNC | EBU Tech 3250; SMPTE 276M |
| MADI (AES10) | 56 o 64 (el modo de 64, hasta 48 kHz + 1 %); 32 a 96 kHz en modo de 64 canales | Coaxial de 75 Ω con BNC (hasta 100 m en un equipo de RME) o fibra multimodo con conector SC (casi 2 km) | RME; DiGiCo |
| ADAT | 8 a 48 kHz, 4 a 96 kHz, 2 a 192 kHz | Fibra óptica con TOSLINK, unos 10 m | RME |
| SDI con audio embebido | Hasta 16 (SD y HD a 1,5 Gb/s; 4 como máximo en SD compuesto); hasta 32 en las interfaces de 3 Gb/s con la ST 299-2 | Coaxial de vídeo | SMPTE 272M, ST 299-1 y 299-2 |
| Dante y AES67 | Los que quepan en el ancho de banda de la red | Ethernet: cable de pares con RJ45, o fibra | Audinate; SMPTE ST 2110-30 |

Cada fila se desarrolla en su epígrafe; las cifras y sus citas están allí.

### El panel de conexiones

El panel de conexiones (*patch panel*) reúne en un frontal las entradas y salidas de los equipos de
una sala para poder cambiarlas con latiguillos (*patch cords*). Lo que distingue un panel de otro es
qué pasa con la conexión interna, la que existe sin latiguillo, cuando se inserta uno (oficio):

| Diseño | Con el latiguillo puesto |
|---|---|
| Normalizado (*full normalled*) | Se corta la conexión interna en LOS DOS lados: se interrumpe la señal que iba por defecto |
| Seminormalizado (*half normalled*) | Se corta sólo al insertar en la fila INFERIOR; al insertar en la superior se toma una copia y NO se corta nada |
| No normalizado (*non normalled*) | No hay conexión interna: nada pasa si no se pone latiguillo |

Qué gana el seminormalizado: permite ESCUCHAR o DERIVAR una señal sin interrumpirla. Se pincha en
la fila de arriba, se saca una copia, y el camino normal sigue funcionando. Es lo que hace posible
medir una línea en directo sin tirar la emisión.

Un aviso de vocabulario: «balanceado» se refiere al cableado, no a la normalización. Un panel puede
ser balanceado y normalizado, o balanceado y seminormalizado.

### El *splitter*

El dispositivo que distribuye la señal de un micrófono a varias salidas idénticas con el mismo nivel
de señal es el *splitter* de audio (oficio). Se usa cuando la misma fuente tiene que llegar a varias
mesas: la de sala y la de monitores, o la de un directo y la de una unidad de grabación.

Cada mesa ajusta su ganancia de entrada de forma independiente: el previo de cada mesa es suyo.
Subir la ganancia en la mesa de sala no cambia lo que oye la mesa de monitores.

Lo que sí se comparte, y hay que saberlo: con un splitter PASIVO —normalmente un transformador o un
simple paralelo— hay dos cosas que sí se comparten. La primera, la alimentación fantasma: sólo UNA de
las mesas debe entregarla, y las demás deben tenerla cortada o aisladas por transformador. La
segunda, la carga: colgar varias entradas del mismo micrófono baja la impedancia que éste ve. Por eso
los repartos serios llevan transformadores de aislamiento y no un simple paralelo.

El *splitter* no es un filtro de cruce (reparte por frecuencia, tema 10) ni un fader (ajusta el nivel
de un canal, tema 4).

### Las matrices de conmutación

Qué es una matriz: un aparato con N entradas y M salidas que permite llevar cualquier entrada a
cualquier salida, y la misma entrada a varias salidas a la vez. Es el conmutador central de una
instalación.

| Concepto | Qué es |
|---|---|
| Entrada (*source*) | Una señal que llega: cámara, estudio, servidor, exterior |
| Salida (*destination*) | Un destino: un estudio, un grabador, un enlace, un monitor |
| Nivel | Vídeo, audio y datos se conmutan en niveles que pueden ir juntos o por separado |
| Panel de control | Los teclados con que se ordena la conmutación |
| Salvado o *salvo* | El bloqueo de una salida para que nadie la cambie por error durante una emisión |

Y la regla de oro del control central: una señal que va al aire se protege. Esa es la función del
salvado, y es lo que evita que una conmutación equivocada tire una emisión.

Las tres clases de matriz (oficio):

| Clase | Cómo funciona | Dónde |
|---|---|---|
| Analógica | Conmuta señal eléctrica | Instalaciones antiguas y patch de emergencia |
| Digital | Conmuta muestras: la señal ya va digitalizada | Salas técnicas |
| Sobre red (IP) | No conmuta nada: SUSCRIBE. Cada destino pide el flujo que quiere | Instalaciones actuales: es el epígrafe «Dante/AES67» y el tema 15 |

La diferencia de fondo: una matriz física tiene un límite duro de entradas y salidas. Una red no: su
límite es el ancho de banda. Ése es el cambio que el audio sobre IP introduce en una instalación, y no
la calidad del sonido.

## XLR

### El conector y su patillaje

El XLR es el conector circular de tres polos con anillo de bloqueo. La EBU lo identifica por la
norma que lo describe y da el nombre corriente: **«the circular latching three-pin connector
described in IEC 60268-12 (this type of connector is normally called "XLR")»** (EBU Tech 3250,
6.4).

En audio analógico balanceado, en un conector XLR de tres pines el cable «vivo» se conecta al pin 2.
El reparto completo, que es lo que hay que memorizar:

| Pin | Qué lleva |
|---|---|
| 1 | Malla o masa |
| 2 | Vivo, señal en fase, también llamado positivo o *hot* |
| 3 | Retorno, señal en contrafase, también llamado negativo o *cold* |

Y la regla que el oficio usa para no olvidarlo: uno, dos, tres: masa, vivo, retorno. Es convenio de
la AES; Rane (RaneNote 151) lo recuerda así: **«the Audio Engineering Society has adopted the "pin 2
is hot" standard»**.

### Por qué el XLR va balanceado

La señal viaja por dos conductores en oposición de fase; lo que el cable recoge por el camino se
induce igual en los dos, y la entrada, al restar uno del otro, lo cancela. El mecanismo, la masa del
pin 1 y los bucles de masa se estudian en el tema 2. Para este tema bastan sus dos consecuencias:

1. Un cable balanceado puede ser muy largo sin coger ruido. Uno desbalanceado, no.
2. Si un cable tiene el 2 y el 3 cruzados, ese canal entra con la polaridad invertida y al sumarlo
   con otro se cancelan parcialmente. Es la avería que más se busca en un montaje grande.

### El XLR en audio digital: la AES/EBU

El mismo conector es el normalizado para la AES/EBU. La EBU fija qué lado es macho y cuál hembra
(Tech 3250, 6.4):

- Salida: **«An output connector fixed on an item of equipment shall use male pins with a female
  shell. The corresponding cable connector shall thus have female pins with a male shell.»** El
  equipo tiene pines macho en la salida; el cable que se le enchufa, hembra.
- Entrada: **«An input connector fixed on an item of equipment shall use female pins with a male
  shell and the corresponding cable connector shall thus have male pins with a female shell.»**
- Pines: **«Pin 1: Cable shield or signal earth, Pin 2: Signal Pin 3: Signal»**, con una nota que
  separa el digital del analógico: **«(Note that the relative polarity of pins 2 and 3 is not
  important in the digital case)»**.

La razón de esa nota está en la codificación de la señal: la parte de datos de cada subtrama va en
código bifase, precisamente para **«make the interface insensitive to the polarity of connections»**
(Tech 3250, 2.3). Un cable con el 2 y el 3 cruzados invierte la polaridad de un micrófono; a una
señal AES/EBU no le hace nada.

Y como el conector es el mismo, la EBU pide rotularlo: los fabricantes **«should clearly label
digital audio inputs and outputs as such»** y usar las abreviaturas
**«"DI" and "DO"»** para las entradas y salidas digitales cuando falte sitio en el panel y el conector
pueda confundirse con uno analógico.

### Qué puede ir por un XLR

Por el mismo conector pueden llegar a una mesa cuatro cosas distintas (oficio):

| Señal | Qué exige | Dónde se estudia |
|---|---|---|
| Micrófono | Entrada de micro, con ganancia alta; *phantom* sólo si el micrófono la pide | Temas 2 y 3 |
| Línea analógica | Entrada de línea; nunca por una entrada de micro sin atenuar | Tema 2 |
| AES/EBU | Entrada digital y cable de 110 Ω | Epígrafe «AES/EBU» |
| Alimentación A-B (12 V) | Sólo micrófonos preparados para ella; puede dañar un dinámico | Tema 2 |

Aplicación práctica: el XLR no dice lo que lleva. Antes de enchufar una manguera o un latiguillo
conviene saber si esa línea es de micro, de línea o digital, y si la entrada tiene la *phantom*
activada.

## Jack

### El jack TRS y el TS

El jack es el conector de clavija cilíndrica de los paneles de conexiones, los instrumentos, los
auriculares y muchas entradas de línea. El de 6,35 mm (un cuarto de pulgada, 1/4") puede tener tres
contactos (TRS: punta, anillo y cuerpo) o dos (TS: punta y cuerpo).

El patillaje del TRS balanceado, frente al del XLR, lo da Crown para las entradas de sus etapas de
potencia: **«XLR Pin 1 is ground (shield). Pin
2 is hot (non-inverting) Pin 3 is low (inverting) 1/4" TRS Tip: hot (non-inverting) Ring: low
(inverting) Sleeve: Shield (ground)»**.

| XLR | Jack TRS | Qué lleva |
|---|---|---|
| Pin 1 | Cuerpo (*sleeve*) | Malla |
| Pin 2 | Punta (*tip*) | Vivo |
| Pin 3 | Anillo (*ring*) | Retorno |

Rane (RaneNote 151) confirma la equivalencia de la malla y la medida: la malla va al **«pin 1 for
3-pin (XLR-type) connectors, the sleeve on 1/4" (6.35mm) jacks»**.

El jack TS, de sólo punta y cuerpo, no tiene retorno: es desbalanceado (tema 2). Aplicación
práctica: un latiguillo TS entre dos equipos balanceados pierde la inmunidad al ruido y, según cómo
estén cableadas las salidas, parte del nivel; un jack TRS no garantiza por sí solo que la conexión
sea balanceada, porque el mismo conector de tres contactos se usa también para señales que no lo son.
Rane lo enumera: **«Stereo ¼" connectors are used for headphones, balanced interconnection, effect
and insert send/return loops, relay switch closure points, and an extravagant collection of other
miscellaneous connections»**. Hay que leer la hoja del equipo (oficio).

Qué lleva cada contacto según el uso. Las dos primeras filas son el convenio que Rane da para sus
propios equipos (**«On Rane equipment outfitted with input/output phone jacks»**); la de auriculares,
para las salidas **«designed exclusively for headphone use»**:

| Uso del TRS | Punta (*tip*) | Anillo (*ring*) | Cuerpo (*sleeve*) | Fuente |
|---|---|---|---|---|
| Línea balanceada | Positivo (vivo) | Negativo (retorno) | Masa | Rane, RaneNote 102: **«Tip = Positive Ring = Negative Sleeve = Ground»** |
| Auriculares estéreo | Canal izquierdo | Canal derecho | Común | Rane, RaneNote 102: **«Tip = Left Positive Ring = Right Positive Sleeve = Common Ground»** |
| Punto de inserción de una mesa | Envío (sale de la mesa) | Retorno (vuelve a la mesa) | Masa (oficio) | Soundcraft (abajo) |

En el jack TS, Rane da **«Tip = Positive Sleeve = Ground»**. La inserción la explica Soundcraft: el
punto de inserción es **«a single, ‘A’ Gauge, 3-pole (stereo), switched jack socket»**; al enchufar
el jack **«the signal path is interrupted. The signal is taken out of the mixer via the plug tip,
through an external piece of equipment and then back to the mixer on the ring of the plug»**, con
un cable en Y: **«A special Ycord is required which has the stereo jack at one end and two mono
jacks, for the processor’s input and output, at the other»**. Y para llevar una fuente desbalanceada
a una entrada de línea TRS, **«the screen of the cable is wired to both the Ring and the Sleeve of the
jack»**. Soundcraft avisa de que **«wiring conventions can vary between manufacturers»**.

El jack pequeño, que Shure mide en 1/8" (en el oficio se le llama de 3,5 mm), es también TRS en los
equipos estéreo. Shure lo cita en las videocámaras, **«an 1/8" stereo (tip-ring-sleeve) external microphone jack»**, y en los receptores de
monitores intraauriculares, cuya salida es un **«stereo (TRS) mini-phone jack»** con una señal desbalanceada
(**«effectively an unbalanced»**) apta para la mayoría de las entradas de línea (**«suitable for
most line level input devices»**).

## BNC

### El conector BNC y los 75 ohmios

El BNC es el conector coaxial de bayoneta del mundo del vídeo. En audio aparece en tres formatos del
tema: la AES/EBU por coaxial, el MADI por coaxial y el SDI con audio embebido. La norma de la AES/EBU
por coaxial lo define por su mecánica: **«The connector shall have mechanical characteristics
conforming to BNC as described in IEC 169-8, but may feature an impedance of 75 ohms.»** (SMPTE
276M, cláusula 8). La IEC 169-8 es, según el título con que la cita la propia 276M, la del BNC de 50 Ω (**«Characteristic
Impedance 50 Ohms (Type BNC)»**); la SMPTE admite la versión de 75 Ω.

### La AES/EBU por coaxial (SMPTE 276M)

La SMPTE normalizó la AES/EBU sobre coaxial para que el audio digital pudiera usar la
infraestructura de vídeo de un centro de televisión. Su alcance: **«a point-to-point coaxial cable
interface for the transmission of AES/EBU digital audio signals throughout television production and
broadcast facilities»**, compatible con **«analog video equipment, such as nonclamping distribution
amplifiers, switchers, cables, and connectors»**.

| | AES/EBU balanceada (EBU Tech 3250) | AES/EBU por coaxial (SMPTE 276M) |
|---|---|---|
| Circuito | Balanceado | **«unbalanced output circuit with a source impedance of 75 ohms»** |
| Cable | **«balanced and screened (shielded) with nominal characteristic impedance of 110 Ω»** | **«nominal characteristic impedance of 75 ohms over the frequency range 0.1 MHz to 6.0 MHz»** |
| Amplitud de salida | **«between 2 and 7 V peak-to-peak, when measured across a 110 Ω resistor»** | **«1.0 V ± 10%, when measured across a 75-ohm resistive load»** |
| Señal mínima en el receptor | Diagrama de ojo con **«Vmin of 200 mV»** | **«an eye-height level of 100 mV»** |
| Conector | XLR | BNC |
| Ecualización | **«there shall be no equalization before transmission»**; opcional en el receptor | **«Equalization for transmission cable losses is not usually required. When necessary, equalization shall be provided at the link receiver only.»** |

La amplitud de 1 V no es casual: la propia norma explica que la restricción se fija **«to ensure that
unbalanced coaxial AES/EBU signals can be routed successfully through nonclamping analog video
amplifiers»** (anexo A, informativo). Es decir, para que el audio pase por los distribuidores y
matrices de vídeo analógico como si fuera una señal de vídeo.

Pasar de una versión a otra exige un adaptador, no un simple cable: el anexo A trata la
**«conversion between coaxial and balanced twisted-pair transmission formats»**, es decir, redes de
adaptación **«for interfacing balanced 110-Ω circuits to unbalanced 75-Ω circuits»**, y remite a la
norma de la AES para esta variante: **«the reader's attention is drawn to AES 3ID»** (texto de la
AES no leído).

### El BNC en MADI y en SDI

- MADI: el coaxial es **«Coaxial via BNC, 75 Ohm, according to AES10-1991»** (RME). Se desarrolla en
  el epígrafe «MADI».
- SDI: la señal de vídeo digital, con su audio embebido, va por coaxial de 75 Ω con BNC. La norma de
  la capa física del SDI no se ha leído: es dato de oficio.

Aplicación práctica: el mismo cable BNC de 75 Ω sirve para vídeo SDI, para MADI y para AES/EBU
coaxial, y un panel de vídeo puede llevar cualquiera de las tres. Lo que no se puede es enchufar un
BNC de AES/EBU coaxial directamente en una entrada XLR de AES/EBU: hay que pasar por el adaptador de
75 a 110 Ω.

## Dante/AES67

El audio sobre red tiene tema propio (el 15: redes, sincronía, latencia, PTP y redundancia). Aquí se
estudia como conexión: qué cable y qué equipos pide, cómo se «enchufa» una señal, qué se puede
conectar con qué y qué avería da cada error.

### De la matriz a la red

| | Matriz clásica | Red IP |
|---|---|---|
| Límite | Duro: las entradas y salidas que tenga el bastidor | El ancho de banda |
| Cableado | Un cable por señal | Un cable por EQUIPO, con todas sus señales dentro |
| Cambiar un encaminamiento | Reconfigurar la matriz | Suscribirse al flujo desde el destino |
| Ampliar | Comprar más bastidor | Añadir un equipo a la red |

El precio de esa flexibilidad: una red no garantiza nada por sí sola. Hay que darle un reloj común,
hay que dimensionar su ancho de banda y hay que configurarla para que el audio no compita con el
resto del tráfico (oficio; se desarrolla en el tema 15).

### Qué es Dante

Dante es el sistema de audio en red de la casa Audinate: un protocolo que permite la transmisión de
señales de audio y control a través de una red Ethernet. Por la misma red viajan el audio y las
órdenes de encaminamiento, de configuración y de supervisión (oficio). El fabricante lo presenta así,
en tono comercial: **«Dante replaces all audio and video connections with a computer network,
effortlessly sending video or hundreds of channels of audio over slender Ethernet cables with perfect
digital fidelity.»** Es un sistema propietario, de una sola casa, no una norma.

Lo que en una matriz es un cruce, en Dante es una suscripción: **«Dante routing is performed by
associating a receiving (Rx) channel with a transmitting (Tx) channel. This is called
'subscription'.»** Los canales se nombran, no se numeran: **«Example: "Analog L@my-transmitter"
describes a channel named "Analog L" on a device named "my-transmitter".»** Y un aviso de operación:
**«If a device or channel is renamed, Dante routing considers it to be a different device or
channel.»** Renombrar un equipo en pleno montaje rompe sus suscripciones.

### Flujos: unicast y multicast

Dante agrupa los canales en flujos: **«Each flow carries several channels of audio, or one channel of
video from a transmitter to one or more receivers.»**

| | Unicast | Multicast |
|---|---|---|
| Qué es | **«point-to-point from a single transmitter to a single receiver»** | **«one-to-many from a single transmitter to any number of receivers»** |
| Canales por flujo | **«typically have room for 4 channels of audio or 1 channel of video»** | No se da una cifra |
| Ancho de banda | Una copia por destino (oficio) | **«consume network bandwidth even if there are no receivers, but do not require additional bandwidth to add more receivers»** |
| Quién lo crea | Se crea con la suscripción | **«must be set up on the transmitting Dante device before receivers can subscribe to these flows»** |
| Por defecto | **«Dante routing is unicast by default.»** | **«Dante receivers will automatically prefer multicast to unicast if it is available.»** |

La cifra de cuatro canales lleva el matiz «typically» (habitualmente) de la fuente. Con ella, diez
canales en unicast necesitan tres flujos: cuatro, cuatro y dos (cálculo).

### Qué se puede conectar con qué

Una suscripción sólo se establece entre canales del mismo formato: **«It is only possible to set up a
subscription between channels which have a common media format.»** Y un equipo trabaja en un solo
formato a la vez: **«Devices can usually be switched between media formats, but will not support
more than one at a time.»** La guía de Audinate da los mensajes de error más comunes, que son las
averías de conexión típicas:

| Mensaje | Causa según Audinate |
|---|---|
| **«Incorrect channel format: source and destination channels do not match»** | **«The receiver and transmitter are set to different sample rates.»** |
| **«Mismatched clock domains»** | **«One of the devices is configured with sample rate pull-up/down that does not match the other device.»** |
| **«Tx Scheduler failure»** | **«This is typically because you are trying to use sub-millisecond latency over a 100 Mbps network link (1 msec is the minimum supported latency over 100 Mbps links).»** |

Aplicación práctica: si un canal Dante aparece en gris y no deja suscribirse, lo primero es comprobar
que emisor y receptor están a la misma frecuencia de muestreo.

### La latencia

En Dante la latencia no es casual: se configura en el receptor. **«Each receiver has a device latency
setting. This setting defines the latency between the timestamps on the incoming audio samples and
when those samples are played out.»**

- Valor habitual: **«The typical default latency for a Dante audio device is 1 msec. This is
  sufficient for a very large network, consisting of a Gigabit network core (with up to 10 hops
  between edge switches) and 100 megabit links to Dante devices.»**
- Mínimo: **«Smaller, Gigabit-only networks can use lower values of latency (down to 150 µsec for very
  fast devices, such as PCIe cards).»** Con un puerto de 100 Mbps, el mínimo es 1 ms.
- Si no coinciden: **«If the transmitter and receiver have different latency settings, Dante will use
  the higher of the two as the effective flow latency.»** Es la latencia de cada flujo, no la de todo
  el sistema.

### El reloj y la redundancia, en lo que tocan a la conexión

- Reloj: **«All Dante-enabled devices use the IEEE 1588 Precision Time Protocol (PTP) across the
  network to synchronize their local clocks to a leader clock, providing sample-accurate time
  alignment throughout the network.»** Uno de los equipos se elige como reloj principal (*leader*),
  y en esa elección **«Devices with clock inputs (e.g. Word Clock or AES3) will be preferred»**. La
  versión: **«By default, Dante devices use PTPv1. However, when RTP is enabled for a device, it also
  uses PTPv2»**, y **«AES67 and ST 2110-30 require PTPv2»**. El detalle de PTP, en el tema 15.
- Redundancia: los equipos que la admiten tienen dos puertos de red, primario y secundario. **«If
  redundancy is being used, secondary interfaces should be connected to a second separate network.
  Secondary interfaces cannot communicate with primary interfaces.»** **«The same media data is
  transmitted on both the primary and secondary networks simultaneously. In the event of a failure on
  one network, media will continue to flow via the other network.»** Dos reglas de cableado: los dos
  puertos a la misma velocidad (**«connected using the same link speed»**) y **«Dante devices that do
  not support redundancy must be connected to the primary network only.»**

Aplicación práctica: cablear el puerto secundario de un equipo al mismo conmutador que el primario no
da redundancia; la red secundaria tiene que ser otra red.

### El cable y el conmutador

Dante viaja sobre Ethernet, por la red de cable de pares con conector RJ45 o por fibra de red, a 100
Mbps o a gigabit por puerto. Audinate da preferencia al gigabit (en la elección del reloj, **«A
gigabit connected device is preferred over a device connected via 100Mbps»**) y señala como causas de
pérdida de sincronía **«Poorly-implemented EEE (Energy Efficient Ethernet)»** y **«Overloaded network
links»**.

No vale cualquier conmutador. Una red Dante pide conmutadores gestionables, con calidad de servicio
para dar prioridad al audio, con soporte de PTP y, si se usa multicast, con control de suscripciones
(oficio). La calidad de servicio se marca en cada paquete: **«The DSCP is a field in the IP packet
header used to classify and prioritise network traffic (Quality of Service, or QoS).»**

El límite de unos 100 m por tramo de cable de cobre es el de Ethernet, y en la práctica se usan
cables de categoría 5e o 6; la norma de cableado estructurado no se ha leído y el dato va como
oficio.

### Por qué UDP y cuánto ocupa un canal

El audio en tiempo real viaja en paquetes UDP, no TCP. En la televisión sobre IP lo exige la SMPTE
ST 2110-10:2022 (6.2): **«All RTP Streams shall be transported on UDP as specified in IETF RFC 768.»**
La comparación que sigue es de oficio; los límites de tamaño del paquete UDP, en el tema 15:

| | TCP | UDP |
|---|---|---|
| Qué hace si un paquete se pierde | Lo PIDE otra vez y espera | Sigue adelante |
| Garantiza la entrega | Sí | No |
| Retardo | Variable, y puede crecer mucho | Bajo y predecible |
| Sirve para audio en tiempo real | NO | SÍ |

El razonamiento: en audio en directo, un paquete que llega tarde es tan inútil como uno que no
llega. Ese instante de sonido ya pasó.

La cuenta del caudal:

> Caudal de un canal = frecuencia de muestreo × profundidad de bits

A 48 kHz y 24 bits, un canal son 1,152 megabits por segundo. Ése es el número que hay que tener.
Para 32 canales en los dos sentidos:

1. Un canal: 48.000 × 24 = 1,152 Mbps.
2. Treinta y dos canales: 1,152 × 32 = 36,9 Mbps.
3. Bidireccionales: ×2 = 73,7 Mbps.

Es el caudal del audio en crudo. El de la red es mayor: cada paquete lleva sus cabeceras de
Ethernet, IP y UDP, y en audio en tiempo real los paquetes son pequeños y frecuentes, así que la
proporción de cabecera es alta. Es un recargo que en las cuentas de red de audio nunca se puede
despreciar.

### AES67 y la ST 2110-30

La AES67 es la norma abierta. Audinate la define: **«AES67 is an open standard for audio-over-IP
interoperability, allowing devices from different manufacturers to exchange audio streams.»** Y la
norma de la SMPTE para audio en las instalaciones de televisión sobre IP se apoya en ella: **«SMPTE
ST 2110-30 is a broadcast industry standard for transporting audio over IP networks, building on
AES67 with additional requirements for clocking and network configuration.»**

- ST 2110-30:2025, alcance: **«This standard specifies the real-time, RTP-based transport of PCM
  digital audio streams over IP networks by reference to AES67.»** Y el límite: **«Non-PCM digital
  audio signals including compressed audio signals are outside the scope of this standard.»** La
  edición vigente de esta parte es la de 2025, que revisa la de 2017.

La ST 2110-30 obliga a seguir la AES67 (**«Digital audio streams shall conform to AES67»**) y cita
como edición la **«AES67-2023»**; el texto de la AES67 es de pago y no se ha leído. Lo que la ST
2110-30 fija por sí misma:

- Frecuencia de muestreo (6.1): **«All senders and receivers of PCM digital audio conforming to this
  standard shall support a digital audio sampling rate of 48 kHz, and should support digital audio
  sampling rates of 44.1 kHz, or 96 kHz, or both. Other sampling rates are out of scope.»** 48 kHz es
  obligatoria («shall»); 44,1 y 96 kHz, recomendadas («should»).
- Niveles de conformidad de los emisores (tabla 2), con el nivel A como mínimo común: **«All senders
  and receivers shall be compliant to Level A as defined in this document.»**

| Nivel | Frecuencia | Tiempo de paquete | Canales |
|---|---|---|---|
| A | 48 kHz | 1.000 µs | 1 a 8 |
| AX | 96 kHz | 1.000 µs | 1 a 4 |
| B | 48 kHz | 125 µs | 1 a 8 |
| BX | 96 kHz | 125 µs | 1 a 8 |
| C | 48 kHz | 125 µs | 9 a 64 |
| CX | 96 kHz | 125 µs | 9 a 32 |

La tabla es la de los emisores, que cumplen con **«at least one channel count»** del intervalo. La de
los receptores (tabla 3) es más amplia, y el receptor debe admitir **«all possible combinations»** de
frecuencia, tiempo de paquete y canales que da para su nivel; así, el receptor de nivel C recibe **«1 to 8»**
canales a 1.000 µs y **«1 to 64»** a 125 µs, no sólo de 9 a 64.

- El paso desde SDI: la norma recuerda que **«SDI allows the carriage of at least 16 embedded audio
  channels»** y que, para seguir en el nivel A (hasta 8 canales por flujo), el emisor puede repartirlos
  **«into multiple AES67 streams»**. Y tiene un símbolo para ello en su convenio de orden de canales:
  «SGRP», **«One SDI audio group»**, cuatro canales.

Dante y AES67 no son alternativas excluyentes: Dante puede mandar flujos AES67. Audinate: **«Multicast
flows can carry Dante audio, or RTP audio (AES67 or ST 2110-30).»** Con dos cautelas: esos flujos
necesitan PTPv2, y **«Avoid mixing AES67 and ST 2110-30 modes on the same network unless you
understand the implications for clocking and compatibility.»**

## MADI

### Qué es el MADI

El MADI es la interfaz multicanal de la AES, la AES10. Su texto es de pago y no se ha leído; lo que
sigue sale de dos fabricantes que la aplican, RME y DiGiCo. RME lo explica desde la AES/EBU:
**«MADI, the serial Multichannel Audio Digital Interface, has been defined already in 1989 as an
extension of the existing AES3 standard»**. **«Simply put, MADI contains 28 of those AES/EBU signals
in serial, i. e. after one another, and the sample rate can still even vary by +/-12.5%. The limit
which cannot be exceeded is a data rate of 100 Mbit/s.»** Veintiocho señales AES/EBU de dos canales
son 56 canales (cálculo).

El modo de 64 canales vino después: **«Because an exact sampling frequency is used in most cases, the
64 channel mode was introduced officially in 2001. It allows for a maximum sample rate of 48 kHz +
ca. 1%, corresponding to 32 channels at 96 kHz, without exceeding the maximum data rate of 100
Mbit/s. The effective data rate of the port is 125 Mbit/s due to additional coding.»**

DiGiCo lo resume así: **«The MADI or AES-10 Standard, originated in the 1980's to support serial
digital transmission of up to 64 channels of digital audio over coaxial or fibre optic cable at
sampling rates of up to 96K with a resolution of up to 24 bits per channel.»** Sobre la fecha de los
64 canales, las dos fuentes no coinciden: RME habla de 2001 y DiGiCo de revisiones de la norma
**«in 2003 and again in 2008 adding 64 channel and 96KHz sample rates support»**. Sin el texto de la
AES10, el tema no decide.

| Modo | Canales | Frecuencia |
|---|---|---|
| 56 canales (el original) | 56 | RME no da frecuencia base: dice que puede variar ±12,5 %; DiGiCo lo trabaja a 48 kHz (**«Standard MADI at 48K»**) |
| 64 canales | 64 | Hasta 48 kHz + 1 % |
| 64 canales a doble frecuencia | 32 | 96 kHz |

### Por coaxial y por fibra

| | Coaxial | Fibra óptica |
|---|---|---|
| Conector | **«Coaxial via BNC, 75 Ohm, according to AES10-1991»** | **«Optical via FDDI duplex SC connector»**; SC, no ST: **«Please don't mix them up with ST connectors»** |
| Cable | Coaxial de 75 Ω; DiGiCo suministra cable **«standard 75 ohm BNC»** del tipo RG59U, **«basically a good quality video connection cable»** | **«The cables have an internal fibre of only 50 or 62.5 µm diameter and a coating of 125 µm»** (fibras 50/125 y 62,5/125), y **«these are always (!) glass fibre cables»** |
| Alcance | **«distances of up to 100 meters using coaxial cables»**, que RME atribuye a la ecualización y a las entradas de alta sensibilidad de su conversor | **«The transmission uses the multimode technique which supports cable lengths of up to almost 2 km.»** |
| Nivel | Salida **«around 400 mVpp when terminated with 75 Ohm»**; entrada **«error-free from about 180 mVpp»** (equipo de RME) | Luz de **«1300 nm»**, invisible |

Así, el MADI óptico estándar es multimodo. RME distingue la otra fibra: **«Single mode allows for
much longer distances, but it uses a completely different fibre (8 µm).»** La de plástico no sirve:
**«Plastic fibre cables (POF, plastic optical fibre) can not be manufactured in such small
diameters.»** Y la fibra da algo que el coaxial no: RME destaca de la interfaz óptica su
**«complete galvanic separation»**, la separación eléctrica completa entre los dos equipos.

Esa separación importa por lo que DiGiCo advierte del coaxial: **«MADI is approximately 0.5V RMS
125MHz serial data. Earth (ground) differentials of over 0.25V due to poor power wiring will
effectively stop the system from functioning.»** Una diferencia de potencial de masa de más de un cuarto
de voltio entre dos equipos basta para tirar un enlace MADI coaxial. Y sobre la distancia, la misma nota
matiza: **«The maximum distance that a MADI signal can be sent is dependent on the performance of both
the cable and the equipment being connected.»**

### Por qué dos equipos MADI pueden no entenderse

Que dos equipos tengan MADI no garantiza que se entiendan. Hay que casar dos cosas:

1. El número de canales. RME: **«Older devices understand and generate only the 56 channel format.
   Newer devices often work in the 64 channel format, but offer still no more than 56 audio
   channels.»** Y al revés, DiGiCo avisa de que **«some 3rd party MADI interfaces will not accept a 56
   channel MADI connection as valid, although this is within the AES-10 specification.»**
2. El modo a 96 kHz. DiGiCo describe dos, con nombres que varían según la casa: **«S-MUX (48K Frame)
   and Hi-Speed (96K Frame)»**, y advierte: **«These modes are not compatible.»** Los dos llevan el
   mismo caudal y ordenan las muestras de otra manera; si no coinciden, **«audio will appear on the
   wrong channels on the receiving device.»** En la consola de DiGiCo, además, 96 kHz para 56 o 64
   canales exige dos puertos MADI: **«You need 2 pairs of cables to connect for 56 or 64 channels of
   audio.»**

Aplicación práctica: si al conectar una mesa a un grabador por MADI el audio llega a canales
equivocados a 96 kHz, lo primero es comprobar que los dos extremos usan el mismo modo (S/MUX o
alta velocidad); si no llega nada, que el receptor acepta el formato de 56 o 64 canales que manda el
emisor.

### Cómo se protege un enlace MADI

El MADI es una conexión PUNTO A PUNTO por un solo cable. Sesenta y cuatro canales viajan por ese
cable, y si se corta, se caen los sesenta y cuatro. La única protección real es tener un segundo
camino físico (oficio). Los equipos lo prevén con puertos duplicados; DiGiCo, por ejemplo, habla de
**«redundant MADI port connections, marked 1A and 1B»** en algunas de sus consolas.

Las soluciones de una red no sirven aquí: el MADI no usa PTP, no es una red conmutada y no tiene
topología que configurar. Una interfaz dedicada y una red no se protegen igual. La primera se
duplica; la segunda se configura.

## AES/EBU

### Qué es

La AES/EBU es la interfaz digital de dos canales de audio que la AES publica como AES3 y la EBU en su
Tech 3250. La EBU define su alcance: **«serial digital transmission of two channels of periodically
sampled and linearly represented digital audio data in a broadcasting complex, up to a distance of a
few hundred metres»**. Y señala la frecuencia de trabajo en radiodifusión: **«it is intended that the interface
be primarily used at 48 kHz, as this is the recommended sampling frequency for use in broadcasting
studios (CCIR Recommendation 646).»**

Los dos canales pueden usarse de varias maneras (Tech 3250, apartado 2.2): dos canales independientes, un
par estéreo (**«The left or "A" channel is in sub-frame 1 and the right or "B" channel is in
sub-frame 2»**), un solo canal, o un canal principal y otro secundario.

### La estructura: subtrama, trama y bloque

- Subtrama: **«Each sub-frame is divided into 32 time slots, numbered from 0 to 31»**. Lleva una
  muestra de un canal.
- Trama: **«A frame is uniquely composed of two sub-frames»**, una por canal.
- Bloque: **«The block is a group of 192 consecutive frames.»** Lo marca el preámbulo Z, que aparece
  **«once every 192 frames»**.

| Intervalos de la subtrama | Qué llevan |
|---|---|
| 0 a 3 | El preámbulo (X, Y o Z), que sincroniza e identifica subtrama y bloque |
| 4 a 27 | La muestra de audio, con el bit más significativo en el 27: 24 bits; o 20 bits en los intervalos 8 a 27, y los 4 a 7 como bits auxiliares |
| 28 | Validez (V) |
| 29 | Datos de usuario (U) |
| 30 | Estado del canal (C) |
| 31 | Paridad (P) |

El bit de estado del canal, uno por subtrama, se va acumulando a lo largo del bloque y forma un
mensaje por canal. Lleva, entre otras cosas, **«length of audio sample words, number of audio
channels, sampling frequency, time code, alphanumeric source and destination codes, and
pre-emphasis»**. Su longitud es de 192 bits: la Tech 3250 habla de **«The channel status clock format
of 192 bits»** y lo divide en 24 bytes (24 × 8 = 192). En otro pasaje la misma edición escribe
«92-bit blocks», que es una errata.

Cada trama lleva una muestra de cada canal y tiene 64 intervalos (dos subtramas de 32), y **«The rate
of transmission of frames corresponds exactly to the source sampling frequency»**: a 48 kHz salen
48.000 tramas por segundo, es decir, 64 × 48.000 = 3,072 millones de intervalos por segundo
(cálculo).

### Las características eléctricas

Todas de la Tech 3250, capítulo 6:

| Parámetro | Valor |
|---|---|
| Base | **«ITU-T Recommendation V.11»**, que permite **«distances of up to a few hundred metres»** |
| Cable | **«balanced and screened (shielded) with nominal characteristic impedance of 110 Ω»** |
| Emisor | Salida balanceada con **«an internal impedance of 110 Ω ± 20%»** |
| Amplitud | **«between 2 and 7 V peak-to-peak, when measured across a 110 Ω resistor»** |
| Receptor | **«110 Ω ± 20%»** |
| Señal mínima | Diagrama de ojo con **«Vmin of 200 mV»** |
| Modo común | Sin errores con **«a common mode signal of up to 7 V peak at frequencies from DC to 20 kHz»** |
| Fluctuación propia de la salida | **«less then 0,025 UI»** (sic) |

Tres reglas de conexión salen de ahí:

1. Un receptor por línea: **«The application of more than one receiver to any one line might create
   transmission errors due to the resulting impedance mismatch.»** Para mandar una señal AES/EBU a
   varios equipos se usa un distribuidor, no un cable en Y (oficio).
2. La ecualización, sólo en el receptor: **«there shall be no equalization before transmission»**, y
   en el receptor es opcional **«to enable interconnecting cable longer than 100 m to be used»**.
3. El cable, de 110 Ω: un cable de micrófono no garantiza esa impedancia (epígrafe «Los cables y sus
   impedancias»).

### AES/EBU por cable de red

La Tech 3250 admite en su apéndice 2 llevar la AES/EBU por cableado estructurado de categoría 5:
**«the practice has been shown to be viable on Category 5 unscreened pairs, meeting EMI
requirements, and offering transmission up to 400 metres overall unequalised, or 800 metres
equalised, at 48 kHz frame rate.»** Con dos condiciones: el mismo tipo de cable en todo el recorrido
(todo sin apantallar o todo apantallado) y, con conectores RJ45, **«current practice favours the use
of pins 4 and 5 for AES/EBU signals»**, con los 3 y 6 como segundo par. Para los adaptadores, la
sugerencia es unir **«XLR Pin 2 should be connected to RJ45 Pin 5»** y **«XLR Pin 3 should be connected to RJ45 Pin 4»**.

Aplicación práctica: si una señal AES/EBU llega con cortes intermitentes, se comprueba, por este
orden, que el cable es de 110 Ω, que no hay dos receptores colgados de la misma línea y que emisor y
receptor están a la misma frecuencia o sincronizados a la misma referencia (oficio).

## ADAT

### Qué lleva y por dónde

El ADAT óptico es una interfaz de fabricante, no de un organismo de normalización: RME la describe
como **«TOSLINK, according to Alesis specification»**. Su capacidad, según el mismo fabricante:
**«ADAT optical carries 8 channels of 24 bit audio at up to 48 kHz sample rate, 4 channels at up to 96
kHz, and 2 channels at up to 192 kHz. Transmission is done via a single optical line (TOSLINK). The
length of the optical cable is limited to about 10 m.»**

| Frecuencia | Canales por cable | Cómo |
|---|---|---|
| Hasta 48 kHz | 8 | Normal |
| Hasta 96 kHz | 4 | S/MUX: **«8 x 4 channels 24 bit / 96 kHz»** en un equipo de ocho puertos |
| Hasta 192 kHz | 2 | S/MUX4: **«8 x 2 channels 24 bit / 192 kHz»** |

La razón de que los canales se dividan: **«As ADAT optical is restricted to 48kHz, in DS mode (Double
Speed) two channels are being used for the transmission of one channel's data.»** Cada canal de 96
kHz ocupa dos de 48 kHz.

### El aviso práctico: el S/MUX no se detecta solo

**«Because the Sample Split (S/MUX, S/MUX4) format doesn't contain a coding, the ADI-648 cannot
distinguish it from normal (44.1/48 kHz) material.»** El receptor no sabe si le llegan ocho canales
de 48 kHz o cuatro de 96 kHz repartidos en ocho: hay que ajustarlo a mano en los dos extremos. Si no
se hace, el audio llega por canales que no le corresponden.

Frente a los demás formatos del tema, el ADAT es el de menor alcance (unos 10 m) y el propio de
equipos de estudio próximos entre sí; para distancias de sala a sala se usa MADI o red (oficio). Un
conversor como el ADI-648 de RME pasa de uno a otro: reparte **«64 MADI channels»** en **«8 ADAT
optical outputs (TOSLINK)»**.

## SDI

### El audio embebido en SDI

La interfaz digital serie (SDI) lleva la señal de vídeo por un coaxial y, además de la imagen, tiene
espacios de datos auxiliares donde cabe el audio. Tres normas de la SMPTE fijan cómo:

| Norma | Para qué SDI | Canales | Muestra |
|---|---|---|---|
| SMPTE 272M-2004 | Definición estándar (ANSI/SMPTE 259M o SMPTE 344M) | **«a minimum of two audio channels and a maximum of 16 audio channels»** (cuatro como máximo en digital compuesto) | 20 bits por defecto; 24 como opción |
| SMPTE ST 299-1:2009 | Alta definición (SMPTE 292) | Hasta 16 a 32, 44,1 o 48 kHz; hasta 8 a 96 kHz | 24 bits |
| SMPTE ST 299-2:2010 | Formatos de imagen sobre interfaz de 3 Gb/s (nivel A) | Los canales **«numbered from 17 to 32»**: hasta 32 a 32, 44,1 o 48 kHz; hasta 16 a 96 kHz | 24 bits |

Las citas que sostienen la tabla:

- SD (272M): mapea **«AES digital audio data, AES auxiliary data, and associated control information
  into the ancillary data space of serial digital video conforming to ANSI/SMPTE 259M or SMPTE
  344M»**. **«The minimum, or default, operation of this standard supports 20 bits of audio data»**, y
  como opción **«24-bit audio or four bits of AES auxiliary data»**.
- HD (ST 299-1): **«the mapping of 24-bit AES digital audio data and associated control information
  into the ancillary data space of a serial digital video conforming to SMPTE 292»**, y **«Audio
  channels are transmitted in groups of four, up to a maximum of 16 audio channels in the case of 32
  kHz, 44.1 kHz or 48 kHz sampling, and up to a maximum of 8 audio channels in case of 96-kHz
  sampling.»**
- Interfaz de 3 Gb/s (ST 299-2): su título es **«Extension of the 24-Bit Digital Audio Format to 32
  Channels for 3 Gb/s Bit-Serial Interfaces»**; define paquetes **«for identifying audio channels numbered from 17 to 32,
  beyond the 16 channels defined in SMPTE ST 299-1»**; cada grupo ampliado lleva **«up to four 24-bit
  audio channels with 32, 44.1, or 48-kHz sample rates, or up to two 24-bit audio channels with
  96-kHz sample rate»**, para llegar a 32 canales en **«the video source image formats mapped to a 3 Gb/s
  Level A serial data interface»**. El SDI de alta definición a 1,5 Gb/s (SMPTE 292) se queda en los 16
  de la ST 299-1.

Un aviso de nombre: la norma de HD se citaba antes como SMPTE 299M; su denominación actual es SMPTE
ST 299-1 (el documento consta como **«Document renumbered July 21, 2010»**).

### Grupos, pares y espacio auxiliar

El audio embebido se organiza en grupos de cuatro canales. La 272M: **«Audio channels are transmitted
in pairs combined, where appropriate, into groups of four. Each group is identified by a unique
ancillary data ID.»** Y la numeración: **«Channels 1 through 4 are in group 1, channels 5 through 8
are in group 2, and so on.»**

| Grupo | Canales | Pares AES/EBU |
|---|---|---|
| 1 | 1 a 4 | Dos |
| 2 | 5 a 8 | Dos |
| 3 | 9 a 12 | Dos |
| 4 | 13 a 16 | Dos |

Cada par de canales corresponde a una señal AES/EBU (el audio embebido **«derived from AES3»**, dice
la 272M), así que 16 canales son ocho pares (cálculo).

Dónde va dentro de la señal en HD: **«Audio data packets are multiplexed (embedded) into the
horizontal ancillary data space of the Cb/Cr data stream, and audio control packets are multiplexed
into the horizontal ancillary data space of the Y data stream.»** (ST 299-1, 1.4). Es decir, en el
espacio auxiliar horizontal (HANC), el intervalo que la señal deja en cada línea fuera de la imagen
activa.

### El reloj del audio embebido

El audio embebido va atado al vídeo. Las dos normas prefieren audio síncrono: **«Audio sampled at 48
kHz and clock locked (synchronous) to video is the preferred implementation for intrastudio
applications»** (272M) y, en HD, **«Audio sampled at a clock frequency of either 48 kHz or 96 kHz
locked (synchronous) to video, is the preferred implementation for intrastudio applications»** (ST
299-1). Como opción admiten audio de 32 a 48 kHz síncrono o asíncrono.

Aplicación práctica: una fuente de audio que no esté enganchada a la referencia de vídeo del centro
necesita un conversor de frecuencia de muestreo antes del embebedor, y ese paso tiene su coste (ver
«Conversiones»).

### Audio no PCM embebido

El SDI no sólo lleva audio lineal: la ST 299-1 admite en el par AES **«linear PCM audio or non-PCM
data formatted according to SMPTE 337»**, y en su anexo A aclara que esos datos **«may include
compressed (bit-rate reduced) audio or other types of non-audio data»**. Es el caso del Dolby E, audio con
reducción de caudal que viaja en un par AES/EBU (tema 14).

La norma da dos cautelas, como recomendación («should») y en parte en un anexo informativo, que el
operador de sonido tiene que conocer:

- Nada de conversión de frecuencia: **«when the AES audio data contains SMPTE 337 formatted data the
  use of sample rate conversion will corrupt the SMPTE 337 data»**. Recomienda **«that operation be
  restricted to 48-kHz synchronous modes when SMPTE 337 data is present»**.
- Nada de procesado PCM: la norma recomienda desactivarlo o puentearlo porque **«such processing will corrupt the
  SMPTE 337 data»**, y pone ejemplos: **«gain changes, sample rate conversion, truncation, dithering,
  cross-fades, etc.»**

Aplicación práctica: un par embebido con Dolby E no se pasa por un canal de mesa con ganancia ni por
un conversor de frecuencia; se lleva entero, bit a bit, hasta el decodificador. Y la norma avisa de
que **«not all devices compliant with the standard will properly handle SMPTE 337 data»**.

### Del SDI a la red

En las instalaciones sobre IP, el audio sale del SDI y viaja como flujos AES67/ST 2110-30. La ST
2110-30 prevé el paso: el grupo SDI de cuatro canales tiene su símbolo («SGRP») y, para seguir en el
nivel A, los 16 canales se reparten en varios flujos (epígrafe «AES67 y la ST 2110-30»). La capa
física del SDI (normas 259M y 292) no se ha leído.

## Embebido y desembebido

### Qué es embeber y desembeber

| Operación | Qué hace | Aparato |
|---|---|---|
| Embeber | Meter pistas de audio dentro de la señal de vídeo | Embebedor (*embedder*) |
| Desembeber | Sacarlas de la señal de vídeo | Desembebedor (*de-embedder*) |

En la práctica el mismo aparato hace las dos cosas (oficio). La ST 299-1 nombra así los dos lados:
**«multiplexing (embedding) and demultiplexing (receiving) devices»**.

La función de un embebedor situado en un control central técnico de televisión es extraer o insertar
audios en una señal de vídeo.

Hay tres aparatos de un control central con los que se confunde. Lo que separa al embebedor de los
tres es que no mueve señales entre sitios: mueve audio dentro de una señal. Es una operación de
formato, no de encaminamiento.

| Lo que no hace | Qué aparato lo hace |
|---|---|
| Multiplexar señales procedentes de una señal satélite | Un demultiplexor de transporte, en la recepción de satélite |
| Multiplexar señales procedentes de codificadores IP | Un multiplexor de transporte sobre red |
| Enrutar señales hacia los controles de realización | La matriz de conmutación |

Y por qué importa en la práctica: una señal que llega de fuera puede traer su audio embebido en
pistas que no coinciden con las del centro. El embebedor las reordena, y sin ese paso el programa sale
con el sonido en el canal equivocado.

### Dónde se embebe y se desembebe

En una instalación de televisión con SDI, el audio entra y sale del vídeo en varios puntos (oficio):

| Punto | Qué se hace | Para qué |
|---|---|---|
| Cámaras y enlaces de exteriores | La señal llega con el sonido de la cámara o del reportero embebido | Tema 8: el sonido que llega de las cámaras |
| Entrada al control de sonido | Se desembebe y se lleva a la mesa (por AES/EBU, MADI o red) | Que cada fuente sea un canal de la mesa |
| Salida del control de sonido | La mezcla se embebe en el programa | Que el vídeo del programa salga con su sonido |
| Control central | Se reordenan, sustituyen o insertan pistas | Adaptar lo que llega o sale al reparto del centro |

Hay mesas de sonido y mezcladores de vídeo que integran el embebedor y el desembebedor en sus
tarjetas de entrada y salida; otros necesitan un aparato aparte (oficio).

### Conversiones y compatibilidad

| Conversión | Qué hay que vigilar |
|---|---|
| Analógico ↔ digital | El nivel de referencia: qué dBu equivalen a qué dBFS. No hay una equivalencia universal |
| AES3 ↔ SDI incrustado | El reloj: el audio incrustado va atado a la referencia de vídeo |
| MADI ↔ Dante | Reloj y latencia: son dos mundos con dos relojes, y hay que decidir cuál manda |
| Frecuencia de muestreo distinta | Un conversor de frecuencia de muestreo, que introduce latencia y, si es barato, degradación |

En una instalación mixta, lo que más falla no es el formato de los datos sino el reloj: la
conversión de datos es fácil; la de tiempo, no (oficio). Las excepciones las da este mismo tema: los
modos de MADI y de ADAT a 96 kHz, que hay que casar a mano, y el audio no PCM, que no admite conversión
de frecuencia.

### Un supuesto práctico

Una unidad móvil manda al centro una señal HD-SDI con 16 canales embebidos. El reparto previsto es:
canales 1 y 2, la mezcla de programa en estéreo; 3 y 4, el sonido internacional; 5 a 8, micrófonos
de reportero. El control de sonido recibe la señal y la mesa sólo admite entradas MADI.

1. Desembeber los 16 canales (cuatro grupos, ocho pares AES/EBU) y llevarlos a la mesa, por ejemplo
   con un desembebedor con salida MADI o un conversor a AES/EBU y de ahí a MADI.
2. Comprobar el reparto de pistas con quien envía antes del directo: si el internacional llega en 1 y
   2 y el programa en 3 y 4, se reordena en el desembebedor o en la mesa, no sobre la marcha.
3. Comprobar el reloj: la señal debe estar enganchada a la referencia del centro. Si llega sin
   sincronizar, el sincronizador o un conversor de frecuencia la ajusta; si alguno de los pares lleva
   Dolby E, ese par no se convierte ni se procesa: va directo al decodificador (tema 14).
4. Si el directo lleva retorno al reportero, la mezcla N-1 sale de la mesa y se embebe en la señal de
   retorno o se envía por otra vía (tema 8).
5. Medir la sonoridad y los niveles antes de dar paso (tema 13).

## Normas técnicas que el tema cita

El tema no cita normas legales. Las normas técnicas, en la edición leída:

| Norma | Qué se toma | Edición |
|---|---|---|
| EBU Tech 3250-E, *Specification of the digital audio interface (The AES/EBU interface)* | Alcance, 48 kHz, subtrama, trama y bloque, estado del canal, código bifase, características eléctricas, conector XLR y su patillaje, rotulado DI/DO, apéndice 2 (categoría 5 y RJ45) | 3.ª ed., 2004 |
| ANSI/SMPTE 276M-1995, AES/EBU por coaxial | Alcance, generador de 75 Ω y 1 V, receptor, ecualización, cable, conector BNC, anexo A | Aprobada el 1-12-1995; la biblioteca de la SMPTE la da como «stabilized» |
| SMPTE 272M-2004, audio AES en el espacio auxiliar del SDI de definición estándar | Alcance, 48 kHz síncrono, 20 y 24 bits, 2 a 16 canales, grupos | 2004; «stabilized» |
| SMPTE ST 299-1:2009, audio de 24 bits en el SDI de alta definición | Alcance, datos SMPTE 337, 48 y 96 kHz, grupos de cuatro y 16 u 8 canales, HANC, anexo A (datos no PCM) | Aprobada el 29-5-2009, renumerada el 21-7-2010; «active» |
| SMPTE ST 299-2:2010, canales 17 a 32 en interfaces de 3 Gb/s | Canales ampliados, título | Aprobada el 21-7-2010; «stabilized» |
| SMPTE ST 2110-10:2022, tiempos y definiciones del sistema | Transporte de los flujos RTP sobre UDP (6.2) | Aprobada el 28-3-2022; revisa la de 2017; «active» |
| SMPTE ST 2110-30:2025, audio PCM sobre IP | Alcance, conformidad con AES67 (edición citada AES67-2023), 48 kHz obligatoria, niveles de conformidad, nota sobre SDI y símbolo SGRP | Aprobada el 1-10-2025; revisa la de 2017 |

Se nombran sin haberlas leído (son de pago o no se han descargado): AES3, AES10, AES67, AES3-id, IEC
60268-12 (conector XLR), IEC 169-8 (BNC), las normas de capa física del SDI (SMPTE 259M y 292), la SMPTE 425 (interfaz de 3 Gb/s) y
la norma de cableado estructurado.

## Lo que este tema no da, y dónde está

- El texto de las normas de la AES (AES3, AES10 del MADI, AES67): son de pago. La AES/EBU va con la
  Tech 3250 de la EBU; el MADI, con la documentación de RME y DiGiCo; la AES67, a través de la ST
  2110-30 y de Audinate. Por eso no se da la frecuencia máxima de la AES67 ni el año exacto en que
  la AES10 incorporó los 64 canales (las dos fuentes de fabricante discrepan).
- La capa física del SDI (amplitud, alcance por tipo de cable) y la norma de cableado estructurado
  (longitud máxima de un tramo de cobre, categorías): no leídas; el tema da los 75 Ω del SDI y los
  100 m de Ethernet como oficio.
- Las medidas del jack pequeño (3,5 mm) y la norma del jack: sin fuente leída. El reparto de los
  contactos de los jacks de cuatro contactos (TRRS, auriculares con micrófono): tampoco.
- De qué material es la fibra del TOSLINK: no consta en las fuentes leídas.
- La alimentación *phantom* y la A-B, la masa y los bucles de masa, el mecanismo del balanceado y el
  jack TS con equipos balanceados: tema 2. Los micrófonos: tema 3.
- El audio sobre IP en detalle (PTP y su perfil SMPTE, redundancia ST 2022-7, QoS y dimensionado de
  la red), y la sincronía de una instalación (*word clock*, referencia de vídeo): tema 15; la
  sincronía en la estación de trabajo, tema 9.
- El Dolby E, sus tramas y su retardo: tema 14. El sonido que llega de las cámaras, los retornos y el
  N-1: tema 8. La sonoridad y los niveles: tema 13.
- Lo propio de CSRTV (equipamiento de sus controles, formato de sus mesas, red de audio, reparto de
  pistas embebidas): no consta en un documento publicado localizado.

## Trazabilidad

Fuentes leídas el 25/09/2026. El tema no cita normas legales.

| Fuente | Qué sostiene |
|---|---|
| EBU Tech 3250-E, 3.ª ed., 2004 (https://tech.ebu.ch/docs/tech/tech3250.pdf) | Todo el epígrafe «AES/EBU»; el XLR en digital (conector, macho y hembra, pines, polaridad indiferente, DI/DO); los 110 Ω |
| ANSI/SMPTE 276M-1995 (https://pub.smpte.org/doc/st276/) | El BNC de 75 Ω y la AES/EBU por coaxial; la tabla comparada; la referencia a AES 3ID |
| SMPTE 272M-2004 (https://pub.smpte.org/doc/st272/) | Audio embebido en SD: alcance, bits, canales, grupos, reloj preferido |
| SMPTE ST 299-1:2009 y ST 299-2:2010 (https://pub.smpte.org/doc/st299-1/ y /st299-2/) | Audio embebido en HD: canales, grupos, HANC, reloj, datos SMPTE 337 y sus límites, renumeración; canales 17 a 32 en interfaces de 3 Gb/s |
| SMPTE ST 2110-10:2022 (https://pub.smpte.org/doc/st2110-10/) | Flujos RTP sobre UDP |
| SMPTE ST 2110-30:2025 | AES67 como base, 48 kHz, niveles A a CX, SDI y SGRP |
| Audinate, *Dante Controller User Guide*, versión 4.18.x, publicada el 6-5-2026 | Dante: presentación, suscripción, nombres, flujos unicast y multicast, formatos, mensajes de error, latencia, PTP y su versión, redundancia, gigabit, EEE, DSCP, AES67 y ST 2110-30 |
| RME, *User's Guide MADI Converter* (sin fecha), cap. 7.1 «MADI Basics» y especificaciones | MADI: origen, 28 señales AES/EBU, 100 y 125 Mbit/s, 56 y 64 canales, 96 kHz, coaxial y fibra, conectores, alcances, niveles, 1.300 nm, vidrio, monomodo de 8 µm, separación galvánica |
| RME, *User's Guide ADI-648* (sin fecha) | ADAT: canales por frecuencia, TOSLINK, 10 m, especificación de Alesis, S/MUX y S/MUX4, doble velocidad, sin codificación que la identifique; conversión MADI-ADAT |
| DiGiCo, nota técnica TN294 «SD Series MADI Implementation», rev. 3, 27-2-2013 | MADI: definición y revisiones de la AES10, cable RG59U, 0,5 V y 125 MHz, diferencias de masa de 0,25 V, distancia dependiente del equipo, 56 frente a 64 canales, S-MUX y Hi-Speed, dos puertos a 96 kHz, puertos redundantes |
| Crown Audio, FAQ «Professional Power Amplifiers» (https://www.crownaudio.com/en-US/faq_categories/1), respuesta sobre el pin vivo en sus etapas | Patillaje XLR y jack TRS |
| Rane, RaneNote 151 «Grounding and Shielding Audio Devices», 1995, rev. 2002 (https://www.ranecommercial.com/legacy/note151.html) | «Pin 2 is hot» como convenio de la AES; malla al pin 1 y al cuerpo del jack de 6,35 mm; usos del jack estéreo |
| Rane, RaneNote 102 «Analog I/O Standards», 1982 (https://www.ranecommercial.com/legacy/pdf/old/note102.pdf) | Patillaje del jack TRS balanceado, del TS y del TRS de auriculares |
| Soundcraft (Harman), *The Soundcraft Guide to Mixing*, sección 7 «Wiring Up & Connectors» | Punto de inserción (punta envío, anillo retorno, cable en Y); entrada TRS con fuente desbalanceada; variación entre fabricantes |
| Shure, *Wireless Microphone Systems* (Tim Vear), capítulos de videocámaras y de monitores intraauriculares | Jack de 1/8" TRS estéreo |

Oficio sin norma detrás, y así se declara: las tres familias de línea; el comportamiento de una señal
digital en un cable de impedancia equivocada; la tabla del cable de micrófono; el panel de conexiones
y sus tres diseños; el *splitter* y lo que comparte; la matriz, sus conceptos, el salvado y sus
clases; qué puede ir por un XLR; la masa del punto de inserción; el nombre de 3,5 mm del jack pequeño; los 75 Ω y el BNC
del SDI; la descripción de Dante como protocolo de audio y control; los requisitos del conmutador;
los 100 m y las categorías de cable de Ethernet; UDP frente a TCP y la sobrecarga de cabeceras; el
distribuidor para varios receptores AES/EBU; la protección del MADI duplicando el camino; el alcance
práctico del ADAT frente a MADI y red; el embebedor, sus confusiones y la reordenación de pistas;
dónde se embebe y desembebe; la tabla de conversiones; el supuesto práctico. Es cálculo, y se puede
rehacer: 56 canales de 28 señales AES/EBU; tres flujos para diez canales; 1,152 Mbps por canal y
73,7 Mbps para 32 bidireccionales; 3,072 millones de intervalos por segundo en la AES/EBU a 48 kHz;
192 bits en 24 bytes; ocho pares AES/EBU en 16 canales embebidos.
