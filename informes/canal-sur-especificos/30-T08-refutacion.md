# Puesto 30 · Tema 8 · Refutación (fase 4, segunda ronda)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). No corrige: sólo señala.
Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/08-ingesta-digitalizacion-transferencia-verificacion-copias-metadatos-archivo.md`
(11.525 palabras, estado del commit b08a902, tras remate y 5 bis).
Preguntas: `30-T08-preguntas.md` (ronda nueva). La primera refutación (graves 0, menores 0, laguna
XMP) y su remate quedan en git; esta ronda revisa el tema ya ampliado.

## Alcance

Exactitud: todo lo que no es «Copiado del común» (Cámara T07) ni «Copiado de RTVE sin cambios»,
según `30-T08-redaccion.md`; incluidos los pasajes nuevos del remate (XMP, sexta tarea, LTO 30/40 TB).
Cobertura: el tema entero contra el enunciado.

## Método y fuentes releídas (25-09-2026)

- Script: cada negrita del tema, normalizada (comillas, guiones de corte, marcas de página), buscada
  en `fuentes/canal-sur/montador/**` (Resolve 21, EBU Tech 3293, CCSDS 650.0-M-3, lto.org, XMP,
  Adobe) más el X Convenio y el Libro de estilo. **Todas las negritas de lo no copiado aparecen
  literales.** Las 22 que no aparecen son todas de bloques «Copiado del común» (DPC, Sony Z200 e
  ILCE-1, INCIBE, Panasonic), cuyas fuentes están en la carpeta de Cámara: se saltan.
- Páginas por marca `[[pNNN]]`: Resolve pp. 373-374 (*Clone Tool*, seis opciones, 128 bits,
  XXHASH64), 417, 418, 420, 434 (metadatos, CSV/ALE), 558-564 (captura; 00086400.dpx en *Capture
  Now*, p. 562; regla de no duplicar por EDL, p. 564): cuadran.
- CCSDS: § 4.2.2 «six functional entities»; rótulos 4.2.3.3-4.2.3.8; diciembre de 2024, Magenta.
- EBU Tech 3293: v. 1.10, Ginebra, abril de 2020.
- lto.org: 10.ª generación, 100 TB comprimidos, 1200 MB/s con nota 2.5:1, compatibilidad por
  generaciones, 30/40 TB; LTFS desde LTO-5.
- Adobe: página de ingesta (transcodificar, consolidar, verificar sin algoritmo); XMP (ISO 16684-1),
  `dc` (DCMI) y `xmpDM` (`altTapeName` nombra Premiere).

Lo explicativo añadido (UMID como identificador de paquete en MXF, remitido al tema 15; captura
registrada sin control remoto) es correcto y va declarado como oficio o remitido.

## Hallazgos de exactitud

**Graves: 0.**

**Menores: 1 (error 9 leve, trazabilidad incompleta).** La sexta tarea de la ficha
(**«Etiquetar, grabar e introducir en base de datos…»**), citada literal en «El punto en la ficha
del puesto» desde el remate, no figura en «Documentos técnicos que el tema cita» (fila del convenio:
«configurar y preparar materiales, enlaces, compactar para el archivo, control de calidad, repicar
cintas»). Propuesta: añadir «etiquetar para la emisión automatizada (remitida al tema 13)» a esa fila.

## Cobertura del enunciado

Las siete rúbricas tienen epígrafe propio, en el orden del enunciado, con teoría y aplicación.
Preguntas: 13 enteras, 1 a medias, 1 no.

- **A medias (pregunta 6)**: nombre del clip en *Capture Now* a otra cadencia. El tema da la regla y
  el ejemplo del manual; el cálculo se deduce. No es laguna. Opcional para el remate: una frase de
  oficio que diga que 86.400 = 3.600 s × 24 cuadros (cálculo, sin fuente nueva).
- **Laguna (pregunta 15)**: formatos de conservación en el archivo. § 7 explica el soporte (LTO,
  LTFS) y el modelo (OAIS), pero no en qué formato de fichero se guarda lo digitalizado o archivado
  (códecs sin pérdidas de preservación, p. ej. FFV1 o JPEG 2000, en MXF o Matroska), ni el tema 4 lo
  trata. Es preguntable en «digitalización» y «archivo». El remate (Opus) debe buscar fuente
  publicada (p. ej. IASA TC-06, FADGI, Library of Congress «Sustainability of Digital Formats», o
  documentación EBU) y añadir un subepígrafe breve en § 7; si no confirma, declararlo en «Lo que
  este tema no da». No escribir de memoria.

## Resumen

Graves 0 · menores 1 (trazabilidad de la sexta tarea) · lagunas 1 (formatos de conservación).
Ampliación: Opus, § 7 y, si procede, «Lo que este tema no da»; después, 5 bis sólo sobre lo ampliado.

Ficheros tocados: `30-T08-preguntas.md` y este informe (sustituyen a los de la primera ronda). El
tema no se ha tocado.
