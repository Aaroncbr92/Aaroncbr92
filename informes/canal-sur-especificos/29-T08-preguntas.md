# Puesto 29 · Tema 8 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Quince preguntas tipo test de cuatro opciones sobre
`temas/canal-sur-especificos/29-operador-a-informatico/08-administracion-de-sistemas-windows-server.md`,
contestadas **sólo con el tema**. (AP) = aplicación práctica. Distintas de las diez del informe de
redacción. Veredicto: entera / a medias / no.

1. (Administración de Windows Server) ¿Qué NO tiene la opción de instalación Server Core?
   a) PowerShell; b) la mayoría de los roles de servidor; c) herramientas de accesibilidad, experiencia
   de configuración inicial y audio; d) administración remota con RSAT.
   → **c**. § 1, «Server Core y Experiencia de escritorio». **Entera.**

2. (Administración, AP) Un técnico quiere instalar RSAT en su portátil con Windows Home para
   administrar el dominio. a) Se instala desde la Tienda; b) no se puede: sólo en ediciones Professional
   o Enterprise; c) basta activar la característica en Configuración; d) sólo con Server Core.
   → **b** (con la salvedad, que el tema dice, de que el artículo leído es de Windows 10/7). § 1, «Las
   herramientas de administración». **Entera.**

3. (Active Directory) Un controlador con Windows Server 2012 R2 en un dominio cuyo nivel funcional es
   Windows Server 2016: a) admitido; b) no admitido; c) admitido sólo como RODC; d) admitido si el
   bosque está en 2012 R2. → **b**. § 2, matriz de «Niveles funcionales». **Entera.**

4. (Servicio de directorio) El puerto del cambio de contraseña de Kerberos: a) 88; b) 135; c) 464;
   d) 9389. → **c** (88 es Kerberos, 135 el asignador RPC, 9389 ADWS). § 2, tabla de puertos. **Entera.**

5. (Servicio de directorio) Para que los dominios `contoso.com` y `fabrikam.com` estén en el mismo bosque
   con espacios de nombres distintos, el segundo se añade como: a) dominio secundario; b) dominio de
   árbol; c) unidad organizativa; d) bosque de recursos. → **b**. § 2, «El modelo lógico», *Árbol*
   (síntesis declarada). **Entera.**

6. (Controlador de dominio) Un usuario cambia su contraseña y al minuto inicia sesión contra otro
   controlador al que aún no ha llegado el cambio. ¿Qué ocurre? a) Se rechaza siempre; b) ese controlador
   reenvía la autenticación al emulador de PDC antes de rechazarla; c) la consulta va al maestro RID;
   d) se bloquea la cuenta. → **b**. § 3, roles FSMO. **Entera.**

7. (Controlador de dominio) En un bosque de varios dominios donde no todos los controladores son
   catálogo global, el maestro de infraestructura: a) debe ir en un catálogo global; b) no debe ir en un
   catálogo global, porque no funcionará; c) debe ir en un RODC; d) da igual dónde vaya.
   → **b**. § 3, roles FSMO. **Entera.**

8. (Gestión de usuarios / grupos predeterminados) Los miembros de Operadores de cuentas: a) pueden crear
   y modificar grupos globales y locales; b) no pueden administrar grupos; c) pueden administrar la
   cuenta Administrador; d) pueden modificar derechos de usuario.
   → El tema da **a** en «Los grupos predeterminados» («pueden crear y modificar la mayoría de los tipos de
   cuentas, incluidas … los grupos locales y los grupos globales») y **b** en «Usuarios y equipos de
   Active Directory…» («no pueden administrar grupos o permisos»), sin advertir la contradicción.
   **A medias** (hallazgo G1 de la refutación).

9. (Recursos y servicios, AP) Al crear una GPO vinculada a una UO, ¿dónde queda su plantilla?
   a) En el registro del controlador; b) en la carpeta SYSVOL de cada controlador; c) en la partición
   de esquema; d) en el catálogo global. → **b** (el contenedor, en la partición de dominio). § 5,
   «Directivas de grupo», y § 3, «SYSVOL». **Entera.**

10. (Recursos y servicios, AP) Una carpeta compartida da Lectura en el recurso compartido a un grupo y
    Modificar en NTFS al mismo grupo. Un miembro accede por `\\servidor\recurso`. Su acceso efectivo:
    a) Modificar; b) Lectura (el más restrictivo de las dos capas); c) Control total; d) ninguno.
    → El tema dice expresamente que no da la regla de combinación. **No** (laguna L1).

11. (Controlador de dominio, AP) El controlador que tiene el rol de maestro RID se va a retirar. Para ver
    quién tiene los roles y moverlos: a) `netdom query fsmo` y `Move-ADDirectoryServerOperationMasterRole`
    (o `ntdsutil`); b) `dcdiag /test:DNS`; c) `Get-ADUser -Filter *`; d) no hace falta, los roles migran
    solos. → El tema dice que fuera de la creación del dominio y de la degradación del titular los cambios
    «debe iniciarlos un administrador» y recomienda maestros en espera, pero no da cómo consultar ni
    transferir (ni la diferencia entre transferir y tomar el rol). Descarta d, no llega a a. **No**
    (laguna L2).

12. (Servicio de directorio, AP) Un equipo del dominio con el reloj adelantado diez minutos respecto al
    controlador falla al autenticar. Causa: a) la tolerancia de reloj de Kerberos (5 minutos por defecto);
    b) el puerto 445 cerrado; c) el nivel funcional; d) la caché de grupos universales.
    → El tema sólo da el puerto 123/UDP de W32Time; no relaciona hora y Kerberos. **No** (laguna L3).

13. (Gestión de usuarios) Se quiere dar permiso sobre una carpeta de un dominio a usuarios de varios
    dominios del bosque, y que el grupo sólo sirva en ese dominio: a) global; b) dominio local;
    c) distribución; d) Builtin Local. → **b**. § 4, «Grupos: tipos y ámbitos». **Entera.**

14. (Gestión de usuarios, AP) `New-ADUser -Name "Ana Ruiz" -SamAccountName aruiz` sin más parámetros:
    a) crea la cuenta habilitada sin contraseña; b) falla; c) crea la cuenta deshabilitada, en el
    contenedor predeterminado de usuarios; d) la crea en la UO Domain Controllers.
    → **c**. § 4, «La gestión desde PowerShell…». **Entera.**

15. (Gestión de usuarios, AP) Se pide que una cuenta del dominio se bloquee tras cinco intentos fallidos
    y se desbloquee sola a los 30 minutos. ¿Dónde y cómo? a) En una GPO vinculada al dominio
    (directiva de bloqueo de cuentas: umbral y duración); b) en la pestaña Cuenta del usuario;
    c) con `Unlock-ADAccount`; d) en el DHCP.
    → El tema dice que las directivas de contraseña son de nivel de dominio y que el bloqueo lo produce
    la directiva de contraseñas de la cuenta, pero declara no leídas las directivas de bloqueo con sus
    valores y no nombra umbral ni duración. Permite elegir a por descarte. **A medias** (laguna L4).

## Recuento

Enteras: 10 (1-7, 9, 13, 14). A medias: 2 (8, 15). No: 3 (10, 11, 12).
