# Tema 10 del específico de Producción (Asistencia) · Imagen y sonido: captación y tratamiento

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Producción (Asistencia) · punto 10 |
| **Sirve para** | **Producción (Asistencia)** |
| **Fuente** | **Sin norma en el enunciado.** Se apoya en dos **recomendaciones UIT-R**, dos **reales decretos** y la documentación de la **AES**, y dice de cuál viene cada dato |
| **Identificador** | `UIT-R BT.601-7` · `UIT-R BT.2100-1` · `BOE-A-2010-927` · `BOE-A-2007-18400` |
| **Redacción que se estudia** | Las **recomendaciones UIT-R en la edición que cita el examen** —BT.601-7 de 03/2011 y BT.2100-1 de 06/2017—, y los **reales decretos en su texto vigente al 21/12/2022** |
| **Jerarquía de fuentes** | **Cinco niveles declarados**, del BOE a la plantilla oficial. El tema marca el nivel de cada afirmación, y **siete de las diecisiete preguntas tienen norma detrás** |
| **Extensión** | **5.260 palabras** |

<!-- /portada -->

> **Enunciado de la convocatoria (Anexo 2, temario específico de Producción, punto 10):**
> «IMAGEN Y SONIDO: Captación y tratamiento.»

**De dónde sale cada dato de este tema, y por qué hay que decirlo.** El enunciado **no cita
ninguna norma**, y no la cita porque no la hay: esto no es un tema jurídico. Pero eso no autoriza
a escribirlo de memoria. Se aplica la **jerarquía de fuentes declarada para el bloque específico**,
y el tema **dice de qué nivel viene cada afirmación**.

Tres organismos aparecen una y otra vez, y conviene presentarlos antes de abreviarlos. La **Unión
Internacional de Telecomunicaciones (UIT)** es el organismo de las Naciones Unidas para las
telecomunicaciones; su **Sector de Radiocomunicaciones (UIT-R)** publica **recomendaciones**
agrupadas en series, y la de radiodifusión de televisión (TV) es la **serie BT**. La **Audio
Engineering Society (AES)** es la asociación profesional que normaliza el audio. Y el **Código
Técnico de la Edificación (CTE)** se ordena en **documentos básicos (DB)**, de los que aquí
interesa el de protección frente al ruido, el **DB-HR**. Las normas españolas se citan por su
rango completo —**real decreto (RD)** y orden ministerial—, y los ficheros de las
recomendaciones, por su formato de documento portátil (**PDF**):

| Nivel | Qué se ha usado en este tema |
|---|---|
| **1 · Norma del BOE** | **Real Decreto 2032/2009**, unidades legales de medida, para el **ohmio**. **Documento Básico DB-HR** del Código Técnico de la Edificación, aprobado por el **Real Decreto 1371/2007**, para la **definición del tiempo de reverberación** |
| **2 · Organismo de normalización** | **Recomendación UIT-R BT.601-7 (03/2011)**, la antigua norma del Comité Consultivo Internacional de Radiocomunicaciones (**CCIR 601**), para la codificación digital de estudio. **Recomendación UIT-R BT.2100-1 (06/2017)** para la elevada gama dinámica. Ambas leídas **en español y en la edición exacta que cita el examen** |
| **3 · Documentación institucional** | La propia **AES** para la identidad de la interfaz digital de audio multicanal (**MADI**) |
| **5 · La plantilla oficial** | Lo que no sostiene ninguno de los anteriores y el tribunal ya ha dado por correcto: los **patrones polares**, los **tipos de micrófono por transductor**, el **N-1** y el **vectorscopio**. Va marcado en cada caso |

Además hay física —óptica y ondas— que no necesita norma porque **se demuestra**: la relación
entre distancia focal y profundidad de campo, o entre longitud de onda y tono. Ésa se explica
razonada, no citada.

---

<!-- indice -->

## Índice

- [1. La captación de la imagen: óptica](#1-la-captación-de-la-imagen-óptica)
  - [1.1 Distancia focal, diafragma y profundidad de campo](#11-distancia-focal-diafragma-y-profundidad-de-campo)
  - [1.2 Las cualidades de la luz que intervienen en la captación](#12-las-cualidades-de-la-luz-que-intervienen-en-la-captación)
- [2. De la luz a la señal: luminancia y crominancia](#2-de-la-luz-a-la-señal-luminancia-y-crominancia)
  - [2.1 Por qué se codifica en Y, C'B y C'R, y no en R, G, B](#21-por-qué-se-codifica-en-y-cb-y-cr-y-no-en-r-g-b)
  - [2.2 Qué es exactamente la luminancia](#22-qué-es-exactamente-la-luminancia)
  - [2.3 El submuestreo de color: qué significa 4:2:2](#23-el-submuestreo-de-color-qué-significa-422)
  - [2.4 Los parámetros de la BT.601-7 que conviene retener](#24-los-parámetros-de-la-bt601-7-que-conviene-retener)
- [3. La imagen de elevada gama dinámica](#3-la-imagen-de-elevada-gama-dinámica)
- [4. La medida de la señal de vídeo](#4-la-medida-de-la-señal-de-vídeo)
- [5. El sonido: la onda y sus magnitudes](#5-el-sonido-la-onda-y-sus-magnitudes)
  - [5.1 Frecuencia, longitud de onda y amplitud](#51-frecuencia-longitud-de-onda-y-amplitud)
  - [5.2 Trémolo, y con qué se confunde](#52-trémolo-y-con-qué-se-confunde)
  - [5.3 Reflexión, eco y reverberación](#53-reflexión-eco-y-reverberación)
  - [5.4 El tiempo de reverberación](#54-el-tiempo-de-reverberación)
- [6. El micrófono](#6-el-micrófono)
  - [6.1 Por su transductor](#61-por-su-transductor)
  - [6.2 Por su patrón polar](#62-por-su-patrón-polar)
  - [6.3 La impedancia](#63-la-impedancia)
- [7. La digitalización del sonido](#7-la-digitalización-del-sonido)
  - [7.1 Muestreo: el teorema de Nyquist](#71-muestreo-el-teorema-de-nyquist)
  - [7.2 Cuantificación](#72-cuantificación)
  - [7.3 Las interfaces de audio digital: AES3 y MADI](#73-las-interfaces-de-audio-digital-aes3-y-madi)
- [8. El retorno al reportero: la señal N-1](#8-el-retorno-al-reportero-la-señal-n-1)
- [9. Los datos que el examen ha preguntado](#9-los-datos-que-el-examen-ha-preguntado)
- [10. Trazabilidad](#10-trazabilidad)

<!-- /indice -->

## 1. La captación de la imagen: óptica

### 1.1 Distancia focal, diafragma y profundidad de campo

**Distancia focal** es la distancia entre el centro óptico del objetivo y el plano donde se forma
la imagen enfocada al infinito. Se mide en **milímetros**, y es lo que determina el **ángulo de
visión**: a menor focal, ángulo más ancho; a mayor focal, ángulo más estrecho y mayor
acercamiento aparente.

**Profundidad de campo** es la **zona por delante y por detrás del punto enfocado que se percibe
también nítida**. Depende de tres cosas, y conviene tenerlas separadas porque el examen sólo
pregunta por la primera:

| Si aumenta… | La profundidad de campo… |
|---|---|
| La **distancia focal** | **Disminuye** |
| El **número f** del diafragma (más cerrado) | **Aumenta** |
| La **distancia al sujeto** | **Aumenta** |

**La relación con la focal es inversa, y ésa es la que se ha preguntado**: **cuanto mayor sea la
distancia focal del objetivo, menor será la profundidad de campo**. Un teleobjetivo largo deja el
fondo desenfocado; un gran angular mantiene nítido casi todo.

El porqué es geométrico: al alargar la focal se **amplía la imagen del círculo de confusión**
—la mancha que forma un punto que no está exactamente en el plano de enfoque—, de modo que ese
punto deja de percibirse nítido antes. No hace falta memorizarlo como una regla suelta: **basta
recordar que el teleobjetivo «recorta» el fondo y lo funde**.

### 1.2 Las cualidades de la luz que intervienen en la captación

Cuatro comportamientos de la luz al encontrarse con un cuerpo, que conviene no confundir. **La
pregunta que el examen hace sobre ellos se cuenta en el tema 9**, donde vive la iluminación; aquí
se recogen porque sin ellos no se entiende qué llega al objetivo:

- **Reflexión**: la luz **rebota** en la superficie y vuelve al mismo medio.
- **Absorción**: la superficie **retiene** parte de la energía luminosa, y de ahí que un cuerpo se
  vea de un color u otro.
- **Refracción**: la luz **cambia de dirección** al pasar de un medio a otro de distinta densidad.
- **Transmisión**: la luz **atraviesa** un cuerpo no opaco y sale por el otro lado, **difusa o
  directamente**, según el material.

**Ésa última es la que se ha preguntado**, y la que más se confunde con la refracción: la
pregunta describe la luz que **atraviesa una superficie no opaca y cuyos rayos, al cambiar de
medio, pasan difusa o directamente**. Que atraviese y salga es **transmisión**; la refracción es
sólo el **desvío** que sufre al entrar. Es la propiedad en la que se apoyan los **difusores** y
las **gelatinas** de iluminación.

---

## 2. De la luz a la señal: luminancia y crominancia

### 2.1 Por qué se codifica en Y, C'B y C'R, y no en R, G, B

Un sistema de televisión en color capta **tres señales primarias** —rojo, verde y azul—, pero
**no las transmite así**. Las convierte en **una señal de luminancia** y **dos de diferencia de
color**, por dos razones que están en el propio texto de la recomendación:

- **Compatibilidad**: la señal de luminancia es, por sí sola, **la imagen en blanco y negro**.
- **Eficacia**: el ojo humano distingue mucho mejor las variaciones de brillo que las de color,
  así que las señales de color **pueden transmitirse con menos muestras** sin que se note.

La **Recomendación UIT-R BT.601-7** lo dice en su punto 1.2: «**La codificación digital debe
basarse en el empleo de una señal de luminancia y de dos señales de diferencia de color** (o, en
su caso, señales de rojo, verde y azul).»

### 2.2 Qué es exactamente la luminancia

**Luminancia (Y) es la señal en blanco y negro**: la que lleva el brillo y el detalle de la
imagen, y la que, si se emitiera sola, daría una imagen monocroma completa. **Crominancia** es lo
que llevan las otras dos señales: **la información de color**, en forma de **diferencias**
respecto de la luminancia.

Ésta es la distinción que pregunta el examen, y las cuatro opciones están medidas para que se
falle: «al brillo» es una descripción vaga —el brillo es una **magnitud**, no la señal—; «a la
diferencia de color» y «a la intensidad de color» son **la crominancia**, justo lo contrario. La
respuesta es **la señal en blanco y negro**.

**La ecuación, en la BT.601-7**, para los sistemas de definición convencional:

> **E'Y = 0,299 E'R + 0,587 E'G + 0,114 E'B**

Los tres coeficientes no son arbitrarios: reparten el peso según **cuánto contribuye cada
primario a la sensación de brillo**. El **verde pesa más de la mitad**; el azul, poco más de una
décima. De ahí salen las dos señales de diferencia de color: **E'R − E'Y** y **E'B − E'Y**.

**En elevada gama dinámica los coeficientes son otros.** La **Recomendación UIT-R BT.2100-1**,
que trabaja sobre la gama de colores ancha de la BT.2020, usa:

> **Y' = 0,2627 R' + 0,6780 G' + 0,0593 B'**

Es un dato fino, pero enseña algo que sí se pregunta de muchas formas: **los coeficientes
dependen de los primarios del sistema**, no son una constante de la naturaleza.

### 2.3 El submuestreo de color: qué significa 4:2:2

La nomenclatura de tres cifras dice **cuántas muestras de cada señal se toman en un bloque de
referencia de cuatro muestras de luminancia**:

| Notación | Qué significa |
|---|---|
| **4:4:4** | Por cada **cuatro** muestras de luminancia, **cuatro** de cada diferencia de color. Sin submuestreo |
| **4:2:2** | Por cada **cuatro** muestras de luminancia, **dos** de la diferencia de color rojo y **dos** de la azul. Se reduce la resolución de color **en horizontal**, no en vertical |
| **4:2:0** | Por cada cuatro de luminancia, **dos** de cada diferencia de color, y **alternando líneas**: se reduce también **en vertical** |

**La pregunta del examen es exactamente esa definición del 4:2:2**, y la respuesta oficial la
recoge palabra por palabra: «por cada cuatro muestras de luminancia se toman sólo **dos muestras
de la diferencia de color rojo y dos de azul**». Las opciones falsas cambian **rojo y azul por
amarillo y azul**, o invierten los papeles poniendo la crominancia como referencia.

**Y hay una advertencia sobre el enunciado.** Dice «la norma **CCIR 601**». La **CCIR** —Comité
Consultivo Internacional de Radiocomunicaciones— es **la antecesora del actual Sector de
Radiocomunicaciones de la UIT (UIT-R)**, de modo que aquella norma es hoy la **Recomendación
UIT-R BT.601**, cuya versión vigente es la **-7, de marzo de 2011**. Es la misma norma con otro
nombre, y así se cita en este tema.

### 2.4 Los parámetros de la BT.601-7 que conviene retener

Del **cuadro 3** de la recomendación, el de la relación **4:2:2**:

| Parámetro | Sistemas de 525 líneas | Sistemas de 625 líneas |
|---|---|---|
| Señales codificadas | **Y, C'R, C'B**, obtenidas de señales con **precorrección gamma** | igual |
| Muestras por **línea completa**: luminancia / cada diferencia de color | **858 / 429** | **864 / 432** |
| Muestras por **línea activa digital**: luminancia / cada diferencia de color | **720 / 360** | **720 / 360** |
| **Estructura de muestreo** | **Ortogonal**, repetitiva en cada línea, en cada trama y en cada imagen. Las muestras de C'R y C'B **coinciden con las impares** de Y | igual |
| **Frecuencia de muestreo**: luminancia / cada diferencia de color | **13,5 MHz / 6,75 MHz** | igual |
| **Codificación** | Modulación por impulsos codificados (**MIC**), **con cuantificación uniforme**, **8 o 10 bits** por muestra | igual |
| **Niveles** | Negro en **16**, blanco de cresta en **235** (8 bits) | igual |

Dos observaciones que salen de la propia tabla:

- **720 de luminancia y 360 de cada diferencia de color** en la línea activa: ahí está el 4:2:2,
  contado en muestras. Y **13,5 MHz frente a 6,75 MHz**: exactamente la mitad.
- La misma **frecuencia de 13,5 MHz sirve para 4:3 y para 16:9**, que es lo que la recomendación
  destaca en su propio resumen.

---

## 3. La imagen de elevada gama dinámica

La **Recomendación UIT-R BT.2100-1 (06/2017)** es la que el examen cita por su nombre y su fecha.
Regula los **parámetros de imagen de los sistemas de televisión de elevada gama dinámica**
(en inglés *high dynamic range television*, de donde salen las siglas **HDR** y **HDR-TV**) para
producción e intercambio internacional de programas.

**Qué es la elevada gama dinámica.** Un sistema HDR puede representar **más contraste**: negros
más profundos y **altas luces mucho más brillantes**, con más detalle en las dos puntas. Ésa es
la respuesta que el examen da por buena a la pregunta de qué significan las siglas HDR, y las
otras tres opciones —códecs de audio, formato de ingesta, refuerzo de la señal sonora— no tienen
nada que ver.

**Los dos métodos que especifica la recomendación**, y que hay que saber nombrar:

- **Cuantización perceptiva** (*perceptual quantization*), **PQ**.
- **Híbrido log-gamma** (*hybrid log-gamma*), **HLG**.

**Del cuadro 1, características espaciales y temporales de la imagen:**

| Parámetro | Valor |
|---|---|
| Forma del contenedor de imagen | **16:9** |
| Cómputo de píxeles | **7 680 × 4 320**, **3 840 × 2 160** y **1 920 × 1 080** |
| **Muestreo reticular** | **Ortogonal** |
| Formato de píxel | **1:1**, píxeles cuadrados |
| Orden de píxeles | De **izquierda a derecha** en cada fila, y las filas **de arriba abajo** |
| Frecuencia de trama (Hz) | 120, 120/1,001, 100, 60, 60/1,001, 50, 30, 30/1,001, 25, 24 y 24/1,001 |
| Formato de imagen | **Progresiva** |

**El «muestreo reticular ortogonal» es la pregunta literal del examen**, con tres distractores
—pentagonal, hexagonal, heptagonal— que no existen como estructuras de muestreo de televisión.
**Ortogonal** significa que las muestras se disponen en una **retícula rectangular**, alineadas
en filas y columnas y **repitiéndose en la misma posición** en cada línea y en cada imagen. Es la
misma estructura que ya fijaba la BT.601 para la definición convencional: **no es una novedad del
HDR**, y por eso la respuesta se puede razonar aunque no se haya leído la recomendación.

---

## 4. La medida de la señal de vídeo

Dos instrumentos, y el examen los ha preguntado dos veces, así que conviene la comparación
directa:

| | **Monitor de forma de onda** | **Vectorscopio** |
|---|---|---|
| Qué representa | La **amplitud** de la señal a lo largo de la línea | La señal de **color** en un plano polar |
| Qué se mide con él | **Luminancia**: niveles de negro y de blanco, contraste, si la señal se sale de rango | **Crominancia**: **tono** —el ángulo— y **saturación** —la distancia al centro— |
| Para qué se usa | Ajustar exposición y niveles | **Comprobar y ajustar la crominancia**, equilibrar cámaras entre sí, verificar barras de color |

**Las dos preguntas del examen son las dos caras de lo mismo**: cuál es el instrumento que mide
**el componente de color** de la señal —el **vectorscopio**— y qué es lo que ese instrumento
**comprueba y ajusta** —**la crominancia**—. Los distractores de la primera son revelador:
*colorburst* y *salva de color* son **la misma cosa** —la ráfaga de sincronismo de color—, y no
un instrumento; el generador sinusoidal tampoco mide nada.

**Nivel de la fuente.** Esto no lo fija ninguna norma leída para este tema: es **instrumentación
de uso común**, y las dos respuestas se apoyan en la plantilla oficial y en el uso profesional.
Lo que sí está en la BT.601-7 son **los niveles que el monitor de forma de onda comprueba**: negro
en **16** y blanco de cresta en **235** sobre 8 bits.

---

## 5. El sonido: la onda y sus magnitudes

### 5.1 Frecuencia, longitud de onda y amplitud

Tres magnitudes que el examen mezcla a propósito:

- **Frecuencia**: número de ciclos por segundo, en **hercios**. Determina el **tono**: a más
  frecuencia, **más agudo**.
- **Longitud de onda**: distancia que recorre la onda en un ciclo. Es **inversamente
  proporcional** a la frecuencia.
- **Amplitud**: magnitud de la variación de presión. Determina el **volumen**, no el tono.

De la relación inversa entre frecuencia y longitud de onda sale la respuesta a la pregunta de
**cuándo el sonido es más grave**: **con una longitud de onda larga**. Las otras tres opciones
son las tres maneras de equivocarse: «frecuencia alta» y «longitud corta» dan **agudo**, y
«amplitud alta» da **más volumen**, que no es lo mismo que más grave.

### 5.2 Trémolo, y con qué se confunde

**Trémolo** es la **fluctuación o variación periódica de la intensidad** —volumen o amplitud— de
un sonido, **mientras la frecuencia se mantiene constante**. Es un efecto de amplitud.

Conviene tenerlo junto a su pareja, porque quien confunda los dos falla las dos:

| | Qué varía | Qué se mantiene |
|---|---|---|
| **Trémolo** | La **intensidad** (amplitud) | La **frecuencia** |
| **Vibrato** | La **frecuencia** (tono) | La intensidad |

Los distractores del examen apuntan a otras tres cosas que sí existen y no son esto: la **potencia
máxima** que soporta un altavoz, el **acople** del micrófono y el **temblor de la imagen** en un
envío con mochila.

### 5.3 Reflexión, eco y reverberación

El fenómeno físico por el que **el sonido rebota en una superficie** es la **reflexión**. Lo que
el oyente percibe de esa reflexión depende del **retardo** con que le llega:

- **Eco**: la onda reflejada llega **lo bastante tarde** como para percibirse como **una
  repetición separada** del sonido original.
- **Reverberación**: las reflexiones llegan **tan seguidas** que no se distinguen una a una y se
  perciben como **una cola** que prolonga el sonido.

**La pregunta del examen** —«¿qué fenómeno ocurre cuando el sonido rebota en una superficie?»— da
por buena **el eco**, frente a *difracción de ondas*, *reflejo de luz* y *absorción*. Es la
respuesta que el tribunal considera correcta y con la que se acierta; el tema deja dicho, porque
es lo honesto, que **el nombre del fenómeno físico es la reflexión** y que el eco es **el efecto
audible** que produce cuando el retardo es suficiente. De las cuatro opciones, la única que
describe un rebote de sonido sigue siendo el eco: *reflejo de luz* no es sonido, la *absorción*
es lo contrario del rebote y la *difracción* es el rodeo de un obstáculo, no el rebote.

### 5.4 El tiempo de reverberación

**Definición, y ésta sí tiene fuente publicada en el BOE.** El **Documento Básico DB-HR
«Protección frente al ruido»** del Código Técnico de la Edificación, en su anejo de terminología:

> «**Tiempo de reverberación, T:** Tiempo, en s, necesario para que **el nivel de presión sonora
> disminuya 60 dB** después del cese de la fuente. En general es función de la frecuencia.»

**Sesenta decibelios.** Ése es el dato que pregunta el examen, y de ahí viene el nombre con el
que se conoce la magnitud en la práctica: **RT60**. La misma definición añade dos precisiones
útiles: que **depende de la frecuencia**, y que los valores límite se entienden como **la media de
los medidos a 500, 1000 y 2000 Hz**.

**Dos avisos sobre esta fuente**, que el tema da porque cambian su alcance:

1. **El DB-HR regula edificios, no platós.** Su ámbito son los edificios de uso residencial,
   docente, sanitario y administrativo. De aquí se toma **la definición del término**, que es la
   que usa la acústica en cualquier recinto, **no una exigencia aplicable a un estudio de
   televisión**.
2. Se ha leído el **texto publicado en el BOE en 2007**. El DB-HR se modificó después dos veces
   —**Real Decreto 1675/2008** y **Orden VIV/984/2009**—: el primero **no menciona la
   reverberación** y la segunda toca los **valores límite**, la fórmula de Sabine y el coeficiente
   de absorción, **pero no esta definición**.

**Por qué importa en un plató.** Un tiempo de reverberación alto emborrona la palabra y obliga a
acercar el micrófono; uno muy bajo deja el sonido «seco» y sin cuerpo. Se controla con
**absorción acústica** —el propio DB-HR la define como «cantidad de energía acústica, en m²,
absorbida por un objeto del campo acústico»— y por eso los platós llevan **paneles absorbentes,
moqueta y cortinajes**.

---

## 6. El micrófono

### 6.1 Por su transductor

| Tipo | Cómo funciona | Carácter |
|---|---|---|
| **Dinámico** | Una bobina móvil unida a la membrana se mueve dentro de un campo magnético y genera la señal | **Robusto y versátil**, no necesita alimentación, aguanta niveles altos |
| **De condensador** | La membrana forma una de las placas de un condensador; su movimiento varía la capacidad | Más **sensible** y con mejor respuesta, pero **necesita alimentación** (*phantom*) y es más delicado |
| **De cinta** | Una lámina metálica muy fina vibra dentro del campo magnético | Sonido cálido, **muy frágil** |

**La pregunta del examen** describe un micrófono que sirve «para captar tanto sonidos
unidireccionales como omnidireccionales, además de ser **versátil y duradero**», y la respuesta
oficial es el **dinámico**. Las dos palabras del enunciado —**versátil** y **duradero**— son las
que lo separan del de condensador y del de cinta, que son más sensibles pero más delicados.

**Nivel de la fuente**: esta clasificación es **uso profesional consolidado**, no norma leída para
este tema. Se recoge porque es la que maneja el tribunal.

### 6.2 Por su patrón polar

El **patrón o diagrama polar** representa **la sensibilidad del micrófono según la dirección** de
la que llega el sonido:

| Patrón | Por dónde recoge | Rasgo que lo identifica |
|---|---|---|
| **Omnidireccional** | **Los 360 grados**, con la misma sensibilidad en todas las direcciones | No tiene zona muerta |
| **Bidireccional** (figura de ocho) | **Frente y espalda, en la misma proporción**; rechaza los laterales | Simetría delante-detrás |
| **Cardioide** | Sobre todo por el frente; atenúa los laterales y **rechaza la espalda** | Una sola zona de rechazo, detrás |
| **Hipercardioide** | Más directivo que el cardioide, con **un pequeño lóbulo trasero** | Rechazo máximo no en la espalda, sino en los laterales traseros |
| **Cañón** (*shotgun*) | Muy directivo hacia el frente, con lóbulos laterales | Tubo de interferencia |

**Las dos preguntas del examen se contestan con esta tabla.** La primera pide el patrón con «más
sensibilidad en la parte **frontal y posterior en la misma proporción**»: eso es exactamente el
**bidireccional**, y ninguno de los otros tres, porque el hipercardioide tiene lóbulo trasero pero
**no del mismo tamaño** que el frontal. La segunda pregunta en cuántos grados recoge el
**omnidireccional**: **360**.

**Nivel de la fuente**: igual que la anterior, **uso profesional**. El propio enunciado del examen
llama a esta representación «diagrama o patrón polar», que es como se conoce.

### 6.3 La impedancia

**Impedancia** es la oposición que presenta un circuito al paso de la corriente alterna. Se mide
en **ohmios**, símbolo **Ω**, que el **Real Decreto 2032/2009** de unidades legales de medida
recoge como la unidad de **resistencia eléctrica**, con expresión **V/A**. El mismo real decreto
avala la grafía castellanizada: «amperio, culombio, faradio, hercio, julio, **ohmio**, voltio,
vatio».

En la práctica de un plató, la impedancia separa dos mundos:

- Los micrófonos **profesionales son de baja impedancia**, lo que permite **tiradas largas de
  cable** sin pérdida de agudos ni captación de ruido, y van por **cable balanceado con conector
  conector de tres contactos (**XLR**).
- Los de **alta impedancia** son de uso doméstico y **no admiten tiradas largas**.

Los tres distractores del examen son las tres unidades con las que se confunde: **kilohercios**
—frecuencia—, **voltios** —tensión— y **decibelios** —nivel—.

---

## 7. La digitalización del sonido

### 7.1 Muestreo: el teorema de Nyquist

Digitalizar una señal analógica es **medirla a intervalos regulares** —muestrear— y **asignar a
cada medida un valor numérico** —cuantificar—.

**La regla del muestreo**: para poder reconstruir la señal sin ambigüedad, **la frecuencia de
muestreo debe ser como mínimo el doble de la frecuencia máxima de la señal**. Es el **teorema de
muestreo**, atribuido a **Nyquist** y **Shannon**.

**Ésa es la pregunta del examen**, y las cuatro opciones juegan con dos ejes a la vez —*doble* o
*igual*, *mínima* o *máxima*—, de modo que sólo una combina bien las dos: **el doble de la máxima
frecuencia de la señal**.

**Qué pasa si no se cumple**: aparece el **aliasing** o solapamiento, y frecuencias que no
existían en el original se cuelan en la señal digitalizada. Por eso los conversores llevan
delante un **filtro paso bajo** —filtro *antialiasing*—. La **BT.601-7** lo recoge en su punto
1.3: «deben controlarse las características espectrales de las señales **para evitar el solape de
los diferentes espectros**, conservando al mismo tiempo la respuesta en la banda de paso».

**El teorema, aplicado, con el único ejemplo que este tema puede sostener en su fuente**: la
**BT.601-7** fija **13,5 MHz** de frecuencia de muestreo para la luminancia y **6,75 MHz** para
cada señal de diferencia de color, y exige delante los filtros que evitan el solape. Las
frecuencias de muestreo de audio de uso corriente en estudio responden a la misma regla, pero
**este tema no da su cifra**: no está en ninguna de las fuentes leídas, ninguna pregunta la pide,
y escribirla sería exactamente lo que el método prohíbe.

### 7.2 Cuantificación

La **profundidad de bits** determina **cuántos escalones** distintos puede tomar cada muestra, y
por tanto la **resolución de amplitud**. La BT.601-7 usa **8 o 10 bits por muestra** para la
luminancia y para cada diferencia de color. Cuantificar con pocos bits produce **ruido de
cuantificación**.

### 7.3 Las interfaces de audio digital: AES3 y MADI

En un centro de producción conviven dos interfaces de la **AES** —*Audio Engineering Society*—,
la asociación profesional que normaliza el audio:

- **AES3**, para **audio digital de dos canales**. Es el que se conoce comercialmente como
  **AES/EBU**, y en su versión no balanceada, **S/PDIF**.
- **AES10**, más conocido como **MADI** —*Multichannel Audio Digital Interface*—, para **audio
  digital multicanal**: decenas de canales por un solo cable **coaxial** o por **fibra óptica**.

**La pregunta del examen** pide qué es el protocolo MADI, y da por buena «**un estándar de la
asociación de audio especializada (AES), para la transmisión de audio digital multicanal**». Las
tres opciones falsas describen otras cosas reales: el **par trenzado**, el conector óptico
**TOSLINK** —que es S/PDIF, no MADI— y el **vídeo por coaxial**.

**Nivel de la fuente**: la propia **AES**, en la presentación de sus normas, enumera «**AES3**
(*2-channel digital audio*), **AES10 (MADI)**, AES14 (*analog XLR pin-out*), AES67 (*networked
audio*)». Es documentación institucional del organismo que normaliza —tercer nivel—: **el texto
completo de la AES10 está tras un muro de pago y no se ha podido leer**, así que este tema
**no afirma nada de su contenido interno**, sólo su identidad y su objeto.

---

## 8. El retorno al reportero: la señal N-1

En un directo con un reportero en exteriores hay que devolverle **el programa** para que oiga al
plató y pueda responder. Pero si se le devolviera el programa **entero**, se oiría a sí mismo con
el retardo del enlace, y eso hace imposible hablar.

**La solución es el N-1**: la señal que se envía al reportero es **la del programa menos su propia
aportación** —de ahí el nombre, *N menos uno*—. Se le manda **audio y vídeo del programa**, sin su
canal.

**Nivel de la fuente**: uso profesional. Los distractores del examen son otros tres retornos y
señales que también existen y que conviene no confundir: la **señal internacional** —el programa
sin la locución, para insertar doblajes—, la **copia estándar** de un negativo y la **señal
limpia** o *clean feed* sin rótulos.

---

## 9. Los datos que el examen ha preguntado

Los dos cuadernillos de Producción (Asistencia) traen **diecisiete preguntas** de esta materia
—**la segunda más preguntada del bloque específico**, sólo por detrás de escenografía e
iluminación—. Las diecisiete se contestan con el tema delante:

| Materia | Dato preguntado | Nivel de la fuente |
|---|---|---|
| Óptica | A **mayor distancia focal, menor profundidad de campo** | Física |
| Sonido | **N-1**: el programa **menos la propia aportación** del reportero | Plantilla oficial |
| Vídeo | **Luminancia** es **la señal en blanco y negro** | UIT-R BT.601-7 |
| Vídeo | **4:2:2**: por cada cuatro muestras de luminancia, **dos de diferencia de color rojo y dos de azul** | UIT-R BT.601-7 |
| Vídeo | **BT.2100-1**: el muestreo reticular es **ortogonal** | UIT-R BT.2100-1 |
| Vídeo | El **vectorscopio** mide el **componente de color** | Plantilla oficial |
| Vídeo | El vectorscopio comprueba y ajusta **la crominancia** | Plantilla oficial |
| Sonido | El rebote del sonido en una superficie: **eco** | Plantilla oficial |
| Sonido | **Trémolo**: variación periódica de la **intensidad**, con frecuencia constante | Plantilla oficial |
| Sonido | Tono más grave: **longitud de onda larga** | Física |
| Sonido | Tiempo de reverberación: caída de **60 dB** | DB-HR, Real Decreto 1371/2007 |
| Micrófono | Patrón con igual sensibilidad **delante y detrás**: **bidireccional** | Plantilla oficial |
| Micrófono | El **omnidireccional** recoge en **360º** | Plantilla oficial |
| Micrófono | Versátil y duradero: **dinámico** | Plantilla oficial |
| Micrófono | La impedancia se mide en **ohmios** | Real Decreto 2032/2009 |
| Digitalización | Muestreo: **el doble de la frecuencia máxima** | Teorema de muestreo |
| Audio digital | **MADI** es un estándar **de la AES**, multicanal | AES |

**Siete de las diecisiete tienen norma o recomendación detrás.** Las diez restantes son
vocabulario y práctica del oficio, y el tema **lo dice en cada una** en vez de disfrazarlas de
dato normativo.

**Lo que no se ha preguntado y conviene no descuidar**, porque está en las mismas fuentes ya
leídas: la **frecuencia de muestreo de 13,5 MHz** y las **720 muestras** de línea activa de la
BT.601-7; los **niveles 16 y 235** que comprueba el monitor de forma de onda; los **contenedores
de imagen** de la BT.2100-1 —**7 680 × 4 320**, **3 840 × 2 160** y **1 920 × 1 080**— y sus dos
métodos, **PQ** e **HLG**; y la diferencia entre **trémolo y vibrato**, que es la pareja natural
de una pregunta ya caída.

---

## 10. Trazabilidad

- **Recomendación UIT-R BT.601-7**, «Parámetros de codificación de televisión digital para
  estudios con formatos de imagen normal 4:3 y de pantalla ancha 16:9», **edición 03/2011**,
  **versión en español**, descargada de la biblioteca pública de la UIT el **2 de septiembre de
  2026**. Es la norma que el examen llama **CCIR 601**.
- **Recomendación UIT-R BT.2100-1**, «Valores de los parámetros de imagen de los sistemas de
  televisión de elevada gama dinámica para la producción y el intercambio internacional de
  programas», **edición 06/2017**, **versión en español**, misma procedencia y misma fecha. Es
  **la edición exacta que cita el enunciado del examen**.
- **Real Decreto 2032/2009**, de 30 de diciembre, por el que se establecen las unidades legales de
  medida, `BOE-A-2010-927`, leído en su texto consolidado **a 21 de diciembre de 2022**.
- **Real Decreto 1371/2007**, de 19 de octubre, que aprueba el Documento Básico **DB-HR
  «Protección frente al ruido»** del Código Técnico de la Edificación, `BOE-A-2007-18400`, leído
  en el **texto publicado en el BOE núm. 254, de 23 de octubre de 2007**. Se han revisado sus dos
  modificaciones posteriores —**RD 1675/2008** y **Orden VIV/984/2009**— y **ninguna toca la
  definición** que aquí se cita.
- **AES**, presentación de sus normas en `aes.org`, leída el **2 de septiembre de 2026**, para la
  identidad de **AES3** y **AES10 (MADI)**. **El texto de la AES10 no se ha podido leer**: está
  tras un muro de pago. El tema no afirma nada de su contenido.

**Una corrección que hay que dejar escrita.** La extracción automática de texto del PDF de la
BT.601-7 daba «**16,75 MHz**» como frecuencia de muestreo de cada señal de diferencia de color.
Es falso: la cifra real es **6,75 MHz**, y el «1» venía pegado de la fila superior de la tabla. Se
detectó porque **6,75 es la mitad exacta de 13,5**, como exige el 4:2:2, y **se comprobó
recortando y ampliando esa celda del PDF para leerla a ojo**. Queda anotado porque enseña algo
sobre este nivel de la jerarquía: **con una norma técnica en PDF, el texto extraído no es la
fuente; la página lo es**.

**Lo que este tema no puede sostener y por eso no afirma:**

- **No hay norma leída** para los patrones polares, los tipos de micrófono por transductor, el
  vectorscopio ni el N-1. Se recogen porque son **uso profesional consolidado** y porque **el
  tribunal ya los ha dado por correctos**, y el tema lo marca en cada caso.
- La respuesta oficial a «qué fenómeno ocurre cuando el sonido rebota» es **el eco**. El tema la
  recoge y **añade** que el fenómeno físico se llama **reflexión**, sin cambiar la respuesta:
  ninguna de las otras tres opciones describe un rebote de sonido.
- **La AES10 no se ha leído.** Sólo se afirma **qué es** —una norma de la AES, para audio digital
  multicanal—, que es lo que la propia AES publica.
