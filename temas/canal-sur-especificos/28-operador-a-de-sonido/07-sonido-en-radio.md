# Tema 7 del específico de Operador/a de Sonido · Sonido en radio

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 7 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Documentos técnicos de la UER: EBU Tech 3326 Rev. 4 y EBU Tech 3368 v1.0 (audio de contribución sobre IP, ACIP). AES TD1008.1.21-9 (sonoridad del *streaming*). RFC 8216 (HLS). Contrato-programa 2024-2026 entre la Junta de Andalucía y la RTVA (Canal Sur Más y pódcast). Documentación de fabricante y de plataforma: Clear-Com (híbridos), Yamaha (mezcla menos, órdenes), DPA (filtro en peine), Apple Podcasts. UIT-T I.412 (RDSI), G.722 y G.712 (banda ancha y banda estrecha de la voz). Lo demás, oficio |
| **Redacción que se estudia** | La vigente el 24/09/2026; de cada documento, la versión citada en «Trazabilidad» |
| **Extensión** | 10.000 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Europea de
Radiodifusión (**UER**, en inglés **EBU**, *European Broadcasting Union*), que publica sus
recomendaciones (**R**) y sus documentos técnicos (**Tech**); Sociedad de Ingeniería de Audio
(**AES**, *Audio Engineering Society*) y sus documentos técnicos (**TD**); Unión Internacional de
Telecomunicaciones (**UIT**, en inglés **ITU**); Grupo de Trabajo de Ingeniería de Internet
(**IETF**, *Internet Engineering Task Force*), y la serie de documentos de internet llamada
peticiones de comentarios (**RFC**, *Request for Comments*), en la que publica la IETF y también
autores independientes; la red digital de servicios integrados (**RDSI**, o
**ISDN** en la documentación en inglés); el protocolo de internet (**IP**) en sus versiones 4 y 6
(**IPv4**, **IPv6**); el audio de contribución sobre IP (**ACIP**, *Audio Contribution over IP*),
nombre de la norma de interoperabilidad de la UER; el códec, que es el equipo o el algoritmo que
codifica y descodifica el audio; la mezcla que devuelve todo menos la propia señal del que escucha
(**N-1**, o *mix-minus*); la escucha antes del fader (**PFL**, *pre-fade listen*) y el atenuador de
la escucha (**DIM**, de *dimmer*); el retorno interrumpible (**IFB**, *interruptible fold back*); el protocolo de transporte en tiempo real (**RTP**, *Real-time Transport
Protocol*) y su protocolo de control (**RTCP**); el protocolo de datagramas de usuario (**UDP**) y el
de control de transmisión (**TCP**); la corrección de errores hacia delante (**FEC**, *Forward Error
Correction*); el protocolo de inicio de sesión (**SIP**, *Session Initiation Protocol*), el de
descripción de sesión (**SDP**) y el de anuncio de sesión (**SAP**); el método de servicios
diferenciados para la calidad de servicio (**DiffServ**, y **QoS**, *quality of service*) y su código
(**DSCP**, *Differentiated Services Code Point*); la
modulación por impulsos codificados (**PCM**, *pulse-code modulation*); el grupo de expertos de
imágenes en movimiento (**MPEG**) y sus codificaciones de audio (capa II, capa III, **AAC**,
*Advanced Audio Coding*, en sus perfiles de baja complejidad, **LC**, de bajo retardo, **LD**, y de
alta eficiencia, **HE**); la línea de abonado digital (**DSL**); la fibra hasta el hogar (**FTTH**,
*fibre to the home*); las generaciones de telefonía móvil (**3G**, **4G** y **5G**); los sistemas de
satélite de banda ancha global (**BGAN**) y **Thuraya**, y la **banda Ka**; la difusión de audio
digital (**DAB**); el estéreo (**ST**); la retransmisión en directo por HTTP (**HLS**, *HTTP Live
Streaming*), donde **HTTP** es el protocolo de transferencia de hipertexto; la plataforma de
contenidos por internet (**OTT**, *over the top*); las unidades de sonoridad referidas a la escala
completa (**LUFS**, o **LKFS** en la UIT) y la unidad de diferencia de sonoridad (**LU**); el pico
verdadero en decibelios referidos a la escala completa (**dBTP**); la asociación estadounidense de
la industria discográfica (**RIAA**), por su curva de ecualización de disco. *Streaming* se deja en
inglés, como en la documentación del oficio; pódcast se escribe en español (el enunciado lo escribe
*podcast*). También: la Organización Internacional de Normalización (**ISO**); los formatos de
fichero de audio **WAV** (onda sin comprimir), **FLAC** (compresión sin pérdida) y **MP3** (capa III de
MPEG); el canal de sindicación con que se publican los pódcast (**RSS**); la banda ancha (**WB**, *wideband*), como la llaman la UIT-T y el códec AMR-WB. Dante, Opus y APT-X son
nombres comerciales o de códec, y DPA, Clear-Com, Yamaha y Apple son fabricantes o empresas, no
siglas. Los mensajes de SIP (INVITE, ACK, BYE, OPTIONS, REGISTER) se citan en inglés, como en la
norma. SRT, RIST y RTMP se citan sólo por su nombre de protocolo.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 7):
>
> Sonido en radio: microfonía, mesa, híbridos, RDSI/IP, codecs, telefonía, streaming y podcast.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué distingue al sonido de radio del de televisión; cómo se reparte un
estudio entre locutorio y control; qué es una señal de contribución y en qué se diferencia de la de
distribución y la de emisión; qué pasa cuando dos micrófonos abiertos captan la misma voz y qué es la
regla 3:1; qué fuentes llegan a la mesa de un control de radio; qué es un N-1, en qué se diferencia de
un retorno de programa y qué retornos se mandan cuando hay línea principal y de reserva; qué hace la
función de mezcla menos de una consola; qué es un híbrido, qué es la pérdida transhíbrida y qué es
el ajuste de nulo; qué daba la RDSI y por qué se sustituye por IP; qué norma de la UER fija la
interoperabilidad de los códecs de audio sobre IP; qué protocolo de transporte, qué puertos y qué
señalización exige; qué códecs son obligatorios, recomendados u opcionales; qué es un perfil y qué es
un búfer de fluctuación; qué enlace no sirve para una conexión bidireccional; por qué Dante no es un
códec de contribución; qué es el *streaming*, qué es HLS y qué sonoridad se recomienda para
distribuir por internet; qué es Canal Sur Más; qué formatos y sonoridad pide una plataforma de
pódcast. En la prueba práctica: montar los retornos de una conexión exterior, meter una llamada
telefónica en antena sin eco, elegir códec y búfer para un directo desde una red pública, o preparar
un programa ya emitido para publicarlo como pódcast.

<!-- indice -->

## Índice

- [Sonido en radio](#sonido-en-radio)
  - [Lo que distingue al sonido de radio](#lo-que-distingue-al-sonido-de-radio)
  - [El estudio y su reparto](#el-estudio-y-su-reparto)
  - [Contribución, distribución y emisión](#contribución-distribución-y-emisión)
- [Microfonía](#microfonía)
  - [El micrófono de locución](#el-micrófono-de-locución)
  - [Varios micrófonos abiertos: el filtro en peine](#varios-micrófonos-abiertos-el-filtro-en-peine)
- [Mesa](#mesa)
  - [Las fuentes que llegan a la mesa](#las-fuentes-que-llegan-a-la-mesa)
  - [El N-1: la resta que hace posible un directo](#el-n-1-la-resta-que-hace-posible-un-directo)
  - [La mezcla menos en una consola digital](#la-mezcla-menos-en-una-consola-digital)
  - [Dos líneas, dos retornos](#dos-líneas-dos-retornos)
  - [Las órdenes](#las-órdenes)
- [Híbridos](#híbridos)
  - [Qué es un híbrido: de dos a cuatro hilos](#qué-es-un-híbrido-de-dos-a-cuatro-hilos)
  - [La pérdida transhíbrida y el ajuste de nulo](#la-pérdida-transhíbrida-y-el-ajuste-de-nulo)
  - [El híbrido y el N-1](#el-híbrido-y-el-n-1)
  - [Un caso práctico: el oyente en antena](#un-caso-práctico-el-oyente-en-antena)
- [RDSI/IP](#rdsiip)
  - [La RDSI](#la-rdsi)
  - [Por qué se pasa a IP](#por-qué-se-pasa-a-ip)
  - [La norma ACIP: EBU Tech 3326](#la-norma-acip-ebu-tech-3326)
  - [El transporte](#el-transporte)
  - [La señalización: cómo se establece la llamada](#la-señalización-cómo-se-establece-la-llamada)
  - [Los perfiles: EBU Tech 3368](#los-perfiles-ebu-tech-3368)
  - [El búfer de fluctuación](#el-búfer-de-fluctuación)
  - [Calidad de servicio y protección](#calidad-de-servicio-y-protección)
  - [Qué enlaces sirven para una conexión de ida y vuelta](#qué-enlaces-sirven-para-una-conexión-de-ida-y-vuelta)
- [Códecs](#códecs)
  - [Los códecs de la norma ACIP](#los-códecs-de-la-norma-acip)
  - [Qué no es un códec: Dante](#qué-no-es-un-códec-dante)
  - [Cómo se elige el códec](#cómo-se-elige-el-códec)
- [Telefonía](#telefonía)
  - [La llamada telefónica en antena](#la-llamada-telefónica-en-antena)
  - [Banda estrecha y banda ancha](#banda-estrecha-y-banda-ancha)
  - [El teléfono móvil como enlace](#el-teléfono-móvil-como-enlace)
- [Streaming](#streaming)
  - [Qué es el *streaming*](#qué-es-el-streaming)
  - [El protocolo HLS](#el-protocolo-hls)
  - [La sonoridad del *streaming*](#la-sonoridad-del-streaming)
  - [El *streaming* en Canal Sur: Canal Sur Más](#el-streaming-en-canal-sur-canal-sur-más)
- [Podcast](#podcast)
  - [Qué es un pódcast](#qué-es-un-pódcast)
  - [La sonoridad de un pódcast](#la-sonoridad-de-un-pódcast)
  - [El formato de entrega](#el-formato-de-entrega)
  - [Un caso práctico: de la emisión al pódcast](#un-caso-práctico-de-la-emisión-al-pódcast)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Sonido en radio

### Lo que distingue al sonido de radio

Las características particulares del sonido radiofónico son costumbre de oficio, no norma, y así se
dicen:

1. No hay imagen que lo sostenga. Todo lo que el oyente entiende del lugar, de quién habla y de
   qué pasa tiene que estar en el sonido. De ahí que la radio use más ambiente, más ráfagas y más
   identificación verbal que la televisión.
2. La cadena está pensada para la voz. Micrófono cercano, mucha compresión, ecualización que
   realza la presencia y corta lo que no sirve. Una locución de radio suena densa a propósito.
3. Se emite en condiciones de escucha malas. El coche, la cocina, el móvil. Por eso el
   margen dinámico se comprime mucho más que en música: lo que no se oye por encima del ruido de un
   coche, no existe.
4. El directo es la norma, no la excepción. La radio se hace en vivo con el guion cambiando, y
   eso condiciona el equipamiento entero: todo tiene que poder lanzarse ya.

### El estudio y su reparto

Ninguna fuente documental leída regula el reparto del estudio. Lo que sigue es costumbre de oficio.

| Zona | Quién está | Qué hay |
|---|---|---|
| Locutorio | Locutores e invitados | Micrófonos, auriculares, un monitor de escaleta y, a veces, una mesa de autocontrol |
| Control | Técnico y realizador | Mesa, ordenadores de emisión, híbridos telefónicos, códecs, monitores de escucha |

Entre las dos zonas hay un cristal: la comunicación durante la emisión se hace por señas, que no están
normalizadas y varían de emisora a emisora. En muchas emisoras el locutor maneja su propia mesa
(autocontrol), y el técnico pasa de operar a preparar, mantener y resolver.

### Contribución, distribución y emisión

La distinción es de oficio, no de norma.

Las tres clases de señal que se manejan en una emisora, y que conviene no confundir:

| Clase | De dónde a dónde | Calidad |
|---|---|---|
| Contribución | Del exterior HACIA la emisora: el enviado, el estadio, el estudio remoto | La más alta posible: va a sufrir proceso después |
| Distribución | Entre centros de la propia cadena | Alta |
| Emisión o difusión | De la emisora HACIA el público | La que el sistema de difusión permita |

La regla que las ordena: una señal de contribución se comprime lo menos posible, porque
todavía va a pasar por la mesa, por el proceso de emisión y por el codificador de difusión.
Cada compresión con pérdida que se le añade antes de tiempo se paga al final.

Casi todo el enunciado cae en la primera columna: los híbridos, la RDSI, los códecs IP y la telefonía
son maneras de traer al control una señal de contribución y de devolverle al que está fuera lo que
necesita oír. El *streaming* y el pódcast caen en la tercera: son dos formas de llevar el programa al
público por internet.

## Microfonía

### El micrófono de locución

En radio la voz se capta de cerca: es el primer rasgo de la cadena pensada para la voz del epígrafe
«Lo que distingue al sonido de radio». Los tipos de micrófono, los diagramas polares, la
sensibilidad y el efecto de proximidad —el aumento de graves cuando la fuente se acerca a un
micrófono direccional, que en locución se nota y se aprovecha— se estudian en el tema 3. Aquí va lo
que es propio de un estudio de radio: que en el locutorio suele haber varios micrófonos abiertos a la
vez, a poca distancia unos de otros.

### Varios micrófonos abiertos: el filtro en peine

Cuando dos micrófonos abiertos captan la misma voz a distancias distintas, la señal se suma consigo
misma con un pequeño retraso. El fabricante DPA lo explica así: **«Comb filtering occurs when a sound
adds to itself within a short time interval. This interval typically ranges from less than one ms to
approximately 25 ms. Comb filtering can emerge in two ways:»**, que son las reflexiones (**«Due to
reflections»**) y **«Because more than one microphone is open and picking up the same signal at
different positions.»** Y añade: **«In addition, in order for comb filtering to occur, the levels of
the signals must be within 10 dB from each other.»** El nombre
viene de la forma de la respuesta: **«the effect acts as a filter with a frequency response looking
like a comb for the hair»**.

Es el problema típico de una tertulia, y la misma fuente lo describe en un estudio de conversación:
**«In a talk studio, sometimes you can hear that the host's microphone may sound a little muddy, while
the interviewed guest's microphone sounds much cleaner … the voice of the host is picked up by two
microphones with some distance between them»**.

Los remedios que da DPA:

| Remedio | Lo que dice la fuente |
|---|---|
| Atenuar el sonido retrasado | **«Attenuate delayed sound picked up by the microphone by at least 10 dB to minimize the problem of comb filtering»** |
| Regla 3:1 | **«a neighboring microphone should be at least three times further away, (given the sensitivity and the gain is the same on both microphones). (20 *log (1/3) ≈ -10 dB)»** |
| Micrófonos en línea a igual distancia | La proporción, **«in theory, should be 4.5:1»**; pero con micrófonos direccionales **«a distance factor of 3 is normally ok even though there are two neighboring microphones»** |
| Reflexiones | Quitar o girar la superficie que refleja, absorberla, o poner el micrófono sobre ella: **«In this way, it becomes a boundary layer microphone»** |

Lo que eso significa en la operación (oficio): en una tertulia se abre sólo el micrófono de quien
habla o se bajan los que no hablan, y cada invitado se sienta de modo que su micrófono le quede
mucho más cerca a él que a su vecino. Un micrófono abierto de más no suma voz: suma coloración.

## Mesa

### Las fuentes que llegan a la mesa

La estructura de una mesa, sus entradas y salidas, los auxiliares, la escucha previa (PFL) y el DIM
se estudian en el tema 4. Lo propio de un control de radio es el tipo de fuentes que entran en ella.
La tabla es de oficio.

Lo que en una emisora se entiende por fuente de reproducción, y qué le pide cada una a la mesa:

| Fuente | Qué exige |
|---|---|
| Servidor de audio o sistema de automatización | Salidas a nivel de línea y arranque por orden: es la fuente principal de una radio moderna |
| Reproductores físicos (disco compacto, giradiscos, cinta) | Previo específico en el caso del giradiscos: nivel muy bajo y la ecualización normalizada de disco de la asociación estadounidense de la industria discográfica (RIAA) |
| Ordenador de redacción o de invitado | Caja de inyección o entrada de línea desbalanceada: es la que más ruido de masa introduce |
| Teléfono e híbrido telefónico | Un N-1 propio: el híbrido separa la ida de la vuelta sobre una sola línea |
| Códec de contribución | Su N-1 y su retorno |

Las dos últimas filas son las que hacen distinta una mesa de radio: cada línea exterior —teléfono o
códec— entra por un canal y necesita que la mesa le devuelva una mezcla hecha a su medida. Esa mezcla
es el N-1.

### El N-1: la resta que hace posible un directo

Una conexión en dúplex N-1 entre dos mezcladores es aquella que envía todas las señales a la mezcla
del envío excepto la que nos envían. La definición es de oficio.

La aritmética del nombre lo explica entero: si hay N fuentes, al que está al otro lado se le
manda N MENOS UNA: todas menos la suya.

Por qué: porque el enlace tiene retardo. Si al enviado especial se le devuelve su propia voz
con doscientos milisegundos de retraso, se oye a sí mismo con eco y no puede hablar. La solución
no es bajarle el volumen —entonces no oiría el programa—: es quitarlo de su mezcla.

Tres ideas que parecen N-1 y no lo son (oficio): sumar las señales restando el primer canal (la resta
tiene que ser la del que escucha, no la de un canal cualquiera); enviar todas las señales recibidas
(eso es un retorno de programa completo, lo contrario del N-1); y «evitar el retardo entre
codificadores» (el N-1 no quita el retardo: quita la señal que ese retardo haría insoportable).

La distinción con el retorno de programa:

| Retorno | Qué lleva | Cuándo se usa |
|---|---|---|
| De programa (ST) | Todo lo que sale al aire, en estéreo | Cuando el que escucha NO está en antena |
| N-1 | Todo menos la propia señal del que escucha | Cuando el que escucha SÍ está en antena |

### La mezcla menos en una consola digital

En una mesa analógica el N-1 se monta a mano con un auxiliar: se envía a ese bus todo lo que el de
fuera tiene que oír y se deja sin enviar su propio canal (oficio). Las consolas digitales lo
automatizan. En la Yamaha CL, tomada como ejemplo de fabricante: **«The Mix Minus function removes a
specific channel signal from the signals sent to the MIX/MATRIX buses. You can use this function to
quickly send monitoring signals to a performer or announcer simply by removing his or her audio
signal.»**

El envío que alimenta un retorno conviene que sea previo al fader, por la misma razón que el de los
monitores de escenario (tema 4): así la mezcla del que está fuera no cambia cada vez que el técnico
mueve un fader del programa. Yamaha lo dice de los envíos previos en general: **«Pre-fader auxiliary
sends are independent of the channel fader position and are often used for independent mixes: stage
monitors and recording sends.»** Aplicarlo al N-1 es oficio.

### Dos líneas, dos retornos

El caso que mejor mide si se ha entendido el N-1 (oficio). La emisora es cabecera y tiene una
conexión con exteriores por dos caminos —una línea principal y una de reserva— desde su múltiplex, que
es la matriz desde la que se reparten las líneas. ¿Qué retornos se mandan para no devolver señal?

La respuesta: retorno N-1 excluyendo la línea de reserva a la línea principal, y retorno N-1
excluyendo la línea principal a la línea de reserva. El razonamiento:

1. El exterior está en antena, así que su retorno tiene que ser N-1. Mandar programa estéreo por
   cualquiera de las dos líneas le devolvería su voz.
2. Pero hay DOS líneas y las dos traen la misma voz. Restar sólo «la línea principal» del
   retorno que va por la principal no basta: por la reserva sigue entrando esa misma voz, y
   volvería.
3. La única que cierra el lazo por los dos caminos es excluir de cada retorno la OTRA línea
   —además, desde luego, de la propia—, de modo que ninguna de las dos vías puede devolverle al
   enviado su propia voz.

La lección que deja, y vale para cualquier montaje redundante: la redundancia duplica los
caminos de vuelta igual que los de ida. Un N-1 pensado para una sola línea deja de proteger en
cuanto se añade la de reserva.

### Las órdenes

El control habla al locutorio y a los de fuera por el circuito de órdenes. Yamaha lo define así:
**«Talkback is a function that sends the signal of a mic connected to the TALKBACK jack to the desired
bus. This is used mainly to convey instructions from the operator or sound engineer to the performers
and staff.»** Y mientras se habla, la consola puede bajar la escucha: **«When talkback is on, you can
use the talkback dimmer to lower the monitor levels other than the talkback signal»**. Si las órdenes
se meten en el bus de un N-1, el de fuera las oye por su retorno sin que salgan al aire (oficio). La
comunicación con realización y el intercom se estudian en el tema 8.

## Híbridos

### Qué es un híbrido: de dos a cuatro hilos

Una línea telefónica lleva la voz que va y la que viene por el mismo par de hilos; la mesa, en
cambio, trabaja con una entrada y una salida separadas. El híbrido es el aparato que pasa de una
cosa a la otra. La definición es de un fabricante de intercom (Clear-Com), que los usa también como
enlace con la red telefónica: **«Hybrids are also used in intercom systems as interfaces to telephone
networks»**. Y:

**«The term hybrid refers to a device that converts two-wire to four-wire audio and vice versa. Analog
hybrids initially used transformers [...] and later used op-amps [...]. Digital hybrids with digital
signal processing (DSP) chips are most commonly used».**

| Lado | Qué lleva |
|---|---|
| Dos hilos | La línea telefónica: ida y vuelta juntas por el mismo par |
| Cuatro hilos | Dos caminos separados: lo que se envía a la línea y lo que se recibe de ella, cada uno por su lado |

En el control, el lado de cuatro hilos se conecta a la mesa: lo recibido entra por un canal y lo
enviado sale de un bus de la mesa, que es el N-1 de esa línea (oficio).

### La pérdida transhíbrida y el ajuste de nulo

El híbrido perfecto no dejaría pasar nada de lo enviado hacia lo recibido. El real deja pasar algo, y
eso se mide. Clear-Com: **«we evaluate this with a metric called ‘trans-hybrid loss’. This is a
measure of the loss or isolation between the transmit and the receive ports on the four-wire side of
the circuit – in this case ‘loss’ being desirable up to some amount. Trans-hybrid loss depends on
signal cancellation accomplished through defining the line impedance and mirroring it in a balanced
network.»**

Es decir, la pérdida transhíbrida es el aislamiento entre el puerto de envío y el de recepción en el
lado de cuatro hilos, y aquí «pérdida» es algo bueno: cuanta más, menos se cuela lo enviado en lo
recibido. Se consigue cancelando la señal: el híbrido imita la impedancia de la línea en una red
equilibrada. La misma fuente advierte de la dificultad: **«The variations in impedance presented on the
two-wire side of the hybrid make balancing difficult and often result in poor trans-hybrid loss.»**
Cómo cancela, dicho del híbrido de un puesto de intercom: **«There should be no component of the talk
signal in the listen signal. This is accomplished by adding an inverse polarity copy of the talk to the
Listen. The level of the inverted talk signal must be exactly the same amplitude as the 2wire
circuit.»**

El ajuste que busca esa cancelación es el nulo: **«Null: Nulling refers to adjustments made in
balancing a network to achieve greater trans-hybrid loss [...]. Modern hybrids are digital, thus
capable of auto-nulling.»** Los híbridos digitales lo hacen solos.

### El híbrido y el N-1

Y el híbrido telefónico merece una línea, porque es el N-1 hecho aparato: su trabajo es separar
en una sola línea la voz que va de la que viene. Cuando ese aislamiento no es perfecto, lo que
vuelve es eco, y es el mismo problema que el N-1 resuelve en un enlace de dos direcciones.

El riesgo que añade la fuente: **«High gain between the send and receive poses a risk of oscillation
or ‘howling’ resulting from acoustic and/or electronic coupling within a headset or between a speaker
and a microphone.»** Es decir, con mucha ganancia entre envío y recepción, el acoplamiento acústico o
eléctrico —en unos auriculares, o entre un altavoz y un micrófono— puede hacer oscilar el circuito: un
pitido. Que una pérdida transhíbrida escasa lo favorece, porque devuelve más señal, es oficio.

### Un caso práctico: el oyente en antena

Un oyente entra por teléfono y en el control se oye con eco al presentador por el canal del teléfono
(oficio, sobre lo anterior):

1. Se comprueba que el bus que alimenta el envío del híbrido es un N-1: si lleva el propio canal del
   teléfono, la voz del oyente vuelve a la línea.
2. Si el N-1 está bien, lo que vuelve es la fuga del híbrido: poca pérdida transhíbrida. Se rehace el
   nulo (un híbrido digital lo ajusta solo) o se
   baja el nivel de envío.
3. Si aparece un pitido, sobra ganancia entre envío y recepción: se baja antes de que oscile.

## RDSI/IP

### La RDSI

Qué es: la red digital de servicios integrados fue durante veinte años el enlace de
contribución de radio por excelencia. Sobre una línea telefónica digital daba dos canales de 64
kilobits por segundo, que combinados y con un códec adecuado permitían mandar audio de calidad de
radio desde cualquier sitio con teléfono.

Las cifras son las de la recomendación de la UIT que define los interfaces de la RDSI (UIT-T I.412):
**«La estructura de interfaz básica se compone de dos canales B y un canal D (2 B + D). El canal D en
esta estructura de interfaz tiene una velocidad de 16 kbit/s.»**; **«Un canal B es un canal a 64 kbit/s
acompañado de temporización.»**; y **«Los canales B pueden utilizarse independientemente, es decir, en
conexiones diferentes al mismo tiempo.»** Los canales B llevan la información del usuario (el audio);
el D **«está previsto principalmente para transmitir información de señalización»**. La I.412 es de
noviembre de 1988 y sigue en vigor.

Sus tres virtudes explican por qué duró tanto y por qué se echa de menos:

1. Establecía una LLAMADA, no una conexión a una red compartida: el ancho de banda estaba
   garantizado de extremo a extremo.
2. El retardo era bajo y CONSTANTE.
3. Funcionaba en cualquier sitio con línea telefónica.

### Por qué se pasa a IP

La UER lo explica en su norma de interoperabilidad (EBU Tech 3326, § 1.1): **«Increasingly,
broadcasters are using IP connections for the purposes of streaming high-quality broadband audio to
their production centres. This is in part accounted for by the fact that several countries are
withdrawing ISDN services, which have been heavily used for contribution in the past.»** Es decir, dos
razones: IP permite audio de banda ancha y la RDSI se está retirando.

La contrapartida (oficio): IP es más barato y más flexible, pero tiene el problema que la RDSI no
tenía: una red compartida no garantiza nada. Los paquetes pueden llegar tarde, desordenados o no
llegar. De ahí que los códecs sobre IP lleven búferes de fluctuación y corrección de errores, que se
ven más abajo.

Y el problema de la transición: **«About 15 to 20 manufacturers currently provide units capable of
transferring audio over both ISDN and IP connections, and efforts must be made to achieve
interoperability between units from different manufacturers.»** Para que códecs IP de marcas
distintas se entiendan hace falta una norma común. Esa norma es ACIP.

### La norma ACIP: EBU Tech 3326

La EBU Tech 3326 (*Audio contribution over IP – Requirements for Interoperability*, revisión 4,
noviembre de 2014) fija **«a minimum set of requirements necessary to ensure interoperability between
equipment intended for the transport of contribution-quality audio over IP networks»**. Es un
mínimo común para que dos códecs de fabricantes distintos se conecten; las buenas prácticas van en
otro documento: **«Best practices and other considerations not directly linked to interoperability
are published in EBU Tech 3329»** (§ 1.4).

Su vocabulario obligacional lo define la propia norma en su alcance, y en un test decide la respuesta:

| Término | Qué significa en la norma |
|---|---|
| MUST, SHALL | **«identify mandatory elements»**: obligatorio |
| SHOULD, RECOMMENDED | **«identify elements that are not mandatory, but whose implementation is advisable»**: recomendado |
| MAY, OPTIONAL | **«identify facultative elements which, if present, SHOULD be implemented as specified for better interoperability with other equipment implementing the same elements»**: opcional, pero si se implementa, como dice la norma |

Distingue tres tipos de contribución (§ 1.2):

| Tipo | Ejemplos de la norma | Latencia |
|---|---|---|
| **«Unidirectional with no return channel»** | **«contribution by satellite»** | — |
| **«Bidirectional where the return audio is narrowband and for the purposes of cueing the contribution»** | **«concert, football commentary»** | **«Latency is not an issue.»** |
| **«Bidirectional with bidirectional broadband audio»** | **«interview, discussion»** | **«Latency is an issue.»** |

Es decir: en una retransmisión de fútbol el retorno sólo sirve para dar paso y puede ir en banda
estrecha, y el retardo no molesta; en una entrevista las dos voces van en banda ancha y en antena, y
el retardo sí importa.

Y dos clases de equipo (§ 1.3): **«General contribution equipment: Equipment meant for all type of
contribution (fixed or remote).»** y **«Portable contribution equipment: Equipment meant mainly for
monophonic speech contribution at low bitrates.»**, cuyos requisitos son **«less stringent»**.

Regula cuatro áreas (§ 1.4): el transporte sobre IP, **«including port definition and packet loss
recovery mechanisms»**; **«Audio coding algorithms to be implemented»**; **«Audio frame
encapsulation»**; y **«Signalling: defines connection setup and termination procedure»**.

### El transporte

Lo que la Tech 3326 fija en su § 2:

| Elemento | Nivel | Texto |
|---|---|---|
| IPv4 | Obligatorio | **«IP version 4 as defined in RFC791 MUST be used.»** |
| IPv6 | Recomendado | **«IP version 6, as defined in RFC2460, SHOULD be supported.»** |
| Multidifusión | Recomendada | **«SHOULD be available for sending and receiving according to RFC1112»** |
| RTP sobre UDP | Obligatorio | **«Realtime Transport Protocol (RTP) over UDP SHALL be used as transport protocol»**, según RFC3550 y RFC3551 |
| RTCP | Recomendado | **«RECOMMENDED»** |
| Puertos | Recomendados | **«Port 5004 (RTP) and port 5005 (RTCP) SHOULD be used as default ports.»** |
| TCP | Opcional | **«MAY be implemented in addition to RTP»**; puerto por defecto 5004 para **«RTP over TCP»** |

Contra la pérdida de paquetes, la norma prevé dos mecanismos (§ 2.2.6 y 2.2.7). La corrección de
errores hacia delante: **«If FEC is required, RTP Payload Format for Generic Forward Error Correction as
described in RFC5109 SHOULD be used.»**, con **«Port 5006»** por defecto; el soporte según la RFC2733 es
**«OPTIONAL»**. Y la retransmisión: **«Active recovery by using retransmission according to RFC4588 MAY
be used.»**, para la que hace falta el perfil RTP extendido de la RFC4585.

### La señalización: cómo se establece la llamada

Lo que la Tech 3326 fija en su § 4:

- Descripción de la sesión: **«Session Description Protocol according to RFC4566 MUST be used for
  session description.»**
- Enlaces unidireccionales por multidifusión: **«SAPv1 according to RFC2974 SHOULD be supported.»**
- Enlaces bidireccionales: **«SIP, according to RFC3261, MUST be used as the signalling method for
  bidirectional links. The SIP requests ‘INVITE’, ‘ACK’, ‘BYE’ and ‘OPTIONS’ MUST be supported for
  basic communication. SIP registrar MUST also be supported so ‘REGISTER’ message MUST be
  supported.»**
- Puerto: **«5060 MUST be used as a default port for establishment.»**
- Negociación del códec: **«the model described in RFC3264 (An Offer/Answer Model with the Session
  Description Protocol) MUST be used. User SHOULD be able to define prioritisation of codec.»**
- Cambio de códec en plena llamada, que es recomendado (**«Reconfiguration SHOULD be supported.»**):
  **«the sender MUST send a new SIP INVITE command with SDP
  signalling the new codec to be used. The receiver replies with a SIP ACK command»**.

Dicho en corto: un códec ACIP llama a otro como un teléfono por internet. SIP establece y cuelga la
llamada (por el puerto 5060); SDP describe qué códec y qué parámetros se usan, con un modelo de
oferta y respuesta; y el audio viaja después por RTP sobre UDP (por defecto, puerto 5004).

### Los perfiles: EBU Tech 3368

Configurar a mano todos los parámetros de una conexión en plena calle no es práctico. La EBU Tech 3368
(*Audio contribution over IP – Profiles*, versión 1.0, noviembre de 2014) lo resuelve con perfiles:
**«audio engineers or reporters should not be required to specify these parameters in detail;
instead, it would be more useful to be able to select a profile to use for this particular
connection»** (§ 1).

Definición: **«A profile is a set of parameters describing how to transmit and receive audio streams
and for the decoder to successfully decode the audio, based on the parameters sent.»** Y: **«It must
be possible to store a number of pre-configured profiles in all user agents.»** (§ 2).

Los parámetros de un perfil (tabla 1 de la norma): número y nombre del perfil, algoritmo de
codificación, velocidad, frecuencia de muestreo, modo de canal, versión, **«RX jitter buffer»**,
**«Packet length»**, **«QoS-Recommendation»** y **«Protection»**. La norma añade al SDP su propio
atributo, **«a=ebuacip:»**, en su versión 0 (**«a=ebuacip:version 0»**), con parámetros como
**«jb (jitter buffer)»**, **«jbdef»**, **«plength (packet length)»**, **«qosrec»** y **«protp»**.

El perfil asimétrico **«specifies different parameter values for the sent and received streams»**; el
ejemplo de la norma es **«a DSL line with low upload capacity and high download capacity»**. Se
señala con **«a=sendonly and/or a=recvonly»** (§ 2.1). En la práctica (oficio): desde una línea con
poca subida se envía con una velocidad baja y se recibe el retorno con otra más alta.

Si el que recibe la llamada no acepta ninguna de las opciones ofrecidas (la norma lo explica con el
ejemplo de tres opciones de búfer), **«the invitation will be rejected with a "488 Not Acceptable
Here" response, as defined in RFC3261»** (§ 3.4.4.1).

### El búfer de fluctuación

Los paquetes no llegan a ritmo constante por una red IP. El códec receptor los guarda un tiempo en
un búfer antes de reproducirlos, y el tamaño de ese búfer decide entre cortes y retardo. La Tech 3368
(§ 3.4): **«If the jitter buffer is too small, packets can fill up the buffer quicker than they can be
played out, causing packets to be lost [...]. If the jitter buffer is too large, all packets can
expect to be safe, but then the total delay in the system may be unacceptably high, particularly for
two way conversations»**.

| Búfer | Qué pasa |
|---|---|
| Demasiado pequeño | Se pierden paquetes: cortes y chasquidos |
| Demasiado grande | No se pierde nada, pero el retardo total crece, y en una conversación de ida y vuelta puede ser inaceptable |

Puede ser adaptativo, con un mínimo y un máximo, o estático, de tamaño fijo (§ 3.4.1 y 3.4.2).

El caso práctico que da la propia norma (§ 3.4.3): un equipo en la red corporativa con un búfer fijo
de **«six milliseconds»** recibe una llamada desde la wifi de un hotel: **«this call will fail or at
the very best be full of audio glitches, since the stream is transported over the public Internet»**.
La lección: un búfer muy corto sirve en una red controlada, no en internet pública; para un enviado
que conecta desde una red pública se usa un búfer mayor, o adaptativo, y se acepta más retardo.

### Calidad de servicio y protección

Para que la red trate los paquetes de audio con prioridad, la Tech 3368 (§ 3.6) exige el método
DiffServ: **«The DiffServ method as described in RFC2474 shall be implemented. The DS field is the 6
most-significant bits of the deprecated TOS field»**. Con una salvedad: recomendar un valor
**«is only relevant if the callee is located in a known network, where DSCP values are not ignored or
stripped from the packets in at least part of the transmission path»**.

Y contra la pérdida de paquetes enumera tres protecciones (§ 3.7.2): **«Media duplication
redundancy»** (mandar el flujo duplicado), **«Forward error correction»** (mandar datos de más con
los que el receptor reconstruye lo perdido) y **«Multiplexing protection»**.

### Qué enlaces sirven para una conexión de ida y vuelta

Un códec de contribución en una entrevista necesita ida y vuelta, y no todo enlace la da. La
palabra que decide es «bidireccional»: el DAB es un sistema de DIFUSIÓN. Va de un
transmisor a muchos receptores y no tiene camino de vuelta. Los otros tres —fibra,
telefonía móvil y satélite— son enlaces de red y los tres permiten ida y vuelta.

| Enlace | Bidireccional | Qué lo caracteriza |
|---|---|---|
| Fibra FTTH a internet pública | Sí | El más barato y el menos garantizado |
| 3G/4G/5G | Sí | Movilidad |
| Satélite BGAN, Thuraya, banda Ka | Sí | Cobertura donde no hay nada, con retardo alto |
| Microondas por DAB | NO | Es difusión: un emisor, muchos receptores |

La tabla es de oficio. Lo que aquí importa para la radio es que cualquier enlace de ida y vuelta
sirve para un códec IP, y que cada uno pide su perfil: la fibra admite más velocidad y un búfer
menor; el móvil y el satélite, menos velocidad y más búfer.

## Códecs

### Los códecs de la norma ACIP

La Tech 3326 (§ 3) reparte los algoritmos de codificación en tres escalones. Todos tienen que tener
**«an RTP payload format defined and registered at IETF»** (§ 3.3.5).

**Obligatorios** (§ 3.1):

| Códec | Qué dice la norma |
|---|---|
| G.711 | **«ITU G.711 audio coding standard with a bitrate of 64 kbit/s SHALL be implemented.»** Tipos de carga **«‘PCMA’ for A-law with RTP Payload type ‘8’ and ‘PCMU’ with RTP Payload Type ‘0’ for mu-law»**; **«20 ms of audio per RTP packet SHOULD be used as default»** |
| G.722 | **«ITU G.722 audio coding standard with a bitrate of 64 kbit/s SHALL be implemented.»** Tipo de carga 9 |
| MPEG capa II | **«ISO/IEC 11172-3 MPEG-1 Layer II and ISO/IEC 13818-3 MPEG-2 Layer II coding SHALL be implemented.»** Tipo de carga 14 o dinámico; el reloj RTP es **«always 90 kHz»** |
| PCM lineal de 16 bits | **«L16 (RFC3555) Linear audio. Sampling frequencies to be supported: 32 kHz, 48 kHz»**; **«4 ms of audio per RTP packet SHOULD be used as default»**. **«OPTIONAL for portable units»** |
| PCM de 12, 20 y 24 bits | **«DAT12, L20, L24»**; **«12-bit per sample quantization is OPTIONAL»**, y también opcional en los portátiles |

Una rareza de G.722 que puede preguntarse: **«Even though the sampling rate for G.722 audio is 16 kHz,
the RTP clock rate for the G.722 payload format is 8 kHz because this value was erroneously assigned
in RFC1890»**. Es decir, muestrea a 16 kHz, pero en RTP se declara a 8 kHz por un error histórico que
se mantuvo.

Para MPEG capa II la norma da una tabla de velocidades recomendadas de 32 a 384 kbit/s, a 16, 24
(MPEG-2), 32 y 48 kHz, en modos **«M = Mono, JS = Joint-Stereo, S = Stereo»**; a 32 kHz, las
velocidades de 320 y 384 kbit/s quedan marcadas **«frame too large»**. La tabla lleva dos salvedades:
**«Bitrates and sampling rates in bold are mandatory»** (lo demás es recomendado), y las velocidades
de 192, 256 y 384 kbit/s, marcadas con †, son **«OPTIONAL for portable equipment»**.

**Recomendados** (§ 3.2): **«MPEG-4 AAC Low Complexity Profile, MPEG-4 AAC-LD»** (con RFC3640, y
**«High bitrate AAC profile (AAC-hbr) MUST be supported and SHOULD be used»**) y **«Standard/Enhanced
APT-X»**, un **«ADPCM based format»** (RFC7310).

**Opcionales** (§ 3.3): MPEG-1/2 capa III; MPEG-4 HE-AACv2; Opus, **«Free Open source voice/music
codec with bitrates ranging from 6 kbit/s to 510 kbit/s as defined in RFC6716»**; y AMR-WB/AMR-WB+
(**«AMR-WB (G.722.2)»**).

| Escalón | Códecs |
|---|---|
| Obligatorios | G.711, G.722, MPEG-1/2 capa II, PCM de 16, 20 y 24 bits (el de 12 bits, opcional; el PCM, opcional en los portátiles) |
| Recomendados | AAC-LC, AAC-LD, APT-X estándar y mejorado |
| Opcionales | MPEG capa III, HE-AACv2, Opus, AMR-WB/AMR-WB+ |

### Qué no es un códec: Dante

Dante no es un algoritmo de compresión. Es un protocolo de transporte de audio sin comprimir
por red local, así que no puede elegirse como algoritmo para una llamada por IP a través de un códec
de contribución. Y aunque se le tomara por tal, no serviría: Dante está pensado para una red local
controlada, con reloj compartido y latencia muy baja. No atraviesa internet pública (oficio). Dante,
AES67 y el audio sobre IP dentro del centro se estudian en los temas 11 y 15.

La diferencia de fondo (oficio): el audio sobre IP de producción —Dante, AES67— mueve audio sin
comprimir por una red controlada; el códec de contribución —ACIP— lleva audio, casi siempre
comprimido, por una red que no se controla, y por eso lleva búfer de fluctuación y protección contra
pérdidas.

### Cómo se elige el códec

Criterios de oficio, sobre la norma:

- Calidad frente a ancho de banda: la regla de la contribución es comprimir lo menos posible
  (epígrafe «Contribución, distribución y emisión»). Si el enlace lo permite, PCM lineal; si no, el
  códec de menos pérdida que quepa.
- Retardo: en una entrevista de ida y vuelta (**«Latency is an issue.»**) se prefieren códecs de bajo
  retardo como AAC-LD (el glosario de la norma lo desarrolla como **«Advanced Audio Coding Low
  Delay»**) y búferes cortos; en un partido con retorno de sólo órdenes el retardo importa menos.
- Compatibilidad: si no se sabe qué hay al otro lado, los obligatorios de la norma (G.711, G.722, MPEG
  capa II, aunque en los portátiles son opcionales sus velocidades de 192, 256 y 384 kbit/s; el PCM
  lineal, salvo en los portátiles) son los que cualquier equipo ACIP tiene que tener.
- Voz frente a música: un equipo portátil está pensado para **«monophonic speech contribution at low
  bitrates»**; un concierto pide equipo general, estéreo y más velocidad.

## Telefonía

### La llamada telefónica en antena

La telefonía entra en el control de dos maneras: por el híbrido, que convierte la línea de dos hilos
en ida y vuelta separadas para la mesa (epígrafe «Híbridos»), y por los códecs IP, que usan la misma
lógica de llamada que un teléfono por internet (SIP, epígrafe «La señalización»). En los dos casos la
mesa tiene que devolver a la línea un N-1.

### Banda estrecha y banda ancha

Los dos primeros códecs obligatorios de la Tech 3326 vienen de la telefonía, y los dos van a
64 kbit/s: G.711, con sus leyes A y mu, y G.722, que muestrea a **«16 kHz»**. La UIT-T I.412 los cita
entre lo que puede llevar un canal B de la RDSI: **«voz codificada a 64 kbit/s, de conformidad con la
Recomendación G.711»** y **«voz de banda ancha codificada a 64 kbit/s de conformidad con la
Recomendación G.722»**. La banda de cada uno la fija la UIT-T. La G.722 describe **«an audio wideband (WB, 50 to 7 000 Hz)
coding system»**, y precisa: **«The nominal 3 dB bandwidth is 50 to 7 000 Hz.»**; de ahí su título,
**«7 kHz audio-coding within 64 kbit/s»**. La voz de G.711 es la de la telefonía clásica, de 300 a
3 400 Hz: la UIT-T G.712, que da las características de transmisión de los canales PCM **«coded in
accordance with ITU-T Rec. G.711»**, fija sus exigencias en esa banda (por ejemplo, la pérdida de
retorno se cumple **«over the frequency range 300 Hz to 3400 Hz»**). En resumen: banda estrecha,
300-3 400 Hz (G.711); banda ancha, 50-7 000 Hz (G.722). Lo que el oyente nota (oficio): una voz por
G.711 suena a teléfono; por G.722, más llena. Para G.711 la Tech 3326 fija por defecto paquetes de 20 ms **«for improved compatibility
with voice-over-IP systems»**.

La norma distingue también el retorno de banda estrecha, que sirve sólo para dar paso (**«for the
purposes of cueing the contribution»**), del de banda ancha que exige una entrevista.

### El teléfono móvil como enlace

La telefonía móvil —3G, 4G, 5G— es hoy uno de los enlaces de contribución de ida y vuelta (tabla de
«Qué enlaces sirven para una conexión de ida y vuelta»). Es el caso del perfil asimétrico y del búfer
adaptativo: la red cambia durante la conexión, y el códec tiene que tolerarlo (oficio).

## Streaming

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

En radio, el *streaming* es la emisión del programa por internet, en directo o a la carta, además de
la emisión por ondas. Para el operador de sonido es un destino más de la mezcla, con sus propias
exigencias de sonoridad (oficio).

### El protocolo HLS

HLS es la retransmisión en directo por HTTP que describe la RFC 8216 (agosto de 2017). Su finalidad,
según la propia RFC: **«HTTP Live Streaming provides a reliable, cost-effective means of delivering
continuous and long-form video over the Internet.»** Permite ofrecer **«multiple renditions of the same content, such as audio
translations»**.

Cómo se organiza: **«A Playlist is either a Media Playlist or a Master Playlist. Both are UTF-8 text
files containing URIs and descriptive tags.»** Y el receptor va cambiando de versión según la red:
**«Clients should switch between different Variant Streams to adapt to network conditions.»**

HLS trocea: **«A Media Playlist contains a list of Media Segments, which, when played sequentially,
will play the multimedia presentation.»**, y permite al receptor **«adapt the bit rate of the media
to the current network conditions in order to maintain uninterrupted playback at the best possible
quality.»** (RFC 8216, 1 y 2). Es la base documentada de la «transmisión por secuencias» y su
adaptación a la red de la tabla de «Qué es el *streaming*». La RFC describe **«version 7 of this protocol»**; su
revisión está en curso como borrador (draft-pantos-hls-rfc8216bis), que no la sustituye todavía.

Su estatus, que en un test importa: **«This document is not an Internet Standards Track
specification; it is published for informational purposes.»** No es una norma de la IETF, sino un
documento informativo; su cabecera lo publica como **«Independent Submission»**, en la categoría
**«Informational»**.

### La sonoridad del *streaming*

La emisión por ondas se mide con la EBU R 128 (tema 13). Para la distribución por internet hay una
recomendación propia de la AES: el documento técnico **«AESTD1008.1.21-9 (supersedes TD1004)»**, de 24
de septiembre de 2021, *Recommendations for Loudness of Internet Audio Streaming and On-Demand
Distribution*. Es una recomendación, no una norma.

El techo de pico: **«For all content, it is recommended that the Maximum True Peak level not exceed -1
dBTP at the codec input of lossy-encoded streams.»**

La sonoridad de distribución, por tipo de contenido (tabla 1 del documento), con la advertencia que
la precede: **«Distribution Loudness is not to be targeted to the upper tolerance.»** La tolerancia es
un margen, no un objetivo.

| Contenido | Sonoridad de distribución | Tolerancia superior | Cómo se mide |
|---|---|---|---|
| Variado (*assorted*), con voz medible | −18 LUFS | +1 LU | Sonoridad integrada del diálogo |
| Variado, sin voz medible | −18 LUFS | +2 LU, o la propia del formato (tabla 2) | Sonoridad integrada |
| Música, normalizada por pista | −16 LUFS | +0,2 LU | Sonoridad integrada |
| Música, pista más alta del álbum (servicios de música a la carta) | −14 LUFS | +0,2 LU | Sonoridad integrada |
| Piezas intercaladas (*interstitial*) | −18 LUFS | +0,2 LU | Sonoridad integrada |
| Asistente virtual | −18 LUFS | no aplica | Sonoridad integrada de la voz del asistente |

Qué entra en cada fila: «variado» **«applies to radio-style streams, musical concert performances,
podcasts containing speech, music and/or effects elements»** (nota 1); las piezas intercaladas son
**«Interstitial Content such as commercial advertising, public service announcements, promotional
material»** (nota 7). Una emisora de radio por internet es, por tanto, contenido «variado»: −18 LUFS (o, si no trata
voz y música por separado, el valor de su formato en la tabla 2).

Por formato (tabla 2, para quien no puede tratar voz y música por separado, como las emisoras
comerciales que usan proceso de audio radiofónico en línea): informativos y tertulia (*News/Talk*), −18 LUFS; música pop, −16; formato mixto,
−17; deportes, −17; ficción (*Drama*), −18. Los valores se pueden afinar según la proporción de voz, y
el documento da **«A useful formula»**: sonoridad integrada de distribución = −16 − [2 × (porcentaje
de voz / 100)] LUFS. Con un 100 % de voz sale −18; con un 50 %, −17; sin voz, −16.
Sobre la música: **«listener experience can be improved by normalizing music 2 or 3 LU higher than
speech»**. Y la referencia de percepción: **«approximately 1 LU is considered a just noticeable
loudness difference»**.

Relación con la emisión: la propia AES recomienda que, cuando los aparatos avancen y los metadatos de
sonoridad estén más extendidos, se revise el documento **«lowering its Distribution
Loudness recommendations by 6 LU. This will harmonize this document with others such as EBU R 128,
ATSC A/85, ANSI/CTA-2075 and AES71-2018, which recommend -23 to -24 LUFS»**, y producir y archivar
**«at a loudness of -24 LUFS or lower and then remastered for distribution to current devices by
applying linear gain followed by peak limiting if needed»**. Las unidades son las mismas: LUFS y LKFS
**«are identical units of measurement as specified in ITU-R BS.1770»**.

La EBU R 128 remite para el *streaming* a su suplemento R 128 s2, y para la radio a su suplemento
R 128 s3 y a la EBU Tech 3401 (tema 13). Sus cifras no se han leído (ver «Lo que este tema no da»).

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

Lo que eso significa para el operador de sonido (oficio): la programación de radio no acaba en las
ondas; también se distribuye por internet, en directo y a la carta.

## Podcast

### Qué es un pódcast

No hay una definición normativa de pódcast en las fuentes leídas. Para el operador de sonido es un
programa de audio que se publica como fichero para escucharlo a la carta, y que llega al oyente a
través de plataformas (oficio). En Canal Sur, el Contrato-programa lo sitúa **«en el ámbito del audio
digital a través de su propia plataforma digital de servicios Podcast»** (epígrafe anterior), y
atribuye el pódcast a la dirección organizativa **«Canal Sur Media»**.

Frente al *streaming* en directo, el pódcast es un fichero terminado: se puede medir y corregir
entero antes de publicarlo.

### La sonoridad de un pódcast

La AES TD1008 incluye expresamente los pódcast en el contenido «variado» (**«podcasts containing
speech, music and/or effects elements»**): −18 LUFS, medidos sobre el diálogo si la voz es medible, con
+1 LU de tolerancia, y pico verdadero que no pase de −1 dBTP a la entrada del codificador.

Una plataforma concreta pide otra cifra. Apple Podcasts, en sus requisitos de audio para creadores
(requisitos de una empresa, no norma): **«we recommend that the audio signals are preconditioned so
the overall loudness remains around -16 dB LKFS, with a +/- 1 dB tolerance, and that the true-peak
value doesn’t exceed -1 dB FS. The LKFS and true-peak values are calculated according to the ITU-R
BS.1770-5 recommendation.»** Y el orden de las operaciones: **«The preconditioning steps need to occur
before the encoding process [...] audio compression algorithms typically don’t modify the loudness and
might clip the signal if the recommended true-peak value is not respected»**.

| Destino | Sonoridad | Pico | Quién lo dice |
|---|---|---|---|
| Emisión (radio y televisión) | −23 LUFS | Ver tema 13 | EBU R 128 (tema 13) |
| Pódcast o radio por internet | −18 LUFS | −1 dBTP a la entrada del codificador | AES TD1008 (recomendación) |
| Pódcast en Apple Podcasts | En torno a −16 LKFS, ±1 dB | −1 dBFS de pico verdadero | Apple (requisito de plataforma) |

### El formato de entrega

Lo que acepta Apple Podcasts, como ejemplo de plataforma:

- Para subir el audio: **«Apple Podcasts Connect accepts WAV, FLAC, or MP3 audio»**, y **«Single-channel
  audio will not be accepted for WAV or FLAC files.»** Si sólo hay fuente mono (una grabación de
  campo, por ejemplo), en WAV o FLAC Apple pide: **«send the audio source with two identical channels for left
  and right»**; y **«If a stereo audio source exists, it must be used.»** En MP3 se admiten mono y
  estéreo.
- MP3 monofónico: mínimo de **«44.1 kHz»** y **«32 kbps»**; recomendado, **«44.1/48 kHz»** y
  **«96–128 kbps»**. MP3 estéreo: mínimo de **«64 kbps»**; recomendado, **«128–256 kbps»**.
- Por canal RSS: **«For RSS feeds, Apple Podcasts accepts MP3 or AAC formats.»** **«For the same bit
  rate, AAC will result in better audio quality.»**; la plataforma dice: **«we strongly recommend using AAC
  instead of MP3»**. Velocidades recomendadas, iguales para AAC y MP3 (**«These bit rates apply to both
  the AAC and MP3 formats.»**):

  | Canales | 22,05/24 kHz | 44,1/48 kHz |
  |---|---|---|
  | 1 (mono) | 40–80 kbps | 64–128 kbps |
  | 2 (estéreo) | 80–160 kbps | 128–256 kbps |
- Los valores de sonoridad y de pico se pueden incrustar como metadatos en **«the ID3 tags of an MP3
  file or in the header of an MP4 file»**.

### Un caso práctico: de la emisión al pódcast

Un programa de radio emitido a −23 LUFS se va a publicar como pódcast (oficio, sobre las fuentes
anteriores):

1. Se parte de la mezcla de emisión o, mejor, de un máster archivado a −24 LUFS o menos, como
   recomienda la AES, y se remasteriza para la distribución.
2. Se sube la sonoridad hasta el objetivo del destino: desde −23 LUFS, unos 5 LU para −18 LUFS y
   unos 7 para los −16 LKFS de Apple (desde un máster a −24, uno más). Es la ganancia lineal seguida, si hace falta, de limitación de picos que
   describe la AES; en la práctica, un limitador de pico verdadero para no pasar de −1 dBTP.
3. Se mide y se ajusta ANTES de codificar a MP3 o AAC, porque el codificador no corrige la sonoridad
   y puede recortar si no se respeta el pico verdadero recomendado.
4. Se exporta en el formato que pida la plataforma y, si se puede, con los metadatos de sonoridad y
   de pico.

## Recomendaciones técnicas que el tema cita

| Documento | Qué se toma |
|---|---|
| EBU Tech 3326, *Audio contribution over IP – Requirements for Interoperability*, Rev. 4, noviembre de 2014 | ACIP: alcance, vocabulario MUST/SHOULD/MAY, tipos de contribución y de equipo, transporte, códecs obligatorios, recomendados y opcionales, señalización |
| EBU Tech 3368, *Audio contribution over IP – Profiles*, v1.0, noviembre de 2014 | Perfiles, perfil asimétrico, atributo a=ebuacip, búfer de fluctuación, respuesta 488, DiffServ, protecciones |
| AES TD1008.1.21-9, *Recommendations for Loudness of Internet Audio Streaming and On-Demand Distribution*, 24-09-2021 | Sonoridad de distribución por internet y pico máximo |
| RFC 8216, *HTTP Live Streaming*, agosto de 2017 (informativa) | HLS |
| UIT-T G.722, *7 kHz audio-coding within 64 kbit/s*, 09/2012 (en vigor, con su enmienda 1 de 10/2014) | Banda de 50 a 7 000 Hz |
| UIT-T G.712, *Transmission performance characteristics of pulse code modulation channels*, 11/2001 (en vigor) | Canales PCM de G.711; exigencias entre 300 y 3 400 Hz |
| UIT-T I.412, *Estructuras del interfaz y capacidades de acceso de los interfaces usuario-red de la RDSI*, 11/1988 (extracto del Libro Azul; en vigor) | Interfaz básica 2 B + D, canal B de 64 kbit/s, canal D de 16 kbit/s, G.711 y G.722 por un canal B |

## Lo que este tema no da, y dónde está

- Los equipos de sonido de CSRTV (mesas, híbridos, códecs, sistema de emisión de sus emisoras), sus
  procedimientos de operación y su nivel objetivo de sonoridad en radio y en internet: no constan en
  un documento publicado localizado. Del *streaming* y del pódcast de Canal Sur sólo consta lo que dice
  el Contrato-programa.
- El lenguaje de señas entre control y locutorio: no está normalizado, varía de emisora a emisora y
  no hay fuente publicada que lo fije.
- La EBU Tech 3329 (buenas prácticas de ACIP), los suplementos R 128 s2 (*streaming*) y s3 (radio) y
  la EBU Tech 3401 (sonoridad en radio): no se han leído; sus cifras no se dan.
- Los protocolos de contribución por internet que no son de la UER (SRT, RIST) y los de ingesta en
  plataformas (RTMP): en el tema 13 del específico de Cámara Operador se describen SRT y RTMP; para
  la radio no se ha leído fuente.
- Una definición normativa de pódcast y los términos de continuidad de radio (cuña, ráfaga,
  sintonía, careta): no hay fuente leída; la continuidad, las cuñas y las ráfagas, en el tema 9.
- Los tipos y diagramas de micrófono y el efecto de proximidad, en el tema 3; la estructura de la
  mesa, los auxiliares, el PFL y el DIM, en el tema 4; el proceso de la voz (ecualización,
  compresión), en el tema 5; el intercom, el IFB y los retornos en televisión, en el tema 8; Dante,
  AES67 y las conexiones, en los temas 11 y 15; la EBU R 128 y la medición de la sonoridad, en el
  tema 13.

## Trazabilidad

Fuentes releídas en su original el 25/09/2026; el Contrato-programa y la RFC 8216, además, en el tema
13 del específico de Cámara Operador (leídos el 24/09/2026).

| Fuente | Qué sostiene |
|---|---|
| EBU Tech 3326, Rev. 4 (noviembre de 2014) | Retirada de la RDSI y paso a IP; interoperabilidad entre fabricantes; alcance; MUST/SHOULD/MAY; tres tipos de contribución y dos clases de equipo; cuatro áreas; IPv4, IPv6, multidifusión, RTP/UDP, RTCP, puertos 5004 y 5005, TCP, FEC (RFC5109, puerto 5006; RFC2733 opcional) y retransmisión (RFC4588, con el perfil RFC4585); códecs obligatorios, recomendados y opcionales, con tipos de carga, reloj de G.722 y de MPEG, paquetes de 20 y 4 ms y tabla de MPEG capa II; SDP, SAP, SIP y sus mensajes, puerto 5060, oferta y respuesta, cambio de códec y su carácter recomendado; remisión a la Tech 3329; glosario (AAC-LD, *Low Delay*); paquetes de 20 ms por compatibilidad con la voz sobre IP |
| EBU Tech 3368, v1.0 (noviembre de 2014) | Para qué sirven los perfiles; definición; parámetros; a=ebuacip versión 0; perfil asimétrico y DSL; búfer de fluctuación, adaptativo y estático, caso del hotel; respuesta 488; DiffServ y su salvedad de red conocida; tres protecciones |
| Clear-Com LLC, *A Comprehensive Guide to Clear-Com Analog and Digital Partyline Systems*, febrero de 2018 | Híbrido de dos a cuatro hilos; analógicos y digitales; pérdida transhíbrida; dificultad del equilibrado; nulo y autonulo; cancelación por polaridad invertida en el puesto de intercom; riesgo de oscilación y su causa |
| Yamaha Corporation, *CL5/CL3/CL1 V5 Reference Manual*; Yamaha Corporation of America, D. Gould, *Get on the Bus* | Función Mix Minus; envíos previos al fader; órdenes y atenuador de órdenes |
| DPA Microphones, Mic University, E. Bøgh Brixen, «The basics about comb filtering (and how to avoid it)» | Filtro en peine: definición, causas, caso del estudio de conversación, remedios, regla 3:1, 4,5:1 «en teoría» y factor 3 con micrófonos direccionales |
| AES TD1008.1.21-9 (24-09-2021) | Pico −1 dBTP; tolerancia que no es objetivo; tablas 1 y 2 (traducidas en redonda); notas 1 y 7; fórmula; 1 LU; música 2 o 3 LU más alta; revisión condicionada a −23/−24 LUFS; máster a −24 LUFS y remasterización con ganancia lineal y limitación; LUFS = LKFS |
| RFC 8216 (agosto de 2017) | Finalidad de HLS, listas, variantes, versión 7, estatus informativo y envío independiente |
| Apple, *Audio requirements – Apple Podcasts for Creators* (web, sin fecha visible) | Formatos, fuente mono en WAV/FLAC con dos canales idénticos, velocidades de subida y de RSS, AAC frente a MP3, −16 LKFS ±1 dB, −1 dBFS de pico, BS.1770-5, orden de las operaciones y riesgo de recorte, metadatos |
| Contrato-programa 2024-2026 entre el Consejo de Gobierno de la Junta de Andalucía y la RTVA, apartados 3.5 (puntos 45 y 46) y 3.19 (punto 103) | Canal Sur Media, Canal Sur Más y plataforma de pódcast |
| EBU R 128-2023 (V5, noviembre de 2023; tema 13) | Remisión a los suplementos s2 y s3 y a la Tech 3401; −23 LUFS de emisión |
| UIT-T G.722 (09/2012, en vigor), leída el 25/09/2026 | Banda ancha de 50 a 7 000 Hz, ancho de banda nominal a 3 dB, título |
| UIT-T G.712 (11/2001, en vigor), leída el 25/09/2026 | Alcance (canales PCM de G.711); pérdida de retorno entre 300 y 3 400 Hz |
| UIT-T I.412 (11/1988, en vigor), versión española | Interfaz básica 2 B + D; canales B de 64 kbit/s, independientes; canal D de 16 kbit/s, para señalización; G.711 y G.722 por un canal B |

Oficio sin norma detrás, y así se declara: las cuatro características del sonido de radio; el reparto
del estudio, las señas y el autocontrol; la distinción entre contribución, distribución y emisión y
la regla de comprimir lo menos posible; el uso de los micrófonos en una tertulia; la tabla de
fuentes de la mesa; la definición y la aritmética del N-1, su diferencia con el retorno de programa,
el N-1 hecho a mano y con envío previo, los retornos cruzados con línea de reserva, las órdenes por
el N-1; el caso del oyente con eco; que una pérdida transhíbrida escasa favorece la oscilación; las
virtudes de la RDSI; la ventaja y el problema de
IP; qué enlaces son de ida y vuelta y qué perfil pide cada uno; Dante frente a un códec de
contribución; los criterios para elegir códec; la voz por G.711 y por G.722; qué es un pódcast para
el operador; el caso de la emisión al pódcast. Es cálculo, y se puede rehacer: la fórmula de la AES
(−16 − 2 = −18; −16 − 1 = −17) y la subida de −23 a −18 y a −16 LUFS (5 y 7 LU; desde −24, 6 y 8).
