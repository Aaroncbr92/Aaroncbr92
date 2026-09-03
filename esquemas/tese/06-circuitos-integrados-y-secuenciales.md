# Esquema · Tema 6 del específico de Técnica de Equipos y Sistemas Electrónicos · Circuitos integrados y secuenciales

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio y electrónica digital.
**Siglas**: el biestable (*flip-flop*), la señal de reloj (**CLK**, de
*clock*) y los cuatro tipos de biestable, que se nombran por letra (**RS**, **D**, **JK** y **T**).

**Cabecera.** Enunciado: punto 6 del anexo · **4 preguntas** · **ninguna lleva figura, y es uno de los
dos puntos limpios de la ocupación.**

<!-- indice -->

## Índice

- [Combinacional frente a secuencial](#combinacional-frente-a-secuencial)
- [El multiplexor](#el-multiplexor)
- [El biestable](#el-biestable)
- [El registro](#el-registro)
- [Síncrono y asíncrono](#síncrono-y-asíncrono)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Combinacional frente a secuencial

| | **Combinacional** | **Secuencial** |
|---|---|---|
| **De qué depende la salida** | **Sólo de las entradas de ahora** | **De las entradas y del estado anterior** |
| **Tiene memoria** | **No** | **Sí** |
| **Ejemplos** | **Puertas, multiplexor, decodificador, sumador** | **Biestable, registro, contador** |

- **ES LA DIVISIÓN QUE ORDENA TODO EL PUNTO**, y **las cuatro preguntas se colocan solas en una de las
  dos columnas.**

## El multiplexor

- **PREGUNTA 52** · `[of]` · **De un multiplexor es verdadero que usa las entradas de control para
  conmutar una de sus entradas a su salida.**
- **QUÉ ES, EN UNA LÍNEA**: **un conmutador gobernado por bits.** **Con *n* bits de control elige entre
  2 elevado a *n* entradas.**
- **SU PAREJA**: **el demultiplexor hace lo contrario**: reparte una entrada entre varias salidas.
- **DÓNDE APARECE EN LA OCUPACIÓN**: **es el mismo concepto que la matriz de conmutación del tema 10**,
  bajado al nivel de los bits.

## El biestable

- **PREGUNTA 17** · `[of]` · **Un flip-flop es un circuito secuencial que almacena un bit.**
- **ES LA CÉLULA DE MEMORIA MÁS PEQUEÑA QUE EXISTE**: **un bit, y nada más.**
- **LOS TIPOS**: **RS, D, JK y T.** **El D es el que más se usa: copia a la salida lo que hay en su
  entrada en cada flanco de reloj.**

## El registro

- **PREGUNTA 89** · `[of]` · **La función de un registro es almacenar datos temporalmente.**
- **QUÉ ES**: **varios biestables en fila gobernados por el mismo reloj.** **Ocho biestables son un
  registro de un byte.**
- **PARA QUÉ SIRVEN LOS DE DESPLAZAMIENTO**: **para convertir serie en paralelo y al revés**, que es
  exactamente lo que hace un interfaz digital serie al recibir.

## Síncrono y asíncrono

- **PREGUNTA 37** · `[of]` · **Es FALSO que en los circuitos secuenciales síncronos las entradas
  síncronas cambien el estado en cualquier momento.**
- **LA DEFINICIÓN QUE LA DESMIENTE**: **una entrada síncrona sólo actúa en el flanco del reloj.**
  **Justamente por eso se llama síncrona.**
- **LAS QUE SÍ ACTÚAN EN CUALQUIER MOMENTO SON LAS ASÍNCRONAS**: **las de puesta a uno y a cero**, que
  se saltan el reloj y por eso se reservan para la inicialización.
- **POR QUÉ IMPORTA**: **un diseño síncrono es previsible y uno asíncrono depende de retardos.** **En
  equipos de televisión, donde todo cuelga de un reloj común, el diseño síncrono es la norma.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 17 | Qué es un flip-flop | d) Un circuito secuencial que almacena un bit ✔ |
| 37 | Afirmación FALSA sobre circuitos secuenciales síncronos | a) Que las entradas síncronas cambien en cualquier momento ✔ |
| 52 | Qué es verdadero para un multiplexor | d) Usa las entradas de control para conmutar una entrada a su salida ✔ |
| 89 | Función de un registro | a) Almacenar datos temporalmente ✔ |

**Las cuatro oficiales son correctas** y **ninguna descansa sólo en la plantilla.** · **Aviso de
estudio**: **es el punto más rentable de la mitad electrónica del temario**: **cuatro preguntas, ninguna
figura y todas de definición.** **Con la tabla del primer epígrafe se contestan las cuatro.**
