# Tema 16 del específico de Sonido · El audio sobre redes de datos

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Sonido · punto 14 |
| **Sirve para** | **Sonido** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el audio sobre redes, y **va entera como oficio**: el texto de la norma AES67 **está tras un muro de pago y no se ha leído** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Dos respuestas descansan en la plantilla**: la frecuencia máxima de muestreo de AES67, cuyo texto no se ha consultado, y el número de flujos de un envío unicast, que es dato de implementación del fabricante |
| **Extensión** | **2.647 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el protocolo de internet (**IP**); el protocolo de
control de transmisión (**TCP**) y el de datagramas de usuario (**UDP**); la norma de audio en red de
la Sociedad de Ingeniería de Audio (**AES67**); el sistema **Dante** de la casa Audinate, cuyo nombre
desarrolla la propia pregunta 75 (*Digital Audio Network Through Ethernet*); el protocolo de tiempo
de precisión (**PTP**, *precision time protocol*), definido por el estándar **IEEE 1588**; el
protocolo de tiempo de red (**NTP**) y su versión simple (**SNTP**); el envío a un solo destino
(*unicast*) y a varios (*multicast*); el megabit por segundo (**Mbps**); y el conmutador de red
(*switch*).

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 14):
> «AUDIO SOBRE IP. Normativa AES 67 donde se describe la capacidad, transporte y uso de señales de
> este tipo. Sistema DANTE.»

**Nueve preguntas: el banco más grande de esta ocupación.** **Y el punto que mejor retrata dónde está
hoy el oficio**: **el examen dedica más preguntas a mover audio por una red que a captarlo con un
micrófono.**

**Su reparto interno es revelador**: **siete de las nueve son de Dante**, un sistema propietario, y
**dos son de la norma abierta.** **El cuadernillo pregunta por lo que está instalado, no por lo que
está normalizado.**

<!-- indice -->

## Índice

- [1. Por qué el audio va por red](#1-por-qué-el-audio-va-por-red)
- [2. Qué protocolo lleva el audio](#2-qué-protocolo-lleva-el-audio)
- [3. El reloj: PTP](#3-el-reloj-ptp)
- [4. Qué es Dante](#4-qué-es-dante)
- [5. La latencia](#5-la-latencia)
- [6. Las cuentas de ancho de banda](#6-las-cuentas-de-ancho-de-banda)
- [7. La norma abierta: AES67](#7-la-norma-abierta-aes67)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Por qué el audio va por red

**El tema 11 acababa con la diferencia entre una matriz y una red**, y **aquí se desarrolla:**

| | **Matriz clásica** | **Red IP** |
|---|---|---|
| **Límite** | **Duro**: las entradas y salidas que tenga el bastidor | **El ancho de banda** |
| **Cableado** | **Un cable por señal** | **Un cable por EQUIPO**, con todas sus señales dentro |
| **Cambiar un encaminamiento** | **Reconfigurar la matriz** | **Suscribirse al flujo desde el destino** |
| **Ampliar** | **Comprar más bastidor** | **Añadir un equipo a la red** |

**Y el precio de esa flexibilidad es lo que ocupa el resto del tema**: **una red no garantiza nada por
sí sola.** **Hay que darle un reloj común, hay que dimensionar su ancho de banda y hay que
configurarla para que el audio no compita con el resto del tráfico.**

## 2. Qué protocolo lleva el audio

**El protocolo que se utiliza por norma general para audio en red es UDP.** Ésa es la respuesta oficial
a la pregunta 7.

**Y la razón es exactamente la contraria de la que la intuición sugiere:**

| | **TCP** | **UDP** ✔ |
|---|---|---|
| **Qué hace si un paquete se pierde** | **Lo PIDE otra vez y espera** | **Sigue adelante** |
| **Garantiza la entrega** | **Sí** | **No** |
| **Retardo** | **Variable, y puede crecer mucho** | **Bajo y predecible** |
| **Sirve para audio en tiempo real** | **NO** | **SÍ** |

**El razonamiento**: **en audio en directo, un paquete que llega tarde es tan inútil como uno que no
llega.** **Ese instante de sonido ya pasó.** **Pedir la retransmisión sólo consigue retrasar todo lo
que viene detrás.** **Es preferible perder una muestra y seguir en hora.**

**Y las opciones falsas están bien construidas**: **«TCP/IP» es la familia entera de protocolos, no un
protocolo de transporte** —es la respuesta que da quien reconoce el nombre y no la función—; **«TCP»
es el que NO sirve; y la cuarta opción («UCP») no nombra ningún protocolo.**

## 3. El reloj: PTP

**Dante maneja la sincronización a través del protocolo PTP.** Ésa es la respuesta oficial a la
pregunta 58.

**Por qué hace falta un reloj común, y es lo que más cuesta entender de este punto**: **cada equipo de
audio digital tiene su propio oscilador, y dos osciladores nunca van exactamente igual.** **Si el que
manda muestras y el que las recibe no comparten reloj, cada cierto tiempo sobra o falta una muestra**,
y **eso se oye como un chasquido periódico.**

**Los tres protocolos de tiempo que la pregunta pone juntos, y no sirven para lo mismo:**

| Protocolo | Precisión | Para qué |
|---|---|---|
| **NTP** | **Milisegundos** | **Poner en hora un ordenador** |
| **SNTP** | **Peor que el NTP** | **Lo mismo, en versión simplificada** |
| **PTP (IEEE 1588)** ✔ | **Sub-microsegundo** | **Sincronizar equipos de audio y vídeo** |

**La diferencia de escala es de tres órdenes de magnitud**, y **es la que decide la pregunta**: **a 48
kHz, una muestra dura 20 microsegundos.** **Un protocolo con precisión de milisegundos no puede
alinear muestras; uno con precisión de sub-microsegundo, sí.**

**Y el mecanismo que lo hace posible, en una línea**: **el PTP no se limita a decir la hora: MIDE el
retardo de ida y vuelta de la red y lo compensa.** **Por eso necesita conmutadores que lo entiendan y
por eso una red de audio no se monta con cualquier switch doméstico.**

## 4. Qué es Dante

**Tres preguntas del cuadernillo piden definirlo desde tres ángulos, y las tres respuestas son
compatibles entre sí.**

**La pregunta 72**: **el protocolo Dante es un protocolo que permite la transmisión de señales de
audio y control a través de una red Ethernet.** Ésa es la respuesta oficial.

**Las dos palabras que importan de esa definición son «y control»**: **por la misma red viajan el
audio y las órdenes de encaminamiento, de configuración y de supervisión.** **Un cable hace el trabajo
del audio y el del control.**

**La pregunta 75**: **Dante permite transmisiones de datos unicast y multicast.** Ésa es la respuesta
oficial.

**La diferencia entre las dos, que el epígrafe 6 usa para una cuenta:**

| Modo | Cómo se manda | Cuándo conviene |
|---|---|---|
| **Unicast** | **Una copia POR DESTINO**: si tres equipos quieren la misma señal, se manda tres veces | **Pocos destinos** |
| **Multicast** | **UNA sola copia** que la red reparte a quien se haya suscrito | **Muchos destinos de la misma señal** |

**Y las tres opciones falsas de la 75 son afirmaciones concretas y falsas**: **el límite de canales
que da no es el del sistema, la afirmación de que no necesita un equipo maestro contradice el epígrafe
3 —alguien tiene que ser el reloj—, y la resolución de 16 bits es menor que la que el sistema
maneja.** **La opción c) es la más instructiva**: **precisamente porque Dante sincroniza, alguno de
sus equipos tiene que ser el maestro de reloj.**

**La pregunta 76**: **un conmutador en una red Dante es un dispositivo que permite la conexión de
múltiples dispositivos en una red, gestionando el tráfico de datos.** Ésa es la respuesta oficial.

**Es la definición de un switch de red, sin más**, y **la pregunta mide que no se confunda con un
conmutador de audio.** **Las tres opciones falsas lo convierten en un selector de frecuencias, en un
amplificador de línea y en un conversor**, que **es lo que la palabra «conmutador» sugiere a quien
viene del audio analógico.**

**Lo que sí conviene añadir, y el tema lo hace**: **no vale cualquier switch.** **Una red Dante pide
conmutadores gestionables, con calidad de servicio para dar prioridad al audio, con soporte de PTP y,
si se usa multicast, con control de suscripciones.**

## 5. La latencia

**Si una red Dante presenta alta latencia, se introduce un retraso entre la reproducción de las
señales de audio, lo que afecta a la sincronización.** Ésa es la respuesta oficial a la pregunta 73.

**Y es una pregunta que se contesta descartando disparates**: **las otras tres opciones dicen que el
sonido se vuelve más agudo, que la calidad se incrementa y que la señal se transmite más deprisa.**
**Ninguna tiene relación con lo que la latencia es.**

**Lo que sí hay que saber, y el tema lo añade**: **Dante trabaja con una latencia CONFIGURADA, no
casual.** **Cada equipo tiene un valor de latencia —desde unos 150 microsegundos hasta unos pocos
milisegundos— y el sistema entero se alinea al mayor.** **Esa latencia se elige según el tamaño de la
red: más conmutadores en el camino exigen más margen.**

**Y la consecuencia de oficio es la que la respuesta apunta**: **el problema de la latencia no es que
el sonido llegue tarde, es que llegue a DESTIEMPO respecto a otra cosa** —la imagen, otro camino de
audio, el sonido directo de una sala—.

## 6. Las cuentas de ancho de banda

**Dos preguntas del punto son cálculos**, y **las dos salen de la misma fórmula:**

> **Caudal de un canal = frecuencia de muestreo × profundidad de bits**

**A 48 kHz y 24 bits, un canal son 1,152 megabits por segundo.** **Ése es el número que hay que tener.**

**La pregunta 43**: **una red Dante con 32 canales de audio BIDIRECCIONALES a 48 kHz y 24 bits usa un
ancho de banda total aproximado de 73 Mbps.** Ésa es la respuesta oficial.

**La cuenta:**

1. **Un canal**: **48.000 × 24 = 1,152 Mbps.**
2. **Treinta y dos canales**: **1,152 × 32 = 36,9 Mbps.**
3. **Bidireccionales**: **×2 = 73,7 Mbps.**

**La palabra que decide es «bidireccionales»**: **quien no la lea se queda en 37 y no encuentra su
resultado entre las opciones.** **Y la opción a), 26 Mbps, es la que sale de usar 16 bits en lugar de
24.**

**La pregunta 47**: **enviando 10 canales por Dante en modo unicast a 48 kHz y 24 bits, el ancho de
banda y la cantidad de flujos serán 18 Mbps y 3 flujos.** Ésa es la respuesta oficial.

**Los flujos son la parte que hay que saber**: **Dante agrupa hasta CUATRO canales por flujo en
unicast.** **Diez canales necesitan tres flujos: cuatro, cuatro y dos.**

**Y el ancho de banda de 18 Mbps frente a los 11,5 que darían los diez canales en crudo se explica por
la sobrecarga**: **cada paquete lleva sus cabeceras de Ethernet, IP y UDP**, y **en audio en tiempo
real los paquetes son pequeños y frecuentes, así que la proporción de cabecera es alta.** **Es un
recargo que en las cuentas de red de audio nunca se puede despreciar.**

## 7. La norma abierta: AES67

**La máxima frecuencia de muestreo que se puede utilizar en AES67 es 96 kHz.** Ésa es la respuesta
oficial a la pregunta 52.

**Qué es la AES67 y qué la distingue de Dante**: **es una norma de INTEROPERABILIDAD.** **No pretende
sustituir a los sistemas propietarios, sino definir un terreno común en el que puedan entenderse.**
**Fija el transporte, el reloj y los formatos mínimos que todos deben admitir.**

**La propia Sociedad de Ingeniería de Audio la presenta en su relación de normas**, y **este proyecto
tiene esa presentación volcada:**

> «AES3 (2-channel digital audio), **AES10 (MADI)**, AES14 (analog XLR pin-out), AES67 (networked
> audio) — AES Standards have contributed to your operations, making your work more successful,
> improved your workflow, and saved your production, more times than you realize.»

---

**De esa frase este temario sólo toma lo que dice: que la AES67 es la norma DE AUDIO EN RED de la
AES**, y **que convive con la AES3 de dos canales y con la AES10 del MADI, que es el tema 17.** **El
texto de la norma está tras un muro de pago y no se ha leído**, así que **la cifra de 96 kHz descansa
en la respuesta oficial y en el uso del sector, y el temario lo declara.**

**Y la relación entre las dos cosas que este punto pregunta**: **Dante puede funcionar en modo AES67.**
**Un sistema propietario y una norma abierta no son alternativas excluyentes: el primero implementa la
segunda para poder hablar con equipos de otras casas.**

## 8. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 7 | Qué protocolo se usa por norma general para audio en red | d) UDP ✔ |
| 43 | Ancho de banda de 32 canales bidireccionales | c) 73 Mbps ✔ |
| 47 | Ancho de banda y flujos de 10 canales en unicast | d) 18 Mbps y 3 flujos ✔ **·** sólo con la plantilla |
| 52 | Máxima frecuencia de muestreo de AES67 | b) 96 kHz ✔ **·** sólo con la plantilla |
| 58 | Con qué protocolo sincroniza Dante el reloj | c) PTP ✔ |
| 72 | Qué es el protocolo Dante | c) Transmisión de audio y control por Ethernet ✔ |
| 73 | Qué ocurre con alta latencia en una red Dante | b) Se introduce retraso y afecta a la sincronización ✔ |
| 75 | Qué permite Dante | a) Transmisiones unicast y multicast ✔ |
| 76 | Qué es un conmutador en una red Dante | a) Conecta varios dispositivos y gestiona el tráfico ✔ |

**Las nueve respuestas oficiales son correctas.**

**Dos de las nueve descansan sólo en la plantilla**: **la agrupación de canales por flujo de un
sistema propietario y una cifra de una norma que está tras un muro de pago.**

**Y el aviso de estudio**: **este es el banco más grande de la ocupación y siete de sus nueve
preguntas son de un sistema de una sola casa.** **No es un punto que se pueda estudiar por conceptos
generales**: **hay que conocer Dante.**

## 9. Trazabilidad

**Este tema no cita ninguna norma articulada**, y **cita la presentación pública de las normas de la
AES.**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Segundo: organismo de normalización** | **Presentación de las normas de la Audio Engineering Society** (`fuentes/normas-tecnicas/AES-normas-de-audio.md`) | **Que la AES67 es la norma de audio en red de la AES**, citado literal. **Nada de su contenido interno** |
| **Quinto: la plantilla oficial** | **Dos afirmaciones**: la agrupación en flujos de un sistema propietario y la máxima frecuencia de muestreo de la AES67 | Preguntas 47 y 52 |

**Cuatro declaraciones expresas:**

1. **El texto de la norma AES67 está tras un muro de pago y no se ha leído.** **Este proyecto ya lo
   declaró para la AES10 en el temario de Producción (Asistencia)**, y **la situación es la misma.**
   **La cifra de 96 kHz de la pregunta 52 descansa en la plantilla oficial y en el uso del sector.**
2. **La documentación técnica de Audinate no se ha consultado.** **Las cifras de este tema sobre Dante
   —cuatro canales por flujo en unicast, márgenes de latencia configurable— descansan en la plantilla
   y en el uso del sector.** **Lo que el tema sostiene por su cuenta son los CONCEPTOS**: qué hace un
   protocolo de audio en red, por qué necesita un reloj y por qué el ancho de banda real supera al
   caudal de audio.
3. **La cuenta de ancho de banda del epígrafe 6 está hecha por este temario** con la fórmula que allí
   se declara. **La cifra de la pregunta 43 sale exacta; la de la 47 incluye una sobrecarga de red que
   este temario no calcula y sólo explica**, y **por eso esa respuesta se declara como dependiente de
   la plantilla.**
4. **La precisión del PTP —sub-microsegundo— y la del NTP —milisegundos— son órdenes de magnitud de
   uso corriente.** **El estándar IEEE 1588 no se ha consultado**, y **lo que la pregunta mide es cuál
   de los tres protocolos sirve para sincronizar audio, que es inequívoco.**

**El resto del tema va como oficio y así se declara**: la comparación entre matriz y red, la razón de
que el audio use UDP y no TCP, la necesidad de un reloj común y qué pasa sin él, la diferencia entre
unicast y multicast, el significado operativo de la latencia y los requisitos de un conmutador para
audio. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el
tema no lo presenta como si lo estuviera.
