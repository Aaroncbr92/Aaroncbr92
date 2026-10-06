# Puesto 29 · Tema 9 · Revisión final (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en las descargas de
redacción (descargadas el 05-10-2026): `ub-cycle.txt` (Ubuntu release cycle), `ub-pkg.txt`
(Ubuntu Server, «Package management»), `fdisk.8.txt`, `ps.1.txt`. Nada nuevo descargado.

Alcance: sólo los pasajes cambiados que lista `29-T09-remate.md` (1-7), con atención a los que
amplían (2, 3, 4).

## Cotejo

| Pasaje | Dato | Fuente | Resultado |
|---|---|---|---|
| 1 Siglas | ESM, *Expanded Security Maintenance*; CVE sin desarrollar | ub-cycle «Expanded Security Maintenance (ESM)» | Correcto |
| 2 § 1 ESM/Pro | 5 años, CVE, *Main*; ESM 10 años *Main* y *Universe*, vía Pro; *Legacy* +5 = 15; Pro hasta 15; gratis uso personal 5 equipos | ub-cycle l. 711, 715, 719, 721, 727, 729, 737 | Citas literales; tabla 5/10/15 cuadra. Antecedente «La misma página» = página del ciclo citada antes en § 1: correcto |
| 3 § 8 MBR/GPT | GPT 64 bits, ilimitadas, 128 habitual, MBR protector, recomendación UEFI; MBR 4 primarias en sector 0, 1-4 y lógicas desde 5, 32 bits, 2 TB con 512 B | fdisk(8) l. 212-238 | Literales. **Salvedad omitida (error 6)**: la fuente dice que la tabla DOS **«can describe an unlimited number of partitions»** (las lógicas); sin ella, el tema invitaba a contestar «MBR: máximo 4 particiones». Añadida. «Una de ellas» sigue remitiendo a las 4 primarias |
| 4 § 9 categorías | Cuatro categorías; base/comunidad; abierto/no abierto; Universe y Multiverse activados; edición de `Components:` | ub-cycle l. 723; ub-pkg l. 738 | Literales. Tabla: «Contiene software no abierto» → «Contiene **algún** software no abierto» (fuente: *some*). «esa guía», «la misma guía» = «Package management»: correcto |
| 5 § 13 `ps` | formato `u`, 4.ª columna `pmem`, cabecera `%MEM`, definición | ps(1) l. 352-353, 677-679, 1038 | Correcto |
| 6 No da | NVMe/tarjetas, órdenes interactivas de `fdisk`, límite de tamaño GPT | fdisk(8) | Correcto: la página no da tamaño máximo GPT |
| 7 Trazabilidad | Filas ciclo, Package management, `ps`, discos | — | Fila del ciclo: «gratis en cinco equipos» → «gratis para uso personal en cinco equipos» (salvedad de la fuente) |

## Correcciones aplicadas (3)

1. § 8: salvedad de la tabla DOS con número ilimitado de particiones (cita literal de fdisk(8)).
2. § 9, tabla de categorías: «algún» software no abierto (dos filas).
3. Trazabilidad: «para uso personal» en la fila de Ubuntu Pro.

## Observación fuera de alcance

La cita previa al remate de «Package management» escribe «Ubuntu Pro's» con apóstrofo recto; la
fuente usa el tipográfico («Pro’s»). Mismo texto; no se toca.

## Otros ficheros tocados

Sólo el tema y este informe.
