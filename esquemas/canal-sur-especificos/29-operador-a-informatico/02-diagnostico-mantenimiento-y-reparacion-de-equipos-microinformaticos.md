# Tema 2 del específico de Operador/a Informático · Diagnóstico, mantenimiento y reparación de equipos microinformáticos

**Siglas**: BIOS, UEFI, POST, CMOS, RTC, ECC, DMA, XMP, SSD, NVMe, SMART, LBA, NIC, DHCP, DNS, ICMP, APIPA, TDR, FRU, CRU, MIPS, MFLOPS, SPEC, TPC, IOPS.

Esqueleto para repasar, no resumen: ante la duda, el tema.

<!-- indice -->

## Índice

- [1. Cómo se trabaja](#1-cómo-se-trabaja)
- [2. Principales averías](#2-principales-averías)
- [3. Mensajes de error de la BIOS](#3-mensajes-de-error-de-la-bios)
- [4. Discos, memorias, gráficas y tarjetas de red](#4-discos-memorias-gráficas-y-tarjetas-de-red)
- [5. Benchmark y sus tipos](#5-benchmark-y-sus-tipos)

<!-- /indice -->

## 1. Cómo se trabaja

- Lenovo M920s (2.ª ed., 08-2019): manda el manual del equipo. FRU = la cambia técnico formado, incluye las CRU; CRU = la cambia el usuario.
- Lenovo: sólo personal certificado; leer la sección; cuidado al formatear (orden de unidades); FRU del modelo correcto, sólo la defectuosa.
- Lenovo: fallo único no reproducible no justifica cambio (radiación cósmica, ESD, software); borrar registro, repetir prueba; si no recurre, no cambiar.
- Estática (Lenovo): limitar movimiento; piezas por los bordes; bolsa contra metal sin pintar ≥2 s; no abrir bolsa antes de tiempo; no dejarla sobre metal. Pulsera: oficio.
- Mantenimiento: `chkdsk` ocasional (en SSD, `/r` repetido gasta ciclos); `smartctl --smart=on --offlineauto=on --saveauto=on /dev/sda` (offline cada cuatro horas); `sfc /scannow` repara, `/verifyonly` comprueba, Administradores. Polvo, pasta térmica, calendario: oficio.

## 2. Principales averías

- Ordenación por momento = oficio. AMI: pitidos = antes de inicializar el vídeo; mensaje = después.
- Hardware o software: Microsoft, `chkdsk` rápido en disco grande = volumen bloqueado, sectores sin leer o «failing read head».
- HP ProDesk 600 G5 SFF (3.ª ed., 09-2019) «System does not power on…»: pulsar <4 s. Si luce el piloto del disco: selector de tensión, quitar tarjetas una a una hasta que se encienda 5V_aux, si no placa.
- Si nada luce: toma; cable del botón; cables de fuente a placa; 5V_aux encendido = cambiar botón; apagado = cambiar fuente; último, placa.
- Apagado solo con piloto parpadeando (HP): protección térmica; ventilador parado o disipador mal asentado.
- Fuente: se cambia entera, nunca se abre (Lenovo, tensión peligrosa). M920s: 180, 210, 260 W, «automatic voltage-sensing».
- Pantalla azul (Microsoft): bug check = system crash, kernel error, stop error, BSOD; reinicio automático; «Your device ran into a problem and needs to restart.»; se lee código de detención y módulo.
- Códigos: 0x1A MEMORY_MANAGEMENT; 0x50 PAGE_FAULT_IN_NONPAGED_AREA; 0x7B INACCESSIBLE_BOOT_DEVICE; 0xD1 DRIVER_IRQL_NOT_LESS_OR_EQUAL; 0x116 VIDEO_TDR_FAILURE; 0x117 VIDEO_TDR_TIMEOUT_DETECTED; 0x124 WHEA_UNCORRECTABLE_ERROR.
- Causas: 70 % controladores de terceros; 10 % hardware; 5 % Microsoft; 15 % desconocida.
- Pasos: reinicio aislado, nada más; si repite: quitar hardware nuevo, modo seguro, Administrador de dispositivos (actualizar, deshabilitar, desinstalar), 10-15 % libre, actualizaciones, punto de restauración.
- Por escenario: memoria, Diagnóstico de memoria; ficheros del sistema, `sfc /scannow`; sistema de ficheros, comprobar disco; BIOS antigua, versión nueva; tarjetas y cables bien asentados.
- Volcado: Inicio y recuperación, «Write debugging information», «Automatic memory dump», reiniciar. Pequeño (256 kB) `%SystemRoot%\Minidump`; núcleo, completo, automático o activo `%SystemRoot%\MEMORY.DMP`. DumpChk comprueba; WinDbg `!analyze -v`.

## 3. Mensajes de error de la BIOS

- AMI, *AMIBIOS8 Check Point and Beep Code List* v2.0 (10-06-2008): checkpoint = byte o palabra al puerto de E/S 80h, en bootblock y POST. Se lee con tarjeta POST (ISA o PCI, LED).
- Puntos: 04 pila y suma CMOS; suma mala = valores por defecto y borra contraseñas · 2C vídeo · 3B memoria total · 84 registra errores · 85 los muestra y pide respuesta · 87 setup, contraseña de arranque · 00 cargador (INT19h).
- Límites AMI: productos anteriores a mayo de 2002 (núcleo 8.00.04); núcleo genérico, sin códigos de chipset o placa; varía por plataforma. AMI es ejemplo, no norma.
- Pitidos AMI: altavoz de placa, error grave antes del vídeo. 1 «Memory refresh timer error»; 3 «Base memory read/write test error»: reasentar memoria o módulos buenos. 6 «Keyboard controller BAT command failed»; 7 «General exception error»: fatal, consultar fabricante, antes aislar tarjetas. 8 «Display memory error»: tarjeta, reasentar o cambiar; integrada, placa.
- v1.8 (17-05-2006) retiró POST 2, 4, 5, 9, 10, 11 y bootblock 8, 9; v1.9 corrigió 6 pitidos.
- Aislamiento (6 y 7): quitar tarjetas salvo vídeo; si pita, soporte del fabricante; si no, reponer una a una.
- Bootblock: 4 «Flash Programming successful»; 7 «No Flash EPROM detected»; 10 «Flash Erase error»; 11 «Flash Program error»; 13 «BIOS ROM image mismatch».
- HP *Interactive Beep and LED Diagnostic* (Desktop Pro A G2/G3): familia = pitidos largos. BIOS 2 largos + 2, 3 o 4 cortos; Hardware 3 + 2 a 6; Thermal 4 + 2 o 3; System Board 5 + 2 a 5.
- HP ProDesk 600 G5: mayor (largos, rojo) = categoría; menor (cortos, blanco) = error; «3.5» = 3 rojos + 5 blancos. Sin códigos de un pitido; pitidos sólo 5 iteraciones, parpadeo hasta desenchufar o pulsar.
- Códigos HP: 2.2 DXE dañada sin recuperación · 2.3 pide teclas · 2.4 recupera bootblock · 3.2 memoria, tiempo agotado · 3.3 gráfica, tiempo agotado · 3.4 fallo de alimentación (*crowbar*) · 3.5 procesador no detectado · 3.6 función no admitida · 4.2 sobretemperatura de procesador · 4.3 temperatura ambiente · 4.4 módulo MXM · 5.2 sin firmware válido · 5.3 y 5.4 tiempo agotado · 5.5 reinicio por bloqueo. Desktop Pro A: térmica hasta 4 + 3; códigos no valen entre modelos.
- Pila CMOS (Lenovo): guarda fecha, hora, configuración; al fallar se pierden (con contraseñas) y sale mensaje. Cambiar pila y reconfigurar.
- Mensajes HP (pitido tras mostrarlos): 002-Option ROM Checksum Error (regrabar ROM, quitar tarjeta nueva, borrar CMOS, placa) · 005-Real-Time Clock Power Loss (fecha y hora; si repite, pila) · 2E1-MemorySize Error (F1; revisar módulos) · 2E2-Memory Error (cambiar módulo, placa).
- 301-Hard Disk 1: SMART Hard Drive Detects Imminent Failure (F2, parche de firmware; «Back up contents and replace hard drive.») · 3F0–Boot Device Not Found · 800-Keyboard Error (reconectar apagado, cambiar) · 900-CPU Fan Not Detected (reasentar, cambiar) · 90D-System Temperature («Make sure system has proper airflow.»).
- Textos «CMOS checksum error», «No boot device»; Dell, Award, Phoenix, UEFI: no leídos.

## 4. Discos, memorias, gráficas y tarjetas de red

- smartctl(8): SMART en ATA/SATA y SCSI/SAS, HDD y SSD; vigila, predice, autopruebas. `-H` fallo = ya falló o fallará en 24 h: sacar datos. NVMe: *Critical Warning*.
- `-A`: atributos 1 a 253 (12 «power cycle count»). RAW_VALUE bruto; VALUE normalizado 1-254; WORST peor; THRESH 0-255; TYPE *Pre-fail* o *Old_age*; WHEN_FAILED.
- Normalizado ≤ umbral = fallido; *Pre-fail* fallido = fallo inminente; *Pre-fail* sin pasar umbral no implica fallo; *Old_age* = desgaste. WHEN_FAILED: FAILING_NOW; In_the_past (sólo el peor); guion.
- NVMe (Base Spec 2.1, 05-08-2024, Log Page 02h): *Critical Warning* byte 0: bit 0 reserva baja; bit 1 temperatura; bit 2 fiabilidad degradada; bit 3 sólo lectura. *Available Spare* byte 3 (0-100 %); *Threshold* byte 4; *Percentage Used* byte 5; *Composite Temperature* bytes 1-2 (kelvin); *Power Cycles*, *Power On Hours*, *Unexpected Power Losses*; *Media and Data Integrity Errors*.
- *Percentage Used* 100 = resistencia consumida, no fallo; puede superar 100 (>254 = 255); se actualiza cada hora de funcionamiento. `-l ssd`: SCSI 0 nueva, 100 fin de vida, hasta 255.
- Autopruebas `-t`: `short` <10 min; `long` decenas de minutos a horas; `conveyance` sólo ATA, transporte; `select,N-M` sólo ATA, LBA (hasta cinco). Con el sistema en uso; `-l selftest`. NVMe: experimental desde 7.4.
- `chkdsk` (Windows 10, 11, Server 2016-2025): sin parámetros sólo informa. `/f` corrige, disco bloqueado · `/r` sectores y recupera, incluye `/f` · `/x` desmonta, incluye `/f` · `/b` sólo NTFS, borra clústeres defectuosos, incluye `/r`, tras imagen a disco nuevo · `/scan`, `/spotfix` sólo NTFS.
- chkdsk: Administradores locales; discos locales; volumen en uso = programar al reiniciar (Y/N); FAT `File<nnnn>.chk`. Salida: 0 sin errores; 1 corregidos; 2 limpieza o no hecha sin `/f`; 3 no comprobado o no corregido. Registro: Visor de eventos, Aplicación, Chkdsk y Wininit.
- Disco, cambio (Lenovo 3,5"): desconectar cable de señal y de corriente; 2,5" en adaptador; M.2 aparte. Copia y recuperación: tema 3.
- Memoria, señales: 1 o 3 pitidos AMI; MemTest86 (PassMark); intermitentes válidos sin excepción.
- Windows: Diagnóstico de memoria (Panel de control, «Diagnose your computer's memory problems»); resultado en Visor de eventos, Sistema, MemoryDiagnostics-Results. `mdsched.exe` (TechNet, Windows 7): F1 «Basic, Standard, or Extended», F10.
- MemTest86: 0-2 direcciones (0 «walking ones»); 3-5 y 7 inversiones móviles; 6 bloques de 4 MB; 10 desvanecimiento de bits; 13 martilleo (*row hammer*, filas distintas del mismo banco; desde 6.2 dos pasadas); 14 DMA.
- Interpretar: no todo error es de memoria (CPU, cachés L1 y L2, placa); incompatibilidad; sólo con todos los módulos = multicanal, módulos idénticos, lista de compatibles.
- Localizar (PassMark): quitar módulos; rotar (tres o más, intercambiar dos); sustituir. Remedios: «Replace the RAM modules (most common solution)»; tiempos por defecto, sin XMP; más tensión RAM (riesgo); menos CPU; «Apply BIOS update»; marcar zonas defectuosas.
- Módulo (Lenovo): orden de la figura. `winsat mem` = rendimiento, no errores.
- Gráfica: 8 pitidos (2C); TDR, 2 segundos, reinicia pila gráfica, parpadeo, «Display driver stopped responding and has recovered.» (Visor de eventos); aviso aislado no es avería (tema); código 43; estrés UL: cuelgue o defectos visuales = fiabilidad, apagado = refrigeración.
- Gráfica, cambio (Lenovo): ranura «PCI Express x16», pestaña de retención, instalar controlador. Aislar: método AMI.
- NIC (Ethernet, PCIe o Wi-Fi M.2): Administrador de dispositivos (22 deshabilitada, 28 sin controlador, 10 no arranca, 43 fallo); `ipconfig`; `ping`.
- `ipconfig`: sin parámetros IPv4 e IPv6, máscara, puerta; `/all`; `/release`, `/renew`; `/flushdns`. `ping` (ICMP echo): 4 peticiones (`/n`) de 32 bytes (`/l`), 4.000 ms (`/w`); «Request timed out»; `/t`; IP sí, nombre no = resolución de nombres.
- NIC, cambio: PCIe como gráfica; Wi-Fi M.2 con *Wi-Fi card shield* y antenas. RJ45: temas 4 y 13.
- Códigos (`Cfg.h`, `CM_PROB_*`): 10 FAILED_START «This device cannot start.», Update Driver · 22 DISABLED, Enable Device · 28 FAILED_INSTALL «The drivers for this device are not installed.», driver del fabricante; DNF = sin controlador compatible; otros tres casos (dependencias, `.inf`) · 43 FAILED_POST_START «Windows has stopped this device because it has reported problems.», desinstalar y reinstalar.
- PnPUtil (Administrador): `/enum-devices /problem` (1903; `/problem 43`); `/drivers` (2004); `/restart-device`, `/remove-device`, `/scan-devices`; `/add-driver <.inf> /install`.

## 5. Benchmark y sus tipos

- UCM, *Estructura de Computadores*, tema 4 (2010-11): métrica = unidad; patrón = carga. Técnicas: analíticos, simulación, máquina real. Benchmark = programa o conjunto patrón para medir y comparar.
- Tiempo de respuesta (*response time*): percibe el usuario; productividad (*throughput*): tareas por unidad de tiempo. Tiempo de CPU: sin E/S ni otros programas (usuario + SO).
- MIPS = instrucciones / (tiempo · 10⁶); dependen del repertorio, varían por programa, pueden ir al revés del rendimiento. MFLOPS = operaciones en coma flotante / (tiempo · 10⁶); normalizados: 1 suma, resta, comparación, multiplicación; 4 división, raíz cuadrada; 8 exponenciación, trigonométricas. Media geométrica con referencia.
- Criterios no excluyentes. Ámbito: enteros (SPECint2000); punto flotante (SPECfp2000, LINPACK, Fortran, Mflops/s); transacciones (TPC-C). Naturaleza: reales (más precisos); núcleos (Linpack, Livermore Loops); conjuntos (SPEC, TPC); reducidos (10-100 líneas, Quicksort); sintéticos (Whetstone, Dhrystone).
- SPEC: sin ánimo de lucro, cocientes frente a referencia. TPC: consorcio; TPC-A, B, C «ya están en desuso» (2010). SPEC2006 «la última» (2010).
- SPEC CPU 2026 (web 05-10-2026): 52 benchmarks, cuatro suites; SPECspeed Integer y Floating Point = tiempo; SPECrate = productividad; energía opcional. SPEC CPU 2017: 43 pruebas; 03-11-2026 sin resultados; 17-11-2026 retirada; nota 05-05-2026.
- Cinebench 2026 (Maxon): Redshift de Cinema 4D, CPU y GPU, programa real. 3DMark (UL): juegos, fotogramas, estrés. PerformanceTest (PassMark): CPU, 2D, 3D, disco, memoria; IOPS; compara con equipos similares. CrystalDiskMark: disco secuencial y aleatorio; SSD depende de datos (aleatorios, ceros). `winsat mem`: ancho de banda de memoria; Administradores; `winsat mem -mint 4.0 -maxt 12.0 -buffersize 32MB -xml memtest.xml`.
- Rendimiento = cifra para comparar; estrés = aguantar al máximo (UL). Lentitud = rendimiento; fallos con carga = estrés.
- `time` `90.7u 12.9s 2:39 65%`: CPU 103,6 s; respuesta 159 s; 65 %; resto 55,6 s.
- 600·10⁶ instrucciones en 2 s: 300 MIPS; 50·10⁶ coma flotante: 25 MFLOPS. Otra: 1,5 s, 300·10⁶ instrucciones = 200 MIPS y más rápida.
