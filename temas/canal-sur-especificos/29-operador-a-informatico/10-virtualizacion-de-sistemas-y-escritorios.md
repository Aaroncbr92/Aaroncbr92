# Tema 10 del específico de Operador/a Informático · Virtualización de sistemas y escritorios

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 10 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. Publicaciones especiales del Instituto Nacional de Normas y Tecnología de los Estados Unidos (NIST SP 800-125, de enero de 2011, sobre virtualización completa, y NIST SP 800-145, de septiembre de 2011, definición de computación en la nube); documentación de Microsoft Learn (Hyper-V, Escritorio remoto, Servicios de Escritorio remoto, Azure Virtual Desktop, Windows 365, App-V, App Attach, FSLogix, Azure Local, contenedores, responsabilidad compartida); manual de Oracle VirtualBox; página del proyecto KVM; documentación de Docker, de Amazon WorkSpaces y de Citrix; páginas del proyecto Xen, de Red Hat, de IBM, de Amazon Web Services y de la arquitectura de Omnissa Horizon 8 (ejemplos de hipervisor, cliente ligero, protocolos de visualización y DaaS). Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las páginas citadas, en línea el 05-10-2026 y leídas ese día (las añadidas en el remate, el 06-10-2026); las dos publicaciones del NIST, en su versión final |
| Extensión | 12.400 palabras aproximadamente (con tablas y órdenes) |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); Instituto Nacional de
Normas y Tecnología de los Estados Unidos (NIST, *National Institute of Standards and
Technology*) y sus publicaciones especiales (SP, *Special Publication*); máquina virtual (MV; en las
citas de Microsoft, VM, *virtual machine*); monitor de máquina virtual (VMM, *virtual machine
monitor*), otro nombre del hipervisor; sistema operativo (SO; en las citas inglesas, OS); unidad
central de proceso (CPU); unidad de procesamiento gráfico (GPU); memoria de acceso aleatorio (RAM);
interfaz de firmware extensible unificada (UEFI) y sistema básico de entrada y salida (BIOS); módulo
de plataforma segura (TPM); traducción de direcciones de segundo nivel (SLAT); tecnologías de
virtualización de Intel (Intel VT) y de AMD (AMD-V); máquina virtual basada en el núcleo (KVM,
*Kernel-based Virtual Machine*), el hipervisor de Linux, que no hay que confundir con el
conmutador de teclado, vídeo y ratón, que también se abrevia KVM; objetivo de punto de recuperación
(RPO, *recovery point objective*); protocolo de escritorio remoto (RDP, *Remote Desktop
Protocol*); Servicios de Escritorio remoto (RDS, *Remote Desktop Services*) y su host de sesión
(RDSH, *Remote Desktop Session Host*); licencia de acceso de cliente (CAL, *client access
license*); autenticación de nivel de red (NLA, *network level authentication*); autenticación
multifactor (MFA); seguridad de la capa de transporte (TLS); protocolo de internet (IP); ordenador personal (PC);
tecnologías de la información (TI); gigabyte (GB); bus serie universal (USB); herramienta de
administración y mantenimiento de imágenes de implementación (DISM, *Deployment Image Servicing and
Management*); QEMU, nombre del programa que incluye el componente de espacio de
usuario de KVM; protocolo de transferencia de hipertexto
seguro (HTTPS); protocolo de control de transmisión (TCP) y de datagramas de usuario (UDP); red
privada virtual (VPN); infraestructura de escritorio virtual (VDI, *virtual desktop
infrastructure*); Azure Virtual Desktop (AVD); virtualización de aplicaciones de Microsoft (App-V,
*Application Virtualization*), del paquete de optimización de escritorio de Microsoft (MDOP,
*Microsoft Desktop Optimization Pack*); formato de paquete de aplicaciones MSIX, nombre de producto;
disco duro virtual (VHD y su versión VHDX); bloque de mensajes del servidor (SMB), protocolo de
carpetas compartidas; software, plataforma e infraestructura como servicio (SaaS, PaaS e IaaS);
centro de proceso de datos (CPD); interfaz de programación de aplicaciones (API); escritorio como
servicio (DaaS, *desktop as a service*); arquitectura informática independiente (ICA, *Independent
Computing Architecture*), la de Citrix; HDX, Blast y PCoIP, nombres de protocolo o tecnología de
Citrix y de Omnissa; ESXi, nombre de producto de VMware; International Business Machines (IBM), la empresa. *On-premise* (en
las instalaciones, local) y *cloud* (nube) se usan como los usa el enunciado.

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 10): «Virtualización de
> sistemas y escritorios: virtualización de escritorio remoto, modelos de virtualización —PC
> virtual, escritorio virtual, virtualización de aplicaciones y workspace virtual— y modos de
> despliegue on-premise, cloud e híbridos.»

Qué se puede preguntar: qué es virtualizar y qué es un hipervisor; qué distingue un hipervisor de
tipo 1 (nativo, *bare metal*) de uno de tipo 2 (alojado) y de qué tipo son Hyper-V, VirtualBox,
Xen, VMware ESXi y VMware Workstation;
qué ventajas e inconvenientes tiene la virtualización; qué exige el procesador para Hyper-V, en qué
ediciones de Windows 11 se puede activar y con qué orden; qué es un punto de control y qué
diferencia el estándar del de producción; qué es KVM en Linux; qué separa una máquina virtual de un
contenedor; qué puerto usa por defecto el Escritorio remoto, qué ediciones de Windows pueden
recibir conexiones, qué es la NLA y con qué cliente se conecta uno; qué roles tiene RDS (host de
sesión, host de virtualización, agente de conexión, acceso web, puerta de enlace, licencias) y por
qué puerto sale la puerta de enlace; qué distingue el escritorio basado en sesión de la VDI
agrupada y de la personal; qué son un PC en la nube (Windows 365), Azure Virtual Desktop, un grupo
de hosts y un área de trabajo; qué es un cliente ligero; qué protocolo de visualización usa cada
fabricante (RDP, HDX/ICA, Blast, PCoIP); qué es el DaaS; qué es RemoteApp, qué fue App-V y qué es App Attach; qué hace
FSLogix; qué es el KVM sobre IP; cómo define el NIST la nube, sus cinco características, sus tres
modelos de servicio y sus cuatro de despliegue; qué es una nube híbrida; y qué responsabilidades
conserva el cliente en cada modelo. En la aplicación práctica: activar Hyper-V y crear un punto de
control antes de un cambio; abrir el Escritorio remoto de un equipo y cambiar su puerto; elegir
entre sesión compartida, VDI agrupada, VDI personal o PC en la nube para un perfil de usuario;
diagnosticar por qué un usuario pierde su perfil en un escritorio agrupado; y decidir si un
servicio va en el CPD propio, en la nube o en un modelo híbrido.

<!-- indice -->

## Índice

- [1. Virtualización de sistemas](#1-virtualización-de-sistemas)
  - [Qué es virtualizar](#qué-es-virtualizar)
  - [Por qué se virtualiza: ventajas e inconvenientes](#por-qué-se-virtualiza-ventajas-e-inconvenientes)
  - [El hipervisor: tipo 1 y tipo 2](#el-hipervisor-tipo-1-y-tipo-2)
  - [Hyper-V: requisitos e instalación](#hyper-v-requisitos-e-instalación)
  - [Hyper-V: lo que un operador debe reconocer](#hyper-v-lo-que-un-operador-debe-reconocer)
  - [Puntos de control (instantáneas)](#puntos-de-control-instantáneas)
  - [KVM, el hipervisor de Linux](#kvm-el-hipervisor-de-linux)
  - [Máquinas virtuales y contenedores](#máquinas-virtuales-y-contenedores)
- [2. Virtualización de escritorio remoto](#2-virtualización-de-escritorio-remoto)
  - [Virtualizar el escritorio: local o remoto](#virtualizar-el-escritorio-local-o-remoto)
  - [Escritorio remoto de un equipo: RDP](#escritorio-remoto-de-un-equipo-rdp)
  - [Servicios de Escritorio remoto (RDS)](#servicios-de-escritorio-remoto-rds)
  - [KVM sobre IP](#kvm-sobre-ip)
- [3. Modelos de virtualización](#3-modelos-de-virtualización)
  - [Una advertencia de vocabulario](#una-advertencia-de-vocabulario)
  - [PC virtual](#pc-virtual)
  - [Escritorio virtual (VDI)](#escritorio-virtual-vdi)
  - [Virtualización de aplicaciones](#virtualización-de-aplicaciones)
  - [Workspace virtual](#workspace-virtual)
  - [Los cuatro modelos, frente a frente](#los-cuatro-modelos-frente-a-frente)
- [4. Modos de despliegue: on-premise, cloud e híbridos](#4-modos-de-despliegue-on-premise-cloud-e-híbridos)
  - [La nube según el NIST](#la-nube-según-el-nist)
  - [On-premise: en las instalaciones](#on-premise-en-las-instalaciones)
  - [Cloud: en la nube](#cloud-en-la-nube)
  - [Híbrido](#híbrido)
  - [Cómo se elige: los tres modos frente a frente](#cómo-se-elige-los-tres-modos-frente-a-frente)
  - [Caso práctico](#caso-práctico)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Virtualización de sistemas

### Qué es virtualizar

El NIST define la virtualización en general: **«Virtualization is the simulation of the software
and/or hardware upon which other software runs. This simulated environment is called a virtual
machine (VM).»** (la virtualización es la simulación del software o del hardware sobre el que
funciona otro software; ese entorno simulado se llama máquina virtual). Y distingue formas según la
capa que se simula: **«There are many forms of virtualization, distinguished primarily by computing
architecture layer.»**

La que interesa en este epígrafe es la virtualización completa, la de sistemas: **«In full
virtualization, one or more OSs and the applications they contain are run on top of virtual
hardware. Each instance of an OS and its applications runs in a separate VM called a guest
operating system.»** (uno o varios sistemas operativos, con sus aplicaciones, funcionan sobre
hardware virtual; cada uno, en su propia máquina virtual, que se llama sistema operativo invitado).

La idea, en una línea: un solo equipo físico ejecuta varias máquinas completas, cada una con su
propio sistema operativo, gracias a una capa que reparte el soporte físico entre ellas.

Esa capa es el hipervisor: **«The guest OSs on a host are managed by the hypervisor, also called
the virtual machine monitor (VMM), which controls the flow of instructions between the guest OSs and
the physical hardware, such as CPU, disk storage, memory, and network interface cards.»** El
hipervisor reparte y aísla: **«The hypervisor can partition the system’s resources and isolate the
guest OSs so that each has access to only its own resources»**, además de un posible acceso a
recursos compartidos, como ficheros del sistema anfitrión. Y cada invitado se puede llevar de
un sitio a otro: **«each guest OS can be completely encapsulated, making it portable»**.

El vocabulario que hay que manejar: el equipo físico es el anfitrión (*host*); cada sistema que
corre encima es un invitado (*guest*); cuando el hipervisor funciona encima de otro sistema, ese
sistema es el sistema operativo anfitrión: **«Some hypervisors run on top of another OS, which is
known as the host operating system.»**

Lo que ve cada invitado es un ordenador corriente: **«each guest OS appears to have its own
hardware, like a regular computer»**, con su CPU, su memoria, su almacenamiento y controladoras de
almacenamiento, sus controladoras Ethernet, su pantalla y sonido, y su teclado y ratón. Muchos
entornos añaden controladoras USB y puertos serie y paralelo.

Dos variantes que conviene reconocer por el nombre:

- *Paravirtualización*: el hipervisor ofrece al invitado interfaces propias en lugar de las del
  hardware normal (**«a method for the hypervisor to offer interfaces to the guest OS that the guest
  OS can use instead of the normal hardware interfaces»**), que son **«significantly faster»** para
  discos y red si el invitado las sabe usar.
- *Emulación de hardware*: **«Hardware emulation (sometimes called hardware translation) is a type
  of hosted virtualization.»** El hipervisor presenta un hardware distinto del físico y por eso
  puede ejecutar sistemas hechos para otra plataforma.

### Por qué se virtualiza: ventajas e inconvenientes

El NIST pone en cabeza la eficiencia: **«One of the most common reasons for adopting full
virtualization is operational efficiency: organizations can use their existing hardware (and new
hardware purchases) more efficiently by putting more load on each computer.»**

Qué gana una organización con ello, que es lo preguntable:

- Aprovechamiento: un servidor físico dedicado a un solo servicio pasa la mayor parte del
  tiempo ocioso.
- Aislamiento: si una máquina virtual cae, las demás siguen.
- Movilidad: una máquina virtual se copia, se mueve de anfitrión y se restaura como un
  fichero.
- Instantáneas: se puede volver al estado anterior a un cambio.

Microsoft enumera las mismas ventajas al presentar Hyper-V, con más detalle. La de costes:
**«reduzca los costos de adquisición y mantenimiento de hardware a través de la consolidación del
servidor, al tiempo que reduce los requisitos de espacio, energía y refrigeración del centro de
datos.»** La de operación: **«Las plantillas de máquina virtual y la automatización de PowerShell
reducen el tiempo de implementación de horas a minutos.»** La de continuidad: **«minimice el tiempo
de inactividad a través de características de alta disponibilidad, implemente estrategias de
recuperación ante desastres completas con Hyper-V Réplica y garantice la continuidad empresarial con
las funcionalidades de migración en vivo.»** Y la de pruebas: **«La capacidad de realizar
instantáneas de máquinas virtuales antes de realizar cambios proporciona una red de seguridad para
escenarios de experimentación y reversión»**.

Los inconvenientes, que el tribunal también puede pedir, los da el NIST:

- Más capas, más trabajo de seguridad: **«Virtualization adds layers of technology, which can
  increase the security management burden by necessitating additional security controls.»**
- Todos los huevos en la misma cesta: **«combining many systems onto a single physical computer can
  cause a larger impact if a security compromise occurs.»**
- Compartir es cómodo y peligroso: **«some virtualization systems make it easy to share information
  between the systems; this convenience can turn out to be an attack vector if it is not carefully
  controlled.»**
- Entornos que cambian deprisa: **«In some cases, virtualized environments are quite dynamic, which
  makes creating and maintaining the necessary security boundaries more complex.»** (en algunos
  casos, los entornos virtualizados son muy dinámicos, y eso complica crear y mantener los límites
  de seguridad necesarios).

A eso se suma, como oficio, que el anfitrión se convierte en un punto único de fallo: si cae, caen
todos sus invitados, salvo que haya un clúster que los arranque en otro (lo que Microsoft llama
conmutación por error, más abajo).

### El hipervisor: tipo 1 y tipo 2

Los dos tipos de esa capa:

| Tipo | Dónde se instala | Para qué |
|---|---|---|
| De tipo 1, nativo | Directamente sobre el soporte físico | Servidores de producción |
| De tipo 2, alojado | Sobre un sistema operativo ya instalado | Escritorio y pruebas |

El NIST los llama virtualización *bare metal* (o nativa) y virtualización alojada (*hosted*): **«In
bare metal virtualization, also known as native virtualization, the hypervisor runs directly on the
underlying hardware, without a host OS; the hypervisor can even be built into the computer’s
firmware. In the other form of full virtualization, known as hosted virtualization, the hypervisor
runs on top of the host OS»**. Y confirma el uso típico de cada uno: **«Servers are most often
virtualized on computers using bare metal virtualization. Desktops are most often virtualized on
computers with hosted virtualization.»**

Los números «tipo 1» y «tipo 2» no están en el NIST; los usan los fabricantes. El manual de
VirtualBox los asocia expresamente: **«Oracle VirtualBox is a so-called hosted hypervisor, sometimes
referred to as a type 2 hypervisor. Whereas a bare-metal or type 1 hypervisor runs directly on the
hardware, Oracle VirtualBox requires an existing OS to be installed.»** Microsoft clasifica Hyper-V
en el otro: **«Como hipervisor de tipo 1, Hyper-V se ejecuta directamente en el hardware informático,
lo que proporciona un rendimiento casi nativo y un aislamiento sólido para cargas de trabajo
virtualizadas.»** La página de Microsoft que lo dice se aplica a Windows Server y también a
Windows 10 y 11, y no hace distingo: Hyper-V es de tipo 1 también cuando se activa en un Windows de
escritorio.

Los ejemplos de cada tipo fuera de Microsoft, que son la pregunta de test más previsible, con la
fuente que los clasifica:

| Producto | Tipo | Quién lo dice |
|---|---|---|
| Xen (proyecto Xen) | 1 | El propio proyecto: **«The Xen Project hypervisor is an open-source type-1 or baremetal hypervisor»** |
| VMware ESXi | 1 | IBM: **«VMware ESXi (Elastic Sky X Integrated) is a type 1 (or bare-metal) hypervisor targeting server virtualization in the data center.»** |
| KVM, Hyper-V y VMware vSphere | 1 | Red Hat: **«KVM, Microsoft Hyper-V, and VMware vSphere are examples of a type 1 hypervisor.»** |
| VMware Workstation y Oracle VirtualBox | 2 | Red Hat: **«VMware Workstation and Oracle VirtualBox are examples of a type 2 hypervisor.»** |

Xen tiene un rasgo propio: encima del hipervisor arranca una primera máquina con privilegios, el
dominio 0, que maneja los dispositivos: **«A special domain, called domain 0 contains the drivers for
all the devices in the system.»** Las demás máquinas, sin acceso al hardware, se llaman por eso
**«unprivileged domain (or DomU)»**. Y el proyecto se atribuye la paravirtualización: **«PV is a
software virtualization technique originally introduced by the Xen Project»**.

Cómo se elige, según el NIST:

- Seguridad: el hipervisor nativo es un blanco más pequeño. **«Adding a hypervisor on top of a host
  OS adds more complexity and more vulnerabilities to the host. However, a hypervisor is much simpler
  and smaller than a host OS, so it provides a smaller target.»**
- Compatibilidad: el alojado funciona en más equipos. **«bare metal hypervisors run on a much more
  limited range of hardware than hosted hypervisors; for example, bare metal hypervisors often work
  on only a limited number of Ethernet controllers and graphics cards.»**
- Uso del equipo: con el alojado, el usuario sigue trabajando en su sistema. **«Hosted virtualization
  architectures also allow users to run applications such as web browsers and email clients
  alongside the hosted virtualization application, unlike bare metal architectures, which can only
  run applications within virtualized systems.»**

Un aviso práctico de Microsoft: dos hipervisores en el mismo equipo se estorban. Antes de instalar
Hyper-V hay que comprobar que no se van a usar **«aplicaciones de virtualización de terceros que
dependen de las mismas características de procesador que Hyper-V requiere. Entre los ejemplos se
incluyen la estación de trabajo de VMware y VirtualBox.»** VirtualBox dice lo mismo desde el otro
lado: **«do not attempt to run virtual machines from competing hypervisors at the same time.»**

### Hyper-V: requisitos e instalación

Requisitos de hardware (la virtualización asistida y la prevención de ejecución se activan en la
BIOS o UEFI):

- **«Un procesador de 64 bits con traducción de direcciones de segundo nivel (SLAT)»**; Microsoft
  subraya que **«la traducción de direcciones de segundo nivel (SLAT) ahora es obligatoria, no
  recomendada.»** La SLAT hace falta para instalar el hipervisor, no para instalar sólo las
  herramientas de administración (Administrador de Hyper-V, cmdlets).
- **«Extensiones del modo monitor de máquina virtual.»**
- Memoria: **«Planee al menos 4 GB de RAM.»**
- **«La compatibilidad con la virtualización está activada en el BIOS o UEFI»**: la virtualización
  asistida por hardware, **«específicamente procesadores con tecnología de virtualización Intel
  (Intel VT) o amd Virtualization (AMD-V) tecnología.»**
- **«La prevención de ejecución de datos (DEP) mediante hardware tiene que estar disponible y
  habilitada. En los sistemas Intel, es el bit XD (bit para deshabilitar la ejecución). En los
  sistemas AMD, es el bit NX (bit de no ejecución).»**

La comprobación se hace con una orden: **`Systeminfo.exe`**, y se mira la sección «Requisitos de
Hyper-V»; **«Si todos los requisitos de Hyper-V enumerados tienen un valor sí, el sistema puede
ejecutar el rol de Hyper-V.»** En un equipo donde Hyper-V ya funciona, la sección sólo dice
**«A hypervisor has been detected. Features required for Hyper-V will not be displayed.»**

Ediciones. En Windows Server, **«Hyper-V está disponible fácilmente como rol de servidor en todas
las ediciones de Windows Server 2025»**, tanto con Experiencia de escritorio como en Server Core. La
edición Datacenter da **«derechos ilimitados de máquina virtual»**. En el Windows de escritorio, la
página de requisitos dice **«Windows 11 Professional o Enterprise»** y la de presentación dice que
**«Para Windows 11, Hyper-V se incluye en las ediciones Pro, Enterprise y Education»**; la de
instalación da Pro o Enterprise, como la de requisitos. Las tres coinciden en lo que se pregunta, y
la de instalación lo dice expresamente: **«El rol Hyper-V no se puede instalar en Windows 10 Home o
Windows 11 Home.»** Y **«Hyper-V está integrado en Windows como una característica opcional; no hay ninguna
descarga Hyper-V.»**

Cómo se instala:

| Dónde | Orden o camino |
|---|---|
| Windows Server, PowerShell | **`Install-WindowsFeature -Name Hyper-V -ComputerName <computer_name> -IncludeManagementTools -Restart`** (sin `-ComputerName` si se trabaja en el propio servidor) |
| Windows Server, gráfico | Administrador del servidor, **«Agregar roles y características»**, rol Hyper-V |
| Windows 11, PowerShell | **`Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All`** |
| Windows 11, DISM | **`DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V`** |
| Windows 11, gráfico | Panel de control, Programas, Programas y características, **«Activar o desactivar características de Windows»**, Hyper-V |

Las dos piezas que aparecen en «Activar o desactivar características de Windows» son **«plataforma de
Hyper-V»** y **«Herramientas de gestión Hyper-V»**. En Server Core, `-IncludeManagementTools` sólo
instala el módulo de PowerShell y la consola gráfica se usa desde otro equipo.

Herramientas de administración: **«Hyper-V Manager proporciona una administración gráfica intuitiva
para las operaciones diarias, mientras que el módulo Hyper-V para Windows PowerShell habilita
escenarios avanzados de scripting y automatización.»** A escala están Windows Admin Center y System
Center Virtual Machine Manager. Y una que se pregunta por el nombre: **«PowerShell Direct permite la
administración segura de máquinas virtuales sin conectividad de red»**.

### Hyper-V: lo que un operador debe reconocer

| Función | Qué es, según Microsoft |
|---|---|
| Generación 2 | **«Las máquinas virtuales de generación 2 ofrecen seguridad mejorada con firmware UEFI, funcionalidades de arranque seguro y resistencia mejorada al malware.»** Admiten TPM 2.0 virtual y BitLocker en el invitado |
| Máquina virtual blindada | Protección **«a través del cifrado de BitLocker, la comprobación de arranque seguro y la atestación de TPM 2.0»** |
| Migración en vivo | **«La migración en vivo permite el mantenimiento planeado sin interrupción del servicio.»** |
| Clúster de conmutación por error | **«permiten la conmutación automática por error de máquinas virtuales entre nodos de clúster»** |
| Hyper-V Réplica | **«replicación asincrónica de máquinas virtuales en sitios secundarios»**; **«Los objetivos de punto de recuperación (RPO) pueden ser tan bajos como 30 segundos»** |
| Memoria dinámica | **«ajusta automáticamente la asignación de memoria en función de las demandas reales de carga de trabajo»** |
| Particiones de GPU | **«permite que varias máquinas virtuales compartan recursos de GPU»** |
| Virtualización anidada | **«permite ejecutar hipervisores dentro de máquinas virtuales»** |
| Aislamiento de red | **«REDES virtuales (VLAN), conmutadores virtuales privados y redes definidas por software (SDN)»** (sic: la traducción pone «REDES virtuales» por *virtual LAN*) |

### Puntos de control (instantáneas)

**«Una de las grandes ventajas de la virtualización es la capacidad de guardar fácilmente el estado
de una máquina virtual. En Hyper-V esto se realiza mediante el uso de puntos de control de máquina
virtual.»** Se hacen antes de un cambio: **«antes de realizar cambios en la configuración de
software, aplicar una actualización de software o instalar software nuevo.»**

Hay dos tipos:

| Tipo | Qué guarda |
|---|---|
| Estándar | **«toma una instantánea de la máquina virtual y el estado de memoria de la máquina virtual en el momento en que se inicia el punto de control.»** |
| De producción | **«usa el servicio de instantáneas de volumen o la inmovilización del sistema de archivos en una máquina virtual Linux para crear una copia de seguridad coherente con los datos de la máquina virtual. No se toma ninguna instantánea del estado de memoria de la máquina virtual.»** |

Tres datos que caen en test:

- **«Los puntos de control de producción se seleccionan de forma predeterminada»**.
- Del punto de control estándar advierte: **«Una instantánea no es una copia de seguridad completa
  y puede causar problemas de coherencia de datos con sistemas que replican datos entre distintos
  nodos, como Active Directory.»** Un punto de control no sustituye a la copia de seguridad del
  tema 3.
- El nombre antiguo: **«Hyper-V solo ofrecía puntos de control estándar (anteriormente denominados
  instantáneas) antes de Windows 10.»**

Las órdenes:

| Qué | Orden |
|---|---|
| Crear un punto de control | **`Checkpoint-VM -Name <VMName>`** |
| Listarlos | **`Get-VMCheckpoint -VMName <VMName>`** |
| Aplicar uno | **`Restore-VMCheckpoint -Name <checkpoint name> -VMName <VMName> -Confirm:$false`** |
| Cambiar el tipo | `Set-VM -Name <vmname> -CheckpointType` seguido de `Standard`, `Production` (si falla, hace uno estándar) o `ProductionOnly` |

Al aplicar
uno desde el Administrador de Hyper-V, la opción **«Crear punto de control y aplicar»** guarda antes
el estado actual; la opción **«Aplicar»** no, y **«No es posible deshacer esta acción.»**

### KVM, el hipervisor de Linux

**«KVM (for Kernel-based Virtual Machine) is a full virtualization solution for Linux on x86
hardware containing virtualization extensions (Intel VT or AMD-V). It consists of a loadable kernel
module, kvm.ko, that provides the core virtualization infrastructure and a processor specific
module, kvm-intel.ko or kvm-amd.ko.»** (KVM es una solución de virtualización completa para Linux en
hardware x86 con extensiones de virtualización; consta de un módulo del núcleo, `kvm.ko`, y de otro
propio del procesador, `kvm-intel.ko` o `kvm-amd.ko`).

Con él, **«one can run multiple virtual machines running unmodified Linux or Windows images»**, y
**«KVM is open source software. The kernel component of KVM is included in mainline Linux, as of
2.6.20. The userspace component of KVM is included in mainline QEMU, as of 1.3.»** (el componente del
núcleo está en Linux desde la versión 2.6.20, y el de espacio de usuario, en QEMU desde la 1.3).

Igual que Hyper-V, exige que el procesador traiga Intel VT o AMD-V. La página del proyecto no lo
clasifica como tipo 1 ni como tipo 2, y las fuentes de fabricante no coinciden: Red Hat lo pone entre
los de tipo 1 (tabla de ejemplos, más arriba); Amazon lo llama híbrido, aunque más cerca del tipo 1:
**«a kernel-based virtual machine (KVM) is considered a hybrid hypervisor, although it leans towards a
type 1 hypervisor.»** En un test, si la opción «tipo 1» está y la de «híbrido» no, es la que
sostiene Red Hat.

No hay que confundirlo con el KVM sobre IP, que es un conmutador de teclado, vídeo y ratón y no
virtualiza nada (epígrafe 2).

### Máquinas virtuales y contenedores

Y el contraste con los contenedores, porque el sector los confunde: una máquina virtual lleva su
propio sistema operativo completo; un contenedor comparte el núcleo del anfitrión y sólo empaqueta la
aplicación y sus dependencias.

Microsoft lo dice así: **«Un contenedor es un silo aislado y ligero para ejecutar una aplicación en el
sistema operativo host. Los contenedores se basan en el kernel del sistema operativo host»**, mientras
que **«A diferencia de los contenedores, las máquinas virtuales ejecutan un sistema operativo
completo, incluido su propio kernel»**. Y no son rivales: **«muchas implementaciones de contenedores
usan máquinas virtuales como sistema operativo host en lugar de ejecutarse directamente en el
hardware, especialmente cuando se ejecutan contenedores en la nube.»**

| | Máquina virtual | Contenedor |
|---|---|---|
| Aislamiento | **«Proporciona aislamiento completo del sistema operativo host y de otras máquinas virtuales.»** | **«Normalmente proporciona aislamiento ligero del host y otros contenedores, pero no proporciona un límite de seguridad tan sólido como una máquina virtual.»** |
| Sistema operativo | **«Ejecuta un sistema operativo completo, incluido el kernel, lo que requiere más recursos del sistema (CPU, memoria y almacenamiento).»** | **«Ejecuta la parte del modo de usuario de un sistema operativo»**, **«con menos recursos del sistema.»** |
| Invitados | **«Ejecuta casi cualquier sistema operativo dentro de la máquina virtual.»** | **«Se ejecuta en la misma versión del sistema operativo que el host»**, salvo con el aislamiento de Hyper-V, que permite versiones anteriores del mismo sistema |
| Despliegue | Windows Admin Center, Hyper-V Manager, PowerShell o System Center Virtual Machine Manager | **«Implementar contenedores individuales mediante Docker a través de la línea de comandos; implemente varios contenedores mediante un orquestador como Azure Kubernetes Service.»** |
| Si cae un nodo | **«Las máquinas virtuales pueden conmutarse a otro servidor de un clúster, reiniciando su sistema operativo en el nuevo servidor.»** | **«el orquestador vuelve a crear rápidamente los contenedores que se ejecutan en él en otro nodo de clúster.»** |

El término medio: **«Puede aumentar la seguridad si usa el modo de aislamiento de Hyper-V para aislar
cada contenedor en una máquina virtual ligera»**.

El NIST, por su parte, llama a esto virtualización del sistema operativo: **«provides a virtual
implementation of the OS interface that can be used to run applications written for the same OS as
the host, with each application in a separate VM container.»**

Docker, la herramienta más extendida, se presenta como **«an open platform for developing, shipping,
and running applications.»** Sus dos piezas: **«An image is a read-only template with instructions
for creating a Docker container.»** y **«A container is a runnable instance of an image.»** (una
imagen es una plantilla de sólo lectura; un contenedor es una instancia de esa imagen en
ejecución). Lo que no se guarda fuera se pierde: **«When a container is removed, any changes to its
state that aren't stored in persistent storage disappear.»** Funciona como cliente y servidor:
**«Docker uses a client-server architecture. The Docker client talks to the Docker daemon»**.

## 2. Virtualización de escritorio remoto

### Virtualizar el escritorio: local o remoto

El NIST describe la virtualización de escritorio como el segundo gran uso de la virtualización
completa, después de los servidores: **«desktop virtualization, where a single PC is running more
than one OS instance»**. Sus motivos: ejecutar aplicaciones de otro sistema (**«to allow a user to
run applications for different OSs on a single host»**), poder volver atrás (**«It allows changes to
be made to an OS and subsequently revert to the original if needed»**) y controlar mejor el puesto
(**«The organization stores a known-good image that contains the OS and all the applications needed
for the user.»**). Y advierte del riesgo de siempre: los datos del usuario tienen que guardarse fuera
de la imagen, **«otherwise, it would be lost each time the user quits from the virtualization
system.»**

Lo que el enunciado llama virtualización de escritorio remoto da un paso más: el escritorio no corre
en el equipo del usuario, sino en un servidor, y al usuario sólo le llega la imagen de la pantalla.
Microsoft lo explica al presentar los Servicios de Escritorio remoto: **«Al centralizar el
procesamiento en el centro de datos y el acceso remoto solo a la interfaz de usuario, el servicio de
Escritorio remoto le ayuda a reducir la carga administrativa, mejorar la seguridad y proporcionar un
acceso consistente y eficiente a los usuarios a los recursos que necesitan.»** Y lo resume en dos
frases que se preguntan: **«Los puntos de conexión simplemente presentan la interfaz de usuario remota
mediante el Protocolo de escritorio remoto (RDP).»** y **«Los datos permanecen en el centro de
datos»**.

Hay, pues, tres escalones, de menos a más centralizado (ordenación del tema, como oficio): la
máquina virtual que corre en el propio PC; el escritorio remoto de un equipo concreto, físico o
virtual, al que uno se conecta; y la plataforma que sirve escritorios y aplicaciones a muchos
usuarios desde el CPD o desde la nube.

### Escritorio remoto de un equipo: RDP

Para qué sirve: **«Puede usar Escritorio remoto para conectarse y controlar el equipo desde un
dispositivo remoto mediante la aplicación de Windows o el cliente de Escritorio remoto de Microsoft.»**

Qué ediciones pueden recibir conexiones, que es la pregunta típica: **«Puede usar Escritorio remoto
para conectarse a equipos que ejecutan las ediciones Windows Professional, Enterprise, Education y
Windows Server. Estas ediciones pueden actuar como anfitrionas para las conexiones de Escritorio Remoto
entrantes. Sin embargo, las ediciones de Windows Home no pueden servir como hosts de Escritorio remoto,
aunque se pueden usar como clientes para conectarse a otros sistemas que admiten el hospedaje de
Escritorio remoto.»**

Requisitos para conectarse, según Microsoft:

- **«El equipo remoto está encendido y conectado a la red.»**
- **«Escritorio remoto está habilitado en el equipo remoto.»**
- **«Tiene acceso de red al equipo remoto (localmente o a través de Internet).»**
- **«La cuenta de usuario puede conectarse (la cuenta se encuentra en la lista de usuarios
  permitidos).»**
- **«Las conexiones a Escritorio remoto se permiten a través del firewall del equipo remoto.»**

Para cambiar la configuración hay que **«ser miembro del grupo Administradores o tener privilegios
administrativos»**.

Cómo se habilita en Windows 11: **«Seleccione Inicio, Configuración y Sistema.»**; **«Seleccione
Escritorio remoto, cambie la opción Habilitar Escritorio remoto a Activado.»**; y se confirma. A otros
usuarios se les da acceso desde la misma pantalla (**«seleccione Usuarios de Escritorio remoto»**,
**«Seleccione Agregar, escriba el nombre de usuario»**).

Cómo se conecta uno: con la aplicación **«Conexión a Escritorio remoto»**, el cliente clásico que
Microsoft identifica como **«(`mstsc.exe`)»**, escribiendo **«el nombre del equipo o la dirección IP
del equipo remoto»**; o con la Aplicación de Windows. Desde fuera de la red, **«puede usar el reenvío
de puertos o configurar una VPN»**. Como oficio de seguridad, de las dos se prefiere la VPN o la
puerta de enlace de RDS (más abajo): publicar el puerto del Escritorio remoto en Internet por
reenvío lo deja a la vista de cualquiera.

El puerto: el Escritorio remoto funciona **«a través del Protocolo de escritorio remoto (RDP)
escuchando en el puerto 3389 de forma predeterminada. Este puerto de escucha se puede cambiar con
fines de seguridad o de configuración.»** Se consulta en el registro:

```powershell
Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name 'PortNumber'
```

Se cambia con `Set-ItemProperty` sobre la misma clave y el valor `PortNumber`, o en el Editor del
Registro (en decimal, y por ese camino se reinicia el equipo), y luego hay que abrir el puerto nuevo en el cortafuegos: **«Si usa el
Firewall de Windows, debe agregar una nueva regla de entrada para permitir el tráfico en el puerto
nuevo.»** El ejemplo de Microsoft crea dos reglas, una para TCP y otra para UDP. Al conectarse, el
puerto se escribe tras el nombre: **«si ha cambiado el puerto para usar 3390 en el equipo
`pc1.contoso.com`, la dirección es `pc1.contoso.com:3390`.»**

La autenticación de nivel de red: **«Con el NLA habilitado, los usuarios deben autenticarse antes de
que se establezca una sesión remota, lo que reduce el riesgo de acceso no autorizado y ayuda a
proteger el equipo frente a usuarios malintencionados y software. Se recomienda habilitar NLA para la
mayoría de los entornos»**. La salvedad de la misma página: con dispositivos o clientes antiguos que
no admiten NLA puede hacer falta deshabilitarla temporalmente.

Los clientes. La Aplicación de Windows **«se conecta de forma remota a los dispositivos y
aplicaciones de Windows desde Azure Virtual Desktop, equipos en la nube de Windows 365, Microsoft Dev
Box, Servicios de Escritorio remoto y equipos»**, en Windows, macOS, iOS/iPadOS, Android/ChromeOS,
desde un navegador web y en el visor Meta Quest. A la fecha de lectura tenía dos excepciones en Windows, que dice la propia
página: **«Para conectarse a Servicios de Escritorio remoto en Windows, siga usando la aplicación
Escritorio remoto en Windows.»** y **«Las conexiones de PC remotos están en versión preliminar en
Windows. Para conectarse a un equipo remoto mediante una aplicación disponible con carácter general,
siga usando la aplicación Conexión a Escritorio remoto que viene con Windows (también conocido como
MSTSC).»** Para iniciar sesión en ella **«requiere una cuenta profesional o educativa de Microsoft
proporcionada por el administrador»**; para un PC remoto no hace falta.

### Servicios de Escritorio remoto (RDS)

Cuando no se trata de un equipo sino de servir escritorios a muchos usuarios, Windows Server tiene
RDS: **«Servicios de Escritorio remoto (RDS) en Windows Server es una plataforma integrada para ofrecer
de forma segura escritorios y aplicaciones administrados a los usuarios, ya sea en la oficina,
trabajando desde casa o conectando desde ubicaciones de sucursales y asociados.»**

Qué ofrece: **«Los Servicios de Escritorio remoto admiten escritorios virtuales basados en servidor
multisesión y escritorios virtuales de sesión única (o agrupados/personales), además de la
publicación de aplicaciones individuales (RemoteApp).»** Es decir, el usuario se conecta a **«Un
escritorio completo (basado en sesión o en máquina virtual).»** o a **«Aplicaciones específicas
(programas remoteApp) que aparecen y se comportan como aplicaciones instaladas localmente.»**

Sus roles, que se preguntan uno a uno:

| Rol | Qué hace |
|---|---|
| Host de sesión de Escritorio remoto (RDSH) | **«Ejecuta escritorios de usuario basados en sesión y programas RemoteApp en Windows Server»** |
| Host de Virtualización de Escritorio Remoto | **«Hospeda colecciones de infraestructura de escritorio virtual (máquinas virtuales cliente windows agrupadas o personales). Se integra con Hyper-V para el aprovisionamiento.»** |
| Agente de conexión de Escritorio remoto | **«Mantiene las sesiones de usuario, equilibra la carga de conexiones, vuelve a conectar usuarios a sesiones existentes, administra colecciones (sesión y VDI).»** |
| Acceso web de Escritorio remoto | **«Proporciona un portal web y fuentes de datos»** con los escritorios y aplicaciones que cada usuario puede usar |
| Puerta de enlace de Escritorio remoto (*RD Gateway*) | **«Habilita el acceso RDP seguro y cifrado a través de HTTPS (TCP 443) desde redes externas sin abrir puertos RDP internos. Admite MFA y directivas condicionales.»** |
| Licencias de Escritorio remoto | Gestiona **«las licencias de acceso de cliente de Servicios de Escritorio Remoto (CAL de RDS) necesarias para el uso legal (Usuario o Dispositivo).»** |

Alrededor suele haber **«servicios de archivos para perfiles de usuario, servicios de certificado
para TLS y soluciones de supervisión.»**

Los modelos de implementación de RDS:

| Modelo | Cómo funciona | Para quién | Coste y densidad |
|---|---|---|---|
| Basado en sesión (RDSH) | **«Varios usuarios comparten una instancia de Windows Server; cada obtiene una sesión aislada.»** | **«Trabajadores por tareas, aplicaciones empresariales, usuarios temporales.»** | **«Mayor densidad de usuario, menor costo por usuario.»** |
| VDI en entorno compartido | **«Los usuarios se conectan a una máquina virtual cliente Windows asignada dinámicamente desde un grupo. Estado no persistente o restablecible.»** | **«Los trabajadores del conocimiento que necesitan compatibilidad con el cliente de Windows; aislamiento de aplicaciones.»** | **«Densidad media/costo.»** |
| VDI personal | **«A cada usuario se le asigna una máquina virtual cliente Windows dedicada que conserva los cambios.»** | **«Desarrolladores, usuarios avanzados, aplicaciones con mucha personalización.»** | **«Densidad más baja, mayor flexibilidad.»** |
| Híbrido | **«Combine RDSH para aplicaciones de línea base + VDI para necesidades especializadas.»** | **«Entornos de personas mixtas.»** | **«Equilibrio optimizado.»** |

Ojo con la palabra: aquí «híbrido» significa mezclar sesiones y VDI, no mezclar CPD propio y nube,
que es lo que el enunciado llama despliegue híbrido (epígrafe 4).

Las ventajas que Microsoft atribuye a RDS: centraliza **«la gestión de aplicaciones y escritorios
para aplicar parches y proteger los recursos de una vez, en lugar de hacerlo en múltiples puntos de
conexión»**; **«La densidad de varias sesiones reduce el costo por usuario»**; y los datos no salen
del CPD. En seguridad: **«TLS protege el tráfico RDP»** y **«la Puerta de enlace de RD encapsula RDP
en HTTPS para minimizar los puertos expuestos»**; **«la ejecución centralizada mantiene los datos
residentes en el centro de datos, por lo que solo sale el flujo de la interfaz de usuario.»**

Lo que hay que planificar: los perfiles de usuario (**«La estrategia de perfil (perfiles móviles,
redirección de carpetas o administración de perfiles de terceros) afecta al rendimiento del inicio de
sesión y al crecimiento del disco»**), la GPU si hay trabajo gráfico (**«Si los usuarios necesitan
3D o multimedia rico, planifique recursos de GPU»**), la red (**«La topología de red y la latencia
afectan la experiencia del usuario»**) y si la aplicación soporta varias sesiones en la misma
máquina (**«Valide el comportamiento de varias sesiones de la aplicación al principio»**).

Dónde se instala: **«En las instalaciones: Control total del hardware, la red y la localización de
los datos.»** o en **«Infraestructura de Azure (IaaS)»**. Y Microsoft remite a su servicio en la
nube como alternativa: **«Si desea evaluar una solución de escritorio más amplia basada en la nube,
consulte Azure Virtual Desktop.»** (epígrafe 3).

### KVM sobre IP

El otro sentido de las siglas, y el que más se ve en una televisión:

| Qué es | Qué hace |
|---|---|
| KVM sobre IP | Llevar el teclado, el vídeo y el ratón de un ordenador por la red, para manejarlo desde otro sitio |

Y por qué el KVM sobre IP importa: permite sacar los ordenadores de la sala de realización y
dejarlos en el centro de proceso de datos, quedando en el puesto sólo el teclado, el monitor y el
ratón. Menos calor y menos ruido en la sala, y el mantenimiento se hace sin entrar en el plató.

La diferencia con lo anterior, como oficio: el KVM sobre IP transporta la consola de un ordenador
físico concreto y no necesita que ese ordenador tenga sistema ni red operativos (sirve para entrar en
la BIOS o ver un arranque), mientras que el Escritorio remoto es software dentro del sistema
operativo y sólo funciona con el sistema arrancado y en red. Ninguno de los dos virtualiza el equipo:
los dos lo manejan a distancia.

## 3. Modelos de virtualización

### Una advertencia de vocabulario

Los cuatro modelos que nombra el enunciado (PC virtual, escritorio virtual, virtualización de
aplicaciones y *workspace* virtual) no tienen una definición en norma técnica. El NIST define la
virtualización de escritorio y la de aplicaciones; los otros dos nombres son de fabricante. El tema
da cada modelo con la definición del fabricante que lo usa y dice cuándo la equivalencia es suya.

### PC virtual

Hay dos lecturas, y el tribunal puede tomar cualquiera.

La primera, clásica: un PC virtual es una máquina virtual de escritorio que corre en el propio PC del
usuario, con un hipervisor de tipo 2, como VirtualBox, o con Hyper-V activado en Windows 11 Pro
(que Microsoft clasifica como de tipo 1). Es la
virtualización de escritorio local que describe el NIST (**«Desktop virtualization allows users to
access both OSs simultaneously on one computer.»**) y la que Microsoft ofrece en el escritorio:
**«Hyper-V en Windows proporciona a los profesionales de TI y a los desarrolladores una solución
ligera adecuada para escenarios de desarrollo y pruebas.»**, con **«Creación rápida para la
configuración simplificada de máquinas virtuales»** en Windows 11. El NIST cita un producto
antiguo con ese nombre, VirtualPC, como ejemplo de emulación (**«early versions of VirtualPC allowed
users to run the Microsoft Windows OS on the PowerPC processor»**); que el enunciado lo use en este sentido es
interpretación del tema.

Un caso particular de esta lectura es el Espacio aislado de Windows: **«Espacio aislado de Windows
(WSB) ofrece un entorno de escritorio ligero y aislado para ejecutar aplicaciones de forma
segura.»** Es una máquina virtual de usar y tirar: **«El espacio aislado es temporal; cerrarlo
elimina todo el software, los archivos y el estado. Cada inicio proporciona una instancia nueva.»** (Desde Windows 11, versión 22H2, los datos
sí se conservan en los reinicios hechos dentro del espacio aislado.) Funciona en las ediciones Pro, Enterprise, Pro Education/SE y Education; **«Espacio aislado de
Windows no se admite actualmente en la edición Windows Home.»** Dos avisos de la página: **«Espacio
aislado de Windows habilita la conexión de red de forma predeterminada.»** y **«Espacio aislado de
Windows actualmente no permite que varias instancias se ejecuten simultáneamente.»** Uso típico para
el operador: abrir un adjunto sospechoso (**«abriendo un espacio aislado con redes deshabilitadas y
asignando la carpeta con la aplicación o el archivo que desea abrir al espacio aislado en modo de
solo lectura»**).

La segunda lectura, actual: el PC en la nube. **«Windows 365 es un software como servicio (SaaS)
basado en la nube que crea automáticamente un nuevo tipo de máquina virtual Windows (PC en la nube)
para los usuarios finales.»** **«Un equipo en la nube es una máquina virtual de alta disponibilidad,
optimizada y escalable que proporciona a los usuarios finales una experiencia de escritorio de
Windows enriquecida. El servicio Windows 365 lo hospeda y puede acceder a él desde cualquier lugar,
en cualquier dispositivo.»** Rasgos que se preguntan:

- Es uno por persona: **«los usuarios finales tienen una relación 1:1 con su PC en la nube. Es su
  propio equipo personal en la nube.»** (en Enterprise, Business y Government).
- Nadie lo monta a mano: **«El servicio Windows 365 crea automáticamente equipos en la nube al
  asignar una licencia de Windows 365 a un usuario final en un grupo de usuarios Microsoft Entra
  adecuado.»** **«Los administradores no crean PC en la nube de forma manual.»**
- Se paga por usuario y mes: **«Los equipos en la nube para uso humano se facturan en un modelo de
  costo por usuario y mes.»**
- Ediciones: Business, para **«empresas más pequeñas (hasta 300 puestos)»**; Enterprise, con
  **«integración completa con Microsoft Intune»**; Government; Flex, con **«una sola licencia para
  aprovisionar hasta tres equipos en la nube para su uso no simultáneo»**; y una para agentes de
  inteligencia artificial, en versión preliminar.
- Hay un dispositivo hecho para ello: **«Windows 365 Link, el primer dispositivo de PC en la nube
  creado específicamente para conectar a los usuarios directamente a Windows 365.»**

### Escritorio virtual (VDI)

Un escritorio virtual es un escritorio completo que corre en un servidor y que el usuario ve en su
dispositivo. Ya se ha visto en RDS, que lo sirve de dos maneras: por sesión (muchos usuarios en un
mismo Windows Server) o por VDI (una máquina virtual con Windows cliente por usuario, agrupada o
personal).

Las dos distinciones que ordenan cualquier oferta de escritorios virtuales, con las palabras de las
fuentes:

| Distinción | Una opción | La otra |
|---|---|---|
| Cuántos usuarios por máquina | Sesión única: una máquina, un usuario | Multisesión: varios usuarios comparten una instancia de Windows |
| Qué pasa con los cambios | Personal o persistente: la máquina **«conserva los cambios»** | Agrupado o no persistente: **«Estado no persistente o restablecible.»** |

Azure Virtual Desktop es el servicio de escritorios virtuales de Microsoft en la nube: **«Azure
Virtual Desktop es un servicio de escritorio y de virtualización de aplicaciones que se ejecuta en
Azure.»** Lo que ofrece:

- **«Ofrezca una experiencia completa de Windows con Windows 11, Windows 10 o Windows Server. Usa
  sesión única para asignar dispositivos a un solo usuario o usa varias sesiones para
  escalabilidad.»**
- **«Ofrezca escritorios completos o use RemoteApp para entregar aplicaciones individuales.»**
- **«Reemplace las implementaciones de Servicios de Escritorio remoto (RDS) existentes.»**
- Una función propia: **«Con la nueva funcionalidad multisesión de Windows 11 y Windows 10
  Enterprise, exclusiva de Azure Virtual Desktop o Windows Server, puede reducir considerablemente el
  número de máquinas virtuales»**.
- Menos infraestructura que mantener: **«No es necesario administrar personalmente los roles de
  infraestructura auxiliares, como una puerta de enlace o un agente, como lo hace con los Servicios
  de Escritorio remoto.»**
- Sin puertos de entrada: **«Establezca usuarios de forma segura a través de conexiones inversas al
  servicio, por lo que no es necesario abrir ningún puerto de entrada.»**
- Escala sola: **«Aumente o disminuya automáticamente la capacidad según la hora del día, días
  específicos de la semana o según cambie la demanda con escalabilidad automática»**.

Su vocabulario, que se pregunta:

| Término | Definición de Microsoft |
|---|---|
| Grupo de hosts | **«Un grupo de hosts es una colección de Azure máquinas virtuales que están registradas en Azure Virtual Desktop como hosts de sesión.»** Todas deben salir **«de la misma imagen»** |
| Grupo de hosts personal | **«Personal, donde cada host de sesión se asigna a un usuario individual.»** Límite de sesiones: **«Uno.»** |
| Grupo de hosts agrupado | **«Agrupadas, donde las sesiones de usuario se pueden cargar con equilibrio de carga en cualquier host de sesión del grupo host. Puede haber varios usuarios diferentes en un único host de sesión al mismo tiempo.»** Reparto: **«amplitud primero o profundidad en primer lugar.»** |
| Grupo de aplicaciones | **«Un grupo de aplicaciones controla el acceso a un escritorio completo o a una agrupación lógica de aplicaciones que están disponibles en los hosts de sesión de un único grupo host.»** De dos tipos, Escritorio y RemoteApp; RemoteApp **«Solo está disponible con grupos de hosts agrupados.»** |
| Área de trabajo | **«Un área de trabajo es una agrupación lógica de grupos de aplicaciones.»** |
| Sesión desconectada | **«Cuando un usuario cierra la ventana de sesión remota sin cerrar sesión, la sesión se desconecta.»** Al volver, se le lleva a esa misma sesión |

Dos diferencias prácticas entre personal y agrupado, de la misma tabla de Microsoft. Las
actualizaciones: el personal **«Se ha actualizado con Windows Novedades, Microsoft Configuration
Manager u otras herramientas»** (sic: «Windows Novedades» es la traducción automática de *Windows
Update*); el agrupado **«Se ha actualizado mediante la implementación de hosts de sesión a partir de
imágenes actualizadas en lugar de actualizaciones tradicionales.»** Y los datos de usuario: en el
personal **«puede almacenar sus datos de perfil de usuario en el disco del sistema operativo (SO) de
la máquina virtual.»**; en el agrupado los usuarios **«pueden conectarse a distintos hosts de sesión
cada vez que se conectan, por lo que deben almacenar sus datos de perfil de usuario en FSLogix.»**

FSLogix es, pues, la pieza que hace usable un escritorio no persistente: **«FSLogix mejora y permite
una experiencia coherente para los perfiles de usuario de Windows en entornos informáticos de
escritorios virtuales.»** Cómo lo hace: **«FSLogix usa un controlador de filtro para virtualizar y
redirigir el perfil a nivel de sistema de archivos. Las aplicaciones no saben que el perfil está en la
red.»** Lo que aporta: **«Transferencia de datos de usuario entre hosts de sesiones informáticas
remotas.»**, **«Minimización de los tiempos de inicio de sesión de los entornos de escritorio
virtual.»** y **«Proporcionar una experiencia de perfil local, eliminando la necesidad de perfiles
móviles.»** La página trae además un aviso con fecha: **«en la actualización de abril de 2026 de
Windows Server, el tipo de cifrado Kerberos predeterminado cambia de RC4 a AES-SHA1»**, y los
recursos compartidos con contenedores de FSLogix no actualizados **«podrían tener problemas de
acceso»**.

Un aviso de vigencia: **«Azure Virtual Desktop clásico se retira el 30 de septiembre de 2026. Las
conexiones a los recursos clásicos se bloquearán después de la retirada.»** El 24-09-2026, fecha del
BOJA, faltaban seis días; lo vigente es la versión basada en Azure Resource Manager.

El mismo modelo lo ofrecen otros proveedores con sus nombres. Amazon, por ejemplo: **«Amazon
WorkSpaces enables you to provision virtual, cloud-based desktops known as WorkSpaces for your
users.»**, con escritorios persistentes (**«WorkSpaces Personal»**) o no persistentes (**«WorkSpaces
Pool»**).

El dispositivo con el que el usuario ve el escritorio virtual puede ser un PC corriente, una tableta o
un cliente ligero (*thin client*). Amazon lo define así: **«Thin clients are end-user terminals
designed specifically for VDI.»** (terminales de usuario hechos expresamente para la VDI). IBM lo
presenta como la opción barata: **«The user's endpoint can be a relatively inexpensive thin client or
a mobile device.»**, y añade que el usuario no se conecta al hipervisor, sino a un agente de conexión:
**«Users don't connect to the hypervisor directly. Instead, they access a connection broker that
coordinates with the hypervisor to source an appropriate virtual desktop from the pool.»** El NIST
usa la palabra en sentido más amplio, para cualquier cliente que sólo presenta lo que corre en el
servidor (**«a thin client interface, such as a web browser»**). Windows 365 Link, citado en el PC
virtual, es un dispositivo de este tipo para un servicio concreto.

Cada fabricante de escritorios virtuales lleva su propio protocolo de visualización remota, el que
transporta pantalla, teclado y ratón entre el escritorio y el dispositivo:

| Protocolo | Fabricante | Qué dice la fuente |
|---|---|---|
| RDP | Microsoft | El de Escritorio remoto y RDS (epígrafe 2) |
| HDX, sobre ICA | Citrix (Citrix Virtual Apps and Desktops) | **«Citrix HDX represents a broad set of technologies that deliver a high-definition experience to users of centralized applications and desktops, on any device and over any network.»** La conexión se abre con un fichero **«Independent Computing Architecture (ICA)»** y va **«between the device and the ICA stack»** del escritorio. Con el transporte adaptable, que prefiere el protocolo EDT (*Enlightened Data Transport*), sobre UDP, y cae a TCP si no puede, en las conexiones internas el host de sesión debe admitir tráfico entrante por UDP en los puertos **«2598»** (con fiabilidad de sesión), **«1494»** (sin ella) y **«443»** (HDX Direct o conexión cifrada) |
| Blast y PCoIP (además de RDP) | Omnissa (Horizon 8) | **«Horizon is a multi-protocol solution. Three remoting protocols are available when creating desktop pools or RDSH-published applications: Blast, PCoIP, and RDP.»** De Blast: admite varios códecs, **«both TCP and UDP»**, y codificación por hardware en una GPU virtual de un fabricante de tarjetas gráficas |

Ninguno es norma: son protocolos de fabricante, cada uno documentado por quien lo hace.

### Virtualización de aplicaciones

Aquí no se virtualiza el escritorio entero, sino cada aplicación. El NIST la define por la API: **«application
virtualization provides a virtual implementation of the application programming interface (API)
that a running application expects to use, allowing applications developed for one platform to run
on another without modifying the application itself.»**, y pone de ejemplo la máquina virtual de
Java (**«The Java Virtual Machine (JVM) is an example of application virtualization»**). También dice
cuándo basta con ella: si el problema es una aplicación concreta (una web que sólo funciona en un
navegador antiguo), **«many organizations use application virtualization instead of desktop
virtualization.»**

En el mundo Windows, tres formas que hay que distinguir:

| Forma | Qué hace | Estado |
|---|---|---|
| Publicación de aplicaciones (RemoteApp) | La aplicación corre en el servidor (RDS o AVD) y al usuario sólo le llega su ventana; los programas RemoteApp **«aparecen y se comportan como aplicaciones instaladas localmente»** | Vigente |
| App-V | **«Microsoft Application Virtualization (App-V) para Windows entrega aplicaciones Win32 a los usuarios como aplicaciones virtuales. Estas aplicaciones se instalan en servidores administrados de forma centralizada y se entregan a los usuarios como un servicio en tiempo real y según sea necesario.»** | En retirada: **«El soporte extendido para MDOP finaliza el 14 de abril de 2026.»** y **«El cliente de Windows App-V se encuentra en soporte extendido fijo.»** Microsoft remite a **«Azure Virtual Desktop con la conexión de aplicaciones MSIX»** |
| App Attach (Azure Virtual Desktop) | **«App Attach permite adjuntar aplicaciones de forma dinámica desde un paquete de aplicación a una sesión de usuario en Azure Virtual Desktop. Las aplicaciones no se instalan localmente en hosts de sesión o imágenes»** | Vigente |

Lo que App Attach añade, y que explica por qué se virtualizan las aplicaciones:

- Aislamiento: **«Las aplicaciones se ejecutan dentro de contenedores, que separan los datos de
  usuario, el sistema operativo y otras aplicaciones, lo que aumenta la seguridad y facilita su
  solución de problemas.»**
- Varias versiones a la vez: **«Los usuarios pueden ejecutar varias versiones de la misma aplicación
  simultáneamente en el mismo host de sesión.»**
- Actualizar sin parada: **«Las aplicaciones se pueden actualizar a una nueva versión de aplicación
  con una nueva imagen de disco sin necesidad de una ventana de mantenimiento.»**
- Permisos por persona: **«Los permisos se aplican por aplicación por usuario»**.
- Paquetes admitidos: MSIX (`.msix`, `.msixbundle`), Appx (`.appx`, `.appxbundle`) y App-V
  (`.appv`); **«MSIX es un superconjunto de Appx.»**
- Dónde viven: **«La conexión de aplicaciones requiere que las imágenes de la aplicación se almacenen
  en un recurso compartido de archivos SMB, que luego se monta en cada host de sesión durante el
  inicio de sesión.»** Las imágenes MSIX y Appx pueden ser CimFS (sistema de archivos de imagen compuesta),
  VHDX o VHD, **«pero no se recomienda usar VHD.»**
- Cuándo se registran: por defecto, a petición (**«A petición es el método de registro
  predeterminado.»**), para no alargar el inicio de sesión.

### Workspace virtual

Es el término menos asentado de los cuatro. Ninguna norma lo define; lo usan los fabricantes, cada
uno a su manera:

- Microsoft llama área de trabajo (*workspace* en la consola inglesa) a la agrupación que el usuario
  ve en su cliente: **«Cada grupo de aplicaciones debe estar asociado a un área de trabajo para que los
  usuarios vean los escritorios y las aplicaciones publicados en ellos.»**
- Amazon llama WorkSpaces a cada escritorio virtual en la nube (cita de arriba).
- Citrix ofrece un punto de acceso único a todo lo publicado: **«Citrix® StoreFront Cloud is a
  service that provides secure access to your virtual apps, desktops, web and SaaS apps from a web
  browser or Citrix Workspace app.»**

Lo común a todos, y lo que el tema entiende por *workspace* virtual (interpretación del tema, no
definición de norma): un espacio de trabajo único, al que el usuario entra con una identidad y desde
cualquier dispositivo, y en el que encuentra reunidos sus escritorios virtuales, sus aplicaciones
publicadas o virtualizadas, sus aplicaciones web y en la nube y sus datos. No es otra técnica de
virtualización, sino la capa que agrega las anteriores y se las presenta al usuario.

### Los cuatro modelos, frente a frente

Cuadro de síntesis del tema (oficio, construido con lo citado arriba):

| Modelo | Qué se virtualiza | Dónde corre | Ejemplos citados |
|---|---|---|---|
| PC virtual | Un equipo entero, para un usuario | En su propio PC (local) o en la nube (PC en la nube) | Hyper-V en Windows 11, VirtualBox, Espacio aislado de Windows; Windows 365 |
| Escritorio virtual | El escritorio, servido a muchos usuarios | En servidores del CPD o de la nube | RDS (sesión o VDI), Azure Virtual Desktop, Amazon WorkSpaces |
| Virtualización de aplicaciones | Cada aplicación por separado | En el servidor (publicada) o en el puesto, aislada | RemoteApp, App-V, App Attach |
| *Workspace* virtual | Nada nuevo: agrega lo anterior en un único acceso | Donde estén los recursos que agrega | Área de trabajo de AVD, aplicación Citrix Workspace |

## 4. Modos de despliegue: on-premise, cloud e híbridos

### La nube según el NIST

La definición de referencia es la del NIST: **«Cloud computing is a model for enabling ubiquitous,
convenient, on-demand network access to a shared pool of configurable computing resources (e.g.,
networks, servers, storage, applications, and services) that can be rapidly provisioned and
released with minimal management effort or service provider interaction.»** (un modelo que permite
acceder por red, en cualquier sitio, cómodamente y a demanda, a un conjunto compartido de recursos
configurables, que se dan y se retiran deprisa y con poco esfuerzo de gestión). Y su estructura se
pregunta por el número: **«This cloud model is composed of five essential characteristics, three
service models, and four deployment models.»**

Las cinco características esenciales:

| Característica | Qué significa, según el NIST |
|---|---|
| Autoservicio bajo demanda (*on-demand self-service*) | El cliente se da recursos **«as needed automatically without requiring human interaction with each service provider.»** |
| Acceso amplio por red (*broad network access*) | **«Capabilities are available over the network and accessed through standard mechanisms»**, desde clientes ligeros o pesados |
| Agrupación de recursos (*resource pooling*) | **«The provider’s computing resources are pooled to serve multiple consumers using a multi-tenant model»**; por lo general, el cliente no sabe dónde están exactamente |
| Elasticidad rápida (*rapid elasticity*) | Los recursos crecen y menguan **«commensurate with demand»** y **«often appear to be unlimited»** |
| Servicio medido (*measured service*) | **«Resource usage can be monitored, controlled, and reported»**; normalmente, pago por uso |

Los tres modelos de servicio:

| Modelo | Qué recibe el cliente | Qué controla |
|---|---|---|
| SaaS | **«to use the provider’s applications running on a cloud infrastructure»** | Como mucho, **«limited userspecific application configuration settings»** |
| PaaS | **«to deploy onto the cloud infrastructure consumer-created or acquired applications»** | **«the deployed applications and possibly configuration settings for the application-hosting environment»** |
| IaaS | **«to provision processing, storage, networks, and other fundamental computing resources where the consumer is able to deploy and run arbitrary software, which can include operating systems and applications»** | **«operating systems, storage, and deployed applications»**, y quizá un control limitado de algunos componentes de red, como los cortafuegos del host |

Microsoft da los mismos tres con ejemplos suyos: en IaaS **«gestionas máquinas virtuales, sistemas
operativos y aplicaciones»**; en PaaS **«Despliegas aplicaciones sin gestionar máquinas virtuales ni
sistemas operativos»**; en SaaS **«Usas aplicaciones ya hechas. Entre los ejemplos se incluyen
Microsoft 365, Dynamics 365 y otras aplicaciones en la nube.»**

Y los cuatro modelos de despliegue:

| Modelo | Definición del NIST |
|---|---|
| Nube privada | **«The cloud infrastructure is provisioned for exclusive use by a single organization comprising multiple consumers (e.g., business units).»** Puede estar **«on or off premises»** |
| Nube comunitaria | **«provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns»** |
| Nube pública | **«provisioned for open use by the general public»**; **«It exists on the premises of the cloud provider.»** |
| Nube híbrida | **«a composition of two or more distinct cloud infrastructures (private, community, or public) that remain unique entities, but are bound together by standardized or proprietary technology that enables data and application portability (e.g., cloud bursting for load balancing between clouds).»** |

Una precisión que el tribunal puede buscar: la nube privada no es lo mismo que *on-premise*. El NIST
admite expresamente una nube privada fuera de las instalaciones de la organización, gestionada por
un tercero. Y un CPD propio con servidores virtualizados no es por eso una nube privada: lo es si
reúne las cinco características (autoservicio, elasticidad, medida…).

### On-premise: en las instalaciones

Todo está en el CPD de la organización: el hardware, el hipervisor, los servidores de escritorios y
los datos. En virtualización de escritorios, es RDS sobre Hyper-V en servidores propios, o una
granja de máquinas virtuales con cualquier otro hipervisor. Lo que da, en palabras de Microsoft:
**«En las instalaciones: Control total del hardware, la red y la localización de los datos.»** Lo
que cuesta: **«En un centro de datos local, usted es el propietario de toda la pila.»** Es decir, la
organización responde de todo, del edificio a los datos.

Microsoft enumera los fallos típicos de ese modelo, que sirven de lista de riesgos: **«Aplicación de
revisiones retrasadas»**, **«Seguridad física insuficiente»**, **«Monitorización incompleta de la
red»**, **«Hardware obsoleto»** y **«Copia de seguridad insuficiente y recuperación ante
desastres»**. Por qué se elige pese a todo, como oficio: datos que no pueden salir, latencia baja con
equipos del propio edificio, inversión ya hecha y licencias propias.

### Cloud: en la nube

El escritorio o el servidor corre en el CPD de un proveedor. En este tema hay tres ejemplos, cada
uno en un modelo de servicio:

| Ejemplo | Modelo de servicio | Qué gestiona la organización |
|---|---|---|
| Windows 365 | SaaS, según Microsoft (**«Windows 365 es un software como servicio (SaaS)»**) | Licencias, usuarios, directivas; no crea ni mantiene las máquinas |
| Azure Virtual Desktop | Servicio en Azure: **«Administre solo la imagen y las máquinas virtuales que usa para las sesiones de su suscripción de Azure, no la infraestructura.»** | Las imágenes, las máquinas de sesión y la asignación |
| RDS en máquinas virtuales de Azure | IaaS: **«despliegue roles de Servicios de Escritorio Remoto en máquinas virtuales de Azure»** | Todo desde el sistema operativo hacia arriba |

La clasificación de Azure Virtual Desktop en uno de los tres modelos del NIST no la da Microsoft en
las páginas leídas; por lo que deja al cliente (imagen y máquinas), queda entre IaaS y PaaS, y así se
dice como interpretación del tema.

En el sector circula además un término que no es del NIST: escritorio como servicio (DaaS). IBM lo define como escritorios completos servidos desde la nube: **«Known as desktop
as a service (DaaS), this technology delivers complete desktop virtualization environments,
including operating systems, applications, files and user preferences from the cloud.»** Amazon lo
usa en un sentido más estrecho, el de un tercero que monta y administra la VDI del cliente: **«DaaS
providers offer a turn-key solution, deploying the fully managed service for your organization and
also taking over administration responsibilities»**, y distingue de ello su propio Amazon WorkSpaces,
que llama **«fully managed virtual desktop solution»**. Citrix lo lleva en el nombre de su servicio
en la nube, Citrix DaaS, que puede gestionar a la vez máquinas en nubes públicas y en hipervisores
propios: **«Citrix DaaS allows you to manage on-premises data center and public cloud workloads
together in a hybrid deployment.»** Microsoft, en las páginas leídas, no usa el término para Windows
365 (lo llama SaaS) ni para Azure Virtual Desktop. En un test, «escritorio virtual completo,
servido y gestionado por un proveedor desde la nube» es DaaS; entre los tres modelos
del NIST, no existe.

Quién responde de qué en la nube (matriz de Microsoft, resumida):

| Área | Local | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| Datos, configuración, identidades y usuarios | Cliente | Cliente | Cliente | Cliente |
| Dispositivos cliente | Cliente | Cliente | Cliente | Compartida |
| Aplicaciones | Cliente | Cliente | Compartida | Compartida |
| Controles de red | Cliente | Cliente | Compartida | Microsoft |
| Sistema operativo | Cliente | Cliente | Microsoft | Microsoft |
| Hosts físicos, red física y centro de datos | Cliente | Microsoft | Microsoft | Microsoft |

La regla que no cambia nunca: **«Para todos los tipos de implementación en la nube, posee sus datos e
identidades.»** Y siempre quedan en casa los datos, los puntos de conexión, las cuentas y la
administración del acceso. El hipervisor, en cambio, pasa al proveedor: Microsoft se encarga de la
**«administración de la capa de virtualización que habilita máquinas virtuales en IaaS y PaaS.»**

### Híbrido

Un despliegue híbrido combina lo propio y la nube. La definición formal es la de nube híbrida del
NIST (dos o más infraestructuras que siguen siendo distintas pero están unidas por una tecnología
que permite mover datos y aplicaciones). En rigor, el NIST habla de infraestructuras de nube:
un CPD propio que no reúna las cinco características no es una nube privada, y llamar híbrido a la
suma de ese CPD y una nube pública es uso común, no definición del NIST. En virtualización de escritorios y sistemas, los ejemplos
de las fuentes leídas:

- Azure Virtual Desktop sobre hardware propio: **«Hospede escritorios y aplicaciones locales con el
  hipervisor de su elección con Azure Virtual Desktop Hybrid o Azure Virtual Desktop para Azure
  Local.»** Azure Local **«es la solución de infraestructura distribuida de Microsoft que amplía las
  funcionalidades de Azure a entornos propiedad del cliente.»** y **«admite implementaciones
  conectadas o desconectadas de la nube.»** Se paga **«por núcleo físico en las máquinas locales»**.
- RDS en el CPD propio ampliado con Azure Virtual Desktop: la propia página de RDS dice que **«Incluso
  puede ampliar Azure Virtual Desktop al centro de datos local con Azure Local.»**
- Hyper-V con la nube como sitio de recuperación: **«Azure Site Recovery amplía las capacidades de
  recuperación ante desastres de Hyper-V a la nube»** y permite **«usar Azure como sitio secundario
  para la recuperación ante desastres sin configuración compleja ni hardware adicional.»**
- Cargas que se mueven: Hyper-V en Azure Local permite **«escenarios de nube híbrida en los que las
  cargas de trabajo se pueden mover sin problemas entre entornos locales y Azure»**.

Por qué se elige lo híbrido, según Microsoft al presentar Azure Local: la **«necesidad de proceso
para permanecer en el entorno local»**, la **«resistencia de las aplicaciones críticas»**, la
**«toma de decisiones de baja latencia»** o requisitos de cumplimiento, como la **«Estricta soberanía
y requisitos normativos que requieren que los datos se conserven y controlen localmente.»**

### Cómo se elige: los tres modos frente a frente

Cuadro de síntesis del tema (oficio, apoyado en lo citado):

| | On-premise | Cloud | Híbrido |
|---|---|---|---|
| Dónde está el hardware | En el CPD propio | En el del proveedor | En los dos |
| Quién mantiene hipervisor y hosts | La organización | El proveedor | Cada uno, lo suyo |
| Gasto | Inversión inicial en equipos y licencias | Cuota periódica por uso o por usuario | Mixto |
| Crecer | Comprando equipos | Elasticidad del proveedor | Desbordar a la nube lo que no cabe |
| Datos | No salen | Salen al proveedor, pero siguen siendo responsabilidad del cliente | Se elige qué sale |
| Depende de Internet | No para el uso interno | Sí | Parcialmente |

### Caso práctico

Planteamiento (inventado para practicar): un centro de producción necesita dar puesto de trabajo a
treinta personas eventuales durante tres meses para una cobertura especial, a cinco técnicos de
grafismo que trabajan con aplicaciones de 3D, y a la plantilla de administración, que usa siempre las
mismas aplicaciones de gestión. Además, un técnico quiere probar una actualización de un servidor
antes de aplicarla.

Cómo se razona, con lo del tema:

1. Eventuales: el modelo basado en sesión de RDS es el de **«Trabajadores por tareas, aplicaciones
   empresariales, usuarios temporales»**, el de **«Mayor densidad de usuario, menor costo por
   usuario.»** Si no se quiere comprar hardware para tres meses, el equivalente en la nube es un
   grupo de hosts agrupado de Azure Virtual Desktop, que escala solo, o un PC en la nube con licencia
   Flex si cada persona lo usa pocas horas. Los perfiles, en FSLogix, porque en un grupo agrupado
   el usuario puede caer cada día en un host distinto.
2. Grafismo: VDI personal (**«Desarrolladores, usuarios avanzados, aplicaciones con mucha
   personalización»**) con GPU: **«Si los usuarios necesitan 3D o multimedia rico, planifique
   recursos de GPU»**. Si la latencia o el volumen de material obligan a que los datos no salgan del
   edificio, on-premise.
3. Administración: no necesita un escritorio entero; basta publicar sus aplicaciones como RemoteApp
   o entregarlas con App Attach, que se actualiza sin ventana de mantenimiento.
4. Acceso desde fuera: por la puerta de enlace de Escritorio remoto, que va por **«HTTPS (TCP 443)»**
   **«sin abrir puertos RDP internos»**, o con Azure Virtual Desktop, que no necesita abrir puertos de
   entrada; nunca publicando el 3389 a Internet.
5. La prueba del servidor: si es una máquina virtual de Hyper-V, se crea antes un punto de control
   (`Checkpoint-VM`); si la actualización falla, se aplica el punto de control. Si es un controlador
   de dominio, con cuidado, porque del punto de control estándar Microsoft advierte: **«Una instantánea no es una copia de seguridad completa y puede causar
   problemas de coherencia de datos con sistemas que replican datos entre distintos nodos, como Active
   Directory.»** Para probar sin tocar nada, mejor una copia en una red aislada.

## Lo que este tema no da, y dónde está

- La infraestructura real de la RTVA y de CSRTV (si usa virtualización de escritorios, con qué
  producto, en el CPD propio o en la nube, qué hipervisor): no consta en ningún documento publicado.
- VMware (vSphere, ESXi, Workstation) y Omnissa Horizon por dentro: no se ha podido leer la
  documentación de Broadcom (no se descarga en texto). El tema da su clasificación como hipervisores
  con IBM y Red Hat, y de Horizon sólo sus protocolos, con la arquitectura de referencia de Omnissa.
  Tampoco se dan Citrix Virtual Apps and Desktops en detalle, Xen más allá de su tipo y su dominio 0,
  ni Proxmox. El «cliente cero» (*zero client*) no aparece en las fuentes leídas.
- Las herramientas de gestión de KVM (QEMU en detalle, libvirt, `virsh`, `virt-manager`): no se han
  leído en fuente.
- Una definición de norma de «PC virtual» y de «workspace virtual»: no existe en las fuentes leídas;
  el tema da las de fabricante y su propia interpretación, y lo dice.
- Precios y licencias concretas (CAL de RDS por número, precio de Windows 365 o de Azure Virtual
  Desktop): fuera del enunciado y cambiantes.
- La edición Education en Hyper-V de Windows 11: una página de Microsoft la incluye y otras dos
  no; el tema da las dos versiones.
- El protocolo RDP por dentro (canales, códecs) y la clasificación de Azure Virtual Desktop en IaaS
  o PaaS: no constan en las páginas leídas.
- Otras partes de la materia: el almacenamiento (SAN, NAS, RAID) y las copias de seguridad, en el
  tema 3; Windows 11 (ediciones, características opcionales), en el 6; PowerShell, en el 7; Windows
  Server, Active Directory y la licencia de máquinas virtuales por edición, en el 8; Linux, en el 9;
  Microsoft 365, OneDrive y Teams, en el 11; redes, VLAN y VPN en general, en el 13; seguridad,
  acceso remoto seguro y certificados, en el 14.

## Trazabilidad

Todas las páginas se leyeron el 05-10-2026; las de Microsoft Learn, en español, con su traducción
automática y sus erratas (se citan tal cual y se marcan con *sic* donde estorban). La fecha de
actualización que muestra cada página va entre paréntesis.

| Fuente | Qué sostiene |
|---|---|
| NIST SP 800-125, *Guide to Security for Full Virtualization Technologies* (K. Scarfone, M. Souppaya y P. Hoffman, enero de 2011) | Definición de virtualización y de máquina virtual, virtualización completa, invitado, hipervisor o VMM, virtualización de aplicaciones y del sistema operativo, paravirtualización, emulación, *bare metal* frente a alojada, ventajas e inconvenientes, virtualización de escritorio |
| NIST SP 800-145, *The NIST Definition of Cloud Computing* (P. Mell y T. Grance, septiembre de 2011) | Definición de nube, cinco características, tres modelos de servicio, cuatro de despliegue |
| Microsoft Learn, «Virtualización de Hyper-V en Windows Server y Windows» (2025-08-13) | Hyper-V de tipo 1, ventajas, funciones (generación 2, blindadas, migración en vivo, clúster, Réplica, memoria dinámica, particiones de GPU, anidada, PowerShell Direct, herramientas), ediciones, Datacenter, Azure Local, Site Recovery |
| Microsoft Learn, «Requisitos del sistema para Hyper-V en Windows y Windows Server» (2025-08-16) | SLAT, extensiones, 4 GB, Intel VT/AMD-V, DEP, `Systeminfo.exe`, ediciones de Windows |
| Microsoft Learn, «Instalar Hyper-V» (2025-05-26) | `Install-WindowsFeature`, `Enable-WindowsOptionalFeature`, DISM, Panel de control, Server Core, Home, convivencia con VMware Workstation y VirtualBox |
| Microsoft Learn, «Uso de puntos de control para revertir las máquinas virtuales a un estado anterior» (2025-08-15) | Puntos de control estándar y de producción, órdenes, aplicar |
| Manual de Oracle VirtualBox, «Introduction» | Hipervisor alojado o de tipo 2, tipo 1, competencia entre hipervisores |
| linux-kvm.org, «Main Page» | KVM, módulos, código abierto, versiones de Linux y QEMU |
| Microsoft Learn, «Contenedores frente a máquinas virtuales» (2025-02-05) | Contenedor, máquina virtual, tabla comparativa, aislamiento de Hyper-V |
| Docker Docs, «What is Docker?» | Docker, imagen, contenedor, cliente-servidor |
| Microsoft Learn, «Información general sobre Servicios de Escritorio remoto en Windows Server» (2025-10-31) | RDS, roles, puerta de enlace por 443, CAL, modelos, ubicaciones, ventajas, seguridad, planificación |
| Microsoft Learn, «Habilitar Escritorio remoto en el equipo» (2025-08-16) | Ediciones anfitrionas, requisitos, pasos, conexión, NLA |
| Microsoft Learn, «Cambiar el puerto de escucha de Escritorio remoto en el equipo» (2025-08-16) | Puerto 3389, registro, cortafuegos, `mstsc.exe` |
| Microsoft Learn, «¿Qué es la aplicación Windows?» (2026-07-21) | Aplicación de Windows, plataformas, excepciones en Windows |
| Microsoft Learn, «¿Qué es Azure Virtual Desktop?» (2026-09-18) | AVD, retirada del clásico, multisesión, RemoteApp, sin puertos de entrada, escalado, AVD Hybrid |
| Microsoft Learn, «Azure terminología de Virtual Desktop» (2025-06-20) | Grupo de hosts personal y agrupado, grupos de aplicaciones, área de trabajo, sesiones, perfiles en FSLogix |
| Microsoft Learn, «¿Qué es Windows 365?» (2025-11-19) | PC en la nube, ediciones, relación 1:1, creación automática, facturación, Windows 365 Link |
| Microsoft Learn, «Espacio aislado de Windows» (2026-03-29) | Espacio aislado, ediciones, red por defecto, una sola instancia |
| Microsoft Learn, «¿Qué es FSLogix?» (2026-03-30) | Perfiles, controlador de filtro, aviso de Kerberos |
| Microsoft Learn, «Virtualización de aplicaciones (App-V) para información general del cliente de Windows» (2024-07-30) | Fin del soporte extendido de MDOP, cliente App-V, recomendación de App Attach |
| Microsoft Learn, «Asociación de aplicaciones en Azure Virtual Desktop» (2026-08-26) | App Attach, App-V, MSIX y Appx, imágenes, registro, recurso SMB |
| Microsoft Learn, «¿Qué es Azure Local?» (2026-09-15) | Azure Local, conectado o desconectado, precio por núcleo, motivos de lo local |
| Microsoft Learn, «Responsabilidad compartida en la nube» (2026-08-24) | IaaS, PaaS, SaaS, matriz de responsabilidades, responsabilidades que se conservan, riesgos de lo local |
| Amazon Web Services, «What is Amazon WorkSpaces?» | WorkSpaces, Personal y Pools |
| Citrix, «Citrix StoreFront Cloud Overview» (2026-06-22; a la que redirige la dirección de Citrix Workspace) | Acceso único a aplicaciones y escritorios virtuales |

Añadidas en el remate, leídas el 06-10-2026:

| Fuente | Qué sostiene |
|---|---|
| Xen Project Wiki, «Xen Project Software Overview» (2024-02-13) | Xen de tipo 1, dominio 0 y DomU, paravirtualización |
| Red Hat, «What is a hypervisor?» (2023-01-03) | Ejemplos de tipo 1 (KVM, Hyper-V, vSphere) y de tipo 2 (VMware Workstation, VirtualBox) |
| IBM Think, «What are hypervisors?» | ESXi de tipo 1, cliente ligero, agente de conexión, DaaS |
| Amazon Web Services, «What is a hypervisor?» | KVM como hipervisor híbrido |
| Amazon Web Services, «What is VDI?» | Cliente ligero, VDI totalmente gestionada frente a DaaS |
| Citrix, «HDX» (2025-09-06), «Technical overview» (2026-04-22) y «Adaptive transport» (2025-09-15) | HDX, fichero y pila ICA, transporte EDT y puertos |
| Citrix, «Overview · Citrix DaaS» (2026-06-24) | Citrix DaaS, despliegue híbrido |
| Omnissa Tech Zone, «Horizon 8 architecture» (revisión de 2026-06-24) | Blast, PCoIP y RDP en Horizon |

Cinco pasajes técnicos proceden de otro temario y se dan como oficio, sin norma ni fabricante
que los sostenga: la definición de virtualización en una línea, la tabla de tipos de
hipervisor, la lista de cuatro ventajas y la frase que separa máquina virtual y contenedor
(epígrafe 1); y la definición y utilidad del KVM sobre IP (epígrafe 2). Lo que esas líneas dicen
coincide con las fuentes citadas a su lado; la frase de la movilidad («se restaura como un fichero»)
es la única sin apoyo directo en ellas. También son oficio, y así se dicen, la ordenación en tres
escalones del epígrafe 2, la comparación entre KVM sobre IP y Escritorio remoto, la interpretación
de PC virtual y de *workspace* virtual, los dos cuadros de síntesis y el caso práctico.
