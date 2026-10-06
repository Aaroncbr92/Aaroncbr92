# Tema 9 del específico de Operador/a Informático · Administración del sistema operativo Linux

**Siglas**: LTS, ESM, FHS, UID, GID, ACL, PID, UEFI, GRUB, MBR, GPT, UUID, LVM (PV, VG, LV), RAID, LUKS, APT, RPM, DNF, NFS, WAN, BRE, ERE.

Esqueleto para repasar, no resumen: cada línea lleva su fuente; el detalle está en el tema.

<!-- indice -->
<!-- /indice -->

## 1. Instalación
- Ubuntu release cycle: versión cada 6 meses, numerada año.mes (26.04, abril 2026); LTS cada 2 años, 5 años de seguridad estándar (*Main*), para producción; intermedia 9 meses; en curso 26.04 LTS, 24.04 LTS aún mantenida.
- Ubuntu Pro: ESM 10 años (*Main*, *Universe*); *Legacy add-on* +5 = 15; gratis personal, 5 equipos.
- Debian: estable 13 *trixie*, revisión 13.7 (12-09-2026); *bookworm* oldstable. Versiones RPM: no consultadas.
- Tutorial Ubuntu Server: amd64, arm64, ppc64el, s390x; RAM 2 GB, disco 5 GB; copia previa; ISO de releases.ubuntu.com con instalador; USB de arranque; menú firmware: Escape, F2, F10 o F12.
- Pasos: idioma; actualizar instalador; teclado; red (DHCP, sigue sin red); sin proxy; «use an entire disk»; usuario, hostname, contraseña; SSH y snap; reiniciar. Usuario = grupo `sudo`.

## 2. Estructura y sistema de archivos
- mount(8): un solo árbol con raíz `/`; sin letras de unidad.
- FHS 3.0 (2015): `/bin` órdenes esenciales de todos; `/sbin` de sistema; `/boot` gestor de arranque; `/dev` dispositivos; `/etc` configuración del equipo; `/home` personales; `/root` del superusuario; `/lib` bibliotecas; `/media` extraíbles; `/mnt` montaje temporal; `/opt` aplicaciones añadidas; `/proc`, `/sys` virtuales; `/run`; `/srv`; `/tmp` borrable sin aviso; `/usr` sólo lectura (`/usr/bin`, `/usr/sbin`, `/usr/local`); `/var` variable; `/var/log`; `/var/spool` (cron, lpd, mail); `/var/tmp` sobrevive al reinicio.
- coreutils, `ls -l`: `-` normal, `d`, `l` simbólico, `b` bloques, `c` caracteres, `p` FIFO, `s` socket. `ln` duro por defecto (destino existente), `-s` simbólico.
- chmod(1): u g o a; r w x; `+` `-` `=`; octal r4 w2 x1, hasta 4 dígitos (primero: setuid 4, setgid 2, sticky 1). 755 rwxr-xr-x; 750 rwxr-x---; 644 rw-r--r--; 600 rw-------.
- Directorio: r lista, w crea y borra, x accede. setuid: identidad del dueño; setgid en directorio: hereda grupo; sticky: sólo dueño borra o renombra (`/tmp`). En `ls`: `s`/`S`, `t`/`T`.
- `chown ana:prensa f` (sin espacios); `chgrp` grupo. umask(2): bits apagados; 022; 0666 & ~022 = 0644.
- ACL: `getfacl` ve, `setfacl` pone (`-m u:lisa:r f`, `-x g:staff f`, `--set-file=-`). Básicos: `ls -l`/`chmod`.

## 3. Usuarios y grupos
- Ubuntu «User management»: locales en `/etc/passwd` y `/etc/group`.
- passwd(5), 7 campos: name:password:UID:GID:GECOS:directory:shell; `x` = clave en shadow; lo lee todo el mundo, escribe el superusuario; root UID 0; shell vacío = /bin/sh.
- shadow(5), 9 campos: nombre, clave, último cambio (días desde 1970-01-01 UTC; 0 = cambiar al entrar), mínima, máxima, aviso, inactividad, caducidad, reservado; `!` = bloqueada.
- group(5): group_name:password:GID:user_list; claves en `/etc/gshadow`. `id`: UID y GID.
- UID: 0-99 sistema; 100-999 dinámicos; 1000-59999 corrientes; `nobody` 65534.
- Root sin contraseña válida; `sudo` con clave propia y rastro; primer usuario en grupo `sudo` (`/etc/sudoers`); `sudo passwd` habilita root, `-l root` bloquea; sudo-rs desde 25.10 (clásico `sudo.ws`); `sudo -l`, `-u`, `-i`.
- `adduser`/`useradd -m -s`; `deluser`/`userdel -r` (home y spool de correo); `addgroup`/`groupadd`; `adduser n g`/`usermod -aG`/`gpasswd -a`; `passwd -l/-u`/`usermod -L/-U`; `chage -l`. `-G` sin `-a` sustituye (oficio); `-g` primario; `-u` único salvo `-o`; `usermod -l` no renombra home, `-d -m` lo mueve, `-e` caducidad; `passwd -e` caduca ya, `-S` estado; `groupadd -g`, `-r`.
- `/etc/skel`. Baja: home no se borra; mismo UID heredaría carpeta (`chown -R root:root`, `/home/archived_users/`).
- Home 0750 desde 21.10 (antes 0755); `DIR_MODE=0750` en `/etc/adduser.conf`; clave mínima 6, `/etc/pam.d/common-password`, `minlen=8`.

## 4. Utilización del shell
- bash(1): reimplementa Bourne; POSIX. `pwd`; `cd` (sin argumento, HOME); `ls -a -l -h`; `~` = HOME.
- `mv` también renombra; `head`/`tail` 10 líneas, `-n`, `tail -f`; `find -name -type -user -size -mtime`.
- `man`: secciones 1 órdenes, 5 formatos, 8 administración; `man -k`; `--help`.
- Comodines: `*` cualquier cadena; `?` un carácter; `[...]` uno del conjunto, `!`/`^` niega; los expande el shell.
- Comillas: escape `\`, simples (literal), dobles (respetan `$`, acento grave, `\`).
- Variables: `n=valor` sin espacios; `export`; `unset`; `PATH`; `$?` (0 éxito); `$$` PID; `$0`; `$1`; `$#`; `$(orden)`; `alias`.
- Redirección: descriptores 0, 1, 2; `<`; `>` trunca; `>>` añade; `2>`; `2>&1`; `&>`; `&>>`. `ls > f 2>&1` ambas; `ls 2>&1 > f` sólo la estándar.
- Tuberías `|`; `sort -n -r`, `uniq` (adyacentes, `-c`), `wc -l`, `cut -d -f`, `tr`, `tee -a`, `xargs`. Listas: `;` secuencial; `&` segundo plano; `&&` si éxito; `||` si fallo.
- Scripts: `#!` primera línea; `chmod u+x`; `if/elif/else/fi`; `for`; `while`/`until`; `case/esac`.

## 5. Arranques y paradas
- bootup(7): firmware → gestor (systemd-boot, GRUB) → núcleo → initramfs (CPIO en tmpfs; antes initrd) → systemd. Parada: detiene servicios, desmonta, apaga.
- systemd(1): PID 1, `/sbin/init`. Unidades: `.service`, `.socket`, `.target` (agrupan), `.device`, `.mount`, `.timer` (como cron).
- runlevel(8): 0 `poweroff.target`; 1 `rescue.target`; 2, 3, 4 `multi-user.target` (sin gráfico); 5 `graphical.target`; 6 `reboot.target`; equivalencia «aproximada». `emergency.target`: PID 1 y shell; también si falla fsck necesario.
- `default.target`: `get-default`, `set-default multi-user.target`, `isolate rescue.target`, `rescue`, `emergency`.
- `systemctl poweroff`, `reboot`, `halt`. shutdown(8): `hh:mm`, `+m`, `now` (= +0); sin hora +1; mensaje; `-P` (defecto), `-r`, `-H`, `-h` = `--poweroff`, `-c` cancela; `/run/nologin` 5 min antes.

## 6. Herramientas básicas de administración
- systemctl(1), `.service` por defecto: `start`, `stop`, `restart`, `reload` (configuración del servicio), `status` (más diario), `enable` (no arranca), `enable --now`, `disable`, `mask`, `is-active`, `is-enabled`, `list-units`, `--failed`, `daemon-reload`. `start/stop` ahora; `enable/disable` próximo arranque.
- journalctl(1): `-u`, `-f`, `-b`, `-p` (emerg 0, alert 1, crit 2, err 3, warning 4, notice 5, info 6, debug 7; ese nivel y más graves), `-n` (10), `-r`, `--since`/`--until`, `-k`,. `/var/log`; `dmesg` búfer del núcleo.
- `ps` instantánea (`-ef`, `aux`; Unix con guion, BSD sin, GNU `--`); `top` (`k`, `r`, `q`, `M`, `P`).
- `kill` TERM por defecto; KILL (9) no capturable; SIGHUP 1, SIGINT 2, SIGTERM 15. `nice` -20 a 19, +10 por defecto; `nohup`.
- crontab: `-e`, `-l`, `-r`, `-u`; `sudo crontab -e` = root. Campos: minuto 0-59; hora 0-23; día mes 1-31; mes 1-12; día semana 0-7 (0 y 7 domingo). `*`, `8-11`, `1,15`, `*/2`; día mes y semana: basta uno. `@reboot`, `@daily` = `0 0 * * *`, `@weekly` = `0 0 * * 0`, `@monthly`, `@yearly`, `@hourly`.
- `5 0 * * *` 00:05 diario; `15 14 1 * *` 14:15 día 1; `0 22 * * 1-5` 22:00 laborables. Errata Ubuntu: `0 0 * * *` = medianoche, no «12:00 pm».
- `uname -a`; `uptime` (carga 1, 5, 15 min); `free -h`; `who`, `w`, `last`; `whoami`; `ip`; `ss` (≈ netstat).
- Windows: registro=visor de eventos; tareas=programador; sudo=UAC; LUKS=BitLocker.

## 7. Sistemas de ficheros
- fstab(5): ext4, xfs, btrfs, f2fs, vfat, ntfs, hfsplus, tmpfs, sysfs, proc, iso9660, udf, squashfs, nfs, cifs. Swap no lo es.
- `mkfs` obsoleto frente a `mkfs.<tipo>`; `mke2fs` = ext2/3/4; `-L` máx. 16 bytes. Formatear destruye (oficio).
- mount(8): `mount -t tipo disp dir`; oculta el contenido previo; root; `-a` todo fstab salvo `noauto`; `-o`: `ro`, `rw`, `noexec`, `noauto`, `user`, `defaults` = rw, suid, dev, exec, auto, nouser, async. `umount`: «busy» si hay ficheros abiertos o directorio de trabajo dentro.
- `/etc/fstab`, 6 campos: `fs_spec` (qué); `fs_file` (punto); tipo (o `swap`); opciones (al menos `defaults`); `fs_freq` dump (0); `fs_passno` raíz 1, resto 2, 0 no se comprueba.
- LABEL o UUID recomendado: `/dev/sdX` cambia con el orden de detección. `blkid`, `lsblk -f`. Tras editar: `systemctl daemon-reload`; `mount -a` (oficio).
- fsck: `-A` recorre fstab; e2fsck no seguro con montado.
- Swap: `mkswap`; `swapon` (`-a`, `--show`); `swapoff`.

## 8. Gestión de discos
- Dispositivos de bloques en `/dev`; tabla en sector 0.
- fdisk(8) GPT: 64 bits, sumas de comprobación, UUID, particiones ilimitadas (usual 128), MBR protector. MBR: 4 primarias (1-4), extendida con lógicas desde 5; 32 bits, hasta 2 TB con 512 bytes. GPT mejor, sobre todo con UEFI.
- `lsblk` (árbol; `-f` = NAME,FSTYPE,FSVER,LABEL,UUID,FSAVAIL,FSUSE%,MOUNTPOINTS); `blkid`; `fdisk -l`; `df -h` (libre); `du -sh` (ocupa).
- `fdisk` interactivo (GPT, MBR, Sun, SGI, BSD), escribe al final; `parted` (MS-DOS y GPT).
- lvm(8): PV (disco o partición), VG (colección de PV), LV (se formatea y monta). `pvcreate`, `vgcreate`, `lvcreate --type raid1 -m1 -L 500m -n mylv vg00`, `lvextend -L +54 vg01/lvol10`, `vgextend`; `-r` amplía el sistema de ficheros.
- mdadm(8): LINEAR, RAID0 (bandas), RAID1 (espejo), RAID4, RAID5, RAID6, RAID10, MULTIPATH, FAULTY, CONTAINER. `mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/hd[ac]1`;- cryptsetup: LUKS2 por defecto; dm-crypt; `luksFormat /dev/sdb1`; `open --type luks /dev/sdb1 seguro`.

## 9. Administración del software
- rpm(8): paquete = ficheros + metadatos; `.deb` (Debian, Ubuntu), `.rpm`. Bajo nivel `dpkg`, `rpm` (sin dependencias ni descarga); alto nivel `apt`, `dnf`; Aptitude menús.
- APT: índice desde `/etc/apt/sources.list.d/ubuntu.sources` (antes de 24.04, `/etc/apt/sources.list`). *Main*, *Restricted* (base); *Universe*, *Multiverse* (comunidad); *Restricted*, *Multiverse* con software no abierto; Universe y Multiverse activados, sin parches salvo ESM.
- `update` (índice); `upgrade` (nunca elimina); `full-upgrade` (puede eliminar); `install`; `remove` (deja configuración); `purge` = `remove --purge`; `autoremove`; `search`; `show`; `list --installed`.
- `apt` interactivo; `apt-get` en scripts; Ubuntu Server: seguridad automática.
- dpkg: `-l`; `-L` ficheros del paquete; `-S` paquete de un fichero; `-i`; `-r` (salvo conffiles); `-P` (todo). Desinstalar con dpkg no recomendado.
- rpm: `-i`, `-U`, `-e`, `-q`, `-qa`. dnf (sucesor de YUM): `install`, `remove`, `upgrade`, `search`, `info`, `list --installed`.

## 10. Salvaguarda y restauración
- Ubuntu Server: plan = qué, cada cuánto, dónde, cómo restaurar; soportes fuera de sede o por WAN; varios métodos.
- Bacula (varios sistemas, red); rsnapshot (uno, SSH); incremental = cambios desde la última; `etckeeper`: `/etc` en VCS.
- tar(1): `-c`, `-x`, `-t`, `-v`, `-f`, `-z` gzip, `-j` bzip2, `-J` xz, `-C`, `-p`, `-g`. Nombres relativos salvo `--absolute-names`; lectura detecta compresión.
- `tar czf`; `tar -tzvf`; `tar -xzvf f.tgz -C /tmp etc/hosts` → `/tmp/etc/hosts`; `cd / && sudo tar -xzvf …` sobrescribe. Mejor prueba: restaurar un fichero.
- Script Ubuntu: `/home /var/spool/mail /etc /root /boot /opt` a `/mnt/backup` (NFS); `$hostname-$day.tgz`; `sudo crontab -e`; abuelo-padre-hijo (diaria dom-vie, semanal sábado, mensual día 1).
- GNU tar: `-g`/`--listed-incremental=snap` o `-G`; fichero inexistente = nivel 0.
- rsync(1): delta-transfer; `-a` = `-rlptgoD` (sin `-A`, `-X`, `-H`); barra final del origen = contenido; `--delete` espejo; `-n` simulación.
- dd(1): `if=`, `of=`, `bs=` (512), `count=`, `status=progress`; `of=` erróneo destruye. No copiar `/proc`, `/sys`, `/tmp` (oficio).

## 11. Filtros: grep
- GNU grep: busca patrones, copia líneas coincidentes; sin fichero, entrada estándar.
- `-i` ignora mayúsculas; `-v` invierte; `-w` palabras; `-c` cuenta líneas; `-l` nombres de fichero; `-n` número de línea; `-r` recursivo; `-E` ERE; `-F` cadenas fijas.
- Salida grep: 0 hay línea; 1 ninguna; 2 error.
- Regex: `.`; `*` cero o más; `+` una o más (ERE); `?` opcional (ERE); `{n}`, `{n,}`, `{n,m}`; `^`, `$`; `[...]`, `[^...]`. No es el comodín del shell.
- BRE: `? + { | ( )` pierden significado, con barra `\?` `\+` `\{` `\|` `\(` `\)`; `\|` no portable. `grep -E ':[0-9]{4,}'` = UID de 4 cifras o más.

## 12. Editor de flujo: sed
- GNU sed: una pasada, filtro en tuberías; lee línea, ejecuta, imprime salvo `-n`.
- `s/regexp/reemplazo/flags`: sin `g` sólo la primera por línea; `g` todas; número N la N-ésima; `I` insensible. `&` lo encontrado; `\1`…`\9` grupos.
- Direcciones: `144s/…`; `/apple/s/…`; `4,17s/…`; `/apple/!s/…`; `$` última.
- `d` borra; `p` imprime; `-n` sin impresión automática; `-e`; `-f`; `-i[SUFIJO]` en el sitio (`-i.bak`); `-E` ERE; `y/abc/xyz/`.

## 13. Lenguaje awk
- gawk: `patrón { acción }`, dirigido por datos; `awk 'programa' f`.
- Campos por espacios; `$1`; `$0` registro entero; `$NF` último; `NF` campos; `NR` registros procesados; `FS` entrada (`-F`; `-f` es fichero); `OFS` salida (un espacio).
- Patrones: `/regex/`; `~`, `!~`; sin patrón = todo; sin acción = `{ print }`. `BEGIN` una vez antes; `END` una vez después; contadores a cero.
- `print $1, $2` → `Jan 13`; `print $1 $2` → `Jan13`; `printf` da formato.
- Propios: `awk -F: '$3 >= 1000 { print $1 }' /etc/passwd`; `ps aux | awk '{ s += $4 } END { print s }'` (`%MEM`).
- Oficio: `grep` selecciona; `sed` sustituye; `awk` calcula.
