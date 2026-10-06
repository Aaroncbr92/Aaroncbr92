# Tema 3 del específico de Operador/a Informático · Sistemas de almacenamiento y recuperación de información

**Siglas**: HDD disco duro; SSD estado sólido; RAID discos redundantes; JBOD sin redundancia; LTO cinta lineal; LTFS su sistema de ficheros; DAS/NAS/SAN conexión directa/conectado a red/red de almacenamiento; FC canal de fibra; LUN unidad lógica; IOPS operaciones por segundo; MAM gestión de activos de medios; RPO/RTO punto/tiempo de recuperación.

Esqueleto para repasar, no resumen: cada línea nombra su fuente; «of.» = oficio, sin fuente.

<!-- indice -->

- [Discos duros](#discos-duros)
- [Discos de estado sólido](#discos-de-estado-sólido)
- [Memorias flash](#memorias-flash)
- [Sistemas SAN y NAS](#sistemas-san-y-nas)
- [Copia de seguridad](#copia-de-seguridad)
- [Compresión de datos](#compresión-de-datos)
- [Clonación de discos](#clonación-de-discos)
- [Borrado accidental](#recuperación-borrado-accidental)
- [Avería](#recuperación-avería)
- [Ataque de virus](#recuperación-ataque-de-virus)

<!-- /indice -->

## Discos duros

- Of., unidades: decimal base 1.000; binaria 1.024. 1 B: 8 bits; 1 KiB: 8.192 bits; 4 KiB: 32.768 bits.
- Of.: HDD vs SSD: tiempo de acceso, no transferencia. Caudal (bits/s; vídeo); IOPS (muchos puestos); dimensionar sólo por TB: error clásico. Avería típica HDD: desgaste mecánico.
- Arpaci-Dusseau, *OSTEP* cap. 37: sectores de 512 B de 0 a n−1; plato, 2 superficies; pista: círculo concéntrico de sectores; 1 cabeza por superficie, brazo; pistas exteriores, más sectores; caché (búfer de pista).
- Arpaci-Dusseau: 7.200 a 15.000 rpm; a 10.000 rpm vuelta ≈ 6 ms. **TI/O = Tseek + Trotation + Ttransfer**. Búsqueda: aceleración, deslizamiento, deceleración, asentamiento (0,5 a 2 ms). Rotación media: media vuelta (15.000 rpm: 4 ms vuelta, 2 ms media). Transferencia: tamaño / caudal pico.
- Seagate BarraCuda 3,5″ (DS17.2-2603US): hasta 24 TB; SATA 6 Gb/s; 512e; 185 a 220 MB/s; 7.200 rpm (24, 20, 16, 12, 2 TB ST2000DM008, 1 TB) o 5.400 rpm (8, 6, 4, 3, 2 TB ST2000DM005); caché 512 MB (24 a 12 TB) o 256 MB.
- Of.: SATA (escritorio); SAS (cabinas); NVMe (muchas colas). SMART, `chkdsk`: tema 2.

## Discos de estado sólido

- SNIA: **«A storage capability built using solid state electronics as the non-volatile storage medium.»** Of.: sin partes móviles; más rápido y caro; escrituras finitas.
- SNIA: nivelación de desgaste: controlador reparte escrituras y borrados entre celdas; TRIM: SO informa de bloques sin uso (ATA TRIM, NVMe Deallocate, SCSI UNMAP); amplificación de escritura: se escribe más de lo pedido, en flash por recolección de basura; sobreaprovisionamiento: capacidad extra reservada al controlador, no direccionable, mejora rendimiento y vida, sustituye capacidad inutilizable.
- Microsoft Learn `fsutil behavior`: TRIM (notificaciones de borrado) activo por defecto en NTFS. `fsutil behavior query disabledeletenotify`; `fsutil behavior set disabledeletenotify {1|0}` (1 desactiva, 0 activa); `= 0`: TRIM activo.
- NVM Express: registros y órdenes del almacenamiento sobre PCIe; estándar de hecho de SSD PCIe; transportes PCIe, RDMA, TCP; U.2, M.2, AIC, EDSFF. Últimas versiones 4-8-2026; NVMe 2.4 vigente.

## Memorias flash

- SNIA: **«A type of non-volatile memory used in solid state storage.»** No volátil: conserva sin alimentación. Of.: misma tecnología en SSD, USB y tarjeta.
- SD Association: SD hasta 2 GB, FAT12 y FAT16; SDHC más de 2 a 32 GB, FAT32; SDXC más de 32 GB a 2 TB, exFAT; SDUC más de 2 a 128 TB, exFAT.
- SD Association: Class 2, 4, 6, 10; UHS U1, U3; vídeo V6, V10, V30, V60, V90; SD Express E150, E300, E450, E600. Número: escritura mínima; clase 10, U1 y V10: 10 MB/s; símbolos de familias distintas entre equipo y tarjeta: no se obtiene velocidad.
- Microsoft: FAT y exFAT para SD, flash o USB (< 4 GB); NTFS para equipos, externos, flash o USB (> 4 GB). USB: tema 4.

## Sistemas SAN y NAS

- Of.: DAS: disco propio, cable propio. NAS: carpeta compartida (ficheros), red general. SAN: disco propio aunque lejano (bloques), red dedicada.
- SNIA, NAS: dispositivos en red con acceso a ficheros; motor de ficheros más discos; NFS o CIFS. Of.: NFS (unix), SMB (escritorio).
- SNIA, SAN: red para transferir datos entre ordenadores y almacenamiento y entre almacenamientos; **«usually (but not necessarily) identified with block services»**. Of.: FC: red dedicada, conmutadores y direccionamiento propios; iSCSI: órdenes de disco por red general.
- SNIA: iniciador: origina orden SCSI de E/S (servidor); destino: recibe (cabina); unidad lógica: entidad direccionable del destino que ejecuta órdenes; LUN: su identificador SCSI en destino («Synonym for logical volume»); zonificación (FC): zonas disjuntas; nodos fuera de zona, salvo direcciones bien conocidas, invisibles.
- Of.: NAS sirve ficheros; SAN sirve bloques (el cliente pone el sistema de ficheros); volumen de bloques en dos máquinas a la vez corrompe. Regla: órdenes de disco, bloques; ficheros o carpetas, ficheros.
- Of., RAID (mínimo; útil; aguanta): 0 reparte, 2, toda, ninguno; 1 espejo, 2, mitad, uno por pareja; 5 paridad distribuida, 3, n−1, uno; 6 doble paridad, 4, n−2, dos; 10 espejo repartido, 4, mitad, uno por pareja. Microsoft: RAID-5 en **«tres o más discos físicos»**; con dos, paridad: espejo.
- Of.: reconstrucción: momento peligroso. Paridad exige leer antes de escribir. JBOD: sin protección. Cuatro de 4 TB: RAID 0 16 TB; 1 o 10, 8 TB; 5, 12 TB; 6, 8 TB.
- Of.: en línea (disco); casi en línea (disco lento o biblioteca con robot); fuera de línea (cinta). MAM: catálogo.

## Copia de seguridad

- Of.: copia: réplica separada, periódica y con restauración probada. Redundancia (fallo de componente) ≠ copia (borrado, corrupción, desastre) ≠ archivo (preserva). RAID no es copia.
- Of.: RPO: datos que se pueden perder (cada cuánto se copia); RTO: cuánto parado. RPO 24 h: copia diaria; 15 min: replicación continua. RTO semana: cinta; hora, no.
- Of., tipos: completa: todo, restaura última; diferencial: cambiado desde última completa, restaura completa + última diferencial; incremental: cambiado desde copia anterior, restaura completa + todas incrementales. Incremental barata de hacer, cara de restaurar.
- Microsoft Learn `attrib`: atributo de archivo marca lo cambiado desde última copia; `xcopy` crea ficheros con él. `xcopy /a` copia marcados sin modificarlo; `/m` copia y lo desactiva. `robocopy /a` sólo con Archive; `/m` igual y lo restablece. Of.: completa copia todo y desmarca; incremental como `/m`; diferencial como `/a`. `wbadmin`: `-vssFull` actualiza historial de cada fichero; `-vssCopy` no.
- Of., abuelo-padre-hijo: hijo diaria, padre semanal, abuelo mensual. 3-2-1: 3 copias (original y dos); 2 soportes; 1 fuera; añadido: inmutable o fuera de línea.
- INCIBE (2020) § 3.2.1: al menos tres copias actualizadas en distintos soportes; lugar distinto del servidor de ficheros; desactivar sincronización persistente de nube; probar a restaurar.
- Of., política: qué, cada cuánto, dónde, cuánto (retención) y cada cuánto se PRUEBA la restauración.
- Of., cinta: menos coste por capacidad; sin energía; soporte separado. Biblioteca: cartuchos (capacidad), lectores (caudal), brazo robótico. LTFS: cartucho como carpeta.
- Soporte de Microsoft, Copias de seguridad de Windows (W11, W10; soporte de W10 finalizó 14-10-2025): Escritorio, Documentos, Imágenes, Vídeos y Música a OneDrive (gratuita 5 GB). Sólo consumidor con MSA; cuentas profesionales o educativas no.
- Microsoft Learn `wbadmin start backup`: Backup Operators o Administrators; símbolo elevado. `-backupTarget:` (letra, volumen o UNC); `-include:`; `-allCritical` (equipo desnudo; sólo con `-backupTarget`); `-systemState`; `-vssCopy` por defecto; `-quiet`. Repetir en la misma carpeta compartida sobrescribe.
- Microsoft Learn `robocopy`: `/s` sin vacíos; `/e` con vacíos; `/z` reiniciable; `/b` modo copia (ignora ACL); `/mir`: `/e` + `/purge`; `/purge` borra en destino lo ausente en origen; `/r:<n>` (1.000.000); `/w:<n>` (30 s); `/log:` sobrescribe, `/log+:` añade. Salida ≥ 8: fallo. Of.: `/mir` replica también lo borrado o cifrado.
- Microsoft Learn `vssadmin`: `list shadows`; `delete shadows`. Of.: instantáneas en el equipo no sustituyen copia. Puntos de restauración: tema 6.
- `rsync(1)`: algoritmo delta; `-a`: `-rlptgoD` (sin ACL, atributos extendidos ni enlaces duros); `-n` ensayo; `--delete` (como `/mir`). Of.: `tar`, copia completa clásica en Linux (tema 9).

## Compresión de datos

- Of.: sin pérdida devuelve original bit a bit; con pérdida descarta. Archivar ≠ comprimir: `tar` junta; `gzip` comprime fichero; ZIP y 7z, ambas.
- GNU gzip: **Lempel–Ziv (LZ77)**; `.gz`; `-d`, `-k`, `-l`, `-r`, `-1` a `-9`; texto −60–70 %; peor caso +0,015 %.
- GNU tar: gzip, bzip2, lzip, lzma, lzop, zstd, xz, compress; `-z` gzip, `-j` bzip2, `-J` xz; `tar czf archive.tar.gz .` crea.
- 7-Zip: 7z con LZMA y LZMA2; empaqueta 7z, XZ, BZIP2, GZIP, TAR, ZIP, WIM (RAR sólo desempaqueta); AES-256 en 7z y ZIP; versión 26.03 (3-9-2026).
- Soporte de Microsoft, Windows 11 24H2: Explorador admite ZIP, RAR, 7z, TAR; no opera con archivos cifrados.
- Microsoft Learn: `tar` incluido en Windows (bsdtar). `compact`: NTFS; `/c`, `/u`; `/EXE`: XPRESS4K (por defecto), XPRESS8K, XPRESS16K, LZX (más compacto).

## Clonación de discos

- Of.: clonar: copiar disco o partición entera; imagen: volcarla a fichero. Lleva arranque y tabla de particiones. 1 TB (300 GB ocupados) a SSD de 500 GB: reducir antes partición.
- Clonezilla: Variantes: live, lite server, SE. Sólo bloques usados; no reconocido: sector a sector con dd; MBR y GPT; BIOS o uEFI; AES-256; multicast en SE; BitTorrent en lite server; drbl-winroll cambia nombre, grupo y SID. Límites: destino igual o mayor; sin diferencial ni incremental; partición desmontada; no recupera fichero suelto.
- Microsoft Learn, Sysprep: prepara Windows para imagen; generalizar quita lo propio del equipo (controladores instalados, SID), no borra controladores. Modo auditoría; sin apps de la Store; `%WINDIR%\system32\sysprep\sysprep.exe /generalize /shutdown /oobe` (`/oobe`: arranca en OOBE); capturar con DISM.
- Sysprep, límites: sólo grupo de trabajo (en dominio lo saca); archivos cifrados NTFS irrecuperables; SID sólo del volumen donde corre; apps de la Store antes: fallo; hasta 1001 ejecuciones por imagen; no admitido en Windows desplegado.
- GNU Coreutils `dd`: copia entrada a salida; discos y particiones (`/dev/sda`). Of.: confundir entrada y salida sobrescribe el origen. Disco que falla: imagen primero: `dd conv=noerror,sync iflag=fullblock </dev/sda1 > /mnt/rescue.img` (sigue tras errores, rellena con NUL; partición sin montar). Mejor: GNU ddrescue.

## Recuperación, borrado accidental

- PhotoRec: al borrar se pierde metainformación (nombre, fecha, tamaño, primer bloque); datos siguen hasta sobrescribirse. Microsoft: espacio marcado libre. **do NOT save any more pictures or files** en ese dispositivo; no recuperar a la misma partición; minimizar uso del equipo.
- Of., orden: 1 Papelera; 2 copia, instantánea o nube; 3 herramienta sobre disco.
- Soporte de Microsoft, Recuperación de archivos de Windows (`winfr`, Store, W11 y W10): borrados de almacenamiento local (internas, externas, USB), no de Papelera; no admite recursos compartidos ni nube. **«winfr source-drive: destination-drive: [/mode] [/switches]»**; origen y destino distintos.
- `/regular` (normal): NTFS no dañadas; `/extensive` (extensivo): todos sistemas; fuera de NTFS sólo extensivo; en duda, Normal. NTFS recién borrado: normal; borrado hace tiempo, tras formatear o dañado: extenso; FAT y exFAT: extenso.
- `/n` filtra por nombre, ruta, tipo o comodín. Resultado en `Recovery_<date and time>`.
- CGSecurity, PhotoRec: ignora el sistema de ficheros, busca cabeceras; entero sin fragmentación; más de 480 extensiones; sólo lectura. TestDisk: recupera particiones y hace arrancar discos; recupera ficheros de FAT, exFAT, NTFS y ext2.
- Microsoft: en SSD espacio libre se sobrescribe más.

## Recuperación, avería

- Of., lógica: TestDisk (partición); `chkdsk` (tema 2); PhotoRec o `winfr` extenso. Física con disco legible: imagen con `dd conv=noerror,sync` o ddrescue. RAID: sustituir y reconstruir; copia al día antes.

## Recuperación, ataque de virus

- INCIBE: **«lo primero es apagar el equipo afectado»**; no pagar nunca (no garantiza recuperar ni evita segundo rescate); plan de respuesta si existe; si no, última copia.
- INCIBE, etapas AÍSLA, CLONA, DESINFECTA, INTENTA RECUPERAR, RESTAURA. Aislar: sacar equipo de la red; sospechar de discos, unidades de red y nube conectados; cambiar contraseñas de red y cuentas online.
- Clonar: clonación completa; recuperar sobre el clon, conservar original; disco «esclavo» en otro ordenador aislado; salvar sólo datos importantes (documentos, fotos, certificados), no ejecutables. Denunciar: Guardia Civil (Grupo de Delitos Telemáticos); Policía Nacional (Brigada de Investigación Tecnológica).
- Desinfectar clon con antivirus actualizado antes de recuperar. Intentar recuperar: www.nomoreransom.org (EUROPOL), «Crypto-sheriff» con dos ficheros cifrados o nota de rescate; sin solución, conservar disco cifrado.
- Restaurar: revisar shadow copy o snapshot; disco nuevo o formateado, instalación limpia, copia más reciente anterior a la infección.
- Microsoft Learn, Acceso controlado a carpetas: sólo apps de confianza cambian ficheros protegidos; desactivado por defecto; incluye Documentos.
