# Tema 29 del específico de Gestión · Estadística descriptiva básica

Las siglas de este tema, presentadas de entrada: la desviación típica (**σ**, sigma), el coeficiente
de variación (**CV**) y el Boletín Oficial del Estado (**BOE**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Gestión, punto 29):
> «Estadística descriptiva básica: población y muestra; variables estadísticas; frecuencias;
> distribuciones; medidas de posición y centralización; medidas de dispersión; representaciones
> gráficas.»

*Como el punto 28, no descansa en ninguna norma*: es matemática. Y por la misma razón, **ninguna
cifra calculada va en negrita**: los números se dan con la operación a la vista para que el lector
la repita.

<!-- indice -->

## Índice

- [1. Población y muestra](#1-población-y-muestra)
- [2. Variables estadísticas](#2-variables-estadísticas)
- [3. Frecuencias y distribuciones](#3-frecuencias-y-distribuciones)
- [4. Medidas de centralización](#4-medidas-de-centralización)
- [5. Medidas de posición](#5-medidas-de-posición)
- [6. Medidas de dispersión](#6-medidas-de-dispersión)
- [7. Varianza de la población y cuasivarianza de la muestra](#7-varianza-de-la-población-y-cuasivarianza-de-la-muestra)
- [8. Forma de la distribución](#8-forma-de-la-distribución)
- [9. Representaciones gráficas](#9-representaciones-gráficas)
- [10. Los datos que el examen ha preguntado](#10-los-datos-que-el-examen-ha-preguntado)
- [11. Trazabilidad](#11-trazabilidad)

<!-- /indice -->

## 1. Población y muestra

- **Población** o *universo*: el conjunto **completo** de elementos sobre los que se quiere
  concluir. Puede ser **finita** o **infinita**.
- **Muestra**: el subconjunto de la población que efectivamente se observa. Se usa cuando estudiar
  la población entera es imposible, demasiado caro o destruye lo observado.
- **Individuo** o *unidad estadística*: cada elemento.
- **Censo**: el estudio de **toda** la población. Una encuesta a toda la plantilla de una empresa es
  un censo de esa plantilla, no una muestra.
- **Parámetro**: una medida referida a la **población** —se representa con letras griegas, μ para la
  media y σ para la desviación típica—.
- **Estadístico**: la misma medida referida a la **muestra** —letras latinas, *x̄* y *s*—.

**Muestreo probabilístico**, en el que cada elemento tiene una probabilidad conocida de ser
elegido: **aleatorio simple**, **sistemático** —uno de cada *k*—, **estratificado** —se divide la
población en estratos homogéneos y se muestrea dentro de cada uno— y **por conglomerados** —se
eligen grupos completos—. Sólo el probabilístico permite calcular el error muestral.

**Muestreo no probabilístico**: por **conveniencia**, por **cuotas**, **intencional** o **bola de
nieve**. Es más barato y no permite inferir con garantías.

Y la distinción que separa las dos mitades de la asignatura: **la estadística descriptiva resume lo
observado; la estadística inferencial concluye sobre la población a partir de la muestra.** Este
punto del temario es de la primera.

---

## 2. Variables estadísticas

Una **variable estadística** es la característica que se observa en cada individuo. Sus tipos:

| Tipo | Subtipo | Qué mide | Ejemplos |
|---|---|---|---|
| **Cualitativa** | **Nominal** | Categorías **sin orden** | Sexo, provincia, tipo de contrato |
| **Cualitativa** | **Ordinal** | Categorías **con orden** pero sin distancia medible | Grado de satisfacción, nivel de estudios |
| **Cuantitativa** | **Discreta** | Valores **aislados**, normalmente enteros | Número de hijos, número de programas emitidos |
| **Cuantitativa** | **Continua** | **Cualquier valor** de un intervalo | Peso, tiempo, salario |

La distinción importa porque **determina qué se puede calcular**: de una variable nominal sólo tiene
sentido la moda; de una ordinal, además, la mediana y los cuantiles; y sólo de una cuantitativa
puede calcularse la media, la varianza y la desviación típica. Calcular la media de una variable
nominal codificada con números es el error de principiante más frecuente.

---

## 3. Frecuencias y distribuciones

Para cada valor *xᵢ* de la variable:

- **Frecuencia absoluta** *nᵢ*: cuántas veces aparece. La suma de todas es *N*, el tamaño.
- **Frecuencia relativa** *fᵢ = nᵢ / N*: la proporción. La suma de todas es 1, o 100 si se expresa
  en porcentaje.
- **Frecuencia absoluta acumulada** *Nᵢ*: la suma de las absolutas hasta ese valor, incluido.
- **Frecuencia relativa acumulada** *Fᵢ*: lo mismo con las relativas. Su último valor es 1.

**Las acumuladas sólo tienen sentido si la variable está ordenada**: en una variable nominal no
existen, porque no hay un «hasta aquí».

La **tabla de frecuencias** es la disposición de todos esos datos. Cuando la variable es continua o
tiene demasiados valores distintos, los datos se agrupan en **intervalos de clase**, y entonces
aparecen:

- Los **límites** inferior y superior del intervalo.
- La **marca de clase** *cᵢ*: el punto medio del intervalo, que es el valor con el que se opera y
  que sustituye a todos los datos del intervalo.
- La **amplitud** *aᵢ*: la anchura del intervalo.
- La **densidad de frecuencia** *nᵢ / aᵢ*, necesaria cuando los intervalos tienen amplitudes
  distintas.

Agrupar en intervalos **pierde información**: a partir de la tabla agrupada ya no se puede recuperar
el dato original, y todos los cálculos se hacen sobre las marcas de clase, de modo que dan
aproximaciones y no valores exactos.

---

## 4. Medidas de centralización

| Medida | Qué es | Cuándo se usa | Puntos débiles |
|---|---|---|---|
| **Media aritmética** *x̄* | La suma de los valores dividida por su número | La medida por defecto en variables cuantitativas | **Muy sensible a los valores extremos** |
| **Mediana** *Me* | **El valor central de un conjunto de datos ordenados**: deja el 50 % a cada lado | Cuando hay valores atípicos o la distribución es asimétrica | No usa toda la información |
| **Moda** *Mo* | El valor **que más se repite** | La única aplicable a variables cualitativas | Puede no existir o no ser única |
| **Media geométrica** | La raíz *n*-ésima del producto de los valores | Tasas de variación y crecimientos acumulados | No admite valores nulos ni negativos |
| **Media armónica** | El inverso de la media de los inversos | Promedios de velocidades y de ratios | Muy sensible a valores próximos a cero |

**La mediana es el valor central de los datos ordenados**, y de esa definición salen sus dos reglas
de cálculo: con un número **impar** de datos es el que ocupa la posición central; con un número
**par**, la **media de los dos centrales**. Su virtud es la **robustez**: si al mayor de los datos
se le añade un cero, la media se dispara y la mediana no se mueve.

Las tres primeras no son intercambiables y se confunden a diario:

- **La mediana no es el valor más frecuente**: eso es la moda.
- **La mediana no es el mayor ni el menor**: eso son el máximo y el mínimo, que son medidas de
  posición extrema y no de centralización.
- **La media no siempre es representativa**: en una distribución muy asimétrica —los salarios de una
  empresa con dos directivos muy bien pagados— la media queda por encima de lo que cobra la mayoría
  y la mediana no.

---

## 5. Medidas de posición

Los **cuantiles** dividen la distribución ordenada en partes con el mismo número de datos:

- **Cuartiles** *Q₁, Q₂, Q₃*: la dividen en **cuatro** partes del 25 % cada una.
- **Deciles** *D₁* a *D₉*: en **diez** partes del 10 %.
- **Percentiles** *P₁* a *P₉₉*: en **cien** partes del 1 %.

Las equivalencias que hay que tener presentes: **Q₂ = D₅ = P₅₀ = mediana**, y **Q₁ = P₂₅**,
**Q₃ = P₇₅**.

---

## 6. Medidas de dispersión

Dicen **cuánto se separan los datos** de su centro. Sin ellas, la media no informa: dos
distribuciones con la misma media pueden ser completamente distintas.

| Medida | Fórmula | Unidades |
|---|---|---|
| **Recorrido** o rango | Máximo − mínimo | Las de la variable |
| **Recorrido intercuartílico** | *Q₃ − Q₁* | Las de la variable |
| **Desviación media** | Media de los valores absolutos de las desviaciones respecto de la media | Las de la variable |
| **Varianza** *σ²* | Media de los **cuadrados** de las desviaciones respecto de la media | **Las de la variable, al cuadrado** |
| **Desviación típica** *σ* | **La raíz cuadrada de la varianza** | Las de la variable |
| **Coeficiente de variación** | *σ / x̄* | **Ninguna: es adimensional** |

Tres consecuencias que hay que retener:

- **La varianza no se puede comparar con la media**, porque está en unidades al cuadrado. La
  desviación típica sí, y por eso se usa en la práctica.
- **La varianza nunca es negativa**, y vale cero **sólo si todos los datos son iguales**.
- **El coeficiente de variación es la única medida de dispersión que permite comparar distribuciones
  con distinta unidad o con medias muy distintas**, porque es un cociente sin unidades. Comparar la
  dispersión de los salarios en euros con la de las edades en años sólo se puede hacer con él.

---

## 7. Varianza de la población y cuasivarianza de la muestra

Es la distinción que resuelve la pregunta 12 del examen y la que más confusión genera, porque **hay
dos divisores en circulación**:

| | **Varianza** *σ²* | **Cuasivarianza** o varianza muestral *s²* |
|---|---|---|
| Divisor | *N*, el número de datos | *N − 1* |
| Qué describe | La dispersión **del conjunto observado**, tomado como población | Una **estimación insesgada** de la varianza de la población de la que procede la muestra |
| Cuándo se usa | Cuando los datos son toda la población | Cuando los datos son una **muestra** y se quiere concluir sobre la población |
| Cuál es mayor | La menor de las dos | **La mayor**, y la diferencia crece cuanto menor es *N* |

La razón del *N − 1* tiene nombre —**grados de libertad**— y una explicación intuitiva: al calcular
las desviaciones respecto de **la media muestral**, y no respecto de la media verdadera de la
población, los datos quedan «demasiado cerca» de su centro y la dispersión sale **subestimada**.
Dividir por *N − 1* en lugar de por *N* corrige exactamente ese sesgo.

**Con muestras grandes la diferencia es despreciable; con tres datos, no.** De ahí que en un
ejercicio con pocos datos haya que decidir cuál se pide, y que la respuesta cambie según la
decisión.

**El cálculo de la pregunta 12, paso a paso.** Rendimientos del 10 %, 20 % y −15 %. Trabajando en
tanto por uno —0,10, 0,20 y −0,15—, que es como hay que operar:

1. Media: (0,10 + 0,20 − 0,15) / 3 = 0,05.
2. Desviaciones respecto de la media: 0,05, 0,15 y −0,20.
3. Cuadrados: 0,0025, 0,0225 y 0,04. Suman 0,065.
4. **Con divisor N = 3**: varianza = 0,065 / 3 = 0,02167, es decir 2,17 %; desviación típica =
   √0,02167 = 0,1472, es decir 14,72 %.
5. **Con divisor N − 1 = 2**: cuasivarianza = 0,065 / 2 = 0,0325, es decir 3,25 %; desviación típica
   = √0,0325 = 0,1803, es decir 18,03 %.

Las dos parejas de números están entre las opciones del examen: la opción c) recoge la primera,
redondeada a 2 % y 14 %, y la opción d) la segunda, 3,25 % y 18 %. **La respuesta oficial es la d),
y es la defendible**, por dos razones: es la de la **cuasivarianza**, que es lo que corresponde
cuando tres rendimientos anuales se toman como muestra del comportamiento de una acción; y es la
única de las dos cuyos números **coinciden con el cálculo sin redondear a la baja** —3,25 % es
exacto y 18 % es 18,03 % redondeado, mientras que la opción c) redondea 2,17 % a 2 % y 14,72 % a
14 %, lo que además sería un redondeo incorrecto, porque 14,72 redondea a 15—.

Es, con todo, la pregunta menos limpia del examen en este punto: **el enunciado no dice si los tres
datos son población o muestra**, y de esa omisión depende cuál de las dos parejas es la buena. Quien
la conteste debe fijarse en que **sólo una de las dos opciones está bien redondeada**, que es la
pista que el propio examen deja.

---

## 8. Forma de la distribución

- **Asimetría** o *sesgo*. Una distribución es **simétrica** si media, mediana y moda coinciden;
  tiene **asimetría positiva** o a la derecha si la cola larga está a la derecha, y entonces
  **media > mediana > moda**; y **asimetría negativa** si es al revés. **La distribución de los
  salarios es el ejemplo clásico de asimetría positiva.**
- **Curtosis** o apuntamiento: mide cuánto se concentra la distribución en torno a su centro
  comparada con la normal. **Leptocúrtica** si es más apuntada, **mesocúrtica** si se comporta como
  la normal y **platicúrtica** si es más aplanada.

---

## 9. Representaciones gráficas

Cada gráfico sirve para un tipo de variable, y usarlo con otra es un error, no una elección de
estilo:

| Gráfico | Para qué variable | Qué muestra |
|---|---|---|
| **Diagrama de barras** | Cualitativa o cuantitativa **discreta** | Una barra **separada** por valor, con altura igual a la frecuencia |
| **Diagrama de sectores** o de tarta | Cualitativa, con pocas categorías | El **reparto proporcional** sobre el total |
| **Histograma** | Cuantitativa **continua agrupada** | Rectángulos **contiguos**, cuya **área** —no la altura— es proporcional a la frecuencia |
| **Polígono de frecuencias** | Cuantitativa | La línea que une las marcas de clase |
| **Diagrama acumulativo** u ojiva | Cuantitativa ordenada | Las frecuencias acumuladas |
| **Diagrama de caja y bigotes** | Cuantitativa | Mediana, cuartiles, recorrido y **valores atípicos** |
| **Diagrama de dispersión** | **Dos** variables cuantitativas | La relación entre ambas |
| **Pictograma** | Cualitativa | Frecuencias con símbolos |

**La diferencia entre el diagrama de barras y el histograma no es estética**: en el de barras las
barras van **separadas**, porque la variable toma valores aislados; en el histograma van
**contiguas**, porque los intervalos se tocan. Y en un histograma con intervalos de amplitud
distinta, **lo que representa la frecuencia es el área y no la altura**, de modo que hay que usar la
densidad de frecuencia. Dibujarlo con la altura igual a la frecuencia cuando las amplitudes difieren
**distorsiona el gráfico** y es un error frecuente en informes reales.

---

## 10. Los datos que el examen ha preguntado

| Nº | Qué pregunta | Qué hay que saber | Oficial |
|---|---|---|---|
| 12 | Varianza y desviación típica de tres rendimientos | Distinguir varianza de cuasivarianza y operar en tanto por uno | d) Varianza 3,25 % y desviación típica 18 % ✔ |
| 38 | Qué describe mejor la mediana | Definición de mediana | a) El valor central de un conjunto de datos ordenados ✔ |

**Las dos respuestas oficiales son correctas.**

La **38** es de definición pura, y sus tres distractores son las tres confusiones clásicas del
epígrafe 4: la moda —«el valor que ocurre con mayor frecuencia»—, el máximo y el mínimo. Quien tenga
claras las tres medidas de centralización la contesta sin dudar.

La **12** es la más laboriosa del examen entero y ya se ha desarrollado en el epígrafe 7. Lo que
conviene retener de ella es el método, que sirve para cualquier pregunta parecida: **operar en tanto
por uno**, **calcular la media**, **elevar al cuadrado las desviaciones**, **decidir el divisor** y
**tomar la raíz al final**. Y una advertencia sobre el enunciado: **no dice si los tres datos son
población o muestra**, de modo que dos de sus cuatro opciones responden a lecturas distintas del
mismo cálculo. La oficial es la de la cuasivarianza y es la que hay que marcar.

---

## 11. Trazabilidad

**Este tema no cita ninguna norma, porque su materia no está en ninguna.** Es estadística
descriptiva: sus definiciones y fórmulas se demuestran, no se citan.

Va como desarrollo propio, y así se declara:

- Todas las **definiciones y fórmulas**: población y muestra, tipos de variable, frecuencias,
  medidas de centralización, de posición y de dispersión, asimetría y curtosis.
- La distinción entre **varianza** y **cuasivarianza** y la explicación de los **grados de
  libertad**.
- La **tabla de gráficos** y la regla de que en un histograma la frecuencia la representa el área.
- **Todos los cálculos numéricos**, incluidos los de la pregunta 12, que son aritmética propia y por
  eso van sin negrita, con los pasos escritos para que el lector los repita.
- La observación de que el enunciado de la pregunta 12 **no precisa si los datos son población o
  muestra**. Es una crítica al enunciado, no a la respuesta oficial: **la plantilla es correcta**.

Y el enlace con el resto del proyecto: las **medidas de dispersión** de este punto son las que el
punto 30 pide calcular con las herramientas para análisis de Excel, y las **medidas de posición** son
las que el punto 27 usa al describir el perfil de una audiencia.
