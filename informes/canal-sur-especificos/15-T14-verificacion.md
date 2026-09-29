# Grafista (puesto 15) · Tema 14 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/15-grafista/14-gestion-proyectos-graficos-briefing-propuesta-revision-aprobacion-calidad.md`.
Encargo fechado el 24-09-2026. Todas las fuentes se releyeron el 29-09-2026 (fecha del sistema).

## Fuentes releídas (29-09-2026)

| Fuente | Cómo | Resultado |
|---|---|---|
| X Convenio (BOJA 240/2014), volcado local | grep + lectura de las fichas 5301010 (p. 201), 5302010 (p. 125), 5345100 Grafista (p. 129), 5331000 Productor, 5351000 Realizador (p. 196) | Citas literales y páginas confirmadas; la ficha del Grafista no nombra *briefing*, aprobación ni calidad |
| Libro de Estilo (RTVA, 1.ª ed., marzo 2004), volcado local | 3.6.1, 4.4, 4.4.3, 4.4.4 puntos 1-6, con los marcadores de página | Todo literal; 3.6.1 en p. 50; 4.4 en p. 75; 4.4.4, puntos 1 a 6, en p. 77 (el punto 6 también: el marcador 78 va después). Hueco del redactor resuelto |
| Design Council, «The Double Diamond» y «Framework for Innovation» (descargadas de nuevo) | Cotejo automático de las 10 citas | 10/10 literales; cada cita, en la página que dice la Trazabilidad |
| *The Client Brief* (PDF de studiowide.co.uk, descargado de nuevo) | `documento.py texto` + cotejo de 26 fragmentos | Todos literales; encuesta de 2002 (más de 100 anunciantes y más de 100 agencias) confirmada; **el PDF tiene 12 páginas, no 10** |
| Frame.io V4 Knowledge Center, artículos 9105311, 9105251, 9101068 y 9952618, más la portada de frame.io | Cotejo de 20 citas y del contexto de las paráfrasis | 20/20 literales; «Manage Fields» = campos propios, confirmado; la titularidad de Adobe consta en la portada (© 2025 Adobe Inc.), no en los artículos |

## Pasajes que no se re-verifican (sólo se comprueba que sean literales)

- **Copiado del común.** De Montador 09: las dos viñetas de § 1 son idénticas a sus líneas 465-472 (diff limpio), y la frase de 4.4.4, punto 1, también es igual. De Realizador 13, en § 5 «El control de calidad de la UER»: el primer párrafo, la tabla de plantillas y las tres viñetas son idénticos a sus líneas 1265-1292 (diff limpio). La remisión «AS11 DPP (tema 8)» está bien: el tema 8 la desarrolla.
- **Copiado de RTVE sin cambios** (diseno-grafico/07): 34 pasajes o filas cotejados sin negritas ni ✔, y todos literales.

## Correcciones aplicadas

| # | Error | Dónde | Antes | Ahora |
|---|---|---|---|---|
| 1 | 9 | El Doble Diamante | «organismo británico de promoción del diseño», «el modelo de proceso más citado» | Cita literal de la fuente: **«the UK’s national strategic advisor for design»**; «un modelo de proceso muy difundido», que la cita de 2004 respalda |
| 2 | 9 | Revisar sobre la pieza | Frame.io, «muy extendida» | Se quita, porque no tiene fuente |
| 3 | 9 | Generar ideas | «en su formulación de oficio más repetida» | «que el oficio suele dar … (sin fuente leída)» |
| 4 | 9 | Aprobar tarde | «cuantifica el coste de cambiar el objetivo» | La encuesta mide cuántos están de acuerdo, no el coste. Se reescribe así |
| 5 | 6 | 5, Aplicado al grafismo | La cita de 3.6.1 aparecía como regla general | Se añade que el LE lo dice al tratar los titulares |
| 6 | 6 | Quién comprueba en la casa | Sólo las fichas de Emisiones y Continuidad | Se añade la ficha del Realizador (5351000, p. 196): **«…controlar la calidad y duración de los mismos.»**. Se ajusta la frase «dos veces» y se actualizan la tabla de Normativa y la Trazabilidad |
| 7 | 9 | Un estado, no un comentario | Reparto productor / realizador / grafista presentado como dato | Se marca como «lectura propia»: «criterio formal» no es literal de la ficha del Realizador |
| 8 | 3 | Trazabilidad | *The Client Brief*, «10 pp.» | «12 pp.» |
| 9 | 9 | Trazabilidad | Titularidad de Adobe sin fuente | Se añade la portada de frame.io (© Adobe Inc.) |
| 10 | 1 | Ficha, Fuente | LE, «capítulo 4.4» (el tema cita también 3.6.1) | «3.6.1 y 4.4» |

He releído los pasajes cambiados. «esa metodología» sigue teniendo delante su antecedente (el *design thinking*). No se ha quitado ningún dato. Extensión: unas 6.220 palabras de cuerpo, así que la ficha (6.300) sigue valiendo.

## Lentes

- `negritas.py` contra el convenio, el LE (con las ligaduras ﬁ/ﬂ normalizadas en una copia de trabajo), *The Client Brief*, las dos páginas del Design Council y los cuatro artículos de Frame.io: 74 negritas cotejadas. Las 15 que no aparecen son de tres tipos: las 11 de la UER, copiadas del común (nueve citas y los rótulos «File Package Compliance» y «File Structure Analysis»); 2 citas con «[…]» y 2 citas de un PDF a dos columnas (la de los ocho apartados y TIMINGS), que he comprobado a mano por partes; y ningún rótulo. No hay atribuciones cruzadas.
- `refutar_exactitud.py` y `refutar_modo.py` no se aplican: trabajan por artículo del BOE y el tema no cita ningún articulado (el convenio va por fichas y el LE es un documento). En su lugar he comprobado a mano el modo verbal de las citas del LE («se cursarán», «nunca se formularán», «es obligatorio») y la salvedad de 4.4 («Salvo razones infrecuentes y de extremada urgencia»), que está recogida como «salvo urgencia extrema».
- `refutar_prosa.py`: 0 hallazgos. `indice.py`: 30 epígrafes, índice correcto.

## Aviso al coordinador

- El informe de investigación C dice que el PDF de *The Client Brief* tiene 10 páginas; tiene 12.
- En el tema de Montador 09 (del común, no tocado), la viñeta «salvo urgencia extrema» parafrasea «Salvo razones infrecuentes y de extremada urgencia», y «peticiones a producción» parafrasea «peticiones a los productores». Está fuera de la cita, así que es correcto, pero no es literal.

## Ficheros tocados

- El tema 14 (correcciones de la tabla).
- Este informe (nuevo).
- Copias de trabajo de las fuentes en el directorio temporal de la sesión, fuera del repositorio.
