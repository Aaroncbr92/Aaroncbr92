# Tema 5 del específico de Operador/a de Sonido · Procesamiento de audio

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 5 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Recomendaciones técnicas: EBU R 68 (nivel de alineación), EBU R 128 y EBU Tech 3343 (pico verdadero y margen). Documentación de fabricante: Rane, RaneNote 155 (procesadores de dinámica: estructura, compresor, expansor, puerta, *ducker* y limitador), RaneNote 160 (pendiente de los filtros por orden) y RaneNotes 101 y 122 (bandas de los ecualizadores gráficos). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | La vigente el 24/09/2026: EBU R 128-2023 (versión 5, noviembre de 2023) y EBU Tech 3343-2023 (versión 4, noviembre de 2023) |
| **Extensión** | 8.590 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Europea de
Radiodifusión (**UER**, en inglés **EBU**, *European Broadcasting Union*), que publica sus
recomendaciones (**R**) y sus documentos técnicos (**Tech**); Unión Internacional de
Telecomunicaciones (**UIT**, en inglés **ITU**); Organización Internacional de Normalización
(**ISO**); decibelio (**dB**); decibelios referidos a 0,775
voltios (**dBu**); decibelios referidos a la escala completa digital (**dBFS**, *decibels relative
to full scale*); decibelios de pico verdadero (**dBTP**, *decibels true peak*); nivel de presión
sonora (**dB SPL**, *sound pressure level*); nivel máximo permitido (**PML**, *permitted
maximum level*); modulación por impulsos codificados (**PCM**, *pulse code modulation*); grupo de expertos en imágenes en
movimiento (**MPEG**, *Moving Picture Experts Group*), cuya norma MPEG-1 Layer 2 es un sistema de
reducción de datos de audio, como el Dolby AC-3; el margen entre el nivel de
trabajo y la saturación (*headroom*); el umbral (*threshold*), la relación de compresión
(*ratio*), el ataque, la relajación (*release*), el codo (*knee*) y la recuperación de ganancia
(*make-up*) de un compresor; el control automático de ganancia (**AGC**, *automatic gain
control*); la cadena lateral de control (*side-chain*) y la entrada de clave externa (*key
input*); el mantenimiento (*hold*) y la profundidad (*depth*) de una puerta; el atenuador
automático de una señal por otra (*ducker*, y su efecto, *ducking*); el reductor de sibilantes
(*de-esser*); el factor de selectividad de un filtro (**Q**); el filtro de ranura (*notch*); el
filtro de estantería (*shelving*); el amplificador controlado por tensión (**VCA**,
*voltage-controlled amplifier*); el transistor de efecto campo (**FET**, *field-effect
transistor*); el compresor de válvula de ganancia variable (*Vari-Mu*); los pulsos por minuto
(**BPM**); el retardo (*delay*); la reverberación (*reverb*); la predemora (*pre-delay*); el
tiempo de reverberación medido como caída de sesenta decibelios (**RT60**); la estación de trabajo
de audio digital. El fabricante se cita por su nombre
comercial: Rane.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 5):
>
> Procesamiento de audio: ecualización, dinámica, compresión, limitación, puertas, filtros,
> reverberación y efectos.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué tipos de ecualizador hay y qué parámetros deja tocar cada uno; qué es
el factor Q y a qué ancho en octavas corresponde un Q dado; por qué «multibanda» no es un tipo de
ecualizador; qué es el *headroom* y en qué se diferencia del rango dinámico; a qué nivel se alinea
el tono en digital según la EBU; qué estructura comparten todos los procesadores de dinámica; qué
hace cada mando de un compresor, qué márgenes de ataque y relajación da el fabricante y qué significa una relación 4:1; para qué sirve el *make-up*; qué
tecnología de compresor responde más rápido; qué convierte un compresor en limitador y para qué se
usa un limitador; qué pico verdadero máximo fija la EBU R 128 en producción; qué es una puerta, en
qué se diferencia de un expansor y qué hacen su umbral, ataque, mantenimiento, liberación y
profundidad; qué son la clave externa y el *ducker*; qué causa el «respirar» y el chasquido de una
puerta; qué pendiente tiene un filtro según su orden; qué filtro se usa contra el acoplamiento de una megafonía y por qué; qué sistemas de
reducción de ruido hay; qué parámetros tiene una reverberación y qué hace la predemora; en qué
familias se ordenan los efectos; cuánto dura un retardo de corchea a un tempo dado. En la prueba
práctica: ajustar un compresor sobre una voz, cerrar con una puerta los micrófonos de una mesa, quitar
un acoplamiento, calcular un retardo a tempo y elegir la cadena de proceso de un canal.

<!-- indice -->

## Índice

- [Ecualización](#ecualización)
  - [Qué hace un ecualizador](#qué-hace-un-ecualizador)
  - [Los tipos de ecualizador](#los-tipos-de-ecualizador)
  - [El factor Q](#el-factor-q)
  - [La ecualización en la práctica](#la-ecualización-en-la-práctica)
- [Dinámica](#dinámica)
  - [Qué es un procesador de dinámica](#qué-es-un-procesador-de-dinámica)
  - [El headroom](#el-headroom)
  - [Por qué 18 dB de reserva](#por-qué-18-db-de-reserva)
  - [Headroom no es rango dinámico](#headroom-no-es-rango-dinámico)
- [Compresión](#compresión)
  - [Qué hace un compresor y sus mandos](#qué-hace-un-compresor-y-sus-mandos)
  - [La recuperación de ganancia](#la-recuperación-de-ganancia)
  - [Las tecnologías de compresor](#las-tecnologías-de-compresor)
  - [El compresor multibanda y el reductor de sibilantes](#el-compresor-multibanda-y-el-reductor-de-sibilantes)
  - [La compresión en la práctica](#la-compresión-en-la-práctica)
- [Limitación](#limitación)
  - [Qué es un limitador](#qué-es-un-limitador)
  - [Para qué se usa](#para-qué-se-usa)
  - [El limitador y el pico verdadero](#el-limitador-y-el-pico-verdadero)
- [Puertas](#puertas)
  - [Qué es una puerta y en qué se diferencia del expansor](#qué-es-una-puerta-y-en-qué-se-diferencia-del-expansor)
  - [Los parámetros de la puerta](#los-parámetros-de-la-puerta)
  - [Usos y defectos de la puerta](#usos-y-defectos-de-la-puerta)
  - [La clave externa y el *ducker*](#la-clave-externa-y-el-ducker)
- [Filtros](#filtros)
  - [Los filtros de corte](#los-filtros-de-corte)
  - [El filtro notch y el acoplamiento](#el-filtro-notch-y-el-acoplamiento)
  - [Los sistemas de reducción de ruido](#los-sistemas-de-reducción-de-ruido)
- [Reverberación](#reverberación)
  - [Qué es una reverberación artificial](#qué-es-una-reverberación-artificial)
  - [Los parámetros de una reverberación](#los-parámetros-de-una-reverberación)
  - [La reverberación en la práctica](#la-reverberación-en-la-práctica)
- [Efectos](#efectos)
  - [Las familias de efectos](#las-familias-de-efectos)
  - [El retardo a tempo](#el-retardo-a-tempo)
  - [Inserción y envío: dónde va cada proceso](#inserción-y-envío-dónde-va-cada-proceso)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Ecualización

### Qué hace un ecualizador

Un ecualizador cambia el reparto de una señal por frecuencias: sube o baja unas bandas y deja
otras. Al hacerlo cambia el peso relativo de los armónicos, y con él el timbre (tema 1). Es el
procesador que más se usa en una mesa: casi todos los canales de entrada llevan uno.

Las formas de actuar sobre una banda son tres, y cada una se dibuja distinta sobre la curva de
respuesta:

| Forma | Qué hace | Para qué se usa |
|---|---|---|
| Campana (*peaking*) | Sube o baja una franja alrededor de una frecuencia central; lo de los lados queda igual | Corregir o realzar una zona concreta: la nasalidad de una voz, el cuerpo de un bombo |
| Estantería (*shelving*) | Sube o baja por igual todo lo que queda por encima (agudos) o por debajo (graves) de una frecuencia | Dar o quitar brillo o peso a todo el extremo del espectro |
| Filtro de corte | Elimina lo que queda por debajo o por encima de una frecuencia | Quitar lo que está fuera de la banda útil; se desarrolla en «Filtros» |

La clasificación es de oficio, no de norma.

### Los tipos de ecualizador

| Tipo | Qué se puede tocar |
|---|---|
| Gráfico | Sólo la ganancia de cada banda: la frecuencia y el ancho vienen fijos |
| Paramétrico | Frecuencia, ganancia Y ancho de banda: los tres parámetros |
| Semiparamétrico | Frecuencia y ganancia, con el ancho fijo |
| «Multibanda» | No es un tipo de ecualizador: es un adjetivo que se aplica a los COMPRESORES |

El gráfico reparte el espectro en bandas fijas, cada una con su potenciómetro deslizante, y la
fila de mandos dibuja a la vista la curva que se aplica; el de tercio de octava es el de la última
fila de la tabla del factor Q. Según Rane, el gráfico de realce y corte, el más corriente, se ofrece
**«with 10 to 31 bands on octave to 1/3-octave spacing»**, es decir, de 10 a 31 bandas, separadas
entre una octava y un tercio de octava. En los gráficos, las frecuencias centrales están fijas en
las posiciones normalizadas por la ISO, y se dividen en dos grupos en los que dominan,
respectivamente, los **«15 band 2/3-octave equalizers and 30 band 1/3-octave equalizers»**: los de 15
bandas a 2/3 de octava y los de 30 bandas a tercio de octava. El paramétrico es el de los canales de una mesa y el de las estaciones de
trabajo.

El compresor multibanda existe y es corriente —parte el espectro en bandas y comprime cada una por
separado—. La palabra es real; el aparato al que se aplica es otro. Y para más confusión, todo
ecualizador gráfico es, literalmente, de muchas bandas. Lo que hay que saber es que «multibanda» no
es una categoría de ecualizador.

### El factor Q

Qué es el Q: la frecuencia central dividida entre el ancho de banda. A más Q, más estrecha la
campana. Y la relación con las octavas es la que hay que tener:

| Q | Ancho aproximado |
|---|---|
| 0,7 | 2 octavas: muy ancho, para dar carácter |
| 1,41 | 1 octava: el ajuste corriente de trabajo |
| 2,9 | 1/2 octava |
| 4,3 | 1/3 de octava: el ancho de un ecualizador gráfico de tercio |
| Más de 10 | Quirúrgico: es el terreno del notch |

La tabla sale de una cuenta que se puede rehacer. Con el ancho de banda medido entre los puntos a
3 dB por debajo del máximo, una campana de N octavas tiene Q = √(2ᴺ) ÷ (2ᴺ − 1). Para una octava
(N = 1): √2 ÷ 1 ≈ 1,41. Para dos octavas: 2 ÷ 3 ≈ 0,67, que se redondea a 0,7. Para media octava:
1,19 ÷ 0,41 ≈ 2,9. Para un tercio: 1,12 ÷ 0,26 ≈ 4,3. Los manuales la tabulan con pequeñas
diferencias según cómo definan el ancho de banda.

Ejemplo resuelto: una campana centrada en 1.000 Hz con Q = 1,414 tiene un ancho de unos 1.000 ÷
1,414 ≈ 707 Hz, es decir, va aproximadamente de 707 Hz a 1.414 Hz: una octava (1.414 ÷ 707 = 2).

En un gráfico el Q está fijo y no se toca, y es precisamente en el paramétrico donde el Q se
ajusta. Decir que «el Q sólo existe en los ecualizadores gráficos» dice lo contrario de lo que
ocurre.

### La ecualización en la práctica

Las reglas de trabajo son de oficio, y así se dan:

- Q ancho y poca ganancia para dar carácter; Q estrecho para quitar un problema concreto.
- Buscar la frecuencia molesta realzando con Q estrecho y barriendo, y después atenuarla ahí.
- Antes de ecualizar, comprobar la colocación del micrófono: lo que se corrige en la captación no
  hay que corregirlo después.
- Todo ecualizador desfasa alrededor de las frecuencias que toca (tema 1); por eso un canal
  ecualizado y otro sin ecualizar de la misma fuente pueden sumar mal.
- Las ondas estacionarias de una sala no se corrigen ecualizando (tema 1): un hueco de presión no
  se llena subiendo esa banda.

## Dinámica

### Qué es un procesador de dinámica

La dinámica de una señal es la distancia entre sus pasajes más fuertes y los más débiles (tema 1).
Un procesador de dinámica cambia la ganancia de la señal según su propio nivel: la baja cuando es
fuerte (compresor, limitador) o cuando es débil (expansor, puerta). Todos comparten la misma
estructura, que el fabricante Rane describe así: **«All dynamics processors have the common
structure …: a gain control element in the main signal path and a side-chain containing a detector
and gain computer»**. Es decir, un elemento que controla la ganancia en el camino principal de la
señal y una cadena lateral con un detector y un calculador de ganancia. La cadena lateral **«examines
the input signal (or a separate Key Input) and issues a control voltage to adjust the gain of the
signal path»**: mira la señal de entrada, o una señal distinta que entra por la clave externa, y
ordena cuánto bajar.

De ahí la conclusión de Rane, que ordena todo el tema: **«The only difference between a compressor,
limiter, AGC, de-esser, ducker, or gate, is the type of side-chain detector, the gain computer
attributes and the type of gain control element used»**. Compresor, limitador, control automático
de ganancia, reductor de sibilantes, *ducker* y puerta son el mismo aparato con otro detector, otro
cálculo de ganancia u otro elemento de control.

| Procesador | Actúa sobre | Qué hace con el rango dinámico |
|---|---|---|
| Compresor | Lo que pasa por encima del umbral | Lo reduce |
| Limitador | Lo que pasa por encima del umbral, sin dejarlo pasar | Pone un techo |
| Expansor (hacia abajo) | Lo que queda por debajo del umbral | Lo aumenta: lo flojo, más flojo |
| Puerta | Lo que queda por debajo del umbral, casi hasta el silencio | Corta lo que no llega |

Rane resume la simetría en una analogía: **«a peak limiter is to a compressor as a noise gate is
to an expander»**; el limitador es el caso extremo del compresor y la puerta, el del expansor.

### El headroom

El margen de seguridad (*headroom*) es la diferencia de nivel entre el nivel nominal y el punto de
saturación que se debe tener en una mezcla de audio.

Qué es y por qué existe: el nivel nominal es dónde se trabaja; la saturación es dónde el sistema se
rompe. La distancia entre los dos es el margen que queda para lo imprevisto: un grito, un golpe de
caja, una entrada mal medida.

En analógico, el margen depende del equipo: el tema 2 da el ejemplo de Rane, con un nivel medio de
+4 dBu y un máximo de +26 dBu, 22 dB de margen. En digital, el techo es fijo, y la EBU fija dónde
se trabaja:

En digital, el máximo absoluto es 0 dBFS: el mayor número que el sistema puede escribir. Por encima
no hay más; la señal se recorta. Por eso los niveles digitales son negativos, y el nivel de
referencia se fija por debajo de ese techo.

La EBU R 68 recomienda que sus miembros usen **«coding levels for digital audio signals which
correspond to an alignment level which is 18 dB below the maximum possible coding level of the
digital system, irrespective of the total number of bits available»**; la nota 2 lo precisa:
**«corresponding to a ratio of 1:8 (18.06 dB)»**. La EBU Tech 3343 (§ 8.1) lo aplica al tono:
**«An Alignment Signal in broadcasting consists of a sine-wave signal at a frequency of typically
1 kHz, which is used to technically align a programme’s audio path. In digital systems the level of
such an Alignment Signal is 18 dB below the maximum coding level, irrespective of the total number
of bits available (−18 dBFS).»**

Es decir: el tono de referencia es una senoide de 1 kHz a −18 dBFS.

### Por qué 18 dB de reserva

La R 68 explica de dónde sale la reserva. La alineación se define con **«a sine wave signal which has
a level (the alignment level) which is 9 dB (or 8 dB in some organizations) below the permitted
maximum level of the audio programme»**; y los medidores de cuasipico de las emisoras engañan:
**«due to the characteristics of quasi-peak programme meters used by broadcasters, the true
programme peaks can be 3 dB greater than those indicated; When operator errors are taken into
account the true peaks may occasionally be 6 dB greater than indicated or 15 dB above alignment
level»**.

Sumado: el nivel máximo permitido va 9 dB sobre la alineación; los picos reales pueden quedar hasta
3 dB por encima de lo que marca el medidor y, contando los errores de operación, ocasionalmente
hasta 6 dB: 15 dB sobre la alineación. Con 18 dB de reserva, esos
picos todavía caben por debajo de 0 dBFS (cálculo sobre las cifras de la R 68).

El nivel máximo permitido de −9 dBFS ha cambiado con la sonoridad. Dice la Tech 3343 (§ 8.1) que,
con el paso al **«Maximum Permitted True-Peak Level» (−1 dBTP in production for generic PCM
signals) the recommended PML of −9 dBFS in ITU-R BS.645 becomes obsolete**. Lo que no cambia es la
alineación: **«The switch to loudness normalisation does NOT change this approach»**, y **«electrical
alignment for sound-programme exchange can be performed as usual, with a sine-wave signal of 1 kHz
at a level of −18 dBFS.»**

La diferencia que más cuesta interiorizar: en analógico, pasarse un poco distorsiona
progresivamente; en digital, pasarse un poco RECORTA. El 0 dBFS no es una recomendación: es el
número más grande que cabe. Por eso una mezcla digital se trabaja con el nominal bien por debajo
del techo.

### Headroom no es rango dinámico

Tres conceptos cercanos se confunden con el *headroom*, y ninguno lo es:

| Concepto | Qué es de verdad |
|---|---|
| Masterización | La fase final de una producción: no es una distancia entre niveles |
| Nivel de presión sonora | Lo que hay en el aire, en dB SPL: no es un margen |
| Rango dinámico | La distancia entre el ruido de fondo y la saturación. El headroom mide desde el nominal hacia arriba; el rango dinámico, desde el suelo de ruido |

Los procesadores de dinámica trabajan precisamente sobre esa distancia: el compresor y el limitador
recortan por arriba lo que se come el margen; el expansor y la puerta bajan por abajo lo que se
confunde con el ruido.

## Compresión

### Qué hace un compresor y sus mandos

Un compresor reduce la diferencia entre lo más fuerte y lo más flojo. Sus mandos, y qué hace cada
uno:

| Mando | Qué hace |
|---|---|
| Umbral | A partir de qué nivel empieza a actuar |
| Relación | Cuánto reduce lo que pasa del umbral: 4:1 significa que cuatro decibelios de más a la entrada se convierten en uno a la salida |
| Ataque | Cuánto tarda en empezar a reducir |
| Relajación | Cuánto tarda en soltar |
| Codo | Si la reducción entra de golpe (*hard knee*) o progresivamente (*soft knee*) |
| Recuperación de ganancia | Sube todo lo que queda, para compensar lo que la compresión ha bajado |

Por debajo del umbral el compresor no toca la señal; la relación sólo se aplica a lo que lo supera.
Como orden de magnitud de fabricante, Rane da para los compresores un umbral ajustable de **«-40
dBu to +20 dBu»**; unos tiempos de ataque que **«for compressors generally range between 25 ms and
500 ms»**, de 25 a 500 ms (en los expansores y las puertas, de 0 a 250 ms: ver «Los parámetros de
la puerta»); y, para compresores y expansores, unos ajustes típicos de relajación **«between 25 ms
and 2 seconds»**.

La salvedad de la relajación: ese margen es el del mando, no el tiempo que tarda el compresor en
soltar del todo. Rane advierte que **«There is no industry standard and different manufacturers
define this control differently»**: cada fabricante define el mando a su manera, y Rane lo define
como el tiempo que tarda la ganancia en cambiar 10 dB, **«not how long it takes to return to unity
gain»**, no el que tarda en volver a la ganancia unidad. El tiempo real sale de **«Release Time =
(Gain Reduction x Release Setting) / 10 dB»**: con el mando a 1 s y 5 dB de reducción aplicada,
la relajación real es (5 × 1) ÷ 10 = 0,5 s.

Ejemplo resuelto: umbral a −20 dBFS y relación 4:1. Un pico que llega a −8 dBFS supera el umbral
en 12 dB; a la salida lo supera en 12 ÷ 4 = 3 dB, así que sale a −17 dBFS y el compresor le ha
quitado 9 dB (la reducción de ganancia que marca su medidor). Una señal a −25 dBFS, por debajo del
umbral, sale igual que entra. Con 2:1, el mismo pico saldría a −14 dBFS (6 dB de reducción); con
relaciones muy altas, prácticamente a −20 dBFS: es el limitador.

El ataque y la relajación deciden cómo suena. Un ataque muy rápido se come el golpe inicial de una
percusión o de una consonante; uno lento lo deja pasar y comprime lo que viene después. Una
relajación muy corta hace que la ganancia suba y baje con cada sílaba y se oiga «bombear»; una muy
larga deja el canal bajado cuando la señal ya ha caído. Estas descripciones son de oficio.

### La recuperación de ganancia

El ajuste de recuperación (*make-up*) de un compresor recupera ganancia.

Por qué hace falta: un compresor sólo BAJA. Después de comprimir, el material tiene menos nivel de
pico que antes, y si se dejara así el compresor sonaría siempre «peor» que el original. El make-up
devuelve al conjunto el nivel que la reducción le quitó, y ése es el efecto que se percibe como «más
fuerte y más denso»: no lo hace la compresión, lo hace la ganancia de después.

No hay que confundirlo con el codo, que es un mando distinto: el make-up está al final de la cadena
interna del compresor, después de la reducción.

En el ejemplo anterior, con 9 dB de reducción en los picos, unos 9 dB de recuperación devuelven los
picos a donde estaban y suben todo lo demás: la voz queda más igualada y, en conjunto, más fuerte.

### Las tecnologías de compresor

| Tecnología | Cómo controla la ganancia | Velocidad | Carácter |
|---|---|---|---|
| VCA | Un amplificador controlado por tensión | La más rápida y la más precisa | Limpio, transparente, controlable |
| Óptico | Una lámpara y una célula fotosensible | Lenta, y con una relajación en dos tiempos | Muy musical en voz |
| Vari-Mu | Una válvula cuya ganancia varía con la polarización | Lenta | Denso, «pegado»: el sonido clásico |
| *FET* | Un transistor de efecto campo | Muy rápida | Agresivo: el de las cajas de batería |

De las cuatro, la de respuesta más rápida es el VCA. Es un dato de oficio: ninguna documentación
de fabricante leída compara la velocidad de las cuatro. Rane sólo dice que en los diseños analógicos
**«VCAs dominate»**, que predominan los de VCA.

La clase A no es una tecnología de compresión, es una clase de amplificador. Un compresor puede
tener su etapa de salida en clase A y ser óptico, o de válvula, o de VCA.

Y la regla que ordena la tabla: la velocidad y el carácter van reñidos. El VCA es el que mejor
obedece y el que menos se nota; el óptico y el de válvula se notan, y eso es exactamente por lo que
se eligen.

La clasificación es asentada en el sector, no normalizada, y los caracteres sonoros son
descripciones de uso.

### El compresor multibanda y el reductor de sibilantes

El compresor multibanda parte el espectro en bandas y comprime cada una por separado: una subida de
graves no hace bajar los agudos. Es de uso corriente en masterización (oficio).

El reductor de sibilantes (*de-esser*) es un compresor cuya cadena lateral sólo «escucha» la zona
de las eses: cuando una sibilante pasa del umbral, baja la ganancia (de toda la señal o sólo de esa
banda) y la voz no silba. Es uno de los procesadores que Rane cuenta en la misma familia (ver «Qué
es un procesador de dinámica»); su funcionamiento concreto, como se ha descrito, es de oficio.

### La compresión en la práctica

Para la voz, Rane da como puntos de partida (**«starting points»**) en su tabla de ajustes
sugeridos: **«Vocals 25 ms to 100 ms 100 ms to 500 ms 2:1 to 4:1 Soft»**, es decir, ataque de 25 a
100 ms, relajación de 100 a 500 ms, relación de 2:1 a 4:1 y codo blando. Lo demás es oficio, y así
se da:

- En una voz de radio o de informativos, relación moderada (de 2:1 a 4:1, dentro del margen de
  Rane) y pocos decibelios de reducción: la voz se iguala sin que se oiga el proceso.
- Se ajusta mirando el medidor de reducción de ganancia y escuchando, no sólo mirando.
- Comprimir no es subir: la sensación de «más fuerte» la da el *make-up*, y con ella sube también
  el ruido de fondo y el ambiente que la voz tapaba.
- En emisión, la sonoridad del programa la mide el medidor de sonoridad (tema 13), no el compresor.

## Limitación

### Qué es un limitador

El compresor que actúa sólo atenuando los niveles de entrada superiores a un umbral, dejando pasar
inalteradas las señales de nivel inferior, es el compresor limitador.

Qué lo define: una relación de compresión muy alta —10:1 o mayor, y en el límite infinita— y un
ataque muy rápido. Por debajo del umbral no toca nada; por encima, no deja pasar. Un limitador es
un techo.

Rane lo define por su detector y su relación: **«Unlike the compressor, the limiter must ensure that
a signal never exceeds the set threshold. This requires the use of a peak responding detector and a
fixed ratio of infinity:1»**. Es decir, un detector que responde al pico y una relación fija
infinita a uno; en el compresor, en cambio, **«An rms detector is typically used»**: un detector de
valor eficaz.

### Para qué se usa

Rane enumera los usos del limitador de picos: **«Prevent clipping and distortion in power
amplifiers. Protection of loudspeakers …. Preventing overs (digital clipping) during recording.
Preventing overmodulation of the transmitted signal in broadcast»**: evitar el recorte y la
distorsión en las etapas de potencia, proteger los altavoces, evitar que la grabación pase de 0 dBFS
y evitar la sobremodulación de la señal transmitida.

| Uso | Por qué |
|---|---|
| Proteger una etapa de potencia | Que no le lleguen picos que la rompan |
| Proteger un transmisor | Que no se sobremodule |
| Cerrar una masterización | Subir el nivel medio sin pasar de 0 dBFS: es el limitador de pico |

Y en captación: el limitador de un grabador o de una cámara es una red de seguridad para el pico
imprevisto, no un sustituto del ajuste de nivel.

### El limitador y el pico verdadero

Con la sonoridad, el techo de producción ya no es el 0 dBFS sino el pico verdadero. La EBU R 128
fija que **«the True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during
production (linear audio)»**, con una salvedad en el mismo punto: **«Permitted Maximum True Peak
Levels may be lower for different distribution systems and data reduction rates»**. Según la Tech 3343, **«It is only
necessary to leave a headroom of 1 dB below 0 dBFS to still accommodate the potential
under-read of about 0.5 dB (for a 4x oversampling true-peak meter; basic sample rate: 48
kHz)»**; para dos sistemas de reducción de datos muy usados en Europa, MPEG-1 Layer 2 y Dolby AC-3, el límite
recomendado es −2 dBTP.

La R 128 define el pico verdadero máximo como **«The maximum value of the audio signal waveform of
a programme in the continuous time domain»**: el valor máximo de la forma de onda en tiempo
continuo, que puede quedar entre dos muestras y no verse en un medidor que sólo lee muestras. Por eso el limitador de salida de una
cadena de emisión o de una masterización se ajusta en dBTP, y no en dBFS de muestra. La medida del
pico verdadero y la sonoridad se desarrollan en el tema 13.

## Puertas

### Qué es una puerta y en qué se diferencia del expansor

El expansor es el complemento del compresor. Rane: **«Expanders complement compressors by
increasing (expanding) the dynamic range of the signal passing through it, i.e., an expander is a
compressor running in reverse»**; y **«Unlike a compressor, the expander reduces gain for signals
below the threshold»**: **«an expander makes the quiet parts quieter»**. A esa forma de trabajar se
la llama expansión hacia abajo: **«The term downward expander (or downward expansion) evolved to
describe this type of application. The most common use is noise reduction»**.

Ejemplo de Rane: con el umbral **«just below the quietest recorded vocal level»**, justo por debajo
del pasaje más flojo de la voz, y una relación de 2:1, cuando la voz calla la señal cae de su nivel
más flojo al ruido de fondo; si ese escalón es de −10 dB, a la salida es de −20 dB (la relación 2:1
dobla la caída): **«a noise reduction improvement of 10 dB»**. La voz, que está por encima del
umbral, no se toca.

La puerta es el caso extremo del expansor. Rane: **«A gate is to an expander, as a limiter is to a
compressor. Like an expander, gain is reduced below the threshold. Like a limiter, a gate must
respond very quickly to changes in level, dictating the use of a peak detector in the side-chain.
Unlike an expander, a gate uses a fixed ratio of infinity:1 and a variable depth»**. Es decir:
relación fija infinita a uno, detector de pico, y una profundidad ajustable que dice cuánto se baja.

Qué hace: **«When the incoming audio signal drops below the threshold point, the gate prevents
further output by reducing the gain to "zero." Typically, this means attenuating all signals by
about 80 dB»**. Se dice que la puerta **«"opening" and "closing"»**: se abre cuando la señal pasa
del umbral y se cierra cuando cae por debajo.

| | Expansor | Puerta |
|---|---|---|
| Qué baja | Lo que queda por debajo del umbral | Lo que queda por debajo del umbral |
| Cómo | Progresivamente, según la relación (2:1, 3:1…) | Todo o nada: relación infinita, hasta la profundidad fijada |
| Detector | De valor eficaz: **«True rms detection is necessary for compressor and expander modes»** | De pico, para responder muy deprisa |
| Cuándo se prefiere | Cuando cerrar del todo se nota | Cuando entre sonido y sonido debe haber silencio |

### Los parámetros de la puerta

Los mandos y sus márgenes típicos, según Rane (cifras de fabricante):

| Mando | Qué hace | Margen típico |
|---|---|---|
| Umbral | **«the beginning point of gain adjustment»**: el nivel por debajo del cual la puerta se cierra | En expansores, **«A good expander extends the range to -60 dBu for low-level signals»** |
| Ataque | **«determines how quickly the gate opens once the control signal exceeds the threshold setting»** | **«0 ms ("instantaneous" attack …) to 250 ms»** |
| Mantenimiento (*hold*) | **«determines how long the gate remains open after the control signal drops below the threshold setting»** | **«0 to 3 seconds»** |
| Liberación | **«determines how quickly the gate closes as the control signal drops below the threshold setting»** | — |
| Profundidad (*depth*) | **«determines how many dB the signal is attenuated when the control signal is at or below the threshold setting»** | **«0 to -80 dB»** |

La profundidad es lo que distingue una puerta útil de una que «corta»: con −80 dB el canal queda en
silencio; con −10 o −15 dB sólo baja, y el cierre se nota menos. El mantenimiento evita que la
puerta se cierre en las pausas cortas de una palabra o entre golpes seguidos.

Rane añade dos mandos más: **«Almost all gates provide side-chain equalization and external Key
Input»**. La ecualización de la cadena lateral hace que la puerta sólo reaccione a una zona del
espectro (por ejemplo, al golpe del bombo y no al platillo que entra por el mismo micrófono); la
clave externa hace que la abra otra señal distinta. Y una tercera prestación: **«A good gate is able
to "look-ahead" by delaying the main signal a small amount. The best gate combines look-ahead with
pre-ramping»**: retrasa un poco la señal principal para abrir antes de que llegue el golpe.

La histéresis —un umbral de cierre algo más bajo que el de apertura, para que la puerta no abra y
cierre sin parar cuando la señal ronda el umbral— es un mando de oficio que algunas puertas llevan;
no consta en la fuente leída.

### Usos y defectos de la puerta

Los usos, según Rane: **«Gates find use in live sound to reduce crosstalk (bleed) from adjacent
microphones, to keep toms from ringing … and to tighten up the sound. Gates are also used to punch
up and tighten percussive instruments & drums. And gates control unwanted noise, such as preventing
open microphones and hot instrument pick-ups from introducing extraneous sounds»**. Y el expansor,
en directo, **«to reduce stage noise between passages for a quiet vocalist»**.

En una tertulia de radio o televisión con varios micrófonos abiertos, una puerta o un expansor en
cada canal baja los micrófonos de quien no habla: menos ruido de sala, menos captación cruzada y
menos filtro en peine entre micrófonos (tema 1). Si cierra del todo y el umbral está alto, se come
el principio de las frases; por eso en voz se prefiere el expansor o una profundidad moderada.
Esta aplicación es de oficio.

Los defectos, según Rane: **«poorly designed gates cause breathing and clicking. The term breathing
describes an audible problem caused by hearing the noise floor rise and fall»**; y **«Clicking is
caused by opening the gate too fast. It is a common myth that if you make a gate open faster it will
sound better; however, such is not the case. The faster a gate opens, the higher in frequency the
click is»**.

| Defecto | Qué se oye | Causa |
|---|---|---|
| Respiración (*breathing*) | El ruido de fondo sube y baja con cada apertura | La puerta abre y cierra sobre un fondo audible |
| Chasquido (*clicking*) | Un clic al abrir | Ataque demasiado rápido: cuanto más rápido, más agudo el clic |
| Frases cortadas | Se pierde el principio o el final de las palabras | Umbral demasiado alto, o mantenimiento y liberación demasiado cortos |

La última fila es de oficio.

### La clave externa y el *ducker*

El *ducker* trabaja al revés que la puerta: baja una señal cuando otra, la de control, supera el
umbral. Rane: **«A ducker works the opposite of a gate. The signal is attenuated when the side-chain
input goes above the threshold»**; y sus mandos: **«In ducker mode, attack time determines how quickly the signal is reduced as the control
signal exceeds the threshold setting»**; **«The hold time determines how long the signal remains
ducked when the control signal drops below the threshold setting»**; y la profundidad, de **«0 to
-80 dB»**, fija cuánto se atenúa **«when the control signal is at or above the threshold
setting»**.

Rane da dos usos: la megafonía, **«A typical application is paging»**, en la que la voz del
micrófono de avisos baja la música ambiente mientras dura el aviso, y la función de hablar por
encima del programa en las mesas de pinchadiscos (**«talkover»**). En radio y televisión, el uso
corriente es el de la música bajo la voz: la música entra por el camino principal, la voz del
locutor por la clave externa, y cada vez que el locutor habla la música baja sola; cuando calla,
vuelve. Es el efecto de *ducking*. Esta aplicación a la radio y la televisión es de oficio.

## Filtros

### Los filtros de corte

Un filtro deja pasar una zona del espectro y atenúa el resto. Los de uso diario en sonido son
cuatro, y su clasificación es de oficio:

| Filtro | Qué deja pasar | Uso corriente |
|---|---|---|
| Paso alto (corte de graves) | Lo que está por encima de la frecuencia de corte | Quitar el retumbar de baja frecuencia, los golpes de pie de micro, el viento y el exceso de graves por efecto de proximidad |
| Paso bajo (corte de agudos) | Lo que está por debajo | Quitar siseo y ruido de alta frecuencia |
| Paso banda | Sólo una franja | Limitar una señal a una banda: el efecto «teléfono» sobre una voz |
| Banda eliminada o ranura (*notch*) | Todo menos una franja estrecha | Quitar un tono concreto: un zumbido, un acoplamiento |

Dos datos describen un filtro de corte: la frecuencia de corte, que se toma donde la respuesta ha
caído 3 dB, y la pendiente, que se da en decibelios por octava y dice lo deprisa que atenúa más allá
del corte. La pendiente la fija el orden del filtro. Rane da la regla: **«each order, or degree, of a
filter increases the slopes by 6 dB/octave or 20 dB/decade»**; cada orden suma 6 dB por octava (o
20 dB por década). Un filtro de primer orden cae 6 dB/octava; aplicando la regla, uno de segundo
orden, 12 dB/octava, y uno de tercer orden, 18 dB/octava; y uno de cuarto orden, según el ejemplo de Rane, **«24 dB/octave (4 x 6 dB/octave) or 80
dB/decade»**. A diferencia del ecualizador de estantería, que baja por igual todo un extremo, el filtro
de corte atenúa cada vez más cuanto más se aleja de la frecuencia de corte.

*Rumble* es el ruido de baja frecuencia de un giradiscos, y el filtro que lo quita se llama así.

En la práctica, el filtro paso alto está en casi todos los canales de entrada de una mesa y es el
primer proceso que se aplica a una voz: por debajo de la voz no hay nada útil, y lo que hay (tráfico,
aire acondicionado, golpes) se come el margen y hace trabajar al compresor sin necesidad. Es oficio.

### El filtro notch y el acoplamiento

Un filtro notch se utiliza idealmente para evitar un acople con una megafonía.

Qué es un notch: un filtro de ranura, de Q altísimo, que quita una franja de frecuencia muy estrecha
y no toca lo de al lado.

Por qué sirve contra el acoplamiento: la realimentación de un sistema de megafonía se dispara siempre
a UNA frecuencia concreta —aquella en la que la ganancia del lazo llega a uno primero—. Quitando dos o
tres decibelios exactamente ahí, el lazo deja de oscilar y el resto del sonido no se entera. Con un
ecualizador de campana ancha habría que quitar mucho más y se oiría.

Y para qué no sirve el notch, porque no hay una frecuencia estrecha que quitar:

1. La diafonía entre canales es un problema de aislamiento eléctrico o de cableado, no de
   frecuencia: no hay una frecuencia que quitar.
2. Atenuar toda la banda de medias de un bombo pide justo lo contrario que un notch: toda una banda
   es un filtro ancho.
3. Quitar las pes de una voz es trabajo de un antipop o de un filtro de corte de graves: el golpe de
   aire de una oclusiva no es una frecuencia estrecha.

El acoplamiento y la ganancia disponible de un sistema de sonorización se desarrollan en el tema 10.

### Los sistemas de reducción de ruido

| Familia | Cómo funciona | Dónde se usó o se usa |
|---|---|---|
| De doble extremo (*companding*) | Comprime al grabar y expande al reproducir: exige el mismo sistema en los dos extremos | Los sistemas de cinta analógica |
| Puerta de ruido | Cierra el canal cuando la señal baja del umbral | Directo y grabación multipista: es el de uso diario |
| Expansor | Como la puerta, pero progresivo en vez de todo o nada | Cuando cerrar del todo se nota |
| Reducción espectral | Aprende el perfil del ruido y lo resta banda a banda | Postproducción y restauración |
| Filtro de corte | Quita lo que está fuera de la banda útil: *rumble* abajo, siseo arriba | Siempre, y es el primero que hay que probar |

Rane confirma que el uso más común de la expansión hacia abajo es la reducción de ruido (ver
«Puertas»). La tabla, en lo demás, es de oficio.

Y la regla del oficio que ordena la tabla: el mejor sistema de reducción de ruido es no grabarlo. Un
micrófono bien elegido y bien colocado (tema 3) ahorra más ruido que cualquier proceso posterior.

## Reverberación

### Qué es una reverberación artificial

En una sala, la reverberación es la cola de reflexiones que sigue al sonido directo, y su duración se
mide con el tiempo de reverberación, RT60 (tema 1). La reverberación artificial la imita sobre una
señal captada de cerca o en un locutorio seco. Su pariente menor es el retardo: una reverberación
es, en el fondo, miles de retardos con distinta duración y distinta atenuación.

Los aparatos que la han producido, en una clasificación de oficio:

| Tipo | Cómo la produce |
|---|---|
| Cámara de eco | Una sala reverberante real, con un altavoz y un micrófono |
| Muelle | Un muelle que la señal hace vibrar, con un captador en el otro extremo |
| Placa | Una lámina metálica grande puesta en vibración |
| Digital algorítmica | Un cálculo que simula retardos y reflexiones |
| Digital de convolución | La respuesta al impulso medida en una sala real, aplicada a la señal |

### Los parámetros de una reverberación

Los tres parámetros de una reverberación que hay que saber leer:

1. Tiempo de reverberación: cuánto tarda la cola en caer. Es el mismo RT60 del tema 1, aquí puesto a
   mano en vez de medido en una sala.
2. Predemora: cuánto tarda en empezar la cola. Es lo que separa la fuente de la sala: sin
   predemora, la voz suena metida dentro del muro.
3. Mezcla seco/húmedo: cuánta señal procesada se suma a la original.

Las unidades suelen ofrecer además el tamaño de la sala simulada, el nivel de las primeras
reflexiones y un ecualizador o filtro de la cola (lo más corriente, recortar sus graves para que no
embarre). Es oficio.

La predemora y el tiempo de relajación de un compresor sobre material rítmico se pueden ajustar a
tempo, con la misma cuenta que el retardo (ver «Efectos»).

### La reverberación en la práctica

Oficio, y así se da:

- Se coloca en un envío auxiliar y no en inserción: la señal original sigue seca en su canal, y la
  reverberación vuelve por un retorno de efecto al 100 % húmedo; varios canales comparten la misma
  unidad y cada uno decide cuánto manda (el envío y los auxiliares de la mesa son materia del tema
  4).
- En informativos y en palabra se usa poco o nada; en música y en ficción coloca las fuentes en un
  espacio común y da profundidad.
- Una voz de doblaje o un efecto grabado en sala seca necesita la reverberación del lugar de la
  imagen para no sonar «pegado» encima.

## Efectos

### Las familias de efectos

| Familia | Qué hace | Ejemplos |
|---|---|---|
| Basados en TIEMPO | Repiten o prolongan la señal | Delay, reverberación, eco |
| Basados en MODULACIÓN | Varían un parámetro cíclicamente | Chorus, flanger, phaser, trémolo, vibrato |
| Basados en DINÁMICA | Alteran la relación entre fuerte y flojo | Compresor, puerta, expansor |
| Basados en FRECUENCIA | Cambian el reparto espectral | Ecualizadores y filtros |
| De altura | Cambian el tono | Afinador, armonizador, cambio de formantes |

Es una clasificación asentada de la postproducción, no normalizada. Las dos familias centrales son
las de los epígrafes anteriores de este tema; las de tiempo y modulación son los efectos en sentido
estricto.

Qué hacen los efectos de modulación, en descripción de oficio: el coro (*chorus*) suma a la señal
copias levemente retrasadas y desafinadas, y la engorda; el *flanger* suma una copia con un retardo
muy corto que varía, y produce un filtro en peine que se mueve (el mismo filtro en peine del tema 1,
hecho a propósito); el *phaser* consigue un barrido parecido con filtros que desfasan; el trémolo
varía cíclicamente el nivel y el vibrato, la altura.

### El retardo a tempo

Un retardo que no va a tempo se oye como un error. Ajustarlo de oído en un directo no es viable, así
que se calcula.

La cuenta, en dos pasos:

1. La negra dura 60.000 dividido entre los pulsos por minuto.
2. Cada figura se saca de la negra: la blanca vale dos negras, la corchea media, la semicorchea un
   cuarto.

Ejemplo resuelto: un retardo de corchea en un tema de 4/4 a 102 pulsos por minuto. 60.000 ÷ 102 =
588 milisegundos la negra; 588 ÷ 2 = 294 milisegundos la corchea. La trampa no está en la fórmula,
está en la figura que se pide: quien calcula la negra y no lee «corchea» se queda a un paso.

La tabla que evita la cuenta, para las figuras corrientes a este tempo:

| Figura | A 102 BPM |
|---|---|
| Blanca | 1.176 ms |
| Negra | 588 ms |
| Corchea | 294 ms |
| Semicorchea | 147 ms |

Lo mismo vale para el tiempo de relajación de un compresor sobre material rítmico y para la predemora
de una reverberación.

### Inserción y envío: dónde va cada proceso

Oficio, y así se da. Un proceso se conecta de una de dos maneras:

| Conexión | Cómo | Qué procesos |
|---|---|---|
| Inserción | La señal entera del canal pasa por el procesador y vuelve procesada | Ecualizador, filtros, compresor, limitador, puerta, expansor, reductor de sibilantes: los que corrigen la señal |
| Envío auxiliar | Se manda una copia al procesador y su salida se suma a la mezcla por un retorno | Reverberación, retardo y efectos de modulación: los que añaden algo a la señal |

Dentro de un canal, un orden corriente es filtro paso alto, puerta o expansor, ecualizador,
compresor y, al final de la mezcla, limitador. No es norma: la puerta va antes del compresor porque
el compresor, al subir lo flojo con la recuperación de ganancia, dejaría el ruido más cerca del
umbral de la puerta; y el limitador va al final porque es el techo de todo lo anterior.

Todo proceso digital añade algún retardo; en una estación de trabajo, la latencia y su cálculo son
materia del tema 9.

## Recomendaciones técnicas que el tema cita

| Documento | Qué se toma |
|---|---|
| EBU R 68-2000 | Nivel de alineación a 18 dB bajo el máximo (1:8, 18,06 dB); alineación 9 u 8 dB bajo el nivel máximo permitido; picos reales hasta 15 dB sobre la alineación |
| EBU R 128-2023 (V5) | Pico verdadero máximo de −1 dBTP en producción (audio lineal), que puede ser menor según el sistema de distribución; definición del pico verdadero máximo |
| EBU Tech 3343-2023 | Tono de 1 kHz a −18 dBFS; la sonoridad no cambia la alineación; PML de −9 dBFS de la UIT-R BS.645 obsoleto; margen de 1 dB bajo 0 dBFS; −2 dBTP para MPEG-1 Layer 2 y AC-3 |

El tema no invoca ninguna norma legal (ley o reglamento): el resto es documentación de fabricante y
oficio.

## Lo que este tema no da, y dónde está

- Las frecuencias de corte habituales de un filtro paso alto de voz: no se han leído en fuente.
- Los ajustes de compresor para fuentes distintas de la voz (la tabla de Rane los da para bajo,
  guitarras, metales y batería; el tema sólo toma la voz), las tecnologías de compresor, su
  velocidad y su carácter (salvo el predominio del VCA en los diseños analógicos, que da Rane), los tipos de reverberación, los efectos de modulación, el
  orden de la cadena de proceso y la conexión en inserción o envío: se dan como oficio, sin norma ni
  documento de fabricante leído.
- La histéresis de la puerta: sin fuente primaria leída; se da como oficio.
- La reducción espectral de ruido y la restauración en una estación de trabajo, con sus
  herramientas concretas: sin fuente leída; la limpieza de audio en postproducción es materia del
  tema 9.
- El nivel analógico de trabajo y el margen de un equipo analógico, en el tema 2; la estructura de la
  mesa, los auxiliares, los envíos y retornos, en el tema 4; la sonorización y el acoplamiento, en el
  tema 10; la sonoridad, el pico verdadero y sus medidores, en el tema 13; la latencia de proceso de
  una estación de trabajo, en el tema 9.
- Los procesadores y ajustes de CSRTV (procesado de salida de sus emisoras de radio y televisión,
  cadenas de voz de sus locutorios): no constan en un documento publicado localizado.

## Trazabilidad

Fuentes leídas el 25/09/2026; las recomendaciones de la UER, en su versión vigente ese día.

| Fuente | Qué sostiene |
|---|---|
| EBU R 68-2000, *Alignment level in digital audio production equipment and in digital audio recorders* | −18 dBFS; 1:8 (18,06 dB); 9 u 8 dB bajo el PML; picos 3, 6 y 15 dB |
| EBU R 128-2023 (V5, noviembre de 2023), *Loudness normalisation and permitted maximum level of audio signals* | Punto m): −1 dBTP en producción (audio lineal) y salvedad de máximos menores según distribución; definición de *Maximum True Peak Level* |
| EBU Tech 3343-2023 (V4, noviembre de 2023), *Guidelines for Production of Programmes in accordance with EBU R 128* | § 8.1: tono a −18 dBFS, alineación sin cambios con la sonoridad, PML de −9 dBFS obsoleto; margen de 1 dB bajo 0 dBFS; −2 dBTP para MPEG-1 Layer 2 y AC-3 |
| Rane, RaneNote 155, «Dynamics Processors — Technology & Applications», R. Jeffs, S. Holden y D. Bohn, septiembre de 2005 | Estructura común de los procesadores de dinámica y cadena lateral; clave externa; expansor y expansión hacia abajo con su ejemplo de 10 dB; puerta (relación infinita, detector de pico, profundidad, unos 80 dB, abrir y cerrar); analogía limitador-compresor y puerta-expansor; umbral, ataque, mantenimiento, liberación y profundidad con sus márgenes típicos; ecualización de la cadena lateral y anticipación (*look-ahead*); usos y defectos (respiración y chasquido) de la puerta; *ducker*; usos del limitador de picos; umbral de compresor de −40 a +20 dBu, ataque de compresor de 25 a 500 ms y relajación de 25 ms a 2 s; mando de relajación definido como cambio de 10 dB, sin norma común, y su fórmula; puntos de partida para voz (25-100 ms, 100-500 ms, 2:1 a 4:1, codo blando); predominio del VCA en analógico; limitador de picos (detector de pico y relación infinita) frente al detector de valor eficaz del compresor y el expansor; *ducker* (funciona al revés que la puerta; megafonía y *talkover*) |
| Rane, RaneNote 160, «Linkwitz-Riley Crossovers: A Primer», D. Bohn, octubre de 2005 | Cada orden de un filtro suma 6 dB/octava (20 dB/década); el de cuarto orden, 24 dB/octava |
| Rane, RaneNote 101, «Constant-Q Graphic Equalizers», D. Bohn (1982 y 1987, revisada en noviembre de 2005) | Gráficos de 15 bandas a 2/3 de octava y de 30 bandas a 1/3 de octava; centros en posiciones ISO |
| Rane, RaneNote 122, «Operator Adjustable Equalizers: An Overview», D. Bohn (1990, revisada en agosto de 1997) | Gráfico de realce y corte, el más corriente, de 10 a 31 bandas, de octava a 1/3 de octava |

Oficio sin norma detrás, y así se declara: las tres formas de actuar de un ecualizador (campana,
estantería, corte); los tipos de ecualizador y por qué «multibanda» califica a los compresores; la
tabla del factor Q y sus usos; las reglas de ecualización; la definición de *headroom* y su
diferencia con el rango dinámico, la masterización y el nivel de presión sonora; los seis mandos de
un compresor y el efecto del ataque y la relajación; la recuperación de ganancia; las cuatro
tecnologías de compresor y la clase A; el compresor multibanda y el reductor de sibilantes; la
compresión de la voz, salvo los puntos de partida de Rane; qué convierte un compresor en limitador y la tabla de sus usos; el limitador
de captación como red de seguridad; la histéresis; las aplicaciones de la puerta y el expansor en
una tertulia; las frases cortadas; la música bajo la voz; los cuatro filtros de corte y su frecuencia
de corte a −3 dB; el *rumble*; el filtro paso alto como primer proceso; el notch
contra el acoplamiento y lo que no resuelve; la tabla de reducción de ruido; los tipos y parámetros
de la reverberación y su uso; las familias de efectos y los efectos de modulación; la inserción y el
envío; el orden de la cadena de proceso. Es cálculo, y se puede rehacer: la fórmula del Q para N
octavas y sus valores; el ancho de una campana de Q 1,414 a 1 kHz; la reducción de ganancia de un
compresor con relaciones 4:1 y 2:1; la suma de 9 + 6 dB (15 dB) sobre la alineación frente a los
18 dB de reserva; la duración de las figuras a 102 BPM; la pendiente de 12 y 18 dB/octava de los filtros de segundo y tercer orden, por la regla de 6 dB/octava por orden.
