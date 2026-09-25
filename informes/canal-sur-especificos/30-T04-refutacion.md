# Puesto 30 · Tema 4 · Refutación (fase 4)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/04-formatos-de-video-y-audio.md`
(unas 13.700 palabras). No se corrige nada: sólo se informa.

Exactitud: se saltan «Copiado del común» y «Copiado de RTVE sin cambios» (lista en `30-T04-redaccion.md`).
Cobertura: el tema entero.

## Fuentes releídas (25-09-2026, sólo el pasaje citado)

UIT-R BT.601-7 (punto 6, 720/360; 4:3 y 16:9; Cometido «entrelazada»); BT.709-6 (introducción de la
parte 2 y tabla de sistemas); BT.2020-2 (nota 1 al cuadro 1, elección de cadencia, tabla 2, «10 or 12
bits»); BT.2100-3 (recommends, tabla 1 y nota 1b, submuestreo, tabla 9 y párrafo narrow/full);
Informe BT.2408-9 (§ 2, tabla 1, § 5 introducción y 5.1, escalado a 203 cd/m², § 5.2, «round-trip»);
SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023 y fichas de catálogo (259, 292-1, 424,
2082-1, 2084, 2086, 377-1, 2067-2); ST 2110-10:2022 (introducción y cl. 1), -20:2022 (cl. 1, 7.4-7.6),
-30:2025 (cl. 1 y 6) e índice de la familia; EBU R 128-2023 (h, l, m); AMWA AS-11; SMPTE IMF (ST 2067-2,
CPL, OPL, RDD 59-1).

## Hallazgos

| Nº | Gravedad | Error (de los nueve) | Pasaje | Qué dice el tema | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|---|
| 1 | Grave | 9 afirmación sin fuente / 6 salvedad omitida | § 11, «La interfaz digital serie», párrafo tras la tabla | «Cuanto más rápida la interfaz, más pérdida de cable admite el receptor a la mitad de la frecuencia de reloj: «20 dB to 30 dB» en la ST 259, «up to 30 dB» en la ST 424 y «up to 40 dB» en la ST 2082-1» | ST 292-1:2018, 8.1.10 (y alcance, lín. 91): receptores **«operating with input cable losses in the range of up to 20 dB at one-half the clock frequency»**. El HD-SDI, más rápido que el SD-SDI, admite menos (20 dB frente a 20-30 dB): la regla general es falsa. Además, en las cuatro normas son valores **típicos** («Typical loss amounts…», «are typical»), no un límite de lo que el receptor «admite» | Quitar la regla general; dar las cuatro cifras (incluida la de la ST 292-1, «up to 20 dB») como pérdidas típicas; conservar la conclusión de oficio (a más velocidad, menos alcance con el mismo cable) |
| 2 | Menor | 5 sigla mal presentada | § 2, cita de la BT.2020-2, glosa final | «LSDI es la presentación en pantalla grande» | BT.2020-2, lín. 129-134: **«large screen digital imagery (LSDI)»**, **«a system providing a display on a very large screen, typically for public…»** | «LSDI, *large screen digital imagery*: imagen digital en pantalla grande» |
| 3 | Menor | 9 literalidad de la cita | § 2, misma cita | «"being there"» (comillas rectas) | BT.2020-2, lín. 183: «“being there”» | Comillas de la fuente (el verificador ya lo hizo en «‘round-trip’» y «“Core Constraints”») |
| 4 | Menor | 6 salvedad omitida | § 11, viñeta de la ST 2110-20 | «con la regla de que, si no se declara, «receivers shall assume the value SDR» (§ 5)» | ST 2110-20:2022, 7.6: sigue «unless the sampling keyword indicates the signal is a KEY signal…» | Añadir «salvo en las señales de clave (§ 5)» o cerrar la cita con «[…]» |
| 5 | Menor | 9 (oficio impreciso) | § 7, «La cadencia en el montaje», 1.ª viñeta (y fila «Material del móvil» del supuesto) | «un clip a 29,97 en una secuencia a 25 salta o se repite cuadros, porque 25 no divide a 29,97» | Sin fuente (oficio). Al bajar de 29,97 a 25 sin mezcla de cuadros se descartan cuadros (unos 5 por segundo); la repetición es el caso inverso. «25 no divide a 29,97» es una formulación matemática impropia | «…se descartan cuadros (o se mezclan), porque las cadencias no son múltiplos» |

Todo lo demás del texto adaptado y nuevo se confirmó literal: BT.601-7 (720/360), BT.709-6 (cadencias,
P/PsF/I, 50/I «25 interlace», 25/PsF), BT.2020-2 (cuadro 1, cadencias, «Progressive», elección de
cadencia), BT.2100-3 (NOTE PQ/HLG, tabla 1, 1:1, nota 1b, 4:4:4/4:2:2/4:2:0, 64/940 y 256/3.760,
narrow/full), BT.2408-9 (todas las citas; tabla 1: 26/38/38 y 203/58/75), velocidades SDI y BNC 75 Ω,
estados y fechas de catálogo (2084: 16-08-2014; 2086: 2014-10-13 y 2018-04-09; 377-1: 2019-11-28;
2067-2: 2013, 2016, 2020-04-07; 259/292-1/424 «stabilized», 2082-1 «active»), títulos del índice
ST 2110 (-10 a -43), ST 2110-10/-20/-30 (alcances, 16f, ALPHA «for key signals», 48 kHz obligatorio y
44,1/96 kHz recomendables), R 128-2023 h), l) y m) con su salvedad, AS-11, IMF, CPL, OPL y RDD 59-1.
Cálculos rehechos: 1.037, 2.074 y 8.294 Mb/s; 20,7 y 8,6; 54.450 MB; 4 × 2.074 < 10.000.

## Cobertura del enunciado

Las doce rúbricas («resolución, compresión, HD, UHD, HDR, códecs, frame rate, bitrate, contenedores,
compresión, SDI/IP y estándares de entrega») tienen epígrafe propio y en el orden del enunciado; la
segunda «compresión» se resuelve como compresión en la cadena (§ 10). «Formatos de audio»: códecs
con y sin pérdida, LPCM 24 bits/48 kHz, WAV/BWF, 48 kHz en ST 2110-30 y R 128.

Preguntas (`30-T04-preguntas.md`): 12 enteras, 1 a medias, 2 no.

- **Laguna (pregunta 12)**: configuraciones de canales de audio (mono, estéreo, 5.1) y orden de pistas
  en el fichero de entrega. El § 12 nombra «pistas de audio y su orden» como parte de una ficha de
  entrega sin desarrollarlo. Se propone ampliar con fuente (p. ej. UIT-R BS.775 para 5.1, o la EBU R 123
  para la disposición de pistas, si se leen); si no se confirma, declararlo en «Lo que este tema no da».
- Pregunta 13 (no): no es laguna de cobertura sino consecuencia del hallazgo 1.
- Pregunta 7 (a medias): HDR10/HDR10+/Dolby Vision ya están declarados en «Lo que este tema no da»
  por falta de fuente normativa; no se cuenta como laguna.

## Lentes

Tema técnico sin norma jurídica: proceden sólo `refutar_prosa.py` e `indice.py`, ya pasados en
redacción y verificación (0 hallazgos; 61 epígrafes). No se re-ejecutan: el tema no ha cambiado desde
la verificación.

## Resumen

Graves: 1 · Menores: 4 · Lagunas: 1.

Ficheros tocados: creados `30-T04-preguntas.md` y este informe. El tema no se ha modificado.
