# Puesto 29 · Tema 9 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en las descargas de
redacción (`ub-cycle.txt`, `ub-pkg.txt`, `fdisk.8.txt`, `ps.1.txt`; leídas por el redactor el
05-10-2026). No se descargó nada nuevo.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/09-administracion-del-sistema-operativo-linux.md`
(19.100 → 19.240 palabras según `indice.py`).

## Comprobación de cada corrección en la fuente

| # | Propuesta | Fuente | Resultado |
|---|---|---|---|
| H1 | Columna 4 de `ps aux` = `%MEM` | `ps(1)` l. 352-353 (formato `u`: `user,pid,pcpu,pmem,…`), l. 1038 (`pmem %MEM`), l. 677-679 (`%mem`, definición) | Confirmada. Aplicada |
| L1 | Ubuntu Pro / ESM / Legacy | `ub-cycle.txt` l. 711, 715, 717, 727, 737 | Confirmada. Aplicada |
| L2 | Cuatro categorías; Universe y Multiverse por defecto | `ub-cycle.txt` l. 723; `ub-pkg.txt` l. 738 | Confirmada. Aplicada (la segunda cita es de «Package management», no del ciclo: se atribuye así) |
| L3 | MBR frente a GPT | `fdisk(8)` l. 212-245 | Confirmada. Aplicada, con 4 primarias, lógicas desde 5, 32 bits y 2 TB con sectores de 512 bytes |

Nota de la refutación sobre el informe de redacción (Ubuntu Pro sí está en la página): cierta; no
afecta al tema.

## Pasajes cambiados

1. **Siglas de entrada**: se añade «mantenimiento de seguridad ampliado de Ubuntu (ESM, *Expanded
   Security Maintenance*)»; CVE se añade a las siglas que quedan sin desarrollar dentro de las citas.
2. **§ 1, «Qué distribución se instala»**: nuevo párrafo «*Más allá de los cinco años: ESM y Ubuntu
   Pro.*» (5 años de *Main* con parches CVE; ESM 10 años *Main* y *Universe*; *Legacy add-on* +5,
   15 en total; Pro hasta 15 años; gratis en cinco equipos) y tabla de plazos 5/10/15.
3. **§ 8, «Discos y particiones como ficheros de /dev»**: nuevo bloque «*MBR frente a GPT*, según
   `fdisk(8)`» (GPT 64 bits, particiones ilimitadas salvo el límite habitual de 128, MBR protector;
   MBR con 4 primarias en el sector 0, lógicas desde la 5, 32 bits y 2 TB; GPT siempre mejor con UEFI).
4. **§ 9, «APT», «Los repositorios»**: se sustituye «Además de los repositorios oficiales están
   Universe y Multiverse, mantenidos por la comunidad;» por «*Las cuatro categorías*» (cita y tabla)
   y la cita de «Package management» de que Universe y Multiverse vienen activados (y cómo quitarlos);
   sigue la cita ya existente sobre su falta de soporte («Y la misma guía avisa…»).
5. **§ 13, «Ejemplos de administración»**: la salvedad «no se ha comprobado en la página de `ps`» se
   sustituye por las citas de `ps(1)` (formato `u`, `pmem %MEM`, definición de `%mem`).
6. **«Lo que este tema no da»**: el punto de discos queda en nombres NVMe/tarjetas y órdenes
   interactivas de `fdisk`; se añade que el límite de tamaño de GPT no se ha leído en fuente.
7. **Trazabilidad**: filas del ciclo de Ubuntu (ESM, Legacy, Pro, categorías), «Package management»
   (activados por defecto), herramientas del epígrafe 6 (`ps`, columna `%MEM` del epígrafe 13) y
   discos (MBR frente a GPT).

Antecedentes releídos: «La misma página» (§ 1) remite a la página del ciclo citada justo antes;
«esa guía» y «la misma guía» (§ 9) remiten a «Package management», nombrada en la frase anterior.

## Lentes

- `indice.py`: 19.240 palabras, 84 epígrafes, sin incidencias.
- `refutar_prosa.py`: sin frases repetidas ni negritas rotas; siglas sin presentar: BEGIN, FS, NF
  (nombres de código de `awk`, previos al remate; no son siglas).
- `negritas.py` contra todas las descargas: 529 cotejadas, 4 no halladas, todas previas al remate y
  con elisión «[…]» o «…» (las añadidas, todas halladas).

## Amplió

Sí: tres lagunas (L1-L3) con contenido nuevo; procede la fase 5 bis sobre los pasajes 2, 3 y 4.

## Otros ficheros tocados

Sólo el tema y este informe.
