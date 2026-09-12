# Tema 13 del específico de Técnica de Equipos y Sistemas Electrónicos · Equipos de medida y control

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica de Equipos y Sistemas Electrónicos · punto 15 |
| **Sirve para** | **Técnica de Equipos y Sistemas Electrónicos** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los instrumentos de medida, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Tres de las ocho preguntas dependen de una pantalla.** En una de ellas —la frecuencia de una senoide— **el temario escribe el método de cálculo entero**, porque la figura sólo aporta el número de divisiones que ocupa un ciclo |
| **Extensión** | **3.527 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la modulación de amplitud (**AM**) y la modulación de
frecuencia (**FM**); la difusión de vídeo digital terrestre de segunda generación (**DVB-T2**); la
señal de reloj de un microprocesador (**CLK**, de *clock*); el megahercio (**MHz**) y el gigahercio
(**GHz**); el milivoltio (**mV**); el vatio (**W**) y el kilovatio (**kW**); la radiofrecuencia
(**RF**); el conector coaxial roscado de la serie N (**conector N**); y la designación del cable
coaxial de cincuenta ohmios **RG213U**, que es una referencia de catálogo y no unas siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 15):
> «EQUIPOS DE MEDIDA Y CONTROL: Polímetro, osciloscopio, monitor de audio, monitor de forma de onda de
> señal compuesta, en componentes y digital, vectorscopio y monitor de imagen. Analizador de espectro.
> Medidor de campo. Vúmetro, Picómetro, Watímetro. Medidor de Redes de RF. Medidor de modulación.
> Analizador de audio.»

**Ocho preguntas.** **Y el punto que define el oficio de esta ocupación**: **un técnico de equipos y
sistemas electrónicos es, antes que nada, alguien que mide.**

**Su reparto**: **cuatro preguntas son de osciloscopio**, **una de polímetro**, **una de reconocer un
instrumento que no lo es**, **una de medida sin instrumento** y **una de adaptación de conectores en
radiofrecuencia.**

**Tres de las ocho dependen de una figura** —la 49 del primer cuadernillo y la 12 y la 19 del
segundo—, y **este tema no describe ninguna de las tres**: da la regla de su familia y declara que la
respuesta descansa en la plantilla. **En la 12, además, se escribe el método completo de cálculo**,
porque **la figura sólo aporta un dato que el opositor sabría leer si la tuviera delante.**

<!-- indice -->

## Índice

- [1. El osciloscopio: qué es y cómo se maneja](#1-el-osciloscopio-qué-es-y-cómo-se-maneja)
- [2. Las dos preguntas de osciloscopio con figura](#2-las-dos-preguntas-de-osciloscopio-con-figura)
- [3. El polímetro y las medidas sin instrumento](#3-el-polímetro-y-las-medidas-sin-instrumento)
- [4. Los instrumentos del punto, y el que no lo es](#4-los-instrumentos-del-punto-y-el-que-no-lo-es)
- [5. La medida de potencia en radiofrecuencia](#5-la-medida-de-potencia-en-radiofrecuencia)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. El osciloscopio: qué es y cómo se maneja

**El osciloscopio dibuja la tensión frente al tiempo.** **Ésa es toda su definición**, y de ella salen
sus dos mandos fundamentales:

| Mando | Qué gradúa | En qué unidades |
|---|---|---|
| **Amplitud, o base de tensión** | **El eje vertical** | **Voltios por división** |
| **Base de tiempos** | **El eje horizontal** | **Segundos por división** |
| **Disparo** | **En qué punto de la señal empieza a dibujar, para que la traza se quede quieta** | **Nivel de tensión y flanco** |

**La pregunta 73 va del reparto de esos mandos entre canales**: **en un osciloscopio de dos canales,
la base de tiempos es única para los dos canales.** Ésa es la respuesta oficial.

---

**Y el porqué es el motivo mismo de que un osciloscopio tenga dos canales**: **se ponen dos señales a
la vez para compararlas en el tiempo.** **Si cada canal tuviera su propia base de tiempos, las dos
trazas no serían comparables y el aparato no serviría para lo único para lo que se compran dos
canales: ver el retardo entre una señal y otra.**

**Las otras tres opciones, y por qué son falsas:**

| Opción | Por qué no |
|---|---|
| **a) Un canal mide tensiones y el otro corrientes** | **Un osciloscopio mide siempre tensión.** **Para ver corriente hace falta una pinza o una resistencia que la convierta en tensión** |
| **b) El control de amplitud es único** | **Es justo al revés: cada canal tiene el suyo**, porque las dos señales suelen ser de tamaños muy distintos |
| **d) El disparo se establece por separado para cada canal** | **El disparo es uno solo, y se elige de qué canal se toma.** **Si hubiera dos, cada traza empezaría en un sitio y volverían a ser incomparables** |

**La regla que resume las cuatro**: **lo que es del eje vertical va por canal; lo que es del eje
horizontal es común.**

**La pregunta 24 del segundo cuadernillo va de sondas**: **al medir la señal de reloj de un
microprocesador, con frecuencias entre 100 MHz y 5 GHz, es recomendable usar una sonda de alta
impedancia para evitar afectar a la señal de reloj.** Ésa es la respuesta oficial.

---

**El principio que hay detrás vale para toda medida eléctrica**: **el instrumento forma parte del
circuito que mide.** **Una sonda de baja impedancia carga el nodo**: le roba corriente, le baja la
amplitud y, a estas frecuencias, le redondea los flancos hasta el punto de que el reloj deje de
funcionar mientras se mide. **La medida altera lo medido, y en una señal de reloj eso significa que
el equipo se para al poner la punta.**

**Las tres opciones falsas dicen tres cosas peligrosas**: **la a recomienda precisamente lo que carga
el circuito; la c afirma que el apantallamiento evita el problema, que confunde el ruido captado con
la carga introducida; y la d propone pinchar el bus de datos, que no es donde está el reloj y que
además multiplicaría el estropicio.**

**El aviso de oficio que conviene llevar**: **la sonda es parte del instrumento y hay que
compensarla.** **Una sonda descompensada deforma los flancos aunque su impedancia sea la debida**, y
por eso todos los osciloscopios llevan una salida de onda cuadrada de calibración en el frontal.

## 2. Las dos preguntas de osciloscopio con figura

**La pregunta 12 del segundo cuadernillo** enseña una senoide en un osciloscopio con la base vertical
en 500 mV por división y la horizontal en 200 microsegundos por división, y pide la frecuencia. **La
plantilla da 1 kHz.**

**Aquí el método se escribe entero, porque la figura sólo aporta el número de divisiones que ocupa un
ciclo**, y **ese número es lo único que el opositor tendría que leer si tuviera la imagen delante:**

1. **Se cuentan las divisiones horizontales que ocupa un ciclo completo**, de un paso por cero
   ascendente al siguiente.
2. **Se multiplican por lo que vale cada división**: en este caso, 200 microsegundos. **El resultado
   es el periodo.**
3. **La frecuencia es la inversa del periodo.**

**Y la tabla de correspondencia con las cuatro opciones, que se puede construir sin ver nada:**

| Divisiones por ciclo | Periodo | Frecuencia |
|---|---|---|
| **5** | **1.000 microsegundos, es decir 1 milisegundo** | **1 kHz** |
| **2,5** | **500 microsegundos** | **2 kHz** |
| **0,5** | **100 microsegundos** | **10 kHz** |
| **0,25** | **50 microsegundos** | **20 kHz** |

**La respuesta oficial, 1 kHz, corresponde a un ciclo que ocupa cinco divisiones**, que es además la
lectura más cómoda de dibujar en una pantalla de diez divisiones: **dos ciclos completos y
centrados.** **El dato de los 500 mV por división no interviene en el cálculo**: **está en el
enunciado para comprobar que el opositor sabe que la frecuencia sale del eje horizontal.** **Aun así,
la lectura concreta descansa en la figura y por tanto en la plantilla**, y el temario lo declara.

**La pregunta 49 del primer cuadernillo** enseña una imagen de osciloscopio y pide qué representa.
**La plantilla da una señal de radio AM con una modulación del 100 %.** **Este temario no ha visto la
imagen y no la describe.** **La regla de la familia:**

| Qué se ve en el osciloscopio | Qué es |
|---|---|
| **Una portadora cuya envolvente sube y baja pero nunca llega a cero** | **Modulación de amplitud con índice menor del 100 %** |
| **Una portadora cuya envolvente llega justo a tocar el cero en los mínimos** | **Modulación de amplitud al 100 %** |
| **Una portadora cuya envolvente cruza el cero y se invierte** | **Sobremodulación: más del 100 %** |
| **Una banda de amplitud constante y anchura variable** | **Modulación de frecuencia: la amplitud no cambia** |
| **Un ruido de amplitud aparentemente aleatoria y espectro plano** | **Una portadora digital como la del DVB-T2** |

**Y el porqué de las tres opciones falsas**: **la a dice modulación de frecuencia, cuya envolvente en
el osciloscopio es plana y por tanto no se parece en nada a lo que una pregunta sobre porcentaje de
modulación puede estar enseñando; la b dice DVB-T2, que en el dominio del tiempo se ve como ruido; y
la c dice el 50 %, que es la misma familia que la respuesta y se distingue sólo por si la envolvente
toca el cero o no.** **La pregunta se juega entre la c y la d**, y **la diferencia es exactamente
ésa**: **al 100 % la envolvente toca el cero; al 50 % se queda a la mitad.** **La lectura concreta
descansa en la plantilla**, y el temario lo declara.

**Cómo se define el índice de modulación, que es lo que hay que llevar aprendido**: **es la razón
entre la amplitud de la moduladora y la de la portadora, expresada en tanto por ciento.** **Al 100 %
la envolvente llega a cero en los mínimos y al doble en los máximos.** **Pasar del 100 % no da más
alcance: da distorsión y ensancha el espectro más de lo permitido.**

## 3. El polímetro y las medidas sin instrumento

**La pregunta 13 del segundo cuadernillo**: **para medir la continuidad de un componente o un cable,
el multímetro se coloca en la posición de ohmímetro (Ω).** Ésa es la respuesta oficial.

---

**Y la razón es de definición**: **la continuidad es que haya camino, y que haya camino es que la
resistencia sea prácticamente nula.** **La posición de ohmímetro es la que mide eso.** **Casi todos
los aparatos llevan además un zumbador asociado a esa misma posición, que pita por debajo de unos
pocos ohmios**, y ésa es la comodidad que hace la prueba de cable tan rápida.

**Las cuatro posiciones del polímetro y para qué son:**

| Posición | Qué mide | Cómo se conecta |
|---|---|---|
| **Voltímetro (V)** | **Tensión** | **En paralelo con el elemento, sin cortar nada** |
| **Amperímetro (A)** | **Corriente** | **En serie: hay que abrir el circuito** |
| **Ohmímetro (Ω)** | **Resistencia y continuidad** | **Con el circuito sin alimentar** ✔ |
| **Capacitancia (F)** | **Capacidad** | **Con el condensador descargado y fuera del circuito** |

**Los dos avisos que hacen falta**: **el ohmímetro sólo se usa con el circuito desconectado de la
alimentación**, porque **inyecta él su propia corriente y una tensión externa falsea la lectura o
estropea el aparato**; **y el amperímetro es el único que obliga a abrir el circuito**, que es el
motivo de que casi nadie lo use si puede evitarlo.

**La pregunta 11 del segundo cuadernillo es la más ingeniosa del punto**: **la polaridad de un altavoz
se puede averiguar, sin conectarlo a una fuente de señal, conectando una pila y observando el
movimiento del cono.** Ésa es la respuesta oficial.

---

**Cómo funciona**: **la bobina móvil recibe una corriente continua, el campo del imán la empuja en un
sentido u otro según el signo, y el cono sale o entra.** **El convenio del sector es que con el
positivo de la pila en el terminal positivo del altavoz el cono sale hacia fuera.** **Un toque breve
basta**, y **el toque tiene que ser breve**: **una pila conectada de forma permanente a una bobina de
pocos ohmios la calienta.**

**Para qué sirve esto en la práctica**: **dos altavoces de un mismo sistema conectados con polaridad
opuesta se cancelan en las frecuencias graves.** **Se oye poco grave y el sonido se descoloca sin que
haya avería en ninguna pieza.** **Es una de las averías más difíciles de encontrar por oído y una de
las más fáciles de encontrar con una pila.**

**Las tres opciones falsas**: **el calibre mide dimensiones y no dice nada de polaridad; un diodo
polarizado necesita corriente que alguien le dé, y el enunciado prohíbe expresamente la fuente de
señal; y una lámpara de 12 voltios tampoco genera corriente por sí sola.** **La pila es el único
elemento de los cuatro que es a la vez fuente y no es fuente de señal**, y ahí está la gracia del
enunciado.

## 4. Los instrumentos del punto, y el que no lo es

**La pregunta 64 es negativa**: **el instrumento técnico que NO se utiliza en el diagnóstico de
problemas específicos en los equipos es el «Trompeter».** Ésa es la respuesta oficial.

---

**Y la razón es que no es un instrumento**: **Trompeter es un fabricante de conectores y paneles de
conexión coaxial**, muy presente en las instalaciones de televisión, **y su nombre se ha convertido en
el sector en sinónimo del panel de conexiones.** **Un panel de conexiones no diagnostica nada: es
cableado.** **Las otras tres opciones —polímetro, osciloscopio y generador de señales— son los tres
instrumentos básicos de cualquier banco de trabajo.**

**El generador de señales merece una línea, porque es el que menos se estudia**: **no mide, genera.**
**Es la pareja del osciloscopio**: se inyecta una señal conocida por la entrada de una etapa y se mira
por el osciloscopio qué sale por su salida. **Con esa pareja se recorre una cadena averiada etapa a
etapa hasta encontrar dónde deja de aparecer la señal**, que es el método del tema 15.

**El inventario completo que el enunciado del punto nombra, con lo que hace cada uno:**

| Instrumento | Qué mide |
|---|---|
| **Polímetro** | **Tensión, corriente, resistencia y continuidad** |
| **Osciloscopio** | **La forma de onda: tensión frente a tiempo** |
| **Monitor de forma de onda** | **La señal de vídeo en el tiempo: niveles, sincronismos, amplitud** |
| **Vectorscopio** | **La crominancia en fase y amplitud: saturación y tinte** |
| **Monitor de imagen** | **Lo que el espectador vería** |
| **Analizador de espectro** | **La energía frente a la frecuencia** |
| **Medidor de campo** | **El nivel y la calidad de una señal de radiodifusión recibida** |
| **Vúmetro** | **Nivel de audio con respuesta lenta** |
| **Picómetro** | **Nivel de audio con respuesta rápida: el valor de pico** |
| **Vatímetro** | **Potencia** |
| **Medidor de redes de RF** | **Cómo se comporta un circuito frente a la frecuencia: pérdidas y adaptación** |
| **Medidor de modulación** | **La desviación o el índice de modulación de un transmisor** |
| **Analizador de audio** | **Distorsión, ruido, respuesta en frecuencia y diafonía de una cadena de sonido** |

**La pareja que más se confunde es el vúmetro y el picómetro**, y **la diferencia es la velocidad de
respuesta**: **el vúmetro sigue la sensación de sonoridad y se salta los transitorios; el picómetro
los caza.** **Los dos hacen falta**: **el primero dice cómo suena de fuerte, el segundo dice si va a
saturar.** **El tema 10 contestó la pregunta 80 con la mitad de esta pareja.**

## 5. La medida de potencia en radiofrecuencia

**La pregunta 19 del segundo cuadernillo** plantea una medida real: **se van a medir equipos de
frecuencia modulada de 500 vatios, se dispone de una carga de 1 kilovatio con conector N hembra y de
un cable RG213U con conectores N macho en los extremos, y la figura enseña el conector de salida de
potencia de los equipos.** **La plantilla da la transición de 1 5/8" a N hembra.** **Este temario no
ha visto la figura y no la describe.**

**Lo que sí se puede razonar entero, y es casi todo:**

1. **El cable acaba en N macho por los dos lados.** **La carga tiene N hembra**, luego **ese extremo
   ya casa.**
2. **El otro extremo necesita, por fuerza, una N hembra donde enchufarse.** **Por eso las tres
   opciones que proponen transición terminan todas en «a N hembra»**: no podían terminar en otra
   cosa.
3. **Lo único que la figura decide es la otra mitad de la transición**, es decir, **qué conector
   tiene la salida del equipo.**
4. **La opción c, «no hace falta transición», sólo sería correcta si la salida del equipo fuera ya
   una N hembra.** **La plantilla la descarta**, luego la figura enseña otra cosa.

**Las medidas que las tres opciones barajan —7/8", 1 5/8" y 3 5/8"— son diámetros de línea coaxial
rígida**, que es como se saca la potencia de un transmisor de radiodifusión. **La regla de la
familia:**

| Diámetro de la línea | Orden de potencia que maneja |
|---|---|
| **7/8"** | **Cientos de vatios** |
| **1 5/8"** | **Unos pocos kilovatios** |
| **3 1/8" y mayores** | **Decenas de kilovatios** |

**Y el aviso que hace útil el ejercicio más allá de la pregunta**: **la carga tiene que aguantar la
potencia que se le va a meter.** **Aquí son 500 vatios contra una carga de 1 kilovatio**, es decir,
**el doble de margen**, que es lo razonable. **Medir 500 vatios contra una carga de 300 la destruye**,
y con ella a veces la etapa de salida del transmisor. **Comprobar el margen de la carga antes de
conectar es la primera regla de la medida de potencia.**

**La segunda regla**: **nunca se mide un transmisor sin carga.** **Una etapa de potencia con la salida
al aire se ve reflejada su propia energía y se destruye.** **Antes de dar potencia, la carga o la
antena tienen que estar conectadas.**

**La identificación del conector de la figura descansa en la plantilla**, y el temario lo declara.

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 49 | Qué representa la imagen de osciloscopio | d) Radio AM con modulación del 100 % ✔ (figura) |
| 64 | Instrumento que NO se usa en el diagnóstico | d) Trompeter ✔ |
| 73 | Afirmación correcta sobre un osciloscopio de dos canales | c) La base de tiempos es única ✔ |
| 11 (2.º llam.) | Cómo hallar la polaridad de un altavoz sin fuente de señal | b) Con una pila, viendo el movimiento del cono ✔ |
| 12 (2.º llam.) | Frecuencia de la senoide de la figura | a) 1 kHz ✔ (figura) |
| 13 (2.º llam.) | Posición del multímetro para medir continuidad | d) Ohmímetro (Ω) ✔ |
| 19 (2.º llam.) | Transición necesaria para medir potencia | a) 1 5/8" a N hembra ✔ (figura) |
| 24 (2.º llam.) | Sonda para medir el reloj de un microprocesador | b) De alta impedancia ✔ |

**Las ocho respuestas oficiales son correctas.** **Tres descansan en la plantilla**, y son las tres que
llevan figura.

**El aviso de estudio**: **cinco de las ocho se contestan con principios que no cambian nunca** —la
base de tiempos común, la carga que introduce la sonda, la posición de ohmímetro, la pila del altavoz
y qué es y qué no es un instrumento—; **y las tres restantes exigen leer una pantalla, que es
justamente lo que este oficio hace todos los días.** **Merece la pena practicar la lectura de un
osciloscopio con divisiones**, porque **la pregunta 12 es enteramente calculable si se ve la
imagen.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Seis declaraciones expresas:**

1. **El cálculo del epígrafe 2 no se toma de ninguna fuente: se hace.** **La frecuencia es la inversa
   del periodo y el periodo es divisiones por escala**, y la tabla de correspondencia se construye con
   esa sola operación. **Su resultado coincide con la respuesta oficial.**
2. **La definición del índice de modulación de amplitud y su lectura en el osciloscopio son
   conocimiento común de la materia.** **Ninguna norma se ha consultado para ellas**, y **la lectura
   de la figura concreta se declara dependiente de la plantilla.**
3. **«Trompeter» es un nombre comercial de fabricante de conectores y paneles.** **Este temario lo
   identifica como tal porque es lo que la respuesta oficial exige para ser correcta —que no sea un
   instrumento— y porque es de uso corriente en el sector**, y **no atribuye a ese fabricante ningún
   catálogo ni ninguna característica de producto concreta.**
4. **Los diámetros de línea coaxial rígida del epígrafe 5 y los órdenes de potencia que se les
   asocian son de uso corriente en radiodifusión.** **No se han tomado de ninguna norma ni de ningún
   catálogo**, y **ninguna respuesta depende de esa correspondencia**: la pregunta 19 se decide por
   la figura.
5. **La designación RG213U es una referencia de catálogo de cable coaxial de cincuenta ohmios**,
   reproducida del enunciado. **El temario no le atribuye ninguna característica que el enunciado no
   dé.**
6. **Las tres preguntas con figura se declaran como tales en los epígrafes 2 y 5 y en el cuadro del
   epígrafe 6.** **Este temario no ha visto ninguna de las tres imágenes y no las describe.**

**El resto del tema va como oficio y así se declara**: la tabla de mandos del osciloscopio y su
reparto entre canales, el principio de que el instrumento carga lo que mide, la compensación de la
sonda, las cuatro posiciones del polímetro con sus avisos, el truco de la pila y su explicación
electromagnética, el inventario de instrumentos del enunciado, la pareja vúmetro-picómetro y las dos
reglas de la medida de potencia. **Nada de eso está en un boletín oficial ni en una norma técnica de
las consultadas**, y el tema no lo presenta como si lo estuviera.
