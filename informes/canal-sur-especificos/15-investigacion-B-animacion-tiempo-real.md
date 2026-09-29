# Grafista (puesto 15) · Investigación del bloque B-animacion-tiempo-real (temas 5, 6, 8, 9)

Fase 1 · Investigar. Fecha de trabajo: 29-09-2026 (el encargo fija «hoy» el 24-09-2026; las fuentes se
leyeron el 29-09-2026 y así se declara en cada una). Sólo lo que falta para cubrir el enunciado: lo
reutilizable (RTVE y temas cerrados de Canal Sur) ya está localizado y lo lee el redactor.

Convención: **negrita entre comillas = literal de la fuente**; lo demás, lectura propia o traducción.
«Oficio» = práctica de oficio sin norma que la fije. Cada dato lleva su fuente al lado.

Lo que ya dan los temas cerrados (no se repite aquí, sólo se señala para que el redactor no lo busque):

- Realizador/a 12: canal alfa y tabla de formatos con/sin alfa (TGA 32 bits), EBU R 95 (3,5 % / 5 %,
  valores en 1080 y 2160), grafismo HDR (BT.2408 Graphics White 75 % HLG / 58 % PQ, 203 cd/m²),
  seguimiento de cámara (Mo-Sys, FreeD), motor en tiempo real (Unreal), croma frente a pared de LED,
  paso de píxel y moiré (Epic), retardo de pantallas, envío por matriz/aux/M/E, plantillas Viz Pilot
  Edge (Vizrt).
- Realizador/a 14 y Montador/a 04: resolución, aspecto, BT.709/2020/2100, HDR (PQ/HLG, metadatos,
  conversiones), muestreo 4:4:4 + alfa, colorimetría «ALPHA» de SMPTE ST 2110 (Montador 04 § 11),
  límites EBU R 103, códecs (ProRes, DNxHD, XAVC, AVC-Intra), contenedores, AS-11, IMF, R 128.

---

## Tema 8 · Formatos técnicos: resolución, códecs, alfa, safe areas, colorimetría, HDR/SDR y entrega

### 8.1 Zonas seguras según SMPTE ST 2046-1:2009 (nuevo; los temas cerrados sólo dan EBU R 95)

Fuente: SMPTE ST 2046-1:2009, *Specifications for Safe Action and Safe Title Areas for Television*,
aprobada el 23-11-2009; PDF de la biblioteca pública de SMPTE
(https://pub.smpte.org/doc/st2046-1/20091123-pub/st2046-1-2009.pdf), leída el 29-09-2026. La
biblioteca la marca **«active»** con una sola versión, **«Publication (2009-11-23)»**: es la vigente.

- Qué sustituye: **«This Standard is a comprehensive revision of SMPTE RP 218-2002, Specifications for
  Safe Action and Safe Title Areas for Television Systems.»** (Introduction).
- Qué es una zona segura: **«A safe area, in the context of television production, is the area of the
  image that is certain to be seen by the vast majority of viewers in the home. Historically, two types
  of safe areas are specified, the Safe Action Area and the Safe Title Area. They differ in that the
  extremes of the Safe Action Area are deemed usable even if there is some degree of geometric,
  chromatic or other distortion, whereas the Safe Title Area must be free of these distortions.»**
  (Introduction, informativa).
- Por qué cambió: **«the complete replacement of scanned analog imagers and displays by fixed-pixel-matrix
  imagers and displays has eliminated the need for large tolerances in image geometry, convergence and
  displayed area.»** (Introduction).
- La familia SMPTE: **«SMPTE ST 2046-1, Specifications for Safe Action and Safe Title Areas for
  Television / SMPTE RP 2046-2, Safe Areas for Protection of Alternate Aspect Ratios / SMPTE RP 218,
  Specifications for Safe Action and Safe Title Areas for Television Systems (Note: The Scope of this
  Recommended Practice has been narrowed significantly.)»** (Introduction). RP 2046-2 no se ha leído.
- Alcance: **«This Standard defines and specifies Safe Action and Safe Title Areas for 1920 x 1080, 1280 x
  720, 720 x 576 and 720 x 480 television formats. This document is intended for application in program
  production where the image aspect ratio of the acquired essence is the same as that of the display.»**
  y **«They do not offer guidance in situations where material generated in one aspect ratio may need to
  be displayed in a different aspect ratio.»** (§ 1). No cubre UHD (2160): para 2160 sólo EBU R 95
  (en Realizador 12).
- Definiciones (§ 4.4 y 4.5): **«The Safe Action Area is the maximum image area within which all
  significant action shall be contained. The image area defined by the Safe Action Area is concentric
  with the Production Aperture.»**; **«The Safe Title Area is the maximum image area within which all
  significant title information shall be contained.»** Production Aperture (§ 4.3): **«the Image Lattice
  that represents the maximum possible active image area in a given image format»**.
- Redondeo (§ 5): **«Safe area calculations resulting in non-integer values for lines or pixel numbers
  shall be rounded to the nearest whole number.»**
- Valores (§ 5.1-5.4), todos con **«shall»**:

| Formato | Safe Action Area | Safe Title Area |
|---|---|---|
| 1920 x 1080 (§ 5.1) | **«93% of the width and 93% of the height of the Production Aperture (1786 x 1004)»** | **«90% of the width and 90% of the height of the Production Aperture (1728 x 972)»** |
| 1280 x 720 (§ 5.2) | 93 % **«(1190 x 670.)»** | 90 % **«(1152 x 648.)»** |
| 720 x 576 (§ 5.3), **«regardless of Aspect Ratio»** | 93 % **«(670 x 536)»** | 90 % **«(648 x 518.)»** |
| 720 x 480 (§ 5.4) | 93 % **«(670 x 446)»** | 90 % **«(648 x 432)»** |

- Compatibilidad heredada, sólo 480 líneas (§ 5.4): **«the RP-218 Safe Title Area and Safe Action Area
  may be used as follows: the Safe Action Area shall be 90% of the width and 90% of the height of the
  720 x 480 Image Lattice (648 x 432). The Safe Title Area shall be 80% of the width and 80% of the
  height of the 720 x 480 Image Lattice (576 x 384).»**
- Aviso de toda la imagen (§ 5, nota): **«many consumer fixed-pixel-matrix displays can be configured to
  show the entire image area. It is critically important to ensure that the entire image area is kept
  clear of extraneous elements such as lighting instruments, boom shadows, cables and graphics that are
  not intended to be seen by the viewer.»**
- Subtítulos (§ 5, nota): **«All versions of CEA-708 reference the SMPTE RP 218 Safe Title Area, which is
  80% of the width and 80% of the height of the Production Aperture.»** (norma de EE. UU.).
- Nota de 576 (§ 5.3): **«A different safe-area specification was developed by ITU-R for use during the
  transition period to wide-screen 16:9 broadcasting, and is still in use in some regions where 576-line
  formats are used.»** La bibliografía (anexo A) cita **«EBU R95 (2008)»** e **«ITU-R BT.1379-2 (09/07)»**.
- Casa entre normas (cálculo propio): 93 % del ancho = 3,5 % por cada lado; 90 % = 5 % por lado. Es lo
  mismo que EBU R 95 (**«3.5%»** acción y **«5%»** grafismo, en Realizador 12): en 1080 SMPTE y EBU
  coinciden en el porcentaje. Comprobación aritmética: 1920 × 0,93 = 1785,6 → 1786; 1080 × 0,93 =
  1004,4 → 1004; 1920 × 0,90 = 1728; 1080 × 0,90 = 972. Cotejado con la tabla de R 95 de Realizador 12
  (1080p: acción 1786 píxeles de ancho, líneas 80 a 1083 = 1004 líneas; grafismo 1728, líneas 96 a
  1067 = 972 líneas): en 1080 las dos normas dan las mismas cajas, 1786 × 1004 y 1728 × 972.
- Nombres: SMPTE dice «Safe Title Area» (título); EBU dice «Graphics Safe Area» (grafismo). Misma idea,
  distinto rótulo.

### 8.2 El alfa en la salida de un motor de grafismo: relleno y llave (Vizrt)

Fuente: Vizrt, *Viz Engine Administrator Guide* 5.4, «Video Output» (docs.vizrt.com/viz-engine-guide/
5.4/Video_Output.html) y 5.2, «Dual Channel Mode», leídas el 29-09-2026. En directo, el alfa sale del
motor como una segunda señal de vídeo (llave, *key*) junto a la de color (relleno, *fill*); el mezclador
la usa para incrustar (tres señales de la incrustación: RTVE edición-montaje 09 y Montador 07).

- **«Dual Channel is a video version with, typically, two program outputs (fill and key on two
  channels).»** (Dual Channel Mode).
- Propiedades de la llave (Key Properties): **«Contains Alpha: Defines if this output channel provides key
  information on the associated key output connector.»**; **«Downscale Luma: Compresses the luminance range
  of the output key signal from 0-255 to 16-235. Default mode is Active.»**; **«Invert Luma: Inverts the
  luminance part of the output key signal (inverts the key).»**; **«Watchdog Key Opaque: Specifies if the
  output key must be opaque or transparent when the watchdog unit activates.»**
- Márgenes de la señal: **«Allow Super White: Allows the luminance of the output signal to exceed the
  nominal SMPTE pixel values (100 IRE units) when enabled. Default mode is Inactive.»**; **«Allow Chroma
  Clipping: Determines whether to clip over-saturated chroma levels in the active portion of the output
  video signal.»** (enlaza con los límites EBU R 103 de Realizador 14).
- Sincronía: **«The fill and key channels are set with this H-delay.»** (misma fase para las dos señales).
- En IP, la colorimetría **«ALPHA»** de SMPTE ST 2110 para señales de llave ya está en Montador 04 § 11.

### 8.3 Ficheros de vídeo con alfa: ProRes 4444 (Apple)

Fuente: Apple, *Apple ProRes* (white paper), **«April 2022»**
(https://www.apple.com/final-cut-pro/docs/Apple_ProRes.pdf), leído el 29-09-2026. Realizador 14 cita la
familia ProRes pero no su alfa.

- **«Apple ProRes 4444: An extremely high-quality version of ProRes for 4:4:4:4 image sources (including
  alpha channels).»**; **«Apple ProRes 4444 is a high-quality solution for storing and exchanging motion
  graphics and composites, with excellent multigeneration performance and a mathematically lossless alpha
  channel up to 16 bits.»**; objetivo **«approximately 330 Mbps for 4:4:4 sources at 1920 x 1080 and
  29.97 fps»**.
- 4444 XQ: **«Like standard Apple ProRes 4444, this codec supports up to 12 bits per image channel and up
  to 16 bits for the alpha channel.»**; **«approximately 500 Mbps for 4:4:4 sources at 1920 x 1080 and
  29.97 fps»**.
- La regla: **«Note: Apple ProRes 4444 XQ and Apple ProRes 4444 are ideal for the exchange of motion
  graphics media because they are virtually lossless, and are the only ProRes codecs that support alpha
  channels.»** Ningún ProRes 422 lleva alfa.
- Premultiplicado o directo al exportar: ver 5.3 (Resolve y Blender). EXR premultiplicado; PNG, TGA,
  BMP directos (glosario de Blender 5.2).
- No confirmado: alfa en DNxHR/DNxHD (Avid) y en el códec QuickTime Animation. Buscado «alpha» en el
  white paper de DNxHD de 2012 (`fuentes/fabricantes/Avid_DNxHD_white-paper-2012.txt`): no aparece. No
  afirmar que DNxHD lleve alfa.

### 8.4 Lo que no se pudo confirmar (tema 8)

- SMPTE RP 2046-2 (*Safe Areas for Protection of Alternate Aspect Ratios*): no leída.
- Recomendación UIT-R BT.1379 (zonas seguras en la transición 4:3/16:9): citada por ST 2046-1, no leída.
- sRGB (IEC 61966-2-1) frente a BT.709 para el grafismo que se diseña en programas de imagen fija: sin
  norma leída; sólo la mención de Epic a **«linear sRGB color space»** hacia la pared de LED (6.1).
- Entrega del grafismo para emisión (qué pide Canal Sur: fichero con alfa, secuencia de imágenes, par
  relleno/llave): sin documento publicado de la casa.

---

## Tema 5 · Animación 2D/3D, motion graphics, composición, rotoscopia, tracking y efectos visuales

Lo que ya hay: RTVE diseño-gráfico 04 § 4 (stop motion, pixilación, rotoscopia, animatrónica), 11
(capa, alfa, incrustación, seguimiento de uno/dos puntos/plano/cámara, interpolación), edición-montaje
09 (tres señales de la incrustación, precomposición, fotogramas clave). Montador 07 § 3 y Realizador
13 (fotograma clave, interpolación, curva de velocidad, incrustación, alfa, máscara) ya cerrados.
Todo eso va **sin fuente** en RTVE; lo que sigue le pone fuente oficial y cubre 3D, rotoscopia y
tracking con documentación de fabricante.

### 5.1 La norma española que describe el oficio: RD 1583/2011 (título FP de Animaciones 3D)

Fuente: Real Decreto 1583/2011, de 4 de noviembre, por el que se establece el Título de Técnico
Superior en Animaciones 3D, Juegos y Entornos Interactivos y se fijan sus enseñanzas mínimas
(BOE-A-2011-19532), texto del diario (https://www.boe.es/diario_boe/txt.php?id=BOE-A-2011-19532),
leído el 29-09-2026. No hay texto consolidado en el BOE (la API responde 404). Referencias posteriores
(ficha «Análisis» del BOE, leída el 29-09-2026): **«SE MODIFICA los arts. 2, 10, 12, 15, anexos I, III y
referencias indicadas, por Real Decreto 500/2024, de 21 de mayo (Ref. BOE-A-2024-10685).»**;
**«SE DEROGA el anexo indicado, por Real Decreto 1085/2020, de 9 de diciembre»**; corrección de errores
BOE núm. 61, de 12-III-2012; currículo: Orden ECD/309/2012. **Comprobado en el RD 500/2024** (art. 7,
leído el 29-09-2026): la modificación del anexo I sólo **«Se suprimen los siguientes módulos
profesionales: Formación y Orientación Laboral, Empresa e iniciativa emprendedora y Formación en
centros de trabajo»**, añade Inglés profesional, Itinerarios, Digitalización y Sostenibilidad y
cambia «Proyecto» por **«Proyecto intermodular»**. Los módulos técnicos citados abajo (1085-1088,
0907) siguen como en 2011. No se ha comprobado qué anexo derogó el RD 1085/2020 (probablemente una
cualificación; sin leer) ni la corrección de errores de 2012: el redactor debe mirarlas si cita
literal algún criterio.

- Competencia general (art. 4): **«La competencia general de este título consiste en generar
  animaciones 2D y 3D para producciones audiovisuales y desarrollar productos audiovisuales multimedia
  interactivos»**.
- Fases de la animación 2D (art. 5.c): **«Producir el proyecto de animación 2D en sus fases de
  animática, layout, animación clave, intercalación, pintura y composición, realizando los chequeos y
  pruebas de línea necesarias hasta la obtención de las imágenes definitivas que lo conforman.»**
- Fases de la animación 3D (art. 5.d): **«Producir el proyecto de animación 3D en sus fases de diseño y
  modelado, setup, texturización, iluminación, animación y renderizado, realizando los chequeos
  necesarios hasta la obtención de las imágenes definitivas que lo conforman.»** ← el canon de fases
  3D con fuente oficial.
- Módulo 1087 «Animación de elementos 2D y 3D» (16 ECTS, 150 h):
  - RA 1: **«Realiza la animación y captura en stop motion o pixilación»**; contenidos: **«La
    persistencia retiniana.»**, **«Asignación y reparto de tiempos. Temporalización (timing) y
    fragmentación del movimiento.»**, **«La pixilación.»**, **«(sincronización, lipsync)»**.
  - RA 2 (setup/rigging): **«Se ha construido un esqueleto dentro de cada modelo que se va a animar
    mediante una jerarquía de ensamblajes (joints)»** (2.b); **«Se ha realizado la asignación de
    cinemáticas a diferentes partes del esqueleto, diferenciando directas (FK) e inversas (IK) para
    poder controlar varias articulaciones al mismo tiempo, influyendo unas en otras.»** (2.c); **«Se ha
    emparentado la geometría con el esqueleto (bind skin)»** (2.d); **«Se han pintado los pesos o
    influencias de los ensamblajes sobre los puntos de la geometría»** (2.e); **«Se han incluido
    músculos y diferenciado los sólidos rígidos (rigid bodies) y la geometrías controladas por
    partículas (soft bodies)»** (2.g).
  - RA 3 (2D): **«Se han dibujando los fotogramas clave y se han fragmentado decorados, personajes y
    elementos de atrezo en las diferentes capas que hay que animar»** (3.b, errata «dibujando» en el
    original); **«Se han dibujado las intercalaciones, adaptándose a los tiempos marcados y a los
    dibujos anteriores y posteriores según la carta de animación.»** (3.c). Contenidos: **«La carta de
    animación»**, **«La animación en fotogramas completos.»**, **«La intercalación.»**
  - RA 4 (efectos 3D): **«Se han generado las partículas y se han creado los emisores necesarios para
    cada plano, asignando los campos de fuerza que definirán el comportamiento de estas.»** (4.b);
    **«Se han creado multitudes realizando la sustitución de las partículas por modelos animados.»**
    (4.e).
  - RA 6 (cámara virtual): **«Se han marcado las trayectorias de los movimientos de cámara
    temporizando los mismos (arranques, frenadas, aceleraciones y deceleraciones) mediante la
    colocación de fotogramas clave (key frames)»** (6.d).
  - RA 7: **«Realiza la captura de movimiento y rotoscopia en 2D y 3D»**; **«Se ha realizado la
    ubicación definitiva de los sensores de captura en los puntos adecuados del actor»** (7.c); **«Se
    han dibujado, física o virtualmente, sobre las imágenes de referencia, los personajes y elementos
    que se van a animar, respetando las hojas de modelo.»** (7.i). Contenidos: **«Sistemas de captura
    de movimiento: • Herramientas de captura de movimiento: software, cámaras y sensores.»**; **«La
    rotoscopia: • Obtención, escalado y archivado de las imágenes originales. […] • Elaboración de
    superposiciones y rotoscopias: en superficies planas y por ordenador.»**
- Módulo 1085 «Proyectos de animación audiovisual 2D y 3D», RA 3 y 4 (render por capas): **«Realiza la
  separación de capas y organiza los efectos de render»**; **«Se ha valorado la disponibilidad,
  capacidad y velocidad de las estaciones de trabajo y granja de render»** (4.a); **«Se ha comprobado el
  cumplimiento de los requisitos del render (integridad del fotograma, orden y posición de los
  elementos de las capa y flicker, entre otros) fotograma a fotograma y capa a capa.»** (4.c).
  Contenidos: **«Separación de elementos en capas.»**, **«Las granjas de render.»**
- Módulo 1088 «Color, iluminación y acabados 2D y 3D»: **«Genera los mapas UV de los modelos»** (RA 1);
  tipos: **«usando los mapas planos, cilíndricos, esféricos, automáticos o basados en cámara»** (1.b).
  Materiales: **«Especularidad. • Ambientación. • Transparencia. • Reflexión. • Refracción. •
  Translucencia. • Autoiluminación. • Relieve.»**; **«Las texturas procedurales 2D.»**, **«Las
  texturas procedurales 3D.»**
- Módulo 0907 «Realización del montaje y postproducción de audiovisuales» (común con RD 1680/2011, ya
  citado en Realizador 13): contenidos **«Técnicas y procedimientos de composición multicapa: •
  Organización del proyecto y flujo de trabajo. • Gestión de capas. • Creación de máscaras. •
  Animación. Interpolación. Trayectorias.»**; **«Efectos de key. Superposición e incrustación.»**;
  **«Planificación de la grabación para efectos de seguimiento.»**; **«Técnicas de creación de
  gráficos y rotulación.»**

### 5.2 Vocabulario 3D y de animación con fuente (Blender 5.2 LTS Manual)

Fuente: Blender Foundation, *Blender 5.2 LTS Manual* (docs.blender.org/manual/en/latest/, el título de
página dice **«Blender 5.2 LTS Manual»**), leído el 29-09-2026. Páginas: «Glossary», «Animation ›
Introduction», «Keyframes › Introduction», «Graph Editor › F-Curves › Properties», «Movie Clip ›
Tracking › Introduction», «Masking › Introduction». Documentación de un programa libre; vale como
definición técnica, no como norma.

- Animación: **«Animation is making an object move or change shape over time.»**; tres modos: **«Moving
  as a whole object»**, **«Deforming them»**, **«Inherited animation»** (movimiento heredado de un
  padre, gancho o armadura). **«Animation is typically achieved with the use of keyframes.»**
- Fotograma clave (glosario): **«A frame in an animated sequence drawn or otherwise constructed
  directly by the animator. In classical animation, when all frames were drawn by animators, the senior
  artist would draw these frames, leaving the “in between” frames to an apprentice. Now, the animator
  creates only the first and last frames of a simple sequence (keyframes); the computer fills in the
  gap.»** Interpolación (glosario): **«The process of calculating new data between points of known
  value, like Keyframes.»**
- Tipos de interpolación (Keyframes › Introduction): **«There are a number of modes with fixed shapes,
  e.g. Constant, Linear, Quadratic etc, and a free form Bézier mode.»**; las curvas: **«Keyframe
  interpolation is represented and controlled by animation curves, also known as F-Curves.»**; **«The X
  axis of the curve corresponds to time, while Y represents the value of the property.»**; extrapolación:
  **«Extrapolation specifies how the curve extends before the first, and after the last keyframe.»**
- Constante (F-Curves › Properties): **«The curve holds the value until the next keyframe, producing a
  stair step effect with very abrupt changes. Normally only used during the initial “blocking” stage in
  pose-to-pose animation workflows.»**
- Suavizado (*easing*): **«Ease In: The value accelerates, moving slowly at the beginning of the curve
  segment and speeding up towards the end.»**; **«Ease Out: The value decelerates, moving quickly at the
  beginning of the curve segment and slowing down towards the end.»**; **«Ease In Out: The value moves
  slowly in the beginning, speeds up towards the middle, and slows down again towards the end.»**
  Efectos dinámicos: **«Bounce Makes the value bounce a few times with exponential decay, like a tennis
  ball that was dropped on the floor.»**
- Rigging (Animation › Introduction): **«Rigging is a general term used for adding controls to objects,
  typically for the purpose of animation.»**; **«Rigs effectively define a user interface for the
  animator to use, without being concerned with the underlying mechanisms»**.
- FK / IK (glosario): FK **«The process of determining the movement of interconnected segments or bones
  of a body or model in the order from the parent bones to the child bones.»**; IK **«… in the order from
  the child bones to the parent bones. Using inverse kinematics on a hierarchically structured object,
  you can move the hand then the upper and lower arm will automatically follow that movement.»**
- Malla, mapa UV, render (glosario): Mesh **«Type of object consisting of Vertices, Edges and Faces.»**;
  UV Map **«Defines a relation between the surface of a mesh and a 2D texture.»**; Render **«The process
  of computationally generating a 2D image from 3D geometry.»**; Ray Tracing **«Rendering technique that
  works by tracing the path taken by a ray of light through the scene, and calculating reflection,
  refraction, or absorption of the ray whenever it intersects an object in the world. More accurate
  than Scanline, but much slower.»**
- Desenfoque de movimiento (glosario): **«Simulating motion blur makes computer animation appear more
  realistic.»**
- Máscara/mate (glosario): **«Matte¶Mask¶A grayscale image used to include or exclude parts of an
  image. A matte is applied as an Alpha Channel, or it is used as a mix factor when applying Color
  Blend Modes.»** (el «¶» es del volcado: separa los dos rótulos, Matte y Mask).
- Tracking (Movie Clip › Tracking › Introduction): **«Blender’s motion tracker supports a couple of very
  powerful tools for 2D tracking and 3D motion reconstruction, including camera tracking and object
  tracking, as well as some special features like the plane track for compositing. Tracks can also be
  used to move and deform masks for rotoscoping»**. Distorsión de objetivo: **«All cameras record
  distorted video.»** y **«For accurate camera motion, the exact value of the focal length and the
  “strength” of distortion are needed.»** Estabilización: **«the 2D Stabilization is able to detect and
  compensate such movements»**.
- Rotoscopia con máscaras (Masking › Introduction): **«They can be used for manual rotoscoping to pull a
  particular object out of the footage, or as a rough matte for green-screen keying.»**; **«Masks can be
  animated over the time so that they follow some object from the footage, e.g. a running actor. This
  can be achieved with shape keys or parenting the mask to tracking markers.»**

### 5.3 Tracking, rotoscopia y alfa en un compositor de nodos (Blackmagic, DaVinci Resolve 21 / Fusion)

Fuente: Blackmagic Design, *DaVinci Resolve 21 Reference Manual*, **«July 2026»** (PDF de 1 390 252
palabras, volcado en el scratchpad de sesiones anteriores; el mismo manual que cita Montador 13),
leído el 29-09-2026. Capítulos 77 «Understanding Image Channels» (pp. 1726-1728), 79 «Rotoscoping with
Masks» (p. 1775), 81 «Using the Tracker Node» (p. 1827), 85 «3D Camera Tracking» (p. 1930) y 139
«Magic Mask» (p. 3338).

- Definición de tracking: **«Tracking is one of the most useful and essential techniques available to
  a compositor. It can be roughly defined as the creation of a motion path from analyzing a specific
  area in a clip over time.»**; usos: **«stabilization, motion smoothing, matching the motion of one
  object to that of another»**.
- Tres tipos de tracker (el cuadro de RTVE con fuente):
  - **«Tracker: Follows a relatively small, identifiable feature or pattern in a clip to derive a 2D
    motion path. This is sometimes referred to as point tracking.»**
  - **«Planar Tracker: Follows a flat, unvarying surface area in a clip to derive a 2 ½D motion path
    including perspective. A planar tracker is also more tolerant than a point tracker when some tracked
    pixels move offscreen or become obscured.»**
  - **«Camera Tracker: Tracks multiple points or patterns in a clip and performs a more sophisticated
    analysis by comparing those moving patterns. The result is a precise recreation of the live-action
    camera in virtual 3D space.»**
  - El nodo Tracker hace **«tracking, stabilizing, matching moving, and corner-pinning operations»**.
- Seguimiento de cámara 3D: **«Camera tracking is used for match moving, and it’s a vital link between
  2D scenes and 3D scenes, allowing compositors to integrate 3D CGI elements into live-action clips.»**;
  **«camera tracking algorithms follow features that are “nailed to the set.” Objects in the scene that
  move independently of the camera movement in the shot, such as cars driving or people walking, cause
  poor tracks, so masks can be used to restrict the features that are tracked»**; **«it is helpful to
  provide specific camera metadata, such as the sensor size and the focal length of the lens»**; dos
  fases: **«Tracking, which is the analysis of a scene.»** y **«Solving, which calculates the virtual 3D
  scene.»**; resultado: **«The Camera Tracker’s purpose is to create a 3D animated camera and point
  cloud of the scene.»**
- Rotoscopia con polilíneas: **«Polygon masks are user-created Bézier shapes. This is the most common
  type of polyline and the basic workhorse of rotoscoping.»**; **«Mask nodes create an image that is used
  to define transparency in another image. Unlike other image creation nodes in Fusion, mask nodes
  create a single channel image rather than a full RGBA image.»**
- Rotoscopia asistida por IA (Magic Mask): **«The Magic Mask palette uses the DaVinci Neural Engine,
  guided by the user via a click-based interface, to automatically create detailed masks with which to
  isolate objects or humans, either whole or in part»** (la v2 es **«Studio Version Only»**, índice del
  capítulo).
- Alfa directo y premultiplicado (cap. 77, p. 1726): **«Unpremultipled (Straight): An RGB image
  unaltered by the semi-transparency information in a fourth channel (alpha channel)»** (errata
  «Unpremultipled» en el original); **«Premultiplied: An RGB image that has each channel multiplied by
  its alpha channel before compositing.»**; **«The alpha channel itself is not multiplied. The R, G, and
  B channels are multiplied by the alpha.»**; **«Most computer-generated images are premultiplied for
  convenience»** (p. 1727); **«color correction is best performed on a non-premultiplied (straight) RGBA
  image»**.
- Reglas (p. 1728): **«Always use premultiplied images with a Merge node. / Only color-correct images
  that are not premultiplied. / Always filter and transform images that are premultiplied. / Never
  double premultiply an image.»**; el fallo típico: **«if the image is not premultiplied, the pixels
  that should be transparent are still added, which typically results in an unwanted bright fringe
  around the edges of your foreground subject.»**
- Mismo concepto en el glosario de Blender 5.2 (para contrastar): Straight **«This is the alpha type
  used by paint programs such as Photoshop or Gimp, and used in common file formats like PNG, BMP or
  TARGA.»**; Premultiplied **«This is the natural output of render engines […] The OpenEXR file format
  uses this alpha type.»**; conversión: **«Conversion between the two alpha types is not a simple
  operation and can involve data loss»**.

### 5.4 Motion graphics y VFX: lo que se ha podido y no se ha podido fijar

- Motion graphics: no se ha encontrado definición en norma ni en manual universitario leído. Uso
  documentado del término: el manual de Resolve 21 dice **«DaVinci Resolve integrates editing,
  compositing and motion graphics, color»** (p. inicial) y Apple llama a ProRes 4444 **«a high-quality
  solution for storing and exchanging motion graphics and composites»** (8.3). Definirlo como «grafismo
  animado» es oficio.
- VFX: el RD 1583/2011 habla de **«animaciones para incrustación de efectos especiales en películas de
  imagen real»** (orientaciones del 1087) y de **«efectos 3D»** con partículas, rigid y soft bodies (RA
  4). El manual de Resolve: **«In addition to the kinds of robust compositing, paint, rotoscoping, and
  keying effects you’d expect»** (Fusion). Sin definición normativa de «efectos visuales» frente a
  «efectos especiales»: oficio.
- Doce principios de animación (Thomas y Johnston, Disney): no leídos en fuente; no se incluyen.
- Adobe After Effects (interpolación, Roto Brush, Mocha, 3D Camera Tracker, expresiones): la ayuda de
  helpx.adobe.com devuelve **403/Access Denied** a la descarga el 29-09-2026. No confirmado; si el
  redactor quiere nombrarlo, sólo como programa (ya está en RTVE diseño-gráfico 10 § 4).

---

## Tema 6 · Escenarios virtuales, realidad aumentada, pantallas, videowalls y grafismo en tiempo real

Lo que ya hay: Realizador 12 (cerrado) da decorado virtual/RA/producción virtual, seguimiento de
cámara, motor en tiempo real, retardo de RA, croma frente a LED, iluminación de croma, pantallas del
plató, moiré y paso de píxel, retardo de pantallas y envío por matriz/aux/M/E. RTVE realización 15-16,
ing-sup-teleco 16, diseño-gráfico 10 § 6 (Unreal, Unity, Vizrt, Chyron; diferido frente a tiempo
real). **Falta: videowall como sistema (armarios, procesador, controlador, clúster) y los fabricantes
con fuente.**

### 6.1 El videowall de LED: armarios, procesador y paso de píxel (Epic Games)

Fuente: Epic Games, *In-Camera VFX Overview in Unreal Engine* (documentación de Unreal Engine 5.8),
volcado local ya usado por Realizador 12 (`fuentes/canal-sur/realizador/web/epic-icvfx-overview.txt`),
releído el 29-09-2026. Realizador 12 sólo tomó paso de píxel, distancia y moiré; esto es lo nuevo.

- Armarios: **«An LED volume is made up of a cluster of cabinets. Each cabinet has a fixed resolution
  that can range from a very low resolution, such as 92x92 pixels that can be used for outdoor signs, to
  400x450 pixels for ultra-high-resolution indoor displays. The physical size of each cabinet can vary
  from manufacturer to manufacturer.»**
- Procesador de LED: **«The LED processor is the hardware and software that combines multiple cabinets
  into an array that displays a single image. You can arrange the cabinets in any configuration inside
  the canvas that the LED processor drives. On a large LED stage, there could be ten or more LED
  processors driving a seamless LED wall.»**
- Paso de píxel y coste: **«A higher pixel density means a noticeable increase in resolution and
  quality—and higher cost for each cabinet. A cabinet with a lower pixel pitch does not ensure it will be
  the correct product for your production, as other factors, such as viewing angle, color shift, color
  consistency, and heat dissipation, must also be considered.»**
- Frustum interior/exterior (producción virtual en LED): **«This inner frustum represents the field of
  view (FOV) from the camera's perspective based on the current lens focal length.»**; **«Content
  displayed on the LED volume outside of the camera's FOV is called the outer frustum. This outer frustum
  turns the LED panels into a dynamic light and reflection source for the physical set»**.
- Sincronía: **«Each device, such as the camera, computers, and tracking systems, has an internal clock.
  […] This can cause problems in the resulting display, such as tearing, if they are not unified.
  Genlocking with nDisplay prevents these issues.»**
- Color hacia la pared: **«Ensure that the tonemapper is disabled so content from the engine does not
  have a tone curve and is in linear sRGB color space as input to the LED panels.»** OCIO: **«OpenColorIO,
  or OCIO, is a color management system used primarily in film and virtual production.»**
- Efectos que no deben usarse en un clúster: **«Screen spaced effects such as SSGI, SSAO, SSR, vignetting,
  eye-adaptation, and bloom should be avoided. Since the nature of these effects are screen spaced, there
  can be issues with borders between two clustered nodes in the nDisplay system.»**
- Composición en directo (croma dentro del frustum): **«Composure is Unreal Engine's framework for
  real-time compositing. With this suite of features, you can include live video feeds, AR compositing,
  green-screen keying, garbage mattes, color correction, and lens distortion in your shots.»**

Fuente complementaria: Epic Games, *Recommended Hardware for In-Camera VFX in Unreal Engine* (UE 5.8,
dev.epicgames.com), leída el 29-09-2026:

- **«Most LED processors have the option to receive sync either from an external genlock source or from
  the incoming video signal from the graphics cards.»**
- **«NVIDIA Quadro Sync is required to synchronize displays across an LED volume. Each render node
  machine must have this card in addition to its graphics card.»**
- **«If you plan to use live green-screen compositing, you will need a SDI video card to handle camera
  input, compositing output, and timecode synchronization. SDI video cards such as the AJA Kona 5 and the
  Blackmagic DeckLink are recommended for live compositing.»**

### 6.2 Muchas pantallas como un solo lienzo: nDisplay (Epic Games)

Fuente: Epic Games, *nDisplay Overview for Unreal Engine* (UE 5.8; descripción de la página:
**«Describes how multiple computers work together in an nDisplay rendering network.»**), leída el
29-09-2026.

- **«Every nDisplay setup has a single primary computer, and any number of additional computers, called
  secondary nodes.»**; **«Each Unreal Engine instance handles rendering to one or more display devices,
  such as screens, LED displays, or projectors.»**
- Para qué: **«By setting up these viewports so that their location in the 3D world matches the physical
  locations of the screens or projected surfaces in the real world, you give viewers the illusion of being
  present and immersed in the virtual world.»**
- El plugin **«ensures all instances render the same frame at the same time, ensures each display device
  renders the correct frustum of the game world»**.
- Lienzo: **«Using the Output Mapping tool, these separate viewports are then mapped into different areas
  of a large 2D canvas, referred to as the application window.»**; **«We recommend leveraging
  multi-display technologies from graphics card vendors such as NVIDIA Mosaic or AMD Eyefinity to treat
  multiple connected displays as one display.»**
- Tolerancia a fallos: **«when a render node becomes unresponsive, whether because of a crash or because it
  loses its network connection, it is dropped from the cluster after a configurable timeout value.»**

### 6.3 Videowall de plató en un sistema de grafismo de televisión (Vizrt)

Fuente: Vizrt, *Viz Multiplay User Guide* 3.3, «Introduction» (docs.vizrt.com/viz-multiplay-guide/3.3/
Introduction.html, © 2025), leída el 29-09-2026.

- **«Viz Multiplay is a powerful tool for controlling studio screen content. The simple interface can be
  used in the control room or by the presenter in the studio.»**; funciones: **«Send content quickly to
  multiple screens.»**, **«Control live, video, graphics and still images.»**, **«Build playlists and
  full content editing.»**
- Arquitectura: **«Uses Viz Engine for playout»**; **«The video wall feature allows up to four
  DisplayPort outputs with UHD resolution from a single GPU in a Viz Engine. With Datapath Fx4 display
  controllers, the number of outputs can be increased to match numerous screens and panels of different
  shapes and orientations.»**; **«Also supports Standard SDI-based playout.»**; **«Can open and control
  newsroom playlists in a MOS workflow.»**; **«You are able to access and use templates and elements from
  Pilot Data Server.»**

Fuente: Vizrt, *Viz Engine Administrator Guide* 5.4, «Video Output» (docs.vizrt.com/viz-engine-guide/5.4/
Video_Output.html), leída el 29-09-2026:

- **«Video Wall/Multi-Display: Sets the main output to the Digital Visual Interface (DVI). Important: For
  video wall setups, this setting must be active and the output format must be set to FULLSCREEN.»**
  (el videowall se alimenta por salida de gráfica, no por SDI).

### 6.4 Tres sistemas de grafismo en tiempo real, con fuente del fabricante

**Vizrt (Viz Artist / Viz Engine).** Fuente: *Introduction to Viz Artist* (documentation.vizrt.com/
viz-artist-guide/5.3/), leída el 29-09-2026: **«Throughout this guide, the term Viz refers to the
complete software suite installed, and as a general reference for the following modes: Viz Artist / Viz
Engine […] / Viz Configuration»**; **«The available features and modes of the software depend on the
license on the connected license hardware dongle.»** Doble canal (*Viz Engine Administrator Guide* 5.2,
«Dual Channel Mode», leída el 29-09-2026): **«Dual Channel is a video version with, typically, two
program outputs (fill and key on two channels). To support two program outputs, this option requires two
graphics cards.»**; **«use an external application (for example, Viz Trio or Viz Pilot) to control the
Viz Engine.»** Plantillas de Viz Pilot Edge / Template Builder: ya en la investigación de Realizador
(33-investigacion-B, § 12.2) y en Realizador 12; no se repite.

**Unreal Engine (Epic Games) · Motion Design.** Fuente: *Motion Design in Unreal Engine* y *Motion
Design Quickstart Guide in Unreal Engine* (UE 5.8, dev.epicgames.com), leídas el 29-09-2026:

- **«Motion Design is a feature set for motion graphics artists who need a streamlined and creative suite
  of tools that provide for rapid iteration and scalability. Motion Design includes a reworked world
  outliner, user interface, rigging tools, cloners, customizable 2D/3D shapes, and a new way to create
  materials using a streamlined, layer-based workflow called Material Designer.»**
- **«Motion Design offers a robust Rundown tool that, in conjunction with its Transition Logic system,
  can run live-updated broadcast graphics with minimal rigging.»**; **«All of Motion Design's features
  combine to help you create on-air compatible graphics as well as high-end 3D product design and
  advertising visuals.»**
- **«Motion Design is an Internal Editor plugin for broadcasting. You can use it for graphics creation,
  playout, and real-time data visualization for live television, news, weather, sports production,
  interstitial graphics»** (Quickstart).
- La barra del visor incluye **«color channel visualizer (useful for previewing the alpha channel)»** y
  **«safe frame toggle»** (Quickstart): alfa y zona segura también en el motor.
- Vídeo profesional: *Professional Video IO in Unreal Engine* (UE 5.8), leída el 29-09-2026: **«Play
  professional-level video and audio live in the Unreal Engine, composited into the virtual 3D world on
  the fly.»**; **«Apply effects to the imported video directly in the Unreal Engine, like chroma-keying,
  lens undistortion, color correction, and more.»**; **«Synchronize the Unreal Engine with the timecode
  and frame rate of your input video»**; **«Render video feeds from the Unreal Editor or from your running
  game project back out to your studio's video pipeline.»** Y su premisa: **«Augmented reality
  experiences — mixing traditional 2D video with real-time 3D environments — are becoming increasingly in
  demand for film and broadcast media applications.»**

**Chyron · PRIME.** Fuentes: página de producto *PRIME CG™ - 3D Real-Time Graphics* (chyron.com), nota
de prensa *Chyron Merges Live Web Content and CG Graphics with PRIME 5.3* (12-II-2026) y *About Chyron*
(chyron.com), leídas el 29-09-2026. Es publicidad del fabricante: vale para decir qué hace el producto,
no para valorarlo.

- **«A module of the PRIME Platform™, PRIME CG™ offers powerful 3D real-time graphics rendering,
  intuitive authoring tools and flexible playout capabilities to easily create and air sophisticated
  lower thirds, over-the-shoulders, bugs and other character-generated graphics.»** (rótulos inferiores,
  gráficos sobre el hombro del presentador, moscas). **«And designers with mastery of PRIME CG™ can apply
  their skills to PRIME Video Walls™, PRIME Touchscreen™, and PRIME Branding™.»**
- Herramientas: **«timelines, a spline editor, and a full set of effects, available for keyframing. Tight
  integration with best-in-class design tools, including full Adobe®️ Photoshop + After Effects import and
  Autodesk™️ FBX®️»**.
- Plantillas: **«Base Scenes, our templatized graphics creation feature, streamlines design
  workflows.»**; datos: **«Logic-based scenes function as editable templates that designers can configure
  to refresh up-to-the-second based on data feeds and trigger controls.»**; redacción: **«For pre-planned
  productions, PRIME CG integrates with all leading newsroom computer systems via Chyron CAMIO.»**
- La página cita ya **«PRIME 5.4»** (**«expands newsroom workflows, simplifies playout»**); la nota de
  5.3: **«PRIME 5.3 delivers the first official integration of HTML content within PRIME, through a
  powerful and flexible HTML Input.»** y **«news broadcasters can utilize the Playout Automation mode to
  dedicate all PRIME Engine performance to set-and-forget automated playout.»**
- Empresa: **«It all started in 1966»**; **«The PRIME Platform™ may be deployed with a range of
  functionalities, from graphics, to vision mixing, branding, video walls, venue control, touchscreen
  and more.»**; protocolos: **«our products support CII, AMP, PBus, VDPC, XML, Oxtel and RossTalk»**.
- Que «chyron» se use en EE. UU. como nombre común del rótulo inferior: no leído en fuente; no se afirma.

### 6.5 No confirmado (tema 6)

- Documentación de Brompton (procesadores Tessera) y de otros fabricantes de LED: la web no responde al
  proxy (502 / página vacía) el 29-09-2026. Lo del procesador de LED se apoya sólo en Epic.
- Videowall de LCD (marcos o *bezels*, controladoras de videowall): sin fuente leída; sólo Datapath
  aparece nombrado por Vizrt. No afirmar cifras de marco.
- Zero Density, Pixotope, Ross (XPression): no investigados; si el redactor los nombra, sin datos.
- Qué sistema de grafismo, plató virtual o videowall tiene Canal Sur: sin documento publicado leído.

---

## Tema 9 · Herramientas profesionales de diseño, composición, edición, plantillas y automatización gráfica

Lo que ya hay: RTVE diseño-gráfico 10 (tres familias de programa: imagen fija, vectorial,
composición/animación; formatos de fichero; tiempo real). **Aviso al redactor: hay un tema cerrado de
Canal Sur que el encargo no lista y cubre la mitad «plantillas y automatización»:** Montador 13
(`30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`), § 2
«Plantillas» (plantillas de rótulo, Motion Graphics templates de Adobe, plantillas basadas en datos,
*presets*, variables de metadatos) y § 4 «Newsroom» (protocolo MOS, con MOS 2.8.5 y 4.0 leídos). Copiar
literal; no investigar de nuevo. También Realizador 12 § «Diseñar, rellenar y lanzar» (Viz Pilot Edge).

Lo nuevo: plantillas y automatización en los sistemas de directo y en un compositor.

### 9.1 Plantillas en los sistemas de grafismo de directo

- Vizrt: *Viz Pilot Edge* y *Template Builder* (ya en 33-investigacion-B § 12.2 y Realizador 12).
  Viz Multiplay **«You are able to access and use templates and elements from Pilot Data Server.»** y
  **«Can open and control newsroom playlists in a MOS workflow.»** (6.3).
- Chyron PRIME (6.4): **«Base Scenes, our templatized graphics creation feature, streamlines design
  workflows. With full access to all the elements of a base scene (conditions, events, triggers,
  data-binding, etc.), a designer can make full-package changes in minutes instead of hours!»**;
  **«Logic-based scenes function as editable templates that designers can configure to refresh
  up-to-the-second based on data feeds and trigger controls.»**; automatización: **«Playout Automation
  mode»** (PRIME 5.3).
- Unreal Engine Motion Design: *Setting Up Rundown Server for Motion Design in Unreal Engine* (UE 5.8),
  leída el 29-09-2026: **«Controlling the Motion Design playout can be accomplished by combining two
  APIs. The Rundown Server API is used to load the rundown assets and the page’s templates, and contains
  an embedded Remote Control Preset (RCP).»**; **«The RCP for the corresponding page can be accessed and
  modified via the Remote Control API, then saved back in the rundown page for immediate or later
  playout.»**; **«The Rundown Server API is exposed to WebSocket through the WebSocket Messaging bridge
  plugin.»** Lectura: escaleta (*rundown*) + páginas con plantilla + control remoto por red = el mismo
  esquema diseño/relleno/lanzamiento de Vizrt y Chyron (cotejo propio).
- CasparCG (programa libre de emisión de grafismo). Fuente: README del repositorio CasparCG/server
  (raw.githubusercontent.com/CasparCG/server/master/README.md), leído el 29-09-2026: **«CasparCG
  Server, a professional software used to play out and record professional graphics, audio and video to
  multiple outputs. CasparCG Server has been in 24/7 broadcast production since 2006.»**; **«CasparCG
  Server is distributed under the GNU General Public License GPLv3 or higher»**; cliente aparte:
  **«Connect to the Server from a client software, such as the "CasparCG Client"»**. Que sus plantillas
  sean HTML: la wiki no se pudo descargar (404); no se afirma. Que lo creara la televisión pública
  sueca (SVT): no leído; no se afirma.

### 9.2 Plantillas y automatización en un compositor (DaVinci Resolve 21 / Fusion)

Fuente: *DaVinci Resolve 21 Reference Manual* (julio de 2026), leído el 29-09-2026.

- Plantilla de rótulo (cap. 56, p. 1226): **«In actuality, these text generators are Fusion templates,
  which are Fusion compositions that have been turned into macros and come installed with DaVinci
  Resolve to be used from within the Edit page like any other generator.»**; se crean propias:
  **«It’s possible to make all kinds of Fusion title compositions in the Fusion page, and save them for
  use in the Edit page by creating a macro»**.
- Expresiones (cap. 73, p. 1634): **«Simple Expressions are a special type of script that can be placed
  alongside the parameter it is controlling. These are useful for setting simple calculations, building
  unidirectional parameter connections, or a combination of both.»**
- Guiones (cap. 73, p. 1640): **«Scripting is an essential means of increasing productivity. Scripts can
  create new capabilities or automate repetitive tasks, especially those specific to your projects and
  workflows. Inside Fusion, scripts can rearrange nodes in a comp, manage caches, and generate multiple
  output files for delivery.»**; **«FusionScript is the blanket term for the scripting environment in
  Fusion. It includes support for Lua as well as Python 2 and 3 for some contexts.»**

### 9.3 Familias de herramientas: lo que queda sin fuente

- Adobe (Photoshop, Illustrator, After Effects, Premiere): la ayuda de helpx.adobe.com da **403** el
  29-09-2026 a la descarga directa (Montador 13 sí la leyó el 25-09-2026 para los Motion Graphics
  templates: usar eso). Variables y conjuntos de datos de Photoshop/Illustrator, expresiones de After
  Effects: no confirmados.
- Blender (libre) y Resolve/Fusion (Blackmagic): documentados arriba (5.2, 5.3). Cinema 4D, Maya,
  Houdini, Nuke: no leídos (la página de Foundry sobre premultiplicación no devolvió contenido).
- Cuadro diferido/tiempo real de RTVE diseño-gráfico 10 § 6: sostenible con Epic (Motion Design para
  **«on-air compatible graphics»**) y Vizrt/Chyron (motores de directo); Blender como render diferido
  lo sostiene su glosario (**«The process of computationally generating a 2D image from 3D geometry.»**) sólo en parte: que sea «diferido» es oficio.

---

## Trazabilidad (fuentes leídas en esta fase, todas el 29-09-2026)

| Fuente | Temas | Qué sostiene |
|---|---|---|
| SMPTE ST 2046-1:2009, PDF de pub.smpte.org (estado **«active»**, única versión 23-11-2009) | 8 | Zonas seguras de acción (93 %) y de título (90 %), píxeles por formato, RP 218 heredada |
| RD 1583/2011, título de Técnico Superior en Animaciones 3D, Juegos y Entornos Interactivos (BOE-A-2011-19532, texto del diario y ficha de referencias posteriores) | 5 | Fases 2D y 3D, rigging FK/IK, rotoscopia, captura de movimiento, render por capas, UV, materiales |
| RD 500/2024 (BOE-A-2024-10685), art. 7 y lista del art. 1.Dos (37.º) | 5 | Que la modificación del anexo I no toca los módulos técnicos |
| Blender Foundation, *Blender 5.2 LTS Manual*: Glossary; Animation, Keyframes, F-Curves Properties; Movie Clip Tracking; Masking | 5, 8 | Fotograma clave, interpolación, *easing*, rigging, FK/IK, malla, UV, render, trazado de rayos, máscara, tracking, rotoscopia, alfa directo/premultiplicado |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual* (julio de 2026), caps. 56 (p. 1226), 73 (pp. 1634, 1640), 77 (pp. 1726-1728), 79 (p. 1775), 81 (p. 1827), 85 (p. 1930), 139 (p. 3338) | 5, 8, 9 | Tipos de tracker, cámara 3D, rotoscopia con polilíneas, Magic Mask, premultiplicación y sus reglas, plantillas Fusion, expresiones, FusionScript |
| Apple, *Apple ProRes* white paper (abril de 2022) | 8 | ProRes 4444 y 4444 XQ con alfa hasta 16 bits; únicos ProRes con alfa |
| Epic Games, documentación de Unreal Engine 5.8: *In-Camera VFX Overview* (volcado local de Realizador, releído), *Recommended Hardware for In-Camera VFX*, *nDisplay Overview*, *Motion Design in Unreal Engine*, *Motion Design Quickstart Guide*, *Setting Up Rundown Server for Motion Design*, *Professional Video IO* | 6, 9 | Armarios, procesador de LED, frustum, genlock, clúster nDisplay, Motion Design, Rundown Server, E/S de vídeo |
| Vizrt: *Viz Multiplay User Guide* 3.3 «Introduction»; *Viz Engine Administrator Guide* 5.4 «Video Output» y 5.2 «Dual Channel Mode»; *Introduction to Viz Artist* 5.3 | 6, 8, 9 | Control de pantallas y videowall, salida DVI a pantalla completa, relleno y llave, propiedades de la llave |
| Chyron: *PRIME CG™ - 3D Real-Time Graphics*; nota *PRIME 5.3* (12-II-2026); *About Chyron* (chyron.com) | 6, 9 | Qué hace PRIME CG, Base Scenes, datos, CAMIO, HTML Input, Playout Automation, 1966 |
| CasparCG Server, README (GitHub) | 9 | Qué es, desde 2006, licencia GPLv3 |

Intentos fallidos (no se usa nada de ellos): ayuda de Adobe (helpx.adobe.com, 403), Foundry Nuke
(página vacía), Brompton (502 / página vacía), docs.chyron.com (502), wiki de CasparCG (404),
glosario ICVFX de Epic (página vacía).

Ficheros tocados: sólo este informe. Descargas de trabajo en el scratchpad de la sesión, fuera del
repositorio.
