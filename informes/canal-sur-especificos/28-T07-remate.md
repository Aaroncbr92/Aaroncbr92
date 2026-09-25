# Puesto 28 · Operador/a de Sonido · Tema 7 · Fase 5, remate

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/07-sonido-en-radio.md`.
Remate hecho el 25-09-2026 («hoy» del encargo: 24-09-2026), sobre `28-T07-refutacion.md` y
`28-T07-preguntas.md`. **Hay ampliación con contenido nuevo** (lagunas 1 y 2): procede la fase 5 bis.

## Fuentes releídas antes de aplicar (25-09-2026)

| Fuente | Qué se comprobó |
|---|---|
| EBU Tech 3326 Rev. 4 (texto del PDF) | Tabla de MPEG capa II: «Bitrates and sampling rates in bold are mandatory», † en 192, 256 y 384, «†OPTIONAL for portable equipment» |
| AES TD1008.1.21-9 (texto del PDF) | Tabla 1: «Integrated loudness» en música por pista, pista más alta del álbum e intercaladas |
| RFC 8216 (texto) | Primera frase de la finalidad, para dejarla sola en el primer párrafo |
| Apple, *Audio requirements* (web pasada a texto) | «If a stereo audio source exists, it must be used.», «send the audio source with two identical channels for left and right», mono y estéreo admitidos en MP3, tabla de RSS y «These bit rates apply to both the AAC and MP3 formats.» |
| UIT-T G.722 (09/2012, en vigor; enmienda 1 de 10/2014), PDF del paquete oficial de la UIT | Resumen «an audio wideband (WB, 50 to 7 000 Hz) coding system»; § 2.4.1 «The nominal 3 dB bandwidth is 50 to 7 000 Hz.»; título |
| UIT-T G.712 (11/2001, en vigor), PDF de la UIT | § 1: canales PCM «coded in accordance with ITU-T Rec. G.711»; § 5.2: pérdida de retorno «over the frequency range 300 Hz to 3400 Hz» |

Las cinco correcciones del informe se confirmaron en la fuente; ninguna se descartó.

## Pasajes cambiados

**Exactitud**

1. Siglas (IETF/RFC): «que publica sus documentos como peticiones de comentarios» pasa a «y la serie
   de documentos de internet llamada peticiones de comentarios (RFC…), en la que publica la IETF y
   también autores independientes».
2. «Los códecs de la norma ACIP», párrafo de la tabla de MPEG capa II: añadida la frase de las dos
   salvedades (negrita obligatoria; 192, 256 y 384 kbit/s «OPTIONAL for portable equipment»).
3. «Cómo se elige el códec», viñeta «Compatibilidad»: añadido «aunque en los portátiles son
   opcionales sus velocidades de 192, 256 y 384 kbit/s».
4. «La sonoridad del *streaming*», tabla 1: «—» sustituido por «Sonoridad integrada» en tres filas.
5. «El protocolo HLS», primer párrafo: la cita queda en la primera frase de la finalidad; la segunda
   frase se mantiene sólo en el tercer párrafo (copiado de Cámara, sin tocar).

**Ampliación (contenido nuevo)**

6. «Banda estrecha y banda ancha» (laguna 1, pregunta 13): párrafo nuevo con la banda de G.722
   (50-7 000 Hz, WB, ancho nominal a 3 dB, título «7 kHz audio-coding…») y la de G.711 (300-3 400 Hz,
   por la G.712 y su alcance). La cifra 300-3 400 como «banda de la telefonía clásica» se apoya en la
   G.712, que fija ahí sus exigencias; la G.711 no se ha leído y no se le atribuye banda.
7. «El formato de entrega» (laguna 2, pregunta 15): fuente mono en WAV/FLAC con dos canales idénticos;
   fuente estéreo obligatoria si existe; mono y estéreo en MP3; tabla de velocidades de RSS.
8. Siglas: añadida WB (*wideband*), que entraba con la cita de la G.722.
9. Ficha (Fuente), «Recomendaciones técnicas que el tema cita» y «Trazabilidad»: filas de G.722 y
   G.712; fila de Apple ampliada.

Relectura de los pasajes: cada «esa banda», «la tabla», «sus velocidades» tiene su antecedente en la
misma frase o la anterior.

## Lentes

- `indice.py`: 49 epígrafes, sin cambios de estructura; 10.414 palabras (antes 10.031, el +3,8 % es la
  ampliación).
- `refutar_prosa.py`: 8 hallazgos, los mismos que antes del remate (siglas dentro de citas en inglés:
  ANSI, ATSC, FS, HE, PCMA, PCMU, RX, TOS); el de WB que introdujo la ampliación, resuelto.
- El tema no cita normas jurídicas salvo el Contrato-programa, copiado del común: no se corren
  `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

Preguntas: con el remate, las 15 quedan enteras.

## Otros ficheros tocados

Sólo el tema y este informe. PDF de la G.722 y la G.712 y copia previa del tema, en el scratchpad
(`rem28t07/`), fuera del repositorio.
