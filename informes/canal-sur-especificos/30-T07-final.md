# Puesto 30 · Tema 7 · Revisión final (fase 5 bis)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/07-postproduccion.md`.
Alcance: sólo los pasajes que cambió el remate (`30-T07-remate.md`), sacados por `diff` contra la copia
previa `30t07-antes-remate.md` del scratchpad.

## Fuentes releídas (25-09-2026)

| Fuente | Qué |
|---|---|
| *DaVinci Resolve 21 Reference Manual* (PDF, metadatos 09-07-2026), cap. 58, pp. 1254-1266, y cap. 56, p. 1214 | Directamente en el PDF (PyMuPDF), página a página; el extracto `speed.txt` coincide con el PDF en todo lo cotejado |
| UBU, *Guía para elaborar Material Multimedia Accesible* (PDF y txt), pp. impresas 4-7 | La numeración impresa va en la cabecera: p. 4 = PDF 8, p. 5 = PDF 9, p. 6 = PDF 10, p. 7 = PDF 11 |

## Cotejo de los pasajes cambiados

| # remate | Pasaje | Resultado |
|---|---|---|
| 1 | Guías *Social Media* (p. 1214) | Literal y página correctos |
| 2 | Paso 4, paréntesis sobre la UNE 153010 | Correcto (el título de la norma, en la guía, es de subtitulado para personas sordas) |
| 3 | Siglas: UNE | **Corregido**: «la sigla con la que se numeran las normas españolas» no está en la guía (afirmación sin fuente, error 9). Queda: «la sigla que llevan las normas que la guía … cita como publicadas por AENOR (la guía no desarrolla ninguna de las dos siglas)». La guía sólo da «norma UNE …» y «AENOR … Madrid: AENOR» |
| 4, 5 | Tabla de normativa; «no se ha leído» | Correctos |
| 6 | Criterios de subtitulado: pausas, tipografía, información contextual (pp. 4 y 6), mayúsculas, cursiva, números, signos (p. 5), efectos sonoros (p. 6); incoherencia p. 5/p. 6; tabla de ocho colores, uso por personajes (p. 5); orden color-etiquetas-guiones (p. 6) y mantener color y guiones sólo con riesgo de confusión (p. 7) | Todos los literales y páginas correctos. Antecedente de «Ese orden» (tabla de colores) y de «La guía no es del todo coherente» (tabla de criterios), en su sitio |
| 7 | «Los efectos de tiempo» | Definición (p. 1254), *Change Clip Speed*, *Speed %*, *Retime Controls* Comando-R, *Fit to Fill*, *Reverse Speed*/*Reverse Segment*, flechas a la izquierda, *Freeze Frame* Mayúsculas-R, dos puntos de velocidad (p. 1259), suavizado, rampas y rebobinado (p. 1260), curvas *Retime Frame* con marcha atrás (p. 1263) y *Retime Speed* sin ella (p. 1264), triángulos amarillos/azules (p. 1258), audio y *muted* (p. 1254), *Retime Process* en *Master Settings* / *Frame Interpolation* y en el inspector, tres literales y límite del flujo óptico (p. 1265), modos *Standard*/*Enhanced*/*Speed Warp* con *Neural Engine* y «isn't always the best choice» (pp. 1265-1266), línea de tiempo de cadencia mixta (p. 1265; el tema 3 la trata): correctos. **Tres correcciones**: (a) rango de la entrada de la tabla «pp. 1254-1261» → «pp. 1254-1264», porque la fila de velocidad variable cita hasta la p. 1264; (b) *Pitch Correction* «en cambios grandes suena peor» → «puede no sonar tan bien» (el manual: «may not sound as good», error 4 de modo); (c) cuenta propia: «el movimiento da tirones» no está en la fuente → «(es el método que el manual llama menos sofisticado)», que sí está («least sophisticated», p. 1265). Antecedentes de «El flujo óptico tiene su límite» y «El mismo proceso», en su sitio |
| 8, 9, 10 | «Qué se puede preguntar», Trazabilidad, ficha | Correctos; la extensión (13.500 aprox.) cuadra con las 13.656 medidas |

El remate no se equivocó en lo que corrigió; los cuatro ajustes son de pasajes nuevos.

## Pendiente fuera de alcance

«La norma española de subtitulado …» (§ 5, primera línea del epígrafe) no la cambió el remate y no se
ha tocado; la guía no llama «española» a la norma. Queda para quien retome el tema.

## Lentes

`indice.py`: 13.656 palabras, 50 epígrafes, índice sin cambios. `refutar_prosa.py`: 0 hallazgos.

## Ficheros tocados

El tema y este informe.

## Adenda (relanzamiento de la fase 5 bis, 25-09-2026)

La fase 5 bis ya estaba hecha (arriba). No se repite entera para no pisar sus ajustes. Comprobado en el
tema que siguen los cuatro: siglas «no desarrolla ninguna de las dos siglas» (l. 34), «pp. 1254-1264»
(l. 483), «puede no sonar tan bien» (l. 495) y «menos sofisticado» (l. 514); fuera «se numeran las
normas españolas», «suena peor» y «da tirones». El pendiente fuera de alcance («La norma española de
subtitulado») lo cerró la adenda de la verificación (`30-T07-verificacion.md`): «La norma de
subtitulado para personas sordas que cita la guía es la UNE 153010:2012 (AENOR)».

Recotejo de muestra contra `speed.txt` (Resolve 21, cap. 58, releído el 25-09-2026): definición y
audio *muted* (p. 1254), corrección de tono Linux/Windows sin, Mac con (p. 1254), *may not sound as
good* (pp. 1255-1256), *Project Settings* / *Frame Interpolation* / inspector, *Nearest*, *Frame
Blend* (útil cuando el flujo óptico deja defectos), *Optical Flow* y su límite (p. 1265), modos
*Standard*/*Enhanced*/*Speed Warp* con *Neural Engine* e *isn't always the best choice*
(pp. 1265-1266): todo cuadra. Antecedentes de «El flujo óptico tiene su límite» y «El mismo proceso»,
en su sitio. Cero hallazgos nuevos.

Ficheros tocados: sólo este informe.
