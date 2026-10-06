# Tema 2 del específico de Operador/a Informático · Diagnóstico, mantenimiento y reparación de equipos microinformáticos

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 2 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Documentación de fabricante: American Megatrends, *AMIBIOS8 Check Point and Beep Code List* 2.0 (2008); HP, *Interactive Beep and LED Diagnostic* y *Maintenance and Service Guide HP ProDesk 600 G5 SFF* (3.ª ed., 2019); Lenovo, *M920s User Guide and Hardware Maintenance Manual* (2.ª ed., 2019). Microsoft Learn y Microsoft Support (chkdsk, sfc, ipconfig, ping, PnPUtil, códigos del Administrador de dispositivos, TDR, winsat mem, errores de detención y volcados de memoria; Diagnóstico de memoria de Windows, en TechNet Magazine archivado). NVM Express, *NVM Express Base Specification* 2.1 (2024). Manual de `smartctl` (smartmontools). PassMark (MemTest86, PerformanceTest). Universidad Complutense de Madrid, *Estructura de Computadores*, tema 4. SPEC, Maxon, UL y Crystal Dew World. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las ediciones citadas, en línea el 05-10-2026 o el 06-10-2026 y leídas el día que se indica en «Trazabilidad» |
| Extensión | 13.900 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); sistema básico de entrada y
salida (BIOS, *basic input/output system*) y su sucesora, la interfaz de firmware extensible unificada
(UEFI, *unified extensible firmware interface*); autoprueba de encendido (POST, *power-on self test*);
memoria de configuración alimentada por pila (CMOS, por la tecnología *complementary
metal-oxide-semiconductor* con que se fabricaba); reloj de tiempo real (RTC, *real-time clock*); unidad
central de proceso (CPU, *central processing unit*); unidad de procesamiento gráfico (GPU, *graphics
processing unit*); memoria de acceso aleatorio (RAM, *random-access memory*); módulo de memoria de
doble línea de contactos (DIMM, *dual in-line memory module*); memoria con código de corrección de
errores (ECC, *error-correcting code*); acceso directo a memoria (DMA, *direct memory access*); perfil de
memoria extremo (XMP, *extreme memory profile*), perfil de sobrevelocidad de los módulos; disco duro
(HDD, *hard disk drive*) y unidad de estado sólido (SSD, *solid-state drive*); NVMe (*NVM Express*),
interfaz de las SSD sobre el bus PCI Express (PCIe); las familias de interfaz de disco ATA y SATA
(*Serial ATA*), SCSI y SAS (*Serial Attached SCSI*); la tecnología de autosupervisión, análisis e
informe de los discos (SMART, *self-monitoring, analysis and reporting technology*); bloque de
direcciones lógicas (LBA, *logical block address*); sistemas de ficheros NTFS (*New Technology File
System*) y FAT, FAT32 y exFAT (*file allocation table* y su variante extendida); tarjeta de interfaz de
red (NIC, *network interface card*); red de área local (LAN, *local area network*) e inalámbrica (Wi-Fi);
protocolo de control de transmisión e Internet (TCP/IP); protocolo de configuración dinámica de
equipos (DHCP, *dynamic host configuration protocol*); sistema de nombres de dominio (DNS, *domain name
system*); protocolo de mensajes de control de Internet (ICMP, *Internet control message protocol*);
direccionamiento IP privado automático (APIPA, *automatic private IP addressing*); conexión y uso,
*Plug and Play* (PnP); modelo de controladores de pantalla de Windows (WDDM, *Windows display driver
model*); detección y recuperación de tiempo de espera (TDR, *timeout detection and recovery*); unidad
reemplazable en campo (FRU, *field replaceable unit*) y reemplazable por el cliente (CRU, *customer
replaceable unit*); descarga electrostática (ESD, *electrostatic discharge*); millones de
instrucciones por segundo (MIPS) y millones de operaciones en coma flotante por segundo (MFLOPS);
la Standard Performance Evaluation Corporation (SPEC), que la fuente universitaria desarrolla como
«System Performance and Evaluation Cooperative», y el Transaction Processing Performance Council
(TPC), consorcios que publican pruebas de rendimiento; operaciones de entrada y salida por segundo
(IOPS, *input/output operations per second*); entrada y salida (E/S, en inglés I/O); sistema operativo
(SO, en inglés OS); ordenador personal (PC, *personal computer*); memoria de solo lectura (ROM,
*read-only memory*) y su variante programable y borrable (EPROM, *erasable programmable read-only
memory*); diodo emisor de luz (LED, *light-emitting diode*); los buses de expansión ISA (*Industry
Standard Architecture*) y PCI (*Peripheral Component Interconnect*), antecesores de PCIe; protocolo de
Internet (IP) en sus versiones 4 y 6 (IPv4, IPv6); lenguaje de marcas extensible (XML, *extensible
markup language*); megabyte (MB) y kilobyte (kB); corriente alterna (AC, *alternating current*); comprobación de redundancia cíclica (CRC, *cyclic
redundancy check*); pantalla azul de Windows, que Microsoft llama error de detención o comprobación de
errores (*stop error*, *bug check*) y también por su sigla inglesa, BSOD. BAT es el nombre de la prueba del controlador de teclado en la
fuente de American Megatrends, que no desarrolla la sigla; DXE (zona principal de la BIOS) y MXM (un módulo cuya
temperatura vigila la placa) son nombres que la guía de HP usa sin desarrollar, y 5V_aux es el rótulo
de un piloto de su placa. Fabricantes y editores que se citan por su nombre
comercial: American Megatrends (AMI), HP, Lenovo, PassMark, Maxon, UL (editor de 3DMark), Crystal
Dew World y NVM Express, la organización que publica la especificación NVMe. VALUE, WORST, THRESH, TYPE y WHEN_FAILED son rótulos de columna que imprime `smartctl`.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 2): «Diagnóstico, mantenimiento
> y reparación de equipos microinformáticos: principales averías, mensajes de error de la BIOS,
> sustitución y detección de averías en discos duros, memorias, tarjetas gráficas y tarjetas de red;
> pruebas de rendimiento Benchmark y sus tipos.»

Qué se puede preguntar: qué es el POST y qué es un punto de control (*checkpoint*); en qué puerto de
E/S se escriben los puntos de control y con qué tarjeta se leen; por qué un error se avisa con pitidos
y no con un mensaje en pantalla; qué significan 1, 3, 6, 7 y 8 pitidos en AMIBIOS8 y qué se hace en
cada caso; cómo se aísla una tarjeta de expansión averiada; qué hace la BIOS si la suma de
comprobación de la CMOS es incorrecta; qué significan los códigos mayor y menor de HP y sus mensajes
numerados del POST (pila, memoria, SMART, arranque, ventilador); qué se pierde cuando falla la pila de botón; qué es una FRU y
una CRU y cuándo no se cambia una pieza; qué precauciones se toman contra la electricidad estática;
qué se comprueba cuando el equipo no enciende y por qué no se abre la fuente de alimentación;
qué es una pantalla azul, qué es el código de detención, cuáles son sus causas más frecuentes y dónde
queda el volcado de memoria; qué es SMART, qué distingue un atributo *Pre-fail* de uno *Old age* y qué significa «FAILING_NOW»;
cuánto duran las autopruebas corta y larga; qué indican en una NVMe el *Critical Warning*, la reserva
disponible y el porcentaje usado; qué hacen `chkdsk`, `chkdsk /f`, `/r`, `/x` y `/b`, qué
permiso exige y qué códigos de salida devuelve; qué hace `sfc /scannow`; cómo se lanza el Diagnóstico de memoria de Windows y dónde se lee su
resultado; qué mide MemTest86, por qué
un error suyo no prueba siempre que la memoria esté mal y cómo se localiza el módulo averiado; qué es
la prueba de martilleo; qué significan los códigos 10, 22, 28 y 43 del Administrador de dispositivos;
qué es el TDR y cuánto tarda en saltar; para qué sirven `ipconfig` y `ping`; qué es un *benchmark*,
qué distingue tiempo de respuesta y productividad, y cómo se clasifican las pruebas por su ámbito
(enteros, coma flotante, transacciones) y por la naturaleza del programa (reales, núcleos, conjuntos,
reducidos, sintéticos); qué miden SPECspeed y SPECrate; qué mide cada herramienta del puesto
(Cinebench, 3DMark, PassMark PerformanceTest, CrystalDiskMark, `winsat mem`). En la aplicación
práctica: leer una secuencia de pitidos, elegir la orden o la prueba ante un síntoma, interpretar una
línea de atributos SMART y calcular MIPS o MFLOPS de un programa.

<!-- indice -->

## Índice

- [1. Diagnóstico, mantenimiento y reparación: cómo se trabaja](#1-diagnóstico-mantenimiento-y-reparación-cómo-se-trabaja)
  - [Antes de abrir el equipo](#antes-de-abrir-el-equipo)
  - [La electricidad estática](#la-electricidad-estática)
  - [El mantenimiento](#el-mantenimiento)
- [2. Principales averías](#2-principales-averías)
  - [Dónde se manifiesta la avería](#dónde-se-manifiesta-la-avería)
  - [Hardware o software](#hardware-o-software)
  - [El equipo no enciende](#el-equipo-no-enciende)
  - [La pantalla azul (error de detención)](#la-pantalla-azul-error-de-detención)
- [3. Mensajes de error de la BIOS](#3-mensajes-de-error-de-la-bios)
  - [El POST y los puntos de control](#el-post-y-los-puntos-de-control)
  - [Los códigos de pitidos](#los-códigos-de-pitidos)
  - [Los pitidos de otros fabricantes](#los-pitidos-de-otros-fabricantes)
  - [Los mensajes en pantalla](#los-mensajes-en-pantalla)
- [4. Sustitución y detección de averías en discos duros, memorias, tarjetas gráficas y tarjetas de red](#4-sustitución-y-detección-de-averías-en-discos-duros-memorias-tarjetas-gráficas-y-tarjetas-de-red)
  - [Discos duros: detectar con SMART](#discos-duros-detectar-con-smart)
  - [Discos duros: comprobar el sistema de ficheros con chkdsk](#discos-duros-comprobar-el-sistema-de-ficheros-con-chkdsk)
  - [Discos duros: sustituir](#discos-duros-sustituir)
  - [Memorias: detectar](#memorias-detectar)
  - [Memorias: localizar el módulo y sustituirlo](#memorias-localizar-el-módulo-y-sustituirlo)
  - [Tarjetas gráficas: detectar](#tarjetas-gráficas-detectar)
  - [Tarjetas gráficas: sustituir](#tarjetas-gráficas-sustituir)
  - [Tarjetas de red: detectar](#tarjetas-de-red-detectar)
  - [Tarjetas de red: sustituir](#tarjetas-de-red-sustituir)
  - [El Administrador de dispositivos y PnPUtil](#el-administrador-de-dispositivos-y-pnputil)
- [5. Pruebas de rendimiento (benchmark) y sus tipos](#5-pruebas-de-rendimiento-benchmark-y-sus-tipos)
  - [Qué es un benchmark](#qué-es-un-benchmark)
  - [Qué se mide](#qué-se-mide)
  - [Tipos de benchmark](#tipos-de-benchmark)
  - [SPEC CPU hoy](#spec-cpu-hoy)
  - [Pruebas del puesto de usuario](#pruebas-del-puesto-de-usuario)
  - [Prueba de rendimiento y prueba de estrés](#prueba-de-rendimiento-y-prueba-de-estrés)
  - [Ejercicio de aplicación](#ejercicio-de-aplicación)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Diagnóstico, mantenimiento y reparación: cómo se trabaja

### Antes de abrir el equipo

El manual de mantenimiento de un fabricante es la primera fuente de cualquier reparación: dice qué
piezas se pueden cambiar, en qué orden se desmontan y qué precauciones exige el modelo. Se toma aquí
como ejemplo el de un ordenador de sobremesa de Lenovo (*M920s User Guide and Hardware Maintenance
Manual*, 2.ª edición, agosto de 2019); otro fabricante o modelo tendrá su propio manual, y manda el
del equipo que se repara.

El manual distingue dos clases de piezas:

| Clase | Qué es (literal) | Ejemplos del manual |
|---|---|---|
| FRU, unidad reemplazable en campo | **«Field Replaceable Units (FRUs) are computer parts that a trained technician can upgrade or replace. FRUs include all CRUs.»** | Todas las piezas del equipo que cambia un técnico formado, incluidas las CRU; el manual remite a una base de datos de recambios para el número de pieza de cada una |
| CRU, unidad reemplazable por el cliente | **«Customer Replaceable Units (CRUs) are computer parts that a user can upgrade or replace.»** | De autoservicio: **«the keyboard, mouse, any USB device»**; de servicio opcional, piezas internas tras un panel atornillado, que exigen **«some technical skills and simple tools (such as a screwdriver)»** |

Antes de cambiar una FRU, el manual fija reglas que valen como método general de diagnóstico:

- **«Only certified and trained personnel can service the computer.»** (Sólo personal certificado y
  formado.)
- **«Before replacing an FRU, read the entire section about replacing the part.»**
- **«Be extremely careful during writing operations such as copying, saving, or formatting.»** El
  motivo: el orden de las unidades del equipo puede estar cambiado y, si se elige la que no es, se
  sobrescriben datos o programas.
- **«Replace an FRU only with another FRU of the correct model.»**
- **«An FRU should not be replaced because of a single, unreproducible failure.»** La explicación
  del manual: **«Single failures can occur for a variety of reasons that have nothing to do with a
  hardware defect, such as cosmic radiation, electrostatic discharge, or software errors. Consider
  replacing an FRU only when a problem recurs. If you suspect that an FRU is defective, clear the
  error log and run the test again. If the error does not recur, do not replace the FRU.»** (Un fallo
  aislado que no se repite no justifica cambiar la pieza: se borra el registro de errores, se repite
  la prueba y sólo si el error vuelve se cambia.)
- **«Only replace a defective FRU.»**

Las sustituciones del manual empiezan igual, con el equipo apagado y sin corriente: **«Remove
any media from the drives and turn off all connected devices and the computer. Disconnect all power
cords from electrical outlets and disconnect all cables from the computer.»** Para el disipador y el
procesador añade una advertencia: **«The heat sink and fan assembly might be very hot. Before you open
the computer cover, turn off the computer and wait several minutes until the computer is cool.»** Y
todas terminan en el mismo cierre (**«Completing the parts replacement»**): comprobar **«that all
components have been reassembled correctly and that no tools or loose screws are left inside your
computer»**, que los cables van bien guiados antes de cerrar la tapa, volver a poner la tapa y
reconectar los cables externos y de corriente.

### La electricidad estática

El mismo manual dedica un apartado al manejo de piezas sensibles a la electricidad estática
(**«Handling static-sensitive devices»**). Parte de un aviso: **«Static electricity, although harmless
to you, can seriously damage computer components and options.»** Y de una regla de orden: no abrir la
bolsa antiestática de la pieza nueva hasta haber sacado la averiada y estar listo para instalarla.
Las precauciones, literal:

- **«Limit your movement. Movement can cause static electricity to build up around you.»**
- **«Handle PCI/PCIe cards, memory modules, system boards, and microprocessors by the edges. Never
  touch any exposed circuitry.»** (Las tarjetas, los módulos de memoria, la placa y el procesador se
  cogen por los bordes; nunca se toca un circuito al aire.)
- **«Prevent others from touching the options and other computer components.»**
- **«Touch the static-protective package containing the part to a metal expansion-slot cover or other
  unpainted metal surface on the computer for at least two seconds.»** (Tocar con la bolsa de la pieza
  una tapa metálica de ranura u otra superficie metálica sin pintar del equipo durante al menos dos
  segundos; según el manual, así se reduce la electricidad estática de la bolsa y del cuerpo.)
- Si se puede, sacar la pieza de la bolsa e instalarla directamente sin dejarla en ningún sitio; si
  no, dejarla sobre su bolsa en una superficie lisa y plana.
- **«Do not place the part on the computer cover or other metal surface.»**

La pulsera antiestática y la alfombrilla conectadas a tierra son práctica habitual del oficio, pero el
manual leído no las menciona y el tema no les atribuye fuente.

### El mantenimiento

El enunciado nombra el mantenimiento junto al diagnóstico y la reparación. Lo que las fuentes leídas
dicen de mantenimiento periódico es esto:

- Disco: Microsoft recomienda pasar `chkdsk` de vez en cuando (**«You should use chkdsk occasionally
  on FAT and NTFS file systems to check for disk errors.»**). En SSD advierte que no es peligroso,
  pero que los barridos completos repetidos, sobre todo con `/r`, pueden aumentar sin necesidad los
  ciclos de escritura y borrado y acortar algo su vida; para comprobaciones ocasionales no es
  preocupante.
- SMART: el manual de `smartctl` da como buena línea de arranque del sistema la que activa SMART, la
  prueba automática fuera de línea **«every four hours»** y el guardado automático de los atributos:
  `smartctl --smart=on --offlineauto=on --saveauto=on /dev/sda` (epígrafe 4).
- Pila de la CMOS: Lenovo dice que normalmente no necesita carga ni mantenimiento en toda su vida, **«however, no
  coin-cell battery lasts forever»** (epígrafe 3).
- Firmware: MemTest86 cuenta la actualización de la BIOS entre los remedios de errores de memoria por
  incompatibilidad (**«Apply BIOS update to fix incompatibility issues»**).
- Archivos del sistema: `sfc` **«Scans and verifies the integrity of all protected system files and
  replaces incorrect versions with correct versions.»** Con `/scannow` comprueba y repara cuando
  puede; con `/verifyonly` sólo comprueba. Exige ser miembro del grupo Administradores.
- Calor: HP agrupa una de sus cuatro familias de pitidos bajo el rótulo **«Thermal»**, y UL presenta
  las pruebas de estrés de 3DMark como forma de detectar **«a need for better cooling»** (epígrafe 5).

La limpieza de polvo, el cambio de pasta térmica y un calendario de mantenimiento preventivo son
oficio sin fuente leída; véase «Lo que este tema no da».

## 2. Principales averías

### Dónde se manifiesta la avería

El enunciado no da una lista cerrada de averías ni la hay en las fuentes leídas. El tema las ordena por
el momento en que aparecen, que es lo que decide la herramienta de diagnóstico. La ordenación es de
oficio; cada fila se apoya en la fuente que se cita en su epígrafe.

| Cuándo aparece | Cómo se manifiesta | Con qué se diagnostica | Epígrafe |
|---|---|---|---|
| Al pulsar el botón de encendido | Nada: ni pilotos, ni ventiladores, ni pitidos | Toma y cables; piloto de la placa; fuente de alimentación | 2 |
| Al encender, antes de que haya imagen | Pitidos por el altavoz de la placa; códigos en una tarjeta POST | Tabla de pitidos del fabricante; método de aislamiento de tarjetas | 3 |
| Durante el POST, ya con imagen | Mensaje en pantalla; la BIOS pide respuesta o entra en la configuración | Registro de errores del POST; configuración de la BIOS | 3 |
| Con el sistema operativo en marcha | Dispositivo con exclamación amarilla y código | Administrador de dispositivos, PnPUtil | 4 |
| Con el sistema en marcha, sobre el disco | Errores de lectura, sistema de ficheros dañado, aviso SMART | SMART (`smartctl`), `chkdsk` | 4 |
| Con el sistema en marcha, de golpe | Pantalla azul con un código de detención y reinicio | Código de detención, volcado de memoria, Administrador de dispositivos, prueba de memoria | 2 |
| De forma intermitente o aleatoria | Cuelgues, errores que no se repiten | MemTest86, pruebas de estrés; no cambiar la pieza por un fallo aislado | 1 y 4 |
| Sobre la imagen | Parpadeo y aviso de que el controlador de pantalla se ha recuperado | TDR, código 43, pruebas de estrés de la gráfica | 4 |
| Sobre la red | Sin conectividad, sin dirección, nombres que no se resuelven | `ipconfig`, `ping`, Administrador de dispositivos | 4 |
| Lentitud | El equipo rinde menos de lo esperado | Pruebas de rendimiento comparadas con una referencia | 5 |

La primera división la da la propia documentación de AMI: **«Beep codes are used when an error occurs
before the system video has been initialized.»** Es decir: si el equipo pita, la avería es anterior a
que se inicialice el vídeo; si muestra un mensaje, es posterior. Y la segunda, el manual de Lenovo:
lo que no se reproduce no se cambia.

### Hardware o software

Varias fuentes advierten que un síntoma de hardware puede no ser del componente que parece:

- MemTest86: **«not all errors reported by MemTest86 are due to bad memory»**; la prueba ejercita
  también la CPU, las cachés y la placa base (epígrafe 4).
- Lenovo: los fallos aislados pueden deberse a radiación cósmica, descarga electrostática o errores de
  software.
- Microsoft, sobre `chkdsk` en un disco grande que termina demasiado deprisa: puede ser que el volumen
  estuviera bloqueado, que no se leyeran todos los sectores o que el disco tenga **«a failing read head
  or other hardware issue»**.
- AMI, ante 6 o 7 pitidos: antes de dar la placa por perdida, descartar una tarjeta de expansión
  averiada (epígrafe 3).

### El equipo no enciende

La avería más básica es la del equipo que no da ninguna señal al pulsar el botón. La guía de
mantenimiento de HP para su sobremesa ProDesk 600 G5 SFF (*Maintenance and Service Guide*, 3.ª
edición, septiembre de 2019) la trata con este rótulo: **«System does not power on and the LEDs on the
front of the computer are not flashing.»** El primer paso separa dos casos: **«Press and hold the power
button for less than 4 seconds.»**

- Si se enciende en blanco el piloto del disco, se comprueba el selector de tensión de la
  fuente, si lo tiene; después, **«Remove the expansion cards one at a time until the 5V_aux light on
  the system board turns on.»**; y, si no, se cambia la placa.
- Si no se enciende nada, el orden es: **«Check that the unit is plugged into a working AC outlet.»**;
  comprobar que el cable del botón de encendido está bien conectado a la placa; **«Check that the power
  supply cables are properly connected to the system board.»**; mirar el piloto 5V_aux de la placa: si
  está encendido, se cambia el conjunto del botón de encendido, y **«If the 5V_aux light on the system
  board is off, then replace the power supply.»**; en último lugar, la placa.

La misma guía, en los problemas de alimentación, da como causa de que la fuente no arranque un fallo
interno, con un único remedio: **«Replace the power supply.»** Y un caso vecino, el equipo que se
apaga solo con el piloto parpadeando: la protección térmica del procesador, porque un ventilador está
bloqueado o parado o el disipador no está bien asentado; se comprueba que las rejillas no estén tapadas
y que el ventilador gire y esté conectado a la placa, y si no gira, se cambia.

La fuente de alimentación se cambia entera, nunca se abre. El manual de Lenovo lo advierte, por la
certificación de seguridad del equipo: **«Never remove the cover on a power supply or any part that has
the following label attached.»** Y explica por qué: **«Hazardous voltage, current, and energy levels are
present inside any component that has this label attached. There are no serviceable parts inside these
components. If you suspect a problem with one of these parts, contact a service technician.»** (Dentro
hay tensión, corriente y energía peligrosas y ninguna pieza reparable.) Su procedimiento
(**«Replacing the power supply assembly»**): quitar la tapa, el frontal, la unidad óptica y el soporte
del disco; **«Disconnect the power supply assembly cable from the system board.»**; cambiar el conjunto
de la fuente; **«Connect the new power supply assembly cable to the system board.»**; volver a montar.
Para ese modelo el manual lista fuentes de 180, 210 y 260 vatios, todas **«automatic
voltage-sensing»** (detectan solas la tensión de la red).

### La pantalla azul (error de detención)

Con el sistema en marcha, la avería más visible es la parada total de Windows. Microsoft la define así:
**«When Windows encounters a condition that compromises safe system operation, the system halts. This
condition is referred to as a bug check, or sometimes, a system crash, kernel error, or stop
error.»** En su página de soporte añade los nombres comunes: **«This is also known as a stop code
error, a bug check, a kernel error, or a Blue Screen error, or a Black Screen error, or BSOD.»** El
usuario ve brevemente un mensaje como «Your device ran into a problem and needs to restart.» y el
equipo se reinicia solo. El color y el texto de la pantalla cambian con la versión de Windows 11 (hay un
modelo para la 24H2 y posteriores y otro para la 23H2 y anteriores).

Lo que hay que leer en la pantalla es el código de detención y, si aparece, el módulo: **«a stop code,
such as PAGE_FAULT_IN_NONPAGED_AREA or MEMORY_MANAGEMENT will appear at the bottom of the screen, and if
available, the module name of the code that was being executed at the time the problem occurred.»**
Cada código tiene un nombre y un valor hexadecimal; algunos de la referencia de Microsoft:

| Valor | Nombre |
|---|---|
| 0x0000001A | MEMORY_MANAGEMENT |
| 0x00000050 | PAGE_FAULT_IN_NONPAGED_AREA |
| 0x0000007B | INACCESSIBLE_BOOT_DEVICE |
| 0x000000D1 | DRIVER_IRQL_NOT_LESS_OR_EQUAL |
| 0x00000116 | VIDEO_TDR_FAILURE |
| 0x00000117 | VIDEO_TDR_TIMEOUT_DETECTED |
| 0x00000124 | WHEA_UNCORRECTABLE_ERROR |

Los dos de vídeo llevan en el nombre el mecanismo TDR de la gráfica (epígrafe 4).

Las causas, según el análisis de Microsoft de los volcados que recibe: **«70% are caused by third-party
driver code.»**, un 10 % el hardware, un 5 % el código de Microsoft y un 15 % de causa desconocida,
porque la memoria está demasiado dañada para analizarla. Y **«The root cause of stop errors is rarely a
user-mode process.»**: el programa que estaba en marcha suele sólo destapar el fallo de un controlador,
del hardware o del sistema.

Qué se hace, según Microsoft:

- Un reinicio aislado no exige más: **«In most cases when Windows 11 restarts unexpectedly, the problem
  is resolved by the restart and no further action is needed.»** Si se repite el mismo código, los pasos
  básicos son quitar el hardware nuevo, arrancar en modo seguro, buscar en el Administrador de
  dispositivos los marcados con exclamación y actualizar su controlador (o deshabilitarlo o
  desinstalarlo), dejar libre entre el 10 y el 15 % del disco, instalar las actualizaciones de Windows y,
  si nada sirve, volver a un punto de restauración u otra opción de recuperación.
- La tabla de Microsoft por escenarios añade: ante errores de memoria, la herramienta Diagnóstico de
  memoria de Windows (epígrafe 4); ante errores del sistema de ficheros, la comprobación del disco; ante
  ficheros del sistema dañados, `sfc /scannow`; ante BIOS o firmware antiguo, preguntar al fabricante por
  una versión nueva de la BIOS o de la UEFI; y, en hardware, **«make sure all expansion boards are
  properly seated and all cables are properly connected.»**

Para analizar la causa, el sistema guarda un volcado de memoria. Se configura en las propiedades del
sistema (en la documentación, «Advanced system settings», pestaña «Advanced», «Startup and Recovery»,
lista «Write debugging information»): Microsoft
indica elegir **«Automatic memory dump»** y reiniciar para que surta efecto. Dónde queda cada tipo:

| Tipo de volcado | Ubicación |
|---|---|
| Volcado de memoria pequeño (256 kB) | `%SystemRoot%\Minidump` |
| Volcado de memoria del núcleo, completo, automático o activo | `%SystemRoot%\MEMORY.DMP` |

El volcado se comprueba con la herramienta DumpChk de Microsoft (que no esté dañado) y se analiza en otro
equipo con el depurador WinDbg de las herramientas de depuración de Windows, con la orden `!analyze -v`;
la pila de llamadas que muestra suele indicar el módulo causante.

## 3. Mensajes de error de la BIOS

### El POST y los puntos de control

Al encender el equipo, el firmware de la placa comprueba e inicializa el hardware antes de ceder el
control al sistema operativo: es la autoprueba de encendido, el POST. Las fuentes de este epígrafe
son de BIOS; los códigos propios de los equipos UEFI actuales no se han leído en fuente (véase «Lo que
este tema no da»).

La documentación pública de American Megatrends (AMI), *AMIBIOS8 Check Point and Beep Code List*,
versión 2.0 de 10 de junio de 2008, explica cómo informa la BIOS de lo que va haciendo:

- **«A checkpoint is either a byte or word value output to I/O port 80h. The BIOS outputs checkpoints
  throughout bootblock and Power-On Self Test (POST) to indicate the task the system is currently
  executing.»** (Un punto de control es un valor de un byte o de una palabra que la BIOS escribe en el
  puerto de E/S 80h durante el bloque de arranque y el POST para indicar la tarea que está ejecutando.)
- Para qué sirven: **«Checkpoints are very useful in aiding software developers or technicians in
  debugging problems that occur during the pre-boot process.»**
- Cómo se leen: **«Viewing all checkpoints generated by the BIOS requires a checkpoint card, also
  referred to as a "POST Card" or "POST Diagnostic Card". These are ISA or PCI add-in cards that show
  the value of I/O port 80h on a LED display.»** (Una tarjeta de diagnóstico POST, pinchada en una
  ranura, muestra en un visor de LED el valor del puerto 80h.)
- La alternativa en pantalla: algunos equipos muestran los puntos de control en la esquina inferior
  derecha durante el POST (no todos activan esta función), pero **«This display method is limited, since it only displays checkpoints
  that occur after the video card has been activated.»** Por eso, **«In most cases, a checkpoint card
  is the best tool for viewing AMIBIOS checkpoints.»**

El documento recorre la secuencia por fases. Primero el bloque de arranque: **«The Bootblock
initialization code sets up the chipset, memory and other components before system memory is
available.»** En esa fase se verifica la suma de comprobación del propio bloque (punto D2): **«System
will hang here if checksum is bad.»** Después, el POST, del que estos puntos interesan al
diagnóstico:

| Punto | Qué hace (literal) |
|---|---|
| 04 | **«Check CMOS diagnostic byte to determine if battery power is OK and CMOS checksum is OK.»** Y si la suma no cuadra: **«If the CMOS checksum is bad, update CMOS with power-on default values and clear passwords.»** |
| 2C | **«Detects and initializes the video adapter installed in the system that have optional ROMs.»** |
| 3B | **«Test for total memory installed in the system.»** |
| 84 | **«Log errors encountered during POST.»** |
| 85 | **«Display errors to the user and gets the user response for error.»** |
| 87 | **«Execute BIOS setup if needed / requested. Check boot password if installed.»** |
| 00 | **«Passes control to OS Loader (typically INT19h).»** |

De ahí sale el orden del diagnóstico: lo que falla antes del punto 2C (vídeo) sólo puede avisarse con
pitidos o con la tarjeta POST; lo que falla después se registra (84) y se muestra al usuario (85).

La propia fuente pone tres límites. Declara su alcance: se revisó por última vez con la publicación del núcleo AMIBIOS8 Core 8.00.04 y **«covers AMIBIOS products released before May 2002»**. Los puntos de control son del núcleo genérico de AMIBIOS: **«The
checkpoints defined in this document are inherent to the AMIBIOS generic core, and do not include any
chipset or board specific checkpoint definitions.»** Y pueden cambiar con la plataforma: **«Please
note that checkpoints may differ between different platforms based on system configuration.»**
Consecuencia práctica: los códigos dependen del fabricante del firmware, de la placa y de la
generación, y hay que consultarlos en la documentación del equipo concreto. AMI es el ejemplo, no la
norma.

### Los códigos de pitidos

AMI define así los pitidos: **«Beep codes are used by the BIOS to indicate a serious or fatal error to
the end user. Beep codes are used when an error occurs before the system video has been initialized.
Beep codes will be generated by the system board speaker, commonly referred to as the "PC
speaker."»** (Los pitidos avisan de un error grave o fatal ocurrido antes de que se inicialice el
vídeo, y suenan por el altavoz de la placa.)

Tabla de pitidos del POST de AMIBIOS8 (§ 8.2 y 8.2.1 del documento):

| Pitidos | Error (literal) | Qué hacer (literal) |
|---|---|---|
| 1 | **«Memory refresh timer error.»** | **«Reseat the memory, or replace with known good modules.»** |
| 3 | **«Base memory read/write test error»** | Igual que el anterior: volver a asentar la memoria o cambiarla por módulos que se sepa que funcionan |
| 6 | **«Keyboard controller BAT command failed»** | **«Fatal error indicating a serious problem with the system. Consult your system manufacturer.»** Antes, descartar una tarjeta de expansión averiada (método de aislamiento, abajo) |
| 7 | **«General exception error (processor exception interrupt error)»** | Igual que el de 6 pitidos |
| 8 | **«Display memory error (system video adapter)»** | **«If the system video adapter is an add-in card, replace or reseat the video adapter. If the video adapter is an integrated part of the system board, the board may be faulty.»** |

Resumen para el examen: 1 y 3 pitidos, memoria; 8 pitidos, memoria de vídeo (tarjeta gráfica); 6 y 7,
error fatal del sistema (controlador de teclado y excepción del procesador). La tabla tiene huecos
porque AMI los suprimió: el historial de revisiones del documento recoge, en la 1.8 (17 de mayo de
2006), **«Removed unused POST(2,4,5,9,10,11) and Boot Block(8,9) beep codes.»**, y en la 1.9 (11 de
octubre de 2007) se corrigió el código de 6 pitidos a **«Keyboard controller BAT command failed»**.
Quien recuerde tablas antiguas de 2, 4, 5, 9, 10 u 11 pitidos tiene una versión que el propio
fabricante retiró.

El método de aislamiento que AMI da para 6 y 7 pitidos, literal: **«Before declaring the motherboard
beyond all hope, eliminate the possibility of interference by a malfunctioning add-in card. Remove all
expansion cards except the video adapter.»** Después:

1. **«If beep codes are generated when all other expansion cards are absent, consult your system
   manufacturer's technical support.»** (Si sigue pitando sin tarjetas, el problema es de la placa o
   del sistema: servicio técnico.)
2. **«If beep codes are not generated when all other expansion cards are absent, one of the add-in
   cards is causing the malfunction. Insert the cards back into the system one at a time until the
   problem happens again. This will reveal the malfunctioning card.»** (Si deja de pitar, la culpable
   es una tarjeta: se van reponiendo de una en una hasta que vuelve el fallo.)

AMI tiene además pitidos del bloque de arranque, que se oyen durante la recuperación del firmware
(**«Boot Block Beep Codes»**): por ejemplo, 4 pitidos, **«Flash Programming successful»**; 7, **«No
Flash EPROM detected»**; 10, **«Flash Erase error»**; 11, **«Flash Program error»**; 13, **«BIOS ROM
image mismatch (file layout does not match image present in flash device)»**. No son averías del
POST, sino avisos del proceso de regrabar la BIOS.

### Los pitidos de otros fabricantes

Cada fabricante tiene su propio código, y no coinciden. HP, en su diagnóstico interactivo de pitidos y
LED para la serie Desktop Pro A G2/G3, combina pitidos largos y cortos y los agrupa en cuatro familias
según el número de pitidos largos:

| Familia (rótulo de HP) | Pitidos |
|---|---|
| **«BIOS»** | 2 largos y 2, 3 o 4 cortos |
| **«Hardware»** | 3 largos y de 2 a 6 cortos |
| **«Thermal»** | 4 largos y 2 o 3 cortos |
| **«System Board»** | 5 largos y de 2 a 5 cortos |

El documento leído es interactivo y no trae el significado de cada combinación; ofrece también un
diagnóstico por LED. Lo que sí trae es la estructura: en HP, la familia la da el número de pitidos
largos.

El significado se lee en la guía de mantenimiento de otro sobremesa de HP, el ProDesk 600 G5 SFF
(*Maintenance and Service Guide*, 3.ª edición, septiembre de 2019), que usa las mismas cuatro familias.
Al arrancar, la BIOS valida la alimentación, el procesador, la propia BIOS, la memoria, la gráfica y la
placa; si algo falla, lo avisa con parpadeos de los pilotos frontales, largos y cortos, acompañados de
pitidos largos y cortos donde los hay. El código tiene dos partes: la mayor (pitidos o parpadeos largos,
en rojo) da la categoría, y la menor (cortos, en blanco), el error concreto. Así, «3.5» son tres
parpadeos rojos largos y cinco blancos cortos. Reglas de la guía: **«Single beep/blink codes are not
used.»**; **«Beep error code sequences occur for the first 5 iterations of the pattern and then
stop.»**, mientras que el parpadeo sigue hasta que se desenchufa el equipo o se pulsa el botón; y
**«Not all diagnostic lights and audible codes are available on all models.»**

| Código | Categoría | Qué indica (resumen del literal de HP) |
|---|---|---|
| 2.2 | BIOS | La zona principal de la BIOS (DXE) se ha dañado y no hay imagen de recuperación |
| 2.3 | BIOS | El controlador integrado exige que el usuario teclee una secuencia de teclas |
| 2.4 | BIOS | El controlador integrado está comprobando o recuperando el bloque de arranque |
| 3.2 | Hardware | Tiempo agotado esperando a que la BIOS termine de inicializar la memoria |
| 3.3 | Hardware | Tiempo agotado esperando a que la BIOS termine de inicializar la gráfica |
| 3.4 | Hardware | La placa muestra un fallo de alimentación (*crowbar*) |
| 3.5 | Hardware | **«The processor is not detected.»** |
| 3.6 | Hardware | El procesador no admite una función que está activada |
| 4.2 | Térmica | **«A processor over temperature condition has been detected.»** |
| 4.3 | Térmica | Exceso de temperatura ambiente |
| 4.4 | Térmica | Exceso de temperatura en el módulo MXM |
| 5.2 | Placa | El controlador integrado no encuentra un *firmware* válido |
| 5.3 y 5.4 | Placa | Tiempo agotado esperando a la BIOS (en general, o al inicializar la placa) |
| 5.5 | Placa | El controlador integrado reinició el sistema tras detectar un posible bloqueo |

En el modelo Desktop Pro A, la familia térmica sólo llega a 4 largos y 3 cortos: los códigos de un
modelo no valen para otro, y manda la guía del equipo concreto. Las tablas de Dell, Award y Phoenix
no se han podido leer en fuente.

### Los mensajes en pantalla

Cuando el error ocurre con el vídeo ya inicializado, la BIOS lo registra y lo muestra (puntos 84 y 85
de AMI) y, si hace falta, entra en la configuración (punto 87). La pila de la CMOS es el caso que las
fuentes documentan:

- Qué guarda, según Lenovo: **«Your computer has a special type of memory that maintains the date,
  time, and settings for built-in features, such as parallel connector assignments (configurations). A
  coin-cell battery keeps this information active when you turn off the computer.»**
- Qué pasa cuando falla: **«If the coin-cell battery fails, the date, time, and configuration
  information (including passwords) are lost. An error message is displayed when you turn on the
  computer.»** (Se pierden fecha, hora, configuración y contraseñas, y aparece un mensaje de error al
  encender.)
- Qué hace la BIOS de AMI, punto 04: comprueba si la alimentación de la pila es correcta y si cuadra
  la suma de comprobación de la CMOS; si no cuadra, carga los valores por defecto y borra las
  contraseñas.

Síntoma típico, por tanto: el equipo arranca con la fecha y la hora desfasadas y la configuración de
fábrica, y avisa en pantalla. La reparación es cambiar la pila y volver a configurar fecha, hora y
opciones de la BIOS. El manual de Lenovo da para ello su propio procedimiento (**«Replacing the
coin-cell battery»**): sacar los discos u otros soportes de las unidades, apagar el equipo y todo lo
conectado y desenchufar los cables de alimentación y los demás; quitar la tapa y el frontal; abatir hacia
arriba el conjunto de bahías; cambiar la pila, y volver a montar las piezas retiradas. La pila gastada se desecha según el
aviso sobre pilas de litio de la guía de seguridad del fabricante, como indica el manual.

El texto de los mensajes lo fija cada fabricante, y cambia de una BIOS a otra. Como ejemplo, la guía
de mantenimiento de HP del ProDesk 600 G5 SFF da una lista de mensajes numerados del POST, con su
causa y lo que hay que hacer (**«POST numeric codes and text messages»**); tras mostrar uno, el equipo
da un pitido. Los más útiles para el diagnóstico:

| Mensaje (literal) | Causa según HP | Qué hacer, según HP |
|---|---|---|
| **«002-Option ROM Checksum Error»** | Suma de comprobación de la ROM del sistema o de la ROM de una tarjeta de expansión | Verificar la ROM y regrabarla si hace falta; quitar la tarjeta recién añadida; borrar la CMOS; cambiar la placa |
| **«005-Real-Time Clock Power Loss»** | Fecha u hora no válidas en la memoria de configuración; puede hacer falta cambiar la pila del RTC | Poner fecha y hora; si se repite, cambiar la pila |
| **«2E1-MemorySize Error»** | La cantidad de memoria ha cambiado desde el último arranque | Pulsar F1 para guardar el cambio; si persiste, comprobar que los módulos están bien instalados |
| **«2E2-Memory Error»** | Falló la configuración de los módulos al arrancar | Comprobar la instalación y el tipo de módulo; cambiar el módulo averiado; si sigue, la placa |
| **«301-Hard Disk 1: SMART Hard Drive Detects Imminent Failure»** | El disco va a fallar (algún disco tiene un parche de *firmware* para un aviso erróneo) | Confirmar con el diagnóstico del arranque (F2); aplicar el parche si procede; **«Back up contents and replace hard drive.»** |
| **«3F0–Boot Device Not Found»** | No se encuentra dispositivo de arranque | Insertar un dispositivo de arranque o cargar el sistema operativo |
| **«800-Keyboard Error»** | Fallo del teclado | Reconectarlo con el equipo apagado, revisar el conector, comprobar que no hay teclas pulsadas, cambiarlo |
| **«900-CPU Fan Not Detected»** | El ventilador del procesador no está conectado o puede haber fallado | Reasentar el ventilador y su cable; cambiarlo |
| **«90D-System Temperature»** | El equipo se apagó antes para no sobrecalentarse (rejillas tapadas o temperatura fuera de especificación) | **«Make sure system has proper airflow.»** |

El 005 es el caso de la pila con el texto de HP; el 301 enlaza con SMART (epígrafe 4). Los textos que
circulan en manuales de oficio con otra redacción («CMOS checksum error», «No boot device», «CPU fan
error») corresponden a otras BIOS que no se han leído en fuente: el tema no los da como literal.

## 4. Sustitución y detección de averías en discos duros, memorias, tarjetas gráficas y tarjetas de red

### Discos duros: detectar con SMART

Los discos llevan dentro su propio sistema de vigilancia. El manual de `smartctl` (smartmontools) lo
define: **«smartctl controls the Self-Monitoring, Analysis and Reporting Technology (SMART) system
built into most ATA/SATA and SCSI/SAS hard drives and solid-state drives. The purpose of SMART is to
monitor the reliability of the hard drive and predict drive failures, and to carry out different types
of drive self-tests.»** Sirve, por tanto, para discos mecánicos y SSD, y hace tres cosas: vigilar la
fiabilidad, predecir el fallo y lanzar autopruebas.

**Estado de salud** (`smartctl -H`). Si el disco informa de un estado de fallo, eso quiere decir que
**«the device has already failed»** o que **«it is predicting its own failure within the next 24
hours»**. La instrucción del manual es tajante: **«get your data off the disk and to someplace safe as
soon as you can.»** En NVMe, el estado se obtiene leyendo el byte **«Critical Warning»** del registro
de salud.

**Atributos** (`smartctl -A`). Cada atributo tiene un número (de 1 a 253) y un nombre; el ejemplo del
manual es el 12, **«power cycle count»**, cuántas veces se ha encendido el disco. De cada uno se
muestran:

| Columna | Qué es |
|---|---|
| RAW_VALUE | El valor en bruto, el que puede tener sentido físico (horas, grados, ciclos). La conversión a unidades no la fija el estándar SMART y algún fabricante usa convenciones raras |
| VALUE | El valor normalizado, de 1 a 254, que calcula el *firmware* del disco con un algoritmo de cada fabricante |
| WORST | El peor valor normalizado registrado en la vida del disco |
| THRESH | El umbral, de 0 a 255, fijado por el fabricante |
| TYPE | *Pre-fail* u *Old_age* |
| WHEN_FAILED | Si el atributo falla ahora, falló antes o nunca |

La regla de lectura: **«If the Normalized value is less than or equal to the Threshold value, then the
Attribute is said to have failed. If the Attribute is a pre-failure Attribute, then disk failure is
imminent.»** Los dos tipos: **«Attributes are one of two possible types: Pre-failure or Old age.»** Los
de prefallo, por debajo del umbral, anuncian fallo inminente; los de vejez, **«indicate end-of-product
life from old-age or normal aging and wearout»**. La salvedad que más se olvida: **«the fact that an
Attribute is of type 'Pre-fail' does not mean that your disk is about to fail! It only has this meaning
if the Attribute's current Normalized value is less than or equal to the threshold value.»** Y la
columna WHEN_FAILED: **«FAILING_NOW»** si el valor actual está en el umbral o por debajo; **«In_the_past»**
si no lo está, pero el peor registrado sí; un guion si el atributo está bien y nunca ha fallado.

Dos cautelas del propio manual: `smartctl` no calcula nada, sólo informa de lo que guarda el disco; y
en las SSD algunos atributos tienen otro significado, de modo que el nombre que muestra el programa
puede ser incorrecto si la unidad no está en su base de datos.

**Salud y desgaste de una SSD NVMe.** Las unidades NVMe no usan la tabla de atributos anterior, sino un
registro propio que define la especificación de NVM Express (*NVM Express Base Specification*, revisión
2.1, de 5 de agosto de 2024): la página de registro **«SMART / Health Information (Log Page Identifier
02h)»**, con información **«over the life of the controller»** que se conserva entre encendidos. Los
campos que sirven para diagnosticar:

| Campo | Qué es, según la especificación |
|---|---|
| *Critical Warning* (byte 0) | Avisos críticos, un bit por tipo; entre ellos: bit 0, la reserva disponible ha caído por debajo del umbral; bit 1, temperatura por encima (o por debajo) de un umbral; bit 2, **«the NVM subsystem reliability has been degraded due to significant media related errors or any internal error»**; bit 3, **«all of the media has been placed in read only mode»** |
| *Available Spare* (byte 3) | **«Contains a normalized percentage (0% to 100%) of the remaining spare capacity available.»** (La capacidad de reserva que le queda.) |
| *Available Spare Threshold* (byte 4) | El umbral, también en porcentaje: si la reserva cae por debajo, puede generarse un aviso al sistema |
| *Percentage Used* (byte 5) | **«Contains a vendor specific estimate of the percentage of NVM subsystem life used based on the actual usage and the manufacturer’s prediction of NVM life.»** (El desgaste estimado, en porcentaje de la vida prevista.) |
| *Composite Temperature* (bytes 1 y 2) | Una temperatura compuesta del controlador y de sus espacios de nombres, en kelvin; cómo se calcula depende de la implementación y puede no corresponder a ningún punto físico de la unidad |
| *Power Cycles*, *Power On Hours*, *Unexpected Power Losses* | Encendidos, horas de funcionamiento y cortes de corriente inesperados |
| *Media and Data Integrity Errors* | Veces que el controlador ha detectado un error de integridad de datos no recuperado (ECC no corregible, fallo de CRC…) |

La salvedad del *Percentage Used*, literal: **«A value of 100 indicates that the estimated endurance of
the NVM in the NVM subsystem has been consumed, but may not indicate an NVM subsystem failure. The value
is allowed to exceed 100.»** Un 100 % no significa que la unidad haya fallado, sino que ha consumido la
resistencia estimada por el fabricante; el valor puede pasar de 100 (por encima de 254 se muestra 255) y
se actualiza una vez por hora de funcionamiento (cuando el controlador no está en reposo). En `smartctl`, la opción `-l ssd` muestra en las SSD
SCSI un indicador equivalente (0, como nueva; 100, al final de la vida prevista por el fabricante; puede
llegar a 255) y en las ATA, la página de estadísticas de dispositivo de estado sólido.

**Autopruebas** (`smartctl -t`). **«The "Self" tests check the electrical and mechanical performance as
well as the read performance of the disk.»** Los tipos:

| Prueba | Duración y alcance según el manual |
|---|---|
| `short` | **«runs SMART Short Self Test (usually under ten minutes)»** |
| `long` | **«runs SMART Extended Self Test (tens of minutes to several hours)»**; versión más larga y completa de la corta |
| `conveyance` | Sólo ATA; de minutos; **«intended to identify damage incurred during transporting of the device»** (daños del transporte) |
| `select,N-M` | Sólo ATA; prueba un rango de LBA en vez del disco entero (hasta cinco rangos por orden) |

Las pruebas corta, larga y de transporte pueden lanzarse con el sistema en uso. Los resultados se leen
en el registro de autopruebas (`smartctl -l selftest`). En NVMe, las autopruebas corta y extendida
figuran en el manual como función experimental nueva de la versión 7.4. Ejemplos del manual:
`smartctl -a /dev/sda` muestra gran cantidad de información SMART; `smartctl -t long /dev/sdc` lanza la prueba
extendida, y su resultado se ve después con `-l selftest`.

### Discos duros: comprobar el sistema de ficheros con chkdsk

`chkdsk`, en Windows 10, Windows 11 y Windows Server de 2016 a 2025, **«Checks the file system and file
system metadata of a volume for logical and physical errors. If used without parameters, chkdsk
displays only the status of the volume and doesn't fix any errors.»** Sin parámetros, sólo informa;
para reparar hacen falta `/f`, `/r`, `/x` o `/b`.

| Parámetro | Qué hace (literal) |
|---|---|
| `/f` | **«Fixes errors on the disk. The disk must be locked.»** |
| `/r` | **«Locates bad sectors and recovers readable information. The disk must be locked. /r includes the functionality of /f, with the additional analysis of physical disk errors.»** |
| `/x` | **«Forces the volume to dismount first, if necessary.»** Invalida los manejadores abiertos e incluye `/f` |
| `/b` | Sólo NTFS. **«Clears the list of bad clusters on the volume and rescans all allocated and free clusters for errors. /b includes the functionality of /r. Use this parameter after imaging a volume to a new hard disk drive.»** |
| `/scan` | Sólo NTFS. **«Runs an online scan on the volume.»** |
| `/spotfix` | Sólo NTFS. **«Runs spot fixing on the volume.»** |

Los parámetros se encadenan: `/x` incluye `/f`; `/r` incluye `/f`; `/b` incluye `/r`. El uso de `/b`
enlaza con la sustitución: tras volcar la imagen de un volumen a un disco nuevo, se borra la lista de
clústeres defectuosos heredada del disco viejo y se vuelve a examinar.

Condiciones y mensajes:

- Permisos: **«Membership in the local Administrators group, or equivalent, is the minimum required to
  run chkdsk.»** Se abre el símbolo del sistema como administrador.
- Alcance: **«Chkdsk can be used only for local disks.»** No sirve sobre una letra de unidad redirigida
  por la red.
- Volumen en uso: si hay ficheros abiertos, aparece **«Chkdsk cannot run because the volume is in use
  by another process. Would you like to schedule this volume to be checked the next time the system
  restarts? (Y/N)»**; si se acepta, la comprobación se hace en el siguiente arranque, y si es la
  partición de arranque, el equipo se reinicia solo al terminar.
- FAT: las cadenas perdidas pueden guardarse en la raíz como ficheros **«File&lt;nnnn&gt;.chk»**.
- No conviene interrumpirlo, aunque interrumpirlo no debería dejar el volumen peor de lo que estaba.
- En HDD, `/r` y `/b` tardan mucho porque leen cada sector; en SSD, más deprisa, y marcar un clúster
  como defectuoso es una operación lógica, no una reasignación física.

Códigos de salida:

| Código | Significado (traducción del literal) |
|---|---|
| 0 | No se encontraron errores |
| 1 | Se encontraron errores y se corrigieron |
| 2 | Se hizo limpieza del disco (por ejemplo, recolección de basura) o no se hizo porque no se indicó `/f` |
| 3 | No se pudo comprobar el disco, los errores no se pudieron corregir o no se corrigieron porque no se indicó `/f` |

El registro de `chkdsk` se consulta en el Visor de eventos (`eventvwr.msc`), registro Aplicación,
filtrando por los orígenes Chkdsk y Wininit.

### Discos duros: sustituir

El procedimiento del manual de Lenovo para cambiar el disco principal de 3,5 pulgadas: apagar y
desconectar todo; quitar la tapa; quitar el frontal; abatir el conjunto de bahías; **«Disconnect the
signal cable and the power cable from the 3.5-inch primary storage drive.»**; cambiar el disco;
**«Connect the signal cable and the power cable to the new 3.5-inch storage drive.»**; volver a montar
y cerrar. El de 2,5 pulgadas va en un adaptador (*storage converter*) que se saca con él. El mismo
manual trata aparte la unidad M.2, que va en la placa. Dos cautelas que el manual da para cualquier
sustitución afectan de lleno al disco: cuidado extremo al copiar, guardar o formatear, porque el orden
de las unidades puede estar cambiado; y cambiar la pieza sólo por otra del modelo correcto.

Lo que el disco contiene no se sustituye con la pieza: la copia de seguridad, la clonación y la
recuperación de datos son materia del tema 3. Si SMART avisa de fallo, la prioridad que da el manual
de `smartctl` es sacar los datos cuanto antes.

### Memorias: detectar

Las señales de una memoria averiada en las fuentes leídas son tres:

1. Pitidos al encender: en AMIBIOS8, 1 pitido (**«Memory refresh timer error.»**) y 3 pitidos
   (**«Base memory read/write test error»**), con el remedio de volver a asentar los módulos o cambiarlos
   por otros que funcionen (epígrafe 3).
2. Errores en una prueba de memoria arrancada fuera del sistema operativo, como MemTest86 (PassMark).
3. Errores intermitentes: PassMark advierte que pueden causar problemas que tardan mucho en dar la cara y que
   los errores intermitentes que detecta MemTest86 son, sin excepción, válidos.

Windows trae su propia prueba, el Diagnóstico de memoria de Windows. La página vigente de Microsoft
sobre errores de detención la recomienda ante errores de memoria: **«Run the Windows Memory Diagnostics
tool to test the memory.»** Se abre desde el Panel de control, buscando «Memory» y eligiendo «Diagnose
your computer's memory problems», y el resultado se lee después en el Visor de eventos: **«After the
test runs, use Event Viewer to see the results under the system log. Look for the
MemoryDiagnostics-Results entry and view the results.»** El ejecutable, `mdsched.exe`, y el detalle de
su funcionamiento constan en un consejo de TechNet Magazine escrito para Windows 7, que Microsoft
mantiene archivado: se elige entre reiniciar ya o en el siguiente arranque; la prueba corre al
reiniciar, con la mezcla estándar por defecto; con F1 se elige **«Basic, Standard, or Extended»** y con
F10 se aplica; al terminar, el equipo se reinicia y muestra el resultado al iniciar sesión; y si Windows
detecta que un cuelgue se debe a la memoria, propone programar la prueba para el siguiente arranque.
Que ese detalle siga igual en Windows 11 no se ha confirmado en fuente vigente.

MemTest86 ejecuta una serie de pruebas numeradas, combinación de algoritmo, patrón de datos y uso de la
caché, ordenadas **«so that errors will be detected as rapidly as possible»**. Algunas, por lo que
detectan:

| Prueba | Qué busca |
|---|---|
| 0 a 2, de direcciones | Errores de direccionamiento: **«Tests all address bits in all memory banks by using a walking ones address pattern.»** (prueba 0) |
| 3 a 5 y 7, inversiones móviles | Errores «duros» y errores sensibles a los datos, con patrones de unos y ceros, de 8 bits, aleatorios y de 32 bits |
| 6, movimiento de bloques | Estrés de la memoria moviendo bloques de 4 MB |
| 10, desvanecimiento de bits | Llena la memoria con un patrón, espera unos minutos y comprueba si algún bit ha cambiado |
| 13, martilleo | **«designed to detect RAM modules that are susceptible to disturbance errors caused by charge leakage»** |
| 14, DMA | Errores que aparecen en transferencias por DMA iniciadas por periféricos como los discos |

La prueba de martilleo (*row hammer*) merece una explicación: según PassMark, los módulos sensibles
pueden sufrir errores de perturbación **«when repeatedly accessing addresses in the same memory bank but
different rows in a short period of time»**: abrir y cerrar filas una y otra vez provoca fugas de carga
en las filas vecinas y puede invertir bits. Desde la versión 6.2 la prueba puede hacer dos pasadas: la
primera a la máxima frecuencia posible; si en ella hay errores, se lanza una segunda a la frecuencia que
los fabricantes de memoria consideran el peor caso, y si sólo falla la primera se muestra un aviso en vez
de un error. Para equipos que exigen alta disponibilidad, PassMark dice que se cambiaría la RAM sin
dudarlo y probablemente se pasaría a memoria con corrección de errores (ECC), advirtiendo que no todas
las placas la admiten.

Cómo se interpreta un error de MemTest86, literal de PassMark:

- **«Please be aware that not all errors reported by MemTest86 are due to bad memory. The test
  implicitly tests the CPU, L1 and L2 caches as well as the motherboard. It is impossible for the test
  to determine what causes the failure to occur. However, most failures will be due to a problem with
  memory module. When it is not, the only option is to replace parts until the failure is
  corrected.»**
- **«Sometimes memory errors show up due to component incompatibility. A memory module may work fine in
  one system and not in another.»**
- Los errores que sólo salen con todos los módulos puestos apuntan a la configuración multicanal: lo
  recomendado son **«modules with identical specifications (ie. "matching modules")»**, y la lista de
  memorias compatibles que publica el fabricante de la placa.
- **«MemTest86 cannot diagnose many types of PC failures. For example a faulty CPU that causes Windows
  to crash will most likely just cause MemTest86 to crash in the same way.»**
- Los resultados pueden variar de una pasada a otra: celdas débiles que fallan sólo a veces, errores
  sensibles a la temperatura, ruido eléctrico, ranuras de la placa que no se comportan igual; y
  **«Moving RAM between slots will re-seat the RAM. This can clean up dirty or corroded contacts»**,
  con lo que el error puede desaparecer al mover el módulo.

### Memorias: localizar el módulo y sustituirlo

MemTest86 informa de la dirección del fallo, pero de ella no se deduce sin más el módulo, porque cada
procesador reparte las direcciones entre los módulos a su manera. PassMark propone tres técnicas:

1. **Quitar módulos**: el método más sencillo, si se pueden retirar. Se prueba con algunos y se anota
   exactamente qué módulos había cuando la prueba pasa y cuando falla.
2. **Rotar módulos**: si no se puede quitar ninguno, con tres o más módulos se intercambian dos de
   posición; si cambia el bit o la dirección del fallo, el culpable es uno de los dos movidos.
3. **Sustituir módulos** de forma selectiva, si no cabe ninguna de las anteriores.

Remedios, por orden de la fuente: **«Replace the RAM modules (most common solution)»**; poner tiempos
de memoria por defecto o conservadores y desactivar XMP; subir la tensión de la RAM; bajar la del
procesador; **«Apply BIOS update to fix incompatibility issues»**; marcar como defectuosas las zonas
de memoria que fallan. Al cambiar módulos, PassMark aconseja elegir uno de la lista de compatibles del
fabricante de la placa. Subir la tensión de la RAM es a riesgo propio, porque una tensión excesiva puede
dañar componentes.

El cambio físico, según Lenovo: apagar y desconectar, quitar la tapa y el frontal, abatir las bahías,
cambiar el módulo y cerrar. El manual exige respetar el orden de instalación de los módulos en las
ranuras que indica su figura (**«Ensure that you follow the order of installing memory modules shown in
the following figure.»**), y el módulo se coge por los bordes (precauciones del epígrafe 1).

Windows trae además una prueba de ancho de banda de memoria, `winsat mem`, que es de rendimiento, no de
errores (epígrafe 5).

### Tarjetas gráficas: detectar

La avería de la gráfica se manifiesta en momentos distintos, y en cada uno hay una herramienta:

- **Al encender, sin imagen**: AMIBIOS8 avisa con 8 pitidos, **«Display memory error (system video
  adapter)»**. Si la gráfica es una tarjeta, se vuelve a asentar o se cambia; si va integrada en la
  placa, la placa puede estar averiada (epígrafe 3). La detección de la tarjeta de vídeo es el punto
  2C del POST.
- **Con Windows en marcha, la imagen se congela**: Windows tiene un mecanismo de detección y
  recuperación (TDR). El planificador de la GPU detecta cuándo una tarea tarda más de lo permitido e
  intenta interrumpirla; **«The default timeout period in Windows is two seconds. If the GPU can't
  complete or preempt the current task within the TDR timeout period, the OS diagnoses that the GPU is
  frozen.»** Entonces el sistema reinicia la pila gráfica: el controlador se reinicializa y reinicia la
  GPU, y se vacía la memoria de vídeo. Lo que ve el usuario: **«The only visible artifact from hang
  detection to recovery is a screen flicker.»**, y un aviso, **«Display driver stopped responding and
  has recovered.»**, que queda también en el Visor de eventos. Algunas aplicaciones antiguas pueden
  quedarse en negro y hay que reiniciarlas. Un aviso de recuperación aislado no es, por sí, una avería;
  que se repita apunta al controlador o a la tarjeta.
- **En el Administrador de dispositivos**: el código 43 (**«Windows has stopped this device because it
  has reported problems. (Code 43)»**) es el que se ve cuando uno de los controladores informa de que
  el dispositivo ha fallado; los demás códigos, abajo.
- **Bajo carga**: las pruebas de estrés. UL, de 3DMark: **«Stress testing is a good way to check the
  reliability and stability of your system after buying or building a new PC, upgrading your graphics
  card, or overclocking your GPU. It can help you identify faulty hardware or a need for better
  cooling.»** Y cómo se lee: **«If your GPU crashes, hangs, or produces visual artifacts during the test,
  it may indicate a reliability or stability problem. If it overheats and shuts down, you may need more
  cooling in your computer.»** (Cuelgues o defectos visuales durante la prueba indican un problema de
  fiabilidad; si se calienta y se apaga, falta refrigeración.)

### Tarjetas gráficas: sustituir

Una gráfica dedicada es una tarjeta PCI Express. El manual de Lenovo lo describe para su modelo, cuya
placa tiene **«PCI Express x16 graphics card slot»** además de otras ranuras PCIe: apagar y desconectar,
quitar la tapa y el frontal, abatir las bahías y cambiar la tarjeta. **«If the card is held in place by
a retaining latch, press the latch 1 as shown to disengage the latch. Then, gently remove the card from
the slot.»** (Si la sujeta una pestaña de retención, se pulsa para soltarla y la tarjeta se saca con
suavidad.) Se coge por los bordes. Tras el cambio, el controlador se instala o actualiza (abajo).

Cuando el equipo no da imagen y la gráfica es sospechosa, el método de aislamiento de AMI (dejar sólo
la tarjeta de vídeo y reponer las demás de una en una) y la alternativa de la gráfica integrada en la
placa permiten separar la avería de la tarjeta de la de la placa.

### Tarjetas de red: detectar

La tarjeta de red (NIC) puede ser integrada en la placa, como el conector Ethernet que el manual de
Lenovo lista entre los conectores traseros (**«Used to connect an Ethernet cable for network
access.»**), una tarjeta PCIe o una tarjeta Wi-Fi M.2. La detección pasa por tres niveles:

1. **¿La ve el sistema?** Administrador de dispositivos: si tiene exclamación amarilla, el código
   orienta (22, deshabilitada; 28, sin controlador; 10, no arranca; 43, ha informado de un fallo).
2. **¿Tiene configuración IP?** `ipconfig` **«Displays all current TCP/IP network configuration values
   and refreshes Dynamic Host Configuration Protocol (DHCP) and Domain Name System (DNS) settings. Used
   without parameters, ipconfig displays Internet Protocol version 4 (IPv4) and IPv6 addresses, subnet
   mask, and default gateway for all adapters.»** Con `/all` da la configuración completa de todos los
   adaptadores; con `/release` y `/renew`, libera y renueva la concesión DHCP; con `/flushdns`, vacía la
   caché del resolvedor DNS. Microsoft señala que es más útil en equipos con dirección automática, para
   ver qué ha configurado DHCP, la asignación automática privada (APIPA) o una configuración alternativa.
3. **¿Llega a otro equipo?** `ping` **«Verifies IP-level connectivity to another TCP/IP computer by
   sending Internet Control Message Protocol (ICMP) echo Request messages.»** y es **«the primary TCP/IP
   command used to troubleshoot connectivity, reachability, and name resolution.»** Por defecto envía 4
   peticiones (`/n`) de 32 bytes (`/l`) y espera 4.000 ms cada respuesta (`/w`); si no llega, muestra
   **«Request timed out»**; `/t` repite hasta que se interrumpe. El diagnóstico clásico de la fuente:
   **«If pinging the IP address is successful, but pinging the computer name isn't, you might have a
   name resolution problem.»** (Si responde la dirección y no el nombre, el problema es de resolución de
   nombres, no de la tarjeta.)

El cable, la toma RJ45 y los indicadores luminosos de enlace de la tarjeta son materia del tema 4
(conectividad) y del tema 13 (redes); aquí no se han leído en fuente de fabricante.

### Tarjetas de red: sustituir

Una tarjeta PCIe se cambia como la gráfica. El manual de Lenovo trae además el cambio de la tarjeta
Wi-Fi M.2: apagar y desconectar, quitar la tapa y el frontal, abatir las bahías, quitar la pantalla
de la tarjeta (*Wi-Fi card shield*), desconectar las antenas, cambiar la tarjeta, volver a conectarlas y
montar de nuevo. Las antenas Wi-Fi tienen su propio procedimiento de sustitución, y la placa base también.

### El Administrador de dispositivos y PnPUtil

En Windows, el diagnóstico de gráficas y tarjetas de red pasa también por los controladores.
Microsoft: **«When Device Manager marks a device with a yellow exclamation point, it also provides an
error message.»** Los códigos están definidos en el fichero de cabecera `Cfg.h` con nombres
`CM_PROB_*`. Los que se explican aquí, con su mensaje y la solución recomendada:

| Código | Nombre | Mensaje (literal) | Solución recomendada por Microsoft |
|---|---|---|---|
| 10 | CM_PROB_FAILED_START | **«This device cannot start. (Code 10)»** (mensaje genérico: si la clave del dispositivo trae un texto propio, *FailReasonString*, se muestra ese) | **«Select Update Driver, which starts the Hardware Update wizard.»** Uno de los controladores de la pila del dispositivo ha fallado al arrancarlo |
| 22 | CM_PROB_DISABLED | **«This device is disabled. (Code 22)»** | **«The device is disabled because the user disabled it using Device Manager. Select Enable Device, which will enable the device.»** |
| 28 | CM_PROB_FAILED_INSTALL | **«The drivers for this device are not installed. (Code 28)»** | **«Please visit the website of the company that manufactures the device and look for the most recent drivers for this device.»** El primer caso que da la página es que no hay controlador compatible (**«PnP could not find a compatible driver for the device. This failure is often referred to as a DNF (driver not found) problem.»**); la página da otros tres casos, debidos a dependencias del paquete de controlador que faltan o a un fichero de instalación (`.inf`) que no asocia servicio al dispositivo |
| 43 | CM_PROB_FAILED_POST_START | **«Windows has stopped this device because it has reported problems. (Code 43)»** | **«Uninstall and reinstall the device.»** Un controlador ha informado de que el dispositivo ha fallado |

Otros códigos de la misma lista, con la explicación breve de Microsoft: el 1, dispositivo no
configurado; el 12, recursos insuficientes para arrancarlo; el 14, hace falta reiniciar para que
surtan efecto los cambios; el 18, hay que reinstalarlo; el 31, el dispositivo no se añadió (por
ejemplo, porque falla la rutina del controlador o falta su servicio en el registro). La página de
Microsoft lista además códigos del 3 al 57 que aquí no se desarrollan.

Microsoft cuenta un caso típico del código 28 tras actualizar el sistema: el dispositivo funcionaba
con su controlador, y después de la actualización a Windows 10 muestra el código 28, con frecuencia
porque el paquete del controlador quedó fuera de la migración.

PnPUtil, incluido en Windows desde Vista en `%windir%\system32` y que se ejecuta como administrador,
hace lo mismo por línea de órdenes. `pnputil /enum-devices /problem` lista los dispositivos con
problema (o con un código concreto: `/problem 43`), opción disponible desde Windows 10 versión 1903;
`/drivers` (desde la versión 2004) muestra los controladores que coinciden y los instalados; `/restart-device`,
`/remove-device` y `/scan-devices` reinician, quitan o vuelven a buscar dispositivos; `/add-driver
&lt;fichero.inf&gt; /install` añade e instala un paquete de controlador.

## 5. Pruebas de rendimiento (benchmark) y sus tipos

### Qué es un benchmark

La fuente universitaria de este epígrafe es el tema 4, «Rendimiento del procesador», de la asignatura
*Estructura de Computadores* de la Facultad de Informática de la Universidad Complutense de Madrid
(curso 2010-11). Distingue dos cosas al comparar equipos: la unidad de medida (la métrica) y el patrón
de medida (la carga de trabajo sobre la que se compara).

Para evaluar el rendimiento hay tres técnicas: **«Modelos analíticos (matemáticos) de la máquina»**,
**«Modelos de simulación (algorítmicos) de la máquina»** y **«La máquina real»**. Las dos primeras se
usan cuando la máquina no está disponible. Con la máquina real, **«será necesario disponer de un conjunto de
programas representativos de la carga real de trabajo que vaya a tener la máquina, y con respecto a los
cuales se realicen las medidas. Estos programas patrones se denominan benchmarks»**. Un *benchmark* es,
por tanto, un programa o conjunto de programas patrón con el que se mide y compara el rendimiento.

### Qué se mide

La métrica por excelencia es el tiempo, visto de dos maneras:

- **«tiempo de respuesta (response time)»**: lo que interesa al usuario, que quiere que su programa
  acabe antes. La fuente lo define como **«el tiempo necesario para completar una tarea, incluyendo los
  accesos al disco, a la memoria, las actividades de E/S y los gastos del S.O. Es el tiempo que percibe
  el usuario.»**
- **«productividad (throughput)»**: lo que interesa al responsable de un centro de cálculo, el número de
  trabajos por unidad de tiempo (**«Número de tareas ejecutadas en la unidad de tiempo»**).

Y en los dos casos, **«el procesador que realiza la misma cantidad de trabajo en el menor tiempo posible
será el más rápido, la diferencia estriba en si medimos una tarea (tiempo de respuesta) o muchas
(productividad).»**

El tiempo de CPU es otra cosa: **«Es el tiempo que tarda en ejecutarse un programa, sin tener en cuenta
el tiempo de espera debido a la E/S o el tiempo utilizado para ejecutar otros programas.»** Se divide en
tiempo de CPU del usuario y tiempo de CPU del sistema operativo.

Dos métricas clásicas, con sus fórmulas en la fuente:

| Métrica | Fórmula | Problema que señala la fuente |
|---|---|---|
| MIPS, millones de instrucciones por segundo | Número de instrucciones / (tiempo de ejecución · 10⁶) | **«Los MIPS dependen del repertorio de instrucciones, por lo que resulta un parámetro difícil de utilizar para comparar máquinas con diferente repertorio»**; **«Varían entre programas ejecutados en el mismo computador»**; y pueden variar al revés que el rendimiento: una máquina con hardware de coma flotante tarda menos pero da menos MIPS, porque ejecuta menos instrucciones |
| MFLOPS, millones de operaciones en coma flotante por segundo | Número de operaciones en coma flotante de un programa / (tiempo de ejecución · 10⁶) | Hay operaciones rápidas (suma) y lentas (división); por eso se usan MFLOPS normalizados, con peso 1 para suma, resta, comparación y multiplicación, 4 para división y raíz cuadrada y 8 para exponenciación y trigonométricas |

La conclusión de la fuente sobre los MIPS: **«los MIPS pueden fallar al dar una medida del rendimiento,
puesto que no reflejan el tiempo de ejecución.»** Para resumir varios resultados normalizados frente a
una máquina de referencia se usa la media geométrica (**«Se utiliza con medidas de rendimiento
normalizadas con respecto a una máquina de referencia.»**).

### Tipos de benchmark

La fuente clasifica las pruebas con dos criterios **«no excluyentes»**.

**Por el ámbito de aplicación** (el tipo de recurso que más interviene):

| Tipo | Definición (literal) | Ejemplo de la fuente |
|---|---|---|
| Enteros | **«aplicaciones en las que domina la aritmética entera, incluyendo procedimientos de búsqueda, operaciones lógicas, etc.»** | SPECint2000 |
| Punto flotante | **«aplicaciones intensivas en cálculo numérico con reales.»** | SPECfp2000 y LINPACK |
| Transacciones | **«aplicaciones en las que dominan las transacciones on-line y off-line sobre bases de datos.»** | TPC-C |

**Por la naturaleza del programa**:

| Tipo | Definición (literal) | Ejemplos de la fuente |
|---|---|---|
| Programas reales | **«Compiladores, procesadores de texto, etc. Permiten diferentes opciones de ejecución. Con ellos se obtienen las medidas más precisas»** | — |
| Núcleos (*kernels*) | **«Trozos de programas reales. Adecuados para analizar rendimientos específicos de las características de una determinada máquina»** | Linpack, Livermore Loops |
| Patrones conjunto (*benchmark suites*) | **«Conjunto de programas que miden los diferentes modos de funcionamiento de una máquina»** | SPEC y TPC |
| Patrones reducidos (*toy benchmarks*) | **«Programas reducidos (10-100 líneas de código) y de resultado conocido.»** | Quicksort |
| Patrones sintéticos (*synthetic benchmarks*) | **«Código artificial no perteneciente a ningún programa de usuario y que se utiliza para determinar perfiles de ejecución.»** | Whetstone, Dhrystone |

Tres de estos ejemplos, en la fuente:

- **LINPACK**: **«Es una colección de subrutinas Fortran que analizan y resuelven ecuaciones lineales y
  problemas de mínimos cuadrados.»** Da el resultado en Mflops/s.
- **SPEC**: **«SPEC es una sociedad sin ánimo de lucro cuya misión es establecer, mantener y distribuir
  un conjunto estandarizado de benchmarks»**. Sus resultados se calculan como cocientes frente a una
  máquina de referencia.
- **TPC**: un consorcio de fabricantes de *software* y *hardware* que diseña pruebas de procesamiento
  de transacciones, es decir, **«accesos de consulta y actualización a bases de datos»**. La fuente
  añade que sus pruebas son caras y largas y, en 2010, que TPC-A, TPC-B y TPC-C **«ya están en
  desuso»**, aunque siga poniendo TPC-C como ejemplo de prueba de transacciones.

La fuente es de 2010-11 y da SPEC2006 como **«la última en vigor»**. Lo vigente se lee en SPEC.

### SPEC CPU hoy

La Standard Performance Evaluation Corporation publica en su web (consultada el 05-10-2026) dos
generaciones de su prueba de procesador:

- **SPEC CPU 2026**: **«The SPEC CPU 2026 benchmark package contains 52 benchmarks, organized into four
  suites»**. Las cuatro: **«The SPECspeed® 2026 Integer and SPECspeed® 2026 Floating Point suites are
  used for comparing time for a computer to complete single tasks. The SPECrate® 2026 Integer and
  SPECrate® 2026 Floating Point suites measure the throughput or work per unit of time.»** SPECspeed
  mide, pues, tiempo de respuesta, y SPECrate, productividad: la misma pareja de la fuente
  universitaria, y la misma división entre enteros y coma flotante. Las cargas de trabajo se
  desarrollan **«from real user applications»** y la prueba **«also includes an optional metric for
  measuring energy consumption.»** Se distribuye como código fuente que hay que compilar.
- **SPEC CPU 2017** (43 pruebas en cuatro conjuntos con la misma estructura) se retira con la salida de
  la 2026: **«On November 3, 2026 03:00 AM US Eastern Time, SPEC will stop accepting SPEC CPU 2017
  results for publication. By end of day on November 17, 2026 US Eastern Time, SPEC will retire SPEC
  CPU 2017.»** A la fecha del BOJA conviven las dos, con la 2017 en retirada. La salida de la 2026 la
  anunció SPEC en nota de prensa de 5 de mayo de 2026 (**«SPEC Releases the SPEC CPU 2026 Benchmark
  Suites to Address the Latest Advances in CPU, Memory, and Compiler Technology (05/05/2026)»**).

### Pruebas del puesto de usuario

Las pruebas que un operador usa en un puesto de trabajo son programas comerciales o gratuitos de
fabricantes concretos. Los de este epígrafe son ejemplos, cada uno con lo que dice su web; su
encaje en la clasificación anterior es del tema.

| Herramienta | Qué mide (literal de su web) | Tipo |
|---|---|---|
| Cinebench 2026 (Maxon) | **«Cinebench 2026 utilizes the power of Redshift, Cinema 4D's default rendering engine, to evaluate your computer's CPU and GPU capabilities»**; **«Cinebench offers a real-world benchmark»** | Procesador y gráfica con un programa real (motor de render) |
| 3DMark (UL) | **«3DMark includes everything you need to benchmark gaming performance in one app.»**; **«3DMark helps you relate your score to real-world game performance by estimating the frame rates you can expect»**; incluye pruebas de estrés | Gráfica 3D; conjunto de pruebas y estrés |
| PerformanceTest (PassMark) | **«Compare the performance of your PC to similar computers around the world.»**; **«Measure the effect of configuration changes and hardware upgrades.»**; conjuntos de CPU, gráficos 2D y 3D, discos y memoria; en disco, **«sequential read, sequential write, random seek read+write and IOPS measurements»** | Equipo completo; conjunto de pruebas, comparación con una base de referencias |
| CrystalDiskMark (Crystal Dew World) | **«CrystalDiskMark is a simple disk benchmark software.»**; **«Measure Sequential and Random Performance (Read/Write/Mix)»** | Almacenamiento |
| `winsat mem` (Windows) | **«The winsat mem command tests system memory bandwidth using a process similar to the large memory-to-memory buffer copies in multimedia processing.»** | Memoria; integrado en el sistema |

Detalles que pueden preguntarse:

- CrystalDiskMark avisa de que **«A part of SSDs depend on test data(random, 0fill).»**: el resultado de
  algunas SSD cambia según los datos de prueba sean aleatorios o ceros.
- `winsat mem` exige pertenecer al grupo Administradores local y un símbolo del sistema elevado.
  Ejemplo de Microsoft: `winsat mem -mint 4.0 -maxt 12.0 -buffersize 32MB -xml memtest.xml` (al menos 4
  segundos, como mucho 12, búfer de 32 MB y resultado en XML).
- PassMark comercializa aparte BurnInTest, que presenta como **«PC Reliability and Load Testing»**.

### Prueba de rendimiento y prueba de estrés

Las dos se parecen, pero buscan cosas distintas, y las fuentes lo muestran:

- La prueba de rendimiento da una cifra para comparar: con otros equipos, con el mismo equipo antes y
  después de un cambio de configuración o de pieza (PassMark), con una máquina de referencia (SPEC).
- La prueba de estrés o de carga mantiene el equipo al máximo para ver si aguanta: UL la recomienda
  tras montar un equipo, cambiar la gráfica o forzar su frecuencia, para detectar hardware averiado o
  falta de refrigeración (epígrafe 4).

En el diagnóstico, la prueba de rendimiento sirve para la avería de «el equipo va lento»: un resultado
muy por debajo del de equipos iguales apunta a un problema; la de estrés, para los fallos que sólo
salen con carga. Esta distinción de uso es oficio, apoyada en las citas de PassMark y de UL.

### Ejercicio de aplicación

**Tiempos.** La fuente universitaria da este ejemplo con la orden `time` de Unix, que devuelve `90.7u
12.9s 2:39 65%`:

- Tiempo de CPU del usuario: 90,7 s. Tiempo de CPU del sistema: 12,9 s.
- Tiempo de CPU: 90,7 + 12,9 = 103,6 s.
- Tiempo de respuesta: 2 min 39 s = 159 s.
- La CPU ocupa el 65 % del tiempo de respuesta (159 · 0,65 = 103,6 s); el 35 % restante (159 · 0,35
  = 55,6 s) es espera de E/S o ejecución de otras tareas.

**MIPS y MFLOPS** (cálculo propio con las fórmulas de la fuente). Un programa ejecuta 600 millones de
instrucciones en 2 segundos, de las que 50 millones son operaciones en coma flotante:

- MIPS = 600 · 10⁶ / (2 · 10⁶) = 300.
- MFLOPS = 50 · 10⁶ / (2 · 10⁶) = 25.

Si otra máquina con un repertorio distinto ejecuta el mismo programa en 1,5 segundos pero con 300
millones de instrucciones, da 200 MIPS y, sin embargo, es más rápida: es el defecto de los MIPS que
señala la fuente, porque no reflejan el tiempo de ejecución.

## Lo que este tema no da, y dónde está

- **Mantenimiento preventivo**: limpieza, ventilación, cambio de pasta térmica, calendario de revisiones
  y actualización de BIOS y controladores como rutina. No se ha leído en fuente de fabricante; sólo
  constan los apuntes del epígrafe 1.
- **Códigos de otros fabricantes**: el significado de cada combinación de pitidos del modelo HP Desktop
  Pro A (sí se dan los del ProDesk 600 G5); las tablas de Dell (la página del fabricante no se dejó
  descargar), Award y Phoenix; los códigos de POST de UEFI y los visores de código de las placas de
  consumo.
- **Textos de los mensajes de BIOS** con la redacción de los manuales de oficio («CMOS checksum error»,
  «No boot device»): no se han leído en fuente de fabricante; se dan los de HP.
- **Diagnóstico de memoria de Windows** (`mdsched.exe`): el detalle de sus opciones consta sólo en una
  fuente archivada escrita para Windows 7; no se ha leído una página vigente para Windows 11.
- **Análisis de volcados** con WinDbg más allá de `!analyze -v`, y el significado de cada código de
  detención (la referencia de Microsoft está escrita para programadores).
- **Síntomas físicos de un disco mecánico** (ruidos, golpeteo) y la pulsera antiestática: oficio sin
  fuente leída.
- **Copia, clonación y recuperación de datos** del disco averiado: tema 3. **Conectores y cableado**
  (RJ45, USB, vídeo): tema 4. **Herramientas de Windows** en general (Visor de eventos, gestión de
  discos, controladores, puntos de restauración): tema 6. **Redes** y diagnóstico de la conexión más
  allá de `ipconfig` y `ping`: tema 13.
- **Prevención de riesgos** al manipular equipos (riesgo eléctrico, pantallas de visualización): tema 16.
- **Los equipos, contratos de mantenimiento y procedimientos de soporte de la RTVA y de CSRTV**: no
  constan en ningún documento publicado.

## Trazabilidad

| Fuente | Qué sostiene | Leída |
|---|---|---|
| American Megatrends, *AMIBIOS8 Check Point and Beep Code List*, versión 2.0, 10-06-2008 (documento público) | Puntos de control, puerto 80h, tarjeta POST, bloque de arranque, puntos 04, 2C, 3B, 84, 85, 87 y 00, pitidos del POST y del bloque de arranque, método de aislamiento, historial de revisiones (códigos suprimidos), límites del documento | 05-10-2026 |
| HP, *Interactive Beep and LED Diagnostic*, HP Desktop Pro A G2/G3 Series | Cuatro familias de pitidos y sus combinaciones | 05-10-2026 |
| HP, *Maintenance and Service Guide HP ProDesk 600 G5 SFF*, 3.ª ed., septiembre de 2019 (h10032.www1.hp.com, c06442415) | Equipo que no enciende y fuente que no arranca, protección térmica, códigos mayor y menor de pitidos y parpadeos, mensajes numerados del POST | 06-10-2026 |
| Lenovo, *M920s User Guide and Hardware Maintenance Manual*, 2.ª ed., agosto de 2019 (download.lenovo.com) | FRU y CRU, reglas antes de cambiar una FRU, electricidad estática, procedimientos de sustitución (disco, memoria, tarjeta PCIe, Wi-Fi, pila, fuente de alimentación), cierre, pila de la CMOS y su mensaje de error, advertencia de la fuente, potencias de fuente, ranuras y conectores | 05-10-2026 (fuente de alimentación y pila, releídas el 06-10-2026) |
| smartmontools, página de manual `smartctl(8)` (rama master, GitHub) | SMART, `-H`, `-A`, atributos y columnas, tipos *Pre-fail* y *Old age*, WHEN_FAILED, autopruebas y su duración, NVMe, `-l ssd`, ejemplos | 05-10-2026 |
| Microsoft Learn, «chkdsk» (actualizada el 26-05-2025) | Parámetros, permisos, volumen en uso, cadenas perdidas, HDD y SSD, códigos de salida, registro en el Visor de eventos, uso ocasional | 05-10-2026 |
| Microsoft Learn, «sfc» (01-11-2024) | `sfc`, `/scannow`, `/verifyonly`, permisos | 05-10-2026 |
| Microsoft Learn, «Device Manager Error Messages», «Device Manager Problem Codes» (15-12-2021) y páginas de los códigos 10 (15-12-2021), 22 (14-03-2023), 28 y 43 (15-12-2021) | Exclamación amarilla, `Cfg.h`, códigos y sus mensajes y soluciones, DNF y los otros tres casos del código 28, caso de la actualización | 05-10-2026 (código 28, releído el 06-10-2026) |
| Microsoft Learn, «PnPUtil Command Syntax» (08-01-2024) | PnPUtil y sus órdenes | 05-10-2026 |
| Microsoft Learn, «WDDM support for timeout detection and recovery» (05-11-2025) | TDR, dos segundos, recuperación, parpadeo y mensaje | 05-10-2026 |
| Microsoft Learn, «ipconfig» (03-02-2023) y «ping» (01-11-2024) | Órdenes de diagnóstico de red | 05-10-2026 |
| PassMark, MemTest86: «Troubleshooting Memory Errors» e «Individual Test Descriptions» | Pruebas de memoria, martilleo, interpretación de errores, localización del módulo, remedios | 05-10-2026 |
| Universidad Complutense de Madrid, Facultad de Informática, *Estructura de Computadores*, tema 4, «Rendimiento del procesador», curso 2010-11 | Técnicas de evaluación, definición de benchmark, tiempo de respuesta y productividad, tiempo de CPU, MIPS, MFLOPS, media geométrica, clasificaciones, LINPACK, SPEC, TPC, ejemplo de `time` | 05-10-2026 |
| SPEC, páginas «SPEC CPU 2026» y «SPEC CPU 2017» (aviso de retirada actualizado el 28-07-2026) | Conjuntos, número de pruebas, SPECspeed y SPECrate, energía, nota de prensa de 05-05-2026, retirada de la 2017 | 05-10-2026 (nota de prensa, releída el 06-10-2026) |
| Maxon, «Cinebench»; UL, «3DMark»; PassMark, «PerformanceTest»; Crystal Dew World, «CrystalDiskMark» | Qué mide cada herramienta; pruebas de estrés | 05-10-2026 |
| Microsoft Learn, «winsat mem» (04-05-2023) | Prueba de ancho de banda de memoria, permisos, ejemplo | 05-10-2026 |
| Microsoft Learn, «Bug checks (stop code errors)» (23-07-2025), «Bug check code reference» (15-07-2025) y «Advanced troubleshooting for stop code errors» (12-02-2026); Microsoft Support, «Troubleshooting Windows unexpected restarts and stop code errors» (28-07-2026) | Definición y nombres de la pantalla azul, código y módulo, códigos citados, causas en porcentaje, pasos básicos y tabla por escenarios, Diagnóstico de memoria de Windows y su resultado en el Visor de eventos, volcados y su ubicación, DumpChk, WinDbg | 06-10-2026 |
| Microsoft, TechNet Magazine, «Run Diagnostics to Check Your System for Memory Problems» (contenido archivado de *previous versions*, escrito para Windows 7) | `mdsched.exe`, reinicio, mezclas de prueba, F1 y F10, resultado al iniciar sesión | 06-10-2026 |
| NVM Express, *NVM Express Base Specification*, revisión 2.1, 05-08-2024, § 5.1.12.1.3 y figura 206 | Página de salud NVMe: *Critical Warning*, reserva disponible y su umbral, porcentaje usado y su salvedad, temperatura, contadores, errores de integridad | 06-10-2026 |

La sigla CRC se desarrolla según el manual de gzip (leído el 06-10-2026). Las fuentes de
fabricante están en inglés: las citas van en negrita en su lengua y la explicación en
castellano es del tema. La de la Universidad Complutense está en castellano y se cita tal cual.

Oficio sin fuente detrás, y así se declara: la ordenación de las averías por el momento en que
aparecen y la tabla del epígrafe 2 (cada fila remite a su fuente); la lectura de que un aviso aislado
de TDR no es por sí una avería; el encaje de cada herramienta del puesto en la clasificación de la
fuente universitaria; la distinción de uso entre prueba de rendimiento y de estrés. Es cálculo, y se
puede rehacer: el ejercicio de MIPS y MFLOPS.
