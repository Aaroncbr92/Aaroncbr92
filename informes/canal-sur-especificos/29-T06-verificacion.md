# Puesto 29 · Tema 6 · Verificación (fase 3)

Fecha: 05-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/06-windows-11.md`. Copia previa en el
directorio temporal de la sesión (`29t06-antes-verif.md`); diff en `29t06-verif.diff`.

## Fuentes y fecha de lectura

Todas releídas el 05-10-2026 sobre los volcados de la redacción, que se descargaron ese mismo día:
`fuentes/canal-sur/informatico/web/w11-*.txt` (69 páginas de Microsoft Learn y del soporte de Microsoft) y
`snia-dict-trim.txt`. Además, la página de atajos de teclado `fuentes/ofimatica/MS_windows-atajos.txt`,
descargada el 02-09-2026 para otro tema. Para la fecha de «Requisitos de Windows 11» se ha usado
`ms-win11-requirements.txt` (en-us). No se ha descargado ninguna fuente nueva.

## Método

1. Literalidad: un script normaliza las comillas y los espacios y busca cada negrita (troceada por
   […]) en las fuentes. Resultado: **586 negritas, 0 sin encontrar**. Las 20 que fallaban en la primera
   pasada eran atajos de teclado y la definición de TRIM, y estaban en las dos fuentes que van fuera de
   `w11-*`.
2. Prosa en redonda, tablas y rutas de menú: cada dato se ha releído en su pasaje con los nueve
   errores delante. También se ha comprobado que cada negrita cuadra con el contexto de su fuente
   (salvedades, ámbito y versión).
3. Lentes (tema técnico sin norma): `refutar_prosa.py` da 0 hallazgos. `indice.py` da 17.155
   palabras y 62 epígrafes, y se ha actualizado la Extensión de la ficha a 17.200. `negritas.py`,
   `refutar_exactitud.py` y `refutar_modo.py` no se aplican porque el tema no cita normas.

## Copiado del común / de RTVE sin cambios

- Del común no se ha copiado nada.
- La redacción no declara pasajes de RTVE «sin cambios», porque los dos temas fuente están en
  «actualizar: sí», así que todo se ha verificado.
- Literalidad de los pasajes que la redacción lista como copiados de RTVE: un script compara el texto
  normalizado y sin negrita con RTVE 16 y RTVE 09. Los 13 pasajes literales están tal cual en RTVE y
  en el tema. Los 2 adaptados («El chip no cifra el disco…» y «…no pasa por la papelera») no son
  literales, como ya declaraba la redacción, y se han verificado:
  - «guarda la llave» no tenía fuente. Se ha reescrito con «se crea el protector de TPM», de la
    página de BitLocker.
  - Lo demás de RTVE sigue declarado como oficio en la Trazabilidad.

## Hallazgos y correcciones (19)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 9 | § 1, tabla de métodos: Windows Update «conserva archivos, aplicaciones y configuración» | La página «Formas de instalar» no lo dice. Se cambia por «La página no lo detalla» |
| 2 | 6+9 | § 1, Asistente: «Se puede usar antes…» y «Igual que la anterior» | Se añade que Microsoft recomienda esperar a Windows Update. «Qué conserva» pasa a «La página no lo detalla» |
| 3 | 6 | Tabla de versiones: «Home y Pro» / «Enterprise y Education» | La fuente enumera más ediciones. Se ponen las columnas completas |
| 4 | 9 | § 2, Explorador: «barra de comandos» | La página dice «cinta de opciones». Corregido |
| 5 | 9 | § 3, discos dinámicos: «definiciones, que siguen siendo las de la consola» | No hay fuente. Se quita |
| 6 | 9 | § 3: «La conversión… conserva los datos» | La fuente dice que las particiones pasan a volúmenes simples. Se reescribe en esos términos |
| 7 | 9+6 | § 3, `defrag` en SSD: «hace análisis y recorte, y la desfragmentación tradicional una vez al mes» | Según `defrag`, la optimización tradicional (desfragmentación **y recorte**) se hace una vez al mes desde la tarea programada. Se añade la salvedad literal: cambiar la frecuencia no afecta a esa cadencia |
| 8 | 9 | § 3, revertir el controlador: «Útil cuando el fallo empezó tras una actualización» | No hay fuente. Queda como oficio y se declara |
| 9 | 9 | § 4, Wi-Fi: la contraseña se ve en «Administrar redes conocidas» | La fuente la sitúa en las propiedades de la red, con **Mostrar**. Corregido |
| 10 | 6 | § 5, tabla de pérdidas: medios de instalación «A elegir» | La misma página dice también «Esto quita todo del dispositivo». Se señala la discrepancia y se remite a `setup.exe` (§ 1) |
| 11 | 6 | § 6, BitLocker sin TPM con contraseña | Se añade que Microsoft la desaconseja y que **«se deshabilita de forma predeterminada»** |
| 12 | 9 | § 6, adaptado de RTVE: «guarda la llave y comprueba que el arranque no se ha tocado» | Reescrito con «protector de TPM» y con la comprobación de manipulación, ambas con fuente |
| 13 | 9 | § 6, UAC: consentimiento, «basta con pulsar Sí» | La fuente dice que el usuario aprueba el cambio. Corregido |
| 14 | 9 | § 7: desde el calendario «se puede iniciar una sesión de concentración (Foco)» | No hay fuente. Se sustituye por el atajo Win + N, que abre centro y calendario |
| 15 | 9 | § 7: «Centro de actividades/acciones» como nombres de lo que Windows 11 «reparte» | Se reformula con lo que consta: la página de Windows 10 llama así al centro, y en Windows 11 Win + A abre Configuración rápida y Win + N el centro de notificaciones |
| 16 | 9 | § 9, servicios: `services.msc` y «pestaña en Propiedades (botón secundario)» | Ninguna fuente lo dice. Se marcan como oficio, y Administración de equipos queda con su fuente. Actualizados «Lo que este tema no da» y la lista de oficio |
| 17 | 9 | § 12: «La carga lateral es instalar aplicaciones que no vienen de la tienda» | La página no la define. Queda marcada como oficio |
| 18 | 9 | § 13: «la GPMC para crear, vincular y filtrar» | Sin fuente. Se sustituye por lo que la documentación sí atribuye a la GPMC: bloquear la herencia, configurar el bucle invertido y actualizar una UO |
| 19 | 6 | § 14, restauración puntual: «Y sólo si el volumen… 200 GB» | El requisito vale sólo para que venga activada de forma predeterminada. Se añade que con volúmenes menores se puede activar a mano |

Ajustes menores, también en el diff:
- § 10: en la actualización de WinRE con la partición fuera de su sitio, la antigua «queda huérfana».
- § 15: se completa la salvedad de KB5121772, que dice que Windows termina instalando la actualización
  retenida.
- Trazabilidad: la fecha 14-07-2026 de «Requisitos» sale de la versión en inglés, y ahora se dice.
- Ficha: Extensión 17.200.

## Comprobado sin cambios (muestra de lo releído)

- Requisitos de hardware, de máquina virtual y de la actualización desde Windows 10.
- La tabla de versiones y las fechas de 26H2, 26H1, 25H2, 24H2, 23H2 y LTSC.
- Herramientas del ADK, WDS, WSUS, Autopilot e Intune.
- Barra de tareas: los seis componentes y sus atajos. Menú Inicio: anuncia «seis áreas» y enumera siete.
- Atajos (contra la copia del 02-09-2026).
- Administración de discos: vías de apertura y operaciones. GPT y MBR, 2,2 TB y 128 particiones.
- `diskpart` y sus órdenes; códigos del Administrador de dispositivos.
- Red: perfiles, TCP/IP, DoH, `ipconfig`, `ping`, `tracert`, `netstat` y UNC.
- WinRE: herramientas, entradas, los cinco disparadores automáticos y la contradicción sobre las credenciales.
- Opciones de recuperación y su orden; recuperación rápida de equipo.
- Seguridad de Windows; cifrado de dispositivo (24H2, XTS-AES 128, cuentas locales); colores del UAC y sus cuatro niveles.
- Notificaciones y No molestar; temas y colores; categorías de Configuración; herramientas avanzadas.
- Diseño UEFI/GPT: ESP de 200/300 MB, MSR de 16 MB, Windows de 20 GB, recuperación (250 MB, 990 MB, tipo, ubicación) y letras S/W/R/X.
- Modo desarrollador en 25H2.
- GPO: componentes, orden LSDOU, herencia, filtros, bucle invertido, 60/90+30/5 min, `gpupdate`/`gpresult`, `Invoke-GPUpdate`.
- Protección del sistema y Restaurar sistema.
- Restauración puntual: 24 h, 72 h, 2 %, Enterprise, sólo desde WinRE.
- KB5121772: fechas, versiones y listas.
- Horas activas (8–17, 12/18 h), siete días, 2–14 días, valores 0/1/2.

## Pasajes cambiados: relectura de antecedentes

Se han releído los 19 pasajes cambiados:
- «la misma página» (§ 5, tabla) remite a «Opciones de recuperación», nombrada justo antes («según
  la misma página»).
- «Esa pestaña» (§ 9) tiene delante «su pestaña de dependencias».
- «epígrafe 1» y «epígrafe 2» existen y tratan lo que se cita.

## Otros ficheros tocados

Ninguno, fuera del tema y de este informe.
