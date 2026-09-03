# Tema 17 del específico de Técnica Informática · Arquitectura de ordenadores y virtualización

Las siglas de este tema, presentadas de entrada: la unidad central de proceso (**CPU**), con su unidad
aritmético-lógica (**ALU**) y su unidad de control (**UC**); la memoria de acceso aleatorio (**RAM**) y
la de sólo lectura (**ROM**); la entrada y salida (**E/S**); la unidad de estado sólido (**SSD**,
*solid state drive*); el almacenamiento conectado a la red (**NAS**) y la red de área de
almacenamiento (**SAN**); el conjunto redundante de discos independientes (**RAID**); y el circuito
integrado, que el examen llama por su nombre común.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 20):
> «Arquitectura de Ordenadores. Componentes internos. Funciones. Periféricos. Sistemas de
> almacenamiento. Servidores de datos y de aplicaciones. Virtualización de servidores.»

**Dos preguntas.** **Y el enunciado es de los más largos del anexo**: **siete asuntos y dos
preguntas.** **Eso conviene decirlo porque marca dónde apretar: es un punto de leer, no de
memorizar.**

**Las dos que han caído son de lo más elemental**: **clasificar un dispositivo y situar una
generación.**

<!-- indice -->

## Índice

- [1. Los componentes y la arquitectura clásica](#1-los-componentes-y-la-arquitectura-clásica)
- [2. Cómo se clasifican los periféricos](#2-cómo-se-clasifican-los-periféricos)
- [3. Las generaciones de ordenadores](#3-las-generaciones-de-ordenadores)
- [4. Los sistemas de almacenamiento](#4-los-sistemas-de-almacenamiento)
- [5. La virtualización](#5-la-virtualización)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Los componentes y la arquitectura clásica

**El modelo que sigue explicando cualquier ordenador**, y que el examen da por sabido:

| Bloque | Qué hace |
|---|---|
| **Unidad aritmético-lógica** | **Opera**: sumas, comparaciones, operaciones lógicas |
| **Unidad de control** | **Dirige**: busca la instrucción, la descodifica y ordena ejecutarla |
| **Memoria principal** | **Guarda datos e instrucciones**, las dos cosas en el mismo sitio |
| **Entrada y salida** | **Comunica con el exterior** |

**Y el rasgo que define ese modelo**: **los datos y el programa comparten memoria.** **La alternativa
—memorias separadas para uno y otro— existe y se usa en microcontroladores**, pero **el ordenador de
propósito general sigue el primero.**

**Los tres buses que unen los bloques**, ya vistos en el tema 7 del específico de Técnica de Equipos:
**el de datos, el de direcciones y el de control.** **Con *n* líneas de direcciones se direccionan 2
elevado a *n* posiciones**, que es la misma potencia de dos de las máscaras de red del tema 2.

## 2. Cómo se clasifican los periféricos

**La pregunta 11**: **de los dispositivos enumerados, el que se considera de entrada y salida es el
disco duro.** Ésa es la respuesta oficial.

---

**La clasificación es de tres cajones y se decide por el sentido en que va la información:**

| Clase | Qué hace | Ejemplos |
|---|---|---|
| **De entrada** | **Mete información en el ordenador** | **Teclado**, ratón, escáner, micrófono |
| **De salida** | **Saca información del ordenador** | **Monitor**, impresora, altavoz |
| **De entrada y salida** | **Las dos cosas** | **Disco duro** ✔, memoria portátil, tarjeta de red, pantalla táctil |

**La regla que la contesta sin dudar**: **hay que preguntarse si el dispositivo puede hacer las dos
cosas.** **Del disco se lee y en el disco se escribe**; **al monitor sólo se le escribe y del teclado
sólo se lee.**

**Y el aviso que evita el error más común**: **una pantalla táctil sí es de entrada y salida**, y **un
monitor corriente no.** **La misma familia de aparato cambia de cajón según lo que pueda hacer.**

## 3. Las generaciones de ordenadores

**La pregunta 52**: **los circuitos integrados empezaron a usarse en la tercera generación.** Ésa es la
respuesta oficial.

---

**Las cinco generaciones, con la tecnología que las define**, que es la lista entera que hay que
llevar:

| Generación | Tecnología | Años, aproximados |
|---|---|---|
| **Primera** | **Válvulas de vacío** | **De 1940 a mediados de los cincuenta** |
| **Segunda** | **Transistores** | **De mediados de los cincuenta a los sesenta** |
| **Tercera** | **Circuitos integrados** ✔ | **Los años sesenta y primeros setenta** |
| **Cuarta** | **Microprocesador**: la integración a gran escala | **Desde los años setenta** |
| **Quinta** | **Proceso en paralelo e inteligencia artificial** | **Desde los años ochenta, y discutida** |

**El atajo de memoria que ordena las cuatro primeras**: **cada generación integra más en menos
espacio.** **La válvula ocupa una habitación, el transistor una placa, el circuito integrado una
pastilla y el microprocesador mete la unidad central entera en una sola.**

**Y la advertencia que conviene hacer**: **la quinta generación no tiene una definición pacífica.**
**Se enuncia por su objetivo y no por una tecnología concreta**, y por eso el examen se detiene en la
cuarta.

## 4. Los sistemas de almacenamiento

**El enunciado los pide y el examen no ha entrado.** **Los tres modelos que hay que distinguir:**

| Modelo | Cómo se ve desde el servidor | Por dónde va |
|---|---|---|
| **Almacenamiento local** | **Como discos propios** | **Dentro de la máquina** |
| **Almacenamiento en red (NAS)** | **Como una carpeta compartida** | **Por la red de datos, con protocolo de ficheros** |
| **Red de almacenamiento (SAN)** | **Como un disco propio, aunque esté lejos** | **Por una red dedicada, con protocolo de bloques** |

**La distinción que se pregunta**: **el almacenamiento en red sirve ficheros y la red de almacenamiento
sirve bloques.** **Por eso una base de datos exigente se pone sobre la segunda**: **necesita un disco,
no una carpeta.**

**Y los niveles RAID, que el tema 10 del específico de Técnica de Equipos calcula con números:**

| Nivel | Qué hace | Capacidad útil |
|---|---|---|
| **RAID 0** | **Reparte**: más velocidad y ninguna protección | **Toda** |
| **RAID 1** | **Duplica** | **La mitad** |
| **RAID 5** | **Reparte con paridad distribuida** | **La de *n* − 1 discos** |
| **RAID 6** | **Como el 5, con doble paridad** | **La de *n* − 2 discos** |

## 5. La virtualización

**Es lo último que el enunciado pide y lo que más ha cambiado la sala de servidores.**

**La idea, en una línea**: **un solo equipo físico ejecuta varias máquinas completas, cada una con su
propio sistema operativo, gracias a una capa que reparte el soporte físico entre ellas.**

**Los dos tipos de esa capa:**

| Tipo | Dónde se instala | Para qué |
|---|---|---|
| **De tipo 1, nativo** | **Directamente sobre el soporte físico** | **Servidores de producción** |
| **De tipo 2, alojado** | **Sobre un sistema operativo ya instalado** | **Escritorio y pruebas** |

**Qué gana una organización con ello, que es lo preguntable:**

- **Aprovechamiento**: **un servidor físico dedicado a un solo servicio pasa la mayor parte del
  tiempo ocioso.**
- **Aislamiento**: **si una máquina virtual cae, las demás siguen.**
- **Movilidad**: **una máquina virtual se copia, se mueve de anfitrión y se restaura como un
  fichero.**
- **Instantáneas**: **se puede volver al estado anterior a un cambio.**

**Y el contraste con los contenedores, porque el sector los confunde**: **una máquina virtual lleva su
propio sistema operativo completo; un contenedor comparte el núcleo del anfitrión y sólo empaqueta la
aplicación y sus dependencias.** **El contenedor arranca en segundos y aísla menos.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 11 | Qué dispositivo es de entrada y salida | c) El disco duro ✔ |
| 52 | Generación en que empezaron los circuitos integrados | c) Tercera ✔ |

**Las dos respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **el enunciado pide siete asuntos y el examen ha entrado por dos, los dos más
elementales.** **Lo que hay que llevar aprendido de memoria es la tabla de generaciones**; **el resto
del punto se lee y se entiende, y su rendimiento por hora es bajo.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **La arquitectura de bloques del epígrafe 1 y la clasificación de periféricos son teoría clásica
   de la informática**, presentadas como conocimiento común. **Coinciden con la respuesta oficial de
   la pregunta 11.**
2. **La tabla de generaciones y sus años son de uso corriente en la enseñanza de la materia**, y los
   años **se dan como aproximados**. **Lo que la pregunta 52 pide es la generación, no la fecha**, y
   ahí no hay discusión: **los circuitos integrados definen la tercera.**
3. **La afirmación de que la quinta generación no tiene definición pacífica es una observación del
   temario**, y **ninguna respuesta oficial depende de ella.**
4. **Los modelos de almacenamiento, los niveles RAID y los tipos de capa de virtualización son
   oficio de sistemas.** **Ninguna documentación de fabricante se ha consultado**, y **ninguna
   pregunta depende de ellos.**

**El resto del tema va como oficio y así se declara**: la regla para clasificar un periférico, el
aviso sobre la pantalla táctil, el atajo de que cada generación integra más en menos espacio, la
distinción entre servir ficheros y servir bloques y el contraste entre máquina virtual y contenedor.
**Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo
presenta como si lo estuviera.
