# Grafista (15) · Investigación del bloque A-diseño (temas 1, 2, 3, 4, 16)

Fase 1. Fecha de trabajo: 29-09-2026 (el encargo fija como «hoy» el 24-09-2026; las fuentes locales
y web se leyeron el 29-09-2026). Sólo lo que falta a lo reutilizable (RTVE y común cerrado).
Negrita = literal de la fuente.

## Fuentes propias de la casa leídas (locales)

- LE = Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía, 1.ª ed., marzo 2004, © RTVA
  (`fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`). Leído 29-09-2026.
- CSP = Carta del servicio público de la RTVA 2024-2029, BOJA núm. 247, 2023
  (`carta-servicio-publico-2024-2029-boja-247-2023.txt`). Leído 29-09-2026.
- CP = Contrato-programa 2024-2026, Acuerdo de 19-XII-2023 del Consejo de Gobierno, BOJA núm. 245,
  de 26-XII-2023 (`contrato-programa-2024-2026-boja-245-2023.txt`). Leído 29-09-2026. Vigencia hasta
  2026: sigue vigente el 24-09-2026 salvo que conste prórroga o sustituto (no comprobado).

## Tema 4 · Infografía y visualización de datos: claridad, rigor, ética, fuentes y representación accesible

Lo que ya cubren los reutilizables: tipos de infografía, cuadro de elección de gráfico y tres reglas
de honradez (RTVE 08 §2); gráficos por tipo de variable, distorsiones (eje, escalas, pictograma de dos
dimensiones), LE 3.16 (cuatro o cinco elementos, ocho segundos, dinamismo, orden alfabético, no se
firma) y redondeo (Redactor/a T15 §5-6, cerrado). **Falta**: fuentes (cómo se atribuye), representación
accesible (norma técnica) y matices de rigor. Material nuevo:

### Fuente 1 · WCAG 2.2 (W3C)

W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*, **W3C Recommendation 12 December 2024**,
https://www.w3.org/TR/WCAG22/ (leída 29-09-2026). Es la versión que tomo como vigente en la web del W3C
ese día. Criterios aplicables a un gráfico o infografía publicados en web (texto literal en inglés;
la traducción es mía y va en redonda):

- **1.1.1 Non-text Content (Level A)**: «**All non-text content that is presented to the user has a text
  alternative that serves the equivalent purpose, except for the situations listed below.**» → todo
  gráfico necesita una alternativa textual equivalente.
- **1.4.1 Use of Color (Level A)**: «**Color is not used as the only visual means of conveying
  information, indicating an action, prompting a response, or distinguishing a visual element.**»
- **1.4.3 Contrast (Minimum) (Level AA)**: «**The visual presentation of text and images of text has a
  contrast ratio of at least 4.5:1**», salvo: «**Large-scale text and images of large-scale text have a
  contrast ratio of at least 3:1**»; sin requisito el texto incidental y «**Text that is part of a logo
  or brand name has no contrast requirement.**» (esto último, útil para el tema 2: el logotipo está
  exento).
- **1.4.11 Non-text Contrast (Level AA)**: «**The visual presentation of the following have a contrast
  ratio of at least 3:1 against adjacent color(s)**»: componentes de interfaz y «**Graphical Objects:
  Parts of graphics required to understand the content, except when a particular presentation of
  graphics is essential to the information being conveyed.**»
- Definición de *contrast ratio*: «**(L1 + 0.05) / (L2 + 0.05)**», L1 luminancia relativa del más
  claro, L2 la del más oscuro; «**Contrast ratios can range from 1 to 21 (commonly written 1:1 to
  21:1).**»
- Definición de *large scale (text)*: «**with at least 18 point or 14 point bold**» (puntos, no
  píxeles).
- Ojo: WCAG es para contenido web. **No hay en WCAG un umbral para rótulos de emisión de TV**; aplicar
  4,5:1 al faldón es analogía de oficio, no norma. El enlace con la ley española (RD 1112/2018 y
  UNE-EN 301549) lo investiga el bloque D (tema 10); aquí no se ha leído.

### Fuente 2 · Guía del Analysis Function del Gobierno británico: gráficos

Government Analysis Function (Reino Unido), *Data visualisation: charts*, guía, **Publication
date: 19 May 2022**, **Owner: Analysis Function Central Team**, **Who this is for: People in government
who design and publish charts**,
https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/ (leída
29-09-2026). Es guía de un organismo público estadístico, no norma española: citarla como «guía
publicada». Datos útiles, literales:

Elegir el gráfico:
- «**If you cannot write down the message your chart is giving in a few sentences, you should think
  again about the chart you have chosen.**»
- Tabla relación estadística → gráfico (literal): **Distribution — Bar chart, population pyramid, box
  plot, dot plot**; **Time series — Line chart, calendar heat map**; **Ranking — Bar chart, lollipop
  chart, slope chart**; **Deviation — Bar chart, dot plot**; **Correlation — Scatterplot, line graph**;
  **Magnitude — Bar chart**; **Spatial — Map**; **Part-to-whole — Bar chart, pie chart, donut chart,
  tree map, bubble chart**; **Flow — Sankey graph**. Remite a **the Visual Vocabulary tool from the
  Financial Times**.

Rigor (honradez) — matiza la regla 1 de RTVE 08, que dice sin excepción «el eje de las cantidades
empieza en cero»:
- Barras: «**breaking the numerical axis on a bar chart is problematic and highly controversial. In bar
  charts you perceive the bars being proportional to each other – breaking the numerical axis distorts
  these relative proportions.**» Alternativa: «**consider an alternative chart, such as a Cleveland dot
  plot.**» Ejemplo: la Office for Statistics Regulation escribió a HM Treasury (27-02-2023) por un
  gráfico de barras de inflación con el eje desde el 8 % que exageraba la bajada de 11,1 % a 10,1 %.
- Líneas: «**it is acceptable to break a numerical y-axis on a line chart, when necessary. Line charts
  are not read in the same way as bar charts so breaking the numerical axis does not mislead in the
  same way.**» Si se corta: símbolo de corte visible, corte en número redondo («**break to focus on 50% to
  90% rather than 54.3% to 93.5%**») y mencionarlo en la descripción. → Coincide con lo que ya dice
  Redactor/a T15 («en un gráfico de líneas… puede estar justificado, pero hay que indicarlo»). **El
  redactor debe matizar la regla absoluta de RTVE 08.**
- Doble eje: «**In general, we do not recommend using dual axis charts because: they can be easily
  misinterpreted; the way we display lines in relation to each other can manipulate the data story**»;
  mejor dos gráficos separados.
- Series con huecos: «**If you do use a line, do not join the points either side of the missing data
  point, even if the line is dotted or dashed. Joining points implies we know something about the
  data.**»
- Proporción del gráfico: «**In line charts, the aspect ratio you choose alters the slope of the lines.
  This can be misleading.**»
- Pequeños múltiplos: «**it is essential for all the y-axes to have the same scale to avoid
  misunderstandings.**» (respalda la regla 3 de RTVE 08).
- Líneas: «**Aim for a maximum for four lines**» (rótulo literal del epígrafe).
- Tarta, sólo si: «**there are five categories or fewer**»; «**the categories sum to a meaningful whole
  (you can combine categories when appropriate, but never remove a category from the 'whole')**»;
  «**there is a dominant category (if several categories are a similar size, use a bar chart
  instead)**». Orden: «**Rank the categories in a pie chart by size and start the first sector at the
  12 o'clock position.**» Etiquetas: «**Do not use a key, label the categories themselves.**»
- Barras: «**The gap between bars should be narrower than the width of a single bar.**»
- Simplicidad, evitar: «**shaded backgrounds; unnecessary borders; boxes around legends and other
  content; patterns, textures and shadows; 3D shapes; unnecessary data markers on line charts; thick or
  dark gridlines**».

Fuentes (lo que el enunciado pide y el reutilizable no da):
- «**You should give the specific data source for each chart and link directly to it if you can. Avoid
  stating things like 'Office for National Statistics' and then linking to the website homepage.**»
- Formato: «**[publication, survey or other source of data] from the [organisation]**». Ejemplo: «**Source:
  Childcare and early years survey of parents from the Department for Education.**»
- Datos descargables: «**It is best practice to provide the data displayed in each chart as an
  accessible data download.**»
- Títulos: dos, «**a headline title and a formal statistical subtitle**»; el subtítulo dice «**what the
  data is, the geography the data relates to and the time period shown**».
- Notas al pie: «**footnotes do play an important role in making sure data is not misused.**»

Representación accesible:
- «**all content published on public sector websites must meet the level A and AA success criteria in the
  Web Content Accessibility Guidelines 2.2. This includes charts.**» (es la ley británica; en España,
  bloque D).
- Alternativa textual: puede ser «**a table of the data presented in the chart**» o «**a text description
  of the message the chart is presenting**»; «**If you expect a non-disabled user to read the data from the
  chart, give a table. If you expect them to take away an overall understanding of the data, give a text
  description … If you expect them to do both, give both.**» La descripción «**should not repeat the chart
  title, be a literal description or outline every data point shown.**»
- Formato: «**It is best practice to use the Scalable Vector Graphic (SVG) format when publishing images of
  charts.**» «**Changing a PNG or JPEG file into an SVG does not make it scalable, it must be done from the
  source file.**»
- Pie charts: «**pie charts are not the best in terms of accessibility as they are hard to understand when
  magnified.**»

### Fuente 3 · Guía del Analysis Function: colores

Government Analysis Function, *Data visualisation: colours*, **Publication date: 23 November 2021**,
**Updates: 12 February 2026 - sequential colour palette guidance updated**,
https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/ (leída
29-09-2026). Literales:
- 1.4.11 aplicado: «**This means that all adjacent colours need at least a 3 to 1 contrast ratio.**»
- 1.4.1 aplicado: «**we should avoid using legends in line charts and pie charts. Instead, label the lines
  and sectors on the chart.**»
- 1.3.3 (Sensory characteristics): no decir «**'the green line' or 'the blue bar'**» en el texto.
- Texto en imagen de gráfico: aconsejan «**sticking to a 4.5 to 1 colour contrast ratio for text whenever
  possible**» porque al publicar como imagen el texto se reescala.
- Pocos colores: «**You should only use different colours when they show helpful differences in the
  data.**» «**When you have categorical data that cannot be grouped, use a single colour.**»
- Coherencia: «**If you have a series of charts, assign the same colour to the same variable in each
  chart.**»
- Asociaciones: «**people tend to link blue with water and green with grass**»; «**Colours can also have
  cultural associations.**»
- Fondo: «**Never use an image as a background.**»
- Daltonismo: «**Colour blindness affects around 8% of men and 0.5% women.**» (cifra de la guía; no la he
  contrastado con fuente médica: si se usa, atribuirla).
- Escala de grises: «**It is a good idea to check your charts can be understood in greyscale.**»
- Baja visión: el 3:1 entre colores adyacentes «**is important for people with low vision.**»

### Casa (Canal Sur) para el tema 4
- LE 3.16 ya está copiado en Redactor/a T15. Nada más en LE sobre infografía salvo LE 6.5.2 «Eficacia y espectáculo» (p. 95,
  realización de informativos): «**infografías, 'vidi wall', pantallas de plasma... cuyo uso precisa cierto sentido
  estético y de una capacidad notable para aprovechar y armonizar los recursos disponibles.**»
- CP compromiso 48: la web de RTVA/Canal Sur con «**contenidos informativos, textuales, fotográficos,
  infográficos y elementos audiovisuales**» (cláusula tercera, A). Sirve para decir que la infografía web
  es compromiso del Contrato-programa.

### No confirmado (tema 4)
- Guía española oficial equivalente (INE, datos.gob.es): no la he localizado ni leído; no citar.
- Umbral de contraste para rótulos de TV: no hay norma leída (ver arriba).
- «Ética» de la infografía como código deontológico propio: no hay documento de la casa más allá de LE.

## Tema 1 · Diseño gráfico aplicado a televisión, radio visual, web, redes y plataformas digitales

Reutilizable: RTVE 06 (sintaxis de la imagen), 08 (interfaz, UX, retícula adaptable), 02 (resolución,
aspecto, HDR). **Faltan radio visual, web (en concreto) y redes/plataformas, y el marco de la casa.**
Para redes y miniaturas hay temas cerrados de Canal Sur que el encargo no lista para el tema 1 pero
que tratan lo mismo: Montador/a T12 (`30-operador-a-montador-a-de-video/12-edicion-para-redes-y-plataformas.md`,
formatos 9:16, 1:1, 4:5, miniaturas de YouTube leídas el 25-09-2026) y Realizador/a T15
(`33-realizador-a/15-transmedia-plataformas-redes-directos-ip.md`). Son materia del tema 13 de
Grafista (bloque C); en el tema 1 basta remitir o copiar un párrafo.

### Radio visual

Fuente: Sánchez Cid, M.; Cuevas-Molano, E.; López Carral, A.; Marroquín-Ciendúa, F., «Radiovisión» /
«Radiovision: consumption and evaluations of a sample of university communication students», *VISUAL
REVIEW. International Visual Culture Review / Revista Internacional de Cultura Visual*, vol. 17, núm. 1,
2025, pp. 179-192, DOI 10.62161/revvisual.v17.5410 (metadatos Crossref; PDF inglés en
https://visualreview.net/revVISUAL/article/download/5410/4054, leído 29-09-2026). Autores de la
Universidad Rey Juan Carlos, Universidad Europea de Madrid y Univ. Jorge Tadeo Lozano (Bogotá).
Literales (inglés; traducción mía en redonda):
- Denominaciones: «**The most common include "radiovision" (Palazio, 1999; Cavia, 2016), "visual radio"
  (Pedrero-Esteban, 2022), "radio with image" (Zambelli, 2023), the term "radio cam," or "radio that can
  be seen," which is used by Radio Nacional de España, and "televised radio" (García Lastra, in
  Ballesteros, 2014).**» La última «**appears to be more widely rejected due to its direct association
  with television.**»
- Definición citada: «**Ala-Fossi et al. (2008) define visual radio as a medium in which broadcasters speak
  in front of professional cameras and music is played, as well as artists' videos being watched. They
  posit that visual radio is more than a webcam showing the radio studio's signal.**»
- Las cuatro posibilidades de la señal de vídeo (útil para el grafista): «**displaying events occurring in
  the studio; visualising a mask or fixed image; incorporating a video signal from outside the studio; or
  utilising closed videos that are not related to the activity taking place in the studio.**»
- Debate de identidad: «**It is unclear whether radio with video can still be defined as radio, whether it
  constitutes a form of television, or whether it is a hybrid**» (Cavia Fraile, 2016).
- Contexto de consumo (AIMC, *Marco General de los Medios 2024*, p. 31, citado por el artículo, no leído
  por mí): FM sola **44.9%**, radio por Internet **11.3%**, TDT **1.4%**. Si se usa, atribuirlo «según
  AIMC citado por…».
- Conclusión: la muestra señala «**YouTube as the preferred platform for listening to and downloading radio
  content**» y la radio con vídeo se consume sobre todo allí (inferencia de los autores).
- Lo que el grafista hace en radio visual (cortinillas, rótulos, mosca, «máscara o imagen fija» cuando no
  hay cámara): el artículo sólo da la «máscara o imagen fija». Lo demás sería oficio; declararlo así.

Casa: CSP art. 6.8 compromete «**agregadores digitales de programaciones de canales de radio,
prestaciones de radio y de televisión digital híbrida**»; CP compromiso 46 encarga a la dirección
«**'Canal Sur Media'**» los servicios digitales, entre ellos «**plataformas de streaming OTT; de podcasting;
portales en Internet; canales audiovisuales web; presencia y contribución en redes sociales; desarrollo de
aplicaciones para dispositivos móviles; agregadores de servicios digitales de radio; prestaciones de radio
digital híbrida, de televisión digital híbrida, prestaciones de 'televisión conectada' y servicios bajo
estándar europeo HbbTV; prestaciones de inteligencia artificial, de realidad virtual, extendida y
aumentada, y de metaverso**». **Ningún documento de la casa leído usa «radio visual»** ni dice que
Canal Sur Radio emita con cámaras. Una búsqueda web sólo dio listas de YouTube no oficiales: **no
confirmado**; no afirmarlo en el tema.

### Web: diseño adaptable (responsivo)

Fuente: MDN Web Docs (Mozilla), «Diseño receptivo» (versión española),
https://developer.mozilla.org/es/docs/Learn_web_development/Core/CSS_layout/Responsive_Design, **This
page was last modified on 12 sept 2026 by MDN contributors** (leída 29-09-2026). Documentación técnica de
referencia, no norma. Literales:
- «**el concepto de diseño web responsivo (RWD, responsive web design), un conjunto de prácticas que permite
  a las páginas web alterar su diseño y apariencia para adaptarse a diferentes anchos de pantalla,
  resoluciones, etc.**»
- «**El término diseño responsivo fue acuñado por Ethan Marcotte en 2010, y describía el uso combinado de tres
  técnicas.**»: redes (retículas) fluidas, imágenes fluidas (**«establecer la propiedad de max-width al
  100%»**) y consultas a los media.
- «**el diseño web responsivo no es una tecnología independiente: es un término utilizado para describir un
  enfoque para el diseño web**».
- Antes: versión móvil aparte, «**con una URL diferente (a menudo algo así como m.example.com o
  example.mobi)**», con dos sitios que mantener.
- Imágenes: el elemento `<picture>` y los atributos `srcset` y `sizes` dejan al navegador elegir la imagen;
  «**imágenes de director artístico, que proporcionan un recorte o una imagen completamente diferente para
  diferentes tamaños de pantalla**» (el grafista entrega varios recortes).
- Accesibilidad en web: ver tema 4 (WCAG 2.2, 1.4.3 y 1.4.11) y bloque D.

### Plataformas de la casa (marco para el grafista)
- CP compromiso 45: plataforma OTT propia «**'Canal Sur Más'**», accesible en «**televisores smartTV,
  terminales móviles, tabletas, ordenadores personales, videoconsolas**» y la «**propia plataforma digital de
  servicios Podcast**».
- CP compromiso 47: la actividad digital como «**una línea de actividad en pie de importancia e igualdad con
  las actividades de radio y de televisión**»; producción «**con criterios convergentes y de interoperablidad
  de sistemas y recursos de los medios de radio y de televisión para la consecución de contenidos multimedia
  susceptibles de difusión y de distribución a través de todo tipo de soporte**» (sic: «interoperablidad»).
- CP compromiso 48 (web con «**infográficos**», «**páginas web para eventos extraordinarios de interés
  social**», «**nuevos entornos web específicos para programas informativos**», posición proactiva en redes).
- CSP art. 7.2: potenciar «**la presencia y actividad de Canal Sur en redes sociales y aplicaciones digitales
  basadas en la aportación, compartición e intercambio de contenidos audiovisuales de usuario en plataformas
  de intercambio de vídeo, conforme a las posibilidades que determina la Ley 13/2022.**»

### No confirmado (tema 1)
- Que Canal Sur Radio haga radio visual y con qué grafismo.
- Guía de estilo gráfico web de Canal Sur: no publicada (ver tema 2).
- Normas técnicas de grafismo en redes: no existen como norma; lo de YouTube está en Montador/a T12.

## Tema 2 · Identidad visual corporativa: manual de marca, coherencia gráfica, legibilidad, color, tipografía y adaptación a formatos

Reutilizable: RTVE 12 (signos de identidad, manual de identidad; §4 «imagen corporativa de la casa» es
RTVE y **hay que quitarla**), 05 (tipografía, leyes de percepción), 01 (color). Faltan: el manual de la
casa, legibilidad con criterio medible y adaptación a formatos.

### Manual de marca de Canal Sur/RTVA: **no publicado**
- Búsquedas web (29-09-2026: «Canal Sur RTVA manual de identidad corporativa logotipo pdf», «Canal Sur nueva
  imagen corporativa logotipo rediseño»): **no hay manual de identidad de RTVA/Canal Sur accesible
  públicamente.** Aparecen un portfolio de agencia (ea-branding.com, «Canal Sur Televisión») que dice haber
  hecho un manual para la cadena, un rediseño de estudiante en Behance y prensa de diseño (Brandemia, que no
  cargó). **Nada de eso es documento de la casa: no usarlo.** Declarar en «Lo que este tema no da».
- Lo único de la casa publicado sobre su imagen: blog oficial «Memoranda | Archivo CanalSur» (Documentación y
  Archivo de Canal Sur), entrada «Canal Sur TV: nueva programación e imagen corporativa (1995)»,
  http://blogs.canalsur.es/documentacionyarchivo/cstv-nueva-programacion-con-triangulo-del-sur/ (leída
  29-09-2026, HTML descargado y leído completo): «**También CSTV estrena nueva imagen corporativa con colores
  en la gama de los amarillos símbolos de la luz de Andalucía, y logotipo, un triángulo invertido, que
  representa el concepto del Sur.**» Fechas literales: «**1995: 9 de marzo. Joaquín Marín, director general
  de la RTVA, presenta la nueva programación de CSTV y la nueva imagen corporativa de la cadena de televisión
  andaluza.**» y «**1995: 13 de marzo. Comienza la nueva programación de Canal Sur Televisión**». Fuente
  primaria que cita el blog: «**[Informativo «Diario 2», 9/3/1995, Canal Sur Televisión]**». Es historia, no
  identidad vigente.
- Identidad vigente (logotipo actual, sol con ocho rayos-provincias, trapecio, verde): sólo en prensa no
  oficial y resúmenes de buscador (tutele.net 28-02-2011, no cargó; noticia de canalsur.es sobre el «4D», URL
  devuelve 404). **No confirmado: no usar.**
- LE 2.3.2.4 (Credenciales): «**No se podrá usar el nombre de la empresa en objetos privados (tarjetas de
  visita, membretes, logotipos...) o para actividades particulares.**» Único precepto de la casa sobre uso
  del logotipo.
- CSP art. 34.1: «**nuevas acciones de prestigio basadas en la solidez de la marca Canal Sur**» dentro de la
  responsabilidad social corporativa. CP compromiso 105: TDT «**de las marcas televisivas Canal Sur Televisión y Canal Sur
  2**», distribución internacional por satélite «**bajo la marca Canal Sur Andalucía**» y FM «**de las
  diversas marcas de servicios sonoros de radio de Canal Sur**» (útil: la casa habla de «marcas» por canal);
  compromiso 112: «**La señal internacional de la marca Canal Sur Andalucía procurará alcanzar
  la máxima**…» (numeración comprobada en el texto del BOJA).
- Coherencia gráfica exigida por la casa: ya está en Realizador/a T12, epígrafe «Coherencia visual: lo que
  exige la casa» (cerrado): copiar de ahí, no reinvestigar.

### Legibilidad y color medibles
- WCAG 2.2, 1.4.3 (4,5:1; 3:1 texto grande = 18 pt o 14 pt negrita) y 1.4.11 (3:1 objetos gráficos), y
  **exención de logotipos** («**Text that is part of a logo or brand name has no contrast requirement.**»):
  ver tema 4. Sirve para la legibilidad en web y redes. Para emisión, oficio.
- Colorimetría de emisión (BT.709/BT.2020) y zonas seguras: bloque B (temas 8) y Realizador/a T12 ya dan
  zonas seguras; no repetir.

### Adaptación a formatos
- Imágenes de «director artístico» (MDN, tema 1) y relaciones de aspecto de redes (Montador/a T12) son lo
  único con fuente. Sistema de diseño y retícula adaptable ya en RTVE 08 §3.
- Versiones del logotipo (horizontal, vertical, monocromo, área de respeto, tamaño mínimo): RTVE 12 §5 lo
  trata en abstracto; no hay versión de la casa publicada.

### No confirmado (tema 2)
- Manual de identidad de RTVA/Canal Sur, tipografía corporativa, colores corporativos (códigos): **no
  publicados.**
- Autoría y fecha del logotipo vigente.

## Tema 3 · Grafismo para informativos, programas, deportes, promociones, continuidad y eventos especiales

Reutilizable: RTVE 08 §1 (informativos frente a programas), RTVE 09 (continuidad), RTVE realización 15
(pantallas, grafismo en directo, continuidad); cerrado: Realizador/a T12 (rotulación, zonas seguras,
elementos de continuidad, coherencia visual de la casa, grafismo de un informativo). **Faltan deportes,
promociones y eventos especiales.** Promociones: el tema cerrado es Montador/a T6 §2 (LGCA art. 127
autopromoción, 136, técnica de *spot*/tráiler/*teaser*, LE 9.10.1): copiarlo. Deportes (ley y LE): Montador/a
T6 §4 ya da LGCA arts. 137.2.i (sobreimpresiones «**que formen parte indivisible de la retransmisión de
acontecimientos deportivos**» no computan) y 139, y LE 8.4. Lo nuevo:

### Deportes: fuente académica
Torres-Martín, J. L.; Castro-Martínez, A.; Díaz-Morilla, P. (Universidad de Málaga), «La representación de
datos como elemento informativo y de construcción de marca en las competiciones deportivas: las innovaciones
tecnológicas en los grafismos de LaLiga Santander», *Fonseca, Journal of Communication*, núm. 25, 2022,
pp. 95-113, https://doi.org/10.14201/fjc.29755 (PDF de revistas.usal.es, leído 29-09-2026). Literales:
- Resumen: «**Los grafismos tienen una importancia capital en las retransmisiones deportivas actuales, ya que
  contribuyen a la comprensión del evento, definen la identidad visual de las competiciones y ayudan a la
  espectacularización de estos acontecimientos.**» → tres funciones: comprensión, identidad, espectáculo.
- «**la representación gráfica de datos no solo posee una función informativa, sino que también incide en la
  identidad visual de la propia competición y en el aumento del atractivo de sus productos audiovisuales.**»
- Cuatro «niveles de significado» de la realización deportiva (Raunsbjerg y Sand, 1998, citados): la imagen,
  los comentarios, el sonido ambiente y «**los grafismos -que aportan la información complementaria que no
  pueden suministrar las imágenes y los sonidos-**».
- Producción: «**los grafismos se crean actualmente a partir de una base de datos introducida con anterioridad
  al inicio de la realización, para que durante la misma se puedan recrear gráficamente en pantalla gracias a
  equipos informáticos.**»
- Arbitraje: Epsio, que «**permite trazar una línea durante la retransmisión para marcar el fuera de juego**»
  (Roger, 2015, p. 139, citado), hoy recurso del videoarbitraje.
- Función pedagógica (Marín, 2011, p. 20, citado): los grafismos tienen «**una vertiente pedagógica,
  «especialmente cuando se aplican técnicas de Realidad Virtual»**»; la infografía se ha convertido en muchos
  deportes en «**un elemento decisivo para aclarar acciones controvertidas no captadas por la imagen real**».
- Espectacularidad (Blanco, 2001, citado): «**La aparición del resultado, del tiempo de partido, del de
  posesión, el nombre o estadística individual y la estadística global favorecen esta espectacularización**»
  (baloncesto).
- Datos en deporte (Perin et al., 2018, citado): usos «**el analítico o exploratorio y el narrativo o
  comunicativo**»; tres categorías: «**«box-score data, tracking data, and meta-data»**», es decir «**datos
  estadísticos, datos del seguimiento de la acción y metadatos**».
- Ciclismo y GPS (Benítez, López y Sánchez, 2014, p. 17, citado): el realizador «**es un demiurgo que conoce
  toda la información relevante de la carrera y puede dosificarla**».
- Flujo LaLiga (gráfico 1, elaboración de los autores): Mediacoach «**Lidera la estrategia: selecciona datos y
  necesidades narrativas**» → Audiovisual «**Coordina, supervisa y analiza las retransmisiones**» → Grafismo
  «**Valora la viabilidad de la representación de datos y su ejecución**» → Realización «**Confecciona discurso
  gráfico-narrativo durante la retransmisión**». Grafismo valora «**si operativamente es posible, sobre todo
  ahora que los tiempos para confeccionar y mostrar un dato estadístico grafiado son muy cortos al hacerlo sobre
  la misma señal en directo**» (entrevista, 21-05-2022).
- Técnicas citadas: «**Live 3D Graphics, las repeticiones volumétricas en 360º y el modelo avanzado de
  probabilidad de gol**»; «videomarcadores».
- Informativos, útil también para T3 (Andueza y Pérez, 2016, p. 127, citados): «**cada cadena de televisión
  cuenta con una línea gráfica propia: colores, efectos, tipografía y composición se basan en esos estándares
  del medio**»; rasgos comunes de los rótulos de sumario: «**la composición siempre abajo, sobre pastilla de color
  diferente a las letras, letras sin serifa en blanco o negro, tamaño sobre los 20 puntos y efectos de entrada
  y/o salida sencillos**», para «**facilitar la lectura de los rótulos, porque en la segunda década del siglo XXI
  la televisión también se lee**». Taxonomía de Valero (2004, citado) del grafismo informativo: «**fotografías
  estáticas, dibujos e iconos, grafismo de posición, Realidad Virtual, tablas alfanuméricas, fichas con dibujos,
  textos, grafismos ubicativos y gráficos.**»
- Aviso: es un caso (LaLiga produce la señal internacional); el grafismo de un partido que emite Canal Sur lo
  pone en gran parte el productor de la señal. No he confirmado qué grafismo propio añade Canal Sur en sus
  retransmisiones.

### Eventos especiales: casa y ley
- CSP art. 13.6: los informativos atenderán «**a todos los grandes acontecimientos de la vida democrática,
  social, cultural, etnográfica, institucional, política, asociativa, empresarial, sindical y económica de
  Andalucía en toda su diversidad territorial.**» Art. 13.7: «**se producirán coberturas informativas
  especiales sobre las sesiones más significativas de la actividad del Parlamento de Andalucía**».
- CP 48: «**la creación de páginas web para eventos extraordinarios de interés social**».
- LE 8.4 (retransmisiones «**generalmente deportivas, taurinas o de fiestas populares**») y la moderación en
  «**fiestas populares (Semana Santa, Rocío, Santa María de la Cabeza, Ferias...)**» (8.4.2): ya en Montador/a T6
  §4 en parte; afecta a la palabra, no al grafismo. Útil sólo como marco.
- Noche electoral: LE 7.1.3 (pp. 97-98): la encuesta no abre un informativo, «**la única excepción es el uso de
  sondeos propios o ajenos al cierre de las urnas en una jornada electoral**». LOREG art. 69 (ficha técnica que
  debe acompañar a toda publicación de un sondeo, 69.1; prohibición de los cinco días, 69.7) ya está en
  Redactor/a T12 (cerrado, `34-redactor-a/12-informacion-politica-institucional-electoral.md`): copiar de ahí
  la parte que afecta a un gráfico de sondeo (la ficha técnica en pantalla). Texto del BOE leído en
  `fuentes/canal-sur/BOE-A-1985-11672.md` (art. 69.1 a y b, 69.7) el 29-09-2026: coincide.

### No confirmado (tema 3)
- Grafismo deportivo propio de Canal Sur (marcadores, estadísticas): sin documento.
- Manuales de grafismo electoral de la casa: no publicados.
- La tesis de Roger Monzó (UPV, DOI 10.4995/thesis/10251/8440) no se pudo leer (protección antibots del
  repositorio).

## Tema 16 · Promoción y creatividad visual al servicio de la programación pública

Reutilizable: RTVE 09 §3 (piezas de continuidad y autopromoción); cerrado: Montador/a T6 §2 (autopromoción
en LGCA art. 127, identificación, técnica de *spot*, tráiler, *teaser*, *sneak peek*; promoción e información
en LE). **Falta «creatividad visual al servicio de la programación pública»**: sólo hay fuente de la casa:

- CSP art. 10.1 (Sello distintivo de calidad audiovisual): calidad «**tanto técnica en los componentes,
  utilización y producción de elementos audiovisuales de la comunicación, como la relativa al desempeño y
  capacitación profesional y funcional del capital humano en todas sus vertientes, ya sea artística, creativa,
  escénica, narrativa, argumental, textual, infográfica o de tratamiento periodístico**». Art. 10.2: «**con la
  finalidad de establecer un reconocible y singular sello de calidad que identifique las producciones de los
  medios de Canal Sur por sus elevados estándares de excelencia técnica y profesional.**» (Sirve también para el
  tema 2: la marca como sello de calidad.)
- CSP art. 19.1 (Entretenimiento de calidad): «**estimulando la creatividad de los contenidos, la innovación de
  los formatos, la atracción en sus presentaciones**»; 19.2: «**se potenciará una originalidad e innovación
  siempre respetuosa con los valores y principios sociales y derechos estatutarios y constitucionales, y se
  apoyará a los nuevos talentos y emergentes creativos artísticos andaluces.**»
- CP compromiso 53 (entretenimiento), casi igual: «**estimulando la creatividad de los contenidos, la innovación
  en los formatos, la atracción en sus presentaciones, y potenciando la originalidad e innovación siempre
  respetuosa con los valores sociales**».
- CSP art. 12 (Alfabetización mediática): «**campañas de diversos aspectos y temáticas relativas a la
  alfabetización mediática e informacional**» (12.1); campañas específicas para menores y jóvenes (12.2) y para
  mayores y zonas rurales (12.3). Son piezas que diseña o anima el grafista.
- CP compromiso 59: «**Todos los medios de Canal Sur incluirán campañas institucionales y propias en defensa de
  la igual de la mujer, y campañas contra la violencia de género**» (sic, «igual»), con remisión a la Ley
  18/2007, art. 4.3.l).
- CSP art. 34.1: «**acciones de prestigio basadas en la solidez de la marca Canal Sur**» (RSC).
- Ley 18/2007 art. 4.3.l citado por el CP: no lo he releído en el BOE/BOJA; si el redactor lo cita, leerlo
  (está en el común, tema 5).

### No confirmado (tema 16)
- Criterios internos de autopromoción o manual de promociones de Canal Sur: no publicados.
- Fuente académica sobre creatividad en promociones de televisión pública: no localizada en esta fase;
  declararlo como oficio.

## Trazabilidad (fuentes nuevas de esta fase, todas leídas el 29-09-2026)

| Fuente | Dónde | Temas |
|---|---|---|
| W3C, WCAG 2.2, Recommendation 12-12-2024 | https://www.w3.org/TR/WCAG22/ | 4, 2, 1 |
| Government Analysis Function, *Data visualisation: charts* (19-05-2022) | analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/ | 4 |
| Government Analysis Function, *Data visualisation: colours* (23-11-2021, act. 12-02-2026) | analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/ | 4, 2 |
| Sánchez Cid et al., «Radiovisión», *VISUAL REVIEW* 17(1), 2025, 179-192 | DOI 10.62161/revvisual.v17.5410 | 1 |
| MDN, «Diseño receptivo» (mod. 12-09-2026) | developer.mozilla.org/es/docs/Learn_web_development/Core/CSS_layout/Responsive_Design | 1, 2 |
| Torres-Martín et al., *Fonseca, Journal of Communication* 25, 2022, 95-113 | DOI 10.14201/fjc.29755 | 3 |
| Blog «Memoranda», Documentación y Archivo de Canal Sur, entrada 1995 | blogs.canalsur.es/documentacionyarchivo/cstv-nueva-programacion-con-triangulo-del-sur/ | 2 |
| Libro de estilo de Canal Sur TV y Canal 2 Andalucía (2004): 2.3.2.4, 3.16, 6.5.2, 7.1.3, 8.4, 9.10.1 | fuentes locales | 1-4, 16 |
| Carta de servicio público 2024-2029 (BOJA 247/2023): arts. 6.8, 7.2-3, 10, 12, 13.6-7, 19, 34.1 | fuentes locales | 1, 2, 3, 16 |
| Contrato-programa 2024-2026 (BOJA 245/2023): cláusula tercera A, compromisos 45-48, 53, 59, 105, 112 | fuentes locales | 1, 2, 3, 16 |
| LOREG art. 69 (BOE-A-1985-11672) | fuentes locales | 3 |

Ficheros tocados: sólo este informe. Descargas de trabajo en el scratchpad de la sesión (`g15a/`).
