# Tema 7 del específico de Operador/a Informático · Automatización y administración mediante PowerShell

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 7 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Documentación oficial de PowerShell en Microsoft Learn, en castellano: artículos conceptuales `about_*`, ayuda de cada cmdlet, el libro introductorio *PowerShell 101* y las páginas de ciclo de vida, instalación y diferencias entre versiones |
| Redacción que se estudia | PowerShell 7.6 (versión de soporte a largo plazo) y 7.5 (estable), y Windows PowerShell 5.1, integrado en Windows; documentación en línea el 05-10-2026 y leída ese día |
| Extensión | 15.000 palabras aproximadamente (con los ejemplos de código) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); la plataforma de
desarrollo de Microsoft .NET y su entorno de ejecución común (CLR, *Common Language Runtime*);
versión de soporte a largo plazo (LTS, *long-term support*); Windows Management Framework (WMF),
paquete con el que Microsoft distribuía Windows PowerShell; entorno de scripting integrado de
Windows PowerShell (ISE, *Integrated Scripting Environment*); Visual Studio Code (VS Code), editor de
Microsoft; instalador de Windows (MSI, *Microsoft Installer*) y su formato de paquete moderno (MSIX);
Control de cuentas de usuario (UAC, *User Account Control*); convención de nomenclatura universal
(UNC, *universal naming convention*) para rutas de red; valores separados por comas (CSV,
*comma-separated values*); notación de objetos de JavaScript (JSON, *JavaScript Object Notation*);
lenguaje de marcas extensible (XML, *eXtensible Markup Language*); código estándar estadounidense
para el intercambio de información (ASCII, *American Standard Code for Information Interchange*);
formato de transformación Unicode de 8 bits (UTF-8, *Unicode Transformation Format*) y marca de
orden de bytes (BOM, *byte order mark*); expresión regular (en inglés *regular expression*, abreviado
*regex*); el intérprete de órdenes clásico de Windows, `cmd.exe` (CMD); el formato de fichero
comprimido ZIP; el lenguaje de consulta estructurado (SQL, *Structured Query Language*) y el servicio
en la nube Amazon Web Services (AWS), que aparecen en la lista de módulos de Microsoft.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 7): «Automatización y
> administración mediante PowerShell: entorno PowerShell, ayuda, variables, operadores, arrays,
> strings, metacaracteres, tuberías, direccionamiento, estructuras de control y gestión de ficheros.»

Qué se puede preguntar: qué es PowerShell y en qué se distingue de los shells que trabajan con texto;
qué diferencia hay entre Windows PowerShell 5.1 y PowerShell 7, cómo se llama el ejecutable de cada
uno y cuál es la versión LTS vigente; cómo se forma el nombre de un cmdlet; qué es un alias, un
proveedor, un perfil y un script `.ps1`; qué directivas de ejecución hay, cuál rige por defecto en un
cliente Windows y en qué orden se aplican sus ámbitos; para qué sirven `Get-Help`, `Update-Help`,
`Get-Command` y `Get-Member`; cómo se nombra, se tipa y se borra una variable, y qué son `$_`, `$?`,
`$null`, `$Error` o `$Env:`; qué operadores de comparación hay, por qué no se usan `>` ni `<` para
comparar, qué hace `-like` frente a `-match` y qué devuelven con una colección a la izquierda; cómo
se crea una matriz y una tabla hash, cómo se indexan y qué devuelve un índice negativo; qué
diferencia una cadena entre comillas dobles de una entre comillas simples; qué es una cadena *here*;
qué significan `*`, `?`, `[a-l]` y el acento grave; qué es una canalización y cómo se enlazan sus
objetos (`ByValue` y `ByPropertyName`); qué número tiene cada flujo de salida y qué hacen `>`, `>>`,
`2>&1` y `*>`; cómo se escriben `if`, `switch`, `for`, `foreach`, `while`, `do`, `break`, `continue`
y `try/catch`; y qué cmdlets listan, crean, copian, mueven, renombran, borran, leen y escriben
ficheros. En la aplicación práctica: leer una línea de órdenes y decir qué hace, encontrar el error de
una comparación o de una redirección, o escoger el cmdlet y el parámetro que resuelven una tarea de
administración del puesto.

<!-- indice -->

## Índice

- [1. El entorno PowerShell](#1-el-entorno-powershell)
  - [Qué es PowerShell](#qué-es-powershell)
  - [Windows PowerShell 5.1 y PowerShell 7](#windows-powershell-51-y-powershell-7)
  - [Instalación de PowerShell 7 en Windows](#instalación-de-powershell-7-en-windows)
  - [Dónde se escribe: consola, editores y elevación](#dónde-se-escribe-consola-editores-y-elevación)
  - [Los comandos: cmdlets, funciones, alias y scripts](#los-comandos-cmdlets-funciones-alias-y-scripts)
  - [Proveedores y unidades](#proveedores-y-unidades)
  - [El perfil](#el-perfil)
  - [La directiva de ejecución](#la-directiva-de-ejecución)
- [2. La ayuda](#2-la-ayuda)
  - [Get-Help](#get-help)
  - [Buscar comandos con la ayuda](#buscar-comandos-con-la-ayuda)
  - [Los artículos about](#los-artículos-about)
  - [Actualizar la ayuda](#actualizar-la-ayuda)
  - [Get-Command](#get-command)
  - [Get-Member](#get-member)
- [3. Variables](#3-variables)
  - [Qué es una variable](#qué-es-una-variable)
  - [Crear, cambiar y borrar](#crear-cambiar-y-borrar)
  - [Tipos](#tipos)
  - [Variables entre comillas](#variables-entre-comillas)
  - [Ámbito](#ámbito)
  - [Variables automáticas que hay que conocer](#variables-automáticas-que-hay-que-conocer)
  - [Variables de entorno](#variables-de-entorno)
- [4. Operadores](#4-operadores)
  - [Aritméticos](#aritméticos)
  - [De asignación](#de-asignación)
  - [De comparación](#de-comparación)
  - [Lógicos](#lógicos)
  - [De división y combinación de cadenas](#de-división-y-combinación-de-cadenas)
  - [De tipo](#de-tipo)
  - [Especiales](#especiales)
- [5. Arrays (matrices) y tablas hash](#5-arrays-matrices-y-tablas-hash)
  - [Crear una matriz](#crear-una-matriz)
  - [Leer elementos](#leer-elementos)
  - [Contar, añadir, quitar](#contar-añadir-quitar)
  - [Recorrer y filtrar](#recorrer-y-filtrar)
  - [Tablas hash](#tablas-hash)
- [6. Strings (cadenas)](#6-strings-cadenas)
  - [Comillas dobles y comillas simples](#comillas-dobles-y-comillas-simples)
  - [Comillas dentro de una cadena y escape](#comillas-dentro-de-una-cadena-y-escape)
  - [Cadenas here](#cadenas-here)
  - [Operaciones con cadenas](#operaciones-con-cadenas)
- [7. Metacaracteres](#7-metacaracteres)
  - [Comodines](#comodines)
  - [El acento grave y las secuencias de escape](#el-acento-grave-y-las-secuencias-de-escape)
  - [Expresiones regulares](#expresiones-regulares)
- [8. Tuberías](#8-tuberías)
  - [Qué es una canalización](#qué-es-una-canalización)
  - [Uno a uno](#uno-a-uno)
  - [Cómo recibe el comando el objeto: ByValue y ByPropertyName](#cómo-recibe-el-comando-el-objeto-byvalue-y-bypropertyname)
  - [Los cmdlets de la tubería](#los-cmdlets-de-la-tubería)
  - [Buenas prácticas de la documentación](#buenas-prácticas-de-la-documentación)
- [9. Direccionamiento (redirección de la salida)](#9-direccionamiento-redirección-de-la-salida)
  - [Los flujos de salida](#los-flujos-de-salida)
  - [Los operadores](#los-operadores)
  - [Out-File y Tee-Object](#out-file-y-tee-object)
- [10. Estructuras de control](#10-estructuras-de-control)
  - [if, elseif, else](#if-elseif-else)
  - [switch](#switch)
  - [for](#for)
  - [foreach](#foreach)
  - [while](#while)
  - [do-while y do-until](#do-while-y-do-until)
  - [break y continue](#break-y-continue)
  - [try, catch, finally](#try-catch-finally)
- [11. Gestión de ficheros](#11-gestión-de-ficheros)
  - [Los cmdlets de elementos](#los-cmdlets-de-elementos)
  - [Listar: Get-ChildItem](#listar-get-childitem)
  - [Crear, copiar, mover, renombrar](#crear-copiar-mover-renombrar)
  - [Borrar](#borrar)
  - [Leer y escribir contenido](#leer-y-escribir-contenido)
  - [Buscar dentro de ficheros](#buscar-dentro-de-ficheros)
  - [Unidades y rutas](#unidades-y-rutas)
  - [Aplicación práctica: un script de mantenimiento](#aplicación-práctica-un-script-de-mantenimiento)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. El entorno PowerShell

### Qué es PowerShell

La documentación oficial lo define así: **«PowerShell es una solución de automatización de tareas
multiplataforma formada por un shell de línea de comandos, un lenguaje de scripting y un marco de
administración de configuración. PowerShell se ejecuta en Windows, Linux y macOS.»** Son, por tanto,
tres cosas a la vez:

| Pieza | Qué es | Lo que dice Microsoft |
|---|---|---|
| Intérprete de línea de comandos | El shell en el que se escriben órdenes una a una | **«PowerShell es un shell de comandos moderno que incluye las mejores características de otros shells populares»** |
| Lenguaje de scripting | Las mismas órdenes guardadas en un fichero y ejecutadas como programa | **«Como lenguaje de scripting, PowerShell se usa normalmente para automatizar la administración de sistemas»** |
| Administración de configuración | Desired State Configuration (DSC), configuración declarativa | **«Desired State Configuration (DSC) de PowerShell es un marco de administración en PowerShell que permite administrar la infraestructura empresarial con configuración como código»** |

Lo que lo separa del símbolo del sistema (`cmd.exe`) y de los shells de Unix es que no maneja texto
sino objetos: **«A diferencia de la mayoría de los shells que solo aceptan y devuelven texto,
PowerShell acepta y devuelve objetos .NET.»** Y más adelante: **«PowerShell se basa en .NET Common
Language Runtime (CLR). Todas las entradas y salidas son objetos de .NET. No es necesario analizar la
salida de texto para extraer información de la salida.»** Cuando `Get-Process` devuelve los procesos,
cada uno es un objeto con propiedades (nombre, identificador, memoria) y métodos (`Kill()`); el
comando siguiente de la canalización puede leer esas propiedades sin recortar columnas de texto.
Esta idea explica casi todo lo que viene después: las tuberías pasan objetos, `Get-Member` enseña
qué hay dentro de un objeto, y la salida a fichero es una representación en texto de esos objetos.

Las características del shell que enumera la documentación: **«Un historial de línea de comandos
sólido.»**, **«Finalización con tabulación y predicción de comandos»**, **«Admite alias de comandos
y parámetros.»**, una **«Canalización para encadenar comandos.»** y un **«Sistema de ayuda en la
consola, similar a las páginas man de UNIX.»** Las del lenguaje: es **«Extensible mediante funciones,
clases, scriptsy módulos»** [sic] y tiene **«Compatibilidad integrada con formatos de datos comunes,
como CSV, JSONy XML»** [sic].

Para la administración, PowerShell se amplía con módulos: la documentación cita módulos de Microsoft
para Azure, Windows, Exchange y SQL, y de terceros para AWS, VMware y Oracle Cloud.

### Windows PowerShell 5.1 y PowerShell 7

En un equipo Windows conviven dos productos con nombre casi igual, y el examen puede jugar con ello.

*Windows PowerShell 5.1* es el que trae el sistema. **«Windows PowerShell 5.1 se basa en .NET
Framework v4.5.»** Microsoft lo fecha en **«Agosto de 2016»**, **«Publicado en Windows 10
Actualización de aniversario y Windows Server 2016, WMF 5.1»**, y advierte que **«Microsoft ya no
admite Windows versiones de PowerShell inferiores a la 5.1»** [sic]. Es un componente del sistema:
**«Windows PowerShell es un componente del sistema operativo Windows y está sujeto al ciclo de vida
de soporte técnico de Windows.»** El libro *PowerShell 101* añade que **«Windows PowerShell está
preinstalado en todas las versiones modernas del sistema operativo Windows.»** Su ejecutable es
`powershell.exe`.

*PowerShell 7* es el producto que sigue evolucionando: **«Con el lanzamiento de PowerShell 6.0,
PowerShell se convirtió en un proyecto de código abierto basado en .NET Core 2.0. Pasar de .NET
Framework a .NET Core permitió a PowerShell convertirse en una solución multiplataforma.»** Se
instala aparte y no sustituye al anterior: **«PowerShell 7 no reemplaza Windows PowerShell 5.1. Se
instala en un nuevo directorio y se ejecuta en paralelo con Windows PowerShell 5.1.»** Por eso
cambió el nombre del ejecutable: **«El nombre binario de PowerShell se ha cambiado de powershell(.exe)
a pwsh(.exe). Este cambio proporciona una manera determinista para que los usuarios ejecuten
PowerShell en máquinas y admitan instalaciones en paralelo de Windows PowerShell y PowerShell.»**

Las versiones de PowerShell 7 son de dos clases. La versión LTS: **«Una versión LTS de PowerShell es
una versión LTS de .NET.»** y **«Las actualizaciones de una versión LTS solo contienen
actualizaciones de seguridad críticas y correcciones de mantenimiento»**. La versión estable: **«una
versión estable es una versión que se produce entre versiones LTS»**, y **«Microsoft admite una
versión estable durante aproximadamente seis meses después de la próxima versión LTS.»** La tabla de
Microsoft, leída el 05-10-2026:

| Versión | Clase | Publicada | Fin de soporte | Basada en |
|---|---|---|---|---|
| PowerShell 7.6 | LTS | 18-03-2026 | 14-11-2028 | .NET 10.0 |
| PowerShell 7.5 | Estable | 23-01-2025 | 10-11-2026 | .NET 9.0 |
| PowerShell 7.4 | LTS anterior | 16-11-2023 | 10-11-2026 | .NET 8.0 |
| Windows PowerShell 5.1 | Componente de Windows | Agosto de 2016 | El del propio Windows | .NET Framework |

El número de revisión (el tercer dígito) cambia cada mes y no se da aquí; **«Microsoft solo admite la
versión más actualizada»**. La versión que corre en una sesión se ve con la variable automática
`$PSVersionTable`, que **«contiene información de la versión sobre la sesión de PowerShell»**.

Algunos módulos de Windows PowerShell no pasaron a PowerShell 7. Entre los que Microsoft cita como
**«Los módulos ya no se incluyen con PowerShell»** están el ISE, `Microsoft.PowerShell.LocalAccounts`,
`PSScheduledJob` y `PSWorkflow` (el flujo de trabajo de PowerShell). Para lo que sólo funciona en 5.1
se sigue usando `powershell.exe`.

### Instalación de PowerShell 7 en Windows

Microsoft da cinco vías y dice para qué sirve cada una:

| Método | Para qué |
|---|---|
| WinGet | **«manera recomendada de instalar PowerShell en clientes de Windows»** |
| Paquete MSI | **«mejor opción para los escenarios de implementación empresarial y servidores de Windows»** |
| Paquete MSIX | **«una manera fácil de instalar para usuarios casuales de PowerShell, pero tiene limitaciones»** |
| Paquete ZIP | **«forma más sencilla de cargar o instalar varias versiones o instalar en sistemas basados en Windows Server Core, Windows IoT y Arm»** |
| Herramienta global de .NET | Para desarrolladores de .NET que ya usan otras herramientas globales |

WinGet es el administrador de paquetes de Windows; **«La herramienta de línea de comandos winget está
incluida en Windows 11 y Windows Server 2025 como parte del App Installer»**, y **«winget no está
disponible en Windows Server 2022 ni en versiones anteriores»**. Las órdenes que da la documentación:

```powershell
winget search --id Microsoft.PowerShell --exact
winget install --id Microsoft.PowerShell --source winget
winget install --id Microsoft.PowerShell --source winget --installer-type wix
```

La segunda instala el paquete MSIX (**«A partir del paquete winget para PowerShell 7.6.0, winget
instala el paquete MSIX de forma predeterminada.»**); la tercera, el MSI. Instalado en Windows, el
directorio de PowerShell 7 es **«normalmente, C:\Program Files\PowerShell\7 en sistemas Windows»**, y
lo guarda la variable automática `$PSHOME`.

### Dónde se escribe: consola, editores y elevación

Las órdenes se escriben en la consola de PowerShell, que en Windows 11 puede abrirse dentro de
Terminal Windows (**«En función de la versión de Windows 11 que esté ejecutando, Windows PowerShell
podría abrirse en Terminal Windows.»**). Para escribir scripts, Microsoft recomienda un editor:
**«Visual Studio Code con la extensión de PowerShell es el editor recomendado para escribir scripts de
PowerShell.»** El editor clásico, el ISE, sigue en Windows pero congelado: **«Windows PowerShell ISE
sigue estando disponible para Windows. Sin embargo, ya no se incluye en el desarrollo activo de
características. El ISE solo funciona con PowerShell 5.1 y versiones anteriores.»**

Muchas tareas de administración exigen privilegios. El libro *PowerShell 101* lo explica: **«PowerShell
no participa en el Control de acceso de usuario (UAC). Esto significa que no puede solicitar la
elevación para las tareas que requieren la aprobación de un administrador.»** La solución es abrir la
consola con **«Ejecutar como administrador»**; la ventana se reconoce porque su barra de título indica
**«Administrador: Windows PowerShell»**. La recomendación de Microsoft es usarla sólo cuando haga
falta: **«Solo debe ejecutar PowerShell con privilegios elevados como administrador cuando sea
absolutamente necesario.»**

### Los comandos: cmdlets, funciones, alias y scripts

El comando nativo de PowerShell es el cmdlet: **«Los comandos compilados en PowerShell se conocen
como cmdlets, pronunciados como "command-let", no "CMD-let". La convención de nomenclatura de los
cmdlets sigue un formato singular Verbo-Sustantivo para que sean fácilmente descubribles. Por
ejemplo, Get-Process es el cmdlet para determinar qué procesos se ejecutan y Get-Service es el cmdlet
para recuperar una lista de servicios.»** El verbo dice la acción (`Get`, `Set`, `New`, `Remove`,
`Start`, `Stop`) y el sustantivo, en singular, el objeto (`Service`, `Item`, `Content`). Además hay
**«Las funciones, también conocidas como cmdlets de script, y los alias»**, y **«El término "comando
de PowerShell" describe cualquier comando de PowerShell, independientemente de si es un cmdlet,
función o alias.»**

Los parámetros se escriben tras el nombre, precedidos de guion (`Get-Service -Name w32time`). Algunos
son posicionales y pueden escribirse sin nombre: en `help Get-Help -Full`, el valor `Get-Help` ocupa
el lugar del parámetro `Name` porque **«Name es un parámetro posicional»**. Los cmdlets que cambian el
sistema, como `Remove-Item`, admiten dos parámetros que importan mucho al administrador: `-WhatIf`, que **«Muestra lo que sucedería si el cmdlet se ejecuta. El cmdlet no se ejecuta.»**, y
`-Confirm`, que **«Le pide confirmación antes de ejecutar el cmdlet.»**

*Alias.* **«Un alias es un nombre o alias alternativo para un cmdlet o para un elemento de comando,
como una función, un script, un archivo o un archivo ejecutable.»** PowerShell trae alias integrados
que imitan las órdenes de `cmd.exe` y de Unix: **«incluidos cd y chdir para el cmdlet Set-Location, ls
y dir en Windows y dir en Linux y macOS para el cmdlet Get-ChildItem»**. La ayuda de cada cmdlet
distingue los alias de todas las plataformas de los que sólo existen en Windows (`ls`, `cp`, `mv`,
`rm`, `cat`, `sort`; tabla del epígrafe 11). Los cmdlets de alias son `Get-Alias`, `New-Alias`, `Set-Alias`, `Remove-Alias`,
`Export-Alias` e `Import-Alias`. Dos límites: **«Los alias que cree solo se guardan en la sesión
actual»** (para conservarlos se ponen en el perfil), y **«No se puede asignar un alias a un comando y
sus parámetros»**; para eso se escribe una función.

*Scripts.* **«Un script es un archivo de texto sin formato que contiene uno o varios comandos de
PowerShell.»** y **«Los scripts de PowerShell tienen una extensión de archivo .ps1.»** Se ejecuta
escribiendo su ruta; si está en el directorio actual, con `.\` delante:

```powershell
C:\Scripts\Get-ServiceLog.ps1
.\Get-ServiceLog.ps1 -ServiceName WinRM
```

No basta con escribir el nombre ni con hacer doble clic: **«Como característica de seguridad,
PowerShell no ejecuta scripts al hacer doble clic en el icono de script en el Explorador de archivos o
al escribir el nombre del script sin una ruta de acceso completa, incluso cuando el script está en el
directorio actual.»** Los parámetros de un script se declaran con `param`, que **«debe ser la primera
instrucción de un script, excepto los comentarios y las instrucciones #Requires»**. Los comentarios
de una línea empiezan por `#`; los de bloque **«comenzar con <# y terminar con #>»** [sic]. Para
ejecutar un script en otros equipos se usa **«el parámetro FilePath del cmdlet Invoke-Command»**.

Dos operadores sirven para lanzar scripts y órdenes guardadas. El de llamada, `&`, **«Ejecuta un
comando, un script o un bloque de scripts»**, y hace falta cuando la ruta lleva espacios y va entre
comillas (`& ".\script name with spaces.ps1"`); sin `&`, PowerShell sólo mostraría la cadena. El de
*dot sourcing*, un punto seguido de espacio (`. .\sample.ps1`), **«Ejecuta un script en el ámbito
actual para que las funciones, alias y variables que cree el script se agreguen al ámbito actual»**.

### Proveedores y unidades

PowerShell presenta con el aspecto de un disco muchos almacenes de datos que no son discos: **«Los
proveedores de PowerShell son programas .NET que proporcionan acceso a almacenes de datos
especializados para facilitar la visualización y administración. Los datos aparecen en una unidad y
accede a los datos en una ruta de acceso como lo haría en una unidad de disco duro.»** Los integrados:

| Proveedor | Unidad | Qué contiene |
|---|---|---|
| Alias | `Alias:` | Los alias de la sesión |
| Certificate | `Cert:` | Los almacenes de certificados |
| Environment | `Env:` | Las variables de entorno |
| FileSystem | `C:` y las demás según el equipo | Ficheros y carpetas |
| Function | `Function:` | Las funciones |
| Registry | `HKLM:`, `HKCU:` | El Registro de Windows |
| Variable | `Variable:` | Las variables de la sesión |
| WSMan | `WSMan:` | La configuración de la administración remota |

**«Los proveedores de certificado de, Registryy WSMan solo están disponibles en la plataforma
Windows.»** [sic]. La consecuencia práctica es que los mismos cmdlets sirven para todo: **«el cmdlet
New-Item crea un nuevo elemento. En la unidad de C: compatible con el proveedor de FileSystem, puede
usar New-Item para crear un nuevo archivo o carpeta. En las unidades compatibles con el proveedor de
Registry de, puede usar New-Item para crear una nueva clave del Registro.»** Los proveedores
disponibles se listan con `Get-PSProvider`. Una carpeta puede montarse como unidad propia con
`New-PSDrive` (epígrafe 11).

### El perfil

**«Un perfil de PowerShell es un script que se ejecuta cuando se inicia PowerShell. Puede usar el
perfil como script de inicio para personalizar el entorno. Puede agregar comandos, alias, funciones,
variables, módulos, unidades de PowerShell y mucho más.»** PowerShell **«no crea los perfiles
automáticamente»**. Hay cuatro, según afecten a todos los usuarios o al actual y a todos los
programas que alojan PowerShell (*hosts*) o sólo al actual. En Windows, con PowerShell 7:

| Perfil | Ruta en Windows |
|---|---|
| Todos los usuarios, todos los hosts | `$PSHOME\Profile.ps1` |
| Todos los usuarios, host actual | `$PSHOME\Microsoft.PowerShell_profile.ps1` |
| Usuario actual, todos los hosts | `$HOME\Documents\PowerShell\Profile.ps1` |
| Usuario actual, host actual | `$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1` |

**«Los scripts de perfil se ejecutan en el orden indicado.»** y **«El perfil de CurrentUserCurrentHost
siempre se ejecuta en último lugar»**, de modo que lo que se pone en él prevalece. La variable
automática `$PROFILE` **«almacena la ruta de acceso al perfil "Usuario actual, Host actual"»**; los
otros tres están en sus propiedades (`$PROFILE.AllUsersAllHosts`, etc.). El perfil es un script, así
que sólo se carga si la directiva de ejecución lo permite.

### La directiva de ejecución

**«La directiva de ejecución de PowerShell es una característica de seguridad que controla las
condiciones en las que PowerShell carga archivos de configuración y ejecuta scripts. Esta
característica ayuda a evitar la ejecución de scripts malintencionados.»** Pero no es una barrera
infranqueable: **«La directiva de ejecución no es un límite de seguridad, es la defensa en
profundidad. Por ejemplo, los usuarios pueden omitir fácilmente una directiva escribiendo el
contenido del script en la línea de comandos cuando no pueden ejecutar un script.»** Y sólo existe en
Windows: **«El cumplimiento de estas directivas solo se produce en plataformas Windows.»**

Las directivas:

| Directiva | Qué hace |
|---|---|
| Restricted | **«Permite comandos individuales, pero no permite scripts.»** Impide también cargar los perfiles y los módulos de script |
| AllSigned | **«Requiere que todos los scripts y archivos de configuración estén firmados por un editor de confianza, incluidos los scripts que escriba en el equipo local.»** |
| RemoteSigned | **«Requiere una firma digital de un editor de confianza en scripts y archivos de configuración que se descargan desde Internet»**; **«No requiere firmas digitales en scripts escritos en el equipo local y no descargados de Internet.»** |
| Unrestricted | **«Los scripts sin firmar se pueden ejecutar.»**; avisa antes de ejecutar lo que no viene de la intranet local |
| Bypass | **«No se bloquea nada y no hay advertencias ni avisos.»** |
| Undefined | **«No hay ninguna directiva de ejecución establecida en el ámbito actual.»** |
| Default | Pone la predeterminada |

Cuál rige si nadie la cambia lo dice con claridad la página de Windows PowerShell 5.1: Default es
**«Restricted para clientes de Windows.»** y **«RemoteSigned para servidores Windows.»**, y **«Si la
directiva de ejecución en todos los ámbitos es Undefined, la directiva de ejecución efectiva es
Restricted para los clientes de Windows y RemoteSigned para Windows Server.»** En un Windows 11 recién
instalado, por tanto, ejecutar un `.ps1` escribiendo su ruta falla hasta que se cambia la directiva
(el doble clic no lo ejecuta nunca, sea cual sea la directiva: epígrafe 1, *Scripts*). La página equivalente de PowerShell 7 se contradice: en un sitio llama a RemoteSigned
**«Directiva de ejecución predeterminada para equipos Windows.»** y en otro repite que, sin directiva
en ningún ámbito, la efectiva es **«Restricted, que es el valor predeterminado para los clientes de
Windows»**. En Linux y macOS la directiva es Unrestricted **«y no se puede cambiar»**.

RemoteSigned funciona con la marca que Windows pone a lo descargado: **«los programas como Internet
Explorer y Microsoft Edge agregan un flujo de datos alternativo a los archivos que se descargan. Esto
marca el archivo como "procedente de Internet".»** Un script descargado y no firmado puede ejecutarse
si se desbloquea con el cmdlet `Unblock-File`.

La directiva se fija por ámbitos, y el orden importa:

| Ámbito | Alcance | Dónde se guarda (5.1) |
|---|---|---|
| MachinePolicy | Directiva de grupo para todos los usuarios del equipo | Directiva de grupo |
| UserPolicy | Directiva de grupo para el usuario actual | Directiva de grupo |
| Process | **«afecta solo a la sesión actual de PowerShell»** | Variable de entorno `$Env:PSExecutionPolicyPreference`; se pierde al cerrar |
| CurrentUser | **«afecta solo al usuario actual»** | Registro, `HKCU:\Software\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell` |
| LocalMachine | Ámbito por defecto, **«que afecta a todos los usuarios del equipo»** | Registro, `HKLM:\Software\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell` |

PowerShell 7 guarda CurrentUser y LocalMachine en ficheros `powershell.config.json` en lugar del
Registro, y por eso **«Windows PowerShell 5.1 y PowerShell 6.0 y versiones posteriores almacenan la
configuración de directiva de ejecución en diferentes ubicaciones y se administran por separado»**.
Si no hay directiva de grupo, **«Process - Prioridad más alta»**, **«CurrentUser - Segunda prioridad
más alta»** y **«LocalMachine - Prioridad más baja»**. La directiva de grupo manda sobre todo: **«La
configuración de directiva de grupo invalida las directivas de ejecución establecidas en PowerShell
en todos los ámbitos.»** El valor se fija en la directiva **«Activar ejecución de scripts»**, bajo
**«Administrative Templates\Windows Components\Windows PowerShell»**; deshabilitarla **«equivale a la
directiva de Restricted ejecución»**, y habilitarla deja escoger entre permitir todos los scripts
(Unrestricted), los locales y los remotos firmados (RemoteSigned) o sólo los firmados (AllSigned).

Las órdenes:

```powershell
Get-ExecutionPolicy                       # la efectiva en la sesión
Get-ExecutionPolicy -List                 # la de cada ámbito, en orden de prioridad
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned                       # LocalMachine
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope LocalMachine      # la quita
powershell.exe -ExecutionPolicy AllSigned                               # sólo esa sesión
```

**«El ámbito predeterminado del cmdlet Set-ExecutionPolicy es LocalMachine, lo que afecta a todos los
usuarios que usan el equipo. Para cambiar la directiva de ejecución de LocalMachine, inicie
PowerShell con Ejecutar como administrador.»** El cambio **«es efectivo inmediatamente»**. El ejemplo
de Microsoft para leer la tabla: con CurrentUser en RemoteSigned y LocalMachine en AllSigned, **«la
directiva de ejecución efectiva es RemoteSigned porque la directiva de ejecución del usuario actual
tiene prioridad sobre la directiva de ejecución establecida para el equipo local.»**

## 2. La ayuda

### Get-Help

PowerShell lleva su manual dentro. **«Tanto Get-Help como Get-Command son recursos valiosos para
detectar y comprender comandos en PowerShell.»** El primero **«es un comando multipropósito que le
ayuda a aprender a usar comandos una vez que los encuentre»**.

```powershell
Get-Help -Name Get-Help
Get-Help -Name Get-Command -Full
Get-Help -Name Get-Command -Detailed
Get-Help -Name Get-Command -Examples
Get-Help -Name Get-Command -Online
Get-Help -Name Get-Command -Parameter Noun
```

Lo que da cada parámetro:

| Parámetro | Qué muestra |
|---|---|
| (ninguno) | Nombre, sinopsis, sintaxis, descripción, vínculos relacionados y comentarios |
| `-Detailed` | Añade la descripción de los parámetros y los ejemplos |
| `-Full` | El artículo entero: **«la salida incluye varias secciones adicionales. Entre estas secciones, PARÁMETROS a menudo proporciona una explicación detallada de cada parámetro»** |
| `-Examples` | Sólo el nombre, la sinopsis y los ejemplos |
| `-Parameter <nombre>` | Sólo ese parámetro (`*` para todos) |
| `-Online` | **«abre el artículo de ayuda en el explorador web predeterminado. El contenido en línea es el contenido que se encuentra más actualizado.»** No sirve para los artículos *about* |
| `-ShowWindow` | La ayuda en una ventana aparte; **«requiere un sistema operativo con una interfaz gráfica de usuario (GUI). Devuelve un error al intentar usarlo en Windows Server Core.»** |

La ayuda de `Get-Help` advierte que `-Detailed`, `-Examples` y `-Full` sólo surten efecto cuando los
ficheros de ayuda están instalados en el equipo, y que no cambian nada en los artículos *about*.

La sintaxis de `Get-Help` aparece repetida seis veces porque el cmdlet tiene seis conjuntos de
parámetros, y por eso hay parámetros incompatibles: **«no puede usar los parámetros Full y Detailed
de Get-Help juntos porque pertenecen a diferentes conjuntos de parámetros.»** Lo mismo pasa en
muchos cmdlets: dos parámetros de conjuntos distintos no se pueden mezclar.

En lugar de `Get-Help` se suele escribir `help`, una función que pagina la salida: **«Canaliza la
salida de Get-Help para more.com, mostrando una página de contenido de ayuda a la vez.»** En el ISE
no pagina, porque **«El ISE no admite el uso de more.com»**.

### Buscar comandos con la ayuda

`Get-Help` admite comodines y, si no encuentra un nombre, busca en el texto de toda la ayuda: **«Al
usar Get-Help para buscar comandos, inicialmente realiza una búsqueda de caracteres comodín para los
nombres de comandos en función de la entrada. Si eso no encuentra ninguna coincidencia, realiza una
búsqueda completa de texto completo en todos los artículos de ayuda de PowerShell en el sistema.»**
De ahí estos resultados, que la propia documentación enseña:

| Orden | Resultado |
|---|---|
| `help *process*` | Los comandos con *process* en el nombre (`Get-Process`, `Stop-Process`…) |
| `help process` | Lo mismo: no hay comando llamado así y busca con comodines |
| `help pr*cess` | Nada: con un comodín dentro **«solo busca comandos que coincidan con el patrón proporcionado. No realiza una búsqueda de texto completo.»** |
| `help -process` | Error: lo toma por un nombre de parámetro |
| `help *-process` | Los que terminan en *-process* |
| `help processes` | Búsqueda de texto completo: 78 resultados frente a 12, muchos ajenos |

**«Si la búsqueda solo encuentra una coincidencia, Get-Help muestra el contenido de ayuda en lugar de
enumerar los resultados de la búsqueda.»**

### Los artículos about

Además de la ayuda de cada comando, hay artículos conceptuales cuyo nombre empieza por `about_`:
`about_Variables`, `about_Arrays`, `about_Pipelines`, `about_Execution_Policies`… Son la fuente de
este tema. Se listan con `help about_*` y se abren con su nombre (`help about_Updatable_Help`).

### Actualizar la ayuda

La ayuda no viene instalada: **«A partir de la versión 3.0 de PowerShell, el contenido de ayuda no se
incluye previamente con el sistema operativo.»** La primera vez que se ejecuta `Get-Help`, PowerShell
ofrece descargarla, y **«Al responder Sí pulsando Y ejecuta el cmdlet Update-Help»**.

```powershell
Update-Help -Force
```

**«Debe usar el parámetro Force para asegurarse de descargar la versión más reciente del contenido de
ayuda.»** En Windows PowerShell 5.1, **«debe ejecutar Update-Help como administrador en una sesión de
PowerShell con privilegios elevados»**. Y para un equipo sin conexión: **«Update-Help requiere acceso
a Internet para descargar el contenido de ayuda. Si el equipo no tiene acceso a Internet, use el
cmdlet Save-Help en un equipo con acceso a Internet para descargar y guardar el contenido de ayuda
actualizado. A continuación, use el parámetro SourcePath de Update-Help para especificar la ubicación
del contenido de ayuda actualizado guardado.»** Es normal que algún módulo falle al actualizar;
**«Los errores no son raros»**.

### Get-Command

`Get-Command` **«obtiene todos los comandos instalados en el equipo, incluidos cmdlets, alias,
funciones, filtros, scripts y aplicaciones»**. A diferencia de la ayuda, **«Get-Command obtiene sus
datos directamente desde el código de comando, a diferencia de Get-Help, que obtiene su información
de temas de ayuda»**, así que encuentra también lo que no tiene ayuda instalada.

```powershell
Get-Command                                 # cmdlets, funciones y alias instalados
Get-Command -Noun Process                   # los que actúan sobre procesos
Get-Command -Verb Get -Noun *Service*
Get-Command -Name Get-Command -Syntax       # sólo la sintaxis
Get-Command *                               # también los ejecutables del PATH
```

Los parámetros `Name`, `Noun` y `Verb` aceptan comodines. **«Sin parámetros, Get-Command obtiene todos
los cmdlets, funciones y alias instalados en el equipo.»**, mientras que **«Get-Command * obtiene
todos los tipos de comandos, incluidos todos los archivos que no son de PowerShell en la variable de
entorno PATH ($Env:PATH), que se muestra en el tipo de comando Application.»** Con el nombre exacto,
además, importa el módulo que contiene el comando.

### Get-Member

Como todo son objetos, la tercera herramienta de consulta es la que enseña qué tiene un objeto: **«El
Get-Member cmdlet obtiene los miembros, las propiedades y los métodos de los objetos .»** [sic].
Se le canaliza el objeto:

```powershell
Get-Process | Get-Member
Get-Process | Get-Member -MemberType Method
```

**«Get-Member devuelve una lista de miembros ordenados alfabéticamente. Los métodos se enumeran
primero, seguidos de las propiedades .»** [sic]. La primera línea de su salida (`TypeName:
System.Diagnostics.Process`) dice además el tipo .NET del objeto. Un método se invoca con un punto,
su nombre y paréntesis: **«Los paréntesis son necesarios para cada llamada de método, incluso cuando
no hay argumentos»** (`(Get-Process notepad).Kill()`).

## 3. Variables

### Qué es una variable

**«Una variable es una unidad de memoria en la que se almacenan los valores. En PowerShell, las
variables se representan mediante cadenas de texto que comienzan con un signo de dólar ($), como $a,
$processo $my_var.»** [sic]. Reglas que se preguntan:

- **«Los nombres de variable no distinguen mayúsculas de minúsculas»**: `$Ruta` y `$ruta` son la
  misma variable.
- **«No es necesario declarar la variable antes de usarla. El valor predeterminado de todas las
  variables es $null.»**
- **«El procedimiento recomendado es que los nombres de variable incluyan solo caracteres
  alfanuméricos y el carácter de subrayado (_).»** Un nombre con espacios o guiones exige llaves:
  `${save-items}` o `${Env:ProgramFiles(x86)}`.
- Lo que se crea en la consola dura lo que la sesión: **«Las variables que cree solo están
  disponibles en la sesión en la que se crean. Se pierden cuando cierra la sesión.»** Para tenerlas
  siempre, se ponen en el perfil.

Hay tres clases:

| Clase | Quién la crea y quién la cambia | Ejemplo de Microsoft |
|---|---|---|
| Creadas por el usuario | **«el usuario crea y mantiene las variables creadas por el usuario»** | `$MyVariable` |
| Automáticas | **«almacenan el estado de PowerShell»**; **«Los usuarios no pueden cambiar el valor de estas variables.»** | `$PSHOME` |
| De preferencia | **«almacenan preferencias de usuario para PowerShell»**; **«Los usuarios pueden cambiar los valores de estas variables.»** | `$MaximumHistoryCount` |

### Crear, cambiar y borrar

Se crea asignando un valor:

```powershell
$MyVariable = 1, 2, 3          # una matriz
$Path = "C:\Windows\System32"  # una cadena
$Processes = Get-Process       # el resultado de un comando
$a = $b = $c = 0               # el mismo valor a tres variables
$i,$j,$k = 10, "red", $true    # un valor a cada una
```

Para mostrar el valor basta escribir la variable. Para vaciarla o borrarla:

| Acción | Cómo |
|---|---|
| Quitar el valor (la variable sigue existiendo) | **«use el cmdlet Clear-Variable o cambie el valor a $null»** |
| Eliminar la variable | **«use Remove-Variable o Remove-Item»** (`Remove-Item -Path Variable:\MyVariable`) |
| Listar todas | `Get-Variable` (los nombres salen sin el `$`) |
| Crear o cambiar con opciones | `New-Variable`, `Set-Variable` |

### Tipos

**«Las variables de PowerShell se escriben de forma flexible, lo que significa que no se limitan a un
tipo determinado de objeto.»** El tipo lo dan los valores: **«El tipo de datos de una variable viene
determinado por los tipos de .NET de los valores de la variable. Para ver el tipo de objeto de una
variable, use Get-Member.»** (o el método `GetType()`).

```powershell
$a = 12          # System.Int32
$a = "Word"      # System.String
$a = 12, "Word"  # matriz de System.Int32 y System.String
```

Se puede fijar el tipo con una conversión entre corchetes delante del nombre: **«Puede usar un
atributo de tipo y una notación de conversión para asegurarse de que una variable solo puede contener
tipos de objetos o objetos específicos que se pueden convertir a ese tipo. Si intenta asignar un valor
de otro tipo, PowerShell intenta convertir el valor en su tipo. Si no se puede convertir el tipo, se
produce un error en la instrucción de asignación.»**

```powershell
[int]$number = 8
$number = "12345"   # se convierte a entero
$number = "Hello"   # error: no se puede convertir a System.Int32
[string]$words = "Hello"
$words = 2          # se convierte a cadena
$words += 10        # concatena: "210"
```

El último ejemplo es de examen: como `$words` es de tipo cadena, `+=` concatena y el resultado es
`210`, no `12`.

### Variables entre comillas

**«Si el nombre de la variable y el signo de dólar no están entre comillas, o si están entre comillas
dobles ("), el valor de la variable se usa en el comando o expresión.»** En cambio, **«Si el nombre de
la variable y el signo de dólar se incluyen entre comillas simples ('), el nombre de la variable se
usa en la expresión.»** Se desarrolla en el epígrafe 6.

### Ámbito

**«De forma predeterminada, las variables solo están disponibles en el ámbito en el que se crean.»**
Una variable creada dentro de una función sólo existe en la función; la creada en un script, sólo en
el script (salvo que se ejecute con *dot sourcing*). Las reglas:

- **«Un elemento es visible en el ámbito en el que se creó y en cualquier ámbito secundario, a menos
  que lo haga explícitamente privado.»**
- **«Un elemento que creó dentro de un ámbito solo se puede cambiar en el ámbito en el que se creó, a
  menos que especifique explícitamente un ámbito diferente.»**

Los ámbitos con nombre son `Global` (el de la sesión, donde están las variables automáticas y lo que
crean los perfiles), `Script` (el del fichero de script en ejecución) y `Local` (**«el ámbito
actual»**). Se fuerzan con un modificador delante del nombre: `$Global:Computers = "Server01"` crea
la variable en el ámbito global aunque se escriba en un script; `$Private:` la hace visible sólo en el
ámbito actual; y `$Using:` lleva el valor de una variable local a un script o comando que se ejecuta
fuera de la sesión, como el que se lanza en un equipo remoto.

### Variables automáticas que hay que conocer

| Variable | Qué contiene |
|---|---|
| `$_` y `$PSItem` | **«Contiene el objeto actual del objeto de canalización.»** [sic]; son la misma |
| `$?` | **«Contiene el estado de ejecución del último comando. Contiene True si el último comando se realizó correctamente y False si se produjo un error.»** |
| `$LASTEXITCODE` | **«Contiene el código de salida del último programa nativo o script de PowerShell que se ejecutó.»** |
| `$Error` | **«Contiene una matriz de objetos de error que representan los errores más recientes. El error más reciente es el primer objeto de error de la matriz $Error[0].»** |
| `$null` | **«una variable automática que contiene un valor nulo o vacío»** |
| `$true` y `$false` | Los valores lógicos; se usan **«en lugar de usar la cadena "false"»**, porque una cadena no vacía se evalúa como verdadera |
| `$args` | **«una matriz de valores para parámetros no declarados que se pasan a una función, un script o un scriptblock»** |
| `$Matches` | La tabla hash con lo que encontró el último `-match` que dio coincidencia: si el siguiente no la da, `$Matches` no se vacía (epígrafe 4) |
| `$HOME` | **«la ruta de acceso completa del directorio principal del usuario»**; en Windows, `$Env:USERPROFILE` |
| `$PSHOME` | El directorio de instalación de PowerShell |
| `$PROFILE` | La ruta del perfil del usuario actual y host actual |
| `$PSVersionTable` | **«una tabla hash de solo lectura que muestra detalles sobre la versión de PowerShell que se ejecuta en la sesión actual»** |
| `$PWD` | La ruta del directorio actual |

### Variables de entorno

Las variables de entorno del sistema se leen y escriben con el prefijo de la unidad `Env:`:

```powershell
$Env:windir                  # C:\Windows
$Env:Foo = 'An example'      # crea o cambia la variable de entorno Foo
Get-ChildItem Env:           # todas
```

Tres diferencias con las demás variables: **«Las variables de entorno, a diferencia de otros tipos de
variables en PowerShell, siempre se almacenan como cadenas.»**; se heredan por los procesos hijos; y
lo que se cambia así dura lo que la sesión: **«Al cambiar las variables de entorno en PowerShell, el
cambio afecta solo a la sesión actual.»** Para cambiarlas en los ámbitos de máquina o de usuario
**«debe usar los métodos de la clase System.Environment»**, y en el de máquina hace falta permiso.
En Windows sus nombres no distinguen mayúsculas; en Linux y macOS, sí (`$Env:Path` y `$Env:PATH`
son allí variables distintas).

## 4. Operadores

**«Un operador es un elemento de lenguaje que se puede usar en un comando o expresión.»** PowerShell
los agrupa así: aritméticos, de asignación, de comparación, lógicos, de redireccionamiento, de
división y combinación, de tipo, unarios y especiales. La regla que más se pregunta es que los
operadores de comparación y lógicos se escriben con guion y letras (`-eq`, `-gt`, `-and`), no con
los símbolos de otros lenguajes, porque `>` y `<` están ocupados por la redirección.

### Aritméticos

| Operador | Qué hace | Ejemplo de Microsoft |
|---|---|---|
| `+` | **«agrega números, concatena cadenas, matrices y tablas hash»** | `"file" + "name"` da `filename` |
| `-` | Resta o cambia el signo | `6 - 2` da 4 |
| `*` | **«multiplica los números o copia las cadenas y matrices el número de veces especificado»** | `"!" * 3` da `!!!` |
| `/` | Divide | `6 / 2` da 3 |
| `%` | **«devuelve el resto de una operación de división»** | `7 % 2` da 1 |
| `-band`, `-bor`, `-bxor`, `-bnot` | Operaciones bit a bit | `5 -band 3` da 1 |
| `-shl`, `-shr` | Desplazamiento de bits | `102 -shl 2` da 408 |

**«El método que se usa para evaluar la instrucción viene determinado por el tipo del objeto situado
más a la izquierda en la expresión.»** Por eso `"1" + 2` concatena y `1 + "2"` suma. El orden de
cálculo: paréntesis; signo negativo; multiplicación, división y resto; suma y resta; y por último los
operadores bit a bit. Los ejemplos oficiales: **«3+6/3*4 # result = 11»**, **«3+6/(3*4) # result =
3.5»** y **«(3+6)/3*4 # result = 12»**. La división no trunca: si el resultado no es entero, da
decimales; y al convertir a entero redondea al entero más cercano y, si la parte decimal es ,5, al par
más cercano: `[int](5/2)` da 2 y `[int](7/2)` da 4.

PowerShell entiende sufijos multiplicadores en los números (`kb`, `mb`, `gb`, `tb`, `pb`, en múltiplos
de 1024, sin distinguir mayúsculas: `100KB`, `1mb`, `512MB`), lo que es cómodo para filtrar ficheros
por tamaño (`$file.Length -gt 100KB`).

### De asignación

`=`, `+=`, `-=`, `*=`, `/=` y `%=`. **«Puede combinar operadores aritméticos con asignación para
asignar el resultado de la operación aritmética a una variable.»** Los unarios `++` y `--` suman o
restan uno: **«para incrementar la variable $a de 9 a 10, escriba $a++»**.

### De comparación

| Operador | Devuelve verdadero cuando… |
|---|---|
| `-eq` | **«es igual a»** |
| `-ne` | no es igual |
| `-gt` / `-ge` | **«El lado izquierdo es mayor»** / mayor o igual |
| `-lt` / `-le` | **«El lado izquierdo es más pequeño»** / menor o igual |
| `-like` / `-notlike` | **«la cadena coincide con el patrón de caracteres comodín»** / no coincide |
| `-match` / `-notmatch` | **«la cadena coincide con el patrón regex»** / no coincide |
| `-replace` | No compara: **«busca y reemplaza cadenas que coinciden con un patrón regex»** |
| `-contains` / `-notcontains` | **«la colección contiene un valor»** / no lo contiene |
| `-in` / `-notin` | **«el valor está en una colección»** / no está |
| `-is` / `-isnot` | el objeto es (o no es) del tipo indicado |

Cuatro reglas:

1. *Mayúsculas.* **«Las comparaciones de cadenas no distinguen entre mayúsculas y minúsculas, a
   menos que se utilice un operador explícitamente sensible»**. Para distinguirlas se añade una `c`
   tras el guion (`-ceq`, `-clike`, `-cmatch`, `-creplace`); con una `i` (`-ieq`) se pide
   expresamente que no se distingan. `'PowerShell' -eq 'powershell'` es verdadero; con `-ceq`, falso.
2. *Escalar o colección a la izquierda.* **«Cuando el valor izquierdo de la expresión de comparación
   es un valor escalar de , el operador devuelve un valor booleano de . Cuando el valor izquierdo de la
   expresión es una colección, el operador devuelve los elementos de la colección que coinciden con el
   valor derecho de la expresión.»** [sic]. Así, `1,2,3 -eq 2` no devuelve `True` sino `2`. Los de
   contención y tipo, en cambio, **«siempre devuelven un valor booleano»**.
3. *Conversión al tipo de la izquierda.* **«el valor del lado derecho de la comparación se puede
   convertir al tipo de valor del lado izquierdo para compararlos»**: `1 -eq '1.0'` es verdadero. Por
   lo mismo, para saber si algo es nulo, **«debe colocar $null en el lado izquierdo del operador de
   igualdad»** (`$null -eq $a`), porque con una matriz a la izquierda el operador filtraría.
4. *No usar `>` para comparar.* **«En la mayoría de los lenguajes de programación, el operador mayor
   que es >. En PowerShell, este carácter se usa para el redireccionamiento.»** El ejemplo de
   Microsoft: `if (36 > 42) { "true" } else { "false" }` devuelve `false`, pero además crea **«un
   archivo denominado 42, con el contenido 36»**; y `36 < 42` da error porque **«The '<' operator is
   reserved for future use.»**

`-like` frente a `-match`: el primero usa comodines y exige que el patrón cubra la cadena entera; el
segundo, expresiones regulares, y le basta una coincidencia parcial. Microsoft lo enseña con el mismo
texto: `'PowerShell' -match 'shell'` es verdadero y `'PowerShell' -like 'shell'` es falso; para que
`-like` acierte hacen falta los comodines (`'PowerShell' -like '*shell'` es verdadero). **«Los operadores -match y -notmatch también rellenan la variable automática $Matches a
menos que el lado izquierdo de la expresión sea una colección.»**

`-replace` sigue la sintaxis `<entrada> -replace <regex>, <sustituto>`. El ejemplo de la documentación
cambia la extensión de todos los `.txt` del directorio:

```powershell
Get-ChildItem *.txt | Rename-Item -NewName { $_.Name -replace '\.txt$','.log' }
```

`-contains` y `-in` son el mismo operador con los lados cambiados: **«Los operadores -in y -notin se
introdujeron en PowerShell 3 como la inversa sintáctica de los operadores de -contains y
-notcontains.»** Se escribe `<colección> -contains <valor>` y `<valor> -in <colección>`:
`'a','b','c' -contains 'b'` y `'b' -in 'a','b','c'` son ambos verdaderos.

### Lógicos

**«Use operadores lógicos (-and, -or, -xor, -not, !) para conectar instrucciones condicionales a un
único condicional complejo.»** `-not` y `!` son lo mismo. La evaluación se corta en cuanto se conoce
el resultado: **«Si el operando izquierdo de una instrucción que contiene la -or instrucción es TRUE,
el operando derecho no se evalúa.»** [sic], y **«Los -andoperadores , -or y -xor tienen la misma prioridad. Se
evalúan de izquierda a derecha»** [sic].

Qué es verdadero y qué es falso cuando PowerShell convierte un valor a lógico: son falsos **«Cadenas
vacías como '' o ""»**, **«Valores NULL como $null»** y **«Cualquier tipo numérico con el valor de
0»**; son verdaderas las **«Cadenas no vacías»** y las demás instancias que no son colecciones.

### De división y combinación de cadenas

**«El -split operador divide una cadena en subcadenas. El -join operador concatena varias cadenas en
una sola cadena.»** [sic].

```powershell
-split "red yellow blue green"             # red / yellow / blue / green
"Lastname:FirstName:Address" -split ":"    # Lastname / FirstName / Address
-join ("a", "b", "c")                      # abc
"Windows", "PowerShell", "2.0" -join " "   # Windows PowerShell 2.0
```

En `-split`, el delimitador por defecto **«es un espacio en blanco, incluidos espacios y caracteres no
imprimibles, como nueva línea ('n) y tabulación ('t)»** [sic], y lo que se le da como delimitador se
trata como expresión regular: **«El operador Split de PowerShell usa una expresión regular en el
delimitador, en lugar de un carácter simple.»** En `-join`, sin delimitador **«El valor
predeterminado es ningún delimitador ("")»**. Una trampa: `-join "a", "b", "c"` no une nada, porque
**«El operador unario join (-join <string[]>) tiene mayor prioridad que una coma»**; hay que poner
paréntesis.

### De tipo

`-is`, `-isnot` y `-as` **«para buscar o cambiar el tipo de .NET de un objeto»**: `12 -is [int]` es
verdadero; `"5" -as [int]` convierte la cadena en entero.

### Especiales

| Operador | Para qué |
|---|---|
| `( )` agrupación | **«sirve para invalidar la precedencia del operador en las expresiones»**; también hace que un comando se ejecute antes y su salida entre en una expresión |
| `$( )` subexpresión | **«Devuelve el resultado de una o varias instrucciones»**; sirve para meter un resultado dentro de una cadena |
| `@( )` subexpresión de matriz | **«El resultado siempre es una matriz de 0 o más objetos.»** |
| `@{ }` | Declara una tabla hash |
| `&` llamada | Ejecuta un comando, script o bloque de script guardado en una variable o cadena |
| `&` al final | **«Ejecuta la canalización antes que en segundo plano, en un trabajo de PowerShell»** [sic]; equivale a `Start-Job` |
| `.` *dot sourcing* | Ejecuta un script en el ámbito actual |
| `[ ]` conversión | **«Convierte o limita los objetos al tipo especificado.»** |
| `,` coma | **«Como operador binario, la coma crea una matriz»**; como unario, una matriz de un elemento (`,1`) |
| `[ ]` índice | Elige elementos de una matriz o de una tabla hash |
| `\|` canalización | Pasa la salida de un comando al siguiente (epígrafe 8) |
| `..` intervalo | Una serie de enteros o, desde PowerShell 6, de caracteres: `1..10`, `10..1`, `'a'..'e'` |
| `.` acceso a miembros | Propiedades y métodos: `$myProcess.PeakWorkingSet` |
| `::` miembro estático | Miembros de una clase .NET: `[datetime]::Now` |
| `-f` formato | Formato compuesto de .NET: `"{0} {1,-10} {2:N}" -f 1,"hello",[Math]::PI` |

Los de PowerShell 7, que no existen en Windows PowerShell 5.1:

- Ternario: **«PowerShell 7.0 introdujo una nueva sintaxis mediante el operador ternario»**,
  `<condición> ? <si verdadero> : <si falso>`. Ejemplo: `$message = (Test-Path $path) ? "Path
  exists" : "Path not found"`. Si una de sus partes es un comando, va entre paréntesis.
- Fusión de nulos: **«El operador de fusión de NULL ?? devuelve el valor de su operando de la izquierda
  si no es NULL. De lo contrario, evalúa el operando derecho y devuelve su resultado.»** `$x ?? 100`;
  y `??=` asigna sólo si la variable es nula.
- Cadena de canalización: **«A partir de PowerShell 7, PowerShell implementa los operadores && y ||
  para encadenar canalizaciones condicionalmente.»** **«El operador && ejecuta la canalización de la
  derecha, si la canalización izquierda se realizó correctamente. Por el contrario, el operador ||
  ejecuta la canalización de la derecha si se produjo un error en la canalización izquierda.»** Ejemplo:
  `Get-Process notepad && Stop-Process -Name notepad`.

## 5. Arrays (matrices) y tablas hash

### Crear una matriz

**«Una matriz es una estructura de datos diseñada para almacenar una colección de elementos.»** y
**«Los elementos pueden ser del mismo tipo o de tipos diferentes.»** La documentación en castellano
traduce *array* por «matriz».

```powershell
$A = 22,5,10,8,12,9,80      # siete enteros
$B = ,7                     # matriz de un solo elemento
$C = 5..8                   # 5, 6, 7 y 8
$b = @()                    # matriz vacía
$p = @(Get-Process Notepad) # siempre matriz, aunque haya 0 o 1 procesos
[Int32[]]$ia = 1500, 2230, 3350, 4000   # sólo admite enteros
```

**«Cuando no se especifica ningún tipo de datos, PowerShell crea cada matriz como una matriz de
objetos (System.Object[]).»** Una matriz tipada (`[int32[]]`, `[string[]]`) sólo admite valores de ese
tipo o convertibles. El operador `@( )` **«es útil en scripts cuando se obtienen objetos, pero no sabe
cuántos esperar»**: garantiza que el resultado se pueda contar e indexar aunque el comando devuelva
un solo objeto o ninguno.

### Leer elementos

| Expresión | Qué devuelve (con `$a = 0..9`) |
|---|---|
| `$a` | Todos los elementos |
| `$a[0]` | El primero: **«Los valores de índice comienzan en 0.»** |
| `$a[2]` | El tercero |
| `$a[1..4]` | Del segundo al quinto |
| `$a[-1]` | El último: **«-1 hace referencia al último elemento de la matriz»** |
| `$a[-3..-1]` | Los tres últimos, en orden |
| `$a[0,2+4..6]` | Los de índice 0, 2, 4, 5 y 6 |
| `$a[0..-2]` | Ojo: el primero, el último y el penúltimo, no «todos menos el último» |

El último caso es la trampa que la propia documentación señala: **«un error común es suponer que
$a[0..-2] hace referencia a todos los elementos de la matriz, excepto por el último. Hace referencia a
los elementos primero, último y segundo a último de la matriz.»**

### Contar, añadir, quitar

**«Count: esta propiedad es la propiedad más usada para determinar el número de elementos de
cualquier colección, no solo una matriz.»**; `Length` da lo mismo en una matriz, pero en una cadena
es el número de caracteres. Una matriz tiene tamaño fijo: `+=` no añade, sino que crea otra: **«Cuando
se usa el operador +=, PowerShell crea realmente una nueva matriz con los valores de la matriz original
y el valor agregado. Esto puede provocar problemas de rendimiento si la operación se repite varias
veces o el tamaño de la matriz es demasiado grande.»** Tampoco hay operador para quitar: **«No es
fácil eliminar elementos de una matriz, pero puede crear una nueva matriz que solo contenga elementos
seleccionados de una matriz existente»**. Dos matrices se unen con `+`.

### Recorrer y filtrar

Una matriz se recorre con los bucles del epígrafe 10 (`foreach`, `for`, `while`). Tiene además dos métodos
propios: `ForEach()` (**«Este método se agregó en PowerShell v4.»**), que aplica un bloque de script a
cada elemento, y `Where()`, que **«Permite filtrar o seleccionar los elementos de la matriz»**:

```powershell
$a = @(0 .. 3)
$a.ForEach({ $_ * $_})            # 0, 1, 4, 9 (ejemplo de Microsoft)
(1..10).Where({ $_ % 2 -eq 0 })   # 2, 4, 6, 8, 10
```

Y, como cualquier colección, se puede filtrar con un operador de comparación a la derecha
(`$a -gt 5` devuelve los mayores que 5).

Las matrices de PowerShell suelen tener una dimensión, aunque se aniden; las verdaderamente
multidimensionales se indexan con una coma dentro de un único par de corchetes (`$rank2[1,1]`).

### Tablas hash

**«Una tabla hash, también conocida como diccionario o matriz asociativa, es una estructura de datos
compacta que almacena uno o varios pares clave-valor.»** Se escriben entre `@{` y `}`, con `=` entre
clave y valor y `;` o salto de línea entre pares:

```powershell
$hash = @{ Number = 1; Shape = "Square"; Color = "Blue" }
$hash["Time"] = "Now"        # añade una clave
$hash.Add("Time2", "Later")  # también con el método Add()
$hash.Remove("Time")         # la quita
$hash.Keys                   # las claves
$hash.Values                 # los valores
$hash.Count                  # número de pares
```

**«El orden de las claves de una tabla hash no es determinista.»** Para conservar el orden de
escritura existe el diccionario ordenado, `[ordered]@{ … }`, desde PowerShell 3.0; el `[ordered]` va
justo delante de la `@`, y **«Si lo coloca antes del nombre de la variable, se produce un error en el
comando»**. Para quitar un par **«No puede usar un operador de resta»**: se usa `Remove()`.

Las tablas hash aparecen por todas partes en PowerShell: la salida de `$PSVersionTable` y de
`$Matches` lo es; sirven para crear propiedades calculadas y para el *splatting*: **«"Splatting" es un método para pasar una colección de valores de parámetro a
un comando como una unidad.»** Se escribe `@` delante del nombre de la variable en lugar de `$`
(`Invoke-Command @invokeCommandSplat`).

## 6. Strings (cadenas)

### Comillas dobles y comillas simples

Una cadena es texto entre comillas, y en PowerShell las dos clases de comillas no son lo mismo.

*Comillas dobles: cadena expandible.* **«Una cadena entre comillas dobles es una cadena expandible.
Los nombres de variable precedidos por un signo de dólar ($) se reemplazan por el valor de la variable
antes de que la cadena se pase al comando para su procesamiento.»** También se evalúan las
subexpresiones:

```powershell
$i = 5
"The value of $i is $i."        # The value of 5 is 5.
"The value of $(2+3) is 5."     # The value of 5 is 5.
"PS version: $($PSVersionTable.PSVersion)"
```

La tercera línea muestra una regla que se pregunta: **«Solo las referencias de variables básicas se
pueden incrustar directamente en una cadena expandible. Las referencias de variables que usan la
indexación de matriz o el acceso a miembros deben incluirse en una subexpresión.»** Si se escribe
`"Time: $directory.CreationTime"`, PowerShell sustituye sólo `$directory` y deja `.CreationTime` como
texto; hay que escribir `"Time: $($directory.CreationTime)"`. Y cuando el nombre de la variable va
pegado a otro texto, se delimita con llaves: con `$test = "Bet"`, `"${test}ter"` da `Better`.

*Comillas simples: cadena literal.* **«Una cadena entre comillas simples es un cadena textual. La
cadena se pasa al comando exactamente al escribirla. No se realiza ninguna sustitución.»** [sic].

```powershell
'The value of $i is $i.'        # sale tal cual, con $i
'The value of $(2+3) is 5.'     # sale tal cual
```

Por eso las expresiones regulares con `$` (fin de cadena) se escriben entre comillas simples: si se
escriben entre dobles, **«PowerShell interpreta la cadena como una expresión de variable
expandible»**.

### Comillas dentro de una cadena y escape

| Para obtener… | Se escribe |
|---|---|
| Comillas dobles dentro | Toda la cadena entre simples: `'As they say, "live and learn."'`; o dobladas: `"As they say, ""live and learn."""` |
| Comillas simples dentro | Toda la cadena entre dobles, o la simple doblada: `'don''t'` da `don't` |
| Un `$` sin sustituir dentro de comillas dobles | El acento grave delante: ``"The value of `$i is $i."`` da `The value of $i is 5.` |

El acento grave (`` ` ``, en inglés *backtick*) **«es el carácter de escape de PowerShell»**. La
documentación en castellano dice en un punto **«use un carácter de barra diagonal inversa»** para
escapar una comilla doble, pero el ejemplo que pone justo debajo usa el acento grave (`` `" ``): en
PowerShell la barra inversa `\` no es carácter de escape (sí lo es dentro de una expresión regular,
epígrafe 7). PowerShell trata además las comillas tipográficas (“ ” ‘ ’) como comillas normales, y
Microsoft avisa: **«No use comillas inteligentes para incluir cadenas.»**

### Cadenas here

**«Una cadena here-string es una cadena entre comillas simples o dobles rodeada de signos (@). Las
comillas dentro de una cadena aquí se interpretan literalmente.»** La traducción oficial las llama
«cadenas aquí». Una cadena *here*:

- **«abarca varias líneas»**;
- **«comienza con la marca de apertura seguida de una nueva línea»**;
- **«termina con una nueva línea seguida de la marca de cierre»**;
- **«incluye cada línea entre las marcas de apertura y cierre como parte de una sola cadena»**.

```powershell
@"
For help, type "Get-Help"
"@

@'
The $PROFILE variable contains the path
of your PowerShell profile.
'@
```

Con `@"…"@` las variables se sustituyen; con `@'…'@`, no. Sirven para texto con comillas, para
bloques de varias líneas (HTML o XML) y para el texto de ayuda de un script.

### Operaciones con cadenas

Lo que se hace con una cadena, con las herramientas ya vistas:

| Tarea | Cómo |
|---|---|
| Unir | Con `+` (`'Hello, ' + $name`), con `-join` o metiendo las variables en una cadena de comillas dobles |
| Dar formato | Con `-f`: `'Hello, {0} {1}.' -f $first, $last`; en el ejemplo de Microsoft, `"{0:N0}" -f 8175133` da `8,175,133` |
| Partir | Con `-split` |
| Comparar y buscar | Con `-eq`, `-like`, `-match` (sin distinguir mayúsculas salvo con `-c…`) |
| Sustituir | Con el operador `-replace` (expresión regular) o con el método `Replace()` (texto literal): `'this is rocket science'.Replace('rocket', 'rock')` |
| Longitud | Con la propiedad `Length`, que **«para una cadena es el número de caracteres de la cadena»** |
| Otros métodos | Los de la clase `System.String` de .NET, que lista `'texto' \| Get-Member -MemberType Method` |
| Construir rutas | `Join-Path -Path 'C:\windows' -ChildPath $folder`, que pone bien las barras |

Una cadena no se modifica: cada concatenación crea otra nueva. La guía de Microsoft lo explica con un
bucle que añade diez mil números a una cadena: **«cada vez que se agrega una cadena a $message que se
crea una nueva cadena completa. La memoria se asigna, los datos se copian y se descarta el
anterior.»** [sic]. Para cadenas muy grandes propone la clase .NET `System.Text.StringBuilder`.

## 7. Metacaracteres

Tres juegos de caracteres especiales conviven en PowerShell y no deben confundirse: los comodines
(para nombres de fichero y `-like`), las secuencias de escape con acento grave (dentro de cadenas
entre comillas dobles) y los metacaracteres de las expresiones regulares (para `-match`, `-replace`,
`-split`, `switch -Regex` y `Select-String`).

### Comodines

**«Las expresiones comodín se usan con el operador -like o con cualquier parámetro que acepte
caracteres comodín.»** y **«Las expresiones comodín son más sencillas que las expresiones
regulares.»**

| Comodín | Significa | Ejemplo de Microsoft |
|---|---|---|
| `*` | **«coincidencia con cero o más caracteres»** | `a*` coincide con *aA*, *ag* y *Apple*, no con *banana* |
| `?` en cadenas | **«coincida con un carácter en esa posición»** | `?n` coincide con *an*, *in* y *on*, no con *ran* |
| `?` en ficheros y carpetas | **«coincida con cero o un carácter en esa posición»** | `?.txt` coincide con *a.txt*, no con *ab.txt* |
| `[a-l]` | **«coincidencia de un intervalo de caracteres»** | `[a-l]ook` coincide con *book*, *cook* y *look*, no con *took* |
| `[bc]` | **«coincidencia de caracteres específicos»** | `[bc]ook` coincide con *book* y *cook*, no con *hook* |
| `` `* `` | **«coincide con cualquier carácter como literal (no comodín)»** | ``12`*4`` coincide con *12\*4*, no con *1234* |

**«Para los parámetros que aceptan caracteres comodín, su uso no distingue mayúsculas de
minúsculas.»** Se combinan: `Get-ChildItem C:\Techdocs\[a-l]*.txt` lista los `.txt` que empiezan por
una letra de la *a* a la *l*. Si un nombre de fichero contiene corchetes, el parámetro `-LiteralPath`
evita que se lean como comodines: **«El valor de LiteralPath se usa exactamente tal como está escrito.
Ninguno de los caracteres se interpreta como caracteres comodín.»**

### El acento grave y las secuencias de escape

**«Las secuencias de escape comienzan con el carácter de retroceso, conocido como énfasis grave (ASCII
96) y distinguen mayúsculas de minúsculas.»** y **«Las secuencias de escape solo se interpretan
cuando se encuentran en cadenas entre comillas dobles (").»**

| Secuencia | Carácter |
|---|---|
| `` `0 `` | Nulo |
| `` `a `` | Alerta (pitido) |
| `` `b `` | Retroceso |
| `` `e `` | Escape (desde PowerShell 6) |
| `` `f `` | Avance de página (Microsoft traduce **«Fuente de formularios»** [sic]) |
| `` `n `` | Nueva línea |
| `` `r `` | Retorno de carro |
| `` `t `` | Tabulación horizontal (Microsoft: **«Pestaña Horizontal»** [sic]) |
| `` `u{x} `` | Carácter Unicode por su código (desde PowerShell 6) |
| `` `v `` | Tabulación vertical |

El nulo `` `0 `` **«no es equivalente a la variable $null»**. Hay además dos fichas de análisis: `--`,
**«Tratar los valores restantes como argumentos no parámetros»**, y `--%`, **«Dejar de analizar todo
lo que sigue»**, útil para pasar a un programa nativo una línea que PowerShell interpretaría.

El acento grave al final de una línea sirve para continuar la orden en la siguiente, pero Microsoft lo
desaconseja: **«El uso del acento grave (`) como carácter de continuación de línea es un tema
controvertido. Es mejor evitarlo si es posible.»** Una línea larga se puede partir sin él después de
una tubería, y **«PowerShell 7 agrega soporte para la continuación de las canalizaciones con el
símbolo de tubería al principio de una línea.»**

### Expresiones regulares

**«Una expresión regular es un patrón que se usa para hacer coincidir el texto. Se puede componer de
caracteres literales, operadores y otras construcciones. PowerShell usa el motor de regex de .NET.»**
Las usan **«Select-String»**, **«operadores -match y -replace»**, **«operador -split»** y la
**«declaración switch con la opción -regex»**. **«Las expresiones regulares de PowerShell no
distinguen mayúsculas de minúsculas de forma predeterminada.»**

| Metacarácter | Significa |
|---|---|
| `.` | **«Coincide con cualquier carácter excepto una nueva línea (\n).»** |
| `[iou]` / `[^iou]` | Cualquiera de esos caracteres / cualquiera salvo esos |
| `[0-9]`, `[A-Z]` | Un carácter del intervalo |
| `\d` / `\D` | **«coincide con cualquier dígito decimal»** / cualquier carácter que no lo sea |
| `\w` / `\W` | **«coincide con cualquier carácter de palabra [a-zA-Z_0-9]»** / lo contrario |
| `\s` / `\S` | Un espacio en blanco / cualquier carácter que no lo sea |
| `*` | **«Cero o más veces.»** |
| `+` | **«Una o varias veces.»** |
| `?` | **«Cero o una vez.»** |
| `{n}`, `{n,}`, `{n,m}` | Exactamente *n* veces, al menos *n*, entre *n* y *m* |
| `^` y `$` | **«El símbolo de acento circunflejo ^ coincide con el inicio de una cadena y $, que corresponde al final de una cadena.»** |
| `\` | **«La barra diagonal inversa (\) se usa para caracteres de escape»** |

Los caracteres reservados, que hay que escapar con `\` para buscarlos literalmente, son, según la
documentación, **«[().\^$|?*+{»**; `[regex]::Escape()` los escapa todos de una vez. Ejemplos de la
documentación: `'big' -match 'b[iou]g'` es verdadero; `42 -match '[0-9][0-9]'` también;
`'PowerShell' -match '^Power\w+'` también.

Comodín y expresión regular usan algunos signos iguales con significado distinto: en un comodín `*`
es «cualquier cosa»; en una expresión regular, «el elemento anterior cero o más veces», y
«cualquier cosa» se escribe `.*`. El `?` de un comodín es un carácter; en una expresión regular hace
opcional el anterior.

## 8. Tuberías

### Qué es una canalización

**«Una tubería es una serie de comandos conectados por operadores de tubería (|) (ASCII 124). Cada
operador de canalización envía los resultados del comando anterior al siguiente comando.»** La
documentación en castellano dice indistintamente tubería y canalización (*pipeline*).

```powershell
Get-ChildItem -Path *.txt |
  Where-Object {$_.Length -gt 10000} |
  Sort-Object -Property Length |
  Format-Table -Property Name, Length
```

El ejemplo es de Microsoft: obtiene los `.txt` del directorio, se queda con los de más de 10 000
bytes, los ordena por tamaño y muestra nombre y longitud en una tabla. **«En una canalización, los
comandos se procesan en orden de izquierda a derecha. El procesamiento se controla como una sola
operación y la salida se muestra a medida que se genera.»** Lo que circula son objetos, no texto:
`Get-Process notepad | Stop-Process` funciona porque `Stop-Process` recibe el objeto proceso entero.

### Uno a uno

**«Al canalizar varios objetos a un comando, PowerShell envía los objetos al comando uno a uno.
Cuando se usa un parámetro de comando, los objetos se envían como un único objeto de matriz.»** Las
matrices y demás colecciones se desenrollan al entrar en la tubería; dos excepciones: las tablas hash
(hay que llamar a su método `GetEnumerator()`) y las cadenas, que no se enumeran carácter a carácter.
El ejemplo oficial: `@(1,2,3) | Measure-Object` cuenta 3; `@{"One"=1;"Two"=2} | Measure-Object`
cuenta 1.

Dentro de la canalización, el objeto que está pasando se llama `$_` (o `$PSItem`). Lo usan los
bloques de script de `Where-Object` y `ForEach-Object`.

### Cómo recibe el comando el objeto: ByValue y ByPropertyName

**«Para admitir la canalización, el cmdlet receptor debe tener un parámetro que acepte la entrada de
canalización.»** Hay dos maneras de aceptarla:

- **«ByValue: el parámetro acepta valores que coinciden con el tipo de .NET esperado o que se pueden
  convertir a ese tipo.»**
- **«ByPropertyName: el parámetro acepta la entrada solo cuando el objeto de entrada tiene una
  propiedad del mismo nombre que el parámetro .»** [sic]

El ejemplo es `Start-Service`: su parámetro `InputObject` acepta objetos servicio y su parámetro
`Name`, cadenas o cualquier objeto con una propiedad `Name`. Qué parámetros aceptan entrada por
tubería, y de qué modo, lo dice la ayuda completa (`Get-Help Start-Service -Full`, línea «Accept
pipeline input?»). Si PowerShell no logra enlazar el objeto, el comando falla: **«No puede sugerir ni
forzar que PowerShell se enlace a un parámetro específico.»**

### Los cmdlets de la tubería

**«Muchos de los cmdlets de utilidades, como Get-Member, Where-Object, Sort-Object, Group-Object y
Measure-Object, se usan casi exclusivamente en canalizaciones.»**

| Cmdlet | Alias | Qué hace |
|---|---|---|
| `Where-Object` | `?`, `where` | **«Selecciona objetos de una colección en función de sus valores de propiedad.»** |
| `ForEach-Object` | `%`, `foreach` | **«Realiza una operación en cada elemento de una colección de objetos de entrada.»** |
| `Select-Object` | `select` | **«Selecciona objetos o propiedades de objeto.»** (`-Property`, `-First`, `-Last`, `-Unique`) |
| `Sort-Object` | `sort` (sólo Windows) | **«Ordena los objetos por valores de propiedad.»** (`-Descending`, `-Unique`) |
| `Measure-Object` | `measure` | **«Calcula las propiedades numéricas de objetos y los caracteres, palabras y líneas en objetos de cadena (como archivos de texto).»** (cuenta, suma, media, máximo, mínimo) |
| `Group-Object` | `group` | **«Agrupa objetos que contienen el mismo valor para las propiedades especificadas.»** |
| `Format-Table`, `Format-List` | `ft` (el de `Format-List` no se ha leído) | Dan formato para la pantalla: **«Da formato a la salida como una tabla.»**; `Format-List`, como lista de propiedades |
| `Export-Csv` | `epcsv` | **«crea un archivo CSV de los objetos que envía»** |
| `Out-File`, `Tee-Object` | `tee` (sólo Windows), para `Tee-Object` | Envían a fichero (epígrafe 9) |

`Where-Object` y `ForEach-Object` admiten dos sintaxis desde Windows PowerShell 3.0, la de bloque de
script y la simplificada:

```powershell
Get-Process | Where-Object {$_.PriorityClass -eq "Normal"}   # bloque de script
Get-Process | Where-Object PriorityClass -EQ Normal          # simplificada
Get-Process | ForEach-Object {$_.ProcessName}
Get-Process | ForEach-Object ProcessName
```

### Buenas prácticas de la documentación

- *Filtrar a la izquierda.* **«Es un procedimiento recomendado en PowerShell filtrar los resultados
  lo antes posible en la canalización.»** `Get-Service -Name w32time` es mejor que `Get-Service |
  Where-Object Name -EQ w32time`, porque el segundo trae todos los servicios para quedarse con uno.
  Por la misma razón, en `Get-ChildItem` **«Los filtros son más eficaces que otros parámetros»**.
- *El orden cuenta.* Si `Select-Object` deja fuera una propiedad, un `Where-Object` posterior ya no
  puede filtrar por ella.
- *No dar formato antes de exportar.* **«No formatee los objetos antes de Export-Csv enviarlos al
  cmdlet. Si Export-Csv recibe objetos formateados, el archivo CSV contiene las propiedades de formato
  en lugar de las propiedades del objeto.»** [sic]. `Format-Table` y `Format-List` van al final.

La tubería también recibe la salida de programas nativos, como texto: `ipconfig.exe | Select-String
-Pattern 'IPv4'`. Y no tiene entrada estándar: **«stdin no está conectado a la canalización de
PowerShell para recibir entradas»**.

## 9. Direccionamiento (redirección de la salida)

### Los flujos de salida

**«De forma predeterminada, PowerShell envía la salida al host de PowerShell. Normalmente se trata de
la aplicación de consola.»** La salida de un comando no es una sola: PowerShell tiene varios flujos
numerados, y cada uno puede redirigirse por su número.

| N.º | Flujo | Cmdlet que escribe en él | Desde |
|---|---|---|---|
| 1 | Éxito (*Success*) | `Write-Output` | PowerShell 2.0 |
| 2 | Error | `Write-Error` | PowerShell 2.0 |
| 3 | Advertencia (*Warning*) | `Write-Warning` | PowerShell 3.0 |
| 4 | Detallado (*Verbose*) | `Write-Verbose` | PowerShell 3.0 |
| 5 | Depuración (*Debug*) | `Write-Debug` | PowerShell 3.0 |
| 6 | Información | `Write-Information`, `Write-Host` | PowerShell 5.0 |
| `*` | Todos | — | PowerShell 3.0 |

**«También hay un flujo Progress en PowerShell, pero no admite el redireccionamiento.»** Los flujos 1
y 2 **«son similares a los flujos stdout y stderr de otros shells»**.

### Los operadores

| Operador | Qué hace |
|---|---|
| `>` (o `n>`) | **«Envíe una secuencia especificada a un archivo.»** [sic]; sobrescribe |
| `>>` (o `n>>`) | **«Añade el transmisión especificado a un archivo.»** [sic]; añade al final |
| `n>&1` | **«Redirige la transmisión especificada a la transmisión de éxito.»** |

**«La transmisión Éxito ( 1 ) es el predeterminado si no se especifica ningún transmisión.»** [sic]:
`>` a secas equivale a `1>`. Y una limitación frente a Unix: **«solo puede redirigir otros flujos a la
transmisión de Éxito.»** Los ejemplos de la documentación:

```powershell
dir C:\, fakepath 2>&1 > .\dir.log   # errores al flujo de éxito y todo al fichero
.\script.ps1 > script.log            # sólo la salida normal
.\script.ps1 *> script.log           # todos los flujos
&{ Write-Warning "hello"; Write-Error "hello"; Write-Output "hi" } 3>&1 2>&1 > C:\Temp\redirection.log
```

Para descartar una salida se redirige a `$null` (el ejemplo oficial suprime el flujo de información
con `6> $null`).

### Out-File y Tee-Object

**«Redirigir la salida de un comando de PowerShell (cmdlet, función, script) mediante el operador de
redirección (>) es funcionalmente equivalente a canalizar a Out-File sin parámetros adicionales.»**
`Out-File` se usa cuando hacen falta sus parámetros, **«como los parámetros Encoding, Force, Widtho
NoClobber»** [sic]: `-Append` añade, `-NoClobber` impide sobrescribir un fichero que ya existe
(**«De forma predeterminada, Out-File sobrescribe los archivos existentes.»**) y `-Encoding` cambia
la codificación. `Tee-Object` **«envía la salida del comando a un archivo de texto y, a continuación,
lo envía a la canalización»**: guarda y deja seguir (también puede guardar en una variable: **«Guarda
la salida del comando en un archivo o variable y también la envía a la canalización.»**).

La codificación por defecto en PowerShell 7 es UTF-8 sin BOM: **«Al escribir en archivos, los
operadores de redireccionamiento usan la codificación UTF8NoBOM.»** Y lo que se guarda es lo que se
vería en pantalla: Out-File **«Usa implícitamente el sistema de formato de PowerShell para escribir en
el archivo. El archivo recibe la misma representación de presentación que el terminal.»**, con el
ancho de la consola; **«Esto significa que la salida puede no ser ideal para el procesamiento mediante
programación a menos que todos los objetos de entrada sean cadenas.»** Para datos que otro programa
vaya a leer, `Export-Csv` guarda las propiedades de los objetos.

**«PowerShell 7.4 cambió el comportamiento de los operadores de redirección cuando se utilizan para
redirigir el flujo stdout de un comando nativo.»**: desde esa versión conservan los bytes tal cual
salen del programa nativo.

## 10. Estructuras de control

Todas siguen el mismo patrón: una palabra clave, una condición entre paréntesis y un bloque de
instrucciones entre llaves. La condición se convierte a valor lógico con las reglas del epígrafe 4
(cero, cadena vacía y `$null` son falsos), y dentro se compara con `-eq`, `-lt`, etc.

### if, elseif, else

**«Puede usar la instrucción if para ejecutar bloques de código si una prueba condicional especificada
se evalúa como true. También puede especificar una o varias pruebas condicionales adicionales para
ejecutarse si todas las pruebas anteriores resultan falsas.»**

```powershell
if ($a -gt 2) {
    Write-Host "The value $a is greater than 2."
}
elseif ($a -eq 2) {
    Write-Host "The value $a is equal to 2."
}
else {
    Write-Host "The value $a is less than 2 or was not created or initialized."
}
```

Se ejecuta el primer bloque cuya condición sea verdadera y se sale; `else` recoge el resto. **«Si
necesita crear una instrucción if que contenga muchas instrucciones elseif, considere la posibilidad
de usar una instrucción switch en su lugar.»** En PowerShell 7 hay además el operador ternario
(epígrafe 4).

### switch

**«La switch instrucción es similar a una serie de if instrucciones, pero es más sencilla.»** [sic].

```powershell
switch (3) {
    1 { "It's one." }
    2 { "It's two." }
    3 { "It's three." }
    4 { "It's four." }
    3 { "Three again." }
}
```

Este ejemplo oficial devuelve las dos líneas `It's three.` y `Three again.`: a diferencia de otros
lenguajes, `switch` prueba todas las condiciones y ejecuta todas las que coinciden. Para pararlo:
**«La palabra clave break detiene el procesamiento y sale de la instrucción switch.»** y **«La palabra
clave continue detiene el procesamiento del valor actual, pero continúa procesando los valores
posteriores.»** Otras reglas:

- **«La switch instrucción convierte todos los valores en cadenas antes de la comparación.»**
- Si el valor de prueba es una colección, se evalúa cada elemento por separado; dentro, el valor que
  se está probando es `$_`.
- **«La cláusula default se desencadena cuando el valor no coincide con ninguna de las condiciones. Es
  equivalente a una cláusula else en una instrucción if.»** Sólo puede haber una.
- Sin parámetros, la comparación es exacta y sin distinguir mayúsculas. Los parámetros cambian el
  modo: `-Wildcard` (comodines), `-Regex` (expresiones regulares; deja disponible `$Matches`),
  `-Exact`, `-CaseSensitive` y `-File`, que **«toma la entrada de un archivo en lugar de un
  <test-expression>. El archivo se lee una línea a la vez y se evalúa mediante la instrucción
  switch.»**

### for

**«La instrucción for (también conocida como bucle for) es una construcción de lenguaje que puede usar
para crear un bucle que ejecute comandos en un bloque de comandos mientras una condición especificada
se evalúa como $true.»**

```powershell
for (<Init>; <Condition>; <Repeat>) { <Statement list> }

$a = 0..9
for ($i = 0; $i -le ($a.Length - 1); $i += 2) {
    $a[$i]          # 0, 2, 4, 6, 8
}
```

`Init` se ejecuta una vez antes de empezar; `Condition` se evalúa antes de cada vuelta; `Repeat`, al
final de cada vuelta. Es el bucle para recorrer con contador; **«si desea iterar todos los valores de
una matriz, considere la posibilidad de usar una instrucción foreach»**.

### foreach

**«La instrucción foreach es una construcción de lenguaje para recorrer en iteración un conjunto de
valores de una colección.»**

```powershell
foreach ($file in Get-ChildItem) {
    if ($file.Length -gt 100KB) {
        Write-Host $file
    }
}
```

**«PowerShell crea la variable $<item> automáticamente cuando se ejecuta el bucle foreach. Al
principio de cada iteración, foreach establece la variable de elemento en el siguiente valor de la
colección.»** No hay que confundir la instrucción `foreach (… in …)` con el cmdlet `ForEach-Object`,
que trabaja dentro de una tubería con `$_`, aunque `foreach` sea también alias de ese cmdlet; a la
instrucción **«no se puede canalizar la entrada»**. Si la
palabra va al principio de una instrucción con paréntesis e `in`, es la instrucción; si va detrás de
un `|`, es el alias del cmdlet.

### while

**«La while instrucción (también conocida como while bucle) es una construcción de lenguaje para crear
un bucle que ejecuta comandos en un bloque de comandos siempre que una prueba condicional se evalúe
como true.»** [sic]. La condición se evalúa antes de entrar, así que el bloque puede no ejecutarse
nunca.

```powershell
while($val -ne 3)
{
    $val++
    Write-Host $val      # 1, 2, 3 (con $val sin crear o a 0)
}
```

### do-while y do-until

**«A diferencia del bucle relacionado while , el bloque de instrucciones de un do bucle siempre se
ejecuta al menos una vez.»** [sic]. Hay dos formas, según cómo se lea la condición:

| Forma | Se repite mientras la condición sea… |
|---|---|
| `do { … } while (<condición>)` | Verdadera |
| `do { … } until (<condición>)` | Falsa: **«el bloque de instrucciones solo se ejecuta mientras la condición es false»** |

Los dos ejemplos oficiales cuentan lo mismo cambiando `-ne` por `-eq`:

```powershell
$x = 1,2,78,0
do { $count++; $a++; } while ($x[$a] -ne 0)
do { $count++; $a++; } until ($x[$a] -eq 0)
```

### break y continue

**«La instrucción break proporciona una manera de salir del bloque de control actual.»**; en un bucle
**«PowerShell sale inmediatamente del bucle»**. **«Una instrucción continue sin etiquetar devuelve
inmediatamente el flujo del programa a la parte superior del bucle más interno»**: termina la vuelta
actual y pasa a la siguiente. En un `for`, tras `continue` se ejecuta la parte `Repeat` y después se
evalúa la condición.

```powershell
while ($ctr -lt 10) {
    $ctr += 1
    if ($ctr -eq 5) { continue }
    Write-Host -Object $ctr      # del 1 al 10, salvo el 5
}
```

Los dos admiten etiquetas para salir de bucles anidados: la etiqueta es dos puntos y un nombre
delante del bucle (`:myLabel while (…) { … break myLabel … }`).

### try, catch, finally

Para tratar errores: **«Use trybloques , catchy finally para responder o controlar errores de
terminación en scripts.»** [sic].

```powershell
try   { <instrucciones que se vigilan> }
catch [<tipo de error>] { <qué hacer si fallan> }
finally { <lo que se ejecuta siempre> }
```

**«Una instrucción try debe tener al menos un bloque catch o un bloque finally.»** Un `catch` sin tipo
recoge cualquier error; puede haber varios para tipos distintos. **«Dentro de un catch bloque, se puede acceder al error actual mediante la $_ variable o $PSItem
automática. El objeto es de tipo ErrorRecord.»** [sic]. **«Un bloque finally se puede usar para liberar los recursos que ya no necesite el
script.»**, y se ejecuta haya error o no.

`try/catch` sólo captura errores de terminación. Muchos errores de cmdlet no lo son (el cmdlet avisa y
sigue); para capturarlos se cambia la preferencia de error a `Stop`, en la variable
`$ErrorActionPreference` o en el parámetro `-ErrorAction` del cmdlet. Con `Stop`, el cmdlet
**«muestra el mensaje de error y deja de ejecutarse»**. El ejemplo de la documentación de la
redirección lo enseña: con `$ErrorActionPreference = 'Stop'`, un `Get-Item /not-here` dentro de `try`
salta al `catch`. El valor por defecto de la preferencia es `Continue`, que muestra el error y sigue.

Para devolver un código de error desde un script se usa `exit`: **«De forma predeterminada, la
instrucción exit devuelve 0. Puede proporcionar un valor numérico para devolver un estado de salida
diferente. Normalmente, un código de salida distinto de cero indica un error.»** Ese valor queda en
`$LASTEXITCODE`.

## 11. Gestión de ficheros

### Los cmdlets de elementos

PowerShell no tiene un juego de órdenes sólo para ficheros: usa los cmdlets de elementos (*Item*),
que valen para cualquier proveedor (epígrafe 1), y los de contenido (*Content*). Con el proveedor
FileSystem, un elemento es un fichero o una carpeta.

| Tarea | Cmdlet | Alias (todas las plataformas / sólo Windows) | Qué dice Microsoft |
|---|---|---|---|
| Listar | `Get-ChildItem` | `dir`, `gci` / `ls` | **«Obtiene los elementos y elementos secundarios de una o varias ubicaciones especificadas.»** |
| Cambiar de carpeta | `Set-Location` | `cd`, `chdir`, `sl` | — |
| Crear | `New-Item` | `ni` | **«Crea un nuevo elemento.»** |
| Copiar | `Copy-Item` | `copy`, `cpi` / `cp` | **«Este cmdlet no corta ni elimina los elementos que se copian.»** |
| Mover | `Move-Item` | `mi`, `move` / `mv` | **«Al mover un elemento, se agrega a la nueva ubicación y se elimina de su ubicación original.»** |
| Renombrar | `Rename-Item` | `ren`, `rni` | **«Este cmdlet no afecta al contenido del elemento al que se va a cambiar el nombre.»** |
| Borrar | `Remove-Item` | `del`, `erase`, `rd`, `ri` / `rm` | **«Elimina los elementos especificados.»** |
| Comprobar que existe | `Test-Path` | — | **«Devuelve $true si todos los elementos existen y $false si falta alguno.»** |
| Leer | `Get-Content` | `gc`, `type` / `cat` | — |
| Escribir (reemplaza) | `Set-Content` | — | **«Escribe contenido nuevo o reemplaza el contenido existente en un archivo.»** |
| Añadir | `Add-Content` | `ac` (Windows) | **«anexa contenido a un elemento o archivo especificados»** |
| Buscar texto | `Select-String` | `sls` | **«Puede usar Select-String de forma similar a grep en Unix o findstr.exe en Windows.»** |

### Listar: Get-ChildItem

```powershell
Get-ChildItem -Path C:\ -Force              # incluidos ocultos y de sistema
Get-ChildItem -Path C:\ -Force -Recurse     # con todas las subcarpetas
Get-ChildItem -Path C:\Datos -File          # sólo ficheros
Get-ChildItem -Path C:\Datos -Directory     # sólo carpetas
Get-ChildItem -Path C:\Datos -Filter *.log -Recurse -Depth 2
```

`-Force` muestra **«elementos ocultos o del sistema»**; `-Recurse` baja por todas las subcarpetas y
`-Depth` limita los niveles (se añadió en PowerShell 5.0). Se filtra por nombre con `-Path`,
`-Filter`, `-Include` y `-Exclude`; `-Filter` es el más rápido porque **«El proveedor aplica el
filtro cuando el cmdlet obtiene los objetos en lugar de que PowerShell filtre los objetos una vez
recuperados.»**. Para filtrar por otras propiedades (fecha, tamaño) se canaliza a `Where-Object`. El
ejemplo de la documentación busca los ejecutables de Archivos de programa modificados tras el
1-10-2005 y de entre 1 y 10 MB:

```powershell
Get-ChildItem -Path $env:ProgramFiles -Recurse -Include *.exe |
  Where-Object -FilterScript {
    ($_.LastWriteTime -gt '2005-10-01') -and ($_.Length -ge 1mb) -and ($_.Length -le 10mb)
  }
```

### Crear, copiar, mover, renombrar

```powershell
New-Item -Path 'C:\temp\New Folder' -ItemType Directory
New-Item -Path 'C:\temp\New Folder\file.txt' -ItemType File
Copy-Item -Path $PROFILE -Destination $($PROFILE -replace 'ps1$', 'bak')
Copy-Item C:\temp\test1 -Recurse C:\temp\DeleteMe
Copy-Item -Filter *.txt -Path c:\data -Recurse -Destination C:\temp\text
Move-Item -Path .\informe.txt -Destination D:\Archivo\
Rename-Item -Path .\informe.txt -NewName informe-2026.txt
```

Lo que distingue a cada uno:

- *New-Item* necesita `-ItemType` (`Directory` o `File`) en el sistema de ficheros, porque el
  proveedor tiene dos clases de elemento. Con `-Force`, sobre una carpeta que ya existe **«no
  sobrescribirá ni reemplazará la carpeta. Simplemente devolverá el objeto de carpeta existente. Sin
  embargo, si usa New-Item -Force en un archivo que ya existe, el archivo se sobrescribe.»**
- *Copy-Item* falla si el destino existe, salvo con `-Force`, que **«funciona aunque el destino sea
  de solo lectura»**; para copiar una carpeta con su contenido hace falta `-Recurse`. Puede copiar y
  renombrar en la misma orden, dando el nombre nuevo en `-Destination`.
- *Move-Item* mueve **«incluidas sus propiedades, contenido y elementos secundarios»**, y por eso
  **«todos los movimientos son recursivos de forma predeterminada»**. Mueve ficheros entre unidades
  del mismo proveedor, pero **«solo moverá directorios dentro de la misma unidad»**. Si el nombre de
  destino ya existe, falla salvo con `-Force`.
- *Rename-Item* sólo cambia el nombre: **«No puede usar Rename-Item para mover un elemento»**, y
  **«No se puede usar Rename-Item para reemplazar un elemento existente»**; para ambas cosas se usa
  `Move-Item` (con `-Force` si hay que reemplazar).

### Borrar

```powershell
Remove-Item -Path C:\temp\DeleteMe              # pide confirmación si tiene contenido
Remove-Item -Path C:\temp\DeleteMe -Recurse     # sin preguntar por cada elemento
Remove-Item -Path C:\temp\*.tmp -WhatIf         # sólo dice qué borraría
```

**«Los elementos contenidos se pueden quitar mediante Remove-Item, pero se pedirá que se confirme la
eliminación si el elemento contiene algo más.»** `-Force` **«Obliga al cmdlet a quitar elementos que,
de lo contrario, no se pueden cambiar, como archivos ocultos o de solo lectura»**. Antes de un borrado
masivo, `-WhatIf` enseña la lista sin borrar nada.

### Leer y escribir contenido

`Get-Content` lee un fichero de texto y **«devuelve una colección de objetos, cada uno de los cuales
representa una línea de contenido»**. Así, `(Get-Content -Path $PROFILE).Length` es el número de
líneas, y una lista de equipos guardada en un fichero, uno por línea, se convierte en una matriz:

```powershell
$Computers = Get-Content -Path C:\temp\DomainMembers.txt
Get-Content -Path .\app.log -TotalCount 10    # las 10 primeras líneas
Get-Content -Path .\app.log -Tail 20          # las 20 últimas
Get-Content -Path .\app.log -Wait            # sigue el fichero mientras crece
Get-Content -Path .\config.json -Raw          # todo en una sola cadena
```

`-Tail` (alias `Last`) da **«el número de líneas del final de un archivo»**; `-Wait` **«comprueba el
archivo una vez por segundo y genera nuevas líneas si están presentes»**; `-Raw` devuelve el contenido
entero en una cadena.

Para escribir: **«Set-Content reemplaza el contenido existente y difiere del cmdlet Add-Content que
anexa contenido a un archivo.»** Los dos aceptan el texto por `-Value` o por tubería.

```powershell
Set-Content -Path .\equipos.txt -Value "PC01"
Add-Content -Path .\equipos.txt -Value "PC02"
Get-Service | Export-Csv -Path .\servicios.csv
```

`Out-File` y `>` también escriben, pero lo que guardan es la vista de pantalla (epígrafe 9); `Set-Content`
escribe cadenas; `Export-Csv` escribe los objetos como filas de valores separados.

### Buscar dentro de ficheros

`Select-String` **«usa la coincidencia de expresiones regulares para buscar patrones de texto en
cadenas y archivos de entrada»**; por cada coincidencia **«muestra el nombre del archivo, el número de
línea y todo el texto de la línea que contiene la coincidencia»**.

```powershell
Select-String -Path C:\Logs\*.log -Pattern 'error'
ipconfig.exe | Select-String -Pattern 'IPv4'
```

### Unidades y rutas

`New-PSDrive` crea una unidad de PowerShell sobre una carpeta: **«El siguiente comando crea una unidad
local P: con raíz en el directorio local Archivos de programa, visible solo desde la sesión de
PowerShell»** (`New-PSDrive -Name P -Root $env:ProgramFiles -PSProvider FileSystem`). Para que se vea
en el Explorador de archivos se usa `-Persist`, que sólo admite rutas remotas. `Join-Path` construye
rutas sin preocuparse de las barras, y `Test-Path` comprueba que existen antes de usarlas.

### Aplicación práctica: un script de mantenimiento

El script siguiente es un ejemplo propio de este tema, construido sólo con lo explicado y no
ejecutado: borra de una carpeta los `.log` de más de *N* días y deja constancia. Reúne casi todas las
rúbricas del enunciado.

```powershell
# Limpieza-Logs.ps1 — borra los .log antiguos de una carpeta
param ($Ruta = 'C:\Logs', $Dias = 30)                 # parámetros con valor por defecto

$limite = (Get-Date).AddDays(-$Dias)                  # variable con un objeto fecha
$log    = Join-Path $Ruta 'limpieza.txt'
$err    = Join-Path $Ruta 'errores.txt'
if (-not (Test-Path -Path $Ruta)) {                   # operador lógico y estructura if
    Write-Warning "No existe la carpeta $Ruta"        # flujo 3, advertencia
    exit 1                                            # código de salida distinto de cero
}

$viejos = @(Get-ChildItem -Path $Ruta -Filter *.log -File -Recurse |   # tubería
            Where-Object { $_.LastWriteTime -lt $limite })             # $_ y -lt

foreach ($f in $viejos) {                             # bucle sobre la matriz
    try {
        Remove-Item -Path $f.FullName -ErrorAction Stop
        "Borrado: $($f.FullName)" >> $log             # subexpresión y >>
    }
    catch {
        "Error en $($f.FullName): $_" >> $err         # $_ es el error capturado
    }
}
"Ficheros tratados: $($viejos.Count)"                 # cadena expandible y Count
```

Puntos que un tribunal podría preguntar sobre él: `@( )` garantiza que `$viejos.Count` funcione
aunque haya un solo fichero o ninguno; `-ErrorAction Stop` hace que un fallo de `Remove-Item` llegue al
`catch`; `>>` añade al registro en lugar de sobrescribirlo; el script sólo correrá en un Windows
recién instalado si se cambia antes la directiva de ejecución (Restricted por defecto en los
clientes); y para probarlo sin riesgo basta añadir `-WhatIf` a `Remove-Item` (no borra nada, aunque
el registro anotaría igualmente «Borrado»).

## Lo que este tema no da, y dónde está

- La administración de Windows 11 (directivas de grupo, puntos de restauración, seguridad) y la de
  Windows Server y Active Directory, aunque muchas de sus tareas se hagan con PowerShell: temas 6 y 8.
  Los cmdlets de módulos concretos (Active Directory, Hyper-V, Microsoft 365) no se tratan.
- El shell de Linux (bash), `grep`, `sed` y `awk`: tema 9. La correspondencia con `Select-String` y
  `-replace` se apunta en los epígrafes 7 y 11.
- La firma de scripts con certificados (Authenticode) y la administración de certificados: tema 14.
  Aquí sólo se dice qué exige cada directiva de ejecución.
- Las funciones avanzadas, los módulos, las clases, la administración remota (`Enter-PSSession`,
  `Invoke-Command` más allá de su mención), los trabajos en segundo plano y Desired State
  Configuration: el enunciado no los pide y no se desarrollan.
- La directiva de ejecución que rige por defecto en Windows con PowerShell 7: la página de Microsoft
  se contradice (RemoteSigned en un pasaje, Restricted en otros dos); el tema da la de Windows
  PowerShell 5.1, que es clara.
- Qué versión de PowerShell, qué directiva de ejecución o qué scripts se usan en los equipos de la
  RTVA y de CSRTV: no consta en ningún documento publicado.

## Trazabilidad

Todas las páginas son de Microsoft Learn en castellano (learn.microsoft.com/es-es/powershell/…),
versión PowerShell 7.x salvo donde se indica, leídas el 05-10-2026.

| Fuente | Qué sostiene |
|---|---|
| «¿Qué es PowerShell?» (scripting/overview) | Definición, objetos .NET, CLR, características del shell y del lenguaje, DSC, módulos |
| «Ciclo de vida de soporte técnico de PowerShell» (scripting/install/powershell-support-lifecycle) | Versiones LTS y estable, tabla de fechas y versiones de .NET, Windows PowerShell 5.1 (agosto de 2016, WMF 5.1), soporte de 5.1 |
| «Diferencias entre Windows PowerShell 5.1 y PowerShell 7.x» (scripting/whats-new/differences-from-windows-powershell) | .NET Framework 4.5 frente a .NET Core, `pwsh.exe`, módulos que ya no se incluyen |
| «Instalación de PowerShell 7 en Windows» (scripting/install/install-powershell-on-windows) | Instalación en paralelo, métodos (WinGet, MSI, MSIX, ZIP, .NET), órdenes `winget` |
| «Uso de Visual Studio Code para el desarrollo de PowerShell» (scripting/dev-cross-plat/vscode/using-vscode) | Editor recomendado; estado del ISE |
| *PowerShell 101*, cap. 1 «Introducción a PowerShell», cap. 2 «El sistema de ayuda», cap. 4 «Canalización» (scripting/learn/ps101/…) | Windows PowerShell preinstalado, Terminal Windows, UAC y elevación, `$PSVersionTable`; cmdlets y Verbo-Sustantivo, `Get-Help` y sus parámetros, `help`, búsqueda, `Update-Help`, `Save-Help`, `Get-Command`; filtrar a la izquierda, continuación de línea |
| `about_Aliases`, `about_Scripts`, `about_Comments`, `about_Providers`, `about_Profiles`, `about_Scopes` | Alias, scripts y su ejecución, `param`, `exit`, comentarios, proveedores y unidades, perfiles, ámbitos |
| `about_Execution_Policies` (versiones 7 y 5.1) y `Set-ExecutionPolicy` | Directivas, valores por defecto, ámbitos y precedencia, Registro, directiva de grupo, `Unblock-File` |
| `about_Variables`, `about_Automatic_Variables`, `about_Environment_Variables`, `about_Preference_Variables` | Variables, tipos, borrado, ámbito, automáticas, de entorno, `$ErrorActionPreference` |
| `about_Numeric_Literals` | Sufijos multiplicadores `kb` a `pb` |
| `about_Operators`, `about_Arithmetic_Operators`, `about_Comparison_Operators`, `about_Logical_Operators`, `about_Split`, `about_Join`, `about_Booleans`, `about_If`, `about_Pipeline_Chain_Operators`, `about_Splatting` | Operadores y su precedencia, ejemplos, conversión a lógico, ternario, `&&` y `\|\|`, *splatting* |
| `about_Arrays`, `about_Hash_Tables` | Matrices, índices, `Count`, `+=`, `ForEach()` y `Where()`, tablas hash y diccionarios ordenados |
| `about_Quoting_Rules`, `about_Methods`, guía «Todo lo que quería saber sobre la sustitución de variables en cadenas» (scripting/learn/deep-dives/everything-about-string-substitutions) | Comillas, cadenas *here*, escape, métodos, formato, concatenación y `StringBuilder` |
| `about_Wildcards`, `about_Special_Characters`, `about_Regular_Expressions` | Comodines, secuencias de escape, expresiones regulares |
| `about_Pipelines`; ayuda de `Where-Object`, `ForEach-Object`, `Select-Object`, `Sort-Object`, `Measure-Object`, `Group-Object`, `Format-Table`, `Get-Member`, `Export-Csv` | Canalización, enlace de parámetros, cmdlets de utilidad y sus alias |
| `about_Redirection`; ayuda de `Out-File` y `Tee-Object` | Flujos, operadores, codificación, confusión con `>` |
| `about_If`, `about_Switch`, `about_For`, `about_Foreach`, `about_While`, `about_Do`, `about_Break`, `about_Continue`, `about_Try_Catch_Finally` | Estructuras de control |
| «Trabajar con archivos y carpetas» (scripting/samples/working-with-files-and-folders); ayuda de `Get-ChildItem`, `New-Item`, `Copy-Item`, `Move-Item`, `Rename-Item`, `Remove-Item`, `Test-Path`, `Get-Content`, `Set-Content`, `Add-Content`, `Select-String`, `Set-Location`, `Get-Command` | Gestión de ficheros, parámetros y alias |

La traducción automática de Microsoft trae erratas (palabras pegadas, artículos sueltos, «Pestaña»
por tabulación); se citan tal cual con [sic]. Microsoft traduce *array* por «matriz», *pipeline* por
«canalización» y *here-string* por «cadena aquí»; el tema usa también los términos del enunciado.

Oficio sin fuente detrás, y así se declara: la clasificación en tres juegos de metacaracteres
(comodines, escape y expresiones regulares) y la comparación entre `*` y `?` en cada uno; la regla
para distinguir la instrucción `foreach` del alias del cmdlet `ForEach-Object` por su posición; la
observación de que el último perfil que se ejecuta prevalece; la deducción de que `"1" + 2` concatena
y `1 + "2"` suma (aplicación de la regla del tipo más a la izquierda); los ejemplos propios con
nombres en castellano (`equipos.txt`, `informe.txt`) y el script de aplicación práctica, que no se ha
ejecutado. Son también propios los ejemplos de una línea que el tema no atribuye a Microsoft (por
ejemplo `12 -is [int]`, `(1..10).Where(…)`, `Get-Process notepad && Stop-Process -Name notepad` o las
órdenes sobre `C:\Datos` y `app.log`); los que presenta como de Microsoft, oficiales o de la
documentación lo son.
