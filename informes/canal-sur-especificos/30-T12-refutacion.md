# Puesto 30 · Tema 12 · Refutación

Fase 4 · Refutar (no corrige). Fecha de trabajo y de todas las lecturas: 25-09-2026 (el encargo fija
«hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/12-edicion-para-redes-y-plataformas.md`.

Se saltan en exactitud, según `30-T12-redaccion.md`: «Copiado del común» (§ 1 de «El servicio
público digital» a «Multiplataforma…», líneas 107-185; LGCA 2.18 en § 3; Manual de RTVE 4.1, 4.3.2-4.3.3
en § 3; LGCA 2.13, 2.20 y 86-93.1 en § 6; «Conservar lo publicado…») y «Copiado de RTVE sin cambios»
(identificador, listas de reproducción, FTP). La cobertura mira el tema entero.

## 1. Exactitud: lo releído en la fuente

| Pasaje | Fuente releída (25-09-2026) | Resultado |
| --- | --- | --- |
| § 1 «Dónde se ve hoy…»; § 5 | `fuentes/canal-sur/montador/web/redes/reuters-dnr-2026-executive-summary.txt` (48 mercados, 54/51 %, 77 %, −5 pp, 43/34/26/20 %, «less than two minutes», «differs markedly», 27 %) | Literales ✓ |
| § 2 relación de aspecto y resoluciones | `youtube-ayuda-6375112.txt` | Literales ✓ |
| § 2 Shorts; § 6 música y Content ID | `youtube-ayuda-15424877.txt` (15-10-2024, cuadrada o vertical, tres minutos; 90/60/30 s; 24-09-2026) | Literales ✓ |
| § 4 miniaturas (tabla, 4:5, políticas, 30 días, límite diario) | `youtube-ayuda-72431.txt` | Literales y bien resumidas ✓ |
| § 6 codificación, tasas SDR, audio, entrelazado, BT.2020 → BT.709 | `youtube-ayuda-1722171.txt` | Literales ✓ |
| § 2 cap. 41 p. 860; cap. 127 p. 3119 | `resolve21-extractos/timelines.txt`, `scopes.txt` | Literales y bien paginados ✓ |
| § 6 cap. 182 p. 4140 | `meters.txt` | Literal ✓ (ver hallazgo 1) |
| § 4 y § 6 cap. 187 pp. 4187-4190 | `render.txt` | Literales ✓ (ver hallazgos 2 y 3) |
| § 4 art. 9 LGCA; § 6 art. 101.1.g) | `fuentes/canal-sur/BOE-A-2022-11311.md` | ✓ |
| § 6 LAA 31.1.i) por remisión | tema 11 del puesto, § 5 | ✓ |
| Cálculos de reencuadre (3413; 32 %; 608) | cálculo | ✓ |

## 2. Hallazgos

Ninguno grave. Tres menores:

1. **Supuesto, paso 7 (líneas 698-700), y § 6 «Sonoridad» (líneas 550-553)** · error 9 (inferencia
   presentada como dato del fabricante). El paso 7 dice que «el preajuste de YouTube de Resolve
   normaliza a −14 LUFS según el fabricante». El manual no lo dice: el preajuste normaliza **«to
   YouTube’s standard»** (cap. 187, p. 4187), y en otro capítulo (cap. 182, p. 4140), al hablar del
   objetivo de los medidores, afirma que **«the YouTube target LUFS specification is -14 LUFS»**. La
   unión de ambos es deducción. En § 6 la frase «Qué nivel es ése lo dice el mismo fabricante» tiene
   el mismo matiz. Propuesta (paso 7): «sabiendo que el preajuste de YouTube de Resolve normaliza al
   “estándar de YouTube”, que el mismo fabricante cifra, en el capítulo de medidores, en −14 LUFS».
2. **§ 2, líneas 240-241, y § 6, tabla de preajustes, fila TikTok (línea 538)** · error 6. El tema
   dice que el preajuste de TikTok «fija 1920 × 1080». El manual: **«A dropdown menu lets you choose
   two different resolutions to render to»**, y en la lista de parámetros **«Resolution: 1920x1080
   HD»** (p. 4188). Propuesta: «ofrece dos resoluciones en un desplegable; el manual cita 1920 × 1080
   HD, con una casilla para entregarlo en vertical».
3. **§ 6, tabla de preajustes, fila «Vimeo y Dropbox» (línea 539)** · error 6 leve. En «Opciones
   propias» sólo pone «Subir directamente»; para Vimeo el manual añade título, descripción y
   **«Visible To»** (con protección por contraseña) (p. 4188). Además, el perfil de codificación
   de Vimeo, TikTok y Dropbox es **«Encoding Profile: Auto»**, frente al **«High»** del de YouTube,
   que la tabla sólo recoge para YouTube. Propuesta: «Subir directamente (Vimeo: título, descripción
   y visibilidad, con contraseña); perfil de codificación automático».

## 3. Cobertura del enunciado

«Formatos verticales, clips, miniaturas, ritmo y distribución multiplataforma»: cada rúbrica tiene su
epígrafe y aplicación práctica. Huecos declarados en «Lo que este tema no da» (especificaciones de
TikTok, Instagram y Facebook; zonas que tapa cada interfaz; reencuadre automático de Premiere; guía de
Canal Sur): correctos y honestos.

**Laguna 1 (ampliable, fuente ya en el repositorio).** El tema dice qué es un clip y cómo debe ser,
pero no cómo se saca en el programa de edición un fragmento como fichero aparte. El manual de
DaVinci Resolve 21 (cap. 187, p. 4211) lo explica: se marcan entrada y salida (teclas I y O, o
*Mark In*/*Mark Out* en la regla de la línea de tiempo) y se renderiza ese rango; **«You cannot
render partial clips in Individual Clips mode, but you may do so in Single Clip mode.»** Propuesta:
una viñeta en § 3 «Qué es un clip» o en § 6 «Un máster, muchas salidas», con remisión al tema 3.
Pregunta 10 de `30-T12-preguntas.md`: a medias.

## 4. Preguntas

`30-T12-preguntas.md`: 15 preguntas (9 T, 6 P). 13 enteras, 1 a medias (laguna 1), 1 no (Reels de
Instagram: hueco declarado, sin fuente oficial legible; no se propone ampliar).

## 5. Avisos

- La ficha dice «8.400 palabras aproximadamente»; el fichero tiene hoy unas 8.950 (`wc -w`, con
  marcas). No es error del enunciado.
- Sigue en pie el aviso de redacción y verificación para el tema 7 (guías de redes en «cap. 56,
  p. 1214» frente a cap. 127, p. 3119). No se ha comprobado aquí.

## Ficheros tocados

Sólo `30-T12-preguntas.md` y este informe. El tema no se ha modificado.

---

# Segunda ronda (fase 4 repetida sobre el tema rematado)

Fecha de trabajo y de lectura: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema en su estado
actual (commit b08a902; sin cambios en el árbol; 9.327 palabras con marcas). No corrijo. Se saltan en
exactitud, como en la primera ronda, lo «Copiado del común» y lo «Copiado de RTVE sin cambios»
(`30-T12-redaccion.md`); la cobertura mira el tema entero.

## Exactitud: releído en la fuente (25-09-2026)

| Pasaje | Fuente | Resultado |
| --- | --- | --- |
| § 2 relación de aspecto, relleno, barras, resoluciones | `youtube-ayuda-6375112.txt` (entera) | Literales ✓ |
| § 2 Shorts; § 6 música y Content ID | `youtube-ayuda-15424877.txt` (entera) | Literales ✓ (menor 1) |
| § 4 miniaturas | `youtube-ayuda-72431.txt` (entera) | Literales ✓ (laguna 1) |
| § 6 codificación, tasas, audio, BT.709, BT.2020 | `youtube-ayuda-1722171.txt` (entera) | Literales ✓ |
| § 1 y § 5, DNR 2026 | `reuters-dnr-2026-executive-summary.txt`, líneas 36-46, 238 | Literales ✓ |
| § 2, § 3, § 4, § 6: Resolve 21 caps. 41, 127, 182, 187 (pp. 4187-4190) | `timelines.txt`, `scopes.txt`, `meters.txt`, `render.txt` | Literales y paginados ✓; los tres menores de la primera ronda, bien resueltos en el remate y la fase 5 bis |
| § 4 art. 9 LGCA; § 6 art. 101.1.g) | `BOE-A-2022-11311.md` | ✓ |

Graves: ninguno.

Menores (1):

1. **§ 6 «Música y reclamaciones», primera viñeta · error 6 (salvedad omitida).** La cita arranca en
   «puedes usar la mayoría de las canciones durante un máximo de 90 segundos…», pero la página la
   precede de **«Puedes usar cualquier canción disponible en la Biblioteca de audio de Shorts.
   Además,»**. Sin esa frase, el límite de 90/60/30 s parece la única regla. Propuesta: citar la
   frase completa desde «Puedes usar cualquier canción…».

Observación sin hallazgo: la ficha dice «8.800 palabras aproximadamente»; `indice.py` contó 8.886 en
la fase 5 bis. Vale.

Lentes: `refutar_prosa.py`, 0 hallazgos. Las lentes de norma no proceden: lo que cita norma es copiado
del común o remisión.

## Cobertura

Las cinco rúbricas del enunciado (formatos verticales, clips, miniaturas, ritmo, distribución
multiplataforma) tienen epígrafe propio, en su orden, y el supuesto las recorre. La laguna de la
primera ronda (sacar un rango como fichero) está cubierta en § 3 «Sacar el clip como fichero».

Lagunas (2, leves, fuente ya leída y citada):

1. **Límite diario de miniaturas** (pregunta 6, a medias). La página dice qué hacer: **«Si aparece un
   mensaje de error que dice "Límite de miniaturas personalizadas diarias superado" al intentar subir
   una miniatura, inténtalo de nuevo pasadas 24 horas.»** (answer 72431). Una frase en § 4 «Lo que no
   se puede poner».
2. **Resoluciones entre 4K y 8K** (pregunta 9, no). **«En el 2022, empezamos a retirar la
   compatibilidad con la reproducción en resoluciones de entre 4K y 8K. Por ejemplo, es posible que
   ya no se pueda reproducir contenido en 5K.»** (answer 6375112). Una frase tras la lista de
   resoluciones de § 2.

## Preguntas

`30-T12-preguntas.md`, segunda ronda: 15 (8 T, 7 P). 13 enteras, 1 a medias, 1 no.

## Ficheros tocados

Ampliados: este informe y `30-T12-preguntas.md` (sección «Segunda ronda»). El tema no se ha tocado.
