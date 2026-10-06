# Tema 8 del específico de Operador/a Informático · Administración de sistemas Windows Server

**Siglas**: AD DS, LDAP, DNS, DHCP, SMB, UNC, DFSN/DFSR/FRS, NTFS, ReFS, UO, GPO, FSMO, PDC, RID, SID, RODC, DSRM, KDC, TGT, SAM, DN, DACL, RSAT, ADAC, LTSC, LAPS, ESE.

Esqueleto para repasar, no resumen: fuente delante de cada línea (MS Learn salvo indicación); «oficio» = sin fuente.

<!-- indice -->
- 1. Administración de sistemas Windows Server
- 2. Active Directory y el servicio de directorio
- 3. El controlador de dominio
- 4. Gestión básica de usuarios
- 5. Recursos y servicios asociados
<!-- /indice -->

## 1. Administración de sistemas Windows Server

- Info de versión: LTSC y canal anual; Windows Server 2025 = LTSC actual; ciclo de vida fijo. Disponible/fin estándar/fin extendido: 2025: 2024-11-01/2029-11-13/2034-11-14; 2022: 2021-08-18/2026-10-13/2031-10-14; 2019: 2018-11-13/fin de actualización/2029-01-09; 2016: 2016-08-02/fin de actualización/2027-01-12.
- Ciclo de vida: Datacenter, Datacenter: Azure Edition, Standard (+ Essentials).
- Novedades 2025: Hotpatch (Azure Arc, preliminar); ESE 32k opcional; firma LDAP por defecto; TLS 1.3.
- Server Core: Standard o Datacenter; la mayoría de roles, no todos; menos superficie de disco y de ataque; sin escritorio, accesibilidad, configuración inicial ni audio; se administra por línea de comandos, PowerShell, RSAT, Windows Admin Center. Alternativa: experiencia de escritorio.
- Administrador del servidor: consola centralizada, servidores locales y remotos, roles y características; no administra clientes.
- RSAT (KB 2693643): no en Home/Standard, sí Professional/Enterprise; en el servidor, característica. Herramientas AD DS: ADAC, Dominios y confianzas, Sitios y servicios, Usuarios y equipos, Editor ADSI, módulo ActiveDirectory, `DCDiag.exe`, `RepAdmin.exe`, `NTDSUtil.exe`, `NetDom.exe`, `DSAdd.exe`, `DSQuery.exe`, `NSLookup.exe`.

## 2. Active Directory y el servicio de directorio

- Intro AD DS: directorio = estructura jerárquica de objetos de red (servidores, volúmenes, impresoras, cuentas); servicio de directorio = los almacena y sirve; autenticación y control de acceso; base de datos distribuida.
- Cuatro piezas: esquema (clases, atributos, restricciones, formato de nombres); catálogo global; consulta e índice; replicación (copia completa por DC).
- Bosque: esquema, configuración (sitios y replicación) y catálogo global comunes; confianzas transitivas bidireccionales automáticas.
- Dominio: partición del bosque; identidad, autenticación, autorización, confianzas externas. NetBIOS 15 caracteres.
- Árbol (síntesis del tema): «Dominio secundario» (`emea.corp.contoso.com`) o «Dominio de árbol» (`fabrikam.com`); árbol = DNS contiguo.
- UO: jerarquía en un dominio, para directiva de grupo y delegación; no es grupo de seguridad.
- Sitios (Sitios y servicios): replicación, afinidad de cliente, SYSVOL, DFSN, ubicación; dentro del sitio rápida, sin compresión, por actualización; entre sitios comprimida, WAN; sitio por IP del cliente; DC por SRV del sitio.
- Kerberos: KDC en todos los DC; TGT; autenticación mutua (NTLM no); inicio único. Hora: marcas de tiempo; *Maximum tolerance for computer clock synchronization* (Kerberos Policy), Default Domain Policy 5 minutes; DCDiag CheckSecurityError `/ReplSource` <300 s; 10 minutos desviado = fallo.
- W32Time: miembro sincroniza con DC local; emulador de PDC del dominio raíz = mejor fuente (NTP/GPS); otro origen = fallo Kerberos.
- Puertos (KB 179442, 2008 y posteriores): LDAP 389 TCP/UDP; LDAP SSL 636 TCP; GC 3268 TCP; GC SSL 3269 TCP; Kerberos 88 TCP/UDP; cambio contraseña Kerberos 464 TCP/UDP; DNS 53 TCP/UDP; SMB 445 TCP; RPC 135 TCP; W32Time 123 UDP; ADWS 9389 TCP; RPC dinámico 49152-65535 TCP. 445 en confianzas sólo para crearla; sin LDAP SSL/TLS sobran 636 y 3269.
- Niveles funcionales: funcionalidades y SO de los DC; no afectan a miembros ni estaciones; dominio ≥ bosque, nunca inferior; el más alto posible. Nivel 2025: sólo DC 2025; 2016: DC 2025 a 2016; 2012 R2: DC 2022 a 2012 R2. Sin nivel 2019/2022 (usan 2016); 2025 = 32k, `DomainLevel 10`/`ForestLevel 10`; bosques nuevos mínimo 2016; promover réplica exige dominio en 2016+; 2016 exige DFSR en SYSVOL.

## 3. El controlador de dominio

- DC: AD DS promovido; autentica (KDC), replicación multimaestro; localizado por DNS.
- FSMO (5): dominio, emulador de PDC (actualizaciones de contraseñas; DC con error de contraseña reenvía al PDC; uno por dominio); maestro RID (grupos de RID, identificador único); maestro de infraestructura (entidades de otros dominios en grupos; no con catálogo global salvo todos GC o un dominio). Bosque, maestro de esquema; maestro de nomenclatura (dominios y particiones).
- Asignación: primer DC del bosque (2) y del dominio (3); cambios sólo al crear dominio, degradar titular o por administrador; maestros en espera.
- Consultar: `netdom query fsmo` (elevado; AD DS o RSAT). Usuarios y equipos (PDC, RID, infraestructura; pestañas PDC, Infraestructura, Grupo de RID); complemento Esquema (`regsvr32 schmmgmt.dll`); Dominios y confianzas (nomenclatura).
- KB 255504: transferir (titular accesible, degradar, mantenimiento); tomar (titular falla, SO reinstalado o equipo inexistente). Permisos: Administradores de empresa (esquema, nomenclatura); Admins. de dominio (PDC, RID, infraestructura).
- `Move-ADDirectoryServerOperationMasterRole -Identity <destino> -OperationMasterRole PDCEmulator|RIDMaster|InfrastructureMaster|SchemaMaster|DomainNamingMaster`; transfiere (recomendado); `-Force` transfiere y si no, toma; remoto. `ntdsutil`: `roles`, `connections`, `connect to server`, `q`, `transfer`/`seize` (`seize rid master`, `seize pdc`, `seize naming master`); GUI transfiere (Cambiar), tomar exige `ntdsutil` o cmdlet.
- Tomar RID: cmdlet +30 000, `ntdsutil` +10 000. Antiguo titular: quitarlo; reutilizar = reconstruir, limpiar metadatos con `ntdsutil`, promover.
- Catálogo global: puerto 3268; un dominio, todos GC; recomendado al instalar DC; ubicaciones con más de 100 usuarios; alternativa caché de grupos universales.
- RODC: copia no modificable, sucursales con WAN caída; sin FSMO; no replica contraseñas (ni de Admins. del dominio); directiva de replicación de contraseñas. Dos fases: Admins. del dominio crean cuenta RODC, luego se adjunta servidor (delegado). Único servidor: también DNS y GC.
- SYSVOL: carpetas en cada DC; GPO, scripts de inicio/apagado, inicio/cierre de sesión; DFSR; 2016 última con FRS.
- Credenciales: nuevo bosque = Administrador local; dominio secundario o árbol = Administradores de empresas; DC adicional = Admins. del dominio.
- PowerShell: `Install-WindowsFeature -name AD-Domain-Services -IncludeManagementTools` (sin modificador, sin consolas). ADDSDeployment: `Install-ADDSForest` (`-DomainName "corp.contoso.com"`, DNS por defecto), `Install-ADDSDomain`, `Install-ADDSDomainController`, `Add-ADDSReadOnlyDomainControllerAccount`; pruebas `Test-ADDSForestInstallation`, `Test-ADDSDomainControllerInstallation`. DSRM: contraseña no en claro en scripts; quien la sepa suplanta al DC.
- Asistente: Administrar > Agregar roles y características > Active Directory Domain Services > «Promover este servidor a un controlador de dominio». Páginas: implementación (DC a dominio existente, nuevo dominio, nuevo bosque); opciones del DC (niveles, DNS, GC o RODC, sitio, DSRM); DNS, RODC, NetBIOS/origen; rutas de base de datos, registros y SYSVOL (no ReFS); `adprep`, «Ver script», requisitos, reinicio automático. `dcpromo.exe` en desuso desde 2012.
- DCDiag: estado de DC, derechos administrativos; `/s:`, `/test:DNS`.

## 4. Gestión básica de usuarios

- Predeterminadas (contenedor Usuarios, no mover): Administrador (no se elimina ni bloquea; sí cambiar o deshabilitar; SID acaba en 500), Invitado (deshabilitada, contraseña en blanco), KRBTGT (servicio del KDC; no se elimina, renombra ni habilita). Locales en DC sólo antes de AD DS. Una cuenta por usuario; SID único.
- Usuarios y equipos (`dsa.msc`; equipo en dominio): Admins. de dominio y de empresa; Operadores de cuenta «no pueden administrar grupos o permisos» (contradice la página de grupos; el tema sigue la de grupos). ADAC (`dsac.exe`): cuentas, papelera, directivas de contraseña detalladas.
- Alta (Acción > Nuevo > Usuario): obligatorios «Nombre completo» y «Nombre de inicio de sesión de usuario». Casillas: cambiar contraseña en el siguiente inicio; no puede cambiarla; nunca expira; cuenta deshabilitada.
- Pestañas: General; Cuenta («Horas de inicio de sesión», «Iniciar sesión en», «Desbloquear cuenta», «Expira la cuenta»); Perfil; Miembro de; Objeto (proteger contra eliminación).
- Restablecer: Acción > Restablecer contraseña, con casilla de desbloqueo. Bloqueo = intentos erróneos sobre el máximo (`Unlock-ADAccount`), por el sistema; deshabilitar = administrador (sesión iniciada sigue, sin nuevos inicios; Habilitar cuenta). Eliminar: deshabilitar antes; recuperar con papelera o restauración autoritativa con copia.
- Papelera de AD: restaura grupos y derechos; no habilitada por defecto, irreversible; nivel 2008 R2+, Admins. del dominio; ADAC («Habilitar Papelera de reciclaje») o `Enable-ADOptionalFeature`.
- Delegación: control por ACL de la UO; UO homogéneas.
- Cmdlets: `New-ADUser` (exige `-SamAccountName`; sin `-Path`, contenedor por defecto; sin contraseña, deshabilitada; `Import-Csv` + `New-ADUser` en masa); `Get-ADUser`; `Set-ADAccountPassword` (`-Reset`); `Unlock-ADAccount`; `Disable-ADAccount`/`Enable-ADAccount`; `Search-ADAccount` (`-LockedOut`, `-AccountDisabled`, `-PasswordExpired`); `Add-ADGroupMember`; `New-ADGroup` (`Name`, `GroupScope`); `New-ADOrganizationalUnit` (protegida).
- Identidad: DN, GUID, SID o nombre SAM; DN `CN=Patti Fuller,OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM`.
- `net user`: `/domain` (DC del dominio principal), `/active:{yes | no}`.
- Grupos: seguridad (permisos, DACL) y distribución (correo, no en DACL). Ámbitos: universal (cuentas, globales y universales del bosque; permisos en el bosque o bosques confiables); global (cuentas y globales del mismo dominio; permisos en el bosque y dominios de confianza); dominio local (cuentas, globales y universales de cualquier dominio o de confianza, locales del mismo dominio; permisos en su dominio); Builtin Local (inmutable). Global → universal si no es miembro de otro global.
- Predeterminados (Builtin = locales de dominio; Usuarios = globales y locales): Admins. del dominio (administran el dominio; en Administradores de todos los equipos unidos, DC incluidos); Administradores de empresas y de esquema (sólo dominio raíz; cambios en el bosque, esquema); Operadores de cuentas (usuarios, grupos locales y globales; sesión local en DC; no modifican derechos de usuario ni administran Administrador, administradores ni los grupos Administradores, Operadores de servidores, cuentas, copias, impresión); Operadores de copias (copiar y restaurar sin permisos); Operadores de servidores (DC; crear y eliminar recursos compartidos, detener e iniciar servicios); Operadores de impresión (impresoras de DC; cargan controladores); Usuarios del dominio (todas las cuentas); Equipos del dominio (salvo DC); Invitados del dominio; Usuarios de escritorio remoto.
- Derecho = acción en un equipo (copias, apagar); permiso = regla de un objeto. Permisos a grupos.
- `Add-Computer -DomainName Domain01 -Restart`; `Add-Computer -DomainName Domain02 -OUPath "OU=testOU,DC=domain,DC=Domain,DC=com"`; crea cuenta; entra en Equipos del dominio; Admins. del dominio administrador.

## 5. Recursos y servicios asociados

- DNS: resolución predeterminada de Windows; en bosque nuevo se instala con AD; cliente detecta DC y convierte nombres. Integración con AD (actualizaciones seguras), dinámicas, DNSSEC, reenvío y reenvío condicional. Registros: tema 13.
- DHCP (RFC 2131 y 2132, IETF): IP, máscara, puerta de enlace; rol opcional. Grupo, exclusiones, reservas (oficio: impresoras), concesión, opciones (Enrutador, Servidores DNS, Nombre de dominio DNS; oficio: DC). Autorización en AD; DNS dinámico; conmutación por error (dos servidores, un ámbito).
- SMB: archivos sobre TCP/IP; servidor comparte archivos, impresoras, canalizaciones con nombre; cliente `\\server\share`; SMB 3.1.1 (Windows 10 1607+, Server 2016+), negocian el más alto; 445/TCP.
- Compartido + NTFS (archivada, Server 2008, 03-07-2012, inglés): independientes; se aplica el más restrictivo; NTFS en local y remoto; compartido sólo por red.
- `New-SmbShare`: `-FullAccess`, `-ChangeAccess`, `-ReadAccess`, `-NoAccess`; `-FolderEnumerationMode AccessBased` (desactivado por defecto).
- `icacls` (DACL; reemplaza `cacls`): `N` sin acceso, `F` completo, `M` modificar, `RX` lectura y ejecución, `R` sólo lectura, `W` sólo escritura, `D` eliminar. Orden: denegaciones explícitas, concesiones explícitas, denegaciones heredadas, concesiones heredadas. `/grant`, `/deny`, `/t`, `/inheritancelevel:d`; `(OI)` objeto, `(CI)` contenedor.
- Ejemplo: `icacls D:\Datos\Informativos /grant "Contoso\Informativos-Modificar:(OI)(CI)M"`.
- DFS: DFSN agrupa carpetas en espacios de nombres (`\\Contoso\Public`); referencia al destino; basado en dominio (metadatos en AD DS); destino del sitio.
- Impresoras: objetos de AD, atributo de ubicación, permisos a grupos, Operadores de impresión.
- GPO (tema 6): vinculadas a sitios, dominios, UO; contenedor en partición de dominio, plantilla en SYSVOL; gana el más cercano; cliente 90 minutos + hasta 30; DC cinco.
- Contraseña y bloqueo (Account Policies, nivel dominio; Default Domain Policy): *Enforce password history* 0-24, 24; *Maximum password age* 0 = nunca, 42 days; *Minimum password age* 1 day; *Minimum password length* 0 = sin contraseña, Seven characters (aconseja 8); *complexity* Enabled (sin nombre de cuenta ni completo, tres de cinco categorías); *Account lockout threshold* 1-999, 0 = nunca bloquea, 0; *Account lockout duration* 0 = hasta desbloqueo manual, Not defined; *Reset account lockout counter after* Not defined; duración ≥ restablecimiento; líneas base 10 y 15 minutos; Administrador integrado excluido.
- Detalladas (*fine-grained*, ADAC): usuarios, inetOrgPerson y grupos globales de seguridad; no a una UO.
- Windows LAPS: contraseña de administrador local única, respaldada (Entra ID o AD), también DSRM; Windows 11 23H2+ y Server 2025; antes con actualización del 11-04-2023 (Windows 10 soporte terminó 14-10-2025).
- No da el tema: sistemas reales RTVA/CSRTV; licencias de VM; permisos especiales NTFS; servidor de impresión; contraseña >14; Entra ID; definición literal de árbol. Remite: GPO 6; PowerShell 7; DNS y DHCP 13; seguridad 14; virtualización 10; copias 3.
