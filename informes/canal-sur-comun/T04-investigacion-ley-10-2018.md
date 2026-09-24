# T04 · Investigación · Ley 10/2018, audiovisual de Andalucía

Fase 1 (investigar) del punto 4 del temario común de Canal Sur. Parte: la Ley 10/2018.
Fuente: texto consolidado `BOE-A-2018-15240` volcado el 24-09-2026 en
`fuentes/canal-sur/` (el BOE declara el consolidado actualizado el 26-05-2026) y cadenas
de redacciones sacadas con `boe.py precepto` y la API de datos abiertos del BOE.
**Todos los preceptos se leyeron el 24-09-2026.** No se ha tocado ningún otro fichero
del proyecto.

## 0. Avisos sobre la fuente (leer antes que nada)

1. **Normas de reforma.** El volcado rotula las reformas `BOE-A-AAAA-9xxxx`; en el BOE su
   identificador es `BOJA-b-…`. Según el análisis y las notas del BOE: **DL 2/2020, de 9 de
   marzo** (art. 28; vigencia 13-03-2020); **DL 26/2020, de 13 de octubre** (DF 2.ª; deja
   sin efecto la supresión del art. 40 y cambios de los arts. 66, 74, 80 y 81); **DL 4/2021,
   de 23 de marzo** (art. 37.b); **DL 26/2021, de 14 de diciembre** (arts. 46.4 y 51);
   **DL 3/2024, de 6 de febrero** (art. 59; vigencia 17-02-2024), que adapta la ley a la
   Ley 13/2022.
2. **Todas las reformas son decretos-leyes andaluces.** Del 2/2020 consta la convalidación
   (por la Diputación Permanente) en la STC 40/2025 (`BOE-A-2025-5737`). **La
   convalidación de los demás no la he podido confirmar** en el BOE (se publica en BOJA).
3. **Recursos.** Contra el DL 3/2024 hay recurso de inconstitucionalidad n.º 3473-2024,
   admitido por providencia de 17-06-2024 (`BOE-A-2024-12561`), contra el decreto-ley en
   su conjunto; **no he encontrado sentencia** en el BOE a 24-09-2026. La STC 40/2025
   anula el art. 7 del DL 2/2020 (el que reformaba la Ley 1/2004, ver §3) y **desestima
   todo lo demás**, incluido el art. 28 que reformaba la Ley 10/2018.
4. **El volcado pierde las tablas** de la disposición transitoria primera (calendario de
   accesibilidad). Las he leído en la API del BOE (§2.4).
5. **Remisiones colgando en el texto vigente** (no las arreglo, las señalo): el art. 48.2
   remite al «Observatorio Público de Audiencias de Andalucía, previsto en el artículo
   21.3», y el art. 21 está **(Suprimido)** por el DL 3/2024; la DT 1.ª.1 habla de las
   obligaciones de accesibilidad «a los que se refiere el artículo 9», y el art. 9 vigente
   ya no contiene porcentajes ni horas.

## 1. Estructura, objeto y ámbito

Título oficial: **Ley 10/2018, de 9 de octubre, audiovisual de Andalucía** (BOJA núm. 200,
de 16-10-2018). Entrada en vigor: **«el día siguiente de su publicación en el "Boletín
Oficial de la Junta de Andalucía"»** (DF 12.ª) → 17-10-2018.

Índice real (recuento hecho sobre las rúbricas del consolidado): **82 artículos**, 4
disposiciones adicionales, 6 transitorias, 1 derogatoria y 12 finales.

| División | Rúbrica | Arts. |
|---|---|---|
| Título preliminar | Disposiciones generales | 1–4 |
| Título I | Derechos de la ciudadanía | 5–13 |
| Título II | La Administración audiovisual en Andalucía | 14–26 |
| · Cap. I | Organización de la Administración audiovisual | 14–17 |
| · Cap. II | Política audiovisual | 18–26 |
| Título III | Derechos y obligaciones de las personas prestadoras del servicio de comunicación audiovisual | 27–38 (el 27 va antes del cap. I) |
| · Cap. I | Derechos de las personas prestadoras… | 28–30 |
| · Cap. II | Obligaciones… (Sec. 1.ª ante la ciudadanía 31–32; 2.ª ante la Administración audiovisual 33–35; 3.ª específicas 36–38) | 31–38 |
| Título IV | Comunicaciones comerciales audiovisuales | 39–43 |
| Título V | Servicios de comunicación audiovisual | 44–64 |
| · Cap. I | El servicio público audiovisual en Andalucía (Sec. 1.ª Disposiciones generales 44–49; 2.ª Modalidades 50–54) | 44–54 |
| · Cap. II | Servicios… comunitarios sin ánimo de lucro | 55–59 |
| · Cap. III | El servicio… privado de carácter comercial (Sec. 1.ª Régimen jurídico 60–62; 2.ª Negocios jurídicos 63–64) | 60–64 |
| Título VI | Inspección y sanción (Cap. I Disposiciones generales 65–66; II De la inspección 67–70; III Régimen sancionador 71–82) | 65–82 |

Suprimidos hoy: **art. 21** (medición de audiencias), **DA 1.ª** (sistemas de medición de
audiencias) y **DF 5.ª** (código interno regulador), por el DL 3/2024; **DA 4.ª**
(Estatuto de la Información), por el DL 2/2020. También apartados sueltos: 3.2.n), 41.2.a),
51.3, 63.2.c).

**Objeto (art. 1, 1 redacción):** **«regular el régimen jurídico de la comunicación
audiovisual en Andalucía, de acuerdo con la Constitución Española y el Estatuto de
Autonomía para Andalucía, sin perjuicio de la legislación estatal de aplicación.»**

**Ámbito (art. 4, 1 redacción).** Se aplica: a) a los servicios públicos de titularidad de
la Junta; b) a los sujetos a autorización o comunicación previa de competencia de la
Junta; c) a los prestados en Andalucía sin título o sin comunicación previa; d) a personas
relacionadas con la prestación (anunciantes, agencias de publicidad y de medios, y
obligados a colaborar del art. 81). **Excluidos** (4.2): a) titulares de título habilitante
de **cobertura estatal**; b) quienes **«únicamente difundan o transporten la señal»** de
programas con responsabilidad editorial de terceros, «sin perjuicio de» el art. 81.

**Definiciones (art. 3, 2 redacciones; vigente la del DL 3/2024).** El 3.1 arranca hoy
**«Sin perjuicio de las definiciones establecidas en la Ley 13/2022, de 7 de julio, General
de Comunicación Audiovisual»** (en 2018: Ley 7/2010). Para el tema:
- 3.1.m) **«Servicio público de comunicación audiovisual. Aquel que es prestado por
  entidades públicas y cuya titularidad corresponde a la Administración de la Junta de
  Andalucía, a entidades locales de Andalucía o a entes supramunicipales mancomunados, a
  universidades públicas andaluzas o a centros docentes públicos andaluces no
  universitarios.»** (2018: prestado «a través de empresas o sociedades de capital 100%
  público», e incluía expresamente «el ente público RTVA»).
- 3.1.d) Horario no residual: **«El comprendido entre las 8:00 y las 23:00 horas en
  televisión y radio.»**

## 2. Las rúbricas del enunciado

### 2.1. Principios de la comunicación audiovisual

**Art. 2 «Principios inspiradores» (1 redacción, intacto desde 2018).** El 2.1 enumera
**quince** letras, de la a) a la ñ) (a–n más ñ). Las decisivas, literales:
- a) **«La libertad de comunicación audiovisual, entendida como la prestación de servicios
  de comunicación audiovisual por parte de la ciudadanía en el marco del ejercicio
  legítimo de los derechos fundamentales de libertad de expresión y de información.»**
- b) libre elección; c) pluralismo (ver 2.2); d) protección de los derechos fundamentales;
- e) **«La protección de la infancia, la juventud y las personas con discapacidad, así como
  la garantía de accesibilidad universal a los servicios de comunicación audiovisual.»**
- h) **«La objetividad, veracidad e imparcialidad de las informaciones.»**; j) **«La
  accesibilidad universal y el diseño para todas las personas.»**; n) **«La defensa y
  potenciación del servicio público de comunicación audiovisual.»**; ñ) equilibrio entre
  prestadores públicos, comunitarios y privados (la Junta **«tenderá con carácter
  global»**). Las demás: consumidores (f), propiedad intelectual y rectificación (g),
  inclusión (i), alfabetización mediática (k), igualdad (l), medioambiente (m).

El 2.2 añade **tres** principios propios del **servicio público**: a) **transparencia**
«en especial con los relativos a la libertad de comunicación y el pluralismo»; b) fomento
y defensa de la **cultura andaluza** y de los intereses locales y de proximidad, y la
convivencia; colaboración con otras comunidades autónomas; c) **«El buen uso del espacio
radioeléctrico de Andalucía como bien demanial limitado.»**


### 2.2. Pluralismo

- **Art. 2.1.c)** (1 redacción): **«El pluralismo político, religioso y sociocultural en la
  comunicación audiovisual, como condición esencial para el cumplimiento de la libertad de
  expresión, de información y de comunicación, garantizando la libre formación de la
  opinión pública, la diversidad y la cohesión social.»**
- **Art. 7 «Derecho a recibir una comunicación audiovisual plural»** (2 redacciones).
  Vigente (DL 3/2024, art. 59.3): **«…tienen derecho a recibir una comunicación audiovisual
  plural de acuerdo con el principio de pluralismo previsto en el artículo 5 de la Ley
  13/2022, de 7 de julio.»** Redacción 2018: «en los términos previstos en el artículo 4 de
  la Ley 7/2010, de 31 de marzo, **así como aquella que refleje la diversidad étnica de
  Andalucía**». **Esa última cláusula desaparece en 2024.**
- **Art. 11 «Derecho de participación y acceso de los grupos sociales»** (1 redacción):
  las entidades representativas o significativas de la diversidad política, social y
  cultural **«podrán ejercer el derecho de acceso a los servicios de comunicación
  audiovisual públicos»**, **«en horario no residual»** y con duración semanal **«no sea
  inferior a doce horas»**, según reglamento (dieciocho meses).
- **Art. 12** Consejo de Participación Audiovisual de Andalucía (ver §3).
- **Art. 31.1.b)**: obligación de **«Cumplir con el deber de transparencia en relación con
  los aspectos de su actividad que son relevantes para la libertad de comunicación y el
  pluralismo.»**
- **Art. 45.1** (fines del servicio público, 1 redacción): **«Transmitir una información
  veraz, plural, equitativa, crítica y participativa…»**
- **DA 3.ª** (vigente DL 2/2020), criterios de adjudicación de licencias privadas: b)
  **«Las garantías para la libre expresión de ideas y opiniones y el pluralismo.»**

### 2.3. Protección de menores

- **Art. 2.1.e)** (arriba).
- **Art. 8 «Derechos de las personas menores»** (2 redacciones). Vigente (DL 3/2024, art.
  59.4), **tres** letras: **«a) Los derechos que les reconoce el Capítulo I del Título VI
  de la Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual. b) Al acceso a
  contenidos que fomenten valores educativos y formativos acordes con su edad… c) Al
  fomento de estilos de vida saludables y de la dieta mediterránea como patrimonio de la
  humanidad.»** (El cap. I del tít. VI de la Ley 13/2022 se rotula «Protección de los
  menores», leído en `BOE-A-2022-11311`.) La redacción 2018 tenía **cinco** letras y
  **se suprimieron**: b) no perjuicio del desarrollo físico, mental o moral; c)
  prohibiciones adicionales al art. 7.2 Ley 7/2010 (programas con estereotipos sexistas,
  maltrato animal, acciones contra la naturaleza); d) señalización acústica y visual
  **«según los criterios fijados en cada momento por el Consejo Audiovisual de
  Andalucía»** y advertencia verbal en informativos.
- **Art. 31.1** (2 redacciones). e) respetar honor, intimidad e imagen **«especialmente de
  los menores de edad y de las personas con discapacidad»** (sin cambios). f) vigente (DL
  3/2024, art. 59.9): **«Está prohibida, conforme a lo dispuesto en el artículo 95.2 de la
  Ley 13/2022, de 7 de julio, la difusión de los nombres, imágenes y otros datos personales
  que permitan identificar a las personas menores de edad en el contexto de hechos
  delictivos, de emisiones en las que se discuta su tutela o filiación, o relativos a
  situaciones en las que los menores hayan sido víctimas de violencia en cualquiera de sus
  manifestaciones.»** La f) de 2018 decía «Evitar la difusión…» (menores **o personas con
  discapacidad**, como víctimas, testigos o inculpados) y prohibía **«en todo caso la
  difusión de contenidos pornográficos y de violencia gratuita»**: todo eso sale en 2024.
  i) mantener la clasificación por edades y la accesibilidad cuando los contenidos se
  ofrezcan en medios sin restricciones horarias (sin cambios). 31.2.c) hijos menores de
  víctimas de violencia de género **«como víctimas directas»**.
- **Art. 32 «Normas de programación y limitaciones de las comunicaciones comerciales»**
  (2 redacciones). Vigente (DL 3/2024, art. 59.10), entero: **«La programación de las
  personas prestadoras de servicios de comunicación audiovisual autonómicos o locales en
  Andalucía, así como sus contenidos, deberán ajustarse a lo establecido en la Ley 13/2022,
  de 7 de julio.»** En 2018 tenía cinco letras propias: franjas de **protección reforzada**
  (7–9 y 17–20 h laborables; 9–12 y 17–20 h sábados, domingos y festivos), indicativo
  visual obligatorio de calificación, juegos de azar y esoterismo sólo de 1:00 a 5:00, etc.
  **Todo derogado por sustitución.** Es el cambio más preguntable.
- **Art. 41.2** (2 redacciones), comunicaciones comerciales **«emitidas en horario de
  protección de menores»**: b) prohíbe las que inciten a la desigualdad o transmitan
  estereotipos de género (y los anuncios para menores no pueden diferenciar por sexo);
  c) **«Queda prohibido el emplazamiento de producto en programas con importante audiencia
  infantil.»**; d) **«Se limitarán»** las que fomenten alimentación no saludable; e)
  cosificación de la mujer o sexualización de menores. La **a)** (juegos de azar,
  apuestas, esoterismo y paraciencia) está **(Suprimido)** por el DL 3/2024, art. 59.18.
- **Art. 43.2–3**: códigos de conducta (art. 15 Ley 13/2022) para reducir la exposición de
  menores a publicidad de alimentos con alto contenido en sal, azúcares o grasas.

### 2.4. Accesibilidad

- **Art. 2.1.e) y j)** (arriba).
- **Art. 6 «Garantía de accesibilidad universal…»** (1 redacción): **«Se garantizará a toda
  la población que los servicios de comunicación audiovisual sean accesibles, sin que pueda
  existir discriminación por razón de discapacidad, circunstancias económicas, geográficas
  o por cualquier otra condición…»**
- **Art. 9 «Derechos de las personas con discapacidad»** (**3 redacciones**):
  - 2018: siete apartados, con cifras (TV autonómica: subtitulado 100 %, 15 h diarias de
    lengua de signos y 15 h de audiodescripción más todos los informativos; TV local: 75 %
    y 8 h). DL 2/2020 (art. 28.1) quitó las cifras de la TV local.
  - **Vigente, DL 3/2024 (art. 59.5), cuatro apartados:** 9.1 **«Se garantizará el acceso
    universal a los servicios de comunicación audiovisual, de acuerdo con los avances
    tecnológicos, a las personas con discapacidad visual o auditiva.»** (antes «Se
    reconoce»). 9.2 imagen **«real, positiva, digna, inclusiva y no estereotipada y/o
    paternalista»**. 9.3 radio autonómica pública o privada comercial con programas
    subtitulados en sus canales de TDT e Internet, **«sin perjuicio de lo dispuesto en los
    artículos 84 y 101 de la Ley 13/2022»**. 9.4 TV autonómica: programas subtitulados
    **«según métodos de lectura fácil»** para personas con discapacidad intelectual.
    **Desaparecen del art. 9 todos los porcentajes y horas.**
- **DT 1.ª** (2 redacciones; vigente DL 2/2020, art. 28.18). 1: TV **pública autonómica**,
  efectivo **«a 31 de diciembre de cada año»**: subtitulación 100 % (2018–2021); lengua de
  signos y audiodescripción 5 h (2018), 8 (2019), 12 (2020), **15 y todas las informativas
  (2021)**. 2: TV **privada autonómica** (desde 2020 ya no incluye la local): subtitulación
  25/45/65/**75 %**; signos y audiodescripción 1/2/4/**8 h** y todas las informativas. 3
  (redacción 2020): **«Se autoriza a la Consejería…»** a ampliar reglamentariamente los
  plazos del apartado anterior (en 2018, «al órgano directivo»). 4: plan de participación
  de colectivos con diversidad funcional, **aprobado por el Consejo Audiovisual**. 5:
  estudios accesibles **«con la mayor brevedad posible»**. 6: medidas en radio y publicidad,
  **«podrá introducir»**.
- **Art. 31.1.h)** (sin cambio): obligación de **«alcanzar y mantener los porcentajes y
  valores… establecidos en la disposición transitoria primera»** para la TV **en abierto
  de ámbito autonómico y local, tanto públicas como privadas**, y en radio **«fomentar y
  posibilitar gradualmente»** la accesibilidad en webs. Choca con la DT 1.ª.2, que desde
  2020 ya no fija valores para la local (lo señalo, no lo resuelvo). 31.1.c): accesibilidad
  de estudios y dependencias.
- Conexos: art. 41.3 y 43.5 (publicidad y discapacidad), 19.1.b) y DA 3.ª.d).

### 2.5. Servicio público

- **Art. 2.1.n) y 2.2** (arriba).
- **Art. 44** (2 redacciones; vigente DL 2/2020, art. 28.7). 44.1: **«un servicio esencial
  de titularidad pública para la sociedad, de interés económico general»**, producción,
  edición y difusión de un conjunto equilibrado de programaciones y canales **«generalistas
  y temáticos, en abierto»**, de radio, TV y nuevos soportes, **«con el fin de atender a las
  necesidades democráticas, sociales y culturales del conjunto de la población andaluza»**.
  Pueden prestarlo la Junta, las entidades locales, las universidades públicas y los centros
  docentes públicos no universitarios. **El DL 2/2020 suprimió «siempre bajo el régimen de
  gestión directa»** (44.1) y «directa» en el 44.2. 44.2: se rige por los principios del
  art. 2 y el gestor **«debe definir, planificar y controlar»** programas orientados a los
  fines del art. 45.
- **Art. 45** (1 redacción): **siete** fines específicos del servicio público local y
  autonómico (información veraz y plural; educación permanente; colectivos vulnerables y
  transversalidad de género; igualdad; divulgación; cultura andaluza; sociedad del
  conocimiento).
- **Art. 46 «Gestión del servicio público»** (**4 redacciones**). Vigente (DL 3/2024, art.
  59.21): 46.1 autonómico **«mediante gestión directa, de conformidad con lo establecido en
  el artículo 72 de la Ley 13/2022… y el artículo 210 del Estatuto»**; local **«mediante
  gestión directa»** conforme al **art. 75** Ley 13/2022. Cadena: 2018 gestión directa para
  ambos (art. 40.2 Ley 7/2010 y 85.2 LBRL) → DL 2/2020 el local **«podrá gestionarse por
  cualquiera de las formas»** del art. 85.2 LBRL → DL 26/2021 (46.4) suprime la
  autorización del órgano directivo para la colaboración de terceros → DL 3/2024 vuelve a
  la gestión directa del local. 46.3 **principio de equilibrio presupuestario**. 46.4 la
  colaboración de terceros **«no podrá conllevar merma de capacidad productiva…»** (la
  prohibición de 2018 para **«contenidos de difusión de información diaria»** cayó en
  2020). 46.5 servicio **local**: **quince años**, renovación **automática** si se cumple
  el **art. 29** Ley 13/2022.
- **Art. 47** control: comisión del **Parlamento de Andalucía** sobre la RTVA y filiales;
  y el servicio autonómico, en gestión y presupuesto, **«al control parlamentario y del
  Consejo Audiovisual de Andalucía, de conformidad con la legislación estatal básica.»**
- **Art. 48** financiación: **«no podrá sostener actividades ni contenidos ajenos al
  cumplimiento de la función de servicio público»** (remisión colgada al art. 21.3, §0).
- **Art. 50.1**: **«Corresponde a la Agencia Pública Empresarial de la Radio y Televisión
  de Andalucía (RTVA) la función y misión de servicio público de radio y televisión»**.
  **Art. 51** (2 redacciones; vigente DL 26/2021): sujeto a la legislación básica, a esta
  ley y a la **Ley 18/2007**; 51.3 (proyecto técnico de instalaciones) suprimido.
- Conexos RTVA: arts. 20.2 (archivos) y 22–26 (cine y audiovisual andaluz).

### 2.6. ¿Ha desplazado algo la Ley 13/2022?

**Ninguna norma que haya leído declara «desplazado» un precepto de la Ley 10/2018.** Lo
que consta es que el **DL 3/2024 (art. 59) reescribió** la ley sustituyendo las
remisiones a la Ley 7/2010 por la Ley 13/2022 y **suprimiendo** reglas propias (arts. 8,
9, 31.1.f, 32, 41.2.a…). Es modificación expresa por norma autonómica, no desplazamiento.

## 3. Consejo Audiovisual de Andalucía (Ley 1/2004, `BOE-A-2005-655`)

Lo que la Ley 10/2018 le atribuye sobre las rúbricas (todo leído el 24-09-2026):
- **Art. 12**: Consejo de Participación Audiovisual **«adscrito al Consejo Audiovisual de
  Andalucía»**. **Art. 13**: procedimiento del derecho a conocer la programación; la
  ciudadanía puede **dirigirse** a él por incumplimientos en contenidos y publicidad.
- **Art. 43.5**: **informe anual** sobre contenidos y publicidad relativos a personas con
  discapacidad (43.4: arbitraje y mediación por convenio). **Art. 47.1**: control del
  servicio público autonómico en gestión y presupuesto. Arts. 35.3 y 59: otros controles.
- **Art. 66.1.b)**: potestad inspectora; **66.3.c)** potestad sancionadora sobre la Ley
  13/2022: **art. 157, apartados 1, 2, 3, 9 y 11 a 16** (incluyen identificación de
  menores, 157.9, y violencia gratuita o pornografía, 157.11); **art. 158, apartados 7 a
  30** (calificación por edades, 158.7; accesibilidad, 158.11–14; publicidad y menores,
  158.17); **art. 159, apartados 1 y 3 a 8**; y los arts. 72.c), 73.a), b), d) y 74.a),
  d) de la propia ley. Ojo: **158.30 y 159.1 y 159.8 también figuran en el reparto del
  órgano directivo** (66.3.a); solapamiento del texto, no lo interpreto.
- **Art. 73.a)**: es infracción grave desatender sus instrucciones y decisiones.
- **Art. 78.3**: **«podrá, de forma motivada… requerir el cese de aquellos contenidos que
  contravengan la normativa vigente.»**
- **DT 1.ª.4**: aprueba los planes de participación de colectivos con diversidad funcional.
- **DF 1.ª**: dio nueva redacción al **art. 4 de la Ley 1/2004** (funciones, **28**
  números). Relevantes: 4.4–4.5 informes preceptivos **«a los efectos de garantizar el
  pluralismo»**; 4.7 **«Salvaguardar los derechos de los menores… facilitando la
  accesibilidad a las personas con discapacidad auditiva o visual…»**; 4.14 **«Garantizar
  el cumplimiento… de la función del servicio público»**; 4.19 calificación de programas;
  4.26 derecho de acceso **«respetando el pluralismo de la sociedad»**.

**Cadena del art. 4 Ley 1/2004 (4 redacciones):** original 2005 → Ley 10/2018 (DF 1.ª),
17-10-2018 → **DL 2/2020, art. 7** (27 números; suprime el informe sobre pliegos y
refunde los informes), 13-03-2020 → **STC 40/2025, de 11 de febrero** (`BOE-A-2025-5737`,
BOE 21-03-2025) **declara inconstitucional y nulo el art. 7 del DL 2/2020**. El
consolidado del BOE muestra hoy el art. 4 como **«(Anulado)»** y reproduce como
«Redacción anterior» el texto de la Ley 10/2018 (28 números). **No puedo confirmar con una
norma qué texto rige hoy**: el BOE no lo repone como texto vigente, y la sentencia no
dice nada de la reviviscencia en lo que he leído. Es decisión del redactor, con nota.

## 4. Lo que no he podido confirmar

1. La **convalidación** parlamentaria de los DL 26/2020, 4/2021, 26/2021 y 3/2024 (sólo la
   del 2/2020 consta en la STC 40/2025).
2. El resultado del **recurso de inconstitucionalidad 3473-2024** contra el DL 3/2024:
   admitido; sin sentencia en el BOE a 24-09-2026. No sé qué preceptos impugna en concreto;
   el art. 59 del DL es el que da la redacción vigente de los arts. 3, 7, 8, 9, 31, 32, 41 y 46.
3. **Qué texto del art. 4 de la Ley 1/2004 está vigente** tras la STC 40/2025 (§3).
4. El texto de los decretos-leyes y su exposición de motivos: están en BOJA, no en BOE; no
   los he leído. Todo lo que atribuyo a ellos sale de las notas del consolidado del BOE.
5. Si se aprobaron los reglamentos de desarrollo (art. 11.2, art. 12 y DF 6.ª): no buscado.
6. Cómo se resuelven la tensión 31.1.h)/DT 1.ª.2, la remisión del 48.2 al 21.3 y el
   solapamiento del 66.3: ninguna norma leída lo dice.
