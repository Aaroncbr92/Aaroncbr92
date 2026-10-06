# Puesto 29 · Tema 2 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). No corrijo: el tema queda como estaba.
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/02-diagnostico-mantenimiento-y-reparacion-de-equipos-microinformaticos.md`
(911 líneas, 10.693 palabras de cuerpo).

## Alcance

- «Copiado del común»: nada. «Copiado de RTVE sin cambios»: nada (`29-T02-redaccion.md`). Se mira
  todo el tema en las dos lentes.
- Fuentes: los volcados de la redacción en `fuentes/canal-sur/informatico/web/` (descargados el
  05-10-2026), releídos el **06-10-2026** sobre los pasajes concretos: `ami-amibios8-beep.txt`,
  `hp-beep-led-diagnostic.txt`, `lenovo-m920s-ughmm.txt`, `smartctl-man.txt`, `ms-chkdsk.txt`,
  `ms-sfc.txt`, `ms-devmgr-errors.txt`, `ms-devmgr-problem-codes.txt`, `ms-cm-prob-*.txt` (4),
  `ms-pnputil.txt`, `ms-tdr.txt`, `ms-ipconfig.txt`, `ms-ping.txt`, `memtest86-tests.txt`,
  `memtest86-troubleshooting.txt`, `ucm-ec4-rendimiento.txt`, `spec-cpu2026.txt`, `spec-cpu2017.txt`,
  `cinebench.txt`, `3dmark.txt`, `passmark-pt.txt`, `crystaldiskmark.txt`, `ms-winsat.txt`. Nada
  descargado de nuevo.
- Lentes (tema técnico sin norma): `refutar_prosa.py` 0 hallazgos; `indice.py` sobre una copia en el
  scratchpad: 33 epígrafes, índice idéntico al del tema. No proceden `negritas.py`,
  `refutar_exactitud.py` ni `refutar_modo.py`.

## Lente 1 · Exactitud

Comprobado contra la fuente y correcto (sobre todo la redonda): AMI (alcance «before May 2002» y
Core 8.00.04; puerto 80h; tarjetas ISA o PCI; esquina inferior derecha y «not all computers»; D2;
puntos 04, 2C, 3B, 84, 85, 87 y 00; pitidos 1/3/6/7/8 y sus acciones; método de aislamiento;
revisiones 1.8 de 17-05-2006 y 1.9 de 11-10-2007; pitidos del bloque de arranque 4, 7, 10, 11, 13);
HP (cuatro familias y combinaciones 2L 2-4C, 3L 2-6C, 4L 2-3C, 5L 2-5C); Lenovo (FRU/CRU y ejemplos
de autoservicio, seis reglas, inicio común y «very hot» en disipador y procesador, bolsa sin abrir,
dos segundos, «reduces static electricity from the package and your body», superficie lisa y plana;
disco de 3,5″ con *pivot outward*, conversor de 2,5″, M.2 aparte; orden de los módulos; pestaña de
retención; Wi-Fi con *shield* y antenas, tipos 1 y 2; pila: «normally», mensaje de error, aviso de
pilas de litio); smartctl (24 h, 1-253, 1-254, 0-255, *Critical Warning*, cada cuatro horas,
duraciones, *conveyance* sólo ATA, 7.4 experimental); chkdsk (aplicabilidad, «If used with the /f,
/r, /x, or /b parameters, it fixes errors», cabezal, interrupción, `File<nnnn>.chk`, HDD/SSD,
códigos 0-3, Chkdsk y Wininit); sfc; códigos 1, 10, 12, 14, 18, 22, 28, 31, 43 y lista del 1 al 57;
PnPUtil (Vista, 1903, 2004); TDR (2 s, reinicio, parpadeo, mensaje, aplicaciones en negro); ipconfig
(APIPA y configuración alternativa); ping (4, 32 bytes, 4000 ms); MemTest86 (pruebas 0-14, 4 MB,
v6.2 y dos pasadas, ECC «probably», tres técnicas, seis remedios en su orden, tensión «at your own
risk»); UCM (técnicas, *benchmark*, tiempos, MIPS, pesos 1/4/8, «no excluyentes», ejemplos,
TPC «ya están en desuso», SPEC2006 «la última en vigor»); SPEC (52 y 43 pruebas, retirada 03-11 y
17-11-2026, *real user applications*, código fuente, energía); Cinebench, 3DMark, PerformanceTest,
BurnInTest, CrystalDiskMark y `winsat mem`. Rehechos los cálculos de `time` y MIPS/MFLOPS: cuadran.

### Hallazgos

| # | Gravedad | Error | Pasaje | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|
| M1 | Menor | 1 cita cruzada | Ep. 3, «Los mensajes en pantalla»: «La reparación es cambiar la pila (epígrafe 4, Lenovo)» | El epígrafe 4 no tiene procedimiento de cambio de la pila: trata discos, memorias, gráficas y tarjetas de red. El manual de Lenovo sí lo trae («Replacing the coin-cell battery», pasos 1-5 con el inicio común) | Quitar «(epígrafe 4, Lenovo)» y poner «(procedimiento propio en el manual de Lenovo)», o bien añadir dos líneas del procedimiento en el ep. 3 |
| M2 | Menor | 9 afirmación contraria a la fuente | Ep. 5, «SPEC CPU hoy»: «La fecha exacta de publicación de SPEC CPU 2026 no figura en el texto leído.» | La misma página leída, en «Benchmark Press Releases»: **«SPEC Releases the SPEC CPU 2026 Benchmark Suites to Address the Latest Advances in CPU, Memory, and Compiler Technology (05/05/2026)»** | Sustituir por: «SPEC anunció su publicación en nota de prensa de 05-05-2026» (la fecha de la nota, que es lo que consta) |
| M3 | Menor | 6 salvedad omitida | Ep. 4, tabla de códigos, fila 28: «Falta un controlador compatible: «This failure is often referred to as a DNF (driver not found) problem.»» | En la página del código 28, el DNF corresponde sólo al estado 0xC0000490 (**«PnP could not find a compatible driver for the device»**); la página da otros tres estados (0xC0000491, 0xC0000492, 0xC0000494) por dependencias del paquete de controlador que faltan o INF sin servicio asociado | Añadir «en su causa más común» o «uno de los casos, el más citado», y una frase: los demás casos son dependencias del paquete de controlador que faltan |

Sin hallazgo en: ley por reglamento (2), recuentos (3: «tres límites», «tres técnicas», «cuatro
familias», «seis remedios», 52/43 pruebas cuadran), «podrá»/«deberá» (4: «normally», «probably»,
«may» bien llevados), siglas (5; 0 en `refutar_prosa.py`), redacción derogada (7: AMI 2008 y UCM
2010-11 se dan con su fecha y su vigencia), artículo mal (8).

## Lente 2 · Cobertura

Las cinco rúbricas del enunciado tienen epígrafe propio y en su orden. Quince preguntas en
`29-T02-preguntas.md`: **10 enteras, 3 a medias (4, 10, 14), 2 no (9, 13)**.

| # | Laguna | Rúbrica | Propuesta |
|---|---|---|---|
| L1 | Fuente de alimentación y equipo que no enciende (sin LED, sin ventiladores, sin pitidos): es la avería más básica y el tema no la nombra (pregunta 13) | Principales averías; sustitución | El manual de Lenovo ya descargado trae «Replacing the power supply assembly» y la advertencia **«Never remove the cover on a power supply or any part that has the following label attached.»** (tensiones peligrosas, sin piezas reparables); fila nueva en la tabla del ep. 2 y párrafo breve |
| L2 | Pantalla azul de Windows (error de detención, *bug check*), su código y los volcados de memoria: avería típica del puesto, ligada a memoria y controladores (pregunta 14) | Principales averías | Leer en Microsoft Learn la página de solución de errores de pantalla azul y la de opciones de volcado; fila en la tabla del ep. 2 y párrafo en «Hardware o software» |
| L3 | Diagnóstico de memoria de Windows (`mdsched.exe`): declarado en «Lo que este tema no da», pero es la prueba de memoria que trae Windows y la más preguntable en test (pregunta 10) | Memorias: detectar | Buscar de nuevo la página vigente de Microsoft (soporte o Learn) y añadir dos líneas en «Memorias: detectar»; si no se encuentra, dejarlo declarado |
| L4 | Desgaste de las SSD y salud NVMe más allá del byte *Critical Warning* (porcentaje usado, reserva disponible); y la detección en SSD en general (pregunta 9) | Discos duros: detectar | El manual de `smartctl` sólo da el porcentaje de resistencia en SCSI; leer la especificación NVMe o la documentación del fabricante (o `smartctl -x` de un NVMe en smartmontools wiki) y añadir una tabla corta |
| L5 | Textos de los mensajes de error de la BIOS («CMOS checksum error», «No boot device», «CPU fan error»): la rúbrica dice «mensajes de error de la BIOS» y el tema sólo da pitidos y el caso de la pila (pregunta 4) | Mensajes de error de la BIOS | Buscar una lista publicada por un fabricante (manual de mantenimiento con «POST error messages»: Lenovo de otro modelo, Dell, HP «POST error messages») y dar tres o cuatro con su causa |

## Recuento

Graves: 0. Menores: 3 (M1-M3). Lagunas: 5 (L1-L5).

## Otros ficheros tocados

Ninguno, salvo este informe y `29-T02-preguntas.md`. Copia del tema para `indice.py`, en el
scratchpad de la sesión (fuera del proyecto).
