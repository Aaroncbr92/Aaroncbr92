# Tema 13 del específico de Operador/a Informático · Redes, Internet y comunicaciones

**Siglas**: RTVA, CSRTV, FNC, RFC, IANA, RIR, LIR, ISP, OSI, DHCP, NAPT, CGN, CIDR, SLAAC, ULA, MTU, TTL, IHL, DS, ECN, VLAN, PCP, ACL, PoE, BSS, SSID, MLO, PMF, SAE, EAP, RADIUS, NPS.



Esqueleto para repasar, no resumen: fuente delante de cada línea (leídas 05/06-10-2026).

<!-- indice -->
## Índice
- 1 Internet · 2 HTTP, HTTPS, TLS · 3 Navegadores · 4 IPv4 e IPv6 · 5 LAN · 6 802.11 · 7 Práctica
<!-- /indice -->

## 1. Internet: arquitectura, origen, evolución, servicios
- FNC 24-X-1995: Internet = espacio de direcciones único (IP) + TCP/IP u otros compatibles + servicios encima. Web ≠ Internet.
- Kahn: red autónoma sin cambios internos; best effort; gateways/routers; sin control global operativo.
- RFC 1122: 4 capas (aplicación, transporte, internet, enlace); OSI 7 (Bonaventure). RFC 1122: aplicación = presentación + aplicación; manda el RFC si se cita.
- 7-6-5 aplicación (HTTP, DNS, SMTP, SSH); 4 transporte (TCP, UDP); 3 internet (IPv4, IPv6, ICMP); 2-1 enlace (802.3, 802.11).
- TCP: conexión, entrega, orden, congestión. UDP: ninguno, retardo bajo (RFC 768).
- RFC 4632: IANA a RIR (5; RIPE NCC uno), RIR a LIR/ISP.  Interno: RIP (v1, v2), OSPF, EIGRP. Externo: BGP. Métrica: saltos, coste, ancho de banda o retardo (oficio).
- ISOC: 1962 Licklider (MIT) «Galactic Network»; IX-1969 primer IMP en UCLA, 4 nodos a fin de año, S. Crocker crea RFC; 1970-72 NCP, 1972 correo; 1973 TCP escrito, 1974 publicado; 1-I-1983 NCP a TCP/IP (flag day); 1985 NSFNET exige TCP/IP; 1990 baja ARPANET, nace la web; IV-1995 fin NSFNET Backbone.
- CERN «home of the first website». TCP original: 8 bits red + 24 equipo.
- IPv4 agotado 3-II-2011 (ICANN); RIPE NCC 25-XI-2019 (solo recuperadas, lista de espera; transferencias y CGNAT no resuelven). IPv6 «a billion-trillion times larger» que 4,3 mil millones.
- HTTP/1.1 (1995-97), /2, /3 (QUIC sobre UDP), conviven (RFC 9110). TLS 1.3: RFC 8446 (2018), sustituido por RFC 9846 (VII-2026). UIT 2025: 6.000 M usuarios, 2.200 M sin conexión.
- Puertos: HTTP 80, HTTPS 443 (RFC 9110); DNS 53; SMTP 25 (587 cliente); IMAP 143/993; POP3 110/995; FTP 21 (desaconsejado), SFTP 22; SSH 22, Telnet 23 (desaconsejado); LDAP 389/636; SNMP 161 UDP, traps 162 (Microsoft).
- DNS (RFC 1034): A IPv4; AAAA IPv6; CNAME nombre; MX correo; NS autoritativos; TXT texto. TTL en segundos = máximo en caché.
- DHCP (RFC 2131): UDP 67 servidor, 68 cliente. DISCOVER (difusión) · OFFER · REQUEST (difusión, rechaza otras ofertas; confirma o prorroga) · ACK. NAK: dirección ya no vale; DECLINE: en uso; RELEASE; INFORM: ya configurado a mano. Relay si otra subred.
- NAPT (RFC 3022): muchas direcciones y puertos a una dirección y sus puertos.
- URL: esquema, anfitrión, ruta, puerto, parámetros, fragmento. Cookie (RFC 6265): estado sobre HTTP.

## 2. HTTP, HTTPS y TLS
- HTTP: petición (método + destino) y respuesta (código); sin estado (RFC 9110).
- Seguros: GET, HEAD, OPTIONS, TRACE. Idempotentes: PUT, DELETE y los seguros. POST y CONNECT, ninguno. HEAD = GET sin contenido; CONNECT túnel.
- Primer dígito = clase: 1xx informativo (100, 101); 2xx éxito (200, 201, 204); 3xx redirección (301, 302, 304); 4xx error cliente (400, 401, 403, 404); 5xx error servidor (500, 502, 503).
- 401 faltan credenciales; 403 entendida pero denegada; 404 sin representación actual o no la revela; 503 sobrecarga/mantenimiento. Desconocido = x00 de su clase (471 como 400).
- Versiones: 0.9/1.0 solo GET al principio; 1.1 (1995, estándar 1997, conexiones persistentes); 2 multiplexada sobre TLS y TCP; 3 QUIC sobre UDP. QUIC (RFC 9000): flujos con control, conexión de baja latencia, migración de ruta.
- HTTPS = HTTP sobre TLS, puerto 443: servidor autenticado, confidencialidad, integridad. No garantiza que el sitio sea de fiar; candado = cómo viaja, no a quién llega.
- HSTS (RFC 6797): cabecera Strict-Transport-Security; HTTPS obligatorio `max-age` segundos.
- TLS (RFC 9846, obsoleta RFC 8446; misma versión, compatible): contra escucha, manipulación, falsificación. Servidor siempre autenticado, cliente opcional; no oculta la longitud; integridad. Handshake + registro.
- SSL 3.0 (18-XI-1996; RFC 6101, 2011) prohibido, RFC 7568. TLS 1.0 RFC 2246 (I-1999), 1.1 RFC 4346 (IV-2006): retiradas por RFC 8996 (2021), RFC 9846 prohíbe negociarlas. TLS 1.2 RFC 5246 (VIII-2008). «Certificado SSL» = para TLS.
- 1.2 a 1.3: sin algoritmos legacy, todo AEAD; sin RSA ni DH estáticos, secreto hacia delante; cifrado tras ServerHello; 0-RTT (a costa de propiedades de seguridad).

## 3. Navegadores: configuración, privacidad y seguridad
- Favoritos guardan la dirección. Chrome: Configuración > Privacidad y seguridad. Edge: Configuración y más > privacidad, búsqueda y servicios.
- Actualización automática = primera medida. Administrador fija opciones (SmartScreen, DNS seguro).
- Incógnito (Ctrl+Mayús+N): al terminar no guarda historial ni datos de sitios; conserva marcadores y descargas; no anonimiza (sitios, red, proveedor ven); termina al cerrar todas las ventanas; terceros bloqueadas.
- Cookies propias y de terceros (seguimiento). Excepciones por sitio; dominio entero `[*.]`.
- RFC 6265: Expires/Max-Age (prevalece Max-Age; sin ninguno, sesión); Domain (sin él, solo origen); Path (no es seguridad); Secure (solo canal seguro; confidencialidad, no integridad); HttpOnly (oculta a scripts); pueden ir los dos.
- Edge, seguimiento: Básico; Equilibrado (recomendado; bloquea dañinos y de sitios no visitados); Estricto (puede romper sitios).
- DNS seguro Chrome: automático, si falla sin cifrar. DoH (RFC 8484).
- Navegación segura (Chrome): mejorada, estándar (predeterminada), sin protección; mejorada envía URL y muestra a Google. SmartScreen (Edge): suplantación, malware, descargas; no bloquea elementos emergentes. Advertencia ≠ bloqueo. Sin HTTPS: «No es seguro».

## 4. IPv4 e IPv6
- IPv4 (RFC 791, IX-1981): Version 4b; IHL 4b (palabras de 32 b, mín. 5); Type of Service 8b (hoy DS, RFC 2474; ECN, RFC 3168, 2 bits); Total Length 16b (65.535); Identification 16b; Flags 3b (reservado, DF, MF); Fragment Offset 13b (unidades de 8 octetos); TTL 8b (0 = destruir); Protocol 8b; Header Checksum 16b (recalculada por salto); direcciones 32b; Options y Padding.
- Cabecera mín. 5×4 = 20 octetos; IHL 15 = 60.
- IPv6 (RFC 8200, VII-2017, STD 86), fija 40 octetos: Version 4b; Traffic Class 8b; Flow Label 20b; Payload Length 16b (extensiones cuentan); Next Header 8b; Hop Limit 8b; direcciones 128b.
- Extensiones: fragmento = Next Header 44. Fragmenta solo el origen. MTU mínima 1280; Path MTU Discovery. Sin difusión.
- Clases: A 0, 0-127, 8/24; B 10, 128-191, 16/16; C 110, 192-223, 24/8; D 1110, 224-239 multidifusión (RFC 1112); E 1111, 240-255 reservada (RFC 791, 1122).
- Privadas RFC 1918: 10/8; 172.16/12; 192.168/16. Clase ≠ pública. Necesitan NAT.
- RFC 6890, 6598: 0.0.0.0/8; 127/8 bucle; 169.254/16 enlace local (RFC 3927; sin DHCP); 100.64/10 CGN; 192.0.2/24, 198.51.100/24, 203.0.113/24 documentación; 240/4 reservado; 255.255.255.255 difusión limitada.
- CIDR (RFC 4632, RFC 950): /0 a /32; 172.16.0.0/16 = 255.255.0.0. Utilizables = 2^b − 2.
- /8 16.777.214; /16 65.534; /20 255.255.240.0 4.094; /22 255.255.252.0 1.022; /23 255.255.254.0 510; /24 254; /25 .128 126; /26 .192 62; /27 .224 30; /28 .240 14; /29 .248 6; /30 .252 2.
- 192.168.30.150/25: subred .128 a .255 (red .128, difusión .255); .250 sí, .124 no, 192.168.31.150 no.
- 500 equipos: 512 = 9 bits, /23 (255.255.254.0), 510; /21 2.046; /24 254; /25 126; 511 exige /22.
- 192.168.10.0/24 en 4 = /26: .0, .64, .128, .192; 2.ª: utilizable .65, difusión .127.
- IPv6 (RFC 4291): unicast, anycast (la más cercana), multicast; sin broadcast. `::` una vez; ceros a la izquierda omitibles. RFC 5952: `::` al máximo, no para un solo grupo 0, minúsculas.
- 2001:DB8:0:0:8:800:200C:417A = 2001:DB8::8:800:200C:417A; ::FFFF:129.144.52.38.
- ::/128; ::1/128; FF00::/8; FE80::/10 enlace local; FC00::/7 ULA (RFC 4193); 2001:db8::/32 documentación; ::ffff:0:0/96 IPv4-mapped; 64:ff9b::/96 NAT64. Interface ID 64 bits (salvo 000); subred /64.
- SLAAC (RFC 4862). DHCPv6 RFC 9915 (I-2026, sustituye RFC 8415). Vecinos (RFC 4861) sustituye a ARP; ICMPv6 (RFC 4443).
- Transición: pila doble (RFC 4213; RFC 6724 elige; desactivable); túnel configurado (RFC 4213); NAT64 (RFC 6146) + DNS64 (RFC 6147, sintetiza AAAA). NAT y CGN estiran IPv4.
- 6to4 (RFC 3056) 2002::/16, sin túnel explícito, «not intended as a permanent solution». Teredo (RFC 4380) 2001::/32, sobre UDP, tras NAT. DS-Lite (RFC 6333) 192.0.0.0/29, IPv4 en IPv6 hasta CGN.

## 5. Redes de área local
- LAN: decenas o centenares de equipos en sala, edificio o recinto. Ethernet 802.3; Wi-Fi 802.11.
- Ethernet: años 70, 3 Mbit/s; DIX 10 Mbit/s. MAC 48 bits, 24 altos OUI. EtherType 0x0800 IPv4, 0x86DD IPv6, 0x806 ARP; datos 46-1.500 octetos; CRC 32 bits. Sin conexión, no fiable.
- 10BASE-T 10 Mbps 2 pares; 100BASE-TX 100 Mbps 2 pares; 1000BASE-T 1000 Mbps 4 pares, ambos sentidos.
- Malla completa (n(n−1)/2 enlaces, n−1 interfaces); bus (corte = 2 redes); estrella (cae el central; 10BaseT); anillo (un corte cae la red; dobles en MAN); árbol (sin bucles).
- Determinista (testigo: Token Ring 802.5, Token Bus 802.4; sin colisiones). Estocástica: ALOHA, CSMA, CSMA/CD, CSMA/CA.
- CSMA/CD (Ethernet): para al detectar colisión, jam, espera aleatoria creciente; 51,2 µs = trama mínima 64 bytes. CSMA/CA (Wi-Fi): DIFS, ACK tras SIFS, espera aleatoria congelable, RTS/CTS opcional. Testigo: trama = permiso.
- Colisión: lo parte el conmutador (uno por puerto); hub, uno solo. Difusión: lo parte enrutador o VLAN. Control de acceso: 802.1X.
- VLAN: conjunto de puertos; entre VLAN, enrutador. 802.1Q: etiqueta 32 bits, VLAN 12 bits, 0x8100, PCP 3 bits (0-7), 4094 VLAN (0 y 0xFFF reservados), trama +4 octetos. TRUNK: varias VLAN etiquetadas. ACL: qué pasa, por dirección y puerto. Puerto de acceso: VLAN sin etiquetar (oficio).
- IEEE 802 (LMSC): 802.1 Higher Layer LAN Protocols (802.1D, Q, X); 802.3 Ethernet; 802.11 Wireless LAN; 802.15 Wireless Specialty Network (PAN); 802.18 Radio Regulatory TAG; 802.19 Coexistence; 802.24 Vertical Applications TAG.
- Disueltos: 802.2 LLC, 802.4, 802.5, 802.6, 802.16, 802.17, 802.20-802.23; ninguno en hibernación.
- 802.3: z-1998 Gigabit; ab-1999 1000BASE-T; ac-1998 VLAN TAG; ad-2000 Link Aggregation; ae-2002 10 Gb/s; an-2006 10GBASE-T; af-2003 DTE Power via MDI (PoE); at-2009 DTE Power Enhancements; bt-2018 4 pares; bz-2016 2.5G/5GBASE-T; az-2010 Energy-efficient. 100BASE-TX no consta.

## 6. Redes inalámbricas IEEE 802.11
- Enmienda IEEE ≠ nombre Wi-Fi Alliance. ISM 2,400-2,500 GHz desde 1985.
- 2,4 GHz: 14 canales, sin solapamiento 1, 6, 11 (Cisco). 5 y 6 GHz (20 MHz): sin solapamiento. España: no consta.
- Original 2 Mbit/s. a-1999 5 GHz 54. b-1999 2,4 GHz 11. g-2003 2,4 GHz 54. n-2009 High Throughput, Wi-Fi 4 (2009), 2,4 y 5. ac-2013 Very High Throughput, Wi-Fi 5 (2014), <6 GHz. ax-2021 High Efficiency WLAN, Wi-Fi 6 (2018), 6E añade 6 GHz. be-2024 Extremely High Throughput, Wi-Fi 7 (2024), 2,4/5/6.
- 802.11-2024 «Accumulated Maintenance Changes»; i-2004 MAC Security Enhancements; s-2011 Mesh.
- `netsh wlan show drivers` (802.11be / ax); Wi-Fi 7 desde Windows 11 24H2.
- OFDMA (Wi-Fi 6); MU-MIMO (Wi-Fi 6, 4 a 8 flujos); 1024-QAM (6), 4K-QAM +20 % (7); 160 MHz (6), 320 MHz en 6 GHz doble caudal (7); beamforming; TWT; MLO (7, varias bandas). Microsoft: Wi-Fi 7 hasta 4x Wi-Fi 6/6E, casi 6x Wi-Fi 5.
- Ad hoc (sin Internet); infraestructura (mayoría; un AP); malla (802.11s). BSS = grupo de dispositivos. Balizas (SSID hasta 32 caracteres), sondeo, asociación.
- WEP y TKIP inseguros (Windows avisa desde 1903; usar AES con WPA2/WPA3). WPA3: obligatorio para certificados, sin legacy, PMF. WPA3-Personal: SAE contra adivinación. WPA3-Enterprise: PMF + 802.1X + RADIUS; 192 bits solo EAP-TLS. Enhanced Open: cifrado sin autenticación. WPA2/WPA3 mezclados: primero WPA3-Personal.
- 802.1X: bloquea hasta que RADIUS valida; puerto o asociación a AP. Solicitante (equipo), autenticador (conmutador o AP; cliente RADIUS), servidor de autenticación (RADIUS).
- EAP: marco multimétodo sobre enlace sin IP; EAPOL; EAPOL-Start. EAP-TLS: certificados, mutua, mayor seguridad. PEAP: EAP en túnel TLS. EAP-MSCHAP v2: interno en cable e inalámbrico (independiente solo en VPN).
- RADIUS puerto 1812 (RFC 2865). NPS = RADIUS de Microsoft; credenciales de AD DS; «Servidor RADIUS para conexiones 802.1X inalámbricas o por cable».
- Juniper: single supplicant (solo el primero), single-secure (un equipo), multiple (cada uno). Empresa = 802.1X; personal = clave compartida.

## 7. Aplicación práctica
- IP, máscara, puerta, DNS: sin IP no habla; máscara mal, habla con quien no debe; sin puerta no sale; sin DNS no encuentra nombres.
- Capa (oficio): cable = física; VLAN o 802.1X = enlace; IP/máscara = red; cortafuegos = transporte; certificado o 403 = aplicación.
- `ping` ICMP eco (IP sí, nombre no = resolución); `tracert` TTL 1 creciente, 30 saltos, `*`, falla el salto tras el último que contesta; `netstat` conexiones abiertas.
- 169.254.12.7 sin puerta = sin DHCP: `ipconfig /release` `/renew` (`/release6` `/renew6`), cable, servidor, VLAN. `ping 8.8.8.8` sí y nombres no = DNS, `/flushdns`. 60 equipos: /26, 255.255.255.192. 2001:0db8:0000:0000:0000:ff00:0042:8329 = 2001:db8::ff00:42:8329. IHL 6 = 24 octetos. WLAN con AD: WPA3-Enterprise, 802.1X, NPS, EAP-TLS o PEAP, invitados en otra VLAN; nunca WEP ni TKIP. VLAN 10 y 20: enrutador o capa 3. Wi-Fi 7: `netsh` y 24H2.

## Lo que el tema no da
- Texto IEEE e ISO, SIFS/DIFS, velocidades Wi-Fi, canales en España, 100BASE-TX, repetidor, % IPv6, Firefox, red de RTVA/CSRTV. Cableado: tema 4; Windows: 6; AD: 8; certificados, VPN: 14.
