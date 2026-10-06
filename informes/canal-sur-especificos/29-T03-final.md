# Puesto 29 · Tema 3 · Revisión final de lo ampliado (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/03-sistemas-de-almacenamiento-y-recuperacion-de-informacion.md`.
Alcance: los once pasajes que lista `29-T03-remate.md`, cada dato contra su fuente y cada remisión contra
su antecedente. Fuentes releídas el 06-10-2026 en `fuentes/canal-sur/informatico/web/`.

## Resultado por pasaje

| # | Pasaje | Fuente releída | Veredicto |
|---|---|---|---|
| 1 | Ficha | — | Correcta; Extensión 12.700 → 12.800 tras las correcciones |
| 2 | Siglas (rpm, TI/O, LUN, ASIC, Sysprep, OOBE, DISM) | OSTEP l. 387; SNIA; Sysprep | Correctas |
| 3 | Qué se puede preguntar | — | Cuadra con lo que el tema da |
| 4 | Índice | `indice.py` | 56 epígrafes; sin cambios |
| 5 | § 2 «Partes y parámetros» | `ostep-file-disks.txt` (v1.10) l. 21-22, 57-73, 218-226, 295-311, 387, 436-472; `seagate-barracuda-ds.txt` (DS17.2-2603US) | Todas las citas literales. **Corregido (error 9/6)**: el ejemplo de 4 KB atribuía los 4 ms de búsqueda a «un disco de 15.000 rpm»; en el manual son la búsqueda media del Seagate Cheetah 15K.5 (l. 432-450). Tabla BarraCuda: rpm, caché (512 MB de 24 a 12 TB; 256 MB el resto), 185-220 MB/s, 512e y los dos ST2000 comprobados modelo a modelo: correcta |
| 6 | § 3 SD | `sda-speed-class.txt` l. 342 | Cita correcta. **Corregido (error 4)**: «no garantiza esa velocidad» suavizaba **«expected write speed will not be available»**; ahora: con símbolos de familias distintas la velocidad esperada no se obtiene |
| 7 | § 4 SAN | `snia-dict-*.txt` | Definiciones literales (iniciador y destino en su acepción [SCSI]; LUN en sus dos acepciones; zonificación [Fibre Channel]). **Corregido (error 6)**: *mapping* se presentaba como «la relación entre un disco virtual y su iniciador»; la SNIA lo define como relación entre dos o más elementos y pone esa como ejemplo |
| 8 | § 5 Tipos de copia | `ms-attrib.txt` l. 82; `ms-xcopy.txt` l. 157, 161, 249; `ms-robocopy.txt` l. 324, 328; `ms-wbadmin-start-backup.txt` l. 120, 125 | Citas literales; oficio bien declarado. **Corregido en el antecedente (error 9)**: el pasaje nuevo remite a «la tabla de `wbadmin`, más abajo», y su fila `-vssCopy` decía «Una copia así no sirve de base para copias incrementales o diferenciales»; la fuente dice lo contrario en sustancia: **«does not affect the sequence of incremental and differential backups that might happen independent of this copy backup»**. Fila reescrita. (La fila no figuraba en la lista del remate; se toca porque es el antecedente de un pasaje cambiado.) |
| 9 | § 7 Sysprep | `ms-sysprep-overview.txt` (2-6-2026) l. 62, 100, 112, 122, 130, 132, 146; `ms-sysprep-generalize.txt` (15-12-2021) l. 62, 70, 72, 82-90, 104, 116-138 | Citas, orden y límite de 1001 (8.1 / Server 2012 o posteriores) correctos; se mantiene el 1001 frente al «unlimited» de la presentación, como hizo el remate. **Corregido**: «aunque el hardware de destino sea igual» por «parecido» (**«similar hardware»**); y **salvedad omitida (error 6)**: generalizar desinstala los dispositivos pero **«doesn't remove device drivers from the PC»** (l. 76), añadida tras la cita del SID y los controladores |
| 10 | Lo que este tema no da | OSTEP (sin «cylinder»); Seagate (sin 2,5″) | Correcto: ni el cilindro ni el 2,5″ constan |
| 11 | Trazabilidad | Fechas «Last updated» de `attrib` (2023-09-25), `xcopy` (2024-05-28), Sysprep (2026-06-02 y 2021-12-15); OSTEP «VERSION 1.10» | Correctas. La atribución a la Universidad de Wisconsin-Madison sale del dominio `wisc.edu` de la URL, no del texto |

## Antecedentes

«El mismo manual» (OSTEP), «la SD Association dice también», «lo anterior» (tabla del atributo), «la
tabla de `wbadmin`, más abajo» (existe, § 5 «Windows: wbadmin»), «Lo último» y «lo penúltimo» (filas de la
tabla de Clonezilla, sin cambiar), «Con Clonezilla, drbl-winroll» (fila de la tabla de Clonezilla). Todos
cuadran tras las correcciones.

## Lentes

- `refutar_prosa.py`: 0 hallazgos.
- `indice.py`: 12.763 palabras, 56 epígrafes.

## Ficheros tocados

- El tema (cinco correcciones y la Extensión).
- Este informe.
