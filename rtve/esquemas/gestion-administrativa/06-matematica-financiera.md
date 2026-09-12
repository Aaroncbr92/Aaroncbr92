# Esquema · Gestión Administrativa 6: matemática financiera

Esqueleto para repasar. Todo desarrollado y comprobado con la cuenta hecha en el tema.

<!-- indice -->

## Índice

- [Capitalización simple](#capitalización-simple)
- [Capitalización compuesta](#capitalización-compuesta)
- [Rentas](#rentas)
- [Amortización de préstamos](#amortización-de-préstamos)
- [Simples y compuestas](#simples-y-compuestas)
- [El aviso](#el-aviso)

<!-- /indice -->

## Capitalización simple

Los intereses **no** se acumulan.

- **I = C₀ · i · n**
- **Cₙ = C₀ · (1 + i · n)**
- **C₀ = Cₙ / (1 + i · n)**

- **Tipo y tiempo, en la misma unidad.** 6 % anual, 3 meses → i = 0,06 · 3/12 = 0,015.
- **Capital final ≠ intereses.** El final incluye el inicial.

| 5.000 € · 6 % · 3 años | I = 900 → **C = 5.900 €** |
| Montante 3.600, 20 %, 10 años | **C₀ = 1.200 €** |
| 2.400 € · 10 % · 10 años | I = 2.400 → **C = 4.800 €** |

**Trampa del tercero**: al 10 % durante 10 años los intereses **igualan al capital**. Quien se para
en los intereses obtiene 2.400 y lo encuentra entre las opciones.

## Capitalización compuesta

Los intereses **sí** se acumulan y generan intereses.

- **Cₙ = C₀ · (1 + i)ⁿ** · **C₀ = Cₙ / (1 + i)ⁿ** · **I = C₀ · [(1 + i)ⁿ − 1]**
- 100 € · 10 % · 3 años → 100 · 1,331 = **133,10 €**. En simple serían 130 €.
- **Cómo se reconoce**: «se van acumulando», «se capitalizan», «compuesto», «se reinvierten».

## Rentas

- **Constante**: términos **iguales** a intervalos **iguales**. Las dos cosas.
- **Variable**: términos distintos; en progresión **aritmética** o **geométrica**.
- **Entera / fraccionada**: según venza una o varias veces por periodo de capitalización.
- **Pospagable / prepagable** · **temporal / perpetua** · **inmediata / diferida / anticipada**.
- **Ojo al vocabulario**: «renta variable» de la inversión (acciones) **no es** la renta variable
  actuarial (términos desiguales).

## Amortización de préstamos

Amortizar = **devolver el capital**, no aumentar deuda ni pagar sólo intereses.
Cada pago = **cuota de interés** (sobre el capital vivo) + **cuota de amortización** (reduce
capital). Suma = **término amortizativo**.

| **Francés** | cuota total constante; interés decrece, amortización crece |
| **Cuota de amortización constante** | amortiza **C₀ / n** cada periodo; interés y cuota total decrecen |
| **Americano** | sólo intereses durante la vida; **el capital, íntegro al final** |

- 10.000 € en 5 años, amortización constante → **2.000 € cada año**, incluido el segundo. El tipo
  **no interviene** en esa cifra: interviene en la cuota de interés (año 2: 10 % de 8.000 = 800 €).
- **Cuadro**: término · interés · amortización · total amortizado · capital vivo. Cierra cuando el
  total amortizado iguala el capital y el vivo queda en cero.

## Simples y compuestas

- **Simples**: capitalización simple · descuento simple · descuento comercial.
- **Compuestas**: capitalización compuesta · **constitución de capitales** · amortización de
  préstamos.
- **Descuento**: comercial sobre el **nominal**; racional sobre el **efectivo**. El comercial es
  siempre mayor.

## El aviso

- **Pregunta 37 — errata de plantilla, refutada con una multiplicación.** 2.400 € al 10 % simple
  durante 10 años dan **4.800 €**, opción d). La plantilla da 2.400 €, que es el capital de partida.
  Y el error es creíble porque a ese tipo y ese plazo **los intereses valen lo mismo que el
  capital**.
