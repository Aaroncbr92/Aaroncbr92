# Grafista (15) · Tema 1 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/01-diseno-grafico-television-radio-visual-web-redes-plataformas.md`
(781 líneas). Fecha de trabajo del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema).
No corrijo: sólo señalo. Ficheros tocados: este informe y `15-T01-preguntas.md`.

Alcance de la exactitud: se saltan lo «Copiado del común» (Montador/a T12: cuatro epígrafes; Realizador/a
T12: primer párrafo de «Qué es el grafismo» y los dos de HDR) y lo «Copiado de RTVE sin cambios» (tablas y
frases listadas en `15-T01-redaccion.md`). La cobertura mira el tema entero.

## Fuentes releídas (29-09-2026)

| Fuente | Qué se cotejó | Resultado |
|---|---|---|
| Carta del Servicio Público 2024-2029, BOJA 247, 28-XII-2023 (volcado `.txt`) | art. 6.8 (dentro de «Artículo 6. Servicio público centrado en la sociedad»); 7.1 (páginas web con contenidos infográficos, dentro de «Artículo 7. Expansión digital»); 7.6 (HD exclusiva desde 14-II-2024; UHD 4K) | Literales y numeración correctos |
| Contrato-programa 2024-2026, Acuerdo de 19-XII-2023, BOJA 245, 26-XII-2023 (volcado `.txt`) | cláusula TERCERA, epígrafe 3.5; puntos 46 (Canal Sur Media, agregadores, HbbTV, radio online temáticos), 47 (con la errata «interoperablidad»), 48 | Literales correctos |
| W3C, WCAG 2.2, Recommendation 12 December 2024 (copia local) | 1.1.1, 1.4.1, 1.4.3 (Large Text, Incidental, Logotypes), 1.4.11; *contrast ratio*; *large scale*; *relative luminance* (0-1) | Literales y niveles correctos; ver M4 |
| MDN, «Diseño receptivo» (copia local, *modified on 12 sept 2026*) | los seis literales, `<picture>`/`srcset`/`sizes`, tres técnicas | Correctos (MDN dice «redes fluidas»; el tema, en redonda, «retículas fluidas»: traducción admisible) |
| Sánchez Cid y otros, *VISUAL Review* 17(1), 2025 (texto del PDF) | autores; nombres; rechazo de «televised radio»; Ala-Fossi; debate; cuatro posibilidades; YouTube preferido | Correctos; ver M5 |
| Montador/a T12 (cerrado) | citas de YouTube del epígrafe adaptado (16:9, sin barras, Shorts desde 15-10-2024, canales estándar) | Literales |

Cuentas rehechas: 4096/2160 = 1,896 ≈ 1,90; 16/9 = 1,78; 1080 × 9/16 = 607,5; (1 + 0,05)/(0 + 0,05) = 21. Correctas.

## Hallazgos de exactitud

**Graves: 0.**

**Menores: 5.**

- **M1 · Error 9 (afirmación sin fuente): el 4:5.** Líneas 184, 636-637, 682 y 708 dan el 4:5 (y en 708 «1:1 o 4:5
  según la red») como formato de redes que «fija cada plataforma». La única plataforma leída es YouTube, que habla
  de relación «cuadrada o vertical», no de 4:5; las especificaciones de Instagram, TikTok y Facebook se declaran no
  leídas (l. 655, 753). El 1:1 tiene apoyo en la cita de YouTube; el 4:5 no, y no figura en la lista de oficio de la
  Trazabilidad. Propuesta: quitar el 4:5 o declararlo expresamente como uso de oficio sin fuente leída.
- **M2 · Error 9 (negativos absolutos).** L. 104-106 «Canal Sur no ha publicado una guía de estilo gráfico … ni un
  manual de identidad»; l. 354 «No tiene norma ni definición legal»; l. 751-752 «No hay tampoco norma ni documento
  público español que defina la radio visual». Son negativos que nadie puede confirmar leyendo; la fórmula del
  encargo es «no consta en documento publicado» / «no se ha encontrado». Propuesta: rebajar a «no consta».
- **M3 · Siglas presentadas que el tema no usa.** Las siglas de entrada presentan IU, UX, PNG, JPEG y SVG, que no
  aparecen en el cuerpo (el epígrafe de interfaz escribe «interfaz de usuario» y «experiencia de usuario» sin sigla).
  No es error de dato; es ruido. Propuesta: quitarlas de la lista o usarlas.
- **M4 · Error 6 (salvedad omitida) en 1.4.11 y rótulo impropio.** La columna «Qué exige» del 1.4.11 dice
  «controles: 3:1 frente a los colores vecinos» sin la excepción del propio criterio para los componentes de
  interfaz (**«except for inactive components or where the appearance of the component is determined by the user
  agent and not modified by the author»**), mientras que la de los objetos gráficos sí se cita. De paso: l. 535
  anuncia «Tres definiciones de las propias pautas», pero la tercera viñeta no es una definición sino la exención
  de logotipos del 1.4.3 (más la de texto incidental). Propuesta: añadir la excepción en redonda y retitular la
  lista («Tres precisiones de las pautas»).
- **M5 · Literal cortado sin marca.** L. 375-376: **«It is unclear whether radio with video can still be defined
  as radio, whether it constitutes a form of television, or whether it is a hybrid»** cierra comillas donde la
  fuente sigue: «that extends beyond the boundaries of traditional radio but does not fully align with the
  conventions of television». No cambia el sentido, pero la negrita = literal pide marcar el corte («…») o
  completar la frase.

Sin hallazgo, comprobado: art. 6.8 y 7.1 bien numerados; cláusula tercera 3.5 puntos 46-48; fecha del Acuerdo
(19-XII-2023) y de los BOJA 245 y 247; niveles A/AA de los cuatro criterios WCAG; texto grande 18 pt / 14 pt
negrita; luminancia relativa 0-1; atribución a Cavia Fraile ya corregida por la verificación; YouTube como
preferencia de la muestra, bien acotada a la encuesta.

## Cobertura del enunciado

Enunciado: «Diseño gráfico aplicado a televisión, radio visual, web, redes y plataformas digitales.» Los cinco
destinos tienen epígrafe, en el orden del enunciado. Televisión, radio visual, web y redes están bien cubiertas
(teoría, casa y práctica).

**Laguna (1): plataformas digitales en sentido propio.** El epígrafe 4 junta «redes y plataformas», pero de las
plataformas sólo da lo institucional (Canal Sur Más, Canal Sur Media, HbbTV y televisión conectada como literales
del Contrato-programa y de la Carta). No dice qué es HbbTV ni qué aporta al grafista, ni nada del diseño para la
aplicación OTT y el televisor conectado (visión a distancia, navegación con mando, carátulas de catálogo). La
pauta de oficio «se diseña pensando en la salida más estrecha» (l. 685) incluso empujaría a una respuesta
equivocada en una pregunta sobre interfaz de televisor. Preguntas 14 (a medias) y 15 (no). Propuesta para el
remate (Opus, amplía): un epígrafe breve «Plataformas OTT y televisión conectada» con fuente citable (p. ej.,
la especificación ETSI TS 102 796 para qué es HbbTV; guías de diseño de TV de fabricantes o de plataformas para
distancia de visión y navegación por foco), o, si no se confirma fuente, declararlo en «Lo que este tema no da».
Las miniaturas y carátulas ya están remitidas al tema 13.

## Preguntas tipo test

15 preguntas en `15-T01-preguntas.md` (teoría 9, práctica 6; TV 5, radio visual 2, web 3, redes 2,
plataformas 3): **13 enteras, 1 a medias, 1 no**.

## Resumen

Graves 0 · Menores 5 (M1-M5) · Lagunas 1 (plataformas digitales: OTT, televisión conectada, HbbTV).
