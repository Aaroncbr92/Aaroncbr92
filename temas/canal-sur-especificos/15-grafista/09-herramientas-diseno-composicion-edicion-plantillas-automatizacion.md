# Tema 9 del específico de Grafista · Herramientas profesionales de diseño, composición, edición, plantillas y automatización gráfica

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Grafista · punto 9 |
| Sirve para | Grafista de Canal Sur (grupo B03): test de teoría específica y de aplicación práctica, y prueba práctica del puesto |
| Fuente | Sin norma: ninguna regula qué programas usa un grafista ni cómo. Lo propio de la casa: X Convenio Colectivo de la RTVA (anexo III, ficha del Grafista). Documentación de fabricante: Blackmagic Design (*DaVinci Resolve 21 Reference Manual*), Adobe (ayuda de Premiere sobre plantillas de *motion graphics* y Media Encoder, ayuda de After Effects sobre plantillas de *motion graphics* y ayuda de Photoshop sobre gráficos con datos, acciones y lotes), Blender Foundation (*Blender 5.2 LTS Manual*), Vizrt (*Viz Pilot Edge User Guide* 3.5, *Viz Multiplay User Guide* 3.3, *Viz Engine Administrator Guide* 5.2, *Introduction to Viz Artist* 5.3), Chyron (página de *PRIME CG* y nota de prensa de PRIME 5.3), Epic Games (documentación de Unreal Engine 5.8 sobre *Motion Design*), Apple (*Apple ProRes*, abril de 2022) y el proyecto CasparCG; especificación pública del protocolo MOS (mosprotocol.com). Lo demás, oficio declarado como tal |
| Redacción que se estudia | Convenio (BOJA núm. 240, de 10-XII-2014); documentación de fabricante en la versión publicada el día en que se leyó (fechas en «Trazabilidad») |
| Extensión | 11.000 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA). «El convenio» es el X
Convenio Colectivo de la RTVA.

Los términos técnicos del tema, presentados de entrada: los formatos de fichero de imagen, que se
nombran por su extensión (PSD, TIFF o TIF, PNG, JPG, TGA, GIF, SVG, EPS y AI, el nativo del programa
vectorial de Adobe); el modelo de color de cian, magenta, amarillo y negro (CMYK) y el de rojo, verde
y azul (RGB), que con el canal alfa (A) se escribe RGBA; las dos y las tres dimensiones (2D y 3D); la
interfaz de programación de aplicaciones (API, del inglés *application programming interface*); el
lenguaje de marcas extensible (XML) y el de las páginas web (HTML); el protocolo de comunicaciones con
servidores de objetos de medios (MOS, del inglés *Media Object Server*) y el sistema informático de
redacción (NCS, del inglés *newsroom computer system*, como lo abrevia la especificación MOS); el
generador de caracteres (CG, del inglés *character generator*), el equipo que compone los rótulos; la
familia de protocolos de internet (TCP/IP); la licencia pública general de GNU (GPL, del inglés
*General Public License*); la Sociedad de Ingenieros de Cine y Televisión (SMPTE, del inglés
*Society of Motion Picture and Television Engineers*) y la Unión Europea de Radiodifusión (EBU, del
inglés *European Broadcasting Union*). Palabras en inglés que el tema usa porque así las rotula el programa o
la fuente: *template* (plantilla), *preset* (ajuste guardado), *script* (guion de programación),
*render* (cálculo y escritura de la imagen o del fichero de salida), *rundown* (escaleta), *playout*
(emisión), *plugin* (módulo que se añade a un programa). Photoshop, Illustrator, InDesign, After Effects, Premiere y Media Encoder son
programas de Adobe; DaVinci Resolve y Fusion, de Blackmagic Design; Blender, de la Blender
Foundation; Cinema 4D, un programa de 3D; Viz Artist, Viz Engine, Viz Pilot, Viz Trio y Viz Multiplay,
de Vizrt; PRIME y CAMIO, de Chyron; Unreal Engine, de Epic Games; Unity, otro motor de tiempo real;
CasparCG, un servidor de grafismo de programa libre; ProRes 4444 y 4444 XQ, nombres de códec de
Apple. Se citan como ejemplos: qué programas usa CSRTV
no consta en documento publicado.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.15, punto 9): «Herramientas
> profesionales de diseño, composición, edición, plantillas y automatización gráfica.»

Qué se puede preguntar: qué familias de programa usa un grafista y qué distingue al mapa de bits del
vectorial; qué es un trazado, qué hace el calco de imagen y qué hace cada operación de buscatrazos; qué
elementos tiene una curva Bézier; qué formato conserva capas y cuál no admite CMYK; qué es el área de
trabajo de una línea de tiempo, qué es precomponer, qué capa está delante, a qué capas afecta una luz,
qué es el calado de una máscara, qué es interpolar y qué es una expresión de movimiento aleatorio; qué
hace «recopilar archivos»; qué diferencia la composición por capas de la de nodos y qué reglas tiene el
alfa premultiplicado en un compositor; qué diferencia el renderizado diferido del tiempo real y qué es
un motor gráfico; qué dice la ficha del convenio del Grafista; qué es una plantilla, qué son los
Fusion Titles, un fichero .mogrt, una plantilla de datos, un *preset* y una variable de metadatos;
cómo se reparten diseño, relleno y emisión en un sistema de grafismo de directo y qué son las Base
Scenes, el Rundown Server o CasparCG; qué automatizan las expresiones y los *scripts*, en qué lenguajes;
qué es MOS, qué tres mensajes intercambia y si es norma oficial; qué automatizan la cola de *render* y
las carpetas vigiladas, y qué no automatiza nada de eso. En la prueba práctica: montar la plantilla de
un rótulo, entregar una cabecera con transparencia, preparar el grafismo de datos de una noche
electoral y sacar muchas versiones de una misma pieza.

<!-- indice -->

## Índice

- [De dónde sale este tema](#de-dónde-sale-este-tema)
- [1. Herramientas profesionales](#1-herramientas-profesionales)
  - [Qué dice el convenio](#qué-dice-el-convenio)
  - [Las familias de programa](#las-familias-de-programa)
  - [Diferido y tiempo real](#diferido-y-tiempo-real)
  - [Licencias y versiones](#licencias-y-versiones)
- [2. Diseño](#2-diseño)
  - [El programa de imagen fija](#el-programa-de-imagen-fija)
  - [El programa vectorial](#el-programa-vectorial)
  - [Qué se diseña en cada familia (oficio)](#qué-se-diseña-en-cada-familia-oficio)
- [3. Composición](#3-composición)
  - [Capas y nodos](#capas-y-nodos)
  - [La línea de tiempo y el orden de las capas](#la-línea-de-tiempo-y-el-orden-de-las-capas)
  - [La máscara y sus parámetros](#la-máscara-y-sus-parámetros)
  - [La interpolación](#la-interpolación)
  - [El alfa dentro del compositor](#el-alfa-dentro-del-compositor)
  - [Recopilar archivos](#recopilar-archivos)
- [4. Edición](#4-edición)
  - [El programa de edición y el grafista](#el-programa-de-edición-y-el-grafista)
  - [Qué fichero se entrega](#qué-fichero-se-entrega)
  - [Cómo se reparten grafismo y montaje (oficio)](#cómo-se-reparten-grafismo-y-montaje-oficio)
- [5. Plantillas](#5-plantillas)
  - [Qué es una plantilla](#qué-es-una-plantilla)
  - [Plantillas de rótulo en el programa de edición](#plantillas-de-rótulo-en-el-programa-de-edición)
  - [Hacer la plantilla propia en un compositor](#hacer-la-plantilla-propia-en-un-compositor)
  - [Plantillas en el sistema de grafismo de directo](#plantillas-en-el-sistema-de-grafismo-de-directo)
  - [Plantillas de salida: los *presets*](#plantillas-de-salida-los-presets)
  - [Plantillas de nombre: las variables de metadatos](#plantillas-de-nombre-las-variables-de-metadatos)
- [6. Automatización gráfica](#6-automatización-gráfica)
  - [Qué es automatizar el grafismo](#qué-es-automatizar-el-grafismo)
  - [Las expresiones](#las-expresiones)
  - [Los *scripts*](#los-scripts)
  - [Los datos rellenan la plantilla](#los-datos-rellenan-la-plantilla)
  - [La escaleta manda: el protocolo MOS](#la-escaleta-manda-el-protocolo-mos)
  - [La emisión automatizada del grafismo](#la-emisión-automatizada-del-grafismo)
  - [Automatizar la salida](#automatizar-la-salida)
- [Aplicación práctica](#aplicación-práctica)
  - [El rótulo de identificación de un informativo](#el-rótulo-de-identificación-de-un-informativo)
  - [Una cabecera de programa con transparencia](#una-cabecera-de-programa-con-transparencia)
  - [El grafismo de datos de una noche electoral](#el-grafismo-de-datos-de-una-noche-electoral)
  - [Cuarenta versiones de una misma pieza](#cuarenta-versiones-de-una-misma-pieza)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## De dónde sale este tema

Ninguna norma dice qué programas usa un grafista ni cómo se usan. El convenio le da el diseño gráfico
de canales y programas, sin nombrar herramienta alguna. Lo técnico sale de la documentación publicada
de los fabricantes, que describe sus propios productos y se cita como ejemplo, no como regla del
sector; y de la especificación pública de un protocolo de la industria, MOS. Los rótulos de menú y los
nombres de función cambian de un programa a otro y de una versión a la siguiente: lo que se estudia es
qué hace cada función, no dónde está el botón. El resto es costumbre de oficio, y así se dice en cada
caso.

Los cinco términos del enunciado se leen en dos mitades (oficio). Las tres primeras —diseño,
composición, edición— son familias de programa: con qué se hace una pieza. Las dos últimas
—plantillas y automatización— son la manera de trabajar de una televisión: cómo se consigue que miles
de rótulos al año salgan iguales, a tiempo y sin teclear dos veces el mismo dato.

Lo que otros temas ya dan y aquí sólo se remite: animación, motion graphics, composición, rotoscopia y
tracking, en el tema 5; los sistemas de grafismo en tiempo real, los motores y las pantallas, en el
tema 6; formatos de entrega, códecs, alfa, zonas seguras y color, en el tema 8.

## 1. Herramientas profesionales

### Qué dice el convenio

El convenio describe el puesto en su ficha (anexo III), y su función básica ya fija para qué son las
herramientas: **«Crear y realizar, con criterios artísticos, el diseño gráfico que requieren los
canales y programas.»**

En la RTVA, el diseño es del Grafista (5345100, p. 129): **«Diseñar y realizar y todo tipo de imagen
gráfica para programas y postproducciones, y otros fines promocionales.»** y **«Realizar escenarios
virtuales y diseñar la representación gráfica de la información. Realizar el asesoramiento estético a
otras áreas como rotulación o postproducción.»** La ficha no le atribuye el lanzamiento de rótulos en
el control.

La ficha no nombra un solo programa. Qué herramientas tiene hoy el departamento gráfico de CSRTV no
consta en documento publicado leído; los productos que el tema cita son ejemplos con documentación
pública.

### Las familias de programa

Un grafista trabaja con varias familias de programa, y conviene tener el cuadro (oficio):

| Familia | Con qué trabaja | Qué pasa al ampliar | Programas de ejemplo |
|---|---|---|---|
| Mapa de bits | Una rejilla de píxeles | Pierde calidad: hay que inventar píxeles | Photoshop |
| Vectorial | Descripciones matemáticas de curvas | No pierde nada: se recalcula | Illustrator |
| Maquetación | Páginas con texto e imágenes colocadas | Según lo que coloque dentro | InDesign |
| Composición y animación | Capas en una línea de tiempo | Según la capa | After Effects |
| Tres dimensiones | Geometría, materiales y luces | No pierde: se vuelve a calcular | Blender, Cinema 4D |

A esas cinco se suman dos que el enunciado nombra aparte (oficio): el programa de edición, donde el
grafismo se coloca sobre las imágenes montadas (epígrafe 4), y el sistema de grafismo de directo, que
dibuja el rótulo en el instante de la emisión (epígrafe 5 y tema 6). Y hay programas que reúnen varias
familias: el manual de DaVinci Resolve lo presenta así: **«DaVinci Resolve integrates editing,
compositing and motion graphics, color correction, audio recording and mixing, and finishing within a
single, easy to learn application.»** (edición, composición, *motion graphics*, corrección de color,
grabación y mezcla de audio y acabado en una sola aplicación; su módulo de composición es Fusion).

La primera fila del cuadro es la que más conviene tener clara: en un programa de imagen se puede duplicar el
tamaño sin pérdida de calidad sólo si la imagen es vectorial. El matiz: un programa de mapa de bits,
aun así, admite objetos vectoriales dentro —formas, texto, objetos inteligentes—, y lo que no pierde al
ampliarse es lo vectorial, esté donde esté. En la práctica una ampliación al doble con buen remuestreo
casi no se nota. «Casi no se nota» no es «sin pérdida alguna».

### Diferido y tiempo real

La otra línea que divide las herramientas es cuándo se calcula la imagen (oficio):

| Modo | Cuándo se calcula la imagen | Ejemplos |
|---|---|---|
| Renderizado diferido | Antes de emitir, todo el tiempo que haga falta | Blender, Cinema 4D |
| Tiempo real | Mientras se emite, a la velocidad del vídeo | Unreal, Unity, Vizrt, Chyron |

*Render*, en el glosario de Blender, es **«The process of computationally generating a 2D image from
3D geometry.»** (el cálculo de una imagen 2D a partir de geometría 3D). Que un programa lo haga en
diferido significa que puede tardar lo que haga falta en cada fotograma; el mismo glosario dice del
trazado de rayos que es más exacto que la técnica de líneas de barrido, **«but much slower»** (pero
mucho más lento). En directo no hay ese tiempo: un sistema de grafismo o un motor tiene que dibujar la
imagen tantas veces por segundo como fotogramas tenga la señal (tema 6).

Los programas de tiempo real que conviene distinguir (oficio):

| Programa | Qué es |
|---|---|
| Unreal | Motor gráfico de videojuego, hoy muy usado en televisión |
| Unity | El otro motor grande, con programación escrita |
| Vizrt | Sistema de grafismo de televisión |
| Chyron | Sistema de grafismo y titulación de televisión |

Por qué un motor de videojuego está en el temario de un grafista de televisión: porque la
escenografía virtual y la realidad aumentada de los platós se calculan hoy con ellos. Unreal
Engine tiene además un conjunto de herramientas propio para el grafismo de emisión, Motion Design,
que su fabricante presenta como **«an Internal Editor plugin for broadcasting»** (un módulo del editor
para emisión; qué hace, en el tema 6 y en el epígrafe 5).

### Licencias y versiones

Una herramienta profesional no es sólo un programa: es un programa con una licencia, y la licencia
decide qué funciones hay (oficio). Tres ejemplos documentados:

- En Vizrt, **«The available features and modes of the software depend on the license on the
  connected license hardware dongle.»** (las funciones y los modos dependen de la licencia de la llave
  física conectada; *Introduction to Viz Artist* 5.3).
- DaVinci Resolve tiene una versión gratuita y otra, Studio, con funciones que la
  gratuita no tiene: el *render* remoto, los módulos de integración por *scripts* (epígrafe 6) o la
  segunda versión de la máscara asistida por inteligencia artificial, Magic Mask, que el manual marca
  **«Studio Version Only»**.
- CasparCG, un servidor de grafismo de emisión, es programa libre: **«CasparCG Server is distributed
  under the GNU General Public License GPLv3 or higher»** (se distribuye bajo la GPL, versión 3 o
  posterior).

La consecuencia práctica (oficio): un proyecto que usa una función de la versión Studio no se abre
entero en un puesto con la gratuita, y una plantilla que depende de una licencia no funciona en un
motor que no la tenga. Antes de mandar un proyecto a otro equipo se comprueba que el otro lado tiene
la misma versión y la misma licencia.

## 2. Diseño

### El programa de imagen fija

Lo que se estudia de él es dónde está cada función y para qué sirve (oficio).

El trazado (*path*) permite contornear con precisión un objeto irregular. Qué es un trazado, en una
línea: una curva vectorial dibujada dentro de un documento de mapa de bits. No pinta píxeles:
describe un contorno, y de ahí que sirva para recortar con precisión lo que una selección a mano no
consigue.

Qué es un canal: cada una de las capas de información de color o de selección de la imagen. Una
imagen en rojo, verde y azul tiene tres canales de color más el compuesto; cada máscara guardada añade
un canal alfa.

Para conservar capas, efectos y máscaras se guarda en el formato nativo, `PSD`. Qué conserva cada
formato:

| Formato | ¿Conserva capas? |
|---|---|
| `PSD` | Sí: capas, efectos, máscaras, canales y trazados |
| `TIFF` | Puede llevar capas, pero no es su cometido y no todos los programas las leen |
| `TGA` | No. Es una imagen plana con canal alfa |
| `PNG` | No. Imagen plana con transparencia |

Y qué formato admite el modo de color de la imprenta; la razón está en para qué nació cada uno:

| Formato | Para qué nació | ¿Admite CMYK? |
|---|---|---|
| `PSD` | Trabajo en el propio programa | Sí |
| `JPG` | Fotografía, también para imprenta | Sí |
| `TIFF` | Artes gráficas | Sí |
| `PNG` | La web, donde todo es rojo, verde y azul | No |

La regla que lo fija: cian, magenta, amarillo y negro es el modelo de la tinta; rojo, verde y azul,
el de la pantalla. Un formato pensado para la web no necesita el de la tinta, y por eso no lo lleva.
Para televisión todo se diseña en RGB; cómo pasa el color del programa de diseño a la señal de vídeo
es el tema 8.

### El programa vectorial

Cuatro funciones que conviene no confundir (oficio):

| Función | Qué hace |
|---|---|
| Calco de imagen | Convierte un mapa de bits en vectores |
| Buscatrazos (*pathfinder*) | Combina formas: unir, restar, intersecar, excluir, dividir |
| Fusión (*blend*) | Genera pasos intermedios entre dos objetos |
| Ajustar segmentos | Modifica un tramo de una curva ya dibujada |

Las operaciones de buscatrazos, que se reconocen mirando el resultado:

| Operación | Qué queda |
|---|---|
| Unir | Una sola forma con el contorno exterior de todas |
| Restar | La forma de abajo menos lo que la de arriba tapaba |
| Intersecar | Sólo la zona común a las dos |
| Excluir | Todo menos la zona común: el solape queda hueco |
| Dividir | Tantas formas como trozos creen los cortes |

Cómo se decide mirando: si desapareció un trozo de la forma de abajo y la de arriba también, es
restar; si lo que desapareció es justo el solape, es excluir; si lo que queda es sólo el solape, es
intersecar.

Las características de las curvas Bézier son nodo inicial, nodo final, punto de control y palanca de
curva. La regla es que una curva Bézier necesita los dos extremos Y los controles que la doblan, y una
lista sin nodo inicial y final está incompleta. La misma curva gobierna la animación: entre los
modos de interpolación de Blender está **«a free form Bézier mode»** (un modo libre, de curva Bézier;
epígrafe 3 y tema 5).

### Qué se diseña en cada familia (oficio)

- En el vectorial, lo que tiene que escalar sin pérdida: el logotipo, la mosca, los pictogramas, las
  formas de la retícula de rótulos. Una marca se guarda en vectorial y se exporta al tamaño que pida
  cada salida.
- En el de imagen fija, lo que es fotografía o textura: fondos, retoques, recortes de personas para un
  gráfico. Se trabaja en el nativo y se exporta al final.
- En el de composición, lo que se mueve (epígrafe 3).
- En el de 3D, lo que tiene volumen, luz y cámara: decorados, objetos de realidad aumentada, logotipos
  corpóreos (tema 5).

Un logotipo en mapa de bits que hay que ampliar para una pantalla de plató o para un cartel es el
fallo clásico que evita trabajar en la familia correcta desde el principio.

## 3. Composición

### Capas y nodos

Los programas de composición organizan el trabajo de dos maneras (oficio):

| Modelo | Cómo se ve | Ejemplo |
|---|---|---|
| Por capas | Una pila de capas sobre una línea de tiempo; lo de arriba tapa a lo de abajo | After Effects |
| Por nodos | Un diagrama de cajas unidas por cables; cada caja hace una operación y pasa la imagen a la siguiente | Fusion, dentro de DaVinci Resolve |

El manual de Resolve habla de nodos en Fusion: **«The Merge node is the primary tool available for
compositing images together.»** (el nodo *Merge* es la herramienta principal para componer imágenes; cada
uno combina dos entradas), y **«Mask nodes create an image that is used to define transparency in
another image. Unlike other image creation nodes in Fusion, mask nodes create a single channel image rather than a full RGBA
image.»** (los nodos de máscara crean una imagen de un solo canal que define la transparencia de otra,
no una imagen RGBA completa). Las dos maneras hacen lo mismo; la de nodos deja ver el camino de cada
imagen, y la de capas es más directa para piezas cortas (oficio). Qué es una capa y qué es componer,
en el tema 5.

### La línea de tiempo y el orden de las capas

El área de trabajo (*work area*) es la sección de la línea de tiempo para previsualizar o renderizar.
La distinción es que el área de trabajo es un TRAMO DE TIEMPO, marcado con dos asas sobre la línea, y
el espacio de trabajo es la disposición de los paneles en pantalla.

En una composición en la que sólo existen capas de dos dimensiones, la que está en primer término es
la de numeración más baja. Y es la regla que gobierna el orden de apilamiento: la lista de capas se
lee de arriba abajo, la número 1 arriba, y lo de arriba tapa a lo de abajo. En cuanto hay capas de
tres dimensiones, el orden lo decide la posición en el eje de profundidad y no el número.

Las luces virtuales afectan a las capas en tres dimensiones. Una luz es un objeto del espacio, y una
capa plana no está en el espacio. Sólo lo que tiene profundidad puede recibir una luz. La consecuencia
práctica que conviene llevar: si se añade una luz y no pasa nada, lo que falta es activar la tercera
dimensión en las capas.

Para que dos capas trabajen como una sola se seleccionan las dos y se elige «precomponer». Qué hace
precomponer, en una línea: mete las capas elegidas en una composición nueva y deja en su lugar una sola
capa que la contiene. Es la manera de aplicar un efecto al conjunto y no a cada una por separado.

### La máscara y sus parámetros

Los cuatro parámetros de una máscara (oficio):

| Parámetro | Qué controla |
|---|---|
| Trazado | La forma de la máscara |
| Calado | Cuánto se difuminan sus bordes |
| Opacidad | Cuánto tapa |
| Expansión | Cuánto crece o encoge la forma |

El parámetro que permite animar el desenfoque de los bordes es el calado (*mask feather*). La
expansión también modifica el borde: pero lo mueve, no lo difumina. En Fusion la máscara más usada es la de
polígono (**«The most used mask tool, the Polygon mask tool»**), y el manual la tiene por la herramienta de
la rotoscopia: **«Polygon masks are user-created
Bézier shapes. This is the most common type of polyline and the basic workhorse of rotoscoping.»**
(tema 5).

### La interpolación

El proceso de creación de fotogramas intermedios entre dos fotogramas clave se denomina interpolación.
Blender la define como **«The process of calculating new data between points of known value, like
Keyframes.»** (el cálculo de datos nuevos entre puntos de valor conocido, como los fotogramas clave).
Los dos tipos de interpolación que conviene distinguir:

| Tipo | Qué interpola | Se ve en |
|---|---|---|
| Espacial | Por dónde pasa el objeto | La trayectoria en el lienzo |
| Temporal | A qué velocidad recorre esa trayectoria | El editor de gráficos |

Los modos de interpolación (constante, lineal, Bézier) y el suavizado de entrada y salida, en el tema
5.

### El alfa dentro del compositor

Un compositor mezcla imágenes con transparencia, y el manual de Resolve da cuatro reglas para no
estropearlas: **«Always use premultiplied images with a Merge node. / Only color-correct images that
are not premultiplied. / Always filter and transform images that are premultiplied. / Never double
premultiply an image.»** (mezclar siempre con la imagen premultiplicada; corregir el color sólo sobre la
no premultiplicada; filtrar y transformar sobre la premultiplicada; no premultiplicar nunca dos veces).
El fallo que se ve si se mezcla una imagen que no está premultiplicada: **«an unwanted bright
fringe around the edges of your foreground subject»** (un borde claro no deseado alrededor de la figura). Qué es el alfa directo y el
premultiplicado, en los temas 5 y 8.

### Recopilar archivos

Un proyecto de composición no contiene sus imágenes: las enlaza. El comando «recopilar archivos» busca
los archivos usados y crea una copia en una carpeta nueva junto con el proyecto (oficio). La palabra
que decide es COPIA: si los moviera, cualquier otro proyecto que usara esos mismos archivos se
rompería. Un programa serio no mueve lo que no es suyo.

Para qué sirve, que es lo que hay que entender: para llevarse un proyecto a otro equipo con todo lo
que necesita. Es el paso previo a mandar un trabajo fuera, y la causa número uno de que un proyecto
llegue con enlaces rotos es no haberlo hecho. Archivar un proyecto para reutilizarlo pide lo mismo
(tema 12).

## 4. Edición

### El programa de edición y el grafista

El programa de edición es el sitio donde se montan las imágenes, y el grafista no suele operarlo: la
ficha del convenio le da la imagen gráfica **«para programas y postproducciones»** y el asesoramiento
estético a la postproducción, no el montaje (epígrafe 1). Pero su trabajo entra en él por dos puertas
(oficio):

1. Como fichero terminado: una cabecera, una cortinilla o un gráfico animado que el montador coloca en
   su línea de tiempo. Si va encima de la imagen, lleva transparencia.
2. Como plantilla: un rótulo diseñado por grafismo que el montador rellena en su programa, sin
   tocar el diseño (epígrafe 5).

Edición lineal y no lineal (oficio): la lineal copiaba el material de una cinta a otra en el orden
del montaje, y cambiar algo del principio obligaba a rehacer lo que venía detrás; la no lineal trabaja
sobre ficheros en disco, permite ir a cualquier punto y cambiar cualquier plano sin tocar los demás.
Hoy el grafismo se entrega a sistemas no lineales, como ficheros.

### Qué fichero se entrega

El cuadro de los formatos de fichero, con lo que cada uno sirve para el grafismo (oficio):

| Formato | Familia | Transparencia | Para qué se usa |
|---|---|---|---|
| `PSD` | Mapa de bits, nativo | Sí, con capas | Trabajo en curso |
| `AI` | Vectorial, nativo | Sí | Trabajo en curso |
| `TIFF` | Mapa de bits | Sí | Artes gráficas, archivo |
| `PNG` | Mapa de bits | Sí, canal alfa | Web y grafismo sobre fondo |
| `JPG` | Mapa de bits, con pérdida | No | Fotografía |
| `TGA` | Mapa de bits | Sí, canal alfa | Secuencias de fotogramas |
| `GIF` | Mapa de bits, 256 colores | Sí, de un solo valor | Animaciones cortas |
| `SVG` | Vectorial | Sí | Web |
| `EPS` | Vectorial | Según el caso | Intercambio con imprenta |

La regla que este cuadro deja para el examen: si la pregunta habla de transparencia y web, es `PNG`;
si habla de capas, es el nativo; si habla de secuencias de fotogramas renderizados, es `TGA`; si habla
de fotografía comprimida, es `JPG`.

Un fotograma renderizado en formato `TGA` sin compresión ocupa el mismo espacio en bytes en todos los
casos. La razón es la definición misma de «sin compresión»: el tamaño es el número de píxeles por los
bytes de cada píxel, y nada más. Ni el entrelazado ni cuál sea el primer campo cambian cuántos
píxeles hay.

Para una pieza animada con transparencia en un solo fichero de vídeo, Apple fija qué códecs de su
familia sirven: **«Apple ProRes 4444 XQ and Apple ProRes 4444 are ideal for the exchange of motion
graphics media because they are virtually lossless, and are the only ProRes codecs that support alpha
channels.»** (son los únicos ProRes con canal alfa). Ningún ProRes 422 lleva alfa. Los códecs, el alfa
en la entrega, las zonas seguras y el color son el tema 8.

### Cómo se reparten grafismo y montaje (oficio)

- Lo que no cambia de una pieza a otra —cabeceras, cortinillas, fondos, la mosca— se entrega hecho,
  como fichero, en el formato que pida la casa.
- Lo que cambia en cada pieza —el nombre y el cargo de quien habla, el lugar, la fecha— se entrega como
  plantilla, para que lo rellene quien monta o lo lance el control.
- Quién rellena cada rótulo y cuál se incrusta en la pieza o se lanza en directo lo decide la casa, y
  no consta publicado (tema 7).

## 5. Plantillas

### Qué es una plantilla

Una plantilla es un diseño preparado de antemano en el que sólo se cambia lo que cambia de una pieza a
otra —el texto, un dato, una imagen—, para que todas salgan iguales sin rehacerlas (definición de
oficio). Para el grafista es la herramienta de la identidad visual: diseña una vez y el diseño se
repite en miles de rótulos, los rellene quien los rellene.

Qué fija la plantilla y qué deja libre (oficio):

| La plantilla fija | Quien la usa cambia |
|---|---|
| Tipografía, cuerpo, color y posición | El texto |
| Animación de entrada y salida, y su duración | Los datos: cifras, resultados, nombres |
| Márgenes dentro de la zona segura (tema 8) | Una imagen o un logotipo, si se ha previsto su hueco |
| Todo lo demás, cerrado | Sólo los campos que el diseñador abrió |

Hay plantillas en cada eslabón de la cadena (oficio): de rótulo, en el programa de edición; de escena,
en el sistema de grafismo de directo; de salida, con los ajustes de exportación; y de nombre, con las
reglas que componen el nombre de un fichero. Las cuatro persiguen lo mismo: que la imagen de marca,
los formatos de entrega y los nombres no dependan de quién esté trabajando ese día.

### Plantillas de rótulo en el programa de edición

Resolve trae generadores de rótulos con la composición ya resuelta. Tres ejemplos del manual (cap. 56,
p. 1215):

- Los rótulos inferiores (*Lower 3rd*) izquierdo, central y derecho: el central, por ejemplo,
  **«Automatically positions two lines of text at the bottom middle of title safe»**, cada línea con
  sus propios controles de estilo, posición, tamaño y giro. Es la forma del rótulo de identificación
  de un total: dos líneas, nombre y cargo, en la parte baja del cuadro.
- *Text+*: **«An advanced title generator»** con muchas más opciones de estilo y animación, pero en el
  que **«all title text shares a single style»**.
- *Fusion Titles*: **«A variety of pre-built title templates assembled in Fusion. DaVinci Resolve
  comes with a library of pre-assembled Fusion titles, but you can also create your own to appear in
  this category of the Effects browser.»** Es la plantilla propiamente dicha: la casa diseña su rótulo
  una vez y queda en la biblioteca de efectos de cada puesto.

En Premiere la plantilla de rótulo tiene formato propio: **«A Motion Graphics template is a file type
(.mogrt) that can be created in Adobe Premiere or Adobe After Effects.»** Se empaqueta con controles
sencillos pensados para ajustarse en Premiere y sirve para **«titles, lower thirds, and buttons»**; se
gestiona en el panel *Graphics Templates*, y puede llegar desde una carpeta local de plantillas, desde
las bibliotecas de Creative Cloud o desde Adobe Stock (ayuda de Premiere, «Overview of Motion Graphics
templates»). Al instalar un fichero .mogrt, la plantilla queda en la pestaña *My Templates* de ese
panel; se pueden instalar varias a la vez arrastrándolas a esa pestaña, y la que está en una biblioteca
de Creative Cloud **«is automatically available for use in Premiere. It doesn't need to be installed.»**
(«Install Motion Graphics templates»). Se usa arrastrándola a una pista de vídeo de la secuencia y
cambiando después su aspecto en la pestaña *Edit* del panel *Properties*; si pide fuentes que no están
instaladas, se pueden resolver las que faltan («Add Motion Graphic templates to a sequence»). Un gráfico hecho en
Premiere se exporta como plantilla con *Graphics and Titles > Export Motion Graphics template* o con el
botón derecho sobre el clip, pero **«This export feature is only available for graphics created in
Premiere, not for .mogrt files that were originally created in After Effects»**, y la opción no está
disponible si hay dos o más gráficos seleccionados («Export graphic as a Motion Graphics template»).
Hay además plantillas alimentadas por datos, para gráficos de barras, de líneas y otros, que admiten tres
tipos de dato (texto, color y números), fijados por su autor en After Effects y no modificables en
Premiere («Use data-driven Motion Graphics templates»). Todas esas páginas llevan fecha de 7-I-2026.

La otra vía, cuando el rótulo no lo compone el montador, es que lo componga el grafismo desde la
escaleta: el sistema de redacción manda el texto y el generador de caracteres lo pone sobre su propia
plantilla en el momento de la emisión. En iNews, según Manfredi (2010), cuyo ejemplo es el sistema
entonces instalado en Canal Sur, los rótulos que el periodista inserta en su texto **«irán
directamente a la emisión»**. Qué rótulos se incrustan en la pieza y cuáles se lanzan en directo es
decisión de la casa, que no consta publicada (oficio: los que pueden cambiar a última hora, mejor en
directo).

### Hacer la plantilla propia en un compositor

Los rótulos de Resolve son composiciones de su módulo de composición guardadas como macros: **«In
actuality, these text generators are Fusion templates, which are Fusion compositions that have been
turned into macros and come installed with DaVinci Resolve to be used from within the Edit page like
any other generator.»** (cap. 56, p. 1226; los generadores de texto son en realidad plantillas de
Fusion, composiciones convertidas en macros que se usan desde la página de edición como cualquier
generador). Y el grafista puede hacer las suyas: **«It’s possible to make all kinds of Fusion title
compositions in the Fusion page, and save them for use in the Edit page by creating a macro»** (se
compone el rótulo en la página de Fusion y se guarda como macro para usarlo en la de edición).

En el mundo de Adobe, el mismo papel lo hace el fichero .mogrt: se diseña en After Effects y se usa en
Premiere. La herramienta es el panel *Essential Graphics* (gráficos esenciales): **«The Essential
Graphics panel allows you to build custom controls for motion graphics and share them as Motion
Graphics templates via Creative Cloud Libraries or as local files.»** (permite crear controles propios y
compartirlos como plantillas por las bibliotecas de Creative Cloud o como ficheros locales). Se trabaja
en el espacio de trabajo *Essential Graphics*. Los pasos, según la ayuda de After Effects («Work with
Motion Graphics templates», 11-V-2026):

1. Se abre la composición en el panel (*Composition > Open in Essential Graphics*); esa es la
   composición principal (*Primary*). Una propiedad de otra composición que no esté en su jerarquía se
   añade en rojo y no funciona al exportar: hay que anidar esa composición dentro de la principal o de su jerarquía.
2. Se arrastran al panel, desde la línea de tiempo, las propiedades que el montador podrá cambiar
   (también con el botón derecho, *Add Property to Essential Graphics*). **«Only these properties will
   be available for customization to the editors in Premiere.»** Admite, entre otras, casilla, color,
   deslizadores numéricos como la opacidad, el texto (*Source text*), posición, escala y giro. Del texto
   se pueden abrir además la familia y el estilo de la fuente, el cuerpo y los estilos simulados.
3. Se ordenan los controles: se renombran, se reordenan, se agrupan y se añaden comentarios para que
   el montador sepa qué está cambiando. Cada control está enlazado a su propiedad: cambiarlo en el panel
   la cambia en la composición.
4. Se exporta (*Export Motion Graphics Template*) a las bibliotecas de Creative Cloud, a la carpeta
   local de plantillas —**«Templates stored in the Essential Graphics folder are directly available in
   the Essential Graphics panel in Premiere.»**— o a otra carpeta del disco, desde la que no aparece
   sola en Premiere. Se elige el fotograma que servirá de miniatura (*Set Poster Time*) y, si se quiere,
   una vista previa en vídeo.

La ayuda lo resume así: **«Only the controls you expose are available for customization in Premiere,
which allows you to retain creative control of your design.»** (el diseñador conserva el control de su
diseño). Dos cautelas de la misma página. Algunas plantillas exigen tener After Effects instalado para
personalizarlas; para que no haga falta, sólo vale el motor de composición 3D clásico (*Classic 3D*),
no valen los módulos de terceros, el formato FLV ni el material enlazado por *Dynamic Link* (una secuencia de Premiere, por ejemplo), y quedan fuera algunos efectos, entre ellos
*Puppet* y *Warp Stabilizer*. Y la exportación puede avisar de fuentes tipográficas que no estén en
Adobe Fonts, pero sólo avisa: no cambia nada de la plantilla. Un .mogrt se puede volver a abrir en After
Effects como proyecto (*File > Open Project*), corregir y exportar de nuevo.

Las plantillas con datos se preparan en el mismo panel: se importa al proyecto un fichero de valores
separados por comas (CSV) o por tabuladores (TSV), se añade a la composición y se arrastra al panel el
grupo de propiedades de datos de la capa que se ha creado con él; el autor fija el tipo de cada columna, que en Premiere se
ve como texto, número o color, y el número mínimo y máximo de filas. La regla de oficio es la de la
tabla anterior: sólo se abren los campos que deben cambiar.

### Plantillas en el sistema de grafismo de directo

En un control moderno el grafismo informativo se hace con plantillas. Un fabricante de grafismo,
Vizrt, describe así el reparto (*Viz Pilot Edge User Guide*, versión 3.5, «Introduction»). Diseño hace
las plantillas: **«Template Builder is used by design teams to create customized templates via scene
import from Viz Artist, supports scripting (Typescript), and live data integrations.»** (el equipo de
diseño crea las plantillas a partir de las escenas hechas en Viz Artist, con programación y datos en
directo). Redacción las rellena: la herramienta sirve **«to help journalists and producers to
independently create and preview graphics using on-brand, show-aligned templates»** (para que
periodistas y productores creen y previsualicen gráficos con plantillas ajustadas a la marca y al
estilo del programa); **«Fill templates with content and store them as data elements.»**; **«Move data
elements into the newsroom rundown.»** (se rellenan, se guardan como elementos de datos y se colocan en
la escaleta de la redacción). Y el control las emite: **«The template is saved in the Viz Pilot system
and is available to newsroom and control room systems for playout.»**

La misma casa lleva las plantillas a las pantallas del plató: su programa de control de pantallas,
Viz Multiplay, **«Uses Viz Engine for playout»** y **«You are able to access and use templates and
elements from Pilot Data Server.»** (usa las plantillas y elementos del servidor de datos de Viz Pilot;
*Viz Multiplay User Guide* 3.3). Una plantilla, por tanto, no es de un monitor ni de un control: está
en un servidor y la usa quien la necesita.

Chyron llama a sus plantillas *Base Scenes*: **«Base Scenes, our templatized graphics creation
feature, streamlines design workflows. With full access to all the elements of a base scene
(conditions, events, triggers, data-binding, etc.), a designer can make full-package changes in
minutes instead of hours!»** (con acceso a todos los elementos de la escena base —condiciones,
eventos, disparadores, enlace con datos—, el diseñador cambia el paquete entero en minutos). Es la
razón de ser de la plantilla dicha por un fabricante: se cambia el diseño en un sitio y cambian todos
los rótulos que cuelgan de él. Es publicidad del fabricante: vale para decir qué hace el producto, no
para valorarlo.

En Unreal Engine, el grafismo de Motion Design se organiza en una escaleta (*Rundown*) con páginas que
llevan su plantilla: **«The Rundown Server API is used to load the rundown assets and the page’s
templates, and contains an embedded Remote Control Preset (RCP).»** (*Setting Up Rundown Server for
Motion Design*, Unreal Engine 5.8; la interfaz del servidor de escaleta carga la escaleta y las plantillas de
cada página, con un ajuste de control remoto incorporado). Cómo se lanza desde fuera, en el epígrafe
6.

CasparCG es un servidor de emisión de grafismo de programa libre: **«CasparCG Server, a professional
software used to play out and record professional graphics, audio and video to multiple outputs.
CasparCG Server has been in 24/7 broadcast production since 2006.»** (un programa para emitir y
grabar grafismo, audio y vídeo por varias salidas, en producción continua desde 2006). Se controla
desde un programa cliente aparte: **«Connect to the Server from a client software, such as the
"CasparCG Client"»**.

Lo que tienen en común (oficio): el diseñador hace la escena con los campos abiertos; alguien la
rellena, a mano o con datos; y un motor la dibuja en el momento de la emisión. Quién diseña, rellena y
lanza en un informativo es el tema 3; los tres sistemas y su motor, el tema 6.

### Plantillas de salida: los *presets*

Un *preset* de exportación guarda todos los ajustes de salida (formato, códec, resolución, audio,
nombre y destino) con un nombre, y se aplica de un clic.

- En Resolve, se eligen los ajustes y se guarda con *Save as New Preset*; al pulsar un *preset*
  **«Every setting in the Render Settings pane updates to reflect the preset you selected»**. Se pueden
  actualizar y borrar, y también exportar e importar: **«Presets are saved in .xml files that can be
  easily sent to other users or workstations to ensure the exact same delivery methods are used between
  machines.»** Los *presets* nuevos aparecen además en el menú *Add to Render Queue Using* al pulsar
  con el botón derecho sobre una línea de tiempo (cap. 187, pp. 4193-4194).
- En Premiere, al enviar una secuencia a Media Encoder se aplica por defecto el *preset* **«H.264
  Match Source - Adaptive High Bitrate»**, salvo que la secuencia se haya abierto antes en el modo de
  exportación o en la exportación rápida, en cuyo caso **«the last-used export setting is applied
  instead»**; en Media Encoder se puede elegir otro o cambiar los ajustes (ayuda de Premiere, «Export
  directly to Adobe Media Encoder»). La consecuencia práctica: no conviene fiarse de lo que salga por
  defecto; se elige el *preset* de la casa cada vez.

Que el *preset* se pueda mandar a otros puestos es lo que convierte un ajuste personal en una norma
de la sala: todas las cabinas entregan el mismo formato porque cargan el mismo fichero.

Para el grafista, el *preset* es la manera de que toda pieza entregada salga en el formato que pide la
casa (oficio): un *preset* por destino —emisión, redes, pantallas del plató—, con nombre claro, en
todos los puestos del departamento. Los formatos de cada destino son el tema 8; las versiones para
redes, el tema 13.

### Plantillas de nombre: las variables de metadatos

Resolve permite escribir **«metadata variables»** en los campos de texto que las admiten, para que
el programa rellene el nombre con los datos del propio clip. Se escribe el signo de porcentaje (%) y
aparece la lista de variables disponibles. El ejemplo del manual: con las variables de escena, plano y
toma separadas por guiones bajos, un clip con escena «12», plano «A» y toma «3» se muestra como
«12_A_3». Si el campo de origen está vacío, en su lugar no aparece nada (cap. 15, p. 345).

Dónde se pueden usar, según el manual, entre otros sitios: en el nombre de los clips del *Media Pool*;
en otros campos del editor de metadatos; en el rótulo automático de las imágenes fijas de la galería;
en el texto sobreimpreso de la paleta *Data Burn*; y en el nombre de fichero de los ajustes de *render*
de la página *Deliver*, **«especially useful when you want to generate specific file names when
rendering individual source clips»** (p. 345). Hay además variables de fecha y hora (%date, %time) que
toman **«the actual date and time as of the output, rather than the date and time a clip was shot»**
(p. 346).

La aplicación al grafismo (oficio): si la casa fija una regla de nombres para los ficheros gráficos,
una variable la aplica sin errores de tecleo. La catalogación y la reutilización de plantillas y
proyectos son el tema 12.

## 6. Automatización gráfica

### Qué es automatizar el grafismo

Automatizar es que una tarea repetida la haga el programa, a partir de una regla o de un dato, en vez
de hacerla una persona cada vez (definición de oficio). En grafismo hay cuatro niveles (oficio):

| Nivel | Qué se automatiza | Con qué |
|---|---|---|
| Dentro de una pieza | Que un parámetro siga a otro o se calcule | Expresiones |
| En el programa | Tareas repetidas: generar versiones, ordenar, exportar | *Scripts* |
| En el contenido | Que la plantilla se rellene sola | Fuentes de datos y escaleta de la redacción |
| En la salida | Que el grafismo se exporte o se emita sin intervención | Colas de *render*, carpetas vigiladas, automatización de emisión |

### Las expresiones

Una expresión es una pequeña fórmula escrita sobre un parámetro. De las más sencillas, las *Simple
Expressions* de Fusion, Blackmagic dice que son **«a special type of script that can be placed
alongside the parameter it is controlling. These are useful for setting simple calculations, building
unidirectional parameter connections, or a combination of both.»** (cap. 73, p. 1634; un pequeño guion
junto al parámetro, para cálculos sencillos o para que un parámetro siga a otro).

El ejemplo clásico es la expresión de movimiento aleatorio (*wiggle*), que suele llamarse efecto
aunque es, en rigor, una expresión y no un efecto: se escribe sobre una propiedad y le añade una
oscilación al azar, con dos números: cuántas veces por segundo y cuánto (oficio).

### Los *scripts*

Un *script* es un programa corto que maneja el programa de diseño desde dentro. El manual de Resolve
dice para qué: **«Scripting is an essential means of increasing productivity. Scripts can create new
capabilities or automate repetitive tasks, especially those specific to your projects and workflows.
Inside Fusion, scripts can rearrange nodes in a comp, manage caches, and generate multiple output
files for delivery.»** (cap. 73, p. 1640; los *scripts* crean funciones nuevas o automatizan tareas
repetitivas; en Fusion pueden reordenar nodos, gestionar cachés y generar varios ficheros de salida
para la entrega). Y en qué lenguajes: **«FusionScript is the blanket term for the scripting
environment in Fusion. It includes support for Lua as well as Python 2 and 3 for some contexts.»**
(FusionScript es el entorno de *scripts* de Fusion, con Lua y, en algunos contextos, Python 2 y 3).

Sin escribir código también se automatiza. En Photoshop, una acción es **«a sequence of recorded
tasks, such as menu commands, tool operations, and panel adjustments, that you can play back on a
single file or across multiple files.»** (una serie de pasos grabados —órdenes de menú, herramientas,
ajustes de panel— que se reproduce sobre un fichero o sobre muchos; «Overview of Actions», 18-VIII-2026).
Para muchos está el procesamiento por lotes: **«The Batch command automates repetitive editing by running
an action on groups of files.»** (*File > Automate > Batch*: se elige la acción, el origen —por ejemplo, una
carpeta, con sus subcarpetas si se quiere, o los ficheros abiertos— y el destino: dejarlos abiertos,
guardar y cerrar sobrescribiendo los originales, o guardar en otra carpeta; «Batch-process files»,
23-II-2026). Y una acción se puede convertir en un icono (*droplet*, *File > Automate > Create
Droplet*): se arrastra un fichero o una carpeta sobre él y la acción se ejecuta («Create a droplet from
an action», 23-II-2026). Oficio: antes de lanzar un lote que guarda sobre los originales, copia de
seguridad.

Fuera del módulo de composición, el programa entero se puede integrar con otros:

- **Integraciones por *scripts*.** En la versión Studio, Resolve permite que terceros creen módulos
  de interfaz propios **«using scripting languages»**, y el usuario puede escribir su propio
  *Workflow Integration Plugin* **«(an Electron app), using Resolve Javascript's API, and Python or Lua
  scripts»** (cap. 201, p. 4418).

En los sistemas de directo la programación va en la plantilla. El Template Builder de Vizrt **«supports
scripting (Typescript), and live data integrations»** (admite programación en TypeScript e integración
de datos en directo; epígrafe 5). Y en Unreal Engine se programa sin escribir código: los *blueprints*
son el sistema de programación visual de ese motor, en el que se programa uniendo nodos con cables en
vez de escribiendo código (oficio).

Lo que eso pide al grafista (oficio): leer y retocar un *script* o una expresión, no ser programador.
La regla es la de cualquier automatización: se prueba con un caso conocido antes de lanzarla sobre
cien.

### Los datos rellenan la plantilla

La automatización que más se ve en antena es la plantilla que se rellena sola con datos: resultados
deportivos, escrutinio electoral, meteorología, bolsa. Tres ejemplos documentados:

- Chyron: **«Logic-based scenes function as editable templates that designers can configure to
  refresh up-to-the-second based on data feeds and trigger controls.»** (escenas con lógica que
  funcionan como plantillas editables y se actualizan al segundo con fuentes de datos y disparadores).
  Su versión 5.3 añadió además contenido web dentro del grafismo: **«PRIME 5.3 delivers the first
  official integration of HTML content within PRIME, through a powerful and flexible HTML Input.»**
- Unreal Engine: Motion Design sirve, según su guía de inicio, para **«graphics creation, playout, and
  real-time data visualization for live television, news, weather, sports production, interstitial
  graphics»** (creación, emisión y visualización de datos en tiempo real para televisión en directo,
  informativos, meteorología, deportes y piezas de continuidad).
- Adobe: las plantillas .mogrt alimentadas por datos del epígrafe 5, que admiten texto, color y
  números.
- Photoshop, para imagen fija: variables y conjuntos de datos. Las variables marcan qué cambia en la
  plantilla, y son de tres tipos: **«Visibility Variable shows or hides the contents of a layer. Text
  Replacement variables replace a string of text in a type layer. Pixel Replacement variables replace
  the pixels in the layer with pixels from another image file.»** (de visibilidad, que muestra u oculta
  una capa; de sustitución de texto, en una capa de texto; y de sustitución de píxeles, que cambia la
  imagen de la capa por otra). No se pueden definir en la capa de fondo. **«A data set is a collection
  of variables and associated data»**: un conjunto por cada versión que se quiere sacar. Los conjuntos
  se pueden importar de un fichero de texto separado por comas o tabuladores, con los nombres de las
  variables en la primera línea y un conjunto por línea; todas las variables del documento tienen que
  estar en el fichero. Las variables se definen en *Image > Variables > Define*; los conjuntos se crean en
  *Image > Variables > Data Sets*, y la importación, en *File > Import > Variable Data Sets*. Se revisa cada versión con la vista
  previa y se generan con *File > Export > Data Sets As Files*, que saca un PSD por conjunto (ayuda de
  Photoshop, «Create data-driven graphics», 24-V-2023). Ojo: aplicar un conjunto al documento
  (*Apply*) sobrescribe el original.

Qué se diseña distinto cuando el dato entra solo (oficio): la plantilla tiene que aguantar el dato más
largo y el más corto —el nombre de municipio más largo de Andalucía, una cifra de siete dígitos, un
cero—; tiene que decir qué muestra cuando el dato no llega; y tiene que dejar un camino para teclearlo
a mano si la fuente falla. La visualización de datos y su rigor son el tema 4; la noche electoral, el
tema 3.

### La escaleta manda: el protocolo MOS

El otro dato que rellena plantillas es el texto de la redacción. En un informativo, el rótulo se
escribe en la escaleta del sistema de redacción y llega de ahí al grafismo, sin teclearlo dos veces
(oficio). Uno de los enlaces entre la redacción y los equipos, con especificación publicada, es MOS.

La web del proyecto MOS lo define así: **«Media Object Server Communications Protocol (MOS): An
evolving protocol for communications between Newsroom Computer Systems (NCS) and Media Object Servers
(MOS) such as Video Servers, Audio Servers, Still Stores, and Character Generators.»** Es decir, un
protocolo, en evolución, para que el sistema de redacción hable con los servidores de objetos de medios:
servidores de vídeo, de audio, almacenes de imágenes fijas y generadores de caracteres. Su finalidad,
en la misma fuente: **«allows integration of diverse NCS and MOS equipment»**.

Lo que hay que saber de él (portada, «Current Versions» y FAQ de mosprotocol.com):

- **El reparto de papeles.** En general (**«In General»**, dice la FAQ), **«the Newsroom Computer System is responsible for the creation,
  modification, and deletion of editorial information, including playlists»**; **«the Media Object
  Server is responsible for the creation, modification, and deletion of media objects and their
  associated meta-data»**. La redacción manda en el orden y en el texto; el servidor, en el material y
  sus datos.
- **Los tres tipos de mensajes.** *Descriptive Data for Media Objects*: el servidor **«"pushes"
  descriptive information and pointers to the NCS as objects are created, modified, or deleted»**, de
  modo que la redacción sabe qué hay en él y puede buscarlo. *Playlist Exchange*: la redacción construye
  y envía la lista de reproducción al servidor, lo que **«allows the NCS to control the sequence that
  media objects are played or presented by the MOS»**. *Status Exchange*: el servidor informa a la
  redacción del estado de cada clip o de todo el sistema, y la redacción informa al servidor del estado
  de los elementos de la lista o de los órdenes de emisión (*running orders*).
- **Cómo viaja.** Entre sus objetivos: **«Common implementation of the protocol will be over a TCP/IP
  network via socket communication»**; los mensajes **«will make use of a tagged text unicode format»**;
  y **«Each new version of the protocol will be a "super set" of the previous version»**, para que una
  máquina antigua siga hablando con una nueva con un vocabulario más reducido.
- **Versiones vigentes.** La página de versiones actuales da tres: **«MOS Version 4.0 was published on
  June 7th, 2019»** (*Secure Web Sockets*); **«MOS Version 2.8.5 was published on September 7, 2017»**
  (*Socket*); y **«MOS Version 3.8.4 was published on February 11, 2011»** (*Web Services*).
- **No es una norma oficial.** La FAQ dice que el protocolo **«will be presented to appropriate
  standards bodies at a later date»**, y que su desarrollo no se frenará a la espera de **«the official
  "blessing" of a standards body»**. No es, por tanto, una norma de la SMPTE, de la EBU ni de otro
  organismo de normalización: es un protocolo de la industria con especificación pública.

Los sistemas de grafismo lo usan: Viz Multiplay **«Can open and control newsroom playlists in a MOS
workflow.»**, y Chyron dice que **«For pre-planned productions, PRIME CG integrates with all leading
newsroom computer systems via Chyron CAMIO.»** Para el grafista, la consecuencia es de diseño (oficio):
la plantilla que va a rellenar la redacción se diseña para el texto que escribe un periodista con
prisa, no para el que queda bien en la maqueta.

### La emisión automatizada del grafismo

El último nivel es que el grafismo salga al aire sin que nadie lo dispare a mano, o gobernado desde
otro equipo. Tres ejemplos documentados:

- Chyron tiene un modo para emisión automatizada: con él, **«news broadcasters can utilize the Playout
  Automation mode to dedicate all PRIME Engine performance to set-and-forget automated playout.»**
  (el motor dedica todo su rendimiento a una emisión automatizada que se programa y se deja correr;
  nota de PRIME 5.3).
- Unreal Engine separa escaleta y control remoto: **«Controlling the Motion Design playout can be
  accomplished by combining two APIs.»**; la página de la escaleta se puede modificar desde fuera:
  **«The RCP for the corresponding page can be accessed and modified via the Remote Control API, then
  saved back in the rundown page for immediate or later playout.»**, y la interfaz de la escaleta se
  expone en red: **«The Rundown Server API is exposed to WebSocket through the WebSocket Messaging
  bridge plugin.»** (misma página de la documentación de Unreal Engine citada en el epígrafe 5).
- Vizrt separa el motor que dibuja del programa que lo gobierna: **«use an external application (for
  example, Viz Trio or Viz Pilot) to control the Viz Engine.»** (*Viz Engine Administrator Guide* 5.2,
  «Dual Channel Mode»).

Leído en términos de oficio: escaleta, páginas con plantilla y control remoto por red son el mismo
esquema en los tres —diseño, relleno y lanzamiento separados—, y es lo que permite que el grafismo lo
dispare una automatización, un operador o la propia escaleta.

### Automatizar la salida

En la entrega de piezas cerradas lo que se automatiza es la exportación:

- **Cola de *render*.** En la página *Deliver* de Resolve se definen los ajustes de salida, se elige
  qué se va a exportar y se añade un trabajo a la cola: **«You can queue up as many different render
  jobs as you like, each with different formats, output options, and ranges of clips»**; al final se
  pulsa *Start Render* (cap. 187, p. 4185). En Premiere, la cola la lleva Adobe Media Encoder, que
  **«lets you queue multiple exports, use custom presets, and render files without interrupting your
  editing workflow»**, y Adobe lo recomienda **«for longer exports or when you need to create multiple
  delivery versions»** (ayuda de Premiere, «Export directly to Adobe Media Encoder»).

Una carpeta vigilada es una carpeta que un programa observa y cuyo contenido procesa en cuanto entra:
el ejemplo documentado es el generador de copias ligeras (*proxies*) de Blackmagic, Blackmagic Proxy
Generator, que transcodifica **«without any additional human interaction needed»** lo que cae en ella
(oficio en lo general; la cita, del manual de Resolve, cap. 8, p. 215).

Lo que la automatización no hace, como oficio: no mira el contenido. Una carpeta vigilada transcodifica
cualquier fichero que caiga en ella, sea el bueno o no; una cola de *render* exporta la secuencia que se
le dio aunque sea la versión equivocada; la emisión automatizada lanza la pieza que responde al nombre
aunque dentro esté otra. Por eso lo automatizado se revisa al final: se abre el fichero exportado, se
comprueba el nombre y la duración, y se mira el principio y el final antes de darlo por entregado.

Para el grafista (oficio): una plantilla con un dato mal enlazado saca el rótulo equivocado con toda
la corrección técnica, y una fuente de datos caída deja un hueco en la pantalla. Lo automático se
ensaya, se revisa y tiene siempre un camino manual.
## Aplicación práctica

### El rótulo de identificación de un informativo

Encargo: el rótulo de nombre y cargo de todos los totales de un informativo (oficio, salvo lo que se
cita).

1. Diseño en el programa vectorial la caja y los elementos de marca, para que escalen sin pérdida; la
   tipografía, la de la identidad del canal (tema 2).
2. Monto la animación de entrada y salida en el programa de composición o en el editor de escenas del
   sistema de directo, con la caja dentro de la zona segura de título (tema 8).
3. La convierto en plantilla: dos campos de texto abiertos, nombre y cargo; todo lo demás, cerrado.
   Pruebo el nombre más largo que pueda darse y un cargo de dos líneas.
4. Si el rótulo se lanza en directo, la plantilla va al sistema de grafismo y la redacción la rellena
   desde la escaleta; si se incrusta en la pieza, va como plantilla al programa de edición (Fusion
   Titles o .mogrt). En los dos casos el texto se teclea una vez.
5. Compruebo en el mezclador, o en el visor de alfa del programa, que la transparencia es la buena: sin
   borde claro ni fondo negro pegado.

### Una cabecera de programa con transparencia

1. Logotipo en vectorial; texturas en imagen fija; animación en el compositor; si hay volumen, en 3D,
   renderizado en diferido.
2. Composición: se mezcla con la imagen premultiplicada, se corrige el color sobre la directa y no se
   premultiplica dos veces (reglas del manual de Resolve, epígrafe 3).
3. Entrega: si va sobre imagen, en un fichero que lleve alfa —ProRes 4444 o 4444 XQ, o una secuencia
   PNG o TGA—, nunca en JPG ni en ProRes 422. Con un *preset* de la casa y un nombre compuesto por
   variables.
4. Antes de mandarla fuera, se recopilan los archivos del proyecto; y se revisa lo exportado: nombre,
   duración, principio y final.

### El grafismo de datos de una noche electoral

1. Plantillas de escaños, porcentajes y mapas con los campos enlazados a la fuente de datos del
   escrutinio (Chyron las llama escenas con lógica que se actualizan al segundo; Unreal Engine, en su
   Motion Design, habla de visualización de datos en tiempo real).
2. Prueba de límites: el partido de nombre más largo, un cero, un empate, un municipio sin datos.
3. Camino manual: si la fuente cae, el dato se teclea. Una plantilla sin ese camino deja la pantalla
   en blanco.
4. Ensayo con datos de prueba antes de la noche. Los datos, su fuente y su rigor, en los temas 3 y 4.

### Cuarenta versiones de una misma pieza

Encargo: la promoción de un programa en cuarenta versiones —horarios, días, formatos para antena y
para redes (oficio).

- Una plantilla con los campos que cambian (día, hora, formato) en lugar de cuarenta proyectos.
- Un *script* o la plantilla de datos para generarlas: el manual de Fusion dice que los *scripts*
  pueden **«generate multiple output files for delivery»** (epígrafe 6). Si son carteles fijos, las
  variables y los conjuntos de datos de Photoshop, con un fichero de texto de cuarenta y una líneas (la de los nombres de las variables y una por versión); y una
  acción pasada por lotes para sacar cada formato.
- Un *preset* por destino y una regla de nombre con variables, para que cada fichero salga con su
  nombre y su formato.
- Revisión al final: la automatización no mira el contenido. Se abren al azar varias versiones y se
  comprueba el dato que cambia en cada una.

## Lo que este tema no da, y dónde está

- Qué programas, qué sistema de grafismo, qué servidor de emisión y qué sistema de redacción usa hoy
  CSRTV: no consta en documento publicado leído. El dato de iNews, de Avid, en Canal Sur es de 2010. Los
  productos citados son ejemplos.
- De la documentación de Adobe, las expresiones de After Effects, la automatización de Illustrator y
  los *scripts* de Photoshop: no se han leído. Sí se da lo que dice la ayuda sobre el panel *Essential
  Graphics* de After Effects y sobre las variables, las acciones y el procesamiento por lotes de
  Photoshop.
- Cinema 4D, Maya, Houdini, Nuke, Brainstorm, Ross XPression, Ventuz y otros programas de diseño, 3D o
  tiempo real: no se ha leído su documentación. Que las plantillas de CasparCG sean páginas web y qué
  televisión lo creó: no leído; no se afirma.
- Cifras de límites de un programa concreto (tamaño máximo de un fichero nativo, número máximo de
  canales o de píxeles de una composición): dependen del programa y de la versión, no se han leído en
  su documentación y el tema no las da.
- El equipo físico del puesto (estación de trabajo, tarjeta gráfica, monitores de referencia): sin
  fuente leída sobre lo que pide un programa concreto; el doble canal de Vizrt con dos tarjetas
  gráficas, en el tema 6.
- La tabla de familias de programa, la de formatos de fichero, las funciones de los programas de imagen
  fija, vectorial y de composición, la distinción entre edición lineal y no lineal y el reparto entre
  grafismo y montaje: oficio, sin norma.
- Otras materias: diseño para televisión, radio visual y redes, tema 1; identidad visual y tipografía,
  tema 2; quién diseña, rellena y lanza por género, tema 3; visualización de datos, tema 4; animación,
  composición, rotoscopia y tracking, tema 5; sistemas de grafismo en tiempo real, motores, pantallas y
  videowalls, tema 6; flujos con realización y edición, tema 7; formatos de entrega, códecs, alfa,
  zonas seguras y color, tema 8; archivo y reutilización de plantillas y proyectos, tema 12; redes,
  tema 13; inteligencia artificial generativa, tema 15; colaboración en directo, tema 17; pantallas de visualización de
  datos y ergonomía del puesto, tema 18.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| X Convenio Colectivo de la RTVA y sociedades filiales (BOJA núm. 240, de 10-XII-2014), anexo III, ficha 5345100 Grafista (p. 129) | Función básica y tareas del Grafista | Texto tomado de los temas cerrados del puesto de Realizador/a (tema 4) |
| Antonio Manfredi Díaz, «Escribir para televisión. La imagen manda», en R. Reig García (ed.), *La dinámica periodística: perspectiva, contexto, métodos y técnicas*, Sevilla, Asociación Universitaria Comunicación y Cultura, 2010, pp. 129-145 | iNews de Avid en Canal Sur (2010); rótulos que van directamente a la emisión | Texto tomado del tema cerrado 13 de Operador/a Montador/a de Vídeo |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual* (julio de 2026): cap. 1 (p. 13), cap. 8 (p. 215), cap. 15 (pp. 345-346), cap. 56 (pp. 1215 y 1226), cap. 66 (p. 1449), cap. 73 (pp. 1634 y 1640), cap. 77 (p. 1728), cap. 79 (p. 1775), cap. 139 (p. 3339), cap. 187 (pp. 4185, 4193-4194 y 4215), cap. 201 (p. 4418) | Integración de edición, composición y color; nodos de máscara y *Merge*; reglas del premultiplicado; máscara de polígono; Magic Mask v2 y *render* remoto sólo en Studio; plantillas de rótulo y macros de Fusion; expresiones simples; FusionScript; variables de metadatos; cola de *render*; *presets*; carpetas vigiladas; integraciones por *scripts* | 29-09-2026; los pasajes de los caps. 8, 15, 56 (p. 1215), 187 y 201, tomados del tema cerrado 13 de Operador/a Montador/a de Vídeo (leídos allí el 25-09-2026) |
| Adobe, ayuda de Premiere (helpx.adobe.com, páginas de 7-I-2026): «Overview of Motion Graphics templates», «Install Motion Graphics templates», «Add Motion Graphic templates to a sequence», «Export graphic as a Motion Graphics template», «Use data-driven Motion Graphics templates», «Export directly to Adobe Media Encoder» | Plantillas .mogrt, plantillas con datos, cola y *preset* de Media Encoder | Texto tomado del tema cerrado 13 de Operador/a Montador/a de Vídeo (leídas allí el 25-09-2026) |
| Adobe, ayuda de After Effects (helpx.adobe.com): «Work with Motion Graphics templates» (11-V-2026) | Panel *Essential Graphics*: composición principal, propiedades admitidas, controles, exportación, requisitos, plantillas con datos CSV y TSV | 29-09-2026 |
| Adobe, ayuda de Photoshop (helpx.adobe.com): «Create data-driven graphics» (24-V-2023), «Overview of Actions» (18-VIII-2026), «Batch-process files» y «Create a droplet from an action» (23-II-2026) | Variables y conjuntos de datos; acciones; procesamiento por lotes; *droplets* | 29-09-2026 |
| Blender Foundation, *Blender 5.2 LTS Manual*: «Glossary» y «Keyframes › Introduction» | *Render*, trazado de rayos, interpolación, modo Bézier | 29-09-2026 |
| Apple, *Apple ProRes* (white paper, abril de 2022) | ProRes 4444 y 4444 XQ, únicos ProRes con alfa | 29-09-2026 |
| Vizrt, *Viz Pilot Edge User Guide* 3.5, «Introduction» | Template Builder, relleno por la redacción y emisión de plantillas | Texto tomado del tema cerrado 12 de Realizador/a |
| Vizrt, *Viz Multiplay User Guide* 3.3, «Introduction»; *Viz Engine Administrator Guide* 5.2, «Dual Channel Mode»; *Introduction to Viz Artist* 5.3 | Plantillas desde Pilot Data Server, MOS, emisión por Viz Engine; control externo del motor; licencia por llave física | 29-09-2026 |
| Chyron, *PRIME CG™ - 3D Real-Time Graphics* (chyron.com); nota de prensa *Chyron Merges Live Web Content and CG Graphics with PRIME 5.3* (12-II-2026) | Base Scenes, escenas con datos, CAMIO, HTML Input, Playout Automation | 29-09-2026 |
| Epic Games, documentación de Unreal Engine 5.8: *Motion Design Quickstart Guide in Unreal Engine* y *Setting Up Rundown Server for Motion Design in Unreal Engine* | Motion Design como módulo de emisión y de datos en tiempo real; Rundown Server API, Remote Control API y WebSocket | 29-09-2026 |
| CasparCG Server, página de presentación (README) del repositorio oficial en GitHub | Qué es, en producción desde 2006, licencia GPLv3, cliente aparte | 29-09-2026 |
| MOS Project, mosprotocol.com: portada, «Current Versions» y «MOS FAQ» | Definición de MOS, reparto NCS/MOS, tres tipos de mensajes, objetivos, versiones vigentes, carácter no oficial | Texto tomado del tema cerrado 13 de Operador/a Montador/a de Vídeo (leídas allí el 25-09-2026) |

La fecha de trabajo del encargo es el 24-09-2026; las fuentes nuevas se leyeron el 29-09-2026, fecha
del sistema.

Va como oficio, y así se declara en el texto: la lectura del enunciado en dos mitades; la tabla de
familias de programa y lo que se diseña en cada una; la ampliación sin pérdida de lo vectorial; los
cuadros de diferido y tiempo real y de programas de tiempo real, y los *blueprints*; la consecuencia
práctica de las licencias; las funciones del programa de imagen fija (trazado, canales, formatos que
conservan capas o admiten CMYK), del vectorial (calco, buscatrazos, curvas Bézier) y del compositor
(capas y nodos, área de trabajo, orden de apilamiento, luces, precomposición, parámetros de la
máscara, tipos de interpolación, recopilar archivos); la edición lineal y no lineal, las dos puertas
del grafismo al montaje y el reparto entre fichero y plantilla; el cuadro de formatos de fichero y el
tamaño del TGA sin compresión; la definición de plantilla y lo que fija; la definición de
automatización y sus cuatro niveles; la expresión de movimiento aleatorio; la copia de seguridad antes de un lote; el diseño para datos y el
camino manual; los límites de la automatización; y los pasos de la aplicación práctica que no llevan
fuente.
