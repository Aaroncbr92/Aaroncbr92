# Grafista (15) · Tema 15 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/15-innovacion-ia-generativa-etica-visual-validacion-humana-deepfakes-trazabilidad.md`.
Fecha del encargo 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema).
Ficheros tocados: el tema y este informe. **Amplía contenido nuevo: sí** (lagunas 1 y 2) → toca 5 bis.

## Fuentes cotejadas (29-09-2026)

- RDL 24/2021, art. 67.3 (volcado BOE-A-2021-17910, l. 1855).
- Comisión, *EU Icons for labelling AI-generated content* (volcado local, l. 83-91).
- IPTC, noticia del Código (volcado local, l. 209-212).
- IPTC NewsCodes *Digital Source Type* (volcado local, entero: 17 vigentes, 3 retirados).
- X Convenio RTVA, ficha 5345100 (volcado local, l. 5199-5214).

## Correcciones (las cuatro se comprobaron en la fuente y se aplicaron)

1. **Menor 1 (RDL 67.3).** Antes: «…tiene que reservarlo expresamente por medios de lectura mecánica.»
   Ahora: «…por medios de lectura mecánica u otros medios adecuados.»
2. **Menor 2 (iconos, fila «Fully AI-Generated»).** Se añade tras «música o arte compuestos del todo por IA»:
   «(con asterisco: «**May enjoy limited disclosure requirements for artistic, creative, fictional or satirical
   works**», es decir, las obras artísticas, creativas, de ficción o satíricas pueden tener un aviso atenuado)».
3. **Menor 3 (caso «Voz sintética…»).** Antes: «icono «Partially AI-Modified» o «Fully AI-Generated» según el
   caso». Ahora: «si se usa el icono de la UE (voluntario), el ejemplo que da la página para voces es el icono
   básico precedido de una etiqueta de texto («voices generated with»: «voces generadas con»); el total o el
   parcial, según el caso».
4. **Menor 4 (BBC).** «(EBU, BBC)» pasa a «(EBU, *British Broadcasting Corporation*, BBC)».

## Ampliaciones

1. **Laguna 1** («Lo que el Código pide a los proveedores», tras la medida 1.2). Nuevo: cita de IPTC «**In
   addition, the Code requires Signatories to add terms and conditions to prohibit users of AI systems from
   intentionally stripping metadata from AI-generated content.**», su traducción y la consecuencia para el
   grafista (borrar esos metadatos a propósito puede incumplir las condiciones del proveedor; lectura propia).
2. **Laguna 2** («El vocabulario IPTC del origen digital»).
   - «Son los valores que el grafista verá…» pasa a «Estos son los valores del vocabulario que más interesan al
     grafista (una selección, no la lista completa)…».
   - Fila nueva: dataDrivenMedia, **«Data-driven media»**, **«Digital media representation of data via human
     programming or creativity»**.
   - Párrafo nuevo: 17 valores vigentes; los nueve que no están en la tabla (computationalCapture, negativeFilm,
     positiveFilm, print, algorithmicMedia, screenCapture, virtualRecording, composite, compositeCapture), con dos
     citas literales; y los retirados con su sustituto (minorHumanEdits → humanEdits; digitalArt →
     digitalCreation; softwareImage, retirado en junio de 2022).
   - **La refutación se equivocó en parte**: pedía añadir `minorHumanEdits` como valor; la fuente lo da como
     **RETIRED** («Retired. Use "humanEdits" instead.»). No se añade como vigente; se explica como retirado.
   - Párrafo de la analogía con el RIA: se añade «un gráfico que representa datos (una infografía o una
     visualización programada, tema 4), «dataDrivenMedia»».
3. **Observación del convenio** (aplicada, comprobada en la ficha): en «La trazabilidad en el departamento
   gráfico», viñeta «Catalogar en el archivo», se añade «La ficha del convenio encarga al grafista «**Mantener
   el archivo de imagen del departamento gráfico.**»». La frase de l. 138 («las tres tareas») sigue siendo
   cierta: habla de las tres donde entra la IA.
4. Trazabilidad: fila IPTC-noticia añade «condiciones de uso contra la retirada de metadatos»; fila IPTC
   *Digital Source Type*, «(17 vigentes; retirados y sustitutos)». Portada: Extensión 11.800 → 12.100 palabras.

Antecedentes releídos: «esos metadatos» (tiene delante «los metadatos del contenido generado con IA»); «los ocho
de la tabla» (la tabla tiene ahora ocho filas); «dos compuestos» (composite y compositeCapture).

## Lentes

- `indice.py`: 12.145 palabras, 42 epígrafes (sin epígrafes nuevos; el tema no está en `portadas.tsv`, la
  portada se ajustó a mano).
- `refutar_prosa.py`: 1 aviso, «IA» en el título antes de la frase de siglas (preexistente, falso positivo:
  se presenta en la frase de siglas).
- `negritas.py --todas` contra los volcados de iconos, IPTC (dos), convenio: todas las negritas nuevas «ok».
  El único «NO ESTÁ» es una cita del RIA (art. 99) ajena a esas fuentes y no tocada.
- `refutar_exactitud.py` / `refutar_modo.py`: no se ha tocado ningún precepto de norma salvo la consecuencia
  (redonda) del 67.3; no aplican.

Respuestas afectadas: la 9 pasa a entera; la 14 y la 15, a enteras.
