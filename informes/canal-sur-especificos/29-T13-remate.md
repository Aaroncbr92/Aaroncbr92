# Puesto 29 · Tema 13 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/13-redes-internet-y-comunicaciones.md`.
Entrada: `29-T13-refutacion.md` (1 hallazgo menor, 6 lagunas, 1 observación) y `29-T13-preguntas.md`
(9 enteras, 1 a medias, 5 no). **Se amplió contenido nuevo**: necesita fase 5 bis sobre los pasajes
de abajo.

## Fuentes

Releídas el 06-10-2026 en disco (descargadas el 05-10-2026): `r-rfc2131.txt` (tabla 2 de mensajes,
pasos 1-5 del § 3.1, puertos 67/68), `r-rfc6265.txt` (§ 4.1.2.1-4.1.2.6), `r-ms-wificx7.txt`
(línea 18), `r-ms-wifi.txt` (línea 59), `r-rfc6890.txt` (bloques ya citados).

Descargadas y leídas el 06-10-2026 (nuevas en `fuentes/canal-sur/informatico/web/`):

| Fichero | URL |
|---|---|
| `r-rfc3056.txt`, `r-rfc4380.txt`, `r-rfc6333.txt` | rfc-editor.org/rfc/rfcNNNN.txt (resúmenes; de 6333 además § 4.1) |
| `r-ieee8023-archive.txt` | https://www.ieee802.org/3/archive.html |
| `r-ieee8023ab.txt`, `r-ieee8023at.txt` | https://www.ieee802.org/3/ab/index.html y /3/at/index.html |
| `r-cisco-rf.txt` | Cisco, *Wireless RF Reference Guide* (Catalyst 9800) |
| `r-wfa-wpa3-2018.txt` | Wi-Fi Alliance, comunicado de 25-VI-2018 de presentación de WPA3 |

## Correcciones y lagunas, una a una

| # | Qué decía el informe | Comprobado en la fuente | Qué se hizo |
|---|---|---|---|
| E1 | Columna «Qué sostiene» de la fila RFC 9110…768 sólo habla de HTTP | Cierto | Completada (QUIC, HSTS, cookies y atributos, DoH, DNS/TTL, DHCP y puertos, UDP) |
| L1 | Falta el intercambio DHCP y los puertos 67/68 | RFC 2131, tabla 2, § 3.1 y § 4.1: confirmado | Ampliado § 1, «Los principales servicios» |
| L2 | Faltan atributos de cookie | RFC 6265 § 4.1.2: confirmado; SameSite no está, no se da | Ampliado § 3, «Privacidad» |
| L3 | Qué hace 6to4, Teredo y DS-Lite | Fuentes descargadas; resumen de cada RFC y § 4.1 del 6333 | Ampliado § 4, «Convivencia y transición» (tabla) |
| L4 | Enmiendas de 802.3 | Archivo del 802.3: z, ab, ac, ad, ae, an, af, at, bt, bz, az confirmadas. **802.3u no figura**: no se da y se declara | Ampliado § 5, «Las normas IEEE 802» (tabla) |
| L5 | Canales de 2,4 GHz sin solapamiento | Cisco: 1, 6 y 11 (con la precisión «in the U.S.»). El plan europeo de la pregunta (1, 5, 9, 13) no consta: no se da | Ampliado § 6, «Los estándares»; «Lo que este tema no da» ajustado. La pregunta 13 queda contestable en su opción a) sólo en la parte 1, 6 y 11 |
| L6 | SAE en WPA3-Personal | La refutación decía que la unión WPA3-Personal/SAE no tenía fuente; el comunicado de la Wi-Fi Alliance de 2018 la da literal (**«WPA3 leverages Simultaneous Authentication of Equals (SAE)…»**, en el párrafo de WPA3-Personal). «Sustituye a la PSK de WPA2» no consta: no se escribe | Ampliada fila WPA3-Personal de § 6, «La seguridad»; sigla SAE añadida |
| Nota | Comparación de Wi-Fi 7 de Microsoft | `r-ms-wifi.txt` línea 59: confirmada | Añadida en § 6, «Las técnicas de transmisión» |
| Obs. | Repetidor y controlador inalámbrico | Sin fuente | Declarado en «Lo que este tema no da» |

## Pasajes cambiados

1. Ficha: Fuente (+ Cisco), Redacción que se estudia (05-10 o 06-10-2026), Extensión (17.500).
2. Siglas: + SAE.
3. «Qué se puede preguntar»: + mensajes DHCP, Secure/HttpOnly, 6to4/Teredo/DS-Lite, enmiendas 802.3
   y PoE, canales de 2,4 GHz, SAE.
4. § 1, viñeta DHCP: puertos 67/68, tabla de los cuatro mensajes, DHCPNAK, DECLINE, RELEASE, INFORM,
   retransmisión y agente de retransmisión (la razón de la difusión, marcada como oficio).
5. § 3, tras las cookies de terceros: tabla de atributos Expires/Max-Age, Domain, Path, Secure,
   HttpOnly; independencia de Secure y HttpOnly; recomendación de llevar los dos (oficio).
6. § 4, «Convivencia y transición»: la frase que sólo nombraba 6to4, Teredo y DS-Lite pasa a tabla
   con bloque, RFC y qué hace cada uno, y una línea de diferencia.
7. § 5, «Las normas IEEE 802»: tabla de enmiendas de 802.3 y frase sobre su publicación en la
   edición de la norma; 802.3u declarada no encontrada.
8. § 6, «Los estándares»: canales 1, 6 y 11 de 2,4 GHz y los de 5 GHz sin solapamiento (Cisco).
9. § 6, «Las técnicas de transmisión»: comparación de Wi-Fi 7 de Microsoft.
10. § 6, «La seguridad», fila WPA3-Personal: SAE (Wi-Fi Alliance 2018) y «WPA3-SAE authentication»
    (Microsoft).
11. «Lo que este tema no da»: CNAF reescrita; + 802.3u; + repetidor y controlador; 6to4/Teredo/DS-Lite
    reescrita (sólo resúmenes).
12. «Trazabilidad»: frase de fechas; fila RFC 9110… completada (E1); filas nuevas RFC 3056/4380/6333,
    IEEE 802.3 archivo, Cisco, Wi-Fi Alliance 2018.

Releídos todos: cada «su RFC», «el grupo», «esa banda» tiene delante su antecedente.

## Lentes

Tema técnico sin norma jurídica: `indice.py` (17.572 palabras, 43 epígrafes, sin cambios de índice:
no hay epígrafes nuevos) y `refutar_prosa.py` (0 hallazgos tras presentar «RF» en Trazabilidad).

## Preguntas tras el remate

3, 6, 10, 11 y 14 pasan a **entera**; 13 pasa a **a medias** (da 1, 6 y 11, no la variante de
cuatro canales). Recuento: 14 enteras, 1 a medias, 0 no.

## Otros ficheros tocados

Las ocho fuentes nuevas listadas arriba y este informe. Ningún otro tema.
