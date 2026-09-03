# Esquema · Tema 2 del específico de Técnica Informática · Comunicaciones y redes: modelos y direccionamiento

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de redes · `[exam]` = opciones
del propio cuadernillo. **Siglas**: la interconexión de sistemas abiertos (**OSI**); el protocolo de
internet (**IP**), el de control de transmisión (**TCP**) y el par que forman (**TCP/IP**), con sus
versiones 4 y 6 (**IPv4** e **IPv6**); el control de acceso al medio (**MAC**); el protocolo de
transferencia de hipertexto (**HTTP**); y el bloque de mensajes del servidor (**SMB**), que sale como
opción falsa.

**Cabecera.** Enunciado: punto 3 del anexo · **8 preguntas** · **ninguna lleva figura** · **es el
punto que esta ocupación comparte casi palabra por palabra con el 14 de Técnica de Equipos y Sistemas
Electrónicos**, y **donde las dos preguntan lo mismo, la respuesta coincide.**

<!-- indice -->

## Índice

- [Las dos pilas](#las-dos-pilas)
- [Cada protocolo en su capa](#cada-protocolo-en-su-capa)
- [Clases y rangos privados de IPv4](#clases-y-rangos-privados-de-ipv4)
- [IPv6](#ipv6)
- [Qué dirección usa cada equipo](#qué-dirección-usa-cada-equipo)
- [Configuración básica: los cuatro datos](#configuración-básica-los-cuatro-datos)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las dos pilas

| OSI (siete capas) | TCP/IP (cuatro) | Qué resuelve |
|---|---|---|
| **7. Aplicación · 6. Presentación · 5. Sesión** | **Aplicación** | **Qué significan los datos para el programa** |
| **4. Transporte** | **Transporte** | **Que lleguen, o que lleguen deprisa** |
| **3. Red** | **Internet** | **Cómo se encamina un paquete de una red a otra** |
| **2. Enlace · 1. Física** | **Acceso a la red** | **Cómo viajan los bits por el cable o por el aire** |

- **PREGUNTA 57** · `[exam]` · **La pila TCP/IP consta de 4 capas.**
- **PREGUNTA 22** · `[exam]` · **La que NO es capa del modelo OSI es «Inalámbrica».**
- **LAS DOS CIFRAS SE APRENDEN JUNTAS Y CON NOMBRE**: **siete el OSI, cuatro el TCP/IP.** **La opción
  «7» de la 57 es la trampa evidente.**
- **LAS SIETE, DE ABAJO ARRIBA**: **física, enlace, red, transporte, sesión, presentación,
  aplicación.** **«Inalámbrica» no es una capa: es un medio**, y el medio vive en la física.

## Cada protocolo en su capa

- **PREGUNTA 67** · `[exam]` · **El de la capa de transporte —capa 4— es TCP.**

| Protocolo | Capa OSI |
|---|---|
| **Ethernet** | **2, enlace** |
| **IP** | **3, red** |
| **TCP** | **4, transporte** ✔ |
| **HTTP** | **7, aplicación** |

- **LAS TRES FALSAS SON CADA UNA DE OTRA CAPA**: **la pregunta es un repaso del cuadro.**
- **LA REGLA QUE SITÚA CUALQUIER PROTOCOLO SIN MEMORIZARLO**: **si mueve tramas por un cable, enlace;
  si encamina entre redes, red; si garantiza o no la entrega extremo a extremo, transporte; si lo
  entiende un programa, aplicación.**

## Clases y rangos privados de IPv4

| Clase | Primer octeto | Para qué se pensó |
|---|---|---|
| **A** | **1 a 126** | **Redes muy grandes** |
| **B** | **128 a 191** | **Redes medianas** |
| **C** | **192 a 223** | **Redes pequeñas** |
| **D** | **224 a 239** | **Envío a varios destinos** |
| **E** | **240 a 255** | **Reservada** |

| Clase | Rango privado |
|---|---|
| **A** | **10.0.0.0 a 10.255.255.255** ✔ |
| **B** | **172.16.0.0 a 172.31.255.255** |
| **C** | **192.168.0.0 a 192.168.255.255** |

- **PREGUNTA 9** · `[exam]` · **El privado de clase A es 10.0.0.0 a 10.255.255.255.**
- **LAS TRES FALSAS ESTÁN TODAS EN EL CUADRO**: **una recorta el rango a 256 direcciones, otra es el
  privado de clase B y otra el de clase C.**
- **PREGUNTA 45** · `[exam]` · **La pública de clase C es 201.55.23.147.**
- **SE RESUELVE EN DOS COMPROBACIONES Y EN ESTE ORDEN**: **primero, ¿clase C? el primer octeto entre
  192 y 223** —fuera 10.50.100.62, de clase A, y 146.34.207.39, de clase B—; **después, ¿pública?**
  **192.168.150.86 está en el rango privado**, luego queda la otra.
- **EL AVISO QUE HACE ÚTIL EL EJERCICIO**: **pertenecer a una clase y ser pública son dos cosas
  distintas**, y la pregunta pide las dos a la vez.

## IPv6

- **PREGUNTA 28** · `[exam]` · **128 bits.**
- **PREGUNTA 33** · `[exam]` · **El bucle local es `::1/128`.**

| | **IPv4** | **IPv6** |
|---|---|---|
| **Bits** | **32** | **128** |
| **Cómo se escribe** | **Cuatro decimales de 0 a 255 con puntos** | **Ocho grupos de cuatro cifras hexadecimales con dos puntos** |
| **Loopback** | **127.0.0.1** | **`::1`** |
| **Ruta por defecto** | **0.0.0.0/0** | **`::/0`** |

- **LAS FALSAS DE LA 33 SE ORDENAN CON ESE CUADRO**: **`::/0` es la ruta por defecto, no el bucle
  local**; **`fe81::/1` y `ffff:/1` no son direcciones válidas** —la segunda ni siquiera bien escrita.
- **EL DATO QUE HACE MEMORIZABLE EL `::1`**: **el doble dos puntos abrevia una sucesión de ceros**,
  así que **`::1` es «ciento veintisiete ceros y un uno»**, lo mismo que 127.0.0.1 con otra notación.

## Qué dirección usa cada equipo

- **PREGUNTA 70** · `[exam]` · **Los enrutadores usan la dirección IP.**

| Dirección | Capa | Quién la usa | Cuánto alcanza |
|---|---|---|---|
| **MAC, o física** | **Enlace, 2** | **El conmutador** | **Sólo el segmento local** |
| **IP, o lógica** | **Red, 3** | **El enrutador** | **De una red a otra, por todo internet** ✔ |

- **LA RAZÓN DE FONDO**: **la física va grabada en la tarjeta y no dice dónde está el equipo; la
  lógica se asigna y sí dice a qué red pertenece**, y **encaminar es decidir a qué red va el paquete.**
- **LAS FALSAS**: **«dirección MAC» y «dirección física» son la misma cosa dicha de dos maneras**
  —indicio de que ninguna puede ser la respuesta—, y **«dirección SMB» no existe**: SMB es un
  protocolo de compartición de ficheros.

## Configuración básica: los cuatro datos

| Dato | Qué decide |
|---|---|
| **Dirección IP** | **Quién es el equipo** |
| **Máscara de subred** | **Hasta dónde llega su red local** |
| **Puerta de enlace** | **Por dónde sale lo que no es de su red** |
| **Servidor de nombres** | **Quién traduce los nombres a direcciones** |

- **EL ORDEN EN QUE SE MIRA UNA CONFIGURACIÓN AVERIADA ES EL MISMO**: **sin dirección no habla; con
  máscara mal puesta habla con quien no debe; sin puerta de enlace no sale de su red; sin servidor de
  nombres sale pero no encuentra nada por su nombre.**
- **NO SE HA PREGUNTADO AQUÍ**, sino en el tema 3.

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 9 | Rango privado de clase A | a) 10.0.0.0 a 10.255.255.255 ✔ |
| 22 | Cuál NO es capa del modelo OSI | b) Inalámbrica ✔ |
| 28 | Bits de una dirección IPv6 | c) 128 ✔ |
| 33 | Loopback de IPv6 | b) `::1/128` ✔ |
| 45 | IPv4 pública de clase C | c) 201.55.23.147 ✔ |
| 57 | Capas de la pila TCP/IP | b) 4 ✔ |
| 67 | Protocolo de transporte en OSI | b) TCP ✔ |
| 70 | Qué direcciones usan los enrutadores | d) Dirección IP ✔ |

**Las ocho oficiales son correctas** · **ninguna descansa en la plantilla** · **ninguna sale de una
norma volcada.** · **Aviso de estudio**: **el cuadro de las dos pilas y el de clases y rangos privados
contestan seis de las ocho.** **Dos tablas, una sentada.**
