# 05-T15 · Fase 5 bis · Realización para plataformas digitales, redes sociales y directos IP

Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/15-plataformas-digitales-redes-directos-ip.md`.
Alcance: sólo los pasajes que lista `05-T15-remate.md`. Fuentes leídas el 30-09-2026.

## Pasajes revisados y resultado

| Pasaje | Fuente | Resultado |
|---|---|---|
| Tabla «El ayudante en las plataformas digitales», fila «Minutar» (15-10-2024, canales estándar) | El propio tema, «Qué vídeo es un Short» (cita de YouTube) | Correcto |
| CR3.3 y «La cualificación no habla de salidas ni de internet» | `incual-IMS077_3.txt`, l. 160-162 | Literal correcto; la glosa va marcada como oficio |
| Magacín, ensayo: «lo comunica al realizador y, por regiduría, al presentador» | Tabla de «Lo que hace el ayudante en un directo IP» | Coherente |
| CDN: definición 1.1, *surrogate* 1.1, «concurrently» 2; septiembre de 2012, informativa | `ietf-rfc6707.txt`, l. 9, 13, 267-269, 417-423, 488-489 | Correcto (l. 489 está en la sección 2) |
| MPEG-DASH: título, cita del MPEG, ediciones | `mpeg-dash-part1.txt` | **Corregido** (ver 2 y 3) |
| DASH-IF: abril de 2012, «not owned…», «any HTTP server» | `dashif-about.txt`, l. 55-56, 84, 125 | Correcto |
| Estatus HLS frente a DASH | Tema, fila HLS (RFC 8216 «Informational», vía independiente) | **Corregido** (ver 4) |
| Piloto RTVE 2016, CNLSE p. 35 | `cnlse-guia-tv-2017.txt`, l. 1170-1175; página comprobada en el PDF (pág. 35) | Correcto |
| Multidifusión: ST 2110-10, 6.5; IPv6 «should»; RFC 3376 (octubre de 2002, resumen); SDP 239.101.9.10/50020 | `SMPTE_ST-2110-10-2022.txt`, l. 378-387, 852; `ietf-rfc3376.txt`, l. 10, 29-38 | **Corregido** (ver 1 y 5) |
| Siglas nuevas (CDN, IGMP, MPEG-DASH, DASH-IF, ISO/IEC, HbbTV, CNLSE) | `hbbtv-org-overview.txt`; «International Organization for Standardization» consta en otras fuentes del repositorio (p. ej. `montador/web/rfc9559.txt`) | Correcto |
| Portada, normas citadas, Trazabilidad | — | Correcto; añadida RFC 5771 por remisión |

Antecedentes: «su propia RFC», «La propia norma», «ese grupo», «la misma cláusula» tienen delante su
antecedente. Tras las correcciones, «Otro» (MPEG-DASH) remite a HLS, nombrado en la frase.

## Correcciones aplicadas (comprobadas en la fuente)

1. **Error 9 (exceso)**. «ST 2110-10 obliga a emitir y recibir en multidifusión» → «obliga a emisores y
   receptores a admitir la multidifusión». La norma dice «shall support», no que se emita siempre así.
   Lo mismo en «también la unidifusión».
2. **Error 6 (salvedad omitida)**, 6.5: añadida la prohibición de usar para medios los bloques de
   control multidifusión de la RFC 5771 (literal de la cláusula).
3. **Error 6**, MPEG-DASH: la cita «can be used with any media format» se amplía al literal completo, que
   incluye **«has specific provisions for the MPEG-4 file format and MPEG-2 Transport Streams»**.
4. **Error 9**: «HLS es una RFC informativa presentada por una empresa» no consta en ninguna fuente leída
   (no hay copia de la RFC 8216 en `fuentes/`; el propio tema la da como presentada «por la vía
   independiente»). Queda así: «RFC informativa, fuera de la vía de normas de Internet».
5. **Error 9 (traducción)**: «quinta edición como publicada («released»)». La página usa «published» para
   la 2.ª edición y «released» para la 3.ª a la 5.ª. Queda así: «da la quinta edición como «released» y la sexta
   como «ongoing» (en elaboración)».
6. Recuento: «El otro, y el que es norma internacional» → «Otro, y éste sí norma internacional». La
   fuente del DASH-IF habla de tres formatos segmentados comparables, así que no son sólo dos.

## Lentes

- `negritas.py` con ST 2110-10, RFC 6707, RFC 3376, MPEG, DASH-IF y CNLSE: ninguna negrita de los pasajes
  revisados ni de los añadidos sale «NO ESTÁ» (los «NO ESTÁ» restantes son de otras fuentes, fuera del
  alcance); ninguna negrita rota.
- `refutar_prosa.py`: 1 aviso, el mismo que antes («IP» en el título literal).
- `indice.py`: 19.651 palabras, 64 epígrafes. La portada dice «19.600 aproximadamente», así que sigue valiendo.

## Ficheros tocados

El tema (pasajes anteriores) y este informe.
