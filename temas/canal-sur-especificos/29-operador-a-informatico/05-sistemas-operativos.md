# Tema 5 del específico de Operador/a Informático · Sistemas operativos

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 5 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Manual universitario R. H. Arpaci-Dusseau y A. C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces*, Universidad de Wisconsin-Madison, versión 1.10 (el capítulo de interbloqueos, versión 1.20); apuntes de curso de J. Bell, Universidad de Illinois en Chicago, sobre el manual de Silberschatz, Galvin y Gagne; documentación de Microsoft Learn (Win32 y controladores de Windows); documentación del núcleo Linux; *The Linux Kernel Module Programming Guide*; página oficial de MINIX 3. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las ediciones citadas, en línea el 05-10-2026 y leídas ese día (lo añadido en el remate, el 06-10-2026) |
| Extensión | 12.800 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); sistema operativo (SO);
unidad central de proceso (CPU, *central processing unit*); entrada y salida (E/S, en inglés I/O);
interfaz de programación de aplicaciones (API, *application programming interface*); bloque de
control de proceso (PCB, *process control block*) y de hilo (TCB, *thread control block*); contador
de programa (PC, *program counter*); acceso directo a memoria (DMA, *direct memory access*); rutina
de servicio de interrupción (ISR, *interrupt service routine*); el estándar de interfaz portable de
sistemas operativos (POSIX); los algoritmos de planificación primero en llegar, primero en ser
servido (FIFO, *first in, first out*, o FCFS, *first come, first served*), primero el trabajo más
corto (SJF, *shortest job first*), primero el de menor tiempo hasta terminar (STCF, *shortest
time-to-completion first*, también PSJF, *preemptive shortest job first*), turno rotatorio (RR,
*round robin*) y colas multinivel con realimentación (MLFQ, *multi-level feedback queue*); la
planificación multiprocesador de cola única (SQMS, *single-queue multiprocessor scheduling*) y de
colas múltiples (MQMS, *multi-queue multiprocessor scheduling*); el planificador del núcleo Linux
de plazo virtual más temprano entre los elegibles (EEVDF, *earliest eligible virtual deadline
first*), con su plazo virtual (VD, *virtual deadline*), y su antecesor, el planificador completamente
justo (CFS, *completely fair scheduler*); la distribución de software de Berkeley (BSD, *Berkeley
Software Distribution*), familia de sistemas Unix; Windows NT, nombre de producto de Microsoft; y el
manual que sirve de fuente principal, *Operating Systems: Three Easy Pieces* (OSTEP).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 5): «Sistemas operativos:
> conceptos generales, componentes funcionales y estructura; gestión de procesos, algoritmos de
> planificación, concurrencia, multitarea y multiprogramación.»

Qué se puede preguntar: qué es un sistema operativo y por qué se le llama máquina virtual y gestor de
recursos; qué es un sistema de tiempo real y uno distribuido; qué distingue el modo núcleo del modo usuario y cómo se pasa de uno a otro; qué es una
llamada al sistema; qué funciones tiene el sistema y qué hace el gestor de entrada y salida; qué es
un controlador de dispositivo, una interrupción y el acceso directo a memoria; qué distingue un
núcleo monolítico de un micronúcleo y qué es un módulo del núcleo Linux; qué es un proceso, en qué
estados puede estar y qué transiciones hay entre ellos; qué guarda el PCB; qué hacen `fork()`,
`exec()` y `wait()`; qué distingue un hilo de un proceso, y los hilos de usuario de los de núcleo
(modelos muchos a uno, uno a uno y muchos a muchos); qué es un cambio de contexto; qué hacen los
planificadores de largo, medio y corto plazo y el despachador; qué miden el tiempo de retorno, el de
respuesta y el de espera, la utilización de la CPU y la productividad; cómo funcionan FIFO, SJF,
STCF, RR, la planificación por prioridades y MLFQ, cuál es apropiativo y cuál no, qué es el efecto
convoy y qué es el envejecimiento; qué rango de prioridades usa Windows y qué planificador usa hoy
Linux; qué es una condición de carrera, una sección crítica y la exclusión mutua; qué hacen los
algoritmos de Dekker y Peterson; qué es un cerrojo, un semáforo, una variable de condición y un
monitor; qué distingue la memoria compartida del paso de mensajes; qué son los problemas del
productor-consumidor, de los lectores-escritores y de los filósofos; cuáles son las cuatro
condiciones del interbloqueo y cómo se previene, se evita o se detecta; qué es la inanición; qué
distingue la multitarea apropiativa de la cooperativa, y la multiprogramación del tiempo compartido.
En la aplicación práctica: calcular tiempos medios de retorno, de respuesta y de espera de un conjunto de
trabajos con cada algoritmo, seguir el estado de un proceso a lo largo de una operación de E/S y
reconocer en un caso las condiciones de un interbloqueo.

<!-- indice -->

## Índice

- [1. Conceptos generales](#1-conceptos-generales)
  - [Qué es un sistema operativo](#qué-es-un-sistema-operativo)
  - [Los modos núcleo y usuario](#los-modos-núcleo-y-usuario)
  - [La llamada al sistema](#la-llamada-al-sistema)
  - [Mecanismo y política](#mecanismo-y-política)
  - [Clases de sistemas operativos](#clases-de-sistemas-operativos)
- [2. Componentes funcionales](#2-componentes-funcionales)
  - [Las funciones del sistema](#las-funciones-del-sistema)
  - [El gestor de entrada y salida](#el-gestor-de-entrada-y-salida)
- [3. Estructura](#3-estructura)
  - [El núcleo](#el-núcleo)
  - [Tipos de núcleo](#tipos-de-núcleo)
- [4. Gestión de procesos](#4-gestión-de-procesos)
  - [Qué es un proceso](#qué-es-un-proceso)
  - [Los estados de un proceso](#los-estados-de-un-proceso)
  - [El bloque de control de proceso](#el-bloque-de-control-de-proceso)
  - [Las operaciones sobre procesos](#las-operaciones-sobre-procesos)
  - [Hilos](#hilos)
  - [El cambio de contexto](#el-cambio-de-contexto)
- [5. Algoritmos de planificación](#5-algoritmos-de-planificación)
  - [Qué decide el planificador y cómo se mide](#qué-decide-el-planificador-y-cómo-se-mide)
  - [Los niveles de planificación y el despachador](#los-niveles-de-planificación-y-el-despachador)
  - [Planificación apropiativa y no apropiativa](#planificación-apropiativa-y-no-apropiativa)
  - [FIFO o FCFS](#fifo-o-fcfs)
  - [SJF, primero el trabajo más corto](#sjf-primero-el-trabajo-más-corto)
  - [STCF, primero el de menor tiempo restante](#stcf-primero-el-de-menor-tiempo-restante)
  - [Round Robin, el turno rotatorio](#round-robin-el-turno-rotatorio)
  - [Ejercicio de aplicación](#ejercicio-de-aplicación)
  - [Planificación por prioridades](#planificación-por-prioridades)
  - [Colas multinivel con realimentación (MLFQ)](#colas-multinivel-con-realimentación-mlfq)
  - [Planificación con varios procesadores](#planificación-con-varios-procesadores)
  - [Cómo planifica Windows](#cómo-planifica-windows)
  - [Cómo planifica Linux](#cómo-planifica-linux)
- [6. Concurrencia](#6-concurrencia)
  - [El problema: la condición de carrera](#el-problema-la-condición-de-carrera)
  - [Cerrojos](#cerrojos)
  - [Soluciones por programa: Dekker y Peterson](#soluciones-por-programa-dekker-y-peterson)
  - [Semáforos](#semáforos)
  - [Variables de condición](#variables-de-condición)
  - [Monitores](#monitores)
  - [Memoria compartida y paso de mensajes](#memoria-compartida-y-paso-de-mensajes)
  - [Los problemas clásicos](#los-problemas-clásicos)
  - [El interbloqueo](#el-interbloqueo)
  - [La inanición](#la-inanición)
- [7. Multitarea y multiprogramación](#7-multitarea-y-multiprogramación)
  - [De los lotes a la multiprogramación](#de-los-lotes-a-la-multiprogramación)
  - [El tiempo compartido](#el-tiempo-compartido)
  - [Multitarea apropiativa y cooperativa](#multitarea-apropiativa-y-cooperativa)
  - [Concurrencia y paralelismo](#concurrencia-y-paralelismo)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Conceptos generales

### Qué es un sistema operativo

El manual de referencia de este tema define el sistema operativo por lo que hace. Hay un conjunto de
programas que se encarga de que sea fácil ejecutar programas (incluso de que parezca que se ejecutan
muchos a la vez), de que los programas compartan la memoria y de que se comuniquen con los
dispositivos; ese conjunto de programas (**«That body of software»**) **«is called the operating system
(OS)»**, **«as it is in charge of making sure the system operates correctly and efficiently in an
easy-to-use manner»** (se llama sistema operativo porque se encarga de que el sistema funcione
de forma correcta, eficiente y fácil de usar). El manual recuerda en nota que otros nombres antiguos del sistema
operativo fueron **«the supervisor or even the master control program»** (el supervisor o el programa
de control maestro).

Tres maneras de describirlo, las tres del mismo manual:

| Visto como | Por qué | Fuente |
|---|---|---|
| Máquina virtual | Toma un recurso físico (el procesador, la memoria, un disco) y lo transforma en una forma virtual más general, potente y fácil de usar: **«we sometimes refer to the operating system as a virtual machine»** | OSTEP, cap. 2 |
| Biblioteca estándar | Ofrece interfaces que los programas llaman: **«A typical OS, in fact, exports a few hundred system calls that are available to applications»**; por eso se dice que **«the OS provides a standard library to applications»** | OSTEP, cap. 2 |
| Gestor de recursos | Varios programas comparten la CPU, la memoria y los discos: **«the OS is sometimes known as a resource manager»**, y su papel es gestionar esos recursos de forma eficiente, justa o con otros objetivos | OSTEP, cap. 2 |

La técnica general con que el sistema consigue todo eso es la virtualización: **«the OS takes a
physical resource (such as the processor, or memory, or a disk) and transforms it into a more
general, powerful, and easy-to-use virtual form of itself»**. El manual organiza la materia en tres
grandes piezas, que son las tres preguntas que vuelven en este tema: la virtualización (de la CPU y
de la memoria), la concurrencia y la persistencia (los datos que sobreviven en disco).

Los objetivos de diseño que el manual enumera:

- Construir abstracciones que hagan el sistema cómodo y fácil de usar.
- Dar alto rendimiento, que el manual formula como **«minimize the overheads of the OS»** (reducir el
  coste añadido del propio sistema, en tiempo y en espacio).
- Dar protección **«between applications, as well as between the OS and applications»** (entre
  aplicaciones, y entre el sistema y las aplicaciones). Su principio es el aislamiento: **«isolating
  processes from one another is the key to protection»**.
- Fiabilidad: el sistema debe funcionar sin parar, porque **«when it fails, all applications running
  on the system fail as well»**.
- Y, según el uso, eficiencia energética, seguridad (que el manual llama **«an extension of
  protection, really»**) y movilidad.

### Los modos núcleo y usuario

La división que atraviesa todo el tema es la del modo núcleo y el modo usuario.

| Modo | Qué puede hacer | Qué corre ahí |
|---|---|---|
| Núcleo | Todo: acceder al soporte físico y a cualquier memoria | El núcleo y sus controladores |
| Usuario | Sólo lo suyo, y pedir el resto por llamada al sistema | Los programas |

La razón de que existan los dos: un error de un programa no puede llevarse el sistema por
delante. Cuando un programa necesita algo del soporte físico, no lo toca: lo pide.

El manual lo describe así. El código que corre en modo usuario **«is restricted in what it can do»**:
por ejemplo, un proceso en modo usuario no puede lanzar peticiones de E/S, y si lo intenta el
procesador genera una excepción y el sistema probablemente lo termina. En cambio, el modo núcleo es
el modo en que corre el sistema operativo, y en él **«code that runs can do what it likes, including
privileged operations such as issuing I/O requests and executing all types of restricted
instructions»** (el código puede hacer lo que quiera, incluidas las operaciones privilegiadas).

Microsoft lo explica igual para Windows, con un matiz sobre los controladores:

- **«Un procesador en un equipo que ejecuta Windows funciona en dos modos diferentes: el modo de
  usuario y el modo kernel . El procesador cambia entre estos modos en función del tipo de código
  que se está ejecutando. Las aplicaciones funcionan en modo de usuario. Los componentes principales
  del sistema operativo funcionan en modo kernel. Aunque muchos controladores funcionan en modo
  kernel, algunos pueden funcionar en modo de usuario.»**
- En modo usuario, **«Al iniciar una aplicación en modo de usuario, Windows crea un proceso para
  ella»**, con **«un espacio de direcciones virtuales privado»**; por eso **«una aplicación no puede
  modificar los datos de otra aplicación»** y **«si una aplicación se bloquea, no afecta a otras
  aplicaciones ni al sistema operativo»**.
- En modo núcleo, **«Todo el código que se ejecuta en modo kernel comparte un único espacio de
  direcciones virtuales»**, de modo que **«Si un controlador en modo kernel se bloquea, provoca que
  todo el sistema operativo se bloquee.»**

Es decir: «el núcleo y sus controladores» de la tabla es la regla general, pero en Windows hay
controladores que corren en modo usuario.

### La llamada al sistema

Cómo pide un programa lo que no puede hacer él mismo. **«To execute a system call, a program must
execute a special trap instruction. This instruction simultaneously jumps into the kernel and raises
the privilege level to kernel mode»** (para hacer una llamada al sistema, el programa ejecuta una
instrucción especial de *trap*, que salta al núcleo y a la vez eleva el nivel de privilegio a modo
núcleo). Hecho el trabajo, el sistema ejecuta **«a special return-from-trap instruction»**, que vuelve
al programa y a la vez baja el privilegio a modo usuario.

Dos detalles que se preguntan:

- Dónde salta el *trap*. No lo decide el programa: **«The kernel does so by setting up a trap table at
  boot time»** (el núcleo prepara una tabla de *traps* durante el arranque, que la máquina hace en
  modo privilegiado).
- Por qué una llamada al sistema parece una llamada a función. Porque lo es, por fuera: el programa
  llama a una función de la biblioteca de C, como `open()` o `read()`, y dentro de ella va **«the
  famous trap instruction»**.

La diferencia con una llamada a procedimiento, en palabras del manual: **«a system call transfers
control (i.e., jumps) into the OS while simultaneously raising the hardware privilege level»**. Las
llamadas al sistema nacieron en el ordenador Atlas.

### Mecanismo y política

Un principio de diseño que el manual pone en el centro del estudio de los procesos: separar el
mecanismo de la política. El mecanismo responde a una pregunta de *cómo* (cómo se hace un cambio de
contexto); la política, a una pregunta de *cuál*: **«The policy provides the answer to a which
question; for example, which process should the operating system run right now?»**. Separarlos
permite cambiar de política sin rehacer el mecanismo. En este tema, el cambio de contexto es
mecanismo (epígrafe 4) y los algoritmos de planificación son políticas (epígrafe 5).

### Clases de sistemas operativos

Los sistemas se clasifican también por el entorno para el que están hechos. La sucesión de los
sistemas por lotes, los multiprogramados y los de tiempo compartido está en el epígrafe 7; las
demás clases que se preguntan, con su fuente:

| Clase | Rasgo | Fuente |
|---|---|---|
| De tiempo compartido | Varios usuarios y varias tareas a la vez: **«A time-sharing ( multi-user multi-tasking ) OS»** | Apuntes de J. Bell, cap. 1 |
| De tiempo real | Cada trabajo tiene un plazo: **«a job absolute deadline d_j, which is the time within which the job should be finished»**. Los dispositivos de control de procesos los exigen: **«Process control devices require real-time ( interrupt driven ) OSes. Response time can be critical for many such devices.»** | Núcleo Linux, «Deadline Task Scheduling»; apuntes de J. Bell, cap. 1 |
| Empotrados | Integrados en aparatos: **«Embedded into devices such as automobiles, climate control systems, process control, and even toasters and refrigerators.»** | Apuntes de J. Bell, cap. 1 |
| Distribuidos y de red | **«Distributed Systems consist of multiple, possibly heterogeneous, computers connected together via a network and cooperating in some way, form, or fashion.»** La visión que el sistema tiene de la red va **«from just a special form of file access to complex well-coordinated network operating systems»** (desde un simple acceso a ficheros hasta los sistemas operativos de red) | Apuntes de J. Bell, cap. 1 |

Lo que distingue al tiempo real es la garantía de plazo, no la rapidez. La documentación del núcleo
Linux dice que su política de planificación por plazos, `SCHED_DEADLINE`, es **«particularly suited for periodic or
sporadic real-time tasks that need guarantees on their timing behavior, e.g., multimedia, streaming,
control applications, etc.»** (tareas periódicas o esporádicas que necesitan garantías de tiempo,
como el multimedia o el *streaming*); y explica que la configuración PREEMPT_RT
**«transforms the Linux kernel into a real-time kernel»**. Con las políticas de
tiempo real de Linux, como `SCHED_FIFO`, **«When a task with a real-time policy becomes runnable,
the scheduler immediately selects it for execution if it has a higher priority than the currently
running task.»**

## 2. Componentes funcionales

### Las funciones del sistema

El sistema operativo se describe por los recursos que gestiona. Sus cinco funciones:

| Función | De qué se ocupa |
|---|---|
| Gestión de procesos | Quién se ejecuta, cuándo y durante cuánto |
| Gestión de memoria | Qué hay en memoria y dónde |
| Gestión de ficheros | Cómo se organizan los datos en el almacenamiento |
| Gestión de entrada y salida | Cómo se habla con los dispositivos |
| Protección y seguridad | Quién puede hacer qué |

Cada fila tiene su apoyo en el manual:

- Procesos: la virtualización de la CPU. **«By running one process, then stopping it and running
  another, and so forth, the OS can promote the illusion that many virtual CPUs exist when in fact
  there is only one physical CPU (or a few)»** (ejecutando un proceso, parándolo y ejecutando otro,
  el sistema crea la ilusión de que hay muchas CPU virtuales). Lo desarrollan los epígrafes 4 y 5.
- Memoria: el sistema hace que muchos programas accedan a la vez a sus propias instrucciones y datos,
  **«thus sharing memory»**. Cada proceso tiene su espacio de direcciones (epígrafe 4).
- Ficheros: **«The file system is the part of the OS in charge of managing persistent data»** (el
  sistema de ficheros es la parte del sistema que gestiona los datos persistentes).
- Entrada y salida: el sistema **«provides a standard and simple way to access devices through its
  system calls»**; lo desarrolla el apartado siguiente.
- Protección: el objetivo de diseño del aislamiento, visto en el epígrafe 1.

### El gestor de entrada y salida

Qué hace el gestor de entrada y salida, en tres líneas: recibe la petición del programa, la
convierte en órdenes concretas para el controlador del dispositivo, y devuelve el resultado.
Su valor está en que el programa no tiene que saber qué disco ni qué impresora hay debajo: pide
«escribe estos bytes» y el gestor se entiende con el aparato.

Es, por tanto, la pieza que comunica los dispositivos con los programas del modo usuario. No hace
operaciones aritméticas (eso es la unidad aritmético-lógica del procesador), no reparte el
procesador entre procesos (eso es el planificador) y no es la pila de red. En Windows tiene nombre
propio: Microsoft llama **«administrador de E/S»** al componente del modo núcleo que exporta, por
ejemplo, la rutina `IoCreateDevice` con la que un controlador crea un objeto de dispositivo.

**El controlador de dispositivo.** El problema que resuelve es mantener el sistema neutral respecto a
cada aparato. **«At the lowest level, a piece of software in the OS must know in detail how a device
works. We call this piece of software a device driver, and any specifics of device interaction are
encapsulated within.»** (En el nivel más bajo, una pieza del sistema debe saber en detalle cómo
funciona el dispositivo; esa pieza es el controlador, y encierra todo lo específico del aparato.) En
Linux, el sistema de ficheros no sabe qué clase de disco hay debajo: envía lecturas y escrituras de
bloques a una capa de bloques genérica, que las encamina al controlador que toca. Dos datos del
manual: en los estudios del núcleo Linux, **«over 70% of OS code is found in device drivers»**, y los
controladores, a menudo escritos fuera del equipo del núcleo, **«are a primary contributor to kernel
crashes»** (son una causa principal de caídas del núcleo).

**El diálogo con el aparato.** Un dispositivo sencillo presenta tres registros: **«a status register,
which can be read to see the current status of the device; a command register, to tell the device to
perform a certain task; and a data register to pass data to the device, or get data from the
device»** (de estado, de orden y de datos). Hay tres formas de llevar ese diálogo:

| Técnica | Cómo funciona | Cuándo conviene |
|---|---|---|
| Sondeo (*polling*) | El sistema lee una y otra vez el registro de estado hasta que el aparato está listo: **«we call this polling the device (basically, just asking it what is going on)»** | Dispositivos rápidos; el manual advierte que las interrupciones **«only really make sense for slow devices»** |
| Interrupciones | El sistema lanza la petición, duerme al proceso y pasa a otro; al acabar, el aparato **«will raise a hardware interrupt, causing the CPU to jump into the OS at a predetermined interrupt service routine (ISR) or more simply an interrupt handler»** | Dispositivos lentos: permiten solapar cálculo y E/S |
| Acceso directo a memoria (DMA) | **«A DMA engine is essentially a very specific device within a system that can orchestrate transfers between devices and main memory without much CPU intervention»**; al terminar, el controlador de DMA lanza una interrupción | Transferencias grandes, para no ocupar la CPU copiando datos |

Un riesgo de las interrupciones que el manual nombra es el bloqueo activo (*livelock*): una
avalancha de interrupciones deja al sistema ocupado sólo en atenderlas, y para ese caso el manual
aconseja volver a veces al sondeo. Y una optimización: la agrupación (*coalescing*), en la que el
aparato espera un poco para entregar varias interrupciones en una y rebajar así el coste de
atenderlas, a cambio de más latencia.

Y dos formas de que el procesador hable con los registros del aparato: las instrucciones de E/S
explícitas, **«The first, oldest method (used by IBM mainframes for many years)»**, y la E/S
mapeada en memoria, en la que **«the hardware makes device registers available as if they were memory
locations»**. **«both approaches are still in use today»**.

## 3. Estructura

### El núcleo

El núcleo es la parte del sistema que corre en modo núcleo. Microsoft lo define en la documentación
de Windows: **«El kernel de un sistema operativo implementa la funcionalidad básica de la que depende
todo lo demás del sistema operativo. El kernel de Microsoft Windows proporciona operaciones básicas de
bajo nivel, como programar hilos o enrutamiento de interrupciones de hardware.»** Y en Windows **«el
sistema operativo Windows incluye componentes de modo de usuario y modo kernel»**.

La función del núcleo en un sistema Unix o Linux es controlar los procesos, la memoria y la
administración de dispositivos. No lo es gestionar la interfaz gráfica, que en Unix es un programa
más en modo usuario (un servidor gráfico); ni dar los servicios de red, que prestan demonios en modo
usuario aunque la pila de protocolos esté en el núcleo; ni comunicar usuarios por terminales, que
hacen programas de usuario.

### Tipos de núcleo

La clasificación clásica separa los sistemas por cuánto meten en modo núcleo:

| Tipo | Qué mete dentro | Ejemplo con fuente |
|---|---|---|
| Monolítico | Procesos, memoria, ficheros, red y controladores, todo en modo núcleo y en un mismo espacio | Linux (con módulos) |
| Micronúcleo | Lo mínimo; el resto, servicios en modo usuario | MINIX 3; GNU Hurd y Zircon, el núcleo de Fuchsia de Google |

Las fuentes:

- Micronúcleo. La página oficial de MINIX 3: **«It is based on a tiny microkernel running in kernel
  mode with the rest of the operating system running as a number of isolated, protected, processes in
  user mode.»** (Se basa en un micronúcleo diminuto que corre en modo núcleo, y el resto del sistema
  corre como procesos aislados y protegidos en modo usuario.) La guía de programación de módulos del
  núcleo Linux da otros dos: **«Two notable examples of microkernels include the GNU Hurd and the
  Zircon kernel of Google’s Fuchsia.»**
- Monolítico y modular. La misma guía define el módulo: **«A Linux kernel module is precisely defined
  as a code segment capable of dynamic loading and unloading within the kernel as needed. These modules
  enhance kernel capabilities without necessitating a system reboot.»** Sin módulos, **«the prevailing
  approach leans toward monolithic kernels, requiring direct integration of new functionalities into
  the kernel image»**, lo que obliga a recompilar el núcleo y reiniciar. El módulo **«shares the
  kernel’s codespace rather than having its own»**, de modo que un fallo del módulo es un fallo del
  núcleo, y la guía añade que eso **«applies to any operating system utilizing a monolithic kernel»**;
  en cambio, en los micronúcleos **«modules are allocated their own code space»**.

Linux es monolítico y a la vez modular: los controladores se cargan y descargan en caliente,
que es lo que permite añadir soporte físico sin recompilar.

La ventaja de cada diseño se sigue de lo anterior, y es oficio: el micronúcleo aísla los fallos (un
servicio caído en modo usuario no tumba el núcleo); el monolítico evita el coste de que los
componentes se hablen a través de fronteras de modo.

Windows no entra en la tabla: las fuentes leídas describen sus componentes de modo núcleo y de modo
usuario (con controladores en uno y otro modo), pero no lo clasifican; Microsoft sólo descarta una
de las dos casillas: **«El término microkernel no se aplica al kernel actual que se usa en el
sistema operativo Windows.»**

## 4. Gestión de procesos

### Qué es un proceso

La definición del manual: **«a process is simply a running program»** (un proceso es un programa en
ejecución). La de Microsoft: **«Una aplicación consta de uno o varios procesos. Un proceso , en los
términos más sencillos, es un programa en ejecución. Uno o varios subprocesos se ejecutan en el
contexto del proceso. Un subproceso es la unidad básica a la que el sistema operativo asigna tiempo
de procesador.»** (Microsoft traduce *thread* por «subproceso»; en el resto del tema se dice «hilo».)

El programa es lo que está en el disco; el proceso es ese programa vivo, con su estado. Ese estado
(**«machine state»**, el estado de máquina) tiene tres partes, según el resumen del manual: **«the
contents of memory in its address space, the contents of CPU registers (including the program
counter and stack pointer, among others), and information about I/O (such as open files which can
be read or written)»**. Es decir:

- La memoria que el proceso puede direccionar, que se llama su espacio de direcciones (**«address
  space»**).
- Los registros de la CPU, entre ellos el contador de programa, que **«tells us which instruction of
  the program will execute next»**, y el puntero de pila.
- La información de E/S, como la lista de ficheros abiertos.

Para crear un proceso, el sistema carga el código y los datos estáticos del programa en el espacio
de direcciones (los sistemas antiguos, de una vez, **«eagerly»**; los modernos, por partes según se
necesitan, **«lazily»**), reserva la pila (y puede reservar memoria para el montículo), prepara la E/S (en Unix, cada proceso nace
con tres descriptores abiertos: entrada, salida y error estándar) y salta al punto de entrada del
programa.

### Los estados de un proceso

En una vista simplificada, **«a process can be in one of three states»**:

| Estado | Definición del manual |
|---|---|
| En ejecución (*running*) | **«In the running state, a process is running on a processor. This means it is executing instructions.»** |
| Listo (*ready*) | **«In the ready state, a process is ready to run but for some reason the OS has chosen not to run it at this given moment.»** |
| Bloqueado (*blocked*) | **«In the blocked state, a process has performed some kind of operation that makes it not ready to run until some other event takes place. A common example: when a process initiates an I/O request to a disk, it becomes blocked and thus some other process can use the processor.»** |

Las transiciones (figura 4.2 del manual):

| De | A | Nombre en el manual | Qué la provoca |
|---|---|---|---|
| Listo | En ejecución | **«Scheduled»** | El sistema lo elige |
| En ejecución | Listo | **«Descheduled»** | El sistema lo retira (por ejemplo, se le acaba el turno) |
| En ejecución | Bloqueado | **«I/O: initiate»** | Lanza una E/S u otra espera |
| Bloqueado | Listo | **«I/O: done»** | Termina la E/S o llega el suceso esperado |

Lo que no hay: no se pasa de bloqueado a en ejecución directamente (primero se vuelve a listo,
**«and potentially immediately to running again, if the OS so decides»**), ni de listo a bloqueado
(sólo se bloquea quien está ejecutando y pide algo).

Hay más estados que esos tres. Un estado inicial, mientras el proceso se crea, y uno final en que el
proceso ha terminado pero aún no se ha limpiado, que en Unix se llama **«zombie state»** (zombi): sirve
para que el padre recoja el código de retorno del hijo con `wait()`, y entonces el sistema libera
sus estructuras.

Con esos dos estados añadidos sale el modelo de cinco estados que dan los apuntes de curso sobre el
manual de Silberschatz: **«Processes may be in one of 5 states»**, que son nuevo (**«New - The
process is in the stage of being created.»**), listo, en ejecución, en espera (**«Waiting»**, el
bloqueado de la tabla anterior) y terminado (**«Terminated - The process has completed.»**). Los
apuntes avisan de que **«Some systems may have other states besides the ones listed here.»**

### El bloque de control de proceso

Para seguir todos los procesos, el sistema mantiene una lista de procesos (**«The process list (also
called the task list)»**). Cada entrada es una estructura con la información de un proceso, que se
llama bloque de control de proceso: **«Process Control Block (PCB), a fancy way of talking about a C
structure that contains information about each process (also sometimes called a process
descriptor)»**. El ejemplo del manual (la estructura `proc` del sistema docente xv6) guarda, entre
otros datos, los registros guardados del proceso cuando no se ejecuta, su estado, su identificador,
su proceso padre, sus ficheros abiertos y su directorio actual. Los registros guardados son los que
permiten reanudarlo: **«by restoring these registers (i.e., placing their values back into the actual
physical registers), the OS can resume running the process»**.

### Las operaciones sobre procesos

Lo que todo sistema ofrece, según el manual:

| Operación | Qué hace |
|---|---|
| Crear (**«Create»**) | Crear un proceso nuevo, por ejemplo al escribir una orden en el intérprete o hacer doble clic en un icono |
| Destruir (**«Destroy»**) | Detener por la fuerza un proceso que no termina por sí solo |
| Esperar (**«Wait»**) | Esperar a que un proceso termine |
| Control diverso (**«Miscellaneous Control»**) | Por ejemplo, suspender un proceso y reanudarlo después |
| Estado (**«Status»**) | Consultar cuánto tiempo lleva en ejecución o en qué estado está |

En Unix, las llamadas que lo hacen:

- **«The fork() system call is used in UNIX systems to create a new process. The creator is called
  the parent; the newly created process is called the child.»** El hijo es una copia casi idéntica del
  padre.
- **«The wait() system call allows a parent to wait for its child to complete execution.»**
- **«The exec() family of system calls allows a child to break free from its similarity to its parent
  and execute an entirely new program.»**
- El intérprete de órdenes usa las tres para lanzar cada orden, y separar `fork()` de `exec()` es lo
  que le permite redirigir la entrada y la salida o montar tuberías sin tocar el programa que lanza.
- **«Process control is available in the form of signals»** (el control de procesos se ejerce también
  mediante señales, que pueden detener, reanudar o terminar un proceso).

### Hilos

**«thread is very much like a separate process, except for one difference: they share the same
address space and thus can access the same data.»** (Un hilo es muy parecido a un proceso aparte, con
una diferencia: los hilos de un proceso comparten el espacio de direcciones y por tanto los mismos
datos.) Cada hilo tiene sus propios registros y su contador de programa, y su propia pila. Su
estado se guarda en un bloque de control de hilo (TCB). El cambio de contexto entre hilos de un mismo
proceso se parece al cambio entre procesos, con una diferencia: **«the address space remains the same
(i.e., there is no need to switch which page table we are using)»**.

Para qué sirven los hilos, según el manual, hay al menos dos razones:

- Paralelismo (**«parallelism»**): repartir el trabajo de un programa entre varias CPU. Convertir un
  programa de un solo hilo en uno que reparte así el trabajo se llama paralelización
  (**«parallelization»**).
- No quedarse parado por una E/S lenta: mientras un hilo espera, el planificador ejecuta otro. **«Threading
  enables overlap of I/O with other activities within a single program, much like multiprogramming did
  for processes across programs»**.

Windows nombra además otras dos piezas: la fibra, **«Una fibra es una unidad de ejecución
que la aplicación debe programar manualmente. Las fibras se ejecutan en el contexto de los
subprocesos que los programan.»**, y el grupo de subprocesos, **«una colección de subprocesos de
trabajo que ejecutan de forma eficaz devoluciones de llamada asincrónicas en nombre de la
aplicación»**.

**Hilos de usuario y de núcleo.** Los apuntes de curso sobre el manual de Silberschatz distinguen
dos clases: **«User threads are supported above the kernel, without kernel support.»** (los de usuario
se gestionan por encima del núcleo, sin su apoyo), y **«Kernel
threads are supported within the kernel of the OS itself.»**; además, **«All modern OSes support
kernel level threads»**. Los hilos de usuario tienen que corresponderse con hilos de núcleo, y hay
tres modelos:

| Modelo | Cómo es | Ventaja e inconveniente |
|---|---|---|
| Muchos a uno | **«many user-level threads are all mapped onto a single kernel thread»** | La gestión la hace la biblioteca en espacio de usuario, **«which is very efficient»**; pero **«if a blocking system call is made, then the entire process blocks»**, y el proceso no puede repartirse entre varias CPU. Los apuntes dicen que **«few systems continue to do so today»** |
| Uno a uno | **«creates a separate kernel thread to handle each user thread»** | Resuelve los dos problemas anteriores, pero con más coste, y **«Most implementations of this model place a limit on how many threads can be created.»** Los apuntes ponen como ejemplo Linux |
| Muchos a muchos | **«multiplexes any number of user threads onto an equal or smaller number of kernel threads»** | Sin límite de hilos para el usuario, una llamada bloqueante no bloquea todo el proceso y el proceso se reparte entre procesadores. Una variante es el modelo de dos niveles (**«two-tier model»**), que admite a la vez muchos a muchos y uno a uno |

### El cambio de contexto

Para cambiar de proceso, el sistema tiene que recuperar el control de la CPU, y hay dos maneras de
recuperarlo (epígrafe 7): esperar a que el proceso haga una llamada al sistema, o forzarlo con una
interrupción de reloj. Recuperado el control, decide el planificador: **«a decision has to be made:
whether to continue running the currently-running process, or switch to a different one. This
decision is made by a part of the operating system known as the scheduler»**. Si decide cambiar, el
sistema hace un cambio de contexto: **«all the OS has to do is save a few register values for the
currently-executing process (onto its kernel stack, for example) and restore a few for the
soon-to-be-executing process (from its kernel stack)»** (guarda los registros del proceso que sale y
restaura los del que entra).

El cambio de contexto tiene un coste, y no sólo el de guardar y restaurar registros: los programas
acumulan estado en las cachés de la CPU y otros elementos del procesador, y al cambiar de trabajo ese
estado se pierde, **«which may exact a noticeable performance cost»**.

En Windows, los pasos del cambio de contexto son, literalmente:

1. **«Guarde el contexto del subproceso que el procesador ha adelantado o generado voluntariamente.»**
2. **«Si el subproceso permanece en un estado listo, colóquelo al final de la cola para su nivel de
   prioridad.»**
3. **«Busque la cola de prioridad más alta que contiene subprocesos listos.»**
4. **«Quite el subproceso en el encabezado de la cola, restaure su contexto y reanude la ejecución.»**

Y sus causas más comunes: **«El quantum de un subproceso ha expirado y otro subproceso con al menos la
misma prioridad está lista.»**; **«Un subproceso con una prioridad más alta está listo para
ejecutarse.»**; **«Un subproceso en ejecución debe esperar.»** No reciben tiempo de procesador,
cualquiera que sea su prioridad, los hilos creados suspendidos, los detenidos con `SuspendThread` o
`SwitchToThread` y los que esperan un objeto de sincronización o una entrada.

## 5. Algoritmos de planificación

### Qué decide el planificador y cómo se mide

El planificador es la política que decide qué proceso listo pasa a ejecutarse. Para comparar
políticas hacen falta métricas, y el manual usa dos:

| Métrica | Definición | Fórmula |
|---|---|---|
| Tiempo de retorno (*turnaround time*) | **«The turnaround time of a job is defined as the time at which the job completes minus the time at which the job arrived in the system.»** | T retorno = T finalización − T llegada |
| Tiempo de respuesta (*response time*) | **«the time from when the job arrives in a system to the first time it is scheduled»** | T respuesta = T primera ejecución − T llegada |

El tiempo de retorno es una métrica de rendimiento; la otra gran preocupación es la equidad
(*fairness*), y las dos chocan: **«Performance and fairness are often at odds in scheduling»**. El
tiempo de respuesta nació con los sistemas de tiempo compartido, cuando los usuarios se sentaron
ante un terminal y pidieron respuesta interactiva.

Los apuntes de curso sobre el manual de Silberschatz añaden tres criterios más:

| Criterio | Definición de los apuntes | Qué se busca |
|---|---|---|
| Utilización de la CPU (*CPU utilization*) | **«Ideally the CPU would be busy 100% of the time, so as to waste 0 CPU cycles. On a real system CPU usage should range from 40% ( lightly loaded ) to 90% ( heavily loaded. )»** | Maximizarla |
| Productividad (*throughput*) | **«Number of processes completed per unit time.»** | Maximizarla |
| Tiempo de espera (*waiting time*) | **«How much time processes spend in the ready queue waiting their turn to get on the CPU.»** | Reducirlo |

La regla general, en los apuntes: **«Maximize CPU utilization and throughput, and minimize all the
others.»** Para un trabajo que sólo usa la CPU, el tiempo de espera es su tiempo de retorno menos lo
que dura (T espera = T retorno − T ráfaga); es cálculo, no cita. En un algoritmo no apropiativo con
todos los trabajos llegados a la vez, coincide con el tiempo de respuesta, porque cada trabajo sólo
espera antes de empezar.

### Los niveles de planificación y el despachador

El planificador de este epígrafe es el de corto plazo, pero los apuntes distinguen tres:

| Planificador | Qué hace, según los apuntes |
|---|---|
| De largo plazo | **«A long-term scheduler is typical of a batch system or a very heavily loaded system. It runs infrequently, ( such as when one process ends selecting one more to be loaded in from disk in its place )»** (decide qué trabajo nuevo entra) |
| De medio plazo | **«When system loads get high, this scheduler will swap one or more processes out of the ready queue system for a few seconds, in order to allow smaller faster jobs to finish up quickly and clear the system.»** (saca procesos temporalmente para aliviar la carga) |
| De corto plazo o de CPU | **«The short-term scheduler, or CPU Scheduler, runs very frequently, on the order of 100 milliseconds, and must very quickly swap one process out of the CPU and swap in another one.»** |

De los tres, el de medio plazo es opcional: **«Some systems also employ a medium-term scheduler.»**

El despachador (*dispatcher*) es la pieza que ejecuta la decisión: **«The dispatcher is the module
that gives control of the CPU to the process selected by the scheduler.»** Su trabajo: cambiar de
contexto, pasar a modo usuario y saltar al punto adecuado del programa. Como corre en cada cambio de
contexto, debe ser lo más rápido posible, y **«The time consumed by the dispatcher is known as
dispatch latency»** (latencia de despacho).

### Planificación apropiativa y no apropiativa

Un planificador no apropiativo deja que cada trabajo acabe: **«such systems would run each job to
completion before considering whether to run a new job»**. Uno apropiativo (*preemptive*) puede
quitarle la CPU a un proceso para dársela a otro, mediante un cambio de contexto. **«Virtually all
modern schedulers are preemptive»**. De los algoritmos que siguen, FIFO y SJF son no apropiativos;
STCF, RR y MLFQ son apropiativos.

### FIFO o FCFS

**«The most basic algorithm we can implement is known as First In, First Out (FIFO) scheduling or
sometimes First Come, First Served (FCFS).»** Se ejecutan los trabajos en el orden en que llegan, cada
uno hasta el final. Es simple y fácil de implementar.

Su problema es el efecto convoy (**«convoy effect»**): si llega primero un trabajo largo, los cortos
esperan detrás. El ejemplo del manual: tres trabajos que llegan a la vez, A de 100 segundos y B y C
de 10; con FIFO, A primero, el tiempo medio de retorno es de 110 segundos ((100 + 110 + 120) / 3).

### SJF, primero el trabajo más corto

**«Shortest Job First (SJF) […] it runs the shortest job first, then the next shortest, and so on.»**
Con los mismos tres trabajos, B y C primero: el tiempo medio de retorno baja a 50 segundos
((10 + 20 + 120) / 3, cálculo del manual). Si todos los trabajos llegan a la vez (y con los demás supuestos
del manual: sólo usan la CPU y se conoce su duración), SJF es óptimo para el tiempo de retorno.

Dos límites. Es no apropiativo, de modo que si A empieza y B y C llegan un instante después, tienen
que esperar a que A termine: vuelve el convoy (en el ejemplo del manual, A de 100 segundos llega en
el instante 0 y B y C, de 10, en el instante 10: tiempo medio de retorno de 103,33 segundos). Y supone conocer de antemano cuánto dura cada trabajo,
cosa que el manual califica de irreal: haría al planificador omnisciente.

### STCF, primero el de menor tiempo restante

La solución al primer límite es añadir la apropiación: **«add preemption to SJF, known as the Shortest
Time-to-Completion First (STCF) or Preemptive Shortest Job First (PSJF) scheduler»**. Cada vez que
llega un trabajo nuevo, el planificador mira cuál de los pendientes (el nuevo incluido) tiene menos
tiempo restante y ejecuta ése. En el ejemplo del manual (A de 100 segundos llega en el instante 0;
B y C, de 10, en el instante 10), STCF interrumpe A, ejecuta B y C y luego termina A: el tiempo medio
de retorno es de 50 segundos (((120 − 0) + (20 − 10) + (30 − 10)) / 3). Con esos mismos supuestos (duración
conocida y sin E/S), STCF es óptimo para el tiempo de retorno, pero no para el de respuesta: el último trabajo espera a que acaben todos los anteriores
antes de ejecutarse por primera vez.

### Round Robin, el turno rotatorio

**«instead of running jobs to completion, RR runs a job for a time slice (sometimes called a
scheduling quantum) and then switches to the next job in the run queue»** (en vez de ejecutar cada
trabajo hasta el final, RR lo ejecuta durante una porción de tiempo, el cuanto, y pasa al siguiente
de la cola). Por eso también se le llama **«time-slicing»**. La porción tiene que ser múltiplo del
periodo de la interrupción de reloj: si el reloj interrumpe cada 10 milisegundos, la porción puede
ser de 10, 20 o cualquier múltiplo de 10 ms.

La longitud del cuanto es la decisión clave:

- Corto: mejor tiempo de respuesta. **«The shorter it is, the better the performance of RR under the
  response-time metric.»**
- Demasiado corto: el coste del cambio de contexto domina. El ejemplo del manual: con un cuanto de
  10 ms y un cambio de contexto de 1 ms, se pierde en cambios alrededor del 10 % del tiempo; con un
  cuanto de 100 ms, menos del 1 %. Repartir así un coste fijo se llama amortización.

RR es excelente para el tiempo de respuesta y de los peores para el de retorno, porque estira cada
trabajo todo lo posible. El manual lo resume como un compromiso inevitable: los algoritmos tipo SJF
y STCF optimizan el tiempo de retorno y son malos para el de respuesta; RR, al revés.

**La E/S.** Cuando un trabajo lanza una E/S, se bloquea y no usa la CPU; el planificador debe dar la
CPU a otro, y cuando la E/S termina, una interrupción devuelve el trabajo de bloqueado a listo. Si un
trabajo interactivo usa la CPU a ráfagas cortas entre E/S, tratar cada ráfaga como un trabajo corto
permite solapar su E/S con el cálculo de los demás: **«Overlap is useful in many different
domains»**, y mejora el aprovechamiento del sistema.

### Ejercicio de aplicación

Tres trabajos llegan a la vez (instante 0), en el orden A, B, C; A dura 6 unidades, B 3 y C 1. El
cálculo es propio, con las definiciones del manual:

| Algoritmo | Orden de ejecución | Finalización A, B, C | Retorno medio | Respuesta media | Espera media |
|---|---|---|---|---|---|
| FIFO | A (0-6), B (6-9), C (9-10) | 6, 9, 10 | 25 / 3 ≈ 8,33 | (0 + 6 + 9) / 3 = 5 | (0 + 6 + 9) / 3 = 5 |
| SJF | C (0-1), B (1-4), A (4-10) | 10, 4, 1 | 15 / 3 = 5 | (4 + 1 + 0) / 3 ≈ 1,67 | (4 + 1 + 0) / 3 ≈ 1,67 |
| RR, cuanto 1 | A, B, C, A, B, A, B, A, A, A | 10, 7, 3 | 20 / 3 ≈ 6,67 | (0 + 1 + 2) / 3 = 1 | (4 + 4 + 2) / 3 ≈ 3,33 |

Con RR, la espera de cada trabajo es su retorno menos su duración: A, 10 − 6 = 4; B, 7 − 3 = 4; C,
3 − 1 = 2. En FIFO y SJF coincide con la respuesta, porque nadie es interrumpido.

Y un caso con llegadas distintas: A llega en 0 y dura 6; B llega en 2 y dura 2. Con SJF (no
apropiativo), A sigue hasta 6 y B va de 6 a 8: retornos 6 y 6, media 6. Con STCF, B interrumpe a A
en 2, va de 2 a 4, y A termina en 8: retornos 8 y 2, media 5.

### Planificación por prioridades

Cada trabajo tiene una prioridad y se ejecuta primero el de prioridad más alta. Los apuntes la
presentan como generalización de SJF: **«Priority scheduling is a more general case of SJF, in which
each job is assigned a priority and the job with the highest priority gets scheduled first.»** (SJF
es el caso en que la prioridad es la inversa de la duración prevista de la próxima ráfaga.) Rasgos que se preguntan:

- Qué número es «más alto» depende del sistema: **«there is no agreed-upon convention as to whether
  "high" priorities use large numbers or small numbers»**. El libro que siguen los apuntes toma 0 como la
  más alta; Windows, al revés, usa 31 como la más alta (más abajo).
- Las prioridades pueden ser internas (las fija el sistema por criterios como la duración media de
  las ráfagas o la proporción de CPU y de E/S) o externas (las fijan los usuarios por la importancia
  del trabajo).
- **«Priority scheduling can be either preemptive or non-preemptive.»**
- Su gran problema es la inanición, que los apuntes llaman **«indefinite blocking, or starvation, in
  which a low-priority task can wait forever because there are always some other jobs around that
  have higher priority»**. El remedio habitual es el envejecimiento: **«aging, in which priorities of
  jobs increase the longer they wait»**.

El ejemplo de los apuntes, con el número más bajo como prioridad más alta (los apuntes no dan
instantes de llegada; el cálculo supone que todos llegan en el 0): P1 dura 10 (prioridad 3), P2 1 (prioridad 1), P3 2 (prioridad 4), P4 1
(prioridad 5) y P5 5 (prioridad 2). El orden es P2 (0-1), P5 (1-6), P1 (6-16), P3 (16-18) y P4
(18-19); las esperas, 0, 1, 6, 16 y 18, y el tiempo medio de espera, **«8.2 ms»** (41 / 5; el orden
y la suma son cálculo propio que reproduce la cifra de los apuntes).

### Colas multinivel con realimentación (MLFQ)

Resuelve el segundo límite de SJF: no conocer la duración de los trabajos. MLFQ tiene varias colas,
cada una con un nivel de prioridad, y en lugar de una prioridad fija **«MLFQ varies the priority of a
job based on its observed behavior»** (ajusta la prioridad según lo que observa del trabajo). Sus
reglas, en su forma final:

1. **«Rule 1: If Priority(A) > Priority(B), A runs (B doesn’t).»**
2. **«Rule 2: If Priority(A) = Priority(B), A & B run in round-robin fashion using the time slice
   (quantum length) of the given queue.»**
3. **«Rule 3: When a job enters the system, it is placed at the highest priority (the topmost
   queue).»**
4. **«Rule 4: Once a job uses up its time allotment at a given level (regardless of how many times it
   has given up the CPU), its priority is reduced (i.e., it moves down one queue).»**
5. **«Rule 5: After some time period S, move all the jobs in the system to the topmost queue.»**

Por qué funcionan. Todo trabajo nuevo empieza arriba, como si fuera corto; si lo es, termina pronto,
y si no, va bajando: así MLFQ se aproxima a SJF sin conocer duraciones. Un trabajo interactivo, que
cede la CPU a menudo, se queda arriba. La regla 5, el impulso de prioridad (**«priority boost»**),
evita la inanición (**«starvation»**): sin ella, si hay muchos trabajos interactivos, los largos
**«will never receive any CPU time (they starve)»**. Y la regla 4 cuenta todo el tiempo gastado en el
nivel, ceda o no la CPU, para que un programa no pueda engañar al planificador (**«game the
scheduler»**) cediendo la CPU justo antes de agotar su porción.

El manual da a MLFQ por base de varios sistemas reales: **«many systems, including BSD UNIX
derivatives […], Solaris […], and Windows NT and subsequent Windows operating systems […] use a form
of MLFQ as their base scheduler»** (los cortes son las llamadas a la bibliografía).

### Planificación con varios procesadores

Con varias CPU caben dos enfoques:

- Una sola cola para todos (SQMS): **«putting all jobs that need to be scheduled into a single
  queue»**. Es simple, pero escala mal, porque la cola compartida exige cerrojos (epígrafe 6), y
  pierde la afinidad de caché: un trabajo que salta de CPU en CPU tiene que recargar su estado en
  cada una.
- Una cola por CPU (MQMS): cada trabajo entra en una cola y se planifica allí, **«thus avoiding the
  problems of information sharing and synchronization found in the single-queue approach»**. Su
  problema es el desequilibrio de carga, que se corrige migrando trabajos; una técnica es el robo de
  trabajo (**«work stealing»**), en que una cola con poca carga se lleva trabajos de otra más llena.

### Cómo planifica Windows

- Prioridades: **«Los niveles de prioridad van de cero (prioridad más baja) a 31 (prioridad más
  alta). Solo el subproceso de página cero puede tener una prioridad de cero.»**
- Turno entre iguales y apropiación: **«El sistema asigna segmentos de tiempo de forma round robin a
  todos los subprocesos con la prioridad más alta.»** Si ninguno está listo, pasa a la prioridad
  siguiente. **«Si un subproceso de prioridad más alta está disponible para ejecutarse, el sistema
  deja de ejecutar el subproceso de prioridad inferior (sin permitirle terminar de usar su intervalo
  de tiempo) y asigna un segmento de tiempo completo al subproceso de prioridad más alta.»**
- Prioridad base: se forma con **«La clase de prioridad de su proceso»** y **«El nivel de prioridad
  del subproceso dentro de la clase de prioridad de su proceso»**. Las clases son seis, de
  `IDLE_PRIORITY_CLASS` a `REALTIME_PRIORITY_CLASS`, y **«De forma predeterminada, la clase de
  prioridad de un proceso es NORMAL_PRIORITY_CLASS.»** Los niveles dentro de la clase son siete, de
  `THREAD_PRIORITY_IDLE` a `THREAD_PRIORITY_TIME_CRITICAL`, y **«Todos los subprocesos se crean
  mediante THREAD_PRIORITY_NORMAL.»**
- Dos avisos de Microsoft con valor práctico: la clase alta, con cuidado, porque **«Si un subproceso se
  ejecuta en el nivel de prioridad más alto durante períodos prolongados, otros subprocesos del
  sistema no obtendrán tiempo de procesador.»**; y la de tiempo real, casi nunca, **«ya que interrumpe
  los subprocesos del sistema que administran la entrada del mouse, la entrada del teclado y el
  vaciado del disco en segundo plano»**.

### Cómo planifica Linux

La documentación del núcleo: **«The Linux kernel began transitioning to EEVDF in version 6.6 (as a
new option in 2024), moving away from the earlier Completely Fair Scheduler (CFS)»**. Su objetivo:
**«Similarly to CFS, EEVDF aims to distribute CPU time equally among all runnable tasks with the same
priority.»** Para ello asigna a cada tarea un tiempo de ejecución virtual y un desfase (*lag*) que dice
si ha recibido su parte; entre las tareas con desfase mayor o igual que cero calcula un plazo
virtual para cada una y **«selecting the task with the earliest VD to execute next»** (elige la de
plazo virtual más temprano). Eso permite dar prioridad a las tareas sensibles a la latencia con
porciones de tiempo más cortas.

## 6. Concurrencia

### El problema: la condición de carrera

Hay concurrencia cuando varios hilos o procesos avanzan a la vez sobre datos compartidos. El ejemplo
del manual son dos hilos que suman uno a un mismo contador: la suma son tres instrucciones de máquina
(leer, sumar, escribir), y si un cambio de contexto cae en medio, una de las dos sumas se pierde. Los
cuatro términos que el manual destaca, casi todos acuñados, según el manual, por Dijkstra:

| Término | Definición del manual |
|---|---|
| Sección crítica | **«A critical section is a piece of code that accesses a shared variable (or more generally, a shared resource) and must not be concurrently executed by more than one thread.»** |
| Condición de carrera | **«race condition (or, more specifically, a data race): the results depend on the timing of the code’s execution»** |
| Programa indeterminado | **«An indeterminate program consists of one or more race conditions; the output of the program varies from run to run, depending on which threads ran when.»** |
| Exclusión mutua | **«This property guarantees that if one thread is executing within the critical section, the others will be prevented from doing so.»** |

La salida: **«threads should use some kind of mutual exclusion primitives; doing so guarantees that
only a single thread ever enters a critical section, thus avoiding races, and resulting in
deterministic program outputs»**. Y la idea que hay debajo es la atomicidad: **«The idea behind making
a series of actions atomic is simply expressed with the phrase “all or nothing”»** (o se ven hechas
todas las acciones del grupo, o ninguna, sin estado intermedio visible).

### Cerrojos

**«A lock is just a variable»**, que en cada momento está **«either available (or unlocked or free)
and thus no thread holds the lock, or acquired (or locked or held), and thus exactly one thread holds
the lock and presumably is in a critical section»** (libre, y nadie lo tiene, o adquirido, y lo tiene
exactamente un hilo, que está en su sección crítica). Se usa rodeando la sección crítica con
`lock()` y `unlock()`; mientras un hilo lo tiene, `lock()` no vuelve en los demás. En POSIX el
cerrojo se llama *mutex*: **«The name that the POSIX library uses for a lock is a mutex, as it is used
to provide mutual exclusion between threads»**.

Un cerrojo se juzga por tres criterios: si da exclusión mutua; si es equitativo (**«does any thread
contending for the lock starve while doing so, thus never obtaining it?»**, si algún hilo espera para
siempre); y su rendimiento. La forma más simple es el cerrojo de espera activa (*spin lock*), que se
construye con una instrucción atómica del procesador como *test-and-set* y **«simply spins, using CPU
cycles, until the lock becomes available»** (da vueltas gastando CPU hasta que el cerrojo queda
libre); en un solo procesador necesita un planificador apropiativo. Una de las soluciones más antiguas,
inhibir las interrupciones durante la sección crítica, se ideó para un solo procesador y no sirve con
varios.

### Soluciones por programa: Dekker y Peterson

Además de con instrucciones atómicas, se buscó la exclusión mutua sólo con programa. El manual lo
cuenta en un recuadro: en los años sesenta Dijkstra planteó el problema a sus colegas, y uno de
ellos, el matemático Theodorus Jozef Dekker, dio con una solución; **«Unlike the solutions we discuss
here, which use special hardware instructions and even OS support, Dekker’s algorithm uses just
loads and stores (assuming they are atomic with respect to each other, which was true on early
hardware).»** (Sin instrucciones especiales ni apoyo del sistema: sólo lecturas y escrituras de
memoria.)

**«Dekker’s approach was later refined by Peterson»**, con la misma idea: **«just loads and stores
are used, and the idea is to ensure that two threads never enter a critical section at the same
time»**. El algoritmo de Peterson es para dos hilos y usa dos variables compartidas:

- `flag[2]`: cada hilo pone a 1 la suya para indicar que quiere entrar (**«indicate you intend to
  hold the lock»**).
- `turn`: de quién es el turno. Para entrar, el hilo marca su `flag`, cede el turno al otro
  (`turn = 1 - self`) y espera en bucle mientras el otro quiera entrar y sea su turno. Para salir,
  basta con bajar su `flag`.

El manual advierte de su valor actual: era más fácil suponer un poco de apoyo del procesador, y
además **«algorithms like the ones above don’t work on modern hardware (due to relaxed memory
consistency models)»** (no funcionan en el soporte físico actual, por sus modelos de consistencia de
memoria relajados).

### Semáforos

**«A semaphore is an object with an integer value that we can manipulate with two routines; in the
POSIX standard, these routines are sem_wait() and sem_post()»**. Dijkstra las llamó P() y V().

| Operación | Qué hace |
|---|---|
| `sem_wait()` (P) | **«decrement the value of semaphore s by one»** y **«wait if value of semaphore s is negative»** |
| `sem_post()` (V) | **«increment the value of semaphore s by one»** y **«if there are one or more threads waiting, wake one»** |

Un dato que se pregunta: **«the value of the semaphore, when negative, is equal to the number of
waiting threads»** (cuando el valor es negativo, su valor absoluto es el número de hilos que esperan).
Y el valor inicial decide el uso:

- Iniciado a 1, hace de cerrojo. **«Because locks only have two states (held and not held), we
  sometimes call a semaphore used as a lock a binary semaphore.»**
- Iniciado a 0, sirve para ordenar sucesos: un hilo espera hasta que otro le avisa con `sem_post()`.

### Variables de condición

**«A condition variable is an explicit queue that threads can put themselves on when some state of
execution (i.e., some condition) is not as desired (by waiting on the condition); some other thread,
when it changes said state, can then wake one (or more) of those waiting threads and thus allow them
to continue (by signaling on the condition).»** El nombre se lo dio Hoare en su trabajo sobre
monitores.

### Monitores

El monitor une la exclusión mutua con la programación orientada a objetos. Lo describió primero Per
Brinch Hansen y lo refinó después Tony Hoare, y consiste en una clase cuyos
métodos no pueden ejecutarse a la vez: **«the monitor guarantees that only one thread can be active
within the monitor at a time»**. Lo hace con un cerrojo implícito: **«Whenever a thread tries to
call a monitor routine, it implicitly tries to acquire the monitor lock.»** Si no lo consigue, se
bloquea hasta que el hilo que está dentro termina. C++ no tiene monitores; **«However, Java does
support monitors, with what are called synchronized methods.»**

Para esperar a que cambie un estado (por ejemplo, a que haya hueco en el búfer), el monitor usa
variables de condición con dos operaciones: **«wait() blocks the calling thread on a given
condition; signal() wakes one waiting thread that is waiting on the condition.»** Hay dos
semánticas de `signal()`:

| Semántica | Qué hace `signal()` |
|---|---|
| De Hoare | **«the signal() immediately wakes one waiting thread and runs it»**: el cerrojo del monitor pasa en el acto al hilo despertado |
| De Mesa (Lampson y Redell, Xerox PARC) | Es sólo una pista: mueve un hilo de bloqueado a listo, pero no lo ejecuta en el acto, y el hilo que avisa sigue hasta salir del monitor |

**«virtually any system today that uses condition variables with signaling and waiting uses Mesa
semantics»**, y de ahí la regla práctica del manual: **«always recheck the condition after being
woken! Put in even simpler terms, use while loops and not if statements when checking
conditions.»** El manual les dedica un apéndice titulado **«Monitors (Deprecated)»** (obsoletos), y explica que se
inventaron cuando llegaba la programación orientada a objetos, para unir las dos ideas:
**«Nothing more than that.»**

### Memoria compartida y paso de mensajes

Los procesos que cooperan (los que pueden afectar a otros o ser afectados por ellos) necesitan
comunicarse, y los apuntes de curso sobre el manual de Silberschatz dan dos modelos: **«Shared
Memory systems or Message Passing systems»**.

| Modelo | Ventaja | Inconveniente |
|---|---|---|
| Memoria compartida | **«Shared Memory is faster once it is set up, because no system calls are required and access occurs at normal memory speeds.»** | Más difícil de montar y **«doesn't work as well across multiple computers»**; además, el acceso concurrente hay que sincronizarlo (lo que trata este epígrafe) |
| Paso de mensajes | Más sencillo de montar y **«works well across multiple computers»** | **«Message Passing requires system calls for every message transfer, and is therefore slower»** |

El paso de mensajes necesita al menos dos llamadas: **«system calls for "send message" and "receive
message"»**. Y deja tres decisiones de diseño:

- Nombrado. En la comunicación directa, **«the sender must know the name of the receiver»**; en la
  indirecta, los mensajes van a buzones o puertos: **«Indirect communication uses shared mailboxes,
  or ports.»**
- Sincronización. **«Either the sending or receiving of messages ( or neither or both ) may be
  either blocking or non-blocking.»** (Enviar y recibir pueden ser bloqueantes o no.)
- Almacenamiento en cola, con tres capacidades: cero (el emisor se bloquea hasta que el receptor
  acepta el mensaje), limitada (se bloquea si la cola está llena) e ilimitada (nunca se bloquea).

### Los problemas clásicos

| Problema | Planteamiento | Solución que da el manual |
|---|---|---|
| Productor-consumidor o búfer acotado | Uno o varios productores dejan datos en un búfer y uno o varios consumidores los sacan. Ejemplos del manual: la cola de peticiones de un servidor web y la tubería de `grep foo file.txt \| wc -l` | Dos semáforos, `empty` y `full`, para los huecos vacíos y llenos, y un cerrojo sólo alrededor de la sección crítica. Si el cerrojo envuelve también las esperas, hay interbloqueo |
| Lectores-escritores | Varias operaciones leen una estructura y otras la modifican | Un cerrojo de lectura y escritura: un solo escritor a la vez, y muchos lectores a la vez mientras no haya escritor |
| La cena de los filósofos | Cinco filósofos alrededor de una mesa con un tenedor entre cada dos; para comer, cada uno necesita los dos de sus lados | Que al menos uno coja los tenedores en orden distinto (así lo resolvió Dijkstra): se rompe el ciclo de espera |

El manual advierte del último que **«its practical utility is low»**, pero que su fama obliga a
estudiarlo.

### El interbloqueo

El interbloqueo (*deadlock*) es la espera circular sin salida: el hilo 1 tiene el cerrojo L1 y pide
L2, y el hilo 2 tiene L2 y pide L1; **«each thread is waiting for the other and neither can run»**.
**«Four conditions need to hold for a deadlock to occur»**:

| Condición | Definición del manual |
|---|---|
| Exclusión mutua | **«Threads claim exclusive control of resources that they require (e.g., a thread grabs a lock).»** |
| Retención y espera | **«Threads hold resources allocated to them (e.g., locks that they have already acquired) while waiting for additional resources (e.g., locks that they wish to acquire).»** |
| Sin apropiación | **«Resources (e.g., locks) cannot be forcibly removed from threads that are holding them.»** |
| Espera circular | **«There exists a circular chain of threads such that each thread holds one or more resources (e.g., locks) that are being requested by the next thread in the chain.»** |

**«If any of these four conditions are not met, deadlock cannot occur.»** De ahí las tres
estrategias:

1. Prevención: romper una de las cuatro condiciones.
   - Espera circular: la técnica probablemente más práctica, según el manual, es un orden total de adquisición de los cerrojos (si sólo
     hay L1 y L2, coger siempre L1 antes que L2).
   - Retención y espera: coger todos los cerrojos a la vez, de forma atómica (por ejemplo, tras un
     cerrojo global de prevención).
   - Sin apropiación: usar `pthread_mutex_trylock()`, que coge el cerrojo si está libre o devuelve
     error, y soltar lo que se tiene si falla. Su riesgo es el bloqueo activo (*livelock*): dos hilos
     que reintentan sin fin **«but progress is not being made»**; se mitiga con una espera aleatoria
     antes de reintentar.
   - Exclusión mutua: estructuras sin cerrojos (*lock-free*), construidas con instrucciones atómicas
     del procesador.
2. Evitación: conocer de antemano qué cerrojos pedirá cada hilo y planificarlos de forma que el
   interbloqueo no pueda darse. El ejemplo famoso es **«Dijkstra’s Banker’s Algorithm»** (el algoritmo
   del banquero); el manual advierte que sólo es útil en entornos muy limitados y que reduce la
   concurrencia.
3. Detección y recuperación: dejar que ocurra de vez en cuando y actuar al detectarlo. **«A deadlock
   detector runs periodically, building a resource graph and checking it for cycles»**; si hay un
   ciclo, el sistema se reinicia. Lo usan muchos sistemas de bases de datos.

### La inanición

La inanición (*starvation*) es que un hilo o proceso no consiga nunca el recurso o la CPU aunque el
sistema avance. Aparece dos veces en el manual: en la planificación, cuando los trabajos largos
**«will never receive any CPU time (they starve)»** porque los interactivos se llevan toda la CPU
(epígrafe 5), y en los cerrojos, como el criterio de equidad. Se distingue del interbloqueo en que en
éste no avanza nadie del grupo, y del bloqueo activo en que en éste los hilos trabajan sin progresar.

## 7. Multitarea y multiprogramación

### De los lotes a la multiprogramación

En los primeros sistemas se ejecutaba un programa cada vez, bajo el control de un operador humano
que decidía el orden de los trabajos; ese modo **«was known as batch processing, as a number of jobs
were set up and then run in a “batch” by the operator»** (proceso por lotes).

Llegó después la multiprogramación: **«multiprogramming became commonplace due to the desire to make
better use of machine resources. Instead of just running one job at a time, the OS would load a
number of jobs into memory and switch rapidly between them, thus improving CPU utilization. This
switching was particularly important because I/O devices were slow; having a program wait on the CPU
while its I/O was being serviced was a waste of CPU time.»** (Para aprovechar mejor la máquina, el
sistema carga varios trabajos en memoria y salta de uno a otro; mientras uno espera una E/S lenta,
otro usa la CPU.)

La multiprogramación trajo dos problemas que son el resto de este tema: la protección de memoria
(**«we wouldn’t want one program to be able to access the memory of another program»**) y la
concurrencia (**«Understanding how to deal with the concurrency issues introduced by multiprogramming
was also critical»**).

### El tiempo compartido

El paso siguiente fue el tiempo compartido: el sistema reparte la CPU entre procesos a intervalos
cortos y crea así la ilusión de que hay muchas CPU virtuales (epígrafe 2). **«This basic technique, known as
time sharing of the CPU, allows users to run as many concurrent processes as they would like; the
potential cost is performance, as each will run more slowly if the CPU(s) must be shared.»** Con el
tiempo compartido nació la métrica del tiempo de respuesta (epígrafe 5).

La diferencia que se pregunta: la multiprogramación busca aprovechar la CPU (cambiar de trabajo
cuando uno espera E/S); el tiempo compartido busca la respuesta interactiva (cambiar de trabajo a
intervalos aunque nadie espere). Esta forma de contraponerlas es oficio, sobre las citas anteriores.

### Multitarea apropiativa y cooperativa

La multitarea es la capacidad de tener varias tareas en curso repartiéndose el procesador. Microsoft
la define así: **«Un sistema operativo multitarea divide el tiempo de procesador disponible entre los
procesos o subprocesos que lo necesitan. El sistema está diseñado para la multitarea preferente;
asigna un segmento de tiempo de procesador a cada subproceso que ejecuta. El subproceso que se está
ejecutando actualmente se suspende cuando transcurre su segmento de tiempo, lo que permite que se
ejecute otro subproceso.»** («Preferente» es la traducción de Microsoft de *preemptive*: apropiativa.)
Y da una cifra, tras advertir que **«La duración del período de tiempo depende del sistema
operativo y del procesador.»**: **«Dado que cada segmento de tiempo es pequeño (aproximadamente 20 milisegundos),
aparecen varios subprocesos que se están ejecutando al mismo tiempo. Este es realmente el caso en
sistemas multiprocesador, donde los subprocesos ejecutables se distribuyen entre los procesadores
disponibles.»**

La diferencia entre las dos multitareas está en cómo recupera el sistema el control de la CPU:

| | Cooperativa | Apropiativa |
|---|---|---|
| Cómo recupera el control | Esperando a que el proceso lo ceda: **«the OS regains control of the CPU by waiting for a system call or an illegal operation of some kind to take place»**; estos sistemas suelen tener una llamada explícita `yield` | Con una interrupción de reloj: **«A timer device can be programmed to raise an interrupt every so many milliseconds; when the interrupt is raised, the currently running process is halted, and a pre-configured interrupt handler in the OS runs.»** |
| Supuesto | **«the OS trusts the processes of the system to behave reasonably»** | El sistema no se fía: puede parar a cualquiera |
| Riesgo | Un proceso en bucle infinito que no hace llamadas al sistema se queda la máquina; el único remedio es reiniciar | El coste de los cambios de contexto |
| Ejemplos del manual | **«early versions of the Macintosh operating system»** y el antiguo Xerox Alto | Los sistemas actuales (Windows, por la cita de Microsoft) |

### Concurrencia y paralelismo

Con un solo procesador, la multitarea es concurrencia sin paralelismo: los procesos avanzan
intercalados y parece que van a la vez. Con varios, hay paralelismo real; es lo que dice Microsoft al
señalar que en los sistemas multiprocesador los hilos sí se ejecutan al mismo tiempo, repartidos entre
los procesadores. La planificación con varios procesadores está en el epígrafe 5. Esta distinción
entre concurrencia y paralelismo es oficio, apoyada en esa cita y en la definición de paralelismo del
epígrafe 4.

## Lo que este tema no da, y dónde está

- La gestión de memoria en detalle (memoria virtual, paginación, segmentación, intercambio) y los
  sistemas de ficheros por dentro: el enunciado no los nombra; aquí sólo aparecen como funciones del
  sistema. Los sistemas de ficheros de Windows y Linux en la práctica: temas 6 y 9.
- Windows 11, PowerShell, Windows Server y la administración de Linux (órdenes como `ps` o `top`,
  servicios, arranque): temas 6, 7, 8 y 9. La virtualización de sistemas: tema 10.
- La clasificación de Windows por tipo de núcleo: las fuentes leídas describen sus componentes de modo
  núcleo y de modo usuario y Microsoft niega que sea un micronúcleo, pero no lo llaman monolítico ni
  híbrido, y el tema no lo clasifica.
- El estado suspendido y los modelos de más de cinco estados que lo incluyen: las fuentes leídas sólo
  dicen que el planificador de medio plazo saca procesos de la cola de listos, sin dar nombre a ese
  estado, y el tema no lo da. Tampoco da, por no haberlos encontrado en fuente, la clase de los
  sistemas monousuario ni la distinción entre tiempo real estricto y no estricto.
- Las llamadas concretas de comunicación entre procesos de Unix y Windows (tuberías, colas de
  mensajes, memoria compartida POSIX): a la práctica de Linux y Windows van los temas 6 y 9.
- La implantación concreta de los sistemas operativos en los equipos de la RTVA y de CSRTV: no consta
  en ningún documento publicado.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| R. H. Arpaci-Dusseau y A. C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (OSTEP), Universidad de Wisconsin-Madison, versión 1.10, capítulos en pages.cs.wisc.edu/~remzi/OSTEP/: cap. 2 «Introduction to Operating Systems» (© 2008–25) | Definición del sistema, máquina virtual, biblioteca estándar, gestor de recursos, objetivos de diseño, lotes, llamada al sistema, multiprogramación | 05-10-2026 |
| OSTEP, cap. 4 «The Abstraction: The Process» y cap. 5 «Interlude: Process API» (© 2008–23 y 2008–25) | Proceso, estado de máquina, creación, estados y transiciones (fig. 4.2), zombi, lista de procesos y PCB (fig. 4.5, xv6), operaciones, `fork()`, `exec()`, `wait()`, señales, mecanismo y política, tiempo compartido | 05-10-2026 |
| OSTEP, cap. 6 «Mechanism: Limited Direct Execution» (© 2008–23) | Modos usuario y núcleo, *trap* y tabla de *traps*, enfoque cooperativo y apropiativo, interrupción de reloj, planificador, cambio de contexto | 05-10-2026 |
| OSTEP, cap. 7 «Scheduling: Introduction», cap. 8 «Scheduling: The Multi-Level Feedback Queue» (© 2008–23) y cap. 10 «Multiprocessor Scheduling (Advanced)» (© 2008–25) | Métricas, FIFO, SJF, STCF, RR, amortización, E/S y solapamiento, ejemplos de 110, 50 y 103,33 segundos, reglas de MLFQ, SQMS, MQMS, robo de trabajo | 05-10-2026 |
| OSTEP, cap. 26 «Concurrency: An Introduction», 28 «Locks», 30 «Condition Variables», 31 «Semaphores» (© 2008–25) | Hilos y TCB, paralelismo, condición de carrera, sección crítica, indeterminación, exclusión mutua, atomicidad, cerrojos, *spin lock*, semáforos, variables de condición, productor-consumidor, lectores-escritores, filósofos | 05-10-2026 |
| OSTEP, cap. 28 «Locks», recuadro «Dekker’s and Peterson’s algorithms» (© 2008–25), y apéndice D «Monitors (Deprecated)» (threads-monitors.pdf, © 2008–23) | Dekker y Peterson; monitores, semánticas de Hoare y de Mesa | 06-10-2026 |
| J. Bell, apuntes del curso CS 385 «Operating Systems», Universidad de Illinois en Chicago (www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/), sobre A. Silberschatz, P. B. Galvin y G. Gagne, *Operating System Concepts*, 9.ª ed.; caps. 1 «Introduction», 3 «Processes», 4 «Threads» y 6 «CPU Scheduling» | Clases de sistemas (tiempo compartido, tiempo real, empotrados, distribuidos), cinco estados, planificadores de largo, medio y corto plazo, despachador, utilización, productividad y tiempo de espera, planificación por prioridades y envejecimiento, ejemplo de 8,2 ms, hilos de usuario y de núcleo y sus modelos, memoria compartida y paso de mensajes | 06-10-2026 |
| Documentación del núcleo Linux, «Deadline Task Scheduling» (docs.kernel.org/scheduler/sched-deadline.html) y «Theory of operation» de «Real-time preemption» (docs.kernel.org/core-api/real-time/theory.html) | Plazo de una tarea de tiempo real, idoneidad para multimedia y *streaming*, PREEMPT_RT, `SCHED_FIFO` | 06-10-2026 |
| OSTEP, cap. 32 «Common Concurrency Problems», versión 1.20 (© 2008–26) | Interbloqueo: cuatro condiciones, prevención, *livelock*, banquero, detección | 05-10-2026 |
| OSTEP, cap. 36 «I/O Devices» (© 2008–25) | Registros del dispositivo, sondeo, interrupciones, DMA, E/S explícita y mapeada en memoria, controlador de dispositivo, 70 % del código | 05-10-2026 |
| Microsoft Learn (es-es), «Modo de usuario y modo kernel», «Información general sobre los componentes de Windows» (actualizada el 15-06-2023) y «Biblioteca de kernels en modo kernel de Windows» | Modos en Windows, componentes, administrador de E/S, definición de kernel, «microkernel» no aplicable a Windows | 05-10-2026 |
| Microsoft Learn (es-es), Win32: «Procesos y subprocesos», «Multitarea», «Prioridades de programación», «Modificadores de contexto» | Proceso, subproceso, fibra, grupo de subprocesos, multitarea preferente y 20 ms, prioridades 0-31, clases y niveles, cambio de contexto | 05-10-2026 |
| Documentación del núcleo Linux, «EEVDF Scheduler» (docs.kernel.org/scheduler/sched-eevdf.html) | EEVDF desde la versión 6.6, objetivo y funcionamiento | 05-10-2026 |
| P. J. Salzman, M. Burian, O. Pomerantz, B. Mottram y J. Huang, *The Linux Kernel Module Programming Guide* (sysprog21.github.io/lkmpg, edición de 7-9-2026) | Módulo del núcleo, núcleo monolítico, micronúcleos GNU Hurd y Zircon | 05-10-2026 |
| MINIX 3, página oficial (minix3.org) | Micronúcleo | 05-10-2026 |

El manual OSTEP está en inglés: las citas van en negrita en su lengua y la explicación en castellano
es del tema. Microsoft traduce *thread* por «subproceso» y *preemptive* por «preferente»; se cita tal
cual. Los apuntes de J. Bell son de un curso universitario (montados en la primavera de 2006 y, según su
página principal, en curso de actualización para la primavera de 2013) y siguen la 9.ª edición del manual de Silberschatz;
el tema toma de ellos conceptos y definiciones estables, y no los ejemplos de sistemas concretos que
podrían haber cambiado, salvo los que se dicen como suyos. La documentación del núcleo Linux dice que la transición a EEVDF empezó en la versión 6.6
**«(as a new option in 2024)»**; no se ha comprobado aparte la fecha de publicación de esa versión.

Oficio sin fuente detrás, y así se declara: la tabla de los modos núcleo y usuario y la razón de que
existan los dos (las citas de OSTEP y de Microsoft que la siguen la sostienen); el gestor de entrada
y salida «en tres líneas» y el reparto de funciones entre el núcleo, el planificador, la unidad
aritmético-lógica y la pila de red; la función del núcleo en Unix y Linux y lo que no hace (interfaz gráfica,
servicios de red, comunicación por terminales); lo que mete dentro cada tipo de núcleo en la tabla
y la ventaja de cada uno; la contraposición entre
multiprogramación y tiempo compartido; que lo que distingue al tiempo real es la garantía de plazo y
no la rapidez; que el acceso a la memoria compartida hay que sincronizarlo; la distinción entre concurrencia y paralelismo; la definición
de inanición como síntesis de las dos citas del manual. Es cálculo, y se puede rehacer: el ejercicio
de aplicación del epígrafe 5, con sus tiempos de espera y la fórmula T espera = T retorno − T ráfaga,
y el orden y las esperas del ejemplo de prioridades.
