# Puesto 29 · Tema 2 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/02-diagnostico-mantenimiento-y-reparacion-de-equipos-microinformaticos.md`.
Entrada: `29-T02-refutacion.md` (0 graves, 3 menores, 5 lagunas) y `29-T02-preguntas.md` (10 enteras,
3 a medias, 2 no). **Se amplió el tema** con contenido nuevo: hace falta la fase 5 bis sobre los pasajes
listados abajo. Extensión: de unas 10.700 a 13.914 palabras de cuerpo.

## Fuentes nuevas, leídas el 06-10-2026

Guardadas en `fuentes/canal-sur/informatico/web/`:

| Fichero | Fuente | Para qué |
|---|---|---|
| `hp-prodesk600g5-msg.pdf/.txt` | HP, *Maintenance and Service Guide HP ProDesk 600 G5 SFF*, 3.ª ed., IX-2019, h10032.www1.hp.com/ctg/Manual/c06442415.pdf (cap. 6 y 7) | Equipo que no enciende, fuente que no arranca, protección térmica; códigos mayor/menor de pitidos y parpadeos; mensajes numerados del POST |
| `ms-bugchecks.txt` | Microsoft Learn, «Bug checks (stop code errors)», ms.date 23-07-2025 | Definición, tabla de escenarios (memoria, `sfc`, BIOS, tarjetas asentadas), Diagnóstico de memoria y evento MemoryDiagnostics-Results |
| `ms-bugcheck-codes.txt` | Microsoft Learn, «Bug check code reference», 15-07-2025 | Valores y nombres de los siete códigos citados |
| `ms-stop-error-advanced.txt` | Microsoft Learn, «Advanced troubleshooting for stop code errors», 12-02-2026 | Causas en porcentaje, volcados (configuración y ubicación), DumpChk, WinDbg `!analyze -v` |
| `ms-stop-error-support.txt` | Microsoft Support, «Troubleshooting Windows unexpected restarts and stop code errors», 28-07-2026 | Nombres (BSOD), mensaje, código y módulo, pasos básicos, diseño según 24H2/23H2 |
| `ms-mdsched-technet.txt` | Microsoft, TechNet Magazine, «Run Diagnostics to Check Your System for Memory Problems», learn.microsoft.com/en-us/previous-versions/technet-magazine/ff700221(v=msdn.10) (archivado, Windows 7; ms.date 31-08-2016) | `mdsched.exe`, reinicio, mezclas Basic/Standard/Extended, F1/F10 |
| `nvme-base-2.1.txt` (sólo el texto; el PDF, 11 MB, no se guarda) | NVM Express, *NVM Express Base Specification*, rev. 2.1, 05-08-2024, nvmexpress.org/wp-content/uploads/NVM-Express-Base-Specification-Revision-2.1-2024.08.05-Ratified.pdf, § 5.1.12.1.3, fig. 206 | Página de salud NVMe 02h |

Releídas el 06-10-2026 de las ya guardadas: `lenovo-m920s-ughmm.txt` (pila y fuente), `spec-cpu2026.txt`
(nota de prensa), `ms-cm-prob-failed-install.txt` (código 28), `smartctl-man.txt` (`-l ssd`),
`gnu-gzip.txt` (desarrollo de CRC). Comprobación por script: las 239 negritas «…» del tema se buscan en el
texto normalizado de las fuentes; todas las nuevas aparecen. Las 3 que el script no casa son anteriores
(manual de `smartctl`, con marcas troff entre palabras) y ya las dio por buenas la refutación.

Nota sobre la versión NVMe: la web de NVM Express anuncia la familia 2.4; se leyó la 2.1 por ser el PDF
localizable. Los campos usados no dependen de la revisión, pero la cita es a la 2.1 y así consta.

## Correcciones de la refutación (las tres, comprobadas en fuente y aplicadas)

| # | Comprobación | Qué se hizo |
|---|---|---|
| M1 | Confirmado: el ep. 4 no trae el cambio de pila; Lenovo lo trae («Replacing the coin-cell battery», pasos 1-6) | Quitada la remisión «(epígrafe 4, Lenovo)»; añadido el procedimiento en el ep. 3 |
| M2 | Confirmado: la página dice «… Compiler Technology (05/05/2026)» | Sustituida la frase de «no figura» por la nota de prensa de 05-05-2026, literal |
| M3 | Confirmado: DNF es sólo el estado 0xC0000490; hay otros tres (0xC0000491, 0xC0000492, 0xC0000494) | Fila 28: «el caso más citado» + literal completo + los otros tres casos en redonda |

## Lagunas cubiertas (se amplía el tema; ninguna pregunta se recorta)

| Pregunta | Laguna | Dónde se cubre |
|---|---|---|
| 13 (No) | Equipo que no enciende; fuente de alimentación | Ep. 2, nuevo «El equipo no enciende» (HP 600 G5 + Lenovo: advertencia y sustitución) |
| 14 (A medias) | Pantalla azul y volcados | Ep. 2, nuevo «La pantalla azul (error de detención)» |
| 10 (A medias) | `mdsched.exe` | Ep. 4, «Memorias: detectar», párrafo nuevo (vigente: Microsoft Learn; detalle: TechNet archivado, con su salvedad) |
| 9 (No) | Desgaste y salud NVMe | Ep. 4, «Discos duros: detectar con SMART», tabla nueva de la página 02h |
| 4 (A medias) | Textos de mensajes de la BIOS | Ep. 3, «Los mensajes en pantalla», tabla HP (002, 005, 2E1, 2E2, 301, 3F0, 800, 900, 90D) |

Con lo añadido, las 15 preguntas se contestan con el tema. Salvedad en la 4: el texto «CMOS checksum error
– Defaults loaded» del enunciado de la pregunta no está en ninguna fuente leída; se contesta por el
síntoma (pila, punto 04 de AMI y mensaje 005 de HP). La pregunta se deja como está.

## Pasajes cambiados (para la fase 5 bis)

1. Portada: «Fuente» (HP 600 G5, Microsoft Support, errores de detención, TechNet archivado, NVMe 2.1),
   «Redacción que se estudia» (05 o 06-10-2026), «Extensión» (13.900).
2. Siglas: kB, AC, CRC, pantalla azul/BSOD/*bug check*; DXE, MXM y 5V_aux como nombres de HP sin
   desarrollar; NVM Express; «BAT … fuente de American Megatrends» (antes «de AMI», para que la sigla no
   aparezca antes de presentarse).
3. «Qué se puede preguntar»: códigos y mensajes de HP; equipo que no enciende; pantalla azul y volcado;
   NVMe; Diagnóstico de memoria de Windows.
4. Ep. 2, tabla «Dónde se manifiesta la avería»: dos filas nuevas (no enciende; pantalla azul).
5. Ep. 2, nuevo «El equipo no enciende».
6. Ep. 2, nuevo «La pantalla azul (error de detención)».
7. Ep. 3, «Los pitidos de otros fabricantes»: sustituido el párrafo final por los códigos de HP 600 G5
   (reglas y tabla 2.2-5.5) y la advertencia de que no valen para otro modelo.
8. Ep. 3, «Los mensajes en pantalla»: reparación de la pila con el procedimiento de Lenovo (M1);
   sustituido el párrafo final por la tabla de mensajes numerados de HP.
9. Ep. 4, «Discos duros: detectar con SMART»: bloque «Salud y desgaste de una SSD NVMe» con tabla y
   salvedad del *Percentage Used*; `smartctl -l ssd`.
10. Ep. 4, «Memorias: detectar»: párrafo del Diagnóstico de memoria de Windows.
11. Ep. 4, tabla del Administrador de dispositivos, fila 28 (M3).
12. Ep. 5, «SPEC CPU hoy», último inciso (M2).
13. «Lo que este tema no da»: reescritos «Códigos de otros fabricantes», «Textos de los mensajes» y
    «Diagnóstico de memoria»; nuevo «Análisis de volcados».
14. «Trazabilidad»: filas nuevas (HP 600 G5, errores de detención, TechNet, NVMe); ampliadas Lenovo,
    Microsoft códigos, smartctl y SPEC con la fecha de relectura; frase sobre CRC (gzip).

Releídos los pasajes cambiados: cada «epígrafe 4», «la misma guía», «el manual» tiene su antecedente
delante.

## Lentes

Tema técnico sin norma: `refutar_prosa.py` 0 hallazgos (tras presentar AC y quitar AMI y GNU antes de
su presentación); `indice.py`: 35 epígrafes, índice regenerado (el tema no está en `portadas.tsv`; la
portada se mantiene a mano). No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Otros ficheros tocados

Las siete fuentes nuevas de la tabla de arriba, en `fuentes/canal-sur/informatico/web/`. Ningún otro
tema.
