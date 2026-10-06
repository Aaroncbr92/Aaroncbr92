# Puesto 29 · Tema 13 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en sus volcados de
`fuentes/canal-sur/informatico/web/` (`r-*.txt`, descargados el 05-10-2026). No se descargó nada.
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/13-redes-internet-y-comunicaciones.md`
(1.389 líneas, unas 16.600 palabras). No se ha corregido nada: sólo se refuta.

## Alcance

- Exactitud: todo salvo lo «Copiado de RTVE sin cambios» (tabla de `29-T13-redaccion.md`). «Copiado
  del común»: nada. Lo adaptado de RTVE sí se miró.
- Cobertura: el tema entero contra el enunciado del punto 13 (BOJA núm. 186, Anexo V, 2.29).
- Lentes automáticas: tema técnico sin norma jurídica; `refutar_prosa.py` e `indice.py` ya dieron
  0 en la verificación y el tema no ha cambiado desde entonces. No se repitieron.

## Lente 1 · Exactitud

Contrastado en la fuente (muestra amplia, centrada en lo que la verificación no listaba como
releído): reparto IANA-RIR-LIR/ISP (RFC 4632, líneas 302-312); cronología ISOC (cuatro reglas de
Kahn, NCP en diciembre de 1970, *flag day* de 1-I-1983, NSFNET y TCP/IP obligatorio en 1985, baja de
ARPANET en 1990, FNC de 24-X-1995); RIPE NCC (direcciones recuperadas y lista de espera); RFC 9846
(sustituye al 8446 sin cambiar de versión, prohíbe negociar TLS 1.0 y 1.1, requisitos nuevos para
TLS 1.2) y el índice de RFC (9846 de julio de 2026, 9915 de enero de 2026); HTTP/1.1 de 1995/1997
(RFC 9110); DNS seguro de Chrome en modo automático y rutas de menú de Chrome y Edge; bloques de RFC
6890 (6to4 2002::/16, TEREDO 2001::/32, DS-Lite 192.0.0.0/29); Bonaventure (Ethernet en PARC a 3
Mbit/s y DIX a 10, ranura de 51,2 µs y trama mínima, estrella 10BaseT, árbol con concentradores,
anillo doble en redes metropolitanas, familias pesimista y optimista, SIFS/DIFS y temporizador que se
congela, RTS/CTS, cabecera 802.1Q con 0x8100, PCP, VID 0 «no pertenece a ninguna VLAN», 0xFFF
reservado, 4094 VLAN y +4 octetos, tabla de 802.11 a 802.11n); página de grupos disueltos del IEEE 802
(ninguno en hibernación; 802.2, 802.4, 802.5, 802.6, 802.16…); Wi-Fi Alliance (Wi-Fi 4 2009, 5 2014,
6 2018, 7 2024, HaLow 2017, WiGig 60 GHz; OFDMA, 160 MHz, TWT, 1024 QAM, *beamforming*, 4K QAM, 320
MHz); Microsoft (cuatro a ocho flujos y 1024-QAM en Wi-Fi 6, 6E en 6 GHz, `netsh wlan show drivers`,
24H2, WPA3-Personal primero, 192 bits y EAP-TLS como único método).

Todo cuadra. Hallazgos:

| # | Tipo | Gravedad | Dónde | Qué pasa | Propuesta |
|---|---|---|---|---|---|
| E1 | 9 (atribución) | Menor | Trazabilidad, fila «RFC 9110 (HTTP), RFC 9000…, RFC 768 (UDP)» | La columna «Qué sostiene» sólo habla de HTTP («Sin estado, métodos, códigos de estado, versiones, puertos 80 y 443, esquema https»), pero la fila incluye UDP (RFC 768), DNS (1034), DHCP (2131), cookies (6265), HSTS (6797), DoH (8484) y QUIC (9000), que sostienen otras cosas | Completar la columna: «…; QUIC, HSTS, cookies, DoH, objeto de DNS y DHCP, UDP sin entrega garantizada» |

Graves: ninguno. Cero hallazgos graves es un buen resultado: la verificación (30 correcciones) dejó
el tema limpio.

Nota sin hallazgo: Microsoft da además, de Wi-Fi 7, «up to 4x faster speeds than Wi-Fi 6 and Wi-Fi
6E, and close to 6x faster than Wi-Fi 5» (`r-ms-wifi.txt`, línea 59). El tema dice que las fuentes
«sólo dan comparaciones (el doble, un 20 % más)»; sigue siendo cierto, pero el remate puede añadir
esta comparación si quiere.

## Lente 2 · Cobertura

Cada rúbrica del enunciado tiene su epígrafe, en orden: arquitectura, origen, evolución, estado
actual y servicios (§ 1); HTTP, HTTPS y TLS (§ 2); navegadores (§ 3); IPv4 e IPv6, cabeceras,
direccionamiento, subredes, convivencia y transición (§ 4); LAN, conceptos, topologías, control de
acceso, segmentación, IEEE 802 (§ 5); 802.11, estándares, técnicas, dispositivos, topologías,
seguridad y 802.1X (§ 6); aplicación práctica (§ 7). Ninguna rúbrica falta.

Quince preguntas en `29-T13-preguntas.md`: **9 enteras, 1 a medias, 5 no**.

Lagunas (laguna = se amplía el tema; fuente ya en disco salvo donde se dice):

| # | Pregunta | Rúbrica | Qué falta | Fuente para ampliar |
|---|---|---|---|---|
| L1 | 3 (no) | Principales servicios | Intercambio DHCP (DHCPDISCOVER, OFFER, REQUEST, ACK; también NAK, RELEASE) y puertos 67/68 | `r-rfc2131.txt` (línea 747 y ss.; puerto 67 en 1245) |
| L2 | 6 (no) | Seguridad y privacidad de navegadores | Atributos de cookie Secure, HttpOnly (y Expires/Max-Age, Domain, Path) | `r-rfc6265.txt` (SameSite no está en el RFC 6265: no darlo sin otra fuente) |
| L3 | 10 (a medias) | Convivencia y transición | Qué hace cada uno de 6to4, Teredo y DS-Lite (una línea cada uno) | No en disco: RFC 3056, 4380 y 6333 (rfc-editor.org). Si no se leen, se queda como está |
| L4 | 11 (no) | Normalizaciones IEEE 802 | Enmiendas de 802.3 de uso diario: 802.3u (100BASE-TX), 802.3ab (1000BASE-T), 802.3z, PoE 802.3af/at/bt | No en disco (`r-ieee8023.txt` no las nombra). Necesita fuente IEEE o manual; si no, declararlo en «Lo que este tema no da» |
| L5 | 13 (no) | Estándares 802.11 | Canales de 2,4 GHz sin solapamiento | Ya declarado como no dado (falta el CNAF). Se mantiene la laguna; para cerrarla, leer el CNAF vigente |
| L6 | 14 (no) | Seguridad 802.11 | SAE como autenticación de WPA3-Personal | `r-ms-wificx7.txt`, línea 18: **«enhanced capabilities for WPA3-SAE authentication and Opportunistic Wireless Encryption (OWE)»** y línea 34 (`DOT11_AUTH_ALGO_WPA3_SAE`). Permite decir «WPA3 usa autenticación SAE (Microsoft)»; la unión con WPA3-Personal en concreto sigue sin fuente, así que redactarlo con esa cautela. Enhanced Open = OWE tampoco se une explícitamente |

Observación de cobertura sin pregunta: en «dispositivos de interconexión» inalámbricos el tema da el
punto de acceso, el conmutador, el enrutador y el PoE, pero no el repetidor o extensor ni el
controlador de red inalámbrica. No hay fuente en disco; basta declararlo en «Lo que este tema no da».

## Otros ficheros tocados

Sólo este informe y `29-T13-preguntas.md`. El tema no se ha modificado.
