# Puesto 29 · Tema 9 · Preguntas tipo test (fase 4, refutación)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Contestadas **sólo con el tema**
(`temas/canal-sur-especificos/29-operador-a-informatico/09-administracion-del-sistema-operativo-linux.md`).
Clave en negrita. Resultado: 11 enteras, 1 a medias, 3 no.

1. *Instalación (teoría).* Según la página oficial del ciclo de Ubuntu, una versión intermedia (no LTS) recibe actualizaciones durante:
   a) 5 años; b) 3 años; **c) 9 meses**; d) 6 meses.
   → § 1, cita «only 9 months of updates». **Entera.**

2. *Estructura (teoría).* Directorio para ficheros temporales que se conservan entre reinicios:
   a) `/tmp`; **b) `/var/tmp`**; c) `/run`; d) `/var/spool`.
   → § 2, tabla FHS y cuadro de parejas. **Entera.**

3. *Permisos (práctica).* Tras `chmod 4755 /usr/local/bin/prog`, `ls -l` muestra:
   a) `-rwxr-xr-t`; b) `-rwxr-sr-x`; **c) `-rwsr-xr-x`**; d) `-rwSr-xr-x`.
   → § 2: primer dígito 4 = *setuid*; `s` en el trío del dueño si hay ejecución, `S` sin ella. **Entera.**

4. *Usuarios (teoría).* En `/etc/shadow`, un `!` al principio del campo de contraseña indica que:
   a) la contraseña está vacía; **b) la contraseña está bloqueada**; c) debe cambiarse en el próximo inicio; d) la cuenta es del sistema.
   → § 3, cita de `shadow(5)` y `passwd -l`/`usermod -L`. **Entera.**

5. *Usuarios (teoría).* En Ubuntu, los usuarios del sistema creados dinámicamente al instalar servicios tienen UID:
   a) 0 a 99; **b) 100 a 999**; c) 1000 a 59999; d) 65534.
   → § 3, tabla de tipos por UID. **Entera.**

6. *Shell (práctica).* `ls 2>&1 > dirlist`:
   a) envía salida estándar y de error a `dirlist`; **b) sólo la salida estándar va a `dirlist`; la de error sigue a donde iba la estándar antes**; c) añade al final de `dirlist`; d) da error de sintaxis.
   → § 4, Redirección (ejemplo de `bash(1)`). **Entera.**

7. *Arranques (teoría).* `systemctl enable ssh`, sin más opciones:
   a) arranca el servicio ahora y en cada arranque; **b) lo deja habilitado para el próximo arranque, sin arrancarlo ahora**; c) lo arranca ahora sólo; d) impide arrancarlo.
   → § 6, cita «does not have the effect of also starting»; `--now`. **Entera.**

8. *Herramientas (práctica).* `journalctl -p warning` muestra:
   a) sólo los mensajes de prioridad *warning*; **b) los de *warning* y los de prioridad más importante (*emerg* a *warning*)**; c) los de *warning* a *debug*; d) sólo los del núcleo.
   → § 6, cita sobre «this log level or a lower (hence more important)». **Entera.**

9. *cron (práctica).* `*/15 8-18 * * 1-5 /usr/local/bin/sonda.sh` se ejecuta:
   **a) cada 15 minutos entre las 8 y las 18 h, de lunes a viernes**; b) a las 8.15 y 18.15 todos los días; c) cada 15 horas los días 8 a 18; d) cada 15 minutos de los meses 1 a 5.
   → § 6: campos, rangos, pasos con `/`, ejemplo `1-5` «weekdays». **Entera.**

10. *fstab (teoría).* Valor de `fs_passno` que `fstab(5)` prescribe para el sistema de ficheros raíz:
    a) 0; **b) 1**; c) 2; d) el que se quiera.
    → § 7, tabla de campos. **Entera.**

11. *LVM (práctica).* Para ampliar un volumen lógico y a la vez su sistema de ficheros:
    a) `pvcreate -r`; b) `vgcreate --resize`; **c) `lvextend -r -L +10G vg/lv`**; d) `lvcreate --extend`.
    → § 8, cita de `-r|--resizefs`. **Entera.**

12. *Instalación / software (teoría).* Según la página del ciclo de Ubuntu, la suscripción Ubuntu Pro ofrece hasta:
    a) 5 años de cobertura; b) 10 años; **c) 15 años (ESM y *Legacy add-on*)**; d) 20 años.
    → El tema no lo da (y el informe de redacción dice que no estaba en la página; sí está). **No.**

13. *Administración del software (teoría).* De las cuatro categorías de paquetes de Ubuntu, las que forman el sistema base son:
    **a) Main y Restricted**; b) Universe y Multiverse; c) Main y Universe; d) Restricted y Multiverse.
    → El tema sólo nombra Universe y Multiverse (comunidad, sin parches salvo ESM); no Main ni Restricted, ni que Universe y Multiverse vienen habilitados por defecto. **No.**

14. *Gestión de discos (teoría).* Según `fdisk(8)`, ante un equipo moderno con arranque UEFI:
    a) MBR es preferible por compatibilidad; **b) GPT es siempre mejor opción que MBR**; c) da igual; d) hay que usar la tabla Sun.
    → El tema declara no dar las diferencias MBR/GPT. **No.**

15. *awk (práctica).* `ps aux | awk '{ s += $4 } END { print s }'` suma:
    a) el PID; b) el %CPU; **c) el %MEM**; d) el tamaño virtual.
    → § 13 lo da como ejemplo propio, pero dice que la columna 4 = `%MEM` no se comprobó. **A medias.**
