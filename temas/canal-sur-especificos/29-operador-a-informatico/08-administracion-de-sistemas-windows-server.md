# Tema 8 del específico de Operador/a Informático · Administración de sistemas Windows Server

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 8 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Documentación oficial de Microsoft en Microsoft Learn (Windows Server 2025, Active Directory Domain Services, módulo ActiveDirectory de PowerShell, referencia de órdenes de Windows) y artículos de soporte técnico de Microsoft. Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las páginas citadas, en línea el 05-10-2026 y leídas ese día; la versión de producto es la vigente el 24-09-2026 (Windows Server 2025) |
| Extensión | 12.400 palabras aproximadamente, con tablas, siglas y ejemplos de órdenes |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); Servicios de dominio de
Active Directory (AD DS, *Active Directory Domain Services*) y Active Directory Lightweight Directory
Services (AD LDS), la variante ligera; protocolo ligero de acceso a directorios (LDAP, *lightweight
directory access protocol*); sistema de nombres de dominio (DNS); protocolo de configuración dinámica
de host (DHCP); bloque de mensajes del servidor (SMB, *server message block*), el protocolo de
archivos compartidos de Windows; convención de nomenclatura universal (UNC, *universal naming
convention*), la forma `\\servidor\recurso` de las rutas de red; sistema de archivos distribuido (DFS),
con sus espacios de nombres (DFSN) y su replicación (DFSR), y el servicio de replicación de archivos
(FRS) al que esta sustituyó; sistema de archivos de nueva tecnología (NTFS) y sistema de archivos
resistente (ReFS); unidad organizativa (UO, en inglés OU); objeto de directiva de grupo (GPO);
operaciones de maestro único flexible (FSMO, *flexible single master operations*); controlador de
dominio principal (PDC, *primary domain controller*); identificador relativo (RID) e identificador de
seguridad (SID); controlador de dominio de solo lectura (RODC, *read-only domain controller*); modo
de restauración de servicios de directorio (DSRM); centro de distribución de claves (KDC) y vale de
concesión de vales (TGT, *ticket-granting ticket*) del protocolo Kerberos; administrador de cuentas
de seguridad (SAM, *Security Accounts Manager*), cuyo nombre de cuenta es el nombre corto de inicio de
sesión; nombre distintivo (DN, *distinguished name*); identificador único global (GUID); lista de
control de acceso (ACL) y lista de control de acceso discrecional (DACL); entrada de control de acceso
(ACE); Herramientas de administración remota del servidor (RSAT); Centro de administración de Active
Directory (ADAC); Microsoft Management Console (MMC); Canal de mantenimiento a largo plazo (LTSC);
solución de contraseñas de administrador local de Windows (Windows LAPS); red de área extensa (WAN);
llamada a procedimiento remoto (RPC); protocolo de control de transmisión (TCP) y de datagramas de
usuario (UDP); seguridad de la capa de transporte (TLS) y su antecesora (SSL); protocolo de
internet (IP); motor de almacenamiento extensible (ESE), la base de datos de Active Directory;
protocolo de escritorio remoto (RDP); interfaz gráfica de usuario (GUI); tecnologías de la
información (TI); valores separados por comas (CSV, *comma-separated values*), el formato de fichero
de las altas masivas; NTLM, el protocolo de autenticación de Windows anterior a Kerberos, y KRBTGT,
la cuenta de servicio de Kerberos, que se citan por su nombre; SYSVOL, nombre de la carpeta que
comparten los controladores de dominio; el Editor ADSI, nombre de una consola de Microsoft; las
letras de permiso de `icacls` (`N`, `F`, `M`, `RX`, `R`, `W`, `D`), que se explican en su tabla; y el
nombre NetBIOS, el nombre corto heredado de las redes Windows.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 8): «Administración de
> sistemas Windows Server: Active Directory, servicio de directorio, controlador de dominio, gestión
> básica de usuarios, recursos y servicios asociados.»

Qué se puede preguntar: qué versión de Windows Server es la vigente, qué ediciones tiene y qué
distingue la instalación Server Core de la de Experiencia de escritorio; con qué herramientas se
administra un servidor (Administrador del servidor, Windows Admin Center, RSAT, PowerShell); qué es
un directorio y un servicio de directorio; qué guarda AD DS y qué son el esquema, el catálogo global
y la replicación; qué son un bosque, un dominio, un árbol y una unidad organizativa, y qué relación
de confianza une a los dominios de un bosque; qué son los sitios; qué protocolos y puertos usa
Active Directory (LDAP 389 y 636, catálogo global 3268 y 3269, Kerberos 88, DNS 53, SMB 445); qué
son los niveles funcionales; qué hace un controlador de dominio, qué son los cinco roles FSMO y
cuáles son de bosque y cuáles de dominio; qué es un RODC y por qué no puede tener roles FSMO; qué
hay en SYSVOL; cómo se instala AD DS y se promueve un servidor a controlador de dominio, qué
credenciales hacen falta y qué se instala con él por defecto; qué cuentas crea el dominio; cómo se
crea, se deshabilita, se desbloquea, se restablece y se elimina una cuenta; qué distingue un grupo
de seguridad de uno de distribución y los ámbitos universal, global y dominio local; qué grupos
predeterminados hay y qué puede hacer cada uno; qué distingue un derecho de un permiso; qué hacen
DNS, DHCP, SMB, DFS y las directivas de grupo en un dominio. En la aplicación práctica: dar de alta un
usuario en una UO con su contraseña temporal, meterlo en un grupo y darle acceso a una carpeta
compartida; atender a un usuario bloqueado; unir un equipo al dominio; decidir el ámbito de un grupo;
y diagnosticar por qué un equipo no encuentra el controlador de dominio.

<!-- indice -->

## Índice

- [1. Administración de sistemas Windows Server](#1-administración-de-sistemas-windows-server)
  - [La versión vigente y sus ediciones](#la-versión-vigente-y-sus-ediciones)
  - [Server Core y Experiencia de escritorio](#server-core-y-experiencia-de-escritorio)
  - [Las herramientas de administración](#las-herramientas-de-administración)
  - [Las tareas del administrador](#las-tareas-del-administrador)
- [2. Active Directory y el servicio de directorio](#2-active-directory-y-el-servicio-de-directorio)
  - [Directorio y servicio de directorio](#directorio-y-servicio-de-directorio)
  - [Qué incluye AD DS](#qué-incluye-ad-ds)
  - [El modelo lógico: bosque, dominio, árbol y unidad organizativa](#el-modelo-lógico-bosque-dominio-árbol-y-unidad-organizativa)
  - [Relaciones de confianza](#relaciones-de-confianza)
  - [Los sitios: la estructura física](#los-sitios-la-estructura-física)
  - [LDAP, Kerberos y los puertos de Active Directory](#ldap-kerberos-y-los-puertos-de-active-directory)
  - [Niveles funcionales](#niveles-funcionales)
- [3. El controlador de dominio](#3-el-controlador-de-dominio)
  - [Qué hace un controlador de dominio](#qué-hace-un-controlador-de-dominio)
  - [Los roles de maestro de operaciones (FSMO)](#los-roles-de-maestro-de-operaciones-fsmo)
  - [Catálogo global](#catálogo-global)
  - [Controlador de dominio de solo lectura (RODC)](#controlador-de-dominio-de-solo-lectura-rodc)
  - [SYSVOL](#sysvol)
  - [Instalar AD DS y promover el controlador](#instalar-ad-ds-y-promover-el-controlador)
  - [Diagnóstico: DCDiag](#diagnóstico-dcdiag)
- [4. Gestión básica de usuarios](#4-gestión-básica-de-usuarios)
  - [Las cuentas predeterminadas](#las-cuentas-predeterminadas)
  - [Usuarios y equipos de Active Directory y el Centro de administración](#usuarios-y-equipos-de-active-directory-y-el-centro-de-administración)
  - [Crear una cuenta de usuario](#crear-una-cuenta-de-usuario)
  - [Restablecer, desbloquear, deshabilitar y eliminar](#restablecer-desbloquear-deshabilitar-y-eliminar)
  - [La gestión desde PowerShell y la línea de órdenes](#la-gestión-desde-powershell-y-la-línea-de-órdenes)
  - [Grupos: tipos y ámbitos](#grupos-tipos-y-ámbitos)
  - [Los grupos predeterminados](#los-grupos-predeterminados)
  - [Derechos y permisos](#derechos-y-permisos)
  - [Unidades organizativas y delegación](#unidades-organizativas-y-delegación)
  - [Unir un equipo al dominio](#unir-un-equipo-al-dominio)
- [5. Recursos y servicios asociados](#5-recursos-y-servicios-asociados)
  - [DNS](#dns)
  - [DHCP](#dhcp)
  - [Carpetas compartidas: SMB y permisos NTFS](#carpetas-compartidas-smb-y-permisos-ntfs)
  - [Espacios de nombres DFS](#espacios-de-nombres-dfs)
  - [Impresoras](#impresoras)
  - [Directivas de grupo](#directivas-de-grupo)
  - [Windows LAPS](#windows-laps)
  - [Caso práctico completo](#caso-práctico-completo)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Administración de sistemas Windows Server

### La versión vigente y sus ediciones

Microsoft publica Windows Server por dos canales: **«el Canal de mantenimiento a largo plazo y el
canal anual. El LTSC ofrece una opción a más largo plazo centrada en un ciclo de vida tradicional de
actualizaciones de seguridad y calidad.»** Y fija cuál es la versión de hoy: **«Windows Server 2025
es la versión de LTSC actual.»** Es la que se estudia. Su página de información de versión da estas
fechas, en formato año-mes-día:

| Versión | Disponible desde | Fin del soporte estándar | Fin del soporte extendido |
|---|---|---|---|
| Windows Server 2025 | 2024-11-01 | 2029-11-13 | 2034-11-14 |
| Windows Server 2022 | 2021-08-18 | 2026-10-13 | 2031-10-14 |
| Windows Server 2019 | 2018-11-13 | Fin de actualización | 2029-01-09 |
| Windows Server 2016 | 2016-08-02 | Fin de actualización | 2027-01-12 |

Windows Server 2022 seguía, pues, en soporte estándar el 24-09-2026, pero por pocos días. La regla
general: **«Windows Server se rige por la directiva de ciclo de vida fijo.»**

Las ediciones de Windows Server 2025 que da la página de ciclo de vida son **«Datacenter,
Datacenter: Azure Edition y Standard»**, y su lista de ediciones añade Essentials; la tabla de
versiones da para Windows Server 2025 Datacenter y Standard. La página de comparación de ediciones
marca, rol por rol, cuáles trae cada una; muchos están en las tres (los clústeres de conmutación por
error, por ejemplo, figuran en Standard, Datacenter y Datacenter: Azure Edition). Lo que cambia en la
licencia de máquinas virtuales de cada edición no se ha confirmado en fuente y no se da.

Novedades de la versión 2025 que tocan al tema:

- Actualizar sin reiniciar: **«Puede usar Hotpatch para aplicar actualizaciones de seguridad del
  sistema operativo sin reiniciar la máquina.»**, en equipos conectados a Azure Arc; la página de novedades lo
  da como versión preliminar.
- La base de datos de Active Directory: **«Active Directory usa una base de datos del motor de
  almacenamiento extensible (ESE) desde que se incluyera en Windows 2000 que usa un tamaño de página
  de base de datos de 8k.»** La versión 2025 añade una **«Función opcional de tamaño de página de
  base de datos de 32k»**, que exige el nuevo nivel funcional (epígrafe 2).
- Más seguridad en LDAP: **«todas las nuevas implementaciones de Active Directory requieren la firma
  LDAP (sellado) de forma predeterminada»**, y LDAP admite TLS 1.3.

### Server Core y Experiencia de escritorio

Al instalar se elige entre dos opciones. **«La opción Server Core es una opción de instalación mínima
que está disponible al implementar la edición Standard o Datacenter de Windows Server. Server Core
incluye la mayoría de los roles de servidor, pero no todos. Server Core tiene una superficie de disco
más pequeña y, por tanto, una superficie de ataque más pequeña debido a una base de código menor.»**
La otra es **«Servidor con experiencia de escritorio»**, con interfaz gráfica completa.

En Server Core **«no hay escritorio en Server Core, por diseño.»** Se administra **«de forma remota
a través de la línea de comandos, PowerShell, una herramienta de GUI como RSAT o Windows Admin
Center.»** Tampoco tiene **«ninguna herramienta de accesibilidad»**, ni experiencia de configuración
inicial, ni audio. El ejemplo que da Microsoft de servidor que no necesita escritorio es el de
virtualización: **«un servidor de Hyper-V no necesita una interfaz gráfica de usuario (GUI), ya que se
pueden administrar prácticamente todos los aspectos de Hyper-V desde la línea de comandos mediante
Windows PowerShell o de forma remota mediante el Administrador de Hyper-V.»**

### Las herramientas de administración

| Herramienta | Qué es |
|---|---|
| Administrador del servidor | **«una consola de administración centralizada en Windows Server que permite a los profesionales de TI aprovisionar y administrar servidores locales y remotos basados en Windows desde sus escritorios.»** Desde él se añaden roles y características y se agrupan servidores para administrarlos a la vez |
| Windows Admin Center | **«una herramienta de administración remota para Windows Server que se ejecuta en cualquier lugar (físico, virtual, en el entorno local, en Azure o en un entorno hospedado) sin coste adicional.»** Ofrece **«versiones modernizadas de herramientas tan conocidas como el Administrador del servidor»** |
| RSAT | Las herramientas de administración remota del servidor: **«RSAT permite a los administradores de TI administrar de forma remota roles y características en Windows Server»** desde un equipo cliente |
| PowerShell | El módulo ActiveDirectory y el módulo ADDSDeployment (epígrafes 3 y 4). El lenguaje en sí es el tema 7 |

Dos límites que se preguntan. El Administrador del servidor sólo administra servidores: **«El
Administrador del servidor no se puede usar para administrar equipos o dispositivos que ejecutan un
sistema operativo cliente windows.»** Y las RSAT no van en cualquier Windows: **«No puede instalar
RSAT en equipos que ejecutan ediciones Home o Standard de Windows. Solo puede instalar RSAT en las
ediciones Professional o Enterprise del sistema operativo cliente Windows.»** (el artículo de soporte
que lo dice está escrito para Windows 10 y Windows 7; no se ha leído la página equivalente de
Windows 11). En el propio servidor no se descargan, se añaden como característica: **«Inicie el Asistente para
agregar roles y características en Windows Server 2012 R2 y versiones posteriores. A continuación, en
la página Seleccionar características, expanda Herramientas de administración remota del servidor y
luego seleccione las herramientas que desea instalar.»**

Las herramientas de AD DS que forman parte de RSAT son, según esa misma página: **«Centro de
administración de Active Directory»**, **«Dominios y confianzas de Active Directory»**, **«Sitios y
servicios de Active Directory»**, **«Usuarios y equipos de Active Directory»**, **«Editor ADSI»** y el
**«Módulo de Active Directory para Windows PowerShell»**, más utilidades de línea de órdenes como
`DCDiag.exe`, `RepAdmin.exe`, `NTDSUtil.exe`, `NetDom.exe`, `DSAdd.exe`, `DSQuery.exe` o `NSLookup.exe`.

### Las tareas del administrador

Lo mínimo que conviene llevar visto de administración:

| Tarea | En Linux | En Windows Server |
|---|---|---|
| Usuarios y grupos | Ficheros de sistema y órdenes de alta y baja | Directorio Activo, o cuentas locales |
| Servicios | `systemctl` | La consola de servicios |
| Registro y auditoría | `journalctl` y los ficheros de registro | El visor de eventos |
| Programas instalados | El gestor de paquetes de la distribución | Instaladores y el gestor de paquetes del sistema |
| Tareas programadas | `cron` y temporizadores del sistema | El programador de tareas |

La consola de servicios, el visor de eventos y el programador de tareas son los mismos que en
Windows 11 (tema 6). Lo propio del servidor es la columna de usuarios y grupos: en un dominio, las
cuentas no viven en cada equipo sino en Active Directory, y de eso tratan los epígrafes siguientes.

## 2. Active Directory y el servicio de directorio

### Directorio y servicio de directorio

Las dos definiciones con que abre Microsoft su introducción: **«Un directorio es una estructura
jerárquica que almacena información sobre los objetos de una red. Un servicio de directorio, como
Active Directory Domain Services (AD DS), proporciona los métodos para almacenar datos de directorio y
poner dichos datos a disposición de los usuarios y administradores de la red.»** El directorio es el
almacén; el servicio de directorio, lo que lo guarda, lo replica y lo sirve.

Qué se guarda: **«Estos objetos suelen incluir recursos compartidos como servidores, volúmenes,
impresoras y cuentas de usuario y equipo de red.»** Y para qué: **«La seguridad se integra con AD DS
mediante la autenticación de inicio de sesión y el control de acceso a los objetos del directorio.
Con un único nombre de usuario y contraseña de red, los administradores pueden administrar los datos
de directorio y la organización en toda su red, y los usuarios de red autorizados pueden acceder a
los recursos en cualquier parte de la red.»** Dicho en una línea: el directorio donde una
organización guarda sus usuarios, sus equipos y sus permisos, y contra el que se autentica todo lo
demás.

Microsoft lo describe también como base de datos: **«AD DS es una base de datos distribuida que
almacena y administra información acerca de los recursos de red y datos específicos de las
aplicaciones habilitadas para el uso de directorios.»** Distribuida porque cada controlador de
dominio guarda una copia (epígrafe 3).

### Qué incluye AD DS

Cuatro piezas, con las palabras de Microsoft:

| Pieza | Qué es |
|---|---|
| Esquema | **«Un conjunto de reglas, el esquema, que define las clases de objetos y atributos contenidos en el directorio, las restricciones y los límites en las instancias de estos objetos y el formato de sus nombres.»** |
| Catálogo global | **«Catálogo global que contiene información sobre todos los objetos del directorio. Los usuarios y administradores pueden usar el catálogo para buscar información de directorio independientemente del dominio de directorio que realmente contenga los datos.»** |
| Consulta e índice | **«Un mecanismo de consulta e índice para poder publicar los objetos y sus propiedades, y buscar por usuarios o aplicaciones de red.»** |
| Replicación | **«Un servicio de replicación que distribuye los datos de directorio a través de una red. Todos los controladores de dominio de un dominio participan en la replicación y contienen una copia completa de toda la información de directorio del dominio. Cualquier cambio en los datos del directorio se replica en todos los controladores de dominio del dominio.»** |

### El modelo lógico: bosque, dominio, árbol y unidad organizativa

AD DS ordena los objetos en contenedores, unos dentro de otros: **«El contenedor de nivel superior es
el bosque. Dentro de los bosques hay dominios y dentro de los dominios hay unidades organizativas.
Esto se denomina modelo lógico porque es independiente de los aspectos físicos de la implementación,
como el número de controladores de dominio necesarios dentro de cada dominio y la topología de
red.»**

*Bosque.* **«Un bosque es una colección de uno o varios dominios de Active Directory que comparten
una estructura lógica común, un esquema de directorio (definiciones de clase y atributo), una
configuración de directorio (información de sitio y replicación) y un catálogo global (funcionalidades
de búsqueda en todo el bosque). Los dominios del mismo bosque se vinculan automáticamente con
relaciones de confianza transitivas bidireccionales.»** Lo que comparten todos los dominios de un
bosque, por tanto: esquema, configuración y catálogo global. El bosque más pequeño tiene un solo
dominio, y su primer dominio es el dominio raíz del bosque.

*Dominio.* **«Un dominio es una partición de un bosque de Active Directory. La creación de
particiones de datos permite a las organizaciones replicar datos solo en los casos en los que sea
necesario.»** Funciones que Microsoft le atribuye:

- **«Identidad de usuario en toda la red. En los dominios, las identidades de usuario se pueden crear
  una vez y, a continuación, hacer referencia a ellas en cualquier equipo unido al bosque en el que se
  encuentra el dominio.»**
- Autenticación: **«Los controladores de dominio proporcionan servicios de autenticación para los
  usuarios y proporcionan datos de autorización adicionales, como pertenencias a grupos de usuarios,
  que se pueden usar para controlar el acceso a los recursos de la red.»**
- **«Relaciones de confianza. Los dominios pueden ampliar los servicios de autenticación a los
  usuarios de dominios fuera de su propio bosque mediante confianzas.»**
- Replicación: **«todos los controladores de dominio tienen el mismo nivel en un dominio y se
  administran como una unidad.»**

Cada dominio tiene un nombre DNS (`corp.contoso.com` en los ejemplos de Microsoft) y un nombre
NetBIOS corto: la instalación lo genera solo, y un parámetro permite cambiar **«el nombre de 15
caracteres que se genera automáticamente según el prefijo de nombre DNS o si el nombre excede los 15
caracteres.»**

*Árbol.* Las fuentes leídas no dan una definición literal de árbol, pero el asistente de
instalación distingue los dos modos de añadir un dominio a un bosque existente: como **«Dominio
secundario»**, escribiendo **«el nombre relativo del nuevo dominio secundario (por ejemplo emea)»**
bajo un dominio primario (`emea.corp.contoso.com` cuelga de `corp.contoso.com`), o como **«Dominio de
árbol»**, escribiendo **«el nombre DNS del nuevo dominio (por ejemplo, fabrikam.com)»**. Es decir: un
árbol es un dominio con los secundarios que cuelgan de él compartiendo su espacio de nombres DNS, y un
bosque puede tener varios árboles con nombres distintos (`contoso.com` y `fabrikam.com`) unidos por
las confianzas automáticas del bosque. Esta síntesis es del tema, no cita.

*Unidad organizativa.* **«Las unidades organizativas se pueden usar para formar una jerarquía de
contenedores dentro de un dominio. Las unidades organizativas se usan para agrupar objetos con fines
administrativos, como la aplicación de una directiva de grupo o la delegación de autoridad.»** Una UO
no es un grupo de seguridad: no se le dan permisos sobre carpetas; sirve para ordenar, delegar y
aplicar directivas (epígrafes 4 y 5).

| Contenedor | Qué lo define | Para qué sirve |
|---|---|---|
| Bosque | Esquema, configuración y catálogo global comunes | Reunir todos los dominios, unidos por confianzas automáticas |
| Árbol | Espacio de nombres DNS contiguo | Agrupar dominios con un mismo nombre raíz |
| Dominio | Partición del directorio replicada entre sus controladores | Identidad, autenticación, confianzas, replicación |
| UO | Contenedor dentro de un dominio | Directiva de grupo y delegación |

La tabla es síntesis del tema a partir de las citas anteriores.

### Relaciones de confianza

Dentro de un bosque las confianzas son automáticas, **«transitivas bidireccionales»**: cada dominio
confía en los demás y la confianza se encadena. Fuera del bosque hay que crearlas. Microsoft describe
tres modelos de diseño de bosque, y en dos de ellos la confianza es la herramienta: en el bosque
organizativo, **«Si los usuarios de un bosque organizativo necesitan acceder a los recursos de otros
bosques (o a la inversa), se pueden establecer relaciones de confianza entre un bosque organizativo y
otros bosques.»**; en el de recursos, **«Las confianzas de bosque se establecen para que los usuarios
de otros bosques puedan acceder a los recursos contenidos en el bosque de recursos.»** El tercero, el
de acceso restringido, es justo lo contrario: **«No se puede conceder acceso a los usuarios de otros
bosques a los datos restringidos porque no existe relación de confianza.»** Las confianzas se
administran con la consola **«Dominios y confianzas de Active Directory»**.

### Los sitios: la estructura física

El modelo lógico no dice nada de la red; para eso están los sitios, que se administran con **«Sitios
y servicios de Active Directory»**. Microsoft enumera para qué los usa el sistema: **«el enrutamiento
de la replicación, la afinidad de cliente, la replicación del volumen del sistema (SYSVOL), los
Espacios de nombres del Sistema de archivos distribuido (DFSN) y la ubicación del servicio.»**

- Replicación: **«Dentro de los sitios, la replicación está optimizada para la velocidad, las
  actualizaciones de datos desencadenan la replicación y los datos se envían sin la sobrecarga
  requerida por la compresión de datos. Por el contrario, la replicación entre sitios se comprime
  para minimizar el costo de la transmisión mediante vínculos de red de área extensa (WAN).»**
- Afinidad de cliente: **«Los controladores de dominio usan la información del sitio para informar a
  los clientes de Active Directory sobre los controladores de dominio presentes en el sitio más
  cercano como cliente.»** El sitio del cliente se deduce **«En función de la dirección IP del
  cliente»**, y el cliente busca entonces su controlador en DNS mediante **«el registro de recursos
  del servicio específico del sitio (SRV) (un registro de recursos del Sistema de nombres de dominio
  (DNS) utilizado para buscar controladores de dominio para AD DS)»**.

Para el operador, la consecuencia práctica: un usuario de una delegación inicia sesión contra el
controlador de su sede, no contra el de la central, si los sitios están bien definidos.

### LDAP, Kerberos y los puertos de Active Directory

LDAP es el protocolo con que se lee y se escribe en el directorio: los cmdlets de Active Directory
aceptan **«Lightweight Directory Access Protocol (LDAP) query strings»** como filtro, y las
herramientas de diagnóstico comprueban que **«El controlador de dominio permite la conectividad del
Protocolo ligero de acceso a directorios (LDAP) mediante el enlace a la instancia.»** De ahí que se
diga que Active Directory es la implementación de LDAP de Microsoft: es un servicio de directorio que
habla LDAP, aunque además usa Kerberos, DNS, RPC y SMB.

Kerberos es el protocolo de autenticación del dominio: **«Kerberos es un protocolo de
autenticación que se utiliza para comprobar la identidad de un usuario o un host.»** **«En Windows
Server, el KDC se ejecuta en todos los controladores de dominio y utiliza la base de datos Active
Directory Domain Services del dominio como base de datos de cuentas.»** El usuario obtiene al iniciar
sesión un TGT, **«una credencial que permite al cliente solicitar acceso a los servicios sin mostrar
de nuevo la contraseña del usuario.»**; con él pide al KDC un ticket para cada servicio, y el servicio
lo autentica **«sin contactar con un controlador de dominio para cada conexión.»** Frente al protocolo
anterior, NTLM, Kerberos ofrece autenticación mutua: **«NTLM no permite a los clientes comprobar la
identidad del servidor ni habilita a un servidor para comprobar la identidad de otro.»** Y de ahí el
inicio de sesión único: **«Con la autenticación Kerberos dentro de un dominio o en un bosque, el
usuario o servicio puede tener acceso a los recursos permitidos por los administradores sin varias
solicitudes de credenciales.»**

Los puertos del controlador de dominio, según el artículo de Microsoft sobre cortafuegos para dominios
y confianzas (Windows Server 2008 y posteriores):

| Servicio (como lo nombra Microsoft) | Puerto del servidor |
|---|---|
| LDAP | **389/TCP/UDP** |
| SSL de LDAP | **636/TCP** |
| GC DE LDAP (catálogo global) | **3268/TCP** |
| SSL de GC de LDAP | **3269/TCP** |
| Kerberos | **88/TCP/UDP** |
| Cambio de contraseña de Kerberos | **464/TCP/UDP** |
| DNS | **53/TCP/UDP** |
| SMB | **445/TCP** |
| Asignador de extremos de RPC | **135/TCP** |
| W32Time (hora) | **123/UDP** |
| Servicios web de Active Directory (ADWS) | **9389/TCP** |

El mismo artículo explica cuándo sobran los cifrados: **«si sabe que ningún cliente usa LDAP con
SSL/TLS, no tiene que abrir los puertos 636 y 3269.»** El atajo de memoria: 389 y 636 van juntos,
como 80 y 443: el par sin cifrar y el cifrado. Y 3268 y 3269 son la misma pareja para el catálogo
global.

### Niveles funcionales

**«Los niveles funcionales determinan las funcionalidades disponibles de dominio o bosque de Active
Directory Domain Services (AD DS). También determinan los sistemas operativos Windows Server que se
pueden ejecutar en los controladores de dominio del dominio o del bosque. Sin embargo, los niveles
funcionales no afectan a los sistemas operativos que se pueden ejecutar en las estaciones de trabajo y
los servidores miembro que están unidos al dominio o al bosque.»**

Las reglas: **«Puede establecer un nivel funcional de dominio superior al nivel funcional del bosque.
No se puede establecer un nivel funcional de dominio inferior al nivel funcional del bosque.»**, y
Microsoft recomienda establecerlos **«en el valor más alto que pueda admitir el entorno»**. Los niveles
vigentes:

| Controlador con | Nivel Windows Server 2025 | Nivel Windows Server 2016 | Nivel Windows Server 2012 R2 |
|---|---|---|---|
| Windows Server 2025 | Admitido | Admitido | No admitido |
| Windows Server 2022 | No admitido | Admitido | Admitido |
| Windows Server 2019 | No admitido | Admitido | Admitido |
| Windows Server 2016 | No admitido | Admitido | Admitido |
| Windows Server 2012 R2 | No admitido | No admitido | Admitido |

No hay nivel 2019 ni 2022: **«Windows Server 2019 y Windows Server 2022 usan Windows Server 2016 como
el nivel funcional más reciente.»** El nivel 2025 sólo admite controladores 2025 y es el que permite
las páginas de 32k; en instalación desatendida **«se asigna al valor de `DomainLevel 10` y
`ForestLevel 10`»**. Y un mínimo nuevo: **«Los nuevos bosques de Active Directory o conjuntos de
configuración de AD LDS deben tener un nivel funcional de Windows Server 2016 o posterior.»** Con el
nivel 2016, además, **«Los dominios deben usar DFSR como motor para replicar SYSVOL.»**

## 3. El controlador de dominio

### Qué hace un controlador de dominio

Un controlador de dominio es un servidor Windows Server con el rol AD DS instalado y promovido: guarda
una copia del directorio de su dominio, autentica a usuarios y equipos y replica los cambios con los
demás controladores. Las tres cosas están en las fuentes: **«Los controladores que componen el
dominio se usan para almacenar las cuentas y credenciales de usuario, como contraseñas o
certificados, de forma segura.»**; **«Los controladores de dominio proporcionan servicios de
autenticación para los usuarios»**, porque en cada uno corre el KDC de Kerberos; y la replicación es
multimaestro: **«Active Directory Domain Services (AD DS) admite la replicación multimaestro de datos de directorio, lo que significa que
cualquier controlador de dominio puede aceptar cambios de directorio y replicar los cambios en los
demás controladores de dominio.»** Por eso en un dominio conviene tener al menos dos: si uno cae, el
otro sigue autenticando con su copia completa. Esa recomendación es de oficio; la cita que la sostiene
es la de la replicación.

Además se localiza por DNS: **«DNS es esencial para Active Directory Domain Services (AD DS), que
actúa como mecanismo de ubicación del controlador de dominio para operaciones como autenticación,
actualizaciones y búsquedas. Los controladores de dominio también usan DNS para localizarse entre
sí.»** Un servidor del dominio que no es controlador se llama servidor miembro.

### Los roles de maestro de operaciones (FSMO)

Que todos los controladores escriban no vale para todo: **«algunos cambios, como las modificaciones de
esquema, no es práctico realizarlos en modo multimaestro. Por este motivo, determinados controladores
de dominio, conocidos como maestros de operaciones, hacen que los roles sean responsables de aceptar
las solicitudes de determinados cambios.»** Son cinco: tres por dominio y dos por bosque.

| Rol | Ámbito | Qué hace |
|---|---|---|
| Emulador de PDC | Dominio | **«procesa todas las actualizaciones de contraseñas.»** |
| Maestro RID | Dominio | **«mantiene el grupo de RID global para el dominio y asigna grupos de RID locales a todos los controladores de dominio, para asegurarse de que todas las entidades de seguridad creadas en el dominio tengan un identificador único.»** |
| Maestro de infraestructura | Dominio | **«mantiene una lista de las entidades de seguridad de otros dominios que son miembros de grupos dentro de su dominio.»** |
| Maestro de esquema | Bosque | **«administra los cambios en el esquema.»** |
| Maestro de nomenclatura de dominios | Bosque | **«agrega y quita dominios y otras particiones de directorio (por ejemplo, particiones de aplicación del Sistema de nombres de dominio (DNS)) en el bosque.»** |

Lo que hay que saber de cada uno:

- El emulador de PDC es el árbitro de las contraseñas: **«Si se produce un error en la autenticación
  de inicio de sesión en otro controlador de dominio debido a una contraseña incorrecta, ese
  controlador de dominio reenvía la solicitud de autenticación al emulador de PDC antes de decidir si
  aceptar o rechazar el intento de inicio de sesión.»** Así, un usuario que acaba de cambiar la
  contraseña no queda rechazado porque el cambio aún no haya llegado a su controlador. **«Solo un
  controlador de dominio actúa como emulador de PDC en cada dominio del bosque.»**
- Sin maestro RID accesible, un controlador no puede renovar su reserva de identificadores **«a medida
  que se agotan»**.
- El maestro de infraestructura no debe ir en un catálogo global salvo que todos los controladores lo
  sean o el bosque tenga un solo dominio: **«Si el maestro de infraestructura y el catálogo global
  están en el mismo controlador de dominio, el maestro de infraestructura no funcionará.»**

Quién los tiene: **«Los titulares de roles de maestro de operaciones se asignan automáticamente cuando
se crea el primer controlador de dominio en un determinado dominio.»** Los dos de bosque van al
primer controlador del bosque y los tres de dominio, al primero de cada dominio. Después no se
mueven solos: **«Las asignaciones automáticas de titulares de roles de maestro de operaciones solo se
realizan cuando se crea un nuevo dominio y cuando se degrada un titular de roles actual. Los demás
cambios en los propietarios de roles debe iniciarlos un administrador.»** Microsoft recomienda
repartirlos y designar maestros en espera, **«controladores de dominio a los que puede transferir
los roles de maestro de operaciones en el caso de que los titulares de roles originales fallen.»**

### Catálogo global

El catálogo global es una función que se activa en un controlador: guarda información de todos los
objetos del bosque, no sólo de su dominio, y atiende búsquedas en el puerto 3268. **«En bosques de
varios dominios, los servidores de catálogos globales facilitan las solicitudes de inicio de sesión
de usuario y las búsquedas en todo el bosque.»** En un bosque de un solo dominio la recomendación es
sencilla: **«En un bosque de un solo dominio, configure todos los controladores de dominio como
servidores de catálogo global.»**, porque no cuesta disco ni replicación adicional. En general,
**«En la mayoría de los casos, se recomienda incluir el catálogo global al instalar controladores de
dominio nuevos.»**, con excepciones como el enlace lento con la sede central, y Microsoft recomienda
colocarlo en **«todas las ubicaciones que contengan más de 100 usuarios»**. Para sedes pequeñas con
enlace lento existe la alternativa del **«almacenamiento en caché de pertenencia a grupos
universales»**.

### Controlador de dominio de solo lectura (RODC)

Un RODC guarda una copia del directorio que no se puede modificar; está pensado para sedes donde el
servidor no está bien protegido. Dos reglas suyas:

- No puede tener roles FSMO: **«Debido a la naturaleza de solo lectura de la base de datos de Active
  Directory en un controlador de dominio de solo lectura (RODC), los RODC no pueden actuar como
  titulares de roles de maestro de operaciones.»**
- No guarda contraseñas salvo que se le permita: **«No se replican contraseñas de cuentas en el RODC
  de manera predeterminada y se impide explícitamente la replicación de las contraseñas de las
  cuentas que son críticas para la seguridad (como las que son miembros del grupo Admins. del
  dominio) en el RODC.»** Qué cuentas sí se guardan lo decide la directiva de replicación de
  contraseñas, con los grupos predeterminados de replicación permitida y denegada.

Se puede instalar en dos fases: **«En la primera fase, un miembro del grupo Admins. del dominio crea
una cuenta RODC. En la segunda fase, se adjunta un servidor a la cuenta RODC.»** La segunda la puede
hacer un usuario o grupo delegado, que **«también tendrá derechos administrativos locales en el RODC
una vez completada la instalación.»** Si el RODC es el único servidor de la sede, conviene que sea
también DNS y catálogo global: sin DNS, **«los usuarios de la sucursal no podrán realizar la
resolución de nombres cuando la red de área extensa (WAN) del sitio central esté sin conexión.»**

### SYSVOL

**«SYSVOL es una colección de carpetas del sistema de archivos que existe en cada controlador de
dominio de un dominio. Las carpetas SYSVOL proporcionan una ubicación predeterminada de Active
Directory para los archivos que se deben replicar en todo un dominio, incluidos los objetos de
directiva de grupo (GPO), los scripts de inicio y apagado, y los scripts de inicio y cierre de
sesión.»** Hoy se replica con DFSR: **«Windows Server 2016 es la última versión de Windows Server que
admite el servicio de replicación de archivos (FRS).»**

### Instalar AD DS y promover el controlador

Hay dos pasos: instalar el rol y promover el servidor a controlador de dominio. Antes de empezar, las
credenciales:

- **«Para instalar un nuevo bosque, debe iniciar sesión como Administrador local del equipo.»**
- **«Para instalar un nuevo dominio secundario o un nuevo árbol de dominios, debe haber iniciado
  sesión como miembro del grupo Administradores de empresas.»**
- **«Para instalar un controlador de dominio adicional en un dominio existente, debe ser miembro del
  grupo Admins. del dominio.»**

*Con PowerShell.* Primero el rol con sus herramientas:

```powershell
Install-WindowsFeature -name AD-Domain-Services -IncludeManagementTools
```

Sin el modificador las consolas no se instalan: **«Las herramientas de administración del servidor no
se instalan de forma predeterminada cuando se usa Windows PowerShell.»** Después, uno de los cmdlets
del módulo ADDSDeployment:

| Cmdlet | Para qué |
|---|---|
| `Install-ADDSForest` | **«El cmdlet Install-ADDSForest instala un nuevo bosque.»** |
| `Install-ADDSDomain` | Un dominio secundario o de árbol en un bosque existente |
| `Install-ADDSDomainController` | **«Use Install-ADDSDomainController para instalar un controlador de dominio adicional.»** |
| `Add-ADDSReadOnlyDomainControllerAccount` | Crear previamente la cuenta de un RODC |

```powershell
Install-ADDSForest -DomainName "corp.contoso.com"
```

Dos detalles de ese ejemplo: **«El servidor DNS se instala de forma predeterminada al ejecutar
Install-ADDSForest.»**, y el cmdlet pide la contraseña del modo de restauración de servicios de
directorio (DSRM), que Microsoft no recomienda escribir en claro en un script. El aviso de Microsoft sobre quien
la vea: **«Si saben esto, podrán suplantar el controlador de dominio y elevar su privilegio al nivel
máximo en un bosque de Active Directory.»**
Cada cmdlet tiene uno de prueba que sólo comprueba requisitos, como `Test-ADDSForestInstallation` o
`Test-ADDSDomainControllerInstallation`.

*Con el Administrador del servidor.* **«En el Administrador del servidor, seleccione Administrar y
seleccione Agregar roles y características»**; se elige **«Instalación basada en roles o basada en
características»**, el servidor, el rol **«Active Directory Domain Services»** y, al acabar, **«Promover
este servidor a un controlador de dominio»**, que abre el Asistente para configuración de AD DS. Sus
páginas:

1. Configuración de implementación: **«Agregar un controlador de dominio a un dominio existente»**,
   **«Agregar un nuevo dominio a un bosque existente»** (secundario o de árbol) o **«Agregar un nuevo
   bosque»**.
2. Opciones del controlador de dominio: en un bosque o dominio nuevo, **«seleccione los niveles
   funcionales de dominio y bosque, seleccione Servidor del Sistema de nombres de dominio (DNS),
   especifique la contraseña DSRM»**; en uno existente, DNS, **«Catálogo global (GC) o Controlador de
   dominio de solo lectura (RODC) según sea necesario»**, el sitio y la contraseña DSRM.
3. Opciones de DNS (delegación), opciones de RODC si procede, opciones adicionales (nombre NetBIOS
   del dominio nuevo, o controlador de origen de la replicación).
4. Rutas de acceso de la base de datos, los registros y SYSVOL, con una advertencia: **«No almacene
   la base de datos de Active Directory, los archivos de registro ni la carpeta SYSVOL en un volumen de
   datos con formato sistema de archivos resistente (ReFS).»**
5. Opciones de preparación (credenciales para ejecutar `adprep`), revisión (con **«Ver script»**, que
   exporta lo elegido como script de PowerShell), comprobación de requisitos e instalación. **«El servidor se reiniciará automáticamente para completar la
   instalación de AD DS.»**

La orden de antes ya no se usa: **«El Asistente para instalación de Active Directory Domain Services
(dcpromo.exe) está en desuso a partir de Windows Server 2012.»**

### Diagnóstico: DCDiag

**«`DCDiag.exe` analiza el estado de los controladores de dominio (DC) en un bosque o empresa e
informa de cualquier problema que le ayude a solucionar problemas.»** Está disponible en el
controlador o con las RSAT, y **«debe ejecutarse con derechos administrativos»**. Entre sus pruebas
de conectividad comprueba que **«El controlador de dominio se puede ubicar en DNS.»**, que responde a
ping y que admite conexiones LDAP y RPC. `dcdiag /s:<controlador>` analiza uno concreto y
`dcdiag /test:DNS` se centra en DNS.

## 4. Gestión básica de usuarios

### Las cuentas predeterminadas

Al crear el dominio aparecen unas cuentas que no hay que crear: **«Las cuentas locales predeterminadas
del contenedor Usuarios incluyen: Administrador, Invitado y KRBTGT. La cuenta HelpAssistant se instala
cuando se establece una sesión de Asistencia remota.»** Se recomienda dejarlas donde están, en el
contenedor Usuarios, sin moverlas a otra UO.

| Cuenta | Lo que dicen las fuentes |
|---|---|
| Administrador | **«Esta cuenta no se puede eliminar ni bloquear, pero la cuenta se puede cambiar o deshabilitar.»** Es **«la cuenta más eficaz del dominio»**, y su SID acaba en 500. **«Cambiar el nombre o deshabilitar la cuenta de administrador dificulta que los usuarios malintencionados intenten obtener acceso a la cuenta.»** |
| Invitado | **«La cuenta de invitado es una cuenta local predeterminada que tiene acceso limitado al equipo y está deshabilitada de forma predeterminada. De forma predeterminada, la contraseña de la cuenta de invitado se deja en blanco.»** Microsoft recomienda dejarla deshabilitada |
| KRBTGT | **«La cuenta KRBTGT es una cuenta predeterminada local que actúa como cuenta de servicio para el servicio centro de distribución de claves (KDC). Esta cuenta no se puede eliminar y no se puede cambiar el nombre de la cuenta. La cuenta KRBTGT no se puede habilitar en Active Directory.»** |

Un detalle que se pregunta: en un controlador de dominio ya no hay usuarios locales propios. **«Puede
crear cuentas de usuario locales en el controlador de dominio solo antes de instalar Servicios de
dominio de Active Directory y no después.»**

Dos principios de seguridad que Microsoft aplica a todas las cuentas: **«Se recomienda asignar cada
usuario a una sola cuenta para garantizar la máxima seguridad. No se permite que varios usuarios
compartan una cuenta.»** Y cada cuenta se representa por un identificador que no cambia aunque cambie
el nombre: **«Una entidad de seguridad se representa mediante un identificador de seguridad único
(SID).»**

### Usuarios y equipos de Active Directory y el Centro de administración

La consola clásica es Usuarios y equipos de Active Directory: **«Puede crear, eliminar y administrar
entidades de seguridad, incluidas las cuentas de usuario, en la consola de Usuarios y equipos de
Active Directory. Esta consola está disponible cuando los componentes active Directory Domain Services
(AD DS) y Active Directory Lightweight Directory Services (AD LDS) de las Herramientas de
administración remota del servidor están instalados en un equipo cliente o Windows Server.»** Quién
puede usarla: **«De forma predeterminada, los miembros del grupo Administradores de dominio y
Administradores de empresa pueden administrar cuentas de usuario, grupo y equipo. Los miembros del
grupo Operadores de cuenta pueden crear, modificar y eliminar cuentas de usuario, pero no pueden
administrar grupos o permisos.»** El equipo **«debe estar unido a un dominio»**.

La otra consola es el Centro de administración de Active Directory (ADAC), que se abre
**«desde el menú Herramientas de la consola de Administrador del servidor o ejecutando una sesión de
PowerShell con privilegios elevados y escribiendo dsac.exe.»** Además de administrar cuentas, gestiona
la papelera de reciclaje de Active Directory y las directivas de contraseña detalladas. El nombre de archivo de la consola clásica
(`dsa.msc`) es de uso común, pero no figura en las páginas leídas.

### Crear una cuenta de usuario

En Usuarios y equipos de Active Directory: **«expanda el árbol de dominio y seleccione el contenedor o
la unidad organizativa que desea hospedar la cuenta de usuario.»**; menú Acción, Nuevo, Usuario. La
primera página pide nombre, iniciales y apellidos (opcionales), **«Nombre completo: nombre completo del
usuario (obligatorio)»** y **«Nombre de inicio de sesión de usuario: nombre de cuenta de usuario
(obligatorio)»**. La segunda, la contraseña y cuatro casillas:

- **«El usuario debe cambiar la contraseña en el siguiente inicio de sesión.»**
- **«El usuario no puede cambiar la contraseña.»**
- **«La contraseña nunca expira. Active esta casilla si desea excluir la cuenta de las directivas de
  contraseña.»**
- **«La cuenta está deshabilitada. Active esta casilla si desea crear la cuenta en un estado
  deshabilitado.»**

Lo habitual en un alta es una contraseña temporal con la primera casilla marcada, para que sólo el
usuario conozca la definitiva. Esa práctica es de oficio; la casilla y su efecto, de la fuente.

La ficha de propiedades de la cuenta tiene muchas pestañas; las que usa el operador:

| Pestaña | Para qué |
|---|---|
| General | Nombre, nombre para mostrar, descripción, oficina, teléfono |
| Cuenta | Nombre de inicio de sesión (y el anterior a Windows 2000), **«Horas de inicio de sesión»**, **«Iniciar sesión en»** (equipos permitidos), **«Desbloquear cuenta»**, opciones de contraseña, **«La cuenta está deshabilitada»**, **«Expira la cuenta»** |
| Perfil | **«Ruta de acceso al perfil»**, **«Script de inicio de sesión»**, **«Carpeta principal»** |
| Miembro de | **«permite agregar o quitar la pertenencia a grupos de seguridad.»** |
| Objeto | La opción **«Proteger el objeto contra la eliminación accidental»** |

Microsoft advierte de que algunas pestañas sólo se ven si está activada la opción
**«Características avanzadas»** del menú Ver, sin decir cuáles.

### Restablecer, desbloquear, deshabilitar y eliminar

Son las cuatro operaciones del día a día, todas desde el menú Acción de la consola:

- *Restablecer la contraseña*: **«En el menú Acción , seleccione Restablecer contraseña.»** El
  cuadro pide la nueva contraseña, su confirmación y dos casillas: obligar a cambiarla en el siguiente
  inicio de sesión y desbloquear: **«Si la cuenta está bloqueada porque el usuario escribió demasiadas
  contraseñas incorrectas, active esta casilla para desbloquear la cuenta.»**
- *Desbloquear*: una cuenta se bloquea **«when the number of incorrect password entries exceeds the
  maximum number allowed by the account password policy»** (cmdlet `Unlock-ADAccount`). Bloquear no
  es deshabilitar: lo primero lo hace el sistema por intentos fallidos; lo segundo, el administrador.
- *Deshabilitar*: **«En el menú Acción , seleccione Deshabilitar cuenta.»** Efecto: **«Cuando se
  deshabilita una cuenta, un usuario que ha iniciado sesión permanece iniciado sesión, pero no puede
  realizar nuevos inicios de sesión.»** Se vuelve atrás con Habilitar cuenta.
- *Eliminar*: **«El procedimiento recomendado es deshabilitar las cuentas antes de eliminarlas en
  caso de que la cuenta tenga permisos para los recursos a los que no se puede acceder a través de
  otros métodos.»** Y la eliminación sólo tiene remedio sencillo si se preparó antes: **«Puede
  recuperar cuentas eliminadas mediante la papelera de reciclaje de Active Directory si habilita la
  papelera de reciclaje antes de eliminar la cuenta. Si la papelera de reciclaje no está habilitada,
  debe realizar una restauración autoritativa de AD DS mediante una copia de seguridad de AD DS que
  incluya la cuenta.»**

La papelera de reciclaje de Active Directory merece tres datos: devuelve el objeto entero (**«las
cuentas de usuario restauradas recuperan automáticamente todas las pertenencias a grupos y los
derechos de acceso correspondientes que tenían justo antes de la eliminación»**); **«no está habilitada
de forma predeterminada. El proceso de habilitar la papelera de reciclaje de Active Directory es
irreversible.»**; y exige que **«El nivel funcional del bosque y el dominio debe ser Windows Server 2008
R2 o posterior.»** y ser miembro de Admins. del dominio. Se habilita desde el ADAC (**«Habilitar
Papelera de reciclaje»** en el panel Tareas) o con `Enable-ADOptionalFeature`.

### La gestión desde PowerShell y la línea de órdenes

El módulo ActiveDirectory de PowerShell (su página de referencia está en inglés y se cita así) hace
todo lo anterior por script, que es como se dan de alta cien usuarios a la vez:

| Cmdlet | Qué hace |
|---|---|
| `New-ADUser` | **«Creates an Active Directory user.»** Requisito: **«You must specify the SamAccountName parameter to create a user.»** Si no se indica `-Path`, crea el usuario **«in the default container for user objects in the domain.»** |
| `Get-ADUser` | **«gets a specified user object or performs a search to get multiple user objects.»** Con `-Filter` y `-SearchBase` busca en una UO |
| `Set-ADAccountPassword` | **«sets the password for a user, computer, or service account.»** Con `-Reset` la restablece |
| `Unlock-ADAccount` | **«restores Active Directory Domain Services (AD DS) access for an account that is locked.»** |
| `Disable-ADAccount` y `Enable-ADAccount` | Deshabilitan y habilitan **«an Active Directory user, computer, or service account.»** |
| `Search-ADAccount` | **«retrieves one or more user, computer, or service accounts that meet the criteria specified by the parameters.»** Con `-LockedOut`, las bloqueadas; con `-AccountDisabled`, las deshabilitadas; con `-PasswordExpired`, las de contraseña caducada |
| `Add-ADGroupMember` | **«adds one or more users, groups, service accounts, or computers as new members of an Active Directory group.»** |
| `New-ADGroup` | **«The Name and GroupScope parameters specify the name and scope of the group and are required to create a new group.»** |
| `New-ADOrganizationalUnit` | Crea una UO, que queda protegida contra el borrado accidental: **«Note that accidental protection is implicit.»** |

Un detalle de `New-ADUser` que se pregunta: una cuenta creada sin contraseña nace deshabilitada.
**«No password is specified: No password is set and the account is disabled unless it is requested to
be enabled.»** Y otro: admite el alta masiva con **«the `Import-Csv` cmdlet with the `New-ADUser`
cmdlet»**, leyendo los datos de un fichero CSV y pasándolos por la tubería.

La identidad de una cuenta se puede dar de cuatro formas, según los cmdlets: **«distinguished name
(DN), GUID, security identifier (SID), or Security Account Manager (SAM) account name.»** El nombre
distintivo es la ruta LDAP del objeto, por ejemplo `CN=Patti Fuller,OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM`.

Un ejemplo de alta completa:

```powershell
New-ADUser -Name "Ana Ruiz" -SamAccountName aruiz -Path "OU=Informativos,DC=corp,DC=contoso,DC=com" `
  -AccountPassword (Read-Host -AsSecureString "Contraseña") -ChangePasswordAtLogon $true -Enabled $true
Add-ADGroupMember -Identity "GG-Informativos" -Members aruiz
```

Todos los parámetros usados (`-Name`, `-SamAccountName`, `-Path`, `-AccountPassword`,
`-ChangePasswordAtLogon`, `-Enabled`) figuran en la sintaxis de `New-ADUser`; los nombres de usuario,
UO y grupo son inventados.

Desde la línea de órdenes clásica sigue existiendo `net user`: **«El `net user` comando permite
agregar, modificar o eliminar cuentas de usuario y mostrar información detallada sobre las cuentas de
usuario en un equipo o dominio local.»** El modificador `/domain` **«Realiza la operación en el
controlador de dominio del dominio principal del equipo.»**, y `/active:{yes | no}` **«Habilita o
deshabilita la cuenta de usuario.»** Por ejemplo, `net user aruiz /domain` muestra los datos de la
cuenta del dominio.

### Grupos: tipos y ámbitos

**«Los grupos de seguridad son una manera de recopilar cuentas de usuario, cuentas de equipo y otros
grupos en unidades administrables.»** Hay dos tipos:

- **«Grupos de seguridad: se usa para asignar permisos a los recursos compartidos.»**
- **«Grupos de distribución: se usa para crear listas de distribución de correo electrónico.»** No
  sirven para dar permisos: **«Los grupos de distribución no están habilitados para la seguridad, por
  lo que no se pueden incluir en las DACL.»**

Y tres ámbitos: **«Active Directory define los tres ámbitos de grupo siguientes:»** universal, global y
dominio local, más el de los grupos integrados: **«los grupos predeterminados del contenedor Builtin
tienen un ámbito de grupo de Builtin Local. Este ámbito de grupo y tipo de grupo no se pueden
cambiar.»**

| Ámbito | Miembros posibles | Dónde puede recibir permisos |
|---|---|---|
| Universal | **«Cuentas de cualquier dominio del mismo bosque»**, grupos globales y otros universales de cualquier dominio del bosque | **«En cualquier dominio dentro del mismo bosque o bosques confiables»** |
| Global | **«Cuentas del mismo dominio»** y **«Otros grupos globales del mismo dominio»** | **«En cualquier dominio del mismo bosque, o en dominios o bosques de confianza»** |
| Dominio local | **«Cuentas de cualquier dominio o de cualquier dominio de confianza»**, grupos globales y universales, **«Otros grupos locales de dominio del mismo dominio»** | **«Dentro del mismo dominio»** |

Cómo se leen juntas las dos columnas: el global reúne gente de un solo dominio pero sirve en todo el
bosque; el dominio local reúne gente de cualquier sitio pero sólo sirve en su dominio. De ahí el uso
corriente, que es de oficio: los usuarios van a grupos globales por función (por ejemplo, todo
Informativos), los permisos de una carpeta se dan a un grupo de dominio local (los que pueden
modificar esa carpeta), y el global se mete en el de dominio local. Las conversiones también tienen
reglas: un global **«Se puede convertir al ámbito universal si el grupo no es miembro de ningún otro
grupo global.»**

### Los grupos predeterminados

**«Los grupos predeterminados, como el grupo Administradores de dominio, son grupos de seguridad que
se crean automáticamente al crear un dominio de Active Directory.»** Están en dos contenedores:
**«El contenedor Builtin incluye los grupos que se han definido con el ámbito local del dominio. El
contenedor Usuarios incluye grupos definidos con ámbito Global y grupos definidos con ámbito Local de
dominio.»** Los que más se preguntan:

| Grupo | Qué puede hacer |
|---|---|
| Admins. del dominio | **«Los miembros del grupo de seguridad Administradores de dominio están autorizados para administrar el dominio. De forma predeterminada, el grupo Administradores de dominio es miembro del grupo Administradores en todos los equipos que se unen a un dominio, incluidos los controladores de dominio.»** |
| Administradores de empresas | **«solo existe en el dominio raíz de un bosque»**; **«Los miembros de este grupo están autorizados para realizar cambios en todo el bosque en Active Directory, como agregar dominios secundarios.»** |
| Administradores de esquema | **«pueden modificar el esquema de Active Directory. Este grupo solo existe en el dominio raíz de un bosque de Dominios de Active Directory.»** |
| Operadores de cuentas | **«Los miembros de este grupo pueden crear y modificar la mayoría de los tipos de cuentas, incluidas las cuentas para los usuarios, los grupos locales y los grupos globales.»** No pueden modificar los derechos de usuario ni administrar las cuentas de administrador |
| Operadores de copias de seguridad | **«pueden hacer copias de seguridad y restaurar archivos de un equipo, independientemente de los permisos que protejan dichos archivos.»** |
| Operadores de servidores | **«pueden administrar controladores de dominio. Este grupo solo existe en controladores de dominio.»** Entre otras cosas, **«Creación y eliminación de recursos compartidos de red»** y **«Detener e iniciar los servicios»** |
| Operadores de impresión | **«pueden administrar, crear, compartir y eliminar las impresoras que hay conectadas a los controladores del dominio.»** |
| Usuarios del dominio | **«incluye todas las cuentas de usuario de un dominio. Cuando se crea una cuenta de usuario en un dominio, se agrega a este grupo de forma predeterminada.»** |
| Equipos del dominio | **«todos los equipos y servidores que se unen al dominio, excepto los controladores de dominio.»** |
| Invitados del dominio | **«incluye la cuenta de invitado integrada del dominio.»** |
| Usuarios de escritorio remoto | Concede permiso para conectarse de forma remota a un servidor host de sesión de Escritorio remoto |

Los grupos de operadores de copia, impresión y servidores **«no se puede cambiar de nombre, eliminar
ni quitar»** y nacen vacíos. Microsoft advierte de que varios de ellos son, en la práctica,
administradores: de los operadores de copia de seguridad, **«Dado que los miembros de este grupo
pueden reemplazar archivos en controladores de dominio, se consideran administradores de
servicios.»**; de los de impresión, **«Puesto que los miembros de este grupo pueden cargar y
descargar controladores de dispositivo en todos los controladores del dominio, tenga precaución al
agregar usuarios.»**

### Derechos y permisos

**«Los permisos y los derechos de usuario no son lo mismo.»** La diferencia, con la definición de
Microsoft: **«Un derecho autoriza a un usuario a realizar ciertas acciones en un equipo, como hacer
copias de seguridad de archivos y carpetas, o apagar el equipo. Por el contrario, un permiso de
acceso es una regla asociada a un objeto, normalmente un archivo, una carpeta o una impresora, que
regula qué usuarios pueden acceder al objeto y de qué manera.»**

La regla de oro de la asignación: **«Cuando los administradores asignan permisos para recursos como
recursos compartidos de archivos o impresoras, deben asignar esos permisos a un grupo de seguridad en
lugar de a usuarios individuales.»** Así, dar o quitar acceso a una persona es meterla o sacarla de un
grupo, sin tocar la carpeta: **«Cuando se agrega un usuario a un grupo, dicho usuario recibe todos los
derechos de usuario que el grupo tenga asignados, incluidos todos los permisos asignados al grupo
sobre cualquier recurso compartido.»**

### Unidades organizativas y delegación

La UO sirve para dos cosas: vincular directivas de grupo (epígrafe 5) y delegar. **«El control (sobre
una unidad organizativa y los objetos que contiene) viene determinado por las listas de control de
acceso (ACL) en la unidad organizativa y en los objetos de esta. Para facilitar la administración de
un gran número de objetos, AD DS admite el concepto de delegación de autoridad. Mediante la
delegación, los propietarios pueden transferir un control administrativo total o limitado sobre los
objetos a otros usuarios o grupos.»** Así se puede dejar a un técnico de una sede restablecer las
contraseñas de los usuarios de su UO y nada más.

Para que las directivas se apliquen bien, Microsoft aconseja UO homogéneas: **«Mediante el uso de una
estructura en la que las UNIDADES organizativas contienen objetos homogéneos, como objetos de usuario
o equipo, pero no ambos, puede deshabilitar fácilmente esas secciones de un GPO que no se aplican a
un tipo determinado de objeto.»** Y **«Si es posible, cree unidades organizativas para delegar la
autoridad administrativa y para ayudar a implementar la directiva de grupo.»**

### Unir un equipo al dominio

Desde PowerShell, **«El cmdlet `Add-Computer` agrega el equipo local o los equipos remotos a un
dominio o grupo de trabajo, o los mueve de un dominio a otro. También crea una cuenta de dominio si el
equipo se agrega al dominio sin una cuenta.»**

```powershell
Add-Computer -DomainName Domain01 -Restart
Add-Computer -DomainName Domain02 -OUPath "OU=testOU,DC=domain,DC=Domain,DC=com"
```

El primero **«agrega el equipo local al dominio Domain01 y, a continuación, reinicia el equipo para que
el cambio sea efectivo.»**; el segundo coloca la cuenta del equipo en una UO concreta. Al unirse, la
cuenta del equipo entra en Equipos del dominio, y el grupo Admins. del dominio pasa a ser
administrador del equipo. Para que la unión funcione, el equipo tiene que encontrar un controlador de
dominio por DNS (epígrafe 5): el fallo más común es un equipo que tiene como servidor DNS el del
proveedor de internet y no el del dominio. Ese diagnóstico es de oficio.

## 5. Recursos y servicios asociados

Los servicios que acompañan a Active Directory en un dominio Windows son los que el directorio
necesita para funcionar (DNS), los que reparten la configuración de red (DHCP) y los que ofrecen
recursos a los usuarios (archivos, impresoras) o les aplican configuración (directivas de grupo).
Todos son roles de Windows Server que se instalan desde **«Agregar roles y características»** del
Administrador del servidor o con PowerShell.

### DNS

**«DNS es un protocolo estándar del sector que asigna nombres de dominio a direcciones IP, lo que
permite la resolución de nombres para computadoras y usuarios. En las redes de Windows, DNS es el
servicio de resolución de nombres predeterminado.»** En Windows Server **«DNS es un rol de servidor
que se puede instalar mediante el Administrador del servidor o comandos de PowerShell. Al configurar
un nuevo bosque y dominio de Active Directory, DNS se instala automáticamente con Active
Directory.»**

Por qué no hay dominio sin DNS: el cliente DNS de cada equipo hace dos cosas, **«Detecta
controladores de dominio.»** y **«Convierte los nombres de equipo en direcciones IP.»** El ejemplo de
Microsoft: **«cuando un usuario de red con una cuenta de usuario de Active Directory inicia sesión en
un dominio de Active Directory, el servicio cliente DNS consulta el servidor DNS para buscar un
controlador de dominio para el dominio. Una vez que el servidor DNS responde con la dirección IP del
controlador de dominio, el cliente se pone en contacto con el controlador de dominio para comenzar el
proceso de autenticación.»**

Características del DNS de Windows Server que el examen puede nombrar: **«Integración de Active
Directory: actualizaciones seguras y replicación de datos DNS.»**; **«Actualizaciones dinámicas:
registro automático y actualizaciones de registros DNS de cliente.»**; **«DNSSEC: garantiza la
integridad y la autenticidad de los datos, lo que evita ataques como la intoxicación por caché.»**;
**«Reenvío y reenvío condicional: resuelve de forma eficaz los nombres fuera de la red local mediante
el reenvío de consultas.»** Los tipos de registro y el funcionamiento general de DNS se estudian en
el tema 13.

### DHCP

**«El Protocolo de configuración dinámica de host (DHCP) es un protocolo cliente-servidor que
proporciona automáticamente un host de protocolo de Internet (IP) con su dirección IP y otra
información de configuración relacionada, como la máscara de subred y la puerta de enlace de
predeterminada. En RFC 2131 y RFC 2132, DHCP se define como un estándar del Grupo de trabajo de
ingeniería de Internet (IETF)»**. En Windows Server es **«un rol de servidor de red opcional»**, y
**«Todos los sistemas operativos cliente basados en Windows incluyen el cliente DHCP (habilitado de
forma predeterminada) como parte de TCP/IP.»**

Lo que guarda el servidor en su base de datos:

- **«Direcciones IP válidas, mantenidas en un grupo para la asignación a clientes, así como direcciones
  excluidas.»**
- **«Direcciones IP reservadas asociadas a determinados clientes DHCP. Esto permite una asignación
  coherente de una única dirección IP a un único cliente DHCP.»** Es lo que se usa para que una
  impresora reciba siempre la misma dirección.
- **«La duración de la concesión, o el período de tiempo durante el que se puede usar la dirección IP
  antes de que se requiera una renovación de la concesión.»**
- Las opciones: **«Algunos ejemplos de opciones DHCP son Enrutador (puerta de enlace predeterminada),
  Servidores DNS y Nombre de dominio DNS.»** En un dominio, la opción de servidores DNS debe apuntar a
  los controladores de dominio que hacen de DNS.

Dos funciones ligadas a Active Directory: la autorización, que **«permite autorizar servidores DHCP en
Active Directory, lo que impide que los servidores no autorizados proporcionen direcciones IP a los
clientes.»**, y la integración con DNS, por la que **«El DNS dinámico actualiza automáticamente los
registros DNS cuando se asignan o renuevan concesiones DHCP»**. Además, **«Conmutación por error dhcp.
Esta característica permite que dos servidores DHCP compartan un único ámbito, lo que proporciona
redundancia y equilibrio de carga.»**, y el agente de retransmisión evita tener un servidor en cada
subred.

### Carpetas compartidas: SMB y permisos NTFS

Las carpetas compartidas de Windows usan SMB: **«El protocolo SMB es un protocolo de uso compartido de
archivos de red. SMB permite leer y escribir en archivos a través de la red sobre TCP/IP u otros
protocolos.»** El servidor SMB **«es el componente que comparte recursos (archivos, impresoras,
canalizaciones con nombre) y responde a las solicitudes de los clientes SMB.»**; el cliente actúa
**«Cuando asigna una unidad de red o accede a una ruta de acceso UNC como `\\server\share`»**. El
dialecto más alto, **«SMB 3.1.1»**, lo admiten Windows 10 1607 y posteriores y Windows Server 2016 y
posteriores; el cliente y el
servidor **«negocian para usar la versión de dialecto más alta que ambos admiten.»** El puerto es
445/TCP (epígrafe 2).

Una carpeta compartida tiene dos capas de control: los permisos del recurso compartido y los permisos
NTFS de la carpeta y sus archivos. Las fuentes leídas describen cada capa por separado, pero no dan
la regla de cómo se combinan, y el tema no la afirma.

- *Permisos del recurso compartido.* `New-SmbShare` **«exposes a file system folder to remote
  clients as a Server Message Block (SMB) share.»** Sus parámetros de acceso son `-FullAccess`
  (**«full permission»**), `-ChangeAccess` (**«modify permission»**), `-ReadAccess` (**«read
  permission»**) y `-NoAccess` (cuentas a las que **«are denied access»**). Con
  `-FolderEnumerationMode AccessBased`, la enumeración basada en el acceso: **«SMB doesn't display the
  files and folders for a share to a user unless that user has rights to access the files and
  folders.»**, que **«By default»** está desactivada.
- *Permisos NTFS.* **«NTFS permite asignar permisos detallados a archivos y carpetas mediante listas
  de control de acceso (ACL). Puede especificar qué usuarios y grupos tienen acceso, definir el tipo de
  acceso, como lectura, escritura o modificación»**. Desde la línea de órdenes se ven y cambian con
  `icacls`, que **«Muestra o modifica listas de control de acceso discrecional (DACL) en archivos
  especificados»** y **«reemplaza al comando cacls»**.

Los permisos básicos de `icacls`:

| Letra | Permiso |
|---|---|
| `N` | **«Sin acceso»** |
| `F` | **«Acceso completo»** |
| `M` | **«Modificar acceso»** |
| `RX` | **«Acceso de lectura y ejecución»** |
| `R` | **«Acceso de solo lectura»** |
| `W` | **«Acceso solo de escritura»** |
| `D` | **«Eliminar acceso»** |

Y el orden en que se colocan las entradas, que explica por qué una denegación explícita pesa más que
una concesión heredada: **«Explicit denials»**, **«Explicit grants»**, **«Inherited denials»**,
**«Inherited grants»**. `/grant` concede, `/deny` **«Deniega explícitamente los derechos de acceso de
usuario especificados.»**, `/t` actúa **«en todos los archivos especificados del directorio actual y
sus subdirectorios»** y `/inheritancelevel:d` **«Desactiva la herencia y copia los ACEs»**.

```powershell
New-SmbShare -Name "Informativos" -Path "D:\Datos\Informativos" -ChangeAccess "Contoso\Informativos-Modificar"
icacls D:\Datos\Informativos /grant "Contoso\Informativos-Modificar:(OI)(CI)M"
```

El ejemplo comparte una carpeta dando permiso de cambio a un grupo de dominio local y le da el
permiso NTFS de modificar, heredable a subcarpetas y archivos: `(OI)` es **«Objeto heredar. Los
objetos de este contenedor heredan esta ACE.»** y `(CI)` es **«Contenedor heredar. Los contenedores
de este contenedor primario heredan esta ACE.»** Los nombres son inventados; los parámetros, los de
las páginas citadas.

Quién puede crear recursos compartidos en un controlador de dominio sin ser administrador: los
Operadores de servidores (epígrafe 4).

### Espacios de nombres DFS

**«Espacios de nombres DFS (Sistema de archivos distribuido) es un servicio de rol de Windows Server
que permite agrupar carpetas compartidas ubicadas en distintos servidores en uno o varios espacios de
nombres estructurados de forma lógica.»** El usuario ve una sola ruta, como `\\Contoso\Public`, y el
sistema lo redirige al servidor real: **«Cuando los usuarios examinan una carpeta con destinos de
carpeta en el espacio de nombres, el equipo cliente recibe una referencia que lo redirige de forma
transparente a uno de los destinos de carpeta.»** Un espacio de nombres que empieza por el nombre del
dominio es **«un espacio de nombres basado en dominio porque comienza con un nombre de dominio y sus
metadatos se almacenan en Active Directory Domain Services (AD DS).»** Si hay varios destinos, se
elige el del sitio del usuario: **«DFSN usa la información del sitio para dirigir a un cliente al
servidor en el que se hospedan los datos solicitados dentro del sitio.»** **«Espacios de nombres DFS y
Replicación DFS forman parte del rol Servicios de archivos y almacenamiento.»**

### Impresoras

Las impresoras compartidas son objetos del directorio como los demás (**«recursos compartidos como
servidores, volúmenes, impresoras y cuentas de usuario y equipo de red»**). Publicadas en AD DS se
encuentran por ubicación: **«Los servicios de impresión usan el atributo de ubicación almacenado en AD
DS para permitir que los usuarios busquen impresoras por ubicación sin conocer su ubicación
precisa.»** Los permisos se dan a grupos, como en las carpetas; el ejemplo de Microsoft: **«si desea
que todos los usuarios de dominio tengan acceso a una impresora, puede asignar permisos para la
impresora a este grupo.»** (Usuarios del dominio). La gestión puede delegarse en Operadores de
impresión, con la cautela ya dicha sobre los controladores de dispositivo. El rol de servidor de
impresión y su consola no se han leído en fuente y no se detallan.

### Directivas de grupo

Las directivas de grupo se estudian en el tema 6 (qué son, orden de aplicación, herencia, `gpupdate`
y `gpresult`). Lo que añade el servidor es el ámbito de dominio: **«Puede vincular GPO a varios
niveles dentro de la jerarquía de AD, como sitios, dominios y unidades organizativas (UO), que definen
su ámbito de aplicación.»** Cada GPO tiene dos partes: **«El contenedor de directivas de grupo se
almacena en la partición de dominio de Active Directory, mientras que la plantilla de directiva de
grupo se encuentra en la carpeta SYSVOL de cada controlador de dominio (DC).»** Se editan con **«el
Editor de objetos de directiva de grupo dentro de un complemento MMC relacionado con AD para la
configuración de todo el dominio.»**

Tres datos que conectan con este tema:

- Las directivas de contraseña son de dominio: **«También puede aplicar algunas opciones de directiva
  de grupo en el nivel de dominio, especialmente las directivas de contraseña.»**
- Gana lo más cercano: **«El contenedor de AD más cercano al equipo o el usuario invalida la directiva
  de grupo establecida en un contenedor de AD de nivel superior.»**
- Los controladores van más rápido que los clientes: **«De forma predeterminada, se produce una
  actualización cada 90 minutos. El sistema puede agregar un tiempo aleatorio de hasta 30 minutos al
  intervalo de actualización.»**, pero **«Los controladores de dominio comprueban los cambios en las
  directivas de equipo cada cinco minutos.»**

### Windows LAPS

Un problema clásico del dominio es que todos los equipos tengan la misma contraseña de administrador
local. **«Las cuentas de administrador local suelen compartir la misma contraseña en muchos
dispositivos, que los actores malintencionados pueden aprovechar para moverse lateralmente por tu
entorno.»** La solución integrada: **«La solución de contraseñas de administrador local de Windows
(Windows LAPS) es una característica de Windows que administra y realiza automáticamente copias de
seguridad de la contraseña de una cuenta de administrador local en los dispositivos unidos a
Microsoft Entra o unidos a Active Directory de Windows Server.»** También sirve para **«la contraseña
de la cuenta de Directory Services Restore Mode (DSRM) en tus controladores de dominio»**. Está en
Windows 11 23H2 y posteriores y en Windows Server 2025, y en versiones anteriores de Windows 11, en
Windows 10 y en Windows Server 2019 y 2022 que recibieron la actualización del 11 de abril de 2023 o
posteriores (Windows 10 sólo mientras siga recibiendo actualizaciones, porque su soporte terminó el 14
de octubre de 2025).

### Caso práctico completo

Una petición típica, resuelta con lo que da el tema. Una redactora se incorpora a la sede de Sevilla;
debe poder entrar en su equipo, ver la carpeta compartida de su área y no tocar otras.

1. *Alta.* En Usuarios y equipos de Active Directory, en la UO de los usuarios de esa sede, Nuevo,
   Usuario: nombre completo y nombre de inicio de sesión (obligatorios), contraseña temporal y
   **«El usuario debe cambiar la contraseña en el siguiente inicio de sesión.»** O, por script,
   `New-ADUser` con `-SamAccountName`, `-Path`, `-AccountPassword`, `-ChangePasswordAtLogon $true` y
   `-Enabled $true` (sin contraseña nacería deshabilitada).
2. *Acceso.* No se toca la carpeta: se la mete en el grupo global de su área (pestaña Miembro de, o
   `Add-ADGroupMember`), que ya es miembro del grupo de dominio local con permiso sobre la carpeta.
3. *Equipo.* Si el equipo es nuevo, se une al dominio con `Add-Computer -DomainName … -OUPath …`
   (o desde la configuración del sistema) y se reinicia. Recibirá las directivas de su UO al
   arrancar.
4. *Al día siguiente no puede entrar.* Si la cuenta está bloqueada por intentos fallidos:
   `Search-ADAccount -LockedOut` para confirmarlo y `Unlock-ADAccount`, o Restablecer contraseña con
   la casilla de desbloqueo. Si el problema es que el equipo no encuentra el dominio: comprobar con
   `ipconfig` que su servidor DNS es el del dominio (la opción de DHCP), y en el servidor,
   `dcdiag /test:DNS`.
5. *Baja.* Cuando deje la empresa: deshabilitar primero, eliminar después, y sólo con la papelera
   de reciclaje habilitada se podrá recuperar la cuenta con sus grupos si se borró por error.

El orden y la división de tareas del caso son de oficio; cada paso remite a una cita de los epígrafes
anteriores.

## Lo que este tema no da, y dónde está

- La organización real de los sistemas de la RTVA y de CSRTV (número de dominios, sedes, servidores,
  versión de Windows Server instalada, nombres de grupos o UO): no consta en ningún documento
  publicado.
- Las diferencias de licencia entre las ediciones Standard y Datacenter en número de máquinas
  virtuales: la tabla de ediciones leída no lo da de forma extraíble; no se afirma.
- La regla de combinación de los permisos de recurso compartido con los NTFS, y el detalle de los
  permisos especiales y de herencia de NTFS: no se han leído en fuente.
- El rol de servidor de impresión y la consola Administración de impresión; las directivas de
  contraseña y de bloqueo de cuentas con sus valores; las directivas de contraseña específicas: no se
  han leído en fuente.
- La identidad híbrida (Microsoft Entra ID y su sincronización con Active Directory): fuera de lo que
  pide el enunciado; la nube y el despliegue híbrido aparecen en el tema 10, y Microsoft 365 en el
  tema 11.
- La definición literal de árbol de dominios: no aparece en las páginas leídas; el tema la deduce del
  asistente de instalación y lo dice.
- Las directivas de grupo en detalle: tema 6. PowerShell como lenguaje: tema 7. DNS, DHCP y
  direccionamiento en general: tema 13. Seguridad en redes, certificados y acceso remoto: tema 14.
  Escritorio remoto y virtualización: tema 10. Copias de seguridad: tema 3.

## Trazabilidad

Todas las páginas se leyeron el 05-10-2026 en Microsoft Learn (learn.microsoft.com, en español salvo
las de referencia del módulo ActiveDirectory y de `New-SmbShare`, que se sirven en inglés). La
traducción automática de Microsoft trae erratas («Admins. del dominio» junto a «Administradores de
dominio» para el mismo grupo, «Replication» y «Authentication» sin traducir en el modelo lógico, «la
puerta de enlace de predeterminada»); se citan tal cual.

| Fuente | Qué sostiene |
|---|---|
| «Información de versión de Windows Server» (windows-server/get-started/windows-server-release-info) | LTSC y canal anual, Windows Server 2025 versión actual, fechas de soporte, ciclo de vida fijo |
| «Windows Server 2025» en el ciclo de vida de Microsoft (lifecycle/products/windows-server-2025) | Ediciones |
| «Comparación de ediciones de Windows Server» | Clústeres de conmutación por error en las tres ediciones |
| «Novedades de Windows Server 2025» | Hotpatch (versión preliminar), ESE y páginas de 32k, nivel funcional 10, mínimo de nivel 2016, firma LDAP por defecto, TLS 1.3 |
| «¿Qué es la opción de instalación Server Core en Windows Server?» | Server Core y Experiencia de escritorio |
| «Administrador de servidores»; «Introducción a Windows Admin Center» | Herramientas de administración |
| Soporte técnico de Microsoft, «Herramientas de administración remota del servidor (RSAT) para Windows» (KB 2693643) | RSAT: ediciones, instalación en el servidor, lista de herramientas de AD DS |
| «Introducción a Active Directory Domain Services» (actualizada el 16-08-2025) | Directorio, servicio de directorio, objetos, seguridad, esquema, catálogo global, consulta, replicación |
| «Descripción del modelo lógico de Active Directory» (actualizada el 12-05-2025) | Bosque, dominio, UO, delegación, base de datos distribuida |
| «Modelos de diseño de bosque» | Confianzas entre bosques |
| «Funciones de sitio» | Sitios, replicación, afinidad de cliente, registros SRV, SYSVOL, DFSN, ubicación de impresoras |
| «Introducción a la autenticación Kerberos en Windows Server» | Kerberos, KDC, TGT, inicio de sesión único, autenticación mutua |
| Soporte técnico de Microsoft, «Cómo configurar un firewall para dominios y confianzas de Active Directory» (KB 179442) | Puertos |
| «Niveles funcionales de Servicios de dominio de Active Directory en Windows Server» | Niveles funcionales y matriz de compatibilidad, DFSR para SYSVOL, FRS |
| «Planear la ubicación del rol de maestro de operaciones» | Replicación multimaestro, roles FSMO, asignación, RODC sin roles |
| «Planear la ubicación del servidor de catálogo global» | Catálogo global, bosque de un solo dominio, ubicaciones de más de 100 usuarios, caché de grupos universales |
| «Instalación de Active Directory Domain Services» | Credenciales, cmdlets ADDSDeployment, DNS por defecto, DSRM, asistente, ReFS, dcpromo en desuso, RODC por fases y en sucursal (DNS y catálogo global) |
| «DCDiag» (referencia de órdenes de Windows) | DCDiag |
| «Cuentas de Active Directory» | Cuentas predeterminadas, SID, cuentas locales en el controlador, derecho y permiso |
| «Administrar cuentas de usuario en usuarios y equipos de Active Directory» | Consola, alta, grupos, restablecer, deshabilitar, eliminar, pestañas |
| «Habilitación y uso de la Papelera de reciclaje de Active Directory» | Papelera, requisitos, `dsac.exe` |
| «Centro de administración de Active Directory» | Papelera y directivas de contraseña detalladas en el ADAC |
| Módulo ActiveDirectory: `New-ADUser`, `Get-ADUser`, `Set-ADAccountPassword`, `Unlock-ADAccount`, `Disable-ADAccount`, `Enable-ADAccount`, `Search-ADAccount`, `Add-ADGroupMember`, `New-ADGroup`, `New-ADOrganizationalUnit` | Gestión por PowerShell |
| «net user» (referencia de órdenes de Windows) | `net user` |
| «Grupos de seguridad de Active Directory» | Tipos y ámbitos de grupo, Builtin Local, grupos predeterminados, permisos a grupos |
| `Add-Computer` (Microsoft.PowerShell.Management, Windows PowerShell 5.1) | Unión al dominio |
| «¿Qué es el sistema de nombres de dominio (DNS)?» | DNS |
| «¿Qué es el servidor del Protocolo de configuración dinámica de host (DHCP) en Windows Server?» | DHCP |
| «¿Qué es el uso compartido de archivos SMB para Windows y Windows Server?»; `New-SmbShare` | SMB, UNC, dialectos, permisos del recurso compartido, enumeración basada en el acceso |
| «Introducción a NTFS»; «icacls» (referencia de órdenes de Windows) | ACL de NTFS, `icacls` |
| «Introducción a los Espacios de nombres de DFS» | DFSN |
| «Introducción a la directiva de grupo para Windows Server»; «Procesamiento de directivas de grupo» (las mismas del tema 6) | GPO en el dominio, directivas de contraseña, precedencia, intervalos, UO homogéneas y para delegar |
| «¿Qué es Windows LAPS?» | LAPS |

Oficio sin fuente detrás, y así se declara: la recomendación de tener al menos dos controladores de
dominio; la síntesis de qué es un árbol y la tabla de contenedores; la lectura de los ámbitos de grupo
como «global para la gente, dominio local para el permiso» y el ejemplo que la ilustra; la contraseña
temporal en el alta; que la opción DHCP de servidores DNS apunte a los controladores que hacen de
DNS y el uso de la reserva para impresoras; el diagnóstico del equipo que no encuentra el dominio por tener otro servidor
DNS; los nombres de usuarios, grupos, rutas y
dominios de los ejemplos; el caso práctico como secuencia; la tabla de tareas del administrador del
epígrafe 1; la definición en una línea del directorio («el directorio donde una organización guarda
sus usuarios, sus equipos y sus permisos, y contra el que se autentica todo lo demás»); y el atajo de
memoria de los puertos 389 y 636.
