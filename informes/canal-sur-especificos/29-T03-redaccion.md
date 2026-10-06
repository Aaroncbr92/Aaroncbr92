# Puesto 29 · Tema 3 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real del
sistema, como en la investigación). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/03-sistemas-de-almacenamiento-y-recuperacion-de-informacion.md`.
Material: `29-investigacion-A-hardware.md` (§ Tema 3); RTVE `temas/ing-sup-teleco/18-almacenamiento-de-datos-y-servidores.md`,
`temas/tecnica-informatica/15-politicas-y-procedimientos-para-la-conservacion-de-datos.md`,
`temas/tecnica-informatica/17-arquitectura-de-ordenadores-y-virtualizacion.md` (§ 4) y
`temas/gestion-administrativa/08-ofimatica.md` (§ 4) (fila 29/3 de `informes/canal-sur-reuso/informatica.tsv`:
45 %, «actualizar: no»).

## Fuentes releídas y fecha

Todas el 05-10-2026, en sus copias de `fuentes/canal-sur/informatico/web/`: `snia-dict-*.txt` (flash
memory, solid state storage, wear leveling, trim, write amplification, garbage collection, over
provisioning, storage area network), `snia-nas.txt`, `ms-fsutil-behavior.txt`, `nvme-about.txt`,
`nvme-specs.txt`, `sda-capacity.txt`, `sda-speed-class.txt`, `ms-wbadmin-start-backup.txt`,
`ms-robocopy.txt`, `ms-vssadmin.txt`, `rsync-man.txt`, `gnu-gzip.txt`, `gnu-tar-compress.txt`,
`7zip.txt`, `ms-tar-windows.txt`, `ms-compact.txt`, `clonezilla.txt`, `gnu-dd.txt`, `photorec.txt`,
`testdisk.txt`, `incibe-guia-ransomware.txt` (§ 3.2.1 y § 4 enteros), `nomoreransom-es.txt`,
`ms-controlled-folders.txt`.

Nuevas en esta fase (la investigación las tenía sólo por resumen de WebFetch, «cotejar»): se
descargaron con `curl` (support.microsoft.com respondió) y se guardaron como texto con cabecera de URL y
fecha:

| Fuente | Copia | Resultado del cotejo |
|---|---|---|
| Soporte de Microsoft, «Recuperación de archivos de Windows» (es-es, `.../backup-recovery/windows-file-recovery`) | `ms-winfr.txt` | Confirmado todo lo de la investigación; añadidos: cuándo usarla (tras copia y Papelera), no admite recursos compartidos ni nube, tabla de sistemas de archivos, «Si no está seguro, empiece con el modo Normal», ejemplos, carpeta `Recovery_<date and time>` |
| Soporte de Microsoft, «Realizar copias de seguridad y restaurar con Copias de seguridad de Windows» (es-es) | `ms-windows-backup.txt` | La KB5032038 en inglés da 404 a fecha de hoy; se usa esta página en castellano. La salvedad MSA / Entra ID / AD de la investigación se sustituye por la redacción actual: «Las cuentas profesionales o educativas de Microsoft no funcionarán». No se da la fecha del 22-8-2023 (no consta en la página leída) |
| Soporte de Microsoft, «Zip and unzip files» (en-us) | `ms-zip.txt` | Confirmados formatos de 24H2 y archivos cifrados; añadidos los pasos de comprimir y extraer |

Comprobación de literalidad por script (comillas tipográficas, guiones, barras invertidas y espacios
normalizados) contra toda la carpeta de fuentes: 144 negritas, 143 halladas tal cual. La restante,
INCIBE **«algunas familias de ransomware también cifran y bloquean las copias de seguridad en la nube,
por lo que es conveniente desactivar la sincronización persistente.»**, es literal pero en el PDF la
parte un salto de página (cabecera «16 / Ransomware: Una guía de aproximación al empresario / 3» entre
«ransomware» y «también»): el verificador debe leerla saltando esa cabecera.

## Qué se hizo

Ocho epígrafes en el orden del enunciado: (1) mapa: unidades, soportes, magnitudes y «almacenar no es
recuperar»; (2) discos duros; (3) discos de estado sólido y memorias flash; (4) sistemas SAN y NAS, con
RAID y jerarquía; (5) herramientas de copia; (6) compresión; (7) clonación; (8) recuperación por
borrado, avería y virus, con tres casos prácticos. 54 epígrafes; `indice.py`: 9.795 palabras (sin
portada generada: ficha escrita a mano, como en los demás temas del puesto). `refutar_prosa.py`: 0
hallazgos (5 siglas sin presentar en la primera pasada —MS, RAM, RAR, USB, WIM—, corregidas). Tema
técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

Negrita = literal de la fuente (inglés con glosa en redonda). Lo copiado de RTVE va en redonda (RTVE lo
tenía todo en negrita sin ser cita), como en los temas 1 y 5-10 del puesto.

Decisiones frente al material:

- Lo propio de RTVE fuera: preguntas 3, 14, 20 y 70 del cuadernillo, «la plantilla oficial», «regla de
  examen», marcas ✔, § 6 de TI 15 («Lo que el examen ha preguntado»), «Cero preguntas», remisiones a los
  temas 10, 19, 20, 22, 23 y 25 de RTVE, § 5 de TI 15 (LOPDGDD y ENS: ajeno al enunciado de Canal Sur) y
  § 7 de IST 18 (servidores de vídeo: no lo pide el enunciado). De IST 18 § 3 sólo las tres razones de
  la cinta, la biblioteca y LTFS; fuera la compatibilidad LTO (era la respuesta de la pregunta 14).
- Avisos de la investigación respetados: la SAN con la salvedad **«usually (but not necessarily)»**;
  SLC/MLC/TLC/QLC fuera; no se afirma que TRIM impida recuperar en SSD (dicho expresamente); el 017 y la
  notificación a la AEPD fuera; Historial de archivos y Papelera sin página propia (la Papelera sí sale,
  citada desde la página de `winfr`).
- Comprobado y añadido sobre la investigación: semántica de `disabledeletenotify` (**«Disables (1) or
  enables (0)»**); códigos de salida de `robocopy` (8 o más = fallo); `/purge`, `/r`, `/w`; `-allCritical`,
  `-vssCopy` por defecto y `-quiet` de `wbadmin`; opciones de `rsync` (`-a`, `-n`, `--delete`, barra
  final) y de `gzip` y `tar`; AES-256 de 7-Zip; ejemplos de `tar` en Windows; en INCIBE, «lo primero es
  apagar el equipo afectado» y la denuncia.
- La compresión sin/con pérdida: la investigación no la confirmó con fuente; se toma la idea de RTVE TI
  18 § 3 (tabla de audio), reescrita y declarada como oficio. No se incluye en «sin cambios».
- El ejemplo de `wbadmin` del tema es construido con la sintaxis (los dos ejemplos de la página tienen
  erratas: «cc566d14-4410» frente a «cc566d14-44a0», «g\folder1»), y así se dice.
- Aplicación práctica añadida: cálculo de KiB a bits; capacidad útil de RAID con cuatro discos; qué juegos
  restaurar con diferencial o incremental; caso de clonado a SSD menor; tres casos (borrado en NTFS,
  SD formateada, *ransomware*).

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata almacenamiento, copias ni
recuperación.

## Copiado de RTVE sin cambios

Pasajes copiados literal, palabra por palabra, de temas marcados sin actualizar. Único cambio: se quita
la negrita (RTVE no citaba fuente) y, en tablas, las marcas ✔. Comprobado ya por script en esta fase:
cada frase y cada fila aparece tal cual en su origen. El verificador sólo comprueba que son literales.

| Origen | Pasaje | Dónde va |
|---|---|---|
| RTVE IST 18 § 1 | Párrafo «Todo lo demás depende de tener clara la aritmética, y es donde más se falla, porque hay dos familias de múltiplos y se parecen.»; tabla «Familia / Base / Ejemplo» (dos filas); «Las tres igualdades que hay que saber de memoria:» y las tres igualdades | § 1 «Las unidades» |
| RTVE IST 18 § 2 | «Los cuatro soportes que conviven en una instalación de televisión, con lo que aporta cada uno:» y tabla «Soporte / Cómo guarda / Para qué sirve aquí» (cuatro filas) | § 1 «Los soportes» |
| RTVE GA 08 § 4 | Las tres viñetas «Local / En red / En la nube» | § 1 «Los soportes» (la frase «Y por la ubicación:» es nueva) |
| RTVE IST 18 § 2 | Párrafos «La diferencia que de verdad importa … mil peticiones pequeñas a la vez.», «Y de ahí salen las dos magnitudes …:», las dos viñetas (caudal, operaciones por segundo) y «Un sistema puede tener … el error clásico.» | § 1 «Las dos magnitudes con que se dimensiona» |
| RTVE IST 18 § 7 | Frases «No protege del borrado por error, ni del programa malicioso que cifra los ficheros, ni del incendio de la sala. Un conjunto redundante no es una copia de seguridad, y confundir las dos cosas es el error que más material ha destruido en esta industria.» | § 1 «Almacenar no es recuperar» |
| RTVE GA 08 § 4 | Frases «Barato por unidad de capacidad, más lento y con partes móviles.» y «Mucho más rápido, más caro y con un número finito de ciclos de escritura.» | § 2 «Cómo guardan» y § 3 «La memoria flash» |
| RTVE IST 18 § 6 | Tabla «Interfaz / Dónde vive / Qué la caracteriza» (tres filas) y párrafo «La idea que ordena la tabla: … una cabeza que mover.» | § 2 «Por dónde se conectan» |
| RTVE IST 18 § 5 | Párrafo «Consolidar es sacar … lo que se usa una.», «Las tres arquitecturas, que es la pregunta clásica:» y tabla «Arquitectura / Qué ve el equipo / Por dónde va» (tres filas) | § 4 «Por qué se saca el disco del equipo» |
| RTVE IST 18 § 6 | «Los protocolos de ficheros, que sirven carpetas:» y viñetas NFS y SMB | § 4 «NAS» |
| RTVE IST 18 § 6 | «Los protocolos de red de almacenamiento, que sirven bloques:» y viñetas FC e iSCSI | § 4 «SAN» |
| RTVE IST 18 § 5 | Párrafo «La frontera que hay que saber explicar … De ahí se derivan las dos consecuencias prácticas:» y las dos viñetas | § 4 «Ficheros frente a bloques» |
| RTVE IST 18 § 6 | Párrafo «La regla para no equivocarse en un examen: … con los segundos.» | ídem |
| RTVE IST 18 § 4 | «El principio: … no sea la pérdida de los datos.»; cabecera de la tabla de niveles; «Con dos discos, la paridad de un solo dato es una copia del dato, y eso ya tiene nombre y es el espejo.»; las dos viñetas de advertencia sobre la paridad; «Sirve para capacidad bruta y no protege nada.» | § 4 «La redundancia dentro de la cabina: RAID» |
| RTVE IST 18 § 5 | Lista numerada «En línea / Casi en línea / Fuera de línea» | § 4 «En línea, casi en línea, fuera de línea» |
| RTVE GA 08 § 4 | Párrafo «La copia de seguridad es un concepto distinto … no se sabe si sirve.» | § 5 «Qué es una copia de seguridad» |
| RTVE TI 15 § 2 | Tabla «Redundancia / Copia de seguridad / Archivo» (tres filas) y párrafo «Y la frase que lo resume: … que cifra los ficheros.» | ídem |
| RTVE TI 15 § 1 | Tabla «Objetivo / Qué pregunta / Qué determina» (dos filas) y párrafos «El ejemplo que lo hace concreto: …» y «El error de método más frecuente: …» | § 5 «Las dos cifras …» |
| RTVE TI 15 § 3 | Tabla «Tipo / Qué copia / Restaurar exige» (tres filas) y párrafo «La regla de elección: …» | § 5 «Los tipos de copia» |
| RTVE TI 15 § 3 | Tabla «Cifra / Qué exige» (3-2-1) y párrafo «Y lo que la extorsión por cifrado ha obligado a añadir: … la misma copia.» | § 5 «La regla 3-2-1 …» |
| RTVE TI 15 § 4 | Párrafo «Una política de conservación tiene cinco piezas …», lista de cinco y párrafo «El aviso, dicho sin adornos: … el resto funciona.» | § 5 «La política y la prueba de restauración» |
| RTVE IST 18 § 3 | «Una biblioteca de cintas tiene tres piezas: … el número de lectores.» | § 5 «La cinta» |

Adaptado de RTVE (no literal; sí se verifica):

- IST 18 § 7: «La redundancia interna de un conjunto de discos protege del fallo de un disco y de nada
  más.» (mayúscula inicial; quitado «El aviso de oficio con el que se cierra el tema:»).
- GA 08 § 4: «El disco duro clásico guarda los datos en platos giratorios que lee y escribe un cabezal.»
  y «Frente al disco magnético: memoria flash sin partes móviles.» (reescritos a partir de las viñetas).
- IST 18 § 4: tabla de niveles con «RAID 0 / 1 / 5 / 6 / 10» añadido a cada nombre; «Por qué la paridad
  simple pide tres discos: hacen falta …» (era la razón de la pregunta 20); «Y el conjunto que no es un
  conjunto: … (JBOD).»; la cuenta con cuatro discos de 4 TB es nueva.
- TI 17 § 4: «Por eso una base de datos exigente se pone sobre la SAN: necesita un disco, no una carpeta.»
  («sobre la segunda» → «sobre la SAN»).
- IST 18 § 5: «La tercera forma, más reciente: el almacenamiento por objetos …» (quitado «y ya presente en
  las casas de televisión»); «Quien gobierna ese ciclo en una casa de televisión es la gestión de activos
  de medios (MAM): …» (quitada la frase final «Sin catálogo, …»).
- IST 18 § 3: «La cinta no ha desaparecido, por tres razones que hay que saber decir: …» (quitado «y no
  va a desaparecer»); frase de LTFS recortada.
- RTVE TI 18 § 3 (audio): base de la distinción con/sin pérdida del § 6, reescrita.

## Ficheros tocados

- Creados: el tema y este informe.
- Añadidas tres copias de fuente en `fuentes/canal-sur/informatico/web/`: `ms-winfr.txt`,
  `ms-windows-backup.txt`, `ms-zip.txt` (con cabecera URL y fecha). HTML de trabajo y scripts de
  comprobación en el directorio temporal de la sesión, fuera del repositorio.
- Ningún otro fichero modificado.

## Preguntas de control (10, tipo test)

Repartidas por las rúbricas del enunciado; teoría y aplicación práctica. Se contestan con el tema.

1. **Discos duros.** La diferencia decisiva entre un disco magnético y uno de estado sólido es: a) la
   velocidad de transferencia secuencial; b) el tiempo de acceso; c) la interfaz SATA; d) la capacidad.
   → b. § 1 «Las dos magnitudes» (y § 2 «Cómo guardan»). **Entera.**
2. **Discos de estado sólido.** El mecanismo por el que el sistema operativo avisa a la unidad de los
   bloques que ya no usa es: a) la nivelación de desgaste; b) el sobreaprovisionamiento; c) TRIM; d) la
   amplificación de escritura. Y en Windows, `DisableDeleteNotify = 0` significa… → c; TRIM activo. § 3
   «Lo que hace el controlador». **Entera.**
3. **Memorias flash.** Una tarjeta SDXC tiene: a) hasta 2 GB y FAT16; b) de 2 a 32 GB y FAT32; c) de más
   de 32 GB a 2 TB y exFAT; d) de más de 2 TB a 128 TB y exFAT. → c. § 3 «Tarjetas de memoria SD».
   **Entera.**
4. **SAN y NAS.** Señale la correcta: a) un NAS sirve bloques por canal de fibra; b) un NAS sirve
   ficheros con protocolos como NFS o CIFS, y una SAN se identifica normalmente, no necesariamente, con
   servicios de bloques; c) iSCSI es un protocolo de ficheros; d) montar el mismo volumen de bloques
   corriente en dos equipos es seguro. → b. § 4 «NAS», «SAN», «Ficheros frente a bloques». **Entera.**
5. **SAN y NAS · práctica (RAID).** Una cabina con cuatro discos de 4 TB en RAID 6 ofrece: a) 12 TB y
   aguanta un fallo; b) 8 TB y aguanta dos fallos; c) 16 TB sin protección; d) 8 TB y aguanta un disco
   de cada pareja. → b. § 4 «La redundancia dentro de la cabina», aplicación práctica. **Entera.**
6. **Copia de seguridad · práctica.** Completa el domingo e incrementales cada noche; el disco falla el
   jueves por la mañana. Para restaurar hace falta: a) sólo la completa; b) la completa y la incremental
   del miércoles; c) la completa y las incrementales de lunes, martes y miércoles; d) sólo las
   incrementales. → c. § 5 «Los tipos de copia». **Entera.**
7. **Copia de seguridad · herramientas.** En `robocopy`, la opción que replica un árbol de carpetas y
   equivale a `/e` más `/purge` es: a) `/z`; b) `/b`; c) `/mir`; d) `/s`. ¿Y qué indica un código de
   salida de 8? → c; al menos un fallo en la copia. § 5 «Windows: robocopy». **Entera.**
8. **Compresión de datos.** `gzip` comprime con: a) LZW; b) codificación de Lempel-Ziv (LZ77); c)
   Huffman adaptativo; d) LZMA2. ¿Y qué no admite el Explorador de Windows 11 24H2? → b; operar con
   archivos comprimidos cifrados. § 6 «gzip y tar» y «Lo que trae Windows 11». **Entera.**
9. **Clonación y avería.** a) En Clonezilla, la partición de destino debe ser… ; b) en `dd`, `conv=noerror,sync`
   sirve para… → a) igual o mayor que la de origen; b) seguir tras los errores de lectura rellenando con
   ceros lo no leído, para sacar imagen de un disco que falla (sin montar). § 7 «Clonezilla» y «Rescatar
   un disco que falla»; § 8 «Avería». **Entera.**
10. **Recuperación por borrado y por virus.** a) Para recuperar ficheros borrados de una tarjeta SD con
    exFAT, `winfr` se usa en modo: normal / extenso / cualquiera / no se admite. b) Según INCIBE, ante un
    *ransomware*, tras aislar el equipo, el paso siguiente es: pagar / clonar el disco / formatear /
    restaurar la copia. → a) extenso; b) clonar el disco. § 8 «Recuperación de archivos de Windows» y
    «Ataque de virus: el ransomware». **Entera.**

Resultado: las 10 se contestan enteras con el tema; no hizo falta ampliarlo tras la prueba.
