# Esquema · Gestión 29: estadística descriptiva básica

Esqueleto para repasar. Todo desarrollado y verificado en el tema.

<!-- indice -->

## Índice

- [Población y muestra](#población-y-muestra)
- [Variables](#variables)
- [Frecuencias](#frecuencias)
- [Centralización](#centralización)
- [Posición](#posición)
- [Dispersión](#dispersión)
- [Varianza y cuasivarianza](#varianza-y-cuasivarianza)
- [Forma](#forma)
- [Gráficos](#gráficos)
- [El aviso](#el-aviso)

<!-- /indice -->

## Población y muestra

**Población** = el conjunto completo · **muestra** = el subconjunto observado · **censo** = estudiar
toda la población.
**Parámetro** (población, letras griegas: μ, σ) frente a **estadístico** (muestra: *x̄*, *s*).
Muestreo **probabilístico** —aleatorio simple, sistemático, estratificado, por conglomerados— y **no
probabilístico** —conveniencia, cuotas, intencional, bola de nieve—. Sólo el primero permite
calcular el error muestral.
**Descriptiva** resume lo observado; **inferencial** concluye sobre la población.

## Variables

**Cualitativa nominal** (sin orden) · **cualitativa ordinal** (con orden) · **cuantitativa
discreta** · **cuantitativa continua**.
*Determina qué se puede calcular: de una nominal, sólo la moda; de una ordinal, además mediana y
cuantiles; la media y la varianza, sólo de una cuantitativa.*

## Frecuencias

*nᵢ* absoluta · *fᵢ* relativa · *Nᵢ* y *Fᵢ* acumuladas —**sólo si la variable está ordenada**—.
Agrupar en intervalos: **límites**, **marca de clase**, **amplitud**, **densidad de frecuencia**.
*Agrupar pierde información: los cálculos se hacen sobre marcas de clase.*

## Centralización

- **Media**: sensible a los extremos.
- **Mediana**: **el valor central de los datos ordenados**. Con *n* par, media de los dos
  centrales. **Robusta**.
- **Moda**: el valor que **más se repite**. La única aplicable a variables cualitativas.
- **Geométrica** (tasas de variación) · **armónica** (velocidades y ratios).

*La mediana no es la moda, ni el máximo, ni el mínimo.*

## Posición

**Cuartiles · deciles · percentiles.**
**Q₂ = D₅ = P₅₀ = mediana** · **Q₁ = P₂₅** · **Q₃ = P₇₅**.

## Dispersión

Recorrido · recorrido intercuartílico · desviación media · **varianza** (unidades al cuadrado) ·
**desviación típica** (raíz de la varianza) · **coeficiente de variación** = σ/x̄, **adimensional**.

*La varianza nunca es negativa y vale cero sólo si todos los datos son iguales. El coeficiente de
variación es el único que permite comparar distribuciones con distinta unidad.*

## Varianza y cuasivarianza

| | **Varianza** *σ²* | **Cuasivarianza** *s²* |
|---|---|---|
| Divisor | **N** | **N − 1** |
| Describe | el conjunto como población | estimación insesgada de la población |
| Tamaño | menor | **mayor** |

*El N−1 son los **grados de libertad**: las desviaciones se toman respecto de la media muestral, no
de la verdadera, y la dispersión sale subestimada.*

**El cálculo de la pregunta 12** (10 %, 20 %, −15 %, en tanto por uno):
media 0,05 → desviaciones 0,05, 0,15, −0,20 → cuadrados 0,0025 + 0,0225 + 0,04 = 0,065.
Con N: 0,065/3 = 2,17 % y σ = 14,72 %. Con N−1: 0,065/2 = **3,25 %** y σ = **18,03 %**.
*La oficial es la de la cuasivarianza, y además es la única bien redondeada.*

## Forma

**Asimetría**: simétrica (media = mediana = moda) · **positiva** (cola a la derecha, media >
mediana > moda; el ejemplo son los salarios) · negativa.
**Curtosis**: leptocúrtica · mesocúrtica · platicúrtica.

## Gráficos

**Barras** (cualitativa o discreta, **separadas**) · **sectores** · **histograma** (continua
agrupada, **contiguas**, y **la frecuencia la representa el área**) · polígono de frecuencias ·
ojiva · **caja y bigotes** (mediana, cuartiles y atípicos) · dispersión (dos variables) ·
pictograma.

## El aviso

**Las 2 respuestas oficiales son correctas.** El enunciado de la 12 **no dice si los datos son
población o muestra**, y de eso depende cuál de sus opciones es la buena.