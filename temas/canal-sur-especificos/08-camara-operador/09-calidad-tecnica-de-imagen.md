# Tema 9 del específico de Cámara Operador · Calidad técnica de imagen

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Cámara Operador · punto 9 |
| **Sirve para** | Puesto 2.8, Cámara Operador (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Sin norma jurídica. Recomendaciones técnicas de la Unión Europea de Radiodifusión: EBU R 103 v3.0 (mayo de 2020), EBU R 118 v2 (abril de 2017), EBU Tech 3335 (agosto de 2014) y EBU Tech 3355 (marzo de 2017). Recomendaciones UIT-R BT.709-6 (06/2015), BT.2020-2 (10/2015) y BT.2100-3 (02/2025). Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía (1.ª ed., marzo de 2004). Documentación de fabricante: Sony, *PXW-Z200/HXR-NX800 Help Guide* (5-060-574-13(1), 2024) y *PXW-FS5/FS5K Operating Guide* (4-581-849-11(1)); Blackmagic Design, *URSA Broadcast G2 Installation and Operation Manual* (noviembre de 2021); Panasonic, *AVC-Intra Frequently Asked Questions*. Lo demás, oficio |
| **Redacción que se estudia** | Las ediciones de las recomendaciones vigentes el 24/09/2026 (R 103 en su versión 3.0; R 118 en su versión 2; BT.2100 en su edición 3) |
| **Extensión** | 10.000 palabras aproximadamente |

<!-- /portada -->

Siglas que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Europea de Radiodifusión (**EBU**,
*European Broadcasting Union*, que firma así sus recomendaciones); Sector de Radiocomunicaciones de
la Unión Internacional de Telecomunicaciones (**UIT-R**); unidad de control de cámara (**CCU**,
*camera control unit*) y su panel de control remoto (**RCP**, *remote control panel*); técnico de
imagen digital (**DIT**, *digital imaging technician*); dispositivo de acoplamiento de carga
(**CCD**) y semiconductor complementario de óxido metálico (**CMOS**); filtro óptico de paso bajo
(**OLPF**, *optical low-pass filter*); densidad neutra (**ND**, *neutral density*); alta definición
(**HD**) y ultra alta definición (**UHD**); rango dinámico estándar (**SDR**) y alto rango dinámico
(**HDR**), con sus dos curvas, la cuantificación perceptual (**PQ**, *perceptual quantizer*) y la
híbrida logarítmica-gamma (**HLG**, *hybrid log-gamma*); tabla de consulta (**LUT**, *look-up
table*); balance de blancos automático continuo (**ATW**, *auto tracing white*); relación
señal/ruido (**S/N**); grupo de imágenes (**GoP**, *group of pictures*) y su forma larga (***Long
GoP***); la norma de codificación de vídeo avanzada H.264 (**AVC**, *advanced video coding*);
índice de consistencia de iluminación para televisión (**TLCI**, *Television Lighting Consistency
Index*); decibelio (**dB**); megabits por segundo (**Mbit/s**); lux (**lx**); candela por metro
cuadrado (**cd/m²**); cuadros por segundo (**fps**); hercio (**Hz**); interfaz digital serie
(**SDI**) y pantalla de cristal líquido (**LCD**); la señal de ajuste del negro de los monitores
(**PLUGE**), que especifica la Recomendación UIT-R BT.814; los tres primarios rojo, verde y azul
(**RGB**) y la luminancia (**Y**).

Los rótulos de menú y de panel se escriben tal como los imprime el fabricante (***KNEE***,
***Detail***, ***Crispening***, ***Noise Suppression***, ***SteadyShot***, ***Flicker Reduce***…):
son rótulos de la máquina, no siglas, y cambian de una marca a otra.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.8, punto 9):
>
> Calidad técnica de imagen: foco, exposición, color, estabilidad, ruido, compresión y
> continuidad.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué criterios usa la EBU para clasificar una cámara por su calidad y qué
nivel admite para informativos; qué mide un monitor de forma de onda y qué un vectorscopio; por qué
se ajusta el tiraje y cómo; qué es el punto dulce de un objetivo y por qué se pierde nitidez con el
diafragma muy cerrado; qué es el *aliasing* y el *moiré*; entre qué valores de código debe quedar
una señal de 10 bits según la EBU y a qué límites se ajustan los recortadores en directo; qué hace
el *knee* y qué el levantado de negros; cuántos pasos de latitud pierde una cámara al subir 6 dB de
ruido; qué es el balance de blancos y hacia qué color vira la imagen si se balancea sobre una
superficie azul; qué distingue 4:2:2 de 4:2:0; qué es la estabilización pasiva y cuándo se apaga el
estabilizador; de dónde sale el parpadeo y qué obturación lo evita con red de 50 Hz; qué defecto
produce el obturador de persiana; qué parámetro de detalle limpia el ruido de las sombras; qué
diferencia hay entre compresión intracuadro y *Long GoP*; qué pide el Libro de estilo de Canal Sur
para el *raccord* técnico. En la prueba práctica: revisar y corregir una imagen defectuosa
(desenfocada, quemada, con dominante, temblorosa, ruidosa o con parpadeo) y dejar una cámara
preparada para que sus planos casen con los de otra.

<!-- indice -->

## Índice

- [La calidad técnica de imagen](#la-calidad-técnica-de-imagen)
  - [Qué se mide cuando se habla de calidad](#qué-se-mide-cuando-se-habla-de-calidad)
  - [Quién responde de ella](#quién-responde-de-ella)
  - [Los niveles de calidad de la EBU](#los-niveles-de-calidad-de-la-ebu)
  - [Los instrumentos de medida](#los-instrumentos-de-medida)
- [Foco](#foco)
  - [Qué hace nítida una imagen](#qué-hace-nítida-una-imagen)
  - [El punto dulce y la difracción](#el-punto-dulce-y-la-difracción)
  - [El ajuste de tiraje](#el-ajuste-de-tiraje)
  - [Las ayudas al enfoque](#las-ayudas-al-enfoque)
  - [Resolución, *aliasing* y *moiré*](#resolución-aliasing-y-moiré)
- [Exposición](#exposición)
  - [La exposición correcta y el orden de los mandos](#la-exposición-correcta-y-el-orden-de-los-mandos)
  - [Los límites de la señal según la EBU](#los-límites-de-la-señal-según-la-ebu)
  - [Las altas luces: el *knee*](#las-altas-luces-el-knee)
  - [Las sombras: los negros](#las-sombras-los-negros)
  - [El margen de exposición](#el-margen-de-exposición)
  - [Las ayudas a la exposición](#las-ayudas-a-la-exposición)
  - [La exposición en alto rango dinámico](#la-exposición-en-alto-rango-dinámico)
- [Color](#color)
  - [La colorimetría de referencia](#la-colorimetría-de-referencia)
  - [El balance de blancos](#el-balance-de-blancos)
  - [La matriz y la saturación](#la-matriz-y-la-saturación)
  - [La luz que la cámara no reproduce bien](#la-luz-que-la-cámara-no-reproduce-bien)
  - [Profundidad de bits y submuestreo](#profundidad-de-bits-y-submuestreo)
  - [Medir el color](#medir-el-color)
- [Estabilidad](#estabilidad)
  - [La imagen estable: el soporte](#la-imagen-estable-el-soporte)
  - [El estabilizador de la cámara](#el-estabilizador-de-la-cámara)
  - [El parpadeo](#el-parpadeo)
  - [El obturador de persiana](#el-obturador-de-persiana)
- [Ruido](#ruido)
  - [Qué es y de dónde sale](#qué-es-y-de-dónde-sale)
  - [Cómo se mide](#cómo-se-mide)
  - [El realce de detalle y el ruido](#el-realce-de-detalle-y-el-ruido)
  - [La reducción de ruido en cámara](#la-reducción-de-ruido-en-cámara)
- [Compresión](#compresión)
  - [Qué hace la compresión y qué se pierde](#qué-hace-la-compresión-y-qué-se-pierde)
  - [Intracuadro y *Long GoP*](#intracuadro-y-long-gop)
  - [Las tasas mínimas de la EBU](#las-tasas-mínimas-de-la-ebu)
  - [Lo que el operador hace por la compresión](#lo-que-el-operador-hace-por-la-compresión)
- [Continuidad](#continuidad)
  - [La continuidad técnica](#la-continuidad-técnica)
  - [La continuidad con una sola cámara](#la-continuidad-con-una-sola-cámara)
  - [La continuidad entre cámaras](#la-continuidad-entre-cámaras)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## La calidad técnica de imagen

### Qué se mide cuando se habla de calidad

La calidad técnica de una imagen no es una impresión: se mide. La EBU propone clasificar las cámaras
«**according to their technical specifications and their measured quality based on the results of
tests that are specified in EBU Tech 3335**» (R 118 v2), y fija cinco criterios de medida, a los que
suma el códec de grabación:

| Criterio (R 118) | Qué es |
|---|---|
| ***Noise*** | El ruido, medido como relación señal/ruido |
| ***Sensitivity*** | La sensibilidad: qué diafragma da el blanco de pico con una iluminación dada |
| ***Exposure Range*** | La latitud: cuántos pasos de luz caben entre el ruido y el recorte |
| ***Spatial Resolution*** | La resolución real, no el número de píxeles |
| ***Spatial Alias artefacts*** | Los defectos de solapamiento sobre texturas finas |
| ***Codec*** | La compresión con que graba la cámara, que sólo cuenta si graba a bordo |

La propia recomendación dice que «**Apart from spatial aliasing, each factor can be measured using
the procedures of EBU Tech 3335.**» Y avisa de que el códec puede estropear lo que el sensor ganó:
«**Although a camera can meet the requirements of a Tier, it may be let down (or even be downgraded
by the on-board codec.**» (sic: el paréntesis no se cierra en el original).

EBU Tech 3335 ordena la medida de una cámara en estos apartados: «**Opto-Electronic transfer curve
(Gamma)**», «**Noise levels and noise distribution**», «**Sensitivity**», «**Exposure range**»,
«**Colour rendering**», «**Infrared response**», «**Spatial resolution, detail settings &
aliasing**», «**Lens/optical effects**» y «**Temporal/shutter effects**».

El enunciado del tema recorre esa misma lista con palabras de operador: el foco es la resolución y
los efectos ópticos; la exposición, la curva y la latitud; el color, la reproducción cromática; la
estabilidad, los efectos temporales y del obturador; el ruido, el ruido; la compresión, el códec.
La continuidad es lo único que no se mide en una cámara sola: es que dos planos casen.

### Quién responde de ella

En una producción multicámara el ajuste de imagen no lo hace el operador: lo hace el control de
imagen, desde la unidad de control de cámara. El operador ejecuta lo que se le pide por la
intercomunicación, y para eso tiene que conocer el vocabulario (oficio).

| Puesto | De qué responde |
|---|---|
| Operador de cámara | El encuadre, el foco y el movimiento. Y ejecutar en la cámara lo que el control le pide |
| Control de imagen | Que todas las cámaras casen: nivel, color, sombras, altas luces, detalle |
| Técnico de imagen digital | En producciones de un solo sistema: configuración, calidad, calibración y gestión de ficheros |

En reportaje el operador es también el control de imagen, y hace los ajustes él mismo en el menú.
En multicámara los hace otro, y el operador sólo tiene que entender la orden (oficio). Desde el
panel remoto se gobierna lo que altera la señal —diafragma, color, obturación, nivel de negro,
ganancia—; por las manos del operador pasa lo que altera el encuadre —zoom, foco, movimiento—.

El Libro de estilo de Canal Sur sitúa la responsabilidad última en la realización: el realizador
«**es responsable máximo de la corrección de la imagen y de la calidad de la emisión del
programa**» (6.5, p. 92). Y, cuando no hay realizador, la pone en el cámara: «**En el caso,
habitual en el trabajo diario, de que no haya un realizador, el criterio del cámara es
imprescindible para proponer soluciones a las dificultades técnicas o, simplemente, para aportar
ideas útiles para el discurso periodístico.**» (5.1, p. 79).

### Los niveles de calidad de la EBU

EBU R 118 clasifica las cámaras por niveles (*Tiers*). Su finalidad: «**Knowing which quality Tier
a camera corresponds to will enable its targeting to programme genres and applications [...] and,
in the case of News, to balance speed of delivery against quality.**» Parte de un supuesto: «**these
guidelines assume Standard Dynamic Range production. The broadcaster must be consulted if High
Dynamic Range (as described in ITU-R BT.2100) images are required**».

| Nivel HD (R 118) | Texto de la recomendación |
|---|---|
| HD Tier 1 | «**Shoulder mounted or handheld single or 3 sensor professional cameras**» |
| HD Tier 2L | «**(Long-form) professional cameras**» |
| HD Tier 2J | «**(Journalism) professional cameras**» |
| HD Tier 3 | «**Small, high quality semi-professional for production use**» |
| HD Tier 4 | «**Small consumer HD cameras (broadcaster approval required before use)**» |
| Tier SP | «**Specialist or special effects cameras (broadcaster approval required before use)**» |

En UHD hay niveles propios: UHD1 Tier 1 (3840 × 2160), UHD1 Tier 2 (desde 2715 × 1527), UHD2 Tier 1
(7680 × 4320) y UHD2 Tier 2 (desde 5430 × 3054).

Tres datos que sirven al operador de informativos:

- El nivel de periodismo es una rebaja consciente: 2J supone «**a relaxation of some of the criteria
  to take account of the balance between speed to air and quality that News programmes may have to
  make**».
- El material de nivel 3 se raciona: «**Broadcasters will usually limit the amount of Tier 3
  material allowed in an HD programme to around 33%**».
- HD Tier 1 pide «**10-bit**» y «**4:2:2**»; HD Tier 2L y 2J, «**8-bit (10-bit preferred)**».

### Los instrumentos de medida

La calidad se comprueba con instrumentos, no a ojo (oficio). Los tres que un operador encuentra en
el visor o en el monitor de campo:

| Instrumento | Qué mide | Qué se ve en él |
|---|---|---|
| Monitor de forma de onda | La luminancia, línea a línea | Un perfil del brillo, con el pedestal de negros abajo y el blanco arriba |
| Vectorscopio | La crominancia: tono y saturación | Un diagrama polar con las cajas de los seis colores de barras |
| Histograma | El reparto estadístico de los niveles | Cuántos píxeles hay en cada nivel |

La regla que separa los dos primeros: la forma de onda dice si la exposición está bien; el
vectorscopio dice si el color está bien. Son dos preguntas distintas y hacen falta los dos (oficio).
Las cámaras de reportaje los llevan dentro: la Sony PXW-Z200 permite ver en el visor «**waveform,
vectorscope, or histogram**», y en la forma de onda «**The orange line indicates the set value of
the zebra level.**»

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

## Foco

### Qué hace nítida una imagen

Una imagen está enfocada cuando el plano de nitidez cae sobre lo que importa. Pero la nitidez de un
plano no depende sólo del anillo de foco: dependen de ella el objetivo, el diafragma, el ajuste de
tiraje, el sensor y el realce electrónico (oficio). Los defectos que siguen son los que un operador
tiene que saber reconocer.

Las aberraciones son defectos de formación de la imagen que un sistema óptico introduce, y no se
corrigen enfocando: son propias del diseño y de los materiales del objetivo (oficio). Las cinco
aberraciones básicas de Seidel son la esférica, el coma, el astigmatismo, la curvatura de campo y la
distorsión:

| Aberración | Qué hace |
|---|---|
| Esférica | Los rayos que pasan por el borde de la lente enfocan en un punto distinto que los del centro: la imagen pierde nitidez por igual en todo el cuadro |
| Coma | Un punto fuera del eje se dibuja como una coma o un cometa, con una cola apuntando hacia fuera |
| Astigmatismo | Las líneas radiales y las tangenciales no enfocan a la vez |
| Curvatura de campo | La imagen nítida se forma sobre una superficie curva y el sensor es plano: si se enfoca el centro, los bordes salen blandos |
| Distorsión | Las líneas rectas salen curvadas: de barril hacia fuera, o de corsé hacia dentro |

Las cinco de Seidel son monocromáticas —aparecen incluso con luz de un solo color—, y la aberración
cromática es aparte: viene de que el índice de refracción depende de la longitud de onda (oficio).

### El punto dulce y la difracción

El punto dulce es donde el trabajo de la óptica es óptimo, reduciendo aberraciones y proporcionando
una mayor definición, y se encuentra en las aperturas de diafragma intermedias (oficio). Dos
defectos tiran en direcciones contrarias:

| Extremo de la escala | Qué degrada la imagen |
|---|---|
| Abertura máxima —f/1,4, f/2— | Las aberraciones: a plena abertura la lente trabaja con todo su vidrio, defectos incluidos |
| Abertura mínima —f/16, f/22— | La difracción: al estrecharse mucho el paso, la luz se dispersa en el borde del iris y el detalle se emborrona. Este defecto no depende de la calidad de la lente: es física |
| Aberturas intermedias | El punto dulce: el diafragma ya ha tapado los bordes de la lente y todavía no es tan pequeño como para difractar |

Dónde cae en la práctica: unos dos o tres pasos por debajo de la abertura máxima. No es un valor
fijo: es una posición relativa dentro de la escala de cada objetivo (oficio).

El fabricante lo dice para la cámara de reportaje, y da el remedio: «**When shooting a bright
subject, diffraction (a common phenomenon in video cameras, caused by closing the iris too much) may
result in poor focusing. Using the ND FILTER dial A suppresses this phenomenon for better shooting
images.**» (Sony, PXW-FS5 Operating Guide). Es decir: con mucha luz no se cierra el diafragma hasta
el final; se mete densidad neutra y se deja el diafragma en su zona buena. El mismo manual avisa de
que no se cambie el filtro en plena toma: «**If you switch ND FILTER dial A during recording, the
image or sound may become distorted.**»

### El ajuste de tiraje

El ajuste de tiraje (*back focus*) es el ajuste de la distancia entre el plano de la montura del
objetivo y el plano del sensor. Si esa distancia no es exactamente la que el objetivo espera, el
enfoque no se mantiene al recorrer el zoom (oficio). Es el defecto de foco más típico de un zoom de
televisión: la imagen enfocada en tele se ablanda al abrir al angular.

Cuándo hay que hacerlo: cada vez que se cambia de objetivo o de cuerpo, cuando el equipo ha sufrido
un golpe y cuando hay un cambio grande de temperatura, porque los metales se dilatan (oficio).

El método, paso a paso (oficio):

1. Se va al tele sobre un punto o una carta alejados, con el diafragma abierto, y se enfoca ahí,
   porque en el tele la profundidad de campo es mínima: es donde el error de foco se ve.
2. Se va al angular sin tocar el foco. Si el tiraje está mal, la imagen se desenfoca al llegar al
   angular.
3. Se corrige con el anillo de tiraje, no con el de foco.
4. Se recorre el zoom entero comprobando que el enfoque se mantiene.

La regla que lo resume: se enfoca en el tele y se ajusta el tiraje en el angular, sobre un punto
lejano y con el diafragma abierto, para que la profundidad de campo no disimule el error.

### Las ayudas al enfoque

En un visor pequeño el foco engaña, y las cámaras traen dos ayudas. El realce de contornos
(*peaking*): «**You can display an image on the LCD screen with its outlines enhanced. This function
helps you to adjust the focus.**» Y la lupa: «**The selected area on the LCD screen is magnified and
displayed. This is useful when adjusting the focus.**» (Sony, PXW-FS5 Operating Guide). Ninguna de
las dos llega a la grabación: «**The enhanced outlines will not be recorded on the memory card.**» y
«**Even though the image appears expanded on the LCD screen, the recorded image is not
expanded.**» El mismo manual aconseja combinarlas: «**You can focus more easily using this function
in combination with the focus magnifier function**».

El nivel de realce hay que adaptarlo al plano: «**The optimum level of focus assistance varies shot
by shot. When focusing on actors, for example, a higher level of focus assistance can help resolve
edge detail in faces. A shot of foliage or brickwork, on the other hand, may show distracting
amounts of focus information at higher settings.**» (Blackmagic, URSA Broadcast G2).

El autofoco con detección de caras ayuda en la cobertura rápida, pero tiene límites que el
fabricante declara: «**Faces may not be detected depending on the recording environment, the
condition of the subject or the settings.**» (Sony, PXW-FS5). Un foco que salta al fondo cuando la
persona gira la cabeza es un plano inservible (oficio).

### Resolución, *aliasing* y *moiré*

Más píxeles no es más nitidez. La EBU lo dice sin rodeos: «**The sensor pixel count is not an
acceptable measure of a camera’s actual resolution.**» (R 118 v2, § 3.1.4). La resolución real se
mide con cartas, como manda Tech 3335.

El solapamiento (*aliasing*) aparece cuando el sujeto tiene un detalle más fino del que el sensor
puede muestrear: surge una frecuencia más baja que no estaba en la escena (oficio). La EBU destaca
dos consecuencias: «**Aliasing is also highly distracting in a finished programme as it tends to
move in the opposite direction to the movement of the camera**» y «**Aliasing causes
motion-dependent video compression to fail in the extreme**» (R 118 v2, § 3.1.5). Una panorámica
sobre una fachada de ladrillo o una persiana es el caso típico.

Su forma más visible es el *moiré*: un dibujo de ondas o de colores falsos sobre una trama fina —una
corbata de rayas, una rejilla—, que nace de la interferencia entre la trama del sujeto y la del
sensor y se combate con el filtro óptico de paso bajo, el OLPF (oficio). En la toma, el operador lo
evita cambiando la focal o la distancia, que cambian el tamaño de la trama en el sensor (oficio).

Junto a ellos, dos defectos de sensor que se distinguen a simple vista (oficio):

| Defecto | Qué se ve | Por qué ocurre |
|---|---|---|
| *Blooming* | Un halo o una mancha alrededor de una zona muy iluminada, que se come el detalle | Un fotodiodo saturado desborda su carga hacia los vecinos |
| *Smear* | Una raya vertical luminosa que atraviesa la imagen de arriba abajo desde una fuente muy brillante | La carga se cuela en el registro de transferencia vertical del CCD |

*Blooming* es contaminación entre vecinos —se extiende en todas direcciones—; *smear* es
contaminación por el camino de lectura —se extiende sólo en vertical—, y es propio de los CCD.

## Exposición

### La exposición correcta y el orden de los mandos

Una imagen está bien expuesta cuando lo importante cae en la zona de la curva donde hay detalle: ni
las luces recortadas ni las sombras hundidas en el ruido (oficio). Cuatro mandos la gobiernan: el
diafragma, la obturación, el filtro de densidad neutra y la ganancia. No son intercambiables, porque
cada uno tiene un precio: el diafragma cambia la profundidad de campo; la obturación, la nitidez del
movimiento y el parpadeo; el filtro sólo quita luz; la ganancia añade ruido.

La ganancia es el último recurso, no el primero. El orden correcto es: abrir el diafragma, bajar la
obturación si el movimiento lo permite, añadir luz y, sólo entonces, subir ganancia. Cada paso de
ganancia es un paso de ruido, y el ruido de una toma no se quita después (oficio).

La cadencia también cuenta: «**if you switch from 25 to 50 frames per second, the amount of light
reaching the sensor will be halved. To maintain your exposure you need to compensate for this change
by opening up your lens an extra stop, by opening up your shutter angle from 180º to 360º or by
adding some extra lighting**» (Blackmagic, URSA Broadcast G2).

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

- Recortar mal es peor que no recortar: el recorte «**can cause harmonic distortion and alias
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

### Las altas luces: el *knee*

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

En una cámara de reportaje actual esos ajustes están en el menú de pintura. En la Sony PXW-Z200,
[Knee] tiene [Setting] y [Auto Knee] activados de fábrica en SDR, un punto regulable «**75% to
109%**» con valor de fábrica «**90%**» y una pendiente de «**−99 to +99**».

El *knee* no cambia la sensibilidad —reparte de otra manera lo que ya se captó— ni oscurece la
imagen: conserva información en las luces (oficio). Es lo que permite, en un exterior con cielo, que
el cielo conserve algo de nube mientras el rostro está bien expuesto.

### Las sombras: los negros

Dos circuitos distintos actúan sobre las zonas oscuras de la imagen, y confundirlos es el error
clásico (oficio):

| Circuito | Sobre qué actúa | Qué hace | ¿Bidireccional? |
|---|---|---|---|
| Levantado de negros (*black stretch*) | La señal de luminancia (Y) | Sólo levanta las zonas de sombra | No: sólo en un sentido |
| Gamma de negros (*black gamma*) | Los tres canales RGB | Levanta o comprime la parte baja de la curva | Sí |

Levantar los negros abre las sombras y deja ver lo que hay en ellas, a cambio de perder contraste y
hacer visible el ruido que en negro no se veía. Y por eso sólo levanta: comprimir los negros por
debajo del nivel de negro no tiene sentido, porque no hay nada por debajo del negro (oficio).

A esos dos se suma el nivel de negro, el pedestal sobre el que se apoya toda la curva. En la Sony
PXW-Z200 el menú [Black] regula «**[Master Black]**», «**[R Black]**» y «**[B Black]**», de
«**−99.0 to +99.0**».

El mapa que ordena todo: el levantado y la gamma de negros trabajan en la parte baja de la curva; el
*knee* en la parte alta; y el realce de detalle sobre los bordes de toda ella (oficio).

### El margen de exposición

La latitud de una cámara tiene dos límites: «**It is limited at the low end by noise levels, and at
the high end by the clipping level.**» (R 118 v2, § 3.1.3). Tech 3335 lo formula como dos
parámetros: «**the maximum exposure level (Lmax) [...] and the noise level which defines the minimum
exposure level (Lmin)**». Por encima del blanco de referencia queda un margen: «**This ‘headroom’
varies in cameras between about 1 stop and 3 stops.**»

Las cifras de Tech 3335 (§ 4.4):

- «**A typical broadcast camera with video noise levels of about -50dB can capture about 7.5 stops,
  with the controls set to factory settings.**»
- «**the effective dynamic range will be reduced by about 1 stop per 6dB of video noise level
  increase.**»
- «**most cameras [...] can be set to capture at least 1 extra photographic stop by manipulation of
  the gamma curve and/or knee. In some extreme cases, cameras can capture up to 3 extra stops, and
  effectively handle 12 to 13 stops**».

La consecuencia práctica: subir ganancia no sólo ensucia la imagen; también estrecha la latitud,
porque sube el suelo de ruido (se deduce de la segunda cita).

### Las ayudas a la exposición

La cebra marca en el visor las zonas que pasan de un nivel: «**The zebra pattern is a stripe pattern
that appears in areas of brightness equal to or exceeding the brightness level you have set.**»; su
nivel se elige «**70 to 100, or 100+**», y «**Zebra is not recorded onto the memory card.**» (Sony,
PXW-FS5). Con la cebra a 100 %, «**shows which areas are completely overexposed**»; y «**If you’re
shooting in variable light such as outdoors on a partly overcast day, setting your zebra level lower
than 100 can warn you of potential overexposure.**» (Blackmagic, URSA Broadcast G2).

El falso color pinta cada zona según su nivel: «**when elements in your image change from yellow to
red, that means they are now over exposed.**» (Blackmagic). Sus colores no están normalizados: cada
fabricante tiene su escala.

### La exposición en alto rango dinámico

La Recomendación UIT-R BT.2100-3 fija para el HDR dos curvas: «**the Perceptual Quantization (PQ)
or Hybrid Log-Gamma (HLG) specifications described in this Recommendation should be used**». La HLG
es la que mejor convive con lo que ya existe: «**The HLG specification offers a degree of
compatibility with legacy displays by more closely matching the previously established television
transfer curves.**»

La referencia de exposición en HDR es el blanco de referencia: «**HDR Reference White is the
nominal signal level obtained from an HDR camera and a 100% reflectance white card resulting in a
nominal luminance of 203 cd/m2 on a PQ display or on an HLG display that has a nominal peak
luminance capability of 1 000 cd/m2.**» (BT.2100-3, nota 10a). El nivel de señal HLG que corresponde
a ese blanco, expresado en porcentaje, está en el Informe UIT-R BT.2408, que este tema no da.

En el visor, las cámaras ofrecen una ayuda: con salida HLG, la Sony PXW-Z200 puede mostrar una
conversión sencilla a SDR para trabajar «**with the same feeling as conventional SDR**».

## Color

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
error en el canal azul se note mucho menos que el mismo error en el verde, y de que el ruido suela
verse antes en el azul (oficio).

La BT.709-6 recuerda que el aspecto final se juzga en un monitor de referencia: «**In typical
production practice the encoding function of image sources is adjusted so that the final picture has
the desired look, as viewed on a reference monitor having the reference decoding function of
Recommendation ITU-R BT.1886**».

### El balance de blancos

El balance de blancos es el ajuste de la temperatura de color de los sensores de la cámara a la
existente en la escena. La cámara mide una superficie que se le presenta como blanca y ajusta la
ganancia relativa de los canales rojo y azul hasta que los tres canales dan el mismo valor. A partir
de ahí, lo que era blanco en la escena sale blanco en la señal, y todo lo demás cae en su sitio
(oficio).

Los tres caminos para hacerlo (oficio):

| Camino | Cuándo |
|---|---|
| Balance automático sobre una carta blanca | Siempre que haya tiempo: es el fiable |
| Preajuste de 3.200 K o 5.600 K | Cuando no hay tiempo y se sabe qué luz hay |
| Balance automático continuo | Cuando la luz cambia sin control, a cambio de que los tonos deriven en plano |

La cámara empuja la imagen hacia el color complementario del de la superficie sobre la que se
balancea (oficio). Si se balancea sobre un vaquero azul claro, la cámara recibe de él mucho más azul
que rojo; como tiene orden de verlo blanco, baja la ganancia del azul y sube la del rojo, y ese
ajuste se aplica a toda la imagen, que sale más cálida.

| Superficie de balance | Cómo sale la imagen |
|---|---|
| Blanco o gris neutro | Neutra: es el uso normal |
| Azul | Cálida |
| Naranja o ámbar | Fría |
| Verde | Magenta |

Es el error típico de balancear sobre la camisa de color del entrevistado en lugar de sobre una carta
blanca, y también un recurso deliberado para forzar una dominante (oficio).

El balance de negros es su pareja en la parte baja: iguala los tres canales en el negro para que las
sombras no tengan dominante. En las cámaras de reportaje se regula con el negro de cada canal —[R
Black] y [B Black] en la Sony PXW-Z200— y en las de estudio lo hace el control de imagen (oficio).

### La matriz y la saturación

Pintar la cámara es ajustar su color más allá del balance: saturación, tono y reproducción de cada
color (oficio). La Sony PXW-Z200 tiene dos niveles de ajuste. La matriz de usuario actúa sobre toda
la imagen: [User Matrix Level] «**Adjusts the color intensity of the entire image.**» y [User Matrix
Phase] «**Adjusts the color tone of the entire image.**» La matriz múltiple actúa por colores:
«**Multi matrix correction adjusts the hue and saturation for each color axis, with the total hue
subdivided into 16.**»

Los ajustes de imagen se guardan y se recuperan: la misma cámara permite guardar «**the current
image quality state as a scene file in internal memory**», pasarlo a una tarjeta y cargarlo desde
ella. Llevar ese archivo a otra cámara del mismo modelo es la herramienta de la continuidad entre
cámaras de reportaje (oficio; véase «Continuidad»).

### La luz que la cámara no reproduce bien

Una cámara bien balanceada reproduce mal el color si la fuente de luz tiene un espectro pobre. Para
medirlo la EBU creó el TLCI (EBU Tech 3355). El valor 50 marca la frontera: «**The formulation for
Qa was constrained to produce a value of 50 for a typical daylight fluorescent tube, and this number
appears to represent the watershed separating luminaires into those which are correctable for
television use, and those which are not.**» Por debajo de ese valor, el color no se arregla con el
balance (el tema 5 trata la iluminación).

### Profundidad de bits y submuestreo

La profundidad de bits es con cuántos niveles se anota cada muestra de la señal: ocho bits dan 256
niveles por canal, diez bits dan 1.024 y doce bits dan 4.096 (cálculo: 2 elevado al número de bits).

Con más bits hay más niveles de brillo, más colores posibles, degradados más suaves y archivos más
pesados. El defecto que evita es el bandeado (*banding*): escalones visibles en un degradado suave,
como un cielo o una pared lisa. La profundidad de bits no crea rango dinámico —ése lo determina el
sensor—, pero lo hace utilizable: al codificar un rango amplio con pocos bits, los escalones se
hacen tan grandes que el rango deja de ser aprovechable (oficio).

El submuestreo cromático reduce la resolución de los componentes de la crominancia para disminuir el
tamaño de los archivos sin una pérdida significativa de calidad. Funciona porque el ojo distingue
mucho mejor los detalles de brillo que los de color (oficio).

| Notación | Qué guarda | Dónde se usa |
|---|---|---|
| 4:4:4 | Una muestra de color por píxel: sin submuestreo | Grafismo, croma, cine |
| 4:2:2 | La mitad de muestras de color en horizontal | El estándar de producción de televisión |
| 4:2:0 | La mitad en horizontal y la mitad en vertical | Emisión y distribución |

El submuestreo limita lo que se puede hacer después: un croma sobre material 4:2:0 recorta mal,
porque el borde del recorte se calcula sobre información de color que no está. Por eso el material
destinado a incrustación se graba en 4:2:2 como mínimo, y mejor en 4:4:4 (oficio). La EBU pide
4:2:2 y 10 bits a la cámara de nivel 1 (véase «Los niveles de calidad de la EBU»).

### Medir el color

El vectorscopio es el instrumento del color: el ángulo alrededor del centro es el tono y la distancia
al centro es la saturación. El centro es la ausencia de color, así que una imagen en blanco y negro
se ve como un punto en el centro y una imagen con dominante se ve como un punto desplazado hacia el
color de la dominante (oficio). Una carta blanca bien balanceada queda en el centro; si se aparta,
el balance está mal.

## Estabilidad

### La imagen estable: el soporte

La estabilidad tiene dos caras: que el encuadre no tiemble y que la imagen no parpadee ni se deforme
en el tiempo (oficio). La primera empieza por el soporte. El Libro de estilo de Canal Sur lo fija
como norma de la casa: «**En circunstancias normales, la cámara se instalará sobre el trípode para
conseguir una imagen estable y de calidad, pero no hay que descartar su manejo al hombro aun cuando
el foco de atención sea estático, sobre todo para captar recursos en una rueda de prensa o en una
entrevista.**» (5.2, p. 80).

Cuando no hay trípode, la estabilización puede ser pasiva o activa (oficio):

| Familia | Con qué lo consigue | Ejemplos |
|---|---|---|
| Pasiva | Sólo medios mecánicos: masa, inercia, contrapesos, cardanes libres, brazos con muelles | La steadicam clásica, los brazos articulados con resorte, los cardanes sin motor |
| Activa | Motores y electrónica: sensores que miden el movimiento y motores que lo corrigen | Los gimbals motorizados de tres ejes, los giroestabilizados de helicóptero, la estabilización óptica de la lente |

La estabilización pasiva es la capacidad de mantener fija la orientación de la cámara a través de los
medios mecánicos de un soporte. Las fricciones de una cabeza fluida no estabilizan: amortiguan.
Amortiguar es suavizar un movimiento; estabilizar es cancelarlo (oficio). Los soportes se tratan en
el tema 4.

La regla de oficio para la toma sin soporte: cuanto más tele, más se nota el temblor, porque la
focal larga amplía el movimiento igual que amplía el sujeto. Al hombro se trabaja en angular y se
acerca uno al sujeto en lugar de cerrar el zoom.

### El estabilizador de la cámara

La Sony PXW-Z200 describe sus modos: «**[Standard]: Reduces blurring of captured images caused by
camera shake.**» y «**[Active]: Applies more powerful correction than [Standard] for correcting
stronger camera shake, such as shooting while walking.**» El modo activo tiene un coste: «**The
framing shifts slightly to the telephoto side.**»

Y la regla que más se olvida: el estabilizador se apaga en trípode. «**When shooting using a tripod
for stability, set image stabilization to [Off]. If you perform slow pan/tilt movements with image
stabilization set to [Standard] or [Active], the image may become distorted.**» El mismo manual
añade que «**Slow pan/tilt movements may also cause the image to become distorted when shooting
handheld. If this occurs, try adjusting the image stabilization setting.**»

### El parpadeo

El parpadeo (*flicker*) es la inestabilidad de brillo o de color de un cuadro al siguiente. Nace de
la iluminación: «**If shooting under lighting produced by fluorescent lights, sodium lamps,
mercury-vapor lamps, or LEDs, the screen may flicker or colors may vary.**» (Sony, PXW-Z200). La
luz alimentada por la red varía con su frecuencia, y si la obturación no casa con ella, cada cuadro
recoge una cantidad distinta de luz (oficio). La UIT-R lo tiene en cuenta al elegir cadencia: «**The
choice of frame frequency may be influenced by the frequency of the mains power and the type of
scene lighting in use**» (BT.2020-2).

Lo peligroso es que no siempre se ve en el visor: «**Artificial light sources such as tungsten,
fluorescent and LED may introduce some flicker to your images. You may not see these flicker issues
when previewing the scene on your LCD and SDI feed or while recording, so it’s important to perform
a test shoot with the lights you plan to use**», y «**Your shutter setting can also affect the
visibility of flicker when shooting under lights**» (Blackmagic, URSA Broadcast G2).

Cómo se evita:

- Con la obturación: la nominal es «**1/50 second for 50 Hz, 1/60 for 59.94 Hz, or 180 degrees
  for either**» (EBU Tech 3335). Con la red europea de 50 Hz, una obturación de 1/50 o de 1/100
  recoge ciclos enteros de luz y evita el parpadeo (oficio).
- Con la corrección de la cámara: la Sony PXW-Z200 tiene [Flicker Reduce], con modo «**[Auto] /
  [On] / [Off]**» (de fábrica, [Off]) y una frecuencia «**[50Hz] / [60Hz]**» que hay que poner a la
  de la red que alimenta la luz: el valor de fábrica es [60Hz], así que en España hay que cambiarlo.
- Con pantallas en cuadro (monitores, marcadores, pantallas LED) se ajusta la obturación fina hasta
  que la banda desaparece del visor (oficio).

### El obturador de persiana

Los sensores CMOS no leen toda la imagen a la vez, sino por líneas, y eso produce deformaciones con
el movimiento rápido: «**Cameras with CCD sensors usually exhibit no odd temporal effects, but
cameras with one or more CMOS sensor can produce visible effects from the use of a ‘rolling
shutter’. The effect is identical to that seen in focal plane film stills cameras; leaning
verticals, distorted edges, and jelly-like images from rapid motion.**» (EBU Tech 3335, § 2.9).

En la toma se nota en las panorámicas rápidas —los edificios se inclinan— y en la cámara que vibra
—la imagen ondula como gelatina—. Se reduce moviendo la cámara más despacio y fijándola mejor
(oficio).

## Ruido

### Qué es y de dónde sale

El ruido es la variación aleatoria de la señal que no viene de la escena: el grano que se mueve sobre
las zonas lisas y oscuras (oficio). Su causa principal en la operación es la ganancia: una
amplificación electrónica de la señal que ya ha salido del sensor. La imagen se ve más clara, pero no
hay más luz: la ganancia multiplica lo que el sensor entregó, y el sensor entrega dos cosas
mezcladas, señal y ruido. Al multiplicar, se multiplican las dos, y como la señal ya estaba escasa
—por eso se sube la ganancia— lo que se nota es el ruido (oficio).

La equivalencia que hay que saber hacer: un paso de diafragma duplica la luz; en decibelios de
tensión, duplicar es +6 dB, porque 20 por el logaritmo decimal de 2 es aproximadamente 6 (cálculo).

| Ganancia | Pasos de diafragma | Precio en ruido |
|---|---|---|
| +3 dB | Medio paso | Poco |
| +6 dB | 1 paso | Apreciable |
| +12 dB | 2 pasos | Mucho |
| +18 dB | 3 pasos | La imagen ya es ruidosa |

Los sensores tienen además un defecto propio que la ganancia agrava: los puntos blancos. «**fine
white flecks may be generated on the screen in rare cases, caused by cosmic rays, etc.**», que se
ven sobre todo «**When operating at a high environmental temperature**» y «**When you have raised
the gain (sensitivity)**» (Sony, PXW-Z200).

### Cómo se mide

El ruido se mide como relación señal/ruido, en decibelios. EBU R 118 fija mínimos por nivel (tabla
6): HD Tier 1, «**Better than -48 dB @ 0db gain**»; HD Tier 2L, «**Better than -44 dB**»; HD Tier
2J y Tier 3, «**Better than -40 dB**». Y añade que la cifra no lo es todo: «**Noise should be rated
by its impact and visibility as well as by measurement.**»

La ganancia también puede bajar: «**Some camera menus allow negative gain settings (with respect to
the published 0 dB). It is therefore possible to improve the S/N ratio using a negative (lower) gain
setting.**» (R 118 v2).

### El realce de detalle y el ruido

El realce de detalle es un circuito que aumenta el contraste local en los bordes para que la imagen
se perciba más nítida. Su problema es que también realza el ruido, y de ahí salen sus controles
(oficio):

| Control | Qué hace |
|---|---|
| Nivel de detalle | Cuánto realce se aplica |
| Frecuencia | En qué banda de detalle actúa: bordes finos o gruesos |
| Dependencia del nivel (*level depend*) | Reduce o suprime el realce en las zonas oscuras, donde el ruido es peor |
| Recorte (*crispening*) | Ignora las diferencias pequeñas, que suelen ser ruido |

En una imagen diafragmada correctamente en la que hay una zona oscura y ruidosa, el parámetro que
ayuda a limpiar ese ruido es la dependencia del nivel: el ruido de una imagen bien expuesta está
sobre todo en las sombras, el realce de detalle lo amplifica ahí más que en ningún sitio, y la
dependencia del nivel apaga el realce en la parte baja de la escala, mientras el detalle de las
zonas bien iluminadas se mantiene. Levantar los negros hace lo contrario: sube el ruido con ellos
(oficio).

En la Sony PXW-Z200 el menú [Detail] regula el nivel «**−7 to +7**», el reparto entre bajas y altas
luces ([B/W Balance]: «**Sets the balance between detail for low-luminance areas (Black) and detail
for high-luminance areas (White)**»), el límite y el [Crispening], «**0 to 7**».

Cuánto detalle es demasiado es cuestión de estilo, pero con un límite: «**Moderate overshooting on
high-contrast edges is acceptable, it is a signature of the ‘videolook’**» (EBU Tech 3335, § 4).
Un realce excesivo dibuja un contorno blanco alrededor de los bordes y hace más visible el ruido
(oficio).

### La reducción de ruido en cámara

Las cámaras actuales traen un filtro de ruido. En la Sony PXW-Z200, [Noise Suppression] se activa o
se desactiva y tiene tres niveles, «**[Low] / [Mid] / [High]**», con [On] y [Mid] de fábrica en el
modo de rodaje personalizado. Un filtro fuerte suaviza también el detalle fino (oficio).

La regla de oficio: el ruido de las sombras no se arregla iluminando la imagen desde el menú. Se
arregla iluminando la escena, o quitándole realce a esa parte de la escala.

## Compresión

### Qué hace la compresión y qué se pierde

Casi todo lo que graba una cámara de televisión está comprimido. La transformada discreta del coseno
es la operación matemática sobre la que se construye la mayor parte de la compresión de imagen y de
vídeo. Convierte un bloque de píxeles en un conjunto de coeficientes que describen ese bloque como
suma de patrones de frecuencia, de los más suaves a los más finos. No comprime nada por sí misma:
reorganiza la información de manera que la parte importante quede concentrada en unos pocos
coeficientes (oficio).

La compresión viene después, en la recuantificación: los coeficientes se recuantifican
individualmente, de manera que se puede desechar información de altas frecuencias y comprimir la
señal según el flujo de datos manteniendo la información fundamental. Se desecha el detalle muy fino
porque el ojo lo distingue mal. La recuantificación es precisamente lo que introduce la pérdida
(oficio).

De ahí salen los defectos de compresión que el operador ve en el material (oficio): bloques en las
zonas lisas y en los degradados, contornos sucios alrededor de los bordes, detalle fino que
desaparece o que «hierve» de un cuadro al siguiente. Aparecen cuando la imagen pide más datos de los
que el flujo permite.

### Intracuadro y *Long GoP*

La EBU distingue tres familias de códec de cámara (R 118 v2, § 1.3.1): el RAW, sin procesar;
«**Intra Frame (I-Frame). I-Frame codecs do not employ temporal compression, meaning each frame is
processed alone**»; e «**Inter Frame (Long GoP). Long GoP codecs offer most bit rate reduction for a
given quality by looking and processing across multiple frames**».

La diferencia se nota en el montaje y con el movimiento. Un fabricante lo explica así: «**By
contrast, Intra frame compression processes the entire image within the boundaries of each video
field or frame. There is zero interaction between adjacent frames, so its image quality stands up
well to motion and editing.**» Y del *Long GoP* dice: «**any image manipulation or processing will
severely degrade the image quality in long GOP compression schemes.**» (Panasonic, AVC-Intra
Frequently Asked Questions; es documentación comercial de quien vende el intracuadro, y así se lee).

La regla de oficio: el intracuadro gasta más datos y aguanta mejor el montaje, el movimiento y las
generaciones; el *Long GoP* ahorra más, y sufre con el movimiento rápido y con cada nueva
codificación.

### Las tasas mínimas de la EBU

EBU R 118 fija tasas mínimas por nivel de cámara (tabla 1, en Mbit/s, a 25 / 50 fps), y avisa de que
son mínimos: «**The bit rates given are the MINIMUM for general-purpose 10-bit Standard Dynamic Range
content**».

| Códec | Nivel | 25 fps | 50 fps |
|---|---|---|---|
| Intracuadro | HD 2L y superior | 100 | 200 |
| Intracuadro | HD 2J e inferior | 50 | 75 |
| H.264 (AVC), GoP variable | HD 2L y superior | 25 | 35 |

En UHD, el MPEG-2 figura como «**Not to be used**».

### Lo que el operador hace por la compresión

El códec no se elige en cada toma, pero el operador decide cuánto trabajo le da (se deduce de las
recomendaciones citadas):

- El *aliasing* rompe la compresión: «**Aliasing causes motion-dependent video compression to fail
  in the extreme**» (R 118 v2).
- El recorte mal hecho también: produce «**compression artefacts and the potential for increased
  data rates**» (R 103 v3.0).
- El ruido es detalle aleatorio que cambia en cada cuadro, y el códec lo trata como información que
  hay que codificar: una imagen ruidosa gasta flujo en ruido y deja menos para la imagen (oficio).
- El temblor y la panorámica rápida obligan al *Long GoP* a codificar mucho cambio entre cuadros
  (oficio).

Una imagen limpia, bien expuesta y estable es también una imagen que se comprime mejor (oficio). El
tema 7 trata los formatos, los códecs y los soportes de grabación.

## Continuidad

### La continuidad técnica

La continuidad técnica es que los planos de una misma pieza casen entre sí: el mismo color, el
mismo brillo, el mismo contraste, la misma calidad. El Libro de estilo de Canal Sur la pone en el
centro de la edición: «**La clave del equilibrio en la edición correcta está en un concepto
imprescindible: el ‘raccord’, esto es, la continuidad y uniformidad visual de los planos con sentido
lógico.**» Y su primer aspecto es el técnico: «**1. Técnico. No deben permitirse diferencias de
color, brillo, contraste, tono, luz, altura de planos, calidad de la imagen...**» (6.4, p. 92). Los
otros tres aspectos —físico, sonoro y cinético— y las clases de *raccord* del oficio se tratan en el
tema 2.

El Libro de estilo pide también armonía entre el material nuevo y el de archivo: «**Cada vídeo debe
montarse con imágenes y sonidos homogéneos. Hay que ser cuidadosos con la inclusión de recursos de
archivo por la distorsión técnica que suponen en un montaje con material de actualidad y por el
contraste de indumentaria o situación.**» (6.3.4, p. 91).

En informativos la continuidad se garantiza en la grabación, no en el montaje: el montador no puede
rehacer nada, y si el operador ha grabado la pregunta y la respuesta con luz o color distintos, el
corte se verá (oficio).

### La continuidad con una sola cámara

Lo que rompe la continuidad técnica entre planos de una misma cámara, y cómo se evita (oficio):

| Causa | Remedio |
|---|---|
| Balance automático continuo, que cambia el color a mitad de plano o entre planos | Balance fijo, en memoria, y se rehace cuando cambia la luz |
| Diafragma automático, que cambia el brillo cuando entra algo claro u oscuro en cuadro | Diafragma manual en la entrevista y en el plano fijo |
| Ganancia distinta entre planos | Misma ganancia en toda la pieza, para que el ruido no salte en el corte |
| Luz que cambia con la hora | Grabar seguidos el plano y el contraplano; si no, rebalancear y ajustar |
| Ajustes de imagen tocados en el menú y olvidados | Volver a un archivo de escena conocido |

El aviso de oficio: el balance automático continuo es el enemigo del montaje. Dos tomas de la misma
escena salen de distinto color, y el montador no puede casarlas. En reportaje se hace balance fijo y
se rehace cuando cambia la luz.

### La continuidad entre cámaras

Cuando dos cámaras cubren lo mismo, sus planos se cortan uno detrás de otro, y tienen que casar
(oficio). En estudio y en unidad móvil lo resuelve el control de imagen, cuyo cometido es que todas
las cámaras casen en nivel, color, sombras, altas luces y detalle (véase «Quién responde de ella»).
El procedimiento de igualación desde la unidad de control —con carta de grises, forma de onda y
vectorscopio— es oficio de ese puesto, y este tema no lo da en detalle.

En reportaje con varias cámaras, cada operador tiene que dejar la suya igual que las demás (oficio):

- Los mismos ajustes de imagen: en la Sony PXW-Z200, el archivo de escena se puede guardar en una
  tarjeta y cargar en otra cámara ([Save to Media(B)] y [Load from Media(B)]).
- El balance hecho sobre la misma carta y bajo la misma luz.
- La misma cadencia y la misma obturación, para que el movimiento y el parpadeo sean iguales.
- Cámaras de nivel parecido: la EBU limita el material de nivel 3 a «**around 33%**» de un programa
  HD, precisamente porque se nota al mezclarlo.

La luz también cuenta: el TLCI tiene una escala de lectura propia para la «**Live multi-camera
production [...] such as sport and news where pictures have no post-processing and the pictures are
required only to be credible**» (EBU Tech 3355), porque en directo no hay etalonaje que iguale
después.

## Recomendaciones técnicas que el tema cita

No hay norma jurídica que regule este tema. Las recomendaciones técnicas que cita, en su edición
vigente el 24/09/2026:

- EBU R 103 v3.0, *Video Signal Tolerance in Digital Television Systems*, Ginebra, mayo de 2020:
  márgenes de la señal digital, error de gama y ajuste de los recortadores de cámara.
- EBU R 118 v2, *Tiering of Cameras for use in Television Production*, Ginebra, abril de 2017:
  criterios y niveles de calidad de cámara, relación señal/ruido, latitud, resolución, *aliasing*,
  familias de códec y tasas mínimas.
- EBU Tech 3335, *Methods of measuring the imaging performance of television cameras for the
  purposes of characterisation and setting*, Ginebra, agosto de 2014: apartados de medida, margen
  de exposición, obturador de persiana, obturación nominal y realce de detalle.
- EBU Tech 3355, *Method for the assessment of the colorimetric properties of luminaires. The
  Television Lighting Consistency Index (TLCI-2012) and the Television Luminaire Matching Factor
  (TLMF-2013)*, Ginebra, marzo de 2017: el valor 50 del índice y la escala para multicámara en
  directo.
- Recomendación UIT-R BT.709-6 (06/2015): primarios, blanco D65 y niveles de cuantificación de la
  alta definición.
- Recomendación UIT-R BT.2020-2 (10/2015): primarios de la ultra alta definición y elección de la
  cadencia según la red eléctrica.
- Recomendación UIT-R BT.2100-3 (02/2025): curvas PQ y HLG y blanco de referencia HDR.

## Lo que este tema no da, y dónde está

- Criterios de calidad técnica propios de CSRTV (niveles de cámara admitidos, códecs de la casa,
  procedimientos del control de imagen): no constan en un documento publicado localizado. El Libro
  de estilo de 2004 da sólo los criterios citados (trípode, *raccord*, armonía, responsabilidad del
  realizador).
- El procedimiento de igualación de cámaras desde la unidad de control (carta de grises, pintado,
  ajuste de negros y de blancos por canal): es oficio del control de imagen y no se ha leído una
  fuente que lo describa.
- El nivel de señal del blanco de referencia HLG en porcentaje: está en el Informe UIT-R BT.2408,
  que no pudo leerse.
- Los umbrales por tramos del TLCI: están en una figura de EBU Tech 3355 que no pudo leerse como
  texto.
- Las filas de la tabla de tasas mínimas de EBU R 118 que no se reproducen (H.264 de nivel 2J e
  inferior, códecs UHD): no se han comprobado una a una.
- El obturador global de las cámaras de estudio actuales: la documentación del fabricante no pudo
  leerse.
- El sensor, el diafragma, el enfoque, la cebra, la ganancia y los filtros como mandos de la cámara,
  en el tema 1; el *raccord* completo (físico, sonoro, cinético y sus clases), en el tema 2; los
  soportes y estabilizadores, en el tema 4; la temperatura de color y la calidad de la luz, en el
  tema 5; los formatos, los códecs y la gestión del material, en el tema 7; la estabilización como
  recurso creativo, en el tema 15.

## Trazabilidad

Todas las fuentes se leyeron el 24/09/2026.

| Fuente | Qué sostiene |
|---|---|
| EBU R 103 v3.0 (mayo de 2020), anexos 1 y 2, tabla 1 | Márgenes nominal, preferente y total; error de gama y umbral del 1 %; recortadores en directo; legalizadores; recorte y compresión; sub-negros y PLUGE; 0-700 mV |
| EBU R 118 v2 (abril de 2017), § 1.2, 1.3.1, 3.1.3-3.1.5, tablas 1 y 6 | Criterios de calidad, niveles de cámara, nivel 2J, límite del 33 % del nivel 3, 10 bits y 4:2:2 del nivel 1, familias de códec, tasas mínimas, relación señal/ruido, ganancia negativa, latitud, resolución, *aliasing* |
| EBU Tech 3335 (agosto de 2014), índice, § 2.9, 4 y 4.4 | Apartados de medida, Lmax y Lmin, margen sobre blanco, margen dinámico y ruido, obturador de persiana, obturación nominal, realce de detalle |
| EBU Tech 3355 (marzo de 2017) | Valor 50 del índice; escala de multicámara en directo |
| UIT-R BT.709-6, BT.2020-2 y BT.2100-3 | Primarios, blanco D65, niveles de 8 y 10 bits, monitor de referencia BT.1886, cadencia y red eléctrica, PQ y HLG, blanco de referencia HDR |
| Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía, 1.ª ed., marzo de 2004: 5.1 (p. 79), 5.2 (p. 80), 6.3.4 (p. 91), 6.4 y 6.5 (p. 92) | Criterio del cámara sin realizador, trípode, armonía con el archivo, *raccord* técnico, responsabilidad del realizador |
| Sony, *PXW-Z200/HXR-NX800 Help Guide*, 5-060-574-13(1), 2024 | Monitor de señal, *knee*, negros, matriz, archivos de escena, detalle, reducción de ruido, puntos blancos, parpadeo y su corrección, estabilizador, conversión HDR a SDR en el visor |
| Sony, *PXW-FS5/FS5K Operating Guide*, 4-581-849-11(1) | Difracción y ND, cambio de ND en grabación, realce de contornos, lupa, detección de caras, cebra |
| Blackmagic Design, *URSA Broadcast G2 Installation and Operation Manual*, noviembre de 2021 | Nivel de ayuda al enfoque, cebra, falso color, parpadeo, cadencia y luz |
| Panasonic, *AVC-Intra Frequently Asked Questions* (documento comercial sin fecha) | Comportamiento de la compresión intracuadro y *Long GoP* ante el montaje y el movimiento |

La tabla de coeficientes de luminancia (BT.601, BT.709 y BT.2020) procede de las recomendaciones
UIT-R correspondientes y se toma de un temario ya verificado con ellas; en esta redacción no se han
vuelto a leer las tres.

Oficio sin norma detrás, y así se declara: el reparto de tareas entre operador, control de
imagen y técnico de imagen digital; la lectura del monitor de forma de onda y del vectorscopio; las
funciones del monitor de referencia y las señales de prueba; las aberraciones de Seidel; el punto
dulce; el procedimiento de ajuste de tiraje; *blooming*, *smear* y *moiré*; el orden de los mandos
de exposición; el *knee* y los circuitos de sombras; el balance de blancos, sus tres caminos y la
regla del color complementario; el balance de negros; la profundidad de bits y el submuestreo; la
estabilización pasiva y activa; la obturación de 1/50 o 1/100 con red de 50 Hz; la equivalencia
entre decibelios y pasos, que es además una cuenta (20 · log₁₀ 2 ≈ 6); los controles del realce de
detalle y la dependencia del nivel; la transformada del coseno y los defectos de compresión; el
efecto del ruido y del movimiento sobre el códec; y los remedios de continuidad con una y con varias
cámaras.
