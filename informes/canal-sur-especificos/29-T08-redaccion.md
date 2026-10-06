# Puesto 29 · Tema 8 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real,
como en la investigación y en los temas 5 a 7). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/08-administracion-de-sistemas-windows-server.md`.
Material: `29-investigacion-B-sistemas.md` (§ Tema 8 y § 6.3). `AGRUPACION.tsv`: tema 8 «nuevo».
Fila de `informes/canal-sur-reuso/informatica.tsv`: RTVE `tecnica-informatica/03` y `/14`, 10 %,
«actualizar: no».

## Avance

- Ficha, siglas, enunciado, índice y epígrafe 1 (versión, Server Core, herramientas, tareas) guardados.
- Epígrafe 2 (directorio, AD DS, modelo lógico, confianzas, sitios, LDAP/Kerberos/puertos, niveles funcionales) guardado.
- Epígrafe 3 (controlador de dominio, FSMO, catálogo global, RODC, SYSVOL, instalación, DCDiag) guardado.
- Epígrafe 4 (cuentas predeterminadas, consolas, alta, operaciones, PowerShell y net user, grupos, predeterminados, derechos y permisos, UO, unión al dominio) guardado.
- Epígrafe 5 (DNS, DHCP, SMB/NTFS, DFS, impresoras, GPO, LAPS, caso práctico), «Lo que este tema no da» y «Trazabilidad» guardados.

## Fuentes leídas y fecha

La investigación (§ 8) dejaba huecos: definición de árbol, consolas `dsa.msc`/ADAC con cita, VMs por
edición, DFS, impresoras, permisos NTFS, Entra ID. Se descargaron como texto, con URL y fecha de
lectura (05-10-2026) en cabecera, 47 páginas de Microsoft Learn y del soporte técnico de Microsoft en
`fuentes/canal-sur/informatico/web/ws-*.txt` (nuevas). Se usan además, ya descargadas para el tema 6,
`w11-gpo.txt` y `w11-gpproc.txt`. Lista por contenido en la «Trazabilidad» del tema.

Huecos cubiertos con fuente: consola Usuarios y equipos de Active Directory y su procedimiento
completo (alta, grupos, restablecer, deshabilitar, eliminar, pestañas) en «Administrar cuentas de
usuario…»; ADAC y `dsac.exe` y la papelera de reciclaje; lista de herramientas RSAT de AD DS;
versión vigente y fechas en ISO (página «Información de versión», que además confirma «Windows Server
2025 es la versión de LTSC actual» con revisión del 14-09-2026); Server Core; Administrador del
servidor; Windows Admin Center; niveles funcionales (matriz); catálogo global (3268, caché de grupos
universales); puertos de AD (KB 179442); Kerberos; sitios; modelos de bosque y confianzas; grupos
predeterminados (Admins. del dominio, Operadores de cuentas, de copia, de servidores, de impresión,
etc.); cmdlets del módulo ActiveDirectory; `net user`; `Add-Computer`; `DCDiag`; DNS, DHCP, SMB,
`New-SmbShare`, NTFS, `icacls` (incluidos `(OI)` y `(CI)`), DFSN; Windows LAPS.

Huecos que siguen (declarados en «Lo que este tema no da»): árbol sin definición literal (se deduce
del asistente y se dice); licencia de VMs por edición; regla de combinación de permisos de recurso
compartido y NTFS; rol de servidor de impresión; directivas de contraseña/bloqueo con valores;
Entra ID (fuera del enunciado); `dsa.msc` (se dice que no figura en las páginas leídas).

Comprobación de literalidad por script (`scratchpad/t08check.py`, normaliza espacios, comillas y
acentos graves, y admite celdas de tabla): las 311 citas en negrita del tema se hallan tal cual en
las fuentes descargadas. En la primera pasada fallaron 16: 13 eran rótulos en negrita que no son
cita (pasados a cursiva) y 3 citas mal recortadas («en el valor más alto…», «Active Directory Domain
Services (AD DS) admite…», «…ámbitos de grupo siguientes:»), corregidas. Una cita mal atribuida
(«podrá suplantar», cuando la fuente dice «Si saben esto, podrán suplantar») se corrigió antes del
script.

## Qué se hizo

Cinco epígrafes en el orden del enunciado: 1 administración de sistemas Windows Server (versión,
ediciones, Server Core, herramientas, tareas); 2 Active Directory y el servicio de directorio
(definiciones, piezas de AD DS, bosque/dominio/árbol/UO, confianzas, sitios, LDAP, Kerberos,
puertos, niveles funcionales); 3 controlador de dominio (funciones, FSMO, catálogo global, RODC,
SYSVOL, instalación por PowerShell y por asistente, DCDiag); 4 gestión básica de usuarios (cuentas
predeterminadas, consolas, alta, restablecer/desbloquear/deshabilitar/eliminar, papelera, PowerShell
y `net user`, grupos y ámbitos, grupos predeterminados, derechos y permisos, UO y delegación, unión al
dominio); 5 recursos y servicios asociados (DNS, DHCP, SMB y NTFS, DFSN, impresoras, GPO en el
dominio con remisión al tema 6, LAPS, caso práctico completo). `indice.py`: 12.410 palabras, 43
epígrafes; índice sin cambios respecto al escrito a mano. `refutar_prosa.py`: 4 hallazgos residuales
(ADSI, KRBTGT, SYSVOL, RX), los cuatro presentados en las siglas como nombres; el script no lo
reconoce. Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni
`refutar_modo.py`. Ficha escrita a mano (el tema no está en `herramientas/portadas.tsv`).

Decisiones:

- Las GPO no se repiten: el tema 6 las desarrolla. Aquí sólo lo que añade el dominio (vínculo a
  sitio/dominio/UO, contenedor en AD y plantilla en SYSVOL, directivas de contraseña de dominio,
  precedencia, intervalos 90 + 30 min y 5 min en DC), con citas de las mismas fuentes que el tema 6.
- Fechas de soporte tomadas de la página de versión (ISO) y no de la de ciclo de vida (formato
  estadounidense con hora del Pacífico, que da un día más: «11/14/2029 6:59:59 AM»). La diferencia es
  de zona horaria; manda la página que fecha en ISO.
- Errata de fuente señalada en Trazabilidad: «Admins. del dominio» y «Administradores de dominio»
  para el mismo grupo; «Replication» y «Authentication» sin traducir; «puerta de enlace de
  predeterminada».
- «Directorio Activo como implementación de LDAP» (RTVE 03): no se copia como afirmación; el tema
  dice que AD es un servicio de directorio que habla LDAP «de ahí que se diga que» es la
  implementación de LDAP de Microsoft, y apoya LDAP en citas de Microsoft (filtros LDAP de los
  cmdlets, prueba LDAP de DCDiag, firma LDAP en 2025, puertos).
- Tabla de puertos de RTVE 03 (LDAP 389, LDAP sobre TLS 636): se sustituye por la tabla del artículo
  de Microsoft sobre cortafuegos de AD, que trae además 3268/3269, 88, 464, 53, 445, 135, 123 y 9389.

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata Windows Server ni Active
Directory. El tema 6 de este mismo puesto (GPO) no está cerrado y no se copia: se remite a él.

## Copiado de RTVE sin cambios

Los dos temas de RTVE de este tema están marcados «actualizar: no» en `informatica.tsv`. Pasajes
técnicos copiados literal, sin cambiar una palabra; único cambio, de formato: quitada la negrita,
porque RTVE no citaba fuente y en este tema negrita es cita. Se declaran como oficio en la
Trazabilidad del tema. Lo que se ha cambiado alrededor (entradillas) se indica y no forma parte del
pasaje.

| Pasaje en RTVE | Dónde va en el tema |
|---|---|
| RTVE `tecnica-informatica/14` § 5: «Lo mínimo que conviene llevar visto de administración:» y la tabla «Tarea / En Linux / En Windows Server» entera (cinco filas: usuarios y grupos, servicios, registro y auditoría, programas instalados, tareas programadas), texto de las celdas literal. Se omite la frase previa «El examen ha entrado por las órdenes y el enunciado pide más.» | § 1, «Las tareas del administrador» |
| RTVE `tecnica-informatica/03` § 1: «el directorio donde una organización guarda sus usuarios, sus equipos y sus permisos, y contra el que se autentica todo lo demás.» (entradilla «Qué es, en una línea:» cambiada por «Dicho en una línea:»; se omite la frase siguiente sobre las opciones falsas) | § 2, «Directorio y servicio de directorio» |
| RTVE `tecnica-informatica/03` § 1: «389 y 636 van juntos, como 80 y 443: el par sin cifrar y el cifrado.» (entradilla «El atajo que sí ayuda es que» cambiada por «El atajo de memoria:») | § 2, «LDAP, Kerberos y los puertos de Active Directory» |

Quitado por propio de RTVE: números de pregunta (14 y 83), «Ésa es la respuesta oficial», análisis
de las opciones falsas, «La pregunta se contesta…», las declaraciones de Trazabilidad de RTVE («No
se ha consultado su documentación»), que aquí ya no valen porque la documentación sí se ha leído.

## Otros ficheros tocados

- `fuentes/canal-sur/informatico/web/ws-*.txt`: 47 volcados de texto nuevos (URL y fecha en
  cabecera). Cinco intentos fallidos (URL inexistentes) se borraron. No se ha modificado ningún
  fichero existente.
- Ningún otro tema ni informe.

## Diez preguntas tipo test (comprobación de cobertura)

Repartidas por las rúbricas del enunciado; (AP) = aplicación práctica. Todas se contestan enteras
con el tema; no ha hecho falta ampliarlo.

1. (Administración de Windows Server) La versión LTSC actual de Windows Server y el fin de su soporte
   estándar: a) Windows Server 2022, 2026-10-13; b) Windows Server 2025, 2029-11-13; c) Windows Server
   2025, 2034-11-14; d) Windows Server 23H2, sin fecha. → **b** (c es el fin del extendido). § 1, «La
   versión vigente y sus ediciones». Entera.
2. (Administración de Windows Server) La opción Server Core: a) tiene escritorio con menos
   herramientas; b) no tiene escritorio por diseño y se administra por línea de órdenes, PowerShell,
   RSAT o Windows Admin Center; c) sólo existe en Datacenter; d) se administra con el Administrador del
   servidor instalado en Windows 11 Home. → **b** (Standard o Datacenter; RSAT no se instala en Home).
   § 1. Entera.
3. (Active Directory) Todos los dominios de un mismo bosque comparten: a) la partición de dominio y
   las UO; b) el esquema, la configuración y el catálogo global, y se unen por confianzas transitivas
   bidireccionales; c) el mismo nombre DNS; d) los mismos controladores de dominio. → **b**. § 2, «El
   modelo lógico». Entera.
4. (Servicio de directorio) Un cliente consulta el catálogo global por LDAP sin cifrar. Puerto: a)
   389; b) 636; c) 3268; d) 3269. → **c** (389/636 LDAP y su versión cifrada; 3269 el catálogo global
   cifrado). § 2, «LDAP, Kerberos y los puertos». Entera.
5. (Controlador de dominio) ¿Qué rol FSMO procesa las actualizaciones de contraseñas, y cuáles son
   de bosque? a) Maestro RID; infraestructura y PDC; b) Emulador de PDC; esquema y nomenclatura de
   dominios; c) Maestro de esquema; RID e infraestructura; d) Maestro de infraestructura; PDC y RID. →
   **b**. § 3, tabla de roles FSMO. Entera.
6. (Controlador de dominio) Sobre el RODC, ¿cuál es correcta? a) Puede ser maestro RID; b) no puede
   ser titular de roles de maestro de operaciones; c) replica por defecto las contraseñas de los
   miembros de Admins. del dominio; d) no puede ser catálogo global. → **b** (por defecto no replica
   contraseñas y las críticas se deniegan expresamente; conviene que sea DNS y catálogo global). § 3,
   «Controlador de dominio de solo lectura». Entera.
7. (AP, controlador) Tras `Install-WindowsFeature -name AD-Domain-Services -IncludeManagementTools`,
   para crear un bosque nuevo se ejecuta: a) `dcpromo.exe`; b) `Install-ADDSForest`; c)
   `Install-ADDSDomainController`; d) `New-ADDomain`. → **b**; instala DNS por defecto y pide la
   contraseña DSRM; `dcpromo` está en desuso desde 2012 y `Install-ADDSDomainController` añade un
   controlador. § 3, «Instalar AD DS». Entera.
8. (AP, gestión de usuarios) Un usuario no puede iniciar sesión porque escribió mal la contraseña
   demasiadas veces. Lo correcto: a) deshabilitar y volver a habilitar la cuenta; b) `Unlock-ADAccount`
   o Restablecer contraseña marcando la casilla de desbloqueo; c) eliminar la cuenta y crearla de nuevo;
   d) `gpupdate /force` en su equipo. → **b** (bloquear no es deshabilitar; eliminar pierde grupos y
   permisos salvo papelera). § 4, «Restablecer, desbloquear…» y cmdlets. Entera.
9. (Gestión de usuarios) Grupo que puede tener como miembros cuentas de cualquier dominio de confianza
   pero sólo recibe permisos dentro de su propio dominio: a) global; b) universal; c) dominio local; d)
   distribución. → **c** (el de distribución no entra en DACL). § 4, «Grupos: tipos y ámbitos». Entera.
10. (Recursos y servicios asociados) Para impedir que un servidor DHCP no autorizado reparta
    direcciones en la red del dominio: a) una reserva; b) la autorización del servidor DHCP en Active
    Directory; c) la conmutación por error; d) un intervalo de exclusión. → **b**. § 5, «DHCP».
    Entera.

Rúbricas cubiertas sin pregunta propia en estas diez y que el tema también contesta: recursos
compartidos (§ 5: SMB 3.1.1, puerto 445, `New-SmbShare` con sus cuatro niveles, enumeración basada en
el acceso, letras de `icacls`, orden canónico de las ACE, `(OI)(CI)`), DNS como localizador del
controlador, DFSN, impresoras publicadas por ubicación, GPO en el dominio, LAPS, papelera de reciclaje
(deshabilitada por defecto, irreversible, nivel 2008 R2), efecto de deshabilitar con sesión abierta,
`New-ADUser` sin contraseña crea la cuenta deshabilitada, `Add-Computer`, niveles funcionales.
