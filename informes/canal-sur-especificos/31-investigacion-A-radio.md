# Puesto 31 · Presentador Productor de Radio · Investigación del bloque A-radio (temas 1, 2, 3, 4, 5, 6, 8, 16)

Fase 1 · Investigar. El encargo fija «hoy» en 24-09-2026; las descargas web de este informe se
hicieron con el reloj del sistema a **03-10-2026** y así se declara en cada fuente. Para lo que
cambia con el tiempo (EGM, medidor digital) se ha comprobado que lo dicho ya era así el
24-09-2026 o se avisa de lo contrario.

Método: sólo lo que falta. Lo ya cerrado en Redactor/a (34), Operador/a de Sonido (28), en el común
de Canal Sur y en los temas de RTVE señalados por el coordinador **no se repite aquí**: se indica
dónde está y qué hueco deja.

## Fuentes nuevas y fecha de lectura

Todas guardadas en `fuentes/canal-sur/radio/` (carpeta nueva; declarada como fichero tocado).

| Clave | Documento | Fichero | Leído |
|---|---|---|---|
| **NR-AIMC** | AIMC, *Normas de radio en EGM* (documento con fechas internas 2005-2019; la última nota, «AIMC 24/07/2019») | `aimc-normas-radio-egm.pdf/.txt` | 03-10-2026 |
| **MG26** | AIMC, *Marco General de los Medios en España 2026* (datos de 2025), febrero 2026 | `aimc-marco-general-medios-2026.pdf/.txt` | 03-10-2026 (tablas leídas sobre la imagen de las págs. 29, 30, 33 y 35 del PDF; el .txt desordena las tablas) |
| **AIMC-web** | aimc.es, páginas «¿Qué es el EGM?»: características técnicas, universo y muestra, trabajo de campo, cuestionario, fusión, equilibraje, entrega de resultados, márgenes de error, radio streaming, calendario 2026, ficha técnica 1.ª ola 2026, usos | `aimc-web-*.txt` | 03-10-2026 |
| **AIMC-NP** | AIMC, comunicados de 08-10-2025 (Comisión de Seguimiento), 10-07-2026 (Comscore) y 01-09-2026 (situación del concurso) | `aimc-comunicado-2025-10-*.pdf`, `aimc-np-2026-07-10-comscore.pdf`, `aimc-np-2026-09-01-situacion-concurso.pdf` (+ .txt) | 03-10-2026 |
| **IAB-POD** | IAB Tech Lab, *Podcast Measurement Technical Guidelines* v2.2 (© 2024) | `iabtechlab-podcast-measurement-v2.2.pdf/.txt` | 03-10-2026 |
| **LV** | José Ignacio López Vigil, *Manual urgente para radialistas apasionados y apasionadas*, ed. PDF (Quito), ISBN 9978-55-045-3, introducción fechada «Lima, abril 2005». **Copyleft**: «Se autoriza toda copia y distribución siempre que sea citando la fuente, respetando la integridad del texto y sin fines de lucro.» Copia de Internet Archive (colección «manualradioslibres») | `lopez-vigil-manual-urgente-radialistas.pdf/.txt` | 03-10-2026 |
| **UNLP** | Universidad Nacional de La Plata, Fac. de Periodismo, cátedra Narrativas Radiales, «Trabajo Práctico Nº4 El Lenguaje Radiofónico» (10-03-2021); cita literal la definición de Balsebre | `unlp-narrativas-radiales-tp4-lenguaje-radiofonico.txt` | 03-10-2026 |
| **CS-web** | canalsur.es/radio (portada de radio) | `canalsur-web-radio-2026-10-03.txt` | 03-10-2026 |

Fuentes ya existentes en el proyecto, leídas para este bloque:

| Clave | Documento | Fichero | Leído |
|---|---|---|---|
| **CSP** | Carta del Servicio Público de la RTVA 2024-2029 (BOJA núm. 247, de 28-12-2023) | `fuentes/canal-sur/documentos/carta-servicio-publico-2024-2029-boja-247-2023.txt` | 03-10-2026 |
| **CP** | Contrato-programa Junta-RTVA 2024-2026 (BOJA núm. 245, de 2023) | `fuentes/canal-sur/documentos/contrato-programa-2024-2026-boja-245-2023.txt` | 03-10-2026 |
| **ME-RTVE** | Manual de estilo de RTVE, cap. 1 (CRTVE, 1.1.5) y cap. 7 (Anexos, 7.5 «Glosario de términos utilizados en el lenguaje radiofónico») | `fuentes/informacion/RTVE_manual-de-estilo_crtve.txt`, `..._anexos.txt` (volcado 02-09-2026) | 03-10-2026; **el glosario 7.5 se cotejó con la web viva (manualdeestilo.rtve.es/anexos/) el 03-10-2026: coincide** |
| **LO 1/1982** | Ley Orgánica 1/1982, de protección civil del honor, intimidad y propia imagen | `fuentes/canal-sur/BOE-A-1982-11196.md` (vía `boe.py precepto`) | 03-10-2026 |

### Advertencias generales para el redactor

1. **No hay libro de estilo publicado de Canal Sur Radio** (ya declarado en Redactor/a 08). El Libro de
   estilo de Canal Sur (2004) es de televisión. Lo radiofónico descansa en ME-RTVE (referencia de oficio,
   no norma de Canal Sur), en LV (manual de oficio) y en AIMC (que sí es la fuente oficial de audiencia).
2. **LV es latinoamericano, de radio comunitaria y con opiniones políticas explícitas** (p. ej. sobre
   agencias de noticias, Sharon, Bush). Usarlo **sólo** en sus pasajes técnicos (géneros/formatos,
   radiorrevista, debate, entrevista, programación, música y efectos). Su terminología no siempre es la
   española: «libreto» = guion; «radiorevista» = magazine; «cuña» coincide; «cortina» ≈ ráfaga/cortinilla.
   Se cita como «costumbre de oficio recogida en un manual», nunca como norma.
3. **Choque de criterio sobre el silencio** (útil para pregunta): ME-RTVE 3.1 cuenta el silencio entre los
   elementos sonoros; Balsebre (vía UNLP) también; LV sostiene que no es «una cuarta voz» sino ritmo y
   puntuación. Presentarlo como dos posturas.
4. **El *share* en radio no se define como en televisión.** El tema de RTVE (gestion/27) define el *share*
   como porcentaje «respecto de los que están viendo la televisión». En el EGM de radio, el *share*
   («Participación») se calcula sobre la **audiencia media del total medio** y con **bases distintas**
   (Total Generalista, Total Temática, Total Oyentes). Y la «fidelidad» de RTVE («cuánto del programa ve
   quien lo ve») no es el **índice de fidelidad** de AIMC (audiencia media / audiencia acumulada). Si se
   copia gestion/27, hay que corregir o acotar esos dos puntos al pasar a radio.
5. **gestion/27 de RTVE declara su propio párrafo de medición como no contrastado** («Kantar Media… y la
   AIMC… se dan como descripción del sector… no como cita de una fuente contrastada»). Para radio, lo de
   AIMC ya queda contrastado aquí; lo de Kantar (televisión) no se ha verificado en este bloque.

---

## Tema 1 · Lenguaje radiofónico: palabra, música, silencio, efectos, ritmo, continuidad y narrativa sonora

**Ya cerrado** (copiar literal): Redactor/a 08, epígrafe 1 (fugacidad; «La voz, la música, los efectos y
el silencio son los elementos sonoros que determinan la capacidad expresiva»; tono comunicativo).
Sonido 09 (28) «La continuidad: que todo suene igual» y «Las piezas de continuidad». RTVE sonido/12 lo
que distingue el sonido de radio.

**Falta**: definición académica de lenguaje radiofónico; funciones de cada elemento; silencio
(bache/pausa); efectos (descriptivos/narrativos); música (cortina, ráfaga, puente, fondo, golpe,
leitmotiv, ambientación); planos sonoros; ritmo; glosario de continuidad (sintonía, careta, cortinilla,
indicativo, punto).

### 1.1 Definición (Balsebre, vía UNLP)

- UNLP cita literal a Armand Balsebre (*El lenguaje radiofónico*; la UNLP no da editorial ni año en la
  cita): «Lenguaje radiofónico es el conjunto de formas sonoras y no­sonoras representadas por los
  sistemas expresivos de la palabra, la música, los efectos sonoros y el silencio, cuya significación
  viene determinada por el conjunto de los recursos técnico-expresivos de la reproducción sonora y el
  conjunto de factores que caracterizan el proceso de percepción sonora e imaginativo-visual de los
  radio­yentes».
- UNLP (texto propio de la cátedra): «Cuando en radio hablamos de sonidos estamos aludiendo a la voz
  hecha palabra, a la música y a los efectos sonoros, y -por contraposición- a la ausencia de sonido o
  silencio. Estos cuatro elementos constituyen la base del lenguaje radiofónico.»
- Balsebre (vía UNLP), sobre la estética: «La información estética de un mensaje es portadora de un
  segundo nivel de significación, connotativo, afectivo, cargado de valores emocionales o sensoriales».
- **No confirmado**: año y editorial de Balsebre (búsqueda web: Cátedra, Madrid, 1994 — no leído en
  fuente primaria; no afirmarlo o decir «según la cita de la UNLP»).

### 1.2 Las «tres voces» y la función de cada una (LV, cap. 3, «La triple voz de la radio»)

- «La radio es sólo sonido, sólo voz. Pero una voz triple: La voz humana, expresada en palabras. La voz
  de la naturaleza, del ambiente, los llamados efectos de sonido. La voz del corazón, de los
  sentimientos, expresada a través de la música.»
- Efectos: «lo más propio de los efectos de sonido consiste en describir los ambientes, pintar el
  paisaje, poner la escenografía del cuento […] Los efectos van directo a la imaginación del oyente.»
- Música: «Lo más propio del lenguaje musical es crear un clima emotivo, calentar el corazón. La música
  le habla prioritariamente a los sentimientos del oyente.»
- Palabra: «entre las tres voces del lenguaje radiofónico, es la palabra la que más se dirige a la razón
  del oyente.» «La palabra manda. La palabra humana es la principal portadora del mensaje y su sentido.»
- Síntesis: «Imaginación, emoción, razón. Especificidades de cada voz radiofónica. Tres códigos
  complementarios».

### 1.3 Silencio: bache y pausa (LV, cap. 3, «¿Y el silencio?»)

- «En radio llamamos bache cuando se produce un silencio inesperado, no previsto, en cualquier momento
  de la programación.» «Estos silencios no pretendidos equivalen a la pantalla de televisión en negro. No
  tienen ningún significado, son fallas que deben evitarse.»
- «La pausa, por el contrario, está cargada de sentido. Hacer pausas es tomarse el tiempo necesario para
  subrayar una frase o una situación.»
- Postura de LV: «más que un código autónomo, los distintos tipos de silencios vienen siendo como el
  sistema de puntuación en el lenguaje escrito.» «El silencio, en radio, no dice nada por sí mismo,
  refuerza otros decires.»
- LV recoge en nota a **Mariano Cebrián Herreros** (*Información radiofónica*, Síntesis, Madrid, 1995,
  pág. 364): «El silencio es la ausencia del resto de componentes. Se incorpora como elemento de
  significación cuando aparece fragmentado entre diversos sonidos. […] La radio valora
  extraordinariamente el silencio informativo. […] siempre que no haya la más mínima sospecha de que se
  trata de un silencio debido a fallos técnicos.» (cita de segunda mano: decirlo así).
- Ritmo: «la monotonía se puede provocar tanto por lentitud como por sobreexcitación.»

### 1.4 Efectos: descriptivos y narrativos (LV, cap. 6, «Efectos y defectos»)

- «Clasifiquemos los efectos de sonido en dos grupos fundamentales: descriptivos y narrativos.»
- Descriptivos «también llamados ambientales, nos sirven para pintar los paisajes, mostrar el entorno
  donde ocurre la historia. […] Se mantienen en segundos y terceros planos.»
- Narrativos: «son los efectos que forman parte de la trama […] el efecto de sonido hace avanzar la
  acción. También son efectos narrativos los que usamos para sugerir el paso del tiempo».
- Economía: «Un efecto o dos, máximo tres, suelen ser suficientes para crear la mayoría de nuestros
  escenarios sonoros.» Criterio: «El criterio es la expresividad.»
- Orden efecto/palabra: «El kikirikí debe ir primero. Porque el efecto ocurre en la escena.»

### 1.5 Música: separar, subrayar, ambientar (LV, cap. 6)

- Tres utilidades: «Para separar las escenas», «Para subrayar una escena», «Para ambientar una escena».
- Cortina: «Establezcamos márgenes: con más de veinte segundos, resulta larga; con menos de ocho, no
  suele alcanzar para una separación tranquila de escenas.» (criterio de oficio de LV, no norma).
- «indicamos ráfaga musical. Dura menos segundos que la cortina y, sobre todo, exige una música bien
  ágil. También se suele marcar puente musical cuando buscamos un cambio sencillo de escena […] La
  llamada música de telón, más larga y rematada, se reserva para el final del programa.»
- Fondos: «Un criterio básico para los fondos es la sobriedad.» «la música se anticipa a la acción,
  precede al diálogo de los personajes.»
- Golpes musicales: «resultan muy efectistas»; leitmotiv: tema musical asociado a un personaje o
  situación recurrente.

### 1.6 Planos sonoros (LV, cap. 6)

- «El primerísimo plano (PP) sugiere la distancia íntima […] El primer plano (1P) indica una distancia
  personal […] Los segundos planos (2P) representan distancias sociales […] Terceros y cuartos planos
  (3P y 4P) se reservan para las distancias públicas: discursos, sermones, mítines.» (LV lo atribuye a
  Hall.)
- «La monotonía es a la voz lo que la falta de planos a la escena.»

### 1.7 Glosario de continuidad radiofónica (ME-RTVE 7.5, cotejado en la web el 03-10-2026)

- **Ambiente sonoro**: «Conjunto de señales acústicas que recrean el marco y la atmósfera de un espacio
  o sección radiofónicos.»
- **Careta**: «Señal sonora que sobre la sintonía o fondo musical incluye créditos, títulos fijos y otros
  textos sobre los contenidos de un espacio de radio.»
- **Cortinilla**: «También llamada ráfaga, es la señal sonora que separa secciones, noticias o párrafos
  en un espacio radiofónico. En determinadas ocasiones cumple una función gramatical: si su duración es
  de 4 segundos equivale al punto y seguido; las de 8 segundos corresponden a un punto y aparte.»
- **Golpe**: «Efecto sonoro que sirve para acentuar un instante concreto de un espacio de radio.»
- **Indicativo**: «Montaje sonoro muy breve que identifica a una emisora ante el oyente.»
- **Punto**: «Recurso radiofónico que tiene la misma función que el indicativo, pero aplicado no a la
  emisora, sino a un espacio concreto de su programación.»
- **Sintonía**: «Señal sonora, generalmente una melodía, que marca el comienzo y el final de un espacio
  radiofónico. Sirve para identificarlo entre los demás.»
- **Cuña**: «Montaje breve […] destinado a la venta de un producto comercial (cuña publicitaria); o a
  captar audiencia para un espacio de radio (cuña promocional).» Variante: «cuña de contenido o, más
  coloquialmente, "píldora"».
- Ojo: LV usa «cortina» y «ráfaga» como cosas distintas (la ráfaga más corta); ME-RTVE identifica
  cortinilla = ráfaga. No contradictorio, pero distinto uso: decirlo.

**No confirmado / no hay**: definición documentada de «narrativa sonora» como término; «continuidad» en
el sentido de programación (más allá de lo de Sonido 09 y el «guion de continuidad» de 2.3). Nada propio
de Canal Sur Radio sobre estos recursos.

---

## Tema 2 · Diseño de programas de radio: formatos, secciones, escaleta, guion, rundown, tono y público objetivo

**Ya cerrado/reutilizable**: RTVE produccion/03 y realizacion/02 (escaleta, minutado, guion en TV).
**Falta**: todo lo radiofónico.

### 2.1 Género y formato (LV, cap. 5)

- «Los géneros, entonces, son los modelos abstractos. Los formatos, los moldes concretos de
  realización. En realidad, casi todos los formatos podrían servir para casi todos los géneros.»
- Tres criterios de clasificación: «el modo de producción de los mensajes, la intencionalidad del emisor
  y la segmentación de los destinatarios». Por modo: **dramático, periodístico, musical**. Por intención:
  informativo, educativo, de entretenimiento, participativo, cultural, religioso, de movilización social,
  publicitario. Por destinatarios: infantil, juvenil, femenino, de tercera edad, campesino, urbano,
  sindical… «Es el target de nuestro programa.» (LV atribuye la estructuración a Cristina Romo, ITESO.)
- Formatos periodísticos: «En el periodismo informativo están las notas simples y ampliadas, crónicas,
  semblanzas, boletines, entrevistas individuales y colectivas, ruedas de prensa, reportes y
  corresponsalías… En el periodismo de opinión tenemos comentarios y editoriales, debates, paneles y
  mesas redondas, encuestas, entrevistas de profundidad, charlas, tertulias, polémicas… En el periodismo
  interpretativo e investigativo el formato que más se trabaja es el reportaje.»
- Formatos dramáticos: radioteatros, radionovelas, series, sociodramas, sketches…; narrativos: cuentos,
  leyendas…; combinados: noticias dramatizadas, radioclips…
- Formatos musicales: «programas de variedades musicales, estrenos, música del recuerdo, programas de
  un solo ritmo, programas de un solo intérprete, recitales, festivales, rankings, complacencias».
- Formato vs. recurso: «Un formato es un producto completo. Tiene sentido por sí mismo.» Saludar, dar la
  hora, presentar discos «No constituyen un formato, sino recursos para dinamizarlo.» Los formatos se
  anidan («matriushkas»): nota → boletín → revista informativa → programación.
- El magazine **no es un cuarto género** para LV: «La revista no es un nuevo género, sino un contenedor
  donde todo cabe».

### 2.2 Modelos y estructuras de programación (LV, cap. 11; ME-RTVE 7.5)

- LV: «cuatro tipos básicos de programación: la total (de todo para todos); la segmentada (de todo para
  algunos); la especializada (de algo para algunos); y las llamadas radio-fórmulas.» (LV remite a Josep
  Mª Martí, *Modelos de programación radiofónica*, Feed Back, Barcelona, 1990.)
- Especializada: «All music», «All news», «All talk».
- Estructuras: mosaico (unidad de media hora, «Contiguos, pero no continuos»), **bloques** («la más
  empleada en la actualidad— amplía la unidad de tiempo a dos, tres y hasta cuatro horas»; las secciones
  dentro del bloque «suelen durar de cinco a diez minutos»), y programación continua.
- ME-RTVE 7.5: **Radio convencional** — «Su parrilla puede ser horizontal, cuando mantiene diariamente
  los mismos espacios a las mismas horas; o vertical, si hay una programación distinta cada día de la
  semana.» **Radio temática o monográfica**: «utiliza variedad de formatos radiofónicos. Esta última
  característica la distingue de la radio-fórmula.» **Radio-fórmula**: «contenidos similares en una
  parrilla diaria única».
- **AIMC (NR-AIMC)** clasifica las emisiones en: «Generalista. Temática. Musical. Informativa. Otras.»
- **Definición de programa (AIMC, Grupo de Radio, 03-03-2010)**: «una unidad de espacio radiofónico con
  un mismo nombre y franja horaria definida que puede tener uno o varios conductores siempre que uno de
  ellos esté al menos en 2/3 del programa y tenga presencia en el otro tercio».
- **Definición de emisión radiofónica a efectos del EGM** (Grupo Radio AIMC 01/04/2016): «cualquier
  servicio de audio que consista principalmente en la difusión simultánea de programas y contenidos sobre
  la base de una estructura de programación definida, organizada en parrilla con horarios y con presencia
  en la programación de presentadores/locutores.»

### 2.3 Pauta, guion de continuidad y escaleta (ME-RTVE 7.5, cotejado web 03-10-2026)

Orden de los tres documentos según el glosario (esto es lo que el tema pide y RTVE-TV no da):
- **Pauta**: «Esquema previo al guión que contiene la estructura de un espacio radiofónico. En él figuran
  los bloques temáticos y la duración estimada de cada uno de ellos, pero se excluyen textos de locución e
  instrucciones técnicas.»
- **Guión de continuidad**: «Escrito que recoge, con todos los detalles necesarios para su realización,
  el contenido de un programa de radio. Incluye textos de las locuciones del presentador, fuentes de
  sonido externas (conexiones, unidades móviles, etc.), recursos sonoros y las instrucciones técnicas para
  el control.»
- **La escaleta**: «Esquema posterior a la elaboración del guión. Equivale a una pauta que refleja de
  forma precisa los datos que anteriormente eran sólo estimativos: temas, tiempos, pies o finales de
  frases y, ahora sí, indicaciones técnicas.»
- **Sección**: «Cada uno de los apartados formales o temáticos en que se divide un espacio radiofónico.»
- **Microespacio**: «Unidad temática de la programación de una emisora que, en tiempo breve y con
  estructura propia, trata sobre noticias, asuntos o personajes.»
- Contraste con RTVE-TV (produccion/03): en ese tema la escaleta puede ser previa; en el glosario de radio
  de ME-RTVE es **posterior** al guion. Señalarlo.

### 2.4 Guion radiofónico (LV, cap. 6, «El libreto y sus formalidades»)

Normas convencionales de LV (radio dramática; costumbre de oficio): papel de un solo lado, doble
espacio, no partir palabras, «Numere los renglones», «Los nombres de los PERSONAJES se escriben a la
izquierda y en mayúsculas», acotaciones «en mayúsculas y entre paréntesis», «(PAUSA)», planos «Sólo se
indican los 2P y 3P», «La MÚSICA […] se indica como CONTROL», efectos de disco como CONTROL y efectos
grabados en estudio como EFECTO, «Saque copias claras, una para cada actor y otra para el técnico.»
Guion «horizontal» a dos columnas: «A la izquierda, se ubican los diálogos de los personajes. A la
derecha, se indica la música y los efectos.»

### 2.5 Secciones, estructura y conducción del magazine (LV, cap. 9) — también sirve al tema 5

- Tres piezas: «la música, las secciones y la conducción».
- Música: «hasta el 50% o más del tiempo total del programa» (dato de LV, para revistas musicadas).
- Secciones: «espacios breves, generalmente hablados y de mayor elaboración». Unas pregrabadas
  (reportajes, encuestas, sketches), otras enlatadas, otras en directo (debates, consultorios, concursos).
- Fijas y móviles: «Podemos diseñar secciones fijas y otras que varían.»
- Orden: «Como en la programación musical, la amenidad es el criterio que rige el armado de las
  revistas.» No hay pirámide: en una revista larga los oyentes «subirán en la primera parada, otras a
  media ruta».
- Diseño transversal: «planificar ejes o hilos conductores que crucen toda la revista».
- «Coherencia y variedad, como recomienda McLeish». Tejido interno: «la costumbre y la sorpresa».
- Revista compacta (15-30 min): «¿Cuántas secciones? Dos, máximo tres.»
- Planificación: «En la parrilla de planificación se determinarán los temas (qué), los formatos y
  recursos a emplear (cómo), el responsable de cada sección (quién o quiénes), la fecha de emisión
  (cuándo).» «Quien cambia lo planificado se llama flexible. Quien no planifica, irresponsable.»

### 2.6 Público objetivo, franjas y tono (LV, cap. 11, «Pasos para armar una programación»)

- Pasos: perfiles y públicos; diagnóstico (contexto, públicos, competencia, equipo); estilo, objetivos y
  oferta; franjas horarias; parrilla; validación, monitoreo y evaluaciones; bautismo de programas.
- «No hay un público, sino muchos públicos.»
- Franjas: «conocer los hábitos de trabajo y ocio de nuestro público objetivo para adecuar los horarios
  de los programas». «La periodicidad óptima para un programa de radio es la diaria, de lunes a
  viernes.» (LV, cap. 9: «mejor 3 minutos al día que 30 a la semana»).
- Estilo/tono: «El estilo está relacionado directamente con el perfil de la emisora.»
- Dato objetivo de franja para España (MG26, pág. 30, consumo promedio diario de radio 2025, minutos
  sobre total población): **total 89,4**; mañana (06:00-12:00) 40,2; mediodía 18,7; tarde 15,0; noche
  (20:00-06:00) 15,5; L-V 96,2; sábado 74,6; domingo 70,5; generalista 48,1, temática 40,8. Gráfico de
  pág. 29: el consumo sube desde las 6:00 y la meseta más alta está entre las 8:00 y las 11:00 (valor
  cercano al 14 % en el gráfico; no hay cifra tabulada, no dar un número exacto).
- **Canal Sur (CP 3.18, ap. 98)**, porcentajes anuales «orientativos» de la oferta de radio por ondas:
  generalista: **Informativos 55 %, Divulgativos/Culturales 23 %, Entretenimiento 22 %**; radio «dedicada
  a la actualidad informativa y divulgación de interés público»: **55 / 40 / 5**; radio temática para
  audiencia joven: «El 75% […] divulgación de las creaciones de artistas andaluces de la música popular,
  así como del resto de España, y el 25% en espacios de entretenimiento»; radio online de flamenco:
  «producción propia al 100%». Son «porcentajes anuales orientativos como referencia general en torno a
  los siguientes valores aproximados» (salvedad, no omitir).

**No confirmado**: «rundown» no aparece en ninguna fuente leída (ni ME-RTVE ni LV ni AIMC). Es anglicismo
de oficio equivalente a escaleta/orden de emisión; decirlo como costumbre, sin fuente. «Tono» como rúbrica
de diseño: sin fuente específica más allá de lo citado.

---

## Tema 3 · Producción de contenidos: búsqueda de temas, documentación, invitados, entrevistas, permisos y coordinación

**Ya reutilizable**: RTVE documentacion/03 (búsqueda en internet). Redactor/a 04 (fuentes, verificación)
está en el bloque B; no se repite.

### 3.1 Búsqueda de temas y fuentes (LV, cap. 7)

- «La radio, más que otros medios, tiene que ser selectiva.» (noticiero de media hora «apenas salen al
  aire unas 20 noticias»; LV lo matiza en nota: depende del perfil de la emisora).
- Contra el periodismo de agenda: «¡La pauta! Ir a donde te llamen, trabajar a remolque de las
  conferencias de prensa que otros se inventan». «El periodista es un vigilante de la sociedad. No espera
  que lo llamen.»
- Pluralidad de fuentes: «La variedad de fuentes a las que acudiremos por propia iniciativa nos
  garantizará una selección de información más plural y balanceada.» Tipos: oficiales/extraoficiales,
  directas/indirectas, confidenciales.
- Ojo terminológico: en LV «pauta» es la agenda diaria de convocatorias; en ME-RTVE 7.5 «pauta» es el
  esquema previo al guion. Dos usos.

### 3.2 Invitados: condiciones de participación y permisos (ME-RTVE 1.1.5)

Literal (RTVE lo escribe para sí; usar como referencia de oficio, quitando «de RTVE»):
- «Derecho a conocer las condiciones de su participación. Las personas e instituciones invitadas […]
  serán informadas de las condiciones esenciales de su participación, entre ellas, si será emitida total
  o parcialmente y si será –en función del medio- en directo o diferido. Los invitados tienen derecho a
  conocer la identidad de otras personas invitadas, si las hubiera, al mismo espacio.»
- «Permisos y solicitudes de participación. […] cursarán una petición por escrito cuando así lo requiera
  la persona o institución invitada».
- «Permisos de grabación. Cuando una persona o institución requiera una solicitud o permiso para el
  acceso a sus instalaciones o al personal de las mismas, los profesionales […] velarán para que no se
  vulneren sus derechos ni su libertad editorial con condiciones inaceptables.»
- «Selección de fragmentos […] las declaraciones que se editen deben situarse en su contexto y reflejar
  lo que quiso decir el entrevistado. Los invitados no podrán imponer ninguna condición ni criterio».
- «Preguntas pactadas y cuestionario previo. Los invitados […] no tienen derecho a exigir cuestionario
  previo ni a pactar dicho cuestionario. Sí podrán, en cambio, solicitar ser informados sobre los asuntos
  genéricos objeto de la entrevista.»
- «Acceso previo a la emisión. […] no tienen derecho a leer, oír o visionar dicho espacio antes de su
  emisión […] salvo que, de modo excepcional […] se haya pactado lo contrario. Si se trata de contenidos
  que afectan a menores, dicho pacto sólo cabe hacerse con sus representantes legales.»
- Y (ME-RTVE, crtve, línea 73 del volcado): «Cuando una o más partes invitadas declinen su participación
  en un espacio de opinión se informará de ello a la audiencia.»
- Canal Sur (CP ap. 97): estudios de radio y platós «acondicionados para su accesibilidad física para el
  óptimo uso por parte del personal de la empresa como de las personas con diversidad funcional física
  invitadas a participar en programas de radio y de televisión».

### 3.3 Permisos y voz: Ley Orgánica 1/1982 (redacción vigente leída con `boe.py`)

- Art. 2.Dos (redacción vigente desde 15-02-1990; **inciso anulado por STC 9/1990**, leer la nota del
  BOE antes de citar): «No se apreciará la existencia de intromisión ilegítima […] cuando estuviere
  expresamente autorizada por Ley o cuando el titular del derecho hubiere otorgado al efecto su
  consentimiento expreso». Art. 2.Tres: «El consentimiento […] será revocable en cualquier momento, pero
  habrán de indemnizarse en su caso, los daños y perjuicios causados, incluyendo en ellos las
  expectativas justificadas.»
- Art. 7 (redacción vigente desde 23-12-2010): ap. 1 y 2 (aparatos de escucha, grabación de
  «manifestaciones o cartas privadas no destinadas a quien haga uso de tales medios»); **ap. 6: «La
  utilización del nombre, de la voz o de la imagen de una persona para fines publicitarios, comerciales o
  de naturaleza análoga.»**
- Art. 8.Uno: no son intromisión «las actuaciones autorizadas o acordadas por la Autoridad competente de
  acuerdo con la ley, ni cuando predomine un interés histórico, científico o cultural relevante.»
- **Límite**: derechos de voz e imagen son materia del tema 10 (bloque B, ya cerrado en Operador/a
  Montador/a 10). Aquí sólo lo que toca al permiso del invitado; remitir.

### 3.4 Entrevista en radio: preparación (LV, cap. 7, «Antes de la entrevista»)

- Clasificación por objetivo: «Entrevistas informativas», «Entrevistas de opinión», «Entrevistas de
  personalidad» («También se llaman de semblanza»). Por integrantes: individual, colectiva, encuesta
  («Un entrevistador y varios entrevistados por separado»), conferencia de prensa.
- Preparar: el equipo («haga una prueba de voz con el entrevistado para medir la distancia correcta del
  micrófono»), el tema («No se pide al entrevistador que domine todos los temas. Pero sí que domine la
  ruta de acceso a ellos, la documentación necesaria»), el cuestionario («El mejor cuestionario es el que
  se lleva en la cabeza»), al entrevistado («No caiga en la tentación de ensayar la entrevista»), a uno
  mismo, el lugar («Lo principal es evitar los ruidos»).
- Grabada o en vivo: «adoptaremos una actitud permanente de transmitir en vivo».
- Después: edición, ambientación y «archivo» («Esas entrevistas podrán ser utilizadas en otros
  programas»).
- LV cita a Kaplún: «El cuestionario sirve como guía y esquema» (*Producción de programas de radio*,
  CIESPAL, 1978, pág. 258; segunda mano).

### 3.5 Coordinación

Sin fuente nueva: la planificación en parrilla de LV (2.5) y la coordinación con el control (Redactor/a
08 ep. 10; Redactor/a 09 ep. 7). La relación con redacción/producción/centros territoriales es tema 15
(bloque C).

---

## Tema 4 · Presentación y locución: dicción, ritmo, improvisación, lectura, autocontrol y comunicación con el operador

**Ya cerrado** (copiar literal): Redactor/a 09 casi entero (claridad, ritmo, lectura, normas de
pronunciación de Canal Sur, improvisación, autocontrol «El locutor que maneja su propia mesa»,
comunicación con control). RTVE sonido/12 ep. 1 (señas del control: declara que **no hay fuente pública
que las fije** y aporta la clasificación entrar/salir/preparar).

**Falta y no se ha podido cubrir**: un código de señas publicado. Búsqueda en LV: ninguno (sólo menciona
«distráigalo con una mueca o un gesto de manos» en la entrevista). **Se mantiene el hueco declarado.**

Añadido útil de LV (cap. 9) sobre conducción del magazine — sirve a «ritmo» e «improvisación»:
- «la principal cualidad que se espera de un presentador o presentadora de revistas: la capacidad de
  conectarse con el oyente».
- «la primera profesionalidad de los conductores, en su capacidad de recuperación emocional rápida.»
- Pareja de conductores: «la posibilidad de dialogar entre ellos, de contrapuntearse las opiniones».
  Tres conductores: «probablemente resultará más confusa».
- En vivo: «Una radiorevista es plato caliente.» Si se graba: «grábelos como si estuviera saliendo en
  directo, sin parar la máquina».
- Pausas (ver 1.3): «Un comentarista que no maneja las pausas arriesga la convicción de sus palabras.»

---

## Tema 5 · Informativos y magazines radiofónicos: actualidad, servicio público, territorios, cultura y participación ciudadana

**Ya cerrado**: Redactor/a 08 ep. 6 (boletín), 7 (informativo), 8 (magazine: «El Manual de estilo de
RTVE no define el magazine radiofónico, y ninguna fuente leída lo hace»), participación del oyente
(ME-RTVE). Redactor/a 05 (géneros). RTVE realizacion-tv/07 (magazine en TV). Común 06 (Carta) y 05
(Ley 18/2007).

### 5.1 El magazine: ahora sí hay definición de oficio (LV, cap. 9) — cubre el hueco de Redactor/a 08

- «la radiorevista. También se la conoce como magazine.» «Su primer objetivo —antes que ningún otro—
  es hacernos pasar un buen rato, entretenernos.»
- «La revista […] no constituye un cuarto género de la producción radiofónica. Más bien, es un formato
  amplio, híbrido, capaz de englobar a los demás. […] también se la conoce como programa ómnibus».
- Segmentación y especialización: revistas por destinatarios (infantiles, de mujeres, de jóvenes…) y por
  contenido («informativas, deportivas, musicales, educativas, religiosas, culturales»).
- Duraciones: revistones de «tres, cuatro y más horas»; medianas «de una o dos horas»; compactas «entre
  los 15 y los 30 minutos».
- Participación: «Tal vez el formato radiofónico que permite una participación popular más intensa es
  la revista. No sólo permite: necesita.» Cuatro vías tradicionales: «Las visitas», «Las cartas y los
  emails», «Las llamadas telefónicas», «La radio entre la gente».
- Debe decirse que es fuente de oficio (latinoamericana); que ME-RTVE no lo define.

### 5.2 Informativos de radio de Canal Sur: lo que fija el Contrato-programa (CP 3.1)

- Ap. 4: «los programas y espacios informativos de radio y de televisión tendrán una aportación diaria
  sobresaliente de contenidos de ámbito local y provincial, en función de los recursos disponibles para
  ese fin». Producidos «con criterios convergentes de utilización con optimización de recursos y medios
  de los Centros de Producción de la RTVA en las ochos provincias andaluzas, y la Delegación de la RTVA en
  Madrid» [sic «ochos»]. «En las programaciones lineales contarán con un marcado protagonismo en franjas
  horarias destacadas, habituales, y estables».
- Ap. 5: informativos «en cadena» con «franjas horarias protagonistas […] en las franjas de mañana,
  mediodía y de noche, con amplias duraciones». «Los informativos serán efectivamente independientes,
  plurales, con credibilidad y rigor sin caer en la banalización de la realidad o el efectismo
  mediático». Contribución de «la Delegación de la RTVA en Madrid, y de las corresponsalías permanentes o
  eventuales».
- Ap. 6: «La oferta televisiva y de radio generalista incluirá programas, servicios y espacios
  informativos diarios, no-diarios, divulgativos-informativos, electorales cuando concurran comicios de
  cualquier ámbito territorial, sobre eventos sociales especiales y extraordinarios, información
  meteorológica, deportiva, información internacional, e información especializada».
- Ap. 9: «Todos los programas y contenidos informativos generales como provinciales de radio y de
  televisión serán ofrecidos tanto en directo por ondas hertzianas terrestres como en directo online y en
  diferido ‘a petición’ […] Igualmente, se producirá y distribuirá una relevante oferta de contenidos de
  audio digital de temática informativa para los servicios sonoros ‘a petición’ de las prestaciones de
  Canal Sur en su propia plataforma de Podcast.»
- Ap. 11 (debate) y 13 (acceso de grupos, art. 33 Ley 18/2007 y art. 11 Ley 10/2018): ya en Redactor/a 05
  y en el común.
- Ap. 14: unidad «‘Canal Sur Comprueba’» contra la desinformación (tema 9, bloque B).
- Ap. 15: «microespacios divulgativos» de alfabetización informacional «a lo largo de las programaciones
  lineales de radio y de televisión».

### 5.3 Servicio público y territorio (CSP)

- Art. 13.1: «Canal Sur se posiciona con vocación y propósito para ser el primer garante informativo de
  Andalucía. Todas las programaciones de los medios de radio, televisión […] tendrán como núcleo y eje
  fundamental los contenidos […] de los Servicios Informativos».
- Art. 13.8: «Tanto en los medios de radio como de televisión y servicios en plataformas y soportes
  digitales, Canal Sur producirá servicios informativos provinciales con la atención que requieran todos
  los municipios de cada provincia, además de las capitales y grandes ciudades, y estando disponibles los
  servicios provinciales en directo y «a petición» en los soportes web y plataformas digitales».
- Art. 6.3: «consideración permanente de atención sobre la diversidad de municipios de cada provincia
  andaluza, reflejando su realidad y actualidad con cercanía en el tratamiento de prestaciones de
  servicios y contenidos de «proximidad».»
- Art. 6.6: emisión de programas de servicio público por ondas «se adecuarán a las franjas horarias más
  idóneas y en consideración de las preferencias de la audiencia potencial a los que estén dirigidos.
  Asimismo, estarán orientados a la rentabilidad social […] y se fundamentarán en la diferenciación sobre
  las ofertas audiovisuales de otros operadores, en la proximidad de los asuntos y temas de que traten, y
  en la calidad».
- (El común 06 desarrolla la Carta: tomar de allí lo que ya esté y citar sólo la aplicación a radio.)

### 5.4 Cultura (CP 3.2)

- Ap. 19: «Los servicios informativos de todos los medios de Canal Sur informarán de la actividad
  cultural que se desarrolla en la actualidad de Andalucía, y de forma singular promoverán la difusión y
  el conocimiento de las creaciones […] de los nuevos talentos andaluces».
- Ap. 23: flamenco «conforme a la Ley 4/2023, de 18 de abril» […] «con programas habituales sobre toda
  modalidad del ‘Flamenco’ […] y con la contribución del portal y servicio web flamencoradio.com».
  (No verificada aquí la Ley 4/2023 andaluza del flamenco; si se cita, leerla.)

### 5.5 Participación ciudadana (CP 3.18 ap. 99; CSP art. 26; CP ap. 30)

- **CP ap. 99** (específico de la radio): «Todos los programas, espacios y contenidos divulgativos,
  culturales y de entretenimiento de la programación de Canal Sur Radio tendrán planteamientos
  interactivos en la utilización de aplicaciones y herramientas tecnológicas para poner en acción todas
  las posibilidades de las redes sociales para un contacto ágil, dinámico y permanente de la audiencia
  con los programas, en los que se tenderá a su participación notable. Se producirán programas cara al
  público y con participación de la audiencia, sobre eventos especiales que estén orientados a audiencias
  significativas o a eventos de notorio interés general o sectorial de la Comunidad o de cada una de sus
  ocho provincias.»
- CSP art. 26.2: «Los medios de Canal Sur prestarán los máximos niveles de atención a la audiencia y
  personas usuarias de sus servicios, realizando producciones que contengan sus manifestaciones y
  prestando servicios participativos. La atención y participación se convertirá en un eje rector».
- CSP art. 26.1: cauce ante el «órgano interno de Defensa de la Audiencia de la RTVA, que preservará los
  derechos de todas las personas espectadoras, oyentes y usuarias».
- CP ap. 30: «Los medios de Canal Sur conciben la interacción de las personas usuarias como un necesario
  eslabón de la cadena de valor de la producción audiovisual.»

### 5.6 Canal Sur Radio: lo publicado sobre su oferta

- CP ap. 105: FM 24 h «de las diversas marcas de servicios sonoros de radio de Canal Sur». Ap. 106:
  distribución por internet 24 h «de toda la oferta sonora de radio lineal y no-lineal». Ap. 107: «a través
  de los canales de audio de televisión en TDT de toda la oferta lineal sonora de radio de Canal Sur».
  Ap. 104: plataforma de Podcast 24 h. Ap. 109: flamencoradio.com.
- CS-web (03-10-2026): el menú de radio muestra **Canal Sur Radio, Canal Fiesta (Radio) y Flamenco Radio**;
  Canal Fiesta se presenta como «la radio musical de Andalucía». **No consta** en lo leído el nombre de la
  «oferta de radio lineal dedicada a la actualidad informativa» del CP 98.b; no nombrarla.
- No usar nombres de programas de la web (cambian por temporada).

---

## Tema 6 · Técnicas de entrevista, debate, tertulia, reportaje sonoro, crónica, conexión en directo y narración deportiva

**Ya cerrado** (copiar literal): Redactor/a 05 ep. 3 (crónica), 4 (reportaje), 5 (entrevista), 7 (directo
y conexión, con la cita de ME-RTVE sobre conexiones «con el exterior, ya con la red de emisoras locales y
territoriales»), 8 (debate y tertulia, ME-RTVE 3.4.1 y 3.4.2), 9 (narración deportiva, radio vía ME-RTVE
3.5). Redactor/a 08 ep. 3-5 (cortes, crónica, entrevista en radio). RTVE realizacion-tv/07.

**Falta**: estructura y moderación del debate en radio; técnica de la entrevista radiofónica (3.4 arriba);
rueda de corresponsales/emisoras (conexión); reportaje sonoro.

### 6.1 Debate en radio (LV, cap. 9, «Prohibido prohibir: los debates»)

- Debate ≠ mesa redonda: «En éstas, se pretende complementar ideas en torno a un tema […] En el debate,
  se busca la polémica.»
- Cuatro elementos: el tema («Que sea provocativo»), los invitados («ideas contrarias […] de un nivel
  semejante»; «La mejor solución radiofónica son dos y con el moderador, tres. Así no se confunden las
  voces»), el moderador, los dinamizadores (testigo, sociodrama, encuesta, canción).
- Errores del moderador: «Moderar demasiado», «No moderar nada», «Robar protagonismo», «No ser
  imparcial» («Regla inviolable de la moderación es la imparcialidad»), «Sacar conclusiones».
- Estructura: «Apertura», «Presentación de los invitados (nombres y cargos)» («el moderador se referirá a
  ellos por sus nombres y cargos para identificarlos ante un oyente distraído»), «Primera ronda»,
  «Segunda ronda», «Tercera ronda» (llamadas), «Ultima ronda» (alegato), «Cierre» («el moderador no
  concluye nada»).
- Coherente con ME-RTVE 3.4.1 (mismas condiciones de sonido para todos; ya en Redactor/a).

### 6.2 Conexión: ruedas (ME-RTVE 7.5, cotejado)

- **Rueda radiofónica**: «Formato que consiste en conexiones simultáneas mediante múltiplex. Suele estar
  dirigida por un presentador que coordina, desde el estudio central, las intervenciones de los
  participaciones» [sic].
- **Rueda de corresponsales**: «Rueda radiofónica cuyos participantes son los corresponsales y enviados
  especiales en el extranjero.»
- **Rueda de emisoras**: «Rueda radiofónica en la que participan informadores de distintas delegaciones de
  una cadena. Normalmente gira en torno a un tema o noticia concretos.» (Encaja con los centros de
  producción provinciales de CP 3.1 ap. 4.)

### 6.3 Entrevista: tipos y fases

Ver 3.4 (LV). Añadir, de LV «Después de la entrevista»: «No regrabe sus preguntas» (salvo en reportaje,
donde se sustituyen por narración).

### 6.4 Reportaje sonoro

- LV: el reportaje es el formato del periodismo interpretativo e investigativo (2.1). LV, cap. 7,
  «¿Y el documental?»: «Algunos productores, más que de reportaje, prefieren hablar de documental» (no se
  leyó el epígrafe entero; si el redactor lo usa, leer líneas 8314-8430 del .txt).
- **No confirmado**: definición de «reportaje sonoro» como término en fuente española; nada propio de
  Canal Sur.

### 6.5 Narración deportiva

Sin fuente nueva más allá de Redactor/a 05 ep. 9. LV, cap. 9, «Mente sana en emisora sana» trata el
deporte en la revista (no se ha leído entero; leer si se quiere más). **Hueco**: técnica de narración
deportiva radiofónica con fuente española.

---

## Tema 8 · Autocontrol y operación básica: niveles, entradas, salidas, cuñas, músicas, ráfagas y continuidad

**Ya cerrado** (copiar literal): Sonido 04 (28) — Niveles, Entradas, Salidas (PFL/AFL, ganancia, faders,
nivel de alineación, auxiliares, mezcla menos); Sonido 09 (28) — Músicas («La ambientación musical»,
«La música bajo la voz»), «Cuñas, ráfagas y continuidad» (R 128 s1 para piezas cortas, «La continuidad:
que todo suene igual», caso de la cuña que no pasa). Redactor/a 09 ep. 5 (locutor que maneja su propia
mesa). RTVE sonido/12, 07 y 14 (autocontrol, dinámica, medición).

**Falta**: sólo vocabulario de piezas de continuidad, que da ME-RTVE 7.5 (ver 1.7: careta, cortinilla =
ráfaga con su 4 s / 8 s, indicativo, punto, sintonía, cuña y «píldora») y la ráfaga/cortina/puente/telón de
LV (1.5). **Nada más que investigar**: el resto está cerrado y verificado.

---

## Tema 16 · Análisis de audiencia radiofónica y digital, indicadores y mejora de contenidos

**Reutilizable con cautela**: RTVE gestion/27 ep. 9 y produccion/04 (TV; ver advertencias 4 y 5).

### 16.1 Quién mide la radio: el EGM de AIMC

- Fuente oficial: AIMC-web (radio streaming) lo llama «la **fuente oficial de audiencia de radio**».
- Nacimiento (AIMC-web, nacimiento y evolución, vía WebFetch): «es en 1968, cuando nace verdaderamente el
  EGM»; «En 2002 se produce un trascendente cambio en la historia del EGM con la implantación del sistema
  CAPI». (Leído en resumen de WebFetch, no en el .txt guardado: si se usa, releer la página.)
- Estudio poblacional: «No se trata de representar a los lectores, o a los oyentes, o a los espectadores,
  sino que busca una representación adecuada de la población». «Es un estudio anual. El diseño muestral
  es anual, aunque tal diseño se divida posteriormente en tres partes de igual tamaño y composición; el
  ciclo muestral sólo se completa en tres oleadas».
- Universo: «individuos de 14 o más años residentes en hogares unifamiliares de la España peninsular,
  Baleares y Canarias» (página «Universo y muestra»; la ficha técnica 2026 dice «residentes en hogares,
  ubicados en municipios dentro de la España Peninsular, Islas Baleares e Islas Canarias»).
- Muestra de radio (ficha técnica 1.ª ola 2026): «Tamaño muestral anual: **78.236 entrevistas** (23.158
  personales “face to face” + 6.611 online + 48.467 telefónicas).» Métodos: CAPI, CAWI y CATI.
  «Afijación proporcional por Comunidades Autónomas y provincias pero con un mínimo muestral provincial de
  156 entrevistas por ola, 470 al año.» «Incremento muestral en las comunidades de **Andalucía**, Aragón,
  […]». Teléfono: 49 % fijo, 32 % móvil con fijo, 19 % sólo móvil. (La página «Universo y muestra» da una
  tabla redonda anterior —30.000 + 37.000 + 11.011 = 78.011—: **usar la ficha técnica 2026**.)
- Trabajo de campo: «Random y Kantar» (personal), online «Random, Kantar, Netquest y Dynata», telefónico
  «Imop Insights». Supervisión: «Un 10% de entrevistas se supervisa directamente por AIMC.»
- Calendario 2026 (resultados a asociados): 1.ª ola **15 abril**, 2.ª ola **30 junio**, 3.ª ola **10
  diciembre**. A 24-09-2026 la última publicada es la 2.ª ola (30-06-2026; AIMC-web blog «Resultados EGM 2ª
  ola 2026», 30 junio 2026).
- Fusión (desde la 1.ª ola de 2008): un único fichero con multimedia y monomedias; premisas «Mantener en
  lo posible los datos oficiales antes de la fusión» y que sea «trazable».
- Márgenes de error: «calculados para un nivel de confianza del 95,5% equivalente a dos Sigma»; «sólo son
  válidos para variables dicotómicas (audiencia, posesión, etc.), pero no son válidos para otro tipo de
  variables (share, minutos de consumo, etc.)».
- Entrega: tablas de la ola y del acumulado con las dos anteriores, «una acumulación anual móvil».

### 16.2 La pregunta y los indicadores de radio (NR-AIMC)

- «El dato que se investiga es la audiencia de un día promedio con un nivel de desglose de medias horas,
  empezando a las 6 de la mañana del día de ayer y terminando a las 6 de la mañana de hoy.» Pregunta:
  «Por favor, trate de recordar todos los momentos en los que ayer escuchó u oyó la radio a lo largo del
  día, en cualquier lugar y a través de cualquier tipo de aparato, aunque solo fuera unos minutos.»
  (Canarias: de 5 a 5.) Cuestionario (AIMC-web): audiencia del último período = «“Ayer” para Diarios,
  Radio, Televisión e Internet».
- Varias emisoras por media hora: para la acumulada cuentan todas; «Para el cálculo de la audiencia
  media, en casos de este tipo, se reparten los 30 minutos a partes iguales».
- **Audiencia acumulada**: «Número de individuos […] que declaran escucha de un determinado soporte en al
  menos un intervalo de media hora.»
- **Minutos de escucha**: consumo promedio por individuo, «“per cápita” (referido al total población) o
  “por oyente”».
- **Audiencia media**: «Promedio de individuos […] que han escuchado un determinado soporte a lo largo del
  periodo especificado. Se calcula ponderando cada oyente por su tiempo de escucha respectivo. […] Este
  indicador expresado en porcentaje (rating) es equivalente al porcentaje que el consumo “per cápita”
  supone sobre la duración total del intervalo temporal considerado.»
- **Índice de fidelidad**: «Cociente porcentual entre la audiencia media y la audiencia acumulada. Su
  valor máximo es 100». En media hora «es siempre 100».
- **Participación o Share**: «Expresa la distribución de la escucha por soportes durante un periodo de
  tiempo. […] cociente porcentual entre su audiencia media y la audiencia media del total medio». Bases:
  «Para soportes incluidos en “Generalista”: Total Generalista. Para soportes incluidos en “Temática”:
  Total Temática. Para Total Generalista y Total Temática: Total Oyentes.»
- **Aportación**: porcentaje de la audiencia media de un bloque horario sobre la del total día (suma 100).
- **Perfil**: «Distribución porcentual de la audiencia acumulada a través de diferentes categorías».
- **Penetración**: «Número de oyentes expresado en porcentaje sobre el universo.»
- Asignación de cada mención: prioridad «1) Nombre del locutor 2) Programa 3) Cadena 4) Emisora» (dato
  bueno para pregunta: **el locutor manda**).
- Publicación: «Los datos de audiencia de emisoras aparecen […] exclusivamente en año móvil y no en
  oleada.» Cortes mínimos de publicación (año móvil, individuos, ranking): Radio L-D 0,15 %, L-V 0,15 %.
- Podcast en el EGM: la audiencia «se asignará a la cadena correspondiente en el momento que haya
  declarado escucharlo el individuo, independientemente del programa a que corresponda y de la franja en
  la que fuese emitido originalmente».
- Desde la 1.ª ola de 2018 el EGM «Incluye la escucha desglosada de radio en directo/streaming y en
  formato diferido/podcast» (AIMC blog 18-04-2018).

### 16.3 Streaming censal (AIMC-web, radio streaming)

- «desde la 3ª ola de 2024, el EGM incluye la audiencia a través de Internet vía streaming/directo de las
  principales cadenas de radio, obtenida directamente a partir de sus datos censales de consumo.» Socio
  técnico: ODEC. «pionera a nivel mundial».
- Participan 37 cadenas de grupos entre los que figura **«RTVA (Canal Sur)»**.
- Proceso: logs de los servidores de audio, «Depuración del tráfico no humano», sesiones desde España;
  convertir sesiones en individuos con datos sociodemográficos del EGM; se traslada «con sus respectivos
  promedios de día de la semana por medias horas».

### 16.4 Canal Sur Radio en el EGM (MG26, datos anuales 2025; leídos en la imagen de la tabla)

- Audiencia acumulada diaria (% población 14+), Radio Generalista, págs. 33: **Canal Sur Radio 0,5 % en
  2025** (0,9 en 2005; serie descendente). Temática: **Canal Fiesta Radio 0,5 % en 2025**.
- Share (pág. 35): **Canal Sur Radio 1,6 en 2025** (base Total Generalista según NR-AIMC); **Canal Fiesta
  Radio 1,5** (base Total Temática).
- Totales 2025: generalista 30,8 %; temática 31,5 % (acumulada diaria).
- **Advertencia**: son porcentajes sobre la población **de toda España**, no de Andalucía. El dato
  andaluz no se ha extraído (MG26 tiene tablas por CC. AA. de consumo, no de cadenas). Las cifras de
  oyentes por ola (p. ej. «315.000» en la 2.ª ola 2026) **sólo aparecen en prensa secundaria**
  (gorkazumeta, dircomfidencial, Barlovento) y **no se han confirmado** en AIMC: no usarlas.

### 16.5 Medición digital: estado a 24-09-2026 (AIMC-NP)

- 08-10-2025 (Comisión de Seguimiento aea/AIMC/IAB Spain): plazo de GfK DAM como «medidor recomendado
  para la medición digital del mercado español» finaliza en diciembre de 2025 «tras los cuatro años
  transcurridos de adjudicación»; «Durante el período que conlleve establecer la nueva medición, se
  mantiene la recomendación a GfK DAM.»
- 10-07-2026: la Junta Directiva de AIMC selecciona «de manera unánime» la propuesta de **COMSCORE** en el
  concurso convocado el 9-03-2026; principios del reglamento europeo **EMFA**; metodología «híbrida
  -que combina datos censales con datos provenientes de diferentes paneles-»; competían GfK y Nielsen.
- **01-09-2026**: «Comscore haya comunicado que no está en disposición de formalizar el contrato ni de
  ejecutar el proyecto comprometido»; «la Junta Directiva de AIMC se reunirá en los próximos días para
  analizar el escenario». A 03-10-2026 la página del concurso no tiene entradas posteriores.
- **Conclusión para el tema**: a la fecha del temario **no hay nuevo medidor digital recomendado en
  funcionamiento**; lo último confirmado es la recomendación prorrogada a GfK DAM (08-10-2025). **No
  confirmado**: si GfK DAM sigue publicando datos en septiembre de 2026. Redactar con esa salvedad.

### 16.6 Métricas de podcast (IAB-POD v2.2)

- Medición basada en logs de servidor; categorías: «1. Podcast Content Delivery 2. Podcast Audience 3.
  Podcast Ad 4. Higher Level or Advanced».
- **Download**: «a unique file request that was downloaded. This includes complete file downloads as well
  as partial downloads».
- **Listener**: «data that represents a single user who downloads content […] represented by the unique
  combination of IP address and User Agent». «Listeners must be specified within a stated time frame
  (day, week, month, etc.).» «Listener = Count of Unique (IP* + UA)».
- Umbral contra precargas: «Use a download threshold based on one minute of content».
- Duplicados en ventana de 24 horas: «The date and time is used to define a 24-hour window (either by
  calendar day or rolling 24 hours) in which downloads are filtered for duplicates.»
- Hay una v2.3 en comentario público (iabtechlab.com, julio 2026, no leída): la vigente es la 2.2.
- Traducción: es inglés; el redactor debe traducir y decir que es directriz de la industria (IAB Tech
  Lab), no norma.

### 16.7 Mejora de contenidos: qué manda Canal Sur y cómo lo dice el oficio

- CSP art. 6.5: «estrategia de permanente estudio y conocimiento profundo de la sociedad andaluza», con
  «Análisis prospectivos», «Estudios cuantitativos y cualitativos sobre niveles de aceptación social de
  programaciones y servicios».
- **CSP art. 6.7**: «A los seguimientos sobre la audiencia de los servicios por ondas hertzianas
  terrestres se sumarán periódicos estudios de análisis cualitativos de la audiencia en relación a los
  programas y su aceptación social. A las tradicionales fuentes de información sobre audiencia como cuota
  de pantalla share se incorporarán sistemas de analítica big data, con registros crossmedia y transmedia
  […] para alcanzar la óptima adaptación de los contenidos y servicios a la demanda real de la sociedad».
- **CP ap. 29**: «se analizarán de manera permanente los datos servidos por entidades del sector sobre
  medición de audiencia, consumos digitales sobre flujo de uso y acceso, visionado/escuchado […] de su
  propia plataforma streaming ‘Canal Sur Más’ y la de servicios Podcast»; «Paulatinamente los medios de
  Canal Sur incorporarán sistemas de analítica Big Data con registros ‘cross media’ y ‘transmedia’».
- CP ap. 126: «un propio sistema de indicadores de referencias sobre la rentabilidad social»; ap. 129:
  «Sistema Integral de Indicadores de gestión».
- CP ap. 30: atención a «tendencias en redes sociales digitales» y a «cuestiones, sugerencias, quejas y
  reclamaciones»; Defensa de la Audiencia (CSP art. 26).
- AIMC-web (usos del EGM «Para el medio»): «Marketing de producto: […] determinación de huecos de
  mercado, confección de parrillas de programación (medios audiovisuales)».
- Oficio (LV, cap. 11): validar, monitorear y evaluar — «Prueba de materiales», «Monitoreo permanente»,
  «Evaluaciones periódicas» («una vez al año, al menos»); «dos caminos clásicos de la investigación: el
  más cuantitativo, que se trabaja en base a encuestas, y el más cualitativo, que emplea las entrevistas
  individuales, las colectivas y los focus group.»
- Lectura crítica del rating (LV, «El fetiche del rating»): «los resultados del rating, aun siendo
  importantes, sólo son cuantitativos»; «Los diferentes perfiles de las radios diferencian la
  competencia.» (Matiz: LV habla de radios comunitarias; útil sólo como criterio general.)

**No confirmado / no hay**: GfK/Comscore métricas concretas de radio digital; datos de audiencia digital de
Canal Sur; datos del EGM de Canal Sur Radio en Andalucía; una norma que defina *rating/share* (ninguna: los
define la industria — AIMC para radio).

---

## Lo que queda sin fuente en todo el bloque

1. Código de señas control-locutorio (tema 4): no hay fuente pública. Se mantiene el hueco ya declarado.
2. «Rundown» (tema 2): sin fuente; anglicismo de oficio.
3. Definición de «reportaje sonoro» y técnica de narración deportiva radiofónica con fuente española
   (tema 6).
4. Año/editorial de Balsebre en fuente primaria (tema 1).
5. Nombre de la emisora de actualidad de CP 98.b; audiencia de Canal Sur Radio en Andalucía; cifras por
   ola 2026 (sólo prensa) (temas 5 y 16).
6. Situación real de GfK DAM en septiembre de 2026 (tema 16).
7. Ley 4/2023 andaluza del flamenco: citada por el CP, no leída.

## Ficheros tocados

- Creado: `informes/canal-sur-especificos/31-investigacion-A-radio.md` (este).
- Creada la carpeta `fuentes/canal-sur/radio/` con los 28 ficheros listados en «Fuentes nuevas»
  (aimc-*, iabtechlab-*, lopez-vigil-*, unlp-*, canalsur-web-radio-*). La carpeta la comparten otros
  bloques: `BOE-A-2011-19600.*`, `canalsur-web-frecuencias-radio-*` y `memoria-rtva-2022.*` no son de
  este bloque.
- Ningún tema ni otro informe modificado.
