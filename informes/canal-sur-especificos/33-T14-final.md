# Realizador/a (puesto 33) · Tema 14 · Fase 5 bis, revisión de lo rematado

Tema: `temas/canal-sur-especificos/33-realizador-a/14-formatos-video-resolucion-compresion-hdr-codecs-entregables.md`.
Fecha del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha del sistema). Alcance: sólo los
cuatro pasajes que lista `33-T14-remate.md`, delimitados con `diff` contra la copia previa al remate.

Fuentes: `fuentes/canal-sur/montador/resolve21-extractos/hdr.txt` (DaVinci Resolve 21 Reference
Manual, cap. 10, pp. 259-274), `.../hdr-entrega.txt` (pp. 280-291) y
`fuentes/canal-sur/montador/smpte/catalogo-st2094-40.txt` (ficha SMPTE).

## Negritas

28 negritas del epígrafe nuevo cotejadas con script propio (espacios y comillas tipográficas
normalizadas; la de Dolby Vision con «[…]», en sus dos trozos): **28/28 literales**.

## Datos en redonda, uno a uno

| Pasaje | Dato | Fuente | Resultado |
|---|---|---|---|
| 1 | «(oficio, a partir de la ficha)» | Etiqueta, no dato | Conforme |
| 2 | Supresión de la frase de perfiles no desarrollados | Coherente con el epígrafe nuevo | Conforme |
| 3 | Cinco perfiles; cuatro con PQ; HDR Vivid de la UWA con análisis y ajuste plano a plano | pp. 262, 267, 284, 286-288 | Conforme |
| 3 | HDR10: resolución 3.840 × 2.160 «el máster se hace a…» | p. 282: son características que el HDR10 estipula **para los discos** Ultra HD Blu-ray | **Corregido**: «fija para esos discos resolución UHD de 3.840 × 2.160…» |
| 3 | MaxCLL/MaxFALL en el nivel 6; recorte en pantalla de 500 | pp. 267, 282 | Conforme |
| 3 | HDR10+: Samsung, análisis de bajada a SDR, per clip, HEVC «ST 2094 App4»; resuelve la incompatibilidad con BT.709 | pp. 282, 284-286 | Conforme |
| 3 | Dolby Vision: niveles 0, 1, 2, 8, 5, 6; ejemplo 100/1.000 nits; licencia de Dolby para ajustes manuales | pp. 267, 273 | Conforme |
| 3 | HLG: BBC y NHK, sin metadatos, un flujo, 10 bits; «benefit»/«deficiency» | p. 289 | Conforme |
| 3 | ST 2094-40: título, fechas, «stabilized»; identidad App4 = Application #4 | ficha SMPTE | Conforme |
| 3 | Estático/dinámico; ST 2086 «describe el monitor de masterizado» | Declarado oficio; antecedente en «Los metadatos de masterizado» | Conforme |
| 3 | Entrega: XML junto a TIFF/EXR, IMF con MXF, H.265; .json sidecar, Mezzanine File, HEVC Main10; informe de niveles de luz | pp. 280, 286, 291 | Conforme |
| 4 | Siglas: «las cadenas públicas BBC y NHK» | El manual sólo dice «The BBC and NHK»; «cadenas públicas» no consta en lo leído (error 9) | **Corregido**: «BBC y NHK, que su fuente nombra sólo por las siglas» |
| 4 | Ficha, «Qué se puede preguntar», «Normas», «Lo que no da», «Trazabilidad» | Coinciden con lo leído y con las páginas citadas | Conforme |

## Antecedentes

«la norma que el manual nombra» → ST 2094 de la fila HDR10+ (delante). «los cuatro primeros» →
lista de cinco perfiles (delante). «esos discos» → Ultra HD Blu-ray (misma frase). Sin remisiones huérfanas.

## Lentes

`indice.py`: 20.640 palabras, 75 epígrafes; ficha «20.600 aproximadamente», cuadra.
`refutar_prosa.py`: 3 hallazgos previos (HD, UHD, HDR en el título literal), no tocados.

**Resultado: 2 correcciones menores (error 9 y precisión de alcance); el tema queda cerrado.**

Ficheros tocados: el tema y este informe.
