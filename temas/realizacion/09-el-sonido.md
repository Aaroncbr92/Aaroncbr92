# Tema 9 del específico de Realización (Asistencia) · El sonido

Las siglas de este tema, presentadas de entrada: el hercio (**Hz**) y el kilohercio (**kHz**), que
miden la frecuencia; el decibelio (**dB**) y el decibelio ponderado A (**dBA**), que miden el nivel;
el nivel de presión sonora (**NPS**, *SPL* en inglés, del inglés *sound pressure level*); el
Grupo de Expertos en Imágenes en Movimiento (**MPEG**); el formato de fichero de audio en forma de
onda (**WAV**, del inglés *waveform audio file format*) y el formato de fichero de intercambio de
audio (**AIFF**, del inglés *audio interchange file format*); la codificación avanzada de vídeo
(**AVC**, del inglés *advanced video coding*); la unidad de volumen (**VU**, del inglés *volume
unit*), que da nombre al vúmetro; la realidad virtual (**RV**, *VR* en inglés); la modulación por
impulsos codificados (**PCM**, del inglés *pulse-code modulation*); el códec libre de audio sin
pérdidas (**FLAC**, del inglés *free lossless audio codec*) y su equivalente de Apple (**ALAC**, del
inglés *Apple lossless audio codec*); el Instituto Alemán de Normalización (**DIN**, del alemán
*Deutsches Institut für Normung*); la empresa **IBM**, cuyo nombre es hoy la sigla entera; el
sistema de refuerzo de sonido hacia el público (**P.A.**, del inglés *public address*); y la señal
de programa menos uno (**N-1**), que es como se escribe el retorno limpio.

**Y una que no es sigla de nada: «AIFFK».** Así está escrita una de las opciones de la pregunta 84
del segundo cuadernillo, y **es una errata del cuadernillo** por **AIFF**. Se recoge tal cual en el
epígrafe 14, porque el efecto que tiene sobre la pregunta es justamente el contrario del que se
esperaría.

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización (Asistencia),
> punto 3.4): «El sonido. Conceptos generales. Planos de sonido. Toma de sonido en exteriores y en
> estudio. Postproducción y ambientación. Equipos de sonido en exteriores y en estudio.»

**Trece preguntas.** Y hay que decir de entrada por qué un temario de realización pregunta tanto de
sonido: porque **en un control de realización el realizador no opera el sonido pero sí lo pide, lo
juzga y responde de él**. Las preguntas del examen no son de técnico de sonido: son de quien tiene
que entenderse con el técnico de sonido.

<!-- indice -->

## Índice

- [1. Las cualidades del sonido](#1-las-cualidades-del-sonido)
- [2. El rango audible y lo que queda fuera](#2-el-rango-audible-y-lo-que-queda-fuera)
- [3. Cómo se mide el sonido](#3-cómo-se-mide-el-sonido)
- [4. El tono de referencia](#4-el-tono-de-referencia)
- [5. Los micrófonos](#5-los-micrófonos)
- [6. La alimentación fantasma](#6-la-alimentación-fantasma)
- [7. Las técnicas de toma estereofónica](#7-las-técnicas-de-toma-estereofónica)
- [8. Los planos de sonido](#8-los-planos-de-sonido)
- [9. La ecualización](#9-la-ecualización)
- [10. Las capas de la banda sonora](#10-las-capas-de-la-banda-sonora)
- [11. La pista internacional](#11-la-pista-internacional)
- [12. El sonido en directo: el retorno N-1](#12-el-sonido-en-directo-el-retorno-n-1)
- [13. El sonido de un concierto: el backline](#13-el-sonido-de-un-concierto-el-backline)
- [14. Formatos y códecs de audio](#14-formatos-y-códecs-de-audio)
- [15. Los datos que el examen ha preguntado](#15-los-datos-que-el-examen-ha-preguntado)
- [16. Trazabilidad](#16-trazabilidad)

<!-- /indice -->

## 1. Las cualidades del sonido

**Un sonido se describe con cuatro cualidades, y cada una tiene detrás una magnitud física:**

| Cualidad | Magnitud física | Qué distingue |
|---|---|---|
| **Tono** o altura | **Frecuencia**, en hercios | Agudo o grave |
| **Intensidad** o volumen | **Amplitud**, en decibelios | Fuerte o flojo |
| **Timbre** | **La forma de la onda**: los armónicos que acompañan al fundamental | **Quién lo produce** |
| **Duración** | El tiempo | Largo o corto |

**El timbre es lo que permite distinguir dos instrumentos que tocan la misma nota.** Es la respuesta
oficial a la pregunta 66 y la razón está en la física: **dos instrumentos que tocan un la de 440 Hz
emiten los dos ese 440 Hz**, pero cada uno lo acompaña de una serie de armónicos —múltiplos de la
frecuencia fundamental— con intensidades distintas, y esa mezcla es lo que el oído reconoce como
«violín» o «clarinete».

Las tres opciones falsas de esa pregunta se descartan por el propio enunciado, que ya dice «aunque
tengan **la misma frecuencia**»: **tono y frecuencia son la misma cosa** —una es la cualidad
percibida y la otra la magnitud medida— y por tanto ninguna de las dos puede distinguirlos; y la
**intensidad** los distinguiría por volumen, no por «matiz sonoro».

---

## 2. El rango audible y lo que queda fuera

**El oído humano medio percibe de 20 Hz a 20.000 Hz**, y las dos fronteras tienen nombre:

| Franja | Frecuencia | Nombre |
|---|---|---|
| Por debajo | **Menos de 20 Hz** | **Infrasonido** |
| Audible | **20 Hz – 20.000 Hz** | Sonido |
| Por encima | **Más de 20.000 Hz** | **Ultrasonido** |

**Un ultrasonido tiene una frecuencia superior a 20.000 Hz**, y ésa es la respuesta oficial a la
pregunta 17. Las tres opciones falsas —2.000, 12.000 y 500 Hz— **están todas dentro del rango
audible**, y de hecho las dos primeras están en la zona donde el oído es más sensible.

**El límite superior real baja con la edad**, y conviene tenerlo escrito: a partir de los cuarenta
años es raro oír por encima de 15.000 Hz. Pero **la cifra de referencia del sistema es 20.000 Hz**, y
de ella salen dos consecuencias técnicas del tema 5: que la frecuencia de muestreo del audio digital
sea de **44,1 o 48 kHz** —el doble del límite audible, más un margen— y que los códecs con pérdidas
empiecen por tirar lo que está por encima.

---

## 3. Cómo se mide el sonido

**Hay que distinguir tres aparatos que miden tres cosas distintas**, porque el examen los pone juntos
como opciones:

| Aparato | Qué mide | Unidad | Dónde se usa |
|---|---|---|---|
| **Sonómetro** | **El nivel de presión sonora del aire**, es decir, cuánto suena en un sitio | dB, normalmente ponderados en A (dBA) | **Prevención de riesgos, acústica de sala, control de niveles en directo** |
| **Dosímetro** | La **dosis acumulada** de ruido que recibe una persona a lo largo de una jornada | dBA integrados en el tiempo | Prevención de riesgos laborales, medida individual |
| **Vúmetro** | **El nivel de la señal eléctrica**, con una respuesta lenta que imita al oído | VU o dB | Mesas de mezcla, magnetófonos |
| **Picómetro** (*peak meter*) | El nivel de la señal eléctrica, con respuesta **instantánea** | dB de pico | Grabación digital, donde el pico satura |

**El nivel de presión sonora se mide con un sonómetro.** Ésa es la respuesta oficial a la pregunta 48
y la clave está en la palabra *presión*: **la presión es del aire, no de un cable**. El vúmetro y el
picómetro miden señal eléctrica; el dosímetro mide presión, pero **acumulada en el tiempo y sobre una
persona**, que es otra pregunta.

**La distinción entre sonómetro y dosímetro es la que separa dos medidas de la prevención de riesgos
laborales**, y por eso vuelve en el tema 21, que es el punto de prevención de esta ocupación: **el
sonómetro dice cuánto suena ahora; el dosímetro dice cuánto ha recibido esta persona hoy**.

---

## 4. El tono de referencia

**Antes de grabar o de emitir, toda la cadena se alinea con un tono.** Es una señal senoidal —
normalmente de 1.000 Hz— generada eléctricamente a un nivel conocido, y se manda de punta a punta del
sistema para que **cada etapa lo lea igual**.

**El tono a nivel cero es un tono generado eléctricamente a un nivel de referencia, utilizado para
ajustar los equipos.** Ésa es la respuesta oficial a la pregunta 97 y es la definición.

**Y hay que decir algo de la opción d), porque es verdad y no es la respuesta.** Dice: «tono que se
envía a través de todo el sistema y debe producir una lectura normalizada en los medidores de cada
etapa». **Eso es exactamente lo que se hace con el tono**, y describirlo así no es falso. Lo que
ocurre es que **describe su uso, no su naturaleza**: la pregunta es «qué es», y lo que es viene dado
por la opción b). En una pregunta de definición, **la opción que dice para qué sirve no es la
definición**, por cierta que sea.

Las otras dos opciones sí son falsas de plano: «una señal que no contiene frecuencia» no existe
—todo sonido tiene frecuencia—, y «una señal que contiene una frecuencia de audio» es tan general
que describe cualquier sonido.

---

## 5. Los micrófonos

**Dos clasificaciones a la vez: por cómo transforman el sonido y por qué dirección recogen.**

**Por el transductor:**

| Tipo | Cómo funciona | Necesita alimentación | Carácter |
|---|---|---|---|
| **Dinámico** o de bobina móvil | Una bobina unida a la membrana se mueve en un campo magnético y genera corriente | **No** | Robusto, aguanta niveles altos, menos detalle |
| **De condensador** (o **electrostático**) | La membrana y una placa fija forman un condensador cuya capacidad varía | **Sí**: alimentación fantasma o pila | Sensible, detallado; el de estudio |
| **De cinta** | Una lámina metálica muy fina en un campo magnético | No, salvo los activos | Muy suave, delicado |
| **Electret** | Condensador con carga permanente | Sí, pero le basta poca tensión | Pequeño; el de corbata y el de teléfono |

**Por el patrón polar:**

| Patrón | De dónde recoge | Dónde se usa |
|---|---|---|
| **Omnidireccional** | **De todas las direcciones por igual** | Ambientes, corbata, tomas binaurales |
| **Cardioide** | Sobre todo de delante | Voz, refuerzo en directo |
| **Supercardioide** e **hipercardioide** | De delante, con lóbulo más estrecho y algo por detrás | Directo con mucho ruido |
| **Cañón** (*shotgun*) | De un cono muy estrecho de delante | **Pértiga en rodaje y reportaje** |
| **Bidireccional** o de ocho | De delante y de detrás, no de los lados | Entrevista cara a cara, técnica M/S |

---

## 6. La alimentación fantasma

**La alimentación fantasma es una tensión continua —normalmente 48 voltios— que la mesa o la cámara
envía por el mismo cable de audio para alimentar el micrófono.** Se llama «fantasma» porque **viaja
por los dos conductores de señal a la vez**, de modo que un micrófono que no la necesita no la ve.

**La necesitan los micrófonos de condensador**, y ésa es la respuesta oficial a la pregunta 76 del
segundo cuadernillo: su cápsula **tiene que estar polarizada** para funcionar, y además llevan dentro
un preamplificador que hay que alimentar. **Los dinámicos no la necesitan** —generan su propia
corriente por inducción— y **los inalámbricos tampoco por el cable**, porque llevan pila.

**Y aquí hay que señalar un defecto de construcción de esa pregunta.** Entre sus cuatro opciones
están **«micrófonos de condensador»** y **«micrófonos electroestáticos»**, y **son la misma
familia con dos nombres**: un micrófono de condensador es, por definición, electrostático —su
principio de funcionamiento es la variación de capacidad entre dos placas cargadas—. **Dos opciones
que nombran lo mismo no pueden ser una la verdadera y la otra la falsa.**

La plantilla marca **«de condensador»**, que es el nombre corriente en castellano y el que usa el
oficio, y como respuesta es correcta. **No es una errata de plantilla** —la opción marcada es
verdadera— **pero sí un defecto de redacción del enunciado**, y el opositor que sepa la sinonimia
puede quedarse bloqueado ante dos opciones que le parecen igual de ciertas. **Lo que resuelve el
bloqueo es advertir que la pregunta busca el nombre de uso, no el nombre físico.**

---

## 7. Las técnicas de toma estereofónica

**Todas consisten en colocar dos o más micrófonos de manera que la diferencia entre lo que captan
reconstruya una escena espacial.** Las familias:

| Técnica | Cómo | Qué da |
|---|---|---|
| **Par coincidente** (X-Y) | Dos direccionales en el **mismo punto**, formando ángulo | Estéreo por diferencia de **intensidad**; compatible en mono |
| **M/S** (medio-lado) | Un cardioide de frente y un bidireccional cruzado | Estéreo con anchura ajustable después |
| **Par espaciado** (A-B) | Dos micrófonos **separados** | Estéreo por diferencia de **tiempo**; muy amplio |
| **ORTF** y **NOS** | Dos cardioides con ángulo y separación fijados | Estéreo natural para música y ambientes |
| **Estéreo binaural** | **Dos micrófonos omnidireccionales** colocados donde estarían los oídos, a menudo en una cabeza artificial | **La escena tal como la oiría una persona**; se escucha con auriculares |

**La técnica que usa dos micrófonos omnidireccionales y se emplea para realidad virtual es el estéreo
binaural**, y ésa es la respuesta oficial a la pregunta 73.

**Por qué la realidad virtual pide justamente ésa.** El binaural **conserva las claves con las que el
cerebro localiza**: la diferencia de tiempo entre los dos oídos, la diferencia de intensidad y, sobre
todo, **el filtrado que produce la cabeza y el pabellón auricular**. Al grabar con los micrófonos en
esa posición, esas claves quedan grabadas, y con auriculares el oyente vuelve a situar cada sonido
en su sitio, incluso arriba y detrás. **Ninguna otra técnica estéreo hace eso**, porque ninguna otra
mete la cabeza en medio.

Las tres opciones falsas: el **par coincidente** es la técnica X-Y, real pero de micrófonos
direccionales en un punto, y no reconstruye el espacio alrededor; y «bin estéreo» y «din estéreo» no
son nombres de ninguna técnica —el segundo se parece a la norma **DIN**, que sí da nombre a una
disposición de par casi coincidente, pero no se llama así—.

---

## 8. Los planos de sonido

**Igual que hay planos de imagen, hay planos de sonido**, y la correspondencia entre unos y otros es
lo que hace creíble una escena:

| Plano de sonido | Cómo suena | A qué plano de imagen acompaña |
|---|---|---|
| **Primer plano** | Cercano, seco, con presencia y detalle | Primer plano y plano medio |
| **Plano medio** | Con algo de sala, voz aún clara | Plano medio y americano |
| **Plano general** | Lejano, con reverberación del espacio | Plano general |
| **Plano de fondo** | Apenas inteligible, mezclado con el ambiente | Cualquiera, como capa |

**El principio es el de la coherencia**: un primer plano de imagen con sonido lejano suena falso, y
un plano general con la voz pegada al oído también, salvo que se busque el efecto. **Lo que se cambia
para pasar de un plano a otro es la distancia del micrófono y la proporción de sonido reverberado**,
no el volumen: subir el fader no acerca, sólo hace más fuerte lo lejano.

---

## 9. La ecualización

**Ecualizar es subir o bajar el nivel de unas bandas de frecuencia respecto de otras.** El reparto
grosso modo del espectro de una voz:

| Banda | Frecuencias | Qué aporta |
|---|---|---|
| **Graves** | 20 – 250 Hz | **Cuerpo y calidez**; en exceso, retumbe |
| **Medios bajos** | 250 – 800 Hz | Cuerpo; en exceso, sonido «encajonado» |
| **Medios** | 800 Hz – 4 kHz | **Inteligibilidad y presencia**; el oído es más sensible aquí |
| **Agudos** | 4 – 12 kHz | Definición, aire, siseo de las eses |
| **Muy agudos** | 12 – 20 kHz | Brillo, aire |

**Para que una voz en off suene más cálida y presente hay que aumentar ligeramente las frecuencias
medias y bajas y atenuar un poco las altas.** Ésa es la respuesta oficial a la pregunta 23, y las dos
palabras del enunciado piden dos cosas distintas que la opción resuelve a la vez: **«cálida» son las
bajas** —el cuerpo de la voz— y **«presente» son las medias** —la inteligibilidad—; atenuar las altas
quita el siseo y el filo.

Las tres opciones falsas hacen lo contrario o hacen otra cosa: **cortar las medias** es exactamente
quitar presencia; **aumentar agudas y atenuar graves** es la receta de una voz fría y delgada; y
**una reverberación muy corta** no es ecualización, es un efecto de espacio, y además aleja en lugar
de acercar.

---

## 10. Las capas de la banda sonora

**Una banda sonora terminada tiene cuatro capas**, y cada una se graba, se busca o se fabrica de una
manera distinta:

| Capa | Qué es | De dónde sale |
|---|---|---|
| **Diálogo** | Voces de los personajes, entrevistas, voz en off | Rodaje, o sala de doblaje |
| **Ambientes** | El sonido del lugar: calle, sala, campo | Toma de ambiente en rodaje, o archivo |
| **Efectos** | Los ruidos de la acción | **Archivo** o **sala de Foley** |
| **Música** | Sintonía, ráfagas, fondos | Composición o biblioteca |

**La ambientación sonora es la que se compone con efectos, ráfagas y fondos musicales.** Ésa es la
respuesta oficial a la pregunta 2, y es una definición de oficio: **ambientar es vestir la imagen con
todo lo que no es la voz**. Las tres opciones falsas nombran cosas concretas y más estrechas: la
**sintonía** es una pieza musical, una sola; los **efectos de vídeo** son de imagen; y la
**posproducción sonora** es la fase entera en la que la ambientación se hace, no la ambientación.

**Y ahora la distinción que el examen pregunta con la palabra *Foley*.** Se llama así por Jack Foley,
que la puso en práctica, y designa **los efectos que se graban en sala, en sincronía con la imagen,
imitando lo que se ve**: pasos, roces de ropa, una puerta, un vaso que se posa.

**Un sonido Foley es un sonido que tiene correspondencia visual con la imagen.** Ésa es la respuesta
oficial a la pregunta 54, y es lo que lo distingue de sus tres vecinos:

- **El sonido de archivo** viene de una biblioteca; puede tener correspondencia visual o no, pero no
  se ha grabado para esa imagen.
- **El sonido sin correspondencia visual** es el **sonido fuera de campo**, otra categoría.
- **El sonido del doblador** es diálogo, no efecto.

**Lo que define el Foley no es que lo haga una persona: es que se graba mirando la imagen y encaja
con lo que se ve.**

---

## 11. La pista internacional

**Cuando un programa se vende fuera, hay que poder cambiarle el idioma sin rehacer el sonido.** Para
eso se entrega, junto al programa, una **pista internacional** —también llamada **soporte
internacional** o **M&E**, de música y efectos— que **contiene todo el sonido menos la voz que hay
que traducir**.

Qué lleva y qué no:

| Lleva | No lleva |
|---|---|
| **La música** | **La voz en off**, que se vuelve a grabar en el idioma de destino |
| **Los ambientes** | El diálogo doblado |
| **Los efectos y el Foley** | |
| **Los totales de los entrevistados**, en su idioma original | |

**En un documental para vender en el extranjero, la pista internacional lleva músicas, ambientes y
los totales de los entrevistados.** Ésa es la respuesta oficial a la pregunta 3 del segundo
cuadernillo, y la razón de que los **totales** —las declaraciones grabadas de los entrevistados— sí
vayan es que **no se doblan: se subtitulan o se locutan por encima**, dejando oír debajo la voz
original. La voz en off del narrador, en cambio, **se sustituye entera**, y por eso es lo único que
la pista no puede llevar.

Las tres opciones falsas se explican por ahí: «todos» haría imposible cambiar el idioma; «músicas,
ambientes y off» **mete justamente lo que hay que quitar**; y «ambientes y traducciones» quita la
música, que sí va, y mete traducciones, que son del comprador.

---

## 12. El sonido en directo: el retorno N-1

**Cuando alguien participa en un programa desde fuera del estudio, hay que devolverle el sonido del
programa para que oiga a los demás.** Y hay un problema: **si se le devuelve también su propia voz,
la oirá con el retardo del enlace y no podrá hablar.** Ese eco de sí mismo es el fallo más común de
una conexión en directo.

**La solución es la señal N-1: la mezcla del programa menos la señal de la fuente a la que se envía.**
Ésa es la respuesta oficial a la pregunta 33 del segundo cuadernillo, y el nombre lo dice: de las *N*
fuentes de la mezcla se le mandan *N* menos una, la suya.

**Cada envío tiene su propia N-1**, porque cada uno tiene que perder una señal distinta. En una mesa
de directo con cuatro conexiones exteriores hay cuatro N-1 distintas, y en una unidad móvil son
justamente estos envíos los que más tiempo llevan de comprobar.

Las tres opciones falsas describen otros envíos reales de un control y por eso engañan: quitar «las
órdenes del realizador» es lo que hace el circuito de **intercom**, que va por otro camino; quitar
«los monitores de audio del estudio» es la manera de evitar el acople del plató, que es otro
problema; y la cuarta mezcla las dos cosas.

---

## 13. El sonido de un concierto: el backline

**En una actuación musical hay dos mundos de sonido que no se tocan:**

| | **Sistema de refuerzo** (*P.A.*) | **Backline** |
|---|---|---|
| Qué es | Los altavoces que llevan el sonido al público | **El conjunto de instrumentos y amplificadores que acompañan al grupo en el escenario** |
| Dónde está | **Delante del escenario**, hacia el público | **En el escenario**, con los músicos |
| De quién es | De la producción del recinto | Del grupo, o alquilado para él |
| Qué hace en televisión | No se graba: se toma de la mesa | Se microfona, y sale en imagen |

**El backline es el conjunto de instrumentos y amplificadores que acompañan al grupo musical en el
escenario.** Ésa es la respuesta oficial a la pregunta 6, y las tres opciones falsas describen cosas
del recinto que se llaman de otro modo: la zona de espera antes de salir es el ***backstage***; el
equipo de amplificación hacia el público es el **P.A.** o sistema de refuerzo; y la zona reservada
para los músicos y sus acompañantes es el **camerino** o la zona de invitados.

**Y por qué le importa a la realización**: el *backline* **está en imagen**. Su colocación es a la
vez una decisión de sonido y de escenografía, y de ella depende que las cámaras tengan tiro limpio a
cada músico.

---

## 14. Formatos y códecs de audio

**Hay que separar tres cosas que se llaman igual en la conversación:**

- **El contenedor** es el fichero: qué pistas hay y cómo se ordenan.
- **El códec** es la manera de escribir las muestras.
- **La compresión** puede ser **ninguna**, **sin pérdidas** o **con pérdidas**.

| Formato | Qué es | Compresión |
|---|---|---|
| **WAV** | Contenedor de Microsoft e IBM, normalmente con muestras **PCM** | **Ninguna** |
| **AIFF** | Contenedor de Apple, también con muestras PCM | **Ninguna** |
| **FLAC** y **ALAC** | Códecs de audio | **Sin pérdidas**: se reduce el tamaño y se recupera el original exacto |
| **MPEG-1 capa III** (*MP3*), **AAC**, **MPEG** en general | Códecs | **Con pérdidas** |
| **Dolby Digital** (AC-3) | Códec de emisión multicanal | Con pérdidas |

**El formato de audio que no lleva compresión es el WAV**, y ésa es la respuesta oficial a la
pregunta 84 del segundo cuadernillo.

**Con dos precisiones que este tema debe hacer, porque la pregunta las necesita.**

**La primera es sobre la opción c), que está escrita «AIFFK».** El formato existente se llama
**AIFF**, sin la ka final, y **también es sin compresión**: si estuviera bien escrito, la pregunta
tendría dos respuestas verdaderas. **Escrito con la ka, no nombra ningún formato**, y por eso la
pregunta se sostiene. Es una errata del cuadernillo que, por casualidad, salva el enunciado en lugar
de romperlo; queda anotada como tal.

**La segunda es de vocabulario.** El enunciado pregunta por un «códec de audio» y **WAV no es un
códec: es un contenedor** —lo que va dentro suele ser PCM, que sí es la codificación—. La respuesta
oficial es la correcta de las cuatro y el uso corriente llama «formato» a las dos cosas, así que la
pregunta se responde sin dificultad; pero **la palabra exacta es contenedor**, y el opositor que la
sepa no debe dudar por eso.

Y la opción d), **AVC**, es de otra materia: **es un códec de vídeo**, el H.264 del tema 5.

---

## 15. Los datos que el examen ha preguntado

| Nº | Cuadernillo | Qué pregunta | Oficial |
|---|---|---|---|
| 2 | primero | Qué componen efectos, ráfagas y fondos musicales | a) La ambientación sonora ✔ |
| 6 | primero | Qué es el *backline* | d) Instrumentos y amplificadores en el escenario ✔ |
| 17 | primero | Frecuencia a partir de la cual hay ultrasonido | b) 20.000 Hz ✔ |
| 23 | primero | Ecualización para una voz en off cálida y presente | c) Subir medias y bajas, atenuar altas ✔ |
| 48 | primero | Aparato que mide el nivel de presión sonora | c) Sonómetro ✔ |
| 54 | primero | Qué es un sonido Foley | b) Sonido con correspondencia visual con la imagen ✔ |
| 66 | primero | Cualidad que distingue dos instrumentos en la misma nota | a) Timbre ✔ |
| 73 | primero | Técnica con dos omnidireccionales para realidad virtual | d) Estéreo binaural ✔ |
| 97 | primero | Qué es el tono a nivel cero | b) Tono a un nivel de referencia para ajustar equipos ✔ |
| 3 | segundo | Qué lleva la pista de sonido internacional | b) Músicas, ambientes y los totales ✔ |
| 33 | segundo | Qué es la señal N-1 | b) El programa menos la señal de la fuente del envío ✔ |
| 76 | segundo | Para qué micrófonos hace falta la alimentación fantasma | a) De condensador ✔ **·** con sinónimo entre las opciones |
| 84 | segundo | Qué formato de audio no tiene compresión | b) WAV ✔ **·** con errata en otra opción |

**Las trece respuestas oficiales son correctas.** Ninguna es errata de plantilla. Pero **tres llevan
anotación**, y las tres por defectos de construcción del enunciado, no de la respuesta:

1. **La 76** ofrece «de condensador» y «electroestáticos», que son **la misma familia de micrófonos
   con dos nombres**. La plantilla marca el nombre de uso, y acierta.
2. **La 84** escribe «AIFFK» donde el formato se llama **AIFF**. **La errata es la que salva la
   pregunta**: bien escrito, ese formato tampoco lleva compresión y habría dos respuestas
   verdaderas. Y el enunciado llama «códec» a lo que es un **contenedor**.
3. **La 97** tiene una opción —la d)— que **describe correctamente el uso del tono de referencia**.
   No es la respuesta porque la pregunta es de definición, y la definición es la b).

**Y una observación de reparto**: el sonido tiene nueve preguntas en el primer llamamiento y cuatro
en el segundo, con **cero solapamiento**: no repite ni una. Es el punto del programa que más renueva
su banco de un llamamiento a otro.

---

## 16. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es acústica elemental, técnica de sonido y práctica
de estudio y directo, y va como oficio: las cualidades del sonido, el rango audible, la tabla de
aparatos de medida, el tono de referencia, las dos clasificaciones de micrófonos, la alimentación
fantasma, las técnicas de toma estereofónica, los planos de sonido, el reparto del espectro para
ecualizar, las cuatro capas de la banda sonora, la pista internacional, el retorno N-1, la separación
entre refuerzo y *backline* y la tabla de formatos.

**Tres apoyos que vienen de otros temas de este mismo libro y quedan enlazados:**

- **La frecuencia de muestreo del audio digital** —44,1 y 48 kHz— se explica por el límite de
  20.000 Hz de este tema y por el proceso de digitalización del **tema 5**.
- **La distinción entre sonómetro y dosímetro** es la que el **tema 21** necesita para el punto de
  prevención de esta ocupación, que es el único del proyecto que añade la exposición a altos niveles
  de sonido.
- **El AVC de la pregunta 84 es el H.264 del tema 5**, y aparece aquí como opción falsa precisamente
  porque es un códec de vídeo.

**Y una precisión sobre las bandas de frecuencia de la tabla del epígrafe 9: son orientativas y así
van declaradas.** No hay una frontera exacta entre «medios» y «agudos», y cada escuela de sonido
corta el espectro donde le conviene. Lo que la tabla sostiene sin margen de duda —y lo que la
pregunta 23 exige— es **qué aporta cada zona**: las bajas dan cuerpo, las medias dan presencia y las
altas dan filo.
