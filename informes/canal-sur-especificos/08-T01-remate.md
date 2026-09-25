# Puesto 08 · Tema 1 · Fase 5 · Remate

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/01-camara-sensores-opticas-exposicion.md`
(≈9.800 → 10.731 palabras según `indice.py`; ficha: «10.700 palabras aproximadamente»). Entrada:
`08-T01-refutacion.md` (6 hallazgos + 2 lagunas) y `08-T01-preguntas.md` (12 enteras, 1 a medias, 2 no).
Sólo leídos del método: `ENCARGO.md` y el enunciado del puesto 08.

**¿Amplía contenido nuevo? Sí**: dos subepígrafes nuevos («El extensor», «El balance de negros») y
párrafos nuevos con fuente en montura y LUT. Toca fase 5 bis sobre los pasajes listados abajo.

## Fuentes leídas (todas el 24-09-2026)

| Fuente | Copia local |
|---|---|
| Sony, *PXW-Z200/HXR-NX800 Help Guide*, 5-060-574-13(1) | `fuentes/fabricantes/Sony_PXW-Z200_help-guide.txt` (ya existía) |
| Sony, *PXW-X400 Operating Instructions*, 4-587-873-13(1), © 2015 (descargado de utopiacam.com; el PDF de pro.sony devolvió «Access Denied») | `fuentes/fabricantes/Sony_PXW-X400_operating-instructions.txt` (nuevo, texto con `documento.py`) |
| Fujifilm, «4K Portable Lenses», ficha UA22x4.8BERD (fujifilm.com/au) | `fuentes/fabricantes/Fujinon_UA22x4.8_especificaciones.txt` (nuevo, extracto literal) |
| FUJINON, página «Support», preguntas frecuentes (fujinon.com/support) | `fuentes/fabricantes/Fujinon_FAQ-soporte_extractos.txt` (nuevo, extracto literal) |

## Hallazgos: comprobación y decisión

1. **SDI y LUT (grave)** — Comprobado en el Z200 Help Guide («[Shooting] – [LUT On/Off]»): «[SDI/HDMI]
   (PXW-Z200 only) [LUT On] / [LUT Off] … Selects whether to apply a monitor LUT to the SDI and HDMI output
   video», de fábrica [LUT Off], «Configurable in log shooting mode»; y [LCD/VF/Proxy/Stream] igual.
   **Aplicado.** Quitado «La salida SDI lleva la misma señal logarítmica… La interfaz es un transporte, no un
   procesador»; nuevo párrafo con las citas; la tabla pasa a «Lo que se ve en el visor o en la salida».
2. **180° y 1/50** — Es cuenta, no dato de fuente: ángulo/360 × duración del cuadro. Coherente con la cita
   Blackmagic ya en el tema (25→50 cuadros, abrir de 180° a 360°). **Aplicado** como párrafo «Ojo con esa
   equivalencia…» tras la cita de EBU Tech 3335; declarado como oficio en «Trazabilidad».
3. **B4 = prisma de tres sensores** — No se encuentra fuente que ligue B4 con prisma, ni que lo niegue.
   **Aplicado quitando la subordinada** («detrás de la cual va el bloque de prisma de tres sensores»).
4. **Adaptación por brida «nunca»** — La FAQ de FUJINON confirma las dos mitades: un adaptador puede montar
   físicamente un objetivo de brida corta en cuerpo de brida larga pero «it won’t focus to the sensor», y
   existen «B4 to PL mount expanders» con «between 1 and 1½ stops less light». **Aplicado**: «con un simple
   anillo…», más las dos citas.
5. **Círculo de confusión en los factores de la PdC** — **Aplicado**: línea tras la tabla y matiz en el
   punto 1 del razonamiento sensor-PdC («lista de factores físicos»).
6. **Residuos de examen y repeticiones** — **Aplicado**: fuera «la palabra que decide es "binario"…»; la
   justificación del distractor «obturación» en la hiperfocal queda en una frase (se conserva el dato: la
   obturación no influye); «La ganancia es el último recurso» ya no repite el orden de mandos, remite a él.
7. **Laguna: extensor** — Ampliado con fuente: ficha Fujifilm («Extender 2x», «[1x] 4.8-106mm», «[2x]
   9.6-212mm», ángulos a 106 y 212 mm, «1:1.8 (4.8-61mm) 1:3.15 (106mm)»), FAQ FUJINON («a 2x conversion
   will reduce the light falling on the sensor by two stops») e indicador «EX» de la X400. Nuevo
   `### El extensor` tras «El diafragma y el número f». La pregunta 14 se contesta entera.
8. **Laguna: balance de negros** — Ampliado con la X400 (conmutador AUTO W/B BAL, cuándo hacerlo, cuándo no,
   «black set and black balance», diafragma cerrado automáticamente, «NG: Iris not Closed», no «During
   recording», se conserva en memoria). El orden negros → blancos **no lo impone el manual**: se dice como
   oficio. Añadido que la Z200 no documenta balance de negros automático y sí [Master Black], [R Black],
   [B Black] (Help Guide, «[Paint/Look] – [Black]»). Nuevo `### El balance de negros` al final de «Balance
   de blancos». La pregunta 15 se contesta entera; su opción b («objetivo tapado/diafragma cerrado, antes del
   de blancos») queda cubierta con la salvedad de que el orden es oficio.

Preguntas tras el remate: 15 enteras (10, 12, 14 y 15 pasan a entera). Ninguna pregunta recortada.

## Pasajes cambiados (para la fase 5 bis)

- Ficha: «Fuente» (añade X400, ficha y FAQ de FUJINON) y «Extensión» (10.700).
- Siglas/rótulos: añadido ***NG*** a la lista de rótulos de la máquina.
- «Qué se puede preguntar»: + extensor y balance de negros.
- Índice (regenerado con `indice.py`): + «El extensor», + «El balance de negros».
- «Del fotón al número»: último párrafo recortado.
- **Nuevo** «El extensor» (Ópticas).
- «La profundidad de campo»: párrafo nuevo tras la tabla.
- «El círculo de confusión y la distancia hiperfocal»: final recortado.
- «El tamaño del sensor y la profundidad de campo»: punto 1.
- «La montura y la distancia de brida»: segundo y tercer párrafo reescritos.
- «La obturación»: párrafo nuevo «Ojo con esa equivalencia…».
- «Las curvas logarítmicas y el visor»: cabecera de tabla y párrafo SDI/LUT.
- **Nuevo** «El balance de negros» (Balance de blancos).
- «La ganancia es el último recurso»: reescrito.
- «Trazabilidad»: tres filas nuevas y dos añadidos a «Oficio sin norma detrás».

Releídos: cada «ese», «el mismo UA22x4.8BERD», «la X400», «esa equivalencia», «esa pérdida» tiene su
antecedente en el mismo párrafo o el anterior.

## Lentes

Tema técnico sin norma: `indice.py` (índice regenerado, 54 epígrafes, 10.731 palabras) y
`refutar_prosa.py`: 1 hallazgo, «PUB» sin presentar en la ficha y «Trazabilidad» (código de publicación
del manual Canon, *PUB. DIE-0559-000B*; preexistente, es parte de la referencia, no una sigla; no se toca).
Las siglas nuevas «MK» y «NG» se resolvieron (cita recortada con […] y rótulo declarado).

## Otros ficheros tocados

`fuentes/fabricantes/Sony_PXW-X400_operating-instructions.txt`,
`fuentes/fabricantes/Fujinon_UA22x4.8_especificaciones.txt`,
`fuentes/fabricantes/Fujinon_FAQ-soporte_extractos.txt` (nuevos) y este informe. Los cambios sin confirmar
que `git status` muestra en los temas 02, 05, 09 y 15 no son míos.
