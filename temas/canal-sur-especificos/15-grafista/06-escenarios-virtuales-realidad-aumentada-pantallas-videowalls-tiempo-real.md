# Tema 6 del específico de Grafista · Escenarios virtuales, realidad aumentada, pantallas, videowalls y grafismo en tiempo real

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Grafista · punto 6 |
| Sirve para | Grafista de Canal Sur (grupo B03): test de teoría específica y de aplicación práctica, y prueba práctica del puesto |
| Fuente | Ninguna norma regula cómo es un plató virtual, un sistema de realidad aumentada, una pantalla de plató o un sistema de grafismo en tiempo real. Lo propio de la casa: *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, 1.ª ed., marzo de 2004). Documentación de fabricante: Epic Games (documentación de Unreal Engine 5.8: *In-Camera VFX Overview*, *Recommended Hardware for In-Camera VFX*, *In-Camera VFX Best Practices*, *nDisplay Overview*, *Motion Design*, *Professional Video IO*), Vizrt (*Viz Multiplay User Guide* 3.3, *Viz Engine Administrator Guide* 5.2 y 5.4, *Introduction to Viz Artist* 5.3), Chyron (páginas de *PRIME CG* y *About Chyron*, y nota de prensa de PRIME 5.3) y Mo-Sys (ficha del StarTracker Max y catálogo de seguimiento de cámara). Lo demás, oficio declarado como tal |
| Redacción que se estudia | Libro de Estilo, 1.ª ed., marzo de 2004; documentación de fabricante en la versión publicada el día en que se leyó (fechas en «Trazabilidad») |
| Extensión | 12.000 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); *Libro de
Estilo de Canal Sur Televisión y Canal 2 Andalucía* (Libro de Estilo o LE).

Los términos técnicos del tema, presentados de entrada: la realidad aumentada (RA; AR en la
documentación en inglés), la realidad virtual (RV, VR en inglés) y la realidad mixta (RM); los efectos visuales (VFX, del
inglés *visual effects*); el diodo emisor de luz (LED, del inglés *light-emitting diode*) y la pantalla de
cristal líquido (LCD, del inglés *liquid crystal display*); la unidad de proceso gráfico (GPU, del
inglés *graphics processing unit*), es decir, la tarjeta gráfica; el campo de visión (FOV, del inglés
*field of view*); el banco de mezcla y efectos del mezclador (M/E, del inglés *mix/effects*); los
fotogramas por segundo (fps; FPS en la documentación de Epic Games) y el milisegundo (ms); los niveles
de detalle de un modelo 3D (LOD, del inglés *level of detail*); el protocolo de internet (IP); la interfaz digital en serie (SDI, del
inglés *serial digital interface*), la salida de gráfica DisplayPort y la interfaz visual digital (DVI,
del inglés *digital visual interface*); la resolución de ultra alta definición (UHD); el espacio de
color de los monitores de informática (sRGB) y el sistema de gestión de color OpenColorIO (OCIO); el alto rango dinámico (HDR, del inglés *high
dynamic range*); SSGI, SSAO y SSR, siglas con que Epic Games nombra tres efectos calculados en espacio
de pantalla (así los presenta la cita en que aparecen); el
lenguaje de marcado de las páginas web (HTML); el protocolo con que el sistema de redacción habla con
los equipos de producción (MOS, del inglés *media object server*); el identificador de protocolo de
seguimiento **FreeD** (así lo escribe el fabricante); el elemento virtual que se pone delante del
presentador (*foreground*); la incrustación por color (croma, *chroma key*) y el rebote de color del
fondo sobre la figura (*spill*); el relleno (*fill*) y la llave (*key*) con que un sistema de grafismo
entrega una imagen con transparencia; y la pantalla de plató formada por muchos paneles (videowall, que
el Libro de Estilo escribe «vidiwall» y «‘vidi wall’»). Viz Artist, Viz Engine, Viz Pilot, Viz Trio y
Viz Multiplay son productos de Vizrt; Unreal Engine, con sus módulos nDisplay, Composure y Motion
Design, es el motor de representación en tiempo real de Epic Games; PRIME y CAMIO son productos de
Chyron (FBX es un formato de Autodesk que Chyron dice importar); StarTracker, de Mo-Sys; After Effects es un programa de composición de Adobe; Unity es otro
motor de tiempo real, y Blender y Cinema 4D, programas de 3D que renderizan en diferido; Datapath,
NVIDIA y AMD, fabricantes de equipos que la documentación leída nombra. Se citan como ejemplos: qué sistemas usa CSRTV no consta en
documento publicado.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.15, punto 6): «Escenarios virtuales,
> realidad aumentada, pantallas, videowalls y grafismo en tiempo real.»

Qué se puede preguntar: qué distingue decorado virtual, realidad aumentada, realidad mixta y producción
virtual en pared de LED; cuáles son las tres piezas de un plató virtual y cuál es la clave; qué mide un
sistema de seguimiento de cámara, qué familias hay y qué es el FreeD; cómo se ilumina un plató de croma
y qué pide el Libro de Estilo al vestuario; qué diferencia al croma de la pared de LED; qué son el
frustum interior y el exterior; cómo se pone un elemento virtual delante del presentador; cómo se
compensa el retardo de la realidad aumentada y cuántos milisegundos son N fotogramas; qué puede ir en
una pantalla de plató, qué problemas tiene (moiré, retardo, realimentación, parpadeo) y cómo se le manda
una señal distinta del programa; de qué se compone un videowall de LED (armarios, procesador), qué es el
paso de píxel y qué se gana y se pierde al reducirlo; cómo se reparte una imagen entre muchas pantallas
y por qué hace falta el genlock; cómo se alimenta un videowall desde un sistema de grafismo; qué es un
motor de representación en tiempo real, qué lo distingue del renderizado diferido y cuántos hacen falta
para varias cámaras; qué funciones tiene un sistema de grafismo; qué ofrecen Vizrt, Unreal Engine y
Chyron. En la prueba práctica: montar un plató virtual con varias cámaras, sincronizar cámaras con y sin
realidad aumentada, preparar el contenido de un videowall y resolver una conexión por pantalla con
retardo.

<!-- indice -->

## Índice

- [De dónde sale este tema](#de-dónde-sale-este-tema)
- [1. Escenarios virtuales](#1-escenarios-virtuales)
  - [Decorado virtual, realidad aumentada y producción virtual](#decorado-virtual-realidad-aumentada-y-producción-virtual)
  - [Qué es un decorado virtual](#qué-es-un-decorado-virtual)
  - [Las tres piezas del plató virtual](#las-tres-piezas-del-plató-virtual)
  - [El seguimiento de cámara](#el-seguimiento-de-cámara)
  - [Croma o pared de LED](#croma-o-pared-de-led)
  - [Croma y pared de paneles, cara a cara](#croma-y-pared-de-paneles-cara-a-cara)
  - [La pared de LED: frustum interior y exterior](#la-pared-de-led-frustum-interior-y-exterior)
  - [La iluminación de un plató de croma](#la-iluminación-de-un-plató-de-croma)
  - [Lo que hace el grafista en un escenario virtual](#lo-que-hace-el-grafista-en-un-escenario-virtual)
  - [Preparar la escena para que el motor la dibuje a tiempo](#preparar-la-escena-para-que-el-motor-la-dibuje-a-tiempo)
- [2. Realidad aumentada](#2-realidad-aumentada)
  - [Realidad virtual, aumentada y mixta](#realidad-virtual-aumentada-y-mixta)
  - [La realidad aumentada en el motor: vídeo que entra y sale](#la-realidad-aumentada-en-el-motor-vídeo-que-entra-y-sale)
  - [Poner un objeto delante del presentador](#poner-un-objeto-delante-del-presentador)
  - [El retardo de la realidad aumentada](#el-retardo-de-la-realidad-aumentada)
- [3. Pantallas](#3-pantallas)
  - [Las pantallas del plató](#las-pantallas-del-plató)
  - [Tres problemas técnicos](#tres-problemas-técnicos)
  - [Cómo se manda una señal a las pantallas](#cómo-se-manda-una-señal-a-las-pantallas)
  - [El retardo de las pantallas y cómo se compensa](#el-retardo-de-las-pantallas-y-cómo-se-compensa)
  - [El programa de gestión de pantallas](#el-programa-de-gestión-de-pantallas)
  - [Lo que el grafista prepara para cada pantalla](#lo-que-el-grafista-prepara-para-cada-pantalla)
- [4. Videowalls](#4-videowalls)
  - [Qué es un videowall](#qué-es-un-videowall)
  - [Armarios y procesador](#armarios-y-procesador)
  - [El paso de píxel](#el-paso-de-píxel)
  - [Muchas pantallas, un solo lienzo](#muchas-pantallas-un-solo-lienzo)
  - [La sincronía: genlock](#la-sincronía-genlock)
  - [El color que se manda a la pared](#el-color-que-se-manda-a-la-pared)
  - [Lo que no funciona en un clúster](#lo-que-no-funciona-en-un-clúster)
  - [El videowall en un sistema de grafismo de televisión](#el-videowall-en-un-sistema-de-grafismo-de-televisión)
- [5. Grafismo en tiempo real](#5-grafismo-en-tiempo-real)
  - [El motor de representación en tiempo real](#el-motor-de-representación-en-tiempo-real)
  - [Diferido y tiempo real](#diferido-y-tiempo-real)
  - [Cuántos motores hacen falta](#cuántos-motores-hacen-falta)
  - [Las dos exigencias del tiempo real](#las-dos-exigencias-del-tiempo-real)
  - [Qué hace un sistema de grafismo](#qué-hace-un-sistema-de-grafismo)
  - [Tres sistemas, con la documentación de su fabricante](#tres-sistemas-con-la-documentación-de-su-fabricante)
  - [La conexión con la redacción y los datos](#la-conexión-con-la-redacción-y-los-datos)
- [Aplicación práctica](#aplicación-práctica)
  - [Un plató virtual con tres cámaras y una cabeza caliente, y realidad aumentada en dos](#un-plató-virtual-con-tres-cámaras-y-una-cabeza-caliente-y-realidad-aumentada-en-dos)
  - [Lo que se comprueba en el ensayo de un plató virtual](#lo-que-se-comprueba-en-el-ensayo-de-un-plató-virtual)
  - [El videowall de un informativo](#el-videowall-de-un-informativo)
  - [Cuentas que se piden](#cuentas-que-se-piden)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## De dónde sale este tema

Ninguna norma regula cómo es un sistema de grafismo, un plató virtual o una pantalla de plató. Lo que
el tema cita de fuera de la casa es documentación de fabricante —Epic Games, Vizrt, Chyron y Mo-Sys—,
en inglés y con la traducción o la lectura en redonda: vale como definición técnica de lo que hace cada
producto, no como norma, y lo que dice un fabricante es de ese fabricante aunque el concepto sea común a
los equipos profesionales. Lo que no está en ninguna fuente va como oficio y se dice.

Qué sistema de grafismo, de plató virtual, de seguimiento de cámara o de pantallas tiene CSRTV no consta
en documento publicado leído, y el tema no lo afirma. Lo que la casa dice de la materia está en su Libro
de Estilo, y se cita con su epígrafe y su página.

Los cinco términos del enunciado no son cinco técnicas independientes, sino piezas de una misma
maquinaria (oficio): un motor que dibuja imagen sintética a la cadencia del vídeo (el grafismo en tiempo
real), unos datos que le dicen desde dónde mira la cámara (el seguimiento) y un sitio donde esa imagen
se junta con la real, sea por incrustación (el escenario virtual y la realidad aumentada) o en una
pantalla que la cámara filma (las pantallas y los videowalls). El tema sigue el orden del enunciado y
deja el grafismo en tiempo real para el final, porque es lo que sostiene todo lo anterior.

## 1. Escenarios virtuales

### Decorado virtual, realidad aumentada y producción virtual

La realidad aumentada y el decorado virtual se estudian juntos porque usan la misma maquinaria, pero
no son lo mismo.
Tres cosas que se confunden y que son distintas por dónde está lo real y dónde lo sintético:

| Técnica | Qué es real | Qué es sintético | Cómo se junta |
|---|---|---|---|
| Decorado virtual (plató virtual) | Sólo las personas y los objetos que tocan | Todo el fondo | El fondo se sustituye por incrustación de crominancia |
| Realidad aumentada | El plató entero, con su decorado construido | Los objetos añadidos, que aparecen encima | Los objetos se superponen sobre la imagen real, con llave |
| Producción virtual en pared de LED | Las personas y el decorado próximo | El fondo, pero se muestra en pantallas reales del plató | No hay incrustación: la cámara filma la pantalla |

Las tres necesitan lo mismo para funcionar: saber en todo momento dónde está la cámara. Si la cámara
se mueve y el fondo sintético no se mueve con ella —con la misma perspectiva, el mismo encuadre y el
mismo enfoque—, el truco se cae. De ahí el seguimiento de cámara, más abajo. Y las tres tienen el
mismo problema de tiempo: generar la imagen sintética lleva unos cuantos fotogramas, y eso
desincroniza. De ahí el retardo, al final del epígrafe 2.

### Qué es un decorado virtual

En un decorado virtual sólo son reales las personas y los objetos que tocan; todo el fondo lo dibuja un
motor de *render* y se pone detrás de la figura por incrustación de crominancia (arriba). La
cámara se mueve porque su seguimiento le dice al motor desde dónde dibujar. El mezclador puede incrustar él mismo o
recibir la imagen ya compuesta del motor y limitarse a conmutarla (oficio).

### Las tres piezas del plató virtual

Las tres piezas que la hacen posible, y hay que saber que sin la tercera no funciona:

| Pieza | Qué hace |
|---|---|
| Plató de croma | El fondo que se va a sustituir, iluminado uniforme |
| Motor de renderizado en tiempo real | Genera el decorado virtual cuadro a cuadro |
| Seguimiento de cámara | Le dice al motor dónde está la cámara y cómo mira |

Y por qué la tercera es la clave: sin seguimiento, el decorado virtual es un fondo plano. En
cuanto la cámara se mueve o hace zum, el fondo tiene que moverse con la perspectiva correcta, y eso
exige conocer en cada cuadro la posición, la orientación, la focal y el foco de la cámara.

Los datos que el seguimiento tiene que entregar: giro
horizontal, inclinación, balanceo, las tres coordenadas de posición, la focal y el enfoque. Con
menos de eso, la integración se rompe en cuanto la cámara deja de estar quieta.

### El seguimiento de cámara

Para que un decorado virtual funcione hay que medir la cámara en seis grados de libertad —tres de
posición y tres de orientación— más el zum y el foco, y entregar esos datos al motor que dibuja
el fondo, fotograma a fotograma y en tiempo real.

Las familias de sistemas que lo hacen:

| Familia | Cómo mide | Rasgos |
|---|---|---|
| Mecánica, por codificadores | Sensores en la cabeza, el pedestal y la grúa | Muy precisa, pero la cámara no puede salirse del soporte instrumentado |
| Óptica por marcas de referencia | Una cámara auxiliar apuntando al techo lee marcas retrorreflectantes y calcula la posición | Cámara libre por el plató |
| Óptica sin marcas | Reconocimiento del propio entorno | No hace falta preparar el techo |
| Por ultrasonidos o radiofrecuencia | Emisores y receptores repartidos por el plató | Hay que instalarlos en el plató |
| Inercial | Acelerómetros y giróscopos en la cámara | Deriva con el tiempo; se usa combinada |

La tabla es de oficio.

La documentación de un fabricante de estos sistemas, Mo-Sys, describe la segunda familia. La ficha
del StarTracker Max dice de su configuración de seguimiento:

> Tracking Stars Configuration / Ceiling, wall or floor mounted retro-reflective stickers or digital
> LED wall markers

y de su salida de datos:

> Data Output / Mo-Sys F4 / FreeD / OpenTrackIO over IP

y describe el origen del producto así:

> Mo-Sys invented 'simple-to-use' marker-based optical camera tracking for Virtual Production.

Es decir: el seguimiento se hace leyendo pequeñas marcas retrorreflectantes colocadas en el techo (o
en paredes, suelo o pantallas de LED), y FreeD es uno de los formatos en que esos datos se entregan al
motor. La misma ficha dice qué mide: **«StarTracker Max delivers 6-axis tracking with lens zoom and
focus for precision blending of photo realistic 3D virtual graphics with the real-world scenes and
objects.»** (seis ejes de posición y giro, más el zum y el foco de la óptica, para fundir el grafismo
3D con la escena real). Y por qué el sensor va en la cámara y mirando hacia fuera: **«Immune to
occlusion and blind spotting often experienced by 'outside-in' tracking systems, StarTracker Max
provides absolute 'inside-out' tracking.»** (un sensor en la cámara que mira a las marcas no se queda
ciego cuando alguien se cruza, como le pasa a un sistema de sensores fijos que miran a la cámara).

El catálogo del mismo fabricante resume para qué sirve toda la familia:

> «Mo-Sys camera tracking systems for Virtual Production, VFX and live broadcast combine ‘absolute’
> marker-based tracking (StarTracker), vSLAM support solutions, and precision encoder technology to
> deliver accurate, real-time tracking. Supporting AR graphics workflows and in-camera VFX, these
> real-time tracking systems integrate seamlessly with render engines, LED volumes, and studio
> pipelines.»

Leída en términos de oficio: el seguimiento es lo que permite mover la cámara —en pedestal, grúa o al
hombro— sin que el decorado virtual o el objeto aumentado se despeguen de la imagen real. A la
posición de la cámara se suman los datos de los codificadores de la óptica —zum y foco— para que el
decorado virtual tenga también la lente correcta. Una cámara sin seguimiento puede trabajar en plató
virtual, pero fija: el fondo se dibuja para una posición y una focal que no cambian (oficio).

### Croma o pared de LED

El decorado sintético puede ir detrás de la figura por croma o mostrarse en una pared de LED que la
cámara filma (arriba). El mismo seguimiento sirve para las dos. El catálogo de Mo-Sys explica qué
hace el seguimiento en el croma: **«In a greenscreen virtual production setup, camera tracking data
tells the compositing software how to move and scale the digital background to match the live camera,
so the composite holds together even as the camera pans, tilts, or moves through the space.»** (los
datos de seguimiento le dicen al programa de composición cómo mover y escalar el fondo digital para
que case con la cámara real mientras panoramiza, bascula o se desplaza). Y la ficha del StarTracker Max
dice que el sistema sirve igual en los dos: **«StarTracker Max is equally at home in green screen
virtual production studios and LED wall virtual production stages»**, con marcas en techo, paredes o
suelo o marcadores en la propia pared de LED.

La diferencia práctica (oficio): con croma, la figura se recorta y el decorado se incrusta, y el
problema es el recorte (bordes, rebote verde, sombras); con pared de LED no hay incrustación, la
figura recibe luz y reflejos reales del fondo, y los problemas son los de filmar una pantalla —el
moiré, el parpadeo y el retardo, en el epígrafe 3—.

### Croma y pared de paneles, cara a cara

Y la evolución que hay que nombrar, porque cambia el planteamiento: el fondo de paneles de diodos
emisores de luz. En vez de sustituir un croma en la mesa de mezclas, se proyecta el decorado
virtual en una pared de paneles detrás de los intérpretes, y la cámara lo graba de verdad.

| | Croma | Pared de paneles |
|---|---|---|
| Dónde se compone | En el control, después de la cámara | En el plató, delante de la cámara |
| Iluminación del sujeto | Hay que imitarla para que case con el fondo | La da el propio fondo: reflejos y luz correctos |
| Lo que ve el intérprete | Un fondo verde | El decorado |
| Derrame de color | Es el problema clásico | No existe |
| Su problema propio | Máscara y submuestreo | Batido entre la trama de paneles y el sensor, y el ángulo de visión |

### La pared de LED: frustum interior y exterior

En la producción virtual en pared de LED, lo que la pared enseña no es una imagen única. Epic Games, en
la documentación de Unreal Engine sobre efectos visuales rodados en cámara (*In-Camera VFX Overview*),
distingue dos zonas. La que ve la cámara es el frustum interior (*frustum* es la pirámide truncada que
forma el campo de visión de una cámara; oficio): **«This inner frustum represents the field of view (FOV) from
the camera's perspective based on the current lens focal length.»** (representa el campo de visión
desde la perspectiva de la cámara, según la focal de la óptica en ese momento). Lo demás es el
exterior: **«Content displayed on the LED volume outside of the camera's FOV is called the outer
frustum. This outer frustum turns the LED panels into a dynamic light and reflection source for the
physical set»** (lo que la pared muestra fuera del campo de visión de la cámara convierte los paneles en
una fuente dinámica de luz y de reflejos para el decorado físico). Y a diferencia del interior, no
acompaña a la cámara: **«The outer frustum remains static when the camera moves. This mimics how lights
and reflections do not move with the camera in the real world.»** (el frustum exterior se queda quieto
cuando la cámara se mueve, igual que en el mundo real las luces y los reflejos no se mueven con ella).

Leído en términos de oficio: el frustum interior se dibuja con la perspectiva exacta de la cámara, y por
eso se mueve con ella gracias al seguimiento; el exterior no sale en plano, pero ilumina a la figura y
se refleja en los objetos. Es la razón por la que en la pared de LED la luz del fondo «la da el propio
fondo», como dice la tabla anterior.

Y dentro del frustum interior puede seguir habiendo croma. Unreal Engine tiene un sistema de
composición en tiempo real: **«Composure is Unreal Engine's framework for real-time compositing. With
this suite of features, you can include live video feeds, AR compositing, green-screen keying, garbage
mattes, color correction, and lens distortion in your shots.»** (Composure permite incluir señales de
vídeo en directo, composición de realidad aumentada, incrustación por croma verde, máscaras de
descarte, corrección de color y distorsión de la óptica). Para componer en directo con croma, la misma
casa pide una tarjeta de vídeo profesional: **«If you plan to use live green-screen compositing, you
will need a SDI video card to handle camera input, compositing output, and timecode synchronization.»**
(*Recommended Hardware for In-Camera VFX*; hace falta una tarjeta SDI para la entrada de cámara, la
salida compuesta y la sincronía de código de tiempo). La razón de poner el croma sólo en el frustum
interior la da la página de Epic sobre efectos visuales rodados en cámara (*In-Camera VFX Overview*): **«Using a green screen only in the camera's FOV minimizes the
amount of green screen required for a given shot. Less green screen means less green spilling onto the
actors and set.»** (con croma sólo en el campo de visión de la cámara hace falta menos verde, y menos
verde es menos rebote de verde sobre los actores y el decorado); el exterior sigue dando la luz y los
reflejos del entorno virtual.

### La iluminación de un plató de croma

En un decorado virtual hay dos iluminaciones que resolver a la vez, y la tentación es olvidar una de
las dos (oficio).

| Qué se ilumina | Cómo | Para qué |
|---|---|---|
| El personaje | Como si estuviera en el decorado virtual: con la dirección, la dureza y la temperatura de color que tendría allí | Para que no desentone con el fondo que se le va a poner |
| El fondo de croma | Uniformemente, sin sombras, sin manchas y sin caídas hacia los bordes | Para que la incrustación tenga un solo color que declarar transparente |

Para obtener una incrustación realista y sin problemas hay que iluminar al personaje para que no
desentone con el decorado virtual y, además, iluminar el fondo uniformemente: son dos trabajos, no
uno. Los errores corrientes (oficio):

- Creer que no hace falta iluminar el fondo porque será sustituido. El fondo se sustituye precisamente
  por su color, y si el color no es uniforme el recorte no lo es tampoco: aparecen jirones, bordes
  verdes y zonas que no se van.
- Pegar al personaje al fondo para que se recorte mejor, que es justo lo contrario de lo que hay que
  hacer: cuanto más cerca está el personaje del croma, más rebote verde recibe —el *spill*— y peor
  sale el recorte. La regla es separar, no pegar. Separar al personaje del fondo es también lo que
  permite desenfocar el croma, con lo que se evitan de paso las arrugas de la tela y las juntas de los
  paneles.

El Libro de Estilo trata el vestuario de los presentadores ante la cámara (8.6.1, «Vestuario», p.
122). El punto 4 habla de la saturación del color, no de la incrustación: **«Los colores fuertes
tampoco son aconsejables. Se saturan e impregnan de ‘croma’ el cuello y el mentón.»** El punto 9 es el
que lleva el croma de incrustación al vestuario: **«Los departamentos de Estilismo y Realización
deberán tener muy en cuenta los condicionantes técnicos de cromas, transparencias o bien de la
grabación o emisión desde un plató con decorado virtual.»** Es un **«deberán»**: el realizador
responde, con Estilismo, de que el vestuario no rompa el croma. Y la regla de siempre (oficio): nadie
viste del color del fondo, porque se vuelve transparente.

### Lo que hace el grafista en un escenario virtual

Lo que el motor dibuja lo ha construido antes alguien, y en un plató virtual ese trabajo es del
grafismo (oficio): el decorado se modela, se texturiza y se ilumina en 3D como cualquier otra escena
(las técnicas son el tema 5), pero con dos condiciones que no tiene una pieza renderizada. La primera,
que el motor tiene que dibujarlo entero en cada fotograma, así que la escena se construye para que
quepa en ese tiempo: lo que no llega a tiempo no se ve más lento, se ve como un tirón (epígrafe 5). La
segunda, que el decorado tiene que casar con el plató real: la escala y el suelo del modelo, con los
del estudio; la luz virtual, con la que se ha puesto al presentador; y las zonas donde irán rótulos,
pantallas virtuales y objetos aumentados, con las marcas que se le dan al presentador. Lo que cambia
cada día —los datos de un gráfico, el contenido de una pantalla virtual— se deja como plantilla que se
rellena, no como escena que se rehace (tema 9).

### Preparar la escena para que el motor la dibuje a tiempo

Cómo se consigue que la escena «quepa» lo explica Epic Games para la pared de LED (*In-Camera VFX Best
Practices in Unreal Engine*), que plantea las dos preocupaciones de quien construye el entorno:
**«Building assets that appear realistic on an LED wall. Optimizing the environment for performance so
it runs in real time.»** (construir elementos que parezcan reales en la pared de LED y optimizar el
entorno para que corra en tiempo real). Lo que recomienda:

- Un objetivo de rendimiento con margen. En su prueba de producción fijaron **«a frame rate between
  48-72 frames-per-second (FPS) on Artist workstations when viewed in 4K full screen»** (entre 48 y 72
  fps en los puestos de los artistas, a pantalla completa en 4K), como referencia que después hubo que
  comprobar en el equipo de destino, fuera del plató, y con una salvedad: **«While a 2-3x
  target frame rate approach can provide a rough guideline for Artists, do not assume it will be
  sufficient in all cases»** (apuntar a dos o tres veces la cadencia de destino orienta, pero no basta
  en todos los casos); por eso piden pruebas de rendimiento periódicas.
- Niveles de detalle. **«Level of Detail: Use different levels of polygon counts for when a Mesh is
  rendered larger or smaller on the screen.»** (un modelo con distinto número de polígonos según lo
  grande que se vea en pantalla). Los automáticos pueden quedar blandos: **«We recommend you budget
  resources for some hand-crafted LODs.»** (reservar recursos para hacer a mano algunos LOD).
- Pocos materiales por objeto. **«Each material ID adds draw calls»** (cada material añade llamadas
  de dibujo, que cuestan rendimiento); la recomendación es un material por elemento.
- Texturas en potencias de dos. **«textures need to be a power of 2 in both dimensions, however,
  they don't have to be perfect squares»** (su ejemplo: 128 × 256 y 256 × 256 sirven; 8080 × 8080, no).
- Luz precalculada antes que trazado de rayos. **«Because ray tracing is expensive in terms of
  performance, you can achieve better-looking and more stable image quality using baked lighting with
  volumetric light maps and reflection probes.»** (como el trazado de rayos es caro, la luz precalculada,
  con mapas de luz volumétricos y sondas de reflejo, da una imagen mejor y más estable).

Y la optimización no es sólo técnica: Epic aconseja que, cuando se pueda, la versión optimizada la
apruebe quien firma el aspecto,
**«approved by the Art Director, the Production Designer, or whoever else is signing off on the look»**,
porque, si no, optimizar puede introducir diferencias visibles. La guía es de producción virtual en pared de LED; que sus
criterios sirvan igual para un decorado virtual de croma es lectura de oficio.

## 2. Realidad aumentada

### Realidad virtual, aumentada y mixta

Las tres realidades se ordenan en una escala según lo que hacen con el entorno real:

| Tecnología | Qué hace con el entorno real |
|---|---|
| Realidad virtual (RV) | Lo sustituye entero: el espectador está en otro sitio |
| Realidad aumentada (RA) | Lo conserva y le añade objetos: el espectador sigue donde estaba, con cosas nuevas encima |
| Realidad mixta (RM) | Lo conserva y le añade objetos que interactúan con él: lo virtual se ocluye detrás de lo real, se apoya en él y responde a él |

Y la manera de acertar es una sola comprobación: ¿queda algo del mundo real? En realidad
aumentada, sí. En realidad virtual, no.

Y la regla que separa la aumentada de la mixta al ver una imagen:

1. Si no se ve nada del plató, es realidad virtual.
2. Si se ve el plató y encima hay un objeto virtual que siempre queda delante de todo, es realidad
   aumentada.
3. Si se ve el plató y el objeto virtual se comporta como si estuviera allí —una persona pasa por
   delante y lo tapa, proyecta sombra, se apoya en el suelo real—, es realidad mixta. La oclusión
   es la firma: lo que distingue a la mixta de la aumentada es que lo real puede taparlo.

En televisión, un objeto de realidad aumentada que el presentador puede rodear o tapar pide, además
del seguimiento de cámara, saber qué está delante y qué detrás: es el problema del *foreground*, más
abajo (oficio).

### La realidad aumentada en el motor: vídeo que entra y sale

Para que un motor de tiempo real haga realidad aumentada tiene que recibir la señal de la cámara,
componerla con lo sintético y devolverla al control. La documentación de Unreal Engine sobre vídeo
profesional (*Professional Video IO*) parte de esa necesidad: **«Augmented reality experiences —
mixing traditional 2D video with real-time 3D environments — are becoming increasingly in demand for
film and broadcast media applications.»** (la realidad aumentada, que mezcla el vídeo 2D de siempre con
entornos 3D en tiempo real, se pide cada vez más en cine y en televisión). Y enumera lo que el motor
hace con el vídeo:

- recibirlo y componerlo: **«Play professional-level video and audio live in the Unreal Engine,
  composited into the virtual 3D world on the fly.»** (reproducir en directo vídeo y audio profesional,
  compuestos al vuelo en el mundo 3D virtual);
- tratarlo: **«Apply effects to the imported video directly in the Unreal Engine, like chroma-keying,
  lens undistortion, color correction, and more.»** (croma, corrección de la distorsión de la óptica,
  corrección de color);
- sincronizarse con él: **«Synchronize the Unreal Engine with the timecode and frame rate of your input
  video»** (con el código de tiempo y la cadencia del vídeo de entrada);
- devolverlo: **«Render video feeds from the Unreal Editor or from your running game project back out
  to your studio's video pipeline.»** (sacar la señal renderizada de vuelta a la cadena de vídeo del
  estudio).

Son las cuatro cosas que hacen falta para que un objeto aumentado salga en antena: entrada de cámara,
composición, sincronía y salida al mezclador. La corrección de la distorsión de la óptica importa en
realidad aumentada porque el objeto virtual tiene que deformarse igual que la imagen real que lo rodea
(oficio).

### Poner un objeto delante del presentador

El problema, planteado con claridad: una incrustación normal tiene dos capas. Detrás, el
decorado virtual; delante, el presentador recortado del croma. Si se quiere una tercera capa por
delante del presentador —una mesa virtual, un rótulo tridimensional, un objeto que pase por delante—,
hay que decirle al incrustador que ese trozo de imagen virtual va encima y no debajo.

Y eso es lo que hace una máscara: le dice al incrustador, píxel a píxel, qué parte de la capa
virtual va delante y qué parte va detrás. El motor de render entrega el decorado y además entrega
esa máscara; el incrustador la usa para repartir las capas.

Por eso, con un solo motor de *render*, lo que hace falta para el *foreground* es un incrustador capaz
de gestionar varias máscaras: el mismo motor puede dibujar el fondo y el primer término en una sola
salida y entregar aparte la información de qué es qué. Dos motores serían otra manera de hacerlo, no
la única. Un plató de croma es condición previa de todo el montaje, no la solución de este problema:
sin croma no hay decorado virtual, y con croma sigue sin haber *foreground* (oficio).

### El retardo de la realidad aumentada

El programa que genera la realidad aumentada tarda unos fotogramas en dibujar, y la señal aumentada
llega al mezclador más tarde que la directa. La regla es una (oficio): en televisión, todo lo que llega
antes se retrasa hasta el más lento, y el sonido se retrasa con ello. Nunca se adelanta nada, porque
nadie sabe lo que va a pasar dentro de dos fotogramas.

Un caso que hay que saber resolver. En un plató, dos cámaras tienen realidad aumentada a través de un
programa que genera un retardo de 2 fotogramas; otras cinco cámaras no la tienen; y se van a hacer
transiciones entre una cámara con realidad aumentada y la misma cámara sin ella. La misma cámara
entra, pues, dos veces al mezclador —directa y aumentada—, y las entradas no son siete sino nueve:

| Entrada | De dónde viene | Retardo que trae |
|---|---|---|
| Cámaras 1 a 7, señal directa | De la cámara al mezclador | 0 |
| Cámaras 1 y 2, señal con realidad aumentada | De la cámara al programa de realidad aumentada y de ahí al mezclador | 2 fotogramas |

La solución: un retardo de 2 fotogramas en las siete entradas directas y aviso a sonido para que
retrase 80 milisegundos todas las fuentes de sonido del plató. Las siete, y no sólo las cinco sin
realidad aumentada: las directas de las cámaras 1 y 2 son justamente las que se van a mezclar con
sus propias versiones aumentadas, y si no se retrasan, al cortar entre ellas habría un salto de 2
fotogramas. Y sí se puede mezclar una cámara con su versión aumentada: el retardo se compensa (oficio).

La aritmética del sonido:

A 25 fotogramas por segundo, un fotograma dura 40 milisegundos, porque 1.000 ÷ 25 = 40. Por tanto:

| Fotogramas | Milisegundos a 25 fps |
|---|---|
| 1 | 40 |
| 2 | 80 |
| 3 | 120 |
| 4 | 160 |

Dos fotogramas son 80 milisegundos; 160 serían cuatro. La cadencia de 25 fotogramas por segundo es la
de la familia europea, y es la que hace que dos fotogramas sean 80 milisegundos; a otras
cadencias el número cambia —a 50 fotogramas por segundo, dos fotogramas son 40 milisegundos— (cuenta:
1.000 ms entre la cadencia).

## 3. Pantallas

### Las pantallas del plató

En un plató moderno el decorado es, en buena parte, pantallas: paneles de LED, retroproyección,
monitores empotrados. Y esas pantallas no enseñan el programa por defecto: enseñan lo que se les
mande, y decidir qué se les manda es una tarea de realización.

El Libro de Estilo las cuenta entre los recursos del realizador de informativos: **«En ello tienen
gran importancia las crecientes posibilidades del medio: conexiones en directo, uso normalizado de
satélites, presencia de otros centros de producción, infografías, ‘vidi wall’, pantallas de plasma...
cuyo uso precisa cierto sentido estético y de una capacidad notable para aprovechar y armonizar los
recursos disponibles.»** (6.5.2, p. 93). Y en los cierres de un informativo, cuando el vídeo final
sustituye a la cabecera de salida, **«el realizador puede arbitrar numerosas variantes estéticas
(vidiwall, croma...)»** (3.10, p. 53).

Lo que puede ir en una pantalla de plató:

| Contenido | De dónde sale |
|---|---|
| Grafismo de fondo | Del programa de gestión de pantallas, con su propio servidor |
| El programa | De un bus auxiliar o de un banco M/E |
| Una conexión exterior | De la matriz, para «abrir una ventana» en el decorado |
| Un vídeo | Del servidor de vídeo |
| El marcador o los datos | De un sistema de datos |

### Tres problemas técnicos

Y hay tres restricciones que hacen de esto un problema técnico y no una decisión estética (oficio):

1. El moiré: la trama de la pantalla y la del sensor interfieren, y se resuelve desenfocando la
   pantalla o cambiando el tamaño con que la cámara la ve. En una pared de LED, la medida que manda es el paso de píxel (*pixel pitch*),
   la distancia entre los diodos, que suele darse en milímetros: la documentación de Unreal Engine (Epic
   Games) lo define como **«the distance between each LED light. The closer the LEDs are together—the
   lower the pitch—the higher the pixel density»** (cuanto más juntos los diodos, menor el paso y
   mayor la densidad de píxeles), y advierte que **«The combination of the distance from the screen,
   pixel pitch, and camera sensor size will help you determine how far away you should shoot your
   subject from the LED wall without seeing any visible artifacts.»** (la distancia a la pantalla, el
   paso de píxel y el tamaño del sensor ayudan a determinar a qué distancia se puede rodar sin que se vean
   defectos). Cuanto menor es el paso, más cerca puede ponerse la cámara (oficio, deducido de lo
   anterior). La misma fuente da dos remedios: **«It is recommended to have the camera's focus placed
   either in front or behind the LED surface so that the image is slightly out of focus.»** (el foco,
   delante o detrás de la superficie de LED) y, como el moiré aparece más con la cámara muy oblicua a la pared,
   **«Try to maintain a perpendicular angle of the camera to the LED's surface where possible.»**
   (cámara perpendicular a la pared cuando se pueda).
2. El retardo: el programa que gestiona las pantallas tarda en pintar (más abajo).
3. La realimentación: si a una pantalla que sale en imagen se le manda el programa, y el programa la
   está enseñando, se produce un túnel infinito. Por eso a las pantallas nunca se les manda el
   programa a secas.

Y un cuarto, que es de iluminación: las pantallas de LED, como cualquier fuente de luz, pueden
parpadear en cámara si su refresco no casa con la obturación (oficio).

### Cómo se manda una señal a las pantallas

Una pantalla se alimenta desde la matriz, desde una salida auxiliar del mezclador o desde un banco M/E
propio (oficio).

Un caso que hay que saber resolver: en una retransmisión deportiva hay que mandar la señal del
programa a las pantallas del pabellón durante todo el evento, pero sin que se vean las repeticiones ni
los vídeos.
El motivo (oficio): una repetición en la pantalla del pabellón puede provocar protestas del público
contra una decisión arbitral.

La solución es enviar a las pantallas otro banco M/E distinto del programa, enlazarlo al programa y
cambiar el mapeado de ese banco para que no tenga los vídeos. Cómo funciona, pieza por pieza (oficio):

1. Otro banco M/E. Se construye una segunda salida completa, independiente del programa.
2. Un enlace (*link*) al programa. El banco sigue automáticamente al de programa: lo que el realizador
   pincha en programa se pincha solo en el otro banco, sin que nadie tenga que operarlo.
3. Un mapeado distinto. El mapeado es la correspondencia entre botones y fuentes, y es un atributo
   por banco. Si en ese banco el botón donde el programa tiene el servidor de repeticiones apunta a
   otra cosa —a la cámara máster, por ejemplo—, cuando el programa pinche la repetición, la pantalla
   pinchará la cámara.

Con eso la pantalla lleva el programa siempre, y cuando el programa lleva una repetición, la pantalla
lleva otra cosa. Las soluciones que no valen: una tabla de sustitución en el enlace es una capa
añadida al enlace, no una propiedad del banco, y el mapeado del banco es un ajuste permanente que no
depende de que el enlace esté activo; y una macro que cierre la pantalla a negro cuando se selecciona
un vídeo en previo deja la pantalla en negro en lugar de darle contenido y depende de que el vídeo
pase por previo, cosa que en directo no siempre ocurre (oficio).

### El retardo de las pantallas y cómo se compensa

Todo procesado añade retardo. El programa que gestiona una pared de LED recibe una señal, la
escala, la reparte entre los paneles y la pinta: eso lleva unos cuantos fotogramas. Si por esa
pantalla entra una conexión en directo, la imagen del exterior llega al plató más tarde que su
sonido, y el resultado es un desfase visible.

Un caso que hay que saber resolver: un plató cuyo decorado son pantallas de LED gestionadas por un
programa que produce un retardo de 4 fotogramas, y conexiones en directo con exteriores a través de
ventanas abiertas en esas pantallas. El audio y el vídeo no van sincronizados. La solución es
retrasar la entrada de los exteriores al mezclador 4 fotogramas, mandarlos a las pantallas por matriz
y retrasar el sonido de los exteriores 4 fotogramas. Por qué esas tres cosas a la vez (oficio):

| Acción | Qué corrige |
|---|---|
| Mandar el exterior a las pantallas por matriz, no por un auxiliar del mezclador | Que la señal llegue a la pantalla por el camino más corto, sin pasar por el mezclador: así el único retardo que sufre es el del programa de pantallas, y es un retardo conocido y constante |
| Retrasar 4 fotogramas la entrada del exterior al mezclador | Que la imagen que el mezclador toma del exterior coincida con la que se está viendo en la pantalla del plató. Las cámaras del plató filman la pantalla, que va 4 fotogramas retrasada; si el mezclador tuviera el exterior sin retrasar, al cortar de la pantalla al exterior habría un salto de 4 fotogramas |
| Retrasar 4 fotogramas el sonido del exterior | Que el sonido acompañe a la imagen |

Mandar la señal a las pantallas por un auxiliar del mezclador añade el retardo del mezclador al del
programa de pantallas, y adelantar la entrada es imposible: una señal no se puede adelantar, sólo se
puede retrasar lo demás. A 25 fotogramas por segundo, cuatro fotogramas son 160 milisegundos
(epígrafe 2).

### El programa de gestión de pantallas

El «programa de gestión de pantallas» de las tablas anteriores es un producto concreto en cada casa. Un
ejemplo con documentación publicada es Viz Multiplay, de Vizrt (*Viz Multiplay User Guide* 3.3,
«Introduction»): **«Viz Multiplay is a powerful tool for controlling studio screen content. The simple
interface can be used in the control room or by the presenter in the studio.»** (una herramienta para
controlar el contenido de las pantallas del plató, que se maneja desde el control o por el propio
presentador en el plató). Sus funciones: **«Send content quickly to multiple screens.»** (mandar
contenido a varias pantallas), **«Control live, video, graphics and still images.»** (controlar
señales en directo, vídeo, grafismo e imágenes fijas) y **«Build playlists and full content
editing.»** (construir listas de reproducción y editar el contenido).

Tres rasgos de su arquitectura enlazan las pantallas con el resto del grafismo:

- el motor que pinta es el mismo que el de los rótulos: **«Uses Viz Engine for playout»** (emite con
  Viz Engine, el motor de grafismo en tiempo real de Vizrt; epígrafe 5);
- se enlaza con la redacción: **«Can open and control newsroom playlists in a MOS workflow.»** (abre y
  controla las listas de la redacción mediante MOS);
- usa las plantillas de siempre: **«You are able to access and use templates and elements from Pilot
  Data Server.»** (accede a las plantillas y elementos del servidor de datos de Viz Pilot).

Leído en términos de oficio: lo que va en una pantalla de plató se diseña y se prepara como cualquier
otro gráfico —en plantilla, con los mismos datos y la misma identidad— y entra en la escaleta del
programa. Lo que cambia es la salida: no va al mezclador con relleno y llave, sino a los paneles, por la salida
de la gráfica o, según la misma guía, también por SDI (epígrafe 4).

### Lo que el grafista prepara para cada pantalla

Antes del programa, para cada pantalla del plató (oficio):

| Qué | Por qué |
|---|---|
| El lienzo: resolución y proporción reales de la pantalla | Una pantalla de plató rara vez es 16:9 ni tiene la resolución de la señal; lo que se diseña a otro tamaño se deforma o se escala |
| Qué muestra en cada bloque de la escaleta | Fondo, conexión, vídeo o datos, y quién la cambia y a la orden de quién |
| Qué parte sale en plano en cada cámara | Lo que no sale en ningún plano no necesita detalle; lo que sale detrás del presentador no debe competir con él |
| Brillo y contraste del fondo | Un fondo muy luminoso deslumbra en cámara y recorta mal la figura del presentador |
| Que no haya texto importante detrás del rótulo | La pantalla forma parte del decorado: su contenido tiene que casar con el grafismo del programa y no competir con el rótulo que va encima |
| Tramas finas y rayados | Son los dibujos que más moiré provocan al filmarse |

Es la parte que toca al grafismo de lo que el Libro de Estilo dice del uso de las pantallas en un
informativo, que **«precisa cierto sentido estético y de una capacidad notable para aprovechar y
armonizar los recursos disponibles»** (6.5.2, p. 93, citado arriba).

## 4. Videowalls

### Qué es un videowall

Un videowall es una pantalla grande hecha de muchas pequeñas que se comportan como una sola: la imagen
se reparte entre ellas y el espectador la ve entera (oficio). En el plató se usa como decorado, como
ventana para las conexiones y, en la producción virtual, como fondo que la cámara filma (epígrafes 1 y
3). El Libro de Estilo lo nombra como **«‘vidi wall’»** entre los recursos del informativo (6.5.2, p.
93) y como **«vidiwall»** entre las variantes estéticas de un cierre (3.10, p. 53).

Hay videowalls de LED y de monitores LCD unidos (oficio). El tema desarrolla el de LED, que es el que
describe la documentación leída; del de LCD no se ha leído fuente (véase «Lo que este tema no da»).

### Armarios y procesador

La documentación de Unreal Engine (*In-Camera VFX Overview*) describe cómo está hecha una pared de LED.
La unidad es el armario (*cabinet*), un módulo con su resolución fija: **«An LED volume is made up of a
cluster of cabinets. Each cabinet has a fixed resolution that can range from a very low resolution,
such as 92x92 pixels that can be used for outdoor signs, to 400x450 pixels for ultra-high-resolution
indoor displays. The physical size of each cabinet can vary from manufacturer to manufacturer.»** (una
pared de LED es un conjunto de armarios; cada uno tiene una resolución fija, que va de muy baja, como
92 × 92 píxeles, propia de rótulos de exterior, a 400 × 450 píxeles en pantallas de interior de muy
alta resolución; el tamaño físico de cada armario varía de un fabricante a otro).

Lo que convierte los armarios en una sola pantalla es el procesador de LED: **«The LED processor is the
hardware and software that combines multiple cabinets into an array that displays a single image. You
can arrange the cabinets in any configuration inside the canvas that the LED processor drives. On a
large LED stage, there could be ten or more LED processors driving a seamless LED wall.»** (el
procesador es el equipo y el programa que combina varios armarios en una matriz que muestra una sola
imagen; los armarios pueden disponerse en cualquier configuración dentro del lienzo que el procesador
gobierna, y en un plató grande puede haber diez procesadores o más para una sola pared sin juntas).

Consecuencia para el grafista (oficio): el lienzo que se diseña para un videowall no es una resolución
de vídeo, sino la suma de los píxeles de los armarios en la disposición que tengan. Una pared de 8
armarios de ancho por 3 de alto con armarios de 400 × 450 píxeles tiene un lienzo de 3.200 × 1.350
píxeles (8 × 400 y 3 × 450). Esa es la resolución a la que se diseña, y la cuenta se hace con la
resolución del armario que se tenga, que cambia con el fabricante.

### El paso de píxel

La medida que caracteriza una pared de LED es el paso de píxel, la distancia entre los diodos
(epígrafe 3). Cuanto menor, más densidad, pero la misma fuente avisa de que no es el único criterio:
**«A higher pixel density means a noticeable increase in resolution and quality—and higher cost for
each cabinet. A cabinet with a lower pixel pitch does not ensure it will be the correct product for
your production, as other factors, such as viewing angle, color shift, color consistency, and heat
dissipation, must also be considered.»** (más densidad es más resolución y calidad, y más coste por
armario; un paso menor no asegura que sea el producto adecuado, porque cuentan también el ángulo de
visión, el desplazamiento del color, la uniformidad del color y la disipación del calor).

Resumido: un paso menor da más densidad y cuesta más (según la fuente); que permita acercar la cámara a la
pared sin que aparezca moiré es deducción de oficio (epígrafe 3); el ángulo de visión y el
desplazamiento de color importan porque la cámara no siempre mira la pared de frente (oficio).

### Muchas pantallas, un solo lienzo

Cuando el contenido de la pared lo genera un motor en tiempo real, el trabajo puede repartirse entre
varias máquinas. Unreal Engine lo hace con nDisplay (*nDisplay
Overview*): **«Every nDisplay setup has a single primary computer, and any number of additional
computers, called secondary nodes.»** (un ordenador principal y los secundarios que hagan falta,
llamados nodos) y **«Each Unreal Engine instance handles rendering to one or more display devices,
such as screens, LED displays, or projectors.»** (cada instancia del motor dibuja para uno o varios
dispositivos: pantallas, paredes de LED o proyectores).

Entre lo que el sistema garantiza hay dos cosas: que todos dibujen a la vez y que cada uno dibuje su
trozo con la perspectiva correcta. El plugin **«ensures all instances render the same frame at the same time,
ensures each display device renders the correct frustum of the game world»** (garantiza que todas las
instancias dibujan el mismo fotograma al mismo tiempo y que cada dispositivo dibuja el frustum que le
corresponde). La perspectiva se consigue colocando cada pantalla virtual donde está la real: **«By
setting up these viewports so that their location in the 3D world matches the physical locations of
the screens or projected surfaces in the real world, you give viewers the illusion of being present
and immersed in the virtual world.»**

El reparto de las salidas se dibuja en un lienzo 2D: **«Using the Output Mapping tool, these separate
viewports are then mapped into different areas of a large 2D canvas, referred to as the application
window.»** (cada vista se asigna a una zona de un gran lienzo 2D, la ventana de la aplicación), y Epic
recomienda que la tarjeta gráfica trate varias salidas como una: **«We recommend leveraging
multi-display technologies from graphics card vendors such as NVIDIA Mosaic or AMD Eyefinity to treat
multiple connected displays as one display.»**

Y si una máquina cae, el resto puede seguir. La tolerancia a fallos (*failover*) de nDisplay sólo cubre
los fallos de los nodos que se detectan por la red y hay que activarla en la configuración del clúster
(política **«Drop S-node on fail»**); activada, **«when a render node becomes unresponsive, whether because of a
crash or because it loses its network connection, it is dropped from the cluster after a configurable
timeout value.»** (un nodo que deja de responder, porque se cuelga o pierde la red, sale del clúster
tras un tiempo de espera configurable). En directo, eso significa que el trozo de pared que pintaba
deja de actualizarse, y hay que tener previsto qué se hace entonces (oficio).

### La sincronía: genlock

Una pared hecha de muchas partes sólo parece una si todas cambian de imagen a la vez, y a la vez que
la cámara. Epic: **«Each device, such as the camera, computers, and tracking systems, has an internal
clock. […] This can cause problems in the resulting display, such as tearing, if they are not unified.
Genlocking with nDisplay prevents these issues.»** (cada dispositivo —cámara, ordenadores, seguimiento—
tiene su reloj; si no se unifican, aparecen defectos como el desgarro de la imagen, y el genlock, el
enganche de todos a una misma referencia de sincronismo, lo evita).

Lo que hace falta para ello, según la guía de equipos de Epic (*Recommended Hardware for In-Camera
VFX*): en los ordenadores, **«NVIDIA Quadro Sync is required to synchronize displays across an LED
volume. Each render node machine must have this card in addition to its graphics card.»** (cada nodo
necesita, además de su tarjeta gráfica, una tarjeta de sincronía); y en los procesadores, **«Most LED
processors have the option to receive sync either from an external genlock source or from the
incoming video signal from the graphics cards.»** (la mayoría de los procesadores de LED toman el
sincronismo de una referencia externa o de la señal que les llega de las tarjetas gráficas).

### El color que se manda a la pared

La pared no es un monitor de referencia ni una señal de emisión, y el color se trata en consecuencia.
Epic pide mandarle la imagen sin la curva tonal del motor: **«Ensure that the tonemapper is disabled so
content from the engine does not have a tone curve and is in linear sRGB color space as input to the
LED panels.»** (desactivar el mapeo tonal para que el contenido llegue a los paneles sin curva y en
espacio sRGB lineal). Para gestionar el color entre el motor, la pared y la cámara recurre a OCIO:
**«OpenColorIO, or OCIO, is a color management system used primarily in film and virtual
production.»** Qué espacio de color concreto pide cada pared lo fija su fabricante (oficio); la colorimetría
de la señal de emisión es el tema 8.

### Lo que no funciona en un clúster

Algunos efectos del motor calculan su resultado a partir de lo que hay en la pantalla que se está
dibujando, y en una pared repartida entre varios nodos cada nodo sólo ve su trozo (oficio). Epic pide evitarlos:
**«Screen spaced effects such as SSGI, SSAO, SSR, vignetting, eye-adaptation, and bloom should be
avoided. Since the nature of these effects are screen spaced, there can be issues with borders between
two clustered nodes in the nDisplay system.»** (deben evitarse los efectos en espacio de pantalla —tres que
Epic nombra sólo por sus siglas, SSGI, SSAO y SSR, y el viñeteado, la adaptación de la exposición y el resplandor o *bloom*—, porque dan problemas en
las juntas entre dos nodos). Para el grafista, la lección es de oficio: un efecto que queda bien en un
monitor puede partir la imagen en la pared, y se prueba en la pared.

### El videowall en un sistema de grafismo de televisión

Fuera de la producción virtual, lo corriente en un plató es que la pared muestre grafismo, vídeo y
conexiones que se lanzan como cualquier otro gráfico. Vizrt lo resuelve dentro de Viz Multiplay
(epígrafe 3): **«The video wall feature allows up to four DisplayPort outputs with UHD resolution from a
single GPU in a Viz Engine. With Datapath Fx4 display controllers, the number of outputs can be
increased to match numerous screens and panels of different shapes and orientations.»** (hasta cuatro
salidas DisplayPort en UHD desde una sola tarjeta gráfica de un Viz Engine; con controladores de
pantallas Datapath Fx4, las salidas aumentan para alimentar muchas pantallas y paneles de formas y
orientaciones distintas) y **«Also supports Standard SDI-based playout.»** (también admite la salida
SDI normal).

En un videowall, la salida no es la de los rótulos. El manual de Viz Engine (*Administrator Guide* 5.4,
«Video Output») lo dice en su opción de videowall: **«Video Wall/Multi-Display: Sets the main output to
the Digital Visual Interface (DVI). Important: For video wall setups, this setting must be active and
the output format must be set to FULLSCREEN.»** (la salida principal pasa a la interfaz visual digital,
DVI, y para un videowall ese ajuste debe estar activo y el formato de salida en pantalla completa). Es
decir (oficio): para la pared, el motor pinta a pantalla completa por la salida de la gráfica, sin la
pareja de relleno y llave que va al mezclador.

## 5. Grafismo en tiempo real

### El motor de representación en tiempo real

Un motor de representación en tiempo real es el programa que dibuja el decorado sintético tantas
veces por segundo como fotogramas tenga la señal. Es la pieza que hizo posible que el decorado
virtual dejara de parecerlo.

Unreal Engine es un ejemplo. El motor necesita los datos de seguimiento para saber desde dónde
dibujar, y la ficha del StarTracker Max lo dice al describir su salida:

> delivering low latency camera tracking data over IP (Mo-Sys F4, FreeD, OpenTrackIO) into real-time
> render engines such as Unreal Engine

Seguimiento y motor son las dos mitades del mismo sistema.

### Diferido y tiempo real

Por qué un motor de videojuego está en el temario de un grafista de televisión: porque la
escenografía virtual y la realidad aumentada de los platós se calculan hoy con ellos. Lo que antes
se renderizaba durante horas se calcula ahora en el mismo instante en que la cámara se mueve, y esa
es toda la diferencia entre el grafismo grabado y el grafismo en directo.

Los dos modos de trabajo que conviene distinguir:

| Modo | Cuándo se calcula la imagen | Ejemplos |
|---|---|---|
| Renderizado diferido | Antes de emitir, todo el tiempo que haga falta | Blender, Cinema 4D |
| Tiempo real | Mientras se emite, a la velocidad del vídeo | Unreal, Unity, Vizrt, Chyron |

Lo que distingue al grafismo del control del de postproducción es el tiempo real (oficio). Un
programa de composición como After Effects trabaja por renderizado:
After Effects compone fotograma a fotograma y entrega un fichero; no tiene entrada de vídeo en
directo ni salida a la que un mezclador pueda enchufarse. Es la herramienta con la que se preparan
antes las cabeceras y las ráfagas que después dispara un servidor.
El sistema de grafismo del control, en cambio, genera el rótulo en el momento y lo entrega al
mezclador como una fuente más, con su relleno y su llave. Lo mismo vale para el decorado
virtual y la realidad aumentada: sólo sirve para el directo un motor que dibuje la imagen tantas
veces por segundo como fotogramas tenga la señal.

El tema 1 trata la misma distinción desde el diseño.

### Cuántos motores hacen falta

Un plató virtual con varias cámaras necesita más de un motor de *render*.
El porqué: un motor de render dibuja el decorado virtual desde un punto de vista concreto. Ese
punto de vista es el de una cámara, con su posición, su orientación y su focal. Dos cámaras
distintas ven el decorado desde sitios distintos, así que necesitan dos dibujos distintos, calculados
a la vez, veinticinco o cincuenta veces por segundo.

La cuenta, por tanto, es uno por cámara que pueda salir al aire (oficio). Una cabeza caliente —una
cabeza robotizada con la cámara montada encima, colgada de una grúa o de un raíl— es una cámara más:
tres cámaras y una cabeza caliente son cuatro puntos de vista y cuatro motores. La cabeza caliente no
necesita dos motores; lo que necesita es que su seguimiento resuelva más ejes —la posición del brazo
además de la de la cabeza—, y eso es seguimiento, no *render*.

Tampoco basta un solo motor muy potente para todas: el problema no es de cálculo, sino de
simultaneidad. Cada salida tiene que estar disponible al mismo tiempo, porque el realizador puede
cortar a cualquiera en cualquier momento; un decorado virtual renderizado sólo para la cámara que
está en el aire dejaría el previo vacío y no se podría preparar el corte. Existen arquitecturas que
reparten varios puntos de vista en una sola máquina con varias tarjetas, y eso no cambia la cuenta:
sigue habiendo un motor por punto de vista, aunque compartan chasis (oficio).

### Las dos exigencias del tiempo real

Y las dos exigencias temporales que hacen difícil todo esto:

1. El decorado se genera en tiempo real. Un cuadro por cadencia, sin fallar ninguno, y una
   caída de rendimiento se ve como un tirón.
2. Hay que alinear los retardos. El motor tarda en renderizar y el seguimiento en medir, así
   que la señal de cámara se retarda lo mismo para que fondo y figura correspondan al mismo
   instante. Un desajuste de un solo cuadro se ve como si el decorado flotara.

### Qué hace un sistema de grafismo

Qué hace un sistema de grafismo, en cuatro funciones:

| Función | Qué es |
|---|---|
| Diseño | Crear las plantillas: tipografía, color, animación, retícula |
| Datos | Rellenar esas plantillas con contenido, a mano o desde una fuente |
| Reproducción | Sacarlas en el instante justo, con su alfa |
| Control | Decidir qué sale y cuándo: manual, desde la escaleta o desde una automatización |

El reparto entre quien diseña la plantilla, quien la rellena y quien la lanza es el tema 3; las
plantillas y su automatización, el tema 9.

La reproducción «con su alfa» se hace, en un sistema de grafismo de directo, por dos salidas: el
relleno, que es la imagen, y la llave, que dice dónde es transparente (oficio; el alfa en la entrega
es el tema 8). En Vizrt, que una salida entregue la llave es una propiedad de esa salida de vídeo
(*Viz Engine Administrator Guide* 5.4, «Video Output», propiedades de la llave): **«Contains Alpha:
Defines if this output channel provides key information on the associated key output connector.»**
(define si ese canal de salida entrega la información de llave por su conector de llave asociado). No
hace falta, por tanto, un modo especial para tener relleno y llave (se deduce de que sea una propiedad
de cada salida; oficio). Otra cosa es el modo de doble canal
(*Viz Engine Administrator Guide* 5.2, «Dual Channel Mode»), que sirve para tener dos salidas de
programa: **«Dual Channel is a video version with, typically, two program outputs (fill and key on two
channels). To support two program outputs, this option requires two graphics cards.»** (normalmente dos
salidas de programa, con relleno y llave en dos canales; para dos salidas de programa exige dos
tarjetas gráficas). En ese modo, el motor
puede gobernarse desde sus consolas o desde fuera: **«use an external application (for example, Viz Trio or Viz Pilot) to control the Viz
Engine.»** (una aplicación externa, como Viz Trio o Viz Pilot, controla el Viz Engine). Es la
separación entre el motor que dibuja y el control que decide qué sale y cuándo, las dos últimas filas de
la tabla.

### Tres sistemas, con la documentación de su fabricante

El temario no nombra producto alguno. Los tres que siguen se describen porque tienen documentación
publicada que se ha leído, y con lo que dice el fabricante; eso vale para saber qué hace cada uno, no
para valorarlo, y no significa que Canal Sur los use.

Vizrt (Viz Artist y Viz Engine). Es un conjunto de programas con varios modos, entre ellos el de
diseño y el de emisión: **«Throughout this guide, the term Viz refers to the complete software suite installed,
and as a general reference for the following modes: Viz Artist / Viz Engine […] / Viz Configuration»**
(*Introduction to Viz Artist* 5.3; «Viz» designa el conjunto instalado y sus modos: Viz Artist, Viz
Engine y la configuración). En Viz Artist se diseñan las escenas; Viz Engine las emite (oficio, por la
división de modos y porque Viz Multiplay **«Uses Viz Engine for playout»**). Lo que cada instalación puede hacer depende de su licencia: **«The available
features and modes of the software depend on the license on the connected license hardware
dongle.»** (las funciones y los modos disponibles dependen de la licencia de la llave física
conectada). La misma casa controla pantallas con Viz Multiplay (epígrafes 3 y 4) y rellena plantillas
con Viz Pilot (tema 9).

Unreal Engine (Epic Games), Motion Design. El motor de los escenarios virtuales tiene también un
conjunto de herramientas para grafismo de emisión, que la documentación de Unreal Engine 5.8 lleva con
la etiqueta **«experimental»**: **«Motion Design is a feature set for motion
graphics artists who need a streamlined and creative suite of tools that provide for rapid iteration
and scalability. Motion Design includes a reworked world outliner, user interface, rigging tools,
cloners, customizable 2D/3D shapes, and a new way to create materials using a streamlined, layer-based
workflow called Material Designer.»** (un conjunto para artistas de *motion graphics*, con
herramientas de rigging, clonadores, formas 2D y 3D personalizables y un editor de materiales por
capas, Material Designer). Su uso en directo: **«Motion Design offers a robust Rundown tool that, in
conjunction with its Transition Logic system, can run live-updated broadcast graphics with minimal
rigging.»** (una herramienta de escaleta, *Rundown*, que con su sistema de lógica de transiciones emite
grafismo actualizado en directo) y, según su guía de inicio, **«Motion Design is an Internal Editor
plugin for broadcasting. You can use it for graphics creation, playout, and real-time data
visualization for live television, news, weather, sports production, interstitial graphics»**
(creación, emisión y visualización de datos en tiempo real para televisión en directo, informativos,
meteorología, deportes y piezas de continuidad). Su visor lleva dos controles que el grafista de
televisión conoce: **«color channel visualizer (useful for previewing the alpha channel)»** (para ver
el canal alfa) y **«safe frame toggle»** (para mostrar la zona segura; la zona segura es el tema 8).

Chyron (PRIME). Su módulo de rotulación: **«A module of the PRIME Platform™, PRIME CG™ offers
powerful 3D real-time graphics rendering, intuitive authoring tools and flexible playout capabilities
to easily create and air sophisticated lower thirds, over-the-shoulders, bugs and other
character-generated graphics.»** (representación 3D en tiempo real, herramientas de creación y
emisión para rótulos inferiores, gráficos sobre el hombro del presentador, moscas y demás grafismo de
generador de caracteres). Trabaja con **«timelines, a spline editor, and a full set of effects,
available for keyframing»** (líneas de tiempo, editor de curvas y efectos animables por fotogramas
clave) e importa de las herramientas de diseño: **«full Adobe®️ Photoshop + After Effects import and
Autodesk™️ FBX®️»**. Sus plantillas se llaman *Base Scenes*: **«Base Scenes, our templatized graphics
creation feature, streamlines design workflows.»**, y las escenas se alimentan de datos: **«Logic-based
scenes function as editable templates that designers can configure to refresh up-to-the-second based
on data feeds and trigger controls.»** (plantillas editables que se actualizan al segundo con fuentes
de datos). Con la redacción se enlaza a través de Chyron CAMIO: **«For pre-planned productions, PRIME CG
integrates with all leading newsroom computer systems via Chyron CAMIO.»** Y la plataforma no se
limita a los rótulos: **«The PRIME Platform™ may be deployed with a range of functionalities, from
graphics, to vision mixing, branding, video walls, venue control, touchscreen and more.»** (grafismo,
mezcla, identidad de canal, videowalls, control de recintos y pantallas táctiles). La versión 5.3
añadió contenido web: **«PRIME 5.3 delivers the first official integration of HTML content within
PRIME, through a powerful and flexible HTML Input.»** (nota de prensa de 12-II-2026).

Lo que los tres tienen en común (oficio): un entorno de diseño donde se hace la escena o la plantilla,
un motor que la dibuja a la cadencia del vídeo, una forma de rellenarla con datos o con la escaleta de
la redacción y una salida al mezclador o a las pantallas. Son las cuatro funciones de la tabla
anterior.

### La conexión con la redacción y los datos

Un sistema de grafismo en tiempo real no trabaja aislado. Con quién habla (oficio):

| Con quién | Para qué |
|---|---|
| Sistema de redacción | El rótulo sale de la escaleta, no se teclea dos veces; uno de los enlaces es el protocolo MOS, que cita Viz Multiplay (epígrafe 3) |
| Bases de datos externas | Resultados, elecciones, meteorología, mercados: el dato entra solo |
| Mezclador y automatización | Quién dispara el gráfico |
| Pantallas del plató | Qué se ve en el decorado (epígrafes 3 y 4) |
| Postproducción | Elementos con alfa para composiciones (tema 5) |

Tres reglas de oficio para esa integración:

1. Un dato se teclea una vez. Si el nombre de un invitado se escribe en la escaleta y otra vez
   en el grafismo, algún día no coincidirán, y coincidirá en directo.
2. Las plantillas son del programa, no del operador. Un grafismo hecho a mano cada día se
   desvía, y la identidad visual del canal se deshace sin que nadie lo decida.
3. Lo automático necesita un camino manual. Cuando la base de datos externa falla —y falla en
   una noche electoral—, tiene que poder teclearse. Un sistema sin ese camino deja la pantalla en
   blanco.

## Aplicación práctica

### Un plató virtual con tres cámaras y una cabeza caliente, y realidad aumentada en dos

- Motores: uno por punto de vista, cuatro en total.
- Seguimiento: cada cámara con el suyo, con zum y foco; la cabeza caliente con los ejes del brazo.
- Retardos: todas las entradas directas retrasadas hasta la más lenta; a 25 fps, cada fotograma son
  40 ms, y el sonido se retrasa lo mismo.
- Luz: el fondo de croma uniforme y el presentador iluminado como si estuviera en el decorado; el
  presentador separado del fondo; vestuario sin el color del croma (oficio) y, mejor, sin colores
  fuertes, que el Libro de Estilo desaconseja (8.6.1).
- *Foreground*: si un objeto virtual pasa por delante del presentador, un incrustador con máscaras.

### Lo que se comprueba en el ensayo de un plató virtual

Un plató virtual se ensaya como cualquier otro, y además (oficio):

| Qué | Por qué |
|---|---|
| Que cada cámara tiene su seguimiento calibrado y su motor | Sin ello, el fondo se despega al mover la cámara |
| Que el zum y el foco de la óptica llegan al motor | Si no, al cerrar plano el fondo no acompaña |
| Que la figura no pisa las zonas que el motor no dibuja | Fuera del decorado sintético se ve el estudio |
| Las marcas del presentador respecto a los objetos virtuales | El presentador no ve el decorado: se orienta por marcas en el suelo y por un monitor de retorno |
| El orden de las capas si hay objetos delante del presentador | Una máscara mal hecha pone el objeto detrás |
| El retardo de cada entrada y el del sonido | Una cámara aumentada o virtual llega más tarde que la directa |
| La luz del personaje frente a la del decorado | Dirección, dureza y temperatura de color tienen que casar |

A esa lista el grafista añade lo suyo (oficio): que el decorado se dibuja entero en cada fotograma sin
tirones con todas las cámaras en marcha; que los rótulos y los objetos aumentados caen dentro de la zona
segura en todas las cámaras; y que lo que se va a rellenar con datos entra y sale bien con los textos
más largos previstos.

### El videowall de un informativo

Un plató de informativos con una pared de LED de fondo, que muestra grafismo de cabecera, la ventana de
las conexiones y un gráfico de datos (oficio, con las fuentes citadas arriba):

1. El lienzo: la resolución real de la pared, que es la suma de la de sus armarios en su disposición
   (epígrafe 4), y qué zonas de ella entran en cada plano de cámara.
2. Los fondos: diseñados a ese tamaño, sin tramas finas ni rayados, con brillo contenido y sin texto
   importante donde irá el presentador o el rótulo.
3. Los datos y los gráficos: en plantillas del mismo sistema que el resto del grafismo, rellenables
   desde la escaleta, con un camino manual si falla la fuente de datos.
4. Las conexiones: la señal del exterior a la pared por matriz; la entrada del exterior al mezclador y
   su sonido, retrasados lo que tarde en pintar la pared (a 25 fps, cada fotograma, 40 ms).
5. Que nunca vaya a la pared el programa a secas, para no provocar realimentación.
6. En el ensayo, con cámara: moiré, parpadeo, desfase entre armarios o nodos, y efectos que se parten
   en las juntas.

### Cuentas que se piden

| Pregunta | Cuenta | Resultado |
|---|---|---|
| Milisegundos de un fotograma a 25 fps | 1.000 ÷ 25 | 40 ms |
| Milisegundos de 2 fotogramas a 25 fps | 2 × 40 | 80 ms |
| Milisegundos de 4 fotogramas a 25 fps | 4 × 40 | 160 ms |
| Milisegundos de 2 fotogramas a 50 fps | 2 × (1.000 ÷ 50) | 40 ms |
| Motores para tres cámaras y una cabeza caliente | Uno por punto de vista | 4 |
| Lienzo de una pared de 8 × 3 armarios de 400 × 450 píxeles | 8 × 400 y 3 × 450 | 3.200 × 1.350 píxeles |
| Entradas al mezclador con 7 cámaras, 2 de ellas también con realidad aumentada | 7 directas + 2 aumentadas | 9 |

## Lo que este tema no da, y dónde está

- Qué sistema de grafismo, de plató virtual, de seguimiento de cámara, de pantallas o de videowall tiene
  CSRTV: no consta en documento publicado leído. Los productos citados (Vizrt, Unreal Engine, Chyron,
  Mo-Sys, Datapath, NVIDIA, AMD) son ejemplos.
- La documentación de fabricantes de procesadores y paneles de LED (Brompton y otros): no se ha podido
  leer; lo que el tema dice del procesador de LED sale sólo de la documentación de Epic Games. Tampoco
  una tabla publicada de distancias mínimas de cámara por paso de píxel.
- Videowalls de monitores LCD (marcos entre pantallas, controladoras): sin fuente leída; el tema no da
  cifras de marco.
- Otros sistemas de grafismo y plató virtual (Zero Density, Pixotope, Ross XPression, Ventuz, CasparCG):
  no se ha leído su documentación para este tema. Que «chyron» se use como nombre común del rótulo
  inferior: no se ha leído en fuente y no se afirma.
- La especificación del protocolo FreeD: no se ha consultado; lo que se dice de él sale de la ficha de
  un fabricante que lo usa como formato de salida.
- Las familias de seguimiento, la cuenta de motores, el *foreground*, la compensación de retardos, la
  iluminación del croma, la preparación de las pantallas y del videowall: oficio, sin norma.
- Diseño gráfico para televisión y grafismo de directo frente a postproducción: tema 1. Quién diseña,
  rellena y lanza los rótulos y el grafismo por géneros: tema 3. Infografía y datos: tema 4. Modelado,
  animación 3D, composición, croma en postproducción y tracking en postproducción: tema 5. Flujos con
  realización y continuidad: tema 7. Alfa, relleno y llave en la entrega, zonas seguras, colorimetría y
  HDR: tema 8. Herramientas, plantillas y automatización: tema 9. Colaboración en directo: tema 17.
  Pantallas de visualización de datos del puesto de trabajo (prevención de riesgos): tema 18.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004: 3.10, 6.5.2 y 8.6.1 | Vidiwall y pantallas de plató, vestuario ante el croma | Texto tomado del tema cerrado del puesto de Realizador/a (leído allí el 29-09-2026) |
| Mo-Sys, ficha del StarTracker Max y catálogo «Camera Tracking» (mo-sys.com) | Marcas retrorreflectantes, FreeD, seis ejes con zum y foco, seguimiento *inside-out*, salida a motores como Unreal Engine, croma y pared de LED | Texto tomado del tema cerrado del puesto de Realizador/a (volcados el 02-09-2026; releídos el 29-09-2026) |
| Epic Games, *In-Camera VFX Overview in Unreal Engine* (documentación de Unreal Engine 5.8, dev.epicgames.com) | Paso de píxel, distancia y moiré (texto del tema de Realizador/a); armarios, procesador de LED, paso de píxel y coste, frustum interior y exterior, genlock, color hacia la pared, OCIO, efectos en espacio de pantalla, Composure | 29-09-2026 |
| Epic Games, *In-Camera VFX Best Practices in Unreal Engine* (UE 5.8) | Preparar la escena para el tiempo real: las dos preocupaciones, objetivo de 48-72 fps y su salvedad, niveles de detalle, materiales y llamadas de dibujo, texturas en potencias de dos, luz precalculada frente a trazado de rayos, aprobación de lo optimizado | 29-09-2026 |
| Epic Games, *Recommended Hardware for In-Camera VFX in Unreal Engine* (UE 5.8) | Sincronía de los procesadores de LED, tarjeta de sincronía por nodo, tarjeta SDI para croma en directo | 29-09-2026 |
| Epic Games, *nDisplay Overview for Unreal Engine* (UE 5.8) | Nodo principal y secundarios, reparto de pantallas, sincronía de fotograma, lienzo 2D, tecnologías multipantalla, tolerancia a fallos (*failover*) y salida de un nodo del clúster | 29-09-2026 |
| Epic Games, *Motion Design in Unreal Engine* y *Motion Design Quickstart Guide in Unreal Engine* (UE 5.8) | Qué es Motion Design y su etiqueta «experimental», Rundown y Transition Logic, usos en emisión, visor de alfa y zona segura | 29-09-2026 |
| Epic Games, *Professional Video IO in Unreal Engine* (UE 5.8) | Realidad aumentada en el motor: entrada, tratamiento, sincronía y salida de vídeo | 29-09-2026 |
| Vizrt, *Viz Multiplay User Guide* 3.3, «Introduction» (docs.vizrt.com) | Control de las pantallas del plató, Viz Engine, MOS, Pilot Data Server, videowall con DisplayPort y Datapath Fx4, SDI | 29-09-2026 |
| Vizrt, *Viz Engine Administrator Guide* 5.4, «Video Output», y 5.2 (publicada el 20-III-2024), «Dual Channel Mode» | Salida de videowall a pantalla completa; la llave como propiedad de la salida («Contains Alpha», 5.4); doble canal con relleno y llave; control externo | 29-09-2026 |
| Vizrt, *Introduction to Viz Artist* 5.3 | Modos del programa y licencia | 29-09-2026 |
| Chyron, *PRIME CG™ - 3D Real-Time Graphics* y *About Chyron* (chyron.com); nota de prensa *Chyron Merges Live Web Content and CG Graphics with PRIME 5.3* (12-II-2026) | Qué hace PRIME CG, herramientas, Base Scenes, datos, CAMIO, funciones de la plataforma, HTML Input | 29-09-2026 |

La fecha de trabajo del encargo es el 24-09-2026; las fuentes se leyeron el 29-09-2026, fecha del
sistema.

Oficio, declarado así en el texto: la lectura de los cinco términos del enunciado como una misma
maquinaria; la tabla de técnicas (decorado virtual, realidad aumentada, producción virtual en pared de
LED), la escala de realidades y la regla de la oclusión; las tres piezas del plató virtual y los datos
del seguimiento; las familias de seguimiento; la comparación entre croma y pared de paneles; la lectura
del frustum; lo que hace el grafista en un escenario virtual y que los criterios de optimización de la pared de LED valgan para el croma; la cuenta de motores, el *foreground* y la
compensación de retardos, que se deducen de la definición de fotograma por segundo y de la regla de que
sólo se puede retrasar; la iluminación del plató de croma; los contenidos y problemas de las pantallas
(moiré, retardo, realimentación, parpadeo) y el montaje con banco enlazado y mapeado distinto; lo que
el grafista prepara para cada pantalla y para un videowall; la cuenta del lienzo de la pared; los modos
diferido y en tiempo real, las dos exigencias del tiempo real, las cuatro funciones de un sistema de
grafismo y las reglas de integración; y la aplicación práctica.

