# Puesto 29 · Tema 8 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). No corrijo: el tema queda como estaba.
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/08-administracion-de-sistemas-windows-server.md`
(1.141 líneas, 12.879 palabras según `wc -w`).

## Alcance

- «Copiado del común»: nada. «Copiado de RTVE sin cambios»: la tabla «Tarea / En Linux / En Windows
  Server» (§ 1), «el directorio donde una organización guarda…» (§ 2) y «389 y 636 van juntos…» (§ 2);
  la lente de exactitud los salta y la de cobertura mira el tema entero.
- Fuentes: los volcados `fuentes/canal-sur/informatico/web/ws-*.txt` (cabecera «Leído: 2026-10-05»),
  releídos el **06-10-2026** sobre los pasajes concretos. No se descargó nada nuevo.
- Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Lente 1 · Exactitud

Comprobado contra la fuente y correcto (muestra de la prosa en redonda): tabla de fechas ISO
(ws-release); ediciones (ws-life); Server Core sin accesibilidad/OOBE/audio (ws-core); grupos de
servidores en el Administrador del servidor (ws-servermgr); Hotpatch en Azure Arc y preliminar, ESE 8k
y 32k, `DomainLevel 10`, TLS 1.3 (ws-new2025); matriz de niveles funcionales celda a celda y la nota de
DFSR bajo el nivel 2016 (ws-levels); tabla de puertos contra la sección «Windows Server 2008 y versiones
posteriores» (ws-firewall); reparto 3+2 de FSMO, primer controlador, excepciones del maestro de
infraestructura, «a medida que se agotan» (ws-fsmo); catálogo global, 3268, bosque de un solo dominio,
100 usuarios, caché de grupos universales (ws-gc); credenciales de instalación, `Install-ADDSForest` con
DNS por defecto, DSRM, asistente (páginas 2, 4 y 5, ReFS, Ver script, reinicio), dcpromo (ws-install);
RODC como DNS y GC en sucursal (ws-install, ws-rodc); DCDiag (ICMP, RPC, `/s:`, `/test:`, derechos
administrativos); cuentas predeterminadas (SID -500, no moverlas, Invitado deshabilitada) (ws-defusers);
ámbitos de grupo, conversiones, Operadores de servidores (sólo en DC, recursos compartidos, servicios),
Usuarios de escritorio remoto, Admins. del dominio en Administradores de cada equipo unido (ws-groups);
Kerberos (TGT, sin contactar con el DC, NTLM, SSO) (ws-kerberos); SMB 3.1.1 (ws-smb); LAPS
(plataformas y fin de Windows 10) (ws-laps); agente de retransmisión DHCP (ws-dhcp); DFSN (ws-dfsn);
ADAC y `dsac.exe` (ws-adac, ws-recycle).

### Hallazgos

| # | Gravedad | Error | Pasaje | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|
| G1 | Grave | 6 / 9 (fuentes contradictorias sin declarar) | § 4, «Usuarios y equipos de Active Directory y el Centro de administración»: Operadores de cuenta **«pueden crear, modificar y eliminar cuentas de usuario, pero no pueden administrar grupos o permisos.»**; y § 4, «Los grupos predeterminados», fila Operadores de cuentas: **«pueden crear y modificar la mayoría de los tipos de cuentas, incluidas las cuentas para los usuarios, los grupos locales y los grupos globales.»** | Las dos citas son literales (ws-aduc l. 18; ws-groups l. 385), pero se contradicen sobre los grupos, y el tema las da en dos epígrafes sin advertirlo. Una pregunta («¿pueden los Operadores de cuentas crear grupos globales?») tiene dos respuestas en el tema (pregunta 8). ws-groups añade además que pueden iniciar sesión localmente en los DC y la lista de cuentas y grupos que no pueden administrar (Administradores, Operadores de servidores, de cuentas, de copia, de impresión) | Declarar la contradicción entre las dos páginas de Microsoft y decir que la de grupos de seguridad, que es la que define el grupo, incluye grupos locales y globales; completar la fila con la lista de grupos protegidos de ws-groups |
| M1 | Menor | 6 (salvedad omitida) | § 2, tabla «Los puertos del controlador de dominio» | ws-firewall da además el intervalo dinámico **49152-65535/TCP** para «RPC para LSA, SAM, NetLogon (*)», «FRS RPC» y «DFSR RPC», y la nota (**) del 445: **«Para el funcionamiento de la confianza este puerto no es necesario, se usa solo para la creación de confianza.»** El tema presenta la tabla como completa | Añadir la fila del intervalo dinámico RPC (y que Windows Server 2008 y posteriores lo usan) y la nota del 445 (ya apuntada en la verificación) |
| M2 | Menor | 6 (salvedad omitida, cita recortada) | § 1, novedades: **«todas las nuevas implementaciones de Active Directory requieren la firma LDAP (sellado) de forma predeterminada»** | La frase sigue: «para toda la comunicación del cliente LDAP después de un enlace de capa de autenticación y seguridad simple (SASL)» (ws-new2025 l. 197). El recorte generaliza a todo LDAP | Completar la cita o decir «tras un enlace SASL» |
| M3 | Menor | 6 (salvedad omitida) | § 2, «Niveles funcionales»: se cita **«Los nuevos bosques … deben tener un nivel funcional de Windows Server 2016 o posterior.»** | La frase siguiente: «La promoción de una réplica de Active Directory o AD LDS requiere que el dominio o conjunto de configuración existente ya se esté ejecutando con un nivel funcional de Windows Server 2016 o posterior.» (ws-new2025 l. 159). Es el requisito práctico para añadir un DC 2025 a un dominio existente | Añadir la segunda frase |
| M4 | Menor | 9 | § 3, RODC: «está pensado para sedes donde el servidor no está bien protegido» | Las fuentes leídas dan como objetivo **«los escenarios de sucursales, en los que puede que la red de área extensa no esté disponible»** (ws-rodc l. 169); la seguridad física no figura | Sustituir por la cita de ws-rodc, o declararlo oficio |

Sin hallazgo en: cita cruzada (1; las remisiones a epígrafes y a los temas 3, 6, 7, 10, 11, 13 y 14,
comprobadas), ley por reglamento (2), recuentos (3: cinco FSMO, tres ámbitos, cuatro piezas, once
puertos), «podrá»/«deberá» (4), siglas (5; los residuales ADSI, KRBTGT, SYSVOL, RX están presentados),
redacción derogada (7), artículo mal (8).

## Lente 2 · Cobertura

Las cinco rúbricas del enunciado (Active Directory, servicio de directorio, controlador de dominio,
gestión básica de usuarios, recursos y servicios asociados) tienen epígrafe y van en su orden. Quince
preguntas en `29-T08-preguntas.md`: **10 enteras, 2 a medias (8, 15), 3 no (10, 11, 12)**.

| # | Laguna | Rúbrica | Propuesta |
|---|---|---|---|
| L1 | Combinación de permisos de recurso compartido y NTFS (el más restrictivo de los dos al acceder por red; sólo NTFS en local). Declarada en «Lo que no da», pero es pregunta clásica de práctica (pregunta 10) | Recursos | Leer una página de Microsoft Learn que la dé (p. ej. «Permisos de recursos compartidos y NTFS» en la documentación de Servicios de archivos y almacenamiento) y añadir un párrafo en «Carpetas compartidas» |
| L2 | Consultar, transferir y tomar (*seize*) roles FSMO: `netdom query fsmo`, `Move-ADDirectoryServerOperationMasterRole` (con `-Force` para tomar), `ntdsutil` (pregunta 11) | Controlador de dominio | Añadir un párrafo en «Los roles de maestro de operaciones», con la página «Transferir o tomar roles FSMO» y la referencia del cmdlet |
| L3 | Hora y Kerberos: tolerancia de sincronización de reloj (5 minutos por defecto) y el emulador de PDC como origen de hora del dominio (pregunta 12) | Servicio de directorio | Añadir dos frases en «LDAP, Kerberos y los puertos», con la página de la directiva «Tolerancia máxima para la sincronización de los relojes del equipo» y la de jerarquía de W32Time |
| L4 | Directivas de contraseña y bloqueo de cuenta del dominio (umbral, duración, restablecimiento del contador; longitud, historial, vigencia) — declarada en «Lo que no da»; el tema sólo dice que se fijan en el dominio (pregunta 15) | Gestión de usuarios | Leer las páginas de «Directiva de bloqueo de cuentas» y «Directiva de contraseñas» de Microsoft Learn y añadir una tabla breve en § 5, «Directivas de grupo» |

## Recuento

Graves: 1 (G1). Menores: 4 (M1-M4). Lagunas: 4 (L1-L4).

## Otros ficheros tocados

Sólo `29-T08-preguntas.md` y este informe. El tema no se ha modificado.
