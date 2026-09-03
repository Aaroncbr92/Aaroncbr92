# Esquema · Tema 6 del específico de Edición, Montaje y Procesos Audiovisuales · Equipos de medida y control

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio, sin norma detrás.

**Cabecera.** Enunciado: «3. Equipos de Medida y control · 3.1. De la señal de vídeo · 3.2. De la
señal de audio · 3.3. Matrices de conmutación y conectividad» · **3 preguntas** · **DOS DE LAS TRES
SON LA MISMA PREGUNTA** (la 57 y la 61) · **ninguna descansa sólo en la plantilla**.

<!-- indice -->

## Índice

- [Por qué se mide](#por-qué-se-mide)
- [Los instrumentos de vídeo](#los-instrumentos-de-vídeo)
- [Los instrumentos de audio](#los-instrumentos-de-audio)
- [El 0 dBFS](#el-0-dbfs)
- [La cadencia y la reproducción](#la-cadencia-y-la-reproducción)
- [Las matrices](#las-matrices)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Por qué se mide

- **UN MONITOR Y UN ALTAVOZ NO SIRVEN PARA DECIDIR SI UNA SEÑAL ES CORRECTA**: cada monitor tiene su
  brillo, cada sala su acústica, cada oído su costumbre. **Lo que sirve es un instrumento.**
- **LAS TRES COSAS QUE GARANTIZA LA MEDIDA**: **estar dentro de los límites de emisión** · **que el
  material sea homogéneo** · **que el defecto se pueda LOCALIZAR** —el ojo sólo dice que algo se ve
  raro—.

## Los instrumentos de vídeo

| Instrumento | Qué mide |
|---|---|
| **Monitor de forma de onda** | **La LUMINANCIA**, línea a línea |
| **Vectorscopio** | **La CROMINANCIA**: tono y saturación |
| **Monitor de referencia** | Lo que se ve, **calibrado** |
| **Histograma** | El reparto estadístico de niveles |
| **Analizador de errores** | La integridad de la señal digital |

- **LAS DOS REFERENCIAS**: **la señal de BARRAS**, con la que se ajusta la cadena, y **la escala IRE**,
  con el negro en 0 y el blanco de referencia en 100.
- **LA REGLA DE OFICIO**: **la forma de onda dice si la EXPOSICIÓN está bien; el vectorscopio dice si
  el COLOR está bien.** **Son dos preguntas distintas y hacen falta los dos.**

## Los instrumentos de audio

| Instrumento | Qué mide |
|---|---|
| **Medidor de pico** | **El valor instantáneo más alto** |
| **Medidor VU** | **Un valor promediado** |
| **Medidor de sonoridad** | **La sonoridad integrada**, en LUFS (recomendación R 128 de la UER) |
| **Fasímetro** | **La fase entre canales**: avisa de que un estéreo se anula en mono |
| **Analizador de espectro** | El reparto de energía por frecuencias |

- **LA DISTINCIÓN**: **el PICO dice si algo va a DISTORSIONAR; la SONORIDAD dice si algo SUENA FUERTE
  O FLOJO.** **No son lo mismo**: una señal muy comprimida puede tener el mismo pico y sonar mucho más
  alta.
- **DE AHÍ LA NORMA DE EMISIÓN EUROPEA**: **se normaliza por SONORIDAD y no por pico**, para que el
  espectador no toque el mando entre programa y anuncio.

## El 0 dBFS

- **PREGUNTA 9** · **Un valor de 0 dBFS representa LA MÁXIMA AMPLITUD QUE PUEDE TENER LA SEÑAL.**
- **LAS SIGLAS RESUELVEN LA PREGUNTA**: **dBFS = decibelios respecto de la ESCALA COMPLETA**, y **la
  escala completa es el valor más alto que los bits pueden representar**. **Por convenio, ese valor es
  el cero.**

| Escala | Dónde está el cero | Qué hay por encima |
|---|---|---|
| **Analógica** (dBu, VU) | **En el nivel de trabajo** | **Margen de sobrecarga** |
| **Digital** (dBFS) | **EN EL MÁXIMO ABSOLUTO** | **NADA** |

- **POR ESO TODOS LOS VALORES DIGITALES SON NEGATIVOS**: −6, −18, −20 dBFS. **Rebasar el cero no da
  saturación agradable: da RECORTE**, porque el convertidor no tiene más números.
- **LAS TRES FALSAS**: «mínima amplitud» → **lo contrario** · «inexistencia de señal» → **LA TRAMPA
  BUENA**: **el silencio es −∞ dBFS, no 0** · «un error de lectura» → **el 0 dBFS es un valor
  legítimo**.
- **LA REGLA DE TRABAJO**: **se trabaja con margen**, con los picos **entre −18 y −20 dBFS**,
  **precisamente porque por encima del cero no hay sitio.**

## La cadencia y la reproducción

- **PREGUNTAS 57 Y 61** · **La misma pregunta con «fps» añadido**: **la tasa de grabación original
  DETERMINA LA FLUIDEZ Y LA VELOCIDAD DEL VÍDEO.**

| Efecto | En qué consiste |
|---|---|
| **Fluidez** | **Más imágenes por segundo, movimiento más suave** |
| **Velocidad** | **Grabar a MÁS cadencia de la que se reproduce → CÁMARA LENTA**; a menos → acelerado |

- **EL SEGUNDO EFECTO ES OFICIO PURO**: **grabar a 100 y reproducir a 25 da una cámara lenta de cuatro
  veces SIN repetir ni inventar cuadros.** **Ésa es la única cámara lenta que no degrada**, y es la
  razón de que las cámaras de deportes graben a cadencia alta.
- **LAS TRES FALSAS, IDÉNTICAS EN LAS DOS PREGUNTAS**: «sólo afecta al tamaño» → **la palabra que la
  hunde es «SÓLO»** · «sólo afecta al audio» → **la cadencia de vídeo no toca el audio** · «no tiene
  ningún impacto» → **niega la respuesta**.
- **AVISO**: **es la ÚNICA repetición de este cuadernillo. Una sola respuesta vale dos preguntas de
  noventa y seis.**

## Las matrices

| Concepto | Qué es |
|---|---|
| **Entradas × salidas** | **El tamaño**: 64 × 64, 128 × 128 |
| **Punto de cruce** | Cada conexión posible |
| **Nivel** | **Cada tipo de señal que se conmuta a la vez**: vídeo, audio, datos |
| **Conmutación en el intervalo vertical** | **El cambio se hace en el hueco entre dos imágenes** |

- **POR QUÉ IMPORTA AL MONTADOR**: **la sala recibe sus fuentes y entrega su salida a través de la
  matriz**, y **una fuente que no aparece suele ser un problema de ENCAMINAMIENTO, no de la sala**.
- **LA REGLA QUE EVITA EL ERROR MÁS VISIBLE**: **se conmuta en el intervalo vertical.** Un cambio a
  mitad de imagen **parte el cuadro en dos, y eso se ve en antena.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 9 | Qué amplitud representa 0 dBFS | c) La máxima amplitud posible ✔ |
| 57 | Cómo afecta la tasa de grabación a la reproducción | a) Determina fluidez y velocidad ✔ |
| 61 | Cómo afecta la tasa fps a la reproducción | a) Determina fluidez y velocidad ✔ **·** repetida de la 57 |

**Las tres oficiales son correctas y ninguna descansa sólo en la plantilla.** · **Aviso de estudio**:
**la 57 y la 61 se diferencian en tres letras y tienen las mismas cuatro opciones en el mismo orden.**
· **Aviso de reparto**: **el punto 3 tiene tres subpuntos y sólo dos materias preguntadas**: **las
matrices de conmutación no han salido**, y el tema las desarrolla porque el programa las manda.
