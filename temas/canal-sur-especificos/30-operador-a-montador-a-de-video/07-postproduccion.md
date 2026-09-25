# Tema 7 del específico de Operador/a Montador/a de Vídeo · Postproducción

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Montador/a de Vídeo · punto 7 |
| Sirve para | Operador/a Montador/a de Vídeo de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Una norma, sólo para la frecuencia de la red eléctrica: Reglamento electrotécnico para baja tensión (Real Decreto 842/2002, de 2 de agosto), art. 4.4. Recomendaciones técnicas: UIT-R, Informe BT.2408-9 (grafismo en alto rango dinámico) y EBU R 128-2023 (sonoridad). Documentación de fabricante: Blackmagic Design (*DaVinci Resolve 21 Reference Manual*), Adobe (ayuda de Premiere, 2026), Rane (RaneNotes) e iZotope (*RX 11*). Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía (2004). Para los subtítulos, síntesis de la norma UNE 153010 publicada por la Universidad de Burgos (la norma no se ha leído). Lo demás, oficio declarado como tal |
| Redacción que se estudia | La vigente el 24-09-2026: Informe UIT-R BT.2408-9 (03/2026) y art. 4 del Reglamento electrotécnico para baja tensión (redacción única, vigente desde el 18-09-2003), leídos el 25-09-2026; EBU R 128-2023 (versión 5) y EBU Tech 3343-2023 (versión 4), leídas el 24-09-2026 para los temas cerrados de Operador/a de Sonido de los que se copian; el temario no nombra programa de edición y la ficha del puesto tampoco |
| Extensión | 13.500 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Unión Internacional de Telecomunicaciones (UIT) y su sector de
radiocomunicaciones (UIT-R, en inglés ITU-R); Unión Europea de Radiodifusión (UER, en inglés EBU,
*European Broadcasting Union*), que publica recomendaciones (R) y documentos técnicos (Tech); los
tres primarios rojo, verde y azul (RGB); la luminancia (Y) y las diferencias de color (Cb y Cr, que
Blackmagic escribe CB y CR); YRGB, la luminancia más los tres primarios, como la escribe Blackmagic;
la tabla de consulta (LUT, *look-up table*); el formato de LUT común (CLF, *Common LUT Format*) y el
lenguaje de transformación de color de Resolve (DCTL, *DaVinci Color Transform Language*); matiz,
saturación y luminosidad (HSL, *hue, saturation, luminance*); alto rango dinámico (HDR, *high dynamic
range*), con sus dos curvas, la híbrida logarítmica-gamma (HLG, *hybrid log-gamma*) y la de
cuantificación perceptual (PQ, *perceptual quantizer*), y rango dinámico estándar (SDR); candela por
metro cuadrado (cd/m²); los formatos gráficos JPG o JPEG (*Joint Photographic Experts Group*), PNG
(*portable network graphics*), TIF o TIFF (*tagged image file format*) y TGA (*Truevision Advanced
Raster Graphics Adapter*); los formatos de subtítulos SRT (*SubRip Text*), WebVTT (*Web Video Text
Tracks*), IMSC1 (*Internet Media Subtitles and Captions*, versión 1) y DFXP (*Distribution Format
Exchange Profile*), y los subtítulos cerrados CEA-608 y CEA-708 (así los nombra Blackmagic); el formato de intercambio de material (MXF, *Material eXchange Format*) y el formato maestro
interoperable (IMF, *Interoperable Master Format*); la Society of Motion Picture and Television
Engineers (SMPTE); la Recomendación UIT-R BT.709, que el oficio llama Rec. 709; UNE, la sigla
que llevan las normas que la guía de la Universidad de Burgos cita como publicadas por AENOR
(la guía no desarrolla ninguna de las dos siglas); decibelio (dB); decibelios referidos a la
escala completa digital (dBFS); decibelios de pico verdadero (dBTP, *decibels true peak*); unidades
de sonoridad referidas a la escala completa (LUFS, *loudness units relative to full scale*) y unidad
de sonoridad (LU, *loudness unit*); rango o margen de sonoridad (LRA, *loudness range*); relación señal-ruido (SNR, *signal-to-noise ratio*); voz en off
(VO, *voice-over*, como la escribe Blackmagic); efectos de sonido (SFX, como los escribe Adobe);
calefacción, ventilación y aire acondicionado (HVAC, *heating, ventilation and air conditioning*),
en una cita de iZotope; inteligencia artificial (IA).
Los nombres de órdenes, ventanas y complementos se dan con su rótulo inglés, en cursiva la primera
vez: *lift*, *gamma* y *gain* (sombras, medios tonos y altas luces); *key* (recorte), *fill* (relleno)
y *background* (fondo); *keyframe* (fotograma clave); *handles* (colas o márgenes de un clip);
*ducking* (atenuación de una pista por otra); *de-esser* (reductor de sibilantes); *hum* (zumbido).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.30, punto 7): «Postproducción: color
> básico, corrección, efectos, grafismo, subtítulos, transiciones y limpieza de audio.»

Qué se puede preguntar: qué es etalonar y qué fases tiene; qué hace una LUT, qué diferencia una 1D de
una 3D y una técnica de una creativa, y qué pasa con los valores fuera de rango; qué muestran el
monitor de forma de onda, el desfile (*parade*) y el vectorscopio, y cómo se lee en ellos una
dominante; qué zonas tonales gobiernan *lift*, *gamma* y *gain*; qué hacen los mandos de temperatura
y matiz; qué distingue la corrección primaria de la secundaria y qué son una ventana y un
cualificador HSL; qué es el «color de memoria»; qué es una incrustación, qué familias hay, por qué el
fondo es verde o azul y cuántas señales intervienen; qué es el canal alfa y qué formato gráfico no lo
tiene; cuántos bits tiene un TGA con alfa; qué es un fotograma clave y qué hace la curva de velocidad;
cómo se hace una cámara lenta, un congelado o una marcha atrás y qué diferencia la repetición de
cuadros, la mezcla y el flujo óptico;
qué efectos de edición limita el Libro de Estilo en informativos; a qué nivel se inserta el grafismo
en un programa HDR; qué son las zonas de seguridad de acción y de título; qué distingue un subtítulo
abierto de uno cerrado, en qué formatos se entrega y cuántos caracteres por línea y por segundo da la
síntesis de la UNE 153010, y qué colores, cursivas y mayúsculas recomienda; qué son las colas y qué pasa si no las hay al poner una transición; qué
distingue un fundido lineal de uno logarítmico; qué filtro quita un zumbido y cuál los graves; qué
hacen un reductor de ruido, un *de-esser*, un nivelador de diálogos y un *ducker*; qué artefactos deja
una limpieza excesiva; en qué orden se limpia un diálogo; y qué sonoridad y qué pico verdadero ha de
cumplir la pieza terminada. En la prueba práctica: corregir e igualar los planos de una pieza,
incrustar un rótulo o un croma, poner una transición sin colas suficientes, limpiar un total con
ruido y zumbido, bajar la música bajo la locución y entregar la pieza dentro de la R 128.

<!-- indice -->

## Índice

- [La postproducción en la sala de montaje](#la-postproducción-en-la-sala-de-montaje)
- [1. Color básico](#1-color-básico)
  - [Qué es etalonar](#qué-es-etalonar)
  - [Medir antes de tocar: los monitores de señal](#medir-antes-de-tocar-los-monitores-de-señal)
  - [Las LUT](#las-lut)
- [2. Corrección](#2-corrección)
  - [Primaria y secundaria](#primaria-y-secundaria)
  - [*Lift*, *gamma* y *gain*](#lift-gamma-y-gain)
  - [Temperatura, matiz, contraste y saturación](#temperatura-matiz-contraste-y-saturación)
  - [La corrección secundaria: ventanas y cualificadores](#la-corrección-secundaria-ventanas-y-cualificadores)
  - [Igualar los planos](#igualar-los-planos)
  - [Lo que no se corrige](#lo-que-no-se-corrige)
- [3. Efectos](#3-efectos)
  - [Qué es un efecto en el sistema de edición](#qué-es-un-efecto-en-el-sistema-de-edición)
  - [Incrustar](#incrustar)
  - [Las tres señales de una incrustación](#las-tres-señales-de-una-incrustación)
  - [El canal alfa](#el-canal-alfa)
  - [La máscara](#la-máscara)
  - [Fotogramas clave y curva de velocidad](#fotogramas-clave-y-curva-de-velocidad)
  - [Los efectos de tiempo](#los-efectos-de-tiempo)
  - [Los efectos y la información](#los-efectos-y-la-información)
- [4. Grafismo](#4-grafismo)
  - [Quién hace qué](#quién-hace-qué)
  - [Títulos y rótulos en el sistema de edición](#títulos-y-rótulos-en-el-sistema-de-edición)
  - [Las zonas de seguridad](#las-zonas-de-seguridad)
  - [Los ficheros gráficos](#los-ficheros-gráficos)
  - [El grafismo en alto rango dinámico](#el-grafismo-en-alto-rango-dinámico)
  - [Lo que pide el Libro de Estilo](#lo-que-pide-el-libro-de-estilo)
- [5. Subtítulos](#5-subtítulos)
  - [Abiertos y cerrados](#abiertos-y-cerrados)
  - [Cómo se hacen y cómo se entregan](#cómo-se-hacen-y-cómo-se-entregan)
  - [Los criterios del subtitulado](#los-criterios-del-subtitulado)
- [6. Transiciones](#6-transiciones)
  - [Corte y transición](#corte-y-transición)
  - [Las transiciones corrientes](#las-transiciones-corrientes)
  - [Las colas](#las-colas)
  - [Duración, alineación y suavizado](#duración-alineación-y-suavizado)
- [7. Limpieza de audio](#7-limpieza-de-audio)
  - [Qué se limpia](#qué-se-limpia)
  - [Ecualización](#ecualización)
  - [Los filtros de corte](#los-filtros-de-corte)
  - [La reducción de ruido por perfil](#la-reducción-de-ruido-por-perfil)
  - [Los artefactos](#los-artefactos)
  - [La música bajo la voz](#la-música-bajo-la-voz)
  - [La limpieza de un diálogo, paso a paso](#la-limpieza-de-un-diálogo-paso-a-paso)
  - [La sonoridad de la pieza terminada](#la-sonoridad-de-la-pieza-terminada)
- [Aplicación práctica: la postproducción de una noticia](#aplicación-práctica-la-postproducción-de-una-noticia)
- [Normativa y recomendaciones técnicas que el tema cita](#normativa-y-recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## La postproducción en la sala de montaje

Postproducir es trabajar sobre el material ya montado para que llegue a emisión técnicamente correcto
y con la forma que pide la pieza: color, efectos, grafismo, subtítulos, transiciones y sonido. En un
programa grande cada parte tiene su especialista (etalonador, grafista, técnico de sonido); en una
pieza informativa buena parte la hace el propio montador en el sistema de edición (oficio). Qué
programa usa CSRTV no consta en ningún documento publicado; el tema toma como ejemplo DaVinci Resolve
y Premiere, cuya documentación se ha leído, y el tema 3 explica el sistema de edición no lineal y el
*render*.

Blackmagic resume así el fin de la corrección de color: **«Clearly, the most fundamental aspect of
the color correction process is that of making every clip look its best.»** (hacer que cada plano se
vea lo mejor posible; *Resolve 21*, cap. 125, p. 3086). Y la idea vale para toda la postproducción:
**«you have the opportunity to overcome inconsistencies with exposure and white balance that were,
for various reasons, unavoidable»** (corregir lo que en la grabación no se pudo evitar), sin olvidar
que **«the quality of your results will depend heavily on the data quality and "latitude" of your
source media»**: el resultado depende de la calidad y la latitud del material de origen.

## 1. Color básico

### Qué es etalonar

El etalonaje es la fase de posproducción en la que se ajusta la imagen de toda la producción para
que sea coherente y esté a la altura de un patrón. La palabra viene del francés *étalonnage* y del
*étalon*, «patrón» o «medida de referencia»: etalonar es llevar algo a un patrón.

Lo que se hace en un etalonaje, por orden:

| Fase | En qué consiste |
|---|---|
| Etalonaje técnico o primario | Poner cada plano en su sitio: niveles de negro y de blanco dentro del rango legal del tema 2, balance de blancos, exposición |
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
primeros se desarrollan en el epígrafe 2).

### Medir antes de tocar: los monitores de señal

El color no se corrige a ojo sobre un monitor cualquiera: se mide. Las formas de onda, los niveles
legales de la señal y el monitor de referencia están en el tema 2 («Medir la señal» y «Los límites de
la señal según la EBU»). Aquí se ve lo que cada instrumento dice cuando se corrige. Resolve ofrece
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
(p. 3147). En HDR se mide con la escala de la curva con la que se trabaja (tema 2).

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

Blackmagic da tres usos frecuentes que coinciden con los tres últimos: el punto de partida para el
material logarítmico (**«it's usually faster to use a LUT that's tailored to your type of media and
the exposures you're using»**), el rodaje (**«LUTs are commonly used in onset workflows»**) y el
aspecto (**«LUTs are frequently used as a stylistic component of a grade, or "look"»**) (p. 3545).

Resolve trabaja con el formato .cube: **«The .cube format can be used as either a simple 33x33x33 3D
LUT, or as a shaper LUT»**; Resolve exporta cubos de 17, 33 o 65 puntos por lado, y avisa de que los
de 17 **«are not recommended to use for grading»**, aunque sirven para monitorizar en rodaje (p. 3546).

Dos avisos que separan al montador del aficionado:

1. Una LUT no corrige un plano mal expuesto: aplicada sobre material mal expuesto exagera el error en
   vez de corregirlo (oficio).
2. Una LUT 3D recorta lo que se sale de su rango: **«when a 3D LUT is fed values that are outside of
   the range that LUT is designed to handle, the out-of-range data will be clipped»**. El ejemplo de
   Blackmagic es el vídeo con superblancos que entra en una LUT pensada para rango completo, que
   **«will clip the super-white part of the signal»** (p. 3546). Para eso existe la *shaper LUT*, que
   antepone una 1D que encaja la señal en el rango de la 3D.

## 2. Corrección

### Primaria y secundaria

La corrección de color se divide en dos niveles (oficio, con los términos que usa Blackmagic):

| Nivel | Qué toca | Herramientas |
|---|---|---|
| Primaria | La imagen entera: negros, blancos, contraste, balance, saturación | Ruedas de color y barras (*lift*, *gamma*, *gain*, *offset*), temperatura, matiz, contraste, saturación |
| Secundaria | Una parte de la imagen: una zona, un color, un objeto | Ventanas (*windows*), cualificadores (HSL, RGB, luminancia) y curvas de matiz |

Primero se hace la primaria de todos los planos y después la secundaria donde haga falta: no se
aísla un color hasta que el plano entero está equilibrado (oficio).

### *Lift*, *gamma* y *gain*

Las ruedas de la corrección primaria actúan sobre tres zonas de tono: **«Color balance wheels let you
adjust all three color channels at once, altering the color temperature of the scene at specific
ranges of tonal detail referred to as lift, gamma, and gain.»** (cap. 125, p. 3087). Y lo hacen por
separado: **«All of these controls let you adjust the color tone of the shadows, midtones, and
highlights independently from each other.»** (p. 3088).

| Mando | Zona | Qué se consigue |
|---|---|---|
| *Lift* | Sombras | Subir o bajar los negros; quitar una dominante en las sombras |
| *Gamma* | Medios tonos | Aclarar u oscurecer el cuerpo de la imagen sin mover negros ni blancos |
| *Gain* | Altas luces | Subir o bajar los blancos; corregir el balance de blancos |
| *Offset* | Todo el rango | Mover los tres canales por igual en todo el rango: **«linear adjustments to rebalance the entire tonal range of the RGB channels»** (cap. 131, p. 3204) |

Las zonas se solapan: son **«three overlapping tonal ranges referred to as Lift, Gamma, and Gain»**,
definidas por la luminosidad **«on a scale where 0 is absolute black and 1023 is absolute white»**
(cap. 131, pp. 3202-3203). Por eso tocar una mueve algo las otras, y el ajuste se hace yendo y
viniendo entre ellas. Cada rueda tiene debajo su mando maestro, que cambia el brillo sin cambiar el
color: **«the Master Lift, Gamma, and Gain wheels work together to let you alter image contrast in
different ways: deepening shadows, lightening highlights, and brightening or darkening the midtones
in between»** (p. 3088).

### Temperatura, matiz, contraste y saturación

Los mandos que acompañan a las ruedas (cap. 131, pp. 3200-3201):

| Mando | Qué hace, según Blackmagic |
|---|---|
| Temperatura (*Temp*) | **«A specifically constrained Gain color balance adjustment»** sobre el eje cálido-frío: **«Raising this parameter performs a Gain color balance adjustment toward orange»**; al bajarlo, hacia azul-cian. Rango −4000 a +4000 |
| Matiz (*Tint*) | Ajuste del *gain* sobre el eje magenta-verde, para la luz artificial **«such as fluorescent and sodium vapor lighting fixtures»**: al subirlo, hacia magenta («menos verde», contra el fluorescente); al bajarlo, hacia verde. Rango −100 a +100 |
| Contraste y pivote (*Contrast*, *Pivot*) | Separa o junta claros y oscuros **«about a center point defined by the Pivot parameter»**; por defecto aplica una curva en S para que sombras y luces **«will not be clipped»** |
| Saturación (*Saturation*) | **«A uniform saturation operation»**: 50 es la unidad, 0 blanco y negro, 100 el doble |
| Realce de color (*Color Boost*) | Saturación no uniforme, que actúa más en lo poco saturado: **«sometimes referred to as a vibrance operation»** |

Temperatura y matiz son, por tanto, ajustes del *gain*: corrigen la luz, que se ve sobre todo en los
blancos. Una dominante sólo en las sombras se corrige en el *lift* (oficio).

Resolve tiene además una corrección automática, *Auto Color*, que **«provides a quick way to
automatically balance the blacks and whites of a clip based on the current frame at the position of
the playhead»**, pensada para **«the Rec. 709 color space, and at a gamma of 2.4»** (p. 3201). Da un
punto de partida, no un resultado: se comprueba siempre en los monitores de señal (oficio).

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
  (p. 3090). Es un croma (epígrafe 3) que no sustituye el fondo sino que decide dónde se corrige. Los
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

### Lo que no se corrige

Hay límites que no pone el programa sino la información. El Libro de Estilo de Canal Sur, al tratar
los reportajes de sucesos en su capítulo de malos tratos (9.2), advierte contra los recursos que
convierten la noticia en ficción: **«La estética y la narrativa propias de reportajes de sucesos deben
acometerse con cuidado. La imagen oscilante ‘cámara en mano’, una
música tópica, un virado a blanco y negro... evocan inevitablemente escenas ficticias de misterio,
terror... o de una película. Y la información sólo habla de realidad.»** (9.2.12.4, p. 130). La regla está
escrita para esos reportajes; extenderla a toda la información es criterio de oficio: un aspecto
creativo (el virado, la dominante fuerte) cabe en una promoción o una pieza cultural; en un
informativo, la corrección busca que la imagen se parezca a lo que pasó.

## 3. Efectos

### Qué es un efecto en el sistema de edición

Todo lo que no es cortar un clip detrás de otro es un efecto: una transición, un cambio de tamaño o
posición, una corrección, una incrustación, un cambio de velocidad, un rótulo. Cada clip trae de
serie sus parámetros de composición, transformación y recorte; Blackmagic lo dice a propósito de los
títulos, que **«expose the same Composite, Transform, and Cropping parameter groups as any other
clip»** (cap. 56, p. 1213). Los efectos no existen como archivo: hay que calcularlos, y eso es el
*render* del tema 3.

La clasificación práctica de oficio:

| Familia | Ejemplos |
|---|---|
| De composición | Incrustación (croma, luma, alfa), superposición de capas, opacidad, modos de fusión |
| De transformación | Tamaño, posición, rotación, recorte, estabilización |
| De tiempo | Cámara lenta o rápida, imagen congelada, marcha atrás |
| De imagen | Corrección de color, desenfoque, pixelado, nitidez, viñeta |
| De transición | Fundido, cortinilla (epígrafe 6) |

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
necesita resolución de color, así que un material con submuestreo cromático fuerte (tema 2) da bordes
peores que uno 4:2:2 o 4:4:4.

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
bueno. De aquí sale la notación 4:4:4:4 del tema 2: la cuarta cifra es el alfa.

El formato del fichero decide si puede llevar alfa (epígrafe 4, «Los ficheros gráficos»).

### La máscara

La función principal de una máscara de capa es ocultar o mostrar partes específicas de una capa sin
eliminar permanentemente el contenido.

Cómo funciona: la máscara es una imagen en escala de grises pegada a la capa. Donde la máscara es
blanca, la capa se ve; donde es negra, no; donde es gris, se ve a medias. Es exactamente un canal alfa
dibujado a mano, y por eso este epígrafe va detrás del anterior.

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

Por debajo del 100 %, la pista de control muestra triángulos amarillos más separados; por encima,
azules más juntos (p. 1258). El sonido: con los cambios lineales cambia de duración con el vídeo
(sin corrección de tono en Linux y Windows y con ella en Mac, según el manual; la casilla *Pitch
Correction* la aplica, aunque en cambios grandes puede no sonar tan bien), pero **«audio that accompanies variable speed effects will be muted.»** (pp. 1254-1256).

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
proceso decide cómo se convierten los clips de otra cadencia en una línea de tiempo mixta (tema 3).

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

La selección de planos y el tratamiento informativo se desarrollan en el tema 1.

## 4. Grafismo

### Quién hace qué

El grafismo de una casa (cabeceras, cortinillas, mapas, infografías, plantillas de rótulos) lo diseña
el área de grafismo; el montador lo inserta en la pieza, rellena las plantillas y hace los rótulos
sencillos en el propio sistema de edición. La ficha del Grafista y el circuito de los rótulos entre
redacción, realización y emisión están en el tema 9. Si en Canal Sur los rótulos van incrustados en el
vídeo desde la sala o los inserta realización en la emisión no consta en ningún documento publicado.

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
el mismo tamaño y la misma posición (oficio). Las plantillas y la automatización se ven en el tema 13.

### Las zonas de seguridad

Las zonas de seguridad son dos marcos dentro del cuadro. Resolve los define así (cap. 56, p. 1214):
**«Action: Keep all movement and important action within this box.»** y **«Title: Keep all on screen
text within this box.»** Nacieron para los televisores de tubo, que recortaban los bordes de la
imagen, y Blackmagic reconoce que hoy son **«somewhat anachronistic in this age of flat screen digital
televisions»**, pero siguen sirviendo para que la imagen no quede recortada por **«the variety of
mobile devices and social media sites in use today»**. Los valores por defecto que Resolve da a sus
zonas personalizadas son **«93% for Action Area and 90% for Title Area»** (p. 1215): la de título,
más estrecha, dentro de la de acción.

Regla de oficio: ningún rótulo fuera de la zona de título, y ningún logotipo ni marcador que tape la
cara del entrevistado. En las versiones verticales o cuadradas para redes, el mismo programa ofrece
guías *Social Media* de **«1:1, 4:5, 9:16, 1.91:1, 16:9»** (p. 1214); se ven en el tema 12.

### Los ficheros gráficos

El canal alfa es la máscara de transparencia que un fichero gráfico puede llevar dentro, y es la
señal de recorte del epígrafe 3 guardada en el propio archivo.

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
precisamente el canal alfa. En gráficos, «bits» se cuenta por píxel; en vídeo (tema 2) se cuenta por
componente. Una imagen de «8 bits» en vídeo tiene 8 bits por cada componente —24 en total— y una
imagen de «32 bits» en gráficos los tiene en total. Es la misma palabra con dos unidades.

La tabla y las cuentas son de oficio. La consecuencia en la sala: un rótulo o un logotipo que tiene que
ir encima de la imagen se pide en PNG o TIF con alfa, o como par relleno-recorte; si llega en JPG,
llega con fondo (oficio).

### El grafismo en alto rango dinámico

En HDR, un rótulo blanco no va al máximo de la señal. El Informe UIT-R BT.2408-9 define el blanco del
grafismo: **«Graphics White is defined within the scope of this Report as the equivalent in the
graphics domain of a 100% reflectance white card: the signal level of a flat, white element without
any specular highlights within a graphic element. It therefore has the same signal level as HDR
Reference White, and graphics should be inserted based on this level.»** (§ 2.1). Ese nivel es el 75 %
de la señal en HLG y el 58 % en PQ, que corresponde a 203 cd/m² en un monitor PQ o en uno HLG de
1 000 cd/m² de pico (tabla 1; se da entera en el tema 2).

Y el porqué, en el apartado de grafismo: **«SDR graphics should be directly mapped into the HDR signal
at the ‘Graphics White’ signal level specified in Table 1 (75% HLG or 58%PQ) to avoid them appearing
too bright, and thus making the underlying video appear dull in comparison.»** (§ 9). Un rótulo al
100 % en HDR deslumbra y hace que el vídeo de debajo parezca apagado. El mismo apartado distingue dos
casos: si se quiere conservar el color corporativo del gráfico, **«a display-light mapping should be
used»**; si se quiere igualar con un rótulo que aparece en la escena (el marcador de un estadio), **«a
scene-light mapping is usually preferred»**.

### Lo que pide el Libro de Estilo

El Libro de Estilo de Canal Sur fija reglas para los gráficos informativos (3.16, «Gráficos», pp. 57-58), que se
desarrollan en el tema 9. Las dos que el montador mide con el reloj: **«La primera norma es dar
información ajustada que no incluya más de cuatro o cinco elementos por pantalla, con una presencia
mínima recomendable de ocho segundos.»** (3.16, p. 57). Y la del sonido (al final de 3.16.2, p. 58):
los gráficos **«llevarán una ‘cama’ de audio
por el canal correspondiente, salvo que se respete el sonido propio de la grabación»**. El rótulo,
además, es información: **«El rótulo que acompaña es también información. Reúne brevedad, impacto y
síntesis.»** (3.6.1, p. 50).

## 5. Subtítulos

### Abiertos y cerrados

La distinción que manda en la sala es dónde va el subtítulo. La guía de la Universidad de Burgos la
formula así: **«los subtítulos abiertos van incrustados en el video y el usuario no tiene control
sobre ellos. Los subtítulos cerrados, pueden añadirse y eliminarse a voluntad del espectador cuando
desee.»** Y añade: **«Desde el punto de vista de la accesibilidad son más adecuados los subtítulos
cerrados ya que permiten decidir activarlos o no.»** (Universidad de Burgos, *Guía para elaborar
Material Multimedia Accesible*, 2020, p. 4).

| | Abierto (incrustado) | Cerrado |
|---|---|---|
| Dónde va | Dentro de la imagen: forma parte de los píxeles | Aparte: un fichero o una pista de datos junto al vídeo |
| Quién decide si se ve | Nadie: se ve siempre | El espectador |
| Se corrige | Rehaciendo el vídeo | Cambiando el fichero |
| Uso corriente | Versiones para redes, que se ven sin sonido; traducción de un total en otro idioma | Emisión con subtitulado para personas sordas; plataformas |

La columna de uso es de oficio. En una pieza informativa, el total en otro idioma o con sonido
ininteligible se subtitula incrustado, como un rótulo más; el subtitulado de accesibilidad de la
emisión va aparte y no lo hace normalmente el montador (oficio). Las obligaciones de subtitulado, la
audiodescripción y la lectura fácil son el tema 11; las versiones para redes, el tema 12.

### Cómo se hacen y cómo se entregan

Los sistemas de edición tienen pistas propias de subtítulos, además de las de vídeo y audio. Resolve,
al entregar, ofrece estas salidas (cap. 187, p. 4205):

| Salida | Qué hace (Resolve 21) |
|---|---|
| Fichero aparte (*As a separate file*) | **«Outputs each subtitle track you select as a separate file»**, en los formatos **«IMSC1, DFXP, SRT, and WebVTT»** |
| Incrustado (*Burn into video*) | **«Renders all video with the currently selected subtitle track burned into the video.»** Es el subtítulo abierto |
| Embebido (*As embedded captions*) | **«Outputs the currently selected subtitle track as an embedded metadata layer within supported media formats»**; admite **«CEA-608 closed captions within MXF OP1A and QuickTime files»** |

El mismo manual avisa de un límite: **«Neither analog (Line 21) nor digital (CEA-708) closed caption
output via Decklink or UltraStudio is supported at this time.»** Y en la entrega IMF (tema 4), las
pistas de subtítulos van dentro del paquete como **«subtitle tracks (data essences)»** (p. 4219).

Qué formato pide cada destino (el sistema de emisión de Canal Sur, cada plataforma) no consta en
ningún documento publicado de la RTVA; se pregunta antes de entregar (oficio).

### Los criterios del subtitulado

La norma de subtitulado para personas sordas que cita la guía es la UNE 153010:2012 (AENOR). Su texto no se ha
leído; lo que sigue es la síntesis publicada por la Universidad de Burgos, que advierte que
son **«algunos requisitos que deben cumplir los subtítulos, los cuales se tratan con mayor detalle en
la norma UNE 153010»** (p. 4; los requisitos visuales, en las pp. 4-5; los de tiempo, en la p. 6):

| Aspecto | Criterio, según la síntesis de la Universidad de Burgos |
|---|---|
| Posición | **«Los subtítulos deben aparecer centrados en la parte inferior de la pantalla y ocupar dos líneas de texto y excepcionalmente tres.»** |
| Caracteres | **«El máximo número de caracteres por línea es 37.»** |
| Cortes | **«No se deben separar sílabas de la misma palabra en dos líneas.»** |
| Diálogos | **«En los diálogos, se debería asignar una línea nueva para cada personaje.»** |
| Velocidad | **«La velocidad recomendada para los subtítulos es de unos 15 caracteres por segundo.»** |
| Sincronía | **«Las entradas y salidas de los subtítulos deben coincidir, siempre que sea posible, con el movimiento labial, con los cambios de plano, con la locución y/o información sonora.»** |
| Permanencia | **«Un subtítulo de una línea permanece en pantalla unos tres segundos, y el subtítulo de dos líneas no debería mantenerse más de seis segundos.»** **«Los subtítulos han de estar en pantalla como mínimo un segundo y como máximo seis.»** |
| Pausas | **«Hay que considerar las pausas interpretativas, y deben coincidir en la medida de lo posible con comas y puntos.»** (p. 4) |
| Tipografía | **«La elección de la tipografía debe responder a criterios de máxima legibilidad.»** (p. 4) |
| Información contextual | **«La información contextual debe aparecer entre paréntesis y en la misma línea del subtítulo correspondiente.»** (p. 4); en «Efectos sonoros»: **«La información contextual se subtitula en mayúsculas y entre paréntesis.»** (p. 6) |
| Mayúsculas | **«Las mayúsculas sólo se usan para traducir el título del programa y para dar cuenta de texto que aparece escrito en mayúsculas en el original: titulares de periódicos, pancartas, etc.»** (p. 5) |
| Cursiva | **«La cursiva da cuenta de las voces procedentes de un televisor, una radio, o de personajes que están fuera de pantalla.»** También para títulos de películas o libros, letras de canciones y términos en otro idioma (p. 5) |
| Números | **«Escribir la numeración con letras del cero al diez y con caracteres arábigos el resto de las cantidades.»** (p. 5) |
| Signos | **«Utilizar mejor los paréntesis que los corchetes.»** (p. 5) |
| Efectos sonoros | Se describen los que sean relevantes para entender el vídeo (música, ruidos de fondo, sonidos de animales o cosas), diferenciados del diálogo (p. 6) |

La guía no es del todo coherente: en la p. 5 reserva las mayúsculas para títulos y rótulos del
original, y en la p. 6 pone en mayúsculas la información contextual. Se da como la guía lo dice.

Los colores. La guía, citando la norma, dice que **«ciertas combinaciones de colores facilitan la
lectura ya que producen mayor contraste y menor fatiga visual»**, y las ordena por legibilidad
(p. 5):

| Orden | Carácter sobre fondo |
|---|---|
| 1 | **«Carácter amarillo sobre fondo negro.»** |
| 2 | Verde sobre negro |
| 3 | Cian sobre negro |
| 4 | Magenta sobre negro |
| 5 | Blanco sobre negro |
| 6 | Rojo sobre blanco |
| 7 | Azul sobre blanco |
| 8 | Azul sobre amarillo |

Ese orden sirve también para distinguir a los personajes: **«el personaje principal estaría
subtitulado con caracteres amarillos sobre fondo negro, el segundo en importancia le correspondería
caracteres verdes y así sucesivamente.»** (p. 5). Para identificarlos, la guía da este orden de
prioridad: uso del color, de etiquetas y de guiones; el color asignado se mantiene, y los guiones
sólo **«cuando exista riesgo de confusión entre personajes»** (pp. 6-7).

Una cuenta que el tribunal puede pedir (cálculo propio): a 15 caracteres por segundo, un subtítulo de
dos líneas llenas (74 caracteres) necesita unos 5 segundos, dentro del máximo de seis; uno de una línea
llena (37 caracteres), unos 2,5 segundos, cerca de los «unos tres segundos» de la guía.

Y una regla de sala que sale de la sincronía: el subtítulo que cruza un corte de plano se nota; si se
puede, se parte en el corte (oficio, coherente con el criterio anterior).

## 6. Transiciones

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

Las colas son también lo que se deja al exportar o conformar un montaje (tema 3): sin colas no se
puede alargar un plano ni poner un fundido en la fase siguiente.

### Duración, alineación y suavizado

Tres parámetros de toda transición (Resolve, p. 1198):

- Duración: **«The duration of the transition, shown in both seconds and frames.»** Resolve ofrece de
  entrada un cuarto de segundo, medio, uno y dos: **«quarter-second, half-second, one second, and two
  seconds, expressed in frames at whatever the current frame rate of the Timeline is»** (p. 1195).
- Alineación respecto del corte: **«“Start on Edit,” “Center on Edit,” and “End on Edit.”»** Empieza en
  el corte, está centrada en él o termina en él; según la alineación, los cuadros de más salen sólo del
  plano que sale (la transición empieza en el corte), de los dos (centrada) o sólo del que entra
  (termina en el corte) (oficio).
- Suavizado (*Ease*): la curva de velocidad del epígrafe 3 aplicada a la transición (p. 1199).

Qué transición se usa por defecto se puede cambiar: **«Right-click any transition or effect and choose
“Set as Standard Transition.”»** (p. 1199). En una casa, la transición estándar y su duración suelen
formar parte de la plantilla del programa (oficio).

## 7. Limpieza de audio

Limpiar el audio es la parte de la postproducción de sonido que hace el montador: dejar la voz
inteligible, quitar lo que molesta y encajar la música bajo la locución. La mezcla de un programa
grande la hace el área de sonido (tema 9); una pieza informativa la cierra, casi siempre, el propio
montador en el sistema de edición (oficio). Las cualidades del sonido, el audio digital y los niveles
están en el tema 2.

### Qué se limpia

Limpiar es quitar de una grabación lo que sobra sin tocar lo que sirve (oficio). Los defectos
corrientes y la herramienta que se usa contra cada uno:

| Defecto | Qué es | Contra él (oficio) |
|---|---|---|
| Ruido de fondo constante | Soplido, climatización, ventiladores, motores | Reducción de ruido por perfil |
| Zumbido de red | La frecuencia de la red eléctrica y sus armónicos | Filtros de ranura en la fundamental y sus armónicos, o un reductor de zumbido |
| Chasquidos y crepitaciones | Impulsos cortos: un mal corte, un contacto, un disco | Reductor de chasquidos, o edición de la muestra |
| Recorte | La onda saturada, con la cresta plana | Reconstrucción de la forma de onda; si es grave, no tiene arreglo |
| Oclusivas | El golpe de aire de la p y la b en el micrófono | Filtro paso alto en ese tramo o reductor de oclusivas |
| Sibilantes | La s demasiado brillante | Reductor de sibilantes |
| Viento y roces | Golpes de graves, roce de la ropa con un corbata | Filtro paso alto, reductores específicos o edición |
| Reverberación de la sala | La voz lejana, con cola | Reductor de reverberación, con límites |

El fabricante del programa de restauración cuyo manual se ha leído, iZotope, tiene un módulo para
casi cada fila: **«De-click»**, **«De-clip»**, **«De-crackle»**, **«De-ess»**, **«De-hum»**,
**«De-plosive»**, **«De-reverb»**, **«De-rustle»**, **«De-wind»**, además del **«Spectral
De-noise»** del epígrafe siguiente. Son nombres de un producto comercial: sirven para ver qué
familias de herramientas existen, no como norma.

La regla de oficio que va antes que todas: lo que no se graba no hay que limpiarlo. Toda limpieza
fuerte deja huella, y lo que se recorta en la grabación no se recupera.

Los sistemas de edición traen herramientas del mismo tipo. Las de Resolve, en su módulo de sonido
(*Resolve 21*, cap. 181, «Fairlight FX»):

| Herramienta | Qué hace, según Blackmagic |
|---|---|
| *Noise Reduction* (reducción de ruido) | **«A repair plugin designed to reduce a wide variety of noise in all kinds of recordings.»** Trae tres ajustes de partida: **«De-Hiss, De-Rumble, and De-Rumble and Hiss»** (contra el soplido, contra el retumbar grave, y los dos) (p. 4121) |
| *De-Hummer* (reductor de zumbido) | **«Eliminates hum noise that often stems from electrical interference with audio equipment due to improper cabling or grounding. Typically 50 or 60 cycle hum is a harmonic noise, consisting of a fundamental frequency and subsequent partial harmonics starting at twice this fundamental frequency.»** (p. 4102) |
| *De-Esser* (reductor de sibilantes) | **«designed to reduce excessive sibilance, such as hissing "s" sounds or sharp "ts" sounds, in dialogue or vocals»**; las sibilantes **«are usually found in the range of 5 - 8kHz»** (p. 4101) |
| *Dialogue Leveler* (nivelador de diálogo) | **«analyzes source material to detect dialogue and then "rides down" louder areas, "lifts up" softer areas, and lowers background sounds that are not dialogue»** (p. 4091) |
| *Voice Isolation* (aislamiento de voz; sólo en la versión Studio del programa) | **«uses an AI model trained for any type of human voice»**; con el mando de cantidad, **«Values between 70 and 80 work well for natural results while strongly isolating the source»** (p. 4096) |
| *Ducker* | Baja una pista con la señal de otra (epígrafe «La música bajo la voz») |

En España, **«La frecuencia empleada en la red será de 50 Hz.»** (Reglamento electrotécnico para
baja tensión, aprobado por el Real Decreto 842/2002, art. 4.4): el zumbido está en 50 Hz y en sus
armónicos, 100, 150, 200… (cálculo sobre lo que dice el manual de Resolve). Adobe organiza lo mismo por tipos de sonido: en el panel
*Essential Sound* de Premiere cada clip se clasifica como **«Dialogue, Music, SFX, and Ambience»**, y
para el diálogo el panel reúne **«unifying the different recordings to a common loudness, reducing
background noise, and adding compression and EQ»** (ayuda de Premiere, «Audio editing with Essential
Sound panel», actualizada el 07-01-2026).

### Ecualización

Ecualizar es cambiar el equilibrio entre las bandas de frecuencia de una señal. En una sala de
edición se hace por tres motivos: corregir un defecto de captación, encajar una voz sobre una
música, y construir un efecto.

Las formas de actuar sobre una banda de frecuencias son tres:

| Forma | Qué hace | Para qué se usa |
|---|---|---|
| Campana (*peaking*) | Sube o baja una franja alrededor de una frecuencia central; lo de los lados queda igual | Corregir o realzar una zona concreta: la nasalidad de una voz, el cuerpo de un bombo |
| Estantería (*shelving*) | Sube o baja por igual todo lo que queda por encima (agudos) o por debajo (graves) de una frecuencia | Dar o quitar brillo o peso a todo el extremo del espectro |
| Filtro de corte | Elimina lo que queda por debajo o por encima de una frecuencia | Quitar lo que está fuera de la banda útil; se desarrolla en «Los filtros de corte» |

La clasificación es de oficio, no de norma.

La imagen que fija la definición: el nombre viene de *shelf*, «estante». La curva sube o baja
hasta un nivel y allí se queda plana, como la balda de una estantería. Eso es lo que lo distingue
de la campana, que vuelve a bajar al otro lado, y del paso alto o bajo, que siguen cayendo
hasta el infinito en lugar de estabilizarse.

Dos reglas de oficio para la voz: el ecualizador corrige (un micrófono de corbata tapado, una voz
nasal) y se toca poco; y una voz que tiene que entenderse sobre música no se sube de volumen, se le
hace sitio, bajando la música o recortando en la música la zona de frecuencias de la voz.

### Los filtros de corte

Un filtro deja pasar una zona del espectro y atenúa el resto. Los de uso diario en sonido son
cuatro, y su clasificación es de oficio:

| Filtro | Qué deja pasar | Uso corriente |
|---|---|---|
| Paso alto (corte de graves) | Lo que está por encima de la frecuencia de corte | Quitar el retumbar de baja frecuencia, los golpes de pie de micro, el viento y el exceso de graves por efecto de proximidad |
| Paso bajo (corte de agudos) | Lo que está por debajo | Quitar siseo y ruido de alta frecuencia |
| Paso banda | Sólo una franja | Limitar una señal a una banda: el efecto «teléfono» sobre una voz |
| Banda eliminada o ranura (*notch*) | Todo menos una franja estrecha | Quitar un tono concreto: un zumbido, un acoplamiento |

Dos datos describen un filtro de corte: la frecuencia de corte, que se toma donde la respuesta ha
caído 3 dB, y la pendiente, que se da en decibelios por octava y dice lo deprisa que atenúa más allá
del corte. La pendiente la fija el orden del filtro. Rane da la regla: **«each order, or degree, of a
filter increases the slopes by 6 dB/octave or 20 dB/decade»**; cada orden suma 6 dB por octava (o
20 dB por década). Un filtro de primer orden cae 6 dB/octava; aplicando la regla, uno de segundo
orden, 12 dB/octava, y uno de tercer orden, 18 dB/octava; y uno de cuarto orden, según el ejemplo de Rane, **«24 dB/octave (4 x 6 dB/octave) or 80
dB/decade»**. A diferencia del ecualizador de estantería, que baja por igual todo un extremo, el filtro
de corte atenúa cada vez más cuanto más se aleja de la frecuencia de corte.

*Rumble* es el ruido de baja frecuencia de un giradiscos, y el filtro que lo quita se llama así.

En la práctica, el filtro paso alto está en casi todos los canales de entrada de una mesa y es el
primer proceso que se aplica a una voz: por debajo de la voz no hay nada útil, y lo que hay (tráfico,
aire acondicionado, golpes) se come el margen y hace trabajar al compresor sin necesidad. Es oficio.

Qué es un notch: un filtro de ranura, de Q altísimo, que quita una franja de frecuencia muy estrecha
y no toca lo de al lado.
Es el filtro del zumbido de red: un *notch* en 50 Hz y otros en sus armónicos, que es lo que
automatiza un reductor de zumbido (oficio).

### La reducción de ruido por perfil

El principio lo explica el manual de iZotope RX 11: **«Spectral De-noise is designed to remove
stationary or slowly changing tonal noise and broadband hiss by learning a profile of the offending
noise and then subtracting it from the signal. It can be useful for tape hiss, HVAC systems,
outdoor environments, line noise, ground loops, camera motors, fans, wind, and complex buzz with
many harmonics.»** Es decir: el programa aprende cómo es el ruido y lo resta del conjunto.

Cómo se trabaja:

1. Se busca un trozo con sólo ruido: **«Make a selection of the longest section of noise you can
   find in your file (ideally a few seconds in length).»** Por eso se graba un minuto de ambiente
   sin nadie hablando: sin trozo de ruido limpio no hay perfil.
2. Se aprende el perfil. El perfil aprendido a mano sirve para el ruido fijo: **«Manually learned
   noise profiles are best suited to removing or reducing noise that is constant and continuous»**.
   Para el ruido que cambia —**«recordings in outdoor environments, traffic noise, or ocean
   waves»**— el programa tiene un modo adaptativo, que sigue al ruido.
3. Se ajusta el umbral: **«Higher threshold settings reduce more noise, but also suppress low-level
   signal components.»**
4. Se ajusta la reducción, que puede ser distinta para las partes tonales y las aleatorias del
   ruido: **«tonal parts (such as hum, buzz or interference) and random parts (such as hiss)»**.

Y el aviso del fabricante: **«Strong suppression of noise can also degrade low-level signals, so
it is recommended to apply only as much suppression as needed»**.

En Resolve los mandos equivalentes son el umbral y la sensibilidad. El umbral **«Relates to the
signal-to-noise ratio (SNR) in the source recording. Recordings with a poor signal-to-noise ratio will
require a higher threshold value, resulting in more noise reduction being applied.»** Y la
sensibilidad avisa del mismo riesgo: **«Higher sensitivity values exaggerate the detected noise
profile; the result is that more noise will be removed, but more of the dialogue you want to keep may
be affected.»** Para comprobarlo, la casilla que deja oír sólo lo que se quita: **«Listen to Noise
Only»**, **«very useful to determine if too much signal is being removed»** (p. 4122).

### Los artefactos

Una limpieza excesiva se oye, y el manual nombra dos artefactos, uno en cada extremo del mismo
ajuste:

- La sustracción espectral fuerte **«can produce musical noise artifacts, resulting in a “chirpy”
  or “watery” sound during heavy processing»**: el ruido que queda suena a gorjeo o a agua.
- Y si, para evitarlo, el proceso se apoya más en la puerta de banda ancha, tiene menos ruido
  musical pero suena a puerta y deja **«bursts of noise right after the signal falls below the
  threshold»**: ráfagas de ruido justo cuando la voz se calla. Es un compromiso entre los dos
  artefactos, que el módulo regula con un control propio (*Artifact Control*).

Cómo se evitan (oficio): reducir poco y en varias pasadas mejor que mucho en una; escuchar el
resultado y también lo que se ha quitado; y comparar con el original a igual nivel. Una voz algo
ruidosa se entiende; una voz con artefactos, peor.

### La música bajo la voz

El *audio ducking* es una función que permite reducir el nivel de audio de una o más pistas cuando
se desea escuchar el nivel de otra pista de audio.

Para qué sirve, en el trabajo real: es lo que hace que la música baje sola cuando entra la voz
en off y vuelva a subir cuando la voz calla. El nombre viene de *duck*, agacharse: la música se
agacha para dejar pasar la voz.

Cómo funciona: el nivel de una pista —la que manda— controla la ganancia de otra —la que
cede—.

La puerta de ruido cierra el canal cuando la señal baja de un umbral (oficio). El *ducker* se
gobierna por una entrada de control aparte, la cadena lateral o clave externa (*side-chain*); el
fabricante citado es Rane, en sus notas técnicas:

El *ducker* trabaja al revés que la puerta: baja una señal cuando otra, la de control, supera el
umbral. Rane: **«A ducker works the opposite of a gate. The signal is attenuated when the side-chain
input goes above the threshold»**; y sus mandos: **«In ducker mode, attack time determines how quickly the signal is reduced as the control
signal exceeds the threshold setting»**; **«The hold time determines how long the signal remains
ducked when the control signal drops below the threshold setting»**; y la profundidad, de **«0 to
-80 dB»**, fija cuánto se atenúa **«when the control signal is at or above the threshold
setting»**.

En radio y televisión, el uso
corriente es el de la música bajo la voz: la música entra por el camino principal, la voz del
locutor por la clave externa, y cada vez que el locutor habla la música baja sola; cuando calla,
vuelve. Es el efecto de *ducking*. Esta aplicación a la radio y la televisión es de oficio.

Blackmagic lo describe igual, y precisa que se hace sin comprimir las señales: **«a common use of
"ducking" is automatically lowering a music or sound effects bed so that dialogue or a VO track can be
heard more prominently in a mix. This is achieved without compressing the incoming signals.»**
(*Resolve 21*, cap. 181, p. 4094). Un mismo *ducker* puede tomar el control de varias pistas de
diálogo a la vez, para que baje la música con cualquiera de ellas.

El nivelador de diálogo hace otra cosa: iguala la voz consigo misma. Según Blackmagic trabaja **«without
the typical "pumping" or other unwanted side effects of dynamics processors (compression/limiting)»**
y da resultados como los de **«detailed, manual clip gain adjustments or "riding" the track with fader
automation»** (p. 4091).

Y una advertencia de oficio: el *ducking* automático se nota si está mal ajustado. Un retorno
demasiado rápido hace que la música «respire» detrás de la voz, y ése es el defecto por el que se
reconoce una mezcla hecha con prisa.

La alternativa manual, que es la de oficio en una pieza corta: bajar la música con la línea de volumen
del clip o con la automatización, con puntos antes de que entre la voz y después de que termine. El
Libro de Estilo de Canal Sur, por otra parte, pide moderación con la música en los reportajes de
sucesos (9.2.12.4, dentro del capítulo de malos tratos): **«La
música es un aditamento impropio en los informativos diarios y, en formatos más extensos, estos
recursos deben manejarse con matices.»** (9.2.12.4, pp. 130-131).

### La limpieza de un diálogo, paso a paso

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

### La sonoridad de la pieza terminada

Limpia y mezclada, la pieza tiene que cumplir la sonoridad de la EBU R 128, que se explica en el
tema 2. Lo que fija la R 128 (versión 5, noviembre de 2023):

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

## Aplicación práctica: la postproducción de una noticia

Supuesto: pieza de 1 minuto 30 segundos para el informativo, montada con planos de dos cámaras (una
con dominante verdosa por un fluorescente), un total de un testigo grabado en la calle con tráfico y
zumbido, un total de un menor, un gráfico con cinco cifras, música de fondo en la cabecera y
locución. Orden de trabajo (oficio, con los datos de cada epígrafe):

1. Color. Primaria plano a plano mirando el desfile y el vectorscopio: negros y blancos en su sitio
   (tema 2); la dominante verdosa, con el matiz hacia magenta (es un ajuste del *gain*). Igualar
   contra el plano de referencia y comprobar que la piel cae en el mismo punto del vectorscopio.
2. Efectos. Si hay factor de riesgo, tramar la cara del menor con una máscara que la siga todo el
   plano (Libro de Estilo, 9.9). Nada de cámara lenta ni congelados para dramatizar (9.9.2).
3. Grafismo. Rótulo de identificación del testigo dentro de la zona de título; el gráfico, con no más
   de cuatro o cinco elementos y al menos ocho segundos en pantalla, con su «cama» de audio (3.16 y 3.16.2). Si
   el programa se produce en HLG, el blanco del gráfico al 75 % (BT.2408).
4. Subtítulos. Si el testigo no se entiende, subtítulo incrustado en su total, a no más de 37
   caracteres por línea y unos 15 por segundo (criterio tomado, por oficio, de la síntesis de la
   UNE 153010, que es norma de subtitulado para personas sordas, no de traducción).
5. Transiciones. Cortes; un fundido corto sólo si hay salto de tiempo, comprobando que hay colas (a
   25 imágenes por segundo, 12 o 13 cuadros por lado para un segundo centrado).
6. Audio. En el total: filtro paso alto, reductor de zumbido en 50 Hz y armónicos, reducción de ruido
   suave escuchando lo que se quita; relleno de ambiente en los cortes. La música de cabecera, bajo la
   locución con *ducking* o a mano, sin que «respire».
7. Entrega. Medir la pieza entera: −23 LUFS (±0,2 LU en postproducción, según la Tech 3343) y el
   pico verdadero que no pase de −1 dBTP. Si mide −24,5 LUFS con picos a −1,8 dBTP, limitar antes de
   subir 1,5 dB. Después, *render* y exportación (tema 3).

## Normativa y recomendaciones técnicas que el tema cita

| Documento | Qué es | Qué se toma |
|---|---|---|
| Reglamento electrotécnico para baja tensión, aprobado por el Real Decreto 842/2002, de 2 de agosto | Reglamento (norma jurídica); art. 4 en su redacción única, vigente desde el 18-09-2003 | Art. 4.4: frecuencia de la red, 50 Hz |
| Informe UIT-R BT.2408-9 (03/2026), *Guidelines for operational practices in high dynamic range television production* | Informe de la UIT-R, no recomendación | § 2.1 (blanco de referencia HDR y del grafismo, tabla 1) y § 9 (grafismo SDR en HDR) |
| EBU R 128-2023 (versión 5, noviembre de 2023) | Recomendación de la UER | Nivel objetivo, tolerancias, pico verdadero, medida del programa entero, definición de programa |
| EBU Tech 3343-2023 (versión 4) | Guía de producción de la UER para aplicar la R 128 | Tolerancia de ±0,2 LU en postproducción y corrección por ganancia estática |
| UNE 153010:2012, *Subtitulado para personas sordas y personas con discapacidad auditiva* | Norma UNE, publicada en 2012 por AENOR, según la referencia de la guía de la Universidad de Burgos | No se ha leído: sus criterios se dan por la síntesis de la Universidad de Burgos |

## Lo que este tema no da, y dónde está

- Qué sistema de edición, qué corrector de color, qué plantillas de grafismo y qué formatos de
  subtítulos y de entrega usa CSRTV: no consta en un documento publicado de la RTVA. Tampoco si los
  rótulos van incrustados desde la sala o los inserta realización en la emisión.
- El texto de la UNE 153010:2012: no se ha leído. Lo que se da es la síntesis de la
  Universidad de Burgos, que no sustituye a la norma.
- La documentación de Adobe After Effects y Photoshop (capas, precomposición, complementos,
  asistente de fotogramas clave): no se ha consultado; el tema no da sus nombres de órdenes.
- Las zonas de seguridad de una norma de la UER o de la SMPTE: no se han leído; los valores del tema
  son los que Resolve trae por defecto.
- Los monitores de histograma y de cromaticidad de la CIE: el tema no los desarrolla (el manual de
  Resolve los describe en las pp. 3152-3153).
- El contenido de los apartados del Informe BT.2408-9 sobre conversiones SDR-HDR y LUT en producción
  HDR: sólo se han leído sus títulos.
- Señal de vídeo y audio, colorimetría, niveles legales, monitores de medida, HDR y sonoridad
  (explicación completa): tema 2.
- *Render*, conformado, colas al conformar y exportación: tema 3.
- Formatos, códecs y estándares de entrega (IMF y otros): tema 4.
- Valor narrativo del corte, del fundido y de la elipsis; tratamiento informativo e imágenes duras:
  tema 1.
- Coordinación con grafismo y sonido, reglas completas del Libro de Estilo para los gráficos y
  circuito de los rótulos: tema 9.
- Obligaciones de subtitulado, audiodescripción y lectura fácil: tema 11.
- Formatos verticales y versiones para redes: tema 12.
- Plantillas y automatización: tema 13.
- Derechos de la música y de los materiales de terceros: tema 10.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual*: cap. 55 «Using Transitions», pp. 1194-1199; cap. 56 «Titles, Generators, and Stills», pp. 1213-1215; cap. 58 «Speed Effects», pp. 1254-1266; cap. 125 «Introduction to Color Grading», pp. 3086-3092 y 3095; cap. 127 «Viewers, Monitoring, and Video Scopes», pp. 3147 y 3150-3152; cap. 131 «Primaries Palette», pp. 3200-3204; cap. 150 «Using LUTs», pp. 3545-3546; cap. 181 «Fairlight FX», pp. 4091, 4094, 4096, 4101-4102 y 4121-4122; cap. 187 «Rendering Media», p. 4205; cap. 188 (entrega IMF), p. 4219 | Epígrafes 1 a 7 | 25-09-2026 |
| Adobe, ayuda de Premiere (copias de Wayback Machine): «Transitions overview» y «Audio editing with Essential Sound panel» (act. 07-01-2026) | Epígrafes 6 y 7 | 25-09-2026 |
| Unión Internacional de Telecomunicaciones, Informe UIT-R BT.2408-9 (03/2026), §§ 2.1 y 9 | Epígrafe 4 | 25-09-2026 |
| EBU R 128-2023 y EBU Tech 3343-2023 (a través de los temas 9 y 13 cerrados del puesto de Operador/a de Sonido) | Epígrafe 7 | 24-09-2026 (lectura del tema de origen) |
| Rane, RaneNote 155 (2005) y RaneNote 160 (2005) (a través del tema 5 cerrado del puesto de Operador/a de Sonido) | Epígrafe 7: filtros de corte, pendiente por orden, *ducker* | 24-09-2026 (lectura del tema de origen) |
| iZotope, *RX 11 Manual*, módulo «Spectral De-noise» (a través del tema 9 cerrado del puesto de Operador/a de Sonido) | Epígrafe 7: reducción por perfil y artefactos | 24-09-2026 (lectura del tema de origen) |
| RTVA, *Libro de Estilo de Canal Sur Televisión y Canal 2 Andalucía*, 1.ª ed., 2004: 3.2.2 (p. 46), 3.6.1 (p. 50), 3.16 (p. 57) y 3.16.2 (p. 58), 9.2.12.4 (pp. 130-131), 9.9, 9.9.1 y 9.9.2 (pp. 166-167) | Epígrafes 2, 3, 4 y 7 | 25-09-2026 |
| Universidad de Burgos, Unidad de Atención a la Diversidad, *Guía para elaborar Material Multimedia Accesible* (2020, fecha del PDF), pp. 4 a 7 (numeración impresa) | Epígrafe 5 | 25-09-2026 |
| W3C, especificaciones IMSC1, WebVTT y DFXP (portadas de w3.org/TR) | Desarrollo de las siglas IMSC1, WebVTT y DFXP | 25-09-2026 |
| Reglamento electrotécnico para baja tensión (Real Decreto 842/2002, de 2 de agosto, BOE-A-2002-18099), art. 4.4, redacción única vigente desde el 18-09-2003 | Epígrafe 7: frecuencia de la red, 50 Hz | 25-09-2026 |
| Oficio | Definición y fases del etalonaje; primaria y secundaria; lectura de la dominante en el desfile; orden de igualación; familias de efectos e incrustación; tres señales de la incrustación; canal alfa, máscara, fotogramas clave y curva; formatos gráficos y cuentas de bits; uso de subtítulos abiertos y cerrados; uso de cada transición; colas; ecualización, *ducking* manual y orden de limpieza; supuesto práctico | — |
