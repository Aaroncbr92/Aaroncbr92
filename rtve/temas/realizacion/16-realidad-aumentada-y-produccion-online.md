# Tema 16 del específico de Realización (Asistencia) · Realidad aumentada, decorados virtuales y producción online

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Realización (Asistencia) · puntos 5.8 y 5.9 |
| **Sirve para** | **Realización (Asistencia)** |
| **Fuente** | **Documentación de fabricante**: ficha del **Mo-Sys StarTracker Max** |
| **Identificador** | Documentación de fabricante, leída el **02/09/2026** |
| **Redacción que se estudia** | La ficha, **en la fecha en que se leyó** |
| **Aviso sobre las fuentes** | **Aquí está la errata de plantilla de este libro**: la opción marcada en la pregunta del sistema free-d describe un montaje de croma y no una sensorización. La correcta es la a) |
| **Extensión** | **4.131 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la realidad aumentada (**RA**, escrita **R.A.** en
el examen) y la realidad virtual (**RV**, *VR* en inglés); los efectos visuales (**VFX**, del inglés
*visual effects*) y las imágenes generadas por ordenador (**CGI**, del inglés *computer-generated
imagery*); el fotograma (**fr**, del inglés *frame*) y el milisegundo (**ms**); el diodo emisor de
luz (**LED**); la televisión digital (**DTV**); la conmutación en el mismo plano (**IPS**, del inglés
*in-plane switching*), que es un tipo de panel de pantalla; el protocolo de internet (**IP**); y el
identificador **free-d**, que en este tema se escribe con minúscula porque así lo escribe el examen.

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización (Asistencia),
> puntos 5.8 y 5.9): «5.8. Realidad aumentada y decorados virtuales. 5.9. Sistemas de producción y
> transmisión online. Narración transmedia y sistemas de vídeo conferencia.»

**Nueve preguntas**, repartidas casi por igual entre los dos subpuntos: cuatro sobre plató virtual y
realidad aumentada, cinco sobre lo que se distribuye por la red.

**Y este tema contiene el hallazgo más serio del libro**: una respuesta oficial que, contrastada con
la documentación de fabricante disponible, **no describe lo que la pregunta pregunta**. Está en el
epígrafe 3 y se declara como tal.

<!-- indice -->

## Índice

- [1. Decorado virtual, realidad aumentada y producción virtual](#1-decorado-virtual-realidad-aumentada-y-producción-virtual)
- [2. La iluminación de un plató de croma](#2-la-iluminación-de-un-plató-de-croma)
- [3. El seguimiento de cámara y el sistema free-d](#3-el-seguimiento-de-cámara-y-el-sistema-free-d)
  - [El hallazgo: la pregunta 46 del primer cuadernillo](#el-hallazgo-la-pregunta-46-del-primer-cuadernillo)
- [4. El motor de representación en tiempo real](#4-el-motor-de-representación-en-tiempo-real)
- [5. El retardo, y la aritmética que hay que saber hacer](#5-el-retardo-y-la-aritmética-que-hay-que-saber-hacer)
- [6. Efectos visuales: el *plate*](#6-efectos-visuales-el-plate)
- [7. El vídeo de 360 grados](#7-el-vídeo-de-360-grados)
- [8. El *streaming*](#8-el-streaming)
- [9. La videoconferencia](#9-la-videoconferencia)
- [10. Los datos que el examen ha preguntado](#10-los-datos-que-el-examen-ha-preguntado)
- [11. Trazabilidad](#11-trazabilidad)

<!-- /indice -->

## 1. Decorado virtual, realidad aumentada y producción virtual

**Tres cosas que se confunden y que son distintas por dónde está lo real y dónde lo sintético:**

| Técnica | Qué es real | Qué es sintético | Cómo se junta |
|---|---|---|---|
| **Decorado virtual** (plató virtual) | **Sólo las personas y los objetos que tocan** | **Todo el fondo** | El fondo se sustituye por incrustación de crominancia |
| **Realidad aumentada** | **El plató entero**, con su decorado construido | **Los objetos añadidos**, que aparecen encima | Los objetos se superponen sobre la imagen real, con llave |
| **Producción virtual en pared de LED** | Las personas y el decorado próximo | El fondo, **pero se muestra en pantallas reales del plató** | **No hay incrustación**: la cámara filma la pantalla |

**Las tres necesitan lo mismo para funcionar: saber en todo momento dónde está la cámara.** Si la
cámara se mueve y el fondo sintético no se mueve con ella —con la misma perspectiva, el mismo
encuadre y el mismo enfoque—, el truco se cae. **De ahí el epígrafe 3.**

**Y las tres tienen el mismo problema de tiempo:** generar la imagen sintética lleva unos cuantos
fotogramas, y eso desincroniza. **De ahí el epígrafe 5.**

---

## 2. La iluminación de un plató de croma

**En un decorado virtual hay dos iluminaciones que resolver a la vez, y la tentación es olvidar una
de las dos.**

| Qué se ilumina | Cómo | Para qué |
|---|---|---|
| **El personaje** | **Como si estuviera en el decorado virtual**: con la dirección, la dureza y la temperatura de color que tendría allí | Para que **no desentone** con el fondo que se le va a poner |
| **El fondo de croma** | **Uniformemente**, sin sombras, sin manchas y sin caídas hacia los bordes | Para que la incrustación tenga **un solo color que declarar transparente** |

**Para obtener una incrustación realista y sin problemas hay que iluminar al personaje para que no
desentone con el decorado virtual y, además, iluminar el fondo uniformemente.** Ésa es la respuesta
oficial a la pregunta 37 del segundo cuadernillo, y **la palabra que decide es *además***: son dos
trabajos, no uno.

Las tres opciones falsas se equivocan cada una en un sitio:

- «**No es necesario iluminar el fondo porque será sustituido**» es el error más común y el más
  costoso. **El fondo se sustituye precisamente por su color**, y si el color no es uniforme el
  recorte no lo es tampoco: aparecen jirones, bordes verdes y zonas que no se van.
- «**La iluminación no es importante ya que el decorado es virtual**» dice lo mismo llevado al
  extremo.
- «**Lo pegamos al fondo para que se recorte mejor**» hace justamente lo contrario de lo que hay que
  hacer: **cuanto más cerca está el personaje del croma, más rebote verde recibe** —el llamado
  *spill*— y peor sale el recorte. **La regla es separar**, no pegar: al menos dos o tres metros, si
  el plató da para ello.

**Y el vínculo con el tema 7**: separar al personaje del fondo es también lo que permite **desenfocar
el croma**, con lo que se evitan de paso las arrugas de la tela y las juntas de los paneles.

---

## 3. El seguimiento de cámara y el sistema free-d

**Para que un decorado virtual funcione hay que medir la cámara en seis grados de libertad** —tres de
posición y tres de orientación— **más el zum y el foco**, y entregar esos datos al motor que dibuja
el fondo, fotograma a fotograma y en tiempo real.

Las familias de sistemas que lo hacen:

| Familia | Cómo mide | Rasgos |
|---|---|---|
| **Mecánica, por codificadores** | Sensores en la cabeza, el pedestal y la grúa | Muy precisa, pero **la cámara no puede salirse del soporte instrumentado** |
| **Óptica por marcas de referencia** | **Una cámara auxiliar apuntando al techo lee marcas retrorreflectantes** y calcula la posición | **Cámara libre por el plató**; es la familia dominante hoy |
| **Óptica sin marcas** | Reconocimiento del propio entorno | No hace falta preparar el techo; menos robusta |
| **Por ultrasonidos o radiofrecuencia** | Emisores y receptores repartidos por el plató | Menos precisa; poco usada en televisión |
| **Inercial** | Acelerómetros y giróscopos en la cámara | Deriva con el tiempo; se usa combinada |

**La documentación de fabricante que este proyecto tiene guardada describe la segunda familia y
nombra el free-d.** La ficha del **Mo-Sys StarTracker Max** dice de su configuración de seguimiento:

> Tracking Stars Configuration / Ceiling, wall or floor mounted retro-reflective stickers or digital
> LED wall markers

y de su salida de datos:

> Data Output / Mo-Sys F4 / FreeD / OpenTrackIO over IP

y describe el origen del producto así:

> Mo-Sys invented 'simple-to-use' marker-based optical camera tracking for Virtual Production.

**Es decir, y esto es lo que hay que retener: el seguimiento se hace leyendo pequeñas marcas
retrorreflectantes colocadas en el techo, y *FreeD* es uno de los formatos en que esos datos se
entregan al motor.** El nombre viene del sistema óptico de marcas del que salió, y hoy designa sobre
todo **el protocolo de datos de seguimiento** que casi todos los fabricantes admiten.

### El hallazgo: la pregunta 46 del primer cuadernillo

**El enunciado pregunta**: «En un sistema de escenografía virtual, ¿qué tipo de sensorización
corresponde al sistema free-d?» **Y sus cuatro opciones son:**

| Opción | Qué dice | Qué describe en realidad |
|---|---|---|
| **a)** | «Sistema de trabajo con croma que además incorpora sensores que permite establecer la posición de la cámara **mediante la lectura de pequeñas marcas de referencia**» | **El seguimiento óptico por marcas**, que es exactamente lo que el free-d nombra |
| b) | «Sistema que consta de una serie de elementos de croma que sirve de ajuste tanto en las paredes como en el suelo» | **El croma**, es decir, el fondo. No es sensorización |
| **c) · marcada** | «Sistema que dispone de unos **postes de croma colocados en el techo**, fuera de plano, para favorecer el movimiento escénico y evita la inclusión de sombras» | **Un montaje de croma**. Tampoco es sensorización |
| d) | «Sistema mediante el empleo de **ultrasonidos** que puede establecer la posición de la cámara» | **El seguimiento por ultrasonidos**, que existe y **no** es el free-d |

**La plantilla marca la c), y la c) no describe ninguna sensorización.** Describe un montaje de
croma: unos postes de tela verde colgados del techo. **Eso no mide la posición de la cámara**, que es
lo que el enunciado pregunta.

**La opción a) sí la describe, y coincide palabra por palabra con lo que el fabricante documenta**:
sensores que establecen la posición de la cámara **leyendo pequeñas marcas de referencia**. Las
«marcas de referencia» de la opción son las *retro-reflective stickers* de la ficha del StarTracker
Max, y ése es el único de los cuatro montajes de la lista que produce datos de seguimiento —los que
se entregan, entre otros formatos, **en free-d**—.

**Se declara, por tanto, errata de plantilla: la respuesta correcta es la a).** Es la **novena errata
de plantilla** documentada por este proyecto y **la primera de materia técnica audiovisual**; las
ocho anteriores eran de derecho y de contabilidad.

**Y se declara también el límite de esta afirmación**, como exige el apartado 5 del manual —*el que
detecta se equivoca*—: la comprobación se apoya en la **documentación de un fabricante que usa el
free-d como formato de salida**, no en una especificación del propio free-d, que **no se ha podido
consultar**. Lo que esa documentación demuestra sin margen de duda es **que el free-d pertenece al
mundo del seguimiento óptico por marcas** y no al del montaje del croma. **Sobre esa base, la opción
c) es insostenible: no describe una sensorización de ninguna clase.**

**Para el opositor, la consecuencia práctica es la de siempre con una errata**: hay que saber cuál es
la respuesta buena **y cuál es la que el tribunal dio por buena**, porque en una impugnación sirve la
primera y en una plantilla de corrección manda la segunda.

---

## 4. El motor de representación en tiempo real

**Un motor de representación en tiempo real es el programa que dibuja el decorado sintético tantas
veces por segundo como fotogramas tenga la señal.** Es la pieza que hizo posible que el decorado
virtual dejara de parecerlo.

**Unreal Engine es un motor de representación en tiempo real para aplicaciones de televisión, cine y
videojuegos.** Ésa es la respuesta oficial a la pregunta 98 del primer cuadernillo, y las tres
opciones falsas confunden el motor con lo que hace, con dónde se usa o con otro programa:

- «**Un decorado virtual**» es **el resultado**, no la herramienta.
- «**Un estudio de televisión para hacer realidad virtual**» es **el sitio**.
- «**Una función de posproducción de After Effects**» es otro programa distinto, del tema 15, y que
  además no trabaja en tiempo real.

**Y su relación con el epígrafe 3**: el motor **necesita** los datos de seguimiento para saber desde
dónde dibujar. La ficha del StarTracker Max lo dice al describir su salida:

> delivering low latency camera tracking data over IP (Mo-Sys F4, FreeD, OpenTrackIO) into real-time
> render engines such as Unreal Engine

**Seguimiento y motor son las dos mitades del mismo sistema**, y el examen pregunta por las dos.

---

## 5. El retardo, y la aritmética que hay que saber hacer

**La pregunta 34 del primer cuadernillo es la mejor del examen y hay que resolverla despacio.**

**El planteamiento**: un plató en el que **dos cámaras tienen realidad aumentada** a través de un
programa que **genera un retardo de 2 fotogramas**. Hay **otras cinco cámaras sin realidad
aumentada**. Se pregunta qué hacer para mezclar las siete sin que haya problemas de sincronización
entre audio y vídeo. **Y el enunciado añade la frase que lo decide todo**: «Ten en cuenta que haremos
transiciones entre una cámara con R.A. y **la misma cámara sin R.A.**»

**La respuesta oficial: poner un retardo de 2 fotogramas en cada una de las entradas al mezclador de
las siete cámaras, e informar a sonido para que retarde 80 milisegundos todas las fuentes de sonido
del plató.**

**Por qué las siete y no las cinco, que es la opción falsa más tentadora.**

La frase del enunciado dice que **una misma cámara entra al mezclador dos veces**: una vez tal cual y
otra vez pasada por el programa de realidad aumentada. Así que las entradas del mezclador no son
siete, son **nueve**:

| Entrada | De dónde viene | Retardo que trae |
|---|---|---|
| Cámaras 1 a 7, señal directa | De la cámara al mezclador | **0** |
| Cámaras 1 y 2, señal con realidad aumentada | De la cámara al programa de RA y de ahí al mezclador | **2 fotogramas** |

**Para que todo case, las siete señales directas necesitan los 2 fotogramas que las dos aumentadas ya
traen.** Y eso incluye **las señales directas de las dos cámaras que tienen realidad aumentada**,
porque es entre esas dos versiones —la aumentada y la directa de la misma cámara— entre las que se va
a transicionar.

**La opción d) retrasa sólo las cinco cámaras sin realidad aumentada**, y es la que casi acierta:
deja sin retrasar las señales directas de las cámaras 1 y 2, **que son justamente las que el
enunciado dice que se van a mezclar con sus propias versiones aumentadas**. Al cortar entre ellas
habría un salto de 2 fotogramas. **La frase final del enunciado está puesta ahí para descartar esta
opción**, y quien no la lea se la lleva.

**Y ahora la aritmética del sonido, que es la otra mitad de la respuesta.**

**A 25 fotogramas por segundo, un fotograma dura 40 milisegundos**, porque 1.000 ÷ 25 = 40. Por tanto:

| Fotogramas | Milisegundos a 25 fps |
|---|---|
| 1 | 40 |
| **2** | **80** |
| 3 | 120 |
| 4 | 160 |

**Dos fotogramas son 80 milisegundos**, y por eso la respuesta correcta dice 80 y **la opción c) —que
por lo demás es idéntica a la correcta— dice 160 y es falsa**. Ciento sesenta milisegundos serían
cuatro fotogramas.

**La opción b) —«no se puede mezclar entre las cámaras con R.A. y ellas mismas sin R.A.»— es la
respuesta de quien no sabe que el retardo se compensa.** Sí se puede, y así es como se hace.

**La regla, que es la misma del tema 15 y conviene enunciarla una vez para las dos**: en televisión,
**todo lo que llega antes se retrasa hasta el más lento**, y el sonido se retrasa con él. Nunca se
adelanta nada.

---

## 6. Efectos visuales: el *plate*

**Un *plate* es el plano grabado que sirve de fondo o de punto de partida para integrar efectos
visuales.** Ésa es la respuesta oficial a la pregunta 73 del segundo cuadernillo.

**Es la imagen real sobre la que se monta todo lo demás**: el paisaje al que se le añadirá una nave,
la calle sobre la que se pondrá un edificio, el fondo que se verá tras un actor rodado en croma. En
un rodaje con efectos, **la unidad de *plates* graba esos fondos aparte**, muchas veces en otro
momento y en otro sitio, anotando con precisión la posición y la óptica para que después encajen.

Las tres opciones falsas son términos reales de otras partes del proceso: la creación del esqueleto
de un personaje sintético es el ***rigging***; la cámara dedicada a la captura de movimiento es
material de *motion capture*; y una técnica de mezcla de efectos sonoros no es de efectos visuales.

---

## 7. El vídeo de 360 grados

**Una imagen de 360 grados no se toma con una cámara: se toma con varias, y luego se cose.** Cada
objetivo cubre una porción de la esfera, las porciones se solapan por los bordes, y un programa
**busca las coincidencias en esas zonas de solape y las empalma** hasta formar una imagen continua.

**Ese proceso se llama *stitching*** —del inglés *stitch*, «puntada»—, y es la respuesta oficial a la
pregunta 78 del primer cuadernillo.

**Con una errata que hay que anotar: el cuadernillo escribe «Steaching».** No existe esa palabra: el
término es ***stitching***. La opción sigue siendo reconocible y sigue siendo la única de las cuatro
que nombra el proceso, así que **la pregunta se sostiene**; pero **la grafía está mal** y queda
constancia. Las otras tres opciones —«espacial», «*snapshots*» y «mapa circular»— no nombran nada de
esto: la segunda es una memoria del mezclador, del tema 10.

**Lo que el *stitching* tiene de difícil**, y que explica por qué es una operación y no un botón: las
cámaras no comparten centro óptico, así que los objetos cercanos se ven desde puntos distintos y **no
casan**; la exposición y el balance de blancos varían de un objetivo a otro y hay que igualarlos; y
la costura tiene que caer donde menos se note.

---

## 8. El *streaming*

**El *streaming* es la distribución de contenido multimedia de forma continua, de manera que el
usuario consume el producto al mismo tiempo que se descarga, sin necesidad de descargarlo
previamente.** Ésa es la respuesta oficial a la pregunta 48 del segundo cuadernillo, y su rasgo
definitorio es **la simultaneidad**: se ve mientras llega.

**Hay que distinguirlo de sus tres vecinos**, que son las tres opciones falsas:

| Modo | Cómo funciona | Se puede ver antes de terminar |
|---|---|---|
| **Descarga** | El fichero se descarga entero y luego se abre | **No** |
| **Descarga progresiva** | El fichero se descarga en orden y se puede empezar a ver antes de que acabe | **Sí, pero se descarga entero igual**, y no se puede adaptar a la red |
| **Transmisión por secuencias** (*streaming* propiamente dicho) | El contenido se trocea en segmentos que se piden y se consumen sobre la marcha | **Sí**, y **se adapta**: si la red baja, se pide un segmento de menos calidad |
| **Difusión digital** (DTV, TDT) | Se emite por ondas y se recibe con antena | Sí, pero **no es por red informática** |

**El tipo de *streaming* más adecuado para la distribución de transmisiones de audio y vídeo en
directo es la transmisión por secuencias.** Ésa es la respuesta oficial a la pregunta 44 del segundo
cuadernillo, y la razón está en la tabla: **la descarga progresiva no sirve para el directo**, porque
un directo no es un fichero terminado que se pueda ir descargando en orden —**lo que va a venir aún
no existe**—. La transmisión por secuencias, que trocea y sirve segmento a segmento, sí.

**Las otras dos opciones de esa pregunta no son modos de *streaming***: la **DTV** es televisión
digital difundida por ondas, y el **IPS** —*in-plane switching*— es **una tecnología de panel de
pantalla**, que no tiene nada que ver con la distribución. Es un distractor de otra materia.

---

## 9. La videoconferencia

**La videoconferencia entró en el temario porque entró en los programas**: la conexión con un
invitado por videollamada es hoy una fuente de contribución más, y su calidad es responsabilidad de
quien realiza.

**La pregunta 25 del segundo cuadernillo pregunta cuál es el mayor desafío para garantizar una
comunicación fluida y de alta calidad en una videoconferencia internacional con múltiples
participantes, y la respuesta oficial es la diversidad de dispositivos y sistemas operativos que usan
los participantes.**

**Es la correcta y merece explicarse, porque las otras tres son problemas reales:**

| Opción | Por qué no es «el mayor desafío» |
|---|---|
| «La elección de una plataforma popular y conocida» | Es **una decisión que se toma una vez** y que además se resuelve sola: se elige y ya está |
| «La calidad de la conexión del anfitrión» | Es **un solo punto** y se puede controlar: se contrata mejor línea, se conecta por cable |
| «La capacidad de compartir pantallas simultáneamente» | Es **una función**, no un desafío; y casi ninguna reunión la necesita |
| **«La diversidad de dispositivos y sistemas operativos»** | **Es lo único que no se controla**: cada participante trae su ordenador, su cámara, su micrófono, su versión y su red |

**El criterio que ordena las cuatro es quién controla qué.** Los tres primeros problemas están del
lado del organizador y tienen solución conocida. **El cuarto está del lado de los participantes, es
distinto en cada uno y no se puede uniformar.** De ahí que sea el mayor.

**Y la consecuencia de producción, que es lo que la ocupación tiene que saber hacer**: cuando una
videoconferencia va a salir en antena, **se prueba antes con cada participante, en su equipo y en su
sitio**, y se le dan instrucciones concretas —cable en lugar de radio, cámara a la altura de los
ojos, auriculares para evitar el acople—. La prueba no sobra: es la única manera de convertir un
problema que no se controla en uno que se conoce.

---

## 10. Los datos que el examen ha preguntado

| Nº | Cuadernillo | Qué pregunta | Oficial |
|---|---|---|---|
| 34 | primero | Cómo sincronizar siete cámaras con dos de realidad aumentada | a) Retardo de 2 fotogramas en las siete y 80 ms en sonido ✔ |
| 46 | primero | Qué sensorización corresponde al sistema free-d | c) **· errata de plantilla: la correcta es la a)** |
| 78 | primero | Cómo se llama el empalme de las imágenes de un 360º | b) *Stitching* ✔ **·** escrito «Steaching» |
| 98 | primero | Qué es Unreal Engine | b) Motor de representación en tiempo real ✔ |
| 25 | segundo | Mayor desafío de una videoconferencia internacional | d) La diversidad de dispositivos y sistemas ✔ |
| 37 | segundo | Cómo lograr una incrustación realista | c) Iluminar al personaje y el fondo uniformemente ✔ |
| 44 | segundo | *Streaming* más adecuado para el directo | b) Transmisión por secuencias ✔ |
| 48 | segundo | Qué es el *streaming* | c) Consumo simultáneo a la descarga ✔ |
| 73 | segundo | Qué es el *plate* en efectos visuales | a) El plano grabado que sirve de fondo ✔ |

**Ocho respuestas oficiales correctas y una errata de plantilla.**

**La errata es la 46**, y está razonada en el epígrafe 3: la opción marcada describe un montaje de
croma, no una sensorización; la a) describe el seguimiento óptico por marcas de referencia, que es a
lo que el free-d pertenece según la documentación del fabricante.

**Y una anotación de grafía en la 78**: el cuadernillo escribe «Steaching» donde el término es
*stitching*. No afecta a la respuesta.

**Un aviso de estudio sobre la 34.** Es la pregunta que más recompensa leer el enunciado entero: su
última frase —«haremos transiciones entre una cámara con R.A. y la misma cámara sin R.A.»— es la que
descarta la opción d), que por lo demás parece más razonable que la correcta. **Y su segunda mitad se
resuelve con una división: 1.000 entre 25 son 40 milisegundos por fotograma.**

---

## 11. Trazabilidad

**Una fuente de fabricante sostiene los epígrafes 3 y 4**, y es del cuarto nivel de la jerarquía de
fuentes (el informe de fuentes del bloque específico), citada con la fecha en que se leyó:

| Fichero | Qué sostiene | Leído |
|---|---|---|
| Ficha técnica del **Mo-Sys StarTracker Max** | Que el seguimiento óptico de cámara se hace con **marcas retrorreflectantes en techo, pared o suelo**; que **FreeD** es uno de los formatos en que esos datos se entregan; que Mo-Sys **inventó el seguimiento óptico por marcas** para producción virtual; y que esos datos alimentan **motores de representación en tiempo real como Unreal Engine** | 02/09/2026 |

**Sobre esa fuente descansa el hallazgo del epígrafe 3, y su límite se declara allí mismo**: la
especificación del propio protocolo free-d **no se ha podido consultar**, y lo que la ficha del
fabricante prueba es la familia a la que pertenece, no su articulado. **La conclusión —que la opción
marcada no describe ninguna sensorización— no depende de esa especificación**, porque se sostiene por
el contenido de la propia opción.

**El resto va como oficio y así se declara**: la tabla que separa decorado virtual, realidad
aumentada y producción en pared de LED; las dos iluminaciones de un plató de croma y la regla de
separar al personaje del fondo; las familias de sistemas de seguimiento; el cálculo de retardo del
epígrafe 5, que **se deduce de las cifras del propio enunciado y de la definición de fotograma por
segundo**; la definición de *plate*; el proceso de *stitching* y sus dificultades; la tabla de modos
de distribución por red; y el criterio de control que ordena las opciones de la pregunta 25.

**La cifra de 25 fotogramas por segundo es la de la televisión europea** y es la que hace que dos
fotogramas sean 80 milisegundos, tal como la respuesta oficial exige. **A otras cadencias el número
cambia** —a 50 fotogramas por segundo, dos fotogramas son 40 milisegundos— y este tema lo hace
constar: **la respuesta de la pregunta 34 vale porque el sistema es de 25**.
