# Tema 3 del específico de Ingeniería Técnica · Telecomunicación · La señal audiovisual y su sincronización

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 3 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma del boletín.** Su materia son las normas técnicas de la interfaz digital serie y del audio digital, **tras muro de pago**, así que **va como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Tercer banco** | **Catorce preguntas.** Seis son de la interfaz digital serie y sus generaciones, y **cuatro se deducen de una sola cifra**: cada generación dobla la anterior |
| **Extensión** | **3.663 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la interfaz digital serie (**SDI**), en sus
generaciones de alta definición (**HD-SDI**), de tres, seis y doce gigabits por segundo (**3G-SDI**,
**6G-SDI** y **12G-SDI**); la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**), que publica las
normas **SMPTE 259M**, **292M**, **311M** y **424M**; la Sociedad de Ingeniería de Audio (**AES**),
que publica **AES10** —que es la interfaz digital de audio multicanal, **MADI**— y **AES11**; el
comienzo y el fin del vídeo activo (**SAV** y **EAV**); la interfaz serie asíncrona (**ASI**); la
interfaz de transporte de datos serie (**SDTI**); el sistema de línea alternada en fase (**PAL**); las
componentes de luminancia y diferencia de color (**Y**, **Pb** y **Pr**); la codificación sin retorno
a cero (**NRZ**) y con retorno a cero (**RZ**); el conector coaxial de bayoneta (**BNC**); la matriz
de gráficos de vídeo (**VGA**), la interfaz visual digital (**DVI**), la interfaz multimedia de alta
definición (**HDMI**) y el **DisplayPort** (**DP**); los gigabits por segundo (**Gbps**) y los
megahercios (**MHz**); y la ultraalta definición (**UHD**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 3):
> «Señal audiovisual: Señal video SDI. Normativas (SMPTE 259M, 292M, 424M, etc.). Señal de audio AES.
> Señales de sincronización. BB, TRILEVEL, AES11, Word clock, etc.»

**Catorce preguntas: el tercer banco de la ocupación.** **Y es el punto que más distingue a un
ingeniero de televisión de un ingeniero de telecomunicación general**: **su materia no se estudia en
ninguna escuela, se aprende en una instalación.**

**Su reparto**: **seis preguntas son de la interfaz digital serie y sus generaciones**, **tres de
señales de sincronismo y medida**, **dos de cableado**, **dos de interfaces de vídeo** y **una de
televisión analógica.**

<!-- indice -->

## Índice

- [1. La interfaz digital serie y su escalera](#1-la-interfaz-digital-serie-y-su-escalera)
- [2. Cómo va montada la trama](#2-cómo-va-montada-la-trama)
- [3. La codificación y la medida](#3-la-codificación-y-la-medida)
- [4. Lo que cabe por el mismo cable](#4-lo-que-cabe-por-el-mismo-cable)
- [5. Las señales de sincronización](#5-las-señales-de-sincronización)
- [6. El cableado de cámara](#6-el-cableado-de-cámara)
- [7. Las interfaces de vídeo del mundo informático](#7-las-interfaces-de-vídeo-del-mundo-informático)
- [8. Lo que queda de la televisión analógica](#8-lo-que-queda-de-la-televisión-analógica)
- [9. Los datos que el examen ha preguntado](#9-los-datos-que-el-examen-ha-preguntado)
- [10. Trazabilidad](#10-trazabilidad)

<!-- /indice -->

## 1. La interfaz digital serie y su escalera

**Ésta es la tabla del punto, y de ella salen cuatro preguntas:**

| Norma | Nombre corriente | Caudal | Qué transporta |
|---|---|---|---|
| **SMPTE 259M** | **SD-SDI** | **270 Mbps** | **Definición estándar** |
| **SMPTE 292M** | **HD-SDI** | **1,485 Gbps** ✔ | **Alta definición hasta 1080i y 720p** |
| **SMPTE 424M** | **3G-SDI** | **2,970 Gbps** | **1080p a 50 y 60 imágenes** |
| **SMPTE 2081** | **6G-SDI** | **5,940 Gbps** | **2160p hasta 30 imágenes** ✔ |
| **SMPTE 2082** | **12G-SDI** | **11,880 Gbps** | **2160p hasta 60 imágenes** ✔ |

**La pregunta 8**: **la tasa de bits de la señal de vídeo de alta definición según la norma SMPTE-292M
es 1,485 Gbps.** Ésa es la respuesta oficial.

**La pregunta 66**: **la normativa SMPTE-292M especifica la interfaz digital serie de alta definición
a 1,5 Gbps.** Ésa es la respuesta oficial.

---

**Son la misma norma preguntada dos veces**, y **conviene ver que las dos respuestas no dicen el mismo
número**: **una da la cifra exacta y la otra la redondea.** **Eso no es una contradicción: es que la
primera pregunta pide el caudal y la segunda pide qué especifica la norma**, y en el sector esa
interfaz se llama «uno y medio».

**Y la relación numérica que hace innecesario memorizar la escalera entera**: **cada generación
DOBLA la anterior**, salvo el primer salto:

| De | A | Relación |
|---|---|---|
| **1,485** | **2,970** | **El doble** |
| **2,970** | **5,940** | **El doble** |
| **5,940** | **11,880** | **El doble** |

**Sabiendo 1,485 se deducen las tres siguientes.** **Y sabiendo que la cifra exacta lleva el factor
1000/1001 de las cadencias fraccionarias, se entiende por qué no es 1,5 redondo.**

**La pregunta 46**: **la señal que se puede transmitir por la interfaz de seis gigabits es 2160p30.**
Ésa es la respuesta oficial.

---

**Se resuelve con una cuenta, no con memoria**: **2160p30 necesita aproximadamente cuatro veces lo que
1080p30**, y **cuatro veces 1,485 son 5,94**, que es justo el caudal de esa generación.

**Las tres opciones falsas se descartan una a una:**

| Opción | Por qué no cabe |
|---|---|
| **2160p120** | **Necesitaría cuatro veces más: es materia de la generación siguiente y aun así apurada** |
| **2160p60** | **Necesita el doble: es lo que lleva la de doce gigabits** |
| **1080p150** | **No es una cadencia normalizada de televisión** |
| **2160p30** | **Cabe justo** ✔ |

**La pregunta 59**: **los estudios de producción en ultraalta definición usan la interfaz de doce
gigabits en lugar de la de tres porque puede transmitir sin comprimir señales de 4K en un solo
cable.** Ésa es la respuesta oficial.

---

**Y la palabra que decide es «un solo cable»**: **la alternativa era llevar la misma señal por CUATRO
cables de tres gigabits**, cada uno con un cuadrante o una imagen de la secuencia. **Eso multiplica
por cuatro el cableado, las matrices y los puntos de fallo.**

**Las tres opciones falsas y por qué caen:**

| Opción | Por qué es falsa |
|---|---|
| **Para reducir la longitud de los cables** | **Es al revés**: a más caudal, MENOS alcance por el mismo coaxial |
| **Porque es compatible con señales de definición estándar y alta** | **Cierto, pero no es la razón**: la de tres gigabits también lo es |
| **Porque usa modulación sin retorno a cero** | **Cierto, y lo usan todas las generaciones**: no distingue nada |

**El aviso de oficio que se deriva y que la pregunta no cubre**: **el alcance baja con el caudal.**
**Donde una señal de definición estándar llegaba a más de doscientos metros, una de doce gigabits no
pasa de unas decenas**, y **por eso las instalaciones nuevas de ultraalta definición van a fibra o a
red**, que es el tema 7.

## 2. Cómo va montada la trama

**La pregunta 7**: **EAV son las siglas en inglés de fin de vídeo activo.** Ésa es la respuesta
oficial.

---

**Y conviene ver la pareja completa, porque el examen puede pedir la otra:**

| Marca | Qué significa | Dónde va |
|---|---|---|
| **SAV** | **Comienzo del vídeo activo** | **Antes de la parte visible de la línea** |
| **EAV** | **Fin del vídeo activo** ✔ | **Después de la parte visible de la línea** |

**Para qué sirven, que es lo que da sentido a las siglas**: **la interfaz serie no lleva sincronismos
separados como la analógica.** **Los sincronismos van DENTRO de la propia trama, como códigos
reservados**, y **esas dos marcas son las que dicen dónde empieza y dónde acaba la imagen de cada
línea.**

**Y lo que va entre el fin de una y el comienzo de la siguiente es el intervalo de borrado
horizontal**, **que es exactamente donde se mete el audio incrustado, el código de tiempo y los datos
auxiliares.** **Ésa es la razón de que un solo coaxial lleve vídeo, dieciséis canales de audio y datos
a la vez.**

**La opción falsa «duración de vídeo activo» es la buena**, porque **existe un parámetro con ese
nombre**: **lo que la sigla nombra es el FIN, no la duración.**

## 3. La codificación y la medida

**La pregunta 41**: **en la interfaz digital serie se utiliza codificación sin retorno a cero.** Ésa es
la respuesta oficial.

---

**Y hay que precisar lo que la respuesta abrevia**: **la interfaz usa sin retorno a cero INVERTIDO,
con aleatorización previa.** **De las cuatro opciones ofrecidas, la marcada es la única de esa
familia**, y se marca.

**Las cuatro codificaciones de la pregunta:**

| Codificación | Cómo representa los bits | Rasgo |
|---|---|---|
| **Sin retorno a cero** | **Un nivel por bit, sin volver a cero entre ellos** ✔ | **Aprovecha el ancho de banda; necesita aleatorización para no perder el reloj** |
| **Con retorno a cero** | **Vuelve a cero entre bits** | **Gasta el doble de ancho de banda** |
| **Manchester** | **Una transición en medio de cada bit** | **Lleva el reloj dentro; gasta el doble** |
| **Bifase** | **Familia de la anterior** | **Se usa en el código de tiempo longitudinal** |

**Por qué hace falta aleatorizar**: **una secuencia larga de ceros o de unos no produce ninguna
transición**, y **el receptor recupera el reloj DE las transiciones.** **Sin ellas se pierde la
sincronía.** **La aleatorización garantiza que las haya**, sin añadir bits.

**La pregunta 55**: **en un diagrama de ojo se puede analizar el jitter.** Ésa es la respuesta oficial.

---

**Qué es un diagrama de ojo**: **la superposición en pantalla de muchos periodos de bit, uno encima de
otro.** **Lo que dibuja parece un ojo**, y **de su forma se leen dos cosas:**

| Qué se mira | Qué dice |
|---|---|
| **La apertura VERTICAL del ojo** | **El margen de amplitud frente al ruido** |
| **La apertura HORIZONTAL, o grosor de los cruces** | **El jitter: la inestabilidad temporal del reloj** ✔ |

**Y las tres opciones falsas son medidas reales de otro instrumento**: **la amplitud y el ruido de las
componentes se miden en un monitor de forma de onda**, y **el caudal es un dato de la norma, no algo
que se mida en un ojo.**

**Qué es el jitter y por qué importa tanto en una instalación**: **la variación del instante en que
llega cada transición.** **Si es mayor que el margen del receptor, éste muestrea en el sitio
equivocado y aparecen errores**, que en vídeo se ven como cortes o como imagen congelada, no como
ruido. **Es un fallo de todo o nada, y por eso se mide antes de que ocurra.**

## 4. Lo que cabe por el mismo cable

**La pregunta 19**: **sí es posible utilizar un distribuidor de vídeo digital serie para distribuir una
señal de interfaz serie asíncrona.** Ésa es la respuesta oficial.

---

**Y la razón es que las dos comparten la capa física**: **el mismo coaxial de 75 ohmios, el mismo
conector y el mismo nivel de señal.** **Lo que cambia es lo que va dentro:**

| | **Interfaz digital serie** | **Interfaz serie asíncrona** |
|---|---|---|
| **Qué transporta** | **Vídeo sin comprimir** | **Un flujo de transporte comprimido** |
| **Caudal** | **Fijo, el de la norma** | **Variable, hasta 270 Mbps** |
| **Capa física** | **Coaxial de 75 ohmios** | **La misma** ✔ |

**Las tres opciones falsas afirman una incompatibilidad que no existe**, y **la que habla de caudal
distinto es la trampa fina**: **el caudal SÍ es distinto y aun así el distribuidor funciona**, porque
**un distribuidor no interpreta la señal: la reamplifica.**

**El matiz de oficio que conviene añadir**: **un distribuidor REGENERADOR sí puede fallar**, porque
reconstruye la trama y espera la estructura de vídeo. **Un distribuidor sencillo, que sólo amplifica,
pasa cualquiera de las dos.** **La respuesta oficial es correcta y el temario añade dónde está el
límite.**

**La pregunta 33**: **la impedancia de una conexión coaxial de bayoneta para vídeo digital serie es 75
ohmios.** Ésa es la respuesta oficial.

---

**Y es la cifra que separa el mundo del vídeo del mundo de la radiofrecuencia**, que conviene
aprender junta:

| Impedancia | Dónde |
|---|---|
| **50 ohmios** | **Radiofrecuencia, instrumentación, redes antiguas** |
| **75 ohmios** | **Vídeo y televisión** ✔ |
| **110 ohmios** | **Audio digital por par simétrico** |
| **600 ohmios** | **Audio analógico antiguo, líneas telefónicas** |

**El aviso que hace útil el dato**: **el conector de bayoneta existe en las dos impedancias y se
parecen mucho.** **Poner uno de 50 en una línea de vídeo produce una reflexión** que en definición
estándar apenas se nota y **en doce gigabits tumba el enlace.** **A más caudal, menos tolerancia.**

**La pregunta 74**: **la interfaz de transporte de datos serie es una interfaz de transporte de datos
serie con velocidad hasta cuatro veces la velocidad de reproducción en algunos equipos.** Ésa es la
respuesta oficial.

---

**Qué es y para qué se inventó**: **una manera de mandar material COMPRIMIDO por la misma
infraestructura de vídeo digital serie**, y **más deprisa que en tiempo real.** **Eso permitía copiar
una cinta a cuatro veces su velocidad entre dos equipos por el coaxial que ya estaba tendido.**

**Las tres opciones falsas juegan con dos palabras**: **serie o paralelo, y cuántas veces la
velocidad.** **La regla que las descarta: es SERIE —como todo lo que va por coaxial— y el factor
corriente es CUATRO.**

## 5. Las señales de sincronización

**El enunciado las nombra expresamente y la pregunta 35 las pide.** **Ésta es la tabla:**

| Señal | Qué sincroniza | Dónde se usa |
|---|---|---|
| **Negro de barras** | **El vídeo de toda la instalación**, con sincronismos de dos niveles | **Instalaciones de definición estándar y mixtas** |
| **Tres niveles** | **Lo mismo, con sincronismos de tres niveles** | **Instalaciones de alta definición** |
| **AES11** | **El audio digital** | **Referencia de audio de la instalación** |
| **Reloj de palabra** | **Cada muestra de audio** | **Enlaces cortos entre equipos de audio** |
| **Tiempo de precisión** | **Todo, sobre red** | **Instalaciones sobre red del tema 7** |

**La pregunta 35 es negativa**: **de las señales enumeradas, la que NO se utiliza para sincronización
es AES10.** Ésa es la respuesta oficial.

---

**Y la razón es que esa norma es MADI**: **transporte de 64 canales de audio**, no referencia de
tiempo. **Está desarrollada en el tema 12.**

**La regla que la contesta sin memorizar los números**: **tres de las cuatro opciones sólo llevan
tiempo y una lleva audio.** **La que lleva audio es la intrusa.**

**Y el aviso de instalación que este epígrafe deja**: **la referencia de vídeo y la de audio tienen que
estar BLOQUEADAS entre sí.** **Si el reloj de audio deriva respecto al de vídeo, aparecen
deslizamientos** que se oyen como chasquidos periódicos y que **son de los fallos más difíciles de
localizar**, porque tardan horas en manifestarse.

## 6. El cableado de cámara

**La pregunta 31**: **el cable SMPTE 311M es un cable híbrido de fibra óptica para cámaras que
transporta vídeo, audio, control y alimentación eléctrica.** Ésa es la respuesta oficial.

---

**Y las cuatro opciones son una combinación de dos variables**, lo que hace la pregunta un ejercicio
limpio:

| Variable | Opciones |
|---|---|
| **Medio** | **Triaxial o fibra híbrida** |
| **Qué lleva** | **Con alimentación o sin ella** |

**La respuesta correcta es fibra CON alimentación**, y **conviene entender por qué esa combinación
existe**: **una cámara de estudio necesita las cuatro cosas por un solo cable**, porque **tender uno
solo hasta una grada o un plató ya es bastante trabajo.** **El cable lleva dos fibras monomodo para la
señal y dos conductores de cobre para la corriente**, y de ahí el nombre de híbrido.

**Y la comparación con lo que sustituyó, que es lo preguntable de lo que no ha caído:**

| | **Triaxial** | **Híbrido de fibra** |
|---|---|---|
| **Medio** | **Cobre, tres capas concéntricas** | **Dos fibras más dos conductores** ✔ |
| **Alcance** | **Cientos de metros, con pérdida de calidad** | **Kilómetros, sin degradar** |
| **Qué lleva** | **Vídeo, audio, control y alimentación** | **Lo mismo** |
| **Peso y manejo** | **Pesado y rígido** | **Más ligero, pero el conector es delicado** |

**El aviso de oficio que conviene llevar**: **el conector de ese cable es la pieza más frágil y más
cara de una unidad móvil.** **Se limpia con material específico antes de cada conexión**, y **una mota
de polvo en la cara de la fibra basta para que la cámara no dé imagen.**

## 7. Las interfaces de vídeo del mundo informático

**La pregunta 82**: **la interfaz que puede transmitir tanto señal de vídeo analógica como digital es
la interfaz visual digital.** Ésa es la respuesta oficial.

---

**Y es la misma distinción que el tema 18 del específico de Diseño Gráfico plantea al revés:**

| Interfaz | Vídeo | Audio | Rasgo |
|---|---|---|---|
| **Matriz de gráficos de vídeo** | **Sólo analógico** | **No** | **La antigua de quince patillas** |
| **Interfaz visual digital** | **Analógico Y digital**, según la variante ✔ | **No** | **Nació en la transición: hay variante analógica, digital y mixta** |
| **Interfaz multimedia de alta definición** | **Sólo digital** | **Sí** | **El estándar del equipo doméstico** |
| **DisplayPort** | **Sólo digital** | **Sí** | **El del mundo informático, con retención mecánica** |

**La regla que la contesta**: **de las cuatro, una es sólo analógica, dos son sólo digitales y una es
las dos.** **La que nació en la transición entre los dos mundos es la que lleva las dos.**

## 8. Lo que queda de la televisión analógica

**La pregunta 13**: **el valor de la frecuencia usada en la ráfaga de la señal del sistema de línea
alternada en fase es 4,43 MHz.** Ésa es la respuesta oficial.

---

**Es memoria de una cifra histórica**, y **conviene saber qué es esa ráfaga para que el número
signifique algo**: **unos ciclos de la subportadora de color que se mandan en cada línea, antes de la
imagen, para que el receptor sepa con qué fase y con qué frecuencia demodular el color.**

**Sin ella no hay color**, y de ahí que la frecuencia sea un dato de norma y no un ajuste.

| Sistema | Subportadora de color |
|---|---|
| **Sistema de línea alternada en fase** | **4,43 MHz** ✔ |
| **Sistema estadounidense** | **3,58 MHz** |

**Las tres opciones falsas son frecuencias reales de otras cosas**: **10,7 megahercios es la
frecuencia intermedia de un receptor de frecuencia modulada** y **21,4 es su doble**, usada también
como intermedia. **Ninguna tiene que ver con el color.**

**Por qué esto sigue en un temario de 2022**: **porque las instalaciones conservan referencia de negro
de barras**, que es una señal analógica con esa subportadora dentro, **y porque los equipos de medida
la usan.** **La emisión analógica se apagó; la referencia no.**

## 9. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 7 | Qué significan las siglas del fin de vídeo activo | c) Fin de vídeo activo ✔ |
| 8 | Tasa de bits de la norma SMPTE-292M | a) 1,485 Gbps ✔ |
| 13 | Frecuencia de la ráfaga de color analógica | c) 4,43 MHz ✔ |
| 19 | Si un distribuidor de vídeo sirve para una señal asíncrona | b) Sí, es posible ✔ |
| 31 | Qué es el cable SMPTE 311M | d) Fibra híbrida con vídeo, audio, control y alimentación ✔ |
| 33 | Impedancia de una conexión coaxial de vídeo | c) 75 ohmios ✔ |
| 35 | Cuál NO se usa para sincronización | a) AES10 ✔ |
| 41 | Codificación de bit de la interfaz digital serie | a) Sin retorno a cero ✔ **·** con precisión |
| 46 | Qué señal cabe por la interfaz de seis gigabits | d) 2160p30 ✔ |
| 55 | Qué se analiza en un diagrama de ojo | a) Jitter ✔ |
| 59 | Por qué se usa la interfaz de doce gigabits en ultraalta definición | d) Transmite 4K sin comprimir en un solo cable ✔ |
| 66 | Qué especifica la norma SMPTE-292M | c) Interfaz de alta definición a 1,5 Gbps ✔ |
| 74 | Qué es la interfaz de transporte de datos serie | c) Transporte serie hasta cuatro veces la velocidad ✔ |
| 82 | Qué interfaz lleva vídeo analógico y digital | b) La interfaz visual digital ✔ |

**Las catorce respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **Una lleva
precisión declarada**: la 41, cuya codificación es, en rigor, sin retorno a cero invertido y
aleatorizado.

**El aviso de estudio**: **la escalera de caudales contesta cuatro preguntas y se deduce de una sola
cifra, porque cada generación dobla la anterior.** **Es lo más rentable del punto.**

## 10. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **Las normas de la Sociedad de Ingenieros de Cine y Televisión y de la Sociedad de Ingeniería de
   Audio que este tema nombra no se han consultado**: su texto está tras un muro de pago. **Los
   caudales, las impedancias y el cometido de cada una son de uso universal en el sector**, y
   **coinciden con las respuestas oficiales.**
2. **La precisión sobre la pregunta 41 es del temario, no una impugnación**: **la interfaz usa sin
   retorno a cero INVERTIDO y con aleatorización previa**, y **de las cuatro opciones ofrecidas la
   marcada es la única de esa familia.**
3. **El matiz sobre la pregunta 19 tampoco lo es**: **la respuesta oficial es correcta para un
   distribuidor que amplifica**, y **el temario añade que uno regenerador puede comportarse de otro
   modo**, que es observación de oficio.
4. **Los alcances de cada generación de la interfaz, la fragilidad del conector de fibra híbrida y el
   aviso sobre el bloqueo entre referencias son oficio de instalación**, y **ninguna respuesta oficial
   depende de ellos.**
5. **Las frecuencias de subportadora de los dos sistemas analógicos y las frecuencias intermedias de
   las opciones falsas son datos de uso corriente**, dados como referencia. **La única que una
   respuesta oficial exige es 4,43 megahercios.**

**El resto del tema va como oficio y así se declara**: la relación de doblado entre generaciones, el
razonamiento que descarta las tres cadencias imposibles, la explicación de por qué el alcance baja con
el caudal, el cometido del intervalo de borrado horizontal, la razón de que haya que aleatorizar, la
lectura de las dos aperturas del diagrama de ojo, la comparación entre triaxial y fibra híbrida y la
razón de que la referencia analógica siga viva. **Nada de eso está en un boletín oficial ni en una
norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
