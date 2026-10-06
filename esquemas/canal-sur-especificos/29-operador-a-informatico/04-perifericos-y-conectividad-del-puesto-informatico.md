# Tema 4 del específico de Operador/a Informático · Periféricos y conectividad del puesto informático

**Siglas**: USB-IF, PD, UASP, HID, DVI, HDMI, ARC/eARC, VESA, MST, DSC, TMDS, EDID, HPD, MFP, IPP, WIA, OTG.

Esqueleto para repasar, no resumen: nada que no esté en el tema; ante la duda, vuelve a él.

<!-- indice -->
<!-- /indice -->

## 1. Periféricos del puesto

- Bourgeois: puertos de la placa; casi todo USB (1996); Bluetooth (1994): impresora, móvil, teclado y ratón.
- Oficio: entrada = teclado, ratón, escáner, micrófono, cámara; salida = monitor, impresora, altavoz, proyector; E/S = disco, memoria, tarjeta de red, pantalla táctil (monitor normal no). Familias: impresión salida (MFP E/S); almacenamiento E/S; visualización salida; digitalización entrada; multimedia los tres.
- USB-IF: clase = 3 bytes (Base Class, SubClass, Protocol); Windows carga el controlador de clase solo.
- Learn 13-06-2025: 01h Audio Usbaudio.sys; 03h HID Hidclass.sys y Hidusb.sys; 06h Image/Still Imaging Usbscan.sys; 07h Printer Usbprint.sys; 08h Mass Storage Usbstor.sys (Uaspstor.sys UASP); 09h Hub Usbhub.sys (Usbhub3.sys SuperSpeed); 0Eh Video Usbvideo.sys.
- Clase USB ≠ categoría: audio 01h, en Sonido, vídeo y juegos (Media). Uaspstor = SuperSpeed con bulk streams. Usbscan = componente USB de WIA.

## 2. Elementos de impresión

- Canon, láser: electrofotográfica; tambor cargado; láser expone, carga se disipa donde se imprime; tóner queda (revelado); estática lo pasa al papel (transferencia); calor y presión (rodillo) fijan.
- Color 4 tóneres CMYK; desgaste: tambor, cargador electrostático, limpiador, tóner; Canon 1982 cartucho integrado; MFP láser = copia, escaneo, fax. FPOT = tiempo hasta la primera hoja.
- Canon, inyección: gotas de picolitros; térmica (burbuja: calentador; boquilla simple, mayor densidad); piezoeléctrica (elemento se deforma con la tensión; cantidad regulable con voltaje). Cian, magenta, amarillo + negro; colorante disuelto; pigmento en partículas sin disolver.
- Zebra: Transferencia térmica: cinta de cera o resina; duradera; papel, poliéster, polipropileno. Térmica directa: sin cinta, tóner ni tinta; soporte termosensible que ennegrece; se desvanece. Ninguna usa tinta. Impacto: golpea cinta entintada (matricial, margarita, bola).
- ISO/IEC 24734 (HP 2009): productividad, papel normal, modo por defecto, B/N y color, mono y multifunción, cualquier tecnología; FSOT primer juego; EFTP rendimiento efectivo; ESAT sostenido estimado. Velocidad depende de equipo, controlador, aplicación, SO, conexión.
- PWG, IPP Everywhere: imprimir sin software del fabricante (USB y red); exige IPP/2.0, DNS-SD, PWG Raster, JPEG JFIF (color). PWG 5100.12-2024 IPP/2.x 4.ª ed.; RFC 7472 IPP sobre HTTPS, 'ipps'.
- Windows 10 21H2: Mopria nativo (IPP Class Driver). Fin controladores de terceros (calendario mayo 2025): sept. 2023 anuncio; 15-01-2026 Windows 11+/Server 2025+ sin controladores nuevos en Windows Update; 01-07-2026 se prefiere siempre IPP de clase; 01-07-2027 sin actualizaciones de terceros salvo seguridad. Otoño 2026: rigen los dos primeros; existentes siguen instalándose.
- MFP red: Print IPP, Fax IPP Fax Out, Scan WS-Scan o eSCL; USB sólo en modo IPP Over USB.
- Impresión protegida (Microsoft 18-06-2026): sólo Windows Ready Print; Configuración > Bluetooth y dispositivos > Impresoras y escáneres > Preferencias > Set up. Efectos: desinstala impresoras de terceros; quita XPS y fax; por GPO no se desactiva sin administrador (tema 6); escáner de MFP no Mopria no disponible, sólo impresión.

## 3. Elementos de almacenamiento

- Memoria USB, disco/SSD externo, lector: E/S, 08h Usbstor.sys, UASP si SuperSpeed. USB PD 3.1: discos duros e impresoras alimentados por bus.
- Discos, SSD, flash, RAID, NAS, SAN, copias, compresión, clonación, recuperación: tema 3.

## 4. Elementos de visualización

- Aspecto (oficio): ancho:alto; 4:3 TV analógica y monitores antiguos (1,33); 1:1 cuadrada; 5:4 monitor antiguo; 16:9 TV digital y actual (1,78); 640×480 = 4:3; 1920×1080 = 16:9.
- EIZO (sin fecha), IPS/VA/TN: ángulo IPS excelente, VA muy bueno, TN regular; respuesta IPS buena, VA y TN excelente; contraste IPS aprox. 500:1, VA y TN 1.000:1 o más; precio IPS alto, VA medio, TN bajo; gama de color independiente del panel; gráficos IPS o VA.
- Reloj de píxel a 60 Hz (MIT 6.111): 640×480 VGA 25 MHz (40 ns); 800×600 SVGA 40; 1024×768 XVGA 65; 1280×720 74,25 (SMPTE ST 2059-1:2021; MIT 75.25 no cuadra); 1920×1080 148,5 (6,7 ns). VGA exacto 25,175 MHz (Cornell). DVI sencillo 165 MHz: 1080p60 cabe.
- Windows 11: Identify; Display > Multiple displays > Detect; arrastrar y Apply.
- Windows + P: PC screen only; Duplicate (proyector); Extend (dos monitores); Second screen only.

## 5. Elementos de digitalización

- Epson Technical Brief 2007: óptica = píxeles del CCD (600×2400: óptica 600, primera cifra); hardware = motor paso a paso (doble o cuádruple paso) sube la segunda cifra; interpolada = algoritmo añade píxeles. Hardware 1200×2400 anuncia 9600×9600 interpolada.
- 2×2,5 pulg a 1200 ppp ampliada a 8×10 = 300 ppp.
- Profundidad = bits por píxel; colores = 2^profundidad: 1 bit 2; gris 8 bits 256; RGB 24 bits 16,7 millones; RGB 48 bits más de 250 billones.
- WIA (Microsoft Learn): imagen fija desde Windows Me y XP; antes STI (hardware) + TWAIN (API); WIA se apoya en STI, no requiere TWAIN, que sigue soportado. Escáneres WIA sin instalar con Fax y Escáner y Paint; red WS-Scan (MFP: WS-Scan o eSCL); USB Usbscan.sys clase 06h.

## 6. Elementos multimedia

- Micrófono y cámara web entrada; altavoces salida; auriculares con micrófono ambos.
- USB: audio 01h Usbaudio.sys; cámara 0Eh Usbvideo.sys. Bluetooth: auriculares y altavoces.
- MIT: VGA analógica solo vídeo; HDMI digital con audio. DisplayPort con audio y DVI sin audio: oficio (VESA y DDWG no tratan audio).
- ARC: TV envía audio «upstream» a AVR o barra de sonido por el mismo cable; eARC: formatos más avanzados y máxima calidad.

## 7. Conectividad: USB

- USB-IF: la versión fija sólo la velocidad; 3.2 no es Type-C, Standard-A, Micro-USB, USB PD ni Battery Charging; Type-C de 480 Mbit/s a 80 Gbit/s; Standard-A puede ser 5 Gbit/s.
- Cinco velocidades (USB4 y 3.2): 80, 40, 20, 10, 5 Gbps; al público «USB 80Gbps», etc.; nombres técnicos (USB4 V2.0/V1.0, 3.2, SuperSpeed Plus, Enhanced SuperSpeed, SuperSpeed+) no en producto (guía enero 2024).
- Tabla: 1,5 y 12 Mbit/s Basic-Speed; 480 Mbit/s USB 2.0 Hi-Speed; 5 Gbit/s USB 3.2 Gen 1; 10 Gen 2; 20 Gen 2x2 (dos carriles de 10) o USB4 20Gbps; 40 USB4 40Gbps; 80 USB4 en cables certificados 80. USB4 por versión 1.0 o 2.0: no consta.
- USB 3.2 absorbió las 3.x; velocidad común más baja (SSD 10 en puerto 5 rinde 5). USB4: Thunderbolt (Intel), dobla ancho de banda, varios protocolos de datos y pantalla; compatible con 3.2, 2.0, Thunderbolt 3; menor velocidad común.
- USB 2.0: Standard-A, Standard-B, Mini-B; Micro-USB rev. 1.01 (04-04-2007): Micro-B, Micro-AB receptáculo, Micro-A clavija. Tabla 4-1: Standard-A admite A; Standard-B admite B; Mini-B admite Mini-B; Micro-B admite Micro-B; Micro-AB admite Micro-A o Micro-B.
- A-device da VBUS y es anfitrión; B-device periférico; Micro-AB sólo OTG; PC Standard-A, impresora a menudo Standard-B (oficio). Micro: 10.000 ciclos.
- Longitud máxima (Class Document rev. 2.0, agosto 2007): Standard ambos extremos 5 m; Mini-B + Standard-A 4,5 m; cualquier Micro 2 m.
- Type-C: delgado, reversible (clavija y sentido del cable). Cable USB-C a USB-C: logo USB-IF obligatorio, velocidad y vatios (USB 20Gbps, 20 V 3 A = 60 W: logo 20Gbps/60W); USB 2.0 Type-C 240 W o 60 W: datos hasta 480 Mbps.
- USB PD 3.1 (2021): hasta 240 W; antes 100 W (20 V × 5 A); 28 V 140 W, 36 V 180 W, 48 V 240 W; dirección no fija; monitor con corriente carga el portátil mientras muestra imagen.
- Thunderbolt: TB4 siempre 40 Gbps (datos, vídeo, potencia); TB5 (Intel 12-09-2023) 80 Gbps bidireccional, Bandwidth Boost 120; USB4 V2, DisplayPort 2.1, PCIe Gen 4 (doble PCIe); red punto a punto 10GbE (TB5 el doble). Vatios: no constan.

## 8. Conectividad: RJ45

- Oficio: 8 hilos, 4 pares trenzados; 100 m por tramo.
- Fluke: T568A y T568B intercambian los pares naranja y verde; T568A verde en 1-2 y naranja en 3-6; T568B naranja en 1-2 y verde en 3-6; el resto igual.
- T568A: preferido, compatible con USOC de uno y dos pares; T568B: más usado, coincide con AT&T 258A, sólo un par compatible con USOC. Ambas en ANSI/TIA-568.2-D, mismo rendimiento, incluido Gigabit; no mezclar: color con color, raya con raya.
- Panduit TR103: ambas son cable directo (mismo pin en ambos extremos); Fluke: mismo código en ambos extremos.
- Cruzado (Fluke): PC a PC, hub o switch entre sí; envío y recepción cruzados; ANSI/TIA-568-C.2 no lo define. Cisco: pin 1 = pin 3 del otro extremo; pin 2 = pin 6. Clásico T568A con T568B (deducción propia).
- Panduit: cruzado de 2 pares 10/100 Mbit/s; de 4 pares hasta 1 Gbit/s.
- Auto-MDIX (Cisco): detecta directo o cruzado y configura; switches modernos admiten directo; sin él, directo a servidores, estaciones o routers y cruzado a otros equipos o repetidores. Catalyst 9300: activado por defecto; el enlace sólo cae con cable equivocado si está desactivado en ambos extremos.

## 9. Conectividad: VGA

- MIT: analógica, solo vídeo. 5 señales (rojo, verde, azul, hsync, vsync) por conector HD15 (15 contactos); 0,7 V pico a pico (1 V con sincronismo); 75 Ω por señal en el monitor; sincronismos activos a nivel bajo (Cornell); 640×480 a 25,175 MHz.
- DDC/EDID y patillaje VGA: no constan; DVI trata monitor analógico como el de 15 pines VGA.

## 10. Conectividad: DVI

- DDWG DVI rev. 1.0 (02-04-1999), 4 objetivos: digital sin pérdidas; independiente de la pantalla; plug and play (HPD, EDID, DDC2B); un conector digital y analógico.
- Dos conectores de igual mecánica: sólo digital (24 contactos, tres filas de ocho, TMDS); combinado (29: los 24 + 5 analógicos: R, G, B y 2 sincronismos). Monitor analógico no encaja en el sólo digital.
- Enlace sencillo hasta 165 MHz incluido; más, dos enlaces (200 MHz = 100 MHz por enlace); doble enlace sin máximo especificado.
- EDID por DDC; HPD lo maneja el monitor para avisar de su presencia; +5 V del sistema para leer EDID con monitor apagado.
- DVI-A analógica, DVI-D digital, DVI-I ambas: nombres de uso, no de la especificación de 1999.

## 11. Conectividad: HDMI

- 1.4b: 4096×2160 a 24 Hz, 3840×2160 a 24, 25 y 30 Hz, 1920×1080 a 120 Hz; HDMI Ethernet Channel (High Speed HDMI Cable with Ethernet); ARC; conector HDMI Micro.
- 2.1: Ultra High Speed HDMI Cable, mercado 2020, hasta 48 Gbps.
- 2.2 (vigente): 96 Gbps, Fixed Rate Link; hasta 12K@120 y 16K@60; cable Ultra96, único para todas las aplicaciones 2.2; compatible hacia atrás. Además eARC; VRR (menos lag, stutter, tearing); HDMI Cable Power alimenta cables activos.
- Ultra96 y Ultra High Speed: certificación obligatoria; etiqueta con QR; nombre en la cubierta.
- Conectores A, C y D; adaptadores pasivos; HDMI Alt Mode para USB Type-C (página de la 1.4b).

## 12. Conectividad: DisplayPort

- VESA: estándar de facto de monitores de PC y pantallas integradas; conectores: estándar con retención, Mini-DP, Type-C; dentro de Thunderbolt y USB4.
- DisplayPort 2.1 (VESA 17-10-2022): compatible con 2.0 y la sustituye; capa física común con USB Type-C y USB4.
- DP40: UHBR10 (10 Gbps), cuatro carriles, 40 Gbps; DP80: UHBR20 (20 Gbps), cuatro carriles, 80 Gbps; DP40 certificados valen para DP54; 2.1b: cable activo DP80LL hasta 3 m. DSC obligatoria en túnel USB4; reduce ancho de banda más del 67 % sin artefactos.
- MST: varias pantallas (resoluciones distintas) desde una salida. Conversión a HDMI, DVI, VGA con cables o convertidores (DisplayPort o USB-C).
- Frente a frente: DVI analógico y digital, sin audio; HDMI sólo digital, audio, doméstico; DisplayPort sólo digital, audio, informático, retención; VGA analógica, solo vídeo, 15 contactos.

## 13. Aplicación práctica

- Casos (oficio): USB-C con monitor con fuente = imagen, datos y carga, mirar rótulo; VGA a HDMI = convertidor activo; segundo monitor: Detect, Win + P Extend; DVI >165 MHz = doble enlace; latiguillo A-A o B-B; escáner 9600 ppp: mirar la óptica; USB 10Gbps en puerto 5Gbps: 5.

## No lo da el tema

- No consta: patillaje VGA y DDC/EDID; ISO/IEC 24734 vigente, 19752, 24711; CIS, OCR; OLED; vatios TB4 y TB5; USB4 por versión; reloj de otras resoluciones; patillaje RJ45. Remite: temas 3, 6, 13.
