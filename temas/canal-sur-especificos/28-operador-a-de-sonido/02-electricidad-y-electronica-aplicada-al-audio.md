# Tema 2 del específico de Operador/a de Sonido · Electricidad y electrónica aplicada al audio

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 2 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Una norma: Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida (sólo para el nombre y el símbolo de tres unidades). Documentación de fabricante: Rane, RaneNotes 110, 124, 135, 151, 155 y 169; DPA Microphones y Schoeps (alimentación *phantom*, que remiten a la norma IEC 61938:2018; DPA también para el CMRR); Crown y Texas Instruments (amplificadores). Lo demás, oficio |
| **Redacción que se estudia** | Real Decreto 2032/2009 en la redacción vigente el 24/09/2026 (la de su capítulo II, en vigor desde el 30/04/2020); documentación de fabricante leída el 25/09/2026 |
| **Extensión** | Unas 9.000 palabras |

<!-- /portada -->

Siglas y símbolos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); corriente continua (**CC**, o **DC** en
la documentación en inglés) y alterna (**CA**, o **AC**); voltio (**V**), amperio (**A**), ohmio
(**Ω**), vatio (**W**) y faradio (**F**), unidades legales de medida; hercio (**Hz**); miliamperio
(**mA**) y kiloohmio (**kΩ**); valor eficaz (**rms**, *root mean square*); decibelio referido a
0,775 voltios eficaces (**dBu**), referido a 1 voltio (**dBV**) y referido a la escala completa de
un convertidor digital (**dBFS**, *full scale*); nivel de presión sonora (**SPL**, *sound pressure
level*) y el decibelio que lo mide (**dB SPL**); pascal (**Pa**); distorsión armónica total (**THD**,
*total harmonic distortion*); relación señal/ruido (**S/N**); interferencia de radiofrecuencia
(**RFI**, *radio frequency interference*); Sociedad de Ingeniería de Audio (**AES**, *Audio
Engineering Society*) y su norma de audio digital de dos canales (**AES3**); Comisión Electrotécnica
Internacional (**IEC**, *International Electrotechnical Commission*); conector de tres polos con
anillo de bloqueo (**XLR**) y jack de 6,35 mm de punta, anillo y cuerpo (**TRS**, *tip, ring,
sleeve*) o sólo de punta y cuerpo (**TS**); alimentación fantasma a 48 y a 12 voltios (**P48** y
**P12**); alimentación por hilos (**A-B** o *Tonader*); caja de inyección directa (**DI**, *direct
box*); las clases de amplificador, que se nombran por letra y de las que una es doble (**clase
AB**); la unidad de volumen del vúmetro (**VU**, *volume unit*); la modulación por anchura de
impulsos (**PWM**, *pulse width modulation*); la compatibilidad electromagnética (**EMC**,
*electromagnetic compatibility*); la interferencia electromagnética (**EMI**, *electromagnetic
interference*); la relación de rechazo en modo común (**CMRR**, *common mode rejection ratio*); la
Unión Europea de Radiodifusión (**EBU**, *European Broadcasting Union*), que firma sus
recomendaciones como EBU R; la interfaz digital de audio multicanal (**MADI**, *multichannel audio
digital interface*); el Instituto Alemán de Normalización (**DIN**); la interfaz digital
serie de vídeo (**SDI**, *serial digital interface*). **Dante** es el nombre comercial de un sistema de audio sobre
red, no una sigla. Los fabricantes citados se nombran por su
marca: Rane, Crown y Texas Instruments (electrónica de audio), Schoeps y DPA Microphones (**DPA**),
estos dos de micrófonos.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 2):
>
> Electricidad y electrónica aplicada al audio: niveles, impedancias, balanceado, masa, ruido y
> alimentación phantom.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: la ley de Ohm y sus despejes, las unidades de tensión, corriente,
resistencia y potencia, y la tensión y frecuencia de la red; qué es el dBu y a cuántos voltios
equivale, qué es el dBV y el dBFS, cuál es el nivel medio de trabajo profesional, qué es el margen
dinámico (*headroom*) y el factor de cresta, y cómo se reparte la ganancia en una mesa; qué es la
impedancia y en qué se diferencia de la resistencia, por qué hoy se conecta una salida de baja
impedancia a una entrada de alta y no se «adaptan» impedancias, cuánto da un grupo de altavoces en
serie o en paralelo, por qué un altavoz de baja impedancia pierde más en el cable y qué impedancia
tiene un cable AES3; cómo va cableado un XLR y un jack TRS, por qué la línea balanceada rechaza el
ruido y cómo se llama la magnitud que lo mide (CMRR), qué pasa si se cruzan los pines 2 y 3 y qué diferencia hay entre invertir la polaridad y
desfasar; qué es un bucle de masa y una masa en estrella, dónde se conecta la malla en un XLR según la AES y qué remedios
se admiten (y cuál nunca); de dónde viene un zumbido, cómo entra la radiofrecuencia y en qué se
distingue el ruido de la distorsión; y la alimentación *phantom*: tensión, tolerancia, corriente,
pines, a qué micrófonos daña y en qué se diferencia de la A-B. En la prueba práctica: localizar un
zumbido, conectar un equipo doméstico o un instrumento a una mesa profesional, ajustar la ganancia
de una cadena, y dar o quitar *phantom* sin dañar nada.

<!-- indice -->

## Índice

- [1. La base eléctrica: magnitudes, ley de Ohm, red y amplificadores](#1-la-base-eléctrica-magnitudes-ley-de-ohm-red-y-amplificadores)
  - [1.1 Las magnitudes y sus unidades legales](#11-las-magnitudes-y-sus-unidades-legales)
  - [1.2 La ley de Ohm](#12-la-ley-de-ohm)
  - [1.3 La corriente de la red](#13-la-corriente-de-la-red)
  - [1.4 El diferencial y el magnetotérmico](#14-el-diferencial-y-el-magnetotérmico)
  - [1.5 Los amplificadores y sus clases](#15-los-amplificadores-y-sus-clases)
- [2. Niveles](#2-niveles)
  - [2.1 Las escalas: dBu, dBV y dBFS](#21-las-escalas-dbu-dbv-y-dbfs)
  - [2.2 Los niveles de trabajo](#22-los-niveles-de-trabajo)
  - [2.3 Margen dinámico, factor de cresta y sensibilidad de entrada](#23-margen-dinámico-factor-de-cresta-y-sensibilidad-de-entrada)
  - [2.4 La estructura de ganancia](#24-la-estructura-de-ganancia)
- [3. Impedancias](#3-impedancias)
  - [3.1 Qué es la impedancia](#31-qué-es-la-impedancia)
  - [3.2 Salida baja, entrada alta: por qué ya no se adaptan impedancias](#32-salida-baja-entrada-alta-por-qué-ya-no-se-adaptan-impedancias)
  - [3.3 Altavoces en serie y en paralelo](#33-altavoces-en-serie-y-en-paralelo)
  - [3.4 Por qué la impedancia baja hace perder corriente en el cable](#34-por-qué-la-impedancia-baja-hace-perder-corriente-en-el-cable)
  - [3.5 Los cables y sus impedancias](#35-los-cables-y-sus-impedancias)
  - [3.6 Cómo se mide: el multímetro y sus límites](#36-cómo-se-mide-el-multímetro-y-sus-límites)
- [4. Balanceado](#4-balanceado)
  - [4.1 El conector XLR y el jack TRS](#41-el-conector-xlr-y-el-jack-trs)
  - [4.2 Por qué la conexión balanceada rechaza el ruido](#42-por-qué-la-conexión-balanceada-rechaza-el-ruido)
  - [4.3 Polaridad no es fase](#43-polaridad-no-es-fase)
  - [4.4 Balanceado con desbalanceado](#44-balanceado-con-desbalanceado)
- [5. Masa](#5-masa)
  - [5.1 El bucle de masa](#51-el-bucle-de-masa)
  - [5.2 El pin 1: malla a chasis](#52-el-pin-1-malla-a-chasis)
  - [5.3 Los remedios, y el que nunca se usa](#53-los-remedios-y-el-que-nunca-se-usa)
- [6. Ruido](#6-ruido)
  - [6.1 De dónde viene](#61-de-dónde-viene)
  - [6.2 Ruido no es distorsión](#62-ruido-no-es-distorsión)
- [7. Alimentación phantom](#7-alimentación-phantom)
  - [7.1 Qué es y qué norma la regula](#71-qué-es-y-qué-norma-la-regula)
  - [7.2 Las cifras](#72-las-cifras)
  - [7.3 Por qué «fantasma»](#73-por-qué-fantasma)
  - [7.4 Los riesgos](#74-los-riesgos)
  - [7.5 La alimentación A-B, que no es fantasma](#75-la-alimentación-a-b-que-no-es-fantasma)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. La base eléctrica: magnitudes, ley de Ohm, red y amplificadores

El enunciado da por sabida la electricidad de base y pide su aplicación al audio. Este epígrafe la
reúne, porque todo lo demás (niveles, impedancias, masas) se calcula con ella.

### 1.1 Las magnitudes y sus unidades legales

Las cuatro magnitudes de un circuito, con la unidad que el Real Decreto 2032/2009 les asigna:

| Magnitud | Qué es | Unidad legal |
|---|---|---|
| Tensión o diferencia de potencial | La fuerza que empuja a los electrones | Voltio (V) |
| Intensidad o corriente | Cuántos electrones pasan por segundo | Amperio (A) |
| Resistencia | Lo que se opone al paso | Ohmio (Ω) |
| Potencia | Energía por unidad de tiempo | Vatio (W) |

Y no son convención de sector: están en el Boletín Oficial del Estado. El Real Decreto 2032/2009,
de 30 de diciembre, por el que se establecen las unidades legales de medida, recoge en su cuadro de
unidades derivadas coherentes las filas que las definen, con las celdas separadas por puntos porque
un cuadro no se puede entrecomillar de otra manera y cada celda va literal:

> **«diferencia de potencial eléctrico, fuerza electromotriz» · «voltio» · «V» · «W/A»**
>
> **«resistencia eléctrica» · «ohmio» · «Ω» · «V/A»**
>
> **«capacidad eléctrica» · «faradio» · «F» · «C/V»**

El amperio, además, es una de las siete unidades básicas del Sistema Internacional, y no deriva de
ninguna otra.

### 1.2 La ley de Ohm

La ley de Ohm describe la relación entre tensión, corriente y resistencia en un circuito eléctrico.
La fórmula, y las tres maneras de despejarla:

| Se busca | Fórmula |
|---|---|
| Tensión | V = I × R |
| Intensidad | I = V / R |
| Resistencia | R = V / I |

Un ejemplo: un circuito de 5 ohmios que necesita 3 amperios requiere 15 voltios (5 × 3 = 15). La
trampa habitual de estas preguntas no está en la cuenta, sino en las unidades: si las opciones dan
el mismo número en voltios y en vatios, sólo una es correcta. Hay que mirar siempre la unidad de la
opción.

La potencia se obtiene de las mismas magnitudes: P = V × I, y sustituyendo con la ley de Ohm, P =
I² × R o P = V² / R. Es la forma que explica las pérdidas en el cable del epígrafe 3.4.

### 1.3 La corriente de la red

Las redes eléctricas domésticas de la mayoría de los países europeos suministran corriente alterna a
230 voltios.

| | 230 V | 110 V |
|---|---|---|
| Alterna | Europa | Ninguno de los dos habituales |
| Continua | No existe como red doméstica | No existe como red doméstica |

La frecuencia de esa alterna es de 50 hercios en Europa y de 60 en América, y ese dato es el que
explica el zumbido de red: un zumbido de 50 Hz en un equipo de audio europeo delata un problema de
alimentación o de masas (epígrafes 5 y 6).

### 1.4 El diferencial y el magnetotérmico

Un diferencial salta cuando no hay la misma intensidad entre hilos. El interruptor diferencial
compara la corriente que entra por el activo con la que vuelve por el neutro. En un circuito sano
las dos son iguales. Si no lo son, es que parte de la corriente se está yendo por otro camino
—tierra, la carcasa de un equipo, una persona— y el diferencial corta. El diferencial no protege la
instalación: protege a las personas.

| Causa del disparo | Qué aparato actúa |
|---|---|
| El consumo es excesivo | El magnetotérmico, en su parte térmica: protege contra sobrecargas |
| Hay un cortocircuito | El magnetotérmico, en su parte magnética: corta en milisegundos |
| Hay una fuga (no vuelve por el neutro lo que sale por el activo) | El diferencial |

La distinción que hay que llevarse, y que en un plató salva un turno: si salta el magnetotérmico,
hay demasiado consumo o un cortocircuito y se revisa la carga. Si salta el diferencial, hay una fuga
a tierra y se busca el equipo que está derivando. Son dos averías distintas y se buscan de dos
maneras distintas.

### 1.5 Los amplificadores y sus clases

Las clases se definen por el ángulo de conducción, es decir, por qué parte del ciclo de la señal
conduce el transistor de salida:

| Clase | Cuánto conduce | Rendimiento | Distorsión | Dónde se usa |
|---|---|---|---|---|
| A | El ciclo entero —360º— | Bajo | Mínima | Etapas de calidad y previos |
| B | Medio ciclo —180º— | Mayor | Distorsión de cruce | Etapas en contrafase |
| Clase AB | Algo más de medio ciclo | Intermedio | Sin cruce apreciable | La inmensa mayoría de las etapas lineales de audio |
| C | Menos de medio ciclo | Más alto que A, B y AB | Muy alta | Radiofrecuencia, no audio |
| D | Conmuta: el transistor está del todo abierto o del todo cerrado | El más alto | Depende del filtrado | Etapas de potencia en las que el rendimiento manda |

La clase C no sirve para audio: su distorsión es tan grande que la señal sólo se recupera con un
circuito resonante sintonizado, que es justo lo que hay en un transmisor de radiofrecuencia.

La clase D no es una prolongación de la serie A-B-C, sino conmutación. Texas Instruments, en una
nota de aplicación, lo cifra así: **«Class AB exhibits a theoretical peak efficiency of 78%, and is
only 30% - 40% efficient at normal operating levels. Efficiency is where the switching, or Class D,
audio amplifier has large advantages over linear classes»** (la clase AB tiene un rendimiento
teórico máximo del 78 % y sólo del 30 al 40 % a niveles normales; la clase D, conmutada, gana ahí),
y pone el ejemplo de **«a 90% efficient amplifier»** (un amplificador con un rendimiento del 90 %).
La clase D **«outputs a high frequency PWM signal»**: su salida es una señal de alta frecuencia
modulada en anchura de impulsos, que un filtro devuelve a audio.

La etapa de potencia se conecta a la mesa por su sensibilidad de entrada, que es un nivel (epígrafe
2.3), y al altavoz por una impedancia de carga (epígrafe 3.3).

## 2. Niveles

Un nivel es una tensión expresada en decibelios respecto de una referencia. El decibelio es una
razón logarítmica: para tensiones, 20 × log (V / V_ref). Doblar la tensión son unos 6 dB; diez veces
la tensión, 20 dB. Sin la referencia, un número de decibelios no dice nada: por eso cada escala
lleva su letra.

### 2.1 Las escalas: dBu, dBV y dBFS

| Escala | Referencia (0 dB) | Dónde se usa |
|---|---|---|
| dBu | 0,775 V eficaces | Audio analógico profesional |
| dBV | 1 V eficaz | Equipos domésticos y sensibilidad de micrófonos |
| dBFS | La escala completa del convertidor digital | Audio digital |
| dB SPL | El umbral de audición (presión sonora en el aire, no tensión) | Acústica y micrófonos |

El origen de los 0,775 V lo explica Rane (RaneNote 169): **«the definition of dBu is a voltage
reference point equal to 0.775 Vrms (derived from the old power standard of 0 dBm, which equals 1 mW
into 600 Ω)»**: 0 dBu son 0,775 voltios eficaces, la tensión que disipa un milivatio sobre 600
ohmios. De ahí que **«by definition it is an rms level, not a peak level»**: el dBu es un valor
eficaz, y **«It is incorrect to state peak voltage levels in dBu»** (es incorrecto expresar
tensiones de pico en dBu).

El valor eficaz (rms) es la tensión continua que produciría el mismo calor en una resistencia. Para
una senoide, el pico vale 1,414 veces el eficaz.

El dBFS es otra cosa. Rane: **«0 dBFS refers to a digital audio reference level equal to "Full
Scale."»**; **«all signal levels expressed in terms of dBFS are peak levels, and expressed as
negative numbers (since the maximum is 0 dBFS)»**: el dBFS mide picos y siempre es negativo, porque
por encima de 0 dBFS no hay códigos y la señal se recorta. El mismo documento advierte de que un
documento informativo de la AES (AES-2id-2006) define la escala completa de otro modo, sobre el valor eficaz de una senoide, con lo que una
senoide a escala completa leería +3 dBFS: la costumbre y la definición AES no coinciden.

### 2.2 Los niveles de trabajo

| Señal | Nivel | Fuente |
|---|---|---|
| Nivel medio de trabajo profesional | +4 dBu, que en un vúmetro verdadero marca 0 VU | Rane, RaneNote 135 |
| Máximo de un equipo doméstico | Con frecuencia, sólo −10 dBV (316 mV) | Rane, RaneNote 135 |
| Máximo seguro de un equipo profesional | +20 dBu (7,75 V eficaces) | Rane, RaneNote 135 |
| Máximo de un equipo profesional de proceso | +26 dBu | Rane, RaneNotes 135 y 155 |
| Suelo de ruido de los mejores equipos | En torno a −94 dBu | Rane, RaneNotes 135 y 155 |
| Salida de un micrófono | Milivoltios: se da como sensibilidad, en mV/Pa o dBV/Pa | DPA |

Las frases de Rane (RaneNote 135): **«It is normal pro audio practice to set your average level at
+4 dBu (which, incidentally, registers as "0 dB" on a true VU meter)»**; **«since all high quality
pro audio equipment can handle +20 dBu in and out, then this value becomes a safe maximum level for
setting gains, giving you 16 dB of headroom»**; y, del lado doméstico, **«max consumer level is
often only -10 dBV (316 mv)»**. Y sobre el margen total: **«Professional-grade analog signal
processing equipment can output maximum levels of +26 dBu, with the best noise floors being down
around -94 dBu. This gives a maximum unit dynamic range of 120 dB»**. Son cifras de fabricante, no
de norma.

La consecuencia práctica: entre un equipo doméstico y uno profesional hay una diferencia de nivel
grande, además de una diferencia de conexión (desbalanceado frente a balanceado, epígrafe 4). Un
reproductor doméstico conectado a una entrada de línea profesional llega bajo; se sube la ganancia o
se usa una caja de adaptación.

El micrófono entrega mucho menos que una línea. Su salida se expresa como sensibilidad: DPA (que
remite a la norma IEC 60268-4) la define como **«the voltage a microphone generates when placed in a
free sound field at a sound pressure of 1 Pascal (which is the same as a sound pressure level (SPL)
of 94 dB)»**, y se da como **«xx mV per Pascal @ 1 kHz or yy dBV/Pascal @ 1 kHz»**; por ejemplo,
**«10 mV/Pa; -40 dB re. 1 V/Pa»**. Por eso la entrada de micrófono de una mesa tiene un
preamplificador con mucha ganancia y la de línea no. Y por eso una fuente muy fuerte puede saturar
la entrada de micrófono: DPA calcula que un cantante muy fuerte, a 150 dB de pico en los labios, con
micrófonos de 1 y 10 mV/Pa, da **«outputs of 0.63 and 6.3 volt peak! Signals of this magnitude
should instead be handled by the line input or the signal should be attenuated»**: esas tensiones
van a la entrada de línea o con atenuador.

### 2.3 Margen dinámico, factor de cresta y sensibilidad de entrada

El margen dinámico (*headroom*) es lo que queda por encima del nivel de trabajo antes del recorte.
Rane (RaneNote 135): **«Headroom is the ratio of the largest undistorted signal possible through a
unit or system, to that of the average signal level. For example, if the average level is +4 dBu and
the largest level is +26 dBu, then there is 22 dB of headroom»**. El rango dinámico, en cambio, va
del máximo al suelo de ruido (los 120 dB del epígrafe anterior).

El margen hace falta por el factor de cresta, la razón entre el pico y el valor eficaz. Rane
(RaneNote 169): **«Sine waves have a crest factor of 1.4 (or 3 dB)»**; **«Music has a wide crest
factor of 4-10 (12 dB – 20 dB)»**; y **«a square wave represents the extreme where the rms and peak
levels are the same»**. Es decir: una música con nivel eficaz de +4 dBu tiene picos entre +16 y +24
dBu, y por eso se pide un margen de 12 a 20 dB.

La sensibilidad de entrada de una etapa de potencia es el nivel que la lleva a plena potencia. Crown
la ofrece en posiciones: **«For amplifiers with a 0.775V position, this positions corresponds to a 0
dBu level. The 1.4V position corresponds to a +4 dBu level. The 26 dB position is a fixed gain
position.»** (0,775 V corresponde a 0 dBu; 1,4 V, a +4 dBu; la posición de 26 dB es de ganancia
fija). Ojo con la segunda cifra, que es la del fabricante y no la de la escala: con la definición del
epígrafe 2.1, +4 dBu son 0,775 × 10^(4/20) ≈ 1,23 V eficaces (cálculo), y 1,4 V quedan algo por
encima, en unos +5 dBu. Si se pregunta a cuántos voltios equivale +4 dBu, la respuesta es 1,23 V. Rane (RaneNote 135) añade que ese mando no cambia la potencia disponible: **«Amplifier input
sensitivity controls do not change the available output power»**.

### 2.4 La estructura de ganancia

Ajustar la ganancia de una cadena es repartir el nivel para que la señal quede lejos del ruido y
lejos del recorte. La regla de Rane (RaneNote 135): **«take as much gain as necessary to bring the
signal up to the desired average level, say, +4 dBu, as soon as possible. If you need 60 dB of gain
to bring up a mic input, you don't want to do it with 20 dB here, and 20 dB there, and 20 dB some
other place. You want to do it all at once at the input mic stage.»** La ganancia se toma de una
vez, en el previo de micrófono, porque cada etapa añade su ruido y lo que se amplifica tarde
amplifica también el ruido de las etapas anteriores.

Y un matiz de la «ganancia unidad» que confunde en la práctica: Rane (RaneNote 124) explica que
muchos procesadores tienen **«a gain difference of 6 dB between unbalanced and balanced out»**, porque
la salida balanceada activa lleva la señal en fase por un conductor y en contrafase por el otro, y la
diferencia entre ambos es el doble. Como no hay norma que defina la ganancia unidad, **«manufacturers
make their own decision»**, y una cadena con todos los mandos en la marca de 0 dB puede ganar 6 o 12
dB. Rane exceptúa las salidas con transformador y las de etapa de acoplamiento cruzado (*cross-coupled*),
que dan el mismo nivel balanceadas o no. El remedio que da Rane: **«turn the level control down 6 dB»**.

## 3. Impedancias

### 3.1 Qué es la impedancia

La resistencia que se ofrece a una corriente alterna debido a la capacidad, la inductancia y la
resistencia de un circuito se denomina impedancia.

| Concepto | En qué corriente | Qué la produce |
|---|---|---|
| Resistencia | Continua y alterna | Sólo el material del conductor |
| Reactancia | Sólo alterna | La capacidad y la inductancia, que dependen de la frecuencia |
| Impedancia | Alterna | Resistencia y reactancia juntas |

Por qué le importa a un técnico de sonido: porque el audio es corriente alterna. Una señal de audio
cambia de sentido cientos o miles de veces por segundo, así que todo lo que un circuito de audio
opone a la señal es impedancia, no resistencia. Y como la reactancia depende de la frecuencia, la
impedancia de un altavoz o de un micrófono no es la misma a 100 Hz que a 10 kHz: el número que da el
fabricante es un valor nominal.

### 3.2 Salida baja, entrada alta: por qué ya no se adaptan impedancias

Entre equipos de audio de línea se transfiere tensión, no potencia. Rane (RaneNote 124) lo dice sin
rodeos: **«Impedance matching went out with vacuum tubes»**; **«Modern solid-state devices transfer
voltage between products, not power. Optimum power transfer requires impedance matching. Optimum
voltage transfer does not.»**; **«Today's products have high input impedances and low output
impedances»**, y **«Low impedance output stages drive high impedance input stages. This way, there
is no loading, or signal loss, between stages.»**

Las cifras típicas que da Rane son **«around 100 ohms for R OUT and 20k ohms for R IN»**: salida de
unos 100 ohmios contra entrada de unos 20 kiloohmios. Es un divisor de tensión casi sin pérdida
(Rane calcula −0,04 dB). Si se «adaptaran» impedancias, poniendo la entrada también a 100 ohmios, el
divisor sería de la mitad: **«100 ohms driving 100 ohms creates a voltage divider of 1/2»**, **«a
voltage loss of 6 dB»**. La conclusión de Rane: **«Impedance matching is not necessary and creates
many ills»**: baja el nivel y el rango dinámico 6 dB y, por la corriente que exige, empeora la
distorsión y calienta la fuente.

El oficio lo llama conexión en puente (*bridging*): la carga de entrada es muchas veces mayor que la
impedancia de la salida que la ataca. La herencia de los 600 ohmios está sólo en la definición del
dBu (epígrafe 2.1). Donde sí se sigue adaptando la impedancia es en las líneas digitales y de vídeo
(epígrafe 3.5), por otra razón: las reflexiones.

El micrófono entra en la misma lógica: DPA da como regla que la carga sea de 5 a 10 veces la impedancia de la fuente
(con un micrófono de 100 Ω, al menos 500-1.000 Ω), y que eso no es problema, porque **«with
phantom-powered input, … the input impedance is 3.4 kΩ»**.

Y la conversión de impedancia más corriente en un estudio es la caja de inyección directa. Rane
(RaneNote 110): **«Originally named for its use to convert the high impedance, high level output of
an electric guitar to the low impedance, low level input of a recording console, it allowed the
player to plug "directly" into the console. Now this term is commonly used to describe any box used
to convert unbalanced lines to balanced lines.»** La DI pasa de alta a baja impedancia, de nivel de
instrumento a nivel de micrófono y de desbalanceado a balanceado; la que lleva transformador es además la forma habitual del aislamiento de los epígrafes
4.4 y 5.3.

### 3.3 Altavoces en serie y en paralelo

| Montaje | Fórmula con cargas iguales | Tres de 8 Ω |
|---|---|---|
| Serie | Se suman: Z × n | 24 Ω |
| Paralelo | Se divide: Z / n | 2,67 Ω |

Con cargas distintas, en serie se suman y en paralelo se suman sus inversas: 1/Z = 1/Z1 + 1/Z2 + …
Dos altavoces de 8 Ω en paralelo dan 4 Ω; uno de 8 y otro de 4 en paralelo, 2,67 Ω.

Si una pregunta pide el valor «más aproximado» de tres altavoces de 8 ohmios en paralelo y ofrece
2,5 ohmios, ésa es la respuesta: el valor exacto es 2,67 y no está entre las opciones. Se calcula y
se elige el más cercano, sin buscar el redondo.

Y la consecuencia práctica, que es por qué esto se pregunta: al bajar la impedancia, la etapa entrega
más corriente. Una etapa estable hasta 4 ohmios conectada a 2,67 trabaja fuera de especificación y
puede protegerse o quemarse. La cuenta no es un ejercicio de escuela: decide si el montaje se puede
hacer.

El otro dato de la salida de una etapa es el factor de amortiguamiento. Crown: **«Damping factor is
the ratio of the rated speaker impedance to the amplifier's output impedance.»** Por eso la
impedancia de salida de una etapa es muy baja, y por eso un cable largo y fino, que suma su
resistencia a esa salida, lo empeora.

### 3.4 Por qué la impedancia baja hace perder corriente en el cable

En un cable de altavoz habrá más pérdida cuanto menor sea la impedancia del altavoz conectado. El
razonamiento, en tres pasos:

1. A menor impedancia de carga, mayor corriente circula por el circuito, porque la corriente es la
   tensión dividida entre la impedancia total.
2. El cable tiene su propia resistencia, pequeña pero no nula.
3. La pérdida en el cable crece con el cuadrado de la corriente —es I² × R—, así que doblar la
   corriente cuadruplica la pérdida.

De ahí la regla del oficio: cuanto más baja es la impedancia del altavoz, más gruesa tiene que ser
la sección del cable y más corta la tirada. Con 16 ohmios se puede tirar lejos con poca sección; con
4, no. Crown lo resume: **«The longer the run, the heavier gauge you will need to minimize power and
damping factor loss.»**

Y de ahí también la razón de ser de la línea de 100 voltios en megafonía: subiendo la tensión se
baja la corriente para la misma potencia, y con poca corriente la pérdida en el cable deja de
importar.

### 3.5 Los cables y sus impedancias

Un cable de micrófono y un cable AES3 llevan el mismo conector y no son el mismo cable.

| Cable | Impedancia | Para qué |
|---|---|---|
| De micrófono | No está especificada: es audio analógico y la impedancia característica no interviene | Audio analógico balanceado |
| AES3 sobre XLR | 110 ohmios | Audio digital de dos canales |
| AES3 sobre coaxial (AES3id) | 75 ohmios | Audio digital sobre infraestructura de vídeo |
| Vídeo SDI | 75 ohmios | Vídeo digital |

Por qué importa: una señal digital tiene flancos muy rápidos y se comporta como radiofrecuencia. Si
la impedancia del cable no es la del sistema, hay reflexiones, y las reflexiones producen errores de
bit. Un cable de micrófono lleva AES3 unos metros y falla a partir de cierta longitud, sin previo
aviso y de forma intermitente: es una de las averías más difíciles de encontrar. Los conectores y
formatos digitales se estudian en el tema 11.

### 3.6 Cómo se mide: el multímetro y sus límites

Un multímetro corriente no mide impedancia: mide resistencia en continua. Lo que el técnico hace con
él es comprobar la resistencia de continua de una bobina de altavoz o de una línea, que es un valor
próximo a la impedancia nominal pero no el mismo. Medir impedancia de verdad, frecuencia a
frecuencia, exige un puente de impedancias o un analizador. Si un test ofrece multímetro,
osciloscopio, sonómetro y preamplificador como «herramienta para medir la impedancia», la mejor de
las cuatro es el multímetro, con esa salvedad.

| Aparato | Qué mide |
|---|---|
| Multímetro | Tensión, corriente y resistencia; la resistencia, en continua |
| Osciloscopio | La forma de onda en el tiempo: tensión frente a tiempo |
| Sonómetro | El nivel de presión sonora en el aire: no toca el circuito |

## 4. Balanceado

### 4.1 El conector XLR y el jack TRS

Por definición, en un conector XLR de tres pines el cable «vivo» se conecta al pin 2. El reparto
completo, que es lo que hay que memorizar:

| Pin | Qué lleva |
|---|---|
| 1 | Malla o masa |
| 2 | Vivo, señal en fase, también llamado positivo o *hot* |
| 3 | Retorno, señal en contrafase, también llamado negativo o *cold* |

Y la regla que el oficio usa para no olvidarlo: uno, dos, tres: masa, vivo, retorno. Rane (RaneNote
151) recuerda que es convenio de la AES: **«the Audio Engineering Society has adopted the "pin 2 is
hot" standard»**.

El mismo reparto en jack de 6,35 mm, según Crown: **«XLR Pin 1 is ground (shield). Pin 2 is hot
(non-inverting) Pin 3 is low (inverting) 1/4" TRS Tip: hot (non-inverting) Ring: low (inverting)
Sleeve: Shield (ground)»**. Punta, vivo; anillo, retorno; cuerpo, malla. El jack TS, de sólo punta y
cuerpo, no tiene retorno: es desbalanceado.

### 4.2 Por qué la conexión balanceada rechaza el ruido

La señal viaja por dos conductores en oposición de fase. Cualquier interferencia que el cable recoja
por el camino —un zumbido de red, la radiofrecuencia de un transmisor— se induce igual en los dos
conductores. En la entrada, el receptor resta un conductor del otro: la señal, que iba en oposición,
se suma; la interferencia, que iba igual en los dos, se cancela.

Rane (RaneNote 110) lo formula para las corrientes de masa: **«Balanced interconnect was developed to
be immune to these noise currents, which can never be entirely eliminated»**. Y exige un cable
concreto: **«Always use twisted pair cable»**; el par trenzado hace que los dos conductores reciban la
misma interferencia.

La capacidad de una entrada balanceada para rechazar lo que llega igual a los dos conductores se mide
con la relación de rechazo en modo común (CMRR). DPA la define así: **«Common Mode Rejection Ratio (CMRR) expresses the suppression of induced EMI noise on
the terminals of a device. This suppression is possible only if you use balanced lines»** (expresa
cuánto se suprime el ruido electromagnético inducido en los terminales de un equipo, y sólo es posible
con líneas balanceadas). Para eso es importante que **«the impedance measured from pin 2 to ground and from pin 3 to
ground is exactly the same»**, en el equipo que envía, en el que recibe y en el cable, porque **«The
weakest link determines the final result»**. Se da en decibelios, y **«a larger number equals better
data»**: más es mejor. Como ejemplo, DPA da para un previo suyo **«approximately 65 dB»**, que según el
fabricante **«means that less than one thousandth of the noise will pass»** (pasa menos de una
milésima del ruido).

De ahí las consecuencias que un técnico usa a diario:

1. Un cable balanceado puede ser muy largo sin coger ruido. Uno desbalanceado, no.
2. Si un cable tiene el 2 y el 3 cruzados, ese canal entra con la polaridad invertida y al sumarlo
   con otro se cancelan parcialmente. Es la avería que más se busca en un montaje grande.
3. Muchas salidas balanceadas activas entregan 6 dB más que la misma salida usada desbalanceada; no
   las de transformador ni las de acoplamiento cruzado (epígrafe 2.4).

### 4.3 Polaridad no es fase

Invertir la polaridad y desfasar dan un resultado parecido con una senoide, pero no son lo mismo.
DPA: **«Changing the polarity is a simple swap of the negative part becoming positive and the
positive part then becoming negative. The signal is inverted … the signal is multiplied by "-1"»**; y
**«Sometimes, it is said that the phase is shifted by 180°. This is, however, not exactly correct. A
phase shift requires a time shift, i.e., a delay, which is not involved in swopping polarity. On the
other hand, after inversion, the signal is now 180° out of phase»**. Invertir es multiplicar por −1,
sin retardo; desfasar exige un retardo. El resultado de invertir es una señal a 180°, pero la
operación no es un desfase.

El botón de la mesa que invierte la polaridad lleva, según DPA, **«The Greek letter φ»**, que
**«Sometimes, it looks like the letter Ø»**. Y el convenio del pin 2 tiene también sentido acústico:
**«rising pressure on the diaphragm, moving the diaphragm inward, provides a rising positive voltage
on pin 2»** (dato de DPA para micrófonos de condensador profesionales; los dinámicos **«behave a
little differently»**).

Un apunte de trigonometría que sostiene todo esto: una señal senoidal se describe con un seno, cuyo
valor máximo, 1, está a 90 grados.

| Ángulo | Seno | Dónde cae en la onda |
|---|---|---|
| 0º | 0 | Cruce por cero, subiendo |
| 90º | 1 | Pico positivo |
| 180º | 0 | Cruce por cero, bajando |
| 270º | −1 | Pico negativo |

Dos señales iguales a 180 grados se cancelan al sumarse: es el fundamento de la conexión balanceada
y del defecto de polaridad invertida entre dos micrófonos. La fase en acústica se estudia en el tema
1.

### 4.4 Balanceado con desbalanceado

Rane (RaneNote 110) avisa: **«Balanced interconnect is not compatible with unbalanced»**. Unir un
equipo balanceado con uno desbalanceado pierde la inmunidad al ruido y abre la puerta al bucle de
masa (epígrafe 5). Para los sistemas mixtos, Rane recomienda **«use isolation transformers or, if you
can't do that, try the special cable assemblies described here»**, y la caja DI del epígrafe 3.2 es
la forma habitual de hacerlo en un estudio.

## 5. Masa

En audio se llama masa a tres cosas que conviene no confundir: la tierra de protección, que llega
por el tercer hilo del cable de red y protege a las personas; la masa de chasis, la caja metálica
del equipo; y la masa de señal, la referencia de 0 V de los circuitos de audio. La malla del cable
une masas de equipos distintos.

### 5.1 El bucle de masa

Rane (RaneNote 110) describe el mecanismo: **«Ground loops occur when the grounds of the two units
are also tied together in another place: via the third wire in the line cord, by tying the metal
chassis together through the rack rails, etc. These situations create a circuit through which
current may flow in a closed "loop" from one unit's ground out to a second unit and back to the
first. It is not simply the presence of this current that creates the hum -- it is when this current
flows through a unit's audio signal ground that creates the hum»**.

Dicho en castellano: dos equipos quedan unidos por masa por dos caminos (la malla del cable de audio
y la tierra de los enchufes, o el rack), se forma un lazo, y por él circula corriente. El zumbido no
lo produce la corriente en sí, sino que esa corriente pase por la masa de señal. La tensión entre las
masas es baja, pero la impedancia del lazo también, así que la corriente es alta: Rane dice que es
**«thanks to Mr. Ohm»**. Y concluye que **«Almost all cases of noise can be traced directly to ground
loops, grounding or lack thereof»**: casi todo el ruido se debe a bucles de masa o a masas mal
hechas.

Con conexiones balanceadas bien hechas el bucle no llega a oírse: **«The mere presence of this ground
loop current is no cause for alarm if your system uses properly implemented and completely balanced
interconnects, which are excellent at rejecting ground loop and other noise currents»**.

### 5.2 El pin 1: malla a chasis

La AES tiene norma para esto. Rane (RaneNote 110) la nombra: **«AES48-2005: AES standard on
interconnections -- Grounding and EMC practices -- Shields of connectors in audio equipment
containing active circuitry.»** (no se ha leído el texto de la norma ni comprobado si sigue vigente).
Y da la regla: **«Since standard XLR cables come with their shields tied to pin 1 at each end …, this
means equipment using 3-pin, XLR-type connectors must tie pin 1 to the chassis (usually called
chassis ground) -- not the audio signal ground as is most common»**: el pin 1 va al chasis, no a la
masa de señal.

Lo que pasa si no se hace así, que el oficio llama «problema del pin 1», lo explica Rane (RaneNote
151): muchos fabricantes **«connect balanced shields to audio signal ground; pin 1 for 3-pin
(XLR-type) connectors, the sleeve on 1/4" (6.35mm) jacks. Any currents induced into the shield
modulate the ground where the shield is terminated. This also modulates the signal referenced to that
ground»**. La corriente que recoge la malla entra en la masa de señal y se suma al audio.

Dentro de cada equipo, la misma nota de Rane pide que la masa de señal, aunque se divida (por ejemplo,
en analógica y digital), se reúna en un único punto: **«all "divisions" of signal ground connect
together in one place. This is usually called a star grounding scheme»**. Es la masa en estrella. Y
la unión de la masa de señal con el chasis se hace también en un solo sitio: **«can only be done in one
place in each unit. If done twice, one leaves the possibility open that the noise currents will flow
through a path shared by audio»**. Rane recoge **«two schools of thought»** sobre dónde poner el
centro de la estrella: en la fuente de alimentación (**«a point originating at the output of the power
supply as the center of the star»**) o en la masa del conector de entrada (**«simply moves the center
of the star ground to the input jack's ground»**), esta última la más razonable, dice, para equipos
desbalanceados y para los balanceados con jack de 6,35 mm en los que cabe una clavija mono.

La otra nota, la RaneNote 110, añade que unir la malla al chasis en los dos extremos **«also guarantees the best possible
protection from RFI [radio frequency interference] and other noises [neon signs, lighting
dimmers]»**.

### 5.3 Los remedios, y el que nunca se usa

| Remedio | Qué dice el fabricante |
|---|---|
| Quitar la tierra del enchufe | Nunca. **«Safety regulations require that all original grounding means provided from the factory be left intact for safe operation»** (Rane, RaneNote 110) |
| Levantar masa con el conmutador del equipo (*ground lift*) | **«In only a few cases can it be shown that a ground lift switch improves ground related noise»**; **«Ground lifts are simply another Band-Aid to try in case of grounding problems»**: un parche (RaneNote 110) |
| Transformador de aislamiento | **«Transformer isolation and other interface solutions are the best solutions for balanced/unbalanced interconnections»**, aunque caros; **«Even fully balanced systems can require isolation transformers»** (RaneNote 151) |
| Levantar la malla en un extremo | Si se hace, conviene dejar un camino a la radiofrecuencia: **«providing an RF path through a small capacitor connected from the lifted end of the shield to the chassis»** (RaneNote 151) |
| Equipos con alimentador externo | **«Balanced units with outboard power supplies (wall warts …) do not ground the chassis through the line cord. Make sure such units are solidly grounded by tying the chassis to an earth ground»** (RaneNote 110) |

La regla de seguridad es la primera: la tierra de protección del enchufe no se quita nunca para
matar un zumbido. Sin ella, un fallo de aislamiento deja la carcasa en tensión, y el diferencial
(epígrafe 1.4) es lo que queda entre esa carcasa y la persona. La solución de fondo, según Rane,
es el sistema bien hecho: **«an entire system of properly grounded equipment, without ground lift
switches, is guaranteed (yes guaranteed) to be hum free»**.

## 6. Ruido

### 6.1 De dónde viene

Ruido es toda señal que no pertenece al programa y no guarda relación con él. En electrónica de
audio tiene tres orígenes:

| Origen | Cómo suena | Qué se hace |
|---|---|---|
| El propio circuito (ruido térmico de resistencias y semiconductores, ruido propio del micrófono) | Soplido de fondo constante | Estructura de ganancia (epígrafe 2.4) y equipos de menos ruido |
| La red eléctrica, por bucles de masa o inducción | Zumbido a 50 Hz y sus armónicos | Masas (epígrafe 5) y conexión balanceada (epígrafe 4) |
| Radiofrecuencia y equipos ruidosos (reguladores de luz, fluorescentes, transmisores) | Chisporroteo, zumbido con armónicos agudos, voz de una emisora | Balanceado, par trenzado, malla a chasis, separar cables de audio y de potencia |

El zumbido de red suena a 50 Hz en Europa porque ésa es la frecuencia de la red (epígrafe 1.3).
Rane nombra como fuentes de interferencia **«neon signs, lighting dimmers»**, que en un plató son los
reguladores de la iluminación.

El suelo de ruido de un equipo es el nivel mínimo que puede entregar: Rane (RaneNote 135) dice que
**«the minimum output signal is determined by the noise floor of the unit, i.e., it cannot put out a
discernible signal smaller than the noise»**. La relación señal/ruido (S/N) es la distancia en dB
entre el nivel de trabajo y ese suelo; el rango dinámico, la distancia entre el máximo y el suelo
(epígrafe 2.3).

En el micrófono, el ruido propio se da como nivel equivalente. DPA (con la norma IEC 60268-4): **«The
equivalent noise level (also known as the microphone's self-noise) indicates the SPL at which the
microphone produces the same output magnitude as its electrical self-noise»**; con ponderación A,
**«A good result (extremely low noise) on this scale is usually below 15 dB(A)»**. Es materia del tema
3.

### 6.2 Ruido no es distorsión

| Defecto | Qué es |
|---|---|
| Ruido | Señal ajena al programa, que existe aunque no haya programa |
| Distorsión armónica (THD) | El equipo añade armónicos —múltiplos de la frecuencia de entrada— que no estaban en la señal |
| Distorsión de intermodulación | Dos frecuencias presentes se mezclan y aparecen sumas y diferencias que no son armónicos de ninguna |
| Distorsión por transitorios | El equipo no sigue un cambio brusco y rápido de la señal |
| Recorte (sobrecarga) | La señal excede el margen del equipo y se recorta |

Si un amplificador tiene una distorsión armónica total del 0,1 %, significa que el 0,1 % de la señal
consiste en armónicos no presentes en la señal de entrada. El ruido no guarda relación con la señal;
la distorsión armónica es hija de ella. Es la confusión que más buscan las preguntas de test.

La distorsión por transitorios es un problema de velocidad, no de nivel ni de mezcla. Está
relacionada con la velocidad de subida de la etapa —cuántos voltios por microsegundo es capaz de
dar—, y por eso la castiga un platillo o una caja de batería y no un tono sostenido.

## 7. Alimentación phantom

### 7.1 Qué es y qué norma la regula

La alimentación fantasma lleva corriente continua al micrófono por el mismo cable balanceado que
trae la señal. DPA: **«Phantom power is the standard method for powering professional condenser
microphones via the XLR-3 connector and balanced cables»**. La regula una norma IEC, según los dos
fabricantes consultados: **«The standard IEC 61938:2018 outlines the technical specifications. These
specs concern the voltage, the current draw, the impedance, etc.»** (DPA) y **«The technical details
are regulated in the IEC 61938 standard»** (Schoeps). DPA añade que **«The first standard was DIN 45
596 (now superseded by the IEC 61938:2018)»**. El texto de la IEC 61938 no se ha leído: las cifras
que siguen son las que dan los fabricantes.

La inventó Neumann: DPA fecha el invento en 1966, **«in connection with a special delivery to NRK
(Norwegian Broadcasting)»**, la radiotelevisión pública noruega.

### 7.2 Las cifras

| Dato | Valor | Fuente |
|---|---|---|
| Tensión en los pines 2 y 3 | **«+48 volts ±4 volts DC»** | DPA |
| Pin 1 | **«0 volt»** | DPA |
| Nombre abreviado | **«P48»** | DPA |
| Corriente | **«the rated available current of P48 is 7 mA, and 10 mA is the maximum»** | DPA, citando la norma IEC |
| Cómo se inyecta | **«via two resistors, whose value is standardized and must be identical within each channel»** | Schoeps |
| Polo negativo | **«with the negative pole to ground»** | Schoeps |
| Impedancia de una entrada con *phantom* | **«3.4 kΩ»** | DPA |
| Tensiones menores | 12 o 24 V: **«It has previously been an option for designers to choose between 12 volts or 24 volts»** | DPA |
| P12 | **«12 Volts, generally at somewhat higher current»** | Schoeps |

Con tensión menor de la que el micrófono espera, DPA avisa de que **«the microphone's performance is
affected, reducing the max SPL handling and increasing distortion»**: el micrófono admite menos
presión máxima y distorsiona más.

### 7.3 Por qué «fantasma»

La tensión va igual en los pines 2 y 3, con retorno por el 1. Entre el 2 y el 3, que es donde el
micrófono dinámico tiene su bobina, no hay diferencia de tensión: el dinámico no «ve» la
alimentación. DPA: **«The name "phantom power" refers to the "invisibility" when connecting balanced
microphones that do not need external power, like dynamic (moving coil) microphones»**. Y como la
entrada balanceada resta un conductor del otro (epígrafe 4.2), la tensión, igual en los dos,
tampoco llega al audio.

### 7.4 Los riesgos

| Caso | Qué dicen los fabricantes |
|---|---|
| Micrófono dinámico balanceado bien cableado | La *phantom* **«was designed to be safe for microphones that weren't designed to use it, such as dynamic microphones»** (Schoeps) |
| Cableado defectuoso o conexión en caliente | **«However, in unfavorable cases, e.g. faulty wiring, … in particular, plugging or unplugging it while the powering is on»** puede haber daños (Schoeps) |
| Micrófono o cable desbalanceado, micrófono de cinta | **«If an unbalanced and sensitive microphone – like a ribbon microphone – is connected, it may get damaged. So never connect unbalanced microphones or cables to phantom-powered inputs»** (DPA) |

La práctica que de ello se deriva, en palabras de Schoeps: **«it is good general practice to connect
all microphones with the power supply turned off»**: se conecta y se desconecta con la *phantom*
apagada. Y en un reparto pasivo de un micrófono a varias mesas, sólo una debe dar la *phantom*; las
demás la tienen cortada o están aisladas por transformador.

### 7.5 La alimentación A-B, que no es fantasma

La tensión de alimentación A-B, también llamada Tonader, es de 12 voltios.

| Sistema | Tensión | Cómo la manda | A quién alimenta |
|---|---|---|---|
| Fantasma (*phantom*) | 48 V (también 12 y 24 en algunos equipos) | Igual en los pines 2 y 3, con retorno por el 1 | Micrófonos de condensador |
| A-B o Tonader | 12 V | Con polaridad opuesta entre el 2 y el 3 | Micrófonos de reportaje de sistemas antiguos |

La diferencia de fondo, y es la que explica por qué una estropea lo que la otra no: la alimentación
fantasma pone la misma tensión en los dos conductores de señal, así que un micrófono dinámico, que no
la necesita, no la «ve»: para él los dos conductores están al mismo potencial. La A-B, en cambio,
pone doce voltios de diferencia entre los dos conductores, y eso sí atraviesa un micrófono dinámico
y puede dañarlo. Y la P12 de Schoeps no es la A-B: es una fantasma a 12 voltios.

## Normativa que el tema invoca

| Norma | Qué se toma | Redacción |
|---|---|---|
| Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida (BOE núm. 18, de 21/01/2010) | Las filas del cuadro de unidades derivadas del voltio, el ohmio y el faradio (epígrafe 1.1) | Vigente el 24/09/2026: el capítulo II, en la redacción en vigor desde el 30/04/2020 |

Las normas técnicas que el tema nombra (IEC 61938:2018, IEC 60268-4, AES48-2005, DIN 45 596) se
citan a través de los fabricantes que las invocan; su texto no se ha leído.

## Lo que este tema no da, y dónde está

- El texto de la IEC 61938 (*phantom*), de la AES48 (masas) y de la AES3: son de pago. Las cifras de
  *phantom* van con la fuente del fabricante; la AES48 no se ha comprobado vigente.
- El valor de las resistencias de inyección de la *phantom* y un «rango» de tensiones distinto del
  ±4 V de DPA: sólo constan en fuentes de terceros y no se dan.
- Una norma que fije el nivel nominal de línea profesional (+4 dBu) o doméstico (−10 dBV): no se ha
  leído ninguna; las cifras van como práctica profesional con la fuente del fabricante (Rane).
- El nivel de alineación digital (−18 dBFS, EBU R 68), los medidores y la sonoridad: temas 4 y 13.
- Conectores y formatos digitales (AES/EBU, MADI, Dante, SDI): tema 11. Micrófonos, su
  sensibilidad y su ruido propio: tema 3. Etapas, altavoces y cables de altavoz: tema 10.
- Los riesgos eléctricos como materia preventiva: tema 16.
- La instalación eléctrica y de masas de los estudios de la RTVA/CSRTV: no consta en ningún
  documento publicado.

## Trazabilidad

| Fuente | Qué se ha tomado | Leída |
|---|---|---|
| Real Decreto 2032/2009 (BOE-A-2010-927), capítulo II, tabla 3, redacción vigente (en vigor desde el 30/04/2020) | Filas del voltio, ohmio y faradio | En el BOE consolidado, 25/09/2026 |
| Rane, RaneNote 110 «Sound System Interconnection» (1985, rev. 11/2015) | Bucle de masa, AES48 y pin 1, *ground lift*, tierra de seguridad, alimentadores externos, par trenzado, RFI, balanceado frente a desbalanceado, caja DI | 25/09/2026 |
| Rane, RaneNote 151 «Grounding and Shielding Audio Devices» (1995, rev. 2002) | Masa en estrella y sus dos escuelas, unión de señal y chasis en un solo punto, problema del pin 1, «pin 2 is hot», transformadores, malla levantada con condensador | 25/09/2026 |
| Rane, RaneNote 124 «Unity Gain and Impedance Matching: Strange Bedfellows» (1991, rev. 9/97) | Transferencia de tensión, 100 Ω / 20 kΩ, pérdida de 6 dB al adaptar, ganancia unidad balanceada/desbalanceada y sus excepciones | 25/09/2026 |
| Rane, RaneNote 135 «Setting Sound System Level Controls» (1997, rev. 4/05) | +4 dBu y 0 VU, −10 dBV doméstico, +20 y +26 dBu, −94 dBu, *headroom*, estructura de ganancia, sensibilidad de etapa | 25/09/2026 |
| Rane, RaneNote 155 «Dynamics Processors» (2005) | +26 dBu / −94 dBu | 25/09/2026 |
| Rane, RaneNote 169 «No Such Thing as Peak Volts dBu» (2008, rev. 11/2012) | Definición del dBu, dBFS, factor de cresta | 25/09/2026 |
| DPA Microphones, Mic University (E. Bøgh Brixen): «Know the basics about phantom power», «How to read microphone specifications», «10+ statements on condenser microphones versus dynamic mics», «Polarity, phase and delay», «Electromagnetic interference: EMC, RFI immunity and CMRR» | CMRR (definición, igualdad de impedancias, ejemplo de 65 dB), *phantom* (norma, cifras, riesgos, historia), sensibilidad y ruido propio, salida de 0,63 y 6,3 V, polaridad frente a fase | 25/09/2026 |
| Schoeps, «Phantom Power P48/P12» | Norma IEC 61938, resistencias iguales, polo negativo, P12, seguridad y conexión en frío | 25/09/2026 |
| Crown (FAQ de fabricante) | Pines XLR y TRS, factor de amortiguamiento, calibre del cable, sensibilidad de entrada 0,775 V / 1,4 V | 25/09/2026 |
| Texas Instruments, nota AN-1497 | Rendimiento de las clases AB y D | 25/09/2026 |

El resto va como oficio y así se declara: la ley de Ohm y sus despejes, la tensión y frecuencia de la
red, el diferencial y el magnetotérmico, las clases de amplificador A, B, AB y C, la definición de
impedancia y reactancia, la asociación de altavoces, la pérdida en el cable y la línea de 100 V, la
tabla de impedancias de cable, el multímetro, el mecanismo del balanceado y el papel del par trenzado,
el apunte trigonométrico, los tres orígenes del ruido, la clasificación de las distorsiones, la
clase D descrita como conmutación y su uso en etapas de potencia, el reparto de la *phantom* cuando un
micrófono va a varias mesas y la alimentación A-B. Nada de eso se
ha leído en una norma, y el tema no lo presenta como si lo estuviera.
