# Realizador/a (puesto 33) · Tema 7 · Fase 3, verificación

Fecha de trabajo: 24-09-2026 (fecha del encargo; fuentes locales releídas en esta sesión).
Tema: `temas/canal-sur-especificos/33-realizador-a/07-monocamara-reportajes-promociones-microespacios.md`
(10.983 palabras según `indice.py`, 39 epígrafes; antes 10.920).

## Fuentes releídas

| Fuente | Fichero | Qué se ha comprobado |
|---|---|---|
| RD 1680/2011 (BOE-A-2011-19599; BOE núm. 302, de 16-12-2011) | `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` | Título y fecha; 0903 RA 1.b, 1.d, 4.b-4.g, 5 (enunciado), 5.a-5.c, 5.e; contenidos («una o varias cámaras», emplazamiento, plano secuencia/máster/cobertura, diálogo, claqueta, continuidad formal, partes de cámara); 0904 RA 5, 5.c, 5.e y «Operaciones de finales de edición» |
| RD 500/2024 (BOE-A-2024-10685) | `fuentes/canal-sur/realizador/BOE-A-2024-10685.txt` | Fecha (21 de mayo); art. séptimo.Uno (sólo módulos transversales); «Cuarenta» (anexo III de profesorado). 0903 y 0904 sólo aparecen en el anexo XLI. El redactor no lo había releído |
| INCUAL IMS077_3 (publicación: Orden PCI/797/2019) | `fuentes/canal-sur/realizador/incual-IMS077_3.txt` | Portada; UC0218_3 RP1 (CR1.1, CR1.6), RP2 (CR2.1-2.4), RP3 (CR3.1-3.4, errata «un vez»), pp. 10-11; MF0216_3 contenidos pp. 15 (tipología), 16 (autopromociones, ENG), 17 (multicámara y monocámara); MF0217_3 C1 CE1.1 p. 18; MF0218_3 C2 CE2.5, CE2.7 p. 22, C6 CE6.3 p. 23 |
| X Convenio RTVA, BOJA núm. 240, de 10-12-2014, anexo III | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | Fichas 5351000 (p. 196), 5353000 (p. 111), 5345100 (p. 129, «Diseñar y realizar y» [sic]), 5333301 (p. 131); búsqueda de «microespacio» y «promoci» en todo el convenio |
| Libro de Estilo, 1.ª ed., marzo de 2004 | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` (copia con ligaduras normalizadas en el directorio temporal) | 3.4 (pp. 47-48), 3.5 (p. 49), 3.5.1 (pp. 49-50), 3.17.1 a 3.17.1.5 (pp. 59-62), 3.17.2 (p. 62), 8.3.3 (p. 118). Páginas: el número va en la cabecera, al principio de cada página |
| Contrato-programa 2024-2026, BOJA núm. 245, de 26-12-2023 | `fuentes/canal-sur/documentos/contrato-programa-2024-2026-boja-245-2023.txt` | Cláusula tercera, rótulo de 3.1, punto 15, p. 40208/18 |
| Ley 13/2022 (consolidada, volcada el 24-09-2026) | `fuentes/canal-sur/BOE-A-2022-11311.md` y `.redacciones.tsv` | Sólo la vigencia: arts. 127, 128, 136, 137 y 138 con una sola redacción (2022). El texto de los artículos es copiado del común |

Todas leídas el 24-09-2026. Lentes: `negritas.py` con las siete fuentes: 168 cotejadas, 22 «no están»:
las de Mateu (sin volcado local, copiadas del común), «La música es un aditamento…» (copiada) y dos del
Libro de Estilo cortadas por salto de página (3.4 «Las posibilidades…», 3.17.1.5 «En caso de que…»),
cotejadas a mano: literales. `refutar_modo.py` (LGCA): 0. `refutar_exactitud.py` (LGCA): 4 «no
literales», todas falsos positivos (citas del Libro de Estilo 3.4 y 9.2.12.4 leídas como artículos 3 y
9). `refutar_prosa.py`: 0. `indice.py`: 39 epígrafes, índice correcto.

## Lo copiado: sólo comprobación de literalidad

- **Copiado del común** (tema 30/06): los once epígrafes extraídos de ambos ficheros y comparados con
  `diff`. Idénticos salvo lo declarado como adaptación: «(§ 4)» suprimido y «(art. 136.2, § 1)» →
  «en «Programa, bloques y publicidad», § 5»; remisiones de «La música» y «Documental y reportaje
  cultural»; párrafo final de «Estilos según el género». Las remisiones adaptadas apuntan a epígrafes
  que existen en el § indicado; el párrafo nuevo de «Estilos» es correcto (la condensación y la
  fragmentación del *spot* están en § 3, «La técnica»).
- **Copiado de RTVE sin cambios**: cotejo por script, frase a frase y celda a celda, sin negritas y
  sin caja, contra `temas/realizacion/06` y `temas/realizacion-tv/07`: todo lo listado es literal. El
  párrafo adaptado «La diferencia que más pesa…» es literal salvo la cláusula suprimida de la pregunta
  10, como se declara.

## Correcciones aplicadas

| # | Pasaje | Error | Antes → ahora | Fuente |
|---|---|---|---|---|
| 1 | Ficha, IMS077_3 | 9 | «actualización por Orden PCI/797/2019» → «publicación: Orden PCI/797/2019» | IMS077_3, p. 1 |
| 2 | Ficha, Normativa y Trazabilidad, LGCA | 9 | vigencia «a 25-09-2026» (fecha posterior a la del encargo, tomada del tema de origen) → «a 24-09-2026», comprobada en la tabla de redacciones | `.redacciones.tsv` |
| 3 | Siglas | 5 (a la inversa) | Se quitan CSRTV y RTVE: presentadas y nunca usadas | — |
| 4 | 1, La entrevista con una sola cámara | 6 | «repetiremos la pregunta…» → «sólo cuando sea preciso, repetiremos la pregunta…» | LE 3.17.1.4, p. 60 |
| 5 | 2, El reportaje entre los géneros | 9 | «la clasificación de oficio más extendida» → «clasificación de oficio, sin fuente publicada leída» | — |
| 6 | 2, Lo que el realizador traduce a plano | 9 | «el reportaje se graba casi siempre con una cámara» se marca «como oficio» | — |
| 7 | 2, íd., aplicación | 9 | «lo primero que se graba bien es a él: el Libro dice…» (el Libro habla del arranque del relato, no del orden de grabación) → el reportaje arranca con él (cita) y el realizador se asegura de tenerlo bien grabado | LE 3.4, p. 48 |
| 8 | 2, El falso directo, tabla | 9 | «Una entrevista o un programa» → «Una entrevista» (3.17 sólo habla de entrevistas); «sólo se corrigen defectos técnicos fáciles» se limita a la unidad móvil | LE 3.17.1.5, 3.17.2 |
| 9 | 3, Quién las realiza | 3 | «Otras dos tocan la promoción» → «Otras fichas… (también las de comunicación y relaciones públicas)»; se añade del Guionista «Idear campañas de corte publicitario para la promoción de imagen y programación de la cadena.»; «única que encarga realizar promociones» → «promociones de programas» | Convenio, anexo III (7100000, 7200000, 5333301) |
| 10 | 4, Cómo se realiza un microespacio; Aplicación 4 | 6 | Patrocinio «al principio y al final» → se añade el inicio de cada reanudación si hay interrupciones | LGCA 128.3.a |
| 11 | 5, La pieza terminada, aplicación | 9 | «la lista de músicas y autores… (la «declaración de autores» del CR3.4)» → la declaración de autores del CR3.4; su contenido no lo detalla la cualificación (lo de las músicas, oficio) | IMS077_3, CR3.4 |
| 12 | Aplicación 1 | 1 (antecedente) | «a su derecha» (ambiguo: la investigadora o la cámara) → «a la derecha de ella» (la cámara) | LE 3.17.1.3 |
| 13 | Trazabilidad, RD 500/2024 | — | «no releído» → releído; se concreta qué modifica | BOE-A-2024-10685 |

Además: extensión de la ficha 10.900 → 11.000. Releídos los pasajes cambiados: cada remisión tiene su
antecedente.

## Comprobado sin hallazgo

- RD 1680/2011: todas las citas en su módulo, RA y letra (0 cruzadas); «una o varias cámaras» y
  técnicas de grabación en contenidos de 0903; 0904 RA 5 con 5.c y 5.e.
- IMS077_3: CR y CE en su RP o C; páginas según la cabecera «N de 25».
- Convenio: cuatro códigos y páginas; la del Ayudante es la única ficha que nombra microespacios.
- Libro de Estilo: todas las citas, apartados y páginas; errata «un sola cámara» del original; 8.3.3
  en «Presencia en directo».
- Contrato-programa: punto 15, rótulo de 3.1 y página.
- Remisiones internas (§ 1-§ 5, temas 1, 2, 3, 8, 10-17): los epígrafes citados existen.

## Para la refutación

- Quedan como oficio declarado: definiciones de monocámara y microespacio, tabla de técnicas, tabla de
  géneros, motivos del falso directo (copiado de RTVE), estilos por género.
- La LGCA de la parte copiada se leyó en el común «el 25-09-2026», fecha posterior a la del encargo;
  aquí sólo se ha comprobado la vigencia (24-09-2026).

## Ficheros tocados

- Modificado: `temas/canal-sur-especificos/33-realizador-a/07-monocamara-reportajes-promociones-microespacios.md`.
- Creado: este informe. Copia normalizada del Libro de Estilo y copia previa del tema, en el directorio
  temporal de la sesión, fuera del repositorio. Ningún otro fichero.
