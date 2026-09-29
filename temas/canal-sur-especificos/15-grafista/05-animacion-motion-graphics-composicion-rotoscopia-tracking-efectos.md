# Tema 5 del específico de Grafista · Animación 2D/3D, motion graphics, composición, rotoscopia, tracking y efectos visuales

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Grafista · punto 5 |
| Sirve para | Grafista de Canal Sur (grupo B03): test de teoría específica y de aplicación práctica, y prueba práctica del puesto |
| Fuente | Ninguna norma regula cómo se anima o se compone una imagen. Norma de enseñanza que describe el oficio: Real Decreto 1583/2011, de 4 de noviembre, título de Técnico Superior en Animaciones 3D, Juegos y Entornos Interactivos (módulos 1085, 1086, 1087, 1088 y 0907), y Real Decreto 1680/2011, de 18 de noviembre, título de Técnico Superior en Realización de proyectos audiovisuales y espectáculos (módulo 0907). Documentación de fabricante: Blender Foundation (*Blender 5.2 LTS Manual*), Blackmagic Design (*DaVinci Resolve 21 Reference Manual*) Apple (*Apple ProRes*, white paper) y Adobe (ayuda de Photoshop en español, para los nombres de los modos de fusión). Especificación técnica: W3C, *Portable Network Graphics (PNG) Specification (Third Edition)*. Lo propio de la casa: *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, 2004). Lo demás, oficio declarado como tal |
| Redacción que se estudia | RD 1583/2011 en su redacción vigente a 24-09-2026 (modificado por el RD 500/2024, de 21 de mayo, que no toca los módulos que se citan; corrección de errores de 12-III-2012, que no los toca tampoco); manual de Blender 5.2 LTS y manual de Resolve 21 (julio de 2026) en la versión publicada el día en que se leyeron; white paper de ProRes de abril de 2022; especificación del PNG, 3.ª ed., recomendación del W3C de 24-VI-2025; Libro de estilo, 1.ª ed., marzo de 2004 |
| Extensión | 10.000 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía* (Libro de estilo
o LE); real decreto (RD); resultado de aprendizaje de un módulo de formación profesional (RA), que se
mide por criterios de evaluación identificados con letras; dos y tres dimensiones (2D y 3D;
«2 ½D», como la escribe Blackmagic, es el seguimiento plano con perspectiva); cinemática directa (FK,
*forward kinematics*) e inversa (IK, *inverse kinematics*); los ejes con que se nombra un mapa de
texturas (UV); los tres primarios rojo, verde y azul (RGB) y los tres más el alfa (RGBA); efectos
visuales (VFX, *visual effects*); imágenes generadas por ordenador (CGI, *computer-generated
imagery*, como la escribe Blackmagic); inteligencia artificial (IA); World Wide Web Consortium (W3C), que publica la especificación del PNG. Los
formatos de fichero se nombran por su extensión: PNG (*portable network graphics*), TGA (*Truevision
Advanced Raster Graphics Adapter*), TIF o TIFF (*tagged image file format*), BMP (*bitmap*), JPG o JPEG
(*Joint Photographic Experts Group*), EXR (el formato OpenEXR) y MOV (el contenedor QuickTime de Apple);
TARGA es otro nombre del TGA; ProRes es la familia de códecs de Apple. Megabyte y gigabyte (MB y
GB); alto rango dinámico (HDR, *high dynamic range*). La versión del manual de Blender lleva la
etiqueta LTS (*long-term support*, soporte de larga duración).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.15, punto 5): «Animación 2D/3D, motion
> graphics, composición, rotoscopia, tracking y efectos visuales.»

Qué se puede preguntar: qué es animar y qué es un fotograma clave; qué es la interpolación y qué tipos
hay (constante, lineal, Bézier, suavizados); qué son la curva de animación y el suavizado de entrada y
de salida; qué distingue *stop motion*, pixilación, rotoscopia y animatrónica; las fases de la
animación 2D (animática, layout, animación clave, intercalación, pintura y composición) y de la 3D
(diseño y modelado, *setup*, texturización, iluminación, animación y renderizado); qué métodos de
modelado hay (nurbs, polígonos, superficies de subdivisión); qué son una malla, un
mapa UV, un *rig*, la cinemática directa y la inversa; qué es renderizar y qué es el trazado de rayos;
qué son las partículas, los sólidos rígidos y los blandos; qué es el motion graphics y en qué formato se
entrega una pieza con transparencia; qué es una capa, qué es precomponer; qué familias de incrustación
hay y cuántas señales intervienen en una; qué es el canal alfa y qué valores toma; cuántos bits ocupa un píxel con alfa; qué distingue el
alfa directo del premultiplicado y qué ocurre si se confunden; qué es una máscara; qué hacen los modos de fusión (multiplicar, trama, sobreexposición lineal, superponer,
diferencia); qué es la rotoscopia
y cómo se hace hoy; qué es el tracking y qué tipos hay (de punto, planar, de cámara); qué pasos tiene el
seguimiento de cámara; qué es un efecto visual; qué dice el Libro de estilo de los efectos en la
información. En la prueba práctica: animar la entrada de un rótulo, pegar un elemento a un objeto que se
mueve, recortar una figura, exportar una pieza con alfa y hacer las cuentas de fotogramas.

<!-- indice -->

## Índice

- [De dónde sale este tema](#de-dónde-sale-este-tema)
- [1. Animación 2D y 3D](#1-animación-2d-y-3d)
  - [Qué es animar](#qué-es-animar)
  - [Las técnicas de animación](#las-técnicas-de-animación)
  - [Fotograma clave e interpolación](#fotograma-clave-e-interpolación)
  - [La curva de animación y los tipos de interpolación](#la-curva-de-animación-y-los-tipos-de-interpolación)
  - [El suavizado: entrada y salida](#el-suavizado-entrada-y-salida)
  - [La animación 2D y sus fases](#la-animación-2d-y-sus-fases)
  - [La animación 3D y sus fases](#la-animación-3d-y-sus-fases)
  - [El *rig*: esqueleto y cinemática](#el-rig-esqueleto-y-cinemática)
  - [El render](#el-render)
  - [La cámara virtual](#la-cámara-virtual)
- [2. Motion graphics](#2-motion-graphics)
  - [Qué es](#qué-es)
  - [Con qué se hace](#con-qué-se-hace)
  - [El ritmo y el sonido](#el-ritmo-y-el-sonido)
  - [La entrega: una pieza con transparencia](#la-entrega-una-pieza-con-transparencia)
- [3. Composición](#3-composición)
  - [Qué es componer](#qué-es-componer)
  - [La capa](#la-capa)
  - [La precomposición](#la-precomposición)
  - [Incrustar](#incrustar)
  - [Las tres señales de una incrustación](#las-tres-señales-de-una-incrustación)
  - [El canal alfa](#el-canal-alfa)
  - [Los ficheros gráficos que llevan alfa](#los-ficheros-gráficos-que-llevan-alfa)
  - [Alfa directo y alfa premultiplicado](#alfa-directo-y-alfa-premultiplicado)
  - [La máscara](#la-máscara)
  - [Los modos de fusión](#los-modos-de-fusión)
- [4. Rotoscopia](#4-rotoscopia)
  - [Las dos rotoscopias](#las-dos-rotoscopias)
  - [Cómo se rotoscopia en composición](#cómo-se-rotoscopia-en-composición)
  - [La captura de movimiento](#la-captura-de-movimiento)
- [5. Tracking](#5-tracking)
  - [Qué es](#qué-es-1)
  - [Los tipos de seguimiento](#los-tipos-de-seguimiento)
  - [El seguimiento de cámara](#el-seguimiento-de-cámara)
  - [Estabilizar](#estabilizar)
  - [Por qué falla y cómo se prepara](#por-qué-falla-y-cómo-se-prepara)
- [6. Efectos visuales](#6-efectos-visuales)
  - [Qué son](#qué-son)
  - [Los efectos 3D: partículas, dinámicas y multitudes](#los-efectos-3d-partículas-dinámicas-y-multitudes)
  - [La integración](#la-integración)
  - [Los efectos y la información](#los-efectos-y-la-información)
- [Aplicación práctica](#aplicación-práctica)
  - [Cinco encargos corrientes](#cinco-encargos-corrientes)
  - [Cuentas que se piden](#cuentas-que-se-piden)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## De dónde sale este tema

Ninguna norma dice cómo se anima un rótulo ni cómo se compone una imagen. Lo más parecido a un
canon oficial del oficio son las normas que fijan las enseñanzas de formación profesional: el RD
1583/2011, del título de Técnico Superior en Animaciones 3D, Juegos y Entornos Interactivos, describe
con precisión las fases de la animación 2D y 3D, la rotoscopia, la captura de movimiento, los efectos
3D y la composición por capas; el RD 1680/2011, del título de Realización, comparte con él el módulo de
montaje y postproducción. Son normas de enseñanza: dicen qué aprende quien se forma para el oficio, no
cómo trabaja la RTVA. El tema las cita porque dan nombre oficial a cada operación.

Para las definiciones técnicas el tema acude a la documentación de dos programas: Blender, programa
libre de 3D y animación, y DaVinci Resolve con su compositor Fusion, de Blackmagic Design. Son manuales
de fabricante y se citan como tales, en inglés y con la traducción o la lectura en redonda; valen
como definición técnica, no como norma, y no significan que Canal Sur use esos programas: el temario no
nombra programa alguno. Lo que no está en ninguna de esas fuentes va como oficio y se dice.

De la casa, sólo el Libro de estilo de 2004 dice algo de la materia, y lo dice de los efectos en la
información. Canal Sur no ha publicado un manual de grafismo animado ni de postproducción.

El tema sigue el orden del enunciado: animación 2D y 3D, motion graphics, composición, rotoscopia,
tracking y efectos visuales.

## 1. Animación 2D y 3D

### Qué es animar

Blender da la definición más llana: **«Animation is making an object move or change shape over
time.»** (animar es hacer que un objeto se mueva o cambie de forma a lo largo del tiempo). Distingue
tres maneras de conseguirlo: **«Moving as a whole object»** (mover el objeto entero: posición,
rotación, escala), **«Deforming them»** (deformarlo) e **«Inherited animation»** (el movimiento
heredado de otro objeto al que está enlazado, su padre). Y añade: **«Animation is typically achieved
with the use of keyframes.»** (lo corriente es animar con fotogramas clave).

La ilusión de movimiento descansa en una propiedad de la vista que el RD 1583/2011 pone la primera en
los contenidos del módulo 1087 «Animación de elementos 2D y 3D»: **«La persistencia retiniana.»**
Sobre ella, el animador reparte el movimiento en imágenes sucesivas; el mismo módulo llama a ese
reparto **«Asignación y reparto de tiempos. Temporalización (timing) y fragmentación del movimiento.»**
Cuántas imágenes hacen falta depende de la cadencia de la salida: la televisión europea trabaja a 25
imágenes por segundo (oficio; la cadencia de cada formato es el tema 8).

### Las técnicas de animación

Las técnicas que conviene distinguir:

| Técnica | En qué consiste | Ejemplo |
|---|---|---|
| *Stop motion* | Fotografiar un objeto real, moverlo un poco y volver a fotografiar | Las películas de plastilina |
| Pixilación | Lo mismo, pero con PERSONAS como objeto | Cuerpos que se mueven a saltos |
| Rotoscopia | Dibujar encima de imagen real, fotograma a fotograma | La animación que calca movimiento humano filmado |
| Animatrónica | Muñecos con mecanismos que se mueven de verdad ante la cámara | No es animación fotograma a fotograma |

El buen distractor es la pixilación, porque es un caso particular de la primera: la diferencia es sólo
qué se fotografía.

La norma de enseñanza las recoge así. El primer resultado de aprendizaje del módulo 1087 es
**«Realiza la animación y captura en stop motion o pixilación»**, y sus contenidos incluyen **«La
pixilación.»** y la sincronía de los labios con la voz (**«sincronización, lipsync»**). La rotoscopia
tiene su propio resultado (RA 7), que se ve en el epígrafe 4.

A esas técnicas «de fotograma» se suman las que hoy hace el ordenador, que son las del resto del
epígrafe: la animación 2D por fotogramas dibujados o por fotogramas clave, y la animación 3D de
modelos.

### Fotograma clave e interpolación

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

El glosario de Blender define el fotograma clave con su historia: **«A frame in an animated sequence
drawn or otherwise constructed directly by the animator. In classical animation, when all frames were
drawn by animators, the senior artist would draw these frames, leaving the “in between” frames to an
apprentice. Now, the animator creates only the first and last frames of a simple sequence (keyframes);
the computer fills in the gap.»** Es decir: en la animación clásica el dibujante principal hacía las
claves y un ayudante los dibujos intermedios; hoy el animador fija las claves y el ordenador rellena el
hueco. Y la interpolación: **«The process of calculating new data between points of known value, like
Keyframes.»** (el cálculo de datos nuevos entre puntos de valor conocido, como los fotogramas clave).

### La curva de animación y los tipos de interpolación

En un programa de animación, la interpolación se ve y se corrige como una curva. Blender lo explica
así: **«Keyframe interpolation is represented and controlled by animation curves, also known as
F-Curves.»**; **«The X axis of the curve corresponds to time, while Y represents the value of the
property.»** (el eje horizontal es el tiempo y el vertical el valor del parámetro: posición, escala,
opacidad). La pendiente de la curva es, por tanto, la velocidad: una curva empinada es un cambio
rápido; una plana, quieto.

Los tipos de interpolación: **«There are a number of modes with fixed shapes, e.g. Constant, Linear,
Quadratic etc, and a free form Bézier mode.»** Los tres que hay que saber distinguir:

| Tipo | Qué hace, según Blender | Para qué |
|---|---|---|
| Constante | **«The curve holds the value until the next keyframe, producing a stair step effect with very abrupt changes.»** | Saltos: un valor que cambia de golpe. Blender añade: **«Normally only used during the initial “blocking” stage in pose-to-pose animation workflows.»** (se usa en el primer encaje de poses) |
| Lineal | **«The curve goes from one keyframe to the next in a straight line, which prevents abrupt changes in value but not in speed.»** | Movimiento a velocidad constante, con arranque y parada secos |
| Bézier | **«The default interpolation, which is smooth in both values and speed.»** | Movimiento suave en valor y en velocidad; se ajusta con las asas de la curva |

Lo que pasa antes de la primera clave y después de la última es la extrapolación: **«Extrapolation
specifies how the curve extends before the first, and after the last keyframe.»**, con dos opciones
principales, constante (el valor se queda quieto) y lineal (sigue en la misma dirección); Blender añade
que la curva también se puede configurar para que se repita en bucle.

### El suavizado: entrada y salida

Los suavizados (*easing*) son interpolaciones pensadas para acelerar o frenar. Blender define las tres
formas:

- **«Ease In: The value accelerates, moving slowly at the beginning of the curve segment and speeding
  up towards the end.»** (arranca despacio y acelera).
- **«Ease Out: The value decelerates, moving quickly at the beginning of the curve segment and slowing
  down towards the end.»** (sale deprisa y frena).
- **«Ease In Out: The value moves slowly in the beginning, speeds up towards the middle, and slows down
  again towards the end.»** (arranca despacio, acelera y frena al llegar).

Y efectos dinámicos, como el rebote (*Bounce*): **«Makes the value bounce a few times with exponential
decay, like a tennis ball that was dropped on the floor.»** (el valor rebota unas cuantas veces cada
vez menos, como una pelota de tenis que cae al suelo).

Cuidado con los nombres: *in* y *out* se refieren al tramo de la curva, y cada programa los rotula a
su modo; lo que no cambia es la idea. Un rótulo que entra y se detiene en su sitio pide frenar al
final; uno que sale de cuadro pide arrancar despacio y acelerar; el que entra y sale en un solo
movimiento, las dos cosas (oficio).

### La animación 2D y sus fases

La animación 2D es la que se hace sobre el plano: dibujos, recortes, formas y textos que se mueven en
dos dimensiones. El RD 1583/2011 fija sus fases como competencia del título (art. 5.c): **«Producir el
proyecto de animación 2D en sus fases de animática, layout, animación clave, intercalación, pintura y
composición, realizando los chequeos y pruebas de línea necesarias hasta la obtención de las imágenes
definitivas que lo conforman.»**

| Fase | Qué es (lectura de la norma y oficio) |
|---|---|
| Animática | El guion gráfico (*storyboard*) montado con sus tiempos y, si lo hay, el sonido: la pieza en borrador |
| Layout | La preparación de cada plano: encuadre, fondos, personajes y elementos, y su colocación |
| Animación clave | Las poses principales de cada movimiento |
| Intercalación | Los dibujos intermedios entre las claves |
| Pintura | El color de cada dibujo |
| Composición | La reunión de todas las capas en la imagen final |

La norma describe también el método. La carta de animación es la tabla de tiempos de cada plano: el
RA 3 del módulo 1087 pide que **«Se han temporizado los movimientos de todos los elementos que se van
a animar, indicando el número de fotogramas necesario para cada variación y generando una carta de
animación por cada plano, personaje y/o decorado.»** (3.a); las claves se dibujan por capas:
**«Se han dibujando los fotogramas clave y se han fragmentado decorados, personajes y elementos de
atrezo en las diferentes capas que hay que animar»** (3.b; «dibujando» es errata del original); y los
intermedios siguen la carta: **«Se han dibujado las intercalaciones, adaptándose a los tiempos marcados
y a los dibujos anteriores y posteriores según la carta de animación.»** (3.c). Los contenidos del
módulo nombran **«La animación en fotogramas completos.»** y **«La intercalación.»**

La intercalación es lo que el ordenador hace hoy con la interpolación: en la animación 2D por
ordenador el grafista pone las claves y el programa calcula los intermedios. El grafismo de televisión
—rótulos, cortinillas, cabeceras— es casi siempre de este tipo (oficio).

### La animación 3D y sus fases

La animación 3D mueve modelos construidos en un espacio de tres dimensiones y fotografiados por una
cámara virtual. El RD 1583/2011 fija sus fases (art. 5.d): **«Producir el proyecto de animación 3D en
sus fases de diseño y modelado, setup, texturización, iluminación, animación y renderizado,
realizando los chequeos necesarios hasta la obtención de las imágenes definitivas que lo
conforman.»**

| Fase | Qué es |
|---|---|
| Diseño y modelado | Construir la forma del objeto. En Blender, el objeto corriente es la malla: **«Type of object consisting of Vertices, Edges and Faces.»** (vértices, aristas y caras). El método de modelado se elige según el modelo (módulo 1086, RA 5.c, abajo) |
| *Setup* (*rigging*) | Dotar al modelo de controles para animarlo: esqueleto, articulaciones, deformadores (epígrafe siguiente) |
| Texturización | Dar al modelo su superficie: color, material, relieve. Se apoya en el mapa UV, que Blender define como **«Defines a relation between the surface of a mesh and a 2D texture.»** (la relación entre la superficie de la malla y una textura plana) |
| Iluminación | Colocar las luces virtuales de la escena |
| Animación | Mover modelos y cámara con fotogramas clave y curvas |
| Renderizado | Calcular las imágenes finales (más abajo) |

La norma da detalle de la texturización en el módulo 1088 «Color, iluminación y acabados 2D y 3D»: el
primer resultado es **«Genera los mapas UV de los modelos»**, que se hacen **«usando los mapas planos,
cilíndricos, esféricos, automáticos o basados en cámara, que se adecuen mejor a su morfología.»**
(1.b); y los materiales se ajustan en su **«especularidad, refracción y reflexión»** (2.c). Distingue
las texturas pintadas (*bitmaps*) de las calculadas: **«texturas procedurales 2D y 3D»** (RA 3).

El modelado lo trata el módulo 1086 «Diseño, dibujo y modelado para animación», cuyo RA 5 es
**«Modela en 3D personajes, escenarios, atrezo y ropa, analizando las características del empleo de
diferentes tipos de software.»** Sus criterios nombran los tres métodos: **«Se ha elegido el método de
modelado (nurbs, polígonos, subdivision surfaces) atendiendo a las características del modelo que hay
que realizar.»** (5.c). El glosario de Blender define los dos que no son la malla de polígonos: NURBS
(*non-uniform rational basis spline*, como lo desarrolla Blender), **«A computer graphics technique for
generating and representing curves and surfaces.»** (curvas y superficies definidas matemáticamente), y
la superficie de subdivisión, **«A method of creating smooth higher poly surfaces which can take a low
polygon mesh as input.»** (parte de una malla de pocos polígonos y la convierte en una superficie suave
de más polígonos). Antes de modelar se fijan **«los tamaños finales, los métodos de modelado, la escala
final y las características de movimiento de cada objeto»** (5.a).

### El *rig*: esqueleto y cinemática

Blender define el *rigging* por su función: **«Rigging is a general term used for adding controls to
objects, typically for the purpose of animation.»**, y añade que el *rig* es la interfaz del animador:
**«Rigs effectively define a user interface for the animator to use, without being concerned with the
underlying mechanisms»** (el animador mueve controles sin ocuparse de lo que hay debajo).

El RD 1583/2011 describe los pasos en el RA 2 del módulo 1087 (*character setup* de personajes 3D):

- El esqueleto: **«Se ha construido un esqueleto dentro de cada modelo que se va a animar mediante
  una jerarquía de ensamblajes (joints)»** (2.b).
- La cinemática: **«Se ha realizado la asignación de cinemáticas a diferentes partes del esqueleto,
  diferenciando directas (FK) e inversas (IK) para poder controlar varias articulaciones al mismo
  tiempo, influyendo unas en otras.»** (2.c).
- La unión de la malla al esqueleto: **«Se ha emparentado la geometría con el esqueleto (bind
  skin)»** (2.d), y el reparto de su influencia: **«Se han pintado los pesos o influencias de los
  ensamblajes sobre los puntos de la geometría»** (2.e).

La diferencia entre las dos cinemáticas, con las definiciones de Blender:

| | Cinemática directa (FK) | Cinemática inversa (IK) |
|---|---|---|
| Qué es | **«The process of determining the movement of interconnected segments or bones of a body or model in the order from the parent bones to the child bones.»** | **«The process of determining the movement of interconnected segments or bones of a body or model in the order from the child bones to the parent bones.»** |
| Orden | Del padre al hijo | Del hijo al padre |
| Ejemplo de Blender | **«you can move the upper arm then the lower arm and hand go along with the movement.»** | **«you can move the hand then the upper and lower arm will automatically follow that movement.»** |

La regla para no confundirlas: en la directa se mueve el hombro y la mano va detrás; en la inversa se
coloca la mano y el brazo se acomoda solo. Para que un personaje apoye la mano en una mesa, inversa;
para un brazo que describe un arco, directa (oficio).

La misma idea de jerarquía sirve en 2D: enlazar un elemento a otro que actúa de padre, a veces
invisible, para moverlos juntos. Es la «animación heredada» de Blender (**«Inherited animation»**).

### El render

Renderizar es calcular la imagen. Blender: **«The process of computationally generating a 2D image
from 3D geometry.»** (generar por cálculo una imagen plana a partir de geometría 3D). Uno de los
métodos es el trazado de rayos: **«Rendering technique that works by tracing the path taken by a ray of
light through the scene, and calculating reflection, refraction, or absorption of the ray whenever it
intersects an object in the world. More accurate than Scanline, but much slower.»** (sigue el camino
de cada rayo de luz y calcula reflexión, refracción o absorción cada vez que toca un objeto; más
exacto que el método por líneas de barrido, pero mucho más lento).

En la norma de enseñanza, el render de una pieza 3D se organiza por capas. El módulo 1085 «Proyectos de
animación audiovisual 2D y 3D» tiene dos resultados sobre ello: **«Realiza la separación de capas y
organiza los efectos de render»** (RA 3) y **«Realiza el render final por capas»** (RA 4). Pide
valorar **«la disponibilidad, capacidad y velocidad de las estaciones de trabajo y granja de render»**
(4.a) —la granja de render es el conjunto de ordenadores que calcula en paralelo— y comprobar
**«el cumplimiento de los requisitos del render (integridad del fotograma, orden y posición de los
elementos de las capa y flicker, entre otros) fotograma a fotograma y capa a capa.»** (4.c; el
parpadeo, *flicker*, es uno de los defectos que se revisan). Separar en capas —personaje, fondo,
sombras, reflejos— permite corregir una sin volver a calcular las demás, que es la misma lógica de la
composición del epígrafe 3.

Un efecto que se calcula en el render es el desenfoque de movimiento: **«Simulating motion blur makes
computer animation appear more realistic.»** (simularlo hace más realista la animación por ordenador).
Blender explica el fenómeno por la vista: un objeto que se mueve deprisa **«appears to be blurred
because of our persistence of vision»** (se ve borroso por la persistencia de la visión). Una cámara
virtual no lo produce si no se le pide (oficio).

### La cámara virtual

En animación también hay cámara, y se anima como un objeto más. El RA 6 del módulo 1087 pide que
**«Se han marcado las trayectorias de los movimientos de cámara temporizando los mismos (arranques,
frenadas, aceleraciones y deceleraciones) mediante la colocación de fotogramas clave (key frames)»**
(6.d). Los arranques y frenadas son, otra vez, el suavizado de las curvas; las focales y la
profundidad de campo virtuales se eligen en cada plano (6.a, 6.b y 6.f).

## 2. Motion graphics

### Qué es

Ni la norma de enseñanza ni los manuales leídos definen *motion graphics*. El término se usa en la
documentación técnica como nombre de una tarea: Blackmagic presenta su programa diciendo que
**«DaVinci Resolve integrates editing, compositing and motion graphics, color correction, audio
recording and mixing, and finishing within a single, easy to learn application.»** (reúne montaje,
composición, motion graphics, color, sonido y acabado), y Apple dice de ProRes 4444 que es **«a
high-quality solution for storing and exchanging motion graphics and composites»** (para guardar e
intercambiar motion graphics y composiciones).

En el oficio, motion graphics es el grafismo animado: texto, formas, logotipos, iconos, datos y
fotografías que se mueven, sin personajes ni narración dramática, y casi siempre en 2D o en un 3D
sencillo (oficio). En televisión son las cabeceras, las cortinillas, los rótulos que entran y salen,
las promociones, los mapas y gráficos animados de los informativos (temas 3 y 4). Se distingue de la
animación de personajes en que el movimiento no representa un cuerpo, sino que ordena la información
y la marca de la cadena.

### Con qué se hace

El motion graphics usa las herramientas de los epígrafes 1 y 3: capas, fotogramas clave, curvas de
animación y composición. Tres cosas le son propias:

- La animación de las propiedades de cada capa. Cada capa lleva sus propias propiedades —posición,
  escala, rotación, opacidad— que se pueden animar por separado. Ésa es la razón de ser del modelo:
  poder tocar una cosa sin tocar las demás.
- La jerarquía. Se enlazan capas a otra que hace de padre para moverlas juntas (la «animación
  heredada» del epígrafe 1), y se agrupan en una composición anidada (precomposición, epígrafe 3).
- La automatización. Los parámetros se pueden relacionar entre sí con expresiones. De las más
  sencillas, las *Simple Expressions*, Blackmagic dice que son **«a special type of script that can be placed alongside the parameter it is
  controlling. These are useful for setting simple calculations, building unidirectional parameter
  connections, or a combination of both.»** (un pequeño guion junto al parámetro, para cálculos
  sencillos o para que un parámetro siga a otro). Y las piezas repetidas se convierten en plantillas:
  en Resolve, los generadores de texto **«are Fusion templates, which are Fusion compositions that
  have been turned into macros»** (composiciones convertidas en macros que se usan desde el montaje
  como cualquier generador). Las plantillas y la automatización gráfica son el tema 9.

### El ritmo y el sonido

Una pieza de motion graphics se monta sobre música o sobre un golpe de sonido, y ahí se juzga. El
audio en una pieza de grafismo, con los cuatro conceptos que un diseñador necesita:

| Concepto | Qué es |
|---|---|
| Sincronía | Que el golpe de sonido caiga en el fotograma del golpe visual |
| Nivel | Que la pieza salga al mismo volumen que el resto de la emisión |
| Sonido de marca | El logotipo sonoro que acompaña al visual |
| Silencio | Que una pieza sin audio se entregue con pista muda, no sin pista |

El aviso que resume el epígrafe: una cabecera se juzga con sonido. Montada muda parece bien y con
música puede quedar medio fotograma corta, y medio fotograma se nota.

### La entrega: una pieza con transparencia

Casi todo el motion graphics de televisión va encima de otra imagen —un rótulo sobre un plano, una
mosca sobre el programa—, así que se entrega con su transparencia. Hay dos maneras: un fichero que
lleve el canal alfa dentro (epígrafe 3), o dos señales o ficheros, el relleno y el recorte (*fill* y
*key*).

En vídeo, Apple fija qué códecs de su familia sirven: **«Apple ProRes 4444 XQ and Apple ProRes 4444
are ideal for the exchange of motion graphics media because they are virtually lossless, and are the
only ProRes codecs that support alpha channels.»** (son los únicos ProRes que admiten alfa); ProRes
4444 guarda **«a mathematically lossless alpha channel up to 16 bits.»** (un alfa sin pérdidas de hasta
16 bits). Ningún ProRes 422 lleva alfa. En imagen fija o en secuencia de fotogramas, PNG, TGA o TIFF
(tabla del epígrafe 3). El JPG nunca. Los formatos de entrega a emisión, las zonas de seguridad y la
salida de relleno y llave de un motor de grafismo son el tema 8.

## 3. Composición

### Qué es componer

Componer es reunir en una sola imagen varias imágenes o elementos superpuestos: un plano, un rótulo,
un fondo virtual, un elemento 3D, una sombra. La norma de enseñanza lo llama composición multicapa y
lo pone en los contenidos del módulo 0907 «Realización del montaje y postproducción de audiovisuales»,
común a los títulos de Animaciones 3D (RD 1583/2011) y de Realización (RD 1680/2011): **«Técnicas y
procedimientos de composición multicapa: • Organización del proyecto y flujo de trabajo. • Gestión de
capas. • Creación de máscaras. • Animación. Interpolación. Trayectorias.»**, seguidas de los
procedimientos de efectos, entre ellos **«Efectos de key. Superposición e incrustación.»**

Y enumera lo que una composición combina: **«Se ha realizado una composición multicapa, combinando
ajustes de corrección de color, efectos de movimiento o variación de velocidad de la imagen (congelado,
ralentizado y acelerado), ocultación/difuminado de rostros, aplicación de keys y efectos de
seguimiento y estabilización, entre otros.»** (módulo 0907, RA 3.b); y el tipo de recorte: **«Se han
determinado y generado las keys necesarias para la realización de un efecto y se ha seleccionado el
tipo (luminancia, crominancia, matte y por diferencia) y el procesado más adecuado para cada caso.»**
(RA 3.c).

Hay dos maneras de organizar una composición en un programa (oficio): por capas apiladas, en las que
lo de arriba tapa lo de abajo, y por nodos, en las que cada operación es una caja y las imágenes
circulan de una a otra por conexiones; Fusion, el compositor de Resolve, trabaja por nodos. El
resultado es el mismo; cambia cómo se ve y se ordena el trabajo.

### La capa

Una capa es cada una de las subdivisiones en las que organizamos el diseño de un grafismo. Qué hace una
capa, en tres líneas, para que la definición signifique algo: cada elemento del grafismo vive en su
propia capa; el orden de apilamiento decide qué tapa a qué; y cada capa lleva sus propias propiedades
—posición, escala, rotación, opacidad— que se pueden animar por separado.

La capa no es el fotograma: la imagen impresa en el celuloide es el fotograma, y el término inglés que
se refiere a él es *frame*.

### La precomposición

Precomponer coge las capas seleccionadas y las mete dentro de una composición nueva, que pasa a
ocupar en la composición original el sitio de todas ellas. A partir de ahí, la composición anidada se
comporta como una capa: se le aplican efectos, se transforma y se anima de una vez.

Para qué sirve en el trabajo: para aplicar un efecto al conjunto y no a cada pieza, y para ordenar
una composición que ha crecido. Es el equivalente de agrupar en un programa de dibujo, con la
diferencia de que la precomposición se puede abrir y editar por dentro.

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
necesita resolución de color, así que un material con submuestreo cromático fuerte (tema 8) da bordes
peores que uno 4:2:2 o 4:4:4.

La distinción entre las dos incrustaciones por clave:

| | Por color | Por luminancia |
|---|---|---|
| Qué elimina | Un color concreto y sus vecinos | Todo lo más claro o lo más oscuro de un umbral |
| Cuándo se usa | Plató con fondo verde o azul | Rótulos blancos sobre negro, humo, fuego |
| Qué la estropea | Que el sujeto vista de ese color, o que el fondo esté mal iluminado | Que el sujeto tenga el mismo brillo que el fondo |

Y una regla para las preguntas de intruso: el cambio de velocidad de una capa (*time remapping*) no es
una técnica de transparencia. De estos cuatro nombres —croma, luma, alfa y *time remapping*—, los tres
primeros se refieren a QUÉ se ve y el cuarto a CUÁNDO se ve.

### Las tres señales de una incrustación

En una composición creada por efecto de incrustación intervienen tres señales.

| Señal | Qué es |
|---|---|
| Fondo (*background*) | La imagen que queda debajo: lo que se ve por el agujero |
| Relleno (*fill*) | La imagen que se pone encima: lo que se ve dentro de la forma |
| Recorte (*key*) | La señal que define la forma del agujero: dónde se ve una y dónde la otra |

Por qué son tres y no dos: con dos imágenes no hay composición posible, porque falta decir dónde
acaba una y empieza la otra. El recorte es una señal por derecho propio, y en un mezclador de vídeo
viaja por una entrada distinta de la del relleno: por eso los mezcladores tienen entradas rotuladas
*key* y *fill* por separado.

Y por qué no son cuatro: el canal alfa no es una cuarta señal, es la forma de llevar el recorte
pegado al relleno cuando los dos vienen del mismo fichero. Cuando hay alfa hay tres señales igual:
fondo, relleno y recorte, sólo que dos de ellas comparten fichero.

### El canal alfa

El canal alfa es el cuarto canal de una imagen, y dice cuánto de opaco es cada píxel. Los tres
primeros son rojo, verde y azul; el cuarto no lleva color: lleva transparencia.

| Valor del alfa | Qué significa |
|---|---|
| 0 | Píxel totalmente transparente: se ve el fondo |
| Valores intermedios | Píxel semitransparente: se mezclan fondo y relleno |
| Máximo | Píxel totalmente opaco: se ve el relleno |

Los valores intermedios son la razón de ser del alfa. Sin ellos, los bordes de un recorte serían
escalones; con ellos, un borde puede estar medio dentro y medio fuera, que es como se ve un recorte
bueno. De aquí sale la notación 4:4:4:4 del tema 8: la cuarta cifra es el alfa.

### Los ficheros gráficos que llevan alfa

El canal alfa es la máscara de transparencia que un fichero gráfico puede llevar dentro, y es la
señal de recorte guardada en el propio archivo.

| Formato | ¿Lleva canal alfa? | Bits por píxel con alfa |
|---|---|---|
| JPG | Nunca | — |
| PNG | Sí | 32 (8 por canal, cuatro canales) |
| TIF | Sí | 32 o más |
| TGA | Sí | 32 |

El fichero gráfico que nunca tiene canal alfa es el JPG. La razón está en el diseño del formato: el
JPG se creó para fotografías, con compresión con pérdidas y tres canales de color y ninguno más. No
hay sitio donde guardar la transparencia.

Un archivo gráfico TGA con canal alfa tiene 32 bits:

8 bits de rojo + 8 de verde + 8 de azul + 8 de alfa = 32 bits

Los 24 bits son el mismo fichero sin alfa —tres canales de ocho—: la diferencia entre 24 y 32 es
precisamente el canal alfa.

Los 32 bits del PNG de la tabla son el caso de 8 bits por canal, no el único. La especificación del
PNG (W3C, 3.ª edición, 2025) cuenta la profundidad por muestra: **«Bit depth is a single-byte integer
giving the number of bits per sample or per palette index (not per pixel).»** Y para el PNG con alfa en
color (*truecolor with alpha*, tipo de color 6) admite dos profundidades, **«8, 16»**, con esta
estructura: **«Each pixel is an R,G,B triple followed by an alpha sample.»** (cada píxel, los tres de
color seguidos del alfa). Así, un PNG con alfa ocupa 32 bits por píxel a 8 bits por canal o 64 bits por
píxel a 16 bits por canal:

16 bits × 4 canales (rojo, verde, azul y alfa) = 64 bits

En vídeo, el alfa lo llevan ProRes 4444 y 4444 XQ, normalmente en contenedor MOV (epígrafe 2). El aviso de oficio:
un grafismo entregado en un formato sin alfa llega al control con un fondo negro pegado.

### Alfa directo y alfa premultiplicado

Un fichero con alfa puede guardar el color de dos maneras, y confundirlas estropea los bordes de la
composición. Blackmagic tiene la premultiplicación por **«arguably one of the most confusing areas of visual effects
compositing»** y las define así (cap. 77, p. 1726):

| | Directo (*straight*, *unpremultiplied*) | Premultiplicado (*premultiplied*) |
|---|---|---|
| Definición | **«An RGB image unaltered by the semi-transparency information in a fourth channel (alpha channel)»** (el color no está afectado por el alfa) | **«An RGB image that has each channel multiplied by its alpha channel before compositing.»** (cada canal de color ya viene multiplicado por el alfa) |
| Quién lo produce, según Blender | **«This is the alpha type used by paint programs such as Photoshop or Gimp, and used in common file formats like PNG, BMP or TARGA.»** (programas de pintura y formatos corrientes: PNG, BMP, TGA) | **«This is the natural output of render engines»**; **«The OpenEXR file format uses this alpha type.»** (la salida natural de los motores de render; el EXR) |

En el premultiplicado, **«The alpha channel itself is not multiplied. The R, G, and B channels are
multiplied by the alpha.»** (el alfa no se toca; se multiplican los tres de color). Y Blackmagic
advierte que **«Most computer-generated images are premultiplied for convenience»** (p. 1727).

Las cuatro reglas del manual de Resolve (p. 1728): **«Always use premultiplied images with a Merge
node. / Only color-correct images that are not premultiplied. / Always filter and transform images
that are premultiplied. / Never double premultiply an image.»** Es decir: se compone y se transforma
(escala, desenfoque) en premultiplicado; se corrige el color en directo, porque **«color correction is
best performed on a non-premultiplied (straight) RGBA image»**; y nunca se premultiplica dos veces.

El fallo que produce la confusión: **«if the image is not premultiplied, the pixels that should be
transparent are still added, which typically results in an unwanted bright fringe around the edges of
your foreground subject.»** (si la imagen no está premultiplicada y se trata como si lo estuviera, los
píxeles que debían ser transparentes se suman y aparece un halo claro alrededor del sujeto). El error
inverso, tratar como directa una imagen premultiplicada, oscurece los bordes (oficio). Por eso al
exportar y al importar un grafismo con alfa se declara de qué tipo es. Y no se convierte de uno a otro
sin necesidad: **«Conversion between the two alpha types is not a simple operation and can involve
data loss»** (Blender).

### La máscara

La función principal de una máscara de capa es ocultar o mostrar partes específicas de una capa sin
eliminar permanentemente el contenido.

Cómo funciona: la máscara es una imagen en escala de grises pegada a la capa. Donde la máscara es
blanca, la capa se ve; donde es negra, no; donde es gris, se ve a medias. Es exactamente un canal alfa
dibujado a mano.

Blender lo dice en su glosario: **«A grayscale image used to include or exclude parts of an image. A
matte is applied as an Alpha Channel, or it is used as a mix factor when applying Color Blend
Modes.»** (una imagen en grises que incluye o excluye partes de una imagen; se aplica como canal alfa
o como factor de mezcla de los modos de fusión). Máscara y mate (*matte*) nombran lo mismo. En un
compositor de nodos, la máscara es una imagen de un solo canal: **«Mask nodes create an image that is
used to define transparency in another image. Unlike other image creation nodes in Fusion, mask nodes
create a single channel image rather than a full RGBA image.»** (Blackmagic).

El aviso de oficio: la máscara de capa es la razón por la que un fichero de grafismo se puede retocar
meses después. Quien recorte borrando píxeles entrega un trabajo que no se puede corregir, y en una
casa de televisión los rótulos se corrigen siempre.

### Los modos de fusión

El modo de fusión decide con qué cuenta se mezcla una capa con lo que tiene debajo. En el nodo Merge de
Fusion es el *Apply Mode*: **«The Apply Mode setting determines the math used when blending or combining
the foreground and background pixels.»** (la operación con que se mezclan los píxeles del primer plano
y del fondo). Los que más se usan, con la definición del manual de Resolve (cap. 94, pp. 2266-2267); el
nombre en castellano es el de la ayuda de Photoshop en español (Adobe):

| Modo | Qué hace |
|---|---|
| *Normal* (normal) | **«The default Normal merge mode uses the foreground’s Alpha channel as a mask to determine which pixels are transparent and which are not.»** (el alfa del primer plano decide qué tapa) |
| *Multiply* (multiplicar) | **«Multiplies the values of a color channel. This will give the appearance of darkening the image as the values are scaled from 0 to 1. White has a value of 1, so the result would be the same.»** (oscurece; el blanco no cambia nada) |
| *Screen* (trama) | **«The resulting color is always lighter. Screening with black leaves the color unchanged, whereas screening with white will always produce white.»** (aclara; el negro no cambia nada) |
| *Linear Dodge (Add)* (sobreexposición lineal o añadir) | **«This blending mode looks at the color information in each channel and brightens the base color to reflect the blend color by increasing the brightness. Blending with black produces no change.»** (aclara más que la trama) |
| *Overlay* (superponer) | **«Overlay multiplies or screens the color values of the foreground image, depending on the color values of the background image.»** (multiplica o trama según el fondo; conserva sus luces y sombras) |
| *Difference* (diferencia) | **«Merging with white inverts the color. Merging with black produces no change.»** (resta un color del otro) |
| *Darken* / *Lighten* (oscurecer / aclarar) | Se queda, canal a canal, con el valor más oscuro o más claro de los dos |

Uso de oficio: multiplicar para sombras y texturas oscuras sobre el fondo; trama y sobreexposición lineal para brillos,
destellos y fuego grabados sobre negro, que así se integran sin recortarlos.

## 4. Rotoscopia

### Las dos rotoscopias

La palabra se usa en dos sentidos, y los dos están en las fuentes.

El primero es una técnica de animación: dibujar encima de imagen real, fotograma a fotograma, para
que el dibujo tenga el movimiento del original. El RD 1583/2011 la describe en el RA 7 del módulo
1087, **«Realiza la captura de movimiento y rotoscopia en 2D y 3D»**, cuyo último criterio es el
dibujo sobre la referencia: **«Se han dibujado, física o virtualmente, sobre las imágenes de
referencia, los personajes y elementos que se van a animar, respetando las hojas de modelo.»** (7.i;
las hojas de modelo son los dibujos que fijan cómo es cada personaje). Sus contenidos recorren el
proceso, de la preparación de la imagen al dibujo: **«La rotoscopia: • Obtención, escalado y archivado
de las imágenes originales.»**, las cámaras y el escáner, **«Elaboración de capas para rotoscopia en
acetatos según los parámetros técnicos de la fotografía de animación.»** y **«Elaboración de
superposiciones y rotoscopias: en superficies planas y por ordenador.»**

El segundo es una operación de composición, y es el que más usa un grafista: recortar a mano un
objeto o una persona de un plano con una máscara que se ajusta fotograma a fotograma, para separarlo
del fondo cuando no hay croma. Blender lo dice de sus máscaras: **«They can be used for manual
rotoscoping to pull a particular object out of the footage, or as a rough matte for green-screen
keying.»** (sirven para rotoscopiar a mano, sacando un objeto del plano, o como mate aproximado de
un croma).

Las dos comparten el principio: la imagen real manda y el trabajo se hace encima de ella, fotograma a
fotograma.

### Cómo se rotoscopia en composición

La herramienta es la máscara vectorial: una forma cerrada de curvas Bézier que se anima con fotogramas
clave. Blackmagic: **«Polygon masks are user-created Bézier shapes. This is the most common type of
polyline and the basic workhorse of rotoscoping.»** (la máscara de polígono, una forma Bézier dibujada
por el usuario, es la herramienta básica de la rotoscopia).

La máscara sigue al objeto de dos maneras: animándola a mano o enlazándola al seguimiento. Blender:
**«Masks can be animated over the time so that they follow some object from the footage, e.g. a
running actor. This can be achieved with shape keys or parenting the mask to tracking markers.»** (la
máscara se anima para que siga, por ejemplo, a un actor que corre; con formas clave o enlazándola a los
marcadores de seguimiento). Es el enlace entre este epígrafe y el siguiente: el tracking mueve la
máscara en bloque, y el rotoscopista sólo corrige la forma donde cambia.

Hoy existe también la rotoscopia asistida por IA. Resolve tiene una herramienta, Magic Mask, que
**«uses the DaVinci Neural Engine, guided by the user via a click-based interface, to automatically
create detailed masks with which to isolate objects or humans, either whole or in part»** (usa el
motor neuronal de Resolve, guiado por clics del usuario, para crear automáticamente máscaras que aíslan
objetos o personas, enteros o en parte). Asistida no quiere decir revisada: el resultado se comprueba
fotograma a fotograma, sobre todo en el pelo, las manos y los bordes con desenfoque de movimiento
(oficio). Las garantías de uso de la IA en el trabajo del grafista son el tema 15.

Tres reglas de oficio de la rotoscopia: se usan varias máscaras sencillas en lugar de una complicada
(una para el cuerpo, otra para cada brazo); se ponen claves donde el movimiento cambia, no en todos los
fotogramas; y el borde se suaviza (difuminado) y se ajusta al desenfoque de movimiento del plano, porque
un borde duro sobre una imagen movida delata el recorte.

### La captura de movimiento

La pariente 3D de la rotoscopia es la captura de movimiento: en lugar de dibujar sobre la imagen, se
registran con sensores los movimientos de un actor y se trasladan al esqueleto del modelo. El mismo RA
7 del módulo 1087 describe los pasos: **«Se ha realizado la ubicación definitiva de los sensores de
captura en los puntos adecuados del actor, respondiendo a las exigencias del software y mediante
diversos ensayos.»** (7.c) y **«Se ha realizado la captura de movimiento trasladando los resultados al
setup del modelo que se va a animar.»** (7.d). Los contenidos nombran las **«Herramientas de captura de
movimiento: software, cámaras y sensores.»**

## 5. Tracking

### Qué es

El tracking o seguimiento de movimiento es, en palabras de Blackmagic, **«one of the most useful and
essential techniques available to a compositor. It can be roughly defined as the creation of a motion
path from analyzing a specific area in a clip over time.»** (la creación de una trayectoria a partir del
análisis de una zona concreta del plano a lo largo del tiempo). Esa trayectoria se aplica después a lo
que se quiera; los usos que da el manual: **«stabilization, motion smoothing, matching the motion of
one object to that of another»** (estabilizar, suavizar el movimiento, hacer que un objeto siga el
movimiento de otro).

Cómo funciona, en una línea: el programa elige un rasgo de la imagen con contraste suficiente y lo
busca fotograma a fotograma, generando una trayectoria que después se aplica a lo que se quiera.

No hay que confundirlo con sus vecinos de sala:

| Término | Qué es |
|---|---|
| *Motion blur* | El desenfoque que deja un objeto al moverse deprisa |
| *Keying* | La incrustación del epígrafe 3 |
| *Motion tracking* | El seguimiento de un punto o de un plano a lo largo del tiempo |
| *Time remapping* | El cambio de velocidad de una capa |

### Los tipos de seguimiento

Blackmagic distingue tres herramientas (cap. 81):

| Tipo | Qué hace, según Blackmagic |
|---|---|
| De punto (*Tracker*) | **«Follows a relatively small, identifiable feature or pattern in a clip to derive a 2D motion path. This is sometimes referred to as point tracking.»** (sigue un rasgo pequeño e identificable y saca una trayectoria 2D) |
| Planar (*Planar Tracker*) | **«Follows a flat, unvarying surface area in a clip to derive a 2 ½D motion path including perspective. A planar tracker is also more tolerant than a point tracker when some tracked pixels move offscreen or become obscured.»** (sigue una superficie plana y saca una trayectoria con perspectiva; tolera mejor que parte de la zona salga de cuadro o quede tapada) |
| De cámara (*Camera Tracker*) | **«Tracks multiple points or patterns in a clip and performs a more sophisticated analysis by comparing those moving patterns. The result is a precise recreation of the live-action camera in virtual 3D space.»** (sigue muchos puntos, los compara y reconstruye la cámara real en un espacio 3D virtual) |

El seguimiento de punto sirve para **«tracking, stabilizing, matching moving, and corner-pinning
operations»**: seguir, estabilizar, casar el movimiento y el *corner pin*, que es deformar una imagen
para encajar sus cuatro esquinas en cuatro puntos seguidos (una pantalla, un cartel).

Lo que se recupera según los puntos que se siguen, en los cuatro grados que conviene distinguir:

| Grado | Qué recupera | Para qué sirve |
|---|---|---|
| De un punto | Posición | Pegar un elemento a algo que se mueve |
| De dos puntos | Posición, escala y rotación | Un rótulo que acompaña a un objeto que se acerca |
| De plano | La deformación de una superficie entera | Sustituir la pantalla de un móvil en mano |
| De cámara | El movimiento de la cámara en el espacio | Meter un objeto tridimensional en la escena |

### El seguimiento de cámara

El seguimiento de cámara es el puente entre la imagen grabada y el 3D. Blackmagic: **«Camera tracking
is used for match moving, and it’s a vital link between 2D scenes and 3D scenes, allowing compositors
to integrate 3D CGI elements into live-action clips.»** (sirve para casar el movimiento y permite
integrar elementos 3D generados por ordenador en planos reales). Su resultado: **«The Camera Tracker’s
purpose is to create a 3D animated camera and point cloud of the scene.»** (una cámara 3D animada y una
nube de puntos de la escena).

Tiene dos fases: **«Tracking, which is the analysis of a scene.»** (el análisis de la escena) y
**«Solving, which calculates the virtual 3D scene.»** (la resolución, que calcula la escena 3D virtual).

Tres condiciones para que salga bien, todas de la documentación:

- Seguir sólo lo que está fijo: **«camera tracking algorithms follow features that are “nailed to the
  set.” Objects in the scene that move independently of the camera movement in the shot, such as cars
  driving or people walking, cause poor tracks, so masks can be used to restrict the features that are
  tracked»** (el algoritmo sigue lo que está «clavado al decorado»; coches o personas que se mueven por
  su cuenta estropean el seguimiento, y se excluyen con máscaras).
- Dar los datos de la cámara: **«it is helpful to provide specific camera metadata, such as the sensor
  size and the focal length of the lens»** (tamaño del sensor y focal).
- Contar con la distorsión del objetivo. Blender: **«All cameras record distorted video.»** y **«For
  accurate camera motion, the exact value of the focal length and the “strength” of distortion are
  needed.»** (para un movimiento de cámara exacto hacen falta la focal y la intensidad de la
  distorsión).

### Estabilizar

El mismo análisis sirve para lo contrario: en lugar de mover un elemento con el plano, quitar el
movimiento del plano. Blender: **«the 2D Stabilization is able to detect and compensate such
movements»** (detecta y compensa el temblor). La estabilización recorta y amplía la imagen para
esconder los bordes que quedan al moverla (oficio).

### Por qué falla y cómo se prepara

El aviso de oficio: el seguimiento falla cuando el punto elegido no tiene contraste, se sale del
cuadro o se desenfoca. Elegir bien el punto es el noventa por ciento del trabajo.

El seguimiento se prepara antes de grabar. La norma de enseñanza lo pone entre los contenidos del
módulo 0907: **«Planificación de la grabación para efectos de seguimiento.»** En la práctica (oficio):
marcas de seguimiento en el decorado o en el croma, que se borran después; nada de desenfoque ni de
movimientos demasiado rápidos en el plano que se va a seguir; y anotar la focal y la cámara.

El seguimiento en directo —cámaras con sensores que envían su posición al motor de grafismo para la
realidad aumentada y los escenarios virtuales— es el tema 6.

## 6. Efectos visuales

### Qué son

Tampoco los efectos visuales tienen definición en norma. En el oficio se distinguen los efectos
especiales, que se producen físicamente ante la cámara durante la grabación (lluvia, humo, explosiones,
maquetas, animatrónica), de los efectos visuales o VFX, que se crean o se añaden a la imagen en
postproducción con composición, animación 3D, rotoscopia y tracking (oficio). La norma de enseñanza
usa la expresión clásica: entre los proyectos que el módulo 1087 aconseja trabajar están las
**«animaciones para incrustación de efectos especiales en películas de imagen real»**.

Un efecto visual es, por tanto, la suma de todo lo anterior: se graba el plano pensando en el efecto
(croma, marcas de seguimiento), se sigue la cámara, se genera el elemento en 3D con la misma cámara
virtual, se recorta lo que haya de ir delante por rotoscopia y se compone. El grafista de televisión lo
usa en cabeceras, promociones, reconstrucciones e infografías que integran elementos en imagen real.

### Los efectos 3D: partículas, dinámicas y multitudes

El RD 1583/2011 dedica el RA 4 del módulo 1087 a los efectos 3D, **«aplicando las leyes físicas al
universo virtual»**:

- Partículas: **«Se han generado las partículas y se han creado los emisores necesarios para cada
  plano, asignando los campos de fuerza que definirán el comportamiento de estas.»** (4.b). Un emisor
  suelta partículas; los campos de fuerza (gravedad, viento, turbulencia) las mueven. Con partículas
  se hacen humo, fuego, chispas, lluvia, nieve o polvo (oficio).
- Sólidos rígidos: **«Se han creado objetos dinámicos (rigid bodies) de comportamiento activo o
  pasivo, simulando movimientos y colisiones»** (4.c): objetos que caen, chocan y rebotan sin
  deformarse.
- Cuerpos blandos: **«Se han creado las geometrías controladas por partículas (soft bodies) necesarias
  para cada plano, pintando las influencias y generando los tensores que definirán el movimiento.»**
  (4.d).
- Multitudes: **«Se han creado multitudes realizando la sustitución de las partículas por modelos
  animados.»** (4.e): cada partícula se convierte en un personaje.

### La integración

Un efecto visual está bien hecho cuando no se nota. La norma pide, al acabar un proyecto de animación,
generar **«los efectos para la integración, movimiento de multiplanos y reencuadre»** y **«los efectos
de foco y desenfoque de movimiento, ajustándose a las diferentes resoluciones de exhibición.»**
(módulo 1085, RA 5.c y 5.d). En la práctica (oficio), el elemento añadido ha de casar con el plano en
cinco cosas: la perspectiva y el movimiento (tracking), la luz (dirección y dureza de las sombras), el
color y el contraste (corrección), el enfoque y el desenfoque de movimiento, y el grano o el ruido de
la imagen. Y el borde, que es donde se delatan casi todos los efectos: un alfa bien premultiplicado y
una máscara suavizada (epígrafes 3 y 4).

### Los efectos y la información

El Libro de Estilo de Canal Sur pone límites a los efectos en la información, y el grafista que hace
efectos para los informativos los aplica:

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

- No lucirse. Del informe, el Libro de estilo dice: **«Tampoco es oportuno el abuso de cifras,
  gráficos, postproducciones o alardes técnicos que dificulten su comprensión.»** (3.3, p. 47). El
  efecto en la información está al servicio de que se entienda.

La reconstrucción de un suceso con infografía animada es la aplicación más directa al grafista de la
regla del rótulo «reconstrucción» (tema 4). No se ha localizado un manual de efectos o de grafismo
animado publicado por Canal Sur.

## Aplicación práctica

### Cinco encargos corrientes

Los pasos son de oficio y aplican lo visto en el tema.

1. Animar la entrada de un rótulo. Dos claves de posición: fuera de cuadro y en su sitio. Como el
   rótulo llega y se para, la curva frena al final (suavizado de salida, *ease out*, en el sentido de
   Blender: sale deprisa y frena); la opacidad puede subir en los primeros fotogramas. La salida, al
   revés: arranca despacio y acelera (*ease in*). Se revisa la curva, no sólo las claves.
2. Pegar un rótulo o una flecha a un coche que se aleja. Seguimiento de dos puntos (posición, escala y
   rotación) y el rótulo enlazado a la trayectoria. Si hay que sustituir lo que se ve en una pantalla o
   un cartel, seguimiento planar y *corner pin*. Si hay que meter un objeto 3D en el plano, seguimiento
   de cámara, con la focal y el sensor anotados en la grabación.
3. Separar a una persona de un fondo sin croma para poner un grafismo detrás. Rotoscopia con varias
   máscaras sencillas, movidas con el seguimiento y corregidas donde cambia la forma; o una máscara
   asistida por IA, revisada fotograma a fotograma. Bordes suavizados y con el desenfoque del plano.
4. Tramar el rostro de un menor en una pieza informativa (LE 9.9). Máscara sobre la cara, enlazada a un
   seguimiento, con pixelado o desenfoque dentro; se revisa en los giros y en las entradas y salidas de
   cuadro. Si el seguimiento se pierde un solo fotograma, la cara se ve.
5. Entregar una cortinilla que va encima del programa. ProRes 4444 (o 4444 XQ) en MOV, o una secuencia
   PNG, TGA o TIFF; nunca JPG ni ProRes 422. Se dice si el alfa es directo o premultiplicado, y se
   comprueba sobre fondos negro, blanco y gris: un halo claro alrededor delata un alfa mal
   interpretado. Formatos y zonas seguras de la entrega: tema 8.

### Cuentas que se piden

Las cuentas son aritmética propia, con la cadencia de 25 imágenes por segundo.

- Duración en fotogramas = segundos × cadencia. Una cortinilla de 2 segundos son 2 × 25 = 50
  fotogramas; una entrada de rótulo de 0,8 segundos, 0,8 × 25 = 20 fotogramas.
- Intermedios entre dos claves: si una clave está en el fotograma 0 y la siguiente en el 20, el
  programa interpola los 19 fotogramas que hay entre ellas (del 1 al 19).
- Peso de un fotograma con alfa sin comprimir: una imagen de 1920 × 1080 píxeles a 32 bits (4 bytes)
  por píxel ocupa 1920 × 1080 × 4 = 8.294.400 bytes, unos 8,3 MB. Una secuencia de 10 segundos son 250
  fotogramas: 250 × 8.294.400 = 2.073.600.000 bytes, unos 2,07 GB. Por eso las secuencias de imágenes
  se guardan comprimidas sin pérdida o se entregan en un códec con alfa.
- Bits del TGA: 8 + 8 + 8 + 8 = 32 con alfa; 24 sin él.

## Normativa que el tema invoca

- Real Decreto 1583/2011, de 4 de noviembre, por el que se establece el Título de Técnico Superior en
  Animaciones 3D, Juegos y Entornos Interactivos y se fijan sus enseñanzas mínimas (BOE núm. 301, de
  15-XII-2011): artículo 5, letras c) y d); anexo I, módulos 1085 «Proyectos de animación audiovisual
  2D y 3D» (RA 3, 4 y 5), 1086 «Diseño, dibujo y modelado para animación» (RA 5), 1087 «Animación de elementos 2D y 3D» (RA 1, 2, 3, 4, 6 y 7, orientaciones
  pedagógicas y contenidos), 1088 «Color, iluminación y acabados 2D y 3D» (RA 1, 2 y 3) y 0907
  «Realización del montaje y postproducción de audiovisuales» (RA 3 y contenidos). Modificado por el
  Real Decreto 500/2024, de 21 de mayo, en módulos no técnicos; el anexo de convalidaciones del RD
  1583/2011 lo derogó el Real Decreto 1085/2020, de 9 de diciembre; corrección de errores en el BOE núm. 61, de
  12-III-2012, que afecta a códigos de módulo y al anexo de convalidaciones.
- Real Decreto 1680/2011, de 18 de noviembre, título de Técnico Superior en Realización de proyectos
  audiovisuales y espectáculos: el mismo módulo 0907.

Son normas de enseñanza: fijan qué se aprende en un título de formación profesional, no obligan a la
RTVA ni regulan el trabajo del grafista. El Libro de estilo es norma interna de la casa; los manuales
de Blender, Resolve y ProRes son documentación de fabricante.

## Lo que este tema no da, y dónde está

- Una definición normativa de motion graphics, de efectos visuales o de efectos especiales: no se ha
  encontrado en norma ni en manual leído; el tema los define como oficio.
- Los principios clásicos de la animación (los llamados doce principios de la animación de Disney): ni
  la norma de enseñanza ni los manuales leídos los recogen, no se han leído en una fuente citable y no se
  dan.
- Los rótulos exactos de las órdenes de Adobe After Effects (tipos de capa, asistente de fotogramas
  clave, recorte de trazado, complementos como Mocha): la documentación de Adobe no se ha podido leer, y
  el tema no los da. Tampoco Cinema 4D, Maya, Houdini ni Nuke.
- Qué programas de animación y composición usa Canal Sur: no consta en documento publicado.
- Formatos de entrega a emisión, códecs, zonas seguras, colorimetría y HDR de un grafismo, y la salida de
  relleno y llave de un motor de grafismo: tema 8.
- Escenarios virtuales, realidad aumentada, seguimiento de cámara en directo y motores de tiempo real:
  tema 6.
- Plantillas y automatización del grafismo: tema 9.
- Uso de la IA generativa, deepfakes y trazabilidad de una imagen manipulada: tema 15.
- Grafismo por géneros (cabeceras, promociones, continuidad): tema 3; infografía y reconstrucciones:
  tema 4.
- Derechos de las músicas, imágenes y modelos 3D que se usan en una pieza: tema 11.
- El montaje, las transiciones y los efectos de tiempo en el sistema de edición: no los pide este
  enunciado.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| RD 1583/2011 (BOE-A-2011-19532), texto del diario y ficha de análisis del BOE | Fases 2D y 3D, carta de animación, intercalación, rigging FK/IK, efectos 3D, cámara virtual, rotoscopia y captura de movimiento, render por capas, mapas UV y materiales, composición multicapa, keys, seguimiento, integración | 29-09-2026 |
| RD 1583/2011, módulo 1086, RA 5 (5.a y 5.c) | Métodos de modelado | 29-09-2026 |
| RD 500/2024 (BOE-A-2024-10685), art. 7 | Que la modificación del anexo I no toca los módulos técnicos citados | 29-09-2026 (lectura de la fase de investigación) |
| RD 1085/2020 (BOE-A-2020-17274), disposición derogatoria única, apartado 2 | Que lo derogado del RD 1583/2011 es el anexo de convalidaciones | 29-09-2026 |
| Corrección de errores del RD 1583/2011 (BOE-A-2012-3441) | Que sólo corrige el código del módulo de formación en centros de trabajo y el anexo IV | 29-09-2026 |
| RD 1680/2011, módulo 0907, RA 3.b y 3.c | Composición multicapa y tipos de key (mismo texto que el módulo 0907 del RD 1583/2011) | Texto tomado del tema cerrado del puesto de Realizador/a; cotejado con el RD 1583/2011 el 29-09-2026 |
| Blender Foundation, *Blender 5.2 LTS Manual* (docs.blender.org/manual/en/latest/): Glossary; Animation › Introduction; Keyframes › Introduction; Graph Editor › F-Curves › Properties; Movie Clip › Tracking › Introduction; Masking › Introduction | Animación, fotograma clave, interpolación, curvas, suavizado, rigging, FK/IK, malla, UV, render, trazado de rayos, desenfoque de movimiento, máscara, alfa directo y premultiplicado, tracking, estabilización, rotoscopia con máscaras | 29-09-2026 |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual* (julio de 2026): caps. 73 (expresiones simples), 56 (plantillas Fusion), 77 (pp. 1726-1728, canales y premultiplicación), 79 (máscaras), 81 (Tracker), 85 (seguimiento de cámara), 139 (Magic Mask); introducción | Motion graphics como tarea, expresiones y plantillas, alfa y sus reglas, máscaras y rotoscopia, tipos de tracker, seguimiento de cámara, rotoscopia asistida por IA | 29-09-2026 |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual*, cap. 55, p. 1199 | Suavizado de transiciones (*Ease*) | Texto tomado del tema cerrado del puesto de Operador/a Montador/a de Vídeo |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual*, cap. 94 (Composite Nodes, nodo Merge, *Apply Mode*), pp. 2266-2267 | Modos de fusión | 29-09-2026 |
| Blender Foundation, *Blender 5.2 LTS Manual*, Glossary: «NURBS» y «Subdivision Surface» | Definición de los métodos de modelado | 29-09-2026 |
| Adobe, «Descripciones de modos de fusionar en Photoshop» (ayuda en español, actualizada el 2-XII-2025) | Nombres en castellano de los modos de fusión | 29-09-2026 |
| W3C, *Portable Network Graphics (PNG) Specification (Third Edition)*, recomendación de 24-VI-2025, 11.2.1 IHDR, tabla 12 | Profundidad por muestra; PNG con alfa a 8 o 16 bits por canal | 29-09-2026 |
| Apple, *Apple ProRes* (white paper, abril de 2022) | ProRes 4444 y 4444 XQ, únicos ProRes con alfa; alfa sin pérdidas hasta 16 bits | 29-09-2026 |
| *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004: 3.3 | Abuso de postproducciones y alardes técnicos | 29-09-2026 |
| Libro de estilo: 3.2.2, 9.9, 9.9.1 y 9.9.2 | Ocultar rostros, no acentuar, rótulos «reconstrucción» y «Archivo» | Texto tomado del tema cerrado del puesto de Operador/a Montador/a de Vídeo |

La fecha de trabajo del encargo es el 24-09-2026; las fuentes se leyeron en las fechas de la tabla.

Oficio o desarrollo propio, declarado así en el texto: las técnicas de animación de fotograma
(*stop motion*, pixilación, rotoscopia, animatrónica) y su cuadro; la cadencia de 25 imágenes por
segundo; la lectura de las fases 2D y 3D; la regla para distinguir FK de IK y su uso; la definición de
motion graphics y su uso en televisión; el ritmo y el sonido de una pieza; las dos maneras de organizar
una composición (capas y nodos); la definición de capa y de precomposición; las familias de
incrustación, el porqué del fondo verde, las consecuencias del croma y el cuadro de color frente a
luminancia; las tres señales de una incrustación; el funcionamiento del canal alfa, el cuadro de
formatos con alfa y las cuentas del TGA y del PNG; el oscurecimiento de bordes del error inverso de premultiplicado;
el funcionamiento y el aviso de la máscara; las reglas de rotoscopia; el cuadro de los cuatro grados de
seguimiento y el aviso sobre su fallo; la preparación de la grabación; la estabilización con recorte; la
distinción entre efectos especiales y visuales; los usos de las partículas; el uso de los modos de fusión; las cinco condiciones de la
integración; el trabajo del tramado con seguimiento; y la aplicación práctica. Las cuentas son
aritmética propia.
