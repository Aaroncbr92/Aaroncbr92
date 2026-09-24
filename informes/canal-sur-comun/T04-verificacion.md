# T04 · Verificación · Ley 13/2022 y Ley 10/2018

Tema: `temas/canal-sur-comun/04-ley-13-2022-y-ley-10-2018.md`. Fase 3 del CICLO (verificar,
corrige). Leídos antes: `ENCARGO.md`, `CICLO.md`, `metodo/MANUAL.md`, `metodo/ENCARGOS.md`, y los
informes `T04-investigacion-lgca.md`, `T04-investigacion-ley-10-2018.md` y `T04-redaccion.md`.

**Fecha de lectura de todos los preceptos: 24-09-2026**, redacción vigente ese día, sobre:

- los volcados de `fuentes/canal-sur/` (`BOE-A-2022-11311`, `BOE-A-2018-15240`, `BOE-A-2005-655`,
  `BOE-A-2007-5825`) y sus `.redacciones.tsv`;
- `boe.py --fecha 20190101 | 20210101 | 20220101 precepto` para las redacciones anteriores de la
  Ley 10/2018 (arts. 3, 7, 8, 9, 31, 32, 35, 41, 44, 46, 51);
- la API de datos abiertos del BOE: texto completo en XML de las dos leyes (todas las versiones de
  cada bloque, con sus notas), el bloque `dt` de la Ley 10/2018 (tablas de la DT 1.ª en sus dos
  redacciones), el `dt-2` de la Ley 13/2022, el análisis de la Ley 10/2018 y los metadatos de
  `BOE-A-2023-25886`, `BOE-A-2024-8716`, `BOE-A-2010-5292`, `BOE-A-2008-1185`; el sumario XML de
  `BOE-A-2024-12561` (providencia de 17-06-2024, BOE 21-06-2024) y de `BOE-A-2025-5737`
  (STC 40/2025, BOE 21-03-2025).

## 1. Qué se releyó

Cada precepto que el tema cita, en su redacción vigente:

- **Ley 13/2022**: arts. 1, 2 (2.10), 4 a 15, 33, 35, 36, 50 a 66, 67 a 71 (solo rúbricas, para
  la descripción del capítulo V), 72 a 75, 78, 79, 82, 83, 84, 95 a 109, 118, 124, 153, 155, 157,
  158; DT 2.ª (con sus categorías por la API) y 4.ª; DF 6.ª, 7.ª, 8.ª y 9.ª; derogatoria única;
  rúbricas de los diez títulos y de los capítulos de los títulos III y VI. Recuentos: 166
  artículos, 5 DA, 7 DT, 1 DD, 9 DF; 229 bloques, 1 redacción cada uno, 210/4/15 por fecha de
  aplicación (los 4 son los arts. 88-91); sin avisos de reforma cruzada.
- **Ley 10/2018**: arts. 1 a 4, 6 a 13, 19, 20, 22, 23, 25, 27, 31, 32, 35, 37, 41, 43 a 48, 50,
  51, 54, 66, 78; DA 3.ª; DT 1.ª; preámbulo (estructura y cita de los arts. 69, 70 y 210 del
  Estatuto). Estructura: 82 artículos; rango de artículos de cada título comprobado sobre el
  volcado.
- **Cadenas de redacción** de la Ley 10/2018, leídas enteras en cada versión: art. 3 (2), 7 (2), 8
  (2), 9 (3), 31 (2), 32 (2), 35 (2), 41 (2), 44 (2), 46 (4), 51 (2) y DT 1.ª (2). Cada «qué
  decía» del tema y cada norma que lo cambió se contrastó con las notas del consolidado (qué
  artículo de qué decreto-ley modifica qué apartado).
- **Ley 1/2004**: art. 1 (una redacción) y el estado del art. 4. **Estatuto**: arts. 69, 70, 210.

## 2. Aviso de incisos anulados (CICLO)

- Busqué en el XML del BOE, versión vigente de **cada bloque** de las dos leyes, las marcas
  `<strong>`: en la Ley 13/2022 no hay ninguna; en la Ley 10/2018 solo marcan «(Suprimido/a)» (arts.
  3.2.n, 21, 41.2.a, 51.3, 63, DA 1.ª, DA 4.ª, DF 5.ª). **Ningún precepto citado lleva inciso
  anulado.**
- Único bloque citado con nota de sentencia del TC: **art. 4 de la Ley 1/2004** («(Anulado)», STC
  40/2025). El tema no lo estudia y lo declara en «Lo que este tema no da». Comprobé que la
  «Redacción anterior» que reproduce el BOE es, línea a línea, el texto de la DF 1.ª de la Ley
  10/2018 (30 líneas; solo difiere la línea del rótulo por las comillas): lo que dice el tema es
  exacto.
- **Art. 66 de la Ley 10/2018**: sus notas del TC son de suspensión (2020), levantamiento y
  desistimiento (Auto 68/2021), no de nulidad. Las negritas del XML están solo en la versión
  suspendida de 2020 («párrafos destacados»); la vigente (DL 3/2024) no trae ninguna.
- STC 40/2025: el título del BOE confirma «nulidad de los preceptos legales que reforman la Ley de
  creación del Consejo Audiovisual de Andalucía» y la convalidación del DL 2/2020 por la
  Diputación Permanente. Lo que el tema dice de ella es exacto.

## 3. Correcciones hechas en el tema

| # | Dónde | Qué decía | Qué dice | Precepto (leído 24-09-2026) | Error |
|---|---|---|---|---|---|
| 1 | Tabla de reformas, DL 2/2020 | «Reescribió, entre otros, los artículos 9, 44 y 46 y la disposición transitoria primera» | «Modificó, entre otros, los artículos 9 (apartados 2 y 3), 44 y 46 y la disposición transitoria primera (apartados 2 y 3)» | Notas BOE: «Se modifican los apartados 2 y 3 por el art. 28.1 del Decreto-ley 2/2020» (art. 9); «Se modifican los apartados 2 y 3 por el art. 28.18» (DT 1.ª) | 9 |
| 2 | Tabla de reformas, DL 4/2021 | «26/03/2021» sin más | «26/03/2021, fecha que da el BOE consolidado, con la advertencia de que su vigencia se rige por la disposición final 11.4 del propio decreto-ley» | Nota BOE al art. 37: «Téngase en cuenta, en cuanto a la vigencia de esta modificación, lo que establece la disposición final 11.4 del citado Decreto-ley» | 6 |
| 3 | Ley 10/2018, «Las autoridades audiovisuales en Andalucía» | potestad sancionadora repartida entre órgano directivo y Consejo «(artículo 66.3)» | añade que la revocación definitiva de la habilitación para emitir por infracciones muy graves la acuerda el Consejo de Gobierno, a propuesta de la persona titular de la Consejería (66.3.b) | Art. 66.3.b): «No obstante lo anterior, la revocación definitiva de la habilitación para emitir… será acordada por el Consejo de Gobierno» | 6 |
| 4 | Principios, tras la tabla del título I | «rige para Canal Sur tal cual» | «rige también para Canal Sur» | DF 6.ª uno (el título I es básico); pero 6.4 y 10.5 hablan de lo estatal, así que «tal cual» no se sostiene | 9 |
| 5 | Art. 15.4.d) | «alto contenido en sal, azúcares o grasas» | «alto contenido en sal, azúcares, grasa, grasas saturadas o ácidos grasos trans» | Art. 15.4.d) | 6 (menor) |
| 6 | Art. 15.5 | fomentará, «**de acuerdo con el principio…**» | fomentará, «**cuando proceda, de acuerdo con el principio…**» (literal y con la salvedad) | Art. 15.5: «fomentará cuando proceda, de acuerdo con…» | 6 |
| 7 | Contraste de principios, fin del art. 2 de la Ley 10/2018 | «hay principios andaluces sin artículo propio en el título I estatal: la libre elección (b), el medioambiente (m) y la defensa del servicio público (n)» (se leía como lista cerrada) | «…; entre ellos, la libre elección (b)…» | Art. 2.1 de la Ley 10/2018 frente a los arts. 4-15 de la Ley 13/2022: tampoco tienen artículo propio la d), f), i) o ñ) | 3 |
| 8 | Art. 98.2 | la CNMC «firmará un acuerdo de corregulación» con los prestadores | «…», entre otros, con los prestadores | Art. 98.2: «firmará un acuerdo de corregulación… entre otros, con…» | 6 (menor) |
| 9 | Menores, Ley 10/2018, entradilla | el DL 3/2024 «sustituyó casi todas sus reglas propias sobre menores por remisiones» | «sustituyó varias de sus reglas propias sobre menores por remisiones a la Ley 13/2022 y suprimió otras» | Siguen propias el 8.b-c, 31.1.e e i, 31.2.c, 41.2.b-e; el 41.2.a se suprimió sin remisión (nota: art. 59.18 DL 3/2024) | 9 |
| 10 | Tabla de la cadena del art. 9, fila DL 3/2024 | «la radio se sujeta a los artículos 84 y 101 de la Ley 13/2022» | «el derecho sobre la radio se reconoce «sin perjuicio de lo dispuesto en los artículos 84 y 101 de la Ley 13/2022»» | Art. 9.3 vigente | 4 |
| 11 | Mandato-marco y contrato-programa | «Los plazos del ámbito autonómico son máximos…; los estatales, fijos» | «…; los estatales se dan como «un periodo de ocho años» (54.1) y «de cuatro años» (55.1), sin «máximo»» | Arts. 54.1, 54.2, 55.1, 55.2 («fijos» no está en la ley) | 9 |
| 12 | Tabla de franjas (art. 99) | «**De 22:00 a 6:00**», «**De 1:00 a 5:00**» (x2), «**esoterismo y paraciencias**» en negrita no literal | «**Entre las 22:00 y las 6:00 horas**», «**Entre la 1:00 y las 5:00 horas**», programas relacionados con «**el esoterismo y las paraciencias**» | Arts. 99.2.c), 99.5, 99.6 | negrita no literal |
| 13 | Tabla de cuotas (arts. 102-103) | «**5 horas semanales**» (x3), «**15 horas semanales**» (x2) | «**cinco horas semanales**», «**quince horas semanales**» | Arts. 102.1.b-c, 102.2.b-c, 103.1.b | negrita no literal |
| 14 | Accesibilidad, entradilla | «**en vigor desde el 9 de julio de 2023**» en negrita | en redonda | Es un dato calculado (DF 9.ª: «transcurrido un año»), no texto de la ley | negrita no literal |
| 15 | Mandato-marco | «**seis objetivos generales**» en negrita | en redonda | Art. 54.3.a) no dice «seis objetivos generales» | negrita no literal |
| 16 | Art. 118.3 | «**respetando sus proporciones**» | «**respetando las proporciones establecidas en el mismo**» | Art. 118.3 | negrita no literal |
| 17 | Otras piezas, derecho de acceso | «un mínimo de **doce horas semanales**» | en redonda | Art. 11.2: «computado en periodo semanal no sea inferior a doce horas» | negrita no literal |
| 18 | Trazabilidad, punto 2 | citaba sin cadena el «artículo 73 (dos)» de la Ley 10/2018 | quitado | El tema no cita el art. 73 de la Ley 10/2018 (solo el 73 de la Ley 13/2022) | 1 |
| 19 | Trazabilidad, punto 5 | recurso 1998/2020 contra los «artículos 37, 66.3, 72, 74, 80 y 81», sin más | añade que las notas del consolidado lo asocian al art. 40, no al 37, y que el 66.3 vigente no trae incisos anulados | Análisis BOE (dice 37) frente a las notas de los bloques: la versión `BOE-A-2020-4873` está en los arts. 40, 66, 72, 74, 80 y 81, no en el 37 | 1 |
| 20 | Ficha | Extensión «EXTENSION» | «18.386 palabras» | Cifra de `indice.py` | — |

Índice: generado por `indice.py` (22 epígrafes `##`/`###`).

## 4. Lo que se comprobó y está bien (sin tocar)

- **Cadenas de redacción de la Ley 10/2018**: todas las que da el tema son exactas, cotejadas en
  cada versión: art. 3.1 (encabezado Ley 7/2010 a Ley 13/2022; 3.1.m de 2018 con «a través de
  empresas o sociedades de capital 100% público» y «el prestado por el ente público RTVA»); art. 7
  (cláusula de «la diversidad étnica de Andalucía» suprimida); art. 8 (cinco letras; a) y e)
  pasan a b) y c); b), c) y d) suprimidas, con la cita «por el Consejo Audiovisual de Andalucía»);
  art. 9 (siete apartados, 100 %/15 h diarias autonómica, 75 %/8 h diarias local, «Se reconoce»;
  DL 2/2020 quita lo local; DL 3/2024 cuatro apartados, «Se garantizará»); art. 31.1.f (2018:
  «Evitar la difusión», «o personas con discapacidad», «en todo caso la difusión de contenidos
  pornográficos y de violencia gratuita»); art. 31.1.e, h, i sin cambio; art. 32 (2018: cinco
  letras; franjas 7-9 y 17-20 laborables, 9-12 y 17-20 sábados, domingos y festivos; menores de 12
  años; responsabilidad **solidaria**); art. 35 (2018: «producción en castellano», art. 5.3 Ley
  7/2010); art. 41.2.a (juegos de azar y esoterismo, suprimida por el art. 59.18 del DL 3/2024);
  art. 44 («siempre bajo el régimen de gestión directa» y «gestión directa» suprimidos por el DL
  2/2020); art. 46, cuatro redacciones exactamente como en la tabla (2018 directa para ambos, con
  40.2 Ley 7/2010 y 85.2 LBRL; 2020 local «podrá gestionarse por cualquiera de las formas», 210
  del Estatuto, cae la prohibición de información diaria, renovación automática; 2021 sin
  autorización del órgano directivo; 2024 arts. 72, 75 y 29); art. 51.3 suprimido por el DL
  26/2021; DT 1.ª (apartado 2 y 3 cambiados por el DL 2/2020).
- **Cuotas y porcentajes de accesibilidad**: 80 % / 90 % / 30 % / 30 %; 5 h / 15 h semanales de
  signos y de audiodescripción; acceso condicional 5 h audiodescritas e incorporación gradual de
  signos; a petición, incorporación gradual; «desde el inicio de la prestación» en 102.1.a, 103.1.a
  y 104.1.a pero no en 102.2.a; contenido obligado de las horas de signos (noticiarios, infantil…)
  y de las audiodescritas (películas y series); DT 4.ª (2 M€, 2 %, 1 %). Tablas de la DT 1.ª de la
  Ley 10/2018 cotejadas celda a celda en sus dos redacciones (100 % y 5/8/12/15 h diarias;
  25/45/65/75 % y 1/2/4/8 h diarias; 2018 incluía la local en el apartado 2).
- **Franjas y reglas de menores**: 22:00-6:00 (+18); 1:00-5:00 esoterismo y juego; «solo podrán»
  en 99.5, 99.6 y 83.4 frente a «podrán» en 83.3 (el tema lo dice bien); las dos salvedades de
  loterías (incluida «o por la correspondiente legislación autonómica») y concursos; 99.2 a-c,
  99.3, 99.4; 95, 96, 97, 98.1-3 y 98.7; DT 2.ª (apta, +7, +12, +16, +18, X); art. 124.1 (siete
  conductas), 124.2, 124.3; infracciones 157.9, 157.11, 157.12, 158.7-10, 158.11-14, 158.17, y su
  atribución al Consejo Audiovisual por el art. 66.3.c) de la Ley 10/2018.
- **Servicio público**: arts. 50-66 y 72-75 de la Ley 13/2022 (ocho y cuatro años; «periodo
  máximo» solo en lo autonómico; seis objetivos del 54.3.a; once extremos del 55.3; 10 % y cuatro
  años del 64; cuatro condiciones del 73.1; 1 de abril del 74.1.c); 33.2 y 82.2; 118 (6 %, 70 %,
  45 %, 12 %); Ley 10/2018 arts. 2.2, 44-48, 50, 51, 54.3, 37.c, 35.
- **Identificación**: DF 6.ª, 8.ª, 9.ª (tabla literal), derogatoria 1.b), 2.10 (cuatro supuestos),
  153.1, 153.2, 153.5, 155.4; rúbricas de títulos y capítulos; RD 1138/2023 y RD 444/2024 (título y
  fecha de BOE por la API); DL 26/2020 (deja sin efecto la supresión del art. 40 y cambios de los
  66, 74, 80 y 81), DL 26/2021 (arts. 46 y 51), DL 3/2024 (supresión de art. 21, DA 1.ª y DF 5.ª);
  recurso 3473-2024 (providencia 17-06-2024, BOE 21-06-2024); Estatuto 69.1, 70 (vía preámbulo) y
  210.1-3.
- Siglas: todas presentadas antes de su primer uso (RTVA, CSRTV, BOE, BOJA, RTVE, CE, CNMC; CESyA y
  CNSLE en el art. 109).

Quité nada por no poder confirmarlo: **cero afirmaciones suprimidas**. Lo que no se puede
confirmar ya estaba fuera del cuerpo y declarado en notas y en «Lo que este tema no da» (art. 4
de la Ley 1/2004; recurso 3473-2024; convalidaciones; fecha jurídica de los arts. 39 y 94;
articulación DT 1.ª / art. 9 / 31.1.h / 102.2; remisión colgada del 48.2 al 21.3; criterios de la
DT 2.ª).

## 5. Lentes automáticas

Corridas al final, sobre el tema corregido, con las cuatro fuentes
(`BOE-A-2022-11311`, `BOE-A-2018-15240`, `BOE-A-2005-655`, `BOE-A-2007-5825`).

```
refutar_prosa.py      hallazgos de prosa: 0   (tejido conectivo 0, frases repetidas 0, siglas sin presentar 0, negritas rotas 0)
refutar_exactitud.py  negritas comprobadas: 442 ; no literales: 134
                      citas con el artículo entre paréntesis: 114 comprobadas ; no literales: 43
                      sin comprobar: 12 remiten a otra norma ; 0 con un artículo que no está en las fuentes
refutar_citas.py      tramos de cita comprobados: 1 ; no literales: 0
refutar_modo.py       hallazgos: 21 (las 4 fuentes juntas; 50 bloques del tema comparados)
                      por separado: 6 contra la Ley 13/2022 (49 bloques) ; 14 contra la Ley 10/2018 (36 bloques)
refutar_documento.py  no aplica: el tema no se apoya en documentos fuera del BOE
```

**Exactitud.** Antes de corregir: 143 negritas y 47 citas no literales. Las 170 entradas que la
lente lista al final las cotejé una a una contra todas las fuentes y todas las redacciones (texto
XML de la API de las dos leyes, con versiones anteriores y tablas):

- **104 son literales** en otro bloque o en otra redacción: la lente las mide contra el artículo
  que tiene más cerca en el tema, y aquí casi todo se cita desde una disposición (DF 9.ª, DF 6.ª,
  DA 3.ª, DT 1.ª), desde la redacción de 2018 de un artículo (cadenas) o desde el otro texto legal
  con la misma numeración. Falsos positivos.
- **63 son rótulos** de párrafo o de celda («Características (15.2).», «Cadena de redacciones:
  dos.», «La pieza autonómica (98.7)», «El error típico»…). Falsos positivos.
- **3 son literales del título de los reales decretos** 1138/2023 y 444/2024 («en desarrollo del
  artículo 94»), comprobados en los metadatos del BOE. Falsos positivos.
- Las **no literales de verdad** eran las nueve de las correcciones 12 a 17, ya arregladas.

**Modo.** Todas las líneas explicadas:

- **15 por colisión de numeración** (la propia lente lo avisa): arts. 5, 7, 12, 42, 53, 57, 61, 65,
  67-71, 69, 70, 75, 78, 105-109 y 124 miden un bloque del tema que habla de un artículo de la Ley
  13/2022 (o del art. 42 del Código de Comercio) contra el artículo del mismo número del Estatuto,
  de la Ley 1/2004 o de la Ley 10/2018. El art. 78 de la Ley 10/2018 que el tema cita es solo el
  78.3; la salvedad marcada es la del 78.2, que el tema no usa. Falsos positivos.
- **arts. 88-91**: el tema solo da su fecha de entrada en vigor (DF 9.ª), no su contenido; la
  salvedad marcada no tiene dónde ir. Falso positivo. En las pasadas por separado, los avisos de 53, 62, 64, 73,
  74 y 75 contra la Ley 10/2018 son también bloques de la Ley 13/2022, donde el modo verbal del
  tema coincide con la ley («deberá contar» 53.3; «debiendo respetar» 62.2; «podrán mantener» 64.1;
  «requerirán» 74.3; «gestionarán de forma directa» 75.2).
- **art. 210**: la salvedad «Sin perjuicio de lo dispuesto en el apartado anterior» (210.2) sí
  está en el tema, citada literal. Falso positivo.
- **arts. 83 y 99**: las salvedades de loterías y concursos están en el tema (99.6 las desarrolla y
  83.4 remite a «las mismas dos salvedades»). Falso positivo.
- **art. 8**: la lente ve «obligatoria» contra el art. 8 vigente; el tema la usa para la redacción
  de 2018, que decía «estarán obligadas a señalizar». Falso positivo.
- **art. 140** (solo en la pasada contra la Ley 13/2022): la lente asigna a la fila del art. 140 de
  la tabla de la DF 9.ª el texto que sigue (reales decretos, estructura); el tema no dice nada del
  art. 140 salvo su entrada en vigor. Falso positivo.
- **art. 66**: era un hallazgo bueno (revocación por el Consejo de Gobierno, 66.3.b) y está
  corregido (corrección 3); la lente lo sigue marcando porque el tema lo recoge sin la fórmula «no
  obstante».

## 6. Puntos que dejo a la refutación

- El BOE (análisis) dice que el recurso 1998/2020 afectaba al art. 37; las notas de los bloques lo
  ponen en el 40. El tema da los dos datos; no lo resuelvo.
- Las tablas de horas diarias de la DT 1.ª conviven con el art. 9 sin cifras y con el 102.2
  estatal: el tema lo declara abierto, y así debe seguir mientras ninguna norma lo resuelva.

## 7. Ficheros tocados

- `temas/canal-sur-comun/04-ley-13-2022-y-ley-10-2018.md` (correcciones, índice por `indice.py`,
  Extensión).
- Creado este informe, `informes/canal-sur-comun/T04-verificacion.md`.
- Nada más. Los XML y las comprobaciones intermedias quedaron en la carpeta temporal de la sesión;
  no toqué `fuentes/`. (`git status` muestra modificados `T08-redaccion.md` y `10-proteccion-de-datos.md`:
  no son míos.)
