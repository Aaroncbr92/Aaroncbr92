# Puesto 28 · Operador/a de Sonido · Tema 9 · Fase 5 bis

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/09-grabacion-edicion-y-postproduccion.md`.
Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Revisados sólo los pasajes 6 a 9
de `28-T09-remate.md` (las ampliaciones); las correcciones 1 a 5 no son objeto de esta fase.
Ficheros tocados: el tema (una línea) y este informe.

## Fuente releída

Avid, *Pro Tools Reference Guide* 2025.12 (PDF de resources.avid.com, © 2025; copia local y su
`.txt` descargados el 25-09-2026), leída el 25-09-2026 en: cap. 2 «Pro Tools Concepts» (líneas 6692-6710 del texto extraído),
cap. 13 «Tracks» (p. 298-299), cap. 22 «Sample Rate Conversion Quality» y «Bit Depth Conversion and
Dither» (p. 628-629) y «Export Clips as Files» (p. 640), cap. 52 «Dither» (p. 1464-1465), cap. 56
«Using Dither» y «Sample Rate Conversion and Bit Depth Reduction» (p. 1593-1594).

## Comprobación, dato a dato

| Pasaje | Dato | Resultado |
|---|---|---|
| 6 | Enumeración «audio, Auxiliary Input, … and video tracks» | Literal, cap. 13, p. 298 |
| 6 | Citas de audio, auxiliar, máster, VCA («control, group, or offset…», «do not pass audio»), MIDI, carpeta de encaminamiento | Literales, p. 298-299 |
| 6 | Máster también para submezclas; VCA gobierna un grupo de mezcla; instrumento MIDI + audio | Conformes (p. 298) |
| 6 | Mono/estéreo/multicanal, 3 a 8 canales, Ultimate y Studio; tipos que lo admiten | Conforme, p. 299 («from 3 to 8 channels») |
| 6 | Vídeo como imagen de referencia; aplicación a la sesión | Marcado como oficio: correcto |
| 7 | Definición, «quiet passage or a fade-out», «very low-level random noise», «trade-off…» | Literales, p. 1464 |
| 7 | *Noise shaping* «(around 4 kHz)…» | Literal, p. 1465 |
| 7 | «When mixing down to a 16-bit destination…», también en sesión de 16 bits | Literal/conforme, p. 1593 |
| 7 | Casos sin *dither* | **Salvedad omitida (error 6)**: faltaba el destino analógico con interfaz de 24 bits (p. 1594). Corregido |
| 7 | Último proceso en el máster, inserciones posfader; truncado en *Bounce Mix* | Conforme/literal, p. 1594 |
| 7 | *Dither* automático al exportar fragmentos y al importar a menos bits | Conforme: p. 640 y p. 629; y cap. 52, p. 1465 |
| 7 | Cinco calidades SRC «Low … Tweak Head», más calidad más tiempo | Literal, p. 628 |
| 7 | Orden SRC a 24 bits y luego reducción con *dither* | Literal, p. 1594 |
| 7 | Caso 48/24 a 44,1/16 | Aplicación correcta de la regla |
| 8 | Cuña, paso 3: remisión al epígrafe | El epígrafe existe con ese título |
| 9 | Portada, siglas VCA/MIDI/SRC, «Qué se puede preguntar», «Lo que este tema no da», fila de Trazabilidad | Conformes; los capítulos y páginas citados coinciden con la guía |

## Antecedentes

«Su guía de referencia» sigue a «Pro Tools, de Avid»; «Esos artefactos» sigue a «quantization
artifacts»; «sus inserciones» tiene delante «la pista máster»; «esas reglas» del caso, las del epígrafe.
Todos con antecedente.

## Corrección aplicada (comprobada en la fuente)

Epígrafe «Reducir la resolución y cambiar la frecuencia», segunda viñeta: «ni al mezclar hacia un
destino de 24 bits» → «ni al mezclar hacia un destino de 24 bits o hacia un destino analógico con
una interfaz de 24 bits» (p. 1594: «When mixing down to an analog destination with any 24-bit capable
interface, do not use a dither plugin on the main output.»).

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 60 epígrafes, 11.646 palabras (Extensión de la portada,
11.600, sigue valiendo).

## Resultado

Un hallazgo (error 6), corregido. El resto de lo ampliado, confirmado en la fuente.
