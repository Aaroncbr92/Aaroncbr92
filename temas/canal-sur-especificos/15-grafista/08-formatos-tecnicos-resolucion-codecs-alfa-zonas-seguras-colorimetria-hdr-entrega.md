# Tema 8 del específico de Grafista · Formatos técnicos: resolución, códecs, alfa, safe areas, colorimetría, HDR/SDR y entrega para emisión

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Grafista · punto 8 |
| Sirve para | Grafista de Canal Sur (grupo B03): test de teoría específica y de aplicación práctica, y prueba práctica del puesto |
| Fuente | Sin norma jurídica que regule los formatos. Lo propio de la casa: Contrato-programa 2024-2026 entre el Consejo de Gobierno y la RTVA (BOJA núm. 245, de 26/12/2023), puntos 85 y 101. Recomendaciones e informes de la UIT-R: BT.601-7, BT.709-6, BT.2020-2, BT.2100-3 e Informe BT.2408-9. SMPTE: ST 2046-1:2009 (zonas seguras), ST 2110-20:2022 y fichas de catálogo (ST 377-1, ST 2084, ST 2086, ST 2094-40). EBU: R 95 v1.1, R 103 v3.0 y hoja informativa *Quality Control* (2015) con su catálogo de ítems. AMWA (AS-11); Library of Congress (MXF y ProRes 422). Documentación de fabricante: Apple (*Apple ProRes*, abril de 2022), Avid, Sony, Blackmagic Design (manual de DaVinci Resolve 21 y manual de los mezcladores ATEM), Blender Foundation (manual de Blender 5.2) y Vizrt (*Viz Engine Administrator Guide* 5.2 y 5.4). Lo demás, oficio y cálculo |
| Redacción que se estudia | Las ediciones vigentes el 24-09-2026 de cada documento citado; fechas de lectura en «Trazabilidad» |
| Extensión | 10.000 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); televisión digital terrestre (TDT). Sector de Radiocomunicaciones de la Unión
Internacional de Telecomunicaciones (UIT-R), que escribe la ultra alta definición como UHDTV; Unión
Europea de Radiodifusión (EBU, *European Broadcasting Union*); Sociedad de Ingenieros de Cine y
Televisión (SMPTE, *Society of Motion Picture and Television Engineers*), cuyas normas llevan el
prefijo ST (*standard*) o RP (*recommended practice*, práctica recomendada); Advanced Media Workflow
Association (AMWA); Digital Production Partnership (DPP) y North American Broadcasters Association
(NABA), que se nombran como los cita la fuente; Biblioteca del Congreso de Estados Unidos (LOC,
*Library of Congress*); Comisión Internacional de la Iluminación (CIE); la norma estadounidense de
subtítulos CEA-708, que se nombra como la cita la SMPTE.

Los términos técnicos, presentados de entrada: definición estándar (SD), alta definición (HD) y ultra
alta definición (UHD); iniciativa de cine digital (DCI, *Digital Cinema Initiatives*); rango dinámico
estándar (SDR) y alto (HDR); cuantificación perceptual (PQ, *perceptual quantization*) e híbrida
logarítmica-gamma (HLG, *hybrid log-gamma*); candela por metro cuadrado (cd/m²), que la industria
llama *nit*; cuadros o fotogramas por segundo (fps); progresivo (p), progresivo por cuadro segmentado
(PsF, *progressive segmented frame*) y entrelazado (i); rojo, verde y azul (RGB), el mismo con canal
alfa (RGBA), luminancia con diferencias de color (YCbCr) y el modelo de tinta cian, magenta, amarillo y
negro (CMYK); tabla de consulta (LUT, *look-up table*); luminancia constante (CL) y no constante (NCL);
grupo de imágenes (GOP, *group of pictures*); codificación avanzada de vídeo (AVC, la norma H.264) y de
alta eficiencia (HEVC, la norma H.265); formato de intercambio de material (MXF, *material exchange
format*), con sus patrones operacionales OP1a y OP-Atom; contenedores de Apple (MOV, QuickTime), de la
familia de normas del Grupo de Expertos en Imágenes en Movimiento (MP4) y de Microsoft (AVI); relación
señal/ruido de pico (PSNR, *peak signal-to-noise ratio*); megabits y gigabits por segundo (Mb/s,
Gb/s), megabyte y gigabyte (MB, GB); descripción del formato activo (AFD, *Active Format
Description*); control de calidad (QC, *quality control*), cuyo catálogo de la EBU se publica con
licencia Creative Commons de atribución (CC-BY 4.0); composición posterior del mezclador (DSK, del
inglés *downstream keyer*); protocolo de internet (IP); interfaz digital serie (SDI); señal de ajuste de
los negros del monitor (PLUGE, *picture line-up generation equipment*); los sistemas analógicos de
color PAL y NTSC, que sólo se nombran; el relleno (*fill*) y la llave (*key*) con que un sistema de
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
estrecho (16 a 235). Un motor de grafismo de directo hace esa conversión en su salida; en Viz Engine,
por ejemplo, la llave tiene una opción para ello: **«Downscale Luma: Compresses the luminance range of
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
Las dos únicas tasas de este documento que el tema da son las de esas dos variantes: para la 4444,
**«approximately 330 Mbps for 4:4:4 sources at 1920 x 1080 and 29.97 fps»**; para la 4444 XQ,
**«approximately 500 Mbps for 4:4:4 sources at 1920 x 1080 and 29.97 fps»**. Las del resto de la
familia no se dan.

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
**«ALPHA»**, y exime a las señales de llave de declarar la curva de transferencia: **«If the TCS value
is not specified, receivers shall assume the value SDR, unless the sampling keyword indicates the signal
is a KEY signal, in which case the TCS value is not meaningful.»** (TCS es el sistema de transferencia:
SDR, PQ o HLG, epígrafe 6).

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

