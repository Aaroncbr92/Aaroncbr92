# Tema 2 del específico de Técnica de Equipos y Sistemas Electrónicos · Componentes electrónicos

Los términos y símbolos de este tema, presentados de entrada: la resistencia y su código de colores; el
potenciómetro; el condensador y su capacidad, medida en faradios (**F**) y en sus submúltiplos, el
microfaradio (**µF**), el nanofaradio (**nF**) y el picofaradio (**pF**); el culombio (**C**), unidad
de carga; el diodo y el diodo túnel; el transistor bipolar (**BJT**, *bipolar junction transistor*), sus
dos polaridades (**NPN** y **PNP**, por el orden de las capas de semiconductor) y sus tres patas
—base, colector y emisor—; la ganancia de corriente del transistor (**β**, beta); la
constante de tiempo de un circuito de resistencia y condensador (**τ**, tau); y los montajes de
filtro por resistencia y condensador (**RC**) o por bobina y condensador (**LC**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 2):
> «COMPONENTES ELECTRÓNICOS: Resistencias lineales. Potenciómetros. Condensadores. Diodo y
> transistores. Montajes con transistores.»

**Doce preguntas: el tercer banco de esta ocupación.** **Y el punto que más figuras trae**: **seis de
sus doce muestran un esquema, un símbolo o un dibujo de componente.**

**Y sin embargo es de los más contestables**, porque **cuatro de esas doce se resuelven con dos tablas
—el código de colores y las fórmulas del condensador— que este tema reúne.**

<!-- indice -->

## Índice

- [1. El código de colores de las resistencias](#1-el-código-de-colores-de-las-resistencias)
- [2. El condensador](#2-el-condensador)
- [3. Asociación de condensadores](#3-asociación-de-condensadores)
- [4. La carga de un condensador](#4-la-carga-de-un-condensador)
- [5. El diodo](#5-el-diodo)
- [6. El transistor bipolar](#6-el-transistor-bipolar)
- [7. El potenciómetro y los filtros pasivos](#7-el-potenciómetro-y-los-filtros-pasivos)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. El código de colores de las resistencias

**Dos preguntas del cuadernillo se contestan con esta sola tabla**, y **una tercera con la fila del
multiplicador.**

| Color | Cifra | Multiplicador |
|---|---|---|
| **Negro** | **0** | **× 1** |
| **Marrón** | **1** | **× 10** |
| **Rojo** | **2** | **× 100** |
| **Naranja** | **3** | **× 1.000** |
| **Amarillo** | **4** | **× 10.000** |
| **Verde** | **5** | **× 100.000** |
| **Azul** | **6** | **× 1.000.000** |
| **Violeta** | **7** | |
| **Gris** | **8** | |
| **Blanco** | **9** | |

**Y las dos bandas de tolerancia que el examen usa**: **dorado, ±5 %; plateado, ±10 %.**

**Cómo se lee una resistencia de cuatro bandas**: **las dos primeras son cifras, la tercera es el
multiplicador y la cuarta la tolerancia.**

**La pregunta 74**: **si el multiplicador de una resistencia es rojo, multiplica por 100.** Ésa es la
respuesta oficial.

**La pregunta 18 del segundo llamamiento**: **marrón, rojo, negro y dorado dan 12 ohmios.** Ésa es la
respuesta oficial. **Marrón es 1, rojo es 2, negro multiplica por 1: 12 × 1 = 12.**

**La pregunta 61, que junta el código con la ley de Ohm**: **una resistencia de naranja, negro, rojo y
dorado conectada a 12 voltios deja pasar 4 miliamperios.** Ésa es la respuesta oficial.

**La cuenta, en dos pasos:**

1. **El valor**: **naranja 3, negro 0, rojo ×100** → **30 × 100 = 3.000 ohmios.**
2. **La corriente**: **12 ÷ 3.000 = 0,004 amperios = 4 miliamperios.**

**Y el dato de 30 vatios que el enunciado da no interviene en la cuenta**: **es la capacidad de la
fuente, no lo que el circuito consume.** **Está para descolocar, y de hecho una de las opciones falsas
es «30 mA».**

## 2. El condensador

**La capacidad de un condensador es la carga que acumula por cada voltio aplicado:**

> **C = Q / V**

**La pregunta 21**: **un condensador con 0,002 culombios a 10 voltios tiene una capacitancia de 200
µF.** Ésa es la respuesta oficial.

**La cuenta y la conversión, que es donde está la trampa:**

1. **0,002 ÷ 10 = 0,0002 faradios.**
2. **0,0002 faradios son 200 microfaradios**, porque **un microfaradio es una millonésima de faradio.**

**Y las cuatro opciones están construidas sobre errores de prefijo**: **0,02 mF es lo mismo que 20 µF
—un factor de diez de menos—, 0,02 µF se equivoca en seis órdenes de magnitud y 0,002 F confunde la
carga con la capacidad.** **La aritmética es trivial; el manejo de prefijos, no.**

| Prefijo | Vale |
|---|---|
| **mili (m)** | **10⁻³** |
| **micro (µ)** | **10⁻⁶** |
| **nano (n)** | **10⁻⁹** |
| **pico (p)** | **10⁻¹²** |

## 3. Asociación de condensadores

**La pregunta 44 muestra una combinación de condensadores iguales de 5 µF y pide la capacidad
equivalente entre dos puntos.** **La respuesta oficial es 5 µF.**

**El temario no ha visto la figura.** **Lo que da es la regla de la familia**, que **es la que resuelve
cualquier pregunta de esta clase:**

1. **Los condensadores se asocian AL REVÉS que las resistencias.** **En PARALELO se suman las
   capacidades; en SERIE se suman las inversas.**
2. **Con n condensadores iguales de valor C**: **en paralelo dan n × C; en serie dan C / n.**
3. **Y de ahí el atajo que hace legible cualquier montaje simétrico**: **si el resultado es igual al
   valor de uno solo, el montaje tiene tantos en serie como ramas en paralelo.** **Dos ramas de dos en
   serie, por ejemplo, dan 2 × (C/2) = C.**

**Con esa tercera regla, un resultado de 5 µF a partir de condensadores de 5 µF se explica por sí
solo**, y **es lo que la respuesta oficial da.** **Ninguna de las tres reglas sustituye a ver la
figura**, y **el tema lo dice.**

## 4. La carga de un condensador

**La pregunta 70 también lleva figura**: **muestra un circuito con el condensador descargado y
pregunta qué tensión habrá adquirido C1 al cabo de un segundo.** **La respuesta oficial es 5 voltios.**

**La regla de familia, que es una de las más rentables de la electrónica:**

**Un condensador que se carga a través de una resistencia sigue una curva exponencial gobernada por la
constante de tiempo τ = R × C**, y **la tabla de esa curva se sabe de memoria:**

| Tiempo transcurrido | Tensión alcanzada |
|---|---|
| **1 τ** | **63 %** de la final |
| **2 τ** | **86 %** |
| **3 τ** | **95 %** |
| **5 τ** | **99 %**: se considera cargado |

**Y las dos comprobaciones que ordenan cualquier pregunta de este tipo:**

1. **Si el tiempo del enunciado es MUY MENOR que τ, la tensión es casi cero.** **Si es MUY MAYOR, es
   casi la de la fuente.** **La mayoría de estas preguntas se resuelven situando el tiempo en la
   escala, sin calcular nada.**
2. **Un resultado que sea exactamente la MITAD de la tensión de la fuente delata un divisor
   resistivo**, no la exponencial: **el condensador ya cargado se comporta como un circuito abierto y
   la tensión la fija la red de resistencias.**

**Ninguna de las dos sustituye a ver el esquema**, y **el tema lo dice.**

## 5. El diodo

**El diodo conduce en un sentido y no en el otro**, y **de ahí salen sus usos: rectificar, proteger
contra inversión de polaridad y recortar.**

**Sus valores característicos:**

| Dato | Valor corriente |
|---|---|
| **Tensión de codo en silicio** | **≈ 0,7 V** |
| **Tensión de codo en germanio** | **≈ 0,3 V** |
| **Tensión de codo en un led** | **De 1,8 a 3,5 V**, según el color |

**Y las variantes que un técnico de equipos encuentra:**

| Diodo | Para qué |
|---|---|
| **Rectificador** | **Convertir alterna en continua** |
| **Zener** | **Estabilizar una tensión**: trabaja en inversa |
| **Led** | **Emitir luz** |
| **Schottky** | **Conmutar rápido**, con caída menor |
| **Túnel** | **Presenta resistencia NEGATIVA en parte de su curva**: se usa en osciladores de muy alta frecuencia |

**La pregunta 26 pide identificar el símbolo del diodo túnel** y **la 34, el del transistor NPN.**
**Las dos dependen de una imagen y las dos descansan en la plantilla.**

**La regla de familia de los símbolos, que es lo que el temario puede aportar:**

1. **Todo diodo es un TRIÁNGULO que apunta a una BARRA.** **El triángulo indica el sentido de
   conducción y la barra es el cátodo.**
2. **Lo que distingue a cada variante es la FORMA DE LA BARRA**: **recta, el rectificador; con las
   puntas dobladas, el zener; en forma de ese, el Schottky; con dos trazos cortos, el túnel.**
3. **Y todo transistor bipolar es un círculo con tres patas, una de ellas con una FLECHA.** **La
   flecha está siempre en el EMISOR**, y **su sentido decide el tipo**: **si sale del transistor, es
   NPN; si entra, es PNP.** **La regla del oficio: «NPN, no apunta adentro».**

## 6. El transistor bipolar

**La corriente de colector en la región activa de un transistor bipolar es la corriente de base por el
factor de ganancia β.** Ésa es la respuesta oficial a la pregunta 76.

**Es la relación que define al transistor como amplificador:**

> **I(colector) = β × I(base)**

**Y con ella, la ley de nudos da la tercera corriente**: **la del emisor es la suma de las otras
dos.** **De ahí que las opciones falsas de la pregunta suenen todas plausibles: cada una enuncia mal
una de las dos relaciones verdaderas.**

**Las tres regiones de trabajo, que hay que separar:**

| Región | Cómo está | Para qué se usa |
|---|---|---|
| **Corte** | **No conduce** | **Interruptor abierto** |
| **Activa** ✔ | **La corriente de colector es β veces la de base** | **Amplificar** |
| **Saturación** | **Conduce todo lo que la carga deja**, y β deja de mandar | **Interruptor cerrado** |

**La pregunta 87 pide la ganancia en decibelios de un circuito amplificador con β = 200** y **lleva
figura.** **La respuesta oficial es 20 dB.**

**La regla de familia**: **la ganancia en decibelios de un amplificador de TENSIÓN es veinte veces el
logaritmo decimal de la relación de tensiones** —la misma fórmula del audio—, **y 20 dB corresponden a
una ganancia de diez veces.** **La beta del transistor NO es la ganancia de tensión del circuito**:
**la de tensión la fijan las resistencias de colector y de emisor.** **Confundir las dos es el error
que la pregunta busca.**

## 7. El potenciómetro y los filtros pasivos

**La pregunta 60 muestra un circuito con un potenciómetro y pide los valores máximo y mínimo que puede
medir un voltímetro.** **La respuesta oficial es mínimo 4 voltios, máximo 8.**

**La regla de familia**: **un potenciómetro en un divisor de tensión da un margen, no un valor.**
**Los dos extremos se calculan poniendo su resistencia a cero y a su valor máximo**, y **el resultado
es siempre un divisor resistivo: la tensión de salida es la de entrada multiplicada por la resistencia
de abajo dividida entre la suma de las dos.** **Si el margen calculado no incluye ni el cero ni la
tensión de la fuente, hay otra resistencia fija en serie**, que es lo normal en un circuito real.

**La pregunta 22 del segundo llamamiento**: **el componente que se utiliza principalmente para filtrar
una señal eléctrica eliminando frecuencias no deseadas es el filtro pasivo, RC o LC.** Ésa es la
respuesta oficial.

**Y aquí conviene una precisión que el temario hace**: **la opción marcada no nombra un COMPONENTE,
nombra un MONTAJE de componentes.** **Las otras tres sí son componentes —diodo, resistencia variable y
amplificador operacional— y ninguna filtra por sí sola.** **La respuesta es la correcta porque es la
única que describe algo que filtre**, y **el enunciado usa «componente» con holgura.**

**Los cuatro filtros pasivos básicos:**

| Filtro | Deja pasar |
|---|---|
| **Paso bajo** | **Las frecuencias por debajo del corte** |
| **Paso alto** | **Las de encima** |
| **Paso banda** | **Una franja** |
| **Banda eliminada** | **Todo menos una franja**: es el notch del temario de Sonido |

## 8. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 21 | Capacitancia de 0,002 C a 10 V | b) 200 µF ✔ |
| 26 | Símbolo del diodo túnel | c) ✔ **·** sólo con la plantilla |
| 34 | Símbolo del transistor NPN | b) ✔ **·** sólo con la plantilla |
| 44 | Capacidad equivalente de la combinación | b) 5 µF ✔ **·** sólo con la plantilla |
| 60 | Valores máximo y mínimo del voltímetro | a) Mínimo 4 V, máximo 8 V ✔ **·** sólo con la plantilla |
| 61 | Corriente por una resistencia de código naranja, negro, rojo | a) 4 mA ✔ |
| 70 | Tensión del condensador al cabo de 1 segundo | b) 5 V ✔ **·** sólo con la plantilla |
| 74 | Por cuánto multiplica el color rojo | c) 100 ✔ |
| 76 | Corriente de colector en región activa | c) La de base por β ✔ |
| 87 | Ganancia en decibelios del amplificador | d) 20 dB ✔ **·** sólo con la plantilla |
| 18 (2.º llam.) | Valor de una resistencia marrón, rojo, negro, dorado | c) 12 ohmios ✔ |
| 22 (2.º llam.) | Componente que filtra frecuencias no deseadas | a) Filtro pasivo RC o LC ✔ |

**Las doce respuestas oficiales son correctas.**

**Seis de las doce descansan sólo en la plantilla**: **las seis que dependen de una figura.** **Es la
proporción más alta de todos los temas de esta ocupación y de todo el proyecto.**

**Y el aviso de estudio, que es el que hay que retener**: **de las seis restantes, CINCO se contestan
con las dos tablas de este tema** —el código de colores y los prefijos—. **Aprender esas dos tablas es
lo más rentable que se puede hacer con media hora en esta ocupación.**

## 9. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son los componentes electrónicos pasivos y activos, y
**va como oficio**, salvo seis afirmaciones que descansan en la plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Seis afirmaciones**: dos identificaciones de símbolo y cuatro resultados numéricos de circuitos que el temario no puede reproducir | Preguntas 26, 34, 44, 60, 70 y 87 |

**Cuatro declaraciones expresas:**

1. **Seis de las doce preguntas dependen de una figura y el temario no la describe.** **Lo que aporta
   en su lugar son cuatro reglas de familia**: la asociación inversa de condensadores, la tabla de la
   constante de tiempo, la construcción de los símbolos de diodo y transistor, y el margen de un
   divisor con potenciómetro. **Ninguna sustituye a ver la figura**, y **el tema lo dice.**
2. **El código de colores y la tabla de prefijos son normalizados por la Comisión Electrotécnica
   Internacional**, cuya norma **no se ha consultado en este proyecto.** **Los valores que este tema da
   son los de uso universal y coinciden con las respuestas oficiales**, y **no se atribuyen a un
   articulado.**
3. **Las tensiones de codo del epígrafe 5 son valores típicos, no especificaciones.** **Varían con el
   componente, con la corriente y con la temperatura**, y **ninguna pregunta depende de ellas.**
4. **Sobre la pregunta 22 del segundo llamamiento, el temario sostiene la respuesta oficial y señala
   que su enunciado usa «componente» con holgura**: **un filtro RC o LC es un montaje de componentes,
   no un componente.** **Es la única de las cuatro opciones que filtra, y por eso es la correcta.**

**El resto del tema va como oficio y así se declara**: la lectura del código de colores, la fórmula de
la capacidad, la asociación de condensadores, la curva de carga y su tabla, la familia de diodos, las
tres regiones del transistor y la relación entre corriente de base y de colector, y los cuatro filtros
pasivos. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el
tema no lo presenta como si lo estuviera.
