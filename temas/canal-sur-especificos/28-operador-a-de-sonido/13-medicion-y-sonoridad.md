# Tema 13 del específico de Operador/a de Sonido · Medición y sonoridad

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 13 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Recomendaciones técnicas: EBU R 128 (normalización de sonoridad y pico verdadero máximo), EBU Tech 3341 (medidor en «modo EBU»), EBU Tech 3342 (rango de sonoridad), EBU Tech 3343 (guía de producción con R 128), EBU R 68 (nivel de alineación), EBU Tech 3205-E (medidor de cuasipico, histórico) y UIT-R BS.1770 (algoritmo de sonoridad y de pico verdadero). Documentación de fabricante: RTW (correlación de fase y vectorscopio). Prensa técnica: Sound On Sound (vúmetro). Página histórica de la UIT (nombre del C.C.I.T.T.). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | La vigente el 24/09/2026: EBU R 128-2023 (versión 5, noviembre de 2023), EBU Tech 3341-2023, Tech 3342-2023 (versión 4) y Tech 3343-2023 (versión 4), todas de noviembre de 2023; UIT-R BS.1770-5 (noviembre de 2023); EBU R 68-2000. La Tech 3205-E (1979) se estudia como documento sustituido |
| **Extensión** | 8.700 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Europea de
Radiodifusión (**UER**, en inglés **EBU**, *European Broadcasting Union*), que publica sus
recomendaciones (**R**) y sus documentos técnicos (**Tech**); Unión Internacional de
Telecomunicaciones (**UIT**, en inglés **ITU**) y su sector de radiocomunicaciones (**UIT-R**);
decibelio (**dB**); decibelios referidos a 1 milivatio (**dBm**, la referencia del vúmetro clásico;
las referencias del decibelio, en los temas 1 y 2); decibelios referidos a la escala completa digital (**dBFS**, *decibels relative
to full scale*); decibelios de pico verdadero (**dBTP**, *decibels true peak*), que la UIT escribe
separados (dB FS, dB TP); unidad de sonoridad
(**LU**, *loudness unit*); unidades de sonoridad referidas a la escala completa (**LUFS**, *loudness
units relative to full scale*) y su equivalente de la UIT (**LKFS**, *loudness, K-weighted,
relative to full scale*); las tres lecturas del medidor de sonoridad —momentánea (**M**), a corto
plazo (**S**, *short-term*) e integrada (**I**)—; rango de sonoridad (**LRA**, *loudness range*);
la puerta de medida (*gating*); la ponderación en frecuencia K y la curva B revisada de baja
frecuencia (**RLB**, *revised low-frequency B-curve*); medidor de programa de pico (**PPM**, *peak
programme meter*) y de cuasipico (**QPPM**, *quasi-peak programme meter*); el vúmetro (**VU**,
*volume unit*); nivel máximo permitido (**PML**, *permitted maximum level*); modulación por
impulsos codificados (**PCM**, *pulse code modulation*); canal de efectos de baja frecuencia
(**LFE**, *low frequency effects*); grupo de expertos en imágenes en movimiento (**MPEG**, *Moving
Picture Experts Group*), cuya norma MPEG-1 Layer 2 es un sistema de reducción de datos de audio,
como el Dolby AC-3; el margen entre el nivel de trabajo y la saturación (*headroom*). Los
fabricantes se citan por su nombre comercial: RTW y Dolby.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 13):
>
> Medición y sonoridad: LUFS, EBU R128, picos, loudness, fases y control de calidad.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: por qué se pasó de normalizar por pico a normalizar por sonoridad; qué
significan LUFS, LKFS y LU y en qué se diferencian; qué norma define el algoritmo de medida y en qué
etapas se divide; qué es la ponderación K; qué canales pesan más y cuál se excluye; quién publica la
R 128 y cuál es su versión vigente; cuál es el nivel objetivo, la tolerancia del directo, la
tolerancia de medida y el pico verdadero máximo; qué diferencia hay entre el pico de muestra y el
pico verdadero y cómo se mide éste; qué miden el vúmetro y el PPM, con qué tiempos, y por qué
ninguno sirve para la sonoridad; a qué nivel se alinea el tono y qué marca en un medidor de
sonoridad; qué pasó con el PML de −9 dBFS; cuáles son las tres lecturas del medidor, sus ventanas
y cuál lleva puerta; qué umbrales tiene la puerta; qué escalas ofrece un medidor en «modo EBU»;
qué es el LRA y cómo se calcula; qué mide un correlador de fase y qué indica cada valor; cómo se lee un goniómetro; qué
tolerancia admite la R 128 en control de calidad y qué metadatos de sonoridad son sospechosos. En
la prueba práctica: leer un medidor de sonoridad y decidir si un programa cumple; ajustar la
sonoridad de un directo; alinear una cadena con tono; comprobar la compatibilidad mono de una
mezcla; revisar un fichero antes de entregarlo a emisión.

<!-- indice -->

## Índice

- [LUFS](#lufs)
  - [Por qué la sonoridad y no el pico](#por-qué-la-sonoridad-y-no-el-pico)
  - [Cómo se mide: el algoritmo de la UIT-R BS.1770](#cómo-se-mide-el-algoritmo-de-la-uit-r-bs1770)
  - [LUFS, LKFS y LU](#lufs-lkfs-y-lu)
- [EBU R 128](#ebu-r-128)
  - [Qué es y qué versión rige](#qué-es-y-qué-versión-rige)
  - [Lo que fija la R 128](#lo-que-fija-la-r-128)
  - [La tolerancia del directo](#la-tolerancia-del-directo)
  - [Los documentos que acompañan a la R 128](#los-documentos-que-acompañan-a-la-r-128)
- [Picos](#picos)
  - [Pico de muestra y pico verdadero](#pico-de-muestra-y-pico-verdadero)
  - [Por qué −1 dBTP y no 0](#por-qué-1-dbtp-y-no-0)
  - [Los medidores clásicos: vúmetro y PPM](#los-medidores-clásicos-vúmetro-y-ppm)
  - [La alineación: −18 dBFS y el fin del −9 dBFS](#la-alineación-18-dbfs-y-el-fin-del-9-dbfs)
- [Loudness: el medidor de sonoridad](#loudness-el-medidor-de-sonoridad)
  - [Las tres lecturas: M, S e I](#las-tres-lecturas-m-s-e-i)
  - [La puerta de la sonoridad integrada](#la-puerta-de-la-sonoridad-integrada)
  - [Las escalas del medidor: EBU +9 y EBU +18](#las-escalas-del-medidor-ebu-9-y-ebu-18)
  - [El rango de sonoridad (LRA)](#el-rango-de-sonoridad-lra)
  - [Sonoridad y compresión](#sonoridad-y-compresión)
- [Fases](#fases)
  - [La correlación de fase](#la-correlación-de-fase)
  - [Fase y sonoridad: el tono en los dos canales](#fase-y-sonoridad-el-tono-en-los-dos-canales)
- [Control de calidad](#control-de-calidad)
  - [Lo que la R 128 exige al control de calidad](#lo-que-la-r-128-exige-al-control-de-calidad)
  - [Los metadatos de sonoridad](#los-metadatos-de-sonoridad)
  - [La revisión de un programa, paso a paso](#la-revisión-de-un-programa-paso-a-paso)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## LUFS

### Por qué la sonoridad y no el pico

Durante décadas los programas se ajustaron por su pico. La EBU R 128 parte de que **«peak
normalisation of audio signals has led to considerable loudness differences between programmes and
between broadcast channels»**, y de que esas diferencias **«are the cause of the most
viewer/listener complaints»**. Lo que el espectador percibe no es el pico, sino la sonoridad: lo
fuerte que suena el programa en conjunto. Y el medidor clásico, usado para leer picos, no la mide: el **«QPPM
(Quasi-Peak Programme Meter) specified in EBU Tech 3205-E [1] does not reflect the loudness of an
audio signal»**.

La razón es que un medidor de picos mide el instante más alto y el oído no oye instantes: oye
promedios ponderados. Una emisión muy comprimida tiene el mismo pico que una sin comprimir y suena
mucho más fuerte, porque todo su contenido está pegado al techo.

| Se mide | Qué contesta | Con qué se mide |
|---|---|---|
| Pico | ¿Me paso del máximo técnico? | Picómetro, dBFS, dBTP |
| Sonoridad | ¿Cómo de fuerte lo va a percibir el oyente? | Medidor de sonoridad, LUFS |

Las dos preguntas hay que contestarlas a la vez, y así está construida la R 128: **«The EBU
recommends the measurement of the average loudness of a programme ('Programme Loudness') for the
normalisation of audio signals. The 'Maximum True Peak Level' of an audio signal should be used to
check compliance with the upper technical limit of the signal chain.»** La sonoridad media del
programa sirve para normalizarlo; el pico verdadero máximo, para no pasar del techo de la cadena.
La misma recomendación añade tres medidas más para caracterizar la señal: el rango de sonoridad y
las sonoridades máximas momentánea y a corto plazo (se ven en «Loudness: el medidor de sonoridad»).

### Cómo se mide: el algoritmo de la UIT-R BS.1770

La medida de sonoridad no la define la UER, sino la UIT. La R 128 lo reconoce en sus
considerandos: **«measuring audio programme loudness has been defined in ITU-R BS.1770 [3], introducing
the measures LU (Loudness Unit) and LUFS (Loudness Units, referenced to Full Scale)»**. La versión
vigente es la UIT-R BS.1770-5, de noviembre de 2023, titulada **«Algorithms to measure audio
programme loudness and true-peak audio level»**: un mismo documento para la sonoridad y para el
pico verdadero. Las versiones −0 (2006) a −4 (2015) están sustituidas.

Su alcance: el algoritmo del anexo 1 se usa para programas **«produced with up to five main channels
per Recommendation ITU-R BS.775 (mono source, stereo and 3/2 multichannel sound)»**; para más
canales (las configuraciones de la UIT-R BS.2051), el anexo 3; y para audio basado en objetos, o
en canales y objetos combinados, el anexo 4.

El anexo 1 describe el algoritmo en cuatro etapas: **«"K" frequency weighting; – mean square
calculation for each channel; – channel-weighted summation (surround channels have larger weights,
and the LFE channel is excluded); – gating of 400 ms blocks (overlapping by 75%), where two
thresholds are used: – the first at −70 LKFS; – the second at −10 dB relative to the level measured
after application of the first threshold»**.

| Etapa | Qué hace |
|---|---|
| 1. Ponderación K | Filtra cada canal para parecerse a cómo oye el oído |
| 2. Valor cuadrático medio | Calcula la energía de cada canal filtrado |
| 3. Suma ponderada de canales | Suma los canales con su peso; los envolventes pesan más y el LFE no cuenta |
| 4. Puerta | Divide la señal en bloques de 400 ms solapados un 75 % y descarta los bloques por debajo de dos umbrales: −70 LKFS y, después, 10 dB por debajo del nivel medido con el primero |

**La ponderación K.** Lo que hace de la sonoridad una medida distinta del nivel es que va
ponderada. Según la BS.1770, **«The K-weighting filter is composed of two stages of filtering; a
first stage shelving filter and a second stage high-pass filter»**. La primera etapa, un filtro de
estantería, **«accounts for the acoustic effects of the head, where the head is modelled as a rigid
sphere»**; la segunda, un filtro paso alto, es la ponderación RLB. Las dos juntas forman lo que la
norma llama ponderación K. En la práctica, el filtro paso alto resta peso a los graves más
profundos. Por eso un bombo enorme sube menos los LUFS de lo que sube el picómetro.

**El peso de cada canal.** La tabla 3 de la BS.1770 da los coeficientes de los cinco canales
principales; la exclusión del LFE no está en esa tabla, sino en la descripción de las etapas del
anexo 1 (**«The low frequency effects (LFE) channel is not included in the measurement»**):

| Canal | Peso |
|---|---|
| Izquierdo, derecho y central | **1.0 (0 dB)** |
| Envolvente izquierdo y envolvente derecho | **1.41 (~ +1.5 dB)** |
| LFE | Excluido de la suma (anexo 1, no tabla 3) |

La Tech 3343 explica el porqué del peso de los envolventes: **«Humans appear to perceive direct
sounds coming from the back louder than frontal ones with the same sound pressure level»**. Y
confirma la exclusión del LFE: **«the LFE channel of a 5.1 Surround Sound mix is excluded from the
loudness measurement»**.

**Límites del algoritmo.** La BS.1770 advierte de que la medida es una estimación: **«measured
loudness is an estimation of subjective loudness and involves some degree of uncertainty»**, y de
que **«the algorithm is not, in general, suitable for use to estimate the subjective loudness of
pure tones»**.

### LUFS, LKFS y LU

LUFS significa unidades de sonoridad referidas a la escala completa. La UIT, en la BS.1770, usa
otro nombre para lo mismo, LKFS, que **«signifies: Loudness, K-weighted, relative to nominal full
scale»**. La R 128 lo aclara en su nota 1: **«'LUFS' is equivalent to 'LKFS' (which is used in
ITU-R BS.1770). The EBU uses 'LUFS' which is compliant with international naming conventions.»**
Son la misma unidad: la UER dice LUFS; la UIT, LKFS.

Y las dos unidades que hay que separar, porque se confunden todo el rato:

| Unidad | Qué es | Cuándo se usa |
|---|---|---|
| LUFS | Una medida ABSOLUTA, referida a la escala completa | «Este programa está a −23 LUFS» |
| LU | Una medida RELATIVA: una diferencia | «Le faltan 2 LU», o «la tolerancia es ±1 LU» |

Un LU y un decibelio valen lo mismo: son la misma escala logarítmica. La diferencia no es de
tamaño, es de si el número apunta a un absoluto o a una diferencia. Lo dicen las dos fuentes: la
Tech 3341, **«1 LU is equivalent to 1 dB»**; la BS.1770, que **«an increase in the level of a
signal by 1 dB will cause the loudness reading to increase by 1 LKFS»**.

**El punto de referencia.** La BS.1770 fija qué marca un tono: **«If a 0 dB FS, 1 kHz (997 Hz to be
exact …) sine wave is applied to the left, centre, or right channel input, the indicated loudness
will equal −3.01 LKFS»**. La constante de su fórmula, −0,691, está para eso: **«cancels out the
K-weighting gain for 997 Hz»**. Es decir, un tono a escala completa en un solo canal frontal marca
−3,01 LUFS; si baja 1 dB, la lectura baja 1 LU (cálculo sobre la cifra de la norma).

## EBU R 128

### Qué es y qué versión rige

La R 128 es una recomendación de la UER, no de la Sociedad de Ingeniería de Audio (AES, *Audio
Engineering Society*), aunque a veces se la cite así. Su portada: **«R 128 LOUDNESS NORMALISATION
AND PERMITTED MAXIMUM LEVEL OF AUDIO SIGNALS · Status: EBU Recommendation · Geneva · November
2023»**. Su objeto está en el título: normalizar la sonoridad de las señales de audio y fijar su
nivel máximo permitido.

Ha tenido cinco versiones. Su historial:

| Versión | Fecha | Cambio |
|---|---|---|
| Primera | **February 2010** | Publicación |
| V2 | **August 2011** | **«relative gate changed from −8 to −10 LU»** |
| V3 | **June 2014** | **«Target level (−23 LUFS) tolerance changed to ± 0.5 LU (except Live-programmes)»** |
| V4 | **August 2020** | **«Tolerances updates and references to R 128 s1 and s2 added»** |
| V5 | **November 2023** | **«References to R 128 s3, s4 and Tech 3401 added»** |

La vigente es la V5, de noviembre de 2023.

Sus considerandos explican el cambio de modelo: la normalización por pico ha causado diferencias de
sonoridad entre programas y entre canales, que son la causa de la mayoría de las quejas del público;
el QPPM de la Tech 3205-E no refleja la sonoridad; y además **«the permitted maximum level of an
audio signal specified in ITU-R BS.645 [2] is no longer appropriate»**.

### Lo que fija la R 128

Lo que fija la R 128 (versión 5, noviembre de 2023):

| Punto | Lo que dice |
|---|---|
| h) Nivel objetivo | **«the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS. Where attaining the Target Level is not achievable practically (for example, live programmes), a tolerance of ±1.0 LU is permitted.»** |
| i) Tolerancia de medida | **«a tolerance of ±0.2 LU is allowed in order to take account of measurement errors»** |
| m) Pico verdadero | **«the True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during production (linear audio)»**; tolerancia de medida de **«±0.3 dB (for signals with a bandwidth limited to 20 kHz)»** |
| k) Medidor | Conforme a la UIT-R BS.1770 y a la EBU Tech 3341 |
| n) Margen de sonoridad (LRA) | Según la EBU Tech 3342; nota 2: **«For programmes shorter than 1 minute, the use of the measure Loudness Range is not recommended»** |

Las tres cifras que hay que saber de memoria son −23 LUFS, ±1 LU y −1 dBTP. Y el resto del
articulado que un operador aplica:

| Punto | Lo que dice |
|---|---|
| h), final | **«A broadcaster should ensure that a deviation from the Target Level towards the limits of the tolerance does not become standard practice»** |
| j) Objetivo más bajo a propósito | **«in special cases the Programme Loudness Level may be normalised to a Target Level lower than −23.0 LUFS on purpose. This exception shall be clearly indicated to ensure that such a lower Programme Loudness Level is not compensated»** |
| k) Medidor, completo | **«the measurement shall be made with a loudness meter compliant with ITU-R BS.1770 (including the level-gating method described in equation (7)) and EBU Tech 3341»** |
| l) Todo el programa | **«the audio signal shall generally be measured in its entirety, without emphasis on specific foreground elements such as speech, music or sound effects»** |
| m), final | **«Permitted Maximum True Peak Levels may be lower for different distribution systems and data reduction rates. A broadcaster should check EBU Tech 3344 [5] for details»** |
| o) Máximos | Las sonoridades máximas momentánea y a corto plazo **«may be used to determine if a programme exceeds the upper loudness tolerance limit of the target audience»** |
| p) Metadatos | **«Loudness Metadata shall correctly indicate the actual Programme Loudness»** |

Tres matices que un tribunal puede usar como trampa:

1. El −1 dBTP es **«during production (linear audio)»**: en producción y con audio sin reducir.
   Tras un códec puede hacer falta un techo más bajo (se ve en «Por qué −1 dBTP y no 0»).
2. El punto l) quiere decir que se mide el programa entero, no sólo la voz: la R 128 no normaliza
   por diálogo.
3. «Programa» incluye la publicidad. Las definiciones de la R 128 cuentan como programa **«An
   advertisement (commercial), trailer, promotional item ('promo'), interstitial or similar item
   ("Short-form Content")»**. La sonoridad del programa se define como **«The integrated loudness
   over the duration of a programme»**.

### La tolerancia del directo

La tolerancia de ±1 LU es para cuando alcanzar el objetivo **«is not achievable practically (for
example, live programmes)»**. Un programa grabado se puede medir entero y ajustar. Un directo no:
su sonoridad integrada no se conoce hasta que termina. El operador de un directo trabaja con la
lectura a corto plazo y con la integrada que va acumulando, y corrige sobre la marcha para acabar
dentro de −23 ± 1 LUFS, es decir, entre −24 y −22 LUFS (oficio y cálculo).

La Tech 3343 da un caso de aplicación en deportes: la voz de los comentaristas puede quedar algo
por debajo del objetivo, **«(for example, at −24 LUFS), so that unexpected crowd noise has more room
to move»** (§ 3.5.1).

Para un tribunal, el dato que más se pregunta es el nivel objetivo: −23 LUFS, con ±1 LU en directo.
La ficha de revisiones de la propia R 128 menciona una tolerancia de ±0,5 LU introducida en 2014;
el articulado vigente de 2023 no la recoge, y manda el articulado.

### Los documentos que acompañan a la R 128

La R 128 remite a una familia de documentos. Este tema desarrolla los cuatro primeros; de los
demás sólo consta, por la propia R 128, su existencia y su objeto:

| Documento | Objeto |
|---|---|
| UIT-R BS.1770 | Algoritmo de sonoridad y de pico verdadero |
| EBU Tech 3341 | El medidor en «modo EBU»: lecturas, escalas, puerta |
| EBU Tech 3342 | El rango de sonoridad (LRA) |
| EBU Tech 3343 | Guía de producción de programas con la R 128 |
| EBU Tech 3344 | Distribución y reproducción |
| EBU R 128 s1 | Contenido corto: anuncios, promociones |
| EBU R 128 s2 | Distribución por *streaming* |
| EBU R 128 s3 y EBU Tech 3401 | La sonoridad en radio |
| EBU R 128 s4 | Contenido cinematográfico |

## Picos

### Pico de muestra y pico verdadero

En digital, el máximo absoluto es 0 dBFS: el mayor número que el sistema puede escribir. Por encima
no hay más; la señal se recorta. Por eso los niveles digitales son negativos, y el nivel de
referencia se fija por debajo de ese techo.

Un medidor de pico de muestra lee el valor de la muestra más alta, en dBFS. Pero la señal que sale
del convertidor no son muestras sueltas: es la onda reconstruida entre ellas. La BS.1770 explica
por qué hace falta otra medida en sus considerandos: **«that digital media overloads abruptly, and
thus even momentary overload should be avoided»**; **«that peak signal levels may increase due to
commonly applied processes such as filtering or bit-rate reduction»**; y **«that existing metering
technologies do not reflect the true-peak level contained in a digital signal since the true-peak
value may occur between samples»**.

La R 128 define ese pico: **«Maximum True Peak Level: The maximum value of the audio signal waveform
of a programme in the continuous time domain»**. Se mide en dBTP: la BS.1770 pide dar el resultado **«in the units of dB TP»**, decibelios referidos al
100 % de la escala completa, en medida de pico verdadero.

**Cómo lo mide el medidor de pico verdadero** (BS.1770, anexo 2):

1. Atenúa la señal: **«The first step consists of imposing an attenuation of 12.04 dB (2-bit
   shift)»**, para dar margen al procesado posterior si se hace con aritmética de enteros; si los
   cálculos se hacen en coma flotante, este paso **«is not necessary»**.
2. Sobremuestrea: **«The 4 × over-sampling filter increases the sampling rate of the signal from 48
   kHz to 192 kHz»**; y **«for an incoming signal at 96 kHz sample rate a 2 × over-sampling would be
   sufficient»**. La señal sobremuestreada **«more accurately indicates the actual waveform that is
   represented by the audio samples»**.
3. Filtra (paso bajo), toma el valor absoluto, compensa la atenuación inicial de 12,04 dB y
   expresa el resultado en dBTP: ése es el pico verdadero.

| Medidor | Qué lee | Unidad |
|---|---|---|
| Pico de muestra | La muestra más alta | dBFS |
| Pico verdadero | El máximo de la onda reconstruida, por sobremuestreo | dBTP |

Aun sobremuestreando, el medidor puede quedarse algo corto. La Tech 3343 lo cuantifica: **«It is
only necessary to leave a headroom of 1 dB below 0 dBFS to still accommodate the potential
under-read of about 0.5 dB (for a 4x oversampling true-peak meter; basic sample rate: 48 kHz)»**.

### Por qué −1 dBTP y no 0

Por qué no cero, que es lo que parecería lógico: porque el pico real no es el pico de las
muestras. Entre dos muestras la onda reconstruida puede pasar por encima de las dos, así que una
señal que en muestras marca 0 dBFS puede tener un pico real superior. Ese exceso lo descubre el
codificador de emisión y lo convierte en distorsión. El decibelio de margen es lo que lo evita.

El techo de −1 dBTP es para audio lineal en producción. Con reducción de datos el pico sube (lo
dice la BS.1770: el pico puede aumentar con la **«bit-rate reduction»**), y la R 128 admite techos
más bajos según el sistema de distribución. La Tech 3343 lo concreta: para dos sistemas de
reducción de datos muy usados en Europa, MPEG-1 Layer 2 y Dolby AC-3, el límite recomendado es −2
dBTP.

La herramienta que hace cumplir el techo es el limitador de pico verdadero al final de la cadena
(el limitador, en el tema 5).

### Los medidores clásicos: vúmetro y PPM

Antes de la sonoridad, el nivel se leía con dos instrumentos que siguen en muchas mesas:

| Medidor | Qué mide | Cómo responde | Fuente |
|---|---|---|---|
| Vúmetro | Un promedio: se aproxima a la sensación de volumen | Lento: agujas de subida y bajada de unos 300 ms | Prensa técnica |
| PPM de la UER (QPPM) | El cuasipico | En modo normal, tiempo de integración de 10 ms; cae de +12 a −12 en 2,8 s (3,8 s en modo lento) | EBU Tech 3205-E |
| Pico de muestra | La muestra más alta | Instantáneo en muestras | — |
| Pico verdadero | La onda reconstruida | Sobremuestreo | UIT-R BS.1770 |
| Sonoridad | La sonoridad ponderada | Tres ventanas: M, S, I | EBU Tech 3341 |

**El PPM de la UER.** La Tech 3205-E (2.ª edición, 1979) lo define, en su modo normal, como **«a
quasi-peak-reading instrument having a nominal integration time of 10 ms»**, con tolerancia **«10 ±2
ms»**; si se retira de golpe un tono que marcaba +12, la aguja cae **«to the -12 mark in 2.8 ±0.3
s»** en modo normal. Su escala tiene **«twelve approximately
equal 2 dB divisions»**, y su marca «Test», 0 dB referida a 0,775 V, está **«9 dB below the maximum
amplitude»** de las señales de programa que las recomendaciones del Comité Consultivo Internacional Telefónico y Telegráfico de la UIT (C.C.I.T.T.; en inglés, *International Telephone and Telegraph Consultative Committee*) permiten
en los circuitos internacionales de programas sonoros: no es el máximo del medidor. La Comisión Electrotécnica Internacional (CEI, en inglés IEC) reconoce tres tipos de
PPM, **«types I, IIa and IIb»**, y **«the latter corresponds to the standard E.B.U. meter»**. El
tiempo de integración se define con una ráfaga de 5 kHz que, aplicada de forma continua, marcaría
+9: si dura el tiempo de integración, **«results in an indication of +7»**, 2 dB menos. Un
transitorio breve no llega a marcar su valor entero: por eso es de cuasipico y no llega al pico
verdadero. La EBU R 68 lo cuantifica: **«due to the characteristics of quasi-peak programme meters
used by broadcasters, the true programme peaks can be 3 dB greater than those indicated»**. La Tech 3205-E es hoy un documento histórico; una nota al comienzo
dice **«This Technical Document is now
superseded by EBU R128»**.

**El vúmetro.** Según la prensa técnica (Sound On Sound, 2024), sus agujas, relativamente lentas
**«(300ms)»**, registran mejor los sonidos graves y sostenidos que los picos breves; y en el instrumento original, con su atenuador a 0, **«a steady
tone of +4dBm at the input … gave an indication of 0VU»**. Su especificación básica, publicada en
1940, **«remains in use today»**; la norma de la CEI que la recoge no se ha leído.

El vúmetro no protege contra el recorte —es demasiado lento— y el picómetro no dice cómo de fuerte
suena. Hacen falta los dos tipos de lectura, y por eso la R 128 fija un objetivo de sonoridad y un
techo de pico verdadero.

### La alineación: −18 dBFS y el fin del −9 dBFS

La EBU R 68 recomienda que sus miembros usen **«coding levels for digital audio signals which
correspond to an alignment level which is 18 dB below the maximum possible coding level of the
digital system, irrespective of the total number of bits available»**; la nota 2 lo precisa:
**«corresponding to a ratio of 1:8 (18.06 dB)»**. La EBU Tech 3343 (§ 8.1) lo aplica al tono:
**«An Alignment Signal in broadcasting consists of a sine-wave signal at a frequency of typically
1 kHz, which is used to technically align a programme’s audio path. In digital systems the level of
such an Alignment Signal is 18 dB below the maximum coding level, irrespective of the total number
of bits available (−18 dBFS).»**

El nivel máximo permitido de −9 dBFS ha cambiado con la sonoridad. Dice la Tech 3343 (§ 8.1) que,
con el paso al **«Maximum Permitted True-Peak Level» (−1 dBTP in production for generic PCM
signals) the recommended PML of −9 dBFS in ITU-R BS.645 becomes obsolete**. Lo que no cambia es la
alineación: **«The switch to loudness normalisation does NOT change this approach»**, y **«electrical
alignment for sound-programme exchange can be performed as usual, with a sine-wave signal of 1 kHz
at a level of −18 dBFS.»**

El tono se alinea con un medidor de pico, no con el de sonoridad: la Tech 3343 lo dice expresamente
(**«The EBU therefore recommends using a peakmeter for alignment.»**). Lo que marca el tono en un
medidor de sonoridad se ve en «Fase y sonoridad: el tono en los dos canales». La reserva de 18 dB,
su origen en los medidores de cuasipico y el margen de trabajo (*headroom*) se desarrollan en el
tema 5.

## Loudness: el medidor de sonoridad

*Loudness* es el término inglés de sonoridad. El medidor que la R 128 exige es el definido por la
EBU Tech 3341, el medidor en «modo EBU» (*EBU Mode*).

### Las tres lecturas: M, S e I

La Tech 3341 (§ 2.1) nombra las tres escalas temporales: **«The shortest time scale is called
'Momentary', abbreviated 'M'. The intermediate time scale is called 'Short-term', abbreviated 'S'.
The programme- or segment-wise time scale is called 'Integrated', abbreviated 'I'»**.

| Lectura | Abreviatura | Ventana | ¿Puerta? |
|---|---|---|---|
| Momentánea (*Momentary*) | M | **«a sliding rectangular time window of length 0.4 s»** | **«The measurement is not gated.»** |
| Corto plazo (*Short-term*) | S | **«a sliding rectangular time window of length 3 s»** | **«The measurement is not gated.»** |
| Integrada (*Integrated*) | I | Todo el programa o el tramo medido, desde que se arranca la medida | Sí: **«uses gating as described in ITU-R BS.1770»** |

Para qué sirve cada una en el trabajo diario (oficio):

- La M, de 400 ms, enseña lo que pasa ahora: es la que se mueve con la música.
- La S, de 3 s, enseña la tendencia: es la que se mira para mezclar.
- La I es la cifra del programa, la que tiene que dar −23 LUFS: es la que se entrega.

Otros requisitos del medidor. La Tech 3341 (§ 2.2): en los medidores en directo (*live meters*), la
lectura a corto plazo se actualiza a **«at least 10 Hz»** y la integrada a **«at least 1 Hz»**; el
medidor debe permitir, como mínimo, **«start/pause/continue the measurement of Integrated Loudness
and Loudness Range simultaneously»** (pasar de «en marcha» a «en espera» y a la inversa) y poner a
cero a la vez la integrada y el LRA, **«regardless of whether the meter is in the ‘running’ and
‘stand-by’ state»**. La misma Tech 3341, ya en su § 2.1: el medidor **«shall be able to display the maximum value of the ‘Momentary
Loudness’ and of the ‘Short-term Loudness’»**, que son los máximos del punto o) de la
R 128.

### La puerta de la sonoridad integrada

Qué es la puerta y por qué existe: la sonoridad integrada de un programa no debe contar los
silencios. Si contara, una película con muchos pasajes callados daría una cifra bajísima y habría
que subirla entera hasta que los diálogos gritaran. La puerta descarta lo que está por debajo de
un umbral, y así la cifra integrada refleja el material que de verdad suena.

La Tech 3341 (§ 2.3) la fija con dos umbrales: la integrada se mide **«using an absolute 'silence'
gating threshold at −70 LUFS for the computation of the absolute-gated loudness level; using a
relative gating threshold, 10 LU below the absolute-gated loudness level»**, sobre **«400 ms blocks
with a constant overlap between consecutive gating blocks of 75%»**.

| Umbral | Valor | Qué hace |
|---|---|---|
| Absoluto | −70 LUFS | Descarta los bloques de silencio |
| Relativo | 10 LU por debajo de la sonoridad calculada con el absoluto | Descarta los pasajes muy flojos respecto al resto del programa |

El proceso, en orden: se mide la sonoridad con los bloques que superan −70 LUFS; se resta 10 a ese
resultado para obtener el umbral relativo (la BS.1770: **«subtracting 10 from the result»**); y la
sonoridad integrada final se calcula sólo con los bloques que superan ese umbral relativo. El umbral
relativo era de −8 LU hasta que la versión 2 de la R 128 (2011) lo cambió a −10 LU.

Y la clave para no equivocarse es a qué lectura se le aplica:

| Escala | ¿Puerteada? | Por qué |
|---|---|---|
| M —momentánea— | No | Es un instrumento de lectura instantánea: tiene que enseñar lo que hay |
| S —corto plazo— | No | Lo mismo: es lectura, no promedio de programa |
| I —integrada— | SÍ, con dos umbrales | Es la cifra del programa: sin puerta, los silencios la falsearían |

Si una pregunta ofrece «−70 LU» o «−10 LU» como la puerta de la lectura a corto plazo, es falsa:
esos umbrales son de la integrada (y del LRA, con otro relativo), y la S no tiene puerta.

### Las escalas del medidor: EBU +9 y EBU +18

El medidor puede ser sólo numérico; si muestra una escala, la Tech 3341 (§ 2.7) obliga a ofrecer
dos, que elige el usuario: **«range −18.0 LU to +9.0 LU (−41.0 LUFS to
−14.0 LUFS), named 'EBU +9 scale'; range −36.0 LU to +18.0 LU (−59.0 LUFS to −5.0 LUFS), named
'EBU +18 scale'»**. La de uso por defecto es la primera: **«The 'EBU +9 scale' shall be used by
default»**.

| Escala | En LU | En LUFS | Uso (oficio) |
|---|---|---|---|
| EBU +9 | −18 a +9 LU | −41 a −14 LUFS | Programas de dinámica normal: más resolución alrededor del objetivo |
| EBU +18 | −36 a +18 LU | −59 a −5 LUFS | Material de mucha dinámica o muy fuerte |

El cero de la escala relativa es el objetivo: **«the target loudness level shall be −23.0 LUFS = 0.0
LU (as defined in EBU R 128)»**. El medidor tiene que ofrecer la escala relativa y la absoluta, y
**«The unit, whether LUFS or LU, shall be displayed for all values and scales, at all times»**.

Pasar de una a otra es sumar o restar 23: −20 LUFS son +3 LU; −26 LUFS son −3 LU (cálculo).

### El rango de sonoridad (LRA)

La Tech 3342 define el LRA: **«Loudness Range (abbreviated 'LRA') quantifies the variation in a
time-varying loudness measurement»**. Se calcula **«using a sliding analysis-window of length 3
seconds»**, es decir, sobre la lectura a corto plazo, y se expresa en LU.

Cómo se calcula:

1. Se toman las sonoridades a corto plazo del programa.
2. Se aplican dos puertas: **«The absolute threshold is set to −70 LUFS»** y **«The relative
   threshold is set to a level of −20 LU relative to the absolute-gated loudness level»** (−20, no
   −10 como en la integrada).
3. **«LRA is defined as the difference between the estimates of the 10th and the 95th percentiles
   of the distribution»**: se descarta el 10 % más flojo y el 5 % más fuerte, y el LRA es la
   distancia entre esos dos percentiles. La norma da la razón del percentil bajo: **«can, for example,
   prevent the fade-out of a music track from dominating Loudness Range»**; el alto evita que un
   solo sonido muy fuerte dispare el resultado.

Para qué sirve: la R 128 dice que el LRA **«may be used to evaluate the loudness variation of a
programme, its potential subsequent dynamic treatment and the dynamic integrity of a distribution
path»**. Un LRA alto indica un programa con mucha diferencia entre pasajes flojos y fuertes; uno
bajo, un programa muy comprimido (oficio). Y en programas de menos de un minuto no se recomienda,
por **«too few data points»** (R 128, nota 2).

### Sonoridad y compresión

La relación entre compresión y sonoridad es lo que un técnico de emisión maneja (el compresor y sus
mandos, en el tema 5). Tres ideas, de oficio:

1. Comprimir sube la sonoridad sin subir el pico: el compresor acerca lo flojo a lo fuerte, y el
   conjunto suena más denso con el mismo techo.
2. Con la R 128, comprimir ya no da ventaja de volumen: si la sonoridad integrada tiene que ser
   −23 LUFS, comprimir más sólo obliga a bajar más el conjunto. Lo que se gana en densidad se
   pierde en nivel.
3. Lo que sí se sigue ganando es consistencia: una emisión comprimida se oye mejor en un coche. La
   compresión pasa de ser un arma de volumen a una decisión de inteligibilidad. El LRA es la cifra
   que mide ese efecto.

## Fases

La fase, la polaridad y el filtro en peine como fenómenos físicos están en el tema 1. Aquí interesa
cómo se miden en una señal estéreo y qué tienen que ver con la sonoridad.

### La correlación de fase

El correlador de fase compara los dos canales de una señal estéreo. Según el fabricante RTW,
**«Mostly, phase correlation is used to determine the mono compatibility of a stereo signal, but
depending on where you use it, it can also reveal other things, such as bad microphone
placement»**. Su escala: **«a linear scale going from -1 (switched polarity) over 0 (unrelated) to
1 (identical)»**.

| Lectura | Qué significa | Qué pasa al sumar a mono (oficio) |
|---|---|---|
| +1 | Los dos canales son idénticos | Suma limpia: es, de hecho, una señal mono |
| Entre 0 y +1 | Estéreo con información común | Compatible |
| 0 | Canales sin relación | Suma sin refuerzo ni cancelación sistemática |
| Por debajo de 0, hacia −1 | Polaridad invertida o gran desfase entre canales | Cancelación: al sumar a mono se pierde señal, a veces casi toda |

El mismo fabricante da una referencia de trabajo: **«Normal stereo mixes usually show correlation
values between 0.3 and 0.7»**. Es una cifra de fabricante, no de norma. En multicanal, el
correlador múltiple sirve para comprobar que la mezcla envolvente **«also sounds great when down
mixed to stereo or even mono»** (RTW); la mezcla descendente y la compatibilidad se desarrollan en
el tema 14.

**Aplicación práctica** (oficio). Una lectura negativa y estable en una fuente que debería ser mono
—una voz por dos canales, un micrófono de corbata— apunta a un cable o una conexión con la polaridad
invertida, o a una inversión de polaridad en un canal de la mesa; se comprueba invirtiendo uno de
los dos canales y viendo si la correlación pasa a +1. Una lectura que oscila hacia valores negativos
en una pareja estéreo de micrófonos apunta a una mala colocación: la misma fuente llega a los dos
micrófonos con retardo distinto (colocación de micrófonos, en el tema 3). La prueba definitiva es
escuchar la suma en mono.

**El goniómetro o vectorscopio de audio.** Según el fabricante RTW, el vectorscopio **«displays the
changing phase relationship between a selectable channel pair in real time»**; la figura se llama
**«Lissajous display»**, y respecto a unos ejes clásicos con izquierdo y derecho, la representación
está **«rotated counter-clockwise by 45°»**, con el origen en el centro. El vectorscopio de RTW lleva un control automático
de ganancia (**AGC**, *automatic gain control*) que compensa los cambios de nivel. Cómo se lee (RTW):

| Figura | Qué indica |
|---|---|
| Línea vertical | Mono doble: **«Dual-mono signals with exactly the same level in each channel appear as a vertical line»**; cuanto más vertical, más cerca del mono |
| Línea horizontal | Polaridad invertida en un canal: **«If the two channels have switched polarity - one channel rotated by 180° or "inverted" - you will see a horizontal line»** |
| Línea inclinada 45° a la izquierda o a la derecha | Señal sólo en el canal izquierdo o sólo en el derecho; si la figura se inclina hacia un lado, la imagen estéreo está desequilibrada |
| Madeja equilibrada | Mezcla estéreo normal: **«a well-balanced "ball of wool"»**; su movimiento y su dispersión pueden informar, entre otras cosas, de la anchura de la base estéreo |

Las figuras horizontales indican canales muy distintos, que pueden dar problemas de compatibilidad mono, y la polaridad invertida suele
venir, según RTW, de un cableado erróneo o del botón de inversión (*INV*) de un micrófono o de la
mesa pulsado sin querer.

### Fase y sonoridad: el tono en los dos canales

Lo que marca el medidor de sonoridad con un tono depende de cuántos canales lo llevan, no de la
fase entre ellos: la BS.1770 calcula primero el valor cuadrático medio de cada canal (**«mean square
calculation for each channel»**) y sólo después suma los canales con su peso (**«channel-weighted
summation»**). Con la energía de cada canal calculada por separado, un tono con la polaridad
invertida en un canal marca lo mismo que en fase (cálculo sobre esas etapas). La contrafase no se ve
en el medidor de sonoridad, sino en el correlador, en el goniómetro o al sumar a mono. La Tech 3343 (§ 8.1), al dar la lectura del tono de alineación, lo pide en fase en los dos canales: **«The alignment level of −18 dBFS (1 kHz tone) will read as −18 LUFS
on a loudness meter with the absolute scale (or +5 LU on the relative EBU mode scale), provided that
the 1 kHz tone is present (in phase) on both the left and right channel of a stereo or surround
sound signal.»**

Las cuentas, sobre la cifra de la BS.1770 (un tono de 0 dBFS en un canal frontal marca −3,01 LUFS):

| Tono de 1 kHz a −18 dBFS | Lectura de sonoridad (cálculo) |
|---|---|
| En los dos canales, en fase | −18 LUFS, que en la escala relativa son +5 LU (−18 − (−23)) |
| En un solo canal | Unos −21 LUFS: −18 − 3,01 |

Por eso el tono se alinea con el medidor de pico: el de sonoridad da lecturas distintas según
cuántos canales lleven el tono, y además pondera en frecuencia. La Tech 3343 recomienda el medidor
de pico para alinear, como se vio en «La alineación: −18 dBFS y el fin del −9 dBFS».

## Control de calidad

### Lo que la R 128 exige al control de calidad

La R 128 menciona el control de calidad de forma expresa en su tolerancia de medida: **«for the
implementation of Loudness workflows (for example, in Quality Control environments) a tolerance of
±0.2 LU is allowed in order to take account of measurement errors»**.

Hay que distinguir las dos tolerancias:

| Tolerancia | Valor | Para qué |
|---|---|---|
| Del directo (punto h) | ±1,0 LU | Cuando no se puede alcanzar el objetivo en la práctica, como en directo |
| De medida (punto i) | ±0,2 LU | Errores de medida en los flujos de trabajo, por ejemplo en control de calidad |

Un programa grabado que llega a control de calidad debe dar −23 LUFS; con la tolerancia de medida,
se acepta entre −23,2 y −22,8 LUFS (cálculo sobre el punto i). Además:

- Se mide entero, sin atender sólo a la voz o la música (punto l).
- El medidor cumple la BS.1770, con su puerta, y la Tech 3341 (punto k).
- El pico verdadero no pasa de −1 dBTP, con una tolerancia de medida de ±0,3 dB (punto m), o el
  techo más bajo que pida el sistema de distribución.
- Si el programa va más bajo de −23 LUFS a propósito, tiene que indicarse claramente (punto j).

### Los metadatos de sonoridad

En Dolby AC-3 (Dolby Digital), según la Tech 3343 (§ 6), los metadatos de sonoridad se llaman
**«dialnorm (dialogue normalisation), dynrng (dynamic range) and Centre/Surround Downmix Level»**.
El dialnorm es el que declara la sonoridad: **«The parameter dialnorm genuinely describes the
loudness of an entire programme with all its elements such as voice, music or sound effects»**; sólo
cuando se normaliza tomando el diálogo como ancla describe la sonoridad del diálogo. Con la R 128,
el parámetro debe indicar −23 LUFS (§ 6.1): **«the relevant Metadata parameter shall naturally also be set
to indicate −23 LUFS»**. La misma § 6.1 admite otro valor en tres casos: programas de archivo que no
se pueden ajustar a tiempo, programas externos en directo que llegan con otra sonoridad y otros
metadatos, y sistemas en los que los metadatos viajan fielmente por toda la cadena hasta el receptor.

La R 128 exige que los metadatos digan la verdad: **«Loudness Metadata shall correctly indicate the
actual Programme Loudness»**. La Tech 3343 (§ 6) señala dos valores sospechosos en el sistema Dolby
Digital: **«Programme Loudness Metadata indicating −27 (the factory default for dialnorm in the
Dolby-Digital system) or −31 (the lowest possible value in that system) are likely to raise special
awareness»**. −27 es el valor de fábrica; −31, el mínimo posible: si un fichero llega con uno de
ellos, lo probable es que nadie haya medido.

Y la conclusión de la misma guía: **«It is therefore recommended to discard Loudness and Dynamic
Range Control Metadata for external sources except where the source can be fully trusted»**. El
material que llega de fuera se vuelve a medir.

### La revisión de un programa, paso a paso

Una lista de comprobación de sonoridad antes de entregar un programa a emisión (oficio, sobre las
cifras de las recomendaciones citadas):

1. Medidor en «modo EBU», conforme a la BS.1770 y a la Tech 3341, con la escala adecuada (EBU +9
   o +18) y el objetivo en −23 LUFS = 0 LU.
2. Medida integrada del programa entero, de principio a fin, sin cortes: −23 LUFS (±0,2 LU de
   medida); si es un directo, dentro de ±1 LU.
3. Pico verdadero máximo: no más de −1 dBTP en audio lineal; −2 dBTP si va a MPEG-1 Layer 2 o
   AC-3.
4. Máximos momentáneo y a corto plazo: que ningún pasaje moleste al público, aunque la integrada
   cumpla.
5. LRA, si el programa dura más de un minuto: coherente con el tipo de programa y con el destino.
6. Fase: correlación positiva en el estéreo y escucha de la suma en mono.
7. Metadatos: que la sonoridad declarada coincida con la medida; desconfiar de −27 y −31.
8. Material externo: medir de nuevo y no fiarse de sus metadatos.

Si el programa no cumple, se corrige su nivel de conjunto (una diferencia de ganancia en dB mueve
la lectura integrada en la misma cantidad de LU) y, si el pico verdadero lo impide, se limita.
Ejemplo: un programa grabado que mide −20 LUFS con picos de −3 dBTP se baja 3 dB; queda en −23
LUFS y con picos en −6 dBTP (cálculo). Uno que mide −26 LUFS con picos de −2 dBTP necesita subir 3
dB, pero sus picos llegarían a +1 dBTP: hay que limitar antes de subir.

Las normas de control de calidad de ficheros de la UER, los requisitos de entrega de CSRTV y sus
procedimientos de control de calidad no constan en las fuentes leídas (se ve en «Lo que este tema
no da, y dónde está»).

## Recomendaciones técnicas que el tema cita

| Documento | Qué se toma |
|---|---|
| EBU R 128-2023 (V5) | Considerandos; planteamiento (sonoridad del programa y pico verdadero máximo); puntos h) a p); notas 1 y 2; definiciones; historial de versiones; documentos asociados |
| UIT-R BS.1770-5 (2023) | Alcance; las cuatro etapas del algoritmo; ponderación K; pesos de los canales y exclusión del LFE; LKFS; −3,01 LKFS; puerta; considerandos y anexo 2 del pico verdadero; dBTP |
| EBU Tech 3341-2023 | Lecturas M, S e I, ventanas y puerta; actualización a 10 Hz y a 1 Hz; funciones mínimas de arranque, pausa y puesta a cero; máximos; puerta de la integrada; 1 LU = 1 dB; escalas EBU +9 y EBU +18; unidades siempre visibles |
| EBU Tech 3342-2023 (V4) | Definición y cálculo del LRA |
| EBU Tech 3343-2023 (V4) | Tono de alineación y su lectura en sonoridad; PML obsoleto; medidor de pico para alinear; margen de 1 dB y −2 dBTP; LFE excluido y peso de los envolventes; −24 LUFS en deportes; metadatos sospechosos |
| EBU R 68-2000 | Alineación 18 dB bajo el máximo (1:8, 18,06 dB); picos reales 3 dB sobre lo que indica el cuasipico |
| EBU Tech 3205-E (1979, sustituida) | El PPM de la UER: cuasipico, 10 ms, retorno, escala, tipos CEI |

Ninguna norma legal (ley o reglamento) regula la medición de sonoridad en las fuentes leídas: el
tema se apoya en recomendaciones técnicas, documentación de fabricante, prensa técnica y oficio.

## Lo que este tema no da, y dónde está

- El texto de los suplementos R 128 s1 (contenido corto), s2 (*streaming*), s3 (radio) y s4 (cine),
  de la Tech 3344 (distribución) y de la Tech 3401 (radio): sólo consta su existencia y objeto, por
  la propia R 128. Las cifras de sonoridad que fijen para radio o para *streaming*, y los techos de
  pico por sistema de distribución de la Tech 3344, no se dan.
- La tabla de tolerancias del pico verdadero de la Tech 3341 y las ecuaciones del algoritmo de la
  BS.1770 (salvo su constante): no se reproducen.
- La norma de la CEI que especifica hoy el vúmetro y la Publicación 268-10 de la CEI sobre los PPM
  (que cita la Tech 3205-E): no leídas; el tiempo del vúmetro va con fuente de prensa técnica.
- Las normas de control de calidad de ficheros de la UER: no consultadas.
- Lo propio de CSRTV: su nivel objetivo de emisión en radio y en televisión, sus requisitos de
  entrega de programas, sus procedimientos de control de calidad y los medidores de sus controles no
  constan en un documento publicado localizado.
- Fase, polaridad y filtro en peine como fenómenos, en el tema 1; el compresor, el limitador y el
  margen de trabajo, en el tema 5; la mezcla para emisión en televisión, en el tema 8; la entrega en
  postproducción, en el tema 9; el multicanal, el LFE y la mezcla descendente, en el tema 14.

## Trazabilidad

Fuentes leídas el 25/09/2026, primero a través del material de investigación del bloque y después,
en la verificación, directamente en su texto (el mismo día); las recomendaciones de la UER y de la
UIT, en su versión vigente ese día.

| Fuente | Qué sostiene |
|---|---|
| EBU R 128-2023 (V5, noviembre de 2023), *Loudness normalisation and permitted maximum level of audio signals* | Portada y estado; historial de versiones; considerandos a) a e); planteamiento; puntos h), i), j), k), l), m), n), o) y p); notas 1 y 2; definiciones de *Programme Loudness*, *Maximum True Peak Level* y programa; documentos asociados (puntos q a v) |
| UIT-R BS.1770-5 (11/2023), *Algorithms to measure audio programme loudness and true-peak audio level* | Alcance (recomienda 1 a 3); considerandos del pico verdadero; anexo 1: cuatro etapas, ponderación K, RLB, tabla 3 de pesos, exclusión del LFE en la descripción de las etapas, LKFS, −3,01 LKFS, −0,691, umbrales de la puerta; límites del algoritmo; anexo 2: 12,04 dB y su finalidad, sobremuestreo 4× y 2×, etapas, dBTP. Estado de versiones según la página de la UIT (BS.1770-5 «In force»; -0 de 2006 a -4 de 2015, «Superseded») |
| EBU Tech 3341-2023, *Loudness Metering: ‘EBU Mode’ metering to supplement EBU R 128 loudness normalization* | § 2.1 nombres y máximos; § 2.2 ventanas de 0,4 y 3 s, puerta, 10 Hz y 1 Hz, funciones start/pause/continue y reset; § 2.3 puerta de la integrada; § 2.4 1 LU = 1 dB; § 2.7 escalas, escala por defecto y objetivo = 0 LU; § 2.8 unidades |
| EBU Tech 3342-2023 (V4), *Loudness Range* | Definición del LRA; ventana de 3 s; umbrales −70 LUFS y −20 LU; percentiles 10 y 95 |
| EBU Tech 3343-2023 (V4), *Guidelines for Production of Programmes in accordance with R 128* | § 8.1 tono, alineación, PML obsoleto, −18 LUFS y +5 LU, medidor de pico; margen de 1 dB e infralectura de 0,5 dB; −2 dBTP para MPEG-1 Layer 2 y AC-3; § 4.2 LFE; nota 3 envolventes; § 3.5.1 −24 LUFS; § 6 metadatos (dialnorm, dynrng, coeficientes de mezcla descendente; −27 y −31); § 6.1 metadato a −23 LUFS y sus tres excepciones |
| EBU R 68-2000, *Alignment level in digital audio production equipment and in digital audio recorders* | 18 dB bajo el máximo; 1:8 (18,06 dB); picos 3 dB sobre el cuasipico |
| EBU Tech 3205-E, 2.ª ed., noviembre de 1979, *The EBU standard peak-programme meter* | Modo normal: 10 ms (10 ± 2) y definición del tiempo de integración (+9 → +7); caída de +12 a −12 en 2,8 ± 0,3 s; divisiones de 2 dB; marca «Test» y su salvedad (máximo en circuitos internacionales según el C.C.I.T.T.); retorno en modo lento 3,8 ± 0,5 s; tipos CEI I, IIa y IIb; sustituida por la R 128 |
| RTW, «Focus: The Multi Correlator», Thomas Valter, 9-VIII-2019 (fabricante) | Uso del correlador; escala de −1 a +1; 0,3 a 0,7 en mezclas normales; correlador múltiple y mezcla descendente |
| RTW, «Focus: The Audio Vectorscope», Mike Kahsnitz, 2-VIII-2019 (fabricante), leído el 25/09/2026 | Qué muestra el vectorscopio; figura de Lissajous girada 45°; AGC; línea vertical (mono), horizontal (polaridad invertida), 45° a un lado (un solo canal), «ball of wool» (mezcla normal); causas de la polaridad invertida |
| UIT, «ITU's History», página 3 (itu.int), leída el 25/09/2026 | Nombre del C.C.I.T.T. (*International Telephone and Telegraph Consultative Committee*), creado en 1956 |
| Sound On Sound, H. Robjohns, «VU Meters: "Virtually Useless" or Very Useful?», mayo de 2024 (prensa técnica, no norma) | 300 ms del vúmetro; +4 dBm = 0 VU con el atenuador a 0; especificación de 1940 aún en uso |

Oficio sin norma detrás, y así se declara: la tabla pico/sonoridad y la razón de que el oído no oiga
picos; el efecto del filtro paso alto sobre un bombo; el uso de cada lectura M, S e I; el trabajo
del operador en un directo; la explicación de por qué el codificador descubre el exceso de pico;
el uso de las escalas EBU +9 y +18; la lectura de un LRA alto o bajo; las tres ideas sobre
compresión y sonoridad; la tabla de lecturas del correlador y lo que ocurre al sumar a mono; la
aplicación práctica de la correlación; la lista de comprobación de control de
calidad. Es cálculo, y se puede rehacer: −24 a −22 LUFS en directo; −23,2 a −22,8 LUFS con la
tolerancia de medida; el paso de LUFS a LU; −18 LUFS y +5 LU del tono en fase, unos −21 LUFS en
un solo canal, y la misma lectura con un canal en contrafase; los ejemplos de corrección de nivel.
