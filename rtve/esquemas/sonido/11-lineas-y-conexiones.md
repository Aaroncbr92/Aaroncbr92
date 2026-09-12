# Esquema · Tema 11 del específico de Sonido · Líneas y conexiones

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalación · `[norma]` =
norma de organismo técnico. **Siglas**: el conector de audio profesional de tres contactos (**XLR**);
la norma de audio digital de dos canales de la Sociedad de Ingeniería de Audio (**AES3**); la categoría
de un cableado de par trenzado (**Cat5** y **Cat6**); la alimentación de micrófono por tensión de pilas
(**A-B**); y **Dante**, que es un nombre comercial y no unas siglas.

**Cabecera.** Enunciado: punto 9 del anexo, «Líneas y conexiones» · **8 preguntas** · **cuatro son de cable y
conector, dos de reparto de señal y dos de panel y matriz.**

<!-- indice -->

## Índice

- [La conexión balanceada y el XLR](#la-conexión-balanceada-y-el-xlr)
- [Las alimentaciones del micrófono](#las-alimentaciones-del-micrófono)
- [El panel de conexiones](#el-panel-de-conexiones)
- [El splitter](#el-splitter)
- [Los cables y sus impedancias](#los-cables-y-sus-impedancias)
- [Las matrices de conmutación](#las-matrices-de-conmutación)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La conexión balanceada y el XLR

- **PREGUNTA 48** · `[of]` · **En un XLR, el vivo va al pin 2.**
- **EL REPARTO COMPLETO**: **pin 1, masa; pin 2, vivo o fase positiva; pin 3, retorno o fase
  negativa.** **La regla mnemotécnica es «1 tierra, 2 vivo, 3 frío».**
- **POR QUÉ SE EQUILIBRA**: **la interferencia entra igual en los dos conductores y la entrada
  diferencial resta**, de modo que el ruido se cancela y la señal no.

## Las alimentaciones del micrófono

- **PREGUNTA 49** · `[of]` · **La tensión de la alimentación A-B es de 12 voltios.**
- **LAS DOS, UNA FRENTE A OTRA**: **la fantasma son 48 voltios entre los dos vivos y la masa; la A-B
  son 12 voltios entre los dos vivos.**
- **AVISO**: **no son intercambiables.** **Meter A-B a un micrófono de condensador de fantasma puede
  estropearlo.**

## El panel de conexiones

- **PREGUNTA 18** · `[of]` · **El diseño que no corta la salida al insertar un latiguillo es el
  seminormalizado.**
- **LOS TRES DISEÑOS**: **normalizado** —insertar corta el camino directo—, **seminormalizado**
  —insertar en la fila de abajo corta, en la de arriba no— **y sin normalizar** —nunca hay camino
  directo.
- **PARA QUÉ SIRVE LA DIFERENCIA**: **para poder escuchar una señal sin quitarla del sitio donde está
  trabajando**, que en directo es la diferencia entre comprobar y cortar.

## El splitter

- **PREGUNTA 32** · `[of]` · **El dispositivo que reparte un micrófono a varias salidas idénticas con
  el mismo nivel es el splitter de audio.**
- **PREGUNTA 42** · `[of]` · **Con dos mesas alimentadas por splitters pasivos y sin transformador de
  aislamiento, cada mesa tiene su propio nivel de ganancia.**
- **LO QUE ESO SIGNIFICA EN LA PRÁCTICA**: **la ganancia es de cada mesa, pero la alimentación fantasma
  es común**: **si una mesa la quita, el micrófono se queda sin alimentar para todas.**
- **PARA QUÉ SE USA**: **para que la mesa de sala, la de monitores y la de emisión compartan los mismos
  micrófonos sin estorbarse.**

## Los cables y sus impedancias

| Cable | Impedancia o límite | Para qué |
|---|---|---|
| **XLR de audio analógico** | **Baja impedancia** | **Micrófono y línea** |
| **XLR para AES3** | **110 ohmios** | **Audio digital de dos canales** |
| **Coaxial para AES3 en versión no equilibrada** | **75 ohmios** | **Tirada larga** |
| **Cat5** | **100 metros** | **Redes de audio** |
| **Cat6** | **100 metros y más ancho de banda** | **Dante y redes de audio** |

- **PREGUNTA 57** · `[norma]` · **Los cables XLR para AES3 deben tener 110 ohmios de impedancia.**
- **PREGUNTA 51** · `[of]` · **La longitud máxima recomendada de un cable de categoría 5 es de 100
  metros.**
- **PREGUNTA 25** · `[of]` · **De los enumerados, el que sirve para Dante es el Cat6.**
- **EL ERROR CLÁSICO**: **usar un cable de micrófono para AES3.** **Funciona en tiradas cortas y falla
  en las largas**, porque su impedancia no es la debida y aparecen reflexiones.

## Las matrices de conmutación

- **QUÉ HACEN**: **encaminan una entrada a una o a varias salidas.** **No mezclan.**
- **DÓNDE ESTÁN**: **en el control central**, y son el punto donde una instalación se reconfigura sin
  tocar un cable.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 18 | Diseño de panel que no corta la salida | b) Seminormalizado ✔ |
| 25 | Cable que sirve para Dante | b) Cat6 ✔ |
| 32 | Dispositivo que reparte un micrófono a varias salidas | a) Splitter de audio ✔ |
| 42 | Qué controla la ganancia con splitters pasivos | a) Cada mesa tiene su propio nivel ✔ |
| 48 | A qué pin del XLR va el vivo | b) 2 ✔ |
| 49 | Tensión de la alimentación A-B | a) 12 V ✔ |
| 51 | Longitud máxima de un cable de categoría 5 | a) 100 metros ✔ |
| 57 | Impedancia de un XLR para AES3 | c) 110 ohmios ✔ |

**Las ocho oficiales son correctas** y **ninguna descansa sólo en la plantilla.** · **Aviso de
estudio**: **el cuadro de cables e impedancias contesta tres preguntas de las ocho** y **es lo que un
técnico consulta en la instalación todos los días.**
