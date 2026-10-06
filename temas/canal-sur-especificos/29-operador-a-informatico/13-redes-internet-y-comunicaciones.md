# Tema 13 del específico de Operador/a Informático · Redes, Internet y comunicaciones

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 13 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Normas técnicas de Internet (RFC del IETF), páginas del comité IEEE 802 y de su grupo 802.11, de la Wi-Fi Alliance, documentación de Microsoft, Google, Juniper Networks, la ICANN, el RIPE NCC y la UIT, la *Brief History of the Internet* de la Internet Society y un manual universitario abierto (Bonaventure, Universidad Católica de Lovaina) |
| Redacción que se estudia | Versión en línea de cada documento el 05-10-2026, leída ese día: TLS 1.3 según el RFC 9846 (julio de 2026), HTTP según el RFC 9110, IPv6 según el RFC 8200, IEEE 802.11-2024 con la enmienda 802.11be-2024 |
| Extensión | 16.000 palabras aproximadamente (con tablas y siglas) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA). Organismos: Consejo Federal
de Redes de los Estados Unidos (FNC, *Federal Networking Council*); Grupo de Trabajo de Ingeniería de
Internet (IETF, *Internet Engineering Task Force*), que publica las peticiones de comentarios (RFC,
*Request for Comments*); Internet Society (ISOC); Corporación de Internet para la Asignación de Nombres
y Números (ICANN) y su función de Autoridad de Números Asignados de Internet (IANA); registros
regionales y locales de Internet (RIR y LIR) y proveedores de acceso (ISP, *Internet service
provider*); el registro regional europeo RIPE NCC; Unión Internacional de Telecomunicaciones (UIT);
Organización Internacional de Normalización (ISO); Instituto de Ingenieros Eléctricos y Electrónicos
(IEEE) y su comité de normas de redes de área local y metropolitana (LMSC, *LAN/MAN Standards
Committee*); el laboratorio de física CERN, donde nació la web; el Instituto Tecnológico de
Massachusetts (MIT); la red ARPANET, con sus procesadores de mensajes de interfaz (IMP, *Interface
Message Processor*) y su primer protocolo (NCP, *Network Control Protocol*), y la red académica NSFNET, de la Fundación Nacional para la Ciencia de los Estados Unidos (NSF). Modelos y protocolos: interconexión de sistemas abiertos (OSI); protocolo de internet (IP) en
sus versiones 4 y 6 (IPv4, IPv6); protocolo de control de transmisión (TCP) y la familia TCP/IP;
protocolo de datagramas de usuario (UDP); protocolo de mensajes de control de Internet (ICMP, e
ICMPv6 para IPv6); protocolo de resolución de direcciones (ARP); protocolo de transferencia de
hipertexto (HTTP), sus métodos GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS y TRACE (verbos en
inglés, no siglas) y su código de éxito 200 OK, y su versión segura (HTTPS); seguridad de la capa de transporte (TLS) y su
antecesora, la capa de conexión segura (SSL, *Secure Sockets Layer*); seguridad estricta de transporte
HTTP (HSTS); QUIC, el transporte cifrado sobre UDP de HTTP/3; sistema de nombres de dominio (DNS), con
los tipos de registro A, AAAA, CNAME, MX (correo), NS (servidores de nombres) y TXT (texto), y DNS sobre
HTTPS (DoH); protocolo de configuración dinámica de equipos (DHCP, y DHCPv6); traducción de
direcciones de red (NAT), de direcciones y puertos (NAPT), de operador (CGN o CGNAT, *carrier-grade
NAT*) y de IPv6 a IPv4 (NAT64), con su complemento DNS64; localizador uniforme de recursos (URL);
protocolos de transferencia de ficheros (FTP) y de transferencia segura sobre SSH (SFTP); intérprete
seguro (SSH, *Secure Shell*); protocolo simple de transferencia de correo (SMTP), de acceso a mensajes
de Internet (IMAP) y de oficina de correos (POP3); protocolo ligero de acceso a directorios (LDAP);
protocolo simple de gestión de red (SNMP); protocolos de encaminamiento BGP (*Border Gateway
Protocol*), RIP (*Routing Information Protocol*), OSPF (*Open Shortest Path First*) y EIGRP
(*Enhanced Interior Gateway Routing Protocol*); encaminamiento entre dominios sin clases (CIDR);
autoconfiguración de direcciones sin estado (SLAAC); direcciones locales únicas (ULA, *unique local
addresses*); cifrado autenticado con datos asociados (AEAD); tiempo de ida y vuelta (RTT, en el modo
0-RTT de TLS); cabeceras de autenticación (AH) y de carga de seguridad encapsulada (ESP); servicios
diferenciados (DS) y notificación explícita de congestión (ECN). Campos y medidas: longitud de la
cabecera (IHL), tiempo de vida (TTL), indicadores DF (*Don't Fragment*) y MF (*More Fragments*),
unidad máxima de transmisión (MTU); GHz (gigahercios) y Mbit/s (megabits por segundo). Redes de área
local: red de área local, metropolitana, personal, regional e inalámbrica (LAN, MAN, PAN, RAN y WLAN); las
variantes de Ethernet de par trenzado 10BASE-T, 100BASE-TX y 1000BASE-T; control de
acceso al medio (MAC) y control de enlace lógico (LLC); código de redundancia cíclica (CRC); la
especificación DIX de Digital, Intel y Xerox; acceso múltiple con detección de portadora (CSMA), con
detección de colisiones (CSMA/CD) y con prevención de colisiones (CSMA/CA), y su antecesor ALOHA;
espacios entre tramas distribuido y corto (DIFS y SIFS); tramas de petición y autorización de envío
(RTS/CTS); protocolo de árbol de expansión (STP, *Spanning Tree Protocol*); red de área local virtual
(VLAN), su punto de código de prioridad (PCP) y el enlace troncal (TRUNK); lista de control de acceso
(ACL); alimentación por Ethernet (PoE). Redes inalámbricas: bandas industriales, científicas y
médicas (ISM); conjunto básico de servicios (BSS) e identificador del conjunto de servicios (SSID);
operación multienlace (MLO); acceso múltiple por división de frecuencias ortogonales (OFDMA);
entradas y salidas múltiples multiusuario (MU-MIMO); modulación de amplitud en cuadratura (QAM);
tiempo de activación programado (TWT); privacidad equivalente a la del cable (WEP, *Wired Equivalent
Privacy*) y protocolo de integridad de clave temporal (TKIP, *Temporal Key Integrity Protocol*);
acceso protegido Wi-Fi (WPA, *Wi-Fi Protected Access*, y sus versiones WPA2 y WPA3); norma de cifrado avanzado (AES, *Advanced Encryption Standard*); tramas de gestión
protegidas (PMF, *Protected Management Frames*). Autenticación: protocolo de autenticación extensible (EAP), EAP
sobre LAN (EAPOL) y sus métodos EAP-TLS, PEAP (EAP protegido) y EAP-MSCHAP v2 (protocolo de
autenticación por desafío mutuo de Microsoft, versión 2); servicio de autenticación remota telefónica
de usuario (RADIUS, *Remote Authentication Dial In User Service*); protocolo punto a punto (PPP);
Servidor de directivas de redes de Windows Server (NPS, *Network Policy Server*); Servicios de dominio
de Active Directory (AD DS); red privada virtual (VPN); ordenador personal (PC).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 13): «Redes, Internet y
> comunicaciones: arquitectura de red de Internet, origen, evolución y estado actual, principales
> servicios, protocolos HTTP, HTTPS y TLS, configuración, privacidad y seguridad de navegadores web;
> protocolos IPv4 e IPv6, cabeceras, direccionamiento, subredes, mecanismos de convivencia y
> transición; redes de área local, conceptos, topologías, control de acceso, segmentación,
> normalizaciones IEEE 802; redes inalámbricas IEEE 802.11, estándares, técnicas de transmisión,
> dispositivos de interconexión, topologías, seguridad y autenticación 802.1x.»

Qué se puede preguntar: cómo define Internet el FNC y qué principios de arquitectura fijó Kahn;
cuántas capas tiene el modelo TCP/IP y cuántas el OSI, y en qué capa trabaja cada protocolo y cada
equipo; cuándo nació ARPANET, cuándo pasó a TCP/IP y cuándo se agotaron las direcciones IPv4; qué
puerto usa cada servicio; qué significa que HTTP sea un protocolo sin estado, qué métodos son seguros
o idempotentes y qué indica cada clase de código de estado; qué aporta TLS y qué versiones están
prohibidas; qué hace y qué no hace la navegación privada; qué campos tienen las cabeceras IPv4 e
IPv6 y cuánto miden; cuáles son los rangos privados y los bloques especiales; cómo se abrevia una
dirección IPv6; cómo se calcula una subred; qué son la pila doble, el túnel y NAT64/DNS64; qué
topologías hay y qué hacen CSMA/CD, CSMA/CA y el paso de testigo; qué separa un dominio de colisión
de uno de difusión y cómo se etiqueta una VLAN; qué grupos de trabajo tiene el comité IEEE 802; qué
nombre comercial tiene cada enmienda 802.11 y en qué banda trabaja; qué técnicas de transmisión
trae cada generación de Wi-Fi; qué es una red de infraestructura y una *ad hoc*; qué exige WPA3 y
cómo funciona la autenticación 802.1X con sus tres papeles. En la aplicación práctica: calcular una
subred o la máscara para un número de equipos, abreviar una dirección IPv6, leer la salida de un
comando de red, situar una avería en su capa y escoger la configuración segura de una red
inalámbrica.

<!-- indice -->

## Índice

- [1. Internet: arquitectura, origen, evolución, estado actual y servicios](#1-internet-arquitectura-origen-evolución-estado-actual-y-servicios)
  - [Qué es Internet](#qué-es-internet)
  - [La arquitectura abierta](#la-arquitectura-abierta)
  - [Las capas: el modelo TCP/IP y el modelo OSI](#las-capas-el-modelo-tcpip-y-el-modelo-osi)
  - [Quién reparte las direcciones y cómo se unen las redes](#quién-reparte-las-direcciones-y-cómo-se-unen-las-redes)
  - [El origen](#el-origen)
  - [La evolución y el estado actual](#la-evolución-y-el-estado-actual)
  - [Los principales servicios](#los-principales-servicios)
- [2. Los protocolos HTTP, HTTPS y TLS](#2-los-protocolos-http-https-y-tls)
  - [HTTP: petición y respuesta, sin estado](#http-petición-y-respuesta-sin-estado)
  - [HTTPS: HTTP sobre TLS](#https-http-sobre-tls)
  - [TLS: qué es y qué garantiza](#tls-qué-es-y-qué-garantiza)
  - [Las versiones: de SSL a TLS 1.3](#las-versiones-de-ssl-a-tls-13)
- [3. Configuración, privacidad y seguridad de los navegadores web](#3-configuración-privacidad-y-seguridad-de-los-navegadores-web)
  - [Configuración básica](#configuración-básica)
  - [Privacidad: navegación privada, cookies y rastreadores](#privacidad-navegación-privada-cookies-y-rastreadores)
  - [Seguridad: listas de sitios peligrosos y conexiones seguras](#seguridad-listas-de-sitios-peligrosos-y-conexiones-seguras)
- [4. Los protocolos IPv4 e IPv6](#4-los-protocolos-ipv4-e-ipv6)
  - [La cabecera IPv4](#la-cabecera-ipv4)
  - [La cabecera IPv6](#la-cabecera-ipv6)
  - [El direccionamiento IPv4](#el-direccionamiento-ipv4)
  - [Las subredes y la notación CIDR](#las-subredes-y-la-notación-cidr)
  - [El direccionamiento IPv6](#el-direccionamiento-ipv6)
  - [Convivencia y transición entre IPv4 e IPv6](#convivencia-y-transición-entre-ipv4-e-ipv6)
- [5. Redes de área local](#5-redes-de-área-local)
  - [Conceptos](#conceptos)
  - [Topologías](#topologías)
  - [Control de acceso al medio](#control-de-acceso-al-medio)
  - [Segmentación](#segmentación)
  - [Las normas IEEE 802](#las-normas-ieee-802)
- [6. Redes inalámbricas IEEE 802.11](#6-redes-inalámbricas-ieee-80211)
  - [Los estándares](#los-estándares)
  - [Las técnicas de transmisión](#las-técnicas-de-transmisión)
  - [Los dispositivos de interconexión](#los-dispositivos-de-interconexión)
  - [Las topologías inalámbricas](#las-topologías-inalámbricas)
  - [La seguridad](#la-seguridad)
  - [La autenticación 802.1X](#la-autenticación-8021x)
- [7. Aplicación práctica](#7-aplicación-práctica)
  - [Los cuatro datos de la configuración y el orden de la avería](#los-cuatro-datos-de-la-configuración-y-el-orden-de-la-avería)
  - [Las herramientas de diagnóstico](#las-herramientas-de-diagnóstico)
  - [Supuestos resueltos](#supuestos-resueltos)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Internet: arquitectura, origen, evolución, estado actual y servicios

### Qué es Internet

El 24 de octubre de 1995 el Consejo Federal de Redes de los Estados Unidos (FNC) aprobó por
unanimidad esta definición: **«"Internet" refers to the global
information system that — (i) is logically linked together by a globally unique address space based
on the Internet Protocol (IP) or its subsequent extensions/follow-ons; (ii) is able to support
communications using the Transmission Control Protocol/Internet Protocol (TCP/IP) suite or its
subsequent extensions/follow-ons, and/or other IP-compatible protocols; and (iii) provides, uses or
makes accessible, either publicly or privately, high level services layered on the communications
and related infrastructure described herein.»** Es decir: un espacio de direcciones único (IP), una
familia de protocolos común (TCP/IP) y unos servicios que se apoyan en ellos.

Internet es la red de redes: un conjunto mundial de redes interconectadas que se comunican mediante
la familia de protocolos TCP/IP. La web no es internet: es uno de los servicios que funcionan sobre
ella, el que usa HTTP para transferir documentos de hipertexto. Otros servicios son el correo
electrónico, la transferencia de ficheros, la mensajería o la voz sobre IP.

### La arquitectura abierta

La idea técnica que hace de Internet una red de redes es la que Robert Kahn llamó *open architecture
networking* (redes de arquitectura abierta): **«the choice of any individual network technology was
not dictated by a particular network architecture but rather could be selected freely by a provider
and made to interwork with the other networks through a meta-level "Internetworking
Architecture"»**. Cada red elige su tecnología (Ethernet, Wi-Fi, fibra, radio, satélite) y todas se
entienden por encima, en IP.

Las cuatro reglas de partida de Kahn explican todavía cómo funciona la red:

1. **«Each distinct network would have to stand on its own and no internal changes could be required
   to any such network to connect it to the Internet.»** Ninguna red cambia por dentro para unirse.
2. **«Communications would be on a best effort basis.»** Entrega «con el mejor esfuerzo»: sin
   garantía; si algo se pierde, lo reenvía el origen.
3. **«Black boxes would be used to connect the networks; these would later be called gateways and
   routers.»** Y esas cajas no guardan memoria de cada flujo, para ser sencillas.
4. **«There would be no global control at the operations level.»** No hay un centro que mande.

### Las capas: el modelo TCP/IP y el modelo OSI

El RFC 1122, que fija los requisitos de los equipos conectados a Internet, enumera cuatro capas
(**«The protocol layers used in the Internet architecture are as follows»**): aplicación, transporte,
internet y enlace. El modelo de interconexión de sistemas abiertos (OSI), base de la normalización de redes en la
Organización Internacional de Normalización (ISO) según el manual de Bonaventure, tiene siete: el mismo manual explica que **«the OSI
reference model refined the application layer by dividing it in three layers»** (sesión,
presentación y aplicación) y que la capa de enlace de TCP/IP **«combines the functions of the physical
and datalink layers»**.

| Modelo OSI (siete capas) | Modelo TCP/IP (cuatro capas) | Ejemplos de protocolo |
|---|---|---|
| 7 Aplicación · 6 Presentación · 5 Sesión | Aplicación | HTTP, DNS, SMTP, SSH |
| 4 Transporte | Transporte | TCP, UDP |
| 3 Red | Internet | IPv4, IPv6, ICMP |
| 2 Enlace de datos · 1 Física | Enlace (acceso a la red) | Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11) |

Una salvedad que puede salir en un test: el RFC 1122 dice que la capa de aplicación de Internet
**«essentially combines the functions of the top two layers -- Presentation and Application -- of the
OSI reference model»**, es decir, nombra dos capas OSI y no tres. La correspondencia de la tabla (las
tres superiores del OSI en la de aplicación) es la que da el manual de Bonaventure y la habitual en
los temarios; si una pregunta cita el RFC 1122, manda su texto.

La regla que sitúa cualquier protocolo sin memorizarlo: si mueve tramas por un cable, es enlace; si
encamina entre redes, es red; si garantiza o no la entrega extremo a extremo, es transporte; si lo
entiende un programa, es aplicación.

| Protocolo | Capa OSI |
|---|---|
| Ethernet | 2, enlace |
| IP | 3, red |
| TCP | 4, transporte |
| HTTP | 7, aplicación |

Los dos protocolos de transporte, frente a frente:

| | TCP | UDP |
|---|---|---|
| Establece conexión previa | Sí | No |
| Garantiza la entrega | Sí: retransmite lo perdido | No |
| Garantiza el orden | Sí: reordena en destino | No |
| Controla la congestión | Sí | No |
| Coste | Retardo variable y más carga | Retardo bajo y constante |

La especificación de UDP lo dice en una línea: **«delivery and duplicate protection are not
guaranteed. Applications requiring ordered reliable delivery of streams of data should use the
Transmission Control Protocol (TCP)»** (la entrega y la protección frente a duplicados no están
garantizadas; quien necesite entrega ordenada y fiable debe usar TCP).

### Quién reparte las direcciones y cómo se unen las redes

Las direcciones se reparten en cascada. Según el RFC 4632, **«the unallocated pool of addresses is
administered by the Internet Assigned Numbers Authority ([IANA]). The IANA makes allocations from
this pool to Regional Internet Registries, as required.»** Los registros regionales (RIR) asignan a
su vez bloques menores a los registros locales (LIR) y a los proveedores de acceso (ISP), que los
dan a sus clientes. Hay cinco registros regionales; uno de ellos es el RIPE NCC.

Entre redes de distintos dueños se encamina por sistemas autónomos. Qué es un sistema autónomo: un
conjunto de redes bajo una misma política de encaminamiento —un operador, una universidad, una
corporación—, identificado por un número que asigna la IANA.

| Familia | Dónde actúa | Protocolos |
|---|---|---|
| Interno | Dentro de un mismo sistema autónomo | RIP (v1 y v2), OSPF, EIGRP |
| Externo | Entre sistemas autónomos distintos | BGP |

Y la métrica de un enrutador sirve para calcular el mejor trayecto hacia un destino: no mide longitud
física, sino, según el protocolo, saltos, coste, ancho de banda o retardo (oficio).

### El origen

| Año | Hecho | Fuente |
|---|---|---|
| 1962 | J. C. R. Licklider, del MIT, describe su «Galactic Network»: **«a globally interconnected set of computers through which everyone could quickly access data and programs from any site»** | ISOC |
| 1969 | El primer conmutador de paquetes de ARPANET (un IMP) se instala en la Universidad de California en Los Ángeles: **«September 1969 when BBN installed the first IMP at UCLA and the first host computer was connected»**; a final de año hay cuatro nodos. Ese mismo año S. Crocker crea la serie de RFC | ISOC |
| 1970-1972 | Primer protocolo de ARPANET, el NCP (**«Network Control Protocol»**); en 1972, primera demostración pública y el correo electrónico, **«the initial "hot" application»** | ISOC |
| 1972-1974 | Kahn plantea la arquitectura abierta; con Vinton Cerf diseña TCP; la primera versión escrita circula en septiembre de 1973 y la refinada se publica en 1974 | ISOC |
| 1983 | ARPANET pasa de NCP a TCP/IP **«as of January 1, 1983»**, un cambio de golpe (*flag day*) para todos los equipos | ISOC |
| 1985 | La red académica estadounidense NSFNET hace obligatorio TCP/IP | ISOC |
| 1990 | Se da de baja ARPANET; nace la web: **«HTTP has been the primary information transfer protocol for the World Wide Web since its introduction in 1990.»** | ISOC; RFC 9110 |
| 1995 | **«NSF's privatization policy culminated in April, 1995, with the defunding of the NSFNET Backbone»**: el dinero pasa a las redes regionales para que compren conectividad a redes privadas de larga distancia. En octubre, definición del FNC | ISOC |

La web nació en el CERN, cuyo servidor conserva **«home of the first website»** (la casa del primer
sitio web). La página del proyecto que conserva ese servidor lo presentaba así: **«The WorldWideWeb (W3) is a wide-area hypermedia
information retrieval initiative aiming to give universal access to a large universe of
documents.»** (una iniciativa de recuperación de información hipermedia de área amplia para dar
acceso universal a un gran universo de documentos).

Un detalle del diseño original que explica el direccionamiento de hoy: en el TCP de Cerf y Kahn
**«a 32 bit IP address was used of which the first 8 bits signified the network and the remaining 24
bits designated the host on that network»**; se suponía que 256 redes bastarían, y la llegada de las
redes de área local a finales de los setenta obligó a revisarlo (de ahí las clases del epígrafe 4).

### La evolución y el estado actual

- *Agotamiento de IPv4.* El 3 de febrero de 2011 la ICANN anunció que **«the pool of first
  generation Internet addresses has now been completely emptied»**: la IANA entregó los cinco últimos
  bloques a los cinco registros regionales. El RIPE NCC agotó los suyos el 25 de noviembre de 2019
  (**«The RIPE NCC has run out of IPv4 Addresses»**) y anunció que en adelante sólo repartiría
  direcciones recuperadas, por lista de espera. El mismo comunicado constata **«the emergence of an IPv4 transfer
  market and greater use of Carrier Grade Network Address Translation (CGNAT)»**, y que ninguna de las
  dos cosas resuelve el problema: **«there are not enough IPv4 addresses for everyone»**.
- *IPv6* es la salida. La ICANN lo resumía en 2011: IPv6 abre un espacio **«a billion-trillion times
  larger than the total pool of IPv4 addresses (about 4.3 billion)»**.
- *La web cambia de transporte.* HTTP/1.1 (1995-1997), HTTP/2 y HTTP/3; este último usa **«QUIC as a
  secure multiplexed transport over UDP instead of TCP»** (RFC 9110). Las tres versiones conviven:
  **«They have not obsoleted each other»**.
- *El cifrado es la norma.* TLS 1.3 se especificó en el RFC 8446 (2018) y desde julio de 2026 en el
  RFC 9846, que lo sustituye sin cambiar de versión; TLS 1.0, 1.1 y SSL 3.0 están prohibidos
  (epígrafe 2).
- *Uso.* Según la Unión Internacional de Telecomunicaciones (UIT), **«an estimated 6 billion people
  – about three-quarters of the world's population – are using the Internet in 2025»**, y **«2.2
  billion people remain offline»**.

### Los principales servicios

| Servicio | Protocolo | Puerto |
|---|---|---|
| Web | HTTP / HTTPS | 80 / 443 |
| Nombres de dominio | DNS | 53 |
| Correo saliente | SMTP | 25, y 587 para el envío del cliente |
| Correo entrante | IMAP / POP3 | 143 / 110, y 993 / 995 cifrados |
| Transferencia de ficheros | FTP, hoy desaconsejado, y SFTP | 21 y 22 |
| Terminal remota | SSH, y el desaconsejado Telnet | 22 y 23 |

El patrón que ordena toda la columna de la derecha: casi todos los servicios tienen un puerto en
claro y otro cifrado, y la versión cifrada es la que hay que usar. FTP y Telnet mandan la contraseña
en claro por la red, y por eso están desaconsejados: sus sustitutos son SFTP y SSH, que van los dos
por el puerto 22. Los puertos de HTTP y HTTPS los fija el RFC 9110: **«TCP port 80 (the reserved port
for WWW services)»** y **«TCP port 443 (the reserved port for HTTP over TLS)»**. Otros dos puertos de
la casa, según la tabla de puertos de Windows Server de Microsoft: LDAP, el protocolo del directorio
(tema 8), usa el 389, y el 636 cifrado (**«LDAP SSL»**); SNMP, el de gestión de red, el 161 (UDP), y el
162 para las capturas (*traps*).

Tres servicios de soporte que el operador ve a diario:

- *DNS.* Traduce nombres en direcciones; su objetivo, en el RFC 1034, es **«a consistent name space
  which will be used for referring to resources»** (un espacio de nombres coherente). Los tipos de
  registro que conviene tener vistos:

  | Tipo | Qué resuelve |
  |---|---|
  | A | Un nombre a una dirección IPv4 |
  | AAAA | Un nombre a una dirección IPv6 |
  | CNAME | Un nombre a otro nombre |
  | MX | A qué servidor va el correo del dominio |
  | NS | Qué servidores son autoritativos del dominio |
  | TXT | Texto libre: verificaciones y políticas de correo |

  El tiempo de vida se expresa en segundos, y es cuánto puede un servidor intermedio guardar la
  respuesta antes de volver a preguntar. Pasado ese plazo, la caché caduca y se consulta de nuevo, de
  modo que el peor caso es exactamente el tiempo de vida.
- *DHCP.* **«The Dynamic Host Configuration Protocol (DHCP) provides a framework for passing
  configuration information to hosts on a TCPIP network.»** Da al equipo su dirección, máscara,
  puerta de enlace y servidores DNS sin tocarlo (oficio).
- *NAT.* La traducción de direcciones que hace el router de casa o de la oficina: la NAPT traduce
  **«many network addresses and their TCP/UDP (Transmission Control Protocol/User Datagram Protocol)
  ports»** a **«a single network address and its TCP/UDP ports»**, y así toda una red con direcciones
  privadas sale con una sola pública (RFC 3022).

Una dirección completa de un recurso (URL) tiene esquema (`https`), anfitrión (`www.canalsur.es`),
ruta y, opcionalmente, puerto, parámetros y fragmento. Una cookie es estado que el servidor deja en el
navegador: el RFC 6265 permite a los servidores **«store state (called cookies) at HTTP user agents,
letting the servers maintain a stateful session over the mostly stateless HTTP protocol»**.

## 2. Los protocolos HTTP, HTTPS y TLS

### HTTP: petición y respuesta, sin estado

El protocolo de transferencia de hipertexto (HTTP) es el de la web. Funciona por petición y
respuesta: **«A client sends requests to a server in the form of a "request" message with a method
(Section 9) and request target (Section 7.1).»** El servidor contesta con un mensaje de respuesta que
lleva un código de estado.

Es un protocolo sin estado: **«HTTP is defined as a stateless protocol, meaning that each request
message's semantics can be understood in isolation»** (cada petición se entiende por sí sola). Por
eso, para recordar quién es el usuario entre una página y otra, hacen falta las cookies del epígrafe
anterior.

Los métodos que define el RFC 9110 (tabla 4 de la sección 9.1; cada uno se desarrolla en la 9.3), con
su función traducida:

| Método | Qué pide | ¿Seguro? | ¿Idempotente? |
|---|---|---|---|
| GET | Transferir una representación actual del recurso | Sí | Sí |
| HEAD | Lo mismo que GET, pero sin el contenido de la respuesta | Sí | Sí |
| POST | Que el recurso procese el contenido enviado | No | No |
| PUT | Sustituir todas las representaciones del recurso por el contenido enviado | No | Sí |
| DELETE | Eliminar todas las representaciones del recurso | No | Sí |
| CONNECT | Abrir un túnel hasta el servidor del recurso | No | No |
| OPTIONS | Describir las opciones de comunicación del recurso | Sí | Sí |
| TRACE | Hacer una prueba de bucle del mensaje a lo largo del camino | Sí | Sí |

Las dos columnas de la derecha salen de dos frases de la norma: **«Of the request methods defined by
this specification, the GET, HEAD, OPTIONS, and TRACE methods are defined to be safe.»** (seguro: no
pretende cambiar nada en el servidor) y **«Of the request methods defined by this specification, PUT,
DELETE, and safe request methods are idempotent.»** (idempotente: repetir la petición deja el
servidor igual que hacerla una vez). POST no es ni lo uno ni lo otro: enviar dos veces un formulario
puede crear dos pedidos.

Los códigos de estado tienen tres cifras y **«The first digit of the status code defines the class
of response.»**

| Clase | Significado (RFC 9110, sección 15) | Ejemplos |
|---|---|---|
| 1xx | **«Informational»**: **«The request was received, continuing process»** | 100 Continue, 101 Switching Protocols |
| 2xx | **«Successful»**: **«The request was successfully received, understood, and accepted»** | 200 OK, 201 Created, 204 No Content |
| 3xx | **«Redirection»**: **«Further action needs to be taken in order to complete the request»** | 301 Moved Permanently, 302 Found, 304 Not Modified |
| 4xx | **«Client Error»**: **«The request contains bad syntax or cannot be fulfilled»** | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| 5xx | **«Server Error»**: **«The server failed to fulfill an apparently valid request»** | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

Tres que confunden en el test: el 401 dice que a la petición le faltan credenciales (**«it lacks
valid authentication credentials for the target resource»**); el 403, que **«the server understood
the request but refuses to fulfill it»** (entendida, pero denegada aunque se esté autenticado); y el
404, que **«the origin server did not find a current representation for the target resource or is
not willing to disclose that one exists»**. El 503 es una sobrecarga o un mantenimiento
**«which will likely be alleviated after some delay»** (que probablemente se resolverá con el tiempo).
Y una regla útil: un cliente que recibe un código que no conoce lo trata como el x00 de su clase (un
471, como un 400).

Las versiones, según el RFC 9110 (sección 1.2):

| Versión | Qué trae |
|---|---|
| HTTP/0.9 y HTTP/1.0 | Al principio, **«a single method (GET)»**; después, peticiones y respuestas dentro de mensajes, tipos de contenido e intermediarios |
| HTTP/1.1 | **«introduced in 1995 and published on the Standards Track in 1997»**; entre otras cosas, **«default persistent connections»** (conexiones que se reutilizan) |
| HTTP/2 | **«a multiplexed session layer on top of the existing TLS and TCP protocols»**: varias peticiones a la vez por una conexión |
| HTTP/3 | **«QUIC as a secure multiplexed transport over UDP instead of TCP»** |

QUIC, por su parte, ofrece **«flow-controlled streams for structured communication, low-latency
connection establishment, and network path migration»** (RFC 9000): flujos con control, conexión
rápida y la posibilidad de cambiar de red (de Wi-Fi a móvil) sin cortar.

### HTTPS: HTTP sobre TLS

HTTPS no es un protocolo distinto de HTTP: es el mismo HTTP hablado dentro de un túnel cifrado. La
norma define el esquema `https` para un servidor **«capable of establishing a TLS ([TLS13]) connection
that has been secured for HTTP communication»**, y aclara qué significa *secured*: **«the server has
been authenticated as acting on behalf of the identified authority and all HTTP communication with
that server has confidentiality and integrity protection that is acceptable to both client and
server»**. El puerto, si la dirección no dice otro, es el 443.

Lo que ese túnel aporta son tres cosas, y conviene no confundirlas:

| Qué aporta | Qué significa |
|---|---|
| Confidencialidad | Nadie por el camino puede leer lo que pasa |
| Integridad | Nadie por el camino puede modificarlo sin que se note |
| Autenticación del servidor | El cliente comprueba, con el certificado, que habla con quien cree |

Lo que NO aporta, y es la confusión más extendida: HTTPS no dice que el sitio sea de fiar. Dice que
la conexión con ese sitio es privada. Un sitio fraudulento puede tener un certificado válido, y
millones lo tienen.

Cómo funciona el certificado, en tres líneas: el servidor presenta un certificado firmado por una
autoridad de certificación; el navegador comprueba que esa autoridad está en su lista de confianza y
que el nombre del certificado coincide con el del sitio; si las dos cosas cuadran, negocian una clave
de sesión y a partir de ahí todo va cifrado. (Los certificados y las autoridades de certificación se
estudian en el tema 14.)

Un sitio puede además obligar al navegador a usar siempre HTTPS con la política HSTS (*HTTP Strict
Transport Security*), que **«is declared by web sites via the Strict-Transport-Security HTTP response
header field»** (o por otros medios, como la configuración del navegador; RFC 6797): una vez recibida,
el navegador trata el sitio como de HTTPS obligatorio durante los segundos que fija la directiva
`max-age` de la cabecera.

### TLS: qué es y qué garantiza

La seguridad de la capa de transporte (TLS) es el protocolo que cifra HTTPS, el correo seguro y
muchos otros servicios. La versión vigente es TLS 1.3, especificada desde julio de 2026 en el RFC
9846, que **«obsoletes RFC 8446, which specified TLS 1.3»** y es **«a minor update to TLS 1.3 that
retains the same version number and is backward compatible»**. Su objeto: **«TLS allows
client/server applications to communicate over the Internet in a way that is designed to prevent
eavesdropping, tampering, and message forgery.»** (escuchas, manipulación y falsificación de
mensajes).

El canal seguro tiene tres propiedades:

- **«Authentication: The server side of the channel is always authenticated; the client side is
  optionally authenticated.»** El servidor siempre se identifica; el cliente, sólo si se pide (por
  ejemplo, con un certificado de cliente).
- **«Confidentiality: Data sent over the channel after establishment is only visible to the
  endpoints.»** Con un matiz: **«TLS does not hide the length of the data it transmits»**.
- **«Integrity: Data sent over the channel after establishment cannot be modified by attackers
  without detection.»**

Y dos componentes: el protocolo de negociación (*handshake*), **«that authenticates the communicating
parties, negotiates cryptographic algorithms and parameters, and establishes shared keying
material»**, y el protocolo de registro, que **«uses the parameters established by the handshake
protocol to protect traffic between the communicating peers»**. TLS **«is application protocol
independent»**: cualquier protocolo puede ir encima.

### Las versiones: de SSL a TLS 1.3

| Versión | Documento y fecha | Situación |
|---|---|---|
| SSL 3.0 (Netscape) | Versión del 18 de noviembre de 1996, publicada como registro histórico en el RFC 6101 (2011) | Prohibida: **«This document requires that SSLv3 not be used.»** (RFC 7568) |
| TLS 1.0 | RFC 2246, enero de 1999 | Retirada por el RFC 8996 (2021) |
| TLS 1.1 | RFC 4346, abril de 2006 | Retirada por el RFC 8996 (2021) |
| TLS 1.2 | RFC 5246, agosto de 2008 | Sustituida por TLS 1.3; el RFC 9846 todavía le fija requisitos: **«This document also specifies new requirements for TLS 1.2 implementations.»** |
| TLS 1.3 | RFC 8446 (agosto de 2018), sustituido por el RFC 9846 (julio de 2026) | Vigente |

El RFC 8996 **«formally deprecates Transport Layer Security (TLS) versions 1.0 (RFC 2246) and 1.1
(RFC 4346)»** porque **«These versions lack support for current and recommended cryptographic
algorithms and mechanisms»**, y el RFC 9846 ya prohíbe negociarlas: **«Forbid negotiating TLS 1.0 and
1.1 as they are now deprecated by [RFC8996].»** SSL 3.0 fue **«the basis for Transport Layer Security
(TLS)»** pero **«was never formally published by the IETF»** (salvo en borradores de Internet caducados).

El aviso de nomenclatura, porque el sector arrastra el nombre viejo: cuando alguien dice
«certificado SSL» quiere decir certificado para TLS. SSL, como protocolo, no debe usarse.

Qué cambió de TLS 1.2 a TLS 1.3 (RFC 9846, sección 1.3):

- Fuera los algoritmos antiguos: la lista de cifrados simétricos **«has been pruned of all algorithms
  that are considered legacy»**, y los que quedan son todos de cifrado autenticado (AEAD).
- **«Static RSA and Diffie-Hellman cipher suites have been removed; all public-key based key exchange
  mechanisms now provide forward secrecy.»** Secreto hacia delante: si mañana se roba la clave
  privada del servidor, no sirve para descifrar las sesiones grabadas hoy.
- **«All handshake messages after the ServerHello are now encrypted.»**
- Se añade el modo de ida y vuelta cero (0-RTT), que ahorra un viaje al conectar **«at the cost of
  certain security properties»**.

## 3. Configuración, privacidad y seguridad de los navegadores web

Se toman como referencia Microsoft Edge y Google Chrome. Las rutas de menú son las de su ayuda oficial en castellano a
05-10-2026; cambian con las versiones.

### Configuración básica

Funcionalidades básicas que comparten todos:

- Barra de direcciones, que en los navegadores actuales es también caja de búsqueda.
- Pestañas, para varias páginas en una ventana.
- Historial, con las páginas visitadas.
- Favoritos o marcadores: enlaces guardados por el usuario, organizables en carpetas. Un favorito no
  guarda la página, guarda su dirección: si la página desaparece, el favorito deja de funcionar.
- Descargas, con su gestor.

Dónde está la configuración que interesa a este epígrafe:

| Navegador | Ruta |
|---|---|
| Chrome | **«Más Configuración»**, y a la izquierda **«Privacidad y seguridad»** (dentro, **«Seguridad»** y **«Cookies de terceros»**) |
| Edge | **«Configuración y más>>privacidad, búsqueda y servicios»** (dentro, **«Prevención de seguimiento»** y **«Seguridad»**) |

La actualización es la primera medida de seguridad: **«Para asegurar que cuentas con las últimas
actualizaciones de seguridad, Chrome puede actualizarse automáticamente si hay una nueva versión del
navegador disponible.»** En un equipo de empresa, varias opciones las fija el administrador y el
usuario no las puede cambiar: lo dicen tanto Microsoft de SmartScreen (**«en una red de escuela o
trabajo, es posible que esta opción sea controlada por un administrador del sistema y no se pueda
cambiar»**) como Google del DNS seguro (**«Si tu dispositivo está administrado o los controles
parentales están activados, no podrás usar la función DNS seguro de Chrome.»**). Esas opciones se
reparten con directivas de grupo (temas 6 y 8; oficio).

### Privacidad: navegación privada, cookies y rastreadores

La navegación privada (en Chrome, el modo Incógnito) no conserva en el equipo, al terminar, el
historial ni las cookies y demás datos de sitios. No hace anónimo al usuario: el proveedor de acceso y el sitio visitado
siguen viendo la conexión. Es la confusión más frecuente sobre esta función. La ayuda de Chrome lo
precisa:

- **«Chrome no inicia sesión automáticamente en tu cuenta de Google ni en otros sitios web»**.
- **«Cuando finaliza tu sesión de Incógnito, Chrome no conserva datos de sitios ni un registro de los
  sitios que has visitado»**; mientras dura, guarda cookies temporales que se borran al terminar la sesión.
- Pero **«Chrome conserva los marcadores que guardas y los archivos que descargas cuando sales del
  modo Incógnito»**.
- Y **«no te hace invisible. Los sitios web que visites, incluidos los sitios de Google, y las
  organizaciones que gestionen tu red, como tu centro educativo, tu empresa o tu proveedor de
  Internet, pueden observar tu actividad en el modo Incógnito.»**
- La sesión termina sólo al cerrar todas las ventanas: **«Para finalizar tu sesión de Incógnito, debes
  cerrar todas las ventanas de Incógnito.»** Atajo en Windows: **«Ctrl + Mayús + N»**.

Las cookies son de dos clases: **«Cookies propias: las crea el sitio al que accedes y que se muestra
en la barra de direcciones.»** y **«Cookies de terceros: las crean otros sitios.»**, que pueden usarse
**«para saber qué acciones realizas en otros sitios»**. En Chrome se pueden permitir o bloquear las de
terceros, con excepciones por sitio (para un dominio entero se escribe `[*.]` delante), y
**«De forma predeterminada, las cookies de terceros están bloqueadas en el modo Incógnito.»**

Edge tiene la prevención de seguimiento, con tres niveles:

| Nivel | Qué hace (ayuda de Microsoft) |
|---|---|
| Básico | **«bloquea rastreadores potencialmente dañinos, pero permite la mayoría de los demás rastreadores y los que personalizan contenido y anuncios»** |
| Equilibrado (recomendado) | **«bloquea rastreadores potencialmente dañinos y rastreadores de sitios que no ha visitado»** |
| Estricto | **«bloquea los rastreadores potencialmente dañinos y la mayoría de los rastreadores de todos los sitios»**; puede romper sitios (**«un vídeo podría no reproducirse o es posible que no puedas iniciar sesión»**) |

Se pueden crear excepciones por sitio; una excepción **«permitirá todos los rastreadores en estos
sitios, incluidos los que son potencialmente dañinos»**.

El DNS seguro cifra la consulta del nombre: **«Si la petición del sistema de nombres de dominio (DNS)
seguro está activada, Chrome cifra tu información durante el proceso de búsqueda para proteger tu
privacidad y seguridad.»** Viene activado en modo automático, y si falla **«buscará el sitio web en el
modo sin cifrar»**. La técnica normalizada es DNS sobre HTTPS (DoH), que el RFC 8484 define como **«a
protocol for sending DNS queries and getting DNS responses over HTTPS»**.

### Seguridad: listas de sitios peligrosos y conexiones seguras

| Función | Navegador | Qué hace |
|---|---|---|
| Navegación segura | Chrome | **«recibes advertencias que te protegen contra malware, extensiones y sitios engañosos, phishing, anuncios maliciosos e invasivos, y ataques de ingeniería social»**. Tres niveles: protección mejorada, protección estándar (**«opción predeterminada»**) y sin protección (**«no recomendado»**) |
| SmartScreen de Microsoft Defender | Edge | **«ayuda a proteger su seguridad frente a sitios y software de suplantación de identidad y malware, y le ayuda a tomar decisiones informadas sobre las descargas»**; avisa también si una descarga no está en la lista de las conocidas y populares |
| Usar siempre conexiones seguras | Chrome | **«Chrome mejorará las URLs para que utilicen HTTPS y mostrará una advertencia antes de visitar un sitio que no sea compatible con ese protocolo»** |
| Comprobación de seguridad | Chrome | Detecta, entre otras cosas, **«Contraseñas vulneradas, reutilizadas o poco seguras»** y actualizaciones pendientes |

Dos matices de la protección mejorada de Chrome: protege incluso de sitios **«que Google desconocía
antes»**, y para ello **«Chrome envía la URL del sitio y una pequeña muestra del contenido de la
página, la actividad de la extensión e información del sistema a Navegación segura de Google»**. Y
un aviso: **«Aunque recibas una advertencia de Chrome, podrás visitar el sitio no seguro o descargar
el archivo.»** La advertencia no es un bloqueo.

En la barra de direcciones, cuando un sitio no usa HTTPS, **«se mostrará la advertencia "No es
seguro"»**. Y el candado indica que la comunicación con el sitio va cifrada y que el certificado del
sitio es válido. No garantiza que el sitio sea honrado: un sitio fraudulento puede tener certificado.
El candado dice cómo viaja la información, no a quién llega.

SmartScreen tampoco es el bloqueador de ventanas emergentes: **«SmartScreen comprueba que los sitios
que visitas y los archivos que descargas no supongan una amenaza para tu seguridad. Por lo general, el
bloqueador de elementos emergentes solo bloquea la mayor parte de los elementos emergentes»**.

## 4. Los protocolos IPv4 e IPv6

### La cabecera IPv4

El protocolo de internet versión 4 (IPv4) lo especifica el RFC 791, de septiembre de 1981. Su
cabecera tiene estos campos, en este orden (figura 4 del RFC, filas de 32 bits):

| Campo | Bits | Para qué sirve |
|---|---|---|
| Version | 4 | **«The Version field indicates the format of the internet header.»** Vale 4 |
| IHL (*Internet Header Length*) | 4 | Longitud de la cabecera **«in 32 bit words»**; **«the minimum value for a correct header is 5»** |
| Type of Service | 8 | Calidad de servicio pedida; hoy redefinido (véase abajo) |
| Total Length | 16 | **«the length of the datagram, measured in octets, including internet header and data»**; permite **«up to 65,535 octets»** |
| Identification | 16 | **«An identifying value assigned by the sender to aid in assembling the fragments of a datagram.»** |
| Flags | 3 | Bit 0 reservado; DF (**«Don't Fragment»**) y MF (**«More Fragments»**) |
| Fragment Offset | 13 | Dónde va el fragmento; se mide **«in units of 8 octets (64 bits)»** |
| Time to Live (TTL) | 8 | **«If this field contains the value zero, then the datagram must be destroyed.»** Cada equipo que procesa el datagrama lo baja al menos en uno |
| Protocol | 8 | **«the next level protocol used in the data portion of the internet datagram»** |
| Header Checksum | 16 | **«A checksum on the header only.»** Se recalcula en cada salto, porque el TTL cambia |
| Source Address / Destination Address | 32 cada una | Direcciones de origen y destino |
| Options y Padding | variable | Opcionales; el relleno completa la fila de 32 bits |

Las cuentas que el test pregunta: con IHL mínimo de 5 palabras de 32 bits, la cabecera mínima es de
5 × 4 = 20 octetos, y con el máximo del campo (15) es de 60. El propio RFC lo dice: **«The maximal
internet header is 60 octets, and a typical internet header is 20 octets»**.

El campo *Type of Service* ya no se usa como lo describe el RFC 791: el RFC 2474 define el campo de
servicios diferenciados (DS), y **«In IPv4, it defines the layout of the TOS octet; in IPv6, the
Traffic Class octet»**; el RFC 3168 añade la notificación explícita de congestión (ECN), que usa
**«two bits in the IP header»**. El índice de RFC registra el RFC 791 como actualizado, entre otros,
por el 2474.

### La cabecera IPv6

El protocolo de internet versión 6 (IPv6) lo especifica el RFC 8200 (julio de 2017), norma de
Internet número 86. Su cabecera es más sencilla y de longitud fija:

| Campo | Bits | Para qué sirve |
|---|---|---|
| Version | 4 | **«4-bit Internet Protocol version number = 6.»** |
| Traffic Class | 8 | **«8-bit Traffic Class field.»** El equivalente del antiguo Type of Service (campo DS) |
| Flow Label | 20 | **«20-bit flow label.»** Marca los paquetes de un mismo flujo |
| Payload Length | 16 | **«Length of the IPv6 payload, i.e., the rest of the packet following this IPv6 header, in octets.»** Las cabeceras de extensión cuentan como carga |
| Next Header | 8 | **«Identifies the type of header immediately following the IPv6 header. Uses the same values as the IPv4 Protocol field»** |
| Hop Limit | 8 | **«Decremented by 1 by each node that forwards the packet.»** Es el TTL de IPv6 |
| Source Address | 128 | **«128-bit address of the originator of the packet.»** |
| Destination Address | 128 | **«128-bit address of the intended recipient of the packet»** |

La cabecera mide 4 + 4 + 16 + 16 = 40 octetos (cálculo sobre la figura, que cuadra con el RFC: la
cabecera IPv6 mínima es **«20 octets longer than a minimum-length IPv4 header»**, de 20). Lo que IPv6 quita respecto de IPv4: el campo de longitud de cabecera (IHL), la
suma de comprobación de la cabecera y los campos de fragmentación, que pasan a una cabecera de
extensión.

Las cabeceras de extensión: **«In IPv6, optional internet-layer information is encoded in separate
headers»**, que se colocan entre la cabecera IPv6 y la de la capa superior. Se
encadenan con el campo Next Header, y el orden recomendado es: cabecera IPv6, opciones salto a salto,
opciones de destino, encaminamiento, fragmento, autenticación (AH), carga de seguridad encapsulada
(ESP), opciones de destino y cabecera de la capa superior. La de fragmento **«is identified by a Next
Header value of 44»**.

Dos diferencias de funcionamiento que se preguntan:

- Fragmentación: **«unlike IPv4, fragmentation in IPv6 is performed only by source nodes, not by
  routers along a packet's delivery path»**. El enrutador IPv6 no fragmenta.
- Tamaño mínimo de enlace: **«IPv6 requires that every link in the Internet have an MTU of 1280
  octets or greater.»** Y se recomienda que el origen descubra la MTU del camino: **«It is strongly
  recommended that IPv6 nodes implement Path MTU Discovery»**.

| | IPv4 | IPv6 |
|---|---|---|
| Longitud de dirección | 32 bits | 128 bits |
| Cabecera | 20 a 60 octetos, variable (IHL) | 40 octetos, fija, más extensiones |
| Suma de comprobación de cabecera | Sí, recalculada en cada salto | No |
| Fragmentación | Origen y enrutadores | Sólo el origen (cabecera de fragmento) |
| Tiempo de vida | TTL | Hop Limit |
| Protocolo siguiente | Protocol | Next Header (mismos valores) |
| Difusión (*broadcast*) | Sí | No: la sustituye la multidifusión |

### El direccionamiento IPv4

Una dirección IPv4 tiene 32 bits y se escribe como cuatro números decimales de 0 a 255 separados por
puntos. Cada dirección tiene una parte de red y una de equipo. En el RFC 791 eso se hacía por
clases: **«in class a, the high order bit is zero, the next 7 bits are the network, and the last 24
bits are the local address; in class b, the high order two bits are one-zero, the next 14 bits are
the network and the last 16 bits are the local address; in class c, the high order three bits are
one-one-zero, the next 21 bits are the network and the last 8 bits are the local address.»** Después
se añadieron dos: **«There are now five classes of IP addresses: Class A through Class E. Class D
addresses are used for IP multicasting [IP:4], while Class E addresses are reserved for experimental
use.»** (RFC 1122). Los rangos de cada clase se deducen de esos bits iniciales:

| Clase | Bits iniciales | Primer octeto | Red / equipo | Uso |
|---|---|---|---|---|
| A | 0 | 0 a 127 (0 y 127 reservados: véase la tabla de bloques especiales) | 8 / 24 | Pocas redes muy grandes |
| B | 10 | 128 a 191 | 16 / 16 | Redes medianas |
| C | 110 | 192 a 223 | 24 / 8 | Muchas redes pequeñas |
| D | 1110 | 224 a 239 | — | Multidifusión: **«host group addresses range from 224.0.0.0 to 239.255.255.255»** (RFC 1112) |
| E | 1111 | 240 a 255 | — | Reservada (experimental) |

Las clases ya no gobiernan el reparto (subepígrafe siguiente), pero se siguen preguntando y explican
los rangos privados. El RFC 1918 reserva tres bloques para redes privadas, que no se encaminan en
Internet:

| Bloque | Prefijo | Equivalencia por clases |
|---|---|---|
| 10.0.0.0 a 10.255.255.255 | 10/8 | Una red de clase A |
| 172.16.0.0 a 172.31.255.255 | 172.16/12 | 16 redes de clase B contiguas |
| 192.168.0.0 a 192.168.255.255 | 192.168/16 | 256 redes de clase C contiguas |

**«An enterprise that decides to use IP addresses out of the address space defined in this document
can do so without any coordination with IANA or an Internet registry.»** Por eso las usan todas las
redes internas, y por eso para salir a Internet hace falta NAT. El aviso que hace útil el ejercicio:
192.168 y 192.0.2 son de clase C y no son públicas. Pertenecer a una clase y ser pública son dos cosas
distintas.

Otros bloques de uso especial (registro del RFC 6890 y RFC 6598):

| Bloque | Nombre en el registro | Qué es |
|---|---|---|
| 0.0.0.0/8 | **«"This host on this network"»** | Sólo como origen, al arrancar |
| 127.0.0.0/8 | **«Loopback»** | Bucle local; la habitual es 127.0.0.1 |
| 169.254.0.0/16 | **«Link Local»** | Dirección que el equipo se pone solo si no encuentra servidor DHCP |
| 100.64.0.0/10 | **«Shared Address Space»** | Para la NAT de operador (CGN): **«Shared Address Space is distinct from RFC 1918 private address space because it is intended for use on Service Provider networks.»** |
| 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 | **«Documentation (TEST-NET-1)»**, TEST-NET-2 y TEST-NET-3 | Para ejemplos en documentos |
| 240.0.0.0/4 | **«Reserved»** | La antigua clase E |
| 255.255.255.255/32 | **«Limited Broadcast»** | Difusión a la red física propia |

El 169.254 lo regula el RFC 3927: cuando falta configuración (**«such address configuration information
may not always be available»**), el equipo puede ponerse solo **«an IPv4 address within the 169.254/16
prefix that is valid for communication with other devices connected to the same physical (or
logical) link»**. Ver una 169.254 en `ipconfig` suele querer decir que el servidor DHCP no ha
contestado (oficio).

Dentro de cada red hay dos direcciones que no se dan a ningún equipo. El RFC 1122 usa «-1» para un
campo de todo unos: **«{ <Network-number>, -1 }»** es la **«Directed broadcast to the specified
network»** (difusión dirigida, la última de la red); la dirección con el campo de equipo a ceros es, por
convención de oficio, la que identifica a la red.
La difusión limitada, **«{ -1, -1 }»**, **«will be received by every host on the connected physical
network but will not be forwarded outside that network»**.

### Las subredes y la notación CIDR

La máscara indica qué bits son de red. El RFC 950 la introdujo para partir una red en subredes, con
**«a bit mask ("address mask")»**, y el encaminamiento entre dominios sin clases (CIDR, RFC 4632) la
generalizó: **«In CIDR notation, a prefix is shown as a 4-octet quantity, just like a traditional IPv4
address or network number, followed by the "/" (slash) character, followed by a decimal value between
0 and 32 that describes the number of significant bits.»** El ejemplo del propio RFC: **«the legacy
"Class B" network 172.16.0.0, with an implied network mask of 255.255.0.0, is defined as the prefix
172.16.0.0/16»**. Con CIDR, los bloques pueden ser de **«any power of two-sized block of between one
and 2^32 end system addresses»**.

Tabla de cálculo (direcciones = 2 elevado a los bits de equipo; utilizables = esa cifra menos la de
red y la de difusión):

| Prefijo | Máscara | Direcciones | Utilizables |
|---|---|---|---|
| /8 | 255.0.0.0 | 16.777.216 | 16.777.214 |
| /16 | 255.255.0.0 | 65.536 | 65.534 |
| /20 | 255.255.240.0 | 4.096 | 4.094 |
| /22 | 255.255.252.0 | 1.024 | 1.022 |
| /23 | 255.255.254.0 | 512 | 510 |
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |

Método para saber si dos equipos comparten subred (ejemplo: 192.168.30.150 con máscara
255.255.255.128):

1. La máscara 255.255.255.128 tiene veinticinco unos: los tres primeros octetos completos son
   veinticuatro, y el 128 del cuarto aporta uno más. De ahí la notación `/25`.
2. Con `/25`, el cuarto octeto se parte por la mitad: una subred va de 0 a 127 y la otra de 128 a
   255.
3. El 150 del equipo dado es mayor que 127, luego está en la subred alta: de 192.168.30.128 a
   192.168.30.255.
4. Comparten subred con él los equipos de ese tramo con los mismos tres primeros octetos: el
   192.168.30.250/25 sí; el 192.168.30.124/25 no (subred baja); el 192.168.31.150/25 tampoco (otra
   red). La 192.168.30.128 es la dirección de la subred y la 192.168.30.255 su difusión: ninguna se
   asigna.

Y al revés, la máscara para un número de equipos (ejemplo: 500). La cuenta: con *b* bits de equipo
hay 2^b direcciones, menos dos —la de red y la de difusión— que no se asignan. Se busca la potencia
de dos inmediatamente superior a 500, que es 512, y 512 son nueve bits. Treinta y dos menos nueve son
veintitrés, luego la máscara es `/23`, y `/23` en decimal es 255.255.254.0: veintitrés unos son los
dos primeros octetos completos más siete del tercero, y siete unos seguidos de un cero son 254.

| Máscara | Prefijo | Direcciones asignables | Veredicto |
|---|---|---|---|
| 255.255.254.0 | /23 | 510 | La ajustada |
| 255.255.248.0 | /21 | 2.046 | Cuatro veces más de lo necesario |
| 255.255.255.0 | /24 | 254 | No caben los 500 |
| 255.255.255.128 | /25 | 126 | Mucho menos aún |

Y el detalle que a veces despista: 510 es menor que 512 por los dos que no se asignan, y aun así
basta para 500 equipos. Si la red hubiera pedido 511, habría que subir a `/22`.

Partir una red en subredes iguales: cada bit que se toma prestado de la parte de equipo duplica el
número de subredes y divide por dos su tamaño. Ejemplo (cálculo): 192.168.10.0/24 en cuatro subredes
toma dos bits y da /26, de 64 direcciones cada una: .0 a .63, .64 a .127, .128 a .191 y .192 a .255;
la primera utilizable de la segunda es la .65 y su difusión la .127.

### El direccionamiento IPv6

**«IPv6 addresses are 128-bit identifiers for interfaces and sets of interfaces»** (RFC 4291). Hay tres
tipos:

- *Unicast*: **«An identifier for a single interface.»**
- *Anycast*: un conjunto de interfaces; el paquete llega a una sola, **«the "nearest" one, according to
  the routing protocols' measure of distance»** (la más cercana según el encaminamiento).
- *Multicast*: un conjunto de interfaces; el paquete llega a todas.

Y una ausencia que se pregunta: **«There are no broadcast addresses in IPv6, their function being
superseded by multicast addresses.»**

Cómo se escriben. **«The preferred form is x:x:x:x:x:x:x:x, where the 'x's are one to four
hexadecimal digits of the eight 16-bit pieces of the address.»** Dos abreviaturas: no hace falta
escribir los ceros a la izquierda de cada grupo, y **«The use of "::" indicates one or more groups of
16 bits of zeros. The "::" can only appear once in an address.»** El RFC 4291 pone estos ejemplos:

| Forma completa | Abreviada |
|---|---|
| 2001:DB8:0:0:8:800:200C:417A | 2001:DB8::8:800:200C:417A |
| FF01:0:0:0:0:0:0:101 | FF01::101 |
| 0:0:0:0:0:0:0:1 | ::1 (bucle local) |
| 0:0:0:0:0:0:0:0 | :: (sin especificar) |
| 0:0:0:0:0:FFFF:129.144.52.38 | ::FFFF:129.144.52.38 (forma mixta con IPv4) |

El RFC 5952 fija además cómo debe escribirse para que todos lo hagan igual: **«The use of the symbol
"::" MUST be used to its maximum capability. For example, 2001:db8:0:0:0:0:2:1 must be shortened to
2001:db8::2:1.»**; **«The symbol "::" MUST NOT be used to shorten just one 16-bit 0 field.»**; y las
letras, en minúscula (**«MUST be represented in lowercase»**). El RFC 4291 escribe en mayúsculas: al
leer valen las dos; al escribir, minúsculas.

Los prefijos que hay que reconocer:

| Prefijo | Qué es | Fuente |
|---|---|---|
| ::/128 | Sin especificar | RFC 4291 |
| ::1/128 | Bucle local (el 127.0.0.1 de IPv6) | RFC 4291 |
| FF00::/8 | Multidifusión | RFC 4291 |
| FE80::/10 | Unidifusión de enlace local: **«Link-Local addresses are for use on a single link.»** | RFC 4291 |
| FC00::/7 | Direcciones locales únicas (ULA), el equivalente de las privadas: **«These addresses are not expected to be routable on the global Internet.»** | RFC 4193 |
| 2001:db8::/32 | **«Documentation»** | RFC 6890 |
| ::ffff:0:0/96 | **«IPv4-mapped Address»** | RFC 6890 |
| 64:ff9b::/96 | Prefijo de traducción IPv4-IPv6 (NAT64) | RFC 6890 |
| Todo lo demás | **«Global Unicast (everything else)»** | RFC 4291 |

Estructura de una dirección global: prefijo global de encaminamiento, identificador de subred e
identificador de interfaz; **«For all unicast addresses, except those that start with the binary
value 000, Interface IDs are required to be 64 bits long»**. En la práctica, la subred IPv6 es un
/64 y la mitad derecha de la dirección identifica al equipo.

Cómo obtiene dirección un equipo IPv6:

- Autoconfiguración sin estado (SLAAC, RFC 4862): **«The autoconfiguration process includes generating
  a link-local address, generating global addresses via stateless address autoconfiguration, and the
  Duplicate Address Detection procedure to verify the uniqueness of the addresses on a link.»**
- DHCPv6 (RFC 9915, enero de 2026, que sustituye al 8415): **«DHCPv6 can operate either in place of
  or in addition to stateless address autoconfiguration (SLAAC).»**
- El descubrimiento de vecinos (RFC 4861) sustituye a ARP: los nodos lo usan **«to discover each
  other's presence, to determine each other's link-layer addresses, to find routers»**; va sobre
  ICMPv6, el protocolo de mensajes de control de IPv6 (RFC 4443).

### Convivencia y transición entre IPv4 e IPv6

IPv4 e IPv6 no son compatibles entre sí: un equipo que sólo habla IPv6 no puede hablar con uno que
sólo habla IPv4 sin ayuda. Los mecanismos se agrupan en tres familias (la agrupación es didáctica;
cada una tiene su norma):

| Familia | Qué hace | Norma |
|---|---|---|
| Pila doble | **«Dual stack implies providing complete implementations of both versions of the Internet Protocol (IPv4 and IPv6)»**; esos equipos se llaman **«"IPv6/IPv4 nodes"»** | RFC 4213 |
| Túnel | Meter IPv6 dentro de IPv4 para cruzar una red que sólo tiene IPv4: **«The technique of encapsulating IPv6 packets within IPv4 so that they can be carried across IPv4 routing infrastructures.»** En el túnel configurado, los extremos se fijan a mano | RFC 4213 |
| Traducción | NAT64 con estado **«allows IPv6-only clients to contact IPv4 servers using unicast UDP, TCP, or ICMP»**; DNS64 **«is a mechanism for synthesizing AAAA records from A records»**, para que el cliente IPv6 encuentre al servidor que sólo tiene IPv4 | RFC 6146 y RFC 6147 |

En un equipo de pila doble, cuál de las dos se usa la decide el algoritmo de selección de direcciones
del RFC 6724: **«the algorithm might prefer IPv6 addresses over IPv4 addresses, or vice versa»**,
según las direcciones de origen disponibles. Un equipo de pila doble puede apagar una de las dos:
**«IPv6/IPv4 nodes MAY provide a configuration switch to disable either their IPv4 or IPv6 stack.»**

Mientras tanto, IPv4 se estira con NAT: la de casa o de la oficina (RFC 3022) y la de operador (CGN,
bloque 100.64.0.0/10), que el RIPE NCC cita como una de las respuestas al agotamiento que no lo
resuelven. El registro de bloques especiales recoge otros mecanismos de transición —**«6to4»**
(2002::/16), **«TEREDO»** (2001::/32), **«DS-Lite»** (192.0.0.0/29)—, que este tema sólo nombra.

En Windows, `ipconfig` **«muestra las direcciones IPv6 y de la versión 4 del Protocolo de Internet
(IPv4), la máscara de subred y la puerta de enlace predeterminada para todos los adaptadores»**; con
`/all`, la configuración completa; `/release` y `/renew` liberan y renuevan la concesión DHCP, y
`/release6` y `/renew6` la de DHCPv6; `/flushdns` **«Vacía y restablece el contenido de la caché de
resolución del cliente DNS.»**

## 5. Redes de área local

### Conceptos

**«A LAN is a network that efficiently interconnects several hosts (usually a few dozens to a few
hundreds) in the same room, building or campus.»** (una red de área local, LAN, une con eficacia unas
decenas o centenares de equipos en una sala, un edificio o un recinto). La tecnología de cable que
domina es Ethernet, normalizada por el grupo IEEE 802.3; la inalámbrica, Wi-Fi (IEEE 802.11,
epígrafe 6).

Datos de Ethernet que conviene tener (manual de Bonaventure):

- Origen: **«Ethernet was designed in the 1970s at the Palo Alto Research Center»**, con cable coaxial
  compartido a 3 Mbit/s; la primera especificación comercial (DIX) lo fijó en 10 Mbit/s.
- Direcciones físicas (MAC) de 48 bits, únicas en el mundo: **«The upper 24 bits are used to encode an
  Organization Unique Identifier (OUI)»**, el identificador del fabricante, y **«The first bit of the
  address indicates whether the address identifies a network adapter or a multicast group.»**
- La trama: dirección de destino, dirección de origen, tipo (*EtherType*), datos y control de errores.
  Valores frecuentes del tipo: **«0x0800 for IPv4, 0x86DD for IPv6 6 and 0x806 for the Address
  Resolution Protocol (ARP)»** (el «6» que aparece tras IPv6 es una llamada a nota del manual). Los
  datos van de 46 a 1.500 octetos: **«The minimum length of the payload is 46 bytes»** y **«The Ethernet
  payload cannot be longer than 1500 bytes.»** Al final, **«a 32 bit Cyclical Redundancy Check (CRC)»**.
- El servicio: **«An Ethernet network provides an unreliable connectionless service. It supports three
  different transmission modes : unicast, multicast and broadcast.»**

La diferencia entre las dos direcciones que maneja un equipo:

| Dirección | De qué capa es | Quién la usa | Cuánto alcanza |
|---|---|---|---|
| MAC, o dirección física | Enlace, capa 2 | El conmutador | Sólo dentro del segmento local |
| IP, o dirección lógica | Red, capa 3 | El enrutador | De una red a otra, por todo internet |

La razón de fondo, que conviene entender y no memorizar: la dirección física va grabada en la tarjeta
y no dice dónde está el equipo; la dirección IP se asigna y sí dice a qué red pertenece, y encaminar
es precisamente decidir a qué red hay que mandar el paquete. ARP (en IPv4) y el descubrimiento de
vecinos (en IPv6) son los que averiguan qué MAC corresponde a una IP del mismo segmento.

Las capas físicas de Ethernet de par trenzado y su uso de los pares:

| Variante | Velocidad | Cómo usa los cuatro pares |
|---|---|---|
| 10BASE-T | 10 Mbps | Dos pares: uno transmite y otro recibe |
| 100BASE-TX | 100 Mbps | Dos pares: uno transmite y otro recibe |
| 1000BASE-T | 1000 Mbps | Los cuatro, a la vez, en los dos sentidos |

El aviso práctico que se deriva: un cable con dos pares partidos funcionaba a cien megabits y no
funciona a mil. (Los conectores y el cableado del puesto están en el tema 4.)

### Topologías

El manual de Bonaventure describe cuatro organizaciones físicas:

| Topología | Cómo es | Ventaja | Inconveniente |
|---|---|---|---|
| Malla completa | Un enlace entre cada par de equipos | **«the lowest delay between the hosts and the best resiliency against link failures»** | Hacen falta n(n−1)/2 enlaces y n−1 interfaces por equipo: **«full-mesh networks are rarely used except when there are few network nodes and resiliency is key»** |
| Bus | **«all hosts are attached to a shared medium, usually a cable through a single interface»**; lo que uno emite lo reciben todos | Un solo cable | **«if the bus is physically cut, then the network is split into two isolated networks»**. Fue la del primer Ethernet coaxial |
| Estrella | Un enlace de cada equipo a un nodo central | Si se corta un cable, **«only one node is disconnected from the network»**; se administra desde el centro | **«the failure of the central node implies the failure of the network»** |
| Anillo | Cada equipo enlazado con el siguiente; la señal circula en un sentido | Acceso ordenado (paso de testigo) | Con un solo anillo, **«if one of the links composing the ring is cut, the entire network fails»**; por eso se usan anillos dobles en redes metropolitanas |

Una quinta, el árbol, es la que resulta de encadenar concentradores o conmutadores en jerarquía: con
concentradores **«the network topology must be a tree»** (no admite bucles). Hoy la LAN de cable es una
estrella (o un árbol de estrellas): **«A 10BaseT network is a star-shaped network.»** Física y lógica
pueden no coincidir: una estrella con concentrador en el centro se comportaba como un bus, porque el
concentrador repetía todo a todos (oficio).

### Control de acceso al medio

Cuando varios equipos comparten el medio, dos que emiten a la vez chocan: **«Such simultaneous
transmissions are called collisions.»** Todas las tecnologías de LAN usan un algoritmo de control de
acceso al medio (MAC), y hay dos familias:

| Familia | Idea | Ejemplos |
|---|---|---|
| Determinista (pesimista) | **«These algorithms ensure that at any time, at most one device is allowed to send a frame on the LAN.»** No hay colisiones | Paso de testigo: Token Ring (IEEE 802.5), Token Bus (IEEE 802.4) |
| Estocástica (optimista) | **«These algorithms assume that collisions are part of the normal operation of a Local Area Network.»** Las reducen, no las evitan | ALOHA, CSMA, CSMA/CD (Ethernet), CSMA/CA (Wi-Fi) |

- *CSMA* (acceso múltiple con detección de portadora): **«CSMA requires all nodes to listen to the
  transmission channel to verify that it is free before transmitting a frame»**.
- *CSMA/CD* (con detección de colisiones), el de Ethernet: el equipo escucha mientras transmite;
  **«When an Ethernet host detects a collision while it is transmitting, it immediately stops its
  transmission.»** Después **«it sends a special jamming signal on the cable to ensure that all hosts
  have detected the collision»** y vuelve a intentarlo tras una espera aleatoria que crece con cada
  colisión. Por eso Ethernet tiene una trama mínima: el intervalo de 51,2 microsegundos **«corresponds
  to a minimum frame size of 64 bytes»**.
- *CSMA/CA* (con prevención de colisiones), el de Wi-Fi: **«was designed for the popular WiFi
  wireless network technology»**. En lugar de detectar colisiones intenta evitarlas ajustando sus
  temporizadores: espera a que el canal esté libre un tiempo (DIFS), usa
  acuses de recibo tras una pausa corta (SIFS) y una espera aleatoria que se congela si el canal se
  ocupa. Puede además reservar el canal con tramas RTS/CTS.
- *Paso de testigo*: **«The token is a small frame that represents the authorization to transmit
  data frames on the ring.»** Sólo transmite quien tiene el testigo.

Con conmutadores y enlaces dúplex (cada equipo con su cable hasta el conmutador), las colisiones
desaparecen en la práctica: cada puerto es un dominio de colisión propio (siguiente apartado; oficio).

Además del acceso al medio, el control de acceso a la red —quién puede conectarse a un puerto o a una
red inalámbrica— lo hace la norma IEEE 802.1X, que se explica en el epígrafe 6.

### Segmentación

Segmentar es partir la red para que el tráfico de unos no moleste a otros, contener averías y
separar por seguridad. Hay dos dominios que hay que distinguir:

| Dominio | Qué es | Quién lo parte |
|---|---|---|
| De colisión | El conjunto de equipos que pueden pisarse al transmitir a la vez | Cada puerto de un conmutador es uno: el conmutador lo parte |
| De difusión | El conjunto de equipos a los que llega un mensaje dirigido a todos | Cada VLAN es uno, y sólo un enrutador o una VLAN distinta lo parte |

Y el dato histórico que explica por qué la pregunta insiste en la colisión: en un concentrador todos
los equipos compartían un solo dominio de colisión y se pisaban. El conmutador acabó con eso al darle
a cada puerto el suyo.

Los tres escalones de la segmentación:

1. *Conmutador (capa 2).* **«An Ethernet switch is a relay that operates in the datalink layer»**:
   aprende en qué puerto está cada MAC (**«This algorithm extracts the source address of the received
   frames and remembers the port over which a frame from each source Ethernet address has been
   received.»**) y reenvía cada trama sólo por el puerto del destino; si no lo conoce, por todos menos
   por el de llegada. Si hay bucles entre conmutadores, una trama se duplica sin fin, porque Ethernet
   no tiene TTL; lo evita el protocolo de árbol de expansión (STP, IEEE 802.1D), que **«allows
   switches to automatically disable ports on Ethernet switches to ensure that the network does not
   contain any cycle»**.
2. *VLAN (capa 2 lógica).* **«A virtual LAN can be defined as a set of ports attached to one or more
   Ethernet switches.»** Qué añade la VLAN: partir un conmutador físico en varias redes lógicas que no
   se ven entre sí. Dos equipos en VLAN distintas del mismo conmutador necesitan un enrutador para
   hablarse, igual que si estuvieran en edificios distintos. Entre conmutadores, la VLAN viaja en una
   etiqueta IEEE 802.1Q: **«This 32 bit header includes a 12 bit VLAN field that contains the VLAN
   identifier of each frame.»** El identificador de protocolo de la etiqueta vale **«0x8100»**, hay
   un campo de prioridad de 3 bits (PCP, de 0 a 7), y como el 0 indica que la trama no es de ninguna
   VLAN y el 0xFFF está reservado, **«4094 different VLAN identifiers can be used in an Ethernet
   network»**. El tamaño máximo de trama crece 4 octetos.
3. *Subred IP (capa 3).* Cada VLAN suele llevar su propia subred (epígrafe 4) y el enrutador o el
   conmutador de capa 3 decide qué pasa de una a otra (oficio).

| Término | Qué es, en una línea |
|---|---|
| VLAN | Partir un conmutador físico en varias redes lógicas que no se ven entre sí |
| TRUNK | Un enlace entre conmutadores que transporta a la vez el tráfico de varias VLAN, etiquetado |
| ACL | Una lista que dice qué tráfico se deja pasar y cuál no, por dirección y puerto |

Un puerto que lleva una sola VLAN sin etiquetar se llama de acceso (es donde se conecta el puesto);
el troncal lleva varias etiquetadas (oficio). Y la segmentación también es seguridad: con un
concentrador **«A host attached to a hub will be able to capture all the frames exchanged between any
pair of hosts attached to the same hub.»**; con un conmutador eso mejora, pero su tabla de MAC es
atacable: **«A malicious host could overflow the MAC address table of the switch by generating
thousands of frames with random source addresses.»**

### Las normas IEEE 802

El comité de normas de LAN y MAN del IEEE (LMSC) **«develops and maintains networking standards and
recommended practices for local, metropolitan, and other area networks»**; **«The most widely used
standards are for Ethernet, Bridging and Virtual Bridged LANs Wireless LAN, Wireless PAN, Wireless
MAN, Wireless Coexistence, Media Independent Handover Services, and Wireless RAN.»** Cada área la
lleva un grupo de trabajo.

| Grupo | Nombre (página del IEEE 802) | Normas que hay que conocer |
|---|---|---|
| 802.1 | **«Higher Layer LAN Protocols Working Group»** | Puentes y conmutación (802.1D, árbol de expansión), VLAN (802.1Q), control de acceso por puerto (802.1X); el reparto se deduce de la numeración de cada norma (oficio) |
| 802.3 | **«Ethernet Working Group»** | Ethernet; entre sus proyectos en curso, **«200 Gb/s, 400 Gb/s, 800 Gb/s, and 1.6 Tb/s Ethernet»** |
| 802.11 | **«Wireless LAN Working Group»** | Wi-Fi (epígrafe 6) |
| 802.15 | **«Wireless Specialty Network (WSN) Working Group»** | Redes inalámbricas de área personal (PAN) |
| 802.18 | **«Radio Regulatory TAG»** | Grupo asesor de regulación radioeléctrica |
| 802.19 | **«Wireless Coexistence Working Group»** | Convivencia entre redes inalámbricas |
| 802.24 | **«Vertical Applications TAG»** | Aplicaciones sectoriales |

Disueltos, según la página de grupos inactivos del comité (no hay ninguno en hibernación): **«802.2 Logical Link Control Working Group»** (la subcapa de control
de enlace lógico, LLC), **«802.4 Token Bus Working Group»**, **«802.5 Token Ring Working Group»**, 802.6
(MAN), 802.16 (**«Broadband Wireless Access Working Group»**), 802.17, 802.20, 802.21, 802.22 y 802.23,
entre otros. La historia de los tres primeros explica la familia: el comité **«chose to work in
parallel on three different LAN technologies and created three working groups»**: 802.3 para CSMA/CD,
802.4 para el bus con testigo y 802.5 para el anillo con testigo; las tres **«agreed to use the 48 bits
MAC addresses specified initially for Ethernet»**.

La división de la capa de enlace que hizo el IEEE: arriba, el control de enlace lógico (LLC, 802.2),
común a todas; abajo, el control de acceso al medio (MAC) y la capa física propios de cada tecnología
(802.3, 802.11…). Es la razón de que la dirección MAC se llame así (oficio).

## 6. Redes inalámbricas IEEE 802.11

### Los estándares

El grupo IEEE 802.11 normaliza las redes de área local inalámbricas (WLAN); la Wi-Fi Alliance
certifica los productos y les da el nombre comercial (Wi-Fi 4, 5, 6, 7). Las dos cosas no son lo
mismo: «802.11ax» es una enmienda de la norma y «Wi-Fi 6» un programa de certificación. Wi-Fi creció en
una banda de uso libre: **«In 1985, the 2.400-2.500 GHz band was added to the list of ISM
bands.»**, las bandas industriales, científicas y médicas que no necesitan licencia.

| Enmienda IEEE | Título del proyecto (IEEE 802.11) | Nombre comercial | Banda | Notas |
|---|---|---|---|---|
| 802.11 (original) | — | — | 2,4 GHz | 2 Mbit/s máximos según el manual de Bonaventure |
| 802.11a-1999 | **«Higher Speed PHY Extension in the 5GHz Band»** | — | 5 GHz | 54 Mbit/s máximos (Bonaventure) |
| 802.11b-1999 | **«Higher Speed PHY Extension in the 2.4 GHz Band»** | — | 2,4 GHz | 11 Mbit/s máximos (Bonaventure) |
| 802.11g-2003 | **«Further Higher Data Rate Extension in the 2.4 GHz Band»** | — | 2,4 GHz | 54 Mbit/s máximos (Bonaventure) |
| 802.11n-2009 | **«High Throughput»** | Wi-Fi 4 (**«introduced in 2009»**) | 2,4 y 5 GHz | Primera de la tabla en las dos bandas (Bonaventure) |
| 802.11ac-2013 | **«Very High Throughput < 6 GHz»** | Wi-Fi 5 (**«introduced in 2014»**) | Por debajo de 6 GHz | **«Most Wi-Fi 5 products are dual-band, operating in both the 2.4 GHz and 5 GHz bands.»** |
| 802.11ax-2021 | **«High Efficiency WLAN»** | Wi-Fi 6 (**«Introduced in 2018»**) y Wi-Fi 6E | 2,4, 5 y 6 GHz | **«Wi-Fi 6E extends Wi-Fi 6 support to the 6ghz band.»** |
| 802.11be-2024 | **«Extremely High Throughput»** | Wi-Fi 7 (**«Introduced in 2024»**) | 2,4, 5 y 6 GHz | Operación multienlace (MLO) |
| 802.11bn (en curso) | **«Ultra High Reliability»** | — | — | Proyecto en tramitación |

Dos fechas distintas conviven en la tabla: la del documento IEEE (en el nombre de la enmienda) y la
de lanzamiento del programa de la Wi-Fi Alliance, que puede ser anterior (Wi-Fi 6 en 2018, la
enmienda en 2021). La Wi-Fi Alliance presenta ya **«Wi-Fi 8 is the next generation of Wi-Fi®»**; qué
enmienda IEEE le corresponderá no consta en lo leído.

La norma base vigente es la revisión **«802.11-2024»**, que el grupo de trabajo describe como
**«802.11 Accumulated Maintenance Changes»**; la tabla de proyectos del grupo (actualizada el
19-09-2026) lista la 802.11be-2024 como enmienda aparte, con la 802.11-2024 entre sus bases. Otras
enmiendas que se citan: **«MAC Security Enhancements»** (802.11i-2004, la seguridad) y **«Mesh
Networking»** (802.11s-2011, la malla). Fuera de las bandas habituales, la Wi-Fi Alliance certifica
además Wi-Fi HaLow, que **«operates in sub-1 GHz spectrum to deliver approximately 1 km range»**, y
WiGig, que da acceso a **«the uncongested 60 GHz frequency band»**.

Para saber qué admite la tarjeta de un portátil con Windows: **«typing the command netsh wlan show
drivers. Look next to Radio types supported and see if it includes 802.11be (for Wi-Fi 7) or 802.11ax
(for Wi-Fi 6/6e)»**. Y una condición de versión: **«Wi-Fi 7 is available starting with Windows 11,
version 24H2.»**

### Las técnicas de transmisión

Todas las 802.11 comparten el acceso al medio y la trama: **«802.11 networks use the CSMA/CA Medium
Access Control technique described earlier and they all assume the same architecture and use the same
frame format.»** Lo que cambia de una generación a otra es la capa física:

| Técnica | Qué hace | Generación en que la cita la fuente |
|---|---|---|
| OFDMA (acceso múltiple por división de frecuencias ortogonales) | **«effectively shares channels to increase network efficiency and lower latency»**: reparte un canal entre varios equipos a la vez | Wi-Fi 6 |
| MU-MIMO (entrada y salida múltiples multiusuario) | **«allows more data to be transferred at one time, enabling APs to concurrently handle more devices»**; Wi-Fi 6 pasa de cuatro a ocho flujos espaciales | Wi-Fi 6 |
| Modulación QAM | Más bits por símbolo: 1024-QAM en Wi-Fi 6; en Wi-Fi 7, **«4K quadrature amplitude modulation mode (4K QAM) achieves 20% higher transmission rates than Wi-Fi 6's 1024 QAM»** | Wi-Fi 6 / Wi-Fi 7 |
| Anchura de canal | **«160 MHz channel utilization capability»** en Wi-Fi 6; **«320 MHz channels available in the 6 GHz band provide twice the throughput of Wi-Fi 6»** en Wi-Fi 7 | Wi-Fi 6 / Wi-Fi 7 |
| Conformación de haz (*beamforming*) | **«Transmit beamforming enables higher data rates at a given range to increase network capacity»** | Wi-Fi 6 (lista de la Wi-Fi Alliance) |
| TWT (tiempo de activación programado) | **«significantly improves network efficiency and device battery life»** | Wi-Fi 6 |
| MLO (operación multienlace) | **«allows devices to use multiple bands (2.4 GHz, 5 GHz, and/or 6 GHz) simultaneously to avoid network congestion and maintain connectivity»** | Wi-Fi 7 |

Las velocidades máximas teóricas de Wi-Fi 6 y Wi-Fi 7 no se dan: las fuentes leídas sólo dan
comparaciones (el doble, un 20 % más) y Microsoft advierte de que **«performance may vary by
manufacturer and hardware device capabilities»**.

### Los dispositivos de interconexión

| Equipo | En qué capa trabaja | Qué decide | Con qué dirección |
|---|---|---|---|
| Concentrador | 1, física | Nada: repite por todos los puertos | Ninguna |
| Conmutador | 2, enlace | Por qué puerto sale la trama | La dirección física |
| Enrutador | 3, red | A qué red se manda el paquete | La dirección IP |
| Puerta de enlace | La que haga falta | Traduce entre dos mundos distintos | La que corresponda |

Qué es exactamente una puerta de enlace, porque el término se usa con dos sentidos:

1. En la configuración de un equipo, la puerta de enlace predeterminada es la dirección del enrutador
   por el que sale lo que no es de su red. Ése es el uso corriente.
2. En su sentido estricto, una puerta de enlace es el elemento que traduce entre dos protocolos o dos
   formatos distintos —una pasarela de correo, una de voz sobre red a telefonía—, y ahí puede trabajar
   hasta en la capa de aplicación.

El que es propio de la red inalámbrica es el punto de acceso: **«An 802.11 access point is a relay that
operates in the datalink layer like switches.»** Une los equipos inalámbricos con la LAN de cable.
Los puntos de acceso suelen alimentarse por el propio cable de red (PoE): van por el mismo cable las
dos cosas: los datos y la alimentación. Una cámara de red, un punto de acceso o un teléfono de
sobremesa se cuelgan de un solo cable y no necesitan enchufe. La cuenta que hay que hacer al
instalar: un conmutador PoE tiene un presupuesto total de potencia, y la suma de lo que piden los
aparatos no puede pasarlo.

En casa o en una oficina pequeña todo va en un solo aparato. Qué hace cada mitad del aparato: el
módem adapta la señal entre el medio físico del operador y la red local; el router encamina los
paquetes entre la red local e internet, y normalmente también asigna direcciones por DHCP y hace
traducción de direcciones. A eso se suma el punto de acceso inalámbrico.

### Las topologías inalámbricas

**«There are, in practice, two main types of WiFi networks : independent or adhoc networks and
infrastructure networks»**:

| Topología | Cómo es |
|---|---|
| Independiente o *ad hoc* | **«An independent or adhoc network is composed of a set of devices that communicate with each other.»** Todos tienen el mismo papel y no suele haber salida a Internet; sirve, por ejemplo, para **«connect a computer with a WiFi printer»** |
| Infraestructura | **«Most WiFi networks are infrastructure networks.»** Uno o varios puntos de acceso unidos a una LAN fija; **«Each WiFi device is associated to one access point»** |
| Malla | Los puntos de acceso se enlazan entre sí por radio; enmienda **«Mesh Networking»** (802.11s) |

El IEEE llama conjunto básico de servicios (BSS) a **«a group of devices that communicate with each
other»**. Cómo se une un equipo a una red de infraestructura: los puntos de acceso emiten tramas
baliza (*beacon*) con sus capacidades y su identificador de red (SSID), que **«can contain up to 32
characters»**; un punto de acceso puede no emitir balizas, y entonces el equipo pregunta con tramas de
sondeo (*probe request*). Después **«a WiFi station must be associated to this access point»** mediante una
petición y una respuesta de asociación.

### La seguridad

| Mecanismo | Qué es (fuentes de la Wi-Fi Alliance y de Microsoft) |
|---|---|
| WEP y TKIP | Antiguos e inseguros. Windows avisa desde la versión 1903 al conectarse a redes con ellos (**«which aren't as secure as those using WPA2 or WPA3»**) y anuncia que en una versión futura **«any connection to a Wi-Fi network using these old ciphers will be disallowed»**; los enrutadores **«should be updated to use AES ciphers, available with WPA2 or WPA3»** |
| WPA2 | La generación anterior, con más de una década de uso (**«the widespread adoption of WPA2 over more than a decade»**) |
| WPA3 | **«WPA3 is mandatory for Wi-Fi CERTIFIED devices»**. Las redes WPA3 **«Use the latest security protocols»**, **«Disallow outdated legacy protocols»** y **«Require use of Protected Management Frames (PMF)»** |
| WPA3-Personal | Con contraseña compartida; **«increased protections from password guessing attempts»** |
| WPA3-Enterprise | **«builds on top of WPA2-Enterprise by providing the additional requirement of using Protected Management Frames on all WPA3 connections with 802.1X for user authentication with a RADIUS server»**. Modo de 192 bits para datos sensibles; en él, **«EAP-TLS es el único método EAP permitido»** |
| PMF | Tramas de gestión protegidas: **«PMF is required for all new certified devices.»** |
| Wi-Fi Enhanced Open | Para redes abiertas: **«provide unauthenticated data encryption to users, an improvement over traditional open networks with no protections at all»** |

Si en la red hay puntos de acceso WPA2 y WPA3, **«your PC will first try to connect using
WPA3-Personal»**.

### La autenticación 802.1X

IEEE 802.1X es el control de acceso a la red por puerto: vale para un puerto de conmutador y para la
asociación a un punto de acceso. **«It blocks all traffic from a supplicant (client) at the interface
until the supplicant's credentials are presented and matched on the authentication server (a RADIUS
server).»** Cuando el cliente se autentica, **«the switch stops blocking access and opens the
interface to the supplicant»** (Juniper Networks). Tres papeles:

| Papel | Quién es | Qué hace |
|---|---|---|
| Solicitante (*supplicant*) | El equipo que se conecta (**«supplicant (end device)»**) | Presenta sus credenciales (usuario y contraseña, o certificado) |
| Autenticador | El conmutador o el punto de acceso (**«an authenticator port access entity (the switch)»**) | Bloquea el puerto hasta que el servidor dice sí, y hace de intermediario |
| Servidor de autenticación | Un servidor RADIUS | Comprueba las credenciales y autoriza |

Las piezas que intervienen:

- *EAP*, el protocolo de autenticación extensible: **«an authentication framework which supports
  multiple authentication methods. EAP typically runs directly over data link layers such as
  Point-to-Point Protocol (PPP) or IEEE 802, without requiring IP.»** Entre el equipo y el autenticador
  viaja encapsulado en la LAN (EAPOL; Windows espera unos segundos antes de enviar **«un mensaje de
  EAPOL-Start para iniciar el proceso de autenticación 802.1X»**).
- *Los métodos EAP* que Microsoft documenta para Windows: EAP-TLS, **«método EAP basado en
  estándares que usa TLS con certificados para la autenticación mutua»**, que por basarse en
  certificados suele dar la mayor seguridad; PEAP,
  que **«encapsula EAP dentro de un túnel TLS»**; y EAP-MSCHAP v2 (usuario y contraseña), que **«se
  puede usar como método independiente para VPN, pero solo como método interno para conexiones
  cableadas o inalámbricas»**.
- *RADIUS*, el servidor: **«RADIUS es un protocolo cliente-servidor que permite al equipo de acceso
  a la red (usado como clientes RADIUS) enviar solicitudes de autenticación y de cuentas a un servidor
  RADIUS.»** El conmutador o el punto de acceso es, por tanto, cliente RADIUS. Puerto:
  **«The officially assigned port number for RADIUS is 1812.»** En Windows Server, el servidor
  RADIUS es el Servidor de directivas de redes (NPS): **«NPS es la implementación de Microsoft del
  estándar RADIUS»**, y con Active Directory **«El mismo conjunto de credenciales se usa para el
  control de acceso a la red (autenticación y autorización del acceso a una red) y para iniciar sesión
  en un dominio de AD DS.»** Su asistente tiene un escenario para **«Servidor RADIUS para conexiones
  802.1X inalámbricas o por cable»**.

En un puerto de cable pueden conectarse varios equipos (por ejemplo, un teléfono con el ordenador
detrás). Juniper distingue tres modos: **«single supplicant—Authenticates only the first end
device.»** (los demás entran sin autenticarse), **«single-secure supplicant—Allows only one end device
to connect to the port.»** y **«multiple supplicant—Allows multiple end devices to connect to the
port. Each end device is authenticated individually.»** Y combina 802.1X con VLAN: el puerto puede
llevar a una VLAN distinta a quien falla la autenticación o no tiene 802.1X.

La relación con la red inalámbrica (oficio, a partir de la frase de Microsoft citada en el apartado
anterior): los modos de empresa de WPA2 y WPA3 son 802.1X aplicado a Wi-Fi, cada usuario con su
credencial comprobada por RADIUS; los modos personales, una contraseña compartida por todos. En una
organización, la opción segura es el modo de empresa.

## 7. Aplicación práctica

### Los cuatro datos de la configuración y el orden de la avería

Lo que conviene llevar visto son los cuatro datos que configuran cualquier equipo:

| Dato | Qué decide |
|---|---|
| Dirección IP | Quién es el equipo |
| Máscara de subred | Hasta dónde llega su red local |
| Puerta de enlace | Por dónde sale lo que no es de su red |
| Servidor de nombres | Quién traduce los nombres a direcciones |

Y la comprobación de averías que se deriva de ellos, en ese mismo orden: sin dirección, el equipo no
habla; con máscara mal puesta, habla con quien no debe; sin puerta de enlace, no sale de su red; sin
servidor de nombres, sale pero no encuentra nada por su nombre. Es el orden en que se mira una
configuración que no funciona.

Situar la avería en su capa antes de tocar nada (oficio): un cable roto o un puerto apagado es capa
física; un puerto del conmutador en la VLAN equivocada, o un 802.1X que no autentica, es capa de
enlace; una dirección o una máscara mal puestas, capa de red; un cortafuegos que cierra un puerto,
capa de transporte; un certificado caducado o un error 403, capa de aplicación.

### Las herramientas de diagnóstico

| Comando | Qué hace | Cuándo se usa |
|---|---|---|
| `ipconfig` | Enseña la configuración de red del propio equipo | Para saber qué dirección y qué puerta de enlace tengo yo |
| `ping` | Pregunta si el destino contesta | Para saber si hay conexión, sí o no |
| `tracert` | Enumera los saltos del camino hasta el destino | Para saber en qué salto se pierde |
| `netstat` | Enumera las conexiones abiertas del propio equipo | Para ver qué está hablando con qué |

`ping` **«Comprueba la conectividad a nivel de IP con otro equipo TCP/IP mediante el envío de mensajes
de solicitud de eco del protocolo de mensajes de control de Internet (ICMP).»** Y sirve para separar
red de nombres: **«Si el ping a la dirección IP se realiza correctamente, pero el ping al nombre del
equipo no, es posible que tenga un problema de resolución de nombres.»**

`tracert` se apoya en el TTL de la cabecera IP: envía el primer mensaje **«con un TTL de 1 e
incrementando el TTL en 1 en cada transmisión posterior hasta que el destino responde o se alcanza el
número máximo de saltos»**, que **«es 30 de forma predeterminada»**; cada enrutador que tira el
paquete al llegar el TTL a cero devuelve un aviso de tiempo excedido, y así se va sabiendo quién está
en el camino. Si un enrutador no devuelve ese aviso, **«se muestra una fila de asteriscos (`*`) para
ese salto»**. El `ping` contesta si llega o no llega; no dice dónde se cortó. El `tracert` va
preguntando por el camino, salto a salto, y el último que contesta es el punto donde termina lo que
funciona: el fallo está en el salto siguiente.

### Supuestos resueltos

1. *Un usuario no navega; `ipconfig` muestra 169.254.12.7 y ninguna puerta de enlace.* El equipo no ha
   obtenido dirección del servidor DHCP y se ha puesto una de enlace local (epígrafe 4). Se comprueba
   el cable o la conexión inalámbrica, se pide de nuevo con `ipconfig /release` y `ipconfig /renew`, y
   si sigue igual se mira el servidor DHCP o la VLAN del puerto.
2. *El `ping` a 8.8.8.8 responde, pero no se abre ninguna página por su nombre.* La red y la salida
   funcionan; falla la resolución de nombres. Se revisa el servidor DNS configurado y se vacía la caché
   con `ipconfig /flushdns`.
3. *Hay que dar direcciones a una red de 60 equipos con el mínimo desperdicio.* 60 + 2 = 62 ≤ 64 = 2⁶:
   seis bits de equipo, prefijo /26, máscara 255.255.255.192, 62 direcciones utilizables.
4. *Abreviar 2001:0db8:0000:0000:0000:ff00:0042:8329.* Se quitan los ceros a la izquierda de cada
   grupo (2001:db8:0:0:0:ff00:42:8329) y se sustituye por «::» la secuencia más larga de grupos a cero:
   2001:db8::ff00:42:8329. Con el RFC 5952, en minúsculas y con un solo «::».
5. *Un datagrama IPv4 llega con IHL = 6.* La cabecera mide 6 × 4 = 24 octetos: lleva 4 octetos de
   opciones.
6. *Un navegador muestra un 401 en una aplicación interna y otro usuario recibe un 403.* El primero
   no ha presentado credenciales válidas; el segundo está identificado pero no tiene permiso (epígrafe
   2).
7. *Se monta la red inalámbrica de una oficina con cuentas de Active Directory.* Modo WPA3-Enterprise
   (o WPA2-Enterprise si algún equipo no admite WPA3), autenticación 802.1X con un servidor RADIUS
   (NPS en Windows Server), método EAP-TLS con certificados o PEAP; puntos de acceso como clientes
   RADIUS; la red de invitados, aparte, en otra VLAN. Nunca WEP ni TKIP.
8. *Dos equipos en el mismo conmutador, en las VLAN 10 y 20, no se ven.* Es lo esperado: cada VLAN es
   un dominio de difusión; para hablarse hace falta un enrutador o un conmutador de capa 3 entre las
   dos subredes.
9. *Comprobar si el portátil admite Wi-Fi 7.* `netsh wlan show drivers` y buscar 802.11be en los
   tipos de radio; además, Windows 11 24H2 o posterior.

## Lo que este tema no da, y dónde está

- El texto de las normas IEEE (802.3, 802.1D, 802.1Q, 802.1X, 802.11-2024 y sus enmiendas) y el de la
  norma ISO del modelo OSI: no se han leído (son de pago o la página del IEEE no se pudo abrir). Lo que
  el tema dice de ellas procede de las páginas del comité IEEE 802 y del grupo 802.11, del manual de
  Bonaventure y de la documentación de Microsoft, Juniper Networks y la Wi-Fi Alliance. Por eso no se
  da el año de la edición vigente de 802.1X, ni los valores de tiempo de SIFS, DIFS y la ranura de
  Wi-Fi, que dependen de la capa física.
- Las velocidades máximas teóricas de Wi-Fi 5, Wi-Fi 6 y Wi-Fi 7, y qué enmienda IEEE corresponderá
  a Wi-Fi 8: no constan en las fuentes leídas. Para 802.11n el manual de Bonaventure da 150 Mbit/s
  máximos, cifra que no se ha contrastado con la norma y por eso no se recoge en la tabla.
- Qué canales y potencias de las bandas de 2,4, 5 y 6 GHz se pueden usar en España (Cuadro Nacional de
  Atribución de Frecuencias): no se ha leído; por eso tampoco se da el reparto de canales sin
  solapamiento de 2,4 GHz.
- El porcentaje actual de uso de IPv6: no se ha encontrado una fuente leíble a la fecha.
- Los mecanismos de transición 6to4, Teredo y DS-Lite: sólo se nombran, porque figuran en el registro
  de bloques especiales; no se desarrollan, ni otros que no se han leído.
- WEP y la primera WPA: sólo lo que dice Microsoft de WEP y TKIP; su funcionamiento no se ha leído.
- El navegador Firefox: su página de ayuda no se pudo descargar; el epígrafe 3 se basa en Chrome y
  Edge.
- Los protocolos de encaminamiento (RIP, OSPF, BGP) más allá de su clasificación, el detalle de DNS y
  el funcionamiento interno de TCP (ventanas, control de congestión): el enunciado no los pide.
- Cableado, conectores RJ45 y fibra: tema 4. Configuración de red de Windows 11: tema 6. Active
  Directory: tema 8. Certificados, autoridades de certificación, cortafuegos, VPN y malware: tema 14.
- La red de la RTVA o de CSRTV (qué electrónica, qué VLAN, qué Wi-Fi y qué autenticación usa): no consta
  en ningún documento publicado.

## Trazabilidad

Todas las fuentes se leyeron el 05-10-2026, en su versión en línea de ese día. La vigencia de cada
RFC se comprobó en el índice de la serie (el índice publicado en rfc-editor.org), que registra el RFC 8446
como sustituido por el RFC 9846 y el RFC 8415 por el RFC 9915.

| Fuente | Qué sostiene |
|---|---|
| Internet Society, *Brief History of the Internet* (Leiner, Cerf, Clark, Kahn y otros) | Definición del FNC, arquitectura abierta y reglas de Kahn, cronología de 1962 a 1995, direcciones de 32 bits del TCP original |
| RFC 791 (IPv4), RFC 1112 (multidifusión), RFC 1122 (requisitos de equipos), RFC 1918 (privadas), RFC 950 (subredes), RFC 4632 (CIDR), RFC 6890 y RFC 6598 (bloques especiales), RFC 3927 (enlace local), RFC 2474 y RFC 3168 (DS y ECN), RFC 3022 (NAT) | Cabecera y clases de IPv4, cinco clases, capas de Internet, difusión, máscara y prefijos, reparto IANA-RIR, bloques especiales, campo DS, NAT |
| RFC 8200 (IPv6), RFC 4291 (direccionamiento), RFC 4193 (ULA), RFC 5952 (escritura), RFC 4862 (SLAAC), RFC 4861 (descubrimiento de vecinos), RFC 4443 (ICMPv6), RFC 9915 (DHCPv6), RFC 6724 (selección de direcciones) | Cabecera, extensiones, fragmentación y MTU de IPv6; tipos, notación y prefijos; autoconfiguración |
| RFC 4213, RFC 6146 y RFC 6147 | Pila doble, túnel configurado, NAT64 y DNS64 |
| RFC 9110 (HTTP), RFC 9000 (QUIC), RFC 6797 (HSTS), RFC 6265 (cookies), RFC 8484 (DoH), RFC 1034 (DNS), RFC 2131 (DHCP), RFC 768 (UDP) | Sin estado, métodos, códigos de estado, versiones, puertos 80 y 443, esquema https |
| RFC 9846 (TLS 1.3), RFC 8996, RFC 7568, RFC 6101 y fechas del índice de RFC (2246, 4346, 5246, 8446) | Propiedades y componentes de TLS, cambios de 1.2 a 1.3, retirada de SSL 3.0, TLS 1.0 y 1.1 |
| RFC 3748 (EAP) y RFC 2865 (RADIUS) | Marco EAP sobre la capa de enlace; puerto 1812 |
| ICANN, comunicado de 3-II-2011; RIPE NCC, noticia de 25-XI-2019; UIT, comunicado de 17-XI-2025 (*Facts and Figures 2025*) | Agotamiento de IPv4, CGNAT, usuarios de Internet en 2025 |
| CERN, info.cern.ch | Primer sitio web y su presentación |
| Ayuda de Google Chrome (Incógnito, Navegación segura, seguridad y protección, cookies) y de Microsoft Edge (prevención de seguimiento, SmartScreen), en castellano | Epígrafe 3 |
| IEEE 802 LMSC (portada y grupos disueltos), IEEE 802.3, IEEE 802.11 *Timelines* (19-09-2026) | Grupos de trabajo, títulos y años de las enmiendas 802.11, 802.11-2024 y 802.11be-2024 |
| O. Bonaventure, *Computer Networking: Principles, Protocols and Practice*, 3.ª ed., Universidad Católica de Lovaina, licencia CC BY (capítulos «Sharing resources», «Datalink layer technologies», «Reference models») | LAN, topologías, control de acceso al medio, Ethernet, conmutadores, STP, VLAN 802.1Q, 802.11 (bandas antiguas, *ad hoc* e infraestructura, punto de acceso, balizas, SSID, asociación), modelos de referencia |
| Wi-Fi Alliance (generaciones Wi-Fi y seguridad) y Microsoft (*Faster and more secure Wi-Fi in Windows*, WiFiCx Wi-Fi 7, funciones retiradas de Windows) | Wi-Fi 4 a 8, técnicas de transmisión, WPA3, PMF, Enhanced Open, `netsh wlan show drivers`, WEP y TKIP |
| Microsoft Learn: EAP para acceso a redes, Servidor de directivas de redes, `ipconfig`, `ping`, `tracert`, información general sobre servicios y puertos de Windows Server (castellano); Juniper Networks, *802.1X Authentication* | 802.1X, métodos EAP, RADIUS y NPS, modos de solicitante; comandos de diagnóstico; puertos de LDAP y SNMP |

Algunas citas en inglés llevan detrás, en redonda, su traducción. Los RFC se citan sin los saltos
de página del texto original.

Oficio sin fuente detrás, y así se declara: las tablas de correspondencia entre capas OSI y TCP/IP con
sus ejemplos de protocolo, la regla para situar un protocolo en su capa y la de situar una avería; la
tabla de TCP frente a UDP; la definición de sistema autónomo y la tabla de protocolos de encaminamiento
internos y externos; la lista de servicios con sus puertos (salvo 80 y 443, del RFC 9110, y los de LDAP
y SNMP, de Microsoft); la tabla de tipos de registro DNS y la explicación del tiempo de vida (que el
RFC 1034 respalda: el TTL va **«in units of seconds»** y dice cuánto puede guardarse en caché); las partes de una URL;
la frase de que HTTPS no garantiza que el sitio sea honrado, el funcionamiento del certificado en tres
líneas y el sentido del candado; el aviso sobre «certificado SSL»; las funciones básicas del
navegador; la tabla de dirección física frente a lógica; la
tabla de pares de 10BASE-T, 100BASE-TX y 1000BASE-T; la tabla de dominios de colisión y difusión y la
de VLAN, TRUNK y ACL; puerto de acceso y troncal; la división LLC/MAC; la tabla de equipos por capa y
los dos sentidos de «puerta de enlace»; el PoE; el módem-router; los cuatro datos de la configuración
y el orden de la avería; la tabla de herramientas de diagnóstico; y los cálculos (rangos de clase
deducidos de los bits, cabeceras de 20, 40 y 60 octetos, tabla de prefijos, subredes y supuestos
resueltos), que no se toman de ninguna fuente: se hacen.
