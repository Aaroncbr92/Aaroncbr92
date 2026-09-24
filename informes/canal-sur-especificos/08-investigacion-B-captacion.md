# Puesto 08 · Cámara Operador · Investigación del bloque B-captacion (temas 3, 4, 8, 10, 13)

Fase 1 · Investigar. Fecha de trabajo: 24-09-2026. Se escribe según avanza.

Alcance: **sólo lo que falta** tras el material RTVE ya localizado por el coordinador (el redactor
lo copia de `temas/informacion-grafica/`, `temas/realizacion/`, `temas/montaje-equipos/`,
`temas/realizacion-tv/`). Aquí va: (a) lo propio de CSRTV que consta en documento publicado, y
(b) la fuente técnica de los huecos (operativa de cámara en retransmisión, entrevistas y relación
con redacción, cultura/sucesos/eventos no controlados, señales IP y coordinación con control).

Regla de cita: **negrita entre comillas = literal de la fuente**; redonda = paráfrasis o nota mía.

## Fuentes y fecha de lectura

| Clave | Documento | Dónde | Leído |
|---|---|---|---|
| **LE-CS** | *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, coord. José María Allas Llorente y Luis Carlos Díaz Salgado, 1.ª ed., marzo 2004, ISBN 84-609-0453-9 | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` (y .pdf) | 24-09-2026 |
| **LU800** | Ficha web del fabricante, LiveU LU800 | `fuentes/fabricantes/LiveU_LU800_ficha.txt` (página `liveu.tv`) | 24-09-2026 (fichero local; fecha de descarga no consta en el README de la carpeta) |
| **ST2110-IDX** | Índice oficial de la familia SMPTE ST 2110, `pub.smpte.org/doc/2110/` | `fuentes/normas-tecnicas/SMPTE-ST-2110-indice.md` (descargado 02-09-2026) | 24-09-2026 |

| **ST2110-10** | SMPTE ST 2110-10:2022, «Professional Media over Managed IP Networks: System Timing and Definitions», aprobada 28-03-2022, revisión de ST 2110-10:2017 | `pub.smpte.org/doc/st2110-10/20220328-pub/` → guardada en `fuentes/normas-tecnicas/SMPTE_ST-2110-10-2022.pdf` y `.txt` | 24-09-2026 |
| **ST2110-20** | SMPTE ST 2110-20:2022, «… Uncompressed Active Video», aprobada 14-12-2022 | `pub.smpte.org/doc/st2110-20/20221214-pub/` → `fuentes/normas-tecnicas/SMPTE_ST-2110-20-2022.pdf` y `.txt` | 24-09-2026 |
| **ST2110-30** | SMPTE ST 2110-30:2025, «… PCM Digital Audio», aprobada 01-10-2025, revisión de ST 2110-30:2017 | `pub.smpte.org/doc/st2110-30/20251001-pub/` → `fuentes/normas-tecnicas/SMPTE_ST-2110-30-2025.pdf` y `.txt` | 24-09-2026 |
| **ST311** | SMPTE 311-2009, «Television — Hybrid Electrical and Fiber-Optic Camera Cable», aprobada 04-06-2009, revisión de SMPTE 311M-2003 | `pub.smpte.org/doc/st311/20090604-pub/` → `fuentes/normas-tecnicas/SMPTE_ST-311-2009.pdf` y `.txt` | 24-09-2026 |
| **SRT-ID** | IETF Internet-Draft draft-sharabayko-srt-01, «The SRT Protocol», 07-09-2021; estado en datatracker: **expirado**, *Independent Submission*, estado previsto *Informational* | `datatracker.ietf.org/doc/html/draft-sharabayko-srt-01` | 24-09-2026 |
| **SRT-GH** | Repositorio de referencia de SRT (Haivision): README y `docs/API/API-socket-options.md` | `github.com/Haivision/srt` | 24-09-2026 |
| **SRT-AL** | SRT Alliance, portada | `srtalliance.org` | 24-09-2026 |
| **NDI-DOC** | NDI Docs & Guides: «What is NDI», «Discovery & Registration», «NDI Related Network Ports» (páginas vivas, sin fecha ni versión) | `docs.ndi.video/all/getting-started/...` | 24-09-2026 |
| **NMOS** | AMWA, índice de especificaciones NMOS | `specs.amwa.tv/nmos/` | 24-09-2026 |
| **ATEM** | Blackmagic Design, *Manual de instalación y funcionamiento ATEM Live Production Switchers*, español, dic. 2024 | `fuentes/fabricantes/Blackmagic_ATEM_manual-es.txt` | 24-09-2026 |
| **MVS060A** | Manfrotto, página de producto «Camera Slider, 60cm - MVS060A» | `manfrotto.com/global-en/camera-slider-60cm-mvs060a/` | 24-09-2026 |
| **TIFFEN** | Tiffen, página «Steadicam» | `tiffen.com/pages/steadicam` | 24-09-2026 |

Aviso de método: las fuentes web se leyeron con un extractor que resume; las citas web marcadas
**(extractor)** son la frase que el extractor devolvió entrecomillada, no cotejada línea a línea en el
HTML. Las citas de SMPTE, LE-CS y ATEM sí están leídas en el texto completo local.

Advertencias sobre **LE-CS** (valen para todo el bloque):
- Es de **2004**, anterior a la fusión de 2015 y al archivo en fichero: habla de **«cinta»**,
  **«barras»**, **«preroll»**, «CSTV» (= Canal Sur Televisión) y «Canal 2 Andalucía». Lo técnico
  que depende del soporte (barras al principio de cinta, TC a 00:00:00 «al principio de la cinta»)
  **es histórico** y el redactor debe presentarlo como tal, no como práctica vigente.
- Su valor normativo lo fija él mismo (Introducción, p. 9): **«no es un reglamento inﬂexible ni un
  compendio de obligaciones ineludibles. Es un conjunto de recomendaciones periodísticas y una
  selección de métodos de trabajo»**, pero **«hay casos en los que se marca una conducta
  obligatoria o se señala un comportamiento inaceptable. En estos casos no hay elección posible»**.
- No se ha localizado una edición posterior del Libro de estilo de CSRTV. No consta publicado un
  manual operativo de cámaras, de unidades móviles o de transmisiones de CSRTV.

---

## Tema 3 · Captación ENG, estudio, exteriores, unidades móviles, retransmisiones y directos informativos

Hueco declarado: operativa de cámara en retransmisión; lo propio de CSRTV.

### 3.1 El equipo ENG en CSRTV: el cámara dentro del tándem (LE-CS cap. 5, p. 79)

- Pórtico del cap. 5: **«El tándem cámara/periodista sale a la calle con una propuesta informativa
  concreta, acopio de documentación y una idea clara de la grabación que hay que acometer para
  poder mostrar una historia con los elementos básicos de la noticia y según la técnica narrativa
  audiovisual.»**
- **«La clave de un trabajo rápido y eﬁcaz es el orden para captar imagen y sonido de acuerdo con la
  estructura de narración y el formato que hayamos previsto, grabar en escenarios y situaciones
  determinadas y recoger testimonios y opiniones interesantes.»**
- 5.1 «El cámara y la cámara»: **«La cámara es en este punto la herramienta principal. Quien la
  maneja tiene que estar informado del hecho sobre el que trabajamos, con todas las claves
  posibles: los elementos noticiosos, la idea informativa básica, la orientación que se quiere dar
  a la noticia, los posibles cambios, margen de tiempo para trabajar... El periodista debe ser
  permeable a las sugerencias que formule.»**
- **«[el periodista] tiene que hacer partícipe de ello al cámara porque éste tiene la
  responsabilidad de transformarlo en imagen, incluido el imprevisto que pueda producirse.»**
- **«En el caso, habitual en el trabajo diario, de que no haya un realizador, el criterio del cámara
  es imprescindible para proponer soluciones a las diﬁcultades técnicas o, simplemente, para
  aportar ideas útiles para el discurso periodístico.»**

(Sirve también al tema 8.)

### 3.2 La grabación en exteriores: las cuatro condiciones mínimas (LE-CS 5.2, pp. 79-80)

**«Una grabación realizada en exteriores, para facilitar el posterior montaje y edición, se asienta
en cuatro condiciones mínimas.»**
1. **«Grabar las imágenes y los testimonios con un orden narrativo lógico, sea de manera
   cronológica o temática.»**
2. **«Captar la imagen prevista, según cada caso y circunstancia, con alternancia y asociaciones de
   planos que tengan un nexo común técnico, de situación o informativo.»**
3. **«Grabar el número suﬁciente de planos, sin desmesura, pero con la duración necesaria para
   facilitar la selección y el corte en la edición, y para crear un ritmo narrativo adecuado. La
   imagen que no ha sido grabada no se puede recuperar y, por tanto, es como si no existiera a
   cualquier efecto.»**
4. **«Rodar siempre planos de recurso para no tener que recurrir al archivo, salvo que sea
   inevitable para ampliar detalles con imágenes muy concretas de algún antecedente de la
   noticia.»**

Soporte y altura de cámara (enlaza con tema 4):
- **«En circunstancias normales, la cámara se instalará sobre el trípode para conseguir una imagen
  estable y de calidad, pero no hay que descartar su manejo al hombro aun cuando el foco de
  atención sea estático, sobre todo para captar recursos en una rueda de prensa o en una
  entrevista.»**
- **«El cámara, sin embargo, se abstendrá de usar su herramienta de trabajo como un instrumento
  desvinculado de la realidad para crear una estética de ﬁcción. Por ello eludirá encuadres,
  composiciones y perspectivas extravagantes, al menos en las coberturas habituales de los
  informativos diarios.»**
- **«Para mostrar la realidad al espectador, la cámara es sus ojos y sus oídos, por ello se colocará
  frontalmente a los hechos con la óptica a la altura de la teórica mirada del espectador.»**
- **«Las innovaciones que puedan llevarse a cabo en una grabación —barridos, doble foco, zoom
  rápido— tienen que responder a una intención previa para lograr una estética determinada,
  admisible sólo en determinados formatos informativos.»**

### 3.3 Cifras de una noticia tipo (LE-CS 5.3.1, p. 80) — dato preguntable

- **«Un vídeo de televisión convencional necesita entre veinte y veinticinco buenos planos
  diferentes y, generalmente, agrupados en tres o cuatro secuencias distintas, para obtener una
  edición correcta de un minuto.»**
- **«El equipo debe captar un total de entre cuatro y ocho minutos de imagen útiles, según las
  circunstancias y la previsión, para la elaboración de una noticia tipo de un minuto o algo más.»**
- Encuadre: **«El periodista y el reportero gráﬁco deben elegir para poner ante su mirada la
  realidad de la que ellos son testigos, lo que van a contar, dejando fuera del relato lo que no sea
  relevante.»**

### 3.4 El plano y los movimientos (LE-CS 5.3.2, pp. 80-81) — datos preguntables

- **«No se interrumpirá la grabación de un hecho mientras se mantenga la acción que se desarrolla
  en ese momento a ﬁn de facilitar la selección y el montaje posterior.»**
- **«Cuanto más personal e intimista sea el motivo sobre el que estamos trabajando, más cortos
  serán los planos y más abierto cuanto más coral sea la noticia y mayor el número de
  protagonistas»**.
- **«Cualquier movimiento de cámara (‘paneo’, ‘travelling’, ‘zoom’...) debe hacerse con prudencia y
  usarse con moderación. El zoom sólo se usará en circunstancias excepcionales, y con el único
  objeto de mostrar correctamente una noticia que lo necesite. Es un recurso muy poco natural
  porque el ojo humano no lo hace y, dentro de una información normal, no es adecuado.»**
- **«Ambos supuestos, sobre todo las panorámicas, comenzarán y ﬁnalizarán con un plano ﬁjo de
  suﬁciente duración —lo recomendable es, al menos, un margen de diez segundos— como para que
  pueda ser empleados por sí mismos e independientemente del movimiento, en la edición ﬁnal.»**
- **«es conveniente seguir registrando la imagen al menos durante cinco segundos después de recoger
  la imagen hasta pulsar ‘stop’. Es el margen que se precisa para el ‘preroll’ en una edición
  convencional.»** (Nota: «preroll» de edición en cinta; histórico.)
- **«La situación ideal es que la acción discurra ante un plano ﬁjo sin modiﬁcar el encuadre, pero
  eso ocurre siempre así.»** Ojo: el original dice «eso ocurre siempre así»; por el sentido falta un
  «no» (errata del libro). Si se cita, citar tal cual con [sic] o parafrasear.
  Sigue: **«Por tanto, es preferible un movimiento moderado de la cámara para centrarse en las
  imágenes verdaderamente atractivas, sin descuidar la grabación de recursos estáticos,
  fundamentales para el montaje.»**

### 3.5 Código de tiempo, luz, ganancia y comprobación (LE-CS 5.3.3, pp. 81-82)

- **«En cada grabación el código de tiempo es un acuerdo básico entre periodista y cámara,
  especialmente cuando van a estar físicamente separados durante la cobertura y cuando hay poco
  margen para la posterior elaboración del correspondiente vídeo.»** Opciones: **«un código de
  tiempo real previamente acotado»** o **«el TC poniendo el marcador a 00:00:00 al principio de la
  cinta. Esta referencia es generalmente mejor, sobre todo cuando el material va a ser usado por
  terceras personas.»**
- Luz: **«Siempre que sea posible, la grabación se efectuará con luz natural a la que se añadirá, si
  es necesario, el recurso de la antorcha para eliminar contraluces o sombras, pero sin ‘quemar’ la
  imagen por exceso de luz y proximidad.»**
- Ganancia: **«en algunas circunstancias forzar la ganancia no resta verosimilitud a la noticia e
  incluso incrementa su eﬁcacia. El ejemplo habitual para justiﬁcar este método es el de una redada
  nocturna.»**
- Histórico (cinta): **«registrar una sola noticia por cinta, después de un mínimo de treinta
  segundos de barras al principio de la misma. Si hay dos noticias en el mismo soporte deben
  separarse con un minuto de barras.»**
- Vigente como criterio: **«Otra norma elemental de prudencia es revisar la grabación en el mismo
  lugar de la misma para comprobar que es correcta desde la perspectiva de la imagen y del
  sonido.»**

### 3.6 Canales de sonido en ENG (LE-CS 5.4, p. 82) — dato preguntable (sirve también al tema 6)

- **«Como norma general, el sonido directo de declaraciones, ruedas de prensa o el del periodista
  ante cámara se registra por el canal 1. El canal 2 recoge el sonido ambiente, captado a través del
  micrófono de la cámara.»**
- **«Si las circunstancias lo permitan, el canal 1 se tomará de mesa de sonido sobre todo si éste es
  tan importante como la imagen: actuación musical, discurso político, ensayo general...»**
- **«El sonido ambiente tiene que ser registrado siempre y en cualquier circunstancia»**.
- Sonido como base (concierto, lemas de protesta): grabación específica **«incluso por los canales 1
  y 2 simultáneamente, en previsión de incluirlo en emisión como vídeo total»**.

### 3.7 Directo informativo: lo que CSRTV pide al equipo (LE-CS 8.3 y 8.3.2, pp. 116-117)

- **«La improvisación no tiene cabida como elemento de trabajo. Hasta donde sea posible, el equipo
  coordinado de producción, realización, enlaces e informativos debe prever todo lo que pueda
  planiﬁcarse, sin olvidar cualquier eventualidad: desde un aguacero hasta la interrupción del
  sonido de retorno.»**
- Mirada: **«Las apariciones en directo se harán mirando siempre directamente a cámara, que son los
  ojos del espectador, con el micrófono vertical, apoyando levemente sobre el esternón la mano que lo
  sujeta, sin que oculte el rostro y de modo relajado.»**
- **«En caso de que hagamos el directo desde un lugar especialmente habilitado para ello,
  generalmente en interiores, el micrófono puede ser de corbata»**.
- Encuadre del directo: **«El encuadre y el plano serán acordes con las circunstancias. En un recinto
  cerrado o sin referencias bastará un plano medio, pero lo abriremos si el fondo forma parte del
  propio mensaje o lo refuerza. Un enviado especial se colocará en un punto que permita al
  espectador reconocer sin diﬁcultad el lugar donde se encuentra y desde el que informa»**.
- **«Descartaremos siempre los emplazamientos que muestren con nitidez imágenes, nombres, anagramas
  o cualquier elemento que aporte connotaciones publicitarias o propagandísticas explícitas.»**
- 8.3.3: **«El uso de la modalidad de falso directo debe erradicarse.»** … **«Si el directo es falso,
  lo haremos constar.»**
- 8.3.4 (seguridad del equipo en localización, enlaza tema 14): **«Siempre usaremos casco en una obra
  de construcción, bata en un quirófano, en un laboratorio, y en cualquier otro lugar donde las
  condiciones de asepsia lo precisen.»**; y **«todos los miembros de un equipo de CSTV deberán usar,
  dentro y fuera del centro de producción, una indumentaria adecuada cuando el trabajo lo exija.»**

### 3.8 Retransmisiones en CSRTV (LE-CS 8.4, pp. 119-120)

- Ámbito: **«En las retransmisiones —generalmente deportivas, taurinas o de ﬁestas populares—
  seguiremos las mismas pautas que en el resto de la programación informativa: manda la imagen y
  la palabra debe adecuarse a ella.»**
- **«La mejor forma de evitarlo es utilizar el monitor con la imagen de programa como base de la
  narración con la seguridad de que es lo mismo que ve el espectador.»** (dirigido al narrador).
- Juicios de valor apoyados en **«las ventajas técnicas del medio (repeticiones, tomas diferentes,
  ralentizaciones...)»**.
- Fiestas populares citadas: **«(Semana Santa, Rocío, Santa María de la Cabeza, Ferias...)»**.
- El capítulo se dirige al narrador, **no** describe la operativa de cámara. La operativa de cámara
  en retransmisión (CCU, tally, intercom, retorno) va en 3.9 con fuente técnica.

### 3.9 Operativa de cámara en retransmisión y estudio: fuente técnica

No existe norma que regule «la operativa del cámara» en retransmisión: lo que sigue es fuente de
fabricante y norma de cable. Lo demás (seguir el intercom, anticipar el plano, no mover con piloto
rojo) es **costumbre de oficio** y el redactor debe decirlo así si lo incluye.

**a) Piloto (tally): verde anticipo, rojo aire** (ATEM, «Primeros pasos», manual líneas ~1017-1024):
- **«presione uno de lo botones correspondientes a una entrada a fin de seleccionarla como anticipo.
  Esto hará que la luz piloto en las cámaras compatibles de Blackmagic Design se encienda de color
  verde. Al presionar el botón CUT o AUTO, se producirá un corte o una transición para transmitir la
  fuente a través de la salida principal y por ende la luz piloto se encenderá de rojo, indicando así
  que la cámara está al aire.»**
  Salvedad: es el comportamiento de ese fabricante; el verde de anticipo no es universal. El rojo =
  al aire sí lo describe también el apartado GPI/Tally del mismo manual:
- **«Esta señal se utiliza generalmente para encender una luz roja sobre la cámara o el monitor, de
  forma que el operador sepa que está al aire.»** (ATEM, «Señalización mediante el dispositivo GPI and
  Tally Interface»).
- Llamada: **«Manteniendo presionado el botón CALL, la luz piloto de las cámaras conectadas comenzará
  a parpadear. Esta es una manera muy útil de llamar la atención de los camarógrafos»** (ATEM, «Botón
  de llamada»).

**b) Retorno de programa y control de cámara por el retorno SDI** (ATEM):
- **«El mezclador permite controlar unidades URSA Mini y Blackmagic Studio Camera mediante la señal
  SDI de retorno.»**
- PTZ: **«También es posible controlar cabezales PTZ mediante una conexión SDI. Esto puede lograrse
  conectando la señal de retorno del mezclador a una cámara, y luego la salida SDI del puerto de
  expansión de la cámara al cabezal.»** (apartado «Control PTZ mediante el protocolo VISCA»; sirve
  también al tema 4, sistemas remotos).
- N-1 (retorno sin la propia voz): **«Esta modalidad disponible en las salidas SDI permite silenciar el
  audio de una entrada específica en la señal de retorno. Por ejemplo, al realizar coberturas en
  directo, la demora en el audio de retorno podría provocar que el presentador se distraiga al
  escuchar su voz con retraso.»** (apartado «Ajustes del modo N-1»).
- Intercomunicación: **«Si la comunicación con los camarógrafos o los ingenieros se ha establecido con
  éxito, es posible ajustar el volumen de los auriculares.»**

**c) Cable de cámara de fibra híbrida: SMPTE 311-2009** (ST311):
- Título: **«Television — Hybrid Electrical and Fiber-Optic Camera Cable»**.
- Alcance (cl. 1): **«This standard describes the minimum performance for a hybrid cable containing
  single-mode optical fibers and electrical conductors to convey signal and control in a variety of
  environments where moisture, weather, and ozone resistance are required.»** … **«The cable
  described in this standard is intended to be used to interconnect cameras and base stations in
  conjunction with the connectors complying with SMPTE 304M»**.
- Fibras (cl. 5.1): **«There shall be two optical fibers.»** — monomodo.
- Conductores: **«There shall be two or more auxiliary conductors»** (cl. 6.1; configuraciones de 2, 4
  u 8) y **«There shall be two signal conductors»** (cl. 6.2).
- Nota: la «base station» es la CCU; que la CCU la maneje el control de cámaras/técnico de imagen
  está en el RTVE (informacion-grafica/08, «Quién ajusta qué»). SMPTE 304M (conector) no se ha leído:
  no citar su contenido.
- Triax: no se ha localizado norma abierta; no afirmar nada de él con cifras.

**d) Tally, retorno e intercom en la mochila** → ver 13.1 (LU800).

### 3.10 Entrevista grabada en unidad móvil (LE-CS 3.17.1.5, pp. 61-62)

- **«En caso de que la entrevista en exteriores sea grabada en una unidad móvil, tenderemos a la
  fórmula de falso directo (sin interrupciones) y sólo se manipulará el ‘master’ para corregir
  defectos técnicos de fácil resolución y que no modiﬁquen sustancialmente el mensaje ni el
  concepto estético de la propia entrevista.»**
- Con varias ENG: **«Si disponemos de dos o más cámaras ENG independientes, el realizador preverá que
  los planos respectivos sean técnicamente compatibles y uniformes. El código de tiempo que se
  aplicará será idéntico para facilitar el montaje ﬁnal.»**

---

## Tema 8 · Trabajo con redacción y realización

Hueco declarado: entrevistas y relación con redacción. LE-CS los cubre bien.

### 8.1 Planificación de cobertura (LE-CS 4.1 y 4.1.1, pp. 65-67)

- Tres conceptos que deben salir de la planificación: **«1. Decisión de cobertura.»** … **«Esta
  primera decisión sobre el trabajo debe conjugar el aspecto periodístico y las posibilidades
  técnicas. El equipo encargado de la información debe estar informado de cada decisión y de
  cualquier modiﬁcación posterior.»**; **«2. Material necesario.»**; **«3. Base de trabajo. Las
  decisiones tienen que ser ﬁrmes para que el equipo que va a la calle tenga una tesis periodística
  y televisiva perfectamente deﬁnida, una idea central para trabajar sobre ella y una previsión, al
  menos inicial, del formato en el que se va a plasmar su trabajo.»**
- Medios propios o contratados: **«La norma es que los asuntos surgidos desde las fuentes propias
  de los periodistas de CSTV no serán gestionados, en la medida de lo posible, por medios ajenos a
  la emisora.»**
- Convocatorias: **«Es nuestra obligación reclamar y obtener de la instancia que emite la noticia
  unas mínimas condiciones para la obtención de imágenes.»**
- **«La planiﬁcación básica de una cobertura en televisión debe contemplar estos elementos:»**
  1. **«Relación de imágenes y secuencias suﬁcientes para contar una historia con corrección y orden
     narrativo. Previsión de documentación complementaria.»**
  2. **«Escenarios y situaciones adecuados para captar imágenes vinculadas con la noticia»**…
  3. **«Personas a las que vamos a entrevistar para contar un hecho (protagonistas), que hagan una
     referencia del mismo (testigos), que opinen al respecto (expertos o peritos), o incluso que
     muestren tesis contrarias o de contraste.»**
  4. **«Equipo con los elementos técnicos precisos, decisión sobre aspectos informativos y estéticos
     de la grabación y necesidades posteriores, como elementos de postproducción, gráﬁcos, imágenes
     de archivo, etc...»**

### 8.2 Producción y comunicación del equipo desplazado (LE-CS 4.4, pp. 75-77)

- Productor responsable de **«la planiﬁcación y asignación ordenada de recursos para las grabaciones
  en exteriores y en plató, transmisiones y enlaces, intercambios y asistencias a otras
  televisiones»** … **«acreditaciones, permisos, transporte, alojamiento, dietas...»**.
- 4.4.1: **«Ante una eventualidad, los equipos desplazados tienen que comunicarse con productores y
  editores por si hay nuevas instrucciones o cambios sobre la planiﬁcación inicial.»**
- Puntualidad: **«Incumplir este requisito sin justiﬁcación es un acto de insolidaridad con quienes
  sí lo cumplen y una actitud indisciplinada que, además, pone en situación de riesgo la elaboración
  y emisión de un espacio informativo.»**
- 4.4.2 (ejemplo de orden de citación): **«Sería un error, por ejemplo, citar a un iluminador para
  una grabación a la misma hora que un cámara porque hasta que aquel no termine su tarea no se puede
  iniciar la siguiente fase del trabajo.»**
- LE-CS 5.6: **«Cualquier retraso en el trabajo que un equipo realice fuera del centro de producción
  debe ser comunicado a los editores para que tomen una decisión.»** … **«En la medida de lo
  posible, los equipos de trabajo se ajustarán a la planiﬁcación del noticiario.»**

### 8.3 Relación con realización (LE-CS 6.5, pp. 92-93)

- **«la realización es territorio profesional de los técnicos encargados de la misma y su criterio
  no puede soslayarse. Su cabeza visible, el realizador, es responsable máximo de la corrección de
  la imagen y de la calidad de la emisión del programa.»**
- 6.5.1 Delegación: **«El realizador actúa por delegación en profesionales que asumen funciones
  concretas y criterios particulares en cada fase de elaboración de la noticia.»** … **«su función
  se ciñe a la coordinación y supervisión de la parte ﬁnal del mismo.»**
- Prevalencia: **«cuando haya imperfecciones técnicas moderadas, la información —competencia del
  editor— tendrá preeminencia sobre la técnica —atribución del realizador—.»**
- 6.5.2: **«En la realización informativa, la urgencia acaba imponiéndose a cualquier otra
  consideración aunque no puede hacerlo hasta el punto de anular un aceptable nivel de calidad.»**

### 8.4 Toma de recursos (LE-CS 5.2 punto 4; 3.17.1.4)

- Ver 3.2 punto 4 (rodar siempre recursos).
- Entrevista: **«La entrevista, como sucede con la rueda de prensa, apenas aporta elementos para
  elaborar un vídeo aceptable. Esta carencia debe ser prevista y suplida mediante grabaciones
  especíﬁcas anteriores o posteriores, recopilación de archivo y, en cualquier caso, con la
  captación de recursos en el momento de la grabación: cambios de plano, movimientos de cámara,
  imagen de manos u objetos personales del entrevistado, primerísimos planos, imagen de escucha del
  entrevistador, etc.»**

### 8.5 Entrevistas: la norma de CSRTV (LE-CS 3.17 y 3.17.1, pp. 58-62) — núcleo de datos preguntables

- Doble perspectiva: **«1. Método de trabajo, generalmente fuera de plató, para extraer información y
  opiniones que después se integran en la edición con criterio informativo. 2. Formato en sí mismo,
  ya sea grabado fuera de los estudios para su posterior emisión o elaboración, o bien como directo
  en plató.»**
- Condiciones (3.17.1): **«en un ambiente adecuado, con luz suﬁciente preferiblemente natural,
  cámara apoyada sobre trípode y micrófono de corbata para quien nos habla.»** Material:
  **«auriculares, antorcha, equipo básico de iluminación, ﬁltros, micrófonos...»**
- Plano (3.17.1.1): **«Como norma, plano medio o primer plano en interiores, y plano americano en
  exteriores, especialmente cuando el fondo tenga carácter informativo suﬁciente.»**
  **«Es necesario prever la inclusión de rótulos, al menos en una ocasión, muy especialmente cuando
  registremos primeros planos.»**
  **«El plano será más largo cuanta más importancia tenga el emplazamiento y más corto cuanto más
  importante sea el personaje, más denso su testimonio o la carga emocional que lo acompañe.»**
  **«Si está previsto que en el montaje ﬁnal vayan a utilizarse varias respuestas, es conveniente
  variar el plano e incluso el encuadre al menos una vez durante la grabación.»**
  Ejemplo: **«entrevistemos al profesor dentro del aula, al agricultor en el campo y al investigador
  en su laboratorio»**.
- Fondos (3.17.1.2): **«eludiremos los fondos tópicos o vacuos (escribanías, banderas, fotos
  oﬁciales, mesas, pantallas de ordenador...) y descartaremos aquellos que tengan carácter
  publicitario o comercial»** … **«El fondo tenderá a la neutralidad cuando sea superﬂuo y, si es
  necesario en estos casos, se dejará fuera de foco.»** **«Como norma general, el personaje
  aparecerá levemente a la izquierda del encuadre.»**
- Mirada (3.17.1.3): **«El entrevistado nunca puede mirar directamente a la cámara, salvo en
  circunstancias excepcionales que deben ser autorizadas por la Dirección de los Servicios
  Informativos, o en los casos establecidos: el Rey o el presidente de la Junta de Andalucía en
  discursos institucionales.»**
  Posición del periodista: **«El periodista se ubicará frente a él, al lado de la cámara —con los
  ojos a la altura del objetivo, o sólo unos centímetros por debajo, y a la derecha de la misma—
  para que el personaje lo mire directamente»**.
  **«el periodista no se colocará al lado del personaje, a quien no permitiremos que sujete el
  micrófono de mano»**.
  Nota de coherencia (mía): personaje «levemente a la izquierda» + periodista «a la derecha» de la
  cámara → la mirada cruza hacia la derecha del cuadro, con aire delante. El libro no lo explica así;
  es deducción, no cita.
- Duración del total (3.17.1.4): **«repetiremos la pregunta hasta lograr una frase cerrada, breve y
  completa, de entre diez y quince segundos.»** **«no accederemos, en circunstancias cotidianas, a
  que revise la grabación.»**
- Una sola cámara (3.17.1.5): **«Es habitual que este formato se grabe con un sola cámara centrada en
  el personaje, con el plano que determine el realizador, que dirige el aspecto técnico y estético.
  En este caso habrá que hacer un segundo recorrido para grabar las preguntas del entrevistador con
  un plano idéntico, planos de escucha de uno y otro, además de los imprescindibles recursos para la
  edición posterior.»**
- Varias ENG y UM: ver 3.10.

### 8.6 Directos: coordinación (LE-CS 8.3)

Ver 3.7. Además (8.3.2): **«Terminado el directo, en la despedida sólo habla el presentador.»**

---

## Tema 10 · Cobertura de noticias, deportes, actos institucionales, cultura, sucesos y eventos no controlados

Hueco declarado: cultura y sucesos poco; eventos no controlados.

### 10.1 Rueda de prensa y actos convocados (LE-CS 4.2 y 5.5, pp. 67-68 y 83-84)

- **«una rueda de prensa no es noticia en sí misma, ni tampoco lo es la relación protocolaria de los
  asistentes a un acto, ni el orden del día o un catálogo de intenciones. Esta es la razón por la
  que hay que buscar siempre vías alternativas, tanto técnicas como periodísticas, para ofrecer la
  noticia correctamente.»**
- **«El equipo acudirá a cada convocatoria muy atento a cualquier novedad, dispuesto cuando sea
  conveniente a ‘dar la vuelta’ a la información»** … **«Lo imprevisto suele ser, casi siempre, más
  noticioso que lo que está preparado.»**
- Tres opciones ante la rueda de prensa pobre en imagen (5.5): **«1. Informarnos previamente del
  contenido de la rueda de prensa y pactar con quien la convoque una grabación especíﬁca, en un
  escenario adecuado»** … **«2. Planiﬁcar la elaboración, en paralelo, de un vídeo complementario, a
  modo de informe»** … **«3. En caso de que no sea posible aplicar ninguna de las opciones
  anteriores, acudiremos a la rueda de prensa o al acto convocado y, posteriormente, registraremos
  las imágenes complementarias adecuadas o recurriremos al archivo para completar el vídeo.»**
- «Efecto Heisenberg» (5.5): **«una cámara de televisión provoca, muchas veces, la aparición de
  determinadas actitudes que no se producirían en su ausencia o bien altera el curso normal de los
  acontecimientos.»** (útil para manifestaciones y eventos convocados para la cámara).

### 10.2 Deportes (LE-CS 7.5.4, pp. 109-110; 8.4)

LE-CS 7.5.4 es de tratamiento verbal (forofismo, estereotipos, violencia). Para cámara, lo aprovechable:
- **«Las actitudes delictivas de grupos o individuos serán denunciadas con la mayor determinación y
  detalle, basándonos en fuentes ﬁables»**.
- Retransmisión: ver 3.8 (repeticiones, tomas diferentes, ralentizaciones al servicio del juicio
  ecuánime). No hay en LE-CS nada sobre posiciones de cámara en deporte.

### 10.3 Cultura y fiestas populares

- Sonido en actuaciones (LE-CS 5.4): canal 1 **«de mesa de sonido sobre todo si éste es tan
  importante como la imagen: actuación musical, discurso político, ensayo general...»**; ambiente
  **«incluso aquellas en las que su ausencia sea casi absoluta (una exposición, el interior de un
  museo)»**; grabación específica cuando **«el sonido sea la base estética y/o noticiosa de una
  información, caso de una actuación musical»**.
- Fiestas populares (LE-CS 8.4.2): **«Idéntica moderación se requiere de las retransmisiones de
  ﬁestas populares (Semana Santa, Rocío, Santa María de la Cabeza, Ferias...)»** … **«habrá quien en
  un paso de palio sólo vea el carácter religioso y espiritual, quien se centre en su valor
  artístico, el que aprecie lo que tiene de armonía y estética o quien simplemente lo considere una
  actividad social extraordinaria.»**
- Taurinas (8.4.2): **«en las retransmisiones taurinas puede admitirse un mayor apoyo de la
  palabra»** (verbal).
- LE-CS no tiene sección de «Cultura»; 7.3 Sociedad trata educación, sanidad, ciencia, consumo y
  medio ambiente (texto, no cámara). **No hay** norma CSRTV sobre grabación en teatros, conciertos o
  museos (derechos, luz de sala). Declarar como hueco.

### 10.4 Sucesos y víctimas (LE-CS 9.9, pp. 165-167) — lo más preguntable para cámara

- Límite: **«nunca ofreceremos planos cortos y nítidos del rostro de una persona muerta o que se
  encuentre gravemente herida, agonizante o presa de una tensión psicológica extrema.»**
- **«Ofrecer un cadáver desmembrado en un plano corto o demasiado explícito no es información
  estricta, es sensacionalismo»**.
- **«La imagen de menores de edad, de víctimas de un delito, de testigos protegidos o de miembros de
  las fuerzas de seguridad y su familia no se emitirán si existe un factor de riesgo. Sus rostros
  serán cubiertos o tramados y no se aportarán detalles sobre su identidad o paradero.»**
- Cámara oculta: **«Canal Sur TV y Canal 2 Andalucía no emitirán imágenes grabadas por medios ilegales
  o conseguidas mediante cualquier ardid (cámara oculta, suplantación de personalidad, engaño...).
  Su emisión o los medios para conseguirlas sólo está justiﬁcada, con autorización previa de la
  Dirección de Informativos, en casos de auténtico interés público»**.
- Dirigido expresamente a los cámaras (9.9.1): **«los cámaras de Canal Sur TV o Canal 2 Andalucía no
  asediarán con una cercanía desmesurada a las víctimas de delitos, accidentes de tráﬁco, hechos
  cruentos, catástrofes naturales o circunstancias dramáticas»**.
- 9.9.2 «Selección de imagen»: **«el cámara está obligado a captar los hechos, con prudencia, con
  cierta distancia física y profesional, y en cualquier circunstancia, especialmente cuando se
  desarrollen de manera fugaz. En este caso, sin restringir la libertad para trabajar, es
  preferible registrar imágenes en las que no se vea un primer plano del rostro o que los heridos
  yazcan de manera que no se les pueda identiﬁcar.»**
- **«En el proceso posterior de selección y edición recae la responsabilidad de elegir la imagen que
  aporte contenido sin incidir desmesuradamente en la ﬁgura de las víctimas o en aspectos
  escabrosos.»**
- Archivo: **«En rotulación debe hacerse constar claramente que es material de ‘Archivo’ durante todo
  el tiempo en que la imagen permanezca en pantalla»**.
- Edición: **«las posibilidades de edición (ralentización, imagen congelada...) pueden generar un
  efecto reprobable y no debemos optar por ello si sólo sirve para acentuar la morbosidad de una
  historia.»**
- (Menores, víctimas, privacidad en profundidad → tema 12; aquí sólo lo operativo.)

### 10.4 bis Judicial, manifestaciones, reconstrucciones (LE-CS)

- Judicial (9.5.2 «Omisiones»): **«Las víctimas de un delito tampoco serán citadas o identiﬁcadas, ni
  mostraremos imágenes o sonidos que contribuyan a ello. La exigencia es inexcusable con los menores,
  sobre todo en actos contra la libertad sexual, salvo que la propia víctima, ya adulta, decida hacer
  públicos los hechos y sus circunstancias.»**
- Manifestaciones (4.3.2.1): cifra propia de asistentes **«a razón de dos, tres ó cuatro personas por
  cada metro cuadrado, según cada caso y grado de concentración»** (dato periodístico, útil para
  saber qué planos generales pedirá la redacción: superficie ocupada).
- Reconstrucciones de sucesos (9.2.12.3): **«cuando el recurso de un montaje de ﬁcción sea
  inevitable, es obligatorio que, durante todo el tiempo de aparición de las imágenes en pantalla,
  ﬁgure el rótulo ‘Reconstrucción’.»**; alternativa: **«podemos usar una imagen subjetiva de cámara
  para reconstruir los hechos a través de sus escenarios, sin la referencia principal de ningún
  personaje o actor.»**
- Estética en sucesos (9.2.12.4): **«La imagen oscilante ‘cámara en mano’, una música tópica, un
  virado a blanco y negro... evocan inevitablemente escenas ﬁcticias de misterio, terror... o de una
  película. Y la información sólo habla de realidad.»**
- Protocolo del CGPJ (grabación en sedes judiciales) disponible en
  `fuentes/informacion/CGPJ_protocolo-comunicacion-2020.txt`; no leído en esta pasada porque el RTVE
  ya cubre lo judicial.

### 10.5 Eventos no controlados y situaciones extremas (LE-CS 5.6, p. 85)

- **«ninguna información vale una vida, ni siquiera ponerla en peligro. La profesión, a veces, tiene
  riesgos, pero las actitudes temerarias nunca son recomendables: un periodista no es mejor porque
  se arriesgue, sino porque vuelve y lo cuenta.»**
- Situaciones: **«incendios, accidentes graves en lugares de difícil acceso o situaciones
  meteorológicas adversas»**.
- **«Un material estropeado, extraviado o sustraído no puede ser una excusa ante los espectadores
  para no dar una información o hacerlo deﬁcientemente.»** … **«la Redacción está obligada a
  encontrar una alternativa inmediata»**.
- Heridos y hechos fugaces: ver 9.9.2 arriba.
- Protestas: grabar el sonido de **«los lemas y gritos de una protesta»** como parte del discurso
  (5.4).

---

## Tema 13 · Producción móvil y transmisión: mochilas, enlaces, streaming, señales IP y coordinación con control

Hueco declarado: señales IP (ST 2110, SRT, NDI) y coordinación con control.

### 13.1 Coordinación con control desde la mochila (LU800, ficha del fabricante)

Funciones que el fabricante declara (documentación de fabricante: cita con fecha, puede cambiar):
- **«LiveU’s Tally Light enables field reporters and camera operators to know instantly when they’re
  live on air.»**
- **«LiveU Video Return enables field crews to see current program feeds and/or receive teleprompting
  information during live sessions.»**
- **«LiveU Audio Connect offers high-quality and reliable cloud-based audio solutions, enabling news
  anchors and producers in the station to communicate easily with camera operators and talents in
  the field.»**
- **«LiveU IP Pipe lets you gain remote control over a wide variety of network-based equipment,
  including robotic and PTZ cameras, Camera Control Units (CCUs), and IP-based intercom.»**
- Capacidad: **«The LU800 bonds up to 14 connections with up to eight 5G/4G internal dual SIM modems;
  supporting up to 60Mbps, based on LiveU’s award-winning, patented HEVC technology.»**;
  **«up to 4Kp60 10-bit HDR transmission»**, **«up to 16 audio channels»**; **«Up to four
  high-res, fully frame-synced feeds from a single portable unit»** (licencia PRO2/PRO4).
- Producción remota: **«producing multi-camera live events from a centralized studio control room
  instead of on-site production and satellite trucks.»**
- Nota: no consta en documento publicado qué modelo de mochila usa CSRTV.

### 13.2 Coordinación en directo según CSRTV (LE-CS 8.3)

Ver 3.7: **«el equipo coordinado de producción, realización, enlaces e informativos»**; eventualidad
**«la interrupción del sonido de retorno»**.

### 13.3 SMPTE ST 2110: qué parte cubre qué (ST2110-IDX)

Títulos oficiales (índice SMPTE): **ST 2110-10** «System Timing and Definitions»; **ST 2110-20**
«Uncompressed Active Video»; **ST 2110-21** «Traffic Shaping and Delivery Timing for Video»;
**ST 2110-22** «Constant Bit-Rate Compressed Video»; **ST 2110-30** «PCM Digital Audio»;
**ST 2110-31** «AES3 Transparent Transport»; **ST 2110-40** «SMPTE ST 291-1 Ancillary Data»;
**ST 2110-41** «Fast Metadata Framework»; **ST 2110-43** «Timed Text Markup Language for Captions and
Subtitles». Título común: **«Professional Media Over Managed IP Networks»**. **No existe
«ST 2110-50»**.
Idea clave (del propio índice): vídeo, audio y datos viajan como **flujos separados** (esencias) —
confirmar redacción en fuente web, ver 13.4.

### 13.4 ST 2110: texto de la norma (ST2110-10, -20, -30)

- Introducción de ST 2110-10:2022 (informativa): **«The capability and capacity of IP networking
  equipment has improved steadily, enabling the use of IP switching and routing technology to
  transport and switch video, audio, and metadata essence within television facilities. This new work
  encapsulates each production element separately into IP.»** → la idea examinable: **cada esencia
  (vídeo, audio, datos) va por separado**.
- Base: **«This family of SMPTE standards builds on the work of VSF TR-03 and TR-04, and of AES67»**.
- Gestión de conexiones: **«The AMWA has developed an interface specification, AMWA IS-05, for
  managing connections of the streams defined in this standard.»**
- Alcance ST 2110-10 (cl. 1): **«This standard is part of a family of engineering documents that
  define an extensible system of RTP-based essence streams referenced to a common reference clock, in
  a manner which specifies their timing relationships.»** **«This standard specifies the system timing
  model and the requirements common to all of the essence streams, and defines timestamping methods
  for video streams and audio streams such that time alignment across essence is possible.»**
- Reloj (PTP): **«A Common Reference Clock, potentially derived from a traceable time source, should
  be provided and distributed on the network using IEEE Std 1588-2008 Precision Time Protocol
  (PTP).»** y **«All Devices conforming to this standard shall support a Common Reference Clock
  delivered via IEEE Std 1588-2008 using any message rates allowed by the SMPTE ST 2059-2 PTP
  Profile.»** (apartado «Distribution of the Common Reference Clock via PTP»). Ojo «should» (debería)
  para proveer el reloj vs «shall» (deberá) para soportarlo — error 4 del encargo.
- Referencias normativas citadas en ST 2110-10: **«SMPTE ST 2059-2:2021 SMPTE Profile for Use of
  IEEE-1588 Precision Time Protocol in Professional Broadcast Applications»**; **«SMPTE ST 2022-7:2019
  Seamless Protection Switching of SMPTE ST 2022 IP Datagrams»**. (Incongruencia de la propia norma:
  en el cuerpo cita «SMPTE ST 2059-2:2020»; en la biblioteca SMPTE la edición publicada figura con
  fecha 09-12-2020. No dar año de la 2059-2 en el tema.)
- Redundancia (cl. 8.5): **«Duplicate RTP streams meeting the requirements of SMPTE ST 2022-7 may be
  used for redundant transmission to achieve higher system availability.»**
- Tamaño UDP (cl. 6.3): **«The Standard UDP Size Limit shall be 1460 octets.»** (dato fino; sólo si el
  tema baja a ese nivel).
- ST 2110-20:2022 alcance: **«This standard specifies the real-time, RTP-based transport of
  uncompressed active video essence over IP networks. An SDP-based signaling method is defined for
  image technical metadata necessary to receive and interpret the stream.»**
- ST 2110-30:2025 alcance: **«This standard specifies the real-time, RTP-based transport of PCM
  digital audio streams over IP networks by reference to AES67.»** … **«Non-PCM digital audio signals
  including compressed audio signals are outside the scope of this standard.»** (ojo: la edición
  vigente es **2025**, no la de 2017).

### 13.5 NMOS (AMWA) — control y descubrimiento en redes ST 2110 (NMOS, extractor)

- **«NMOS is a family name for specifications produced by the Advanced Media Workflow Association
  related to networked media for professional applications.»**
- **IS-04 «Discovery & Registration»**; **IS-05 «Device Connection Management»**; **IS-07 «Event &
  Tally»**; **IS-08 «Audio Channel Mapping»**. (IS-07 = tally sobre IP: enlaza con coordinación con
  control.)

### 13.6 SRT (SRT-ID, SRT-GH, SRT-AL; extractor)

- Nombre: **«SRT (Secure Reliable Transport)»** (SRT-AL). Creado y liberado por Haivision; código en
  `github.com/Haivision/srt`, licencia **MPL-2.0** (SRT-GH).
- README: **«Secure Reliable Transport (SRT) is a transport protocol for ultra low (sub-second)
  latency live video and audio streaming, as well as for generic bulk data transfer.»**
- Draft IETF, resumen: **«SRT is a user-level protocol over User Datagram Protocol and provides
  reliability and security optimized for low latency live video streaming, as well as generic bulk
  data transfer.»**; **«SRT packets are transmitted as UDP payload»** (sec. 3).
- Recuperación de pérdidas: **«Automatic Repeat Request (ARQ), packet acknowledgments, end-to-end
  latency management»** (sec. 1.1); latencia constante mediante *Timestamp-Based Packet Delivery*
  (TSBPD, sec. 4.5).
- Modos: **«Like TCP, SRT employs a listener/caller model»** (sec. 1.2); además *rendezvous*
  (sec. 4.3.2).
- Cifrado: AES de **128, 192 y 256 bits** (draft, tabla 2; SRT-GH `SRTO_PBKEYLEN` 16/24/32).
  Contraseña `SRTO_PASSPHRASE` de **10 a 80** caracteres.
- Latencia por defecto: `SRTO_LATENCY` **120 ms** (tabla de opciones; con asterisco: el valor por
  defecto de recepción cambia según `SRTO_TRANSTYPE`).
- **Estatus**: SRT **no es norma** de la IETF: el draft está **expirado**, *Independent Submission*,
  *Informational*, y el propio documento dice no estar respaldado por la IETF. Decirlo como
  «protocolo abierto», nunca «norma» ni «RFC».

### 13.7 NDI (NDI-DOC; extractor)

- **«NDI stands for Network Device Interface.»** **«It is a widely adopted video connectivity standard
  based on proprietary IP networking specifications.»** (es propietario: «standard» en su sentido
  comercial, no de organismo de normalización).
- **«NDI is not a codec»**; admite códecs, entre ellos **«our proprietary SpeedHQ»**; NDI HX usa
  **«AVC (H.264) and HEVC (H.265)»**.
- Descubrimiento: **«NDI offers two different options for a zero-configuration discovery and
  registration: mDNS and Discovery Service.»**
- Puertos: **5353/UDP** mDNS; **5959/TCP** Discovery Server (**«beneficial in large configurations when
  you need to connect NDI devices between subnets or if mDNS is blocked»**); **5960/TCP** consulta de
  fuentes; **5961+/TCP** un puerto por flujo.
- No consta en documento publicado que CSRTV use NDI, SRT o ST 2110 en sus instalaciones.

### 13.8 Contraste para el tema (nota mía, cada rasgo con su fuente arriba)

| | ST 2110 | SRT | NDI |
|---|---|---|---|
| Quién lo publica | SMPTE (norma) | Haivision / SRT Alliance (código abierto; draft IETF expirado) | Vizrt/NDI (especificación propietaria) |
| Ámbito | red gestionada de la instalación (**«Managed IP Networks»**) | redes no garantizadas / internet (**«unpredictable networks»**, SRT-AL) | red local de producción |
| Compresión | -20 sin comprimir; -22 comprimido CBR | transporta lo que se le dé (contribución) | SpeedHQ / H.264 / HEVC |
| Sincronía | PTP (IEEE 1588, perfil ST 2059-2) | latencia constante TSBPD | — (no leído) |
La fila «Ámbito» de NDI («red local») es inferencia de mDNS en red local, no cita: el redactor debe
formularla con cautela o quitarla.

---

## Tema 4 · Soportes y accesorios

RTVE cubre el 90 %. Lo propio de CSRTV que consta:
- LE-CS 5.2: trípode en circunstancias normales; hombro no descartado para recursos en rueda de
  prensa o entrevista (cita literal en 3.2).
- LE-CS 3.17.1: entrevista **«cámara apoyada sobre trípode»**; material **«auriculares, antorcha,
  equipo básico de iluminación, ﬁltros, micrófonos...»**.
- «steady»: **Steadicam es marca registrada de Tiffen** (TIFFEN, extractor: «Steadicam® revolutionized
  film making with its debut in "Bound for Glory"»). La página **no** da inventor ni año: no afirmar
  Garrett Brown/1975 sin otra fuente.
- **Slider (hueco real: ningún tema RTVE lo desarrolla; grep «slider» sin resultado)**. MVS060A
  (extractor): **«a sturdy yet lightweight, extremely portable solution»**, se monta **en trípodes o
  sobre el suelo / superficie nivelada**; 60 cm; carga **«10 kg safety payload»**; peso 2,19 kg;
  **«fully machined anodized aluminium; high precision steel ball bearings»**; **burbuja de nivel y
  control de fricción**. Es un ejemplo de producto, no una norma: usarlo como ilustración.
- Sistemas remotos: control PTZ por retorno SDI/VISCA (ATEM, ver 3.9 b); control remoto de PTZ y
  CCU a través de la mochila (**«LiveU IP Pipe»**, ver 13.1).

---

## Lo que no se ha podido confirmar (no usar sin fuente)

- Qué equipos usa CSRTV (modelos de cámara, mochila, UM, si su red es ST 2110/NDI/SRT): **no consta
  en documento publicado** leído.
- Norma o manual publicado de CSRTV sobre operativa de cámaras, UM o transmisiones: no localizado.
  Lo propio de CSRTV se limita a LE-CS (2004).
- Inventor/año de la Steadicam: la página de Tiffen no lo da.
- Triax (cable de cámara coaxial triaxial): sin norma abierta leída; no dar cifras.
- SMPTE 304M (conector híbrido) y ST 2059-2 (perfil PTP): no leídos; sólo se sabe su título por la
  lista de referencias de ST 2110-10 (2059-2) y por el alcance de ST 311 (304M).
- ST 2110-22 (vídeo comprimido CBR) y ST 2110-21: sólo título (índice SMPTE).
- Latencia típica de NDI y de una mochila: no hay cifra de fuente; la LU800 sólo dice «lowest
  latency» (reclamo comercial). No inventar milisegundos.
- Cobertura cultural (teatros, conciertos, museos: permisos, luz de sala, derechos): LE-CS no tiene
  norma de cámara; queda como hueco del tema 10 o se cubre con el tema 12 (derechos de imagen).
- Tally con verde para anticipo: sólo documentado en Blackmagic; no generalizar.

## Ficheros tocados en esta fase

- Escrito: `informes/canal-sur-especificos/08-investigacion-B-captacion.md` (este).
- Añadidos a `fuentes/normas-tecnicas/` (descargados de `pub.smpte.org`, biblioteca abierta, el
  24-09-2026): `SMPTE_ST-2110-10-2022.pdf/.txt`, `SMPTE_ST-2110-20-2022.pdf/.txt`,
  `SMPTE_ST-2110-30-2025.pdf/.txt`, `SMPTE_ST-311-2009.pdf/.txt`. El README de esa carpeta **no** se
  ha actualizado (queda para quien lo mantenga).
