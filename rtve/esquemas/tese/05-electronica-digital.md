# Esquema · Tema 5 del específico de Técnica de Equipos y Sistemas Electrónicos · Electrónica digital

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio y electrónica digital ·
`[plan]` = plantilla oficial. **Siglas**: las siete puertas lógicas, que el oficio nombra por su
palabra inglesa (**AND** es «y», **OR** es «o», **NOT** es «no», **NAND** y **NOR** son las dos
anteriores negadas, y **XOR** y **XNOR** son la «o exclusiva» y su negada); y el conversor de analógico
a digital (**A/D**).

**Cabecera.** Enunciado: punto 5 del anexo · **6 preguntas** · **tres dependen de una figura y tres se
razonan.**

<!-- indice -->

## Índice

- [Los sistemas de numeración](#los-sistemas-de-numeración)
- [Las puertas lógicas](#las-puertas-lógicas)
- [La conversión analógico-digital](#la-conversión-analógico-digital)
- [Los esquemas y las expresiones lógicas](#los-esquemas-y-las-expresiones-lógicas)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los sistemas de numeración

- **LA CONVERSIÓN BINARIO A HEXADECIMAL SE HACE DE CUATRO EN CUATRO BITS**, empezando por la derecha.
  **Cada grupo de cuatro es un dígito hexadecimal.**
- **PREGUNTA 12** · `[of]` · **El binario 110100101 en hexadecimal es 1A5.**
- **LA CUENTA, PASO A PASO**: **110100101 se agrupa desde la derecha en 0101, 0010 y 1**, es decir
  **1 · 1010 · 0101**, y **1 es 1, 1010 es A y 0101 es 5.** **De ahí 1A5.**
- **LA TABLA QUE HAY QUE SABERSE**: **1010 = A · 1011 = B · 1100 = C · 1101 = D · 1110 = E · 1111 =
  F.** **Con esas seis y las diez cifras, la conversión es mecánica.**

## Las puertas lógicas

| Puerta | Sale 1 cuando |
|---|---|
| **AND** | **Todas las entradas son 1** |
| **OR** | **Alguna entrada es 1** |
| **NOT** | **La entrada es 0** |
| **NAND** | **NO todas son 1** |
| **NOR** | **Ninguna es 1** |
| **XOR** | **Un número impar de entradas es 1; con dos, exactamente una** ✔ |
| **XNOR** | **Las entradas son iguales** |

- **PREGUNTA 56** · `[of]` · **Una compuerta XOR genera salida verdadera sólo cuando uno y sólo uno de
  sus argumentos lo es.**
- **PREGUNTA 50** · `[plan]` · **La tabla de verdad de la figura corresponde a una XNOR.**
- **PREGUNTA 82** · `[plan]` · **El circuito de puertas de la figura equivale a una NOR exclusiva.**
- **ESTE ESQUEMA NO HA VISTO NINGUNA DE LAS DOS FIGURAS.** **La regla de la familia**: **XOR y XNOR son
  la una la negación de la otra.** **XOR dice «son distintas»; XNOR dice «son iguales».** **Toda tabla
  de verdad de dos entradas y una salida es una de las siete puertas del cuadro**, y **se identifica
  mirando cuántos unos hay en la columna de salida y dónde están.**

## La conversión analógico-digital

- **PREGUNTA 57** · `[of]` · **El aliasing se produce al muestrear a menos del doble de la frecuencia
  máxima de la señal.**
- **EL TEOREMA QUE HAY DETRÁS**: **hay que muestrear a más del doble de la frecuencia más alta
  presente.** **Por debajo, las frecuencias altas aparecen disfrazadas de bajas y ya no se pueden
  separar.**
- **CÓMO SE EVITA EN LA PRÁCTICA**: **con un filtro pasabajo antes del conversor**, que corta lo que
  el muestreo no va a poder representar. **No basta con muestrear rápido: hay que filtrar antes.**
- **LA CIFRA DE REFERENCIA EN AUDIO**: **48.000 muestras por segundo para 20.000 hercios de banda**,
  con margen para el filtro.

## Los esquemas y las expresiones lógicas

- **PREGUNTA 21 del segundo llamamiento** · `[plan]` · **La dirección de la imagen corresponde al
  decimal 300.**
- **LA REGLA DE LA FAMILIA**: **un binario se pasa a decimal sumando las potencias de dos de las
  posiciones que llevan uno.** **300 son 100101100 en binario y 12C en hexadecimal.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 12 | El binario 110100101 en hexadecimal | d) 1A5 ✔ |
| 50 | A qué puerta corresponde la tabla de verdad | d) XNOR ✔ **·** sólo con la plantilla |
| 56 | Qué salida genera una compuerta XOR | a) Verdadero sólo cuando uno y sólo uno lo es ✔ |
| 57 | Cuándo se produce el aliasing | c) Al muestrear a menos del doble de la frecuencia máxima ✔ |
| 82 | A qué equivale el circuito de puertas | a) Una NOR exclusiva ✔ **·** sólo con la plantilla |
| 21 (2.º llam.) | A qué decimal corresponde la dirección de la imagen | d) 300 ✔ **·** sólo con la plantilla |

**Las seis oficiales son correctas** · **tres descansan sólo en la plantilla.** · **Aviso de estudio**:
**la tabla de las siete puertas y la conversión de cuatro en cuatro bits son las dos destrezas del
punto.** **Las dos se practican en un papel en diez minutos y valen para cinco de las seis
preguntas.**
