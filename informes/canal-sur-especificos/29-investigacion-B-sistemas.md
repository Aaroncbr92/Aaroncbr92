# 29 · Operador/a Informático · Investigación bloque B-sistemas (temas 5 a 10)

Fase 1 (investigar). Sólo lo que falta sobre lo reutilizable de RTVE (que el redactor lee aparte).
Fuentes leídas el **05-10-2026** (fecha real de lectura; el encargo fija «hoy» en 24-09-2026, fecha del
BOJA). Donde la vigencia cambia entre ambas fechas, se dice.

Convenciones: «» = cita literal de la fuente (Microsoft Learn en es-es salvo aviso; la traducción
automática de Microsoft trae erratas, se citan tal cual y se señalan con [sic]). [WF] = cita obtenida
mediante resumen de WebFetch (support.microsoft.com bloquea la descarga directa): **el verificador debe
releerla en la página** antes de ponerla en negrita.

---

## Tema 6 · Windows 11

### 6.0 Versión vigente (decide qué se estudia)

Fuente: «Información de versión de Windows 11», https://learn.microsoft.com/es-es/windows/release-health/windows11-release-information (leída 05-10-2026).

- «Windows 11 tiene una cadencia de actualización de características anual. Las actualizaciones de
  características se publican en la segunda mitad del año natural y cuentan con 24 meses de soporte
  técnico para las ediciones Home, Pro, Pro for Workstations y Pro Education.» Enterprise/Education: 36 meses
  (misma página y página 25H2: «Windows 11 Empresas: atendida durante 36 meses a partir de la fecha de lanzamiento»).
- «Windows 11 también publica actualizaciones de seguridad mensuales el segundo martes de cada mes.
  Estas versiones son acumulativas».
- Tabla «Canal de disponibilidad general» (fechas ISO): 26H2 disponible **2026-09-29** (fin Home/Pro
  2028-10-10; Enterprise 2029-10-09; compilación 26300.x); 26H1 2026-02-10; **25H2 2025-09-30** (fin
  Home/Pro 2027-10-12; Enterprise 2028-10-10; compilación 26200.x); 24H2 2024-10-01 (fin Home/Pro
  **2026-10-13**); 23H2 2023-10-31 (Home/Pro ya «Fin de actualización»; Enterprise 2026-11-10).
- 26H1: «tiene como ámbito admitir nuevos dispositivos que empezaron a comercializarse a principios de
  2026 y no está diseñado como una actualización de características para dispositivos existentes».
- **Consecuencia**: a 24-09-2026 (BOJA) la versión de características más reciente para equipos
  existentes era **25H2**; desde el 29-09-2026 lo es **26H2**. Recomendación al redactor: tratar 25H2
  como base y mencionar 26H2 con su fecha; no dar novedades de 26H2 (no investigadas).
- 25H2 (https://learn.microsoft.com/es-es/windows/whats-new/whats-new-windows-11-version-25h2): «Los
  dispositivos que se actualizan desde Windows 11, versión 24H2, usan un paquete de habilitación.»
- Windows 10 (ciclo de vida, https://learn.microsoft.com/es-es/lifecycle/products/windows-10-enterprise-and-education):
  Enterprise y Education, fecha de retirada «10/15/2025 6:59:59 AM» (UTC; es decir, fin el 14-10-2025);
  versión 22H2 misma fecha. Útil para explicar por qué el temario pasa de Windows 10 (RTVE) a 11.

### 6.1 Instalación del cliente Windows

Requisitos — «Requisitos de Windows 11», https://learn.microsoft.com/es-es/windows/whats-new/windows-11-requirements:
- «Procesador: 1 gigahercio (GHz) o más rápido con dos o más núcleos en un procesador o sistema compatible de 64 bits en un chip (SoC).»
- «Memoria: 4 gigabytes (GB) o superior.» «Almacenamiento: 64 GB o más de espacio disponible en disco.»
- «Tarjeta gráfica: compatible con DirectX 12 o posterior, con un controlador WDDM 2.0.»
- «Firmware del sistema: UEFI, compatible con arranque seguro.» «TPM: módulo de plataforma segura (TPM) versión 2.0.»
- «Pantalla: pantalla de alta definición (720p), monitor de 9" o superior, 8 bits por canal de color.»
- «Windows 11 Home edición requiere una conexión a Internet y una cuenta Microsoft para completar la configuración del dispositivo en el primer uso.»
- Actualizar desde 10: «Ejecución de Windows 10, versión 2004 o posterior.» y «Instaló la actualización de seguridad del 14 de septiembre de 2021 o posterior.»
- «El modo S solo se admite en la edición Home de Windows 11.»
- «Windows 11 también se admite en una máquina virtual (VM).»

Particiones en UEFI/GPT — https://learn.microsoft.com/es-es/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions:
- «Al implementar Windows en un dispositivo basado en UEFI, debes dar formato al disco duro que incluye la partición de Windows mediante un sistema de archivos de tabla de particiones GUID (GPT).»
- «Una unidad GPT puede tener hasta 128 particiones.» «Cada partición puede tener un máximo de 18 exabytes».
- ESP: «Tamaño del sector de 512 bytes nativo o 512e: mínimo 200 MB»; «Tamaño de sector nativo de 4K: mínimo de 300 MB»; «debe tener formato con el formato de archivo FAT32».
- MSR: «El tamaño de MSR es de 16 MB.» «No puede almacenar datos de usuario.»
- Partición de Windows: «al menos 20 gigabytes (GB) de espacio en unidad para versiones de 64 bits»; «Se debe dar formato a la partición de Windows usando el formato de archivo NTFS.»
- **Partición de recuperación** (lo que el enunciado llama «partición de recuperación»): tamaño mínimo = tamaño de winre.wim + personalizaciones + «Un espacio libre adicional de 250 MB»; «Debe colocarse inmediatamente después de la partición de Windows. Esto permite a Windows modificar y volver a crear la partición más adelante si las actualizaciones futuras requieren una imagen de recuperación más grande.»; «Debe estar separada de la partición de Windows para permitir la conmutación automática por fallo y el arranque de particiones cifradas con Cifrado de unidad BitLocker».
- Administración de discos (https://learn.microsoft.com/es-es/windows-server/storage/disk-management/overview-of-disk-management, aplica a Windows 11): «Windows normalmente incluye tres particiones en la unidad principal»: Disco local (C:) «Almacena la instalación del sistema operativo Windows»; Sistema EFI «Permite el proceso de inicio (arranque)»; Recuperación «Almacena herramientas que admiten operaciones de recuperación de Windows cuando el equipo no se inicia».

Herramientas de despliegue — https://learn.microsoft.com/es-es/windows/deployment/windows-deployment-scenarios-and-tools (el artículo dice tratar Windows 10, aplicable a 11):
- Windows ADK incluye «Administración y mantenimiento de imágenes de implementación (DISM)», «Designer de configuración de Windows», «Administrador de imágenes del sistema de Windows (Windows SIM)», «Herramienta de migración de estado de usuario (USMT)», «Herramienta de administración de activación por volumen (VAMT)», «Entorno de preinstalación de Windows (Windows PE)».
- DISM: «Se usa para capturar, reparar e implementar imágenes de arranque e imágenes de sistema operativo.»
- USMT: «ScanState.exe: esta herramienta realiza la copia de seguridad de estado de usuario.» «LoadState.exe: esta herramienta realiza la restauración de estado de usuario.»
- Windows SIM: «es una herramienta de creación de archivos Unattend.xml» (instalación desatendida).
- WSUS: «es un rol de servidor en Windows Server que habilita un repositorio local de actualizaciones de Microsoft.»
- Autopilot (https://learn.microsoft.com/es-es/windows/deployment/windows-autopilot/windows-autopilot): «Windows Autopilot es un conjunto de tecnologías que se utilizan para configurar y preconfigurar nuevos dispositivos, preparándolos para un uso productivo.» «En lugar de volver a crear una imagen del dispositivo, la instalación de Windows existente se puede transformar en un estado "listo para empresas"».

### 6.2 Gestión moderna: Intune (lo pide el encargo)

https://learn.microsoft.com/es-es/intune/intune-service/fundamentals/what-is-intune:
- «Microsoft Intune es un servicio de administración de puntos de conexión basado en la nube que protege y administra los dispositivos y aplicaciones de su organización.»
- «Las plataformas admitidas incluyen Android, iOS/iPadOS, Linux, macOS, tvOS, visionOS y Windows. El servicio se ejecuta completamente en la nube, sin que sea necesaria ninguna infraestructura local».
- «La identidad se ejecuta en Microsoft Entra ID.»
- MDM: «los dispositivos están inscritos, ya sea por un usuario a través de la Portal de empresa o automáticamente a través de Windows Autopilot […]. Intune luego administra todo el dispositivo».
- MAM: «Intune solo administra las aplicaciones de trabajo y los datos dentro de ellas, no el resto del dispositivo. MAM es habitual para dispositivos personales en escenarios de bring-your-own-device (BYOD)».

### 6.3 Políticas de grupo (GPO)

https://learn.microsoft.com/es-es/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview (actualizado 2025-06-18; sirve también al tema 8):
- «La directiva de grupo es una característica de Windows que proporciona administración centralizada y configuración de sistemas operativos, aplicaciones y configuración de usuario. Puede almacenar la configuración de directiva de grupo localmente en el sistema de archivos o en Active Directory Domain Services (AD DS).»
- «Un GPO consta de dos componentes principales: el contenedor de directivas de grupo y la plantilla de directiva de grupo. El contenedor de directivas de grupo se almacena en la partición de dominio de Active Directory, mientras que la plantilla de directiva de grupo se encuentra en la carpeta SYSVOL de cada controlador de dominio (DC).»
- «Las configuraciones de equipo se aplican a nivel del sistema y gestionan opciones como la gestión de energía y las normas de firewall. Las configuraciones de usuario afectan únicamente al usuario actual».
- «Puede vincular GPO a varios niveles dentro de la jerarquía de AD, como sitios, dominios y unidades organizativas (UO)».
- «En el caso de los equipos, la directiva de grupo se aplica cuando se inicia el equipo. Para los usuarios, la directiva de grupo se aplica al iniciar sesión.» «Después, el sistema aplica periódicamente la directiva de grupo (actualizaciones) en segundo plano.»
- «Los administradores pueden crear y administrar GPO mediante el Editor de directivas de grupo local (gpedit.msc) para la configuración local o el Editor de objetos de directiva de grupo dentro de un complemento MMC relacionado con AD para la configuración de todo el dominio. Cada GPO tiene un identificador único global (GUID)».
- «Una UO es el contenedor de AD de nivel más bajo al que puede asignar la configuración de directiva de grupo.» «También puede aplicar algunas opciones de directiva de grupo en el nivel de dominio, especialmente las directivas de contraseña.»
- NO CONFIRMADO: orden de procesamiento local-sitio-dominio-UO (LSDOU) y periodicidad de 90 min ± 30 de la actualización en segundo plano; `gpupdate /force` y `gpresult`. Están en «Procesamiento de directivas de grupo» (no leído). Si el redactor los quiere, leer esa página.
- NO CONFIRMADO: que gpedit.msc no exista en Windows 11 Home (no lo dice la página leída).

### 6.4 Opciones de reinicio para instalar actualizaciones

https://learn.microsoft.com/es-es/windows/deployment/update/waas-restart («Administrar los reinicios de los dispositivos después de las actualizaciones», aplica a Windows 11):
- «Puede usar la configuración de directiva de grupo, la administración de dispositivos móviles (MDM) o el registro de Windows para configurar cuándo se reiniciarán los dispositivos después de instalar una actualización de Windows.»
- «En la directiva de grupo, en Configurar Novedades [sic: Actualizaciones] automática, puede configurar un reinicio forzado después de una hora de instalación especificada.» Opción «4 : Descarga automática y programación de la instalación».
- Retrasar reinicio: «Desactivar el reinicio automático para actualizar durante las horas activas» y «No reiniciar automáticamente para instalar actualizaciones automáticas programadas si hay usuarios conectados».
- «Las horas activas identifican el período en el que se prevé que el dispositivo estará en uso. Se reinicia automáticamente después de que se produzca una actualización fuera del horario activo.»
- «De forma predeterminada, las horas activas son de 8 a. m. a 5 p. m. en equipos.» «La longitud máxima de las horas activas para Windows 10, versión 1607 y Windows Server 2016 es 12. Las versiones posteriores admiten una duración máxima de 18 horas.»
- Ruta GPO: «Configuración del equipo\Plantillas administrativas\Componentes de Windows\Windows Update».
- MDM: «ActiveHoursStart», «ActiveHoursEnd», «ActiveHoursMaxRange».
- Manual: «vaya a Configuración>Windows Update>Opciones avanzadas y seleccione Horas activas.»
- «No se recomienda editar directamente el registro de Windows.»

### 6.5 Protección y recuperación del sistema; puntos de restauración

WinRE — https://learn.microsoft.com/es-es/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference:
- «Windows Entorno de recuperación (WinRE) es un entorno de recuperación que puede reparar las causas comunes de los sistemas operativos que no se pueden arrancar. WinRE se basa en el Entorno de preinstalación de Windows (Windows PE)».
- Herramientas: «Reparación automática y otras herramientas de solución de problemas»; «Restauración a un momento dado: los usuarios pueden restaurar rápidamente su equipo Windows al estado exacto, en el que estaba en un momento dado anterior, mediante puntos de restauración almacenados localmente»; «Restablecimiento mediante botón (solo para las ediciones de escritorio de Windows)»; «Recuperación de imágenes del sistema (solo Windows Server ediciones)».
- Entradas: «En la pantalla de inicio de sesión, haga clic en Apagar y mantenga presionada la tecla Mayús mientras selecciona Reiniciar.»; desde Configuración > Inicio avanzado «Reiniciar ahora»; «Arranque en medios de recuperación»; botón de hardware del OEM.
- Arranque automático en WinRE: «Dos intentos fallidos consecutivos de iniciar Windows.»; «Dos apagados inesperados consecutivos que se producen en un plazo de dos minutos después de la finalización del arranque.»; «Dos reinicios consecutivos del sistema en un plazo de dos minutos […]»; «Error de arranque seguro (excepto los problemas relacionados con Bootmgr.efi).»; «Un error de BitLocker en dispositivos solo táctiles.»
- Menú Inicio avanzado: herramientas de recuperación; «Arranque desde un dispositivo (solo UEFI).»; «Acceda al menú Firmware (solo UEFI).»; elegir SO.
- Novedad 11: «Ahora puedes ejecutar la mayoría de las herramientas en WinRE sin seleccionar una cuenta de administrador ni escribir la contraseña. […] los archivos cifrados no serán accesibles a menos que el usuario tenga la clave para descifrar el volumen.»
- «WinRE no mantiene la conectividad de red de uso general de forma predeterminada.»

Soporte de Microsoft (es-es) [WF, releer]:
- Protección del sistema (https://support.microsoft.com/es-es/windows/experience/backup-recovery/system-protection): «La protección del sistema en Windows es una característica de recuperación diseñada para ayudarte a proteger la configuración del sistema.» Puntos de restauración: «Son instantáneas de los archivos del sistema, las aplicaciones instaladas, el Registro de Windows y la configuración del sistema en un momento específico.» «La protección del sistema creará puntos de restauración automáticamente, cuando sea necesario.» Manual: Inicio, buscar «Crear un punto de restauración», Propiedades del sistema, «Crear...». Control deslizante de «cantidad máxima de espacio en disco».
- Restauración del sistema: se abre con `rstrui.exe` (Win+R) o Panel de control > Recuperación > «Abrir Restaurar sistema» [resumen de búsqueda; releer].
- Opciones de recuperación (https://support.microsoft.com/es-es/windows/experience/backup-recovery/recovery-options-in-windows): Restablecer este PC «reinstala Windows desde cero. Puede optar por conservar sus archivos personales o quitarlos todos.»; reinstalar con Windows Update «reinstala la versión actual sin afectar a los archivos, las aplicaciones ni la configuración»; Restauración del sistema «revierte los archivos y la configuración del sistema (pero no los archivos personales)»; Restauración a un momento dado «revierte todo el equipo, incluidas las aplicaciones, la configuración y los archivos personales, a un punto de restauración automática reciente», **sólo Windows 11 24H2 o posterior**; volver a la versión anterior «disponible durante 10 días después de la actualización»; unidad de recuperación. Ruta: Configuración > Sistema > Recuperación. [WF: el resumen dio también «Configuración > Solucionar problemas > Restablecer este equipo», dudoso: releer.]

### 6.6 Configuración de la seguridad

Seguridad de Windows — https://learn.microsoft.com/es-es/windows/security/operating-system-security/system-security/windows-defender-security-center/windows-defender-security-center:
- «Seguridad de Windows es una interfaz de cliente en Windows 10, versión 1703 y posteriores. No es la consola del portal web Centro de seguridad de Microsoft Defender».
- Secciones: «Virus & protección contra amenazas» (incluye «acceso controlado a carpetas» contra ransomware); «Protección de cuentas»; «Firewall & protección de red»; «La aplicación & control del explorador» (SmartScreen y protección contra vulnerabilidades); «Seguridad del dispositivo»; «El rendimiento del dispositivo & el estado» (controladores, almacenamiento, Windows Update); «Opciones familiares».
- «No puede desinstalar Seguridad de Windows».
- BitLocker y UAC: ya en RTVE (tema 16). BitLocker To Go: «requiere una unidad flash USB. Esta característica está disponible en Windows Pro y versiones posteriores» (página de requisitos).

### 6.7 Centro de notificaciones [WF, releer]

https://support.microsoft.com/es-es/windows/cambiar-la-notificaci%C3%B3n-y-la-configuraci%C3%B3n-r%C3%A1pida-en-windows-ddcbbcd4-0a02-f6e4-fe14-6766d850f294:
- Abrir: «Seleccione el icono del reloj o de la campana de notificación en la barra de tareas», «Presione la tecla de Windows + N», deslizar desde el lateral.
- Configuración rápida: tecla Windows + A.
- No molestar: «solo recibirá banners de alarmas, recordatorios y aplicaciones de su elección»; se activa en el centro con la campana «zZ».
- Ruta: Inicio > Configuración > Sistema > Notificaciones.

### 6.8 Modo desarrollador

https://learn.microsoft.com/es-es/windows/apps/get-started/enable-your-device-for-development:
- «El modo de desarrollador desbloquea herramientas, configuraciones y características diseñadas para compilar, implementar y probar aplicaciones».
- «Antes de Windows 11 25H2, esta configuración aparece en la página Para desarrolladores en Windows configuración. En Windows 11 25H2 y versiones posteriores, aparecen en la sección Para desarrolladores de la Configuración avanzada.» (Configuración > Sistema > Avanzado).
- «La habilitación del modo desarrollador requiere acceso de administrador. Si el dispositivo es propiedad de una organización, esta opción puede deshabilitarse.»
- «El modo de desarrollador reemplaza los requisitos de una licencia de desarrollador. Además de la carga lateral, la configuración de modo de desarrollador permite la depuración y opciones de implementación adicionales.» Activa Device Portal (si se habilita) y SSH para detección de dispositivos.
- «Si usas tu ordenador para actividades cotidianas normales […] no es necesario activar el modo de desarrollador.»

### 6.9 Lo que no se ha investigado del tema 6

- Interfaz y aplicaciones, personalización, panel de configuración (Configuración/Panel de control) y conectividad de red de Windows 11: no se buscó fuente oficial específica; la parte de Explorador y escritorio está en RTVE (Windows 10). Hueco declarado.
- Controladores: la página de Learn leída es para desarrolladores y no da texto útil; no hay cita sobre Administrador de dispositivos. Hueco.
- Gestión de discos: sólo lo citado en 6.1 (inicializar, extender, reducir, cambiar letra). Faltan diskpart, discos dinámicos, Espacios de almacenamiento.

---

## Tema 7 · PowerShell

Fuente única: documentación oficial de PowerShell en Microsoft Learn (es-es), leída 05-10-2026. Las
páginas `about_*` son las de la versión por defecto del sitio (PowerShell 7.x). Base:
`https://learn.microsoft.com/es-es/powershell/module/microsoft.powershell.core/about/<about_X>`.
Lo de RTVE no cubre PowerShell: todo este tema es nuevo.

### 7.1 Entorno PowerShell

- «¿Qué es PowerShell?» (https://learn.microsoft.com/es-es/powershell/scripting/overview): «PowerShell es una solución de automatización de tareas multiplataforma formada por un shell de línea de comandos, un lenguaje de scripting y un marco de administración de configuración. PowerShell se ejecuta en Windows, Linux y macOS.»
- «A diferencia de la mayoría de los shells que solo aceptan y devuelven texto, PowerShell acepta y devuelve objetos .NET.» «PowerShell se basa en .NET Common Language Runtime (CLR). Todas las entradas y salidas son objetos de .NET.»
- Características del shell: «Un historial de línea de comandos sólido.» «Finalización con tabulación y predicción de comandos (vea about_PSReadLine).» «Admite alias de comandos y parámetros.» «Canalización para encadenar comandos.» «Sistema de ayuda en la consola, similar a las páginas man de UNIX.»
- Cmdlets (PS101 cap. 2, https://learn.microsoft.com/es-es/powershell/scripting/learn/ps101/02-help-system): «Los comandos compilados en PowerShell se conocen como cmdlets […]. La convención de nomenclatura de los cmdlets sigue un formato singular Verbo-Sustantivo para que sean fácilmente descubribles. Por ejemplo, Get-Process».
- **Versiones vigentes** (https://learn.microsoft.com/es-es/powershell/scripting/install/powershell-support-lifecycle): «La versión estable actual es PowerShell 7.5.11.» «La versión ltS [sic] actual es PowerShell 7.6.6. La versión anterior de LTS, PowerShell 7.4.20, sigue siendo compatible hasta el 10 de noviembre de 2026.» «PowerShell 7.7-preview.3 es la versión preliminar actual.» Tabla: 7.6 (LTS) publicada 18-03-2026, fin 14-11-2028, .NET 10.0; 7.5 publicada 23-01-2025, fin 10-11-2026, .NET 9.0; 7.4 (LTS) 16-11-2023, fin 10-11-2026. «Una versión LTS de PowerShell es una versión LTS de .NET.» Windows PowerShell 5.1: «Agosto de 2016», «Publicado en Windows 10 Actualización de aniversario y Windows Server 2016, WMF 5.1»; «Microsoft ya no admite Windows versiones de PowerShell inferiores a la 5.1.» «La compatibilidad con Windows PowerShell 5.1 se proporciona a través de los canales de soporte técnico de Windows.»
  (Las cifras de parche —7.5.11, 7.6.6, 7.4.20— cambian cada mes: el redactor debería dar sólo 7.6 LTS / 7.5 estable / 5.1 integrada.)
- Ejecutable (https://learn.microsoft.com/es-es/powershell/scripting/whats-new/differences-from-windows-powershell): «El nombre binario de PowerShell se ha cambiado de powershell(.exe) a pwsh(.exe). Este cambio proporciona una manera determinista para que los usuarios ejecuten PowerShell en máquinas y admitan instalaciones en paralelo de Windows PowerShell y PowerShell.»
- **Directivas de ejecución** (about_Execution_Policies): «La directiva de ejecución de PowerShell es una característica de seguridad que controla las condiciones en las que PowerShell carga archivos de configuración y ejecuta scripts.» «El cumplimiento de estas directivas solo se produce en plataformas Windows.» Valores: AllSigned («Requiere que todos los scripts y archivos de configuración estén firmados por un editor de confianza, incluidos los scripts que escriba en el equipo local»), Bypass, Default, RemoteSigned («Directiva de ejecución predeterminada para equipos Windows»; «Requiere una firma digital de un editor de confianza en scripts y archivos de configuración que se descargan desde Internet»; «No requiere firmas digitales en scripts escritos en el equipo local»), Restricted («Permite comandos individuales, pero no permite scripts.»), Undefined, Unrestricted («La directiva de ejecución predeterminada para equipos que no son de Windows y no se puede cambiar.»). `Get-ExecutionPolicy -List`; `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`; «El cambio es efectivo inmediatamente.»
  AVISO: la página es la de PowerShell 7. La versión 5.1 de la misma página (no leída) da Restricted como predeterminada en clientes Windows. NO CONFIRMADO: leer `?view=powershell-5.1` si el redactor quiere afirmarlo.

### 7.2 Ayuda

PS101 cap. 2 (URL arriba):
- «Get-Help es un comando multipropósito que le ayuda a aprender a usar comandos una vez que los encuentre.» «Tanto Get-Help como Get-Command son recursos valiosos para detectar y comprender comandos en PowerShell.» Get-Member en el capítulo 3.
- «A partir de la versión 3.0 de PowerShell, el contenido de ayuda no se incluye previamente con el sistema operativo.» Al aceptar, «ejecuta el cmdlet Update-Help, descargando el contenido de ayuda.» «Si no recibe este mensaje, ejecute Update-Help desde una sesión de PowerShell con privilegios elevados que se ejecuta como administrador.»
- Parámetros: -Full, -Detailed, -Examples, -Online (seis conjuntos de parámetros); «no puede usar los parámetros Full y Detailed de Get-Help juntos porque pertenecen a diferentes conjuntos de parámetros.»
- «la función help puede ser útil. Canaliza la salida de Get-Help para more.com, mostrando una página de contenido de ayuda a la vez.»
- Artículos conceptuales: «about_Arithmetic_Operators», «about_Arrays», etc. (nombres `about_*`).

### 7.3 Variables (about_Variables)

- «Una variable es una unidad de memoria en la que se almacenan los valores. En PowerShell, las variables se representan mediante cadenas de texto que comienzan con un signo de dólar ($)».
- «Los nombres de variable no distinguen mayúsculas de minúsculas».
- Tipos: «Variables creadas por el usuario» («solo existen mientras la ventana de PowerShell está abierta»); «Variables automáticas: las variables automáticas almacenan el estado de PowerShell. […] Los usuarios no pueden cambiar el valor de estas variables. Por ejemplo, la variable $PSHOME»; «Variables de preferencia […] Los usuarios pueden cambiar los valores de estas variables. Por ejemplo, la variable $MaximumHistoryCount».
- «No es necesario declarar la variable antes de usarla. El valor predeterminado de todas las variables es $null.» «Para obtener una lista de todas las variables de la sesión de PowerShell, escriba Get-Variable.»
- «Para eliminar el valor de una variable, use el cmdlet Clear-Variable o cambie el valor a $null.» «Para eliminar la variable, use Remove-Variable o Remove-Item.» Cmdlets: Clear-Variable, Get-Variable, New-Variable, Remove-Variable, Set-Variable.
- «Puede usar un atributo de tipo y una notación de conversión para asegurarse de que una variable solo puede contener tipos de objetos» (p. ej. `[int]$x`).
- «De forma predeterminada, las variables solo están disponibles en el ámbito en el que se crean.»
- `$_` / `$PSItem` = objeto actual en la canalización (aparece en about_Pipelines con `Where-Object {$_.Length -gt 10000}`); `$Matches` (ver 7.4).

### 7.4 Operadores (about_Operators, about_Comparison_Operators, about_Logical_Operators)

- «Use operadores aritméticos (+, -, *, /, %) para calcular valores […] y calcular el resto (módulo)».
- «Use operadores de asignación (=, +=, -=, *=, /=, %=)» [la página trae el orden tipográfico roto; se normaliza].
- Comparación (lista literal): «-eq, -ieq, -ceq : es igual a»; «-ne, -ine, -cne, no son iguales»; «-gt […] mayor que»; «-ge […] mayor o igual que»; «-lt […] menor que»; «-le […] menor o igual que»; «-like […] la cadena coincide con el patrón de caracteres comodín»; «-notlike»; «-match […] la cadena coincide con el patrón regex»; «-notmatch»; «-replace […] busca y reemplaza cadenas que coinciden con un patrón regex»; «-contains […] la colección contiene un valor»; «-notcontains»; «-in […] el valor está en una colección»; «-notin»; «-is: ambos objetos son del mismo tipo»; «-isnot».
- «Las comparaciones de cadenas no distinguen entre mayúsculas y minúsculas, a menos que se utilice un operador explícitamente sensible […]. Para que un operador de comparación distingue mayúsculas de minúsculas, agregue un c después del -. Por ejemplo, -ceq».
- «Los operadores -match y -notmatch también rellenan la variable automática $Matches a menos que el lado izquierdo de la expresión sea una colección.»
- Lógicos: «Use operadores lógicos (-and, -or, -xor, -not, !) para conectar instrucciones condicionales». «Si el operando izquierdo de una instrucción que contiene la -or instrucción es TRUE, el operando derecho no se evalúa.» «Los -and, -or y -xor tienen la misma prioridad. Se evalúan de izquierda a derecha».
- Redirección: «Use operadores de redireccionamiento (>, >>, 2>, 2>> y 2>&1) para enviar la salida de un comando o expresión a un archivo de texto.»
- about_Operators también agrupa: «Operadores de división y combinación» (-split, -join), «Operadores de tipo», «Operadores unarios», «Operadores especiales». «(...) sirve para invalidar la precedencia del operador».

### 7.5 Arrays (about_Arrays)

- «Una matriz es una estructura de datos diseñada para almacenar una colección de elementos.»
- «El operador de subexpresión de matriz crea una matriz a partir de las instrucciones que contiene. […] Incluso si hay cero o un objeto.» `@()`; `$b = @()`.
- «Puede hacer referencia a los elementos de una matriz mediante un índice. […] Los valores de índice comienzan en 0.»
- «Puede recuperar parte de la matriz mediante un operador de intervalo para el índice» (`$a[1..4]`).
- «Los números negativos cuentan desde el final de la matriz. Por ejemplo, -1 hace referencia al último elemento de la matriz.»
- «Count: esta propiedad es la propiedad más usada para determinar el número de elementos de cualquier colección»; «Length: […] Contiene el mismo valor que Count.»; «Length para una cadena es el número de caracteres de la cadena».
- Tablas hash: about_Hash_Tables descargado, no extractado.

### 7.6 Strings y comillas (about_Quoting_Rules)

- «Puede incluir una cadena entre comillas simples (') o comillas dobles (").»
- «Una cadena entre comillas dobles es una cadena expandible. Los nombres de variable precedidos por un signo de dólar ($) se reemplazan por el valor de la variable».
- «en una cadena entre comillas dobles, se evalúan las expresiones» (ej. «"The value of $(2+3) is 5."»). «Las referencias de variables que usan la indexación de matriz o el acceso a miembros deben incluirse en una subexpresión.»
- «Una cadena entre comillas simples es un cadena textual. La cadena se pasa al comando exactamente al escribirla. No se realiza ninguna sustitución.»
- «Para evitar la sustitución de un valor de variable en una cadena entre comillas dobles, use el carácter de retroceso (`), que es el carácter de escape de PowerShell.»
- Here-string: «Una cadena aquí puede abarcar varias líneas.» (sintaxis @"…"@ / @'…'@, no citada literal).

### 7.7 Metacaracteres (about_Wildcards, about_Special_Characters, about_Regular_Expressions)

Comodines: «Las expresiones comodín se usan con el operador -like o con cualquier parámetro que acepte caracteres comodín.» «Las expresiones comodín son más sencillas que las expresiones regulares.»
- «*: coincidencia con cero o más caracteres»
- «?: en el caso de las cadenas, coincida con un carácter en esa posición.» / «?: para archivos y directorios, coincida con cero o un carácter en esa posición.»
- «[ ]: coincidencia de un intervalo de caracteres» ([a-l]ook) y «de caracteres específicos» ([bc]ook)
- «`*: coincide con cualquier carácter como literal (no comodín)»
- «Para los parámetros que aceptan caracteres comodín, su uso no distingue mayúsculas de [minúsculas]».

Caracteres especiales: «Las secuencias de escape comienzan con el carácter de retroceso, conocido como énfasis grave (ASCII 96) y distinguen mayúsculas de minúsculas.» «Las secuencias de escape solo se interpretan cuando se encuentran en cadenas entre comillas dobles (").» Tabla: `0 Nulo; `a Alerta; `b Retroceso; `e Escape (PowerShell 6); `f Fuente de formularios [sic: avance de página]; `n Nueva línea; `r Retorno de carro; `t Pestaña [sic: tabulación] horizontal; `u{x} Unicode (PowerShell 6); `v vertical. Tokens: «--» «Tratar los valores restantes como argumentos no parámetros»; «--%» «Dejar de analizar todo lo que sigue» («impide que PowerShell interprete cadenas como comandos y expresiones»).

Expresiones regulares: «La \d clase de caracteres coincide con cualquier dígito decimal.» «\w coincide con cualquier carácter de palabra [a-zA-Z_0-9].» «\s» espacio en blanco. Cuantificadores: «* Cero o más veces.» «+ Una o varias veces.» «? Cero o una vez.» «{n,m} Al menos n, pero no más de m veces.» Anclajes: «El símbolo de acento circunflejo ^ coincide con el inicio de una cadena y $, que corresponde al final de una cadena.» «La barra diagonal inversa (\) se usa para caracteres de escape».

### 7.8 Tuberías (about_Pipelines)

- «Una tubería es una serie de comandos conectados por operadores de tubería (|) (ASCII 124). Cada operador de canalización envía los resultados del comando anterior al siguiente comando.»
- Ejemplo «Command-1 | Command-2 | Command-3» … «Dado que no hay más comandos en la canalización, los resultados se muestran en la consola.»
- Enlace de parámetros: «ByValue: el parámetro acepta valores que coinciden con el tipo de .NET esperado o que se pueden convertir a ese tipo.» «ByPropertyName: el parámetro acepta la entrada solo cuando el objeto de entrada tiene una propiedad del mismo nombre que el parámetro.»

### 7.9 Direccionamiento / redirección (about_Redirection)

- Tres métodos: «Use el cmdlet Out-File»; «Use el cmdlet Tee-Object, que envía la salida del comando a un archivo de texto y, a continuación, lo envía a la canalización.»; operadores de redireccionamiento.
- Flujos: 1 Éxito (Write-Output, PS 2.0); 2 Error (Write-Error, 2.0); 3 Advertencia (Write-Warning, 3.0); 4 Detallado (Write-Verbose, 3.0); 5 Depuración (Write-Debug, 3.0); 6 Información (Write-Information, Write-Host, 5.0); * todos (3.0). «También hay un flujo Progress en PowerShell, pero no admite el redireccionamiento.»
- «Los flujos de Correcto y Error son similares a los flujos stdout y stderr de otros shells. Sin embargo, stdin no está conectado a la pipeline».
- Operadores: «> Envíe una secuencia especificada a un archivo.» (n>); «>> Añade el transmisión especificado a un archivo.» (n>>); «>&1 Redirige la transmisión especificada a la transmisión de éxito.» (n>&1). «La transmisión Éxito ( 1 ) es el predeterminado». «A diferencia de algunos shells de Unix, solo puede redirigir otros flujos a la transmisión de Éxito.»
- Ejemplo: «dir C:\, fakepath 2>&1 > .\dir.log».

### 7.10 Estructuras de control

- if (about_If): «Puede usar la instrucción if para ejecutar bloques de código si una prueba condicional especificada se evalúa como true. También puede especificar una o varias pruebas condicionales adicionales para ejecutarse si todas las pruebas anteriores resultan falsas.» (elseif / else).
- switch (about_Switch): «La switch instrucción es similar a una serie de if instrucciones, pero es más sencilla.» «La switch instrucción convierte todos los valores en cadenas antes de la comparación.» «La cláusula default se desencadena cuando el valor no coincide con ninguna de las condiciones. Es equivalente a una cláusula else en una instrucción if.» Usa `$_` y `$switch`.
- for (about_For): «crear un bucle que ejecute comandos en un bloque de comandos mientras una condición especificada se evalúa como $true.» «si desea iterar todos los valores de una matriz, considere la posibilidad de usar una instrucción foreach.»
- foreach (about_Foreach): «La instrucción foreach es una construcción de lenguaje para recorrer en iteración un conjunto de valores de una colección.» (Distinto del cmdlet ForEach-Object, que cita como relacionado.)
- while (about_While): «crear un bucle que ejecuta comandos en un bloque de comandos siempre que una prueba condicional se evalúe como true.»
- do (about_Do): «A diferencia del bucle relacionado while, el bloque de instrucciones de un do bucle siempre se ejecuta al menos una vez.» do/until: «el bloque de instrucciones solo se ejecuta mientras la condición es false.» «Las palabras clave de continue control de flujo y break se pueden usar en un do/while bucle o en un do/until bucle.»

### 7.11 Gestión de ficheros

«Trabajar con archivos y carpetas», https://learn.microsoft.com/es-es/powershell/scripting/samples/working-with-files-and-folders:
- «Para obtener todos los elementos directamente dentro de una carpeta, use Get-ChildItem. Agregue el parámetro Force opcional para mostrar elementos ocultos o del sistema.» `-Recurse`; filtros «Path, Filter, Include y Exclude».
- «La copia se realiza con Copy-Item.» «El comando Test-Path comprueba si el script de perfil existe.»
- `New-Item -Path 'C:\temp\New Folder' -ItemType Directory`; `-ItemType File`.
- «Los elementos contenidos se pueden quitar mediante Remove-Item, pero se pedirá que se confirme la eliminación si el elemento contiene algo más.» (`-Recurse` para no preguntar).
- `New-PSDrive -Name P -Root $env:ProgramFiles -PSProvider FileSystem` «visible solo desde la sesión de PowerShell».
- «Get-Content trata los datos leídos del archivo como una matriz, con un elemento por línea de contenido del archivo.»
- NO CONFIRMADO (no leídos): Move-Item, Rename-Item, Set-Content/Add-Content, Out-File parámetros; alias `ls`/`dir`/`cd`. Si se quieren, leer about_Aliases o la ayuda de cada cmdlet.

---

## Tema 8 · Windows Server y Active Directory

Microsoft Learn es-es, leído 05-10-2026. Base: https://learn.microsoft.com/es-es/windows-server/…
RTVE da sólo «Directorio Activo como implementación de LDAP» y la tabla de tareas: lo de abajo es lo que falta.

### 8.0 Versión vigente

- Ciclo de vida (https://learn.microsoft.com/es-es/lifecycle/products/windows-server-2025): Windows Server 2025, inicio «11/1/2024», fin estándar «11/14/2029», fin ampliado «11/15/2034». Ediciones listadas: Datacenter, Datacenter: Azure Edition, Essentials, Standard.
- Novedades 2025 relevantes para AD (https://learn.microsoft.com/es-es/windows-server/get-started/whats-new-windows-server-2025):
  - «Función opcional de tamaño de página de base de datos de 32k: Active Directory usa una base de datos del motor de almacenamiento extensible (ESE) desde que se incluyera en Windows 2000 que usa un tamaño de página de base de datos de 8k.»
  - «Niveles funcionales de bosque y dominio: El nuevo nivel funcional […] es necesario para la nueva función de tamaño de página de base de datos de 32k. El nuevo nivel funcional se asigna al valor de DomainLevel 10 y ForestLevel 10».
  - «Los nuevos bosques de Active Directory o conjuntos de configuración de AD LDS deben tener un nivel funcional de Windows Server 2016 o posterior.»
  - Hotpatch: «Puede usar Hotpatch para aplicar actualizaciones de seguridad del sistema operativo sin reiniciar la máquina» (para máquinas conectadas a Azure Arc; la página lo marca «versión preliminar»). DTrace «como herramienta nativa».
- NO CONFIRMADO: diferencias Standard/Datacenter en número de máquinas virtuales (la tabla de ediciones descargada no lo da de forma extraíble). No afirmarlo.

### 8.1 Active Directory y servicio de directorio

«Información general de AD DS», https://learn.microsoft.com/es-es/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview (actualizado 2025-08-16):
- «Un directorio es una estructura jerárquica que almacena información sobre los objetos de una red. Un servicio de directorio, como Active Directory Domain Services (AD DS), proporciona los métodos para almacenar datos de directorio y poner dichos datos a disposición de los usuarios y administradores de la red.»
- «Estos objetos suelen incluir recursos compartidos como servidores, volúmenes, impresoras y cuentas de usuario y equipo de red.»
- «La seguridad se integra con AD DS mediante la autenticación de inicio de sesión y el control de acceso a los objetos del directorio. Con un único nombre de usuario y contraseña de red […] los usuarios de red autorizados pueden acceder a los recursos en cualquier parte de la red.»
- AD DS incluye: «el esquema, que define las clases de objetos y atributos contenidos en el directorio»; «Catálogo global que contiene información sobre todos los objetos del directorio»; «Un mecanismo de consulta e índice»; «Un servicio de replicación […]. Todos los controladores de dominio de un dominio participan en la replicación y contienen una copia completa de toda la información de directorio del dominio.»

Modelo lógico, https://learn.microsoft.com/es-es/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model (2025-05-12):
- «Un bosque es una colección de uno o varios dominios de Active Directory que comparten una estructura lógica común, un esquema de directorio (definiciones de clase y atributo), una configuración de directorio (información de sitio y replicación) y un catálogo global […]. Los dominios del mismo bosque se vinculan automáticamente con relaciones de confianza transitivas bidireccionales.»
- «Un dominio es una partición de un bosque de Active Directory.» Funciones: «Identidad de usuario en toda la red»; «Los controladores de dominio proporcionan servicios de autenticación»; «Relaciones de confianza»; «Replication [sic]. […] todos los controladores de dominio tienen el mismo nivel en un dominio y se administran como una unidad.»
- «Las unidades organizativas se pueden usar para formar una jerarquía de contenedores dentro de un dominio. Las unidades organizativas se usan para agrupar objetos con fines administrativos, como la aplicación de una directiva de grupo o la delegación de autoridad.»
- NO CONFIRMADO: definición literal de «árbol» de dominios (no aparece en la página leída).

### 8.2 Controlador de dominio

Roles FSMO — https://learn.microsoft.com/es-es/windows-server/identity/ad-ds/plan/planning-operations-master-role-placement:
- «AD DS admite la replicación multimaestro de datos de directorio, lo que significa que cualquier controlador de dominio puede aceptar cambios de directorio y replicar los cambios en los demás controladores de dominio.»
- «Hay tres roles de maestro de operaciones (llamadas también operaciones de maestro único flexible o FSMO) en cada dominio»: emulador de PDC («procesa todas las actualizaciones de contraseñas»); maestro RID («mantiene el grupo de RID global para el dominio y asigna grupos de RID locales a todos los controladores de dominio»); maestro de infraestructura («mantiene una lista de las entidades de seguridad de otros dominios que son miembros de grupos dentro de su dominio»).
- «existen dos roles de maestro de operaciones en cada bosque»: maestro de esquema («administra los cambios en el esquema») y maestro de nomenclatura de dominios («agrega y quita dominios y otras particiones de directorio»).
- «Los titulares de roles de maestro de operaciones se asignan automáticamente cuando se crea el primer controlador de dominio en un determinado dominio.»
- «Debido a la naturaleza de solo lectura de la base de datos de Active Directory en un controlador de dominio de solo lectura (RODC), los RODC no pueden actuar como titulares de roles de maestro de operaciones».
- GPO en el DC: contenedor en AD y plantilla «en la carpeta SYSVOL de cada controlador de dominio» (ver 6.3).

Instalación — https://learn.microsoft.com/es-es/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-:
- `Install-WindowsFeature -name AD-Domain-Services -IncludeManagementTools`
- «El cmdlet Install-ADDSForest instala un nuevo bosque.» `Install-ADDSForest -DomainName "corp.contoso.com"`
- «El servidor DNS se instala de forma predeterminada al ejecutar Install-ADDSForest.»
- «Use Install-ADDSDomainController para instalar un controlador de dominio adicional.»

### 8.3 Gestión básica de usuarios

- Cuentas predeterminadas (https://learn.microsoft.com/es-es/windows-server/identity/ad-ds/manage/understand-default-user-accounts): «Las cuentas locales predeterminadas del contenedor Usuarios incluyen: Administrador, Invitado y KRBTGT.» «La cuenta de invitado es una cuenta local predeterminada que tiene acceso limitado al equipo y está deshabilitada de forma predeterminada.» «se recomienda dejar deshabilitada la cuenta de invitados». Administrador: «Cambiar el nombre o deshabilitar la cuenta de administrador dificulta que los usuarios malintencionados intenten obtener acceso a la cuenta.»
- Alta por PowerShell (https://learn.microsoft.com/es-es/powershell/module/activedirectory/new-aduser — la página es-es sirve el texto en inglés): «The New-ADUser cmdlet creates an Active Directory user.» «You must specify the SamAccountName parameter to create a user.» «$Null password is specified: No password is set and the account is disabled unless it is requested».
- Grupos (https://learn.microsoft.com/es-es/windows-server/identity/ad-ds/manage/understand-security-groups): tipos: «Grupos de seguridad: se usa para asignar permisos a los recursos compartidos.» / «Grupos de distribución: se usa para crear listas de distribución de correo electrónico.» «Los grupos de distribución no están habilitados para la seguridad, por lo que no se pueden incluir en las DACL.» «Los permisos y los derechos de usuario no son lo mismo.» «deben asignar esos permisos a un grupo de seguridad en lugar de a usuarios individuales.»
  - Ámbitos: «Active Directory define los tres ámbitos de grupo siguientes: Universal, Global, Dominio local». Además «Builtin Local».
  - Universal: miembros «Cuentas de cualquier dominio del mismo bosque», grupos globales y universales del bosque; permisos «En cualquier dominio dentro del mismo bosque o bosques confiables».
  - Global: miembros «Cuentas del mismo dominio» y «Otros grupos globales del mismo dominio»; permisos «En cualquier dominio del mismo bosque, o en dominios o bosques de confianza».
  - Dominio local: miembros «Cuentas de cualquier dominio o de cualquier dominio de confianza», grupos globales y universales, otros locales de dominio del mismo dominio; permisos «Dentro del mismo dominio».
- Herramientas gráficas: el Centro de administración de Active Directory existe (página ADAC leída, sólo en contexto de papelera de reciclaje). NO CONFIRMADO con cita: «Usuarios y equipos de Active Directory» (dsa.msc) y ADAC (dsac.exe). Hueco.

### 8.4 Recursos y servicios asociados

- DNS (https://learn.microsoft.com/es-es/windows-server/networking/dns/dns-overview): «DNS es un protocolo estándar del sector que asigna nombres de dominio a direcciones IP». «En Windows Server, DNS es un rol de servidor que se puede instalar mediante el Administrador del servidor o comandos de PowerShell. Al configurar un nuevo bosque y dominio de Active Directory, DNS se instala automáticamente con Active Directory.» «DNS es esencial para Active Directory Domain Services (AD DS), que actúa como mecanismo de ubicación del controlador de dominio». El cliente DNS: «Detecta controladores de dominio.» «Convierte los nombres de equipo en direcciones IP.» Característica: «Integración de Active Directory: actualizaciones seguras y replicación de datos DNS.»
- DHCP (https://learn.microsoft.com/es-es/windows-server/networking/technologies/dhcp/dhcp-top): «El Protocolo de configuración dinámica de host (DHCP) es un protocolo cliente-servidor que proporciona automáticamente un host de protocolo de Internet (IP) con su dirección IP y otra información de configuración relacionada, como la máscara de subred y la puerta de enlace predeterminada. En RFC 2131 y RFC 2132, DHCP se define como un estándar». Base de datos del servidor: parámetros TCP/IP, «Direcciones IP válidas, mantenidas en un grupo […], así como direcciones excluidas», «Direcciones IP reservadas asociadas a determinados clientes DHCP», «La duración de la concesión». Opciones: «Enrutador (puerta de enlace predeterminada), Servidores DNS y Nombre de dominio DNS». «Autorización del servidor DHCP. Esta característica permite autorizar servidores DHCP en Active Directory, lo que impide que los servidores no autorizados proporcionen direcciones IP a los clientes.»
- Archivos compartidos — SMB (https://learn.microsoft.com/es-es/windows-server/storage/file-server/file-server-smb-overview): «El protocolo SMB es un protocolo de uso compartido de archivos de red. SMB permite leer y escribir en archivos a través de la red sobre TCP/IP u otros protocolos.» Rutas UNC: ya en RTVE (tema 16).
- GPO: ver 6.3 (misma fuente, aplica a Windows Server 2016-2025).
- NO investigado: impresoras compartidas, DFS, permisos NTFS vs. compartidos, Administrador del servidor y Windows Admin Center, Entra ID / Entra Connect (híbrido). Huecos.

---

## Tema 9 · Administración de Linux

Fuentes: páginas de manual de Linux (man7.org, proyecto man-pages, versión servida el 05-10-2026),
FHS 3.0 (Linux Foundation), manuales GNU (grep, sed, gawk, tar), documentación oficial de Ubuntu Server
y Debian. Todas en inglés: la traducción es del redactor; se cita el original.
RTVE ya da pwd, top, getfacl, systemctl, journalctl, cron y equivalencias Ubuntu.

### 9.0 Distribuciones vigentes

- Ubuntu (https://ubuntu.com/about/release-cycle): «Ubuntu releases a new version every six months. […] versioned by the year and month of delivery – for example, Ubuntu 26.04 was released in April 2026.» «LTS are released every two years and receive 5 years of standard security maintenance.» Interinas: «only 9 months of updates». Ubuntu Pro: «up to 15 years of security coverage». La LTS vigente es **26.04 LTS** («Resolute Raccoon», wiki.ubuntu.com/Releases). La anterior LTS 24.04 sigue listada.
- Debian (https://www.debian.org/releases/): «The current stable distribution of Debian is version 13, codenamed trixie.» Última revisión «13.7, was released on September 12th, 2026».
- NO investigado: RHEL / Fedora versiones vigentes. dnf: «DNF is the next upcoming major version of YUM, a package manager for RPM-based Linux» (https://dnf.readthedocs.io/en/latest/command_ref.html; frase antigua de la propia doc, no implica versión).

### 9.1 Instalación

Ubuntu Server, «Basic installation» (https://documentation.ubuntu.com/server/tutorial/basic-installation/, actualizado 14-05-2026):
- Requisitos mínimos recomendados del tutorial: «RAM: 2 GB or more»; «Disk: 5 GB or more».
- «Before installing Ubuntu Server Edition you should make sure all data on the system is backed up.»
- ISO de servidor desde releases.ubuntu.com; «the simplest and most common way is to create a bootable USB stick».
- Tecla de menú de arranque «Escape, F2, F10 or F12» según fabricante.
- Pasos: idioma; actualizar instalador; teclado; red («the installer attempts to configure wired network interfaces via DHCP»); proxy/mirror; almacenamiento «use an entire disk»; «Enter a username, hostname and password»; pantallas SSH y snap; reinicio.

### 9.2 Estructura y sistema de archivos (FHS)

Filesystem Hierarchy Standard 3.0, Linux Foundation, 19-03-2015 (https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html) — sigue siendo la última versión publicada [comprobado sólo que la URL es la 3.0; NO CONFIRMADO que no haya otra posterior].
- «This standard consists of a set of requirements and guidelines for file and directory placement under UNIX-like operating systems.»
- Directorios obligatorios en / (3.2): bin «Essential command binaries»; boot «Static files of the boot loader»; dev «Device files»; etc «Host-specific system configuration»; lib «Essential shared libraries and kernel modules»; media «Mount point for removable media»; mnt «Mount point for mounting a filesystem temporarily»; opt «Add-on application software packages»; run «Data relevant to running processes»; sbin «Essential system binaries»; srv «Data for services provided by this system»; tmp «Temporary files»; usr «Secondary hierarchy»; var «Variable data».
- Opcionales (3.3): home «User home directories (optional)»; root «Home directory for the root user (optional)».
- /proc: «Kernel and process information virtual filesystem» (6.1.5).
- NO CONFIRMADO: fusión de /bin en /usr/bin («merged /usr») en Ubuntu/Debian actuales; no se encontró en hier(7) leída. No afirmarlo.

Permisos (chmod(1), https://man7.org/linux/man-pages/man1/chmod.1.html):
- «The format of a symbolic mode is [ugoa...][[-+=][perms...]...], where perms is either zero or more letters from the set rwxXst». «the user who owns it (u), other users in the file's group (g), other users not in the file's group (o), or all users (a).»
- «A numeric mode is from one to four octal digits (0-7), derived by adding up the bits with values 4, 2, and 1. […] The first digit selects the set user ID (4) and set group ID (2) and restricted deletion or sticky (1) attributes. The second digit selects permissions for the user who owns the file: read (4), write (2), and execute (1)».

### 9.3 Usuarios y grupos

- passwd(5): «The /etc/passwd file is a text file that describes user login accounts for the system. It should have read permission allowed for all users […] but write access only for the superuser.» «Each line of the file describes a single user, and contains seven colon-separated fields: name:password:UID:GID:GECOS:directory:shell». Contraseñas sombra: «/etc/passwd has an 'x' character in the password field, and the encrypted passwords are in /etc/shadow, which is readable by the superuser only.»
- group(5): «The /etc/group file is a text file that defines the groups on the system. There is one entry per line, with the following format: group_name:password:GID:user_list».
- useradd(8): «useradd - create a new user or update default new user information». Opciones: «-d, --home-dir HOME_DIR»; «-g, --gid GROUP The name or the number of the user's primary group»; «-G, --groups GROUP1[,GROUP2,...] A list of supplementary groups»; «-m, --create-home Create the user's home directory if it does not exist»; «-s, --shell SHELL»; «-u, --uid UID […] This value must be unique, unless the -o option is used». Ficheros: /etc/passwd, /etc/shadow, /etc/group, /etc/gshadow, «/etc/default/useradd Default values for account creation», «/etc/skel/ Directory containing default files».
- NO leído: usermod, userdel, groupadd, passwd(1), sudo. Hueco.

### 9.4 Arranques y paradas

- bootup(7): «Immediately after power-up, the system firmware will do minimal hardware initialization, and hand control over to a boot loader (e.g. systemd-boot(7) or GRUB) […]. This boot loader will then invoke an OS kernel». «Nowadays this is implemented as an "initramfs" — a compressed CPIO archive that the kernel extracts into a tmpfs.» «After the root file system is found and mounted, the initrd hands over control to the host's system manager (such as systemd(1)) […] which is then responsible for probing all remaining hardware, mounting all necessary file systems and spawning all configured services.» Parada: «the system manager stops all services, unmounts all non-busy file systems […]. As a last step, the system is powered down.»
- systemd.special(7): «default.target The default unit systemd starts at bootup. Usually, this should be aliased (symlinked) to multi-user.target or graphical.target.» «multi-user.target A special target unit for setting up a multi-user system (non-graphical).» «graphical.target A special target unit for setting up a graphical login screen. This pulls in multi-user.target.» «rescue.target […] administer the system in single-user mode with all file systems mounted but with no services running, except for the most basic.» «emergency.target […] starts an emergency shell on the main console. […] It is the most minimal version of starting the system».
- shutdown(8): «shutdown may be used to halt, power off, or reboot the machine. The first argument may be a time string (which is usually "now").» Tiempo: «"hh:mm" […] specified in 24h clock format. Alternatively it may be in the syntax "+m" referring to the specified number of minutes m from now. "now" is an alias for "+0"». «-r, --reboot Reboot the machine.» «-c Cancel a pending shutdown.»
- NO CONFIRMADO: correspondencia niveles de ejecución SysV ↔ targets (runlevel3.target, etc.). No buscada.

### 9.5 Sistemas de ficheros y gestión de discos

- fdisk(8): «fdisk is a dialog-driven program for creation and manipulation of partition tables. It understands GPT, MBR, Sun, SGI and BSD partition tables.» «This division is recorded in the partition table, usually found in sector 0 of the disk.»
- mkfs(8): «This mkfs frontend is deprecated in favour of filesystem specific mkfs.<type> utils.» «mkfs is used to build a Linux filesystem on a device, usually a hard disk partition.»
- fstab(5): «The file fstab contains descriptive information about the filesystems the system can mount. fstab is only read by programs, and not written; it is the duty of the system administrator to properly create and maintain this file.» «on systemd-based systems, it's recommended to use systemctl daemon-reload after fstab modification.» Seis campos: 1.º fs_spec («the block special device, remote filesystem […] to be mounted»); 2.º fs_file («the mount point»); 3.º fs_vfstype («Linux supports many filesystem types: ext4, xfs, btrfs, f2fs, vfat, ntfs, hfsplus, tmpfs, sysfs, proc, iso9660, udf, squashfs, nfs, cifs […]»); 4.º fs_mntops (opciones); 5.º fs_freq («used by dump(8)»; «Defaults to zero (don't dump)»); 6.º fs_passno («used by fsck(8) to determine the order […] The root filesystem should be specified with a fs_passno of 1»).
- lvm(8): «The Logical Volume Manager (LVM) provides tools to create virtual block devices from physical devices.» «A Volume Group (VG) is a collection of one or more physical devices, each called a Physical Volume (PV). A Logical Volume (LV) is a virtual block device that can be used by the system or applications.»
- NO leído: mount(8), df/du, lsblk, parted, RAID (mdadm), swap. Hueco.

### 9.6 Administración del software

Ubuntu Server, «Package management» (https://documentation.ubuntu.com/server/how-to/software/package-management/):
- «Advanced Packaging Tool (APT), which can be used on the command line».
- «The APT package index is a database of available packages from the repositories defined in the /etc/apt/sources.list.d directory.» «Ubuntu repositories are defined in the /etc/apt/sources.list.d/ubuntu.sources file.» (versiones antiguas: «/etc/apt/sources.list»).
- Órdenes: `sudo apt update`; `sudo apt upgrade`; `sudo apt install nmap`; `sudo apt remove nmap`; «Adding the --purge option to apt remove will remove the package» [y su configuración, frase truncada: releer].
- «dpkg is a package manager for Debian-based systems. It can install, remove, and build packages, but unlike other package management systems, it cannot automatically download and install packages – or their dependencies.» `dpkg -l`; `dpkg -L ufw`.
- RPM/dnf: `dnf [options] install <spec>...` (dnf command reference). Hueco: rpm, snap, flatpak.

### 9.7 Salvaguarda y restauración

- GNU tar (manual 1.35.90, https://www.gnu.org/software/tar/manual/html_node/Synopsis.html): «You can use tar to store files in an archive, to extract them from an archive». Operaciones: «--create (-c)», «--extract (--get, -x)», «--list (-t)», «--append (-r)», «--update (-u)», «--compare (--diff, -d)», «--delete». «tar will make all file names relative (by removing leading slashes when archiving or restoring files), unless you specify otherwise (using the --absolute-names option).» «If you give the name of a directory […] tar acts recursively».
- Compresión (gzip.html): «--gzip -z gzip»; «--bzip2 -j bzip2»; «--xz -J xz».
- Incremental (Incremental-Dumps.html): «GNU tar currently offers two options for handling incremental backups: --listed-incremental=snapshot-file (-g snapshot-file) and --incremental (-G).» «The purpose of this file is to help determine which files have been changed, added or deleted since the last backup, so that the next incremental backup will contain only modified files.»
- rsync(1): «Rsync is a fast and extraordinarily versatile file copying tool. It can copy locally, to/from another host over any remote shell, or to/from a remote rsync daemon. […] It is famous for its delta-transfer algorithm, which reduces the amount of data sent over the network by sending only the differences».
- Restauración: `tar -x` (arriba). NO leído: dd, cpio, Déjà Dup, rsnapshot (aparece en Ubuntu pero no extractado).

### 9.8 grep, sed y awk

grep (GNU grep manual, https://www.gnu.org/software/grep/manual/grep.html):
- «Given one or more patterns, grep searches input files for matches to the patterns. When it finds a match in a line, it copies the line to standard output (by default)».
- «-i -y --ignore-case Ignore case distinctions in patterns and input data»; «-v --invert-match Invert the sense of matching, to select non-matching lines.»; «-w --word-regexp Select only those lines containing matches that form whole words.»; «-c --count Suppress normal output; instead print a count of matching lines for each input file.»; «-l --files-with-matches […] print the name of each input file»; «-n --line-number Prefix each line of output with the 1-based line number»; «-r --recursive»; «-E --extended-regexp Interpret patterns as extended regular expressions (EREs).»; «-F --fixed-strings Interpret patterns as fixed strings, not regular expressions.»

sed (GNU sed manual, https://www.gnu.org/software/sed/manual/sed.html):
- «A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline). […] sed works by making only one pass over the input(s), and is consequently more efficient. But it is sed's ability to filter text in a pipeline which particularly distinguishes it from other types of editors.»
- «The s command (as in substitute) is probably the most important in sed […]. The syntax of the s command is 's/regexp/replacement/flags'.» Flag «g Apply the replacement to all matches to the regexp, not just the first.»; «number Only replace the numberth match».
- «-n --quiet --silent By default, sed prints out the pattern space at the end of each cycle […]. These options disable this automatic printing». «-e script». «-i[SUFFIX] --in-place[=SUFFIX] This option specifies that files are to be edited in-place.» «-E -r --regexp-extended Use extended regular expressions».
- Comandos: «d Delete the pattern space; immediately start next cycle.» (`sed 2d`); «p Print out the pattern space […] usually only used in conjunction with the -n» (`sed -n 2p`).

awk (GNU Awk User's Guide, https://www.gnu.org/software/gawk/manual/html_node/):
- «The basic function of awk is to search files for lines (or other units of text) that contain certain patterns. When a line matches one of the patterns, awk performs specified actions on that line.» «awk programs are data driven».
- Uso: «awk 'program' input-file1 input-file2 ...»; patrones especiales BEGIN y END.
- Campos: «By default, fields are separated by whitespace»; «$1 refers to the first field, $2 to the second»; «$0 […] represents the whole input record»; «the last field in a record can be represented by $NF».
- Variables: «NF The number of fields in the current input record.» «NR The number of input records awk has processed since the beginning of the program's execution». «FS The input field separator». «OFS The output field separator».

---

## Tema 10 · Virtualización de sistemas y escritorios

Leído 05-10-2026. RTVE ya da hipervisor tipo 1/2, ventajas y contraste VM/contenedor (como oficio, sin
fuente): aquí se aporta la fuente oficial que les faltaba y lo nuevo (escritorio remoto/virtual,
aplicaciones, workspace, despliegue).

### 10.1 Virtualización de escritorio remoto: RDS

«Servicios de Escritorio remoto (RDS)», https://learn.microsoft.com/es-es/windows-server/remote/remote-desktop-services/remote-desktop-services-overview:
- «Servicios de Escritorio remoto (RDS) en Windows Server es una plataforma integrada para ofrecer de forma segura escritorios y aplicaciones administrados a los usuarios […]. Al centralizar el procesamiento en el centro de datos y el acceso remoto solo a la interfaz de usuario, el servicio de Escritorio remoto le ayuda a reducir la carga administrativa, mejorar la seguridad».
- «Los Servicios de Escritorio remoto admiten escritorios virtuales basados en servidor multisesión y escritorios virtuales de sesión única (o agrupados/personales), además de la publicación de aplicaciones individuales (RemoteApp).»
- Permite conectarse a «Un escritorio completo (basado en sesión o en máquina virtual).» y a «Aplicaciones específicas (programas remoteApp) que aparecen y se comportan como aplicaciones instaladas localmente.» «Los puntos de conexión simplemente presentan la interfaz de usuario remota mediante el Protocolo de escritorio remoto (RDP).»
- «Los datos permanecen en el centro de datos».
- Roles: «Host de sesión RD (RDSH) — Ejecuta escritorios de usuario basados en sesión y programas RemoteApp en Windows Server»; «Host de Virtualización de Escritorio Remoto — Hospeda colecciones de infraestructura de escritorio virtual (máquinas virtuales cliente windows agrupadas o personales). Se integra con Hyper-V»; «Agente de conexión de RD — Mantiene las sesiones de usuario, equilibra la carga de conexiones, vuelve a conectar usuarios a sesiones existentes»; «Acceso web de RD — Proporciona un portal web»; «RD Gateway — Habilita el acceso RDP seguro y cifrado a través de HTTPS (TCP 443) desde redes externas sin abrir puertos RDP internos»; «Licencias de Escritorio remoto — […] (CAL de RDS) necesarias para el uso legal (Usuario o Dispositivo).»
- NO CONFIRMADO: puerto RDP 3389 (no aparece en la página; RTVE tema 03 tiene puertos: comprobar allí).

### 10.2 Modelos de virtualización

**Escritorio virtual (VDI) en la nube — Azure Virtual Desktop** (https://learn.microsoft.com/es-es/azure/virtual-desktop/overview):
- «Azure Virtual Desktop es un servicio de escritorio y de virtualización de aplicaciones que se ejecuta en Azure.»
- «Ofrezca una experiencia completa de Windows con Windows 11, Windows 10 o Windows Server. Usa sesión única para asignar dispositivos a un solo usuario o usa varias sesiones para escalabilidad.» «Ofrezca escritorios completos o use RemoteApp para entregar aplicaciones individuales.» «Reemplace las implementaciones de Servicios de Escritorio remoto (RDS) existentes.» «Hospede escritorios y aplicaciones locales con el hipervisor de su elección con Azure Virtual Desktop Hybrid o Azure Virtual Desktop para Azure Local.»
- Aviso de vigencia: «Azure Virtual Desktop clásico se retira el 30 de septiembre de 2026.»
- Terminología (https://learn.microsoft.com/es-es/azure/virtual-desktop/terminology): «Un grupo de hosts es una colección de Azure máquinas virtuales que están registradas en Azure Virtual Desktop como hosts de sesión.» Tipos: «Personal, donde cada host de sesión se asigna a un usuario individual.» / «Agrupadas, donde las sesiones de usuario se pueden cargar con equilibrio de carga en cualquier host de sesión del grupo host. Puede haber varios usuarios diferentes en un único host de sesión al mismo tiempo.» «Un área de trabajo es una agrupación lógica de grupos de aplicaciones.» (= «workspace» en la consola inglesa).

**PC virtual / PC en la nube — Windows 365** (https://learn.microsoft.com/es-es/windows-365/overview):
- «Windows 365 es un software como servicio (SaaS) basado en la nube que crea automáticamente un nuevo tipo de máquina virtual Windows (PC en la nube) para los usuarios finales.»
- «Un equipo en la nube es una máquina virtual de alta disponibilidad, optimizada y escalable que proporciona a los usuarios finales una experiencia de escritorio de Windows enriquecida. El servicio Windows 365 lo hospeda y puede acceder a él desde cualquier lugar, en cualquier dispositivo.»
- Ediciones: Business («hasta 300 puestos»), Enterprise («integración completa con Microsoft Intune»), Government, Flex («hasta tres equipos en la nube para su uso no simultáneo»), para agentes (versión preliminar). «Windows 365 Link, el primer dispositivo de PC en la nube».
- AVISO DE INTERPRETACIÓN: el enunciado dice «PC virtual»; no hay definición normativa. Windows 365 llama a su producto «PC en la nube». Si el redactor usa «PC virtual» como máquina virtual de escritorio local (Hyper-V en Windows), es oficio: decláralo.

**Virtualización de aplicaciones**:
- App-V (https://learn.microsoft.com/es-es/windows/application-management/app-v/appv-for-windows): «El soporte extendido para MDOP finaliza el 14 de abril de 2026.» «El cliente de Windows App-V se encuentra en soporte extendido fijo.» «Te recomendamos que consultes Azure Virtual Desktop con la conexión de aplicaciones MSIX.» → a fecha de estudio App-V es tecnología en retirada.
- App Attach (https://learn.microsoft.com/es-es/azure/virtual-desktop/app-attach-overview): «App Attach permite adjuntar aplicaciones de forma dinámica desde un paquete de aplicación a una sesión de usuario en Azure Virtual Desktop. Las aplicaciones no se instalan localmente en hosts de sesión o imágenes». «Los usuarios pueden ejecutar varias versiones de la misma aplicación simultáneamente en el mismo host de sesión.»
- RemoteApp (arriba) = publicación de aplicaciones.
- Contenedores como aislamiento de aplicaciones: ver 10.4.

**Workspace virtual** [WF/búsqueda, releer]:
- Citrix (Tech Brief «Citrix Workspace», https://docs.citrix.com/en-us/tech-zone/learn/tech-briefs/citrix-workspace.html): «Citrix Workspace is a digital workspace solution that delivers secure and unified access to apps, desktops, and content (resources) from anywhere, on any device.» [resumen de búsqueda: releer la cita exacta].
- Omnissa Horizon 8 (antes VMware Horizon; https://docs.omnissa.com/Desktops-and-Applications-in-Horizon-V2406/DesktopsandApplicationsinHorizon8): grupos de escritorios de sesión única y escritorios/aplicaciones publicados en hosts RDS multisesión; «golden image» [resumen de búsqueda: releer].
- NO CONFIRMADO: definición neutral (de organismo, no de fabricante) de «workspace virtual». Hueco: el redactor debe presentarlo como término de fabricante.

### 10.3 Hipervisores (fuente oficial para lo que RTVE da como oficio)

- Hyper-V (https://learn.microsoft.com/es-es/windows-server/virtualization/hyper-v/overview): «Hyper-V es la tecnología de hipervisor de nivel empresarial de Microsoft integrada en Windows Server y Windows. […] Como hipervisor de tipo 1, Hyper-V se ejecuta directamente en el hardware informático, lo que proporciona un rendimiento casi nativo y un aislamiento sólido». «Admite una amplia gama de sistemas operativos para máquinas virtuales invitadas, incluidas muchas versiones de Windows, Linux y FreeBSD». «Hyper-V en Windows Server está diseñado para implementaciones empresariales con características avanzadas, como la migración en vivo, la alta disponibilidad y la recuperación ante desastres. Hyper-V en Windows proporciona […] una solución ligera adecuada para escenarios de desarrollo y pruebas.» Ventajas: «Optimización de costos» (consolidación), «Eficiencia operativa», «Agilidad empresarial», «Seguridad mejorada» (máquinas virtuales blindadas, arranque seguro, TPM 2.0).
- KVM (https://www.linux-kvm.org/page/Main_Page): «KVM (for Kernel-based Virtual Machine) is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V). It consists of a loadable kernel module, kvm.ko, that provides the core virtualization infrastructure and a processor specific module, kvm-intel.ko or kvm-amd.ko.»
- OJO: RTVE habla de «KVM sobre IP» (conmutador teclado-vídeo-ratón), que **no** es el hipervisor KVM. El redactor debe distinguirlos.
- VMware ESXi / vSphere: NO investigado (Broadcom). Hueco.

### 10.4 Contenedores

- Microsoft, «Contenedores frente a máquinas virtuales» (https://learn.microsoft.com/es-es/virtualization/windowscontainers/about/containers-vs-vm): «Un contenedor es un silo aislado y ligero para ejecutar una aplicación en el sistema operativo host. Los contenedores se basan en el kernel del sistema operativo host». «A diferencia de los contenedores, las máquinas virtuales ejecutan un sistema operativo completo, incluido su propio kernel». Aislamiento VM: «Proporciona aislamiento completo del sistema operativo host y de otras máquinas virtuales.» Contenedor: «Normalmente proporciona aislamiento ligero del host y otros contenedores, pero no proporciona un límite de seguridad tan sólido como una máquina virtual. (Puede aumentar la seguridad si usa el modo de aislamiento de Hyper-V […])». VM: «Ejecuta un sistema operativo completo, incluido el kernel, lo que requiere más recursos del sistema».
  → Esta es la fuente para la frase de RTVE «una máquina virtual lleva su propio sistema operativo completo; un contenedor comparte el núcleo del anfitrión». La frase de RTVE «El contenedor arranca en segundos» NO se ha confirmado.
- Docker (https://docs.docker.com/get-started/docker-overview/) [WF, releer]: «Docker is an open platform for developing, shipping, and running applications.» «An image is a read-only template with instructions for creating a Docker container.» «A container is a runnable instance of an image.» «Docker uses a client-server architecture. The Docker client talks to the Docker daemon».

### 10.5 Modos de despliegue: on-premise, cloud, híbrido

NIST SP 800-145, «The NIST Definition of Cloud Computing» (Mell y Grance, septiembre 2011; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf):
- «Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model is composed of five essential characteristics, three service models, and four deployment models.»
- Servicio: SaaS («to use the provider's applications running on a cloud infrastructure»), PaaS («to deploy onto the cloud infrastructure consumer-created or acquired applications»), IaaS («to provision processing, storage, networks, and other fundamental computing resources where the consumer is able to deploy and run arbitrary software, which can include operating systems»).
- Despliegue: «Private cloud. The cloud infrastructure is provisioned for exclusive use by a single organization […]. It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises.» «Community cloud.» «Public cloud. The cloud infrastructure is provisioned for open use by the general public. […] It exists on the premises of the cloud provider.» «Hybrid cloud. The cloud infrastructure is a composition of two or more distinct cloud infrastructures (private, community, or public) that remain unique entities, but are bound together by standardized or proprietary technology that enables data and application portability (e.g., cloud bursting for load balancing between clouds).»
- Encaje con el enunciado: on-premise = RDS/Hyper-V/Horizon en el CPD propio; cloud = Windows 365 (SaaS) / Azure Virtual Desktop; híbrido = AVD sobre Azure Local o AVD Hybrid (cita 10.2). Este encaje es interpretación del investigador: decláralo como tal.
- Azure Local (https://learn.microsoft.com/es-es/azure/azure-local/overview): «Azure Local es la solución de infraestructura distribuida de Microsoft que amplía las funcionalidades de Azure a entornos propiedad del cliente.» «admite implementaciones conectadas o desconectadas de la nube.»

---

## Tema 5 · Sistemas operativos: procesos, planificación, concurrencia

RTVE da funciones del SO, modos núcleo/usuario, tipos de núcleo y gestor de E/S **como teoría
clásica sin fuente**. Fuente aportada: manual universitario abierto R. H. Arpaci-Dusseau y A. C.
Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (OSTEP), Universidad de Wisconsin-Madison,
versión 1.10, © 2008–23 (capítulos en https://pages.cs.wisc.edu/~remzi/OSTEP/<cap>.pdf, leídos
05-10-2026; en inglés, traducción del redactor), más Microsoft Learn (Win32, es-es) para Windows y la
documentación del núcleo Linux.

### 5.1 Multiprogramación (intro.pdf, cap. 2)

- «multiprogramming became commonplace due to the desire to make better use of machine resources. Instead of just running one job at a time, the OS would load a number of jobs into memory and switch rapidly between them, thus improving CPU utilization. This switching was particularly important because I/O devices were slow; having a program wait on the CPU while its I/O was being serviced was a waste of CPU time.»
- «Understanding how to deal with the concurrency issues introduced by multiprogramming was also critical».

### 5.2 Proceso (cpu-intro.pdf, cap. 4)

- «a process is simply a running program».
- Virtualización de CPU / tiempo compartido: «By running one process, then stopping it and running another, and so forth, the OS can promote the illusion that many virtual CPUs exist when in fact there is only one physical CPU (or a few).» «time sharing of the CPU, allows users to run as many concurrent processes as they would like; the potential cost is performance».
- Estados: «Running: In the running state, a process is running on a processor.» «Ready: In the ready state, a process is ready to run but for some reason the OS has chosen not to run it at this given moment.» «Blocked: In the blocked state, a process has performed some kind of operation that makes it not ready to run until some other event takes place. A common example: when a process initiates an I/O request to a disk, it becomes blocked». Transiciones de la figura 4.2: «Scheduled» / «Descheduled» (listo↔ejecución), «I/O: initiate» (ejecución→bloqueado), «I/O: done» (bloqueado→listo). «there are some other states a process can be in, beyond running, ready, and blocked.»
- «process control block (PCB), which is really just a structure that contains information about a specific process.»
- Mecanismo/política: «The policy provides the answer to a which question; for example, which process should the operating system run right now?»
- Windows (https://learn.microsoft.com/es-es/windows/win32/procthread/processes-and-threads): «Una aplicación consta de uno o varios procesos. Un proceso, en los términos más sencillos, es un programa en ejecución. Uno o varios subprocesos se ejecutan en el contexto del proceso. Un subproceso es la unidad básica a la que el sistema operativo asigna tiempo de procesador.» «Una fibra es una unidad de ejecución que la aplicación debe programar manualmente.»
- Hilo (threads-intro.pdf, cap. 26): «thread is very much like a separate process, except for one difference: they share the same address space and thus can access the same data.»

### 5.3 Algoritmos de planificación (cpu-sched.pdf, cap. 7; cpu-sched-mlfq.pdf, cap. 8)

- Métricas: «turnaround time of a job is defined as the time at which the job completes minus the time at which the job arrived in the system» (T_turnaround = T_completion − T_arrival); «response time as the time from when the job arrives in a system to the first time it is scheduled» (T_response = T_firstrun − T_arrival).
- FIFO/FCFS: «The most basic algorithm we can implement is known as First In, First Out (FIFO) scheduling or sometimes First Come, First Served (FCFS).» Problema: «convoy effect […], where a number of relatively-short potential consumers of a resource get queued» [tras un consumidor pesado; frase partida en el PDF].
- SJF: «Shortest Job First (SJF) […] it runs the shortest job first, then the next shortest, and so on.»
- Apropiación: «Virtually all modern schedulers are preemptive, and quite willing to stop one process from running in order to run another.»
- STCF: «add preemption to SJF, known as the Shortest Time-to-Completion First (STCF) or Preemptive Shortest Job First (PSJF) scheduler».
- Round Robin: «instead of running jobs to completion, RR runs a job for a time slice (sometimes called a scheduling quantum) and then switches to the next job in the run queue.» «the length of the time slice is critical for RR. The shorter it is, the better the performance of RR under the response-time metric.»
- Colas multinivel con realimentación (MLFQ), reglas finales: «Rule 1: If Priority(A) > Priority(B), A runs (B doesn't).» «Rule 2: If Priority(A) = Priority(B), A & B run in round-robin fashion using the time slice (quantum length) of the given queue.» «Rule 3: When a job enters the system, it is placed at the highest priority (the topmost queue).» «Rule 4: Once a job uses up its time allotment at a given level (regardless of how many times it has given up the CPU), its priority is reduced» «Rule 5: After some time period S, move all the jobs in the system to the topmost queue.»
- Windows (https://learn.microsoft.com/es-es/windows/win32/procthread/scheduling-priorities): «Los niveles de prioridad van de cero (prioridad más baja) a 31 (prioridad más alta). Solo el subproceso de página cero puede tener una prioridad de cero.» «El sistema asigna segmentos de tiempo de forma round robin a todos los subprocesos con la prioridad más alta. […] Si un subproceso de prioridad más alta está disponible para ejecutarse, el sistema deja de ejecutar el subproceso de prioridad inferior (sin permitirle terminar de usar su intervalo de tiempo)». Prioridad base = «La clase de prioridad de su proceso» + «El nivel de prioridad del subproceso dentro de la clase».
- Cambio de contexto en Windows (…/context-switches): «El programador mantiene colas independientes de subprocesos ejecutables para cada nivel de prioridad.» Pasos: guardar contexto; «Si el subproceso permanece en un estado listo, colóquelo al final de la cola para su nivel de prioridad»; buscar la cola de mayor prioridad con listos; quitar el de cabeza, restaurar contexto y reanudar.
- Linux (https://docs.kernel.org/scheduler/sched-eevdf.html): «The "Earliest Eligible Virtual Deadline First" (EEVDF) was first introduced in a scientific publication in 1995. The Linux kernel began transitioning to EEVDF in version 6.6 (as a new option in 2024), moving away from the earlier Completely Fair Scheduler (CFS)». «Similarly to CFS, EEVDF aims to distribute CPU time equally among all runnable tasks with the same priority.» [AVISO: la doc dice «6.6 (as a new option in 2024)»; no se ha comprobado la fecha de publicación de 6.6. Dar sólo «desde la versión 6.6».]

### 5.4 Multitarea

- Windows (https://learn.microsoft.com/es-es/windows/win32/procthread/multitasking): «Un sistema operativo multitarea divide el tiempo de procesador disponible entre los procesos o subprocesos que lo necesitan. El sistema está diseñado para la multitarea preferente; asigna un segmento de tiempo de procesador a cada subproceso que ejecuta. El subproceso que se está ejecutando actualmente se suspende cuando transcurre su segmento de tiempo». «Dado que cada segmento de tiempo es pequeño (aproximadamente 20 milisegundos), aparecen varios subprocesos que se están ejecutando al mismo tiempo. Este es realmente el caso en sistemas multiprocesador».
- NO CONFIRMADO: definición de multitarea cooperativa (no apropiativa) con fuente. Sólo existe implícita en OSTEP («non-preemptive schedulers […] would run each job to completion before considering whether to run a new job» — fragmento: releer cpu-sched.pdf §7.5).

### 5.5 Concurrencia (threads-intro, threads-sema, threads-bugs)

- «race condition (or, more specifically, a data race): the results depend on the timing of the code's execution.» Resultado «indeterminate».
- «A critical section is a piece of code that accesses a shared variable (or more generally, a shared resource) and must not be concurrently executed by more than one thread.»
- Exclusión mutua: «mutual exclusion primitives; doing so guarantees that only a single thread ever enters a critical section, thus avoiding races, and resulting in deterministic program outputs.»
- Atomicidad: «atomic is simply expressed with the phrase "all or nothing"».
- Semáforo: «A semaphore is an object with an integer value that we can manipulate with two routines; in the POSIX standard, these routines are sem_wait() and sem_post()». (Cerrojos/locks: cap. 28, descargado, no extractado.)
- Interbloqueo: «Four conditions need to hold for a deadlock to occur»: «Mutual exclusion: Threads claim exclusive control of resources that they require (e.g., a thread grabs a lock).» «Hold-and-wait: Threads hold resources allocated to them […] while waiting for additional resources». «No preemption: Resources (e.g., locks) cannot be forcibly removed from threads that are holding them.» «Circular wait: There exists a circular chain of threads such that each thread holds one or more resources (e.g., locks) that are being requested by the next thread in the chain.» «If any of these four conditions are not met, deadlock cannot o[ccur]».
- NO investigado: monitores, paso de mensajes, problemas clásicos (productor-consumidor, filósofos), inanición. OSTEP los trata (cap. 30-31) si se quieren.

### 5.6 Componentes y estructura

- Lo de RTVE (núcleo, modos, tipos de núcleo, E/S) queda sin fuente: OSTEP sirve de apoyo genérico, pero no se ha extractado cita para «monolítico/micronúcleo/híbrido». NO CONFIRMADO con cita. El redactor lo mantiene como teoría clásica declarada, o lo verifica en OSTEP/otra fuente.

---

## Resumen de huecos (lo que no se pudo confirmar)

- T5: clasificación de núcleos sin cita; multitarea cooperativa; problemas clásicos de concurrencia.
- T6: procesamiento LSDOU y refresco de GPO; gpedit en Home; interfaz, personalización, Panel de control, conectividad de red y controladores de Windows 11 sin fuente; citas de support.microsoft.com sólo vía resumen [WF].
- T7: directiva de ejecución por defecto en Windows PowerShell 5.1; Move/Rename/Set-Content y alias.
- T8: definición de «árbol»; dsa.msc/ADAC con cita; VMs por edición; DFS, impresoras, permisos NTFS; Entra ID.
- T9: merged /usr; usermod/userdel/groupadd/sudo; mount, lsblk, RAID, swap; runlevels↔targets; RHEL vigente.
- T10: definición neutral de «workspace virtual» y «PC virtual»; VMware ESXi; RDP 3389; citas Citrix/Omnissa/Docker sólo vía resumen.

## Fuentes leídas (todas el 05-10-2026)

Microsoft Learn es-es (Windows 11, Windows Server, PowerShell, Win32, Azure Virtual Desktop, Windows 365,
Intune, ciclo de vida); support.microsoft.com (vía WebFetch); man7.org (passwd(5), group(5), shadow(5),
useradd(8), fstab(5), fdisk(8), mkfs(8), lvm(8), chmod(1), bootup(7), shutdown(8), systemd.special(7),
rsync(1)); FHS 3.0; GNU grep, sed, gawk y tar; Ubuntu (release-cycle, Server docs), Debian releases;
docs.kernel.org (EEVDF); OSTEP v1.10; NIST SP 800-145; linux-kvm.org; docs.docker.com (WebFetch);
docs.citrix.com y docs.omnissa.com (resultados de búsqueda).
Ficheros tocados: sólo este informe.
