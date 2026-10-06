# Tema 9 del específico de Operador/a Informático · Administración del sistema operativo Linux

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 9 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Páginas de manual de Linux (proyecto man-pages, servidas en man7.org), *Filesystem Hierarchy Standard* 3.0 de la Linux Foundation, manuales GNU de grep, sed, gawk y tar, documentación oficial de Ubuntu Server y páginas de versiones de Ubuntu y Debian. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Ubuntu 26.04 LTS y Debian 13 como distribuciones de referencia; las páginas citadas, en línea el 05-10-2026 y leídas ese día |
| Extensión | 18.000 palabras aproximadamente (con los ejemplos de órdenes) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); proyecto GNU (*GNU's Not
Unix*), autor de buena parte de las herramientas del sistema; versión de soporte a largo plazo (LTS,
*long-term support*); imagen de disco óptico (ISO); bus serie universal (USB); disco versátil digital (DVD); protocolo de
configuración dinámica de equipos (DHCP); intérprete de órdenes seguro remoto (SSH, *Secure Shell*);
norma de jerarquía del sistema de ficheros (FHS, *Filesystem Hierarchy Standard*); identificador de
usuario (UID) y de grupo (GID); lista de control de acceso (ACL, *access control list*); interfaz de
sistema operativo portable (POSIX), norma del Instituto de Ingenieros Eléctricos y Electrónicos (IEEE);
tiempo universal coordinado (UTC); identificador de proceso (PID); interfaz de firmware extensible
(EFI y su versión unificada, UEFI); gestor de arranque GRUB (*GRand Unified Bootloader*); registro de
arranque maestro (MBR, *master boot record*) y tabla de particiones GUID (GPT, *GUID partition
table*), donde GUID es el identificador único global; identificador único universal (UUID);
gestor de volúmenes lógicos (LVM, *Logical Volume Manager*) con sus volúmenes físicos (PV), grupos de
volúmenes (VG) y volúmenes lógicos (LV); conjunto redundante de discos independientes (RAID);
configuración de clave unificada de Linux (LUKS, *Linux Unified Key Setup*); herramienta avanzada de
empaquetado (APT, *Advanced Packaging Tool*); gestor de paquetes RPM (*RPM Package Manager*) y su
interfaz DNF; sistema de ficheros en red (NFS); red de área extensa (WAN); expresión regular básica
(BRE) y extendida (ERE); protocolo de control de transmisión (TCP); unidad central de proceso (CPU);
entrada y salida (E/S). Los nombres de orden, de fichero y de opción van en acentos graves porque son
código. Dentro de las citas quedan, tal como los escribe la fuente y sin desarrollar porque su desarrollo
no se ha leído en ella: BSD (la sintaxis de opciones de `ps` sin guion), CPIO (el formato del
*initramfs*), SGI (un tipo de tabla de particiones de `fdisk`), YUM (el gestor al que sucede DNF),
STDOUT (la salida estándar), y LINEAR y FSUSE%, que son un nivel de `mdadm` y una columna de `lsblk`.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 9): «Administración del
> sistema operativo Linux: instalación, estructura y sistema de archivos, usuarios y grupos,
> utilización del shell, arranques y paradas, herramientas básicas de administración, sistemas de
> ficheros, gestión de discos, administración del software, salvaguarda y restauración, filtros grep,
> editor de flujo sed y lenguaje awk.»

Qué se puede preguntar: qué distribución LTS de Ubuntu está vigente, cada cuánto salen y cuánto se
mantienen; qué requisitos y pasos tiene la instalación de Ubuntu Server; qué guarda cada directorio
de la jerarquía (`/etc`, `/var/log`, `/home`, `/proc`, `/tmp`…); cómo se leen y se cambian los
permisos en notación simbólica y octal, qué hacen el *sticky bit*, `umask`, `chown`, `getfacl` y
`setfacl`; qué campos tienen `/etc/passwd`, `/etc/shadow` y `/etc/group`; qué órdenes crean,
modifican, bloquean y borran usuarios y grupos (`useradd`, `usermod -aG`, `userdel -r`, `passwd -l`,
`groupadd`, `adduser`) y por qué Ubuntu usa `sudo` y no la cuenta root; qué hacen `|`, `>`, `>>`,
`2>&1`, `&&`, `||`, `$?`, `*`, `?`, las comillas simples y dobles y la primera línea `#!` de un
script; cómo arranca el sistema (firmware, gestor de arranque, núcleo, initramfs, systemd) y qué
*target* corresponde a cada antiguo nivel de ejecución; qué hacen `systemctl start`, `enable`,
`status`, `isolate`, `set-default`, `shutdown -r +5` y `shutdown -c`; cómo se consultan el registro
(`journalctl -u`, `-f`, `-b`, `-p`), los procesos (`ps`, `top`, `kill`, `nice`) y las tareas
programadas (`crontab -e`, los cinco campos de tiempo); qué es cada campo de `/etc/fstab` y por qué
se recomienda el UUID; con qué se particiona (`fdisk`, `parted`), se formatea (`mkfs.ext4`), se monta
(`mount`), se comprueba (`fsck`) y se mide (`df`, `du`, `lsblk`) un disco; qué son PV, VG y LV en LVM;
qué niveles de RAID admite `mdadm`; qué diferencia `apt` de `dpkg` y `remove` de `purge`; qué hacen
`tar -czf`, `-tzvf`, `-xzvf -C`, `rsync -a` y `dd`; y qué hacen las opciones `-i`, `-v`, `-c`, `-l`,
`-n`, `-r`, `-E` de `grep`, el comando `s///g` y las opciones `-n` e `-i` de `sed`, y `$1`, `$NF`,
`NR`, `-F`, `BEGIN` y `END` en `awk`. En la aplicación práctica: leer una línea de órdenes y decir qué
hace, interpretar una salida de `ls -l` o una línea de `crontab` o de `fstab`, o escoger la orden que
resuelve una tarea de administración.

<!-- indice -->

## Índice

- [1. Instalación](#1-instalación)
  - [Qué distribución se instala](#qué-distribución-se-instala)
  - [Antes de instalar](#antes-de-instalar)
  - [Arrancar el instalador](#arrancar-el-instalador)
  - [Los pasos del instalador](#los-pasos-del-instalador)
- [2. Estructura y sistema de archivos](#2-estructura-y-sistema-de-archivos)
  - [Un solo árbol](#un-solo-árbol)
  - [La norma: FHS 3.0](#la-norma-fhs-30)
  - [Tipos de fichero](#tipos-de-fichero)
  - [Permisos básicos](#permisos-básicos)
  - [Permisos extendidos: ACL](#permisos-extendidos-acl)
- [3. Usuarios y grupos](#3-usuarios-y-grupos)
  - [Las cuentas locales están en tres ficheros de texto](#las-cuentas-locales-están-en-tres-ficheros-de-texto)
  - [Tipos de usuario por UID (Ubuntu)](#tipos-de-usuario-por-uid-ubuntu)
  - [Root y sudo en Ubuntu](#root-y-sudo-en-ubuntu)
  - [Las órdenes](#las-órdenes)
  - [Directorios personales y contraseñas](#directorios-personales-y-contraseñas)
- [4. Utilización del shell](#4-utilización-del-shell)
  - [Qué es el shell](#qué-es-el-shell)
  - [Moverse y mirar](#moverse-y-mirar)
  - [La ayuda](#la-ayuda)
  - [Comodines](#comodines)
  - [Comillas y escape](#comillas-y-escape)
  - [Variables](#variables)
  - [Redirección](#redirección)
  - [Tuberías y listas](#tuberías-y-listas)
  - [Scripts](#scripts)
- [5. Arranques y paradas](#5-arranques-y-paradas)
  - [La secuencia de arranque](#la-secuencia-de-arranque)
  - [systemd y las unidades](#systemd-y-las-unidades)
  - [Los *targets* y los antiguos niveles de ejecución](#los-targets-y-los-antiguos-niveles-de-ejecución)
  - [Parar y reiniciar](#parar-y-reiniciar)
- [6. Herramientas básicas de administración](#6-herramientas-básicas-de-administración)
  - [Servicios: systemctl](#servicios-systemctl)
  - [Registro: journalctl, /var/log y dmesg](#registro-journalctl-varlog-y-dmesg)
  - [Procesos](#procesos)
  - [Tareas programadas: cron](#tareas-programadas-cron)
  - [Información del sistema y de la red](#información-del-sistema-y-de-la-red)
  - [Equivalencias con Windows](#equivalencias-con-windows)
- [7. Sistemas de ficheros](#7-sistemas-de-ficheros)
  - [Qué tipos hay](#qué-tipos-hay)
  - [Crear un sistema de ficheros: mkfs](#crear-un-sistema-de-ficheros-mkfs)
  - [Montar y desmontar](#montar-y-desmontar)
  - [/etc/fstab](#etcfstab)
  - [Comprobar y reparar: fsck](#comprobar-y-reparar-fsck)
  - [Intercambio (swap)](#intercambio-swap)
- [8. Gestión de discos](#8-gestión-de-discos)
  - [Discos y particiones como ficheros de /dev](#discos-y-particiones-como-ficheros-de-dev)
  - [Ver qué hay](#ver-qué-hay)
  - [Particionar: fdisk y parted](#particionar-fdisk-y-parted)
  - [LVM: volúmenes lógicos](#lvm-volúmenes-lógicos)
  - [RAID por software: mdadm](#raid-por-software-mdadm)
  - [Cifrado de disco: LUKS](#cifrado-de-disco-luks)
- [9. Administración del software](#9-administración-del-software)
  - [Paquetes y repositorios](#paquetes-y-repositorios)
  - [APT (Debian y Ubuntu)](#apt-debian-y-ubuntu)
  - [dpkg](#dpkg)
  - [La familia RPM: rpm y dnf](#la-familia-rpm-rpm-y-dnf)
- [10. Salvaguarda y restauración](#10-salvaguarda-y-restauración)
  - [El plan](#el-plan)
  - [tar: archivar y restaurar](#tar-archivar-y-restaurar)
  - [El script de copia de la documentación de Ubuntu](#el-script-de-copia-de-la-documentación-de-ubuntu)
  - [Copias incrementales con tar](#copias-incrementales-con-tar)
  - [rsync: copiar y sincronizar](#rsync-copiar-y-sincronizar)
  - [dd: copia en bruto](#dd-copia-en-bruto)
  - [Qué copiar y qué no](#qué-copiar-y-qué-no)
- [11. Filtros: grep](#11-filtros-grep)
  - [Qué hace](#qué-hace)
  - [Opciones](#opciones)
  - [Expresiones regulares](#expresiones-regulares)
- [12. Editor de flujo: sed](#12-editor-de-flujo-sed)
  - [Qué es](#qué-es)
  - [Sustituir: s](#sustituir-s)
  - [Direcciones: a qué líneas](#direcciones-a-qué-líneas)
  - [Otras órdenes y opciones](#otras-órdenes-y-opciones)
- [13. Lenguaje awk](#13-lenguaje-awk)
  - [Qué es](#qué-es-1)
  - [Campos y registros](#campos-y-registros)
  - [Patrones y acciones](#patrones-y-acciones)
  - [print y printf](#print-y-printf)
  - [Ejemplos de administración](#ejemplos-de-administración)
  - [Cuál usar](#cuál-usar)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Instalación

### Qué distribución se instala

Linux, en sentido estricto, es el núcleo; lo que se instala es una distribución, que lo acompaña de
las herramientas GNU, un gestor de paquetes y un instalador. Las fuentes de este tema son las de las
dos distribuciones de la familia Debian más extendidas en servidores, Ubuntu y Debian, y se señala
cuando algo cambia en la familia Red Hat (RPM). Que la distribución es «núcleo más herramientas» es
oficio, no definición de una fuente leída.

*Ubuntu.* La página oficial del ciclo de versiones dice: **«Ubuntu releases a new version every six
months. Releases of Ubuntu get a development codename ('Resolute Raccoon') and are versioned by the
year and month of delivery – for example, Ubuntu 26.04 was released in April 2026.»** (Ubuntu saca una
versión cada seis meses, con nombre en clave, y se numera por año y mes: la 26.04 salió en abril de
2026.) Hay dos clases de versión:

| Clase | Qué dice la fuente | Para quién |
|---|---|---|
| LTS | **«LTS are released every two years and receive 5 years of standard security maintenance.»** (cada dos años; cinco años de mantenimiento de seguridad estándar) | Producción: **«production environments should use the LTS version»** |
| Intermedia | **«They provide cutting-edge features and hardware support every six months, but with only 9 months of updates.»** (novedades cada seis meses, pero sólo nueve meses de actualizaciones) | Quien prima la rapidez y el ensayo de novedades |

A la fecha del tema, la LTS en curso es la *26.04 LTS*; la página sigue listando la anterior,
24.04 LTS, dentro de su mantenimiento.

*Debian.* La página de versiones dice: **«The current stable distribution of Debian is version 13,
codenamed trixie.»** (la estable vigente es la 13, *trixie*), y su última revisión, la **«13.7, was
released on September 12th, 2026»**. La anterior, *bookworm*, figura como **«Current oldstable
release»**.

La familia RPM (Red Hat, Fedora y derivadas) cambia sobre todo el gestor de paquetes (epígrafe 9).
Sus versiones vigentes no se han consultado y el tema no las da.

### Antes de instalar

El tutorial oficial de instalación básica de Ubuntu Server es la fuente de este apartado.

- Arquitecturas. Ubuntu Server **«supports four 64-bit architectures»**: *amd64* (Intel/AMD de 64
  bits), *arm64* (ARM de 64 bits), *ppc64el* (POWER8 y POWER9) y *s390x* (IBM Z y LinuxONE).
- Requisitos mínimos recomendados para el tutorial: **«RAM: 2 GB or more»** y **«Disk: 5 GB or
  more»** (2 GB de memoria y 5 GB de disco, o más).
- Copia previa: **«Before installing Ubuntu Server Edition you should make sure all data on the system
  is backed up.»** La razón que da: si ya hubo otro sistema, probablemente habrá que reparticionar, y
  **«Any time you partition your disk, you should be prepared to lose all data on the disk should you
  make a mistake or something goes wrong during partitioning.»** (cada vez que se particiona hay que
  estar preparado para perder todo el disco si algo sale mal).
- La imagen: la ISO de servidor se descarga de `releases.ubuntu.com` (**«server install image»**), y
  **«the server download includes the installer»** (la descarga ya trae el instalador).
- El soporte de arranque: hay varias formas, pero **«the simplest and most common way is to create a
  bootable USB stick to boot from»** (lo más sencillo y corriente es un USB de arranque).

### Arrancar el instalador

Se pincha el USB y se enciende el equipo. **«Most computers will automatically boot from USB or DVD,
though in some cases manufacturers disable this feature to improve boot times.»** Si no aparece la
pantalla de bienvenida, hay que entrar en el menú de arranque del firmware con la tecla que indique el
equipo al encender: **«Depending on the manufacturer, this could be Escape, F2, F10 or F12.»** Se
mantiene pulsada al reiniciar hasta que sale el menú y se elige la unidad con el instalador.

### Los pasos del instalador

El tutorial advierte que el instalador tiene valores por defecto razonables, de modo que en una
primera instalación basta con aceptarlos. Los pasos, en su orden:

1. **«Choose your language»**: el idioma.
2. **«Update the installer (if offered)»**: actualizar el instalador si lo ofrece.
3. **«Select your keyboard layout»**: la distribución del teclado.
4. La red: **«Do not configure networking»** (no configurarla), porque **«the installer attempts to
   configure wired network interfaces via DHCP, but you can continue without networking if this
   fails»** (intenta configurar la red cableada por DHCP y, si falla, se puede seguir sin red).
5. No configurar *proxy* ni réplica propia salvo que la red lo exija.
6. El almacenamiento: **«leave "use an entire disk" checked»** (dejar marcado usar el disco entero),
   elegir el disco, «Done» y confirmar la instalación.
7. **«Enter a username, hostname and password»**: usuario, nombre del equipo y contraseña.
8. En las pantallas de SSH y de *snap* (paquetes de Canonical), «Done».
9. Al acabar, **«Select restart when this is complete, and log in using the username and password
   provided»**: reiniciar y entrar con el usuario creado.

Dos consecuencias que se ven en epígrafes posteriores: el usuario creado en el paso 7 queda en el
grupo `sudo` y es el administrador, porque la cuenta root viene sin contraseña utilizable (epígrafe
3); y la opción «usar el disco entero» deja el particionado hecho por el instalador, que después se
consulta con `lsblk` o `fdisk -l` (epígrafe 8).

Para el puesto, lo que conviene retener es el orden (copia, imagen, USB, arranque desde el firmware,
idioma, teclado, red, disco, usuario) y los dos riesgos: perder datos al particionar y no arrancar
desde el USB por la configuración del firmware. Esta síntesis es oficio.

## 2. Estructura y sistema de archivos

### Un solo árbol

Linux no tiene letras de unidad. La página de `mount(8)` lo explica así: **«All files accessible in a
Unix system are arranged in one big tree, the file hierarchy, rooted at /. These files can be spread
out over several devices. The mount command serves to attach the filesystem found on some device to
the big file tree.»** (todos los ficheros forman un gran árbol con raíz en `/`; pueden estar en varios
dispositivos, y `mount` engancha el sistema de ficheros de cada uno a ese árbol). Un segundo disco, un
USB o un recurso de red no aparecen como «D:», sino como un directorio más del árbol (el punto de
montaje, epígrafe 7).

Una ruta absoluta empieza en `/` (`/etc/passwd`); una relativa se resuelve desde el directorio de
trabajo, que muestra `pwd` (epígrafe 4). Que la ruta relativa parte del directorio actual es oficio.

### La norma: FHS 3.0

El reparto de directorios lo fija la *Filesystem Hierarchy Standard*, versión 3.0, publicada por la
Linux Foundation: **«This standard consists of a set of requirements and guidelines for file and
directory placement under UNIX-like operating systems.»** (requisitos y pautas para colocar ficheros y
directorios en sistemas tipo Unix). Los rótulos de la tabla son los de la propia norma; la columna de
la derecha añade, cuando la hay, la descripción de la página de manual `hier(7)`.

| Directorio | Rótulo de la FHS 3.0 | Precisión de `hier(7)` u observación |
|---|---|---|
| `/` | Raíz | **«This is the root directory. This is where the whole tree starts.»** |
| `/bin` | **«Essential user command binaries (for use by all users)»** | **«executable programs which are needed in single user mode and to bring the system up or repair it»** |
| `/boot` | **«Static files of the boot loader»** | **«This directory holds only the files which are needed during the boot process.»** |
| `/dev` | **«Device files»** | **«Special or device files, which refer to physical devices.»** |
| `/etc` | **«Host-specific system configuration»** | **«Contains configuration files which are local to the machine.»** |
| `/home` | **«User home directories (optional)»** | Los directorios personales de los usuarios |
| `/lib` | **«Essential shared libraries and kernel modules»** | Bibliotecas para arrancar y para las órdenes de la raíz |
| `/media` | **«Mount point for removable media»** | Soportes extraíbles |
| `/mnt` | **«Mount point for a temporarily mounted filesystem»** | Montajes temporales |
| `/opt` | **«Add-on application software packages»** | Aplicaciones añadidas |
| `/proc` | **«Kernel and process information virtual filesystem»** (anexo de Linux) | **«a mount point for the proc filesystem, which provides information about running processes and the kernel»** |
| `/root` | **«Home directory for the root user (optional)»** | Directorio personal del superusuario, fuera de `/home` |
| `/run` | **«Run-time variable data»** | Datos de los procesos en marcha |
| `/sbin` | **«System binaries»** | **«Like /bin, this directory holds commands needed to boot the system, but which are usually not executed by normal users.»** |
| `/srv` | **«Data for services provided by this system»** | Datos que sirve el equipo |
| `/sys` | **«Kernel and system information virtual filesystem»** (anexo de Linux) | Virtual, como `/proc` |
| `/tmp` | **«Temporary files»** | **«temporary files which may be deleted with no notice, such as by a regular job or at system boot up»** (pueden borrarse sin aviso, incluso al arrancar) |
| `/usr` | **«Secondary hierarchy»** | **«It should hold only shareable, read-only data»** (sólo datos compartibles y de sólo lectura) |
| `/usr/bin` | **«Most user commands»** | **«This is the primary directory for executable programs.»** |
| `/usr/sbin` | **«Non-essential standard system binaries»** | Administración no necesaria para arrancar |
| `/usr/local` | **«Local hierarchy»** | **«This is where programs which are local to the site typically go.»** |
| `/var` | **«Variable data»** | Lo que cambia con el uso |
| `/var/log` | **«Log files and directories»** | Los ficheros de registro clásicos (el diario de systemd, en el epígrafe 6) |
| `/var/spool` | **«Application spool data»** | Colas; `hier(7)` lista dentro `cron`, `lpd` (impresión) y `mail` (éste, **«Replaced by /var/mail»**) |
| `/var/tmp` | **«Temporary files preserved between system reboots»** | A diferencia de `/tmp`, sobreviven al reinicio |

Para el test, las parejas que se confunden: `/bin` frente a `/sbin` (órdenes de todos frente a órdenes
de administración), `/tmp` frente a `/var/tmp` (se pierde o se conserva al reiniciar), `/home` frente a
`/root` (el directorio del superusuario no cuelga de `/home`) y `/etc` frente a `/var` (configuración
frente a datos que cambian). Este cuadro de parejas es oficio sacado de la tabla.

La FHS 3.0 es de 2015. Si hay una versión posterior no se ha comprobado; tampoco se ha comprobado en
fuente la fusión de `/bin` en `/usr/bin` que hacen algunas distribuciones, y el tema no la afirma.

### Tipos de fichero

Para Linux un directorio, un dispositivo o un enlace son también ficheros, de tipos distintos. El
manual de GNU coreutils da la letra con que `ls -l` muestra cada tipo en el primer carácter de la
línea:

| Letra | Tipo (literal del manual) |
|---|---|
| `-` | **«regular file»** (fichero corriente) |
| `d` | **«directory»** |
| `l` | **«symbolic link»** (enlace simbólico) |
| `b` | **«block special file»** (dispositivo de bloques, como un disco) |
| `c` | **«character special file»** (dispositivo de caracteres, como un terminal) |
| `p` | **«FIFO (named pipe)»** (tubería con nombre) |
| `s` | **«socket»** |

Que un disco es de bloques y un terminal de caracteres es oficio; el manual sólo da los nombres.

Los enlaces se crean con `ln`: **«Create hard links by default, symbolic links with --symbolic.»**
(por defecto, enlaces duros; con `-s`, simbólicos). `ln -s /var/log/syslog registro` crea un acceso
`registro` que apunta a la ruta. **«When creating hard links, each TARGET must exist.»** (el duro exige
que exista el destino); el simbólico guarda una ruta, que puede no existir.

### Permisos básicos

`ls -l` muestra, según el manual de coreutils, **«the file type, file mode bits, number of hard links,
owner name, group name, size, and timestamp»** (tipo, permisos, número de enlaces duros, dueño, grupo,
tamaño y fecha, normalmente la de modificación). Ejemplo del propio manual:

```
-rw-r--r-- 1    0 Jun 10 12:27 f1
drwxr-xr-x 3 4096 Jun 10 12:27 sub/
```

Los nueve caracteres tras el tipo son tres grupos de tres (`rwx`) para tres clases de usuario. Según
`chmod(1)`: **«the user who owns it (u), other users in the file's group (g), other users not in the
file's group (o), or all users (a)»** (el dueño, los demás del grupo del fichero, el resto y todos), y
los permisos son **«read (r), write (w), execute (or search for directories) (x)»**. En un directorio,
explica el manual de coreutils, leer es listar su contenido, escribir es **«permission to create and
remove files in the directory»** (crear y borrar ficheros dentro) y ejecutar es **«permission to
access files in the directory»** (entrar y acceder a lo que contiene).

`chmod` cambia los permisos de dos maneras:

- *Simbólica*: **«The format of a symbolic mode is [ugoa...][[-+=][perms...]...]»**. El `+` añade,
  el `-` quita y el `=` deja exactamente lo indicado. `chmod u+x copia.sh` da ejecución al dueño;
  `chmod go-w informe.txt` quita escritura a grupo y resto.
- *Octal*: **«A numeric mode is from one to four octal digits (0-7), derived by adding up the bits
  with values 4, 2, and 1.»** Lectura 4, escritura 2, ejecución 1; un dígito para el dueño, otro para
  el grupo y otro para el resto. Si son cuatro, **«The first digit selects the set user ID (4) and set
  group ID (2) and restricted deletion or sticky (1) attributes.»**

| Octal | Cadena | Lectura |
|---|---|---|
| `755` | `rwxr-xr-x` | El dueño todo; grupo y resto, leer y ejecutar |
| `750` | `rwxr-x---` | El resto, nada (lo que Ubuntu da a los directorios personales, epígrafe 3) |
| `644` | `rw-r--r--` | El dueño lee y escribe; los demás, sólo leer |
| `600` | `rw-------` | Sólo el dueño |

Las conversiones de la tabla son aritmética del manual (4+2+1 = 7, 4+1 = 5, 4+2 = 6).

Los bits especiales, según coreutils:

- *setuid*: **«On execution, set the process's effective user ID to that of the file.»** (el programa
  se ejecuta con la identidad de su dueño).
- *setgid*: igual con el grupo; en directorios, **«give files created in the directory the same group
  as the directory»** (lo creado dentro hereda el grupo del directorio).
- *Sticky bit* o indicador de borrado restringido, según `chmod(1)`: en un directorio **«prevents
  unprivileged users from removing or renaming a file in the directory unless they own the file or
  the directory»** (nadie sin privilegios borra ni renombra lo que no es suyo) y **«is commonly found
  on world-writable directories like /tmp»**.

En `ls -l`, el manual de coreutils explica que estos bits se ven en el tercer carácter de cada trío:
`s` si están *setuid* o *setgid* con ejecución y `S` sin ella; `t` si está el *sticky bit* con
ejecución para el resto y `T` sin ella.

*Dueño y grupo.* `chown` **«changes the user and/or group ownership of each given file»**;
`chown ana:prensa fichero` cambia ambos (dueño y grupo, separados por dos puntos, **«with no spaces
between them»**). `chgrp` cambia sólo el grupo.

*`umask`.* Los permisos con que nace un fichero los recorta la máscara del proceso. Según
`umask(2)`, **«permissions in the umask are turned off»** (los bits de la máscara se apagan) y **«The
typical default value for the process umask is S_IWGRP | S_IWOTH (octal 022)»**; con una petición de
`0666` sale **«0666 & ~022 = 0644; i.e., rw-r--r--»**. La orden `umask` del intérprete la muestra o la
cambia: **«If mode is omitted, umask prints the current value of the mask.»**

### Permisos extendidos: ACL

Cuando los tres grupos no bastan (dar lectura a un usuario concreto que no es dueño ni del grupo), se
usan listas de control de acceso. `getfacl` **«displays the file name, owner, the group, and the Access
Control List (ACL)»**, y si el sistema de ficheros no las admite, **«displays the access permissions
defined by the traditional file mode permission bits»**. `setfacl` **«sets Access Control Lists (ACLs)
of files and directories»**. Ejemplos de su página de manual:

```
setfacl -m u:lisa:r file        # da lectura a la usuaria lisa
setfacl -x g:staff file         # quita la entrada del grupo staff
getfacl file1 | setfacl --set-file=- file2   # copia la ACL de un fichero a otro
```

`getfacl` es *get file access control list*: obtén la lista de control de acceso del fichero. Su
pareja es `setfacl`, que la escribe.

Y la distinción que hay que llevar: permisos básicos frente a extendidos.

| | Básicos | Extendidos |
|---|---|---|
| Qué expresan | Lectura, escritura y ejecución para dueño, grupo y resto | Permisos por usuario o grupo concretos, tantos como haga falta |
| Con qué se ven | `ls -l` | `getfacl` |
| Con qué se ponen | `chmod` | `setfacl` |

## 3. Usuarios y grupos

### Las cuentas locales están en tres ficheros de texto

La documentación de Ubuntu Server lo resume: **«Local users and groups are those defined in the
/etc/passwd and /etc/group files, respectively.»** Mediante el mecanismo NSS (*Name Service Switch*)
las cuentas pueden venir también de fuera (Active Directory, Samba, OpenLDAP), pero eso, dice la
misma página, se gestiona de otro modo y no es objeto de este tema.

*`/etc/passwd`.* **«The /etc/passwd file is a text file that describes user login accounts for the
system. It should have read permission allowed for all users (many utilities, like ls(1) use it to
map user IDs to usernames), but write access only for the superuser.»** (lo leen todos, porque muchas
utilidades traducen UID a nombre con él, pero sólo lo escribe el superusuario). **«Each line of the
file describes a single user, and contains seven colon-separated fields»**:

```
name:password:UID:GID:GECOS:directory:shell
root:x:0:0:root:/root:/bin/bash
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
```

(El formato es de `passwd(5)`; las dos líneas de ejemplo, de la documentación de Ubuntu.)

| Campo | Qué es (`passwd(5)`) |
|---|---|
| 1 `name` | **«the user's login name»**; no debe llevar mayúsculas |
| 2 `password` | **«either the encrypted user password, an asterisk (\*), or the letter 'x'»** |
| 3 `UID` | **«The privileged root login account (superuser) has the user ID 0.»** |
| 4 `GID` | **«the numeric primary group ID for this user»**; los grupos adicionales van en `/etc/group` |
| 5 `GECOS` | Comentario opcional, **«Usually, it contains the full username.»** |
| 6 `directory` | **«the user's home directory»**; fija la variable `HOME` |
| 7 `shell` | **«the program to run at login (if empty, use /bin/sh)»**; fija `SHELL` |

La `x` del segundo campo significa que la contraseña no está ahí: **«/etc/passwd has an 'x' character
in the password field, and the encrypted passwords are in /etc/shadow, which is readable by the
superuser only.»**

*`/etc/shadow`.* **«shadow is a file which contains the password information for the system's
accounts and optional aging information.»** **«This file must not be readable by regular users if
password security is to be maintained.»** Tiene nueve campos separados por dos puntos: nombre,
contraseña cifrada, fecha del último cambio, edad mínima, edad máxima, periodo de aviso, periodo de
inactividad, fecha de caducidad de la cuenta y un campo reservado. Dos detalles preguntables:

- **«If the password field begins with an exclamation mark !, the password is locked.»** (una `!` al
  principio = contraseña bloqueada; es lo que ponen `passwd -l` y `usermod -L`).
- La fecha del último cambio se cuenta en **«number of days since 1970-01-01 00:00:00 UTC»**, y **«The
  value 0 indicates that the user must change their password the next time they log in»** (un 0
  obliga a cambiarla en el próximo inicio de sesión).

*`/etc/group`.* **«The /etc/group file is a text file that defines the groups on the system. There
is one entry per line, with the following format: group_name:password:GID:user_list»**; el último
campo es **«a list of the usernames that are members of this group, separated by commas»**. Las
contraseñas de grupo cifradas van en `/etc/gshadow`.

*Grupo principal y grupos suplementarios.* Cada usuario tiene un grupo principal (el GID de
`/etc/passwd`) y puede pertenecer a otros, que se anotan en el cuarto campo de `/etc/group`. `id`
muestra los dos: **«print real and effective user and group IDs»**.

### Tipos de usuario por UID (Ubuntu)

La documentación de Ubuntu distingue **«basically three types of local users»**:

| Tipo | UID | Literal |
|---|---|---|
| Del sistema, preinstalados | 0 a 99 | **«system users essential to a working Linux system, like root, man, lp, and others»** |
| Del sistema, dinámicos | 100 a 999 | **«created dynamically, as services are installed»** |
| Corrientes | Desde 1000 hasta, por convenio, 59999 | **«usable for "real" users, generally representing persons using the system»** |

Y un caso aparte: **«By convention, the nobody users has an UID of 65534.»** [sic: *users*], herencia
de cuando los UID eran de 16 bits.

Para listar los usuarios locales, la misma página propone:

```
cat /etc/passwd | cut -d : -f 1
```

que **«will cut each line at the first column, using the ":" character as the delimiter»** (corta cada
línea por los dos puntos y se queda con el primer campo). `getent passwd`, en cambio, lista todas las
cuentas que vea el sistema, incluidas las de directorios remotos si los hay configurados.

### Root y sudo en Ubuntu

**«Ubuntu developers decided to disable the administrative root account by default in all Ubuntu
installations. This does not mean that the root account has been deleted, or that it may not be
accessed. Instead, it has been given a password hash that matches no possible value, and so may not
log in directly by itself.»** (la cuenta root existe, pero con una contraseña que no coincide con
nada, así que no puede entrar directamente.)

En su lugar se usa `sudo`: **«sudo allows an authorized user to temporarily elevate their privileges
using their own password instead of having to know the password belonging to the root account. This
provides accountability for all user actions»** (eleva privilegios con la contraseña propia, sin
conocer la de root, y deja rastro de quién hace qué). Y quién puede: **«By default, the initial user
created by the Ubuntu installer is a member of the group sudo which is added to the file /etc/sudoers
as an authorized sudo user. To give any other account full root access through sudo, add them to the
sudo group.»**

- Habilitar root (darle contraseña): `sudo passwd`. Volver a bloquearla: `sudo passwd -l root`.
- Desde Ubuntu 25.10, **«sudo is provided by the sudo-rs package (a rust implementation)»**; la
  versión clásica sigue instalada con sufijo (`sudo.ws`) en 25.10 y 26.04 LTS, y la página asegura que
  lo que explica vale con las dos.
- La página de manual de la `sudo` clásica: **«sudo, allows a permitted user to execute a command as
  the superuser or another user, as specified by the security policy»**, cuya política por defecto
  **«is configured via the file /etc/sudoers»**. `sudo -l` lista lo que el usuario puede hacer;
  `sudo -u usuario orden` ejecuta como otro usuario; `sudo -i` abre un intérprete de entrada del
  usuario destino.
- `su` es la vía antigua: **«su allows commands to be run with a substitute user and group ID»**; sin
  usuario, abre un intérprete como root (y pide la contraseña de root, que en Ubuntu no está
  habilitada). Que `su` pide la contraseña del usuario destino es oficio.

### Las órdenes

Ubuntu y las demás de la familia Debian **«encourage the use of the adduser package for account
management»**; las órdenes de bajo nivel (`useradd`, `usermod`, `userdel`, `groupadd`) son las de
todas las distribuciones.

| Tarea | Ubuntu (`adduser`) | Bajo nivel (paquete *shadow*) |
|---|---|---|
| Crear usuario | `sudo adduser nombre` (pregunta contraseña y datos) | `useradd -m -s /bin/bash nombre` y luego `passwd nombre` |
| Borrar usuario | `sudo deluser nombre` | `userdel nombre`; con `-r`, también su directorio |
| Crear o borrar grupo | `sudo addgroup grupo` / `sudo delgroup grupo` | `groupadd grupo` / `groupdel grupo` |
| Meter a un usuario en un grupo | `sudo adduser nombre grupo` | `usermod -aG grupo nombre` o `gpasswd -a nombre grupo` |
| Bloquear / desbloquear la contraseña | `sudo passwd -l nombre` / `sudo passwd -u nombre` | `usermod -L` / `usermod -U` |
| Caducidad de la contraseña | `sudo chage -l nombre` (consultar), `sudo chage nombre` (fijar) | — |

`groupdel` no se ha leído en su página de manual; su existencia como pareja de `groupadd` es oficio.

Lo que dicen las páginas de manual de cada opción de la tabla:

- `useradd`: **«-m, --create-home Create the user's home directory if it does not exist.»** Los
  ficheros de partida salen de **«/etc/skel/ Directory containing default files»**, y los valores por
  defecto de **«/etc/default/useradd»**. **«-s, --shell SHELL»** fija el intérprete; si no se da y no
  hay valor por defecto, el campo queda vacío. **«-g»** fija el grupo principal y **«-G»** los
  suplementarios, **«separated from the next by a comma, with no intervening whitespace»**. **«-u»**
  fija el UID, que **«must be unique, unless the -o option is used»**.
- `usermod`: **«-a, --append Add the user to the supplementary group(s). Use only with the -G
  option.»** Sin `-a`, `-G` sustituye la lista de grupos suplementarios por la indicada; por eso la
  forma segura es `usermod -aG`. Que sin `-a` se pierden los demás grupos es oficio deducido de la
  opción. **«-L, --lock Lock a user's password. This puts a '!' in front of the encrypted
  password»**; **«-U, --unlock»** la quita. **«-l, --login NEW_LOGIN»** cambia el nombre (y nada más:
  el directorio personal hay que renombrarlo aparte); **«-d»** cambia el directorio personal y, con
  **«-m, --move-home»**, mueve su contenido; **«-s»** cambia el intérprete; **«-e, --expiredate»**
  fija la fecha en que se deshabilita la cuenta.
- `userdel`: **«-r, --remove Files in the user's home directory will be removed along with the home
  directory itself and the user's mail spool.»**
- `passwd`: **«A regular user can only change the password for their own account, while the superuser
  can change the password for any account.»** **«-l, --lock»** la bloquea, **«-u, --unlock»** la
  devuelve a su valor anterior, **«-e, --expire»** la caduca en el acto (obliga a cambiarla en el
  próximo inicio) y **«-S, --status»** muestra el estado de la cuenta.
- `gpasswd`: **«-a, --add user Add the user to the named group.»**; **«-d, --delete user Remove the
  user from the named group.»**
- `groupadd`: crea el grupo; **«-g, --gid GID»** fija su número; **«-r, --system»** crea un grupo del
  sistema.

Dos avisos de la documentación de Ubuntu sobre bajas:

- **«Deleting an account does not remove their respective home folder.»** Hay que decidir qué hacer
  con él según la política de conservación.
- **«any user added later with the same UID/GID as the previous owner will now have access to this
  folder if you have not taken the necessary precautions»** (un usuario nuevo con el mismo UID
  heredaría la carpeta). La página propone pasarla a root y archivarla:
  `sudo chown -R root:root /home/username/` y moverla a `/home/archived_users/`.

### Directorios personales y contraseñas

- Al crear un usuario, **«the adduser utility creates a brand new home directory named
  /home/username. The default profile is modelled after the contents found in the directory of
  /etc/skel»**.
- Permisos: desde Ubuntu 21.10, **«Home directories are created with private permissions (0750 or
  drwxr-x---) by default. This ensures that only the user and members of their group can access the
  directory.»** Hasta 21.04 eran `0755`, legibles por todos. Se cambia con `sudo chmod 0750
  /home/username`, y para los futuros, con `DIR_MODE=0750` en `/etc/adduser.conf`. La página
  desaconseja `-R` en este caso: basta con cerrar el directorio padre.
- Longitud mínima: **«By default, Ubuntu requires a minimum password length of 6 characters, as well
  as some basic entropy checks. These values are controlled in the file
  /etc/pam.d/common-password»**; se sube con `minlen=8` en la línea de `pam_unix.so`.

## 4. Utilización del shell

### Qué es el shell

El shell es el intérprete de órdenes: lee lo que se escribe, lo expande y lanza los programas. En
Ubuntu y Debian el de los usuarios es Bash, el que figura en el último campo de `/etc/passwd` en los
ejemplos del epígrafe 3. Su página de manual lo define: **«Bash is a command language interpreter that
executes commands read from the standard input, from a string, or from a file. It is a
reimplementation and extension of the Bourne shell, the historical Unix command language
interpreter.»** (interpreta órdenes leídas del teclado, de una cadena o de un fichero; reimplementa y
amplía el shell de Bourne), e incorpora rasgos del Korn shell y del C shell. Aspira además a ser **«a
conformant implementation of the Shell and Utilities portion of the IEEE POSIX specification (IEEE
Standard 1003.1)»** (la parte de intérprete y utilidades de la norma POSIX).

### Moverse y mirar

Conviene aprender las órdenes por familias y no una a una:

| Familia | Órdenes |
|---|---|
| Dónde estoy y qué hay | `pwd` (ruta actual), `ls` (listar), `cd` (cambiar de directorio) |
| Qué se está ejecutando | `top` y `htop` (en tiempo real), `ps` (instantánea) |
| Permisos | `chmod` y `chown` (básicos), `getfacl` y `setfacl` (extendidos) |
| Servicios | `systemctl` (gestión de servicios), `journalctl` (su registro) |
| Parámetros del núcleo | `sysctl` |
| Buscar dentro de ficheros | `grep` |

Lo que dicen sus páginas de manual de las tres primeras:

- `pwd`: **«Print the full filename of the current working directory.»** `pwd` es *print working
  directory*: imprime el directorio de trabajo.
- `cd` es orden interna del intérprete: **«Change the current directory to dir. if dir is not
  supplied, the value of the HOME shell variable is used as dir.»** (sin argumento, vuelve al
  directorio personal).
- `ls`: **«List information about the FILEs (the current directory by default).»** Opciones de uso
  diario: **«-a, --all do not ignore entries starting with .»** (muestra los ocultos, que en Linux son
  los que empiezan por punto), **«-l use a long listing format»** y **«-h, --human-readable with -l
  and -s, print sizes like 1K 234M 2G etc.»**.

La virgulilla abrevia el directorio personal: si la palabra empieza por `~`, **«the tilde is replaced
with the value of the shell parameter HOME»**. `cd ~/informes` va a `informes` dentro del directorio
personal.

Otras órdenes de manejo de ficheros, con el resumen de su página de manual: `cp` **«copy files and
directories»**; `mv` **«move (rename) files»** (mover y renombrar es la misma orden); `rm` **«remove
files or directories»**; `mkdir` **«make directories»**; `cat` **«concatenate files and print on the
standard output»**; `less` **«display the contents of a file in a terminal»** (paginado); `head`
**«output the first part of files»** y `tail` **«output the last part of files»**, las diez primeras
o últimas líneas por defecto, o `-n NUM`; `tail -f` sigue el fichero mientras crece (**«output
appended data as the file grows»**), útil para ver un registro en vivo.

`find` **«search for files in a directory hierarchy»**, evaluando una expresión: `-name` (nombre con
patrón del shell), `-type` (tipo de fichero), `-user`, `-size`, `-mtime`. Dos ejemplos de su manual:
`find $HOME -mtime 0` (**«files in your home directory which have been modified in the last
twenty-four hours»**) y `find /tmp -name core -type f -print | xargs /bin/rm -f` (borra los ficheros
`core` bajo `/tmp`, con el aviso de que falla si los nombres llevan saltos de línea, comillas o espacios; para
eso está `-print0 | xargs -0`).

### La ayuda

`man` es **«an interface to the system reference manuals»**. Las páginas se ordenan en secciones; las
que importan aquí son la **«1 Executable programs or shell commands»**, la **«5 File formats and
conventions, e.g. /etc/passwd»** y la **«8 System administration commands (usually only for root)»**.
Por eso se escribe `passwd(1)` para la orden y `passwd(5)` para el fichero; `man 5 passwd` abre la
segunda. `man -k palabra` busca en las descripciones cortas (**«Approximately equivalent to
apropos»**). Casi todas las órdenes GNU aceptan además `--help`, que imprime la ayuda breve, como
consta en las páginas de manual de `pwd` y de `ls`.

### Comodines

Antes de lanzar una orden, el shell sustituye los patrones por los nombres de fichero que encajan
(**«Pattern Matching»**):

| Patrón | Literal de `bash(1)` | Ejemplo |
|---|---|---|
| `*` | **«Matches any string, including the null string.»** | `ls *.log` |
| `?` | **«Matches any single character.»** | `ls copia?.tar` (copia1.tar, copiaA.tar…) |
| `[...]` | **«Matches any one of the characters enclosed between the brackets.»** Con guion, un rango; con `!` o `^` delante, la negación | `ls informe[0-9].txt`, `ls [!a]*` |

Quien expande es el shell, no la orden; la página de `rsync(1)` lo recuerda: **«the expansion of
wildcards on the command-line (\*.c) into a list of files is handled by the shell before it runs
rsync and not by rsync itself (exactly the same as all other Posix-style programs)»**.

### Comillas y escape

**«Quoting is used to remove the special meaning of certain characters or words to the shell.»** Hay
**«four quoting mechanisms: the escape character, single quotes, double quotes, and dollar-single
quotes»**:

- Barra invertida: **«A non-quoted backslash […] is the escape character.»** **«It preserves the
  literal value of the next character that follows»**. Al final de una línea, la continúa en la
  siguiente.
- Comillas simples: **«preserves the literal value of each character within the quotes»**; dentro no
  se expande nada.
- Comillas dobles: **«preserves the literal value of all characters within the quotes, with the
  exception of»** el dólar, el acento grave y la barra invertida (y `!` con la expansión del
  historial); es decir, dentro de comillas dobles sí se sustituyen las variables.

```
nombre=Ana
echo '$nombre'      # imprime $nombre
echo "$nombre"      # imprime Ana
```

El ejemplo es propio; aplica las dos reglas citadas.

### Variables

**«A variable is a parameter denoted by a name.»** Se asigna con **«name=[value]»**, sin espacios
alrededor del igual (que no lleve espacios es oficio: con espacios, el shell tomaría `nombre` por una
orden), y se lee con `$nombre`. Una variable sólo se borra con `unset`. Para que la vean los programas
que se lancen después hay que exportarla: `export` marca los nombres **«for automatic export to the
environment of subsequently executed commands»**.

Variables y parámetros que hay que conocer:

| Nombre | Qué es |
|---|---|
| `HOME` | El directorio personal (lo fija el campo 6 de `/etc/passwd`) |
| `PATH` | **«The search path for commands. It is a colon-separated list of directories in which the shell looks for commands»** (por eso un script del directorio actual se lanza con `./script.sh`, porque el directorio actual no suele estar en `PATH`: esto último es oficio) |
| `$?` | **«Expands to the exit status of the most recently executed command.»** |
| `$$` | **«Expands to the process ID of the shell.»** |
| `$0` | **«Expands to the name of the shell or shell script.»** |
| `$1`, `$2`… | Parámetros posicionales: los argumentos con que se llamó al script |
| `$#` | **«Expands to the number of positional parameters in decimal.»** |

El estado de salida decide el éxito: **«a command which exits with a zero exit status has succeeded.
So while an exit status of zero indicates success, a non-zero exit status indicates failure.»**

*Sustitución de órdenes.* **«Command substitution allows the output of a command to replace the
command itself.»** Formas: `$(orden)` y, desaconsejada (**«deprecated»**), entre acentos graves.
`dia=$(date +%A)` guarda el día de la semana; así lo hace el script de copia de la documentación de
Ubuntu del epígrafe 10.

*Alias.* `alias` sin argumentos lista los definidos; `alias ll='ls -l'` crea uno.

### Redirección

**«Before a command is executed, its input and output may be redirected using a special notation
interpreted by the shell.»** Los descriptores son 0 (entrada estándar), 1 (salida estándar) y 2
(salida de error).

| Operador | Efecto (`bash(1)`) |
|---|---|
| `< fichero` | Entrada desde el fichero (descriptor 0) |
| `> fichero` | Salida al fichero: **«If the file does not exist it is created; if it does exist it is truncated to zero size.»** (se vacía) |
| `>> fichero` | Salida añadida al final: **«opens the file … for appending»** |
| `2> fichero` | La salida de error al fichero |
| `2>&1` | La salida de error, a donde vaya la estándar |
| `&> fichero` | Las dos salidas al fichero; **«semantically equivalent to >word 2>&1»** |
| `&>> fichero` | Las dos, añadiendo; equivale a **«>>word 2>&1»** |

El orden importa, y la página lo pone de ejemplo: `ls > dirlist 2>&1` **«directs both standard output
and standard error to the file dirlist»**, mientras que `ls 2>&1 > dirlist` **«directs only the
standard output to file dirlist, because the standard error was directed to the standard output
before the standard output was redirected to dirlist»**.

### Tuberías y listas

**«A pipeline is a sequence of one or more commands separated by one of the control operators | or
|&.»** **«The standard output of command1 is connected via a pipe to the standard input of
command2.»** Así se encadenan filtros: `dpkg -l | grep apache2` (epígrafe 9), `cat /etc/passwd | cut
-d : -f 1` (epígrafe 3).

Utilidades que se usan en tubería: `sort` ordena (`-n` numérico, `-r` al revés); `uniq` **«Filter
adjacent matching lines»** (sólo quita repetidas contiguas, por eso suele ir detrás de `sort`) y con
`-c` cuenta; `wc -l` cuenta líneas; `cut -d` fija el separador y `-f` los campos; `tr` **«translate or
delete characters»**; `tee` **«read from standard input and write to standard output and files»** (con
`-a`, añade); `xargs` **«build and execute command lines from standard input»**.

Las listas encadenan órdenes con **«;, &, &&, or ||»**:

| Operador | Qué hace |
|---|---|
| `a ; b` | **«Commands separated by a ; are executed sequentially»**: uno detrás de otro, falle o no |
| `a &` | **«the shell executes the command in the background in a subshell»**: en segundo plano, sin esperar |
| `a && b` | **«command2 is executed if, and only if, command1 returns an exit status of zero (success)»** |
| `a \|\| b` | **«command2 is executed if, and only if, command1 returns a non-zero exit status»** |

`sudo apt update && sudo apt upgrade` sólo actualiza si la lista de paquetes se descargó bien. El
ejemplo es propio.

### Scripts

Un script es un fichero de texto con órdenes. **«If the program is a file beginning with #!, the
remainder of the first line specifies an interpreter for the program.»** Por eso la primera línea es
`#!/bin/bash`. Para lanzarlo hay que darle permiso de ejecución, como en la documentación de Ubuntu:
`chmod u+x backup.sh` y luego `sudo ./backup.sh`.

Las estructuras de control, con su sintaxis de `bash(1)`:

```
if list; then list; [ elif list; then list; ] ... [ else list; ] fi
for name [ [ in word ... ] ; ] do list ; done
while list-1; do list-2; done
case word in [ [(] pattern [ | pattern ] ... ) list ;; ] ... esac
```

`if` ejecuta su lista y, **«If its exit status is zero, the then list is executed»**; `for` da a la
variable cada valor de la lista; `while` repite **«as long as the last command in the list list-1
returns an exit status of zero»** (`until`, al revés); `case` compara una palabra con patrones.

Ejemplo propio, no ejecutado, que reúne lo anterior:

```
#!/bin/bash
# avisa si el disco raíz pasa del 90 %
uso=$(df --output=pcent / | tail -n 1 | tr -d ' %')
if [ "$uso" -gt 90 ]; then
    echo "Disco al ${uso} %" | tee -a /var/log/aviso-disco.log
fi
```

El script de copia de seguridad de la documentación de Ubuntu (epígrafe 10) usa la misma forma
`if [ $month -eq 0 ]; then … fi`. La opción `--output` de `df` **«use the output format defined by
FIELD_LIST»**, y `pcent` es una de sus columnas válidas; `df -h /` da la misma información para leerla
a ojo.

## 5. Arranques y paradas

### La secuencia de arranque

La página `bootup(7)` la describe por fases:

1. Firmware y gestor de arranque: **«Immediately after power-up, the system firmware will do minimal
   hardware initialization, and hand control over to a boot loader (e.g. systemd-boot(7) or GRUB[…])
   stored on a persistent storage device. This boot loader will then invoke an OS kernel from disk
   (or the network).»** En equipos con EFI, **«this firmware may also load the kernel directly»**.
2. El núcleo y el disco inicial en memoria: el núcleo monta un sistema de ficheros en memoria para
   encontrar la raíz; **«Nowadays this is implemented as an "initramfs" — a compressed CPIO archive
   that the kernel extracts into a tmpfs.»** El nombre antiguo, *initrd*, se sigue usando para ambas
   cosas.
3. El gestor del sistema: **«After the root file system is found and mounted, the initrd hands over
   control to the host's system manager (such as systemd(1)) stored in the root file system, which
   is then responsible for probing all remaining hardware, mounting all necessary file systems and
   spawning all configured services.»** (detecta el resto del soporte físico, monta los sistemas de
   ficheros y lanza los servicios).

Y la parada, en orden inverso: **«On shutdown, the system manager stops all services, unmounts all
non-busy file systems […]. As a last step, the system is powered down.»**

### systemd y las unidades

**«systemd is a system and service manager for Linux operating systems. When run as first process on
boot (as PID 1), it acts as init system that brings up and maintains userspace services.»** (es el
primer proceso, con PID 1, y levanta y mantiene los servicios). Está instalado **«as the /sbin/init
symlink»**.

systemd gestiona unidades de varios tipos; los que más salen, en palabras de `systemd(1)`:

| Tipo | Para qué |
|---|---|
| `.service` | **«start and control daemons and the processes they consist of»** (los servicios o demonios) |
| `.socket` | Conexiones locales o de red, para activar servicios al recibir una |
| `.target` | **«useful to group units, or provide well-known synchronization points during boot-up»** (agrupan unidades: son los «estados» del sistema) |
| `.device` | Dispositivos del núcleo |
| `.mount` | **«control mount points in the file system»** |
| `.timer` | **«useful for triggering activation of other units based on timers»** (la alternativa de systemd a `cron`, epígrafe 6) |

### Los *targets* y los antiguos niveles de ejecución

Lo que en los sistemas SysV eran niveles de ejecución (*runlevels*) son hoy *targets*. La página
`runlevel(8)` lo deja claro: **«"Runlevels" are an obsolete way to start and stop groups of services
used in SysV init. systemd provides a compatibility layer that maps runlevels to targets»**, y
**«the mapping to runlevels is confusing and only approximate»** (porque sólo puede haber un nivel
activo y systemd activa varios *targets* a la vez). La tabla de equivalencias de esa misma página:

| Nivel | Target | Qué es (`systemd.special(7)`) |
|---|---|---|
| 0 | `poweroff.target` | Apagado |
| 1 | `rescue.target` | **«administer the system in single-user mode with all file systems mounted but with no services running, except for the most basic»** (modo monousuario de rescate) |
| 2, 3, 4 | `multi-user.target` | **«setting up a multi-user system (non-graphical)»** (multiusuario sin entorno gráfico: lo normal en un servidor) |
| 5 | `graphical.target` | **«setting up a graphical login screen. This pulls in multi-user.target.»** |
| 6 | `reboot.target` | Reinicio |

Más allá de la tabla está `emergency.target`, **«the most minimal version of starting the system in
order to acquire an interactive shell; the only processes running are usually just the system
manager (PID 1) and the shell process»**; se usa también **«when a file system check on a required
file system fails»** (cuando falla la comprobación de un sistema de ficheros necesario, el arranque
cae aquí).

El *target* de arranque es `default.target`: **«The default unit systemd starts at bootup. Usually,
this should be aliased (symlinked) to multi-user.target or graphical.target.»**

| Orden | Qué hace (`systemctl(1)`) |
|---|---|
| `systemctl get-default` | **«Return the default target to boot into.»** |
| `systemctl set-default multi-user.target` | **«Set the default target to boot into.»** (el servidor arrancará sin entorno gráfico) |
| `systemctl isolate rescue.target` | **«Start the unit specified on the command line and its dependencies and stop all others»**; cambia de *target* en caliente |
| `systemctl rescue` | **«Enter rescue mode. This is equivalent to systemctl isolate rescue.target.»** |
| `systemctl emergency` | **«Enter emergency mode.»** |

### Parar y reiniciar

| Orden | Qué hace |
|---|---|
| `systemctl poweroff` | **«Shut down and power-off the system.»** |
| `systemctl reboot` | **«Shut down and reboot the system.»** |
| `systemctl halt` | **«Shut down and halt the system.»** (detiene sin apagar la alimentación: lo de «sin apagar» es oficio) |
| `shutdown` | **«shutdown may be used to halt, power off, or reboot the machine.»** |

`shutdown` admite hora y mensaje:

- El primer argumento es la hora: **«"hh:mm" for hour/minutes specifying the time to execute the
  shutdown at, specified in 24h clock format»** o **«"+m" referring to the specified number of
  minutes m from now. "now" is an alias for "+0"»**. **«If no time argument is specified, "+1" is
  implied.»** (sin hora, al cabo de un minuto).
- Detrás puede ir un mensaje para los usuarios conectados (*wall message*).
- **«-P, --poweroff Power the machine off (the default).»**; **«-r, --reboot Reboot the machine.»**;
  **«-H, --halt Halt the machine.»**; **«-c Cancel a pending shutdown.»**
- **«5 minutes before the system goes down the /run/nologin file is created to ensure that further
  logins shall not be allowed»** (cinco minutos antes se impiden nuevas entradas).

Ejemplos: `sudo shutdown -r 23:30 "Reinicio por actualización"` reinicia a las 23.30 avisando;
`sudo shutdown -h now` apaga ya (`-h` es, según la página, **«The same as --poweroff»**);
`sudo shutdown -c` lo anula. Los ejemplos son propios, con las opciones citadas.

## 6. Herramientas básicas de administración

El enunciado no lista las herramientas. El tema agrupa aquí las de uso diario: servicios, registro,
procesos, tareas programadas, información del sistema y red. Esa selección es oficio; el detalle de
cada orden es de su página de manual. Las de discos, paquetes y copias tienen epígrafe propio.

Las tareas de administración, con su equivalente en Windows Server:

| Tarea | En Linux | En Windows Server |
|---|---|---|
| Usuarios y grupos | Ficheros de sistema y órdenes de alta y baja | Directorio Activo, o cuentas locales |
| Servicios | `systemctl` | La consola de servicios |
| Registro y auditoría | `journalctl` y los ficheros de registro | El visor de eventos |
| Programas instalados | El gestor de paquetes de la distribución | Instaladores y el gestor de paquetes del sistema |
| Tareas programadas | `cron` y temporizadores del sistema | El programador de tareas |

### Servicios: systemctl

**«systemctl may be used to introspect and control the state of the "systemd" system and service
manager.»** Las órdenes sobre una unidad (si no se pone extensión, `systemctl` añade una, **«".service" by
default»**):

| Orden | Qué hace (`systemctl(1)`) |
|---|---|
| `systemctl start ssh` | **«Start (activate) one or more units»** |
| `systemctl stop ssh` | **«Stop (deactivate) one or more units»** |
| `systemctl restart ssh` | **«Stop and then start one or more units»**; si no estaba en marcha, lo arranca |
| `systemctl reload ssh` | **«Asks all units listed on the command line to reload their configuration»**: la del servicio, no el fichero de unidad |
| `systemctl status ssh` | **«Show runtime status information about the whole system or about one or more units followed by most recent log data from the journal»** (estado y últimas líneas del registro) |
| `systemctl enable ssh` | Crea los enlaces para que arranque con el sistema; **«Note that this does not have the effect of also starting any of the units being enabled»** |
| `systemctl enable --now ssh` | Habilita y además arranca (**«--now When used with enable, disable, mask, or reenable, also start/stop […] the units»**) |
| `systemctl disable ssh` | Quita esos enlaces: no arrancará con el sistema |
| `systemctl mask ssh` | **«link these unit files to /dev/null, making it impossible to start them. This is a stronger version of disable»** |
| `systemctl is-active ssh` / `is-enabled ssh` | Comprueban si está en marcha o habilitado (código de salida 0 si sí) |
| `systemctl list-units` | **«List units that systemd currently has in memory»** |
| `systemctl --failed` | **«List units in failed state.»** |
| `systemctl daemon-reload` | Recarga la configuración de systemd tras editar ficheros de unidad (o `fstab`, epígrafe 7) |

La distinción que más se pregunta: `start` y `stop` actúan ahora; `enable` y `disable`, en el próximo
arranque. Lo dice la cita de `enable` del cuadro.

### Registro: journalctl, /var/log y dmesg

**«journalctl is used to print the log entries stored in the journal by systemd-journald.service»**.
Sin parámetros, **«it will show the contents of the journal accessible to the calling user, starting
with the oldest entry collected»**.

| Opción | Qué hace |
|---|---|
| `-u ssh` | **«Show messages for the specified systemd unit»** |
| `-f` | **«continuously print new entries as they are appended to the journal, until Ctrl-C is hit»** (seguir en vivo) |
| `-b` | **«Show messages from a specific boot»**; sin argumento, el arranque actual; `-b -1`, el anterior |
| `-p err` | Filtra por prioridad; las de `syslog` son **«"emerg" (0), "alert" (1), "crit" (2), "err" (3), "warning" (4), "notice" (5), "info" (6), "debug" (7)»**, y con un solo nivel **«all messages with this log level or a lower (hence more important) log level are shown»** |
| `-n 50` | Las últimas entradas (**«The default value is 10 if no argument is given»**) |
| `-r` | **«the newest entries are displayed first»** |
| `--since`, `--until` | Desde o hasta una fecha, **«of the format "2012-10-30 18:17:16"»** |
| `-k` | **«Show only kernel messages.»** |
| `--disk-usage` / `--vacuum-size=` | Cuánto ocupa el diario / borra los archivados más antiguos hasta bajar de un tamaño |

`journalctl -u ssh -b -p err` da los errores de SSH desde el último arranque; el ejemplo combina
opciones citadas.

Los ficheros de registro clásicos siguen en `/var/log` (**«Log files and directories»**, FHS) y se leen
con `less`, `tail -f` o `grep`. Los mensajes del núcleo, además de `journalctl -k`, con `dmesg`:
**«dmesg is used to examine or control the kernel ring buffer.»**

### Procesos

- `ps`: **«ps displays information about a selection of the active processes. If you want a
  repetitive update of the selection and the displayed information, use top instead.»** Es una
  instantánea. Para ver todos, **«To see every process on the system using standard syntax:»** `ps -e`
  o `ps -ef`; **«To see every process on the system using BSD syntax:»** `ps ax` o `ps axu` (sin
  guion). Las tres sintaxis conviven: **«Unix options, which may be grouped and must be preceded by a
  dash.»**; **«BSD options, which may be grouped and must not be used with a dash.»**; **«GNU long
  options, which are preceded by two dashes.»**
- `top`: **«The top program provides a dynamic real-time view of a running system. It can display
  system summary information as well as a list of processes or threads currently being managed by the
  Linux kernel.»** Dentro, `k` mata un proceso (**«Kill a task»**), `r` cambia su prioridad
  (**«Renice a task»**), `q` sale, y las teclas heredadas `M` y `P` ordenan por memoria y por CPU.
  `htop` es **«interactive process viewer»**, una alternativa más visual que no siempre viene
  instalada (esto último es oficio).
- `kill`: **«The command kill sends the specified signal to the specified processes or process
  groups. If no signal is specified, the TERM signal is sent.»** Y el consejo de su página: TERM
  **«should be used in preference to the KILL signal (number 9), since a process may install a handler
  for the TERM signal in order to perform clean-up steps before terminating in an orderly fashion»**;
  KILL **«cannot be caught»**. Números en x86 y ARM (`signal(7)`): SIGHUP 1, SIGINT 2 (**«Interrupt
  from keyboard»**; `bash(1)`: **«SIGINT (usually generated by ^C)»**), SIGKILL 9, SIGTERM 15. `kill 1234` pide terminar; `kill -9 1234`
  fuerza.
- `nice`: **«Niceness values range from -20 (most favorable to the process) to 19 (least favorable to
  the process).»** Sin `-n`, suma 10. `nice -n 15 tar czf …` lanza una copia con poca prioridad.
- En segundo plano: `orden &` (epígrafe 4). `nohup` **«run a command immune to hangups»**, para que
  siga al cerrar la sesión.

### Tareas programadas: cron

El demonio `cron` lanza órdenes a su hora; cada usuario tiene su tabla, que se gestiona con `crontab`
y no editando el fichero: **«Each user can have their own crontab, and though these are files in
/var/spool/, they are not intended to be edited directly.»** (cada usuario tiene la suya; están en
`/var/spool/`, pero no se editan a mano). La página leída es la de la variante *cronie*; los campos de
tiempo son los mismos en la de Debian y Ubuntu, como confirma la documentación de Ubuntu citada abajo.

| Orden | Qué hace (`crontab(1)`) |
|---|---|
| `crontab -e` | **«Edits the current crontab using the editor specified by the VISUAL or EDITOR environment variables.»** Al salir del editor, queda instalada |
| `crontab -l` | **«Displays the current crontab on standard output.»** |
| `crontab -r` | **«Removes the current crontab.»** |
| `crontab -u usuario …` | **«Specifies the name of the user whose crontab is to be modified.»** |
| `sudo crontab -e` | La de root, según la documentación de Ubuntu: **«Using sudo with the crontab -e command edits the root user's crontab.»** |

Cada línea tiene cinco campos de tiempo y la orden (`crontab(5)`):

| Campo | Valores |
|---|---|
| minuto | **«0-59»** |
| hora | **«0-23»** |
| día del mes | **«1-31»** |
| mes | **«1-12 (or names, see below)»** |
| día de la semana | **«0-7 (0 or 7 is Sunday, or use names)»** |

- **«A field may contain an asterisk (\*), which always stands for "first-last".»** (cualquiera).
- Rangos con guion (`8-11`), listas con comas (`1,15`) y pasos con barra: **«if specifying a job to be
  run every two hours, you can use "\*/2"»**.
- Si se restringen a la vez día del mes y día de la semana, basta con que coincida uno: **«"30 4 1,15
  \* 5" would cause a command to be run at 4:30 am on the 1st and 15th of each month, plus every
  Friday.»**
- Abreviaturas: **«@reboot : Run once after reboot.»**, `@daily` (**«"0 0 \* \* \*"»**), `@weekly`
  (**«"0 0 \* \* 0"»**), `@monthly`, `@yearly`, `@hourly`.

Ejemplos de la propia página:

```
# run five minutes after midnight, every day
5 0 * * *       $HOME/bin/daily.job >> $HOME/tmp/out 2>&1
# run at 2:15pm on the first of every month
15 14 1 * *     $HOME/bin/monthly
# run at 10 pm on weekdays
0 22 * * 1-5    mail -s "It's 10pm" joe%Joe,%%Where are your kids?%
```

Un aviso de fuente: la documentación de Ubuntu sobre copias pone la línea `0 0 * * * bash
/usr/local/bin/backup.sh` y dice que se ejecuta **«every day at 12:00 pm»** [sic]. Según los campos de
`crontab(5)`, minuto 0 y hora 0 es la medianoche (las 00.00), no las doce del mediodía. Manda la
definición de los campos.

La alternativa de systemd son las unidades `.timer` (epígrafe 5).

### Información del sistema y de la red

| Orden | Qué da (resumen de su página de manual) |
|---|---|
| `uname -a` | **«print system information»**: núcleo, nombre del equipo, versión |
| `hostnamectl` | **«Control the system hostname»** |
| `uptime` | **«The current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes.»** |
| `free -h` | **«the total amount of free and used physical and swap memory in the system, as well as the buffers and caches used by the kernel»** |
| `df -h`, `du -sh` | Espacio de los sistemas de ficheros y de un directorio (epígrafe 8) |
| `who`, `w`, `last` | **«show who is logged on»**; **«Show who is logged on and what they are doing.»**; **«list logins on the system»** |
| `id`, `whoami` | Identidad y grupos; **«print effective user name»** |
| `sysctl` | **«configure kernel parameters at runtime»** |
| `ip` | **«show / manipulate routing, network devices, interfaces and tunnels»** (`ip a` para las direcciones; la abreviatura es oficio) |
| `ss` | **«another utility to investigate sockets»**; **«It allows showing information similar to netstat.»** |

### Equivalencias con Windows

Lo mínimo que conviene llevar visto, con su equivalencia:

| Tarea | En Windows | En Ubuntu |
|---|---|---|
| Instalar una aplicación | Paquete `.msi` o `.exe` | Gestor de paquetes de la distribución |
| Elevar privilegios | Control de cuentas de usuario | `sudo` |
| Ver conexiones | `netstat` | `ss` |
| Gestionar servicios | Consola de servicios | `systemctl` |
| Cifrar el disco | BitLocker | LUKS |

La columna de Ubuntu se apoya en lo citado en este tema: `sudo` (epígrafe 3), `ss` (arriba),
`systemctl` (arriba), el gestor de paquetes (epígrafe 9) y LUKS (epígrafe 8). La de Windows está
desarrollada en el tema 6.

## 7. Sistemas de ficheros

### Qué tipos hay

Un sistema de ficheros es la forma de organizar los datos dentro de una partición o un volumen; el
mismo disco puede llevar varios. La página de `fstab(5)` enumera los que admite Linux: **«Linux
supports many filesystem types: ext4, xfs, btrfs, f2fs, vfat, ntfs, hfsplus, tmpfs, sysfs, proc,
iso9660, udf, squashfs, nfs, cifs, and many more.»**

Agrupados por uso (la agrupación es oficio): de disco local nativos de Linux, `ext4`, `xfs` y
`btrfs`; para intercambiar con Windows o en memorias USB, `vfat` y `ntfs`; de ópticos, `iso9660` y
`udf`; de red, `nfs` (el de Unix) y `cifs` (el de los recursos compartidos de Windows); virtuales, sin
disco detrás, `proc`, `sysfs` y `tmpfs`. A ellos se suma el área de intercambio (*swap*), que no es un
sistema de ficheros sino espacio de paginación (`swap` en `fstab`).

`ext4` es el tipo que crea `mke2fs`, la herramienta de la familia ext2/ext3/ext4 (abajo). Qué tipo
propone por defecto el instalador de Ubuntu no se ha comprobado en fuente.

### Crear un sistema de ficheros: mkfs

- `mkfs`: **«mkfs is used to build a Linux filesystem on a device, usually a hard disk partition.»**
  Pero **«This mkfs frontend is deprecated in favour of filesystem specific mkfs.<type> utils.»** (se
  prefieren las órdenes específicas: `mkfs.ext4`, `mkfs.xfs`, `mkfs.vfat`…).
- `mke2fs`: **«mke2fs is used to create an ext2, ext3, or ext4 file system, usually in a disk partition
  (or file) named by device.»** **«If mke2fs is run as mkfs.XXX (i.e., mkfs.ext2, mkfs.ext3, or
  mkfs.ext4) the option -t XXX is implied»**. `-L` pone una etiqueta: **«The maximum length of the
  volume label is 16 bytes.»**

```
sudo mkfs.ext4 -L datos /dev/sdb1
```

Formatear destruye lo que hubiera en la partición. Esta advertencia es oficio; la de pérdida de datos
al particionar está en el epígrafe 1.

### Montar y desmontar

La forma estándar de `mount` es **«mount -t type device dir»**: **«This tells the kernel to attach the
filesystem found on device (which is of type type) at the directory dir. The option -t type is
optional.»** Y un efecto que se pregunta: **«The previous contents (if any) and owner and mode of dir
become invisible, and as long as this filesystem remains mounted, the pathname dir refers to the root
of the filesystem on device.»** (lo que hubiera en el directorio queda oculto mientras dure el
montaje). **«The root permissions are necessary to mount a filesystem by default.»**

```
sudo mount /dev/sdb1 /mnt/datos      # monta (el tipo se detecta)
sudo mount -o ro /dev/sdb1 /mnt/datos   # sólo lectura
sudo umount /mnt/datos               # desmonta
mount -a                             # monta todo lo de fstab
```

- **«-a, --all Mount all filesystems (of the given types) mentioned in fstab (except for those whose
  line contains the noauto keyword).»**
- **«-o, --options opts Use the specified mount options. The opts argument is a comma-separated
  list.»** Algunas: **«ro»** (**«Mount the filesystem read-only.»**), **«rw»**, **«noexec»** (**«Do
  not permit direct execution of any binaries on the mounted filesystem.»**), **«noauto»** (**«Can
  only be mounted explicitly»**), **«user»** (**«Allow an ordinary user to mount the filesystem.»**) y
  **«defaults»**: **«Use the default options: rw, suid, dev, exec, auto, nouser, and async.»**
- `umount`: **«The umount command detaches the mentioned filesystem(s) from the file hierarchy.»** No
  siempre se puede: **«a filesystem cannot be unmounted when it is 'busy' - for example, when there
  are open files on it, or when some process has its working directory there»** (si hay ficheros
  abiertos o alguien está dentro, da «ocupado»).

### /etc/fstab

**«The file fstab contains descriptive information about the filesystems the system can mount. fstab
is only read by programs, and not written; it is the duty of the system administrator to properly
create and maintain this file.»** Cada línea, seis campos. Ejemplo de la página:

```
LABEL=t-home2   /home      ext4    defaults,auto_da_alloc      0  2
```

| N.º | Campo | Qué es (`fstab(5)`) |
|---|---|---|
| 1 | `fs_spec` | **«the block special device, remote filesystem or filesystem image for loop device to be mounted or swap file or swap device to be enabled»** (qué se monta) |
| 2 | `fs_file` | El punto de montaje (dónde) |
| 3 | `fs_vfstype` | El tipo; **«An entry swap denotes a file or partition to be used for swapping»** |
| 4 | `fs_mntops` | Las opciones, separadas por comas; **«The usual convention is to use at least "defaults" keyword there.»** |
| 5 | `fs_freq` | Para `dump`; **«Defaults to zero (don't dump) if not present.»** |
| 6 | `fs_passno` | El orden de comprobación al arrancar: **«The root filesystem should be specified with a fs_passno of 1. Other filesystems should have a fs_passno of 2.»** Con 0, no se comprueba |

*Por qué UUID o etiqueta y no `/dev/sdb1`.* **«LABEL=<label> or UUID=<uuid> may be given instead of
a device name. This is the recommended method, as device names are often a coincidence of hardware
detection order, and can change when other disks are added or removed.»** (el nombre `/dev/sdX`
depende del orden en que se detectan los discos y puede cambiar si se añade uno; el UUID no). El UUID
de cada sistema de ficheros lo dan `blkid` o `lsblk -f` (epígrafe 8).

Tras editar `fstab`: **«on systemd-based systems, it's recommended to use systemctl daemon-reload after
fstab modification»**. Probar con `sudo mount -a` antes de reiniciar evita descubrir el error en el
arranque (con el riesgo de caer en `emergency.target`, epígrafe 5); este consejo es oficio.

### Comprobar y reparar: fsck

**«fsck is used to check and optionally repair one or more Linux filesystems.»** Admite nombre de
dispositivo, punto de montaje, etiqueta o UUID. `fsck -A` recorre `fstab` y **«try to check all
filesystems in one run»**. La regla de oro está en la página de `e2fsck`: **«Note that in general it is
not safe to run e2fsck on mounted file systems.»** Se desmonta antes (o se trabaja desde el modo de
rescate: esto último es oficio).

### Intercambio (swap)

- `mkswap` **«sets up a Linux swap area on a device or in a file»**. La página añade que muchos
  instaladores tratan como intercambio las particiones **«of hex type 82 (LINUX_SWAP)»**.
- `swapon` **«is used to specify devices on which paging and swapping are to take place»**; `swapon
  -a` activa todo lo marcado como `swap` en `fstab` (salvo `noauto`), y `swapoff` lo desactiva.
- `swapon --show` muestra las áreas activas; `free -h` (epígrafe 6) muestra cuánta se usa.

## 8. Gestión de discos

### Discos y particiones como ficheros de /dev

Cada disco y cada partición es un fichero especial de bloques en `/dev` (epígrafe 2). Los ejemplos
de las páginas de manual usan nombres del tipo `/dev/sdb` para un disco y `/dev/sdb7` o `/dev/sdb2`
para sus particiones (las páginas de `mkfs` y `fsck` citan también los antiguos `/dev/hda1` y
`/dev/hdc1`). Que la letra cuenta el disco y el número la partición es oficio, deducido de esos
ejemplos; los nombres de otros tipos de dispositivo (NVMe, tarjetas) no se han comprobado en fuente.

**«Block devices can be divided into one or more logical disks called partitions. This division is
recorded in the partition table, usually found in sector 0 of the disk.»** (la división en
particiones se anota en la tabla de particiones, normalmente en el sector 0). Las dos tablas
corrientes son MBR y GPT; que la tabla que `parted` llama *MS-DOS* es la MBR es oficio.

### Ver qué hay

| Orden | Qué da |
|---|---|
| `lsblk` | **«lsblk lists information about all available or the specified block devices.»** Por defecto, **«in a tree-like format»** (el disco y, colgando, sus particiones y volúmenes) |
| `lsblk -f` | Sistemas de ficheros: **«equivalent to -o NAME,FSTYPE,FSVER,LABEL,UUID,FSAVAIL,FSUSE%,MOUNTPOINTS»** |
| `blkid` | Tipo, etiqueta y UUID de cada dispositivo; su propia página recomienda `lsblk` para consultas, porque **«it does not require root permissions to get actual information»** |
| `sudo fdisk -l` | **«List the partition tables for the specified devices and then exit.»** |
| `df -h` | **«df displays the amount of space available on the file system containing each file name argument. If no file name is given, the space available on all currently mounted file systems is shown.»**; `-h`, **«print sizes in powers of 1024 (e.g., 1023M)»**; `-T`, el tipo |
| `du -sh /var/log` | **«Summarize device usage of the set of FILEs, recursively for directories.»**; `-s`, **«display only a total for each argument»** |

`df` mira el sistema de ficheros entero (cuánto queda libre); `du`, lo que ocupa un directorio
concreto (quién se lo come). Es la pareja de diagnóstico cuando se llena un disco; la comparación es
oficio.

### Particionar: fdisk y parted

- `fdisk`: **«fdisk is a dialog-driven program for creation and manipulation of partition tables. It
  understands GPT, MBR, Sun, SGI and BSD partition tables.»** Es interactivo: se abre con `sudo fdisk
  /dev/sdb` y los cambios se preparan en memoria y se escriben al final. Su página aconseja: **«It is
  always a good idea to follow fdisk's defaults»** (sectores de inicio y fin y tamaños quedan así
  alineados con el dispositivo).
- `parted`: **«parted is a program to manipulate disk partitions. It supports multiple partition table
  formats, including MS-DOS and GPT. It is useful for creating space for new operating systems,
  reorganising disk usage, and copying data to new hard disks.»**

Que `fdisk` no escribe hasta que se le ordena se apoya en su página, que habla de modificar la tabla
en memoria **«before you write it to the device»**; las letras de sus órdenes interactivas no se han
leído en fuente y el tema no las da.

El ciclo completo para añadir un disco de datos, con las órdenes de este epígrafe y del anterior
(la secuencia es oficio):

```
lsblk                                  # localizar el disco nuevo (p. ej. /dev/sdb)
sudo fdisk /dev/sdb                    # crear la partición /dev/sdb1
sudo mkfs.ext4 -L datos /dev/sdb1      # darle sistema de ficheros
sudo mkdir /srv/datos                  # crear el punto de montaje
sudo blkid /dev/sdb1                   # anotar su UUID
# añadir a /etc/fstab:  UUID=…  /srv/datos  ext4  defaults  0  2
sudo systemctl daemon-reload && sudo mount -a
df -h /srv/datos                       # comprobar
```

### LVM: volúmenes lógicos

**«The Logical Volume Manager (LVM) provides tools to create virtual block devices from physical
devices. Virtual devices may be easier to manage than physical devices, and can have capabilities
beyond what the physical devices provide themselves.»** Sus tres piezas, en palabras de `lvm(8)`:

| Pieza | Qué es |
|---|---|
| PV (volumen físico) | Cada disco o partición entregado a LVM: **«each called a Physical Volume (PV)»** |
| VG (grupo de volúmenes) | **«A Volume Group (VG) is a collection of one or more physical devices»** |
| LV (volumen lógico) | **«A Logical Volume (LV) is a virtual block device that can be used by the system or applications.»** Es lo que se formatea y se monta |

Las órdenes, con ejemplos de sus páginas:

```
pvcreate /dev/sdc4 /dev/sde              # inicializa una partición y un disco como PV
vgcreate myvg /dev/sdk1 /dev/sdl1        # crea un VG con dos PV
lvcreate --type raid1 -m1 -L 500m -n mylv vg00   # crea un LV en espejo de 500 MiB
lvextend -L +54 vg01/lvol10 /dev/sdk3    # amplía un LV en 54 MiB
```

- `pvcreate` **«initializes a Physical Volume (PV) on a device so the device is recognized as
  belonging to LVM»**, sobre **«a whole device or partition»**.
- `vgcreate` **«creates a new VG on block devices»**; si no eran PV, los inicializa.
- `lvcreate` **«creates a new LV in a VG»**; si no hay espacio, **«the VG can be extended with other
  PVs (vgextend(8))»**.
- `lvextend` **«extends the size of an LV»**; con **«-r|--resizefs Resize underlying filesystem
  together with the LV»** amplía a la vez el sistema de ficheros.

La ventaja que justifica LVM, según la descripción citada, es la gestión: un volumen puede crecer
añadiendo discos al grupo sin reparticionar. Esta lectura de la ventaja es oficio.

### RAID por software: mdadm

`mdadm` gestiona **«MD devices aka Linux Software RAID»**. **«RAID devices are virtual devices created
from two or more real block devices. This allows multiple devices (typically disk drives or
partitions thereof) to be combined into a single device to hold (for example) a single filesystem.
Some RAID levels include redundancy and so can survive some degree of device failure.»**

Niveles: **«Currently, Linux supports LINEAR md devices, RAID0 (striping), RAID1 (mirroring), RAID4,
RAID5, RAID6, RAID10, MULTIPATH, FAULTY, and CONTAINER.»** (RAID0 reparte en bandas y no tiene
redundancia; RAID1 es espejo; la ausencia de redundancia en RAID0 se deduce de la cita general, que
sólo atribuye redundancia a «algunos» niveles, y es oficio). Ejemplo de la página:

```
mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/hd[ac]1
```

**«Create /dev/md0 as a RAID1 array consisting of /dev/hda1 and /dev/hdc1.»** El estado de los
conjuntos se ve en `/proc/mdstat`, que la página cita como fuente de información de `mdadm`.

### Cifrado de disco: LUKS

**«Cryptsetup is a utility for configuring and managing full-disk encryption on storage devices. It
can encrypt block devices (such as hard drives or partitions) and containers (disk images stored as
files).»** Al desbloquear un volumen, **«cryptsetup creates a new device mapping that applications can
access like any regular storage device»**, y el cifrado lo hace el núcleo (*dm-crypt*). Trabaja con
volúmenes *plain* y LUKS; de LUKS hay dos versiones y **«The default format is LUKS2.»**

```
cryptsetup luksFormat /dev/sdb1          # inicializa LUKS y fija la frase de paso
cryptsetup open --type luks /dev/sdb1 seguro   # lo abre como /dev/mapper/seguro
```

`luksFormat` **«Initializes a LUKS partition and sets the initial passphrase»**. Que el volumen abierto
aparece en `/dev/mapper/<nombre>` es oficio; la página sólo dice que crea un *mapping* con ese nombre.

## 9. Administración del software

### Paquetes y repositorios

En Linux el software se instala en paquetes desde repositorios, no con instaladores sueltos. La
página de `rpm(8)` da una buena definición de paquete: **«A package consists of an archive of files
and meta-data used to install and erase the archive files. The meta-data includes helper scripts,
file attributes, and descriptive information about the package.»** (un archivo de ficheros más los
metadatos para instalarlos y borrarlos: guiones auxiliares, atributos y descripción). Hay dos
familias: `.deb` (Debian, Ubuntu) y `.rpm` (Red Hat, Fedora y derivadas).

Cada familia tiene dos niveles de herramienta: una de bajo nivel, que instala un paquete ya
descargado (`dpkg`, `rpm`), y una de alto nivel, que descarga de los repositorios y resuelve
dependencias (`apt`, `dnf`). La documentación de Ubuntu lo dice de `dpkg`: **«It can install, remove,
and build packages, but unlike other package management systems, it cannot automatically download
and install packages – or their dependencies.»**; y **«APT and Aptitude are newer, and layer
additional features on top of dpkg.»**

### APT (Debian y Ubuntu)

**«The recommended way to install Debian packages ("deb" files) is using the Advanced Packaging Tool
(APT), which can be used on the command line using the apt utility.»**

*Los repositorios.* **«The APT package index is a database of available packages from the
repositories defined in the /etc/apt/sources.list.d directory. Ubuntu repositories are defined in the
/etc/apt/sources.list.d/ubuntu.sources file.»** En versiones anteriores a 24.04 LTS, que no usan por
defecto el formato *deb822*, el fichero era `/etc/apt/sources.list`. Además de los repositorios
oficiales están Universe y Multiverse, mantenidos por la comunidad; la documentación avisa de que
**«packages in Universe and Multiverse are not officially supported and do not receive security
patches, except through Ubuntu Pro's Expanded Security Maintenance»**.

Las órdenes de `apt` (página de manual de Ubuntu 26.04):

| Orden | Qué hace |
|---|---|
| `sudo apt update` | **«update is used to download package information from all configured sources»** (refresca el índice; no instala nada) |
| `sudo apt upgrade` | **«install available upgrades of all packages currently installed»**; **«New packages will be installed if required to satisfy dependencies, but existing packages will never be removed.»** |
| `sudo apt full-upgrade` | **«performs the function of upgrade but will remove currently installed packages if this is needed to upgrade the system as a whole»** |
| `sudo apt install nmap` | Instala (se pueden poner varios separados por espacios) |
| `sudo apt remove nmap` | Desinstala, pero **«leaves usually small (modified) user configuration files behind, in case the remove was an accident»** |
| `sudo apt purge nmap` | Quita también esos restos de configuración; equivale a `apt remove --purge`, que **«will remove the package configuration files as well»** |
| `sudo apt autoremove` | Quita **«packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed»** |
| `apt search término` | **«search for the given regex(7) term(s) in the list of available packages»** |
| `apt show paquete` | **«Show information about the given package(s) including its dependencies, installation and download size»** |
| `apt list --installed` | Lista los instalados (`--upgradeable`, los actualizables) |

El orden habitual es `update` y después `upgrade`, como en la documentación de Ubuntu: **«To upgrade
your system, first update your package index and then perform the upgrade»**.

Dos matices preguntables:

- `apt` frente a `apt-get`: **«While apt is a command-line tool, it is intended to be used
  interactively, and not to be called from non-interactive scripts. The apt-get command should be used
  in scripts»**. Para lo básico, **«the syntax of the two tools is identical»**.
- Actualizaciones automáticas: **«the default for Ubuntu Server is to automatically apply security
  updates»**.

`aptitude` es otra interfaz, de menús en modo texto, sobre el mismo sistema: **«Launching Aptitude with
no command-line options will give you a menu-driven, text-based frontend to the APT system.»**

### dpkg

| Orden | Qué hace |
|---|---|
| `dpkg -l` | **«To list all packages in the system's package database (both installed and uninstalled)»**; se filtra con `dpkg -l \| grep apache2` |
| `dpkg -L ufw` | Lista los ficheros que instaló el paquete (**«List files installed to your system from package-name.»**) |
| `dpkg -S /etc/host.conf` | Dice de qué paquete viene un fichero (respuesta del ejemplo: `base-files`) |
| `sudo dpkg -i zip_3.0-4_amd64.deb` | Instala un `.deb` local |
| `sudo dpkg -r zip` | Desinstala; **«This removes everything except conffiles»** |
| `sudo dpkg -P zip` | Purga: **«This removes everything, including conffiles»** |

La documentación de Ubuntu desaconseja desinstalar con `dpkg`: **«Uninstalling packages using dpkg, is
NOT recommended in most cases. It is better to use a package manager that handles dependencies to
ensure that the system is left in a consistent state.»** (los paquetes que dependían del borrado
quedan instalados y pueden dejar de funcionar).

### La familia RPM: rpm y dnf

- `rpm`: **«rpm is a powerful Package Manager, which can be used to build, install, query, verify,
  update, and erase individual software packages.»** Opciones: **«-i, --install»** (instalar, uso
  especial), **«-U, --upgrade Install or upgrade package(s) to a newer version»** (lo normal),
  **«-e, --erase Erase installed packages.»** y **«-q, --query»**.
- `dnf`: la página leída lo presenta así: **«DNF is the next upcoming major version of YUM, a package
  manager for RPM-based Linux distributions.»** (frase antigua de su propia documentación). Órdenes:
  `dnf install` (**«Makes sure that the given packages and their dependencies are installed on the
  system.»**), `dnf remove` (**«Removes the specified packages from the system along with any packages
  depending on the packages being removed.»**), `dnf upgrade` (**«Updates each package to the latest
  version that is both available and resolvable.»**), `dnf search`, `dnf info` y `dnf list
  --installed`.

| Tarea | Debian/Ubuntu | Red Hat/Fedora |
|---|---|---|
| Refrescar índice | `apt update` | `dnf makecache` (o `--refresh`, **«Set metadata as expired before running the command.»**) |
| Instalar del repositorio | `apt install` | `dnf install` |
| Actualizar todo | `apt upgrade` | `dnf upgrade` |
| Desinstalar | `apt remove` / `purge` | `dnf remove` |
| Instalar un fichero local | `dpkg -i fichero.deb` | `rpm -i` o `rpm -U fichero.rpm` |
| Listar instalados | `dpkg -l`, `apt list --installed` | `rpm -qa`, `dnf list --installed` |

`rpm -qa`: **«List all installed packages, using the default formatting.»** *Snap*, *Flatpak* y los paquetes universales no se han
estudiado en fuente; el instalador de Ubuntu ofrece *snaps* en una de sus pantallas (epígrafe 1).

## 10. Salvaguarda y restauración

### El plan

La documentación de Ubuntu Server parte de esto: **«It's important to back up your Ubuntu installation
so you can recover quickly if you experience data loss.»** Y pide un plan con cuatro respuestas:

1. **«What should be backed up»** (qué se copia).
2. **«How often to back it up»** (cada cuánto).
3. **«Where backups should be stored»** (dónde se guarda).
4. **«How to restore your backups»** (cómo se recupera).

Sobre el dónde: **«It is good practice to store important backup media off-site in case of a
disaster.»** Si no se pueden sacar los soportes físicamente, **«backups can be copied over a WAN link
to a server in another location»**. Y sobre la redundancia: **«You can create redundancy by using
multiple back-up methods. Redundant data is useful if the primary back-up fails.»**

Dos vías, según la misma página: herramientas dedicadas o guiones de shell.

| Herramienta | Qué copia | Cómo |
|---|---|---|
| Bacula | **«Multiple systems over a network»** | **«Incremental backups»**; para empresas o necesidades complejas |
| rsnapshot | **«Single system»** | **«Periodic "snapshots" of files locally or remotely with SSH»**; para usuarios o organizaciones pequeñas |

La copia incremental: **«Incremental backups only store changes made since the last backup which can
significantly decrease storage space needs and backup time.»** (sólo guarda lo cambiado desde la
última; ahorra espacio y tiempo). Para la configuración, la página propone `etckeeper`, que **«stores
the contents of /etc in a Version Control System (VCS) repository»** (guarda `/etc` en un control de
versiones).

### tar: archivar y restaurar

`tar` es la herramienta básica: **«You can use tar to store files in an archive, to extract them from
an archive, and to do other types of archive manipulation.»** La documentación de Ubuntu explica que
**«The tar utility creates one archive file out of many files or directories. tar can also filter the
files through compression utilities, thus reducing the size of the archive file.»**

| Opción | Qué hace (`tar(1)` y manual GNU) |
|---|---|
| `-c`, `--create` | **«Create a new archive.»** Los directorios, **«recursively»** |
| `-x`, `--extract` | **«Extract files from an archive.»** |
| `-t`, `--list` | **«List the contents of an archive.»** |
| `-v`, `--verbose` | **«Verbosely list files processed.»** |
| `-f ARCHIVO` | **«Use archive file or device ARCHIVE.»** (va la última del grupo, porque lleva argumento: esto es oficio) |
| `-z` / `-j` / `-J` | Comprime con gzip / bzip2 / xz |
| `-C DIR` | **«Change to DIR before performing any operations.»** (extraer en otro sitio) |
| `-p` | **«Set permissions of extracted files to those recorded in the archive (default for superuser).»** |
| `-g FICHERO` | Copias incrementales (abajo) |

Dos reglas del manual GNU que se preguntan:

- **«tar will make all file names relative (by removing leading slashes when archiving or restoring
  files), unless you specify otherwise (using the --absolute-names option).»** (guarda `etc/hosts`, no
  `/etc/hosts`; al restaurar, lo deja relativo al directorio en que se esté).
- Al leer, no hace falta decir la compresión: **«Reading compressed archive is even simpler: you don't
  need to specify any additional options as GNU tar recognizes its format automatically.»**

El ciclo completo, con los ejemplos de la documentación de Ubuntu:

```
tar czf $dest/$archive_file $backup_files          # crear, comprimido con gzip
tar -tzvf /mnt/backup/host-Monday.tgz              # listar el contenido
tar -xzvf /mnt/backup/host-Monday.tgz -C /tmp etc/hosts   # restaurar un fichero en /tmp
cd / && sudo tar -xzvf /mnt/backup/host-Monday.tgz        # restaurar todo
```

- En la creación, **«c: Creates an archive. z: Filter the archive through the gzip utility, compressing
  the archive. f: Output to an archive file. Otherwise the tar output will be sent to STDOUT.»**
- La restauración parcial **«will extract the /etc/hosts file to /tmp/etc/hosts. tar recreates the
  directory structure that it contains. Also, notice the leading "/" is left off the path of the file
  to restore.»**
- La total, desde `/`, **«will overwrite the files currently on the file system»** (sobrescribe lo
  que haya).

*Probar la copia.* **«Once an archive has been created, it is important to test the archive. The
archive can be tested by listing the files it contains, but the best test is to restore a file from
the archive.»** (listarla está bien; restaurar un fichero es la prueba de verdad).

### El script de copia de la documentación de Ubuntu

La documentación propone un script que copia varios directorios a un recurso NFS montado, con un
fichero por día de la semana (siete días de historia). Su núcleo:

```
#!/bin/bash
backup_files="/home /var/spool/mail /etc /root /boot /opt"
dest="/mnt/backup"
day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"
tar czf $dest/$archive_file $backup_files
ls -lh $dest
```

Se guarda como `backup.sh`, se hace ejecutable (`chmod u+x backup.sh`), se prueba (`sudo ./backup.sh`)
y se programa con `sudo crontab -e` (epígrafe 6). La página añade una variante con rotación
**«grandparent-parent-child»** (mensual, semanal, diaria): diaria de domingo a viernes, semanal el
sábado (cuatro al mes) y mensual el día 1, alternando dos según el mes sea par o impar. Advierte de que
`ls -lh` sirve para ver el tamaño, pero **«This check should not replace testing the archive file.»**

### Copias incrementales con tar

**«GNU tar currently offers two options for handling incremental backups:
--listed-incremental=snapshot-file (-g snapshot-file) and --incremental (-G).»** Con `-g`, un fichero de instantánea
recuerda el estado: **«The purpose of this file is to help determine which files have been changed,
added or deleted since the last backup, so that the next incremental backup will contain only
modified files.»** La primera vez, si el fichero no existe, se crea y la copia es completa (**«a level
0 backup»**); las siguientes con el mismo fichero sólo guardan lo cambiado. Ejemplo del manual:

```
tar --create --file=archive.1.tar --listed-incremental=/var/log/usr.snar /usr
```

### rsync: copiar y sincronizar

**«Rsync is a fast and extraordinarily versatile file copying tool. It can copy locally, to/from
another host over any remote shell, or to/from a remote rsync daemon.»** **«It is famous for its
delta-transfer algorithm, which reduces the amount of data sent over the network by sending only the
differences between the source files and the existing files in the destination. Rsync is widely used
for backups and mirroring»**.

- `-a`, modo archivo: **«This is equivalent to -rlptgoD. It is a quick way of saying you want
  recursion and want to preserve almost everything.»** No incluye ACL (`-A`), atributos extendidos
  (`-X`) ni enlaces duros (`-H`).
- `rsync -avz foo:src/bar /data/tmp` copia del equipo `foo` en modo archivo, con compresión: **«symbolic
  links, devices, attributes, permissions, ownerships, etc. are preserved in the transfer»**.
- La barra final del origen cambia el resultado: **«A trailing slash on the source changes this
  behavior to avoid creating an additional directory level at the destination. You can think of a
  trailing / on a source as meaning "copy the contents of this directory" as opposed to "copy the
  directory by name"»**. `rsync -av /src/foo /dest` y `rsync -av /src/foo/ /dest/foo` hacen lo mismo.
- `--delete` **«tells rsync to delete extraneous files from the receiving side (ones that aren't on the
  sending side)»**: deja el destino como espejo exacto. Conviene probar antes con `-n` (**«perform a
  trial run with no changes made»**); el consejo es oficio.

### dd: copia en bruto

`dd` **«Copy a file, converting and formatting according to the operands»**: `if=` (**«read from FILE
instead of standard input»**), `of=` (**«write to FILE instead of standard output»**), `bs=` (tamaño de
bloque, **«default: 512»**), `count=` (**«copy only N input blocks»**) y `status=` (nivel de
información). Como `/dev/sda` es un fichero, `dd` puede copiar un disco entero a una imagen o a otro
disco:

```
sudo dd if=/dev/sda of=/mnt/backup/disco.img bs=4M status=progress
```

El ejemplo es propio, con los operandos citados; `status=progress` **«shows periodic transfer
statistics»**. `dd` copia sin preguntar, y un `of=` equivocado borra el
disco de destino: esta advertencia es oficio.

### Qué copiar y qué no

Los directorios del script de Ubuntu (`/home`, `/etc`, `/root`, `/boot`, `/opt`, `/var/spool/mail`)
son los de datos y configuración. `/proc`, `/sys` y `/tmp` no se copian: los dos primeros son
virtuales (epígrafe 2) y el tercero puede borrarse sin aviso, incluso al arrancar. Esta deducción es oficio, apoyada en las
definiciones de la FHS y de `hier(7)`.

## 11. Filtros: grep

Un filtro lee texto (de ficheros o de la entrada estándar), lo transforma y lo escribe en la salida
estándar, de modo que se puede encadenar en tuberías (epígrafe 4). `grep`, `sed` y `awk` son los tres
que nombra el enunciado. Esta definición de filtro es oficio; la de cada herramienta, de su manual.

### Qué hace

**«Given one or more patterns, grep searches input files for matches to the patterns. When it finds a
match in a line, it copies the line to standard output (by default), or produces whatever other sort
of output you have requested with options.»** (busca el patrón y copia en la salida las líneas que lo
contienen.) Forma: `grep [opciones] patrón [ficheros]`; sin fichero, lee la entrada estándar.

### Opciones

| Opción | Literal del manual GNU | Ejemplo |
|---|---|---|
| `-i` | **«Ignore case distinctions in patterns and input data»** | `grep -i error syslog` |
| `-v` | **«Invert the sense of matching, to select non-matching lines.»** | `grep -v '^#' fichero.conf` (quita los comentarios) |
| `-w` | **«Select only those lines containing matches that form whole words.»** | `grep -w 'hello' test*.log` no encuentra *Othello* |
| `-c` | **«Suppress normal output; instead print a count of matching lines for each input file.»** | `grep -c sshd auth.log` |
| `-l` | **«Suppress normal output; instead print the name of each input file from which output would normally have been printed.»** | `grep -l 'main' test-*.c` |
| `-n` | **«Prefix each line of output with the 1-based line number within its input file.»** | |
| `-r` | **«For each directory operand, read and process all files in that directory, recursively.»** | `grep -r 'hello' /home/gigi` |
| `-E` | **«Interpret patterns as extended regular expressions (EREs).»** | `grep -E 'error\|fail'` |
| `-F` | **«Interpret patterns as fixed strings, not regular expressions.»** | `grep -F '1.2.3.4'` (el punto, literal) |
| `-o` | **«Print only the matched non-empty parts of matching lines»** | |

Los ejemplos con *hello*, *Othello*, `main` y `/home/gigi` son del manual; los demás, propios.

El estado de salida permite usar `grep` en condiciones: **«Normally the exit status is 0 if a line is
selected, 1 if no lines were selected, and 2 if an error occurred.»** `grep -q usuario /etc/passwd &&
echo existe` es un ejemplo propio de ese uso (la opción `-q` aparece citada junto al estado de salida).

### Expresiones regulares

El patrón de `grep` es una expresión regular, que no es lo mismo que un comodín del shell: el
manual lo avisa, **«the regular expression syntax used in the pattern differs from the globbing syntax
that the shell uses to match file names»**. En un comodín, `*` es «cualquier cosa»; en una expresión
regular, «lo anterior, cero o más veces».

| Elemento | Significado (manual de GNU grep) |
|---|---|
| `.` | **«The period '.' matches any single character.»** |
| `*` | **«The preceding item is matched zero or more times.»** |
| `+` | **«The preceding item is matched one or more times.»** (ERE) |
| `?` | **«The preceding item is optional and is matched at most once.»** (ERE) |
| `{n}`, `{n,}`, `{n,m}` | Exactamente *n*; *n* o más; entre *n* y *m* veces |
| `^` y `$` | **«The caret '^' and the dollar sign '$' are special characters that respectively match the empty string at the beginning and end of a line.»** (anclas de principio y fin de línea) |
| `[...]` | Uno cualquiera de los caracteres; con `^` delante, cualquiera que no esté |

*Básicas frente a extendidas.* Sin `-E`, `grep` usa expresiones básicas, en las que **«The characters
'?', '+', '{', '|', '(', and ')' lose their special meaning; instead use the backslashed versions»**
(`\?`, `\+`, `\{`, `\|`, `\(`, `\)`). Con `-E`, valen sin barra. Por eso, en GNU grep, `grep 'a\|b'` y `grep -E 'a|b'`
buscan lo mismo; el manual avisa de que una expresión básica con `\?`, `\+` o `\|` es de las que
**«portable scripts should avoid»** (no es portable a otras implementaciones).

El ejemplo de la documentación de Ubuntu para listar los usuarios corrientes lo junta todo: `cat
/etc/passwd | cut -d : -f 1,3 | grep -E ':[0-9]{4,}'`, donde **«The regular expression :[0-9]{4,}
means all digits, repeated 4 times or more»** (UID de cuatro cifras o más).

## 12. Editor de flujo: sed

### Qué es

**«sed is a stream editor. A stream editor is used to perform basic text transformations on an input
stream (a file or input from a pipeline).»** **«sed works by making only one pass over the input(s),
and is consequently more efficient. But it is sed's ability to filter text in a pipeline which
particularly distinguishes it from other types of editors.»** (edita sin abrir el fichero en un
editor, en una sola pasada, y sobre todo sirve de filtro en tuberías.)

Cómo trabaja: **«sed operates by performing the following cycle on each line of input: first, sed
reads one line from the input stream, removes any trailing newline, and places it in the pattern
space. Then commands are executed»**; al final del guion, **«unless the -n option is in use, the
contents of pattern space are printed out to the output stream»**. Es decir: lee una línea, le aplica
las órdenes, la imprime y pasa a la siguiente.

### Sustituir: s

**«The s command (as in substitute) is probably the most important in sed and has a lot of different
options. The syntax of the s command is 's/regexp/replacement/flags'.»** **«the s command attempts to
match the pattern space against the supplied regular expression regexp; if the match is successful,
then that portion of the pattern space which was matched is replaced with replacement.»**

| Indicador | Qué hace |
|---|---|
| (ninguno) | **«Without the 'g' (global) modifier, sed affects only the first instance per line.»** |
| `g` | **«Apply the replacement to all matches to the regexp, not just the first.»** |
| un número *N* | **«Only replace the numberth match of the regexp.»** |
| `I` | **«makes sed match regexp in a case-insensitive manner»** (extensión GNU) |

En la sustitución, `&` es todo lo encontrado y `\1`…`\9` lo que estaba entre el paréntesis `\(`…`\)`
correspondiente, según el manual.

### Direcciones: a qué líneas

**«Addresses determine on which line(s) the sed command will be executed.»** Ejemplos del manual:

```
sed '144s/hello/world/' input.txt > output.txt     # sólo en la línea 144
sed '/apple/s/hello/world/' input.txt > output.txt # sólo en las líneas con «apple»
sed '4,17s/hello/world/' input.txt > output.txt    # de la 4 a la 17
sed '/apple/!s/hello/world/' input.txt > output.txt  # en las que NO tienen «apple»
```

`$` es la última línea (**«This address matches the last line of the last file of input»**). El `!`
niega la dirección.

### Otras órdenes y opciones

| Elemento | Qué hace |
|---|---|
| `d` | **«Delete the pattern space; immediately start next cycle.»** `seq 3 \| sed 2d` imprime 1 y 3 |
| `p` | **«Print out the pattern space (to the standard output). This command is usually only used in conjunction with the -n command-line option.»** |
| `-n` | Desactiva la impresión automática: **«These options disable this automatic printing»**. `sed -n '45p' file.txt` imprime sólo la línea 45 |
| `-e` | Añade una orden al guion; se pueden poner varias |
| `-f` | Lee las órdenes de un fichero (`sed -f myscript.sed input.txt`) |
| `-i[SUFIJO]` | **«This option specifies that files are to be edited in-place.»** Con sufijo, guarda una copia del original: `sed -i.bak …` |
| `-E` | **«Use extended regular expressions rather than basic regular expressions.»** |
| `y/abc/xyz/` | **«Transliterate any characters in the pattern space which match any of the source-chars with the corresponding character in dest-chars.»** |

Sin `-i`, `sed` no toca el fichero: **«sed writes output to standard output. Use -i to edit files
in-place instead of printing to standard output.»** `sed 's/hello/world/g' input.txt > output.txt`
deja `input.txt` intacto; `sed -i 's/hello/world/' file.txt` **«modifies file.txt and does not produce
any output»**.

Ejemplo propio de administración: `sed -i.bak 's/^PermitRootLogin yes/PermitRootLogin no/'
/etc/ssh/sshd_config` cambia una directiva de configuración y guarda el original con `.bak`. El nombre
de la directiva de SSH no se ha comprobado en fuente; el ejemplo vale por la sintaxis.

## 13. Lenguaje awk

### Qué es

**«The basic function of awk is to search files for lines (or other units of text) that contain
certain patterns. When a line matches one of the patterns, awk performs specified actions on that
line.»** **«awk programs are data driven (i.e., you describe the data you want to work with and then
what to do when you find it).»** Un programa es una serie de reglas `patrón { acción }`:

```
pattern { action }
pattern { action }
```

Se ejecuta así: **«awk 'program' input-file1 input-file2 ...»**, o con el programa en un fichero:
**«awk -f program-file input-file1 input-file2 ...»**. En Ubuntu y Debian la orden `awk` puede ser
`gawk` (GNU) u otra implementación; el manual citado es el de `gawk`, y cuál se instala por defecto no
se ha comprobado en fuente.

### Campos y registros

**«By default, fields are separated by whitespace, like words in a line.»** **«$1 refers to the first
field, $2 to the second, and so on.»** **«The use of $0, which looks like a reference to the "zeroth"
field, is a special case: it represents the whole input record.»** Y **«the last field in a record can
be represented by $NF»**.

| Variable | Qué es |
|---|---|
| `NF` | **«The number of fields in the current input record.»** |
| `NR` | **«The number of input records awk has processed since the beginning of the program's execution»** (el número de línea, en la práctica) |
| `FS` | **«The input field separator»**; se fija con `-F` |
| `OFS` | **«The output field separator»**; su valor por defecto es **«a string consisting of a single space»** |

*Separador.* **«FS can be set on the command line. Use the -F option to do so.»** `awk -F, 'program'
input-files` usa la coma; **«the option uses an uppercase 'F' instead of a lowercase 'f'. The latter
option (-f) specifies a file containing an awk program.»** Ejemplo del manual sobre el fichero de
usuarios: `awk -F: '$5 == ""' /etc/passwd` imprime **«the entries for users whose full name is not
indicated»** (las cuentas con el campo GECOS vacío).

### Patrones y acciones

- Una expresión regular entre barras es un patrón: **«A regular expression can be used as a pattern by
  enclosing it in slashes.»** `awk '/li/ { print $2 }' mail-list` imprime el segundo campo de las
  líneas que contienen *li*.
- Comparar un campo: `~` y `!~`. `awk '$1 ~ /J/' inventory-shipped` selecciona las líneas cuyo primer
  campo contiene una *J*.
- Sin patrón o sin acción, según `gawk(1)`: **«If the pattern is missing, the action executes for every
  single record of input. A missing action is equivalent to { print } which prints the entire
  record.»** El ejemplo anterior, sin acción, saca la línea entera.
- `BEGIN` y `END`: **«A BEGIN rule is executed once only, before the first input record is read.
  Likewise, an END rule is executed once only, after all the input is read.»**

### print y printf

`print` con comas separa los campos con el separador de salida; sin comas, los pega. El manual lo
muestra: `awk '{ print $1, $2 }' inventory-shipped` da `Jan 13`, y `awk '{ print $1 $2 }'` da
`Jan13`, porque **«juxtaposing two string expressions in awk means to concatenate them»**. `printf`
da formato: `awk '{ printf "%-10s %s\n", $1, $2 }' mail-list` **«prints the names of the people ($1)
in the file mail-list as a string of 10 characters that are left-justified»**.

### Ejemplos de administración

Ejemplos propios, no ejecutados, con los elementos citados:

```
awk -F: '$3 >= 1000 { print $1 }' /etc/passwd     # usuarios corrientes (UID ≥ 1000)
df -h | awk 'NR > 1 { print $5, $6 }'              # uso y punto de montaje, sin cabecera
awk '{ n++ } END { print n }' fichero               # cuenta líneas, como wc -l
ps aux | awk '{ s += $4 } END { print s }'          # suma la columna 4 de ps aux (%MEM)
```

El ejemplo del manual con `BEGIN` y `END` cuenta las líneas que contienen *li*:

```
awk 'BEGIN { print "Analysis of \"li\"" }
     /li/  { ++n }
     END   { print "\"li\" appears in", n, "records." }' mail-list
```

**«There is no need to use the BEGIN rule to initialize the counter n to zero, as awk does this
automatically»** (las variables empiezan a cero).

Que la cuarta columna de `ps aux` es `%MEM` no se ha comprobado en la página de `ps`; el ejemplo vale
por la sintaxis de `awk`.

### Cuál usar

`grep` selecciona líneas; `sed` las transforma (sobre todo, sustituye); `awk` trabaja por campos y
calcula. Las tres se combinan en tubería. El reparto es oficio, coherente con las definiciones
citadas.

## Lo que este tema no da, y dónde está

- Los conceptos generales de sistema operativo (núcleo, procesos, planificación, concurrencia): tema 5.
  Windows 11, PowerShell y Windows Server: temas 6, 7 y 8. La virtualización: tema 10. Las redes
  (direcciones IP, protocolos): tema 13. La seguridad del puesto: tema 14.
- Las versiones vigentes de Red Hat Enterprise Linux, Fedora y derivadas: no se han consultado.
- La fusión de `/bin` y `/sbin` en `/usr` que hacen algunas distribuciones, y si hay una versión de la
  FHS posterior a la 3.0: no se han comprobado en fuente.
- Los nombres de dispositivo de discos NVMe y tarjetas, las diferencias de capacidad y número de
  particiones entre MBR y GPT, y las órdenes interactivas de `fdisk`: no se han leído en fuente.
- El sistema de ficheros que propone por defecto el instalador de Ubuntu, y la implementación de `awk`
  instalada por defecto en Ubuntu y Debian: no comprobados.
- `groupdel`, `chage` en su página de manual, `newgrp`, `visudo` y el formato de `/etc/sudoers`: no se
  han leído en detalle; el tema da sólo lo que cita la documentación de Ubuntu.
- *Snap*, *Flatpak* y otros formatos de paquete universales; `cpio`, *Déjà Dup* y la configuración de
  Bacula y rsnapshot: fuera de las fuentes leídas.
- El editor de texto de consola (`nano`, `vi`): el enunciado no lo nombra y no se ha estudiado.
- Qué distribución, versión o herramientas de copia se usan en los equipos de la RTVA y de CSRTV: no
  consta en ningún documento publicado.

## Trazabilidad

Todas las fuentes se leyeron el 05-10-2026. Las páginas de manual son las del proyecto *Linux
man-pages* servidas en man7.org (cada una en la versión del paquete que la mantiene: coreutils,
util-linux, shadow, systemd, procps, e2fsprogs, LVM2, mdadm, cryptsetup, dpkg, rpm, dnf, tar, rsync,
Bash, sudo, cronie), salvo `apt(8)`, leída en manpages.ubuntu.com en su versión de Ubuntu 26.04
(*resolute*). Están en inglés: la traducción entre paréntesis es del tema.

| Fuente | Qué sostiene |
|---|---|
| Ubuntu, «Ubuntu release cycle» (ubuntu.com/about/release-cycle) | Cadencia semestral, numeración, LTS cada dos años con cinco años de mantenimiento, intermedias de nueve meses, 26.04 y 24.04 LTS |
| Debian, «Debian Releases» (debian.org/releases) | Debian 13 *trixie* estable, revisión 13.7 de 12-09-2026, *bookworm* *oldstable* |
| Ubuntu Server documentation, «Basic installation» (tutorial) | Arquitecturas, requisitos, copia previa, ISO, USB, teclas de arranque, pasos del instalador |
| Ubuntu Server documentation, «User management» | Cuentas locales y NSS, root deshabilitado, sudo y sudo-rs, grupo sudo, tipos de UID, `nobody`, `adduser`/`deluser`/`addgroup`, bloqueo, permisos de los directorios personales, `/etc/skel`, `DIR_MODE`, longitud mínima de contraseña, `chage` |
| Ubuntu Server documentation, «Package management» | APT, índice y `ubuntu.sources`, `apt update/install/remove/upgrade`, `--purge`, `apt` frente a `apt-get`, Aptitude, `dpkg -l/-L/-S/-i/-r`, aviso sobre `dpkg -r`, actualizaciones automáticas, Universe y Multiverse |
| Ubuntu Server documentation, «Backups and version control» y «How to back up using shell scripts» | Plan de copias, copia fuera de las instalaciones, Bacula, rsnapshot, incrementales, etckeeper, script con `tar`, campos de `crontab`, prueba y restauración, rotación abuelo-padre-hijo; la errata de las «12:00 pm» |
| *Filesystem Hierarchy Standard* 3.0, Linux Foundation (refspecs.linuxfoundation.org/FHS_3.0) | Objeto de la norma y rótulos de cada directorio |
| `hier(7)` | Descripciones de `/`, `/bin`, `/boot`, `/dev`, `/etc`, `/proc`, `/sbin`, `/tmp`, `/usr`, `/usr/bin`, `/usr/local`, subdirectorios de `/var/spool` |
| GNU Coreutils manual, «What information is listed», «Structure of File Mode Bits», «The Umask and Protection» (gnu.org, versión 9.12) | Campos de `ls -l`, letras de tipo de fichero, `s`/`S`/`t`/`T`, significado de r, w, x en directorios, *setuid*, *setgid* |
| `chmod(1)`, `chown(1)`, `chgrp(1)`, `umask(2)`, `getfacl(1)`, `setfacl(1)`, `ln(1)`, `ls(1)` | Permisos simbólicos y octales, *sticky bit*, dueño y grupo, máscara 022, ACL y sus ejemplos, enlaces |
| `passwd(5)`, `shadow(5)`, `group(5)`, `useradd(8)`, `usermod(8)`, `userdel(8)`, `groupadd(8)`, `gpasswd(1)`, `passwd(1)`, `id(1)`, `su(1)`, `sudo(8)` | Ficheros de cuentas y sus campos, órdenes de usuarios y grupos y sus opciones |
| `bash(1)` | Definición, POSIX, órdenes internas `cd`, `export`, `umask`, `alias`, virgulilla, comodines, comillas, variables y parámetros especiales, estado de salida, sustitución de órdenes, redirección, tuberías, listas, `#!`, `if`, `for`, `while`, `case`, SIGINT y ^C |
| `pwd(1)`, `cp(1)`, `mv(1)`, `rm(1)`, `mkdir(1)`, `cat(1)`, `less(1)`, `head(1)`, `tail(1)`, `find(1)`, `sort(1)`, `uniq(1)`, `wc(1)`, `cut(1)`, `tr(1)`, `tee(1)`, `xargs(1)`, `man(1)` | Órdenes de ficheros y de texto, secciones del manual |
| `bootup(7)`, `systemd(1)`, `systemd.special(7)`, `runlevel(8)`, `systemctl(1)`, `shutdown(8)` | Secuencia de arranque y parada, PID 1, tipos de unidad, *targets*, equivalencia con niveles, órdenes de `systemctl`, `shutdown` |
| `journalctl(1)`, `dmesg(1)`, `ps(1)`, `top(1)`, `htop(1)`, `kill(1)`, `signal(7)`, `nice(1)`, `nohup(1)`, `crontab(1)`, `crontab(5)`, `uname(1)`, `hostnamectl(1)`, `uptime(1)`, `free(1)`, `who(1)`, `w(1)`, `last(1)`, `whoami(1)`, `sysctl(8)`, `ip(8)`, `ss(8)` | Herramientas de administración del epígrafe 6 |
| `fstab(5)`, `mount(8)`, `umount(8)`, `mkfs(8)`, `mke2fs(8)`, `fsck(8)`, `e2fsck(8)`, `mkswap(8)`, `swapon(8)` | Sistemas de ficheros, montaje, `fstab`, comprobación, intercambio |
| `fdisk(8)`, `parted(8)`, `lsblk(8)`, `blkid(8)`, `df(1)`, `du(1)`, `lvm(8)`, `pvcreate(8)`, `vgcreate(8)`, `lvcreate(8)`, `lvextend(8)`, `mdadm(8)`, `cryptsetup(8)` | Gestión de discos, LVM, RAID, LUKS |
| `apt(8)` (Ubuntu 26.04), `dpkg(1)`, `rpm(8)`, `dnf(8)` | Órdenes de paquetes |
| GNU tar manual 1.35.90 (secciones «General Synopsis», «Creating and Reading Compressed Archives», «Using tar to Perform Incremental Dumps») y `tar(1)` | Operaciones y opciones, nombres relativos, compresión, incrementales |
| `rsync(1)`, `dd(1)` | Copia y sincronización, copia en bruto |
| GNU grep manual (gnu.org/software/grep/manual) | Definición, opciones, estado de salida, expresiones regulares, BRE frente a ERE, ejemplos |
| GNU sed manual (gnu.org/software/sed/manual) | Definición, ciclo, `s` y sus indicadores, direcciones, `d`, `p`, `y`, opciones `-n`, `-e`, `-f`, `-i`, `-E` |
| *The GNU Awk User's Guide* (gnu.org/software/gawk/manual), secciones 1, 1.1, 3.1, 4.2, 4.5.5, 5.2, 5.5.4, 7.1.4.1, 7.5.1, 7.5.2, y `gawk(1)` | Definición, reglas, campos, `NF`, `NR`, `FS`, `OFS`, `-F`, `-f`, patrones, `BEGIN`/`END`, `print`, `printf` |

Las tablas de órdenes por familias (epígrafe 4), de permisos básicos frente a extendidos (epígrafe 2)
y de tareas de administración y equivalencias con Windows (epígrafe 6) son oficio; cada orden de Linux
que nombran está contrastada con su página de manual en el epígrafe correspondiente, y la columna de
Windows está desarrollada en los temas 6 y 8.

Oficio sin fuente detrás, y así se declara en el texto: que una distribución es núcleo más
herramientas; la síntesis de la instalación; que una ruta relativa parte del directorio actual; los
cuadros de parejas de directorios; que un disco es dispositivo de bloques y un terminal de caracteres;
que `usermod -G` sin `-a` sustituye los grupos; que `su` pide la contraseña del destino; que una
asignación de variable no lleva espacios; que el directorio actual no suele estar en `PATH`; que
`halt` no apaga la alimentación; la agrupación de los tipos de sistema de ficheros por uso; la
advertencia de que formatear y `dd` destruyen datos; reparar desde el modo de rescate; que la tabla
*MS-DOS* de `parted` es la MBR; que `-f` de `tar` va la última del grupo; probar `fstab` con `mount -a`; el reparto entre
`df` y `du`; la secuencia para añadir un disco; la lectura de la ventaja de LVM; la falta de
redundancia de RAID0; `/dev/mapper`; la definición de filtro; el reparto entre `grep`, `sed` y `awk`;
los ejemplos propios señalados como tales (no ejecutados) y la selección de herramientas del epígrafe 6.
