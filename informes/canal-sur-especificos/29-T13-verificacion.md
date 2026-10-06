# Puesto 29 · Tema 13 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en sus volcados de
`fuentes/canal-sur/informatico/web/` (`r-*.txt`, `w11-ipconfig`, `w11-ping`, `w11-tracert`,
descargados el 05-10-2026 con URL y fecha en cabecera) y, para los puertos de LDAP y SNMP,
`ws-ports.txt` (Microsoft, *Información general sobre servicios y requisitos de puertos de red*,
descargado el 05-10-2026 para el tema 8). No se descargó nada nuevo.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/13-redes-internet-y-comunicaciones.md`.
Copia previa: `scratchpad/29t13-antes-verif.md`; diff: `scratchpad/29t13-verif.diff`.

## Método

- Copiado del común: nada (según `29-T13-redaccion.md`).
- Copiado de RTVE sin cambios: sólo se comprobó que es literal, por script contra los seis temas de
  RTVE sin negritas ni ✔ (`scratchpad/29t13-rtve.py` por filas de tabla y `29t13-rtve2.py` por
  pasaje, de su frase de arranque a su frase final): los 22 pasajes de la tabla del informe de
  redacción y todas las filas de tabla listadas (capas, TCP/UDP, encaminamiento, servicios y puertos,
  registros DNS, HTTPS, máscaras, pares de Ethernet, MAC/IP, dominios, VLAN/TRUNK/ACL, equipos por
  capa, cuatro datos, comandos). Todo literal. No se ha re-verificado.
- Adaptado de RTVE (sí verificado): métrica, tiempo de vida DNS, URL, navegación privada, candado,
  clases y «192.0.2», método de subred, dato histórico de la colisión, cabecera «Término», PoE.
- Todo lo demás: cada una de las 340 negritas se buscó **en la fuente a la que el tema la atribuye**
  (`scratchpad/29t13-where.py` dice en qué fichero aparece cada una) y se leyó su contexto para lo
  dicho en redonda y las salvedades, con los nueve errores delante. También las cifras y fechas en
  redonda (cronología ISOC, fechas del índice de RFC, tabla 802.11, bandas, puertos, 802.1Q).
- Lentes (tema técnico sin norma): `refutar_prosa.py` dio 1 hallazgo tras las correcciones (PC sin
  presentar, en una cita de Microsoft), corregido: 0. `indice.py`: 43 epígrafes, índice sin cambios.
  No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`. Literalidad final: 341
  citas, 0 no halladas.

## Hallazgos y correcciones (todas aplicadas, cada una comprobada en su fuente)

| # | Error | Dónde | Qué pasaba | Corrección |
|---|---|---|---|---|
| 1 | 9 | § 1, FNC | «definición que sigue siendo la más citada»: ninguna fuente lo dice | Quitado |
| 2 | 9 | § 1, capas | OSI «de la ISO»: Bonaventure lo da como definido en X.200 y como **base** de la normalización en la ISO | Dicho así |
| 3 | 9 | § 1, 1995 | «la troncal pasa a redes privadas»: ISOC dice que los fondos van a las redes regionales para comprar conectividad a redes privadas de larga distancia | Dicho así |
| 4 | 9 | § 1, CERN | «Su primera página la presentaba así»: lo leído es la página del proyecto (`TheProject.html`) en info.cern.ch; nada dice que sea la primera | «La página del proyecto que conserva ese servidor» |
| 5 | 7 | § 1, RIPE NCC | «desde entonces sólo reparte»: noticia de 2019, archivada y sin actualizar | «anunció que en adelante sólo repartiría» |
| 6 | 9 | § 1, puertos LDAP y SNMP | 389/636 y 161/162 dados como oficio, sin fuente | Confirmados en la tabla de puertos de Microsoft (`ws-ports`): «LDAP SSL» 636, SNMP UDP 161, capturas 162. Citada la fuente; sacados de la lista de oficio y añadidos a Trazabilidad |
| 7 | 9 | § 1, DHCP | Dirección, máscara, puerta y DNS: el RFC 2131 leído no los enumera (las opciones están en el 2132, no leído) | Marcado «(oficio)» |
| 8 | 8 artículo mal | § 2, métodos | «RFC 9110 (sección 9.3)»: la tabla de métodos con sus descripciones es la tabla 4 de la sección 9.1 | «tabla 4 de la sección 9.1; cada uno se desarrolla en la 9.3» |
| 9 | 9 | § 2, versiones | HTTP/1.0 con «mensajes con cabeceras»: el RFC dice peticiones y respuestas dentro de mensajes | Corregido |
| 10 | 6 salvedad | § 2, HSTS | Cita cortada antes de «and/or by other means, such as user agent configuration»; y «ya no intenta» sin plazo (la directiva `max-age` lo fija) | Añadidas las dos cosas |
| 11 | 6 | § 2, SSL 3.0 | «never formally published by the IETF» sin «except in several expired Internet-Drafts» | Añadido |
| 12 | 9 | § 3, directivas de grupo | Que las opciones del navegador se repartan por GPO: no lo dice ninguna página leída | Marcado «(oficio)» |
| 13 | 9 | § 3, navegación privada (adaptado de RTVE) | «no guarda… datos de formularios»: la ayuda de Chrome no lo dice; habla de historial y datos de sitios al terminar la sesión | Reescrito con lo de Chrome; sacado de la lista de oficio |
| 14 | 9 | § 3, Incógnito | Cookies temporales «que se borran al cerrar»: Chrome dice al finalizar la sesión (cerrar todas las ventanas) | «al terminar la sesión» |
| 15 | 9 | § 4, IPv6 | «la cifra [40] no aparece escrita en lo leído del RFC»: el RFC 8200 dice que la cabecera mínima es **«20 octets longer than a minimum-length IPv4 header»** | Añadida esa cita, que confirma el cálculo |
| 16 | 9 | § 5, CSMA/CA | «Una radio no puede escuchar mientras emite»: Bonaventure no lo dice; dice que evita colisiones ajustando los temporizadores | Corregido |
| 17 | 9 | § 5, 802.1Q | «el 0 y el 0xFFF están reservados»: el 0 indica que la trama no es de ninguna VLAN; sólo el 0xFFF está reservado. «La trama crece 4 octetos»: es el tamaño máximo | Corregido |
| 18 | 9 | § 5, subred por VLAN | Sin fuente | Marcado «(oficio)» |
| 19 | 9 | § 5, tabla IEEE 802 | Que 802.1D, 802.1Q y 802.1X son del grupo 802.1: la página del grupo no se pudo leer | Dicho como deducción de la numeración (oficio) |
| 20 | 1 cita cruzada | § 5, grupos disueltos | «según la misma página»: es otra (NADots, «Hibernating and Disbanded»; hibernando, ninguno) | Corregido |
| 21 | 9 | § 6, ISM | «Las bandas de uso libre empezaron en 2,4 GHz»: la fuente dice que la banda de 2,4 GHz **se añadió** en 1985 a las ISM (ya había de 27 y 915 MHz) | «Wi-Fi creció en una banda de uso libre» |
| 22 | 9 | § 6, 802.11n | «Primera de doble banda»: sin fuente | «Primera de la tabla en las dos bandas (Bonaventure)» |
| 23 | 9 | § 6, técnicas | Columna «Desde» (Wi-Fi 6): las fuentes listan OFDMA, MU-MIMO, 160 MHz, TWT y *beamforming* entre las funciones de Wi-Fi 6, no dicen que nazcan con él | Columna «Generación en que la cita la fuente» |
| 24 | 9 | § 6, SSID | «un punto de acceso puede ocultarlo»: Bonaventure dice que puede no emitir balizas | Corregido |
| 25 | 6 | § 6, WEP y TKIP | «anuncia que … will be disallowed» sin «In a future release» | «en una versión futura» |
| 26 | 9 | § 6, WPA3-Personal y Enhanced Open; siglas | «Su autenticación es SAE» y Enhanced Open = OWE: ninguna fuente une SAE con WPA3-Personal ni OWE con Enhanced Open (la página de controladores sólo nombra ambas) | Quitadas las dos atribuciones y las siglas SAE y OWE |
| 27 | 6 | § 6, métodos EAP | «que Windows trae de serie» y EAP-TLS «el de mayor seguridad»: Microsoft dice que los métodos con EAP-TLS **suelen** dar el nivel más alto | «que Microsoft documenta para Windows»; «suele dar la mayor seguridad» |
| 28 | 9 | «Lo que este tema no da» | «Las velocidades máximas de 802.11n no constan»: Bonaventure da 150 Mbit/s | Dicho que el manual la da y que no se recoge por no contrastarse con la norma |
| 29 | 9 | Trazabilidad | RFC 9114 listado como fuente: el tema no lo cita; «Las citas en inglés llevan detrás la traducción»: muchas no la llevan | Quitado el 9114; «Algunas citas…» |
| 30 | 5 siglas | Siglas | PC sin presentar (aflorado al quitar OWE y SAE) | Añadido «ordenador personal (PC)» |

Confirmado sin cambios (muestra de lo releído): cronología ISOC 1962-1995 (Licklider, IMP en UCLA
en septiembre de 1969 y cuatro nodos a fin de año, Crocker y los RFC, NCP en 1970-1972, ICCC y
correo en 1972, INWG#39 en septiembre de 1973 y versión de 1974, *flag day* de 1983, NSFNET 1985,
baja de ARPANET en 1990, FNC 24-X-1995 por unanimidad, 32 bits y 256 redes); ICANN (cinco RIR,
cinco últimos bloques, 4.300 millones); UIT 2025; fechas del índice de RFC (791, 2246, 4346, 5246,
6101, 7568, 8446, 8996, 9846 de julio de 2026, 9915 de enero de 2026, 2474 actualiza al 791);
campos y bits de la cabecera IPv4 (figura 4 del RFC 791) e IPv6 (RFC 8200, STD 86, julio de 2017;
orden de las cabeceras de extensión); bloques del RFC 6890 (direcciones y nombres) y del 1918;
ejemplos del RFC 4291; RFC 5952; `ipconfig` (`/release6`, `/renew6`, `/flushdns`), `tracert` (TTL,
30 saltos, asteriscos); Bonaventure (Ethernet, topologías, MAC, STP, VLAN, 802.11 a/b/g); IEEE 802
(grupos activos); 802.11 *Timelines* (títulos de a-1999 a bn, 802.11-2024 «Accumulated Maintenance
Changes», be-2024 con la 802.11-2024 entre sus bases); Wi-Fi Alliance (años de Wi-Fi 4 a 7, HaLow,
WiGig, WPA3, PMF); Microsoft (Wi-Fi 7 y 24H2, `netsh`, cuatro a ocho flujos, 1903); Juniper (modos
de solicitante, VLAN de invitados); NPS y RADIUS 1812.

Pasajes cambiados releídos: cada «ese», «la misma», «el mismo comunicado» tiene delante su
antecedente (el «mismo comunicado» del § 1 es el del RIPE NCC, que es de donde sale la cita).

## Lo que no se tocó y conviene saber

- `fuentes/canal-sur/informatico/web/r-cisco-8021x.txt` sigue en disco (12 líneas, sin contenido
  útil) aunque el informe de redacción lo da por borrado. El tema no lo usa. No lo he borrado.
- La tabla de velocidades de Bonaventure da para 802.11n 150 Mbit/s, cifra discutible frente a la
  norma (no leída); por eso no entra en la tabla.

## Otros ficheros tocados

Ninguno, salvo el tema y este informe. Temporales en el *scratchpad* (`29t13-*`).
