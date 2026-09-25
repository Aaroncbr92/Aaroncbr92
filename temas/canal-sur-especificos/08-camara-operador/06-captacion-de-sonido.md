# Tema 6 del específico de Cámara Operador · Captación de sonido asociada a cámara

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Cámara Operador · punto 6 |
| **Sirve para** | Puesto 2.8, Cámara Operador (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Sin norma jurídica. Lo propio de la casa: *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, 1.ª ed., marzo de 2004). Normas técnicas: EBU R 68-2000 (nivel de alineación), EBU R 128-2023, EBU Tech 3341-2023 y EBU Tech 3343-2023 (sonoridad y pico verdadero). Documentación de fabricante: Sony, *PXW-Z200/HXR-NX800 Help Guide* (5-060-574-13(1), 2024); DPA Microphones, *Mic University* y diccionario (efecto de proximidad, línea balanceada, caída con la distancia). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | Las ediciones vigentes el 24/09/2026: EBU R 68-2000, EBU R 128 de noviembre de 2023 (versión 5), EBU Tech 3341 y Tech 3343 de noviembre de 2023; el Libro de estilo en su única edición publicada |
| **Extensión** | 10.700 palabras aproximadamente |

<!-- /portada -->

Siglas que usa el tema: Boletín Oficial de la Junta de Andalucía (**BOJA**); Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Unión Europea de Radiodifusión (**EBU**,
*European Broadcasting Union*); Sector de Radiocomunicaciones de la Unión Internacional de
Telecomunicaciones (**UIT-R**; en las citas en inglés, **ITU-R**); Sociedad de Ingeniería de Audio (**AES**, *Audio Engineering
Society*); captación electrónica de noticias (**ENG**, *electronic news gathering*); cámara réflex
digital de un solo objetivo (**DSLR**, *digital single-lens reflex*); hercio (**Hz**) y kilohercio
(**kHz**); micrómetro (**µm**); decibelio (**dB**); decibelios referidos a la escala completa digital
(**dBFS**, *decibels relative to full scale*); decibelios de pico verdadero (**dBTP**, *decibels
true peak*); decibelios referidos a 0,775 voltios (**dBu**); unidad de sonoridad (**LU**, *loudness
unit*) y unidades de sonoridad referidas a la escala completa (**LUFS**, *loudness units relative to
full scale*; su equivalente en la UIT es **LKFS**); margen de sonoridad (**LRA**, *loudness
range*); medidor de programa de cuasipico (**QPPM**, *quasi-peak programme meter*); nivel máximo
permitido (**PML**, *permitted maximum level*); control automático de ganancia (**AGC**, *automatic
gain control*); modulación por impulsos codificados (**PCM**, *pulse-code modulation*), y en su
forma lineal (**LPCM**, *linear pulse-code modulation*); código de tiempo (**TC**, *timecode*); conector de audio profesional de tres polos
(**XLR**); interferencia electromagnética (**EMI**, *electromagnetic interference*); razón de rechazo
en modo común (**CMRR**, *common mode rejection ratio*); nivel de presión sonora (**SPL**, *sound
pressure level*).

Los rótulos de menú y los mandos se escriben como los imprime el fabricante (***AUTO/MAN***,
***MIC+48V***, ***[Limiter Mode]***…): son rótulos de la máquina, no siglas.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.8, punto 6):
>
> Captación de sonido asociada a cámara: microfonía, niveles, sincronía, ambiente y criterios
> básicos.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué margen de frecuencias oye el ser humano; qué es un transductor y cuál
es el micrófono y cuál el altavoz; qué micrófonos necesitan alimentación fantasma y de cuántos
voltios; qué patrón polar tiene un micrófono de corbata, uno de mano o un cañón, y para qué sirve un
hipercardioide; qué es el efecto de proximidad y qué micrófonos lo tienen; por qué el XLR es una
línea balanceada y cómo rechaza el ruido; cuánto cae el nivel al doblar la distancia; qué es un grupo de frecuencias en un inalámbrico y por qué dos emisores van en el
mismo grupo; qué es el margen dinámico de un equipo y cuánto margen da cada bit; a qué nivel se
alinea el tono de 1 kHz en digital según la EBU (−18 dBFS) y por qué; qué es la sonoridad, cuál es
el nivel objetivo de la EBU R 128 (−23 LUFS) y el pico verdadero máximo en producción (−1 dBTP);
qué medidor recomienda la EBU para alinear; qué hacen el conmutador ***AUTO/MAN***, el limitador y
el filtro de viento de una cámara; cómo se sincroniza un sonido grabado aparte (claqueta, código de
tiempo); qué va por el canal 1 y qué por el canal 2 según el Libro de estilo de Canal Sur; si el
ambiente se graba siempre; qué pasa con el sonido en cámara lenta. En la prueba práctica: montar y
nivelar un micrófono de corbata inalámbrico y el ambiente en una cámara de hombro, grabar tono y
barras, y sincronizar una cámara con un grabador externo.

<!-- indice -->

## Índice

- [Captación de sonido asociada a cámara](#captación-de-sonido-asociada-a-cámara)
  - [Por qué el sonido es del operador de cámara](#por-qué-el-sonido-es-del-operador-de-cámara)
  - [El sonido y sus magnitudes](#el-sonido-y-sus-magnitudes)
  - [El margen de frecuencias audibles](#el-margen-de-frecuencias-audibles)
  - [Los transductores](#los-transductores)
  - [La cadena de audio de una cámara](#la-cadena-de-audio-de-una-cámara)
  - [El conector XLR y la línea balanceada](#el-conector-xlr-y-la-línea-balanceada)
- [Microfonía](#microfonía)
  - [Los micrófonos por su transductor](#los-micrófonos-por-su-transductor)
  - [Los patrones polares](#los-patrones-polares)
  - [El efecto de proximidad](#el-efecto-de-proximidad)
  - [Los micrófonos por su forma y su uso](#los-micrófonos-por-su-forma-y-su-uso)
  - [Los soportes, el viento y el roce](#los-soportes-el-viento-y-el-roce)
  - [Los inalámbricos y los grupos de frecuencia](#los-inalámbricos-y-los-grupos-de-frecuencia)
  - [Dos inalámbricos en la misma cámara](#dos-inalámbricos-en-la-misma-cámara)
- [Niveles](#niveles)
  - [El margen dinámico](#el-margen-dinámico)
  - [El nivel de alineación: −18 dBFS](#el-nivel-de-alineación-18-dbfs)
  - [Por qué 18 dB de reserva](#por-qué-18-db-de-reserva)
  - [La sonoridad: EBU R 128](#la-sonoridad-ebu-r-128)
  - [Qué hace la sonoridad en la cámara](#qué-hace-la-sonoridad-en-la-cámara)
  - [Los mandos de nivel de la cámara](#los-mandos-de-nivel-de-la-cámara)
  - [Ajustar el nivel en la práctica](#ajustar-el-nivel-en-la-práctica)
- [Sincronía](#sincronía)
  - [Sonido en la cámara o sonido aparte](#sonido-en-la-cámara-o-sonido-aparte)
  - [La cámara fotográfica y el sonido aparte](#la-cámara-fotográfica-y-el-sonido-aparte)
  - [La claqueta](#la-claqueta)
  - [El código de tiempo](#el-código-de-tiempo)
  - [Lo que rompe la sincronía](#lo-que-rompe-la-sincronía)
- [Ambiente](#ambiente)
  - [El ambiente se graba siempre](#el-ambiente-se-graba-siempre)
  - [El canal 2 y el micrófono de cámara](#el-canal-2-y-el-micrófono-de-cámara)
  - [Cuando el sonido es la noticia](#cuando-el-sonido-es-la-noticia)
  - [Los ambientes ruidosos](#los-ambientes-ruidosos)
  - [El ambiente no se falsea](#el-ambiente-no-se-falsea)
  - [La continuidad del sonido](#la-continuidad-del-sonido)
- [Criterios básicos](#criterios-básicos)
  - [El reparto de canales](#el-reparto-de-canales)
  - [Antes de grabar](#antes-de-grabar)
  - [Mientras se graba](#mientras-se-graba)
  - [Después de grabar](#después-de-grabar)
  - [Los errores típicos](#los-errores-típicos)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Captación de sonido asociada a cámara

### Por qué el sonido es del operador de cámara

En una cobertura de informativos no hay técnico de sonido. El equipo es una cámara y, con suerte,
un redactor. El operador de cámara elige el micrófono, lo coloca, ajusta el nivel y comprueba la
señal, y lo hace mientras encuadra y enfoca. El Libro de estilo de Canal Sur, al describir la
entrevista fuera de plató (3.17.1, p. 59), pide que el equipo lleve **«los elementos que sean
necesarios para un resultado técnico óptimo y para solventar imprevistos: auriculares, antorcha,
equipo básico de iluminación, ﬁltros, micrófonos...»**.

Las tres consecuencias que eso tiene (oficio):

1. Hay que decidir rápido y sin poder rehacer. Una entrevista no se repite, así que el micrófono
   correcto se elige a la primera.
2. Hay que conocer los inalámbricos de memoria. Emparejar un emisor y un receptor en la puerta de
   un juzgado no es el momento de leer el manual.
3. Hay que saber cuándo la cámara no basta. Algunas cámaras no admiten dos receptores, y algunas
   máquinas no tienen entrada de audio profesional: entonces la solución es grabar el sonido aparte.

### El sonido y sus magnitudes

El sonido es una onda de presión que viaja por un medio elástico, y se describe con cuatro
magnitudes:

| Magnitud | Qué es | Unidad |
|---|---|---|
| Frecuencia | El número de ciclos por segundo | Hercio (Hz) |
| Periodo | El tiempo que dura un ciclo: la inversa de la frecuencia | Segundo |
| Longitud de onda | La distancia que recorre la onda en un ciclo | Metro |
| Amplitud | La magnitud de la variación de presión | Pascal, o decibelio en escala relativa |

El número de ciclos por segundo es la frecuencia, y su unidad es el hercio. Las dos confusiones
habituales son el periodo —que es el tiempo de un ciclo, no el número de ciclos— y el decibelio,
que mide amplitud, no frecuencia.

Las tres cualidades perceptivas que se derivan:

| Cualidad | De qué depende |
|---|---|
| Tono (grave o agudo) | De la frecuencia |
| Intensidad (fuerte o débil) | De la amplitud |
| Timbre | De la composición armónica: es lo que distingue dos instrumentos que dan la misma nota |

### El margen de frecuencias audibles

El margen de frecuencias audible por un ser humano va de 20 Hz a 20.000 Hz. Es un valor
convencional para un oído joven y sano.

| Zona | Margen | Qué hay ahí |
|---|---|---|
| Infrasonidos | Por debajo de 20 Hz | No se oyen; se sienten |
| Graves | 20 – 250 Hz | El cuerpo del sonido |
| Medios | 250 – 4.000 Hz | La inteligibilidad de la voz |
| Agudos | 4.000 – 20.000 Hz | El brillo y el detalle |
| Ultrasonidos | Por encima de 20.000 Hz | No se oyen |

Los límites entre graves, medios y agudos son de oficio, no de norma. Dos avisos de lectura: una
opción que dé «de 20 µm a 20.000 µm» tiene las cifras correctas y la unidad falsa —el micrómetro es
una longitud, no una frecuencia—; y «de 20 Hz a 20.000 Hz» es un margen de frecuencias, no un
margen dinámico, que se mide en decibelios (se ve en «Niveles»). El margen se estrecha con la edad,
y siempre por arriba.

Los equipos se especifican con ese mismo margen: la Sony PXW-Z200, videocámara cuya guía de ayuda es de 2024 y que
se usa en este tema como ejemplo de fabricante, declara para sus entradas XLR una respuesta en
frecuencia de «**20 Hz to 20 kHz (±3 dB or less)**» (p. 337).

### Los transductores

Un transductor es un dispositivo que convierte una forma de energía en otra, y en una cadena de
sonido hay dos, uno en cada extremo:

| Transductor | De qué a qué | Qué es |
|---|---|---|
| Acústico-mecánico-eléctrico | De presión sonora a corriente | El micrófono |
| Eléctrico-mecánico-acústico | De corriente a presión sonora | El altavoz |

El orden de los tres adjetivos dice el camino de la energía: la primera palabra dice qué entra.
«Eléctrico-mecánico-acústico» empieza por lo eléctrico, así que entra corriente y sale sonido: es
un altavoz. El micrófono es la cadena leída al revés.

Los aparatos de la misma cadena que no transducen: el amplificador sube el nivel de una señal
eléctrica y la deja eléctrica; el ecualizador cambia su reparto por frecuencias; la antena
transduce, pero entre corriente y onda electromagnética, no acústica.

### La cadena de audio de una cámara

Qué cámaras usa CSRTV no consta en un documento publicado. Como ejemplo de la sección de audio de una
videocámara de 2024, la Sony PXW-Z200 declara:

| Elemento | Lo que dice el fabricante |
|---|---|
| Entradas profesionales | «**INPUT 1/2: XLR type, 3-pin, female**», «**LINE / MIC / MIC+48V switchable**» (p. 338) |
| Entrada de consumo | «**INPUT3 connector: Stereo mini jack, plug-in power compatible**» (p. 338) |
| Micrófono interno | «**Omnidirectional stereo electret condenser microphone**» (p. 338), en el asa |
| Formato de grabación | «**LPCM 24-bit, 48 kHz, 4-channel**» (p. 336) |
| Escucha | «**Connecting a set of headphones to the headphone jack enables you to monitor the audio being recorded.**» (p. 99); el canal que se escucha se elige con ***[Monitor CH]*** |

La cadena es siempre la misma (oficio): micrófono, cable o enlace inalámbrico, entrada de la
cámara (con su preamplificador y su conmutador de nivel), control de nivel, conversor analógico
digital, grabación en tarjeta y, en paralelo, escucha por auriculares y lectura en el medidor de la
pantalla. La calidad la limita el eslabón más débil. El conector analógico XLR tiene su propia norma
de la AES, la AES14 (*analog XLR pin-out*), que el tema no desarrolla.

### El conector XLR y la línea balanceada

Por qué el micrófono profesional va por XLR, en línea balanceada, lo explica el fabricante
de micrófonos DPA Microphones en su material de formación. Una línea balanceada (o simétrica) es
**«a transmission line consisting of two conductors of the same type and equal impedance to ground
and other circuits. The balanced impedances to ground minimizes interference pickup.»** En el XLR de
tres polos: **«pin 1 is for the shielding of the cable and should never carry the signal. Pins 2 and
3 carry the signal.»**

| Conexión | Qué pasa con el ruido |
|---|---|
| No balanceada | **«In the unbalanced connection the cable shield is a part of the circuit. Unfortunately this does not provide sufficient isolation to electromagnetic noise present in the surroundings.»** |
| Balanceada | **«When the well balanced cable is running through an electromagnetic field the induced voltage has the same polarity and magnitude on both leads. As the input will only accept a signal if it is oppositely phased on pin 2 and pin 3, the noise from the electromagnetic field is rejected.»** |

Dicho de otro modo: la señal viaja en oposición por los dos conductores y el ruido que se cuela en
el cable llega igual a los dos; la entrada se queda con la diferencia y el ruido, que es común,
desaparece. DPA lo llama **«common mode rejection»**, y la medida de cuánto se suprime es la razón de
rechazo en modo común (CMRR): **«Common Mode Rejection Ratio (CMRR) expresses the suppression of
induced EMI noise on the terminals of a device. This suppression is possible only if you use
balanced lines.»** Para que funcione, **«the impedance measured from pin 2 to ground and from pin 3
to ground is exactly the same»**, en el emisor, en el receptor y en el cable. Y enlaza con la
alimentación fantasma: si las dos patas no están equilibradas, **«the line is not balanced. And with
reference to microphones: Phantom power cannot be supplied.»**

Las consecuencias para la cámara: **«the unbalanced cabling should be kept as short as possible.
The main analog audio cabling should always be balanced.»** Una tirada larga de cable (el micrófono
de una mesa, una pértiga lejos de la cámara) va a una entrada XLR, no al minijack de consumo (oficio); y el
cable se aparta de lo que induce ruido: **«power transformers, along lighting cables, power cables,
speaker cables»** (DPA).

## Microfonía

### Los micrófonos por su transductor

| Tipo | Cómo funciona | ¿Alimentación? |
|---|---|---|
| Dinámico o de bobina móvil | Una bobina unida a la membrana se mueve en un campo magnético | No: genera su propia corriente |
| De cinta | Una lámina metálica muy fina en un campo magnético | No, salvo los activos |
| De condensador o electrostático | Membrana y placa fija forman un condensador de capacidad variable | Sí: fantasma (*phantom*) de 48 V, o pila |
| Electret | Condensador con carga permanente | Sí, poca |

El conmutador de entrada de la cámara tiene que casar con el micrófono. En la Sony PXW-Z200 las
entradas XLR tienen tres posiciones, ***LINE***, ***MIC*** y ***MIC+48V***, y el manual dice qué
va en cada una (en la descripción de las partes de la cámara, y otra vez en p. 136):

- «**LINE: External audio device (e.g. mixer)**»: un mezclador, la salida de la mesa de una rueda
  de prensa o el receptor de un inalámbrico con salida de línea.
- «**MIC: Dynamic microphone, battery-operated microphone**»: el dinámico y el condensador que se
  alimenta con su propia pila.
- «**MIC+48V: +48 V phantom power microphone**»: el condensador que toma la alimentación fantasma de
  la cámara por el mismo cable XLR.

Y avisa: «**Selecting MIC+48V and connecting a microphone that is not compatible with a +48V source
may damage the connected device. Check the setting before connecting the device.**» (p. 136). Es
decir, se comprueba el conmutador antes de enchufar. Y para las entradas vacías: «**If noise is a
concern on connectors with no device connected, set the corresponding INPUT 1/INPUT 2
(LINE/MIC/MIC+48V) switches to LINE.**» (p. 136).

La diferencia entre MIC y LINE es de nivel: un micrófono da una señal muy débil que la cámara tiene
que amplificar mucho; una fuente de línea llega ya amplificada. Una fuente de línea metida en
posición MIC satura; un micrófono en posición LINE se graba casi en silencio (oficio). La Z200
declara para la entrada de micrófono una referencia de «**−30 dBu to −80 dBu**» (p. 338) y deja
elegirla en el menú ***[INPUT1 MIC Reference]*** entre −80 y −30 dB, con −50 dB de fábrica
(p. 260); para la línea, ***[Line Input Reference]*** ofrece «**+4dB / 0dB / −3dB / [EBUL]**»,
con +4 dB de fábrica (p. 260).

### Los patrones polares

El patrón polar de un micrófono dice de qué direcciones recoge, y elegirlo bien es la mitad del
sonido de un reportaje.

| Patrón | De dónde recoge | Cuándo se usa en ENG |
|---|---|---|
| Omnidireccional | De todas las direcciones por igual | Micrófono de corbata, ambientes |
| Cardioide | Sobre todo de delante, algo de los lados | Micrófono de mano del reportero; voz |
| Supercardioide | Lóbulo frontal más estrecho, con un pequeño lóbulo trasero | Directo con ruido |
| Hipercardioide | Lóbulo frontal muy estrecho, con lóbulo trasero apreciable | Sonidos lejanos, entorno ruidoso |
| Cañón (*shotgun*) | Un cono muy estrecho de delante | Pértiga, largo alcance, micrófono sobre la cámara |
| Bidireccional o de ocho | De delante y de detrás, no de los lados | Entrevista cara a cara con un solo micrófono |

Los micrófonos con igual sensibilidad en cualquier dirección son los omnidireccionales: la palabra
que los define es «igual», porque la sensibilidad no cambia con el ángulo. Los que recogen por
delante y por detrás del diafragma y no por los laterales son los bidireccionales; su forma polar,
dos lóbulos opuestos, les da el nombre de «ocho». El micrófono interno de la Sony PXW-Z200 es un
«**Omnidirectional stereo electret condenser microphone**» (p. 338): recoge de todas partes, y por
eso sirve para el ambiente y no para aislar una voz.

El hipercardioide se usa principalmente para captar sonidos lejanos. La razón: cuanto más estrecho
es el lóbulo frontal, más rechaza el micrófono todo lo que no está delante, y más se parece la
relación entre el sonido buscado y el ambiente a la que habría si el micrófono estuviese cerca.
Estrechar el patrón no acerca el sonido: aleja el ruido, y el efecto que se percibe es el mismo. Si
el sonido principal está debilitado por el ambiente, se monta un micrófono direccional.

Lo que no hace un patrón estrecho:

| Situación | Patrón que conviene |
|---|---|
| Fuentes dispersas y múltiples | Omnidireccional |
| El ambiente de todo el entorno, lo más fiel posible | Omnidireccional, o una pareja estereofónica |
| Varias fuentes cercanas en movimiento | Cardioide o incluso omnidireccional |

Un patrón estrecho castiga el movimiento. Un hipercardioide mal apuntado suena peor que un
cardioide bien puesto, porque al salirse del lóbulo el sonido cae de golpe y además cambia de
color. Cuanto más direccional es el micrófono, más importa apuntarlo (oficio).

### El efecto de proximidad

Un micrófono direccional cambia de sonido con la distancia. DPA lo define así: **«Proximity is when
a microphone produces more bass by getting closer to the sound source (a point - or line source).»**
Y en su diccionario: **«An inherent characteristic of pressure gradient microphones, resulting in a
boost in the low-frequency response when the microphone is brought closer to a source.»** En la voz:
**«The singer's voice gets more bass when the microphone moves closer to the mouth. As the microphone
moves away, the sound gets thinner.»**

Qué micrófonos lo tienen y cuándo:

| Condición | Lo que dice DPA |
|---|---|
| Patrón | **«Proximity only exists with gradient-types of microphones – wide cardioid, open cardioid, cardioid, super-cardioid, hyper-cardioid, figure of eight – and everything in between. Thus, the closer the directionality pattern comes to a figure of eight, the more proximity is exhibited.»** |
| Omnidireccionales | **«pressure microphones (omnidirectional microphones) do not exhibit proximity»**, porque el sonido sólo llega a la cara delantera de la membrana |
| Distancia | **«A gradient microphone close to a point source (<1 m) exhibits proximity»**; a más de un metro, **«practically no proximity effect exists»** |
| Ángulo | **«the proximity effect is strongest on-axis. If you turn the microphone, the proximity effect is reduced.»** En un cardioide desaparece a **«exactly 90 degrees»** |

La causa: en un micrófono de gradiente el sonido llega a la membrana por delante y por detrás, y la
membrana se mueve por la diferencia de presión entre las dos caras; muy cerca de la fuente, la cara
trasera queda proporcionalmente más lejos que la delantera, y esa diferencia añadida pesa en los
graves, donde la diferencia principal es pequeña (DPA). Algunos micrófonos de voz están diseñados
para sonar planos precisamente de cerca: por eso DPA pide que la ficha diga a qué distancia la
respuesta es plana.

En el trabajo de cámara (oficio): el micrófono de mano cardioide del reportero, pegado a la boca,
engorda la voz, y si se aleja y se acerca mientras habla la voz cambia de color además de nivel; el
corbata, si es omnidireccional, no tiene efecto de proximidad (DPA); y los graves de más se corrigen en el mismo
sitio, con la distancia, antes que en montaje.

### Los micrófonos por su forma y su uso

| Nombre | Qué es |
|---|---|
| Lavalier o de corbata | Miniatura, se prende en la ropa. Casi siempre omnidireccional |
| De mano | El del reportero |
| De cañón | El de la pértiga o el que va sobre la cámara |
| De diadema | Para presentadores que se mueven |
| De solapa inalámbrico | Lavalier con emisor de petaca |

Electret, condensador y lavalier son tipos de micrófono (el primero y el segundo por su transductor,
el tercero por su forma).

El Libro de estilo de Canal Sur fija dónde va cada uno en la información:

- Entrevista fuera de plató (3.17.1, p. 59): **«cámara apoyada sobre trípode y micrófono de corbata
  para quien nos habla»**.
- Y el micrófono de mano no se cede al entrevistado (3.17.1.3, p. 60): el periodista no se colocará
  al lado del personaje, **«a quien no permitiremos que sujete el micrófono de mano y a quien, bajo
  ningún concepto, se lo cederemos para que aparezca asiéndolo en pantalla como única
  referencia»**.
- Directo (8.3.2, p. 117): **«con el micrófono vertical, apoyando levemente sobre el esternón la
  mano que lo sujeta, sin que oculte el rostro y de modo relajado»**; y **«En caso de que hagamos el
  directo desde un lugar especialmente habilitado para ello, generalmente en interiores, el
  micrófono puede ser de corbata»**.

### Los soportes, el viento y el roce

| Soporte o accesorio | Para qué |
|---|---|
| Pie de suelo con base o trípode | Micrófono de pie, en plató o en directo musical |
| Pie de mesa | Tertulias y ruedas de prensa |
| Pértiga o jirafa | El cañón sobre la escena |
| Suspensión elástica (*shock mount*) | Aísla el micrófono de las vibraciones del soporte |
| Paravientos, peluca y cortavientos | Reducen el ruido del aire |
| Pinza | Sujeta el micrófono al pie, o el de corbata a la ropa |

El micrófono nunca va rígido sobre el soporte: el golpe en el pie llega al diafragma por el metal,
y el de cámara transmite los ruidos de manejo de la propia cámara (zoom, botones, manos). En
exterior el viento es el primer enemigo, y se combate primero con el paravientos o la peluca y
después con el filtro. La Z200 trae un filtro por canal, ***[CH1 Wind Filter]***: «**Enables/disables
the wind reduction filter for CH1.**», desactivado de fábrica (p. 260).

El micrófono de corbata tiene su propio ruido: el roce con la ropa. El Libro de estilo lo recoge al
tratar el vestuario de quien sale en pantalla (8.6.1, p. 122): **«Telas brillantes, satenes y sedas producen
brillo y reﬂejan color. El roce de estos tejidos produce además ruidos que los micrófonos
registran.»** La colocación que lo evita es de oficio: la cápsula a un palmo de la boca, en el
centro del pecho, sin que la roce la solapa, el pelo, un collar o una corbata, y con un pequeño bucle
del cable sujeto para que el tirón no llegue a la cápsula.

### Los inalámbricos y los grupos de frecuencia

Un sistema inalámbrico son dos aparatos: un emisor, que va con el micrófono (la petaca del corbata
o el propio micrófono de mano), y un receptor, que va en la cámara. Los dos tienen que estar en la
misma frecuencia, y ahí empieza la dificultad.

| Nivel | Qué es |
|---|---|
| Banda | El margen de radiofrecuencia en el que trabaja el equipo |
| Grupo | Un conjunto de canales elegidos por el fabricante para que no se interfieran entre sí |
| Canal | Una frecuencia concreta dentro del grupo |

El grupo es la clave: dos emisores en frecuencias cualesquiera pueden interferirse aunque no
coincidan, porque sus armónicos y sus productos de intermodulación caen encima del otro. Un grupo es
una lista de frecuencias que el fabricante ha calculado para que eso no ocurra.

Por eso, en un inalámbrico doble, los dos emisores van en el mismo grupo. Es la respuesta
contraintuitiva, porque el sentido común dice «separarlos todo lo posible». Lo correcto es lo
contrario: dentro de un mismo grupo, las frecuencias están calculadas para convivir; en grupos
distintos, o en el grupo más bajo y el más alto, no hay ninguna garantía de que no se estorben. Y
decir que «el grupo no afecta a la transmisión» niega la razón de ser del grupo.

Lo que el cámara hace con un inalámbrico antes de grabar (oficio): comprobar la pila o la batería
de emisor y receptor, poner los dos en la misma banda, grupo y canal (o emparejarlos si el equipo lo
hace de forma automática), buscar un canal libre si el receptor tiene exploración, ajustar la
sensibilidad del emisor a la voz de quien lo lleva y escuchar con auriculares. Y llevar siempre un
micrófono de cable de reserva.

### Dos inalámbricos en la misma cámara

Sí es posible conectar dos micrófonos de corbata inalámbricos a la vez a una cámara profesional,
ajustando las bandas y las frecuencias de los dos en el mismo grupo para que cada uno coincida con
su receptor. Es la aplicación práctica del epígrafe anterior.

Cómo se hace en la máquina: la cámara lleva una ranura de receptor con dos canales, o dos
receptores, y cada emisor se empareja con su canal. Los dos canales van en el mismo grupo, y cada
uno entra por una pista de audio distinta.

| Idea falsa | Por qué no |
|---|---|
| Hace falta un mezclador externo | No: la cámara tiene dos entradas y dos pistas. El mezclador es una opción, no un requisito |
| La cámara sólo admite un receptor | Falso en una cámara profesional; cierto en algunas, y entonces se graba aparte |
| Se conectan los dos micrófonos al mismo receptor | Un receptor sintoniza una frecuencia: dos emisores en el mismo receptor se pisan |

Dos pistas separadas, una por micrófono, es siempre mejor que las dos mezcladas en la cámara: un
pico de uno no arrastra al otro, y el montador puede corregir cada voz por separado. Mezclar en
cámara es una decisión que no se puede deshacer (oficio).

La Sony PXW-Z200 graba cuatro canales, y con un adaptador puede tomar cuatro fuentes XLR: «**You can
connect up to four channels of XLR audio devices to the unit at the same time by using an XLR-K2M
XLR adaptor (not supplied) or XLR-K3M XLR adaptor (not supplied).**» (p. 139). De fábrica los cuatro
canales toman el micrófono interno (***[CH1 Input Select]*** a ***[CH4 Input Select]***, valor
«**[Internal MIC]**», p. 260): hay que cambiar la fuente de cada canal antes de grabar.

## Niveles

### El margen dinámico

El margen dinámico de un equipo es la diferencia, en decibelios, entre el nivel de señal máximo y el
nivel de ruido del equipo.

| Extremo | Qué es |
|---|---|
| El techo | El nivel máximo que el equipo admite antes de distorsionar |
| El suelo | El ruido propio del equipo: el siseo que hay incluso sin señal de entrada |

El margen dinámico es la distancia entre los dos. Por debajo del suelo la señal se pierde en el
ruido; por encima del techo se distorsiona. Lo utilizable es lo que hay en medio.

Las definiciones falsas cambian uno de los dos extremos: «entre el nivel de señal mínimo y el
ruido» (el mínimo y el ruido son prácticamente lo mismo); «entre el umbral de audición máximo, o
mínimo, y el ruido del equipo» (mezclan una magnitud del oído con una del equipo). El margen
dinámico de un equipo se mide con las dos magnitudes de ese equipo. El margen dinámico del oído es
otra cosa —la diferencia entre el sonido más débil que se percibe y el que produce dolor— y es del
orden de 120 dB.

El cálculo que va con el margen: cada bit de cuantificación aporta unos 6 dB de margen dinámico
teórico (20 × log 2 ≈ 6,02 dB), así que 16 bits dan unos 96 dB y 24 bits unos 144 dB. Por eso el
audio de producción se graba a 24 bits. La EBU R 68 opina que las grabaciones deben hacerse **«with linear coding using no
pre-emphasis and with a resolution of at least 16 bits in accordance with ITU-R Recommendation
BS.646»**, y advierte en su nota 1 que **«16-bit recordings may not meet the requirements of some
organizations regarding the signal-to-noise in production equipment, depending on the performance of the A/D
and D/A converters»**.

El margen real de un equipo lo fija su electrónica analógica, no el número de bits. La Sony
PXW-Z200 graba a 24 bits y declara (p. 337) un margen dinámico de «**XLR input MIC mode: 80 dB
(typical)**» y «**XLR input LINE mode: 90 dB (typical)**»: bastante menos que los 144 dB teóricos,
y peor en micrófono, porque el preamplificador añade su ruido.

### El nivel de alineación: −18 dBFS

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

Es decir: el tono de referencia es una senoide de 1 kHz a −18 dBFS. Es el tono que la cámara graba
con las barras de color, y el que se usa para alinear la cadena de audio entre equipos. Ojo: la
Z200 viene de fábrica con el tono a −20 dB (se ve en «Los mandos de nivel de la cámara»), un
valor que no es el de la EBU R 68 y cuyo origen no consta en las fuentes leídas.

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

### La sonoridad: EBU R 128

Durante décadas los programas se ajustaron por su pico. La EBU R 128 parte de que **«peak
normalisation of audio signals has led to considerable loudness differences between programmes and
between broadcast channels»**, y de que esas diferencias **«are the cause of the most
viewer/listener complaints»**. Lo que el espectador percibe no es el pico, sino la sonoridad: lo
fuerte que suena el programa en conjunto. Y el medidor clásico, usado para leer picos, no la mide: el **«QPPM
(Quasi-Peak Programme Meter) specified in EBU Tech 3205-E [1] does not reflect the loudness of an
audio signal»**.

Lo que fija la R 128 (versión 5, noviembre de 2023):

| Punto | Lo que dice |
|---|---|
| h) Nivel objetivo | **«the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS. Where attaining the Target Level is not achievable practically (for example, live programmes), a tolerance of ±1.0 LU is permitted.»** |
| i) Tolerancia de medida | **«a tolerance of ±0.2 LU is allowed in order to take account of measurement errors»** |
| m) Pico verdadero | **«the True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during production (linear audio)»**; tolerancia de medida de **«±0.3 dB (for signals with a bandwidth limited to 20 kHz)»** |
| k) Medidor | Conforme a la UIT-R BS.1770 y a la EBU Tech 3341 |
| n) Margen de sonoridad (LRA) | Según la EBU Tech 3342; nota 2: **«For programmes shorter than 1 minute, the use of the measure Loudness Range is not recommended»** |

Las unidades: la BS.1770 introduce **«the measures LU (Loudness Unit) and LUFS (Loudness Units,
referenced to Full Scale)»**; y **«‘LUFS’ is equivalent to ‘LKFS’ (which is used in ITU-R
BS.1770)»**. Un LU es un decibelio de sonoridad: **«1 LU is equivalent to 1 dB»** (EBU Tech 3341,
§ 2.4).

El medidor en «modo EBU» (Tech 3341) da tres lecturas, con tres ventanas de tiempo:

| Lectura | Abreviatura | Ventana |
|---|---|---|
| Momentánea (*Momentary*) | M | **«a sliding rectangular time window of length 0.4 s. The measurement is not gated.»** |
| Corto plazo (*Short-term*) | S | **«a sliding rectangular time window of length 3 s.»** |
| Integrada (*Integrated*) | I | **«uses gating as described in ITU-R BS.1770.»**: es la sonoridad del programa entero |

Para un tribunal, el dato que más se pregunta es el nivel objetivo: −23 LUFS, con ±1 LU en directo.
La ficha de revisiones de la propia R 128 menciona una tolerancia de ±0,5 LU introducida en 2014;
el articulado vigente de 2023 no la recoge, y manda el articulado.

### Qué hace la sonoridad en la cámara

La R 128 normaliza el programa terminado: se aplica en posproducción y en emisión. Ninguna norma
EBU leída fija «el nivel de la voz en la cámara», y este tema no da una cifra para ello. Lo que sí
llega a la cámara son tres cosas:

1. La alineación sigue siendo −18 dBFS con tono de 1 kHz, y la EBU recomienda alinear con un
   medidor de pico, no con uno de sonoridad. Dice la Tech 3343 (§ 8.1): **«The alignment level of
   −18 dBFS (1 kHz tone) will read as −18 LUFS on a loudness meter with the absolute scale (or +5 LU
   on the relative EBU mode scale), provided that the 1 kHz tone is present (in phase) on both the left
   and right channel of a stereo or surround sound signal.»** Por la ponderación en frecuencia del
   medidor de sonoridad, usarlo para alinear es una fuente de errores: **«The EBU therefore
   recommends using a peakmeter for alignment.»**
2. El pico verdadero no debe pasar de −1 dBTP en producción. Según la Tech 3343, **«It is only
   necessary to leave a headroom of 1 dB below 0 dBFS to still accommodate the potential
   under-read of about 0.5 dB (for a 4x oversampling true-peak meter; basic sample rate: 48
   kHz)»**; para dos sistemas de reducción de datos muy usados en Europa, MPEG-1 Layer 2 y Dolby AC-3, el límite
   recomendado es −2 dBTP.
3. Con sonoridad hay más sitio para los picos, y eso favorece el ambiente: **«The greater headroom
   will be a welcome bonus for crowd noise, for example, of sports programmes»** (Tech 3343). En
   deportes, la misma guía aconseja que la voz de los comentaristas quede algo por debajo del
   objetivo, **«(for example, at −24 LUFS), so that unexpected crowd noise has more room to move»**
   (§ 3.5.1). No hay que aplastar ni saturar el ambiente en la captación.

En la cámara el operador trabaja con el medidor de pico de la pantalla, referido a la alineación de
−18 dBFS y dejando margen bajo 0 dBFS (oficio).

### Los mandos de nivel de la cámara

Todas las cámaras profesionales tienen los mismos mandos básicos, con nombres distintos. En la Sony
PXW-Z200:

| Mando | Lo que dice el fabricante | Para qué |
|---|---|---|
| Conmutador ***AUTO/MAN*** | «**Switches the CH-1/CH-2 audio recording level between auto mode and manual mode.**» (p. 16) | Elegir nivel automático o manual |
| Ruedas ***AUDIO LEVEL*** | En manual: «**Set the CH1/CH2 (AUTO/MAN) switches for the channels to adjust to the MAN position.**» «**During shooting or standby, turn the AUDIO LEVEL dials (CH1)/(CH2) of the corresponding channels to adjust the audio level.**» (p. 138) | Ajustar el nivel a mano, incluso grabando |
| ***[Limiter Mode]*** | «**[Off] / −6dB / −9dB / −12dB / −15dB / −17dB**», de fábrica ***[Off]***: «**Selects the limiter characteristic for large input signals when adjusting the audio input level manually.**» (p. 261) | Proteger de un golpe de nivel en manual |
| ***[CH1&2 AGC Mode]*** | «**[Mono] / [Stereo]**», de fábrica ***[Stereo]***: «**When [Stereo] is selected, auto gain control is linked between channels.**» (p. 261) | Enlazar o no el automático de dos canales |
| ***[Reference Level]*** | «**−20dB / −18dB / −16dB / −12dB / [EBUL]**», de fábrica −20 dB: «**Selects the recording level of the 1 kHz reference tone signal.**» (p. 260) | Nivel del tono de referencia |
| ***[1kHz Tone on Color Bars]*** | «**Turns the 1 kHz reference tone signal on/off when displaying color bars.**», de fábrica ***[Off]***; y la nota: «**When set to [On], the 1 kHz reference tone signal is output on CH3/CH4, even if [CH3 Input Select]/[CH4 Input Select] are set to [Off].**» (p. 261) | Grabar tono con las barras; con ***[On]***, los canales 3 y 4 llevan el tono aunque su entrada esté apagada |
| ***[CH1 Wind Filter]*** | Filtro de viento por canal, de fábrica ***[Off]*** (p. 260) | Reducir el ruido de viento |

Tres consecuencias:

- El valor de fábrica del tono de referencia es −20 dB. Para trabajar según la EBU R 68 hay que
  cambiarlo a −18 dB. Qué es la opción ***[EBUL]*** no lo explica el manual.
- El automático (AGC) sube el nivel cuando nadie habla y lo baja cuando alguien habla fuerte: en
  una pausa el ambiente «respira» y sube el ruido de fondo (oficio). Sirve para lo imprevisto, en
  un suceso en el que no hay tiempo; en una entrevista o una declaración se trabaja en manual. En
  estéreo enlazado, un golpe en un canal baja también el otro, por eso dos micrófonos
  independientes no se enlazan.
- El limitador sólo actúa en manual y sólo sobre los picos grandes: es una red de seguridad, no un
  sustituto del ajuste.

### Ajustar el nivel en la práctica

No hay norma que fije el procedimiento. Es oficio, y así se da:

1. Conmutador de entrada según la fuente (LINE, MIC o MIC+48V), y fuente de cada canal elegida en
   el menú.
2. Canal en manual.
3. Prueba de voz con la persona que va a hablar, con su voz real y a su distancia real: no vale
   «probando, probando» en voz baja.
4. Nivel en el medidor de pico: la voz por encima de la referencia y los picos lejos de 0 dBFS. Lo
   que se recorta no se recupera; lo que queda algo bajo se puede subir en montaje, a costa de
   subir también el ruido.
5. Limitador puesto, como red de seguridad.
6. Escucha continua con auriculares: el medidor dice cuánto, el oído dice qué (roces, viento,
   zumbidos, un inalámbrico que corta).
7. Revisión de la grabación en el sitio.

El Libro de estilo de Canal Sur recoge dos de esos pasos. Al tratar el sonido (5.4, p. 82):
**«El nivel y la calidad del sonido también deben vigilarse con rigor para evitar defectos y saltos
de volumen que deban ser solucionados en la fase de montaje.»** Y justo antes (p. 82): **«Otra
norma elemental de prudencia es revisar la grabación en el mismo lugar de la misma para comprobar
que es correcta desde la perspectiva de la imagen y del sonido.»**

## Sincronía

### Sonido en la cámara o sonido aparte

Hay dos maneras de grabar el sonido de una imagen (oficio):

| Sistema | Cómo | Sincronía |
|---|---|---|
| Sistema único | El sonido entra en la cámara y se graba en el mismo fichero que la imagen | Viene hecha: imagen y sonido comparten reloj y código de tiempo |
| Doble sistema | El sonido se graba en un grabador aparte | Hay que hacerla: con una marca (claqueta) o con un código de tiempo común |

En ENG se trabaja casi siempre en sistema único. El doble sistema aparece cuando la cámara no puede
con el sonido, cuando hay un técnico de sonido con su grabador, o cuando se toma el sonido de una
mesa sin cable hasta la cámara.

### La cámara fotográfica y el sonido aparte

Una cámara fotográfica usada para grabar vídeo (una DSLR o una sin espejo) tiene una limitación que
una cámara de vídeo profesional no tiene: su entrada de audio no es profesional. Lo habitual es una
entrada de clavija (*jack*) de 3,5 mm con nivel de micrófono de consumo, sin alimentación fantasma,
sin control de nivel fino y con un preamplificador ruidoso (oficio).

Para grabar un micrófono profesional de corbata inalámbrico con la máxima calidad técnica posible
en una cámara fotográfica, se conecta el receptor del micrófono a un grabador externo donde se
graba el sonido aparte, se graba una claqueta y se sincronizan los dos después, en
posproducción.

Por qué va aparte: la calidad del audio la limita el eslabón más débil de la cadena. Meter una señal
profesional por una entrada de consumo tira por la borda la calidad del micrófono: el
preamplificador de la cámara añade su ruido, y su conversor trabaja peor. La única forma de
conservar la calidad es no pasar por ahí.

Las soluciones que no sirven:

| Idea | Por qué no |
|---|---|
| Convertir el conector profesional a clavija de 6,35 mm (un cuarto de pulgada) | Ésa no es la entrada de una cámara fotográfica, que es de 3,5 mm, y sobre todo seguiría entrando por el preamplificador de la cámara |
| Conectar el receptor por XLR al cuerpo de cámara | Una cámara fotográfica no tiene entrada XLR: no hay dónde conectarlo |
| Grabar aparte y además unir el grabador a la cámara por XLR «para que se sincronicen» | Acierta lo de grabar aparte y se inventa una sincronización: un cable de audio no sincroniza nada. La sincronía de dos grabaciones separadas se hace con una marca o con código de tiempo |

### La claqueta

Si el sonido se graba en otra máquina, hay que poder sincronizarlo. Una claqueta —o, a falta de
ella, una palmada delante del objetivo— da un instante que se ve en la imagen y se oye en el sonido:
el cierre del palo. El montador alinea las dos grabaciones por ese instante. Sin marca de
sincronización, alinear dos grabaciones independientes es a ojo (oficio).

Cómo se da una claqueta (oficio): delante del objetivo, dentro del encuadre y enfocada; con las dos
grabaciones ya en marcha; con un golpe seco y cerrando del todo; y, si la toma empieza sin claqueta,
se da al final, invertida, para que el montador sepa que la marca va detrás. En cada toma con
grabador aparte se da una.

### El código de tiempo

El código de tiempo es una etiqueta de horas, minutos, segundos y cuadros que cada cuadro de imagen
lleva grabada, y que permite encontrar un plano y sincronizar grabaciones.

El Libro de estilo de Canal Sur lo trata como un acuerdo del equipo (5.3.3, p. 81): **«En cada
grabación el código de tiempo es un acuerdo básico entre periodista y cámara, especialmente cuando
van a estar físicamente separados durante la cobertura y cuando hay poco margen para la posterior
elaboración del correspondiente vídeo. En este caso puede usarse un código de tiempo real
previamente acotado, aunque también puede ser recomendable es el TC poniendo el marcador a 00:00:00
al principio de la cinta. Esta referencia es generalmente mejor, sobre todo cuando el material va a
ser usado por terceras personas.»** El texto es de 2004 y habla de cinta; la idea —acordar el código
antes de separarse— vale igual para la tarjeta.

Para sincronizar el sonido, el código de tiempo sirve si la cámara y el grabador llevan el mismo.
La Sony PXW-Z200 lo hace así (p. 298):

- **«You can synchronize the timecode of the unit with an external device.»** Se le da un código
  de referencia por el conector ***TC IN/OUT***: **«The timecode generator of the unit acquires lock
  with the reference timecode, and “EXT-LK” is displayed on the screen.»**
- **«Once about ten seconds have elapsed after the timecode locks, the external lock state is
  maintained even if the external reference timecode source is disconnected.»** Es decir: se
  enclava y después se puede desconectar el cable.
- No se graba nada más enclavar: **«do not start recording immediately. Wait for a few seconds until
  the timecode generator stabilizes before recording.»**
- La frecuencia tiene que coincidir: **«If the frequency of the reference timecode and the frame
  frequency on the unit are not the same, lock cannot be acquired»**.
- Y la sincronía se desvía: **«The timecode may shift by one frame per hour with respect to the
  reference timecode.»** Por eso, en una jornada larga, se vuelve a enclavar de vez en cuando
  (oficio).
- Al revés, para que otro equipo tome el código de la cámara, la cámara debe estar en un modo en que
  el código corre siempre: **«[Free Run] or [Clock]»**.

Los bits de usuario sirven para añadir un dato propio a cada clip: **«You can add an 8-digit
hexadecimal number to a clip as user bits.»** (p. 99). Qué se anota en ellos (la fecha, el número de
equipo) es costumbre de cada casa; no consta una regla de CSRTV.

### Lo que rompe la sincronía

- La cámara lenta: en la Z200, **«Audio is not recorded in Slow & Quick Motion mode.»** (p. 136); y
  empezar a grabar en ese modo suelta el enclavamiento del código de tiempo, igual que cambiar la
  frecuencia del sistema (p. 298). Hay que avisar a redacción: ese plano no tendrá sonido.
- Una frecuencia de cuadro distinta entre cámara y grabador (no enclavan).
- El retardo del receptor inalámbrico digital o de la red en un directo: es pequeño en un
  inalámbrico y grande en un enlace por red móvil, y se compensa en el control, no en la cámara
  (oficio; el directo es materia del tema 13).
- Un plano sin claqueta ni código común en doble sistema.

## Ambiente

### El ambiente se graba siempre

El sonido ambiente es el sonido del lugar: la calle, el viento, el público, las máquinas, el
silencio de una sala. Da verdad a la imagen, permite montar sin que se note el corte y sirve de
colchón bajo la voz del locutor. La regla del Libro de estilo de Canal Sur (5.4, p. 82) no admite
excepciones: **«El sonido ambiente tiene que ser registrado siempre y en cualquier circunstancia,
incluso aquellas en las que su ausencia sea casi absoluta (una exposición, el interior de un
museo).»**

El «incluso» es la clave: también el casi silencio es ambiente, y en montaje hace falta para tapar
los cortes. Un plano sin ambiente suena a vacío.

### El canal 2 y el micrófono de cámara

El mismo epígrafe fija por dónde va (5.4, p. 82): **«El canal 2 recoge el sonido ambiente, captado a
través del micrófono de la cámara.»** El micrófono de la cámara es el que va montado en ella: en la
Sony PXW-Z200 el interno es omnidireccional estéreo; en las cámaras de hombro suele ir un cañón en
el soporte del asa (oficio). Un omnidireccional recoge el entorno entero; un cañón en la cámara
recoge sobre todo lo que tiene delante, que es lo que se está grabando.

Mientras se graba ambiente, el cámara no habla ni comenta: todo lo que se dice cerca de la cámara
queda grabado en el canal 2 (oficio).

### Cuando el sonido es la noticia

Hay informaciones en las que el sonido manda. El Libro de estilo (5.4, p. 82): **«Cuando el sonido
sea la base estética y/o noticiosa de una información, caso de una actuación musical, o cuando forme
parte fundamental del discurso narrativo, caso de los lemas y gritos de una protesta, hay que
realizar, si es posible, una grabación especíﬁca, continuada y suﬁciente del sonido —incluso por
los canales 1 y 2 simultáneamente, en previsión de incluirlo en emisión como vídeo total, o
fórmulas similares— e independiente de la imagen que se capte simultáneamente, que tendrá un valor
subalterno en el montaje ﬁnal.»**

Tres condiciones: específica (pensada para el sonido), continuada (sin cortar) y suficiente (lo
bastante larga para montar). Y el orden se invierte: la imagen se subordina al sonido.

Si el sonido importa tanto como la imagen, además, se toma de la mesa (5.4, p. 82): **«Si las
circunstancias lo permitan, el canal 1 se tomará de mesa de sonido sobre todo si éste es tan
importante como la imagen: actuación musical, discurso político, ensayo general...»**. La salida de
una mesa es de línea: la entrada de la cámara va en ***LINE***.

### Los ambientes ruidosos

El ruido de ambiente es el enemigo de la declaración. El Libro de estilo (5.4, p. 82): **«Los
ambientes demasiado ruidosos han de evitarse, sobre todo para la grabación de declaraciones, salvo
que el propio sonido forme parte de la información, como se indica en el párrafo anterior.»**

Cuando no se puede elegir sitio, se elige micrófono (oficio): uno de corbata o de mano muy cerca de
la boca; si no, uno direccional apuntado a quien habla. La distancia manda más que el patrón:
acercar el micrófono a la fuente mejora la relación entre voz y ruido más que cualquier otro
ajuste. La cifra la da DPA: **«The SPL from point sources drops by 6 dB/doubling of distance.»**
Si la boca se toma como fuente puntual (aproximación de oficio), pasar el micrófono de 40 a 20 cm sube la voz
unos 6 dB y de 40 a 10 cm unos 12 dB, mientras el ruido de fondo, que llega de lejos y de todas
partes, apenas cambia (cálculo sobre la cifra de DPA; que el ruido del entorno no cambie también
es aproximación de oficio). Un micrófono direccional muy cerca suma, además, el efecto de proximidad. Y se evitan fuentes constantes cercanas (generadores, aires acondicionados, tráfico) que en
montaje no se pueden quitar.

### El ambiente no se falsea

El sonido ambiente forma parte de la verdad de la información. El Libro de estilo (3.2.2,
«Imágenes ‘falsas’», p. 46): **«La música o el falseamiento del sonido ambiente también es un procedimiento
reprobable porque aleja de la realidad y ofrece al espectador una sensación de ﬁcción indeseable. En
caso de que el sonido original tenga defectos que impidan su emisión, o no exista por cualquier
razón, el ‘falseamiento’ se efectuará sólo con sonidos idénticos a los de la realidad, o lo más
parecidos que sea posible.»** Por eso el cámara graba ambiente de sobra: para que no haya que
inventarlo.

### La continuidad del sonido

El raccord también es sonoro. El Libro de estilo (6.4, «El raccord», p. 92) lo pone entre los
aspectos que deben mantenerse: **«Sonoro. El nivel de las voces, el sonido ambiente y el ruido de
fondo tienen que permanecer en el vídeo sin alteraciones.»**

Lo que eso pide a la captación (oficio): el mismo micrófono y el mismo nivel para una misma persona
a lo largo de la entrevista; ambiente continuo del mismo lugar, grabado unos segundos sin nadie
hablando, para cubrir los cortes; y los recursos del lugar grabados con su propio ambiente, no en
silencio.

## Criterios básicos

### El reparto de canales

La regla de la casa está en el Libro de estilo de Canal Sur (5.4, p. 82): **«Como norma general, el
sonido directo de declaraciones, ruedas de prensa o el del periodista ante cámara se registra por el
canal 1. El canal 2 recoge el sonido ambiente, captado a través del micrófono de la cámara.»**

Aplicado a las situaciones habituales (la columna del canal 1 y la del canal 2 salen del Libro de
estilo; lo demás es oficio):

| Situación | Canal 1 | Canal 2 |
|---|---|---|
| Declaración o entrevista | Corbata (cable o inalámbrico) o micrófono de mano del periodista | Micrófono de cámara (ambiente) |
| Rueda de prensa | Salida de la mesa de sonido, en ***LINE***, o micrófono en el atril | Micrófono de cámara |
| Periodista ante cámara (entradilla, directo) | Su micrófono | Micrófono de cámara |
| Actuación musical, discurso, ensayo | De la mesa de sonido | Micrófono de cámara; o los dos canales para el sonido, si es la noticia |
| Recursos sin nadie hablando | Micrófono de cámara, si la cámara permite asignarlo a los dos canales | Micrófono de cámara |

Con cuatro canales (como en la Z200) caben dos voces separadas y el ambiente: por ejemplo,
entrevistado y periodista con un inalámbrico cada uno, y el ambiente en otra pista. Cómo reparte
CSRTV los canales 3 y 4 no consta en un documento publicado.

### Antes de grabar

No hay norma que fije la comprobación; es oficio:

1. Pilas o baterías de micrófonos, emisores y receptores, y de repuesto.
2. Inalámbricos en la misma banda y grupo, cada emisor en su receptor, y canal libre.
3. Conmutadores de entrada según la fuente (LINE, MIC, MIC+48V); fuente de cada canal en el menú.
4. Canales en manual; limitador puesto; filtro de viento si hace falta; paravientos puesto.
5. Tono de referencia a −18 dB si se trabaja según la EBU R 68, y tono con las barras si se graban.
6. Código de tiempo acordado con el periodista (y enclavado con el grabador, si lo hay).
7. Prueba de voz, nivel y escucha con auriculares.

El Libro de estilo lo recomendaba para la cinta (p. 82): **«Es conveniente mantener la norma de
registrar una sola noticia por cinta, después de un mínimo de treinta segundos de barras al
principio de la misma. Si hay dos noticias en el mismo soporte deben separarse con un minuto de
barras.»** Es una regla escrita para cinta; con tarjeta,
qué se graba al empezar lo decide cada casa, y no consta una regla vigente de CSRTV.

### Mientras se graba

- Auriculares puestos siempre (oficio). El medidor dice cuánto; el oído dice qué: un roce, el
  viento, un zumbido, un inalámbrico que corta o un canal que no entra.
- Nivel vigilado **«con rigor para evitar defectos y saltos de volumen»** (Libro de estilo, 5.4).
- Ambiente siempre, también en los recursos.
- En una entrevista, dejar hablar sin pisar: la pregunta del periodista y la respuesta no deben
  solaparse, porque en montaje no se pueden separar (oficio).
- Grabar unos segundos antes y después de cada declaración.

### Después de grabar

- Revisar en el sitio, **«desde la perspectiva de la imagen y del sonido»** (Libro de estilo, p. 82).
- Avisar a redacción de lo que falta o falla: un canal con ruido, un plano en cámara lenta sin
  sonido, una declaración con un golpe de viento.

### Los errores típicos

Es oficio, y así se da:

| Error | Qué pasa | Cómo se evita |
|---|---|---|
| Micrófono de condensador en ***MIC*** sin pila | No suena | ***MIC+48V*** o pila |
| Micrófono no preparado para fantasma en ***MIC+48V*** | Puede dañarse (lo advierte la Z200) | Comprobar el conmutador antes de enchufar |
| Salida de mesa en ***MIC*** | Satura | ***LINE*** |
| Nivel en automático en una entrevista | El ruido sube en las pausas | Manual |
| Picos en 0 dBFS | Distorsión que no se arregla | Bajar el nivel; limitador |
| Dos inalámbricos en grupos distintos | Interferencias | El mismo grupo |
| Corbata rozando la ropa | Ruido de roce | Colocación y sujeción del cable |
| Grabar sin auriculares | Los fallos se descubren en la redacción | Escucha continua |
| Canal de fábrica en ***[Internal MIC]*** | El corbata conectado no se graba | Elegir la fuente de cada canal |
| Plano en cámara lenta | No se graba sonido | Avisar; grabar el ambiente aparte |

## Recomendaciones técnicas que el tema cita

| Documento | Qué se toma |
|---|---|
| EBU R 68-2000 | Nivel de alineación a 18 dB bajo el máximo (1:8, 18,06 dB); alineación 9 u 8 dB bajo el nivel máximo permitido; picos reales hasta 15 dB sobre la alineación; codificación lineal y al menos 16 bits |
| EBU R 128-2023 (V5) | Nivel objetivo −23,0 LUFS, ±1,0 LU en directo, ±0,2 LU de medida; pico verdadero −1 dBTP en producción, ±0,3 dB (señales limitadas a 20 kHz); el QPPM no mide sonoridad; LUFS = LKFS; LRA no recomendado en programas de menos de un minuto |
| EBU Tech 3341-2023 | Lecturas M (0,4 s, sin puerta), S (3 s, sin puerta) e I (con puerta según la BS.1770); 1 LU = 1 dB |
| EBU Tech 3343-2023 | Tono de 1 kHz a −18 dBFS; la sonoridad no cambia la alineación; PML de −9 dBFS obsoleto; −18 LUFS con el tono en fase en los dos canales; medidor de pico para alinear; margen de 1 dB bajo 0 dBFS; −2 dBTP para la reducción de datos MPEG-1 Layer 2 y AC-3; más margen para el público; comentaristas en torno a −24 LUFS en deportes |

La UIT-R BS.1770, la UIT-R BS.645, la UIT-R BS.646, la EBU Tech 3342 y la AES14 se nombran sólo
como las citan esas recomendaciones o la AES; su texto no se ha leído.

## Lo que este tema no da, y dónde está

- Qué cámaras, micrófonos e inalámbricos usa CSRTV: no consta en un documento publicado localizado.
  Los ejemplos del tema son de la Sony PXW-Z200, cámara del mercado con documentación pública.
- Cómo reparte CSRTV los canales 3 y 4, y si mantiene hoy alguna regla sobre tono y barras en
  tarjeta: el Libro de estilo de 2004 sólo trata los canales 1 y 2 y la cinta.
- Un nivel de voz en cámara en dBFS (el «pico a −12» y similares): ninguna norma leída lo fija; no se
  da ninguna cifra.
- De dónde sale el −20 dB que la Z200 trae de fábrica para el tono: no consta en las fuentes leídas.
- Qué significa la opción ***[EBUL]*** de la Z200: el manual no lo explica.
- Las bandas de frecuencia que pueden usar los micrófonos inalámbricos en España: son materia del
  Cuadro Nacional de Atribución de Frecuencias, que el tema no ha leído.
- Los límites de la banda audible por zonas (graves, medios, agudos), el cálculo de 6 dB por bit y
  el margen dinámico del oído (unos 120 dB) son oficio y cálculo, no norma.
- Los formatos de fichero y la entrega del audio con la imagen, en el tema 7; el trabajo con
  redacción y la entrevista, en el tema 8; la calidad técnica, en el tema 9; el directo y los
  retornos, en los temas 3 y 13; la cámara lenta, en el tema 15; el ruido como riesgo laboral
  (auriculares a volumen alto, entornos ruidosos), en los temas 14 y 17.

## Trazabilidad

Todas las fuentes se leyeron el 24/09/2026, salvo las páginas de DPA Microphones, leídas el 25/09/2026.

| Fuente | Qué sostiene |
|---|---|
| *Libro de estilo de Canal Sur Televisión y Canal 2 Andalucía*, RTVA, 1.ª ed., marzo de 2004 | Equipo de la entrevista con auriculares y micrófonos, corbata para quien habla (3.17.1, p. 59); micrófono de mano no se cede (3.17.1.3, p. 60); micrófono en directo (8.3.2, p. 117); roce de tejidos (8.6.1, p. 122); código de tiempo (5.3.3, p. 81); barras (recomendación para cinta) y revisión en el sitio (p. 82); canales 1 y 2, mesa, ambiente siempre, sonido como noticia, ambientes ruidosos, nivel vigilado (5.4, p. 82); falseamiento del ambiente (3.2.2, p. 46); raccord sonoro (6.4, p. 92) |
| EBU R 68-2000, *Alignment level in digital audio production equipment and in digital audio recorders* | −18 dBFS; 1:8 (18,06 dB); 9 u 8 dB bajo el PML; picos 3, 6 y 15 dB; 16 bits y su nota 1 completa |
| EBU R 128-2023 (V5, noviembre de 2023), *Loudness normalisation and permitted maximum level of audio signals* | Considerandos a), b), c) y e); puntos h), i), k), m) y n); notas 1 y 2; historial de revisiones |
| EBU Tech 3341-2023 (V4, noviembre de 2023), *Loudness Metering: ‘EBU Mode’ metering to supplement EBU R 128 loudness normalization* | M, S, I y sus ventanas; 1 LU = 1 dB (§ 2.4) |
| EBU Tech 3343-2023, *Guidelines for Production of Programmes in accordance with EBU R 128* | § 8.1 (tono, alineación, PML obsoleto, −18 LUFS y su condición, medidor de pico); pico verdadero y margen de 1 dB; −2 dBTP para MPEG-1 Layer 2 y AC-3; público en deportes; § 3.5.1 (−24 LUFS) |
| Sony, *PXW-Z200/HXR-NX800 Help Guide*, 5-060-574-13(1), 2024 | Conmutador LINE/MIC/MIC+48V y sus avisos (p. 136); AUTO/MAN (p. 16); nivel manual (p. 138); cuatro canales XLR (p. 139); menú de audio (pp. 260-261); escucha y bits de usuario (p. 99); sin sonido en cámara lenta (p. 136); código de tiempo y su pérdida de enclavamiento (p. 298); formato LPCM (p. 336); respuesta en frecuencia y margen dinámico (p. 337); entradas y micrófono interno (p. 338) |
| AES, presentación de sus normas | Que la AES14 es la norma del conector XLR analógico |
| DPA Microphones, *Mic University*: «Proximity effect in microphones explained», «About balanced and unbalanced lines», «Electromagnetic interference: EMC, RFI immunity and CMRR», «10 points on microphones in installed systems»; y su diccionario («Proximity Effect», «Balanced and Unbalanced Lines»). Leídos el 25/09/2026 | Efecto de proximidad: definición, patrones, distancia, ángulo, causa y respuesta plana de cerca; caída de 6 dB por duplicar la distancia en una fuente puntual; línea balanceada, patillas del XLR, rechazo en modo común y CMRR, fantasma sólo en línea balanceada; cableado no balanceado corto; fuentes de interferencia |

Oficio sin norma detrás, y así se declara: el papel del cámara como técnico de sonido; las
magnitudes del sonido, el margen audible y sus zonas; los transductores; los tipos de micrófono, los
patrones polares y sus usos; los soportes; la colocación del corbata; los grupos de frecuencia de los
inalámbricos y el uso de dos inalámbricos; el margen dinámico y el del oído; el uso del automático y
el limitador; el procedimiento de ajuste de nivel; el uso del micrófono de mano frente al efecto de proximidad; la tirada larga de cable a la entrada XLR y no al minijack; la boca como fuente puntual y el ruido de fondo que no cambia con la distancia; el sistema único y el doble sistema; la cámara
fotográfica y el sonido aparte; la claqueta; la re-sincronización periódica; el reparto de las
situaciones por canales más allá de la regla del Libro de estilo; las listas de comprobación y los
errores típicos. Es cálculo, y se puede rehacer: 6,02 dB por bit (20 × log 2) y los 96 y 144 dB de 16
y 24 bits; la suma de 9 + 6 dB (15 dB) sobre la alineación frente a los 18 dB de reserva; los 6 y
12 dB de acercar el micrófono a la mitad y a la cuarta parte de la distancia.
