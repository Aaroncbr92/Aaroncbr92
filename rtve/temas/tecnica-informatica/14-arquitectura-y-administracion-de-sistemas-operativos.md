# Tema 14 del específico de Técnica Informática · Arquitectura y administración de sistemas operativos

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · puntos 16 y 17 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia son la arquitectura del sistema y su administración, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Extensión** | **1.761 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la entrada y salida (**E/S**, y en inglés **I/O**);
la unidad central de proceso (**CPU**); la lista de control de acceso (**ACL**, *access control
list*); el protocolo de control de transmisión sobre el protocolo de internet (**TCP/IP**); y los
nombres de orden de la línea de comandos, que van en acentos graves porque son código y no siglas.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, puntos 16 y 17):
> «16. Arquitectura y sistemas operativos: Terminología y conceptos. Arquitectura de sistemas
> operativos: UNIX, Linux y Windows Server.»
>
> «17. Administración y gestión de sistemas operativos y software de base.»

**Cinco preguntas.** **Y este tema reúne dos puntos del anexo porque el examen los ha tratado como
uno**: **la arquitectura del sistema y las órdenes con que se administra.**

**Su reparto**: **tres preguntas son de órdenes de la línea de comandos de Unix o Linux** y **dos son
de arquitectura**: qué hace el núcleo y qué hace el gestor de entrada y salida.

<!-- indice -->

## Índice

- [1. Qué es un sistema operativo y de qué se ocupa](#1-qué-es-un-sistema-operativo-y-de-qué-se-ocupa)
- [2. El núcleo](#2-el-núcleo)
- [3. El gestor de entrada y salida](#3-el-gestor-de-entrada-y-salida)
- [4. Las órdenes de la línea de comandos](#4-las-órdenes-de-la-línea-de-comandos)
- [5. La administración que el punto 17 pide](#5-la-administración-que-el-punto-17-pide)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Qué es un sistema operativo y de qué se ocupa

**Sus cinco funciones, que es el vocabulario del punto 16:**

| Función | De qué se ocupa |
|---|---|
| **Gestión de procesos** | **Quién se ejecuta, cuándo y durante cuánto** |
| **Gestión de memoria** | **Qué hay en memoria y dónde** |
| **Gestión de ficheros** | **Cómo se organizan los datos en el almacenamiento** |
| **Gestión de entrada y salida** | **Cómo se habla con los dispositivos** |
| **Protección y seguridad** | **Quién puede hacer qué** |

**Y la división que atraviesa todo el tema**: **el modo núcleo y el modo usuario.**

| Modo | Qué puede hacer | Qué corre ahí |
|---|---|---|
| **Núcleo** | **Todo**: acceder al soporte físico y a cualquier memoria | **El núcleo y sus controladores** |
| **Usuario** | **Sólo lo suyo**, y pedir el resto por llamada al sistema | **Los programas** |

**La razón de que existan los dos**: **un error de un programa no puede llevarse el sistema por
delante.** **Cuando un programa necesita algo del soporte físico, no lo toca: lo pide.**

## 2. El núcleo

**La pregunta 90**: **la función del núcleo en un sistema operativo Unix o Linux es controlar los
procesos, la memoria y la administración de dispositivos.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son cosas que en Unix NO hace el núcleo**, lo que **convierte la pregunta
en un buen examen de arquitectura:**

| Opción | Quién lo hace realmente |
|---|---|
| **b) Gestionar la interfaz gráfica** | **Un servidor gráfico en modo usuario.** **En Unix, el entorno gráfico es un programa más** |
| **c) Proporcionar servicios de red como TCP/IP** | **La pila está en el núcleo, pero los servicios los dan demonios en modo usuario** |
| **d) Facilitar la comunicación entre usuarios por terminales** | **Programas de usuario** |

**El rasgo de diseño de Unix que la pregunta persigue**: **el núcleo hace lo imprescindible y todo lo
demás son programas.** **Por eso se puede cambiar el escritorio sin tocar el sistema**, y por eso un
servidor Linux puede no tener entorno gráfico en absoluto.

**Y la clasificación de núcleos que conviene tener vista:**

| Tipo | Qué mete dentro | Ejemplo |
|---|---|---|
| **Monolítico** | **Procesos, memoria, ficheros, red y controladores, todo en modo núcleo** | **Linux** |
| **Micronúcleo** | **Lo mínimo; el resto, servicios en modo usuario** | **Minix** |
| **Híbrido** | **Monolítico con partes modulares** | **Windows** |

**Linux es monolítico y a la vez modular**: **los controladores se cargan y descargan en caliente**,
que es lo que permite añadir soporte físico sin recompilar.

## 3. El gestor de entrada y salida

**La pregunta 72**: **la función del gestor de entrada y salida en un sistema operativo es permitir la
comunicación entre dispositivos y subsistemas del modo usuario.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas reparten esa función entre otros tres responsables:**

| Opción | Quién lo hace |
|---|---|
| **a) Operaciones aritmético-lógicas** | **La unidad aritmético-lógica del procesador**, que es soporte físico |
| **c) Administrar procesos del sistema** | **El planificador y el gestor de procesos** |
| **d) Controlar la red** | **La pila de red**, que es un subsistema propio |

**Qué hace el gestor de entrada y salida, en tres líneas**: **recibe la petición del programa, la
convierte en órdenes concretas para el controlador del dispositivo, y devuelve el resultado.**
**Su valor está en que el programa no tiene que saber qué disco ni qué impresora hay debajo**: **pide
«escribe estos bytes» y el gestor se entiende con el aparato.**

**Y de ahí sale la idea que Unix llevó más lejos que nadie**: **casi todo es un fichero.** **Un disco,
un terminal y hasta un dispositivo de red se manejan con las mismas llamadas que un fichero
corriente**, y **eso es posible porque el gestor de entrada y salida hace de traductor.**

## 4. Las órdenes de la línea de comandos

**Tres preguntas del tema son de aquí**, y **conviene aprenderlas por familias y no una a una:**

| Familia | Órdenes |
|---|---|
| **Dónde estoy y qué hay** | `pwd` **(ruta actual)**, `ls` **(listar)**, `cd` **(cambiar de directorio)** |
| **Qué se está ejecutando** | `top` **y** `htop` **(en tiempo real)**, `ps` **(instantánea)** |
| **Permisos** | `chmod` **y** `chown` **(básicos)**, `getfacl` **y** `setfacl` **(extendidos)** |
| **Servicios** | `systemctl` **(gestión de servicios)**, `journalctl` **(su registro)** |
| **Parámetros del núcleo** | `sysctl` |
| **Buscar dentro de ficheros** | `grep` |

**La pregunta 19**: **la orden `pwd` en Unix o Linux sirve para mostrar la ruta completa del
directorio de trabajo actual.** Ésa es la respuesta oficial.

**La pregunta 41**: **la orden que permite ver los procesos en ejecución en Linux es `top`.** Ésa es la
respuesta oficial.

**La pregunta 25**: **la instrucción que muestra los permisos extendidos de un archivo en Linux es
`getfacl`.** Ésa es la respuesta oficial.

---

**Las tres se apoyan unas en otras**: **la 19 y la 41 usan cada una la respuesta de la otra como
distractor**, y **la 25 mete dos órdenes de administración de servicios y parámetros del núcleo que no
tienen nada que ver con permisos.**

**Los atajos que las hacen memorizables:**

- **`pwd`** es *print working directory*: **imprime el directorio de trabajo.** **La opción a de la
  pregunta describe `passwd`**, que sí cambia la contraseña y **se parece en las letras.**
- **`top`** enseña lo que está arriba: **los procesos que más consumen, en tiempo real.**
- **`getfacl`** es *get file access control list*: **obtén la lista de control de acceso del
  fichero.** **Su pareja es `setfacl`**, que la escribe.

**Y la distinción que la pregunta 25 mide de verdad**: **permisos básicos frente a extendidos.**

| | **Básicos** | **Extendidos** |
|---|---|---|
| **Qué expresan** | **Lectura, escritura y ejecución para dueño, grupo y resto** | **Permisos por usuario o grupo concretos, tantos como haga falta** |
| **Con qué se ven** | `ls -l` | `getfacl` ✔ |
| **Con qué se ponen** | `chmod` | `setfacl` |

## 5. La administración que el punto 17 pide

**El examen ha entrado por las órdenes y el enunciado pide más.** **Lo mínimo que conviene llevar
visto de administración:**

| Tarea | En Linux | En Windows Server |
|---|---|---|
| **Usuarios y grupos** | **Ficheros de sistema y órdenes de alta y baja** | **Directorio Activo, o cuentas locales** |
| **Servicios** | `systemctl` | **La consola de servicios** |
| **Registro y auditoría** | `journalctl` **y los ficheros de registro** | **El visor de eventos** |
| **Programas instalados** | **El gestor de paquetes de la distribución** | **Instaladores y el gestor de paquetes del sistema** |
| **Tareas programadas** | `cron` **y temporizadores del sistema** | **El programador de tareas** |

**Y lo que el enunciado llama «software de base»**: **todo lo que no es aplicación de negocio ni
sistema operativo puro** —bases de datos, servidores de aplicaciones, servidores web, gestores de
copias—. **Es la capa que el administrador mantiene y el usuario no ve.**

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 19 | Para qué sirve `pwd` | d) Mostrar la ruta completa del directorio actual ✔ |
| 25 | Instrucción que muestra los permisos extendidos | c) `getfacl` ✔ |
| 41 | Orden para ver los procesos en ejecución | b) `top` ✔ |
| 72 | Función del gestor de entrada y salida | b) Comunicar dispositivos y subsistemas del modo usuario ✔ |
| 90 | Función del núcleo en Unix o Linux | a) Controlar procesos, memoria y dispositivos ✔ |

**Las cinco respuestas oficiales son correctas**, y **ninguna descansa en la plantilla.**

**El aviso de estudio**: **la tabla de órdenes por familias del epígrafe 4 contesta tres de las cinco
preguntas.** **Es lo más rentable del punto y se practica en una terminal en veinte minutos.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Los manuales de Unix, Linux y Windows Server no se han consultado.** **El cometido de cada orden
   y de cada componente del sistema es de uso universal**, y **coincide con las respuestas
   oficiales.**
2. **La clasificación de núcleos del epígrafe 2 —monolítico, micronúcleo e híbrido— es teoría clásica
   de sistemas operativos**, presentada como conocimiento común. **Ninguna pregunta depende de ella.**
3. **Los nombres de orden se escriben en acentos graves porque son código.** **Su forma larga
   —*print working directory*, *get file access control list*— es la corriente en la documentación del
   sistema**, dada como apoyo de memoria y no como cita.
4. **La tabla de tareas de administración del epígrafe 5 es oficio**, y **ninguna respuesta oficial
   depende de ella.**

**El resto del tema va como oficio y así se declara**: la razón de ser de los dos modos de ejecución,
el argumento de que en Unix el entorno gráfico es un programa más, la idea de que casi todo es un
fichero, los atajos de memoria de cada orden y la distinción entre permisos básicos y extendidos.
**Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo
presenta como si lo estuviera.
