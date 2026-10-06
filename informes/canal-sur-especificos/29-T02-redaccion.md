# Puesto 29 · Tema 2 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real del
sistema, como en la investigación). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/02-diagnostico-mantenimiento-y-reparacion-de-equipos-microinformaticos.md`.
Material: `29-investigacion-A-hardware.md` (§ Tema 2). `AGRUPACION.tsv`: «nuevo»; `informes/canal-sur-reuso/informatica.tsv`:
sin tema de RTVE (0 %).

## Fuentes releídas y fecha

Todas las citas de la investigación se releyeron en las copias de `fuentes/canal-sur/informatico/web/`
el 05-10-2026: `ami-amibios8-beep.txt`, `hp-beep-led-diagnostic.txt`, `smartctl-man.txt`,
`ms-chkdsk.txt`, `ms-devmgr-errors.txt`, `ms-devmgr-problem-codes.txt`, `ms-cm-prob-*.txt` (4),
`memtest86-troubleshooting.txt`, `memtest86-tests.txt`, `ucm-ec4-rendimiento.txt`, `spec-cpu2026.txt`,
`spec-cpu2017.txt`, `cinebench.txt`, `3dmark.txt`, `passmark-pt.txt`, `crystaldiskmark.txt`,
`ms-winsat.txt`.

Fuentes nuevas, descargadas y leídas el 05-10-2026 para cubrir huecos de la investigación (sustitución,
ESD, gráfica y red), guardadas en la misma carpeta:

| Fuente | Fichero | Qué cubre |
|---|---|---|
| Lenovo, *M920s User Guide and Hardware Maintenance Manual*, 2.ª ed., VIII-2019 | `lenovo-m920s-ughmm.pdf` / `.txt` | FRU/CRU, reglas antes de cambiar piezas, electricidad estática, sustitución de disco, memoria, PCIe, Wi-Fi, pila; mensaje de error por pila agotada |
| Microsoft Learn, «WDDM support for timeout detection and recovery» (05-11-2025) | `ms-tdr.txt` | TDR, 2 s, recuperación |
| Microsoft Learn, «ipconfig» (03-02-2023), «ping» (01-11-2024) | `ms-ipconfig.txt`, `ms-ping.txt` | Diagnóstico de la tarjeta de red |
| Microsoft Learn, «sfc» (01-11-2024) | `ms-sfc.txt` | Integridad de archivos del sistema |
| Microsoft Learn, «PnPUtil Command Syntax» (08-01-2024) | `ms-pnputil.txt` | Controladores por línea de órdenes |

Intentado sin éxito: Dell kbdoc 000124349 (la descarga devuelve una página vacía de 482 bytes). La
tabla de pitidos Dell de la investigación (sólo vía WebFetch) **no entra** en el tema; se declara.

Comprobación de literalidad por script: las 188 negritas «…» del tema se buscan en el texto
normalizado de las fuentes; las 188 aparecen (una se corrigió: la página de SPEC no lleva «®» tras
«SPEC CPU» en esa frase).

## Qué se hizo

Cinco rúbricas en el orden del enunciado: 1 diagnóstico, mantenimiento y reparación (método, ESD,
mantenimiento); 2 principales averías; 3 mensajes de error de la BIOS; 4 sustitución y detección en
discos, memorias, gráficas y tarjetas de red (más Administrador de dispositivos y PnPUtil); 5 pruebas
de rendimiento y sus tipos (con ejercicio). `indice.py`: 10.454 palabras, 33 epígrafes (índice
generado). `refutar_prosa.py`: 0 hallazgos (12 siglas sin presentar en la primera pasada, corregidas).
Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

Decisiones frente al material:

- AMI se da como ejemplo, no como norma, con su salvedad literal; se añade del historial de revisiones
  que los códigos 2, 4, 5, 9, 10 y 11 del POST fueron suprimidos (rev. 1.8, 2006).
- HP: sólo la estructura de familias; el significado de cada combinación es [SÓLO BUSCADOR] y no entra.
- Mensajes de texto de BIOS («CMOS checksum error», etc.): no entran como literal; el caso de la pila
  se cubre con Lenovo + AMI punto 04.
- SPEC: la fuente UCM desarrolla la sigla como «System Performance and Evaluation Cooperative»; la web
  de SPEC dice «Standard Performance Evaluation Corporation». Manda la web; el tema lo dice.
- UCM (2010-11) da SPEC2006 como vigente y TPC-C «en desuso» a la vez que lo usa de ejemplo: se dice
  así y se actualiza con SPEC CPU 2026/2017.
- Ejercicio MIPS/MFLOPS: cálculo propio, declarado. El de `time` es literal de UCM.
- Se descarta la clasificación FRU/CRU por pieza de la figura de Lenovo (el texto extraído no deja
  saber qué pieza va en qué columna).

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata diagnóstico o reparación de equipos.

## Copiado de RTVE sin cambios

Nada. `informatica.tsv` no asigna tema de RTVE a este punto («Diagnóstico y reparación de
microinformática, errores de BIOS y benchmark no están en los temas de RTVE»).

## Ficheros tocados

- Creado: el tema (ruta arriba) y este informe.
- Añadidos a `fuentes/canal-sur/informatico/web/`: `lenovo-m920s-ughmm.pdf`, `lenovo-m920s-ughmm.txt`,
  `ms-tdr.txt`, `ms-ipconfig.txt`, `ms-ping.txt`, `ms-sfc.txt`, `ms-pnputil.txt`.
- Ningún otro fichero modificado.

## Preguntas tipo test de control (10)

Repartidas por las rúbricas; todas contestadas enteras por el tema (epígrafe entre paréntesis).

1. (BIOS) En AMIBIOS8, 8 pitidos en el POST indican: a) error del temporizador de refresco de memoria;
   b) error de la memoria de vídeo; c) fallo del controlador de teclado; d) excepción del procesador.
   **b** (3, tabla de pitidos). — Entera.
2. (BIOS) Los puntos de control del POST de AMI se escriben en: a) el puerto 60h; b) el puerto 80h;
   c) la NVRAM; d) la CMOS. **b** (3, POST y puntos de control). — Entera.
3. (BIOS, aplicación) Un equipo arranca con la hora desfasada, la BIOS con valores de fábrica y un
   mensaje de error. Lo más probable: a) disco con sectores defectuosos; b) pila de la CMOS agotada;
   c) módulo de memoria mal asentado; d) controlador de vídeo dañado. **b** (3, mensajes en pantalla;
   AMI punto 04 y Lenovo). — Entera.
4. (Método) Según el manual de mantenimiento de Lenovo, ante un fallo aislado que no se reproduce:
   a) se cambia la FRU por precaución; b) se borra el registro de errores, se repite la prueba y sólo
   se cambia si vuelve; c) se actualiza la BIOS; d) se cambia la placa. **b** (1). — Entera.
5. (Discos) El parámetro de `chkdsk` que incluye `/r`, borra la lista de clústeres defectuosos y se
   recomienda tras volcar la imagen a un disco nuevo es: a) `/f`; b) `/x`; c) `/b`; d) `/scan`.
   **c** (4, chkdsk). — Entera.
6. (Discos, aplicación) Un atributo SMART de tipo *Pre-fail* tiene VALUE 100, WORST 98 y THRESH 36:
   a) fallo inminente; b) falló en el pasado; c) está bien y nunca ha fallado; d) hay que cambiar el
   disco. **c** (4, SMART: el tipo no indica fallo si el valor normalizado está por encima del umbral;
   WHEN_FAILED en guion). — Entera.
7. (Memorias) MemTest86 da errores sólo con todos los módulos puestos y no probándolos uno a uno. La
   causa probable según PassMark: a) CPU averiada; b) configuración multicanal con módulos no
   emparejados o incompatibles con la placa; c) disco dañado; d) prueba de martilleo. **b** (4,
   memorias: detectar). — Entera.
8. (Gráficas) El tiempo de espera por defecto del TDR de Windows antes de dar la GPU por bloqueada es:
   a) 0,5 s; b) 2 s; c) 5 s; d) 10 s. **b** (4, gráficas: detectar). — Entera.
9. (Red, aplicación) `ping` a la dirección IP de un servidor responde, pero `ping` a su nombre no. Según
   Microsoft: a) tarjeta de red averiada; b) cable RJ45 cortado; c) problema de resolución de nombres;
   d) controlador sin instalar (código 28). **c** (4, tarjetas de red: detectar). — Entera.
10. (Benchmark) Whetstone y Dhrystone son, según su naturaleza, patrones: a) reales; b) núcleos;
    c) reducidos; d) sintéticos. **d** (5, tipos). — Entera.

Ninguna laguna: no hizo falta ampliar el tema tras las preguntas.
