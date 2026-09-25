# Puesto 30 · Tema 8 · Remate (fase 5)

Fecha: 25-09-2026 (encargo fechado 24-09-2026).
Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/08-ingesta-digitalizacion-transferencia-verificacion-copias-metadatos-archivo.md`.
Entradas: `30-T08-refutacion.md` (graves 0, menores 0, 1 laguna, 1 observación) y `30-T08-preguntas.md`
(13 E, 1 M, 1 N).

**Amplía contenido nuevo: sí** (subepígrafe XMP en § 6). Procede la fase 5 bis sobre los pasajes 1 y 2.

## Fuentes leídas en el remate (25-09-2026)

| Fuente | Cómo | Guardada en |
|---|---|---|
| Adobe, «XMP (Extensible Metadata Platform)», developer.adobe.com/xmp/docs (= README de github.com/adobe/xmp-docs) | curl, HTML a texto | `fuentes/canal-sur/montador/web/xmp-adobe.txt` |
| Adobe, «XMP Dynamic Media namespace» (adobe/xmp-docs, `XMPNamespaces/xmpDM.md`) | curl raw | `.../web/xmp-dm.txt` |
| Adobe, «Dublin Core namespace» (adobe/xmp-docs, `XMPNamespaces/dc.md`) | curl raw | `.../web/xmp-dc.txt` |
| LTO Program, «LTO Generation Compatibility Details», lto.org/lto-generation-compatibility/ | curl, HTML a texto | `.../web/lto-compatibility.txt` |
| X Convenio RTVA, ficha 5212206 (`documentos/x-convenio-rtva-boja-240-2014.txt`, ll. 6812-6837) | relectura | — |

**No se pudo leer**: la ayuda de Premiere sobre metadatos (helpx.adobe.com, «Edit XMP metadata»,
«Link clip data to XMP metadata», «Metadata in Premiere»): 403 de Akamai por curl y WebFetch;
web.archive.org cortó la conexión y archive.org respondió 429. Lo que esas páginas dicen (datos de
clip en el proyecto frente a XMP en el fichero, enlace entre ambos) **no se ha escrito**: sólo se
conocía por resúmenes del buscador, que no son fuente. Queda declarado como hueco. lto.org/lto-10/
devolvió un captcha (202).

Todas las citas nuevas se cotejaron por programa contra los ficheros guardados: literales (la de
ISO 16684-1 lleva en la fuente un enlace sobre «ISO standard (16684-1)»; el texto es el mismo).

## Decisiones sobre la refutación

1. **Laguna pregunta 14 (XMP en Premiere)**: aplicada ampliando el tema, sin tocar la pregunta. Con
   el tema nuevo, la pregunta 14 queda **entera** (b, XMP: § 6, «Los metadatos de fichero de Adobe:
   XMP»; la propiedad `xmpDM:altTapeName` se fija desde Premiere).
2. **Pregunta 15 (capacidad nativa LTO-10)**: se buscó fuente. La página de compatibilidad da
   cartuchos de 30 TB y 40 TB, pero no los califica de nativos; no se afirma que lo sean. Se añade la
   cita y se reescribe el hueco. Sigue **a medias** en la parte «nativa».
3. **Observación (sexta tarea de la ficha)**: comprobada literal en el convenio; se nombra en una
   línea y se remite al tema 13 (que tiene «La emisión automatizada»). El «Cinco de sus ocho» se
   mantiene, ahora con la sexta dicha.

## Pasajes cambiados (texto nuevo)

1. **§ 6, subepígrafe nuevo «Los metadatos de fichero de Adobe: XMP»** (tras «Los metadatos en el
   programa de edición»): definición de XMP, qué recoge, ISO 16684-1, extensible (cuatro citas de
   Adobe); tabla de los espacios `dc` y `xmpDM` con su cita; «El Dublin Core es también la base de
   EBUCore (véase «La norma del sector: EBUCore»)» (sostenido por EBU Tech 3293 § 2.1, ya citado, y
   por la página `dc`); siete propiedades `xmpDM` literales (tapeName, altTapeName, startTimecode,
   good, logComment, scene, shotName); párrafo final de oficio («lo que se escribe en el XMP del
   fichero viaja con él… lo que sólo se anota en el proyecto se queda en el proyecto») y remisión
   al hueco. Entrada nueva en el índice.
2. **§ 7, «La cinta de archivo: la LTO», viñeta Capacidad**: añade **«LTO-10 drives can only read
   and write to LTO-10 media. But they support both 30 TB and 40 TB LTO-10 media interchangeably.»**
   con «no dice si esas cifras son nativas».
3. **«El punto en la ficha del puesto»**: párrafo tras la tabla con la sexta tarea literal y remisión
   al tema 13.
4. **Portada**: Fuente añade «y documentación de XMP»; Extensión 10.000 → 11.000 palabras.
5. **«Qué se puede preguntar»**: añade «qué es XMP y dónde guarda Premiere los metadatos de fichero».
6. **«Documentos técnicos que el tema cita»**: fila nueva de Adobe XMP; fila LTO con la página de
   compatibilidad y los cartuchos de 30 y 40 TB.
7. **«Lo que este tema no da»**: hueco LTO reescrito (100 TB comprimidos; 30 y 40 TB sin calificar);
   hueco nuevo: qué campos del panel de metadatos de Premiere van al XMP y cuáles al proyecto.
8. **«Trazabilidad»**: fila nueva de Adobe XMP (25-09-2026); fila lto.org con la página nueva;
   lista de oficio con «los dos espacios de nombres de XMP que importan al montador y lo que viaja
   con el fichero frente a lo que se queda en el proyecto».

Relectura de antecedentes: «su documentación», «ella», «más abajo» (→ `altTapeName`, en el mismo
subepígrafe), «esas cifras» (→ 30 y 40 TB de la cita anterior), «Una sexta» (→ «ocho TAREAS» del
párrafo anterior a la tabla): todos con su antecedente delante.

## Lentes

- `indice.py`: 11.016 palabras, 44 epígrafes; índice al día (la entrada nueva ya estaba escrita).
- `refutar_prosa.py`: 1 hallazgo, previo al remate (la referencia del convenio repetida en
  «Documentos técnicos» y «Trazabilidad», que es su sitio); siglas y negritas limpias.
- Sin norma jurídica citada: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

El tema; este informe; nuevos en `fuentes/canal-sur/montador/web/`: `xmp-adobe.txt`, `xmp-dm.txt`,
`xmp-dc.txt`, `lto-compatibility.txt`.
