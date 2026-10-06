# Puesto 29 · Tema 3 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en sus copias de
`fuentes/canal-sur/informatico/web/`, descargadas el 05-10-2026 con URL y fecha en cabecera. Se usó
además `w11-dynamic.txt` (Microsoft Learn es-es, discos básicos y dinámicos, actualizada el 12-2-2026),
ya presente en la carpeta. No se descargó nada nuevo.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/03-sistemas-de-almacenamiento-y-recuperacion-de-informacion.md`.

## Método

- Copiado del común: nada (según `29-T03-redaccion.md`).
- Copiado de RTVE sin cambios: sólo se comprobó que es literal, con un script contra IST 18, TI 15,
  TI 17 y GA 08 (sin negritas ni ✔), por filas de tabla y por frases. Todos los pasajes de la lista
  aparecen tal cual en su origen. No se han re-verificado.
- Adaptado de RTVE (sí verificado): la tabla RAID (contenido igual a RTVE salvo los nombres «RAID n»;
  las cifras de la cuenta con cuatro discos de 4 TB cuadran: 16, 8, 12 y 8 TB), la frase de la SAN y la
  base de datos, el almacenamiento por objetos, el MAM, la cinta y LTFS, y la compresión con y sin
  pérdida.
- Todo lo demás: cada una de las 144 negritas se buscó en la fuente a la que el tema la atribuye
  (script que dice en qué fichero aparece cada cita), y cada página se leyó entera para ver contexto,
  salvedades y lo dicho en redonda, con los nueve errores delante. La negrita de INCIBE que parte un
  salto de página es literal saltando la cabecera.
- Lentes (ENCARGO, tema técnico sin norma): `refutar_prosa.py` 0 hallazgos tras las correcciones;
  `indice.py` 54 epígrafes, el índice no cambia. No proceden `negritas.py`, `refutar_exactitud.py` ni
  `refutar_modo.py`. Literalidad tras las correcciones: 156 negritas, 0 no halladas.

## Hallazgos y correcciones (todas aplicadas, cada una comprobada en su fuente)

| # | Error | Dónde | Qué pasaba | Corrección |
|---|---|---|---|---|
| 1 | 3 recuento | § 3, tarjetas SD | «tres familias de clases de velocidad»; la SD Association define cuatro (falta SD Express, E150-E600) | «cuatro familias», con la cita de SD Express y la de que el número indica la velocidad mínima de escritura |
| 2 | 6 salvedad | § 3, tabla SNIA | La glosa del sobreaprovisionamiento omitía que sirve también para sustituir capacidad inservible por defectos o desgaste | Añadido |
| 3 | 9 | § 3, NVMe | «la vigente es la 2.4» se daba como si la página uniera fecha y número | Se dice que la página no los une en una frase, pero describe el conjunto 2.4 |
| 4 | 6 | § 5, `wbadmin` | Faltaban: «o delegados los permisos»; `-include` y `-allCritical` sólo con `-backupTarget` (si no, falla); la copia `-vssCopy` no sirve para incrementales ni diferenciales; la advertencia de sobrescritura en la misma carpeta compartida | Añadidos |
| 5 | 6 | § 5, `robocopy` | `/log` sobrescribe el registro existente (`/log+:` añade) | Añadido |
| 6 | 9 sin fuente | § 5, VSS | «en el propio disco» / «si el disco muere, mueren con él»: `vssadmin` no lo dice (habla de asociaciones de almacenamiento) | Reescrito: «en el propio equipo», como oficio; añadido a la lista de oficio de la Trazabilidad |
| 7 | 6 | § 5, `rsync -a` | Faltaba que no conserva ACL, atributos extendidos ni enlaces duros; «enlaces» eran simbólicos, «-D» incluye especiales | Precisado |
| 8 | 6 | § 6, `gzip` | El manual dice «Whenever possible» al sustituir por `.gz` | «Siempre que es posible» |
| 9 | 6 | § 6, 7-Zip | Licencia: omitía partes BSD y la restricción unRAR | Añadido |
| 10 | 9 | § 6, `compact` | «transparente para el usuario», sin apoyo en la página | Quitado |
| 11 | 6 | § 7, Clonezilla | Sólo un límite de cuatro: faltaban «no differential/incremental», partición desmontada y no recuperar un fichero suelto de la imagen | Añadidos en la fila «Límites» |
| 12 | 9 | § 7, caso práctico | «1 TB medio vacío» a SSD de 500 GB: unos 500 GB ocupados no caben con margen | «1 TB con 300 GB ocupados» |
| 13 | 9 | § 7, SID | La razón («se llamarían igual») no está en la fuente | Marcado como oficio |
| 14 | 6 / 9 | § 8, SSD y TRIM | «Las fuentes leídas no afirman…»: la página de `winfr` sí advierte que **«Es posible que el espacio libre se sobrescriba, especialmente en una unidad de estado sólido (SSD).»** | Añadida la cita; ajustado el punto de «Lo que este tema no da» (sigue sin afirmarse nada de TRIM) |
| 15 | 9 | § 8, tabla de `winfr` | La tabla de la página dice «Regular» y «Amplia», no «Normal» y «Extenso» | Nota con los literales |
| 16 | 6 | § 8, PhotoRec | Recupera el fichero entero sólo **«If there is no data fragmentation»** | Añadido |
| 17 | 6 | § 8, INCIBE | Faltaba: sin plan de respuesta, usar la última copia; el disco como «esclavo» es **«en caso de que no exista denuncia»** | Añadidos |
| 18 | 1 cita cruzada | § 8, etapas | Las cinco etapas son de la ilustración 5; en el texto son cuatro pasos (A y B del paso 4) | Dicho |
| 19 | 6 | § 8, Acceso controlado a carpetas | «Protege por defecto…» omitía **«CFA is turned off by default.»** | Corregido: viene desactivado; activado, protege una lista fija ampliable |
| 20 | 7 / 6 | § 5, Copias de seguridad de Windows | Windows 10 como vigente sin decir que su soporte acabó el 14-10-2025 (lo dice la página) | Añadido |
| 21 | 9 | § 4, cinta (adaptado) | «la única copia que un fallo del sistema no puede borrar» | «una copia que… no puede borrar mientras está fuera del lector» |
| 22 | 9 | § 4, objetos (adaptado) | «Escala sin límite práctico» | Rebajado y marcado como oficio |
| 23 | 9 | § 3, memorias USB | «su velocidad la da la versión de USB» sin fuente | «depende sobre todo de…», oficio |
| 24 | 5 siglas | Siglas | GUID, SCSI y PCI sin presentar | Presentadas |
| 25 | — | § 4, RAID | Mínimo de tres discos de RAID 5 sólo como oficio | Apoyado en Microsoft (volumen RAID-5 «en tres o más discos físicos»); fuente añadida a portada y Trazabilidad |
| 26 | — | § 6 | Que lo ya comprimido apenas gana, sin apoyo | Cita de Microsoft sobre las JPEG («already highly compressed») |

Trazabilidad puesta al día con lo añadido (wbadmin, SD Express, Clonezilla, CFA, `winfr`, PhotoRec,
`rsync`, INCIBE, página de discos dinámicos). Extensión de la ficha: 10.300 palabras.

## Confirmado sin cambios (muestra)

Las ocho definiciones de la SNIA y la salvedad «usually (but not necessarily)» de la SAN; NAS con NFS o
CIFS; `fsutil` (TRIM activo por defecto en NTFS; 1 desactiva, 0 activa); NVMe (transportes, formatos,
4-8-2026); capacidades y sistemas de ficheros de SD, SDHC, SDXC y SDUC; fundación de la SD Association;
5 GB de OneDrive y la salvedad de las cuentas profesionales; destino por defecto `WindowsImageBackup`;
reintentos (un millón) y espera (30 s) de `robocopy`, su ejemplo y el código 8; órdenes de `vssadmin`;
ejemplo y barra final de `rsync`; LZ77, 60-70 % y 0,015 % de `gzip`; opciones `-z/-j/-J` de `tar`;
formatos, AES-256, 2-10 % y versión 26.03 de 7-Zip; formatos de Windows 11 24H2 y archivos cifrados;
`tar` de Windows basado en bsdtar; algoritmos de `compact /EXE`; ejemplo de rescate de `dd`; 480
extensiones y acceso de sólo lectura de PhotoRec; TestDisk; sintaxis, modos, tabla y ejemplos de
`winfr`; citas de INCIBE y No More Ransom; fechas de actualización de las páginas de Microsoft Learn;
título de la guía de INCIBE (portada: «Una guía de aproximación para el empresario»).

## Lo que no se pudo confirmar

Nada se quitó entero: lo que no tenía apoyo se rebajó y quedó marcado como oficio (filas 6, 10, 13 y
21 a 23). Siguen como oficio declarado la tabla RAID (salvo el mínimo de RAID 5), FC e iSCSI, LTFS, MAM y
los casos prácticos.

## Pasajes cambiados

Los 26 de la tabla (unas 60 líneas del diff). Releídos: «la página» del aviso de `wbadmin` remite a la
de Microsoft Learn citada justo antes; «su página de soporte» de Copias de seguridad de Windows, a la
página que se cita después en el mismo párrafo; «la tabla de la página» de `winfr`, a la tabla de
decisión de delante.

## Otros ficheros tocados

Ninguno, salvo el tema y este informe. Copia del tema antes de verificar y scripts de comprobación en el
scratchpad de la sesión, fuera del proyecto.
