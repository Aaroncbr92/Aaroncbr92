# Tema 11 del específico de Sonido · Líneas y conexiones

Los términos y siglas de este tema, presentados de entrada: el conector de tres polos con anillo de
bloqueo (**XLR**); el panel de conexiones (*patch panel*) y su latiguillo (*patch cord*); el reparto
de una señal a varias salidas (*splitter*); la alimentación fantasma (*phantom*) de 48 voltios y la
alimentación por hilos (**A-B** o *Tonader*); la norma de audio digital de dos canales de la Sociedad
de Ingeniería de Audio (**AES3**), y la propia sociedad (**AES**, *Audio Engineering Society*); el
cable de par trenzado por categorías (**Cat5**, **Cat5e**, **Cat6**); el protocolo **Dante**, que el
tema 16 desarrolla; el atenuador de entrada (**PAD**); y la diafonía o paso de señal entre canales
vecinos (*crosstalk*).

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 9):
> «LÍNEAS Y CONEXIONES. Transmisión de sonido. Matrices de conmutación. Conectores: Tipos,
> características y funcionalidad.»

**Ocho preguntas: el tercer banco de esta ocupación**, empatado con el de micrófonos. **Y el punto más
puramente de oficio de los diecisiete**: **son ocho preguntas sobre por dónde va la señal y con qué
cable.**

**Nada de esto se deduce.** **Un pin de un conector, una impedancia de cable, una longitud máxima y
una tensión de alimentación son datos**, y **el temario los reúne para que se aprendan de una vez.**

<!-- indice -->

## Índice

- [1. La conexión balanceada y el conector XLR](#1-la-conexión-balanceada-y-el-conector-xlr)
- [2. Las alimentaciones del micrófono](#2-las-alimentaciones-del-micrófono)
- [3. El panel de conexiones](#3-el-panel-de-conexiones)
- [4. El splitter](#4-el-splitter)
- [5. Los cables y sus impedancias](#5-los-cables-y-sus-impedancias)
- [6. Las matrices de conmutación](#6-las-matrices-de-conmutación)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. La conexión balanceada y el conector XLR

**Por definición, en un conector XLR de tres pines el cable «vivo» se conecta al pin 2.** Ésa es la
respuesta oficial a la pregunta 48.

**El reparto completo, que es lo que hay que memorizar:**

| Pin | Qué lleva |
|---|---|
| **1** | **Malla o masa** |
| **2** | **Vivo**, señal en fase, también llamado positivo o *hot* |
| **3** | **Retorno**, señal en contrafase, también llamado negativo o *cold* |

**Y la regla que el oficio usa para no olvidarlo**: **uno, dos, tres: masa, vivo, retorno.**

**Por qué la conexión balanceada funciona, que es lo que da sentido al pin 2**: **la señal viaja por
dos conductores en oposición de fase.** **Cualquier interferencia que el cable recoja por el camino
—un zumbido de red, la radiofrecuencia de un transmisor— se induce IGUAL en los dos conductores.**
**En la entrada, el receptor RESTA un conductor del otro: la señal, que iba en oposición, se suma; la
interferencia, que iba igual en los dos, se cancela.**

**De ahí las dos consecuencias que un técnico usa a diario:**

1. **Un cable balanceado puede ser muy largo sin coger ruido.** **Uno desbalanceado, no.**
2. **Si un cable tiene el 2 y el 3 cruzados, ese canal entra con la polaridad invertida** y **al
   sumarlo con otro se cancelan parcialmente.** **Es la avería que más se busca en un montaje grande.**

## 2. Las alimentaciones del micrófono

**La tensión de alimentación A-B, también llamada Tonader, es de 12 voltios.** Ésa es la respuesta
oficial a la pregunta 49.

**Los dos sistemas que conviven, y no son intercambiables:**

| Sistema | Tensión | Cómo la manda | A quién alimenta |
|---|---|---|---|
| **Fantasma** (*phantom*) | **48 V** —también 24 y 12 en algunos equipos— | **Igual en los pines 2 y 3**, con retorno por el 1 | **Micrófonos de condensador** |
| **A-B** o **Tonader** ✔ | **12 V** | **Con POLARIDAD OPUESTA entre el 2 y el 3** | **Micrófonos de reportaje de sistemas antiguos** |

**La diferencia de fondo, y es la que explica por qué una estropea lo que la otra no**: **la
alimentación fantasma pone la misma tensión en los dos conductores de señal**, así que **un
micrófono dinámico, que no la necesita, no la «ve»: para él los dos conductores están al mismo
potencial.** **La A-B, en cambio, pone doce voltios de DIFERENCIA entre los dos conductores**, y
**eso sí atraviesa un micrófono dinámico y puede dañarlo.**

**La regla de oficio**: **la fantasma se puede dejar puesta casi siempre; la A-B, no.**

## 3. El panel de conexiones

**Para que al conectar un latiguillo en la entrada de un equipo NO se corte su salida, el patch panel
ha de tener diseño seminormalizado.** Ésa es la respuesta oficial a la pregunta 18.

**Los tres diseños, y qué hace cada uno:**

| Diseño | Con el latiguillo puesto |
|---|---|
| **Normalizado** (*full normalled*) | **Se corta la conexión interna en LOS DOS lados**: se interrumpe la señal que iba por defecto |
| **Seminormalizado** (*half normalled*) ✔ | **Se corta sólo al insertar en la fila INFERIOR**; **al insertar en la superior se toma una copia y NO se corta nada** |
| **No normalizado** (*non normalled*) | **No hay conexión interna**: nada pasa si no se pone latiguillo |

**Qué gana el seminormalizado, y es exactamente lo que el enunciado describe**: **permite ESCUCHAR o
DERIVAR una señal sin interrumpirla.** **Se pincha en la fila de arriba, se saca una copia, y el
camino normal sigue funcionando.** **Es lo que hace posible medir una línea en directo sin tirar la
emisión.**

**La opción d), «diseño balanceado inferior», no nombra ningún diseño de panel**: **balanceado se
refiere al cableado, no a la normalización.** **Mezcla dos conceptos que no se tocan.**

## 4. El splitter

**Dos preguntas del punto van del reparto de un micrófono a varios destinos.**

**La pregunta 32**: **el dispositivo que distribuye la señal de un micrófono a varias salidas idénticas
con el mismo nivel de señal es el splitter de audio.** Ésa es la respuesta oficial.

**Las tres opciones falsas nombran tres aparatos reales que hacen otra cosa**: **el crossover reparte
por FRECUENCIA —es el filtro de cruce del tema 10—, el fader ajusta el NIVEL de un canal, y el
«external live return» no es un dispositivo de reparto.**

**La pregunta 42, que es la interesante**: **con dos mesas alimentadas por splitters pasivos sin
ajuste alguno, la que tiene control sobre la ganancia de micro es… cada mesa tiene su propio nivel.**
Ésa es la respuesta oficial.

**Y aquí hay que ser preciso, porque la respuesta oficial dice una cosa cierta y el escenario tiene un
matiz que el temario debe explicar:**

**Lo que la respuesta afirma es que cada mesa ajusta su ganancia de entrada de forma independiente**,
y **eso es cierto: el previo de cada mesa es suyo.** **Subir la ganancia en la mesa de sala no cambia
lo que oye la mesa de monitores.**

**Y lo que un técnico tiene que saber además, y el temario lo dice**: **con un splitter PASIVO
—normalmente un transformador o un simple paralelo— hay dos cosas que sí se comparten.** **La
primera, la alimentación fantasma: sólo UNA de las mesas debe entregarla, y las demás deben tenerla
cortada o aisladas por transformador.** **La segunda, la carga: colgar varias entradas del mismo
micrófono baja la impedancia que éste ve.** **Por eso los repartos serios llevan transformadores de
aislamiento y no un simple paralelo.**

**Las tres opciones falsas se caen limpiamente**: **la proximidad no da control de ganancia; entregar
la fantasma no da control de ganancia; y activar el atenuador cambia el nivel de ESA mesa, no el de la
otra** —que es, en el fondo, la misma verdad que la respuesta correcta enuncia mejor—.

## 5. Los cables y sus impedancias

**Dos preguntas van de cable, y las dos son de dato.**

**La pregunta 57**: **los cables XLR destinados a transmisión de audio AES3 deben tener una impedancia
de 110 ohmios.** Ésa es la respuesta oficial.

**Y aquí está la trampa que más caro sale en una instalación real**: **un cable de micrófono y un
cable AES3 llevan el mismo conector y NO son el mismo cable.**

| Cable | Impedancia | Para qué |
|---|---|---|
| **De micrófono** | **No está especificada**: es audio analógico y la impedancia característica no interviene | **Audio analógico balanceado** |
| **AES3 sobre XLR** ✔ | **110 ohmios** | **Audio digital de dos canales** |
| **AES3 sobre coaxial (AES3id)** | **75 ohmios** | **Audio digital sobre infraestructura de vídeo** |
| **Vídeo SDI** | **75 ohmios** | **Vídeo digital** |

**Por qué importa**: **una señal digital tiene flancos muy rápidos y se comporta como radiofrecuencia.**
**Si la impedancia del cable no es la del sistema, hay reflexiones**, y **las reflexiones producen
errores de bit.** **Un cable de micrófono lleva AES3 unos metros y falla a partir de cierta longitud,
sin previo aviso y de forma intermitente**: **es una de las averías más difíciles de encontrar.**

**La pregunta 51**: **la longitud máxima de transmisión recomendada de un cable de categoría 5 para
redes de audio es de 100 metros.** Ésa es la respuesta oficial.

**Los 100 metros son el límite de un segmento de cobre en Ethernet**, y **no son un capricho: es el
valor con el que la norma garantiza el temporizado del protocolo.** **Se reparten en 90 metros de
cable fijo más 10 de latiguillos en los dos extremos.**

**La pregunta 25**: **de los cables enumerados, el que puede usarse para el protocolo Dante es el
Cat6.** Ésa es la respuesta oficial.

**Es la misma idea desde el otro lado**: **Dante viaja sobre Ethernet, y Ethernet sobre cobre va por
par trenzado de categoría.** **Las tres opciones falsas —75 ohmios, coaxial y XLR— son cables de
audio y vídeo, no de red.**

## 6. Las matrices de conmutación

**El enunciado del punto pide expresamente matrices de conmutación y el examen no las pregunta.** **El
tema las cubre porque el programa las pide.**

**Qué es una matriz**: **un aparato con N entradas y M salidas que permite llevar cualquier entrada a
cualquier salida, y la misma entrada a varias salidas a la vez.** **Es el conmutador central de una
instalación.**

| Clase | Cómo funciona | Dónde |
|---|---|---|
| **Analógica** | **Conmuta señal eléctrica** | **Instalaciones antiguas y patch de emergencia** |
| **Digital** | **Conmuta muestras**: la señal ya va digitalizada | **Salas técnicas** |
| **Sobre red (IP)** | **No conmuta nada: SUSCRIBE**. Cada destino pide el flujo que quiere | **Instalaciones actuales**: es el tema 16 |

**Y la diferencia de fondo que conviene entender antes del tema 16**: **una matriz física tiene un
límite duro de entradas y salidas.** **Una red no**: **su límite es el ancho de banda.** **Ése es el
cambio que el audio sobre IP introduce en una instalación, y no la calidad del sonido.**

## 7. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 18 | Diseño de patch panel que no corta la salida | b) Seminormalizado ✔ |
| 25 | Cable que sirve para Dante | b) Cat6 ✔ |
| 32 | Dispositivo que reparte un micrófono a varias salidas | a) Splitter de audio ✔ |
| 42 | Qué mesa controla la ganancia con splitters pasivos | a) Cada mesa tiene su propio nivel ✔ |
| 48 | A qué pin del XLR va el vivo | b) 2 ✔ |
| 49 | Tensión de la alimentación A-B | a) 12 V ✔ |
| 51 | Longitud máxima de un cable de categoría 5 | a) 100 metros ✔ |
| 57 | Impedancia de un XLR para AES3 | c) 110 ohmios ✔ |

**Las ocho respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**El aviso de estudio, y es el que define este punto**: **seis de las ocho son datos puros.** **Pin 2,
12 voltios, 110 ohmios, 100 metros, Cat6, seminormalizado.** **No hay manera de deducirlos y sí de
memorizarlos en cinco minutos.** **Es el punto con mejor relación entre esfuerzo y acierto de toda la
ocupación.**

## 8. Trazabilidad

**Este tema no cita ninguna norma**, aunque **nombra dos**: la AES3 y las categorías de cableado
estructurado.

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema**: las que nombra no se han consultado | Las ocho **van como oficio** |

**Cuatro declaraciones expresas:**

1. **El texto de la norma AES3 no se ha consultado**: **está tras un muro de pago, como ya consta en
   `fuentes/normas-tecnicas/AES-normas-de-audio.md` para la AES10.** **La impedancia de 110 ohmios que
   este tema sostiene es la que el sector aplica universalmente y la que la respuesta oficial da**, y
   **el temario no la atribuye a un artículo de la norma que no ha leído.**
2. **Los 100 metros de un segmento de categoría 5 son el límite de la norma de cableado estructurado**,
   que **tampoco se ha consultado.** **El reparto en 90 más 10 metros es la práctica corriente de
   instalación**, y **se presenta como tal.**
3. **La tensión de 12 voltios de la alimentación A-B y el reparto de pines del XLR son convenciones
   asentadas del sector**, no normalizadas por ninguna norma consultada. **El tema las presenta como
   conocimiento común de la materia**, y **coinciden con las respuestas oficiales.**
4. **Sobre la pregunta 42, el temario sostiene la respuesta oficial y añade dos precisiones que ella
   no hace**: **la alimentación fantasma no puede entregarse desde las dos mesas a la vez, y un
   reparto pasivo sin transformadores carga el micrófono.** **Las dos son práctica de oficio y no
   contradicen la respuesta**: **la completan.**

**El resto del tema va como oficio y así se declara**: el mecanismo de la conexión balanceada, la
diferencia entre alimentación fantasma y A-B, los tres diseños de panel de conexiones, la función del
splitter, la tabla de impedancias por tipo de cable y la clasificación de matrices. **Nada de eso está
en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si
lo estuviera.
