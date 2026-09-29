# Tema 8 del específico de Grafista · Formatos técnicos: resolución, códecs, alfa, safe areas, colorimetría, HDR/SDR y entrega para emisión

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Grafista · punto 8 |
| Sirve para | Grafista de Canal Sur (grupo B03): test de teoría específica y de aplicación práctica, y prueba práctica del puesto |
| Fuente | Sin norma jurídica que regule los formatos. Lo propio de la casa: Contrato-programa 2024-2026 entre el Consejo de Gobierno y la RTVA (BOJA núm. 245, de 26/12/2023), puntos 85 y 101. Recomendaciones e informes de la UIT-R: BT.601-7, BT.709-6, BT.2020-2, BT.2100-3 e Informe BT.2408-9. SMPTE: ST 2046-1:2009 (zonas seguras), ST 2110-20:2022 y fichas de catálogo (ST 377-1, ST 2084, ST 2086, ST 2094-40). EBU: R 95 v1.1, R 103 v3.0 y hoja informativa *Quality Control* (2015) con su catálogo de ítems. AMWA (AS-11); Library of Congress (MXF y ProRes 422). Documentación de fabricante: Apple (*Apple ProRes*, abril de 2022), Avid, Sony, Blackmagic Design (manual de DaVinci Resolve 21 y manual de los mezcladores ATEM), Blender Foundation (manual de Blender 5.2) y Vizrt (*Viz Engine Administrator Guide* 5.2 y 5.4). Lo demás, oficio y cálculo |
| Redacción que se estudia | Las ediciones vigentes el 24-09-2026 de cada documento citado; fechas de lectura en «Trazabilidad» |
| Extensión | 18.300 palabras aproximadamente (el enunciado reúne siete materias técnicas) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); televisión digital terrestre (TDT). Sector de Radiocomunicaciones de la Unión
Internacional de Telecomunicaciones (UIT-R), que escribe la ultra alta definición como UHDTV; Unión
Europea de Radiodifusión (EBU, *European Broadcasting Union*); Sociedad de Ingenieros de Cine y
Televisión (SMPTE, *Society of Motion Picture and Television Engineers*), cuyas normas llevan el
prefijo ST (*standard*) o RP (*recommended practice*, práctica recomendada); Advanced Media Workflow
Association (AMWA); Digital Production Partnership (DPP) y North American Broadcasters Association
(NABA), que se nombran como los cita la fuente; Biblioteca del Congreso de Estados Unidos (LOC,
*Library of Congress*); Comisión Internacional de la Iluminación (CIE); Comisión Electrotécnica Internacional (IEC); Consorcio World Wide Web (W3C), autor
de las pautas de accesibilidad para el contenido web (WCAG, *Web Content Accessibility Guidelines*); la norma estadounidense de
subtítulos CEA-708, que se nombra como la cita la SMPTE.

Los términos técnicos, presentados de entrada: definición estándar (SD), alta definición (HD) y ultra
alta definición (UHD); iniciativa de cine digital (DCI, *Digital Cinema Initiatives*); rango dinámico
estándar (SDR) y alto (HDR); cuantificación perceptual (PQ, *perceptual quantization*) e híbrida
logarítmica-gamma (HLG, *hybrid log-gamma*); candela por metro cuadrado (cd/m²), que la industria
llama *nit*; cuadros o fotogramas por segundo (fps); progresivo (p), progresivo por cuadro segmentado
(PsF, *progressive segmented frame*) y entrelazado (i); rojo, verde y azul (RGB), el mismo con canal
alfa (RGBA), luminancia con diferencias de color (YCbCr) y el modelo de tinta cian, magenta, amarillo y
negro (CMYK); tabla de consulta (LUT, *look-up table*); luminancia constante (CL) y no constante (NCL);
intensidad constante (CI), con su señal ICtCp de intensidad (I) y dos diferencias de color (CT y CP);
grupo de imágenes (GOP, *group of pictures*); codificación avanzada de vídeo (AVC, la norma H.264) y de
alta eficiencia (HEVC, la norma H.265); formato de intercambio de material (MXF, *material exchange
format*), con sus patrones operacionales OP1a y OP-Atom; contenedores de Apple (MOV, QuickTime), de la
familia de normas del Grupo de Expertos en Imágenes en Movimiento (MPEG) (MP4) y de Microsoft (AVI); relación
señal/ruido de pico (PSNR, *peak signal-to-noise ratio*); megabits y gigabits por segundo (Mb/s,
Gb/s), megabyte y gigabyte (MB, GB); descripción del formato activo (AFD, *Active Format
Description*); control de calidad (QC, *quality control*), cuyo catálogo de la EBU se publica con
licencia Creative Commons de atribución (CC-BY 4.0); composición posterior del mezclador (DSK, del
inglés *downstream keyer*); protocolo de internet (IP); interfaz digital serie (SDI); señal de ajuste de
los negros del monitor (PLUGE, *picture line-up generation equipment*); código de tiempo (TC, *timecode*); sistema de
transferencia (TCS, *Transfer Characteristic System*) de un flujo SMPTE ST 2110; definición estándar y
alta definición en la notación de la UIT (SDTV y HDTV); puntos de código independientes de la
codificación (CICP, *Coding Independent Code Points*); los sistemas analógicos de
color PAL y NTSC, que sólo se nombran; el espacio de color RGB por defecto (sRGB, norma
IEC 61966-2-1); el relleno (*fill*) y la llave (*key*) con que un sistema de
grafismo entrega una imagen con transparencia. Los formatos de fichero gráfico se nombran por su
extensión (PSD, AI, TIFF o TIF, PNG, JPG, TGA o TARGA, GIF, SVG, EPS, BMP, EXR u OpenEXR).

Los nombres de formato y de producto se escriben como los imprime el fabricante (ProRes 422 HQ, LT o
4444 XQ, DNxHD 145, AVC-Intra 100, XAVC S; la cámara PXW-Z200 de Sony; Viz Engine, de Vizrt; DaVinci
Resolve y Fusion, de Blackmagic Design; Photoshop, After Effects e Illustrator, de Adobe; Blender):
son marcas, no siglas que se desarrollen. Se citan como ejemplos: qué equipos y programas usa CSRTV no
consta en documento publicado.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.15, punto 8): «Formatos técnicos:
> resolución, códecs, alfa, safe areas, colorimetría, HDR/SDR y entrega para emisión.»

Qué se puede preguntar: qué resolución tienen el SD, el HD, el UHD y el 8K, qué recomendación fija cada
uno y en qué se diferencia el UHD del 4K de cine; si el píxel de la televisión actual es cuadrado; qué
es la relación de aspecto y qué son el *letterbox* y el *pillarbox*; en qué sistema emite Canal Sur por
TDT; cuánto ocupa un fotograma sin comprimir; qué es un códec, qué diferencia a intracuadro de GOP
largo y cuál conviene para el grafismo; qué significan 4:2:2, 4:2:0 y 4:4:4:4; cuántos niveles da una
muestra de 10 bits y qué produce el *banding*; cuáles son los rangos nominal y preferente de la EBU
R 103 y qué es el rango estrecho; qué son ProRes, DNxHD y H.264/H.265, y qué ProRes llevan alfa; qué es
un contenedor y si MXF es un códec; qué es el canal alfa, qué ficheros lo llevan y cuántos bits tiene
un TGA con alfa; qué distingue el alfa directo del premultiplicado; cómo sale el alfa de un motor de
grafismo de directo (relleno y llave); qué son las zonas seguras de acción y de título o grafismo,
cuánto miden según la EBU R 95 y según la SMPTE ST 2046-1 y cuántos píxeles son en 1080 y en 2160; qué
primarios y blanco fijan la BT.709 y la BT.2020, cuál es la fórmula de la luminancia y qué es la gamma;
por qué un logotipo de imprenta no se lleva tal cual a la pantalla; qué son PQ y HLG, qué norma SMPTE
publica la PQ, qué perfiles de HDR llevan metadatos; a qué nivel va el blanco de un rótulo en HLG y en
PQ; cómo se convierte un grafismo SDR para un programa HDR; qué es un estándar de entrega, qué son
AS-11 y un control de calidad por destino, y cómo se entrega una pieza gráfica a emisión. En la prueba
práctica: fijar el formato de trabajo y de entrega de un grafismo, calcular zonas seguras y tamaños de
fichero, elegir fichero con alfa o par relleno-llave, preparar un rótulo para HDR y comprobar la pieza
antes de entregarla.

<!-- indice -->

## Índice

- [1. Resolución](#1-resolución)
  - [Resolución y relación de aspecto](#resolución-y-relación-de-aspecto)
  - [Producir en alta y entregar en baja](#producir-en-alta-y-entregar-en-baja)
  - [La relación de aspecto y sus arreglos](#la-relación-de-aspecto-y-sus-arreglos)
  - [El HD: la BT.709](#el-hd-la-bt709)
  - [Lo que emite Canal Sur](#lo-que-emite-canal-sur)
  - [Cuánto ocupa un fotograma sin comprimir](#cuánto-ocupa-un-fotograma-sin-comprimir)
- [2. Códecs](#2-códecs)
  - [Qué es un códec y qué se pierde](#qué-es-un-códec-y-qué-se-pierde)
  - [El muestreo cromático](#el-muestreo-cromático)
  - [La profundidad de bits y los niveles](#la-profundidad-de-bits-y-los-niveles)
  - [Los límites de la señal según la EBU](#los-límites-de-la-señal-según-la-ebu)
  - [Intracuadro y GOP largo](#intracuadro-y-gop-largo)
  - [H.264 y H.265](#h264-y-h265)
  - [Apple ProRes](#apple-prores)
  - [Avid DNxHD (SMPTE VC-3)](#avid-dnxhd-smpte-vc-3)
  - [AVC-Intra (Panasonic)](#avc-intra-panasonic)
  - [Cuadro resumen](#cuadro-resumen)
  - [Los contenedores](#los-contenedores)
- [3. Alfa](#3-alfa)
  - [Qué es el canal alfa](#qué-es-el-canal-alfa)
  - [Los ficheros gráficos que llevan alfa](#los-ficheros-gráficos-que-llevan-alfa)
  - [Alfa directo y alfa premultiplicado](#alfa-directo-y-alfa-premultiplicado)
  - [El alfa en directo: relleno y llave](#el-alfa-en-directo-relleno-y-llave)
  - [Los errores de entrega con el alfa](#los-errores-de-entrega-con-el-alfa)
- [4. Zonas seguras (*safe areas*)](#4-zonas-seguras-safe-areas)
  - [Qué es una zona segura y por qué sigue existiendo](#qué-es-una-zona-segura-y-por-qué-sigue-existiendo)
  - [La EBU R 95](#la-ebu-r-95)
  - [La SMPTE ST 2046-1](#la-smpte-st-2046-1)
  - [Las dos normas, comparadas](#las-dos-normas-comparadas)
  - [El grafista y las zonas seguras](#el-grafista-y-las-zonas-seguras)
- [5. Colorimetría](#5-colorimetría)
  - [El color de la pantalla: síntesis aditiva, RGB y CMYK](#el-color-de-la-pantalla-síntesis-aditiva-rgb-y-cmyk)
  - [Primarios y blanco de referencia](#primarios-y-blanco-de-referencia)
  - [La luminancia: la señal Y](#la-luminancia-la-señal-y)
  - [Luminancia constante y no constante](#luminancia-constante-y-no-constante)
  - [La gamma](#la-gamma)
  - [Del programa de diseño a la señal de vídeo](#del-programa-de-diseño-a-la-señal-de-vídeo)
  - [Las LUT](#las-lut)
- [6. HDR/SDR](#6-hdrsdr)
  - [Qué es y qué recomendación lo fija](#qué-es-y-qué-recomendación-lo-fija)
  - [Los metadatos de masterizado](#los-metadatos-de-masterizado)
  - [Los perfiles de HDR](#los-perfiles-de-hdr)
  - [Cómo se señala el HDR](#cómo-se-señala-el-hdr)
  - [Los niveles del HDR](#los-niveles-del-hdr)
  - [Mezclar SDR y HDR: las conversiones](#mezclar-sdr-y-hdr-las-conversiones)
  - [El grafismo en HDR](#el-grafismo-en-hdr)
- [7. Entrega para emisión](#7-entrega-para-emisión)
  - [Qué es un estándar de entrega](#qué-es-un-estándar-de-entrega)
  - [El MXF como base](#el-mxf-como-base)
  - [AMWA AS-11](#amwa-as-11)
  - [El control de calidad de cada entregable](#el-control-de-calidad-de-cada-entregable)
  - [La sonoridad de entrega: EBU R 128](#la-sonoridad-de-entrega-ebu-r-128)
  - [Cómo entrega el grafista](#cómo-entrega-el-grafista)
  - [La comprobación antes de entregar](#la-comprobación-antes-de-entregar)
  - [Versiones para plataformas](#versiones-para-plataformas)
- [Aplicación práctica](#aplicación-práctica)
  - [Un rótulo animado para un informativo en HD](#un-rótulo-animado-para-un-informativo-en-hd)
  - [Cuentas que se piden](#cuentas-que-se-piden)
  - [Un grafismo SDR en un programa HDR](#un-grafismo-sdr-en-un-programa-hdr)
- [Normas y documentos técnicos que el tema cita](#normas-y-documentos-técnicos-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Resolución

### Resolución y relación de aspecto

La resolución espacial es cuántos píxeles tiene la imagen; la relación de aspecto es la proporción
entre su ancho y su alto. Son dos cosas distintas, y el examen puede preguntar por las dos.

| Formato | Píxeles (horizontal × vertical) | Relación de aspecto | Fuente |
|---|---|---|---|
| Definición estándar (SD) | 720 muestras de luminancia por línea activa | 4:3 o 16:9 | UIT-R BT.601-7: **«Número de muestras por línea activa digital: señal de luminancia 720»**, y **360** para cada diferencia de color |
| HD de 720 líneas | 1.280 × 720 | 16:9 | No es un formato de la BT.709; lo ofrecen cámaras como la Z200 (1.280 × 720 a 50p y 59,94p) |
| HD (Full HD) | 1.920 × 1.080 | 16:9 | UIT-R BT.709-6 |
| UHD o 4K de televisión | 3.840 × 2.160 | 16:9 | UIT-R BT.2020-2 y BT.2100-3 |
| 8K de televisión | 7.680 × 4.320 | 16:9 | UIT-R BT.2020-2 y BT.2100-3 |
| 4K de cine (DCI) | 4.096 × 2.160 | cercana a 17:9 | Oficio (la especificación DCI no se ha leído) |

La BT.2100-3, la recomendación del HDR, recoge los tres formatos de su tabla 1 (**«7 680 × 4 320 /
3 840 × 2 160 / 1 920 × 1 080»**) con **«Pixel aspect ratio 1:1 (square pixels)»**: los píxeles de
la televisión actual son cuadrados, a diferencia de los de la definición estándar, cuyas 720
muestras por línea sirven lo mismo a 4:3 que a 16:9 (oficio).

Lo que UHD multiplica es el número de píxeles, no la forma de la pantalla: HD y UHD son 16:9.
3.840 × 2.160 es exactamente el doble de 1.920 × 1.080 en cada dirección, cuatro veces los píxeles
(cálculo: 8.294.400 frente a 2.073.600). El 8K vuelve a multiplicar por cuatro.

La BT.2020-2 dice para qué se pensaron los dos formatos de ultra alta definición: **«Both 3 840 ×
2 160 and 7 680 × 4 320 systems of UHDTV will find their main applications for the delivery of
television programming to the home where they will provide viewers with an increased sense of “being
there” and increased sense of realness by using displays with a screen diagonal of the order of 1.5
metres or more and for large screen (LSDI) presentations in theatres, halls and other venues such as
sports venues or theme parks.»** (nota 1 a pie de página del apartado *recomienda*; LSDI es **«large screen digital imagery»**,
imagen digital en pantalla grande, que la misma recomendación, en su considerando e), define como **«a system providing a
display on a very large screen, typically for public viewing»**).

### Producir en alta y entregar en baja

La BT.2100-3 da una regla que se aplica al elegir la resolución del proyecto (nota 1b):
**«Productions should use the highest resolution image format that is practical. It is recognized
that in many cases high resolution productions will be down-sampled to lower resolution formats for
distribution. It is known that producing in a higher resolution format, and then electronically
down-sampling for distribution, yields superior quality than producing at the resolution used for
distribution.»**

Aplicado al grafismo (oficio): una pieza se diseña a la resolución de entrega o a una mayor, nunca a
una menor. Un grafismo de mapa de bits ampliado de 1.920 × 1.080 a 3.840 × 2.160 se ablanda, porque el
programa tiene que inventar los píxeles que faltan; reducido de 3.840 × 2.160 a 1.920 × 1.080 conserva
la nitidez. Lo que no pierde nada al cambiar de tamaño es lo vectorial (texto y formas), que se vuelve
a calcular. Por eso las piezas que pueden acabar en varios destinos se preparan en el formato más
alto que vaya a hacer falta y con los elementos en vectorial mientras se pueda.

### La relación de aspecto y sus arreglos

La relación de aspecto es la proporción entre el ancho y el alto de la imagen, y se obtiene
dividiendo el número de píxeles horizontales entre el número de píxeles verticales —siempre que
los píxeles sean cuadrados, que es lo normal en digital—.

Ni la distancia focal, ni el tipo de objetivo, ni el tamaño del sensor la determinan por sí solos:
el objetivo cambia el campo que entra, no la forma del rectángulo; y el tamaño del sensor
importa por su forma, no por su tamaño. Dos sensores de tamaños muy distintos con la misma matriz de
píxeles dan la misma relación de aspecto.

Las relaciones más usadas, escritas de las dos formas:

| Relación | Como decimal | Dónde |
|---|---|---|
| 4:3 | 1,33:1 | Televisión convencional |
| 16:9 | 1,77:1 | Alta definición y televisión digital |
| 1,85:1 | 1,85:1 | Cine, formato panorámico |
| 2,39:1 | 2,39:1 | Cine, formato anamórfico |

El 16:9 es 1,77:1, porque 16 ÷ 9 = 1,777… Es aritmética.

Cuando una imagen no encaja en la pantalla, hay que decidir qué se sacrifica. Los dos arreglos
clásicos:

- Letterboxing: se añaden dos franjas negras horizontales, arriba y abajo, para meter una
  imagen ancha en una pantalla menos ancha sin recortarla ni deformarla.
- Pillarboxing: las franjas van a los lados, para meter una imagen estrecha —un 4:3— en una
  pantalla ancha.

Y el aviso de oficio que se deriva, porque es trabajo diario del grafista: cuando se mezcla material de
1.85 con emisión en 16:9 quedan bandas muy finas, y con 2.35 quedan bandas gruesas arriba y abajo. Un
rótulo colocado sin mirar eso se cuela dentro de la banda negra.

Qué hace el grafista con otra forma (oficio): el grafismo no se estira para llenar un cuadro de otra
proporción, porque deforma la tipografía y el logotipo; se recompone. Una pieza de 16:9 que se va a
recortar a cuadrado o a vertical para redes se diseña con lo esencial en el centro, o se hace una
versión propia para cada forma (los formatos verticales son el tema 13).

Cuando la relación de aspecto viaja con el fichero, la señala un metadato. El catálogo de control de
calidad de la EBU (epígrafe 7) tiene un ítem para comprobarlo, el 0001F: **«System shall check the
presence and value of the Active Format Description (AFD), which describes the aspect ratio of the
active picture, and safe cut-out areas.»** Las zonas seguras son el epígrafe 4.

### El HD: la BT.709

La Recomendación UIT-R BT.709-6 es la de la televisión de alta definición: 1.920 muestras por línea
activa y 1.080 líneas activas. Sus cadencias: **«The following picture rates are specified: 60 Hz,
50 Hz, 30 Hz, 25 Hz and 24 Hz. For the 60, 30 and 24 Hz systems, picture rates having those values
divided by 1.001 are also specified.»**

Y, a diferencia de la BT.2020 y la BT.2100, conserva el entrelazado (la BT.601 de la definición
estándar también es **«entrelazada»**): **«Pictures are defined
for progressive (P) capture and interlace (I) capture. Progressive captured pictures can be
transported with progressive (P) transport or progressive segmented frame (PsF) transport. Interlace
captured pictures can be transported with interlace (I) transport.»** Entre sus combinaciones están
el 50 progresivo, el 25 progresivo (transportado como progresivo o como cuadro segmentado) y el 25
entrelazado.

Cómo se leen las tres formas del HD europeo (oficio, sobre la BT.709):

| Nombre de uso | Qué es según la BT.709 | Imágenes por segundo |
|---|---|---|
| 1080i50 (también 1080i/25) | Sistema 50/I: captación entrelazada a 25 cuadros, cada cuadro en dos campos | 50 campos, 25 cuadros |
| 1080PsF25 | Captación progresiva a 25 cuadros, transportada partiendo cada cuadro en dos segmentos | 25 cuadros |
| 1080p25 y 1080p50 | Captación y transporte progresivos | 25 o 50 cuadros |

La confusión que hay que deshacer: 50i no son 50 cuadros, son 50 campos y 25 cuadros. Si fueran
cuadros la notación sería 1080p50. El PsF no es entrelazado: los dos segmentos salen del mismo
instante, y al montarlo se trata como progresivo (oficio). La BT.709 llama a ese entrelazado sistema
**«50/I»**, con captación **«25 interlace»**, y al progresivo segmentado, **«25/PsF»**; que el mismo
formato se escriba 1080i50 o 1080i/25 es costumbre de fabricantes.

Lo que el entrelazado le hace al grafismo (oficio): la imagen se manda en dos mitades, y una línea
horizontal fina parpadea en entrelazado. Por eso los filetes de un rótulo, las rayas finas de una
tabla o el texto muy pequeño se dibujan con un grosor de más de una línea, y se comprueban en un monitor
de vídeo, no sólo en la pantalla del ordenador.

### Lo que emite Canal Sur

El Contrato-programa 2024-2026 entre el Consejo de Gobierno y la RTVA (BOJA núm. 245, de 26/12/2023)
fija el sistema de la emisión terrestre. Punto 85 (p. 42 del Contrato-programa): **«En sus diversas
programaciones lineales de televisión en TDT, Canal Sur se posicionará de forma activa en la difusión
en sistema de Alta Definición (HD), pasando a ser este el único sistema técnico de difusión televisiva
por ondas hertzianas terrestres empleado en la cobertura del territorio andaluz a partir del 14 de
febrero de 2024, y se continuará cooperando en proyectos de expansión, desarrollo y aplicación del
sistema de difusión en Ultra Alta Definición (UHD 4K) y de TDT en movilidad, en función del espectro
radioeléctrico disponible en Andalucía para esa finalidad.»**

Y el punto 101 (p. 47) da la razón normativa: la cobertura de la TDT de Canal Sur desde esa fecha
**«estará referida a la utilización de la tecnología de difusión del sistema de Alta Definición (HD),
conforme a lo establecido en el artículo segundo del Real Decreto 16/2023, de 17 de enero»**, que
modifica el Plan Técnico Nacional de la Televisión Digital Terrestre (Real Decreto 391/2019). La parte
expositiva del Contrato-programa añade que esa obligación **«implica la necesaria actualización de la
integridad de los sistemas de producción, edición y de emisión de la totalidad de Centros de
Producción que intervienen en la generación de contenidos para televisión»** (p. 11).

Lo que se deduce para el grafista: la emisión lineal de Canal Sur por TDT es en HD, así que el lienzo
de la antena es de 1.920 × 1.080, y la UHD es, según el Contrato-programa, un proyecto de cooperación,
no el sistema de emisión. En qué formato HD concreto (1080i50, 1080p50) produce y emite CSRTV, con qué
códec y si hace alguna producción en UHD o HDR no consta en un documento publicado localizado.

### Cuánto ocupa un fotograma sin comprimir

Sin compresión, el tamaño de una imagen es el número de píxeles por los bytes de cada píxel, y nada
más: ni el contenido ni el entrelazado lo cambian. Un fotograma renderizado en formato TGA sin
compresión ocupa el mismo espacio en bytes en todos los casos (oficio).

| Imagen | Cuenta | Bytes |
|---|---|---|
| 1.920 × 1.080, RGB de 8 bits (3 bytes por píxel) | 2.073.600 × 3 | 6.220.800 (unos 6,2 MB) |
| 1.920 × 1.080, RGBA de 8 bits (4 bytes por píxel) | 2.073.600 × 4 | 8.294.400 (unos 8,3 MB) |
| 3.840 × 2.160, RGBA de 8 bits | 8.294.400 × 4 | 33.177.600 (unos 33,2 MB) |

(Cálculo, con MB de un millón de bytes.) Un segundo de secuencia de TGA con alfa en HD a 25 fotogramas
por segundo son unos 207 MB (8.294.400 × 25), y un minuto, unos 12,4 GB. Esa es la razón práctica de
entregar el vídeo con alfa en un códec como ProRes 4444 (epígrafe 3) en lugar de en secuencia de
imágenes sin comprimir, salvo que el destino la pida.

## 2. Códecs

### Qué es un códec y qué se pierde

Códec es la contracción de codificador-decodificador: el procedimiento que reduce los datos de la
esencia al grabar y los reconstruye al reproducir. Casi todo lo que graba una cámara de televisión
está comprimido con pérdida: lo reconstruido no es idéntico al original, y la diferencia se
concentra en lo que el ojo nota menos (oficio).

La mayoría de los códecs de vídeo se apoyan en la transformada discreta del coseno: convierte cada
bloque de píxeles en coeficientes de frecuencia, y la compresión está en recuantificar esos
coeficientes, desechando sobre todo la información de altas frecuencias, el detalle muy fino. Esa
recuantificación es lo que introduce la pérdida. Los defectos que produce son bloques, contornos
sucios y detalle que «hierve» (oficio).

Comprimir es quitar lo que sobra. Y lo que sobra tiene dos formas:

- La redundancia: información repetida o predecible. Un cielo azul uniforme repite el mismo
  valor miles de veces; dos fotogramas consecutivos de un plano fijo son casi idénticos.
- La entropía: la información nueva o esencial, la que no se puede deducir de nada anterior.
  Es lo que queda cuando se ha quitado toda la redundancia, y es lo que hay que transmitir.

Las cuatro maneras de clasificar un códec:

| Eje | Términos | Diferencia |
|---|---|---|
| Qué se pierde | Sin pérdidas (*lossless*) / con pérdidas (*lossy*) | Si el descomprimido es idéntico al original o sólo se le parece |
| Cuántos fotogramas | Intraframe / Interframe | Si cada fotograma se comprime solo o mirando a los vecinos |
| Para qué | De producción / de distribución | Si prima la calidad y la edición o el tamaño del archivo |
| Tasa | Constante / variable | Si el flujo de bits es fijo o se adapta a la dificultad |

La compresión interframe es la que combina varios fotogramas a la vez: codifica un fotograma de
referencia entero y, a partir de él, sólo las diferencias. La intraframe comprime cada fotograma por
separado, como si fuera una fotografía, y por eso es la que se usa en producción: cualquier
fotograma se puede abrir sin reconstruir los anteriores, que es lo que un montador necesita.

### El muestreo cromático

El muestreo cromático dice cuántas muestras de color se guardan por cada muestra de luminancia.
Se escribe con tres cifras sobre un bloque de referencia de cuatro píxeles de ancho por dos filas: la
primera es ese ancho, y las otras dos, cuántas muestras de color hay en la primera fila y en la
segunda; una cuarta cifra, si la hay, es la del alfa (oficio).

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

Y una cuarta cifra puede aparecer. Un archivo de vídeo con muestreo cromático 4:4:4:4 lleva una señal
sin submuestreo de color, en RGB o en YCbCr, más el canal alfa. Apple lo dice así: **«The sampling
nomenclature for such Y’CBCRA or RGBA images is 4:4:4:4, to indicate that for each pixel location,
there is an alpha—or A—value in addition to the three Y’CBCR or RGB values.»** Qué es el canal
alfa: un cuarto canal que dice, píxel a píxel, cuánto de opaco es. No lleva color: lleva
transparencia. Es lo que permite superponer un rótulo o un elemento de grafismo sobre otra imagen sin
recortarlo a mano. Cuando un muestreo lleva cuarta cifra, ésa es la del canal alfa (oficio).

Lo que el submuestreo le hace al grafismo (oficio): un rótulo de color saturado sobre un fondo pierde
definición en el borde, porque el color se guarda a menor resolución que el brillo. Un texto rojo fino
sobre azul es el caso peor; un texto blanco o amarillo con un borde o una sombra que lo separe del
fondo aguanta mejor el paso a 4:2:0 de la distribución. Por eso el grafismo se crea en 4:4:4 (RGB) y
se comprueba en la señal que va a salir, no sólo en el fichero de trabajo.

### La profundidad de bits y los niveles

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

El *banding* es el defecto que más persigue al grafista: un fondo en degradado amplio y suave (un
cielo, un fundido de color corporativo) puede verse en franjas si se exporta o se emite con pocos
bits, aunque en la pantalla del ordenador se viera limpio. Se diseña y se exporta a 10 bits cuando el
formato lo admite, y se comprueba en un monitor de vídeo (oficio).

Los programas de diseño trabajan en rango completo (0 a 255 en 8 bits), y la televisión, en rango
estrecho (16 a 235) (oficio). En Viz Engine, por ejemplo, la señal de llave tiene una opción que hace
esa conversión: **«Downscale Luma: Compresses the luminance range of
the output key signal from 0-255 to 16-235. Default mode is Active.»** (*Viz Engine Administrator
Guide* 5.4, «Video Output»; la comprime al rango de vídeo y viene activada de fábrica).

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

Para el grafista, los límites se traducen en dos reglas (oficio, sobre la R 103): un grafismo que se
ve perfecto en el ordenador puede ser ilegal en emisión, porque un blanco puro o un rojo muy saturado
de la paleta de un programa de diseño pueden quedar fuera del rango preferente al pasar a vídeo; y lo
que decide es el monitor de vídeo calibrado y los instrumentos de medida, no la pantalla del puesto.
Una pieza de grafismo es material preproducido: se entrega dentro de los límites nominales. Los
motores de grafismo tienen además sus propios controles de salida; Viz Engine los describe así:
**«Allow Super White: Allows the luminance of the output signal to exceed the nominal SMPTE pixel
values (100 IRE units) when enabled. Default mode is Inactive.»**, y **«Allow Chroma Clipping:
Determines whether to clip over-saturated chroma levels in the active portion of the output video
signal.»** (*Viz Engine Administrator Guide* 5.4, «Video Output»): por defecto, no deja pasar el blanco
por encima del nominal.

### Intracuadro y GOP largo

Es la distinción que más importa al elegir un códec. Un fabricante la resume así: **«Intra/Long GOP
is a movie compression format. Intra compresses the movie by frame, and Long GOP compresses multiple
frames. Intra compression has better response and flexibility when editing, but Long GOP compression
has better compression efficiency.»** (Sony, *Help Guide ILCE-1*, «File Format (movie)»).

Otro fabricante lo explica por sus efectos: el GOP largo **«is usually used for content delivery and
packaged media»**, pero **«any image manipulation or processing will severely degrade the image
quality in long GOP compression schemes»**; en cambio, **«Intra frame compression processes the
entire image within the boundaries of each video field or frame. There is zero interaction between
adjacent frames, so its image quality stands up well to motion and editing.»** (Panasonic, *AVC-Intra
FAQ*, pregunta 2; es documentación comercial de quien vende un códec intracuadro, y así se lee).

| | Intracuadro | GOP largo |
|---|---|---|
| Qué comprime | Cada cuadro por separado | Varios cuadros juntos, aprovechando lo que se repite |
| Tasa para una calidad dada | Mayor | Menor |
| Ficheros | Más grandes | Más pequeños |
| Montaje | Más ligero para el ordenador; corte en cualquier cuadro | Más carga; sufre con cada nueva codificación |
| Movimiento rápido | Lo aguanta bien | Lo sufre |
| Uso típico | Producción, material que se va a montar mucho | Informativos con prisa, envíos, larga duración, distribución |

(Tabla de oficio a partir de las dos citas.)

La regla de oficio que lo resume: para editar, intracuadro; para distribuir, intercuadro (el GOP
largo es compresión entre cuadros sucesivos, también llamada temporal).

### H.264 y H.265

Son las dos normas de compresión más extendidas, y las usan muchos formatos de cámara con nombre
propio. Una guía de Sony las presenta así: el XAVC S **«records movies in the widely used MPEG-4
AVC/H.264 codec and therefore enables you to view and edit movies on various compatible devices»**; el
XAVC HS **«records high image quality movies with rich gradations and smaller file sizes using the
MPEG-H HEVC/H.265 codec with 10-bit color sampling»** (Sony, ILCE-7SM3, «Characteristics of each file
format»). El H.265 comprime más a igual calidad, a cambio de más cálculo al decodificar: la misma
guía pide editarlo con **«a video editing software compatible with MPEG-H HEVC/H.265 codec»** y
**«a computer with high processing capability»**.

La compatibilidad es su punto débil también en la transmisión: al elegir el códec de *streaming*,
el manual de la Z200 avisa de que **«When [Codec] is set to [H.265/HEVC], some receivers may not
support playback correctly.»** (p. 202).

Que H.264 no es sinónimo de GOP largo lo muestra el AVC-Intra (más abajo).

### Apple ProRes

**«Apple ProRes is a family of proprietary, lossy compressed, high quality video intermediate codecs
primarily supported by the Final Cut Pro (FCP) suite of post-production and editing software
programs.»** (LOC, fdd000389). Es un códec «intermedio», pensado para la posproducción: **«ProRes was
designed to be a high quality intermediate codec that keeps post-production workflow data at 10-bit
quality»**.

- Dos ramas: **«the Apple ProRes 422 Codec Family (described here) and the Apple ProRes 4444 Codec
  Family»**. La 422 tiene cuatro miembros: **«Apple ProRes 422 Proxy»**, **«Apple ProRes 422 LT»**,
  ProRes 422 y **«Apple ProRes 422 HQ»**; la 4444 incluye el **«4444 XQ»**.
- Rasgos de la familia 422: **«4:2:2 source material»**, **«10-bit sample depth»**, **«intrafame
  (I-frame) only»** [sic] y **«variable bit rate»**.
- Contenedor: **«ProRes codecs are usually contained within the QuickTime "mov" wrapper but starting
  with Final Cut Pro 10.3 released on October 27, 2016, the option for using ProRes in the MXF
  Generic Container was added as an option for broadcast delivery.»**
- Calidad frente a tasa, citando a Apple: **«PSNR for Apple ProRes 422 HQ is 15–20 dB higher than
  that for Apple ProRes 422 Proxy, but the Apple ProRes 422 HQ stream has nearly five times the data
  rate of the Apple ProRes 422 Proxy stream.»**

La rama 4444 es la del grafismo. Apple la describe en su documento técnico *Apple ProRes* (abril de
2022): **«Apple ProRes 4444: An extremely high-quality version of ProRes for 4:4:4:4 image sources
(including alpha channels).»**, y **«Apple ProRes 4444 is a high-quality solution for storing and
exchanging motion graphics and composites, with excellent multigeneration performance and a
mathematically lossless alpha channel up to 16 bits.»** De la 4444 XQ: **«Like standard Apple ProRes
4444, this codec supports up to 12 bits per image channel and up to 16 bits for the alpha channel.»**
Sus tasas objetivo: para la 4444,
**«approximately 330 Mbps for 4:4:4 sources at 1920 x 1080 and 29.97 fps»**; para la 4444 XQ,
**«approximately 500 Mbps for 4:4:4 sources at 1920 x 1080 and 29.97 fps»**. El mismo documento da
también las del resto de la familia, todas en 1.920 × 1.080 a 29,97 fps:

| Variante | Tasa objetivo según Apple | Muestreo |
|---|---|---|
| ProRes 4444 XQ | **«approximately 500 Mbps»** | 4:4:4 (4:4:4:4 con alfa) |
| ProRes 4444 | **«approximately 330 Mbps»** | 4:4:4 (4:4:4:4 con alfa) |
| ProRes 422 HQ | **«approximately 220 Mbps»** | 4:2:2 |
| ProRes 422 | **«approximately 147 Mbps»** | 4:2:2 |
| ProRes 422 LT | **«approximately 102 Mbps»** | 4:2:2 |
| ProRes 422 Proxy | **«approximately 45 Mbps»** | 4:2:2 |

Apple añade que la 422 va **«at 66 percent of the data rate»** de la 422 HQ, y que la LT lleva
**«roughly 70 percent of the data rate»** de la 422. Y lo que importa al grafista: **«Apple ProRes 4444
XQ and Apple ProRes 4444 are ideal for the exchange of motion graphics media because they are
virtually lossless, and are the only ProRes codecs that support alpha channels.»**

Una cuenta que se pide (cálculo, sobre la cifra de Apple, que es a 29,97 fps): un minuto de ProRes 4444
en 1.920 × 1.080 a unos 330 Mb/s son 330 × 60 = 19.800 megabits, es decir, unos 2.475 MB (dividiendo
entre 8), cerca de 2,5 GB. Frente a los unos 12,4 GB del minuto de secuencia TGA sin comprimir del
epígrafe 1 (que es a 25 fps), la diferencia explica por qué se entrega en ProRes 4444.

### Avid DNxHD (SMPTE VC-3)

**«Avid DNxHD is a revolutionary 10 and 8-bit HD encoding technology that significantly reduces
storage and bandwidth requirements while providing mastering-quality HD media.»** Está
**«Codified by SMPTE as VC-3 standard»**; su norma de mapeo en MXF es la **«SMPTE 2019-4 Mapping
VC-3 Coding Units into the MXF Generic Container»**, y **«Avid applications store Avid DNxHD material
natively inside industry-standard MXF files»** (Avid, *Avid DNxHD Technology*, 2012).

El códec **«offers a choice of 8 or 10-bit sampling»** y seis tasas a elegir. La tabla de calidad
del mismo documento («Avid DNxHD encoding quality») da, para cada variante, profundidad, muestreo y
tasa («Bandwidth»); la tabla no dice a qué cadencia. En la 220x, la 220 y la 145, el texto precisa
que el número es la tasa a 1080 entrelazado a 30 cuadros (60 campos), no a 25. En la 444 el número
no es la tasa: la tabla le da **«440 Mb/sec»**.

| Variante | Bits, muestreo y tasa (tabla de Avid) | Qué dice Avid |
|---|---|---|
| DNxHD 444 | 10 bits; 4:4:4; 440 Mb/s | **«10-bit 4:4:4 RGB video sampling»** |
| DNxHD 220x | (la tabla agrupa la 220 y la 220x: 8 y 10 bits; 4:2:2; 220 Mb/s) | **«For superior quality image in a YCbCr-color space for 10-bit sources»**; **«220Mbps is the data rate for 1920 x 1080 30fps interlace sources (60 fields) while progressive sources at 24fps will be 175Mbps»** |
| DNxHD 220 | Ídem | **«For highest quality image when using 8-bit color sources»** |
| DNxHD 145 | 8 bits; 4:2:2; 145 Mb/s | **«145Mbps is the data rate for 1920 x 1080 30fps interlaced sources (60 fields). Progressive sources at 24fps will be 115Mbps and at 25fps will be 120Mbps.»** |
| DNxHD 100 | 8 bits; 4:2:2; 100 Mb/s | **«Sub-samples the video raster from 1920 to 1440 or from 1280 to 960»** |
| DNxHD 36 | 8 bits; 4:2:2; 36 Mb/s | **«High-quality offline editing of HD progressive sources only.»** |

Como el nombre sigue a la tasa, a 25 cuadros las variantes cambian de número. La tabla de
resoluciones del mismo documento («Avid DNxHD family of mastering resolutions») da, para 1080i/50,
la 185x (10 bits) y la 185 (8 bits), las dos a 184 Mb/s; la 120, a 121 Mb/s; y la 85, a 84 Mb/s,
esta con la imagen reducida a 1.440 × 1.080 (**«Sub-sampled to 1440x1080»**). Para 1080p/25 repite
esas cuatro y añade la 365x (10 bits, 4:4:4, 367 Mb/s) y la 36, a 36 Mb/s. Todas son 4:2:2 salvo la
365x.

Su sucesor para resoluciones mayores que HD (DNxHR) no se ha leído en fuente de Avid.

Del canal alfa, el documento de Avid de 2012 no dice nada: la palabra *alpha* no aparece en él. Con lo
leído no se puede afirmar que el DNxHD lleve alfa; el códec con alfa documentado en este tema es el
ProRes 4444.

### AVC-Intra (Panasonic)

**«AVC-Intra … is a professional intra-frame video codec with bit rates of 50 and 100Mb/s, utilizing
the High 10 Intra and High 422 Intra profiles of H.264 respectively.»** Tiene **«two modes: AVC-Intra
100 … and AVC-Intra 50»**; el de 100 es **«4:2:2, 10-bit Intra-frame coding»** y **«records the full
1920x1080 raster»** (Panasonic, *AVC-Intra FAQ*, preguntas 1 y 4). Se graba en MXF OP-Atom en
tarjetas P2 y **«AVC-Intra supports MXF metadata.»** (preguntas 12 y 13).

Es un ejemplo de que «H.264» no es sinónimo de GOP largo: la norma tiene perfiles intracuadro, y
AVC-Intra usa esos.

### Cuadro resumen

| Nombre | Qué es | Compresión | Contenedor habitual |
|---|---|---|---|
| H.264 (AVC) | Norma de compresión | GOP largo o intracuadro, según perfil | MP4, MXF, MOV |
| H.265 (HEVC) | Norma de compresión, más eficiente | En cámara, GOP largo | MP4 |
| XAVC | Familia de formatos de Sony | H.264 o H.265; intra o GOP largo | MP4 o MXF |
| AVC-Intra | Códec de Panasonic sobre H.264 | Intracuadro, 50 y 100 Mb/s | MXF OP-Atom |
| ProRes | Familia de códecs intermedios de Apple | Intracuadro, tasa variable | MOV (también MXF) |
| DNxHD | Códec de Avid, norma SMPTE VC-3 | De 36 a 440 Mb/s según variante; el tipo de compresión no lo desarrolla el documento de Avid leído | MXF (también MOV) |
| LPCM | Audio sin comprimir | — | Dentro del fichero de vídeo |

### Los contenedores

| Contenedor | Quién lo desarrolló | Dónde se ve |
|---|---|---|
| MXF | Normalizado por la SMPTE | El contenedor profesional de televisión: cámaras de broadcast, servidores, intercambio y archivo |
| MOV | Apple (QuickTime) | Posproducción; el habitual de ProRes |
| MP4 | La familia de normas MPEG | Cámaras de gama media y ligeras; distribución |
| AVI | Microsoft | Informática doméstica; poco en televisión |

(Quién desarrolló cada uno: oficio.)

El MXF es el que más se pregunta. La Biblioteca del Congreso de Estados Unidos lo describe así:
**«Object-based file format that wraps video, audio, and other bitstreams ("essences"), optimized for
content interchange or archiving by creators and/or distributors, and intended for implementation
in devices ranging from cameras and video recorders to computer systems.»** Recoge que **«most
commentators say "MXF should be seen as the 'digital equivalent of videotape,'"»**, y que **«The
central specification is SMPTE ST 377-1:2011, Material Exchange Format (MXF) -- File Format
Specification»** (Library of Congress, *Sustainability of Digital Formats*, fdd000013).

El MXF es un contenedor, no un códec: no dice nada sobre cómo está comprimido lo que lleva dentro, y
puede envolver material de casi cualquier códec. Lo que distingue unos MXF de otros es el patrón
operacional, que dice cómo se reparten las pistas dentro del fichero:

| Patrón | Norma | Cómo empaqueta | Dónde se usa |
|---|---|---|---|
| OP1a | **«SMPTE ST 378:2004 (Archived 2010) … Operational Pattern 1a (Single Item, Single Package)»** | Todo en un solo fichero: vídeo y todas las pistas de audio juntas | El fichero autónomo: emisión, intercambio y gran parte de las cámaras |
| OP-Atom | **«SMPTE ST 390:2011 … Specialized Operational Pattern "Atom" (Simplified Representation of a Single Item)»** | Un fichero por pista: uno de vídeo y uno por cada canal de audio | El entorno de edición de Avid; y las cámaras P2 de Panasonic |

(Normas: LOC, fdd000013; el reparto de usos es oficio.)

Para el grafista, la consecuencia es que el nombre de la extensión no dice si un fichero lleva alfa: un
MOV puede llevar ProRes 422 (sin alfa) o ProRes 4444 (con alfa), y lo que decide es el códec de dentro
(se deduce de la cita de Apple). Al pedir o entregar una pieza con transparencia se nombra el códec,
no sólo el contenedor.

## 3. Alfa

### Qué es el canal alfa

Una transparencia alfa es un canal que almacena información de opacidad: un cuarto canal, junto a los
tres de color, que para cada píxel dice cuánto se ve.

| Valor del canal alfa | Qué ocurre con el píxel |
|---|---|
| Negro, o 0 | Totalmente transparente |
| Blanco, o el máximo | Totalmente opaco |
| Gris intermedio | Semitransparente: es lo que hace posible un borde suave |

Por qué los grises son lo importante y no los extremos: un recorte que sólo tuviera negro y blanco daría
un borde de sierra. Los valores intermedios son los que dan el borde limpio, y por eso un canal alfa de
un bit no sirve para vídeo.

(Tabla y explicación, oficio.) En la notación del muestreo, el alfa es la cuarta cifra de 4:4:4:4
(epígrafe 2). En el vídeo se cuenta por componente, como los otros canales: ProRes 4444 guarda el alfa
con hasta 16 bits (epígrafe 2).

### Los ficheros gráficos que llevan alfa

El canal alfa es la máscara de transparencia que un fichero gráfico puede llevar dentro, y es la
señal de recorte de una incrustación guardada en el propio archivo.

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
precisamente el canal alfa. En gráficos, «bits» se cuenta por píxel; en vídeo se cuenta por
componente. Una imagen de «8 bits» en vídeo tiene 8 bits por cada componente —24 en total— y una
imagen de «32 bits» en gráficos los tiene en total. Es la misma palabra con dos unidades.

La tabla y las cuentas son de oficio. El cuadro completo de los ficheros de trabajo y de entrega, con su
familia y su transparencia (oficio):

| Formato | Familia | Transparencia | Para qué se usa |
|---|---|---|---|
| PSD | Mapa de bits, nativo | Sí, con capas | Trabajo en curso |
| AI | Vectorial, nativo | Sí | Trabajo en curso |
| TIFF | Mapa de bits | Sí | Artes gráficas, archivo |
| PNG | Mapa de bits | Sí, canal alfa | Web y grafismo sobre fondo |
| JPG | Mapa de bits, con pérdida | No | Fotografía |
| TGA | Mapa de bits | Sí, canal alfa | Secuencias de fotogramas |
| GIF | Mapa de bits, 256 colores | Sí, de un solo valor | Animaciones cortas |
| SVG | Vectorial | Sí | Web |
| EPS | Vectorial | Según el caso | Intercambio con imprenta |

La regla que este cuadro deja para el examen: si la pregunta habla de transparencia y web, es PNG; si
habla de capas, es el nativo; si habla de secuencias de fotogramas renderizados, es TGA; si habla de
fotografía comprimida, es JPG.

El vídeo con alfa va en un códec que lo admita: en la familia de Apple, sólo **«Apple ProRes 4444 XQ
and Apple ProRes 4444 […] are the only ProRes codecs that support alpha channels.»** (*Apple ProRes*,
abril de 2022). Ningún ProRes 422 lleva alfa. Del DNxHD no consta en lo leído (epígrafe 2).

### Alfa directo y alfa premultiplicado

Un fichero con alfa puede guardar el color de dos maneras, y confundirlas es un error corriente con los
grafismos que salen de un programa 3D (oficio). Blackmagic Design las define en el manual de DaVinci
Resolve 21 (cap. 77, p. 1726; «Unpremultipled», así, en el original):

| | Directo (*straight*) | Premultiplicado (*premultiplied*) |
|---|---|---|
| Qué es | **«Unpremultipled (Straight): An RGB image unaltered by the semi-transparency information in a fourth channel (alpha channel)»** | **«Premultiplied: An RGB image that has each channel multiplied by its alpha channel before compositing.»** |
| Quién lo usa, según el glosario de Blender 5.2 | **«This is the alpha type used by paint programs such as Photoshop or Gimp, and used in common file formats like PNG, BMP or TARGA.»** | **«This is the natural output of render engines»**; **«The OpenEXR file format uses this alpha type.»** |

En el premultiplicado, **«The alpha channel itself is not multiplied. The R, G, and B channels are
multiplied by the alpha.»**, y **«Most computer-generated images are premultiplied for convenience»**
(p. 1727). Las cuatro reglas del manual (p. 1728): **«Always use premultiplied images with a Merge
node. / Only color-correct images that are not premultiplied. / Always filter and transform images
that are premultiplied. / Never double premultiply an image.»** Si se trata como premultiplicada una
imagen que no lo está, **«the pixels that should be transparent are still added, which typically
results in an unwanted bright fringe around the edges of your foreground subject.»**: sale un halo claro
alrededor del borde. Y pasar de uno a otro no es gratis: **«Conversion between the two alpha types is
not a simple operation and can involve data loss»** (Blender).

La consecuencia para la entrega (oficio, sobre las citas): quien exporta dice de qué tipo es el alfa, y
quien recibe lo interpreta igual. La composición y sus técnicas son el tema 5.

### El alfa en directo: relleno y llave

En un control, el grafismo de directo no llega al mezclador como fichero, sino como señal. Como una
señal de vídeo no tiene cuarto canal, el alfa sale del motor de grafismo como una segunda señal: el
relleno (*fill*) lleva la imagen en color y la llave (*key*) dice dónde es opaca y dónde transparente
(oficio). Vizrt lo describe en su modo de doble canal: **«Dual Channel is a video version with,
typically, two program outputs (fill and key on two channels).»** (*Viz Engine Administrator Guide*
5.2, «Dual Channel Mode»).

Las propiedades de la llave en Viz Engine (*Viz Engine Administrator Guide* 5.4, «Video Output»):

| Propiedad | Qué hace (Vizrt) |
|---|---|
| Contains Alpha | **«Defines if this output channel provides key information on the associated key output connector.»** |
| Downscale Luma | **«Compresses the luminance range of the output key signal from 0-255 to 16-235. Default mode is Active.»** |
| Invert Luma | **«Inverts the luminance part of the output key signal (inverts the key).»** |
| Watchdog Key Opaque | **«Specifies if the output key must be opaque or transparent when the watchdog unit activates.»** |

Y las dos señales tienen que llegar a la vez: **«The fill and key channels are set with this
H-delay.»** (el mismo retardo horizontal para las dos). Un relleno y una llave desfasados dan un borde
desplazado o un halo (oficio).

En el mezclador, la mosca y los rótulos entran en la composición posterior. El manual de los
mezcladores ATEM, que llama «composición posterior» al DSK, explica por qué: **«Una composición
posterior siempre se superpone a los restantes elementos, incluida la transición. Por tal motivo,
resulta ideal para insertar logotipos y textos móviles.»** El mezclador puede guardar él mismo
grafismos fijos con su transparencia: en los ATEM, el panel multimedia **«permite guardar imágenes con
sus respectivos canales alfa, que luego pueden asignarse a un reproductor para usarlas durante la
producción»**.

En una instalación sobre red IP, la señal de llave también se declara: la norma SMPTE ST 2110-20:2022,
que transporta el vídeo sin comprimir, incluye entre los valores de colorimetría de cada flujo el de
**«ALPHA»**, y obliga a la señal de llave a declararlo y le prohíbe declarar curva de transferencia:
**«the Key stream shall signal the colorimetry value “ALPHA”, and shall not signal a TCS value.»**
(§ 7.4.1); por eso, para un receptor, **«If the TCS value is not specified, receivers shall assume the
value SDR, unless the sampling keyword indicates the signal is a KEY signal, in which case the TCS
value is not meaningful.»** (§ 7.6). TCS es el sistema de transferencia: SDR, PQ o HLG, entre otros
valores (epígrafe 6).

### Los errores de entrega con el alfa

- Entregar sin alfa: un grafismo entregado en un formato sin alfa llega al control con un fondo negro
  pegado. Es el error de entrega más frecuente, y no se ve hasta que el rótulo entra en emisión. Un
  rótulo, una mosca o un logotipo que tiene que ir encima de la imagen se pide en PNG o TIF con alfa, o
  como par relleno-recorte; si llega en JPG, llega con fondo y tapa la imagen.
- Confundir directo y premultiplicado: halo claro u oscuro en el borde (epígrafe anterior).
- Exportar el alfa en un códec que no lo lleva: un MOV en ProRes 422 no lo tiene (se deduce de la
  cita de Apple).
- Relleno y llave desfasados o con la llave invertida: el recorte sale en negativo o desplazado.

(Los avisos de la lista son oficio.)

## 4. Zonas seguras (*safe areas*)

### Qué es una zona segura y por qué sigue existiendo

La SMPTE lo define en la introducción (informativa) de su norma ST 2046-1:2009, *Specifications for
Safe Action and Safe Title Areas for Television*: **«A safe area, in the context of television
production, is the area of the image that is certain to be seen by the vast majority of viewers in
the home. Historically, two types of safe areas are specified, the Safe Action Area and the Safe Title
Area. They differ in that the extremes of the Safe Action Area are deemed usable even if there is some
degree of geometric, chromatic or other distortion, whereas the Safe Title Area must be free of these
distortions.»**

| Zona | Qué garantiza |
|---|---|
| Zona segura de acción | Que lo que ocurre dentro se ve en cualquier pantalla |
| Zona segura de títulos | Que el texto no se corta: es más estrecha que la anterior |

(Tabla de oficio.) La EBU llama a la segunda zona segura de grafismo (*Graphics Safe Area*) y la
SMPTE, de título (*Safe Title Area*): es la misma idea con distinto rótulo.

Los márgenes nacieron con los televisores de tubo, que recortaban los bordes de la imagen (oficio;
la SMPTE dice que los de sus documentos anteriores, la RP 218 y la RP 27.3, **«were based on analog transmission and CRT
displays»**). Y explica por qué los redujo: **«the complete replacement of scanned analog imagers and displays by
fixed-pixel-matrix imagers and displays has eliminated the need for large tolerances in image
geometry, convergence and displayed area.»** Y añade un aviso en sentido contrario, porque hoy la
pantalla puede enseñarlo todo (§ 5, nota): **«many consumer fixed-pixel-matrix displays can be
configured to show the entire image area. It is critically important to ensure that the entire image
area is kept clear of extraneous elements such as lighting instruments, boom shadows, cables and
graphics that are not intended to be seen by the viewer.»** Para el grafista: nada que no deba verse
puede quedar fuera de la zona segura con la idea de que «no sale».

Por qué siguen existiendo si hoy las pantallas no recortan: porque el material se reencuadra. Una
pieza de 16:9 recortada a vertical para redes pierde los laterales, y el texto que estaba fuera de la
zona segura desaparece.

### La EBU R 95

Los rótulos se colocan dentro del cuadro de la imagen, que en alta definición es de 16:9.
Dentro de ese cuadro, la Unión Europea de Radiodifusión fija dos zonas seguras en su
Recomendación EBU R 95, *Safe areas for 16:9 television production* (versión 1.1, junio de 2017):
«**all essential action should be protected inside an Action Safe Area, and all graphics inside a
Graphics Safe Area**». Su recomendación, dirigida a quien hace programas en 16:9, es encuadrar de
modo que:

- «**where appropriate, all essential action takes place inside the Action Safe Area**» (lo
  esencial de la acción, dentro de la zona segura de acción);
- «**all graphics are framed in the Graphics Safe Area**» (los grafismos y rótulos, dentro de la
  zona segura de grafismo);
- «**the centre of the image retains its position throughout all production processes unless there
  are creative reasons to deliberately do otherwise**» (el centro de la imagen no se desplaza en la
  cadena de producción).

Las medidas: «**The action safe area is 3.5% and the graphics safe area is 5%, at the top, bottom
and lateral parts of the image.**» (nota 5). Es un margen en cada borde; restados los dos lados,
lo seguro para la acción es el 93 % central del ancho y del alto, y para el grafismo, el 90 %
(resta, no cifra de la norma). La zona de grafismo es, por tanto, la más estrecha. La norma da
además los valores exactos en líneas y píxeles para 576i, 720p, 1080i/1080psf, 1080p, 2160p y
4320p (figuras 1 a 6).

Los valores de la EBU R 95 para 1080p (figura 4) y 2160p (figura 5) son estos; en 1080p las líneas se
numeran dentro del cuadro digital completo de 1125, donde las activas van de la 42 a la 1121:

| Formato | Zona segura de acción | Zona segura de grafismo |
|---|---|---|
| 1080p (1920 × 1080) | 67 píxeles por lado y 38 arriba y abajo: 1786 píxeles de ancho, líneas 80 a 1083 | 96 píxeles por lado y 54 arriba y abajo: 1728 píxeles de ancho, líneas 96 a 1067 |
| 2160p (3840 × 2160) | 134 píxeles por lado y 76 arriba y abajo: 3572 × 2008 píxeles | 192 píxeles por lado y 108 arriba y abajo: 3456 × 1944 píxeles |

El 90 % de 1920 (1728) coincide, pues, con el ancho normalizado de la zona de grafismo en 1080p. La
figura de 1080i/1080psf (figura 3) tiene los mismos anchos. En las tres figuras la norma marca además,
en el centro, la zona segura de rótulos para una presentación en 4:3: 1296 píxeles de ancho en 1080 y
2592 en 2160p.

### La SMPTE ST 2046-1

La norma norteamericana es la SMPTE ST 2046-1:2009, aprobada el 23 de noviembre de 2009, que la
biblioteca de la SMPTE da como **«active»** y con una sola publicación: es la vigente. **«This
Standard is a comprehensive revision of SMPTE RP 218-2002, Specifications for Safe Action and Safe
Title Areas for Television Systems.»** Su alcance (§ 1): **«This Standard defines and specifies Safe
Action and Safe Title Areas for 1920 x 1080, 1280 x 720, 720 x 576 and 720 x 480 television formats.
This document is intended for application in program production where the image aspect ratio of the
acquired essence is the same as that of the display.»** No da valores para 3.840 × 2.160, y avisa de
que **«They do not offer guidance in situations where material generated in one aspect ratio may need
to be displayed in a different aspect ratio.»** (esa protección de otras proporciones la trata la
SMPTE RP 2046-2, que no se ha leído).

Las definiciones (§ 4.4 y 4.5): **«The Safe Action Area is the maximum image area within which all
significant action shall be contained. The image area defined by the Safe Action Area is concentric
with the Production Aperture.»**; **«The Safe Title Area is the maximum image area within which all
significant title information shall be contained.»** La *Production Aperture* es (§ 4.3) **«the
Image Lattice that represents the maximum possible active image area in a given image format»**: la
imagen activa entera.

Los valores (§ 5.1 a 5.4), con **«shall»**, es decir, obligatorios dentro de la norma:

| Formato | Zona segura de acción (93 %) | Zona segura de título (90 %) |
|---|---|---|
| 1920 x 1080 | **«93% of the width and 93% of the height of the Production Aperture (1786 x 1004)»** | **«90% of the width and 90% of the height of the Production Aperture (1728 x 972)»** |
| 1280 x 720 | **«(1190 x 670.)»** | **«(1152 x 648.)»** |
| 720 x 576, **«regardless of Aspect Ratio»** | **«(670 x 536)»** | **«(648 x 518.)»** |
| 720 x 480 | **«(670 x 446)»** | **«(648 x 432)»** |

Cuando la cuenta no da entero (§ 5): **«Safe area calculations resulting in non-integer values for
lines or pixel numbers shall be rounded to the nearest whole number.»** Por ejemplo (cálculo),
1.920 × 0,93 = 1.785,6, que se redondea a 1.786, y 1.080 × 0,93 = 1.004,4, que queda en 1.004.

Dos salvedades de la misma norma. Para 480 líneas admite todavía los márgenes antiguos de la RP 218
(§ 5.4): **«the Safe Action Area shall be 90% of the width and 90% of the height of the 720 x 480
Image Lattice (648 x 432). The Safe Title Area shall be 80% of the width and 80% of the height of the
720 x 480 Image Lattice (576 x 384).»** Y para 576 líneas recuerda que hay otra especificación
(§ 5.3): **«A different safe-area specification was developed by ITU-R for use during the transition
period to wide-screen 16:9 broadcasting, and is still in use in some regions where 576-line formats
are used.»** (su bibliografía cita la Recomendación UIT-R BT.1379-2, que no se ha leído).

### Las dos normas, comparadas

| | EBU R 95 v1.1 | SMPTE ST 2046-1:2009 |
|---|---|---|
| Cómo lo expresa | Margen por borde: 3,5 % (acción) y 5 % (grafismo) | Porcentaje del total: 93 % (acción) y 90 % (título) |
| Nombre de la zona de texto | *Graphics Safe Area* | *Safe Title Area* |
| Formatos | 576i, 720p, 1080i/psf, 1080p, 2160p y 4320p | 1080, 720, 576 y 480 |
| En 1080 | Acción 1786 × 1004 (líneas 80 a 1083); grafismo 1728 × 972 (líneas 96 a 1067) | Acción 1786 × 1004; título 1728 × 972 |
| En 2160 | Acción 3572 × 2008; grafismo 3456 × 1944 | No lo trata |

(Comparación propia sobre las dos normas.) Un margen del 3,5 % a cada lado deja el 93 % central, y uno
del 5 %, el 90 %: en 1080 las dos normas dibujan las mismas cajas. Las 1.004 y 972 líneas de la EBU
salen de contar sus líneas (de la 80 a la 1083 son 1.004; de la 96 a la 1067, 972).

### El grafista y las zonas seguras

Las cuentas que se piden (cálculo sobre la R 95 y, en 720, sobre la ST 2046-1):

| Formato | Margen de grafismo a cada lado | Margen arriba y abajo | Caja útil para rótulos |
|---|---|---|---|
| 1.920 × 1.080 | 5 % de 1.920 = 96 píxeles | 5 % de 1.080 = 54 líneas | 1.728 × 972 |
| 3.840 × 2.160 | 192 píxeles | 108 líneas | 3.456 × 1.944 |
| 1.280 × 720 (SMPTE) | 64 píxeles | 36 líneas | 1.152 × 648 |

Lo que se hace con ellas (oficio):

- El rótulo, la mosca, el reloj, el marcador y los textos legales van dentro de la zona de grafismo;
  un fondo o una textura pueden llegar al borde, pero sin nada que haya que leer fuera de la caja.
- Las plantillas de rotulación se construyen con las guías de la zona segura dibujadas, y la mosca
  se ancla a la esquina de la zona de grafismo, no a la del cuadro.
- Si la pieza se va a recortar a 4:3, a cuadrado o a vertical, lo esencial se protege además en el
  centro (la R 95 marca un 4:3 central de 1.296 píxeles de ancho en 1080).
- Los subtítulos tienen su propia referencia: la norma estadounidense citada por la SMPTE (§ 5,
  nota) usa todavía el margen antiguo, **«All versions of CEA-708 reference the SMPTE RP 218 Safe
  Title Area, which is 80% of the width and 80% of the height of the Production Aperture.»** Los
  subtítulos en España y la accesibilidad son el tema 10.
- Las zonas seguras se comprueban en el monitor o en el multipantalla que las superpone, y en el
  ensayo con el rótulo más largo posible (el nombre y el cargo más largos del programa), no con el de
  prueba.

## 5. Colorimetría

### El color de la pantalla: síntesis aditiva, RGB y CMYK

El ojo humano tiene tres tipos de conos, sensibles a zonas distintas del espectro visible. De
ahí sale todo lo demás: como la percepción del color se reduce a tres respuestas, basta con tres
estímulos para reproducir cualquier color percibido. Eso es la síntesis aditiva, y es el
principio sobre el que funciona una pantalla.

Por síntesis aditiva del color es posible conseguir todos los colores percibidos mezclando tres
franjas del espectro visible en la proporción de intensidad adecuada, siempre que ninguno de los tres
iluminantes elegidos pueda obtenerse por mezcla de los otros dos: eso es la primera ley de
Grassmann.

Cian, magenta, amarillo y negro es el modelo de la tinta; rojo, verde y azul, el de la pantalla. Un
formato pensado para la web no necesita el de la tinta, y por eso no lo lleva: el PNG no admite el
modo CMYK, y el PSD, el JPG y el TIFF sí (oficio).

Lo que de ahí se sigue para el grafista (oficio): un logotipo o una imagen preparados para imprenta
en CMYK no se llevan tal cual a la pantalla; se convierten a RGB, y el color corporativo se fija con
sus valores RGB de pantalla, porque la misma referencia de tinta y de pantalla no dan el mismo color.
La adaptación del manual de marca a pantalla es el tema 2.

### Primarios y blanco de referencia

Cada recomendación de la UIT-R fija sus tres primarios y su blanco como coordenadas de cromaticidad
del diagrama de la CIE de 1931. Lo que queda dentro del triángulo que forman los tres primarios es la
gama de colores que el sistema puede representar.

| | BT.709-6 (HD) | BT.2020-2 (UHD) y BT.2100-3 (HDR) |
|---|---|---|
| Rojo (x, y) | **0.640**, **0.330** | **0.708**, **0.292** |
| Verde (x, y) | **0.300**, **0.600** | **0.170**, **0.797** |
| Azul (x, y) | **0.150**, **0.060** | **0.131**, **0.046** |
| Blanco de referencia | **D65**: **0.3127**, **0.3290** | **D65**: **0.3127**, **0.3290** |

(BT.709-6, punto 1.3 y 1.4; BT.2020-2, tabla 3; BT.2100-3, tabla 2, que da los mismos primarios que la
BT.2020 y describe cada uno como monocromático, **«630 nm»**, **«532 nm»** y **«467 nm»**.) El
blanco es el mismo en las tres; lo que cambia son los primarios, más saturados en la BT.2020: su gama
es más amplia. El Informe UIT-R BT.2408-9 lo expresa como meter un espacio dentro de otro: el
contenido con colorimetría BT.709 **«may be placed in a BT.2020 container»** (§ 5.1; la cita
completa, en el epígrafe 6).

Lo que eso le supone al grafista (oficio): un color corporativo muy saturado puede caber en la gama
BT.2020 y no en la BT.709; en un programa HD SDR, lo que se sale se recorta o lo recorta el
legalizador. Por eso el color de marca se comprueba en el espacio de destino, y en el vectorscopio,
no a ojo.

### La luminancia: la señal Y

La televisión no transmite rojo, verde y azul. Transmite una señal de luminancia y dos de
diferencia de color, porque el ojo distingue mucho mejor los detalles de brillo que los de color, y
eso permite dedicar menos ancho de banda al color sin que se note.

La luminancia se construye pesando los tres primarios, y los pesos no son iguales: el verde
aporta la mayor parte del brillo percibido y el azul la menor.

| Recomendación | Para qué | R | G | B |
|---|---|---|---|---|
| UIT-R BT.601 | Definición estándar | 0,299 | 0,587 | 0,114 |
| UIT-R BT.709 | Alta definición | 0,2126 | 0,7152 | 0,0722 |
| UIT-R BT.2020 | Ultra alta definición | 0,2627 | 0,6780 | 0,0593 |

(BT.709-6, punto 3.2, **«Derivation of luminance signal»**; BT.2020-2, tabla 4; BT.601-7.) En
fórmula, para la alta definición: Y = 0,2126 R + 0,7152 G + 0,0722 B. Los tres coeficientes de
cualquiera de estas recomendaciones suman exactamente uno.

Para el grafismo tiene una consecuencia directa (oficio): dos colores de brillo aparentemente
parecido en la paleta pueden tener luminancias muy distintas. Un texto azul puro sobre negro tiene muy
poca luminancia (el azul pesa un 7 % en la BT.709) y se lee mal; un amarillo, que suma rojo y verde,
tiene mucha. El contraste de un rótulo se juzga por la luminancia, y eso es lo que ve la forma de
onda. Los criterios de contraste accesible son el tema 10.

### Luminancia constante y no constante

| Sistema | Orden de las operaciones |
|---|---|
| Luma constante (CL) | Primero se calcula Y a partir del RGB lineal, y después se corrige la gamma |
| Luma no constante (NCL) | Primero se corrige la gamma de cada primario, y después se calcula Y' a partir del R'G'B' ya corregido |

La BT.2020-2 admite las dos (notas de la tabla 4): la constante **«may be used when the most accurate
retention of luminance information is of primary importance or where there is an expectation of
improved coding efficiency for delivery»**, y la no constante, **«when use of the
same operational practices as those in SDTV and HDTV environments is of primary importance through a
broadcasting chain»**. La BT.2100-3 no recoge la luminancia constante: junto
al formato no constante (tabla 6) da uno de intensidad constante (CI, *constant intensity*, la señal
ICtCp de su tabla 7: una componente de intensidad, **«I = 0.5L' + 0.5M'»**, y dos señales de diferencia
de color, CT y CP, que la nota 7a llama **«The newly introduced I, CT and CP symbols»**), y fija cuál manda: **«The Non-Constant Luminance (NCL) format is in widespread
use and is considered the default. The Constant Intensity (CI) format is newly introduced in this
Recommendation and should not be used for programme exchange unless all parties agree.»** La consecuencia visible del sistema no constante:
una parte de la luminancia se cuela por los canales de color, y cuando esos canales se submuestrean
—4:2:2, 4:2:0— se pierde brillo en los colores muy saturados (oficio).

### La gamma

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
Recomendación UIT-R BT.1886, que la BT.709 cita.

Por qué le importa al grafista (oficio): los programas de composición pueden trabajar en espacio
lineal o con gamma, y un degradado, un fundido o un desenfoque dan resultados distintos en cada uno.
Lo que se exporta tiene que llevar la curva que espera el destino (BT.709 en HD SDR; PQ o HLG en
HDR), y el fichero tiene que decirlo.

### Del programa de diseño a la señal de vídeo

Un grafismo nace en un programa de imagen fija o de composición, en RGB y en rango completo, y acaba
en una señal YCbCr de rango estrecho (epígrafe 2). El Informe UIT-R BT.2408-9 describe el problema de
los ficheros de imagen fija: **«Still Image formats are often RGB and therefore typically stored in full
range. There are instances where RGB still images are desired in narrow range.»** Y señala su
solución, los códigos de la Recomendación UIT-T H.273 (CICP, *Coding Independent Code Points*), que
señalan **«Colour Primaries»**, **«Transfer Function»**, **«Matrix Coefficients»** y **«Signal Range
(thru a Video Full Range Flag)»**: **«Now PNG, TIFF, AVIF, HEIF still image formats have the ability
to carry CICP information.»**, y **«CICP adds the ability to properly identify the signal range (full
range or narrow range) in RGB still image files.»** (§ 9).

El espacio de color que se da por supuesto en la web es el sRGB. Las WCAG 2.2 lo dicen así: **«Almost
all systems used today to view web content assume sRGB encoding.»** Lo define la norma IEC
61966-2-1:1999 (*Default RGB colour space - sRGB*), que el tema no ha leído directamente. Lo que de él
dicen documentos publicados que la citan:

- *Primarios y blanco: los de la BT.709.* El manual de Blender lo define como **«A widely used
  display-referred color space that uses the Rec.709 Primaries and a D65 white point.»** La
  especificación PNG del W3C (tercera edición, 2025), en su tabla 17 (**«gAMA and cHRM values for
  sRGB»**), da para el sRGB el blanco 0,3127 / 0,3290, el rojo 0,64 / 0,33, el verde 0,30 / 0,60 y el
  azul 0,15 / 0,06 (los guarda multiplicados por 100.000: **«31270»**, **«64000»**…), que son los de la
  BT.709-6 (véase «Primarios y blanco de referencia»).
- *La luminancia, con los pesos de la BT.709.* Las WCAG 2.2 del W3C, tomando la fórmula de la norma
  sRGB, definen la luminancia relativa como **«L = 0.2126 \* R + 0.7152 \* G + 0.0722 \* B»**.
- *La curva de transferencia es distinta.* Las mismas WCAG 2.2 dan la del sRGB, en el sentido que va
  del valor codificado a la luz lineal: **«if RsRGB <=
  0.04045 then R = RsRGB/12.92 else R = ((RsRGB+0.055)/1.055) ^ 2.4»** (igual para G y B), y la PNG
  guarda para el sRGB una gamma de **«45455»**, es decir, 1/2,2. La BT.709-6 fija la suya en el sentido
  contrario, de la luz a la señal, y con otra forma: V = 1,099 L^0,45 − 0,099, con un tramo recto de pendiente 4,500 por debajo de 0,018 (véase
  «La gamma»). El manual de Blender lo resume: el sRGB **«applies an approximate 2.2 gamma transfer
  function»**.
- *El rango.* Las WCAG normalizan cada valor de 8 bits dividiendo entre **«255»**: el 0 es el negro y
  el 255 el blanco, es decir, rango completo (deducción de esa fórmula), mientras que la señal de vídeo
  va en rango estrecho (epígrafe 2).

En resumen: sRGB y BT.709 comparten primarios y blanco D65, y difieren en la curva de transferencia
y en el rango de los valores. Por eso un grafismo diseñado en sRGB tiene los mismos colores posibles
que el HD (deducción de lo anterior), pero no se puede dar por buena la pantalla del ordenador como
referencia de emisión (oficio).
La regla de oficio que se sostiene con lo dicho: se trabaja con el espacio de color del proyecto fijado desde el principio, se
exporta diciendo espacio, curva y rango, y se comprueba el resultado en el monitor de vídeo y con los
instrumentos (forma de onda y vectorscopio), no en la pantalla del ordenador.

### Las LUT

Las LUT son tablas de consulta para transformar el color de una imagen: para cada combinación de
entrada de rojo, verde y azul, la tabla da una combinación de salida. No calcula: consulta. De ahí
el nombre, *look-up table*.

| Tipo | Qué hace |
|---|---|
| LUT técnica o de conversión | Traduce entre espacios: de logarítmico a Rec. 709, de una gama a otra. Es corrección, no estilo |
| LUT creativa o de *look* | Aplica un aspecto: una paleta, un viraje, un aire de época |
| LUT 1D | Una tabla por canal: cambia curvas de tono, no relaciones entre canales |
| LUT 3D | Una tabla sobre el cubo RGB: puede cambiar el tono y la saturación, no sólo el brillo |

(Tabla de oficio.) Para el grafista, una LUT técnica es la forma habitual de ver en SDR un material
HDR o logarítmico mientras se trabaja, o de convertir un grafismo de un espacio a otro; no sustituye
a la conversión que fija la BT.2408 (epígrafe 6) si el destino es un programa HDR (oficio).

## 6. HDR/SDR

### Qué es y qué recomendación lo fija

El rango dinámico es la distancia entre la luz más tenue y la más brillante que un sistema puede
registrar o mostrar a la vez. No es el número de colores —eso es el espacio de color— ni el número
de píxeles: es cuánto contraste cabe dentro de una misma imagen.

Un mayor rango dinámico da detalle simultáneo en las sombras y en las altas luces. Con rango
corto hay que elegir: o se expone para la ventana y el interior se va a negro, o se expone para el
interior y la ventana se quema. Con rango largo caben las dos cosas.

El alto rango dinámico (HDR) amplía la distancia entre el negro más oscuro y el blanco más brillante
que la imagen puede representar: no es más resolución, es más recorrido de brillo (oficio). Lo fija
la Recomendación UIT-R BT.2100-3 (febrero de 2025), que admite dos curvas de transferencia: **«the
Perceptual Quantization (PQ) or Hybrid Log-Gamma (HLG) specifications described in this
Recommendation should be used»**. Aquí interesa el HDR como formato: cómo se nombra, cómo se señala, qué niveles usa y cómo se
mezcla con el material SDR.

| | PQ | HLG |
|---|---|---|
| Qué dice la BT.2100-3 | **«achieves a very wide range of brightness levels for a given bit depth using a non-linear transfer function that is finely tuned to match the human visual system»** | **«offers a degree of compatibility with legacy displays by more closely matching the previously established television transfer curves»** |
| Referencia | Absoluta: cada código es una luminancia en pantalla; la fórmula llega a 10.000 cd/m² (el valor figura en la ecuación de la BT.2100-3) | Relativa al pico de cada pantalla (oficio) |
| Norma SMPTE | ST 2084, **«High Dynamic Range Electro-Optical Transfer Function of Mastering Reference Displays»** (publicada el 16-08-2014; estado en el catálogo, **«stabilized»**) | — |
| Uso habitual | Máster y plataformas (oficio) | Directo y emisión (oficio) |

Un formato HDR se define, así, por cinco datos (oficio, sobre la BT.2100-3): resolución (1.920 ×
1.080, 3.840 × 2.160 o 7.680 × 4.320), cadencia progresiva, 10 o 12 bits, gama de color de la
BT.2020/BT.2100 y curva PQ o HLG. Un HD con HDR es posible: la resolución y el rango dinámico son ejes
distintos (epígrafe 1).

### Los metadatos de masterizado

Un máster en PQ se suele acompañar de datos que describen el monitor en que se etalonó. La SMPTE los
normaliza en la ST 2086, **«Mastering Display Color Volume Metadata Supporting High Luminance and
Wide Color Gamut Images»** (publicaciones de 2014-10-13 y 2018-04-09; **«stabilized»**). El título lo
dice: son metadatos del volumen de color del monitor de masterizado; su contenido campo a campo no se
ha leído.

### Los perfiles de HDR

Fuera de las recomendaciones de la UIT, el HDR se entrega en perfiles de industria que ninguna norma
leída define; el manual de referencia de DaVinci Resolve 21 (Blackmagic Design, julio de 2026)
enumera cinco: **«Dolby Vision®»**, **«HDR10»**, **«HDR10+»**, **«HDR Vivid»** y **«Hybrid Log-Gamma
(HLG)»**. Los cuatro primeros usan la curva PQ, **«given that each of these standards rely upon the
same PQ curve»**; lo que los separa son los metadatos que acompañan a la imagen (oficio). Del HLG dice que
funciona **«without additional metadata»**.

El manual no usa los rótulos «estático» y «dinámico». El catálogo de la SMPTE sí: la norma que el
manual nombra para el HDR10+, la ST 2094-40, se titula **«Dynamic Metadata for Color Volume Transform
— Application #4»** (publicaciones de 2016-08-24 y 2020-04-09; **«stabilized»**). De ahí la
clasificación que se usa en el oficio: la ST 2086 describe el monitor de masterizado y vale para todo
el programa (metadatos estáticos); los de la ST 2094 cambian plano a plano (dinámicos). Llevan
metadatos plano a plano el HDR10+ y el Dolby Vision; el HDR10 se queda en los del máster, y el HLG no
lleva ninguno (oficio, sobre las citas del manual).


### Cómo se señala el HDR

Un fichero o un flujo HDR tiene que decir qué curva lleva; si no, el receptor lo interpreta mal. El
ejemplo normado es el transporte por red de la ST 2110-20 (la misma norma que declara la señal de llave, epígrafe 3): cada flujo de vídeo declara su
colorimetría (**«BT709»**, **«BT2020»**, **«BT2100»**…) y su sistema de transferencia (TCS), con
valores como **«SDR»**, **«PQ»** y **«HLG»**. Y la regla por defecto: **«If the TCS value is not
specified, receivers shall assume the value SDR, unless the sampling keyword indicates the signal is a
KEY signal, in which case the TCS value is not meaningful.»** Lo mismo pasa en la sala (oficio): un clip HLG que
el sistema de edición interpreta como SDR BT.709 se ve lavado y sin contraste, y un clip SDR
interpretado como HDR se ve oscuro. Lo primero, al importar HDR, es comprobar cómo ha leído el
programa el espacio de color y la curva de cada clip.

### Los niveles del HDR

El Informe UIT-R BT.2408-9 (marzo de 2026) fija el blanco de referencia: **«HDR Reference White, is
defined in this Report as the nominal signal level obtained from an HDR camera and a 100% reflectance
white card resulting in a nominal luminance of 203 cd/m2 on a PQ display or on an HLG display that
has a nominal peak luminance capability of 1 000 cd/m2.»** El grafismo va a ese mismo nivel:
**«Graphics White is defined within the scope of this Report as the equivalent in the graphics domain
of a 100% reflectance white card […]. It therefore has the same signal level as HDR Reference White,
and graphics should be inserted based on this level.»**

| Referencia (BT.2408-9, tabla 1) | cd/m² | % PQ | % HLG |
|---|---|---|---|
| Carta gris del 18 % | 26 | 38 | 38 |
| Blanco de referencia HDR (100 %), que es también el blanco difuso y el del grafismo | 203 | 58 | 75 |

Es decir: en HDR, el blanco de un rótulo no va al 100 % de la señal, sino al 75 % en HLG o al 58 % en
PQ (oficio, sobre la tabla).

El monitor también cambia. La BT.2100-3 fija para el visionado crítico de HDR (tabla 3) un pico de
luminancia de «**≥ 1 000 cd/m2**» y un negro de «**≤ 0.005 cd/m2**», con la precisión de que el pico
se exige «**for small area highlights**», no para toda la pantalla en blanco. Una pantalla de rango
dinámico estándar trabaja alrededor de 100 nits (oficio). De ahí una regla de sentido común
profesional: para etalonar en HDR un máster con salida en HDR se necesita un monitor HDR; no se puede
juzgar lo que no se ve.

La gama de color y el rango dinámico son dos ejes distintos. Se puede tener gama amplia con rango
estándar, y al revés. La BT.2020 amplía qué colores; la BT.2100, además, cuánto brillo (oficio).

### Mezclar SDR y HDR: las conversiones

Una pieza HDR casi siempre lleva material SDR (archivo, teléfono, agencias). El Informe BT.2408-9
distingue dos formas de meterlo: **«SDR content may either be direct-mapped or inverse tone mapped
(up-mapped) into an HDR format for inclusion in HDR programmes.»**

| Método | Qué hace (BT.2408-9) |
|---|---|
| Mapeo directo | **«Direct-mapping places SDR content into an HDR container, analogously to how content specified using BT.709 colorimetry may be placed in a BT.2020 container. This approach is intended to preserve the appearance of the SDR content when shown on an HDR display.»** |
| Expansión (*up-mapping*) | **«inverse tone mapping (up-mapping) is intended to expand the content to use more of the available HDR luminance range»**; **«Up-mapping is intended to make content captured in SDR look more as if it had been captured in HDR even though the highlights are more limited.»** |

Y cada una puede hacerse de dos maneras:

- Por luz de pantalla (*display-light*): **«Display-referred mapping is used when the goal is to
  preserve the colours and relative tones seen on an SDR display, when the content is shown on an
  HDR display; an example of which is the inclusion of SDR graded content within an HDR
  programme.»**
- Por luz de escena (*scene-light*): **«Scene-referred mapping is used when the goal is to match the
  colours and relative tones of a native HDR and native SDR camera; an example of which is the
  inter-mixing of SDR and HDR cameras within a live television production.»**

Para el montaje, el caso de la primera viñeta es el habitual: un plano SDR ya etalonado que entra en
una pieza HDR se convierte por luz de pantalla, llevando el 100 % del SDR a un nivel próximo al
blanco de referencia (el Informe: **«The linear SDR display light may then be scaled to ensure that
100% SDR maps to a similar level to HDR reference white of 203 cd/m2.»**).

En sentido contrario, para sacar una versión SDR de una pieza HDR: **«Display-light down-mapping
attempts to maintain the ‘look’ of the HDR source when converted to SDR, and is usually preferred.»**
La conversión por luz de escena, en cambio, ya no se usa mucho para bajar a SDR porque cambia el
aspecto de los rótulos incrustados: **«change the appearance in both colour and tone of embedded
graphics»**. Y las idas y vueltas cuestan: **«In any large production, SDR to HDR to SDR
‘round-trip’ losses are a major concern.»** La regla de oficio que se deduce: convertir una vez, al
entrar, y no encadenar conversiones SDR-HDR-SDR sobre el mismo plano.

La propia fuente advierte que no hay un método único: **«Currently, there is no universal approach.»**

### El grafismo en HDR

Por qué el rótulo va al blanco del grafismo y no al 100 % lo explica el Informe UIT-R BT.2408-9 en su
apartado de grafismo: **«SDR graphics should be directly mapped into the HDR signal
at the ‘Graphics White’ signal level specified in Table 1 (75% HLG or 58%PQ) to avoid them appearing
too bright, and thus making the underlying video appear dull in comparison.»** (§ 9). Un rótulo al
100 % en HDR deslumbra y hace que el vídeo de debajo parezca apagado. El mismo apartado distingue dos
casos: si se quiere conservar el color corporativo del gráfico, **«a display-light mapping should be
used»**; si se quiere igualar con un rótulo que aparece en la escena (el marcador de un estadio), **«a
scene-light mapping is usually preferred»**.

Lo que el grafista hace con eso (oficio, sobre las citas):

| Caso | Qué se hace |
|---|---|
| Rótulo blanco en un programa HDR | El blanco del grafismo, no el 100 %: 75 % de la señal en HLG, 58 % en PQ (203 cd/m²) |
| Grafismo diseñado en SDR para un programa HDR | Mapeo directo por luz de pantalla, llevando su blanco al nivel del blanco del grafismo; así conserva el color corporativo |
| Grafismo que imita un cartel de la escena (marcador del estadio) | Mapeo por luz de escena, para que case con lo que la cámara ve |
| Grafismo que sale en HDR y en SDR a la vez | Se decide cuál es el máster y se comprueba en los dos monitores; la versión SDR se saca por luz de pantalla |
| Imagen fija HDR (PNG, TIFF) | Con la señalización CICP de primarios, curva y rango (epígrafe 5), para que el sistema la lea bien |
| Degradados y fondos suaves | A 10 bits como mínimo, que es lo que admite el HDR (epígrafe 2) |

Si CSRTV produce o emite en HDR no consta en documento publicado (epígrafe 1): lo que consta para la
antena es la alta definición, y un grafismo para una emisión HD en rango dinámico estándar se entrega
en la colorimetría y la curva de la BT.709 (oficio, sobre la BT.709).

## 7. Entrega para emisión

### Qué es un estándar de entrega

Un estándar de entrega es la ficha técnica que impone quien recibe el programa: formato de imagen
(resolución, cadencia, barrido, SDR o HDR), códec y tasa, contenedor, pistas de audio y su orden,
sonoridad, código de tiempo de inicio, metadatos y, a veces, qué va al principio del fichero (oficio).
No consta publicada una ficha técnica de entrega de la RTVA o de CSRTV; lo que sigue son las normas y
especificaciones de referencia del sector.

### El MXF como base

La especificación del formato de fichero MXF es la **«ST 377-1, Material Exchange Format (MXF) — File
Format Specification»**, que el catálogo de la SMPTE da como **«active»**, con última publicación de
2019-11-28 (la ficha de la Library of Congress citada en el epígrafe 2 nombra la edición de 2011; la
vigente es la de 2019). Sobre ella se construyen las especificaciones de entrega.

### AMWA AS-11

**«The AMWA AS-11 family of Specifications define constrained media file formats (based on MXF) for
the delivery of finished media assets to a broadcaster or publisher. Each Specification is developed
for a particular business purpose.»** Son, por tanto, MXF con restricciones: qué códec, qué pistas y
qué metadatos se admiten para cada destinatario (oficio, sobre la cita).

Su origen: **«The AS-11 UK DPP HD & SD Specifications are well established for the delivery of
finished programs to media companies within the UK.»** Y su ampliación, con especificaciones nuevas
para: **«Meet the requirements of broadcasters in the Nordic countries, Australia and New Zealand, as
well as broadcasters represented by the North American Broadcasters Association (NABA) and the
DPP»**; **«Add support for UHD and HDR content»**; y **«Cater for delivery of short-form content in
addition to full-length programs (such as commercials, promotions, and music videos)»**.


### El control de calidad de cada entregable

Un entregable no se da por bueno porque se haya exportado. La EBU, en su hoja informativa *Quality
Control* (publicada el 01-09-2015), empieza por el error de base: **«There is a common misconception
that DIGITAL means QUALITY! If that were true, there would be no need for Quality Control.»** Y
explica por qué hoy hay más de una revisión: **«Now, traditional television is just one of many
destinations for content and each has its own QC requirements and its own file format checks that
have to be passed before delivery!»**

La respuesta de la EBU es una plantilla de comprobaciones por destino: **«Different QC Templates may
be used for different outputs – the key is to build a viable test set for each of the programme’s
destinations.»**; y **«A finished programme workflow may require several different QC Templates, each
based on the particular requirements of the deliverable.»** Los ejemplos que da:

| Tipo de control (EBU) | Qué comprueba |
|---|---|
| **«Automated QC»** | **«To check signal levels and standards»** |
| **«File Package Compliance»** | **«To check against file standards, e.g. AS11 DPP»** |
| **«Manual QC»** | **«Golden Eyes/Ears watching the programme»** |
| **«File Structure Analysis»** | **«Deep analysis to find if something is wrong with the file structure»** |

Cada plantilla se construye con ítems del catálogo de control de calidad de la EBU (qc.ebu.io),
publicado bajo licencia CC-BY 4.0. Algunos que tocan a una pieza gráfica (identificador,
nombre y definición del catálogo):

| Ítem | Nombre | Qué comprueba |
|---|---|---|
| 0051B | Video Signal Levels | **«System shall report luma and chroma values lying outside the acceptable range, but also RGB gamut, and optionally PAL/NTSC gamut.»** (los límites de la R 103, epígrafe 2) |
| 0010B | Loudness | **«System shall check for programme loudness, loudness range, maximum momentary loudness, maximum short term loudness and true peak.»** (la R 128, más abajo) |
| 0021B | Flashing Video | **«System shall check for segments of video which may be harmful to sufferers of photosensitive epilepsy.»** |
| 0044B | Video Freeze | **«…the System shall verify if 'frozen' (i.e. non-moving) pictures appear in the video for multiple adjacent identical (or near-identical) frames.»** |
| 0078B | Audio Silence | **«…the system shall verify if the audio level on any audio channel is lower than the user defined Silence Threshold Level for intervals longer than a user specified Minimum Silence Duration.»** |
| 0026F | Timecode | Comprobar **«1 - TC start value(s); 2 - TC discontinuities; 3 - Invalid TC (e.g. seconds=80).»** |
| 0082W | Audio / Video Duration Match | **«System shall verify that the audio duration signalled in the wrapper metdata and the video duration signalled in the wrapper metadata are the same.»** (así, «metdata», en el catálogo) |
| 0119B | Slate Details | **«System shall identify the programme information written on the slate or countdown clock before the start of the programme.»** |
| 0248B | Missing Captions/Subtitles | **«…the system shall detect periods where speech is occurring in the audio but no captions/subtitles are displayed.»** |
| 0001F | Active Format Description | La relación de aspecto señalada en el fichero (epígrafe 1) |

Las máquinas no lo ven todo: la EBU mantiene el control manual, y **«The number of times a programme
is actually watched will depend on the level of processing and the accuracy of the automated QC
checks applied at each stage.»** El cierre, según la hoja de 2015, suele ser una firma:
**«A traditional QC report is a
written document with a mixture of comments, critical assessment and technical measurements. The
“sign-off” for transmission is usually just a signature!»** Cada entregable tiene la suya,
también la pieza gráfica (oficio).

### La sonoridad de entrega: EBU R 128

El audio se entrega normalizado por sonoridad, no por picos. La EBU R 128 (noviembre de 2023)
recomienda **«that the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS.
Where attaining the Target Level is not achievable practically (for example, live programmes), a
tolerance of ±1.0 LU is permitted»**; **«that the audio signal shall generally be measured in its
entirety, without emphasis on specific foreground elements such as speech, music or sound effects»**;
y **«that the True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during
production (linear audio)»**, con la salvedad de que **«Permitted Maximum True Peak Levels may be
lower for different distribution systems and data reduction rates.»**


### Cómo entrega el grafista

Una pieza gráfica llega a emisión de una de cuatro formas (oficio; qué pide CSRTV en cada caso no
consta en documento publicado):

| Forma de entrega | Qué es | Cuándo | Qué hay que fijar |
|---|---|---|---|
| Pieza cerrada | Un fichero de vídeo con imagen y sonido: una cabecera, una promoción, una cortinilla | Cuando la pieza va entera, sin nada detrás | El estándar de entrega del destino: resolución, cadencia, barrido, códec, contenedor, pistas y sonoridad |
| Pieza con transparencia | Un fichero de vídeo con alfa (ProRes 4444) o una secuencia numerada de imágenes con alfa (TGA, PNG, EXR) | Cuando va encima de otra imagen: una mosca animada, una transición, un rótulo animado | Códec con alfa, alfa directo o premultiplicado, cadencia y duración exactas |
| Imagen fija | Un PNG o un TIF con alfa | Rótulos fijos, logotipos, fondos para el mezclador o el servidor | Resolución del lienzo, rango y espacio de color |
| Plantilla | Una escena del sistema de grafismo de directo con campos que se rellenan | Rótulos de nombre, marcadores, datos que cambian | Campos, datos que alimentan cada campo y pruebas con el texto más largo (las plantillas son el tema 9) |

En la cuarta, el grafismo sale del motor como par relleno-llave (epígrafe 3) y no hay fichero que
entregar a emisión: lo que se entrega es la plantilla, al sistema de grafismo.

### La comprobación antes de entregar

La lista de comprobación de una pieza gráfica (oficio, sobre lo dicho en el tema):

| Qué | Cómo se comprueba | Epígrafe |
|---|---|---|
| Resolución y relación de aspecto del destino | Propiedades del fichero; la pieza no se ha estirado | 1 |
| Cadencia y barrido | Que coinciden con los del destino; filetes y textos finos sin parpadeo en entrelazado | 1 |
| Códec, muestreo y bits | Códec con alfa si la pieza va encima; 10 bits si hay degradados | 2 y 3 |
| Niveles | Forma de onda: dentro del rango preferente de la R 103; nada de blancos ni rojos ilegales | 2 |
| Alfa | Que existe, que su tipo (directo o premultiplicado) va dicho, sin halos ni fondo negro | 3 |
| Zonas seguras | Todo texto dentro de la zona de grafismo, con el texto más largo posible | 4 |
| Color | Espacio y curva del destino; el color corporativo, en el vectorscopio | 5 |
| HDR | Blanco del grafismo al 75 % HLG o 58 % PQ; versión SDR comprobada | 6 |
| Destellos | Ninguna secuencia de destellos que pueda dañar a personas con epilepsia fotosensible (ítem 0021B) | 7 |
| Sonido, si lo hay | Sonoridad de la R 128 | 7 |
| Nombre, duración y documentación | Nombre del fichero según la convención de la casa, duración exacta, ficha con los datos técnicos | 7 |

La regla que ordena la lista (oficio): la pieza se juzga en la señal que va a salir, en el monitor de
vídeo y con los instrumentos, no en la pantalla del puesto de diseño; y se entrega en el formato que
pide el destino, no en el que salga por defecto del programa.

### Versiones para plataformas

Una misma pieza sale a menudo en varias versiones: el máster de emisión y las de web y redes, con
otros formatos de imagen, otras tasas y a veces otra sonoridad (oficio). Para la distribución, la
pieza se comprime en GOP largo, en H.264 o H.265 (epígrafe 2); la versión para redes suele pedir otra
relación de aspecto, que se compone de nuevo y no se estira (epígrafe 1). Los formatos verticales y las
miniaturas son el tema 13.

## Aplicación práctica

### Un rótulo animado para un informativo en HD

El encargo: una entradilla de rótulo animado que entrará sobre la imagen del informativo, emitido en
alta definición.

1. Formato del proyecto: 1.920 × 1.080, píxel cuadrado, con la cadencia del informativo (25 cuadros;
   si la casa trabaja en 1080i50, se comprueba el parpadeo de los filetes).
2. Zonas seguras: guías en 96 píxeles a cada lado y 54 arriba y abajo; el texto, dentro.
3. Color: el corporativo en valores RGB de pantalla, comprobado en el vectorscopio; niveles dentro del
   rango preferente en la forma de onda.
4. Salida: con alfa. Un fichero ProRes 4444 en MOV, o una secuencia TGA de 32 bits, según pida el
   destino, con el tipo de alfa declarado. En ProRes 422 o en JPG, no: llegaría con fondo negro.
5. Si el rótulo se lanza desde el sistema de grafismo de directo, no se entrega fichero: se entrega
   la plantilla, y el motor saca relleno y llave.

### Cuentas que se piden

| Pregunta | Cuenta | Resultado |
|---|---|---|
| Zona segura de grafismo en 1080 (EBU R 95) | 1.920 − 2 × 96; 1.080 − 2 × 54 | 1.728 × 972 |
| Zona segura de acción en 1080 (SMPTE ST 2046-1) | 93 % de 1.920 y de 1.080, redondeado | 1.786 × 1.004 |
| Zona segura de grafismo en 2160 (EBU R 95) | 3.840 − 2 × 192; 2.160 − 2 × 108 | 3.456 × 1.944 |
| Un fotograma HD RGBA de 8 bits sin comprimir | 1.920 × 1.080 × 4 | 8.294.400 bytes (unos 8,3 MB) |
| Un minuto de ese fotograma a 25 fps | 8.294.400 × 25 × 60 | unos 12,4 GB |
| Un minuto de ProRes 4444 a unos 330 Mb/s (cifra de Apple a 29,97 fps) | 330 × 60 ÷ 8 | unos 2.475 MB |
| Niveles de una muestra de 10 bits | 2^10 | 1.024 |
| Blanco de un rótulo en HLG y en PQ | BT.2408-9, tabla 1 | 75 % y 58 % (203 cd/m²) |

### Un grafismo SDR en un programa HDR

Si un programa se hiciera en HLG, el paquete gráfico diseñado en SDR se llevaría a HDR por mapeo
directo con luz de pantalla, con el blanco del grafismo al 75 % de la señal; el marcador que imita el
del estadio, por luz de escena; y la versión SDR del programa se sacaría por luz de pantalla,
comprobando que los rótulos conservan el color (BT.2408-9, §§ 5.1, 5.2 y 9; aplicación de oficio).

## Normas y documentos técnicos que el tema cita

- Contrato-programa 2024-2026 entre el Consejo de Gobierno y la RTVA (BOJA núm. 245, de 26/12/2023),
  puntos 85 y 101: la emisión en HD por TDT.
- UIT-R BT.601-7 (definición estándar), BT.709-6 (alta definición), BT.2020-2 (ultra alta
  definición), BT.2100-3 (alto rango dinámico) e Informe BT.2408-9 (marzo de 2026, práctica del HDR).
- SMPTE ST 2046-1:2009 (zonas seguras); ST 2110-20:2022 (vídeo sin comprimir sobre IP); ST 377-1
  (MXF), ST 378 (OP1a) y ST 390 (OP-Atom); ST 2084 (PQ), ST 2086 y ST 2094-40 (metadatos de HDR).
- EBU R 95 v1.1 (junio de 2017, zonas seguras), R 103 v3.0 (límites de la señal), R 128 (sonoridad) y
  hoja *Quality Control* (2015) con el catálogo de control de calidad.
- AMWA AS-11 (especificaciones de entrega).
- W3C: especificación PNG, tercera edición (24-06-2025), y WCAG 2.2 (12-12-2024), en lo que dicen del
  sRGB, que definen por remisión a la IEC 61966-2-1.
- Documentación de fabricante: Apple (ProRes), Avid (DNxHD), Sony, Panasonic (AVC-Intra), Blackmagic
  Design (DaVinci Resolve 21 y mezcladores ATEM), Blender Foundation (Blender 5.2) y Vizrt (Viz Engine).

## Lo que este tema no da, y dónde está

- Qué formato HD concreto, qué códec y qué ficha de entrega usa CSRTV para el grafismo: no consta en
  documento publicado localizado. Tampoco si produce en UHD o en HDR.
- La SMPTE RP 2046-2 (protección de otras relaciones de aspecto) y la Recomendación UIT-R BT.1379
  (zonas seguras de la transición a 16:9): no se han leído.
- La norma IEC 61966-2-1 (sRGB) no se ha leído directamente (sólo su ficha de catálogo): lo que el
  tema dice del sRGB viene de la especificación PNG, las WCAG 2.2 y el manual de Blender, que la citan. Qué perfil de color usa por
  defecto cada programa de diseño no se da.
- Si el DNxHD o el DNxHR llevan alfa: no consta en la documentación de Avid leída.
- La especificación DCI del 4K de cine: no se ha leído; su resolución va como oficio.
- Las plantillas y la automatización: tema 9. La composición, el *tracking* y la rotoscopia: tema 5.
  Los escenarios virtuales y los videowalls: tema 6. El manual de marca y el color corporativo: tema 2.
  La accesibilidad (contraste, subtítulos): tema 10. Los formatos para redes: tema 13.

## Trazabilidad

Todas las fuentes, en la edición vigente el 24-09-2026. Las de los epígrafes 1 a 7 que vienen de
temas cerrados de Canal Sur (Operador/a Montador/a de Vídeo, tema 4; Realizador/a, temas 12 y 14)
conservan la fecha con que allí se leyeron, que se da en cada fila; las demás se leyeron el
29-09-2026.

| Fuente | Qué sostiene | Lectura |
|---|---|---|
| Contrato-programa 2024-2026 (BOJA núm. 245, de 26/12/2023), puntos 85 y 101, y parte expositiva | Emisión en HD por TDT desde el 14-02-2024 | Tomado del tema 14 de Realizador/a (leído allí el 29-09-2026) |
| UIT-R BT.601-7 | 720 muestras por línea; coeficientes de luminancia de la SD | 29-09-2026 |
| UIT-R BT.709-6 (06/2015) | 1.920 × 1.080, cadencias, entrelazado, 8 o 10 bits, niveles, primarios y blanco D65, luminancia, gamma 0,45 | 29-09-2026 |
| UIT-R BT.2020-2 | UHD, 10 o 12 bits, primarios, coeficientes de luminancia, luminancia constante y no constante | 29-09-2026 |
| UIT-R BT.2100-3 | Formatos del HDR, píxel cuadrado, muestreo, rango estrecho y completo, primarios (tabla 2), NCL por defecto e intensidad constante, PQ y HLG, monitor de referencia | 29-09-2026 |
| Informe UIT-R BT.2408-9 (03/2026), §§ 2.1, 5.1, 5.2, 7.1 y 9, tabla 1 | Blanco de referencia y del grafismo; conversiones SDR-HDR; imagen fija y CICP | 29-09-2026 |
| SMPTE ST 2046-1:2009 (pub.smpte.org; **«active»**) | Zonas seguras de acción y de título; RP 218; CEA-708 | 29-09-2026 |
| EBU R 95 v1.1 (junio de 2017), nota 5 y figuras 3 a 5 | Zonas seguras de la EBU y sus valores en 1080 y 2160 | Tomado del tema 12 de Realizador/a (leída allí el 29-09-2026) |
| EBU R 103 v3.0 | Rangos nominal, preferente y total | Tomado del tema 14 de Realizador/a (leída el 24-09-2026 por el tema de origen) |
| EBU *Quality Control* (2015) y catálogo qc.ebu.io (CC-BY 4.0) | Plantillas de control por destino; ítems 0001F, 0010B, 0021B, 0026F, 0044B, 0051B, 0078B, 0082W, 0119B, 0248B | Tomado del tema 14 de Realizador/a (leídos allí el 29-09-2026) |
| EBU R 128 (noviembre de 2023) | Sonoridad de entrega | Tomado del tema 14 de Realizador/a (leída el 24 o el 25-09-2026 por el tema 4 de Montador/a) |
| AMWA AS-11; SMPTE ST 377-1 | Especificaciones de entrega sobre MXF | Tomado del tema 14 de Realizador/a (leídas el 24 o el 25-09-2026 por el tema 4 de Montador/a) |
| SMPTE ST 2110-20:2022, §§ 7.4.1, 7.5 y 7.6 | Colorimetría «ALPHA», TCS y señal de llave | Tomado de los temas 4 de Montador/a y 14 de Realizador/a (leída el 24 o el 25-09-2026); §§ 7.4.1 y 7.6 releídos el 29-09-2026 |
| SMPTE ST 2084, ST 2086, ST 2094-40 (fichas de catálogo) | PQ y metadatos de HDR | Tomado del tema 14 de Realizador/a (fichas leídas el 24 o el 25-09-2026; la ST 2094-40, el 29-09-2026) |
| Library of Congress, fdd000013 (MXF) y fdd000389 (ProRes 422) | MXF, patrones operacionales, familia ProRes | Tomado de los temas 4 de Montador/a y 14 de Realizador/a (leídas el 24 y el 25-09-2026) |
| Apple, *Apple ProRes* (abril de 2022) | ProRes 4444 y 4444 XQ, alfa hasta 16 bits, únicos ProRes con alfa, 4:4:4:4 en Y'CbCrA o RGBA; tasas de toda la familia | 29-09-2026 |
| Avid, *Avid DNxHD Technology* (2012) | DNxHD, VC-3, variantes; ausencia de «alpha» | Tomado de los temas 4 de Montador/a y 14 de Realizador/a (leído el 24-09-2026); búsqueda de «alpha», 29-09-2026 |
| Sony (guías ILCE-1, ILCE-7SM3 y manual de la PXW-Z200); Panasonic, *AVC-Intra FAQ* | Intracuadro y GOP largo, H.264 y H.265, AVC-Intra | Tomado de los temas 4 de Montador/a y 14 de Realizador/a (leídas el 24-09-2026) |
| Blackmagic Design, manual de DaVinci Resolve 21 (julio de 2026), cap. 77, pp. 1726-1728; perfiles de HDR | Alfa directo y premultiplicado; Dolby Vision, HDR10, HDR10+, HDR Vivid, HLG | 29-09-2026 (cap. 77 y lista de los cinco perfiles); lo demás de los perfiles, tomado del tema 14 de Realizador/a |
| Blackmagic Design, manual de los mezcladores ATEM | Composición posterior (DSK) y panel multimedia con alfa | Tomado del tema 12 de Realizador/a (releído allí el 29-09-2026) |
| Blender Foundation, *Blender 5.2 LTS Manual*, glosario | Quién usa cada tipo de alfa; conversión con pérdida; definición del sRGB | 29-09-2026 |
| W3C, *Portable Network Graphics (PNG) Specification (Third Edition)*, Recommendation de 24-06-2025, § 11.3.2.5 y tabla 17 | Primarios, blanco y gamma del sRGB; referencia a la IEC 61966-2-1 | 29-09-2026 |
| W3C, WCAG 2.2, Recommendation de 12-12-2024, definición de «relative luminance» y su nota 3 | Luminancia y curva de transferencia del sRGB; el sRGB, supuesto en la web | 29-09-2026 |
| IEC, ficha de catálogo de la IEC 61966-2-1:1999 (webstore.iec.ch, publicación 6169, la que enlazan la PNG y las WCAG) | Número y año de la norma sRGB | 29-09-2026 |
| UIT-R BT.2100-3, tabla 7 y nota 7a | Señal ICtCp | 29-09-2026 |
| Vizrt, *Viz Engine Administrator Guide* 5.4 («Video Output») y 5.2 («Dual Channel Mode») | Relleno y llave, propiedades de la llave, super blanco, retardo | 29-09-2026 |

Lo que va como oficio se dice en el texto: el uso de cada formato de fichero, las reglas de trabajo
del grafista con cada norma, la lista de comprobación y los casos de la aplicación práctica. Las
cuentas son cálculo sobre las cifras citadas.
