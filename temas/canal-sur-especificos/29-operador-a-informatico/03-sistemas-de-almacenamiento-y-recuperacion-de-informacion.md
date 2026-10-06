# Tema 3 del específico de Operador/a Informático · Sistemas de almacenamiento y recuperación de información

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 3 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Storage Networking Industry Association (SNIA), *Online Dictionary*; NVM Express; SD Association. Microsoft Learn (`fsutil behavior`, administración de discos, `robocopy`, `wbadmin start backup`, `vssadmin`, `compact`, `tar`, Acceso controlado a carpetas) y Soporte de Microsoft (Copias de seguridad de Windows, Recuperación de archivos de Windows, comprimir y descomprimir). Manuales de `rsync`, GNU `dd`, GNU `gzip` y GNU `tar`; 7-Zip; Clonezilla; CGSecurity (PhotoRec y TestDisk). INCIBE, guía *Ransomware* (2020); No More Ransom. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las ediciones citadas, en línea el 05-10-2026 y leídas ese día |
| Extensión | 10.300 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); el bit y el byte (B), con los
múltiplos decimales kilobyte (kB), megabyte (MB), gigabyte (GB), terabyte (TB) y petabyte (PB) y los
binarios kibibyte (KiB), mebibyte (MiB), gibibyte (GiB) y tebibyte (TiB); disco duro magnético (HDD,
*hard disk drive*) y disco o unidad de estado sólido (SSD, *solid-state drive*); conjunto redundante de
discos independientes (RAID, *redundant array of independent disks*); conjunto de discos sin más (JBOD,
*just a bunch of disks*); cinta lineal abierta (LTO, *linear tape-open*) y su sistema de ficheros (LTFS,
*linear tape file system*); almacenamiento de conexión directa (DAS, *direct-attached storage*),
almacenamiento conectado a la red (NAS, *network-attached storage*) y red de almacenamiento (SAN,
*storage area network*); las interfaces serie avanzada (SATA, *Serial ATA*) y serie conectada (SAS,
*Serial Attached SCSI*, donde SCSI es la interfaz de sistemas de ordenadores pequeños, *small computer
system interface*); el bus de interconexión de componentes periféricos exprés (PCI, *peripheral component interconnect*; PCI Express o PCIe) y la especificación NVM Express (NVMe), la interfaz de
las SSD sobre PCIe; canal de fibra (FC, *Fibre Channel*) y protocolo de órdenes SCSI sobre redes IP
(iSCSI); sistema de ficheros en red (NFS, *network file system*), bloque de mensajes del servidor (SMB,
*server message block*) y el sistema de ficheros común de Internet (CIFS, *common Internet file
system*), que nombra la SNIA; operaciones de entrada y
salida por segundo (IOPS); gestión de activos de medios (MAM, *media asset management*); objetivo de
punto de recuperación (RPO, *recovery point objective*) y objetivo de tiempo de recuperación (RTO,
*recovery time objective*); servicio de instantáneas de volumen de Windows (VSS, *Volume Shadow Copy
Service*); listas de control de acceso (ACL, *access control lists*); cuenta personal de Microsoft (MSA,
*Microsoft account*); sistemas de ficheros NTFS (*New Technology File System*), FAT, FAT32 y exFAT (*file
allocation table* y su variante extendida) y ext2/ext3/ext4 (los de Linux); tarjetas SD (*Secure
Digital*) y sus clases SDHC, SDXC y SDUC (alta capacidad, capacidad extendida y ultra capacidad); bus
de velocidad ultra alta de las tarjetas (UHS, *ultra high speed*); registro de arranque maestro (MBR,
*master boot record*) y tabla de particiones con identificadores únicos globales (GPT, *GUID partition table*, con GUID por
*globally unique identifier*); interfaz de firmware
extensible unificada (UEFI) y sistema básico de entrada y salida (BIOS); identificador de seguridad de
Windows (SID, *security identifier*); estándar de cifrado avanzado (AES, *advanced encryption
standard*); convención universal de nombres de las rutas de red (UNC, *universal naming convention*);
codificación de Lempel y Ziv (LZ77), base de `gzip`, y LZMA y LZMA2, algoritmos de compresión del
formato 7z; licencias públicas generales de GNU (GPL) y su variante reducida
(LGPL, *Lesser GPL*); formato de documento portátil (PDF); memoria de acceso aleatorio (RAM,
*random-access memory*); bus serie universal (USB, *universal serial bus*); Microsoft, abreviado MS en
alguna cita; formatos de archivo comprimido ZIP, 7z y RAR, y formato de imagen de Windows (WIM,
*Windows Imaging Format*); tecnología de
autosupervisión de los discos (SMART); Instituto Nacional de Ciberseguridad (INCIBE); Oficina Europea
de Policía (EUROPOL).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 3): «Sistemas de almacenamiento
> y recuperación de información: discos duros, discos de estado sólido, memorias flash, sistemas SAN y
> NAS; herramientas software de copia de seguridad, compresión de datos y clonación de discos;
> recuperación de datos en caso de borrado accidental, avería o ataque de virus.»

Qué se puede preguntar: cuántos bits tiene un kibibyte y en qué se diferencia de un kilobyte; qué
distingue un disco magnético de uno de estado sólido (tiempo de acceso, partes móviles, ciclos de
escritura) y qué son caudal e IOPS; qué es la memoria flash, la nivelación de desgaste, TRIM, la
amplificación de escritura, la recolección de basura y el sobreaprovisionamiento; cómo se comprueba
TRIM en Windows; qué es NVMe, sobre qué bus trabaja y cuál es su versión vigente; las capacidades y el
sistema de ficheros de SD, SDHC, SDXC y SDUC y sus clases de velocidad; qué hace cada nivel RAID, con
cuántos discos y cuánta capacidad útil deja; por qué un RAID no es una copia de seguridad; qué
diferencia DAS, NAS y SAN, qué sirve ficheros y qué sirve bloques, y qué protocolos van con cada uno;
qué son RPO y RTO; la regla 3-2-1; qué copian la copia completa, la diferencial y la incremental y qué
exige restaurar cada una; qué herramientas de copia trae Windows (Copias de seguridad de Windows,
`wbadmin`, `robocopy`, instantáneas) y Linux (`rsync`, `tar`); qué es la compresión sin pérdida, qué
algoritmo usa `gzip`, qué formatos maneja 7-Zip y el Explorador de Windows 11 y qué hace `compact`;
qué es clonar un disco, qué hace Clonezilla y qué hace `dd conv=noerror,sync`; por qué se puede
recuperar un fichero borrado y qué no hay que hacer después; qué modo de `winfr` corresponde a cada
caso; qué hacen PhotoRec y TestDisk; y los pasos que da INCIBE ante un *ransomware*. En la aplicación
práctica: calcular la capacidad útil de un RAID, decidir qué copias hacen falta para restaurar,
escribir la orden de copia o de recuperación adecuada y ordenar la respuesta a un cifrado.

<!-- indice -->

## Índice

- [1. Sistemas de almacenamiento y recuperación de información: el mapa](#1-sistemas-de-almacenamiento-y-recuperación-de-información-el-mapa)
  - [Las unidades](#las-unidades)
  - [Los soportes](#los-soportes)
  - [Las dos magnitudes con que se dimensiona](#las-dos-magnitudes-con-que-se-dimensiona)
  - [Almacenar no es recuperar](#almacenar-no-es-recuperar)
- [2. Discos duros](#2-discos-duros)
  - [Cómo guardan](#cómo-guardan)
  - [Por dónde se conectan](#por-dónde-se-conectan)
  - [Vigilarlo y sustituirlo](#vigilarlo-y-sustituirlo)
- [3. Discos de estado sólido y memorias flash](#3-discos-de-estado-sólido-y-memorias-flash)
  - [La memoria flash](#la-memoria-flash)
  - [Lo que hace el controlador: desgaste, TRIM y recolección de basura](#lo-que-hace-el-controlador-desgaste-trim-y-recolección-de-basura)
  - [NVMe](#nvme)
  - [Tarjetas de memoria SD](#tarjetas-de-memoria-sd)
  - [Memorias USB](#memorias-usb)
- [4. Sistemas SAN y NAS](#4-sistemas-san-y-nas)
  - [Por qué se saca el disco del equipo](#por-qué-se-saca-el-disco-del-equipo)
  - [NAS: almacenamiento conectado a la red](#nas-almacenamiento-conectado-a-la-red)
  - [SAN: red de almacenamiento](#san-red-de-almacenamiento)
  - [Ficheros frente a bloques](#ficheros-frente-a-bloques)
  - [La redundancia dentro de la cabina: RAID](#la-redundancia-dentro-de-la-cabina-raid)
  - [En línea, casi en línea, fuera de línea](#en-línea-casi-en-línea-fuera-de-línea)
- [5. Herramientas software de copia de seguridad](#5-herramientas-software-de-copia-de-seguridad)
  - [Qué es una copia de seguridad](#qué-es-una-copia-de-seguridad)
  - [Las dos cifras que se fijan antes de elegir la herramienta](#las-dos-cifras-que-se-fijan-antes-de-elegir-la-herramienta)
  - [Los tipos de copia](#los-tipos-de-copia)
  - [La regla 3-2-1 y lo que hoy se le añade](#la-regla-3-2-1-y-lo-que-hoy-se-le-añade)
  - [La política y la prueba de restauración](#la-política-y-la-prueba-de-restauración)
  - [La cinta](#la-cinta)
  - [Windows: Copias de seguridad de Windows](#windows-copias-de-seguridad-de-windows)
  - [Windows: wbadmin](#windows-wbadmin)
  - [Windows: robocopy](#windows-robocopy)
  - [Windows: las instantáneas (VSS)](#windows-las-instantáneas-vss)
  - [Linux: rsync y tar](#linux-rsync-y-tar)
- [6. Herramientas software de compresión de datos](#6-herramientas-software-de-compresión-de-datos)
  - [Sin pérdida y con pérdida](#sin-pérdida-y-con-pérdida)
  - [gzip y tar](#gzip-y-tar)
  - [7-Zip](#7-zip)
  - [Lo que trae Windows 11](#lo-que-trae-windows-11)
- [7. Herramientas software de clonación de discos](#7-herramientas-software-de-clonación-de-discos)
  - [Clonar o hacer imagen](#clonar-o-hacer-imagen)
  - [Clonezilla](#clonezilla)
  - [dd](#dd)
  - [Rescatar un disco que falla](#rescatar-un-disco-que-falla)
- [8. Recuperación de datos en caso de borrado accidental, avería o ataque de virus](#8-recuperación-de-datos-en-caso-de-borrado-accidental-avería-o-ataque-de-virus)
  - [Borrado accidental: por qué se puede](#borrado-accidental-por-qué-se-puede)
  - [Borrado accidental: el orden en que se busca](#borrado-accidental-el-orden-en-que-se-busca)
  - [Recuperación de archivos de Windows (winfr)](#recuperación-de-archivos-de-windows-winfr)
  - [PhotoRec y TestDisk](#photorec-y-testdisk)
  - [Avería](#avería)
  - [Ataque de virus: el ransomware](#ataque-de-virus-el-ransomware)
  - [Aplicación práctica: tres casos del puesto](#aplicación-práctica-tres-casos-del-puesto)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Sistemas de almacenamiento y recuperación de información: el mapa

### Las unidades

Todo lo demás depende de tener clara la aritmética, y es donde más se falla, porque hay dos familias de
múltiplos y se parecen.

| Familia | Base | Ejemplo |
|---|---|---|
| Decimal | potencias de mil | un kilobyte son mil bytes; un terabyte, un billón de bytes |
| Binaria | potencias de mil veinticuatro | un kibibyte son mil veinticuatro bytes |

Las tres igualdades que hay que saber de memoria:

1. Un byte son ocho bits.
2. Un kibibyte son mil veinticuatro bytes.
3. Por tanto un kibibyte son ocho mil ciento noventa y dos bits.

Ejemplo de cálculo: cuatro kibibytes son 4 × 1.024 = 4.096 bytes, y 4.096 × 8 = 32.768 bits. Las dos
trampas habituales son contar en base mil (32.000) y responder en bytes cuando se piden bits (4.096): se
subraya la unidad antes de calcular. Un disco que el fabricante anuncia en terabytes decimales aparece
con menos «TB» en el sistema operativo si este cuenta en potencias de dos; no falta capacidad, cambia la
unidad (oficio).

### Los soportes

Los cuatro soportes que conviven en una instalación de televisión, con lo que aporta cada uno:

| Soporte | Cómo guarda | Para qué sirve aquí |
|---|---|---|
| Disco magnético (HDD) | platos que giran y una cabeza que se desplaza | el grueso de la capacidad en línea: mucho espacio a coste bajo |
| Disco de estado sólido (SSD) | memoria no volátil, sin partes móviles | lo que exige acceso inmediato: bases de datos, caché, edición sobre material vivo |
| Cinta magnética (LTO) | acceso secuencial, soporte extraíble | el archivo a largo plazo y la copia de seguridad |
| Soporte óptico | lectura por haz luminoso | residual en explotación; se conserva por compatibilidad con fondos antiguos |

Y por la ubicación:

- Local: en el propio equipo.
- En red: unidades compartidas, cabinas de almacenamiento.
- En la nube: alojado en servidores de un proveedor y accesible por internet.

### Las dos magnitudes con que se dimensiona

La diferencia que de verdad importa entre el disco magnético y el de estado sólido no es la velocidad de
transferencia: es el tiempo de acceso. El magnético tiene que mover una cabeza y esperar a que el plato
pase por debajo; el de estado sólido no espera a nada. Por eso el magnético sigue siendo excelente para
leer un fichero grande de corrido —una emisión— y malo para atender mil peticiones pequeñas a la vez.

Y de ahí salen las dos magnitudes con las que se dimensiona:

- El caudal: cuántos bits por segundo salen de corrido. Es lo que manda cuando se reproduce o se graba
  vídeo.
- Las operaciones por segundo: cuántas peticiones independientes atiende. Es lo que manda cuando hay
  muchos puestos de edición pinchando a la vez sobre el mismo material.

Un sistema puede tener capacidad de sobra y caudal de sobra y aun así ahogarse por operaciones por
segundo. Dimensionar sólo por terabytes es el error clásico.

### Almacenar no es recuperar

La segunda mitad del enunciado —copia, compresión, clonación, recuperación— existe porque todo soporte
falla o se borra. La redundancia interna de un conjunto de discos protege del fallo de un disco y de
nada más. No protege del borrado por error, ni del programa malicioso que cifra los ficheros, ni del
incendio de la sala. Un conjunto redundante no es una copia de seguridad, y confundir las dos cosas es el
error que más material ha destruido en esta industria.

## 2. Discos duros

### Cómo guardan

El disco duro clásico guarda los datos en platos giratorios que lee y escribe un cabezal. Barato por
unidad de capacidad, más lento y con partes móviles. Las partes móviles explican sus dos rasgos: el
tiempo de acceso (mover la cabeza y esperar a que el plato pase) y el desgaste mecánico, que es la
avería típica (oficio). Por eso sigue siendo el soporte del grueso de la capacidad y de las copias en
disco, y no del sistema del puesto, que hoy va en estado sólido.

### Por dónde se conectan

| Interfaz | Dónde vive | Qué la caracteriza |
|---|---|---|
| Serie avanzada (SATA) | equipos de escritorio y discos de capacidad | sencilla y barata; una cola de órdenes corta |
| Serie conectada (SAS) | cabinas y servidores | doble camino a cada disco, colas largas, pensada para funcionar sin parar |
| Memoria no volátil sobre PCIe (NVMe) | discos de estado sólido rápidos | habla directamente con el bus del procesador; muchas colas en paralelo |

La idea que ordena la tabla: cada interfaz nació para un tipo de disco. La serie avanzada se diseñó para
un disco que gira y no puede atender más de una cosa a la vez; la memoria no volátil, para un disco que
sí puede, y por eso su ganancia no está en el cable sino en dejar de fingir que hay una cabeza que mover.

### Vigilarlo y sustituirlo

El disco anuncia su deterioro por SMART, y el sistema de ficheros se comprueba con `chkdsk`; la lectura
de los atributos SMART, las autopruebas y la sustitución física del disco se estudian en el tema 2.
Para este tema basta la consecuencia: un disco que empieza a dar errores de lectura no se repara, se
copia cuanto antes a otro soporte (§ 7, «Rescatar un disco que falla») y se sustituye.

## 3. Discos de estado sólido y memorias flash

### La memoria flash

La SNIA define la memoria flash como **«A type of non-volatile memory used in solid state storage.»**
(un tipo de memoria no volátil usada en el almacenamiento de estado sólido), y este como **«A storage
capability built using solid state electronics as the non-volatile storage medium.»** (capacidad de
almacenamiento construida con electrónica de estado sólido como medio no volátil). No volátil quiere
decir que conserva los datos sin alimentación, a diferencia de la RAM.

Es la misma tecnología en tres formatos: el disco de estado sólido del equipo, la memoria USB y la
tarjeta de memoria. Frente al disco magnético: memoria flash sin partes móviles. Mucho más rápido, más
caro y con un número finito de ciclos de escritura.

### Lo que hace el controlador: desgaste, TRIM y recolección de basura

Ese número finito de ciclos obliga a que el controlador de la unidad gestione dónde escribe. Las cinco
nociones, con la definición de la SNIA:

| Noción | Definición (SNIA) | En castellano |
|---|---|---|
| Nivelación de desgaste (*wear leveling*) | **«A set of algorithms utilized by a flash controller to distribute writes and erases across the cells in a flash device. Cells in flash devices have a limited ability to survive write cycles. The purpose of wear leveling is to delay cell wear out and prolong the useful life of the overall flash device.»** | El controlador reparte escrituras y borrados entre todas las celdas para que no se gasten unas antes que otras y alargar la vida de la unidad |
| TRIM | **«A method by which the host operating system may inform a storage device of blocks of data that are no longer in use and no longer require logical to physical mapping resources. Many storage protocols support this functionality (e.g., ATA TRIM, NVMe Deallocate, and SCSI UNMAP).»** | El sistema operativo avisa a la unidad de qué bloques ya no usa; cada familia de interfaz tiene su orden |
| Amplificación de escritura | **«Increase in the number of write operations by the device beyond the number of write operations requested by hosts.»** … **«In flash storage this may happen because of garbage collection.»** | La unidad escribe más de lo que el equipo le pide, sobre todo por la recolección de basura |
| Recolección de basura (*garbage collection*) | **«The process of reclaiming resources that are no longer in use.»** | Recuperar el espacio que ya no se usa |
| Sobreaprovisionamiento | **«Purposely providing more capacity than advertised.»** … **«The over provisioned capacity is reserved for controller use, is not addressable by the user, and is used to improve performance and device life.»** | La unidad trae más capacidad de la anunciada, reservada al controlador, para rendimiento y duración; la SNIA añade que sirve también para sustituir la capacidad que deja de ser utilizable, por defectos del soporte o por desgaste |

TRIM en Windows se comprueba con `fsutil` (Microsoft Learn): **«Delete notifications (also known as
trim or unmap) is a feature that notifies the underlying storage device of clusters that have been freed
due to a file delete operation.»** (las notificaciones de borrado avisan al dispositivo de los clústeres
liberados al borrar un fichero), y **«For systems using NTFS, trim is enabled by default unless an
administrator disables it.»** Las órdenes son `fsutil behavior query disabledeletenotify` (consulta) y
`fsutil behavior set disabledeletenotify {1|0}`; el parámetro **«Disables (1) or enables (0) delete
notifications.»**, de modo que `DisableDeleteNotify = 0` en la consulta quiere decir TRIM activo y `= 1`,
desactivado.

### NVMe

NVMe es la interfaz de las SSD rápidas. Su consorcio la define así: **«NVM Express (NVMe)
Specification – The register interface and command set for PCI Express technology attached storage
[…] NVMe is widely considered the defacto industry standard for PCIe SSDs.»** (la interfaz de registros
y el juego de órdenes del almacenamiento conectado a PCI Express; estándar de hecho de las SSD PCIe).
Funciona sobre varios transportes, **«PCI Express® (PCIe®), RDMA, TCP and more»**, y **«It is the
industry standard for solid state drives (SSDs) in all form factors (U.2, M.2, AIC, EDSFF).»** En el
puesto, la forma habitual es la tarjeta M.2 en la placa base (oficio).

Versión vigente: **«The latest versions in the NVMe set of specifications were released on August 4,
2026.»**; **«The NVMe 2.4 specifications consists of multiple documents»**. La página no une la fecha y el número en una misma frase, pero el conjunto que describe a continuación
es el 2.4: a la fecha de este tema, esa es la versión vigente.

### Tarjetas de memoria SD

La SD Association (**«Founded in January 2000 by Panasonic, SanDisk and Toshiba (now KIOXIA)»**) fija
la capacidad de cada clase de tarjeta y el sistema de ficheros con que viene formateada:

| Clase | Capacidad y sistema de ficheros (SD Association) |
|---|---|
| SD | **«Up to 2GB SD memory card using FAT 12 and 16 file systems»** |
| SDHC | **«over 2GB-32GB SDHC memory card using FAT32 file system»** |
| SDXC | **«over 32GB-2TB SDXC memory card using exFAT file system»** |
| SDUC | **«over 2TB-128TB SDUC memory card using exFAT file system»** |

Y cuatro familias de clases de velocidad: **«The Speed Classes defined by the SD Association are Class 2,
4, 6 and 10.»**; **«UHS Speed Class 1 (U1) and UHS Speed Class 3 (U3)»**; **«The Video Speed Classes
defined by the SD Association are V6, 10,30,60 and 90.»**; y **«The SD Express Speed Classes defined by
the SD Association are E150, E300, E450 and E600.»** El número de cada símbolo indica la velocidad mínima
de escritura (**«symbols with a number indicate minimum writing speed»**). Una tarjeta para grabar vídeo se elige por su
clase de vídeo, no sólo por su capacidad (oficio).

### Memorias USB

Son memoria flash con controlador y conector USB; su velocidad depende sobre todo de la versión de USB
(oficio), que se estudia en el tema 4. Por su sistema de ficheros, Microsoft asocia FAT y exFAT a **«Tarjetas SD, flash o
unidades USB (< 4 GB)»** y NTFS a **«Equipos (HDD, SSD), discos duros externos, unidades flash o USB
(> 4 GB)»**, lo que importa al recuperar (§ 8).

## 4. Sistemas SAN y NAS

### Por qué se saca el disco del equipo

Consolidar es sacar el almacenamiento de dentro de cada máquina y ponerlo en un sitio común. La razón no
es la elegancia: es que el disco de dentro de un equipo sólo lo aprovecha ese equipo, y en una
instalación con decenas de puestos eso significa comprar diez veces lo que se usa una.

Las tres arquitecturas, que es la pregunta clásica:

| Arquitectura | Qué ve el equipo | Por dónde va |
|---|---|---|
| Conexión directa (DAS) | un disco suyo | un cable de la propia máquina |
| Conectado a la red (NAS) | una carpeta compartida: ficheros | la red de datos general |
| Red de almacenamiento (SAN) | un disco suyo, aunque esté lejos: bloques | una red dedicada al almacenamiento |

### NAS: almacenamiento conectado a la red

La SNIA define el NAS como **«A term used to refer to storage devices that connect to a network and
provide file access services to computer systems. These devices generally consist of an engine that
implements the file services, and one or more devices, on which data is stored. NAS uses file access
protocols such as NFS or CIFS.»** Es decir: un equipo que se conecta a la red y sirve ficheros, con un
motor que implementa el servicio de ficheros y uno o varios discos; habla protocolos de ficheros.

Los protocolos de ficheros, que sirven carpetas:

- Sistema de ficheros en red (NFS): el compartido de tradición de los sistemas de tipo unix.
- Bloque de mensajes del servidor (SMB): el compartido de tradición de los sistemas de escritorio de
  oficina.

En el puesto, un NAS se ve como una unidad de red o una ruta compartida del tipo
`\\servidor\recurso`; su uso más corriente en una oficina es la carpeta común del departamento y el
destino de las copias de los equipos (oficio).

### SAN: red de almacenamiento

La SNIA la define como **«A network whose primary purpose is the transfer of data between computer
systems and storage devices and among storage devices.»** (una red cuyo fin principal es transferir
datos entre los ordenadores y los dispositivos de almacenamiento, y entre estos), y precisa: **«The term
SAN is usually (but not necessarily) identified with block services.»** Lo normal —no lo necesario— es
que una SAN sirva bloques.

Los protocolos de red de almacenamiento, que sirven bloques:

- Canal de fibra (FC): red dedicada, propia, con sus conmutadores y su direccionamiento. Es la solución
  tradicional de las cabinas grandes y su virtud es que no comparte camino con nada más.
- Órdenes de dispositivo sobre red de datos (iSCSI): las mismas órdenes de disco encapsuladas para
  viajar por la red general. Ahorra una red entera a cambio de compartirla.

### Ficheros frente a bloques

La frontera que hay que saber explicar es la del medio: el almacenamiento conectado a la red sirve
ficheros y la red de almacenamiento sirve bloques. Quien sirve ficheros decide él cómo se guardan y
arbitra entre clientes; quien sirve bloques entrega trozos de disco y es el cliente el que pone encima su
sistema de ficheros. De ahí se derivan las dos consecuencias prácticas:

- Compartir un mismo volumen de bloques entre varios equipos exige un sistema de ficheros preparado para
  ello. Montar un volumen de bloques corriente en dos máquinas a la vez corrompe los datos. Es un error
  caro y se comete.
- Servir ficheros añade una capa y con ella algo de retardo, a cambio de que compartir sea natural.

Por eso una base de datos exigente se pone sobre la SAN: necesita un disco, no una carpeta.

La regla para no equivocarse en un examen: si el nombre del protocolo apunta a órdenes de disco, sirve
bloques; si apunta a ficheros o a carpetas compartidas, sirve ficheros. Y la red de almacenamiento va con
los primeros; el almacenamiento conectado a la red, con los segundos.

La tercera forma, más reciente: el almacenamiento por objetos, donde no hay ni bloques ni árbol de
carpetas, sino objetos con un identificador y sus datos descriptivos, servidos por peticiones de red.
Se usa sobre todo para grandes volúmenes, para el archivo profundo y en el almacenamiento contratado a
un tercero (oficio).

### La redundancia dentro de la cabina: RAID

NAS y SAN guardan los datos en conjuntos de discos. El principio: un disco falla, y con suficientes
discos la pregunta no es si fallará alguno, sino cuándo. La redundancia consiste en guardar información
sobrante para que la pérdida de un disco no sea la pérdida de los datos.

| Nivel | Qué hace | Mínimo de discos | Capacidad útil | Aguanta |
|---|---|---|---|---|
| RAID 0 (conjunto sin redundancia) | reparte los datos en trozos entre todos los discos | dos | toda | ningún fallo |
| RAID 1 (espejo) | escribe lo mismo en dos discos | dos | la mitad | un disco de cada pareja |
| RAID 5 (paridad simple) | reparte los datos y una paridad distribuida | tres | la de todos menos uno | un disco |
| RAID 6 (doble paridad) | reparte los datos y dos paridades distintas | cuatro | la de todos menos dos | dos discos |
| RAID 10 (espejo repartido) | primero espeja y luego reparte | cuatro | la mitad | un disco de cada pareja |

Microsoft lo confirma para los volúmenes de Windows: **«Un volumen RAID-5 es un volumen tolerante a
errores en el que los datos y la paridad se seccionan en tres o más discos físicos.»** Por qué la paridad
simple pide tres discos: hacen falta al menos dos discos con datos para que la paridad
sirva de algo, más el espacio de la propia paridad. Con dos discos, la paridad de un solo dato es una
copia del dato, y eso ya tiene nombre y es el espejo.

Dos advertencias de oficio sobre la paridad:

- La reconstrucción es el momento peligroso. Mientras se reconstruye el disco sustituido, el conjunto lee
  todos los demás de cabo a rabo y está sin protección. Cuanto mayores son los discos, más dura esa
  ventana. Es el argumento de la doble paridad en conjuntos grandes.
- La escritura de una paridad obliga a leer antes. Modificar un trozo pequeño exige recalcular la
  paridad, lo que penaliza la escritura frente al espejo. Por eso el espejo sigue usándose donde manda la
  escritura y no la capacidad.

Y el conjunto que no es un conjunto: agrupar discos sin redundancia ninguna, sólo para verlos como un
volumen (JBOD). Sirve para capacidad bruta y no protege nada.

Aplicación práctica. Con cuatro discos de 4 TB: RAID 0 deja 16 TB sin protección; RAID 1 en parejas o
RAID 10, 8 TB; RAID 5, 12 TB y aguanta un disco; RAID 6, 8 TB y aguanta dos. Si se pide la máxima
capacidad útil con alguna redundancia, la respuesta es RAID 5; si se pide aguantar dos fallos
cualesquiera, RAID 6. La cuenta sale de la tabla anterior.

### En línea, casi en línea, fuera de línea

1. En línea: disco, disponible al instante. El material que se está tocando.
2. Casi en línea: disco lento o biblioteca de cintas con el robot montado. Minutos.
3. Fuera de línea: cinta en la estantería. Requiere que alguien la traiga.

Quien gobierna ese ciclo en una casa de televisión es la gestión de activos de medios (MAM): el catálogo
que sabe qué hay, dónde está cada copia y con qué derechos, y que ordena bajar a cinta lo que no se toca
y subir a disco lo que se va a necesitar.

## 5. Herramientas software de copia de seguridad

### Qué es una copia de seguridad

La copia de seguridad es un concepto distinto del almacenamiento, aunque se confundan. Una copia de
seguridad es una réplica de los datos destinada a recuperarlos si se pierden, y para valer tiene que
cumplir tres condiciones: estar separada del original, ser periódica y haberse probado la restauración.
Una copia que nunca se ha restaurado no se sabe si sirve.

| | Redundancia | Copia de seguridad | Archivo |
|---|---|---|---|
| De qué protege | Del fallo de un componente | Del borrado, la corrupción y el desastre | De nada: preserva |
| Qué contiene | Lo mismo que el original, ahora | El estado en varios momentos pasados | Lo que ya no está en producción y hay que conservar |
| Ejemplo | RAID, replicación | Copia diaria con retención | Fondo documental, obligación legal |

Y la frase que lo resume: el RAID no es una copia de seguridad. Si alguien borra un fichero, se borra a
la vez en los dos discos. La redundancia protege del disco que se rompe, no de la persona que se
equivoca ni del programa que cifra los ficheros.

### Las dos cifras que se fijan antes de elegir la herramienta

| Objetivo | Qué pregunta | Qué determina |
|---|---|---|
| Punto de recuperación | ¿Cuántos datos puedo permitirme perder? | Cada cuánto se copia |
| Tiempo de recuperación | ¿Cuánto puedo estar parado? | Cómo y desde dónde se restaura |

El ejemplo que lo hace concreto: un objetivo de punto de recuperación de veinticuatro horas admite una
copia diaria; uno de quince minutos exige replicación continua. Y un objetivo de tiempo de recuperación
de una semana admite recuperar de cinta; uno de una hora, no.

El error de método más frecuente: fijar la política mirando lo que la herramienta puede hacer. Se fija
al revés: primero se acuerda cuánto se puede perder y cuánto se puede estar parado, y después se elige la
herramienta que lo cumple.

### Los tipos de copia

| Tipo | Qué copia | Restaurar exige |
|---|---|---|
| Completa | Todo | Sólo la última completa |
| Diferencial | Lo cambiado desde la última completa | La completa y la última diferencial |
| Incremental | Lo cambiado desde la copia anterior, sea cual sea | La completa y todas las incrementales desde entonces |

La regla de elección: la incremental es la más barata de hacer y la más cara de restaurar; la completa,
al revés. Y como se copia todos los días y se restaura casi nunca, lo corriente es combinarlas.

Aplicación práctica. Completa el domingo y una copia cada noche de lunes a viernes; el disco falla el
jueves por la mañana. Si las diarias son diferenciales, se restaura la completa del domingo y la
diferencial del miércoles: dos juegos. Si son incrementales, la completa del domingo y las incrementales
del lunes, martes y miércoles, en ese orden: cuatro juegos. En ambos casos se pierde lo hecho desde la
última copia del miércoles por la noche, y eso es el punto de recuperación real de esa política.

### La regla 3-2-1 y lo que hoy se le añade

| Cifra | Qué exige |
|---|---|
| 3 | Tres copias de los datos: el original y dos más |
| 2 | En dos soportes distintos |
| 1 | Al menos una fuera del emplazamiento |

Y lo que la extorsión por cifrado ha obligado a añadir: al menos una copia inmutable o fuera de línea.
Una copia accesible desde la red con las mismas credenciales que el sistema copiado se cifra con él, y
entonces las tres copias son la misma copia.

INCIBE lo dice para el *ransomware* en su guía para empresas: **«la principal medida de seguridad que
va a permitirnos recuperar la actividad de nuestra empresa en poco tiempo, es realizar copias de
seguridad o backups»**, y recomienda: **«Haz y conserva al menos tres copias de seguridad actualizadas
y en distintos soportes.»**, por ejemplo **«disco duro específico para copias, USB externo y nube»**;
**«Guarda las copias de seguridad en un lugar diferente al del servidor de ficheros.»**; con copia en la
nube, **«algunas familias de ransomware también cifran y bloquean las copias de seguridad en la nube,
por lo que es conveniente desactivar la sincronización persistente.»**; y **«Comprueba regularmente que
las copias de seguridad que tienes almacenadas funcionan correctamente»**, **«para lo que hay que probar
a restaurar algunos ficheros cada cierto tiempo.»**

### La política y la prueba de restauración

Una política de conservación tiene cinco piezas, y la quinta es la que se olvida:

1. Qué se copia, con inventario: no se puede copiar lo que no se sabe que existe.
2. Cada cuánto, derivado del objetivo de punto de recuperación.
3. Dónde, con al menos un destino fuera del emplazamiento.
4. Cuánto se guarda, que es la retención, y cuándo se destruye.
5. Cada cuánto se PRUEBA la restauración.

El aviso, dicho sin adornos: una copia que no se ha restaurado nunca no se sabe si sirve. Los fallos
aparecen al restaurar —un soporte ilegible, una clave de cifrado perdida, una base de datos copiada en
caliente sin consistencia—, y aparecen el día del desastre si no se han buscado antes. La prueba de
restauración es la única parte de la política que demuestra que el resto funciona.

### La cinta

La cinta no ha desaparecido, por tres razones que hay que saber decir: cuesta menos por unidad de
capacidad que cualquier disco, se guarda sin consumir energía y el soporte se separa del lector, lo que
la convierte en una copia que un fallo del sistema no puede borrar mientras está fuera del lector.

Una biblioteca de cintas tiene tres piezas: los cartuchos, las unidades de lectura y escritura —los
lectores— y el brazo robótico que lleva un cartucho de su hueco al lector. La capacidad de la biblioteca
la dan los cartuchos; el caudal, el número de lectores. El sistema de ficheros de cinta lineal (LTFS)
presenta el cartucho como si fuera una carpeta, con nombres de fichero y directorios legibles sin la
aplicación que los escribió.

### Windows: Copias de seguridad de Windows

Es la herramienta del usuario en Windows 11 y Windows 10 (su página de soporte recuerda que el soporte de
Windows 10 finalizó el 14 de octubre de 2025). Microsoft la presenta como **«una solución de
copia de seguridad integral, Copias de seguridad de Windows, que le ayuda a realizar una copia de
seguridad de muchas de las cosas que son más importantes para usted. Desde los archivos, temas y
configuraciones hasta muchas de las aplicaciones instaladas e información Wi-Fi»**. Copia en la nube:
las carpetas Escritorio, Documentos, Imágenes, Vídeos y Música se sincronizan con OneDrive (la cuenta
gratuita **«incluye 5 GB de almacenamiento en la nube de OneDrive»**), y las preferencias y aplicaciones
instaladas quedan asociadas a la cuenta. Se abre buscando *backup* en Inicio o en Configuración >
Cuentas > Copias de seguridad de Windows.

La salvedad que importa en una empresa: **«Actualmente, la aplicación Copias de seguridad de Windows se
centra en dispositivos de consumidor, por ejemplo, dispositivos que se pueden usar iniciando sesión en
una cuenta personal de Microsoft (MSA) como *@outlook.com, *@live.com, etc. Las cuentas profesionales o
educativas de Microsoft no funcionarán.»** En un puesto unido al dominio, la copia la organiza el
departamento de sistemas con otras herramientas (oficio); la sincronización de OneDrive en el entorno
Microsoft 365 se estudia en el tema 11.

### Windows: wbadmin

`wbadmin start backup` (Microsoft Learn; vale para Windows 10 y 11 y Windows Server) **«Creates a
backup using specified parameters.»** Exige ser miembro de **«the Backup Operators group or the
Administrators group»**, o tener delegados los permisos adecuados, y ejecutarse desde un símbolo del
sistema elevado. Parámetros:

| Parámetro | Qué hace |
|---|---|
| `-backupTarget:` | Destino: letra de disco, volumen o carpeta compartida UNC; en red, por defecto se guarda en la carpeta `\\<servername>\<sharename>\WindowsImageBackup\<ComputerBackedUp>\` |
| `-include:` | Lista, separada por comas, de ficheros, carpetas o volúmenes que se copian; sólo junto con `-backupTarget` |
| `-allCritical` | Incluye todos los volúmenes críticos, los que contienen el estado del sistema operativo: **«This parameter is useful if you're creating a backup for bare metal recovery.»** (recuperación sobre equipo desnudo). Sólo con `-backupTarget`; si no, la orden falla |
| `-systemState` | Añade el estado del sistema |
| `-vssFull` | Copia completa con VSS que marca los ficheros como copiados |
| `-vssCopy` | Copia de VSS que no toca el historial de los ficheros: **«This is the default value.»** Una copia así no sirve de base para copias incrementales o diferenciales |
| `-quiet` | **«Runs the command without prompts to the user.»** |

Ejemplo construido con esa sintaxis: `wbadmin start backup -backupTarget:f: -include:e: -quiet` copia el
volumen E: en el volumen F: sin pedir confirmación. Una advertencia de la página: repetir la copia del
mismo equipo en la misma carpeta compartida sobrescribe la anterior, y si la nueva falla puede quedarse
sin ninguna; por eso recomienda subcarpetas.

### Windows: robocopy

`robocopy` **«Copies file data from one location to another.»** Es la orden para copiar carpetas
enteras de forma fiable, en local o a una carpeta de red:

| Opción | Qué hace (Microsoft Learn) |
|---|---|
| `/s` | **«Copies subdirectories. This option automatically excludes empty directories.»** |
| `/e` | **«Copies subdirectories. This option automatically includes empty directories.»** |
| `/z` | **«Copies files in restartable mode.»** Si se corta, sigue donde lo dejó |
| `/b` | **«Copies files in backup mode. In backup mode, robocopy overrides file and folder permission settings (ACLs), which might otherwise block access.»** |
| `/mir` | **«Mirrors a directory tree (equivalent to /e plus /purge).»** |
| `/purge` | **«Deletes destination files and directories that no longer exist in the source.»** |
| `/r:<n>` y `/w:<n>` | Número de reintentos (por defecto, un millón) y espera entre ellos en segundos (por defecto, 30) |
| `/log:<fichero>` | Escribe el resultado en un registro, sobrescribiendo el que hubiera (`/log+:` añade al existente) |

Ejemplo literal de la página, una réplica con dos reintentos, cinco segundos de espera y registro:
`robocopy C:\Users\Admin\Records D:\Backup /MIR /R:2 /W:5 /LOG:C:\Logs\Backup.log`. Y la lectura del
resultado: **«Any value equal to or greater than 8 indicates that there was at least one failure during
the copy operation.»** (un código de salida de 8 o más indica al menos un fallo).

La advertencia de oficio: `/mir` hace que el destino sea igual al origen, también en lo borrado. Si en
el origen se borra un fichero por error, o lo cifra un *ransomware*, la siguiente réplica lo borra o lo
sobrescribe en el destino. Una réplica no es una copia con historia.

### Windows: las instantáneas (VSS)

El servicio de instantáneas de volumen guarda versiones anteriores de los ficheros de un volumen;
`wbadmin` se apoya en él (sus parámetros `-vssFull` y `-vssCopy`). `vssadmin` **«Shows current volume shadow copy backups and all installed
shadow copy writers and providers.»**; `vssadmin list shadows` **«Lists existing volume shadow
copies.»**; `vssadmin delete shadows` **«Deletes volume shadow copies.»** Como se guardan en el propio equipo,
no sustituyen a la copia: si el equipo se pierde, se pierden con él (oficio). Los puntos de restauración de Windows 11, que
son instantáneas del sistema, se estudian en el tema 6.

### Linux: rsync y tar

`rsync` (página de manual): **«Rsync is a fast and extraordinarily versatile file copying tool. It can
copy locally, to/from another host over a remote shell, or to/from a remote rsync daemon.»** Su rasgo:
**«It is famous for its delta-transfer algorithm, which reduces the amount of data sent over the network
by sending only the differences between the source files and the existing files in the destination.
Rsync is widely used for backups and mirroring»**. Opciones básicas: `-a` (modo archivo, **«archive
mode is -rlptgoD»**: recursivo y conservando enlaces simbólicos, permisos, fechas de modificación, grupo, propietario,
dispositivos y ficheros especiales; no conserva las ACL, los atributos extendidos ni los enlaces duros), `-v` (detalle), `-z` (comprime durante la transferencia), `-n` (**«perform a trial run
with no changes made»**: ensayo sin cambios) y `--delete` (**«delete extraneous files from dest
directories»**, el equivalente del `/mir` de `robocopy`, con el mismo riesgo). Ejemplo del manual:
`rsync -avz foo:src/bar /data/tmp`; con barra final en el origen (`src/bar/`) se copia el contenido de
la carpeta y no la carpeta.

`tar` agrupa ficheros en un archivo y, con la opción de compresión, lo comprime (§ 6): es la forma
clásica de la copia completa en Linux. La salvaguarda y restauración en Linux se desarrolla en el tema
9.

## 6. Herramientas software de compresión de datos

### Sin pérdida y con pérdida

Comprimir es reducir el tamaño de los datos. Hay dos familias: la compresión sin pérdida, que comprime y
devuelve el original bit a bit, y la compresión con pérdida, que descarta lo que el oído o la vista no
van a notar y no lo devuelve (la propia de los formatos de audio, imagen y vídeo). Los ficheros de
oficina, los programas y las copias de seguridad se comprimen siempre sin pérdida: un documento al que
le falta un bit puede no abrirse. Todas las herramientas de este epígrafe son sin pérdida.

Dos ideas que se preguntan (oficio, con apoyo en el manual de `gzip` en la segunda): comprimir y
archivar no son lo mismo —`tar` junta muchos ficheros en uno sin comprimirlos; `gzip` comprime un
fichero sin juntarlos; ZIP y 7z hacen las dos cosas—; y no todo comprime igual: **«The amount of
compression obtained depends on the size of the input and the distribution of common substrings.
Typically, text such as source code or English is reduced by 60–70%.»** Lo que ya está comprimido
(vídeo, fotos JPEG, otro ZIP) apenas gana —Microsoft lo dice de las JPEG: **«already highly
compressed»**—, y en el peor caso `gzip` declara **«an expansion ratio of
0.015% for large files»**.

### gzip y tar

`gzip` (manual de GNU): **«gzip reduces the size of the named files using Lempel–Ziv coding (LZ77).»**;
**«gzip uses the Lempel–Ziv algorithm used in zip and PKZIP.»** Siempre que es posible, cada fichero se
sustituye por otro con extensión `.gz`. Opciones: `-d` descomprime, `-k` conserva el original, `-l` lista, `-r` recorre
carpetas, `-1` (**«compress faster»**) a `-9` (**«compress better»**).

`tar` (GNU) crea y lee archivos comprimidos con **«gzip, bzip2, lzip, lzma, lzop, zstd, xz and
traditional compress»**; se elige con una opción: `-z` para gzip, `-j` para bzip2, `-J` para xz. Ejemplo
del manual: `tar czf archive.tar.gz .` crea, y `tar xf archive.tar.gz` extrae (al leer, `tar` reconoce
el formato solo). Es la combinación habitual de la copia completa de una carpeta en Linux.

### 7-Zip

**«7-Zip is a file archiver with a high compression ratio.»** Su formato propio es 7z: **«High
compression ratio in 7z format with LZMA and LZMA2 compression»**. Formatos: **«Packing / unpacking:
7z, XZ, BZIP2, GZIP, TAR, ZIP and WIM»**; otros muchos, entre ellos RAR, sólo los descomprime. Cifra:
**«Strong AES-256 encryption in 7z and ZIP formats»**. En ZIP y GZIP, **«7-Zip provides a compression
ratio that is 2-10 % better than the ratio provided by PKZip and WinZip»**. Licencia: **«The most of the
code is under the GNU LGPL license.»** (algunas partes, con licencia BSD de tres cláusulas, y otras con la
restricción de la licencia unRAR), y **«You can use 7-Zip on any computer, including a computer in
a commercial organization.»** Versión a la fecha de este tema: **«7-Zip 26.03 (2026-09-03)»**.

### Lo que trae Windows 11

- El Explorador: **«Windows 11, version 24H2 supports ZIP, RAR. 7z and TAR archive formats.»**, con una
  salvedad: **«it does not support operations on encrypted archive files.»** Para comprimir: **«Right-click
  (or press and hold) the file or folder, select Show more options > Send to > Compressed (zipped)
  folder.»**; para extraer, clic derecho y **«Extract All...»**. Un ZIP cifrado se abre con 7-Zip.
- `tar` en la línea de órdenes: **«tar is a command-line archiving tool that's included with Windows. It
  lets you create, list, and extract archive files — including .tar, .tar.gz, .zip, and .7z — directly
  from the command line, without installing additional software.»**; está **«based on libarchive's
  bsdtar»**. Ejemplos de la página: `tar -czf archive.tar.gz .\my-folder` (crear) y `tar -xf
  archive.tar.gz` (extraer).
- La compresión de NTFS: `compact` **«Displays or alters the compression
  of files or directories on NTFS partitions.»** `/c` comprime y `/u` descomprime; `/EXE` usa una
  compresión pensada para ejecutables que se leen mucho y no cambian, con los algoritmos **«XPRESS4K
  (fastest and default value)»**, XPRESS8K, XPRESS16K y **«LZX (most compact)»**.

## 7. Herramientas software de clonación de discos

### Clonar o hacer imagen

Clonar es copiar un disco o una partición entera, sector a sector o bloque a bloque, a otro disco; hacer
imagen es volcar esa misma copia a un fichero, del que luego se restaura. Sirve para tres cosas en el
puesto: cambiar un disco por otro mayor o por una SSD sin reinstalar, desplegar el mismo sistema en
muchos equipos iguales y guardar el estado completo de un equipo antes de tocarlo (oficio). A diferencia
de la copia de ficheros, la clonación se lleva también el sector de arranque y la tabla de particiones.

### Clonezilla

**«Clonezilla is a partition and disk imaging/cloning program similar to True Image® or Norton Ghost®.
It helps you to do system deployment, bare metal backup and recovery.»** Tres variantes: **«Clonezilla
live, Clonezilla lite server, and Clonezilla SE (server edition). Clonezilla live is suitable for single
machine backup and restore.»**; las otras dos, para despliegue masivo.

| Rasgo | Lo que dice Clonezilla |
|---|---|
| Qué copia | **«Clonezilla saves and restores only used blocks in the hard disk.»** Para sistemas de ficheros que no reconoce, **«sector-to-sector copy is done by dd»** |
| Particiones y arranque | **«Both MBR and GPT partition formats of hard drive are supported. Clonezilla live also can be booted on a BIOS or uEFI machine.»** |
| Cifrado | **«AES-256 encryption could be used»** |
| Despliegue masivo | **«Multicast is supported in Clonezilla SE»**; **«Bittorrent (BT) is supported in Clonezilla lite server»** |
| Equipos Windows clonados | Con drbl-winroll, **«the hostname, group, and SID of cloned MS windows machine can be automatically changed.»** |
| Límites | **«The destination partition must be equal or larger than the source one.»**; **«Differential/incremental backup is not implemented yet.»**; **«The partition to be imaged or cloned has to be unmounted.»**; y de la imagen **«You can _NOT_ recovery single file»** (no se recupera un fichero suelto, salvo con un procedimiento alternativo) |

Lo último decide un caso práctico: para pasar de un disco de 1 TB con 300 GB ocupados a una SSD de 500 GB no
basta clonar tal cual; antes hay que reducir la partición de origen para que quepa (oficio). Y lo
penúltimo explica por qué, al desplegar muchos equipos Windows desde una misma imagen, hay que cambiar
nombre y SID: si no, todos se llamarían igual en la red (oficio).

### dd

`dd` (GNU Coreutils): **«dd copies input to output with a changeable I/O block size, while optionally
performing conversions on the data.»** Copia a bajo nivel cualquier cosa que Linux vea como fichero,
discos y particiones incluidos (`/dev/sda`, `/dev/sda1`). Se escribe con cuidado: confundir la entrada
con la salida sobrescribe el disco que se quería salvar (oficio).

### Rescatar un disco que falla

Para un disco que da errores de lectura, la regla es sacar primero una imagen y trabajar sobre ella, no
sobre el disco enfermo (oficio, que INCIBE aplica al *ransomware* en el § 8). El manual de `dd` da el
método sencillo: **«the operand ‘conv=noerror,sync’ is used to continue after read errors and to pad out
bad reads with NULs»** (sigue tras los errores de lectura y rellena con ceros lo que no pudo leer), con
este ejemplo: `dd conv=noerror,sync iflag=fullblock </dev/sda1 > /mnt/rescue.img`, **«Rescue data from
an (unmounted!) partition of a failing device.»** —la partición, sin montar—. Y remite a algo mejor:
**«For failing storage devices, other tools come with a great variety of extra functionality to ease the
saving of as much data as possible before the device finally dies, e.g. GNU ddrescue.»**

## 8. Recuperación de datos en caso de borrado accidental, avería o ataque de virus

### Borrado accidental: por qué se puede

Borrar un fichero no borra sus datos. PhotoRec lo explica: **«When a file is deleted, the
meta-information about this file (file name, date/time, size, location of the first data block/cluster,
etc.) is lost»** … **«This means the data is still present on the file system, but only until some or
all of it is overwritten by new file data.»** Microsoft dice lo mismo de Windows: **«el espacio usado
por un archivo eliminado se marca como espacio libre, lo que significa que los datos del archivo aún
pueden existir y recuperarse. Sin embargo, cualquier uso de su equipo puede crear archivos, lo que puede
sobrescribir este espacio libre en cualquier momento.»**

De ahí la regla de oro, con las palabras de PhotoRec: **«As soon as a picture or file is accidentally
deleted, or you discover any missing, do NOT save any more pictures or files to that memory device or
hard disk drive; otherwise you may overwrite your lost data. This means that while using PhotoRec, you
must not choose to write the recovered files to the same partition they were stored on.»** Y las de
Microsoft: **«Si quieres aumentar las posibilidades de recuperar un archivo, minimiza o evita usar el
equipo.»** Lo recuperado se guarda siempre en otra unidad.

### Borrado accidental: el orden en que se busca

1. La Papelera de reciclaje, si el borrado fue desde el Explorador.
2. La copia de seguridad (§ 5) o la versión anterior que guarde la instantánea o la nube.
3. Si nada de eso existe, una herramienta de recuperación sobre el disco.

El orden es de oficio; Microsoft lo da implícito al presentar su herramienta: **«Si no puedes encontrar
un archivo perdido en la copia de seguridad, puedes usar Windows File Recovery»**, para los ficheros
**«que se han eliminado del dispositivo de almacenamiento local (incluidas las unidades internas,
unidades externas y dispositivos USB) y no se puede restaurar desde la Papelera de reciclaje.»** Y
añade: **«No se admite la recuperación en recursos compartidos de archivos y almacenamiento en la
nube.»**

### Recuperación de archivos de Windows (winfr)

Es una aplicación de línea de órdenes de Microsoft Store para Windows 11 y 10. Sintaxis: **«winfr
source-drive: destination-drive: [/mode] [/switches]»**. Las unidades de origen y destino tienen que ser
distintas, y al abrirla pide permiso para hacer cambios en el dispositivo.

| Modo | Para qué (Microsoft) |
|---|---|
| `/regular` | **«Modo normal, la opción de recuperación estándar para unidades NTFS no dañadas»** |
| `/extensive` | **«Modo extensivo, una opción de recuperación exhaustiva adecuada para todos los sistemas de archivos»** |

| Sistema de archivos | Circunstancias | Modo recomendado |
|---|---|---|
| NTFS | Eliminado recientemente | Normal |
| NTFS | Eliminado hace un tiempo | Extenso |
| NTFS | Después de dar formato a un disco | Extenso |
| NTFS | Un disco dañado | Extenso |
| FAT y exFAT | Cualquiera | Extenso |

(La tabla de la página llama a los modos **«Regular»** y **«Amplia»**; el texto, normal y extenso.)

**«La recuperación de archivos desde sistemas de archivos que no sean NTFS solo es compatible con el modo
extensivo.»** Y **«Si no está seguro, empiece con el modo Normal.»** El filtro `/n` busca por nombre,
ruta, tipo o comodín. Ejemplos de la página: `Winfr C: E: /regular /n \Users\<username>\Documents\`
(recupera la carpeta Documentos de C: en E:) y `Winfr C: E: /regular /n *.pdf /n *.docx` (PDF y Word).
El resultado va a una carpeta **«Recovery_<date and time>»** de la unidad de destino.

### PhotoRec y TestDisk

Dos programas libres de CGSecurity (licencia GPL v2 o posterior) que se complementan:

- PhotoRec recupera ficheros: **«PhotoRec ignores the file system and goes after the underlying
  data, so it will still work even if your media's file system has been severely damaged or
  reformatted.»**; **«PhotoRec searches for known file headers.»**, y recupera el fichero entero **«If there is no data
fragmentation»**; reconoce **«more than 480 file
  extensions»**; y trabaja sin tocar el soporte: **«PhotoRec uses read-only access»**.
- TestDisk recupera particiones: **«It was primarily designed to help recover lost partitions and/or
  make non-booting disks bootable again when these symptoms are caused by faulty software: certain types
  of viruses or human error (such as accidentally deleting a Partition Table).»** También permite
  **«Undelete files from FAT, exFAT, NTFS and ext2 filesystem»**.

Un apunte sobre las SSD: el aviso de borrado (TRIM, § 3) dice a la unidad qué bloques quedan libres. Las
fuentes leídas no afirman que TRIM impida recuperar lo borrado, y el tema no lo afirma; lo que sí dice
Microsoft, para cuando `winfr` no encuentra el fichero, es que **«Es posible que el espacio libre se
sobrescriba, especialmente en una unidad de estado sólido (SSD).»** En una SSD hay que actuar aún más
rápido y sin escribir en ella.

### Avería

Depende de dónde esté la avería:

- Lógica (tabla de particiones dañada, sistema de ficheros corrupto, disco que no arranca): TestDisk
  para la partición, `chkdsk` para el sistema de ficheros (tema 2), PhotoRec o `winfr` en modo extenso
  para los ficheros.
- Física, con el disco aún legible: no se reparan ni se escanean los datos sobre él; se saca imagen
  con `dd conv=noerror,sync` o GNU ddrescue a otro disco (§ 7) y se recupera desde la imagen. Cada hora
  de uso de un disco que falla puede ser la última (oficio).
- En un RAID: se sustituye el disco averiado y el conjunto se reconstruye; es el momento peligroso
  (§ 4), por lo que conviene tener la copia al día antes de empezar.
- Lo que no lee ningún equipo se deja en manos de un servicio especializado; el tema no da fuente sobre
  esos laboratorios.

### Ataque de virus: el ransomware

El *ransomware* (el malware que cifra los datos y pide un rescate; los tipos de malware y el antivirus
están en el tema 14) es el caso en que la recuperación se juega en las copias. INCIBE resume el primer
gesto: **«lo primero es apagar el equipo afectado para que no se extienda a otros dispositivos de la red
interna»**, y dos reglas: **«No pagar nunca el rescate, ya que esto no garantiza que puedas recuperar la
información ni que no vuelvan a exigirte un segundo rescate.»**, y aplicar el plan de respuesta ante
incidentes si lo hay; si no lo hay, recuperar la información con la última copia de seguridad. No More Ransom dice lo mismo: **«La recomendación general es no pagar el
rescate.»**

Las etapas de INCIBE (ilustración 5 de su guía): **AÍSLA**, **CLONA**, **DESINFECTA**, **INTENTA
RECUPERAR**, **RESTAURA**. En el texto de la guía son cuatro pasos numerados: las dos últimas etapas son
los apartados A) y B) del paso 4, «Recupera y restaura los equipos».

1. Aislar. **«Aísla el equipo de la red: esto evitará que el ciberataque se propague a otros
   dispositivos.»** Se sospecha también de los discos, unidades de red y servicios en la nube que
   estuvieran conectados. **«Cambia inmediatamente todas las contraseñas de red y de cuentas online.»**
2. Clonar. **«Clona el disco duro: se recomienda realizar una clonación completa del disco. De esta
   manera, podrás mantener el dispositivo original y así intentar recuperar los datos sobre el clon. Si
   no existiera solución a día de hoy, es posible que en el futuro sí la haya»**. Como solución en caso de que
   no exista denuncia, se conecta el disco a otro ordenador aislado de la red y preparado para pruebas: **«no arranques con él, utilízalo de «esclavo»»**, y se salvan
   **«solo los datos importantes (documentos, fotos, certificados…) y no archivos ejecutables o
   programas que puedan volver a infectar de nuevo al equipo.»** Se denuncia (Guardia Civil, Grupo de
   Delitos Telemáticos; Policía Nacional, Brigada de Investigación Tecnológica).
3. Desinfectar. **«Desinfecta el disco clonado»** con un antivirus o antimalware actualizado: **«Es muy
   importante eliminar el software malicioso y sus posibles persistencias antes de recuperar los datos,
   ya que si no se hace, podrían volver a ser cifrados.»**
4. Intentar recuperar. En **«www.nomoreransom.org»**, **«un proyecto colaborativo avalado por la
   EUROPOL»**, la sección **«Crypto-sheriff»** identifica la variante con **«dos ficheros cifrados o la
   nota de rescate»** y, si hay solución, da la herramienta para descifrar. Si no la hay, **«conserva el
   disco cifrado por si apareciera una solución en el futuro.»** (No More Ransom: **«Por el momento, no
   todos los tipos de ransomware tienen solución.»**)
5. Restaurar. **«Revisa si el sistema de ficheros del sistema operativo cuenta con shadow copy o
   snapshot, que mantienen copias de versiones anteriores de ficheros.»** Y al final: **«utiliza un disco
   nuevo o formateado, además de una instalación en limpio del sistema operativo, y restaura la copia de
   seguridad más reciente anterior a la infección.»**

Prevenir en el puesto: además de las copias fuera de línea, Windows ofrece el Acceso controlado a
carpetas de Microsoft Defender: **«Controlled folder access (CFA) in Microsoft Defender Antivirus helps
protect your files from ransomware threats.»** **«CFA counters this threat by allowing only trusted apps
to change files in protected folders.»** Viene desactivado: **«CFA is turned off by default.»** Una vez activado, protege una lista fija de
carpetas, entre ellas la carpeta Documentos del usuario, y se pueden añadir otras.

### Aplicación práctica: tres casos del puesto

- Una usuaria borró ayer, con Mayús+Supr, una carpeta de su escritorio en un equipo con Windows 11 y
  disco NTFS; no hay copia. Se le pide que deje de usar el equipo; se instala Recuperación de archivos
  de Windows y se lanza el modo normal (NTFS, borrado reciente) hacia una memoria USB:
  `winfr C: E: /regular /n \Users\<username>\Desktop\`. Si no aparece, modo extenso. (Mayús+Supr borra
  sin pasar por la Papelera: oficio.)
- Una tarjeta SD de 64 GB de una cámara, formateada por error. Es SDXC, luego exFAT: `winfr` sólo en modo
  extenso, o PhotoRec, que no depende del sistema de ficheros; en ambos casos, guardando en otro disco.
- Un equipo muestra una nota de rescate y los ficheros con otra extensión. Se apaga y se aísla de la red;
  se avisa a sistemas; se clona el disco; se desinfecta el clon; se consulta Crypto-sheriff con dos
  ficheros cifrados; se restaura sobre un disco nuevo, con instalación limpia, la última copia anterior a
  la infección. No se paga.

## Lo que este tema no da, y dónde está

- Los tipos de celda flash (SLC, MLC, TLC, QLC) y sus ciclos de programación y borrado: sólo constan en
  fuentes secundarias; no se dan. Tampoco la velocidad mínima en MB/s de cada clase de velocidad SD (la
  SD Association la da en imagen, no en texto).
- Que TRIM impida recuperar los datos borrados de una SSD: ninguna fuente leída lo dice (Microsoft sólo
  advierte que en una SSD el espacio libre se sobrescribe con más facilidad).
- Historial de archivos, «Copias de seguridad y restauración (Windows 7)» y «Versiones anteriores» del
  Explorador en Windows 11: no se han leído sus páginas.
- Capacidades y velocidades de las generaciones LTO, caudales, IOPS y tiempos de reconstrucción de RAID:
  dato de fabricante, no leído.
- Laboratorios de recuperación de discos con avería física: sin fuente.
- La notificación de una brecha de datos personales tras un *ransomware* es del Reglamento General de
  Protección de Datos, que se estudia en el temario común; la Línea de Ayuda en Ciberseguridad de INCIBE
  se cita en la guía sin número de teléfono, y el tema no lo da.
- Diagnóstico de discos con SMART y `chkdsk`: tema 2. USB y sus velocidades: tema 4. Puntos de
  restauración, recuperación del sistema y gestión de discos de Windows 11: tema 6. Salvaguarda y
  restauración en Linux: tema 9. OneDrive y SharePoint: tema 11. Malware y antivirus: tema 14.
- Qué sistemas de almacenamiento, copia y recuperación usa la RTVA o CSRTV: no consta en ningún
  documento publicado.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| SNIA, *Online Dictionary*: «flash memory», «Solid State Storage», «wear leveling», «trim», «write amplification», «garbage collection», «over provisioning», «Storage Area Network»; página «What is Network Attached Storage (NAS)?» | Definiciones de flash, estado sólido, nivelación de desgaste, TRIM, amplificación de escritura, recolección de basura, sobreaprovisionamiento, SAN y NAS | 05-10-2026 |
| Microsoft Learn, «fsutil behavior» | TRIM como aviso de borrado, activo por defecto en NTFS, `disabledeletenotify` | 05-10-2026 |
| NVM Express, páginas «About» y «Specifications» | NVMe como interfaz de las SSD PCIe, transportes, formatos, versión 2.4 de 4-8-2026 | 05-10-2026 |
| SD Association, «Capacity (SD/SDHC/SDXC/SDUC)» y «Speed Class» | Capacidades y sistema de ficheros de cada clase; clases de velocidad, UHS, vídeo y SD Express; fundación | 05-10-2026 |
| Soporte de Microsoft, «Realizar copias de seguridad y restaurar con Copias de seguridad de Windows» (es-es) | Qué copia, OneDrive con 5 GB, ruta, salvedad de las cuentas profesionales | 05-10-2026 |
| Microsoft Learn (es-es), «Cómo usar el complemento de administración de discos para administrar discos básicos y dinámicos» (actualizada el 12-2-2026) | RAID-5 con tres o más discos | 05-10-2026 |
| Microsoft Learn, «wbadmin start backup» (actualizada el 3-2-2023) | Sintaxis, grupos, destino por defecto, `-include`, `-allCritical`, `-vssFull`, `-vssCopy`, `-quiet`, sobrescritura en la carpeta compartida | 05-10-2026 |
| Microsoft Learn, «robocopy» (actualizada el 17-3-2025) | Opciones `/s`, `/e`, `/z`, `/b`, `/mir`, `/purge`, `/r`, `/w`, `/log`, ejemplo y códigos de salida | 05-10-2026 |
| Microsoft Learn, «vssadmin» (actualizada el 8-9-2026) | Órdenes de instantáneas | 05-10-2026 |
| Página de manual `rsync(1)` (samba.org) | Descripción, algoritmo delta, `-a` y lo que no incluye, `-n`, `--delete`, ejemplo y barra final | 05-10-2026 |
| GNU gzip, manual; GNU tar, «Creating and Reading Compressed Archives» | LZ77, 60-70 %, peor caso, opciones; programas y opciones de compresión de `tar`, ejemplos | 05-10-2026 |
| 7-Zip, página principal | Definición, LZMA/LZMA2, formatos, AES-256, mejora sobre PKZip y WinZip, LGPL, uso en empresa, versión 26.03 | 05-10-2026 |
| Soporte de Microsoft, «Zip and unzip files» (en-us) | Formatos que admite Windows 11 24H2, archivos cifrados, pasos, JPEG ya comprimidas | 05-10-2026 |
| Microsoft Learn, «tar on Windows» (actualizada el 2-6-2026); «compact» (3-2-2023) | `tar` incluido y basado en bsdtar; compresión NTFS y algoritmos | 05-10-2026 |
| Clonezilla, página principal | Definición, variantes, bloques usados, dd, MBR/GPT, BIOS/UEFI, AES-256, multicast y BitTorrent, drbl-winroll, límites (destino igual o mayor, sin copias diferenciales ni incrementales, partición desmontada, sin ficheros sueltos) | 05-10-2026 |
| GNU Coreutils, «dd invocation» | Definición, `conv=noerror,sync`, ejemplo de rescate, GNU ddrescue | 05-10-2026 |
| CGSecurity, «PhotoRec» y «TestDisk» | Por qué se recupera lo borrado, regla de no escribir, funcionamiento de PhotoRec y fragmentación, finalidad de TestDisk | 05-10-2026 |
| Soporte de Microsoft, «Recuperación de archivos de Windows» (es-es) | Minimizar el uso, espacio libre, cuándo usarla, sintaxis, modos, tabla de decisión, ejemplos, sobrescritura del espacio libre en SSD | 05-10-2026 |
| INCIBE, *Ransomware. Una guía de aproximación para el empresario* (2020, v2), § 3.2.1 y § 4 | Recomendaciones de copia, apagar, no pagar, las cinco etapas, No More Ransom, shadow copy, restauración en limpio, denuncia (y su condición), pasos numerados frente a etapas | 05-10-2026 |
| No More Ransom, portada en español | No todos tienen solución; no pagar | 05-10-2026 |
| Microsoft Learn, «Controlled folder access» (actualizada el 17-7-2026) | Acceso controlado a carpetas, desactivado por defecto | 05-10-2026 |

Las fuentes en inglés se citan en negrita en su lengua, con la explicación en castellano en redonda.

Oficio sin fuente detrás, y así se declara: las unidades y el ejemplo de cálculo; la tabla de soportes y
la de ubicaciones; la diferencia de tiempo de acceso entre HDD y SSD y las magnitudes de caudal y
operaciones por segundo; la tabla de interfaces SATA, SAS y NVMe con su idea; la consolidación y la
tabla DAS, NAS y SAN; la frontera entre ficheros y bloques con sus consecuencias, la regla de los
protocolos y la descripción de FC, iSCSI, NFS, SMB y del almacenamiento por objetos; la tabla de niveles
RAID, la razón de los tres discos, las advertencias sobre la paridad, el JBOD y la cuenta con cuatro
discos; la jerarquía en línea, casi en línea y fuera de línea y el MAM; las tres condiciones de una copia
de seguridad, la tabla redundancia-copia-archivo, RPO y RTO, los tipos de copia, la regla 3-2-1 con la
copia inmutable, las cinco piezas de la política y la prueba de restauración; las razones de la cinta,
la biblioteca y LTFS; la advertencia sobre `/mir` y `--delete`; que las instantáneas no sustituyen a la copia; la distinción entre compresión con y sin
pérdida y entre comprimir y archivar; la definición de clonar y hacer imagen y sus usos; el orden de
búsqueda tras un borrado; la regla de trabajar sobre la imagen de un disco que falla; y los tres casos
prácticos.
