# Puesto 29 · Tema 9 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real,
como en la investigación). Escrito por epígrafes, guardando cada parte en el fichero del tema.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/09-administracion-del-sistema-operativo-linux.md`.
Material: `29-investigacion-B-sistemas.md` (§ Tema 9). `AGRUPACION.tsv`: tema 9 «nuevo». Fila de
`informes/canal-sur-reuso/informatica.tsv`: RTVE `tecnica-informatica/14` y `/16`, 20 %, actualizar «no».

## Avance (por epígrafes, guardados uno a uno)

1. Instalación (Ubuntu y Debian vigentes, requisitos, copia previa, ISO, USB, teclas de arranque, pasos).
2. Estructura y sistema de archivos (árbol único, FHS 3.0 + `hier(7)`, tipos de fichero, permisos
   simbólicos y octales, bits especiales, `chown`, `umask`, ACL).
3. Usuarios y grupos (`passwd`, `shadow`, `group`, tipos de UID, root y `sudo`/`sudo-rs`, órdenes
   `adduser`/`useradd`/`usermod`/`userdel`/`groupadd`/`gpasswd`/`passwd`, directorios personales).
4. Shell (Bash, órdenes de navegación y ficheros, `find`, `man`, comodines, comillas, variables y
   parámetros especiales, redirección, tuberías, listas, scripts y estructuras de control).
5. Arranques y paradas (`bootup(7)`, systemd y unidades, *targets* y niveles, `systemctl`, `shutdown`).
6. Herramientas básicas (servicios, `journalctl`, `dmesg`, procesos, `kill`/`nice`, `cron`,
   información del sistema y red, equivalencias con Windows).
7. Sistemas de ficheros (tipos, `mkfs`/`mke2fs`, `mount`/`umount`, `fstab`, `fsck`, intercambio).
8. Gestión de discos (`/dev`, tablas de particiones, `lsblk`/`blkid`/`fdisk -l`/`df`/`du`, `fdisk`,
   `parted`, LVM, `mdadm`, LUKS).
9. Administración del software (APT, `dpkg`, `rpm`, `dnf`).
10. Salvaguarda y restauración (plan de Ubuntu, `tar`, script y rotación, incrementales, `rsync`, `dd`).
11. `grep`. 12. `sed`. 13. `awk`.

`indice.py`: 18.395 palabras (con bloques de código), 84 epígrafes. Portada escrita a mano (el tema no
está en `portadas.tsv`, como los demás de Canal Sur).

`refutar_prosa.py`: 9 hallazgos, todos falsos positivos de «siglas sin presentar»: `BEGIN`, `END`,
`FS`, `NF`, `NR`, `OFS` (variables y patrones de `awk`), `PATH` (variable del intérprete) y `LABEL`
(clave de `fstab`) son nombres de código, siempre en acentos graves y explicados en su epígrafe; el
párrafo de siglas declara que los nombres de orden y de opción van como código. Siglas que sí
faltaban en la primera pasada (DVD, IEEE, UTC), añadidas. Una negrita rota (acento grave dentro de una
cita), corregida. Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni
`refutar_modo.py`.

## Fuentes leídas y fecha

Todas el **05-10-2026**. La investigación dejaba huecos (usermod/userdel/groupadd/sudo, mount, lsblk,
RAID, swap, niveles↔*targets*) y la mayoría de lo que no cubría el RTVE estaba sin extracto. Se
descargaron a texto y se leyeron:

- man7.org (proyecto *man-pages*): `pwd(1)`, `top(1)`, `getfacl(1)`, `setfacl(1)`, `ls(1)`, `chmod(1)`,
  `chown(1)`, `chgrp(1)`, `ps(1)`, `systemctl(1)`, `journalctl(1)`, `crontab(1)`, `crontab(5)`,
  `cron(8)`, `usermod(8)`, `userdel(8)`, `groupadd(8)`, `gpasswd(1)`, `passwd(1)`, `passwd(5)`,
  `shadow(5)`, `group(5)`, `useradd(8)`, `su(1)`, `id(1)`, `sudo(8)`, `mount(8)`, `umount(8)`,
  `lsblk(8)`, `df(1)`, `du(1)`, `mkswap(8)`, `swapon(8)`, `fsck(8)`, `e2fsck(8)`, `blkid(8)`,
  `dd(1)`, `dpkg(1)`, `hier(7)`, `bash(1)`, `systemd(1)`, `systemd.special(7)`, `runlevel(8)`,
  `bootup(7)`, `shutdown(8)`, `ss(8)`, `cryptsetup(8)`, `kill(1)`, `signal(7)`, `nice(1)`, `find(1)`,
  `mkdir(1)`, `ln(1)`, `cp(1)`, `mv(1)`, `rm(1)`, `fdisk(8)`, `mkfs(8)`, `mke2fs(8)`, `lvm(8)`,
  `pvcreate(8)`, `vgcreate(8)`, `lvcreate(8)`, `lvextend(8)`, `fstab(5)`, `rsync(1)`, `man(1)`,
  `parted(8)`, `mdadm(8)`, `tar(1)`, `cat(1)`, `less(1)`, `head(1)`, `tail(1)`, `sort(1)`, `wc(1)`,
  `cut(1)`, `uniq(1)`, `tee(1)`, `tr(1)`, `xargs(1)`, `umask(2)`, `hostnamectl(1)`, `ip(8)`, `rpm(8)`,
  `dnf(8)`, `sysctl(8)`, `htop(1)`, `uname(1)`, `free(1)`, `uptime(1)`, `dmesg(1)`, `last(1)`, `w(1)`,
  `who(1)`, `whoami(1)`, `nohup(1)`, `gawk(1)` (y otras descargadas que el tema no cita).
- manpages.ubuntu.com: `apt(8)` de *resolute* (26.04) y de *noble* (24.04); se usa la de 26.04.
- Ubuntu: release cycle; Server docs «Basic installation», «User management», «Package management»,
  «Backups and version control», «How to back up using shell scripts».
- Debian: «Debian Releases».
- FHS 3.0 (refspecs.linuxfoundation.org).
- GNU: manual de grep; manual de sed; manual de tar 1.35.90 (Synopsis, gzip, Incremental-Dumps); *GAWK
  User's Guide* (Getting Started, Running gawk, Regexp Usage, Fields, Command-Line Field Separator,
  Print Examples, Printf Examples, Using BEGIN/END, User-modified, Auto-set); coreutils 9.12 («What
  information is listed», «Structure of File Mode Bits», «The Umask and Protection»).

**Comprobación de literalidad por script**: las **548** citas en negrita «…» del tema se buscaron en el
texto normalizado de esas páginas; aparecen todas (cinco se corrigieron durante la comprobación:
la nota «[1]» tras GRUB en `bootup(7)`, que ahora va como «[…]»; tres de `ps(1)` que unían líneas
separadas por viñetas, partidas; y un corte de línea en la opción `--listed-incremental=` de tar).
El script comprueba que la cita existe en el conjunto de fuentes, no en la página concreta: el
verificador debe mirar la atribución. Las negritas que eran rótulos y no cita pasaron a cursiva.

## Decisiones frente al material

- **Errata de fuente, declarada en el tema**: la página de Ubuntu «How to back up using shell scripts»
  dice que `0 0 * * *` se ejecuta «every day at 12:00 pm»; por `crontab(5)` es la medianoche. Manda la
  definición de los campos; el tema lo señala con [sic].
- `cron(8)` y `crontab(1)` de man7 son de la variante *cronie* (Red Hat): no se usan sus rutas
  (`/etc/crontab` vacío, `/var/spool/cron`), sólo la sintaxis, que confirma la documentación de Ubuntu.
- `sudo(8)` de man7 es la `sudo` clásica; Ubuntu 25.10 y 26.04 usan `sudo-rs` por defecto (la página de
  Ubuntu lo dice y asegura que lo explicado vale para las dos). El tema lo declara.
- `dnf(8)` de man7 se presenta como «next upcoming major version of YUM»: frase antigua de su propia
  documentación, citada como tal; no se infiere versión.
- Ubuntu Pro «hasta 15 años», que traía la investigación, no aparece en el volcado de la página del
  ciclo leído hoy: no se da.
- Quitado lo que no pude confirmar: fusión de `/bin` en `/usr`; nombres NVMe; diferencias MBR/GPT;
  letras de las órdenes interactivas de `fdisk`; sistema de ficheros por defecto del instalador;
  implementación de `awk` por defecto; refresco implícito de `dnf`; `netstat` disponible en Ubuntu.
  Todo ello va en «Lo que este tema no da».
- Del RTVE se quitó: todo lo de preguntas y respuestas oficiales de su examen, la clasificación de
  núcleos y lo de modo núcleo/usuario (tema 5), las secciones de Windows del 16 (tema 6), la fila de
  Samba («habla el mismo protocolo», sin fuente), la frase «`top` enseña lo que está arriba: los
  procesos que más consumen» (la ordenación por defecto de `top` no consta en `top(1)`), la cadencia
  «abril de los años pares» (sustituida por la cita del ciclo de Ubuntu) y la marca ✔.
- Ejemplos propios, señalados en el texto y no ejecutados: script de aviso de disco, `shutdown`,
  `sed -i.bak` sobre `sshd_config` (directiva no comprobada; vale por la sintaxis), ejemplos de `awk`
  (incluida la columna 4 de `ps aux` como `%MEM`, no comprobada), secuencia para añadir un disco,
  `dd` a imagen. **El verificador debería revisarlos línea a línea.**

## Copiado del común

Ninguno. El tema 9 no invoca norma del temario común de Canal Sur.

## Copiado de RTVE sin cambios

Literal, sin tocar una palabra; sólo se quitó la negrita (en este temario la negrita es cita de fuente
y esos pasajes son oficio) y la marca ✔ de respuesta oficial:

1. `temas/tecnica-informatica/14-…`, § 4, tabla «Familia | Órdenes» (seis filas: dónde estoy, qué se
   ejecuta, permisos, servicios, parámetros del núcleo, buscar dentro de ficheros). En el tema: § 4,
   «Moverse y mirar».
2. 14, § 4, frase «`pwd` es *print working directory*: imprime el directorio de trabajo.» Tema § 4.
3. 14, § 4, frases «`getfacl` es *get file access control list*: obtén la lista de control de acceso
   del fichero. Su pareja es `setfacl`, que la escribe.» Tema § 2, «Permisos extendidos: ACL».
4. 14, § 4, tabla «Básicos | Extendidos» (qué expresan, con qué se ven, con qué se ponen), sin ✔.
   Tema § 2, «Permisos extendidos: ACL».
5. 14, § 5, tabla «Tarea | En Linux | En Windows Server» (cinco filas). Tema § 6, entrada.
6. 16, § 7, frase «Lo mínimo que conviene llevar visto, con su equivalencia:». Tema § 6,
   «Equivalencias con Windows».

## Adaptado de RTVE (sí se verifica)

- 16, § 7, tabla de equivalencias Windows/Ubuntu: quitada la fila de Samba y, en «Ver conexiones», el
  `netstat` de la columna de Ubuntu (sólo consta `ss`, «similar to netstat»). Tema § 6.

## Otros ficheros tocados

Ninguno fuera del tema y de este informe. Descargas de trabajo en el directorio temporal de la sesión.

## Preguntas tipo test de control (10, repartidas por las rúbricas)

Comprobadas contra el tema: las diez se contestan enteras con lo que el tema da.

1. *Instalación.* Según la página oficial del ciclo de Ubuntu, las versiones LTS:
   a) salen cada año y se mantienen tres años; **b) salen cada dos años y reciben cinco años de
   mantenimiento de seguridad estándar**; c) salen cada seis meses y se mantienen nueve meses; d) salen
   cada cuatro años con diez años de mantenimiento. → Tema § 1 (cita del ciclo). Entera.
2. *Estructura y sistema de archivos (práctica).* `chmod 750 informe` deja en `ls -l`:
   **a) `-rwxr-x---`**; b) `-rwxr-xr-x`; c) `-rw-r-----`; d) `-rwx---r-x`. → § 2, cita octal de
   `chmod(1)` y tabla. Entera.
3. *Usuarios y grupos.* Para añadir a `ana` al grupo `prensa` sin quitarle sus otros grupos
   suplementarios: a) `usermod -G prensa ana`; **b) `usermod -aG prensa ana`**; c) `useradd -G prensa
   ana`; d) `groupadd prensa ana`. → § 3 (`-a` «Use only with the -G option» y la nota de que sin `-a`
   se sustituye la lista; `gpasswd -a` y `adduser ana prensa` como alternativas). Entera.
4. *Shell y grep (práctica).* `cat /etc/passwd | cut -d : -f 1,3 | grep -E ':[0-9]{4,}'` muestra:
   a) los usuarios con contraseña de cuatro caracteres o más; **b) nombre y UID de las cuentas con UID
   de cuatro cifras o más**; c) los grupos con más de cuatro miembros; d) las líneas con cuatro campos.
   → § 4 (tuberías, `cut -d -f`), § 11 (ERE, intervalos, ejemplo de Ubuntu), § 3 (UID). Entera.
5. *Arranques y paradas.* El antiguo nivel de ejecución 3 equivale en systemd a, y se fija como
   arranque por defecto con: a) `graphical.target`, `systemctl isolate`; **b) `multi-user.target`,
   `systemctl set-default multi-user.target`**; c) `rescue.target`, `systemctl enable`; d)
   `emergency.target`, `shutdown -r`. → § 5 (tabla de `runlevel(8)` y órdenes). Entera.
6. *Herramientas de administración (práctica).* La línea `30 4 1,15 * 5 /usr/local/bin/copia.sh` de
   un crontab se ejecuta: a) a las 4.30 los días 1 y 15 que caigan en viernes; **b) a las 4.30 los días
   1 y 15 de cada mes y además todos los viernes**; c) a las 30 horas de cada 4 días; d) el día 30 de
   abril. → § 6 (campos y cita «plus every Friday»). Entera.
7. *Sistemas de ficheros y gestión de discos.* `fstab(5)` recomienda identificar el sistema de
   ficheros por `UUID=` o `LABEL=` porque: a) es más corto; **b) los nombres `/dev/sdX` dependen del
   orden de detección y pueden cambiar al añadir o quitar discos**; c) `mount` no admite nombres de
   dispositivo; d) así no hace falta el sexto campo. → § 7 (cita), § 8 (`blkid`, `lsblk -f`). Entera.
8. *Administración del software.* Diferencia entre `apt remove` y `apt purge`:
   **a) `purge` borra además los ficheros de configuración que `remove` deja**; b) `remove` sólo quita
   dependencias; c) `purge` sólo actualiza el índice; d) no hay diferencia. → § 9 (citas de `apt(8)` y
   de Ubuntu; `dpkg -r` frente a `-P`). Entera.
9. *Salvaguarda y restauración (práctica).* `tar -xzvf /mnt/backup/host-Monday.tgz -C /tmp etc/hosts`:
   a) sobrescribe `/etc/hosts`; **b) extrae sólo ese fichero en `/tmp/etc/hosts`**; c) crea una copia
   nueva en `/tmp`; d) lista el contenido sin extraer. → § 10 (cita de Ubuntu y regla de nombres
   relativos de GNU tar). Entera.
10. *sed y awk (práctica).* Para imprimir sólo el nombre de usuario de cada línea de `/etc/passwd`:
    **a) `awk -F: '{ print $1 }' /etc/passwd`**; b) `awk '{ print $1 }' /etc/passwd`; c) `sed -n '1p'
    /etc/passwd`; d) `sed 's/:/ /' /etc/passwd`. → § 13 (`-F`, `$1`, separador por defecto blancos),
    § 12 (`-n` y `p`, `s` sin `g`), § 3 (campos de `passwd`). Entera.
