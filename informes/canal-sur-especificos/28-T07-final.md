# Puesto 28 · Operador/a de Sonido · Tema 7 · Fase 5 bis, revisión final

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/07-sonido-en-radio.md`. Revisión del
25-09-2026 («hoy» del encargo: 24-09-2026), limitada a los nueve pasajes que lista `28-T07-remate.md`,
localizados por diff contra la copia previa del tema (`rem28t07/antes.md`, scratchpad).

## Fuentes releídas (25-09-2026)

| Fuente | Cómo | Qué se comprobó |
|---|---|---|
| UIT-T G.722 (09/2012) | PDF del remate, texto; ficha web de la UIT | Resumen «an audio wideband (WB, 50 to 7 000 Hz) coding system»; § 2.4.1 «The nominal 3 dB bandwidth is 50 to 7 000 Hz.»; título «7 kHz audio-coding within 64 kbit/s»; G.722 (09/12) «In force»; enmienda 1 (10/14) «In force» |
| UIT-T G.712 (11/2001) | PDF del remate, texto; ficha web de la UIT | § 1 «PCM channels coded in accordance with ITU-T Rec. G.711»; § 5.2 pérdida de retorno «over the frequency range 300 Hz to 3400 Hz»; también «the telephone band covering the bandwidth 300 Hz to 3400 Hz»; G.712 (11/01) «In force» |
| EBU Tech 3326 Rev. 4 | `fuentes/canal-sur/sonido/EBU_Tech3326.txt` | § 3.1.3 (capa II): «Bitrates and sampling rates in bold are mandatory»; 192†, 256†, 384†; «†OPTIONAL for portable equipment»; § 3.3.4 «Adaptive Multi-Rate Wideband» (apoyo de la sigla WB en AMR-WB) |
| AES TD1008.1.21-9 | PDF descargado de aes.org y pasado a texto | Tabla 1: «Integrated loudness» en las filas Track-normalized, Album-loudest track e Interstitial |
| RFC 8216 | rfc-editor.org, texto | Primera frase de la finalidad; cabecera «Independent Submission» y «a contribution to the RFC Series, independently of any other RFC stream» (apoya «también autores independientes») |
| Apple, *Audio requirements* | web descargada y pasada a texto | «If a stereo audio source exists, it must be used.»; «vintage or field recordings»; «send the audio source with two identical channels for left and right»; «Both mono and stereo sources are accepted for MP3.»; «These bit rates apply to both the AAC and MP3 formats.»; tabla 1 (mono) 40–80 / 64–128 kbps, 2 (stereo) 80–160 / 128–256 kbps a 22.05/24 y 44.1/48 kHz |

## Resultado por pasaje

1. Siglas IETF/RFC: correcto (RFC 8216 es envío independiente a la serie RFC).
2. Tabla de MPEG capa II, dos salvedades: literales exactos; el † pertenece a la tabla de capa II.
3. Viñeta «Compatibilidad»: coherente con 2.
4. Tabla 1 de la AES: «Sonoridad integrada» en las tres filas, confirmado.
5. HLS: la cita acaba en la primera frase, con cierre correcto; la segunda frase sigue en su párrafo.
6. «Banda estrecha y banda ancha»: cifras, literales y título confirmados; no se atribuye banda a la
   G.711, sólo a la G.712 que la aplica. «Banda estrecha» es rótulo de oficio (ya estaba en el epígrafe).
7. «El formato de entrega»: literales y tabla de RSS confirmados.
8. Sigla WB: confirmada (G.722 y EBU Tech 3326 § 3.3.4).
9. Ficha, recomendaciones y trazabilidad: fechas y estado en vigor confirmados.

Antecedentes: «esa banda», «sus exigencias», «sus velocidades», «la tabla» tienen su referente en la
misma frase o la anterior.

## Corrección aplicada

- Ficha (Fuente): «G.722 y G.712 (bandas de la voz telefónica)» pasa a «(banda ancha y banda estrecha
  de la voz)». La G.722 no es de voz telefónica: su resumen habla de **«higher quality speech
  applications»**.

Ningún dato quitado. Cero errores de fondo en la ampliación.

## Otros ficheros tocados

Sólo el tema (línea 9) y este informe. Descargas (TD1008, página de Apple) en el scratchpad (`fb/`).
