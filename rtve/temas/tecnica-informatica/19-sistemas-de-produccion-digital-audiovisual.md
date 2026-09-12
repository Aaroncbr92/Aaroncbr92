# Tema 19 del específico de Técnica Informática · Sistemas de producción digital audiovisual

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · punto 22 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Índice público de la familia de normas SMPTE ST 2110**, de la Sociedad de Ingenieros de Cine y Televisión |
| **Identificador** | Índice publicado por la propia sociedad · **el articulado está tras un muro de pago y no se ha leído** |
| **Redacción que se estudia** | **Los títulos oficiales de sus partes**, citados literalmente del índice. **Nada de su contenido interno** |
| **Rasgo del punto** | **Es el ÚNICO punto de la ocupación cuya respuesta está verificada contra un organismo de normalización**, y no como oficio |
| **Norma no consultada** | **El texto de la norma AES67 está tras un muro de pago y no se ha leído.** Lo que el tema afirma de ella es lo que la respuesta oficial afirma |
| **Extensión** | **1.524 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la Sociedad de Ingenieros de Cine y Televisión
(**SMPTE**), que publica la familia de normas **SMPTE ST 2110**; la Sociedad de Ingeniería de Audio
(**AES**), que publica la norma **AES67**; el protocolo de internet (**IP**) y el de datagramas de
usuario (**UDP**); el protocolo de tiempo de precisión (**PTP**); la interfaz digital serie (**SDI**); la modulación por impulsos codificados (**PCM**), que da nombre
a una de las partes que se citan;
y el audio y el vídeo (**A/V**), como los abrevia el enunciado.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 22):
> «Sistemas de Producción Digital A/V. Arquitectura básica genérica.»

**Dos preguntas.** **Y las dos piden lo mismo: el número de una norma.** **Una de la Sociedad de
Ingenieros de Cine y Televisión y otra de la Sociedad de Ingeniería de Audio.**

**Este punto tiene una particularidad de método que conviene decir**: **es el único del temario de
Técnica Informática cuya respuesta está verificada contra un documento público de un organismo de
normalización**, y no como oficio. **El índice de la familia SMPTE ST 2110 está volcado en este
proyecto**, y de él sale la respuesta.

<!-- indice -->

## Índice

- [1. Por qué una televisión mete el vídeo en la red de datos](#1-por-qué-una-televisión-mete-el-vídeo-en-la-red-de-datos)
- [2. La familia SMPTE ST 2110](#2-la-familia-smpte-st-2110)
- [3. La norma de audio sobre red](#3-la-norma-de-audio-sobre-red)
- [4. La arquitectura básica que el enunciado pide](#4-la-arquitectura-básica-que-el-enunciado-pide)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Por qué una televisión mete el vídeo en la red de datos

**El cambio que este punto describe se resume en una frase**: **la matriz y el cable coaxial se están
sustituyendo por un conmutador y un cable de red.**

**Lo que se gana:**

| Ventaja | Por qué |
|---|---|
| **Un solo cable para todo** | **Vídeo, audio, control y datos por la misma infraestructura** |
| **Encaminamiento sin límite de tamaño** | **Un conmutador crece añadiendo equipos; una matriz tiene un tamaño fijo** |
| **Equipo genérico** | **Se compra electrónica de red corriente, no aparatos de un solo fabricante** |
| **Flexibilidad** | **Reconfigurar es cambiar una suscripción, no recablear** |

**Y lo que se pierde, que es de lo que se ocupan las normas de este punto:**

| Garantía que el cable daba sola | Cómo se recupera en la red |
|---|---|
| **Sincronismo** | **Con un reloj de precisión repartido por la propia red** |
| **Latencia previsible** | **Con calidad de servicio y una red bien dimensionada** |
| **Entrega ordenada y completa** | **Con redundancia de camino y corrección de errores** |

**Ésa es la razón de ser de las dos normas que el examen pregunta**: **existen para poner de acuerdo a
los fabricantes en cómo se recupera cada garantía perdida.**

## 2. La familia SMPTE ST 2110

**La pregunta 30**: **el conjunto de estándares de la SMPTE que establece la norma para la transmisión
de audio, vídeo y datos auxiliares asociados a la media sobre redes IP es SMPTE 2110.** Ésa es la
respuesta oficial.

---

**Y las tres opciones falsas son el mismo número con las cifras cambiadas** —2001, 2100, 2010—, **lo
que convierte la pregunta en memoria de cuatro dígitos.** **El apoyo que sí funciona es recordar la
pareja**: **2110 para los flujos separados y 2022 para la redundancia**, que es la que el tema 9 del
específico de Técnica de Equipos explica.

**Lo que la familia hace, que es lo que da sentido al número**: **descompone la señal audiovisual en
flujos separados** —el vídeo por un lado, el audio por otro y los datos por otro— **y los vuelve a
juntar gracias a un reloj común.** **Eso es lo que la distingue de la interfaz digital serie, donde
todo iba incrustado en la misma trama.**

**Las partes de la familia, con sus títulos oficiales tomados del índice que la propia SMPTE publica:**

| Parte | Título oficial | De qué trata |
|---|---|---|
| **ST 2110-10** | «System Timing and Definitions» | **El reloj y las definiciones comunes** |
| **ST 2110-20** | «Uncompressed Active Video» | **El vídeo sin comprimir** |
| **ST 2110-30** | «PCM Digital Audio» | **El audio** ✔ |
| **ST 2110-40** | «SMPTE ST 291-1 Ancillary Data» | **Los datos auxiliares** |

## 3. La norma de audio sobre red

**La pregunta 63**: **el estándar de interoperabilidad establecido por la Sociedad de Ingeniería de
Audio para trabajar con señales de audio sobre IP y redes Ethernet es AES67.** Ésa es la respuesta
oficial.

---

**Y otra vez las opciones falsas son el mismo número desplazado** —AES65, AES66, AES68—, **de modo que
la pregunta vuelve a ser memoria.**

**El atajo que la hace memorizable**: **67 es el número que hay que retener, y va con 2110-30**,
porque **la parte de audio de la familia de la SMPTE se apoya en él.** **Las dos preguntas de este
punto son, en realidad, las dos caras de la misma pareja.**

**Qué aporta esa norma, en una línea**: **que sistemas de audio sobre red de fabricantes distintos se
entiendan entre sí**, frente a los protocolos propietarios que cada casa había desarrollado por su
cuenta.

**Y el aviso que este proyecto ya hizo en el temario de Sonido**: **el texto de la norma está tras un
muro de pago y no se ha leído.** **Lo que aquí se afirma de ella es lo que la respuesta oficial afirma
y lo que su presentación pública recoge.**

## 4. La arquitectura básica que el enunciado pide

**El enunciado habla de «arquitectura básica genérica», y ésta es la de cualquier instalación de
producción digital:**

| Bloque | Qué contiene |
|---|---|
| **Captación** | **Cámaras y micrófonos**, hoy con salida sobre red |
| **Encaminamiento** | **La red de conmutadores que sustituye a la matriz** |
| **Sincronismo** | **Un reloj maestro que reparte tiempo por la propia red** |
| **Producción** | **Mezcladores, servidores de repetición, grafismo** |
| **Almacenamiento** | **Servidores de vídeo y gestores de material** |
| **Control** | **Los sistemas que dicen qué se encamina a dónde** |

**Los dos rasgos que un informático debe entender de esa arquitectura, y son los que más problemas
dan:**

1. **La red de producción no es la red ofimática.** **Se separa físicamente o por redes lógicas**,
   porque **el tráfico de vídeo sin comprimir llena un enlace de diez gigabits con unas pocas
   señales.**
2. **El envío es a varios destinos, no a uno.** **Una cámara publica su flujo y quien lo necesita se
   suscribe**, lo que exige que la electrónica de red gestione bien la suscripción a grupos. **Una red
   que no la gestione inunda todos los puertos y se cae sola.**

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 30 | Estándares de la SMPTE para audio, vídeo y datos sobre redes IP | d) SMPTE 2110 ✔ **·** verificado en el índice de la SMPTE |
| 63 | Estándar de la AES para audio sobre IP y Ethernet | c) AES67 ✔ |

**Las dos respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.** **La primera
está verificada contra el índice público de la propia SMPTE**, volcado en este proyecto.

**El aviso de estudio**: **el punto entero cabe en dos números, 2110 y 67**, y **conviene aprenderlos
como pareja**, porque van juntos en la instalación y porque el examen los ha preguntado en el mismo
cuadernillo.

## 6. Trazabilidad

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Segundo: organismo de normalización** | **Índice público de la familia SMPTE ST 2110**, volcado en este proyecto | **Los títulos oficiales de sus partes**, citados literalmente. **Nada de su contenido interno** |

**Cuatro declaraciones expresas:**

1. **El articulado de la familia SMPTE ST 2110 no se ha consultado**: **sólo su índice público**, del
   que se toman los títulos de las partes tal como los publica la propia sociedad. **Eso basta para
   sostener la respuesta de la pregunta 30.**
2. **El texto de la norma AES67 está tras un muro de pago y no se ha leído**, y **lo mismo se
   declaró ya al escribir el temario específico de Sonido.** **Lo que el tema afirma de ella es lo
   que la respuesta oficial afirma**: que es el estándar de interoperabilidad de audio sobre red de
   esa sociedad.
3. **La arquitectura del epígrafe 4 no describe la instalación de RTVE**, que no se ha consultado.
   **Es la arquitectura genérica de una instalación de este tipo**, escrita a partir del propio
   enunciado del anexo.
4. **La afirmación de que el vídeo sin comprimir llena un enlace de diez gigabits con unas pocas
   señales es un orden de magnitud**, dado como aviso de dimensionado. **Ninguna respuesta depende de
   ella.**

**El resto del tema va como oficio y así se declara**: la tabla de lo que se gana y lo que se pierde
al pasar el vídeo a la red, el atajo de memoria de la pareja de números, y los dos rasgos que un
informático debe entender de una red de producción. **Nada de eso está en un boletín oficial ni en una
norma técnica de las consultadas más allá de lo citado**, y el tema no lo presenta como si lo
estuviera.
