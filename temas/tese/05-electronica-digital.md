# Tema 5 del específico de Técnica de Equipos y Sistemas Electrónicos · Electrónica digital

Los términos y siglas de este tema, presentados de entrada: el bit y el byte; los sistemas de
numeración binario, decimal y hexadecimal (**hex**); las puertas lógicas —**AND**, **OR**, **NOT**,
**NAND**, **NOR**, **XOR** (u O exclusiva) y **XNOR**—; la tabla de verdad; el bit menos significativo
(**LSB**, *least significant bit*) y el más significativo (**MSB**); la conversión
analógico-digital y digital-analógica (**A/D** y **D/A**); el teorema del muestreo y el solapamiento
espectral que su incumplimiento produce (*aliasing*).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 5):
> «ELECTRÓNICA DIGITAL: Sistemas digitales. Conversiones analógico/digital y digital/analógico.
> Funciones lógicas y puertas lógicas. Esquemas y expresiones lógicas. Obtención de tablas de verdad.»

**Seis preguntas.** **Y el punto que separa la primera mitad de la ocupación de la segunda**: **de aquí
en adelante, casi todo lo que un técnico de equipos toca es digital.**

**Su reparto**: **tres preguntas son de lógica —dos de ellas con figura—, dos son de conversión de
base y una es del teorema del muestreo.**

<!-- indice -->

## Índice

- [1. Los sistemas de numeración](#1-los-sistemas-de-numeración)
- [2. Las puertas lógicas](#2-las-puertas-lógicas)
- [3. La conversión analógico-digital](#3-la-conversión-analógico-digital)
- [4. Los esquemas y las expresiones lógicas](#4-los-esquemas-y-las-expresiones-lógicas)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Los sistemas de numeración

**Tres bases conviven en electrónica digital, y hay que saber pasar de una a otra:**

| Base | Dígitos | Para qué |
|---|---|---|
| **Binaria (2)** | **0 y 1** | **Lo que el circuito maneja de verdad** |
| **Hexadecimal (16)** | **0 a 9 y A a F** | **Escribir binario de forma compacta**: cada dígito son 4 bits |
| **Decimal (10)** | **0 a 9** | **Lo que las personas leen** |

**Y la tabla de equivalencia que hay que tener en la cabeza, porque con ella se hace todo:**

| Binario | Hex | Decimal |
|---|---|---|
| **0000** | **0** | 0 |
| **0001** | **1** | 1 |
| **0010** | **2** | 2 |
| **0011** | **3** | 3 |
| **0100** | **4** | 4 |
| **0101** | **5** | 5 |
| **1000** | **8** | 8 |
| **1010** | **A** | 10 |
| **1100** | **C** | 12 |
| **1111** | **F** | 15 |

**La pregunta 12**: **el número binario 110100101 expresado en hexadecimal es 1A5.** Ésa es la
respuesta oficial.

**El procedimiento, que es mecánico y no admite error si se hace en este orden:**

1. **Agrupar de CUATRO EN CUATRO desde la DERECHA**, rellenando con ceros por la izquierda:
   **`1 1010 0101`** → **`0001 1010 0101`.**
2. **Traducir cada grupo con la tabla**: **`0001` = 1**, **`1010` = A**, **`0101` = 5.**
3. **El resultado es 1A5.**

**El error que las opciones falsas explotan es agrupar desde la IZQUIERDA.** **Hay que hacerlo siempre
desde el bit menos significativo**, que es **el de la derecha.**

**La pregunta 21 del segundo llamamiento** muestra la imagen de un equipo direccionado y pregunta **a
qué número decimal corresponde esa dirección, siendo el bit 1 el de menor peso.** **La respuesta
oficial es 300.**

**El temario no ha visto la imagen.** **Lo que da es la regla de la familia:**

1. **Un banco de microinterruptores se lee como un número binario**: **cada interruptor es un bit, y
   el enunciado dice cuál es el de menor peso.**
2. **El valor de cada bit es una potencia de dos**: **1, 2, 4, 8, 16, 32, 64, 128, 256…** **Se suman
   los que estén a uno.**
3. **La frase «siendo el bit 1 el de menor peso» es la clave y está ahí para evitar la ambigüedad**:
   **dice por qué extremo empieza la cuenta.** **Leerlo al revés da un número completamente distinto**,
   y **por eso las opciones falsas incluyen números que salen de la lectura invertida.**

**Ninguna sustituye a ver la imagen**, y **el tema lo dice.**

## 2. Las puertas lógicas

**Las siete puertas, con su tabla de verdad para dos entradas:**

| Entradas | **AND** | **OR** | **NAND** | **NOR** | **XOR** | **XNOR** |
|---|---|---|---|---|---|---|
| **0 0** | 0 | 0 | **1** | **1** | 0 | **1** |
| **0 1** | 0 | **1** | **1** | 0 | **1** | 0 |
| **1 0** | 0 | **1** | **1** | 0 | **1** | 0 |
| **1 1** | **1** | **1** | 0 | 0 | 0 | **1** |

**Y la manera de recordarlas sin memorizar la tabla:**

| Puerta | Da 1 cuando… |
|---|---|
| **AND** | **Todas** las entradas son 1 |
| **OR** | **Alguna** entrada es 1 |
| **NAND** | **No todas** son 1: es la AND negada |
| **NOR** | **Ninguna** es 1: es la OR negada |
| **XOR** | **Las entradas son distintas** |
| **XNOR** | **Las entradas son iguales** |

**La pregunta 56**: **la salida generada por una compuerta XOR devuelve un valor verdadero sólo cuando
uno y sólo uno de sus valores de entrada es también verdadero.** Ésa es la respuesta oficial.

**Es la definición exacta de la O exclusiva para dos entradas**, y **la palabra que decide es
«sólo».** **La opción que dice «cuando los dos valores de entrada son verdaderos» describe a la AND.**

**La pregunta 50** muestra una tabla de verdad y pide **a qué puerta corresponde.** **La respuesta
oficial es XNOR.**

**El temario no ha visto la tabla.** **La regla de familia es la de arriba, leída al revés:**

1. **Mirar la fila `0 0`.** **Si da 1, la puerta está NEGADA** —NAND, NOR o XNOR—. **Si da 0, no lo
   está.**
2. **Mirar la fila `1 1`.** **Con las dos filas extremas ya se separan las seis puertas**: **NOR da 1
   sólo en `0 0`; NAND da 0 sólo en `1 1`; XNOR da 1 en las DOS filas extremas y 0 en las dos del
   medio.**
3. **Y el patrón de la XNOR es inconfundible**: **1, 0, 0, 1.** **El de la XOR es su inverso: 0, 1, 1,
   0.**

**La pregunta 82** muestra un circuito de puertas y pregunta **a qué equivale.** **La respuesta oficial
es una puerta NOR exclusiva** —es decir, la XNOR—.

**La regla de familia para simplificar un circuito de puertas, en tres pasos:**

1. **Escribir la tabla de verdad del circuito entero**, entrada por entrada. **Es más lento que
   manipular expresiones y no se equivoca.**
2. **Comparar el resultado con los seis patrones del epígrafe.**
3. **Y tener presentes las dos leyes de De Morgan**, que **son las que explican por qué circuitos de
   aspecto muy distinto son el mismo**: **la negación de una AND es la OR de las negadas, y la
   negación de una OR es la AND de las negadas.**

**Ninguna de las tres sustituye a ver la figura**, y **el tema lo dice.** **Lo que sí hacen es
convertir el problema en algo mecánico en cuanto la figura se tiene delante.**

## 3. La conversión analógico-digital

**Convertir una señal analógica en digital son dos operaciones, y el examen pregunta por el fallo de
la primera.**

| Operación | Qué hace | Qué la mide |
|---|---|---|
| **Muestreo** | **Tomar el valor a intervalos regulares** | **La frecuencia de muestreo** |
| **Cuantificación** | **Asignar a cada muestra un valor de una escala finita** | **El número de bits** |

**La pregunta 57**: **el aliasing se produce cuando se muestrea una señal menos del doble que su
frecuencia máxima.** Ésa es la respuesta oficial.

**Es el teorema del muestreo enunciado por su incumplimiento**: **para reconstruir una señal hay que
muestrearla a más del doble de su frecuencia más alta.** **Por debajo de ese límite, las frecuencias
altas no desaparecen: se PLIEGAN y reaparecen como frecuencias bajas que no estaban.**

**De ahí que todo conversor lleve delante un filtro anti-solapamiento**: **un paso bajo que corta por
encima de la mitad de la frecuencia de muestreo.** **Ese filtro no es opcional.**

**Y las tres opciones falsas describen otros tres defectos reales de la digitalización:**

| Opción | Qué defecto es de verdad |
|---|---|
| **«Se recibe una señal con ruido»** | **Ruido**, sin más: no es un fenómeno de muestreo |
| **«Un punto de la cuantificación no es exacto»** | **El error de cuantificación**: es de la SEGUNDA operación, no de la primera |
| **«Recibes la señal desfasada»** | **Un desfase**: no produce solapamiento |

**El aliasing en vídeo se ve, y es la manera de fijar el concepto**: **es el dibujo de muaré de una
corbata de rayas finas o el efecto de rueda que gira al revés en el cine.** **La misma matemática, en
el espacio y en el tiempo.**

## 4. Los esquemas y las expresiones lógicas

**El enunciado pide «esquemas y expresiones lógicas» y «obtención de tablas de verdad»**, y **eso es el
método del epígrafe 2 puesto en orden.**

**Las tres representaciones de una misma función, y cómo se pasa de una a otra:**

| Representación | Qué es | Se obtiene |
|---|---|---|
| **Esquema** | **El dibujo de las puertas** | **Es lo que el examen enseña** |
| **Expresión** | **La fórmula algebraica** | **Recorriendo el esquema de la entrada a la salida** |
| **Tabla de verdad** | **La salida para cada combinación de entradas** | **Evaluando la expresión, o el esquema, en todos los casos** |

**Y la regla práctica**: **la tabla de verdad es la representación que NO admite discusión.** **Dos
circuitos son equivalentes si y sólo si tienen la misma tabla.** **Cuando una pregunta pide a qué
equivale un montaje, la tabla lo resuelve siempre**, aunque sea el camino más largo.

## 5. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 12 | El binario 110100101 en hexadecimal | d) 1A5 ✔ |
| 50 | A qué puerta corresponde la tabla de verdad | d) XNOR ✔ **·** sólo con la plantilla |
| 56 | Qué salida genera una compuerta XOR | a) Verdadero sólo cuando uno y sólo uno lo es ✔ |
| 57 | Cuándo se produce el aliasing | c) Al muestrear a menos del doble de la frecuencia máxima ✔ |
| 82 | A qué equivale el circuito de puertas | a) Una NOR exclusiva ✔ **·** sólo con la plantilla |
| 21 (2.º llam.) | A qué decimal corresponde la dirección de la imagen | d) 300 ✔ **·** sólo con la plantilla |

**Las seis respuestas oficiales son correctas.**

**Tres de las seis descansan sólo en la plantilla**: **las tres que dependen de una figura.**

**Y el aviso de estudio**: **las tres restantes se contestan con la tabla de puertas y con el
procedimiento de agrupar de cuatro en cuatro desde la derecha.** **Son dos cosas que se aprenden en
diez minutos y no se olvidan.**

## 6. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es la electrónica digital, y **va como oficio**, salvo
tres afirmaciones que descansan en la plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Tres afirmaciones**: una tabla de verdad, un circuito de puertas y una imagen de direccionamiento que el temario no puede reproducir | Preguntas 50, 82 y 21 del segundo llamamiento |

**Tres declaraciones expresas:**

1. **Las preguntas 50, 82 y 21 del segundo llamamiento dependen de una figura.** **El temario no la
   describe**, y **lo que aporta en su lugar son tres reglas de familia**: cómo se identifica una
   puerta por sus filas extremas, cómo se demuestra la equivalencia de dos circuitos con una tabla de
   verdad, y cómo se lee un banco de microinterruptores sabiendo cuál es el bit de menor peso.
   **Ninguna sustituye a ver la figura**, y **el tema lo dice.**
2. **La respuesta oficial de la pregunta 82 llama «NOR exclusiva» a lo que la nomenclatura corriente
   llama XNOR o NOR-exclusiva.** **Es la misma puerta**, y **el temario usa las dos denominaciones para
   que no haya duda.**
3. **Las tablas de verdad, el teorema del muestreo y las leyes de De Morgan son conocimiento asentado
   del álgebra de conmutación y de la teoría de la señal**, no normalizados por ninguna norma
   consultada. **El tema los presenta como conocimiento común de la materia.**

**El resto del tema va como oficio y así se declara**: la conversión entre bases y el procedimiento de
agrupar desde el bit menos significativo, la tabla de las seis puertas y sus reglas mnemotécnicas, la
distinción entre muestreo y cuantificación, el mecanismo del solapamiento y las tres representaciones
de una función lógica. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
