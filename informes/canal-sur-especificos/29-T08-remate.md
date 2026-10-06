# Puesto 29 · Tema 8 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/08-administracion-de-sistemas-windows-server.md`.
Entrada: `29-T08-refutacion.md` (1 grave, 4 menores, 4 lagunas) y `29-T08-preguntas.md` (10 enteras,
2 a medias, 3 no). **Se amplió el tema** con contenido nuevo, así que hace falta la fase 5 bis sobre
los pasajes listados abajo. Extensión: 14.900 palabras según `indice.py` (antes 12.400 en la ficha).

## Fuentes nuevas, leídas el 06-10-2026

Guardadas en `fuentes/canal-sur/informatico/web/` (cabecera con la URL, la fecha de lectura y el `ms.date`):

| Fichero | Fuente | Para qué |
|---|---|---|
| `ws-shareperm.txt` | Learn archivado, «Share and NTFS Permissions on a File Server» (Windows Server 2008, ms.date 03-07-2012, servida en inglés) | L1 · se aplica el permiso más restrictivo; NTFS en local y en remoto; los permisos de recurso compartido sólo por red; Control total para Todos |
| `ws-fsmo-seize.txt` | Soporte, KB 255504 «Transferir o aprovechar los roles maestros de operaciones…» | L2 · cuándo transferir y cuándo tomar; permisos; secuencia de `ntdsutil`; RID quemados; antiguo titular |
| `ws-fsmo-view.txt` | Soporte, KB 324801 «Cómo ver y transferir roles FSMO» | L2 · consolas para cada rol, `regsvr32 schmmgmt.dll`, «Si ya no existe un equipo, se debe asumir el rol» |
| `ws-fsmo-find.txt` | Soporte, KB 234790 «Búsqueda de servidores que contienen roles…» | L2 · ver los titulares en las consolas; `dsa.msc` |
| `ws-netdom.txt` | «netdom query» (referencia de órdenes, actualizada el 16-08-2025) | L2 · `netdom query fsmo` |
| `ws-moverole.txt` | `Move-ADDirectoryServerOperationMasterRole` (servida en inglés) | L2 · transferir, `-Force` para tomar, nombres de roles, ejecución remota |
| `ws-clockskew.txt` | Learn archivado (Windows 10), «Maximum tolerance for computer clock synchronization» (en inglés) | L3 · tolerancia de reloj de Kerberos, 5 minutos en Default Domain Policy, ubicación |
| `ws-w32time.txt` | «Funcionamiento del servicio de hora de Windows» (ms.date 25-07-2025) | L3 · jerarquía, emulador de PDC de la raíz del bosque, origen externo, error de Kerberos |
| `ws-pol-*.txt` (10) | Learn archivado (Windows 10/11, en inglés): Password Policy, Account Lockout Policy y las páginas de cada opción (ms.date 2017-2023) | L4 · ubicación, valores posibles y predeterminados, ligadura entre las tres opciones de bloqueo, exclusión del Administrador, directivas detalladas |

Además, se reutilizó `ws-dcdiag.txt` (ya leído el 05-10-2026) para el umbral de 300 segundos.

Las 67 citas en negrita añadidas o cambiadas se comprobaron por script contra los `ws-*.txt`
(espacios normalizados): todas aparecen literalmente.

## Correcciones de la refutación (todas comprobadas en la fuente antes de aplicarlas)

| # | Comprobación | Qué se hizo |
|---|---|---|
| G1 | ws-aduc l. 18 y ws-groups l. 383-406: las dos citas son literales y se contradicen. ws-groups da además el inicio de sesión local en los DC y la lista de cuentas y grupos que no administran | § 4 ADUC: párrafo nuevo «Ojo: …» que declara la contradicción y dice que se sigue la página de grupos de seguridad. § 4 tabla, fila Operadores de cuentas: cita completada (inicio de sesión local), «no pueden modificar los derechos de usuario» en literal y lista de cuentas y grupos protegidos; remisión cruzada |
| M1 | ws-firewall, tabla de 2008 y posteriores: RPC para LSA, SAM, NetLogon, FRS RPC y DFSR RPC en 49152-65535/TCP como puerto de servidor; nota (**) del 445 | Fila nueva en la tabla de puertos; párrafo con el intervalo dinámico, la nota del 445 y «No todos los puertos… son necesarios». No apliqué la idea de que haya UDP en esas filas: la tabla sólo da TCP para ellas |
| M2 | ws-new2025 l. 197 | Cita completada hasta «enlace de capa de autenticación y seguridad simple (SASL)» |
| M3 | ws-new2025 l. 159 | Segunda frase añadida a la cita, con su consecuencia práctica (añadir un DC 2025 exige nivel 2016) |
| M4 | ws-rodc l. 169; ninguna fuente leída habla de la seguridad física | «sedes donde el servidor no está bien protegido» sustituido por la cita de sucursales con WAN no disponible |

## Lagunas cubiertas (se amplía el tema, ninguna pregunta se recorta)

| Pregunta | Laguna | Dónde se cubre ahora |
|---|---|---|
| 10 (No) | L1 · combinación de permisos | § 5 «Carpetas compartidas»: sustituido el párrafo que declaraba no dar la regla por la regla citada, local frente a red, ejemplo Lectura + Modificar y Control total para Todos |
| 11 (No) | L2 · consultar, transferir y tomar FSMO | § 3 «Los roles de maestro de operaciones»: tres bloques nuevos (Consultar quién los tiene; Transferir o tomar; PowerShell y `ntdsutil` con ejemplo; dos consecuencias) |
| 12 (No) | L3 · hora y Kerberos | § 2 «LDAP, Kerberos y los puertos»: dos párrafos nuevos (tolerancia de 5 minutos; jerarquía W32Time y emulador de PDC) |
| 15 (A medias) | L4 · directivas de contraseña y bloqueo | § 5 «Directivas de grupo»: bloque nuevo con ubicación, tabla de ocho opciones con su valor por defecto, ligadura de las tres de bloqueo, líneas base, exclusión del Administrador, ejemplo 5 intentos / 30 minutos y directivas detalladas |
| 8 (A medias) | G1 | Ahora la contradicción está declarada y el tema da qué respuesta seguir |

Con lo añadido, las 15 preguntas se contestan con el tema.

## Pasajes cambiados (para la fase 5 bis)

1. Portada: «Redacción que se estudia» (lectura del 06-10-2026) y «Extensión» (14.900 palabras).
2. Siglas: NTP y GPS.
3. «Qué se puede preguntar»: consulta, transferencia y toma de FSMO; directivas de contraseña y
   bloqueo; combinación de permisos; reloj y Kerberos.
4. § 1 «La versión vigente…», novedades: cita de la firma LDAP completada (M2).
5. § 2 «LDAP, Kerberos y los puertos»: dos párrafos nuevos sobre la hora (L3); fila nueva de la
   tabla de puertos y párrafo del intervalo dinámico y del 445 (M1).
6. § 2 «Niveles funcionales»: segunda frase de la nota y su consecuencia (M3).
7. § 3 «Los roles de maestro de operaciones (FSMO)»: bloques nuevos tras «maestros en espera» (L2).
8. § 3 «Controlador de dominio de solo lectura (RODC)»: primera frase (M4).
9. § 4 «Usuarios y equipos de Active Directory…»: párrafo «Ojo: …» (G1); `dsa.msc`, ahora con fuente
   (sustituye la frase que lo daba como uso común sin fuente).
10. § 4 «Los grupos predeterminados»: fila Operadores de cuentas (G1).
11. § 5 «Carpetas compartidas»: regla de combinación y ejemplo (L1).
12. § 5 «Directivas de grupo»: remisión «(detalle, más abajo)» en el primer punto y bloque nuevo de
    directivas de contraseña y bloqueo (L4).
13. «Lo que este tema no da»: reescritos los puntos de NTFS y de directivas; añadidos los nombres
    ingleses de las opciones y el máximo de longitud de contraseña (no afirmado).
14. «Trazabilidad»: frase de fechas; cinco filas nuevas; una entrada más en «Oficio sin fuente».

Releídas las remisiones de los pasajes nuevos: «epígrafe "Los grupos predeterminados"», «véase
"Usuarios y equipos…"» y «(detalle, más abajo)» tienen su destino; «la misma ventana Maestros de
operaciones» y «esa frase sobre los Operadores de cuentas» tienen el antecedente justo delante.

## Avisos para la fase 5 bis

- Las páginas de las directivas, de la tolerancia de reloj y de los permisos combinados son
  documentación archivada (Windows 10/11 o Windows Server 2008), servida en inglés; el tema lo declara.
  No encontré página vigente de Windows Server 2025 equivalente.
- La página de longitud mínima (2022) dice que más de 14 caracteres no se admite; no lo he afirmado,
  porque no pude confirmar si sigue vigente.
- La traducción automática de KB 255504 dice «aprovechar» por *seize*; el tema usa «tomar» y lo explica.

## Lentes

- `indice.py` sobre el tema: portada e índice regenerados; 43 epígrafes (no cambia el número de `###`).
- `refutar_prosa.py`: 4 avisos de siglas (ADSI, KRBTGT, RX, SYSVOL), que ya existían y la refutación
  dio por presentadas en el párrafo de siglas; sin relleno, frases repetidas ni negritas rotas.
- Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`; las
  negritas nuevas se comprobaron por script contra las fuentes (arriba).

## Otros ficheros tocados

Los 18 ficheros de fuente nuevos que se listan arriba y este informe. Nota: corrí una vez `indice.py` sin
argumentos por error; procesa los temas de `portadas.tsv` y es idempotente, y `git status` no muestra
cambios suyos fuera del tema 8 (los cambios en los temas 01, 05, 06 y 07 del puesto ya estaban o son
de otros remates en curso, no míos).
