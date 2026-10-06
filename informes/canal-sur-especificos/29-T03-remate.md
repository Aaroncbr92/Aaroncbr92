# Puesto 29 · Tema 3 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/03-sistemas-de-almacenamiento-y-recuperacion-de-informacion.md`.
Entrada: `29-T03-refutacion.md` (M1, L1-L4) y `29-T03-preguntas.md` (11 enteras, 1 a medias, 3 no).
**Se amplió contenido nuevo**, así que procede la fase 5 bis sobre los pasajes listados.

## Comprobación en fuente de cada corrección

| # | Veredicto | Fuente releída (06-10-2026) |
|---|---|---|
| M1 | Correcto: se aplica | `sda-speed-class.txt` l. 342: «…Host Class 10 and Card U1, Host U1 and Card V10, etc. even those are indicated to the same 10MB/sec write speed». |
| L1 | Laguna real: se amplía | Nuevas: `ostep-file-disks.pdf/.txt` (Arpaci-Dusseau, OSTEP v1.10, cap. 37) y `seagate-barracuda-ds.pdf/.txt` (DS17.2-2603US). |
| L2 | Laguna real: se amplía | Nuevas: `snia-dict-{initiator,target,logical-unit,logical-unit-number,lun,zoning,mapping}.txt`. «LUN masking» no tiene entrada en el diccionario (404 en `lun-masking`, `masking`, `lun-mapping-and-masking`); se declara. |
| L3 | Laguna real: se amplía | Nuevas: `ms-attrib.txt`, `ms-xcopy.txt`; ya estaba `ms-robocopy.txt` (`/a`, `/m`), y `ms-wbadmin-start-backup.txt` (`-vssFull`). No encontré fuente que vincule el atributo con los tipos de copia (la antigua KB de Microsoft da 404) ni que describa el esquema abuelo-padre-hijo: los dos se dan como oficio declarado. |
| L4 | Laguna real: se amplía | Nuevas: `ms-sysprep-overview.txt` (actualizada el 2-6-2026) y `ms-sysprep-generalize.txt` (15-12-2021). No uso el «unlimited number of times» de la página de presentación porque contradice el límite de 1001 de la otra página; se da el 1001. |

Todas las fuentes nuevas están en `fuentes/canal-sur/informatico/web/` con la cabecera URL/Leído 2026-10-06.

## Pasajes cambiados

1. **Ficha**: Fuente (OSTEP, Seagate, `attrib`, `xcopy`, Sysprep), Redacción (fecha del remate),
   Extensión 10.300 → 12.700.
2. **Siglas**: rpm, TI/O, LUN, ASIC, Sysprep, OOBE, DISM.
3. **Qué se puede preguntar**: partes y tiempo de acceso del HDD; vocabulario SAN; atributo de archivo
   y abuelo-padre-hijo; Sysprep.
4. **Índice**: regenerado con `indice.py` (56 epígrafes).
5. **§ 2, nuevo «Partes y parámetros»** (L1): tabla de piezas (sector, plato, superficie, eje, pista,
   cabeza y brazo, zonas, caché); rpm (7.200-15.000; 6 ms por vuelta a 10.000); TI/O = búsqueda +
   rotación + transferencia, fases de la búsqueda, latencia media de media vuelta; ejemplo de 4 KB;
   escritura diferida (*write back*) e inmediata (*write through*); los dos mercados; tabla BarraCuda 3,5″
   (SATA 6 Gb/s, 7.200/5.400 rpm por modelo, caché 512/256 MB, 185-220 MB/s, 512e).
6. **§ 3, «Tarjetas de memoria SD»** (M1): la clase 10, la U1 y la V10 equivalen a 10 MB/s, más la
   advertencia de la SD Association sobre mezclar familias.
7. **§ 4, «SAN»** (L2): tabla SNIA de iniciador, destino, unidad lógica, LUN y zonificación; ejemplos
   típicos; aplicación a iSCSI; *mapping*.
8. **§ 5, «Los tipos de copia»** (L3): atributo de archivo según `attrib`; tabla `/a` y `/m` de `xcopy`
   y de `robocopy`; `xcopy` crea los ficheros con el atributo marcado; relación con completa,
   incremental y diferencial (oficio); historial de VSS de `wbadmin`; abuelo-padre-hijo (oficio).
9. **§ 7, nuevo «Preparar una imagen de Windows: Sysprep»** (L4): definición, generalizar (SID y
   controladores), obligación de generalizar, procedimiento en cuatro pasos con la orden
   `sysprep.exe /generalize /shutdown /oobe` y la captura con DISM, seis limitaciones y el contraste con
   drbl-winroll.
10. **«Lo que este tema no da»**: matizada la viñeta de SD (M1). Nueva viñeta: cilindro, formato de 2,5″ y
    su velocidad, enmascaramiento de LUN.
11. **Trazabilidad**: nuevas filas OSTEP, Seagate, SNIA (SAN), `attrib`/`xcopy`, Sysprep; SD y `robocopy`
    ampliadas; `wbadmin` con el historial. La lista de oficio añade el atributo frente a los tipos de copia
    y el esquema abuelo-padre-hijo.

Antecedentes releídos: «El mismo manual» (tras OSTEP), «la SD Association dice también» (antes era «la
misma página», sin antecedente: corregido), «lo anterior» (la tabla del atributo), «más abajo» (tabla de
`wbadmin` en § 5). Todos cuadran.

## Preguntas de refutación tras el remate

2 (rpm): entera (BarraCuda 3,5″ y rango del manual). 3 (latencia rotacional): entera. 9 (iniciador/LUN):
entera. 11 (atributo de archivo): entera, apoyada en oficio declarado. 14 (Sysprep): entera. Quedan 15 de 15.

## Lentes

- `indice.py`: regenerado; 12.708 palabras, 56 epígrafes.
- `refutar_prosa.py`: un hallazgo (TI/O sin presentar), corregido en siglas; 0 al final.
- `negritas.py`, `refutar_exactitud.py` y `refutar_modo.py` no proceden: es un tema técnico sin norma.

## Ficheros tocados

- El tema.
- Este informe.
- Fuentes nuevas en `fuentes/canal-sur/informatico/web/`: `ostep-file-disks.pdf`, `ostep-file-disks.txt`,
  `seagate-barracuda-ds.pdf`, `seagate-barracuda-ds.txt`, `snia-dict-initiator.txt`,
  `snia-dict-target.txt`, `snia-dict-logical-unit.txt`, `snia-dict-logical-unit-number.txt`,
  `snia-dict-lun.txt`, `snia-dict-zoning.txt`, `snia-dict-mapping.txt`, `ms-attrib.txt`, `ms-xcopy.txt`,
  `ms-sysprep-overview.txt`, `ms-sysprep-generalize.txt`.
