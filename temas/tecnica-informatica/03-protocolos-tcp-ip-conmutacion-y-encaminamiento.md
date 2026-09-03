# Tema 3 del específico de Técnica Informática · Protocolos de red, conmutación y encaminamiento

Las siglas de este tema, presentadas de entrada: el protocolo de control de transmisión sobre el
protocolo de internet (**TCP/IP**), que da nombre al punto; el protocolo de transferencia de
hipertexto (**HTTP**) y su versión segura (**HTTPS**), con la seguridad de la capa de transporte
(**TLS**) que la sostiene; el protocolo simple de transferencia de correo (**SMTP**); el protocolo de
transferencia de ficheros sobre intérprete de órdenes seguro (**SFTP**); el protocolo de tiempo de red
(**NTP**); los tipos de registro del sistema de nombres, que se nombran por su etiqueta (**A**,
**AAAA**, **CNAME**, **MX**, **NS** y **TXT**); el protocolo ligero de acceso a directorios
(**LDAP**, *lightweight directory access protocol*); el protocolo simple de administración de red
(**SNMP**, *simple network management protocol*); el protocolo de pasarela de frontera (**BGP**,
*border gateway protocol*); el protocolo de información de encaminamiento (**RIP**, *routing
information protocol*), en sus versiones 1 y 2; el primero el camino abierto más corto (**OSPF**,
*open shortest path first*) y el mejorado de encaminamiento de pasarela interior (**EIGRP**,
*enhanced interior gateway routing protocol*); el sistema autónomo (**AS**) y su número (**ASN**);
la Autoridad de Asignación de Números de Internet (**IANA**); la red de área local virtual
(**VLAN**); el sistema de nombres de dominio (**DNS**) y el tiempo de vida de un registro
(**TTL**, *time to live*); y la calidad de servicio (**QoS**, *quality of service*).

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 4):
> «Protocolos TCP/IP. Técnicas de conmutación y enrutamiento. Puntos de acceso WiFi.»

**Nueve preguntas: el banco más grande de la ocupación.** **Y el punto que mejor separa a quien ha
administrado una red de quien sólo la ha estudiado**: **cuatro de sus nueve preguntas describen una
situación y piden la consecuencia.**

**Su reparto**: **tres preguntas son de protocolos de aplicación**, **tres de encaminamiento**, **una
de conmutación**, **una de nombres de dominio** y **una de calidad de servicio.**

<!-- indice -->

## Índice

- [1. Los puertos que el examen pide](#1-los-puertos-que-el-examen-pide)
- [2. El encaminamiento](#2-el-encaminamiento)
- [3. La conmutación y las VLAN](#3-la-conmutación-y-las-vlan)
- [4. Los nombres de dominio](#4-los-nombres-de-dominio)
- [5. La calidad de servicio](#5-la-calidad-de-servicio)
- [6. Los puntos de acceso que el enunciado nombra](#6-los-puntos-de-acceso-que-el-enunciado-nombra)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Los puertos que el examen pide

**Un puerto identifica el servicio dentro de una máquina**, y **los bien conocidos van del 0 al
1023.** **Los que este examen ha preguntado, aquí y en otros temas:**

| Servicio | Puerto |
|---|---|
| **HTTP** | **80** |
| **HTTPS** | **443** |
| **LDAP** | **389** ✔ |
| **LDAP sobre TLS** | **636** |
| **DNS** | **53** |
| **SNMP** | **161**, y **162** para las trampas |

**La pregunta 14**: **el protocolo ligero de acceso a directorios utiliza el puerto 389.** Ésa es la
respuesta oficial.

---

**Las tres opciones falsas —399, 289 y 209— son el mismo número con una cifra cambiada**, lo que
**convierte la pregunta en memoria pura**: no hay nada que razonar. **El atajo que sí ayuda es que
389 y 636 van juntos**, como 80 y 443: **el par sin cifrar y el cifrado.**

**La pregunta 32**: **el protocolo SNMP sirve para intercambiar información de administración entre
dispositivos de red y poder monitorizarlos.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas nombran tres protocolos reales de otra cosa**: **enviar correo es SMTP,
transferir ficheros de forma segura es SFTP y sincronizar la hora es NTP.** **La pregunta se contesta
traduciendo las siglas**: *simple network management protocol*, **gestión de red.**

**Lo que hay que saber de él más allá de las siglas**: **un agente en cada equipo publica variables
—carga, temperatura, tráfico, estado de un puerto— y un gestor las lee periódicamente.** **Cuando el
equipo quiere avisar sin que le pregunten, manda una trampa.**

**La pregunta 83**: **la implementación de Microsoft del protocolo LDAP se conoce como Directorio
Activo.** Ésa es la respuesta oficial.

---

**Qué es, en una línea**: **el directorio donde una organización guarda sus usuarios, sus equipos y
sus permisos**, y contra el que se autentica todo lo demás. **Las opciones falsas son un paquete
ofimático, un servicio de identidad en la nube y unas siglas inventadas.**

## 2. El encaminamiento

**Tres preguntas del punto son de aquí, y las tres cuelgan de la misma división:**

| Familia | Dónde actúa | Protocolos |
|---|---|---|
| **Interno** | **Dentro de un mismo sistema autónomo** | **RIP** (v1 y v2), **OSPF**, **EIGRP** |
| **Externo** | **Entre sistemas autónomos distintos** | **BGP** ✔ |

**Qué es un sistema autónomo**: **un conjunto de redes bajo una misma política de encaminamiento** —un
operador, una universidad, una corporación—, **identificado por un número que asigna la IANA.**

**La pregunta 35**: **el protocolo que intercambia información de encaminamiento entre sistemas
autónomos usando los números que asigna la IANA es BGP.** Ésa es la respuesta oficial.

**La pregunta 54**: **de los enumerados, el protocolo de encaminamiento externo es BGP.** Ésa es la
respuesta oficial.

---

**Son la misma pregunta dos veces**, y **la segunda añade un distractor que no es de encaminamiento**:
**Telnet es un protocolo de terminal remoto.** **RIP y OSPF son los dos internos de manual**, y **BGP
es el único externo que se usa: es el protocolo que sostiene internet.**

**La pregunta 76 va de la métrica**: **la métrica de un enrutador se utiliza para calcular el mejor
trayecto hacia un destino disponible.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son tres malentendidos que conviene desmontar uno a uno:**

| Opción | Por qué es falsa |
|---|---|
| **a) Caminos distintos al mismo destino tienen la misma métrica** | **Justo al revés**: la métrica existe **porque** los caminos son distintos; si todos valieran igual no habría nada que elegir |
| **b) Es la distancia en metros del medio de transmisión** | **La métrica no mide longitud física.** Según el protocolo, cuenta saltos, coste, ancho de banda o retardo |
| **c) Los enrutadores no usan la métrica, sólo los clientes** | **Es exactamente al revés**: el cliente no encamina, sólo tiene puerta de enlace |

**Qué cuenta cada protocolo como métrica, que es lo que da sentido a la palabra:**

| Protocolo | Su métrica |
|---|---|
| **RIP** | **El número de saltos**, con un máximo de 15 |
| **OSPF** | **El coste**, derivado del ancho de banda del enlace |
| **BGP** | **Atributos de política**, no una distancia |

## 3. La conmutación y las VLAN

**La pregunta 43 describe una situación**: **dos puertos de un conmutador configurados como puertos de
acceso de la misma VLAN, con un ordenador en cada uno.** **La respuesta oficial es que estarán en el
mismo dominio de difusión pero en distinto dominio de colisión.**

---

**Los dos dominios, que es todo el epígrafe:**

| Dominio | Qué es | Quién lo parte |
|---|---|---|
| **De colisión** | **El conjunto de equipos que pueden pisarse al transmitir a la vez** | **Cada puerto de un conmutador es uno**: el conmutador lo parte |
| **De difusión** | **El conjunto de equipos a los que llega un mensaje dirigido a todos** | **Cada VLAN es uno**, y sólo un enrutador o una VLAN distinta lo parte |

**Con esa tabla la respuesta sale sola**: **están en puertos distintos, luego en dominios de colisión
distintos**; **están en la misma VLAN, luego en el mismo dominio de difusión.**

**Y el dato histórico que explica por qué la pregunta insiste en la colisión**: **en un concentrador
todos los equipos compartían un solo dominio de colisión y se pisaban.** **El conmutador acabó con
eso al darle a cada puerto el suyo**, y por eso hoy la colisión sólo aparece en los exámenes.

**Qué añade la VLAN**: **partir un conmutador físico en varias redes lógicas que no se ven entre
sí.** **Dos equipos en VLAN distintas del mismo conmutador necesitan un enrutador para hablarse**,
igual que si estuvieran en edificios distintos.

## 4. Los nombres de dominio

**La pregunta 62**: **si un registro DNS de tipo A tiene un tiempo de vida de 60, el tiempo máximo
teórico que tardaría en propagarse un cambio es de un minuto.** Ésa es la respuesta oficial.

---

**El tiempo de vida se expresa en segundos**, y **eso es todo lo que la pregunta mide**: **60 segundos
es un minuto.** **Las tres opciones falsas son una hora, un día y medio y de veinticuatro a cuarenta y
ocho horas**, que son los valores que la gente asocia por costumbre a «propagación de DNS» y que **no
salen del dato del enunciado.**

**Qué significa el tiempo de vida, dicho con precisión**: **es cuánto puede un servidor intermedio
guardar la respuesta antes de volver a preguntar.** **Pasado ese plazo, la caché caduca y se consulta
de nuevo**, de modo que **el peor caso es exactamente el tiempo de vida.**

**El aviso de oficio**: **antes de cambiar un registro se le baja el tiempo de vida con antelación**,
se hace el cambio y después se vuelve a subir. **Cambiarlo con un tiempo de vida de un día significa
un día de tráfico repartido entre el valor viejo y el nuevo.**

**Los tipos de registro que conviene tener vistos:**

| Tipo | Qué resuelve |
|---|---|
| **A** | **Un nombre a una dirección IPv4** ✔ |
| **AAAA** | **Un nombre a una dirección IPv6** |
| **CNAME** | **Un nombre a otro nombre** |
| **MX** | **A qué servidor va el correo del dominio** |
| **NS** | **Qué servidores son autoritativos del dominio** |
| **TXT** | **Texto libre**: verificaciones y políticas de correo |

## 5. La calidad de servicio

**La pregunta 80**: **el tipo de tráfico de red que requiere calidad de servicio es la
videoconferencia.** Ésa es la respuesta oficial.

---

**Y la razón es la misma que ordena el tema 9 del específico de Técnica de Equipos**: **el tráfico en
tiempo real no se puede retransmitir.** **Un paquete de vídeo que llega tarde ya no sirve**, porque su
instante pasó.

**Los cuatro tráficos de la pregunta, clasificados por lo que les molesta:**

| Tráfico | Qué tolera mal | ¿Necesita calidad de servicio? |
|---|---|---|
| **Videoconferencia** | **El retardo y su variación** | **Sí** ✔ |
| **Correo electrónico** | **Nada en particular**: puede tardar minutos | **No** |
| **Compras en línea** | **Un retardo grande, pero no milisegundos** | **No** |
| **Descarga de software** | **Nada**: sólo quiere ancho de banda | **No** |

**Qué hace la calidad de servicio, en una línea**: **clasifica el tráfico y le da prioridad de salida
en las colas de los equipos de red**, de modo que **cuando el enlace se congestiona, lo que se retrasa
es la descarga y no la conferencia.**

**Y el aviso que hace útil el concepto**: **la calidad de servicio no crea ancho de banda.** **Reparte
el que hay.** **En un enlace sobrado no cambia nada; en uno saturado decide quién sufre.**

## 6. Los puntos de acceso que el enunciado nombra

**El punto pide «puntos de acceso WiFi» y el examen no los ha preguntado en este tema.** **Lo mínimo
que conviene llevar visto:**

| Norma | Banda |
|---|---|
| **802.11b** y **802.11g** | **2,4 GHz** |
| **802.11a** y **802.11ac** | **5 GHz** |
| **802.11n** | **2,4 GHz y 5 GHz** |

**Y las dos reglas de instalación**: **en 2,4 gigahercios sólo hay tres canales que no se solapan
—el 1, el 6 y el 11—**, y **los puntos de acceso vecinos deben repartírselos**; **y la alimentación
por el propio cable de red ahorra una toma de corriente en cada punto**, que es lo que el tema 12 del
específico de Técnica de Equipos llama alimentación por Ethernet.

## 7. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 14 | Puerto del protocolo LDAP | b) 389 ✔ |
| 32 | Para qué sirve el protocolo SNMP | c) Intercambiar información de administración y monitorizar ✔ |
| 35 | Protocolo de encaminamiento entre sistemas autónomos | a) BGP ✔ |
| 43 | Dos puertos de acceso de la misma VLAN | b) Mismo dominio de difusión, distinto de colisión ✔ |
| 54 | Cuál es un protocolo de encaminamiento externo | b) BGP ✔ |
| 62 | Propagación de un registro DNS con tiempo de vida 60 | a) Un minuto ✔ |
| 76 | Para qué sirve la métrica de un enrutador | d) Para calcular el mejor trayecto ✔ |
| 80 | Qué tráfico requiere calidad de servicio | b) Videoconferencia ✔ |
| 83 | Implementación de Microsoft del protocolo LDAP | c) Directorio Activo ✔ |

**Las nueve respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **sólo una de las nueve es memoria pura** —el puerto 389—; **las ocho
restantes se razonan con dos ideas: qué separa un dominio de colisión de uno de difusión, y qué
distingue un protocolo interno de uno externo.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **Los documentos que definen LDAP, SNMP, BGP, RIP, OSPF y el sistema de nombres de dominio no se
   han consultado.** **Sus números de puerto, su clasificación en internos y externos y el
   significado del tiempo de vida son de uso universal**, y **coinciden con las respuestas
   oficiales.**
2. **El Directorio Activo es un producto comercial**, y **el temario sólo afirma de él lo que la
   respuesta oficial afirma**: que es la implementación de LDAP de su fabricante. **No se ha
   consultado su documentación.**
3. **El cuadro de métricas por protocolo del epígrafe 2 —saltos en RIP con un máximo de quince,
   coste en OSPF, atributos de política en BGP— es de uso corriente**, y **ninguna respuesta oficial
   depende de él**: la pregunta 76 sólo pide para qué sirve la métrica.
4. **Las bandas de la familia IEEE 802.11 del epígrafe 6 y la regla de los canales 1, 6 y 11 son de
   uso universal.** **La familia de normas no se ha consultado**, y **ninguna pregunta de este tema
   depende de ellas.**
5. **Este punto y el punto 14 del anexo de Técnica de Equipos y Sistemas Electrónicos se solapan**,
   y **lo que allí se declaró vale aquí.**

**El resto del tema va como oficio y así se declara**: el atajo de los pares de puertos sin cifrar y
cifrado, la descripción del funcionamiento de un agente de gestión de red, el desmontaje de las tres
opciones falsas sobre la métrica, la tabla de dominios de colisión y difusión con su explicación
histórica, el aviso sobre bajar el tiempo de vida antes de un cambio y la advertencia de que la
calidad de servicio reparte ancho de banda y no lo crea. **Nada de eso está en un boletín oficial ni
en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
