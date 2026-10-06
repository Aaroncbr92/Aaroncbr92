# Tema 10 del específico de Operador/a Informático · Virtualización de sistemas y escritorios

**Siglas**: MV, VMM, SO, SLAT, DEP, KVM, RPO, RDP, RDS, RDSH, CAL, NLA, MFA, VDI, AVD, App-V, MDOP, MSIX, SMB, SaaS/PaaS/IaaS, CPD, DaaS, ICA, HDX, NIST.

Esqueleto para repasar, no resumen: la fuente va delante de cada línea.

<!-- indice -->
- 1. Virtualización de sistemas
- 2. Virtualización de escritorio remoto
- 3. Modelos de virtualización
- 4. Modos de despliegue: on-premise, cloud e híbridos
<!-- /indice -->

## 1. Virtualización de sistemas

- NIST 800-125: virtualización = simulación del software/hardware sobre el que corre otro software (= MV). Completa: SO invitado en su MV. Hipervisor = VMM: reparte, aísla; invitado encapsulado, portable. Host/guest; SO anfitrión si va encima.
-
- NIST ventajas: eficiencia (más carga por equipo). Oficio: aprovechamiento, aislamiento, movilidad, instantáneas. Microsoft: consolidación; plantillas y PowerShell, horas a minutos; alta disponibilidad; instantáneas.
- NIST inconvenientes: más capas y controles; compromiso con mayor impacto; compartir = vector de ataque; entornos dinámicos. Oficio: anfitrión = punto único de fallo.
- Tipo 1 nativo (sobre hardware, servidores) / tipo 2 alojado (sobre SO, escritorio y pruebas). NIST: bare metal / hosted; los números 1 y 2 son de fabricantes.
- Tipo 1: Hyper-V (Microsoft, también en Windows 10/11), Xen (proyecto), ESXi (IBM), KVM y vSphere (Red Hat). Tipo 2: VirtualBox (Oracle, Red Hat), VMware Workstation (Red Hat).
- Xen: dominio 0 (drivers), DomU sin privilegios; PV introducida por Xen.
- NIST elección: seguridad (nativo, blanco menor); compatibilidad (nativo, menos NIC y gráficas); uso (alojado deja navegador y correo). Microsoft/VirtualBox: no dos hipervisores a la vez (VMware Workstation, VirtualBox).
- Hyper-V requisitos (Microsoft): 64 bits con SLAT (obligatoria; no para sólo herramientas); extensiones VMM; 4 GB RAM; virtualización en BIOS/UEFI (Intel VT, AMD-V); DEP (Intel XD, AMD NX). Se comprueba con `Systeminfo.exe`, sección Requisitos de Hyper-V; con hipervisor ya activo: «A hypervisor has been detected».
- Ediciones: Windows Server 2025 todas (Experiencia de escritorio, Server Core); Datacenter derechos ilimitados de MV. Windows 11: requisitos Pro o Enterprise; presentación Pro, Enterprise y Education; instalación Pro o Enterprise; no Home. Característica opcional, sin descarga.
- Instalar: `Install-WindowsFeature -Name Hyper-V -ComputerName <computer_name> -IncludeManagementTools -Restart`; Windows 11 `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All`; `DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V`; Panel de control, Activar o desactivar características de Windows (plataforma de Hyper-V, Herramientas de gestión). Server Core: sólo módulo PowerShell.
- Gestión: Hyper-V Manager, módulo PowerShell; a escala, Windows Admin Center, System Center VMM. PowerShell Direct = sin red.
- Funciones (Microsoft): generación 2 (UEFI, arranque seguro, TPM 2.0 virtual, BitLocker); blindada (BitLocker, arranque seguro, atestación TPM 2.0); migración en vivo; clúster de conmutación por error; Réplica (asincrónica, RPO desde 30 s); memoria dinámica; particiones de GPU; anidada; aislamiento de red (VLAN, conmutadores privados, SDN).
- Puntos de control (Microsoft): estándar = instantánea con memoria; producción = VSS (o inmovilización en Linux), sin memoria, predeterminado. Estándar: no es copia completa, incoherencia con Active Directory. Antes de Windows 10 sólo estándar (instantáneas). No sustituye a la copia (tema 3).
- Órdenes: `Checkpoint-VM -Name <VMName>`; `Get-VMCheckpoint -VMName <VMName>`; `Restore-VMCheckpoint -Name <checkpoint name> -VMName <VMName> -Confirm:$false`; `Set-VM -Name <vmname> -CheckpointType` Standard | Production (si falla, estándar) | ProductionOnly. Manager: «Crear punto de control y aplicar» guarda el actual; «Aplicar» no; irreversible.
- KVM (linux-kvm.org): virtualización completa en Linux x86 con Intel VT/AMD-V; `kvm.ko` + `kvm-intel.ko`/`kvm-amd.ko`; Linux o Windows sin modificar; núcleo desde Linux 2.6.20; espacio de usuario en QEMU desde 1.3. Red Hat: tipo 1; Amazon: híbrido, cerca del tipo 1.
- MV vs contenedor (Microsoft): contenedor = silo ligero con kernel del host, modo usuario, misma versión de SO (salvo aislamiento Hyper-V), aislamiento ligero, Docker u orquestador (Azure Kubernetes Service), el orquestador recrea al caer nodo. MV = SO completo con kernel, aislamiento completo, casi cualquier SO, conmutación por error del nodo. Aislamiento Hyper-V: contenedor en MV ligera. NIST: virtualización del SO.
- Docker: imagen = plantilla de sólo lectura; contenedor = instancia ejecutable; lo no persistente se pierde al eliminarlo; cliente-daemon.

## 2. Virtualización de escritorio remoto

- NIST: escritorio = un PC con varias instancias de SO; motivos: apps de otro SO, revertir, imagen buena; datos fuera de la imagen. Microsoft RDS: procesamiento en CPD, al usuario la interfaz por RDP, datos en el CPD.
- Escritorio remoto, host (Microsoft): Professional, Enterprise, Education, Windows Server; Home sólo cliente. Requisitos: equipo encendido y en red; habilitado; acceso de red; cuenta permitida; cortafuegos. Cambiar: Administradores.
- Windows 11: Inicio, Configuración, Sistema, Escritorio remoto = Activado; Usuarios de Escritorio remoto, Agregar. Cliente: `mstsc.exe` (nombre o IP) o Aplicación de Windows. Desde fuera: reenvío de puertos o VPN (oficio: VPN o puerta de enlace, no publicar el puerto).
- Puerto 3389 por defecto, cambiable. `Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name 'PortNumber'`; cambio con `Set-ItemProperty` (mismo valor) o Registro (decimal, reinicio); nueva regla de entrada (ejemplo TCP y UDP); conexión `pc1.contoso.com:3390`.
- NLA: autenticar antes de la sesión; recomendada; deshabilitar temporalmente con clientes antiguos.
- Aplicación de Windows: AVD, Windows 365, Dev Box, RDS, equipos; Windows, macOS, iOS/iPadOS, Android/ChromeOS, navegador, Meta Quest. Excepciones en Windows: RDS sigue con la aplicación Escritorio remoto; PC remotos en preliminar, MSTSC. Cuenta profesional o educativa salvo PC remoto.
- RDS (Windows Server): multisesión, sesión única (agrupados/personales), RemoteApp.
- Roles: RDSH (sesión y RemoteApp); Host de Virtualización (colecciones VDI, Hyper-V); Agente de conexión (sesiones, carga, reconexión, colecciones); Acceso web (portal); Puerta de enlace (RDP por HTTPS, TCP 443, sin abrir puertos RDP; MFA); Licencias (CAL usuario o dispositivo).
- Modelos RDS: sesión (comparten Windows Server; tareas, temporales; mayor densidad, menor coste); VDI agrupada (MV de un grupo, no persistente; densidad media); VDI personal (MV dedicada que conserva cambios; desarrolladores; densidad menor); híbrido (RDSH + VDI; no es CPD + nube).
- Ventajas: parches centralizados; coste por usuario; datos en CPD. Planificar: perfiles (móviles, redirección, terceros), GPU, red y latencia, apps multisesión. Ubicación: instalaciones o Azure (IaaS).
- KVM sobre IP (oficio): teclado, vídeo y ratón por red; equipos en el CPD. Frente a Escritorio remoto: consola física, sirve en BIOS/arranque, sin SO ni red. Ninguno virtualiza.

## 3. Modelos de virtualización

- Sin norma para los cuatro; NIST define escritorio y aplicaciones; PC virtual y workspace = fabricante.
- PC virtual 1 (oficio): MV de escritorio en el PC propio (VirtualBox tipo 2, Hyper-V en Windows 11 Pro); NIST «Desktop virtualization»; Microsoft: desarrollo y pruebas, Creación rápida. NIST cita VirtualPC (emulación); su uso en el enunciado es interpretación.
- Espacio aislado de Windows: entorno ligero y temporal; Windows 11 22H2 conserva datos en reinicios internos; Pro, Enterprise, Pro Education/SE, Education, no Home; red por defecto; una instancia; adjuntos sospechosos con red deshabilitada y carpeta de sólo lectura.
- PC virtual 2: Windows 365 (Microsoft), SaaS; PC en la nube 1:1 (Enterprise, Business, Government); creado al asignar licencia en grupo Microsoft Entra, no a mano; coste por usuario y mes. Ediciones: Business (hasta 300 puestos), Enterprise (Intune), Government, Flex (una licencia, hasta tres equipos, uso no simultáneo), agentes de IA (preliminar). Windows 365 Link = dispositivo.
- Escritorio virtual: RDS o AVD. Sesión única/multisesión; personal (conserva)/agrupado (no persistente).
- AVD (Microsoft): escritorio y apps en Azure; Windows 11, 10 o Server; escritorios o RemoteApp; reemplaza RDS; multisesión de Windows 11/10 Enterprise exclusiva de AVD y Windows Server; sin puerta de enlace ni agente propios; conexiones inversas, sin puertos de entrada; escalado automático.
- Términos AVD: grupo de hosts (MV de Azure de la misma imagen); personal (un host por usuario, sesiones: uno); agrupado (equilibrio de carga; amplitud primero o profundidad primero); grupo de aplicaciones (escritorio o apps de un grupo de hosts; Escritorio/RemoteApp; RemoteApp sólo en agrupados); área de trabajo (agrupa grupos de aplicaciones; cada uno asociado a una); sesión desconectada (vuelve a la misma).
- Personal: actualiza con Windows Update, Configuration Manager; perfil en disco del SO. Agrupado: nuevas imágenes; perfil en FSLogix.
- FSLogix: controlador de filtro redirige el perfil en el sistema de archivos; traslada datos entre hosts, reduce tiempos de inicio, sin perfiles móviles. Aviso: abril de 2026, Kerberos RC4 a AES-SHA1.
- Vigencia: AVD clásico se retira el 30-09-2026 (24-09-2026: seis días); vigente = Azure Resource Manager.
- Amazon WorkSpaces: Personal (persistente), Pool (no persistente). Cliente ligero: Amazon, terminal para VDI; IBM, endpoint barato, conecta al agente de conexión, no al hipervisor; NIST, navegador.
- Protocolos (de fabricante): RDP (Microsoft); HDX sobre ICA (Citrix; EDT sobre UDP, cae a TCP; UDP 2598 con fiabilidad de sesión, 1494 sin ella, 443 HDX Direct); Blast, PCoIP y RDP (Omnissa Horizon 8; Blast TCP y UDP, GPU virtual).
- Aplicaciones, NIST: API virtual, apps de una plataforma en otra; ejemplo JVM; sirve en vez de escritorio si el problema es una app.
- RemoteApp: corre en servidor (RDS/AVD), al usuario su ventana; vigente.
- App-V (Microsoft): apps Win32 entregadas desde servidores; MDOP, soporte extendido hasta 14-04-2026; cliente en soporte extendido fijo; sustituto: AVD con App Attach MSIX.
- App Attach (AVD, vigente): adjunta apps a la sesión, sin instalarlas; contenedores aislados; varias versiones; actualizar sin ventana; permisos por app y usuario. Paquetes MSIX (`.msix`, `.msixbundle`), Appx (`.appx`, `.appxbundle`), App-V (`.appv`); MSIX superconjunto de Appx. Imágenes en recurso SMB; CimFS, VHDX o VHD (VHD no recomendado); registro a petición por defecto.
- Workspace virtual (sin norma): Microsoft, área de trabajo; Amazon, WorkSpaces; Citrix, StoreFront Cloud (apps, escritorios, web y SaaS; Citrix Workspace app). Interpretación del tema: espacio único con una identidad, capa que agrega, no otra técnica.

## 4. Modos de despliegue: on-premise, cloud e híbridos

- NIST 800-145: nube = acceso por red, a demanda, a recursos compartidos configurables, rápido y con poco esfuerzo.
- Características: autoservicio bajo demanda; acceso amplio por red; agrupación de recursos (multi-tenant); elasticidad rápida; servicio medido.
- Servicios: SaaS (apps del proveedor, configuración limitada); PaaS (apps propias; controla apps y entorno); IaaS (procesamiento, almacenamiento, redes; controla SO, almacenamiento, apps; quizá cortafuegos del host). Microsoft: IaaS gestionas MV, SO y apps; PaaS sin MV ni SO; SaaS Microsoft 365, Dynamics 365.
- Despliegues: privada (una organización; on o off premises); comunitaria; pública (en instalaciones del proveedor); híbrida (dos o más infraestructuras unidas por tecnología de portabilidad; cloud bursting). Privada no es on-premise; CPD propio es nube privada sólo con las cinco características.
- On-premise: todo en el CPD propio (RDS sobre Hyper-V). Microsoft: control total del hardware, la red y los datos; el propietario de toda la pila. Riesgos: revisiones retrasadas, seguridad física insuficiente, monitorización incompleta, hardware obsoleto, copia y recuperación insuficientes.
- Cloud: Windows 365 = SaaS; AVD = sólo imagen y MV de sesión (entre IaaS y PaaS: interpretación del tema); RDS en MV de Azure = IaaS.
- DaaS (no NIST): IBM, escritorios completos desde la nube; Amazon, tercero que administra la VDI (WorkSpaces, «fully managed»); Citrix DaaS, nube pública y CPD en híbrido. Microsoft no lo usa para Windows 365 ni AVD.
- Responsabilidad (Microsoft), local/IaaS/PaaS/SaaS: datos, identidades y usuarios, cliente siempre; dispositivos, cliente, y compartida en SaaS; aplicaciones, cliente, cliente, compartida, compartida; controles de red, cliente, cliente, compartida, Microsoft; SO, cliente, cliente, Microsoft, Microsoft; hosts físicos, red física y CPD, cliente, Microsoft, Microsoft, Microsoft. Siempre propios datos e identidades; hipervisor de IaaS y PaaS, Microsoft.
- Híbrido: NIST; CPD + nube pública = uso común. Ejemplos: AVD Hybrid o AVD para Azure Local (conectado o desconectado, pago por núcleo físico); RDS ampliado con AVD vía Azure Local; Azure Site Recovery (Azure como sitio secundario de Hyper-V); Hyper-V en Azure Local, cargas entre local y Azure. Motivos: proceso local, resistencia de apps críticas, baja latencia, soberanía y normativa.

## Lo que el tema no da

- Infraestructura real de RTVA y CSRTV: no consta en documento publicado.
- VMware y Omnissa Horizon por dentro; Citrix Virtual Apps and Desktops; Xen más allá de tipo y dominio 0; Proxmox; cliente cero; gestión de KVM (QEMU, libvirt, `virsh`, `virt-manager`).
- Norma de PC virtual y workspace virtual; precios y licencias; RDP por dentro; AVD en IaaS o PaaS; Education en Hyper-V de Windows 11 (fuentes discrepan).
