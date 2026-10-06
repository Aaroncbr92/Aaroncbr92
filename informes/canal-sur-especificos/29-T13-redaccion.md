# Puesto 29 · Tema 13 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real,
como en la investigación y en los temas 5 a 12). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/13-redes-internet-y-comunicaciones.md`.
Material: `29-investigacion-C-datos-redes-seguridad.md` (§ Tema 13). `AGRUPACION.tsv`: tema 13
«nuevo». Fila de `informes/canal-sur-reuso/informatica.tsv`: RTVE `tecnica-informatica/02`, `/03`,
`/04`, `/05`, `gestion-administrativa/10` y `tese/12`, 45 %, «actualizar: no».

## Avance

- Fuentes descargadas como texto, prefijo `r-` en `fuentes/canal-sur/informatico/web/`.
- Ficha, enunciado, «qué se puede preguntar» y epígrafe 1 (definición del FNC, arquitectura abierta, capas, reparto de direcciones y sistemas autónomos, origen, evolución y estado actual, servicios) guardados. Literalidad: 38 citas, todas halladas.
- Epígrafes 2 (HTTP: petición y respuesta, sin estado, métodos seguros e idempotentes, clases de código de estado, versiones, QUIC; HTTPS y HSTS; TLS: propiedades, componentes, versiones de SSL a TLS 1.3 y RFC 9846, cambios de 1.2 a 1.3) y 3 (navegadores: configuración, opciones fijadas por el administrador, navegación privada, cookies, prevención de seguimiento de Edge, DNS seguro, Navegación segura, SmartScreen, conexiones seguras) guardados. Literalidad: 126 citas acumuladas, todas halladas. Quitado «InPrivate» (la página de Edge leída no lo nombra).
- Epígrafe 4 (cabeceras IPv4 e IPv6 con tabla comparada, clases, privadas, bloques especiales, difusión, CIDR y cálculo de subredes, direccionamiento IPv6, SLAAC/DHCPv6/ND, pila doble, túneles, NAT64/DNS64, ipconfig) guardado. Primera pasada: 3 citas fallaban por guiones de fin de línea de los RFC (upper-layer, Carrier-Grade) y una mayúscula; recortadas. Literalidad: 205 citas acumuladas, todas halladas.
- Epígrafe 5 (LAN y Ethernet, MAC frente a IP, pares de 1000BASE-T, topologías, control de acceso al medio, dominios de colisión y difusión, conmutador, STP, VLAN 802.1Q, normas IEEE 802 activas y disueltas) guardado. Primera pasada: 7 rótulos en negrita que no eran cita, pasados a cursiva; quitada una cita con fórmula LaTeX del manual. Literalidad: 258 citas acumuladas, todas halladas.
- Epígrafe 6 (estándares 802.11 con títulos IEEE y nombres Wi-Fi, 802.11-2024 y 802.11be-2024, técnicas de transmisión, dispositivos de interconexión, topologías, seguridad WEP/TKIP/WPA2/WPA3/PMF/Enhanced Open, 802.1X con EAP, métodos, RADIUS, NPS y modos de solicitante) y 7 (aplicación práctica: cuatro datos y orden de la avería, herramientas, nueve supuestos) guardados. Tres rótulos en negrita pasados a cursiva. Literalidad: 340 citas, todas halladas.
- Siglas, «Lo que este tema no da» y «Trazabilidad» guardados. `refutar_prosa.py`: 11 siglas sin presentar en la primera pasada (métodos HTTP, OK, NSF, RAN, TX, WPA, ISATAP), presentadas o quitadas; segunda pasada, 0 hallazgos. Índice generado con `indice.py` (43 epígrafes, 16.040 palabras; ficha escrita a mano: el tema no está en `portadas.tsv`). Tema técnico sin norma jurídica: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Fuentes leídas y fecha

Todas el 05-10-2026, descargadas como texto con URL y fecha en cabecera en
`fuentes/canal-sur/informatico/web/` (nuevas, prefijo `r-`):

- RFC (texto de rfc-editor.org): 768, 791, 826, 950, 1034, 1112, 1122, 1918, 2131, 2474, 2818, 2865,
  3022, 3168, 3748, 3927, 4193, 4213, 4291, 4443, 4632, 4861, 4862, 5737, 5771, 5952, 6101, 6146,
  6147, 6265, 6598, 6724, 6797, 6890, 7230, 7568, 8200, 8446, 8484, 8996, 9000, 9110, 9113, 9114,
  9293, 9846, 9915 (`r-rfcNNNN.txt`), y un extracto del índice de RFC (`r-rfc-index-extracto.txt`)
  con la situación de cada uno. No se usan en el tema, aunque se descargaron: 826 (ARP), 2818, 5737,
  5771, 7230, 9113, 9293. El 8446 sólo se cita como antecesor del 9846.
- Internet Society, *Brief History of the Internet* (`r-isoc-history`); ICANN, comunicado de
  03-02-2011 (`r-icann-ipv4.pdf` y `.txt`, pasado con `documento.py`); RIPE NCC (`r-ripe-ipv4`); UIT,
  comunicado de 17-11-2025 (`r-itu-pr2025`); CERN (`r-cern-info`, `r-cern-project`).
- Google Chrome, ayuda en castellano (`r-chr-incog`, `r-chr-safe`, `r-chr-secure` en su versión de
  ordenador, `r-chr-cookies`); Microsoft Edge (`r-edge-track`, `r-edge-smartscreen`).
- IEEE 802 (`r-ieee802`, `r-ieee802-dormant`, `r-ieee8023`), IEEE 802.11 *Timelines* de 19-09-2026
  (`r-80211time`, la página viene en UTF-16 y se convirtió).
- Bonaventure, CNP3 (`r-cnp3-sharing`, `r-cnp3-lan`, `r-cnp3-principles-referencemodels`,
  `r-cnp3-preface` para la licencia; descargados y no usados: `r-cnp3-principles-network`,
  `-reliability`, `r-cnp3-protocols-ipv6`, `-http`, `-tls`, `r-cnp3-index`).
- Wi-Fi Alliance (`r-wfa-wifi7`, `r-wfa-security`; `r-wfa-wifi6` es la misma página); Microsoft
  (`r-ms-wifi`, `r-ms-wificx7`, `r-ms-deprecated`, `r-ms-eap`, `r-ms-nps`); Juniper Networks
  (`r-juniper-8021x`).
- Ya existentes y reutilizados: `w11-ipconfig`, `w11-ping`, `w11-tracert` (tema 6).

Descargas fallidas, borradas: Cisco 802.1X (403 de Akamai; la investigación la daba como [WF]),
IEEE 802.1 (bloqueo de Cloudflare), Mozilla (desafío de navegador, cuatro páginas), CERN *birth of
the web* (404), página de 802.1X cableado de Microsoft (404), *Facts and Figures* de la UIT (página
dinámica, sustituida por el comunicado), hoja de bandas del IEEE 802 (418).

Comprobación de literalidad por script (`scratchpad/t13check.py`: busca cada negrita en todas las
fuentes de `informatico/web/`, quitando de los RFC las cabeceras y pies de página, las barras de
tabla y los saltos de línea; tolera sólo la mayúscula o minúscula inicial): 340 citas en negrita, 0 no
halladas.

## Qué se hizo

Siete epígrafes en el orden del enunciado: 1 Internet (definición del FNC, arquitectura abierta y
reglas de Kahn, capas TCP/IP y OSI, reparto IANA-RIR-LIR y sistemas autónomos, origen 1962-1995,
evolución y estado actual, servicios con puertos, DNS, DHCP, NAT, URL y cookies); 2 HTTP, HTTPS y TLS;
3 navegadores (configuración, privacidad, seguridad); 4 IPv4 e IPv6 (cabeceras, direccionamiento,
bloques especiales, subredes y CIDR, IPv6, transición); 5 LAN (conceptos, topologías, control de
acceso al medio, segmentación, normas IEEE 802); 6 Wi-Fi (estándares, técnicas, dispositivos,
topologías, seguridad, 802.1X); 7 aplicación práctica.

Decisiones y salvedades (manda la fuente):

- **TLS 1.3: el RFC 8446 ya no es la referencia.** El índice de RFC lo da como sustituido por el **RFC
  9846 (julio de 2026)**, que se leyó y es el que se cita (misma versión 1.3; prohíbe negociar TLS 1.0
  y 1.1). La investigación no lo detectó. Igual con DHCPv6: el RFC 8415 está sustituido por el **RFC
  9915 (enero de 2026)**.
- **802.11be-2024 frente a 802.11-2024**: la investigación lo dejó sin comprobar. La tabla de proyectos
  del grupo 802.11 (19-09-2026) lista la be-2024 como enmienda (tipo «A») con la 802.11-2024 entre sus
  bases: no está integrada en la revisión. Se dice así.
- **WPA3-Enterprise y 802.1X**: la investigación no tenía cita literal. La página de Microsoft
  *Faster and more secure Wi-Fi in Windows* la da (**«…using Protected Management Frames on all WPA3
  connections with 802.1X for user authentication with a RADIUS server»**). Se usa.
- **802.1X**: las citas de Cisco de la investigación eran [WF] y la página devuelve 403; no se usan. Se
  sustituyen por Juniper Networks (solicitante, autenticador, servidor; modos de solicitante),
  Microsoft (EAP, métodos, NPS) y los RFC 3748 y 2865. El EtherType 0x888E de EAPOL no se da (no consta
  en lo leído).
- **Topologías y control de acceso al medio**: la investigación no tenía fuente; se leyó el manual de
  Bonaventure (licencia CC BY), que cubre malla, bus, estrella, anillo, árbol, CSMA, CSMA/CD, CSMA/CA y
  testigo, y la historia de los grupos 802.3, 802.4 y 802.5.
- **Modelo TCP/IP**: RTVE asignaba al nivel de aplicación de TCP/IP las capas OSI 7, 6 y 5. El RFC 1122
  dice que **«essentially combines the functions of the top two layers -- Presentation and Application
  -- of the OSI reference model»**. Se da la tabla habitual (que es la de Bonaventure) con la salvedad
  del RFC 1122 escrita en el tema.
- **IPv6 «ocho grupos de cuatro cifras»** (RTVE, en `tecnica-informatica/02` y `tese/12`): no cuadra
  con el RFC 4291 (**«one to four hexadecimal digits»**). No se copia; el tema da la regla del RFC.
- **Clases de IPv4**: RTVE daba la A como «1 a 126». El tema deduce los rangos de los bits del RFC 791
  (0 a 127) y explica que 0 y 127 están reservados (RFC 6890).
- **Bandas Wi-Fi**: RTVE daba 802.11ac en 5 GHz y los canales 1, 6 y 11. El título IEEE de la ac es
  **«Very High Throughput < 6 GHz»** y la Wi-Fi Alliance dice que la mayoría de productos Wi-Fi 5 son
  de doble banda; se da así. Los canales no se dan (no hay fuente leída del reparto en España).
- **Historia de SSL**: RTVE daba «SSL, 1994, Netscape» y «SSL 3.0, 1995» como aproximados. El tema da
  sólo lo leído: la versión de SSL 3.0 de 18-11-1996 (RFC 6101) y las fechas de los RFC de TLS.
- Firefox no se trata: Mozilla bloquea la descarga.
- Velocidades máximas de Wi-Fi 6 y 7, uso de IPv6 en porcentaje, 6 GHz en España y relación Wi-Fi 8 ↔
  802.11bn: no se afirman (declarados en «Lo que este tema no da»).

## Copiado del común

Nada. Ningún tema cerrado del común de Canal Sur trata redes (son todos jurídicos). El único tema
cerrado de Canal Sur con redes, `28-operador-a-de-sonido/15`, trata audio sobre IP (Dante, AES67, ST
2110) y no tiene ningún epígrafe aprovechable sin cambios para este enunciado.

## Copiado de RTVE sin cambios

Los seis temas de RTVE están marcados «actualizar: no» en `informatica.tsv`. Pasajes técnicos copiados
literal, sin tocar una palabra; sólo se ha quitado la negrita de énfasis de RTVE (aquí negrita es
cita) y las marcas ✔ de respuesta oficial. Comprobados por script contra los ficheros de RTVE: todos
literales. El verificador sólo tiene que comprobar que siguen siéndolo.

| Pasaje de RTVE | Dónde va en el tema 13 |
|---|---|
| `gestion-administrativa/10` § 1: «Internet es la red de redes: … o la voz sobre IP.» | § 1, Qué es Internet, segundo párrafo |
| `tecnica-informatica/02` § 1: «La regla que sitúa cualquier protocolo sin memorizarlo: … es aplicación.» y la tabla Protocolo / Capa OSI | § 1, Las capas |
| `tese/12` § 3: tabla TCP frente a UDP, **sin su última fila** («Para qué se usa aquí», propia de una instalación de televisión); las cinco filas que quedan, literales | § 1, Las capas |
| `tecnica-informatica/03` § 2: «Qué es un sistema autónomo: … asigna la IANA.» y la tabla Familia / Dónde actúa / Protocolos | § 1, Quién reparte las direcciones |
| `tecnica-informatica/04` § 4: tabla de servicios, protocolos y puertos, y el párrafo «El patrón que ordena toda la columna de la derecha: … por el puerto 22.» | § 1, Los principales servicios |
| `tecnica-informatica/03` § 4: «Los tipos de registro que conviene tener vistos:», la tabla Tipo / Qué resuelve y «Pasado ese plazo, … el tiempo de vida.» | § 1, Los principales servicios (DNS) |
| `tecnica-informatica/04` § 3: «HTTPS no es un protocolo distinto de HTTP: … túnel cifrado.»; «Lo que ese túnel aporta … no confundirlas:», la tabla de tres filas, «Lo que NO aporta … millones lo tienen.» y «Cómo funciona el certificado, en tres líneas: … todo va cifrado.» | § 2, HTTPS |
| `tecnica-informatica/04` § 2: «El aviso de nomenclatura, … no debe usarse.» | § 2, Las versiones |
| `gestion-administrativa/10` § 5: las cinco primeras viñetas (barra de direcciones, pestañas, historial, favoritos, descargas) y su frase de entrada | § 3, Configuración básica |
| `tese/12` § 2: «La cuenta: con *b* bits … son 254.», la tabla de cuatro máscaras con su veredicto y «Y el detalle que a veces despista: … subir a `/22`.» | § 4, Las subredes |
| `tecnica-informatica/05` § 2: tabla Variante / Velocidad / pares y la frase «El aviso práctico que se deriva: … no funciona a mil.» | § 5, Conceptos |
| `tecnica-informatica/02` § 4: tabla MAC / IP y «La razón de fondo, … mandar el paquete.» | § 5, Conceptos |
| `tecnica-informatica/03` § 3: tabla De colisión / De difusión; «Qué añade la VLAN: … edificios distintos.» | § 5, Segmentación |
| `tese/12` § 6: filas VLAN, TRUNK y ACL de la tabla (sin la fila KVM sobre IP) | § 5, Segmentación |
| `tecnica-informatica/05` § 3: tabla de equipos por capa y «Qué es exactamente una puerta de enlace, … capa de aplicación.» (los dos sentidos) | § 6, Dispositivos |
| `tese/12` § 5: «La cuenta que hay que hacer al instalar: … no puede pasarlo.» | § 6, Dispositivos |
| `gestion-administrativa/10` § 2: «Qué hace cada mitad del aparato: … traducción de direcciones.» | § 6, Dispositivos |
| `tecnica-informatica/02` § 5: «Lo que conviene llevar visto son los cuatro datos …», la tabla Dato / Qué decide y «Y la comprobación de averías … no funciona.» | § 7, Los cuatro datos |
| `tese/12` § 5: tabla de `ipconfig`, `ping`, `tracert` y `netstat`, y «El `ping` contesta … en el salto siguiente.» | § 7, Herramientas |

**Adaptado de RTVE (sí pasa la verificación entera)**:

| Pasaje de RTVE | Dónde va | Cambio |
|---|---|---|
| `tecnica-informatica/03` § 2, métrica | § 1 | Reescrito en una frase |
| `tecnica-informatica/03` § 4, tiempo de vida | § 1, DNS | Dos frases unidas en una |
| `gestion-administrativa/10` § 3, URL | § 1 | Ejemplo `www.rtve.es` → `www.canalsur.es`; en prosa |
| `gestion-administrativa/10` § 5, navegación privada | § 3 | «Navegación privada, que…» → «La navegación privada (en Chrome, el modo Incógnito) no guarda…» |
| `gestion-administrativa/10` § 7, «HTTPS y el candado» | § 3 | Sujeto en singular («el candado indica… No garantiza…») |
| `tecnica-informatica/02` § 2, «El aviso que hace útil el ejercicio» | § 4 | Cortada la cola «, y la pregunta pide las dos a la vez» |
| `tese/12` § 2, método de la pregunta 11 | § 4, Las subredes | Pasos 1 a 3 sin «que usan las opciones»; paso 4 nuevo, sin las opciones del examen |
| `tecnica-informatica/03` § 3, «Y el dato histórico…» | § 5 | Cortada la cola «, y por eso hoy la colisión sólo aparece en los exámenes» |
| `tese/12` § 6, cabecera de la tabla | § 5 | «Asunto del enunciado» → «Término» |
| `tese/12` § 5, PoE | § 6 | Cortado a partir de «lo que quita una toma…»; añadida la frase de entrada |

Quitado por propio de RTVE: todos los números de pregunta y «Ésa es la respuesta oficial», las
tablas «Los datos que el examen ha preguntado», los avisos de estudio, las referencias a la Técnica de
Equipos, a los temas 9 y 12 de RTVE y a la instalación de televisión (plató, sala de realización,
códec, flujos de vídeo, intercomunicadores), la fila KVM sobre IP, el cuadernillo `23_preguntas_gea`, las
explicaciones de las opciones falsas y la Trazabilidad de RTVE.

## Otros ficheros tocados

- `fuentes/canal-sur/informatico/web/r-*` (nuevos). Ningún fichero existente modificado.
- Ningún otro tema ni informe.

## Diez preguntas tipo test (comprobación de cobertura)

Repartidas por las rúbricas del enunciado; (AP) = aplicación práctica. Todas se contestan enteras
con el tema; no ha hecho falta ampliarlo después de escribirlas.

1. (Arquitectura, origen) ARPANET sustituyó NCP por TCP/IP: a) en septiembre de 1969; b) el 1 de enero
   de 1983, de golpe para todos los equipos; c) en 1990, al darse de baja; d) en abril de 1995. → **b**.
   § 1, El origen. Entera.
2. (Evolución, estado actual y servicios) ¿Cuál es correcta? a) La IANA agotó su reserva de IPv4 en
   2019; b) el RIPE NCC agotó la suya el 25-11-2019 y la IANA el 3-2-2011; c) IMAP cifrado usa el 995;
   d) SMTP para el envío del cliente usa el 110. → **b** (IMAP cifrado es el 993; el envío del cliente,
   587). § 1. Entera.
3. (HTTP) De estos métodos, el que no es seguro ni idempotente es: a) GET; b) PUT; c) DELETE; d) POST.
   → **d**; y un 403 es petición entendida pero denegada, frente al 401, falta de credenciales. § 2.
   Entera.
4. (HTTPS y TLS) Según el RFC 8996 y el RFC 9846: a) TLS 1.2 está prohibido; b) se prohíbe negociar
   TLS 1.0 y 1.1; c) SSL 3.0 sigue permitido para compatibilidad; d) TLS 1.3 cifra sólo el
   ServerHello. → **b** (SSL 3.0, prohibido por el RFC 7568; en TLS 1.3 se cifra todo lo que va tras el
   ServerHello). § 2. Entera.
5. (Navegadores) En el modo Incógnito de Chrome: a) el proveedor de acceso no ve la actividad; b) se
   borran los marcadores y las descargas al cerrar; c) se conservan marcadores y descargas, y las
   cookies de terceros están bloqueadas por defecto; d) la sesión termina al cerrar una ventana. → **c**.
   § 3. Entera.
6. (Cabeceras) ¿Cuál es correcta? a) La cabecera IPv6 lleva suma de comprobación; b) en IPv6 sólo
   fragmenta el origen y la cabecera fija mide 40 octetos; c) la cabecera IPv4 mide siempre 20
   octetos; d) el Hop Limit de IPv6 se incrementa en cada salto. → **b** (IPv4: de 20 a 60). § 4.
   Entera.
7. (Direccionamiento IPv6, convivencia y transición) Un cliente sólo IPv6 que debe llegar a un
   servidor sólo IPv4 usa: a) pila doble en el cliente; b) NAT64 con DNS64, que sintetiza registros
   AAAA a partir de los A; c) un túnel IPv4 sobre IPv6; d) direcciones FE80::/10. → **b**. Y la forma
   correcta de 2001:db8:0:0:0:0:2:1 es 2001:db8::2:1. § 4. Entera.
8. (Subredes, AP) Para 60 equipos con el mínimo desperdicio: a) /24; b) /25; c) /26, 255.255.255.192;
   d) /27. → **c** (62 utilizables; /27 da 30). § 4 y § 7, supuesto 3. Entera.
9. (LAN: topologías, control de acceso, segmentación, IEEE 802) ¿Cuál es correcta? a) Ethernet usa
   CSMA/CA; b) la etiqueta IEEE 802.1Q tiene un identificador de VLAN de 12 bits y permite 4094 VLAN;
   c) en estrella, si cae el nodo central sólo se pierde un equipo; d) el grupo 802.5 normaliza
   Ethernet. → **b** (Ethernet, CSMA/CD; 802.5, Token Ring). § 5. Entera.
10. (802.11: estándares, seguridad y 802.1X) ¿Cuál es correcta? a) Wi-Fi 6 es IEEE 802.11be; b) en
    802.1X el conmutador o el punto de acceso es el solicitante; c) WPA3-Enterprise exige tramas de
    gestión protegidas y 802.1X con servidor RADIUS (puerto 1812); d) las redes WPA3 admiten WEP por
    compatibilidad. → **c** (Wi-Fi 6 es 802.11ax; el conmutador o punto de acceso es el autenticador).
    § 6. Entera.
