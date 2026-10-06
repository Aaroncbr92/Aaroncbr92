# Tema 6 del específico de Operador/a Informático · Sistema operativo Windows 11

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 6 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Documentación oficial de Microsoft: Microsoft Learn (Windows 11, implementación de Windows, Windows Server en lo que se aplica a Windows 11, referencia de órdenes de Windows, PowerShell, Intune) y el sitio de soporte de Microsoft (support.microsoft.com), en castellano. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las páginas vivas de Microsoft, leídas el 05-10-2026 (las de configuración de inicio, cuentas y Windows Hello, el 06-10-2026). Versión de referencia: Windows 11 25H2, la última actualización de características para equipos existentes a la fecha del BOJA (24-09-2026); la 26H2 se publicó el 29-09-2026 |
| Extensión | 19.000 palabras aproximadamente, tablas incluidas |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); sistema operativo (SO);
interfaz de firmware extensible unificada (UEFI, *unified extensible firmware interface*) y su
predecesor, el sistema básico de entrada y salida (BIOS, *basic input/output system*); módulo de
compatibilidad que emula la BIOS (CSM, *compatibility support module*); módulo de plataforma segura
(TPM, *trusted platform module*); tabla de particiones GUID (GPT, *GUID partition table*), donde GUID
es el identificador único global (*globally unique identifier*); registro de arranque maestro (MBR,
*master boot record*); partición del sistema EFI (ESP, *EFI system partition*), donde EFI es la
interfaz de firmware extensible (*extensible firmware interface*); partición reservada de Microsoft
(MSR, *Microsoft reserved partition*); sistema de archivos de nueva tecnología (NTFS) y tabla de
asignación de archivos de 32 bits (FAT32); unidad de estado sólido (SSD, *solid-state drive*) y
NVMe, la interfaz de memoria no volátil exprés (*non-volatile memory express*); entorno de
preinstalación de Windows (Windows PE o WinPE); entorno de recuperación de Windows (Windows RE o
WinRE); experiencia de primer arranque (OOBE, *out-of-box experience*); kit de evaluación e
implementación de Windows (Windows ADK); administración y mantenimiento de imágenes de implementación
(DISM); herramienta de migración de estado de usuario (USMT); administrador de imágenes del sistema
de Windows (Windows SIM); herramienta de administración de activación por volumen (VAMT); servicios
de implementación de Windows (WDS); servicios de actualización de Windows Server (WSUS); entorno de
ejecución previo al arranque por red (PXE, *preboot execution environment*); administración de
dispositivos móviles (MDM) y de aplicaciones móviles (MAM); trae tu propio dispositivo (BYOD, *bring
your own device*); proveedor de servicios de configuración (CSP, *configuration service provider*),
la interfaz por la que MDM configura Windows; objeto de directiva de grupo (GPO, *group policy
object*); Servicios de dominio de Active Directory (AD DS); controlador de dominio (DC); unidad
organizativa (UO, en inglés OU); extensión del lado cliente (CSE, *client-side extension*); consola de
administración de directivas de grupo (GPMC); conjunto resultante de directivas (RSoP, *resultant set
of policy*); consola de administración de Microsoft (MMC); instrumental de administración de Windows
(WMI); control de cuentas de usuario (UAC, *user account control*); sistema de cifrado de archivos
(EFS, *encrypting file system*); acceso directo a memoria (DMA, *direct memory access*); convención de
nomenclatura universal (UNC, *universal naming convention*); el instalador de Windows (Windows
Installer), cuyos paquetes llevan la extensión `.msi`; protocolo de configuración dinámica de host
(DHCP); sistema de nombres de dominio (DNS) y su variante cifrada, DNS sobre HTTPS (DoH), donde HTTPS
es el protocolo seguro de transferencia de hipertexto; protocolo de Internet (IP), en sus versiones 4 y 6
(IPv4, IPv6); protocolo de control de transmisión y protocolo de Internet (TCP/IP); protocolo de
datagramas de usuario (UDP); protocolo de mensajes de control de Internet (ICMP); período de vida
(TTL, *time to live*); dirección de control de acceso al medio (MAC); protocolo de escritorio remoto
(RDP); identificador de proceso (PID); intérprete seguro de órdenes (SSH, *secure shell*) y su
protocolo de transferencia de archivos (SFTP); protección antimalware de inicio anticipado (ELAM,
*early launch antimalware*); unidad central de proceso (CPU); ordenador personal (PC); bus serie universal (USB); red privada
virtual (VPN); código de respuesta rápida (QR); inteligencia artificial (IA); el archivo de imagen ISO, que según
Microsoft sirve para máquinas virtuales o para grabar un DVD; el modelo de controlador de pantalla de
Windows (WDDM); la interfaz de prueba de seguridad de hardware (HSTI); el formato de paquete de
aplicación MSIX; la carpeta SYSVOL de los controladores de dominio, que se cita por su nombre; y
nombres de producto que se citan como tales: Microsoft Entra ID (el servicio de Microsoft en el que,
dice la documentación de Intune, se ejecuta la identidad), .NET y Windows NT. Y los nombres de
orden y de ruta, que van en acentos graves porque son código. «Win» es la tecla del logotipo de
Windows.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 6): «Sistema operativo Windows
> 11: instalación del cliente Windows, interfaz y aplicaciones, gestión de discos y controladores,
> conectividad de red, protección y recuperación del sistema, configuración de la seguridad, centro de
> notificaciones, personalización, configuración básica y avanzada, partición de recuperación, panel
> de configuración, modo desarrollador, políticas de grupo —GPO—, puntos de restauración y opciones
> de reinicio para instalar actualizaciones.»

Qué se puede preguntar: qué versión de Windows 11 está vigente, con qué cadencia salen las
actualizaciones de características y cuánto soporte tienen; los requisitos mínimos de hardware
(procesador, memoria, almacenamiento, UEFI con arranque seguro, TPM 2.0) y desde qué Windows 10 se
puede actualizar; las formas de instalar (Windows Update, Asistente de instalación, medios de
instalación, instalación limpia) y qué se conserva en cada una; el diseño de particiones en UEFI/GPT
(ESP en FAT32, MSR de 16 MB, Windows en NTFS, recuperación justo detrás); las herramientas de
despliegue (DISM, USMT, Windows SIM, Windows PE, WDS, WSUS, Autopilot, Intune); el menú Inicio, la
barra de tareas, Acoplar y los atajos de teclado; cómo se instalan y desinstalan aplicaciones y qué
es un paquete `.msi`; Administración de discos, GPT frente a MBR, discos básicos y dinámicos,
`diskpart`; cómo se actualiza, revierte o reinstala un controlador; cómo se configura la IP, el DNS,
el perfil de red pública o privada y qué hacen `ipconfig`, `ping`, `tracert` y `netstat`; qué es
una ruta UNC; WinRE, sus herramientas y cuándo arranca solo; la Configuración de inicio y las variantes del modo seguro; Restablecer este PC, Restaurar sistema,
la restauración a un momento dado y la unidad de recuperación; la aplicación Seguridad de Windows,
BitLocker, el cifrado de dispositivo y el UAC; los tipos de cuenta, cómo se crea una cuenta local, las
cuentas integradas Administrador e Invitado y Windows Hello; el centro de notificaciones y No molestar; temas y
colores; la aplicación Configuración frente al Panel de control y las consolas `.msc`; el modo
desarrollador; qué es un GPO, en qué orden se procesa, cada cuánto se refresca y qué hacen
`gpupdate` y `gpresult`; las horas activas y el reinicio mensual único. En la aplicación práctica:
elegir la herramienta o la ruta de menú para una tarea, leer la salida de una orden de red,
decidir qué opción de recuperación conserva qué y predecir qué GPO gana en un conflicto.

<!-- indice -->

## Índice

- [Antes de empezar: qué Windows 11 se estudia](#antes-de-empezar-qué-windows-11-se-estudia)
- [1. Instalación del cliente Windows](#1-instalación-del-cliente-windows)
  - [Requisitos de hardware y de partida](#requisitos-de-hardware-y-de-partida)
  - [UEFI, arranque seguro y GPT](#uefi-arranque-seguro-y-gpt)
  - [Las formas de instalar](#las-formas-de-instalar)
  - [El despliegue en una organización](#el-despliegue-en-una-organización)
- [2. Interfaz y aplicaciones](#2-interfaz-y-aplicaciones)
  - [La barra de tareas](#la-barra-de-tareas)
  - [El menú Inicio](#el-menú-inicio)
  - [Las ventanas: Acoplar y los escritorios](#las-ventanas-acoplar-y-los-escritorios)
  - [Los atajos de teclado de uso general](#los-atajos-de-teclado-de-uso-general)
  - [El Explorador de archivos](#el-explorador-de-archivos)
  - [Instalar, desinstalar y arrancar aplicaciones](#instalar-desinstalar-y-arrancar-aplicaciones)
- [3. Gestión de discos y controladores](#3-gestión-de-discos-y-controladores)
  - [Administración de discos](#administración-de-discos)
  - [GPT y MBR](#gpt-y-mbr)
  - [Discos básicos y dinámicos](#discos-básicos-y-dinámicos)
  - [`diskpart`, la gestión de discos desde la consola](#diskpart-la-gestión-de-discos-desde-la-consola)
  - [Optimizar unidades](#optimizar-unidades)
  - [Controladores](#controladores)
- [4. Conectividad de red](#4-conectividad-de-red)
  - [La página Red e Internet](#la-página-red-e-internet)
  - [Red pública o privada](#red-pública-o-privada)
  - [La configuración TCP/IP](#la-configuración-tcpip)
  - [Las órdenes de red](#las-órdenes-de-red)
  - [Las rutas de red (UNC)](#las-rutas-de-red-unc)
- [5. Protección y recuperación del sistema](#5-protección-y-recuperación-del-sistema)
  - [El entorno de recuperación (WinRE)](#el-entorno-de-recuperación-winre)
  - [La configuración de inicio y el modo seguro](#la-configuración-de-inicio-y-el-modo-seguro)
  - [Las opciones de recuperación, de menos a más drásticas](#las-opciones-de-recuperación-de-menos-a-más-drásticas)
  - [La recuperación rápida de equipo](#la-recuperación-rápida-de-equipo)
  - [Prepararse antes de que falle](#prepararse-antes-de-que-falle)
- [6. Configuración de la seguridad](#6-configuración-de-la-seguridad)
  - [La aplicación Seguridad de Windows](#la-aplicación-seguridad-de-windows)
  - [BitLocker y el cifrado de dispositivo](#bitlocker-y-el-cifrado-de-dispositivo)
  - [El control de cuentas de usuario (UAC)](#el-control-de-cuentas-de-usuario-uac)
  - [Las cuentas de usuario del equipo y el inicio de sesión](#las-cuentas-de-usuario-del-equipo-y-el-inicio-de-sesión)
- [7. Centro de notificaciones](#7-centro-de-notificaciones)
- [8. Personalización](#8-personalización)
- [9. Configuración básica y avanzada](#9-configuración-básica-y-avanzada)
  - [La aplicación Configuración](#la-aplicación-configuración)
  - [Las herramientas avanzadas](#las-herramientas-avanzadas)
  - [Los servicios y sus dependencias](#los-servicios-y-sus-dependencias)
- [10. Partición de recuperación](#10-partición-de-recuperación)
  - [El diseño de particiones de un equipo UEFI](#el-diseño-de-particiones-de-un-equipo-uefi)
  - [La partición de recuperación](#la-partición-de-recuperación)
- [11. Panel de configuración: Configuración y Panel de control](#11-panel-de-configuración-configuración-y-panel-de-control)
- [12. Modo desarrollador](#12-modo-desarrollador)
- [13. Políticas de grupo (GPO)](#13-políticas-de-grupo-gpo)
  - [Qué son](#qué-son)
  - [Dónde se vinculan y en qué orden se aplican](#dónde-se-vinculan-y-en-qué-orden-se-aplican)
  - [Cuándo se aplican](#cuándo-se-aplican)
  - [`gpupdate` y `gpresult`](#gpupdate-y-gpresult)
  - [Ejemplos en Windows 11](#ejemplos-en-windows-11)
- [14. Puntos de restauración](#14-puntos-de-restauración)
  - [Protección del sistema](#protección-del-sistema)
  - [Restaurar sistema](#restaurar-sistema)
  - [La restauración a un momento dado (restauración puntual)](#la-restauración-a-un-momento-dado-restauración-puntual)
- [15. Opciones de reinicio para instalar actualizaciones](#15-opciones-de-reinicio-para-instalar-actualizaciones)
  - [Lo que ve el usuario](#lo-que-ve-el-usuario)
  - [Un reinicio al mes](#un-reinicio-al-mes)
  - [Lo que configura el administrador](#lo-que-configura-el-administrador)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Antes de empezar: qué Windows 11 se estudia

El enunciado dice «Windows 11» sin versión. Microsoft publica una actualización de características al
año: **«Windows 11 tiene una cadencia de actualización de características anual. Las actualizaciones
de características se publican en la segunda mitad del año natural y cuentan con 24 meses de soporte
técnico para las ediciones Home, Pro, Pro for Workstations y Pro Education. 36 meses de soporte
técnico para las ediciones Enterprise y Education.»** Además, **«Windows 11 también publica
actualizaciones de seguridad mensuales el segundo martes de cada mes. Estas versiones son
acumulativas y contienen todas las actualizaciones anteriores»**.

Las versiones del canal de disponibilidad general, según la página de información de versiones de
Microsoft (fechas en formato año-mes-día):

| Versión | Disponible desde | Fin de actualización Home, Pro, Pro Education y Pro for Workstations | Fin de actualización Enterprise, Education, IoT Enterprise y Enterprise multisesión | Compilación |
|---|---|---|---|---|
| 26H2 | 2026-09-29 | 2028-10-10 | 2029-10-09 | 26300 |
| 26H1 | 2026-02-10 | 2028-03-14 | 2029-03-13 | 28000 |
| 25H2 | 2025-09-30 | 2027-10-12 | 2028-10-10 | 26200 |
| 24H2 | 2024-10-01 | 2026-10-13 | 2027-10-12 | 26100 |
| 23H2 | 2023-10-31 | ya finalizado | 2026-11-10 | 22631 |

La 26H1 no es para los equipos que ya están en uso: **«Windows 11, versión 26H1 tiene como ámbito
admitir nuevos dispositivos que empezaron a comercializarse a principios de 2026 y no está diseñado
como una actualización de características para dispositivos existentes.»** De ahí la decisión del
tema: el 24-09-2026, fecha del BOJA, la última versión para equipos existentes era la 25H2; el
29-09-2026 salió la 26H2. El tema describe Windows 11 tal como lo documenta Microsoft hoy, y
cuando una característica depende de la versión lo dice. Las novedades propias de la 26H2 no se han
estudiado.

Dos datos de la 25H2 que se preguntan: **«Los dispositivos que se actualizan desde Windows 11,
versión 24H2, usan un paquete de habilitación.»**, y su soporte: **«Windows 11 Pro: atendida durante
24 meses a partir de la fecha de lanzamiento.»**; **«Windows 11 Empresas: atendida durante 36 meses a
partir de la fecha de lanzamiento.»** La rama de mantenimiento a largo plazo (LTSC, *long-term
servicing channel*) es aparte: **«Windows 11 Enterprise LTSC 2024 no dispone de soporte extendido.
Llegará a su fin de actualización (también llamado fin del mantenimiento) el 9 de octubre de 2029.»**

Por qué el temario ya no pide Windows 10: **«Windows 10 llegará al fin de soporte el 14 de octubre de
2025. La versión actual, 22H2, será la versión final de Windows 10»**. Desde entonces, dice el
soporte de Microsoft, **«Microsoft ya no proporcionará actualizaciones de software gratuitas desde
Windows Update, asistencia técnica ni correcciones de seguridad para Windows 10. El PC seguirá
funcionando, pero recomendamos que se cambie a Windows 11.»**

## 1. Instalación del cliente Windows

### Requisitos de hardware y de partida

**«Para instalar o actualizar a Windows 11, los dispositivos deben cumplir los siguientes requisitos
mínimos de hardware:»**

| Elemento | Requisito literal de Microsoft |
|---|---|
| Procesador | **«1 gigahercio (GHz) o más rápido con dos o más núcleos en un procesador o sistema compatible de 64 bits en un chip (SoC).»** |
| Memoria | **«4 gigabytes (GB) o superior.»** |
| Almacenamiento | **«64 GB o más de espacio disponible en disco.»** |
| Tarjeta gráfica | **«compatible con DirectX 12 o posterior, con un controlador WDDM 2.0.»** |
| Firmware | **«UEFI, compatible con arranque seguro.»** |
| TPM | **«módulo de plataforma segura (TPM) versión 2.0.»** |
| Pantalla | **«pantalla de alta definición (720p), monitor de 9" o superior, 8 bits por canal de color.»** |
| Internet | **«la conectividad a Internet es necesaria para realizar actualizaciones y para descargar y usar algunas características.»** |

SoC es *system on a chip*, sistema en un chip; WDDM es el modelo de controlador de pantalla de
Windows (*Windows Display Driver Model*). Y una regla de la edición doméstica: **«Windows 11 Home
edición requiere una conexión a Internet y una cuenta Microsoft para completar la configuración del
dispositivo en el primer uso.»**

Para actualizar directamente desde Windows 10, el equipo debe cumplir dos condiciones: **«Ejecución
de Windows 10, versión 2004 o posterior.»** e **«Instaló la actualización de seguridad del 14 de
septiembre de 2021 o posterior.»** Sobre el modo S, la variante restringida de Windows: **«El modo S
solo se admite en la edición Home de Windows 11.»**; y **«Si desactiva el modo S, no podrá volver al
modo S más adelante.»**

Algunas funciones piden más que el mínimo. Dos que tocan al puesto: **«BitLocker to Go: requiere una
unidad flash USB. Esta característica está disponible en Windows Pro y versiones posteriores.»** y
**«Cliente Hyper-V: requiere un procesador con capacidades de traducción de direcciones de segundo
nivel (SLAT). Esta característica está disponible en las ediciones de Windows Pro y versiones
posteriores.»**

En máquina virtual (**«Windows 11 también se admite en una máquina virtual (VM).»**) los requisitos
son: **«Generación: 2»**, con la advertencia de que **«No es posible actualizar localmente las
máquinas virtuales de generación 1 existentes a Windows 11.»**; 64 GB de disco, 4 GB de memoria, dos
procesadores virtuales y, en Hyper-V, **«arranque seguro y TPM habilitado.»** Microsoft añade que
**«El TPM virtual 2.0 se emula en la máquina virtual invitada independientemente de la versión o la
presencia del TPM del host de Hyper-V.»**

Para comprobar si un equipo con Windows 10 puede pasar a 11, Microsoft remite a la aplicación
**Comprobación de estado del PC** y avisa: **«No es recomendable instalar Windows 11 en un
dispositivo que no cumpla los requisitos.»**

### UEFI, arranque seguro y GPT

El requisito de firmware tiene consecuencias en el disco. Microsoft explica que UEFI **«Es el sucesor
del BIOS»** y que **«Windows 11 y versiones más recientes no admiten BIOS, por lo que solo se ejecuta
en dispositivos modernos que tienen UEFI.»** Además, **«Windows 11 y versiones más recientes solo
admiten versiones x64 de UEFI.»**

El arranque seguro: **«Cuando se usa el arranque seguro, UEFI garantiza que solo inicia un cargador
de sistema operativo comprobado y que el malware no puede cambiar el cargador de arranque.»** Y el
estilo de disco: **«Al implementar Windows en un dispositivo basado en UEFI, debes dar formato al
disco duro que incluye la partición de Windows mediante un sistema de archivos de tabla de
particiones GUID (GPT).»** (Microsoft lo llama «sistema de archivos», pero GPT es un estilo de
partición, no un sistema de archivos; véase el epígrafe 3.)

Un equipo antiguo que arrancaba en modo BIOS con disco MBR puede pasar a UEFI sin borrar el disco:
**«La herramientaMBR2GPT.EXE se puede usar para convertir el disco de MBR a GPT para su uso con UEFI
de forma no destructiva.»** [sic: «herramientaMBR2GPT», sin espacio]. La documentación de BitLocker lo
repite: **«El sistema operativo instalado en el hardware en modo heredado impide que el sistema
operativo arranque cuando se cambia el modo BIOS a UEFI. Use la herramienta mbr2gpt.exe antes de
cambiar el modo BIOS»**.

### Las formas de instalar

Microsoft distingue un método recomendado y otros. El recomendado para pasar de 10 a 11 es Windows
Update: **«Si se actualiza de Windows 10 a Windows 11, Microsoft recomienda esperar hasta que Windows
Update notifique que la actualización está lista para el dispositivo.»** Los demás:

| Método | Qué hace | Qué conserva |
|---|---|---|
| Windows Update | Ofrece la actualización cuando está lista para ese equipo; se pulsa Descargar e instalar y el equipo se reinicia varias veces | La página no lo detalla |
| Asistente de instalación de Windows 11 | **«es una aplicación que proporciona asistencia para actualizar a Windows 11.»** Microsoft recomienda esperar a que Windows Update ofrezca la actualización, aunque el Asistente se puede usar antes | La página no lo detalla |
| Medio de instalación ejecutado desde Windows (`setup.exe`) | Actualización «local» sobre el Windows que corre | A elegir en «Cambiar lo que se conserva»: archivos y aplicaciones (por defecto), sólo archivos o nada |
| Arrancar desde el medio de instalación | **«Este método borra completamente el contenido del disco duro y la instalación existente de Windows e instala una copia nueva de Windows 11.»** | Nada |

Las tres opciones de la actualización con `setup.exe`, en palabras de Microsoft: **«Conservar los
archivos personales y las aplicaciones: los archivos personales, las aplicaciones y la configuración
de Windows se conservan y migran a la nueva instalación de Windows 11. Esta es la opción
predeterminada.»**; **«Conservar solo los archivos personales: los archivos personales se conservan y
migran a la nueva instalación de Windows 11, pero se eliminan las aplicaciones y la configuración de
Windows.»**; y **«Nada : se eliminará todo, incluidos los archivos personales, las aplicaciones y la
configuración de Windows.»**

El medio de instalación: **«Los medios de instalación, como una unidad flash USB, se pueden usar
para instalar una nueva copia de Windows, realizar una instalación limpia de Windows o reinstalar
Windows.»** Se crea con la herramienta que se descarga del sitio de Microsoft: **«Se descarga la
herramienta MediaCreationTool.exe .»** Hace falta **«Una unidad flash USB vacía con al menos 8 GB de
espacio.»**; para máquinas virtuales basta un archivo ISO: **«se puede crear un archivo ISO para su
uso en máquinas virtuales (VM) o para grabar los medios de instalación en un DVD»**. Puede pedirse
**«una clave de producto de 25 caracteres (no es necesaria para las licencias digitales)»**, y
**«Muchos dispositivos modernos contienen la clave de producto incrustada en el firmware del
dispositivo.»**

La instalación limpia, paso a paso según el soporte de Microsoft: se arranca el equipo desde el
medio (el menú de arranque **«normalmente es una de las teclas de función (F1 - ,F12) de la parte
superior del teclado o la tecla SUPR»**, según fabricante); se eligen idioma y teclado; se marca
**«Instalar Windows 11»** y la casilla de que se borrará todo; si se pide clave y la licencia es
digital, **«No tengo una clave de producto»**; se elige la edición, que **«debe coincidir con la
licencia»** (**«si la edición actual de Windows es Home, Windows Home debe instalarse de nuevo.»**);
en la pantalla de ubicación, **«Elimine todas las particiones del Disco 0 que no aparecen como
Espacio sin asignar.»**, con la advertencia **«No modifiques ni borres las particiones en ningún
otro disco que no sea el disco 0.»**; se instala sobre el espacio sin asignar y se completa el
asistente. Una instalación limpia **«elimina todos los elementos siguientes»**: archivos personales,
aplicaciones, personalizaciones del fabricante y cambios de configuración.

Tras reinstalar hay que activar: **«Windows debe activarse después de reinstalarlo. Por lo general,
la activación se realiza automáticamente después de conectarse.»** Y un cambio grande de hardware
puede romperla: **«Si se vuelve a instalar Windows después de realizar un cambio de hardware
importante en el dispositivo (como reemplazar la placa base), es posible que ya no esté activado.»**

### El despliegue en una organización

Cuando hay que instalar decenas de puestos iguales no se va equipo por equipo. Microsoft agrupa las
herramientas en el **«Kit de evaluación e implementación de Windows (Windows ADK)»**:

| Herramienta | Para qué sirve |
|---|---|
| DISM | **«Se usa para capturar, reparar e implementar imágenes de arranque e imágenes de sistema operativo.»** |
| USMT | **«es una herramienta de copia de seguridad y restauración que le permite migrar el estado del usuario, los datos y la configuración de una instalación a otra.»** Sus dos órdenes: **«ScanState.exe: esta herramienta realiza la copia de seguridad de estado de usuario.»** y **«LoadState.exe: esta herramienta realiza la restauración de estado de usuario.»** |
| Windows SIM | **«es una herramienta de creación de archivos Unattend.xml»**, el archivo de respuestas de la instalación desatendida |
| Diseñador de configuraciones de Windows | **«es una herramienta diseñada para ayudar a crear paquetes de aprovisionamiento que se pueden usar para configurar dinámicamente un dispositivo Windows.»** |
| VAMT | Gestiona de forma centralizada claves de activación por volumen (MAK, *multiple activation key*) cuando no se usa el servicio de administración de claves (KMS, *Key Management Services*) |
| Windows PE | **«es una versión "lite" de Windows que se usa como plataforma de implementación.»** |

USMT migra de 32 a 64 bits, **«pero no al revés»**. Fuera del ADK, en el servidor: WDS, cuyas
funciones principales son **«Compatibilidad con el arranque PXE.»**, **«Multidifusión.»** y
**«Desbloqueo de red de BitLocker.»**; y WSUS, que **«es un rol de servidor en Windows Server que
habilita un repositorio local de actualizaciones de Microsoft.»**

La gestión moderna prescinde de la imagen. **«Windows Autopilot es un conjunto de tecnologías que se
utilizan para configurar y preconfigurar nuevos dispositivos, preparándolos para un uso
productivo.»** Parte del Windows que trae el equipo de fábrica: **«En lugar de volver a crear una
imagen del dispositivo, la instalación de Windows existente se puede transformar en un estado "listo
para empresas"»**, que puede aplicar configuraciones y directivas, instalar aplicaciones y cambiar de
edición, por ejemplo **«de Windows Pro a Windows Enterprise.»** Después, el equipo se administra con
Intune: **«Microsoft Intune es un servicio de administración de puntos de conexión basado en la nube
que protege y administra los dispositivos y aplicaciones de su organización.»** **«El servicio se
ejecuta completamente en la nube, sin que sea necesaria ninguna infraestructura local»**, y **«La
identidad se ejecuta en Microsoft Entra ID.»** Tiene dos modos:

- MDM: **«Intune luego administra todo el dispositivo, incluida la configuración, la seguridad y las
  aplicaciones. Si se pierde o se roba un dispositivo, puede borrarlo.»**
- MAM: **«Intune solo administra las aplicaciones de trabajo y los datos dentro de ellas, no el resto
  del dispositivo. MAM es habitual para dispositivos personales en escenarios de bring-your-own-device
  (BYOD)»**.

## 2. Interfaz y aplicaciones

### La barra de tareas

**«La barra de tareas de Windows es una parte central del sistema operativo Windows que te ayuda a
iniciar aplicaciones, cambiar entre ventanas abiertas y acceder a características del sistema como
notificaciones, búsqueda y el menú Inicio.»** Microsoft enumera seis componentes: **«1. Widgets»**,
**«2. Inicio»**, **«3. Buscar»**, **«4. Vista de tareas»**, **«5. Aplicaciones»** y **«6. Bandeja del
sistema»**.

| Componente | Qué es | Cómo se abre |
|---|---|---|
| Widgets | **«elementos interactivos que muestran contenido dinámico y proporcionan acceso rápido a diversas aplicaciones y características.»** Se pueden ocultar | Win + W |
| Inicio | **«un concentrador central que proporciona acceso rápido a las aplicaciones, la configuración y los archivos.»** No se puede quitar de la barra | Tecla Windows |
| Buscar | Busca archivos, aplicaciones, configuración y resultados web; el cuadro se puede mostrar entero, como icono con etiqueta, como icono o ocultar | Win + S |
| Vista de tareas | **«Le permite acceder rápidamente y administrar todas las ventanas abiertas y varios escritorios.»** | Win + Tab |
| Aplicaciones | Ancladas y abiertas; **«Las aplicaciones en ejecución se muestran en la barra de tareas con una línea debajo del icono para indicar que están abiertas.»** Con el botón secundario sobre un icono se abre su lista de accesos directos | — |
| Bandeja del sistema | Iconos de aplicaciones en segundo plano, Configuración rápida (red, volumen, batería), reloj y centro de notificaciones | Win + A (Configuración rápida), Win + N (notificaciones) |

Dos reglas que se preguntan: **«De manera predeterminada, la barra de tareas está centrada en
Windows 11.»**; y **«La configuración de la barra de tareas te permite alinear los iconos de la barra
de tareas en el centro o a la izquierda. No hay ninguna configuración para mover una barra de tareas
a la parte superior o lateral de la pantalla. La barra de tareas se coloca en la parte inferior de
la pantalla.»** La Configuración rápida tampoco se quita: **«Aunque no puedes quitar la configuración
rápida de la barra de tareas, puedes personalizarla moviendo y organizando los elementos»**. Todo se
ajusta con el botón secundario sobre la barra, **Configuración de la barra de tareas**.

### El menú Inicio

**«El menú Inicio de Windows es una característica clave del sistema operativo que proporciona acceso
rápido a las aplicaciones, la configuración y los archivos.»** La página de soporte dice que **«El
menú Inicio está organizado en seis áreas principales:»**, pero enumera siete: Búsqueda; Chinchetas
(los anclados, **«en formato de cuadrícula»**); Todas las aplicaciones (**«una lista alfabética de
todas las aplicaciones instaladas»**); Recomendaciones (**«aplicaciones agregadas recientemente y
usadas con frecuencia, además de archivos abiertos recientemente»**); Todas (vista por categoría,
cuadrícula o lista); Cuenta, con el botón de encendido que **«te permite bloquear, suspender, apagar
o reiniciar tu dispositivo»**; y Compañero de dispositivo móvil (el teléfono a través de Enlace
Móvil). Se ancla con el botón secundario, **«Anclar a Inicio»**; los anclados se agrupan en carpetas
arrastrando uno sobre otro, y **«Cuando solo queda un pin, la carpeta se quita del menú Inicio»**.

El botón Inicio tiene además un menú secundario (clic con el botón derecho, o Win + X, **«Abrir el
menú Vínculo rápido. Este acceso directo es la misma acción que hacer clic con el botón derecho en
el menú Inicio.»**) desde el que se abren, entre otros, Administración de discos, Administrador de
dispositivos, Administrador de tareas, Visor de eventos, Administración de equipos y Configuración,
como recogen las páginas de soporte citadas en los epígrafes siguientes.

### Las ventanas: Acoplar y los escritorios

**«La función Acoplar le permite cambiar rápidamente el tamaño y la posición de las ventanas en la
pantalla arrastrándolas a los bordes o esquinas.»** Con el ratón: **«Ajustar a un lado: arrastre una
ventana al borde izquierdo o derecho de la pantalla para acoplarla a ese lado.»**; **«Ajustar a la
esquina: Arrastra una ventana a una esquina para acoplarla a ese cuarto de la pantalla.»** Con el
teclado, la tecla Windows más una flecha. Los diseños predefinidos se abren pasando el puntero por el
botón de maximizar o con Win + Z (**«Abrir los diseños de ajuste.»**). Al acoplar una ventana,
**«el Asistente para el acoplamiento mostrará miniaturas de las otras ventanas abiertas»** para
rellenar el resto. Un dato de requisitos: **«Acoplar: los diseños de tres columnas requieren una
pantalla con un ancho de 1920 píxeles efectivos o más.»**

Los escritorios virtuales se gestionan desde la Vista de tareas; Win + Ctrl + D sirve para **«Crear
otro escritorio.»**

### Los atajos de teclado de uso general

De la página de métodos abreviados de teclado de Windows del soporte de Microsoft (que se aplica a
Windows 11 y 10):

| Combinación | Qué hace, literal |
|---|---|
| Ctrl + C / Ctrl + X / Ctrl + V | **«Copiar el texto seleccionado.»** / **«Cortar el texto seleccionado.»** / **«Pegar el último elemento del portapapeles.»** |
| Ctrl + Z | **«Deshacer la última escritura.»** |
| Alt + F4 | **«Cerrar la ventana activa.»** |
| Alt + Tabulador | **«Cambiar entre ventanas abiertas.»** |
| Ctrl + Mayús + Esc | **«Abra el administrador de tareas»** |
| F2 | **«Cambiar el nombre del elemento seleccionado.»** |
| Mayús + Suprimir | **«Eliminar permanentemente el elemento seleccionado sin moverlo a la papelera de reciclaje.»** |
| Win + D | **«Mostrar y ocultar el escritorio.»** |
| Win + E | **«Abre el Explorador de archivos.»** |
| Win + I | **«Abrir configuración.»** |
| Win + L | **«Bloquee el equipo.»** |
| Win + R | **«Abrir el cuadro de diálogo Ejecutar.»** |
| Win + V | **«Abra el historial del Portapapeles.»** (**«El historial del Portapapeles no está activado de forma predeterminada.»**) |
| Win + N | **«Abrir el centro de notificaciones y el calendario.»** |
| Win + A | **«Abra el Centro de actividades de Windows 11.»** (la página de la barra de tareas llama a lo mismo «Configuración rápida») |

### El Explorador de archivos

**«El Explorador de archivos de Windows te ayuda a encontrar, abrir, organizar y administrar archivos
y carpetas en tu PC y en la nube.»** Se abre desde la barra de tareas, el menú Inicio o Win + E. En
la cinta de opciones (así la llama la página de Windows 11) están **Ver** (iconos, listas, detalles) y **Compartir**; para
anclar una carpeta, botón secundario y **«Anclar a acceso rápido»**. Un cambio de la 22H2 que separa
Acceso rápido de Este equipo: **«A partir de Windows 11, versión 22H2, las carpetas conocidas de
Windows (escritorio, documentos, descargas, imágenes, música y vídeos) están disponibles de forma
predeterminada como carpetas ancladas en Acceso rápido tanto en el Inicio del Explorador de archivos
como en el panel de navegación izquierdo. Estas carpetas predeterminadas ya no se muestran en Este
equipo para mantener la vista centrada en las unidades y las ubicaciones de red»**.

Dos comportamientos de oficio que no han cambiado desde Windows 10: arrastrar dentro de la misma
unidad mueve; entre unidades distintas, copia. Es el comportamiento por defecto y la causa de la
mitad de los sustos. Y lo borrado de una unidad de red o de una memoria extraíble no pasa por la
papelera.

### Instalar, desinstalar y arrancar aplicaciones

Desinstalar tiene tres caminos, y Microsoft avisa de que **«algunas aplicaciones y programas están
integrados en Windows y no se pueden desinstalar»**:

1. Desde el menú Inicio: **Todas las aplicaciones**, botón secundario sobre la aplicación, **Desinstalar**.
2. Desde Configuración: **«Selecciona Inicio > Configuración > Aplicaciones > Aplicaciones instaladas .»**, y **Más > Desinstalar**. Pero **«En este momento, algunas aplicaciones no se pueden desinstalar de la aplicación Configuración.»**
3. Desde el Panel de control: **«Selecciona Programas > Programas y características.»**, y **Desinstalar** o **Desinstalar/Cambiar**.

Las aplicaciones que arrancan solas al iniciar sesión se activan o desactivan en Configuración >
Aplicaciones > Inicio o en el Administrador de tareas, que **«proporciona una vista más detallada,
incluido el impacto que tiene cada aplicación en el proceso de inicio.»**

El paquete `.msi` es el formato del instalador de Windows (Windows Installer), y su orden es
`msiexec`, que **«Proporciona los medios para instalar, modificar y realizar operaciones en Windows
Installer desde la línea de comandos.»** Sus opciones básicas:

| Opción | Qué hace |
|---|---|
| `/i` | **«Especifica la instalación normal.»** |
| `/x` | **«Desinstala el paquete.»** |
| `/quiet` | **«Especifica el modo silencioso, lo que significa que no se requiere ninguna interacción del usuario.»** |
| `/passive` | **«Especifica el modo desatendido, lo que significa que la instalación solo muestra una barra de progreso.»** |
| `/qn` | **«Especifica que no hay ninguna interfaz de usuario durante el proceso de instalación.»** |
| `/norestart` | **«Impide que el dispositivo se reinicie una vez completada la instalación.»** |

Ejemplo de Microsoft: `msiexec.exe /i "C:\example.msi"`. La misma página explica por qué existe el
modo sin interfaz: **«si va a implementar un paquete mediante la directiva de grupo, que no requiere
ninguna interacción del usuario, no debe haber ninguna interfaz de usuario implicada.»**. Por qué la distinción importa
al administrador: un `.msi` se puede instalar y desinstalar de forma uniforme en cientos de equipos;
un `.exe` hay que estudiarlo caso por caso. Ésa es la razón de que el despliegue corporativo prefiera
el primero. Las aplicaciones empaquetadas modernas usan otro formato, MSIX, que la documentación de
Microsoft nombra al hablar del modo desarrollador (epígrafe 12).

Instalar desde la línea de órdenes con WinGet, el administrador de paquetes que Windows 11 incluye
(`winget install`), se estudia en el tema 7.

## 3. Gestión de discos y controladores

### Administración de discos

**«Administración de discos es una herramienta integrada de Windows que te ayuda a administrar discos
y volúmenes. Puedes usarlo para inicializar nuevas unidades, crear y dar formato a volúmenes, cambiar
letras de unidad y extender o reducir volúmenes existentes.»** Se abre de cuatro maneras: botón
secundario sobre Inicio y **Administración de discos**; buscando **«Crear y formatear particiones de
disco duro»**; con Win + R y `diskmgmt.msc`; o dentro de **Administración de equipos** (`compmgmt.msc`),
en Almacenamiento. Y **«Administración de discos tiene el mismo aspecto y funciona en Windows 10 y
Windows 11. No hay diferencias de características entre las versiones.»**

En el disco principal se ven normalmente tres particiones: **«Disco local (C:)»**, que **«Almacena la
instalación del sistema operativo Windows»**; **«Sistema EFI»**, que **«Permite el proceso de inicio
(arranque) para el ordenador y el sistema operativo en ordenadores modernos.»**; y **«Recuperación»**,
que **«Almacena herramientas que admiten operaciones de recuperación de Windows cuando el equipo no
se inicia»** (epígrafe 10). Microsoft advierte de que la herramienta puede mostrar las particiones
EFI y de recuperación **«como 100 por ciento libre»** aunque están casi llenas, y que **«La práctica
recomendada es no modificar estas particiones de ninguna manera.»**

Las operaciones:

| Operación | Cómo, y qué hay que saber |
|---|---|
| Inicializar un disco nuevo | **«Al agregar un nuevo disco al equipo, el disco no está disponible inmediatamente en el Explorador de archivos de Windows. En primer lugar, debe inicializar el disco»**. Botón secundario, **Inicializar disco**, elegir estilo; si figura **Sin conexión**, antes **En línea**. **«El proceso de inicialización borra todos los datos del disco.»** Hace falta ser de **Operadores de copia de seguridad** o **Administradores** |
| Crear un volumen | Botón secundario sobre el espacio sin asignar, **Nuevo volumen simple**: tamaño en MB, letra, sistema de archivos (**«normalmente NTFS»**). Exige iniciar sesión como administrador y **«debe haber espacio sin asignar o espacio libre en una partición extendida del disco duro.»** |
| Formatear | **«Al formatear un volumen se destruirán los datos de la partición.»** **«No puedes formatear un disco o partición que actualmente esté en uso, incluida la partición que contiene Windows.»** El formato rápido **«creará una nueva tabla de archivos, pero no sobrescribirá ni borrará completamente el volumen.»** |
| Extender y reducir | Extender un volumen básico **«en un espacio no reclamado en un volumen de la misma unidad»**; reducir, **«como para habilitar la extensión en una partición vecina»** |
| Cambiar la letra | Botón secundario sobre el volumen, cambiar letra y rutas de acceso |

Lo que Administración de discos no hace se hace con otras herramientas de Windows: liberar espacio,
desfragmentar u optimizar, y **«Agrupa varios discos duros como una matriz redundante de discos
independientes (RAID) con espacios de almacenamiento en Windows»**.

### GPT y MBR

**«El estilo de partición predeterminado es Tabla de particiones GUID (GPT).»**

| Estilo | Lo que dice Microsoft |
|---|---|
| GPT | **«La mayoría de los equipos usan el tipo de disco GPT para unidades de disco duro y unidades de estado sólido (SSD). GPT es más sólido y permite volúmenes que superan los 2 terabytes (TB).»** **«Una unidad GPT puede tener hasta 128 particiones.»** |
| MBR | **«El estilo MBR es un tipo de disco anterior. Este estilo lo usan equipos de 32 bits, equipos antiguos y unidades extraíbles como tarjetas de memoria.»** Límite del disco de arranque en BIOS: **«Tamaño máximo de disco de arranque de MBR de 2,2 TB»** |

La regla práctica del soporte de Microsoft: **«Usa GPT si tienes un sistema moderno con firmware UEFI
y necesitas compatibilidad con unidades grandes y más de cuatro particiones.»** y **«Usa MBR si estás
trabajando con hardware o sistemas operativos más antiguos que no admiten UEFI.»** En un disco MBR
caben **«hasta cuatro particiones principales en un disco básico, o hasta tres particiones
principales y una partición extendida»**, y en el espacio de la extendida se crean unidades
lógicas. Por eso el asistente avisa: **«Al crear nuevas particiones en un disco básico, las tres
primeras se formatearán como particiones principales. A partir de la cuarta, cada una de ellas se
configurará como una unidad lógica en una partición extendida.»** (lo que sólo tiene sentido en MBR;
en GPT el límite es de 128).

### Discos básicos y dinámicos

El artículo de Microsoft que los explica describe la consola de Windows Server 2003, y se cita sólo
por sus definiciones: **«Un disco básico es un disco físico que contiene
volúmenes básicos (particiones principales, particiones extendidas o unidades lógicas).»**; **«Un
disco dinámico es un disco físico que contiene volúmenes dinámicos. Con discos dinámicos, puede
crear volúmenes simples, volúmenes que abarquen varios discos (volúmenes distribuidos y seccionados)
y volúmenes tolerantes a errores (volúmenes reflejados y RAID-5).»** La conversión de básico a
dinámico transforma lo que hay (**«se cambian las particiones existentes en el disco básico a volúmenes
simples en el disco dinámico»**), pero la vuelta no: **«no puede volver a cambiar los volúmenes
dinámicos a particiones. Elimine primero todos los volúmenes dinámicos del disco y, después, vuelva a
cambiarlo a un disco básico.»** Y nunca se pueden borrar **«la partición del sistema, la partición de
arranque o una partición que contenga el archivo de paginación (intercambio) activo.»**

### `diskpart`, la gestión de discos desde la consola

**«El intérprete de comandos diskpart le ayuda a administrar las unidades del equipo (discos,
particiones, volúmenes o discos duros virtuales).»** Funciona por foco: **«Antes de poder usar los
comandos diskpart , primero debe enumerar y, a continuación, seleccionar un objeto para darle el
foco.»** Y exige ser administrador: **«Debe estar en el grupo de administradores local, o en un grupo
con permisos similares, para ejecutar diskpart.»**

| Orden | Qué hace |
|---|---|
| `list` | **«Muestra una lista de discos, de particiones en un disco, de volúmenes de un disco o de discos duros virtuales (VHD).»** |
| `select` | **«Desplaza el foco a un disco, partición, volumen o disco duro virtual (VHD).»** |
| `clean` | **«Quita todos y todos los formatos de partición o volumen del disco con foco.»** [sic] |
| `create` | **«Crea una partición en un disco, un volumen en uno o varios discos o en un disco duro virtual (VHD).»** |
| `format` | **«Da formato a un disco para aceptar archivos.»** |
| `assign` | **«Asigna una letra de unidad o un punto de montaje al volumen que tiene el foco.»** |
| `extend` / `shrink` | Amplía el volumen con foco en espacio libre / **«Reduce el tamaño del volumen seleccionado por la cantidad que especifique.»** |
| `online` | **«Toma un disco o volumen sin conexión al estado en línea.»** |

Una secuencia para preparar un disco de datos nuevo (es aplicación de la tabla, no un guion de
Microsoft; cada orden, con la sintaxis de su página de referencia): `list disk`, `select disk=1`,
`clean`, `convert gpt`, `create partition primary`, `format fs=ntfs quick`, `assign letter=e`. El orden `clean` borra el disco con foco: equivocarse de
número es perder el disco equivocado. Desde PowerShell, el equivalente de inicializar es el cmdlet
**«Initialize-Disk»**.

### Optimizar unidades

La orden `defrag` **«Localiza y consolida archivos fragmentados en volúmenes locales para mejorar el
rendimiento del sistema.»** Windows la ejecuta como tarea de mantenimiento, **«que normalmente se
ejecuta cada semana»**, y su frecuencia se cambia **«mediante la aplicación Optimizar unidades»**. En
SSD, cuando la lanza la tarea programada, los procesos de optimización tradicionales
incluyen desfragmentación tradicional y recorte: **«Esto se hace una vez al mes.»** Y **«Cambiar la frecuencia
de la tarea programada no afecta a la cadencia de una vez al mes de los SSD.»** El recorte es la orden TRIM, que la
asociación de la industria del almacenamiento SNIA (*Storage Networking Industry Association*) define
como **«A method by which the host operating system may inform a storage device of blocks of data
that are no longer in use»** (el modo en que el sistema avisa a la unidad de qué bloques ya no se
usan). La opción `/o` de `defrag` **«Realiza la optimización adecuada para cada tipo de medio.»**

### Controladores

**«Las actualizaciones de controladores para la mayoría de los dispositivos de hardware de Windows se
descargan e instalan automáticamente a través de Windows Update.»**, y Microsoft considera que **«La
mejor manera de obtener actualizaciones de controladores en Windows es usar automáticamente Windows
Update.»** Lo demás se hace en el Administrador de dispositivos (botón secundario sobre Inicio,
**Administrador de dispositivos**; se despliega la categoría y se trabaja sobre el dispositivo):

| Tarea | Cómo |
|---|---|
| Actualizar automáticamente | Botón secundario, **Actualizar controlador**, **«Buscar automáticamente software de controlador actualizado»** |
| Actualizar a mano | Descargar el controlador del fabricante (**«que coincidan con la versión y la arquitectura de Windows»**), **Actualizar controlador**, **«Buscar controladores en el equipo»**, **Examinar...** |
| Reinstalar | Botón secundario, **Desinstalar dispositivo**, reiniciar: **«Una vez reiniciado el dispositivo Windows, Windows intenta reinstalar el controlador del dispositivo.»** |
| Revertir | **Propiedades**, pestaña **Controlador**, **«Revertir al controlador anterior»**. **«Debes haber iniciado sesión con permisos de administrador para revertir los controladores.»** De oficio, es la salida cuando el fallo empezó tras actualizar el controlador |

Y una advertencia de seguridad: **«Evita descargar controladores de cualquier sitio web que no sea el
sitio oficial del fabricante.»** Cuando un dispositivo falla, su código de error está en
**Propiedades**, en el área **«Estado del dispositivo»**. Los más vistos son **«No se puede iniciar el
dispositivo. (Código 10)»**, **«Este dispositivo está deshabilitado. (Código 22)»**, **«Los
controladores de este dispositivo no están instalados. (Código 28)»** y **«Windows detuvo este
dispositivo porque informó de problemas. (Código 43)»**; el diagnóstico de averías por estos códigos
es materia del tema 2.

## 4. Conectividad de red

### La página Red e Internet

**«La página Red & Internet cubre la configuración relacionada con Wi-Fi, Ethernet, VPN, punto de
acceso móvil y uso de datos.»** (VPN es la red privada virtual, *virtual private network*.) Se abre
desde Configuración o con el botón secundario sobre el icono de red de la barra de tareas,
**«Configuración de Red e Internet»**. En su parte superior aparece el estado de la conexión, y
**Propiedades**, junto a la red conectada, da sus detalles; la dirección propia figura **«junto a la
dirección IPv4»**.

Conectarse a una Wi-Fi: se abre la Configuración rápida (iconos de red, sonido o batería), **«En la
configuración rápida de Wi-Fi, seleccione Administrar conexiones Wi-Fi .»**, se elige la red y
**Conectar**, y se escribe la contraseña. Las redes guardadas están en **«Administrar redes
conocidas»**; la contraseña de una red a la que el equipo se ha conectado se ve en sus propiedades,
junto a la contraseña de la red Wi-Fi, con **Mostrar**. Windows puede conectarse
leyendo con la cámara un código QR, y ofrece **direcciones de hardware aleatorias**: la señal con
que el equipo busca redes **«contiene la dirección única de hardware físico (MAC) del dispositivo»**,
y activarlas hace **«más difícil para los usuarios rastrearte»**.

Administrar el equipo desde otro puesto con Escritorio remoto (RDP) exige habilitarlo en
Configuración > Sistema > Escritorio remoto; los requisitos, la conexión y la seguridad de RDP se
estudian en el tema 10.

### Red pública o privada

**«Cuando se conecta por primera vez a una red en Windows 11, se establece como pública de forma
predeterminada. Esta es la configuración recomendada .»**

| Perfil | Lo que implica |
|---|---|
| Pública (recomendado) | **«El equipo se ocultará a otros dispositivos de la red. Por lo tanto, no puedes usar tu PC para compartir archivos e impresoras.»** |
| Privada | **«El equipo es reconocible para otros dispositivos en la red y puedes usarlo para compartir archivos e impresoras. Debe conocer a las personas y los dispositivos de la red y confiar en ellos.»** |

Se cambia en las propiedades de la red, **«Tipo de perfil de red»**. Para el puesto tiene una
consecuencia práctica: un equipo en red pública no se ve desde los demás aunque tenga carpetas
compartidas.

### La configuración TCP/IP

**«TCP/IP define la forma en que el equipo se comunica con otros equipos. Para facilitar la
administración de la configuración de TCP/IP, se recomienda usar el Protocolo de configuración
dinámica de host (DHCP).»** Se cambia en la red (Wi-Fi > Administrar redes conocidas, o Ethernet),
**«Junto a la asignación de IP, seleccione Editar.»**, eligiendo **«Automático (DHCP) o Manual»**:

- Automático: **«la configuración de la dirección IP y la dirección de servidor DNS son establecidas
  automáticamente por el enrutador u otro punto de acceso (recomendado).»**
- Manual, IPv4: se rellenan **«Dirección IP, Máscara de subred y Puerta de enlace»**, y **«DNS
  preferido y DNS alternativo»**.
- Manual, IPv6: los mismos campos, pero con **«Longitud de prefijo de subred»** en lugar de máscara.

En cada servidor DNS se puede activar DNS sobre HTTPS: **«Activado (plantilla automática): las
consultas DNS se cifrarán y se enviarán al servidor DNS a través de HTTPS.»** Con la **reserva a
texto no cifrado** activada, **«se enviará una consulta DNS sin cifrar si no se puede enviar a través
de HTTPS.»**; desactivada, **«no se enviará una consulta DNS si no se puede enviar a través de
HTTPS.»** **«La configuración de DNS sobre HTTPS no está disponible en Windows 10.»**

Otros controles de la misma página: el modo avión, que **«ofrece una forma rápida de desactivar
todas las comunicaciones inalámbricas en el equipo»** y **«conserva la configuración que usó la
última vez»**; y el límite de datos por red, que avisa al acercarse y al superarlo.

### Las órdenes de red

| Orden | Qué hace, según Microsoft | Opciones que conviene saber |
|---|---|---|
| `ipconfig` | **«Muestra todos los valores actuales de configuración de red TCP/IP y actualiza la configuración del Protocolo de configuración dinámica de host (DHCP) y del sistema de nombres de dominio (DNS).»** | `/all`: **«Muestra la configuración completa de TCP/IP para todos los adaptadores.»**; `/release` y `/renew` liberan y renuevan la concesión de DHCP; `/flushdns`: **«Vacía y restablece el contenido de la caché de resolución del cliente DNS.»**; `/displaydns` muestra esa caché |
| `ping` | **«Comprueba la conectividad a nivel de IP con otro equipo TCP/IP mediante el envío de mensajes de solicitud de eco del protocolo de mensajes de control de Internet (ICMP).»** | `/t`, sin fin hasta Ctrl + C; `/n`, número de mensajes: **«El valor predeterminado es 4.»**; `/l`, tamaño: **«El valor predeterminado es 32.»**; `/a`, resolución inversa del nombre |
| `tracert` | **«Esta herramienta de diagnóstico determina la ruta de acceso a un destino mediante el envío de mensajes de solicitud de eco del Protocolo de mensajes de control de Internet (ICMP) o ICMPv6 al destino con valores de campo de período de vida (TTL) cada vez mayores.»** | **«El número máximo de saltos es 30 de forma predeterminada y se puede especificar mediante el parámetro /h .»**; `/d` no resuelve nombres. Un salto que no responde sale como **«una fila de asteriscos»** |
| `netstat` | **«Muestra las conexiones TCP activas, los puertos en los que escucha el equipo, las estadísticas de Ethernet, la tabla de enrutamiento IP, las estadísticas IPv4 […] y las estadísticas de IPv6»**. **«Se usa sin parámetros; este comando muestra conexiones TCP activas.»** | `-a`: **«Muestra todas las conexiones TCP activas y los puertos TCP y UDP en los que escucha el equipo.»**; `-n`, en número; `-o`, con el PID; `-b`, el ejecutable; `-r`: **«Esto equivale al comando route print.»** |

Dos lecturas de diagnóstico que da Microsoft. De `ping`: **«Si el ping a la dirección IP se realiza
correctamente, pero el ping al nombre del equipo no, es posible que tenga un problema de resolución de
nombres.»** Y de `netstat -o`: **«Puede encontrar la aplicación en función del PID en la pestaña
Procesos del Administrador de tareas de Windows.»** El atajo de memoria: `netstat` es *network
statistics*, estadísticas de red. `tracert` es *trace route*, trazar la ruta.

### Las rutas de red (UNC)

**«Las rutas de acceso de convención de nomenclatura universal (UNC), que se usan para acceder a los
recursos de red, tienen el formato siguiente:»** un servidor **«precedido por \\»**, que **«puede ser
un nombre de equipo NetBIOS o una dirección IP/FQDN (se admiten IPv4, así como v6).»**; un nombre de
recurso compartido, y **«Juntos, el nombre del servidor y el del recurso compartido forman el
volumen.»**; después, directorios y un nombre de archivo opcional. (NetBIOS es el sistema básico de
entrada y salida de red, *network basic input/output system*; FQDN, el nombre de dominio completo,
*fully qualified domain name*.)

La forma de una ruta de este tipo es siempre la misma:

```
\\servidor\recurso\camino\dentro\del\recurso
```

El segundo elemento es el nombre del recurso compartido, no una unidad local. Los dos puntos de `C:`
no caben ahí: es la letra de unidad vista desde el propio equipo, y la ruta de red se escribe desde
fuera. Por eso `\\SRV7\C:\Repositorio\Video.mp4` no es una ruta válida, y estas sí:

| Ruta | Por qué vale |
|---|---|
| `\\SRV7\Repositorio\Video.mp4` | Recurso compartido corriente |
| `\\SRV7\C$\Repositorio\Video.mp4` | `C$` es el recurso administrativo oculto que el sistema crea para cada unidad. El dólar lo oculta del listado, y es válido |
| `\\192.168.100.7\Repositorio\Video.mp4` | El servidor se puede nombrar por dirección en vez de por nombre |

Microsoft pone el mismo ejemplo: **«\\system07\C$\»** es el **«Directorio raíz de la unidad C: en
system07.»** La diferencia es el carácter: el dólar es parte del nombre del recurso compartido y los
dos puntos no lo son. Y una regla más: **«Las rutas de acceso UNC siempre deben ser completas.»**;
**«Solo puede usar rutas de acceso relativas mediante la asignación de una ruta de acceso UNC a una
letra de unidad.»**

## 5. Protección y recuperación del sistema

### El entorno de recuperación (WinRE)

**«Windows Entorno de recuperación (WinRE) es un entorno de recuperación que puede reparar las causas
comunes de los sistemas operativos que no se pueden arrancar. WinRE se basa en el Entorno de
preinstalación de Windows (Windows PE)»**. **«De forma predeterminada, WinRE viene preinstalado en
Windows 10 y Windows 11 para las ediciones de escritorio (Home, Pro, Enterprise y Education)»**, y
vive en la partición de recuperación (epígrafe 10). Sus herramientas:

| Herramienta | Qué hace |
|---|---|
| Reparación automática y solución de problemas | Diagnóstico y reparación del arranque |
| Restauración a un momento dado | **«los usuarios pueden restaurar rápidamente su equipo Windows al estado exacto, en el que estaba en un momento dado anterior, mediante puntos de restauración almacenados localmente.»** |
| Restablecimiento mediante botón | **«(solo para las ediciones de escritorio de Windows). Los usuarios pueden reparar sus propios equipos rápidamente, a la vez que conservan sus datos y personalizaciones importantes, sin tener que realizar copias de seguridad de los datos de antemano.»** Es lo que la interfaz llama Restablecer este PC |
| Recuperación de imágenes del sistema | **«(solo Windows Server ediciones). Esta herramienta restaura todo el disco duro.»** |

Cómo se entra, a mano: **«En la pantalla de inicio de sesión, haga clic en Apagar y mantenga
presionada la tecla Mayús mientras selecciona Reiniciar.»**; desde Configuración > Sistema >
Recuperación, **Inicio avanzado**, **Reiniciar ahora**; **«Arranque en medios de recuperación.»**; o
con el botón de recuperación del fabricante. Y Windows entra solo cuando detecta:

- **«Dos intentos fallidos consecutivos de iniciar Windows.»**
- **«Dos apagados inesperados consecutivos que se producen en un plazo de dos minutos después de la finalización del arranque.»**
- **«Dos reinicios consecutivos del sistema en un plazo de dos minutos después de la finalización del arranque.»**
- **«Error de arranque seguro (excepto los problemas relacionados con Bootmgr.efi).»**
- **«Un error de BitLocker en dispositivos solo táctiles.»**

El menú Inicio avanzado permite lanzar las herramientas de recuperación, **«Arranque desde un
dispositivo (solo UEFI).»**, **«Acceda al menú Firmware (solo UEFI).»** y elegir sistema si hay
varios.

Dos rasgos de seguridad. Primero, el acceso: la página técnica dice a la vez que, si se entra desde
Windows, hay que dar **«el nombre de usuario y la contraseña de una cuenta de usuario local con
derechos de administrador»**, y que, como novedad de Windows 11, **«Ahora puedes ejecutar la mayoría
de las herramientas en WinRE sin seleccionar una cuenta de administrador ni escribir la contraseña.
Cuando se inicia en el entorno de recuperación, los archivos cifrados no serán accesibles a menos que
el usuario tenga la clave para descifrar el volumen.»** Lo que no cambia es esto último: con
BitLocker, **«necesitarás la clave de recuperación de BitLocker para acceder a la mayoría de las
opciones de recuperación de WinRE.»** Segundo, la red: **«WinRE no mantiene la conectividad de red de
uso general de forma predeterminada. Las redes solo están activadas cuando un flujo de trabajo de
recuperación requiere conectividad»**.

### La configuración de inicio y el modo seguro

Entre las opciones avanzadas de WinRE está la Configuración de inicio, que cambia la forma en que
arranca Windows para aislar un fallo. El ejemplo de Microsoft es el modo seguro, **«que inicia Windows
en un estado limitado, en el que solo se inician los servicios y controladores básicos»**. Su lógica de
diagnóstico: **«Si un problema no vuelve a aparecer cuando inicia en modo seguro, puede eliminar la
configuración predeterminada, los controladores de dispositivo básicos y los servicios como posibles
causas.»**

Cómo se llega: se entra en WinRE (por cualquiera de las vías del subepígrafe anterior) y se sigue
Solucionar problemas > Opciones avanzadas > Configuración de inicio > Reiniciar (la ruta sale
desordenada en la página; se da reconstruida). Con el disco cifrado hace falta la clave: **«Si has
cifrado el dispositivo, necesitarás la clave de BitLocker para completar esta tarea.»** Tras el
reinicio aparece la pantalla Configuración de inicio con nueve opciones, que se eligen por su número
según el orden en que Microsoft las enumera;
**«Para seleccionar una, use las teclas numéricas o las teclas de función F1-F9»**:

| N.º | Opción | Qué hace |
|---|---|---|
| 1 | Habilitar la depuración | **«Inicia Windows en un modo avanzado de solución de problemas destinado a profesionales de TI y administradores del sistema»** |
| 2 | Habilitar el registro de arranque | **«Crea un archivo, ntbtlog.txt, que enumera todos los controladores que se instalan durante el inicio»** |
| 3 | Habilitar vídeo de baja resolución | **«Inicia Windows con el controlador de vídeo actual y una configuración de resolución y frecuencia de actualización bajas.»** Sirve **«para restablecer la configuración de pantalla»** |
| 4 | Habilitar el modo seguro | **«El modo seguro inicia Windows en un estado básico, que usa un conjunto limitado de archivos y controladores.»** |
| 5 | Modo seguro con funciones de red | **«agrega los controladores y servicios de red que necesitará para acceder a Internet y a otros equipos de la red»** |
| 6 | Modo seguro con símbolo del sistema | **«Inicia Windows en modo seguro con una ventana de símbolo del sistema en lugar de la interfaz habitual de Windows»** |
| 7 | Deshabilitar la aplicación de firmas de controladores | **«Permite instalar controladores con firmas incorrectas»** |
| 8 | Deshabilitar la protección antimalware de inicio anticipado (ELAM) | ELAM **«permite que el software antimalware se inicie antes que el resto de los componentes de terceros durante el proceso de arranque.»** La opción la deshabilita **«temporalmente»** |
| 9 | Deshabilitar reinicio automático tras error | **«Impide que Windows se reinicie automáticamente en caso de que un error haga que Windows falle.»** Sólo para el bucle en que Windows falla, se reinicia y vuelve a fallar |

**«Puede presionar Entrar para iniciar Windows normalmente.»** Un caso típico de aplicación práctica:
si Windows deja de arrancar tras instalar un controlador, el modo seguro (4) lo arranca con el mínimo de
controladores, y desde ahí se revierte o desinstala el controlador (epígrafe 3); si hace falta
descargar algo, el modo seguro con funciones de red (5).

Para salir, **«Reiniciar el dispositivo debería ser suficiente para salir del modo seguro y volver al
modo normal.»** Si el equipo sigue arrancando en modo seguro, Microsoft indica abrir Win + R, escribir
`msconfig`, ir a la pestaña Arranque y, en Opciones de arranque, desactivar la casilla Arranque seguro.
Por el contexto de la página, esa casilla es la que deja fijado el modo seguro; no debe confundirse con
el arranque seguro de UEFI del epígrafe 1, que es una garantía del firmware sobre el cargador.

### Las opciones de recuperación, de menos a más drásticas

El soporte de Microsoft ordena las opciones según el equipo arranque o no, y pide empezar por la
menos disruptiva. Antes de nada, **«Haz una copia de seguridad de tus archivos importantes»**.

Si el equipo arranca pero falla:

| Orden | Opción | Qué hace | Desde qué versión |
|---|---|---|---|
| 1 | Solucionador de problemas | Configuración > Sistema > Solucionar problemas > Otros solucionadores | Windows 10 y 11 |
| 2 | Reinstalar Windows (con Windows Update) | **«Esta acción reinstala la versión actual sin afectar a los archivos, las aplicaciones ni la configuración.»** | **«Windows 11, versión 22H2 o posterior»** |
| 3 | Desinstalar una actualización | Si el problema empezó tras una actualización; la vuelta a la versión anterior está **«disponible durante 10 días después de la actualización»** | Windows 10 y 11 |
| 4 | Restauración a un momento dado | **«Esta acción revierte todo el equipo, incluidas las aplicaciones, la configuración y los archivos personales, a un punto de restauración automática reciente.»** | **«Windows 11, versión 24H2 o posterior»** |
| 5 | Restablecer este PC | **«Esta acción reinstala Windows desde cero. Puede optar por conservar sus archivos personales o quitarlos todos.»** **«Esta opción es muy perturbadora.»** | Windows 10 y 11 |

Si no arranca, desde WinRE: restauración a un momento dado; desinstalar actualizaciones (**«En WinRE,
seleccione Solucionar> problemasOpciones avanzadas>Desinstalar actualizaciones.»** [sic: Solucionar
problemas > Opciones avanzadas]); Restablecer este PC; y reinstalar desde medios de recuperación del
fabricante o de instalación. Las opciones adicionales: Restaurar sistema (epígrafe 14), reinstalar
con una unidad de recuperación y reinstalar con medios de instalación (**«si sospechas que el
dispositivo se ha infectado con malware, o si nada más funciona. Esto quita todo del dispositivo.»**).

Si el equipo arranca pero se sospecha de archivos del sistema dañados, una herramienta más
es `sfc /scannow`, ejecutada como administrador, que comprueba los archivos protegidos del sistema
y repara los que puede: se estudia en el tema 2.

Qué se pierde en cada una, según la misma página:

| Opción | Archivos personales | Aplicaciones y configuración |
|---|---|---|
| Desinstalar una actualización | Se conservan | Se conservan; se quitan los cambios de esa actualización |
| Volver a la versión anterior | Se conservan | **«se quitan las aplicaciones, los controladores y la configuración agregados o cambiados después de la actualización.»** |
| Reinstalar con Windows Update | Se conservan | Se conservan |
| Restauración a un momento dado | Vuelven al punto | **«Los cambios realizados después de ese punto de restauración se pierden.»** Lo que está en OneDrive no se toca |
| Restaurar sistema | Se conservan | **«se deshacen los cambios del sistema realizados después del punto de restauración.»** |
| Restablecer este PC | A elegir | **«Se quitan las aplicaciones y la configuración.»** |
| Medios de instalación | A elegir: archivos y aplicaciones, sólo archivos, o nada (pero la misma página, al describir la opción, dice que **«Esto quita todo del dispositivo.»**; la elección es la de `setup.exe` del epígrafe 1) | Según lo elegido |
| Unidad de recuperación | **«se quitan los archivos, las aplicaciones y la configuración personales.»** | Se quitan |

### La recuperación rápida de equipo

**«La recuperación rápida de equipo ayuda a los dispositivos Windows 11 a recuperarse de errores de
inicio repetidos causados por un problema conocido y generalizado. Si Windows no se puede iniciar,
el dispositivo puede entrar en el modo de recuperación, conectarse a Internet y comprobar si Windows
Update tiene una corrección proporcionada por Microsoft.»** **«No restablece el equipo ni afecta a
los archivos, las aplicaciones o la configuración.»** **«Está disponible en Windows 11, versión 24H2
o posterior. En Windows 11 Home, está habilitado de forma predeterminada. En los dispositivos Pro y
Enterprise, es posible que un administrador de TI deba habilitarlo.»**

### Prepararse antes de que falle

Microsoft recomienda tres cosas mientras el equipo funciona: **«Habilitar Copias de seguridad de
Windows: guarda las aplicaciones y la configuración en la nube para que se puedan restaurar
automáticamente después de una recuperación. Vaya a Configuración>Cuentas>Copias de seguridad de
Windows.»**; conocer la clave de recuperación de BitLocker; y **«Crear una unidad de recuperación:
mientras el equipo está funcionando, cree una unidad de recuperación en una unidad USB como última
opción.»** A ello se suma la protección del sistema con puntos de restauración, que no viene
activada (epígrafe 14).

## 6. Configuración de la seguridad

### La aplicación Seguridad de Windows

**«Seguridad de Windows es una interfaz de cliente en Windows 10, versión 1703 y posteriores. No es la
consola del portal web Centro de seguridad de Microsoft Defender»**. Reúne siete secciones:

| Sección | Qué contiene |
|---|---|
| Protección contra virus y amenazas | Antivirus y **«protección contra ransomware»**, incluido el **«acceso controlado a carpetas»** |
| Protección de cuentas | Inicio de sesión y protección de cuentas |
| Firewall y protección de red | **«la configuración del firewall, incluido Firewall de Windows.»** |
| Control de aplicaciones y del explorador | **«la configuración de SmartScreen de Windows Defender y las mitigaciones de protección contra vulnerabilidades.»** |
| Seguridad del dispositivo | **«acceso a la configuración de seguridad de dispositivos integrada.»** |
| Rendimiento y estado del dispositivo | **«información sobre los controladores, el espacio de almacenamiento y los problemas generales de Windows Update.»** |
| Opciones familiares | Controles parentales |

(Los nombres de las secciones aparecen en la página traducida con el signo «&» en lugar de «y»: **«Virus
& protección contra amenazas»**, **«Firewall & protección de red»**.)

Se abre con el icono del área de notificación, buscándola en Inicio o desde Configuración >
Privacidad y seguridad > Seguridad de Windows. Tres reglas: **«No puede desinstalar Seguridad de
Windows»**; **«Microsoft Defender Antivirus se deshabilita automáticamente cuando se instala un
producto antivirus de terceros y se mantiene actualizado.»**; y en una organización manda la
administración centralizada: **«La configuración configurada con herramientas de administración, como
la directiva de grupo, Microsoft Intune o Microsoft Configuration Manager, tiene prioridad sobre la
configuración del Seguridad de Windows.»** El antivirus, el malware y el cortafuegos en detalle son
del tema 14.

### BitLocker y el cifrado de dispositivo

**«BitLocker es una característica de seguridad de Windows que proporciona cifrado para volúmenes
enteros, que aborda las amenazas de robo de datos o la exposición de dispositivos perdidos, robados o
retirados inapropiadamente.»** El riesgo que cubre es el de quien se lleva el disco: los datos son
vulnerables **«mediante la transferencia del disco duro del dispositivo a otro dispositivo»**.

Su relación con el TPM: **«BitLocker ofrece máxima protección cuando se usa con un Módulo de
plataforma segura (TPM)»**, que **«funciona con BitLocker para asegurarse de que un dispositivo no se
haya manipulado mientras el sistema está sin conexión.»** El chip no cifra el disco: hace de protector
de la clave (la documentación habla de que **«se crea el protector de TPM»**) y comprueba que el
equipo no se ha manipulado. Se puede reforzar con un PIN o una clave de inicio en
un dispositivo extraíble, lo que da autenticación multifactor. Sin TPM también funciona, con una
clave de inicio en una unidad extraíble o con una contraseña (opción que Microsoft desaconseja por
los ataques de fuerza bruta y que **«se deshabilita de forma predeterminada»**), pero **«Ambas opciones no proporcionan
la comprobación de integridad del sistema previa al arranque ofrecida por BitLocker con un TPM.»**

Requisitos que se preguntan:

- **«el dispositivo debe tener TPM 1.2 o posterior»** para la comprobación de integridad.
- **«TPM 2.0 no se admite en los modos heredado y de módulo de soporte de compatibilidad (CSM) del BIOS.»**
- Dos unidades: la del sistema operativo, **«formateada con el sistema de archivos NTFS»**, y la del sistema, que **«no deben estar cifrados»** [sic], distinta de la anterior y en FAT32 si el firmware es UEFI. **«Cuando se instala en un dispositivo nuevo, Windows crea automáticamente las particiones necesarias para BitLocker.»**
- Ediciones: Windows Pro, Enterprise, Pro Education/SE y Education. BitLocker To Go, para memorias USB, **«está disponible en Windows Pro y versiones posteriores.»**

El cifrado de dispositivo es la versión automática: **«El cifrado de dispositivos es una característica
de Windows que proporciona una manera sencilla para que algunos dispositivos habiliten automáticamente
el cifrado de BitLocker. El cifrado de dispositivos está disponible en todas las versiones de
Windows»**. **«A partir de Windows 11, versión 24H2, se eliminan los requisitos previos de DMA y
HSTI/Modo de espera moderno.»** (HSTI es la interfaz de prueba de seguridad de hardware, *hardware
security test interface*.) La clave de recuperación se guarda automáticamente en Microsoft Entra ID,
en AD DS o en la cuenta Microsoft; pero **«Si un dispositivo usa solo cuentas locales, permanece
desprotegido aunque los datos estén cifrados.»** **«De forma predeterminada, el cifrado del
dispositivo usa el método de XTS-AES 128-bit cifrado.»** [sic], y si se desactiva **«ya no se
habilitará automáticamente en el futuro.»** Si el equipo cumple los requisitos, Información del
sistema (`msinfo32.exe`) muestra **«Compatibilidad con el cifrado de dispositivos»** con el valor
**«Cumple con los requisitos previos»**.

El cifrado de archivos sueltos es otra cosa: EFS, que se maneja con la orden `cipher`, que **«Muestra
o modifica el cifrado de directorios y archivos en volúmenes NTFS.»** Y la distinción que hay que
llevar aprendida: cifrado de volumen frente a cifrado de fichero. El primero protege del robo del
soporte; el segundo, del vecino de escritorio. Son complementarios y resuelven amenazas distintas.

### El control de cuentas de usuario (UAC)

**«Control de cuentas de usuario (UAC) es una característica de seguridad de Windows diseñada para
proteger el sistema operativo frente a cambios no autorizados. Cuando los cambios en el sistema
requieren permiso de nivel de administrador, UAC notifica al usuario y éste puede aprobar o denegar el
cambio.»** **«UAC está habilitado de forma predeterminada y quien tenga privilegios de administrador
puede configurarlo.»**

Cómo funciona: **«Cuando un administrador inicia sesión, se crean dos tokens de acceso independientes
para el usuario: un token de acceso de usuario estándar y un token de acceso de administrador.»** El
escritorio (`explorer.exe`) corre con el estándar, y de él heredan todos los procesos; **«Como
resultado, todas las aplicaciones se ejecutan como un usuario estándar a menos que un usuario
proporcione consentimiento o credenciales»**. Lo que el mecanismo resuelve de verdad: un
administrador trabaja con una ficha de permisos reducida hasta que hace falta elevarla. Así, un
programa lanzado por error no hereda privilegios administrativos sin que nadie lo vea. La ventana que
aparece no es un trámite: es el punto donde el usuario decide elevar.

Hay dos ventanas de elevación:

| Ventana | A quién se le muestra |
|---|---|
| Solicitud de credenciales | Al usuario estándar: **«El componente de elevación UAC integrado predeterminado para los usuarios estándar es el símbolo del sistema de credenciales.»** Tiene que escribir usuario y contraseña de un administrador |
| Solicitud de consentimiento | Al administrador en modo de aprobación de administrador: basta con aprobar el cambio |

Microsoft recomienda trabajar como usuario estándar: **«El método recomendado y más seguro para
ejecutar Windows es asegurarse de que la cuenta de usuario principal es un usuario estándar.»** El
color de la ventana orienta: **«Fondo gris: la aplicación es una aplicación administrativa de
Windows, como un elemento de Panel de control, o una aplicación firmada por un publicador
comprobado»**; **«Fondo amarillo: la aplicación está sin signo o firmada, pero no es de confianza»**
[sic: «sin signo» es «sin firmar»]. El icono de escudo en un botón **«indica que el proceso requiere
un token de acceso de administrador completo.»** Y la ventana sale en el escritorio seguro, al que
**«Solo los procesos de Windows pueden acceder»**, que atenúa el resto de la pantalla.

El nivel de UAC se cambia en Panel de control > Sistema y seguridad > Cambiar configuración de
Control de cuentas de usuario, con un control deslizante de cuatro posiciones (la página de soporte
está en inglés): notificar siempre; notificar sólo cuando las aplicaciones intenten hacer cambios
(**«(default)»**, la predeterminada); lo mismo sin atenuar el escritorio; y no notificar nunca, que
deshabilita UAC y **«isn't recommended due to security concerns»** (no se recomienda por seguridad).

### Las cuentas de usuario del equipo y el inicio de sesión

El UAC protege a quien trabaja en el equipo; antes hay que decidir con qué cuenta trabaja. Las
cuentas locales son las del propio equipo: **«Las cuentas de usuario y sistema locales se definen
localmente en un dispositivo y el dispositivo es la entidad de seguridad. Estas cuentas solo tienen
derechos y permisos en ese dispositivo.»** Junto a ellas, el equipo admite la cuenta Microsoft y la
cuenta profesional o educativa; y Microsoft, en su página de soporte, recomienda la primera: **«Microsoft
recomienda usar una cuenta de Microsoft, no una cuenta local, al iniciar sesión en Windows.»** (En
Home, además, la cuenta Microsoft es obligatoria en la configuración inicial: epígrafe 1.)

Tipos de cuenta. Una cuenta tiene privilegios de administrador o es estándar (Microsoft lo ilustra con
padres administradores e hijos con cuentas estándar), y se piden pocos administradores:
**«Los administradores pueden cambiar la configuración, instalar software y obtener acceso a todos los
archivos.»** **«Es más seguro tener menos administradores y usar cuentas de usuario estándar para las
actividades diarias.»** La documentación técnica lo dice como buena práctica: **«Como procedimiento
recomendado de seguridad, use la cuenta local (que no es de administrador) para iniciar sesión y, a
continuación, use Ejecutar como administrador para realizar tareas que requieran un mayor nivel de
derechos o permisos que una cuenta de usuario estándar.»**

Las tareas, desde Configuración > Cuentas (rutas reconstruidas, porque la página las da desordenadas):

| Tarea | Ruta | Lo que conviene saber |
|---|---|---|
| Agregar un usuario | Cuentas > Otros usuarios > Agregar otro usuario > **Agregar cuenta** | Con cuenta Microsoft basta el correo. Para una cuenta local, tras «No tengo los datos de inicio de sesión de esta persona»: **«Si desea crear una cuenta local, seleccione la opción Agregar un usuario sin una cuenta de Microsoft»** |
| Hacer administrador (o volver a estándar) | Cuentas > Otros usuarios > la cuenta > **Cambiar tipo de cuenta** | Se elige el tipo en la lista desplegable y se acepta |
| Quitar un usuario | Cuentas > Otros usuarios > la cuenta > junto a Cuenta y datos, **Quitar** | **«Al quitar una cuenta, no se elimina la cuenta Microsoft de esa persona. Quita la información de inicio de sesión y los datos del dispositivo.»** |
| Conectar una cuenta profesional o educativa | Cuentas > Obtener acceso a trabajo o escuela > **Conectar** | **«Para conectar una cuenta profesional o educativa, su organización debe admitir dispositivos personales o escenarios de dispositivo propio (BYOD).»** |

Desde las herramientas clásicas, las cuentas se gestionan en Administración de equipos (`compmgmt.msc`,
epígrafe 9): **«Las cuentas de usuario local predeterminadas y las cuentas de usuario local que cree se
encuentran en la carpeta Usuarios y grupos locales\Usuarios de Administración de equipos.»** La orden
`net user` se estudia en el tema 8.

Las cuentas integradas que crea la instalación:

- Administrador. **«El programa de instalación de Windows deshabilita la cuenta de administrador
  integrada y crea otra cuenta local que es miembro del grupo Administradores.»** **«No puede eliminar
  ni bloquear la cuenta de administrador predeterminada. Sin embargo, puede cambiar el nombre o
  deshabilitarlo.»** Y enlaza con el modo seguro (epígrafe 5): **«Incluso cuando la cuenta de
  administrador está deshabilitada, puede usarla para obtener acceso a un equipo si la inicia en modo
  seguro.»** Las reglas del modo seguro: con las redes habilitadas, vale una cuenta de dominio miembro
  del grupo de administradores; si hay otro miembro habilitado del grupo de administradores locales,
  vale esa cuenta; y **«Si no hay ninguna otra cuenta habilitada, el modo seguro habilita
  automáticamente la cuenta de administrador.»**
- Invitado. **«La cuenta de invitado tiene permisos y derechos de usuario limitados. De forma
  predeterminada, la cuenta de invitado está deshabilitada y tiene una contraseña en blanco.»** Por el
  acceso anónimo que puede dar, **«se recomienda dejar deshabilitada la cuenta de invitado, a menos que
  sea necesario su uso.»** No es, por tanto, la cuenta que se da a un usuario nuevo del puesto: a ese se
  le crea una cuenta estándar.

Las opciones de inicio de sesión (Windows Hello) están en Configuración > Cuentas > Opciones de inicio
de sesión. La página de soporte se sirve en inglés: **«Instead of using a password, with Windows Hello
you can sign in using facial recognition, fingerprint, or a PIN.»** (en lugar de la contraseña, cara,
huella o PIN). Tres maneras: reconocimiento facial, con la cámara de infrarrojos del equipo o una
externa de infrarrojos; huella dactilar; y PIN. Requisitos: **«Signing in with your face requires a Hello-compatible
camera. Signing in with your fingerprint requires your device to have a fingerprint reader.»** Del PIN
dice que **«your PIN is only associated with one device»** (sólo vale en ese equipo).

## 7. Centro de notificaciones

**«Las notificaciones en Windows pueden aparecer como banners en la pantalla y también se puede
acceder a ellas en el centro de notificaciones.»** Cuando hay notificaciones nuevas, **«se iluminará
el icono de campana de notificación de la barra de tareas.»** El centro se abre de tres maneras:
**«Seleccione el icono del reloj o de la campana de notificación en la barra de tareas»**, con Win + N
o deslizando el dedo desde el lateral de la pantalla. El atajo Win + N abre a la vez el centro de
notificaciones y el calendario.

En el centro se puede responder sin abrir la aplicación, expandir una notificación, borrarla una a
una o por aplicación, desactivar las de una aplicación y **«Selecciona el botón Borrar todo para
quitar todas las notificaciones del centro de notificaciones»**.

La configuración está en Configuración > Sistema > Notificaciones: un interruptor general y, por
aplicación (**«Notificaciones de aplicaciones y otros remitentes»**), estas opciones: activar o
desactivar; mostrar banners; mostrar en el centro de notificaciones; ocultar el contenido en la
pantalla de bloqueo; reproducir un sonido; y la prioridad, que se puede poner en **«Superior, Alta o
Normal. Solo se puede establecer una aplicación como de máxima prioridad, y las notificaciones de
prioridad alta aparecerán encima de las normales en el centro de notificaciones»**.

No molestar: **«Para activar manualmente la opción No molestar, abre el centro de notificaciones y
selecciona el icono de campana con zZ . Esto silenciará todas las notificaciones hasta que lo
desactives manualmente.»** **«Con No molestar activado, solo recibirá banners de alarmas,
recordatorios y aplicaciones de su elección. Otras notificaciones se envían directamente al centro
de notificaciones hasta que lo desactives.»** Puede activarse sola con Foco o en condiciones que se
configuran.

La aplicación Seguridad de Windows también **«muestra notificaciones a través del Centro de
acciones.»** «Centro de actividades» y «Centro de acciones» son nombres que la documentación
traducida de Microsoft todavía usa en algunas páginas (la versión para Windows 10 de la página de
notificaciones llama así al centro); en Windows 11, Win + A abre la Configuración rápida y Win + N el
centro de notificaciones (epígrafe 2).

## 8. Personalización

**«Usa la página de personalización para personalizar la apariencia de tu PC, incluidos los temas,
fondos, colores, pantalla de bloqueo, menú Inicio y configuración de la barra de tareas.»**

- Temas: **«Los temas de Windows son una combinación de imágenes de fondo de escritorio, colores de
  ventanas, sonidos y otros elementos»**. Se aplican en Configuración > Personalización > Temas, se
  descargan más de Microsoft Store, se guardan y se comparten: **«Esto crea un .deskthemepack
  archivo que puede compartir con otros usuarios.»** [sic, por «un archivo .deskthemepack»].
- Colores: **«Windows admite dos modos de color principal: claro y oscuro.»**, más un modo
  personalizado; y un color de énfasis, que **«se usa para resaltar elementos importantes en la
  interfaz de usuario, como botones, vínculos y otros componentes interactivos.»** y que Windows puede
  tomar automáticamente del fondo. **«El modo claro no personaliza el color del menú Inicio, la barra
  de tareas y el centro de actividades (esa opción solo está disponible para los modos oscuro y
  personalizado).»**
- Inicio: carpetas junto al botón de encendido, vistas de Todas, recomendaciones; alinear Inicio y
  la barra a la izquierda (epígrafe 2).
- Barra de tareas: elementos visibles (Buscar, Vista de tareas, Widgets), iconos de la bandeja,
  comportamientos (alineación, insignias, ocultar automáticamente). En el reloj se pueden mostrar los
  segundos, opción que **«usa más energía»**.

## 9. Configuración básica y avanzada

### La aplicación Configuración

**«Configuración es la aplicación principal para personalizar y administrar la configuración de
Windows.»** Se abre con el botón secundario sobre Inicio o con Win + I. **«Cuenta con un panel de
navegación, con categorías claramente etiquetadas.»** Las categorías de Windows 11:

| Categoría | Qué reúne |
|---|---|
| Inicio | **«acciones relacionadas con la cuenta»** y tarjetas de acceso frecuente |
| Sistema | **«la configuración de pantalla, las notificaciones, la configuración de energía y suspensión, el almacenamiento, las características opcionales y mucho más.»** También Recuperación y Avanzado |
| Bluetooth y dispositivos | **«impresoras, escáneres y dispositivos Bluetooth. También incluye ajustes de ratón, teclado, lápiz y panel táctil.»** |
| Red e Internet | Wi-Fi, Ethernet, VPN, punto de acceso móvil y uso de datos (epígrafe 4) |
| Personalización | Epígrafe 8 |
| Aplicaciones | **«Puede ver, instalar, desinstalar y actualizar aplicaciones, elegir aplicaciones predeterminadas, configurar aplicaciones y acciones de inicio»** |
| Cuentas | Cuenta Microsoft, cuenta profesional o educativa, familia y **«las opciones de inicio de sesión»**; también Copias de seguridad de Windows |
| Hora e idioma | Fecha, hora, idioma y región |
| Juegos | **«la configuración de la barra de juegos, el modo de juego y el streaming de juegos.»** |
| Accesibilidad | **«la configuración de visión, audición e interacción.»** |
| Privacidad y seguridad | Permisos de ubicación, cámara y micrófono, datos de diagnóstico, **«configurar el cifrado y encontrar un dispositivo perdido o robado.»** y Seguridad de Windows |
| Windows Update | **«las actualizaciones de Windows, las horas activas y otras opciones de actualización.»** y el Programa Windows Insider |

La búsqueda de Configuración entiende frases: **«En Configuración, puede usar el lenguaje natural
para encontrar lo que necesita»**, y un agente local puede proponer el ajuste, pero **«El agente
solo sugiere configuraciones; No realiza ningún cambio automáticamente.»**

### Las herramientas avanzadas

Lo que no está en Configuración está en las herramientas clásicas, que Microsoft describe así:

| Herramienta | Qué es | Cómo se abre |
|---|---|---|
| Administrador de tareas | **«una aplicación que sirve como monitor del sistema y administrador de inicio para Windows»**; permite **«finalizar programas que no responden, ajustar las aplicaciones de inicio y monitorear las sesiones de usuario activas»** | Ctrl + Mayús + Esc, o botón secundario sobre Inicio |
| Administración de equipos | **«un complemento de Microsoft Management Console (MMC) que proporciona una ubicación centralizada para administrar diversos componentes, servicios y configuraciones del sistema en Windows. Incluye herramientas para administrar discos, servicios, dispositivos, carpetas compartidas y usuarios»** | `compmgmt.msc` |
| Visor de eventos | **«un complemento de Microsoft Management Console (MMC) que puede usar para ver y administrar registros de eventos.»** Organizado en **«registros de Windows, registros de aplicaciones y servicios y suscripciones.»** | `eventvwr.msc` |
| Configuración del sistema | **«una utilidad del sistema que le permite solucionar problemas de inicio de Windows.»** Pestañas General, Arranque, Servicios, Inicio y Herramientas; la de Inicio **«redirige al Administrador de tareas en versiones más recientes de Windows»** | `MSConfig` |
| Información del sistema | **«una vista completa del hardware, los componentes del sistema y el entorno de software»** | `msinfo32` |
| Editor del Registro | El Registro **«es una base de datos que almacena la configuración de bajo nivel para Windows y para las aplicaciones que optan por usarlo.»** Antes de tocarlo, **«Asegúrese siempre de haber realizado una copia de seguridad del Registro»** | `regedit` |
| Editor de directivas de grupo local | Epígrafe 13. **«El Editor de directivas de grupo local no está disponible en la edición Windows Home.»** | `gpedit.msc` |
| Configuración avanzada del sistema | Para **«configurar las propiedades del sistema, las variables de entorno, la configuración de rendimiento y los perfiles de usuario»** | `SystemPropertiesAdvanced` |

En Windows 11 25H2 la página Configuración > Sistema > Avanzado reúne además las opciones para
desarrolladores (epígrafe 12).

### Los servicios y sus dependencias

Los servicios se gestionan en Administración de equipos, que según Microsoft incluye herramientas
para administrarlos, en la pestaña Servicios de Configuración del sistema y desde la consola de
órdenes; de oficio, también en la consola Servicios (`services.msc`). Qué es
una dependencia de servicio y por qué importa: un servicio puede necesitar que otro esté en marcha
para arrancar. Cuando un servicio no arranca, lo primero que se mira es su pestaña de dependencias,
porque el que falla suele ser el de abajo, no el que da el error. Esa pestaña, de oficio, está en las propiedades
del servicio. En PowerShell, el cmdlet `Get-Service` **«obtiene
objetos que representan los servicios de un equipo, incluidos los servicios en ejecución y
detenidos.»**, y tiene dos parámetros para esto: `-RequiredServices`, que **«obtiene solo los
servicios que requiere este servicio.»**, y `-DependentServices`, que **«obtiene solo los servicios
que dependen del servicio especificado.»** (ejemplo de Microsoft: `Get-Service "WinRM"
-RequiredServices`). En la consola clásica, `sc.exe query` **«Obtiene y muestra información sobre el
servicio, el controlador, el tipo de servicio o el tipo de controlador especificados.»**

## 10. Partición de recuperación

### El diseño de particiones de un equipo UEFI

**«El diseño de partición predeterminado para equipos basados en UEFI es: una partición del sistema,
un MSR, una partición de Windows y una partición de recuperación.»** Y **«Este diseño le permite usar
el cifrado de unidad BitLocker de Windows a través de Windows y a través del entorno de recuperación
de Windows.»**

| Partición | Requisitos literales de Microsoft |
|---|---|
| Sistema (ESP) | **«El dispositivo arranca en esta partición.»** Tamaño: **«Tamaño del sector de 512 bytes nativo o 512e: mínimo 200 MB»**; **«Tamaño de sector nativo de 4K: mínimo de 300 MB»**. **«La partición del sistema EFI debe tener formato con el formato de archivo FAT32.»** No debe contener otros archivos, **«incluidas las herramientas de Windows RE.»** |
| MSR | **«El tamaño de MSR es de 16 MB.»** **«MSR es una partición reservada que no recibe un identificador de partición. No puede almacenar datos de usuario.»** |
| Windows | **«La partición debe tener al menos 20 gigabytes (GB) de espacio en unidad para versiones de 64 bits»**; **«Se debe dar formato a la partición de Windows usando el formato de archivo NTFS.»**; y **«debe tener 16 GB de espacio libre después de que el usuario haya completado la Out Of Box Experience (OOBE)»** |
| Recuperación | La que sigue |

### La partición de recuperación

Es donde vive WinRE: Administración de discos la muestra como **«Recuperación»**, que **«Almacena
herramientas que admiten operaciones de recuperación de Windows cuando el equipo no se inicia o en
otros escenarios de problemas.»** Sus reglas:

- Tamaño mínimo, la suma de tres valores: el tamaño de la imagen `winre.wim` (que está en
  `\Windows\System32\Recovery\winre.wim` de la imagen que se despliega), el de las personalizaciones
  añadidas y **«Un espacio libre adicional de 250 MB, que Windows requiere para atender correctamente
  WinRE.»** Si el fabricante usa su propio guion de `diskpart`, **«el tamaño mínimo de partición
  recomendado es de 990 MB con un mínimo de 250 MB de espacio libre.»**
- Tipo: **«Debe configurarse con el identificador de tipo: DE94BBA4-06D1-4D40-A16A-BFD50179D6AC.»**
- Separada: **«Debe estar separada de la partición de Windows para permitir la conmutación automática
  por fallo y el arranque de particiones cifradas con Cifrado de unidad BitLocker de Windows.»**
- Ubicación: **«Debe colocarse inmediatamente después de la partición de Windows. Esto permite a
  Windows modificar y volver a crear la partición más adelante si las actualizaciones futuras
  requieren una imagen de recuperación más grande.»**
- Si hay particiones de datos, **«deben ubicarse después de la partición RE de Windows.»**

La ubicación importa por lo que hacen las actualizaciones de WinRE cuando la imagen nueva no cabe:
**«Si la partición existente de Windows RE se encuentra inmediatamente después de la partición de
Windows, la partición de Windows se reducirá de tamaño y se añadirá espacio a la partición de Windows
RE.»**; si no está detrás, se reduce la de Windows, se crea una partición de recuperación nueva y la antigua queda huérfana; y
si nada de eso es posible, **«la nueva imagen de WINDOWS RE se instalará en la partición de Windows.
La partición Windows RE existente estará huérfana.»**

En el despliegue con Windows PE y `diskpart`, a las particiones se les dan letras provisionales
(**«System=S, Windows=W y Recovery=R. La partición MSR no recibe una letra de unidad.»**); **«No use
X, ya que esta letra de unidad está reservada para Windows PE.»** Tras el reinicio, **«se asigna la
letra C a la partición de Windows y las otras particiones no reciben ninguna letra de unidad.»** El
estado de WinRE se consulta y gestiona con la orden REAgentC, que la referencia técnica cita entre
sus operaciones; su sintaxis no se ha leído y no se da.

Lo que no hay que hacer: la partición de recuperación aparece en Administración de discos sin letra
y, a veces, **«como 100 por ciento libre»**; **«La práctica recomendada es no modificar estas
particiones de ninguna manera.»**

## 11. Panel de configuración: Configuración y Panel de control

El enunciado dice «panel de configuración». En Windows 11 hay dos interfaces, y Microsoft dice
cuál prefiere:

- Configuración (epígrafe 9): **«Está diseñado teniendo en cuenta la simplicidad, la accesibilidad y la
  facilidad de uso, lo que proporciona una experiencia más intuitiva y fácil de usar que el Panel de
  control tradicional.»** Y **«La aplicación Configuración se actualiza continuamente para admitir las
  características más recientes de Windows.»**
- Panel de control: **«El Panel de control es una característica que ha formado parte de Windows
  durante mucho tiempo. Proporciona una ubicación centralizada para ver y manipular la configuración y
  los controles del sistema. Mediante una serie de applets, puede ajustar varias opciones que van
  desde la hora y fecha del sistema hasta la configuración de hardware, las configuraciones de red y
  más.»** **«Muchos de los valores de configuración del Panel de control se están migrando a la
  aplicación Configuración, que ofrece una experiencia más moderna y optimizada.»**

La recomendación: **«aunque el Panel de control sigue existiendo por motivos de compatibilidad y
para proporcionar acceso a algunas configuraciones que aún no se han migrado, se recomienda usar la
aplicación Configuración, siempre que sea posible.»** El Panel de control se abre buscándolo en
Inicio o con Win + R y `control`.

Lo que en este tema sigue llevando al Panel de control: **Programas > Programas y características**,
para desinstalar lo que Configuración no puede (epígrafe 2); el control deslizante del UAC, en
Sistema y seguridad (epígrafe 6); y Restaurar sistema y la protección del sistema, a través de
Propiedades del sistema (epígrafe 14).

## 12. Modo desarrollador

**«El modo de desarrollador desbloquea herramientas, configuraciones y características diseñadas para
compilar, implementar y probar aplicaciones en Windows.»** Dónde está depende de la versión: **«Antes
de Windows 11 25H2, esta configuración aparece en la página Para desarrolladores en Windows
configuración. En Windows 11 25H2 y versiones posteriores, aparecen en la sección Para
desarrolladores de la Configuración avanzada.»** Es decir, en 25H2: Configuración > Sistema >
Avanzado > Para desarrolladores, interruptor **Modo de desarrollador**, leer el aviso y aceptar.

Las condiciones: **«La habilitación del modo desarrollador requiere acceso de administrador. Si el
dispositivo es propiedad de una organización, esta opción puede deshabilitarse.»** Y quién lo
necesita: **«Si usas tu ordenador para actividades cotidianas normales (como juegos, exploración web,
correo electrónico u aplicaciones de Office), no es necesario activar el modo de desarrollador.»**

Qué activa:

- **«El modo de desarrollador reemplaza los requisitos de una licencia de desarrollador. Además de la
  carga lateral, la configuración de modo de desarrollador permite la depuración y opciones de
  implementación adicionales.»** La carga lateral (la página no la define; de oficio, instalar aplicaciones que no vienen de la tienda) se habilita también por directiva.
- Portal de dispositivos de Windows (Device Portal): **«Device Portal solo está habilitado (y las
  reglas de firewall solo están configuradas para él) cuando la opción Enable Device Portal está
  activada.»**
- Detección de dispositivos: **«permite que el dispositivo sea visible para otros dispositivos de la
  red a través de mDNS.»** (mDNS es el DNS de multidifusión, *multicast DNS*.) Al activarla **«se
  activará el servidor SSH.»** Esos servicios se usan **«cuando el dispositivo es un destino de
  implementación remota para aplicaciones empaquetadas MSIX.»**; **«Esta no es la implementación de
  OpenSSH de Microsoft»**.

Por seguridad, el modo desarrollador abre servicios de red: lo prudente en un puesto corporativo es
dejarlo desactivado salvo que el trabajo lo pida (consejo de oficio que se deduce de las condiciones
anteriores). En organizaciones se puede fijar por directiva; donde no hay editor de directivas,
Microsoft lo advierte: **«Puedes usar gpedit.msc para establecer las directivas de grupo para
habilitar el dispositivo, a menos que tengas Windows 10 Home o Windows 11 Home. Si lo hace, deberá
usar los comandos regedit o PowerShell para establecer las claves del Registro directamente para
habilitar el dispositivo.»**

## 13. Políticas de grupo (GPO)

### Qué son

**«La directiva de grupo es una característica de Windows que proporciona administración centralizada y
configuración de sistemas operativos, aplicaciones y configuración de usuario. Puede almacenar la
configuración de directiva de grupo localmente en el sistema de archivos o en Active Directory Domain
Services (AD DS).»** Cuando se usa con Active Directory, **«se almacena la configuración de directiva
de grupo en un objeto de directiva de grupo (GPO).»** **«Un GPO es una colección virtual de ajustes
de directivas, permisos de seguridad y ámbito de administración (SOM) que puede aplicar a usuarios y
equipos en Active Directory.»** Tiene dos piezas: el contenedor de directivas de grupo, en la
partición de dominio de Active Directory, y la plantilla de directiva de grupo, en la carpeta SYSVOL
de cada controlador de dominio. **«Cada GPO tiene un identificador único global (GUID)»**.

Cada directiva es de equipo o de usuario: **«Las configuraciones de equipo se aplican a nivel del
sistema y gestionan opciones como la gestión de energía y las normas de firewall. Las configuraciones
de usuario afectan únicamente al usuario actual»**. Las aplica en cada equipo una extensión del lado
cliente: **«Una extensión del lado cliente (CSE) aplica la configuración específica que dictan los
GPO, administrando tareas como actualizaciones del registro y configuraciones de seguridad.»**

Las herramientas: **«el Editor de directivas de grupo local (gpedit.msc) para la configuración
local o el Editor de objetos de directiva de grupo dentro de un complemento MMC relacionado con AD para
la configuración de todo el dominio.»**, y la GPMC, con la que, según la documentación de procesamiento, se bloquea la herencia, se edita el
GPO para el bucle invertido y se lanza la actualización de una UO. Recuérdese que
**«El Editor de directivas de grupo local no está disponible en la edición Windows Home.»** El editor
local **«es especialmente útil para administrar dispositivos que no forman parte de un dominio o que
no están administrados centralmente por una organización.»**

### Dónde se vinculan y en qué orden se aplican

**«Puede vincular GPO a varios niveles dentro de la jerarquía de AD, como sitios, dominios y unidades
organizativas (UO), que definen su ámbito de aplicación.»** **«Una UO es el contenedor de AD de nivel
más bajo al que puede asignar la configuración de directiva de grupo.»**, y **«También puede aplicar
algunas opciones de directiva de grupo en el nivel de dominio, especialmente las directivas de
contraseña.»**

El orden de procesamiento, que se suele recordar como local-sitio-dominio-UO:

1. **«Se aplica el GPO local.»**
2. **«Se aplican GPO vinculados a sitios.»**
3. **«Se aplican GPO vinculados a dominios.»**
4. **«Se aplican los GPO vinculados a unidades organizativas (UO). En una estructura de UO anidada, los GPO vinculados a las UO principales se aplican primero, seguidos de los GPo vinculados a las UO secundarias.»**

Y la regla que resuelve los conflictos: **«La secuencia de procesamiento de GPO es fundamental porque
cada aplicación de directiva posterior puede invalidar la configuración aplicada por directivas
anteriores.»** Es decir, gana lo más cercano: **«El contenedor de AD más cercano al equipo o el
usuario invalida la directiva de grupo establecida en un contenedor de AD de nivel superior.»**, y
**«La configuración de directiva de los GPO vinculados a contenedores de AD invalida la configuración
de directiva local.»** Otras tres reglas del mismo texto:

- **«La configuración de directiva relacionada con el equipo invalida la configuración de directiva relacionada con el usuario.»**
- Varios GPO en un mismo contenedor: **«El vínculo de GPO que tiene el orden de vínculo más bajo en la lista de vínculos de objetos de directiva de grupo tiene prioridad de forma predeterminada.»**
- **«La herencia se ignora cuando se establece la opción aplicada para ese vínculo de GPO o cuando se aplica la configuración de bloqueo de herencia.»** El bloqueo de herencia en una UO impide que le lleguen los GPO de arriba, pero no los marcados como aplicados (forzados): un GPO forzado en el dominio **«se aplican a todas las unidades organizativas de ese dominio.»**

Se puede afinar a quién se aplica un GPO con el filtrado de seguridad (por grupos) o con filtros
WMI: **«El GPO solo se aplica si el filtro WMI resulta verdadero.»** Y el modo de bucle invertido
**«aplica las opciones de configuración de usuario de objetos de directiva de grupo asignados al
equipo, independientemente de quién inicie sesión.»**, pensado para **«aulas, quioscos públicos y
áreas de recepción.»**; tiene un modo de combinación y uno de reemplazo.

### Cuándo se aplican

**«En el caso de los equipos, la directiva de grupo se aplica cuando se inicia el equipo. Para los
usuarios, la directiva de grupo se aplica al iniciar sesión.»** Ése es el procesamiento en primer
plano, que puede ser síncrono (no termina el arranque o el inicio de sesión hasta aplicarla) o
asíncrono. **«Todo el procesamiento de directivas debe completarse en un plazo de 60 minutos.»**
Después, la actualización en segundo plano: **«De forma predeterminada, se produce una actualización
cada 90 minutos. El sistema puede agregar un tiempo aleatorio de hasta 30 minutos al intervalo de
actualización.»** **«Los controladores de dominio comprueban los cambios en las directivas de equipo
cada cinco minutos.»** No todo se aplica en segundo plano: **«el procesamiento de redirección de
carpetas solo se produce cuando un usuario inicia sesión.»**, y los scripts sólo corren al iniciar y
apagar el equipo y al iniciar y cerrar sesión.

### `gpupdate` y `gpresult`

| Orden | Qué hace | Opciones |
|---|---|---|
| `gpupdate` | **«Actualiza la configuración de directiva de grupo.»** | `/force`: **«Vuelve a aplicar todas las configuraciones de directiva. De forma predeterminada, solo se aplican las opciones de configuración de directiva que han cambiado.»**; `/target:computer` o `user`; `/boot` y `/logoff` reinician o cierran sesión para las extensiones que sólo actúan al arrancar o al iniciar sesión, como la instalación de software |
| `gpresult` | **«Muestra información del conjunto resultante de directivas (RSoP)»** | `/r`: **«Muestra los datos de resumen de RSoP.»**; `/h` guarda un informe en HTML; `/scope user` o `computer`. **«Excepto cuando se usa /?, debe incluir una opción de salida, /r, /v, /z, /x o /h.»** |

Desde PowerShell, `Invoke-GPUpdate` fuerza la actualización en el equipo local o en uno remoto, y la
GPMC puede lanzarla para toda una UO.

### Ejemplos en Windows 11

Las directivas de Windows Update de este tema (epígrafe 15) viven en **«Configuración del
equipo\Plantillas administrativas\Componentes de Windows\Windows Update»**. Las de seguridad, bajo
**«Configuración de Windows/Configuración de seguridad/Directivas locales/Opciones de seguridad»**,
donde está, por ejemplo, **«Cuentas: Bloquear cuentas Microsoft»** (la referencia de WinRE avisa de
que una configuración de esta directiva da problemas al restaurar el sistema). El comportamiento de la
solicitud de elevación del UAC también se fija por directiva: **«Control de cuentas de usuario:
Comportamiento de la solicitud de elevación para administradores en Administración modo de
aprobación»** [sic]. El paquete
`.msi` se puede desplegar por directiva de grupo (epígrafe 2). Y la configuración aplicada por
directiva prevalece sobre la que el usuario cambie en Seguridad de Windows (epígrafe 6).

## 14. Puntos de restauración

### Protección del sistema

**«La protección del sistema en Windows es una característica de recuperación diseñada para ayudarte
a proteger la configuración del sistema. Consiste principalmente en crear y administrar puntos de
restauración, que son instantáneas de los archivos del sistema, las aplicaciones instaladas, el
Registro de Windows y la configuración del sistema en un momento específico.»** El dato que más se
pregunta: **«Aunque no está habilitado de forma predeterminada, se recomienda habilitar la protección
del sistema.»**

Activarla: buscar **«Crear un punto de restauración»** en Inicio (o Win + R y
`systempropertiesprotection.exe`); en **Propiedades del sistema**, pestaña **Protección del
sistema**, **Configurar...**; **Activar protección del sistema**; el control deslizante fija **«la
cantidad máxima de espacio en disco que puede usar Protección del sistema.»**; **Aplicar**. A partir
de ahí, **«La protección del sistema creará puntos de restauración automáticamente, cuando sea
necesario.»**, por ejemplo **«durante eventos importantes, como instalaciones o actualizaciones de
software»**. Crear uno a mano: misma ventana, **Crear...**, escribir una descripción y **Crear**.

### Restaurar sistema

**«Cuando se selecciona un punto de restauración, Restaurar sistema revierte los archivos de sistema,
la configuración del Registro y los programas instalados al estado que estaban en el momento en que
se creó el punto de restauración.»**, y lo hace **«sin afectar a sus archivos personales»**.

- Desde Windows: **«En el Panel de control, seleccione Recuperación y elija Abrir Restaurar
  sistema.»**, o Win + R y `rstrui.exe`. Se elige el punto (con **«Mostrar más puntos de restauración»**
  si no aparece), opcionalmente **«Buscar programas afectados»**, y **Finalizar**; **«Después de
  aplicar el punto de restauración, Windows se reinicia automáticamente.»**
- Desde WinRE, si Windows no arranca: **«Una vez en Windows RE, seleccione Solucionar problemas, elija
  Opciones avanzadas y, a continuación, Restaurar sistema.»** Si el disco está cifrado, **«necesitarás
  la clave de BitLocker para completar esta tarea.»**

### La restauración a un momento dado (restauración puntual)

Es otra cosa, más reciente y más amplia: **«La restauración puntual te ayuda a recuperar tu PC
Windows devolviéndolo al estado exacto en el que se encontraba en un momento anterior. Esto incluye
las aplicaciones, la configuración y los archivos.»** Requiere Windows 11 24H2 o posterior.

| Ajuste | Valor predeterminado |
|---|---|
| Activación | Activada en equipos no administrados; **«Esta característica está deshabilitada de manera predeterminada en los dispositivos administrados por TI. A partir de Windows 11, versión 26H2, se habilitará de forma predeterminada.»** Para que venga activada de forma predeterminada, **«el volumen del sistema operativo Windows debe ser de 200 GB o más»**; con volúmenes menores **«pueden habilitar la función manualmente»** |
| Frecuencia | **«Cada 24 horas»** |
| Retención | **«72 horas»**: **«Los puntos de restauración se conservan hasta 72 horas. Después, se eliminan automáticamente para liberar espacio.»** |
| Espacio máximo | **«2% del disco»** |

Frecuencia y retención **«solo se puede configurar en dispositivos Windows que ejecuten la edición
Enterprise de Windows.»**, y **«Solo los administradores locales pueden ver o editar configuraciones
para restaurarlas en un momento determinado.»** Se configura en Configuración > Sistema >
Recuperación > Restauración puntual, pero se aplica sólo desde WinRE (**Solucionar problemas** >
restauración puntual, con la clave de BitLocker si se pide). Su riesgo: **«Los cambios realizados
después de ese punto de restauración se perderán. Esto incluye nuevos archivos, instalaciones de
aplicaciones, cambios de configuración y contraseñas.»**

La comparación que hace Microsoft: **«La restauración a un momento dado revierte todo: los archivos
personales, las aplicaciones y la configuración a una instantánea automática.»**; **«Restaurar sistema
solo revierte la configuración y los archivos del sistema. Los archivos personales no se ven
afectados. Está disponible tanto en Windows 10 como en Windows 11.»** Y el orden: **«Si ambas están
disponibles, pruebe primero la restauración a un momento dado, ya que es la más completa.»**
Restaurar sistema queda para cuando la otra no está o hay que ir **«a un punto de restauración
anterior a 3 días»**.

Ninguno de los dos es una copia de seguridad: los puntos viven en el mismo disco del equipo (son
**«instantáneas de todo el sistema almacenados localmente en el equipo»** [sic]), y si el disco se
pierde, se pierden con él. Las copias de seguridad y la recuperación de datos son del tema 3.

## 15. Opciones de reinicio para instalar actualizaciones

### Lo que ve el usuario

**«Para terminar de instalar una actualización, deberá reiniciarse el dispositivo. Windows intentará
reiniciar el dispositivo cuando no lo estés usando.»** Las opciones, todas en Configuración > Windows
Update:

| Opción | Qué hace |
|---|---|
| Horas activas | **«Puedes definir las horas activas para hacernos saber cuando usas normalmente tu PC y ayudar a evitar que se produzcan reinicios en momentos inconvenientes.»** En Opciones avanzadas > Horas activas, **Automáticamente** (según la actividad) o **Manual** |
| Programar el reinicio | **«Selecciona Programar el reinicio y elige un momento conveniente para ti.»** |
| Reiniciar ahora | En Windows Update, en el icono de la bandeja, o desde Inicio > Inicio/apagado: **«Actualizar y reiniciar o Actualizar y apagar.»** |
| Pausar | **«puedes pausar las actualizaciones hasta 35 días.»** Al terminar la pausa, Windows busca e instala las últimas |
| Obtener las últimas actualizaciones en cuanto estén disponibles | Adelanta lo que no es de seguridad; **«Si establece el botón de alternancia en Desactivado o Activado, seguirá recibiendo las actualizaciones de seguridad normales como de costumbre.»** |

Las conexiones de uso medido frenan la descarga: **«a menos que tenga una conexión de uso medido, las
actualizaciones no se descargarán hasta que las obtenga»** [sic].

### Un reinicio al mes

Desde el verano de 2026 Windows agrupa los reinicios (artículo KB5121772, publicado el 14-08-2026,
para Windows 11 24H2, 25H2 y 26H1): **«A partir de las actualizaciones de Windows publicadas el 28 de
julio de 2026, Windows reúne estas actualizaciones, por lo que solo podrá reiniciar el equipo una vez
al mes.»** Las que esperan a la actualización de seguridad mensual son **«Actualizaciones de
controladores entregadas a través de Windows Update»**, **«Actualizaciones de .NET»** y
**«Actualizaciones de firmware»**. Las que siguen instalándose en cuanto llegan: **«Actualizaciones
de inteligencia de seguridad de Microsoft Defender»**, **«Actualizaciones de componentes de IA»**,
**«Actualizaciones críticas o aceleradas de controladores»** y **«Actualizaciones de emergencia y
fuera de banda»**. **«Una vez preparadas las actualizaciones, Windows programa el reinicio fuera de las
horas activas.»** Y dos avisos: **«Esta experiencia se está implementando gradualmente y es posible
que aún no esté disponible en todos los dispositivos.»**; **«Windows no publicará actualizaciones
indefinidamente.»** [sic: «no retendrá»]: si una actualización combinada lleva mucho tiempo
esperando, Windows la instala y reinicia.

Los dos tipos de actualización: **«Las actualizaciones de funciones se distribuyen una vez al año e
incluyen nuevas funcionalidades y capacidades»**; **«Las actualizaciones de calidad son más frecuentes
y principalmente incluyen pequeñas correcciones y actualizaciones de seguridad.»** (La misma página de
preguntas frecuentes dice en otro punto que las de funciones **«suelen ocurrir dos veces al año»**;
la página de versiones de Windows 11, citada al principio, fija la cadencia anual.)

### Lo que configura el administrador

**«Puede usar la configuración de directiva de grupo, la administración de dispositivos móviles (MDM)
o el registro de Windows para configurar cuándo se reiniciarán los dispositivos después de instalar
una actualización de Windows.»** **«No se recomienda editar directamente el registro de Windows.»**

| Qué | Directiva de grupo (en Configuración del equipo\Plantillas administrativas\Componentes de Windows\Windows Update) | MDM |
|---|---|---|
| Programar la instalación | **«Configurar Novedades automática»** [sic: actualizaciones], opción **«4 : Descarga automática y programación de la instalación»**, con hora de instalación | — |
| Horas activas | **«Desactivar reinicio automático para actualizaciones durante horas activas»**, con hora de inicio y fin | **«ActiveHoursStart»**, **«ActiveHoursEnd»** |
| Intervalo máximo de horas activas | **«Especificar intervalo de horas activas para reinicios automáticos»** | **«ActiveHoursMaxRange»** |
| Plazo antes del reinicio forzoso | **«Especificar fecha límite antes del reinicio automático para la instalación de actualizaciones»**: **«El valor mínimo es de dos días y el valor máximo es de dos semanas (14 días).»** | — |
| Notificaciones | **«Mostrar opciones para las notificaciones de actualización»**: 0 las predeterminadas, 1 casi ninguna salvo las de reinicio, 2 ninguna | **«UpdateNotificationLevel»** |

Datos fijos: **«De forma predeterminada, las horas activas son de 8 a. m. a 5 p. m. en equipos.»**;
**«La longitud máxima de las horas activas para Windows 10, versión 1607 y Windows Server 2016 es 12.
Las versiones posteriores admiten una duración máxima de 18 horas.»**; y **«Si el reinicio no se
realiza correctamente después de un período predeterminado de siete días, el usuario ve una
notificación de que se requiere un reinicio.»** La directiva que impide reiniciar con usuarios
conectados tiene una trampa: con conexiones de escritorio remoto, **«solo las sesiones RDP activas
se consideran usuarios con sesión iniciada»**. Varias directivas antiguas de avisos de reinicio
llevan la marca **«Esta directiva es una directiva heredada y no es aplicable a Windows 11.»**

## Lo que este tema no da, y dónde está

- PowerShell como lenguaje (variables, tuberías, estructuras): tema 7. Aquí sólo aparecen los cmdlets
  que sirven a una tarea de Windows 11 (`Get-Service`, `Initialize-Disk`, `Invoke-GPUpdate`).
- Active Directory, el dominio, el controlador de dominio y la gestión de usuarios y recursos: tema 8.
  Aquí la directiva de grupo se estudia desde el puesto cliente, y las cuentas, desde el equipo local;
  la orden `net user`, también en el tema 8.
- Instalar aplicaciones desde la línea de órdenes con WinGet: tema 7. Comprobar y reparar los archivos
  del sistema con `sfc`: tema 2. Habilitar y usar el Escritorio remoto (RDP): tema 10.
- Antivirus, malware, cortafuegos y VPN en detalle: tema 14. Copias de seguridad, clonación y
  recuperación de datos: tema 3. Diagnóstico de averías y códigos de error del hardware: tema 2.
  Virtualización e Hyper-V: tema 10. Microsoft 365, OneDrive y Teams: tema 11. Redes, IPv4/IPv6 y
  Wi-Fi como tecnología: tema 13.
- Las novedades propias de Windows 11 26H2, publicada el 29-09-2026: no se han estudiado.
- La sintaxis de REAgentC, la lista completa de applets del Panel de control y sus órdenes `.cpl`, y
  la configuración de Microsoft Store: no se han leído en una fuente vigente para Windows 11 y no se
  dan. La página de soporte de Microsoft sobre órdenes del Panel de control que se consultó describe
  Windows 95, 98 y NT, y no se ha usado.
- La consola Servicios (`services.msc`), su pestaña de dependencias y dónde está en las propiedades
  del servicio se dan como oficio, sin cita.
- La versión de Windows, las ediciones y la configuración de los puestos de la RTVA y de CSRTV no
  constan en ningún documento publicado.

## Trazabilidad

Todas las fuentes se leyeron el 05-10-2026 en su versión en línea de ese día, salvo las cuatro
añadidas en el remate (configuración de inicio, cuentas de usuario, cuentas locales y Windows Hello),
leídas el 06-10-2026, y las tres de las remisiones a los temas 2, 7 y 10 (`sfc`, WinGet y Habilitar
Escritorio remoto), releídas en la revisión del remate: `sfc` y Escritorio remoto, el 05-10-2026;
WinGet, el 06-10-2026. Las páginas de Microsoft
no llevan versión fechada; cuando la muestran, se anota la fecha de su última actualización.

| Fuente | Qué sostiene |
|---|---|
| Microsoft Learn (es-es), «Información de versión de Windows 11» (windows/release-health/windows11-release-information) | Cadencia anual, 24 y 36 meses, segundo martes, tabla de versiones, 26H1, LTSC 2024 |
| Microsoft Learn, «Novedades de Windows 11, versión 25H2» | Paquete de habilitación, soporte de 24 y 36 meses |
| Microsoft Learn, «Windows 10 Home y Pro» (ciclo de vida) | Fin de soporte el 14-10-2025, 22H2 versión final |
| Microsoft Learn, «Requisitos de Windows 11» (actualizada el 14-07-2026, fecha que muestra la versión en inglés) | Requisitos de hardware, Home y cuenta Microsoft, actualización desde Windows 10, modo S, BitLocker To Go, Hyper-V, Acoplar, máquinas virtuales |
| Microsoft Learn, «Escenarios y herramientas de implementación de Windows» | ADK, DISM, USMT, Windows SIM, Diseñador de configuraciones, VAMT, Windows PE, WinRE, WDS, WSUS, UEFI y BIOS, arranque seguro, MBR2GPT, límite de 2,2 TB de MBR |
| Microsoft Learn, «Introducción a Windows Autopilot» y «¿Qué es Microsoft Intune?» | Autopilot, Intune, MDM, MAM, Entra ID |
| Microsoft Learn, «Particiones de disco duro basadas en UEFI/GPT» (actualizada el 24-09-2026) | GPT y 128 particiones, ESP, MSR, partición de Windows, partición de recuperación, diseño predeterminado, letras en Windows PE, 990 MB |
| Microsoft Learn, «Introducción a la Administración de discos» (14-08-2025) e «Inicialización de discos nuevos» (16-08-2025) | Tareas de la consola, tres particiones, estilos GPT y MBR, inicialización |
| Microsoft Learn, «Cómo usar el complemento de administración de discos para administrar discos básicos y dinámicos» (KB 323442, escrito para Windows Server 2003) | Disco básico y dinámico, conversión, particiones MBR, particiones que no se borran |
| Microsoft Learn, referencia de órdenes de Windows: `diskpart` y sus órdenes `list`, `select disk`, `clean`, `convert gpt`, `create partition primary`, `assign` y `format` (esta última en la versión archivada de Windows Server 2012), `defrag`, `cipher`, `ipconfig`, `ping`, `tracert`, `netstat`, `msiexec`, `gpupdate`, `gpresult`, `sc.exe query` | Definiciones, opciones y valores predeterminados de cada orden |
| Microsoft Learn, «Formatos de ruta de acceso de archivo en los sistemas Windows» (.NET) | Rutas UNC |
| Microsoft Learn, PowerShell, `Get-Service` | `-RequiredServices` y `-DependentServices` |
| Microsoft Learn, «Entorno de recuperación de Windows (Windows RE)» | WinRE, herramientas, entradas, arranque automático, menú Inicio avanzado, seguridad, red, actualización de la partición |
| Microsoft Learn, «Seguridad de Windows» | Secciones, apertura, prioridad de las directivas, Defender con antivirus de terceros |
| Microsoft Learn, «Introducción a BitLocker» | BitLocker, TPM, requisitos, ediciones, cifrado de dispositivo |
| Microsoft Learn, «Información general de Control de cuentas de usuario» (27-05-2026) y «Cómo funciona el Control de cuentas de usuario» (23-04-2026) | UAC, tokens, ventanas de credenciales y consentimiento, colores, escudo, escritorio seguro |
| Microsoft Learn, «Configuración para desarrolladores» | Modo desarrollador |
| Microsoft Learn, «Introducción a la directiva de grupo para Windows Server» (18-06-2025) y «Procesamiento de directivas de grupo» | GPO, componentes, equipo y usuario, CSE, vinculación, orden, herencia, forzado, filtrado, bucle invertido, 60 y 90 minutos, `gpupdate.exe`, `Invoke-GPUpdate` |
| Microsoft Learn, «Administrar los reinicios de los dispositivos después de las actualizaciones» | Directivas, MDM y registro de reinicios, horas activas, siete días, fecha límite, notificaciones, directivas heredadas |
| Soporte de Microsoft (es-es): «Formas de instalar Windows 11» (actualizado el 04-02-2025), «Crear medios de instalación para Windows», «Reinstalar Windows con el soporte de instalación» | Métodos de instalación, medio USB, instalación limpia, activación |
| Soporte de Microsoft: «Personalizar la barra de tareas en Windows», «Personalizar el menú Inicio de Windows», «Acople sus ventanas», «Explorador de archivos en Windows», «Desinstalar o quitar aplicaciones y programas en Windows», «Configurar las aplicaciones de inicio en Windows», «Métodos abreviados de teclado de Windows» (descargada el 02-09-2026 para otro tema y comprobada sobre esa copia) | Interfaz y aplicaciones |
| Soporte de Microsoft: «Administración de discos en Windows», «Actualizar controladores a través de Administrador de dispositivos», «Códigos de error en el Administrador de dispositivos de Windows» | Discos y controladores |
| Soporte de Microsoft: «Tareas y configuración de red esenciales en Windows», «Conectarse a una red Wi-Fi en Windows» | Red e Internet |
| Soporte de Microsoft: «Opciones de recuperación en Windows», «Protección del sistema», «Restauración del sistema», «Restauración puntual para Windows» | Recuperación y puntos de restauración |
| Soporte de Microsoft: «Configuración del control de cuentas de usuario» (la página servida en es-es está en inglés) | Niveles del UAC |
| Soporte de Microsoft: «Notificaciones y No molestar en Windows», «Personalice su experiencia de Windows con temas», «Personalizar los colores en Windows», «Explorar la configuración de Windows», «Herramientas de configuración del sistema en Windows» | Notificaciones, personalización, Configuración, herramientas avanzadas, Panel de control |
| Soporte de Microsoft: «Un reinicio al mes para las actualizaciones de Windows» (KB5121772, 14-08-2026), «Mantener el equipo al día con las horas activas», «Windows Update: Preguntas más frecuentes», «Obtener actualizaciones de Windows tan pronto como estén disponibles para el dispositivo» | Reinicios para actualizar |
| Soporte de Microsoft (es-es): «Configuración de inicio de Windows» | Configuración de inicio, sus nueve opciones, modo seguro y cómo salir de él |
| Soporte de Microsoft (es-es): «Administrar cuentas de usuario en Windows» | Agregar, quitar y cambiar el tipo de cuenta, cuenta local, cuenta profesional o educativa, recomendación de la cuenta Microsoft y de pocos administradores |
| Microsoft Learn (es-es), «Cuentas locales» (13-04-2026) | Cuentas locales, Usuarios y grupos locales, Administrador e Invitado integrados, modo seguro y cuenta de administrador, Ejecutar como administrador |
| Soporte de Microsoft, «Configure Windows Hello» (la dirección es-es redirige a la página en inglés) | Opciones de inicio de sesión: cara, huella y PIN, requisitos |
| Microsoft Learn, «sfc» (referencia de órdenes de Windows, en inglés) | `sfc /scannow`, comprobación y reparación de archivos protegidos, grupo Administradores |
| Microsoft Learn (es-es), «Instalación de PowerShell en Windows» | WinGet incluido en Windows 11 |
| Microsoft Learn (es-es), «Habilitar Escritorio remoto en el equipo» | Ruta Configuración > Sistema > Escritorio remoto |
| SNIA, *Online Dictionary*, «trim» | Definición de TRIM |

Las páginas de Microsoft en castellano son traducción automática y traen erratas; se citan tal cual y
se señalan con [sic]. Varias páginas del soporte, al pasar a texto, pierden el orden de las rutas de
menú (salen como «Configuración>,Solución>de problemas del sistema>»); las rutas de menú se dan en
redonda, reconstruidas, y no se citan en negrita. Dos discrepancias de las propias fuentes, señaladas
donde salen: la página del menú Inicio anuncia seis áreas y enumera siete; y las preguntas frecuentes
de Windows Update dicen en un punto que las actualizaciones de funciones son anuales y en otro que
suelen ser dos al año (la página de versiones fija la cadencia anual). La de
Particiones UEFI/GPT llama a GPT «sistema de archivos»; se señala.

Oficio sin fuente detrás, y así se declara: que arrastrar dentro de la misma unidad mueve y entre
unidades copia, y que lo borrado de una unidad de red o extraíble no pasa por la papelera; la razón de
que el despliegue corporativo prefiera `.msi` a `.exe`; el atajo de memoria de `netstat` y `tracert`;
la explicación de por qué `C:` no cabe en una ruta UNC y de que el dólar oculta el recurso
administrativo; la distinción entre cifrado de volumen y de fichero; la lectura del UAC como punto de
decisión; el consejo de mirar las dependencias cuando un servicio no arranca, y la consola `services.msc`;
el uso de revertir el controlador cuando el fallo sigue a una actualización; qué es la carga lateral; la consecuencia
práctica de la red pública; el consejo de dejar desactivado el modo desarrollador en un puesto
corporativo; el caso práctico del modo seguro tras un controlador que impide arrancar, y la advertencia
de no confundir la casilla Arranque seguro de `msconfig` con el arranque seguro de UEFI; que la cuenta
Invitado no es la que se da a un usuario nuevo del puesto; y la secuencia de `diskpart` del epígrafe 3, que se construye con órdenes cuya sintaxis
sí está citada.
