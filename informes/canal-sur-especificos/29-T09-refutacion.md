# Puesto 29 · Tema 9 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en las descargas de
redacción (directorio temporal de la sesión, `man/`; leídas por el redactor el 05-10-2026). No se
descargó nada nuevo. No corrijo: el remate aplica.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/09-administracion-del-sistema-operativo-linux.md`
(1.868 líneas, ~19.100 palabras). «Copiado del común»: nada. «Copiado de RTVE sin cambios» (seis
pasajes): fuera de la lente de exactitud; dentro de la de cobertura.

## Lente 1 · Exactitud

Método: las 555 negritas «…» vuelven a buscarse en el conjunto de fuentes (0 no halladas); se
contrastan en su página una muestra de datos en redonda y paráfrasis: pasos del instalador, tipos de
UID y `nobody`, `0750`/21.04, `minlen`, `chage`, `addgroup`/`delgroup`, `-R` desaconsejado,
`usermod -l`, `passwd -u/-e`, `sudo -i`, `groupadd -r`, `gpasswd`, comillas de `bash(1)` (cuatro
mecanismos; Korn y C shell), `head`/`tail` 10 líneas, `sort -n/-r`, tipos de unidad de `systemd(1)`,
`/sbin/init`, `shutdown` «+1», `journalctl -n` 10, `nice` 10, teclas `M`/`P` de `top` (heredadas),
`mkswap` tipo 82, `swapon -a` y `noauto`, `fdisk` sector 0, *deb822* y 24.04, Universe/Multiverse,
`tar -p`, `rsync` barra final, `dd status=progress`, `sed` `I` (extensión GNU), ciclo de Ubuntu.

| # | Error | Gravedad | Pasaje | Qué dice el tema | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|---|
| 1 | 9 (al revés) | Menor | § 13, último párrafo y ejemplo `ps aux \| awk '{ s += $4 }…'` | «Que la cuarta columna de `ps aux` es `%MEM` no se ha comprobado en la página de `ps`» | `ps(1)`: **«u Display user-oriented format. (-o user,pid,pcpu,pmem,vsz,rss,tty,stat,start_time,bsdtime,args»**; y **«pmem %MEM see %mem. (alias %mem)»**: la cuarta columna es `%MEM` | Sustituir la salvedad por la cita (y añadir `ps(1)` a lo que sostiene en Trazabilidad; quitarlo de la lista de oficio si figura) |

Sin graves. Notas que no llegan a error: § 1 paso 4 traduce el paréntesis de la fuente como
causal («porque»), aceptable; § 7 `mkswap` vierte «installation scripts» como «instaladores»,
aceptable.

**Error del informe de redacción, no del tema**: dice que «Ubuntu Pro "hasta 15 años"… no aparece en
el volcado de la página del ciclo». Sí aparece (`ub-cycle.txt`): **«It includes up to 15 years of
security coverage (ESM and Legacy add-on)»** y, en ESM, **«providing 10 years of security updates for
the 'Main' repository and also adds 10 years of security coverage for the 'Universe' repository»**.

## Lente 2 · Cobertura del enunciado

Las trece materias del enunciado tienen epígrafe propio, en su orden (instalación … `awk`). Ninguna
queda sin tratar. Huecos preguntables con fuente ya leída:

| # | Laguna | Fuente disponible (ya descargada) | Propuesta de ampliación |
|---|---|---|---|
| L1 | Ubuntu Pro y ESM (años de cobertura) | Página del ciclo: Pro **«up to 15 years of security coverage (ESM and Legacy add-on)»**; ESM **«10 years of security updates for the 'Main' repository… 10 years… 'Universe'»**; **«free for personal use on up to five machines»**; LTS **«security maintained for 5 years with CVE patches for packages in the Main repository»** | § 1, tras la tabla LTS/intermedia; ya se menciona ESM en § 9 sin presentarlo |
| L2 | Las cuatro categorías de paquetes y Universe/Multiverse por defecto | Ciclo: **«'Main' and 'Restricted' (the base system), and 'Universe' and 'Multiverse' (community and extra packages). 'Main' and 'Universe' are open source, while 'Restricted' and 'Multiverse' contain some non-open source software.»**; Package management: **«By default, the universe and multiverse repositories are enabled.»** | § 9, «Los repositorios» (ya lo señalaba la verificación) |
| L3 | MBR frente a GPT | `fdisk(8)`: **«GPT is always a better choice than MBR, especially on modern hardware with a UEFI boot loader»**; MBR protector frente a herramientas **«MBR-only»**; sector 0 con sitio para **«4»** particiones (línea 229, a leer en contexto) | § 8, párrafo de tablas; corregir en consecuencia «Lo que este tema no da» |

## Preguntas

15 en `29-T09-preguntas.md`: **11 enteras, 1 a medias (P15, hallazgo 1), 3 no (P12-P14 = L1-L3)**.

## Recuento

Graves 0 · menores 1 · lagunas 3.

## Otros ficheros tocados

Sólo `29-T09-preguntas.md` y este informe. Nada en el tema.
