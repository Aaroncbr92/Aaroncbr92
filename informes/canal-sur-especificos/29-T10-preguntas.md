# Puesto 29 · Tema 10 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/10-virtualizacion-de-sistemas-y-escritorios.md`.

Quince preguntas tipo test de cuatro opciones, repartidas por las rúbricas del enunciado
(virtualización de sistemas, escritorio remoto, PC virtual, escritorio virtual, virtualización de
aplicaciones, workspace virtual, on-premise, cloud, híbrido), de teoría y de aplicación práctica (AP).
Distintas de las diez de la redacción. Contestadas **sólo con el tema**: entera / a medias / no.

1. **(Virtualización de sistemas)** Según el NIST SP 800-125, la virtualización en la que el
   hipervisor funciona directamente sobre el hardware, sin sistema operativo anfitrión, e incluso
   puede ir integrado en el firmware, es la:
   a) alojada (*hosted*) · b) *bare metal* o nativa · c) emulación de hardware · d) virtualización
   del sistema operativo.
   **b.** Ep. 1 «El hipervisor: tipo 1 y tipo 2». **Entera.**

2. **(Virtualización de sistemas)** ¿Cuál de estos productos es un hipervisor de tipo 1?
   a) Oracle VirtualBox · b) VMware Workstation · c) VMware ESXi · d) Espacio aislado de Windows.
   **c.** El tema da VirtualBox como tipo 2 y Hyper-V como tipo 1; nombra VMware Workstation sin
   clasificarlo y declara que ESXi no se da («Lo que este tema no da»). Por eliminación no se llega:
   quedan b y c sin criterio. **A medias.**

3. **(Virtualización de sistemas)** La técnica por la que el hipervisor ofrece al invitado interfaces
   propias en lugar de las del hardware normal, con acceso bastante más rápido a discos y red, es:
   a) la emulación de hardware · b) la paravirtualización · c) la virtualización anidada · d) la
   migración en vivo.
   **b.** Ep. 1 «Qué es virtualizar». **Entera.**

4. **(Virtualización de sistemas, AP)** Un técnico ejecuta `Systeminfo.exe` en un Windows 11 Pro y en
   la sección de requisitos de Hyper-V sólo ve «A hypervisor has been detected. Features required for
   Hyper-V will not be displayed.». Significa que:
   a) el procesador no tiene SLAT · b) ya hay un hipervisor funcionando en el equipo · c) la
   virtualización está desactivada en la UEFI · d) la edición no admite Hyper-V.
   **b.** Ep. 1 «Hyper-V: requisitos e instalación». **Entera.**

5. **(Virtualización de sistemas, AP)** Se configura una MV con `Set-VM -Name srv1 -CheckpointType
   ProductionOnly`. Si el punto de control de producción no se puede crear:
   a) se crea uno estándar · b) no se crea ninguno · c) se crea uno estándar sin memoria · d) se
   aplica el último existente.
   **b.** Ep. 1 «Puntos de control», tabla de órdenes (con `Production` se cae a estándar; con
   `ProductionOnly`, no). **Entera.**

6. **(Virtualización de sistemas)** Frente a una máquina virtual, un contenedor:
   a) lleva su propio núcleo · b) se basa en el núcleo del sistema operativo anfitrión y da un límite
   de seguridad menos sólido · c) puede ejecutar casi cualquier sistema operativo · d) no puede
   ejecutarse dentro de una máquina virtual.
   **b.** Ep. 1 «Máquinas virtuales y contenedores». **Entera.**

7. **(Escritorio remoto, AP)** Un usuario quiere conectarse por Escritorio remoto a su portátil de
   casa con Windows 11 Home:
   a) basta habilitarlo en Configuración > Sistema · b) Home no puede ser anfitrión de Escritorio
   remoto, sólo cliente · c) basta abrir el 3389 en el router · d) hay que activar antes NLA.
   **b.** Ep. 2 «Escritorio remoto de un equipo: RDP». **Entera.**

8. **(Escritorio remoto)** En RDS, el rol que mantiene las sesiones, equilibra la carga y vuelve a
   conectar al usuario con su sesión existente es:
   a) el Host de sesión · b) el Acceso web · c) el Agente de conexión · d) la Puerta de enlace.
   **c.** Ep. 2, tabla de roles de RDS. **Entera.**

9. **(Escritorio virtual)** El protocolo de visualización remota propio de Citrix para sus
   escritorios y aplicaciones virtuales es:
   a) RDP · b) HDX/ICA · c) Blast · d) SMB.
   **b.** El tema sólo trata RDP y declara que no da el protocolo por dentro ni Citrix Virtual Apps
   and Desktops; los protocolos de otros fabricantes no aparecen. **No.**

10. **(Escritorio virtual)** En una VDI, el equipo de usuario sencillo, normalmente sin disco local
    ni aplicaciones instaladas, que sólo presenta la sesión remota se llama:
    a) host de sesión · b) cliente ligero (*thin client*) · c) grupo de hosts · d) anfitrión.
    **b.** El tema dice que los puntos de conexión «simplemente presentan la interfaz de usuario
    remota» y menciona, en el NIST, clientes «ligeros o pesados», y Windows 365 Link como dispositivo
    hecho para ello; pero no define el cliente ligero. Se llega por eliminación. **A medias.**

11. **(Escritorio virtual, AP)** En un grupo de hosts personal de Azure Virtual Desktop, ¿cuántas
    sesiones admite cada host y cómo se actualiza?
    a) varias; con imágenes nuevas · b) una; con Windows Update, Configuration Manager u otras
    herramientas · c) una; sólo con imágenes nuevas · d) ilimitadas; por FSLogix.
    **b.** Ep. 3, tabla de términos y párrafo de diferencias personal/agrupado. **Entera.**

12. **(Virtualización de aplicaciones, AP)** Para App Attach en AVD con hosts de Windows 11, ¿qué
    formato de imagen se desaconseja y dónde se guardan las imágenes?
    a) CimFS; en el disco del host · b) VHD; en un recurso compartido SMB · c) VHDX; en OneDrive ·
    d) MSIX; en el registro.
    **b.** Ep. 3 «Virtualización de aplicaciones». **Entera.**

13. **(Cloud)** Según el NIST, el modelo de servicio en el que el cliente controla sistemas
    operativos, almacenamiento y aplicaciones desplegadas, pero no la infraestructura subyacente, es:
    a) SaaS · b) PaaS · c) IaaS · d) nube comunitaria.
    **c.** Ep. 4, tabla de modelos de servicio. **Entera.**

14. **(Cloud)** La oferta de escritorios virtuales completos gestionados por un proveedor en la nube
    y pagados por suscripción se conoce en el sector como:
    a) DaaS (escritorio como servicio) · b) PaaS · c) on-premise · d) nube comunitaria.
    **a.** El término DaaS no aparece en el tema; Windows 365 se da como SaaS según Microsoft y AVD
    «entre IaaS y PaaS». Quien estudie con el tema marcaría SaaS si estuviera entre las opciones.
    **No.**

15. **(On-premise / KVM sobre IP, AP)** En una sala de realización hay que entrar en la BIOS de un
    ordenador llevado al CPD. ¿Qué sirve?
    a) Escritorio remoto, porque viaja por la red · b) KVM sobre IP, porque transporta la consola sin
    necesitar sistema operativo arrancado · c) Azure Virtual Desktop · d) RemoteApp.
    **b.** Ep. 2 «KVM sobre IP». **Entera.**

## Recuento

Enteras 11 (1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 15); a medias 2 (2, 10); no 2 (9, 14).
