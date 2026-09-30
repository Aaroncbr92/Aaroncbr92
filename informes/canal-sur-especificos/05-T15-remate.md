# 05-T15 · Remate · Realización para plataformas digitales, redes sociales y directos IP

Fase 5. Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/15-plataformas-digitales-redes-directos-ip.md`.
Insumos: `05-T15-refutacion.md` (3 hallazgos menores, 3 lagunas) y `05-T15-preguntas.md` (12/1/2).
Fecha de lectura de fuentes: 30-09-2026. **Amplía contenido nuevo: sí** (pasa a 5 bis).

## Hallazgos aplicados (comprobados en el propio tema y su fuente)

1. Error 6, tabla «El ayudante en las plataformas digitales», fila «Minutar cada versión»: añadido
   «(canales estándar, vídeos subidos desde el 15-10-2024)», condiciones que da la cita de YouTube en
   «Qué vídeo es un Short». Aplicado.
2. Error 9, mismo epígrafe: CR3.3 releído en `incual-IMS077_3.txt` (no habla de salidas ni de
   internet). Pasaje nuevo: «La cualificación no habla de salidas ni de internet; aplicado a las de
   Canal Sur (oficio), cada salida (antena, Canal Sur Más con difusión mundial, redes) es una
   cobertura distinta…». Aplicado.
3. Incoherencia, magacín, bloque del ayudante, 2.º guion: «lo comunica al realizador y, por
   regiduría, al presentador», como en la tabla de «Lo que hace el ayudante en un directo IP». Aplicado.

## Lagunas: se amplía el tema

| Pregunta | Dónde | Pasaje nuevo | Fuente (leída el 30-09-2026) |
|---|---|---|---|
| 14, CDN | «Dos usos del *streaming*», tras la tabla | Párrafo: definición de CDN, caché (*surrogate*), servicio simultáneo a muchos; «Qué CDN usa Canal Sur Más no consta» | IETF RFC 6707 (sept. 2012, informativa), 1.1 y 2 → `fuentes/canal-sur/realizador/web/ietf-rfc6707.txt` |
| 13, MPEG-DASH | «Emitir hacia una plataforma…», tras HLS | Párrafo: ISO/IEC 23009-1 «Media presentation description and segment formats»; directo y a petición; cualquier formato; ratificada en abril de 2012; cualquier servidor HTTP; ediciones (5.ª «released», 6.ª «ongoing»); estatus frente a HLS; piloto RTVE 2016 con HbbTV | Página MPEG-DASH parte 1 (mpeg.org) → `web/mpeg-dash-part1.txt`; DASH-IF «About» → `web/dashif-about.txt`; guía CNLSE 2017, p. 35 (`cnlse-guia-tv-2017.txt`, l. 1170-1175) |
| 12, multidifusión | Nuevo `###` «Multidifusión: un flujo, muchos receptores», entre «Redundancia…» y «NMOS» | ST 2110-10, 6.5 (multicast IPv4 con IGMP obligatorio; unicast IPv4 obligatorio; IPv6 «should»); IGMP según RFC 3376; explicación del grupo (oficio marcado); ejemplo de SDP (239.101.9.10, puerto 50020) | `fuentes/normas-tecnicas/SMPTE_ST-2110-10-2022.txt`, l. 378-387 y 852; IETF RFC 3376, resumen → `web/ietf-rfc3376.txt` |

No confirmado y por eso no escrito: el desarrollo de las siglas MPEG, IEC y DASH (no aparece en las
fuentes leídas); se nombran «como los escriben sus fuentes».

## Otros pasajes cambiados

- Portada, «Fuente»: añadidas RFC 6707, RFC 3376 e ISO/IEC 23009-1. «Extensión»: 19.600 palabras.
- Siglas: CDN, IGMP, MPEG-DASH, DASH-IF, ISO/IEC, ISO, HbbTV (desarrollo leído en `grafista/hbbtv-org-overview.txt`), CNLSE.
- «Qué se puede preguntar»: MPEG-DASH, CDN, multidifusión.
- «Normas y documentos técnicos que el tema cita» y «Trazabilidad»: tres filas nuevas.
- Índice regenerado.

Relectura de antecedentes: «la misma cláusula», «su propia RFC», «La propia norma» y «ese grupo»
tienen delante su antecedente.

## Lentes

- `indice.py`: 19.583 palabras, 64 epígrafes; índice con la nueva entrada.
- `refutar_prosa.py`: 1 aviso, «IP» sin presentar en el título (preexistente; el título es literal
  del enunciado y la sigla se presenta en «Siglas de la parte de directos por red»).
- `negritas.py` sobre las fuentes nuevas: todas las negritas añadidas, «ok». Una cita de RFC 6707
  salió «NO ESTÁ» en la primera pasada (mezclaba la definición 1.1 con el apartado 2); corregida al
  literal de 1.1 y rehecha la comprobación.

## Ficheros tocados

El tema; este informe; fuentes nuevas guardadas en `fuentes/canal-sur/realizador/web/`
(`ietf-rfc6707.txt`, `ietf-rfc3376.txt`, `mpeg-dash-part1.txt`, `dashif-about.txt`).
