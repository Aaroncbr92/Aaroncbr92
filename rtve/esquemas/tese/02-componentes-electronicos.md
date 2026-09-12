# Esquema · Tema 2 del específico de Técnica de Equipos y Sistemas Electrónicos · Componentes electrónicos

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio y electrónica de componentes ·
`[plan]` = plantilla oficial. **Siglas**: el transistor bipolar de unión con dopado negativo-positivo-
negativo (**NPN**) y su complementario (**PNP**); la ganancia de corriente del transistor (**β**); el
microfaradio (**µF**) y el miliamperio (**mA**); el decibelio (**dB**); y los circuitos formados por
resistencia y condensador (**RC**) o por bobina y condensador (**LC**).

**Cabecera.** Enunciado: punto 2 del anexo · **12 preguntas: el segundo banco de la ocupación** ·
**siete de las doce dependen de un esquema, y este esquema no ha visto ninguno.**

<!-- indice -->

## Índice

- [El código de colores de las resistencias](#el-código-de-colores-de-las-resistencias)
- [El condensador](#el-condensador)
- [La carga del condensador](#la-carga-del-condensador)
- [El diodo y el transistor](#el-diodo-y-el-transistor)
- [El potenciómetro y los filtros pasivos](#el-potenciómetro-y-los-filtros-pasivos)
- [Las preguntas con esquema](#las-preguntas-con-esquema)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El código de colores de las resistencias

| Color | Cifra | Multiplicador |
|---|---|---|
| **Negro** | **0** | **×1** |
| **Marrón** | **1** | **×10** |
| **Rojo** | **2** | **×100** ✔ |
| **Naranja** | **3** | **×1.000** |
| **Amarillo** | **4** | **×10.000** |
| **Verde** | **5** | **×100.000** |
| **Azul** | **6** | **×1.000.000** |
| **Violeta** | **7** | **×10.000.000** |
| **Gris** | **8** | — |
| **Blanco** | **9** | — |
| **Dorado** | — | **Tolerancia del 5 %** |

- **PREGUNTA 74** · `[of]` · **El rojo multiplica por 100.**
- **PREGUNTA 18 del segundo llamamiento** · `[of]` · **Marrón, rojo, negro y dorado son 12 ohmios con
  tolerancia del 5 %.** **Marrón 1, rojo 2, negro ×1.**
- **PREGUNTA 61** · `[of]` · **Con una resistencia naranja, negro, rojo, la corriente es de 4 mA.**
  **Naranja 3, negro 0, rojo ×100: son 3.000 ohmios.**
- **LA REGLA MNEMOTÉCNICA**: **el orden de los colores es el del arcoíris con negro y marrón delante y
  gris y blanco detrás.**

## El condensador

- **LA FÓRMULA**: **C = Q / V.** **Capacidad es carga partido por tensión.**
- **PREGUNTA 21** · `[of]` · **0,002 culombios a 10 voltios son 200 microfaradios.** **0,002 ÷ 10 =
  0,0002 faradios = 200 µF.**
- **EN SERIE Y EN PARALELO VA AL REVÉS QUE LA RESISTENCIA**: **en paralelo se suman las capacidades; en
  serie, las inversas.**

## La carga del condensador

- **LA CONSTANTE DE TIEMPO**: **τ = R × C.** **En una constante de tiempo el condensador alcanza el
  63 % de la tensión final; en cinco, se da por cargado.**
- **PREGUNTA 70** · `[plan]` · **La tensión del condensador al cabo de 1 segundo es de 5 V.** **Depende
  del circuito de la figura**, que este esquema no ha visto.

## El diodo y el transistor

- **EL DIODO**: **conduce en un sentido y no en el otro.** **Su caída directa típica en silicio es de
  unos 0,7 voltios.**
- **PREGUNTA 26** · `[plan]` · **El símbolo del diodo túnel es el de la opción c.** **Depende de la
  figura.**
- **PREGUNTA 34** · `[plan]` · **El símbolo del transistor NPN es el de la opción b.** **Depende de la
  figura.**
- **CÓMO SE DISTINGUEN LOS DOS SÍMBOLOS DE TRANSISTOR BIPOLAR**: **por la flecha del emisor.** **En el
  NPN sale hacia fuera; en el PNP entra.**
- **PREGUNTA 76** · `[of]` · **En región activa, la corriente de colector es la de base multiplicada
  por β.**
- **LAS TRES REGIONES**: **corte** —no conduce—, **activa** —amplifica— **y saturación** —conduce todo
  lo que puede.

## El potenciómetro y los filtros pasivos

- **PREGUNTA 22 del segundo llamamiento** · `[of]` · **El componente que filtra frecuencias no
  deseadas es un filtro pasivo RC o LC.**
- **PASIVO ES EL QUE NO NECESITA ALIMENTACIÓN**: **resistencias, condensadores y bobinas.** **No puede
  dar ganancia; sólo puede quitar.**

## Las preguntas con esquema

- **PREGUNTA 44** · `[plan]` · **La capacidad equivalente de la combinación es 5 µF.**
- **PREGUNTA 60** · `[plan]` · **Los valores del voltímetro son mínimo 4 V y máximo 8 V.**
- **PREGUNTA 87** · `[plan]` · **La ganancia del amplificador es de 20 dB.**
- **LA REGLA DE LA FAMILIA PARA LA ÚLTIMA, QUE SÍ SE PUEDE LLEVAR**: **la ganancia en decibelios de
  tensión son 20 por el logaritmo del cociente de salida entre entrada.** **20 dB son diez veces.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 21 | Capacitancia de 0,002 C a 10 V | b) 200 µF ✔ |
| 26 | Símbolo del diodo túnel | c) ✔ **·** sólo con la plantilla |
| 34 | Símbolo del transistor NPN | b) ✔ **·** sólo con la plantilla |
| 44 | Capacidad equivalente de la combinación | b) 5 µF ✔ **·** sólo con la plantilla |
| 60 | Valores máximo y mínimo del voltímetro | a) Mínimo 4 V, máximo 8 V ✔ **·** sólo con la plantilla |
| 61 | Corriente por una resistencia naranja, negro, rojo | a) 4 mA ✔ |
| 70 | Tensión del condensador al cabo de 1 segundo | b) 5 V ✔ **·** sólo con la plantilla |
| 74 | Por cuánto multiplica el color rojo | c) 100 ✔ |
| 76 | Corriente de colector en región activa | c) La de base por β ✔ |
| 87 | Ganancia en decibelios del amplificador | d) 20 dB ✔ **·** sólo con la plantilla |
| 18 (2.º llam.) | Valor de una resistencia marrón, rojo, negro, dorado | c) 12 ohmios ✔ |
| 22 (2.º llam.) | Componente que filtra frecuencias no deseadas | a) Filtro pasivo RC o LC ✔ |

**Las doce oficiales son correctas** · **seis descansan sólo en la plantilla.** · **Aviso de estudio**:
**el código de colores contesta tres preguntas y es lo más barato de memorizar del volumen.** **Vale
la pena aprenderlo el primer día.**
