# Esquema · Tema 3 del específico de Ingeniería Superior · Telecomunicación · La transmisión: canal, modulación, multiplexado y acceso múltiple

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de teoría de la transmisión ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: la
relación señal a ruido (**SNR**); la tasa de error de bit (**BER**); el intervalo unitario (**UI**); el
hercio (**Hz**) con sus múltiplos **MHz** y **GHz**; el bit por segundo (**bit/s**) con **Mbit/s** y
**Gbit/s**; el picosegundo (**ps**) y el nanosegundo (**ns**); la comprobación de redundancia cíclica
(**CRC**); la corrección de errores hacia delante (**FEC**); el sin retorno a cero (**NRZ**) en sus
variantes **NRZ-L**, **NRZ-M** y **NRZ-S**; el multiplexado por división en tiempo (**TDM**), en
frecuencia (**FDM**), en longitud de onda (**WDM**) y por código (**CDM**); el acceso múltiple por
división en tiempo (**TDMA**), en frecuencia (**FDMA**), por código (**CDMA**) y ortogonal en
frecuencia (**OFDMA**); el dúplex por división en tiempo (**TDD**) y en frecuencia (**FDD**); las
modulaciones de amplitud (**AM**) y de frecuencia (**FM**); las digitales por desplazamiento de
amplitud (**ASK**), de frecuencia (**FSK**) y de fase (**PSK**) y la de cuadratura (**QAM**); y la
multiplexación ortogonal por división en frecuencia (**OFDM**).

**Cabecera.** Enunciado: punto 3 del anexo · **tres preguntas** · **sin norma**: el punto no nombra
ninguna y el tema va entero como teoría y oficio.

**La idea que lo ordena** · `[of]` · **Transmitir es adaptar una señal a un canal que no se eligió.**
**El canal impone ancho de banda, ruido y comportamiento**, y **modular, codificar, multiplexar y
corregir es lo que se hace para meter la información que se tiene por el canal que hay.**

**El deslinde con el punto 4** · `[plan]` · **Aquí, cómo se manda; allí, por qué medio se manda.**

<!-- indice -->

## Índice

- [Clasificación de sistemas](#clasificación-de-sistemas)
- [El canal y la capacidad](#el-canal-y-la-capacidad)
- [El diagrama de ojo](#el-diagrama-de-ojo)
- [Códigos de línea](#códigos-de-línea)
- [Modulación](#modulación)
- [Multiplexado y acceso múltiple](#multiplexado-y-acceso-múltiple)
- [Los dos dúplex](#los-dos-dúplex)
- [Detección y corrección de errores](#detección-y-corrección-de-errores)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Clasificación de sistemas

| Criterio | Clases |
|---|---|
| **Naturaleza** | **analógica** o **digital** |
| **Sentido** | **símplex**, **semidúplex**, **dúplex** |
| **Medio** | **guiado** o **no guiado** |
| **Sincronización** | **síncrona** o **asíncrona** |
| **Banda** | **banda base** o **banda trasladada** |

- **son cinco criterios, no una clasificación** · `[of]` · **Cada uno corta por su lado y una misma
  transmisión cae en las cinco tablas a la vez.**
- **el error de siempre** · `[of]` · **símplex, semidúplex y dúplex** dicen **si se puede hablar en los
  dos sentidos**; **dúplex por división en tiempo y en frecuencia** dicen **cómo se consigue.**
- **banda base no es «sin codificar»** · `[of]` · **Es «sin trasladar a portadora».** **Una señal
  digital en banda base sí lleva código de línea.**

## El canal y la capacidad

| Lo que el canal hace | Qué produce |
|---|---|
| **atenuación** | **menos relación señal a ruido al final** |
| **distorsión de amplitud** | **deformación de la onda** |
| **distorsión de fase** | **componentes descolocados en el tiempo** |
| **ruido e interferencia** | **decisiones equivocadas en el receptor** |
| **ecos y multitrayecto** | **interferencia entre símbolos** |

- **el concepto del epígrafe** · `[of]` · **La interferencia entre símbolos es un problema de TIEMPO,
  no de potencia.** **Un símbolo se alarga y se mete en el del vecino.** **Se combate igualando el
  canal, no subiendo la potencia.**
- **los dos límites** · `[of]` · **Nyquist**: sin ruido, **el ancho de banda limita los SÍMBOLOS por
  segundo.** **Shannon**: con ruido, **la capacidad depende del ancho de banda Y de la relación señal
  a ruido.**
- **las tres lecturas** · `[of]` · **1)** más bits en los mismos símbolos = **modulación de orden más
  alto**. **2)** más bits por símbolo **cuesta relación señal a ruido**: los estados se juntan.
  **3)** hay techo, y **por encima sólo se sube con más banda o mejor relación.**

## El diagrama de ojo

| Lo que se mira | Qué significa |
|---|---|
| **apertura vertical** | **margen de amplitud para decidir** |
| **apertura horizontal** | **margen de tiempo para muestrear** |
| **grosor de los cruces** | **fluctuación de fase** |
| **inclinación de los flancos** | **limitación de ancho de banda del canal** |
| **ojo cerrado** | **interferencia entre símbolos, ruido, o los dos** |

- **el intervalo unitario** · `[of]` · **Es lo que dura un símbolo** y **es el inverso de la velocidad
  de símbolo.**
- **LA REGLA DE EXAMEN** · `[exam]` · **El intervalo unitario sale del RÉGIMEN BINARIO de la interfaz,
  no del formato de imagen.** **Mil ochenta líneas progresivas a veinticinco cuadros viajan por la
  interfaz de 1,485 gigabits**: el intervalo es **el inverso de esa cifra**, no de la cadencia.
- **la escalera que el propio cuadernillo pone en las opciones** · `[exam]` · **270 Mbit/s → 3,7 ns**
  · **1,485 Gbit/s → 673 ps** · **2,970 Gbit/s → 337 ps** · **11,88 Gbit/s → 84 ps.**

## Códigos de línea

| Código | Cómo representa | Rasgo |
|---|---|---|
| **NRZ-L** | **un nivel por estado** | **el más estrecho**; **sin transiciones en rachas largas** |
| **NRZ-M / NRZ-S** | **por inversión ante un uno o ante un cero** | **diferenciales**: la polaridad absoluta da igual |
| **retorno a cero** | **cada bit vuelve al reposo** | **más transiciones, más banda** |
| **Manchester** | **transición en la mitad de cada bit** | **reloj embebido**; **el que más banda pide** |
| **de bloque** | **grupos de bits por grupos mayores** | **garantiza transiciones sin doblar la banda** |

- **los dos criterios van en direcciones opuestas** · `[of]` · **Recuperar el reloj pide
  transiciones**; **el ancho de banda pide que no las haya.** **Un código de línea es el punto de
  equilibrio entre esas dos exigencias.**
- **por qué gana Manchester la pregunta** · `[exam]` · **Mete una transición en cada bit y en el peor
  caso dos**, mientras que **los sin retorno a cero pueden pasar bits enteros sin ninguna.** **Lo que
  compra con esa banda es reloj garantizado y ausencia de componente continua.**

## Modulación

- **las tres razones para modular** · `[of]` · **1)** el medio no deja pasar la banda base —**una
  antena de tamaño razonable radia a frecuencias altas**—; **2)** hay que **compartir** el medio;
  **3)** una señal modulada **resiste mejor** el canal.

| Analógicas | Qué varía | Rasgo |
|---|---|---|
| **amplitud** | **la amplitud** | **estrecha y sencilla**; **sensible al ruido** |
| **frecuencia** | **la frecuencia** | **más inmune, más ancha** |
| **fase** | **la fase** | **emparentada con la anterior** |

- **la regla que resume la tabla** · `[of]` · **El ruido es esencialmente de amplitud**, así que **la
  modulación que no lleva ahí la información lo tolera mejor, a costa de banda.**

| Digitales | Qué desplaza |
|---|---|
| **por amplitud** | **la amplitud** |
| **por frecuencia** | **la frecuencia** |
| **por fase** | **la fase**: dos estados, cuatro, ocho… |
| **de cuadratura** | **amplitud y fase a la vez**: la que más bits mete por símbolo |

- **la que sostiene la difusión digital** · `[of]` · **Multiplexación ortogonal por división en
  frecuencia**: **muchísimas portadoras juntas y ortogonales, cada una lenta.** **Y ahí su ventaja: un
  símbolo largo tolera ecos.** **Con intervalo de guarda, el multitrayecto que destrozaría una
  portadora única rapidísima apenas molesta.** **Se desarrolla en los temas 7 y 22.**

## Multiplexado y acceso múltiple

| | **Multiplexado** | **Acceso múltiple** |
|---|---|---|
| **Qué hace** | **juntar varias señales en un medio** | **repartir un medio entre varios usuarios** |
| **Quién decide** | **un solo equipo que las tiene todas** | **un protocolo entre equipos que no se ven** |
| **Dónde se ve** | **dentro de un enlace** | **en un acceso** |

- **se corresponden una a una** · `[of]` · **tiempo, frecuencia y código** tienen las dos versiones;
  **la longitud de onda** sólo multiplexa —en fibra—; **las subportadoras ortogonales** sólo dan acceso
  múltiple.
- **la longitud de onda es frecuencia con otro nombre** · `[of]` · **En fibra se habla de longitud de
  onda porque así se especifican los componentes ópticos.** **Cada canal, su color.**
- **el código no reparte nada** · `[of]` · **Todos transmiten a la vez y en la misma banda**, y **lo
  que los separa es un código ortogonal.** **Para quien no lo tiene, los demás son ruido.**

## Los dos dúplex

| | **División en frecuencia** | **División en tiempo** |
|---|---|---|
| **Cómo** | **dos bandas, una por sentido** | **una banda, alternando muy deprisa** |
| **Espectro** | **un par de bandas y su guarda** | **una sola banda** |
| **Simetría** | **reparto fijo** | **reparto ajustable** |
| **Latencia** | **menor** | **mayor: hay que esperar turno** |
| **Interferencia** | **los sentidos no se estorban** | **exige sincronización estricta entre vecinas** |

- **la lectura** · `[of]` · **El de tiempo gana con tráfico asimétrico y variable** —el de datos—;
  **el de frecuencia gana con tráfico simétrico y cuando la latencia importa.** **Por eso el de tiempo
  se ha impuesto donde el espectro escasea.**

## Detección y corrección de errores

| Familia | Qué hace | Qué necesita |
|---|---|---|
| **detección** | **dice que llegó mal** | **canal de vuelta para pedir repetición** |
| **corrección hacia delante** | **lo arregla en el receptor** | **redundancia en el emisor**; sin vuelta |

- **las tres cosas de la comprobación de redundancia cíclica** · `[exam]` · **1) DETECTA, no
  corrige.** **2) No es autenticación ni firma**: cualquiera que altere el bloque recalcula el resto.
  **3) No es compresión**: añade bits, no los quita.
- **dónde aparece en esta casa** · `[of]` · **La interfaz de vídeo digital en serie lleva su propia
  comprobación por línea y por campo**, y **es lo que permite decir que un enlace tiene errores aunque
  la imagen se vea.** **Eso es del tema 12.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 23 | Intervalo unitario del diagrama de ojo de una señal de mil ochenta líneas progresivas a veinticinco cuadros | **673 ps, el inverso de 1,485 GHz** ✔ **·** sale del régimen binario, no del formato |
| 55 | Qué es la comprobación de redundancia cíclica | **Un código de detección de errores** ✔ **·** ni autenticación, ni firma, ni compresión |
| 58 | Qué código de línea pide más ancho de banda | **Manchester** ✔ **·** una transición por bit, y dos en el peor caso |
