# Tema 1 del específico de Operador/a Informático · Sistemas de información, arquitectura de ordenadores y componentes del equipo

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 1 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Manual universitario abierto D. Bourgeois et al., *Information Systems for Business and Beyond* (2019); J. von Neumann, *First Draft of a Report on the EDVAC* (1945); documentación de Microsoft Learn (requisitos de Windows 11, ciclo de vida de Windows 10, equipos Copilot+); USB Implementers Forum; Intel (ley de Moore y Thunderbolt 5); NVM Express; apuntes de *Estructura de Computadores* de la Universidad Complutense de Madrid; notas *Computation Structures* del MIT; glosario de Arm; hoja de datos de Microchip (ATmega328P). Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las ediciones citadas, en línea el 05-10-2026 y el 06-10-2026 y leídas esos días |
| Extensión | 9.200 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); sistema de información
(SI, en inglés IS, *information system*); responsable de sistemas de información (CIO, *chief
information officer*); unidad central de proceso (CPU, *central processing unit*), con su unidad
aritmético-lógica (ALU) y su unidad de control (UC); unidad de procesamiento gráfico (GPU,
*graphics processing unit*) y neuronal (NPU, *neural processing unit*); memoria de acceso aleatorio
(RAM, *random-access memory*), de doble tasa de datos (DDR, *double data rate*) y de sólo lectura
(ROM, *read-only memory*); memoria de sólo lectura programable y borrable eléctricamente (EEPROM,
*electrically erasable programmable read-only memory*); entrada y salida (E/S); unidad de estado
sólido (SSD, *solid state drive*); interfaz NVM Express
(NVMe) sobre el bus PCI Express (PCIe); tarjeta de interfaz de red (NIC, *network interface card*);
bus serie universal (USB, *universal serial bus*) y su entrega de energía (USB PD, *power
delivery*); interfaz de firmware extensible unificada (UEFI, *unified extensible firmware
interface*) y sistema básico de entrada y salida (BIOS, *basic input/output system*); ordenador personal (PC, *personal computer*); el fabricante
International Business Machines (IBM); almacenamiento conectado a la red (NAS, *network attached
storage*) y red de área de almacenamiento (SAN, *storage area network*); módulo de
plataforma segura (TPM, *trusted platform module*); sistema en un chip (SoC, *system on a chip*);
modelo de controlador de pantalla de Windows (WDDM, *Windows Display Driver Model*); traducción de
direcciones de segundo nivel (SLAT, *second-level address translation*); billones de operaciones
por segundo (TOPS, *trillion operations per second*); ordenador de juego de instrucciones reducido
(RISC, *reduced instruction set computer*) y complejo (CISC, *complex instruction set computer*);
ciclos por instrucción (CPI); arquitectura del juego de instrucciones (ISA, *instruction set
architecture*); el contador de programa, que las fuentes abrevian PC (*program counter*) y que no
hay que confundir con el ordenador personal; niveles de caché L1, L2 y L3 (del inglés *level*); la familia de microcontroladores AVR de
Microchip, nombre comercial que el fabricante no desarrolla; canal de mantenimiento a largo plazo de Windows (LTSC,
*long-term servicing channel*); y la calculadora EDVAC, para la que von Neumann escribió el informe
de 1945.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 1): «Elementos constitutivos
> de un sistema de información: características y funciones. Arquitectura de ordenadores,
> componentes internos de los equipos microinformáticos y tecnologías actuales aplicables al puesto
> de usuario.»

Qué se puede preguntar: qué es un sistema de información y cuáles son sus cinco componentes (y el
sexto que se propone, las comunicaciones); cuáles de ellos son tecnología; cuáles son sus funciones
(recoger, procesar, almacenar, distribuir) y qué diferencia hay entre dato, información y
conocimiento; qué propiedades de la información hay que preservar; qué partes describió von Neumann
en 1945 y qué rasgo define su modelo; qué distingue la arquitectura de von Neumann de la Harvard, de
memorias separadas; qué buses unen los bloques y cuántas posiciones se direccionan con *n* líneas;
qué guarda el contador de programa y qué fases tiene el ciclo de instrucción; cómo se ordena la
jerarquía de memoria y en qué principio se apoya la caché; qué distingue RISC de CISC y a cuál
pertenece Arm; qué
tecnología define cada generación de ordenadores; qué dice la ley de Moore y cómo se revisó en
1975; qué es un bit, un byte y el tamaño de palabra; qué distingue el hardware del software y cómo
se clasifica el software; qué hace la CPU, qué es un núcleo, qué une la placa base, por qué la RAM
es volátil y qué la distingue del almacenamiento; qué es un SSD y qué es NVMe; cómo se clasifica un
periférico; qué componente mide su velocidad en qué unidad. Y del puesto actual: qué hardware exige
Windows 11 (procesador, memoria, disco, UEFI, arranque seguro, TPM 2.0), cuándo terminó el soporte
de Windows 10, qué es una NPU y un equipo Copilot+, qué velocidades tiene hoy el USB y cómo se
llaman al público, cuánta potencia entrega USB PD y qué aporta Thunderbolt 5. En la aplicación
práctica: decidir si un equipo dado puede pasar a Windows 11, clasificar un dispositivo, situar una
tecnología en su generación, calcular cuántas posiciones direcciona un bus o elegir el cable y el
puerto para conectar un monitor que cargue el portátil.

<!-- indice -->

## Índice

- [1. Elementos constitutivos de un sistema de información](#1-elementos-constitutivos-de-un-sistema-de-información)
  - [Qué es un sistema de información](#qué-es-un-sistema-de-información)
  - [Los cinco componentes](#los-cinco-componentes)
  - [El sexto componente: las comunicaciones](#el-sexto-componente-las-comunicaciones)
  - [Funciones](#funciones)
  - [Características](#características)
- [2. Arquitectura de ordenadores](#2-arquitectura-de-ordenadores)
  - [Lo digital: bit, byte y palabra](#lo-digital-bit-byte-y-palabra)
  - [El modelo de von Neumann](#el-modelo-de-von-neumann)
  - [La arquitectura Harvard](#la-arquitectura-harvard)
  - [Los buses](#los-buses)
  - [Los registros y el ciclo de instrucción](#los-registros-y-el-ciclo-de-instrucción)
  - [La jerarquía de memoria](#la-jerarquía-de-memoria)
  - [RISC y CISC](#risc-y-cisc)
  - [Hardware y software](#hardware-y-software)
  - [Las generaciones de ordenadores](#las-generaciones-de-ordenadores)
  - [La ley de Moore](#la-ley-de-moore)
- [3. Componentes internos de los equipos microinformáticos](#3-componentes-internos-de-los-equipos-microinformáticos)
  - [Visión de conjunto](#visión-de-conjunto)
  - [La CPU](#la-cpu)
  - [La placa base](#la-placa-base)
  - [La memoria](#la-memoria)
  - [El almacenamiento interno](#el-almacenamiento-interno)
  - [La tarjeta de red y las tarjetas de expansión](#la-tarjeta-de-red-y-las-tarjetas-de-expansión)
  - [Puertos, entrada y salida](#puertos-entrada-y-salida)
  - [Qué componentes deciden la velocidad del equipo](#qué-componentes-deciden-la-velocidad-del-equipo)
- [4. Tecnologías actuales aplicables al puesto de usuario](#4-tecnologías-actuales-aplicables-al-puesto-de-usuario)
  - [El suelo del puesto: el hardware que exige Windows 11](#el-suelo-del-puesto-el-hardware-que-exige-windows-11)
  - [El fin de Windows 10](#el-fin-de-windows-10)
  - [La NPU y los equipos Copilot+](#la-npu-y-los-equipos-copilot)
  - [Un solo puerto para todo: USB-C, USB4 y Thunderbolt](#un-solo-puerto-para-todo-usb-c-usb4-y-thunderbolt)
  - [Otras tecnologías del puesto, y dónde están](#otras-tecnologías-del-puesto-y-dónde-están)
  - [Aplicación práctica: ¿puede este equipo pasar a Windows 11?](#aplicación-práctica-puede-este-equipo-pasar-a-windows-11)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Elementos constitutivos de un sistema de información

### Qué es un sistema de información

No hay una definición legal: la que se usa es la de los manuales. El manual universitario abierto de
Bourgeois recoge tres, cada una con su autor, y advierte que se fijan en dos cosas distintas, los
componentes y el papel que cumplen en la organización (**«these definitions focus on two different
ways of describing information systems: the components that make up an information system and the
role those components play in an organization»**):

| Autor | Definición literal |
|---|---|
| K. C. Laudon y J. P. Laudon, *Management Information Systems*, 13.ª ed. (2014) | **«An information system (IS) can be defined technically as a set of interrelated components that collect, process, store, and distribute information to support decision making and control in an organization.»** |
| J. Valacich y C. Schneider, *Information Systems Today*, 4.ª ed. (2010) | **«Information systems are combinations of hardware, software, and telecommunications networks that people build and use to collect, create, and distribute useful data, typically in organizational settings.»** |
| K. C. Laudon y J. P. Laudon, 12.ª ed. (2012) | **«Information systems are interrelated components working together to collect, process, store, and disseminate information to support decision making, coordination, control, analysis, and visualization in an organization.»** |

En castellano, la primera: un sistema de información es, técnicamente, un conjunto de componentes
relacionados entre sí que recogen, procesan, almacenan y distribuyen información para apoyar la toma
de decisiones y el control en una organización. Es la que conviene llevar aprendida, porque de ella
salen a la vez los componentes («componentes relacionados»), las funciones («recoger, procesar,
almacenar, distribuir») y la finalidad («la toma de decisiones y el control»).

Un sistema de información no es sólo el ordenador. Bourgeois pone ejemplos cotidianos: la red
inalámbrica de un campus, la búsqueda en una biblioteca, las impresoras de un aula de ordenadores
(**«Wi-fi networks on your university campus, database search services in the learning resource
center, and printers in computer labs are good examples.»**).

### Los cinco componentes

**«Information systems can be viewed as having five major components: hardware, software, data,
people, and processes. The first three are technology. […] The last two components, people and
processes, separate the idea of information systems from more technical fields, such as computer
science.»**

Es decir: cinco componentes, de los que hardware, software y datos son tecnología, y personas y
procesos son lo que separa los sistemas de información de la informática como disciplina técnica.

| Componente | Qué es, según la fuente | Glosa |
|---|---|---|
| Hardware | **«Hardware is the tangible, physical portion of an information system – the part you can touch.»** | La parte física, la que se toca: ordenadores, teclados, unidades de disco, memorias flash |
| Software | **«Software comprises the set of instructions that tell the hardware what to do. Software is not tangible – it cannot be touched.»** | Dos categorías: **«Operating Systems and Application software»**; el sistema operativo **«provides the interface between the hardware and the Application software»** |
| Datos | **«You can think of data as a collection of facts.»** | Sueltos valen poco: **«Pieces of unrelated data are not very useful. But aggregated, indexed, and organized together into a database, data can become a powerful tool for businesses.»** |
| Personas | **«From the front-line user support staff, to systems analysts, to developers, all the way up to the chief information officer (CIO), the people involved with information systems are an essential element.»** | Desde el soporte de primera línea al usuario hasta el CIO |
| Procesos | **«A process is a series of steps undertaken to achieve a desired outcome or goal.»** | La serie de pasos para lograr un resultado; el objetivo final es **«to improve processes both internally and externally»** |

Ejemplo de examen: Microsoft Windows es software (del componente de tecnología «software», categoría
sistema operativo); un procedimiento de alta de usuarios es un proceso; el técnico que atiende la
incidencia es el componente «personas».

### El sexto componente: las comunicaciones

El manual añade que se ha propuesto un componente más, la comunicación en red: **«it has been
suggested that one other component should be added: communication.»** Admite que podría no existir
(**«the first personal computers were stand-alone machines that did not access the Internet»**),
pero hoy es raro el equipo que no se conecta a otro. Y explica por qué se separa aunque técnicamente
no sea nuevo: **«Technically, the networking communication component is made up of hardware and
software, but it is such a core feature of today's information systems that it has become its own
category.»** Si una pregunta habla de «seis componentes», el sexto es éste.

### Funciones

Las funciones salen de las definiciones. La de Laudon y Laudon da cuatro: **«collect, process,
store, and distribute»**. En el esquema clásico de entrada, proceso y salida:

| Función | Qué es | Ejemplo en el puesto |
|---|---|---|
| Recoger (entrada) | Captar los datos del exterior | El teclado, el escáner, un formulario |
| Procesar | Transformarlos en información útil | El cálculo de una hoja, una consulta a una base de datos |
| Almacenar | Conservarlos para usarlos después | El disco del equipo, la carpeta compartida de red |
| Distribuir (salida) | Hacer llegar la información a quien la necesita | La pantalla, la impresora, el correo |

La tercera definición añade fines a la toma de decisiones y el control: **«coordination, control,
analysis, and visualization»**. Y el manual resume el papel del sistema como una escalera de valor:
**«one of the roles of information systems is to take data and turn it into information, and then
transform that information into organizational knowledge.»** El dato es el hecho aislado; la
información, el dato organizado y con sentido; el conocimiento, lo que la organización aprende de
esa información.

### Características

Ninguna fuente leída da las «características» de un sistema de información como lista cerrada. Lo
que sí se deduce de las definiciones citadas, y así se presenta:

- Es un conjunto de componentes relacionados (**«interrelated components working together»**): no
  basta con tener las piezas; tienen que funcionar juntas.
- Mezcla tecnología, personas y procesos: sin las dos últimas sería sólo informática.
- Tiene una finalidad organizativa: apoyar decisiones y control **«in an organization»**.
- Los datos sólo valen si están organizados; sueltos, **«are not very useful»**.

Lo que un sistema de información debe preservar de la información que maneja son tres propiedades,
que son el punto de partida de toda la seguridad (tema 14):

- Confidencialidad: que la información sólo sea accesible a quien está autorizado.
- Integridad: que no se altere sin autorización.
- Disponibilidad: que esté accesible cuando se necesita.

## 2. Arquitectura de ordenadores

### Lo digital: bit, byte y palabra

Un ordenador es un dispositivo digital: **«A digital device processes electronic signals into
discrete values, of which there can be two or more.»** Lo analógico, en cambio, es continuo
(**«analog signals are continuous and can be represented by a smooth wave pattern»**). Muchos
aparatos trabajan con dos valores, el sistema binario, uno y cero.

| Término | Definición literal (Bourgeois, cap. 2) | Glosa |
|---|---|---|
| Bit | **«Each one or zero is referred to as a bit (a blending of the two words "binary" and "digit").»** | Dígito binario: un uno o un cero |
| Byte | **«A group of eight bits is known as a byte.»** | Ocho bits; el mayor número que cabe es 255 (11111111) |
| Palabra | **«The number of bits that can be processed by a computer's processor at one time is known as word size.»** | Los primeros PC procesaban 8 bits; **«Today's PCs can process 64 bits of data at a time which is where the term 64-bit processor comes from.»** |

El procesador de 64 bits no es una curiosidad histórica: Windows 11 lo exige (epígrafe 4).

### El modelo de von Neumann

El esquema que sigue explicando cualquier ordenador de propósito general es el que John von Neumann
describió en el *First Draft of a Report on the EDVAC*, fechado el 30 de junio de 1945 en la Moore
School of Electrical Engineering de la Universidad de Pensilvania. El informe divide la máquina en
partes específicas:

| Parte | Cómo la nombra el informe (§ 2) | Qué hace |
|---|---|---|
| CA, aritmética central | § 2.2: **«the first specific part: CA»** | Las operaciones aritméticas elementales |
| CC, control central | § 2.3: **«the second specific part: CC»** | El encadenamiento correcto de las operaciones: que las instrucciones, sean cuales sean, se ejecuten |
| M, memoria | § 2.5, la memoria total, tercera parte específica | Guardar resultados intermedios, instrucciones, tablas y datos |
| I, entrada | § 2.7: **«These organs form its input, the fourth specific part: I.»** | Pasar la información del medio exterior a la máquina |
| O, salida | § 2.8, quinta parte específica | Pasar los resultados de la máquina al exterior |

CA y CC juntas forman lo que el informe llama C, el antecedente de la CPU. Y el informe propone tratar
toda la memoria como un solo órgano: **«it is nevertheless tempting to treat the entire memory as one
organ»**, la misma memoria para las instrucciones que gobiernan el problema y para los datos. Ése es
el rasgo que define el modelo.

Traducido a los bloques con que se estudia hoy:

| Bloque | Qué hace |
|---|---|
| Unidad aritmético-lógica | Opera: sumas, comparaciones, operaciones lógicas |
| Unidad de control | Dirige: busca la instrucción, la descodifica y ordena ejecutarla |
| Memoria principal | Guarda datos e instrucciones, las dos cosas en el mismo sitio |
| Entrada y salida | Comunica con el exterior |

Los apuntes de
*Estructura de Computadores* de la Universidad Complutense de Madrid (UCM, tema 1, curso 2011-12)
mantienen el esquema como vigente: **«La estructura básica de un computador actual sigue siendo la
original de von Neumann, una máquina secuencial que ejecuta datos escalares»**, y le asignan cinco
características funcionales:

1. **«Organización lineal de la memoria»**.
2. **«Palabra de longitud fija.»**
3. **«Espacio único de direcciones.»**
4. **«Memoria única para datos e instrucciones sin diferenciar entre ambos.»**
5. **«Ejecución secuencial de las instrucciones salvo las de ruptura de secuencia»**.

A ese esquema básico, dicen los mismos apuntes, se han ido sumando tres aportaciones: el sistema de
interrupciones, la memoria caché y la memoria virtual. La interrupción **«permite la interrupción de
un programa en ejecución producida por una señal externa a la máquina»**, y con ello mejor
sincronización con la E/S y que más de un programa comparta la CPU.

### La arquitectura Harvard

La alternativa a la memoria única se llama arquitectura Harvard: memorias, y buses, separados para el
programa y para los datos. Un ejemplo documentado por su fabricante es el microcontrolador AVR de
Microchip (hoja de datos del ATmega328P, apartado 7, «AVR CPU Core»): **«In order to maximize
performance and parallelism, the AVR uses a Harvard architecture – with separate memories and buses
for program and data.»** La ventaja que alega es el solapamiento: **«While one instruction is being
executed, the next instruction is pre-fetched from the program memory.»** Mientras se ejecuta una
instrucción se trae ya la siguiente, porque leer el programa no compite con leer los datos.

| | Von Neumann | Harvard |
|---|---|---|
| Memoria | Una sola, para datos e instrucciones | Dos: una para el programa y otra para los datos |
| Buses | Comunes | Separados |
| Dónde se ve | El ordenador de propósito general | Microcontroladores como el AVR |

Que el ordenador de propósito general siga a von Neumann y el microcontrolador a Harvard es la
regla de oficio; las fuentes citadas sostienen cada lado, no la comparación como tal. También es
lectura de oficio ver un eco de Harvard dentro del propio PC: los apuntes de la UCM (tema 6)
presentan como opción de diseño las
**«Cachés independientes para datos e instrucciones: frente a cachés unificadas.»**

### Los buses

Los bloques se comunican por buses. Bourgeois lo define así: **«the term bus refers to the electrical
connections between different computer components»**, y la placa base **«provides much of the bus of
the computer»**. De qué depende su velocidad: **«the combination of how fast the bus can transfer
data and the number of data bits that can be moved at one time determine the speed.»** Es decir, de
la frecuencia y de la anchura (cuántos bits pasan a la vez).

Los tres buses que unen los bloques: el de datos, el de direcciones y el de control. Con *n* líneas
de direcciones se direccionan 2 elevado a *n* posiciones.

| Bus | Qué lleva |
|---|---|
| De datos | Los datos y las instrucciones que van y vienen entre la CPU, la memoria y la E/S |
| De direcciones | La posición de memoria o el dispositivo al que se quiere acceder |
| De control | Las órdenes y señales de sincronización: lectura, escritura, reloj, interrupciones |

Ejemplo de cálculo: con 16 líneas de direcciones se alcanzan 2<sup>16</sup> = 65.536 posiciones; con
32, 2<sup>32</sup> = 4.294.967.296 (4 GiB, si cada posición es un byte). Cada línea más duplica el espacio direccionable.

### Los registros y el ciclo de instrucción

Dentro de la CPU hay una pequeña memoria propia, los registros. Arm los define como **«Ultra-fast
memory locations used for temporary data storage and manipulation.»** Los apuntes de la UCM (tema
1) sitúan los registros en la ruta de datos del procesador, junto a la unidad aritmético-lógica, los
buses y la unidad de control: el procesador **«dispone de una ruta de datos constituida por un
conjunto de registros (REG.), una unidad aritmético-lógica (UAL), y unos buses de comunicación; y
una unidad de control, que es la encargada de generar las señales que gobiernan todos los
dispositivos.»**

Hay registros generales, que sirven de origen y destino de las operaciones, y registros con un
papel fijo. El que más se pregunta es el contador de programa. Las notas *Computation Structures*
del Instituto Tecnológico de Massachusetts (MIT, curso 6.004, cap. 14) lo describen así:

- Qué guarda: **«The contents of the program counter specify the main memory address containing the
  next coded instruction to be executed by the CPU.»** La dirección de la siguiente instrucción.
- Cómo avanza: **«With certain exceptions, the CPU increments the contents of the PC after the
  execution of each instruction»**; así se ejecutan en orden las instrucciones guardadas en
  posiciones consecutivas. Las excepciones son las instrucciones de ruptura de secuencia (saltos y llamadas) y las
  interrupciones.
- Qué pasa al llegar una interrupción (UCM, tema 8): **«La CPU salva automáticamente el estado en la
  pila, es decir, el contador de programa (PC) y el registro de estado (RE)»**, para poder volver
  al punto exacto en que se dejó el programa.

El trabajo de la unidad de control es un bucle. El MIT lo llama **«fetch/execute loop»**: buscar y
ejecutar, una instrucción tras otra, en el orden que marca el contador de programa. Arm lo
desglosa en cuatro fases (**«The CPU operates using a repetitive process called the instruction
cycle, consisting of four main stages»**):

| Fase | Literal de Arm | Qué pasa |
|---|---|---|
| Búsqueda | **«Fetch: Retrieves the next instruction from memory»** | Se trae de memoria la instrucción que señala el contador de programa |
| Descodificación | **«Decode: Interprets the instruction and determines the required resources»** | La unidad de control interpreta qué hay que hacer y con qué |
| Ejecución | **«Execute: Performs the specified operation»** | La unidad aritmético-lógica, u otra unidad, opera |
| Almacenamiento | **«Store: Writes the result back to memory or a register»** | El resultado se guarda en un registro o en memoria |

Ésta es la secuencia «busca, descodifica y ordena ejecutar» de la tabla de bloques de «El modelo
de von Neumann», con la escritura del resultado al final. Los procesadores actuales solapan las fases de
instrucciones distintas, la segmentación (en inglés *pipelining*): **«Pipelining: Breaks the
instruction cycle into overlapping stages for higher throughput»** (Arm). Los apuntes de la UCM
(tema 4) lo explican igual: **«La tarea de cada instrucción se divide en etapas, de tal forma que
en cada ciclo se ejecuta una etapa de una instrucción, simultaneándose la ejecución de etapas de
diferentes instrucciones.»**

### La jerarquía de memoria

Un ordenador no tiene una memoria, sino varias, de velocidad y capacidad distintas. Los apuntes de la
UCM (tema 5) lo dicen así: **«Las distintas memorias presentes en un computador se organizan de
forma jerárquica»**, y dibujan los niveles de arriba abajo:

| Nivel (UCM, tema 5) | Dónde está |
|---|---|
| Registros de la CPU | Dentro del procesador |
| Memoria caché (L1, L2, L3) | En el procesador o junto a él |
| Memoria principal | La RAM, en la placa base |
| Discos magnéticos | Almacenamiento interno |
| Cintas, CD-ROM, etc. | Almacenamiento externo o de archivo |

Hacia arriba aumenta la velocidad; hacia abajo, la capacidad. El mismo tema clasifica la memoria por
su ubicación: **«Interna (CPU): registros, cache(L1), cache(L2), cache(L3), memoria principal»** y
**«Externa (E/S): discos, cintas, etc.»** De más rápida a más lenta, por tanto: registros, caché,
RAM y disco.

La caché es el nivel que hace funcionar el conjunto. UCM, tema 6: **«La memoria caché es una memoria
pequeña y rápida que se interpone entre la CPU y la memoria principal para que el conjunto opere a
mayor velocidad.»** Funciona porque cada nivel guarda copia de lo que más probablemente se va a
pedir: **«En el nivel i+1 se ubica una copia de aquellos bloques del nivel i que tienen mayor
probabilidad de ser referenciados en el futuro inmediato»** (tema 5). Y esa probabilidad se puede
predecir por el principio de localidad de referencia, que tiene dos dimensiones (tema 6):

- Temporal: **«las palabras de memoria accedidas recientemente tienen una alta probabilidad de volver
  a ser accedidas en el futuro cercano.»** La explican sobre todo los bucles.
- Espacial: **«las palabras próximas en el espacio de memoria a las recientemente referenciadas tienen
  una alta probabilidad de ser también referenciadas en el futuro cercano.»** La explican la
  ejecución en orden de las instrucciones y el recorrido de estructuras de datos regulares.

Los niveles de caché se numeran desde el procesador: la de segundo nivel (L2) se pone entre la de
primer nivel (L1) y la memoria principal (UCM, tema 6, **«utilizando una caché intermedia o de
segundo nivel (L2) entre Mc (L1)»** y la memoria principal). Arm resume el papel de la caché en la
CPU actual: **«High-speed memory near the processor core that stores frequently accessed
instructions and data.»**

Aplicación práctica: un equipo lento al abrir varios programas a la vez suele tener poca RAM, y lo
que no cabe en ella se va al disco, el nivel más lento. Es la misma idea de la jerarquía que el
diagnóstico de lentitud del epígrafe 3.

### RISC y CISC

La arquitectura del juego de instrucciones (ISA) es la interfaz entre el hardware y el software:
**«it specifies an interface between hardware and software»** (MIT, cap. 14). Hay dos planteamientos,
que los apuntes de la UCM (tema 1) describen así:

- CISC: **«define un repertorio de instrucciones bastante complejo y numeroso, con muchos tipos de
  direccionamiento y muchos modos de control, pretendiendo reducir la distancia semántica que lo
  separa de los lenguajes de alto nivel, y facilitar así el diseño del compilador.»** Según los mismos apuntes, la
  microprogramación es la técnica de diseño de la unidad de control que facilita construir máquinas
  CISC.
- RISC: **«simplifica la complejidad y el número de instrucciones máquina, dejándolo reducido a un
  conjunto pequeño y rápido que cubre un porcentaje muy elevado del peso computacional de los
  programas.»** El compilador carga con el trabajo de combinar esas instrucciones simples.

La comparación, fila a fila, de la tabla de la UCM (tema 4, «Procesadores RISC y CISC»):

| | CISC | RISC |
|---|---|---|
| Operaciones | **«Muchas operaciones básicas y tipos de direccionamiento complejos»** | **«Pocas operaciones básicas y tipos de direccionamiento simples»** |
| Formato | **«Instrucciones largas y complejas con formatos muy diversos»**: descodificación compleja y lenta | Instrucciones de formato simple y tamaño fijo: descodificación simple y rápida |
| Instrucciones por programa y ciclos por instrucción | **«Pocas instrucciones por programa»**, con elevado número de ciclos por instrucción (CPI) | **«Muchas instrucciones por programa»**, con reducido CPI |
| Registros | **«Número limitado de registros de propósito general»** | **«Número elevado de registros»** |
| Acceso a memoria | Operaciones con operandos en registros y en memoria (la fuente lo abrevia «RM y MM») | Operaciones sólo entre registros (la fuente lo abrevia «RR»): arquitectura de **«carga/almacenamiento»**, en la que sólo cargar y almacenar acceden a memoria |

El MIT añade que muchas ISA CISC tienen instrucciones de longitud variable, lo que **«complicates
instruction fetch and decoding»**, y que el enfoque RISC se popularizó en los años ochenta. Arm, que
diseña procesadores RISC, lo resume así: **«A RISC processor executes one action per instruction.
By taking just one cycle to complete, operation execution time is optimized.»** Y del tamaño fijo:
**«Because the architecture uses a fixed length of instruction, it's easier to pipeline.»**

Por qué importa en el puesto: Arm es RISC. Lo dice su nombre (**«ARM, or "Advanced RISC Machine"
is a specific family of instruction set architecture that's based on reduced instruction set
architecture developed by Arm Ltd.»**) y lo dicen los apuntes de la UCM (tema 2: **«El procesador
ARM es un RISC con 16 registros de 32 bits»**). Arm añade que los procesadores de esa arquitectura son comunes en
móviles, tabletas, portátiles, consolas y equipos de sobremesa, y que RISC ofrece **«high performance per watt for battery
operated devices»**: buen rendimiento por vatio, que es lo que busca un portátil. El Snapdragon de
los equipos Copilot+ (epígrafe 4) es de arquitectura Arm.

### Hardware y software

Hardware es el conjunto de componentes físicos de un sistema informático. Se ordena en cinco
funciones:

| Función | Qué hace | Ejemplos |
|---|---|---|
| Proceso | Ejecuta las instrucciones | CPU, con su unidad de control y su unidad aritmético-lógica |
| Memoria principal | Guarda datos e instrucciones en uso | RAM (volátil), ROM (no volátil) |
| Almacenamiento | Guarda datos de forma persistente | Disco duro, SSD, memorias flash |
| Entrada | Introduce datos | Teclado, ratón, escáner, micrófono |
| Salida | Presenta resultados | Monitor, impresora, altavoces |

Software es el conjunto de programas, procedimientos y documentación que hacen funcionar el
hardware. Se clasifica en tres capas:

- Software de sistema: el sistema operativo, los controladores de dispositivo y las utilidades
  del sistema. Es el que hace utilizable la máquina.
- Software de programación: compiladores, intérpretes, entornos de desarrollo.
- Software de aplicación: el que resuelve tareas del usuario. La ofimática es software de
  aplicación: procesador de textos, hoja de cálculo, presentaciones, correo, base de datos.

Bourgeois simplifica en dos: **«Software can be broadly divided into two categories: operating systems
and application software.»** El sistema operativo **«is first loaded into the computer by the boot
program»** y cumple tres funciones: **«managing the hardware resources of the computer»**,
**«providing the user-interface components»** y **«providing a platform for software developers to
write applications.»** (El sistema operativo por dentro es el tema 5.)

Por su licencia se distingue el propietario —cuyo código no se distribuye y cuyo uso está
sujeto a una licencia— del libre —que permite usar, estudiar, modificar y redistribuir—, y el
freeware o el shareware, que son gratuitos o de prueba pero no necesariamente libres.
Gratis y libre no son sinónimos, y es la confusión más frecuente de este epígrafe.

### Las generaciones de ordenadores

Las cinco generaciones, con la tecnología que las define:

| Generación | Tecnología | Años, aproximados |
|---|---|---|
| Primera | Válvulas de vacío | De 1940 a mediados de los cincuenta |
| Segunda | Transistores | De mediados de los cincuenta a los sesenta |
| Tercera | Circuitos integrados | Los años sesenta y primeros setenta |
| Cuarta | Microprocesador: la integración a gran escala | Desde los años setenta |
| Quinta | Proceso en paralelo e inteligencia artificial | Desde los años ochenta, y discutida |

El atajo de memoria que ordena las cuatro primeras: cada generación integra más en menos
espacio. La válvula ocupa una habitación, el transistor una placa, el circuito integrado una
pastilla y el microprocesador mete la unidad central entera en una sola.

La quinta generación no tiene una definición pacífica: se enuncia por su objetivo y no por una
tecnología concreta.

La cuarta generación encaja con lo que dice Bourgeois de la primera CPU, de comienzos de los setenta: **«Since the first
CPU was created in the early 1970s, engineers have constantly worked to figure out how to shrink these
circuits and put more and more circuits onto the same chip – these are known as integrated
circuits.»** Y el primer microordenador que cita es el Altair 8800: **«In 1975, the first
microcomputer was announced on the cover of Popular Mechanics: the Altair 8800.»** En 1981 llegó el
IBM PC, con el sistema operativo de Microsoft (**«in 1981 IBM teamed with Microsoft, then just a
startup company, for their operating system software»**).

### La ley de Moore

El ritmo de esa integración tiene nombre. Intel la define así: **«Moore's Law is the observation that
the number of transistors on an integrated circuit will double every two years with minimal rise in
cost.»** Con su historia: **«Intel co-founder Gordon Moore predicted a doubling of transistors every
year for the next 10 years in his original paper published in 1965. Ten years later, in 1975, Moore
revised this to doubling every two years.»**

Tres matices preguntables, los tres de la misma página de Intel:

- Lo que se duplica son los transistores de un circuito integrado, no los circuitos ni la
  velocidad.
- No es una ley física: **«Moore's Law is not a scientific law (it's not a natural phenomenon).»**
- El artículo original se publicó en *Electronics Magazine* el 19 de abril de 1965 (**«published in
  Electronics Magazine, Volume 38, Issue 8, on April 19, 1965»**).

## 3. Componentes internos de los equipos microinformáticos

### Visión de conjunto

**«All personal computers consist of the same basic components: a Central Processing Unit (CPU),
memory, circuit board, storage, and input/output devices.»** Unidad central de proceso, memoria,
placa de circuito, almacenamiento y dispositivos de entrada y salida: los bloques de von Neumann
convertidos en piezas que se compran y se sustituyen. La fuente añade que casi todo dispositivo
digital tiene esas mismas piezas, de modo que estudiar el PC sirve para
todos.

### La CPU

**«The core of a computer is the Central Processing Unit, or CPU. It can be thought of as the
"brains" of the device. The CPU carries out the commands sent to it by the software and returns
results to be acted upon.»** Es el «cerebro»: ejecuta las órdenes del software y devuelve los
resultados. Los dos fabricantes principales para PC que nombra la fuente son Intel y AMD (**«Intel
and Advanced Micro Devices (AMD)»**).

- Velocidad de reloj: **«The speed ("clock time") of a CPU is measured in hertz. A hertz is defined
  as one cycle per second.»** Un gigahercio son mil millones de ciclos por segundo.
- Núcleos: **«today's CPU chips contain multiple processors. These chips, known as dual-core (two
  processors) or quad-core (four processors), increase the processing power of a computer by
  providing the capability of multiple CPUs all sharing the processing load.»** Cada núcleo es un
  procesador dentro del mismo chip; Windows 11 pide al menos dos (epígrafe 4).
- Caché: la CPU guarda los datos que más usa un programa para no tener que pedirlos a la RAM o al
  disco (**«the CPU contains a cache of frequently used data for a particular program»**).

### La placa base

**«The motherboard is the main circuit board on the computer. The CPU, memory, and storage
components, among other things, all connect into the motherboard.»** Es la placa principal: en ella
se conectan la CPU, la memoria y el almacenamiento, y por ella va buena parte del bus (epígrafe 2).
Su tamaño depende de lo compacto o ampliable que sea el equipo, y hoy integra lo que antes eran
tarjetas aparte: **«Most modern motherboards have many integrated components, such as network
interface card, video, and sound processing, which previously required separate components.»** Red,
vídeo y sonido vienen ya en la placa; una tarjeta gráfica o de red añadida es una ampliación, no una
necesidad.

### La memoria

**«When a computer boots, it begins to load information from storage into its working memory. This
working memory, called Random-Access Memory (RAM), can transfer data much faster than the hard disk.
Any program that you are running on the computer is loaded into RAM for processing.»**

- Es volátil: **«Another characteristic of RAM is that it is "volatile." This means that it can
  store data as long as it is receiving power. When the computer is turned off, any data stored in
  RAM is lost.»**
- Más RAM suele dar más velocidad: **«In most cases, adding more RAM will allow the computer to run
  faster.»**
- Se monta en módulos DDR, y el tipo lo decide la placa: **«RAM is generally installed in a personal
  computer through the use of a Double Data Rate (DDR) memory module. The type of DDR accepted into a
  computer is dependent upon the motherboard.»** Que un módulo de una generación DDR no sirva en la
  ranura de otra es regla de oficio: la fuente sólo dice que el tipo lo decide la placa.

La distinción que más se pregunta es memoria frente a almacenamiento. La RAM es rápida y
volátil: al apagar el equipo pierde su contenido. El almacenamiento es más lento y
persistente: conserva los datos sin corriente. Un equipo con poca RAM va lento; un equipo con
poco disco no cabe.

La ROM es la memoria no volátil de sólo lectura (tabla del epígrafe 2). El firmware que arranca el
equipo tiene que ser hoy UEFI: Windows 11 lo exige (**«System firmware: UEFI, Secure Boot
capable.»**, epígrafe 4). La relación entre UEFI y la BIOS y el arranque seguro son del tema 6; los
mensajes de error del arranque, del tema 2.

### El almacenamiento interno

- Disco duro: **«A hard disk is considered non-volatile storage because when the computer is turned
  off the data remains in storage on the disk, ready for when the computer is turned on.»** Platos
  que giran y un brazo de lectura y escritura que se coloca sobre la pista.
- Disco de estado sólido: **«The SSD performs the same function as a hard disk, namely long-term
  storage. Instead of spinning disks, the SSD uses flash memory that incorporates EEPROM (Electrically
  Erasable Programmable Read Only Memory) chips, which is much faster.»** Y es más fiable: **«SSDs are
  considered more reliable since there are no moving parts.»** Algunos equipos combinan los dos: el
  SSD para lo que más se usa, como el sistema operativo, y el disco duro para lo demás.
- NVMe: es la interfaz de los SSD que van sobre el bus PCI Express. El consorcio que la publica la
  describe como **«The register interface and command set for PCI Express technology attached
  storage with industry standard software available for numerous operating systems»** y añade:
  **«NVMe is widely considered the defacto industry standard for PCIe SSDs.»**

Los sistemas de almacenamiento, las memorias flash y la recuperación de datos son el tema 3.

### La tarjeta de red y las tarjetas de expansión

**«Initially, this was done by adding an expansion card to the computer that enabled the network
connection. These cards were known as Network Interface Cards (NIC). By the mid-1990s an Ethernet
network port was built into the motherboard on most personal computers.»** Después llegó la red
inalámbrica integrada (**«As wireless technologies began to dominate in the early 2000s, many
personal computers also began including wireless networking capabilities.»**). Hoy, por tanto, la
tarjeta de red de un puesto suele estar en la placa, cableada (Ethernet) e inalámbrica (Wi-Fi). Lo
mismo ocurre con el vídeo y el sonido (cita de la placa base). La detección y sustitución de averías
en tarjetas gráficas y de red es del tema 2; las redes, del 13.

### Puertos, entrada y salida

Los periféricos se conectan por puertos que **«generally are part of the motherboard and are
accessible outside the computer case»**. Antes cada aparato tenía su puerto; hoy casi todo va por
USB: **«Today, almost all devices plug into a computer through the use of a USB port. This port
type, first introduced in 1996, has increased in its capabilities, both in its data transfer rate
and power supplied.»** Junto al USB, la conexión inalámbrica de corto alcance Bluetooth para
teclados, altavoces o auriculares (**«computer keyboards, speakers, headsets»**). Las velocidades
actuales del USB están en el epígrafe 4; los conectores (USB, RJ45, VGA, DVI, HDMI, DisplayPort),
en el tema 4.

La clasificación es de tres cajones y se decide por el sentido en que va la información:

| Clase | Qué hace | Ejemplos |
|---|---|---|
| De entrada | Mete información en el ordenador | Teclado, ratón, escáner, micrófono |
| De salida | Saca información del ordenador | Monitor, impresora, altavoz |
| De entrada y salida | Las dos cosas | Disco duro, memoria portátil, tarjeta de red, pantalla táctil |

La regla que la contesta sin dudar: hay que preguntarse si el dispositivo puede hacer las dos
cosas. Del disco se lee y en el disco se escribe; al monitor sólo se le escribe y del teclado
sólo se lee.

Y el aviso que evita el error más común: una pantalla táctil sí es de entrada y salida, y un
monitor corriente no. La misma familia de aparato cambia de cajón según lo que pueda hacer.

### Qué componentes deciden la velocidad del equipo

**«The hardware components that contribute to the speed of a personal computer are the CPU, the
motherboard, RAM, and the hard disk. In most cases, these items can be replaced with newer, faster
components.»** La fuente da con qué se mide cada uno:

| Componente | Qué se mide | Unidad |
|---|---|---|
| CPU | Velocidad de reloj | GHz |
| Bus de la placa base | Velocidad a la que se mueven los datos por el bus | MHz |
| RAM | Tasa de transferencia | Megabytes por segundo |
| Disco duro | Tiempo de acceso (lo que tarda en localizar el dato) y tasa de transferencia | Milisegundos; megabits por segundo |

Aplicación práctica: un equipo que se arrastra al abrir varios programas a la vez apunta a falta de
RAM; uno que tarda en arrancar y abrir ficheros, al disco (el paso de disco duro a SSD es la mejora
que más se nota en ese caso). Es oficio, no dato de fuente; cómo medirlo con pruebas de rendimiento
es del tema 2.

## 4. Tecnologías actuales aplicables al puesto de usuario

### El suelo del puesto: el hardware que exige Windows 11

El sistema operativo de puesto vigente marca el mínimo de hardware. Microsoft lo publica así (página
actualizada el 14-07-2026): **«To install or upgrade to Windows 11, devices must meet the following
minimum hardware requirements:»**

| Componente | Requisito literal | En castellano |
|---|---|---|
| Procesador | **«Processor: 1 gigahertz (GHz) or faster with two or more cores on a compatible 64-bit processor or system on a chip (SoC).»** | 1 GHz o más, dos núcleos o más, 64 bits, procesador o SoC compatible |
| Memoria | **«Memory: 4 gigabytes (GB) or greater.»** | 4 GB de RAM o más |
| Almacenamiento | **«Storage: 64 GB or greater available disk space.»** | 64 GB libres o más |
| Gráfica | **«Graphics card: Compatible with DirectX 12 or later, with a WDDM 2.0 driver.»** | DirectX 12 y controlador WDDM 2.0 |
| Firmware | **«System firmware: UEFI, Secure Boot capable.»** | UEFI con arranque seguro |
| TPM | **«TPM: Trusted Platform Module (TPM) version 2.0.»** | TPM 2.0 |
| Pantalla | **«Display: High definition (720p) display, 9" or greater monitor, 8 bits per color channel.»** | 720p, 9 pulgadas o más, 8 bits por canal |

Y la conexión: **«Internet connectivity is necessary to perform updates, and to download and use some
features.»** La edición Home pide además cuenta Microsoft e internet en la primera configuración.

Algunas funciones piden más que el mínimo. Las que tocan al puesto de oficina:

- **«BitLocker to Go: requires a USB flash drive. This feature is available in Windows Pro and above
  editions.»**
- **«Client Hyper-V: requires a processor with second-level address translation (SLAT)
  capabilities. This feature is available in Windows Pro editions and greater.»**
- **«Microsoft Teams: requires video camera, microphone, and speaker (audio output).»**
- **«Windows Hello: requires a camera configured for near infrared (IR) imaging or fingerprint reader
  for biometric authentication.»** Sin sensor biométrico vale un PIN o una llave de seguridad.
- **«Snap: three-column layouts require a screen that is 1920 effective pixels or greater in
  width.»**

La instalación, la gestión de discos y la seguridad de Windows 11 son del tema 6.

### El fin de Windows 10

**«Windows 10 will reach end of support on October 14, 2025. The current version, 22H2, will be the
final version of Windows 10»**. Las ediciones LTSC siguen su propio calendario:
**«Existing LTSC releases will continue to receive updates beyond that date based on their specific
lifecycles.»** A la fecha de la convocatoria (24-IX-2026), un puesto con Windows 10 Home o Pro ya
está fuera del soporte que da esta página (las actualizaciones de seguridad extendidas no se han
leído: «Lo que este tema no da»); el puesto de referencia es Windows 11, y un equipo que no cumpla
sus requisitos es un equipo que hay que sustituir o ampliar.

### La NPU y los equipos Copilot+

La novedad de hardware del puesto es un tercer procesador junto a la CPU y la GPU. Microsoft
(página actualizada el 17-11-2025): **«Copilot+ PCs are a new class of Windows 11 hardware powered by
a high-performance Neural Processing Unit (NPU) — a specialized computer chip for AI-intensive
processes like real-time translations and image generation—that can perform more than 40 trillion
operations per second (TOPS).»**

- Qué hace: **«NPUs are designed specifically to execute the deep learning math operations that make
  up AI models.»** Ejecuta en el propio equipo las operaciones de los modelos de inteligencia
  artificial.
- Cómo convive con los otros: **«The NPU works in alignment with the CPU and GPU. Windows 11 assigns
  processing tasks to the most appropriate place in order to deliver fast and efficient
  performance.»**
- El umbral: 40 TOPS, más de 40 billones de operaciones por segundo (**«Many of the new Windows AI
  features require an NPU with the ability to run at 40+ TOPS»**).
- Las plataformas que cita: el Snapdragon X Elite de Qualcomm, de arquitectura Arm (RISC, epígrafe 2), y **«AMD Ryzen AI
  300 series and Intel Core Ultra 200V series.»**
- Para el técnico: **«For devices with NPUs, the Task Manager can now be used to view NPU resource
  usage.»** El Administrador de tareas muestra el uso de la NPU como el de la CPU o la GPU.

### Un solo puerto para todo: USB-C, USB4 y Thunderbolt

El puesto actual tiende a conectar datos, vídeo y carga por un mismo puerto. Hay que separar tres
cosas que el comercio mezcla: la versión fija la velocidad, el Type-C es el conector y PD es la
energía. Lo dice el USB-IF: **«USB 3.2 only defines the transfer rate of a product.»**; **«USB 3.2 is not USB
Type-C™, USB Standard-A, Micro-USB, or any other USB cable or connector.»**; **«USB 3.2 is not USB
Power Delivery or USB Battery Charging.»**

Velocidades. **«The USB4® and USB 3.2 specifications together identify five transfer rates – 80Gbps,
40Gbps, 20Gbps, 10Gbps, and 5Gbps.»** Los nombres que el USB-IF recomienda para el público son esas
cifras: «USB 80Gbps», «USB 40Gbps», «USB 20Gbps», «USB 10Gbps», «USB 5Gbps». Los nombres técnicos se
quedan en la especificación: **«USB4® Version 2.0, USB4® Version 1.0, USB 3.2, SuperSpeed Plus,
Enhanced SuperSpeed and SuperSpeed+ are defined in the USB specifications however these terms are not
intended to be used in product names, messaging, packaging or any other consumer-facing content.»**

| Velocidad | Nombre técnico | Nombre al público |
|---|---|---|
| 1,5 y 12 Mbit/s | Basic-Speed | — |
| 480 Mbit/s | USB 2.0, Hi-Speed | — |
| 5 Gbit/s | USB 3.2 Gen 1 | USB 5Gbps |
| 10 Gbit/s | USB 3.2 Gen 2 | USB 10Gbps |
| 20 Gbit/s | USB 3.2 Gen 2x2 (dos carriles de 10) o USB4 20Gbps | USB 20Gbps |
| 40 Gbit/s | USB4 40Gbps | USB 40Gbps |
| 80 Gbit/s | USB4, sobre cables certificados para 80 Gbit/s | USB 80Gbps |

Las fuentes de la tabla: **«The Basic-Speed USB Logo must be used with Basic-Speed (12 Mbps or 1.5
Mbps) Product. The Hi-Speed USB Logo must be used with Hi-Speed (480 Mbps) Product.»**; **«USB 3.2
identifies three transfer rates, USB 3.2 Gen 1 at 5Gbps, USB 3.2 Gen 2 at 10Gbps and USB 3.2 Gen 2x2
at 20Gbps.»**; **«USB4® identifies two transfer rates, USB4® 20Gbps at 20Gbps and USB4® 40Gbps at
40Gbps.»**; y, en la página vigente del USB4, **«up to 80 Gbps operation over 80 Gbps certified
cables»**. La especificación distingue un USB4 versión 1.0 y uno versión 2.0, pero las fuentes leídas
no atan cada velocidad a cada versión, y el tema no lo hace.

El USB4 nace de Thunderbolt y es compatible hacia atrás: **«Based on the Thunderbolt™ protocol
specification contributed by the Intel Corporation, USB4 doubles the maximum aggregate bandwidth of
USB and enables multiple simultaneous data and display protocols.»**; **«Backwards compatibility with
all previous versions of USB»**. Con aparatos de distinta generación, la conexión se ajusta a lo
que pueden los dos: **«the resulting connection scales to the best mutual capability of the devices
being connected»** (y en USB 3.2, **«will operate at lowest common speed capability»**).

El conector Type-C: **«Features reversible plug orientation and cable direction»**; entra en
cualquier posición y en cualquier sentido del cable.

La energía, USB PD: **«Announced in 2021, the USB PD Revision 3.1 specification is a major update to
enable delivering up to 240W of power over full featured USB Type-C® cable and connector. Prior to
this update, USB PD was limited to 100W using a solution based on 20V using USB Type-C cables rated at
5A.»** Hasta 240 W (antes, 100 W). Y la energía ya no va en un solo sentido: **«Power direction is no
longer fixed. This enables the product with the power (Host or Peripheral) to provide the power.»**
El ejemplo del puesto
lo da la propia fuente: **«A monitor with a supply from the wall can power, or charge, a laptop while
still displaying.»** Un solo cable entre monitor y portátil lleva la imagen y la carga.

Thunderbolt es la marca de Intel sobre esa misma base. **«Thunderbolt 4 always delivers 40 Gbps
speeds and data, video and power over a single connection, while Thunderbolt 5 promises speeds of
80/120 Gbps.»** De Thunderbolt 5 (nota de Intel de 12-09-2023): **«Thunderbolt 5 will deliver 80
gigabits per second (Gbps) of bi-directional bandwidth, and with Bandwidth Boost it will provide up to
120 Gbps for the best display experience.»**; **«Built on industry standards including USB4 V2,
DisplayPort 2.1 and PCI Express Gen 4; fully compatible with previous versions.»**

El detalle de conectores y cables (USB, RJ45, VGA, DVI, HDMI, DisplayPort) es del tema 4.

### Otras tecnologías del puesto, y dónde están

- Almacenamiento: SSD NVMe (epígrafe 3; tema 3).
- Impresión sin controlador del fabricante por IPP: tema 4.
- Escritorio virtual y aplicaciones virtualizadas: tema 10.
- Microsoft 365 y trabajo colaborativo: tema 11. Redes inalámbricas: tema 13. Seguridad del puesto
  y antivirus: tema 14.

### Aplicación práctica: ¿puede este equipo pasar a Windows 11?

Caso: un equipo de sobremesa con procesador de 64 bits de dos núcleos a 3 GHz, 8 GB de RAM, disco de
256 GB con 120 GB libres, firmware UEFI con arranque seguro desactivado y sin TPM 2.0 activo.

| Requisito | ¿Lo cumple? |
|---|---|
| Procesador: 1 GHz, dos núcleos, 64 bits, compatible | Sí en cifras; falta comprobar que el modelo sea «compatible», que es lo que pide el requisito (la herramienta de comprobación es del tema 6) |
| Memoria: 4 GB | Sí (8 GB) |
| Almacenamiento: 64 GB libres | Sí (120 GB) |
| UEFI con capacidad de arranque seguro | Sí: la exigencia es que sea capaz; se activa en el firmware |
| TPM 2.0 | No mientras no se active o se instale |

Conclusión: el equipo no pasa tal cual, y el obstáculo es el TPM, no la potencia. Antes de pedir
otro equipo, se mira en el firmware si trae un TPM 2.0 sin activar. El razonamiento y esa
comprobación son oficio; cada cifra es la del requisito de Microsoft citado arriba.

## Lo que este tema no da, y dónde está

- Una lista cerrada de «características» de un sistema de información: ninguna fuente leída la da. El
  tema deduce cuatro rasgos de las definiciones citadas y lo dice.
- Las generaciones de la memoria DDR (DDR5 incluida) y las del bus PCI Express con sus velocidades:
  las especificaciones de JEDEC y PCI-SIG no se han podido leer, y el manual citado está anticuado en
  ese punto (llega a DDR4). No se dan.
- La fuente de alimentación, la refrigeración y el chipset de la placa base: sin fuente leída.
- El registro de instrucción, el acumulador y el resto de registros especiales uno por uno, y la
  adscripción de la familia x86 de Intel y AMD a CISC: las fuentes leídas no lo dicen de forma
  expresa. El tema da sólo el contador de programa, el registro de estado y los registros generales.
- El coste por bit de cada nivel de la jerarquía de memoria: la fuente leída da velocidad y
  capacidad, no coste.
- La asignación de cada velocidad del USB4 a su versión 1.0 o 2.0, y la potencia de carga de
  Thunderbolt 4 y 5 en vatios: las fuentes leídas no lo dicen.
- El programa de actualizaciones de seguridad extendidas de Windows 10 tras el 14-10-2025: no se ha
  leído su página.
- Diagnóstico y averías de los componentes, mensajes de la BIOS y pruebas de rendimiento: tema 2.
  Almacenamiento, memorias flash, NAS, SAN y copias: tema 3. Periféricos de impresión,
  digitalización y visualización, y los conectores: tema 4. El sistema operativo por dentro: tema 5;
  Windows 11: tema 6. Virtualización: tema 10. Seguridad: tema 14.
- Qué equipos de puesto tiene la RTVA o CSRTV y con qué sistema operativo: no consta en ningún
  documento publicado.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| D. Bourgeois, J. L. Smith, S. Wang y J. Mortati, *Information Systems for Business and Beyond* (2019), edición actualizada el 1-8-2019, Saylor Foundation, licencia CC BY-NC 4.0; cap. 1 «What Is an Information System?», cap. 2 «Hardware» y cap. 3 «Software» | Las tres definiciones de sistema de información con sus autores (Laudon y Laudon 2014 y 2012; Valacich y Schneider 2010), los cinco componentes y el de comunicación, el papel dato-información-conocimiento, los ejemplos; dispositivo digital, bit, byte, palabra; componentes del PC, CPU, núcleos, caché, placa base, bus, RAM, DDR, disco duro, SSD, NIC, puertos, USB de 1996, Bluetooth, tabla de velocidad; primera CPU a comienzos de los setenta, Altair 8800, IBM PC de 1981; categorías y funciones del sistema operativo | 05-10-2026 |
| J. von Neumann, *First Draft of a Report on the EDVAC*, Moore School of Electrical Engineering, Universidad de Pensilvania, 30-6-1945 (texto por reconocimiento óptico del ejemplar de la Smithsonian Institution Libraries en Internet Archive; editor y título, de la ficha del ejemplar en Internet Archive) | Las cinco partes CA, CC, M, I y O (§ 2.2 a 2.8), C como unión de CA y CC (§ 2.6) y la memoria como un solo órgano (§ 2.5) | 05-10-2026; ficha, 06-10-2026 |
| Intel, «Moore's Law» (intel.com, newsroom, 18-9-2023) | Definición de la ley de Moore, 1965 y revisión de 1975, que no es una ley científica, publicación en *Electronics Magazine* | 05-10-2026 |
| Microsoft Learn, «Windows 11 requirements» (actualizada el 14-7-2026) | Requisitos mínimos de hardware, conexión, requisitos de funciones | 05-10-2026 |
| Microsoft Learn, ciclo de vida «Windows 10 Home and Pro» | Fin de soporte el 14-10-2025, 22H2 última versión, LTSC | 05-10-2026 |
| Microsoft Learn, «Develop AI applications for Copilot+ PCs» (actualizada el 17-11-2025) | NPU, 40 TOPS, reparto con CPU y GPU, plataformas, Administrador de tareas | 05-10-2026 |
| USB-IF, *USB Data Performance Language Usage Guidelines* (enero de 2024); *USB 3.2 Specification Language Usage Guidelines*; *USB4® Specification Language Usage Guidelines*; *USB Logo Usage Guidelines* (2024); páginas «USB4®», «USB Charger (USB Power Delivery)» y «USB Type-C® Cable and Connector Specification» | Cinco velocidades y sus nombres, nombres técnicos fuera del público, USB 3.2 y sus tres velocidades, versión distinta de conector y de energía, velocidades de USB 2.0, USB4 y su origen en Thunderbolt, compatibilidad, Type-C reversible, USB PD 3.1 hasta 240 W, sentido de la energía, monitor que carga el portátil | 05-10-2026 |
| Intel, nota de prensa «Intel Introduces Thunderbolt 5 Connectivity Standard» (12-9-2023); Thunderbolt Technology Community, página «Technology» | Thunderbolt 4 a 40 Gbit/s; Thunderbolt 5 a 80 y 120 Gbit/s, sobre USB4 V2, DisplayPort 2.1 y PCI Express Gen 4 | 05-10-2026 |
| NVM Express, página «About» | NVMe como interfaz y juego de órdenes del almacenamiento sobre PCI Express, estándar de hecho de los SSD PCIe | 05-10-2026 |
| Universidad Complutense de Madrid, Facultad de Informática, apuntes de *Estructura de Computadores* (J. J. Ruz): tema 1 «Introducción a la estructura de computadores», tema 2 «Formato de instrucciones y modos de direccionamiento», tema 5 «Organización de la memoria: memoria principal», tema 6 «Memoria Caché» y tema 8 «Organización de la Entrada/salida» (curso 2011-12); tema 4 «Rendimiento del procesador» (curso 2010-11) | Vigencia del esquema de von Neumann y sus cinco características, interrupciones, caché y memoria virtual; ruta de datos; CISC y RISC (tema 1) y su tabla comparativa y la segmentación (tema 4); ARM como RISC de 16 registros (tema 2); jerarquía de memoria, ubicación interna y externa, copia entre niveles (tema 5); caché, localidad temporal y espacial, segundo nivel, cachés separadas o unificadas (tema 6); contador de programa y registro de estado en la interrupción (tema 8) | Tema 4, 05-10-2026; los demás, 06-10-2026 |
| Massachusetts Institute of Technology, *Computation Structures* (curso 6.004), cap. 14 «Instruction Set Architectures», de S. Ward (computationstructures.org) | Contador de programa, su incremento, bucle de búsqueda y ejecución; la ISA como interfaz; CISC de longitud variable y RISC de los ochenta | 06-10-2026 |
| Arm, glosario: «What is RISC?» y «Central Processing Unit (CPU)» (arm.com/glossary) | RISC frente a CISC, una acción por instrucción en un ciclo, longitud fija, rendimiento por vatio, ARM como *Advanced RISC Machine*; registros, caché L1-L3, ciclo de instrucción en cuatro fases, segmentación | 06-10-2026 |
| Microchip, *ATmega48A/PA/88A/PA/168A/PA/328/P Data Sheet Complete*, DS40002061B (2020), apartado 7 «AVR CPU Core» | Arquitectura Harvard del AVR, con memorias y buses separados, y búsqueda anticipada de la siguiente instrucción | 06-10-2026 |

Las fuentes están en inglés salvo las cifras: las citas van en negrita en su lengua y la explicación
en castellano es del tema. El texto del informe de von Neumann procede de un reconocimiento óptico
con erratas; sólo se citan en negrita los fragmentos que salen limpios, y las partes M y O se dan en
redonda con su apartado. Bourgeois está anticuado en algunos datos (núcleos de modelos concretos,
generaciones DDR, USB 3.1) que el tema no recoge; y su formulación de la ley de Moore (circuitos
integrados en lugar de transistores) se sustituye por la de Intel.

Oficio sin fuente detrás, y así se declara: la traducción del modelo de von Neumann a los cuatro
bloques de hoy; la comparación entre von Neumann y Harvard como regla (cada lado tiene su fuente, la
comparación no) y el parecido de las cachés separadas con Harvard; la columna «Dónde está» de la jerarquía de memoria y el ejemplo práctico de
lentitud; la incompatibilidad entre generaciones de módulos DDR; los tres buses y lo que lleva cada uno (la fórmula 2
elevado a *n* y los cálculos son aritmética); la tabla de cinco funciones del hardware y la
distinción entre memoria y almacenamiento; la clasificación del software en tres capas y por
licencia; la tabla de generaciones con sus años aproximados, el atajo de memoria y la advertencia
sobre la quinta; la clasificación de periféricos en tres clases, la regla para decidirla y el aviso
de la pantalla táctil; los ejemplos de funciones en el puesto; las tres propiedades de
confidencialidad, integridad y disponibilidad (desarrolladas, también sin cita, en el tema 14); el diagnóstico de lentitud
por RAM o por disco; y el razonamiento del caso de Windows 11.
