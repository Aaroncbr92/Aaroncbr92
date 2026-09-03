# Tema 7 del específico de Técnica de Equipos y Sistemas Electrónicos · Memorias, lógica programable y microprocesadores

Las siglas de este tema, presentadas de entrada: la memoria de acceso aleatorio (**RAM**, *random
access memory*) y la de sólo lectura (**ROM**, *read-only memory*); sus variantes programables
(**PROM**), borrables (**EPROM**) y borrables eléctricamente (**EEPROM**); la memoria estática
(**SRAM**) y la dinámica (**DRAM**); la memoria flash; el dispositivo lógico programable (**PLD**,
*programmable logic device*) y sus parientes mayores, la matriz de puertas programable en campo
(**FPGA**) y el circuito integrado de aplicación específica (**ASIC**); la unidad central de proceso
(**CPU**); el conjunto redundante de discos independientes
(**RAID**, *redundant array of independent disks*), que este tema sólo nombra de pasada y el tema 10
desarrolla; y el bus de datos, el de direcciones y el de control.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, puntos 8 y 9):
> «CIRCUITOS LÓGICOS PROGRAMABLES: Concepto de memoria. Memorias RAM. Memorias ROM. PLD
> combinacionales.»
> «MICROPROCESADORES: Memoria, Registros y puertos.»

**Una pregunta.** **Dos puntos enteros del anexo con una sola pregunta entre los dos**, y **hay que
decirlo antes de estudiar: no es un punto rentable por pregunta.**

**Lo que sí es**: **la base de por qué un equipo moderno se «cuelga», por qué hay que actualizar
firmware y por qué un mismo bastidor puede hacer cosas distintas según lo que se le cargue.** **Eso es
materia del tema 15 y del 16, y aquí está su fundamento.**

<!-- indice -->

## Índice

- [1. Qué es una memoria](#1-qué-es-una-memoria)
- [2. La memoria caché](#2-la-memoria-caché)
- [3. Los dispositivos lógicos programables](#3-los-dispositivos-lógicos-programables)
- [4. El microprocesador](#4-el-microprocesador)
- [5. La única pregunta y lo que deja](#5-la-única-pregunta-y-lo-que-deja)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Qué es una memoria

**Un dispositivo que guarda información y la devuelve cuando se le pide.** **Y se clasifica por dos
criterios que hay que separar:**

| Criterio | Las dos opciones |
|---|---|
| **¿Se puede escribir en uso normal?** | **De lectura y escritura (RAM)** frente a **de sólo lectura (ROM)** |
| **¿Conserva el contenido sin alimentación?** | **No volátil** frente a **volátil** |

**Y la trampa de nombres que casi todo el mundo arrastra**: **«RAM» significa acceso ALEATORIO, no
«volátil».** **El nombre se refiere a que se puede llegar a cualquier posición directamente, sin
recorrer las anteriores.** **Que la RAM de un ordenador sea volátil es una propiedad de su tecnología,
no de su nombre.**

**El cuadro completo:**

| Memoria | Se escribe | Conserva sin corriente | Dónde |
|---|---|---|---|
| **SRAM** | **Sí, rápido** | **No** | **Caché y registros** |
| **DRAM** | **Sí** | **No**, y **necesita refresco constante** | **Memoria principal** |
| **ROM** | **No**: se graba en fabricación | **Sí** | **Arranque de equipos antiguos** |
| **PROM** | **Una sola vez** | **Sí** | |
| **EPROM** | **Se borra con luz ultravioleta** | **Sí** | **Equipos de los años ochenta y noventa** |
| **EEPROM** | **Se borra eléctricamente, byte a byte** | **Sí** | **Configuración y calibración de equipos** |
| **Flash** | **Se borra eléctricamente, por bloques** | **Sí** | **Firmware, tarjetas y unidades de estado sólido** |

## 2. La memoria caché

**Una memoria caché es una memoria de alta velocidad y relativamente pequeña que guarda los datos e
instrucciones de uso más frecuente para que la unidad central de proceso llegue antes a ellos.** Ésa
es la respuesta oficial a la pregunta 36.

**Y las dos palabras que la definen son «alta velocidad» y «pequeña»**, que **es exactamente lo que la
opción a) invierte**: **dice «de menor tamaño y MÁS LENTA», y para operaciones «más lentas».** **Es la
respuesta correcta con el adjetivo del revés**, y **por eso es la falsa mejor construida del punto.**

**Por qué existe la caché**: **porque la memoria principal es mucho más lenta que el procesador.**
**Si la CPU tuviera que esperar a la memoria en cada acceso, pasaría la mayor parte del tiempo
parada.** **La caché aprovecha que los programas piden una y otra vez las mismas posiciones —el
llamado principio de localidad— para tener a mano lo que va a hacer falta.**

**La jerarquía de memoria completa, de más rápida a más lenta:**

| Nivel | Velocidad | Tamaño |
|---|---|---|
| **Registros** | **La máxima** | **Unas decenas de palabras** |
| **Caché** | **Muy alta** | **De kilobytes a decenas de megabytes** |
| **Memoria principal** | **Alta** | **Gigabytes** |
| **Almacenamiento** | **Baja** | **Terabytes**: es el RAID del tema 10 |

**Y la regla que la explica entera**: **cuanto más rápida es una memoria, más cara es por byte y menos
cantidad se pone.** **La jerarquía existe para dar la ilusión de tener mucha memoria muy rápida sin
pagarla.**

## 3. Los dispositivos lógicos programables

**El enunciado los nombra y el examen no los pregunta.** **El tema los cubre porque el programa lo
pide, y porque son lo que hay dentro de casi todo el equipamiento de televisión moderno.**

**Qué son**: **circuitos cuyo comportamiento lógico NO viene fijado de fábrica, sino que se define
cargándoles una configuración.** **El mismo chip puede ser un decodificador, un contador o un
procesador de vídeo según lo que se le cargue.**

| Dispositivo | Qué permite | Cuándo se usa |
|---|---|---|
| **PLD** | **Lógica combinacional programable**: unas cuantas puertas y biestables | **Sustituir varios integrados sueltos** |
| **FPGA** | **Miles o millones de bloques lógicos y memoria**, reconfigurables | **Proceso de vídeo en tiempo real**: es lo que hay en un mezclador o un conversor |
| **ASIC** | **Un circuito hecho a medida, ya no programable** | **Producción en grandes series**: más barato por unidad y más eficiente |

**Y la consecuencia para el mantenimiento, que es lo que enlaza con el tema 15**: **un equipo con FPGA
puede cambiar de funciones con una actualización de firmware.** **Eso es una ventaja —se corrigen
fallos y se añaden formatos— y un riesgo: una actualización interrumpida puede dejar el equipo
inservible.**

## 4. El microprocesador

**El punto 9 del anexo pide «memoria, registros y puertos», que son las tres cosas con las que un
procesador se relaciona con el mundo.**

**Los tres buses por los que se comunica:**

| Bus | Qué lleva | Sentido |
|---|---|---|
| **De direcciones** | **QUÉ posición se quiere** | **Sale del procesador** |
| **De datos** | **El contenido** | **En los dos sentidos** |
| **De control** | **Las órdenes**: leer, escribir, interrumpir | **Sobre todo sale** |

**Y la cuenta que relaciona los dos primeros con el tema 5**: **el ancho del bus de direcciones fija
cuánta memoria se puede direccionar.** **Con n líneas de dirección se llega a 2ⁿ posiciones.**
**Dieciséis líneas dan 65.536 posiciones; treinta y dos dan más de cuatro mil millones.** **Es la misma
potencia de dos del multiplexor del tema 6.**

**Los registros**: **son la memoria interna del procesador, la más rápida de todas.** **Guardan los
operandos con los que la unidad aritmético-lógica trabaja, la dirección de la instrucción en curso y
las banderas de resultado.**

**Los puertos**: **son las ventanas al exterior.** **Un puerto es una dirección que, en vez de llevar a
memoria, lleva a un periférico**, y **por ahí salen y entran las señales que un equipo de televisión
maneja: control de una matriz, lectura de un panel, órdenes por red.**

## 5. La única pregunta y lo que deja

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 36 | Qué es una memoria caché | c) Memoria de alta velocidad y pequeña para los datos de uso frecuente ✔ |

**La única respuesta oficial de estos dos puntos es correcta**, y **no descansa sólo en la plantilla.**

**Y el aviso de reparto, dicho sin adornos**: **dos puntos del anexo y una pregunta.** **Este es, junto
con el 11, el punto menos rentable de la ocupación por hora de estudio.** **Conviene leerlo, quedarse
con la jerarquía de memoria y con qué es una FPGA —porque reaparece en mantenimiento— y volcar el
tiempo en los puntos 10, 12 y 2, que se llevan cuarenta y cuatro preguntas entre los tres.**

## 6. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son las memorias, la lógica programable y los
microprocesadores, y **va entera como oficio.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema** | La única **va como oficio** |

**Tres declaraciones expresas:**

1. **La clasificación de memorias del epígrafe 1 es conocimiento asentado de la arquitectura de
   computadores**, no normalizado por ninguna norma consultada. **El tema la presenta como conocimiento
   común de la materia.**
2. **Los tamaños de caché del epígrafe 2 son órdenes de magnitud de uso corriente**, no
   especificaciones, y **ninguna pregunta depende de ellos.**
3. **Este tema desarrolla DOS puntos del anexo con UNA sola pregunta detrás.** **Todo lo que va más
   allá de la definición de caché se escribe contra el programa, no contra el examen**, y **el temario
   lo declara para que quien estudie reparta el tiempo sabiéndolo.**

**El resto del tema va como oficio y así se declara**: los dos criterios de clasificación de memorias
y la trampa del nombre «RAM», la razón de ser de la caché y la jerarquía de memoria, la diferencia
entre PLD, FPGA y ASIC con su consecuencia para el mantenimiento, y los tres buses del
microprocesador con la relación entre líneas de dirección y posiciones direccionables. **Nada de eso
está en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como
si lo estuviera.
