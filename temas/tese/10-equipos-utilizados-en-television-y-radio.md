# Tema 10 del específico de Técnica de Equipos y Sistemas Electrónicos · Equipos utilizados en televisión y radio

Las siglas de este tema, presentadas de entrada: el panel remoto de control de cámara (**RCP**,
*remote control panel*); la unidad de control de cámara (**CCU**, *camera control unit*); los tres
primarios rojo, verde y azul (**RGB**); la línea de alternancia de fase (**PAL**, *phase alternating
line*); el conjunto redundante de discos independientes (**RAID**, *redundant array of independent
disks*); la conexión serie de tecnología avanzada (**SATA**, *serial advanced technology attachment*);
el terabyte (**TB**); la escucha previa al atenuador (**PFL**, *pre fade listen*); el efecto de baja
frecuencia (**LFE**, *low frequency effect*); el decibelio referido a 0,775 voltios (**dBu**); el
factor de calidad de un filtro (**Q**); el conector de rosca Bayonet Neill-Concelman (**BNC**); el
conector de audio profesional de tres contactos (**XLR**); el conector de red de ocho contactos
(**RJ 45**); la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**), que da nombre al conector
híbrido de fibra; y la interfaz digital serie (**SDI**), presentada en el tema 8.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 12):
> «EQUIPOS UTILIZADOS EN TV Y RADIO: Cámaras de Estudio. Diagrama de bloques. Captación de imagen.
> Procesado analógico y digital. Ópticas. Transmisión cableada (Triax y Fibra) y transmisión
> inalámbrica. Formatos de Grabación (Interno y Externo). Camcorders y formatos de grabación.
> Mezcladores de video. Editores no lineales. Servidores de video. Generadores de efectos digitales.
> Tituladores. Equipos de grafismo. Matrices de conmutación. Mezclador de Sonido. Generadores de
> sincronismos. Equipos de monitoreo de vídeo. Monitores y medidores de vídeo. Sistemas de
> Multipantalla. Equipos de monitoreo de audio. Altavoces, sistemas de escucha personalizada,
> medidores de audio.»

**Diecinueve preguntas: el banco más grande de la ocupación**, y **el enunciado más largo de su
anexo.** **Las dos cosas van juntas**: este punto es el inventario de la sala técnica, y el examen lo
recorre pieza a pieza.

**Su reparto**: **siete preguntas son de la cadena de vídeo** —óptica, matriz de color, submuestreo,
compresión, canal alfa, matriz de conmutación y panel de cámara—; **seis son de la cadena de audio**
—micrófono, ecualizador, escucha previa, niveles, vúmetro y realimentación—; **dos son de
almacenamiento en disco**; **una es de conectores**; **y tres son de cálculo.**

**Dos de las diecinueve dependen de una figura** —la 16 del primer cuadernillo, que enseña un
preamplificador, y la 16 del segundo, que enseña un panel de conexiones—, y **este tema no describe
ninguna de las dos**: da la regla de su familia y declara que la respuesta descansa en la plantilla.

<!-- indice -->

## Índice

- [1. La cámara de estudio y su óptica](#1-la-cámara-de-estudio-y-su-óptica)
- [2. El color: la ecuación de luminancia](#2-el-color-la-ecuación-de-luminancia)
- [3. La compresión y la matriz de conmutación](#3-la-compresión-y-la-matriz-de-conmutación)
- [4. Los servidores de vídeo y el RAID](#4-los-servidores-de-vídeo-y-el-raid)
- [5. El mezclador de sonido](#5-el-mezclador-de-sonido)
- [6. El micrófono, el vúmetro y el efecto Larsen](#6-el-micrófono-el-vúmetro-y-el-efecto-larsen)
- [7. Las dos preguntas con figura](#7-las-dos-preguntas-con-figura)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. La cámara de estudio y su óptica

**La cadena de una cámara de estudio va del objetivo al conector de salida**, y **el examen pregunta
por tres de sus eslabones: la óptica, el procesado de color y el mando a distancia.**

**El bloque de captación**: la luz entra por el objetivo, un divisor la reparte en tres caminos —rojo,
verde y azul— y cada camino cae sobre un sensor. **Lo que sale de ahí son tres señales analógicas que
todavía no son una imagen de televisión**: hay que corregirlas.

**El bloque de procesado** hace esa corrección, y de él sale la señal que la instalación transporta.
**El mando de todo ese bloque no está en la cámara**: está en la unidad de control, y el operador lo
maneja desde el panel remoto.

**La pregunta 9 es de óptica pura**: **una mayor distancia focal disminuye la profundidad de campo.**
Ésa es la respuesta oficial.

---

**Y la regla que hay detrás, porque el examen la ha preguntado en tres ocupaciones distintas**: **la
profundidad de campo crece con el diafragma cerrado, con la distancia al sujeto y con el gran
angular**, y **decrece con el diafragma abierto, con la proximidad y con el teleobjetivo.** **Un
objetivo de mucha focal es un teleobjetivo**, luego menos profundidad de campo. **Las opciones a y b
invierten la relación y la d la niega.**

**La pregunta 66 es la más larga del cuadernillo y la más técnica del tema**: **la corrección
«Matrix» de una cámara de televisión sirve para, mediante combinaciones de las componentes RGB,
compensar valores espectrales de la luz que no se han podido captar en la conversión óptico-eléctrica,
obteniendo una colorimetría adecuada.** Ésa es la respuesta oficial.

---

**Por qué esa y no las otras tres, que es donde está la dificultad**: **ninguna de las cuatro opciones
es absurda**, y **la a describe algo que la cámara sí hace —obtener la luminancia a partir del RGB—
pero que no es la matriz**: eso lo hace el codificador con los coeficientes del epígrafe siguiente.
**La c describe el recorte de altas luces, que es el «knee».** **La d describe el seguimiento
automático de la temperatura de color, que es otro circuito.** **La matriz corrige lo que el prisma y
los filtros no separaron bien**, y **por eso su definición habla de valores espectrales no captados.**

**La pregunta 1 del segundo cuadernillo es negativa y va del panel**: **la afirmación incorrecta sobre
las posibilidades operativas del panel remoto en una producción en directo sin robotizar es que
controle el enfoque de manera remota.** Ésa es la respuesta oficial.

---

**Y el porqué está en las tres palabras «sin robotizar»**: **el panel remoto gobierna el diafragma, el
balance de blancos, el nivel de negro y la gamma, que son ajustes eléctricos del bloque de
procesado**; **el enfoque es un movimiento mecánico del objetivo**, y **sin cabeza robotizada lo hace
el cámara con su mano.** **Con cabeza robotizada sí se enfoca a distancia**, y por eso el enunciado se
molesta en excluirla.

## 2. El color: la ecuación de luminancia

**La pregunta 23 pide la ecuación**: **en el espacio colorimétrico del sistema PAL, la luminancia se
forma como Y = 0,30R + 0,59G + 0,11B.** Ésa es la respuesta oficial.

---

**Los tres coeficientes no son arbitrarios**: **son la sensibilidad relativa del ojo a cada
primario.** **El verde aporta cerca de tres quintos de la luz percibida, el rojo algo menos de un
tercio y el azul poco más de una décima.** **Las tres opciones falsas son la misma ecuación con los
coeficientes permutados**, de modo que **la pregunta se contesta sabiendo únicamente cuál es el
primario que más pesa y cuál el que menos**: **el mayor va con la G y el menor con la B.**

**La regla de memoria que salva la pregunta**: **verde, rojo, azul, de mayor a menor.** **Sumados dan
la unidad**, que es la comprobación de que la ecuación está bien copiada.

**La pregunta 48 va del submuestreo**: **4:2:2, en codificación de vídeo, significa submuestreo de
color.** Ésa es la respuesta oficial.

---

**Y la notación se lee así**: **la primera cifra es la referencia de muestreo de la luminancia, y la
segunda y la tercera dicen cuántas muestras de cada diferencia de color se toman por cada cuatro de
luminancia.** **En 4:2:2 el color va a la mitad de resolución horizontal que la luminancia y a la
misma resolución vertical.** **En 4:2:0 va a la mitad en las dos direcciones.** **En 4:4:4 no hay
submuestreo.**

**Por qué se puede hacer sin que se note**: **el ojo distingue mucho mejor los detalles de brillo que
los de color**, que es la misma razón por la que existe la ecuación de luminancia del comienzo del
epígrafe. **Las tres opciones falsas —relación de aspecto, resolución y frecuencia de cuadro— son los
otros tres parámetros que describen un formato**, y todas se escriben con otras notaciones: 16:9,
1920×1080 y 25 fps.

**La pregunta 25 va del canal alfa**: **en un entorno de vídeo, el canal «Alpha» es la señal de escala
de grises cuya información es la transparencia que hay que aplicar a otra señal.** Ésa es la respuesta
oficial.

---

**Cómo funciona**: **el negro del alfa es transparencia total y el blanco es opacidad total**, o al
revés según el convenio del equipo, **y los grises intermedios son las transiciones suaves de los
bordes.** **Un rótulo se transporta siempre en dos señales**: **el relleno, que es lo que se ve, y la
llave, que es dónde se ve.** **El alfa es la llave.** **La opción d inventa un canal «Omega» que no
existe.**

## 3. La compresión y la matriz de conmutación

**La pregunta 13 va de compresión**: **la principal ventaja de la compresión de vídeo entre cuadros
sobre la de cuadro completo es que reduce el tamaño del archivo al aprovechar la redundancia temporal
entre cuadros sucesivos.** Ésa es la respuesta oficial.

---

**La diferencia entre las dos familias, que es lo único que hay que retener:**

| Familia | Qué codifica | Qué gana | Qué pierde |
|---|---|---|---|
| **Intra-cuadro** | **Cada cuadro entero e independiente** | **Acceso y edición cuadro a cuadro** | **Ocupa mucho más** |
| **Inter-cuadro** | **Un cuadro de referencia y las diferencias con los siguientes** | **Ocupa mucho menos** | **Para llegar a un cuadro hay que reconstruir los anteriores** |

**Y de ahí sale sola la clasificación de las opciones falsas**: **la a describe la ventaja del
intra-cuadro y la d su definición**, **y la c promete calidad sin pérdidas, que no es lo que ninguna
de las dos familias ofrece.** **La palabra que decide la respuesta es «temporal»**: la redundancia que
el inter-cuadro aprovecha está en el tiempo, no dentro de la imagen.

**La pregunta 86 completa una frase**: **una matriz de vídeo es un dispositivo electrónico capaz de
conmutar señales de vídeo de una fuente a varios destinos.** Ésa es la respuesta oficial.

---

**Y la trampa está en dos palabras que las cuatro opciones barajan: «mezclar» y «conmutar».**

| Equipo | Qué hace | Cuántas señales salen |
|---|---|---|
| **Matriz de conmutación** | **Encamina: elige qué entrada llega a cada salida** | **La entrada elegida, intacta** |
| **Mezclador de vídeo** | **Combina: encadena, funde, incrusta** | **Una señal nueva que no era ninguna de las de entrada** |

**Una matriz no mezcla nada.** **No hay transición, no hay incrustación, no hay señal nueva**: hay un
camino que se abre y otro que se cierra. **Y una misma entrada puede ir a la vez a varias salidas,
que es literalmente lo que dice la opción correcta.**

## 4. Los servidores de vídeo y el RAID

**Dos preguntas del tema son de almacenamiento en disco, y las dos son de cálculo.**

**La pregunta 62**: **si dos discos SATA de 1 TB se presentan al sistema operativo como una única
unidad de 2 TB, la configuración es RAID 0.** Ésa es la respuesta oficial.

**La pregunta 32**: **un RAID 5 con cuatro discos de 2 TB da una capacidad teórica total de 6 TB.**
Ésa es la respuesta oficial.

---

**Los cuatro niveles que el examen usa, con su cuenta:**

| Nivel | Qué hace | Capacidad útil con *n* discos de tamaño *c* | Discos que puede perder |
|---|---|---|---|
| **RAID 0** | **Reparte los datos entre los discos** | **n × c**: toda | **Ninguno** |
| **RAID 1** | **Escribe lo mismo en dos discos** | **c**: la mitad | **Uno** |
| **RAID 3** | **Reparte y dedica un disco entero a la paridad** | **(n − 1) × c** | **Uno** |
| **RAID 5** | **Reparte y distribuye la paridad entre todos** | **(n − 1) × c** | **Uno** |

**Con esa tabla las dos preguntas se resuelven en dos líneas**: **dos discos de 1 TB que suman 2 TB
visibles sólo caben en el nivel 0**, porque el 1 daría 1 TB y el 3 y el 5 necesitan tres discos como
mínimo; **y cuatro discos de 2 TB en nivel 5 dan (4 − 1) × 2 = 6 TB.**

**El aviso que conviene llevar aprendido**: **el RAID 0 no es redundante pese al nombre de la
familia.** **Reparte para ir más deprisa y para sumar capacidad, y si cae un disco se pierde todo.**
**Es la configuración que más capacidad ofrece y la única que no protege de nada.**

## 5. El mezclador de sonido

**Seis preguntas del tema son de la cadena de audio, y cuatro de ellas caben en el mezclador.**

**La pregunta 18 va del ecualizador**: **en un ecualizador paramétrico, el ancho de banda del filtro
alrededor de la frecuencia central se determina ajustando el factor de calidad (Q).** Ésa es la
respuesta oficial.

---

**Los tres mandos de una banda paramétrica, que es lo que la distingue de las demás:**

| Mando | Qué elige |
|---|---|
| **Frecuencia** | **Dónde actúa el filtro** |
| **Ganancia** | **Cuánto realza o atenúa** |
| **Factor de calidad** | **Cómo de ancha es la campana** |

**Y la relación del último es inversa**: **a más factor de calidad, más estrecha la campana.** **Un
ecualizador que sólo tiene los dos primeros mandos es semiparamétrico o de banda fija, no
paramétrico.** **Las tres opciones falsas nombran mandos de otros procesadores** —el compresor y su
umbral, y un expansor con canal de efectos de baja frecuencia—, **que no son de ecualización.**

**La pregunta 24 va de la escucha previa**: **la función del modo PFL en un mezclador de audio es
reproducir la señal de audio antes de pasar por el atenuador para monitorizarla a través de los
auriculares o monitores, sin enviarla al bus principal.** Ésa es la respuesta oficial.

---

**Las siglas lo dicen todo cuando se traducen**: *pre fade listen*, **escucha antes del atenuador.**
**Sirve para comprobar un micrófono, un teléfono o una cinta con el atenuador cerrado**, es decir, sin
que salga al aire. **Es la maniobra que hace un técnico de continuidad cien veces al día.** **La
opción b traduce mal las siglas a propósito** —*low frequency*, y además después del máster—, **y las
otras dos describen el limitador y el panorámico.**

**La pregunta 95 es de cálculo**: **si la ganancia del canal está ajustada a −3 dB y se quiere que el
nivel en el bus sea de 1 dB, el atenuador debe ponerse en +4 dB.** Ésa es la respuesta oficial.

---

**Y la cuenta es una suma**: **los decibelios de las etapas en cadena se suman**, luego −3 + x = 1 y
x = 4. **Nada más.** **La única forma de fallarla es restar en vez de sumar o confundir el signo de la
ganancia de entrada.**

**La pregunta 78 es de nivel absoluto**: **en audio analógico, 0 dBu son 0,775 voltios eficaces.** Ésa
es la respuesta oficial.

---

**Y el porqué de esa cifra tan rara, que es lo que la hace memorizable**: **el dBu se definió sobre la
tensión que disipa un milivatio en 600 ohmios**, la impedancia de las líneas telefónicas de las que
viene el oficio. **La raíz de 0,001 × 600 es 0,7746.** **La opción a, 1,228 voltios, es el pico de esa
misma onda multiplicado por raíz de dos y algo más**: es la trampa de confundir eficaz con pico.

## 6. El micrófono, el vúmetro y el efecto Larsen

**La pregunta 15 va de directividad**: **la principal ventaja de utilizar un micrófono hipercardioide
en un entorno de grabación es un mayor rechazo de sonido lateral.** Ésa es la respuesta oficial.

---

**Las cuatro directividades que el examen maneja:**

| Patrón | De dónde capta | Para qué se usa |
|---|---|---|
| **Omnidireccional** | **De todas las direcciones por igual** | **Ambiente, sala** |
| **Cardioide** | **Del frente, con rechazo por detrás** | **Voz de uso general** |
| **Hipercardioide** | **Del frente, con lóbulos laterales muy cerrados y algo de captación trasera** | **Aislar una fuente en sala ruidosa** |
| **Bidireccional** | **Del frente y de detrás, no de los lados** | **Entrevista cara a cara** |

**El hipercardioide es el más estrecho de los tres primeros**, y **eso es exactamente lo que dice la
respuesta oficial.** **La opción a describe el omnidireccional**; **la c y la d confunden directividad
con respuesta en frecuencia y con sensibilidad**, que son parámetros distintos del mismo micrófono.

**La pregunta 80 va del vúmetro**: **un vúmetro mide el nivel de una señal de audio con una respuesta
lenta a los cambios.** Ésa es la respuesta oficial.

---

**Y la lentitud no es un defecto: es la especificación.** **El vúmetro se diseñó para seguir la
sensación de sonoridad, no el pico instantáneo**, y por eso su aguja tarda unos trescientos
milisegundos en llegar al valor. **Un transitorio de percusión lo supera sin que la aguja se entere**,
que es justo lo que la opción a describe y lo que la b niega. **El instrumento que sí sigue los picos
es el picómetro**, y **el tema 13 los pone frente a frente.**

**La pregunta 88 va de realimentación**: **el efecto que se produce cuando el sonido de los altavoces
es captado nuevamente por el micrófono es el efecto Larsen.** Ésa es la respuesta oficial.

---

**Es un lazo cerrado**: **el micrófono capta, el amplificador amplía, el altavoz emite y el micrófono
vuelve a captar lo emitido.** **Cuando la ganancia del lazo llega a la unidad el sistema oscila**, y
la oscilación se oye como el pitido característico. **Se combate bajando la ganancia, alejando el
micrófono del altavoz, orientándolos para que el altavoz quede en la zona de rechazo del micrófono
—que es para lo que sirve el epígrafe anterior— o atenuando con el ecualizador la frecuencia a la que
el lazo arranca.** **Las tres opciones falsas nombran otros tres efectos reales**: el «pop» de las
consonantes explosivas, el de proximidad de los micrófonos direccionales y la reverberación de sala.

## 7. Las dos preguntas con figura

**Dos de las diecinueve enseñan una fotografía**, y **este temario no la ha visto.** **No se describe
lo que no se ha visto**: se da la regla de la familia y se declara que la respuesta viene de la
plantilla.

**La pregunta 16 del primer cuadernillo** enseña un preamplificador de audio y pide el nivel de salida
aproximado en dBu. **La plantilla da 12 dBu.** **La regla de la familia, que es lo que sí se puede
llevar aprendido**: **la escala de un medidor de aparato profesional está rotulada en dBu**, y **los
cuatro valores que el examen ofrece —0, 4, 8 y 12— son los cuatro escalones habituales de esa
escala**; **el nivel de línea profesional de referencia es +4 dBu** y **la reserva por encima de él
llega típicamente hasta cerca de +20 dBu**, de modo que las cuatro opciones son todas verosímiles y
**sólo la lectura del aparato decide.**

**La pregunta 16 del segundo cuadernillo** enseña un pequeño panel de conexiones de una instalación
fija de estadio, con dos puertos rotulados CAM 3 y CAM 4, y pide qué conector se ve. **La plantilla da
el conector SMPTE híbrido de fibra óptica.** **La regla de la familia:**

| Conector | Qué lleva | Dónde se ve |
|---|---|---|
| **BNC** | **Una señal coaxial**: SDI, sincronismo, vídeo | **Matrices, monitores, distribuidores** |
| **XLR** | **Una línea de audio equilibrada** | **Micrófonos, mezcladores** |
| **RJ 45** | **Un enlace de red de par trenzado** | **Conmutadores, equipos sobre red** |
| **Conector híbrido SMPTE de fibra** | **Dos fibras ópticas y la alimentación de la cámara en el mismo cuerpo** | **Bases de cámara de instalaciones fijas y unidades móviles** |

**Y la palabra que resuelve la familia es «CAM»**: **un puerto de cámara de instalación fija de
estadio no se cablea con un conector de audio ni con uno de red**, y **el coaxial de un BNC no lleva
la alimentación.** **El conector híbrido es el único de los cuatro que resuelve en un solo cuerpo lo
que una cámara de estudio necesita: ida, vuelta y corriente.** **Aun así, la identificación concreta
del que aparece en la fotografía descansa en la plantilla**, y el temario lo declara.

## 8. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 9 | Efecto de la distancia focal en la profundidad de campo | c) Mayor focal, menor profundidad ✔ |
| 13 | Ventaja del inter-cuadro sobre el intra-cuadro | b) Aprovecha la redundancia temporal ✔ |
| 15 | Ventaja del micrófono hipercardioide | b) Mayor rechazo lateral ✔ |
| 16 | Nivel de salida del preamplificador de la figura | d) 12 dBu ✔ (figura) |
| 18 | Cómo se fija el ancho de banda en un paramétrico | c) Con el factor de calidad ✔ |
| 23 | Ecuación de luminancia del PAL | d) Y = 0,30R + 0,59G + 0,11B ✔ |
| 24 | Función del modo PFL | d) Escucha antes del atenuador, sin ir al bus ✔ |
| 25 | Qué es el canal alfa | c) Escala de grises de transparencia ✔ |
| 32 | Capacidad de un RAID 5 de cuatro discos de 2 TB | d) 6 TB ✔ |
| 48 | Qué significa 4:2:2 | b) Submuestreo de color ✔ |
| 62 | RAID de dos discos de 1 TB que se ven como 2 TB | a) RAID 0 ✔ |
| 66 | Función de la corrección «Matrix» | b) Compensar valores espectrales no captados ✔ |
| 78 | Voltios que son 0 dBu | c) 0,775 voltios eficaces ✔ |
| 80 | Qué mide un vúmetro | a) Nivel con respuesta lenta ✔ |
| 86 | Definición de matriz de vídeo | b) Conmutar de una fuente a varios destinos ✔ |
| 88 | Sonido del altavoz recaptado por el micrófono | b) Efecto Larsen ✔ |
| 95 | Atenuador para pasar de −3 dB a 1 dB | b) +4 dB ✔ |
| 1 (2.º llam.) | Afirmación incorrecta sobre el panel remoto | b) Que controle el enfoque a distancia ✔ |
| 16 (2.º llam.) | Conector de los puertos CAM 3 y CAM 4 | d) SMPTE híbrido de fibra ✔ (figura) |

**Las diecinueve respuestas oficiales son correctas.** **Dos descansan en la plantilla**, y son las
dos que llevan figura.

**El aviso de estudio**: **tres de las diecinueve son cálculo puro** —el RAID 5, el RAID 0 y la suma
de decibelios—, **dos son cifras que hay que memorizar** —los coeficientes de luminancia y los 0,775
voltios— **y las catorce restantes se contestan sabiendo qué hace cada aparato.** **Es el punto donde
más rinde repasar el inventario de la sala.**

## 9. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **conviene decirlo de entrada porque es
excepcional en esta ocupación**: es un punto de inventario, y **un inventario de equipos no está
articulado en ningún sitio.**

**Lo único que sí tiene respaldo de primer nivel son las unidades**: **el voltio y el ohmio del
epígrafe 5 son unidades legales de medida en España**, fijadas por el **Real Decreto 2032/2009**
(`BOE-A-2010-927`), **y el decibelio figura en ese mismo real decreto como nota al cuadro de unidades
derivadas.** **El tema los usa como magnitudes, no cita su texto**, y **el tema 1 de esta misma
ocupación sí recoge las celdas correspondientes literalmente.**

**Seis declaraciones expresas:**

1. **Las normas SMPTE que dan nombre al conector híbrido no se han consultado.** **Lo que este tema
   afirma del conector es lo que la respuesta oficial afirma —que es híbrido, de fibra óptica y de
   la SMPTE— y lo que su uso universal describe: dos fibras y la alimentación en un cuerpo.** **El
   temario no atribuye a ningún apartado de esas normas el número de fibras ni la tensión de
   alimentación**, y **ninguna pregunta depende de ellos.**
2. **Los coeficientes 0,30, 0,59 y 0,11 son los de la recomendación de luminancia de definición
   estándar**, de uso universal desde la televisión en color analógica. **Coinciden con la respuesta
   oficial**, y **el tema los presenta como conocimiento común de la materia, no como cita.**
3. **Las cifras de nivel de la escala en dBu del epígrafe 7 —el +4 de referencia y la reserva hasta
   cerca de +20— son órdenes de magnitud del uso profesional corriente**, dadas para situar las
   cuatro opciones de una pregunta cuya respuesta descansa en la plantilla. **No se atribuyen a
   ninguna norma.**
4. **El valor 0,775 voltios se deduce de su propia definición** —la tensión que disipa un milivatio
   en 600 ohmios— **y la deducción está escrita en el epígrafe 5**, de modo que la cifra no se toma
   de ninguna fuente: se calcula.
5. **El voltio, el ohmio y el decibelio se usan aquí como magnitudes de trabajo.** **Este tema no
   reproduce ninguna celda del Real Decreto 2032/2009**, y **no atribuye a ese real decreto ninguna
   de las cifras del epígrafe 5.**
6. **Las dos preguntas con figura se declaran como tales en el epígrafe 7 y en el cuadro del
   epígrafe 8.** **Este temario no ha visto ninguna de las dos imágenes y no las describe.**

**El resto del tema va como oficio y así se declara**: la profundidad de campo y sus tres variables,
el reparto de bloques de una cámara de estudio, la diferencia entre matriz y mezclador, la tabla de
niveles RAID, los tres mandos del ecualizador paramétrico, las cuatro directividades de micrófono, la
respuesta lenta del vúmetro y el lazo del efecto Larsen. **Nada de eso está en un boletín oficial ni
en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
