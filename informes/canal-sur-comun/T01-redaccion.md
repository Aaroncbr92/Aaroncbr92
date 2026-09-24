# T01 · Redacción · Constitución Española de 1978

Tema: `temas/canal-sur-comun/01-constitucion-espanola.md` (**34.284 palabras** de cuerpo,
medidas con `tema.cuerpo`). Punto 1 del temario común de Canal Sur, rúbricas a), b) y c).
Fase 2 (redactar), un solo agente. Fecha de trabajo y de lectura de todos los preceptos:
**24-09-2026**, sobre los volcados de `fuentes/canal-sur/` (CE `BOE-A-1978-31229`, EAA
`BOE-A-2007-5825`, LBRL `BOE-A-1985-5392`, LAULA `BOE-A-2010-11491`, LOTCu `BOE-A-1982-11584`,
LODP `BOE-A-1981-10325`), `boe.py precepto` (con y sin `--fecha`) para las cadenas, y el XML del
diario del BOE para las cuatro reformas constitucionales, el RD 2560/1978, el acuerdo de la JEC,
la STC 103/2013 y la STC 111/2016, y el XML consolidado de los bloques `a26` y `a126` de la LBRL.

## 1. Estructura

- Ficha, siglas, enunciado literal completo (a, b y c), párrafo inicial, índice vacío.
- Una sección `## Identificación y estructura de la Constitución` antes de las rúbricas (CICLO.md
  la admite como sección fija): elaboración, entrada en vigor, preámbulo, estructura y las
  quince disposiciones. **Decisión a revisar**: el encargo pedía los tres bloques tras el párrafo
  inicial; lo puse aquí porque no casa con ninguna rúbrica y cae en examen.
- Tres `##` con el texto literal de cada rúbrica y, dentro, un `###` por materia en el orden del
  enunciado (6 + 9 + 7). `####` para subdivisiones (capítulos, tratados, funciones, etc.).
- Donde el enunciado nombra algo sin precepto: «principios inspiradores» (la CE no usa la
  expresión; sólo «inspirado» en 31.1 e «inspirándose» en 132.1: comprobado con grep) y
  «órganos constitucionales» (la CE no la usa; sí «poderes constitucionales», 116.5). En los dos
  se dice y se da lo escrito (tabla de cómo califica la CE a cada órgano, tabla de nombramientos).
- Reformas en el cuerpo, con línea en cursiva (qué, qué norma, desde cuándo) en 13.2, 49, 69.3,
  135, y tabla de las cuatro en «El procedimiento de reforma constitucional». LBRL 13.2, 25, 28 y
  LAULA 9.12, igual.
- Negrita: sólo cita literal. **Excepciones declaradas**: siglas; marcadores «**Artículo N.**»
  (literales: es el rótulo del bloque en la fuente) que puse en negrita porque
  `refutar_exactitud.py` los necesita para abrir bloque; el descriptor que RTVE añadía («Estado,
  soberanía…») va en cursiva detrás. Un rótulo no literal: «**Artículos 82 a 85.**».

## 2. Qué reutilicé de RTVE

Texto de `temas/general/01-constitucion-espanola.md` para: §1.1-1.4 (elaboración, estructura,
reformas), Título Preliminar, Título I entero (3.1-3.8), Títulos II a VII, IX, X y las
disposiciones (13.1-13.3), cuadros de art. 53, 116, investidura/167-168, 148 y 149, 153. Las
explicaciones de RTVE se conservan; **la negrita se rehízo entera**: RTVE la usaba como énfasis
sobre paráfrasis (p. ej. «**Mínimo de 300 y máximo de 400 Diputados**»). Ahora cada tramo en
negrita es texto literal y, en casi todos los artículos, se da el precepto entre comillas.

## 3. Qué corregí (comprobado en la fuente)

- **Reformas**: «dos veces» → cuatro (13.2 de 1992, 135 de 2011, 49 de 2024, 69.3 de 2026), las
  cuatro con disposición final única de entrada en vigor el día de publicación (leídas).
- **Art. 49**: texto vigente de 2024 en el cuerpo.
- **Art. 69.3**: texto vigente; tres cambios de redacción (fuera las «agrupaciones», Ibiza y
  Formentera separadas, «La Gomera, El Hierro») comprobados con `--fecha 20260101`; añadida la
  **disposición transitoria única** (eficacia pospuesta a las primeras elecciones al Senado);
  recuento «siete» → ocho islas con un Senador, con la salvedad.
- **Art. 112**: la negrita «La confianza se entiende otorgada por mayoría simple» no era literal;
  ahora el texto: «cuando vote a favor de la misma la mayoría simple de los Diputados».
- **Art. 67.1**: quitada la inferencia «nada impide compaginarla con la de Senador designado».
- **Incisos que faltaban**: 57.2, 63.2, 67.3, 68.5 párr. 2.º, 79.2, 82.4, 82.5, 84 (2.º inciso),
  98.4, 117.4, 122.2 (2.ª frase), 124.2-3, 127.1, 159.4 párr. 2.º, 161.1.a) 2.º inciso, 161.1.b),
  162.2, 55.2 in fine.
- **Título VIII** (reparos de la investigación c, todos confirmados): negritas no literales de
  137, 140, 141, 144, 145, 148, 149; las salvedades omitidas de 149.1 (6.ª, 8.ª, 17.ª, 18.ª, 19.ª,
  20.ª, 23.ª, 28.ª, 29.ª): ahora las 32 materias van literales; añadido 149.2; corregido 150.3
  («aun en el caso de materias atribuidas a la competencia de éstas»); 151 completo (151.1 con
  «dentro del plazo del artículo 143.2» y la ley orgánica; 151.2 en cinco pasos; 151.3); 152 entero
  (responsabilidad política, 152.2, 152.3); 156-158 enteros. Quitado «Es la vía del artículo 143»
  sobre el 146 como afirmación del precepto (ahora es la organización del epígrafe).
- **Tabla del art. 53**: RTVE ponía «Orgánica» para el art. 14; el 81.1 habla de derechos
  fundamentales y libertades públicas, que es el nombre de la Sección 1.ª. Rehecha.
- «Queda excluida la iniciativa popular» (166): va como deducción, en redonda.

## 4. Qué añadí

- a): preámbulo literal; «Estado social y democrático de Derecho» con los preceptos por adjetivo;
  Título VII (128-133 y 135 literales, DA única de la reforma de 2011); cuadro de deberes.
- b): tablas de órganos y nombramientos; funciones por Cámara; art. 134; tratados 93-96; cuadro
  investidura/confianza/censura; **LO 2/1982** (arts. 1, 2, 4, 9, 10, 12, 15, 19, 21, 29, 30, 33,
  35; art. 30 en redacción de la LO 2/2024 desde 22-08-2024) y **LO 3/1981** (arts. 1 a 11, 15, 17,
  28, 29, 32; 2 y 10 en redacción de la LO 2/1992). Cuadro TC/Tribunal de Cuentas.
- c): vía de Andalucía con citas literales del preámbulo del EAA (sin afirmar nada que el texto
  no diga); EAA 1, 2, 3.4, 4, 42, 60, 89-98, 108; LAULA 1, 3, 4, 5.2, 6, 8, 9 (28 apartados), 11-15,
  57, 89, 91-93, 109, 113; LBRL 1, 3, 4, 11-13, 15, 19-29, 31-37, 121-128.
- **Incisos anulados** (aviso de CICLO.md): identificados en el XML consolidado (`<strong>`) y en
  los fallos. LBRL 26.2: los dos incisos de la STC 111/2016. LBRL 126.2: la frase entera de los no
  concejales en la JGL, STC 103/2013; **leí el FJ 6**, que la investigación no pudo leer: la
  nulidad «se limita única y exclusivamente a la facultad que se reconoce al alcalde para nombrar
  como miembros de la Junta de Gobierno a personas que no ostenten la condición de concejales».
  El tema da el texto anulado en redonda, entre comillas y dice que no está en vigor.
- STC 111/2016, fallo 3.º: interpretación conforme de 36.1.g) y 36.2.a) párr. 2.º (literal).
- Cadenas comprobadas: LBRL 13 (5.000 → 4.000 por RDL 6/2023, desde 21-12-2023), 25 (seis
  redacciones; letra o por RDL 9/2018, apartado 6 por RDL 6/2023, letra p por RDL 7/2026 desde
  22-03-2026), 28 (estaba «(Suprimido)»; lo rehízo el RDL 6/2023).

## 5. Qué dejé fuera y por qué

- Todo lo propio de RTVE y de sus exámenes (ficha, bases, «se pregunta», «cae», Ley 17/2006,
  III Convenio, §14, notas de actualización, trazabilidad al corte de 2022).
- **Senado de 266 (XV legislatura)**: dato de actualidad, no constitucional, sin comprobar y
  alterado por la reforma de 2026.
- **Art. 155 en Cataluña (2017-2018)**: hecho de aplicación, fuera de las fuentes del tema.
- Número de Diputados, LO 2/2026 de adaptación de la LOREG (sólo visto el título), fechas de
  aprobación en las Cámaras de las reformas de 2024 y 2026 (sólo constan en la versión cooficial
  en euskera), composición actual de órganos.
- Reforma del EAA (248-250), instituciones andaluzas y competencias concretas: punto 2 del común
  (se dice en «Lo que este tema no da»).
- LAULA 13.4 bis y el detalle de cada letra del 9: no alimentan pregunta del enunciado más allá
  de la lista de materias.

## 6. Discrepancias con los informes o las fuentes

- El acuerdo de la JEC (BOE-A-1978-30906) cita el «Real Decreto 2550/1978»; el propio RD es el
  **2560/1978** (BOE-A-1978-27525). Manda el RD.
- LO 2/1982: el art. 3 figura con vigencia 01-01-2015 aunque la LO 3/2015 se publicó el
  31-03-2015; no lo cito en el tema por su contenido, así que no afecta.
- Ley 2/2026 (LAULA 9): el `.redacciones.tsv` da «publicada 20260320»; el diario del BOE, el
  03-04-2026. No uso la fecha de publicación en el tema; sí la de vigencia (20-06-2026, nota del
  consolidado).
- Error mío corregido gracias a la lente: el día de Andalucía está en el **art. 3.4** del EAA,
  no en el 4.

## 7. Lentes pasadas (a título de autocomprobación)

- Script propio de negritas contra todo el corpus (normalizado): 1.129 negritas, no literales
  sólo las siglas y «Artículos 82 a 85.».
- `refutar_prosa.py`: 0 hallazgos (una sigla XML quitada).
- `refutar_exactitud.py` con las seis fuentes: 564 negritas por bloque, 8 «no literales»; 139 por
  paréntesis, 9. **Los 17 son falsos positivos de atribución**: citas del preámbulo del EAA y de
  la DA única de la reforma de 2011 (no están en articulado), del RD 2560/1978 y de la fórmula de
  promulgación, de disposiciones adicionales y transitorias, del título del Título III del EAA,
  del art. 81.1 dentro del bloque del 147 y del fallo de la STC 111/2016. Todas comprobadas
  literales por el script de corpus.
- `refutar_modo.py` (sólo con la CE; con varias fuentes mezcla artículos homónimos de normas
  distintas y da 55 avisos sin sentido): 3 avisos, falsos positivos («obligatorio» del
  referéndum del 168.3, «debe» de la DT 4.ª, «ha de ser veraz» del 20.1.d).
- `refutar_citas.py`: 0 tramos (no hay citas en bloque salvo el enunciado).
- Tablas: número de columnas coherente en todas.

## 8. Otros ficheros tocados

- Ninguno del repositorio salvo el tema y este informe.
- **Aviso**: ejecuté por error `herramientas/indice.py` **sin argumentos**; recorre los temas de
  `portadas.tsv` (no los de Canal Sur) y los esquemas, y abortó con una excepción. Comprobé con
  `git status` que no dejó cambios en ningún fichero. El índice del tema 1 queda vacío, como
  pide el encargo.
- **Aviso**: el scratchpad es compartido con otros agentes; uno sobrescribió mi
  `scratchpad/negritas.py` con el suyo del tema 10. Pasé a nombres con prefijo `t01_`.
