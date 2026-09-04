# Esquema · Tema 17 del específico de Ingeniería Superior · Telecomunicación · Sistemas radiantes, parámetros de antena y propagación

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de radiocomunicaciones ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: la
potencia isótropa radiada equivalente (**PIRE**); el decibelio (**dB**), el decibelio sobre milivatio
(**dBm**), sobre el isótropo (**dBi**) y sobre el dipolo (**dBd**); la relación de onda estacionaria
(**ROE**); las frecuencias muy altas (**VHF**), ultraaltas (**UHF**), superaltas (**SHF**) y
extremadamente altas (**EHF**); el hercio (**Hz**) con **kHz**, **MHz** y **GHz**; y la longitud de
onda (**λ**).

**Cabecera.** Enunciado: punto 19 del anexo · **cinco preguntas** · **sin norma del boletín**.

**El reparto con el punto 25** · `[plan]` · **El punto 25 es idéntico palabra por palabra al punto 18
del anexo de Ingeniería Técnica · Telecomunicación y su tema se COMPARTE con aquella ocupación.**
**Allí van las líneas, las guías de onda, los transmisores y la medida de distorsiones; aquí, los
PARÁMETROS y la PROPAGACIÓN.**

**La idea que lo ordena** · `[of]` · **Una antena no amplifica nada.** **La ganancia de una antena es
CONCENTRACIÓN: reparte la misma potencia en menos ángulo.** **Quien entienda eso no se equivoca en
ninguna pregunta de este tema.**

<!-- indice -->

## Índice

- [Qué es una antena](#qué-es-una-antena)
- [Los parámetros básicos](#los-parámetros-básicos)
- [El cálculo de potencia radiada](#el-cálculo-de-potencia-radiada)
- [Los tipos de antena](#los-tipos-de-antena)
- [La propagación](#la-propagación)
- [Las bandas](#las-bandas)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es una antena

- **la definición funcional** · `[of]` · **El dispositivo que convierte una onda guiada en una onda
  radiada, y al revés.** **Es la frontera entre el cable y el espacio.**
- **las dos propiedades que se derivan** · `[of]` · **1) es RECÍPROCA**: su comportamiento al
  transmitir y al recibir es el mismo, **misma ganancia, mismo diagrama, misma polarización.** **2)
  está ADAPTADA o no lo está**: **si su impedancia no casa con la de la línea, parte de la potencia se
  refleja y vuelve**, y **eso no calienta el aire: calienta el transmisor.**

## Los parámetros básicos

| Parámetro | Qué mide |
|---|---|
| **diagrama o patrón de radiación** | **la DISTRIBUCIÓN ESPACIAL de la potencia radiada** |
| **directividad** | **cuánto concentra respecto a un radiador isótropo** |
| **ganancia** | **la directividad por el rendimiento: lo que de verdad sale** |
| **ancho de haz** | **el ángulo dentro del cual la potencia no baja de la mitad** |
| **relación delante-detrás** | **cuánto menos radia hacia atrás que hacia delante** |
| **lóbulos secundarios** | **lo que radia fuera del haz principal: interferencia potencial** |
| **polarización** | **la orientación del campo eléctrico: vertical, horizontal, circular** |
| **impedancia de entrada** | **lo que la antena presenta a la línea** |

- **LA PREGUNTA DEL PATRÓN** · `[exam]` · **El patrón de radiación representa la distribución espacial
  de la potencia radiada.** **No la impedancia característica, ni la polarización, ni la eficiencia
  comparada con un dipolo**: esas tres son otros parámetros de la misma tabla.
- **por qué hay dos referencias de ganancia** · `[of]` · **La misma antena da un número MAYOR medida
  sobre el isótropo que sobre el dipolo**, porque **el dipolo ya concentra algo y el isótropo no
  concentra nada.** **Comparar dos antenas exige que las dos vengan en la misma referencia.**
- **la regla de la polarización** · `[of]` · **Emisor y receptor tienen que coincidir.** **Una antena
  vertical frente a una horizontal pierde casi todo, y no hay ganancia que lo compense.**

## El cálculo de potencia radiada

- **LA REGLA QUE DECIDE LA PREGUNTA** · `[exam]` · **Las PÉRDIDAS se restan y la ganancia se suma**, y
  **todo tiene que estar en la misma escala logarítmica antes de sumar.**
- **las tres cosas que hay que vigilar** · `[of]` · **1)** que la potencia y el resultado vayan en la
  misma unidad de referencia; **2)** que la ganancia esté en la referencia que se dice —isótropo o
  dipolo—; **3)** **que las pérdidas del cableado no se olviden**, que es el descuido que las opciones
  falsas premian.
- **el ejemplo que la plantilla confirma** · `[exam]` · **Potencia de −10, ganancia de 30 y pérdidas de
  1 dan 19**, y **las opciones falsas salen de sumar las pérdidas en vez de restarlas o de olvidarlas.**

## Los tipos de antena

| Tipo | Qué la caracteriza |
|---|---|
| **dipolo** | **la referencia básica**: poco directiva |
| **agrupación de dipolos** | **muchos elementos alimentados en fase**: concentra en el plano que interese |
| **panel** | **la de difusión terrestre**: se agrupan para dibujar el diagrama que la cobertura pide |
| **parabólica** | **muy directiva, para frecuencias altas** |
| **de bocina** | **transición entre guía de onda y espacio** |
| **helicoidal** | **polarización circular** |

- **las dos reglas de tamaño y frecuencia** · `[of]` · **1)** el tamaño de una antena va con la
  LONGITUD DE ONDA: **a más frecuencia, antena más pequeña.** **2)** a igual tamaño físico, **más
  frecuencia da más ganancia**, porque **el mismo reflector abarca más longitudes de onda.**
- **lo que eso esconde** · `[of]` · **Ganancia y tolerancia de apuntamiento van en direcciones
  opuestas**: **más ganancia es haz más estrecho, y un haz estrecho hay que apuntarlo mejor y se mueve
  con el viento.**
- **el radomo** · `[exam]` · **Una CUBIERTA PROTECTORA para antenas.** **No es una modulación, ni un
  sistema de radar, ni un aparato de medida.** **Su exigencia es ser transparente a la onda**: **un
  radomo que atenúa es una pérdida permanente en el sistema.**

## La propagación

| Fenómeno | Qué es |
|---|---|
| **reflexión** | **la onda rebota en una superficie grande y lisa** |
| **refracción** | **cambia de velocidad al pasar de un medio a otro y se dobla** |
| **difracción** | **la onda bordea un obstáculo y llega detrás de él** |
| **dispersión** | **se reparte al chocar con muchos objetos pequeños** |
| **absorción** | **el medio se queda con parte de la energía** |

- **LA PREGUNTA QUE SE HACE** · `[exam]` · **El fenómeno por el que una onda cambia de dirección al
  ENCONTRAR UN OBSTÁCULO es la DIFRACCIÓN.** **La reflexión es rebote en superficie; la absorción no
  cambia dirección, quita energía; y la polarización no es un fenómeno de propagación sino una
  propiedad de la onda.**
- **por qué importa** · `[of]` · **La difracción explica media cobertura terrestre**: **es lo que hace
  que haya señal detrás de una loma.** **Y se difracta más cuanto MÁS BAJA es la frecuencia**, que es
  la razón de que las bandas bajas cubran mejor el terreno accidentado.

## Las bandas

- **la escalera de décadas** · `[exam]` · **De 30 a 300 megahercios, muy altas** —lo que la plantilla
  confirma—; **de 300 a 3.000, ultraaltas; de 3 a 30 gigahercios, superaltas; de 30 a 300,
  extremadamente altas.** **Fijado el punto de partida y el factor diez, la tabla no hay que
  memorizarla.**
- **el intercambio que resume el tema** · `[of]` · **A más frecuencia, más ancho de banda y más
  directividad, y también más atenuación por lluvia y más necesidad de línea de vista.** **Toda la
  ingeniería de radiocomunicaciones es elegir un punto en ese intercambio.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 31 | Potencia radiada de un sistema con potencia, ganancia y pérdidas dadas | **19 dBm** ✔ **·** la ganancia suma y las pérdidas restan |
| 33 | Qué banda ocupan las frecuencias muy altas | **De 30 a 300 megahercios** ✔ |
| 35 | Qué representa el patrón de radiación | **La distribución espacial de la potencia radiada** ✔ |
| 42 | Qué es un radomo | **Una cubierta protectora para antenas** ✔ |
| 87 | Fenómeno por el que la onda cambia de dirección al encontrar un obstáculo | **Difracción** ✔ |
