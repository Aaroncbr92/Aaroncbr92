# Tema 4 del específico de Edición, Montaje y Procesos Audiovisuales · Tratamiento digital de la señal de televisión

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 4 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Recomendaciones UIT-R BT.2020-2** y **BT.709-6**. El resto —muestreos cromáticos, compresión, contenedores y código de tiempo— **va como oficio y así se declara** |
| **Identificador** | **UIT-R BT.2020-2** · **UIT-R BT.709-6**. No tienen identificador del BOE: se citan por su número de recomendación |
| **Redacción que se estudia** | Las **ediciones vigentes**: la **2** de la BT.2020 y la **6** de la BT.709 |
| **Sólo con la plantilla** | **Dos preguntas** —la profundidad de bits de la «fase 1» de UHD, que es una decisión de despliegue y no de la Recomendación, y la atribución de la señal HD 1080/50i a la norma **SMPTE-274M**, cuyo texto no se ha consultado— **descansan en la plantilla oficial**, y así se declara en el tema |
| **Extensión** | **4.435 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la alta definición (**HD**) y la ultra alta
definición (**UHD**); la interfaz digital serie (**SDI**) y su versión de alta definición
(**HD-SDI**); los cuadros por segundo (**fps**, *frames per second*); el código de tiempo (**TC**,
*time code*), con sus modalidades de salto de cuadro (**DF**, *drop frame*) y sin salto (**NDF**,
*non-drop frame*), a las que el examen añade dos siglas inventadas, **FD** y **FF**; la codificación
de vídeo de alta eficiencia (**HEVC**, conocida como **H.265**) y
su predecesora **H.264**, también llamada **AVC**; el formato de intercambio de material (**MXF**,
*material exchange format*); el paquete de cine digital (**DCP**, *digital cinema package*); el
formato de imagen de píxeles digitales (**DPX**) y los contenedores de Apple (**MOV**) y de la
familia MPEG (**MP4**); la línea alternada en fase (**PAL**) y la línea nacional norteamericana
(**NTSC**); los tres primarios rojo, verde y azul (**RGB**); el alto rango dinámico (**HDR**); el
disco versátil digital (**DVD**); la iniciativa de cine digital (**DCI**, *Digital Cinema
Initiatives*), que da nombre al 4K de sala; la Sociedad de Ingenieros de Cine y Televisión
(**SMPTE**); la Unión Internacional de Telecomunicaciones en su nombre inglés (**ITU**), que es como
la escribe una de las opciones del examen; la Unión Internacional de Telecomunicaciones
(**UIT**), cuyo sector de radiocomunicaciones (**UIT-R**) publica las recomendaciones **BT.601**,
**BT.709**, **BT.2020** y **BT.2100**; el Grupo de Expertos en Imágenes en Movimiento (**MPEG**) y el
Grupo Conjunto de Expertos en Fotografía (**JPEG**); y el canal de transparencia, llamado **canal
alfa**.

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, punto 2):
> «Tratamiento digital de la señal de televisión.»
> «2.1. Normas de codificación, compresión y soporte.»
> «2.3. Codificadores y sistemas de compresión.»

**Quince preguntas: el banco más grande de esta ocupación.** Y es el punto que más vocabulario exige:
resoluciones, relaciones de aspecto, muestreos, recomendaciones, normas SMPTE, códecs y código de
tiempo.

<!-- indice -->

## Índice

- [1. La resolución y la relación de aspecto](#1-la-resolución-y-la-relación-de-aspecto)
- [2. La profundidad de bits en UHD](#2-la-profundidad-de-bits-en-uhd)
- [3. El muestreo cromático](#3-el-muestreo-cromático)
- [4. El barrido: progresivo y entrelazado](#4-el-barrido-progresivo-y-entrelazado)
- [5. Las recomendaciones de la UIT y las normas SMPTE](#5-las-recomendaciones-de-la-uit-y-las-normas-smpte)
- [6. Vídeo compuesto, por componentes y digital](#6-vídeo-compuesto-por-componentes-y-digital)
- [7. El *jitter*](#7-el-jitter)
- [8. La compresión: intracuadro e intercuadro](#8-la-compresión-intracuadro-e-intercuadro)
- [9. Los códecs que el examen nombra](#9-los-códecs-que-el-examen-nombra)
- [10. El código de tiempo: DF y NDF](#10-el-código-de-tiempo-df-y-ndf)
- [11. Los datos que el examen ha preguntado](#11-los-datos-que-el-examen-ha-preguntado)
- [12. Trazabilidad](#12-trazabilidad)

<!-- /indice -->

## 1. La resolución y la relación de aspecto

**La resolución espacial es cuántos píxeles tiene la imagen; la relación de aspecto es la proporción
entre su ancho y su alto.** Son dos cosas distintas, y el examen pregunta por las dos.

| Formato | Píxeles (horizontal × vertical) | Relación de aspecto |
|---|---|---|
| **Definición estándar** (PAL) | 720 × 576 | 4:3 o 16:9 |
| **HD** | 1.280 × 720 | 16:9 |
| **Full HD** | 1.920 × 1.080 | 16:9 |
| **UHD** o 4K de televisión | 3.840 × 2.160 | **16:9** |
| **4K DCI**, de cine | 4.096 × 2.160 | 1,90:1 |
| **8K** | **7.680 × 4.320** | **16:9** |

**La resolución espacial de 8K para relación de aspecto 16:9 es de 7.680 píxeles horizontales por
4.320 píxeles verticales.** Ésa es la respuesta oficial a la pregunta 46, y la **Recomendación UIT-R
BT.2020-2** la recoge en su **Cuadro 1**, junto con la de 3.840 × 2.160 y con un formato de imagen de
**«16:9»**.

**Las tres opciones falsas de la pregunta 46 y su error:**

| Opción | Qué es |
|---|---|
| «4.320 horizontales × 7.680 verticales» | **Los números correctos, invertidos.** Daría una imagen vertical |
| «3.840 × 2.160» | **Es UHD, no 8K** |
| «4.096 × 2.160» | **Es el 4K de cine**, y su relación de aspecto no es 16:9 |

**La relación de aspecto en UHD es 16:9.** Ésa es la respuesta oficial a la pregunta 65, y es la misma
que la de HD: **lo que UHD multiplica es el número de píxeles, no la forma de la pantalla**.

**Las tres opciones falsas son relaciones reales de otras cosas**: **21:9** es el formato panorámico
de algunos monitores y de parte del cine; **4:3** es la televisión antigua; y **1,85:1** es una
relación de proyección cinematográfica.

**La confusión que hay que deshacer**: **«4K» no es una sola cosa.** El 4K de televisión —UHD— es
3.840 × 2.160 y es 16:9; **el 4K de cine —DCI— es 4.096 × 2.160 y no es 16:9**. El examen usa las dos
en la misma pregunta.

## 2. La profundidad de bits en UHD

**La profundidad de bits de la señal de vídeo en la fase 1 de desarrollo de UHD en 3.840 × 2.160 es
de 10 bits.** Ésa es la respuesta oficial a la pregunta 6.

**Lo que la norma dice y lo que la norma no dice**, que conviene separar:

- **La Recomendación UIT-R BT.2020-2 admite dos profundidades**: su Cuadro 5, sobre representación
  digital, fija como formato de codificación **«10 ó 12 bits por componente»**.
- **La «fase 1» no es un concepto de la Recomendación**: es una fase de despliegue definida por los
  organismos de radiodifusión europeos, que **eligió 10 bits** de los dos valores que la
  Recomendación permite, junto con 3.840 × 2.160 y cadencias de hasta 60 cuadros por segundo. **La
  fase 2 es la que incorpora el alto rango dinámico, la gama amplia y las cadencias altas.**

**Por tanto**: **la respuesta es una de las dos que la norma admite**, y la elección concreta de esa
fase **no se ha podido contrastar en la documentación del organismo que la definió**. Descansa en la
plantilla oficial.

**Las tres opciones falsas**: **12 bits** es la otra profundidad que la Recomendación admite, y es la
de la fase 2 y de la producción de cine; **14 bits** no aparece en ninguna de las dos; y **8 bits** es
la profundidad de la definición estándar y de la alta definición de consumo.

**Por qué importa esta cifra, más allá de la pregunta**: **a 8 bits, un cielo o un fundido se rompen
en franjas** —el *banding* del tema 2—, y con la mayor luminancia del UHD el defecto se vería aún
más. **Diez bits es el mínimo con el que un degradado aguanta.**

## 3. El muestreo cromático

**El muestreo cromático dice cuántas muestras de color se guardan por cada muestra de luminancia.**
Se escribe con tres o cuatro cifras, y **cada una cuenta muestras en un bloque de referencia de cuatro
píxeles de ancho por dos de alto**.

| Notación | Qué guarda | Dónde se usa |
|---|---|---|
| **4:4:4** | **Una muestra de color por cada píxel**: sin submuestreo | Grafismo, croma, cine digital |
| **4:2:2** | **La mitad de muestras de color en horizontal** | **El estándar de producción de televisión** |
| **4:2:0** | La mitad en horizontal **y la mitad en vertical** | **Emisión y distribución**: ahorra la mitad del color |
| **4:1:1** | Una cuarta parte en horizontal | Formatos antiguos de definición estándar |

**Y una cuarta cifra puede aparecer.** **Un archivo de vídeo con muestreo cromático 4:4:4:4 significa
que tiene una señal de vídeo RGB sin submuestreo de color más información del canal alfa.** Ésa es la
respuesta oficial a la pregunta 18.

**Qué es el canal alfa**: **un cuarto canal que dice, píxel a píxel, cuánto de opaco es**. No lleva
color: lleva **transparencia**. Es lo que permite superponer un rótulo o un elemento de grafismo sobre
otra imagen **sin recortarlo a mano**, y por eso aparece en el punto 5.5 del anexo, el de las
incrustaciones.

**Las tres opciones falsas de la pregunta 18 son la misma frase con el final cambiado:**

| Opción | Por qué no |
|---|---|
| «RGB sin submuestreo de color», sin más | **Eso es 4:4:4, con tres cifras.** La cuarta cifra tiene que significar algo |
| «RGB sin submuestreo más metadatos» | **Los metadatos no van en un canal de muestreo**: van en la cabecera del fichero |
| «RGB con submuestreo de color» | **Contradice la propia notación**: cuatro cuatros es precisamente **sin** submuestreo |

**La regla que resuelve la pregunta**: **la cuarta cifra de un muestreo es siempre el canal alfa**, y
sólo puede ser 4 —alfa completo— o 0 —sin alfa—.

## 4. El barrido: progresivo y entrelazado

**En el barrido progresivo cada imagen se dibuja entera, línea por línea. En el entrelazado, cada
imagen se dibuja en dos pasadas**: primero las líneas impares y después las pares. **Cada pasada es un
campo, y dos campos forman un cuadro.**

**En el sistema PAL el barrido entrelazado es necesario para evitar el parpadeo de la imagen de
televisión.** Ésa es la respuesta oficial a la pregunta 69, y ésa es la razón histórica exacta por la
que se inventó.

**El razonamiento del que salió el entrelazado, en tres pasos:**

1. **Con 25 imágenes completas por segundo, el movimiento se ve fluido pero la pantalla parpadea**:
   el ojo detecta el refresco.
2. **Con 50 imágenes completas por segundo no parpadearía**, pero **haría falta el doble de ancho de
   banda**, que en la televisión analógica no había.
3. **El entrelazado da 50 refrescos por segundo con la información de 25 imágenes**: se refresca media
   imagen cada vez. **Se elimina el parpadeo sin gastar más banda.**

**Las tres opciones falsas de la pregunta 69:**

| Opción | Por qué no |
|---|---|
| «Para llenar toda la pantalla con la imagen» | **La pantalla se llena igual con barrido progresivo** |
| «Al utilizar dos cañones electrónicos han de entrecruzarse» | **Un tubo de televisión en blanco y negro tiene un cañón y uno en color tiene tres**, no dos, y **el entrelazado no tiene que ver con el número de cañones** |
| «Ya no se utiliza este método en el sistema PAL» | **El sistema PAL es entrelazado por definición**: 625 líneas, 50 campos |

**Y de ahí sale la pregunta 43.** **En la señal de vídeo HD-SDI 1080 50i contamos con 50 imágenes por
segundo.** Ésa es la respuesta oficial.

**La lectura de la notación**, que es lo que la pregunta exige: **«1080» son las líneas activas**,
**«50» es el número de campos por segundo** y **«i» significa entrelazado**. **Cincuenta campos por
segundo son veinticinco cuadros completos**, y **cada campo es una imagen que llega a la pantalla**.

**Por qué la opción a) —«50 *frames* por segundo»— es la falsa mejor construida**: **50i no son 50
cuadros, son 50 campos y 25 cuadros**. Si fueran cuadros la notación sería **1080p50**. **Ésa es
exactamente la distinción que la pregunta mide**, y por eso la respuesta buena dice «imágenes» y no
«*frames*».

**Las otras dos opciones** —«50 líneas por segundo» y «50 píxeles por segundo»— **son absurdas por
magnitud**: una señal de 1080 líneas a 50 campos por segundo **transmite decenas de miles de líneas
por segundo y decenas de millones de píxeles**.

## 5. Las recomendaciones de la UIT y las normas SMPTE

**Hay dos familias de documentos que definen la señal de televisión, y el examen pregunta por las
dos.**

| Familia | Quién la publica | Qué define |
|---|---|---|
| **Recomendaciones UIT-R BT** | La **Unión Internacional de Telecomunicaciones** | **Los parámetros de la imagen**: primarios, luminancia, gama, resolución |
| **Normas SMPTE** | La **Sociedad de Ingenieros de Cine y Televisión** | **La interfaz y el formato de la señal**: cómo se transporta y se serializa |

**La recomendación que afecta a la señal de vídeo digital en HD es la Recomendación UIT-R BT.709.**
Ésa es la respuesta oficial a la pregunta 91.

**Las tres opciones falsas son recomendaciones reales que cubren otra cosa:**

| Recomendación | Qué cubre |
|---|---|
| **UIT-R BT.601** | **Definición estándar**: la digitalización del vídeo por componentes de 525 y 625 líneas |
| **UIT-R BT.2020** | **Ultra alta definición** |
| **UIT-R BT.2100** | **Alto rango dinámico** para televisión de alta y ultra alta definición |

**La cadena mnemotécnica**: **601 estándar · 709 alta · 2020 ultra alta · 2100 alto rango dinámico.**
Con esas cuatro se contestan las preguntas 91 y 7 y buena parte del tema 2.

**Y para la interfaz, la norma es de la SMPTE.** **La normativa internacional que define la señal de
vídeo HD 1080/50i es la SMPTE-274M.** Ésa es la respuesta oficial a la pregunta 67.

**Las tres opciones falsas:**

| Opción | Qué es |
|---|---|
| **ITU-R BT.601-5** | **Definición estándar**, no HD |
| **SMPTE-296M** | **La norma hermana de la 274M**, pero **para 1280 × 720**, no para 1080 |
| **R91-2004** | **Una recomendación de la Unión Europea de Radiodifusión**, no una norma de formato de imagen |

**La distinción que hay que fijar**: **SMPTE 274M es la de 1080; SMPTE 296M es la de 720.** El examen
pone las dos juntas, y **quien confunda el número marca la hermana equivocada**.

**Una declaración expresa**: **el texto de las normas SMPTE 274M y 296M no se ha consultado.** Son
normas de pago de una sociedad profesional estadounidense, y este proyecto no ha accedido a su
articulado. **La atribución de 1080 a la 274M y de 720 a la 296M descansa en la plantilla oficial y en
la literatura técnica corriente**, no en el texto de las normas.

## 6. Vídeo compuesto, por componentes y digital

**Las tres formas de llevar una señal de vídeo analógica o digital**, que es lo que la pregunta 71
pone a prueba:

| Señal | Cómo va | Cómo se transporta |
|---|---|---|
| **Compuesto** | **Luminancia y crominancia mezcladas en una sola señal**, con el color **modulado en amplitud sobre una subportadora** | Un solo cable |
| **Por componentes** | **Tres señales separadas**: luminancia y las dos diferencias de color | Tres cables, o un multipar |
| **Digital** | Muestreada y cuantificada, serializada | **Un coaxial de 75 Ω por SDI**, o fibra, o red |

**El tipo de señal de vídeo que utiliza la modulación de amplitud es el vídeo compuesto.** Ésa es la
respuesta oficial a la pregunta 71.

**Por qué**: en el sistema PAL —y en el NTSC— **la información de color se modula sobre una
subportadora que se suma a la luminancia**, y **esa modulación es en amplitud**, con la fase llevando
el tono y la amplitud llevando la saturación. **Eso es lo que define la señal compuesta**, y es de
donde vienen los defectos clásicos de la televisión analógica en color.

**Las tres opciones falsas:**

| Opción | Por qué no |
|---|---|
| «Señal de vídeo digital» | **En digital no hay modulación de amplitud de la crominancia**: hay muestras |
| «Señal de vídeo por componentes» | **Precisamente no modula**: lleva las tres señales separadas y en banda base |
| «Señal de vídeo 4K» | **No es un tipo de señal, es una resolución** |

**La opción d) es del tipo que este cuadernillo repite**: **mezclar una categoría con otra** —una
resolución donde se pide un tipo de señal—. **Se descarta sin saber nada de modulación.**

## 7. El *jitter*

**El *jitter* aplicado a una señal digital significa una cadena de bits con tiempos inestables.** Ésa
es la respuesta oficial a la pregunta 44.

**Qué es, en una frase**: **la variación del instante en que llega cada bit respecto de cuándo
debería llegar.** No cambia el valor de los bits: **cambia cuándo aparecen**.

**Por qué importa en una sala de edición**: el receptor de una señal digital **recupera el reloj de la
propia señal**. Si los flancos no llegan cuando toca, **el receptor decide mal dónde está cada bit**, y
el resultado no es una degradación suave sino **un corte**: la señal se ve o no se ve. **El vídeo
digital falla de golpe, y el *jitter* es una de las causas.**

**Las tres opciones falsas describen otras cosas reales:**

| Opción | Qué es en realidad |
|---|---|
| «Una señal con frecuencia modulada» | **Modulación**, que es una técnica de transmisión, no un defecto |
| «Un aumento en la amplitud de la señal» | **Ganancia** |
| «Un efecto de ruido aleatorio en la señal» | **Ruido**. **Es la trampa buena**: el *jitter* es ruido, pero **de fase, no de amplitud**, y lo que la opción describe es el ruido corriente |

**La palabra que resuelve la pregunta es «tiempos»**: **el *jitter* es un problema de reloj**, y sólo
una de las cuatro opciones habla de tiempo.

## 8. La compresión: intracuadro e intercuadro

**Comprimir vídeo es quitar información redundante**, y hay dos redundancias que quitar:

| Tipo | Qué aprovecha | Consecuencia para el montaje |
|---|---|---|
| **Compresión espacial** o **intracuadro** | **La redundancia dentro de cada imagen** | **Cada cuadro se decodifica solo**: el corte es exacto en cualquier punto |
| **Compresión temporal** o **intercuadro** | **La redundancia entre imágenes sucesivas** | **Un cuadro depende de otros**: hace falta el grupo entero para decodificar |

**El códec que utiliza compresión temporal es H.265.** Ésa es la respuesta oficial a la pregunta 47.

**Las tres opciones falsas son los tres códecs intracuadro que una sala de edición usa a diario:**

| Códec | Cómo comprime |
|---|---|
| **ProRes** | **Sólo intracuadro** |
| **DNxHR** | **Sólo intracuadro** |
| **JPEG 2000** | **Sólo intracuadro**: comprime cada imagen como una fotografía |

**Y ésa es exactamente la razón de que sean los códecs de montaje.** **Un códec intracuadro se puede
cortar en cualquier cuadro sin recalcular nada**, y por eso pesa más y va más rápido en la sala. **Un
códec intercuadro pesa mucho menos y es el de emisión y distribución**, pero **obliga a reconstruir el
grupo de imágenes para llegar a un cuadro cualquiera**.

**La regla de oficio que resume el epígrafe**: **para editar, intracuadro; para distribuir,
intercuadro.** Y la consecuencia práctica: **el material de cámara que llega en H.264 o H.265 se
transcodifica a ProRes o DNx antes de montar**, precisamente por eso.

## 9. Los códecs que el examen nombra

| Códec | Quién lo desarrolló | Qué es |
|---|---|---|
| **H.264 / AVC** | **UIT-T y MPEG**, conjuntamente | El estándar de compresión intercuadro más extendido |
| **H.265 / HEVC** | **UIT-T y MPEG**, conjuntamente | **Su sucesor**: la mitad de tasa de bits para la misma calidad |
| **ProRes** | **Apple** | Intracuadro, de montaje |
| **DNxHD y DNxHR** | **Avid** | Intracuadro, de montaje |
| **JPEG 2000** | **El grupo JPEG** | Intracuadro, **el del cine digital** |
| **MPEG-2** | **MPEG** | El de la televisión digital de primera generación y el DVD |

**Un archivo con códec H.265 es un archivo con un estándar de compresión de vídeo que admite vídeo
UHD 8K a velocidades de bits bajas para una transmisión más fluida, y puede aumentar su eficiencia de
codificación ahorrando hasta un 50 % de la tasa de bits que H.264.** Ésa es la respuesta oficial a la
pregunta 27.

**Las tres opciones falsas son la misma afirmación invertida**: dicen que el H.265 **no admite HDR**,
que tiene **peor calidad** o que tiene **peores algoritmos de seguimiento del movimiento**. **Las tres
son lo contrario de lo que es H.265**, que **mejora a H.264 en las tres cosas**. **Basta con saber que
H.265 es el sucesor y no el predecesor para descartarlas de golpe.**

**El códec que utiliza el estándar de difusión de cine digital es JPEG 2000.** Ésa es la respuesta
oficial a la pregunta 68.

**Las tres opciones falsas y por qué se caen**, que es una lección de vocabulario por sí sola:

| Opción | Qué es en realidad |
|---|---|
| **DPX** | **Un formato de imagen fija**, una por cuadro. **No es un códec de vídeo** |
| **MPEG-2** | **Sí es un códec**, pero **es el de la televisión digital y el DVD**, no el del cine digital |
| **MXF** | **No es un códec: es un contenedor.** Encapsula esencia y metadatos, y **lo que lleva dentro puede ser cualquier códec** |

**La distinción códec / contenedor es la que este cuadernillo más castiga**, y conviene tenerla fija:
**el códec dice cómo se comprime; el contenedor dice cómo se empaqueta.** **MXF, MOV y MP4 son
contenedores**; **H.264, ProRes y JPEG 2000 son códecs**. **Un fichero MXF puede llevar dentro
cualquiera de ellos.**

**El códec DNxHD lo desarrolló Avid.** Ésa es la respuesta oficial a la pregunta 96, y es coherente
con el resto del cuadernillo, que dedica un punto entero a Avid Media Composer. **Las tres opciones
falsas son las tres casas que sí desarrollaron otros códecs**: **Apple** hizo ProRes, **Blackmagic
Design** hizo el códec RAW de sus cámaras y **Adobe** hizo formatos de intercambio, pero **DNxHD es de
Avid**, y la propia sigla lo dice: es el códec de la arquitectura *Digital Nonlinear Extensible* de la
casa.

## 10. El código de tiempo: DF y NDF

**El código de tiempo es la etiqueta que numera cada cuadro** en horas, minutos, segundos y cuadros.
Es lo que permite localizar un punto exacto del material y **lo que sincroniza varias cámaras entre
sí**.

**Hay dos modalidades, y la diferencia sólo existe por una peculiaridad histórica:**

| Modalidad | Qué hace | Cuándo se usa |
|---|---|---|
| **NDF**, *non-drop frame* | **Cuenta todos los cuadros, sin saltarse ninguno** | **Cuando la cadencia es un número entero**: 24, 25, 30, 50 |
| **DF**, *drop frame* | **Se salta números de cuadro periódicamente** para que el código de tiempo coincida con el reloj de pared | **Cuando la cadencia no es entera**: 29,97 o 59,94 |

**En un sistema de televisión de 25 fps usaremos un código de tiempo NDF.** Ésa es la respuesta
oficial a la pregunta 84.

**Por qué, en una frase**: **25 es un número entero, así que veinticinco cuadros son exactamente un
segundo y no hay nada que corregir.** El *drop frame* nació en el sistema americano, cuya cadencia
real es **29,97 cuadros por segundo y no 30**: contando de treinta en treinta, **el código de tiempo se
adelanta al reloj unos tres segundos y medio por hora**, y el *drop frame* corrige esa deriva
saltándose números.

**El malentendido más común, que conviene deshacer**: **el *drop frame* no tira cuadros.** **Salta
números en la cuenta.** El material queda intacto; lo que cambia es **la etiqueta**.

**Las tres opciones falsas de la pregunta 84**: **DF** es la modalidad contraria y **no procede a 25
fps**; **«FD» y «FF», con las letras invertidas, no son modalidades de código de tiempo**, sino letras invertidas de las dos
anteriores. **Es un distractor de los que este cuadernillo construye barajando siglas.**

## 11. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 6 | Profundidad de bits en la fase 1 de UHD | b) 10 bits ✔ **·** sólo con la plantilla |
| 18 | Qué significa un muestreo 4:4:4:4 | a) RGB sin submuestreo más canal alfa ✔ |
| 27 | Qué es un archivo con códec H.265 | d) Admite UHD 8K y ahorra hasta un 50 % de tasa ✔ |
| 43 | Qué contamos en HD-SDI 1080 50i | d) 50 imágenes por segundo ✔ |
| 44 | Qué significa *jitter* en una señal digital | d) Una cadena de bits con tiempos inestables ✔ |
| 46 | Resolución espacial de 8K en 16:9 | d) 7.680 × 4.320 ✔ |
| 47 | Qué códec utiliza compresión temporal | a) H.265 ✔ |
| 65 | Relación de aspecto en UHD | a) 16:9 ✔ |
| 67 | Norma internacional que define HD 1080/50i | b) SMPTE-274M ✔ **·** sólo con la plantilla |
| 68 | Códec del estándar de cine digital | d) JPEG 2000 ✔ |
| 69 | Por qué es necesario el barrido entrelazado en PAL | d) Para evitar el parpadeo ✔ |
| 71 | Señal de vídeo que utiliza modulación de amplitud | c) Señal de vídeo compuesto ✔ |
| 84 | Código de tiempo en un sistema de 25 fps | a) NDF ✔ |
| 91 | Recomendación que afecta a la señal digital en HD | a) UIT-R BT.709 ✔ |
| 96 | Quién desarrolló el códec DNxHD | b) Avid ✔ |

**Las quince respuestas oficiales son correctas.**

**Y dos de las quince descansan sólo en la plantilla**: **la profundidad de bits de la fase 1 de UHD**,
que es una decisión de despliegue y no de la Recomendación, y **la atribución de la señal 1080/50i a
la norma SMPTE-274M**, cuyo texto no se ha consultado.

**Dos avisos de estudio.** **La pregunta 43 mide una sola distinción**: **50i son cincuenta campos y
veinticinco cuadros**, y la opción falsa dice «*frames*» donde la buena dice «imágenes». **Y la
pregunta 68 mete un contenedor entre los códecs**: quien no distinga MXF de JPEG 2000 tiene dos
opciones plausibles en lugar de una.

## 12. Trazabilidad

**Las fuentes técnicas que este tema cita:**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Segundo: organismo de normalización** | **Recomendación UIT-R BT.2020-2** | El Cuadro 1, con las resoluciones de 7.680 × 4.320 y 3.840 × 2.160 y el formato **«16:9»**, y el Cuadro 5, con el formato de codificación de **«10 ó 12 bits por componente»** |
| | **Recomendación UIT-R BT.709-6** | Su condición de recomendación de la alta definición |
| **Quinto: la plantilla oficial** | **Dos afirmaciones**: la profundidad de la fase 1 de UHD y la atribución de HD 1080/50i a la SMPTE-274M | Preguntas 6 y 67 |

**Una declaración expresa sobre lo que no se ha podido contrastar**, y son dos cosas distintas:

1. **La «fase 1» del despliegue de UHD no es un concepto de la Recomendación UIT-R BT.2020**, que
   admite tanto 10 como 12 bits. **La documentación del organismo de radiodifusión que definió esa
   fase no se ha consultado**, así que **la elección de 10 bits para ella descansa en la plantilla**,
   aunque el valor sea uno de los dos que la norma permite.
2. **El texto de las normas SMPTE 274M y 296M no se ha consultado**: son normas de pago de una
   sociedad profesional, y este proyecto no ha accedido a su articulado. **La atribución de 1.080
   líneas a la 274M y de 720 a la 296M descansa en la plantilla y en la literatura técnica
   corriente.**

**El resto del tema se sostiene con norma técnica delante o va como oficio y así se declara**: la
notación de los muestreos cromáticos, el reparto entre compresión intracuadro e intercuadro, la
distinción entre códec y contenedor, el funcionamiento del código de tiempo y la autoría de los
códecs de la industria **son vocabulario técnico asentado**, no doctrina de una fuente concreta.
