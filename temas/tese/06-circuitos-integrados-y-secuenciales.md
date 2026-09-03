# Tema 6 del específico de Técnica de Equipos y Sistemas Electrónicos · Circuitos integrados y secuenciales

Los términos y siglas de este tema, presentados de entrada: el circuito integrado (**CI**); el
multiplexor (**MUX**) y el demultiplexor (**DEMUX**); el codificador y el decodificador; la unidad
aritmético-lógica (**ALU**, *arithmetic logic unit*); el biestable (***flip-flop***) y sus variantes
—**RS**, **D**, **JK** y **T**—; el registro; la señal de reloj (**CLK**, *clock*); las entradas
síncronas y asíncronas; el acarreo (*carry*) de un sumador; y la interfaz digital serie de vídeo
(**SDI**), que este tema sólo nombra de pasada y el tema 8 desarrolla.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, puntos 6 y 7):
> «CIRCUITOS INTEGRADOS: decodificadores y codificadores, multiplexores y demultiplexores. Sumadores y
> restadores. La unidad aritmético-lógica (ALU).»
> «CIRCUITOS SECUENCIALES: Elementos secuenciales. Entradas de reloj síncronas y asíncronas.»

**Cuatro preguntas, y este tema junta dos puntos del anexo** —el 6 y el 7— **porque son las dos caras
de la misma materia: la lógica que no es una puerta suelta.**

**Y la distinción que ordena el tema entero, que es también la que separa los dos puntos:**

| | **Combinacional** | **Secuencial** |
|---|---|---|
| **De qué depende la salida** | **SÓLO de las entradas de ahora** | **De las entradas Y del estado anterior** |
| **Tiene memoria** | **No** | **Sí** |
| **Ejemplos** | **Puertas, multiplexores, codificadores, sumadores, ALU** | **Biestables, registros, contadores** |

**Ninguna de las cuatro preguntas lleva figura**, lo que **hace de éste el punto más limpio de la
primera mitad de la ocupación.**

<!-- indice -->

## Índice

- [1. Los circuitos combinacionales](#1-los-circuitos-combinacionales)
- [2. El biestable](#2-el-biestable)
- [3. El registro](#3-el-registro)
- [4. Síncrono y asíncrono](#4-síncrono-y-asíncrono)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Los circuitos combinacionales

**El punto 6 del anexo enumera cinco y el examen pregunta por uno.** **El tema los cubre todos.**

| Circuito | Qué hace |
|---|---|
| **Multiplexor** | **Selecciona UNA de varias entradas y la lleva a UNA salida**: es un conmutador gobernado por bits |
| **Demultiplexor** | **Lo contrario**: lleva una entrada a una de varias salidas |
| **Codificador** | **Convierte una de N líneas activas en un número binario** |
| **Decodificador** | **Convierte un número binario en una de N líneas activas** |
| **Sumador** | **Suma dos números binarios**, con acarreo de entrada y de salida |
| **ALU** | **Suma, resta y opera lógicamente** según lo que le digan sus bits de control |

**La pregunta 52**: **para un multiplexor, la afirmación verdadera es que utiliza las entradas de
control para conmutar una de sus entradas a su salida.** Ésa es la respuesta oficial.

**Las tres opciones falsas invierten o confunden el sentido, y cada una tiene su nombre:**

| Opción | Qué describe de verdad |
|---|---|
| **«Las entradas de control indican cuántas salidas aparecerán activas»** | **Nada**: un multiplexor tiene UNA salida |
| **«Mezcla todas sus señales de entrada a su única salida»** | **Un sumador analógico**: un multiplexor no mezcla: elige |
| **«Conmuta su señal de entrada a una de sus salidas»** | **Un DEMULTIPLEXOR**: es el sentido contrario. **Es la falsa mejor puesta** |

**La palabra que decide es «una de sus entradas»**: **muchas entradas, una salida.**

**Y la cuenta que hay que saber**: **con n bits de control se eligen 2ⁿ entradas.** **Dos bits para
cuatro entradas, tres para ocho.** **Es la misma relación que gobierna los decodificadores y el
direccionamiento de memoria del tema 7.**

**La unidad aritmético-lógica**, que el enunciado nombra y el examen no pregunta, **es el núcleo del
microprocesador**: **un bloque que recibe dos operandos y un código de operación y devuelve el
resultado más unas banderas** —cero, acarreo, signo, desbordamiento—. **Esas banderas son lo que
permite que un programa tome decisiones.**

## 2. El biestable

**Un flip-flop es un circuito secuencial que almacena un bit de información.** Ésa es la respuesta
oficial a la pregunta 17.

**Es la unidad mínima de memoria**, y **la definición contiene las dos palabras que la pregunta mide**:
**secuencial** —tiene estado— **y un bit** —no más—.

**Las tres opciones falsas nombran otras tres cosas que existen y no son ésta**: **un tipo de puerta
lógica** —una puerta no tiene memoria—, **un conversor analógico-digital** y **un temporizador
digital.**

**Las cuatro variantes que un técnico encuentra:**

| Biestable | Qué hace |
|---|---|
| **RS** | **Pone a uno (*set*) o a cero (*reset*)**. Su combinación prohibida es activar los dos a la vez |
| **D** | **Copia a la salida lo que haya en la entrada** cuando llega el flanco de reloj: es el de los registros |
| **JK** | **Como el RS, pero la combinación de los dos activos INVIERTE** el estado |
| **T** | **Cambia de estado en cada pulso**: es la base de los contadores y de los divisores de frecuencia |

**Y la propiedad del biestable T que conviene tener**: **divide la frecuencia entre dos.** **Encadenando
n de ellos se divide entre 2ⁿ**, y **eso es exactamente cómo se construye un contador binario.**

## 3. El registro

**La función de un registro en un circuito secuencial es almacenar datos temporalmente.** Ésa es la
respuesta oficial a la pregunta 89.

**Qué es**: **un conjunto de biestables que guardan una palabra completa.** **Ocho biestables D forman
un registro de un byte.**

**Las tres opciones falsas y por qué caen:**

1. **«Realizar cálculos»** **es lo que hace la unidad aritmético-lógica**, no el registro. **El
   registro le da los datos y recoge el resultado.**
2. **«Controlar dispositivos de salida»** **es lo que hace un puerto**, que **suele llevar un registro
   dentro pero no es lo mismo.**
3. **«Los circuitos secuenciales no tienen registro»** **es falsa de raíz**: **el registro es el
   ejemplo canónico de circuito secuencial.**

**Los tipos de registro, por cómo entran y salen los datos:**

| Tipo | Cómo funciona | Dónde |
|---|---|---|
| **Paralelo-paralelo** | **Entra y sale la palabra entera de golpe** | **Dentro de un procesador** |
| **De desplazamiento** | **Los bits entran o salen uno a uno**, corriéndose | **Conversión serie-paralelo**: es lo que hay en cada interfaz digital |

**Y el registro de desplazamiento merece la línea**, porque **es lo que convierte un flujo serie —el
SDI y el AES3 del tema 8— en palabras paralelas que el equipo pueda tratar.**

## 4. Síncrono y asíncrono

**La pregunta 37 es negativa**: **la afirmación FALSA sobre circuitos secuenciales síncronos es que
las entradas de reloj síncronas son aquellas que pueden cambiar de estado en cualquier momento.** Ésa
es la respuesta oficial.

**Y la razón está en la propia palabra**: **síncrono significa «al mismo tiempo».** **Una entrada
síncrona SÓLO surte efecto cuando llega el flanco de reloj.** **La que puede actuar en cualquier
momento es justamente la ASÍNCRONA.** **La opción describe lo asíncrono y lo llama síncrono.**

| | **Entrada síncrona** | **Entrada asíncrona** |
|---|---|---|
| **Cuándo actúa** | **Sólo con el flanco de reloj** | **En cuanto se activa, sin esperar a nada** |
| **Para qué se usa** | **La operación normal** | **Puesta a cero inicial y paradas de emergencia** |
| **Cómo se rotula** | **D, J, K, T** | ***Preset* y *clear***, a menudo con una barra encima |

**Las tres afirmaciones verdaderas que la pregunta ofrece describen bien lo síncrono**: **diseño más
sencillo que el asíncrono, comportamiento predecible y cambios de estado bien definidos en el
tiempo.** **Las tres son consecuencias de lo mismo: si todo cambia a la vez, no hay carreras.**

**Y por qué esto importa en un equipo real**: **el mayor problema de los circuitos asíncronos son las
condiciones de carrera** —dos señales que llegan casi a la vez y el circuito acaba en un estado
imprevisto—. **Sincronizar todo con un reloj común elimina el problema de raíz**, y **es la razón de
que un equipo digital necesite reloj y de que la sincronización del tema 8 sea materia de examen.**

## 5. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 17 | Qué es un flip-flop | d) Un circuito secuencial que almacena un bit ✔ |
| 37 | Afirmación FALSA sobre circuitos secuenciales síncronos | a) Que las entradas síncronas cambian en cualquier momento ✔ |
| 52 | Qué es verdadero para un multiplexor | d) Usa las entradas de control para conmutar una entrada a su salida ✔ |
| 89 | Función de un registro | a) Almacenar datos temporalmente ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Es el primer punto de esta ocupación en el que puede decirse eso**, y **la razón es simple: ninguna
de sus cuatro preguntas lleva figura.**

**Un aviso de reparto**: **una de las cuatro es negativa** —la 37—, **y se contesta con la definición
de la palabra «síncrono».**

## 6. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son los circuitos integrados combinacionales y los
secuenciales, y **va entera como oficio.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema** | Las cuatro **van como oficio** |

**Dos declaraciones expresas:**

1. **La clasificación de biestables y de registros del epígrafe 2 y 3 es conocimiento asentado de la
   electrónica digital**, no normalizado por ninguna norma consultada. **El tema la presenta como
   conocimiento común de la materia.**
2. **La relación entre bits de control y entradas de un multiplexor —2 elevado a n— es una consecuencia
   aritmética**, no un dato de catálogo, y **el tema la presenta como tal.**

**El resto del tema va como oficio y así se declara**: la distinción entre lógica combinacional y
secuencial, el sentido de un multiplexor frente a un demultiplexor, las cuatro variantes de biestable
y la propiedad divisora del tipo T, los dos tipos de registro y la diferencia entre entradas síncronas
y asíncronas con las condiciones de carrera que motivan el reloj común. **Nada de eso está en un
boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
