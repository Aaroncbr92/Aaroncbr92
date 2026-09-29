# Realizador/a (puesto 33) · Tema 7 · Fase 2, redacción

Fecha de trabajo: 24-09-2026. Tema: `temas/canal-sur-especificos/33-realizador-a/07-monocamara-reportajes-promociones-microespacios.md`
(10.920 palabras según `indice.py`, 39 epígrafes; `refutar_prosa.py`: 0 hallazgos).

Material: `33-investigacion-A-lenguaje-guion.md` (7.1, 7.2, F.7, I.4 y huecos 1), el tema cerrado
30/06 y los dos temas de RTVE de `realizacion.tsv` (fila 33/7, 30 %, sin actualizar). Releído en
`fuentes/` el 24-09-2026 todo lo que el tema cita fuera de lo copiado: RD 1680/2011 (0903 RA 1, 4, 5 y
contenidos; 0904 RA 5 y contenidos), IMS077_3 (UC0218_3 RP1-RP3; MF0216_3 contenidos; MF0217_3
CE1.1; MF0218_3 CE2.5, CE2.7, CE6.3), convenio (fichas 5351000, 5353000, 5345100, 5333301), Libro de
Estilo (3.4, 3.5, 3.5.1, 3.17.1 a 3.17.1.5, 3.17.2, 8.3.3) y Contrato-programa (3.1, punto 15).
`negritas.py` con esas fuentes (Libro de Estilo con ligaduras normalizadas): 165 negritas; las no
halladas son las de Mateu (sin volcado local, copiadas de 30/06), las copiadas de 30/06 que conservan
ligaduras y dos del Libro de Estilo cortadas por salto de página (3.4 «Las posibilidades…» y 3.17.1.5
«En caso de que…»): comprobadas a mano, son literales.

## Decisiones

- Páginas del INCUAL corregidas sobre la investigación: los marcadores «Página N de 25» van al
  principio de cada página, así que CE1.1 de MF0217_3 está en la p. 18 y la tipología de programas
  en la p. 15.
- La investigación decía que la del Ayudante es la ficha que nombra promociones: es la única que
  encarga realizarlas, pero el Grafista (5345100) y el Guionista (5333301) también nombran
  promoción/autopromociones. Se citan las dos.
- Falso directo: RTVE lo trata como práctica neutra y remite a su manual de estilo. Se sustituye esa
  parte por el Libro de Estilo, que lo rechaza en la presencia en directo (8.3.3: «debe erradicarse»;
  «Si el directo es falso, lo haremos constar») y lo admite como técnica de grabación sin
  interrupciones (3.17.1.5 y 3.17.2). Tabla de los dos sentidos.
- Reportaje: la tabla de RTVE dice que puede contener «criterios subjetivos del autor»; el Libro de
  Estilo (3.4) le da margen de visión pero «no debe incurrir en opiniones subjetivas». Se dejan las dos
  y se dice cuál manda en Canal Sur.
- Microespacio: sin definición publicada (DLE inaccesible, según la investigación) ni duración. La
  definición del tema es de oficio y se declara; no se da duración.
- Plano máster, cobertura y plano secuencia: el RD los nombra; definiciones y tabla de técnicas son
  oficio declarado.
- Se quitan de RTVE las referencias a preguntas y cuadernillos (pregunta 10 del decorado circular, 58,
  53) y el aviso sobre «el manual de estilo de la Corporación».
- Montaje, efectos, mezcla y revisión técnica de calidad: tema 13; aquí sólo documentos, decisión y
  entrega.

## Copiado del común

De `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/06-montaje-de-programas-promociones-cultura-deportes-digital.md`
(cerrado), extraídos por líneas con `sed` (literales al carácter):

- «### Del vídeo informativo al programa»: entero (en § 2).
- «### Qué es una autopromoción»: entero (§ 3).
- «### Lo que la ley exige a la promoción montada»: entero salvo dos remisiones, que son adaptación y
  sí se verifican: se quita «(§ 4)» tras «las sobreimpresiones de las retransmisiones deportivas», y
  «(art. 136.2, § 1)» pasa a «(art. 136.2, en «Programa, bloques y publicidad», § 5)».
- «### La técnica: *spot*, tráiler, *teaser* y *sneak peek*»: entero (§ 3).
- «### Promoción e información: el criterio de la casa»: entero (§ 3).
- «### El patrocinio»: entero (§ 3).
- «### Quién dirige el montaje: las fichas del convenio»: entero (§ 5).
- «### Programa, bloques y publicidad: lo que la ley exige al montaje»: entero (§ 5).
- «### Estilos según el género»: rótulo, primer párrafo y tabla. El párrafo final se reescribe
  (adaptado, se verifica).
- «### La música»: entera salvo la remisión «(§ 1)», que pasa a «(«Del vídeo informativo al
  programa», § 2)».
- «### Documental y reportaje cultural»: literal salvo dos remisiones («del § 1 (3.4)» → «del epígrafe
  «Del vídeo informativo al programa» (3.4)»; «(tabla del § 1)» → «(tabla de «Estilos según el
  género», § 5)»).

## Copiado de RTVE sin cambios

Palabras sin tocar; sólo se han quitado negritas de énfasis y las mayúsculas de énfasis
(«REPORTAJE», «EN EL LUGAR DE LOS HECHOS»). Comprobado por script (normalizando negrita y caja) contra
los dos ficheros.

`temas/realizacion/06-lenguaje-tecnico-y-narrativo.md`, § 14:
- «Son dos oficios distintos que comparten vocabulario.» y la tabla «Una cámara / Multicámara» entera
  (en «Una cámara y multicámara»). Adaptado (se verifica): el párrafo «La diferencia que más pesa…»,
  al que se quita «, y por eso el decorado circular de la pregunta 10 es un problema de plató y no de
  montaje».

`temas/realizacion-tv/07-generos-y-formatos.md`:
- § 3: «Los géneros informativos se distinguen por tres cosas…», la tabla de géneros y «La distinción
  que atraviesa la tabla…» (en «El reportaje entre los géneros informativos»).
- § 4: «Es propio del reportaje televisivo la profundización de la noticia…» (sin la frase de la
  pregunta 58); «Las tres cosas que caracterizan el reportaje televisivo…» y su lista (en «Lo que el
  realizador traduce a plano»).
- § 5: «Cuando en un informativo un redactor hace un «falso directo»…» (sin la frase de la pregunta
  53); «Qué es exactamente, y por qué se llama así…»; «Por qué se hace, y son razones de producción:»
  y la tabla de motivos (en «El falso directo»).

## Ficheros tocados

- Creado: `temas/canal-sur-especificos/33-realizador-a/07-monocamara-reportajes-promociones-microespacios.md`.
- Creado: este informe.
- Ficheros de trabajo en el directorio temporal de la sesión (extractos y copia normalizada del Libro
  de Estilo), fuera del repositorio. Ningún otro fichero del repositorio modificado.

## Diez preguntas de tribunal, contestadas con el tema

| # | Pregunta (rúbrica) | Respuesta | Dónde | ¿Entera? |
|---|---|---|---|---|
| 1 | En la realización con una sola cámara, ¿quién corta y cuándo se decide el plano? (monocámara, teoría) | El montador, después; el plano se decide en el rodaje y otra vez en el montaje | 1, Una cámara y multicámara | Sí |
| 2 | Práctica: entrevista para emisión íntegra grabada con una sola cámara. Según el Libro de Estilo, ¿qué se graba en el segundo recorrido? (monocámara) | Las preguntas del entrevistador con un plano idéntico, planos de escucha de uno y otro, y recursos para la edición | 1, La entrevista con una sola cámara | Sí |
| 3 | Con dos o más cámaras ENG independientes, ¿qué debe prever el realizador según el Libro de Estilo? (monocámara/ENG) | Planos técnicamente compatibles y uniformes y código de tiempo idéntico | 1, Dos o más cámaras ENG | Sí |
| 4 | Según el RD 1680/2011 (0903), ¿qué recoge el informe del día de grabación? (monocámara, norma de enseñanza) | Validez de las tomas, acciones y decisiones, incidencias y modificación del plan, con nuevas órdenes de trabajo | 1, Lo que el realizador hace en la grabación; 5, tabla de documentos | Sí |
| 5 | ¿Cuánto no debe superar un reportaje en un espacio diario según el Libro de Estilo, y por dónde se empieza si la historia se cuenta a través de un personaje? (reportajes) | Tres minutos (sugerencia); es obligatorio comenzar por el personaje | 2, Del vídeo informativo al programa; El reportaje en el Libro de Estilo | Sí |
| 6 | ¿Qué dice el Libro de Estilo de Canal Sur del falso directo en la presencia en directo? (reportajes/piezas) | Debe erradicarse; si no se puede, se revisa el formato, y si el directo es falso se hace constar | 2, El falso directo | Sí |
| 7 | Según la LGCA, ¿computa la autopromoción en el límite de minutos de publicidad, y qué la convierte en anuncio? (promociones) | No computa (art. 137.2.b); los mensajes o locuciones ajenos a la programación o a sus productos derivados (art. 127.2) | 3, Lo que la ley exige a la promoción montada | Sí |
| 8 | Práctica: llega el anuncio de una campaña para ilustrar una noticia sobre ella. ¿Qué permite el Libro de Estilo? (promociones) | No montarlo con el mismo orden y estructura; sólo como recurso, parcial y limitado; si es creación artística, al final del informativo, sin titulares | 3, Promoción e información | Sí |
| 9 | Según el convenio, ¿quién realiza microespacios y promociones de programas, y qué microespacios manda emitir el Contrato-programa 2024-2026 y para qué colectivos? (microespacios) | El Ayudante de Realización, bajo las directrices del Realizador; divulgativos sobre herramientas tecnológicas para la alfabetización informacional, sobre todo para jóvenes, mayores y residentes en el ámbito rural | 3, Quién las realiza; 4, Los microespacios del Contrato-programa | Sí |
| 10 | Según la IMS077_3, ¿qué recoge el parte de emisión de una pieza destinada a emitirse dentro de un programa, y con qué documentación se entrega el soporte final? (piezas postproducidas) | Códigos de entrada y salida, duración, coleos y pies; parte de emisión, declaración de autores e incidencias | 5, La pieza terminada | Sí |

Resultado: diez de diez enteras. No hizo falta ampliar el tema.
