# Tema 3 del específico de Edición, Montaje y Procesos Audiovisuales · Conceptos básicos de sonido

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 3 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Sin norma: no la hay.** Su materia son las cualidades del sonido, el audio digital, los protocolos de transporte en tiempo real y el tratamiento de audio, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Advertencia** | **La definición de filtro *shelving* que da el examen es incompleta**: describe sólo su forma de atenuar, cuando un *shelving* también realza. El tema la completa en lugar de recortarla |
| **Extensión** | **2.153 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el protocolo de internet (**IP**); el protocolo de
transporte en tiempo real (**RTP**, *real-time transport protocol*) y su protocolo de control
(**RTCP**); el protocolo de inicio de sesión (**SIP**, *session initiation protocol*); el protocolo
de control de transmisión (**TCP**) y el de datagramas de usuario (**UDP**); el protocolo de
transferencia de hipertexto (**HTTP**); el ecualizador (**EQ**); el hercio (**Hz**) y el kilohercio
(**kHz**); el decibelio (**dB**); y la Unión Internacional de Telecomunicaciones (**UIT**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, punto 1.4):
> «Conceptos básicos de Sonido.»

**Cuatro preguntas**, y las cuatro son de sitios distintos: **una de física del sonido**, **una de
transporte por red**, **una de ecualización** y **una de la herramienta de edición**. Es un punto
corto pero disperso, y hay que cubrirlo entero.

<!-- indice -->

## Índice

- [1. Las tres cualidades del sonido](#1-las-tres-cualidades-del-sonido)
- [2. El timbre y los armónicos](#2-el-timbre-y-los-armónicos)
- [3. El audio digital: muestreo, cuantificación y caudal](#3-el-audio-digital-muestreo-cuantificación-y-caudal)
- [4. El audio por IP y el audiocódec](#4-el-audio-por-ip-y-el-audiocódec)
- [5. La ecualización y los filtros](#5-la-ecualización-y-los-filtros)
- [6. El *ducking* y las herramientas de mezcla](#6-el-ducking-y-las-herramientas-de-mezcla)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Las tres cualidades del sonido

**Todo lo que se oye se describe con tres cualidades**, y cada una depende de una magnitud física
distinta. **Confundirlas es el error que este punto castiga.**

| Cualidad | Qué distingue | De qué magnitud depende |
|---|---|---|
| **Tono** | Grave o agudo | **De la frecuencia**: los ciclos por segundo |
| **Intensidad** | Fuerte o débil | **De la amplitud**: la magnitud de la variación de presión |
| **Timbre** | **Qué instrumento suena** | **De la composición armónica** |

**La frecuencia no es el tono, es su causa.** Se mide en hercios y es física; el tono es percepción.
La misma distinción vale para las otras dos: **la amplitud es física, la intensidad percibida es
psicoacústica**, y por eso se mide en decibelios, que es una escala logarítmica ajustada a cómo oye el
oído.

**El margen de frecuencias audibles**, que conviene tener a mano: **de 20 Hz a 20.000 Hz**, y se
estrecha con la edad, primero por arriba.

## 2. El timbre y los armónicos

**La propiedad del sonido directamente relacionada con las intensidades relativas de sus armónicos es
el timbre.** Ésa es la respuesta oficial a la pregunta 37.

**Qué son los armónicos.** Cuando un instrumento da una nota, **no produce una sola frecuencia**:
produce **la fundamental** —que es la que determina el tono— **y una serie de múltiplos enteros de
ella**, los armónicos. **Un la de 440 Hz lleva componentes en 880, 1.320, 1.760 y así sucesivamente.**

**Lo que cambia de un instrumento a otro no son las frecuencias, sino cuánto pesa cada una.** Un
violín y una flauta que dan el mismo la **tienen los mismos armónicos**; lo que difiere es **la
intensidad relativa de cada uno**. Y ésa es, literalmente, la definición que el enunciado da del
timbre.

**Las tres opciones falsas de la pregunta 37 son cualidades y magnitudes reales que dependen de otra
cosa:**

| Opción | De qué depende en realidad |
|---|---|
| **Intensidad** | De la amplitud |
| **Tono** | De la frecuencia fundamental |
| **Frecuencia** | **No es una cualidad del sonido, es una magnitud física** |

**El aviso sobre la opción c)**: **«frecuencia» no es una propiedad percibida sino una magnitud**, y
el enunciado pregunta por una propiedad. **Aunque no se supiera nada de armónicos, esa opción se cae
por la construcción de la pregunta.**

**Y una consecuencia de oficio**: **el timbre es lo que un ecualizador modifica.** Al subir o bajar
bandas se cambia el peso relativo de los armónicos, y por eso **la ecualización cambia el carácter de
una voz sin cambiar la nota que dice.**

## 3. El audio digital: muestreo, cuantificación y caudal

**Digitalizar sonido es medirlo muchas veces por segundo y anotar cada medida con un número.**

| Parámetro | Qué fija | Valores de uso |
|---|---|---|
| **Frecuencia de muestreo** | **Cuántas veces por segundo se mide.** Determina la frecuencia máxima que se conserva | **48 kHz** en televisión; 44,1 kHz en disco; 96 kHz en producción musical |
| **Profundidad de bits** | **Cuántos niveles tiene cada medida.** Determina el rango dinámico | **16 bits** en emisión; **24 bits** en producción |
| **Número de canales** | Mono, estéreo, envolvente | 2, 5.1, 5.1.4 |

**La regla que gobierna el muestreo**: **hay que muestrear a más del doble de la frecuencia más alta
que se quiera conservar.** Por eso 48 kHz cubre holgadamente los 20 kHz del oído, y por eso **un
material muestreado a 32 kHz no puede recuperar los agudos que perdió**.

**La regla que gobierna la profundidad**: **cada bit añade unos 6 dB de rango dinámico.** De ahí que
16 bits den unos 96 dB y 24 bits unos 144 dB, que es más de lo que ningún sistema de reproducción
entrega.

**Lo que esto significa en la sala de edición**: **el audio se trabaja con la profundidad más alta
disponible y se reduce al final**, nunca al revés, porque **los bits que se tiran no vuelven**.

## 4. El audio por IP y el audiocódec

**Un audiocódec IP es el aparato que lleva audio de calidad de emisión por una red de datos**: es lo
que hace posible una conexión en directo desde un exterior, o el retorno de un corresponsal, sin
línea dedicada.

**El protocolo de transmisión de datos en un audiocódec IP es RTP.** Ésa es la respuesta oficial a la
pregunta 41.

**Por qué RTP y no otro.** El audio en directo tiene una exigencia que el resto del tráfico de red no
tiene: **debe llegar a tiempo, aunque llegue incompleto**. Un paquete que llega tarde **ya no sirve**,
porque su hueco en el sonido ya ha pasado.

| Protocolo | Qué hace | Por qué no es la respuesta |
|---|---|---|
| **RTP** | **Transporta flujos en tiempo real**, con marca de tiempo y número de secuencia en cada paquete | **Es la respuesta**: lleva el audio |
| **SIP** | **Establece, modifica y termina la sesión**: quién llama a quién | **Señaliza la llamada, no lleva el audio.** Trabaja *con* RTP, no en su lugar |
| **TCP** | Transporte fiable: **retransmite lo que se pierde y ordena** | **La retransmisión llega tarde**: en directo, esperar un paquete perdido es peor que perderlo |
| **HTTP** | Transferencia de páginas y ficheros sobre TCP | **Es de aplicación y hereda el problema de TCP** |

**La distinción que resuelve la pregunta**: **SIP marca el número; RTP lleva la voz.** Es el mismo
reparto que en telefonía sobre IP, y **el examen pone SIP como primera opción precisamente porque
aparece siempre junto a RTP.**

**Y el dato técnico que explica el resto**: **RTP corre normalmente sobre UDP**, que **no retransmite
ni garantiza el orden**, y es RTP quien pone **la marca de tiempo y el número de secuencia** que
permiten al receptor reconstruir el flujo y descartar lo que llegó tarde.

## 5. La ecualización y los filtros

**Ecualizar es cambiar el equilibrio entre las bandas de frecuencia de una señal.** En una sala de
edición se hace por tres motivos: **corregir** un defecto de captación, **encajar** una voz sobre una
música, y **construir** un efecto.

**Las familias de filtro, que es lo que la pregunta 86 pone a prueba:**

| Filtro | Qué hace |
|---|---|
| **Paso alto** (*high pass*) | **Deja pasar las altas y corta las bajas** |
| **Paso bajo** (*low pass*) | **Deja pasar las bajas y corta las altas** |
| **Paso banda** | Deja pasar una banda y corta a los dos lados |
| **De rechazo de banda** o *notch* | **Corta una banda estrecha**: es el que quita un zumbido |
| **Campana** (*peaking*, *bell*) | **Realza o atenúa alrededor de una frecuencia**, y vuelve a cero a los dos lados |
| ***Shelving*** | **Realza o atenúa a partir de una frecuencia, y mantiene ese nivel hasta el extremo del espectro** |

**Un filtro *shelving* es un filtro que atenúa la respuesta en frecuencia a una frecuencia
seleccionada, siguiendo a ese nivel hasta el final del espectro audible.** Ésa es la respuesta oficial
a la pregunta 86.

**La imagen que fija la definición**: **el nombre viene de *shelf*, «estante».** La curva **sube o baja
hasta un nivel y allí se queda plana**, como la balda de una estantería. **Eso es lo que lo distingue
de la campana**, que vuelve a bajar al otro lado, **y del paso alto o bajo**, que **siguen cayendo
hasta el infinito** en lugar de estabilizarse.

**Las tres opciones falsas de la pregunta 86 y por qué se caen:**

| Opción | Qué describe en realidad |
|---|---|
| «Elimina frecuencias bajas» | **El filtro paso alto** |
| «Realza frecuencias altas» | **Un *shelving* de agudos puede hacerlo**, pero es un caso particular, no la definición: el *shelving* **puede realzar o atenuar, y en graves o en agudos** |
| «Ajusta la ganancia de la señal» | **Eso es un control de volumen**, que actúa sobre todas las frecuencias por igual |

**El aviso sobre la opción c)**: es la trampa mejor puesta de la pregunta, **porque no es falsa del
todo**. Lo que la descarta es que **describe un caso concreto y no el filtro**; la opción b) describe
**el comportamiento**, que es lo que el enunciado pide.

## 6. El *ducking* y las herramientas de mezcla

**El *audio ducking* es una función que permite reducir el nivel de audio de una o más pistas cuando
se desea escuchar el nivel de otra pista de audio.** Ésa es la respuesta oficial a la pregunta 87.

**Para qué sirve, en el trabajo real**: es **lo que hace que la música baje sola cuando entra la voz
en off** y vuelva a subir cuando la voz calla. **El nombre viene de *duck*, agacharse**: la música se
agacha para dejar pasar la voz.

**Cómo funciona**: **el nivel de una pista —la que manda— controla la ganancia de otra —la que
cede—**. Es un compresor con **entrada lateral**, y sus tres ajustes son los de cualquier compresor:
**cuánto baja**, **cuánto tarda en bajar** y **cuánto tarda en volver**.

**Las tres opciones falsas describen otras funciones reales de un editor de audio:**

| Opción | Qué describe en realidad |
|---|---|
| «Agrupar pistas de audio» | **Los grupos o *submixes***: no tocan el nivel de nadie automáticamente |
| «Seguimiento visual de *frames* duplicados» | **Una herramienta de detección de duplicados**, y además **de vídeo, no de audio** |
| «Convierte dos pistas mono en dos pistas estéreo» | **El emparejado estéreo**: cambia el enrutado, no el nivel |

**La palabra que resuelve la pregunta es «cuando»**: el *ducking* **es automático y condicional** —baja
una pista **cuando** suena otra—, y ninguna de las otras tres opciones tiene esa condición.

**Y una advertencia de oficio**: **el *ducking* automático se nota si está mal ajustado.** Un retorno
demasiado rápido hace que la música «respire» detrás de la voz, y ése es el defecto por el que se
reconoce una mezcla hecha con prisa.

## 7. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 37 | Propiedad relacionada con las intensidades relativas de los armónicos | d) Timbre ✔ |
| 41 | Protocolo de transmisión de datos en un audiocódec IP | c) RTP ✔ |
| 86 | Qué es un filtro *shelving* | b) Atenúa a partir de una frecuencia y mantiene el nivel ✔ |
| 87 | Qué es el *audio ducking* | c) Reduce el nivel de unas pistas para escuchar otra ✔ |

**Las cuatro respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla**: las
cuatro son definiciones estándar de acústica, de redes y de tratamiento de audio.

**Un aviso de estudio.** **La pregunta 86 define el *shelving* sólo por su forma de atenuar**, cuando
un *shelving* también realza. **La opción marcada es la única que describe el comportamiento
característico** —el nivel que se mantiene hasta el extremo del espectro—, así que es la buena, pero
**quien busque una definición completa no la encontrará entre las cuatro**.

## 8. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son conceptos de acústica, de audio digital, de
protocolos de red y de tratamiento de sonido, y **va entera como oficio**.

**Ninguna de sus cuatro respuestas descansa sólo en la plantilla.** El timbre y los armónicos, el
reparto de papeles entre SIP y RTP, la forma de la curva de un filtro *shelving* y el funcionamiento
del *ducking* **son definiciones asentadas**, verificables en cualquier manual de acústica, de redes o
de mezcla.

**Lo que este tema declara expresamente**: **la definición de *shelving* que el examen da es
incompleta**, y el tema la completa en lugar de recortarla. **La respuesta oficial sigue siendo la
única marcable**, y el motivo va escrito en su epígrafe.
