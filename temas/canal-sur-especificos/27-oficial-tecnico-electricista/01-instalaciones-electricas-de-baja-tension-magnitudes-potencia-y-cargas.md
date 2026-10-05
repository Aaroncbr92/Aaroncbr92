# Tema 1 del específico de Oficial Técnico Electricista · Instalaciones eléctricas de baja tensión: magnitudes, corriente alterna, potencia, energía, factor de potencia, caída de tensión y equilibrado de cargas

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Oficial Técnico Electricista · punto 1 |
| **Sirve para** | Puesto 2.27, Oficial Técnico Electricista (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Real Decreto 842/2002, de 2 de agosto, Reglamento electrotécnico para baja tensión: artículos 2.1, 4 y 16 del Reglamento; ITC-BT-09, ITC-BT-14, ITC-BT-15, ITC-BT-19, ITC-BT-43, ITC-BT-44, ITC-BT-47, ITC-BT-48 e ITC-BT-52. Lo demás es física elemental y oficio, y así se declara |
| **Redacción que se estudia** | La vigente el 24/09/2026. Todos los preceptos citados tienen una sola redacción, la original de 2002 (en vigor desde el 18/09/2003), salvo el artículo 2 (redacción vigente desde el 01/07/2021) y la ITC-BT-52 (redacción vigente desde el 16/06/2022) |
| **Extensión** | Unas 11.000 palabras |

<!-- /portada -->

Siglas y símbolos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Reglamento electrotécnico para baja
tensión (**REBT**) y sus instrucciones técnicas complementarias (**ITC-BT**); corriente alterna
(**CA**) y corriente continua (**CC**); tensión nominal (**Un**); valor eficaz (**RMS**, *root mean
square*); fases de una red trifásica (**L1**, **L2**, **L3**) y neutro (**N**); Asociación Española
de Normalización (**UNE**) y norma europea (**EN**); sistema de alimentación ininterrumpida
(**SAI**). Magnitudes: tensión (**U**), intensidad (**I**), resistencia (**R**), resistividad
(**ρ**) y conductividad (**γ**), reactancia (**X**), impedancia (**Z**), potencia activa (**P**),
reactiva (**Q**) y aparente (**S**), energía (**E**), ángulo de desfase (**φ**) y factor de potencia
(**cos φ**), frecuencia (**f**), periodo (**T**), caída de tensión (**e** o **ΔU**). Unidades:
voltio (**V**), amperio (**A**), ohmio (**Ω**), siemens (**S**), henrio (**H**), faradio (**F**),
hercio (**Hz**), vatio (**W**), kilovatio (**kW**), voltamperio (**VA**, que el REBT escribe también
«voltiamperio»), voltamperio reactivo (**var**), kilovoltamperio (**kVA**) y kilovoltamperio reactivo (**kvar**), julio (**J**), kilovatio hora (**kWh**), milímetro
cuadrado (**mm²**).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.27, punto 1):
>
> Instalaciones eléctricas de baja tensión: magnitudes eléctricas, corriente alterna, potencia,
> energía, factor de potencia, caída de tensión y equilibrado de cargas.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué tensiones abarca la baja tensión y cómo se clasifican; las tensiones
nominales y la frecuencia de la red española; la ley de Ohm, las leyes de Kirchhoff y la resistencia de un conductor; el
valor eficaz, el de pico y el periodo de la red de 50 Hz; la reactancia de bobinas y condensadores;
estrella y triángulo, y la relación entre 230 y 400 V; las tres potencias y sus unidades en
monofásica y en trifásica, y cómo se suman las de varios receptores; la energía y el kilovatio hora; el factor de potencia, sus consecuencias
y lo que el REBT dice de su compensación (cuándo puede y cuándo debe compensarse, el ± 10 %, el 0,9
de las lámparas de descarga, la descarga de los condensadores y la aparamenta que los maniobra); los límites de caída de tensión de
la ITC-BT-19 y los de las líneas generales, derivaciones individuales y alumbrado exterior; las
fórmulas de caída de tensión; el 125 % de los motores y el 1,8 de las lámparas de descarga; el
deber de equilibrar las cargas, la sección del neutro y la corriente que circula por él. En la
prueba práctica: calcular la intensidad, las potencias o la batería de condensadores de una carga,
la caída de tensión o la sección de una línea, la carga de un circuito de alumbrado o de motores, o
repartir circuitos monofásicos entre las tres fases de un cuadro.

<!-- indice -->

## Índice

- [1. Instalaciones eléctricas de baja tensión](#1-instalaciones-eléctricas-de-baja-tensión)
  - [1.1 El campo de la baja tensión](#11-el-campo-de-la-baja-tensión)
  - [1.2 Tensiones nominales y frecuencia de la red](#12-tensiones-nominales-y-frecuencia-de-la-red)
  - [1.3 Las instalaciones interiores o receptoras](#13-las-instalaciones-interiores-o-receptoras)
- [2. Magnitudes eléctricas](#2-magnitudes-eléctricas)
  - [2.1 Tensión, intensidad y resistencia](#21-tensión-intensidad-y-resistencia)
  - [2.2 La ley de Ohm](#22-la-ley-de-ohm)
  - [2.3 La resistencia de un conductor](#23-la-resistencia-de-un-conductor)
  - [2.4 El efecto Joule](#24-el-efecto-joule)
- [3. Corriente alterna](#3-corriente-alterna)
  - [3.1 Corriente continua y corriente alterna](#31-corriente-continua-y-corriente-alterna)
  - [3.2 Las magnitudes de una señal alterna](#32-las-magnitudes-de-una-señal-alterna)
  - [3.3 Resistencias, bobinas y condensadores en alterna](#33-resistencias-bobinas-y-condensadores-en-alterna)
  - [3.4 El sistema trifásico](#34-el-sistema-trifásico)
- [4. Potencia](#4-potencia)
  - [4.1 Las tres potencias](#41-las-tres-potencias)
  - [4.2 Cálculo de potencias e intensidades](#42-cálculo-de-potencias-e-intensidades)
- [5. Energía](#5-energía)
- [6. Factor de potencia](#6-factor-de-potencia)
  - [6.1 Qué es y qué consecuencias tiene](#61-qué-es-y-qué-consecuencias-tiene)
  - [6.2 La compensación con condensadores](#62-la-compensación-con-condensadores)
  - [6.3 Lo que fija el REBT](#63-lo-que-fija-el-rebt)
- [7. Caída de tensión](#7-caída-de-tensión)
  - [7.1 Qué es y por qué importa](#71-qué-es-y-por-qué-importa)
  - [7.2 Los límites del REBT](#72-los-límites-del-rebt)
  - [7.3 Las fórmulas](#73-las-fórmulas)
  - [7.4 Ejemplos resueltos](#74-ejemplos-resueltos)
  - [7.5 Motores y lámparas de descarga](#75-motores-y-lámparas-de-descarga)
- [8. Equilibrado de cargas](#8-equilibrado-de-cargas)
  - [8.1 Lo que exige el REBT](#81-lo-que-exige-el-rebt)
  - [8.2 La corriente por el neutro](#82-la-corriente-por-el-neutro)
  - [8.3 Armónicos, desequilibrio y sección del neutro](#83-armónicos-desequilibrio-y-sección-del-neutro)
  - [8.4 Cómo se equilibra un cuadro](#84-cómo-se-equilibra-un-cuadro)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Instalaciones eléctricas de baja tensión

### 1.1 El campo de la baja tensión

El REBT fija su campo por la tensión nominal. Su artículo 2.1 dice:

> «**El presente Reglamento se aplicará a las instalaciones que distribuyan la energía eléctrica, a
> las generadoras de electricidad para consumo propio y a las receptoras, en los siguientes límites
> de tensiones nominales:
> a) Corriente alterna: igual o inferior a 1.000 voltios.
> b) Corriente continua: igual o inferior a 1.500 voltios.**»
>
> — Real Decreto 842/2002, Reglamento, artículo 2.1, redacción vigente desde el 01/07/2021.

Dentro de ese campo, el artículo 4.1 clasifica las instalaciones «**según las tensiones nominales
que se les asignen**», y da la tensión en alterna como «**(Valor eficaz)**» y en continua como
«**(Valor medio aritmético)**»:

| Clase | Corriente alterna (valor eficaz) | Corriente continua (valor medio aritmético) |
|---|---|---|
| **Muy baja tensión** | **Un ≤ 50V** | **Un ≤ 75V** |
| **Tensión usual** | **50 < Un ≤ 500V** | **75 < Un ≤ 750V** |
| **Tensión especial** | **500 < Un ≤ 1000V** | **750 < Un ≤ 1500V** |

La red de 230/400 V de un edificio es, por tanto, de tensión usual. Que la tensión en alterna se
exprese en valor eficaz importa para el epígrafe 3.2: cuando el reglamento dice 230 V, son 230 V
eficaces.

### 1.2 Tensiones nominales y frecuencia de la red

El artículo 4, apartado 2, del REBT:

> «**Las tensiones nominales usualmente utilizadas en las distribuciones de corriente alterna serán:
> a) 230 V entre fases para las redes trifásicas de tres conductores.
> b) 230 V entre fase y neutro, y 400 V entre fases, para las redes trifásicas de 4 conductores,**»
>
> — Real Decreto 842/2002, Reglamento, artículo 4.2, redacción única (vigente desde el 18/09/2003).

El artículo 4, apartado 4:

> «**La frecuencia empleada en la red será de 50 Hz.**»
>
> — Real Decreto 842/2002, Reglamento, artículo 4.4, redacción única.

El apartado 5 admite excepciones: «**Podrán utilizarse otras tensiones y frecuencias, previa
autorización motivada del órgano competente de la Administración Pública**», si se justifica la
necesidad, no hay perturbaciones significativas en otras instalaciones y no se menoscaba la
seguridad.

La relación entre 230 y 400 es la raíz de tres (230 · √3 ≈ 398, que se redondea a 400). En una red
trifásica de cuatro conductores, la tensión entre dos fases es raíz de tres veces la tensión entre
una fase y el neutro, y eso es geometría de vectores desfasados 120 grados, no una afirmación de la
norma. El reglamento da las dos cifras y no las relaciona.

### 1.3 Las instalaciones interiores o receptoras

El objeto de casi todo este tema son las instalaciones interiores, que el artículo 16.1 del REBT
define así:

> «**Las instalaciones interiores o receptoras son las que, alimentadas por una red de distribución
> o por una fuente de energía propia, tienen como finalidad principal la utilización de la energía
> eléctrica. Dentro de este concepto hay que incluir cualquier instalación receptora aunque toda
> ella o alguna de sus partes esté situada a la intemperie.**»
>
> — Real Decreto 842/2002, Reglamento, artículo 16.1, redacción única.

El apartado 2 del mismo artículo es el que impone el equilibrio de cargas y se estudia en el
epígrafe 8.1. La instrucción que desarrolla las prescripciones generales de estas instalaciones es
la ITC-BT-19, que da los límites de caída de tensión (epígrafe 7.2) y el equilibrado de cargas
(epígrafe 8.1).

## 2. Magnitudes eléctricas

### 2.1 Tensión, intensidad y resistencia

Las tres magnitudes fundamentales, con su definición, su símbolo y su unidad:

| Magnitud | Qué es | Símbolo | Unidad |
|---|---|---|---|
| Tensión, diferencia de potencial o voltaje | El trabajo necesario para mover una carga entre dos puntos: la causa que empuja | U o V | Voltio, V |
| Intensidad de corriente | La cantidad de carga que atraviesa una sección por unidad de tiempo: el efecto | I | Amperio, A |
| Resistencia | La oposición que un conductor ofrece al paso de la corriente | R | Ohmio, Ω |

Y las magnitudes que se derivan de ellas y que el resto del tema usa:

| Magnitud | Qué es | Unidad |
|---|---|---|
| Carga eléctrica, Q | La cantidad de electricidad; una corriente de 1 A transporta 1 culombio por segundo | Culombio, C |
| Conductancia, G | La inversa de la resistencia: G = 1 / R | Siemens, S |
| Resistividad, ρ, y conductividad, γ = 1 / ρ | La resistencia propia del material, independiente de la forma del conductor | Ω·mm²/m, y su inversa, m/(Ω·mm²) |
| Potencia, P | El trabajo por unidad de tiempo (epígrafe 4) | Vatio, W |
| Energía, E | La potencia por el tiempo (epígrafe 5) | Julio, J, o kilovatio hora, kWh |

### 2.2 La ley de Ohm

La ley de Ohm relaciona las tres, y hay que saber decirla en las tres formas, porque un examen
puede pedir cualquiera de ellas:

| Forma | Qué despeja | Cuándo se usa |
|---|---|---|
| U = R · I | La tensión | Caída de tensión en un tramo de conductor |
| I = U / R | La intensidad | Corriente que va a circular por un receptor |
| R = U / I | La resistencia | Resistencia deducida de una medida |

Y la lectura de oficio que hay que tener hecha, porque es la que decide un cálculo de instalación:
en una instalación real la tensión es un dato fijo —la de la red— y la resistencia es lo que se
elige. Lo que resulta de las dos es la corriente, y la corriente es lo que dimensiona el cable
y el interruptor. Por eso un cálculo de instalación no empieza en la ley de Ohm: acaba en ella.

Las resistencias se asocian de dos maneras, y las dos aparecen en un cuadro real:

| Asociación | Resistencia equivalente | Qué se reparte |
|---|---|---|
| En serie | R = R1 + R2 + … | La tensión; la corriente es la misma en todas |
| En paralelo | 1/R = 1/R1 + 1/R2 + … | La corriente; la tensión es la misma en todas |

Los receptores de una instalación se conectan en paralelo, todos a la misma tensión; el conductor
de la línea queda en serie con ellos, y por eso parte de la tensión se queda en él (epígrafe 7).

Las dos reglas de esa tabla se deducen de las leyes de Kirchhoff, junto con la de Ohm; las de
Kirchhoff resuelven cualquier circuito:

| Ley | Qué dice | Ejemplo |
|---|---|---|
| Primera, de los nudos o de las corrientes | En un nudo, la suma de las corrientes que entran es igual a la suma de las que salen | Entran 10 A y 4 A; si por una rama salen 6 A, por la otra salen 10 + 4 − 6 = 8 A |
| Segunda, de las mallas o de las tensiones | En un circuito cerrado, la suma de las fuerzas electromotrices es igual a la suma de las caídas de tensión | Una fuente de 230 V con una línea que cae 6 V deja 224 V al receptor |

La primera es la que se aplica en un cuadro: la corriente de la cabecera es la suma de las de las
salidas que funcionan a la vez. En alterna las dos leyes valen con los valores instantáneos o
sumando vectorialmente, no sumando valores eficaces (epígrafe 8.2).

### 2.3 La resistencia de un conductor

La resistencia de un conductor, que es la fórmula que este oficio usa todos los días:

R = ρ · L / S

| Símbolo | Qué es |
|---|---|
| ρ | La resistividad del material, propia de cada metal y dependiente de la temperatura |
| L | La longitud del conductor |
| S | La sección del conductor |

Las tres consecuencias que se leen directamente en esa fórmula, y que son el fundamento del cálculo
de caída de tensión del epígrafe 7:

1. La resistencia crece con la longitud. Una línea larga cae más.
2. La resistencia baja con la sección. Un cable más grueso cae menos.
3. La resistencia depende del material. El cobre conduce mejor que el aluminio, y por eso a
   igual corriente el aluminio pide más sección.

Y la que no se lee y hay que añadir: la resistividad sube con la temperatura en los metales.
Un conductor cargado se calienta, y al calentarse conduce peor y se calienta más. Ésa es la
razón física de que las intensidades admisibles de la instrucción técnica dependan de la forma de
instalación y de la temperatura ambiente.

El REBT admite los dos metales en las instalaciones interiores: la ITC-BT-19, apartado 2.2.1, dice
que «**Los conductores y cables que se empleen en las instalaciones serán de cobre o aluminio y
serán siempre aislados, excepto cuando vayan montados sobre aisladores, tal como se indica en la
ITC-BT 20.**»

### 2.4 El efecto Joule

Toda corriente que atraviesa una resistencia la calienta. La potencia que se convierte en calor es

P = R · I²

y sale de combinar P = U · I con la ley de Ohm. Dos consecuencias que recorren el tema entero:

- La pérdida en un cable crece con el cuadrado de la corriente: el doble de corriente, cuatro veces
  más calor. Por eso todo lo que reduce la corriente para la misma potencia útil —una tensión más
  alta, un factor de potencia mejor (epígrafe 6), un reparto equilibrado entre fases (epígrafe 8)—
  reduce las pérdidas.
- El calentamiento es lo que limita la corriente que admite un cable. Ese límite, la intensidad
  máxima admisible, es el segundo criterio de cálculo de una sección y se estudia en el tema 4.

## 3. Corriente alterna

### 3.1 Corriente continua y corriente alterna

La diferencia de fondo, dicha en una línea: en continua la magnitud no cambia de valor ni de
sentido; en alterna cambia las dos cosas periódicamente.

| | Corriente continua | Corriente alterna |
|---|---|---|
| Sentido | Siempre el mismo | Se invierte cada semiperiodo |
| Valor | Constante | Varía siguiendo una senoide |
| De dónde sale | Pilas, baterías, rectificadores, paneles fotovoltaicos | Alternadores |
| Transformable | No directamente: hace falta convertirla | Sí, con un transformador |
| Dónde manda | Electrónica, baterías, tracción, sistemas de alimentación ininterrumpida | Generación, transporte y distribución |

La razón técnica de que la red sea alterna: la alterna se puede elevar y reducir de tensión con un
transformador, sin partes móviles. Y elevar la tensión permite transportar la misma potencia con
menos corriente, y las pérdidas en un conductor son proporcionales al cuadrado de la corriente
(epígrafe 2.4). El transformador funciona por inducción electromagnética, que necesita un flujo
magnético variable; una corriente continua no lo da, y por eso la continua no se puede transformar
directamente.

En un centro de radio y televisión conviven las dos: la red llega en alterna y buena parte de los
equipos —fuentes de alimentación, SAI, baterías, electrónica de vídeo y de informática— trabajan
por dentro en continua, con un rectificador o una fuente conmutada en la entrada. Eso explica las
corrientes deformadas del epígrafe 8.3.

### 3.2 Las magnitudes de una señal alterna

Una tensión alterna senoidal se escribe u(t) = Umáx · sen (ω · t), con ω = 2 · π · f, la pulsación
en radianes por segundo. Sus magnitudes, que hay que saber nombrar:

| Magnitud | Qué es |
|---|---|
| Valor de pico o máximo | El valor más alto que alcanza en cada semiperiodo |
| Valor de pico a pico | El doble del anterior, del máximo positivo al negativo |
| Valor medio | En una senoide completa es cero; en un semiperiodo, no |
| Valor eficaz | El de una continua que produciría el mismo efecto calorífico |
| Periodo, T | Lo que tarda en repetirse un ciclo |
| Frecuencia, f | Ciclos por segundo, en hercios; f = 1 / T |

El valor eficaz es el que se maneja siempre y hay que decirlo expresamente: cuando se dice que la
red es de 230 voltios, son 230 voltios eficaces. En una senoide, el valor eficaz es el máximo
dividido por raíz de dos, de modo que una red de 230 voltios eficaces tiene picos de unos 325.
Esa cifra importa porque los aislamientos y las tensiones soportadas se dimensionan por el pico, no
por el eficaz.

Los números de la red española, que salen de las dos cifras del artículo 4 (epígrafe 1.2):

| Dato | Cálculo | Resultado |
|---|---|---|
| Valor de pico | 230 · √2 | ≈ 325 V |
| Valor de pico a pico | 2 · 325 | ≈ 650 V |
| Periodo | 1 / 50 Hz | 0,02 s = 20 ms |
| Pulsación | 2 · π · 50 | ≈ 314 rad/s |
| Inversiones de sentido | Dos por ciclo | 100 por segundo |

La relación eficaz = pico / √2 sólo vale para una senoide pura. Con una onda deformada, que es lo
que absorben las fuentes conmutadas, la relación cambia, y un instrumento que la suponga se
equivoca; la medida de verdadero valor eficaz es materia del tema 14.

### 3.3 Resistencias, bobinas y condensadores en alterna

En continua sólo cuenta la resistencia. En alterna, las bobinas y los condensadores también se
oponen al paso de la corriente, y además la desfasan respecto de la tensión. De ese desfase nacen
la potencia reactiva y el factor de potencia de los epígrafes 4 y 6.

| Elemento | Oposición al paso de la corriente | Desfase de la corriente respecto de la tensión |
|---|---|---|
| Resistencia pura | R, igual que en continua | Ninguno: van en fase |
| Bobina pura (inductancia L, en henrios) | Reactancia inductiva XL = 2 · π · f · L | Retrasada 90° |
| Condensador puro (capacidad C, en faradios) | Reactancia capacitiva XC = 1 / (2 · π · f · C) | Adelantada 90° |

Las dos reactancias se miden en ohmios y varían con la frecuencia en sentido contrario: la de la
bobina crece con la frecuencia y la del condensador baja. A 50 Hz, una bobina de 0,1 H tiene XL =
2 · π · 50 · 0,1 ≈ 31,4 Ω, y un condensador de 100 µF tiene XC = 1 / (2 · π · 50 · 0,0001) ≈ 31,8 Ω.

Un receptor real combina resistencia y reactancia, y su oposición total es la impedancia:

Z = √(R² + X²), con X = XL − XC

La ley de Ohm vale en alterna con la impedancia: I = U / Z. El ángulo φ que forman tensión y
corriente cumple cos φ = R / Z. Un receptor es:

- Inductivo si domina la bobina: la corriente va retrasada. Es el caso de motores,
  transformadores, reactancias de alumbrado y, en general, de todo lo que tiene devanados.
- Capacitivo si domina el condensador: la corriente va adelantada. Es el caso de una batería
  de condensadores sobredimensionada o de cables muy largos en vacío.
- Resistivo si no hay reactancia neta: cos φ = 1. Es el caso de las resistencias de
  calefacción y de las lámparas incandescentes.

### 3.4 El sistema trifásico

Tres tensiones alternas de la misma amplitud y frecuencia, desfasadas 120 grados entre sí. Ésa es
la definición y de ella sale todo lo demás.

Por qué se usa, en tres razones que hay que saber enunciar:

1. Transporta más potencia con menos cobre que tres circuitos monofásicos independientes.
2. La potencia instantánea es constante, no pulsante como en monofásica, y eso hace posible un
   par de motor uniforme.
3. Permite crear un campo magnético giratorio, que es lo que hace girar un motor asíncrono sin
   ningún artificio de arranque.

Las dos conexiones, que son el vocabulario básico del oficio:

| Conexión | Cómo se une | Relación de tensiones | Relación de corrientes |
|---|---|---|---|
| Estrella | Un extremo de cada devanado a un punto común, el neutro | La de línea es raíz de tres veces la de fase | La de línea es igual a la de fase |
| Triángulo | Cada devanado entre dos fases, en serie cerrada | La de línea es igual a la de fase | La de línea es raíz de tres veces la de fase |

La regla que las resume y que evita confundirlas: la raíz de tres está siempre, y cambia de sitio.
En estrella está en la tensión; en triángulo, en la corriente.

Y la consecuencia práctica más importante: un mismo receptor conectado en estrella recibe en cada
devanado una tensión raíz de tres veces menor que en triángulo, y por tanto absorbe una potencia
tres veces menor. En eso se basa el arranque estrella-triángulo de los motores.

El neutro y por qué existe: es el conductor unido al punto común de la estrella, y permite
disponer de dos tensiones en la misma red —230 entre fase y neutro para receptores monofásicos y 400
entre fases para trifásicos—. Y su otra función, que es la que importa a la seguridad: por él
circula el desequilibrio, y por eso una instalación muy desequilibrada carga el neutro. Es la
materia del epígrafe 8.

El REBT da a cada conductor su color de aislamiento, y ése es el modo de reconocer las fases en un
cuadro. La ITC-BT-19, apartado 2.2.4:

> «**Cuando exista conductor neutro en la instalación o se prevea para un conductor de fase su pase
> posterior a conductor neutro, se identificarán éstos por el color azul claro. Al conductor de
> protección se le identificará por el color verde-amarillo. Todos los conductores de fase, o en su
> caso, aquellos para los que no se prevea su pase posterior a neutro, se identificarán por los
> colores marrón o negro.
> Cuando se considere necesario identificar tres fases diferentes, se utilizará también el color
> gris.**»
>
> — Real Decreto 842/2002, ITC-BT-19, apartado 2.2.4, redacción única.

## 4. Potencia

### 4.1 Las tres potencias

La potencia en corriente continua es un producto: P = U · I, en vatios.

En corriente alterna hay tres potencias, y confundirlas lleva a dimensionar mal cables, grupos y SAI:

| Potencia | Qué es | Unidad | Fórmula en monofásica |
|---|---|---|---|
| Activa, P | La que se transforma en trabajo o calor: la que se consume de verdad | Vatio, W | P = U · I · cos φ |
| Reactiva, Q | La que va y vuelve para magnetizar bobinas y cargar condensadores | Voltamperio reactivo, var | Q = U · I · sen φ |
| Aparente, S | La que la instalación tiene que poder transportar | Voltamperio, VA | S = U · I |

En trifásica, las mismas con el factor raíz de tres, siendo U la tensión entre fases e I la
corriente de línea:

| Potencia | Fórmula en trifásica |
|---|---|
| Activa | P = √3 · U · I · cos φ |
| Reactiva | Q = √3 · U · I · sen φ |
| Aparente | S = √3 · U · I |

Las tres forman un triángulo rectángulo, el triángulo de potencias: la activa es el cateto
horizontal, la reactiva el vertical y la aparente la hipotenusa. De ahí salen las relaciones que se
usan para despejar:

S² = P² + Q²  ·  cos φ = P / S  ·  tg φ = Q / P

La lectura de oficio: la activa es la que hace el trabajo y la que mide el contador de energía
activa; la aparente es la que fija la corriente, y por eso los transformadores, los grupos
electrógenos y los SAI se dan en kilovoltamperios, no en kilovatios. Un equipo de 10 kVA no
alimenta 10 kW salvo con cos φ = 1.

### 4.2 Cálculo de potencias e intensidades

Despejando la intensidad, que es lo que dimensiona cable y protección:

| Sistema | Intensidad de línea |
|---|---|
| Monofásico | I = P / (U · cos φ) |
| Trifásico | I = P / (√3 · U · cos φ) |

Ejemplo monofásico. Un receptor de 4.600 W a 230 V con cos φ = 0,8:

- I = 4.600 / (230 · 0,8) = 25 A.
- S = 230 · 25 = 5.750 VA.
- Q = √(5.750² − 4.600²) = 3.450 var (o, con sen φ = 0,6, Q = 5.750 · 0,6).

Ejemplo trifásico. Una carga de 20 kW a 400 V con cos φ = 0,85:

- I = 20.000 / (√3 · 400 · 0,85) ≈ 34 A.
- S = P / cos φ = 20 / 0,85 ≈ 23,5 kVA.
- sen φ = √(1 − 0,85²) ≈ 0,527, y Q = S · sen φ ≈ 12,4 kvar.

Comparación. La misma potencia activa en monofásica a 230 V pediría 20.000 / (230 · 0,85) ≈
102 A por un solo conductor de fase, tres veces la corriente de línea del trifásico. Es la razón
económica de alimentar en trifásica las cargas grandes.

Varios receptores en un mismo cuadro. Las potencias activas se suman entre sí, y las reactivas
también, con su signo (positivo la inductiva, negativo la capacitiva); la aparente no se suma: se
calcula al final con el triángulo de potencias. Es el teorema de Boucherot. Ejemplo, dos cargas de
10 kW con cos φ = 0,8 y de 5 kW con cos φ = 1:

- P = 10 + 5 = 15 kW.
- Q = 10 · tg φ = 10 · 0,75 = 7,5 kvar en la primera, y 0 en la segunda: 7,5 kvar.
- S = √(15² + 7,5²) ≈ 16,8 kVA, no 12,5 + 5 = 17,5 kVA.
- Factor de potencia del conjunto: 15 / 16,8 ≈ 0,89, no la media de 0,8 y 1.

## 5. Energía

La energía es la potencia por el tiempo:

E = P · t

En el sistema internacional se mide en julios (un julio es un vatio durante un segundo, W·s), pero en electricidad se usa el
kilovatio hora: la energía que consume una potencia de 1 kW durante una hora. Un kilovatio hora
son 1.000 W · 3.600 s = 3.600.000 J, es decir, 3,6 megajulios.

La potencia es lo que se contrata; la energía es lo que se gasta. Son dos magnitudes distintas y
un examen las separa:

| | Potencia | Energía |
|---|---|---|
| Qué expresa | El ritmo al que se consume | Lo consumido en un tiempo |
| Unidad práctica | kW | kWh |
| Qué la limita o la registra | El interruptor y la protección del suministro | El contador |

Del mismo modo que hay tres potencias, hay energía activa, en kWh, y energía reactiva, en
kilovoltamperios reactivos hora (kvarh). Un contador de energía reactiva registra la que las
cargas inductivas intercambian con la red; su relación con la activa es la que da el factor de
potencia medio de un periodo (epígrafe 6).

Ejemplos.

- Un plató con 20 kW de iluminación encendido 10 horas consume 20 · 10 = 200 kWh.
- Un SAI que alimenta 3 kW de equipos de una sala técnica durante las 24 horas del día consume, sólo
  en la carga, 3 · 24 = 72 kWh al día, más sus propias pérdidas.

Esas pérdidas se expresan con el rendimiento, el cociente entre la potencia útil que entrega una
máquina y la que absorbe:

η = P útil / P absorbida

Siempre menor que uno; la diferencia es calor. Un equipo que entrega 3 kW con un rendimiento de
0,9 absorbe 3 / 0,9 ≈ 3,33 kW, y los 0,33 kW de diferencia hay que evacuarlos con la climatización
de la sala.

## 6. Factor de potencia

### 6.1 Qué es y qué consecuencias tiene

El factor de potencia es el cociente entre la potencia activa y la aparente. Con tensiones y
corrientes senoidales coincide con el coseno del ángulo de desfase, cos φ, y va de 0 a 1: vale 1 en
una carga resistiva y baja cuanto más reactiva es la carga. Se dice inductivo (o en retraso) cuando
la corriente va retrasada y capacitivo (o en adelanto) cuando va adelantada.

La lectura de oficio que hay que saber dar es ésta: un cos φ bajo significa que por el cable circula
más corriente de la que hace falta para el trabajo que se hace.

| Consecuencia de un cos φ bajo | Por qué |
|---|---|
| Más corriente para la misma potencia útil | Porque I = P / (U · cos φ) |
| Más caída de tensión y más pérdidas | Porque las dos dependen de la corriente |
| Más sección de cable y más aparamenta | Porque se dimensionan por corriente |
| Menos potencia activa disponible de un transformador, un grupo o un SAI | Porque su límite es la potencia aparente |

Cuando la corriente no es senoidal —fuentes conmutadas, variadores, alumbrado electrónico— el
factor de potencia (P / S) y el cos φ dejan de coincidir, porque la corriente deformada aumenta la
potencia aparente sin aportar activa. Los condensadores corrigen el desfase, no la deformación. La
medida de los dos con un analizador de redes es materia del tema 14.

### 6.2 La compensación con condensadores

Lo que corrige un cos φ bajo es la batería de condensadores, que aporta la reactiva que las cargas
inductivas piden, de modo que no tenga que traerla la red. La reactiva capacitiva del condensador
y la inductiva de la carga tienen signo contrario y se restan.

La potencia de la batería que lleva una carga P desde un cos φ1 hasta un cos φ2 se calcula con el
triángulo de potencias:

Qc = P · (tg φ1 − tg φ2)

Ejemplo. La carga trifásica del epígrafe 4.2 (20 kW, cos φ = 0,85) se quiere llevar a 0,95:

- tg φ1 = 0,527 / 0,85 ≈ 0,620.
- Para cos φ2 = 0,95, sen φ2 = √(1 − 0,95²) ≈ 0,312, y tg φ2 ≈ 0,329.
- Qc = 20 · (0,620 − 0,329) ≈ 5,8 kvar.
- La corriente baja de unos 34 A a 20.000 / (√3 · 400 · 0,95) ≈ 30,4 A, con la misma potencia
  útil.

La batería se da en kvar; su capacidad sale de la potencia reactiva de un condensador sometido a
una tensión U, Q = U² · ω · C, con ω = 2 · π · f (epígrafe 3.2). Una batería trifásica son tres
condensadores, y cada uno lleva un tercio de la reactiva; su tensión depende de cómo se conecten:

| Conexión | Tensión en cada condensador | Capacidad por fase |
|---|---|---|
| Triángulo | La de entre fases, 400 V | C = Qc / (3 · 400² · ω) |
| Estrella | La de fase, 400 / √3 ≈ 230 V | C = Qc / (3 · 230² · ω), el triple que en triángulo |

Con la batería de 5,8 kvar del ejemplo, en triángulo, C = 5.800 / (3 · 160.000 · 314) ≈ 38 µF por
fase; en estrella, unos 115 µF. Por eso las baterías trifásicas se conectan en triángulo: la misma
reactiva con un tercio de la capacidad.

La compensación puede hacerse junto a cada receptor (individual), por grupos o para toda la
instalación en la cabecera (global, con una batería automática por escalones). Cuanto más cerca de
la carga, más tramo de línea se descarga de reactiva; cuanto más centralizada, menos condensadores
hacen falta, porque no todas las cargas funcionan a la vez. El REBT admite las dos formas
extremas y fija sus condiciones (epígrafe 6.3).

### 6.3 Lo que fija el REBT

La regla general está en la ITC-BT-43, apartado 2.7, «**Compensación del factor de potencia**»:

> «**Las instalaciones que suministren energía a receptores de los que resulte un factor de
> potencia inferior a 1, podrán ser compensadas, pero sin que en ningún momento la energía absorbida
> por la red pueda ser capacitiva.
> La compensación del factor de potencia podrá hacerse de una de las dos formas siguientes:
> – Por cada receptor o grupo de receptores que funcionen simultáneamente y se conecten por medio de
> un sólo interruptor. En este caso el interruptor debe cortar la alimentación simultáneamente al
> receptor o grupo de receptores y al condensador.
> – Para la totalidad de la instalación. En este caso, la instalación de compensación ha de estar
> dispuesta para que, de forma automática, asegure que la variación del factor de potencia no sea
> mayor de un ± 10 % del valor medio obtenido durante un prolongado período de funcionamiento.
> Cuando se instalen condensadores y la conexión de éstos con los receptores pueda ser cortada por
> medio de interruptores, los condensadores irán provistos de resistencias o reactancias de descarga
> a tierra.
> Los condensadores utilizados para la mejora del factor de potencia en los motores asíncronos, se
> instalarán de forma que, al cortar la alimentación de energía eléctrica al motor, queden
> simultáneamente desconectados los indicados condensadores.
> Las características de los condensadores y su instalación deberán ser conformes a lo establecido
> en la norma UNE-EN 60831-1 y UNE-EN 60831-2.**»
>
> — Real Decreto 842/2002, ITC-BT-43, apartado 2.7, redacción única.

Lo que hay que leer en esa cita:

1. Con carácter general la compensación es potestativa: «**podrán ser compensadas**».
2. El límite es la sobrecompensación: la energía absorbida «**en ningún momento**» puede ser
   capacitiva. Una batería fija dimensionada para la plena carga deja la instalación en adelanto
   cuando la carga baja; por eso la compensación global ha de ser automática.
3. Las dos formas admitidas son la individual o por grupo, con un solo interruptor para receptor y
   condensador, y la global, automática y con la variación limitada a ± 10 % del valor medio.
4. Los condensadores que puedan quedar separados de su carga llevan resistencias o reactancias de
   descarga a tierra, porque un condensador desconectado conserva su carga y su tensión.

Donde sí es obligatoria es en el alumbrado con lámparas de descarga y en el alumbrado exterior. La
ITC-BT-44, apartado 3.1, para los receptores con lámparas de descarga:

> «**En el caso de receptores con lámparas de descarga será obligatoria la compensación del factor
> de potencia hasta un valor mínimo de 0,9, y no se admitirá compensación en conjunto de un grupo de
> receptores en una instalación de régimen de carga variable, salvo que dispongan de un sistema de
> compensación automático con variación de su capacidad siguiendo el régimen de carga.**»
>
> — Real Decreto 842/2002, ITC-BT-44, apartado 3.1, redacción única.

Y en su apartado 3.2, sobre los condensadores de esos equipos:

> «**Todos los condensadores que formen parte del equipo auxiliar eléctrico de las lámparas de
> descarga para corregir el factor de potencia de los balastos, deberán llevar conectada una
> resistencia que asegure que la tensión en bornes del condensador no sea mayor de 50 V
> transcurridos 60 s desde la desconexión del receptor.**»
>
> — Real Decreto 842/2002, ITC-BT-44, apartado 3.2, redacción única.

Para el alumbrado exterior, la ITC-BT-09 lo exige punto a punto. En su apartado 3: «**el factor
de potencia de cada punto de luz, deberá corregirse hasta un valor mayor o igual a 0,90**»; y en el
apartado 8, de los equipos eléctricos de los puntos de luz: «**Cada punto de luz deberá tener
compensado individualmente el factor de potencia para que sea igual o superior a 0,90**».

La instalación de los propios condensadores, sea cual sea su uso, la regula la ITC-BT-48, apartado
2.3, «**Condensadores**»:

> «**Los condensadores que no lleven alguna indicación de temperatura máxima admisible no se podrán
> utilizar en lugares donde la temperatura ambiente sea 50 ºC o mayor.
> Si la carga residual de los condensadores pudiera poner en peligro a las personas, llevarán un
> dispositivo automático de descarga o se colocará una inscripción que advierta este peligro. Los
> condensadores con dieléctrico líquido combustible cumplirán los mismos requisitos que los
> reostatos y reactancias.
> Para la utilización de condensadores por encima de los 2.000 m. de altitud sobre el nivel del
> mar, deberán tomarse precauciones de acuerdo con el fabricante, según especifica la Norma UNE-EN
> 60.831-1.
> Los condensadores deberán estar adecuadamente protegidos, cuando se vayan a utilizar con
> sobreintensidades superiores a 1,3 veces la intensidad correspondiente a la tensión asignada a
> frecuencia de red, excluidos los transitorios.
> Los aparatos de mando y protección de los condensadores deberán soportar en régimen permanente,
> de 1,5 a 1,8 veces la intensidad nominal asignada del condensador, a fin de tener en cuenta los
> armónicos y las tolerancias sobre las capacidades.**»
>
> — Real Decreto 842/2002, ITC-BT-48, apartado 2.3, redacción única.

Ese 1,5 a 1,8 es la razón de que el interruptor o los fusibles de una batería se elijan muy por
encima de su corriente nominal: con armónicos en la red (epígrafe 8.3), el condensador absorbe más
corriente de la que da su placa.

| Caso | Compensación | Valor | Fuente |
|---|---|---|---|
| Instalaciones en general | Potestativa, nunca capacitiva | Global automática: variación ≤ ± 10 % del valor medio | ITC-BT-43, 2.7 |
| Receptores con lámparas de descarga | Obligatoria | Mínimo 0,9 | ITC-BT-44, 3.1 |
| Alumbrado exterior | Obligatoria, en cada punto de luz | ≥ 0,90 | ITC-BT-09, 3 y 8 |
| Condensadores de balastos de descarga | Resistencia de descarga | ≤ 50 V a los 60 s | ITC-BT-44, 3.2 |
| Condensadores en general | Aparamenta de mando y protección | De 1,5 a 1,8 veces su intensidad nominal | ITC-BT-48, 2.3 |

## 7. Caída de tensión

### 7.1 Qué es y por qué importa

La caída de tensión es la parte de la tensión de origen que se pierde en el propio conductor: la
línea tiene resistencia (epígrafe 2.3), está en serie con el receptor y, por la ley de Ohm, se queda
con una parte de la tensión. Hay que decir por qué importa, porque no es evidente:

| Consecuencia de una caída excesiva | Por qué |
|---|---|
| El receptor recibe menos tensión de la nominal | Y no da su potencia |
| Un motor pierde par | El par depende del cuadrado de la tensión |
| Una lámpara de descarga puede no arrancar | Necesita una tensión mínima |
| Se pierde energía en forma de calor en el cable | Que es dinero que se paga y no se usa |

Una sección se comprueba por dos criterios y se elige la mayor de las dos que resulten: el de
calentamiento, que depende de la corriente y de cómo está instalado el cable y es materia del tema
4, y el de caída de tensión, que depende de la corriente y de la longitud. La longitud no influye
en el calentamiento y sí en la caída: en líneas cortas suele mandar el calentamiento y en líneas
largas, la caída.

### 7.2 Los límites del REBT

Los límites de las instalaciones interiores están en la ITC-BT-19, apartado 2.2.2, «**Sección de
los conductores. Caídas de tensión**»:

> «**La sección de los conductores a utilizar se determinará de forma que la caída de tensión entre
> el origen de la instalación interior y cualquier punto de utilización sea, salvo lo prescrito en
> las Instrucciones particulares, menor del 3 % de la tensión nominal para cualquier circuito
> interior de viviendas, y para otras instalaciones interiores o receptoras, del 3 % para alumbrado
> y del 5 % para los demás usos. Esta caída de tensión se calculará considerando alimentados todos
> los aparatos de utilización susceptibles de funcionar simultáneamente. El valor de la caída de
> tensión podrá compensarse entre la de la instalación interior y la de las derivaciones
> individuales, de forma que la caída de tensión total sea inferior a la suma de los valores límites
> especificados para ambas, según el tipo de esquema utilizado.
> Para instalaciones industriales que se alimenten directamente en alta tensión mediante un
> transformador de distribución propio, se considerará que la instalación interior de baja tensión
> tiene su origen en la salida del transformador. En este caso las caídas de tensión máximas
> admisibles serán del 4,5 % para alumbrado y del 6,5 % para los demás usos.**»
>
> — Real Decreto 842/2002, ITC-BT-19, apartado 2.2.2, redacción única.

Lo que hay que leer en esa cita, y es lo que un examen busca:

1. Tres porcentajes generales, que no hay que confundir: 3 % en cualquier circuito interior de
   viviendas; en las demás instalaciones interiores o receptoras —un edificio técnico o de
   oficinas—, 3 % para alumbrado y 5 % para los demás usos.
2. Se miden desde el origen de la instalación interior hasta cualquier punto de utilización, y en
   tanto por ciento de la tensión nominal: el 3 % de 230 V son 6,9 V; el 5 % de 400 V, 20 V.
3. Se calculan con todo lo que pueda funcionar a la vez («**considerando alimentados todos los
   aparatos de utilización susceptibles de funcionar simultáneamente**»). Ésa es la palabra que
   decide cuántos amperios se meten en la fórmula. Y el tercer párrafo del mismo apartado dice
   cómo se cuentan: «**El número de aparatos susceptibles de funcionar simultáneamente, se
   determinará en cada caso particular, de acuerdo con las indicaciones incluidas en las
   instrucciones del presente reglamento y en su defecto con las indicaciones facilitadas por el
   usuario considerando una utilización racional de los aparatos.**»
4. La caída puede compensarse con la de la derivación individual: si la derivación cae poco, la
   instalación interior puede caer algo más, con tal de que la suma no supere la suma de los dos
   límites.
5. Con transformador propio los porcentajes suben a 4,5 y 6,5, porque el origen se mueve a la
   salida del transformador y el cómputo incluye un tramo que en el caso general estaba fuera. Qué edificios de la RTVA se
   alimentan en alta tensión con transformador propio no consta en ningún documento publicado.

Los límites de los tramos anteriores a la instalación interior están en sus instrucciones:

| Tramo | Caída máxima | Fuente |
|---|---|---|
| Línea general de alimentación, contadores totalmente centralizados | «**0,5 por 100**» | ITC-BT-14 |
| Línea general de alimentación, centralizaciones parciales de contadores | «**1 por 100**» | ITC-BT-14 |
| Derivación individual, contadores concentrados en más de un lugar | «**0,5%**» | ITC-BT-15 |
| Derivación individual, contadores totalmente concentrados | «**1%**» | ITC-BT-15 |
| Derivación individual de un único usuario sin línea general de alimentación | «**1,5%**» | ITC-BT-15 |
| Alumbrado exterior, entre el origen y cualquier punto | «**menor o igual que 3%**» | ITC-BT-09, apartado 3 |

Si un edificio técnico se alimenta como «**único usuario en que no existe línea general de
alimentación**», su derivación individual admite 1,5 %, y su instalación interior, 3 % en alumbrado
y 5 % en los demás usos, con la compensación entre ambas que permite la ITC-BT-19.

### 7.3 Las fórmulas

Las dos fórmulas del oficio, que salen de la ley de Ohm y de la geometría del sistema trifásico:

| Sistema | Caída de tensión |
|---|---|
| Monofásico | e = 2 · L · I · cos φ / (γ · S) |
| Trifásico | e = √3 · L · I · cos φ / (γ · S) |

| Símbolo | Qué es |
|---|---|
| e | La caída de tensión, en voltios |
| L | La longitud de la línea, en metros |
| I | La corriente, en amperios |
| γ | La conductividad del material, inversa de la resistividad |
| S | La sección, en milímetros cuadrados |

Y el detalle que hay que saber explicar, porque es la única diferencia entre las dos fórmulas:
el 2 del monofásico es el camino de ida y vuelta —la corriente va por la fase y vuelve por el
neutro, y las dos caen—; la raíz de tres del trifásico sale de la composición vectorial de las tres
fases, y da la caída en la tensión entre fases. Quien entienda eso no confunde las dos.

Como I · cos φ = P / U en monofásica y √3 · I · cos φ = P / U en trifásica, las dos fórmulas se
escriben también en función de la potencia, que es como suele venir el dato:

| Sistema | Caída de tensión con la potencia |
|---|---|
| Monofásico | e = 2 · P · L / (γ · S · U) |
| Trifásico | e = P · L / (γ · S · U) |

con U la tensión de la línea: 230 V entre fase y neutro en monofásica, 400 V entre fases en
trifásica. La caída en tanto por ciento es e % = 100 · e / U.

Despejando la sección, que es como se usan de verdad:

| Sistema | Sección necesaria |
|---|---|
| Monofásico | S = 2 · L · I · cos φ / (γ · e) |
| Trifásico | S = √3 · L · I · cos φ / (γ · e) |

Las cuatro lecturas que se hacen directamente en esas fórmulas, y que son lo que un examen premia:

1. La sección es proporcional a la longitud. El doble de metros pide el doble de sección, si
   todo lo demás se mantiene.
2. La sección es proporcional a la corriente.
3. La sección es inversamente proporcional a la caída admitida. Admitir la mitad de caída
   duplica la sección.
4. A igual potencia, el trifásico pide menos cobre que el monofásico. Ésa es la razón económica
   de repartir cargas en trifásica siempre que se pueda.

Dos avisos de método. Las fórmulas son la versión simplificada: consideran sólo la resistencia de
la línea y desprecian su reactancia, lo que es aceptable en las secciones habituales de un
edificio. Y la conductividad depende de la temperatura: la del cable en servicio no es la de veinte
grados, y calcular con la conductividad a temperatura ambiente da una sección menor de la
necesaria. El valor de γ que se usa en cada cálculo es un dato del material y de su temperatura,
que el REBT no da.

### 7.4 Ejemplos resueltos

En los tres ejemplos la conductividad del cobre se toma como dato supuesto, γ = 48 m/(Ω·mm²); en
un examen la da el enunciado.

Caída de una línea trifásica. La carga del epígrafe 4.2 (20 kW a 400 V, cos φ = 0,85, unos 34
A) se alimenta con una línea de 100 m y 16 mm²:

- e = √3 · 100 · 34 · 0,85 / (48 · 16) ≈ 6,5 V.
- Con la potencia: e = 20.000 · 100 / (48 · 16 · 400) ≈ 6,5 V. Coinciden.
- e % = 100 · 6,5 / 400 ≈ 1,6 %: cumple el 5 % de los demás usos.

Sección de un circuito de alumbrado. Un circuito monofásico de alumbrado de 230 V lleva 10 A
con cos φ = 1 a 40 m del cuadro, y se le asigna toda la caída del 3 %:

- e máxima = 0,03 · 230 = 6,9 V.
- S = 2 · 40 · 10 · 1 / (48 · 6,9) ≈ 2,4 mm².
- Se elige la sección normalizada inmediatamente superior, 2,5 mm², y después se comprueba por
  calentamiento (tema 4).

Longitud máxima. Con ese mismo circuito en 2,5 mm², la longitud máxima para no pasar del 3 % es
L = 48 · 2,5 · 6,9 / (2 · 10 · 1) ≈ 41 m. Más allá hay que subir de sección.

### 7.5 Motores y lámparas de descarga

Dos instrucciones de receptores obligan a calcular la línea por encima de la potencia nominal, y
eso cambia la corriente con que se dimensiona. La de motores lo hace por calentamiento: fija las
secciones mínimas de los conductores de conexión «**con objeto de que no se produzca en ellos un calentamiento excesivo**».

Motores, ITC-BT-47, apartado 3.1, un solo motor:

> «**Los conductores de conexión que alimentan a un solo motor deben estar dimensionados para una
> intensidad del 125 % de la intensidad a plena carga del motor.**»

Y apartado 3.2, varios motores:

> «**Los conductores de conexión que alimentan a varios motores, deben estar dimensionados para una
> intensidad no inferior a la suma del 125 % de la intensidad a plena carga del motor de mayor
> potencia, más la intensidad a plena carga de todos los demás.**»
>
> — Real Decreto 842/2002, ITC-BT-47, apartados 3.1 y 3.2, redacción única.

Ejemplo: tres motores de 20, 10 y 8 A a plena carga en una misma línea: 1,25 · 20 + 10 + 8 = 43 A.

Lámparas de descarga, ITC-BT-44, apartado 3.1:

> «**Los circuitos de alimentación estarán previstos para transportar la carga debida a los propios
> receptores, a sus elementos asociados y a sus corrientes armónicas y de arranque.
> Para receptores con lámparas de descarga, la carga mínima prevista en voltiamperios será de 1,8
> veces la potencia en vatios de las lámparas. En el caso de distribuciones monofásicas, el
> conductor neutro tendrá la misma sección que los de fase.**»
>
> — Real Decreto 842/2002, ITC-BT-44, apartado 3.1, redacción única.

El mismo apartado admite «**un coeficiente diferente para el cálculo de la sección de los
conductores, siempre y cuando el factor de potencia de cada receptor sea mayor o igual a 0,9 y si
se conoce la carga que supone cada uno de los elementos asociados a las lámparas y las corrientes de
arranque**». Ejemplo: un circuito monofásico con 20 lámparas de descarga de 36 W suma 720 W, que
se calculan como 1,8 · 720 = 1.296 VA, es decir, 1.296 / 230 ≈ 5,6 A.

El mismo 1,8 lo fija para el alumbrado exterior la ITC-BT-09, apartado 3, «Dimensionamiento de
las instalaciones»: «**Las líneas de alimentación a puntos de luz con lámparas o tubos de
descarga, estarán previstas para transportar la carga debida a los propios receptores, a sus
elementos asociados, a sus corrientes armónicas, de arranque y desequilibrio de fases. Como
consecuencia, la potencia aparente mínima en VA, se considerará 1,8 veces la potencia en vatios de
las lámparas o tubos de descarga.**» Y, como la ITC-BT-44, admite otro coeficiente: «**Cuando se
conozca la carga que supone cada uno de los elementos asociados a las lámparas o tubos de
descarga, las corrientes armónicas, de arranque y desequilibrio de fases, que tanto éstas como
aquellos puedan producir, se aplicará el coeficiente corrector calculado con estos valores.**»

## 8. Equilibrado de cargas

### 8.1 Lo que exige el REBT

El deber de equilibrar está en el propio Reglamento, artículo 16.2:

> «**En toda instalación interior o receptora que se proyecte y realice se alcanzará el máximo
> equilibrio en las cargas que soportan los distintos conductores que forman parte de la misma, y
> ésta se subdividirá deforma que las perturbaciones originadas por las averías que pudieran
> producirse en algún punto de ella afecten a una mínima parte de la instalación. Esta subdivisión
> deberá permitir también la localización de las averías y facilitar el control del aislamiento de
> la parte de la instalación afectada.**»
>
> — Real Decreto 842/2002, Reglamento, artículo 16.2, redacción única («deforma», así en el BOE).

La ITC-BT-19 lo concreta en su apartado 2.5, «**Equilibrado de cargas**»:

> «**Para que se mantenga el mayor equilibrio posible en la carga de los conductores que forman
> parte de una instalación, se procurará que aquella quede repartida entre sus fases o conductores
> polares.**»
>
> — Real Decreto 842/2002, ITC-BT-19, apartado 2.5, redacción única.

Mirando a la red de distribución, la ITC-BT-43, apartado 2.6, «**Utilización de receptores que
desequilibren las fases o produzcan fuertes oscilaciones de la potencia absorbida**», dice:

> «**No se podrán instalar sin consentimiento expreso de la Empresa que suministra la energí a,
> aparatos receptores que produzcan desequilibrios importantes en las distribuciones polifásicas.**»
>
> — Real Decreto 842/2002, ITC-BT-43, apartado 2.6, redacción única («energí a», así en el BOE).

Y la instrucción de recarga de vehículos eléctricos aplica el reparto entre fases a un caso concreto, el circuito de
recarga de las viviendas unifamiliares. La ITC-BT-52, apartado 3.1, «**Instalación en aparcamientos de
viviendas unifamiliares**»: «**Cuando en un circuito trifásico se conecten estaciones
monofásicas, éstas se repartirán de la forma más equilibrada posible entre las tres fases.**»

Lo que hay que leer en esas citas: el artículo 16.2 manda un resultado («**se alcanzará el máximo
equilibrio**»), y la ITC-BT-19 pone el medio («**se procurará**» repartir la carga entre las fases).
Ninguna de las dos fija un porcentaje de desequilibrio admisible; el REBT no lo da.

### 8.2 La corriente por el neutro

En una red trifásica con neutro, cada circuito monofásico se conecta entre una fase y el neutro, y
su corriente vuelve por el neutro. Las corrientes de las tres fases están desfasadas 120°, y en el
neutro se suman como vectores, no como números:

- Si las tres fases llevan la misma corriente con el mismo cos φ, la suma es cero: el neutro no
  lleva corriente.
- Si están desequilibradas, el neutro lleva la suma vectorial, que ya no es cero.
- Si sólo una fase está cargada, el neutro lleva toda su corriente.

Con cargas resistivas, la corriente del neutro es

IN = √(I1² + I2² + I3² − I1·I2 − I2·I3 − I3·I1)

Ejemplos. Con 20, 20 y 20 A, IN = 0. Con 30, 20 y 10 A, IN = √(900 + 400 + 100 − 600 − 200 −
300) = √300 ≈ 17,3 A. Con 30 A en una sola fase, IN = 30 A.

Lo que cuesta el desequilibrio, y la razón de que el REBT lo combata:

| Efecto | Por qué |
|---|---|
| Fase sobrecargada mientras otras van holgadas | La protección salta en una fase con potencia libre en las otras dos |
| Corriente en el neutro y pérdidas en él | El neutro deja de ir descargado |
| Tensiones distintas en cada fase | Cada fase cae según su corriente |
| Peor aprovechamiento del transformador, el grupo o el SAI | Su límite lo marca la fase más cargada |
| Riesgo grave si se corta el neutro | Sin neutro, los receptores monofásicos de dos fases quedan en serie a 400 V, y la fase menos cargada recibe más tensión de la nominal |

El último es el más peligroso y el que más se olvida: un neutro interrumpido en una instalación
desequilibrada puede dejar receptores a una tensión cercana a la de entre fases, y quemarlos. Por
eso el neutro se trata con el mismo cuidado que una fase.

### 8.3 Armónicos, desequilibrio y sección del neutro

En un sistema trifásico equilibrado con cargas lineales, las tres corrientes se anulan en el neutro
y por él no circula casi nada. Con cargas no lineales —fuentes conmutadas, alumbrado electrónico,
variadores— aparecen armónicos de orden tres y múltiplos, y esos no se anulan: se suman en el
neutro. De ahí que un neutro pueda ir más cargado que las fases, aunque las tres estén
perfectamente equilibradas.

Por eso el REBT no deja reducir el neutro de una instalación interior. La ITC-BT-19, apartado
2.2.2, último párrafo:

> «**En instalaciones interiores, para tener en cuenta las corrientes armónicas debidas cargas no
> lineales y posibles desequilibrios, salvo justificación por cálculo, la sección del conductor
> neutro será como mínimo igual a la de las fases.**»
>
> — Real Decreto 842/2002, ITC-BT-19, apartado 2.2.2, redacción única («debidas cargas», así en el
> BOE).

En la línea general de alimentación, en cambio, la ITC-BT-14 admite un neutro menor, pero obliga a
pensar en lo mismo: «**Para la sección del conductor neutro se tendrán en cuenta el máximo
desequilibrio que puede preverse, las corrientes armónicas y su comportamiento, en función de las
protecciones establecidas ante las sobrecargas y cortocircuitos que pudieran presentarse. El
conductor neutro tendrá una sección de aproximadamente el 50 por 100 de la correspondiente al
conductor de fase, no siendo inferior a los valores especificados en la tabla 1.**»

| Tramo | Sección del neutro | Fuente |
|---|---|---|
| Instalación interior | Como mínimo igual a la de las fases, salvo justificación por cálculo | ITC-BT-19, 2.2.2 |
| Circuito monofásico con lámparas de descarga | La misma que la de fase | ITC-BT-44, 3.1 |
| Línea general de alimentación | Aproximadamente el 50 % de la de fase, con el mínimo de su tabla 1, teniendo en cuenta desequilibrio y armónicos | ITC-BT-14 |

Y el caso de un centro de radio y televisión es exactamente ése: una instalación llena de fuentes
conmutadas —equipos de vídeo, informática, alumbrado de plató electrónico— es una instalación con
armónicos. Dimensionar su neutro como si las cargas fueran resistivas es un error de proyecto poco
visible, porque el sobrecalentamiento del neutro puede no hacer actuar ninguna protección.

### 8.4 Cómo se equilibra un cuadro

El equilibrado es, en la práctica, una tarea del electricista sobre el cuadro, y se hace así:

1. Inventario de los circuitos monofásicos del cuadro, con la potencia prevista de cada uno
   —la simultánea, no la instalada (epígrafe 7.2)—.
2. Reparto entre L1, L2 y L3 de modo que cada fase sume lo más parecido posible a un tercio del
   total. Los receptores trifásicos equilibrados no cuentan: cargan las tres por igual.
3. Identificación: cada circuito se marca con su fase en el esquema y en el cuadro, y las tres
   fases se distinguen por su color (marrón, negro y gris, ITC-BT-19, 2.2.4, epígrafe 3.4).
4. Comprobación con la instalación en servicio: con la pinza amperimétrica, la corriente de cada
   fase y la del neutro en la cabecera, en un momento de carga representativo; o con un analizador
   de redes, que registra la evolución en el tiempo (tema 14).
5. Corrección: si una fase va cargada de forma persistente, se pasan circuitos a la menos
   cargada, con la instalación consignada (tema 15), y se actualiza el esquema.

Ejemplo. Seis circuitos monofásicos de 3,0, 2,5, 2,0, 1,5, 1,5 y 1,0 kW suman 11,5 kW, unos
3,8 kW por fase. Un reparto posible:

| Fase | Circuitos | Total |
|---|---|---|
| L1 | 3,0 + 1,0 | 4,0 kW |
| L2 | 2,5 + 1,5 | 4,0 kW |
| L3 | 2,0 + 1,5 | 3,5 kW |

Con cos φ = 1 y 230 V, las fases llevan unos 17,4, 17,4 y 15,2 A, y el neutro, por la fórmula del
epígrafe 8.2, unos 2,2 A. Si los tres circuitos mayores hubieran ido a la misma fase, ésta llevaría
7,5 kW (unos 32,6 A) y el neutro bastante más.

Dos advertencias de oficio. El equilibrio se juzga con la carga real y su variación a lo largo del
día, no sólo con la instalada: un plató, un estudio de radio y una sala de servidores tienen
horarios distintos. Y un SAI o un grupo monofásico alimentado desde una sola fase de un cuadro
trifásico es un desequilibrio en sí mismo, que conviene compensar con el resto de circuitos.

## Normativa que el tema invoca

- Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para
  baja tensión. Del Reglamento: artículo 2.1 (campo de aplicación), artículo 4 (clasificación de las
  tensiones, tensiones nominales y frecuencia) y artículo 16, apartados 1 y 2 (instalaciones
  interiores o receptoras; equilibrio de cargas). De las instrucciones: ITC-BT-09, apartados 3 y 8
  (alumbrado exterior); ITC-BT-14 (línea general de alimentación: caída de tensión y neutro);
  ITC-BT-15 (derivaciones individuales: caída de tensión); ITC-BT-19, apartados 2.2.1, 2.2.2, 2.2.3,
  2.2.4 y 2.5 (instalaciones interiores); ITC-BT-43, apartados 2.6 y 2.7 (receptores en general:
  desequilibrios y compensación del factor de potencia); ITC-BT-44, apartados 3.1 y 3.2
  (receptores para alumbrado); ITC-BT-47, apartado 3 y sus subapartados 3.1 y 3.2 (motores); ITC-BT-48, apartado 2.3
  (condensadores); ITC-BT-52, apartado 3.1
  (recarga de vehículos eléctricos).
- Normas UNE que esas instrucciones nombran y este tema no ha leído: UNE-EN 60831-1 y UNE-EN 60831-2
  (condensadores de compensación, ITC-BT-43 e ITC-BT-48).

## Lo que este tema no da, y dónde está

- Ningún valor de resistividad ni de conductividad de los metales: el REBT no los da y no se ha
  leído una norma de producto que los fije. El γ = 48 de los ejemplos del epígrafe 7.4 es un dato
  supuesto del ejercicio, no un valor de norma.
- Las tablas de intensidades máximas admisibles, sus coeficientes de corrección y la condición
  entre la corriente de diseño, la de la protección y la admisible del cable: tema 4 (canalizaciones
  y dimensionado) y tema 3 (protecciones). La ITC-BT-19 remite esas intensidades a la norma
  UNE 20.460-5-523, que no se ha leído.
- La facturación de la energía reactiva y el umbral de factor de potencia a partir del cual se
  penaliza: son de la normativa de tarifas y peajes de acceso, no del REBT, y no se han leído. Este
  tema no da ninguna cifra de penalización.
- Un porcentaje de desequilibrio admisible entre fases: el REBT no lo fija (epígrafe 8.1).
- La medida de tensión, corriente, potencias, factor de potencia, armónicos y desequilibrio, con
  multímetro, pinza y analizador de redes, y la diferencia entre valor medio y verdadero valor
  eficaz: tema 14.
- Transformadores y motores como máquinas (constitución, ensayos, arranque): el enunciado no los
  pide; aquí sólo se usan el 125 % de los motores y el arranque estrella-triángulo como consecuencia
  del sistema trifásico.
- La documentación, la puesta en servicio y las verificaciones de una instalación: tema 2. Las
  protecciones contra sobrecargas y cortocircuitos y la selectividad: tema 3. Las puestas a tierra:
  tema 5. Los armónicos y el ruido eléctrico en salas técnicas: tema 8. La eficiencia energética y la
  monitorización de consumos: tema 16. La consignación para cambiar circuitos de fase: tema 15.
- Los cuadros, las acometidas, el tipo de suministro y el reparto de cargas de los edificios de la
  RTVA y de CSRTV: no constan en ningún documento publicado.
- Cualquier reforma del REBT posterior a la última actualización del texto consolidado del BOE
  (18/12/2025): a la fecha de redacción no consta ninguna publicada, y un reglamento anunciado y no
  publicado no se estudia como vigente.

## Trazabilidad

| Fuente | Qué se ha tomado | Leída |
|---|---|---|
| Real Decreto 842/2002 (BOE-A-2002-18099), Reglamento, artículo 2, redacción vigente desde el 01/07/2021 (Real Decreto 298/2021, BOE-A-2021-6879) | Apartado 1, límites de tensión | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, Reglamento, artículos 4 y 16, redacción única (vigente desde el 18/09/2003) | Artículo 4, apartados 1, 2, 4 y 5; artículo 16, apartados 1 y 2 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-19, redacción única | Apartados 2.2.1, 2.2.2 (sus cuatro párrafos: límites y compensación; transformador propio; número de aparatos simultáneos; neutro), 2.2.3 (remisión a la UNE 20.460-5-523), 2.2.4 y 2.5 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-09, ITC-BT-14 e ITC-BT-15, redacción única | ITC-BT-09, apartados 3 (coeficiente 1,8, factor de potencia y caída de tensión) y 8; ITC-BT-14, caída de tensión y sección del neutro; ITC-BT-15, caída de tensión | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-43, ITC-BT-44 e ITC-BT-47, redacción única | ITC-BT-43, apartados 2.6 y 2.7; ITC-BT-44, apartados 3.1 y 3.2; ITC-BT-47, apartado 3 (frase de entrada), 3.1 y 3.2 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-48, redacción única | Apartado 2.3, condensadores | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-52, redacción vigente desde el 16/06/2022 (BOE-A-2022-9848) | Apartado 3.1 (aparcamientos de viviendas unifamiliares), reparto de estaciones monofásicas entre fases | En el BOE consolidado, 05/10/2026 |

El BOE consolidado del REBT da como última actualización el 18/12/2025; ninguno de los preceptos
citados ha cambiado desde las fechas indicadas.

Son física elemental, y así se declaran, sin atribuirlas a la norma: la ley de Ohm, las leyes de
Kirchhoff y la asociación de resistencias; la resistencia de un conductor y su variación con la temperatura; el efecto Joule;
las magnitudes de la señal alterna, la relación entre valor eficaz y de pico y los números de la red
de 50 Hz; las reactancias, la impedancia y el desfase; las conexiones en estrella y triángulo y la
raíz de tres entre 230 y 400 V; las tres potencias, el triángulo de potencias, la suma de potencias de
varios receptores (Boucherot) y las fórmulas de intensidad; la energía, el kilovatio hora y el rendimiento; el cálculo de la batería de
condensadores y de su capacidad en estrella y en triángulo; las fórmulas de caída de tensión y de sección; la corriente del neutro y la suma de
los armónicos de orden tres. Ninguna está en el REBT.

El resto va como oficio y así se declara: que un cálculo de instalación acaba en la ley de Ohm; que
los aislamientos se dimensionan por el pico; que transformadores, grupos y SAI se dan en
kilovoltamperios; las consecuencias de un factor de potencia bajo y de una caída excesiva; las
ventajas de cada forma de compensación; la regla de los dos criterios de sección y de que la
longitud sólo cuenta en la caída; los avisos sobre la reactancia de la línea y la conductividad a
temperatura de servicio; los efectos del desequilibrio y del neutro cortado; el procedimiento para
equilibrar un cuadro y las dos advertencias finales; que las baterías trifásicas se conectan en
triángulo; que la aparamenta de una batería se elige muy por encima de su corriente nominal por
los armónicos. Nada de eso lo dice la norma con esas palabras,
y el tema no lo presenta como si lo dijera.
