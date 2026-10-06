# Puesto 29 · Tema 8 · Fase 5 bis (revisión de los pasajes del remate)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/08-administracion-de-sistemas-windows-server.md`.
Alcance: sólo los 14 pasajes que lista `29-T08-remate.md` (comparados con `git diff` contra HEAD).
Fuentes releídas el 06-10-2026: los `ws-*.txt` de `fuentes/canal-sur/informatico/web/` que cita el
remate (clockskew, w32time, dcdiag, firewall, new2025, rodc, aduc, groups, fsmo-seize, fsmo-view,
fsmo-find, netdom, moverole, shareperm, adac y los diez `ws-pol-*`).

## Comprobación literal

Las 375 negritas del tema, normalizando espacios, se buscaron por script en los `.txt` de fuente:
todas aparecen literalmente, salvo tres que no eran cita (ver C1). Además se comprobó a mano que cada
cita nueva está en la fuente que la tabla de Trazabilidad le asigna y que su contexto no la desvía.

## Correcciones aplicadas (cada una comprobada en la fuente)

| # | Pasaje | Error | Fuente | Qué se hizo |
|---|---|---|---|---|
| C1 | § 3 FSMO y § 5 Directivas | Tres rótulos en negrita («Consultar quién los tiene.», «Transferir o tomar.», «Las directivas de contraseña y de bloqueo de cuentas.») que no son literales: rompían la regla negrita = literal | — | Pasados a cursiva, como los rótulos ya existentes del tema (*Bosque.*, *Con PowerShell.*) |
| C2 | § 2 hora y Kerberos | «DCDiag, al comprobar la replicación» (error 9/8): el umbral de 300 s lo mira la prueba CheckSecurityError, que no se ejecuta por defecto, y sólo con `/ReplSource`; la página añade que no consulta la directiva de Kerberos | ws-dcdiag l. 133-150 | Reescrito con la prueba, el parámetro y la salvedad (error 6) |
| C3 | § 3 FSMO, PowerShell | La página del cmdlet se contradice: el parámetro `-Identity` **«specifies the directory server that receives the roles»** (l. 66, y así los ejemplos), pero la introducción dice «the current role holder» (l. 93). El tema no lo declaraba | ws-moverole | Añadida la cita del parámetro y la nota de la contradicción |
| C4 | § 3 FSMO, antiguo titular | «se reinstala desde cero y se limpian sus metadatos» simplificaba: la fuente da dos vías (formatear y reinstalar, o degradar por la fuerza a servidor miembro), limpieza en otro DC y después nueva promoción | ws-fsmo-seize l. 279-291 | Reescrito con las dos vías y el orden |
| C5 | § 5 Carpetas compartidas | «Por eso muchos administradores simplifican»: la fuente dice **«some experienced administrators»** y no lo presenta como consecuencia | ws-shareperm l. 44 | «La misma página recoge una forma de simplificar:»; segundo «La misma página» cambiado a «Y avisa» |
| C6 | § 4 ADUC, párrafo «Ojo» | Cierre ambiguo («los grupos de este grupo») | ws-groups l. 385 | Reformulado: si un test pregunta si los Operadores de cuentas pueden crear grupos globales o locales |
| C7 | Portada | Extensión: `indice.py` da 14.974 palabras tras los cambios | — | 15.000 palabras aproximadamente |

## Comprobado sin cambios

- Siglas NTP y GPS; «Qué se puede preguntar».
- M2 y M3 (ws-new2025), M4 (ws-rodc l. 169): literales y consecuencia de M3 bien deducida.
- Tolerancia de reloj: ubicación, 5 minutos en *Default Domain Policy*, recomendación (ws-clockskew
  l. 48, 59, 63, 72-73). W32Time: las cuatro citas y su orden lógico (ws-w32time l. 140, 178, 200, 280).
- Puertos: la fila RPC para LSA/SAM/NetLogon, FRS y DFSR es 49152-65535/TCP como puerto de servidor
  (la columna TCP/UDP es la de cliente de la fila siguiente); nota (**) del 445 y «No todos los
  puertos…» literales (ws-firewall l. 24, 109, 147-203, 218). El remate acertó al no añadir UDP.
- FSMO: netdom con privilegios elevados (ws-netdom l. 42); consolas, pestañas PDC/Infraestructura/
  Grupo de RID y `dsa.msc` (ws-fsmo-find l. 62-80, 123); botón Cambiar y «para asumir un rol, emplee
  Ntdsutil» (ws-fsmo-view l. 80, 171); escenarios de transferir y tomar, permisos, secuencia de
  `ntdsutil`, RID +30 000 / +10 000 y «solo cuando esté seguro…» (ws-fsmo-seize l. 104-125, 199-267).
- Operadores de cuentas: cita, derechos y lista de cuentas y grupos protegidos (ws-groups l. 383-406);
  contradicción con ws-aduc l. 18, real.
- Permisos combinados: tres citas y ejemplo coherente con la regla (ws-shareperm l. 44, 95).
- Directivas: rutas (la de bloqueo con `\Policies\` es la de la página general, ws-pol-account-lockout-
  policy l. 46), rangos 0-24, 0-999 (días), 1-999 (intentos), los ocho valores de *Default Domain
  Policy*, ligadura duración ≥ contador, líneas base 10 y 15, exclusión del Administrador (de la
  directiva de umbral), recomendación de 8 caracteres, tres de cinco categorías, directivas detalladas
  (ws-pol-* y ws-adac l. 219-223). Ejemplo 5 / 30 / ≤ 30 cumple la ligadura.
- «Lo que este tema no da» y Trazabilidad: fechas (ms.date 2022-03-30 de la longitud mínima) y filas.
- Antecedentes: «esa frase sobre los Operadores de cuentas» (sigue a la cita de ADUC), «la misma
  ventana Maestros de operaciones», «(detalle, más abajo)», «véase "Usuarios y equipos…"»: todos tienen
  destino o antecedente.

## Lentes

`indice.py` (14.974 palabras, 43 epígrafes) y `refutar_prosa.py`: sólo los 4 avisos de siglas ya
conocidos (ADSI, KRBTGT, RX, SYSVOL); sin negritas rotas.

## Ficheros tocados

El tema 8 y este informe. Ninguno más.
