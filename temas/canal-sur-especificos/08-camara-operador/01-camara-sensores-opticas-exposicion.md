# Tema 1 del específico de Cámara Operador · La cámara de televisión y vídeo

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Cámara Operador · punto 1 |
| **Sirve para** | Puesto 2.8, Cámara Operador (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Sin norma jurídica. Recomendaciones técnicas de la Unión Europea de Radiodifusión: EBU R 103 v3.0 (mayo de 2020), EBU R 118 v2 (abril de 2017) y EBU Tech 3335 (agosto de 2014). Documentación de fabricante: Sony, *PXW-Z200/HXR-NX800 Help Guide* (5-060-574-13(1), 2024) y *PXW-FS5/FS5K Operating Guide* (4-581-849-11(1)); Blackmagic Design, *URSA Broadcast G2 Installation and Operation Manual* (noviembre de 2021); Canon, *XF605 Instruction Manual* (PUB. DIE-0559-000B); nota de producto Fujinon UA22x4.8BERD (18 de marzo de 2026). Lo demás, oficio |
| **Redacción que se estudia** | Las ediciones de las recomendaciones EBU vigentes el 24/09/2026 (R 103 en su versión 3.0; R 118 en su versión 2) |
| **Extensión** | 9.700 palabras aproximadamente |

<!-- /portada -->

Siglas que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Europea de Radiodifusión (**EBU**,
*European Broadcasting Union*, que firma así sus recomendaciones); Sector de Radiocomunicaciones de
la Unión Internacional de Telecomunicaciones (**UIT-R**); captación electrónica de noticias
(**ENG**, *electronic news gathering*) y producción electrónica en campo (**EFP**, *electronic field
production*); unidad de control de cámara (**CCU**, *camera control unit*); dispositivo de
acoplamiento de carga (**CCD**) y semiconductor complementario de óxido metálico (**CMOS**);
conversor analógico-digital (**ADC**, *analog-to-digital converter*); tabla de consulta (**LUT**,
*look-up table*); interfaz digital serie (**SDI**); televisión de definición estándar (**SDTV**),
alta definición (**HD**, **HDTV**) y ultra alta definición (**UHD**, **UHDTV**); rango dinámico
estándar (**SDR**) y alto rango dinámico (**HDR**), con su curva híbrida logarítmica-gamma (**HLG**,
*hybrid log-gamma*); control automático de ganancia (**AGC**, *automatic gain control*); escala de
sensibilidad de la Organización Internacional de Normalización (**ISO**); densidad neutra
(**ND**, *neutral density*); enfoque automático (**AF**, *autofocus*); balance de blancos automático
continuo (**ATW**, *auto tracing white*); decibelio (**dB**); kelvin (**K**), unidad de la
temperatura de color; lux (**lx**); cuadros por segundo (**fps**); los tres primarios rojo, verde y
azul (**RGB**) y la luminancia (**Y**).

Los rótulos de menú y de panel se escriben tal como los imprime el fabricante (***Peaking***,
***Zebra***, ***Auto ND Filter***, ***ATW***, ***KNEE***…): son rótulos de la máquina, no siglas,
y cambian de una marca a otra.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.8, punto 1):
>
> Cámara de televisión y vídeo: sensores, ópticas, enfoque, exposición, balance de blancos,
> ganancia y filtros.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué pieza convierte la carga del sensor en números; en qué se diferencian
un CCD y un CMOS y qué defecto da cada uno; qué es una máscara de Bayer y qué la distingue de un
bloque de tres sensores con prisma; cómo se relacionan focal, ángulo, diafragma, distancia y
profundidad de campo; qué es la velocidad de un objetivo y cómo se lee su referencia; cómo se ajusta
el tiraje; para qué sirven el realce de contornos, la lupa y la cebra; qué hace el *knee*; qué
niveles de señal recomienda la EBU; qué es el balance de blancos y cuándo no conviene el automático
continuo; a cuántos pasos equivalen 6, 12 o 18 dB de ganancia y qué cuestan; qué filtro usar para
oscurecer un cielo o para abrir el diafragma con mucha luz. En la prueba práctica: preparar y
ajustar una cámara de reportaje antes de una toma (tiraje, balance, exposición, filtro, foco).

<!-- indice -->

## Índice

- [La cámara de televisión y vídeo](#la-cámara-de-televisión-y-vídeo)
  - [Las familias de cámara](#las-familias-de-cámara)
  - [Quién ajusta qué](#quién-ajusta-qué)
  - [La clasificación de la EBU por niveles de calidad](#la-clasificación-de-la-ebu-por-niveles-de-calidad)
  - [Del fotón al número](#del-fotón-al-número)
- [Sensores](#sensores)
  - [CCD y CMOS](#ccd-y-cmos)
  - [El obturador de persiana](#el-obturador-de-persiana)
  - [Un sensor con máscara de Bayer o tres sensores con prisma](#un-sensor-con-máscara-de-bayer-o-tres-sensores-con-prisma)
  - [El tamaño del sensor, el píxel y la sensibilidad](#el-tamaño-del-sensor-el-píxel-y-la-sensibilidad)
  - [Resolución, aliasing y píxeles blancos](#resolución-aliasing-y-píxeles-blancos)
- [Ópticas](#ópticas)
  - [La distancia focal y el ángulo de visión](#la-distancia-focal-y-el-ángulo-de-visión)
  - [Cómo se lee la referencia de un objetivo](#cómo-se-lee-la-referencia-de-un-objetivo)
  - [El diafragma y el número f](#el-diafragma-y-el-número-f)
  - [La difracción](#la-difracción)
  - [La profundidad de campo](#la-profundidad-de-campo)
  - [El círculo de confusión y la distancia hiperfocal](#el-círculo-de-confusión-y-la-distancia-hiperfocal)
  - [El tamaño del sensor y la profundidad de campo](#el-tamaño-del-sensor-y-la-profundidad-de-campo)
  - [Las aberraciones y el *bokeh*](#las-aberraciones-y-el-bokeh)
  - [La montura y la distancia de brida](#la-montura-y-la-distancia-de-brida)
  - [El estabilizador](#el-estabilizador)
- [Enfoque](#enfoque)
  - [El foco manual](#el-foco-manual)
  - [El ajuste de tiraje](#el-ajuste-de-tiraje)
  - [Las ayudas al enfoque: realce de contornos y lupa](#las-ayudas-al-enfoque-realce-de-contornos-y-lupa)
  - [El autofoco](#el-autofoco)
- [Exposición](#exposición)
  - [Los cuatro mandos de la exposición](#los-cuatro-mandos-de-la-exposición)
  - [La obturación: velocidad, ángulo y parpadeo](#la-obturación-velocidad-ángulo-y-parpadeo)
  - [Las ayudas a la exposición: cebra, monitor de forma de onda y falso color](#las-ayudas-a-la-exposición-cebra-monitor-de-forma-de-onda-y-falso-color)
  - [Los límites de la señal según la EBU](#los-límites-de-la-señal-según-la-ebu)
  - [El *knee* y las altas luces](#el-knee-y-las-altas-luces)
  - [El margen de exposición](#el-margen-de-exposición)
  - [Las curvas logarítmicas y el visor](#las-curvas-logarítmicas-y-el-visor)
  - [La sensibilidad de catálogo](#la-sensibilidad-de-catálogo)
- [Balance de blancos](#balance-de-blancos)
  - [Qué es y qué hace la cámara](#qué-es-y-qué-hace-la-cámara)
  - [Cómo se hace](#cómo-se-hace)
  - [El balance automático continuo](#el-balance-automático-continuo)
- [Ganancia](#ganancia)
  - [Decibelios y pasos](#decibelios-y-pasos)
  - [El precio: el ruido](#el-precio-el-ruido)
  - [La ganancia es el último recurso](#la-ganancia-es-el-último-recurso)
- [Filtros](#filtros)
  - [La densidad neutra](#la-densidad-neutra)
  - [El ND para abrir el diafragma](#el-nd-para-abrir-el-diafragma)
  - [Los filtros de conversión y la corrección electrónica](#los-filtros-de-conversión-y-la-corrección-electrónica)
  - [Los filtros delanteros](#los-filtros-delanteros)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## La cámara de televisión y vídeo

### Las familias de cámara

Las cámaras de televisión se agrupan en familias, y cada una tiene su forma de trabajar (oficio):

| Familia | Dónde | Cómo trabaja |
|---|---|---|
| ENG | Reportaje e informativos | Autónoma: batería, tarjeta, un operador. Al hombro |
| EFP y estudio | Retransmisiones, plató y producción en exteriores | En cadena: cuelga de una unidad de control por triax o fibra |
| Cinematografía digital | Ficción | Autónoma, con registro propio y flujo de etalonaje |

La distinción que ordena el resto del tema: una cámara ENG lo lleva todo dentro y decide sola; una
EFP o de estudio delega el control de imagen en el control de cámara.

### Quién ajusta qué

En una producción multicámara el ajuste de imagen no lo hace el operador: lo hace el control de
imagen, desde la unidad de control de cámara. El operador ejecuta lo que se le pide por la
intercomunicación, y para eso tiene que conocer el vocabulario (oficio).

| Puesto | De qué responde |
|---|---|
| Operador de cámara | El encuadre, el foco y el movimiento. Y ejecutar en la cámara lo que el control le pide |
| Control de imagen | Que todas las cámaras casen: nivel, color, sombras, altas luces, detalle |

En reportaje el operador es también el control de imagen, y hace los ajustes él mismo en el menú.
En multicámara los hace otro, y el operador sólo tiene que entender la orden. Los nombres de los
circuitos de ajuste varían de un fabricante a otro; lo que importa es qué hace cada uno.

### La clasificación de la EBU por niveles de calidad

La EBU propone clasificar las cámaras por niveles (*tiers*) según su especificación y su calidad
medida: «**a practical approach be taken to the grading, or Tiering of cameras according to their
technical specifications and their measured quality based on the results of tests that are
specified in EBU Tech 3335**» (EBU R 118 v2). La finalidad es asignar cada cámara a un género:
«**Knowing which quality Tier a camera corresponds to will enable its targeting to programme genres
and applications [...] and, in the case of News, to balance speed of delivery against quality.**»

La recomendación da por supuesta la producción en rango dinámico estándar: «**these guidelines
assume Standard Dynamic Range production. The broadcaster must be consulted if High Dynamic Range
(as described in ITU-R BT.2100) images are required**».

Los niveles de alta definición, literales (§ 1.2):

| Nivel | Qué cámaras |
|---|---|
| HD Tier 1 | «**Shoulder mounted or handheld single or 3 sensor professional cameras**» |
| HD Tier 2L | «**(Long-form) professional cameras**» |
| HD Tier 2J | «**(Journalism) professional cameras**» |
| HD Tier 3 | «**Small, high quality semi-professional for production use**» |
| HD Tier 4 | «**Small consumer HD cameras (broadcaster approval required before use)**» |
| Tier SP | «**Specialist or special effects cameras (broadcaster approval required before use)**» |

Para UHD hay además dos niveles por resolución: UHD1 Tier 1 (**3840 x 2160**) y UHD1 Tier 2
(**≥ 2715 x 1527**), y UHD2 Tier 1 (**7680 x 4320**) y UHD2 Tier 2 (**≥ 5430 x 3054**).

Tres datos de la recomendación que tocan al informativo:

- El nivel 2J existe porque en noticias se acepta «**a relaxation of some of the criteria to take
  account of the balance between speed to air and quality that News programmes may have to
  make**».
- El nivel 3 se limita: «**Broadcasters will usually limit the amount of Tier 3 material allowed in
  an HD programme to around 33%**».
- El códec de a bordo puede rebajar una cámara: «**Although a camera can meet the requirements of a
  Tier, it may be let down (or even be downgraded by the on-board codec.**» (el paréntesis está sin
  cerrar en el original).

Los criterios de clasificación son el códec y cinco áreas de imagen: «**Noise · Sensitivity ·
Exposure Range · Spatial Resolution · Spatial Alias artefacts**»; «**Apart from spatial aliasing,
each factor can be measured using the procedures of EBU Tech 3335.**» El códec «**does not apply to
system cameras unless on-board recording in used**» (así en el original). Ruido, sensibilidad y
margen de exposición se tratan más abajo, en su epígrafe.

### Del fotón al número

Cuatro pasos separan la luz de un fichero (oficio):

1. El fotosito convierte fotones en carga eléctrica. Cada fotosito es un pozo que acumula carga en
   proporción a la luz que recibe.
2. La carga se convierte en tensión y se amplifica.
3. El conversor analógico-digital traduce esa tensión en un número binario.
4. El procesador aplica la ganancia, el balance de blancos, la curva de transferencia y la
   compresión, y escribe el fichero.

El dispositivo que convierte las tensiones eléctricas almacenadas en cada píxel en valores digitales
de código binario es el ADC o conversor analógico-digital. Ni el sensor, que convierte luz en carga,
ni el amplificador de cada fotosito, que amplifica, digitalizan: la palabra que decide es «binario»,
y sólo un conversor analógico-digital produce números.

## Sensores

### CCD y CMOS

Son las dos tecnologías de sensor, y la diferencia está en dónde se hace la conversión (oficio).

| | CCD | CMOS |
|---|---|---|
| Dónde se lee la carga | Se transporta pozo a pozo hasta un conversor común | Cada fotosito tiene su propio amplificador |
| Obturación | Global: toda la imagen a la vez | Normalmente por barrido de líneas |
| Defecto característico | *Smear*: una raya vertical bajo una luz muy fuerte | *Rolling shutter*: verticales inclinadas en movimiento rápido |
| Consumo | Mayor | Menor |
| Dónde se usa hoy | Cámaras de estudio antiguas | Prácticamente todo |

El *smear* del CCD es una columna vertical clara que atraviesa la imagen cuando entra una luz
intensa en el cuadro. Las cámaras de reportaje actuales son CMOS: la Sony PXW-Z200 lleva un «**1.0
inch stacked CMOS image sensor**» y la Canon XF605 un «**Type 1.0 (1.0 in.) single-plate CMOS
sensor**» (fichas técnicas del fabricante).

### El obturador de persiana

La EBU describe así el defecto temporal del CMOS: «**Cameras with CCD sensors usually exhibit no odd
temporal effects, but cameras with one or more CMOS sensor can produce visible effects from the use
of a ‘rolling shutter’. The effect is identical to that seen in focal plane film stills cameras;
leaning verticals, distorted edges, and jelly-like images from rapid motion.**» (EBU Tech 3335,
§ 2.9). El obturador de persiana inclina las verticales cuando la cámara panea rápido o el sujeto
se mueve deprisa, porque la imagen no se lee de golpe sino de arriba abajo.

### Un sensor con máscara de Bayer o tres sensores con prisma

Un fotosito no distingue color: cuenta fotones y da un número, sin saber de qué longitud de onda
venían. Hay dos maneras de captar color (oficio):

- Tres sensores con prisma dicroico. Un prisma separa la luz en rojo, verde y azul y cada
  sensor recibe uno de los tres. Es el bloque clásico de las cámaras de estudio y de hombro de
  2/3 de pulgada.
- Un sensor con máscara de Bayer. Una máscara de Bayer es una superposición de microfiltros para
  sensores de imagen que permiten que los píxeles registren las longitudes de onda de la luz. Es un
  mosaico de filtros rojo, verde y azul en el que la mitad de los elementos son verdes y una cuarta
  parte rojos y otra cuarta parte azules. Se pone el doble de verdes porque el ojo humano obtiene
  del verde la mayor parte de la información de brillo.

La consecuencia de la máscara: cada píxel conoce sólo uno de los tres colores y los otros dos hay
que interpolarlos a partir de sus vecinos. Ese proceso se llama *demosaicing*, y es la razón de que
un mismo sensor pueda dar imágenes distintas según el procesado. La máscara reduce la sensibilidad
y la resolución de color, porque cada fotosito recibe sólo una parte del espectro.

No hay que confundirla con el filtro óptico paso bajo, otra pieza que va delante del sensor y que
limita el detalle más fino para que no aparezca muaré. La distinción: la máscara de Bayer da color;
el filtro paso bajo evita el muaré.

La EBU admite los dos diseños en todos sus niveles y fija el tamaño de sensor recomendado para cada
uno (EBU R 118 v2, tabla 2):

| Nivel | Un sensor | Tres sensores |
|---|---|---|
| UHD1 Tier 1 | **1 x 1”** | **3 x 2/3”** |
| HD Tier 1 | **1 x 2/3”** | **3 x 1/2"** |
| HD Tier 2L | **1 x 1/2"** | **3 x 1/3”** |
| HD Tier 2J | **1 x 1/3”** | **3 x 1/4"** |

Para HD Tier 1 pide «**10-bit**» y «**4:2:2**»; para 2L y 2J, «**8-bit (10-bit preferred)**».

### El tamaño del sensor, el píxel y la sensibilidad

A igual superficie de sensor, más píxeles quieren decir píxeles más pequeños, y un píxel más
pequeño recoge menos luz. La EBU lo usa para explicar por qué cada salto de resolución cuesta
sensibilidad: «**for a given sensor size, the pixels of a HDTV camera are much smaller than those of
a SDTV camera and similarly the pixels of a UHDTV camera are smaller than an HDTV camera**» (EBU
R 118 v2). Por la misma razón, a igual número de píxeles, un sensor grande tiene fotositos mayores
y es más sensible (oficio).

La relación entre el tamaño del sensor y la profundidad de campo se explica en «Ópticas».

### Resolución, aliasing y píxeles blancos

Tres avisos de la EBU y del fabricante sobre lo que el sensor no dice en su ficha:

- El número de píxeles no es la resolución: «**The sensor pixel count is not an acceptable measure
  of a camera’s actual resolution.**» (EBU R 118 v2, § 3.1.4).
- El aliasing se mueve al revés que la cámara: «**Aliasing is also highly distracting in a finished
  programme as it tends to move in the opposite direction to the movement of the camera**», y
  además estropea la compresión: «**Aliasing causes motion-dependent video compression to fail in
  the extreme**» (EBU R 118 v2, § 3.1.5). En la práctica, aparece al panear sobre texturas finas
  (rejillas, tejidos, ladrillo).
- Los puntos blancos aislados no son una avería: «**fine white flecks may be generated on the screen
  in rare cases, caused by cosmic rays, etc.**», y se ven sobre todo «**When operating at a high
  environmental temperature**» y «**When you have raised the gain (sensitivity)**» (Sony, PXW-Z200
  Help Guide, «Camera CMOS image sensor phenomena»).

## Ópticas

### La distancia focal y el ángulo de visión

La distancia focal de un objetivo se define, en términos ópticos, como la distancia en milímetros
entre el centro óptico del objetivo y el plano de imagen cuando el objetivo está enfocando al
infinito (oficio). Las dos condiciones importan: del centro óptico al plano de imagen, no del
cristal delantero ni de la montura; y enfocando al infinito, porque al enfocar más cerca el grupo de
lentes se desplaza y la distancia deja de ser la focal nominal.

El campo de visión desde la posición de la cámara se denomina ángulo, y su relación con la focal es
inversa: a más distancia focal, menos ángulo de visión. Depende también del tamaño del sensor: el
mismo objetivo da más ángulo sobre un sensor grande que sobre uno pequeño.

| Tipo de objetivo | Distancia focal | Ángulo |
|---|---|---|
| Gran angular | Corta | Amplio |
| Normal | La que iguala aproximadamente la diagonal del sensor | Parecido al de la visión humana |
| Teleobjetivo | Larga | Estrecho |

Como el ángulo depende del sensor, los fabricantes dan también la focal «equivalente» a la de un
formato de 35 mm, que permite comparar ópticas montadas sobre sensores distintos. El zoom de la Sony
PXW-Z200 es «**f = 7.71 to 154.21 mm, 24 to 480 mm (35 mm equivalent)**»; el de la Canon XF605,
«**f=8.3 – 124.5 mm, F/2.8 – 4.5, 15x optical zoom, 9-bladed iris diaphragm**» (fichas del
fabricante). La distinción que hay que fijar: el ángulo es cuánto se ve; la profundidad de campo es
cuánto está nítido. Uno se mide en grados y la otra en metros.

### Cómo se lee la referencia de un objetivo

Los objetivos zoom de televisión se nombran con una referencia que codifica sus datos (convención
del sector): las letras iniciales son la serie del fabricante; el número antes de la «x», la
relación de zoom (cuántas veces cabe la focal mínima en la máxima); el número después de la «x»,
la distancia focal mínima en milímetros; y las letras finales, los accesorios (servos, extensor,
versión). La focal máxima es la relación de zoom multiplicada por la focal mínima.

Un ejemplo con ficha del fabricante: el Fujinon UA22x4.8BERD es «**a portable zoom lens for 2/3-inch
sensor broadcast cameras, covering the wide to telephoto focal range from 4.8mm to 106mm**» (nota
de Fujifilm de 18 de marzo de 2026): 22 × 4,8 mm = 105,6 mm, que la ficha redondea a 106. La regla:
para saber qué objetivo es más tele hay que multiplicar los dos números, no comparar el primero; un
zoom de relación mayor no es más tele si parte de una focal mínima más corta.

### El diafragma y el número f

El número f expresa la apertura relativa del diafragma, y se calcula como la distancia focal
dividida por el diámetro efectivo de la pupila de entrada (oficio). De ahí sale la particularidad
que desconcierta: cuanto menor es el número f, más abierto está el diafragma y más luz pasa.

| Número f | Apertura | Luz que pasa |
|---|---|---|
| f/1,4 | Muy abierto | Mucha |
| f/2,8 | Abierto | — |
| f/5,6 | Medio | — |
| f/22 | Muy cerrado | Poca |

La escala de números f va de raíz de dos en raíz de dos, y cada paso completo duplica o reduce a la
mitad la luz: 1,4 · 2 · 2,8 · 4 · 5,6 · 8 · 11 · 16 · 22.

La velocidad de un objetivo es su menor número f, es decir, su apertura máxima. Se llama así porque
un objetivo que abre más deja pasar más luz, y con más luz se puede usar un obturador más rápido. El
mayor número f es lo contrario: la apertura mínima.

En muchos zooms la apertura máxima no es la misma en todo el recorrido: la ficha de la Z200 da una
«**Open aperture (F-number) F2.8 to F4.5, minimum aperture (F-number) F11**», y la de la XF605
«**F/2.8 – 4.5**». La cifra mayor corresponde al extremo tele: al cerrar el plano con el zoom, la
óptica pierde luz (oficio).

### La difracción

Cerrar mucho el diafragma no da más nitidez sin límite. Los fabricantes lo advierten: «**When
shooting a brightly lit subject, closing the iris too much may cause diffraction blur, producing an
image starting to go out of focus (typical phenomena in video cameras). You can suppress this effect
to obtain better shooting results using the ND filter.**» (Sony, PXW-Z200 Help Guide, «Adjusting
the Light Level»). El remedio, el filtro de densidad neutra, se explica en «Filtros».

### La profundidad de campo

La profundidad de campo es la zona, delante y detrás del punto enfocado, que se percibe
aceptablemente nítida (oficio). Depende de tres cosas:

| Factor | Efecto |
|---|---|
| Apertura del diafragma | Diafragma más cerrado → más profundidad |
| Distancia focal | Focal más larga → menos profundidad, a igual distancia de enfoque |
| Distancia de enfoque | Más lejos → más profundidad |

Reduciendo la apertura del diafragma se aumenta la profundidad de campo, porque un diafragma más
cerrado hace más estrecho el cono de rayos que llega a cada punto del sensor, así que los puntos que
están fuera del plano de enfoque dibujan un círculo más pequeño y caen dentro del límite de lo que se
percibe nítido. El diafragma no cambia el encuadre.

La afirmación «a mayor distancia focal, menor profundidad de campo» sólo es cierta si se mantiene la
distancia de enfoque. Si al poner una focal más larga se retrocede para mantener el mismo encuadre,
la profundidad de campo apenas cambia. Lo que reduce la profundidad no es la focal por sí sola, es
la focal larga usada desde la misma distancia, que da un plano más cerrado.

### El círculo de confusión y la distancia hiperfocal

El círculo de confusión es el tamaño máximo que puede tener el punto desenfocado sin que el ojo lo
distinga de un punto nítido. Es el criterio con el que se decide qué es nítido, y por eso aparece
en el cálculo de la profundidad de campo y de la hiperfocal. No hay un punto nítido y todo lo demás
borroso; hay una zona en la que el desenfoque no se nota.

La distancia hiperfocal es la distancia de enfoque a partir de la cual todo, desde la mitad de esa
distancia hasta el infinito, queda dentro de la profundidad de campo. Es el ajuste que da la máxima
profundidad posible con una focal y un diafragma dados. Los tres factores que intervienen en su
cálculo son la distancia focal, la apertura del diafragma y el círculo de confusión. La obturación
no influye: el obturador controla cuánto tiempo llega la luz al sensor, y la nitidez de un punto
fuera de foco es un problema de geometría, no de tiempo. Cerrar el diafragma suele obligar a
alargar la obturación para mantener la exposición, así que las dos cosas cambian juntas; pero la que
altera la profundidad es el diafragma.

### El tamaño del sensor y la profundidad de campo

Las cámaras con sensores grandes dan menores profundidades de campo que las de sensores de dos
tercios de pulgada, a igual encuadre y distancia, porque un sensor grande abarca más escena con la
misma óptica y exige una focal más larga para el mismo encuadre (oficio). El razonamiento:

1. La profundidad de campo depende de la focal, del diafragma y de la distancia de enfoque. El
   tamaño del sensor no aparece en esa lista.
2. Pero un sensor grande abarca más escena con la misma óptica, así que para conseguir el mismo
   encuadre desde el mismo sitio hay que poner una focal más larga.
3. Y a más focal, menos profundidad de campo, manteniendo la distancia de enfoque.

Por tanto, el sensor grande no reduce la profundidad de campo por sí mismo: la reduce la focal más
larga que obliga a usar. Al revés, son los sensores pequeños los que «multiplican» la focal
equivalente. La consecuencia de oficio: con una cámara de sensor grande cuesta mucho más mantener
el foco, y por eso los informativos han trabajado durante décadas con sensores pequeños, cuya mayor
profundidad de campo perdona el error de foco cuando no hay tiempo de medir.

### Las aberraciones y el *bokeh*

Una aberración es un defecto de formación de la imagen que un sistema óptico introduce, y no se
corrige enfocando: es propio del diseño y de los materiales del objetivo (oficio). Las cinco
aberraciones básicas de Seidel son monocromáticas:

| Aberración | Qué hace |
|---|---|
| Esférica | Los rayos que pasan por el borde de la lente enfocan en un punto distinto que los del centro |
| Coma | Un punto fuera del eje se dibuja como una coma o un cometa |
| Astigmatismo | Las líneas radiales y las tangenciales no enfocan a la vez |
| Curvatura de campo | La imagen nítida se forma sobre una superficie curva y el sensor es plano: si se enfoca el centro, los bordes salen blandos |
| Distorsión | Las líneas rectas salen curvadas: de barril hacia fuera, o de corsé hacia dentro |

La aberración cromática es aparte, y viene de que el índice de refracción depende de la longitud de
onda. La de barril no es una aberración distinta: es un tipo de distorsión.

El *bokeh* es la calidad estética de las zonas desenfocadas: no cuánto desenfoque hay, que es la
profundidad de campo, sino cómo se ve. Depende de la forma y el número de láminas del diafragma
—más láminas y más redondeadas dan círculos más redondos— y del diseño del objetivo. Otros dos
términos que no hay que confundir con él: el *flare*, el velo o los destellos que produce la luz
parásita dentro del objetivo, y el *knee*, que es un ajuste electrónico de la cámara, no óptico.

### La montura y la distancia de brida

La montura es la unión mecánica y óptica entre objetivo y cuerpo, y cada una tiene su distancia de
brida. Sony la define como la distancia «**from the lens attachment surface and the plane of the
imaging device**» (PXW-Z200 Help Guide, «Adjusting the Flange Focal Distance»). Los objetivos de
televisión de 2/3 de pulgada usan la montura B4, detrás de la cual va el bloque de prisma de tres
sensores (oficio).

La consecuencia práctica de la distancia de brida (oficio): un objetivo se puede adaptar a un
cuerpo cuya brida sea más corta, poniendo un anillo que rellene la diferencia; nunca a uno cuya
brida sea más larga.

### El estabilizador

Las cámaras de reportaje llevan estabilización óptica o electrónica de la imagen. Sony advierte de
dos cosas: con trípode hay que apagarla, «**When shooting using a tripod for stability, set image
stabilization to [Off]. If you perform slow pan/tilt movements with image stabilization set to
[Standard] or [Active], the image may become distorted.**»; y el modo más fuerte cierra el plano:
«**[Active]: Applies more powerful correction than [Standard] for correcting stronger camera shake,
such as shooting while walking. The framing shifts slightly to the telephoto side.**» (PXW-Z200 Help
Guide, «Using Image Stabilization»). La XF605 combina «**Optical-shift image stabilizer + digital
compensation**».

## Enfoque

### El foco manual

En televisión el foco es sobre todo manual: es el operador quien decide qué está nítido. El
fabricante enumera los casos en los que el manual es necesario: «**Subjects on the far side of a
window covered in water droplets**», «**Subjects with low contrast against the background**»,
«**Subjects further away than nearby subjects**» y «**When focus is lost due to a large change in
the ambient temperature (changes due to the temperature characteristics of the lens)**» (Sony,
PXW-Z200 Help Guide, «Adjusting the Focus Manually»).

La técnica de oficio con zoom: se cierra al máximo el plano (extremo tele) sobre el sujeto, se
enfoca ahí, donde la profundidad de campo es mínima y el error se ve, y se abre al encuadre
deseado. Si el tiraje está bien ajustado, el foco se mantiene en todo el recorrido del zoom.

### El ajuste de tiraje

El ajuste de tiraje de un zoom es el *back focus* o foco de carro: el ajuste de la distancia entre
el plano de la montura y el plano del sensor (oficio). Si esa distancia no es exactamente la que el
objetivo espera, el enfoque no se mantiene al recorrer el zoom. Sony lo dice así: «**This
adjustment will be required if the focus is not correct at the wide-angle and telephoto ends of the
optical zoom. When adjusted correctly, the focus will be maintained if you change the zoom position
after adjusting the focus.**» (PXW-Z200 Help Guide, «Adjusting the Flange Focal Distance»).

Hay que hacerlo cada vez que se cambia de objetivo o de cuerpo, cuando el equipo ha sufrido un golpe
y cuando hay un cambio grande de temperatura (oficio). El método, en cuatro pasos:

1. Se va al tele sobre un punto alejado o una carta y se enfoca ahí, porque en el tele la
   profundidad de campo es mínima.
2. Se va al angular sin tocar el foco. Si el tiraje está mal, la imagen se desenfoca al llegar al
   angular.
3. Se corrige con el anillo de tiraje, no con el de foco.
4. Se repite y se recorre el zoom entero comprobando que el enfoque se mantiene.

Se hace con el diafragma abierto, para que la profundidad de campo no disimule el error. En el habla
de plató, «cerrar» un zoom es ir al tele y «abrir» es ir al angular, sin relación con el diafragma.

Algunas cámaras de óptica fija lo hacen solas sobre una carta: la Z200 pide colocar la carta de
ajuste «**about 2 m (6 ft) away**», encuadrarla en tele, pasar al angular con el diafragma a
«**F2.8 (open)**» y la ganancia a «**0 dB**», y ejecutar «**[Technical] – [Lens] – [Auto FB Adjust] –
[Execute]**» (PXW-Z200 Help Guide).

### Las ayudas al enfoque: realce de contornos y lupa

El visor de una cámara de reportaje es pequeño, y la resolución de la imagen es mayor que la del
visor. Para juzgar el foco las cámaras traen dos ayudas que no se graban:

- El realce de contornos (*peaking*): «**You can display an image on the LCD screen with its
  outlines enhanced. This function helps you to adjust the focus.**»; se elige color («**WHITE, RED,
  YELLOW**») y sensibilidad («**HIGH, MIDDLE, LOW**»); y «**The enhanced outlines will not be
  recorded on the memory card.**» (Sony, PXW-FS5 Operating Guide). En la Z200 el nivel es
  «**[High] / [Mid] / [Low]**» con «**[Mid]**» de fábrica, y el color «**[B&W] / [Red] / [Yellow] /
  [Blue]**» (Help Guide, menú [Monitoring]). Blackmagic ofrece dos modos, «**‘peaking’ and ‘colored
  lines’**».
- La lupa de enfoque: «**The selected area on the LCD screen is magnified and displayed. This is
  useful when adjusting the focus.**» (FS5). En la Z200 amplía el centro «**approximately three
  times**» y, con otra pulsación, «**approximately six times**»; y «**The recorded image or SDI/HDMI
  output image is not magnified when the focus is magnified.**»

Las dos se combinan: «**You can focus more easily using this function in combination with the focus
magnifier function**» (FS5). El nivel de realce depende del plano: «**When focusing on actors, for
example, a higher level of focus assistance can help resolve edge detail in faces. A shot of foliage
or brickwork, on the other hand, may show distracting amounts of focus information at higher
settings.**» (Blackmagic, URSA Broadcast G2).

### El autofoco

Los autofocos de las cámaras de reportaje actuales combinan dos métodos: «**The unit uses phase
detection AF for high-speed focusing and contrast AF for high-accuracy focusing. The combination of
these two AF methods provides auto focus with both high speed and high accuracy.**» (Sony, PXW-Z200
Help Guide). Canon distingue en la XF605 «**Dual Pixel CMOS AF, contrast-detection AF**» y ofrece
«**Manual focus, autofocus (AF-boosted MF, continuous AF, Face AF); face detection and subject
tracking available**».

Lo que un operador ajusta del autofoco:

- La zona: en la Z200, «**[Wide]**» busca el sujeto en todo el cuadro, «**[Zone]**» dentro de una
  zona y «**[Flexible Spot]**» en un punto elegido.
- La velocidad de transición: con «**[1(Slow)]**», «**the focus moves slowly when the subject to be
  focused changes**»; con «**[7(Fast)]**», el cambio es inmediato, «**ideal for documentary shooting
  which requires quick focusing**».
- La sensibilidad al cambio de sujeto: con «**[1(Locked On)]**», «**the focus does not readily shift
  even if another subject moves in front of the in-focus subject**»; con «**[5(Responsive)]**», da
  prioridad al que se cruza.
- La detección de caras o personas, que prioriza «**the focusing/tracking on the face/eye/head/body**»
  (Z200). Tiene límites: «**Faces may not be detected depending on the recording environment, the
  condition of the subject or the settings.**» (FS5).

Y un mando mixto muy usado en informativos: el autofoco momentáneo. Con el foco en manual, se pulsa
un botón y la cámara enfoca sola mientras se mantiene pulsado: «**The focus returns to manual focus
when you release the button.**» (Z200, «Using Auto Focus Temporarily»). El autofoco no sustituye al
criterio: «**Accuracy may not be obtained depending on the shooting conditions.**» (Z200).

## Exposición

### Los cuatro mandos de la exposición

La exposición es la cantidad de luz que llega al sensor y cómo la cámara la convierte en señal. Un
operador la gobierna con cuatro mandos (oficio):

| Mando | Qué cambia además de la luz |
|---|---|
| Diafragma | La profundidad de campo |
| Obturación | La nitidez del movimiento y el parpadeo |
| Filtro ND | Nada más: quita luz sin tocar el color |
| Ganancia | El ruido |

El orden correcto cuando falta luz es: abrir el diafragma, bajar la obturación si el movimiento lo
permite, añadir luz y, sólo entonces, subir ganancia. Cuando sobra, se mete filtro ND antes de
cerrar el diafragma hasta la zona de difracción.

Cada mando puede ir en automático. En la Z200, con el conmutador en AUTO, «**the auto ND filter,
auto iris, auto gain control, auto shutter, and ATW mode are enabled, and the brightness and white
balance are adjusted automatically. To adjust these items separately, set the AUTO/MANUAL switch to
MANUAL.**» (PXW-Z200 Help Guide, «Shooting in FULL AUTO mode»). Entre el manual y el automático está
el automático momentáneo: con el diafragma en manual, un botón de diafragma automático corrige
mientras se pulsa, y «**The iris returns to the previous setting when you release the button.**»
(Z200, «Adjusting the Iris»). En reportaje el automático permanente se evita porque el diafragma
«respira» cuando entra o sale del cuadro algo claro u oscuro (oficio).

### La obturación: velocidad, ángulo y parpadeo

La obturación fija cuánto tiempo recibe luz el sensor en cada cuadro. Se expresa como velocidad (una
fracción de segundo) o como ángulo, heredado del obturador de disco del cine: 360° es todo el tiempo
del cuadro y 180° la mitad (oficio). La Z200 admite las dos formas: «**You can set the shutter speed
as an angle, or set the shutter speed value directly according to the frequency of the light
source.**» La EBU toma como nominal «**1/50 second for 50 Hz, 1/60 for 59.94 Hz, or 180 degrees for
either**» (EBU Tech 3335, § 2.9).

Un obturador más corto congela el movimiento y quita luz; uno más largo deja estela. Y la cadencia
también cuesta luz: «**if you switch from 25 to 50 frames per second, the amount of light reaching
the sensor will be halved. To maintain your exposure you need to compensate for this change by
opening up your lens an extra stop, by opening up your shutter angle from 180º to 360º or by adding
some extra lighting**» (Blackmagic, URSA Broadcast G2).

El parpadeo aparece cuando la obturación no casa con la frecuencia de la luz: «**If shooting under
lighting produced by fluorescent lights, sodium lamps, mercury-vapor lamps, or LEDs, the screen may
flicker or colors may vary.**» (Sony, PXW-Z200 Help Guide). Blackmagic avisa de que puede no verse
en el visor: «**You may not see these flicker issues when previewing the scene on your LCD and SDI
feed or while recording, so it’s important to perform a test shoot with the lights you plan to
use**», y de que «**Your shutter setting can also affect the visibility of flicker when shooting
under lights**». La Z200 trae una corrección de parpadeo con modo «**[Auto] / [On] / [Off]**» y la
frecuencia de la red que alimenta las luces, «**[50Hz] / [60Hz]**». En Europa la red es de 50 Hz, y
la obturación a 1/50 o 1/100 es la que evita el parpadeo de la iluminación de red (oficio).

### Las ayudas a la exposición: cebra, monitor de forma de onda y falso color

El ojo se engaña con el visor; la exposición se mide. Tres ayudas, ninguna de las cuales se graba:

- La cebra: «**The zebra pattern is a stripe pattern that appears in areas of brightness equal to or
  exceeding the brightness level you have set.**» y «**Zebra is not recorded onto the memory card.**»
  (Sony, PXW-FS5 Operating Guide). La Z200 tiene dos cebras con nivel ajustable «**0% to 109%**»: la
  1 viene a «**70%**», con un margen de apertura de «**10%**» (ajustable de «**2% to 20%**»), y la 2 a
  «**100%**» (menú [Monitoring] – [Zebra]). Blackmagic explica su uso: «**setting zebra to 100%
  shows which areas are completely overexposed**», y «**If you’re shooting in variable light such as
  outdoors on a partly overcast day, setting your zebra level lower than 100 can warn you of
  potential overexposure.**» En oficio, la cebra alta avisa del blanco quemado y la baja, con su
  margen, sirve para colocar el nivel de un rostro.
- El monitor de señal: la Z200 muestra en el visor «**a waveform, vectorscope, and histogram**», y
  «**The orange line indicates the set value of the zebra level.**» El monitor de forma de onda
  enseña el nivel de cada zona de la imagen en su posición horizontal; el histograma, cuántos puntos
  hay en cada nivel; el vectorscopio, el tono y la saturación del color (oficio).
- El falso color: «**False color overlays different colors onto your image that represent exposure
  values for different elements in your image.**» En la escala de Blackmagic, «**pink represents
  optimum exposure for lighter skin tones, while green is a good match to darker skin tones**», y
  «**when elements in your image change from yellow to red, that means they are now over
  exposed**». Los colores del falso color no están normalizados: cada fabricante tiene su escala.

### Los límites de la señal según la EBU

La EBU fija los márgenes de la señal digital en valores de código (EBU R 103 v3.0, tabla 1):

| Bits | Rango nominal | Mínimo/máximo preferente | Rango total |
|---|---|---|---|
| 8 bits | **16 - 235** | **5 - 246** | **1 - 254** |
| 10 bits | **64 - 940** | **20 - 984** | **4 - 1019** |

El rango nominal va del negro al blanco de pico; el preferente deja un margen por arriba y por
abajo; y lo que sale del preferente es error de gama: «**Any signals outside the "Preferred
Minimum/Maximum" range are described as having a gamut error (or as being out-of-gamut). Signals
shall not exceed the "Total Video Signal Range", overshoots that attempt to "exceed" these values
may clip.**» La recomendación general es que la señal «**should not normally exceed the "Preferred
Minimum/Maximum" range**», y que los aparatos de medida sólo avisen «**after the error exceeds 1% of
the image**».

Para la cámara en directo, la regla es ésta: «**Care should be taken with live productions,
especially those with uncontrolled lighting, to prevent clipping of highlights during temporary
excursions to extremes of code values, i.e. camera clippers should be set to Preferred Range limits
(as per this document). For pre-produced and colour graded material, the nominal limits contained
in this document should be followed closely.**» En analógico, el rango normal equivale a «**0 mV to
700 mV luminance amplitude**».

Un aviso: los porcentajes «−1 % y 103 %» que circulan como «norma EBU» no están en la versión 3.0
vigente de la R 103, que se expresa en valores de código.

### El *knee* y las altas luces

El *knee* es el circuito que comprime las altas luces para que la información por encima del blanco
de referencia quepa dentro del margen de la señal en lugar de recortarse de golpe (oficio). La
respuesta de la cámara es aproximadamente recta hasta un punto —el codo, que es lo que significa la
palabra— y a partir de ahí se tumba. Todo lo que hay por encima del codo se representa con muchos
menos niveles, así que cabe más margen de luz en la señal a cambio de menos matiz en las luces.

| Ajuste | Qué controla |
|---|---|
| Punto del codo | A qué nivel empieza la compresión |
| Pendiente del codo | Cuánto se tumba la curva a partir de ahí |
| Recorte de blancos | El techo absoluto: por encima, todo es blanco |

El *knee* no cambia la sensibilidad ni oscurece la imagen: reparte de otra manera lo que ya se captó
para conservar información en las luces, como la ventana de una entrevista en interior.

### El margen de exposición

El margen de exposición (latitud) es la distancia entre la luz más baja y la más alta que la cámara
registra con detalle: «**It is limited at the low end by noise levels, and at the high end by the
clipping level.**» (EBU R 118 v2, § 3.1.3). La EBU da cifras de referencia (EBU Tech 3335):

- Margen sobre el blanco: «**This ‘headroom’ varies in cameras between about 1 stop and 3 stops.**»
- Margen total: «**A typical broadcast camera with video noise levels of about -50dB can capture
  about 7.5 stops, with the controls set to factory settings.**»
- El ruido se lo come: «**the effective dynamic range will be reduced by about 1 stop per 6dB of
  video noise level increase.**»
- La curva lo amplía: «**most cameras [...] can be set to capture at least 1 extra photographic stop
  by manipulation of the gamma curve and/or knee. In some extreme cases, cameras can capture up to 3
  extra stops, and effectively handle 12 to 13 stops**».

### Las curvas logarítmicas y el visor

Una curva logarítmica reparte los valores disponibles a lo largo de todo el rango dinámico del
sensor, en lugar de concentrarlos donde quedarían bien a la vista (oficio). El resultado es una
imagen de bajo contraste y baja saturación que conserva información en luces y sombras, y que exige
etalonaje.

Si se graba con curva logarítmica, la imagen del visor parecerá lavada, plana y sin contraste, y
para previsualizar el aspecto final hay que aplicar una LUT. El operador juzga la exposición, el
foco y el encuadre por lo que ve en el visor; con una imagen lavada no se ve si una zona está
quemada ni si un rostro está bien expuesto. La LUT de monitorización devuelve al visor un contraste
juzgable sin tocar lo que se graba.

| | Lo que se graba | Lo que se ve en el visor |
|---|---|---|
| Sin LUT | Logarítmico | Logarítmico: lavado |
| Con LUT de monitorización | Logarítmico, sin cambios | Con el contraste aplicado: juzgable |

La salida SDI lleva la misma señal logarítmica: un monitor conectado ahí verá la misma imagen
lavada, salvo que el propio monitor aplique una LUT. La interfaz es un transporte, no un procesador.

Las cámaras de reportaje traen curvas logarítmicas y de alto rango dinámico junto a las de
televisión estándar: la Z200 ofrece, entre sus aspectos base, «**[ITU709]**», «**[S-Log3]**» y
«**[HLG Live] / [HLG Mild] / [HLG Natural]**».

### La sensibilidad de catálogo

La sensibilidad de una cámara se da como el diafragma con el que se expone bien una carta en
condiciones fijas. El método de la EBU: «**Measure the exposure lens aperture, at 2000-lux
illumination level and 0 dB gain (or the recommended nominal gain setting), at which the white side
of a Kodak Gray card produces peak white signal level (100%).**»; y «**the exposure figure should
match the manufacturer’s specification (normally taken for a white card with 89.9%
reflectance)**» (EBU R 118 v2, § 3.1.2). Así se leen las fichas: la Canon XF605 da «**(2000 lux,
89.9% reflection, [High Sensitivity Mode] set to [On]) [...] 50.00 Hz: F13 (at 50.00P)**». A mayor
número f en esa prueba, más sensible es la cámara.

Con curva logarítmica la cámara puede no llegar al 100 %; entonces la EBU mide el diafragma que da
«**exactly 50% signal level [...] with 2000 lux illumination of a 90% grey card. This exposure level
is typically 2 stops below peak exposure for a conventional gamma curve**» (EBU Tech 3335).

## Balance de blancos

### Qué es y qué hace la cámara

El balance de blancos es el ajuste de la temperatura de color de la cámara a la existente en la
escena (oficio). No se cambia la luz de la escena: se ajusta la cámara a ella. Equilibrar la
iluminación para evitar dominantes es trabajo del iluminador con filtros; ajustar la cantidad de
luz es exposición y ganancia.

Al hacerlo, la cámara mide una superficie que se le presenta como blanca y ajusta la ganancia
relativa de los canales rojo y azul hasta que los tres canales dan el mismo valor. A partir de ahí,
lo que era blanco en la escena sale blanco en la señal, y todo lo demás cae en su sitio. La luz de
tungsteno es rojiza (temperatura de color baja, en torno a 3.200 K) y la luz de día azulada (en
torno a 5.600 K); los preajustes de las cámaras usan esas dos cifras: la Canon XF605 trae
«**daylight, 5,600 K**» y «**tungsten lamp, 3,200 K**», y advierte de que «**Color temperatures are
approximate and given only as a reference.**» La temperatura de color y su medida se desarrollan en
el tema de iluminación.

### Cómo se hace

Tres caminos, que son oficio de reportaje:

| Camino | Cuándo |
|---|---|
| Balance automático sobre una carta blanca | Siempre que haya tiempo: es el fiable |
| Preajuste de 3.200 K o 5.600 K | Cuando no hay tiempo y se sabe qué luz hay |
| Balance automático continuo | Cuando la luz cambia sin control, a cambio de que los tonos deriven en plano |

El procedimiento sobre carta, en una cámara de reportaje (Sony, PXW-Z200 Help Guide, «Adjusting the
White Balance Manually»):

1. Se elige memoria A o B con el conmutador de balance (la posición PRESET usa el preajuste, que de
   fábrica es «**[3200K]**»).
2. «**Place white paper (or other object) in a location with the same lighting source and conditions
   as the subject, then zoom in on the paper to show white on the screen.**»
3. Se ajusta el brillo con el diafragma en manual.
4. Se pulsa el botón de balance (WB SET): el resultado se guarda en la memoria elegida.

Las memorias permiten tener dos balances listos —por ejemplo, interior y exterior— y pasar de uno a
otro sin repetir la medida. Los preajustes de la Z200 en modo estándar son «**[3200K] → [4300K] →
[5600K] → [6300K]**», y la temperatura puede fijarse a mano entre «**2000 K to 15000 K**» (ficha
técnica).

### El balance automático continuo

El automático continuo sigue los cambios de luz, pero tiene límites que el fabricante declara: «**It
may not be possible to adjust to the appropriate color using ATW, depending on the lighting and
subject conditions.**», por ejemplo «**When a single color dominates the subject, such as
sky/sea/ground/flowers or similar.**» o «**When the subject is lit by a light source with extremely
high or extremely low color temperature.**» (Z200). La cámara permite congelarlo con una función
de retención (*ATW Hold*).

El aviso de oficio: el balance automático continuo es el enemigo del montaje. Dos tomas de la misma
escena salen de distinto color, y el montador no puede casarlas. En reportaje se hace balance fijo y
se rehace cuando cambia la luz. En multicámara, además, el balance tiene que ser igual en todas las
cámaras, y de eso responde el control de imagen.

## Ganancia

### Decibelios y pasos

La ganancia es una amplificación electrónica de la señal, y se mide en decibelios. No añade luz:
amplifica lo que hay, con su ruido incluido (oficio).

Si se activan 6 dB de ganancia, la equivalencia en pasos de diafragma es un paso. Un paso de
diafragma duplica la luz; en decibelios de tensión, duplicar es +6 dB, porque 20 por el logaritmo
decimal de 2 es aproximadamente 6.

| Ganancia | Pasos de diafragma | Precio en ruido |
|---|---|---|
| +3 dB | Medio paso | Poco |
| +6 dB | 1 paso | Apreciable |
| +12 dB | 2 pasos | Mucho |
| +18 dB | 3 pasos | La imagen ya es ruidosa |

Las cámaras dan la ganancia en conmutador de tres posiciones con valores preajustables: en la Z200,
el conmutador ISO/GAIN tiene posiciones L, M y H, cuyo valor se cambia en el menú, y la ganancia va
de «**−3 dB to +36 dB (1 dB increments, using SDR ITU709)**» (ficha técnica). Algunas cámaras la
expresan también como sensibilidad ISO: la Canon XF605 da «**ISO200 to ISO12800**» y «**Gain: –6 dB
to 21.0 dB**». El ajuste fino sirve para corregir la exposición sin tocar el diafragma: «**This is
useful when you want to adjust the exposure by one step without changing the depth of field.**»
(Z200, «Adjusting the Gain»). La ganancia automática (AGC) se evita en toma controlada por la misma
razón que el diafragma automático.

### El precio: el ruido

La EBU fija la relación señal/ruido mínima de cada nivel de cámara (EBU R 118 v2, tabla 6):

| Nivel | Relación señal/ruido |
|---|---|
| HD Tier 1 | «**Better than -48 dB @ 0db gain**» |
| HD Tier 2L | «**Better than -44 dB**» |
| HD Tier 2J y Tier 3 | «**Better than -40 dB**» |

Y dos matices: «**Noise should be rated by its impact and visibility as well as by measurement.**»;
y la ganancia negativa mejora el ruido: «**Some camera menus allow negative gain settings (with
respect to the published 0 dB). It is therefore possible to improve the S/N ratio using a negative
(lower) gain setting.**» Cada 6 dB de ruido de más cuestan además un paso de margen de exposición
(epígrafe «El margen de exposición»), y subir la ganancia hace más visibles los píxeles blancos del
sensor.

El ruido se ve sobre todo en las sombras, y dos circuitos de la cámara actúan ahí en sentido
contrario (oficio). El levantado de negros actúa sobre la luminancia y sólo levanta las sombras:
abre lo que hay en ellas, a cambio de perder contraste y hacer visible el ruido que en negro no se
veía. La dependencia del nivel reduce o suprime el realce de detalle en las zonas oscuras, donde el
ruido es peor: el ruido de las sombras deja de realzarse y se disimula, mientras el detalle de las
zonas bien iluminadas se mantiene.

### La ganancia es el último recurso

Cada paso de ganancia es un paso de ruido, y el ruido de una toma no se quita después. Antes de
subir ganancia se abre el diafragma, se baja la obturación si el movimiento lo permite y se añade
luz (oficio).

## Filtros

### La densidad neutra

Un filtro de densidad neutra (ND) reduce la luz sin alterar el color. Las cámaras de reportaje lo
llevan dentro, en una rueda o disco con posiciones fijas y, en las más recientes, también variable:

- Sony PXW-Z200: «**[Clear]: No ND filter**», «**1: 1/4ND**», «**2: 1/16ND**», «**3: 1/64ND**»
  (valores de fábrica de las tres posiciones, que el menú permite cambiar entre «**1/4 / 1/8 / 1/16 /
  1/32 / 1/64 / 1/128**») y «**Linearly variable ND: 1/4ND to 1/128ND**».
- Sony PXW-FS5: posiciones «**1/4**», «**1/16**», «**1/64**» y modo variable «**in the range 1/4 to
  1/128**».
- Canon XF605: «**ND Filter Built-in (Off,1/4, 1/16, 1/64), motor operated**».

La fracción es la luz que deja pasar. Como cada paso de diafragma es la mitad de luz, 1/4 son dos
pasos, 1/16 cuatro, 1/64 seis y 1/128 siete (cálculo: 2 elevado al número de pasos). La posición
«clear» no es un filtro: es el hueco sin filtro, y no quita luz.

El ND variable permite además la exposición automática por filtro: en la Z200, «**Set [Auto ND
Filter] to [On] to enable auto exposure adjustment using the ND filter.**», que cambia la luz sin
tocar el diafragma ni, por tanto, la profundidad de campo.

Cambiar de filtro durante la toma se nota: «**If you switch ND FILTER dial A during recording, the
image or sound may become distorted.**» (FS5); en la Z200, al pasar de o a «clear» grabando, «**the
ND filter frame is displayed on the image and the operating sound is included in the audio**».

### El ND para abrir el diafragma

El filtro ND sirve para dos cosas: evitar la difracción cuando hay mucha luz (epígrafe «La
difracción») y conseguir poca profundidad de campo con exposición correcta. El razonamiento
(oficio):

1. Menos profundidad de campo se consigue abriendo el diafragma.
2. Pero abrir el diafragma sobreexpone, si la luz es la que es.
3. Un filtro de densidad neutra quita luz sin tocar el color.
4. Cuanto más denso sea el filtro, más se puede abrir el diafragma manteniendo la exposición
   correcta.
5. Por tanto, el filtro más denso disponible es el que permite el diafragma más abierto y la menor
   profundidad de campo.

Un filtro ND no cambia por sí mismo la profundidad de campo: lo que hace es permitir un diafragma
más abierto, y es el diafragma el que la cambia.

### Los filtros de conversión y la corrección electrónica

Un filtro de conversión cambia la temperatura de color de la luz: por ejemplo, para rodar con
balance de tungsteno bajo luz de día, o al revés (oficio). En las cámaras actuales la corrección de
color se hace sobre todo electrónicamente, con el balance de blancos y sus preajustes; el filtro de
conversión queda para la iluminación (geles en los focos), que se trata en el tema de iluminación.

### Los filtros delanteros

Se enroscan o se colocan delante del objetivo (el de la Z200 tiene un diámetro de filtro de
«**72 mm**»). Los que un operador lleva en el maletín (oficio):

| Filtro | Qué hace | Cuándo se usa |
|---|---|---|
| Polarizador | Elimina la luz polarizada por reflexión | Cielos, reflejos en cristal y en agua |
| Degradado | Oscurece una parte del cuadro | Cielos muy contrastados frente al suelo |
| Difusor | Suaviza | Retrato |
| Ultravioleta y de protección | Protege el frontal | Siempre |

Para resaltar las nubes y oscurecer el cielo se usa el polarizador. La luz del cielo azul está
parcialmente polarizada, y un polarizador puede bloquearla selectivamente: el cielo se oscurece y se
satura, mientras que las nubes, que reflejan luz no polarizada, mantienen su brillo. El efecto es
máximo cuando el eje de la cámara forma noventa grados con la dirección del sol, y nulo cuando se
apunta al sol o en su misma dirección. Un filtro neutro o un degradado oscurecen cielo y nubes por
igual y no separan unas de otro.

Delante del objetivo va también el parasol, y en cámara de estudio o de retransmisión la bandera
francesa: una pantalla opaca en un brazo articulado sobre la cámara que hace sombra al objetivo para
evitar que una luz directa entre en el frontal y produzca velo. Se ajusta con el zoom en el angular,
el ángulo más amplio: si no asoma en el encuadre en el angular, no asoma en ninguna focal (oficio).

## Recomendaciones técnicas que el tema cita

No hay norma jurídica que regule este tema. Las recomendaciones técnicas que cita, en su edición
vigente el 24/09/2026:

- EBU R 103 v3.0, *Video Signal Tolerance in Digital Television Systems*, Ginebra, mayo de 2020:
  márgenes de la señal digital y ajuste de los recortadores de cámara.
- EBU R 118 v2, *Tiering of Cameras for use in Television Production*, Ginebra, abril de 2017:
  niveles de calidad de cámara, tamaños de sensor, relación señal/ruido, sensibilidad, margen de
  exposición, resolución y aliasing.
- EBU Tech 3335, *Methods of measuring the imaging performance of television cameras for the
  purposes of characterisation and setting*, Ginebra, agosto de 2014: métodos de medida, obturador
  de persiana, obturación nominal y margen dinámico.

## Lo que este tema no da, y dónde está

- Qué cámaras, ópticas y filtros usa CSRTV: no consta en un documento publicado localizado. Los
  ejemplos de este tema son cámaras de reportaje del mercado con manual público (Sony, Canon,
  Blackmagic), no el parque de la RTVA.
- El funcionamiento interno del autofoco de doble píxel de Canon: sólo se ha leído el nombre en
  la ficha técnica; las páginas del fabricante no pudieron leerse.
- El obturador global en cámaras de estudio actuales: la documentación del fabricante no pudo
  leerse.
- Las distancias de brida de cada montura (B4, PL, EF, E) en milímetros: no se ha leído la
  especificación de cada montura; el tema da sólo el concepto.
- El nivel de señal del blanco de referencia HDR en porcentaje: está en el Informe UIT-R
  BT.2408, que no pudo leerse.
- La temperatura de color, la escala mired, los filtros de corrección en los focos y el
  contraste de iluminación, en el tema 5 de este específico.
- La profundidad de campo como recurso de lenguaje, en el tema 2; la calidad técnica de la
  imagen (ruido, compresión, detalle, igualación de cámaras), en el tema 9; los formatos de
  grabación y los códecs, en el tema 7; la cámara lenta y el *time lapse*, en el tema 15.

## Trazabilidad

Todas las fuentes se leyeron el 24/09/2026.

| Fuente | Qué sostiene |
|---|---|
| EBU R 103 v3.0 (mayo de 2020), anexos 1 y 2, tabla 1 | Márgenes nominal, preferente y total; error de gama; recortadores en directo; 0-700 mV |
| EBU R 118 v2 (abril de 2017), § 1.2, 1.3, 3.1.2-3.1.5, tablas 2 y 6 | Niveles de cámara, tamaños de sensor, criterios, tamaño de píxel, relación señal/ruido, ganancia negativa, sensibilidad, latitud, resolución, aliasing |
| EBU Tech 3335 (agosto de 2014), § 2.9 y 4.4 | Obturador de persiana, obturación nominal, margen sobre blanco, margen dinámico y ruido, medida con curva logarítmica |
| Sony, *PXW-Z200/HXR-NX800 Help Guide*, 5-060-574-13(1), 2024 | Sensor, zoom y diafragma, estabilizador, foco manual, tiraje automático, lupa, autofoco, diafragma, ganancia, obturación, parpadeo, ND, balance de blancos, cebra, monitor de señal, píxeles blancos, aspectos base |
| Sony, *PXW-FS5/FS5K Operating Guide*, 4-581-849-11(1) | Realce de contornos, lupa, detección de caras, cebra, ND |
| Blackmagic Design, *URSA Broadcast G2 Installation and Operation Manual*, noviembre de 2021 | Realce de contornos, cebra, falso color, parpadeo, cadencia y luz |
| Canon, *XF605 Instruction Manual*, PUB. DIE-0559-000B (especificaciones) | Sensor, zoom, autofoco, ganancia e ISO, sensibilidad, ND, preajustes de balance, estabilizador |
| Fujifilm North America, nota de producto FUJINON UA22x4.8BERD, 18 de marzo de 2026 | Ejemplo de referencia de objetivo de 2/3 de pulgada (4,8-106 mm, 22x) |

**Oficio sin norma detrás**, y así se declara: las familias de cámara y el reparto de tareas con el
control de imagen; la cadena del fotón al número; la comparación entre CCD y CMOS y la máscara de
Bayer; la definición de focal, ángulo, número f, profundidad de campo, círculo de confusión,
hiperfocal y aberraciones; la lectura de la referencia de un objetivo; el procedimiento manual de
ajuste de tiraje; el orden de los mandos de exposición; el *knee*; la curva logarítmica y la LUT;
la definición de balance de blancos y sus tres caminos; la equivalencia entre decibelios y pasos,
que es además una cuenta (20 · log₁₀ 2 ≈ 6); los circuitos de sombras; y el uso de los filtros
delanteros y de la bandera francesa.
