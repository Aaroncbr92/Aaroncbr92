# Esquema · Gestión 28: matemática financiera

Esqueleto para repasar. Todo desarrollado y verificado en el tema.

<!-- indice -->

## Índice

- [Vocabulario](#vocabulario)
- [Simple y compuesta](#simple-y-compuesta)
- [Tantos equivalentes](#tantos-equivalentes)
- [Descuento](#descuento)
- [Descuento de efectos](#descuento-de-efectos)
- [Rentas](#rentas)
- [Amortización de préstamos](#amortización-de-préstamos)
- [Empréstitos](#empréstitos)
- [Selección de inversiones](#selección-de-inversiones)
- [El aviso](#el-aviso)

<!-- /indice -->

## Vocabulario

*C₀* capital inicial · *Cₙ* montante · *I = Cₙ − C₀* interés · *i* tanto, **en tanto por uno** ·
*r = I / C₀* rédito · *n* tiempo, **en la misma unidad que el tipo**.
**Capitalizar** = hacia el futuro. **Descontar** = hacia el presente.

## Simple y compuesta

| | **Simple** | **Compuesta** |
|---|---|---|
| Intereses | sobre el capital inicial, **no se acumulan** | **se acumulan** y generan intereses |
| Crecimiento | lineal | exponencial |
| Uso | corto plazo | largo plazo |

- Simple: *I = C₀ · i · n* · *Cₙ = C₀ · (1 + i · n)*
- Compuesta: *Cₙ = C₀ · (1 + i)ⁿ* · *n = log(Cₙ/C₀) / log(1+i)* · *i = (Cₙ/C₀)^(1/n) − 1*

Para *n = 1* dan lo mismo; para *n < 1* gana la simple; para *n > 1*, la compuesta.

## Tantos equivalentes

- **Simple: proporcionales.** 6 % anual → 1,5 % trimestral. El rédito trimestral es 0,06/4 = 0,015.
- **Compuesta: NO proporcionales.** *i₍ₖ₎ = (1 + i)^(1/k) − 1*. 6 % anual → 1,4674 % trimestral.

**TAE**: coste o rendimiento efectivo anual en régimen compuesto, con comisiones. Dos productos
sólo se comparan por su TAE.

## Descuento

| | **Comercial** | **Racional** |
|---|---|---|
| Se calcula sobre | el **nominal** | el **efectivo** |
| Fórmula | *Dc = N · i · n* | *Dr = N · i · n / (1 + i · n)* |
| Cuál es mayor | **el comercial** | — |

Efectivo: *E = N − Dc = N · (1 − i · n)*.
*El comercial es el que usa la banca, y es más caro porque cobra interés sobre una cantidad mayor
que la que entrega.*

## Descuento de efectos

El banco deduce **descuento + comisión + gastos**.
**Descuento bancario = (N · i · n) + comisión.**
**Salvo buen fin**: el riesgo no se transmite. Cuentas (4311) y **(5208)**.

## Rentas

Por cuantía: **constantes · variables** (progresión aritmética o geométrica).
Por vencimiento: **pospagables · prepagables** (= pospagable × (1 + i)).
Por duración: **temporales · perpetuas**.
Por valoración: **inmediatas · diferidas · anticipadas**.
Por periodo: **enteras · fraccionadas**.

**Las fraccionadas se resuelven convirtiendo el tanto con la equivalencia compuesta, nunca
dividiéndolo.**

*a = (1 − (1 + i)^(−n)) / i* · *s = ((1 + i)ⁿ − 1) / i* · perpetua: *a = c / i*.

## Amortización de préstamos

**Cuota = intereses del periodo + cuota de amortización**, con los intereses sobre el **capital
vivo**.

| Sistema | Cuota | Intereses | Amortización |
|---|---|---|---|
| **Francés** | constante | decrecientes | crecientes |
| **Italiano** | decreciente | decrecientes | constante |
| **Americano** | sólo intereses; capital al final | constantes | cero hasta el final |
| **Alemán** | intereses anticipados | — | constante |
| **Con carencia** | sólo intereses, o nada | — | empieza después |

*El francés es el de las hipotecas: al principio casi toda la cuota son intereses.*

## Empréstitos

Préstamo **dividido en títulos**. Emisor · obligacionista · nominal · valor de **emisión** (a la
par, bajo la par con prima, sobre la par) · valor de **reembolso** · **cupón** · cupón cero ·
**amortización por sorteo**.
*En el préstamo el capital vivo es un importe; en el empréstito, un número de títulos.*

## Selección de inversiones

**VAN = −A + Σ Qₜ / (1 + k)ᵗ.** Se acepta si es **positivo**.
*Es restar el coste inicial al valor presente de los flujos: ésa es la pregunta 48.*
**TIR**: la tasa que hace VAN = 0. Se acepta si supera al coste de capital. Puede no existir, ser
múltiple y **ordenar mal** proyectos de tamaños distintos.
***Payback***: ignora lo que ocurre después y, en su versión simple, no descuenta.

## El aviso

**Las 4 respuestas oficiales son correctas.** El error que el examen castiga es **no convertir la
unidad**: 80 semestres son 40 años, y 80 estaba entre las opciones.