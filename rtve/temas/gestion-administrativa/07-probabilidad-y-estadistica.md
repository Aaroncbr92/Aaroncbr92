# Tema 7 del específico de Gestión Administrativa · Probabilidad y estadística descriptiva

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Gestión Administrativa · punto 7 |
| **Sirve para** | **Gestión Administrativa** |
| **Fuente** | **Ninguna**: la estadística descriptiva y el cálculo de probabilidades no se publican en un boletín oficial |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: las fórmulas no tienen redacción vigente |
| **Aviso sobre las fuentes** | **Segundo tema que se demuestra en vez de citarse**, y **el único punto de la ocupación sin una sola incidencia**: las once respuestas oficiales son correctas. Los cinco cálculos del examen —tres medianas, una moda y un rango— están rehechos en el tema con los datos y el procedimiento a la vista |
| **Extensión** | **1.844 palabras** |

<!-- /portada -->

**Las siglas y símbolos de este tema, presentados de entrada**: la Corporación de Radio y Televisión
Española (**CRTVE**), que aparece en un enunciado de examen; la media aritmética (**x̄**), la
desviación típica (**σ**) y la varianza (**σ²**).

> **Enunciado de la convocatoria (Anexo 2, temario específico de Gestión Administrativa, punto 7):**
> «Probabilidad: conceptos básicos; cálculo. Estadística: conceptos básicos; población y muestra;
> variables estadísticas; medidas de posición y centralización; medidas de dispersión.»

<!-- indice -->

## Índice

- [Antes de empezar: el segundo tema que se demuestra](#antes-de-empezar-el-segundo-tema-que-se-demuestra)
- [1. Población y muestra](#1-población-y-muestra)
  - [1.1. Qué hace aleatoria a una muestra](#11-qué-hace-aleatoria-a-una-muestra)
- [2. Variables estadísticas](#2-variables-estadísticas)
- [3. Medidas de posición y centralización](#3-medidas-de-posición-y-centralización)
  - [3.1. Las tres de tendencia central](#31-las-tres-de-tendencia-central)
  - [3.2. Cómo se calcula una mediana, paso a paso](#32-cómo-se-calcula-una-mediana-paso-a-paso)
  - [3.3. Cómo se calcula una moda](#33-cómo-se-calcula-una-moda)
  - [3.4. Los cuantiles](#34-los-cuantiles)
- [4. Medidas de dispersión](#4-medidas-de-dispersión)
- [5. Probabilidad](#5-probabilidad)
  - [5.1. Los conceptos](#51-los-conceptos)
  - [5.2. Las reglas que ordenan todo lo demás](#52-las-reglas-que-ordenan-todo-lo-demás)
  - [5.3. El cálculo elemental](#53-el-cálculo-elemental)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## Antes de empezar: el segundo tema que se demuestra

**Como el punto 6, este punto no tiene norma detrás.** La estadística descriptiva y el cálculo de
probabilidades no se publican en un boletín: se demuestran. **Y como allí, la garantía que sustituye
a la cita es que todos los cálculos del tema están hechos y escritos**, incluidos los cinco del
examen.

**A diferencia del punto 6, aquí las cinco cuentas del examen salen correctas.** Las cinco respuestas
oficiales coinciden con el resultado.

---

## 1. Población y muestra

- **Población** es el conjunto completo de elementos sobre los que se quiere concluir algo. Puede ser
  finita o infinita.
- **Muestra** es el subconjunto de la población que efectivamente se observa.
- **Unidad estadística** es cada elemento individual.
- **Censo** es la observación de la población entera; **muestreo**, la de una parte.

### 1.1. Qué hace aleatoria a una muestra

**Una muestra es aleatoria cuando todos los elementos de la población tienen la misma probabilidad de
formar parte de ella.** Ésa es la definición, y de ella depende que las conclusiones extraídas puedan
extenderse a la población.

**Lo que no es aleatorio, y el examen enumera como distractores:**

- **Muestreo por conveniencia**: se toma lo que está a mano.
- **Muestreo por criterio** o intencional: el investigador elige quién entra.
- **Muestreo por cuotas**: se fijan proporciones por grupos y dentro de cada grupo se elige sin
  aleatoriedad.

**Los tres son muestreos no probabilísticos.** Pueden ser útiles y baratos, pero **no permiten
calcular el error de muestreo**, porque no todos los elementos tenían la misma opción de entrar.

---

## 2. Variables estadísticas

**La primera división es entre cualitativas y cuantitativas**, y la segunda parte en dos las
cuantitativas.

| Tipo | Qué mide | Ejemplos |
|---|---|---|
| **Cualitativa nominal** | Categorías sin orden | Sexo, provincia, tipo de contrato |
| **Cualitativa ordinal** | Categorías con orden | Nivel de estudios, grado de satisfacción |
| **Cuantitativa discreta** | Valores aislados, normalmente enteros; **entre dos consecutivos no cabe otro** | Número de hijos, número de averías, número de trabajadores |
| **Cuantitativa continua** | Cualquier valor de un intervalo | Temperatura, tiempo, longitud, peso |

**La frontera entre discreta y continua es la que el examen pregunta, y se decide con una sola
prueba**: entre dos valores posibles, ¿cabe otro valor posible? Entre 2 y 3 hijos **no cabe** 2,5
hijos, luego el número de hijos es **discreta**. Entre 20 y 21 grados **caben** infinitos valores,
luego la temperatura es **continua**. Lo mismo vale para el tiempo y la longitud.

**Y dos afirmaciones falsas que conviene tener localizadas**, porque son las que el examen ofrece:
una variable **cualitativa no puede tomar cualquier valor numérico** —si lo tomara sería cuantitativa,
y los códigos numéricos que a veces se le asignan son etiquetas, no cantidades—; y una **cuantitativa
discreta no puede tomar cualquier valor dentro de un intervalo** —eso es precisamente la continua—.

---

## 3. Medidas de posición y centralización

### 3.1. Las tres de tendencia central

- **Media aritmética**: la suma de los valores dividida por su número. Usa **todos** los datos, y por
  eso **es sensible a los valores extremos**.
- **Mediana**: el valor que ocupa la posición central **una vez ordenados los datos**. Si el número de
  datos es par, es **la media de los dos centrales**. No la afectan los extremos.
- **Moda**: el valor **que más veces se repite**. Puede no ser única —distribución bimodal o
  multimodal— y puede no existir si ningún valor se repite.

**Sólo esas tres son medidas de tendencia central.** El **rango**, la **varianza** y la **desviación
típica** miden dispersión, no centro: dicen cuánto se separan los datos, no dónde están.

### 3.2. Cómo se calcula una mediana, paso a paso

**Es lo que el examen pregunta tres veces**, y siempre se falla por lo mismo: no ordenar.

**Caso par.** Edades 20, 40, 50 y 60. Ya están ordenadas y son cuatro datos, luego la mediana es la
media de los dos centrales:

> Mediana = (40 + 50) / 2 = 45

**Caso par con datos ya ordenados.** 5, 5, 7, 9, 11, 12, 15, 18. Ocho datos; los centrales son el
cuarto y el quinto:

> Mediana = (9 + 11) / 2 = 10

**Caso par con datos desordenados.** 1, 5, 2, 8, 9, 4, 7, 7, 5, 7. **Primero se ordenan**:

> 1, 2, 4, 5, 5, 7, 7, 7, 8, 9
> Diez datos; los centrales son el quinto y el sexto: (5 + 7) / 2 = 6

**Si no se ordena, sale otra cosa**, y ése es exactamente el error que el enunciado espera: tomando
los dos valores centrales de la lista sin ordenar —9 y 4— saldría 6,5, que no está entre las
opciones, o quien tome sólo uno de ellos se irá a la respuesta equivocada.

### 3.3. Cómo se calcula una moda

Calificaciones: 6, 4, 4, 4, 6, 10, 10, 8, 5, 6, 6, 8, 5. **Se cuentan las repeticiones:**

| Valor | 4 | 5 | 6 | 8 | 10 |
|---|---|---|---|---|---|
| Veces | 3 | 2 | **4** | 2 | 2 |

> Moda = 6

**El 4 aparece tres veces y llama la atención por estar seguido**, pero el 6 aparece cuatro. **La
moda se cuenta, no se mira.**

### 3.4. Los cuantiles

Además de la mediana, que parte la distribución en dos mitades:

- **Cuartiles**: la parten en cuatro. Q₁ deja por debajo el 25 % de los datos; Q₂ es la mediana; Q₃
  deja por debajo el 75 %.
- **Deciles**: en diez partes. **Percentiles**: en cien.

---

## 4. Medidas de dispersión

- **Rango o recorrido**: **el valor máximo menos el mínimo**. Es la medida más simple y la más
  sensible a un dato extremo, porque sólo usa dos.
- **Recorrido intercuartílico**: Q₃ − Q₁. Descarta el 25 % de cada extremo y por eso es robusto.
- **Varianza**: la media de los cuadrados de las desviaciones respecto a la media. Sus unidades son
  **las de la variable al cuadrado**, lo que la hace difícil de interpretar directamente.
- **Desviación típica**: **la raíz cuadrada de la varianza**. Vuelve a las unidades de la variable, y
  por eso es la medida de dispersión que se usa para comparar.
- **Coeficiente de variación**: desviación típica dividida entre la media. Es **adimensional**, y
  sirve para comparar la dispersión de variables medidas en unidades distintas.

**Ejemplo de rango.** Datos 5, 8, 12 y 20:

> Rango = 20 − 5 = 15

---

## 5. Probabilidad

### 5.1. Los conceptos

- **Experimento aleatorio**: aquel cuyo resultado no se puede predecir con certeza aunque se repita
  en las mismas condiciones.
- **Espacio muestral**: el conjunto de todos los resultados posibles.
- **Suceso**: cualquier subconjunto del espacio muestral.
- **Suceso seguro**: el que ocurre siempre; coincide con el espacio muestral entero.
- **Suceso imposible**: el que no ocurre nunca; es el conjunto vacío.

### 5.2. Las reglas que ordenan todo lo demás

**La probabilidad de cualquier suceso es un número comprendido entre 0 y 1**, ambos incluidos. De ahí
salen las dos afirmaciones que el examen pide reconocer:

- **La probabilidad del suceso seguro es 1.**
- **La probabilidad del suceso imposible es 0.**

Y las tres que ofrece como falsas: que la del imposible sea 1, que la del seguro sea 0, y que una
probabilidad pueda ser **negativa** —no puede: el mínimo es 0— o **mayor que 1** —tampoco: el máximo
es 1, y por eso el 1,5 que aparece entre las opciones se descarta sin más—.

### 5.3. El cálculo elemental

**Regla de Laplace**, válida cuando todos los resultados son igualmente probables:

> P(A) = casos favorables / casos posibles

**Suceso contrario**: P(Ā) = 1 − P(A).

**Unión**: P(A ∪ B) = P(A) + P(B) − P(A ∩ B). Si A y B son **incompatibles** —no pueden darse a la
vez— el último término es cero y las probabilidades simplemente se suman.

**Intersección**: si A y B son **independientes** —que uno ocurra no altera la probabilidad del
otro—, P(A ∩ B) = P(A) · P(B).

**Probabilidad condicionada**: P(A|B) = P(A ∩ B) / P(B), con P(B) > 0.

**Incompatible no es lo mismo que independiente**, y es la confusión más frecuente: dos sucesos
incompatibles con probabilidad positiva **son necesariamente dependientes**, porque saber que ha
ocurrido uno hace imposible el otro.

---

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Resultado | Respuesta oficial |
|---|---|---|---|
| 14 | Qué caracteriza a una muestra aleatoria | Misma probabilidad para todos | d) ✔ |
| 16 | Cuál es cuantitativa discreta | Número de hijos | a) ✔ |
| 36 | Probabilidad del suceso seguro | 1 | b) ✔ |
| 40 | Mediana de 20, 40, 50, 60 | (40 + 50) / 2 = 45 | d) ✔ |
| 45 | Moda de trece calificaciones | 6, que aparece cuatro veces | b) ✔ |
| 55 | Rango de 5, 8, 12, 20 | 20 − 5 = 15 | a) ✔ |
| 65 | Afirmación correcta sobre probabilidad | Está entre 0 y 1 | d) ✔ |
| 71 | Afirmación correcta sobre variables | La discreta toma valores aislados | c) ✔ |
| 78 | Cuál es medida de tendencia central | Media aritmética | c) ✔ |
| 79 | Mediana de diez datos desordenados | Ordenados: (5 + 7) / 2 = 6 | c) ✔ |
| 83 | Mediana de ocho datos ordenados | (9 + 11) / 2 = 10 | a) ✔ |

**Las once respuestas oficiales son correctas**, y las cinco numéricas están recalculadas arriba con
el procedimiento a la vista. **Es el único punto de esta ocupación sin una sola incidencia**: ni
errata de plantilla, ni enunciado defectuoso, ni respuesta sin fuente.

---

## 7. Trazabilidad

**Este tema, como el 6, no tiene fuente que citar.** La estadística descriptiva y el cálculo de
probabilidades son material común de la disciplina, no el contenido de una norma.

**La garantía que sustituye a la cita**: los cinco cálculos del examen —las tres medianas, la moda y
el rango— están rehechos en el epígrafe 3 y 4 con los datos y el procedimiento escritos, de modo que
cualquiera pueda repetirlos.

- **Cuadernillo `23_preguntas_gea`**, preguntas 14, 16, 36, 40, 45, 55, 65, 71, 78, 79 y 83, con su
  plantilla oficial.
