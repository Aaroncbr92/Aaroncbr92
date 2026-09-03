# Esquema · Tema 3 del específico de Técnica Informática · Protocolos de red, conmutación y encaminamiento

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de administración de redes ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: el protocolo de control de transmisión sobre
el de internet (**TCP/IP**); el de transferencia de hipertexto (**HTTP**) y su versión segura
(**HTTPS**), con la seguridad de la capa de transporte (**TLS**); el simple de transferencia de correo
(**SMTP**); el de ficheros sobre intérprete de órdenes seguro (**SFTP**); el de tiempo de red
(**NTP**); los tipos de registro de nombres (**A**, **AAAA**, **CNAME**, **MX**, **NS**, **TXT**); el
ligero de acceso a directorios (**LDAP**); el simple de administración de red (**SNMP**); el de
pasarela de frontera (**BGP**); el de información de encaminamiento (**RIP**), el primero el camino
abierto más corto (**OSPF**) y el mejorado de pasarela interior (**EIGRP**); el sistema autónomo
(**AS**); la Autoridad de Asignación de Números de
Internet (**IANA**); la red de área local virtual (**VLAN**); el sistema de nombres de dominio
(**DNS**) con su tiempo de vida (**TTL**); y la calidad de servicio (**QoS**).

**Cabecera.** Enunciado: punto 4 del anexo · **9 preguntas: el banco más grande de la ocupación** ·
**ninguna lleva figura** · **cuatro de las nueve describen una situación y piden la consecuencia**,
que es lo que separa a quien ha administrado una red de quien sólo la ha estudiado.

<!-- indice -->

## Índice

- [Los puertos](#los-puertos)
- [Gestión de red y directorio](#gestión-de-red-y-directorio)
- [Encaminamiento](#encaminamiento)
- [Conmutación y VLAN](#conmutación-y-vlan)
- [Nombres de dominio](#nombres-de-dominio)
- [Calidad de servicio](#calidad-de-servicio)
- [Puntos de acceso](#puntos-de-acceso)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los puertos

| Servicio | Puerto |
|---|---|
| **HTTP** | **80** |
| **HTTPS** | **443** |
| **LDAP** | **389** ✔ |
| **LDAP sobre TLS** | **636** |
| **DNS** | **53** |
| **SNMP** | **161**, y **162** para las trampas |

- **PREGUNTA 14** · `[exam]` · **LDAP usa el puerto 389.**
- **LAS TRES FALSAS —399, 289, 209— SON EL MISMO NÚMERO CON UNA CIFRA CAMBIADA**: **memoria pura, no
  hay nada que razonar.**
- **EL ATAJO QUE SÍ AYUDA**: **389 y 636 van juntos, como 80 y 443**: el par sin cifrar y el cifrado.
- **LOS BIEN CONOCIDOS VAN DEL 0 AL 1023.**

## Gestión de red y directorio

- **PREGUNTA 32** · `[exam]` · **SNMP sirve para intercambiar información de administración entre
  dispositivos de red y monitorizarlos.**
- **SE CONTESTA TRADUCIENDO LAS SIGLAS**: *simple network management protocol*, **gestión de red.**
  **Las tres falsas son protocolos reales de otra cosa**: **enviar correo es SMTP, transferir ficheros
  con seguridad es SFTP, sincronizar la hora es NTP.**
- **CÓMO FUNCIONA** · `[of]` · **un agente en cada equipo publica variables —carga, temperatura,
  tráfico, estado de un puerto— y un gestor las lee.** **Cuando el equipo avisa sin que le pregunten,
  manda una trampa.**
- **PREGUNTA 83** · `[exam]` · **La implementación de Microsoft de LDAP es el Directorio Activo.**
- **QUÉ ES, EN UNA LÍNEA**: **el directorio donde una organización guarda usuarios, equipos y
  permisos**, y contra el que se autentica todo lo demás.

## Encaminamiento

| Familia | Dónde actúa | Protocolos |
|---|---|---|
| **Interno** | **Dentro de un mismo sistema autónomo** | **RIP**, **OSPF**, **EIGRP** |
| **Externo** | **Entre sistemas autónomos distintos** | **BGP** ✔ |

- **QUÉ ES UN SISTEMA AUTÓNOMO**: **un conjunto de redes bajo una misma política de encaminamiento**
  —un operador, una universidad, una corporación—, **con número asignado por la IANA.**
- **PREGUNTA 35** · `[exam]` · **El que intercambia encaminamiento entre sistemas autónomos es BGP.**
- **PREGUNTA 54** · `[exam]` · **El de encaminamiento externo es BGP.**
- **SON LA MISMA PREGUNTA DOS VECES**, y **la segunda añade un distractor que ni siquiera encamina**:
  **Telnet es terminal remoto.** **BGP es el único externo que se usa: el protocolo que sostiene
  internet.**
- **PREGUNTA 76** · `[exam]` · **La métrica sirve para calcular el mejor trayecto hacia un destino.**

| Opción falsa | Por qué lo es |
|---|---|
| **Caminos distintos tienen la misma métrica** | **Justo al revés**: la métrica existe PORQUE los caminos son distintos |
| **Es la distancia en metros del medio** | **No mide longitud física**: cuenta saltos, coste, ancho de banda o retardo |
| **Sólo la usan los clientes** | **Al revés**: el cliente no encamina, sólo tiene puerta de enlace |

| Protocolo | Su métrica |
|---|---|
| **RIP** | **Saltos**, máximo 15 |
| **OSPF** | **Coste**, derivado del ancho de banda |
| **BGP** | **Atributos de política**, no una distancia |

## Conmutación y VLAN

- **PREGUNTA 43** · `[exam]` · **Dos ordenadores en dos puertos de acceso de la misma VLAN están en el
  mismo dominio de difusión y en distinto dominio de colisión.**

| Dominio | Qué es | Quién lo parte |
|---|---|---|
| **De colisión** | **Los equipos que pueden pisarse al transmitir a la vez** | **Cada puerto de un conmutador es uno** |
| **De difusión** | **Los equipos a los que llega un mensaje dirigido a todos** | **Cada VLAN es uno**; sólo un enrutador o otra VLAN lo parte |

- **CON ESA TABLA LA RESPUESTA SALE SOLA**: **puertos distintos, colisión distinta; misma VLAN,
  difusión igual.**
- **POR QUÉ INSISTE EN LA COLISIÓN**: **en un concentrador todos compartían un solo dominio de
  colisión y se pisaban.** **El conmutador acabó con eso**, y por eso la colisión hoy sólo aparece en
  los exámenes.
- **QUÉ AÑADE LA VLAN**: **parte un conmutador físico en varias redes lógicas que no se ven.** **Dos
  equipos en VLAN distintas necesitan un enrutador**, como si estuvieran en edificios distintos.

## Nombres de dominio

- **PREGUNTA 62** · `[exam]` · **Un registro de tipo A con tiempo de vida 60 tarda como mucho un
  minuto en propagarse.**
- **TODO LO QUE MIDE ES QUE EL TIEMPO DE VIDA VA EN SEGUNDOS**: **60 segundos es un minuto.** **Las
  falsas —una hora, día y medio, de 24 a 48 horas— son lo que la gente asocia por costumbre y no sale
  del enunciado.**
- **QUÉ ES, CON PRECISIÓN**: **cuánto puede un servidor intermedio guardar la respuesta antes de
  volver a preguntar.** **El peor caso es exactamente el tiempo de vida.**
- **EL AVISO DE OFICIO**: **antes de cambiar un registro se le baja el tiempo de vida con antelación,
  se cambia y se vuelve a subir.** **Cambiarlo con un día de vida es un día de tráfico repartido entre
  el valor viejo y el nuevo.**

| Tipo | Qué resuelve |
|---|---|
| **A** | **Nombre a dirección IPv4** ✔ |
| **AAAA** | **Nombre a dirección IPv6** |
| **CNAME** | **Nombre a otro nombre** |
| **MX** | **A qué servidor va el correo del dominio** |
| **NS** | **Qué servidores son autoritativos** |
| **TXT** | **Texto libre**: verificaciones y políticas de correo |

## Calidad de servicio

- **PREGUNTA 80** · `[exam]` · **El tráfico que requiere calidad de servicio es la videoconferencia.**
- **LA RAZÓN**: **el tráfico en tiempo real no se puede retransmitir.** **Un paquete de vídeo que
  llega tarde ya no sirve**, porque su instante pasó.

| Tráfico | Qué tolera mal | ¿La necesita? |
|---|---|---|
| **Videoconferencia** | **El retardo y su variación** | **Sí** ✔ |
| **Correo electrónico** | **Nada**: puede tardar minutos | **No** |
| **Compras en línea** | **Un retardo grande, no milisegundos** | **No** |
| **Descarga de software** | **Nada**: sólo quiere ancho de banda | **No** |

- **QUÉ HACE, EN UNA LÍNEA**: **clasifica el tráfico y le da prioridad de salida en las colas**, de
  modo que **al congestionarse el enlace se retrasa la descarga y no la conferencia.**
- **EL AVISO**: **no crea ancho de banda: reparte el que hay.** **En un enlace sobrado no cambia nada;
  en uno saturado decide quién sufre.**

## Puntos de acceso

| Norma | Banda |
|---|---|
| **802.11b** y **802.11g** | **2,4 GHz** |
| **802.11a** y **802.11ac** | **5 GHz** |
| **802.11n** | **Las dos** |

- **LAS DOS REGLAS DE INSTALACIÓN**: **en 2,4 gigahercios sólo hay tres canales que no se solapan
  —1, 6 y 11— y los vecinos deben repartírselos**; **la alimentación por el propio cable de red ahorra
  una toma de corriente en cada punto.**
- **EL ENUNCIADO LOS PIDE Y EL EXAMEN NO LOS HA PREGUNTADO.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 14 | Puerto de LDAP | b) 389 ✔ |
| 32 | Para qué sirve SNMP | c) Administrar y monitorizar dispositivos de red ✔ |
| 35 | Encaminamiento entre sistemas autónomos | a) BGP ✔ |
| 43 | Dos puertos de acceso de la misma VLAN | b) Misma difusión, distinta colisión ✔ |
| 54 | Protocolo de encaminamiento externo | b) BGP ✔ |
| 62 | Propagación con tiempo de vida 60 | a) Un minuto ✔ |
| 76 | Para qué sirve la métrica | d) Para calcular el mejor trayecto ✔ |
| 80 | Qué tráfico requiere calidad de servicio | b) Videoconferencia ✔ |
| 83 | Implementación de Microsoft de LDAP | c) Directorio Activo ✔ |

**Las nueve oficiales son correctas** · **ninguna descansa en la plantilla** · **ninguna sale de una
norma volcada.** · **Aviso de estudio**: **sólo una es memoria pura —el puerto 389—; las otras ocho se
razonan con dos ideas**: **qué separa colisión de difusión, y qué distingue interno de externo.**
