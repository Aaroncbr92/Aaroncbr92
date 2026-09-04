# Tema 1 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Fundamentos de electricidad y medida

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Téc. Equipos, Instalaciones y Sistemas Eléctricos · punto 1 |
| **Sirve para** | **Téc. Equipos, Instalaciones y Sistemas Eléctricos** |
| **Fuente** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** |
| **Identificador** | `BOE-A-2002-18099` · BOE núm. 224, de 18/09/2002 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. Se citan **los apartados 2 y 4 del artículo 4** |
| **Aviso de reparto** | **Este punto NOMBRA transformadores y motores; el punto 2 los DESARROLLA.** Aquí se presentan y se remite: dos temas del mismo específico no dicen lo mismo |
| **Extensión** | **3.422 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: el reglamento electrotécnico para baja
tensión (**REBT**) y sus instrucciones técnicas complementarias (**ITC-BT 01** a **ITC-BT 52**); el
voltio (**V**), el amperio (**A**), el ohmio (**Ω**), el vatio (**W**), el kilovatio (**kW**), el
voltamperio (**VA**) y el kilovoltamperio (**kVA**); el hercio (**Hz**); la tensión nominal (**Un**);
la corriente alterna (**CA**) y la corriente continua (**CC**); el valor eficaz (**RMS**, *root mean
square*); y la Asociación Española de Normalización (**UNE**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación
> tipo de Técnica de Equipos, Instalaciones y Sistemas Eléctricos, punto 1):
> «Conocimientos de electricidad: Tensión, corriente y resistencia. La ley de Ohm. Corriente alterna
> y corriente continua. Medición de corriente y tensión en continua y alterna. Transformadores.
> Motores.»

**Es el punto de fundamentos, y hay que decir de entrada cómo se reparte con el 2**: **el enunciado de
este punto NOMBRA los transformadores y los motores, y el punto 2 los DESARROLLA.** **Este tema los
presenta y remite; el tema 2 los estudia.** **Repetirlos aquí sería escribir dos veces lo mismo**, que
es lo que este proyecto prohíbe.

**Y una advertencia de método que ordena la ocupación entera**: **este anexo tiene DIECISIETE puntos y
los dos últimos del específico son el reglamento electrotécnico y sus instrucciones.** **Eso significa
que casi todo lo que aquí se estudia como física acaba teniendo un artículo detrás**, y **el temario
lo señala cada vez que ocurre.**

<!-- indice -->

## Índice

- [1. Las tres magnitudes y la ley que las une](#1-las-tres-magnitudes-y-la-ley-que-las-une)
- [2. Potencia, energía y el factor de potencia](#2-potencia-energía-y-el-factor-de-potencia)
- [3. Corriente continua y corriente alterna](#3-corriente-continua-y-corriente-alterna)
- [4. El sistema trifásico](#4-el-sistema-trifásico)
- [5. La medida de tensión y de corriente](#5-la-medida-de-tensión-y-de-corriente)
- [6. Los transformadores y los motores, y dónde se estudian](#6-los-transformadores-y-los-motores-y-dónde-se-estudian)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Las tres magnitudes y la ley que las une

**Las tres magnitudes fundamentales, con su definición, su símbolo y su unidad:**

| Magnitud | Qué es | Símbolo | Unidad |
|---|---|---|---|
| **Tensión, diferencia de potencial o voltaje** | **El trabajo necesario para mover una carga entre dos puntos**: la causa que empuja | **U** o **V** | **Voltio, V** |
| **Intensidad de corriente** | **La cantidad de carga que atraviesa una sección por unidad de tiempo**: el efecto | **I** | **Amperio, A** |
| **Resistencia** | **La oposición que un conductor ofrece al paso de la corriente** | **R** | **Ohmio, Ω** |

**La ley de Ohm relaciona las tres**, y **hay que saber decirla en las tres formas, porque un examen
puede pedir cualquiera de ellas:**

| Forma | Qué despeja | Cuándo se usa |
|---|---|---|
| **U = R · I** | **La tensión** | Caída de tensión en un tramo de conductor |
| **I = U / R** | **La intensidad** | Corriente que va a circular por un receptor |
| **R = U / I** | **La resistencia** | Resistencia deducida de una medida |

**Y la lectura de oficio que hay que tener hecha, porque es la que decide un cálculo de instalación**:
**en una instalación real la tensión es un dato fijo —la de la red— y la resistencia es lo que se
elige.** **Lo que resulta de las dos es la corriente**, y **la corriente es lo que dimensiona el cable
y el interruptor.** **Por eso un cálculo de instalación no empieza en la ley de Ohm: acaba en ella.**

**La resistencia de un conductor, que es la fórmula que este oficio usa todos los días:**

**R = ρ · L / S**

| Símbolo | Qué es |
|---|---|
| **ρ** | **La resistividad del material**, propia de cada metal y **dependiente de la temperatura** |
| **L** | **La longitud del conductor** |
| **S** | **La sección del conductor** |

**Las tres consecuencias que se leen directamente en esa fórmula**, y **que son el fundamento del punto
5 del anexo:**

1. **La resistencia crece con la LONGITUD.** **Una línea larga cae más.**
2. **La resistencia baja con la SECCIÓN.** **Un cable más grueso cae menos.**
3. **La resistencia depende del MATERIAL.** **El cobre conduce mejor que el aluminio**, y **por eso a
   igual corriente el aluminio pide más sección.**

**Y la que no se lee y hay que añadir**: **la resistividad SUBE con la temperatura en los metales.**
**Un conductor cargado se calienta, y al calentarse conduce peor y se calienta más.** **Ésa es la
razón física de que las intensidades admisibles de la instrucción técnica dependan de la forma de
instalación y de la temperatura ambiente.**

## 2. Potencia, energía y el factor de potencia

**La potencia en corriente continua es un producto**: **P = U · I**, en vatios.

**En corriente alterna hay TRES potencias y confundirlas es el error de facturación más caro del
oficio:**

| Potencia | Qué es | Unidad | Fórmula en monofásica |
|---|---|---|---|
| **ACTIVA, P** | **La que se transforma en trabajo o calor**: la que se consume de verdad | **Vatio, W** | **P = U · I · cos φ** |
| **REACTIVA, Q** | **La que va y vuelve** para magnetizar bobinas y cargar condensadores | **Voltamperio reactivo, var** | **Q = U · I · sen φ** |
| **APARENTE, S** | **La que la instalación tiene que poder transportar** | **Voltamperio, VA** | **S = U · I** |

**Y en trifásica, las mismas con el factor raíz de tres**: **P = √3 · U · I · cos φ**, con **U** la
tensión entre fases.

**El FACTOR DE POTENCIA, cos φ, es el cociente entre la activa y la aparente**, y **la lectura de
oficio que hay que saber dar es ésta**: **un cos φ bajo significa que por el cable circula más
corriente de la que hace falta para el trabajo que se hace.**

| Consecuencia de un cos φ bajo | Por qué |
|---|---|
| **Más corriente para la misma potencia útil** | Porque **I = P / (U · cos φ)** |
| **Más caída de tensión y más pérdidas** | Porque las dos dependen de la corriente |
| **Más sección de cable y más aparamenta** | Porque se dimensionan por corriente |
| **Penalización en factura** | Porque la distribuidora transporta lo que no se aprovecha |

**Y lo que lo corrige**: **la batería de condensadores**, que **aporta la reactiva que las cargas
inductivas piden**, de modo que **no tenga que traerla la red.** **El condensador se pone lo más cerca
posible de la carga que causa el problema**, y **eso enlaza con el tema 2, porque la carga inductiva
típica de una instalación es el MOTOR.**

**La energía es la potencia por el tiempo**: **E = P · t**, en kilovatios hora. **Es lo que mide el
contador y lo que se paga.** **La potencia es lo que se contrata; la energía es lo que se gasta.**

## 3. Corriente continua y corriente alterna

**La diferencia de fondo, dicha en una línea**: **en continua la magnitud no cambia de valor ni de
sentido; en alterna cambia las dos cosas periódicamente.**

| | **Corriente continua** | **Corriente alterna** |
|---|---|---|
| **Sentido** | **Siempre el mismo** | **Se invierte cada semiperiodo** |
| **Valor** | **Constante** | **Varía siguiendo una senoide** |
| **De dónde sale** | **Pilas, baterías, rectificadores, paneles fotovoltaicos** | **Alternadores** |
| **Transformable** | **No directamente**: hace falta convertirla | **Sí, con un TRANSFORMADOR** |
| **Dónde manda** | **Electrónica, baterías, tracción, sistemas de alimentación ininterrumpida** | **Generación, transporte y distribución** |

**Y la razón HISTÓRICA Y TÉCNICA de que la red sea alterna, que es lo que hay que saber explicar**:
**la alterna se puede elevar y reducir de tensión con un transformador, sin partes móviles y con
rendimiento altísimo.** **Y elevar la tensión permite transportar la misma potencia con menos
corriente**, porque **las pérdidas en un conductor son proporcionales al CUADRADO de la corriente.**
**Ésa es la única razón por la que existe una red de alta tensión**, y **es toda la justificación del
punto 6 del anexo.**

**Las magnitudes de una señal alterna, que hay que saber nombrar:**

| Magnitud | Qué es |
|---|---|
| **Valor de pico o máximo** | **El valor más alto** que alcanza en cada semiperiodo |
| **Valor de pico a pico** | **El doble del anterior**, del máximo positivo al negativo |
| **Valor medio** | **En una senoide completa es CERO**; en un semiperiodo, no |
| **Valor EFICAZ** | **El de una continua que produciría el mismo efecto calorífico** |
| **Periodo, T** | **Lo que tarda en repetirse un ciclo** |
| **Frecuencia, f** | **Ciclos por segundo**, en hercios; **f = 1 / T** |

**El valor EFICAZ es el que se maneja siempre y hay que decirlo expresamente**: **cuando se dice que la
red es de 230 voltios, son 230 voltios EFICACES.** **En una senoide, el valor eficaz es el máximo
dividido por raíz de dos**, de modo que **una red de 230 voltios eficaces tiene picos de unos 325.**
**Esa cifra importa porque los aislamientos y las tensiones soportadas se dimensionan por el pico, no
por el eficaz.**

**Y aquí está la primera cita literal del punto, que es la que da los valores oficiales de la red
española:**

**Artículo 4**, apartado 2, del reglamento electrotécnico para baja tensión:

> «**Las tensiones nominales usualmente utilizadas en las distribuciones de corriente alterna serán:
> a) 230 V entre fases para las redes trifásicas de tres conductores.
> b) 230 V entre fase y neutro, y 400 V entre fases, para las redes trifásicas de 4 conductores,**»
>
> — Real Decreto 842/2002, artículo 4.2 (`BOE-A-2002-18099`), redacción vigente el 21 de diciembre de
> 2022.

---

**Artículo 4**, apartado 4:

> «**La frecuencia empleada en la red será de 50 Hz.**»
>
> — Real Decreto 842/2002, artículo 4.4 (`BOE-A-2002-18099`), redacción vigente el 21 de diciembre de
> 2022.

---

**Y la relación entre 230 y 400, que un ingeniero debe poder explicar**: **es la raíz de tres.**
**En una red trifásica de cuatro conductores, la tensión entre dos fases es raíz de tres veces la
tensión entre una fase y el neutro**, y **eso es geometría de vectores desfasados 120 grados, no una
afirmación de la norma.** **El reglamento da las dos cifras y no las relaciona.**

## 4. El sistema trifásico

**Tres tensiones alternas de la misma amplitud y frecuencia, desfasadas 120 grados entre sí.** **Ésa es
la definición y de ella sale todo lo demás.**

**Por qué se usa, en tres razones que hay que saber enunciar:**

1. **Transporta más potencia con menos cobre** que tres circuitos monofásicos independientes.
2. **La potencia instantánea es CONSTANTE**, no pulsante como en monofásica, **y eso hace posible un
   par de motor uniforme.**
3. **Permite crear un campo magnético giratorio**, que es **lo que hace girar un motor asíncrono sin
   ningún artificio de arranque.** **Eso es materia del tema 2.**

**Las dos conexiones, que son el vocabulario básico de la ocupación:**

| Conexión | Cómo se une | Relación de tensiones | Relación de corrientes |
|---|---|---|---|
| **ESTRELLA** | **Un extremo de cada devanado a un punto común, el NEUTRO** | **La de línea es raíz de tres veces la de fase** | **La de línea es igual a la de fase** |
| **TRIÁNGULO** | **Cada devanado entre dos fases**, en serie cerrada | **La de línea es igual a la de fase** | **La de línea es raíz de tres veces la de fase** |

**La regla que las resume y que evita confundirlas**: **la raíz de tres está siempre, y cambia de sitio.
En estrella está en la TENSIÓN; en triángulo, en la CORRIENTE.**

**Y la consecuencia práctica más importante, que es la base del arranque estrella-triángulo del tema
2**: **un mismo motor conectado en estrella recibe en cada devanado una tensión raíz de tres veces
menor que en triángulo**, y **por tanto absorbe una potencia TRES veces menor.**

**El NEUTRO y por qué existe**: **es el conductor unido al punto común de la estrella**, y **permite
disponer de dos tensiones en la misma red** —230 entre fase y neutro para receptores monofásicos y 400
entre fases para trifásicos—. **Y su otra función, que es la que importa a la seguridad**: **por él
circula el desequilibrio**, y **por eso una instalación muy desequilibrada carga el neutro.**

## 5. La medida de tensión y de corriente

**Ésta es la parte del enunciado que separa a esta ocupación de un temario teórico**: **medición de
corriente y tensión en continua y alterna.**

**Las dos reglas de conexión, que no se pueden confundir y que hay que saber decir con su razón:**

| Instrumento | Cómo se conecta | Qué resistencia interna tiene | Por qué |
|---|---|---|---|
| **VOLTÍMETRO** | **En PARALELO** con el elemento a medir | **MUY ALTA**, idealmente infinita | **Para no derivar corriente** y no alterar el circuito |
| **AMPERÍMETRO** | **En SERIE**, abriendo el circuito | **MUY BAJA**, idealmente cero | **Para no añadir caída de tensión** |

**Y el error que la regla previene, que es el más grave que se comete con un polímetro**: **conectar un
amperímetro en paralelo sobre una tensión es un cortocircuito a través del instrumento.** **La escala
de corriente de un polímetro tiene una resistencia mínima y un fusible; ése es el fusible que se
funde**, y **con una fuente potente detrás lo que se produce es un arco.**

**La PINZA AMPERIMÉTRICA es la respuesta del oficio a ese problema**, y **hay que saber por qué es la
herramienta característica de esta ocupación:**

| Rasgo | Qué aporta |
|---|---|
| **Mide sin abrir el circuito** | **No hay que cortar nada ni dejar la instalación sin servicio** |
| **Aísla al operador del circuito** | **La medida se hace por el campo magnético del conductor** |
| **Abraza UN solo conductor** | **Si abraza los dos, la suma es cero y no mide nada** |

**El último rasgo tiene una aplicación directa y muy útil**: **abrazar a la vez fase y neutro de un
circuito debería dar CERO.** **Si no da cero, hay una corriente que se va por otro camino**, es decir,
**una corriente de fuga.** **Ésa es la medida con la que se busca una derivación que hace saltar un
diferencial.**

**Las tecnologías de pinza, y la diferencia que decide cuál se compra:**

| Tecnología | Qué mide |
|---|---|
| **De transformador de corriente** | **Sólo ALTERNA**: necesita un campo variable |
| **De efecto Hall** | **ALTERNA Y CONTINUA** |

**El valor que muestra un instrumento en alterna, y aquí está la trampa clásica**: **un polímetro
convencional mide el valor medio rectificado y lo escala suponiendo una senoide perfecta.** **Ante una
corriente deformada —la de un variador, una fuente conmutada o un balasto electrónico— la lectura es
FALSA por defecto.** **Lo que hay que usar es un instrumento de VERDADERO VALOR EFICAZ**, y **en una
instalación moderna, con electrónica en casi todo, ésa es la única lectura fiable.**

**Los demás instrumentos de la ocupación, que se desarrollan en el tema 9:**

| Instrumento | Qué mide |
|---|---|
| **Polímetro o multímetro** | **Tensión, corriente, resistencia, continuidad y a veces frecuencia y capacidad** |
| **Telurómetro** | **La resistencia de una puesta a tierra** |
| **Megóhmetro** | **La resistencia de AISLAMIENTO**, con tensión de ensayo elevada |
| **Analizador de redes** | **Potencias, factor de potencia, armónicos y calidad de onda** |
| **Comprobador de instalaciones** | **Bucle de defecto, disparo del diferencial, continuidad y aislamiento** |

**Y la regla de seguridad que precede a toda medida y que es del tema 14**: **antes de medir hay que
saber qué se va a medir y con qué categoría de medida está clasificado el instrumento.** **Un
polímetro de categoría insuficiente conectado en la cabecera de una instalación es un accidente
esperando el transitorio.**

## 6. Los transformadores y los motores, y dónde se estudian

**El enunciado de este punto los nombra y este tema los presenta, sin desarrollarlos:**

| Máquina | Qué hace, en una línea | Dónde se estudia |
|---|---|---|
| **Transformador** | **Cambia la tensión de una corriente alterna sin cambiar su frecuencia**, con dos devanados acoplados por un núcleo magnético | **Tema 2**, epígrafes 1 a 4 |
| **Motor** | **Convierte energía eléctrica en energía mecánica de rotación** | **Tema 2**, epígrafes 5 a 8 |

**Y lo que sí corresponde decir aquí, porque es fundamento y no máquina**: **las dos leyes en las que
se apoyan los dos.**

| Ley | Qué dice | Qué explica |
|---|---|---|
| **Inducción electromagnética** | **Un flujo magnético VARIABLE a través de un circuito induce en él una tensión** | **El transformador entero**, y por qué **no funciona en continua** |
| **Fuerza sobre un conductor** | **Un conductor recorrido por corriente dentro de un campo magnético sufre una fuerza** | **El par de un motor** |

**La primera es la que explica la frontera del epígrafe 3**: **el transformador necesita un flujo
variable, y una corriente continua no lo da.** **De ahí que la continua no se pueda transformar
directamente y que toda la red de transporte sea alterna.**

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión** (`BOE-A-2002-18099`), **en su redacción vigente el 21 de diciembre de 2022** | **Los apartados 2 y 4 del artículo 4**, citados literalmente |

**Un aviso de la lente de exactitud que hay que declarar**: **esta fuente repite los números de
artículo**, porque **cada una de las cincuenta y dos instrucciones técnicas complementarias numera sus
apartados desde uno.** **La cita de este tema es del ARTICULADO del reglamento**, no de ninguna
instrucción, y **así se identifica al pie.**

**Cinco declaraciones expresas:**

1. **Este tema no desarrolla los transformadores ni los motores**, aunque **el enunciado de su punto
   los nombre.** **Los desarrolla el tema 2, que es el punto 2 del mismo anexo**, y **este tema los
   presenta y remite.** **La razón es de método: dos temas del mismo específico no dicen lo mismo.**
2. **Las fórmulas de este tema son física elemental y así se declaran**: **la ley de Ohm, la
   resistencia de un conductor, las tres potencias, la relación entre valor eficaz y valor de pico y
   la raíz de tres del sistema trifásico.** **Ninguna se atribuye a la norma**, y **el reglamento no
   contiene ninguna de ellas.**
3. **La relación de raíz de tres entre 230 y 400 voltios es aritmética**, no una afirmación del
   reglamento: **el artículo 4.2 da las dos cifras y no las relaciona.**
4. **Este tema no da ninguna tabla de intensidades admisibles, ninguna resistividad y ninguna
   caída de tensión máxima.** **Están en las instrucciones técnicas, que se estudian en los temas 5 y
   15**, y **una cifra que no se ha leído en su fuente no se escribe.**
5. **Las normas que este tema nombra y no se han consultado aquí**: **la norma UNE 20.460-6-61**, que
   la instrucción de verificaciones nombra como metodología, **y las categorías de medida de los
   instrumentos**, que son de norma de producto. **De ninguna se afirma nada más que lo que el
   temario dice de ellas: que existen y para qué se nombran.**

**El resto del tema va como oficio y así se declara**: el reparto explícito entre este punto y el 2, la
lectura de que un cálculo de instalación acaba en la ley de Ohm y no empieza en ella, las tres
consecuencias de la fórmula de la resistencia y la cuarta sobre la temperatura, la explicación de por
qué la red es alterna a partir de las pérdidas proporcionales al cuadrado de la corriente, la
observación de que los aislamientos se dimensionan por el pico y no por el eficaz, la regla de que la
raíz de tres está en la tensión en estrella y en la corriente en triángulo, la explicación de las dos
funciones del neutro, las dos reglas de conexión de voltímetro y amperímetro con su razón, el aviso
sobre el amperímetro en paralelo, la lectura de la pinza que abraza fase y neutro como medida de
fuga, la advertencia sobre el valor eficaz verdadero frente al medio rectificado y la presentación de
las dos leyes que sostienen transformador y motor. **Nada de eso lo dice la norma con esas palabras**,
y el tema no lo presenta como si lo dijera.
