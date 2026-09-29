# Grafista (15) · Tema 11 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/11-derechos-autor-bancos-imagenes-tipografias-licencias-imagen-atribucion.md`.
Entrada: `15-T11-refutacion.md` (2 hallazgos menores, 2 lagunas) y `15-T11-preguntas.md` (10 enteras,
2 a medias, 3 no). Fecha del encargo: 24-09-2026; fuentes leídas el 29-09-2026 (fecha de sistema).
Copia previa: scratchpad `15t11-antes-remate.md`.

**Amplió contenido nuevo: sí** (variantes Creative Commons y CC0; Ley de Marcas; símbolos ® y TM).
Toca fase 5 bis sobre los pasajes listados abajo. Extensión: de 17.152 a unas 19.000 palabras (portada
actualizada); 52 epígrafes (uno nuevo).

## Ficheros tocados

- El tema.
- Este informe.
- Fuentes nuevas (copias locales, `fuentes/canal-sur/grafista/`): `cc-by-nc-4.0-legalcode-es.txt`,
  `cc-by-nc-sa-4.0-legalcode-es.txt`, `cc-by-nd-4.0-legalcode-es.txt`, `cc-by-nd-4.0-legalcode-en.txt`,
  `cc0-1.0-legalcode-es.txt`, `ompi-pub-900-1-es.pdf` y `.txt`; línea añadida a su `README.md`.
  Volcado BOE: `fuentes/canal-sur/BOE-A-2001-23093.md` y `.redacciones.tsv` (Ley 17/2001, `boe.py norma`).
- `indice.py` se corrió una vez sin argumentos (todos los temas del `.tsv`) por error; no cambió
  ningún fichero versionado fuera de los ya modificados por otros agentes (comprobado con `git status`;
  los `M` de otros temas de Grafista son trabajo ajeno previo). Después, sobre el tema 11 sólo.

## Correcciones de exactitud (comprobadas en la fuente antes de aplicarlas)

Las dos del informe eran correctas. Getty, `www_gettyimages_com_eula.txt`, líneas 313, 318 y 332.

1. **Getty, IA (hallazgo 1).** Epígrafe 2, «Maquetas, uso compartido e inteligencia artificial», viñeta
   «IA»: reescrita con el alcance literal de la prohibición (cualquier fin de aprendizaje automático o
   de IA y tecnologías de identificación de personas; también pies y metadatos), la excepción literal
   (i) archivo, búsqueda, indexación u ordenación interna y (ii) edición permitida, sólo contenido
   creativo y sin entrenamiento; se mantiene el entrenamiento indirecto y se añade la cláusula
   «Social Media & AI Tool Termination» (misma fuente, línea 332). Epígrafe 7: fila «Subir una foto…»
   corregida y fila nueva «IA para indexar o catalogar imágenes creativas de Getty…».
2. **Getty, uso compartido RF (hallazgo 2).** Misma sección, viñeta «Uso compartido de RF»: añadidas
   la salvedad «however you may make RF content available for viewing…» y la del archivo en bruto
   (literal). Epígrafe 7: fila «Imagen RF de Getty compartida en el equipo» reescrita.

## Ampliaciones (lagunas)

3. **Variantes Creative Commons y CC0 (laguna 1; preguntas 12 y duda de ARASAAC).** Epígrafe 4:
   - Frase final de «Material con licencia abierta» cambiada (ya no dice «no se han leído»).
   - `###` nuevo «Las variantes: no comercial, sin obras derivadas, compartir igual; y la CC0»:
     definición de material adaptado y regla de la música sincronizada (sección 1), modificaciones
     técnicas (2(a)(4)); NC: concesión (2(a)(1)), definición de «NoComercial», reserva de regalías
     (2(b)(3)); ND: 2(a)(1) y 3(a)(1) del original inglés; SA: 3(b)(1) de BY-NC-SA; derechos morales,
     de imagen, patentes y marcas no licenciados (2(b)(1) y (2)); CC0 1.0: secciones 2, 3 y 4; cuadro
     de las cinco variantes. El párrafo de ARASAAC queda bajo este `###` y remite «arriba» a la
     definición de NC, que no resuelve el caso (se dice).
   - **Aviso de fuente**: la traducción española publicada de BY-ND 4.0 dice en 2(a)(1) «solamente
     para fines NoComerciales» y nombra la BY-NC-SA en su preámbulo, a diferencia del original inglés.
     El tema cita el inglés y lo explica. Qué versión lingüística prevalece no consta en lo leído.
   - Epígrafe 7: filas nuevas BY-ND recortada o rotulada, música CC en vídeo, BY-NC en emisión o
     promoción, imagen CC0.
4. **Ley 17/2001, de Marcas (laguna 2; preguntas 13 y 15).** `boe.py --fecha 20260924`: arts. 4 y 34
   y 37 (redacción del RDL 23/2018, BOE-A-2018-17769, vigente desde 14-01-2019), 31 (original).
   - Epígrafe 3, «Logotipos y marcas ajenas»: se quita «no se ha leído» y se añaden concepto (art. 4),
     duración (31), derecho conferido (34.1, 34.2.a-c, 34.3.e y f) y límites (37.1.a-c y 37.2); y un
     párrafo de aplicación dicho como lectura, no confirmada en sentencia: si una infografía
     informativa es «uso en el tráfico económico» la ley no lo dice; el 37.1.c permite referirse a los
     productos del titular; el derecho de autor sobre el logotipo sigue (35.1, transformación); en una
     promoción es uso en la publicidad (34.3.e).
   - Epígrafe 6, «Los símbolos de reserva»: el último párrafo se sustituye. **La Ley de Marcas no
     menciona ® ni TM** (`grep` en el volcado entero: 0). Se toma la guía de la OMPI «El secreto está en
     la marca» (publicación 900.1S, 2019), apartado «¿TM o ®?», con su advertencia de que no refleja la
     opinión de los Estados miembros; cuadro © / (p) / ® / TM-SM.
   - Epígrafe 7: filas nuevas «Logotipo de una empresa en una infografía informativa» y «Poner ®
     junto a un logotipo».
5. **Periferia**: portada (Fuente, Redacción que se estudia, Extensión 19.000), siglas (ND, CC0, Ley
   de Marcas, OMPI, TM, SM), «Qué se puede preguntar», «Normativa que el tema invoca» (Ley 17/2001),
   «Lo que este tema no da» (bullet de marcas reescrito; nuevo de BY-SA, BY-NC-ND y versiones previas a
   la 4.0), «Trazabilidad» (tres filas nuevas).

Antecedentes releídos: «la Ley de Marcas» (definida en siglas y en el epígrafe 3; «la ley» del
epígrafe 3 corregido a «la Ley de Marcas», porque «la ley» es el TRLPI sólo en los epígrafes 1, 4 y 6);
«arriba» del párrafo de ARASAAC; «el mismo párrafo» de Getty; «(2(b)(3))», «(3(b)(1))» con su licencia
delante.

## Preguntas tras el remate

8 entera (salvedad RF); 9 entera (excepción de IA); 12 entera (ND, 2(a)(1)); 13 entera en lo que la
ley da (37.1.c y 34.3.e; lo demás, declarado como lectura); 15 entera (OMPI; la Ley no lo regula).

## Lentes

- `indice.py` (tema 11): 52 epígrafes, índice regenerado.
- `refutar_prosa.py`: 1 hallazgo (TM sin presentar), corregido; 0 al final.
- `negritas.py` con Ley de Marcas, CC (NC, NC-SA, ND inglés, CC0), OMPI y Getty: todas las negritas
  nuevas, «ok»; los «no está» son de fuentes no pasadas (TRLPI, LO 1/1982, Libro de estilo…), como en
  la refutación; el aviso «art. 681» es falso positivo (LECrim no pasada).
- `refutar_exactitud.py` con TRLPI y Ley de Marcas: 32 no literales, las mismas de la refutación
  (otras normas); ninguna de marcas. `refutar_modo.py`: 0.
