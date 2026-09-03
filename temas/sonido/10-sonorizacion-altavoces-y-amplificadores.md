# Tema 10 del específico de Sonido · Sonorización: altavoces y amplificadores

Los términos de este tema, presentados de entrada: el altavoz electrodinámico y sus piezas —la bobina
móvil, el imán permanente, el yugo, la araña y el diafragma—; la caja acústica o bafle; el filtro de
cruce o divisor de frecuencias (*crossover*); la sensibilidad, expresada en decibelios por vatio a un
metro (**dB/W/m**, que el examen escribe **dBw/m**); la directividad; la distorsión armónica total
(**THD**), que el tema 1 ya presentó; y el acoplamiento o realimentación acústica, que el oficio llama
«acople».

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 8):
> «SONORIZACIÓN. Altavoces: Tipos, características y funcionalidad. Amplificadores: Tipos,
> características y funcionalidad. Acústica para la sonorización de salas.»

**Seis preguntas.** **Y el punto que cierra la cadena**: **todo lo que los nueve temas anteriores han
captado, mezclado y tratado sale por aquí.**

**Su reparto**: **cinco preguntas son de altavoz —su caja, su directividad, su sensibilidad, su
fidelidad y su filtro de cruce— y una es de alineación temporal de un sistema.** **Ninguna es de
amplificador**, aunque el enunciado los pida: **la de clases de amplificador cayó en el punto 1.2 y
está en el tema 1.**

<!-- indice -->

## Índice

- [1. El altavoz electrodinámico](#1-el-altavoz-electrodinámico)
- [2. La caja acústica](#2-la-caja-acústica)
- [3. La directividad](#3-la-directividad)
- [4. La sensibilidad](#4-la-sensibilidad)
- [5. El filtro de cruce](#5-el-filtro-de-cruce)
- [6. La alineación temporal](#6-la-alineación-temporal)
- [7. El acoplamiento](#7-el-acoplamiento)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. El altavoz electrodinámico

**Es el que lleva casi todo lo que suena**, y **sus piezas explican las dos preguntas del cuadernillo
que van de su construcción:**

| Pieza | Qué hace |
|---|---|
| **Imán permanente y yugo** | **Crean el campo magnético fijo** en el que trabaja la bobina |
| **Bobina móvil** | **Recibe la corriente de audio** y se mueve dentro de ese campo |
| **Diafragma o cono** | **Convierte ese movimiento en presión** sobre el aire |
| **Araña** | **Centra la bobina** y la devuelve a su sitio: es una suspensión, no un contacto |
| **Suspensión exterior** | **Cierra el borde del cono** y limita el recorrido |

**La pregunta 88**: **en un altavoz electrodinámico, la fidelidad aumenta si la relación entre la
longitud de la bobina móvil y su número de espiras es la acertada.** Ésa es la respuesta oficial.

**Por qué**: **la fuerza que mueve el cono es proporcional a cuántas espiras están dentro del campo
magnético.** **Si la bobina se sale del entrehierro cuando el cono llega lejos, la fuerza deja de ser
proporcional a la corriente y aparece distorsión.** **La relación entre longitud de bobina y altura
del entrehierro es lo que decide que el altavoz siga siendo lineal en todo su recorrido**, y **ésa es
la definición de fidelidad.**

**Las tres opciones falsas se caen por razones de física, y las tres merecen mirarse:**

1. **«La araña asegura un estrecho contacto de la bobina con el imán y el yugo»** **describe justo lo
   contrario de lo que la araña hace**: **la bobina NO debe tocar nada.** **Si roza, el altavoz
   rasca.** **La araña la mantiene centrada SIN contacto.**
2. **«Aprovechamos las vibraciones transmitidas a la carcasa del bafle»** **describe un defecto**:
   **una caja que vibra añade sonido que no está en la señal.** **Las cajas se refuerzan por dentro
   precisamente para que no lo hagan.**
3. **«El campo magnético del imán es lo más ligero posible»** **es lo contrario de lo que conviene**:
   **a más campo, más fuerza y más control.** **Confunde ligereza del imán con debilidad del campo.**

## 2. La caja acústica

**La capacidad de una caja acústica se mide en litros.** Ésa es la respuesta oficial a la pregunta 13.

**Es una pregunta de las que parecen fáciles y miden un concepto**: **la caja acústica no es un
componente eléctrico, es un VOLUMEN de aire.** **Y el volumen de aire encerrado detrás del cono se
comporta como un muelle que interviene en el comportamiento del altavoz**, sobre todo en graves.

**Las tres opciones falsas son unidades eléctricas o de potencia** —faradios, microfaradios y
vatios—, y **la trampa está en la palabra «capacidad»**: **en electricidad la capacidad se mide en
faradios**, y **quien lea «capacidad» sin leer «caja acústica» cae.**

**Los tres tipos de caja que hay que distinguir:**

| Tipo | Cómo es | Qué consigue |
|---|---|---|
| **Cerrada** | **Volumen sellado** | **Respuesta más controlada** y caída suave en graves |
| **Bass-reflex** | **Lleva un tubo o puerto sintonizado** | **Más rendimiento en graves** a cambio de una caída más brusca por debajo |
| **De pabellón** (*horn*) | **Acopla el cono al aire por una bocina** | **Rendimiento muy alto y directividad controlada**: es la de refuerzo sonoro grande |

## 3. La directividad

**En un altavoz, lo que indica cómo se distribuye su radiación en el espacio es la directividad.** Ésa
es la respuesta oficial a la pregunta 14.

**Es el mismo concepto que el diagrama polar del micrófono del tema 5, del otro lado de la cadena**:
**allí decía de dónde capta; aquí dice hacia dónde emite.**

**Y su regla fundamental es la de la longitud de onda del tema 2**: **un altavoz es direccional cuando
su diámetro es comparable o mayor que la longitud de onda que emite.** **De ahí que:**

1. **Los graves sean prácticamente omnidireccionales**: **una onda de cinco metros rodea cualquier
   caja.** **Por eso el subgrave se puede poner donde quepa y por eso se oye la fiesta del vecino.**
2. **Los agudos sean muy direccionales**: **fuera del eje se pierden.** **Por eso un sistema mal
   apuntado suena apagado en las esquinas.**
3. **La bocina exista**: **es la manera de dar directividad controlada a las frecuencias medias y
   altas**, y **de cubrir un público concreto sin iluminar las paredes.**

**Las tres opciones falsas nombran otras tres especificaciones reales del mismo altavoz**:
**impedancia eléctrica** —la carga que presenta a la etapa, del tema 1—, **distorsión** y
**potencia.** **Ninguna dice nada sobre el reparto en el espacio.**

## 4. La sensibilidad

**Una sensibilidad de 90 dB/W/m significa que el altavoz produce un nivel de presión sonora de 90
decibelios cuando se le suministra 1 vatio de potencia y se mide a 1 metro de distancia.** Ésa es la
respuesta oficial a la pregunta 66.

**La especificación tiene tres partes y las tres están en el nombre**: **decibelios de presión, por
vatio de entrada, a un metro.** **Es un rendimiento: cuánta presión da por cuánta potencia recibe.**

**Y es el dato que decide cuánta etapa hace falta**, con la regla del tema 2 aplicada dos veces:

| Cambio | Efecto en el nivel |
|---|---|
| **Doblar la POTENCIA** | **+3 dB** |
| **Doblar la DISTANCIA** | **−6 dB** |
| **+3 dB de sensibilidad** | **La mitad de potencia para el mismo nivel** |

**Con ella se entiende por qué la sensibilidad importa más que la potencia**: **un altavoz de 93 dB/W/m
con 100 vatios suena igual que uno de 90 dB/W/m con 200.** **Tres decibelios de sensibilidad valen por
doblar la etapa.**

**Las tres opciones falsas cambian uno de los tres términos**: **ponen 10 vatios en lugar de 1,
confunden decibelios con vatios de potencia acústica, o meten la distorsión armónica donde no viene a
cuento.** **La pregunta se acierta leyendo la unidad: dB por W a un m.**

## 5. El filtro de cruce

**Linkwitz-Riley es un tipo de filtro de cruce.** Ésa es la respuesta oficial a la pregunta 38.

**Qué hace un filtro de cruce**: **repartir el espectro entre las vías del sistema.** **Manda los
graves al altavoz de graves y los agudos al de agudos**, porque **ningún transductor cubre bien las
diez octavas del margen audible.**

**Y por qué el Linkwitz-Riley es el nombre que se pregunta**: **porque es el que resuelve el problema
de la suma en la frecuencia de corte.** **En un cruce, las dos vías emiten a la vez alrededor del
punto de corte**, y **lo que se oye es la SUMA de las dos.** **Un filtro mal elegido suma con un
bache o con un pico.** **El Linkwitz-Riley está diseñado para que las dos vías, sumadas, den respuesta
plana y en fase.**

**Las tres opciones falsas —mezclador de micrófonos, limpiador de voz y conversor
analógico-digital— no tienen relación con el reparto del espectro**, y **la pregunta se contesta
sabiendo que es un nombre propio de la teoría de filtros.**

**Y el filtro de cruce puede estar en dos sitios, que es lo que separa dos formas de montar un
sistema:**

| Dónde | Cómo es | Dónde se usa |
|---|---|---|
| **Pasivo** | **Bobinas y condensadores DENTRO de la caja**, después de la etapa | **Cajas de estudio y de instalación pequeña** |
| **Activo** | **Antes de las etapas**, con una etapa por vía | **Refuerzo sonoro profesional**: más control y mejor rendimiento |

## 6. La alineación temporal

**Con dos altavoces a 4 y a 38 metros de un oyente, hay que aplicar 100 milisegundos de delay al
altavoz más cercano** para que los dos lleguen a la vez. Ésa es la respuesta oficial a la pregunta 60.

**La cuenta, con los 340 metros por segundo que el enunciado da:**

1. **La diferencia de camino**: **38 − 4 = 34 metros.**
2. **El tiempo de esos 34 metros**: **34 ÷ 340 = 0,1 segundos = 100 milisegundos.**

**Y la parte que la pregunta mide de verdad no es la cuenta, sino A CUÁL se le aplica**: **al MÁS
CERCANO.** **El sonido del lejano ya va retrasado por el camino que tiene que recorrer; lo único que
se puede hacer es esperar al que llega antes.** **Retrasar el lejano lo empeoraría.**

**Las cuatro opciones cruzan las dos variables** —la cifra y a cuál se aplica—, y **sólo una acierta
las dos:**

| Opción | Cifra | A cuál | |
|---|---|---|---|
| **a)** | **40 ms** ✗ | **Al lejano** ✗ | Falla las dos |
| **b)** ✔ | **100 ms** ✔ | **Al cercano** ✔ | **La respuesta** |
| **c)** | **120 ms** ✗ | **Al cercano** ✔ | Falla la cifra |
| **d)** | **50 ms** ✗ | **Al lejano** ✗ | Falla las dos |

**El atajo que conviene tener, y con él estas preguntas se hacen de cabeza**: **el sonido recorre
aproximadamente un metro cada 3 milisegundos.** **34 metros, unos 100 milisegundos.**

**Y por qué esto se hace en un sistema real**: **en un recinto largo se ponen refuerzos a mitad de
sala.** **Si esos refuerzos no se retrasan, el público de esa zona oye primero el refuerzo y después
el escenario, y la voz parece venir del altavoz de al lado en vez de la persona que habla.** **Con el
retardo bien puesto, el escenario llega primero o a la vez y el oído sigue localizando allí la
fuente**: **es el efecto de precedencia del tema 4.**

## 7. El acoplamiento

**El enunciado del punto pide acústica para la sonorización de salas y el examen no la pregunta
directamente**, pero **el acoplamiento aparece en la pregunta del filtro notch del tema 7 y merece
quedar explicado aquí.**

**El acople se produce cuando el sonido de los altavoces vuelve al micrófono con nivel suficiente para
que el lazo se sostenga solo.** **Y las cinco maneras de ganarle margen, en orden de eficacia:**

1. **Acercar el micrófono a la fuente.** **Cada mitad de distancia da 6 decibelios más de señal útil
   sin subir nada.**
2. **Alejar los altavoces del micrófono** y **apuntarlos donde el micrófono no capta** —los nulos del
   tema 5—.
3. **Usar micrófonos direccionales.**
4. **Tratar la sala**: **menos reverberación es menos energía volviendo.**
5. **Y sólo al final, ecualizar con un notch** las frecuencias que se disparen.

**El orden importa**: **ecualizar es lo último porque es lo que menos margen da y lo que más
deteriora el sonido.**

## 8. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 13 | En qué se mide la capacidad de una caja acústica | a) Litros ✔ |
| 14 | Qué indica cómo se reparte la radiación de un altavoz | b) Directividad ✔ |
| 38 | Qué es Linkwitz-Riley | a) Un tipo de filtro de cruce ✔ |
| 60 | Delay para alinear dos altavoces a 4 y 38 metros | b) 100 ms al más cercano ✔ |
| 66 | Qué significa una sensibilidad de 90 dB/W/m | a) 90 dB con 1 vatio a 1 metro ✔ |
| 88 | De qué depende la fidelidad de un altavoz electrodinámico | d) De la relación entre longitud de bobina y espiras ✔ |

**Las seis respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Y el aviso de estudio**: **la pregunta 60 es la más rentable del cuadernillo entero**, porque **es
la única que se resuelve con una división y sin saber nada de sonido.** **34 entre 340.**

## 9. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son los altavoces, los amplificadores y la
sonorización de salas, y **va entera como oficio.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| — | **Ninguna norma sostiene este tema** | Las seis **van como oficio** |

**Tres declaraciones expresas:**

1. **La velocidad del sonido de 340 metros por segundo la da el propio enunciado de la pregunta 60**,
   y **el temario la usa porque la pregunta la impone.** **El valor real depende de la temperatura**
   —a 20 grados ronda los 343— **y ninguna respuesta de este tema depende de esa diferencia.**
2. **El nombre Linkwitz-Riley designa una familia de filtros de la teoría de circuitos**, y **este
   proyecto no ha volcado ninguna fuente de esa disciplina.** **Lo que el tema sostiene es qué hace un
   filtro de cruce y por qué ese diseño concreto suma plano en el corte**, que **es lo que hace la
   pregunta contestable.**
3. **Las tres reglas de la tabla del epígrafe 4 —tres decibelios por doblar potencia, seis por doblar
   distancia— son consecuencias de la aritmética del decibelio del tema 2**, y **la de la distancia
   supone campo libre.** **En una sala con reverberación la caída real es menor**, y **el tema lo dice
   en lugar de presentar la regla como universal.**

**El resto del tema va como oficio y así se declara**: las piezas del altavoz electrodinámico y por
qué la linealidad de la bobina es la fidelidad, los tres tipos de caja, la relación entre diámetro y
longitud de onda que explica la directividad, la lectura de la sensibilidad, la diferencia entre
cruce activo y pasivo, la alineación temporal y las cinco maneras de ganar margen antes del acople.
**Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo
presenta como si lo estuviera.
