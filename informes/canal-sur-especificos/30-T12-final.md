# Puesto 30 · Tema 12 · Fase 5 bis (revisión de los pasajes del remate)

Fecha de trabajo y de lectura de fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/12-edicion-para-redes-y-plataformas.md`.
Alcance: sólo los siete pasajes que lista `30-T12-remate.md`.

Fuentes releídas (25-09-2026): `fuentes/canal-sur/montador/resolve21-extractos/render.txt`
(cap. 187, pp. 4187-4189, 4196, 4211) y `meters.txt` (cap. 182, p. 4140).

## Pasaje por pasaje

| # | Pasaje | Comprobación | Resultado |
| --- | --- | --- | --- |
| 1 | § 2, «Relación de aspecto», párrafo final | p. 4188: «two different resolutions», «Resolution: 1920x1080 HD», «Use Vertical Resolution… portrait mode» | Citas exactas. **Corregido**: el texto afirmaba que el preajuste entrega 1080 × 1920; el manual no da las medidas del fichero vertical (error 9). Se reescribe: el preajuste «va por ahí», se cita «in portrait mode» y se declara que el manual no escribe esas medidas |
| 2 | § 6, entradilla «pp. 4187-4189» | Marcadores de página: Social Media Presets abre en p. 4187; Dropbox en p. 4189 | Correcto |
| 3 | § 6, tabla (TikTok; Vimeo y Dropbox) | p. 4188 TikTok: desplegable de dos resoluciones, casilla vertical, «Frame rate: The chosen frame rate of your timeline», MP4, H.264, «Encoding Profile: Auto», AAC; título, «Visible To», comentarios, Duet, Stitch. pp. 4187-4189 Vimeo y Dropbox: MP4, H.264, «Encoding Profile: Auto», AAC, «at the timeline’s frame rate»; Vimeo, título, descripción, «Visible To… including password protection» | Correcto. Matiz sin corregir: el manual rotula «Dropbox or Dropbox Replay 720p/1080p/2160p»; la tabla abrevia a «Dropbox» sin alterar ningún dato |
| 4 | § 6, viñeta «Sonoridad» | p. 4187 «Normalize Audio… to YouTube’s standard.»; p. 4140 (entre el marcador [[p4140]] y el pie 4140) «DaVinci Resolve’s default loudness standard target is -23 LUFS, but the YouTube target LUFS specification is -14 LUFS.» | Citas y página exactas; la deducción se declara como tal. «qué nivel es ése» y «esa cifra» tienen antecedente |
| 5 | Supuesto, paso 7 | Mismas fuentes | Dato correcto. **Corregido** el antecedente: «el mismo fabricante» no tenía delante un fabricante nombrado en el paso; pasa a «Blackmagic Design, en el capítulo de medidores del mismo manual» |
| 6 | § 3, «Sacar el clip como fichero» (ampliación) | p. 4211: «To define a continuous range of clips to render», tecla I/«Mark In», tecla O/«Mark Out», regla de la línea de tiempo, barra naranja, campos In/Out/Duration, aviso «IMPORTANT: If you’re in Individual Clips mode…» (literal). p. 4196: «all clips in the session are output together, as a single media file», «the selected range», «each clip is rendered as an individual media file» (la elisión […] sustituye a «is rendered»: correcta). pp. 4187-4189: los cuatro preajustes «renders a single clip» | Datos y citas correctos. **Corregido** en la entradilla: «explica cómo se saca sin duplicar el proyecto ni exportar la pieza entera para recortarla después» atribuía al manual un propósito que no escribe (error 9); pasa a «explica cómo se renderiza sólo un rango de la línea de tiempo». «Para sacar un total de 40 segundos… Single Clip» es consecuencia directa del aviso de la p. 4211: se mantiene. «ya trabajan así» y «el tema 3» (exportación, enunciado punto 3) tienen antecedente |
| 7 | Índice, Trazabilidad, ficha | Índice con la entrada nueva; Trazabilidad «cap. 182, p. 4140; cap. 187, pp. 4187-4190, 4196 y 4211», epígrafes 2, 3, 4 y 6 | Correcto |

## Correcciones aplicadas (3)

1. § 2: se quita que el preajuste de TikTok entregue 1080 × 1920; se cita «in portrait mode» y se declara el hueco.
2. § 3, entradilla del epígrafe nuevo: se quita el propósito atribuido al manual.
3. Supuesto, paso 7: antecedente de «el mismo fabricante».

## Lentes

- `refutar_prosa.py`: 0 hallazgos.
- `indice.py`: 8.886 palabras, 37 epígrafes (la ficha dice 8.800 aproximadamente: vale).
- Lentes de normas: no aplican; ningún pasaje revisado cita normas.

## Ficheros tocados

El tema y este informe.

---

# Segunda ronda (pasajes del segundo remate)

Fecha de trabajo y de lectura de fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Alcance:
sólo los cuatro pasajes de la segunda ronda de `30-T12-remate.md`.

Fuentes releídas (25-09-2026): `fuentes/canal-sur/montador/web/redes/youtube-ayuda-15424877.txt`
(l. 38), `youtube-ayuda-72431.txt` (ll. 93-102) y `youtube-ayuda-6375112.txt` (ll. 15-19).

| # | Pasaje | Comprobación | Resultado |
| --- | --- | --- | --- |
| 1 | § 6 «Música y reclamaciones…», 1.ª viñeta | l. 38: «Puedes usar cualquier canción disponible en la Biblioteca de audio de Shorts. Además, … limitadas a 60 o 30 segundos.» y «no recibirá ninguna reclamación de derechos de autor» | Literal, completo y bajo «Canales estándar de YouTube» (el tema dice «canales estándar»). La salvedad queda recogida. Correcto |
| 2 | § 2 «Relación de aspecto», viñeta 4K-8K | l. 19, bajo «Nota:» tras la lista de resoluciones: «En el 2022, empezamos a retirar … contenido en 5K.» | Literal. «empezamos» remite a YouTube, cuya página se cita en el mismo epígrafe; «2160p (4K)» y «4320p (8K)» están en la viñeta anterior. Correcto |
| 3 | § 4 «Lo que no se puede poner», final del 1.er párrafo | l. 101: mismo párrafo que «Un canal puede subir un número limitado…»; cita literal con las comillas rectas de la fuente | Literal. «el aviso» tiene delante el límite diario; «la página» es la de miniaturas (answer 72431), citada en el epígrafe y en Trazabilidad. Correcto |
| 4 | Ficha, «Extensión» 8.900 | Recuento del remate: 8.971 palabras | Coherente con «aproximadamente». Correcto |

## Correcciones aplicadas

Ninguna (0 hallazgos).

## Ficheros tocados

Sólo este informe (se añade la segunda ronda; la primera queda como estaba).
