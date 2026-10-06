# Puesto 29 · Tema 2 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026. Quince preguntas tipo test de cuatro opciones (teoría y aplicación práctica),
contestadas **sólo con el tema**. Distintas de las diez de control del informe de redacción.
Veredicto: entera (el tema da la respuesta y descarta las demás), a medias (la da sin seguridad o
sólo por descarte), no (el tema no la da).

1. (BIOS) En AMIBIOS8, la BIOS escribe los puntos de control en: a) el puerto de E/S 60h; b) el
   puerto de E/S 80h; c) la CMOS; d) el registro de errores del POST. **b**. — **Entera** (ep. 3, «El
   POST y los puntos de control»).

2. (BIOS) Tres pitidos en el POST de AMIBIOS8 indican: a) error del temporizador de refresco de
   memoria; b) error de lectura/escritura de la memoria base; c) error de la memoria de vídeo;
   d) fallo del controlador de teclado. **b**. — **Entera** (ep. 3, tabla de pitidos).

3. (BIOS, aplicación) Un equipo con AMIBIOS8 da 6 pitidos. Antes de dar la placa por perdida, AMI
   indica: a) cambiar el procesador; b) quitar todas las tarjetas de expansión salvo la de vídeo;
   c) borrar la CMOS; d) regrabar la BIOS. **b**. — **Entera** (ep. 3, método de aislamiento).

4. (BIOS, aplicación) Al encender aparece «CMOS checksum error – Defaults loaded» y la fecha es
   incorrecta. La causa más probable y la reparación: a) disco dañado, `chkdsk /r`; b) pila de la
   CMOS agotada, cambiarla y reconfigurar; c) memoria mal asentada; d) BIOS corrupta, regrabarla.
   **b**. — **A medias**: el tema da el síntoma de la pila (Lenovo y punto 04 de AMI) y declara que
   no da el texto de los mensajes («CMOS checksum error»); se llega por el síntoma, no por el
   mensaje.

5. (Método) Según Lenovo, las CRU de autoservicio son, por ejemplo: a) la placa base y el
   procesador; b) el teclado, el ratón y cualquier dispositivo USB; c) la fuente de alimentación;
   d) los módulos de memoria. **b**. — **Entera** (ep. 1, tabla FRU/CRU).

6. (ESD) Antes de sacar una pieza de su bolsa antiestática, Lenovo indica tocar con la bolsa una
   superficie metálica sin pintar del equipo durante al menos: a) medio segundo; b) dos segundos;
   c) diez segundos; d) un minuto. **b**. — **Entera** (ep. 1, «La electricidad estática»).

7. (Discos, aplicación) `smartctl -A` muestra un atributo *Old_age* con VALUE 30, WORST 30 y THRESH
   30. Significa: a) fallo inminente del disco en 24 h; b) el atributo falla ahora y señala fin de
   vida útil por desgaste; c) falló en el pasado pero ya no; d) nada, porque sólo cuentan los
   *Pre-fail*. **b**. — **Entera** (ep. 4, SMART: valor ≤ umbral = fallo, FAILING_NOW; *Old age*,
   fin de vida por envejecimiento).

8. (Discos) `chkdsk` termina con el código de salida 3. Significa: a) no se encontraron errores;
   b) se encontraron y corrigieron; c) no se pudo comprobar o los errores no se corrigieron;
   d) se hizo limpieza del disco. **c**. — **Entera** (ep. 4, códigos de salida).

9. (Discos) En una unidad NVMe, el indicador del registro de salud que expresa el desgaste estimado
   de la unidad en porcentaje es: a) *Critical Warning*; b) *Percentage Used*; c) *Power Cycles*;
   d) *Temperature*. **b** (a confirmar en fuente en el remate). — **No**: el tema sólo da el byte
   *Critical Warning* para el estado de salud NVMe; nada del desgaste de las SSD.

10. (Memorias, aplicación) Windows 11 se cuelga a menudo y se sospecha de la RAM. La herramienta
    integrada en Windows que comprueba la memoria al reiniciar es: a) `winsat mem`; b) `sfc
    /scannow`; c) el Diagnóstico de memoria de Windows (`mdsched.exe`); d) `chkdsk /b`. **c**. —
    **A medias**: el tema descarta `winsat mem` («de rendimiento, no de errores»), `sfc` y `chkdsk`,
    y nombra `mdsched.exe` sólo en «Lo que este tema no da»; se acierta por descarte.

11. (Memorias) La técnica de PassMark de rotar módulos para localizar el averiado sólo puede usarse
    con: a) un módulo; b) dos módulos; c) tres o más módulos; d) memoria ECC. **c**. — **Entera**
    (ep. 4, «Memorias: localizar el módulo»).

12. (Red, aplicación) La tarjeta de red aparece en el Administrador de dispositivos con el código 22.
    Se resuelve: a) instalando el controlador del fabricante; b) habilitando el dispositivo;
    c) desinstalándolo y reinstalándolo; d) cambiando la tarjeta. **b**. — **Entera** (ep. 4,
    tabla de códigos).

13. (Averías, aplicación) Un equipo de sobremesa no da ninguna señal al pulsar el botón de
    encendido: ni ventiladores, ni LED, ni pitidos. Con el cable y la toma comprobados, la pieza
    sospechosa y la precaución que da el manual de mantenimiento: a) la memoria, cogerla por los
    bordes; b) la fuente de alimentación, sin abrir nunca su carcasa por las tensiones peligrosas;
    c) la gráfica, reasentarla; d) la pila, cambiarla. **b** (Lenovo: **«Never remove the cover on a
    power supply…»**). — **No**: el tema no trata la fuente de alimentación ni el equipo que no
    enciende.

14. (Averías) En Windows, la pantalla azul que detiene el sistema con un código de error se llama en
    la documentación de Microsoft: a) TDR; b) error de detención o comprobación de errores (*bug
    check*); c) código 43; d) POST. **b** (a confirmar en fuente en el remate). — **A medias**: el tema
    no trata la pantalla azul ni los volcados de memoria; se acierta sólo por descarte de a), c) y
    d), que sí explica.

15. (Benchmark, aplicación) Un programa ejecuta 900 millones de instrucciones en 3 segundos. Sus MIPS
    son: a) 30; b) 270; c) 300; d) 2.700. **c** (900 · 10⁶ / (3 · 10⁶)). — **Entera** (ep. 5,
    fórmula y ejercicio).

## Recuento

Enteras: 10 (1, 2, 3, 5, 6, 7, 8, 11, 12, 15). A medias: 3 (4, 10, 14). No: 2 (9, 13).
