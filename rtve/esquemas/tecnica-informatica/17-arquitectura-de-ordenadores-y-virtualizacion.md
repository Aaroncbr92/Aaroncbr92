# Esquema · Tema 17 del específico de Técnica Informática · Arquitectura de ordenadores y virtualización

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de sistemas · `[exam]` =
opciones del propio cuadernillo. **Siglas**: la unidad central de proceso (**CPU**), con su unidad
aritmético-lógica (**ALU**) y su unidad de control (**UC**); la memoria de acceso aleatorio (**RAM**)
y la de sólo lectura (**ROM**); la entrada y salida (**E/S**); la unidad de estado sólido (**SSD**);
el almacenamiento conectado a la red (**NAS**) y la red de área de almacenamiento (**SAN**); y el
conjunto redundante de discos independientes (**RAID**).

**Cabecera.** Enunciado: punto 20 del anexo, **de los más largos: siete asuntos** · **2 preguntas** ·
**ninguna lleva figura** · **las dos que han caído son de lo más elemental**: clasificar un
dispositivo y situar una generación. **Es un punto de leer, no de memorizar.**

<!-- indice -->

## Índice

- [Los bloques clásicos](#los-bloques-clásicos)
- [Periféricos](#periféricos)
- [Generaciones](#generaciones)
- [Almacenamiento](#almacenamiento)
- [Virtualización](#virtualización)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los bloques clásicos

| Bloque | Qué hace |
|---|---|
| **Unidad aritmético-lógica** | **Opera**: sumas, comparaciones, operaciones lógicas |
| **Unidad de control** | **Dirige**: busca la instrucción, la descodifica y ordena ejecutarla |
| **Memoria principal** | **Guarda datos e instrucciones**, las dos cosas en el mismo sitio |
| **Entrada y salida** | **Comunica con el exterior** |

- **EL RASGO QUE DEFINE EL MODELO**: **los datos y el programa comparten memoria.** **La alternativa
  —memorias separadas— se usa en microcontroladores**, no en el ordenador de propósito general.
- **LOS TRES BUSES**: **datos, direcciones y control.** **Con *n* líneas de direcciones se direccionan
  2 elevado a *n* posiciones**, la misma potencia de dos de las máscaras de red del tema 2.

## Periféricos

- **PREGUNTA 11** · `[exam]` · **El dispositivo de entrada y salida es el disco duro.**

| Clase | Qué hace | Ejemplos |
|---|---|---|
| **De entrada** | **Mete información** | **Teclado**, ratón, escáner, micrófono |
| **De salida** | **Saca información** | **Monitor**, impresora, altavoz |
| **De entrada y salida** | **Las dos cosas** | **Disco duro** ✔, memoria portátil, tarjeta de red, pantalla táctil |

- **LA REGLA QUE LA CONTESTA SIN DUDAR**: **preguntarse si el dispositivo puede hacer las dos cosas.**
  **Del disco se lee y en el disco se escribe**; **al monitor sólo se le escribe y del teclado sólo se
  lee.**
- **EL AVISO QUE EVITA EL ERROR MÁS COMÚN**: **una pantalla táctil sí es de entrada y salida, y un
  monitor corriente no.** **La misma familia de aparato cambia de cajón según lo que pueda hacer.**

## Generaciones

- **PREGUNTA 52** · `[exam]` · **Los circuitos integrados empezaron en la tercera generación.**

| Generación | Tecnología | Años, aproximados |
|---|---|---|
| **Primera** | **Válvulas de vacío** | **De 1940 a mediados de los cincuenta** |
| **Segunda** | **Transistores** | **De mediados de los cincuenta a los sesenta** |
| **Tercera** | **Circuitos integrados** ✔ | **Los sesenta y primeros setenta** |
| **Cuarta** | **Microprocesador**: integración a gran escala | **Desde los setenta** |
| **Quinta** | **Proceso en paralelo e inteligencia artificial** | **Desde los ochenta, y discutida** |

- **EL ATAJO QUE ORDENA LAS CUATRO PRIMERAS**: **cada generación integra más en menos espacio.** **La
  válvula ocupa una habitación, el transistor una placa, el circuito integrado una pastilla y el
  microprocesador mete la unidad central entera en una sola.**
- **LA ADVERTENCIA**: **la quinta no tiene definición pacífica** —se enuncia por su objetivo y no por
  una tecnología—, y por eso **el examen se detiene en la cuarta.**

## Almacenamiento

| Modelo | Cómo se ve desde el servidor | Por dónde va |
|---|---|---|
| **Local** | **Como discos propios** | **Dentro de la máquina** |
| **En red (NAS)** | **Como una carpeta compartida** | **Por la red de datos, con protocolo de ficheros** |
| **Red de almacenamiento (SAN)** | **Como un disco propio, aunque esté lejos** | **Por una red dedicada, con protocolo de bloques** |

- **LA DISTINCIÓN QUE SE PREGUNTA**: **el almacenamiento en red sirve ficheros y la red de
  almacenamiento sirve bloques.** **Por eso una base de datos exigente va sobre la segunda**:
  **necesita un disco, no una carpeta.**

| Nivel | Qué hace | Capacidad útil |
|---|---|---|
| **RAID 0** | **Reparte**: más velocidad, ninguna protección | **Toda** |
| **RAID 1** | **Duplica** | **La mitad** |
| **RAID 5** | **Reparte con paridad distribuida** | **La de *n* − 1 discos** |
| **RAID 6** | **Como el 5, con doble paridad** | **La de *n* − 2 discos** |

## Virtualización

- **LA IDEA, EN UNA LÍNEA**: **un solo equipo físico ejecuta varias máquinas completas, cada una con
  su sistema operativo, gracias a una capa que reparte el soporte físico.**

| Tipo | Dónde se instala | Para qué |
|---|---|---|
| **De tipo 1, nativo** | **Directamente sobre el soporte físico** | **Servidores de producción** |
| **De tipo 2, alojado** | **Sobre un sistema operativo ya instalado** | **Escritorio y pruebas** |

- **QUÉ GANA UNA ORGANIZACIÓN**: **aprovechamiento** —un servidor dedicado a un solo servicio pasa la
  mayor parte del tiempo ocioso—; **aislamiento** —si una máquina cae, las demás siguen—;
  **movilidad** —se copia, se mueve de anfitrión y se restaura como un fichero—; **instantáneas** —se
  vuelve al estado anterior a un cambio—.
- **EL CONTRASTE CON LOS CONTENEDORES, QUE EL SECTOR CONFUNDE**: **una máquina virtual lleva su propio
  sistema operativo completo; un contenedor comparte el núcleo del anfitrión y sólo empaqueta la
  aplicación y sus dependencias.** **Arranca en segundos y aísla menos.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 11 | Qué dispositivo es de entrada y salida | c) El disco duro ✔ |
| 52 | Generación de los circuitos integrados | c) Tercera ✔ |

**Las dos oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**el enunciado pide siete asuntos y el examen entró por los dos más elementales.** **De memoria, sólo
la tabla de generaciones**; **el resto se lee y se entiende, y su rendimiento por hora es bajo.**
