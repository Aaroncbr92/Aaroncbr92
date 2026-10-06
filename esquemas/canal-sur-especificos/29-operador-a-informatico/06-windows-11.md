# Tema 6 del específico de Operador/a Informático · Sistema operativo Windows 11

**Siglas**: UEFI, TPM, GPT, MBR, ESP, MSR, WinRE, ADK, DISM, USMT, SIM, VAMT, WDS, WSUS, MDM, MAM, BYOD, GPO, UO, CSE, GPMC, RSoP, WMI, UAC, EFS, UNC, DoH, ELAM.

Esqueleto para repasar, no resumen: fuente delante de cada línea (L=Microsoft Learn; S=soporte de Microsoft).

<!-- indice -->
- [Versión](#versión-que-se-estudia)·[1](#1-instalación-del-cliente-windows)·[2](#2-interfaz-y-aplicaciones)·[3](#3-gestión-de-discos-y-controladores)·[4](#4-conectividad-de-red)·[5](#5-protección-y-recuperación-del-sistema)·[6](#6-configuración-de-la-seguridad)·[7](#7-centro-de-notificaciones)·[8](#8-personalización)·[9](#9-configuración-básica-y-avanzada)·[10](#10-partición-de-recuperación)·[11](#11-panel-de-configuración)·[12](#12-modo-desarrollador)·[13](#13-políticas-de-grupo-gpo)·[14](#14-puntos-de-restauración)·[15](#15-opciones-de-reinicio-para-instalar-actualizaciones)·[No da](#lo-que-este-tema-no-da)
<!-- /indice -->

## Versión que se estudia
- L:anual (2.ª mitad); 24 meses Home/Pro/Pro Workstations/Pro Education, 36 Enterprise/Education; seguridad acumulativa 2.º martes.
- L:26H2 29-09-2026 (no estudiada); 26H1 10-02-2026 (sólo equipos nuevos); 25H2 30-09-2025 (fin 12-10-2027/10-10-2028; última para equipos existentes el 24-09-2026; desde 24H2 paquete de habilitación); 24H2 fin 13-10-2026/12-10-2027; 23H2 Enterprise fin 10-11-2026. LTSC 2024 fin 09-10-2029. Windows 10 fin 14-10-2025 (22H2 última).

## 1. Instalación del cliente Windows
- L:mínimos: 1 GHz, 2+ núcleos, 64 bits/SoC; 4 GB; 64 GB; DirectX 12+WDDM 2.0; UEFI con arranque seguro; TPM 2.0; 720p 9" 8 bits; Internet.
- Home: Internet+cuenta Microsoft. Desde Windows 10: 2004+ y seguridad 14-09-2021+. Modo S sólo Home, irreversible. BitLocker To Go y Hyper-V (SLAT): Pro, Enterprise, Pro Education/SE, Education. VM: gen. 2, 64 GB, 4 GB, 2 procesadores, arranque seguro, TPM; gen. 1 no actualiza.
- L:sólo UEFI x64; arranque seguro=cargador comprobado; UEFI exige GPT; `MBR2GPT.EXE` convierte sin destruir, antes de pasar a UEFI.
- S:Windows Update (recomendado); Asistente; `setup.exe` (archivos y apps [defecto]/sólo archivos/nada); arrancar del medio=borra todo. Medio: `MediaCreationTool.exe`, USB ≥8 GB o ISO; clave 25 caracteres (no licencia digital).
- Limpia: F1-F12/SUPR; «No tengo una clave»; edición=licencia; borrar particiones del Disco 0 (no «Espacio sin asignar»), sólo disco 0; elimina todo. Activar tras reinstalar; cambio de placa puede desactivar.
- L:ADK: DISM (capturar, reparar, implementar imágenes); USMT (`ScanState.exe` copia, `LoadState.exe` restaura; 32→64 sí, inverso no); SIM (`Unattend.xml`); Diseñador de configuraciones (aprovisionamiento); VAMT (MAK/KMS); WinPE («lite»).
- WDS: PXE, multidifusión, desbloqueo de red BitLocker. WSUS: repositorio local. Autopilot: preconfigura, Pro→Enterprise. Intune: nube; MDM (dispositivo, borrado); MAM (apps, BYOD).

## 2. Interfaz y aplicaciones
- S:barra: Widgets (Win+W), Inicio, Buscar (Win+S), Vista de tareas (Win+Tab), Aplicaciones (línea=abierta), Bandeja. Centrada; centro/izquierda, nunca arriba/lateral. Inicio y Configuración rápida no se quitan.
- Inicio: anuncia 6 áreas, enumera 7 (Búsqueda, Chinchetas, Todas las aplicaciones, Recomendaciones, Todas, Cuenta, Compañero móvil); Win+X=Vínculo rápido.
- Acoplar: bordes/esquinas, Win+flecha, Win+Z; 3 columnas ≥1920 px.
- Atajos: Ctrl+Mayús+Esc tareas; Alt+F4; Alt+Tab; F2; Mayús+Supr sin papelera; Win+D, E, I, L, R; Win+V portapapeles (desactivado); Win+N notificaciones; Win+A Configuración rápida.
- Explorador: desde 22H2 carpetas conocidas ancladas, fuera de Este equipo. Misma unidad mueve, distinta copia; red/extraíble sin papelera.
- Desinstalar: Inicio>Todas las aplicaciones; Configuración>Aplicaciones instaladas; Panel de control>Programas y características; integradas no. Arranque: Configuración>Aplicaciones>Inicio o Administrador de tareas.
- L:`msiexec`: `/i`, `/x`, `/quiet`, `/passive` (barra), `/qn`, `/norestart`; `msiexec.exe /i "C:\example.msi"`. WinGet: tema 7.

## 3. Gestión de discos y controladores
- S:`diskmgmt.msc`, `compmgmt.msc`. C:, Sistema EFI, Recuperación (no tocar).
- Inicializar borra; Sin conexión→En línea; Operadores de copia/Administradores. Volumen simple: espacio sin asignar, NTFS. Formatear destruye (no el volumen de Windows); rápido=nueva tabla. RAID: Espacios de almacenamiento.
- GPT defecto, >2 TB, 128 particiones, UEFI. MBR: 32 bits/antiguos/extraíbles, arranque 2,2 TB, 4 principales o 3+extendida (lógicas), sin UEFI.
 básico (principales, extendidas, lógicas); dinámico (simples, distribuidos, seccionados, reflejados, RAID-5); dinámico→básico: eliminar antes volúmenes; no se borran sistema, arranque ni paginación.
- L:`diskpart`: administrador local; foco: `list`, `select`, `clean` (borra), `create`, `format`, `assign`, `extend`, `shrink`, `online`. Secuencia: `list disk`, `select disk=1`, `clean`, `convert gpt`, `create partition primary`, `format fs=ntfs quick`, `assign letter=e`. `Initialize-Disk`.
- L:`defrag`: semanal; SSD TRIM mensual (no cambia); `/o`. SNIA: TRIM=bloques en desuso.
- S:controladores: Windows Update mejor vía; Administrador de dispositivos: automático; manual (versión, arquitectura); desinstalar dispositivo y reiniciar reinstala; Propiedades>Controlador>«Revertir al controlador anterior»; sólo sitio del fabricante. Códigos 10, 22, 28, 43: tema 2.

## 4. Conectividad de red
- S:Wi-Fi vía Configuración rápida>Administrar conexiones Wi-Fi; «Administrar redes conocidas»; QR; MAC aleatorias. RDP: tema 10.
- Perfil: primera vez pública (recomendada: oculto, sin compartir); privada (visible, comparte). «Tipo de perfil de red».
- TCP/IP: DHCP recomendado; Editar junto a asignación de IP: Automático/Manual; IPv4 IP, máscara, puerta, DNS preferido/alternativo; IPv6 longitud de prefijo. DoH: plantilla automática; reserva a texto no cifrado sí/no; no en Windows 10.
- L:`ipconfig`: `/all`, `/release`, `/renew`, `/flushdns`,. `ping` (ICMP): `/t`; `/n` (4); `/l` (32); IP sí, nombre no=resolución de nombres. `tracert`: TTL creciente; 30 saltos, `/h`. `netstat`: sin parámetros TCP activas; `-a` TCP/UDP; `-n`; `-o` PID; `-r`=`route print`.
- L:UNC: `\\servidor\recurso\camino`; servidor NetBIOS, IP o FQDN (v4/v6); servidor+recurso=volumen; completas; relativas sólo con unidad asignada. `\\SRV7\C:\…` inválida; `\\SRV7\C$\…` válida (administrativo oculto); `\\192.168.100.7\Repositorio\Video.mp4` válida.

## 5. Protección y recuperación del sistema
- L:WinRE: sobre WinPE; preinstalado Home/Pro/Enterprise/Education. Herramientas: Reparación automática, Restauración a un momento dado, Restablecimiento mediante botón (Restablecer este PC), Recuperación de imágenes (sólo Server).
- Entrada: Mayús+Reiniciar; Configuración>Sistema>Recuperación>Inicio avanzado; medios; botón del fabricante. Automática: 2 fallos de arranque; 2 apagados inesperados o 2 reinicios en 2 min; error de arranque seguro (salvo Bootmgr.efi); error BitLocker en sólo táctiles. Menú: dispositivo, firmware (sólo UEFI).
- Sin contraseña de administrador; cifrados inaccesibles sin clave (BitLocker: de recuperación).
- S:Configuración de inicio: Solucionar problemas>Opciones avanzadas>Configuración de inicio>Reiniciar (BitLocker: clave). 1-9/F1-F9: 1 depuración; 2 registro (`ntbtlog.txt`); 3 vídeo baja resolución; 4 modo seguro; 5 con red; 6 con símbolo del sistema; 7 sin firmas de controladores; 8 sin ELAM; 9 sin reinicio automático. Salir: reiniciar; si no, `msconfig`>Arranque>quitar «Arranque seguro» (no el de UEFI).
- S:de menos a más (antes, copia): 1 solucionador; 2 reinstalar con Windows Update (22H2+); 3 desinstalar actualización (volver atrás 10 días); 4 momento dado (24H2+); 5 Restablecer este PC (muy perturbadora).
- Conserva: desinstalar actualización=archivos y apps; versión anterior=quita apps, controladores, configuración nuevos; Windows Update=todo; momento dado=todo vuelve al punto, OneDrive intacto; Restaurar sistema=archivos sí, cambios de sistema deshechos; Restablecer=archivos a elegir, apps y configuración fuera; medios=como `setup.exe`; unidad de recuperación=quita todo. `sfc /scannow`: tema 2.
- Recuperación rápida: 24H2+; Home activada, Pro/Enterprise la habilita TI; no restablece.
- Preparar: Copias de seguridad de Windows, clave BitLocker, unidad USB.

## 6. Configuración de la seguridad
- L:Seguridad de Windows: 7 secciones (virus y amenazas [ransomware, acceso controlado a carpetas]; cuentas; firewall y red; aplicaciones y explorador [SmartScreen]; dispositivo; rendimiento y estado; familiares). No se desinstala; Defender se deshabilita con antivirus de terceros; GPO/Intune/Configuration Manager prevalecen.
- L:BitLocker: volúmenes enteros; TPM (protector, integridad); PIN o clave de inicio=multifactor; sin TPM: clave USB o contraseña (desaconsejada, deshabilitada por defecto), sin integridad. TPM 1.2+; 2.0 no en BIOS heredado/CSM; SO en NTFS; unidad del sistema sin cifrar, FAT32 en UEFI. Pro, Enterprise, Pro Education/SE, Education.
- Cifrado de dispositivo: todas las versiones; desde 24H2 sin DMA ni HSTI; clave en Entra ID, AD DS o cuenta Microsoft; sólo cuentas locales=desprotegido; XTS-AES 128; `msinfo32` «Cumple con los requisitos previos». EFS: `cipher`, NTFS. Volumen=robo del soporte; fichero=otros usuarios.
- L:UAC: habilitado; dos tokens; credenciales (estándar)/consentimiento. Gris=administrativa o firmada; amarillo=sin firmar/no fiable; escudo=token completo; escritorio seguro. Deslizante de 4 (Panel de control>Sistema y seguridad), defecto la 2.ª; nunca notificar, desaconsejado.
- Cuentas: locales (sólo ese equipo); Microsoft (recomendada); profesional/educativa (BYOD). Configuración>Cuentas>Otros usuarios: Agregar (local: «Agregar un usuario sin una cuenta de Microsoft»), Cambiar tipo, Quitar (no borra la cuenta Microsoft). `compmgmt.msc`>Usuarios y grupos locales. `net user`: tema 8.
- L:integradas: Administrador deshabilitada, no se elimina ni bloquea (renombrar/deshabilitar), modo seguro la habilita si no hay otra. Invitado deshabilitada, contraseña en blanco; usuario nuevo=estándar.
- Hello: cara, huella, PIN (un dispositivo).

## 7. Centro de notificaciones
- S:Win+N; responder, expandir, borrar una/por aplicación/«Borrar todo».
- Configuración>Sistema>Notificaciones: por aplicación (banners, centro, ocultar en bloqueo, sonido, prioridad Superior/Alta/Normal; una sola Superior).
- No molestar: campana zZ; sólo alarmas, recordatorios y apps elegidas; automático con Foco.

## 8. Personalización
- S:Configuración>Personalización: temas, fondos, colores, bloqueo, Inicio, barra. Temas: `.deskthemepack`. Colores: claro, oscuro, personalizado; énfasis automático; claro no colorea Inicio, barra ni centro.

## 9. Configuración básica y avanzada
- S:Win+I. Categorías: Inicio, Sistema, Bluetooth y dispositivos, Red e Internet, Personalización, Aplicaciones, Cuentas, Hora e idioma, Juegos, Accesibilidad, Privacidad y seguridad, Windows Update.
- Herramientas: Administrador de tareas; Administración de equipos `compmgmt.msc`; Visor de eventos `eventvwr.msc`; `MSConfig`; `msinfo32`; `regedit` (copia antes); `gpedit.msc` (no Home).
- Servicios: Administración de equipos, `MSConfig`; oficio `services.msc`, dependencias. `Get-Service`, `-RequiredServices`, `-DependentServices`.

## 10. Partición de recuperación
- L:UEFI/GPT: sistema, MSR, Windows, recuperación. ESP: FAT32; 200 MB (512/512e), 300 MB (4K); sin herramientas WinRE. MSR 16 MB, sin identificador ni datos de usuario. Windows ≥20 GB, NTFS, 16 GB libres tras OOBE.
- Recuperación: `winre.wim` (`\Windows\System32\Recovery`)+personalizaciones+250 MB libres; guion `diskpart` del fabricante: 990 MB con 250 libres. Tipo `DE94BBA4-06D1-4D40-A16A-BFD50179D6AC`. Separada; justo tras Windows; datos después.
- Imagen nueva no cabe: contigua→Windows se reduce; si no, partición nueva y antigua huérfana; si no, WinRE en Windows.
- `diskpart` en WinPE: S, W, R; X reservada; tras reinicio C. No modificar.

## 11. Panel de configuración
- S:Configuración (simple, accesible; recomendada) frente a Panel de control (applets, compatibilidad, migrando); `control`. Aún en Panel: Programas y características; UAC; Restaurar sistema.

## 12. Modo desarrollador
- L:antes de 25H2 «Para desarrolladores»; 25H2: Configuración>Sistema>Avanzado>Para desarrolladores. Requiere administrador; la organización puede deshabilitarlo.
- Sustituye licencia de desarrollador; carga lateral (oficio), depuración. Device Portal sólo con «Enable Device Portal». Detección de dispositivos: mDNS, servidor SSH (no OpenSSH de Microsoft). `gpedit.msc` salvo Home; Home: `regedit`/PowerShell.

## 13. Políticas de grupo (GPO)
- L:local o AD DS; GPO=ajustes, permisos, ámbito; contenedor en dominio, plantilla en SYSVOL; GUID. Equipo/usuario; CSE aplica. `gpedit.msc` (no Home); GPMC.
- Vínculos: sitios, dominios, UO. Orden: 1 local, 2 sitio, 3 dominio, 4 UO (padres antes que hijas). Gana el más cercano; GPO invalida local; equipo invalida usuario;mismo contenedor: orden de vínculo más bajo gana; herencia ignorada con «aplicado» (forzado, a todas las UO) o bloqueo de herencia (no frena forzados).
- Filtrado: seguridad; WMI verdadero. Bucle invertido: combinación/reemplazo.
- Cuándo: equipo al arrancar, usuario al iniciar sesión; síncrono/asíncrono; ≤60 min; segundo plano 90 min+hasta 30 aleatorios; DC cada 5 min; redirección de carpetas sólo al iniciar sesión.
- `gpupdate`: `/force` (todo), `/target:computer|user`, `/boot`, `/logoff`. `gpresult`: RSoP; `/r`, `/h`, `/scope`; exige `/r`, `/v`, `/z`, `/x` o `/h`. `Invoke-GPUpdate`.
- Rutas: Configuración del equipo\Plantillas administrativas\Componentes de Windows\Windows Update; Opciones de seguridad; UAC; `.msi` por GPO.

## 14. Puntos de restauración
- S:Protección del sistema: instantáneas de sistema, apps, Registro, configuración; no habilitada por defecto, recomendada. Activar: `systempropertiesprotection.exe`>Configurar>Activar; automáticos en instalaciones/actualizaciones.
- Restaurar sistema: sistema, Registro, programas; sin tocar archivos personales; Panel de control>Recuperación o `rstrui.exe`; reinicia solo. WinRE: Solucionar problemas>Opciones avanzadas>Restaurar sistema (clave BitLocker).
- Momento dado: apps, configuración, archivos; 24H2+. No administrados: activada; TI: desactivada (26H2 la habilita); defecto con volumen ≥200 GB. Cada 24 h; 72 h; 2 % del disco; frecuencia/retención sólo Enterprise; sólo administradores locales. Configuración>Sistema>Recuperación; se aplica desde WinRE. Se pierden cambios posteriores.
- Probar primero momento dado; Restaurar sistema (10 y 11) si no está o punto de más de 3 días. No son copia (mismo disco).

## 15. Opciones de reinicio para instalar actualizaciones
- S(Configuración>Windows Update): Horas activas (Automáticamente/Manual); Programar el reinicio; Reiniciar ahora; Pausar 35 días; últimas actualizaciones en cuanto estén.
- KB5121772 (14-08-2026; 24H2, 25H2, 26H1): desde 28-07-2026 un reinicio al mes. Esperan: controladores de Windows Update, .NET, firmware. Inmediatas: inteligencia de Defender, componentes de IA, controladores críticos/acelerados, emergencia/fuera de banda. Fuera de horas activas. Funciones anuales; calidad más frecuentes.
- L:GPO, MDM o registro (no editar). «Configurar Novedades automática» (opción 4); «Desactivar reinicio automático…horas activas» (`ActiveHoursStart`/`ActiveHoursEnd`); «Especificar intervalo de horas activas…» (`ActiveHoursMaxRange`); «Especificar fecha límite antes del reinicio automático…» (2 a 14 días); «Mostrar opciones para las notificaciones de actualización» (0, 1, 2; `UpdateNotificationLevel`).
- Horas activas defecto 8:00-17:00; máx. 12 h (Windows 10 1607, Server 2016), 18 h después. 7 días sin reinicio: aviso. RDP: sólo sesiones activas. Directivas heredadas: no aplican.

## Lo que este tema no da
- Otros temas: 7 PowerShell, WinGet; 8 AD, `net user`; 2 `sfc`, averías; 10 RDP, Hyper-V; 14 antivirus, firewall, VPN; 3 copias; 11 Microsoft 365; 13 redes.
- No estudiado: 26H2; REAgentC; `.cpl`; Store. `services.msc`: oficio. No constan: versión y configuración de puestos RTVA/CSRTV.
