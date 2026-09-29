# Grafista (15) · Tema 2 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/02-identidad-visual-corporativa-manual-de-marca.md`
(unas 9.150 palabras con índice y tablas). Fecha de trabajo del encargo: 24-09-2026; fuentes releídas
el 29-09-2026 (fecha de sistema). No se ha corregido nada: sólo se informa.
Ficheros tocados: este informe y `15-T02-preguntas.md`.

Saltado en exactitud, como manda `15-T02-redaccion.md`: lo «Copiado del común» (LE 6.5, 7.4 y 3.16.2;
párrafo de la EBU R 95 «The action safe area…»). «Copiado de RTVE sin cambios»: ninguno. La cobertura
sí mira el tema entero.

## Fuentes cotejadas (29-09-2026)

| Fuente | Qué se cotejó | Resultado |
|---|---|---|
| WCAG 2.2 (`fuentes/canal-sur/grafista/wcag22.txt`) | 1.4.1, 1.4.3 (tres salvedades), 1.4.11, fórmula, 1 a 21, *large scale*, *relative luminance*, fecha de 12-XII-2024 | Literales correctos |
| Carta 2024-2029 (BOJA 247/2023, `.txt`) | Art. 10.1 y 10.2 literales; rúbrica del art. 34; 34.1 | Correcto |
| Contrato-programa 2024-2026 (BOJA 245/2023, `.txt`) | Puntos 45, 46, 105, 112; búsqueda de «marca» en todo el documento | Literales correctos; **omisión** (hallazgo 1) |
| Libro de Estilo 2004 (`.txt`) | 2.3.2.4 y su destinatario; «logotipo» aparece una sola vez; «anagrama» en 4184 y 4224 | Correcto |
| EBU R 95 (`realizador/ebu-r095.txt`) | v1.1 de junio de 2017, título, 1920 píxeles activos; 96/54/1728/3456 por cálculo | Correcto |
| Analysis Function, *colours* (web) | Seis literales; 23-11-2021, actualizada 12-02-2026 | Correcto |
| UCF, guía «Frutiger» (web) | Cuatro literales | Correcto |
| MDN «Diseño receptivo» (es, web) | Definición, Marcotte 2010, «imágenes de director artístico», 12-09-2026 | Correcto |
| Blog «Memoranda» (web, leído en resumen) | 9-III-1995, Joaquín Marín, amarillos, triángulo invertido, *Diario 2*, 13-III | Correcto en lo que la lectura permite |

No se releyeron (ya cotejadas por el verificador): MDN `<hex-color>`, *charts* y el artículo de
*Fonseca*. Las cuentas (21:1, 1728, 3456, 2⁸, 2²⁴, `#FF0000`, 1,618 y 618) cuadran.

## Hallazgos de exactitud

Graves: **0**.

Menores: **3**.

1. **Error 6 (salvedad omitida), «La arquitectura de marca»**: «Los documentos de la casa hablan de
   marcas por canal… Todas comparten el nombre "Canal Sur" y le añaden un descriptor». El
   Contrato-programa nombra además (punto 52) **«los servicios de sus canales web temáticos de marcas
   canalcocina, canalturismo, canalflamenco, y canal.labanda, y las potenciales nuevas marcas…»**, y
   habla de la marca «Cine andaluz» (líneas 1153 y 1258 del volcado). Esas marcas no llevan «Canal Sur»,
   lo que matiza la lectura de un modelo monolítico. Propuesta: añadir el punto 52 literal y rebajar la
   frase a «las de canal de televisión y radio comparten…»; en «Lo que este tema no da», que el modelo
   decidido no consta.
2. **Error 3 (recuento), «El contraste medible»**: «Tres definiciones de las propias pautas» presenta
   tres viñetas, pero la tercera (el logotipo exento y el texto incidental) no es una definición del
   glosario, sino las salvedades del criterio 1.4.3. Propuesta: «Dos definiciones de las propias pautas y
   las salvedades de 1.4.3» o separar la viñeta.
3. **Error 5 (sigla sin presentar)**: «DOI» en «Trazabilidad» (identificador de objeto digital, del
   inglés *digital object identifier*). Menor. De paso: CSS, HD y UHD se presentan en las siglas y no se
   usan en el cuerpo (CSS sólo aparece dentro de una URL); se pueden quitar.

Observación sin hallazgo: la definición de texto grande se corta antes de «or font size that would yield
equivalent size for Chinese, Japanese and Korean (CJK) fonts»; el corte no cambia el sentido.

## Cobertura del enunciado

Las siete rúbricas (identidad visual corporativa, manual de marca, coherencia gráfica, legibilidad,
color, tipografía, adaptación a formatos) tienen epígrafe propio y en su orden. Resultado de las 15
preguntas (`15-T02-preguntas.md`): **10 enteras, 1 a medias, 4 no**.

Lagunas (el remate amplía, con fuente leída):

1. **Círculo cromático y armonías** (preguntas 9 y 10): el tema sólo da los complementarios de la mezcla
   aditiva; falta el círculo tradicional de pintor, el complementario en él y las armonías (análoga,
   complementaria, triádica, monocromática). Hace falta fuente técnica publicada; si no se halla, se
   declara en «Lo que este tema no da» y se avisa de que «complementario» cambia según el modelo.
2. **Anatomía de la letra** (pregunta 11): altura de x, ascendentes, descendentes, línea base, y por qué
   una altura de x generosa ayuda a leer en pantalla. Encaja en «Las medidas de la letra».
3. **Legibilidad frente a lecturabilidad** (pregunta 15): nombrar la distinción (carácter frente a texto
   seguido) en «Qué hace legible una letra en pantalla», con fuente o declarada como oficio.

La pregunta 3 (marcas web temáticas) se resuelve con la corrección del hallazgo 1 de exactitud; no se
cuenta como laguna aparte.

## Para el remate

- Hallazgos 1-3: corrección de pasajes (Sonnet vale). Lagunas 1-3: ampliación (Opus y fase 5 bis).
- Regenerar el índice si se añaden epígrafes; actualizar «Trazabilidad» y la extensión de la ficha.
