# Realizador/a (puesto 33) · Tema 2 · Fase 3, verificación

Fecha de trabajo: 24-09-2026 (fecha del encargo; fuentes locales releídas en esta sesión).
Tema: `temas/canal-sur-especificos/33-realizador-a/02-guion-escaleta-planificacion.md` (9.562 palabras
según `indice.py`, 30 epígrafes).

## Fuentes releídas

| Fuente | Fichero | Qué se ha comprobado |
|---|---|---|
| RD 1680/2011 (BOE-A-2011-19599, texto original; BOE núm. 302, de 16-12-2011) | `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` | Art. 4; módulo 0902 (RA 3 y 3.b-3.h, 4.b, 4.c, 4.f, 4.g, 5.d, 5.f, 7.a-7.f, contenidos); módulo 0904 (RA 1.b-1.f, 2 y 2.a-2.g, 3.d-3.g, 4 y 4.a-4.g, 5.a, contenidos); módulo 0905 (RA 1 y 1.b-1.g). Nombres de los tres módulos |
| RD 500/2024 (BOE-A-2024-10685) | `fuentes/canal-sur/realizador/BOE-A-2024-10685.txt` | Art. primero.Dos.a) (el RD 1680/2011 está en el grupo a); art. séptimo.Uno (módulos transversales); «Cuarenta» (anexo III sustituido); nota de afectados: arts. 2, 10, 12, 15 y anexos I y III (el art. 4 no se toca) |
| INCUAL IMS077_3 (publicación: Orden PCI/797/2019) | `fuentes/canal-sur/realizador/incual-IMS077_3.txt` | Ámbito profesional; ocupación «Ayudantes de realización»; UC0216_3 CR1.2, 1.3, 1.5, 3.5, 4.4, 5.1, 5.4; UC0217_3 CR1.2, 1.5; UC0218_3 CR1.1; MF0216_3 C5, CE5.1-5.3 |
| X Convenio RTVA, BOJA núm. 240, de 10-12-2014 | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | Disposición adicional segunda (p. 86): centros, «a título enunciativo», escaleta técnica, cuatro trabajadores/as rotatorios |
| Libro de Estilo, 1.ª ed., marzo de 2004 | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` | Cap. 6 (p. 88), 6.1, 6.1.1, 6.1.2 (pp. 88-89), 6.3 (p. 91), 3.9.1 (p. 53), índice del cap. 3; recuento 8 + 6 + 5 |

Todas leídas el 24-09-2026 (según el encargo). `negritas.py` con las cuatro fuentes: 100 negritas, 12
«no están», las mismas 12 de la redacción; revisadas a mano: son ligaduras (ﬁ, ﬂ) y guiones del PDF
(‐), la cita con comillas ‘ ’ y los tres rótulos del común; todas literales una vez normalizadas.
`refutar_modo.py`: 0. `refutar_exactitud.py`: no aplica (no hay volcado .md con articulado; 0
comprobadas). `refutar_prosa.py`: 0. `indice.py`: correcto.

## Lo copiado: sólo comprobación de literalidad

- **Copiado del común** (tema 30/09, «Qué es, en el Libro de Estilo» y «Tres reglas obligatorias»):
  `diff` contra el tema cerrado, idéntico salvo el párrafo nuevo del recuento, que sí se ha
  verificado (8 elementos, 6 acotaciones, 5 del parte: cuadra con LE 6.1).
- **Copiado de RTVE sin cambios**: cotejo frase a frase contra los cuatro temas de RTVE (sin
  negritas). Literal todo lo listado; las únicas diferencias son supresiones declaradas de
  referencias al examen («y el examen pregunta por las dos», «que es donde este temario la usa de
  verdad», «la pregunta 19/41», «El punto 4.6 del anexo…»). Nada añadido.

## Correcciones aplicadas

| # | Pasaje | Error | Antes → ahora | Fuente |
|---|---|---|---|---|
| 1 | Advertencia, art. 4 | 6 salvedad omitida | «define la competencia del título como» → «incluye en la competencia general», con la mención de espectáculos en vivo y eventos | RD 1680/2011, art. 4 |
| 2 | Ficha, IMS077_3 | 9 | «actualización por Orden PCI/797/2019» → «publicación: Orden PCI/797/2019» (es lo que dice el documento) | IMS077_3, p. 1 |
| 3 | 1, documentos intermedios | 9 | «Qué significa que el argumento sea el primer documento plenamente literario» presuponía una afirmación sin fuente → presentado como secuencia de oficio | — (oficio) |
| 4 | 2, «Qué añade al literario» | 1 cita cruzada (contradicción interna) | «Es el guion de trabajo de realización» → «Es el guion de realización». Es pasaje de RTVE sin cambios, pero choca con el propio tema: el RD distingue guion técnico y guion de trabajo (0902 RA 3.g; 0905 RA 1). **Se tocó un pasaje de la lista «RTVE sin cambios»: manda la fuente** |
| 5 | 3, escaleta técnica | 9 | «Lo que el convenio mete en la escaleta técnica coincide con lo que dice la cualificación» → la DA 2.ª pone esas tareas junto a la escaleta; con CR1.3 sólo comparte luz, transiciones y rótulos (CR1.3 no nombra movimientos de cámara ni cabeceras) | Convenio DA 2.ª; UC0216_3 CR1.3 |
| 6 | 3, tres escaletas del RD | 9 | «tres momentos de la escaleta de un programa» → «tres escaletas» (la de continuidad es de la emisión diaria, RA 5.a) | 0904 RA 1.e, 2, 5.a |
| 7 | 3, «Lo que cuelga» | 8 | «en la preproducción» → «en la preparación»: RA 4.g (autocúe) no es del RA 3 de preproducción | 0904 RA 3, 4.g |
| 8 | 4, análisis de contenidos | 1 | «El género y los objetivos» con cita sólo de RA 1.b (el género es 1.a) → «Los objetivos» | 0904 RA 1.a-1.b |
| 9 | 4, planificación de cámaras | 9 | «las instrucciones y la planta de cámaras son del realizador» (CR1.5 no lo dice) → instrucciones recibidas, y la cualificación sitúa el trabajo bajo órdenes del realizador | UC0216_3 CR1.5; ámbito profesional |
| 10 | 4, estructura de un programa | 9 | Se atribuía al LE «bloques» y los formatos «pieza, directo» y la tesis «decisión narrativa» → LE 6.1 (formato en escaleta) y géneros del cap. 3 (reportaje, declaraciones o totales, colas, colas + total); la tesis, como oficio | LE 6.1; índice cap. 3 |
| 11 | 4, señales grabadas | 9 | Las glosas de máster, señal limpia y cámaras dobladas se declaran de oficio | 0905 RA 1.f (sólo la lista) |
| 12 | Trazabilidad | 1 | IMS077_3 «competencia general» → «ámbito profesional» (ahí está «siempre bajo las órdenes…»); LE añade cap. 3; RD 500/2024 añade art. primero.Dos.a); fila de oficio añade la secuencia de documentos intermedios | fuentes citadas |

Además: reflujo de líneas de la cita de UC0217_3 CR1.5 (formato, sin cambio de texto).

## Comprobado sin hallazgo

- Todas las citas del RD en su módulo y letra (0 cruzadas): 0902 3.b (cinco fases), 3.c, 3.d, 3.e,
  3.f, 3.g (cuatro documentos), 3.h, 4.b, 4.c, 4.f, 4.g, 5.d (*cover set*), 5.f, 7.a-7.f; 0904 1.b-1.f,
  2, 2.a-2.g, 3.d-3.g, 4.a-4.g, 5.a y los contenidos citados; 0905 1, 1.b (seis datos), 1.c-1.g (tres
  señales). Recuentos del tema (cinco fases, cuatro documentos, cuatro cosas por bloque, seis datos,
  seis elementos de la planificación, tres criterios, ocho operaciones del enunciado): cuadran.
- IMS077_3: CE5.1 es de informativo y CE5.2-5.3 de ficción y variedades (cuatro plantas), en MF0216_3 C5.
- Convenio: p. 86, cinco centros, «a título enunciativo», cuatro trabajadores/as, rotatorio.
- LE: páginas 53, 88, 89, 91 según los saltos del PDF; edición «Primera edición, Marzo de 2004».
- RD 500/2024: la descripción de los módulos transversales de la «Normativa» es exacta para el grupo a).
- «Orden de realización»: 0 apariciones en las cuatro fuentes; el hueco declarado se mantiene.

## Para la refutación

- La teoría del guion (tipos de conflicto, *beat*, focalización, proporciones del paradigma) queda
  como oficio sin fuente publicada, declarado en el tema; tras quitar las atribuciones de RTVE no hay
  manual que la sostenga.
- Extensión 9.562 palabras frente a las 9.500 de la ficha: sin cambio.

## Ficheros tocados

- Modificado: `temas/canal-sur-especificos/33-realizador-a/02-guion-escaleta-planificacion.md`.
- Creado: este informe. Ninguno más.
