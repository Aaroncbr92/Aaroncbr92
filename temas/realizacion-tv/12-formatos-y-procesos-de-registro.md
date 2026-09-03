# Tema 12 del específico de Realización Televisión · Formatos y procesos de registro, captación y reproducción

Las siglas de este tema, presentadas de entrada: la ultra alta definición (**UHD** o **UHDV**, como la
escribe un enunciado) y la alta definición (**HD**, y **HDTV** referida a la televisión); la
iniciativa de cine digital (**DCI**), que da nombre al 4K de sala; la línea nacional norteamericana
(**NTSC**) y la línea alternada en fase (**PAL**); los cuadros por segundo (**fps**); el código de
tiempo (**TC**), en su forma longitudinal (**LTC**, *longitudinal time code*) y en su forma vertical
(**VITC**); la transformada discreta del coseno (**DCT**, *discrete cosine transform*); la
radiodifusión de vídeo digital terrestre (**DVB-T**) y su segunda generación (**DVB-T2**); el formato
de intercambio de material (**MXF**); los contenedores **MP4**, **AVI**, **MOV** y **MKV**, y el
formato de audio **WAV**; la codificación avanzada de vídeo de alta definición (**AVCHD**); el
conjunto redundante de discos independientes (**RAID**); las tarjetas **SxS** y **P2** y el disco
**XDCAM**; el conector *Bayonet Neill-Concelman* (**BNC**), el conector de audio profesional
(**XLR**, que la industria llama también **Canon** por su fabricante original), el conector de vídeo
para monitores (**VGA**) y el conector de audio de clavija (***jack***); el alto rango dinámico
(**HDR**); y el programa de plan de cámaras **CuePilot**, que es una marca. Y unas cuantas siglas
más que sólo salen como opción falsa o como término suelto: el formato de audio de intercambio
(**AIFF**), la Unión Internacional de Telecomunicaciones (**UIT**), las dos modalidades de código de
tiempo inventadas por otro cuadernillo de este mismo proceso (**FD** y **FF**) y la tarjeta que este
examen inventa (**SWS**), que tampoco existe.

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización, punto 3.2):
> «LA TECNOLOGÍA EN EL ÁMBITO DE LA REALIZACIÓN. Formatos y Procesos de registro, captación y
> reproducción de imagen. Tipos de archivo.»

**Dieciocho preguntas: el segundo banco de esta ocupación.** Y **el más técnico de los veintidós
temas**: resoluciones, cadencias, muestreos, compresión, contenedores, códigos de tiempo y soportes.

**Una de sus dieciocho depende de una imagen**, y va declarada.

<!-- indice -->

## Índice

- [1. La resolución y las dos familias del 4K](#1-la-resolución-y-las-dos-familias-del-4k)
- [2. Qué es la ultra alta definición](#2-qué-es-la-ultra-alta-definición)
- [3. Las cadencias: PAL y NTSC](#3-las-cadencias-pal-y-ntsc)
- [4. El muestreo cromático](#4-el-muestreo-cromático)
- [5. La compresión y la transformada del coseno](#5-la-compresión-y-la-transformada-del-coseno)
- [6. Contenedor, códec y formato de audio](#6-contenedor-códec-y-formato-de-audio)
- [7. El proxy](#7-el-proxy)
- [8. El código de tiempo](#8-el-código-de-tiempo)
- [9. La aritmética del código de tiempo](#9-la-aritmética-del-código-de-tiempo)
- [10. Los soportes de grabación](#10-los-soportes-de-grabación)
- [11. Los conectores](#11-los-conectores)
- [12. El RAID](#12-el-raid)
- [13. La emisión: DVB-T2](#13-la-emisión-dvb-t2)
- [14. Los datos que el examen ha preguntado](#14-los-datos-que-el-examen-ha-preguntado)
- [15. Trazabilidad](#15-trazabilidad)

<!-- /indice -->

## 1. La resolución y las dos familias del 4K

**El tamaño físico de una imagen medida en píxeles se llama resolución.** Ésa es la respuesta oficial a
la pregunta 20.

**Las tres opciones falsas son términos reales de otras magnitudes**: **la escala** es una relación de
proporción; **la proporción** o relación de aspecto es la forma del cuadro; **la clave** —*key*— es una
señal de recorte. **Ninguna cuenta píxeles.**

**Y aquí está la distinción que este punto pregunta DOS VECES, una en cada llamamiento:**

| Familia | Resolución | Relación de aspecto | Quién la define |
|---|---|---|---|
| **UHD**, el 4K de TELEVISIÓN | **3.840 × 2.160** | **16:9** | **La Unión Internacional de Telecomunicaciones** |
| **4K DCI**, el de CINE | **4.096 × 2.160** | **17:9** (1,90:1) | **La iniciativa de cine digital** |

**El estándar 4K UHDV con escala 16:9 es 3.840 × 2.160.** Ésa es la respuesta oficial a la pregunta 7.

**El estándar 4K Cinema con escala 17:9 es 4.096 × 2.160.** Ésa es la respuesta oficial a la pregunta
51.

**Las dos preguntas son la misma con la familia cambiada**, y **el propio enunciado da la pista en la
relación de aspecto**: **16:9 es televisión y 17:9 es cine.** **Quien tenga esa asociación contesta las
dos sin recordar las cifras**, porque **sólo una opción de cada pregunta cuadra con su proporción.**

**Y la comprobación aritmética que las cierra**: **3.840 ÷ 2.160 = 1,777…, que es 16/9.** **4.096 ÷
2.160 = 1,896…, que es aproximadamente 17/9.**

**Las opciones falsas comunes a las dos preguntas** —5.120 × 4.096, 6.400 × 4.800 y 7.680 × 4.800—
**no corresponden a ningún estándar de televisión ni de cine**, y **ninguna da 16:9 ni 17:9.**
**La de 7.680 es la trampa**, porque **7.680 sí es el ancho del 8K**, **pero su alto es 4.320 y no
4.800.**

## 2. Qué es la ultra alta definición

**La ultra alta definición se basa en aumentar la resolución espacial, la resolución temporal, el
rango dinámico, la cuantificación y el espacio de color.** Ésa es la respuesta oficial a la pregunta
87.

**Los cinco ejes, y hay que tenerlos los cinco porque es una pregunta de exhaustividad:**

| Eje | Qué aumenta |
|---|---|
| **Resolución ESPACIAL** | **Más píxeles**: 3.840 × 2.160 y 7.680 × 4.320 |
| **Resolución TEMPORAL** | **Más cuadros por segundo** |
| **RANGO DINÁMICO** | **Más distancia entre el negro y el blanco**: el alto rango dinámico |
| **CUANTIFICACIÓN** | **Más bits por muestra**: diez o doce en lugar de ocho |
| **ESPACIO DE COLOR** | **Gama más amplia**: más colores representables |

**La idea que hay detrás, y es la que hace la respuesta memorable**: **la ultra alta definición NO es
sólo más píxeles.** **Es una mejora en cinco direcciones a la vez**, y **de las cinco, la que menos se
nota en una pantalla doméstica es precisamente la resolución.** **Lo que el espectador percibe como
salto de calidad es sobre todo el rango dinámico y la gama de color.**

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| «Desarrollar el alto rango dinámico dentro del espacio de color 20:20 y con profundidad de más de 10 bits» | **Reduce la ultra alta definición a UNO de los cinco ejes**, y además **inventa un «espacio de color 20:20»**, que **no existe**: **es una deformación del nombre de la Recomendación UIT-R BT.2020** |
| «La utilización de una definición cada vez más amplia, que supone mayor resolución vertical» | **Reduce la ultra alta definición a la resolución**, que es el error corriente |
| «La utilización de códecs más eficientes y siempre compatibles entre sí» | **Ni los códecs definen la ultra alta definición ni la compatibilidad está garantizada** |

**La forma de contestarla**: **es la opción más larga y la que enumera más cosas.** **En una pregunta
de exhaustividad, la respuesta suele ser la que no deja nada fuera**, y **aquí las tres falsas se
quedan cortas.**

## 3. Las cadencias: PAL y NTSC

**La frecuencia de cuadros por segundo utilizada en el sistema NTSC es de 29,97.** Ésa es la respuesta
oficial a la pregunta 8.

| Sistema | Cadencia | Líneas |
|---|---|---|
| **PAL** | **25 cuadros por segundo** | 625 |
| **NTSC** | **29,97 cuadros por segundo** | 525 |
| Cine | 24 cuadros por segundo | — |

**Por qué 29,97 y no 30, que es lo que hay que entender**: **el sistema americano en blanco y negro
funcionaba a 30 cuadros exactos.** **Al añadir el color hubo que meter la subportadora de crominancia
sin interferir con el sonido**, y **la solución fue bajar ligeramente la cadencia**, **exactamente en
una proporción de 1.000 a 1.001.** **De ahí salen los 29,97.**

**Y de ahí sale también el código de tiempo con salto de cuadro** —el *drop frame* del epígrafe 8—:
**contando de treinta en treinta con una cadencia real de 29,97, el código se adelanta al reloj de
pared**, y **hay que corregirlo saltando números.**

**Las tres opciones falsas son cadencias reales de otros sistemas**: **23,98** es la cadencia de cine
adaptada al sistema americano —24 con la misma corrección de 1.000 a 1.001—; **48** es el doble de la
de cine, usada en alta cadencia; y **25** es **la de PAL**, que es la trampa buena por ser la del
sistema europeo.

## 4. El muestreo cromático

**El muestreo cromático dice cuántas muestras de color se guardan por cada muestra de luminancia.**

| Notación | Qué guarda |
|---|---|
| **4:4:4** | **Una muestra de color por cada píxel: SIN submuestreo** |
| **4:2:2** | **La mitad de muestras de color en horizontal** |
| **4:2:0** | **La mitad en horizontal y la mitad en vertical** |
| **4:1:1** | Una cuarta parte en horizontal |

**El patrón en el que NO hay submuestreo de las señales de crominancia es 4:4:4.** Ésa es la respuesta
oficial a la pregunta 48.

**La regla que la resuelve**: **la primera cifra es la referencia de luminancia y las otras dos cuentan
las muestras de color.** **Si las tres cifras son iguales, hay tanta información de color como de
brillo: no hay submuestreo.** **En cuanto la segunda o la tercera bajan, lo hay.**

**Y las opciones falsas de esta pregunta son instructivas por otro motivo**: **dos de las cuatro NO SON
PATRONES REALES.** **«4.2.1» y «3.1.1» no existen como notaciones de muestreo cromático**: **la primera
cifra de la notación es siempre 4**, porque es la referencia. **La opción c) empieza por 3 y se cae
sola.**

## 5. La compresión y la transformada del coseno

**La transformada discreta del coseno es la operación matemática sobre la que se construye la mayor
parte de la compresión de imagen y de vídeo**: el formato de fotografía comprimida, la familia de
compresión de vídeo del grupo de expertos en imágenes en movimiento y sus sucesores.

**Qué hace, en lenguaje llano**: **convierte un bloque de píxeles en un conjunto de COEFICIENTES que
describen ese bloque como suma de patrones de frecuencia**, **de los más suaves a los más finos.**
**No comprime nada por sí misma**: **reorganiza la información de manera que la parte importante quede
concentrada en unos pocos coeficientes.**

**Y la compresión viene después, en la recuantificación:**

**En la transformada discreta del coseno, la recuantificación de los coeficientes supone que los
coeficientes son recuantificados individualmente, de manera que podemos desechar información de altas
frecuencias y comprimir la señal según el flujo de datos manteniendo información fundamental.** Ésa es
la respuesta oficial a la pregunta 54.

**Los tres elementos de la respuesta, y son los que la hacen correcta:**

1. **Los coeficientes se recuantifican INDIVIDUALMENTE.** **No todos con el mismo paso**: **los de baja
   frecuencia con precisión y los de alta con poca.**
2. **Se DESECHA información de ALTAS FRECUENCIAS.** **Y ahí está el porqué**: **el ojo distingue mal el
   detalle muy fino**, así que **es la información que menos se echa de menos.**
3. **Se comprime SEGÚN EL FLUJO DE DATOS disponible**, **manteniendo la información fundamental.**

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| «Mantenemos la proporción del valor de los coeficientes… **compresión SIN PÉRDIDAS**» | **LA TRAMPA MEJOR PUESTA**: **la recuantificación es precisamente lo que introduce la PÉRDIDA.** Si se mantuviera la proporción de todos los coeficientes no habría compresión con pérdida |
| «Es lo que posibilita una eficiente compresión intercuadro o temporal» | **Confunde dos cosas distintas**: **la transformada del coseno es INTRAcuadro** —trabaja dentro de una imagen—; **la compresión temporal compara imágenes sucesivas** y es otro mecanismo |
| «No es posible, ya que entonces sus componentes de frecuencia serían limitados» | **Niega una operación que se hace todos los días** |

**La palabra que decide es «desechar»**: **la respuesta correcta es la única que reconoce que se *tira*
información**, y **eso es lo que hace la compresión con pérdida.**

## 6. Contenedor, códec y formato de audio

**Es la distinción que este punto pregunta tres veces**, y conviene fijarla:

| Concepto | Qué es | Ejemplos |
|---|---|---|
| **CÓDEC** | **Cómo se COMPRIME** | H.264, H.265, ProRes, DNxHD, JPEG 2000 |
| **CONTENEDOR** | **Cómo se EMPAQUETA** la esencia con sus metadatos | **MXF**, **MOV**, **MP4**, **AVI**, **MKV** |
| **Formato de audio** | Un contenedor o codificación de sonido | **WAV**, AIFF, MP3 |

**Cuando hablamos de MXF nos referimos a un tipo de archivo contenedor.** Ésa es la respuesta oficial a
la pregunta 108.

**Las tres opciones falsas lo llaman códec** —sin pérdida y con pérdida— **o «formato comprimido con
canal alfa»**. **Ninguna es correcta**: **el formato de intercambio de material no comprime nada; lo que
lleva dentro puede ser cualquier códec.**

**De los formatos que la pregunta 1 ofrece, el que contiene sólo audio es WAV.** Ésa es la respuesta
oficial.

**Las tres opciones falsas son contenedores multimedia** —**MP4**, **AVI** y **MKV**— **que llevan vídeo
y audio.** **La pregunta se contesta por categoría**: **tres de las cuatro son contenedores de vídeo y
uno es de audio.**

**De los archivos que la pregunta 31 ofrece, el desarrollado por Apple es MOV.** Ésa es la respuesta
oficial.

| Formato | Quién lo desarrolló |
|---|---|
| **MOV** | **Apple**, para su arquitectura multimedia |
| **AVI** | **Microsoft** |
| **MP4** | **El grupo de expertos en imágenes en movimiento** |
| **AVCHD** | **Sony y Panasonic**, conjuntamente |

**El aviso de vocabulario**: **la propia pregunta 31 desarrolla las siglas entre paréntesis**, y **la de
MOV dice «QuickTime Movie»**, **que es el nombre de la arquitectura multimedia de Apple.** **El
enunciado lleva la respuesta dentro.**

## 7. El proxy

**Un *proxy* de vídeo es una copia de menor resolución de la imagen y el sonido original, muy
comprimida, que incluye código de tiempo y algunos otros metadatos básicos.** Ésa es la respuesta
oficial a la pregunta 105.

**Para qué sirve**: **para trabajar sin mover el material pesado.** **Se monta con el *proxy*, que es
ligero y viaja por una línea estrecha**, y **al final se reconforma contra el original.** **Es el flujo
que el temario de Edición y Montaje llama *offline*-*online*.**

**Y por qué el CÓDIGO DE TIEMPO es imprescindible, que es lo que la pregunta mide**: **el *proxy* y el
original tienen que compartir el código de tiempo**, porque **es lo que permite que las decisiones
tomadas sobre el *proxy* se apliquen al original.** **Un *proxy* sin código de tiempo no sirve para
montar: sirve para ver.**

**Las cuatro opciones combinan dos variables**, y hay que acertar las dos:

| Variable | Opciones |
|---|---|
| **Qué es** | **Copia de MENOR RESOLUCIÓN** frente a «versión en un códec más manejable» |
| **¿Lleva código de tiempo?** | **SÍ** frente a no |

**La respuesta correcta es «menor resolución» Y «con código de tiempo».** **Las otras tres fallan en
una de las dos**, y **la más tentadora es la que dice «códec más manejable» y «con código de tiempo»**,
porque **la primera mitad describe una virtud real del *proxy*.** **Lo que la descarta es que un *proxy*
es sobre todo MENOR RESOLUCIÓN**, no sólo otro códec.

## 8. El código de tiempo

**El código de tiempo es la etiqueta que numera cada cuadro** en horas, minutos, segundos y cuadros, y
**es el instrumento de sincronización de toda la cadena.**

**Sus dos formas de transporte:**

| Forma | Cómo viaja | Dónde se usa |
|---|---|---|
| **LTC**, longitudinal | **Como una SEÑAL DE AUDIO** por un canal propio | **Entre equipos**: es el que se reparte a los departamentos |
| **VITC**, vertical | **Dentro de la propia señal de vídeo**, en el intervalo vertical | Dentro de la cadena de vídeo |

**Una palabra de código de tiempo longitudinal para un solo fotograma está formada por 80 bits.** Ésa
es la respuesta oficial a la pregunta 100.

**Cómo se reparten esos ochenta bits, que es lo que hace la cifra memorable en lugar de arbitraria:**

| Contenido | Bits aproximados |
|---|---|
| **Las cifras de hora, minuto, segundo y cuadro**, en decimal codificado en binario | **Veintiséis** |
| **Bits de bandera**: salto de cuadro, color, etcétera | Unos pocos |
| **Bits de usuario**: información libre —fecha, número de bobina— | **Treinta y dos** |
| **Palabra de sincronismo**, al final | **Dieciséis** |

**Y el dato que explica por qué son ochenta y no otros**: **a treinta cuadros por segundo, ochenta bits
por cuadro dan 2.400 bits por segundo**, **que es una frecuencia que cabe holgadamente en un canal de
audio.** **El código longitudinal se diseñó para grabarse en una pista de audio de una cinta**, y **de
ahí su tamaño.**

**Las tres opciones falsas —16, 64 y 32 bits— son potencias de dos plausibles**, y **la de 32 es la
trampa buena**, porque **32 es el número de bits de usuario**, que es una parte real de la palabra.

**De dónde procede el código de tiempo longitudinal en una realización con plan de cámaras
programado**: **del departamento de audio.** Ésa es la respuesta oficial a la pregunta 75.

**Por qué del audio, y es coherente con lo anterior**: **el código longitudinal ES una señal de audio.**
**Se genera y se distribuye por la infraestructura de sonido**, **que es la que tiene los canales, los
repartidores y los cables adecuados para una señal de esa naturaleza.** **El mezclador de imagen no
reparte audio**, y **el ordenador del ayudante de realización lo recibe, no lo genera.**

**Las tres opciones falsas** —el ordenador del control, el mezclador de imagen y el departamento de
iluminación— **son puestos y equipos reales de la misma realización**, y **ninguno genera código de
tiempo longitudinal.**

## 9. La aritmética del código de tiempo

**Un vídeo que empieza en 00:47:17:23 y termina en 01:23:54:00 dura 36 minutos, 36 segundos y 3
cuadros.** Ésa es la respuesta oficial a la pregunta 4.

**Cómo se resta un código de tiempo, y hay que hacerlo de derecha a izquierda con acarreos:**

| Campo | Operación | Resultado |
|---|---|---|
| **Cuadros** | **00 − 23**: no se puede, **se toma prestado un segundo** | **25 − 23 = 2 cuadros** |
| **Segundos** | **54 − 1 prestado = 53**; **53 − 17** | **36 segundos** |
| **Minutos** | **23 − 47**: no se puede, **se toma prestada una hora** | **83 − 47 = 36 minutos** |
| **Horas** | **1 − 1 prestada = 0**; **0 − 0** | **0 horas** |

**La resta da 00:36:36:02**, y **la respuesta oficial da tres cuadros.**

**Por qué, y es una cuestión de convenio que conviene conocer porque aparece en cualquier sala de
montaje:**

| Convenio | Qué cuenta | Resultado aquí |
|---|---|---|
| **EXCLUSIVO** | **La duración es la resta pura**: el código final marca el cuadro SIGUIENTE al último | **36:36:02** |
| **INCLUSIVO** | **Se cuenta el último cuadro también**: se suma uno a la resta | **36:36:03** |

**El enunciado dice que el vídeo «TERMINA EN» ese código**, lo que **apunta al convenio inclusivo**: **si
el último cuadro del vídeo es el 01:23:54:00, ese cuadro cuenta**, y **la duración total es la resta más
uno.**

**Y lo importante para contestar, que hace la pregunta segura pese al convenio**: **las cuatro opciones
son 35' 35'' 00, 35' 36'' 01, 36' 36'' 03 y 36' 42'' 01.** **Sólo una tiene 36 minutos y 36 segundos**,
que es **lo que sale con cualquiera de los dos convenios.** **El convenio sólo afecta al último campo,
y ninguna otra opción compite en los dos primeros.**

**Una declaración expresa**: **el enunciado no dice a qué cadencia va el vídeo**, y **la resta de
cuadros depende de ella**: **a 25 cuadros por segundo el resultado es 02 y a 24 sería 01.** **Este tema
ha operado a 25 cuadros por segundo, que es la cadencia del sistema europeo**, y **lo declara.** **La
respuesta oficial se sostiene con esa cadencia y el convenio inclusivo**, y **en cualquier caso es la
única opción con los minutos y los segundos correctos.**

**El aviso de estudio**: **en una pregunta de código de tiempo, hay que resolver primero los campos
grandes.** **Los minutos y los segundos casi siempre bastan para descartar tres opciones**, y **el campo
de cuadros, que es donde están los convenios y las cadencias, sólo hace falta si dos opciones empatan.**

## 10. Los soportes de grabación

| Soporte | Qué es | Quién lo desarrolló |
|---|---|---|
| **Tarjeta SxS** | **Tarjeta de memoria de estado sólido** para cámara profesional | **Sony y SanDisk** |
| **Tarjeta P2** | **Tarjeta de memoria profesional** | **Panasonic** |
| **Disco XDCAM** | **Disco óptico profesional** | **Sony** |
| **«Tarjeta SWS»** | **NO EXISTE** | — |

**El que NO es un soporte de grabación es la tarjeta SWS.** Ésa es la respuesta oficial a la pregunta
53.

**Cómo se contesta sin conocer los tres soportes reales**: **la sigla falsa es una permutación de otra
verdadera** —**SWS** frente a **SxS**—, **y ése es el mecanismo del distractor.** **Es el mismo recurso
que el cuadernillo usa en el tema 4 con las modalidades de código de tiempo, donde inventa «FD» y «FF»
invirtiendo las letras de las verdaderas.**

## 11. Los conectores

**La pregunta 93 muestra la imagen de un conector y pide identificarlo.** **La respuesta oficial es el
conector BNC.**

**Una declaración expresa**: **esta pregunta depende enteramente de una imagen**, que **un temario
escrito no puede reproducir ni contrastar.** **La respuesta descansa en la plantilla oficial.** Este
tema **no describe la imagen**, porque **no la tiene delante.**

**Lo que sí aporta, y es lo que sirve para cualquier pregunta de esta familia**, son **los rasgos por
los que se distinguen a la vista los cuatro conectores que la pregunta ofrece:**

| Conector | Para qué | Cómo se reconoce a la vista |
|---|---|---|
| **BNC** | **Vídeo** por coaxial, de 75 ohmios | **Cilíndrico y metálico**, con **DOS PIVOTES laterales** y **anillo de bayoneta**: se mete y se gira un cuarto de vuelta |
| ***Canon*** o **XLR** | **Audio profesional** | **Cilíndrico y grueso**, con **TRES PATILLAS** dentro y **pestillo de retención** |
| **VGA** | **Vídeo analógico a monitor de ordenador** | **Trapezoidal**, con **quince pines en tres filas** y **dos tornillos** a los lados |
| ***Jack*** | **Audio** | **Una CLAVIJA CILÍNDRICA con anillos**, sin carcasa metálica que la rodee |

**La regla que permite descartar sin ver bien la imagen**: **son cuatro formas geométricamente muy
distintas.** **Si tiene tres patillas, es XLR; si es trapezoidal con tornillos, es VGA; si es una
clavija lisa con anillos, es un *jack*; y si es cilíndrico con dos pivotes de bayoneta, es BNC.**

**Y el dato de oficio que conviene tener**: **en una instalación de televisión el BNC es el conector de
vídeo por antonomasia**, y **el XLR el de audio.** **Un realizador que ve un cable con BNC sabe que
lleva vídeo o sincronismo, y uno con XLR, que lleva audio.**

## 12. El RAID

**El número mínimo de discos para configurar un RAID 1 es 2.** Ésa es la respuesta oficial a la
pregunta 104.

| Nivel | Cómo escribe | Mínimo de discos |
|---|---|---|
| **RAID 0** | **Reparte los datos**, sin redundancia | **2** |
| **RAID 1** | **ESPEJO: duplica un disco en otro** | **2** |
| **RAID 5** | Reparte con **paridad distribuida** | **3** |
| **RAID 6** | Reparte con **doble paridad** | **4** |

**Por qué dos y no uno**: **el espejo consiste en escribir lo mismo en dos discos**, así que **hace
falta un disco donde escribir y otro donde copiar.** **Con un solo disco no hay espejo posible.**

**La trampa está en la opción a)**: **«1» es la respuesta que daría quien confunda el NÚMERO del nivel
con el NÚMERO de discos.** **El nivel se llama RAID 1 y necesita 2 discos**, igual que **el RAID 5
necesita 3 y el RAID 6 necesita 4.** **El número del nivel no dice cuántos discos hacen falta.**

**Y el dato de oficio para una sala de realización**: **el RAID protege del fallo de UN disco, no de un
borrado ni de un incendio.** **No es una copia de seguridad**: **es lo que mantiene el trabajo vivo
mientras se hace.**

## 13. La emisión: DVB-T2

**La emisión en la segunda generación de radiodifusión de vídeo digital terrestre permitirá un mejor
uso del espectro de radiodifusión terrestre, con entre un 30 y un 50 % extra de ancho de banda, lo que
permite más canales en alta definición y transmisiones en ultra alta definición que el anterior.** Ésa
es la respuesta oficial a la pregunta 35.

**Qué mejora, y por qué importa a una casa de televisión**: **el espectro radioeléctrico es finito y
está repartido.** **Una norma de emisión más eficiente permite meter más canales o canales de más
calidad EN EL MISMO ESPECTRO**, sin pedir más frecuencias. **Es lo que hace posible el paso a la ultra
alta definición por vía terrestre.**

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| «Asegurar la interactividad completa con los contenidos» | **La interactividad no es lo que una norma de modulación y codificación aporta** |
| «Un 80 % más de capacidad, aunque requerirá un cambio completo en los equipamientos domésticos» | **La cifra no es la de la respuesta oficial**, y **la segunda mitad exagera**: **hacen falta receptores compatibles, no un cambio completo de todo el equipamiento** |
| «Actualmente el sistema imperante ya es el DVB-T2» | **LA TRAMPA MEJOR PUESTA, porque es una afirmación de *hecho* y no de capacidad**: **el enunciado pregunta QUÉ PERMITIRÁ**, no qué se usa |

**Una declaración expresa**: **la cifra del 30 al 50 % de ancho de banda adicional no se ha contrastado
en documentación del organismo de normalización.** **Este proyecto no ha volcado la norma técnica
correspondiente**, y **la respuesta descansa en la plantilla oficial.** **Lo que el tema sostiene con
seguridad es el CONCEPTO**: que la segunda generación es más eficiente espectralmente que la primera y
que eso es lo que permite más canales o más calidad en el mismo espectro.

## 14. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 1 | Qué formato contiene sólo audio | c) WAV ✔ |
| 4 | Cuánto dura un vídeo entre dos códigos de tiempo | c) 36' 36'' 03 ✔ **·** ver el epígrafe 9 |
| 7 | Estándar 4K UHDV con escala 16:9 | c) 3.840 × 2.160 ✔ |
| 8 | Cadencia del sistema NTSC | c) 29,97 ✔ |
| 20 | Cómo se llama el tamaño de una imagen en píxeles | d) Resolución ✔ |
| 31 | Qué archivo desarrolló Apple | c) MOV ✔ |
| 35 | Qué permitirá la emisión en DVB-T2 | a) 30-50 % extra de ancho de banda ✔ **·** sólo con la plantilla |
| 48 | En qué patrón NO hay submuestreo | d) 4:4:4 ✔ |
| 51 | Estándar 4K Cinema con escala 17:9 | a) 4.096 × 2.160 ✔ |
| 53 | Cuál NO es un soporte de grabación | c) Tarjeta SWS ✔ |
| 54 | La recuantificación de coeficientes en DCT | d) Se recuantifican individualmente y se desechan altas frecuencias ✔ |
| 75 | De dónde procede el código de tiempo longitudinal | b) Del departamento de audio ✔ |
| 87 | En qué se basa la UHD | d) Resolución espacial y temporal, rango, cuantificación y espacio de color ✔ |
| 93 | Qué conector identificas en la imagen | c) BNC ✔ **·** sólo con la plantilla |
| 100 | Cuántos bits tiene una palabra de LTC por fotograma | a) 80 ✔ |
| 104 | Número mínimo de discos para un RAID 1 | b) 2 ✔ |
| 105 | Qué es un *proxy* de vídeo | a) Copia de menor resolución con código de tiempo ✔ |
| 108 | Qué es MXF | a) Un tipo de archivo contenedor ✔ |

**Las dieciocho respuestas oficiales son correctas.**

**Y dos de las dieciocho descansan sólo en la plantilla**: **la que depende de una imagen** y **la cifra
de ancho de banda de la norma de emisión.**

**El aviso de estudio**: **cuatro preguntas se contestan con la misma distinción** —**resolución,
cadencia, muestreo y profundidad son ejes independientes**— **y dos son la misma pregunta con la
familia cambiada** —el 4K de televisión y el de cine—. **Seis de dieciocho salen de dos ideas.**

## 15. Trazabilidad

**Este tema no cita ninguna norma del BOE.** Su materia son los formatos, los procesos de registro y
los tipos de archivo, y **va como oficio**, salvo lo que descansa en la plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Dos afirmaciones**: la identificación de un conector en una imagen y la cifra de ancho de banda adicional de la segunda generación de radiodifusión terrestre | Preguntas 93 y 35 |

**Cuatro declaraciones expresas:**

1. **La pregunta 93 depende enteramente de una imagen.** **El temario no la describe**, porque no la
   tiene delante. **La respuesta descansa en la plantilla**, y **lo que el tema aporta en su lugar son
   los rasgos por los que se distinguen a la vista los cuatro conectores que la pregunta ofrece.**
2. **La cifra del 30 al 50 % de ancho de banda adicional no se ha contrastado en la norma técnica del
   organismo de normalización.** **La respuesta descansa en la plantilla**, y **lo que el tema sostiene
   es el concepto de mayor eficiencia espectral.**
3. **El enunciado de la pregunta 4 no dice a qué cadencia va el vídeo**, y **la resta del campo de
   cuadros depende de ella.** **Este tema ha operado a 25 cuadros por segundo, la cadencia del sistema
   europeo**, y **lo declara.** **La respuesta oficial se sostiene con esa cadencia y con el convenio
   inclusivo de duración**, y **en cualquier caso es la única opción con los minutos y los segundos
   correctos.**
4. **El reparto de los ochenta bits de la palabra de código de tiempo longitudinal se presenta como
   orden de magnitud y no como cifra verificada.** **Este proyecto no ha volcado la norma del organismo
   que lo fija.** **Lo que la pregunta mide, y lo que el tema sostiene con seguridad, es el total: 80
   bits.**

**Y una remisión**: **las resoluciones de la ultra alta definición, la notación del muestreo cromático,
la distinción entre códec y contenedor y el funcionamiento del código de tiempo están verificados con
la norma delante en los temarios de Edición y Montaje y de Información Gráfica de este mismo
proyecto.** **Aquí se citan por remisión y no se vuelven a sostener.**
