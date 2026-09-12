# Esquema · Tema 3 del específico de Edición, Montaje y Procesos Audiovisuales · Conceptos básicos de sonido

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio, sin norma detrás.

**Siglas**: el protocolo de transferencia de hipertexto (**HTTP**); el protocolo
de internet (**IP**); el protocolo de transporte en tiempo real (**RTP**, *real-time transport
protocol*) y su protocolo de control (**RTCP**); el protocolo de inicio de sesión (**SIP**, *session
initiation protocol*); el protocolo de control de transmisión (**TCP**) y el de datagramas de
usuario (**UDP**).

**Cabecera.** Enunciado: «1.4. Conceptos básicos de Sonido» · **4 preguntas y las cuatro de sitios
distintos**: física del sonido, transporte por red, ecualización y herramienta de mezcla ·
**ninguna descansa sólo en la plantilla**.

<!-- indice -->

## Índice

- [Las tres cualidades](#las-tres-cualidades)
- [El timbre y los armónicos](#el-timbre-y-los-armónicos)
- [El audio digital](#el-audio-digital)
- [RTP y SIP](#rtp-y-sip)
- [Los filtros y el shelving](#los-filtros-y-el-shelving)
- [El ducking](#el-ducking)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las tres cualidades

| Cualidad | De qué magnitud depende |
|---|---|
| **Tono** (grave o agudo) | **De la FRECUENCIA** |
| **Intensidad** (fuerte o débil) | **De la AMPLITUD** |
| **Timbre** | **De la COMPOSICIÓN ARMÓNICA** |

- **LA FRECUENCIA NO ES EL TONO: ES SU CAUSA.** La frecuencia es física; el tono, percepción. Igual
  con amplitud e intensidad.
- **MARGEN AUDIBLE**: **de 20 Hz a 20.000 Hz**, y **se estrecha con la edad, primero por arriba**.

## El timbre y los armónicos

- **PREGUNTA 37** · **La propiedad relacionada con las intensidades relativas de los armónicos es el
  TIMBRE.**
- **QUÉ SON LOS ARMÓNICOS**: un instrumento **no produce una sola frecuencia**: produce **la
  fundamental** —que da el tono— **y múltiplos enteros de ella**. Un la de 440 Hz lleva 880, 1.320,
  1.760…
- **LO QUE CAMBIA ENTRE INSTRUMENTOS NO SON LAS FRECUENCIAS, SINO CUÁNTO PESA CADA UNA.** Violín y
  flauta en el mismo la **tienen los mismos armónicos**: difiere **la intensidad relativa**. Y eso es
  literalmente el enunciado.
- **LAS TRES FALSAS**: intensidad ← amplitud · tono ← frecuencia fundamental · **«frecuencia» NO es
  una cualidad: es una magnitud**. **Esa se cae por la construcción de la pregunta.**
- **CONSECUENCIA DE OFICIO**: **el timbre es lo que un ecualizador modifica**: cambia el peso de los
  armónicos, **y por eso cambia el carácter de una voz sin cambiar la nota**.

## El audio digital

| Parámetro | Qué fija | Valores de uso |
|---|---|---|
| **Frecuencia de muestreo** | **La frecuencia máxima que se conserva** | **48 kHz** en TV; 44,1 en disco |
| **Profundidad de bits** | **El rango dinámico** | **16 bits** emisión; **24 bits** producción |

- **REGLA DEL MUESTREO**: **hay que muestrear a MÁS DEL DOBLE de la frecuencia más alta que se quiera
  conservar.** 48 kHz cubre holgadamente los 20 kHz del oído.
- **REGLA DE LA PROFUNDIDAD**: **cada bit añade unos 6 dB de rango dinámico** → 16 bits ≈ 96 dB, 24
  bits ≈ 144 dB.
- **EN LA SALA**: **se trabaja con la profundidad más alta y se reduce AL FINAL**, porque **los bits
  que se tiran no vuelven**.

## RTP y SIP

- **PREGUNTA 41** · **El protocolo de transmisión de datos en un audiocódec IP es RTP.**
- **LA EXIGENCIA DEL DIRECTO**: **debe llegar A TIEMPO aunque llegue incompleto.** **Un paquete que
  llega tarde ya no sirve**, porque su hueco en el sonido ya pasó.

| Protocolo | Qué hace | Por qué no es la respuesta |
|---|---|---|
| **RTP** | **Transporta el flujo**, con marca de tiempo y número de secuencia | **ES la respuesta** |
| **SIP** | **Establece y termina la sesión** | **Señaliza la llamada, no lleva el audio** |
| **TCP** | **Retransmite lo perdido y ordena** | **La retransmisión llega tarde** |
| **HTTP** | Ficheros sobre TCP | Hereda el problema de TCP |

- **LA FRASE QUE RESUELVE**: **SIP marca el número; RTP lleva la voz.** El examen pone SIP el primero
  **precisamente porque aparece siempre junto a RTP**.
- **EL DATO QUE EXPLICA EL RESTO**: **RTP corre sobre UDP**, que **no retransmite ni ordena**, y es RTP
  quien pone **la marca de tiempo y el número de secuencia**.

## Los filtros y el shelving

| Filtro | Qué hace |
|---|---|
| **Paso alto** | Deja pasar las altas, corta las bajas |
| **Paso bajo** | Deja pasar las bajas, corta las altas |
| **Paso banda** / **notch** | Deja o corta **una banda** |
| **Campana** (*peaking*) | **Realza o atenúa alrededor de una frecuencia y VUELVE A CERO a los dos lados** |
| ***SHELVING*** | **Realza o atenúa A PARTIR de una frecuencia y MANTIENE ese nivel hasta el extremo** |

- **PREGUNTA 86** · **Un *shelving* ATENÚA LA RESPUESTA A UNA FRECUENCIA SELECCIONADA Y SIGUE A ESE
  NIVEL HASTA EL FINAL DEL ESPECTRO AUDIBLE.**
- **LA IMAGEN QUE LO FIJA**: **de *shelf*, «estante»**. **La curva sube o baja hasta un nivel y allí se
  queda PLANA, como una balda.** Eso lo separa **de la campana** (que vuelve al otro lado) **y del
  paso alto o bajo** (que siguen cayendo).
- **LAS TRES FALSAS**: «elimina frecuencias bajas» = **el paso alto** · «realza frecuencias altas» =
  **un caso particular, no la definición** · «ajusta la ganancia» = **un control de volumen**.
- **AVISO**: **la definición del examen es incompleta** —un *shelving* también realza, y en graves o en
  agudos—, **pero la marcada es la única que describe el COMPORTAMIENTO.**

## El ducking

- **PREGUNTA 87** · **El *audio ducking* REDUCE EL NIVEL DE UNA O MÁS PISTAS CUANDO SE DESEA ESCUCHAR
  OTRA.**
- **PARA QUÉ**: **es lo que hace que la música baje sola cuando entra la voz en off** y suba al callar.
  De *duck*, **agacharse**: la música se agacha.
- **CÓMO**: **el nivel de una pista controla la ganancia de otra.** Es **un compresor con entrada
  lateral**, con tres ajustes: **cuánto baja**, **cuánto tarda en bajar** y **cuánto tarda en volver**.
- **LAS TRES FALSAS SON FUNCIONES REALES**: agrupar pistas = **grupos o *submixes*** · seguimiento de
  *frames* duplicados = **detección de duplicados, y de VÍDEO** · convertir dos mono en estéreo = **el
  emparejado estéreo, que cambia el enrutado y no el nivel**.
- **LA PALABRA QUE RESUELVE ES «CUANDO»**: **el *ducking* es automático y CONDICIONAL**, y ninguna otra
  opción tiene esa condición.
- **AVISO DE OFICIO**: **un retorno demasiado rápido hace que la música «respire»** detrás de la voz.
  **Es el defecto por el que se reconoce una mezcla hecha con prisa.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 37 | Propiedad ligada a los armónicos | d) Timbre ✔ |
| 41 | Protocolo de transmisión en un audiocódec IP | c) RTP ✔ |
| 86 | Qué es un filtro *shelving* | b) Atenúa y mantiene el nivel hasta el final ✔ |
| 87 | Qué es el *audio ducking* | c) Reduce unas pistas para escuchar otra ✔ |

**Las cuatro oficiales son correctas y ninguna descansa sólo en la plantilla.** · **Aviso de estudio**:
**la 86 define el *shelving* sólo por su forma de atenuar**, cuando también realza: **la marcada es la
única defendible, pero no es una definición completa.**
