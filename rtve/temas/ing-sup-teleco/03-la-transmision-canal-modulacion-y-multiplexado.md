# Tema 3 del específico de Ingeniería Superior · Telecomunicación · La transmisión: canal, modulación, multiplexado y acceso múltiple

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 3 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la teoría de la transmisión, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Tres preguntas y una regla** | **El intervalo unitario sale del RÉGIMEN BINARIO de la interfaz, no del formato de imagen.** Quien lo busque en el número de líneas o en la cadencia se equivoca de sitio |
| **Extensión** | **3.482 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: la relación señal a ruido (**SNR**,
*signal to noise ratio*); la tasa de error de bit (**BER**, *bit error rate*); el intervalo unitario
(**UI**, *unit interval*); el hercio (**Hz**), el megahercio (**MHz**) y el gigahercio (**GHz**); el bit
por segundo (**bit/s**), con sus múltiplos **Mbit/s** y **Gbit/s**; el picosegundo (**ps**) y el
nanosegundo (**ns**); el decibelio (**dB**); la comprobación de redundancia cíclica (**CRC**, *cyclic
redundancy check*); la corrección de errores hacia delante (**FEC**, *forward error correction*); el
sin retorno a cero (**NRZ**) en sus variantes **NRZ-L**, **NRZ-M** y **NRZ-S**; el multiplexado por
división en tiempo (**TDM**), en frecuencia (**FDM**), en longitud de onda (**WDM**) y por código
(**CDM**); el acceso múltiple por división en tiempo (**TDMA**), en frecuencia (**FDMA**), por código
(**CDMA**) y ortogonal en frecuencia (**OFDMA**); el dúplex por división en tiempo (**TDD**) y en
frecuencia (**FDD**); la modulación de amplitud (**AM**) y de frecuencia (**FM**); la modulación por
desplazamiento de amplitud (**ASK**), de frecuencia (**FSK**), de fase (**PSK**) y en cuadratura
(**QAM**); y la multiplexación ortogonal por división en frecuencia (**OFDM**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 3):
> «Transmisión. Clasificación de sistemas. Canal de transmisión. Diagramas de ojos. Capacidad.
> Adaptación al medio de transmisión: Modulación y tipos. Multiplexado y Acceso Múltiple. TDD y FDD.»

**Es el punto de TEORÍA de la transmisión**, y **conviene decir de entrada qué lo separa del punto 4**:
**éste estudia CÓMO se manda una señal por un medio; el 4 estudia POR QUÉ MEDIO se manda.** **La
modulación, el multiplexado y la capacidad son de aquí; el cable, la fibra y el conector son del
siguiente.**

**Y la idea que ordena el punto entero**: **transmitir es adaptar una señal a un canal que no se
eligió.** **El canal impone su ancho de banda, su ruido y su comportamiento**, y **todo lo que este
tema describe —modular, codificar, multiplexar, corregir— es lo que se hace para meter la información
que se tiene por el canal que hay.**

<!-- indice -->

## Índice

- [1. La clasificación de los sistemas de transmisión](#1-la-clasificación-de-los-sistemas-de-transmisión)
- [2. El canal de transmisión](#2-el-canal-de-transmisión)
- [3. El diagrama de ojo](#3-el-diagrama-de-ojo)
- [4. Los códigos de línea](#4-los-códigos-de-línea)
- [5. La modulación](#5-la-modulación)
- [6. Multiplexado y acceso múltiple](#6-multiplexado-y-acceso-múltiple)
- [7. Dúplex por división en tiempo y en frecuencia](#7-dúplex-por-división-en-tiempo-y-en-frecuencia)
- [8. La detección y la corrección de errores](#8-la-detección-y-la-corrección-de-errores)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. La clasificación de los sistemas de transmisión

**Cinco criterios, y hay que saber que son cinco criterios distintos y no una sola clasificación:**

| Criterio | Clases |
|---|---|
| **Por la NATURALEZA de la señal** | **Analógica** o **digital** |
| **Por el SENTIDO** | **Símplex** —un sentido—, **semidúplex** —los dos, pero no a la vez— y **dúplex** —los dos a la vez— |
| **Por el MEDIO** | **Guiado** —cable, fibra— o **no guiado** —radio, satélite, óptica libre— |
| **Por la SINCRONIZACIÓN** | **Síncrona** —con reloj común— o **asíncrona** —cada carácter con su marca— |
| **Por la BANDA** | **En banda base** —sin trasladar— o **en banda trasladada**, es decir modulada |

**Y las dos que más se preguntan, con lo que hay que saber decir de cada una:**

1. **Símplex, semidúplex y dúplex NO son lo mismo que TDD y FDD.** **Aquéllas describen si se puede
   hablar en los dos sentidos; TDD y FDD describen CÓMO se consigue el dúplex**, y son el último
   apartado del enunciado.
2. **Banda base no significa «sin codificar».** **Significa que la señal ocupa su banda natural, desde
   continua hacia arriba, sin trasladarla a una portadora.** **Una señal digital en banda base sí
   lleva un código de línea**, que es el epígrafe 3.

## 2. El canal de transmisión

**Qué es**: **el camino que la señal recorre entre el emisor y el receptor**, con todo lo que le hace
por el camino.

**Lo que un canal le hace a una señal, que es la lista que hay que saber:**

| Efecto | Qué es | Qué produce |
|---|---|---|
| **ATENUACIÓN** | **La señal pierde amplitud** con la distancia | Menos relación señal a ruido al final |
| **DISTORSIÓN de amplitud** | **El canal no atenúa igual todas las frecuencias** | Deformación de la forma de onda |
| **DISTORSIÓN de fase o de retardo de grupo** | **No todas las frecuencias tardan lo mismo** | Los componentes llegan descolocados |
| **RUIDO** | **Energía ajena que se suma**: térmico, de impulso, de intermodulación | Errores en la decisión del receptor |
| **INTERFERENCIA** | **Otra señal que se cuela** | Igual |
| **ECOS y multitrayecto** | **La misma señal llega por dos caminos** | **Interferencia entre símbolos** |

**Y la consecuencia común de la distorsión y del multitrayecto, que es el concepto del epígrafe**: **la
INTERFERENCIA ENTRE SÍMBOLOS.** **Un símbolo se alarga y se mete en el tiempo del siguiente**, de modo
que **el receptor decide mal aunque haya señal de sobra.** **No es un problema de potencia: es de
tiempo**, y **por eso se combate igualando el canal y no subiendo la potencia.**

**La CAPACIDAD del canal**, que el enunciado nombra expresamente y que hay que saber enunciar en sus
dos formas:

| Límite | Qué dice |
|---|---|
| **Límite de NYQUIST** | **En un canal sin ruido, la velocidad de símbolo está limitada por el ancho de banda**: el doble del ancho de banda, en símbolos por segundo |
| **Límite de SHANNON** | **En un canal con ruido, la capacidad depende del ancho de banda Y de la relación señal a ruido** |

**Las tres lecturas que hay que sacar de esos dos límites, y son lo que un examen puede pedir
razonado:**

1. **El ancho de banda limita los SÍMBOLOS por segundo, no los BITS.** **Para mandar más bits en los
   mismos símbolos hay que meter más bits en cada símbolo**, y **eso es exactamente lo que hace una
   modulación de orden alto.**
2. **Meter más bits por símbolo cuesta relación señal a ruido.** **Cuantos más estados tiene una
   constelación, más juntos están y más fácil es confundirlos.** **Por eso una modulación de orden
   alto pide un canal mejor.**
3. **Hay un techo, y lo pone Shannon.** **Por encima de la capacidad no se transmite sin errores por
   mucho que se afine la modulación**, y **la única salida es más ancho de banda o más relación señal
   a ruido.**

## 3. El diagrama de ojo

**El enunciado lo nombra expresamente y es el instrumento característico de este punto.**

**Qué es**: **la superposición, sobre un mismo eje de tiempos de un símbolo, de muchos tramos de la
señal recibida.** **El osciloscopio dispara con el reloj y va escribiendo encima**, y **lo que se
forma es un dibujo con un hueco en el centro: el «ojo».**

**Qué se lee en él, que es lo que hay que saber decir:**

| Lo que se mira | Qué significa |
|---|---|
| **La APERTURA VERTICAL del ojo** | **El margen de amplitud para decidir**: cuanto más abierto, más ruido se tolera |
| **La APERTURA HORIZONTAL** | **El margen de tiempo para muestrear**: cuanto más abierto, más fluctuación de reloj se tolera |
| **El grosor de los cruces** | **La FLUCTUACIÓN de fase o** ***jitter*** |
| **La inclinación de los flancos** | **La limitación de ancho de banda del canal** |
| **Un ojo CERRADO** | **Interferencia entre símbolos, ruido o ambas**: el receptor va a fallar |

**Y el INTERVALO UNITARIO, que es la medida del eje horizontal y la que un examen pide calcular**:
**es el tiempo que dura un símbolo**, y **es el inverso de la velocidad de símbolo.**

**Aplicado a las interfaces de vídeo digital en serie, que es como se pregunta:**

| Interfaz | Velocidad | Intervalo unitario |
|---|---|---|
| **Definición estándar** | **270 Mbit/s** | **1 / 270 MHz**, unos 3,7 ns |
| **Alta definición** | **1,485 Gbit/s** | **1 / 1,485 GHz**, unos 673 ps |
| **3 gigabits** | **2,970 Gbit/s** | **1 / 2,970 GHz**, unos 337 ps |
| **12 gigabits** | **11,88 Gbit/s** | **1 / 11,88 GHz**, unos 84 ps |

**La regla de examen, y hay que llevarla aprendida**: **el intervalo unitario se calcula del RÉGIMEN
BINARIO de la interfaz, no del formato de imagen.** **Una señal de mil ochenta líneas progresiva a
veinticinco cuadros viaja por una interfaz de 1,485 gigabits**, y **su intervalo unitario es el inverso
de esa cifra**, unos **673 picosegundos.** **Quien busque la cifra en el número de líneas o en la
cadencia se equivoca de sitio.**

## 4. Los códigos de línea

**Antes de modular hay que decidir CÓMO se representa un bit en el medio**, y **eso es el código de
línea.**

| Código | Cómo representa | Rasgo |
|---|---|---|
| **NRZ-L** | **Un nivel para el uno y otro para el cero** | **El más simple y el de menor ancho de banda**; **sin transiciones en una racha larga** |
| **NRZ-M** e **NRZ-S** | **Por INVERSIÓN**: hay transición cuando llega un uno (M) o un cero (S) | Diferenciales: no importa la polaridad absoluta |
| **Retorno a cero** | **Cada bit vuelve al nivel de reposo** | Más transiciones y **más ancho de banda** |
| **MANCHESTER** | **Cada bit lleva una transición EN SU MITAD** | **Reloj embebido**; **el que más ancho de banda pide** |
| **Codificaciones de bloque** | **Sustituyen grupos de bits por grupos mayores** | Controlan la continua y garantizan transiciones sin doblar el ancho |

**Los dos criterios que decide un código de línea, y hay que saber que van en direcciones opuestas:**

1. **RECUPERACIÓN DE RELOJ.** **El receptor saca su reloj de las transiciones de la señal**, así que
   **un código con pocas transiciones lo pierde**: una racha larga de ceros en un código sin retorno a
   cero deja al receptor sin referencia.
2. **ANCHO DE BANDA.** **Cuantas más transiciones, más ancho de banda hace falta**, y **el ancho de
   banda es justo lo que no sobra.**

**Y la conclusión que un examen persigue**: **de los códigos de la tabla, el que MÁS ancho de banda
pide es el Manchester**, porque **mete una transición en cada bit, y en el peor caso dos**, mientras
que **los sin retorno a cero pueden pasar bits enteros sin ninguna.** **Lo que Manchester compra con
ese ancho de banda es reloj garantizado y ausencia de componente continua**, y **por eso se usa donde
el medio no puede llevar continua.**

## 5. La modulación

**Modular es trasladar la información a una portadora**, y **hay que saber por qué se hace, en tres
razones:**

1. **Porque el medio no deja pasar la banda base.** **Una antena de longitud razonable radia bien a
   frecuencias altas, no a las de la voz.**
2. **Porque hay que COMPARTIR el medio.** **Trasladar cada señal a una portadora distinta permite que
   convivan.**
3. **Porque una señal modulada resiste mejor el canal.** **Se puede elegir un esquema robusto para un
   canal malo.**

**Las modulaciones analógicas, con lo que las distingue:**

| Modulación | Qué varía | Rasgo |
|---|---|---|
| **Amplitud** | **La amplitud de la portadora** | **Sencilla y estrecha**; **muy sensible al ruido**, que es de amplitud |
| **Frecuencia** | **La frecuencia de la portadora** | **Más inmune al ruido** y **más ancha** |
| **Fase** | **La fase de la portadora** | Emparentada con la anterior |

**Y la regla que resume la tabla**: **el ruido es esencialmente de amplitud**, así que **una modulación
que no lleva la información en la amplitud lo tolera mejor**, **a costa de ancho de banda.** **Ése es
el intercambio de todo el epígrafe.**

**Las modulaciones digitales, por el parámetro que desplazan:**

| Modulación | Qué desplaza |
|---|---|
| **Por desplazamiento de amplitud** | **La amplitud** |
| **Por desplazamiento de frecuencia** | **La frecuencia** |
| **Por desplazamiento de fase** | **La fase**: dos estados, cuatro, ocho… |
| **En cuadratura de amplitud** | **Amplitud Y fase a la vez**: es la que más bits mete por símbolo |

**Y la MULTIPLEXACIÓN ORTOGONAL POR DIVISIÓN EN FRECUENCIA, que merece párrafo propio porque es la que
sostiene la difusión digital**: **reparte la información entre muchísimas portadoras muy juntas y
ortogonales entre sí**, cada una **con una velocidad de símbolo baja.** **Y ahí está su ventaja
decisiva**: **un símbolo largo tolera ecos.** **Un multitrayecto que destrozaría una portadora única
rapidísima apenas molesta a miles de portadoras lentas**, sobre todo **con intervalo de guarda**, y
**por eso es la modulación de la televisión digital terrestre y de la radio digital.** **Eso se
desarrolla en los temas 7 y 22.**

## 6. Multiplexado y acceso múltiple

**Dos palabras que se confunden y que NO son lo mismo**, y **distinguirlas es la pregunta conceptual
del punto:**

| | **MULTIPLEXADO** | **ACCESO MÚLTIPLE** |
|---|---|---|
| **Qué hace** | **Juntar varias señales en un mismo medio** | **Repartir un mismo medio entre varios usuarios** |
| **Quién decide** | **Un solo equipo**, que tiene todas las señales | **Un protocolo**, entre equipos que no se ven |
| **Dónde se ve** | **Dentro de un enlace**: un múltiplex de televisión | **En un acceso**: una red móvil, un satélite |

**Las técnicas, que se corresponden una a una:**

| Recurso que se reparte | Multiplexado | Acceso múltiple |
|---|---|---|
| **El TIEMPO** | **Por división en tiempo** | **Por división en tiempo** |
| **La FRECUENCIA** | **Por división en frecuencia** | **Por división en frecuencia** |
| **La LONGITUD DE ONDA** | **Por división en longitud de onda**, en fibra | — |
| **El CÓDIGO** | **Por división en código** | **Por división en código** |
| **Las subportadoras** | — | **Ortogonal por división en frecuencia** |

**Y las dos observaciones de oficio:**

1. **La división en longitud de onda es división en frecuencia con otro nombre.** **En fibra se
   prefiere hablar de longitud de onda porque es como se especifican los componentes ópticos**, pero
   **el principio es el mismo: cada canal, su color.**
2. **La división en código no reparte ni tiempo ni frecuencia.** **Todos transmiten a la vez y en la
   misma banda**, y **lo que los separa es un código ortogonal.** **Para un receptor que no tiene el
   código, los demás son ruido.**

## 7. Dúplex por división en tiempo y en frecuencia

**El último apartado del enunciado**, y **el más fácil de recordar si se plantea como una pregunta**:
**si hay que hablar en los dos sentidos, ¿qué se parte, el tiempo o la frecuencia?**

| | **División en FRECUENCIA** | **División en TIEMPO** |
|---|---|---|
| **Cómo consigue el dúplex** | **Dos bandas separadas**, una para cada sentido | **Una sola banda**, alternando el sentido muy deprisa |
| **Espectro** | **Necesita un par de bandas y una banda de guarda entre ellas** | **Una sola banda** |
| **Simetría** | **Reparto fijo** entre subida y bajada | **Reparto AJUSTABLE**: se puede dar más tiempo al sentido que más carga tiene |
| **Latencia** | **Menor**: los dos sentidos están siempre abiertos | **Mayor**: hay que esperar el turno |
| **Interferencia** | **Los dos sentidos no se estorban** | **Exige sincronización estricta** entre estaciones vecinas |

**Y la lectura que hay que saber dar**: **la división en tiempo gana cuando el tráfico es ASIMÉTRICO y
variable** —que es el caso de casi todo el tráfico de datos moderno—, **y la división en frecuencia
gana cuando el tráfico es simétrico y la latencia importa.** **Por eso el dúplex por división en
tiempo se ha impuesto donde el espectro escasea y el tráfico es de datos.**

## 8. La detección y la corrección de errores

**No está nombrada en el enunciado con esas palabras, pero es lo que hace utilizable un canal real**, y
**el temario la incluye porque un examen de transmisión la pregunta.**

**Las dos familias, y hay que no confundirlas:**

| Familia | Qué hace | Qué necesita |
|---|---|---|
| **DETECCIÓN** | **Dice que el bloque llegó mal**, sin arreglarlo | **Un canal de vuelta para pedir repetición** |
| **CORRECCIÓN hacia delante** | **Arregla el error en el propio receptor** | **Redundancia añadida en el emisor**; no necesita vuelta |

**Y el mecanismo de detección que un examen nombra por su sigla**: **la comprobación de redundancia
cíclica.** **Qué es**: **un CÓDIGO DE DETECCIÓN DE ERRORES.** **El emisor trata el bloque como un
polinomio, lo divide por un polinomio generador y manda el resto; el receptor repite la cuenta y
compara.**

**Las tres cosas que hay que saber decir de ella, porque son las que distinguen la respuesta correcta
de las tres falsas:**

1. **DETECTA, no corrige.** **Dice que algo cambió; no dice qué ni lo arregla.**
2. **NO es autenticación ni firma.** **No prueba quién mandó el bloque**, sólo que llegó como salió.
   **Cualquiera que altere el bloque puede recalcular el resto.**
3. **NO es compresión.** **Añade bits, no los quita.**

**Y dónde aparece en esta casa**: **en la interfaz de vídeo digital en serie, que lleva su propia
comprobación por línea y por campo**, y **es lo que permite a un equipo de medida decir que un enlace
tiene errores aunque la imagen se vea.** **Eso es del tema 12.**

## 9. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**Un aviso de método que este tema tiene que dar**: **el enunciado de este punto no nombra ninguna
norma ni ninguna recomendación**, y **el tema va entero como teoría de la transmisión y oficio.**
**Eso deja sin objeto dos de las cinco lentes del proyecto** —la de exactitud normativa y la de
citas—, **y el cero que devolverían no diría «está bien»: diría «no he mirado nada».** **Se declara
aquí y se explica en el informe de refutación de esta ocupación.**

**Cinco declaraciones expresas:**

1. **Los cuatro regímenes binarios del epígrafe 3 —270 Mbit/s, 1,485 Gbit/s, 2,970 Gbit/s y
   11,88 Gbit/s— son los que el propio cuadernillo de esta ocupación pone en las opciones de su
   pregunta 23**, con sus intervalos unitarios al lado. **Se dan porque la plantilla los confirma**,
   y **el temario declara esa procedencia**: **no proceden de la norma que los fija, que no se ha
   consultado.**
2. **Este tema NO da ninguna fórmula de Nyquist ni de Shannon con sus constantes**, ni **ninguna
   relación señal a ruido, ni ningún orden de constelación, ni ninguna tasa de error.** **Se enuncia
   qué limita cada uno y en qué sentido**, que es **lo que un examen escrito puede preguntar.**
3. **Los códigos de línea se describen por su comportamiento y NO se les asigna ningún ancho de banda
   numérico.** **La conclusión de que el Manchester es el que más pide se razona por su número de
   transiciones**, y **así se declara.**
4. **Este tema NO nombra ningún estándar, ninguna norma de la Sociedad de Ingenieros de
   Cine y Televisión (`SMPTE`), de la Unión Internacional de Telecomunicaciones (`ITU`) o de la
   Unión Europea de Radiodifusión (`EBU`), ningún fabricante y ningún
   equipo comercial.** **Las interfaces de vídeo se nombran por su régimen binario**, y **sus normas
   se estudian en el tema 8.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **el medio
   físico y sus conectores, al tema 4**; **la modulación de la difusión terrestre, al tema 7**; **la
   de la radio digital, al tema 22**; **los instrumentos de medida, al tema 12**; **y el multiplexado
   sobre red de paquetes, a los temas 19 y 20.**

**El resto del tema va como oficio y así se declara**: la separación entre este punto y el 4 —cómo se
manda frente a por qué medio—, la idea de que transmitir es adaptar una señal a un canal que no se
eligió, la advertencia de que símplex y dúplex no son lo mismo que las técnicas de dúplex, la lectura
de la interferencia entre símbolos como problema de tiempo y no de potencia, las tres lecturas de los
límites de capacidad, la explicación de qué se lee en cada dimensión de un diagrama de ojo, la regla de
que el intervalo unitario sale del régimen binario y no del formato de imagen, los dos criterios
opuestos que decide un código de línea, las tres razones para modular, la regla de que el ruido es de
amplitud, la explicación de por qué la multiplexación ortogonal tolera ecos, la distinción entre
multiplexado y acceso múltiple con sus dos observaciones, la tabla comparada de los dos tipos de dúplex
con su lectura sobre el tráfico asimétrico y las tres cosas que hay que saber de la comprobación de
redundancia cíclica. **Nada de eso está en un boletín oficial ni en ninguna fuente consultada para este
proyecto**, y el tema no lo presenta como si lo estuviera.
