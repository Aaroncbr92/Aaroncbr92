# Puesto 29 · Tema 2 · Revisión final (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/02-diagnostico-mantenimiento-y-reparacion-de-equipos-microinformaticos.md`.
Alcance: sólo los 14 pasajes que lista `29-T02-remate.md`. Cada dato se cotejó con el `.txt` guardado
en `fuentes/canal-sur/informatico/web/`, leído el 06-10-2026.

## Fuentes cotejadas (06-10-2026)

`hp-prodesk600g5-msg.txt` (3.ª ed., septiembre de 2019; cap. 6, «System does not power on», problemas de
alimentación; cap. 7, mensajes numerados del POST y códigos mayor/menor), `lenovo-m920s-ughmm.txt` (2.ª ed.,
agosto de 2019; pila y fuente), `ms-bugchecks.txt`, `ms-bugcheck-codes.txt`, `ms-stop-error-advanced.txt`,
`ms-stop-error-support.txt`, `ms-mdsched-technet.txt`, `nvme-base-2.1.txt` (§ 5.1.12.1.3, fig. 206),
`smartctl-man.txt` (`-l ssd`), `ms-cm-prob-failed-install.txt`, `spec-cpu2026.txt` (nota de prensa),
`gnu-gzip.txt` (CRC).

## Resultado por pasaje

| # | Pasaje | Resultado |
|---|---|---|
| 1 | Portada | Correcto (ediciones y fechas cuadran) |
| 2 | Siglas | Correcto. Nota: Microsoft escribe «256 kb»; el tema pone «256 kB» en redonda; el sentido (kilobytes) es el de Microsoft; se deja |
| 3 | Qué se puede preguntar | Correcto |
| 4 | Tabla «Dónde se manifiesta» | Correcto (oficio declarado) |
| 5 | El equipo no enciende | Correcto: los pasos de HP, las citas literales, la protección térmica y la advertencia, el procedimiento y las potencias de Lenovo cuadran con la fuente. «La misma guía» tiene su antecedente (HP) |
| 6 | Pantalla azul | Correcto: definición, nombres, código y módulo, los 7 valores/nombres, 70/10/5/15 %, pasos básicos, tabla por escenarios, configuración del volcado, tabla de ubicaciones, DumpChk, `!analyze -v` |
| 7 | Pitidos de HP 600 G5 | Correcto: reglas, 2.2-5.5 y la estructura mayor/menor cuadran |
| 8 | Mensajes en pantalla | **Corregido**: el procedimiento de la pila decía «el inicio común de todas las sustituciones»; en Lenovo, la sustitución de la fuente no empieza así (paso 1, quitar la tapa) y «sacar los soportes de las unidades» se prestaba a leerse como soportes mecánicos. Reescrito siguiendo los pasos 1-6 del manual. Tabla HP (002, 005, 2E1, 2E2, 301, 3F0, 800, 900, 90D): correcta |
| 9 | NVMe y `-l ssd` | **Corregido** (3): *Critical Warning* listaba los bits 0-3 como si fueran todos (la fig. 206 tiene también 4 y 5): añadido «entre ellos». *Composite Temperature*: la fuente dice temperatura compuesta del controlador y sus espacios de nombres, de cálculo propio de la implementación y que puede no ser la de ningún punto físico; el tema decía «la temperatura del controlador»: corregido, con bytes 1-2. *Percentage Used*: añadida la salvedad «cuando el controlador no está en reposo» de la actualización horaria. Resto correcto, `-l ssd` incluido |
| 10 | Diagnóstico de memoria de Windows | Correcto (Learn vigente y TechNet archivado, con su salvedad) |
| 11 | Fila 28 | **Corregido**: «el caso más citado» no consta en la fuente, que sólo enumera los cuatro estados; pasa a decir «El primer caso que da la página». Resto correcto |
| 12 | SPEC CPU hoy | Correcto (título y fecha de la nota, literal) |
| 13 | Lo que este tema no da | Correcto |
| 14 | Trazabilidad | Correcto; CRC confirmada en gzip |

Antecedentes: «la misma guía», «el manual», «epígrafe 4», «los dos de vídeo» tienen su referente delante.
Tras los cambios: `refutar_prosa.py`, 0 hallazgos. El índice no cambia (no se tocaron rótulos).

## Otros ficheros tocados

Ninguno, aparte del tema y de este informe.
