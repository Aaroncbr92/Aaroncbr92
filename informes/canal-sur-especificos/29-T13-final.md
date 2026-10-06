# Puesto 29 · Tema 13 · Revisión de lo rematado (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/13-redes-internet-y-comunicaciones.md`.
Alcance: sólo los 12 pasajes listados en `29-T13-remate.md` (diff contra el último commit).

## Fuentes releídas el 06-10-2026 (en disco, `fuentes/canal-sur/informatico/web/`)

`r-rfc2131.txt` (tabla de mensajes, § 3.1, § 4.1), `r-rfc6265.txt` (§ 4.1.2.1-4.1.2.6, § 4.1.2),
`r-rfc3056.txt`, `r-rfc4380.txt`, `r-rfc6333.txt` (resúmenes y § 4.1), `r-rfc6890.txt` (tablas 8, 23
y el bloque 2002::/16), `r-ieee8023-archive.txt`, `r-ieee8023ab.txt`, `r-ieee8023at.txt`,
`r-cisco-rf.txt`, `r-wfa-wpa3-2018.txt`, `r-ms-wifi.txt`, `r-ms-wificx7.txt`.

## Comprobación, pasaje a pasaje

| # | Pasaje | Resultado |
|---|---|---|
| 1-3 | Ficha, siglas (SAE), «Qué se puede preguntar» | Correctos. Extensión ~17.500: `indice.py` da 17.680 tras esta fase |
| 4 | DHCP: puertos 67/68, cuatro mensajes, NAK, DECLINE, RELEASE, INFORM, retransmisión, agente | Todas las negritas literales en RFC 2131 (tabla, § 3.1 pasos 1-3, § 4.1). **Corregido**: DHCPDECLINE decía «la dirección ofrecida»; según § 3.1 paso 5 el cliente comprueba la dirección tras el DHCPACK → «la dirección recibida con el DHCPACK» |
| 5 | Atributos de cookie | Literales en RFC 6265 (Max-Age partido «Max-\nAge» en la fuente; el literal vale). Secure: confidencialidad, no integridad (§ 4.1.2.5). Correcto |
| 6 | 6to4, Teredo, DS-Lite | Bloques en RFC 6890; citas literales en los resúmenes de 3056, 4380, 6333 y § 4.1 del 6333. Correcto |
| 7 | Enmiendas de 802.3 | Las 11 filas, años y títulos coinciden con el archivo; cita de la 802.3ab y grupo «Power over Ethernet plus» literales. 1000BASE-T y PoE ya presentados con fuente en el tema. **Corregido**: «Fast Ethernet» no figura en ninguna fuente leída → «la enmienda que trajo 100BASE-TX» (aquí y en «Lo que este tema no da») |
| 8 | Canales de 2,4/5 GHz (Cisco) | Citas literales. **Ampliado con fuente**: «En 5 y 6 GHz» sólo citaba 5 GHz; añadida la cita de 6 GHz de la misma guía. Cisco sí trata el plan de cuatro canales (1, 5, 9, 13) y lo desaconseja: añadida su cita literal, y corregida la línea de «Lo que este tema no da» que decía que otros planes no constaban |
| 9 | Wi-Fi 7 de Microsoft | Literal en `r-ms-wifi.txt`. Correcto |
| 10 | WPA3-Personal / SAE | Literal en el comunicado de 25-VI-2018 y en `r-ms-wificx7.txt`. Correcto |
| 11 | «Lo que este tema no da» | Ajustado según 7 y 8 |
| 12 | Trazabilidad | Fechas correctas. Fila Cisco actualizada (plan de cuatro canales; 5 y 6 GHz) |

Antecedentes releídos en cada pasaje cambiado («los dos últimos», «su RFC», «esa banda», «ese
archivo», «la misma guía»): todos tienen delante su referente.

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 17.680 palabras, 43 epígrafes (índice sin cambios).

## Efecto en las preguntas

La 13 (canales sin solapamiento) puede pasar a **entera**: el tema da ya 1, 6 y 11 y la variante de
cuatro canales con la valoración de Cisco. Recuento: 15 enteras.

## Otros ficheros tocados

Ninguno salvo el tema y este informe.
