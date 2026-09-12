# Tema 1 del específico de Técnica de Equipos y Sistemas Electrónicos · Conceptos básicos de electricidad

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica de Equipos y Sistemas Electrónicos · punto 1 |
| **Sirve para** | **Técnica de Equipos y Sistemas Electrónicos** |
| **Fuente** | **Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida** |
| **Identificador** | `BOE-A-2010-927` · BOE núm. 21, de 24/01/2010 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. Se citan **celda a celda** las filas del cuadro de unidades derivadas que definen el voltio, el ohmio y el faradio |
| **Sólo con la plantilla** | **Dos preguntas dependen de un esquema de circuito** que un temario escrito no puede reproducir. **El temario no los describe**: da la regla de la familia —ley de Ohm y leyes de nudos y mallas— y declara que la respuesta descansa en la plantilla |
| **Extensión** | **2.175 palabras** |

<!-- /portada -->

Las siglas y unidades de este tema, presentadas de entrada: la corriente continua (**CC**, o **DC**) y
la alterna (**CA**, o **AC**); el voltio (**V**), el amperio (**A**), el ohmio (**Ω**), el vatio
(**W**), el voltamperio (**VA**) y el voltamperio reactivo (**var**); el henrio (**H**) y el faradio
(**F**); el hercio (**Hz**); el valor eficaz (**RMS**, *root mean square*); las siglas con que este proyecto abrevia el nombre
de la ocupación (**TESE**, Técnica de Equipos y Sistemas Electrónicos); y el factor de potencia, que se
escribe **cos φ** porque es el coseno del ángulo de desfase.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 1):
> «CONCEPTOS BÁSICOS DE ELECTRICIDAD: Principios básicos de electricidad. Corriente eléctrica.
> Magnitudes eléctricas. Ley de Ohm. Corriente continua. Corriente alterna.»

**Seis preguntas.** **Y el punto que abre la ocupación por donde hay que abrirla**: **todo lo que
viene después —componentes, amplificadores, digital, medida— se apoya en las cuatro magnitudes que
aquí se fijan.**

**Un aviso capital, y hay que darlo en el primer tema porque afecta a toda la ocupación**: **dos de
estas seis preguntas dependen de un esquema de circuito que el temario no puede reproducir.** **En
esta ocupación eso no es una excepción: es la norma.** **Alrededor de treinta de las 114 preguntas del
específico llevan una figura**, y **el método de este temario es siempre el mismo: declararlo, no
describir lo que no ha visto y dar la regla de la familia.**

<!-- indice -->

## Índice

- [1. Las magnitudes y sus unidades legales](#1-las-magnitudes-y-sus-unidades-legales)
- [2. La ley de Ohm y las tres fórmulas de potencia](#2-la-ley-de-ohm-y-las-tres-fórmulas-de-potencia)
- [3. Serie y paralelo](#3-serie-y-paralelo)
- [4. La corriente alterna y el desfase](#4-la-corriente-alterna-y-el-desfase)
- [5. El factor de potencia](#5-el-factor-de-potencia)
- [6. Las dos preguntas que dependen de un esquema](#6-las-dos-preguntas-que-dependen-de-un-esquema)
- [7. La pregunta 28: potencia y semiciclos](#7-la-pregunta-28-potencia-y-semiciclos)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Las magnitudes y sus unidades legales

**Las cuatro magnitudes de un circuito, con la unidad que el Real Decreto 2032/2009 les asigna:**

| Magnitud | Símbolo | Qué es | Unidad |
|---|---|---|---|
| **Tensión** | **V** o **U** | **La diferencia de potencial que empuja** | **Voltio** |
| **Intensidad** | **I** | **Cuánta carga pasa por segundo** | **Amperio** |
| **Resistencia** | **R** | **La oposición al paso** | **Ohmio** |
| **Potencia** | **P** | **Energía por unidad de tiempo** | **Vatio** |

**Y están en el Boletín Oficial del Estado.** **El Real Decreto 2032/2009, de 30 de diciembre, por el
que se establecen las unidades legales de medida, las recoge en su cuadro de unidades derivadas
coherentes**, con las celdas separadas por puntos porque un cuadro no admite otro entrecomillado y
cada celda va literal:

> «diferencia de potencial eléctrico, fuerza electromotriz» · «voltio» · «V» · «W/A»
>
> «resistencia eléctrica» · «ohmio» · «Ω» · «V/A»
>
> «capacidad eléctrica» · «faradio» · «F» · «C/V»

**El amperio es, además, una de las siete unidades básicas del Sistema Internacional.**

## 2. La ley de Ohm y las tres fórmulas de potencia

**La ley de Ohm relaciona las tres primeras magnitudes:**

> **V = I × R**

**Y la potencia se calcula de tres maneras equivalentes, según qué dos datos haya:**

| Se tiene | Fórmula |
|---|---|
| **Tensión y corriente** | **P = V × I** |
| **Corriente y resistencia** | **P = I² × R** |
| **Tensión y resistencia** | **P = V² / R** |

**La tercera es la que resuelve las preguntas de este examen que dan tensión y resistencia**, y **la
segunda es la que explica por qué la pérdida en un cable crece con el cuadrado de la corriente.**

## 3. Serie y paralelo

**En un circuito en paralelo, la tensión es la misma en todos los componentes.** Ésa es la respuesta
oficial a la pregunta 40.

**Y conviene tener las cuatro reglas juntas, porque el examen las usa en varios puntos:**

| | **Serie** | **Paralelo** |
|---|---|---|
| **Tensión** | **Se reparte** entre los componentes | **La misma en todos** ✔ |
| **Corriente** | **La misma por todos** | **Se reparte** |
| **Resistencias** | **Se suman** | **Se suman las inversas** |
| **Condensadores** | **Se suman las inversas** | **Se suman** |

**La última fila es la que más se falla**: **los condensadores se comportan al revés que las
resistencias.** **Es lo que la pregunta 44, del tema 2, mide.**

**Las tres opciones falsas de la pregunta 40 describen el comportamiento en serie o disparates**: **«se
divide entre los componentes» es la serie; «aumenta en cada componente» y «es cero» no ocurren en
ningún montaje.**

## 4. La corriente alterna y el desfase

**En un sistema trifásico, las fases están desfasadas 120 grados entre ellas.** Ésa es la respuesta
oficial a la pregunta 59.

**La cuenta es inmediata**: **tres fases repartidas por igual en un ciclo completo de 360 grados dan
120 grados cada una.** **Y de ahí se sigue la propiedad que hace útil el sistema trifásico: la suma
instantánea de las tres es cero**, lo que **permite prescindir del neutro en cargas equilibradas y
transportar más potencia con menos cobre.**

**Y las cuatro opciones son ángulos con sentido eléctrico**, lo que **hace la pregunta buena:**

| Ángulo | Dónde aparece de verdad |
|---|---|
| **120º** ✔ | **El desfase de un trifásico** |
| **90º** | **El desfase entre tensión y corriente en una bobina o un condensador puros** |
| **180º** | **La oposición de fase**: la de la conexión balanceada del audio |
| **60º** | **No corresponde a ningún desfase característico** |

## 5. El factor de potencia

**El factor de potencia en un circuito de corriente alterna es la relación entre la potencia activa y
la potencia aparente.** Ésa es la respuesta oficial a la pregunta 31.

**Las tres potencias de la corriente alterna, que es lo que la pregunta exige separar:**

| Potencia | Qué es | Unidad |
|---|---|---|
| **Activa (P)** | **La que realiza trabajo**: calienta, mueve, ilumina | **Vatio (W)** |
| **Reactiva (Q)** | **La que va y viene** entre la fuente y las bobinas o condensadores **sin hacer trabajo** | **Voltamperio reactivo (var)** |
| **Aparente (S)** | **El producto de tensión por corriente**: lo que la instalación tiene que soportar | **Voltamperio (VA)** |

**Y la relación entre las tres es un triángulo rectángulo**: **la aparente es la hipotenusa.** **El
factor de potencia es el coseno del ángulo entre la activa y la aparente**, de ahí **cos φ.**

**Por qué le importa a un técnico de equipos**: **una instalación con factor de potencia bajo necesita
más corriente para entregar la misma potencia útil.** **Cables más gruesos, protecciones mayores y, en
grandes consumidores, penalización en la factura.** **Las fuentes conmutadas modernas llevan
corrección del factor de potencia precisamente por eso.**

**Las tres opciones falsas cambian uno de los dos términos del cociente**: **activa entre reactiva,
tensión entre corriente —que es una resistencia— y resistencia entre reactancia —que es la tangente
del mismo ángulo, no el coseno—.** **La última es la mejor puesta.**

## 6. Las dos preguntas que dependen de un esquema

**Dos de las seis preguntas de este punto muestran un circuito y el temario no lo ha visto.**

**La pregunta 7 del segundo llamamiento** pide **el valor de la tensión entre dos puntos de un
circuito** y **la respuesta oficial es −1,6 voltios.**

**La pregunta 26 del segundo llamamiento** pide **la potencia que entrega una fuente con una carga de
1 kiloohmio y 1 henrio** y **la respuesta oficial es 144 milivatios.**

**El temario no describe esos esquemas, porque no los tiene delante.** **Lo que sí puede dar, y da, es
la regla de su familia**, que **es lo que hace legible cualquier pregunta de esta clase:**

1. **Un valor de tensión negativo entre dos puntos no es un error: es una convención de sentido.**
   **Significa que el punto A está a menos potencial que el B.** **En un circuito con varias fuentes,
   el signo del resultado es parte de la respuesta**, y **las opciones que sólo cambian el signo están
   puestas para quien recorra la malla en sentido contrario.**
2. **Para hallar una tensión entre dos puntos se recorre un camino entre ellos sumando** las
   elevaciones de las fuentes y **restando** las caídas de las resistencias. **El resultado no depende
   del camino elegido: si sale distinto, hay un error de signo.**
3. **Cuando el enunciado da una inductancia —el henrio de la pregunta 26— hay que preguntarse en qué
   régimen está el circuito.** **En corriente continua estacionaria una bobina ideal es un
   cortocircuito y no consume potencia activa**; **en alterna, su reactancia depende de la frecuencia.**
   **La potencia que una fuente entrega es la activa, y la bobina no la consume: la devuelve.** **Por
   eso una carga con parte inductiva no disipa más que su parte resistiva.**

**Ninguna de las tres reglas sustituye a ver el esquema**, y **el tema lo dice.**

## 7. La pregunta 28: potencia y semiciclos

**Ésta también lleva figura, y su respuesta se puede razonar entera sin verla**, que es **lo que la
hace la mejor del punto.**

**El enunciado da V1 = 5 voltios y R1 = 1 kiloohmio y pregunta por la potencia consumida en la
resistencia en relación al voltaje.** **La respuesta oficial es la b)**: **la potencia será positiva en
el semiciclo positivo y positiva en el semiciclo negativo.**

**El razonamiento es la fórmula del epígrafe 2**: **P = V² / R.** **La tensión está elevada al
cuadrado**, y **el cuadrado de un número negativo es positivo.** **Una resistencia disipa potencia en
los dos semiciclos, y la disipa siempre en el mismo sentido: la convierte en calor.**

**Una resistencia no puede devolver energía al circuito.** **Sólo las bobinas y los condensadores lo
hacen**, y **ésa es exactamente la potencia reactiva del epígrafe 5.**

## 8. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 28 | Potencia en la resistencia según el semiciclo | b) Positiva en los dos ✔ |
| 31 | Qué es el factor de potencia | a) Relación entre potencia activa y aparente ✔ |
| 40 | Qué ocurre con la tensión en un circuito en paralelo | a) Es la misma en todos los componentes ✔ |
| 59 | Desfase de las fases de un sistema trifásico | a) 120º ✔ |
| 7 (2.º llam.) | Tensión entre dos puntos de un circuito | a) −1,6 V ✔ **·** sólo con la plantilla |
| 26 (2.º llam.) | Potencia que entrega una fuente con carga | b) 144 mW ✔ **·** sólo con la plantilla |

**Las seis respuestas oficiales son correctas.**

**Dos de las seis descansan sólo en la plantilla**: **las dos que dependen de un esquema.**

**Y el aviso que abre esta ocupación**: **una cuarta parte larga de las preguntas de este temario
lleva figura.** **Quien lo prepare tiene que practicar con esquemas de circuito, tablas de verdad y
trazas de osciloscopio**, y **eso un temario escrito no lo sustituye.** **Lo que sí da, tema a tema, es
la regla con la que cada familia de figura se lee.**

## 9. Trazabilidad

**Este tema cita una norma del BOE.**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida** (`BOE-A-2010-927`), **en su redacción vigente el 21 de diciembre de 2022** | **Las filas del cuadro de unidades derivadas que definen el voltio, el ohmio y el faradio**, citadas celda a celda |
| **Quinto: la plantilla oficial** | **Dos afirmaciones**: los resultados numéricos de dos circuitos que el temario no puede reproducir | Preguntas 7 y 26 del segundo llamamiento |

**Tres declaraciones expresas:**

1. **Las preguntas 7 y 26 del segundo llamamiento dependen enteramente de un esquema.** **El temario
   no lo describe**, y **lo que aporta en su lugar son las tres reglas del epígrafe 6**: el signo como
   convención de sentido, el recorrido de malla y el papel de una inductancia en la potencia activa.
   **Ninguna sustituye a ver el esquema**, y **el tema lo dice.**
2. **La pregunta 28 también lleva figura y su respuesta NO descansa en la plantilla**: **se razona
   entera con la fórmula de la potencia**, y **el tema muestra el razonamiento.** **Es el ejemplo de
   que una pregunta con imagen no es automáticamente una pregunta perdida.**
3. **Las fórmulas, las reglas de serie y paralelo y la descomposición de la potencia en activa,
   reactiva y aparente son conocimiento asentado de la electrotecnia**, no normalizado por ninguna
   norma consultada. **El tema las presenta como conocimiento común de la materia.**

**El resto del tema va como oficio y así se declara**: la ley de Ohm y las tres fórmulas de potencia,
las cuatro reglas de serie y paralelo, la propiedad de suma nula del trifásico y la consecuencia
práctica de un factor de potencia bajo. **Nada de eso está en un boletín oficial ni en una norma
técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
