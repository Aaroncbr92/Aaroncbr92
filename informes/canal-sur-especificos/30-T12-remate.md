# Puesto 30 · Tema 12 · Remate

Fase 5 · Rematar. Fecha de trabajo y de lectura de fuentes: 25-09-2026 (el encargo fija «hoy» en
24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/12-edicion-para-redes-y-plataformas.md`.
Entrada: `30-T12-refutacion.md` y `30-T12-preguntas.md`.

## Comprobación en la fuente (25-09-2026)

| Hallazgo | Fuente releída | Resultado |
| --- | --- | --- |
| 1 · −14 LUFS como inferencia | `resolve21-extractos/render.txt` p. 4187 («normalize the clip’s audio level to YouTube’s standard»); `meters.txt` p. 4140 («the YouTube target LUFS specification is -14 LUFS») | Confirmado: aplicado |
| 2 · TikTok «fija» 1920 × 1080 | `render.txt` p. 4188 («two different resolutions»; «Resolution: 1920x1080 HD») | Confirmado: aplicado |
| 3 · Vimeo/Dropbox | `render.txt` pp. 4187-4189 (Vimeo: «Visible To … password protection»; Vimeo, TikTok y Dropbox «Encoding Profile: Auto») | Confirmado: aplicado. Matiz: el preajuste de Dropbox está en la p. 4189, no en la 4188; se corrige el rango a pp. 4187-4189 |
| Laguna 1 · sacar un rango como fichero | `render.txt` p. 4211 (Mark In/Out, teclas I y O, barra naranja, «You cannot render partial clips in Individual Clips mode…») y p. 4196 (Single Clip / Individual Clips) | Confirmado: se amplía el tema |

## Pasajes cambiados

1. **§ 2 «Relación de aspecto»**, párrafo final: «que fija 1920 × 1080» → «que ofrece dos resoluciones
   en un desplegable (el manual cita **«Resolution: 1920x1080 HD»**)».
2. **§ 6 «Los preajustes…»**, entradilla: «pp. 4187-4188» → «pp. 4187-4189».
3. **§ 6, tabla de preajustes**: fila TikTok con «dos resoluciones en un desplegable» y «Encoding
   Profile: Auto»; fila «Vimeo 720p/1080p/2160p y Dropbox 720p/1080p/2160p» con «Encoding Profile:
   Auto», cadencia de la línea de tiempo y, en Vimeo, título, descripción y «Visible To» con contraseña.
4. **§ 6, viñeta «Sonoridad»**: se dice que el capítulo de exportación no da la cifra, que el de
   medidores la da al explicar el objetivo de los medidores, y que unir ambos es deducción, no frase del
   manual.
5. **Supuesto, paso 7**: «normaliza a −14 LUFS según el fabricante» → «normaliza al “estándar de
   YouTube”, que el mismo fabricante cifra, en el capítulo de medidores, en −14 LUFS».
6. **§ 3, nuevo epígrafe «Sacar el clip como fichero»** (ampliación, unas 250 palabras): marcar
   entrada y salida (I/O, Mark In/Mark Out), modos Single Clip e Individual Clips (p. 4196), aviso de
   que no se renderizan clips parciales en Individual Clips (p. 4211), y que los preajustes de redes
   renderizan un solo clip (pp. 4187-4189). Remite al tema 3.
7. **Índice**: nueva entrada del epígrafe. **Trazabilidad**: manual de Resolve con pp. 4196 y 4211 y
   epígrafe 3. **Ficha**: extensión 8.400 → 8.800 palabras (indice.py: 8.880).

Relectura de antecedentes: «ese nivel», «el mismo fabricante», «el manual» y «esos dos pasajes» tienen
delante su referente en cada pasaje cambiado.

## Preguntas

- 10 (a medias) → **entera** con el nuevo epígrafe de § 3.
- 15 (Reels): no se toca; hueco declarado sin fuente oficial legible. No se recorta la pregunta.

## Lentes

- `indice.py`: 8.880 palabras, 37 epígrafes, índice regenerado.
- `refutar_prosa.py`: 1 hallazgo (frase repetida «en DaVinci Resolve 21 (manual de referencia, cap.»),
  corregido; segunda pasada: 0.
- Lentes de normas (`negritas.py`, `refutar_exactitud.py`, `refutar_modo.py`): no se corren; ningún
  pasaje cambiado cita normas.

## Ficheros tocados

El tema y este informe.

¿Amplió? **Sí** (epígrafe «Sacar el clip como fichero»): toca fase 5 bis sobre el pasaje 6.
