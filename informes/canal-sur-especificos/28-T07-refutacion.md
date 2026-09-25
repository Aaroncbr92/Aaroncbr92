# Puesto 28 · Operador/a de Sonido · Tema 7 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/07-sonido-en-radio.md` (933 líneas).
Refutación hecha el 25-09-2026 («hoy» del encargo: 24-09-2026). No se corrige nada: esto es para el remate.

## Alcance

- Exactitud: todo el tema salvo los bloques listados en `28-T07-redaccion.md` bajo «Copiado del común»
  (4) y «Copiado de RTVE sin cambios» (8). Lo adaptado de RTVE y lo nuevo sí se ha mirado.
- Cobertura: el tema entero contra el enunciado («Sonido en radio: microfonía, mesa, híbridos,
  RDSI/IP, codecs, telefonía, streaming y podcast»).

## Fuentes releídas (25-09-2026)

EBU Tech 3326 Rev. 4 (texto del PDF de `fuentes/canal-sur/sonido/` y del de la verificación, más la
tabla de MPEG capa II sacada del PDF en modo de maquetación); EBU Tech 3368 v1.0; AES TD1008.1.21-9;
RFC 8216; Apple, *Audio requirements*; DPA, «The basics about comb filtering»; Clear-Com, *Partyline
Guide* 2018; Yamaha CL V5 y *Get on the Bus*; UIT-T I.412 (versión española); EBU R 128-2023;
Contrato-programa 2024-2026 (BOJA 245/2023), sólo para las dos citas de «Qué es un pódcast».

Método: script que coteja cada negrita del cuerpo (troceada por «[...]») con el texto de las fuentes,
normalizando espacios, comillas y guiones. No casaron sólo: «Latency is an issue.» (salto de página
del PDF entre «Latency» y «is an issue», comprobado), «a DSL line…» (salto de página, comprobado),
los rótulos «Obligatorios / Recomendados / Opcionales» (no son citas) y las citas del
Contrato-programa (saltos de línea; las del común, exentas; las de «Qué es un pódcast», comprobadas a
mano en los puntos 45 y 46). Revisadas además a mano las afirmaciones en redonda de lo nuevo y lo
adaptado: RFC3550/3551, RFC4588 + RFC4585, puerto 5004 de RTP sobre TCP, FEC RFC5109/5006/RFC2733,
tipos de carga 0/8/9/14, 20 y 4 ms, § 3.1.5 entre los obligatorios, AAC-hbr, APT-X/ADPCM/RFC7310,
Opus 6-510, § 3.3.5 como regla general, glosario AAC-LD, parámetros de la tabla 1 de la Tech 3368,
búfer adaptativo/estático y caso del hotel, a=sendonly/recvonly, 488, tabla 1 y 2 de la TD1008 y
notas 1 y 7, fórmula, cifras de Apple, R 128 puntos r) y s).

## Exactitud

**Graves: 0.** No hay dato falso, cifra mal ni cita que no esté en su fuente.

**Menores: 4.**

1. **Tabla 1 de la TD1008, columna «Cómo se mide» (error 6, omisión en tabla).** En las filas de
   música por pista, pista más alta del álbum y piezas intercaladas el tema pone «—»; la fuente da
   para las tres «Integrated loudness». Tal como está, sugiere que no hay método. Corrección:
   «Sonoridad integrada» en esas tres celdas.
2. **Tabla de MPEG capa II (error 6).** El tema la presenta como «velocidades recomendadas» (bien),
   pero omite la salvedad de la propia tabla: «Bitrates and sampling rates in bold are mandatory» y
   que las marcadas † (192, 256 y 384 kbit/s) son **«OPTIONAL for portable equipment»**. Afecta
   también a «Compatibilidad» en «Cómo se elige el códec», que da la capa II como obligatoria sin
   matiz para los portátiles. Corrección: una frase con ambas salvedades (la negrita del PDF no se
   conserva en el texto; basta la del †).
3. **Siglas: «IETF … que publica sus documentos como peticiones de comentarios (RFC)».** Choca con lo
   que el propio tema dice después (RFC 8216 es **«Independent Submission»**, no de la IETF). No es
   falso para la mayoría de las RFC citadas, pero en un test sobre el estatus de HLS confunde.
   Corrección: «las RFC, serie de documentos de internet en la que publica la IETF (y también envíos
   independientes)», o quitar «que publica sus documentos como».
4. **Cita repetida en «El protocolo HLS».** «adapt the bit rate of the media to the current network
   conditions in order to maintain uninterrupted playback at the best possible quality» aparece dos
   veces (primer párrafo, nuevo, y tercer párrafo, copiado de Cámara 13). Prosa: sobra la del primer
   párrafo (lo copiado del común no se toca); basta con citar allí la primera frase de la finalidad.

Nota sin hallazgo: la verificación dejó sin tocar el punto 104 del Contrato-programa; no hace falta
para el enunciado.

## Cobertura

Las ocho rúbricas tienen epígrafe propio y en su orden. Preguntas: `28-T07-preguntas.md`; 13 enteras,
1 a medias, 1 no.

**Lagunas: 2.**

1. **Telefonía: bandas de la voz telefónica (pregunta 13, «no»).** El epígrafe «Banda estrecha y
   banda ancha» dice sólo que G.711 «suena a teléfono» y G.722 «más llena», como oficio. Un test puede
   pedir la banda de 300-3 400 Hz de la telefonía clásica o los 50-7 000 Hz de G.722. Ampliación:
   leer la UIT-T G.722 (banda de audio que codifica) y la G.711/G.712 (banda del canal telefónico) y
   dar las cifras con su cita; si no se confirman, dejarlo en «Lo que este tema no da». La rúbrica
   «Telefonía» es, además, la más corta del tema (unas 350 palabras, casi todo remisiones).
2. **Pódcast: fuente mono en WAV/FLAC y velocidades del RSS (pregunta 15, «a medias»).** El tema cita
   que Apple no acepta un canal en WAV/FLAC pero no el remedio que da la misma página: **«send the
   audio source with two identical channels for left and right»**; tampoco da la tabla de velocidades
   para RSS (MP3/AAC: mono 64-128 kbps y estéreo 128-256 kbps a 44,1/48 kHz; 40-80 y 80-160 a
   22,05/24 kHz), que es lo que se entrega de verdad a la plataforma. Fuente ya leída en fase 3;
   ampliación de dos líneas en «El formato de entrega».

## Recuento

| Clase | Número |
|---|---|
| Graves | 0 |
| Menores | 4 |
| Lagunas | 2 |

## Otros ficheros tocados

Ninguno fuera de este informe y de `28-T07-preguntas.md`. Script de cotejo en el scratchpad
(`r28t07/chk.py`), fuera del repositorio.
