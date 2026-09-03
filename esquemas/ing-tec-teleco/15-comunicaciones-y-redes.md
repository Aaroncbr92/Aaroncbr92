# Esquema · Tema 15 del específico de Ingeniería Técnica · Telecomunicación · Comunicaciones y redes

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de redes · `[exam]` = opciones
del propio cuadernillo. **Siglas**: la interconexión de sistemas abiertos (**OSI**); el protocolo de
internet (**IP**), el de control de transmisión (**TCP**), el par que forman (**TCP/IP**) y el de
datagramas de usuario (**UDP**); el control de acceso al medio (**MAC**); el protocolo de resolución
de direcciones (**ARP**); el de información de encaminamiento (**RIP**), el primero el camino abierto
más corto (**OSPF**) y el de pasarela de frontera (**BGP**); la traducción de direcciones de red
(**NAT**); el árbol de expansión (**STP**); el de transporte en tiempo real (**RTP**) y el de tiempo
de precisión (**PTP**); el de mensajería en tiempo real (**RTMP**); el acceso protegido a redes
inalámbricas en su tercera versión (**WPA3**); el par trenzado sin apantallar (**UTP**); el conector
registrado 45 (**RJ45**); la televisión por protocolo de internet (**IPTV**); el ordenador personal
(**PC**); y las órdenes de consola, en acentos graves porque son código.

**Cabecera.** Enunciado: punto 19 del anexo · **18 preguntas: el banco más grande de la ocupación,
empatado con el de sonido** · **reparto**: 6 de direccionamiento, 5 de protocolos, 3 de encaminamiento
y conmutación, 2 de medio físico, 1 de modelos, 1 de control de equipamiento audiovisual · **es el
punto más rentable de la ocupación por tiempo invertido.**

<!-- indice -->

## Índice

- [Los dos modelos](#los-dos-modelos)
- [El direccionamiento](#el-direccionamiento)
- [Los protocolos](#los-protocolos)
- [El encaminamiento](#el-encaminamiento)
- [La conmutación y los lazos](#la-conmutación-y-los-lazos)
- [El medio físico](#el-medio-físico)
- [Las redes de control audiovisual](#las-redes-de-control-audiovisual)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los dos modelos

| Modelo OSI (siete capas) | Modelo TCP/IP (cuatro) | Qué resuelve |
|---|---|---|
| **7. Aplicación · 6. Presentación · 5. Sesión** | **Aplicación** | **Qué significan los datos para el programa** |
| **4. Transporte** | **Transporte** | **Que los datos lleguen, o que lleguen deprisa** |
| **3. Red** | **Internet** | **Cómo se encamina un paquete de una red a otra** |
| **2. Enlace · 1. Física** | **Acceso a la red** | **Cómo viajan los bits por el cable o por el aire** |

- **PREGUNTA 95** · `[exam]` · **El modelo TCP/IP tiene 4 capas.** **La falsa de siete es la del otro
  modelo**: las dos cifras se aprenden juntas y con nombre, o se confunden.
- **PREGUNTA 93** · `[exam]` · **El de datagramas de usuario es de TRANSPORTE y el de transporte en
  tiempo real es de APLICACIÓN.**

| Protocolo | Capa | Qué aporta |
|---|---|---|
| **UDP** | **Transporte** ✔ | **Envío sin conexión, sin garantía y sin retardo de retransmisión** |
| **RTP** | **Aplicación** ✔ | **Marcas de tiempo y números de secuencia, para reconstruir orden y ritmo** |

- **POR QUÉ VAN JUNTOS** · `[of]` · **El vídeo en tiempo real no puede esperar a que se retransmita un
  paquete perdido**, así que usa el transporte que no lo intenta; **pero ese transporte no numera ni
  marca el tiempo**, y el de tiempo real añade encima justo lo que falta.
- **LA FALSA QUE DELATA** · `[exam]` · **«Nunca pueden usarse juntos»**: es exactamente lo que se hace
  todos los días.

## El direccionamiento

| Clase | Primer octeto | Para qué se pensó |
|---|---|---|
| **A** | **1 a 126** | **Redes muy grandes**: pocas redes, muchísimos equipos ✔ |
| **B** | **128 a 191** | **Redes medianas** |
| **C** | **192 a 223** | **Redes pequeñas** |
| **D** | **224 a 239** | **Envío a varios destinos** ✔ |
| **E** | **240 a 255** | **Reservada** |

- **PREGUNTA 45** · `[exam]` · **La clase A representa redes grandes con muchos equipos.**
- **PREGUNTA 1** · `[exam]` · **La reservada es 224.1.1.1**, de clase D. **De las cuatro opciones, una
  ni siquiera es válida** —tiene cinco octetos—, **otra es privada de clase C y otra pública
  corriente.**
- **PREGUNTA 25** · `[exam]` · **La dirección de difusión envía datos a todos los dispositivos de la
  red.**
- **PREGUNTA 53** · `[exam]` · **Con máscara 255.255.255.0, la difusión es 192.168.1.255.**
- **LA REGLA DE UNA LÍNEA** · `[of]` · **La difusión es la que tiene todos los bits de equipo a UNO.**

| Dirección | Qué es |
|---|---|
| **192.168.1.0** | **La red**: bits de equipo a cero |
| **192.168.1.1** | **Un equipo**, normalmente la puerta de enlace |
| **192.168.1.254** | **El último utilizable** |
| **192.168.1.255** | **La difusión** ✔ |

- **PREGUNTA 80** · `[exam]` · **En 172.16.4.0/24 el rango de equipos va de 1 a 254.**
- **LA FÓRMULA GENERAL** · `[of]` · **Con *n* bits de equipo hay 2 elevado a *n*, menos 2, direcciones
  utilizables.**

| Máscara | Bits de equipo | Utilizables |
|---|---|---|
| **/24** | **8** | **254** ✔ |
| **/25** | **7** | **126** |
| **/26** | **6** | **62** |
| **/27** | **5** | **30** |

- **LA FINURA DE LA 80** · `[of]` · **Las tres falsas son las tres filas siguientes de esa tabla.**
  **Quien sepa la fórmula las descarta las tres a la vez.**
- **PREGUNTA 11** · `[exam]` · **El prefijo 0.0.0.0/0 es la ruta por defecto para cualquier destino.**
  **Cero bits de red significa que NINGÚN bit tiene que coincidir**, luego cualquier dirección casa.
- **CÓMO SE USA** · `[of]` · **El enrutador busca la coincidencia MÁS LARGA**: la ruta por defecto, al
  ser la más corta posible, **es la última que gana.**
- **PREGUNTA 30** · `[exam]` · **La traducción de direcciones de red traduce privadas a públicas.**
  **Existe porque las públicas de la versión 4 se agotaron.** **La palabra que decide es «traducir».**

## Los protocolos

- **PREGUNTA 87** · `[exam]` · **El protocolo de resolución de direcciones resuelve direcciones IP a
  direcciones físicas.**

| Dirección | Capa | Quién la usa | Cuánto alcanza |
|---|---|---|---|
| **Física** | **Enlace, 2** | **El conmutador** | **Sólo el segmento local** |
| **IP** | **Red, 3** | **El enrutador** | **De una red a otra** |

- **QUÉ HACE EXACTAMENTE** · `[of]` · **Pregunta a voces «¿quién tiene esta dirección?» y el dueño
  contesta.** **Sin él, dos equipos de la misma red no podrían enviarse ni una trama.**
- **PREGUNTA 70** · `[exam]` · **El transporte más rápido, sin conexión y sin garantía, es el de
  datagramas de usuario.**

| | **TCP** | **UDP** |
|---|---|---|
| **¿Conexión?** | **Sí, saludo de tres pasos** | **No** ✔ |
| **¿Garantiza entrega?** | **Sí: retransmite** | **No** |
| **¿Garantiza orden?** | **Sí** | **No** |
| **Qué cuesta** | **Retardo y variabilidad** | **Nada: manda y olvida** |
| **Para qué** | **Ficheros, web, correo** | **Vídeo, audio en tiempo real, voz** |

- **LA REGLA DE LA ELECCIÓN** · `[of]` · **Si perder un dato es peor que llegar tarde, con conexión; si
  llegar tarde es peor que perder un dato, sin conexión.** **Un paquete de vídeo que llega tarde ya no
  sirve.**
- **PREGUNTA 57** · `[exam]` · **Para conocer la ruta seguida se usa `tracert`.** **Viene de *trace
  route*** y en la familia Unix se llama `traceroute`. **Las falsas son nombres inventados.**

| Orden | Qué hace |
|---|---|
| `ping` | **Comprueba si un destino responde y en cuánto tiempo** |
| `tracert` | **Enumera los saltos y dice en cuál se pierde** ✔ |
| `ipconfig` | **Muestra la configuración del propio equipo** |
| `nslookup` | **Consulta el sistema de nombres** |

- **EL ORDEN EN QUE SE USAN** · `[of]` · **Configuración propia · ping a la puerta de enlace · ping a
  una dirección de fuera · traza · y sólo al final la consulta de nombres.** **Ese orden separa el
  problema en capas y evita mirar donde no está.**
- **PREGUNTA 54** · `[exam]` · **El protocolo inalámbrico de tercera versión cifra con 192 bits.**
- **LA PRECISIÓN DECLARADA** · `[of]` · **192 es la fuerza de la suite de la versión EMPRESARIAL; el
  modo personal usa 128.** **De las cuatro cifras, es la única que corresponde a algo real.**

## El encaminamiento

- **PREGUNTA 29** · `[exam]` · **El protocolo común para actualizar tablas de encaminamiento es el de
  información de encaminamiento.** **Las falsas son dos siglas deformadas y una de otra capa.**

| Familia | Dónde actúa | Protocolo | Qué mide |
|---|---|---|---|
| **Interno, vector de distancia** | **Dentro de un sistema autónomo** | **RIP** ✔ | **Saltos**, máximo 15 |
| **Interno, estado de enlace** | **Dentro de un sistema autónomo** | **OSPF** | **Coste**, del ancho de banda |
| **Externo** | **Entre sistemas autónomos** | **BGP** | **Atributos de política** |

- **LA DIFERENCIA DE FONDO** · `[of]` · **El de vector de distancia sólo sabe lo que le cuentan sus
  vecinos; el de estado de enlace conoce el mapa entero y calcula el camino él mismo.** **Por eso el
  segundo converge antes y escala mejor**, y el primero está limitado a quince saltos.

## La conmutación y los lazos

- **PREGUNTA 17** · `[exam]` · **El protocolo que evita lazos en Ethernet es el de árbol de expansión.**
- **POR QUÉ UN LAZO ES UN DESASTRE** · `[of]` · **Una trama de enlace NO lleva contador de saltos**, así
  que **una trama de difusión en bucle da vueltas indefinidamente, se multiplica en cada conmutador y
  satura la red en segundos.** **Es la tormenta de difusión, y tumba una instalación entera.**
- **QUÉ HACE EL PROTOCOLO** · `[of]` · **Elige un conmutador raíz, calcula el mejor camino hacia él y
  BLOQUEA los enlaces sobrantes.** **Si un enlace activo cae, desbloquea uno de reserva.**

| Sigla | Qué es |
|---|---|
| **RTP** | **Transporte en tiempo real** |
| **PTP** | **Tiempo de precisión**: el reloj del vídeo sobre red |
| **STP** | **Árbol de expansión: evita lazos** ✔ |
| **RTMP** | **Mensajería en tiempo real**: difusión de vídeo por internet |

- **EL AVISO DE VOCABULARIO** · `[of]` · **Las mismas tres letras nombran también el par trenzado
  apantallado.** **Son dos cosas sin relación**, y el examen usa las dos siglas.

## El medio físico

- **PREGUNTA 89** · `[exam]` · **La distancia máxima de un par trenzado sin apantallar de categoría 5
  es 100 metros**: **90 de cable fijo más 10 de latiguillos.**
- **POR QUÉ EXISTE ESE LÍMITE** · `[of]` · **Por la atenuación y por el tiempo de ida y vuelta**: más
  allá, la señal llega demasiado débil y **el mecanismo de detección de colisiones deja de funcionar**
  en las variantes que lo usan.
- **PREGUNTA 86** · `[exam]` · **Ordenador a concentrador: los dos extremos según código de color
  normal.**

| Qué se conecta | Cable |
|---|---|
| **Equipo a conmutador o concentrador** | **Normal, los dos extremos igual** ✔ |
| **Equipo a equipo** | **Cruzado** |
| **Conmutador a conmutador** | **Cruzado** |

- **LA LÓGICA QUE AHORRA MEMORIZAR** · `[of]` · **Un equipo transmite por un par y recibe por otro; un
  conmutador hace lo contrario.** **Entre distintos, el cruce ya está hecho dentro; entre iguales, hay
  que hacerlo en el cable.**
- **LA TRAMPA MODERNA** · `[of]` · **«Todos los aparatos se adaptan»**: hoy casi todos lo hacen con
  detección automática, **pero la pregunta habla de un CONCENTRADOR**, que es equipo antiguo, **y la
  norma de cableado sigue siendo la que es.**

## Las redes de control audiovisual

- **PREGUNTA 63** · `[exam]` · **El equipo que gestiona por red la configuración de los equipos
  audiovisuales es el controlador de difusión.**
- **POR QUÉ ES LA MÁS DE CASA DEL PUNTO** · `[of]` · **No es de informática general: sale del enunciado
  propio de esta ocupación**, que pide «redes de control IP en equipamiento broadcast».
- **QUÉ HACE** · `[of]` · **Cada cámara, matriz, sincronizador y servidor se configura por red**, y el
  controlador **guarda perfiles, los aplica a varios equipos a la vez y permite recuperar el estado de
  un aparato sustituido.**
- **LA FALSA QUE MÁS ENGAÑA** · `[exam]` · **«Controlador de dominio»**: término real y conocido de la
  informática de gestión —**el servidor que gobierna usuarios y permisos**—, **sin nada que ver con
  configurar una cámara.**
- **EL AVISO DE OFICIO** · `[of]` · **La red de control no es la de señal ni la ofimática.** **Se separan
  porque un problema en una no puede tumbar las otras** y **porque el tráfico de señal llena un enlace
  de diez gigabits con unas pocas señales.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 1 | Cuál es una dirección reservada | **224.1.1.1** ✔ |
| 11 | Qué significa 0.0.0.0/0 | **La ruta por defecto** ✔ |
| 17 | Qué protocolo evita lazos | **STP** ✔ |
| 25 | Qué es una dirección de difusión | **La que envía a todos los de la red** ✔ |
| 29 | Protocolo para actualizar tablas de encaminamiento | **RIP** ✔ |
| 30 | Qué es la traducción de direcciones de red | **Traducir privadas a públicas** ✔ |
| 45 | Qué representa una dirección de clase A | **Redes grandes con muchos equipos** ✔ |
| 53 | Difusión con máscara 255.255.255.0 | **192.168.1.255** ✔ |
| 54 | Bits de cifrado del inalámbrico de tercera versión | **192** ✔ **·** con precisión |
| 57 | Orden para conocer la ruta | **`tracert`** ✔ |
| 63 | Equipo que gestiona la configuración audiovisual | **Controlador de difusión** ✔ |
| 70 | Protocolo rápido, sin conexión y sin garantía | **UDP** ✔ |
| 80 | Rango de equipos en 172.16.4.0/24 | **De 1 a 254** ✔ |
| 86 | Cómo conectorizar un equipo a un concentrador | **Los dos extremos en código normal** ✔ |
| 87 | Qué es el protocolo de resolución de direcciones | **Resolver IP a dirección física** ✔ |
| 89 | Distancia máxima de par trenzado de categoría 5 | **100 metros** ✔ |
| 93 | Capas de los dos protocolos de una difusión | **Transporte y aplicación** ✔ |
| 95 | Qué es el modelo TCP/IP | **Un modelo de 4 capas** ✔ |
