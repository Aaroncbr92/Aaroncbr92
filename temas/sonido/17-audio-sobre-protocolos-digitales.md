# Tema 17 del específico de Sonido · Audio sobre protocolos digitales

Las siglas de este tema, presentadas de entrada: la interfaz digital de audio multicanal (**MADI**,
*multichannel audio digital interface*), que es la norma **AES10** de la Sociedad de Ingeniería de
Audio (**AES**); la norma de dos canales **AES3**,
que el sector llama también **AES/EBU**; la interfaz óptica de ocho
canales (**ADAT**, por el sistema de cinta digital que la estrenó); la Sociedad de Ingenieros de Cine
y Televisión (**SMPTE**, *Society of Motion Picture and Television Engineers*) y su interfaz digital
serie de vídeo (**SDI**); el conector coaxial de bayoneta (**BNC**); el reloj de palabra (**word clock**); la señal de referencia de
vídeo o negro compuesto (*black burst*, **BB**); la norma de sincronismo de audio **AES11**; el código
de tiempo longitudinal (**LTC**) y el vertical (**VITC**); la interfaz digital de instrumentos
musicales (**MIDI**); los protocolos de tiempo (**PTP** y **NTP**) y el protocolo de red (**IP**), que
el tema 16 ya presentó; la interfaz de propósito general (**GPI**), que el temario de Realización ya
usó; y el seguimiento del audio al vídeo (**AFV**, *audio follow video*).

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 15):
> «AUDIO SOBRE PROTOCOLOS DIGITALES. MADI, AES EBU, ADAT, SDI, capacidades, transporte,
> compatibilidad, conversión. Sincronía en entornos digitales, Word Clock, LTC, VITC. Audio Follow
> Video, GPI, MIDI.»

**Cinco preguntas.** **Y el punto que cierra la ocupación por donde el tema 16 la abre**: **antes de
que el audio fuera por red, iba por interfaces digitales dedicadas**, y **en una instalación real
conviven las dos cosas.**

**Su reparto**: **tres preguntas son de MADI y dos de sincronismo.** **El enunciado pide además ADAT,
SDI, VITC, MIDI, GPI y el seguimiento de audio al vídeo, y de eso no pregunta nada**: **el tema lo
desarrolla porque el programa lo pide.**

<!-- indice -->

## Índice

- [1. Las interfaces digitales de audio](#1-las-interfaces-digitales-de-audio)
- [2. El MADI](#2-el-madi)
- [3. La sincronía: qué sincroniza qué](#3-la-sincronía-qué-sincroniza-qué)
- [4. El código de tiempo](#4-el-código-de-tiempo)
- [5. Lo que el enunciado pide y el examen no pregunta](#5-lo-que-el-enunciado-pide-y-el-examen-no-pregunta)
- [6. Conversión y compatibilidad](#6-conversión-y-compatibilidad)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Las interfaces digitales de audio

**Antes de la red, cada interfaz llevaba un número fijo de canales por un cable dedicado:**

| Interfaz | Canales | Soporte | Norma |
|---|---|---|---|
| **AES3** (AES/EBU) | **2** | **XLR de 110 ohmios**, o coaxial de 75 | **AES3** |
| **ADAT** | **8** a 48 kHz | **Fibra óptica de plástico** | De fabricante |
| **MADI** | **Hasta 64** | **Coaxial de 75 ohmios o fibra** | **AES10** |
| **SDI** | **Hasta 16 canales incrustados** | **Coaxial de 75 ohmios** | De la SMPTE |

**Y la relación con la AES está documentada en la propia presentación de normas de la Sociedad de
Ingeniería de Audio, que este proyecto tiene volcada:**

> «AES3 (2-channel digital audio), **AES10 (MADI)**, AES14 (analog XLR pin-out), AES67 (networked
> audio) — AES Standards have contributed to your operations, making your work more successful,
> improved your workflow, and saved your production, more times than you realize.»

---

**De ahí este temario toma sólo lo que la frase dice**: **que MADI es la AES10 y AES3 la de dos
canales.** **El texto de las dos normas está tras un muro de pago y no se ha leído**, así que **ningún
dato interno de ellas se atribuye aquí a un articulado.**

## 2. El MADI

**Tres preguntas del cuadernillo van de MADI, y conviene contestarlas juntas.**

**La pregunta 77**: **el protocolo MADI permite la conexión de hasta 64 canales de audio.** Ésa es la
respuesta oficial.

**Y las tres opciones falsas dan cifras concretas y erróneas**, lo que **convierte la pregunta en una
tabla de datos:**

| Opción | Qué dice | Por qué es falsa |
|---|---|---|
| **64 canales** ✔ | | **La capacidad del protocolo** |
| **«Hasta 50 metros»** | **Distancia** | **Se queda MUY corta**: por coaxial llega a unos 100 metros, y por fibra a kilómetros |
| **«Coaxial de 125 ohmios»** | **Impedancia** | **El coaxial de MADI es de 75 ohmios**, como el de vídeo |
| **«24 bits y 128 kHz»** | **Formato** | **La profundidad es correcta**; **la frecuencia, no**: el MADI clásico trabaja hasta 48 kHz para sus 64 canales, y a más frecuencia reduce el número de canales |

**La pregunta 61**: **de forma estándar, el MADI óptico es multimodo.** Ésa es la respuesta oficial.

**La distinción entre los dos tipos de fibra, que reaparece en cualquier instalación:**

| Fibra | Núcleo | Alcance | Dónde |
|---|---|---|---|
| **Multimodo** ✔ | **Más grande**: 50 o 62,5 micras | **Cientos de metros** | **Dentro de un edificio**: es la de MADI |
| **Monomodo** | **Muy fino**: 9 micras | **Kilómetros** | **Entre edificios y enlaces largos** |

**Y las opciones c) y d) —coaxial y BNC— ni siquiera son fibra**: **son el otro soporte del MADI y su
conector.** **La pregunta dice «óptico», y eso las descarta sin más.**

**La pregunta 28**: **el método más eficiente para asegurar el funcionamiento correcto de un sistema
MADI es implementar rutas de transmisión redundantes.** Ésa es la respuesta oficial.

**Por qué**: **el MADI es una conexión PUNTO A PUNTO por un solo cable.** **Sesenta y cuatro canales
viajan por ese cable, y si se corta, se caen los sesenta y cuatro.** **La única protección real es
tener un segundo camino físico.**

**Las tres opciones falsas trasladan soluciones de OTRA tecnología:**

1. **«Redundancia en el PTP»** **es del audio sobre red del tema 16**: **el MADI no usa PTP.**
2. **«Configurar una red en estrella»** **presupone una red conmutada**: **el MADI no es una red y no
   tiene topología que configurar.**
3. **«Utilizar routers y switches verificados»** **es, otra vez, del mundo IP.**

**La lección que deja, y es la que ordena todo este tema frente al 16**: **una interfaz dedicada y una
red no se protegen igual.** **La primera se duplica; la segunda se configura.**

## 3. La sincronía: qué sincroniza qué

**El word clock sincroniza equipos digitales.** Ésa es la respuesta oficial a la pregunta 27.

**Y ésta es la pregunta que más se falla del punto**, porque **las cuatro opciones nombran cosas que
suenan a lo mismo y no lo son:**

| Señal | Qué transmite | Qué NO hace |
|---|---|---|
| **Word clock** ✔ | **El instante de cada MUESTRA** | **No dice qué hora es ni por dónde va la cinta** |
| **Código de tiempo (LTC/VITC)** | **La POSICIÓN**: horas, minutos, segundos y fotogramas | **No sincroniza el reloj de muestreo** |
| **Black burst** | **La referencia de cuadro de vídeo** | **No alinea muestras de audio por sí solo** |
| **NTP** | **La hora del día** | **Nada de lo anterior** |

**El error de concepto que la pregunta castiga es creer que el código de tiempo sincroniza.** **No lo
hace.** **Dos equipos con el mismo código de tiempo y relojes de muestreo distintos derivan
igualmente**: **cuadran al principio y no al final.** **La posición y la velocidad son cosas
distintas**, y **es el mismo aviso que el tema 8 da desde el lado de la estación de trabajo.**

**Y la norma que ordena esto en audio profesional es la AES11**, que **el enunciado del anexo nombra**
y que **este proyecto no ha consultado**: **fija cómo se distribuye la referencia de reloj en una
instalación.**

## 4. El código de tiempo

**Una palabra de código de tiempo LTC para un solo fotograma la conforman 80 bits.** Ésa es la
respuesta oficial a la pregunta 19.

**Y es el mismo dato que el temario de Realización Televisión pregunta en su tema 12**, lo que **da
una idea de cuánto se comparte entre ocupaciones técnicas.**

**Cómo se reparten esos 80 bits:**

| Contenido | Bits |
|---|---|
| **Los dígitos de horas, minutos, segundos y fotogramas** | **32**, en cuatro bits por dígito |
| **Bits de usuario**, para meter datos propios | **32** |
| **Banderas** de estado | **Unos pocos** |
| **Palabra de sincronismo**, que marca el final y da el sentido de la marcha | **16** |

**Las dos formas de llevarlo, que el enunciado nombra:**

| Forma | Cómo viaja | Ventaja | Límite |
|---|---|---|---|
| **LTC** —longitudinal— | **Como una señal de AUDIO**, por una pista o un cable | **Se lee moviendo la cinta a cualquier velocidad** | **No se lee en pausa** |
| **VITC** —vertical— | **Dentro del intervalo de borrado de la IMAGEN** | **Se lee en pausa y a cámara lenta** | **No se lee en avance rápido** |

**Y por eso los sistemas serios llevan los dos**: **se complementan exactamente en lo que al otro le
falta.** **El LTC, además, es lo que hace que el código de tiempo sea materia de un temario de sonido
y no sólo de vídeo: viaja por la infraestructura de audio.**

## 5. Lo que el enunciado pide y el examen no pregunta

**Tres conceptos del enunciado se quedan sin pregunta y el tema los desarrolla:**

**El seguimiento del audio al vídeo (AFV)**: **es la función por la que, al conmutar una fuente de
vídeo en el mezclador, su audio se conmuta con ella.** **Evita que se corte la imagen de una cámara y
siga oyéndose el micrófono de otra.** **Se activa por canal, y en un directo mal preparado es la
diferencia entre un corte limpio y un solapamiento.**

**La interfaz de propósito general (GPI)**: **es un contacto eléctrico simple —se cierra o se abre—
que dispara una acción en otro equipo.** **Es el pegamento de las instalaciones**: **una mesa arranca
un servidor, un mezclador enciende un piloto de «en el aire», un reproductor avisa de que ha
terminado.** **Su virtud es que funciona entre equipos de casas distintas que no comparten ningún
protocolo.**

**El MIDI**: **no transporta audio, transporta ÓRDENES.** **Qué nota, con cuánta fuerza, qué programa,
qué valor de un control.** **En una sala de sonido se usa para gobernar el equipo desde una superficie
de control y para automatizar cambios de escena**, y **su pariente moderno en instalaciones de audio
en red es el control que viaja por la misma Ethernet del tema 16.**

## 6. Conversión y compatibilidad

**El enunciado pide expresamente «capacidades, transporte, compatibilidad, conversión»**, y **eso es
media instalación real.**

**Las conversiones corrientes y qué hay que vigilar en cada una:**

| Conversión | Qué hay que vigilar |
|---|---|
| **Analógico ↔ digital** | **El nivel de referencia**: qué dBu equivalen a qué dBFS. **No hay una equivalencia universal** |
| **AES3 ↔ SDI incrustado** | **El reloj**: el audio incrustado va atado a la referencia de vídeo |
| **MADI ↔ Dante** | **Reloj y latencia**: son dos mundos con dos relojes, y hay que decidir cuál manda |
| **Frecuencia de muestreo distinta** | **Un conversor de frecuencia de muestreo**, que introduce latencia y, si es barato, degradación |

**Y la regla que resume el punto**: **en una instalación mixta, el problema nunca es que los formatos
no se entiendan: es que los relojes no se pongan de acuerdo.** **La conversión de datos es fácil; la
de tiempo, no.**

## 7. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 19 | Bits de una palabra de LTC por fotograma | a) 80 ✔ |
| 27 | Qué hace el word clock | a) Sincroniza equipos digitales ✔ |
| 28 | Método más eficiente para asegurar un sistema MADI | c) Rutas de transmisión redundantes ✔ |
| 61 | Cómo es de forma estándar el MADI óptico | b) Multimodo ✔ |
| 77 | Qué permite el protocolo MADI | a) Hasta 64 canales de audio ✔ |

**Las cinco respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Y el aviso de estudio**: **tres de las cinco son datos del MADI —64 canales, fibra multimodo, 75
ohmios— y dos son conceptos de sincronismo.** **Con la tabla del epígrafe 1 y la del epígrafe 3 se
contesta el punto entero.**

## 8. Trazabilidad

**Este tema no cita ninguna norma articulada**, y **cita la presentación pública de las normas de la
AES.**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Segundo: organismo de normalización** | **Presentación de las normas de la Audio Engineering Society** (`fuentes/normas-tecnicas/AES-normas-de-audio.md`) | **Que el MADI es la AES10 y que la AES3 es la de dos canales**, citado literal. **Nada de su contenido interno** |

**Cuatro declaraciones expresas:**

1. **El texto de la AES10 está tras un muro de pago y no se ha leído**, y **así consta ya en
   `fuentes/normas-tecnicas/AES-normas-de-audio.md` desde que este proyecto escribió el tema 10 de
   Producción (Asistencia).** **Las cifras de este tema sobre el MADI —64 canales, 75 ohmios, fibra
   multimodo, alcances— coinciden con las respuestas oficiales y con el uso universal del sector**, y
   **el temario NO las atribuye a un apartado de la norma.**
2. **Las normas AES3 y AES11 se nombran y no se citan**, por la misma razón.
3. **El reparto de los 80 bits de la palabra de LTC del epígrafe 4 es el de la definición clásica del
   código**, y **no procede de ninguna norma volcada en este proyecto.** **La cifra total —80— es la
   que la pregunta mide y coincide con la que este mismo proyecto verificó en el temario de
   Realización Televisión.**
4. **Los alcances de fibra multimodo y monomodo del epígrafe 2 son órdenes de magnitud de
   instalación**, no valores normativos, y **el tema los presenta como tales.** **Lo que la pregunta 61
   mide es cuál de los dos tipos es el estándar del MADI, no su alcance.**

**El resto del tema va como oficio y así se declara**: la tabla de interfaces y sus capacidades, por
qué una conexión punto a punto se protege duplicándola y no configurándola, la distinción entre
sincronizar posición y sincronizar muestra, la complementariedad entre LTC y VITC, y las funciones del
seguimiento de audio al vídeo, la interfaz de propósito general y el MIDI. **Nada de eso está en un
boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
