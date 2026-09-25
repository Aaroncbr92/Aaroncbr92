# Tema 4 del específico de Operador/a de Sonido · Consolas de mezcla analógicas y digitales

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 4 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Recomendación técnica: EBU R 68-2000 (nivel de alineación). Documentación de fabricante: Yamaha, *CL5/CL3/CL1 V5 Reference Manual* (una consola digital de directo, como ejemplo) y *Get on the Bus*; Soundcraft, *The Soundcraft Guide to Mixing*; Avid, *Pro Tools Reference Guide* 2025.12 (automatización). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | La vigente el 24/09/2026: EBU R 68-2000; de los manuales, la versión citada en «Trazabilidad» |
| **Extensión** | 9.900 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Europea de
Radiodifusión (**UER**, en inglés **EBU**, *European Broadcasting Union*), que publica sus
recomendaciones (**R**) y sus documentos técnicos (**Tech**); decibelio (**dB**); decibelios
referidos a 0,775 voltios (**dBu**); decibelios referidos a la escala completa digital (**dBFS**,
*decibels relative to full scale*); la escucha antes del fader (**PFL**, *pre-fade listen*) y
después del fader (**AFL**, *after-fade listen*); la escucha en solo en posición (**SIP**,
*solo in place*); el atenuador de la escucha (**DIM**, de *dimmer*); el filtro paso alto (**HPF**,
*high pass filter*); la ecualización (**EQ**); el amplificador controlado por tensión (**VCA**,
*voltage-controlled amplifier*) y su equivalente digital, el control digital de nivel (**DCA**,
*digitally controlled amplifier*); el modo de tres salidas izquierda, centro y derecha (**LCR**,
*left, centre, right*); la zona de control de sonido frente al escenario de un espectáculo
(**FOH**, *front of house*); la estación de trabajo de audio digital (**DAW**, *digital audio
workstation*); los equipos de entrada y salida conectados por red a la consola (**I/O**,
*input/output*). **Dante** es el nombre comercial de un sistema de audio sobre red, no una sigla.
Los fabricantes se citan por su nombre comercial: Yamaha, Soundcraft y Avid (Pro Tools es su
estación de trabajo).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 4):
>
> Consolas de mezcla analógicas y digitales: niveles, entradas, salidas, buses, auxiliares, grupos,
> matrices, automatización y escenas.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué funciones cumple una mesa y en qué bloques se ordena; qué distingue
una consola analógica de una digital y una de directo de una de postproducción; qué hacer si a una
mesa digital le llega una señal a otra frecuencia de muestreo; cómo se ajusta la ganancia de una
entrada y con qué escucha; qué es el PFL y en qué se diferencia del AFL y del solo en posición;
dónde conviene tener los faders; cómo se suman los decibelios de las etapas de un canal; a qué
nivel se alinea el tono en digital según la EBU; en qué orden va la cadena de un canal de entrada;
qué son un punto de inserción y una salida directa; qué hace el DIM; qué es un bus; cuándo un envío
auxiliar debe ser previo o posterior al fader, y por qué; qué es una mezcla menos; qué diferencia
un subgrupo de un grupo VCA o DCA; qué es un grupo de silencio; qué hace una matriz y en qué se
diferencia de una matriz de conmutación; qué modos de automatización hay y qué hace cada uno; qué
guarda una escena y qué son la protección de parámetros y la recuperación parcial. En la prueba
práctica: ajustar la ganancia de un micrófono, montar la mezcla de retorno de un presentador o la
de un escenario, enviar un canal a una reverberación, agrupar los micrófonos de una tertulia, sacar
una misma mezcla a varios destinos y preparar las escenas de un programa.

<!-- indice -->

## Índice

- [Consolas de mezcla analógicas y digitales](#consolas-de-mezcla-analógicas-y-digitales)
  - [Qué hace una mesa](#qué-hace-una-mesa)
  - [Analógica frente a digital](#analógica-frente-a-digital)
  - [Directo frente a postproducción](#directo-frente-a-postproducción)
  - [La frecuencia de muestreo en una mesa digital](#la-frecuencia-de-muestreo-en-una-mesa-digital)
- [Niveles](#niveles)
  - [Lo que llega a la entrada](#lo-que-llega-a-la-entrada)
  - [La escucha previa: PFL, AFL y solo en posición](#la-escucha-previa-pfl-afl-y-solo-en-posición)
  - [El ajuste de ganancia de una entrada](#el-ajuste-de-ganancia-de-una-entrada)
  - [Los faders en torno a 0](#los-faders-en-torno-a-0)
  - [Los decibelios de la cadena se suman](#los-decibelios-de-la-cadena-se-suman)
  - [El nivel de alineación](#el-nivel-de-alineación)
- [Entradas](#entradas)
  - [El canal de entrada](#el-canal-de-entrada)
  - [La cadena del canal, en orden](#la-cadena-del-canal-en-orden)
  - [Inserción y salida directa](#inserción-y-salida-directa)
  - [Previos compartidos por red](#previos-compartidos-por-red)
- [Salidas](#salidas)
  - [Los canales de salida](#los-canales-de-salida)
  - [Estéreo, mono y LCR](#estéreo-mono-y-lcr)
  - [La sección de escucha: DIM, solo y silencio](#la-sección-de-escucha-dim-solo-y-silencio)
  - [Las órdenes y el oscilador](#las-órdenes-y-el-oscilador)
- [Buses](#buses)
  - [Qué es un bus](#qué-es-un-bus)
  - [Los buses de una consola digital](#los-buses-de-una-consola-digital)
  - [Un bus que suma y un mando que no suma](#un-bus-que-suma-y-un-mando-que-no-suma)
- [Auxiliares](#auxiliares)
  - [Envíos y retornos](#envíos-y-retornos)
  - [Previo o posterior al fader: la regla](#previo-o-posterior-al-fader-la-regla)
  - [El retorno de efectos, sin realimentación](#el-retorno-de-efectos-sin-realimentación)
  - [Bus fijo o variable](#bus-fijo-o-variable)
  - [Los envíos en los faders](#los-envíos-en-los-faders)
  - [La mezcla menos](#la-mezcla-menos)
- [Grupos](#grupos)
  - [El subgrupo: un bus que suma](#el-subgrupo-un-bus-que-suma)
  - [El grupo VCA o DCA: un mando que no suma](#el-grupo-vca-o-dca-un-mando-que-no-suma)
  - [Subgrupo frente a DCA](#subgrupo-frente-a-dca)
  - [Los grupos de silencio](#los-grupos-de-silencio)
  - [Un caso: los micrófonos de una tertulia](#un-caso-los-micrófonos-de-una-tertulia)
- [Matrices](#matrices)
  - [Qué es la matriz de una consola](#qué-es-la-matriz-de-una-consola)
  - [La matriz en la sonorización](#la-matriz-en-la-sonorización)
  - [Matriz de mezcla y matriz de conmutación](#matriz-de-mezcla-y-matriz-de-conmutación)
- [Automatización](#automatización)
  - [Qué es](#qué-es)
  - [Los modos](#los-modos)
  - [Cómo se distinguen](#cómo-se-distinguen)
  - [Un caso práctico](#un-caso-práctico)
- [Escenas](#escenas)
  - [Qué es una escena](#qué-es-una-escena)
  - [Qué guarda](#qué-guarda)
  - [La protección de parámetros: Recall Safe](#la-protección-de-parámetros-recall-safe)
  - [La recuperación parcial: Focus](#la-recuperación-parcial-focus)
  - [La transición: Fade](#la-transición-fade)
  - [Las escenas en un programa](#las-escenas-en-un-programa)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Consolas de mezcla analógicas y digitales

### Qué hace una mesa

Qué hace una mesa, en cinco funciones: amplificar y adaptar cada fuente, procesarla, mezclarla,
encaminarla y monitorizarla.

Su estructura, que es la que hay que saber describir:

| Bloque | Qué hace |
|---|---|
| PREAMPLIFICADOR de entrada | Adapta el nivel de la fuente al de la mesa: micrófono, línea o digital |
| ECUALIZACIÓN y filtros | Corrige la respuesta en frecuencia |
| DINÁMICA | Compresor, limitador y puerta de ruido |
| Envíos y retornos | Salidas paralelas para efectos y para monitorado |
| Buses y subgrupos | Sumas parciales que se controlan juntas |
| Matriz de salida | Qué mezcla va a qué destino: emisión, grabación, sala, retornos |
| MONITORADO y escucha | Lo que oye el técnico, que no siempre es lo que sale |

La tabla sigue el camino de la señal: de la entrada (epígrafe «Entradas») a los buses, los
auxiliares, los grupos y la matriz, y de ahí a las salidas y a la escucha. La ecualización y la
dinámica de cada canal se estudian en el tema 5; aquí sólo se dice dónde están en el canal.

### Analógica frente a digital

La analógica tiene un camino físico por canal y un mando por función; la digital procesa números,
tiene memorias de escena y un mando que cambia de función según la capa. La digital gana en
recuperar una configuración en segundos; la analógica, en que lo que se ve es lo que hay.

De esa diferencia salen otras dos que el tema desarrolla. El control de nivel de varios canales a
la vez se hizo en analógico con amplificadores controlados por tensión (VCA) y en digital con
control digital (DCA) («Grupos»). Y la memoria de escena, que sólo existe en digital, es la forma
que toma en directo la automatización («Escenas»).

La consola digital, además, puede tener sus previos lejos: en cajas de entrada y salida (I/O)
conectadas por red, compartidas a veces entre dos consolas o con una grabación («Previos
compartidos por red»). En analógico, el previo está en el canal.

### Directo frente a postproducción

Mesa de DIRECTO frente a mesa de POSTPRODUCCIÓN. La primera prioriza la maniobra inmediata y la
fiabilidad; la segunda, la automatización y el número de pistas.

En postproducción la mezcla se hace muchas veces en una estación de trabajo (DAW) con una
superficie de control: la automatización de ese caso se ve en «Automatización». En directo, lo que
se recupera de un bloque a otro del programa es la escena.

### La frecuencia de muestreo en una mesa digital

Si una mesa digital trabaja a una frecuencia de muestreo y le llega una señal digital muestreada a
otra, hay que CONVERTIR LA FRECUENCIA DE MUESTREO. El aparato que lo hace es un convertidor de
frecuencia de muestreo.

Las otras salidas no valen: meterla por una entrada analógica supone convertir a analógico y volver
a digital, que es una pérdida de calidad innecesaria y además exige un convertidor externo; un
atenuador de paso no toca la frecuencia de muestreo, sólo el nivel; y decir que no se puede es
falso, porque la conversión de frecuencia de muestreo es un proceso corriente.

Y la regla de oficio que hay que añadir: una instalación de audio digital tiene UNA referencia de
reloj y todo lo demás se engancha a ella. La conversión de frecuencia se usa para lo que viene de
fuera; dentro de la casa se sincroniza, no se convierte, porque cada conversión es un proceso más.

La referencia de reloj, la sincronía por red y los formatos de interfaz digital se estudian en los
temas 11 y 15.

## Niveles

### Lo que llega a la entrada

A una mesa llegan tres clases de señal: de micrófono, de línea y digital. La de micrófono es de
milivoltios y necesita un previo con mucha ganancia; la de línea llega ya a nivel de trabajo, y la
doméstica, más baja y desbalanceada. Las escalas (dBu, dBV, dBFS), los niveles de trabajo
profesional y doméstico, el margen de un equipo y la estructura de ganancia de una cadena se
estudian en el tema 2; aquí se ve cómo se ajustan en la consola.

La consola digital separa además dos ganancias. En la cadena del canal de entrada de la Yamaha CL
hay un bloque de **«DIGITAL GAIN»**, distinto de la ganancia analógica del previo, que está en la
caja de entrada o en la propia consola: Yamaha sitúa los previos en **«an INPUT jack on the I/O
device, the OMNI IN on the CL unit, or a slot that is connected to an external head amp device»**
(«Entradas»). La ganancia que fija la relación entre señal y ruido es la analógica,
la del previo, porque es la que se toma de una vez al principio de la cadena (tema 2).

### La escucha previa: PFL, AFL y solo en posición

Un PFL en una consola de mezcla de audio es un modo para escuchar una señal antes de que pase por el
fader de volumen.

Para qué sirve en la práctica: para oír un canal sin sacarlo al programa. El técnico pulsa el
PFL de un micrófono con el fader cerrado y lo escucha en sus auriculares o en el altavoz de control:
comprueba que el micrófono está abierto, que el nivel es bueno y que no hay ruido, y sólo entonces
sube el fader. Es lo que evita sacar al aire un canal que zumba.

| Escucha | Qué oye | Cuándo se usa |
|---|---|---|
| PFL | La señal ANTES del fader: se oye aunque el fader esté a cero | Comprobar un canal antes de abrirlo |
| AFL | La señal DESPUÉS del fader: refleja lo que sale de verdad | Comprobar cómo suena un canal ya en la mezcla |

Las siglas lo dicen todo cuando se traducen: *pre fade listen*, escucha antes del atenuador.
Sirve para comprobar un micrófono, un teléfono o una cinta con el atenuador cerrado, es decir, sin
que salga al aire. Y no lleva la señal al bus principal: la manda a la escucha del técnico, no al
programa.

El punto de escucha es antes del fader, no antes del ecualizador: la sigla dice *pre-fade*, no
*pre-EQ*. En la Yamaha CL, el punto de escucha del canal de entrada se elige entre **«PFL
(immediately before fader), AFL (immediately after fader), or POST PAN (immediately after PAN)»**:
el PFL se toma inmediatamente antes del fader, después de la ecualización y la dinámica del canal.
Se oye el canal como está tratado, no como entró.

Soundcraft añade dos matices. El AFL es **«A function that allows the operator to monitor a
post-fade signal. Used with Aux Masters»**: se usa, sobre todo, para escuchar la salida de un
auxiliar. Y el solo en posición (SIP) es otra cosa: **«A function that allows the operator to listen
to a selected channel on it's own but complete with all relevant effects, by automatically muting
all other inputs»**. El PFL no toca la mezcla; el SIP silencia todas las demás entradas, también las
que van al programa. Por eso, según Soundcraft, el PFL **«is very useful for setting proper input
preamp levels»**, mientras que el SIP **«is less good for level setting, but more useful in mixdown
situations»**. En una mesa que está en el aire, un SIP pulsado por error silencia el programa (el
aviso es de oficio, consecuencia de la definición).

### El ajuste de ganancia de una entrada

Soundcraft define la ganancia de entrada así: **«Input gain is designed to take an audio signal, and
adjust it to the level which the mixer understands.»** Y fija el criterio: **«Ideally the input
signal should be as high in level as possible while still leaving a margin of safety to prevent
distortion on loud sections. [...] The remaining safety margin is known as Headroom.»** La señal,
tan alta como se pueda, dejando margen para los pasajes fuertes: ese margen es el *headroom*.

El procedimiento, con la escucha previa: **«Press the PFL/Solo switch on the relevant input. Adjust
gain/input sensitivity until meters read within the yellow [...]. Release PFL/Solo. Repeat for all
other inputs.»** Se pulsa el PFL del canal, se ajusta la ganancia mirando el medidor hasta la zona de
trabajo, se suelta el PFL y se repite en cada entrada. La zona «amarilla» y las cifras del medidor
son las de las mesas Soundcraft; cada consola marca la suya.

Y un aviso del mismo manual: **«NB: EQ affects gains settings.»** Si se realza una banda después de
ajustar la ganancia, el nivel sube; se comprueba otra vez con el PFL.

En la práctica, la ganancia se ajusta con la fuente real a su nivel real: el presentador hablando
como hablará, no diciendo «probando»; el invitado, cuando llegue, y el grupo, tocando el tema más
fuerte. Una ganancia ajustada con una prueba floja satura en el directo (oficio).

### Los faders en torno a 0

Soundcraft: **«It is important to keep your input faders around the ‘0’ mark for greater control.
This is because fader scales are typically logarithmic and not linear»**. Y para los masters:
**«Set your master outputs to ‘0’ on the scale»**.

El porqué: la escala del fader está abierta alrededor de 0 y apretada abajo. Cerca de 0, un
centímetro de recorrido son pocos decibelios y el ajuste es fino; abajo, el mismo centímetro son
muchos y el ajuste es brusco. Si un canal queda con el fader muy bajo para sonar bien, la ganancia
de entrada está demasiado alta y se corrige en el previo, no en el fader; si queda muy alto, al
revés.

### Los decibelios de la cadena se suman

Los decibelios de las etapas en cadena se suman. Si la ganancia de un canal está ajustada a −3 dB y
se quiere que el nivel en el bus sea de 1 dB, el fader debe ponerse en +4 dB: −3 + x = 1 y x = 4.

La única forma de fallarla es restar en vez de sumar o confundir el signo de la ganancia de entrada.

Lo mismo con varias etapas: un previo que da +40 dB, una ecualización que realza 3 dB y un fader a
−5 dB dejan la señal 38 dB más alta que como entró (40 + 3 − 5; cálculo).

### El nivel de alineación

En digital, el máximo absoluto es 0 dBFS: el mayor número que el sistema puede escribir. Por encima
no hay más; la señal se recorta. Por eso los niveles digitales son negativos, y el nivel de
referencia se fija por debajo de ese techo.

La EBU R 68 recomienda que sus miembros usen **«coding levels for digital audio signals which
correspond to an alignment level which is 18 dB below the maximum possible coding level of the
digital system, irrespective of the total number of bits available»**; la nota 2 lo precisa:
**«corresponding to a ratio of 1:8 (18.06 dB)»**. La EBU Tech 3343 (§ 8.1) lo aplica al tono:
**«An Alignment Signal in broadcasting consists of a sine-wave signal at a frequency of typically
1 kHz, which is used to technically align a programme’s audio path. In digital systems the level of
such an Alignment Signal is 18 dB below the maximum coding level, irrespective of the total number
of bits available (−18 dBFS).»**

Es decir: el tono de referencia es una senoide de 1 kHz a −18 dBFS.

La R 68 da la razón de referir el nivel al máximo digital: **«the only reliable method to specify a
level in a digital signal is by reference to the maximum digital codes allowed by the number of bits
in use»**. Lo que la R 68 no dice es a cuántos dBu analógicos corresponde ese −18 dBFS: esa
equivalencia no está en la R 68 ni en la Tech 3343 y no se debe atribuir a la EBU.

La consola lleva su propio generador para alinear: la Yamaha CL incluye **«an oscillator that can
output a sine wave or pink noise»** (una senoide o ruido rosa), **«so that you will be able to check external equipment or to test the
acoustical response of the room or hall»**; con la senoide se alinea la salida de la mesa con el
equipo siguiente (uso de oficio). Por qué la reserva es de 18 dB se estudia en el tema 5; cómo
se lee el tono en los medidores de pico y de sonoridad, y la sonoridad del programa, en el tema 13.


## Entradas

### El canal de entrada

El canal de entrada es la sección que recibe cada fuente, la trata y la reparte. Yamaha lo describe
así en su consola CL, que se toma aquí como ejemplo de consola digital de directo (no es norma ni
consta que sea la que usa CSRTV): **«The input channels comprise the section that processes signals
received from the I/O devices, rear panel input jacks, or slots 1-3, and sends them to the STEREO
bus, MONO bus, MIX buses, or MATRIX buses.»** Hay dos clases: **«MONO channels»** y **«STEREO
channels»**.

El canal recibe la señal de las cajas de entrada por red, de las tomas del panel trasero o de las
tarjetas de ampliación, y la manda a los cuatro destinos de la consola: el bus estéreo, el mono, los
buses de mezcla (MIX) y los de matriz (MATRIX), que se ven en «Buses» y «Matrices».

### La cadena del canal, en orden

El orden de los diez bloques del canal de entrada de la Yamaha CL, con la definición del fabricante:

| Orden | Bloque | Qué hace, según Yamaha |
|---|---|---|
| 1 | **«INPUT PATCH»** | **«Assigns input signals to the input channels»**: decide qué entrada física llega a qué canal |
| 2 | **«Ø (phase)»** | **«Switches the phase of the input signal»**: invierte la polaridad |
| 3 | **«DIGITAL GAIN»** | **«Attenuates/boosts the level of the input signal»**: ganancia digital del canal, aparte de la analógica del previo |
| 4 | **«HPF (High Pass Filter)»** | **«Cuts the region below the specified frequency»**: quita graves por debajo de una frecuencia |
| 5 | **«4 BAND EQ»** | **«A parametric EQ with four bands: HIGH, HIGH MID, LOW MID, and LOW»** |
| 6 | **«DYNAMICS 1»** | Puerta y atenuación por otra señal (*ducking*), o expansor o compresor: **«gating and ducking, or as an expander or compressor»** |
| 7 | **«DYNAMICS 2»** | **«compressor, compander, or de-esser»**: compresor, compansor o reductor de sibilantes |
| 8 | **«INPUT DELAY»** | **«Corrects input signal delay. You can specify up to 1000ms»**: retardo de corrección, hasta 1.000 ms |
| 9 | **«LEVEL/DCA 1-16»** | Por su rótulo, el nivel del canal y los grupos DCA 1-16 («Grupos»). El manual lo describe como **«Adjusts the input level of the effect»**, texto que no casa con un canal de entrada |
| 10 | **«ON (On/off)»** | **«If this is off, the corresponding channel will be muted»**: la tecla que abre o silencia el canal |

Después vienen el panorama y los envíos a los buses. Tres ideas de la tabla que conviene
retener:

1. El encaminamiento (*patch*) es el primer bloque. En una consola digital no hay un cable por canal:
   cualquier entrada puede ir a cualquier canal, y ese reparto se guarda con la escena («Escenas»).
2. El «Ø» invierte la polaridad; no retrasa la señal. Aunque la consola lo rotule *phase*, polaridad
   y fase no son lo mismo (temas 1 y 2). Lo que corrige un desfase por distancia entre micrófonos es
   el retardo de entrada.
3. El filtro paso alto va antes de la ecualización y de la dinámica, para que los graves que no se
   quieren no disparen el compresor (oficio). Ecualizador, dinámica y filtros se estudian en el tema 5.

En una consola analógica el canal es el mismo en lo esencial —previo, filtro, ecualizador, envíos,
panorama, fader—, pero cada bloque es un circuito con su mando y el orden lo fija el fabricante
(oficio).

### Inserción y salida directa

Dos puntos del canal permiten sacar la señal fuera de la mezcla.

El punto de inserción es, para Soundcraft, **«A break point in the signal path to allow the
connection of external devices»**: un corte en el camino de la señal para intercalar un equipo
externo (un compresor, un procesador de voz) que devuelve la señal al mismo canal. En la Yamaha CL
puede situarse **«PRE EQ (immediately before the EQ), PRE FADER (immediately before the fader), or
POST ON»**.

La salida directa es, para Soundcraft, **«A pre-/post-fade, post-EQ line level output from the
input channel, bypassing the summing amplifiers»**: una salida de línea de un solo canal que no pasa
por los amplificadores de suma, es decir, que no entra en ninguna mezcla. En la Yamaha CL se toma en
**«PRE HPF (immediately before the HPF), PRE EQ (immediately before the EQ) or PRE FADER
(immediately before the fader), or POST ON (immediately after the [ON] key)»**.

La diferencia práctica: la inserción vuelve al canal y la salida directa no vuelve. La salida
directa se usa para grabar cada canal por separado en una grabación multipista; tomada antes del
filtro o del ecualizador, la pista queda limpia y se puede tratar después; tomada antes del fader, no
depende de lo que haga el técnico con la mezcla (oficio).

### Previos compartidos por red

En una consola digital con cajas de entrada por red, dos consolas pueden compartir los mismos
previos: la de sala (FOH) y la de monitores de un espectáculo, o la de directo y una grabación. El
problema es que la ganancia analógica es una sola: si una de las dos la cambia, le cambia el nivel a
la otra.

Yamaha lo resuelve con la compensación de ganancia: activada, **«the level of the signal output from
the I/O device to the audio network will be stabilized. For example, if the FOH console and the
monitoring console are sharing an I/O device, or if you are performing digital recording via Dante
connections, using this function will maintain the signal output at a constant level from the I/O
device to the network even if the analog gain value on the I/O device is changed»**. Es decir, la
caja mantiene constante el nivel que manda a la red aunque se toque la ganancia analógica, y cada
consola ajusta su nivel con la ganancia digital de su canal: con la compensación activada,
**«digital gain will be used to adjust the level of the signal input to the input channels»**. El audio sobre red se estudia en el
tema 15.

## Salidas

### Los canales de salida

En la Yamaha CL, cada bus tiene su propio canal de salida, con proceso como el de un canal de
entrada. Yamaha: **«The output channel section takes the signals sent from the input channels to the
various buses, processes them with EQ and dynamics, and sends them to output ports or other
buses.»** La sección de salida recoge lo que las entradas mandan a los buses, lo ecualiza y lo
comprime, y lo manda a una toma de salida o a otro bus.

Los canales de salida de la Yamaha CL son tres clases:

| Canal de salida | Qué hace, según Yamaha |
|---|---|
| MIX | **«These channels process signals sent from input channels to MIX buses, and output them to the corresponding output port, MATRIX bus, STEREO bus, or MONO (C) bus.»** |
| STEREO y MONO (C) | La salida principal. **«If input channels are in LCR mode, the STEREO (L/R) channels and the MONO (C) channel can be used together as a set of three output channels.»** |
| MATRIX | **«These channels process the signals sent from input channels, MIX channels, and STEREO/MONO channels to MATRIX buses, and send them to the corresponding output ports.»** |

Dos cosas se leen en la tabla. Un canal MIX puede ir a una toma de salida o entrar en otro bus (el
estéreo o una matriz): así funciona un subgrupo («Grupos»). Y la matriz es el último escalón: recibe
entradas, mezclas y el estéreo, y sólo sale a tomas de salida («Matrices»).

En una consola analógica, las salidas son las de los masters (estéreo, grupos, auxiliares, matriz),
cada una con su mando de nivel, sin proceso propio salvo que se inserte un equipo externo (oficio).

### Estéreo, mono y LCR

En la Yamaha CL, **«The STEREO bus and MONO bus are used to send signals to the main speakers»**,
y cada canal los alimenta de una de dos maneras, que se eligen canal a canal: en modo ST/MONO (estéreo y mono), el
canal manda al estéreo (izquierda y derecha, con su panorama) y al mono por separado; en modo LCR,
**«This mode sends input channel signals to three buses (STEREO (L/R) and MONO (C))
simultaneously»**, y el panorama y un mando de proporción entre centro y lados (CSR, *Center Side
Ratio*) reparten la señal entre izquierda, centro y derecha. El modo LCR sirve para sonorizar con
tres grupos de altavoces (oficio; la sonorización, en el tema 10);
el multicanal y la compatibilidad con mono se estudian en el tema 14.

Para comprobar que una salida es de verdad estéreo, tres reglas:

1. Estéreo significa dos canales distintos, no dos canales iguales. Una configuración en la que
   las dos salidas reciben lo mismo es mono duplicado, aunque haya dos pistas.
2. Estéreo significa dos canales, no más de dos. Una configuración que abre cuatro salidas
   independientes no es estéreo: es multicanal.
3. Y estéreo significa que cada fuente tiene una posición en el panorama. Un panel donde todos
   los panoramas están al centro entrega dos canales idénticos: vuelve al caso 1.

Con esas tres comprobaciones —dos salidas, distintas, con panorama repartido— se lee cualquier
configuración de mezcla.

### La sección de escucha: DIM, solo y silencio

La escucha del control es una salida más, pero no va al programa: es lo que oye el técnico, que no
siempre es lo que sale. A ella llegan el programa, la escucha previa (PFL o AFL) y lo que se
seleccione.

El DIM en una mesa de sonido atenúa el volumen de los monitores de la sala de control en una
cantidad preestablecida.

Para qué sirve: para hablar con alguien sin perder la referencia de escucha. Baja la escucha una
cantidad fija y conocida, de modo que al soltarlo se vuelve exactamente al mismo nivel de antes.
Bajar el mando y volver a subirlo no garantiza eso.

Los cuatro mandos de la sección de escucha que se confunden:

| Mando | Qué hace |
|---|---|
| DIM | Atenúa la escucha una cantidad fija |
| Ganancia de entrada | Ajusta el nivel del previo, en el canal |
| Solo | Escucha únicamente el canal seleccionado |
| Mute | Silencia por completo |

El DIM actúa sobre la escucha, no sobre el programa: con el DIM pulsado la emisión sigue igual. El
silencio (*mute*) de un canal, en cambio, sí lo quita del programa.

### Las órdenes y el oscilador

La consola lleva un micrófono de órdenes (*talkback*) para hablar con quien está en el plató, en el
escenario o en el locutorio. Yamaha: **«Talkback is a function that sends the signal of a mic
connected to the TALKBACK jack to the desired bus. This is used mainly to convey instructions from
the operator or sound engineer to the performers and staff.»** Las órdenes van a los buses que se
elijan —los retornos de los presentadores, los monitores del escenario—, nunca al programa (oficio).

Y enlazan con el DIM: **«When talkback is on, you can use the talkback dimmer to lower the monitor
levels other than the talkback signal»**. Con las órdenes pulsadas, el atenuador de órdenes baja la
escucha del control, para que se oiga la respuesta y el micrófono de órdenes no recoja los monitores
(la finalidad es de oficio).

La consola incluye también el oscilador visto en «El nivel de alineación», con senoide o ruido rosa.
La comunicación de producción (intercom) y los retornos de los presentadores se estudian en el
tema 8.

## Buses

### Qué es un bus

Soundcraft lo define así: **«BUS or BUSS»**: **«A defined set of conductors along which signals may
travel. A mixer has several busses carrying the stereo mix, the groups, the PFL signal, the aux
sends, etc.»** Un bus es un camino común al que varios canales mandan su señal y en el que esas
señales se suman. Cada mezcla de una consola es un bus: la estéreo, cada grupo, cada auxiliar; y
también la escucha previa, que es el bus al que van los canales con el PFL pulsado.

En una consola analógica el bus es, literalmente, un conductor que recorre todos los canales; en
una digital es una suma que hace el procesador, pero la lógica es la misma (oficio): cada canal
decide si manda al bus, cuánto y desde qué punto.

### Los buses de una consola digital

En la Yamaha CL los canales de entrada alimentan cuatro familias de buses —**«the STEREO bus, MONO
bus, MIX buses, or MATRIX buses»**— y cada bus tiene su canal de salida («Los canales de salida»):

| Bus | Para qué, en la práctica |
|---|---|
| STEREO y MONO | La mezcla principal |
| MIX | Según se configure, auxiliares (retornos, envíos a efectos, mezclas de grabación) o subgrupos |
| MATRIX | Mezclas de mezclas para varios destinos |

La guía de Yamaha *Get on the Bus* añade el de órdenes: **«Talkback buses are used for communication
between the engineer and performers on stage or between different parts of a production team.»**

### Un bus que suma y un mando que no suma

Hay que distinguir dos formas de manejar varios canales juntos, que se ven en «Grupos»: el bus que
suma las señales (subgrupo) y el mando que sólo gobierna su nivel sin sumarlas (VCA o DCA). Sólo el
primero es un bus.

## Auxiliares

### Envíos y retornos

Un auxiliar es un bus que cada canal alimenta con un mando propio, aparte de su fader: una salida
paralela para efectos y para monitorado. Con él se hace una mezcla distinta de la del programa con
las mismas fuentes.

Sus dos usos, según el glosario de Soundcraft: **«EFFECTS SEND»**: **«A post-fade auxiliary output used to
add effects to a mix.»** y **«FOLDBACK SEND»**: **«A pre-fade auxiliary output used to set up an
independent monitor mix for the performers.»** El envío a efectos lleva la señal a una reverberación
o un retardo; el retorno (*foldback*) monta la mezcla que oyen los que están en el escenario o en el
plató.

Lo que vuelve del procesador de efectos entra en la consola por un retorno de efectos o por un canal
de entrada, y se suma al programa (oficio).

### Previo o posterior al fader: la regla

El envío auxiliar se toma antes o después del fader del canal, y de eso depende para qué sirve.

Soundcraft: **«Pre-fade auxiliaries are independent of the fader so that the amount of effect will
not change with new fader levels. This means you will still hear the effect even when the fader is
at the bottom of its travel.»** Y: **«It is important to use post fade auxiliary sends for effects
units. This is because post fade auxiliaries ‘follow’ the input fader so that when input level
changes the amount of effect remains proportional to the new input level.»**

Para los monitores, al revés: **«NOTE: Pre-fade rather than post-fade auxiliaries must be used. This
is because they are independent of the input faders. If postfade auxiliaries are used, then foldback
mix levels will alter with every input fader change made by the FOH engineer. This will annoy the
band and may lead to feedback which can damage speakers and headphones.»**

Yamaha (*Get on the Bus*) lo resume con la grabación añadida: **«Pre-fader auxiliary sends are
independent of the channel fader position and are often used for independent mixes: stage monitors
and recording sends.»** **«Post-fader auxiliary sends depend on the channel fader position and are
often used for effects like reverb and delay, aux-fed subwoofers, etc.»**

| Uso | Envío | Por qué |
|---|---|---|
| Reverberación, retardo, efectos | Posterior al fader | La cantidad de efecto sigue al fader: si se baja el canal, baja su reverberación |
| Monitores del escenario, retornos | Previo al fader | La mezcla de retorno no cambia cada vez que el técnico toca la mezcla del programa |
| Envíos de grabación, mezclas independientes | Previo al fader | La mezcla no depende de los movimientos del programa |
| Subgraves alimentados por auxiliar | Posterior al fader | Siguen al canal, como los efectos |

Los dos errores y lo que producen: una reverberación en envío previo sigue sonando con el fader del
canal cerrado (la voz se va y queda su cola); un retorno en envío posterior cambia cada vez que el
técnico mueve un fader del programa, y el presentador o el músico dejan de oírse como estaban, con
riesgo de acople.

En la Yamaha CL el punto del envío se elige canal a canal: **«PRE/POST button»**: **«Switches the send
point of each send-source channel between PRE and POST. If the button is lit, the send point is set
to PRE.»** Lo que no se elige canal a canal es el punto exacto del envío previo: **«If the PRE/POST
button is on, you can also select PRE EQ (immediately before the EQ) or PRE FADER (immediately before
the fader) for each MIX/MATRIX bus. This setting is made in the BUS SETUP window»**. Es decir, el
canal decide si su envío es previo o posterior; el bus MIX o MATRIX decide, para todos los canales
que le envían en previo, si ese previo va antes del ecualizador o justo antes del fader.

### El retorno de efectos, sin realimentación

Soundcraft avisa: **«Effects Return Aux Post Control must be set to minimum or feedback will
occur»**. Si el canal que devuelve la reverberación manda a su vez al mismo auxiliar que alimenta la
reverberación, la señal da vueltas: la reverberación se reenvía a sí misma. El envío de ese canal de
retorno a su propio auxiliar se deja cerrado.

### Bus fijo o variable

En la Yamaha CL los buses de mezcla pueden ser de dos tipos: **«MIX buses can be either a FIXED type
whose send level is fixed, or a VARI type whose send level is variable. The MATRIX buses are all
VARI type.»** Con un bus fijo **«you cannot adjust the send level»**: el canal manda o no manda, a
nivel fijo, como a un subgrupo. Con uno variable, cada canal tiene su mando de envío, como en un
auxiliar. Por eso un bus MIX de tipo fijo se usa como subgrupo y uno variable como
auxiliar (oficio).

### Los envíos en los faders

Montar un retorno con mandos giratorios pequeños es lento. La Yamaha CL tiene un modo que pasa los
envíos a los faders: **«SENDS ON FADER mode [...] use the faders on the top panel to adjust the
level of signals sent to the MIX/MATRIX buses. When using this method, signals sent from all input
channels to a specific MIX/MATRIX bus can be adjusted simultaneously.»** Se elige un bus y los
faders de la consola pasan a ser los envíos de cada canal a ese bus. El riesgo es de oficio: olvidar
que se está en ese modo y mover un fader creyendo que es el del programa.

Para escuchar lo que sale de un auxiliar se usa el AFL de su master («La escucha previa»).

### La mezcla menos

Un presentador que habla desde otro lugar, un corresponsal o un invitado por teléfono necesitan oír
el programa sin su propia voz, que les volvería con el retardo del enlace (oficio). Yamaha lo automatiza: **«The Mix Minus
function removes a specific channel signal from the signals sent to the MIX/MATRIX buses. You can use
this function to quickly send monitoring signals to a performer or announcer simply by removing his
or her audio signal.»** Se elige el canal de esa persona y la consola monta en un bus el programa
menos ese canal.

En una consola sin esa función, la mezcla menos se hace a mano con un auxiliar: se envían todas las
fuentes menos la de la persona que la va a oír (oficio). La señal de retorno N-1, el retorno de los
presentadores y la comunicación con ellos se estudian en los temas 7 y 8.

## Grupos

### El subgrupo: un bus que suma

Soundcraft define el grupo como **«An output into which a group of signals can be mixed.»** Y
explica los subgrupos: **«These allow the logical assignment of groups of instruments or vocalists so
that they may be controlled by just one pair of faders, or even a single fader, once individual
instruments’ relative levels have been balanced. They also act as additional outputs with separate
volume/level controls»**. Una vez equilibrados entre sí los micrófonos de, por ejemplo, un coro, se
mandan a un subgrupo y se manejan con uno o dos faders; y el subgrupo es además una salida más.

Yamaha (*Get on the Bus*): **«A sub-group is a grouping of multiple audio channels or tracks that are
mixed before being sent to the main mix bus.»** Como la señal pasa de verdad por el subgrupo, se
puede **«apply processing like EQ or compression collectively»**: ecualizar o comprimir el conjunto
de una vez.

### El grupo VCA o DCA: un mando que no suma

Yamaha (*Get on the Bus*): **«A VCA is a control mechanism used to adjust the level (volume) of
multiple channels simultaneously without affecting their relative balance. VCAs do not actually pass
audio signals themselves [...]. Unlike sub-groups, VCAs do not sum audio signals together»**. El VCA
no lleva audio: mueve a la vez el nivel de los canales que tiene asignados, cada uno en su fader y
hacia su destino.

La diferencia entre VCA y DCA es de tecnología, no de uso: **«VCA is an analog technology that uses
control voltages»**; **«DCA is a digital technology that uses digital control signals»**; **«In
practical terms, however, VCAs and DCAs function similarly in most mixing consoles»**.

En la Yamaha CL: **«CL series consoles feature sixteen DCA groups that enable you to control the
level of multiple channels simultaneously.»** **«A single DCA fader will control the level of all
input channels belonging to the same DCA group while maintaining the level difference between the
channels. This provides a convenient way in which drum mics, for example, can be grouped.»** Desde la
versión 3.0 del programa de la consola, el DCA puede agrupar también salidas: **«you can use the DCA
groups for output master channels»**. Y **«DCA group settings are saved as part of the scene.»** La
cifra de dieciséis es de ese modelo.

### Subgrupo frente a DCA

| | Subgrupo | Grupo VCA o DCA |
|---|---|---|
| Qué es | Un bus: suma las señales | Un mando: no pasa audio |
| Proceso del conjunto | Sí: se puede ecualizar o comprimir el grupo | No: cada canal conserva sólo su proceso |
| Salida propia | Sí: es una salida más | No: cada canal sale por donde salía |
| Envíos posteriores al fader | No los mueve: el canal manda al auxiliar con su propio fader | Los mueve: al bajar el DCA baja el fader efectivo de cada canal y, con él, sus envíos posteriores |
| Uso típico | Tratar juntos una batería, un coro, los micrófonos de una mesa | Subir o bajar juntos varios canales sin tocar su equilibrio |

Las filas «Qué es», «Proceso del conjunto», «Salida propia» y «Uso típico» salen de las definiciones
de Yamaha y Soundcraft. La de los envíos es su consecuencia: con un subgrupo, al bajarlo baja lo que sale del subgrupo, pero la reverberación de
cada canal, alimentada desde su fader, sigue igual; con un DCA baja el canal entero, efectos
incluidos (oficio, derivado de las definiciones).

### Los grupos de silencio

Un grupo de silencio une el encendido y apagado de varios canales en una tecla. Soundcraft: **«MUTE
GROUPS»**: **«A method of combining the on/off status of a selection of channels under a single control
button.»** En la Yamaha CL hay ocho: **«CL series consoles feature eight mute groups. Mute groups
enable you to [...] mute or unmute multiple channels in a single operation.»** **«Mute groups 1 - 8
can be used with both input channels and output channels.»** Y **«You may assign a single channel to
more than one mute group.»**

Un ejemplo de uso, de oficio: en un programa con público y actuaciones, un grupo de silencio con
todos los micrófonos del escenario y otro con los del público permiten cerrar de una vez lo que no
debe sonar al pasar al presentador.

### Un caso: los micrófonos de una tertulia

Cuatro contertulios, cada uno con su micrófono. Se equilibran entre sí en sus faders; se asignan a
un DCA para subir o bajar la tertulia entera sin tocar ese equilibrio; si se quiere comprimir el
conjunto, se mandan además a un subgrupo con su compresor; y se incluyen en un grupo de silencio
para cerrarlos a la vez al dar paso a otra sección (oficio). La puerta y el expansor que se usan con
varios micrófonos abiertos se estudian en el tema 5.

## Matrices

### Qué es la matriz de una consola

La matriz es una mezcla de mezclas. Yamaha (*Get on the Bus*): **«Matrix buses allow for the
creation of custom mixes that combine multiple input signals in different proportions. These mixes
can be sent to various destinations, such as additional speakers or recording devices.»** En la
Yamaha CL la matriz recibe **«the signals sent from input channels, MIX channels, and STEREO/MONO
channels»**: no sólo entradas, sino también buses ya mezclados y la mezcla principal.

La matriz de salida decide qué mezcla va a qué destino: emisión, grabación, sala, retornos. Con una
matriz, una misma mezcla estéreo se reparte a varios destinos, cada uno con su nivel y, si hace
falta, con algo añadido: por ejemplo, el programa con más ambiente de público para la grabación, o
el programa sin la música para una sala (ejemplos de oficio).

### La matriz en la sonorización

En sala la matriz alimenta los distintos grupos de altavoces. Soundcraft pide a la consola de sala
**«a large number of matrix outputs so that a complex range of speaker clusters can be placed around
the auditorium»**: tantas salidas de matriz como zonas de altavoces, cada una con su propia mezcla
(la zona del fondo con más voz, la de delante con menos). La sonorización se estudia en el tema 10.

### Matriz de mezcla y matriz de conmutación

La palabra «matriz» nombra dos equipos distintos. La matriz de una consola mezcla: suma varias
señales en proporciones distintas y saca una nueva. La matriz de conmutación de una instalación no
mezcla nada:

| Equipo | Qué hace | Cuántas señales salen |
|---|---|---|
| Matriz de conmutación | Encamina: elige qué entrada llega a cada salida | La entrada elegida, intacta |
| Matriz de mezcla de una consola | Combina en proporciones: suma entradas y buses con un nivel para cada uno | Una mezcla nueva, distinta de cada señal de entrada |

En la matriz de conmutación, una misma entrada puede ir a la vez a varias salidas, pero no hay
suma: hay un camino que se abre y otro que se cierra. El encaminamiento de entradas de una consola
digital (el *patch* de «La cadena del canal, en orden») es, dentro de la consola, una conmutación de
ese tipo.

## Automatización

### Qué es

La automatización graba los movimientos de los mandos de una mezcla —faders, panoramas, silencios,
envíos, parámetros de los procesadores— y los reproduce a lo largo del tiempo del programa. Es propia
de la postproducción, donde la mezcla se repasa sobre un material ya grabado: la mesa de
postproducción prioriza la automatización y el número de pistas. En directo, lo equivalente es la
escena («Escenas»), que no sigue el tiempo de un material, sino que recupera un estado completo
cuando el técnico la llama.

Los modos se toman aquí de la estación de trabajo Pro Tools, de Avid, porque es la documentación que
se ha leído; otras estaciones de trabajo y las superficies de control usan modos con nombres
parecidos, pero sólo se afirma lo que dice Avid. Avid: **«Automation modes control how a track’s
automation data is written and played back.»** Los modos gobiernan cómo se escribe y cómo se
reproduce la automatización de cada pista.

### Los modos

| Modo | Qué hace, según Avid |
|---|---|
| Off | **«Off mode turns off automation for all automatable parameters»**: la automatización escrita **«is ignored during playback»** |
| Read | **«Read mode plays any automation that was previously written for a track.»** Reproduce, no escribe |
| Write | **«Write mode writes automation from the time playback starts to the time it stops, erasing any previously written automation for the duration of the automation pass.»** |
| Touch | **«Touch mode writes automation only while a fader or switch is touched or clicked with the mouse. When the fader is released, the writing of automation stops and the fader returns to any previously automated position»** |
| Latch | **«Latch mode works in the same way as Touch mode, writing automation only if you touch or move a control. However, unlike Touch, writing of automation continues until you stop playback or “punch out”»** |
| Touch/Latch | **«Touch/Latch Automation mode places a track’s Volume control in Touch mode and all other automatable controls in Latch mode»** (sólo en las versiones Ultimate y Studio de Pro Tools) |
| Trim | (sólo en las versiones Ultimate y Studio) Ajusta **«existing track volume and send level automation data in real time»**; **«When writing automation in Trim mode, fader moves write relative rather than absolute values.»** No es un modo aparte: **«Trim mode works in combination with the other Automation modes (Read, Touch, Latch, Touch/Latch, and Write)»**, y así hay Trim Off, Read Trim, Touch Trim, Latch Trim, Touch/Latch Trim y Write Trim |

### Cómo se distinguen

- Read y Off no escriben nada: Read reproduce lo escrito; Off lo ignora.
- Write es el modo que borra: escribe durante todo el pase y sustituye lo que hubiera, se toque o no
  el mando. Es el modo del primer pase; dejarlo puesto en un repaso borra el trabajo anterior (oficio).
  Pro Tools permite además pasar solo, al acabar un pase en Write, a Touch o a Latch, o seguir en
  Write: la preferencia **«After Write Pass, Switch To»** (*Touch*, *Latch* o *No Change*).
- Touch y Latch sólo escriben al tocar un mando. La diferencia está al soltarlo: en Touch el mando
  vuelve a lo que ya estaba escrito; en Latch se queda donde se soltó y sigue escribiendo ese valor
  hasta que se para. Touch sirve para corregir un pasaje y dejar el resto como estaba; Latch, para
  cambiar un valor desde un punto hasta el final del pase. Avid añade que **«Latch mode is
  particularly useful for automating Pan controls and plugins on non-touch sensitive rotary
  controls, since it does not time out and revert to its previous position when you release a
  control»**: al soltar el mando, Latch no vuelve a la posición anterior.
- Trim no escribe valores absolutos, sino cambios relativos sobre lo ya escrito: sube o baja todo un
  pasaje manteniendo sus movimientos. Sólo sirve para el volumen y los envíos: **«Pan, mute and
  plugin automation cannot be trimmed in this manner.»** Cada versión Trim se comporta como su modo:
  en Read Trim se mueve el fader para probar, pero **«no automation is written»**; en Touch Trim se
  escribe mientras se toca y, al soltar, **«the fader returns to any previously written Trim
  automation values»**; en Latch Trim, desde que se toca, **«Writing of Trim automation continues
  until playback stops, or until you punch out of writing automation»**; en Touch/Latch Trim,
  **«The main Volume Trim fader follows Touch Trim behavior, and Send level Trim faders follow Latch
  Trim behavior»**; en Write Trim, **«as soon
  as playback begins, writing of Trim automation begins for Volume and Send levels»**. Trim Off
  **«turns off reading and writing of all automation (main and trim) for a track»**.

### Un caso práctico

La música de una pieza ya tiene automatizados sus bajadas bajo la voz y resulta toda 2 dB alta. Se
pone la pista en Latch Trim, se baja el fader 2 dB al empezar el pase y se suelta: la bajada relativa
se sigue escribiendo hasta que se para, y todas las bajadas se conservan, 2 dB más abajo. Valdría
también Write Trim, que escribe desde que arranca la reproducción; en Touch Trim, en cambio, al
soltar el fader dejaría de escribirse. En Write se habrían borrado las bajadas; en Touch, habría que
rehacer cada movimiento (oficio, aplicando las definiciones de Avid).

## Escenas

### Qué es una escena

Una escena es una fotografía de la consola que se guarda y se recupera. Yamaha: en la consola digital
**«you can assign a name to a set of mix parameter and input/output port patch settings, and store
the mix settings in memory (and later recall them from memory) as a "scene."»** Se guardan con un
nombre los parámetros de la mezcla y el encaminamiento de entradas y salidas, y se recuperan
después.

En la Yamaha CL, **«Each scene is assigned a number in the range of 000-300. Scene 000 is a read-only
scene used to initialize the mix parameters. Scenes 001-300 are writable scenes.»** La escena 000,
que no se puede sobrescribir, devuelve la consola a su estado inicial. La cifra de 300 es de ese
modelo.

### Qué guarda

Según Yamaha, **«the position of the top panel faders and [ON] key status, as well as [...]
Input/output port patching; Bus settings; Head amp settings; EQ settings; Dynamics 1 and 2 settings;
Rack (GEQ/Effect/Premium Rack) settings; Pan/balance settings; Insert/Direct Out settings; On/off
status and send level of signals sent to MIX buses; On/off status and send level of signals sent to
MATRIX buses; DCA group settings; Mute group settings; Channel link settings»**.

Es decir: faders y teclas de encendido; encaminamiento de entradas y salidas; configuración de los
buses; ganancia de los previos; ecualización y dinámica; efectos y ecualizadores gráficos del
bastidor virtual; panorama; inserciones y salidas directas; envíos a los buses MIX y MATRIX; grupos
DCA y de silencio, y canales enlazados. Casi toda la consola.

Los faders que la escena guarda son los físicos, y en la CL se mueven solos al recuperarla: son
motorizados. El manual habla de **«the motion of the motor faders»** al explicar su calibración, y
del Fade dice que **«The faders will begin to move immediately after Recall occurs, and will reach
the values of the recalled scene over the course of the specified fade time»**. El técnico no tiene
que llevarlos a mano a su marca: la superficie queda como la escena. En una analógica, en cambio,
no hay escena que recuperar («Analógica frente a digital»).

### La protección de parámetros: Recall Safe

Que una escena lo recupere casi todo es a veces un problema: hay canales que no deben cambiar al
cambiar de escena (el micrófono del presentador, que ya está ajustado en directo). Para eso está la
protección de parámetros. Yamaha: Recall Safe es **«a function that excludes only specific
parameters/channels (DCA groups) from Recall operations. Unlike the Focus Recall function [...],
which you can apply to individual scenes, the Recall Safe settings are globally applied to all
scenes.»** Excluye canales o parámetros de la recuperación, y vale para todas las escenas.

La salvedad: **«Channel Link [...] and bus settings are not subject to Recall Safe; they will always
be reproduced in the recalled scene.»** Los enlaces de canal y la configuración de los buses se
recuperan siempre, aunque el canal esté protegido.

### La recuperación parcial: Focus

Focus hace lo contrario, escena a escena. Yamaha: **«lets you specify the parameters that will be
updated when you recall a scene. For example, it is convenient to use this if you want to recall only
the input channel settings of a certain scene.»** Con Focus se elige qué parámetros cambia una
escena concreta al recuperarla.

| | Recall Safe | Focus |
|---|---|---|
| Qué indica | Lo que NO se recupera | Lo que SÍ se recupera |
| Alcance | Todas las escenas | Cada escena por separado |

### La transición: Fade

Una escena cambia los faders de golpe salvo que se pida otra cosa. Yamaha: Fade es **«a function that
smoothly changes the faders of specified channels and DCA groups to their new values over a specified
duration when you recall a scene. The settings of the Fade function are made independently for each
scene.»** Los faders elegidos van a su nuevo valor en el tiempo que se fije, y cada escena tiene su
ajuste.

### Las escenas en un programa

En un programa en directo se prepara una escena por bloque —apertura, entrevista, actuación
musical, cierre— y se recuperan en el orden de la escaleta. Tres cuidados, de oficio: proteger con
Recall Safe lo que se ajusta en vivo (el presentador, el público); guardar la escena después de los
ensayos, no antes, para no perder los ajustes; y comprobar, al recuperar, que el encaminamiento no
ha cambiado una salida que está en el aire. Y como la escena guarda también los grupos DCA, los de
silencio y la ganancia de los previos, una escena recuperada sin protección puede cambiar la ganancia
de un micrófono compartido con otra consola («Previos compartidos por red»).

## Recomendaciones técnicas que el tema cita

| Recomendación | Qué se toma |
|---|---|
| EBU R 68-2000, *Alignment level in digital audio production equipment and in digital audio recorders* | Nivel de alineación 18 dB bajo el máximo de codificación, sea cual sea el número de bits (1:8, 18,06 dB); el nivel digital se refiere al máximo de los códigos |
| EBU Tech 3343-2023 (V4, noviembre de 2023), *Guidelines for Production of Programmes in accordance with EBU R 128*, § 8.1 | Señal de alineación: senoide de 1 kHz a −18 dBFS |

## Lo que este tema no da, y dónde está

- Las consolas de CSRTV (marcas, modelos, número de canales, configuración de sus controles de
  radio y televisión y de sus unidades móviles) y sus procedimientos de operación: no constan en un
  documento publicado localizado.
- Las cifras de una consola concreta (número de buses, de grupos, de escenas) son las de la Yamaha
  CL tomada como ejemplo; otras consolas tienen otras. Los nombres de los modos de automatización son
  los de Pro Tools; los de otras estaciones de trabajo no se han leído.
- La equivalencia entre −18 dBFS y un nivel analógico en dBu: no está en la EBU R 68 ni en la Tech
  3343. Los niveles analógicos de trabajo (+4 dBu, −10 dBV) y la estructura de ganancia, en el tema 2.
- Las ventajas e inconvenientes de la consola analógica frente a la digital, más allá de lo que
  aquí se da (recuperación de escenas, mando por capas, lo que se ve es lo que hay): no se han leído
  en fuente.
- La ecualización, la dinámica y los filtros del canal, en el tema 5; los medidores de pico y de
  sonoridad, en el tema 13; el reloj, la sincronía y las interfaces digitales, en los temas 11 y 15;
  la señal N-1, los retornos, el intercom y la comunicación con realización, en los temas 7 y 8; la
  mezcla en la estación de trabajo, en el tema 9; la sonorización y el modo LCR en sala, en el tema
  10; el multicanal y la compatibilidad con mono, en el tema 14.

## Trazabilidad

Fuentes leídas el 25/09/2026 (los manuales de fabricante, releídos ese día en su edición
descargable); la recomendación de la UER, en su versión vigente ese día.

| Fuente | Qué sostiene |
|---|---|
| EBU R 68-2000 | −18 dBFS; 1:8 (18,06 dB); el nivel digital referido a los códigos máximos |
| EBU Tech 3343-2023 (V4, noviembre de 2023), § 8.1 | Señal de alineación de 1 kHz a −18 dBFS |
| Yamaha Corporation, *CL5/CL3/CL1 V5 Reference Manual* | Canal de entrada, sus diez bloques y su definición; ganancia digital y dónde están los previos; puntos de inserción y de salida directa; compensación de ganancia y uso de la ganancia digital; canales de salida MIX, STEREO/MONO (C) y MATRIX; buses STEREO y MONO, modos ST/MONO y LCR por canal, mando CSR; buses FIXED y VARI; botón PRE/POST y PRE EQ/PRE FADER; SENDS ON FADER; Mix Minus; puntos de escucha PFL, AFL y POST PAN; órdenes y atenuador de órdenes; oscilador y su finalidad; dieciséis DCA y DCA de salidas; ocho grupos de silencio; escenas 000-300, qué guardan, Recall Safe con su salvedad, Focus y Fade; faders motorizados (calibración, p. 279) y su movimiento al recuperar con Fade |
| Yamaha Corporation of America, D. Gould, *Get on the Bus. How to Route Input Signals* | Envíos previos y posteriores y sus usos; bus de matriz; bus de órdenes; subgrupo; VCA, y VCA frente a DCA (con su salvedad «in most mixing consoles») |
| Soundcraft (Harman International), *The Soundcraft Guide to Mixing*, ZL0439, 08/01 (2001) | Ganancia de entrada, *headroom* y ajuste con el PFL; la ecualización afecta a la ganancia; PFL y SIP; faders en torno a 0 y masters a 0; envíos previos y posteriores; auxiliares de monitores previos; retorno de efectos al mínimo; subgrupos; matriz de sala; glosario (bus, grupo, grupos de silencio, envío de efectos, envío de monitores, AFL, salida directa, punto de inserción, SIP) |
| Avid Technology, *Pro Tools Reference Guide*, versión 2025.12, cap. 55 «Automation» | Modos Off, Read, Write, Touch, Latch, Touch/Latch y Trim; uso de Latch en mandos giratorios y su porqué; preferencia «After Write Pass, Switch To»; límites de Trim, su combinación con los demás modos y las versiones Trim Off, Read Trim, Touch Trim, Latch Trim, Touch/Latch Trim y Write Trim; Touch/Latch y Trim sólo en Ultimate y Studio |

Oficio sin norma detrás, y así se declara: las cinco funciones y los bloques de una mesa; la
analógica frente a la digital y el directo frente a la postproducción; el convertidor de frecuencia
de muestreo y la regla de una sola referencia de reloj; el uso del PFL en la práctica y la diferencia
PFL y AFL; el riesgo del SIP en el aire; el ajuste de ganancia con la fuente real; el porqué de la
escala del fader; las tres ideas de la cadena del canal; la analógica sin proceso en las salidas; el
uso de la salida directa para grabar; las tres reglas para comprobar un estéreo; el DIM y los mandos
de la sección de escucha; el destino de las órdenes; el retorno de los efectos por un canal; los
errores de envío previo y posterior; el bus fijo como subgrupo; la mezcla menos a mano; el
comportamiento de los envíos con subgrupo y con DCA; los ejemplos de grupos de silencio, de la
tertulia y de la matriz; la matriz de conmutación frente a la de mezcla; la distinción de los modos
de automatización y su caso práctico; las escenas en un programa. Es cálculo, y se puede rehacer: la
suma de decibelios de un canal (−3 + 4 = 1; 40 + 3 − 5 = 38).
