# Esquema · Gestión Administrativa 7: probabilidad y estadística

Esqueleto para repasar. Todos los cálculos rehechos en el tema.

<!-- indice -->

## Índice

- [Población y muestra](#población-y-muestra)
- [Variables](#variables)
- [Centralización](#centralización)
- [Dispersión](#dispersión)
- [Probabilidad](#probabilidad)
- [Sin avisos](#sin-avisos)

<!-- /indice -->

## Población y muestra

- **Población** (todo) · **muestra** (parte observada) · **unidad estadística** (cada elemento) ·
  **censo** frente a **muestreo**.
- **Muestra aleatoria**: **todos los elementos tienen la misma probabilidad de entrar**. Sólo así se
  puede calcular el error de muestreo.
- **No aleatorios**: conveniencia · criterio o intencional · **cuotas**.

## Variables

| **Cualitativa nominal** | categorías sin orden | sexo, provincia |
| **Cualitativa ordinal** | categorías con orden | nivel de estudios |
| **Cuantitativa discreta** | valores aislados; **entre dos consecutivos no cabe otro** | nº de hijos |
| **Cuantitativa continua** | cualquier valor de un intervalo | temperatura, tiempo, longitud |

- **La prueba**: entre dos valores posibles, ¿cabe otro? Entre 2 y 3 hijos, no. Entre 20 y 21 grados,
  infinitos.
- **Falso**: que una cualitativa tome cualquier valor numérico; que una discreta tome cualquier valor
  de un intervalo.

## Centralización

- **Media**: usa todos los datos; **sensible a los extremos**.
- **Mediana**: valor central **con los datos ordenados**; si son pares, **media de los dos
  centrales**. Insensible a los extremos.
- **Moda**: la que **más se repite**. Puede no ser única y puede no existir.
- **Sólo esas tres** son de tendencia central. Rango, varianza y desviación típica **no lo son**.

**Las cuentas del examen:**

| 20, 40, 50, 60 | (40+50)/2 = **45** |
| 5,5,7,9,11,12,15,18 | (9+11)/2 = **10** |
| 1,5,2,8,9,4,7,7,5,7 → ordenar → 1,2,4,5,**5**,**7**,7,7,8,9 | (5+7)/2 = **6** |
| 6,4,4,4,6,10,10,8,5,6,6,8,5 | el 4 sale 3 veces, el **6 sale 4** → moda **6** |

- **Cuantiles**: cuartiles (Q₁ 25 %, Q₂ mediana, Q₃ 75 %) · deciles · percentiles.

## Dispersión

- **Rango** = máximo − mínimo. 5, 8, 12, 20 → **15**.
- **Intercuartílico** = Q₃ − Q₁, robusto.
- **Varianza**: media de los cuadrados de las desviaciones; unidades **al cuadrado**.
- **Desviación típica** = **raíz de la varianza**; vuelve a las unidades de la variable.
- **Coeficiente de variación** = σ / x̄; **adimensional**, sirve para comparar unidades distintas.

## Probabilidad

- **Experimento aleatorio · espacio muestral · suceso · seguro (todo el espacio) · imposible
  (vacío)**.
- **Toda probabilidad está entre 0 y 1**. Seguro = **1**. Imposible = **0**. Nunca negativa ni mayor
  que 1.
- **Laplace**: favorables / posibles.
- **Contrario**: P(Ā) = 1 − P(A).
- **Unión**: P(A∪B) = P(A) + P(B) − P(A∩B); si son **incompatibles**, se suman.
- **Intersección**: si son **independientes**, se multiplican.
- **Condicionada**: P(A|B) = P(A∩B) / P(B).
- **Incompatible ≠ independiente**: dos incompatibles con probabilidad positiva **son
  dependientes**.

## Sin avisos

**Es el único punto de la ocupación sin ninguna incidencia**: las once respuestas oficiales son
correctas.
