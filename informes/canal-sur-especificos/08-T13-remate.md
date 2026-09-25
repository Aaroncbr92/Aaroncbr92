# Puesto 08 · Tema 13 · Fase 5 · Remate

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/13-produccion-movil-y-transmision.md`.
Entradas: `08-T13-refutacion.md` (3 menores, 2 lagunas) y `08-T13-preguntas.md` (12 enteras,
1 a medias, 2 no). Leídos sólo `ENCARGO.md` y el enunciado del puesto 08 (no `metodo/`).
Copia del tema antes del remate en el scratchpad (`t13-antes-remate.md`).

**Resultado: se amplió contenido nuevo** (dos `###` nuevos). Procede la fase 5 bis sobre los
pasajes 4 y 5.

## Correcciones de exactitud: comprobadas en la fuente y aplicadas

| # | Fuente releída (24-09-2026) | Comprobación | Aplicada |
|---|---|---|---|
| M1 | SMPTE ST 2110-10:2022, `.txt` l. 360-377 | 6.3 exceptúa «unless operating conformant to the optional Extended UDP Size Limit specified in section 6.4»; 6.4: «shall be 8960 octets», «Senders may transmit»; receptores obligados sólo hasta el estándar | Sí |
| M2 | Libro de estilo, l. 2619-2622 | La enumeración de 4.4 sigue «contratación de bienes o servicios, edición y postproducción... así como…» | Sí: se cita hasta «postproducción...» (los puntos son del original) |
| M3 | Contrato-programa BOJA 245/2023, l. 2044-2045 | Título: «Compromisos de cobertura por ondas hertzianas terrestres y de distribución de servicios nuevos» | Sí |

El informe de refutación no se equivocó en ninguna.

## Lagunas: se amplió el tema (no se tocó ninguna pregunta)

| # | Qué se añadió | Fuentes leídas el 24-09-2026 |
|---|---|---|
| L1 | `### El enlace inalámbrico de cámara` en «Enlaces» | ETSI EN 300 744 V1.6.2 (local), cláusula 4.1 (l. 620-662); Domo Broadcast Systems, libro blanco «Coded Orthogonal Frequency-Division Multiplexing (COFDM)» (PDF en imagen, págs. 1-3 leídas como imagen) y ficha web del Sapphire-BTX (curl) |
| L2 | `### Emitir hacia una plataforma: URL, clave, RTMP y HLS` en «*Streaming*» | RFC 8216 (rfc-editor.org, txt: cabecera, resumen, 1, 2) y su ficha JSON (sin `obsoleted_by`); datatracker de draft-pantos-hls-rfc8216bis (borrador activo, -22); Adobe RTMP spec 1.0, 21-12-2012 (copia en github.com/veovera/enhanced-rtmp, `docs/legacy/rtmp-v1-0-spec.pdf`): resumen, 1, 7.2.2.6; Ayuda de YouTube en español, artículos 2907883, 10349430 y 10364924 |

Descargas en el scratchpad de la sesión (`rfc8216.txt`, `rtmp.pdf`/`rtmp.txt`, `yt*.txt`,
`l1/wp.pdf` y `l1/wp*.png`, `l1/btx.txt`, `l1/domo.txt`), fuera del repositorio.

Descartado por no confirmarlo: que RTMP sea «el protocolo más habitual» (el tema dice sólo que
YouTube muestra RTMP por defecto); el número de portadoras del libro blanco (2.048, no casa con los
modos de la ETSI sin leer más); el régimen jurídico de las frecuencias (el identificador que probé
no era la Ley General de Telecomunicaciones): se declara en «Lo que este tema no da».

## Pasajes cambiados

1. Portada: «Fuente» (añade ETSI EN 300 744 cl. 4.1, RFC 8216, RTMP de Adobe, Domo, ayuda de
   YouTube) y «Extensión» (7.400 → 8.900; `indice.py` mide 8.878).
2. Siglas: añade OFDM, COFDM, ETSI, URL, RTMP, RTMPS, TLS/SSL, HLS, HTTP.
3. «Qué se puede preguntar»: añade enlace inalámbrico de cámara, URL y clave, RTMP/HLS y latencia,
   tamaño de paquete y su excepción.
4. **Nuevo** «Enlaces» › «El enlace inalámbrico de cámara» (4 párrafos).
5. **Nuevo** «*Streaming*» › «Emitir hacia una plataforma: URL, clave, RTMP y HLS» (párrafo, tabla,
   3 viñetas, cierre).
6. «Qué pide la casa», cita de 4.4 completada (M2).
7. «El *streaming* en Canal Sur», título de 3.19 completado (M3).
8. «Redundancia y límites de paquete», viñeta «Tamaño de paquete» (M1).
9. «Normas técnicas que el tema cita»: fila ETSI EN 300 744; «No son normas» añade HLS, RTMP,
   Domo y YouTube.
10. «Lo que este tema no da»: sustituye la viñeta de protocolos de distribución; añade la de ETSI,
    detalle de COFDM, bandas y régimen de frecuencias.
11. «Trazabilidad»: fila ST 2110-10 con 6.4; cinco filas nuevas; en «Oficio», el transmisor a la
    espalda de la cámara.

Antecedentes releídos: «ese libro blanco» (tiene delante el de Domo), «la misma cláusula» (6.3),
«la tabla de "Qué es el *streaming*"» (nombrada, no «anterior»), «cada uno» (RTMP y HLS de la tabla).

## Lentes

- `indice.py`: índice regenerado, 37 epígrafes (dos nuevos). Portada sin fila en `portadas.tsv`
  (la ficha es manual).
- `refutar_prosa.py`: 2 avisos. IP en el título (previo, ya visto en refutación). «BTX»: es parte
  del nombre del modelo (Sapphire-BTX), no sigla; se deja.
- Sin norma jurídica citada: no se corren `negritas.py`, `refutar_exactitud.py`, `refutar_modo.py`.

## Preguntas tras el remate

12 → entera (M1). 13 → entera (COFDM, «El enlace inalámbrico de cámara»). 14 → entera en lo
confirmable (RTMP, URL y clave; el tema no afirma «más habitual», sólo «por defecto» en YouTube).

## Ficheros tocados

El tema y este informe. Nada más en el repositorio.
