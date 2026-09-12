# Tema 1 del específico de Sonido · Electricidad y electrónica básicas

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Sonido · punto 1.1 y 1.2 |
| **Sirve para** | **Sonido** |
| **Fuente** | **Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida** |
| **Identificador** | `BOE-A-2010-927` · BOE núm. 21, de 24/01/2010 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. Se citan **celda a celda** las filas del cuadro de unidades derivadas que definen el voltio, el ohmio y el faradio: una fila de cuadro no se puede citar como prosa corrida |
| **Salvedad** | **La respuesta oficial a la pregunta 82 es la mejor de las cuatro y no es exacta**: un multímetro corriente mide resistencia en continua, no impedancia. **El temario la sostiene y lo declara.** Y la 46 pide «lo más aproximado»: el valor exacto de tres altavoces de 8 ohmios en paralelo es **2,67**, y la opción marcada es **2,5** |
| **Extensión** | **3.283 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: la corriente continua (**CC**, o **DC** en
la documentación en inglés) y la alterna (**CA**, o **AC**); el voltio (**V**), el amperio (**A**), el
ohmio (**Ω**), el vatio (**W**) y el faradio (**F**), que son unidades legales de medida; el hercio
(**Hz**); la distorsión armónica total (**THD**, *total harmonic distortion*); el decibelio referido a
0,775 voltios (**dBu**) y el referido al umbral de audición (**dB SPL**, *sound pressure level*); las clases
de amplificador, que se nombran por letra y de las que una es doble (**clase AB**); y el interruptor
diferencial, que el oficio llama a secas «el diferencial».

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, puntos 1.1 y 1.2):
> «CONOCIMIENTOS BÁSICOS. Electricidad básica. Electrónica básica aplicada a la captación y
> tratamiento del sonido.»

**Doce preguntas: el segundo banco de esta ocupación.** **Y el punto que más sorprende a quien llega
al temario esperando sonido**: **el examen de Sonido empieza por la ley de Ohm.**

**La razón no es caprichosa.** **Un técnico de sonido conecta altavoces en serie y en paralelo,
calcula si una etapa aguanta la carga, distingue un zumbido de masa de una avería, y decide si un
cable de sección insuficiente le va a costar potencia.** **Nada de eso es acústica: es electricidad.**

<!-- indice -->

## Índice

- [1. Las magnitudes eléctricas y sus unidades legales](#1-las-magnitudes-eléctricas-y-sus-unidades-legales)
- [2. La ley de Ohm](#2-la-ley-de-ohm)
- [3. La impedancia: la resistencia de la corriente alterna](#3-la-impedancia-la-resistencia-de-la-corriente-alterna)
- [4. Asociación de altavoces: serie y paralelo](#4-asociación-de-altavoces-serie-y-paralelo)
- [5. Por qué la impedancia baja hace perder corriente en el cable](#5-por-qué-la-impedancia-baja-hace-perder-corriente-en-el-cable)
- [6. El diferencial](#6-el-diferencial)
- [7. La corriente de la red](#7-la-corriente-de-la-red)
- [8. Los amplificadores y sus clases](#8-los-amplificadores-y-sus-clases)
- [9. Las distorsiones](#9-las-distorsiones)
- [10. Cómo se mide: el multímetro](#10-cómo-se-mide-el-multímetro)
- [11. Un apunte de trigonometría](#11-un-apunte-de-trigonometría)
- [12. Los datos que el examen ha preguntado](#12-los-datos-que-el-examen-ha-preguntado)
- [13. Trazabilidad](#13-trazabilidad)

<!-- /indice -->

## 1. Las magnitudes eléctricas y sus unidades legales

**Las cuatro magnitudes de un circuito, con la unidad que el Real Decreto 2032/2009 les asigna:**

| Magnitud | Qué es | Unidad legal |
|---|---|---|
| **Tensión** o diferencia de potencial | **La fuerza que empuja** a los electrones | **Voltio (V)** |
| **Intensidad** o corriente | **Cuántos electrones pasan** por segundo | **Amperio (A)** |
| **Resistencia** | **Lo que se opone al paso** | **Ohmio (Ω)** |
| **Potencia** | **Energía por unidad de tiempo** | **Vatio (W)** |

**Y no son convención de sector: están en el Boletín Oficial del Estado.** **El Real Decreto
2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida, recoge en su
cuadro de unidades derivadas coherentes las filas que las definen**, con las celdas separadas por
puntos porque un cuadro no se puede entrecomillar de otra manera y cada celda va literal:

> «diferencia de potencial eléctrico, fuerza electromotriz» · «voltio» · «V» · «W/A»
>
> «resistencia eléctrica» · «ohmio» · «Ω» · «V/A»
>
> «capacidad eléctrica» · «faradio» · «F» · «C/V»

**El amperio, además, es una de las siete unidades básicas del Sistema Internacional**, y no deriva de
ninguna otra.

## 2. La ley de Ohm

**La ley de Ohm describe la relación entre tensión, corriente y resistencia en un circuito
eléctrico.** Ésa es la respuesta oficial a la pregunta 74.

**La fórmula, y las tres maneras de despejarla:**

| Se busca | Fórmula |
|---|---|
| **Tensión** | **V = I × R** |
| **Intensidad** | **I = V / R** |
| **Resistencia** | **R = V / I** |

**Con ella se contesta la pregunta 11**: **un circuito de 5 ohmios que necesita 3 amperios requiere 15
voltios.** Ésa es la respuesta oficial. **5 × 3 = 15.**

**Y la trampa de esa pregunta no está en la cuenta, sino en las unidades**: **dos de las cuatro
opciones dan el resultado en vatios.** **0,6 V, 15 V, 0,6 W y 15 W**: **quien haga la cuenta y no mire
la unidad tiene una probabilidad de acertar del cincuenta por ciento.** **Es el patrón más rentable de
este cuadernillo: mirar siempre la unidad de la opción.**

**Las tres opciones falsas de la pregunta 74 describen otras tres relaciones que sí existen en
acústica**: **frecuencia y tono percibido** —que es materia del tema 2—, **longitud de onda y
velocidad del sonido**, y **la diferencia entre corriente alterna y continua.** **Ninguna es la ley de
Ohm.**

## 3. La impedancia: la resistencia de la corriente alterna

**La resistencia que se ofrece a una corriente alterna debido a la capacidad, la inductancia y la
resistencia de un circuito se denomina impedancia.** Ésa es la respuesta oficial a la pregunta 35.

**La distinción que la pregunta mide, y que es la más importante de todo el tema:**

| Concepto | En qué corriente | Qué la produce |
|---|---|---|
| **Resistencia** | **Continua y alterna** | **Sólo el material del conductor** |
| **Reactancia** | **Sólo alterna** | **La capacidad y la inductancia**, que dependen de la frecuencia |
| **Impedancia** ✔ | **Alterna** | **Resistencia y reactancia juntas** |

**Por qué le importa a un técnico de sonido**: **porque el audio es corriente alterna.** **Una señal de
audio cambia de sentido cientos o miles de veces por segundo**, así que **todo lo que un circuito de
audio opone a la señal es impedancia, no resistencia.** **Y como la reactancia depende de la
frecuencia, la impedancia de un altavoz o de un micrófono no es la misma a 100 Hz que a 10 kHz**: **el
número que da el fabricante es un valor nominal.**

**Las tres opciones falsas y qué son de verdad:**

1. **Resonancia** es **la frecuencia a la que un sistema vibra con más facilidad**: es un fenómeno, no
   una oposición.
2. **Capacitancia** es **una de las tres componentes**, no el conjunto. **Es la opción más cercana y la
   que hay que descartar leyendo el enunciado entero**: el enunciado nombra las tres.
3. **«Resistancia»** **no existe en castellano**: es un calco del inglés *resistance*.

## 4. Asociación de altavoces: serie y paralelo

**Si se conectan tres altavoces de 8 ohmios en paralelo, la impedancia resultante más aproximada es
2,5 ohmios.** Ésa es la respuesta oficial a la pregunta 46.

**La cuenta**: **en paralelo, con cargas iguales, la impedancia total es la de una dividida entre el
número de ellas.** **8 dividido entre 3 son 2,67 ohmios**, y **de las cuatro opciones la más próxima
es 2,5.** **El enunciado dice «más aproximada» precisamente porque el valor exacto no está entre
ellas.**

| Montaje | Fórmula con cargas iguales | Tres de 8 Ω |
|---|---|---|
| **Serie** | **Se suman**: Z × n | **24 Ω** |
| **Paralelo** | **Se divide**: Z / n | **2,67 Ω** |

**Y la consecuencia práctica, que es por qué esto se pregunta**: **al bajar la impedancia, la etapa
entrega más corriente.** **Una etapa estable hasta 4 ohmios conectada a 2,67 trabaja fuera de
especificación y puede protegerse o quemarse.** **La cuenta no es un ejercicio de escuela: decide si
el montaje se puede hacer.**

## 5. Por qué la impedancia baja hace perder corriente en el cable

**En un cable de altavoz habrá más pérdida de corriente si el altavoz conectado tiene un valor de 4
ohmios.** Ésa es la respuesta oficial a la pregunta 31, **y es la de menor impedancia de las cuatro
que ofrece.**

**El razonamiento, en tres pasos:**

1. **A menor impedancia de carga, mayor corriente circula** por el circuito, porque **la corriente es
   la tensión dividida entre la impedancia total.**
2. **El cable tiene su propia resistencia**, pequeña pero no nula.
3. **La pérdida en el cable crece con el CUADRADO de la corriente** —es I² × R—, **así que doblar la
   corriente cuadruplica la pérdida.**

**De ahí la regla del oficio**: **cuanto más baja es la impedancia del altavoz, más gruesa tiene que
ser la sección del cable y más corta la tirada.** **Con 16 ohmios se puede tirar lejos con poca
sección; con 4, no.**

**Y de ahí también la razón de ser de la línea de 100 voltios en megafonía**: **subiendo la tensión se
baja la corriente para la misma potencia**, y **con poca corriente la pérdida en el cable deja de
importar.**

## 6. El diferencial

**Un diferencial salta cuando no hay la misma intensidad entre hilos.** Ésa es la respuesta oficial a
la pregunta 29.

**Cómo funciona**: **el interruptor diferencial compara la corriente que entra por el activo con la
que vuelve por el neutro.** **En un circuito sano las dos son iguales.** **Si no lo son, es que parte
de la corriente se está yendo por otro camino** —tierra, la carcasa de un equipo, una persona— **y el
diferencial corta.**

**Su sensibilidad habitual en instalaciones de uso general es de 30 miliamperios**, que **es el orden
de magnitud por debajo del cual una corriente que atraviese a una persona no le produce fibrilación.**
**El diferencial no protege la instalación: protege a las personas.**

**Y las tres opciones falsas describen lo que hace OTRO aparato:**

| Opción | Qué aparato la hace |
|---|---|
| **El consumo es excesivo** | **El magnetotérmico**, en su parte térmica: protege contra sobrecargas |
| **Hay un cortocircuito** | **El magnetotérmico**, en su parte magnética: corta en milisegundos |
| **No coinciden las frecuencias** | **Ninguno**: no es una función de protección eléctrica |

**La distinción que hay que llevarse, y que en un plató salva un turno**: **si salta el
magnetotérmico, hay demasiado consumo o un cortocircuito y se revisa la carga.** **Si salta el
diferencial, hay una fuga a tierra y se busca el equipo que está derivando.** **Son dos averías
distintas y se buscan de dos maneras distintas.**

## 7. La corriente de la red

**Las redes eléctricas domésticas de la mayoría de los países europeos suministran corriente alterna a
230 voltios.** Ésa es la respuesta oficial a la pregunta 84.

**Los dos datos que la pregunta cruza, y las cuatro opciones son sus cuatro combinaciones:**

| | **230 V** | **110 V** |
|---|---|---|
| **Alterna** | **Europa** ✔ | **Ninguno de los dos habituales** |
| **Continua** | **No existe como red doméstica** | **No existe como red doméstica** |

**La frecuencia de esa alterna es de 50 hercios en Europa y de 60 en América**, y **ese dato, que la
pregunta no pide, es el que explica el zumbido de red**: **un zumbido de 50 Hz en un equipo de audio
europeo delata un problema de alimentación o de masas**, y **es exactamente lo que el cuadernillo de
la otra ocupación técnica de este proceso pregunta.**

## 8. Los amplificadores y sus clases

**Un amplificador de potencia en el que la tensión de polarización y la amplitud máxima de entrada
hacen que la corriente de salida circule durante menos de un semiperiodo funciona en clase C.** Ésa es
la respuesta oficial a la pregunta 70.

**Las clases se definen por el ángulo de conducción**, es decir, **por qué parte del ciclo de la señal
conduce el transistor de salida:**

| Clase | Cuánto conduce | Rendimiento | Distorsión | Dónde se usa |
|---|---|---|---|---|
| **A** | **El ciclo entero** —360º— | **Bajo**: en torno al 25 % | **Mínima** | **Etapas de calidad y previos** |
| **B** | **Medio ciclo** —180º— | **Mayor** | **Distorsión de cruce** | **Etapas en contrafase** |
| **Clase AB** | **Algo más de medio ciclo** | **Intermedio** | **Sin cruce apreciable** | **La inmensa mayoría de las etapas de audio** |
| **C** ✔ | **MENOS de medio ciclo** | **El más alto** | **Muy alta** | **Radiofrecuencia, no audio** |

**La palabra que decide la pregunta es «menos»**: **menos de un semiperiodo es menos de 180 grados, y
eso es la clase C.**

**Y el dato que conviene tener aunque no se pregunte**: **la clase C no sirve para audio.** **Su
distorsión es tan grande que la señal sólo se recupera con un circuito resonante sintonizado**, que es
justo lo que hay en un transmisor de radiofrecuencia. **En un equipo de sonido no se encuentra una
etapa de clase C.**

**La clase D, que la pregunta no ofrece, es la que hoy llevan casi todas las etapas de potencia de
sonorización**: **no es una prolongación de la serie A-B-C**, sino **conmutación**: el transistor está
del todo abierto o del todo cerrado, y el rendimiento supera el 90 %.

## 9. Las distorsiones

**Dos preguntas van de distorsión, y las dos se contestan con la misma tabla.**

| Distorsión | Qué la produce |
|---|---|
| **Armónica (THD)** | **El equipo añade armónicos** —múltiplos de la frecuencia de entrada— **que no estaban en la señal** |
| **De intermodulación** | **Dos frecuencias presentes se mezclan** y aparecen sumas y diferencias que no son armónicos de ninguna |
| **Por transitorios** ✔ | **El equipo no sigue un cambio brusco y rápido** de la señal |
| **Por sobremodulación** | **La señal excede el margen** del equipo y se recorta |

**La pregunta 17**: **si un componente de audio no puede responder rápidamente a un cambio brusco y
rápido de la señal, como un sonido percusivo, hablamos de distorsión por transitorios.** Ésa es la
respuesta oficial.

**La palabra que decide es «rápidamente»**: **es un problema de VELOCIDAD, no de nivel ni de mezcla.**
**Está relacionada con la velocidad de subida de la etapa** —cuántos voltios por microsegundo es capaz
de dar—, **y por eso la castiga un platillo o una caja de batería y no un tono sostenido.**

**La pregunta 67**: **si un amplificador tiene una distorsión armónica total del 0,1 %, significa que
el 0,1 % de la señal consiste en armónicos no presentes en la señal de entrada.** Ésa es la respuesta
oficial.

**Las tres opciones falsas y por qué caen:**

1. **«Distorsión mínima del 0,1 % en armónicos impares»** **restringe a los impares** lo que la THD
   mide en todos.
2. **«El 0,1 % de la señal será ruido»** **confunde distorsión con ruido**: **el ruido no guarda
   relación con la señal; la distorsión armónica es hija de ella.** **Es la falsa mejor puesta.**
3. **«Distorsionará 1 de cada 100 dB SPL»** **no significa nada**: mezcla un porcentaje con una escala
   logarítmica de presión sonora.

## 10. Cómo se mide: el multímetro

**La herramienta fundamental para medir la impedancia en un circuito de audio es el multímetro.** Ésa
es la respuesta oficial a la pregunta 82.

**Y aquí conviene una precisión que la respuesta oficial no hace y el temario sí**: **un multímetro
corriente NO mide impedancia: mide RESISTENCIA en continua.** **Lo que el técnico hace con él es
comprobar la resistencia de continua de una bobina de altavoz o de una línea**, que **es un valor
próximo a la impedancia nominal pero no el mismo** —la resistencia de continua de un altavoz de 8
ohmios nominales ronda los 6—. **Medir impedancia de verdad, frecuencia a frecuencia, exige un puente
de impedancias o un analizador.**

**Con esa salvedad, la respuesta oficial es la correcta de las cuatro que ofrece**, y **las otras tres
miden otra cosa:**

| Opción | Qué mide de verdad |
|---|---|
| **Osciloscopio** | **La forma de onda en el tiempo**: tensión frente a tiempo |
| **Sonómetro** | **El nivel de presión sonora en el aire**: no toca el circuito |
| **Preamplificador** | **No mide nada**: es un equipo de proceso |

## 11. Un apunte de trigonometría

**El seno de 90 grados sexagesimales es 1.** Ésa es la respuesta oficial a la pregunta 9.

**Y por sorprendente que sea encontrarla en un examen de Sonido, tiene su sitio**: **una señal de
audio senoidal se describe con un seno**, y **el valor 1 del seno es el máximo de la onda.** **Los
noventa grados son el pico.**

**Los cuatro valores que hay que tener, y con ellos se responde cualquier pregunta de esta clase:**

| Ángulo | Seno | Dónde cae en la onda |
|---|---|---|
| **0º** | **0** | **Cruce por cero, subiendo** |
| **90º** | **1** | **Pico positivo** |
| **180º** | **0** | **Cruce por cero, bajando** |
| **270º** | **−1** | **Pico negativo** |

**Y la aplicación que lo hace útil**: **dos señales desfasadas 180 grados se cancelan al sumarse**, que
es **el fundamento de la conexión balanceada del tema 11 y del defecto de polaridad invertida entre
dos micrófonos.**

## 12. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 9 | Cuánto vale el seno de 90 grados | c) 1 ✔ |
| 11 | Voltaje de un circuito de 5 Ω y 3 A | b) 15 V ✔ |
| 17 | Distorsión al no seguir un cambio brusco | c) Por transitorios ✔ |
| 29 | Cuándo salta un diferencial | b) No hay la misma intensidad entre hilos ✔ |
| 31 | Con qué impedancia se pierde más corriente en el cable | a) 4 ohmios ✔ |
| 35 | Cómo se llama la oposición a la corriente alterna | c) Impedancia ✔ |
| 46 | Tres altavoces de 8 Ω en paralelo | d) 2,5 ✔ **·** el valor exacto es 2,67 |
| 67 | Qué significa una THD del 0,1 % | c) El 0,1 % son armónicos no presentes en la entrada ✔ |
| 70 | Clase de un amplificador que conduce menos de medio ciclo | d) C ✔ |
| 74 | Qué describe la ley de Ohm | a) Tensión, corriente y resistencia ✔ |
| 82 | Herramienta para medir impedancia | d) Multímetro ✔ **·** con la salvedad del epígrafe 10 |
| 84 | Corriente de las redes domésticas europeas | b) Alterna a 230 V ✔ |

**Las doce respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla.**

**Dos avisos de lectura, y valen para todo el cuadernillo:**

1. **Mirar la unidad de la opción.** **La pregunta 11 ofrece el mismo número en voltios y en vatios.**
2. **Cuando el enunciado dice «más aproximada», el valor exacto no está entre las opciones.** **Se
   calcula y se elige el más cercano, sin buscar el redondo.**

## 13. Trazabilidad

**Este tema cita una norma del BOE.**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida** (`BOE-A-2010-927`), **en su redacción vigente el 21 de diciembre de 2022** | **Las filas del cuadro de unidades derivadas que definen el voltio, el ohmio y el faradio**, citadas celda a celda |

**Tres declaraciones expresas:**

1. **La respuesta oficial a la pregunta 82 es la mejor de las cuatro y no es exacta.** **Un multímetro
   corriente mide resistencia en continua, no impedancia.** **El temario sostiene la respuesta oficial
   porque las otras tres opciones miden cosas distintas**, y **declara la imprecisión en lugar de
   repetirla como si fuera una definición.**
2. **El valor exacto de la pregunta 46 es 2,67 ohmios y la plantilla da 2,5.** **No es una errata**:
   **el enunciado pide el valor «más aproximado» y 2,5 es el más próximo de los cuatro ofrecidos.**
   **El temario da la cuenta exacta y explica por qué la respuesta oficial es la correcta.**
3. **Las clases de amplificador y los tipos de distorsión son clasificaciones asentadas de la
   electrónica de audio**, no normalizadas por ninguna norma consultada. **El tema las presenta como
   conocimiento común de la materia.**

**El resto del tema va como oficio y así se declara**: la ley de Ohm y sus despejes, la asociación de
altavoces, la relación entre impedancia baja y pérdida en el cable, el funcionamiento del diferencial
y su diferencia con el magnetotérmico, las clases de amplificador y el papel del seno en una onda.
**Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo
presenta como si lo estuviera.
