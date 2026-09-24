# T08 · Redacción · Normativa sobre igualdad (Ley 12/2007, Ley 15/2022, Ley 4/2023)

Tema: `temas/canal-sur-comun/08-igualdad.md`. Punto 8 del temario común de Canal Sur. Fase 2
(redactar), un solo agente para todo el tema. Fecha de trabajo y de lectura de todos los
preceptos: **24-09-2026**.

Estado: **redacción terminada** (21.045 palabras de cuerpo, 31 epígrafes `##`/`###`).

## Material de partida

- `informes/canal-sur-comun/T08-investigacion-ley-12-2007.md` y
  `informes/canal-sur-comun/T08-investigacion-15-2022-y-4-2023.md`, leídos enteros.
- Fuentes leídas enteras en su redacción vigente el 24-09-2026: `BOE-A-2008-2492` (Ley 12/2007,
  arts. 1 a 86 y disposiciones), `BOE-A-2022-11589` (Ley 15/2022, articulado, adicionales,
  transitoria y finales), `BOE-A-2023-5366` (Ley 4/2023, arts. 1 a 82, adicionales,
  transitorias, derogatoria y finales 15.ª a 20.ª), `BOE-A-2026-16172` (RD 606/2026: arts. 1 a 9,
  16 a 18, DT única, DF 10.ª), `BOE-A-2024-20402` (RD 1026/2024 entero), `BOE-A-2008-1185`
  (Ley 18/2007: arts. 1, 2, 4, 5, 6, 14, 20, DA 3.ª).
- Redacciones anteriores de la Ley 12/2007 leídas con `boe.py --fecha 20181015` y
  `--fecha 20240216`: arts. 3, 6, 7, 8, 9, 11, 12, 13, 23, 27, 31, 32, 40, 57, 58, 61.

## Estructura escrita

Ficha, siglas, enunciado literal (con la nota del paréntesis sin cerrar), párrafo inicial e
índice (generado con `herramientas/indice.py`). Un bloque `##` por ley en el orden del enunciado;
dentro de cada uno, `###` por materias: identificación/estructura; objeto, ámbito y
definiciones; principios y políticas; medidas por ámbitos (empleo y medios con más detalle);
organización institucional / Autoridad; garantías; infracciones y sanciones. Al final del bloque
de la Ley 4/2023, un cuadro comparado de los tres regímenes sancionadores. Después: «Lo que se
aplica a la RTVA y a sus medios», «Normativa que el tema invoca», «Lo que este tema no da» y
«Trazabilidad». Escrito por partes (cabecera + Ley 12/2007 hasta art. 13; título II; títulos
III a V; Ley 15/2022 en dos partes; Ley 4/2023; secciones finales), guardando cada una.

Cadenas de redacción de la Ley 12/2007 en el cuerpo (una línea cada una: qué, qué norma, desde
cuándo): arts. 3, 6.2, 7, 8, 9, 11, 12, 13, 23, 27, 31, 32, 40, 57, 58 y 61.

## Consulta al Tribunal Constitucional (Ley 4/2023)

- 24-09-2026: buscador de jurisprudencia `hj.tribunalconstitucional.es` (formulario de búsqueda,
  campos NUMERO_RECURSO/ANNO_RECURSO). 2428/2023 → «No se han encontrado resultados»;
  3679/2023 → «No se han encontrado resultados». Control: 6706/2022 → devuelve la STC 89/2024
  (el buscador funciona por número de recurso). Búsqueda libre «Ley 4/2023» → solo la STC
  89/2024 (no es sobre esta ley).
- BOE (`herramientas/boe_buscar.py`): «Recurso de inconstitucionalidad 2428-2023», «3679-2023»,
  «Ley 4/2023, de 28 de febrero» (2023-07-01 a 2026-09-24), «personas trans» (2024-2026): solo
  los anuncios de admisión (`BOE-A-2023-11734`, `BOE-A-2023-15068`); ninguna sentencia.
- Conclusión aplicada al texto: **sin sentencia a 24-09-2026**; los preceptos recurridos están
  vigentes. Se dice con la fecha en el bloque de la Ley 4/2023, en la sección RTVA (27.2, cuyo
  inciso final está recurrido en el 2428-2023) y en la trazabilidad.
- Mismo control para el recurso 3473-2024 contra el Decreto-ley 3/2024: sin resultados en el
  buscador del TC y solo el anuncio de admisión en el BOE.

## Discrepancias con el encargo o con la investigación (manda la fuente)

1. **Encargo: «Ley 18/2007 arts. 4.f, 6.3.c».** En la Ley 18/2007 el artículo 6 es «Régimen
   jurídico» y no tiene letra c) sobre igualdad. El texto que el encargo busca está en el
   **artículo 4.3.c)** («Promover el respeto a la dignidad humana […] la igualdad entre hombre y
   mujer…»), y el 4.f es en realidad **4.1.f)**. Se cita así en el tema. Añadidos, por ser norma
   y tocar la igualdad: 4.1.b), 14.1 (paridad en el Consejo de Administración) y 20.1 (Consejo
   Asesor con vocales del Consejo Andaluz LGBTI y del Consejo Andaluz de Participación de las
   Mujeres).
2. **Investigación 12/2007, art. 10.3:** dice «Instituto de Estadística y Cartográfica»; la
   fuente dice **«Instituto de Estadística y Cartografía de Andalucía»**. Corregido.
3. **Remisiones de la Ley 12/2007 a la Ley 1/2004 (arts. 66.2 y 85.4 → arts. 4.15 y 4.16):**
   leída la Ley 1/2004 a 19-12-2007 (`boe.py --fecha 20071219`), esos números eran el cese o
   rectificación de publicidad ilícita (4.15) y la potestad sancionadora (4.16). En el
   consolidado de hoy el 4.15 y el 4.16 tienen otro contenido (códigos de autorregulación;
   quejas), por las reformas del art. 4 de la Ley 1/2004 y la STC 40/2025 (ver
   `T04-investigacion-ley-10-2018.md`). El tema lo dice sin afirmar qué número corresponde hoy.
4. **Investigación 15/2022 y 4/2023:** sin discrepancias en lo comprobado. Añadido: el recurso
   2428-2023 impugna también el **inciso final del art. 27.2** de la Ley 4/2023 (medios de
   titularidad pública), dato relevante para la sección RTVA; leído en `BOE-A-2023-11734`.

## Qué no se ha podido confirmar y cómo se ha tratado

- Existencia y desarrollo reglamentario de los órganos del título III de la Ley 12/2007: el
  tema da lo que dice la ley («se creará», «se crea») y lo declara en «Lo que este tema no da».
- Encaje del permiso del art. 40 de la Ley 12/2007 con los permisos estatales: no se afirma.
- Si la RTVA entra en «entidades instrumentales» (9.2), «agencias y demás entidades
  instrumentales» (31.4, 32.1), el art. 2.2.a) de la Ley 12/2007, el art. 2.4.e) de la Ley
  15/2022 o las «empresas de más de cincuenta personas trabajadoras» del art. 15.1 de la Ley
  4/2023: ninguna norma lo dice; la sección RTVA da el destinatario literal y no infiere.
- Puesta en funcionamiento de la Autoridad (orden ministerial) y nombramiento de su titular: no
  comprobados; se dice.
- Datos tomados de otros informes sin releer su norma: denominación y fecha de la **Ley 2/2019,
  de 26 de junio** (redacción del art. 14.1 de la Ley 18/2007; la cadena del BOE da
  `BOE-A-2019-11576`, vigencia 28-06-2019) y del **Decreto-ley 5/2024, de 21 de mayo** (art.
  20.1; la cadena da `BOJA-b-2024-90100`, vigencia 25-05-2024), según
  `T05-investigacion-ley-organos.md`. Convalidación del Decreto-ley 3/2024 (21-02-2024), según
  `T08-investigacion-ley-12-2007.md`.

## Comprobaciones mecánicas

- Todas las negritas del cuerpo que abren con «» (442) se han contrastado, con espacios
  normalizados, contra la concatenación de las fuentes (volcados de las tres leyes, RD 606/2026,
  RD 1026/2024, Ley 18/2007, STC 89/2024, anuncio del recurso 3679-2023 y redacciones
  anteriores de la Ley 12/2007 sacadas con `boe.py --fecha`): **0 no literales**.
- Se quitó la negrita a 226 rótulos y términos que no eran cita literal (el encargo dice
  «negrita sólo para citas literales»); los rótulos de párrafo pasan a cursiva. Quedan en
  negrita, por la forma de la casa, las etiquetas de la ficha y de la tabla de trazabilidad, las
  siglas del párrafo de siglas y «Enunciado del programa».
- `refutar_prosa.py`: 0 relleno; una «repetida» (la fórmula de las cadenas, intencionada); una
  «sigla sin presentar» (LGBTI, dentro de cita literal de la Ley 18/2007, que la escribe así).
- `refutar_exactitud.py` da muchos falsos positivos en este tema porque cruza artículos del mismo
  número de leyes distintas; no se ha usado como criterio.

## Ficheros tocados

- Creado/escrito: `temas/canal-sur-comun/08-igualdad.md`.
- Creado: este informe.
- Ningún otro. (Nota: en mitad de la redacción apareció en `git` un commit ajeno, `7b03d6d`, que
  incluía una versión parcial del tema; el fichero en disco es la versión final.)
