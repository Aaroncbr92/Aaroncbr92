# Puesto 30 · Tema 8 · Refutación (fase 4)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). No corrige: sólo señala.
Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/08-ingesta-digitalizacion-transferencia-verificacion-copias-metadatos-archivo.md`.
Preguntas: `30-T08-preguntas.md`.

## Alcance

Exactitud: todo lo «Escrito nuevo» y lo «Adaptado de RTVE» de `30-T08-redaccion.md`, más los pasajes
cambiados en la verificación. Se saltan los 11 bloques «Copiado del común» (Cámara T07) y los
«Copiados de RTVE sin cambios», como manda el encargo. Cobertura: el tema entero contra el enunciado.

## Fuentes releídas (25-09-2026)

| Fuente | Qué se cotejó |
|---|---|
| X Convenio RTVA, BOJA 240, ficha 5212206 (txt, ll. 6815-6837) | Objeto literal; las ocho tareas; las cinco citadas, literales |
| Libro de estilo 2004 (txt) | 5.3.3 «Otra norma elemental…» literal; 9 «ASUNTOS COMPROMETIDOS», 9.9 «Material objetable», 9.9.1 literal con su contexto |
| Resolve 21, `mediapool.txt` (pp. 373-374) | *Clone Tool*: «One of the few things…», varios destinos, informe en la raíz, las seis opciones y sus textos, MD5 128 bits, XXHASH64 |
| Resolve 21, `metadata.txt` (pp. 417-420, 434) | Todas las citas y sus páginas (marcas `[[pNNN]]`); «automatically matching…» está al final de p. 434 |
| Resolve 21, `tape.txt` (pp. 558-564) | Todas las citas y páginas: DPX/QuickTime y códecs (p. 561), «from 2 to 16», «at minimum» con la comilla desparejada, 00086400.dpx «based on the ingest frame rate» (p. 562), *Log Clip*/offline tape clips y orden por *Reel No* (p. 563), EDL (p. 563) y regla de no duplicar (p. 564) |
| Adobe, «Ingest and proxy workflows in Premiere» | Título, «Last updated on Jan 7, 2026» y las cuatro citas |
| EBU Tech 3293 v. 1.10 | Abril 2020; p. 3 (dos citas); p. 7 (cinco citas); § 2.1 (definición, «Dublin Core for media», «living specification»); § 2.3 «What is new in EBUCore 1.10» (IMF) |
| CCSDS 650.0-M-3 | § 1.1 (objeto, definición de OAIS, «Open», alcance, p. 1-2); § 1.6.2 (Long Term, SIP, AIP, DIP, PDI y cinco clases, Provenance, Reference + nota ISBN, Fixity); § 4.2.2 «six functional entities»; rótulos 4.2.3.3-4.2.3.8; § 4.2.3.3 QA; § 4.2.3.4 Replace Media («should not be altered»), Error Checking, Disaster Recovery |
| lto.org roadmap (`lto-roadmap.txt`, procedencia curl/WebFetch) y `ltfs.txt` | Todas las citas; la llamada (*) va en la frase de la velocidad, como dice el tema |
| Catálogo SMPTE RP 210 | «withdrawn» |

Cálculo: 12 GB × 8 = 96 Gb = 96.000 Mb ÷ 100 Mb/s = 960 s = 16 min. Correcto.

## Hallazgos de exactitud

**Graves: 0. Menores: 0.** Todas las citas nuevas son literales y están en la página o el apartado
que se dice; las afirmaciones de oficio van declaradas como tales; las correcciones de la
verificación (LTO, 9.9.1, *may want*, *should not be altered*, EDL) están bien aplicadas.

Observación (no hallazgo; decide el remate): la ficha tiene una sexta tarea que roza los metadatos,
**«Etiquetar, grabar e introducir en base de datos, la información para la emisión automatizada de
programas y bloques publicitarios.»** El tema dice «Cinco de sus ocho»; es defendible dejarla fuera
porque su objeto es la emisión automatizada (tema 13), pero podría nombrarse en una línea.

## Cobertura del enunciado

Las siete rúbricas («Ingesta, digitalización, transferencia, verificación, copias de seguridad,
metadatos y archivo») tienen epígrafe propio, en el orden del enunciado, con teoría y aplicación.
Preguntas: 13 enteras, 1 a medias, 1 no.

- **Laguna 1 (pregunta 14, «no»)**: metadatos en Premiere. El tema desarrolla los de Resolve y de
  Premiere sólo dice que tiene «columnas de metadatos»; no nombra XMP, el esquema en que Adobe
  escribe los metadatos de fichero, y los temas 3 y 15 tampoco. Es preguntable para un montador. En
  `fuentes/canal-sur/montador/web/` sólo aparecen los rótulos del menú de la ayuda de Adobe
  («Edit XMP metadata», «Link clip data to XMP metadata»), no su contenido: el remate tendría que
  descargar esa página de ayuda y ampliar § 6 «Los metadatos en el programa de edición» con lo que
  diga, o declarar el hueco en «Lo que este tema no da».
- **A medias (pregunta 15)**: la capacidad nativa de la LTO-10. Ya está declarada como hueco (la
  página no la da en texto); no es laguna nueva. Si el remate encuentra una fuente del programa LTO
  con la cifra nativa, se completa; si no, se deja como está.

## Resumen

Graves 0 · menores 0 · lagunas 1 (XMP en Premiere). Ampliación: Opus, sólo § 6 y, si procede,
«Lo que este tema no da».

Ficheros tocados: `30-T08-preguntas.md` y este informe (nuevos). El tema no se ha tocado.
