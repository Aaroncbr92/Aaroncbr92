# Tema 15 del específico de Operador/a de Sonido · Audio sobre IP, redes, sincronía, latencia, PTP y redundancia

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 15 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Sin norma legal. Normas técnicas: SMPTE ST 2110-30:2025 (audio PCM sobre IP, por referencia a AES67); SMPTE ST 2110-10:2022 (temporización del sistema y definiciones); SMPTE ST 2059-2:2021 (perfil PTP para radiodifusión) y ST 2059-1:2021 (época SMPTE y alineación de señales); SMPTE ST 2022-7:2019 (conmutación de protección sin cortes). Documentación de fabricante: Audinate, *Dante Controller User Guide*, versión 4.18 (publicada el 6 de mayo de 2026). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | Las normas SMPTE en las ediciones citadas, leídas el 25/09/2026 y vigentes ese día; la guía de Audinate en su versión publicada el 6 de mayo de 2026. El texto de la AES67 (edición 2023) y el del IEEE 1588 no se han leído |
| **Extensión** | 8.700 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); protocolo de internet
(**IP**), en su versión 4 (**IPv4**) y 6 (**IPv6**); protocolo de control de transmisión (**TCP**)
y de datagramas de usuario (**UDP**); protocolo de transporte en tiempo real (**RTP**, *real-time
transport protocol*); protocolo de descripción de sesión (**SDP**) y de inicio de sesión (**SIP**);
protocolo de gestión de grupos de internet (**IGMP**), con el que un equipo pide unirse a un
flujo multicast; Audio Engineering Society (**AES**), Society of Motion Picture and Television
Engineers (**SMPTE**) e Institute of Electrical and Electronics Engineers (**IEEE**); la norma de
interoperabilidad de audio sobre red **AES67**; la norma de audio PCM sobre IP para radiodifusión
**SMPTE ST 2110-30** y la de temporización del sistema **ST 2110-10**; **Dante**, nombre comercial
del sistema de audio en red de la casa Audinate, y su programa de gestión, **Dante Controller**;
protocolo de tiempo de precisión (**PTP**, *precision time protocol*), definido en la norma **IEEE
1588**, en sus versiones 1 (**PTPv1**) y 2 (**PTPv2**); algoritmo de elección del mejor reloj
(**BMCA**, *best master clock algorithm*); protocolo de tiempo de red (**NTP**); modulación por
impulsos codificados (**PCM**), el audio digital lineal sin comprimir; interfaz digital serie de
vídeo (**SDI**); calidad de servicio (**QoS**, *quality of service*) y el campo que la marca en cada
paquete (**DSCP**, *differentiated services code point*); Ethernet de eficiencia energética
(**EEE**, *Energy Efficient Ethernet*); dirección física de la tarjeta de red (**MAC**); red de área local (**LAN**, *local area network*); oscilador de cristal controlado por tensión (**VCXO**, *voltage-controlled crystal oscillator*); tiempo
atómico internacional (**TAI**); parte por millón (**ppm**); megabit por segundo (**Mbit/s** o
**Mbps**) y gigabit por segundo (**Gbit/s** o **Gbps**); milisegundo (**ms**) y microsegundo
(**µs**); el envío a un solo destino (*unicast*) y a varios (*multicast*); el conmutador de red
(*switch*); el reloj que manda (*leader*, antes *master*) y los que le siguen (*follower*, antes
*slave*).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 15):
>
> Audio sobre IP, redes, sincronía, latencia, PTP y redundancia.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: por qué el audio en tiempo real viaja en UDP y no en TCP; qué es Dante,
qué es una suscripción y qué es un flujo; cuántos canales lleva un flujo unicast y uno multicast y en qué se
diferencian; qué es AES67, qué edición cita la ST 2110-30 y qué relación tienen las
dos; qué frecuencia de muestreo es obligatoria en la ST 2110-30 y cuáles son recomendables; qué es
el nivel A, cuántos canales admite cada nivel y qué combinaciones debe admitir un receptor; cuánto ocupa un canal de 48 kHz y 24 bits y cuánto
32 canales en los dos sentidos; cuál es el tamaño máximo de un paquete UDP en la ST 2110-10; qué
pide la red a un conmutador (IGMP, QoS, PTP); qué latencia tiene Dante por defecto, cuál es la
mínima, dónde se ajusta y qué pasa si emisor y receptor no coinciden; qué es el PTP, cómo se elige
el reloj principal, qué versión usa Dante y cuál piden AES67 y ST 2110-30; qué dominio PTP usa
AES67 y cuál es el valor por defecto en el perfil SMPTE; qué es la época SMPTE; cómo funciona la
redundancia de Dante con red primaria y secundaria y qué define la ST 2022-7. En la prueba
práctica: montar una red de audio para un directo, calcular su caudal, localizar por qué un canal
no suena o hace chasquidos, decidir dónde va el reloj de la instalación y cablear la red
secundaria.

<!-- indice -->

## Índice

- [Audio sobre IP](#audio-sobre-ip)
  - [Por qué el audio va por red](#por-qué-el-audio-va-por-red)
  - [Qué protocolo lleva el audio: UDP](#qué-protocolo-lleva-el-audio-udp)
  - [Dante, un sistema propietario](#dante-un-sistema-propietario)
  - [AES67, la norma de interoperabilidad](#aes67-la-norma-de-interoperabilidad)
  - [SMPTE ST 2110-30: el audio de la televisión en IP](#smpte-st-2110-30-el-audio-de-la-televisión-en-ip)
- [Redes](#redes)
  - [Unicast y multicast](#unicast-y-multicast)
  - [El conmutador de red](#el-conmutador-de-red)
  - [El tamaño de los paquetes](#el-tamaño-de-los-paquetes)
  - [Las cuentas de ancho de banda](#las-cuentas-de-ancho-de-banda)
- [Sincronía](#sincronía)
  - [Por qué hace falta un reloj común](#por-qué-hace-falta-un-reloj-común)
  - [Reloj interno o reloj externo](#reloj-interno-o-reloj-externo)
  - [Sincronía entre flujos y con la imagen](#sincronía-entre-flujos-y-con-la-imagen)
- [Latencia](#latencia)
  - [Qué es y dónde se ajusta](#qué-es-y-dónde-se-ajusta)
  - [Los valores de Dante](#los-valores-de-dante)
  - [Qué pasa con una latencia alta o baja](#qué-pasa-con-una-latencia-alta-o-baja)
- [PTP](#ptp)
  - [Qué es el PTP](#qué-es-el-ptp)
  - [Cómo se elige el reloj principal](#cómo-se-elige-el-reloj-principal)
  - [Las versiones: PTPv1 y PTPv2](#las-versiones-ptpv1-y-ptpv2)
  - [El perfil SMPTE: ST 2059-2](#el-perfil-smpte-st-2059-2)
- [Redundancia](#redundancia)
  - [La redundancia de Dante: red primaria y secundaria](#la-redundancia-de-dante-red-primaria-y-secundaria)
  - [La redundancia sin cortes de la SMPTE: ST 2022-7](#la-redundancia-sin-cortes-de-la-smpte-st-2022-7)
  - [Aplicación práctica de la redundancia](#aplicación-práctica-de-la-redundancia)
- [Normas técnicas que el tema cita](#normas-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Audio sobre IP

### Por qué el audio va por red

| | Matriz clásica | Red IP |
|---|---|---|
| Límite | Duro: las entradas y salidas que tenga el bastidor | El ancho de banda |
| Cableado | Un cable por señal | Un cable por EQUIPO, con todas sus señales dentro |
| Cambiar un encaminamiento | Reconfigurar la matriz | Suscribirse al flujo desde el destino |
| Ampliar | Comprar más bastidor | Añadir un equipo a la red |

Y el precio de esa flexibilidad es lo que ocupa el resto del tema: una red no garantiza nada por
sí sola. Hay que darle un reloj común, hay que dimensionar su ancho de banda y hay que
configurarla para que el audio no compita con el resto del tráfico.

La comparación es de oficio. Las conexiones punto a punto (XLR, AES/EBU, MADI, SDI embebido) y la
parte física de Dante como conexión están en el tema 11.

### Qué protocolo lleva el audio: UDP

El protocolo que se utiliza por norma general para audio en red es UDP. Y la razón es exactamente
la contraria de la que la intuición sugiere:

| | TCP | UDP |
|---|---|---|
| Qué hace si un paquete se pierde | Lo PIDE otra vez y espera | Sigue adelante |
| Garantiza la entrega | Sí | No |
| Retardo | Variable, y puede crecer mucho | Bajo y predecible |
| Sirve para audio en tiempo real | NO | SÍ |

El razonamiento: en audio en directo, un paquete que llega tarde es tan inútil como uno que no
llega. Ese instante de sonido ya pasó. Pedir la retransmisión sólo consigue retrasar todo lo que
viene detrás. Es preferible perder una muestra y seguir en hora.

Sobre UDP va RTP, el protocolo de transporte en tiempo real: la ST 2110-30 se define como **«the
real-time, RTP-based transport of PCM digital audio streams over IP networks by reference to
AES67»**, y la ST 2110-10 fija el tamaño máximo de los paquetes UDP (epígrafe «Redes»). Que TCP no
sirva para el directo es oficio; «TCP/IP» es el nombre de la familia de protocolos de internet, no
un protocolo de transporte.

### Dante, un sistema propietario

Dante es el sistema de audio en red de la casa Audinate: un protocolo que permite la transmisión de
señales de audio y control a través de una red Ethernet. Por la misma red viajan el audio y las
órdenes de encaminamiento, de configuración y de supervisión. Un cable hace el trabajo del audio y
el del control (oficio). Es un sistema de una sola casa, no una norma; se gestiona con el programa
Dante Controller, cuya guía es la fuente de este tema.

- Encaminar es suscribirse: **«Dante routing is performed by associating a receiving (Rx) channel
  with a transmitting (Tx) channel. This is called 'subscription'.»** Un canal se nombra con su
  nombre y el del equipo: en el ejemplo de la guía, **«Audio L@Source»**.
- La suscripción viaja en flujos: **«Dante media routing creates flows. Each flow carries several
  channels of audio, or one channel of video from a transmitter to one or more receivers.»** Unicast
  y multicast, en el epígrafe «Redes».
- Formatos: **«Devices can usually be switched between media formats, but will not support more than
  one at a time.»** **«It is only possible to set up a subscription between channels which have a
  common media format. Channels on devices with incompatible formats will be shown in grey, and will
  not be routable.»**

Aplicación práctica: un canal en gris en Dante Controller no es una avería de red; es un formato
(por ejemplo, la frecuencia de muestreo) que no coincide entre emisor y receptor.

### AES67, la norma de interoperabilidad

Qué es la AES67 y qué la distingue de Dante: es una norma de INTEROPERABILIDAD. No pretende
sustituir a los sistemas propietarios, sino definir un terreno común en el que puedan entenderse.
Audinate la define así: **«AES67 is an open standard for audio-over-IP interoperability, allowing
devices from different manufacturers to exchange audio streams.»**

- Edición: la ST 2110-30:2025 cita como referencia normativa **«AES67-2023 AES standard for audio
  applications of networks - High-performance streaming audio-over-IP interoperability»**. El texto
  de la AES67 es de pago y no se ha leído; lo que este tema dice de ella sale de la ST 2110-30, de la
  ST 2110-10 y de Audinate.
- Dante y AES67 no se excluyen: un equipo Dante puede trabajar en modo AES67. **«Devices in AES67
  mode are able to transmit and receive AES67 multicast flows to / from non-Dante AES67-enabled
  devices. Between Dante devices, Dante's native audio transport protocol is used instead (even when
  AES67 is enabled for both devices).»** Según la guía, en ese modo un equipo Dante **«Supports up
  to 8 audio channels at 48 kHz or 96 kHz sample rates»**, y los flujos multicast de Dante pueden llevar audio RTP: **«Multicast flows can carry Dante audio, or RTP audio (AES67 or ST 2110-30).»**
- Reloj: **«AES67 and ST 2110-30 require PTPv2»**, y **«For AES67, the domain number is fixed at
  0.»** (epígrafe «PTP»).
- Direcciones: **«some devices will only subscribe to AES67 flows in the 239.x/16 address range»**,
  y el prefijo de dirección multicast del receptor Dante tiene que coincidir con el del flujo: **«If
  they do not match, the subscription will appear to succeed, but audio will not actually flow.»**

La frecuencia máxima de muestreo de la AES67 no se da: su texto no se ha leído. Lo que sí consta es
lo que dice la ST 2110-30, que la incorpora (apartado siguiente), y que Audinate ofrece el modo
AES67 a 48 y a 96 kHz.

Aplicación práctica: si un equipo Dante está suscrito a un flujo AES67 de otra marca, la
suscripción aparece correcta y no llega audio, lo primero es comparar el prefijo multicast del
receptor con la dirección del flujo.

### SMPTE ST 2110-30: el audio de la televisión en IP

La ST 2110-30 es la parte de audio de la familia ST 2110 de la SMPTE. Audinate la sitúa así:
**«SMPTE ST 2110-30 is a broadcast industry standard for transporting audio over IP networks,
building on AES67 with additional requirements for clocking and network configuration.»** Y
advierte: **«Avoid mixing AES67 and ST 2110-30 modes on the same network unless you understand the
implications for clocking and compatibility.»**

Lo que fija la norma (edición de 2025, **«Revision of SMPTE ST 2110-30:2017»**):

- Alcance: **«This standard specifies the real-time, RTP-based transport of PCM digital audio
  streams over IP networks by reference to AES67. An SDP-based signaling method is defined for
  metadata necessary to receive and interpret the stream.»** Y un límite: **«Non-PCM digital audio
  signals including compressed audio signals are outside the scope of this standard.»**
- Base AES67: **«Digital audio streams shall conform to AES67, including the Session Description
  Protocol (SDP) as described in IETF RFC 8866, subject to the constraints in this document.»** Pero
  **«digital audio receivers need not support Session Initiation Protocol (SIP)»**.
- Frecuencia de muestreo: **«All senders and receivers of PCM digital audio conforming to this
  standard shall support a digital audio sampling rate of 48 kHz, and should support digital audio
  sampling rates of 44.1 kHz, or 96 kHz, or both. Other sampling rates are out of scope.»** Los 48
  kHz son obligatorios («shall»); 44,1 y 96 kHz, recomendables («should»).
- Nivel mínimo: **«All senders and receivers shall be compliant to Level A as defined in this
  document.»**

Los niveles de los emisores (tabla 2 de la norma; el tiempo de paquete es lo que dura el audio que
va en cada paquete):

| Nivel | Muestreo (Hz) | Tiempo de paquete (µs) | Canales |
|---|---|---|---|
| A | 48000 | 1000 | 1 a 8 |
| AX | 96000 | 1000 | 1 a 4 |
| B | 48000 | 125 | 1 a 8 |
| BX | 96000 | 125 | 1 a 8 |
| C | 48000 | 125 | 9 a 64 |
| CX | 96000 | 125 | 9 a 32 |

La guía de Audinate resume los mismos seis niveles con otras cifras de canales para sus equipos
(por ejemplo, **«ST 2110-30 AX: Up to 8 audio channels at 96 kHz with 1ms packet times»** y
**«ST 2110-30 CX: Up to 64 audio channels at 96 kHz with 125 µs packet times»**). No es una
contradicción: la tabla 2 es lo que cada nivel exige, y la propia norma admite más: **«Senders and
receivers may support more channels than required by Table 2, providing they are able to operate
within the maximum number of channels required for the claimed conformance level.»** Para declarar
un nivel, un emisor debe admitir («shall») **«the sampling clock rate, packet time and at least one channel count
within the ranges as defined in Table 2»**.

Los receptores tienen su propia tabla (tabla 3), más exigente: **«To be compliant with a given level,
receivers shall support all possible combinations of sampling clock rate, packet time and channel
count within the ranges as defined in Table 3.»** Leída la tabla, todos los niveles de receptor
incluyen el A; B añade 125 µs a 48 kHz; C lo lleva hasta 64 canales; los niveles X añaden 96 kHz (un
receptor C no recibe 96 kHz; el CX recoge todas las combinaciones):

| Nivel | Muestreo (Hz) | Tiempo de paquete (µs) | Canales |
|---|---|---|---|
| A | 48000 | 1000 | 1 a 8 |
| AX | 48000 / 96000 | 1000 / 1000 | 1 a 8 / 1 a 4 |
| B | 48000 / 48000 | 1000 / 125 | 1 a 8 / 1 a 8 |
| BX | 48000 / 48000 / 96000 / 96000 | 1000 / 125 / 1000 / 125 | 1 a 8 / 1 a 8 / 1 a 4 / 1 a 8 |
| C | 48000 / 48000 | 1000 / 125 | 1 a 8 / 1 a 64 |
| CX | 48000 / 48000 / 96000 / 96000 | 1000 / 125 / 1000 / 125 | 1 a 8 / 1 a 64 / 1 a 4 / 1 a 32 |

Aplicación práctica: un receptor de nivel C recibe tanto un emisor de nivel A (48 kHz, 1 ms, hasta 8
canales) como uno de nivel C (48 kHz, 125 µs, hasta 64). Y como todo equipo debe cumplir el nivel A
(**«All senders and receivers shall be compliant to Level A as defined in this document.»**), un
emisor de nivel C también sabe emitir a 48 kHz y 1 ms.

Dos detalles de la norma con aplicación directa:

- El audio de un SDI no cabe entero en el nivel A: **«SDI allows the carriage of at least 16
  embedded audio channels. Senders wishing to remain in compliance with Level A, can do so by sending
  groups of channels organized into multiple AES67 streams»**.
- El orden de los canales se declara en el SDP con símbolos de agrupación: M (mono), DM (mono dual),
  ST (estéreo), LtRt (estéreo matrizado), 51 (**«L, R, C, LFE, Ls, Rs»**), 71, 222, SGRP (**«One SDI
  audio group»**, cuatro canales) y U01 a U64 (sin definir). El ejemplo de la norma: **«a=fmtp:101
  channel-order=SMPTE2110.(51,ST)»** declara un 5.1 en los seis primeros canales y un estéreo en los
  dos siguientes.

## Redes

### Unicast y multicast

Dante agrupa los canales en flujos de dos tipos:

| | Unicast | Multicast |
|---|---|---|
| Qué es | **«point-to-point from a single transmitter to a single receiver»** | **«one-to-many from a single transmitter to any number of receivers»** |
| Cómo se manda | Una copia POR DESTINO: si tres equipos quieren la misma señal, se manda tres veces | UNA sola copia que la red reparte a quien se haya suscrito |
| Canales por flujo | **«Unicast flows typically have room for 4 channels of audio or 1 channel of video.»** | **«Multicast flows can be configured with up to 64 channels (depending on the Dante device type).»** |
| Ancho de banda | Crece con cada destino | **«consume network bandwidth even if there are no receivers, but do not require additional bandwidth to add more receivers»** |
| Quién lo crea | La suscripción: **«Unicast flows are set up when a receiver subscribes to an available media channel, and are automatically removed when the receiver unsubscribes from all channels in that flow.»** | El emisor: **«multicast flows must be set up on the transmitting Dante device before receivers can subscribe to these flows»** |
| Cuándo conviene | Pocos destinos | Muchos destinos de la misma señal |

Tres reglas de la guía de Audinate:

- **«Dante routing is unicast by default.»**
- **«If many receivers want the same channels, using multicast can reduce overall network use,
  especially on the transmitter, because only one copy of each channel needs to be sent, rather than
  many.»**
- **«Dante receivers will automatically prefer multicast to unicast if it is available.»** Si se crea
  un flujo multicast con canales que un receptor ya recibe en unicast, se pasa al multicast y el
  unicast se quita.

Y un aviso: **«In practice, this usually means that the flow is flooded throughout the network.»**
El multicast, sin un conmutador que lo filtre, llega a todos los puertos (apartado siguiente). La
guía saca la consecuencia: **«100Mbps links in particular are easily saturated when large numbers of
multicast flows exist (and would be overwhelmed by 1 channel of video). Therefore, multicast flows
should only be used when there is a good reason to do so.»**

En la familia SMPTE las dos formas son obligatorias: **«Senders and Receivers shall support IPv4
multicast transmission and reception (respectively) of streams including IGMP signaling as
specified in IETF RFC 3376.»** y **«Senders and Receivers shall support IPv4 unicast addressing of
streams as specified in IETF RFC 791.»** IPv6 es recomendable («should»), no obligatorio.

### El conmutador de red

Un conmutador en una red de audio es un dispositivo que permite la conexión de múltiples
dispositivos en una red, gestionando el tráfico de datos: la definición de un conmutador de red,
sin más, que no hay que confundir con un conmutador de audio (oficio). Pero no vale cualquier
switch. Una red Dante pide conmutadores gestionables, con calidad de servicio para dar prioridad al
audio, con soporte de PTP y, si se usa multicast, con control de suscripciones. Lo que dice la fuente de
cada cosa (el resto del párrafo es oficio):

| Función | Qué hace | Fuente |
|---|---|---|
| IGMP *snooping* | **«Enabling IGMP snooping on the network switch will block multicast media to all switch ports unless a device on that port has specifically requested to join a multicast group (stream).»** | Audinate |
| QoS por DSCP | **«The DSCP is a field in the IP packet header used to classify and prioritise network traffic (Quality of Service, or QoS).»** El reloj PTP va marcado con prioridad alta (epígrafe «PTP») | Audinate |
| Velocidad | **«A gigabit connected device is preferred over a device connected via 100Mbps»** en la elección del reloj; con 100 Mbps la latencia mínima es 1 ms (epígrafe «Latencia») | Audinate |
| EEE desactivado | Entre las causas de pérdida de sincronía: **«Overloaded network links»** y **«Poorly-implemented EEE (Energy Efficient Ethernet)»** | Audinate |

Aplicación práctica: el Wi-Fi y el multicast no se llevan bien. Audinate da como remedio **«remove
all multicast flows and use unicast flows instead; or, reduce the amount of multicast bandwidth on
the network»**, o filtrar el multicast antes del punto de acceso; algunos equipos tienen un puerto
de control que **«automatically filters multicast media traffic»**. Un portátil con Dante
Controller conectado por Wi-Fi a una red con mucho multicast va lento o se cae. Y el Wi-Fi sirve
para el control, no para el audio: **«Dante audio and video transmission over Wi-Fi is not
supported.»**

### El tamaño de los paquetes

La ST 2110-10, que la ST 2110-30 aplica al audio (**«The Standard UDP Datagram Size Limit as
defined in SMPTE ST 2110-10 shall be used.»**), fija dos límites:

- **«The Standard UDP Size Limit shall be 1460 octets.»** Ese tamaño **«includes the length of the
  UDP header (8 octets) and also the RTP headers and data»**.
- **«The Extended UDP Size Limit shall be 8960 octets.»** Es optativo y el audio de la ST 2110-30 no
  lo usa, porque ésta impone el límite estándar.

Por qué 1.460: la norma lo explica en su anexo A. **«the payload of the Ethernet Frame is officially
limited to a maximum of 1500 octets»**, la cabecera IPv4 ocupa 20 octetos y la IPv6, 40, y **«the
larger of the two values is assumed. Thus the "standard" UDP datagram size limit specified in
section 6.3 of this standard is 1500-40 = 1460 octets.»** Además, el emisor no puede trocear:
**«Senders shall ensure that there are no fragmented IP packets in the egress interface of the
Sender»**.

La relación con los niveles de la ST 2110-30 sale por cálculo, suponiendo muestras de 24 bits (3
octetos; la profundidad de bits la fija la AES67, que no se ha leído):

| Nivel | Muestras por canal en un paquete | Canales máximos | Octetos de audio por paquete |
|---|---|---|---|
| A (48 kHz, 1 ms) | 48 | 8 | 48 × 8 × 3 = 1.152 |
| AX (96 kHz, 1 ms) | 96 | 4 | 96 × 4 × 3 = 1.152 |
| C (48 kHz, 125 µs) | 6 | 64 | 6 × 64 × 3 = 1.152 |
| CX (96 kHz, 125 µs) | 12 | 32 | 12 × 32 × 3 = 1.152 |

En los cuatro casos el audio de un paquete ocupa lo mismo y cabe, con sus cabeceras, por debajo de
los 1.460 octetos. Por eso, a igual tamaño de paquete, doblar la frecuencia de muestreo divide por
dos los canales, y acortar el tiempo de paquete de 1 ms a 125 µs permite más canales por paquete
en proporción al número de muestras de cada uno (cálculo, no texto de la norma).

### Las cuentas de ancho de banda

Las cuentas de caudal salen de una misma fórmula:

> Caudal de un canal = frecuencia de muestreo × profundidad de bits

A 48 kHz y 24 bits, un canal son 1,152 megabits por segundo. Ése es el número que hay que tener.

Ejemplo: una red Dante con 32 canales de audio BIDIRECCIONALES a 48 kHz y 24 bits.

1. Un canal: 48.000 × 24 = 1,152 Mbps.
2. Treinta y dos canales: 1,152 × 32 = 36,9 Mbps.
3. Bidireccionales: ×2 = 73,7 Mbps.

La palabra que decide es «bidireccionales»: quien no la lea se queda en 37. Y con 16 bits en lugar
de 24 saldrían 49,2 Mbps.

Segundo ejemplo: 10 canales en unicast. Con cuatro canales por flujo unicast (**«typically»**, dice
Audinate), diez canales necesitan tres flujos: cuatro, cuatro y dos. La guía lo cuenta así en otro
pasaje: los flujos unicast **«support up to 4 channels of audio simultaneously»**, y **«If you were to
then subscribe a fifth audio channel, a second flow would have to be created.»** El caudal de audio en crudo es
10 × 1,152 = 11,5 Mbps; el real es mayor.

Lo que la fórmula no cuenta es la sobrecarga: cada paquete lleva sus cabeceras de Ethernet, IP,
UDP y RTP, y en audio en tiempo real los paquetes son pequeños y frecuentes, así que la proporción
de cabecera es alta. Cuanto más corto el tiempo de paquete, más paquetes por segundo y más
cabeceras (oficio). No se da una cifra de sobrecarga: depende de la implementación. Para ver el
caudal real, Dante Controller muestra por equipo **«an approximation of transmit and receive
traffic over individual device interfaces»** y el ancho de banda multicast de la red.

Aplicación práctica: en el primer ejemplo, cada sentido lleva 36,9 Mbps de audio, y un puerto
Ethernet conmutado transmite y recibe a la vez; un enlace de 100 Mbps lo lleva, pero la cuenta se
hace con margen para la sobrecarga, el reloj y el control, y en instalaciones grandes el núcleo de
la red va en gigabit (oficio).

## Sincronía

### Por qué hace falta un reloj común

Lo que más cuesta entender de este punto: cada equipo de audio digital tiene su propio oscilador,
y dos osciladores nunca van exactamente igual. Si el que manda muestras y el que las recibe no
comparten reloj, cada cierto tiempo sobra o falta una muestra, y eso se oye como un chasquido
periódico.

Audinate lo dice de los relojes de sus equipos: **«Hardware clocks are based on a vibrating
(piezoelectric) quartz crystal. All crystals are slightly different, and vibrate at slightly
different frequencies.»** Para seguir al reloj principal, el seguidor corrige su frecuencia: **«its
frequency must be 'pulled' up or down to match the frequency of the leader clock. The amount that
the clock's frequency is pulled is referred to as 'offset'.»** Y esa corrección tiene un límite:
**«Hardware clocks can only support a certain amount of offset, referred to as 'pull range'. If the
pull range is exceeded, the follower clock will lose sync with the leader clock, and the device will
be automatically muted.»**

Qué desestabiliza un reloj, según la misma guía:

- **«Overloaded network links»**.
- **«Poorly-implemented EEE (Energy Efficient Ethernet)»**.
- **«A leader clock that is derived from an inaccurate external word clock (one that does not run at
  its nominal frequency)»**.

Cómo se ve en Dante Controller: los avisos **«Clock Sync Warning»** (reloj inestable, con riesgo de
perder la sincronía), **«Clock Sync Unlocked»** (**«This will result in the device being
automatically muted until it regains sync.»**) y **«Clock Sync Locked»**; y un histograma del
desfase: **«a stable and accurate clock will show consistently stable offset (with variation in the
order of a few ppm)»**, mientras que uno disperso **«indicates an unstable clock»**.

En una red de audio, el reloj común lo reparte el PTP (epígrafe siguiente). La ST 2110-10 lo pide
como recomendación: **«A Common Reference Clock, potentially derived from a traceable time source,
should be provided and distributed on the network using IEEE Std 1588-2008 Precision Time Protocol
(PTP).»** Proveer ese reloj es recomendación («should»); admitirlo es obligación de todo equipo:
**«All Devices conforming to this standard shall support a Common Reference Clock delivered via IEEE
Std 1588-2008»**.

### Reloj interno o reloj externo

**«Each Dante hardware device can derive its clock from either its high-quality onboard clock
circuit, or an externally connected word clock.»** Con la opción de sincronía externa, el equipo
toma el reloj de palabra del aparato que lo aloja: **«A Dante device set to 'Enable Sync To
External' will use the external word clock from its host equipment to tune its onboard VCXO. A Dante
device with this attribute set will become the PTP Leader Clock, unless there is another Dante
device present with 'Preferred Leader' set.»**

Y una trampa que la guía señala expresamente: **«If device A is deriving its clock from an external
word clock source ('Enable Sync To External'), but device B is set as Preferred Leader, device A
will lose sync with the Dante network and will eventually be muted - unless device B is also
deriving its clock from the same external source as device A.»**

Aplicación práctica: en una instalación con reloj de referencia de la casa, se lleva ese reloj a un
solo equipo Dante por word clock, se activa en él la sincronía externa y no se marca otro equipo
como preferido. Dos relojes que mandan a la vez es la receta del chasquido o del silencio.

### Sincronía entre flujos y con la imagen

El reloj común sirve también para alinear flujos distintos que llegan a un mismo destino. La ST
2110-10 lo explica así: **«For streams which share the same clock source (typically the Common
Reference Clock), inter-stream synchronization at a common destination relies on comparison of RTP
Timestamp values in the RTP packet headers that are transmitted by various Senders.»** Cada paquete
lleva la marca de tiempo de sus muestras; el receptor las pone en hora comparándolas.

La referencia de tiempo común de la familia SMPTE es la época SMPTE: **«The SMPTE Epoch shall be 01
January 1970 00:00:00 TAI.»** (**«The SMPTE Epoch is the same as the PTP Epoch specified in IEEE Std
1588-2008.»**) Sobre ella la ST 2059-1 define la alineación de las señales y **«Formulae which
specify the calculation of SMPTE ST 12-1 Time Address values [...] from SMPTE Profile IEEE Std
1588-2008 PTP data»**: el código de tiempo se calcula a partir del PTP.

Cuando el audio acompaña a una imagen que ha cambiado de cadencia, Dante corrige la frecuencia de
muestreo con el *pull-up/down*: **«to synchronise Dante audio with video that has been converted
from 24 fps to 25 fps, set the sample rate pull-up/down for any relevant Dante audio devices to
+4.1667%.»** Ese ajuste saca al equipo de la sincronía común: **«Devices that are configured with
sample rate pull-up/down operate on separate 'clock domains', which have their own dedicated PTP
clocks»**. Y la consecuencia: **«Dante devices can only transmit media to, and receive media from
other devices on the same clock domain (whether that is PTPv1 or PTPv2). For example, a device with
zero sample rate pull-up/down operates on the default clock domain, and cannot transmit media to, or
receive media from any devices on the +4.1667% clock domain, or the -1% clock domain, etc.»** El
límite: **«Up to 5 separate clock domains can be supported at any one time. All clock domains have
their own leader clock.»** En Dante Controller la suscripción lo avisa con **«Mismatched clock
domains: The transmitter and receiver are not part of the same clock domain»**.

Aplicación práctica: el sonido y la imagen de una emisión en IP se sincronizan porque todos los
equipos cuelgan del mismo reloj PTP; si el audio va sincronizado a otro reloj, ninguna cantidad de
retardo lo arregla de forma estable (oficio). Y si dos equipos Dante de la misma red no se oyen
aunque la suscripción esté hecha, se mira si el *pull-up/down* de uno no coincide con el del otro: están
en dominios de reloj distintos.

## Latencia

### Qué es y dónde se ajusta

La latencia de una red de audio es el tiempo que pasa entre que el emisor muestrea y el receptor
reproduce. En Dante no es casual, sino configurada: **«For Dante audio devices, variation in latency
in the network is compensated for at the receiver. Each receiver has a device latency setting. This
setting defines the latency between the timestamps on the incoming audio samples and when those
samples are played out.»**

Es decir, el receptor no reproduce cada paquete cuando llega, sino cuando toca según su marca de
tiempo más la latencia fijada. Mientras los paquetes lleguen antes de ese plazo, las variaciones de
la red no se oyen. Por eso la latencia tiene que ser mayor que el peor retraso de la red: si un
paquete llega después de su hora, se pierde (oficio, coherente con la negociación que se cita
abajo: **«to ensure that the latency for the subscription is high enough to prevent packet
loss»**).

### Los valores de Dante

- Por defecto: **«The typical default latency for a Dante audio device is 1 msec. This is sufficient
  for a very large network, consisting of a Gigabit network core (with up to 10 hops between edge
  switches) and 100 megabit links to Dante devices.»**
- Mínimo: **«Smaller, Gigabit-only networks can use lower values of latency (down to 150 µsec for very
  fast devices, such as PCIe cards).»**
- Con puertos de 100 Mbps: **«The minimum latency available for a device connected to a 100 Mbps
  network port is 1 msec. Using a latency lower than 1 msec over a 100 Mbps link will result in a
  subscription error, with the tooltip 'Tx Scheduler Failure'.»**
- Dónde se ajusta y cómo se negocia: **«Latency is set on the receiver. However, when a subscription
  is made, there is an automatic negotiation process between the receiver and the transmitter, to
  ensure that the latency for the subscription is high enough to prevent packet loss.»** El ejemplo
  de la guía: un equipo Ultimo admite como mínimo 1 ms, así que una tarjeta PCIe ajustada a 0,25 ms
  que se suscribe a él trabaja a 1 ms (en otro pasaje, la misma guía da 2 ms como mínimo de los
  Ultimo: el ejemplo vale por el mecanismo, no por la cifra).
- Multicast: **«Multicast flows are automatically set to a minimum of 1ms»**.
- Si no coinciden: **«If the transmitter and receiver have different latency settings, Dante will use
  the higher of the two as the effective flow latency.»** Es la latencia de cada flujo, no la de todo
  el sistema.

Los valores recomendados para cada equipo se ven en el propio programa: **«Recommended latency
settings are displayed in Dante Controller, and may also be found in the documentation accompanying
the product.»**

### Qué pasa con una latencia alta o baja

Si una red Dante presenta alta latencia, se introduce un retraso entre la reproducción de las
señales de audio, lo que afecta a la sincronización. La consecuencia de oficio: el problema de la
latencia no es que el sonido llegue tarde, es que llegue a DESTIEMPO respecto a otra cosa —la
imagen, otro camino de audio, el sonido directo de una sala—.

| Latencia | Qué gana | Qué arriesga |
|---|---|---|
| Alta (por ejemplo, 1 ms o más) | Margen para redes grandes, con muchos saltos y enlaces de 100 Mbps | Retraso respecto a la imagen, a otro camino de audio o al sonido directo (retorno de un locutor, monitores de escenario) |
| Baja (hasta 150 µs) | Retardo mínimo | Paquetes que llegan tarde y se pierden (chasquidos, cortes) si la red no es pequeña y toda en gigabit; error de suscripción en enlaces de 100 Mbps |

En la ST 2110-30 lo equivalente es el tiempo de paquete: 1 ms en los niveles A y AX, 125 µs en B,
BX, C y CX. Un paquete no puede salir hasta que el emisor ha reunido su audio, así que el tiempo de
paquete es un retardo mínimo que se suma al de la red y al búfer del receptor (cálculo de oficio).

Aplicación práctica: en un directo en que un locutor se escucha por auriculares a través de la red,
se busca la latencia más baja que la red soporte sin pérdidas; en una red grande con enlaces de
100 Mbps, 1 ms. Y si dos caminos del mismo audio llegan con latencias distintas a la mesa (por
ejemplo, uno por red y otro analógico), se suman con desfase y aparece el filtro en peine (tema 1).

## PTP

### Qué es el PTP

El protocolo de tiempo de precisión (PTP) es el que reparte el reloj común por la red. Lo define la
norma IEEE 1588 (la edición que citan las normas SMPTE leídas es la de 2008; el texto del IEEE no se
ha leído). La ST 2059-2 lo presenta así: **«IEEE Std 1588-2008 is a standard for a Precision Time
Protocol (PTP) that enables precise synchronization of clocks in measurement and control systems
implemented with technologies such as network communication, local computing, and distributed
objects.»** **«The protocol generates a hierarchical relationship among the clocks in the system.
All clocks ultimately derive their time from a clock known as the grandmaster clock. In its basic
form, this protocol is intended to be administration free.»**

Dante lo usa en todos sus equipos: **«All Dante-enabled devices use the IEEE 1588 Precision Time
Protocol (PTP) across the network to synchronize their local clocks to a leader clock, providing
sample-accurate time alignment throughout the network.»**

El PTP no se limita a decir la hora: mide el retardo del camino por la red. En el perfil SMPTE,
**«The delay request-response mechanism shall be the default path delay measurement mechanism. The
peer delay mechanism may also be implemented.»** Cómo corrige cada reloj con esa medida lo
detalla el IEEE 1588, que no se ha leído. Por eso necesita conmutadores que lo traten bien y
no se monta una red de audio con cualquier switch doméstico (oficio). No se confunde con el NTP,
el protocolo con que se ponen en hora los ordenadores: el protocolo de las redes de audio y vídeo
es el PTP (las cifras de precisión de uno y otro no se dan, porque ni el IEEE 1588 ni la
especificación del NTP se han leído).

Los nombres: el reloj que manda en un camino es el *leader* y el que se sincroniza, el *follower*.
La ST 2059-2 recuerda los antiguos: *leader*, **«Referred to as ‘master’ in IEEE Std 1588-2008»**;
*follower*, **«Referred to as ‘slave’ in IEEE Std 1588-2008»**. El *grandmaster* es **«clock within a
PTP domain that is the ultimate source of time for clock synchronization»**. La guía de Audinate
usa ya *Leader* y *Follower*.

### Cómo se elige el reloj principal

En Dante: **«One Dante device will be elected as the PTP Leader Clock for the network; all other
Dante devices act as a PTP Follower Clocks to the elected leader clock.»** Criterios, por orden:

1. **«Devices with clock inputs (e.g. Word Clock or AES3) will be preferred in the election
   process.»**
2. **«A gigabit connected device is preferred over a device connected via 100Mbps.»**
3. **«A tie-breaker rule of the lowest MAC address is used if several equivalent candidate leader
   clocks are available.»**

Y se puede forzar: **«The election process may be overridden by manually setting 'Preferred Leader'
on a device.»** Si hay más de uno marcado, **«the device with the lowest MAC address will be
chosen»**. Al revés, la opción **«PTP Follower Only»** asegura que un equipo **«never becomes the PTP
Grand Leader»**. **«Preferred Leader is not supported for devices in ST 2110-30 mode or AES67 Manual
mode (but is supported for devices in AES67 Auto mode).»**

En el perfil SMPTE, la elección la hace el algoritmo del IEEE 1588: **«The default algorithm defined
in IEEE Std 1588-2008 subclauses 9.3.2, 9.3.3, and 9.3.4 (BMCA) shall be used.»**, con dos
prioridades configurables, *priority1* y *priority2*, que **«specifies the priority to be used in
the execution of the BMCA»** y **«the secondary priority»**. Y la ST 2110-10 pide que los equipos que
no deben mandar se configuren como sólo seguidores: **«Ordinary Clocks which are not intended to
become the PTP leader should be configured with defaultDS.slaveOnly set to TRUE.»**

### Las versiones: PTPv1 y PTPv2

**«Two versions of PTP exist: PTPv1 and PTPv2. By default, Dante devices use PTPv1. However, when
RTP is enabled for a device, it also uses PTPv2»**. Y **«AES67 and ST 2110-30 require PTPv2»**.

| | Dante nativo | Dante con AES67 o ST 2110-30 |
|---|---|---|
| Versión | PTPv1 por defecto | PTPv2 además (el v1 se puede desactivar) |
| Dominio | — | En AES67, **«the domain number is fixed at 0»** |
| Aviso | — | **«PTPv1 Multicast is disabled by default for ST 2110-30 and AES67 with Manual clock mode. Note that this may disrupt clocking if there are PTPv1-only devices on the network and no devices using both PTPv1 and PTPv2 to bridge the protocols.»** |

El dominio PTP: **«Devices with the same PTPv2 Domain Number will participate in the same clocking
group and synchronise with each other. Devices with different domain numbers will ignore each
other’s PTP messages and form separate clock groups.»**

La prioridad del reloj en la red, por DSCP: **«EF is the default value for PTPv2 event packets on
all Dante devices. This value is specified by the AES67 standard.»** **«PTP packets with a DSCP value
of CS7 have higher priority those set to EF. This value is recommended for Dante flows.»**

### El perfil SMPTE: ST 2059-2

Un perfil PTP es, en la definición del IEEE 1588 que cita la ST 2059-2, **«a set of required
options, prohibited options, and the ranges and defaults of configurable attributes»**. El de la
SMPTE: **«This standard specifies a Precision Time Protocol profile specifically for the
synchronization of audio/video equipment in a professional broadcast environment. The SMPTE PTP
profile is based on IEEE Std 1588-2008»**. Su identificador: **«Profile identifier:
68-97-E8-00-01-00»**.

| Parámetro | Valor por defecto | Rango | Qué es |
|---|---|---|---|
| *priority1* y *priority2* | 128 | 0 a 255 | Prioridades en la elección del reloj |
| *domainNumber* | 127 | 0 a 127 | El dominio (grupo de relojes que se sincronizan juntos) |
| *logAnnounceInterval* | 0 | −3 a +1 | Intervalo entre mensajes *Announce*, en logaritmo de base 2 de los segundos: 0 es un mensaje por segundo (cálculo) |
| *announceReceiptTimeout* | 3 | 2 a 10 | Intervalos sin *Announce* antes de dar por perdido al reloj |
| *logSyncInterval* | −3 | −7 a −1 | Intervalo entre mensajes *Sync*: −3 es 1/8 s, ocho por segundo (cálculo) |

El intervalo corto tiene una razón: **«This interval is set to a low value (i.e. high message rate)
to allow clocks to synchronize quickly.»** Además, **«Followers shall support one-step and two-step
clocks.»**, y el *grandmaster* de referencia de una instalación **«shall maintain a frequency such
that the value of the second as measured by the Grandmaster Clock deviates by no more than ± 5
parts per million (ppm) from the SI second.»**

Dos consecuencias de la tabla: el dominio por defecto del perfil SMPTE (127) no es el de AES67 (0),
y la ST 2110-10 pide que los equipos acepten **«any message rates allowed by the SMPTE ST 2059-2
PTP Profile»**, pero que, si hay que intercambiar audio con equipos AES67, las tasas de mensajes
**«should be constrained to simultaneously meet the parametric limits of the Media Profile as
specified in AES67»**. La propia norma remite a **«AES-R16-2016, a technical report regarding the
compatibility of parameter ranges between the AES67 Media Profile and SMPTE ST 2059-2»**, que no se
ha leído.

Aplicación práctica: cuando un equipo AES67 y una red ST 2110 no se sincronizan, lo primero es
mirar el dominio PTP (0 frente a 127 por defecto) y las tasas de mensajes; es la advertencia de
Audinate de no mezclar los dos modos sin entender sus implicaciones de reloj.

## Redundancia

### La redundancia de Dante: red primaria y secundaria

**«Many Dante devices support redundant media routing. These devices have two network interfaces,
named primary and secondary. Primary interfaces should be connected to one physical network. If
redundancy is being used, secondary interfaces should be connected to a second separate network.
Secondary interfaces cannot communicate with primary interfaces.»**

Cómo funciona: **«If the secondary network is connected to a device that supports redundancy, it is
enabled automatically. The same media data is transmitted on both the primary and secondary
networks simultaneously. In the event of a failure on one network, media will continue to flow via
the other network.»**

Dos reglas de cableado:

- **«Dante redundancy requires that both the primary and secondary interfaces on any redundant device
  are connected using the same link speed.»** Primario a 1 Gbps, secundario a 1 Gbps; primario a
  100 Mbps, secundario a 100 Mbps.
- **«Dante devices that do not support redundancy must be connected to the primary network only.»**

El reloj, en redundancia: **«the clock synchronization protocol operates over both primary and
secondary networks. Each network will have a designated PTP leader clock; usually this will be the
same device on both networks.»** Si no es el mismo, **«one device will bridge the clock
synchronization information from the primary to the secondary network, ensuring that all devices
derive their clock from the same source.»** Y **«In event of a failure on one network, a redundant
device will continue to receive clock synchronization information over the other network.»**

### La redundancia sin cortes de la SMPTE: ST 2022-7

La ST 2022-7 es la norma de la redundancia de flujos RTP: **«This standard defines requirements for
multiple redundant streams of RTP packets to allow for the creation of a single reconstructed
output stream through seamless protection switching at the RTP datagram level.»** La idea, en su
introducción: **«seamless reconstruction of a stream of RTP datagrams based on the transmission of
multiple streams of identical content over potentially diverse paths»**, de modo que **«a receiver
could switch between them on a datagram by datagram basis without impact to the content or the
stream.»**

- El emisor: **«The transmitter shall transmit at least two streams, each containing copies of each
  RTP datagram. The RTP header and the RTP payload shall be identical for each datagram copy.»**
- Vale para audio: entre los ejemplos de flujo de entrada cita **«SMPTE ST 2110-30, SMPTE ST 2110-40
  and AES67»**.
- En la familia ST 2110 es la forma obligada: **«When using redundant streams, the streams shall be
  generated using the method specified in SMPTE ST 2022-7 and as constrained in section 8.5 of this standard.»**
  (ST 2110-10; su apartado 8.5 regula la señalización de los flujos duplicados).

Los receptores se clasifican por la diferencia máxima de retardo entre caminos que toleran (PD):

| Clase | Uso de ejemplo | PD, flujos de menos de 270 Mbit/s (SBR) | PD, flujos de 270 Mbit/s o más (HBR) |
|---|---|---|---|
| A, *low-skew* | Enlaces dentro de un centro | ≤ 10 ms | ≤ 10 ms |
| B, *moderate-skew* | Enlaces cortos entre centros | ≤ 50 ms | ≤ 50 ms |
| C, *high-skew* | Enlaces largos o especiales | ≤ 450 ms | ≤ 150 ms |
| D, *ultra low-skew* | **«Physical Layer LAN Redundancy»** | ≤ 150 µs | ≤ 150 µs |

Un flujo de audio cae en SBR, que la norma define como **«a flow of RTP datagrams with a payload bit
rate of less than 270 Mbit/s»** (los 64 canales del nivel C son unos 74 Mbit/s de audio, por
cálculo).

Qué no se afirma: la guía de Audinate no dice que la redundancia nativa de Dante sea la de la ST
2022-7. Las dos mandan lo mismo por dos redes; la norma SMPTE fija, además, cómo el receptor rehace
el flujo paquete a paquete. Si la redundancia de un equipo Dante en modo ST 2110-30 cumple la ST
2022-7 hay que verlo en su documentación.

### Aplicación práctica de la redundancia

- La red secundaria es otra red: conectar el puerto secundario al mismo conmutador que el primario
  no protege de la caída de ese conmutador. Lo que se busca es que ningún fallo único (un
  conmutador, un cable, una fuente de alimentación) corte las dos redes a la vez (oficio).
- Un equipo sin redundancia se cuelga sólo de la primaria; si se enchufa a la secundaria, no oye a
  nadie, porque **«Secondary interfaces cannot communicate with primary interfaces.»**
- La redundancia de la red no sustituye a la de los equipos: si cae el emisor, las dos redes se
  quedan sin audio. Para eso se duplican las fuentes críticas o se prevé un camino de reserva
  (oficio).
- Hay que vigilar las dos redes: Dante Controller muestra por separado el tráfico de la primaria y de
  la secundaria (**«The Secondary Tx B/W column displays an approximation of the current transmit
  bandwidth on the secondary Dante network interface for the device.»**). Una red secundaria caída no se nota en el aire hasta que
  falla la primaria (oficio).

## Normas técnicas que el tema cita

- SMPTE ST 2110-30:2025, *PCM Digital Audio* (aprobada el 1 de octubre de 2025; revisa la de 2017).
- SMPTE ST 2110-10:2022, *System Timing and Definitions* (aprobada el 28 de marzo de 2022).
- SMPTE ST 2059-2:2021, *SMPTE Profile for Use of IEEE-1588 Precision Time Protocol in Professional
  Broadcast Applications*.
- SMPTE ST 2059-1:2021, *Generation and Alignment of Interface Signals to the SMPTE Epoch*.
- SMPTE ST 2022-7:2019, *Seamless Protection Switching of RTP Datagrams*.
- Citadas sin leer: AES67-2023 (la edición que cita la ST 2110-30:2025), IEEE Std 1588-2008 (la que
  citan las normas SMPTE) y el informe AES-R16-2016.

## Lo que este tema no da, y dónde está

- El texto de la AES67 (edición 2023): es de pago y no se ha leído. No se dan su frecuencia máxima
  de muestreo, su profundidad de bits ni los parámetros de su perfil de medios; el tema da lo que
  consta de ella en la ST 2110-30, la ST 2110-10 y la guía de Audinate.
- El texto del IEEE 1588 y la especificación del NTP: no se han leído. No se dan cifras de precisión
  de uno ni de otro.
- La documentación técnica de Dante distinta de la guía de Dante Controller (por ejemplo, la de
  Dante Domain Manager o la de cada equipo): no se ha leído. La guía habla de dominios Dante y de
  relojes de frontera entre subredes, que el tema no desarrolla.
- La sobrecarga real de cabeceras en un flujo Dante o ST 2110-30: depende de la implementación; el
  tema explica el concepto y no da cifra.
- La relación entre la redundancia nativa de Dante y la ST 2022-7: no consta en la guía de Audinate.
- La norma de cableado estructurado (longitudes y categorías de cable de red): no se ha leído; lo
  que se dice del cable, como oficio, está en el tema 11.
- La red de audio de la RTVA y CSRTV (si usa Dante, AES67 o ST 2110, dónde está su reloj de
  referencia, cómo es su redundancia): no consta en un documento publicado localizado.
- Dante, XLR, AES/EBU, MADI y SDI como conexiones, en el tema 11; la frecuencia de muestreo, la
  profundidad de bits y la fase, en el tema 1; el códec y la contribución por IP en radio, en el
  tema 7; el intercom y los retornos, en el tema 8.

## Trazabilidad

Fuentes leídas el 25/09/2026, a través del material de investigación del bloque y releídas en sus
pasajes citados el mismo día; las normas, en su edición vigente ese día.

| Fuente | Qué sostiene |
|---|---|
| Audinate, *Dante Controller User Guide*, versión 4.18.x, documento AUD-MAN-DanteController-4.18.x-v1.0, publicada el 6-V-2026 | Suscripción y nombre de canal; flujos, unicast y multicast, cuatro canales por flujo unicast y quinto canal en un segundo flujo, hasta 64 canales por flujo multicast y saturación de enlaces de 100 Mbps, creación y retirada de flujos, unicast por defecto, preferencia por el multicast, inundación; formatos y canales en gris; modo AES67 (ocho canales, 48 y 96 kHz, protocolo nativo entre equipos Dante, prefijo multicast, 239.x/16); definición de AES67 y de ST 2110-30 y aviso de no mezclarlos; niveles ST 2110-30 según Audinate; IGMP *snooping*; Wi-Fi y multicast, puerto de control; DSCP, EF y CS7; relojes de cuarzo, desfase, margen de corrección, silenciado; *pull-up/down* y dominios de reloj (hasta cinco, aviso «Mismatched clock domains»); causas de inestabilidad; avisos de reloj e histograma; reloj interno y externo, sincronía externa, *Preferred Leader*, *PTP Follower Only*; PTP en Dante, elección del reloj; PTPv1 y PTPv2, dominio 0 en AES67, PTPv1 multicast; latencia en el receptor, 1 ms, 150 µs, 1 ms en 100 Mbps y «Tx Scheduler Failure», negociación, ejemplo Ultimo (y los 2 ms de otro pasaje), multicast a 1 ms como mínimo, la mayor de las dos; audio y vídeo no admitidos por Wi-Fi; valores recomendados; redundancia primaria y secundaria, misma velocidad, equipos sin redundancia, reloj en redundancia; columnas de ancho de banda |
| SMPTE ST 2110-30:2025, *PCM Digital Audio* | Alcance (RTP, PCM, por referencia a AES67, SDP), audio comprimido fuera; referencia a AES67-2023; conformidad con AES67 y SDP, SIP no obligatorio; límite UDP estándar; 48 kHz obligatorio, 44,1 y 96 kHz recomendables; nivel A obligatorio; tabla 2 de niveles de emisores y tabla 3 de receptores, regla de conformidad de emisores y receptores y admisión de más canales (cl. 7); nota del SDI y 16 canales; orden de canales y ejemplo |
| SMPTE ST 2110-10:2022, *System Timing and Definitions* | Límites UDP de 1.460 y 8.960 octetos; cabecera UDP de 8 octetos; sin fragmentación; anexo A (1.500 − 40); IPv4 multicast con IGMP y unicast obligatorios, IPv6 recomendable; reloj de referencia común por PTP (proveerlo, recomendación; admitirlo, obligación); soporte de las tasas del perfil ST 2059-2 y ajuste a AES67; AES-R16-2016; *slaveOnly*; sincronía entre flujos por marcas de tiempo RTP; redundancia por ST 2022-7 y su apartado 8.5 |
| SMPTE ST 2059-2:2021, perfil PTP SMPTE | Presentación del IEEE 1588 (jerarquía, *grandmaster*, sin administración); definición de perfil; alcance; identificador; BMCA; mecanismo de retardo petición-respuesta y de pares; tabla de valores por defecto y rangos; razón del intervalo corto; *one-step* y *two-step*; ± 5 ppm; términos *leader*, *follower* y *grandmaster* |
| SMPTE ST 2059-1:2021, época SMPTE | Época SMPTE (1-I-1970, TAI), igual a la época PTP; alcance, código de tiempo desde datos PTP |
| SMPTE ST 2022-7:2019, *Seamless Protection Switching of RTP Datagrams* | Alcance; introducción (flujos idénticos por caminos distintos, cambio paquete a paquete); al menos dos flujos idénticos; ejemplos de flujo con ST 2110-30 y AES67; definiciones SBR y HBR; clases de receptor A a D y sus PD |

Oficio sin norma detrás, y así se declara: la comparación entre matriz y red; que el audio en
tiempo real use UDP y no TCP y su razonamiento; que «TCP/IP» es una familia de protocolos; que Dante
lleve audio y control por el mismo cable; la necesidad de un reloj común y el chasquido sin él; los
requisitos del conmutador (gestionable, QoS, PTP, control de multicast); que el receptor reproduce
según la marca de tiempo y la latencia debe cubrir el peor retraso; que el problema de la latencia
es el destiempo; la comparación de latencia alta y baja; que el tiempo de paquete es un retardo
mínimo; que un reloj ajeno no se arregla con retardo; la sobrecarga de cabeceras; que el núcleo de
una red grande va en gigabit y el Ethernet conmutado transmite y recibe a la vez; las reglas
prácticas de redundancia (ningún fallo único, redundancia de equipos, vigilar la secundaria). Es
cálculo, y se puede rehacer: 48.000 × 24 = 1,152 Mbps por canal; 36,9 y 73,7 Mbps para 32 canales;
49,2 Mbps con 16 bits; tres flujos para diez canales y 11,5 Mbps; 1.152 octetos de audio por
paquete en los niveles A, AX, C y CX (con 24 bits); 73,7 Mbit/s para 64 canales; los intervalos de
mensajes PTP (2⁰ = 1 s, 2⁻³ = 1/8 s).
