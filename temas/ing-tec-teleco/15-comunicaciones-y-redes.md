# Tema 15 del específico de Ingeniería Técnica · Telecomunicación · Comunicaciones y redes

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Técnica Telecomunicación · punto 19 |
| **Sirve para** | **Ing. Técnica Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los modelos, el direccionamiento y los protocolos, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Punto compartido** | **Este bloque es casi idéntico al punto 3 del anexo de Técnica Informática y al 14 del de Técnica de Equipos y Sistemas Electrónicos.** Donde el examen de dos ocupaciones pregunta lo mismo, la respuesta coincide |
| **Extensión** | **3.663 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la interconexión de sistemas abiertos (**OSI**); el
protocolo de internet (**IP**), el de control de transmisión (**TCP**), el par que forman (**TCP/IP**)
y el de datagramas de usuario (**UDP**); el control de acceso al medio (**MAC**); el protocolo de
resolución de direcciones (**ARP**); el de información de encaminamiento (**RIP**), el primero el
camino abierto más corto (**OSPF**) y el de pasarela de frontera (**BGP**); la traducción de direcciones de red (**NAT**); el protocolo de
árbol de expansión (**STP**), que evita lazos; el de transporte en tiempo real (**RTP**) y el de
tiempo de precisión (**PTP**); el de mensajería en tiempo real (**RTMP**); el acceso protegido a redes
inalámbricas en su tercera versión (**WPA3**); el par trenzado sin apantallar (**UTP**); el conector
registrado 45 (**RJ45**); la televisión por protocolo de internet (**IPTV**); el ordenador personal
(**PC**); y las órdenes de consola, que van en acentos graves porque son código.

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Telecomunicación, punto 19):
> «Comunicaciones y redes. Terminología y conceptos. Los modelos de referencia OSI y TCP/IP.
> Protocolos TCP/IP. Redes de control IP en equipamiento broadcast. Técnicas de conmutación y
> enrutamiento. Internet. Servicios y protocolos. Gestión de redes.»

**Dieciocho preguntas: el banco más grande de la ocupación, empatado con el de sonido.**

**Su reparto**: **seis son de direccionamiento**, **cinco de protocolos**, **tres de encaminamiento y
conmutación**, **dos de medio físico**, **una de modelos de referencia** y **una de control de
equipamiento audiovisual.**

**Y el aviso que ordena el punto entero**: **este bloque es casi idéntico al punto 3 del anexo de
Técnica Informática y al 14 del de Técnica de Equipos y Sistemas Electrónicos**, escritos en este
mismo proyecto. **Donde el examen de dos ocupaciones pregunta lo mismo, la respuesta coincide.**

<!-- indice -->

## Índice

- [1. Los dos modelos de referencia](#1-los-dos-modelos-de-referencia)
- [2. El direccionamiento](#2-el-direccionamiento)
- [3. Los protocolos que el examen pide](#3-los-protocolos-que-el-examen-pide)
- [4. El encaminamiento](#4-el-encaminamiento)
- [5. La conmutación y los lazos](#5-la-conmutación-y-los-lazos)
- [6. El medio físico](#6-el-medio-físico)
- [7. Las redes de control del equipamiento audiovisual](#7-las-redes-de-control-del-equipamiento-audiovisual)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Los dos modelos de referencia

| Modelo OSI (siete capas) | Modelo TCP/IP (cuatro) | Qué resuelve |
|---|---|---|
| **7. Aplicación · 6. Presentación · 5. Sesión** | **Aplicación** | **Qué significan los datos para el programa** |
| **4. Transporte** | **Transporte** | **Que los datos lleguen, o que lleguen deprisa** |
| **3. Red** | **Internet** | **Cómo se encamina un paquete de una red a otra** |
| **2. Enlace · 1. Física** | **Acceso a la red** | **Cómo viajan los bits por el cable o por el aire** |

**La pregunta 95**: **el modelo TCP/IP es un modelo de 4 capas utilizado en redes de
comunicaciones.** Ésa es la respuesta oficial.

---

**Y la opción falsa que dice siete capas es la trampa evidente**: **siete son las del otro modelo.**
**Las dos cifras se aprenden juntas y con nombre**, o se confunden.

**La pregunta 93 pide situar dos protocolos concretos**: **el protocolo de datagramas de usuario
pertenece a la capa de transporte y el de transporte en tiempo real, a la capa de aplicación.** Ésa es
la respuesta oficial.

---

**Y es la pregunta mejor construida del punto**, porque **exige entender una jerarquía y no memorizar
una lista.**

| Protocolo | Capa en el modelo TCP/IP | Qué aporta |
|---|---|---|
| **UDP** | **Transporte** ✔ | **Envío sin conexión, sin garantía y sin retardo de retransmisión** |
| **RTP** | **Aplicación** ✔ | **Marcas de tiempo y números de secuencia, para reconstruir el orden y el ritmo** |

**Por qué van juntos, que es la razón de que la pregunta exista**: **el vídeo en tiempo real no puede
esperar a que se retransmita un paquete perdido**, así que **usa el transporte que no lo intenta.**
**Pero ese transporte no numera ni marca el tiempo**, y **sin eso no se puede reconstruir la
secuencia.** **El protocolo de tiempo real añade encima justo lo que falta.**

**La opción falsa que dice que nunca pueden usarse juntos es la que delata quién no ha visto una
instalación**: **es exactamente lo que se hace todos los días.**

## 2. El direccionamiento

**Seis preguntas del punto son de aquí**, y **casi todas se contestan con dos tablas.**

**Las clases y los rangos:**

| Clase | Primer octeto | Para qué se pensó |
|---|---|---|
| **A** | **1 a 126** | **Redes muy grandes**: pocas redes, muchísimos equipos ✔ |
| **B** | **128 a 191** | **Redes medianas** |
| **C** | **192 a 223** | **Redes pequeñas** |
| **D** | **224 a 239** | **Envío a varios destinos** ✔ |
| **E** | **240 a 255** | **Reservada** |

**La pregunta 45**: **una dirección IP de clase A representa redes grandes con un gran número de
equipos.** Ésa es la respuesta oficial.

**La pregunta 1**: **de las direcciones enumeradas, la reservada es 224.1.1.1.** Ésa es la respuesta
oficial.

---

**Las dos se contestan con la misma tabla leída por dos filas distintas**, y **conviene notar la
construcción de la segunda**: **una de las cuatro opciones ni siquiera es una dirección válida** —tiene
cinco octetos—, **otra es privada de clase C y otra es pública corriente.** **La marcada es de clase
D, que está reservada para envío a varios destinos**, y **eso es exactamente lo que hace el vídeo
sobre red del tema 7.**

**La pregunta 25**: **una dirección de difusión es una dirección utilizada para enviar datos a todos
los dispositivos en una red.** Ésa es la respuesta oficial.

**La pregunta 53**: **en una red con máscara 255.255.255.0, la dirección de difusión es
192.168.1.255.** Ésa es la respuesta oficial.

---

**Las dos son la definición y su aplicación**, y **la regla que las une es de una línea**: **la
dirección de difusión es la que tiene todos los bits de equipo a uno.**

**Con máscara de veinticuatro bits, el último octeto es el de equipo**, luego:

| Dirección | Qué es |
|---|---|
| **192.168.1.0** | **La red**: todos los bits de equipo a cero |
| **192.168.1.1** | **Un equipo cualquiera**, normalmente la puerta de enlace |
| **192.168.1.254** | **El último equipo utilizable** |
| **192.168.1.255** | **La difusión**: todos los bits de equipo a uno ✔ |

**La pregunta 80**: **en la red 172.16.4.0/24, el rango de equipos va de 1 a 254.** Ésa es la
respuesta oficial.

---

**Y es la misma cuenta vista al revés**: **veinticuatro bits de red dejan ocho de equipo**, que son
**256 combinaciones**; **menos la de todo ceros —la red— y la de todo unos —la difusión—, quedan
254.**

**La fórmula general, que conviene llevar porque el examen puede cambiar la máscara**: **con *n* bits
de equipo hay 2 elevado a *n*, menos 2, direcciones utilizables.**

| Máscara | Bits de equipo | Equipos utilizables |
|---|---|---|
| **/24** | **8** | **254** ✔ |
| **/25** | **7** | **126** |
| **/26** | **6** | **62** |
| **/27** | **5** | **30** |

**Y ahí está la finura de la pregunta**: **las tres opciones falsas son exactamente las tres filas
siguientes de esa tabla.** **Quien sepa la fórmula las descarta las tres a la vez.**

**La pregunta 11**: **en una tabla de encaminamiento, el prefijo 0.0.0.0/0 es la ruta por defecto para
cualquier destino.** Ésa es la respuesta oficial.

---

**Y la razón está en la propia longitud del prefijo**: **cero bits de red significa que NINGÚN bit
tiene que coincidir**, luego **cualquier dirección casa con ella.**

**Cómo se usa eso en la práctica**: **el enrutador busca siempre la coincidencia más larga.** **La
ruta por defecto, al ser la más corta posible, es la última que gana**, y por eso **es la salida
cuando ninguna otra ruta sirve.**

**Las tres opciones falsas confunden esa dirección con otras tres cosas**: **una red concreta, una
reserva y la difusión.** **Ninguna de las tres tiene longitud de prefijo cero.**

**La pregunta 30**: **la traducción de direcciones de red es una técnica que permite traducir
direcciones IP privadas a públicas.** Ésa es la respuesta oficial.

---

**Para qué existe, en una línea**: **porque las direcciones públicas de la versión 4 se agotaron**, y
**una organización entera sale a internet con unas pocas.**

**Y las tres opciones falsas nombran tres cosas reales de la misma capa**: **un protocolo de
encaminamiento, una tabla de resolución de direcciones físicas y un protocolo de asignación de
direcciones.** **La palabra que decide es «traducir».**

## 3. Los protocolos que el examen pide

**La pregunta 87**: **el protocolo de resolución de direcciones sirve para resolver direcciones IP a
direcciones físicas.** Ésa es la respuesta oficial.

---

**Y ahí está la pareja que ordena las dos primeras capas**, la misma del tema 15 de esta ocupación y
del 2 de Técnica Informática:

| Dirección | Capa | Quién la usa | Cuánto alcanza |
|---|---|---|---|
| **Física** | **Enlace, 2** | **El conmutador** | **Sólo el segmento local** |
| **IP** | **Red, 3** | **El enrutador** | **De una red a otra** |

**Qué hace exactamente ese protocolo**: **un equipo que quiere hablar con una dirección IP de su
propia red necesita la dirección física correspondiente.** **La pregunta a voces —«¿quién tiene esta
dirección?»— y el dueño contesta.** **Sin él, dos equipos de la misma red no podrían enviarse ni una
trama.**

**La pregunta 70**: **el protocolo para una transmisión lo más rápida posible, sin establecer conexión
y sin garantía de entrega, es el de datagramas de usuario.** Ésa es la respuesta oficial.

---

**La comparación que la contesta y que vale para todo el temario:**

| | **TCP** | **UDP** |
|---|---|---|
| **¿Establece conexión?** | **Sí, con un saludo de tres pasos** | **No** ✔ |
| **¿Garantiza la entrega?** | **Sí: retransmite lo perdido** | **No** |
| **¿Garantiza el orden?** | **Sí** | **No** |
| **Qué cuesta** | **Retardo y variabilidad** | **Nada: manda y olvida** |
| **Para qué sirve** | **Ficheros, web, correo** | **Vídeo y audio en tiempo real, voz** |

**La regla que resume la elección**: **si perder un dato es peor que llegar tarde, transporte con
conexión; si llegar tarde es peor que perder un dato, sin conexión.** **Un paquete de vídeo que llega
tarde ya no sirve**, y por eso el vídeo va sin conexión.

**La pregunta 57**: **para conocer la ruta que ha seguido una dirección IP se usa la orden
`tracert`.** Ésa es la respuesta oficial.

---

**Las tres opciones falsas son nombres inventados**, así que **es memoria del nombre correcto.** **El
apoyo es que viene de *trace route*, trazar la ruta**, y **en los sistemas de la familia Unix se llama
`traceroute`.**

**Las cuatro órdenes de diagnóstico que el enunciado da por sabidas:**

| Orden | Qué hace |
|---|---|
| `ping` | **Comprueba si un destino responde y en cuánto tiempo** |
| `tracert` | **Enumera los saltos hasta el destino y dice en cuál se pierde** ✔ |
| `ipconfig` | **Muestra la configuración del propio equipo** |
| `nslookup` | **Consulta el sistema de nombres** |

**El orden en que se usan cuando algo no funciona, que es lo que un ingeniero hace de verdad**:
**primero la configuración propia, después el ping a la puerta de enlace, después el ping a una
dirección de fuera, después la traza y sólo al final la consulta de nombres.** **Ese orden separa el
problema en capas y evita mirar donde no está.**

**La pregunta 54**: **el protocolo de seguridad inalámbrica en su tercera versión utiliza 192 bits
para su cifrado.** Ésa es la respuesta oficial.

---

**Y hay que precisar lo que la pregunta simplifica**: **192 bits es la fuerza de la suite de la
versión empresarial de ese protocolo.** **Su modo personal usa 128.** **De las cuatro cifras
ofrecidas, 192 es la única que corresponde a algo real de esa norma**, y se marca.

## 4. El encaminamiento

**La pregunta 29**: **el protocolo que se utiliza comúnmente para actualizar las tablas de
encaminamiento en un enrutador es el de información de encaminamiento.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son dos siglas mal escritas y una de otra capa**: **la de resolución de
direcciones es de enlace**, y **las otras dos son deformaciones de nombres reales** —una del primero
el camino abierto más corto y otra que no existe—.

**La familia entera, que es lo preguntable de lo que no ha caído:**

| Familia | Dónde actúa | Protocolos | Qué mide |
|---|---|---|---|
| **Interno, por vector de distancia** | **Dentro de un sistema autónomo** | **RIP** ✔ | **Saltos**, con un máximo de 15 |
| **Interno, por estado de enlace** | **Dentro de un sistema autónomo** | **OSPF** | **Coste**, derivado del ancho de banda |
| **Externo** | **Entre sistemas autónomos** | **BGP** | **Atributos de política** |

**La diferencia de fondo entre las dos primeras**: **el de vector de distancia sólo sabe lo que le
cuentan sus vecinos**; **el de estado de enlace conoce el mapa entero de la red y calcula el camino él
mismo.** **Por eso el segundo converge antes y escala mejor**, y por eso el primero está limitado a
quince saltos.

## 5. La conmutación y los lazos

**La pregunta 17**: **el protocolo que evita lazos lógicos en redes Ethernet es el de árbol de
expansión.** Ésa es la respuesta oficial.

---

**Por qué un lazo es un desastre y no un inconveniente**: **una trama de difusión que entra en un
bucle no se agota nunca.** **A diferencia de un paquete de red, una trama de enlace NO lleva contador
de saltos**, así que **da vueltas indefinidamente, se multiplica en cada conmutador y satura la red en
segundos.** **Es la llamada tormenta de difusión**, y **tumba una instalación entera.**

**Qué hace el protocolo, en una línea**: **elige un conmutador raíz, calcula el mejor camino hacia él
desde cada punto y BLOQUEA los enlaces sobrantes**, dejando una topología sin bucles. **Si un enlace
activo cae, desbloquea uno de los que tenía en reserva.**

**Y las tres opciones falsas son tres protocolos reales de otra cosa**, lo que **convierte la pregunta
en un repaso de siglas parecidas:**

| Sigla | Qué es |
|---|---|
| **RTP** | **Transporte en tiempo real**: el de la pregunta 93 |
| **PTP** | **Tiempo de precisión**: el reloj del vídeo sobre red del tema 7 |
| **STP** | **Árbol de expansión: evita lazos** ✔ |
| **RTMP** | **Mensajería en tiempo real**: difusión de vídeo por internet |

**El aviso de vocabulario que conviene llevar**: **las mismas tres letras nombran también el par
trenzado apantallado.** **Son dos cosas sin ninguna relación**, y el examen usa las dos siglas.

## 6. El medio físico

**La pregunta 89**: **la distancia máxima que admite un cable de par trenzado sin apantallar de
categoría 5 es 100 metros.** Ésa es la respuesta oficial.

---

**Es la cifra más repetida de todo el cableado estructurado**, y **conviene saber cómo se reparte**:
**90 metros de cable fijo más 10 de latiguillos**, entre los dos extremos.

**Por qué existe ese límite y no es un capricho**: **por la atenuación y por el tiempo de ida y
vuelta.** **Más allá, la señal llega demasiado débil y el mecanismo de detección de colisiones deja de
funcionar** en las variantes que lo usan.

**La pregunta 86**: **al conectar un ordenador personal a un concentrador con cable de datos y
conector registrado, hay que conectorizar los dos extremos según código de color normal.** Ésa es la
respuesta oficial.

---

**Y la regla que hay detrás es la que el examen persigue:**

| Qué se conecta | Cable |
|---|---|
| **Equipo a conmutador o concentrador** | **Normal, los dos extremos igual** ✔ |
| **Equipo a equipo** | **Cruzado** |
| **Conmutador a conmutador** | **Cruzado** |

**La lógica, que la hace innecesaria de memorizar**: **un equipo transmite por un par y recibe por
otro; un conmutador hace lo contrario.** **Entre distintos, el cruce ya está hecho dentro del aparato;
entre iguales, hay que hacerlo en el cable.**

**Y la opción falsa que dice que todos los aparatos se adaptan es la trampa moderna**: **hoy casi
todos lo hacen**, con detección automática, **pero la pregunta habla de un concentrador**, que es
equipo antiguo, **y la norma de cableado sigue siendo la que es.** **La respuesta oficial es la
correcta según la norma**, y el temario lo sostiene con esa observación.

## 7. Las redes de control del equipamiento audiovisual

**La pregunta 63**: **el equipo que gestiona por red la configuración de los equipos audiovisuales se
denomina controlador de difusión.** Ésa es la respuesta oficial.

---

**Y ésta es la pregunta más de casa del punto**, porque **no es de informática general: es del
enunciado propio de esta ocupación**, que pide expresamente «redes de control IP en equipamiento
broadcast».

**Qué hace y por qué existe**: **en una instalación moderna, cada cámara, cada matriz, cada
sincronizador y cada servidor se configura por red.** **El controlador centraliza esa configuración**:
guarda perfiles, los aplica a varios equipos a la vez y permite recuperar el estado de un aparato
sustituido.

**La opción falsa que más engaña es el controlador de dominio**, porque **es un término real y muy
conocido de la informática de gestión**: **es el servidor que gobierna usuarios y permisos en un
dominio**, y **no tiene nada que ver con configurar una cámara.** **Las otras dos opciones son nombres
verosímiles que no designan ningún equipo.**

**Y la separación de redes que este epígrafe deja como aviso de oficio**: **la red de control no es la
red de señal ni la red ofimática.** **Se separan porque un problema en una no puede tumbar las
otras**, y **porque el tráfico de señal del tema 7 llena un enlace de diez gigabits con unas pocas
señales.**

## 8. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 1 | Cuál es una dirección IPv4 reservada | d) 224.1.1.1 ✔ |
| 11 | Qué significa el prefijo 0.0.0.0/0 | d) La ruta por defecto para cualquier destino ✔ |
| 17 | Qué protocolo evita lazos en Ethernet | c) STP ✔ |
| 25 | Qué es una dirección de difusión | a) La que envía a todos los dispositivos de la red ✔ |
| 29 | Protocolo para actualizar tablas de encaminamiento | b) RIP ✔ |
| 30 | Qué es la traducción de direcciones de red | d) Traducir direcciones privadas a públicas ✔ |
| 45 | Qué representa una dirección de clase A | c) Redes grandes con un gran número de equipos ✔ |
| 53 | Difusión en una red con máscara 255.255.255.0 | c) 192.168.1.255 ✔ |
| 54 | Bits de cifrado del protocolo inalámbrico de tercera versión | b) 192 ✔ **·** con precisión |
| 57 | Orden para conocer la ruta seguida | b) `tracert` ✔ |
| 63 | Equipo que gestiona por red la configuración audiovisual | b) Controlador de difusión ✔ |
| 70 | Protocolo rápido, sin conexión y sin garantía | d) UDP ✔ |
| 80 | Rango de equipos en 172.16.4.0/24 | a) De 1 a 254 ✔ |
| 86 | Cómo conectorizar un equipo a un concentrador | c) Los dos extremos según código normal ✔ |
| 87 | Qué es el protocolo de resolución de direcciones | a) Resolver direcciones IP a direcciones físicas ✔ |
| 89 | Distancia máxima de un par trenzado de categoría 5 | c) 100 metros ✔ |
| 93 | A qué capas pertenecen los dos protocolos de una difusión por internet | b) Transporte y aplicación ✔ |
| 95 | Qué es el modelo TCP/IP | b) Un modelo de 4 capas ✔ |

**Las dieciocho respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **Una
lleva precisión declarada**: la 54, cuya cifra corresponde a la suite empresarial de esa norma.

**El aviso de estudio**: **la fórmula de los bits de equipo contesta una pregunta y descarta las tres
opciones falsas de otra.** **Y las dos tablas de clases y de difusión contestan cuatro.** **Es el
punto más rentable de la ocupación por tiempo invertido.**

## 9. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Los documentos que definen los modelos de referencia, el direccionamiento, los protocolos de
   encaminamiento y el árbol de expansión no se han consultado.** **Sus reglas y sus cifras son de
   uso universal**, y **coinciden con las respuestas oficiales.**
2. **La precisión sobre la pregunta 54 es del temario, no una impugnación**: **192 bits es la fuerza
   de la suite de la versión empresarial de esa norma y su modo personal usa 128.** **De las cuatro
   cifras ofrecidas, la marcada es la única que corresponde a algo real**, y se marca.
3. **La observación sobre la pregunta 86 tampoco es una impugnación**: **hoy casi todos los aparatos
   se adaptan automáticamente**, y **la respuesta oficial es la correcta según la norma de
   cableado**, que es lo que la pregunta pide.
4. **El controlador de difusión de la pregunta 63 se describe con lo que la respuesta oficial afirma
   y con oficio de instalación.** **No se ha consultado la documentación de ningún fabricante**, y
   **el temario no atribuye a ningún producto concreto lo que dice.**

**El resto del tema va como oficio y así se declara**: la explicación de por qué el vídeo en tiempo
real usa los dos protocolos juntos, la regla de la coincidencia más larga, la fórmula de las
direcciones utilizables, el orden en que se usan las órdenes de diagnóstico, la razón de que una
trama en bucle no se agote, la lógica del cable cruzado y la separación entre red de control, de señal
y ofimática. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y
el tema no lo presenta como si lo estuviera.
