# Tema 10 del específico de Operador/a de Sonido · Sonorización

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 10 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Sin norma legal. Documentación técnica: Shure, R. Frank, *Understanding Sound System Design and Feedback Using (Ugh!) Math* (ley del cuadrado inverso, distancia crítica, ganancia necesaria y ganancia potencial antes de la realimentación); M. S. Ureda, «Analysis of Loudspeaker Line Arrays», *Journal of the Audio Engineering Society*, 2004 (arrays lineales); Crown Audio (etapas de potencia); Texas Instruments, AN-1497 (clases AB y D); Shure, guía de antenas (combinadores de monitores intrauriculares). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | No procede: ninguna norma sostiene este tema |
| **Extensión** | 8.000 palabras aproximadamente |

<!-- /portada -->

Siglas y términos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); sistema de sonorización para
el público (**PA**, *public address*); nivel de presión sonora (**SPL**, *sound pressure level*),
en decibelios (**dB**); decibelios referidos a 0,775 voltios (**dBu**); sensibilidad de un altavoz
en decibelios por vatio a un metro (**dB/W/m**); ganancia acústica necesaria (**NAG**, *needed
acoustic gain*); ganancia acústica potencial antes de la realimentación (**PAG**, *potential
acoustic gain*); número de micrófonos abiertos (**NOM**, *number of open microphones*); las cuatro
distancias de un sistema, **D1**, **D2**, **D0** y **DS**, que se definen en «Realimentación»;
monitor intrauricular (**IEM**, *in-ear monitor*); modulación por anchura de impulsos (**PWM**,
*pulse width modulation*); calibre de cable norteamericano (**AWG**, *American wire gauge*); tiempo de
reverberación medido como caída de sesenta decibelios (**RT60**); índice de transmisión de la
palabra (**STI**, *speech transmission index*); curvas de criterio de ruido de fondo (**NC**,
*noise criteria*); frecuencia modulada (**FM**); Audio Engineering Society (**AES**). El filtro de
cruce se llama también divisor de frecuencias (*crossover*), y el acoplamiento o realimentación
acústica, en el oficio, «acople». Los fabricantes se citan por su nombre comercial: Shure, Crown
Audio (Crown), Texas Instruments (TI), JBL.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 10):
>
> Sonorización: altavoces, amplificadores, PA, monitores, cobertura, realimentación y acústica de
> salas.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué piezas tiene un altavoz electrodinámico y qué hace la araña; en qué se
mide la capacidad de una caja acústica y qué diferencia una caja cerrada, una *bass-reflex* y una de
bocina; qué indica la directividad y por qué los graves son casi omnidireccionales; qué significa
una sensibilidad de 90 dB/W/m y cuánta potencia equivalen 3 dB de sensibilidad; qué hace un filtro
de cruce, qué es un Linkwitz-Riley y en qué se diferencia el cruce activo del pasivo; qué clase de
etapa rinde más y por qué; qué nivel de entrada corresponde a una sensibilidad de 0,775 V o de
1,4 V; cómo se conecta una etapa en puente; qué es el factor de amortiguamiento; qué es un array
lineal, cómo cae su nivel en campo cercano y en campo lejano y qué es la distancia de transición;
cuánto retardo lleva un refuerzo y a cuál de los altavoces se aplica; qué son los monitores de
escenario e intrauriculares y qué cuidado piden los transmisores de estos; cuánto cae el nivel al
doblar la distancia y en qué condiciones; qué es la distancia crítica y cómo se estima; qué son la
NAG y la PAG, qué distancias intervienen, cuál conviene cambiar primero, qué margen de estabilidad
se deja y cuánto se pierde al doblar los micrófonos abiertos; en qué orden se gana margen contra el
acople; qué hace una sala al sonido de un sistema. En la prueba práctica: calcular el nivel que da
un altavoz a una distancia, el retardo de un refuerzo, la ganancia necesaria y la potencial de un
montaje, y resolver un acople.

<!-- indice -->

## Índice

- [Sonorización](#sonorización)
  - [Qué es sonorizar](#qué-es-sonorizar)
  - [Las dos exigencias de un sistema](#las-dos-exigencias-de-un-sistema)
- [Altavoces](#altavoces)
  - [El altavoz electrodinámico](#el-altavoz-electrodinámico)
  - [La caja acústica](#la-caja-acústica)
  - [La directividad](#la-directividad)
  - [La sensibilidad](#la-sensibilidad)
  - [El filtro de cruce](#el-filtro-de-cruce)
  - [Impedancia del altavoz](#impedancia-del-altavoz)
- [Amplificadores](#amplificadores)
  - [La etapa de potencia y sus clases](#la-etapa-de-potencia-y-sus-clases)
  - [La sensibilidad de entrada](#la-sensibilidad-de-entrada)
  - [Los modos de funcionamiento](#los-modos-de-funcionamiento)
  - [La salida: conectores, cable y amortiguamiento](#la-salida-conectores-cable-y-amortiguamiento)
  - [Potencia de etapa y altavoz](#potencia-de-etapa-y-altavoz)
- [PA](#pa)
  - [Qué es la PA](#qué-es-la-pa)
  - [Los arrays lineales](#los-arrays-lineales)
  - [Los refuerzos y la alineación temporal](#los-refuerzos-y-la-alineación-temporal)
- [Monitores](#monitores)
  - [Monitores de escenario](#monitores-de-escenario)
  - [La cuña y el micrófono](#la-cuña-y-el-micrófono)
  - [Los transmisores de monitores intrauriculares](#los-transmisores-de-monitores-intrauriculares)
- [Cobertura](#cobertura)
  - [La ley del cuadrado inverso](#la-ley-del-cuadrado-inverso)
  - [El nivel que da un altavoz en el público](#el-nivel-que-da-un-altavoz-en-el-público)
  - [Cubrir con varios altavoces](#cubrir-con-varios-altavoces)
  - [La distancia crítica](#la-distancia-crítica)
- [Realimentación](#realimentación)
  - [Qué es el acople](#qué-es-el-acople)
  - [La ganancia necesaria (NAG)](#la-ganancia-necesaria-nag)
  - [La ganancia potencial antes de la realimentación (PAG)](#la-ganancia-potencial-antes-de-la-realimentación-pag)
  - [El margen de estabilidad](#el-margen-de-estabilidad)
  - [Los micrófonos abiertos (NOM)](#los-micrófonos-abiertos-nom)
  - [Cómo se aplica la ecuación a un sistema real](#cómo-se-aplica-la-ecuación-a-un-sistema-real)
  - [DS, la corrección más rápida](#ds-la-corrección-más-rápida)
  - [Las cinco maneras de ganar margen](#las-cinco-maneras-de-ganar-margen)
- [Acústica de salas](#acústica-de-salas)
  - [Lo que la sala añade al sistema](#lo-que-la-sala-añade-al-sistema)
  - [La reverberación y el sistema](#la-reverberación-y-el-sistema)
  - [Los modos y los graves](#los-modos-y-los-graves)
  - [Lo que la sala le manda al técnico de sonorización](#lo-que-la-sala-le-manda-al-técnico-de-sonorización)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Sonorización

### Qué es sonorizar

Sonorizar es hacer llegar un sonido al público de un recinto o de un espacio abierto con el nivel y
la claridad suficientes, reforzando la fuente con un sistema electroacústico. La cadena, de oficio,
es siempre la misma:

| Eslabón | Qué hace | Dónde se estudia |
|---|---|---|
| Fuente y micrófono | Convierte la voz o el instrumento en señal | Tema 3 |
| Mesa | Mezcla y reparte a sala y a monitores | Tema 4 |
| Procesado de sistema | Ecualiza, retarda y reparte en vías (filtro de cruce) | Este tema y tema 5 |
| Etapa de potencia | Da a la señal la potencia que mueve el altavoz | «Amplificadores» |
| Altavoz | Convierte la señal en presión sonora | «Altavoces» |
| Sala | Añade reflexiones y reverberación | «Acústica de salas» y tema 1 |

La sala es parte de la cadena de audio, y es la única parte que no se puede cambiar por otra.

### Las dos exigencias de un sistema

Todo el tema se ordena alrededor de dos exigencias que tiran en sentido contrario:

1. Que llegue nivel suficiente y parejo a todo el público, también al más lejano: es la
   cobertura, y su medida es la ganancia necesaria (NAG), que se calcula en «Realimentación».
2. Que el sistema no se acople: el sonido de los altavoces vuelve al micrófono, y la ganancia que
   el sistema puede dar antes de acoplar (PAG) es limitada.

Shure lo resume en una frase que vale de regla: **«if the dimensions of a sound system don't provide
the needed gain with the theoretical free field conditions, then they are even less likely to work
under real world conditions»** (si las dimensiones de un sistema no dan la ganancia necesaria en
campo libre teórico, menos aún funcionarán en condiciones reales).

## Altavoces

### El altavoz electrodinámico

Es el que lleva casi todo lo que suena. Sus piezas:

| Pieza | Qué hace |
|---|---|
| Imán permanente y yugo | Crean el campo magnético fijo en el que trabaja la bobina |
| Bobina móvil | Recibe la corriente de audio y se mueve dentro de ese campo |
| Diafragma o cono | Convierte ese movimiento en presión sobre el aire |
| Araña | Centra la bobina y la devuelve a su sitio: es una suspensión, no un contacto |
| Suspensión exterior | Cierra el borde del cono y limita el recorrido |

En un altavoz electrodinámico, la fidelidad depende de que la relación entre la longitud de la
bobina móvil y su número de espiras sea la acertada. Por qué: la fuerza que mueve el cono es
proporcional a cuántas espiras están dentro del campo magnético. Si la bobina se sale del
entrehierro cuando el cono llega lejos, la fuerza deja de ser proporcional a la corriente y aparece
distorsión. La relación entre longitud de bobina y altura del entrehierro es lo que decide que el
altavoz siga siendo lineal en todo su recorrido, y ésa es la definición de fidelidad.

Tres ideas equivocadas que conviene saber rebatir, porque suenan bien:

1. Que la araña asegure un contacto de la bobina con el imán y el yugo: la bobina NO debe tocar
   nada. Si roza, el altavoz rasca. La araña la mantiene centrada SIN contacto.
2. Que convenga aprovechar las vibraciones transmitidas a la carcasa del bafle: una caja que vibra
   añade sonido que no está en la señal. Las cajas se refuerzan por dentro precisamente para que
   no lo hagan.
3. Que el campo magnético del imán deba ser lo más ligero posible: a más campo, más fuerza y más
   control.

### La caja acústica

La capacidad de una caja acústica se mide en litros. La caja acústica no es un componente eléctrico,
es un VOLUMEN de aire. Y el volumen de aire encerrado detrás del cono se comporta como un muelle
que interviene en el comportamiento del altavoz, sobre todo en graves. La trampa está en la palabra
«capacidad»: en electricidad la capacidad se mide en faradios.

| Tipo | Cómo es | Qué consigue |
|---|---|---|
| Cerrada | Volumen sellado | Respuesta más controlada y caída suave en graves |
| Bass-reflex | Lleva un tubo o puerto sintonizado | Más rendimiento en graves a cambio de una caída más brusca por debajo |
| De pabellón (*horn*) | Acopla el cono al aire por una bocina | Rendimiento muy alto y directividad controlada: es la de refuerzo sonoro grande |

### La directividad

En un altavoz, lo que indica cómo se distribuye su radiación en el espacio es la directividad. Es el
mismo concepto que el diagrama polar del micrófono (tema 3), del otro lado de la cadena: allí dice
de dónde capta; aquí dice hacia dónde emite. No la describen la impedancia, la distorsión ni la
potencia, que son otras especificaciones del mismo altavoz.

Y su regla fundamental es la de la longitud de onda (tema 1): un altavoz es direccional cuando
su diámetro es comparable o mayor que la longitud de onda que emite. De ahí que:

1. Los graves sean prácticamente omnidireccionales: una onda de cinco metros rodea cualquier
   caja. Por eso el subgrave se puede poner donde quepa y por eso se oye la fiesta del vecino.
2. Los agudos sean muy direccionales: fuera del eje se pierden. Por eso un sistema mal
   apuntado suena apagado en las esquinas.
3. La bocina exista: es la manera de dar directividad controlada a las frecuencias medias y
   altas, y de cubrir un público concreto sin iluminar las paredes.

Con 340 m/s, la onda de cinco metros es la de 68 Hz, y la de 2 kHz mide 17 cm (cálculo con la cifra
de oficio del tema 1): un cono de 30 cm es pequeño para la primera y grande para la segunda.

### La sensibilidad

Una sensibilidad de 90 dB/W/m significa que el altavoz produce un nivel de presión sonora de 90
decibelios cuando se le suministra 1 vatio de potencia y se mide a 1 metro de distancia.

La especificación tiene tres partes y las tres están en el nombre: decibelios de presión, por
vatio de entrada, a un metro. Es un rendimiento: cuánta presión da por cuánta potencia recibe.

| Cambio | Efecto en el nivel |
|---|---|
| Doblar la POTENCIA | +3 dB |
| Doblar la DISTANCIA | −6 dB |
| +3 dB de sensibilidad | La mitad de potencia para el mismo nivel |

Con ella se entiende por qué la sensibilidad importa más que la potencia: un altavoz de 93 dB/W/m
con 100 vatios suena igual que uno de 90 dB/W/m con 200. Tres decibelios de sensibilidad valen por
doblar la etapa.

La regla de la distancia supone campo libre; dentro de una sala, lejos del altavoz, la caída real es
menor (se ve en «Cobertura»). El nivel que da un altavoz a una distancia se calcula en ese epígrafe.

### El filtro de cruce

Qué hace un filtro de cruce: repartir el espectro entre las vías del sistema. Manda los
graves al altavoz de graves y los agudos al de agudos, porque ningún transductor cubre bien las
diez octavas del margen audible.

Linkwitz-Riley es un tipo de filtro de cruce, y es el nombre que conviene conocer porque es el que
resuelve el problema de la suma en la frecuencia de corte. En un cruce, las dos vías emiten a la vez
alrededor del punto de corte, y lo que se oye es la SUMA de las dos. Un filtro mal elegido suma con
un bache o con un pico. El Linkwitz-Riley está diseñado para que las dos vías, sumadas, den respuesta
plana y en fase.

Y el filtro de cruce puede estar en dos sitios, que es lo que separa dos formas de montar un
sistema:

| Dónde | Cómo es | Dónde se usa |
|---|---|---|
| Pasivo | Bobinas y condensadores DENTRO de la caja, después de la etapa | Cajas de estudio y de instalación pequeña |
| Activo | Antes de las etapas, con una etapa por vía | Refuerzo sonoro profesional: más control y mejor rendimiento |

### Impedancia del altavoz

El altavoz es la carga de la etapa, y su impedancia nominal decide cuánta corriente pide (TI da como típica de los altavoces una resistencia en continua de 4 u 8 ohmios). Cómo se asocian altavoces en serie y en paralelo, por qué una impedancia baja
pierde más en el cable y por qué la megafonía usa línea de 100 voltios se desarrolla en el tema 2.
La regla práctica que aquí importa: la impedancia resultante de los altavoces colgados de un canal no puede bajar de la mínima que admite la etapa (Crown da mínimos distintos según el modelo y el modo).

## Amplificadores

### La etapa de potencia y sus clases

La etapa de potencia recibe de la mesa o del procesador una señal de línea y la convierte en la
tensión y la corriente que mueven el altavoz. Las clases A, B, AB y C se definen por qué parte del ciclo conduce el transistor de salida, y la D, por conmutar; están en el tema 2. Lo que decide en sonorización es el
rendimiento, y lo cifra TI: **«Class AB exhibits a theoretical peak efficiency of 78%, and is only
30% - 40% efficient at normal operating levels. Efficiency is where the switching, or Class D, audio
amplifier has large advantages over linear classes.»** (La clase AB tiene un rendimiento teórico
máximo del 78 % y sólo del 30 al 40 % a niveles normales; ahí la clase D, conmutada, tiene grandes
ventajas.) Su ejemplo: **«a 90% efficient amplifier at 1W output dissipates 100mW»** (un
amplificador con rendimiento del 90 % que entrega 1 W disipa 100 mW). La cifra es redondeada: por cálculo, para entregar 1 W al 90 % entran unos 1,11 W y se disipan unos 111 mW. La clase D **«outputs a high
frequency PWM signal»**: su salida es una señal de alta frecuencia modulada en anchura de impulsos, de la que se extrae el audio con un filtro de salida paso bajo o, en los diseños sin filtro que estudia la nota de TI, con el propio altavoz, que se comporta como un paso bajo.

La nota de TI trata de amplificadores para aparatos portátiles: vale para el concepto (lo que no se
convierte en potencia útil se convierte en calor), no para las cifras de potencia de una etapa de
sonorización. La consecuencia de oficio: a igual potencia, una etapa más eficiente pesa menos, se
calienta menos y pide menos a la red eléctrica.

### La sensibilidad de entrada

La sensibilidad de entrada de una etapa es el nivel de entrada que la lleva a su potencia nominal.
Crown la da en su selector: **«For amplifiers with a 0.775V position, this positions corresponds to
a 0 dBu level. The 1.4V position corresponds to a +4 dBu level. The 26 dB position is a fixed gain
position.»** (La posición de 0,775 V corresponde a un nivel de 0 dBu; la de 1,4 V, a +4 dBu; la de
26 dB es de ganancia fija.) La segunda equivalencia es redondeada: por cálculo, +4 dBu son unos 1,23 V y 1,4 V son unos +5 dBu. El 0 dBu es, por definición, 0,775 voltios (tema 2). La sensibilidad se
elige según el nivel nominal de lo que llega (tema 2): una mesa profesional trabaja a +4 dBu.

### Los modos de funcionamiento

Una etapa de dos canales puede trabajar en estéreo (dos canales independientes) o en mono, de dos
maneras que Crown describe:

| Modo | Cómo se conecta (Crown) |
|---|---|
| Puente mono | **«Place the MODE switch [...] in the Bridge-Mono position. The input connector should be inserted into channel one [...]. Connect the speaker leads across the two red binding posts»** (selector en puente mono, la señal por la entrada del canal uno y el altavoz entre los dos bornes rojos) |
| Paralelo mono | Las dos salidas rojas unidas por un puente y el altavoz **«across the red and black binding posts»** (entre el borne rojo y el negro) |

Cuándo conviene cada uno lo decide la carga. Crown: **«Generally, the deciding factor to this dilemma is the total speaker load impedance you wish to drive.»** (Lo que decide, en general, es la impedancia total de altavoces que se quiere mover.) El puente mono da **«the most power available when driving 8 or 4-ohm loads»** (la mayor potencia con cargas de 8 o 4 ohmios, en sus Micro-Tech y Macro-Tech; en Power-Tech y Com-Tech, 8 ohmios o más); **«Parallel Mono can be used when driving lower impedance loads»** (el paralelo mono sirve para cargas de impedancia más baja: hasta 1 ohmio en Micro-Tech y Macro-Tech, hasta 2 en Power-Tech y Com-Tech). La mayor ventaja del paralelo mono, según Crown, es un número impar de cajas: con tres, en lugar de dos en un canal y una en el otro, se ponen las tres en paralelo y **«the power is distributed equally to all three speakers»** (la potencia se reparte por igual entre las tres).

No todos los modelos admiten los dos modos; el manual de cada etapa manda.

### La salida: conectores, cable y amortiguamiento

- Conector: el Speakon. Crown: **«Speakons allow both channels of amplifier output to be wired to
  the same connector»** (permite llevar las dos salidas de la etapa por el mismo conector); el
  modelo que cita es el **«NL4FC»**.
- Factor de amortiguamiento. Crown: **«Damping factor is the ratio of the rated speaker impedance to
  the amplifier's output impedance.»** (Es la relación entre la impedancia nominal del altavoz y la
  impedancia de salida de la etapa.) Si la etapa no controla las resonancias del altavoz, **«the
  speaker output can have an over accentuated or "boomy" bass sound»** (el grave suena exagerado,
  «retumbante»). La impedancia de salida es baja gracias a la **«negative voltage feedback»**
  (realimentación negativa de tensión).
- Cable. Crown: **«The longer the run, the heavier gauge you will need to minimize power and
  damping factor loss.»** (Cuanto más larga la tirada, más grueso el cable, para no perder potencia
  ni factor de amortiguamiento.) Su orientación: **«runs of 25 Ft or less work well with 14 gauge.
  Over 25 one should use 12 gauge if possible»** (hasta 25 pies —unos 7,6 m— basta un calibre
  AWG 14; por encima, un AWG 12 si es posible). Es recomendación de fabricante, no norma; en el AWG,
  a número menor, cable más grueso.

### Potencia de etapa y altavoz

La potencia de la etapa se elige con la del altavoz y con el nivel que se quiere en el público, que
se calcula en «Cobertura». La regla de la sensibilidad lo ordena: doblar la etapa da sólo 3 dB, así
que para ganar 10 dB hace falta diez veces la potencia (10 × log 10 = 10 dB). Por eso, antes que
subir potencia, se busca más sensibilidad, acercar el altavoz al público o sumar cajas.

## PA

### Qué es la PA

En el oficio, la PA es el sistema principal que cubre al público, frente a los monitores, que
sirven a quien está en el escenario. Una PA grande suele combinar un sistema principal (a menudo un
array lineal), subgraves, refuerzos para las zonas a las que el principal no llega y un procesador
que hace el cruce, la ecualización y los retardos. Es costumbre de oficio, sin norma que la defina.

### Los arrays lineales

Un array lineal es una línea de altavoces que trabaja como una sola fuente alargada. Ureda (JBL)
recuerda el antecedente con una cita de Klepper y Steele, de 1963: **«Line-source loudspeaker arrays, often called ‘column’
loudspeakers»** (los arrays de fuente lineal, a menudo llamados «columnas»). Las columnas clásicas
eran una pila de altavoces de toda la banda con una directividad vertical que cambiaba mucho con la
frecuencia; los fabricantes actuales ponen en los agudos **«specially designed waveguides»** (guías
de onda diseñadas para ello), y así los sistemas de hoy **«behave more like continuous line
sources»** (se comportan más como fuentes lineales continuas).

Lo que distingue a una fuente lineal es cómo cae su nivel con la distancia:

| Zona | Cómo cae el nivel (Ureda) |
|---|---|
| Campo cercano | **«undulates near the source while generally decreasing in level at −3 dB per doubling of distance»** (ondula cerca de la fuente y en general cae 3 dB por cada duplicación de la distancia) |
| Distancia de transición | **«the undulations disappear and the response falls off at −6 dB»** (desaparecen las ondulaciones y la caída pasa a 6 dB) |
| Campo lejano | Más allá de la distancia de transición: 6 dB por duplicación, la misma caída que da la ley del cuadrado inverso («Cobertura») |

**«The near field is defined as the region between the source and the transition distance. Beyond
the transition distance is the far field.»** Y **«The transition distance is a function of the line
source length and frequency»**: depende de la longitud de la línea y de la frecuencia. El ejemplo del
artículo: una línea recta de 4 m a 8 kHz cae 3 dB por duplicación hasta unos 100 m y, más allá, 6 dB.

Las formas: además de la recta, **«curved (arc), J, and progressive line arrays»** (en arco, en J y
progresivos). La razón de curvarlos: las líneas rectas dan, a longitudes grandes y frecuencias altas,
diagramas **«very narrow, often too narrow for sound-reinforcement venues»** (muy estrechos, a menudo
demasiado para un recinto de refuerzo sonoro), mientras que las de arco dan diagramas más anchos que
se acercan, en agudos, al ángulo que abre el arco.

La consecuencia de oficio: dentro del campo cercano, el público de delante y el de atrás reciben
niveles más parecidos que con una caja suelta (3 dB por duplicación en lugar de 6).

### Los refuerzos y la alineación temporal

En un recinto largo se ponen refuerzos a mitad de sala. Si esos refuerzos no se retrasan, el
público de esa zona oye primero el refuerzo y después el escenario, y la voz parece venir del
altavoz de al lado en vez de la persona que habla. Con el retardo bien puesto, el escenario llega
primero o a la vez y el oído sigue localizando allí la fuente. Es el efecto de precedencia, que se
da como oficio.

El caso tipo: dos altavoces a 4 y a 38 metros de un oyente. La cuenta, con 340 metros por segundo:

1. La diferencia de camino: 38 − 4 = 34 metros.
2. El tiempo de esos 34 metros: 34 ÷ 340 = 0,1 segundos = 100 milisegundos.

Y la parte que la pregunta mide de verdad no es la cuenta, sino A CUÁL se le aplica: al MÁS
CERCANO. El sonido del lejano ya va retrasado por el camino que tiene que recorrer; lo único que
se puede hacer es esperar al que llega antes. Retrasar el lejano lo empeoraría.

El atajo que conviene tener, y con él estas preguntas se hacen de cabeza: el sonido recorre
aproximadamente un metro cada 3 milisegundos. 34 metros, unos 100 milisegundos.

La velocidad real depende de la temperatura; los 340 m/s son la cifra redonda de oficio (tema 1).

## Monitores

### Monitores de escenario

Los monitores devuelven a quien está en el escenario (músicos, presentadores, ponentes) lo que
necesita oír para actuar: su voz, la base, los demás. Hay dos familias, de oficio:

| Tipo | Qué es | Qué ventaja y qué riesgo tiene |
|---|---|---|
| Cuña (monitor de suelo) | Una caja inclinada en el suelo, apuntando al artista | Fácil y sin radio; es un altavoz abierto junto al micrófono, así que es la primera fuente de acople |
| Intrauricular (IEM) | Auriculares de inserción que reciben la mezcla, casi siempre por radio | Quita energía acústica del escenario; exige gestionar transmisores y frecuencias (tema 12) |

La mezcla de monitores sale de envíos auxiliares de la mesa, uno por mezcla (tema 4); en montajes
grandes, de una mesa propia de monitores.

### La cuña y el micrófono

La cuña se coloca donde el micrófono menos capta, es decir, en su nulo: con un cardioide, justo
detrás, a 180°; con un supercardioide o un hipercardioide, a los lados del eje trasero, porque justo
detrás tienen un lóbulo (los ángulos, en el tema 3). Es la aplicación directa de la PAG: la cuña es
el altavoz más cercano al micrófono (la D1 más corta del sistema), y un micrófono direccional bien
orientado da margen.

### Los transmisores de monitores intrauriculares

Los transmisores de los IEM suelen ir juntos en un rack, y Shure explica que en estos sistemas la
combinación de antenas **«is used to reduce the number of transmitting antennas, i.e. the antenna
combiner allows all the transmitters to share a common antenna»** (sirve para reducir el número de
antenas emisoras: todos los transmisores comparten una). Y avisa: **«Several closely-spaced,
high-power transmitters suffer from excessive intermodulation (a transmitter interaction that
produces additional frequencies) problems»** (varios transmisores de alta potencia muy juntos sufren
intermodulación excesiva, una interacción que produce frecuencias adicionales). La regla: **«a
passive combiner should be used for combining two transmitters. For more than two, though, an active
combiner is recommended. An active antenna combiner will typically accept between 4 to 8
transmitters.»** (Para dos transmisores, combinador pasivo; para más de dos, uno activo, que suele
admitir de 4 a 8.) Una prohibición: **«active antenna combiners should never be “actively”
cascaded»** (los combinadores activos nunca se encadenan uno tras otro); si hace falta más de uno,
se unen con un pasivo. Y el precio del pasivo, que Shure cifra al tratar la combinación de antenas de varias salas: **«A passive combiner will typically result in at least 3 dB of loss»** (al menos 3 dB de pérdida); para los IEM, pide tener en cuenta esas pérdidas del pasivo. Las bandas, la
coordinación de frecuencias y la intermodulación, en el tema 12.

## Cobertura

### La ley del cuadrado inverso

Cubrir es dar a todo el público un nivel suficiente y parecido. La herramienta es la ley del
cuadrado inverso, que Shure enuncia así: **«as listeners double their distance from the sound
source, the SPL they perceive will decrease by 6.02dB»** (cada vez que el oyente dobla su distancia
a la fuente, el nivel de presión sonora que percibe baja 6,02 dB). Su fórmula:

**L' = L + 20 log D - 20 log D'**

donde L es el nivel a la distancia D y L' el nivel a la nueva distancia D'. Da lo mismo medir en
metros o en pies, porque lo que cuenta es la relación entre las dos distancias. Y la regla que
Shure saca de ella: para cambiar el nivel de forma apreciable, **«the distance must change by double
or half»** (la distancia tiene que doblarse o reducirse a la mitad).

Sus dos condiciones, que el tribunal puede preguntar: vale en **«a so-called "free field."»** (un
«campo libre»), sin reflexiones, y para una **«point source (a sound source which has much smaller
dimensions than the distance to the listener)»** (fuente puntual: mucho más pequeña que la distancia
al oyente). Un array lineal en su campo cercano no la cumple (3 dB por duplicación, en «PA»), y
tampoco una sala lejos de la fuente (en «La distancia crítica»).

Para leer las cifras, Shure da esta escala de percepción: **«A one dB increase is barely audible,
3dB is a generally noticeable change, and a 10dB increase is considered to be twice as loud.»** (Un
decibelio apenas se oye, tres se notan y diez se perciben como el doble de fuerte.)

### El nivel que da un altavoz en el público

Con la sensibilidad, la potencia y la distancia se calcula el nivel en campo libre:

SPL a la distancia d = sensibilidad (dB/W/m) + 10 × log (potencia en W) − 20 × log (d en m)

Ejemplo de cálculo: un altavoz de 97 dB/W/m con 400 W da 97 + 26 = 123 dB SPL a 1 m; a 32 m
(cinco duplicaciones, 30 dB) quedan unos 93 dB. Para tener 6 dB más al fondo harían falta cuatro
veces la potencia (1.600 W), o un altavoz 6 dB más sensible, o acercar un refuerzo al público. En
una sala real el fondo recibe algo más, porque se suma la reverberación, pero ese sonido no aporta
claridad (se ve en «La distancia crítica»). Son cuentas de decibelios, sin norma detrás; el límite
real lo pone también la potencia que admite el altavoz, que da su fabricante.

### Cubrir con varios altavoces

La cobertura se consigue apuntando: los agudos van donde apunta la caja (en «La directividad»), así
que cada caja se orienta al público que le toca y no a las paredes. Cuando hacen falta varias
fuentes, Shure avisa de su efecto: **«multiple speaker locations tend to act like late echoes if they
arc [sic: are] far apart»** (varios altavoces muy separados actúan como ecos tardíos), con filtro en peine
(tema 1) y pérdida de inteligibilidad, algo que **«is minimized by a single loudspeaker or closely
spaced array if it can be placed far from the talker and close enough to the listeners»** (se
reduce con un altavoz único o un grupo de altavoces juntos, lejos de quien habla y cerca de quien
escucha). Si los refuerzos lejanos son inevitables, se retrasan (en «Los refuerzos y la alineación
temporal»).

### La distancia crítica

Shure: **«The term "critical distance" is defined as the distance from a sound source where the
direct sound is the same level as the reverberant sound.»** (La distancia crítica es aquella a la
que el sonido directo de una fuente tiene el mismo nivel que el reverberante.) Dentro de ella manda
el directo y **«the inverse square law works pretty well. Outside the critical distance things get
much more complex.»** (la ley del cuadrado inverso funciona bastante bien; fuera, las cosas se
complican mucho).

Cómo se estima, según Shure, con un sonómetro y una radio de FM desintonizada que da un ruido
constante de banda ancha: alejándose de la fuente hasta que el medidor deja de bajar, y volviendo
hacia ella hasta que suba exactamente 3 dB: **«Equal sound from the direct source and the
reverberant field add up to 3dB more than the reverberant sound alone.»** (Directo y reverberante
iguales suman 3 dB más que el reverberante solo.)

Y la conclusión útil: **«Typically in sound systems, the distance between the microphone and the
talker is the only place where the system component receiver (the listener or microphone) is less
than the critical distance from the source.»** (En un sistema, la distancia entre quien habla y el
micrófono suele ser la única en la que el receptor está dentro de la distancia crítica.) De ahí que
sea la distancia que más rinde cambiar (en «Realimentación»).

## Realimentación

### Qué es el acople

El acople se produce cuando el sonido de los altavoces vuelve al micrófono con nivel suficiente para
que el lazo se sostenga solo. Se dispara a la frecuencia en la que la ganancia del lazo llega
primero a uno (tema 5). Cómo acopla cada patrón de micrófono (el direccional, de golpe y en agudos;
el omnidireccional, poco a poco y en medios graves o graves), en el tema 3.

### La ganancia necesaria (NAG)

La ganancia necesaria es la que el sistema tiene que dar para que el oyente más lejano oiga a quien
habla como lo oye el más cercano. Se calcula con la ley del cuadrado inverso. El ejemplo de Shure:
en una mesa de reunión, la voz da unos 70 dB a 2 pies de quien habla; el oyente del otro extremo está
a 22 pies y recibe 49 dB, 21 dB menos. **«This is called the needed acoustic gain (NAG)»**: el
sistema tiene que aportar al menos esos 21 dB. Con un sonómetro, basta medir en las dos posiciones y
restar.

### La ganancia potencial antes de la realimentación (PAG)

La ganancia que el sistema puede dar antes de acoplar depende de cuatro distancias:

| Distancia | Entre qué y qué (Shure) | Para ganar margen |
|---|---|---|
| D1 | **«the distance between the microphone and the loudspeaker»** (micrófono y altavoz) | Hacerla lo mayor posible |
| D2 | **«the distance between the loudspeaker and the farthest listener»** (altavoz y oyente más lejano) | Hacerla lo menor posible |
| D0 | **«the distance between the talker and the farthest listener»** (quien habla y oyente más lejano) | Mayor, pero casi siempre la fija la sala |
| DS | **«the distance between the talker and the microphone»** (quien habla y micrófono) | Lo menor posible: es la que más rinde |

La ecuación en su forma simple:

**PAG = 20 log D1 - 20 log D2 + 20 log D0 - 20 log DS**

Sus supuestos: **«omnidirectional microphones and loudspeakers and it neglects the effects of
reverberation and echo (as if the system were outdoors)»** (micrófonos y altavoces
omnidireccionales, sin reverberación ni eco, como al aire libre). El sistema funciona si la PAG es
igual o mayor que la NAG.

El ejemplo de Shure, en pies (las distancias van en relación, y la unidad da igual): con D1 = 9,
D2 = 20, D0 = 22 y DS = 1, la PAG es 19 − 26 + 27 − 0 = 20 dB, uno menos de los 21 que hacen falta.
Alejando el altavoz del micrófono y acercándolo al oyente (D1 = 11, D2 = 19) sube a 22 dB.

### El margen de estabilidad

Shure: **«Virtually all systems need to be operated with a safety margin (called the feedback
stability margin), usually 6dB, to avoid the annoying ringing sound associated with a pre-feedback
condition.»** (Casi todos los sistemas necesitan un margen de seguridad, el margen de estabilidad
frente a la realimentación, normalmente de 6 dB, para evitar el «zumbido» o timbre que precede al
acople.) La ecuación queda:

**PAG = 20 log D1 - 20 log D2 + 20 log D0 - 20 log DS - 6**

Con él, el montaje de 22 dB se queda en 16, y no llega. Con D1 = 17,5 y D2 = 13 sale, con las cifras
redondeadas de la fuente, 25 − 22 + 27 − 0 − 6 = 24 dB: 3 dB por encima de la NAG.

### Los micrófonos abiertos (NOM)

Cada micrófono abierto es otro camino de vuelta. La ecuación completa:

**PAG = 20 log D1 – 20 log D2 + 20 log D0 – 20 log DS – 10 log NOM - 6**

Con un micrófono el término vale cero; con dos, 3 dB; con cuatro, 6: **«each time the NOW doubles,
the PAG is decreased by 3dB»** (cada vez que se dobla el número de micrófonos abiertos, la PAG baja
3 dB; «NOW» es errata de la fuente por NOM). En el ejemplo, abrir un segundo micrófono deja la PAG en
21 dB, justo la NAG (la fuente escribe «11 dB» por errata; la resta, 24 − 3, da 21), y con ocho se
come el margen de seguridad entero. Conclusión de Shure: **«the number of open microphones needs to be
limited as much as possible»** (hay que limitar lo más posible los micrófonos abiertos). Las
soluciones: que el técnico cierre los que no se usan, un interruptor en cada micrófono o, la más
práctica según Shure, un mezclador automático de micrófonos, que abre cada canal cuando el sonido que capta supera un umbral o, en los de tecnología más nueva, el ruido de fondo.

### Cómo se aplica la ecuación a un sistema real

- El peor caso de cada distancia: Shure manda tomar el oyente más lejano para D0, la mayor distancia
  previsible entre quien habla y el micrófono para DS, el altavoz más cercano al oyente más lejano
  para D2 y **«the loudspeaker closest to the microphone for D1»** (el altavoz más cercano al
  micrófono para D1).
- Micrófonos y altavoces direccionales dan margen, pero **«The practical limit on the improvement
  that these components can make is usually considered to be about 6dB»** (su mejora práctica se
  suele cifrar en unos 6 dB).
- La sala resta: dentro de un recinto, lo que llega al micrófono desde el altavoz (D1, fuera de la
  distancia crítica) es más de lo que predice la ley, y la PAG real es menor que la calculada.

### DS, la corrección más rápida

Doblar la distancia entre quien habla y el micrófono cuesta 6 dB de ganancia; reducirla a la mitad
los da: de 1 pie a medio pie, +6 dB. Shure lo llama **«one of the first rules in microphone
application: get the microphone as close as possible to the sound source»** (una de las primeras
reglas de la microfonía: el micrófono, lo más cerca posible de la fuente), y es la distancia más
fácil de cambiar porque es la más corta. Además, si DS supera la distancia crítica de quien habla, el
micrófono capta más sala y se pierde inteligibilidad.

### Las cinco maneras de ganar margen

Las cinco maneras de ganarle margen, en orden de eficacia:

1. Acercar el micrófono a la fuente. Cada mitad de distancia da 6 decibelios más de señal útil
   sin subir nada.
2. Alejar los altavoces del micrófono y apuntarlos donde el micrófono no capta —los nulos del
   tema 3—.
3. Usar micrófonos direccionales.
4. Tratar la sala: menos reverberación es menos energía volviendo.
5. Y sólo al final, ecualizar con un notch las frecuencias que se disparen.

El orden importa: ecualizar es lo último porque es lo que menos margen da y lo que más
deteriora el sonido. El orden es de oficio; Shure respalda acercar el micrófono, alejar el altavoz y los componentes direccionales (con su límite práctico de unos 6 dB), y a ellos se suman limitar los micrófonos abiertos y acercar el altavoz al público. El filtro notch, en el tema 5.

## Acústica de salas

### Lo que la sala añade al sistema

La acústica de la sala (sonido directo, reflexiones, tiempo de reverberación, modos, sala para la
palabra y para la música) se desarrolla en el tema 1. Aquí se recoge lo que decide la sonorización.

| Componente | Qué es | Qué aporta |
|---|---|---|
| Sonido directo | Lo que llega en línea recta | La inteligibilidad y la localización |
| Primeras reflexiones | Los rebotes que llegan en los primeros milisegundos | Refuerzan si llegan pronto; estorban si llegan tarde |
| Cola reverberante | La suma de miles de rebotes que decae | El cuerpo, la envolvente y, si sobra, la confusión |

La frontera de los cincuenta milisegundos es la que decide: una reflexión que llega antes de ese
plazo el oído la SUMA al sonido directo y la percibe como refuerzo. La que llega después se
percibe como eco separado. Es convención de la psicoacústica, que se da como oficio.

Shure lo aplica a los altavoces: **«Early echoes tend to help intelligibility and later ones hurt
it. So if a loudspeaker needs to be "somewhat near" the ceiling, put it close to the ceiling to take
advantage of the early echoes produced within a few feet of the reflective surface.»** (Los ecos
tempranos ayudan a la inteligibilidad y los tardíos la perjudican; si un altavoz tiene que ir cerca
del techo, que vaya pegado a él, para aprovechar las reflexiones tempranas.)

### La reverberación y el sistema

El tiempo de reverberación es cuánto tarda el sonido de una sala en caer sesenta decibelios después
de que la fuente calle (RT60). Crece con el volumen de la sala y baja con la absorción; en un teatro, el público es el mayor absorbente, y la misma sala suena distinta vacía y llena (tema 1).

Lo que la reverberación le hace a un sistema:

1. Acorta la distancia crítica: más allá de ella, el público oye sobre todo sala, y subir el nivel
   sube también la sala. Lo que da claridad es acercar el sonido directo al oyente (altavoces más
   cerca, refuerzos) y apuntar al público, no a las superficies reflectantes.
2. Resta ganancia antes del acople: la ecuación de la PAG supone aire libre, y en una sala el
   micrófono recibe más energía del altavoz de la que predice la ley (en «Realimentación»).
3. Emborrona la palabra: una sala para la palabra quiere un RT60 corto, y la inteligibilidad se mide
   con el índice de transmisión de la palabra (STI); una para la música lo quiere más largo (tema 1).
   Y la solución de compromiso de las salas polivalentes es mecánica, no electrónica: cortinas,
   paneles giratorios y techos móviles que cambian la absorción de la sala según el uso.

### Los modos y los graves

Las superficies que favorecen en mayor medida la producción de ondas estacionarias en una sala son
las paralelas. Los modos son un problema de graves, y afectan a los subgraves de un sistema: en unos
puntos de la sala una frecuencia grave sobra y en otros casi desaparece. No se corrigen ecualizando.
Un mínimo de presión no se arregla subiendo esa banda: en ese punto la onda se cancela, y subir el
nivel sólo satura el resto de la sala. Se corrige con trampas de graves, con la geometría o moviendo
la escucha (y, en sonorización, moviendo el subgrave). El mecanismo y su cálculo, en el tema 1.

### Lo que la sala le manda al técnico de sonorización

| Decisión de oficio | Qué manda la acústica |
|---|---|
| Dónde poner el micrófono | Cuanto peor es la sala, más cerca: acercarse aumenta el directo y no la reverberación |
| Qué micrófono elegir | En sala mala, direccional: rechaza lo que viene de los lados y del fondo |
| Cuánta potencia hace falta | No la que cubra la sala, sino la que gane al ruido de fondo medido con las curvas NC |
| Dónde poner los altavoces | Lejos de las paredes y apuntando al público, no a las superficies reflectantes |
| Cuánta ganancia admite un directo | La que la sala deje antes de realimentar: la PAG, con su margen de 6 dB |

Las curvas NC de ruido de fondo se presentan en el tema 1.

## Lo que este tema no da, y dónde está

- Las normas de medida de altavoces, de etapas y de salas (definición normalizada de la sensibilidad,
  de la potencia de un altavoz, del tiempo de reverberación o del STI): no se han leído; el tema da
  las definiciones de oficio y las del fabricante.
- La cobertura angular de las cajas (ángulos horizontal y vertical) y su lectura en una hoja de
  datos, el diseño y la predicción de arrays lineales (ángulos entre cajas, curvado) y la fórmula de
  la distancia de transición: sin fuente leída.
- Las cuñas de escenario y la mezcla de monitores: sin fuente técnica publicada localizada; van como
  oficio. Los monitores de escucha del control de sonido y sus condiciones: fuera de este tema.
- Los procesadores de sistema y los supresores automáticos de realimentación, y las pendientes y
  órdenes del filtro Linkwitz-Riley: sin fuente leída.
- La megafonía de tensión constante (línea de 100 V) más allá de su razón de ser, y la asociación de
  altavoces: tema 2. Las clases de amplificador en detalle: tema 2.
- La velocidad del sonido exacta y su variación con la temperatura, y el efecto de precedencia como
  fenómeno psicoacústico: sin fuente leída (el tema 1 usa los 340 m/s y la frontera de los 50 ms
  como oficio). La acústica de salas en detalle: tema 1.
- Los patrones polares y la manera de acoplar de cada micrófono: tema 3. Los envíos auxiliares para
  monitores: tema 4. El filtro notch: tema 5. La radiofrecuencia de los monitores intrauriculares:
  tema 12. El ruido como riesgo para quien sonoriza: tema 16.
- Lo propio de CSRTV (equipos de sonorización, sistemas de PA de platós y de eventos, monitores): no
  consta en un documento publicado localizado.

## Trazabilidad

Fuentes leídas el 25/09/2026. El tema no cita normas legales.

| Fuente | Qué sostiene |
|---|---|
| Shure Incorporated, R. Frank, *Understanding Sound System Design and Feedback Using (Ugh!) Math*, ref. AL1174, sin fecha | La regla de campo libre; ley del cuadrado inverso (6,02 dB, fórmula, campo libre, fuente puntual, doblar o reducir a la mitad); escala de percepción de 1, 3 y 10 dB; varios altavoces separados como ecos tardíos; distancia crítica, su estimación y los 3 dB; DS como única distancia dentro de la crítica; NAG y ejemplo de 21 dB; las cuatro distancias; PAG y sus supuestos; ejemplos de 20, 22, 16 y 24 dB; margen de estabilidad de 6 dB; NOM y 3 dB por duplicación (con las erratas «NOW» y «11 dB»; en los ecos tardíos, «arc» por «are»); limitar micrófonos abiertos y mezclador automático; peor caso; límite práctico de unos 6 dB de los componentes direccionales; DS y la regla de acercar el micrófono; ecos tempranos y altavoz junto al techo |
| M. S. Ureda (JBL Professional), «Analysis of Loudspeaker Line Arrays», *J. Audio Eng. Soc.*, vol. 52, n.º 5, mayo de 2004 (copia docente de la Universidad Purdue) | Columnas y cita de Klepper y Steele (1963); guías de onda y fuentes lineales continuas; campo cercano a −3 dB, distancia de transición, campo lejano a −6 dB; dependencia de longitud y frecuencia; ejemplo de 4 m a 8 kHz y unos 100 m; formas recta, arco, J y progresiva; rectas demasiado estrechas y arcos más anchos |
| Crown Audio (Harman), FAQ «Professional Power Amplifiers», página web sin fecha | Sensibilidad de entrada (0,775 V, 1,4 V, 26 dB); puente mono y paralelo mono, cómo se conecta cada uno y cuándo conviene (impedancia total de la carga, mínimos por gama, número impar de cajas); Speakon y NL4FC; factor de amortiguamiento, grave «boomy» y realimentación negativa; calibre del cable (25 pies, AWG 14 y 12) |
| Texas Instruments, *AN-1497 Filterless Class D Amplifiers*, SNAA034A, mayo de 2006, revisada en mayo de 2013 | Rendimiento de la clase AB (78 %, 30-40 %) y ventaja de la clase D; ejemplo del 90 % y 100 mW; salida PWM; resistencia en continua típica de los altavoces (4 u 8 ohmios) |
| Shure, *Wireless Systems Guide for Antenna Setup*, G. Sigismondi y C. Tapia, 2013/2016 | Combinación de antenas de monitores personales; intermodulación entre transmisores cercanos; pasivo para dos, activo para más (4 a 8); no encadenar activos; al menos 3 dB de pérdida del pasivo (dada para varias salas) |
| Oficio, sin fuente publicada leída | Piezas del altavoz electrodinámico, fidelidad y las tres ideas equivocadas; tipos de caja; directividad y longitud de onda; lectura de la sensibilidad; filtro de cruce, Linkwitz-Riley y cruce activo o pasivo; alineación temporal y atajo de 3 ms por metro; las cinco maneras de ganar margen y su orden; componentes del sonido en sala, frontera de 50 ms, RT60, modos y salas polivalentes; qué es la PA; familias de monitores; cuña en el nulo; decisiones que manda la sala |

Oficio sin norma detrás, y así se declara: la cadena de sonorización; las piezas del altavoz
electrodinámico y la fidelidad como linealidad de la bobina; la caja como volumen en litros y los
tres tipos de caja; la directividad y su relación con la longitud de onda; la lectura de la
sensibilidad y su tabla; el filtro de cruce, el Linkwitz-Riley y el cruce activo y pasivo; las
impedancias habituales; la PA y sus partes; los refuerzos retardados y el efecto de precedencia; las
cuñas y los monitores intrauriculares como familias; la colocación de la cuña en el nulo; el orden de
las cinco maneras de ganar margen; la frontera de los 50 ms; lo que la sala le manda al técnico. Es
cálculo, y se puede rehacer: la onda de 68 Hz y la de 17 cm a 2 kHz; los 100 ms de 34 m a 340 m/s y
el atajo de 3 ms por metro; 7,6 m en 25 pies; diez veces la potencia para 10 dB; el nivel de 123 y 93
dB del ejemplo de sensibilidad; 21 = 24 − 3 en el ejemplo de micrófonos abiertos.
