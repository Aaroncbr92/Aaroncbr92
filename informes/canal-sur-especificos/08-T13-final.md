# Puesto 08 · Tema 13 · Fase 5 bis · Revisión de los pasajes del remate

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/13-produccion-movil-y-transmision.md`.
Leídos sólo `ENCARGO.md`, el enunciado del puesto 08 y `08-T13-remate.md` (no `metodo/`).
Revisados sólo los 11 pasajes que lista el remate. Copia previa: `t13-antes-5bis.md` en el scratchpad.

**Resultado: 2 correcciones y 1 sigla añadida; el resto confirmado.**

## Fuentes releídas (todas el 24-09-2026)

| Fuente | Dónde | Resultado |
|---|---|---|
| SMPTE ST 2110-10:2022 | `.txt` l. 360-377 (6.3, 6.4), 696-698 (8.5) | 1460 / 8960 octetos, «unless operating conformant…», «Senders may transmit», «All Receivers shall be capable…»: literales exactos |
| ETSI EN 300 744 V1.6.2 | título l. 1-4; 4.1 l. 620-662 | Título, «Orthogonal Frequency Division Multiplexing (OFDM)», «an OFDM system with concatenated error correcting coding»: exactos. La norma no dice «primera generación» (ver C1) |
| Domo, libro blanco COFDM | págs. 1-3 (imágenes, releídas) | Título y cita larga de la pág. 3: exactos. Pág. 2 dice «In a DVB-T COFDM system» |
| Domo, ficha Sapphire-BTX | copia web del remate | «integrates a true 4K HEVC encoder…», «camera control and Tally interfaces», «for direct microphone connection», «Typically 35mS input to output»: exactos. La glosa «por el mismo enlace» no consta (ver C2) |
| Ayuda de YouTube 2907883, 10349430, 10364924 | copias web | Las seis citas, exactas y en el artículo que dice la trazabilidad |
| RFC 8216 | cabecera, resumen, estado, 1, 2 | «Category: Informational», Independent Submission, agosto de 2017, citas de resumen, 1 y 2, «version 7»: exactos. Ficha JSON del RFC Editor, releída hoy: `obsoleted_by` vacío |
| draft-pantos-hls-rfc8216bis | API del datatracker, releída hoy | Revisión -22, caduca el 02-11-2026: activo. Confirmado |
| Adobe RTMP (Parmar y Thornburgh, 21-12-2012) | l. 1-5, 84-90, 7.2.2.6 | Cita de la introducción, orden *publish* y tipo «live»: exactos |
| Libro de estilo, 4.4 | l. 2618-2622 | Cita hasta «postproducción...»: exacta (M2 bien aplicada) |
| Contrato-programa BOJA 245/2023 | l. 2044-2045 | Título de 3.19: exacto (M3 bien aplicada) |

## Correcciones aplicadas (comprobadas en la fuente)

| # | Pasaje | Antes | Después | Por qué |
|---|---|---|---|---|
| C1 | 4 («El enlace inalámbrico de cámara», 2.º párrafo) | «televisión digital terrestre de primera generación» | «televisión digital terrestre DVB-T» | Error 9: la EN 300 744 no se llama «primera generación»; sí nombra DVB-T (4.1) y el libro blanco dice «DVB-T COFDM system» |
| C2 | 4 (4.º párrafo, Sapphire-BTX) | «(control de cámara y piloto por el mismo enlace)» | «(interfaces de control de cámara y de piloto; el control de cámara bidireccional es una opción de hardware)» | Error 9: la ficha habla de interfaces, no de que viajen por el enlace; y dice «Bi-directional camera control is a hardware option» |
| S1 | 2 (siglas) | — | Añade **DVB-T** tras ETSI | Error 5, creado por C1 |

## Antecedentes

Comprobados: «ese libro blanco» (Domo, párrafo anterior), «la misma cláusula» (6.3), «esa
codificación» (la de la cita de 4.1), «Como las de la LU800» (epígrafe de la LU800, antes),
«la tabla de "Qué es el *streaming*"» (nombrada), «cada uno» (RTMP y HLS). Ninguno roto.

## Sin cambios, confirmados

Pasajes 1 (portada; `indice.py` mide 8.899, casa con 8.900), 3, 5, 6, 7, 8, 9, 10 y 11.

## Lentes

`indice.py`: 37 epígrafes, 8.899 palabras. `refutar_prosa.py`: 2 avisos ya vistos (IP en el
título; BTX, parte del nombre de modelo). Sin norma jurídica: no proceden las otras lentes.

## Ficheros tocados

El tema y este informe.
