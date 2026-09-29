# Tema 13 del específico de Realizador/a · Postproducción: montaje, edición, efectos, grafismo, mezcla y revisión de calidad final

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Realizador/a · punto 13 |
| Sirve para | Realizador/a de Canal Sur (grupo B02): test de teoría específica y de aplicación práctica, y prueba práctica del puesto |
| Fuente | Sin norma que regule la postproducción. Lo propio de la casa: X Convenio colectivo de la RTVA (fichas de puesto) y *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, 2004). Norma de enseñanza, no del oficio: Real Decreto 1680/2011 (módulos 0905, 0906 y 0907). Recomendaciones técnicas: UIT-R BT.1702-3 (destellos), EBU R 128 y R 128 s1 (sonoridad), EBU Tech 3343; documentos de control de calidad de la UER. Documentación de fabricante: Avid (*Media Composer User's Guide*, 1999; *Avid DNxHD Technology*, 2012), Blackmagic Design (*DaVinci Resolve 21 Reference Manual*), Adobe (ayuda de Premiere), EVS (manual de IPDirector). Teoría del montaje: tesis de J. M. Todd (Georgia Tech, 1989) sobre Eisenstein. Lo demás, oficio declarado como tal |
| Redacción que se estudia | La vigente el 24-09-2026: Recomendación UIT-R BT.1702-3 (11/2023), en vigor; EBU R 128-2023 (versión 5), R 128 s1 V3 (agosto de 2020) y Tech 3343-2023 (versión 4). Real Decreto 1680/2011 en su texto de 2011: el Real Decreto 500/2024 lo modifica, pero no toca los módulos que se citan. Documentación de fabricante en la versión leída (fechas en «Trazabilidad») |
| Extensión | 15.900 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); real decreto (RD), y en las citas del RD 1680/2011 cada resultado de
aprendizaje (RA) va con la letra de su criterio de evaluación; Unión Internacional de
Telecomunicaciones (UIT) y su sector de radiocomunicaciones (UIT-R, en inglés ITU-R); Unión Europea de
Radiodifusión (UER, en inglés EBU, *European Broadcasting Union*), que publica recomendaciones (R) y
documentos técnicos (Tech); control de calidad (QC, *quality control*); preparado para difusión o
emisión (PPD, así lo desarrolla el propio RD); la especificación de entrega en fichero que la UER cita
como «AS11 DPP», de la Advanced Media Workflow Association (AMWA) en la versión de la Digital
Production Partnership (DPP), que se estudia en el tema 14; la descripción del formato activo (AFD,
*Active Format Description*) y el código de tiempo (TC, *timecode*), que aparecen en las definiciones
de la UER; los tres primarios rojo, verde y azul (RGB); la luminancia (Y) y las diferencias de color
(Cb y Cr, que Blackmagic escribe CB y CR); YRGB, la luminancia más los tres primarios, como la
escribe Blackmagic; la tabla de consulta (LUT, *look-up table*); el formato de LUT común (CLF,
*Common LUT Format*) y el lenguaje de transformación de color de Resolve (DCTL, *DaVinci Color
Transform Language*); matiz, saturación y luminosidad (HSL, *hue, saturation, luminance*); alto rango
dinámico (HDR, *high dynamic range*), con su curva híbrida logarítmica-gamma (HLG, *hybrid log-gamma*),
y rango dinámico estándar (SDR); candela por metro cuadrado (cd/m²); milisegundo (ms); hercio (Hz);
la Recomendación UIT-R BT.709, que el oficio llama Rec. 709; Society of Motion Picture and Television
Engineers (SMPTE); el código de tiempo longitudinal (LTC) y el vertical (VITC), el MIDI (interfaz
digital de instrumentos musicales, *musical instrument digital interface*) y su código de tiempo
(MTC), y el código con salto de cuadro (DF, *drop frame*) y sin él (NDF); la sustitución automatizada
de diálogo (ADR, *automated dialogue replacement*); códecs de Avid DNxHD y DNxHR y de Apple ProRes, y
los formatos de cámara AVC-Intra y XDCAM; codificación avanzada de vídeo (H.264) y de alta eficiencia
(H.265); alta definición (HD); gestión de activos de medios (MAM, *media asset management*) y de activos de producción (PAM,
*production asset management*), con dos nombres comerciales de Avid que no son siglas: NEXIS, su
almacenamiento compartido, y MediaCentral | Cloud UX, su acceso por navegador; el mando de repetición y cámara lenta de EVS (LSM), marca cuyo
nombre se usa en el oficio como nombre común, e IPDirector, su programa de gestión; decibelio (dB);
decibelios de pico verdadero (dBTP, *decibels true peak*); unidades de sonoridad referidas a la
escala completa (LUFS, *loudness units relative to full scale*) y unidad de sonoridad (LU, *loudness
unit*); rango o margen de sonoridad (LRA, *loudness range*); la Comisión Internacional de la
Iluminación (CIE). LB no es una sigla que se desarrolle aquí: es el nombre de variante que da Avid (DNxHR LB).

Los nombres de órdenes y ventanas se dan con su rótulo inglés, en cursiva la primera vez: *trim*
(ajuste de un corte, «trimar» en la sala), *slip* y *slide* (deslizar el contenido de un plano y
desplazar el plano), *match frame* (buscar el fotograma original), *render* (cálculo de efectos),
*offline* y *online* (montaje y acabado), *proxy* (copia ligera), *keyframe* (fotograma clave),
*lift*, *gamma* y *gain* (los mandos de sombras, medios tonos y altas luces), *handles* (colas de un clip),
*crossfade* (fundido cruzado de audio), *ganged* (canales enganchados) y *dump* (volcado).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.33, punto 13): «Postproducción:
> montaje, edición, efectos, grafismo, mezcla y revisión de calidad final.»

Qué se puede preguntar: qué es la postproducción y qué fases tiene; quién dirige el montaje, la
postproducción y las mezclas en la RTVA y quién controla la calidad; qué pide el módulo 0907 del RD
1680/2011; cuáles son los cinco métodos de montaje de Eisenstein y qué ordena cada uno; qué es un
montaje preliminar y qué separa el *offline* del *online*; qué distingue la edición lineal de la no
lineal; qué es trimar y qué diferencia el *slip* del *slide*; qué hace el *match frame*; qué es el
coleo; qué es renderizar; qué códec conviene para montar; cómo se resta un código de tiempo y qué es
el *drop frame*; qué hace un servidor de repetición y qué son los canales
enganchados; qué es un efecto, qué familias de incrustación hay y por qué el fondo es verde; qué es
una máscara, un fotograma clave y la curva de velocidad; cómo se hace una cámara lenta y qué
distingue la repetición de cuadros, la mezcla y el flujo óptico; qué efectos limita el Libro de Estilo
en la información; qué son las colas y qué pasa si faltan al poner una transición; qué es etalonar,
qué muestran el desfile y el vectorscopio, qué es una LUT 1D y una 3D y qué distingue la corrección
primaria de la secundaria; quién hace el grafismo y
qué pide el Libro de Estilo a los gráficos; en qué orden se mezcla, qué es el ADR y qué sonoridad y
qué pico verdadero ha de cumplir el programa; qué es una plantilla de control de calidad de la UER y
qué comprueba; qué destellos y patrones da por dañinos la BT.1702-3; qué especifica un máster y qué
señales se graban en un programa de plató. En la prueba práctica: dirigir el acabado de un reportaje,
montar un resumen deportivo desde el servidor de repetición o resolver una pieza que la revisión de
calidad devuelve.

<!-- indice -->

## Índice

- [Postproducción](#postproducción)
  - [Qué es la postproducción](#qué-es-la-postproducción)
  - [El realizador responde del acabado](#el-realizador-responde-del-acabado)
  - [Lo que pide la norma de enseñanza](#lo-que-pide-la-norma-de-enseñanza)
- [1. Montaje](#1-montaje)
  - [Montar](#montar)
  - [Los cinco métodos de montaje de Eisenstein](#los-cinco-métodos-de-montaje-de-eisenstein)
  - [Del primer armado al montaje final](#del-primer-armado-al-montaje-final)
  - [Offline y online](#offline-y-online)
- [2. Edición](#2-edición)
  - [Lineal y no lineal](#lineal-y-no-lineal)
  - [Los programas](#los-programas)
  - [Ajustar un corte: el *trim*](#ajustar-un-corte-el-trim)
  - [Del montaje al original: el *match frame*](#del-montaje-al-original-el-match-frame)
  - [El coleo](#el-coleo)
  - [El *render*](#el-render)
  - [El códec con que se monta](#el-códec-con-que-se-monta)
  - [El código de tiempo](#el-código-de-tiempo)
  - [La aritmética del código de tiempo](#la-aritmética-del-código-de-tiempo)
  - [Montar en red: el material compartido](#montar-en-red-el-material-compartido)
  - [El servidor de repetición](#el-servidor-de-repetición)
- [3. Efectos](#3-efectos)
  - [Qué es un efecto en el sistema de edición](#qué-es-un-efecto-en-el-sistema-de-edición)
  - [Incrustar](#incrustar)
  - [La máscara](#la-máscara)
  - [Fotogramas clave y curva de velocidad](#fotogramas-clave-y-curva-de-velocidad)
  - [Los efectos de tiempo](#los-efectos-de-tiempo)
  - [Corte y transición](#corte-y-transición)
  - [Las transiciones corrientes](#las-transiciones-corrientes)
  - [Las colas](#las-colas)
  - [El color: corrección y etalonaje](#el-color-corrección-y-etalonaje)
  - [Medir antes de tocar: los monitores de señal](#medir-antes-de-tocar-los-monitores-de-señal)
  - [Las LUT](#las-lut)
  - [Primaria y secundaria](#primaria-y-secundaria)
  - [La corrección secundaria: ventanas y cualificadores](#la-corrección-secundaria-ventanas-y-cualificadores)
  - [Igualar los planos](#igualar-los-planos)
  - [Los efectos y la información](#los-efectos-y-la-información)
- [4. Grafismo](#4-grafismo)
  - [Quién hace qué](#quién-hace-qué)
  - [Títulos y rótulos en el sistema de edición](#títulos-y-rótulos-en-el-sistema-de-edición)
  - [Lo que pide el Libro de Estilo](#lo-que-pide-el-libro-de-estilo)
  - [Lo que ya está en el tema 12](#lo-que-ya-está-en-el-tema-12)
- [5. Mezcla](#5-mezcla)
  - [Qué es mezclar en postproducción](#qué-es-mezclar-en-postproducción)
  - [Limpiar antes de mezclar](#limpiar-antes-de-mezclar)
  - [El fundido cruzado de audio](#el-fundido-cruzado-de-audio)
  - [El doblaje: ADR](#el-doblaje-adr)
  - [Mezclar de oído, con la escucha fija](#mezclar-de-oído-con-la-escucha-fija)
  - [La sonoridad del programa terminado](#la-sonoridad-del-programa-terminado)
  - [Lo que se revisa antes de dar la mezcla por buena](#lo-que-se-revisa-antes-de-dar-la-mezcla-por-buena)
- [6. Revisión de calidad final](#6-revisión-de-calidad-final)
  - [Qué es y quién la hace](#qué-es-y-quién-la-hace)
  - [La revisión en fichero: el control de calidad de la UER](#la-revisión-en-fichero-el-control-de-calidad-de-la-uer)
  - [Destellos y patrones](#destellos-y-patrones)
  - [El máster](#el-máster)
  - [La revisión, paso a paso](#la-revisión-paso-a-paso)
- [Aplicación práctica](#aplicación-práctica)
- [Normativa y recomendaciones técnicas que el tema cita](#normativa-y-recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Postproducción

### Qué es la postproducción

La postproducción es todo lo que se le hace al material después de registrarlo y antes de
entregarlo. Su lista:

| Proceso | Qué hace |
|---|---|
| Volcado e ingesta | Meter el material en el sistema, con sus metadatos |
| Montaje | Elegir y ordenar: qué se ve y cuánto dura |
| Grafismo | Rótulos, cabecera, cortinillas, infografía |
| Efectos visuales | Composición, borrados, elementos generados |
| Etalonaje | Ajustar la imagen y darle su aspecto |
| Montaje y mezcla de sonido | Diálogo, ambientes, efectos y música |
| Máster | El fichero o la cinta final, con sus especificaciones |

La grabación es, por tanto, la fase anterior: lo que se capta en el estudio o en exteriores (temas 6 y
7) llega a la postproducción como ficheros, y lo que no se grabó bien no siempre se puede
arreglar después (oficio). La edición es la parte del montaje que elige, corta y ordena; la
postproducción de sonido engloba la edición y todo lo demás hasta la entrega.

Y una precisión que la propia palabra impone: en un directo no hay postproducción. Una
retransmisión se realiza en tiempo real, y el montaje ocurre en el mezclador mientras se emite. La
postproducción sólo existe cuando hay un después. En una retransmisión, lo más cercano a un después es la repetición: el servidor
de repetición (epígrafe 2) guarda lo grabado mientras se emite.

### El realizador responde del acabado

La ficha del Realizador del X Convenio colectivo de la RTVA (BOJA núm. 240, de 10-12-2014, anexo III,
p. 196) le encarga **«controlar la calidad y duración de los mismos»** (de los programas) y **«Dirigir
las tareas de montaje, postproducción y mezclas hasta su completo acabado.»**; la del Ayudante de
Realización (p. 111), **«Coordinar las tareas de montaje, postproducción y mezclas hasta el acabado
del programa.»** El reparto completo con el montador, el encargado de montaje y el ambientador musical
está en el tema 7 («Quién dirige el montaje: las fichas del convenio»), y las funciones del realizador
antes, durante y después de la grabación, en el tema 3.

Tres fichas más del mismo anexo nombran la calidad, cada una en un punto de la cadena:

| Puesto (código) | Lo que la ficha dice de la calidad |
|---|---|
| Encargado Operación y Montaje Vídeo (5212204) | **«Realizar el control técnico y/o calidad aplicando las posibles correcciones para su correcta emisión o venta.»** (p. 127) |
| Operador Montador de Vídeo (5212206) | **«Realizar el control técnico de calidad y corregir video y audio para su emisión y/o venta.»** (p. 190) |
| Editor de Continuidad (5302010) | **«Controlar la calidad de la imagen y del sonido de la emisión.»** y **«Coordinar la emisión de programas en directo con los realizadores / productores respectivos.»** (p. 125) |

Aplicación: el control técnico de la pieza lo hace la sala de montaje; el de la emisión, continuidad;
y quien responde de que el programa llegue acabado, con la duración pedida y con la calidad debida,
es el realizador, que dirige el montaje y la mezcla hasta el final. Las fichas son de 2014; si la
organización actual del trabajo es otra, no consta en lo publicado.

### Lo que pide la norma de enseñanza

El Real Decreto 1680/2011, de 18 de noviembre, que establece el título de Técnico Superior en
Realización de proyectos audiovisuales y espectáculos, dedica a esta materia el módulo 0907
**«Realización del montaje y postproducción de audiovisuales»**. Es norma de enseñanza: dice qué
aprende quien se forma para el oficio, no cómo se organiza la RTVA. Sus resultados de aprendizaje
siguen casi uno a uno las rúbricas de este tema:

| Resultado (RA) del módulo 0907 | Rúbrica |
|---|---|
| RA 2: **«Realiza el montaje/postproducción de productos audiovisuales, aplicando las teorías, códigos y técnicas de montaje y evaluando la correspondencia entre el resultado obtenido y los objetivos del proyecto.»** | Montaje, edición y mezcla |
| RA 3: **«Genera y/o introduce en el proceso de montaje los efectos de imagen, valorando las características funcionales y operativas de las herramientas y tecnologías estandarizadas.»** | Efectos y grafismo |
| RA 5: **«Realiza los procesos de acabado en la postproducción del producto audiovisual, reconociendo las características de la aplicación de las normativas de calidad a los diferentes formatos de registro, distribución y exhibición.»** | Revisión de calidad final |

Los criterios de evaluación de cada resultado se citan en su epígrafe.

## 1. Montaje

### Montar

Montar es elegir qué planos se ven, en qué orden y cuánto dura cada uno. Y con eso se construyen
tres cosas a la vez: el relato, el tiempo y el ritmo.

El lenguaje del montaje ya se ha estudiado: el corte y dónde se corta, el *raccord*, la elipsis, el
montaje interno y externo, el narrativo y el expresivo, el alternado y el paralelo, el efecto
Kuleshov y las estructuras narrativas están en el tema 1, con su fuente. Aquí va lo que ese tema no
da: la clasificación de Eisenstein y el montaje como proceso de trabajo, del primer armado a la pieza
acabada.

El módulo 0907 del RD 1680/2011 pide al realizador que juzgue el montaje, no sólo que lo haga:
**«Se ha verificado la correspondencia entre el montaje realizado y la documentación del
rodaje/grabación, detectando los errores y carencias del primer montaje y proponiendo las acciones
necesarias para su resolución.»** (RA 2.g) y **«Se han valorado los resultados del montaje,
considerando el ritmo, la claridad expositiva, la continuidad visual y la fluidez narrativa, entre
otros parámetros, y se han realizado propuestas razonadas de modificación.»** (RA 2.h).

### Los cinco métodos de montaje de Eisenstein

Serguéi M. Eisenstein, cineasta ruso, clasificó el montaje en cinco métodos. La
fuente que aquí se ha leído es una tesis universitaria que los expone citando *Film Form*
(edición de Jay Leyda, Nueva York, 1949): J. M. Todd, *Eisenstein's Film Theory of Montage and
Architecture*, Georgia Institute of Technology, 1989. De ella: **«Five specific categorized levels of
montage were developed by Eisenstein; four of which (metric, rhythmic, tonal, and overtonal) could be
described as purely physiological, while the fifth (intellectual) was to direct not only emotions but
the whole thought process.»** (cinco niveles; cuatro, puramente fisiológicos, y el quinto, el
intelectual, dirige no sólo las emociones sino el pensamiento; p. 8).

| Método | Qué ordena el corte |
|---|---|
| Métrico | La duración absoluta de los planos, medida en fotogramas: el corte se decide con una regla, sin mirar el contenido |
| Rítmico | La duración en relación con el movimiento interno del plano: el contenido interviene en la medida |
| Tonal | El tono emocional dominante del plano: su luz, su textura, su carga |
| Sobretonal | El conjunto de todos los estímulos a la vez: la resultante de lo métrico, lo rítmico y lo tonal |
| Intelectual | El choque de dos imágenes para producir un concepto que no está en ninguna de las dos |

Lo que la tesis dice de cada uno:

- Métrico: **«the fundamental criterion for construction is the absolute lengths of the film
  fragments»** (el criterio es la duración absoluta de los fragmentos), y, citando a Eisenstein, **«the
  content within the frame of the (film fragment) is subordinated to the absolute length of the (film
  fragment)»** (el contenido del cuadro se subordina a la duración). Variar la duración de los planos sin
  romper las proporciones de la fórmula da grados de tensión, de la calma al caos (pp. 10-11).
- Rítmico: el contenido del cuadro pesa tanto como la duración, y la tensión sale **«by the conflict
  between the length of the film fragment and the movement within the frame»** (del choque entre la
  duración del plano y el movimiento dentro de él; p. 13).
- Tonal: su base es el **«emotional sound»** (el «sonido emocional») del fragmento, que se puede medir:
  la luz da una «tonalidad luminosa» y los ángulos agudos del cuadro, una «tonalidad gráfica» (p. 15).
- Sobretonal: **«Overtonal montage is distinguished by the collective characteristics of metric,
  rhythmic and tonal montage when they are brought together within the film fragment.»** (reúne los
  tres anteriores; p. 17).
- Intelectual: no busca un efecto fisiológico sino psicológico; es **«an activity of mental fusion or
  synthesis, through which particular details are united at a higher level of thought»** (una síntesis
  mental que une los detalles en un nivel superior de pensamiento; p. 20). El ejemplo de la tesis, en
  *El acorazado Potemkin* (1925): una secuencia de tres planos en la que un león de piedra se levanta
  de su sueño y ruge, metáfora de la indignación del pueblo (p. 20).

El tema 1 da, con el manual de la Universidad Miguel Hernández, que el rítmico incluye al métrico y
que el montaje intelectual es otro nombre del ideológico: las dos cosas casan con esta clasificación.
Los ejemplos de cada método son los de la tesis; la obra de Eisenstein no se ha leído.

### Del primer armado al montaje final

Qué es un montaje preliminar: el primer armado de la película, con los planos en su orden y sin
efectos, sin música y sin ajustar. Su objeto es comprobar que la historia se entiende. La regla: el
montaje preliminar es la primera vez que la película existe entera. Todo lo que se hace sobre una
película entera va después (oficio).

### Offline y online

La idea de los *proxies* es antigua y tiene nombre propio en el oficio: *offline* y *online*.

| Fase | Qué es | Con qué material |
|---|---|---|
| *Offline* | El montaje: decidir qué va, en qué orden y con qué duración | Material de baja resolución, ligero y rápido |
| *Online* | El acabado: efectos, grafismo, etalonaje y salida | El material de resolución completa |

Por qué existió la separación: cuando el disco era caro y lento, montar con material ligero era la
única forma de trabajar, y al final se reconformaba la secuencia contra el material bueno. Hoy la
separación se mantiene en producciones grandes, no por el disco, sino porque el montaje se hace en
una sala y el acabado en otra.

Aplicación: el realizador revisa el primer montaje contra el guion y el minutado (tema 7, «De la
grabación al montaje: los documentos»), pide los cambios de estructura cuando todavía son baratos,
y sólo cuando la estructura está cerrada entra el acabado (color, efectos, grafismo, mezcla).
Cambiar el orden de los bloques después de etalonar y mezclar obliga a rehacer parte de ese trabajo
(oficio).

## 2. Edición

### Lineal y no lineal

| | Edición lineal | Edición no lineal |
|---|---|---|
| Soporte | Cintas físicas | Archivos digitales |
| Cómo se monta | Copiando de una cinta a otra, en orden | Ordenando referencias a los archivos |
| Cambiar algo del medio | Obliga a rehacer desde ahí | No afecta a nada más |
| Acceso | Secuencial: hay que rebobinar | Aleatorio: cualquier fotograma, al instante |
| Generaciones | Cada copia pierde calidad | Ninguna pérdida: no se copia, se referencia |

La edición lineal utiliza cintas físicas, mientras que la no lineal se basa en archivos digitales:
es la diferencia de raíz, y todas las demás salen de ella. La palabra «lineal» no se refiere a la
duración ni al relato: se refiere al acceso. Una cinta se recorre en línea; un disco, no.

La fila de las generaciones tiene una salvedad: no se copia mientras se monta, pero sí se recodifica
cuando se calcula un efecto o se exporta la pieza (epígrafe «El *render*»), y por eso importa con qué códec
se trabaja (epígrafe «El códec con que se monta»).

### Los programas

El enunciado no nombra programa, ni la ficha del puesto tampoco, y qué sistema usa CSRTV no consta
en un documento publicado. El tema toma los tres cuya documentación se ha leído —Avid Media Composer,
DaVinci Resolve de Blackmagic Design y Adobe Premiere (Premiere Pro en las páginas de ayuda de 2025)— y se queda con lo que los
tres comparten. Cada uno llama a las cosas a su manera:

| Pieza | Media Composer | Resolve | Premiere |
|---|---|---|---|
| El trabajo guardado | Proyecto | Proyecto (.drp) | Proyecto |
| Carpeta de clips | *Bin* | *Bin* del *Media Pool* | *Bin* del panel Proyecto |
| El montaje | Secuencia | *Timeline* | Secuencia |
| El clip original | *Master clip* | Clip del *Media Pool* | Clip |
| Salida | *Export* | Página *Deliver* | *Export* / Media Encoder |

Media Composer y el servidor de repetición de EVS son los dos productos que se toman aquí como
ejemplo de montaje y de repetición; lo que se dice de ellos sale de su documentación, citada con su
versión, y sirve para entender las operaciones, no para suponer qué equipos tiene CSRTV.

### Ajustar un corte: el *trim*

Trimar es mover el punto de entrada o de salida de un plano que ya está en el montaje, alargándolo o
acortándolo, y decidir qué pasa con el plano vecino (oficio). Media Composer tiene para ello un modo
propio: **«Trim mode provides a unique set of controls within the Composer window for fine-tuning
edits with various trim procedures.»** (el modo *Trim* reúne los controles para afinar los cortes;
*Media Composer User's Guide*, 1999, p. 522). En su presentación grande (*Big Trim*), los monitores de
fuente y de secuencia se sustituyen por los cuadros del plano que sale y del que entra: **«In Big Trim mode,
the Source and Record monitors are replaced by displays of outgoing and incoming frames.»** (p. 523).

| Modalidad | Qué hace con la duración total |
|---|---|
| Trim de un lado | Alarga o acorta un plano y desplaza todo lo que sigue: la secuencia cambia de duración |
| Trim de los dos lados | Lo que uno gana, el otro lo pierde: la duración total no cambia |
| Deslizar el contenido | El plano ocupa el mismo hueco con otro trozo de la toma: no cambia nada fuera |

La guía de Avid da nombre a cada modalidad:

- Un lado o los dos. Se recorta el lado A (el plano que sale), el B (el que entra) o los dos; el
  cursor cambia a **«a single-roller A-side, single-roller B-side, or double-roller icon»** (p. 531).
  El de dos rodillos (*dual-roller*) añade o quita **«the same number of frames on both sides of a
  transition»** (el mismo número de cuadros a cada lado del corte; p. 526).
- Deslizar (*slip*) y desplazar (*slide*). Los dos ajustan un plano al cuadro **«without affecting the
  overall duration of the sequence or the sync relationships between multiple tracks»** (sin cambiar
  la duración de la secuencia ni la sincronía entre pistas; p. 540). En el *slip* cambia el contenido
  del plano y no lo que lo rodea: **«only the contents of the clip are adjusted»**; en el *slide*, el
  plano queda fijo y se recorta lo de antes y lo de después: **«the clip remains fixed while the
  footage before and after it is trimmed»** (p. 543).

La regla que las separa (oficio): trimar no cambia lo que se ve dentro del plano, sino dónde empieza y
dónde acaba; cambiar un plano por otro es sustituir, y cambiar su velocidad para que encaje es un
efecto de tiempo (epígrafe 3).

### Del montaje al original: el *match frame*

Un montaje se trabaja con dos monitores: el de fuente, que enseña el material bruto, y el de
secuencia, que enseña el montaje. Buscar el fotograma correspondiente (*match frame*) va del segundo
al primero: se está mirando un cuadro montado y se quiere ver de dónde salió. Media Composer lo
describe así: **«The Match Frame function locates the source footage for the frame currently
displayed in either the Source or Record monitor, loads it into the Source monitor, cues to the
matching frame, and marks an IN point.»** (localiza el material original del cuadro, lo carga en el
monitor de fuente, lo sitúa en ese cuadro y marca una entrada; p. 431). La operación inversa
(*Reverse Match Frame*) lleva la secuencia al cuadro que coincide con el del material de fuente
(p. 431).

Para qué sirve (oficio): alargar un plano cuando el original tiene más material del que se montó,
volver a montar un plano con otra entrada, o encontrar de qué toma sale un cuadro. El *match frame*
dice de dónde viene un plano; el *trim* decide cuánto de él se usa.

### El coleo

El coleo es el margen de material que se deja antes del primer fotograma útil y después del último:
el RD 1680/2011 pide minutar de cada pieza su **«coleo de entrada, coleo de salida»** (módulo 0905,
RA 1.b). El de salida sirve para que quien emita o quien monte tenga con qué encadenar, con qué corregir un desfase y con qué cubrir un retardo.
Un vídeo sin coleo de salida obliga a cortar exactamente en el último fotograma, y en directo eso es un riesgo;
en la jerga se dice que el vídeo «acaba a capón» (oficio). El parte de emisión de una pieza recoge sus
coleos y pies (tema 7, «La pieza terminada: máster, parte de emisión y visionado»). Las colas que necesita una transición dentro del
montaje son otra cosa y van en el epígrafe 3.

### El *render*

Hacer *render* es el cálculo que el sistema de edición no lineal tiene que hacer en los efectos para
hacerlos visibles y utilizables.

Por qué hace falta. Un montaje sin efectos se reproduce leyendo los archivos y cortando entre ellos:
eso el ordenador lo hace al vuelo. Pero una transición, un rótulo, una corrección de color o una
composición no existen como archivo: hay que calcular cada fotograma. Cuando el cálculo no da tiempo
a hacerse mientras se reproduce, hay que hacerlo antes y guardarlo. Eso es renderizar.

Resolve lo organiza como caché de *render* con dos modos. El inteligente: **«Choosing Smart triggers
a variety of automatic caching behaviors designed to optimize playback in DaVinci Resolve by
rendering clip formats, grading operations, and timeline effects that are known to be
performance-intensive»** (calcula por su cuenta los formatos, correcciones y efectos que se sabe que
pesan); el de usuario, que **«does not automatically cache clips in processor-intensive formats»**
y deja al montador marcar qué se calcula (p. 209). Y separa la caché de los *proxies*: la caché
**«is designed to improve the real time performance of clips that have enough computationally
intensive effects […] to slow playback»** y **«only works with the project it was made for»** (sólo
sirve al proyecto para el que se hizo; p. 222). El *render* es, por tanto, material desechable: se
puede borrar y rehacer, y no se archiva como si fuera material de origen (oficio).

### El códec con que se monta

Un mismo material pasa por códecs distintos según la fase, y cada uno responde a una necesidad
distinta (oficio):

| Fase | Qué se pide al códec | Ejemplos citados en este tema |
|---|---|---|
| Captación | Mucha calidad en poco espacio de tarjeta | Los formatos de cámara (AVC-Intra, XDCAM, H.264/H.265 de cámara) |
| Montaje y acabado | Aguantar decodificación rápida, efectos y varias generaciones sin degradarse | DNxHD y DNxHR, ProRes, sin comprimir |
| Montaje ligero | Poco flujo para reproducir con fluidez | DNxHD 36, ProRes Proxy, DNxHR LB, H.264 de *proxy* |
| Entrega | Lo que pida el destino: emisión, archivo o plataforma | Tema 14 |

Avid explica así por qué no basta el códec de cámara: **«HD camera compression formats are
efficient, but simply aren't engineered to maintain quality during complex postproduction effects
processing. Uncompressed HD delivers superior image quality, but data rates and file sizes can stop a
workflow dead in its tracks.»** (los formatos de cámara son eficientes pero no están pensados para
mantener la calidad en una posproducción con efectos; el HD sin comprimir tiene la mejor imagen, pero
su flujo y el tamaño de los ficheros atascan el trabajo). Su respuesta es un códec intermedio pensado
para editar: **«Avid DNxHD encoding is specifically designed for nonlinear editing and complex
multi-generation compositing common in today's collaborative post production and broadcast news
environments.»** (*Avid DNxHD Technology*, 2012).

El formato de codificación, el códec y el contenedor, la resolución, la compresión y los formatos de
entrega son el tema 14.

### El código de tiempo

El código de tiempo es la etiqueta que numera cada cuadro en horas, minutos, segundos y cuadros
(HH:MM:SS:CC), y es el instrumento de sincronización de toda la cadena (oficio). Viaja de dos
formas:

| Forma | Cómo viaja | Dónde se usa |
|---|---|---|
| LTC, longitudinal | Como una señal de audio, por un cable o canal propio | Entre equipos: cámara, grabador de sonido, generador |
| VITC, vertical | Dentro de la propia señal de vídeo, en el intervalo vertical | Dentro de la cadena de vídeo |

Una palabra de LTC ocupa 80 bits por cuadro; de ellos, 32 son bits de usuario (oficio; la norma
SMPTE que lo fija no se ha leído).

- DF o NDF sólo importa a 29,97 y 59,94: como esa cadencia no es entera, un código que cuente 30
  cuadros por segundo se adelanta al reloj, y el *drop frame* salta números de cuadro para
  corregirlo (no salta imágenes). A 25 y 50 cuadros no hay nada que corregir.

En la estación de trabajo, el código de tiempo es la regla sobre la que se coloca todo: la sesión
empieza en el mismo código que el vídeo del programa, y cada fichero grabado con código se puede
colocar en su sitio exacto (oficio). Cómo se sincroniza en rodaje un sonido grabado aparte —sistema
único o doble, claqueta— está en el tema 11 («Sistema único o doble sistema»).

### La aritmética del código de tiempo

La duración entre dos códigos se calcula restando campo a campo, de derecha a izquierda, con
acarreos, y sabiendo a qué cadencia va el material (cálculo). Ejemplo a 25 cuadros por segundo, de
00:47:17:23 a 01:23:54:00:

| Campo | Operación | Resultado |
|---|---|---|
| Cuadros | 00 − 23 no se puede: se toma prestado un segundo (25 cuadros) | 25 − 23 = 2 |
| Segundos | 54 − 1 prestado = 53; 53 − 17 | 36 |
| Minutos | 23 − 47 no se puede: se toma prestada una hora | 83 − 47 = 36 |
| Horas | 1 − 1 prestada = 0; 0 − 0 | 0 |

La resta da 00:36:36:02. Si el último código se cuenta como parte del plano (duración inclusiva), se
suma un cuadro: 00:36:36:03. A 24 o a 30 cuadros el campo de cuadros saldría distinto, porque el
préstamo es de 24 o de 30.

El RD 1680/2011 lo pide en el montaje: **«Se ha aplicado adecuadamente un offset de código de tiempos
en una edición y se ha verificado la calidad técnica y expresiva de la banda sonora y su perfecta
sincronización con la imagen y, en su caso, se han señalado las deficiencias.»** (módulo 0907,
RA 2.f). Y el Libro de Estilo de Canal Sur, en la entrevista con varias cámaras: **«El código de
tiempo que se aplicará será idéntico para facilitar el montaje final.»** (3.17.1.5, p. 61).

### Montar en red: el material compartido

La costumbre del sector reserva PAM para el sistema que gestiona el material mientras se produce
(brutos, *proxies*, secuencias en curso, varias personas trabajando a la vez sobre lo mismo) y MAM para
el que gestiona el material terminado y su archivo. Es una distinción de oficio: ninguna fuente
consultada la define, y hay fabricantes que llaman MAM a todo el sistema.

Un ejemplo de producto. Avid presenta con página propia la capa de producción de su
plataforma MediaCentral, llamada *Production Management*, que describe así (página de producto, leída el
25-09-2026):

- Seguimiento del material de principio a fin: **«Take control of your valuable media assets, tracking
  them from ingest to archive and every step in-between. From single resolution to multi-resolution»**.
- Muchas personas sobre el mismo material: **«From journalists working on news packages to researchers
  putting together roughcuts to craft editors delivering the final edit, scale up to hundreds of users
  working together»**.
- Permisos: **«From no access to having administrative rights, Production Management delivers highly
  sophisticated permissions management»**.
- Servicios automáticos: **«integrated media services such as transcoding, archiving, restoring, and
  more to automate manual processes»**.
- Almacenamiento compartido: **«Production Management is driven by Avid NEXIS shared storage»**.
- Búsqueda por metadatos desde los programas de edición: **«system and user generated metadata for
  ultra-fast searching across connected clients such as Media Composer, Adobe Premiere Pro and the
  web-based MediaCentral | Cloud UX.»**

Aplicación: en una redacción o en un programa grabado, el realizador puede pedir el material ya
catalogado en el sistema compartido y ver los montajes en curso sin copiar ficheros; la organización
concreta de CSRTV (qué sistema, qué permisos) no consta en lo publicado.

### El servidor de repetición

La repetición en directo se hace con un servidor de repetición. El que aquí se toma como ejemplo es el
de la marca EVS, con su mando de repetición y cámara lenta (LSM). Lo que
sigue es su arquitectura, como oficio.

Un servidor de repetición graba varias señales a la vez y permite reproducir cualquiera de ellas
desde cualquier punto mientras sigue grabando. Ésa es la máquina que hace posible la repetición de
una jugada quince segundos después de que ocurra, con la cámara que se quiera y a la velocidad que
se quiera.

Las tres cosas que lo distinguen de un sistema de edición corriente:

1. Graba y reproduce al mismo tiempo, sobre el mismo material.
2. Se maneja con un mando físico, no con ratón: una palanca y un puñado de teclas, porque
   en directo no hay tiempo para buscar un menú.
3. Su unidad de trabajo es el clip, marcado sobre la marcha con dos pulsaciones.

Dónde se usa: deportes, galas, cualquier directo con repetición o con cámara lenta. Y su
operador no es un montador que trabaja despacio: es un operador que decide en segundos, y por eso el
sistema está construido alrededor de la velocidad de acceso.

Una lista de reproducción es una secuencia de clips encadenados que se emiten uno detrás de otro.
Es lo que permite sacar en antena un resumen de jugadas sin ir cargándolas de una en una.

La línea de tiempo del sistema es un montaje con transiciones y efectos, un paso más allá de la
lista de reproducción, que sólo encadena.

| | Lista de reproducción | Línea de tiempo |
|---|---|---|
| Qué hace | Encadena clips uno detrás de otro | Monta: transiciones, efectos, audio |
| Canales mínimos | Uno | Dos |
| Para qué se usa | Resúmenes en directo | Piezas acabadas |

Por qué dos canales para la línea de tiempo, como razonamiento de oficio: una transición entre dos clips
es, por definición, dos imágenes a la vez, y un canal de reproducción sólo da una.

Dos operaciones más enlazan el directo con la postproducción:

- Los canales enganchados (*ganged*). En la suite IPDirector de EVS, varios canales de reproducción
  pueden ir agrupados, de modo que se controlan juntos: la pestaña correspondiente **«lists all player
  channels that have been ganged with the player channel currently associated to the Control
  Panel»**, y desde ella se puede **«Synchronize the timecode on all the ganged channels»** y
  desenganchar o volver a enganchar canales (*IPDirector Version 6.2, Control Panel User Manual*, junio
  de 2013, p. 30). Sirve para mover a la vez, con un mando, dos ángulos de la misma jugada (oficio).
- El volcado. Al acabar un partido, el operador vuelca a un servidor o a un soporte el material
  seleccionado durante el directo (jugadas, repeticiones, planos de recurso) para que el resumen y
  los programas posteriores lo tengan; en la jerga se llama *dump* (oficio: el término no se ha
  contrastado en la documentación de EVS). Es el enlace entre el directo y la sala de montaje.

## 3. Efectos

### Qué es un efecto en el sistema de edición

Todo lo que no es cortar un clip detrás de otro es un efecto: una transición, un cambio de tamaño o
posición, una corrección, una incrustación, un cambio de velocidad, un rótulo. Cada clip trae de
serie sus parámetros de composición, transformación y recorte; Blackmagic lo dice a propósito de los
títulos, que **«expose the same Composite, Transform, and Cropping parameter groups as any other
clip»** (cap. 56, p. 1213). Los efectos no existen como archivo: hay que calcularlos, y eso es el
*render* del epígrafe 2.

La clasificación práctica de oficio:

| Familia | Ejemplos |
|---|---|
| De composición | Incrustación (croma, luma, alfa), superposición de capas, opacidad, modos de fusión |
| De transformación | Tamaño, posición, rotación, recorte, estabilización |
| De tiempo | Cámara lenta o rápida, imagen congelada, marcha atrás |
| De imagen | Corrección de color, desenfoque, pixelado, nitidez, viñeta |
| De transición | Fundido, cortinilla (más abajo, «Las transiciones corrientes») |

El RD 1680/2011 enumera los efectos que el montaje ha de saber componer: **«Se ha realizado una
composición multicapa, combinando ajustes de corrección de color, efectos de movimiento o variación
de velocidad de la imagen (congelado, ralentizado y acelerado), ocultación/difuminado de rostros,
aplicación de keys y efectos de seguimiento y estabilización, entre otros.»** (módulo 0907, RA 3.b); y
el tipo de recorte: **«Se han determinado y generado las keys necesarias para la realización de un
efecto y se ha seleccionado el tipo (luminancia, crominancia, matte y por diferencia) y el procesado
más adecuado para cada caso.»** (RA 3.c).

### Incrustar

Incrustar es sustituir una parte de una imagen por otra. Es lo que pone un mapa del tiempo detrás de
un presentador, un rótulo sobre un plano o un fondo virtual detrás de un actor.

Las familias de incrustación, según de dónde salga el recorte (oficio):

| Familia | De dónde sale el recorte |
|---|---|
| *Chroma key* | Del color: se elige un color del fondo —verde o azul— y todo lo que lo tenga se vuelve transparente |
| *Luma key* | Del brillo: se recorta por encima o por debajo de un nivel de luminancia |
| Canal alfa | De un cuarto canal que viene con la imagen y dice, píxel a píxel, cuánto de opaco es |
| Máscara o *roto* | De una forma dibujada a mano, fija o animada |

Por qué el fondo es verde o azul: son los colores más alejados del tono de la piel humana, así que el
recorte se puede hacer sin comerse la cara del presentador. El verde se ha impuesto porque los
sensores digitales tienen el doble de fotositos verdes y por tanto entregan ese canal con menos ruido.

Tres consecuencias de oficio para el croma: el fondo ha de estar iluminado de forma uniforme; el
sujeto no puede llevar ropa del color del fondo, porque se volvería transparente; y la luz que rebota
del fondo tiñe los bordes del sujeto, que hay que limpiar después. Y una de señal: el recorte por color
necesita resolución de color, así que un material con submuestreo cromático fuerte (tema 14) da bordes
peores que uno 4:2:2 o 4:4:4.

Las tres señales de una incrustación (fondo, relleno y recorte) y el croma en el mezclador están en
el tema 9; el canal alfa y los ficheros gráficos que lo llevan, en el tema 12.

### La máscara

La función principal de una máscara de capa es ocultar o mostrar partes específicas de una capa sin
eliminar permanentemente el contenido.

Cómo funciona: la máscara es una imagen en escala de grises pegada a la capa. Donde la máscara es
blanca, la capa se ve; donde es negra, no; donde es gris, se ve a medias. Es exactamente un canal alfa
dibujado a mano.

El aviso de oficio: la máscara de capa es la razón por la que un fichero de grafismo se puede retocar
meses después. Quien recorte borrando píxeles entrega un trabajo que no se puede corregir, y en una
casa de televisión los rótulos se corrigen siempre.

### Fotogramas clave y curva de velocidad

Un fotograma clave —*keyframe*— marca un valor en un instante: dónde está el objeto, cuánto mide, qué
opacidad tiene. El programa calcula lo que hay entre dos fotogramas clave, y eso es la interpolación.

Y la curva de velocidad decide *cómo* se recorre ese trayecto. Con los mismos dos fotogramas clave,
el objeto puede ir a velocidad constante, arrancar despacio y acelerar, o llegar frenando.

La curva de velocidad modifica la rapidez con la que se mueve un objeto entre dos fotogramas clave:
los fotogramas clave fijan el qué y el dónde; la curva fija el cómo.

Y por qué esto importa en un rótulo de televisión: una entrada de rótulo con velocidad constante se
ve mecánica, y una con arranque y frenada se ve natural. La diferencia entre un grafismo profesional
y uno de aficionado está muchas veces sólo en la curva.

Resolve aplica la misma idea a las transiciones con su mando de suavizado (*Ease*): **«lets you apply
nonlinear acceleration to the beginning, ending, or overall duration of a transition»**, con las
opciones *None* (lineal), *In*, *Out*, *In & Out* y *Custom*, esta última con una curva que se ajusta
con fotogramas clave (cap. 55, p. 1199).

### Los efectos de tiempo

Un efecto de tiempo cambia la velocidad a la que se reproduce el clip. Resolve los define como los que
**«speeds up, slows down, or otherwise changes the playback speed of clips in the Timeline»** (cap. 58,
p. 1254), y da estas formas de hacerlos (pp. 1254-1264):

| Efecto | Cómo se hace en Resolve 21 |
|---|---|
| Velocidad constante (cámara lenta o rápida) | Orden *Change Clip Speed* (porcentaje, cuadros por segundo o duración), el mando *Speed %* del inspector, o las *Retime Controls* (Comando-R) arrastrando el borde del clip; también el montaje *Fit to Fill*, que ajusta el clip a una duración dada |
| Marcha atrás | Casilla *Reverse Speed*, que pone la velocidad en valor negativo, o *Reverse Segment* en las *Retime Controls*; las flechas se ven hacia la izquierda |
| Congelado | *Clip > Freeze Frame* (Mayúsculas-R) congela todo el clip en el cuadro que está bajo el cabezal; dentro de las *Retime Controls*, *Freeze Frame* congela sólo un tramo entre dos puntos de velocidad |
| Velocidad variable (rampa) | Puntos de velocidad (*speed points*): **«It takes a minimum of two speed points to create a speed effect.»** (p. 1259); el paso de una velocidad a otra se suaviza solo. Hay rampas y rebobinados preparados, y dos curvas: *Retime Frame*, que sí permite marcha atrás, y *Retime Speed*, que no (pp. 1260-1264) |

Cómo se calculan los cuadros que faltan o sobran es el proceso de reajuste (*Retime Process*), que se
fija para todo el proyecto (*Project Settings*, grupo *Frame Interpolation*) o clip a clip en el
inspector (p. 1265). Tiene tres opciones:

| Opción | Qué hace, según Blackmagic (p. 1265) |
|---|---|
| *Nearest* (el más próximo) | **«The most processor efficient and least sophisticated method of processing; frames are either dropped for fast motion, or duplicated for slow motion.»** |
| *Frame Blend* (mezcla de cuadros) | **«adjacent duplicated frames are dissolved together to smooth out slow or fast motion effects.»** Sirve también cuando el flujo óptico deja defectos |
| *Optical Flow* (flujo óptico) | **«The most processor intensive but highest quality method of speed effect processing. Using motion estimation, new frames are generated from the original source frames to create slow or fast motion effects.»** |

El flujo óptico tiene su límite: **«The result can be exceptionally smooth when motion in a clip is
linear. However, two moving elements crossing in different directions or unpredictable camera movement
can cause unwanted artifacts.»** Con él se elige además el modo de estimación de movimiento
(*Standard*, *Enhanced* y *Speed Warp*, este con el motor neuronal de Resolve), y el manual advierte
que **«the highest quality option isn't always the best choice for a particular clip»** (pp. 1265-1266).

Una cuenta (cálculo propio): un plano de 25 imágenes por segundo al 50 % dura el doble; con *Nearest*
cada cuadro sale dos veces (es el método que el manual llama menos sofisticado); con flujo óptico se generan cuadros intermedios
nuevos, y es la opción para una cámara lenta suave, comprobando que no deja defectos. El mismo
proceso decide cómo se convierten los clips de otra cadencia en una línea de tiempo mixta.

### Corte y transición

Adobe parte del corte: **«By default, placing one clip next to another in the Timeline panel results
in a cut, where the last frame of one clip is followed by the first frame of the next.»** La
transición es otra cosa: **«A transition is an effect added between pieces of media to create an
animated link between them.»** (ayuda de Premiere, «Transitions overview», actualizada el
07-01-2026). Blackmagic añade para qué sirve: **«Transitions provide another way of bridging the
change from one clip to another, and are often used to indicate a change in time or location when
changing scenes.»** (*Resolve 21*, cap. 55, p. 1194).

El corte es la unión por defecto y la más usada; la transición significa algo (paso del tiempo,
cambio de lugar, cierre) y por eso no se pone por adorno (oficio). El valor narrativo del corte, del
fundido y de la elipsis está en el tema 1.

### Las transiciones corrientes

| Transición | Qué hace | Uso corriente (oficio) |
|---|---|---|
| Fundido encadenado (*cross dissolve*) | La imagen que sale se desvanece mientras entra la siguiente | Paso de tiempo, cambio de secuencia, suavizar un salto |
| Fundido a negro y desde negro | La imagen va a negro o sale de él | Cierre y apertura; separar bloques |
| Cortinilla (*wipe*) | Una imagen empuja o barre a la otra con una forma | Separadores, deportes, promociones; casi nunca en una noticia |
| Transición de audio (fundido cruzado) | Un sonido baja mientras sube el otro | Evitar el golpe de un corte de sonido |

Resolve agrupa las suyas en **«various forms of the traditional cross dissolve to different types of
wipes»**, y admite transiciones de otros fabricantes (**«third‑party OpenFX transitions»**) (p. 1194).

El fundido encadenado tiene variantes que cambian cómo se mezclan las dos imágenes. En Resolve hay
seis estilos (p. 1198); las dos básicas:

- **«Video: A simple linear dissolve; the outgoing clip fades out as the incoming clip fades in.»**
- **«Film: A logarithmic dissolve, simulating film dissolves as created by an optical printer.»**

Las otras cuatro usan modos de fusión: la aditiva **«seems to brighten at the halfway point»** (se
aclara a mitad) y la sustractiva **«seems to darken at the halfway point»** (se oscurece a mitad); las
de altas luces y sombras destacan lo más claro o lo más oscuro de cada plano.

### Las colas

Una transición necesita imagen que no se ve en el corte. En un corte, el plano que sale termina en el
punto de edición y el que entra empieza ahí; en un fundido de un segundo centrado, durante medio
segundo antes del corte ya se está viendo el plano que entra, y durante medio segundo después se sigue
viendo el que sale. Esos cuadros de más, que están en el material pero fuera del montaje, son las colas
(*handles*) (oficio).

Qué pasa si no hay colas: Resolve pone la transición con la duración estándar, **«which defaults to
one second, or however long the overlapping handles of the selected edit point allow»** (p. 1196); y
si no hay cuadros suficientes para la duración estándar y la transición se añade con el atajo
(Comando-T) o con el menú contextual del punto de edición, pregunta con tres opciones (p. 1197):

| Opción | Qué hace |
|---|---|
| *Trim Clips* | **«automatically trim the incoming and outgoing sides of each selected edit point to create the overlap needed»**: recorta los planos para sacar las colas |
| *Skip Clips* | **«Don't add transitions to the selected edit points that lack the appropriate overlap.»** |
| *Cancel* | Cancela la operación |

Adobe da un consejo preventivo: **«Before you apply a transition, trim the clips. Then,
apply the transition. The more you trim, the more availability of frames you can use in the
transition.»** Y la regla: **«Trim at least 15 frames off of each clip for a centered 1:00
transition.»** La cifra es de Adobe; «1:00» se lee como un segundo en código de tiempo, y 15 cuadros por lado son
medio segundo a 30 imágenes por segundo (lectura propia: Adobe no da la cadencia). La cuenta general (cálculo propio):
para una transición centrada de duración D, cada plano necesita al menos D/2 de cola; a 25 imágenes por
segundo, una de un segundo pide 12 o 13 cuadros por lado, y una de dos segundos, 25.

Las colas son también lo que se deja al exportar o conformar un montaje (epígrafe 1, «Offline y online»): sin colas no se
puede alargar un plano ni poner un fundido en la fase siguiente.

### El color: corrección y etalonaje

El etalonaje es la fase de posproducción en la que se ajusta la imagen de toda la producción para
que sea coherente y esté a la altura de un patrón. La palabra viene del francés *étalonnage* y del
*étalon*, «patrón» o «medida de referencia»: etalonar es llevar algo a un patrón.

Lo que se hace en un etalonaje, por orden:

| Fase | En qué consiste |
|---|---|
| Etalonaje técnico o primario | Poner cada plano en su sitio: niveles de negro y de blanco dentro del rango legal (tema 14), balance de blancos, exposición |
| Igualación | Que dos planos de la misma escena, rodados con distinta luz o distinta cámara, parezcan el mismo momento |
| Etalonaje creativo o secundario | Dar el aspecto: la dominante, el contraste, las zonas concretas de la imagen |
| Comprobación de entrega | Que el resultado cumpla las especificaciones técnicas del destino |

Un etalonaje no toca sólo el color: pone los niveles dentro del rango legal, iguala la exposición
entre planos, comprueba que la señal cumpla la especificación de entrega y, además, da el aspecto.
La colorimetría es uno de esos parámetros técnicos, no todos. La tabla y la definición son de oficio.

En el lenguaje de la sala, «corrección de color» y «etalonaje» se usan casi como sinónimos. Cuando se
distinguen, corregir es lo técnico (llevar el plano a lo correcto) y etalonar incluye además el
aspecto (oficio). Blackmagic llama a todo el proceso *color correction* o *color grading*, y lo ordena por
objetivos: sacar lo mejor de cada plano, destacar lo importante, respetar lo que el espectador espera
ver, igualar las escenas, dar estilo y el control de calidad (cap. 125, pp. 3086-3095; los cuatro
primeros se desarrollan más abajo).

El RD 1680/2011 los pone en el acabado: **«Se han aplicado, al montaje final, los procesos técnicos
de corrección de color y etalonaje.»** (módulo 0907, RA 5.c), y en los efectos: **«Se ha ajustado e
igualado la calidad visual de la imagen, determinando los parámetros que hay que modificar y el nivel
de procesado de la imagen, con herramientas propias o con equipos y software adicional.»** (RA 3.e).

### Medir antes de tocar: los monitores de señal

El color no se corrige a ojo sobre un monitor cualquiera: se mide. Los niveles
legales de la señal son materia del tema 14. Aquí se ve lo que cada instrumento dice cuando se corrige. Resolve ofrece
cinco: **«There are five available video scopes»** (cap. 127, p. 3150), que son el monitor de forma
de onda (*Waveform*), el desfile (*Parade*), el vectorscopio (*Vectorscope*), el histograma y el
diagrama de cromaticidad de la CIE (Comisión Internacional de la Iluminación).

| Instrumento | Qué muestra (Resolve 21, pp. 3150-3152) | Para qué se usa al corregir |
|---|---|---|
| Forma de onda | **«Overlays waveform analyses of the Y (luma/luminance), CBCR […], or RGB (red, green, and blue) channels over one another so that you can see how they align.»** | Ver dónde están los negros y los blancos y si la señal se sale del rango |
| Desfile | **«shows separate waveforms side by side that analyze the strength of individual video signal components»**; puede analizar RGB, YRGB e Y'CBCR | Comparar las alturas de R, G y B en altas luces, medios y sombras **«for the purposes of identifying color casts and performing scene-by-scene correction»** |
| Vectorscopio | **«Measures the overall range of hue and saturation within an image»** | Ver el matiz (el ángulo) y la saturación (la distancia al centro) |

Cómo se leen las tres cosas que más se preguntan:

- Contraste en el desfile: la base de las gráficas es el punto negro y la cima el punto blanco, y
  **«Tall parade graphs indicate a wide contrast ratio, while short parade graphs indicate a narrow
  contrast ratio.»** Gráficas altas, mucho contraste; bajas, poco.
- Dominante en el desfile: si en una zona que debería ser neutra (un blanco, un gris) las tres gráficas
  no están a la misma altura, hay dominante del color cuya gráfica sobresale (oficio, sobre lo que
  dice el manual).
- Saturación y dominante en el vectorscopio: **«less saturated colors remain closer to the center of
  the vectorscope, which represents 0 saturation»**; y si el centro de la gráfica no está centrado en
  la cruz, **«the direction in which it leans lets you know that there's a color cast (tint) in the
  image»**. El vectorscopio lleva las dianas de las barras de color al 75 % y una línea opcional de
  referencia del tono de piel: **«75 percent color bar targets indicating the angle of each of the
  primary and secondary colors around the edge of the graph, and an optional skin tone reference
  graticule (otherwise known as the In-phase reference)»**.

Un aviso para el material HDR: si se activan los monitores HDR sin gestión de color de Resolve, la
forma de onda enseña niveles HDR aunque la salida sea Rec. 709, **«and thus not be 100% accurate»**
(p. 3147). En HDR se mide con la escala de la curva con la que se trabaja (tema 14).

### Las LUT

Las LUT son tablas de consulta para transformar el color de una imagen.

Cómo funcionan, en una frase: para cada combinación de entrada de rojo, verde y azul, la tabla da una
combinación de salida. No calcula: consulta. De ahí el nombre, *look-up table*.

| Tipo | Qué hace |
|---|---|
| LUT técnica o de conversión | Traduce entre espacios: de logarítmico a Rec. 709, de una gama a otra. Es corrección, no estilo |
| LUT creativa o de *look* | Aplica un aspecto: una paleta, un viraje, un aire de época |
| LUT 1D | Una tabla por canal: cambia curvas de tono, no relaciones entre canales |
| LUT 3D | Una tabla sobre el cubo RGB: puede cambiar el tono y la saturación, no sólo el brillo |

La tabla es de oficio. Blackmagic lo dice así: **«LUTs are simply files, similar to plugins but far
more focused and with no user interface, that specify image processing operations. […] The
traditional approach is to use a 1D table or 3D "cube" of pre-calculated values to perform an image
color transform.»** (cap. 150, p. 3545). Hay formatos más nuevos que no son tablas sino fórmulas:
**«newer LUT formats including CLF and DCTL let you use mathematical scripts to process an image»**.

Una tabla de consulta es estática: los mismos valores de entrada dan siempre los mismos de salida, no
dependen de la escena ni del momento (oficio). Sus usos:

| Uso | Qué hace |
|---|---|
| Calibrar un monitor | Corregir las desviaciones del panel para que enseñe el color correcto |
| Transformar el espacio de color | Pasar de un espacio a otro: de un logarítmico de cámara a la Rec. 709, por ejemplo |
| Previsualizar un aspecto | Ver en rodaje cómo quedará la imagen etalonada |
| Fijar un aspecto | Aplicar la misma corrección a todo el material de una serie |


Dos avisos que separan al montador del aficionado:

1. Una LUT no corrige un plano mal expuesto: aplicada sobre material mal expuesto exagera el error en
   vez de corregirlo (oficio).
2. Una LUT 3D recorta lo que se sale de su rango: **«when a 3D LUT is fed values that are outside of
   the range that LUT is designed to handle, the out-of-range data will be clipped»**. El ejemplo de
   Blackmagic es el vídeo con superblancos que entra en una LUT pensada para rango completo, que
   **«will clip the super-white part of the signal»** (p. 3546). Para eso existe la *shaper LUT*, que
   antepone una 1D que encaja la señal en el rango de la 3D.

### Primaria y secundaria

La corrección de color se divide en dos niveles (oficio, con los términos que usa Blackmagic):

| Nivel | Qué toca | Herramientas |
|---|---|---|
| Primaria | La imagen entera: negros, blancos, contraste, balance, saturación | Ruedas de color y barras (*lift*, *gamma*, *gain*, *offset*), temperatura, matiz, contraste, saturación |
| Secundaria | Una parte de la imagen: una zona, un color, un objeto | Ventanas (*windows*), cualificadores (HSL, RGB, luminancia) y curvas de matiz |

Primero se hace la primaria de todos los planos y después la secundaria donde haga falta: no se
aísla un color hasta que el plano entero está equilibrado (oficio).

### La corrección secundaria: ventanas y cualificadores

La secundaria aísla una parte de la imagen para corregir sólo esa parte. Blackmagic la compara con la
ecualización del sonido: **«It's similar in concept to equalization in audio mixing, in that you're
choosing which color values to boost or suppress»** (cap. 125, p. 3089). Dos maneras de aislar:

- Por forma, con una ventana: **«surrounding a specific part of the image with a window, which lets
  you restrict specific adjustments made to the inside and outside of the window's shape»**. Sirve
  para dirigir la mirada: oscurecer los bordes, aclarar una cara. Si el sujeto se mueve, la ventana
  tiene que seguirlo (seguimiento o fotogramas clave; oficio).
- Por color, con un cualificador: **«HSL Qualification is effectively a chroma keyer that lets you
  sample the image to create a key that's used to define where to apply a specific correction.»**
  (p. 3090). Es un croma («Incrustar») que no sustituye el fondo sino que decide dónde se corrige. Los
  hay por matiz, saturación y luminosidad (HSL), por RGB y por luminancia.

Qué se corrige en secundaria lo explica el «color de memoria»: **«people have finely tuned
expectations for the hues of particular subjects, such as flesh tone, foliage greens, and sky
blues»**. Si la piel, la vegetación o el cielo se apartan de lo que el espectador espera, algo le
parece falso. Los ejemplos de Blackmagic son los dos casos típicos: la piel con un tinte verdoso
**«you can isolate the color of that actor's skin and adjust it to a healthier hue»**, y el cielo
lavado, en el que se aísla **«that wedge of blue»** para devolverle el color (p. 3090).

### Igualar los planos

En una noticia se montan planos grabados con distintas cámaras, luces y horas. Igualarlos es tarea
fundamental: **«Small or large, unintended variations from one shot to the next can call undue
attention to the editing»**, y el trabajo está hecho cuando **«the color in the scene flows
unnoticeably from one clip to the next»** (cap. 125, p. 3091). Las herramientas:

- Comparar con una imagen fija guardada (*Gallery* en Resolve), a pantalla partida o alternando.
- Copiar la corrección de un plano a otro, o agrupar los planos parecidos para corregirlos juntos:
  **«by copying them from clip to clip, or by linking similar clips, either automatically, or manually
  using groups»** (p. 3092).

El orden práctico de oficio: primero la referencia (el plano principal, normalmente el del total o el
del presentador), después los demás contra ella, y en los monitores de señal antes que a ojo. En una
entrevista a dos cámaras, la piel del entrevistado ha de caer en el mismo punto del vectorscopio en los
dos planos.

La igualación empieza en la grabación: con varias cámaras, el Libro de Estilo pide que **«el
realizador preverá que los planos respectivos sean técnicamente compatibles y uniformes»**
(3.17.1.5, p. 61); lo que no se iguló al grabar se iguala en la sala, con más trabajo (oficio).

### Los efectos y la información

El Libro de Estilo de Canal Sur pone límites a los efectos en la información, y el montador es quien
los aplica:

- Ocultar para proteger. En imágenes duras, **«El contenido se puede presentar con planos abiertos,
  impersonales y neutros, o se pueden ocultar parcialmente con medios técnicos.»** (9.9.2, p. 167). Y
  para las personas más expuestas: **«La imagen de menores de edad, de víctimas de un delito, de
  testigos protegidos o de miembros de las fuerzas de seguridad y su familia no se emitirán si existe
  un factor de riesgo. Sus rostros serán cubiertos o tramados y no se aportarán detalles sobre su
  identidad o paradero.»** (9.9, p. 166). El tramado (pixelado o desenfoque) es un efecto con máscara
  que sigue la cara: si la persona se mueve, la máscara ha de seguirla en todo el plano, y se revisa fotograma a
  fotograma en los giros y en las entradas y salidas de cuadro (oficio).
- No acentuar. **«las posibilidades de edición (ralentización, imagen congelada...) pueden generar un
  efecto reprobable y no debemos optar por ello si sólo sirve para acentuar la morbosidad de una
  historia.»** (9.9.2, p. 167).
- Rotular lo que no es real o no es de hoy. Las reconstrucciones llevan **«el rótulo 'reconstrucción'
  durante todo el tiempo en el que las imágenes ‘falsas’ estén en pantalla»** (3.2.2, p. 46), y las
  imágenes de archivo que ilustran reportajes sobre delincuencia, malos tratos o asuntos judiciales
  **«también serán ‘tratados’ en el proceso de
  edición»**, con el rótulo de **«‘Archivo’»** todo el tiempo que estén en pantalla (9.9.1, p. 166).

La selección de planos y el tratamiento informativo se desarrollan en el tema 1, y el tratamiento responsable de imágenes, en el tema 16.

Hay límites que no pone el programa sino la información. El Libro de Estilo de Canal Sur, al tratar
los reportajes de sucesos en su capítulo de malos tratos (9.2), advierte contra los recursos que
convierten la noticia en ficción: **«La estética y la narrativa propias de reportajes de sucesos deben
acometerse con cuidado. La imagen oscilante ‘cámara en mano’, una
música tópica, un virado a blanco y negro... evocan inevitablemente escenas ficticias de misterio,
terror... o de una película. Y la información sólo habla de realidad.»** (9.2.12.4, p. 130). La regla está
escrita para esos reportajes; extenderla a toda la información es criterio de oficio: un aspecto
creativo (el virado, la dominante fuerte) cabe en una promoción o una pieza cultural; en un
informativo, la corrección busca que la imagen se parezca a lo que pasó.

## 4. Grafismo

### Quién hace qué

El grafismo de una casa (cabeceras, cortinillas, mapas, infografías, plantillas de rótulos) lo diseña
el área de grafismo; el montador lo inserta en la pieza, rellena las plantillas y hace los rótulos
sencillos en el propio sistema de edición. La ficha del Grafista y el circuito de los rótulos entre
redacción, realización y emisión están en el tema 4. Si en Canal Sur los rótulos van incrustados en el
vídeo desde la sala o los inserta realización en la emisión no consta en ningún documento publicado.

El RD 1680/2011 lo recoge como integración: **«Se han integrado en el montaje efectos procedentes de
una plataforma externa así como gráficos y rotulación procedente de equipos generadores de
caracteres o de plataformas de grafismo y rotulación externas.»** (módulo 0907, RA 3.d); y pide
guardar los ajustes para poder rehacerlos: **«Se han archivado los parámetros de ajuste de los
efectos, garantizando la posibilidad de recuperarlos y aplicarlos de nuevo.»** (RA 3.f).

### Títulos y rótulos en el sistema de edición

Los sistemas de edición traen generadores de títulos. En Resolve sirven para **«create leader when
outputting to tape, add slates, create subtitles, and otherwise fulfill any textual needs your program
has»** (cap. 56, p. 1213), y se editan como cualquier clip. Al arrastrar un título a la línea de tiempo,
**«the default duration of the resulting clip is 5 seconds»**, duración que se cambia en las
preferencias (p. 1213). Los tipos que ofrece (p. 1215):

| Generador | Qué es |
|---|---|
| *L*, *M* y *R Lower 3rd* | Dos líneas de texto en el tercio inferior, a la izquierda, al centro o a la derecha de la zona segura de título: es el rótulo de identificación (nombre y cargo) |
| *Scroll* | Texto que sube de abajo arriba; **«The duration of the generator clip in the Timeline determines the speed of the scroll»**: son los créditos |
| *Text* | Una palabra, una línea o un párrafo |
| *Text+* | Generador avanzado, con más opciones de estilo y animación, pero con un solo estilo para todo el texto |
| *Fusion Titles* | Plantillas animadas hechas en el módulo de composición del programa, que se pueden crear a medida |

La plantilla es la forma de que todos los rótulos de un programa salgan iguales: la misma tipografía,
el mismo tamaño y la misma posición (oficio). Las plantillas del grafismo de directo se ven en el tema 12.

### Lo que pide el Libro de Estilo

El Libro de Estilo de Canal Sur fija reglas para los gráficos informativos (3.16, «Gráficos», pp. 57-58), que se
desarrollan en el tema 12. Las dos que el montador mide con el reloj: **«La primera norma es dar
información ajustada que no incluya más de cuatro o cinco elementos por pantalla, con una presencia
mínima recomendable de ocho segundos.»** (3.16, p. 57). Y la del sonido (al final de 3.16.2, p. 58):
los gráficos **«llevarán una ‘cama’ de audio
por el canal correspondiente, salvo que se respete el sonido propio de la grabación»**. El rótulo,
además, es información: **«El rótulo que acompaña es también información. Reúne brevedad, impacto y
síntesis.»** (3.6.1, p. 50).

### Lo que ya está en el tema 12

Las zonas seguras de la EBU R 95, los ficheros gráficos y el canal alfa (JPG sin alfa, TGA de 32 bits),
el blanco del grafismo en alto rango dinámico (Informe UIT-R BT.2408), la rotulación de la casa según
el Libro de Estilo (cuándo obliga a rotular, cómo se escribe un rótulo) y los rótulos «Archivo» y
«Reconstrucción» están desarrollados en el tema 12 y no se repiten. En la sala se aplican igual:
ningún rótulo fuera de la zona segura de título; el logotipo o el rótulo que va encima de la imagen,
en un fichero con alfa; y, si el programa es HDR, el gráfico al nivel del blanco de referencia y no al
máximo de la señal.

Y un límite que toca al grafismo animado tanto como al montaje: los destellos y los patrones de
rayas, que se revisan en el control de calidad final (epígrafe 6, «Destellos y patrones»).

## 5. Mezcla

### Qué es mezclar en postproducción

La mezcla equilibra las capas y entrega en el formato de destino (las capas de la banda sonora, en el tema 11). A diferencia del directo (tema 11), se hace sobre material grabado: se
puede repetir, automatizar y medir el programa entero antes de entregarlo (oficio).

El orden de trabajo habitual (oficio):

1. Los diálogos primero: limpios, igualados entre tomas y en su plano. Son la referencia del resto.
2. Los ambientes, que dan continuidad y tapan los cortes.
3. Los efectos, a la medida de la imagen.
4. La música, que deja sitio a la voz.
5. El conjunto: el bus de salida, la medida de sonoridad y el pico verdadero.

Los procesos de la mezcla (ecualización, compresión, limitación, reverberación), la mesa y la
mezcla multicanal son materia del operador de sonido y no los pide este enunciado.

El RD 1680/2011 lo formula así: **«Se ha construido la banda sonora de un programa, incorporando
múltiples bandas de audio (diálogos, efectos sonoros, músicas y locuciones), realizando el ajuste de
niveles y aplicando filtros y efectos.»** (módulo 0907, RA 2.e). Quién mezcla: en la RTVA, la ficha
del Realizador le encarga dirigir las **«mezclas hasta su completo acabado»**, y la mezcla la ejecuta
el área de sonido o, en una pieza sencilla, el propio montador (oficio).

### Limpiar antes de mezclar

El orden de trabajo habitual sobre una pista de diálogo (oficio):

1. Edición: quitar golpes, toses y ruidos sueltos cortando o sustituyendo el trozo por ambiente
   del mismo lugar.
2. Filtro paso alto contra los graves que no son voz.
3. Zumbido, si lo hay.
4. Reducción de ruido por perfil, suave.
5. Sibilantes y oclusivas, si hace falta.
6. Después, la ecualización y la compresión de la mezcla.

Y el relleno: donde se ha cortado algo, debajo tiene que seguir sonando el ambiente del lugar; si no,
el silencio digital delata el corte.

### El fundido cruzado de audio

Cómo funciona: la primera señal baja mientras la segunda sube, y durante unos fotogramas suenan
las dos. Es el encadenado de vídeo aplicado al sonido.

Por qué existe, que es lo que da sentido a la pregunta: un corte seco entre dos audios distintos
produce un chasquido, porque la onda salta de un valor a otro sin transición. Un *crossfade* de
dos o tres fotogramas basta para que ese salto desaparezca, y por eso los montadores lo ponen por
sistema en todos los cortes de audio, aunque no se busque ningún efecto.

### El doblaje: ADR

El ADR es la creación y sustitución de diálogo en sincronía labial, en postproducción de sonido.

Se hace en una sala de doblaje, con el intérprete viendo su propia imagen, y sirve para tres cosas:

1. Sustituir diálogo que se grabó mal: con ruido, con viento, con un avión encima.
2. Cambiar una interpretación sin volver a rodar.
3. Añadir diálogo que no se rodó: reacciones, murmullos, voces de fondo.

Su nombre inglés lo explica: *automated dialogue replacement*, sustitución automatizada de diálogo.
Y *looping* viene del método antiguo: se montaba un bucle de película con la escena y se repetía
sin parar hasta que el intérprete encajaba.

Lo que no es ADR, aunque sea de la misma fase (oficio): el proceso por el que se combinan varias
pistas es la mezcla; el sonido del entorno que se ve en la imagen es el ambiente; y la ventana que
muestra la disposición cronológica del montaje es la línea de tiempo.

### Mezclar de oído, con la escucha fija

La normalización por sonoridad cambia la forma de mezclar. La Tech 3343: **«Loudness levelling
encourages to mix ‘only by ear’ - after setting levels and a fixed monitor gain.»** Se fija el nivel
de escucha una vez y no se toca: si con la escucha fija el programa suena bien, estará cerca del
objetivo.

### La sonoridad del programa terminado

Limpia y mezclada, la pieza tiene que cumplir la sonoridad de la EBU R 128, que el tema 11 sólo
nombra. Lo que fija la R 128 (versión 5, noviembre de 2023):

| Punto | Lo que dice |
|---|---|
| h) Nivel objetivo | **«the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS. Where attaining the Target Level is not achievable practically (for example, live programmes), a tolerance of ±1.0 LU is permitted.»** |
| i) Tolerancia de medida | **«a tolerance of ±0.2 LU is allowed in order to take account of measurement errors»** |
| m) Pico verdadero | **«the True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during production (linear audio)»**; tolerancia de medida de **«±0.3 dB (for signals with a bandwidth limited to 20 kHz)»** |
| k) Medidor | Conforme a la UIT-R BS.1770 y a la EBU Tech 3341 |
| n) Margen de sonoridad (LRA) | Según la EBU Tech 3342; nota 2: **«For programmes shorter than 1 minute, the use of the measure Loudness Range is not recommended»** |
| l) Todo el programa | **«the audio signal shall generally be measured in its entirety, without emphasis on specific foreground elements such as speech, music or sound effects»** |

Las tres cifras que hay que saber de memoria son −23 LUFS, ±1 LU y −1 dBTP. Dos matices que afectan al montador:

- El punto l) quiere decir que se mide el programa entero, no sólo la voz: la R 128 no normaliza
   por diálogo.
- «Programa» incluye la publicidad. Las definiciones de la R 128 cuentan como programa **«An
   advertisement (commercial), trailer, promotional item ('promo'), interstitial or similar item
   ("Short-form Content")»**. La sonoridad del programa se define como **«The integrated loudness
   over the duration of a programme»**.

Un programa postproducido no tiene la excusa del directo. La Tech 3343: en postproducción **«a
general tolerance of ±0.2 LU around the Target Level of −23 LUFS is acceptable»**, para no rechazar
programas por la suma de las tolerancias de medida, mientras que el directo tiene ±1 LU.
Dentro de la tolerancia no hay que hacer nada; fuera de ella, se corrige con **«a simple corrective static gain
calculation»** (§ 3.2), un cambio de ganancia fijo para todo el programa; **«Typically, offline loudness
meters perform both the measurement as well as the correction.»** (§ 3.1).

Un cambio de ganancia de X dB mueve la sonoridad integrada X LU y el pico verdadero X dB.
Dos casos (cálculo):

| Programa medido | Corrección | Resultado |
|---|---|---|
| −21,4 LUFS, pico −2,5 dBTP | Bajar 1,6 dB | −23,0 LUFS, pico −4,1 dBTP: cumple |
| −24,5 LUFS, pico −1,8 dBTP | Subir 1,5 dB | −23,0 LUFS, pero pico −0,3 dBTP: no cumple el −1 dBTP |

En el segundo caso hay que limitar antes de subir: el limitador tiene que rebajar los picos al
menos 0,7 dB (de −1,8 a −2,5 dBTP), para que tras subir 1,5 dB no pasen de −1,0 dBTP (con 0,8 dB
de reducción quedan en −1,1, con algo de margen); y medir de nuevo,
porque limitar baja un poco la integrada (oficio y cálculo).

### Lo que se revisa antes de dar la mezcla por buena

Oficio, sobre las cifras de las recomendaciones citadas (la de las piezas cortas es de la EBU R 128 s1):

- Integrada del programa entero en −23 LUFS (±0,2 LU en postproducción); en una pieza corta,
  además, máxima a corto plazo no mayor de −18 LUFS.
- Pico verdadero no mayor de −1 dBTP.
- La voz se entiende en todo el programa, también sobre la música y los efectos.
- Fase: la suma en mono no pierde la voz.
- Sin chasquidos en los cortes, sin silencios digitales bajo los cortes y sin saltos de ambiente.
- Sincronía con la imagen al principio y al final del programa.

## 6. Revisión de calidad final

### Qué es y quién la hace

Revisar la calidad final es comprobar, antes de entregar, que la pieza terminada cumple lo técnico
(señal, sonido, fichero) y lo editorial (contenido, rótulos, duración), y dejar constancia de ello
(oficio). Lo técnico lo controla la sala de montaje y, en la emisión, continuidad; el realizador
responde de la calidad y la duración del programa (epígrafe «El realizador responde del acabado»).

La norma de enseñanza la sitúa en el acabado (RD 1680/2011, módulo 0907, RA 5):

- **«Se ha establecido un sistema para comprobar la integración de los materiales externos en el
  montaje final, así como la sincronización y contenido de las distintas pistas de sonido.»** (RA 5.e)
- **«Se han especificado las características de las principales normativas existentes respecto a
  referencias, niveles y disposición de las pistas, a los diferentes formatos de intercambio de
  vídeo…»** (RA 5.f)
- **«Se ha generado una cinta para emisión, siguiendo determinadas normas PPD (preparado para
  difusión o emisión), incorporando las claquetas y la distribución solicitada de pistas de audio.»**
  (RA 5.h). Hoy la entrega suele ser un fichero, no una cinta, pero la idea es la misma: una copia
  preparada para difundir, con su claqueta y sus pistas en el orden pedido (oficio).

Y en los contenidos del módulo: **«Control de calidad del producto:»**, con **«Distribución de pistas
sonoras en los soportes videográficos y cinematográficos.»**, **«La banda internacional.»** y
**«Normas PPD (Preparado para difusión o emisión).»**; **«Balance final técnico de la
postproducción: criterios de valoración.»** y **«El control de calidad en el montaje, edición y
postproducción.»** La revisión empieza antes, con el material: el módulo 0906 pide que **«Se han
verificado la disponibilidad y la calidad técnica de todas las imágenes, audio y material gráfico,
asegurando su correspondencia con el estándar de calidad requerido en la documentación del proyecto
audiovisual objeto de montaje.»** (RA 3.e).

### La revisión en fichero: el control de calidad de la UER

El programa de control de calidad de la UER ha reunido un catálogo común de comprobaciones de calidad (QC, del inglés
*quality control*) para el trabajo con ficheros. Su hoja informativa *Quality Control*, publicada el
1 de septiembre de 2015, parte de una advertencia: **«There is a common misconception that DIGITAL
means QUALITY! If that were true, there would be no need for Quality Control.»** (es un error creer
que digital significa calidad; si lo fuera, no haría falta el control de calidad).

Las comprobaciones se agrupan en plantillas, una por destino: **«Different QC Templates may be used
for different outputs – the key is to build a viable test set for each of the programme’s
destinations.»** Los ejemplos que da la UER:

| Plantilla | Qué comprueba |
|---|---|
| **«Automated QC»** | **«To check signal levels and standards»** (niveles y normas de la señal, con una máquina) |
| **«File Package Compliance»** | **«To check against file standards, e.g. AS11 DPP»** (que el fichero cumpla la especificación de entrega) |
| **«Manual QC»** | **«Golden Eyes/Ears watching the programme»** (una persona que ve y escucha el programa entero) |
| **«File Structure Analysis»** | **«Deep analysis to find if something is wrong with the file structure»** (la estructura interna del fichero) |

Tres ideas más de la misma hoja:

- Varias plantillas para una sola pieza: **«A finished programme workflow may require several
  different QC Templates, each based on the particular requirements of the deliverable.»**
- Cuántas veces se ve el programa depende del procesado y de la fiabilidad de las comprobaciones
  automáticas: **«The number of times a programme is
  actually watched will depend on the level of processing and the accuracy of the automated QC checks
  applied at each stage.»**
- El informe: **«A traditional QC report is a written document with a mixture of comments, critical
  assessment and technical measurements. The “sign-off” for transmission is usually just a
  signature!»** (comentarios, valoración y medidas, y una firma que da la pieza por buena para
  emisión).

El catálogo de la UER (qc.ebu.io) define cada comprobación. Las
que más tocan al realizador:

| Comprobación | Definición de la UER |
|---|---|
| Sonoridad (*Loudness*) | **«System shall check for programme loudness, loudness range, maximum momentary loudness, maximum short term loudness and true peak.»** |
| Destellos (*Flashing Video*) | **«System shall check for segments of video which may be harmful to sufferers of photosensitive epilepsy. This includes tests for luminance flashes, red flashes and spatial patterning.»** |
| Niveles de vídeo (*Video Signal Levels*) | **«System shall report luma and chroma values lying outside the acceptable range, but also RGB gamut…»** |
| Imagen congelada (*Video Freeze*) | **«…the System shall verify if 'frozen' (i.e. non-moving) pictures appear in the video for multiple adjacent identical (or near-identical) frames.»** |
| Silencio (*Audio Silence*) | **«…the system shall verify if the audio level on any audio channel is lower than the user defined Silence Threshold Level for intervals longer than a user specified Minimum Silence Duration.»** |
| Fase invertida (*Audio Phase Reversal*) | **«System shall determine if an audio channel pair which should normally be in phase is out of phase.»** |
| Código de tiempo (*Timecode*) | Comprobar **«1 - TC start value(s); 2 - TC discontinuities; 3 - Invalid TC (e.g. seconds=80).»** |
| Subtítulos que faltan (*Missing Captions/Subtitles*) | **«…the system shall detect periods where speech is occurring in the audio but no captions/subtitles are displayed.»** |
| Formato activo (*Active Format Description*) | **«System shall check the presence and value of the Active Format Description (AFD), which describes the aspect ratio of the active picture, and safe cut-out areas.»** |

Aplicación: la máquina mide lo que se puede medir (niveles, sonoridad, silencios, congelados,
destellos, código de tiempo, estructura del fichero); lo que no se mide (que el rótulo diga lo que
tiene que decir, que el plano sea el pedido, que el corte no cambie el sentido de una declaración)
lo revisa una persona viendo la pieza entera (oficio).

### Destellos y patrones

La Recomendación UIT-R BT.1702-3 (11/2023), *Guidance for the reduction of photosensitive epileptic
seizures caused by television*, en vigor, trata las imágenes que pueden provocar crisis a personas
con epilepsia fotosensible. Afecta al montaje (cortes rápidos), al grafismo animado y a la revisión
final. Es una recomendación, no una ley: pide **«that broadcasting organizations should be encouraged
to provide guidance to programme producers of the risks of creating television image content which
may induce photosensitive epileptic seizures in susceptible viewers of television broadcasts»**. Y
parte de que el riesgo no se puede suprimir del todo: **«It is therefore impossible to eliminate the
risk of flashing images on television causing convulsions in viewers with photosensitive
epilepsy.»**

Lo que la recomendación da por potencialmente dañino (directriz 1, destellos):

| Qué | Umbral de la BT.1702-3 |
|---|---|
| Destello, con la imagen oscura por debajo de 160 cd/m² | **«a difference of 20 cd/m2 or more between the screen luminance of the darker and the brighter images»**; **«applicable for both standard dynamic range (SDR) and high dynamic range (HDR) programmes»** |
| Destello, con la imagen oscura en 160 cd/m² o más | **«a difference of more than 1/17 Michelson contrast»**; **«applicable for HDR programmes only»** |
| Rojo saturado | **«Irrespective of luminance, a transition to or from a saturated red is also potentially harmful.»** |
| Secuencia no permitida | Cuando a la vez los destellos simultáneos ocupan **«more than 25% of the displayed (see Note 4) screen area»** y hay **«more than three flashes (i.e. six changes in luminance as described above) within any one-second period»** |
| Lo que siempre vale | **«Isolated single, double, or triple flashes are acceptable»**; y los destellos cuyos frentes están separados **«by 360 ms or more are acceptable in a 50 Hz environment or separated by 334 ms or more are acceptable in a 60 Hz environment, irrespective of their brightness or screen area»** |
| Cortes rápidos | **«Rapidly changing image sequences (for example, fast cuts) are provocative if they result in areas of the screen that flash, in which case the same constraints apply as for flashes.»** |
| Duración | **«a sequence of flashing images lasting more than five seconds might constitute a risk even when it complies with the guidelines above»** |

La directriz 2, patrones: **«Potentially harmful regular patterns occur when an image contains light
and dark pairs of clearly discernible stripes in any orientation.»** La orientación adicional que la
recomendación recoge como usada por algunas administraciones concreta: más de cinco pares de rayas
y **«the stripes are stationary and the pattern occupies more than 40% of the displayed screen
area»**, o **«the stripes change direction, oscillate, flash, or reverse in contrast and the pattern
occupies more than 25% of the displayed screen area»**.

Tres notas de la recomendación que importan en la sala: para medir, la imagen SDR se supone con el
blanco a **«200 cd/m2»** y la HLG a **«1 000 cd/m2»** (nota 3); **«The use of automatic video
analysers to help alert production staff to potentially guideline violations in video material can
be beneficial.»** (nota 5); y **«There may be regional, broadcaster or content distributor variations
to the guidelines given above. It is advisable that programme suppliers consult the relevant delivery
requirements.»** (nota 1).

Una cuenta (cálculo propio): a 25 imágenes por segundo, 360 ms son 9 cuadros; un parpadeo de alto
contraste en pantalla completa con un destello cada 4 cuadros (más de seis por segundo) supera el máximo de
tres por segundo, y uno cada 9 cuadros o más espaciado es aceptable sea cual sea su brillo y su
tamaño. Si Canal Sur tiene una norma propia de destellos, no consta en lo publicado.

### El máster

El máster es el resultado final del que salen todas las copias, y lo que lo define no es su soporte
sino sus especificaciones:

| Especificación | Qué fija |
|---|---|
| Formato y códec | Cómo está escrito el vídeo |
| Resolución y cadencia | Cuántos píxeles y cuántos fotogramas por segundo |
| Espacio de color y niveles | Que la señal esté dentro del rango legal |
| Configuración de pistas de audio | Qué lleva cada pista: mezcla, pista internacional, audiodescripción |
| Nivel de sonoridad | El volumen medio normalizado que el destino exige |
| Estructura | Cabecera con barras y tono, claqueta, cuenta atrás, programa |
| Subtítulos | Incrustados o en fichero aparte |

Y la regla que ordena todo (oficio): el máster se hace para su destino. Una misma pieza tiene un máster de
emisión, uno de plataforma y uno de venta internacional, y los tres se diferencian sobre todo en las
pistas de audio y en los subtítulos.

Dos datos de la casa y de la norma de enseñanza sobre el máster:

- Qué se graba en un programa de plató: el RD 1680/2011 pide que **«Se han determinado las señales de
  la realización televisiva que van a ser grabadas: master, señal sin incrustaciones y cámaras
  dobladas o masterizadas.»** (módulo 0905, RA 1.f). La señal sin incrustaciones (sin rótulos ni
  grafismo) es la que permite reutilizar el programa o rehacer sus rótulos sin volver a montar
  (oficio).
- Lo que no se toca: en la entrevista grabada en exteriores, el Libro de Estilo dice que **«sólo se
  manipulará el ‘master’ para corregir defectos técnicos de fácil resolución y que no modifiquen
  sustancialmente el mensaje ni el concepto estético de la propia entrevista.»** (3.17.1.5,
  pp. 61-62).

Las especificaciones de entrega de CSRTV (formato, códec, pistas, estructura del fichero) no constan
en un documento publicado leído. Los formatos y los entregables son el tema 14; la documentación que
acompaña a la pieza (parte de emisión, declaración de autores), el tema 7.

### La revisión, paso a paso

Orden de oficio, con los datos de este tema, para dar por buena una pieza antes de entregarla:

| Paso | Qué se comprueba | Con qué |
|---|---|---|
| 1. Contenido | Que la pieza cuenta lo que tiene que contar, con los planos y el orden aprobados; rótulos bien escritos y a tiempo; «Archivo» y «Reconstrucción» donde tocan; caras tramadas cuando hay riesgo | Visionado completo contra el guion y la escaleta; Libro de Estilo (temas 12 y 16) |
| 2. Duración | La duración pedida, al cuadro; coleo al final | Código de tiempo |
| 3. Imagen | Negros y blancos dentro de rango; sin dominantes ni saltos de color entre planos; sin imágenes congeladas ni recortes | Forma de onda, desfile, vectorscopio; QC automático |
| 4. Destellos | Sin secuencias de destellos ni patrones fuera de la BT.1702-3 | Analizador automático y visionado |
| 5. Sonido | −23 LUFS (±0,2 LU en postproducción), pico verdadero de −1 dBTP como máximo; sincronía; sin chasquidos, silencios ni fase invertida; la voz se entiende | Medidor de sonoridad; escucha |
| 6. Fichero | El formato, el códec, las pistas de audio en el orden pedido, la claqueta y el código de tiempo de inicio del destino | Plantilla de QC del destino |
| 7. Constancia | Parte de emisión, incidencias, firma | Documentación de la pieza (tema 7) |

Si algo falla, se devuelve a la fase que lo produjo (color a la corrección, sonoridad a la mezcla,
contenido al montaje) y se vuelve a revisar sólo lo cambiado y la pieza entera en lo que el cambio
pueda afectar (duración, sincronía, sonoridad) (oficio).

## Aplicación práctica

Tres supuestos del tipo que puede plantear la prueba práctica, resueltos con lo que el tema da.

1. Reportaje de cinco minutos para un programa, grabado con dos cámaras, con entrevistas, música,
   locución y un gráfico animado. El realizador revisa el primer montaje contra el guion y el
   minutado y cierra la estructura antes del acabado (epígrafe 1). Pide la igualación de color de
   las dos cámaras contra un plano de referencia, con la piel del entrevistado en el mismo punto del
   vectorscopio (epígrafe 3); rótulos de identificación con la plantilla del programa y dentro de la
   zona de título; transiciones sólo donde signifiquen algo, con colas suficientes (a 25 imágenes por
   segundo, 12 o 13 cuadros por lado para un fundido centrado de un segundo). En la mezcla, los
   diálogos primero, la música bajo la voz y el programa entero a −23 LUFS (±0,2 LU) con el pico
   verdadero en −1 dBTP como máximo (epígrafe 5). Antes de entregar, la revisión del epígrafe 6: el
   gráfico animado no puede tener secuencias de más de tres destellos por segundo en más del 25 % de
   la pantalla.
2. Resumen de un partido para el informativo, a partir de la retransmisión. El material sale del
   volcado del servidor de repetición (jugadas y repeticiones seleccionadas en el directo) y se
   monta en la sala; si dos ángulos de una jugada tienen que ir sincronizados, se trabajan con los
   canales enganchados o con el mismo código de tiempo (epígrafe 2). La cámara lenta de una jugada,
   con flujo óptico o con el material grabado a alta velocidad, comprobando que no deja defectos
   (epígrafe 3). Duración al segundo pedida en la escaleta y coleo al final.
3. Pieza que la revisión devuelve: la plantilla de control de calidad marca sonoridad integrada de
   −24,5 LUFS con picos de −1,8 dBTP, un tramo de dos segundos de silencio en el canal 2 y un
   congelado de 12 cuadros. Sonoridad: no se sube sin más 1,5 dB, porque los picos quedarían en
   −0,3 dBTP; se limita primero al menos 0,7 dB y se mide de nuevo (epígrafe 5). El silencio y el
   congelado se revisan en el montaje: si son voluntarios (un silencio dramático, un congelado de
   cierre), se anotan en el parte; si no, se corrigen. Después, nueva pasada de la plantilla entera
   y visionado de la pieza (epígrafe 6).

## Normativa y recomendaciones técnicas que el tema cita

| Documento | Qué es | Qué se toma |
|---|---|---|
| Real Decreto 1680/2011, de 18 de noviembre, título de Técnico Superior en Realización de proyectos audiovisuales y espectáculos (BOE núm. 302, de 16-12-2011) | Norma de enseñanza. Texto de 2011; lo modifica el Real Decreto 500/2024, de 21 de mayo, que no cambia los módulos citados | Módulo 0907, RA 2 (e, f, g, h), RA 3 (b a f), RA 5 (c, e, f, h) y contenidos; módulo 0906, RA 3.e; módulo 0905, RA 1.b y 1.f |
| X Convenio colectivo de la RTVA y sus sociedades filiales (BOJA núm. 240, de 10-12-2014) | Convenio colectivo; su vigencia la trata el temario común | Anexo III, fichas 5351000, 5353000, 5212204, 5212206 y 5302010 |
| Recomendación UIT-R BT.1702-3 (11/2023) | Recomendación de la UIT-R, en vigor; sustituye a la BT.1702-2 (10/2019) | Directrices 1 y 2, notas 1, 3 y 5, orientación sobre patrones |
| EBU R 128-2023 (versión 5, noviembre de 2023) y EBU R 128 s1 V3 (agosto de 2020) | Recomendaciones de la UER | Nivel objetivo, tolerancias, pico verdadero, medida del programa entero; máxima a corto plazo de las piezas cortas |
| EBU Tech 3343-2023 (versión 4) | Guía de producción de la UER para aplicar la R 128 | Tolerancia de ±0,2 LU en postproducción, corrección por ganancia estática, mezcla con la escucha fija |
| UER, hoja informativa *Quality Control* (01-09-2015) y catálogo de comprobaciones qc.ebu.io | Documentos técnicos de la UER, no recomendaciones | Plantillas de control de calidad por destino; definiciones de las comprobaciones |

## Lo que este tema no da, y dónde está

- Qué sistema de edición, de corrección de color, de repetición y de gestión de material usa CSRTV,
  y sus especificaciones de entrega y plantillas de control de calidad: no constan en un documento
  publicado. Avid, Blackmagic, Adobe y EVS se citan como ejemplo, por su documentación.
- La guía de Media Composer leída es la de 1999 (versión 8); los nombres de las operaciones
  (*Trim*, *slip*, *slide*, *Match Frame*) son los de esa guía. La documentación vigente de Avid no se
  ha leído, ni la función de transcripción automática de Media Composer.
- La obra de Eisenstein (*Film Form*) no se ha leído: los cinco métodos se dan por la tesis de
  Georgia Tech que la cita. Las atribuciones de Griffith, Pudovkin o Bazin que traen otros manuales
  no se dan.
- El término *dump* del servidor de repetición: vocabulario de oficio, no contrastado en la
  documentación de EVS.
- Si en España hay una norma jurídica sobre destellos en televisión: no se ha buscado; la BT.1702-3
  es una recomendación. Norma propia de Canal Sur sobre destellos: no consta.
- La leyenda de los sufijos de los identificadores del catálogo de control de calidad de la UER y
  la EBU Tech 3363: no se han podido leer.
- Lenguaje del montaje (corte, *raccord*, elipsis, narrativo y expresivo, alternado y paralelo,
  Kuleshov): tema 1. Documentos de la grabación al montaje, fichas del convenio y documentación de
  la pieza terminada: tema 7. Funciones del realizador y del ayudante: tema 3. Transiciones, efectos
  e incrustaciones del mezclador: tema 9. Planos sonoros, sincronía labial, intercom: tema 11.
  Grafismo, rotulación, zonas seguras, ficheros gráficos y grafismo HDR: tema 12. Formatos, códecs,
  niveles de la señal, HDR y entregables: tema 14. Versiones para redes: tema 15. Subtitulado,
  audiodescripción y tratamiento responsable de imágenes: tema 16. Derechos de la música y del
  archivo: tema 17.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| Real Decreto 1680/2011 (BOE-A-2011-19599), anexo I, módulos 0905, 0906 y 0907 | Epígrafes «Postproducción», 1, 3, 4, 5 y 6 | 29-09-2026 |
| X Convenio colectivo de la RTVA (BOJA núm. 240, de 10-12-2014), anexo III: pp. 111, 125, 127, 190 y 196 | Quién dirige el montaje y quién controla la calidad | 29-09-2026 |
| RTVA, *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, 1.ª ed., 2004: 3.17.1.5 (pp. 61-62); y 3.2.2, 3.6.1, 3.16, 9.2.12.4, 9.9, 9.9.1 y 9.9.2 | Código de tiempo y planos compatibles con varias cámaras; manipulación del máster; límites de los efectos, del color y del grafismo | 29-09-2026 (3.17.1.5); el resto, 25-09-2026, en el texto ya cerrado del tema 7 de Operador/a Montador/a de Vídeo |
| J. M. Todd, *Eisenstein's Film Theory of Montage and Architecture*, tesis de máster, Georgia Institute of Technology, noviembre de 1989, pp. 8-20 (repository.gatech.edu) | Los cinco métodos de Eisenstein | 29-09-2026 |
| Avid Technology, *Avid Media Composer User's Guide*, Release 8.0, 1999: pp. 431 (*Match Frame*), 522-523, 526 y 531 (modo *Trim*), 540 y 543 (*slip* y *slide*) | Epígrafe 2 | 29-09-2026 |
| EVS, *IPDirector Version 6.2, Control Panel User Manual*, junio de 2013, p. 30 (manualsdir.com) | Canales enganchados | 29-09-2026 |
| UER, *Quality Control*, hoja informativa, 01-09-2015 (tech.ebu.ch) | Plantillas de control de calidad, informe | 29-09-2026 |
| UER, catálogo de comprobaciones de calidad, qc.ebu.io, API v1 | Definiciones de las comprobaciones | 29-09-2026 |
| Recomendación UIT-R BT.1702-3 (11/2023), itu.int | Destellos y patrones | 29-09-2026 |
| Textos ya cerrados de Canal Sur: tema 7 (postproducción), tema 3 (edición no lineal), tema 6 (servidor de repetición) y tema 13 (gestión de material) de Operador/a Montador/a de Vídeo; tema 9 (postproducción de sonido) de Operador/a de Sonido | Lo copiado de ellos, con sus fuentes: Blackmagic Design, *DaVinci Resolve 21 Reference Manual*; Adobe, ayuda de Premiere; Avid, *Avid DNxHD Technology* (2012) y página de producto de MediaCentral; EBU R 128, R 128 s1 y Tech 3343 | 24 y 25-09-2026 (lectura de los temas de origen) |
| Oficio | Qué es la postproducción; en directo no hay postproducción; montaje preliminar; tabla de los métodos de Eisenstein; modalidades del *trim*; coleo; volcado; fundido cruzado de audio; qué es revisar la calidad final; cuenta de los destellos a 25 imágenes por segundo; revisión paso a paso; supuestos prácticos | — |
