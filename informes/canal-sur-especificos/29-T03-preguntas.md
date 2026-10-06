# Puesto 29 · Tema 3 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Quince preguntas tipo test de cuatro opciones (teoría
y aplicación práctica), contestadas **sólo con el tema**. Distintas de las diez de control del informe
de redacción. Veredicto: entera (el tema da la respuesta y descarta las demás), a medias (la da sin
seguridad o sólo por descarte), no (el tema no la da).

1. (Unidades, aplicación) ¿Cuántos bits son 2 KiB? a) 16.000; b) 16.384; c) 2.048; d) 2.000.
   **b**. — **Entera** (§ 1, «Las unidades»: 1 KiB = 1.024 B = 8.192 bits).

2. (Discos duros) La velocidad de giro habitual de un disco duro de 3,5″ de sobremesa es: a) 3.600 rpm;
   b) 5.400 rpm; c) 7.200 rpm; d) 15.000 rpm. **c**. — **No**: el tema no da velocidades de giro,
   formatos (3,5″/2,5″), caché ni geometría (pistas, sectores, cilindros).

3. (Discos duros) La parte del tiempo de acceso de un HDD que depende de la velocidad de giro es:
   a) el tiempo de búsqueda; b) la latencia rotacional; c) el tiempo de transferencia; d) la latencia de
   la controladora. **b**. — **A medias**: el tema dice «mover la cabeza y esperar a que el plato pase»,
   pero no nombra búsqueda ni latencia rotacional; se acierta por intuición.

4. (SSD) En Windows, `fsutil behavior query disabledeletenotify` devuelve `DisableDeleteNotify = 1`.
   Significa: a) TRIM activo; b) TRIM desactivado; c) la unidad no es SSD; d) NTFS sin compresión.
   **b**. — **Entera** (§ 3, TRIM: «Disables (1) or enables (0)»).

5. (SSD) Según la SNIA, la capacidad reservada al controlador, no direccionable por el usuario, se
   llama: a) nivelación de desgaste; b) recolección de basura; c) sobreaprovisionamiento; d) TRIM.
   **c**. — **Entera** (§ 3, tabla SNIA).

6. (NVMe) Según NVM Express, NVMe funciona sobre: a) sólo PCIe; b) PCIe, RDMA, TCP y más; c) SATA y
   SAS; d) USB y Thunderbolt. **b**. — **Entera** (§ 3, «NVMe»).

7. (Memorias flash, aplicación) Se compra una tarjeta SD de 1 TB. Es de la clase y sistema de
   ficheros: a) SDHC, FAT32; b) SDXC, exFAT; c) SDUC, exFAT; d) SDXC, NTFS. **b**. — **Entera** (§ 3,
   tabla de capacidades: más de 32 GB a 2 TB).

8. (Memorias flash) ¿Cuál de estos símbolos es una clase de velocidad de vídeo de la SD Association?
   a) U3; b) C10; c) V30; d) E300. **c**. — **Entera** (§ 3, cuatro familias de clases).

9. (SAN) En una SAN iSCSI, el servidor que accede al almacenamiento actúa como … y la unidad lógica que
   le presenta la cabina se identifica por …: a) destino / UNC; b) iniciador / LUN; c) cliente / SID;
   d) iniciador / GUID. **b**. — **No**: el tema no da iniciador, destino (*target*), LUN ni
   zonificación.

10. (RAID, aplicación) Cinco discos de 2 TB en RAID 5 dejan útiles: a) 10 TB; b) 8 TB; c) 6 TB;
    d) 5 TB. **b**. — **Entera** (§ 4, tabla: «la de todos menos uno»).

11. (Copia) ¿Qué tipo de copia desmarca el atributo de archivo de los ficheros copiados y cuál no?
    a) completa e incremental lo desmarcan; diferencial no; b) sólo la completa lo desmarca;
    c) ninguna lo toca; d) sólo la diferencial lo desmarca. **a**. — **No**: el tema define los tipos por
    lo que copian y lo que exige restaurar, sin el atributo de archivo; tampoco da esquemas de rotación
    (abuelo-padre-hijo). Lo más cercano es `-vssFull`, que actualiza el historial.

12. (Copia, aplicación) `wbadmin start backup -allCritical -quiet` sin `-backupTarget`: a) copia en
    `WindowsImageBackup` de C:; b) pide el destino; c) falla; d) copia en la carpeta compartida por
    defecto. **c**. — **Entera** (§ 5, tabla de `wbadmin`).

13. (Compresión) ¿Cuál de estos formatos descomprime 7-Zip pero no puede crear? a) WIM; b) RAR;
    c) XZ; d) TAR. **b**. — **Entera** (§ 6, «7-Zip»).

14. (Clonación, aplicación) Antes de capturar la imagen de un Windows 11 que se va a desplegar en
    cincuenta equipos, la herramienta de Microsoft que lo generaliza (SID, nombre) es: a) `wbadmin`;
    b) Sysprep; c) `robocopy`; d) `compact`. **b**. — **No**: el tema explica por qué cambiar nombre y
    SID y lo resuelve con drbl-winroll de Clonezilla, pero no menciona Sysprep ni la captura de imágenes
    con herramientas de Microsoft.

15. (Virus, aplicación) Según INCIBE, el orden de las etapas tras un *ransomware* es: a) restaura,
    aísla, clona, desinfecta; b) aísla, clona, desinfecta, intenta recuperar, restaura; c) clona,
    aísla, paga, restaura; d) desinfecta, aísla, restaura. **b**. — **Entera** (§ 8, ilustración 5).

Resultado: 11 enteras, 1 a medias, 3 no.
