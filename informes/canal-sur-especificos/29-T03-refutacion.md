# Puesto 29 · Tema 3 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). No corrijo: el tema queda como estaba.
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/03-sistemas-de-almacenamiento-y-recuperacion-de-informacion.md`
(939 líneas).

## Alcance

- «Copiado del común»: nada. «Copiado de RTVE sin cambios»: la lista de `29-T03-redaccion.md` (unidades,
  soportes, magnitudes, DAS/NAS/SAN, protocolos, jerarquía, tablas de copia, 3-2-1, política, cinta)
  no se mira en exactitud; sí en cobertura. Lo adaptado de RTVE sí se mira.
- Fuentes releídas el **06-10-2026** sobre los pasajes concretos, en las copias de
  `fuentes/canal-sur/informatico/web/` (descargadas el 05-10-2026): `ms-wbadmin-start-backup.txt`,
  `ms-robocopy.txt`, `sda-speed-class.txt`, `sda-capacity.txt`, `nvme-about.txt`, `nvme-specs.txt`,
  `7zip.txt`, `clonezilla.txt`, `ms-winfr.txt`, `photorec.txt`, `testdisk.txt`,
  `incibe-guia-ransomware.txt` (§ 4 entero), `ms-controlled-folders.txt`, `gnu-gzip.txt`,
  `gnu-tar-compress.txt`, `ms-tar-windows.txt`, `ms-compact.txt`, `ms-zip.txt`, `rsync-man.txt`,
  `ms-windows-backup.txt`, `ms-fsutil-behavior.txt`, `w11-dynamic.txt`. Nada descargado de nuevo.
- Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Lente 1 · Exactitud

Comprobado y correcto (sobre todo la redonda): `wbadmin` (Applies to Windows 10/11/Server, delegación de
permisos, destino por defecto, `-include` y `-allCritical` sólo con `-backupTarget`, `-vssCopy` por
defecto y no válida para incrementales, sobrescritura y subcarpetas); `robocopy` (`/mir` = `/e`+`/purge`,
un millón de reintentos, 30 s, `/log+:`, ejemplo literal, código 8); clases SD (cuatro familias,
literales); NVMe (transportes, 2.4, 4-8-2026); 7-Zip (formatos, LGPL/BSD/unRAR, 26.03); Clonezilla
(variantes, límites); `winfr` (Store, permiso, unidades distintas, modos Regular/Amplia, tabla,
ejemplos, `Recovery_<date and time>`, SSD); PhotoRec (sólo lectura, cabeceras, fragmentación, 480);
TestDisk; INCIBE (apagar, no pagar, plan o última copia, cuatro pasos y cinco etapas, «esclavo» en caso
de que no exista denuncia, denuncia GDT/BIT, Crypto-sheriff, shadow copy, restauración en limpio);
CFA (desactivado por defecto, carpetas fijas ampliables, Documentos); `gzip`, `tar`, `compact`, ZIP
de Windows 11 24H2 y cifrados con 7-Zip o WinRAR; Copias de seguridad de Windows (5 GB, cuentas
profesionales, fin de soporte de Windows 10); RAID-5 en tres o más discos; cuentas RAID rehechas.

### Hallazgos

| # | Gravedad | Error | Pasaje | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|
| M1 | Menor | 9 afirmación contraria a la fuente | «Lo que este tema no da», 1.ª viñeta: «Tampoco la velocidad mínima en MB/s de cada clase de velocidad SD (la SD Association la da en imagen, no en texto).» | La misma página «Speed Class», en texto: **«even those are indicated to the same 10MB/sec write speed»** (Host Class 10 y Card U1, Host U1 y Card V10); y **«symbols with a number indicate minimum writing speed»** | Matizar: «salvo que Class 10, U1 y V10 equivalen a 10 MB/s de escritura, que la página dice en texto; las demás cifras sólo en imagen», y añadir el dato en § 3 |

Sin hallazgo en: cita cruzada (1: remisiones a § 3, § 4, § 7, § 8 y a los temas 2, 4, 6, 9, 11 y 14
cuadran), ley por reglamento (2), recuentos (3: «cuatro familias», «tres variantes», «cinco etapas /
cuatro pasos», «cinco nociones», «tres piezas»), «podrá»/«deberá» (4: «usually (but not necessarily)»,
«Whenever possible», «should only be used» bien llevados), siglas (5), redacción derogada (7: Windows 10
con su fin de soporte), artículo mal (8).

## Lente 2 · Cobertura

Las ocho rúbricas del enunciado tienen epígrafe propio y en su orden. Preguntas: 11 enteras, 1 a medias,
3 no (`29-T03-preguntas.md`). Lagunas (se amplía el tema):

| # | Rúbrica | Qué falta | Preguntas | Propuesta |
|---|---|---|---|---|
| L1 | Discos duros | Lo físico del HDD: geometría (pistas, sectores, cilindros), velocidad de giro, componentes del tiempo de acceso (búsqueda, latencia rotacional, transferencia), formatos de 3,5″ y 2,5″, caché. El § 2 es el más corto del tema (tres párrafos y una tabla) para una rúbrica nombrada | 2 (no), 3 (a medias) | Una subsección «Partes y parámetros» con fuente de fabricante o manual universitario |
| L2 | SAN | Vocabulario de la SAN: iniciador y destino (*target*) iSCSI, LUN, zonificación/enmascaramiento | 9 (no) | Ampliar «SAN» con fuente SNIA (diccionario: LUN, initiator, target, zoning) |
| L3 | Copia de seguridad | Atributo de archivo (qué tipo de copia lo desmarca) y esquemas de rotación (abuelo-padre-hijo) | 11 (no) | Ampliar «Los tipos de copia» con fuente (Microsoft o manual), o declararlo en «Lo que este tema no da» |
| L4 | Clonación | Preparación de una imagen de Windows para despliegue (Sysprep, generalización); el tema sólo da drbl-winroll | 14 (no) | Dos líneas con Microsoft Learn «Sysprep (Generalize)» en § 7, o remisión al tema 6 si allí se trata (no se trata) |

## Recuento

Graves: 0. Menores: 1 (M1). Lagunas: 4 (L1-L4).

## Ficheros tocados

Creados: este informe y `29-T03-preguntas.md`. El tema no se ha modificado.
