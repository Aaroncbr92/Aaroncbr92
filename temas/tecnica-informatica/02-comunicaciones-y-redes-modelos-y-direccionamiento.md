# Tema 2 del específico de Técnica Informática · Comunicaciones y redes: modelos y direccionamiento

Las siglas de este tema, presentadas de entrada: la interconexión de sistemas abiertos (**OSI**, *open
systems interconnection*); el protocolo de internet (**IP**), el protocolo de
control de transmisión (**TCP**) y el par que forman los dos (**TCP/IP**), con sus versiones 4 y 6
(**IPv4** e **IPv6**); el protocolo de datagramas de usuario
(**UDP**); el control de acceso al medio (**MAC**, *media access control*); el protocolo de
transferencia de hipertexto (**HTTP**); y el bloque de mensajes del servidor (**SMB**, *server message
block*), que aparece como opción falsa.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 3):
> «COMUNICACIONES Y REDES: Terminología y conceptos. Los modelos de referencia OSI y TCP/IP. Redes
> IP. Direccionamiento. Configuración básica de equipos de red.»

**Ocho preguntas.** **Y es un punto que esta ocupación comparte casi palabra por palabra con Técnica
de Equipos y Sistemas Electrónicos**, cuyo punto 14 tiene el mismo título y el mismo contenido. **Las
respuestas coinciden**, y donde el examen ha preguntado lo mismo se dice.

**Su reparto**: **tres preguntas son de los dos modelos de referencia**, **cuatro de direccionamiento**
y **una de qué dirección usa cada equipo.**

<!-- indice -->

## Índice

- [1. Los dos modelos de referencia](#1-los-dos-modelos-de-referencia)
- [2. El direccionamiento IPv4](#2-el-direccionamiento-ipv4)
- [3. IPv6](#3-ipv6)
- [4. Qué dirección usa cada equipo](#4-qué-dirección-usa-cada-equipo)
- [5. La configuración básica que el enunciado nombra](#5-la-configuración-básica-que-el-enunciado-nombra)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Los dos modelos de referencia

| Modelo OSI (siete capas) | Modelo TCP/IP (cuatro capas) | Qué resuelve |
|---|---|---|
| **7. Aplicación · 6. Presentación · 5. Sesión** | **Aplicación** | **Qué significan los datos para el programa** |
| **4. Transporte** | **Transporte** | **Que los datos lleguen, o que lleguen deprisa** |
| **3. Red** | **Internet** | **Cómo se encamina un paquete de una red a otra** |
| **2. Enlace · 1. Física** | **Acceso a la red** | **Cómo viajan los bits por el cable o por el aire** |

**La pregunta 57**: **la pila de protocolos TCP/IP consta de 4 capas.** Ésa es la respuesta oficial.

**La pregunta 22 es negativa**: **de las enumeradas, la que NO es una capa del modelo OSI es
«Inalámbrica».** Ésa es la respuesta oficial.

---

**Las dos cifras hay que aprenderlas juntas y con nombre**: **siete el OSI, cuatro el TCP/IP.** **La
opción «7» de la pregunta 57 es la trampa evidente**, y **quien memorice «siete capas» sin distinguir
el modelo cae.**

**Y la 22 se contesta con la lista de las siete**: **física, enlace, red, transporte, sesión,
presentación y aplicación.** **«Inalámbrica» no es una capa: es un medio**, y el medio vive dentro de
la capa física.

**La pregunta 67**: **de los protocolos enumerados, el que pertenece a la capa de transporte —capa 4—
del modelo OSI es TCP.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son cada una de otra capa**, lo que **convierte la pregunta en un repaso
del cuadro:**

| Protocolo | Capa OSI |
|---|---|
| **Ethernet** | **2, enlace** |
| **IP** | **3, red** |
| **TCP** | **4, transporte** ✔ |
| **HTTP** | **7, aplicación** |

**La regla que sitúa cualquier protocolo sin memorizarlo**: **si mueve tramas por un cable, es
enlace; si encamina entre redes, es red; si garantiza o no la entrega extremo a extremo, es
transporte; si lo entiende un programa, es aplicación.**

## 2. El direccionamiento IPv4

**Las clases de dirección, que es lo que el examen pide:**

| Clase | Primer octeto | Para qué se pensó |
|---|---|---|
| **A** | **1 a 126** | **Redes muy grandes**: pocas redes, muchísimos equipos |
| **B** | **128 a 191** | **Redes medianas** |
| **C** | **192 a 223** | **Redes pequeñas**: muchas redes, pocos equipos |
| **D** | **224 a 239** | **Envío a varios destinos** |
| **E** | **240 a 255** | **Reservada** |

**Y los tres rangos privados, que son los que no salen a internet:**

| Clase | Rango privado |
|---|---|
| **A** | **10.0.0.0 a 10.255.255.255** ✔ |
| **B** | **172.16.0.0 a 172.31.255.255** |
| **C** | **192.168.0.0 a 192.168.255.255** |

**La pregunta 9**: **el rango de direcciones IP privadas de clase A es 10.0.0.0 a 10.255.255.255.**
Ésa es la respuesta oficial.

---

**Las tres opciones falsas están todas en el cuadro**: **la b recorta el rango de clase A a un solo
tramo de 256 direcciones, la c es el privado de clase B y la d el de clase C.** **La pregunta se
contesta sabiendo que el privado de clase A ocupa el primer octeto entero.**

**La pregunta 45**: **de las direcciones enumeradas, la pública de clase C es 201.55.23.147.** Ésa es
la respuesta oficial.

---

**Se resuelve en dos comprobaciones y en este orden:**

1. **¿Es de clase C?** **El primer octeto tiene que estar entre 192 y 223.** **La 10.50.100.62 es de
   clase A y la 146.34.207.39 de clase B**: fuera las dos.
2. **¿Es pública?** **Quedan la 192.168.150.86 y la 201.55.23.147**, y **la primera está dentro del
   rango privado 192.168.**, luego **la pública es la segunda.**

**El aviso que hace útil el ejercicio**: **192.168 y 192.0.2 son de clase C y no son públicas.**
**Pertenecer a una clase y ser pública son dos cosas distintas**, y la pregunta pide las dos a la vez.

## 3. IPv6

**La pregunta 28**: **una dirección IPv6 consta de 128 bits.** Ésa es la respuesta oficial.

**La pregunta 33**: **la dirección de loopback de IPv6 es `::1/128`.** Ésa es la respuesta oficial.

---

**Las dos versiones, con la cifra que las separa:**

| | **IPv4** | **IPv6** |
|---|---|---|
| **Bits** | **32** | **128** |
| **Cómo se escribe** | **Cuatro números decimales de 0 a 255 separados por puntos** | **Ocho grupos de cuatro cifras hexadecimales separados por dos puntos** |
| **Loopback** | **127.0.0.1** | **`::1`** |
| **Ruta por defecto** | **0.0.0.0/0** | **`::/0`** |

**Las opciones falsas de la 33 se ordenan con ese cuadro**: **`::/0` es la ruta por defecto, no el
bucle local**; **`fe81::/1` y `ffff:/1` no son direcciones válidas** —la segunda ni siquiera está bien
escrita, con dos puntos simples.

**Y el dato que hace memorizable el `::1`**: **el doble dos puntos abrevia una sucesión de ceros**, de
modo que **`::1` es «ciento veintisiete ceros y un uno»**, que es exactamente lo que en IPv4 se
escribe 127.0.0.1 con otra notación.

## 4. Qué dirección usa cada equipo

**La pregunta 70**: **los enrutadores utilizan la dirección IP para enviar los paquetes de datos
correctamente.** Ésa es la respuesta oficial.

---

**Y ahí está la distinción que ordena las dos primeras capas de la red:**

| Dirección | De qué capa es | Quién la usa | Cuánto alcanza |
|---|---|---|---|
| **MAC, o dirección física** | **Enlace, capa 2** | **El conmutador** | **Sólo dentro del segmento local** |
| **IP, o dirección lógica** | **Red, capa 3** | **El enrutador** | **De una red a otra, por todo internet** ✔ |

**La razón de fondo, que conviene entender y no memorizar**: **la dirección física va grabada en la
tarjeta y no dice dónde está el equipo**; **la dirección IP se asigna y sí dice a qué red pertenece**,
y **encaminar es precisamente decidir a qué red hay que mandar el paquete.**

**Las opciones falsas de la pregunta**: **«dirección MAC» y «dirección física» son la misma cosa dicha
de dos maneras**, lo que **ya es un indicio de que ninguna de las dos puede ser la respuesta**;
**y «dirección SMB» no existe**: SMB es un protocolo de compartición de ficheros, no un tipo de
dirección.

## 5. La configuración básica que el enunciado nombra

**El punto pide «configuración básica de equipos de red» y el examen no la ha preguntado en este
tema**, sino en el 3. **Lo que conviene llevar visto son los cuatro datos que configuran cualquier
equipo:**

| Dato | Qué decide |
|---|---|
| **Dirección IP** | **Quién es el equipo** |
| **Máscara de subred** | **Hasta dónde llega su red local** |
| **Puerta de enlace** | **Por dónde sale lo que no es de su red** |
| **Servidor de nombres** | **Quién traduce los nombres a direcciones** |

**Y la comprobación de averías que se deriva de ellos, en ese mismo orden**: **sin dirección, el
equipo no habla; con máscara mal puesta, habla con quien no debe; sin puerta de enlace, no sale de su
red; sin servidor de nombres, sale pero no encuentra nada por su nombre.** **Es el orden en que se
mira una configuración que no funciona.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 9 | Rango de direcciones IP privadas de clase A | a) 10.0.0.0 a 10.255.255.255 ✔ |
| 22 | Cuál NO es una capa del modelo OSI | b) Inalámbrica ✔ |
| 28 | Bits de una dirección IPv6 | c) 128 ✔ |
| 33 | Dirección de loopback de IPv6 | b) `::1/128` ✔ |
| 45 | Dirección IPv4 pública de clase C | c) 201.55.23.147 ✔ |
| 57 | Capas de la pila TCP/IP | b) 4 ✔ |
| 67 | Protocolo de la capa de transporte del modelo OSI | b) TCP ✔ |
| 70 | Qué direcciones usan los enrutadores | d) Dirección IP ✔ |

**Las ocho respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **el cuadro de las dos pilas y el de clases y rangos privados contestan seis
de las ocho.** **Son dos tablas y se aprenden de una sentada.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **La norma que define el modelo OSI y los documentos que definen la familia TCP/IP no se han
   consultado.** **El número y el nombre de sus capas son conocimiento común de la materia**, y
   **coinciden con las respuestas oficiales de las preguntas 22, 57 y 67.**
2. **Los rangos de direcciones privadas y las clases de IPv4 son de uso universal**, y **el
   documento que los reserva no se ha volcado.** **La respuesta oficial de la pregunta 9 los
   reproduce**, y el temario no los atribuye a ningún apartado.
3. **La longitud de una dirección IPv6 y su dirección de bucle local se dan como conocimiento común**,
   coincidentes con las respuestas oficiales. **La especificación de IPv6 no se ha consultado.**
4. **Este punto tiene el mismo título y casi el mismo contenido que el punto 14 del anexo de Técnica
   de Equipos y Sistemas Electrónicos**, cuyo tema 12 está escrito en este mismo proyecto. **Lo que
   allí se dijo vale aquí**, y **donde el examen de las dos ocupaciones pregunta lo mismo, la
   respuesta coincide.**

**El resto del tema va como oficio y así se declara**: la regla para situar un protocolo en su capa,
el método de dos comprobaciones de la pregunta 45, la explicación de por qué el doble dos puntos
abrevia ceros, la distinción entre dirección física y lógica y el orden en que se mira una
configuración averiada. **Nada de eso está en un boletín oficial ni en una norma técnica de las
consultadas**, y el tema no lo presenta como si lo estuviera.
