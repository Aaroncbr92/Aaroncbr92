# Tema 3 del específico de Técnica de Equipos y Sistemas Electrónicos · Electrónica de potencia

Las siglas de este tema, presentadas de entrada: el rectificador controlado de silicio o tiristor
(**SCR**, *silicon controlled rectifier*); el triodo para corriente alterna (**TRIAC**); el diodo para
corriente alterna (**DIAC**); el transistor bipolar de puerta aislada (**IGBT**, *insulated-gate
bipolar transistor*); el transistor de efecto campo (**FET**, *field-effect transistor*) y sus dos
familias, el de unión (**JFET**) y el de metal-óxido-semiconductor (**MOSFET**); el transistor
uniunión (**UJT**); el transistor bipolar (**BJT**), que el tema 2 ya presentó; y el conversor
analógico-digital (**A/D**), que aparece en una opción falsa.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 3):
> «ELECTRÓNICA DE POTENCIA: Introducción a sistemas de potencia TIRISTOR TRIAC DIAC. Transistores
> IGBT. Transistor de efecto campo – FET.»

**Cuatro preguntas.** **Y el punto que explica de qué está hecho todo lo que en una instalación mueve
energía**: **las fuentes de alimentación, los reguladores de iluminación del tema 11, los variadores y
los sistemas de alimentación ininterrumpida.**

**Dos de las cuatro preguntas dependen de una figura**, y **las otras dos se contestan con la tabla del
epígrafe 2.**

<!-- indice -->

## Índice

- [1. Qué es la electrónica de potencia](#1-qué-es-la-electrónica-de-potencia)
- [2. Los cinco componentes del punto](#2-los-cinco-componentes-del-punto)
- [3. Las dos preguntas que dependen de una figura](#3-las-dos-preguntas-que-dependen-de-una-figura)
- [4. Dónde se encuentra esto en una instalación](#4-dónde-se-encuentra-esto-en-una-instalación)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Qué es la electrónica de potencia

**Es la que usa componentes semiconductores como INTERRUPTORES, no como amplificadores.** **Y ésa es
toda la diferencia con los temas 2 y 4.**

| | **Electrónica de señal** | **Electrónica de potencia** |
|---|---|---|
| **Qué se busca** | **Fidelidad**: que la salida sea proporcional a la entrada | **Rendimiento**: que se pierda lo menos posible |
| **Cómo trabaja el componente** | **En su zona lineal**, a medio conducir | **Del todo abierto o del todo cerrado** |
| **Por qué** | **Porque a medio conducir hay ganancia** | **Porque a medio conducir hay CALOR**, y el calor es la pérdida |

**De ahí se sigue la regla que ordena el punto entero**: **un interruptor ideal no disipa nada.**
**Abierto no pasa corriente; cerrado no hay tensión.** **En los dos casos, el producto de tensión por
corriente es cero.** **Toda la pérdida de un sistema de potencia está en las conmutaciones y en la
caída residual.**

## 2. Los cinco componentes del punto

| Componente | Qué es | Se controla | Se apaga |
|---|---|---|---|
| **Tiristor (SCR)** | **Un diodo con puerta**: conduce en un sentido | **Con un pulso en la puerta** | **Solo, cuando la corriente pasa por cero** |
| **TRIAC** | **Dos tiristores en antiparalelo**: conduce en los DOS sentidos | **Con un pulso en la puerta** | **Solo, al pasar por cero** |
| **DIAC** | **Un disparador**: conduce al superar una tensión | **No se controla**: dispara solo | |
| **IGBT** | **Entrada de FET y salida de bipolar** | **Con TENSIÓN en la puerta** | **Quitando esa tensión: se apaga cuando se quiera** |
| **FET** | **Un canal cuya conductividad la manda un campo eléctrico** | **Con tensión en la puerta** | **Igual** |

**La diferencia decisiva está en la última columna**: **un tiristor y un triac se encienden cuando uno
quiere y se apagan cuando la corriente pasa por cero.** **Un IGBT y un FET se encienden y se apagan
cuando uno quiere.** **Por eso los primeros valen para regular alterna de red —la iluminación del tema
11— y los segundos, para conmutar a decenas de kilohercios en una fuente conmutada.**

**La pregunta 29**: **el tipo de transistor que se usa más frecuentemente en equipos que trabajan con
tensiones y corrientes altas y necesitan alta capacidad de conmutación es el IGBT.** Ésa es la
respuesta oficial.

**Por qué él y no los otros tres:**

| Opción | Por qué no |
|---|---|
| **IGBT** ✔ | **Junta lo mejor de los dos mundos**: se manda con tensión, como un FET, y aguanta tensión y corriente altas, como un bipolar |
| **UJT** | **No es de potencia**: es un disparador, se usa en osciladores de relajación |
| **JFET** | **Es de señal**: no maneja potencias altas |
| **BJT** | **Aguanta potencia**, pero **se manda con CORRIENTE**, lo que exige una etapa de excitación mucho mayor, y **conmuta más lento** |

**La pregunta 20, que es la misma materia en negativo**: **la aplicación en la que NO es adecuado el
uso de transistores IGBT es en convertidores analógico-digitales de alta resolución en transmisores
ópticos.** Ésa es la respuesta oficial.

**El razonamiento es de categoría, no de grado**: **un conversor analógico-digital es un circuito de
SEÑAL, y de señal pequeña y precisa.** **Un IGBT es un interruptor de potencia.** **Las otras tres
opciones —variadores de frecuencia, control de motores de vehículo eléctrico y fuentes conmutadas— son
las tres aplicaciones canónicas del IGBT.**

**La regla que las tres comparten**: **conmutar mucha energía deprisa.** **Un conversor no conmuta
energía: mide.**

## 3. Las dos preguntas que dependen de una figura

**La pregunta 53** muestra un circuito y pide **de qué forma está polarizado el transistor de efecto
campo.** **La respuesta oficial es autopolarización por fuente.**

**La regla de familia, que es lo que el temario puede aportar:**

**Las cuatro maneras de polarizar un FET se distinguen por DÓNDE están las resistencias:**

| Polarización | Cómo se reconoce en el esquema |
|---|---|
| **Fija** | **La puerta va a una fuente de tensión propia**; **no hay resistencia en la fuente** |
| **Autopolarización por fuente** ✔ | **Hay una RESISTENCIA EN LA FUENTE** y la puerta va a masa por una resistencia grande. **La caída en esa resistencia de fuente es la que polariza** |
| **Por divisor de tensión** | **DOS resistencias en la puerta** formando un divisor, **más** la de fuente |
| **De enriquecimiento** | **No es una forma de polarizar**: es el modo de trabajo de un MOSFET |

**Las dos comprobaciones que ordenan cualquier esquema de esta clase**: **contar cuántas resistencias
hay en la puerta —una, autopolarización; dos, divisor— y comprobar si hay resistencia en la fuente.**
**Y la opción d), «polarización de enriquecimiento», se descarta sin ver la figura**: **enriquecimiento
y empobrecimiento son modos de un MOSFET, no montajes de polarización.**

**La pregunta 55** muestra un circuito regulador de tensión y pide **su eficiencia.** **La respuesta
oficial es el 50 %.**

**La regla de familia, y ésta es de las más útiles del temario:**

**En un regulador LINEAL, la eficiencia es simplemente la tensión de salida dividida entre la de
entrada.**

> **η = V(salida) / V(entrada)**

**Por qué**: **un regulador lineal deja pasar la MISMA corriente que entrega, y la diferencia de
tensión la disipa en calor.** **Un regulador que baja de 12 a 6 voltios pierde la mitad de la energía
calentando**, y **su rendimiento es del 50 %.** **De ahí que un resultado del 50 % delate una relación
de dos a uno entre entrada y salida.**

**Y el contraste que da sentido al epígrafe 1**: **un regulador CONMUTADO no disipa la diferencia:
la trocea y la transforma.** **Su rendimiento ronda el 85 o el 95 % con independencia de la relación
de tensiones.** **Es exactamente por eso por lo que existen los IGBT y los MOSFET de potencia.**

**Ninguna de estas reglas sustituye a ver el esquema**, y **el tema lo dice.**

## 4. Dónde se encuentra esto en una instalación

**El punto no lo pregunta y es lo que da sentido al temario:**

| Equipo de una instalación | Qué lleva dentro |
|---|---|
| **Fuente de alimentación conmutada** | **MOSFET o IGBT** conmutando a decenas de kilohercios |
| **Regulador de iluminación (*dimmer*)** | **TRIAC o tiristores**, disparados en fase: es el tema 11 |
| **Sistema de alimentación ininterrumpida** | **Rectificador, batería e inversor**, con IGBT en el inversor |
| **Variador de velocidad de motor** | **Puente de IGBT** generando alterna de frecuencia variable |
| **Etapa de potencia de audio en clase D** | **MOSFET** conmutando: es la clase que el temario de Sonido nombra |

**Y el hilo común**: **en cuanto un equipo maneja más de unas decenas de vatios, deja de amplificar y
empieza a conmutar.**

## 5. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 20 | Aplicación en la que NO es adecuado un IGBT | c) Conversores A/D de alta resolución ✔ |
| 29 | Transistor para tensiones y corrientes altas y conmutación rápida | a) IGBT ✔ |
| 53 | Cómo está polarizado el FET del circuito | a) Autopolarización por fuente ✔ **·** sólo con la plantilla |
| 55 | Eficiencia del circuito regulador de tensión | b) 50 % ✔ **·** sólo con la plantilla |

**Las cuatro respuestas oficiales son correctas.**

**Dos de las cuatro descansan sólo en la plantilla**: **las dos que dependen de una figura.**

**Y el aviso de reparto**: **una de las cuatro es negativa** —la 20—, **y se contesta por categoría:
la opción que no habla de conmutar potencia.**

## 6. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es la electrónica de potencia, y **va como oficio**,
salvo dos afirmaciones que descansan en la plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Dos afirmaciones**: la identificación de un montaje de polarización y el rendimiento de un regulador, los dos en circuitos que el temario no puede reproducir | Preguntas 53 y 55 |

**Tres declaraciones expresas:**

1. **Las preguntas 53 y 55 dependen enteramente de una figura.** **El temario no la describe**, y **lo
   que aporta en su lugar son dos reglas de familia**: cómo se reconoce cada polarización de un
   transistor de efecto campo por dónde están sus resistencias, y que el rendimiento de un regulador
   lineal es el cociente de tensiones. **Ninguna sustituye a ver el esquema**, y **el tema lo dice.**
2. **Los rendimientos del epígrafe 3 —del 85 al 95 % en conmutados— son órdenes de magnitud de uso
   corriente**, no especificaciones. **Ninguna pregunta depende de ellos.**
3. **La tabla de componentes del epígrafe 2 es una clasificación asentada de la electrónica de
   potencia**, no normalizada por ninguna norma consultada. **El tema la presenta como conocimiento
   común de la materia**, y **lo que la pregunta 29 mide —qué separa un IGBT de un bipolar y de un
   transistor de señal— es lo que esa tabla sostiene.**

**El resto del tema va como oficio y así se declara**: la distinción entre electrónica de señal y de
potencia, la diferencia entre componentes que se apagan solos y componentes que se apagan cuando uno
quiere, las cuatro polarizaciones de un transistor de efecto campo, el rendimiento de un regulador
lineal frente a uno conmutado y la tabla de equipos. **Nada de eso está en un boletín oficial ni en
una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
