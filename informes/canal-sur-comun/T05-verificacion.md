# T05 · Verificación · Ley 18/2007 (RTVA)

Fase 3 (verificar) del tema `temas/canal-sur-comun/05-ley-18-2007-rtva.md`. Leídos antes enteros:
`ENCARGO.md`, `CICLO.md`, `metodo/MANUAL.md`, `metodo/ENCARGOS.md`, `T05-redaccion.md`,
`T05-investigacion-ley-organos.md` y `T05-investigacion-csrtv-control.md`.
**Fecha de lectura de todos los preceptos: 24-09-2026**, en la redacción vigente ese día.

## 1. Qué se ha releído

- **Ley 18/2007** (`BOE-A-2008-1185`): el volcado entero, bloque a bloque (exposición de motivos,
  37 artículos, 4 adicionales, 3 transitorias, derogatoria, 2 finales), con su `.redacciones.tsv`.
  Redacciones anteriores sacadas de nuevo con `boe.py --fecha`: exposición de motivos (20100101),
  art. 8 (20100101), 14 (20100101), 15 (20100101), 18 (20100101 y 20140101, la del DL 3/2013),
  20 (20100101 y 20200101). Sin reformas cruzadas: en todos los preceptos la redacción de mayor
  vigencia es también la de publicación más tardía.
- Estatuto (`BOE-A-2007-5825`): 69, 130, 131, 194, 207, 210 a 215, 217 y rótulos de los títulos
  VII («Medio ambiente») y VIII («Medios de comunicación social», arts. 207-217).
- Ley 9/2007 (`BOE-A-2007-19819`): 54, 68 (vigente desde 22-02-2011), 75 (75.2 vigente desde
  14-12-2023, DF 2.ª Ley 5/2023, con su redacción anterior), 76, 77; título IV, cap. II, sección
  1.ª «Órganos colegiados» = arts. 88-96.
- TRLGHP (`BOE-A-2010-5303`): DA única, DD única letra a) (deroga la Ley 5/1983), art. 5.1
  (vigente desde 20-01-2026 por la DF 1.ª de la Ley 7/2025), 97.1, 98.1.
- Ley 7/2025 (`BOE-A-2026-944`): DD única letra a), DF 1.ª, DF 10.ª (vigor a los veinte días
  del BOJA 251 de 31-12-2025 = 20-01-2026); título comprobado en la API del BOE.
- Ley 1/2004 (`BOE-A-2005-655`): 1, 2, 4, 11, 13. Art. 4: el bloque vigente es «(Anulado)» con la
  nota de la STC 40/2025 y la «Redacción anterior» de 28 funciones (contadas; la 14 es la citada).
  Es la presentación del consolidado del BOE; el tema no decide qué redacción rige.
- Ley 1/1988 (`BOE-A-1988-8592`): 1, 2 (vigente desde 13-06-2001), 4.
- Documentos: Acuerdo de fusión (BOJA 219/2015) leído entero; Reglamento del Parlamento
  (consolidado vigente desde 22-10-2025; las dos copias de `documentos/` son idénticas, `cmp`):
  46, capítulo tercero del título decimocuarto, 188-190 y sus notas 50-52; Contrato-Programa
  2024-2026, expositivo IV.
- Comprobado en línea: título de la Ley 2/2019 (XML del BOE); BOJA núm. 100 de 24-05-2024
  (DL 5/2024) y BOJA núm. 111 de 10-06-2024 (Resolución de 4-06-2024, convalidación), en sus
  sumarios oficiales; BOJA núm. 252 de 26-12-2007 y vigencia 15-01-2008 (XML y API del BOE).

## 2. Comprobación de las negritas, precepto a precepto

Script propio (scratchpad, `t05v/negbloque.py`): parte cada fuente del BOE en sus bloques
(`## [id]`), añade los tres documentos, las redacciones anteriores y el programa, y para **cada
negrita** del tema dice en qué bloque(s) aparece literal (espacios y guiones de corte normalizados).
Después comparé a mano, una por una, ese bloque con el precepto que el tema le atribuye.

- **226 negritas comprobadas** (sin contar las etiquetas de ficha y trazabilidad): **226
  encontradas literales**, cada una en el precepto al que el tema la atribuye. Las 2 que la
  primera pasada no encontró (Reglamento 46.2.4.ª y 188) eran cortes de palabra con guion blando
  en el `.txt` («Socie­dades», «especí­ficas»); corregida la normalización, aparecen.
- Las negritas genéricas («podrán», «favorecerán», «producirán», «Redacción anterior») se
  comprobaron en su artículo concreto (24, 29, 29, bloque del art. 4 de la Ley 1/2004).
- Ninguna negrita atribuida a una redacción derogada: las citas de redacciones anteriores (14.1,
  15.3, 18.2, 18.3, 18.4 de 2008 y 2013, 8.2.b, exposición de motivos) van en redonda entre
  comillas, y coinciden con las redacciones sacadas con `--fecha`.

## 3. Mayorías, plazos y composición (atención especial)

Todo confirmado contra el texto vigente y, donde cambió, contra la redacción anterior:

| Dato | Precepto | Anterior | Resultado |
| --- | --- | --- | --- |
| Consejo de Administración: 9 miembros, paridad de género; representante de los trabajadores con voz sin voto, «deberá ratificar» | 14.1 | 15 miembros, «composición equilibrada» | ✓ |
| Quórum mayoría absoluta; acuerdos mayoría simple, voto dirimente | 14.4 | igual | ✓ |
| Sesión ordinaria al menos una vez al mes | 14.5 | igual | ✓ |
| Consejeros: tres quintos, a propuesta de los Grupos; nombra Consejo de Gobierno | 15.1 | igual | ✓ |
| Presidencia: tres quintos «entre los nueve» | 15.2 | «de entre los quince» | ✓ |
| Mandato hasta publicación del decreto de disolución; un año para elegir | 15.3 | seis años no renovable, sin plazo | ✓ |
| Vacantes hasta cumplir el mandato del cesante | 15.4 | «los seis años del mandato» | ✓ |
| Nueve causas de cese; «tres meses continuos»; propuesta por tres quintos en c), d), f); acuerda el Consejo de Gobierno | 16 | 1 redacción | ✓ |
| Dieciséis competencias (a-o con ñ); mayoría absoluta en b), d), f), h), i) | 17 | 1 redacción | ✓ |
| DG: dos tercios; si no, tres quintos; nombra y cesa el Consejo de Gobierno | 18.1 | igual | ✓ (ver corrección 1) |
| DG: mandato de legislatura renovable por periodos iguales; un año | 18.2-18.3 | seis años renovable una vez | ✓ |
| DG vacante: Parlamento, tres quintos, un mes; directivo de mayor nivel; salvo 16.1.b | 18.4 | 2008 y DL 3/2013 (Consejo de Administración, delegación por mayoría absoluta) | ✓ |
| Catorce funciones (a-n); delegación por tres quintos salvo f), i), l), ñ); voz y voto | 19 | 1 redacción | ✓ |
| Consejo Asesor 15 = 1+1+3+2+8 | 20.1 | 17 = 2+2+3+4+6 (2008); 13 = 1+1+3+2+6 (2019) | ✓ (ver corrección 12) |
| Asesor: mandato de legislatura; vacantes hasta la disolución | 20.3-20.4 | seis años | ✓ |
| Carta seis años; Contrato-Programa tres años | 7.3, 8.1 | igual | ✓ |
| Composición equilibrada 60/40 | DA 3.ª | — | ✓ |
| Asesor en dos meses; Reglamento del Consejo en dos meses; primera elección DG por mayoría absoluta tras un mes | DA 4.ª, DF 1.ª, DT 2.ª | — | ✓ |
| Comisiones permanentes en veinte días; DG comparece a iniciativa de un Grupo o de un Diputado con la firma de otros cuatro | RPA 46.3, 189.1 | — | ✓ |

Recuentos rehechos contando en la fuente: 37 artículos; 9 principios (4.1); 15 mandatos (4.3);
3 órganos (13); 9 causas (16.1); 16 competencias (17.1); 14 funciones (19.2); 4 materias (8.2);
4 indelegables (19.3); 28 funciones en la redacción anterior del art. 4 de la Ley 1/2004.

## 4. Desajustes declarados: siguen sin resolverse por deducción

- **Art. 9 y fusión**: sigue dicho tal cual (art. 9 con una sola redacción; CSRTV por el Acuerdo
  de 2015 y el Contrato-Programa). Una frase de «La organización de CSRTV» aplicaba el 9.5-9.6 a
  CSRTV como si la ley la nombrase: corregida (corrección 9) para que la exigencia se atribuya a
  «las sociedades que nombra» el art. 9 y la de CSRTV a sus estatutos, que invocan ese artículo.
- **«Título VII» / Título VIII**: dicho como desajuste, sin corregir la ley. ✓
- **Art. 4 de la Ley 1/2004**: «(Anulado)», nota y redacción anterior citadas; el tema no decide
  qué redacción rige ni da números de función como dato. ✓
- **Art. 87 de la Ley 5/1983 → 98.1 TRLGHP**: en la identificación estaba declarado como
  correspondencia por contenido, pero en «El resto del control externo» se afirmaba «hoy la regla
  está en el artículo 98.1»: corregido (corrección 17).
- Ley 4/1986 derogada, «voz y voto» del 19.4, tipo de agencia del 68.1, paridad no definida:
  siguen dichos sin resolver. ✓

## 5. Correcciones aplicadas en el tema

| # | Dónde | Decía | Dice | Precepto / motivo (error del catálogo) |
| --- | --- | --- | --- | --- |
| 1 | Párrafo «qué se puede preguntar»; «Qué elige el Parlamento» (tras la tabla); cuadro «Todo lo que la ley pone en manos del Parlamento» | «en segunda votación» / «en segunda» / «tres quintos en segunda» | «si no se alcanzan en primera votación» | 18.1: «En el caso de no alcanzarse la citada mayoría en primera votación». La ley no habla de segunda votación (9, deducción) |
| 2 | Mismo párrafo | «el plazo de un año para elegir los órganos» | «…para elegir el Consejo de Administración y la Dirección General» | 15.3 y 18.3; el Consejo Asesor no tiene ese plazo (20) (6/9) |
| 3 | Mismo párrafo | «un punto que el tribunal puede tomar por sorpresa» | «un punto que conviene tener claro» | No hay exámenes anteriores (encargo) (9) |
| 4 | Remisiones desfasadas, Ley 5/1983 | «Esa ley la sustituyó el texto refundido…» | «Esa ley la derogó, y la sustituyó por un texto refundido, el Decreto Legislativo 1/2010… (disposición derogatoria única, letra a)» | DD única a) del DLeg 1/2010 (precisión) |
| 5 | Régimen de sociedad mercantil, TRLGHP 5.1 | «por la Ley 7/2025» | «por la disposición final primera de la Ley 7/2025» | DF 1.ª Ley 7/2025 (precisión) |
| 6 | Definición de la función de servicio público | «Los elementos que suelen preguntarse» | «Los elementos de la definición» | Sin apoyo: no hay exámenes anteriores (9) |
| 7 | Accesibilidad, DA 2.ª | «las programaciones generalistas…» | «la totalidad de las programaciones generalistas…» | DA 2.ª: «la totalidad de las programaciones generalistas» (6) |
| 8 | Organización, tras la cita del 214.2 | «(dos tercios y, en segunda, tres quintos)» | «(dos tercios y, si no se alcanzan en primera votación, tres quintos)» | 18.1 (9) — incluida en la 1 |
| 9 | «La organización de CSRTV», primer punto | «La ley exige un Administrador único que es, a la vez, titular de la Dirección de la sociedad (9.5 y 9.6).» | «El artículo 9 exige a las sociedades que nombra un Administrador único…; los estatutos de 2015 establecen el Administrador Único de CSRTV «De acuerdo con lo dispuesto en el artículo 9» de la ley (artículo 12.º).» | 9.5-9.6 hablan de Canal Sur Radio y Canal Sur Televisión; estatutos art. 12.º. Evita resolver el desajuste del art. 9 por deducción (9) |
| 10 | Representante de los trabajadores | «…y las mismas incompatibilidades, con una salvedad…» | Las de la primera frase del 15.6 con la salvedad; el régimen de altos cargos y la incompatibilidad con diputado el 15.6 los refiere a «los miembros del Consejo de Administración» | 15.6 (segunda y tercera frases) y 14.1 («no tendrá la condición de Consejero») (6/9) |
| 11 | Consejo Asesor, 20.2 | «Lo convoca el Consejo de Administración, no su Presidencia ni la Dirección General;» | «Lo convoca el Consejo de Administración,» | La negación no está en la fuente (9) |
| 12 | Tres redacciones del art. 20, nota final | «En 2019 … la letra e) [pasó] a hablar del «Consejo de las personas Consumidoras y Usuarias»» | El cambio de nombre es de **2024** (DL 5/2024); en 2008 y 2019 decía «Consejo de los Consumidores y Usuarios» | 20.1.e) vigente a 20200101: «Consejo de los Consumidores y Usuarios de Andalucía» (**7/8, fecha de la reforma errónea**; el error venía del informe de redacción) |
| 13 | Tabla de las tres redacciones del art. 20 | «Corporaciones locales (FAMP)» y, después de la tabla, «FAMP es la …» | «Corporaciones locales (las designa la Federación Andaluza de Municipios y Provincias)»; frase de la sigla suprimida | Sigla usada antes de presentarse (5) |
| 14 | Reglamento del Parlamento, 46 | «Es una comisión permanente no legislativa.» | «Es una comisión permanente que no figura entre las legislativas:» | 46.1-46.2 no la califican; se dice lo que consta (9, menor) |
| 15 | Reglamento, notas | «remiten, en estos artículos, a tres normas internas» | «remiten, en este capítulo, …» | La nota 50 (acuerdo de 2010) va en el rótulo del capítulo tercero, no en un artículo (1, menor) |
| 16 | Cuadro «Todo lo que la ley pone en manos del Parlamento» | «El Pleno elige a la Dirección General (…) y cubre su vacante» | «El Pleno elige a la Dirección General (…); el Parlamento cubre su vacante» | 18.4 dice «el Parlamento», no «el Pleno» (1) |
| 17 | El resto del control externo, art. 37 | «hoy la regla está en el artículo 98.1» | «la obligación de rendir cuentas a esos tres órganos figura hoy en el artículo 98.1 … (correspondencia por el contenido, que ninguna norma leída declara)» | Coherencia con la identificación; no resolver la remisión por deducción (9) |
| 18 | Ficha, Extensión | «14.959 palabras» | «15.087 palabras» | Cifra de `indice.py` tras las correcciones y el índice |

Además, `indice.py` rellenó el índice entre `<!-- indice -->` y `<!-- /indice -->` (42
epígrafes). El tema no está en `herramientas/portadas.tsv`, así que el script no tocó la ficha
(«sin portada»); la Extensión se puso a mano con su cifra.

Nada quitado por no confirmado: todo lo demás del cuerpo se confirmó en su precepto.

## 6. Lentes automáticas (tras las correcciones)

```
refutar_prosa.py      hallazgos de prosa: 2
refutar_exactitud.py  negritas comprobadas: 0 ; citas con el artículo entre paréntesis: 126 comprobadas ; no literales: 21
                      sin comprobar: 11 remiten a otra norma
refutar_citas.py      tramos de cita comprobados: 0 ; no literales: 0
refutar_modo.py       hallazgos: 0
refutar_documento.py  (3 documentos + 7 volcados + programa) negritas comprobadas: 224 ; no literales: 2 ; cifras huérfanas: 0
indice.py             15087 palabras · 42 epígrafes
```

- **prosa (2)**: «Redacción anterior (hasta el 27 de junio de 2019)» ×3, rótulo intencionado en
  14.1, 15.3 y 18.2; «LGBTI» es parte del nombre oficial «Consejo Andaluz LGBTI» (20.1.e), no
  sigla del tema. Falsos positivos.
- **exactitud**: su modo de negritas **no miró nada** (0: ancla en «**Artículo N**», que el tema no
  usa). Su segundo modo miró 126 citas; las **21 «no literales» son falsos positivos**, revisadas
  una a una: toman el número del paréntesis siguiente o del contiguo, no el de la cita (p. ej. el
  2.2 leído como «art. 210» porque la frase siguiente cita el 210.1 del Estatuto; la DT 2.ª como
  «art. 13» por el epígrafe siguiente; el 14.1 como «art. 15» por el «(15.3)» siguiente; el 18.5
  como «art. 9» por el «(9.6)»), o citan artículos del Acuerdo de fusión (1.º, 8.º, 10.º, 12.º,
  Primero, Tercero, Cuarto) o del Reglamento (46, 188, 189, 190), que la lente busca en la Ley
  18/2007. Todas están literales en su precepto real (sección 2).
- **citas**: 0 tramos: el tema no usa bloques de cita salvo el enunciado. **Cero vacío.**
- **modo**: 0 hallazgos (el tramo que mira no lo declara; la comprobación del modo verbal se hizo a
  mano: «podrán» 14.1, 12, 24, 31, 34.2, DA 1.ª; «deberá» 14.1 y 16.2; «deberán» 4.3; «podrá» 19.3).
- **documento**: con todas las fuentes, 224 negritas y 2 «no literales» que son etiquetas
  («Enunciado del programa», «Redacción leída»). Esta lente mira el corpus entero, no el
  precepto; la comprobación precepto a precepto es la de la sección 2 (226 de 226).

## 7. Aviso para las fases siguientes

- El informe de redacción atribuía a 2019 el cambio de nombre del consejo de consumidores; es de
  2024 (corregido, corrección 12).
- La nota del art. 4 de la Ley 1/2004 es sobre la anulación entera del art. 7 del DL 2/2020, no de
  un inciso: no hay negrita perdida que buscar en la página consolidada para lo que el tema cita.

## 8. Ficheros tocados

- `temas/canal-sur-comun/05-ley-18-2007-rtva.md` (correcciones de la sección 5, índice, Extensión).
- Este informe.
- Temporales en el scratchpad, `t05v/` (script, redacciones anteriores, sumarios del BOJA).
- Ningún otro. `git status` muestra modificados otros temas e informes (01, 02, 03, 07, 09, 10,
  T04, T07, T10) que no he tocado: son de otros agentes.
