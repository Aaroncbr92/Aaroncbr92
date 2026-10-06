# Puesto 29 · Tema 8 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en los volcados
`fuentes/canal-sur/informatico/web/ws-*.txt`, `w11-gpo.txt` y `w11-gpproc.txt`, todos con fecha de
lectura 05-10-2026 en cabecera (no se descargó nada nuevo).

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/08-administracion-de-sistemas-windows-server.md`.

## Lo copiado: sólo comprobación de literalidad

- «Copiado del común»: nada declarado.
- «Copiado de RTVE sin cambios»: los tres pasajes (tabla «Tarea / En Linux / En Windows Server» de
  RTVE `tecnica-informatica/14` § 5; «el directorio donde una organización guarda…» y «389 y 636 van
  juntos, como 80 y 443…» de RTVE `tecnica-informatica/03`) se compararon con grep: literales salvo
  la negrita quitada y las entradillas declaradas. No se re-verifican.

## Método

1. Literalidad de las negritas: script del redactor (normaliza espacios y comillas) sobre el tema
   corregido: 310 citas, 0 no halladas (una cita menos: se quitó la de los clústeres).
2. Cada afirmación en redonda (fechas de tabla, matriz de niveles, puertos, parámetros, listas,
   atribuciones de fuente, inferencias) se buscó en su volcado con `grep`/`sed`, y se releyó el
   contexto de las citas que sostienen una conclusión (para el error 6, salvedad omitida).
3. `indice.py`: 12.494 palabras, 43 epígrafes. `refutar_prosa.py`: los 4 hallazgos residuales de
   siempre (ADSI, KRBTGT, SYSVOL, RX), presentados en las siglas. Tema técnico sin norma: no proceden
   `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Confirmado sin cambios (muestra de lo comprobado)

Tabla de versiones y fechas ISO (ws-release); Server Core sin accesibilidad, OOBE ni audio; RSAT y
su lista de herramientas de AD DS; definiciones y modelo lógico; tres modelos de bosque; sitios y
SRV; Kerberos/TGT/NTLM; tabla de puertos (sección «Windows Server 2008 y versiones posteriores» de
KB 179442, con 88 y 445 incluidos); matriz de niveles funcionales celda a celda; DomainLevel 10;
FSMO (reparto 3+2, asignación automática, excepciones del maestro de infraestructura); RODC
(contraseñas, fases, DNS/GC en sucursal); asistente de AD DS; DCDiag (`/s:`, `/test:`, DNS, ICMP,
RPC); cuentas predeterminadas (SID -500, no mover del contenedor); pestañas de ADUC; papelera
(Admins. del dominio, panel Tareas, `Enable-ADOptionalFeature`); parámetros de los cmdlets
(`-Reset`, `-SearchBase`, `-LockedOut`, `-AccountDisabled`, `-PasswordExpired`, DN de Patti
Fuller); ámbitos de grupo y miembros; grupos predeterminados (nacen vacíos, no se renombran);
`Add-Computer` (ejemplos literales); SMB (tabla de dialectos), `New-SmbShare`, `icacls`; DFSN
(`\\Contoso\Public`); DHCP (agente de retransmisión); LAPS; GPO (90 + 30 min, 5 min en DC); fechas
de actualización 16-08-2025 y 12-05-2025; remisiones a los temas 3, 6, 7, 10, 13 y 14 (existen y
tratan lo remitido).

## Correcciones aplicadas

| # | Error | Pasaje | Qué había | Qué dice la fuente | Corrección |
|---|---|---|---|---|---|
| 1 | 9 / 6 | § 1, ediciones | Diferencia de ediciones «de funciones avanzadas (por ejemplo, la agrupación en clústeres)», con la nota «Si se requiere la agrupación en clústeres… Datacenter» | La tabla de ws-editions marca «Clústeres de conmutación por error» ✅ en Standard, Datacenter y Azure Edition; la nota es una llamada de pie cuyo rol no se identifica con seguridad | Quitada la cita; se dice que la página marca rol por rol y que los clústeres están en las tres. Trazabilidad ajustada |
| 2 | 3 | § 1, ediciones | «la tabla de versiones da para las LTSC las dos de siempre, Datacenter y Standard» | Windows Server 2016 (LTSB) trae también Essentials | «da para Windows Server 2025 Datacenter y Standard» |
| 3 | 6 | § 1, Hotpatch | Sin salvedad | «Hotpatch (versión preliminar)»; «está actualmente en versión preliminar» | Añadido que la página lo da como versión preliminar (y en Trazabilidad) |
| 4 | 9 | § 1, Windows Admin Center | «en el navegador» | ws-wac no habla de navegador ni explorador | Quitado |
| 5 | 9 | § 1, RSAT | «En el propio servidor no hace falta instalarlas aparte» | La cita manda instalarlas con el asistente de roles y características | «no se descargan, se añaden como característica» |
| 6 | 9 | § 2, tabla de contenedores | Bosque: «Límite de seguridad y de administración» | No figura en las fuentes leídas | «Reunir todos los dominios, unidos por confianzas automáticas» (lo que da la definición citada) |
| 7 | 9 | § 3, maestro RID | «y llegará un momento en que no pueda crear cuentas» | ws-fsmo sólo dice que no puede renovar los grupos de RID | Quitada la consecuencia |
| 8 | 6 | § 3, catálogo global | «En general, «se recomienda incluir el catálogo global…»» | «En la mayoría de los casos, se recomienda… Se aplican las excepciones siguientes» (ancho de banda limitado…) | Cita completada y salvedad dicha; «pide» pasa a «recomienda colocarlo» (la fuente da recomendación) |
| 9 | 6 | § 3, asistente, página 2 | En dominio existente: DNS, GC/RODC y sitio | «…elija el nombre del sitio y escriba la contraseña DSRM» | Añadida la contraseña DSRM |
| 10 | 3 | § 3, asistente, «Sus páginas» | Faltaba la página «Opciones de preparación» (credenciales para `adprep`) | Está en la secuencia del asistente | Añadida en el paso 5 |
| 11 | 4 | § 3, DSRM | «que no debe escribirse en claro en un script» | «No se recomienda proporcionar o almacenar una contraseña de texto no cifrado» | «que Microsoft no recomienda escribir en claro» |
| 12 | 9 | § 4, ADAC | «La consola más reciente… Hace lo mismo que la anterior y además gestiona la papelera» | ws-adac: papelera, directivas de contraseña detalladas, visor de historial; no dice que haga lo mismo | «La otra consola…»; «Además de administrar cuentas, gestiona la papelera… y las directivas de contraseña detalladas». ws-adac añadido a Trazabilidad |
| 13 | 9 | § 4, pestañas | «Algunas pestañas, como Editor de atributos u Objeto, sólo se ven si…» | La página dice que la lista incluye pestañas visibles sólo con Características avanzadas, sin decir cuáles | Quitados los ejemplos |
| 14 | 9 | § 5, SMB | «El dialecto vigente desde Windows 10 1607 y Windows Server 2016» | La tabla dice qué versiones lo admiten, no desde cuándo es vigente | «el dialecto más alto, SMB 3.1.1, lo admiten Windows 10 1607 y posteriores y Windows Server 2016 y posteriores» |
| 15 | 9 | § 5, GPO | «Es ahí donde se fija el número de intentos fallidos que bloquea una cuenta» | Ninguna fuente leída lo dice; «Lo que no da» declara no leídas las directivas de bloqueo | Quitado |
| 16 | 6 | § 5, LAPS | «…de Windows 10 y de Windows Server que recibieron la actualización del 11 de abril de 2023» | Lista Windows Server 2019 y 2022 (no 2016), «o posteriores», y que Windows 10 acabó soporte el 14-10-2025 y LAPS sólo sigue donde recibe actualizaciones | Precisado |
| 17 | 1 | Trazabilidad, catálogo global | «puerto 3268» atribuido a «Planear la ubicación del servidor de catálogo global» | El puerto sólo está en KB 179442 | Quitado de esa fila; añadido lo que sí sostiene (bosque de un solo dominio, más de 100 usuarios) |
| 18 | 9 | Trazabilidad | Faltaban fuentes u oficio: UO homogéneas (en «Introducción a la directiva de grupo»), RODC en sucursal, ADAC; opción DHCP de servidores DNS que apunte a los DC y reserva para impresoras (oficio no declarado) | — | Añadidos a sus filas y a la lista de oficio |

Antecedentes: se releyeron los pasajes cambiados («su lista de ediciones» remite a la página de
ciclo de vida; «la página de novedades» va en la lista que abre «Novedades de la versión 2025»; se
quitó «esa lista», que no tenía antecedente).

## No corregido, para la refutación

- La nota (**) de KB 179442 dice que el 445 sólo hace falta para crear confianzas, no para su
  funcionamiento; el tema da la tabla como «puertos del controlador de dominio» sin esa nota. No es
  falso (la tabla es la de la fuente), pero podría matizarse.
- `indice.py` imprime «sin portada: es un esquema» aunque el tema tiene `<!-- portada -->`; ya lo
  imprimía con la redacción. Es cosa de la herramienta, no del tema.
- La línea del Hotpatch quedó algo larga (102 caracteres); sin efecto en el render.

## Otros ficheros tocados

Ninguno, aparte del tema y de este informe. Copia del tema antes de verificar en el scratchpad de la
sesión (`t08-antes.md`), fuera del repositorio.
