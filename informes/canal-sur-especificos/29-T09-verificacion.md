# Puesto 29 · Tema 9 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en las descargas del
redactor (directorio temporal de la sesión, `man/`: páginas de man7.org, `apt(8)` de
manpages.ubuntu.com, páginas de Ubuntu y Debian, FHS 3.0, manuales GNU de coreutils 9.12, grep, sed,
tar 1.35.90 y gawk), todas leídas por el redactor el 05-10-2026. No se descargó nada nuevo.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/09-administracion-del-sistema-operativo-linux.md`.

## Lo copiado: sólo comprobación de literalidad

- «Copiado del común»: nada declarado.
- «Copiado de RTVE sin cambios» (seis pasajes de RTVE `tecnica-informatica/14` y `/16`: tabla de
  familias de órdenes, frase de `pwd`, frases de `getfacl`/`setfacl`, tabla básicos/extendidos, tabla
  «Tarea / En Linux / En Windows Server», entradilla «Lo mínimo que conviene…»): comparados con grep;
  literales salvo la negrita y la ✔ quitadas, como se declaró. No se re-verifican.
- «Adaptado de RTVE» (tabla de equivalencias Windows/Ubuntu): verificado. Columna de Ubuntu sostenida
  en el propio tema (`sudo`, `ss`, `systemctl`, APT, LUKS); la de Windows (`.msi`, control de cuentas de
  usuario, `netstat`, BitLocker) está desarrollada en el tema 6 (comprobado con grep).

## Método

1. Las negritas: script del redactor más una anotación por cita de los ficheros de fuente que la
   contienen, para comprobar la **atribución** (el script sólo miraba que la cita existiera en el
   conjunto). Tema corregido: 555 citas, 0 no halladas; cada cita atribuida en el texto a una página
   aparece en esa página (las de una sola palabra u opción, como «-g» o «ro», están en su página).
2. Cada dato en redonda (versiones, rangos de UID, campos, valores por defecto, ejemplos de manual,
   opciones, paráfrasis entre paréntesis) se buscó con grep/sed en su fuente, releyendo el contexto
   para la salvedad omitida (error 6).
3. Lentes: tema técnico sin norma; sólo `indice.py` (18.505 palabras, 84 epígrafes; imprime «sin
   portada: es un esquema», cosa de la herramienta, ya pasaba en el tema 8) y `refutar_prosa.py`.

## Confirmado sin cambios (muestra)

Ciclo de Ubuntu (seis meses, LTS cada dos años con 5 de mantenimiento, intermedias de 9 meses, 26.04
y 24.04 LTS en la tabla, público de cada clase); Debian 13 *trixie*, 13.7 del 12-09-2026, *bookworm*
*oldstable*; arquitecturas, requisitos 2 GB/5 GB, copia previa, `releases.ubuntu.com`, teclas Escape,
F2, F10, F12 y pasos del instalador; rótulos de la FHS 3.0 (2015; `/proc` y `/sys` en el anexo de
Linux) y descripciones de `hier(7)`; letras de tipo y `s`/`S`/`t`/`T` de coreutils; ejemplo `ls -l`;
`chmod` simbólico y octal; *setuid*/*setgid*/*sticky*; `umask` 022 y 0644; ACL; campos de `passwd`,
`shadow` (nueve, `!`, días desde 1970, 0) y `group`; NSS; UID 0-99, 100-999, 1000-59999 y 65534
(16 bits); root sin contraseña, `sudo`, `sudo-rs` desde 25.10 y `sudo.ws`; tabla de órdenes de
cuentas y cada opción (`useradd -s` con campo vacío, `usermod -l` «Nothing else is changed», `-e`,
`passwd -u/-e/-S`); 0750 desde 21.10, `DIR_MODE`, `minlen=8`; Bash (Korn y C shell, POSIX), comodines
(negación con `!` o `^`), comillas, continuación de línea, parámetros especiales, redirecciones
(descriptores 0, 1, 2), listas, `alias`; `bootup(7)` e *initrd*; tipos de unidad; tabla de
`runlevel(8)` y su motivo; `systemctl` (`restart` arranca si no estaba, `reload` no recarga el fichero
de unidad, `enable` crea enlaces, `is-active`/`is-enabled` con código 0, `daemon-reload` tras `fstab`);
`journalctl` (`-b` vacío y `-1`, `--disk-usage`, `--vacuum-size`); `ps -e/-ef`, `ps ax/axu`; teclas
`k`, `r`, `q`, `M`, `P` de `top`; señales en x86/ARM; `nice` suma 10; `crontab -e` instala al salir;
campos y ejemplos de `crontab(5)`; errata «12:00 pm» de Ubuntu; `mount` (tipo detectado sin `-t`),
opciones, `fstab` (campos, `passno` por defecto 0, UUID), `fsck` (dispositivo, punto, etiqueta, UUID),
`mkswap` (tipo 82), `swapon --show`/`swapoff`; ejemplos `/dev/hda1`, `/dev/hdc1`, `/dev/sdb2`;
`blkid` recomienda `lsblk`; `fdisk` y alineación; ejemplos de LVM (500 MiB en raid1, +54 MiB);
`vgcreate` inicializa PV; `mdadm` y `/proc/mdstat`; `cryptsetup` (dm-crypt, *plain*, LUKS1/2); APT,
*deb822* desde 24.04, Universe/Multiverse, `dpkg` (ejemplos `apache2`, `ufw`, `base-files`, `zip`);
`rpm -i` «special usage»; `dnf search/info/list --installed/makecache`; plan de copias, Bacula y
rsnapshot con su público; script de Ubuntu (NFS, siete días, rotación domingo-viernes, sábado, día 1,
par/impar); `tar` (`-z/-j/-J`, `-g`, nivel 0 si no existe el fichero); `rsync -a` sin `-A/-X/-H`,
`-avz` con compresión, barra final; `dd` (`bs` 512, `status`); ejemplos de grep (*Othello*, `main`,
`/home/gigi`, `-q` junto al estado de salida); `sed` (`&`, `\1`-`\9`, direcciones 144, 4,17, `!`,
`seq 3 | sed 2d`, `45p`, `myscript.sed`, `-i[SUFFIX]`); gawk (ejemplos `/li/`, `$1 ~ /J/`, `Jan 13`,
`printf`, números de sección de la Trazabilidad); páginas de remisión (temas 5, 6, 7, 8, 10, 13, 14).

## Correcciones aplicadas

| # | Error | Pasaje | Qué había | Qué dice la fuente | Corrección |
|---|---|---|---|---|---|
| 1 | 6 | § 1, paso 4 del instalador | «La red: «the installer attempts…»» | «Do not configure networking (the installer attempts…)» | Añadido «Do not configure networking» |
| 2 | 6 | § 4, `find … \| xargs rm` | Falla con saltos de línea o comillas | «newlines, single or double quotes, or spaces» | Añadido «o espacios» |
| 3 | 9 | § 5, `shutdown -h now` | «con las opciones citadas»; `-h` no estaba citada | `shutdown(8)`: `-h` «The same as --poweroff» | Citado `-h` |
| 4 | 9 | § 6, `systemctl` | «si no se pone extensión, se entiende `.service`; esto último es oficio» | `systemctl(1)` lo dice: añade el sufijo, «".service" by default» | Pasa de oficio a cita |
| 5 | 9 | § 6, SIGINT | «el Ctrl+C» sin fuente | `bash(1)`: «SIGINT (usually generated by ^C)» | Citado; Trazabilidad de `bash(1)` ampliada |
| 6 | 9 | § 7, `e2fsck` | «o se trabaja desde el modo de rescate», sin fuente | No está en `e2fsck(8)` | Declarado oficio (y en la lista de oficio) |
| 7 | 9 | § 8, tablas | «MBR (la que `parted` llama *MS-DOS*)» | `parted(8)` dice «MS-DOS and GPT» sin equipararlo a MBR | Declarado oficio |
| 8 | 6 | § 2, `/var/spool` | `hier(7)` lista dentro `mail` | `/var/spool/mail` «Replaced by /var/mail» | Añadida la salvedad |
| 9 | 9 | § 10, `tar -f` | «va la última del grupo, porque lleva argumento» | No consta en `tar(1)` ni en el manual GNU leído | Declarado oficio |
| 10 | 6 | § 11, BRE/ERE | `grep 'a\|b'` y `grep -E 'a|b'` buscan lo mismo | El manual: `\?`, `\+`, `\|` en básicas son de GNU; «portable scripts should avoid them» | «en GNU grep» y el aviso de portabilidad |
| 11 | 9 | § 13, patrones | «sin patrón… sin acción, se imprime la línea (lo muestra el ejemplo…)» | Regla en `gawk(1)`: «If the pattern is missing…» | Citada la regla |
| 12 | 5 | Siglas | BSD, CPIO, SGI, YUM, STDOUT, LINEAR, FSUSE% sin presentar (dentro de citas) | Sus desarrollos no están en las fuentes leídas | Presentados por su función, sin desarrollo inventado |

Antecedentes de los pasajes cambiados releídos: «la página» (§ 5) remite a `shutdown(8)`, nombrada
en la misma lista; «el ejemplo anterior» (§ 13) es `$1 ~ /J/`, sin acción; «el manual» (§ 11) es el de
GNU grep del epígrafe.

`refutar_prosa.py`: 9 → 3 hallazgos (`BEGIN`, `FS`, `NF`, variables de `awk` explicadas en su
epígrafe; falsos positivos). Nota: el informe de redacción daba otra lista (BEGIN, END, FS, NF, NR,
OFS, PATH, LABEL); la que imprimía la herramienta era la de la fila 12 más `FS` y `NF`.

## No corregido, para la refutación

- `fdisk(8)` dice que **«GPT is always a better choice than MBR, especially on modern hardware with a
  UEFI boot loader»** y que el primer sector de GPT guarda un MBR protector frente a herramientas
  **«MBR-only»**: el tema declara en «Lo que no da» las diferencias MBR/GPT como no
  leídas, pero hay al menos esta frase disponible. Podría ampliarse.
- Universe y Multiverse: la página añade que **«By default, the universe and multiverse repositories
  are enabled»**; el tema no lo dice (no es falso, pero es dato preguntable).
- `useradd`, *Ubuntu*: el tema no cita que `adduser.conf(5)` fije los rangos de UID (la página lo
  remite); sin efecto en lo que afirma.
- Ejemplos propios no ejecutados (`awk` sobre `df -h` y `ps aux`, script de aviso de disco, `dd`):
  sintaxis coherente con las páginas citadas; `--output=pcent` de `df` es columna válida
  (`df(1)`). La columna 4 de `ps aux` como `%MEM` sigue sin fuente y así se declara.

## Otros ficheros tocados

Ninguno fuera del tema y de este informe. Copia previa del tema y anotaciones de trabajo en el
directorio temporal de la sesión.
