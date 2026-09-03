# Esquema · Tema 14 del específico de Técnica Informática · Arquitectura y administración de sistemas operativos

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de administración de sistemas ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: la entrada y salida (**E/S**, en inglés
**I/O**); la unidad central de proceso (**CPU**); la lista de control de acceso (**ACL**); el
protocolo de control de transmisión sobre el de internet (**TCP/IP**); y los nombres de orden, que van
en acentos graves porque son código y no siglas.

**Cabecera.** Enunciado: puntos 16 y 17 del anexo, que el examen ha tratado como uno · **5
preguntas** · **ninguna lleva figura** · **tres son de órdenes de la línea de comandos y dos de
arquitectura.**

<!-- indice -->

## Índice

- [Qué hace un sistema operativo](#qué-hace-un-sistema-operativo)
- [El núcleo](#el-núcleo)
- [El gestor de entrada y salida](#el-gestor-de-entrada-y-salida)
- [Las órdenes](#las-órdenes)
- [La administración que el enunciado pide](#la-administración-que-el-enunciado-pide)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué hace un sistema operativo

| Función | De qué se ocupa |
|---|---|
| **Gestión de procesos** | **Quién se ejecuta, cuándo y durante cuánto** |
| **Gestión de memoria** | **Qué hay en memoria y dónde** |
| **Gestión de ficheros** | **Cómo se organizan los datos en el almacenamiento** |
| **Gestión de entrada y salida** | **Cómo se habla con los dispositivos** |
| **Protección y seguridad** | **Quién puede hacer qué** |

| Modo | Qué puede hacer | Qué corre ahí |
|---|---|---|
| **Núcleo** | **Todo**: soporte físico y cualquier memoria | **El núcleo y sus controladores** |
| **Usuario** | **Sólo lo suyo**, y pedir el resto por llamada al sistema | **Los programas** |

- **LA RAZÓN DE QUE EXISTAN LOS DOS**: **un error de un programa no puede llevarse el sistema por
  delante.** **Cuando un programa necesita algo del soporte físico, no lo toca: lo pide.**

## El núcleo

- **PREGUNTA 90** · `[exam]` · **La función del núcleo en Unix o Linux es controlar los procesos, la
  memoria y la administración de dispositivos.**

| Opción falsa | Quién lo hace realmente |
|---|---|
| **Gestionar la interfaz gráfica** | **Un servidor gráfico en modo usuario**: en Unix el entorno gráfico es un programa más |
| **Dar servicios de red como TCP/IP** | **La pila está en el núcleo, pero los servicios los dan demonios en modo usuario** |
| **Comunicar usuarios por terminales** | **Programas de usuario** |

- **EL RASGO DE DISEÑO QUE LA PREGUNTA PERSIGUE**: **el núcleo hace lo imprescindible y todo lo demás
  son programas.** **Por eso se cambia el escritorio sin tocar el sistema** y **un servidor Linux
  puede no tener entorno gráfico.**

| Tipo de núcleo | Qué mete dentro | Ejemplo |
|---|---|---|
| **Monolítico** | **Procesos, memoria, ficheros, red y controladores** | **Linux** |
| **Micronúcleo** | **Lo mínimo; el resto en modo usuario** | **Minix** |
| **Híbrido** | **Monolítico con partes modulares** | **Windows** |

- **LINUX ES MONOLÍTICO Y A LA VEZ MODULAR**: **los controladores se cargan y descargan en caliente**,
  que es lo que permite añadir soporte físico sin recompilar.

## El gestor de entrada y salida

- **PREGUNTA 72** · `[exam]` · **Permite la comunicación entre dispositivos y subsistemas del modo
  usuario.**

| Opción falsa | Quién lo hace |
|---|---|
| **Operaciones aritmético-lógicas** | **La unidad aritmético-lógica del procesador**: soporte físico |
| **Administrar procesos del sistema** | **El planificador y el gestor de procesos** |
| **Controlar la red** | **La pila de red**, subsistema propio |

- **QUÉ HACE, EN TRES LÍNEAS**: **recibe la petición del programa, la convierte en órdenes para el
  controlador del dispositivo y devuelve el resultado.** **Su valor está en que el programa no tiene
  que saber qué disco ni qué impresora hay debajo.**
- **DE AHÍ LA IDEA QUE UNIX LLEVÓ MÁS LEJOS QUE NADIE**: **casi todo es un fichero.** **Un disco, un
  terminal y hasta un dispositivo de red se manejan con las llamadas de un fichero corriente.**

## Las órdenes

| Familia | Órdenes |
|---|---|
| **Dónde estoy y qué hay** | `pwd`, `ls`, `cd` |
| **Qué se está ejecutando** | `top` y `htop` **(tiempo real)**, `ps` **(instantánea)** |
| **Permisos** | `chmod` y `chown` **(básicos)**, `getfacl` y `setfacl` **(extendidos)** |
| **Servicios** | `systemctl` **(gestión)**, `journalctl` **(registro)** |
| **Parámetros del núcleo** | `sysctl` |
| **Buscar dentro de ficheros** | `grep` |

- **PREGUNTA 19** · `[exam]` · **`pwd` muestra la ruta completa del directorio de trabajo actual.**
- **PREGUNTA 41** · `[exam]` · **Los procesos en ejecución se ven con `top`.**
- **PREGUNTA 25** · `[exam]` · **Los permisos extendidos se muestran con `getfacl`.**
- **LAS TRES SE APOYAN UNAS EN OTRAS**: **la 19 y la 41 usan cada una la respuesta de la otra como
  distractor**, y **la 25 mete dos órdenes de servicios y de parámetros del núcleo que nada tienen que
  ver con permisos.**
- **LOS ATAJOS**: **`pwd` es *print working directory*** —la opción falsa describe `passwd`, que se
  parece en las letras—; **`top` enseña lo que está arriba**: los procesos que más consumen;
  **`getfacl` es *get file access control list***, y su pareja `setfacl` la escribe.

| | **Básicos** | **Extendidos** |
|---|---|---|
| **Qué expresan** | **Lectura, escritura y ejecución para dueño, grupo y resto** | **Permisos por usuario o grupo concretos** |
| **Con qué se ven** | `ls -l` | `getfacl` ✔ |
| **Con qué se ponen** | `chmod` | `setfacl` |

## La administración que el enunciado pide

| Tarea | En Linux | En Windows Server |
|---|---|---|
| **Usuarios y grupos** | **Ficheros de sistema y órdenes de alta y baja** | **Directorio Activo, o cuentas locales** |
| **Servicios** | `systemctl` | **La consola de servicios** |
| **Registro y auditoría** | `journalctl` **y los ficheros de registro** | **El visor de eventos** |
| **Programas instalados** | **El gestor de paquetes de la distribución** | **Instaladores y gestor de paquetes** |
| **Tareas programadas** | `cron` **y temporizadores del sistema** | **El programador de tareas** |

- **QUÉ ES EL «SOFTWARE DE BASE» DEL ENUNCIADO**: **todo lo que no es aplicación de negocio ni sistema
  operativo puro** —bases de datos, servidores de aplicaciones y web, gestores de copias—. **La capa
  que el administrador mantiene y el usuario no ve.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 19 | Para qué sirve `pwd` | d) Mostrar la ruta completa del directorio actual ✔ |
| 25 | Instrucción de permisos extendidos | c) `getfacl` ✔ |
| 41 | Orden para ver procesos en ejecución | b) `top` ✔ |
| 72 | Función del gestor de entrada y salida | b) Comunicar dispositivos y subsistemas del modo usuario ✔ |
| 90 | Función del núcleo en Unix o Linux | a) Controlar procesos, memoria y dispositivos ✔ |

**Las cinco oficiales son correctas** · **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**la tabla de órdenes por familias contesta tres de las cinco.** **Es lo más rentable del punto y se
practica en una terminal en veinte minutos.**
