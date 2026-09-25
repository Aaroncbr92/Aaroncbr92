# Tema 2 del específico de Operador/a Montador/a de Vídeo · Señal de vídeo y audio

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Montador/a de Vídeo · punto 2 |
| Sirve para | Operador/a Montador/a de Vídeo de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Recomendaciones UIT-R BT.709-6 (06/2015), BT.2020-2 (10/2015) y BT.2100-3 (02/2025) e Informe UIT-R BT.2408-9 (03/2026); EBU R 103 v3.0 (2020), R 68-2000, R 128-2023 y Tech 3250 (3.ª ed., 2004); SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023, 272M-2004, ST 299-1:2009 y ST 299-2:2010. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las ediciones citadas, vigentes el 24-09-2026 y leídas el 24 y el 25-09-2026 |
| Extensión | 11.550 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); Sector de Radiocomunicaciones de la Unión Internacional de
Telecomunicaciones (UIT-R), que publica sus recomendaciones de televisión en la serie BT; Unión
Europea de Radiodifusión (EBU, *European Broadcasting Union*, que firma así sus recomendaciones);
Society of Motion Picture and Television Engineers (SMPTE); Audio Engineering Society (AES) y su
interfaz de dos canales AES3, que el sector llama AES/EBU; Comisión Internacional de la Iluminación
(CIE); definición estándar (SD), alta definición (HD) y ultra alta definición (UHD), que las recomendaciones
escriben en inglés SDTV, HDTV y UHDTV; iniciativa de cine digital (DCI, *Digital Cinema Initiatives*),
que da nombre al 4K de sala; rango dinámico
estándar (SDR) y alto rango dinámico (HDR), con sus dos curvas, la cuantificación perceptual (PQ,
*perceptual quantizer*) y la híbrida logarítmica-gamma (HLG, *hybrid log-gamma*); los tres
primarios rojo, verde y azul (RGB); la luminancia (Y) y las dos señales de diferencia de color (CB y
CR); luminancia constante (CL, *constant luminance*), no constante (NCL, *non-constant luminance*) e
intensidad constante (CI, *constant intensity*); tabla de consulta (LUT, *look-up table*); interfaz
digital serie (SDI, *serial digital interface*) y su versión de alta definición (HD-SDI); conector
coaxial de bayoneta (BNC) y conector circular de tres polos con anillo de bloqueo (XLR); codificación sin retorno a cero invertida (NRZI, *non-return to zero
inverted*); cuadro segmentado progresivo (PsF, *progressive segmented frame*); las señales de
televisión en color analógica de línea alternada en fase (PAL) y norteamericana (NTSC); la señal de
ajuste del negro de los monitores (PLUGE); código de tiempo (TC, *time code*), con y sin salto de
números (DF, *drop frame*, y NDF, *non-drop frame*); modulación por impulsos codificados (PCM), el
audio digital lineal; espacio de datos auxiliares horizontal (HANC) y su identificador de paquete (ID, en las citas); cuadros por segundo (fps);
hercio (Hz), kilohercio (kHz) y megahercio (MHz); decibelio (dB) y decibelios referidos a la escala
completa digital (dBFS); unidad de sonoridad (LU, *loudness unit*), sonoridad referida a la escala
completa (LUFS, que la UIT escribe LKFS) y pico verdadero en decibelios (dBTP, *dB true peak*);
candela por metro cuadrado (cd/m²), que en la industria se llama *nit*; megabits y gigabits por
segundo (Mb/s, Gb/s); protocolo de internet (IP).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.30, punto 2): «Conocimientos y
> fundamentos de la señal de vídeo y audio.»

Qué se puede preguntar: qué recomendación de la UIT-R rige la HD, la UHD y el HDR; cómo se forma la
luminancia a partir de RGB y con qué coeficientes; qué es la luminancia constante y la no constante;
qué es la gamma y qué hace una curva logarítmica; qué distingue el vídeo compuesto del de componentes;
por qué existe el entrelazado y cuántos cuadros hay en un 1080i a 50 campos; qué cadencias admiten la
BT.709 y la BT.2020 y por qué hay valores divididos por 1,001; qué resolución tienen HD, UHD, 8K y el
4K de cine; a qué frecuencia se muestrea la luminancia en HD y cuántas muestras de color hay por línea;
qué significa 4:2:2, 4:2:0 o 4:4:4:4; entre qué valores de código va una señal de 10 bits y qué es el
rango estrecho; qué es el *banding*; qué mide el *nit*, qué monitor pide el HDR y a qué nivel se
inserta el grafismo en HLG y en PQ; qué mide un monitor de forma de onda y qué un vectorscopio; a qué
velocidad va cada SDI, qué es el *jitter* y en qué se mide; qué señal de referencia sincroniza los
equipos de HD; qué distingue tono, intensidad y timbre; qué fijan la
frecuencia de muestreo y la profundidad de bits del audio, y cuánto rango da cada bit; a qué nivel se
alinea el audio digital según la EBU, qué sonoridad pide la R 128, con qué tolerancias, y qué pico
verdadero admite;
cuántos canales lleva la AES/EBU y cuántos van embebidos en un HD-SDI; qué código de tiempo se usa a
25 fps y por qué existe el *drop frame*. En la prueba práctica: leer en el monitor de forma de onda y
en el vectorscopio si un plano es legal, identificar el formato de un material por su notación y
dejar el audio de una pieza en la sonoridad de entrega.

<!-- indice -->

## Índice

- [1. La señal de vídeo](#1-la-señal-de-vídeo)
  - [Cómo se forma el color: tres primarios](#cómo-se-forma-el-color-tres-primarios)
  - [La colorimetría de referencia](#la-colorimetría-de-referencia)
  - [Luminancia y diferencias de color](#luminancia-y-diferencias-de-color)
  - [La gamma y la curva logarítmica](#la-gamma-y-la-curva-logarítmica)
  - [Vídeo compuesto, por componentes y digital](#vídeo-compuesto-por-componentes-y-digital)
  - [El barrido: progresivo y entrelazado](#el-barrido-progresivo-y-entrelazado)
  - [Las cadencias](#las-cadencias)
  - [Resolución y relación de aspecto](#resolución-y-relación-de-aspecto)
  - [El muestreo de la señal](#el-muestreo-de-la-señal)
  - [La cuantificación: profundidad de bits y niveles](#la-cuantificación-profundidad-de-bits-y-niveles)
  - [Los límites de la señal según la EBU](#los-límites-de-la-señal-según-la-ebu)
  - [El alto rango dinámico](#el-alto-rango-dinámico)
  - [Medir la señal](#medir-la-señal)
  - [La interfaz digital serie (SDI)](#la-interfaz-digital-serie-sdi)
  - [La referencia de sincronismo](#la-referencia-de-sincronismo)
- [2. La señal de audio](#2-la-señal-de-audio)
  - [Las cualidades del sonido](#las-cualidades-del-sonido)
  - [Del sonido analógico al digital: muestreo y cuantificación](#del-sonido-analógico-al-digital-muestreo-y-cuantificación)
  - [Los niveles del audio digital: escala completa y alineación](#los-niveles-del-audio-digital-escala-completa-y-alineación)
  - [La sonoridad: EBU R 128](#la-sonoridad-ebu-r-128)
  - [La interfaz AES/EBU](#la-interfaz-aesebu)
  - [El audio dentro del vídeo: embebido en SDI](#el-audio-dentro-del-vídeo-embebido-en-sdi)
- [3. Vídeo y audio juntos: código de tiempo y sincronía](#3-vídeo-y-audio-juntos-código-de-tiempo-y-sincronía)
  - [El código de tiempo](#el-código-de-tiempo)
  - [La sincronía entre imagen y sonido](#la-sincronía-entre-imagen-y-sonido)
- [Recomendaciones y normas técnicas que el tema cita](#recomendaciones-y-normas-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. La señal de vídeo

### Cómo se forma el color: tres primarios

El ojo humano tiene tres tipos de conos, sensibles a zonas distintas del espectro visible. De
ahí sale todo lo demás: como la percepción del color se reduce a tres respuestas, basta con tres
estímulos para reproducir cualquier color percibido. Eso es la síntesis aditiva, y es el
principio sobre el que funciona una pantalla.

Las leyes de Grassmann son las que formalizaron esa idea en el siglo XIX. La formulación y el orden
varían de un manual a otro; en el reparto más extendido son éstas (oficio):

| Ley | Qué dice |
|---|---|
| Primera | Hacen falta tres estímulos independientes —ninguno obtenible de los otros dos— para igualar cualquier color |
| Segunda | Un color se puede sustituir por su mezcla equivalente sin que la igualación cambie |
| Tercera | La suma de dos mezclas equivalentes sigue siendo equivalente: la igualación es aditiva |
| Cuarta | La intensidad de una mezcla es la suma de las intensidades de sus componentes |

La palabra que identifica la primera es «independientes»: que ninguno de los tres primarios se pueda
obtener mezclando los otros dos.

Un color espectral es el que corresponde a una sola longitud de onda del espectro visible: los que
se ven al descomponer la luz blanca en un prisma, del violeta al rojo.

Un color no espectral es el que no corresponde a ninguna longitud de onda, y sólo se percibe
mezclando los dos extremos del espectro.

Los colores no espectrales son el púrpura y el magenta. En el diagrama de cromaticidad de la CIE,
los colores espectrales forman la herradura y los púrpuras y magentas están en la recta que cierra sus
dos extremos, la «línea de los púrpuras» (oficio).

### La colorimetría de referencia

El color de la televisión no es libre: lo fijan las recomendaciones de la UIT-R. La BT.709-6, la de
la alta definición, fija sus primarios —rojo (0,640; 0,330), verde (0,300; 0,600), azul (0,150;
0,060)— y un blanco «**D65**» (0,3127; 0,3290). La BT.2020-2, la de la ultra alta definición, usa
primarios más saturados —rojo (0,708; 0,292), verde (0,170; 0,797), azul (0,131; 0,046)— con el
mismo blanco D65, y la BT.2100-3, la del HDR, usa los mismos primarios que la BT.2020. Un monitor
ajustado a una de ellas no enseña bien el material de la otra (oficio).

La luminancia se forma pesando los tres primarios, y los pesos cambian con la recomendación:

| Recomendación | Para qué | R | G | B |
|---|---|---|---|---|
| UIT-R BT.601 | Definición estándar | 0,299 | 0,587 | 0,114 |
| UIT-R BT.709 | Alta definición | 0,2126 | 0,7152 | 0,0722 |
| UIT-R BT.2020 | Ultra alta definición | 0,2627 | 0,6780 | 0,0593 |

El verde aporta la mayor parte del brillo percibido y el azul la menor. Ésa es la razón de que un
error en el canal azul se note mucho menos que el mismo error en el verde (se deduce de los
coeficientes).

La BT.709-6 recuerda que el aspecto final se juzga en un monitor de referencia: «**In typical
production practice the encoding function of image sources is adjusted so that the final picture has
the desired look, as viewed on a reference monitor having the reference decoding function of
Recommendation ITU-R BT.1886**».

La cadena para no confundirlas: 601 estándar · 709 alta · 2020 ultra alta · 2100 alto rango
dinámico.

### Luminancia y diferencias de color

La televisión no transmite rojo, verde y azul. Transmite una señal de luminancia y dos de
diferencia de color, porque el ojo distingue mucho mejor los detalles de brillo que los de color, y
eso permite dedicar menos ancho de banda al color sin que se note.

La BT.709-6 admite las dos formas: la señal codificada es «**R, G, B or Y, CB, CR**» (punto 4.1). La
luminancia de la alta definición es Y = 0,2126 R + 0,7152 G + 0,0722 B (punto 3.2, «**Derivation of
luminance signal**»); las dos diferencias de color se obtienen restando la luminancia al azul y al
rojo y escalando el resultado (punto 3.3). Un control rápido para no confundir ternas: los tres
coeficientes de cada recomendación suman uno (cálculo: 0,2126 + 0,7152 + 0,0722 = 1).

Luma constante y no constante. La diferencia está en el orden de las operaciones:

| Sistema | Orden de las operaciones |
|---|---|
| Luma constante (CL) | Primero se calcula Y a partir del RGB lineal, y después se corrige la gamma |
| Luma no constante (NCL) | Primero se corrige la gamma de cada primario, y después se calcula Y' a partir del R'G'B' ya corregido |

Por qué existen las dos. La luma constante es la correcta desde el punto de vista de la
colorimetría: al calcular la luminancia sobre señales lineales, Y contiene toda la información de
brillo y las señales de diferencia de color no arrastran nada de ella. La no constante es la que
se usa en la práctica, porque es la que heredó toda la cadena de radiodifusión desde la televisión
en color analógica, y cambiarla obligaría a cambiarlo todo.

La consecuencia visible del sistema no constante: una parte de la luminancia se cuela por los
canales de color, y cuando esos canales se submuestrean —4:2:2, 4:2:0— se pierde brillo en los
colores muy saturados (oficio).

La BT.2020-2 ofrece las dos variantes y dice cuándo usar cada una (notas al cuadro 4): la constante,
«**Constant luminance Y'CC'BCC'RC may be used when the most accurate retention of luminance
information is of primary importance or where there is an expectation of improved coding efficiency
for delivery**»; la no constante, «**Conventional non-constant luminance Y'C'BC'R may be used when use
of the same operational practices as those in SDTV and HDTV environments is of primary importance
through a broadcasting chain**». La BT.2100-3, para el HDR, sustituye la luminancia constante por un
formato de intensidad constante (ICTCP) y deja claro cuál manda: «**The Non-Constant Luminance (NCL)
format is in widespread use and is considered the default. The Constant Intensity (CI) format is newly
introduced in this Recommendation and should not be used for programme exchange unless all parties
agree.**»

### La gamma y la curva logarítmica

La gamma es la relación no lineal entre el valor codificado de una señal y la luz que finalmente
sale de la pantalla. Existe porque el ojo no percibe el brillo linealmente: distingue mucho
mejor los cambios en las zonas oscuras que en las claras. Codificar linealmente sería malgastar
bits en las luces y quedarse corto en las sombras.

La BT.709-6 fija la característica de transferencia de la fuente (punto 1.2): V = 1,099 L^0,45 −
0,099 para 1 ≥ L ≥ 0,018, y V = 4,500 L para 0,018 > L ≥ 0, donde L es la luminancia de la imagen
(de 0 a 1) y V la señal eléctrica; y en el punto 3.1 resume esa precorrección no lineal con el
exponente «**0.45**». El tramo recto junto al negro evita que la curva amplifique sin límite el
ruido de las sombras (oficio). Del exponente 0,45, que es aproximadamente la inversa de 2,2, sale la
«gamma de 2,2» que se cita en el oficio. En la pantalla, la función de referencia es la de la
Recomendación UIT-R BT.1886, que la BT.709 cita (véase «La colorimetría de referencia»).

Las curvas logarítmicas son otra cosa, y son de rodaje, no de emisión. Un plano capturado con
una curva de gamma logarítmica genera una imagen más lavada que necesita de un proceso posterior de
corrección de color (oficio). Por qué sale lavada:

- La curva logarítmica reparte los valores disponibles a lo largo de todo el rango dinámico del
  sensor, en lugar de concentrarlos donde quedarían bien a la vista.
- El resultado es una imagen de bajo contraste y baja saturación: gris, plana, «lavada».
- Pero conserva información en las altas luces y en las sombras que una curva de emisión habría
  recortado.
- Por eso exige etalonaje: la imagen logarítmica es material de trabajo, no imagen final.

Y lo que no es: no es el RAW, que recoge directamente lo que genera el sensor; la curva logarítmica
ya es una codificación (oficio). Las curvas del HDR (PQ y HLG) se ven en «El alto rango dinámico».

### Vídeo compuesto, por componentes y digital

| Señal | Cómo va | Cómo se transporta |
|---|---|---|
| Compuesto | Luminancia y crominancia mezcladas en una sola señal, con el color modulado en amplitud sobre una subportadora | Un solo cable |
| Por componentes | Tres señales separadas: luminancia y las dos diferencias de color | Tres cables, o un multipar |
| Digital | Muestreada y cuantificada, serializada | Un coaxial de 75 Ω por SDI, o fibra, o red |

El tipo de señal de vídeo que utiliza la modulación de amplitud es el vídeo compuesto. En el sistema
PAL —y en el NTSC— la información de color se modula sobre una subportadora que se suma a la
luminancia, y esa modulación es en amplitud, con la fase llevando el tono y la amplitud llevando la
saturación. Eso es lo que define la señal compuesta, y es de donde vienen los defectos clásicos de la
televisión analógica en color (oficio). La señal por componentes, en cambio, no modula: lleva las tres
señales separadas y en banda base; y en digital no hay modulación de la crominancia: hay muestras.

### El barrido: progresivo y entrelazado

En el barrido progresivo cada imagen se dibuja entera, línea por línea. En el entrelazado, cada
imagen se dibuja en dos pasadas: primero las líneas impares y después las pares. Cada pasada es un
campo, y dos campos forman un cuadro.

En el sistema PAL el barrido entrelazado es necesario para evitar el parpadeo de la imagen de
televisión. El razonamiento del que salió el entrelazado, en tres pasos:

1. Con 25 imágenes completas por segundo, el movimiento se ve fluido pero la pantalla parpadea:
   el ojo detecta el refresco.
2. Con 50 imágenes completas por segundo no parpadearía, pero haría falta el doble de ancho de
   banda, que en la televisión analógica no había.
3. El entrelazado da 50 refrescos por segundo con la información de 25 imágenes: se refresca media
   imagen cada vez. Se elimina el parpadeo sin gastar más banda.

La alta definición conserva las dos exploraciones. La BT.709-6 lo dice así: «**Pictures are defined
for progressive (P) capture and interlace (I) capture. Progressive captured pictures can be
transported with progressive (P) transport or progressive segmented frame (PsF) transport. Interlace
captured pictures can be transported with interlace (I) transport.**» En su tabla de exploración
(punto 5), el sistema «50/I» tiene una frecuencia de campo de 50 Hz, una relación de entrelazado de
2:1 y una frecuencia de imagen de 25 Hz; y todos los sistemas tienen «**1 125**» líneas en total (punto 5.2), de
las que «**1 080**» son activas (punto 2.4).

El cuadro segmentado (PsF) no es entrelazado aunque lo parezca. La BT.709-6 lo define en su anexo 2:
«**a picture has been captured in a progressive mode, and transported as two segments. One segment
containing the odd lines of the progressive image, the second segment containing the even lines of
the progressive image.**» Es una forma de transporte, no de captación: «**PsF is an interface
technology not an image capture or processing technology.**» Y «**The digital interface of an
interlace signal and a PsF signal are common, only the signal content is different.**» Un 25PsF es,
pues, una imagen progresiva de 25 cuadros que viaja por la misma interfaz que un 50i.

La lectura de la notación 1080i50 o 1080 50i: «1080» son las líneas activas, «50» es el número de
campos por segundo e «i» significa entrelazado. Cincuenta campos por segundo son veinticinco cuadros
completos, y cada campo es una imagen que llega a la pantalla (oficio). Si fueran cincuenta cuadros
completos, la notación sería 1080p50. La BT.709-6 llama a ese mismo formato «25 interlace» en la tabla
de combinaciones de su parte 2, porque cuenta cuadros; el oficio dice «50i» porque cuenta campos: los
dos nombres designan la misma señal.

La ultra alta definición y el HDR ya no entrelazan. La BT.2020-2 da como modo de exploración sólo
«**Progressive**», y la BT.2100-3, «**Image Format Progressive**».

Qué supone para el montador (oficio): el material entrelazado se monta respetando el orden de los
campos, y cualquier operación que mueva o escale la imagen (una ralentización, un reencuadre) sobre
material entrelazado puede dar peines o temblores en los bordes horizontales si no se desentrelaza
antes.

### Las cadencias

La cadencia es cuántas imágenes por segundo tiene la señal. Las recomendaciones de la UIT-R las
fijan:

- BT.709-6, parte 2: «**The following picture rates are specified: 60 Hz, 50 Hz, 30 Hz, 25 Hz and 24
  Hz. For the 60, 30 and 24 Hz systems, picture rates having those values divided by 1.001 are also
  specified**».
- BT.2020-2, tabla 2: «**Frame frequency (Hz) 120, 120/1.001, 100, 60, 60/1.001, 50, 30, 30/1.001, 25,
  24, 24/1.001**». La BT.2100-3 da la misma lista.

Dos consecuencias. Los valores divididos por 1,001 (29,97 o 59,94) sólo existen en las familias de
24, 30, 60 y 120 Hz, que vienen de la televisión norteamericana (oficio): las de 25, 50 y 100 Hz son enteras,
y de ahí sale el código de tiempo sin salto (§ 3). Y la cadencia no se elige al azar: «**The choice of
frame frequency may be influenced by the frequency of the mains power and the type of scene lighting
in use**» (BT.2020-2). Con la red europea de 50 Hz, las cadencias de trabajo son 25 y 50 (oficio);
un material de 29,97 que entra en un montaje de 25 obliga a convertir la cadencia, con el riesgo de
saltos en el movimiento (oficio).

El paso de 24 a 25 es el caso sencillo, y la BT.709-6 lo describe para el cine transferido: «**The 25
Hz frame rate copy may be created by simply playing back the 24 Hz film rate original at the slightly
faster 25 Hz rate; there is no picture quality loss.**» (anexo 2). La imagen no pierde calidad, pero
todo dura un 4 % menos y el sonido, si se acelera con ella, sube de tono (cálculo y oficio: 24/25 =
0,96).

### Resolución y relación de aspecto

La resolución espacial es cuántos píxeles tiene la imagen; la relación de aspecto es la proporción
entre su ancho y su alto. Son dos cosas distintas.

| Formato | Píxeles (horizontal × vertical) | Relación de aspecto |
|---|---|---|
| Definición estándar (PAL) | 720 × 576 | 4:3 o 16:9 |
| HD | 1.280 × 720 | 16:9 |
| Full HD | 1.920 × 1.080 | 16:9 |
| UHD o 4K de televisión | 3.840 × 2.160 | 16:9 |
| 4K DCI, de cine | 4.096 × 2.160 | 1,90:1 |
| 8K | 7.680 × 4.320 | 16:9 |

Lo que tiene norma leída: la BT.709-6 da para la alta definición «**16:9**», «**1 920**» muestras por
línea activa, «**1 080**» líneas activas y «**1:1 (square pixels)**» (punto 2); la BT.2020-2 da los
dos formatos de la UHD, «**7 680 × 4 320**» y «**3 840 × 2 160**», también en 16:9; y la BT.2100-3
recoge los tres (7 680 × 4 320, 3 840 × 2 160 y 1 920 × 1 080) con «**Pixel aspect ratio 1:1 (square
pixels)**». Las filas de la definición estándar, el 1.280 × 720 y el 4K de cine son oficio.

Lo que la UHD multiplica es el número de píxeles, no la forma de la pantalla: su relación de aspecto
es la misma 16:9 de la HD.

La confusión que hay que deshacer: «4K» no es una sola cosa. El 4K de televisión —UHD— es
3.840 × 2.160 y es 16:9; el 4K de cine —DCI— es 4.096 × 2.160 y no es 16:9.

Y un consejo de la propia UIT-R que vale para la sala de montaje: «**Productions should use the
highest resolution image format that is practical. […] producing in a higher resolution format, and
then electronically down-sampling for distribution, yields superior quality than producing at the
resolution used for distribution.**» (BT.2100-3, nota 1b). Montar en UHD y entregar en HD da mejor
resultado que montar directamente en HD; al revés no se gana nada: escalar un HD a UHD no crea
detalle (oficio).

### El muestreo de la señal

Digitalizar la imagen es tomar muestras de cada línea a una frecuencia fija. La BT.709-6 fija la de
la alta definición (punto 5.8): la luminancia se muestrea a «**148.5**» MHz en el sistema 50/P y a
«**74.25**» MHz en los sistemas 50/I y 25/P, y las diferencias de color, a la mitad (punto 5.9 y su nota 2):
«**CB, CR sampling frequency is half of luminance sampling frequency.**» Por eso cada línea activa tiene «**1 920**»
muestras de luminancia y «**960**» de cada diferencia de color (punto 4.4), y las de color van
«**co-sited with each other and with alternate Y samples**» (punto 4.3): una muestra de color por cada dos de
luminancia en horizontal, que es lo que la notación llama 4:2:2.

La cuenta que casa las cifras (cálculo): en los sistemas de 50 Hz la línea completa tiene «**2 640**»
muestras (punto 5.6) y la imagen, 1.125 líneas; 2.640 × 1.125 × 50 = 148.500.000 muestras por
segundo en 50/P, y la mitad, 74,25 millones, en 50/I y 25/P, que sólo tienen 25 imágenes completas por
segundo.

El muestreo cromático dice cuántas muestras de color se guardan por cada muestra de luminancia.
Se escribe con tres o cuatro cifras, y cada una cuenta muestras en un bloque de referencia de cuatro
píxeles de ancho por dos de alto.

| Notación | Qué guarda | Dónde se usa |
|---|---|---|
| 4:4:4 | Una muestra de color por cada píxel: sin submuestreo | Grafismo, croma, cine digital |
| 4:2:2 | La mitad de muestras de color en horizontal | El estándar de producción de televisión |
| 4:2:0 | La mitad en horizontal y la mitad en vertical | Emisión y distribución: ahorra la mitad del color |
| 4:1:1 | Una cuarta parte en horizontal | Formatos antiguos de definición estándar |

Las tres primeras tienen definición en la BT.2100-3: en 4:4:4 cada componente de color tiene «**the
same number of horizontal samples as the Y' or I component**»; en 4:2:2 está «**Horizontally
subsampled by a factor of two**»; en 4:2:0, «**Horizontally and vertically subsampled by a factor of
two**» respecto de la luminancia. La columna «Dónde se usa» y la fila 4:1:1 son oficio.

El submuestreo cromático reduce la resolución de los componentes de la crominancia para disminuir el
tamaño de los archivos sin una pérdida significativa de calidad. Funciona porque el ojo distingue
mucho mejor los detalles de brillo que los de color (oficio).

El submuestreo limita lo que se puede hacer después: un croma sobre material 4:2:0 recorta mal,
porque el borde del recorte se calcula sobre información de color que no está. Por eso el material
destinado a incrustación se graba en 4:2:2 como mínimo, y mejor en 4:4:4 (oficio).

Y una cuarta cifra puede aparecer. Un archivo de vídeo con muestreo cromático 4:4:4:4 significa que
tiene una señal de vídeo RGB sin submuestreo de color más información del canal alfa. Qué es el canal
alfa: un cuarto canal que dice, píxel a píxel, cuánto de opaco es. No lleva color: lleva
transparencia. Es lo que permite superponer un rótulo o un elemento de grafismo sobre otra imagen sin
recortarlo a mano. Cuando un muestreo lleva cuarta cifra, ésa es la del canal alfa (oficio).

### La cuantificación: profundidad de bits y niveles

La profundidad de bits es con cuántos niveles se anota cada muestra de la señal: ocho bits dan 256
niveles por canal, diez bits dan 1.024 y doce bits dan 4.096 (cálculo: 2 elevado al número de bits).

Con más bits hay más niveles de brillo, más colores posibles, degradados más suaves y archivos más
pesados. El defecto que evita es el bandeado (*banding*): escalones visibles en un degradado suave,
como un cielo o una pared lisa. La profundidad de bits no crea rango dinámico —ése lo determina el
sensor—, pero lo hace utilizable: al codificar un rango amplio con pocos bits, los escalones se
hacen tan grandes que el rango deja de ser aprovechable (oficio).

Resolución espacial es cuántos píxeles hay; profundidad de color es cuántos valores puede tomar
cada uno. El *banding* es un problema de la segunda, no de la primera.

Lo que admite cada recomendación:

| Recomendación | Profundidad |
|---|---|
| BT.709-6 (HD) | «**Linear 8 or 10 bits/component**» (punto 4.5) |
| BT.2020-2 (UHD) | «**10 or 12 bits per component**» |
| BT.2100-3 (HDR) | «**n = 10, 12 bits per component**» (tabla 9) |

La HD admite 8 bits; la UHD y el HDR, no: su mínimo es 10.

No todos los valores de código son imagen. La BT.709-6 (puntos 4.6 y 4.7) reserva un margen por
debajo del negro y por encima del blanco, y los códigos de los extremos para las señales de
sincronismo:

| Nivel (BT.709-6) | 8 bits | 10 bits |
|---|---|---|
| Negro (R, G, B, Y) | «**16**» | «**64**» |
| Blanco de pico nominal (R, G, B, Y) | «**235**» | «**940**» |
| Acromático, sin color (CB, CR) | «**128**» | «**512**» |
| Extremos de las diferencias de color (CB, CR) | «**16 and 240**» | «**64 and 960**» |
| Datos de vídeo | «**1 through 254**» | «**4 through 1 019**» |
| Referencia de sincronismo (*timing reference*) | «**0 and 255**» | «**0-3 and 1 020-1 023**» |

La BT.2100-3 llama a esa forma de codificar «rango estrecho» y la hace la norma general: negro en
64 (10 bits) o 256 (12 bits) y pico nominal en 940 o 3.760 (tabla 9). Admite también un «rango
completo» (negro en 0; pico en 1.023 o 4.095), con una salvedad: «**The narrow range representation
is in widespread use and is considered the default. The full range representation is newly
introduced in this Recommendation and should not be used for programme exchange unless all parties
agree.**» En la sala, un material que se ve lavado o con los negros hundidos después de pasar por
otro programa suele ser una confusión entre rango estrecho y completo al leerlo o al exportarlo
(oficio).

### Los límites de la señal según la EBU

La exposición tiene un techo y un suelo que no son del operador: son de la señal. EBU R 103 v3.0
recomienda que «**the RGB components and the corresponding Luminance (Y) signal should not normally
exceed the "Preferred Minimum/Maximum" range of digital sample levels in Table 1**» (Anexo 1). Su
tabla 1, en valores de código:

| Bits | Nominal Video Range | Preferred Min./Max. | Total Video Signal Range |
|---|---|---|---|
| 8-bit | **16 - 235** | **5 - 246** | **1 - 254** |
| 10-bit | **64 - 940** | **20 - 984** | **4 - 1019** |
| 12-bit | **256 - 3760** | **80 - 3936** | **16 - 4079** |
| 16-bit | **4096 - 60160** | **1280 - 62976** | **256 - 65279** |

Cómo se lee: el rango nominal va del negro (64 en 10 bits) al blanco de pico nominal (940), los
mismos valores de negro y pico que fija la Recomendación UIT-R BT.709-6 para 10 bits (en 8 bits, 16
y 235). El rango preferente deja un margen por debajo y por encima. Lo que se sale de él es un error:
«**Any signals outside the "Preferred Minimum/Maximum" range are described as having a gamut error
(or as being out-of-gamut). Signals shall not exceed the "Total Video Signal Range", overshoots that
attempt to "exceed" these values may clip.**» Los instrumentos no deben avisar por cualquier punto:
«**measuring equipment should indicate an "Out-of-Gamut" occurrence only after the error exceeds 1%
of the image**».

Para el directo, la recomendación habla al control de cámaras: «**Care should be taken with live
productions, especially those with uncontrolled lighting, to prevent clipping of highlights during
temporary excursions to extremes of code values, i.e. camera clippers should be set to Preferred
Range limits (as per this document). For pre-produced and colour graded material, the nominal limits
contained in this document should be followed closely.**»

Tres avisos más de R 103:

- El recorte tiene un precio: la señal que excede el rango total se recorta, y ese recorte «**can cause harmonic distortion and alias
  artefacts in the video signal, which manifests as compression artefacts and the potential for
  increased data rates**».
- Los legalizadores automáticos, con cuidado: «**colour gamut "legalisers" should be used with
  caution as they may create artefacts in the picture that are more disturbing than the gamut errors
  they are attempting to correct**».
- Los negros por debajo del negro no se tiran: «**clipping of sub-blacks prevents the alignment of
  monitors with the PLUGE signal**» (Anexo 2). En analógico, «**the normal range corresponds to 0 mV
  to 700 mV luminance amplitude**».

Un aviso de estudio: los porcentajes de «−1 %» y «103 %» que circulan en manuales como límites «de
la EBU» no aparecen en la versión 3.0 de R 103, que se expresa en valores de código. No se deben
atribuir a esa recomendación.

Para el montador la frase que manda es la del material preproducido: una pieza montada y corregida
de color se entrega dentro de los límites nominales, no de los preferentes, que son el margen del
directo (se deduce de la última cita de R 103).

### El alto rango dinámico

El alto rango dinámico amplía la distancia entre el negro más oscuro y el blanco más brillante que
una imagen puede representar. No es más resolución: es más recorrido de brillo, y con él más
detalle en las luces y en las sombras a la vez.

La unidad del brillo de una pantalla es la luminancia, que se mide en candelas por metro cuadrado; la
industria la llama *nit* (oficio):

| Unidad | Qué mide | Nota |
|---|---|---|
| *Nit* | Luminancia: una candela por metro cuadrado | Es el nombre de industria de la cd/m² |
| Candela | Intensidad luminosa de una fuente | No incluye la superficie: no es luminancia |
| Candela por centímetro cuadrado | Luminancia, pero en otra escala: 1 cd/cm² = 10.000 nits | No es la unidad de uso |
| Lumen | Flujo luminoso total emitido | Es lo que se mide en un proyector, no en una pantalla |

La Recomendación UIT-R BT.2100-3 fija para el HDR dos curvas: «**the Perceptual Quantization (PQ)
or Hybrid Log-Gamma (HLG) specifications described in this Recommendation should be used**». La HLG
es la que mejor convive con lo que ya existe: «**The HLG specification offers a degree of
compatibility with legacy displays by more closely matching the previously established television
transfer curves.**»

La misma nota explica la otra: «**The PQ specification achieves a very wide range of brightness
levels for a given bit depth using a non-linear transfer function that is finely tuned to match the
human visual system.**» La PQ es absoluta (oficio): cada valor de código corresponde a una luminancia
en pantalla, y su fórmula llega hasta 10.000 cd/m² (el valor figura en la ecuación de la BT.2100-3); la
SMPTE la publica como ST 2084, «**High Dynamic Range Electro-Optical Transfer Function of Mastering
Reference Displays**». La HLG es relativa: se adapta al brillo de cada pantalla (oficio).

| | PQ | HLG |
|---|---|---|
| Referencia | Luminancia absoluta en la pantalla | Relativa al pico de cada pantalla (oficio) |
| Compatibilidad con pantallas SDR | No se declara | «**a degree of compatibility with legacy displays**» |
| Uso habitual | Máster y plataformas (oficio) | Directo y emisión (oficio) |

La referencia de exposición en HDR es el blanco de referencia: «**HDR Reference White is the
nominal signal level obtained from an HDR camera and a 100% reflectance white card resulting in a
nominal luminance of 203 cd/m2 on a PQ display or on an HLG display that has a nominal peak
luminance capability of 1 000 cd/m2.**» (BT.2100-3, nota 10a).

El Informe UIT-R BT.2408-9 (marzo de 2026) da ese nivel en porcentaje de señal, y es el dato que el
montador necesita para insertar grafismo: «**Graphics White is defined within the scope of this
Report as the equivalent in the graphics domain of a 100% reflectance white card […]. It therefore has
the same signal level as HDR Reference White, and graphics should be inserted based on this level.**»
Su tabla 1:

| Referencia (BT.2408-9) | cd/m² | % PQ | % HLG |
|---|---|---|---|
| Carta gris del 18 % | 26 | 38 | 38 |
| Máximo de la carta de grises (83 %) | 162 | 56 | 71 |
| Máximo de la carta de grises (90 %) | 179 | 57 | 73 |
| Blanco de referencia HDR (100 %), que es también el blanco difuso y el blanco del grafismo | 203 | 58 | 75 |

Con dos notas: «**The actual signal levels for an 18% grey card may differ significantly where camera
painting controls have been applied.**» y «**The signal level of 'HDR Reference White' is not
directly related to the signal level of SDR 'peak white'.**» Es decir: en HDR el blanco de un rótulo
no va al 100 % de la señal, sino al 75 % en HLG o al 58 % en PQ; lo que queda por encima es para los
brillos especulares (oficio, sobre la tabla).

El monitor también cambia. La BT.2100-3 fija para el visionado crítico de HDR (tabla 3) un pico de
luminancia de «**≥ 1 000 cd/m2**» y un negro de «**≤ 0.005 cd/m2**», con la precisión de que el pico
se exige «**for small area highlights**», no para toda la pantalla en blanco. Una pantalla de rango
dinámico estándar trabaja alrededor de 100 nits (oficio). De ahí una regla de sentido común
profesional: para etalonar en HDR un máster con salida en HDR se necesita un monitor HDR; no se puede
juzgar lo que no se ve.

La gama de color y el rango dinámico son dos ejes distintos. Se puede tener gama amplia con rango
estándar, y al revés. La BT.2020 amplía qué colores; la BT.2100, además, cuánto brillo (oficio).

### Medir la señal

La señal se comprueba con instrumentos, no a ojo. Los tres básicos, que llevan los sistemas de
edición y los monitores de la sala (oficio):

| Instrumento | Qué mide | Qué se ve en él |
|---|---|---|
| Monitor de forma de onda | La luminancia, línea a línea | Un perfil del brillo, con el pedestal de negros abajo y el blanco arriba |
| Vectorscopio | La crominancia: tono y saturación | Un diagrama polar con las cajas de los seis colores de barras |
| Histograma | El reparto estadístico de los niveles | Cuántos píxeles hay en cada nivel |

La regla que separa los dos primeros: la forma de onda dice si la exposición está bien; el
vectorscopio dice si el color está bien. Son dos preguntas distintas y hacen falta los dos (oficio).

El vectorscopio es el instrumento del color: el ángulo alrededor del centro es el tono y la distancia
al centro es la saturación. El centro es la ausencia de color, así que una imagen en blanco y negro
se ve como un punto en el centro y una imagen con dominante se ve como un punto desplazado hacia el
color de la dominante (oficio). Una carta blanca bien balanceada queda en el centro; si se aparta,
el balance está mal.

Un monitor de referencia añade funciones que un monitor de consumo no tiene (oficio):

| Función | Qué hace |
|---|---|
| *Blue only* | Muestra sólo el canal azul en blanco y negro. Sirve para ajustar croma y fase con barras de color, y para ver el ruido |
| *Underscan* | Muestra la imagen completa, incluidos los bordes que un monitor normal recorta |
| Marcadores y zonas de seguridad | Dibujan los límites de título y de acción |
| Falso color y cebras | Señalan zonas por su nivel de exposición |

Y las señales de prueba permiten comprobar la cadena con una imagen conocida (oficio): las barras de
color, para el ajuste de croma, fase y nivel; la rampa o diente de sierra, una subida lineal del
negro al blanco que en el monitor de forma de onda dibuja una diagonal recta y delata cualquier
curvatura o escalón.

En la sala, el monitor de forma de onda se lee contra los valores de código de la EBU: en 10 bits,
un negro que baja de 64 o un blanco que pasa de 940 está fuera del rango nominal, y todo lo que pasa
de 984 o baja de 20 es error de gama (tabla de R 103). El vectorscopio, contra las cajas de las
barras: un color que se sale de ellas está sobresaturado (oficio). Y la señal HDR se mide con escala
HDR: el blanco de un rótulo HLG debe caer en el 75 % (tabla de la BT.2408-9).

### La interfaz digital serie (SDI)

La señal digital sale de la cámara, del servidor o de la estación de edición por la interfaz digital
serie: un solo cable coaxial que lleva en serie las muestras de vídeo, el audio embebido y los datos
auxiliares (oficio; el audio embebido, en el § 2). La SMPTE la ha ido ampliando por velocidades:

| Norma SMPTE | Para qué | Velocidad (cita) |
|---|---|---|
| ST 259:2008 | SD-SDI | «**a 10-bit serial digital interface operating at 143/270/360 Mb/s**»; la de uso, «**nominally 270 Mb/s for 13.5-MHz luma sampling**» |
| ST 292-1:2018 | HD-SDI | «**The total data rate shall be either 1.485 Gb/s or 1.485/1.001 Gb/s**» |
| ST 424:2012 | 3G-SDI | «**total payload of 2.970 Gb/s or 2.970/1.001 Gb/s**» |
| ST 2082-1:2023 | 12G-SDI | «**serial data rate of 11.88 Gb/s or 11.88/1.001 Gb/s**» |

Las tres primeras constan en el catálogo de la SMPTE como estabilizadas; la ST 2082-1, como activa.
Lo que tienen en común:

- El cable y el conector: coaxial de 75 Ω con BNC. La ST 292-1: «**The male and female connectors
  shall be 75-ohm BNC as defined in IEC 61169-8**»; el generador tiene «**an unbalanced output
  circuit with a source impedance of 75 ohms**».
- La codificación: «**The channel coding scheme shall be scrambled NRZI (non-return to zero
  inverted)**» (ST 424; la ST 259 dice «**The channel coding shall be scrambled NRZI.**»).
- La atenuación que admite el receptor, que es lo que fija el alcance de un cable: en la ST 259,
  «**Typical loss amounts may be in the range of 20 dB to 30 dB at one-half clock frequency**»; en la
  ST 424, «**up to 30 dB at one-half the clock frequency**»; en la ST 2082-1, «**up to 40 dB at
  one-half the clock frequency**». Cuanto más rápida la interfaz, más atenúa el mismo cable, y menos
  metros alcanza (oficio).

Qué SDI lleva qué. Las velocidades salen de las frecuencias de muestreo de la BT.709-6 (cálculo): en
4:2:2 por cada muestra de luminancia viaja una de color, así que a 74,25 MHz y 10 bits son 74,25 × 2 ×
10 = 1.485 Mb/s, el HD-SDI; a 148,5 MHz (el 1080p50), el doble, 2.970 Mb/s, el 3G-SDI; y un UHD
2160p50, con cuatro veces más píxeles, 11.880 Mb/s, el 12G-SDI. Por eso un 1080i50 o un 1080p25 caben
en un HD-SDI, un 1080p50 pide 3G-SDI y un 2160p50 pide 12G-SDI o varios cables de menor velocidad en
paralelo (esa solución de cuatro cables tiene su propia norma, que no se ha leído).

El *jitter* aplicado a una señal digital significa una cadena de bits con tiempos inestables. Qué
es, en una frase: la variación del instante en que llega cada bit respecto de cuándo debería llegar.
No cambia el valor de los bits: cambia cuándo aparecen.

Por qué importa en una sala de edición: el receptor de una señal digital recupera el reloj de la
propia señal. Si los flancos no llegan cuando toca, el receptor decide mal dónde está cada bit, y
el resultado no es una degradación suave sino un corte: la señal se ve o no se ve. El vídeo
digital falla de golpe, y el *jitter* es una de las causas (oficio). El *jitter* es ruido, pero de
fase, no de amplitud: no es una modulación, ni un aumento de la amplitud, ni el ruido corriente.

Cómo se mide. La ST 292-1 remite a otra norma de la SMPTE: **«The jitter in the timing of the
transitions of the data signal shall be measured in accordance with SMPTE RP 184»** (8.1.8), y da en su
tabla 3 los valores que la salida HD-SDI debe cumplir. Se expresan en intervalos unitarios, **«UI =
unit interval»**: la duración de un bit (oficio), de modo que el *jitter* se cuenta en fracciones de
bit y no en voltios ni en decibelios. La tabla distingue dos:

| Tabla 3 de la ST 292-1 | Límite | Banda en que se mide (borde inferior) |
|---|---|---|
| **Timing jitter** (*jitter* de temporización) | **1 UI** | **10 Hz** |
| **Alignment jitter** (*jitter* de alineación) | **0.2 UI** | **100 kHz** |

El borde superior de la banda es el mismo para los dos, **«> 1/10 the clock rate»**, y la señal de
prueba, las barras de color: **«Color bars are chosen as a non-stressing test signal for jitter
measurements»** (nota 2). La RP 184 no se ha leído.

La transmisión de estas señales sobre redes IP (SMPTE ST 2110) y los formatos de fichero se estudian
en el tema 4.

### La referencia de sincronismo

Para que los equipos de una instalación (cámaras, mezclador, servidores, estaciones de edición)
cambien de fuente sin saltos, todos deben ir a un mismo compás: se enganchan a una señal de
referencia común que reparte la instalación (oficio). En la HD, esa señal la prevé la propia
BT.709-6 en su parte 6, «Analogue tri level sync signal»: **«The tri level sync signal may be used as
a reference signal for synchronization of devices operating on this Recommendation.»**

Sus parámetros, en la tabla de esa parte 6, iguales para todos los sistemas de la recomendación
(60/P a 24/PsF):

| Punto | Parámetro | Valor |
|---|---|---|
| 6.1 | Nivel nominal de E'R, E'G, E'B y E'Y (mV) | **Reference black: 0**; **Reference white: 700** |
| 6.2 | Nivel nominal de E'CB y E'CR (mV) | ±350 |
| 6.3 | Forma del sincronismo | **Tri-level bipolar** |
| 6.5 | Nivel del sincronismo (mV) | ±300 ± 2 % |
| 6.6 | Temporización del sincronismo | **Sync on all components** |

Tres niveles quiere decir que el pulso baja por debajo del nivel de borrado y sube otro tanto por
encima, en lugar de sólo bajar; su punto medio marca el instante de referencia de la línea (oficio,
sobre la figura 2A, que no se reproduce). Los nombres de sala para enganchar un equipo a la
referencia (*genlock*) y la referencia analógica de definición estándar (*black burst*) son oficio,
sin fuente leída. El reloj propio del audio embebido se ve en el § 3.

## 2. La señal de audio

### Las cualidades del sonido

Todo lo que se oye se describe con tres cualidades, y cada una depende de una magnitud física
distinta.

| Cualidad | Qué distingue | De qué magnitud depende |
|---|---|---|
| Tono | Grave o agudo | De la frecuencia: los ciclos por segundo |
| Intensidad | Fuerte o débil | De la amplitud: la magnitud de la variación de presión |
| Timbre | Qué instrumento suena | De la composición armónica |

La frecuencia no es el tono, es su causa. Se mide en hercios y es física; el tono es percepción.
La misma distinción vale para las otras dos: la amplitud es física, la intensidad percibida es
psicoacústica, y por eso se mide en decibelios, que es una escala logarítmica ajustada a cómo oye el
oído.

El margen de frecuencias audibles, que conviene tener a mano: de 20 Hz a 20.000 Hz, y se
estrecha con la edad, primero por arriba.

Qué son los armónicos. Cuando un instrumento da una nota, no produce una sola frecuencia:
produce la fundamental —que es la que determina el tono— y una serie de múltiplos enteros de
ella, los armónicos. Un la de 440 Hz lleva componentes en 880, 1.320, 1.760 y así sucesivamente.

Lo que cambia de un instrumento a otro no son las frecuencias, sino cuánto pesa cada una. Un
violín y una flauta que dan el mismo la tienen los mismos armónicos; lo que difiere es la
intensidad relativa de cada uno. Por eso la propiedad del sonido relacionada con las intensidades
relativas de sus armónicos es el timbre (oficio, como toda esta sección).

Y una consecuencia de oficio: el timbre es lo que un ecualizador modifica. Al subir o bajar
bandas se cambia el peso relativo de los armónicos, y por eso la ecualización cambia el carácter de
una voz sin cambiar la nota que dice.

### Del sonido analógico al digital: muestreo y cuantificación

Digitalizar sonido es medirlo muchas veces por segundo y anotar cada medida con un número.

| Parámetro | Qué fija | Valores de uso |
|---|---|---|
| Frecuencia de muestreo | Cuántas veces por segundo se mide. Determina la frecuencia máxima que se conserva | 48 kHz en televisión; 44,1 kHz en disco; 96 kHz en producción musical |
| Profundidad de bits | Cuántos niveles tiene cada medida. Determina el rango dinámico | 16 bits en emisión; 24 bits en producción |
| Número de canales | Mono, estéreo, envolvente | 2, 5.1, 5.1.4 |

La regla que gobierna el muestreo: hay que muestrear a más del doble de la frecuencia más alta
que se quiera conservar. Por eso 48 kHz cubre holgadamente los 20 kHz del oído, y por eso un
material muestreado a 32 kHz no puede recuperar los agudos que perdió.

La regla que gobierna la profundidad: cada bit añade unos 6 dB de rango dinámico. De ahí que
16 bits den unos 96 dB y 24 bits unos 144 dB, que es más de lo que ningún sistema de reproducción
entrega.

Lo que esto significa en la sala de edición: el audio se trabaja con la profundidad más alta
disponible y se reduce al final, nunca al revés, porque los bits que se tiran no vuelven.

Lo que tiene norma leída detrás de esa tabla, que es oficio: los 48 kHz de la televisión los da la
EBU para la interfaz AES/EBU, que se usa **«primarily […] at 48 kHz, as this is the recommended
sampling frequency for use in broadcasting studios (CCIR Recommendation 646)»** (Tech 3250); y los 16
bits como mínimo, la EBU R 68, que no lo recomienda en su parte dispositiva sino que lo da como su
parecer: **«It is of the opinion that recordings should be made with linear coding using no
pre-emphasis and with a resolution of at least 16 bits in accordance with ITU-R Recommendation
BS.646»**; es decir, las grabaciones deben hacerse así, en opinión de la EBU. Va con la
salvedad de su nota 1: **«16-bit recordings may not meet the requirements of some organizations
regarding the signal-to-noise in production equipment, depending on the performance of the A/D and
D/A converters.»** Ese
audio lineal, sin comprimir, es el PCM.

El caudal del audio digital sale de multiplicar:

> Caudal de un canal = frecuencia de muestreo × profundidad de bits

A 48 kHz y 24 bits, un canal son 1,152 megabits por segundo. Ése es el número que hay que tener.
Un par estéreo, el doble: 2,304 Mb/s; dieciséis canales, 18,4 Mb/s (cálculo). Es el audio en crudo,
sin cabeceras ni datos auxiliares.

### Los niveles del audio digital: escala completa y alineación

En digital, el nivel se cuenta hacia abajo desde el máximo que los bits permiten, la escala completa:
0 dBFS es el código más alto posible, y todo nivel es negativo; lo que intenta pasar de ahí se recorta
sin remedio (oficio).

La EBU fija dónde se coloca el tono de alineación. La R 68-2000 recomienda **«coding levels for
digital audio signals which correspond to an alignment level which is 18 dB below the maximum
possible coding level of the digital system, irrespective of the total number of bits available»**;
es decir, el tono de referencia a −18 dBFS (la expresión en dBFS es oficio). Por qué 18 dB: la señal
de alineación es **«a sine wave signal which has a level (the alignment level) which is 9 dB (or 8
dB in some organizations) below the permitted maximum level of the audio programme»**, y los
medidores de cuasipico engañan: **«the true programme peaks can be 3 dB greater than those
indicated; When operator errors are taken into account the true peaks may occasionally be 6 dB
greater than indicated or 15 dB above alignment level»**. Los 18 dB dejan margen para esos picos
(se deduce de las dos citas).

Aplicación práctica: el tono de 1 kHz que acompaña a las barras al principio de una pieza debe
leerse en −18 dBFS en el medidor de la estación de edición (oficio sobre la R 68).

### La sonoridad: EBU R 128

El nivel de pico no dice cuánto suena un programa. La EBU mide la sonoridad (*loudness*) con la
Recomendación UIT-R BS.1770 y fija el objetivo en la R 128-2023:

- Objetivo: **«the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS.
  Where attaining the Target Level is not achievable practically (for example, live programmes), a
  tolerance of ±1.0 LU is permitted»**, con el aviso de que el borde de la tolerancia no debe hacerse
  costumbre: **«A broadcaster should ensure that a deviation from the Target Level towards the limits
  of the tolerance does not become standard practice»**.
- Tolerancia por errores de medida, distinta de la anterior: **«for the implementation of Loudness
  workflows (for example, in Quality Control environments) a tolerance of ±0.2 LU is allowed in order
  to take account of measurement errors»** (recomendación i). No se confunden: ±1,0 LU es lo que se
  admite cuando no se puede alcanzar el objetivo, como en directo; ±0,2 LU, lo que se admite por el
  error del medidor en el control de calidad.
- Excepción a la baja: **«in special cases the Programme Loudness Level may be normalised to a Target
  Level lower than −23.0 LUFS on purpose. This exception shall be clearly indicated to ensure that such
  a lower Programme Loudness Level is not compensated»** (recomendación j). Sólo por debajo, a
  propósito y avisado, para que nadie lo suba después.
- Pico: **«the True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during
  production (linear audio)»**, con su tolerancia de medida: **«The measurement tolerance is ±0.3 dB
  (for signals with a bandwidth limited to 20 kHz)»**, y una salvedad: **«Permitted Maximum True Peak
  Levels may be lower for different distribution systems and data reduction rates.»** (recomendación m)
- Cómo se mide: **«the audio signal shall generally be measured in its entirety, without emphasis on
  specific foreground elements such as speech, music or sound effects»**, con un medidor conforme a
  la BS.1770 y a la EBU Tech 3341.
- Qué es programa: también las piezas cortas. La definición de la R 128: **«An individual,
  self-contained audio-visual or audio-only item to be presented in Radio, Television or other
  electronic media. An advertisement (commercial), trailer, promotional item (‘promo’), interstitial
  or similar item (“Short-form Content”) shall also be considered to be a programme in this
  context.»** Para esas piezas cortas remite a un suplemento: **«production and normalisation of
  short-form content (adverts; promos etc.) should be made in compliance with EBU R 128 s1»**; y para
  las plataformas, **«guidance for the normalisation of content for streaming is given in EBU R 128
  s2»** (suplementos no leídos).
- La unidad: **«‘LUFS’ is equivalent to ‘LKFS’ (which is used in ITU-R BS.1770)»**.

Para el montador: una promoción o una pieza de informativos se entregan medidas enteras, con su
sonoridad integrada en −23 LUFS y el pico verdadero sin pasar de −1 dBTP (R 128). La herramienta es
el medidor de sonoridad de la estación de edición; la corrección, la ganancia de la pista o de la
mezcla, no el recorte de picos (oficio). La limpieza del audio y la mezcla se estudian en el tema 7.

### La interfaz AES/EBU

La AES/EBU es la interfaz digital de dos canales de audio que la AES publica como AES3 y la EBU en su
Tech 3250. La EBU define su alcance: **«serial digital transmission of two channels of periodically
sampled and linearly represented digital audio data in a broadcasting complex, up to a distance of a
few hundred metres»**. Y señala la frecuencia de trabajo en radiodifusión: **«it is intended that the interface
be primarily used at 48 kHz, as this is the recommended sampling frequency for use in broadcasting
studios (CCIR Recommendation 646).»**

- Subtrama: **«Each sub-frame is divided into 32 time slots, numbered from 0 to 31»**. Lleva una
  muestra de un canal.
- Trama: **«A frame is uniquely composed of two sub-frames»**, una por canal.
- Bloque: **«The block is a group of 192 consecutive frames.»** Lo marca el preámbulo Z, que aparece
  **«once every 192 frames»**.

Cada trama lleva una muestra de cada canal y tiene 64 intervalos (dos subtramas de 32), y **«The rate
of transmission of frames corresponds exactly to the source sampling frequency»**: a 48 kHz salen
48.000 tramas por segundo, es decir, 64 × 48.000 = 3,072 millones de intervalos por segundo
(cálculo).

| Cable | Impedancia | Para qué |
|---|---|---|
| De micrófono | No está especificada: es audio analógico y la impedancia característica no interviene | Audio analógico balanceado |
| AES3 sobre XLR | 110 ohmios | Audio digital de dos canales |
| AES3 sobre coaxial (AES3id) | 75 ohmios | Audio digital sobre infraestructura de vídeo |

### El audio dentro del vídeo: embebido en SDI

La interfaz digital serie (SDI) lleva la señal de vídeo por un coaxial y, además de la imagen, tiene
espacios de datos auxiliares donde cabe el audio. Tres normas de la SMPTE fijan cómo:

| Norma | Para qué SDI | Canales | Muestra |
|---|---|---|---|
| SMPTE 272M-2004 | Definición estándar (ANSI/SMPTE 259M o SMPTE 344M) | **«a minimum of two audio channels and a maximum of 16 audio channels»** (cuatro como máximo en digital compuesto) | 20 bits por defecto; 24 como opción |
| SMPTE ST 299-1:2009 | Alta definición (SMPTE 292) | Hasta 16 a 32, 44,1 o 48 kHz; hasta 8 a 96 kHz | 24 bits |
| SMPTE ST 299-2:2010 | Formatos de imagen sobre interfaz de 3 Gb/s (nivel A) | Los canales **«numbered from 17 to 32»**: hasta 32 a 32, 44,1 o 48 kHz; hasta 16 a 96 kHz | 24 bits |

El audio embebido se organiza en grupos de cuatro canales. La 272M: **«Audio channels are transmitted
in pairs combined, where appropriate, into groups of four. Each group is identified by a unique
ancillary data ID.»** Y la numeración: **«Channels 1 through 4 are in group 1, channels 5 through 8
are in group 2, and so on.»**

| Grupo | Canales | Pares AES/EBU |
|---|---|---|
| 1 | 1 a 4 | Dos |
| 2 | 5 a 8 | Dos |
| 3 | 9 a 12 | Dos |
| 4 | 13 a 16 | Dos |

Cada par de canales corresponde a una señal AES/EBU (el audio embebido **«derived from AES3»**, dice
la 272M), así que 16 canales son ocho pares (cálculo).

Dónde va dentro de la señal en HD: **«Audio data packets are multiplexed (embedded) into the
horizontal ancillary data space of the Cb/Cr data stream, and audio control packets are multiplexed
into the horizontal ancillary data space of the Y data stream.»** (ST 299-1, 1.4). Es decir, en el
espacio auxiliar horizontal (HANC), el intervalo que la señal deja en cada línea fuera de la imagen
activa.

| Operación | Qué hace | Aparato |
|---|---|---|
| Embeber | Meter pistas de audio dentro de la señal de vídeo | Embebedor (*embedder*) |
| Desembeber | Sacarlas de la señal de vídeo | Desembebedor (*de-embedder*) |

Aplicación práctica para el montador (oficio): el material que entra por SDI trae su audio en pistas
numeradas, y el reparto de esas pistas (qué va en la 1 y la 2, qué en la 3 y la 4) es un acuerdo de
cada casa; al ingestar o al exportar hay que comprobar que las pistas de la pieza van donde el
destino las espera, porque un reparto cambiado saca el programa con el sonido en el canal equivocado.
El reparto de pistas propio de CSRTV no consta en un documento publicado leído.

## 3. Vídeo y audio juntos: código de tiempo y sincronía

### El código de tiempo

El código de tiempo es la etiqueta que numera cada cuadro en horas, minutos, segundos y cuadros.
Es lo que permite localizar un punto exacto del material y lo que sincroniza varias cámaras entre
sí. En la sala, es la referencia común del montaje: con él se localizan los totales en el material
bruto, se reconstruye una edición en otro sistema y se casan imagen y sonido grabados por separado
(oficio).

Hay dos modalidades, y la diferencia sólo existe por una peculiaridad histórica:

| Modalidad | Qué hace | Cuándo se usa |
|---|---|---|
| NDF, *non-drop frame* | Cuenta todos los cuadros, sin saltarse ninguno | Cuando la cadencia es un número entero: 24, 25, 30, 50 |
| DF, *drop frame* | Se salta números de cuadro periódicamente para que el código de tiempo coincida con el reloj de pared | Cuando la cadencia no es entera: 29,97 o 59,94 |

En un sistema de televisión de 25 fps usaremos un código de tiempo NDF. Por qué, en una frase: 25
es un número entero, así que veinticinco cuadros son exactamente un segundo y no hay nada que
corregir. El *drop frame* nació en el sistema americano, cuya cadencia real es 29,97 cuadros por
segundo y no 30: contando de treinta en treinta, el código de tiempo se queda atrás del reloj unos tres
segundos y medio por hora, y el *drop frame* corrige esa deriva saltándose números.

La cuenta (cálculo sobre la cadencia de la BT.709-6, 30/1,001): en una hora pasan 3.600 × 30/1,001 ≈
107.892 cuadros, y un código de treinta en treinta necesitaría 108.000 para marcar la hora; la
diferencia, unos 108 cuadros, son 3,6 segundos.

El malentendido más común, que conviene deshacer: el *drop frame* no tira cuadros. Salta
números en la cuenta. El material queda intacto; lo que cambia es la etiqueta.

Qué supone para el montador (oficio): el código de tiempo de la secuencia se fija con la cadencia de
la secuencia, y un material de 29,97 metido en una secuencia de 25 no conserva su código de tiempo
cuadro a cuadro.

### La sincronía entre imagen y sonido

El audio embebido va atado al vídeo. Las dos normas prefieren audio síncrono: **«Audio sampled at 48
kHz and clock locked (synchronous) to video is the preferred implementation for intrastudio
applications»** (272M) y, en HD, **«Audio sampled at a clock frequency of either 48 kHz or 96 kHz
locked (synchronous) to video, is the preferred implementation for intrastudio applications»** (ST
299-1). Como opción admiten audio de 32 a 48 kHz síncrono o asíncrono.

Por qué 48 kHz casa con el vídeo europeo (cálculo): 48.000 muestras por segundo entre 25 cuadros son
exactamente 1.920 muestras de audio por cuadro, y entre 50, 960. Con cadencias divididas por 1,001 la
cuenta no sale entera, y el reparto de muestras por cuadro varía de un cuadro a otro.

En la sala, la sincronía se pierde de tres maneras (oficio):

| Causa | Qué se ve | Remedio |
|---|---|---|
| Audio y vídeo a relojes distintos (un grabador externo sin sincronizar, un audio de 44,1 kHz en una secuencia de 48 kHz) | El desfase crece a lo largo de la pieza | Sincronizar en origen o convertir la frecuencia de muestreo antes de montar |
| Desplazamiento de un clip de sonido respecto de su imagen al recortar o mover | Desfase fijo desde un corte concreto | Los indicadores de desincronía del sistema de edición y volver a enganchar el clip |
| Retardo del procesado o de la pantalla | Los labios van antes o después que la voz aunque el fichero esté bien | Medir la cadena de monitorado, no tocar el montaje |

Para casar imagen y sonido grabados por separado se usa el código de tiempo común o, si no lo hay,
una referencia visible y audible a la vez, como la claqueta o una palmada (oficio).

## Recomendaciones y normas técnicas que el tema cita

No hay norma jurídica que regule este tema. Las técnicas, en la edición leída:

| Documento | Qué se toma |
|---|---|
| Recomendación UIT-R BT.709-6 (06/2015), parámetros de la HD | Primarios, blanco D65, característica de transferencia y exponente 0,45, luminancia, señal codificada, 1.920 × 1.080 y píxel cuadrado, cadencias, exploración progresiva, entrelazada y PsF (con su anexo 2), 1.125 líneas, frecuencias de muestreo, 8 o 10 bits, niveles de cuantificación y sincronismo de tres niveles (parte 6) |
| Recomendación UIT-R BT.2020-2 (10/2015), parámetros de la UHD | Primarios, luminancia, luminancia constante y no constante, formatos 7.680 × 4.320 y 3.840 × 2.160, cadencias y red eléctrica, exploración progresiva, 10 o 12 bits |
| Recomendación UIT-R BT.2100-3 (02/2025), parámetros del HDR | PQ y HLG, blanco de referencia HDR, entorno y monitor de referencia, formatos y cadencias, NCL por defecto e ICTCP, submuestreo, rango estrecho y completo, nota sobre la mayor resolución práctica |
| Informe UIT-R BT.2408-9 (03/2026), práctica operativa del HDR | Blanco del grafismo y tabla de niveles nominales en PQ y HLG |
| EBU R 103 v3.0 (mayo de 2020), tolerancias de la señal de vídeo digital | Rangos nominal, preferente y total; error de gama; recortadores; legalizadores; sub-negros |
| EBU R 68-2000, nivel de alineación del audio digital | Alineación a 18 dB bajo el máximo; 9 dB bajo el máximo permitido; 16 bits como mínimo (parecer de la EBU, no recomendación) y su nota 1 |
| EBU R 128-2023, normalización de la sonoridad | −23,0 LUFS, ±1,0 LU, ±0,2 LU por errores de medida, excepción por debajo de −23,0 LUFS, −1 dBTP con su tolerancia de ±0,3 dB y su salvedad, medida del programa entero, definición de programa, LUFS y LKFS |
| EBU Tech 3250, 3.ª ed., 2004 (AES/EBU) | Alcance, 48 kHz, subtrama, trama y bloque; 110 Ω |
| SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012 y ST 2082-1:2023 (SDI) | Velocidades, conector BNC de 75 Ω, codificación NRZI aleatorizada, atenuación admisible; *jitter* de la ST 292-1 (8.1.8 y tabla 3) |
| SMPTE 272M-2004, ST 299-1:2009 y ST 299-2:2010 (audio embebido) | Canales, grupos, HANC, reloj síncrono |
| SMPTE ST 2084 (catálogo) | Nombre de la curva PQ |

Se nombran sin haberlos leído: las Recomendaciones UIT-R BT.601, BT.1886, BS.646 y BS.1770; la norma
AES3 (de pago; la AES/EBU va por la Tech 3250); EBU Tech 3341 y los suplementos s1 y s2 de la R 128; la
SMPTE RP 184 de medida del *jitter*; la norma SMPTE 276M del AES3 coaxial (la cita el tema 28-11 de Canal Sur, del que se toma la tabla de
cables).

## Lo que este tema no da, y dónde está

- Lo propio de CSRTV: formato de producción de la casa (resolución, cadencia, SDR o HDR), reparto de
  pistas de audio embebidas, nivel de alineación y sonoridad exigidos en sus entregas. No consta en
  un documento publicado leído; el tema da las recomendaciones de la EBU y la UIT-R.
- La fase de despliegue de la UHD que eligió 10 bits, y las normas SMPTE 274M (formato 1080) y 296M
  (formato 720): no se han leído; el tema no las atribuye.
- El transporte del UHD por cuatro enlaces de 3G-SDI (SMPTE ST 425-5) y el 6G-SDI (SMPTE ST 2081): no
  leídos.
- Los perfiles comerciales de HDR (HDR10, HDR10+, Dolby Vision) y sus metadatos (SMPTE ST 2086, sólo
  su título en el catálogo): sin fuente normativa leída.
- La SMPTE ST 12 del código de tiempo, el código de tiempo longitudinal y el insertado en el
  intervalo vertical, y la regla exacta de qué números salta el *drop frame*: no leídos; el código de
  tiempo va como oficio con la cuenta que lo sostiene.
- La conversión entre SDR y HDR y las LUT de conversión que trata el Informe BT.2408: sólo se leyeron
  los títulos.
- Los códecs, la compresión, los contenedores y la transmisión de vídeo y audio sobre IP (SMPTE ST
  2110, AES67): tema 4. La corrección de color, la limpieza de audio, la ecualización y el *ducking*:
  tema 7. La ingesta y la verificación del material: tema 8.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| UIT-R BT.709-6 (06/2015), PDF de itu.int: puntos 1.2, 1.3, 1.4, 2, 3.1-3.3, 4.1, 4.3-4.7, 5.1-5.9, parte 2, parte 6 (sincronismo de tres niveles) y anexo 2 | Todo lo atribuido a la BT.709 | 25-09-2026 |
| UIT-R BT.2020-2 (10/2015): tablas 1, 2 y 4 con sus notas, tabla 5 | Todo lo atribuido a la BT.2020 | 25-09-2026 |
| UIT-R BT.2100-3 (02/2025): tablas 1, 3, 4, 6, 7, 8, 9, notas 1b, 3c, 10a y nota sobre PQ y HLG | Todo lo atribuido a la BT.2100 | 25-09-2026 |
| Informe UIT-R BT.2408-9 (03/2026): §§ 2.1 y 2.2, tabla 1 | Blanco del grafismo y niveles nominales | 25-09-2026 |
| EBU R 103 v3.0 (mayo de 2020), anexos 1 y 2 | Pasaje copiado del tema 9 de Cámara Operador | 24-09-2026 (por ese tema) |
| EBU R 68-2000, PDF de tech.ebu.ch | Nivel de alineación, 16 bits y su nota 1 (el PDF imprime «161» por la llamada de nota pegada al 16) | 25-09-2026 |
| EBU R 128-2023 (noviembre de 2023): recomendaciones g-t (i, j y la tolerancia de m releídas el 25-09-2026) y definiciones | Sonoridad | 25-09-2026 |
| EBU Tech 3250, 3.ª ed., 2004; SMPTE 272M-2004, ST 299-1:2009 y ST 299-2:2010 | Pasajes copiados del tema 11 de Operador/a de Sonido | 25-09-2026 (por ese tema) |
| SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023 (PDF de pub.smpte.org) y fichas del catálogo SMPTE; ST 292-1, 8.1.8 y tabla 3 con sus notas | SDI y *jitter* | 25-09-2026 |

Oficio sin norma detrás, y así se declara: la síntesis aditiva y las leyes de Grassmann; los colores
no espectrales; la luminancia constante y no constante explicadas; la gamma de 2,2; la curva
logarítmica; el vídeo compuesto y por componentes; el porqué del entrelazado y su notación; la tabla
de resoluciones salvo lo citado; el muestreo cromático y el canal alfa; el *banding*; el *nit* y las
unidades de fotometría; los usos de PQ y HLG; los instrumentos de medida, el monitor de referencia y
las señales de prueba; el *jitter* y el UI como duración de un bit; la referencia común de la
instalación, la forma del pulso de tres niveles, *genlock* y *black burst*; las cualidades del sonido y el audio digital, con las reglas del
doble de la frecuencia y de los 6 dB por bit; la escala completa digital; el código de tiempo; las
causas de desincronía. Es cálculo, y se puede rehacer: 256, 1.024 y 4.096 niveles; 148,5 y 74,25
millones de muestras por segundo; 1.485, 2.970 y 11.880 Mb/s; 1,152 Mb/s por canal de audio; 3,072
millones de intervalos por segundo en la AES/EBU; 108 cuadros y 3,6 segundos por hora de *drop
frame*; 1.920 muestras de audio por cuadro a 25 fps; el 4 % del paso de 24 a 25.
