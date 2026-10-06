# Investigación · Operador/a Informático (29) · Bloque A-hardware (temas 1, 2, 3 y 4)

Fase 1. Sólo lo que falta para cubrir el enunciado, descontado lo de RTVE que el coordinador ya
localizó (lo leerá el redactor). Negrita entre comillas = literal de la fuente (casi todas en inglés:
el redactor traduce en redonda y deja la cifra). Fecha de lectura de todas las fuentes de este
informe: **05-10-2026** (el encargo dice «hoy es 24-09-2026»; el reloj del sistema marca 05-10-2026 y
es la fecha que se declara). Copias de cada fuente en `fuentes/canal-sur/informatico/web/` (texto
plano; los PDF, junto a su `.txt`).

## 0. Avisos para el redactor

1. **Ninguna norma jurídica**: el bloque es técnico puro. Lentes: sólo `refutar_prosa.py` e
   `indice.py`.
2. **Lo de RTVE que no casa con Canal Sur**: RTVE 17 (§ 2 y 3) y RTVE 08 de Gestión Administrativa
   (§ 6) giran en torno a «la pregunta 11», «la pregunta 52», «Ésa es la respuesta oficial»: hay que
   quitarlo (aquí **no hay exámenes anteriores**). Igual con las remisiones «tema 7 del específico de
   Técnica de Equipos», «tema 10 …», «tema 2» de RTVE 17 § 1 y § 4.
3. **RTVE 08 (Ofimática) § 3** dice que FAT32 y exFAT «usados en memorias extraíbles» y que **ext4 o
   APFS en Linux y macOS**: no lo he re-verificado (es del bloque B, tema 9); si se copia, que se
   compruebe allí.
4. **Lo que no pude descargar** (403 o bloqueo del servidor a la descarga automática): iso.org, la web
   de prensa de Intel (se usó la copia PDF de su archivo), la referencia de Digilent, jedec.org
   (véase cada tema). Lo que sólo consta por el resumen del buscador va marcado **[SÓLO BUSCADOR]**:
   no debe entrar en el tema salvo que el verificador lo lea en la fuente.

## Fuentes leídas en esta fase

| Fuente | Fichero | Leída |
|---|---|---|
| USB-IF, *USB Data Performance Language Usage Guidelines*, enero 2024 | `usbif-data-performance-language-2024.txt` | 05-10-2026 |
| USB-IF, *USB 3.2 Specification Language Usage Guidelines* | `usbif-usb32-language.txt` | 05-10-2026 |
| USB-IF, *USB4® Specification Language Usage Guidelines* | `usbif-usb4-language.txt` | 05-10-2026 |
| USB-IF, página «USB4®» (usb.org/usb4) | `usbif-usb4.txt` | 05-10-2026 |
| USB-IF, página «USB Charger (USB Power Delivery)» | `usbif-charger-pd.txt` | 05-10-2026 |
| USB-IF, página «USB Type-C® Cable and Connector Specification» | `usbif-typec.txt` | 05-10-2026 |
| USB-IF, *USB Type-C® Cable Logo Usage Guidelines* (fichero «jan26», © 2024) | `usbif-typec-cable-logo-2026.txt` | 05-10-2026 |
| USB-IF, *USB Logo Usage Guidelines* (Basic-Speed / Hi-Speed), 2024.02.8 | `usbif-original-logo-2024.txt` | 05-10-2026 |
| USB-IF, *USB Performance Logo Usage Guidelines*, 2024-06-21 | `usbif-performance-logo-2024.txt` | 05-10-2026 |
| Intel, nota de prensa «Intel Introduces Thunderbolt 5 Connectivity Standard», 12-IX-2023 (PDF de archivo) | `intel-tb5-press.txt` | 05-10-2026 |
| Thunderbolt Technology Community (Intel), página «Technology» | `thunderbolt-tech.txt` | 05-10-2026 |
| MIT, curso 6.111, *Lab #3* (otoño 2019), «Video display technologies: HDMI & VGA» | `mit-6111-lab3-vga.txt` | 05-10-2026 |
| Cornell, ECE 5760, «DE2 VGA», y ECE 4760, proyecto «Homemade VGA Adapter» (2012) | `cornell-ece5760-vga.txt`, `cornell-ece4760-vga-adapter.txt` | 05-10-2026 |
| Canon Inc., «Laser Printers and MFPs» (global.canon, Canon Technology) | `canon-laser-tech.txt` | 05-10-2026 |
| Canon Inc., «Inkjet Printers» (global.canon, ij2021s) | `canon-inkjet-2021.txt` | 05-10-2026 |
| Epson Europe, «Heat-Free Technology» | `epson-heat-free.txt` | 05-10-2026 |
| HP, «ISO/IEC 24734 Method for Measuring Digital Printing Productivity» (© 2009) | `hp-iso24734.txt` | 05-10-2026 |
| Microsoft Learn, «End of servicing plan for third-party printer drivers on Windows» (act. 2025-05-09) | `ms-print-driver-eos.txt` | 05-10-2026 |
| Microsoft Learn, «Windows Protected Print Mode» (act. 2026-06-18) | `ms-wppm.txt` | 05-10-2026 |
| Printer Working Group, «IPP Everywhere» y página del grupo IPP | `pwg-ipp-everywhere.txt`, `pwg-ipp.txt` | 05-10-2026 |
| Microsoft Learn, «Windows Image Acquisition (WIA)» y «Windows Image Acquisition Drivers» | `ms-wia.txt`, `ms-wia-drivers.txt` | 05-10-2026 |
| Epson America, *Scanner Technical Brief* (6/07) | `epson-scanner-brief.txt` | 05-10-2026 |

(Las de los temas 1, 2 y 3 se añaden en su sección.)

---

## TEMA 4 · Periféricos y conectividad del puesto informático

Enunciado: «Periféricos y conectividad del puesto informático: elementos de impresión,
almacenamiento, visualización, digitalización y multimedia; conectividad USB, RJ45, VGA, DVI, HDMI y
DisplayPort.»

Cubierto por RTVE: clasificación de periféricos (RTVE 17 § 2; RTVE 08 § 1), DVI/HDMI/DisplayPort
(RTVE 18 TI § 4), RJ45 (Montaje 05 § 6). **Falta: impresión, digitalización, USB, VGA en detalle;
también Thunderbolt (lo pide el coordinador) y el estado actual de la impresión en Windows.**
Almacenamiento como periférico: remite al tema 3. Visualización y multimedia: véase 4.6.

### 4.1 USB: velocidades y nombres

**Las cinco velocidades actuales y su nombre comercial** (USB-IF, *Data Performance Language*,
2024):

- **«The USB4® and USB 3.2 specifications together identify five transfer rates – 80Gbps, 40Gbps,
  20Gbps, 10Gbps, and 5Gbps.»**
- Nombres recomendados al consumidor: **«Marketing name: USB 80Gbps»**, **«USB 40Gbps»**, **«USB
  20Gbps»**, **«USB 10Gbps»**, **«USB 5Gbps»**, cada uno con **«Product capability: product signals
  at …»** la cifra correspondiente.
- **«NOTE: USB4® Version 2.0, USB4® Version 1.0, USB 3.2, SuperSpeed Plus, Enhanced SuperSpeed and
  SuperSpeed+ are defined in the USB specifications however these terms are not intended to be used
  in product names, messaging, packaging or any other consumer-facing content.»** Dato de examen: los
  nombres técnicos (USB 3.2 Gen 2x2, USB4 v2) son de la especificación; al público se le dice «USB
  20Gbps», «USB 80Gbps».

**USB 3.2 y sus tres velocidades** (USB-IF, *USB 3.2 Language*, sin fecha en el documento):

- **«The USB 3.2 specification absorbed all prior 3.x specifications. USB 3.2 identifies three
  transfer rates, USB 3.2 Gen 1 at 5Gbps, USB 3.2 Gen 2 at 10Gbps and USB 3.2 Gen 2x2 at 20Gbps.»**
- **«The USB 3.2 specification defines multi-lane operation for new USB 3.2 hosts and devices,
  allowing for up to two lanes of 10Gbps operation to realize a 20Gbps data transfer rate.»**
- Nombres que daba este documento (anterior): **«SuperSpeed USB»** (5 Gbps), **«SuperSpeed USB
  10Gbps»**, **«SuperSpeed USB 20Gbps»**. Ojo: el documento de 2024 los sustituye por «USB 5Gbps»,
  «USB 10Gbps», «USB 20Gbps». Manda el de 2024.
- **«Backwards compatible with all existing USB products; will operate at lowest common speed
  capability.»**
- **«USB 3.2 only defines the transfer rate of a product. USB 3.2 is not USB Type-C™, USB
  Standard-A, Micro-USB, or any other USB cable or connector. USB 3.2 is not USB Power Delivery or USB
  Battery Charging.»** (Distinción clave: versión = velocidad; Type-C = conector; PD = energía.)

**USB4** (USB-IF, página usb.org/usb4):

- **«Based on the Thunderbolt™ protocol specification contributed by the Intel Corporation, USB4
  doubles the maximum aggregate bandwidth of USB and enables multiple simultaneous data and display
  protocols.»**
- **«Compatibility with existing USB 3.2, USB 2.0, and Thunderbolt 3 hosts and devices is supported,
  and the resulting connection scales to the best mutual capability of the devices being
  connected.»**
- **«Two-lane operation using existing USB Type-C cables and up to 80 Gbps operation over 80 Gbps
  certified cables»**; **«Backwards compatibility with all previous versions of USB»**.
- La guía *USB4 Language* (anterior a v2) recoge **«USB4® identifies two transfer rates, USB4® 20Gbps
  at 20Gbps and USB4® 40Gbps at 40Gbps.»** y **«USB4® should not be translated into languages other
  than English.»**

**USB 2.0** (USB-IF, *USB Logo Usage Guidelines*, 2024): **«The Basic-Speed USB Logo must be used with
Basic-Speed (12 Mbps or 1.5 Mbps) Product. The Hi-Speed USB Logo must be used with Hi-Speed (480
Mbps) Product.»** Y la guía de cables Type-C: **«USB 2.0 Type-C® 240W and 60W cables deliver data at
up to 480Mbps»**.

Tabla resumen que el redactor puede montar sólo con lo anterior: 1,5 y 12 Mbit/s (Basic-Speed, USB
2.0 y anteriores), 480 Mbit/s (Hi-Speed), 5 / 10 / 20 Gbit/s (USB 3.2 Gen 1 / Gen 2 / Gen 2x2), 20 /
40 Gbit/s (USB4), 80 Gbit/s (USB4 versión 2.0). **No confirmado en fuente leída**: los nombres «Low
Speed» y «Full Speed» para 1,5 y 12 Mbit/s (la guía dice «Basic-Speed»); el año de cada versión.

**USB Type-C** (USB-IF, página de la especificación): **«Slim and sleek connector tailored to fit
mobile device product designs, yet robust enough for laptops and tablets»**; **«Features reversible
plug orientation and cable direction»**; **«Supports scalable power and performance to future-proof
your solution»**. Motivo: **«the relatively large size and internal volume constraints of the
Standard-A and Standard-B versions of USB connectors»**.

**Marcado de cables USB-C a USB-C** (*Cable Logo Usage Guidelines*): **«All USB-C® to USB-C cables are
required to use the USB-IF approved cable logo on the cable in the form of either being embossed on
the over mold or printed on the overmold»**; **«all USB-C® to USB-C cables must be labeled using the
appropriate data rate and power wattage cable logo. For example, a USB 20Gbps cable that supports 20V
at 3A must be marked with the Combined Performance and Power 20Gbps/60W logo.»**

**USB Power Delivery** (USB-IF, página USB Charger):

- **«Announced in 2021, the USB PD Revision 3.1 specification is a major update to enable delivering
  up to 240W of power over full featured USB Type-C® cable and connector. Prior to this update, USB PD
  was limited to 100W using a solution based on 20V using USB Type-C cables rated at 5A.»**
- **«New 28V, 36V, and 48V fixed voltages enable up to 140W, 180W and 240W power levels,
  respectively.»**
- **«Power direction is no longer fixed. This enables the product with the power (Host or
  Peripheral) to provide the power.»**
- Ejemplo de puesto: **«A monitor with a supply from the wall can power, or charge, a laptop while
  still displaying.»**; **«Enables new higher power use cases such as USB bus powered Hard Disk Drives
  (HDDs) and printers.»**

### 4.2 Thunderbolt

- Intel, nota de 12-IX-2023: **«Thunderbolt 5 will deliver 80 gigabits per second (Gbps) of
  bi-directional bandwidth, and with Bandwidth Boost it will provide up to 120 Gbps for the best
  display experience.»**
- **«Built on industry standards including USB4 V2, DisplayPort 2.1 and PCI Express Gen 4; fully
  compatible with previous versions.»**; **«Double the PCI Express data throughput for faster storage
  and external graphics.»**; **«Utilizes a new signaling technology, PAM-3, […] passive cables up to
  1 meter.»**
- Cita de Microsoft en la misma nota: **«Thunderbolt 5 is fully USB 80Gbps standard compliant»**.
- **«Computers and accessories based on Intel's Thunderbolt 5 controller, code-named Barlow Ridge, are
  expected to be available starting in 2024.»**
- Thunderbolt Technology Community: **«Thunderbolt 4 always delivers 40 Gbps speeds and data, video
  and power over a single connection, while Thunderbolt 5 promises speeds of 80/120 Gbps.»**;
  **«compliance across the broadest set of industry-standard specifications – including USB4,
  DisplayPort and PCI Express (PCIe) – and is fully compatible with prior generations of Thunderbolt
  and USB products.»**; Thunderbolt Networking: **«a peer-to-peer connection at 10GbE speeds»** (se
  refiere a Thunderbolt 3/4; la nota de 2023 dice que el 5 lo duplica: **«Double the bandwidth of
  Thunderbolt Networking»**).
- **[SÓLO BUSCADOR]** Carga de 240 W en Thunderbolt 5 y de 100 W o 140 W en Thunderbolt 4 (los
  resúmenes se contradicen). No está en la nota de prensa leída: no afirmar.

### 4.3 VGA

- MIT 6.111: **«the main difference is that VGA is analog and video only, while HDMI is digital and
  carries audio.»**
- **«most analog computer monitors work -- they accept 5 analog signals (red, green, blue, hsync, and
  vsync) over a standardized HD15 connector. The signals are transmitted as 0.7V peak-to-peak (1V
  peak-to-peak if the signal also encodes sync). The monitor supplies a 75Ω termination for each
  signal»**.
- **«640x480 (VGA), requires 25MHz (40ns) pixel clock for 60Hz refresh»**; **«800x600 (SVGA),
  requires 40MHz»**; **«1024x768 (XVGA), requires 65MHz»**; **«1920x1080 (1080p), requires 148.5MHz
  (6.7ns) pixel clock for 60Hz refresh»**.
- Cornell ECE 4760: **«25.175 MHz is the VGA standard»**; sincronismos **«digital active low»**.
- Frente a HDMI (MIT): **«HDMI is all digital and uses transition-minimized differential signaling
  (TMDS)»**. Útil para el cuadro VGA frente a los digitales de RTVE 18 § 4.
- **No confirmado en fuente leída**: asignación de patillas DE-15 (rojo 1, verde 2, azul 3, sincronismos
  13 y 14, DDC 12 y 15) y el canal DDC/EDID. Sólo en webs comerciales y Wikipedia; la referencia de
  Digilent (fabricante) no se dejó descargar. Que no entre o que el verificador la busque en VESA.

### 4.4 Impresión

**Láser** (Canon, «Laser Printers and MFPs»):

- **«Laser printers are printers that use electrophotographic technology.»** Proceso entero en una
  frase: **«The print command is converted into laser light, which is irradiated (exposed) onto a
  cylindrical photosensitive drum. The photosensitive drum is charged with static electricity
  beforehand, and the exposure causes the static electricity to dissipate only in the printed area
  (development). When the photosensitive drum is covered with powdered ink toner, the toner remains
  only in the area exposed to the laser beam, and the force of static electricity attracts (transfers)
  the toner onto the paper. Heat and pressure are applied to adhere (fix) the toner onto the paper,
  and printing is complete.»** (Fases: carga, exposición, revelado, transferencia, fijado.)
- **«Multifunction laser printers (MFPs) are laser printers equipped with additional functions such as
  copying, scanning, and faxing.»**
- Consumibles y desgaste: **«require parts that are subject to wear and that require frequent
  maintenance, such as a photosensitive drum, an electrostatic charger, and a cleaner, as well as
  toner in powder form»**; **«When used in color printing, a toner produces printed images in the four
  CMYK colors.»**
- Fusor: **«powdered toner is melted by a heat source and put under pressure by a pressure roller,
  fixing it onto paper.»** FPOT: **«first print out time, or the time it takes for the first sheet of
  media to be output»**.
- **«In 1982, Canon developed the world's first integrated toner cartridge system, in which the
  toner, photosensitive drum, and other major components are replaced together.»**

**Inyección de tinta** (Canon, «Inkjet Printers»):

- **«These droplets have volumes of mere picoliters (one trillionth of a liter).»**
- **«There are two main types of ink ejection mechanism. The thermal process (bubble jet process) uses
  a heater to create air bubbles in the ink, which pushes the ink out of the nozzle. In printers that
  use the piezoelectric process, voltage is applied to a piezoelectric element, which changes shape as
  a result. This compresses the ink, ejecting it from the nozzle.»**
- **«The thermal process allows for a more simple nozzle structure and a greater nozzle density […]
  The piezoelectric process […] the amount of ink that is ejected can be changed by adjusting the
  voltage that is applied.»**
- Colores: **«cyan, magenta, and yellow, together with black»**. Tintas: colorante (**«dye is
  dissolved at the molecular level»**) frente a pigmento (**«remains in particle form,
  undissolved»**).
- Epson (piezo): **«Heat-Free printing is Epson's inkjet technology that prints without using heat in
  the ink-delivery process. Traditional laser printers use heat to fuse toner onto the page»**; la
  inyección **«no toner cartridges, drum units, or fuser assemblies to dispose of»**. Las cifras de
  ahorro de Epson («eight times more electricity», «up to 83 %») son publicidad del fabricante: si
  entran, atribuidas.

**Medir la velocidad: ISO/IEC 24734** (HP, página de 2009):

- **«ISO/IEC 24734 specifies a method for measuring the productivity of digital printing devices
  using varying test files, office applications, and print job characteristics on plain paper in
  default mode. It is applicable to black-and-white and color devices, and to single-function and
  multi-function devices, regardless of print technology (e.g. inkjet, laser, etc).»**
- Medidas: **«First Set Out Time (FSOT)»**, **«Effective Throughput (EFTP)»**, **«Estimated Saturated
  Throughput (ESAT)»**; **«HP generally advertises the average single-sided ESAT PPM.»**
- Por qué la velocidad nominal engaña: **«host computer, driver, application, operating system, and
  type of connection to the printer (USB, Ethernet, wireless)»** y el trabajo (color, dúplex, calidad,
  papel…).
- **[SÓLO BUSCADOR]** Edición vigente ISO/IEC 24734:2021 (3.ª ed.); ISO/IEC 19752 (rendimiento de
  tóner monocromo, edición 2025 sustituye a la de 2017) e ISO/IEC 24711 (rendimiento de cartuchos de
  tinta). iso.org devuelve 403. No dar edición sin leerla.

**Impresión en red sin controlador: IPP** (PWG y Microsoft):

- PWG: IPP Everywhere es **«A PWG standard that allows personal computers and mobile devices to find
  and print to networked and USB printers without using vendor-specific software.»** Requisitos:
  **«IPP/2.0, DNS-SD, PWG Raster and JPEG JFIF file formats (JPEG only required for color
  printers)»**. Cifra del PWG: **«98% of all printers sold today support IPP/2.0 and DNS-SD.»**
  Norma: **«PWG 5100.12-2024: Internet Printing Protocol/2.x Fourth Edition»**; IPP sobre HTTPS:
  **«RFC 7472: IPP over HTTPS Transport Binding and 'ipps' URI Scheme»**.
- Microsoft (fin de los controladores de terceros): **«With the release of Windows 10 21H2, Windows
  offers inbox support for Mopria compliant printer devices over network and USB interfaces via the
  Microsoft IPP Class Driver.»** Calendario (revisado en mayo de 2025): septiembre 2023, anuncio;
  **«January 15, 2026 — For Windows 11+ and Windows Server 2025+, no new printer drivers will be
  published to Windows Update.»**; **«July 1, 2026 — Printer driver ranking order modified to always
  prefer Windows IPP inbox class driver.»**; **«July 1, 2027 — Except for security-related fixes,
  third-party printer driver updates will no longer be allowed.»** A 24-IX-2026 ya rigen los dos
  primeros hitos.
- Multifunción: **«For network devices, the Print and Fax endpoints will work via IPP and IPP Fax Out,
  respectively, while the Scan endpoint will work via WS-Scan or eSCL. For USB devices, the endpoints
  will only be accessible when the USB interface is in IPP Over USB mode»**.
- **Modo de impresión protegida de Windows** (Microsoft Learn, act. 18-VI-2026): **«Windows protected
  print mode exclusively uses Windows Ready Print»**; **«is designed to work with Mopria certified
  printers»**; ruta: **«Settings > Bluetooth & Devices > Printers & scanners»**, **«Printer
  Preferences»**, **«Set up»**; efecto: **«Upon enabling Windows protected print mode, printers that
  use third-party drivers are uninstalled.»**; **«XPS and fax are removed when Windows protected print
  mode is turned on.»**; puede imponerse por directiva de grupo (**«If Windows protected print mode is
  enabled as group policy, you won't be able to disable it without contacting your
  administrator.»**). Enlaza con el tema 6 (Windows 11, GPO).

**No confirmado en fuente leída**: impresoras matriciales (impacto) y térmicas (tickets, etiquetas);
lenguajes PCL y PostScript; la unidad «ppp» como resolución de impresión. No encontré fuente de
fabricante o universitaria descargable en esta fase; lo que circula son blogs.

### 4.5 Digitalización

**Resolución del escáner** (Epson, *Scanner Technical Brief*, 2007):

- **«Optical resolution: This is the actual number of pixels read by the CCD (Charge Coupled Device),
  which measures the intensity of the light that is reflected from the image to be scanned, and
  converts it to an analog voltage. If a scanner has a resolution of 600 x 2400 dpi, its optical
  resolution is 600 dpi»**.
- **«Hardware resolution: Using a precision stepper motor to double-step or quadruple-step the
  carriage, the scanner's sub-scanner resolution can be increased.»**
- **«Interpolated resolution: Interpolation is a method to increase the resolution of an image. It
  uses a complex algorithm to "add" pixels to an image based on the mathematical probability of
  surrounding pixels.»** (La cifra «máxima» del folleto suele ser interpolada: ejemplo de la fuente,
  hardware 1200 x 2400 y máxima 9600 x 9600 dpi.)
- Profundidad: **«Pixel depth refers to the number of bits of data captured for each picture element
  (pixel).»** El número de colores es 2 elevado a esa profundidad (la fuente: **«computed by taking
  the pizel depth as an exponent of two»**).
- Ampliar: un original de 2 x 2,5 pulgadas a 1200 dpi ampliado a 8 x 10 queda en **«effective
  resolution: 300 dpi»**.

**Cómo habla Windows con el escáner** (Microsoft Learn, WIA):

- **«Windows Image Acquisition (WIA) is the still image acquisition platform in the Windows family of
  operating systems starting with Windows Millennium Edition (Windows Me) and Windows XP.»**
- **«The imaging architecture in Windows 2000 and Windows 95 or later consisted of a low-level
  hardware abstraction, Still Image Architecture (STI), and a high-level set of APIs known as TWAIN.
  […] WIA is an imaging architecture that builds on STI and does not require TWAIN, although TWAIN is
  still supported alongside WIA.»**
- **«WIA-based scanners work right out of the box on Windows with Windows scanning applications such
  as Windows Fax and Scan and Paint.»**; red: **«Web Services for Scanner (WS-Scan) protocol»** con el
  controlador de clase WSD-WIA.
- Mensajes de error del escáner que WIA canaliza: **«"Lamp warming up," "Cover open," "Paper jam,"»**.
- Escaneo moderno sin controlador: eSCL (véase 4.4, cita de Microsoft sobre multifunción).

**No confirmado**: CIS frente a CCD (sólo blogs y el resumen del buscador); OCR; alimentador
automático (ADF). La web de TWAIN Working Group no devolvió contenido.

### 4.6 Visualización y multimedia

RTVE 18 TI § 4 da DVI/HDMI/DisplayPort; MIT añade VGA (4.3). La nota de Intel aporta **DisplayPort
2.1** dentro de Thunderbolt 5, y USB-IF el monitor que carga el portátil por USB-C (4.1). **No he
encontrado fuente primaria descargable** para tipos de panel (IPS, VA, OLED), cámaras web, auriculares
o altavoces: es un hueco que el tema debe declarar o cubrir sólo con lo genérico de RTVE.

---

## TEMA 2 · Diagnóstico, mantenimiento y reparación de equipos microinformáticos

Enunciado: «Diagnóstico, mantenimiento y reparación de equipos microinformáticos: principales averías,
mensajes de error de la BIOS, sustitución y detección de averías en discos duros, memorias, tarjetas
gráficas y tarjetas de red; pruebas de rendimiento Benchmark y sus tipos.»

**Sin RTVE**: todo es nuevo. Fuentes nuevas de esta sección:

| Fuente | Fichero | Leída |
|---|---|---|
| American Megatrends, *AMIBIOS8 Check Point and Beep Code List*, versión 2.0, 10-VI-2008 (documento público; copia alojada por congatec) | `ami-amibios8-beep.txt` | 05-10-2026 |
| Dell, «Understanding Beep Codes on a Dell Desktop», kbdoc 000124349 (modificado 19-IV-2026) — **leído sólo con WebFetch (resumen de modelo), la descarga directa la bloquea Dell** | — | 05-10-2026 |
| HP, *Interactive Beep and LED Diagnostic*, HP Desktop Pro A G2/G3 (c06515367) | `hp-beep-led-diagnostic.txt` | 05-10-2026 |
| Microsoft Learn, «chkdsk» (act. 2025-05-26) | `ms-chkdsk.txt` | 05-10-2026 |
| Microsoft Learn, «Device Manager Error Messages» y páginas de los códigos 10, 22, 28 y 43 | `ms-devmgr-errors.txt`, `ms-cm-prob-*.txt`, `ms-devmgr-problem-codes.txt` | 05-10-2026 |
| smartmontools, página de manual `smartctl(8)` (rama master, GitHub) | `smartctl-man.txt` | 05-10-2026 |
| PassMark, MemTest86: «Troubleshooting» y «Individual test descriptions» | `memtest86-troubleshooting.txt`, `memtest86-tests.txt` | 05-10-2026 |
| Universidad Complutense de Madrid, Facultad de Informática, *Estructura de Computadores*, tema 4 (rendimiento), curso 2010-11 | `ucm-ec4-rendimiento.txt` | 05-10-2026 |
| SPEC, páginas «SPEC CPU 2017» (act. 28-VII-2026) y «SPEC CPU 2026» | `spec-cpu2017.txt`, `spec-cpu2026.txt` | 05-10-2026 |
| Maxon, «Cinebench»; UL, «3DMark»; PassMark, «PerformanceTest»; Crystal Dew World, «CrystalDiskMark» | `cinebench.txt`, `3dmark.txt`, `passmark-pt.txt`, `crystaldiskmark.txt` | 05-10-2026 |
| Microsoft Learn, «winsat mem» | `ms-winsat.txt` | 05-10-2026 |

### 2.1 El POST, los puntos de control y los pitidos

AMI, *AMIBIOS8 Check Point and Beep Code List* (2008), § 1.2 y 1.3:

- **«A checkpoint is either a byte or word value output to I/O port 80h. The BIOS outputs checkpoints
  throughout bootblock and Power-On Self Test (POST) to indicate the task the system is currently
  executing.»**
- **«Beep codes are used by the BIOS to indicate a serious or fatal error to the end user. Beep codes
  are used when an error occurs before the system video has been initialized. Beep codes will be
  generated by the system board speaker, commonly referred to as the "PC speaker."»** (Regla de oro:
  pitido = el fallo es anterior al vídeo; mensaje en pantalla = posterior.)
- **«Viewing all checkpoints generated by the BIOS requires a checkpoint card, also referred to as a
  "POST Card" or "POST Diagnostic Card". These are ISA or PCI add-in cards that show the value of I/O
  port 80h on a LED display.»** Alternativa en pantalla: **«This display method is limited, since it
  only displays checkpoints that occur after the video card has been activated.»**
- Orden de la secuencia según el documento: bloque de arranque (**«The Bootblock initialization code
  sets up the chipset, memory and other components before system memory is available.»**), POST,
  y entre los puntos del POST: **«Check CMOS diagnostic byte to determine if battery power is OK and
  CMOS checksum is OK. […] If the CMOS checksum is bad, update CMOS with power-on default values and
  clear passwords.»** (punto 04); **«Log errors encountered during POST.»** (84); **«Display errors
  to the user and gets the user response for error.»** (85); **«Execute BIOS setup if needed /
  requested. Check boot password if installed.»** (87).

**Tabla de pitidos de POST de AMIBIOS8** (§ 8.2, literal):

| Pitidos | Descripción | Qué hacer (§ 8.2.1) |
|---|---|---|
| 1 | **«Memory refresh timer error.»** | **«Reseat the memory, or replace with known good modules.»** |
| 3 | **«Base memory read/write test error»** | ídem |
| 6 | **«Keyboard controller BAT command failed»** | **«Fatal error indicating a serious problem with the system.»** Quitar todas las tarjetas salvo la de vídeo e ir reponiéndolas una a una |
| 7 | **«General exception error (processor exception interrupt error)»** | ídem |
| 8 | **«Display memory error (system video adapter)»** | **«If the system video adapter is an add-in card, replace or reseat the video adapter. If the video adapter is an integrated part of the system board, the board may be faulty.»** |

Método de aislamiento (literal, para pitidos 6 y 7): **«Remove all expansion cards except the video
adapter. If beep codes are generated when all other expansion cards are absent, consult your system
manufacturer's technical support. If beep codes are not generated when all other expansion cards are
absent, one of the add-in cards is causing the malfunction. Insert the cards back into the system one
at a time until the problem happens again. This will reveal the malfunctioning card.»**

Advertencia de la propia fuente: **«This covers AMIBIOS products released before May 2002. The
checkpoints defined in this document are inherent to the AMIBIOS generic core, and do not include any
chipset or board specific checkpoint definitions.»** → los códigos **dependen del fabricante y de la
generación**: el tema debe decirlo así y dar AMI como ejemplo, no como norma.

**Dell (kbdoc 000124349, mod. 19-IV-2026) — sólo vía WebFetch, cotejar antes de usar:**
**«The delay between each beep is 300 milliseconds. The delay between each set of beeps is three
seconds, and the beep sound lasts 300 milliseconds.»** Vostro: 1 pitido, fallo de suma de
comprobación de la ROM de BIOS; 2, **«No RAM Detected»**; 3, chipset o placa; 4, **«RAM Read/Write
failure»**; 5, **«RTC Power Fail»**; 6, **«Video BIOS Test Failure»**; 7, **«CPU Failure»**. En
OptiPlex modernos (desde 7010/9010) los pitidos se sustituyeron y sólo **1-3-2** indica fallo de
memoria. Todo ello **pendiente de verificación en la página**.

**HP** (*Interactive Beep and LED Diagnostic*, Desktop Pro A G2/G3): los códigos se agrupan por el
número de pitidos largos en cuatro familias, literal de los rótulos: **«BIOS»** (2 largos + 2, 3 o 4
cortos), **«Hardware»** (3 largos + 2 a 6 cortos), **«Thermal»** (4 largos + 2 o 3 cortos),
**«System Board»** (5 largos + 2 a 5 cortos). El significado de cada código no viene en el PDF (es
interactivo). **[SÓLO BUSCADOR]**: «3 Long, 2 Short» = posible fallo de memoria; los parpadeos
siguen hasta desenchufar y los pitidos se repiten cinco veces; diagnóstico UEFI de HP con Esc + F2
(prueba rápida y extensa, «failure ID» de 24 dígitos). support.hp.com devolvió 503.

**No confirmado**: mensajes de texto típicos de BIOS («CMOS checksum error», «No boot device», «CPU fan
error», «Keyboard error or no keyboard present»), códigos Award y Phoenix, códigos de POST de UEFI
(PEI/DXE) y LED Q-Code de placas de consumo. La pila CMOS sí aparece (punto 04 de AMI y «RTC Power
Fail» de Dell).

### 2.2 Disco duro: detectar y sustituir

**SMART** (`smartctl(8)`):

- **«smartctl controls the Self-Monitoring, Analysis and Reporting Technology (SMART) system built
  into most ATA/SATA and SCSI/SAS hard drives and solid-state drives. The purpose of SMART is to
  monitor the reliability of the hard drive and predict drive failures, and to carry out different
  types of drive self-tests.»**
- Atributos: **«If the Normalized value is less than or equal to the Threshold value, then the
  Attribute is said to have failed. If the Attribute is a pre-failure Attribute, then disk failure is
  imminent.»**; **«Attributes are one of two possible types: Pre-failure or Old age.»**; y la salvedad:
  **«the fact that an Attribute is of type 'Pre-fail' does not mean that your disk is about to fail!»**
  Columna **«WHEN_FAILED»**: **«FAILING_NOW»** o **«In_the_past»**.
- Autopruebas: **«short — [ATA] runs SMART Short Self Test (usually under ten minutes).»**; **«long —
  [ATA] runs SMART Extended Self Test (tens of minutes to several hours).»**; **«The "Self" tests check
  the electrical and mechanical performance as well as the read performance of the disk.»** NVMe: la
  autoprueba corta figura como **«NEW EXPERIMENTAL SMARTCTL 7.4 FEATURE»**.

**chkdsk** (Microsoft Learn, act. 2025-05-26; aplica a Windows 10 y 11 y Server 2016-2025):

- **«Checks the file system and file system metadata of a volume for logical and physical errors. If
  used without parameters, chkdsk displays only the status of the volume and doesn't fix any
  errors.»**
- **/f**: **«Fixes errors on the disk. The disk must be locked.»**; **/r**: **«Locates bad sectors and
  recovers readable information. The disk must be locked. /r includes the functionality of /f, with
  the additional analysis of physical disk errors.»**; **/x**: fuerza el desmontaje e incluye /f;
  **/b** (sólo NTFS): **«Clears the list of bad clusters on the volume and rescans all allocated and
  free clusters for errors. /b includes the functionality of /r. Use this parameter after imaging a
  volume to a new hard disk drive.»** (Enlaza con la clonación del tema 3.)
- Volumen en uso: **«Chkdsk cannot run because the volume is in use by another process. Would you
  like to schedule this volume to be checked the next time the system restarts? (Y/N)»**
- Permisos: **«Membership in the local Administrators group, or equivalent, is the minimum required to
  run chkdsk.»**; **«Chkdsk can be used only for local disks.»**
- FAT: cadenas perdidas guardadas como **«File<nnnn>.chk»**.

**No confirmado**: síntomas físicos típicos del disco mecánico (ruidos, «clic»), procedimiento de
sustitución paso a paso, precauciones electrostáticas (ESD) con fuente de fabricante. El manual de
servicio de cada fabricante es la fuente; no descargué ninguno.

### 2.3 Memoria

MemTest86 (PassMark):

- **«Please be aware that not all errors reported by MemTest86 are due to bad memory. The test
  implicitly tests the CPU, L1 and L2 caches as well as the motherboard. It is impossible for the test
  to determine what causes the failure to occur. However, most failures will be due to a problem with
  memory module. When it is not, the only option is to replace parts until the failure is
  corrected.»**
- **«Sometimes memory errors show up due to component incompatibility. A memory module may work fine
  in one system and not in another.»**
- Errores sólo con los módulos juntos: **«Most memory systems nowadays operate in multiple channel mode
  […] It is recommended that modules with identical specifications (ie. "matching modules")»**.
- **«MemTest86 cannot diagnose many types of PC failures. For example a faulty CPU that causes Windows
  to crash will most likely just cause MemTest86 to crash in the same way.»**
- Prueba de martilleo (test 13): **«designed to detect RAM modules that are susceptible to disturbance
  errors caused by charge leakage»**.
- AMI: pitidos 1 y 3 = memoria → **«Reseat the memory, or replace with known good modules.»**

**No confirmado**: Diagnóstico de memoria de Windows (`mdsched.exe`): no encontré la página vigente de
Microsoft en esta fase.

### 2.4 Tarjeta gráfica y tarjeta de red: el Administrador de dispositivos

- **«When Device Manager marks a device with a yellow exclamation point, it also provides an error
  message.»** Los códigos **«are defined in Cfg.h»**.
- **Código 10** (CM_PROB_FAILED_START): **«This device cannot start. (Code 10)»** — **«Try upgrading
  the device drivers for this device.»**
- **Código 22** (CM_PROB_DISABLED): **«This device is disabled. (Code 22)»** — **«The device is
  disabled because the user disabled it using Device Manager. Select Enable Device»**.
- **Código 28** (CM_PROB_FAILED_INSTALL): **«The drivers for this device are not installed. (Code
  28)»** — **«Please visit the website of the company that manufactures the device and look for the
  most recent drivers for this device.»**; **«PnP could not find a compatible driver for the device.
  This failure is often referred to as a DNF (driver not found) problem.»**
- **Código 43** (CM_PROB_FAILED_POST_START): **«Windows has stopped this device because it has
  reported problems. (Code 43)»** — **«Uninstall and reinstall the device.»**
- Lista de la página: códigos 1, 3, 9, 10, 12, 14, 16, 18, 19, 21, 22, 24, 28, 29, 31-43…, con su
  nombre `CM_PROB_*` (copiar sólo los que se expliquen).
- Gráfica: AMI pitido 8 (memoria de vídeo) y Dell 6 (BIOS de vídeo) — véase 2.1.

**No confirmado**: herramientas de red del puesto (`ipconfig`, `ping`, prueba del cable RJ45, LED de
enlace): son del tema 13 o del bloque B; no las investigué aquí.

### 2.5 Pruebas de rendimiento (benchmarks) y sus tipos

**Clasificación** (UCM, *Estructura de Computadores*, tema 4, 2010-11; en español, literal):

- Definición: **«será necesario disponer de un conjunto de programas representativos de la carga real
  de trabajo que vaya a tener la máquina, y con respecto a los cuales se realicen las medidas. Estos
  programas patrones se denominan benchmarks»**.
- Por el ámbito: **«Enteros: aplicaciones en las que domina la aritmética entera […] Por ejemplo,
  SPECint2000.»**; **«Punto flotante: aplicaciones intensivas en cálculo numérico con reales. Por
  ejemplo, SPECfp2000 y LINPACK.»**; **«Transacciones: aplicaciones en las que dominan las
  transacciones on-line y off-line sobre bases de datos. Por ejemplo, TPC-C.»**
- Por la naturaleza del programa:
  - **«Programas reales: Compiladores, procesadores de texto, etc. Permiten diferentes opciones de
    ejecución. Con ellos se obtienen las medidas más precisas»**
  - **«Núcleos (Kernels): Trozos de programas reales. Adecuados para analizar rendimientos específicos
    de las características de una determinada máquina: Linpack, Livermore Loops»**
  - **«Patrones conjunto (benchmarks suits) Conjunto de programas que miden los diferentes modos de
    funcionamiento de una máquina: SPEC y TPC.»**
  - **«Patrones reducidos (toy benchmarks): Programas reducidos (10-100 líneas de código) y de
    resultado conocido.»** (Quicksort)
  - **«Patrones sintéticos (synthetic benchmarks): Código artificial no perteneciente a ningún programa
    de usuario y que se utiliza para determinar perfiles de ejecución. (Whetstone, Dhrystone)»**
- Métricas: **«tiempo de respuesta (response time)»** frente a **«productividad (throughput)»**;
  **«el procesador que realiza la misma cantidad de trabajo en el menor tiempo posible será el más
  rápido»**. Técnicas: **«Modelos analíticos»**, **«Modelos de simulación»**, **«La máquina real»**.
- **Desfase**: la UCM habla de SPEC2000/2006 como «la última en vigor». Lo vigente (SPEC):

**SPEC CPU hoy** (spec.org, act. 28-VII-2026):

- **«The SPEC CPU® 2026 benchmark package contains 52 benchmarks, organized into four suites»**;
  **«The SPECspeed® 2026 Integer and SPECspeed® 2026 Floating Point suites are used for comparing time
  for a computer to complete single tasks. The SPECrate® 2026 Integer and SPECrate® 2026 Floating Point
  suites measure the throughput or work per unit of time.»** (Es la misma pareja tiempo de
  respuesta / productividad de la UCM.)
- **«using workloads developed from real user applications»**; **«SPEC CPU 2026 also includes an
  optional metric for measuring energy consumption.»**
- SPEC CPU 2017 (43 pruebas) se retira: **«On November 3, 2026 03:00 AM US Eastern Time, SPEC will stop
  accepting SPEC CPU 2017 results for publication. By end of day on November 17, 2026 US Eastern Time,
  SPEC will retire SPEC CPU 2017.»** A 24-IX-2026 conviven las dos; decir que la 2026 es la nueva y la
  2017 está en retirada. **No confirmado**: fecha exacta de publicación de SPEC CPU 2026 (la página no
  la da en texto).

**Benchmarks del puesto de usuario** (ejemplos, cada uno en su web):

- Procesador y gráfica por render, «aplicación real»: Maxon: **«Cinebench 2026 utilizes the power of
  Redshift, Cinema 4D's default rendering engine, to evaluate your computer's CPU and GPU
  capabilities»**; **«Cinebench offers a real-world benchmark»**.
- Gráfica 3D/juegos: UL: **«3DMark includes everything you need to benchmark gaming performance in one
  app.»**; **«3DMark helps you relate your score to real-world game performance by estimating the frame
  rates you can expect»**.
- Sistema completo, sintético: PassMark PerformanceTest: **«Compare the performance of your PC to
  similar computers around the world.»**; **«Measure the effect of configuration changes and hardware
  upgrades.»**; pruebas de CPU, gráficos 2D (**«Word Processing, Web browsing and CAD drawing»**) y 3D.
- Disco: **«CrystalDiskMark is a simple disk benchmark software.»**; **«Measure Sequential and Random
  Performance (Read/Write/Mix)»**.
- Integrado en Windows: **«The winsat mem command tests system memory bandwidth using a process similar
  to the large memory-to-memory buffer copies in multimedia processing.»** (Microsoft Learn; aplica a
  Windows 10 y 11.)

### 2.6 Mantenimiento

**No investigado con fuente**: mantenimiento preventivo (limpieza, pasta térmica, ventilación,
actualización de BIOS/firmware y controladores). Las únicas citas disponibles: Canon sobre piezas de
desgaste de la impresora láser (tema 4); HP agrupa una familia de pitidos como **«Thermal»**. El
redactor debe declarar el hueco o pedir una fase corta.

---

## TEMA 3 · Sistemas de almacenamiento y recuperación de información

Enunciado: «Sistemas de almacenamiento y recuperación de información: discos duros, discos de estado
sólido, memorias flash, sistemas SAN y NAS; herramientas software de copia de seguridad, compresión de
datos y clonación de discos; recuperación de datos en caso de borrado accidental, avería o ataque de
virus.»

Cubierto por RTVE: HDD/SSD/cinta, RAID, DAS/NAS/SAN, NVMe en tabla, tipos de copia, regla 3-2-1,
prueba de restauración (Ing. Sup. Teleco 18; TI 15; TI 17 § 4; GA 08 § 4). **Falta: memorias flash
(tarjetas, desgaste, TRIM), NVMe vigente, herramientas de copia, compresión y clonación, y
recuperación tras borrado, avería o virus.** Fuentes nuevas:

| Fuente | Fichero | Leída |
|---|---|---|
| NVM Express, «About» y «Specifications» | `nvme-about.txt`, `nvme-specs.txt` | 05-10-2026 |
| SD Association, «Capacity (SD/SDHC/SDXC/SDUC)» y «Speed Class» | `sda-capacity.txt`, `sda-speed-class.txt` | 05-10-2026 |
| SNIA, *Online Dictionary*: flash memory, wear leveling, trim, write amplification, garbage collection, over-provisioning, solid state storage, storage area network; página «What is NAS» | `snia-dict-*.txt`, `snia-nas.txt` | 05-10-2026 |
| Microsoft Learn, «fsutil behavior» (TRIM en Windows) | `ms-fsutil-behavior.txt` | 05-10-2026 |
| Microsoft Learn, «robocopy» (act. 2025-03-17), «wbadmin start backup» (2023-02-03), «vssadmin» (2026-09-08), «compact» (2023-02-03), «tar on Windows» (2026-06-02), «Controlled folder access» (2026-07-17) | `ms-robocopy.txt`, `ms-wbadmin-start-backup.txt`, `ms-vssadmin.txt`, `ms-compact.txt`, `ms-tar-windows.txt`, `ms-controlled-folders.txt` | 05-10-2026 |
| Microsoft Support, KB5032038 «Overview of Windows Backup…»; «Zip and unzip files»; «Recuperación de archivos de Windows» — **sólo vía WebFetch** (support.microsoft.com bloquea la descarga directa) | — | 05-10-2026 |
| rsync, página de manual `rsync(1)` (samba.org) | `rsync-man.txt` | 05-10-2026 |
| GNU Coreutils, «dd invocation»; GNU gzip, manual; GNU tar, «Creating and Reading Compressed Archives» | `gnu-dd.txt`, `gnu-gzip.txt`, `gnu-tar-compress.txt` | 05-10-2026 |
| 7-Zip, página principal (versión 26.03, 2026-09-03) | `7zip.txt` | 05-10-2026 |
| Clonezilla, página principal | `clonezilla.txt` | 05-10-2026 |
| CGSecurity, «PhotoRec» y «TestDisk» | `photorec.txt`, `testdisk.txt` | 05-10-2026 |
| INCIBE, *Ransomware. Una guía de aproximación para el empresario* (INCIBE_PTE_AproxEmpresario_007_Ransomware-2020-v2) | `incibe-guia-ransomware.txt` | 05-10-2026 |
| No More Ransom, portada en español | `nomoreransom-es.txt` | 05-10-2026 |

### 3.1 Memorias flash y SSD

- SNIA: flash es **«A type of non-volatile memory used in solid state storage.»**; almacenamiento de
  estado sólido: **«A storage capability built using solid state electronics as the non-volatile
  storage medium.»**
- Desgaste: **«Wear leveling — A set of algorithms utilized by a flash controller to distribute writes
  and erases across the cells in a flash device. Cells in flash devices have a limited ability to
  survive write cycles. The purpose of wear leveling is to delay cell wear out and prolong the useful
  life of the overall flash device.»**
- **«Trim — A method by which the host operating system may inform a storage device of blocks of data
  that are no longer in use and no longer require logical to physical mapping resources. Many storage
  protocols support this functionality (e.g., ATA TRIM, NVMe Deallocate, and SCSI UNMAP).»**
- **«Write amplification — Increase in the number of write operations by the device beyond the number
  of write operations requested by hosts. […] In flash storage this may happen because of garbage
  collection.»**; sobreaprovisionamiento: **«The over provisioned capacity is reserved for controller
  use, is not addressable by the user, and is used to improve performance and device life.»**
- TRIM en Windows (Microsoft Learn, `fsutil behavior`): **«Delete notifications (also known as trim or
  unmap) is a feature that notifies the underlying storage device of clusters that have been freed due
  to a file delete operation.»**; **«For systems using NTFS, trim is enabled by default unless an
  administrator disables it.»** Órdenes: `fsutil behavior query disabledeletenotify` y `fsutil
  behavior set disabledeletenotify {1|0}`.
- **No confirmado en fuente primaria**: SLC/MLC/TLC/QLC (1, 2, 3, 4 bits por celda) y sus ciclos de
  programación y borrado. Kingston (fabricante) bloqueó la descarga (403); sólo constan en resúmenes del
  buscador y blogs. **No afirmar** que TRIM impida recuperar lo borrado en un SSD: ninguna fuente leída
  lo dice.

**NVMe** (NVM Express):

- **«NVM Express (NVMe) Specification – The register interface and command set for PCI Express
  technology attached storage […] NVMe is widely considered the defacto industry standard for PCIe
  SSDs.»**
- **«It is the industry standard for solid state drives (SSDs) in all form factors (U.2, M.2, AIC,
  EDSFF).»**; transportes: **«PCI Express® (PCIe®), RDMA, TCP and more»**.
- Versión vigente: **«The latest versions in the NVMe set of specifications were released on August 4,
  2026.»**; **«The NVMe 2.4 specifications consists of multiple documents»**. (RTVE no da versión; a
  24-IX-2026 la vigente es la 2.4.)
- **«The original NVM Express Work Group was incorporated as NVM Express in 2014»**; **«over 100 member
  companies»**.

**Tarjetas SD** (SD Association):

- Capacidades y sistema de ficheros, literal: **«SD standard – Up to 2GB SD memory card using FAT 12
  and 16 file systems»**; **«SDHC standard – over 2GB-32GB SDHC memory card using FAT32 file
  system»**; **«SDXC standard – over 32GB-2TB SDXC memory card using exFAT file system»**; **«SDUC
  standard – over 2TB-128TB SDUC memory card using exFAT file system»**.
- Clases de velocidad: **«The Speed Classes defined by the SD Association are Class 2, 4, 6 and 10.»**;
  **«UHS Speed Class 1 (U1) and UHS Speed Class 3 (U3)»**; **«The Video Speed Classes defined by the SD
  Association are V6, 10,30,60 and 90.»** **No confirmado**: la velocidad mínima en MB/s de cada clase
  (la página no la da en texto; está en imagen).
- **«Founded in January 2000 by Panasonic, SanDisk and Toshiba (now KIOXIA)»**.

**Memorias USB**: no investigado aparte (velocidades en tema 4, 4.1).

### 3.2 NAS y SAN (complemento de RTVE)

- SNIA, NAS: **«A term used to refer to storage devices that connect to a network and provide file
  access services to computer systems. These devices generally consist of an engine that implements the
  file services, and one or more devices, on which data is stored. NAS uses file access protocols such
  as NFS or CIFS.»**
- SNIA, SAN: **«A network whose primary purpose is the transfer of data between computer systems and
  storage devices and among storage devices.»**; **«The term SAN is usually (but not necessarily)
  identified with block services.»** (Matiz frente a RTVE 17 § 4, que la da como «protocolo de
  bloques» sin salvedad: conviene añadir el «usually (but not necessarily)».)

### 3.3 Herramientas de copia de seguridad

**Windows**

- **Copia de seguridad de Windows** (KB5032038, vía WebFetch): **«a system component to Back up your
  Windows PC»** que **«provides a solution for users to back up certain files and folders, as well as
  settings, credentials, and apps to the cloud»**; instalada por las actualizaciones **«released on and
  after August 22, 2023»**. Salvedad clave en una empresa: sólo **«for users that log-in with a MSA
  account and not for Microsoft Entra ID (formerly known as Azure AD) or Active Directory (AD)
  users»**. Cotejar en la página antes de copiar.
- **wbadmin start backup**: **«Creates a backup using specified parameters. […] If parameters are
  specified, it creates a Volume Shadow Copy Service (VSS) copy backup»**; requiere **«the Backup
  Operators group or the Administrators group»**; destino por defecto
  **«\\<servername>\<sharename>\WindowsImageBackup\<ComputerBackedUp>\»**. Aplica a Windows 10 y 11.
- **robocopy**: **«Copies file data from one location to another.»** Opciones: `/s` **«Copies
  subdirectories. This option automatically excludes empty directories.»**; `/e` **«… includes empty
  directories.»**; `/z` **«Copies files in restartable mode.»**; `/b` **«Copies files in backup mode.
  In backup mode, robocopy overrides file and folder permission settings (ACLs)»**; `/mir` **«Mirrors
  a directory tree (equivalent to /e plus /purge).»** Ejemplo literal de la página: `robocopy
  C:\Users\Admin\Records D:\Backup /MIR /R:2 /W:5 /LOG:C:\Logs\Backup.log`.
- **Instantáneas (VSS)**: `vssadmin` **«Shows current volume shadow copy backups and all installed
  shadow copy writers and providers.»**; `vssadmin list shadows` **«Lists existing volume shadow
  copies.»**; `vssadmin delete shadows` **«Deletes volume shadow copies.»**
- **No confirmado**: Historial de archivos (File History) y «Copias de seguridad y restauración
  (Windows 7)» en Windows 11 vigente; no leí su página.

**Linux**

- **rsync**: **«Rsync is a fast and extraordinarily versatile file copying tool. It can copy locally,
  to/from another host over a remote shell, or to/from a remote rsync daemon. […] It is famous for its
  delta-transfer algorithm, which reduces the amount of data sent over the network by sending only the
  differences between the source files and the existing files in the destination. Rsync is widely used
  for backups and mirroring»**. (El tema 9 del bloque B pide «salvaguarda y restauración» en Linux:
  conviene repartir.)

### 3.4 Compresión de datos

- **gzip** (GNU): **«gzip reduces the size of the named files using Lempel–Ziv coding (LZ77).»**;
  **«gzip uses the Lempel–Ziv algorithm used in zip and PKZIP.»**; **«Typically, text such as source
  code or English is reduced by 60–70%.»**; peor caso: **«an expansion ratio of 0.015% for large
  files»**.
- **7-Zip**: **«7-Zip is a file archiver with a high compression ratio.»**; **«High compression ratio
  in 7z format with LZMA and LZMA2 compression»**; **«Packing / unpacking: 7z, XZ, BZIP2, GZIP, TAR,
  ZIP and WIM»**; RAR sólo descomprime; **«For ZIP and GZIP formats, 7-Zip provides a compression ratio
  that is 2-10 % better than the ratio provided by PKZip and WinZip»**; licencia: **«The most of the
  code is under the GNU LGPL license.»**; uso libre en empresa: **«You can use 7-Zip on any computer,
  including a computer in a commercial organization.»** Versión del día: **«7-Zip 26.03
  (2026-09-03)»**.
- **Windows 11** («Zip and unzip files», vía WebFetch): **«Windows 11, version 24H2 supports ZIP, RAR.
  7z and TAR archive formats.»**; **«it does not support operations on encrypted archive files.»**
  `tar` incluido (Microsoft Learn, 2026-06-02): **«tar is a command-line archiving tool that's
  included with Windows. It lets you create, list, and extract archive files — including .tar,
  .tar.gz, .zip, and .7z»**; **«based on libarchive's bsdtar»**.
- **Compresión NTFS** (`compact`): **«Displays or alters the compression of files or directories on
  NTFS partitions.»**; algoritmos de `/EXE`: **«XPRESS4K (fastest and default value)»**, XPRESS8K,
  XPRESS16K, **«LZX (most compact)»**.
- **No confirmado con fuente**: la distinción compresión sin pérdida / con pérdida (para ficheros
  ofimáticos y copias siempre sin pérdida). Hay base en RTVE TI 18 § 3 (compresión de audio): el
  redactor puede tomarla de allí.

### 3.5 Clonación de discos

- **Clonezilla**: **«Clonezilla is a partition and disk imaging/cloning program similar to True
  Image® or Norton Ghost®. It helps you to do system deployment, bare metal backup and recovery.»**;
  tres variantes: **«Clonezilla live, Clonezilla lite server, and Clonezilla SE (server edition).
  Clonezilla live is suitable for single machine backup and restore.»**; **«Clonezilla saves and
  restores only used blocks in the hard disk.»**; para sistemas de ficheros no admitidos, **«sector-to-
  sector copy is done by dd»**; **«Both MBR and GPT partition formats of hard drive are supported.
  Clonezilla live also can be booted on a BIOS or uEFI machine.»**; **«AES-256 encryption could be
  used»**; restricción: **«The destination partition must be equal or larger than the source one.»**;
  despliegue masivo por **«multicast»** (SE) y **«Bittorrent»** (lite server); con drbl-winroll **«the
  hostname, group, and SID of cloned MS windows machine can be automatically changed.»**
- **dd** (GNU): **«dd copies input to output with a changeable I/O block size, while optionally
  performing conversions on the data.»**; rescate de un disco que falla: **«the operand
  ‘conv=noerror,sync’ is used to continue after read errors and to pad out bad reads with NULs»**;
  ejemplo literal: `dd conv=noerror,sync iflag=fullblock </dev/sda1 > /mnt/rescue.img` (**«Rescue data
  from an (unmounted!) partition of a failing device.»**); y **«For failing storage devices, other
  tools come with a great variety of extra functionality […] e.g. GNU ddrescue.»**
- Tras clonar a un disco nuevo, `chkdsk /b` (tema 2, 2.2).

### 3.6 Recuperación de datos

**Borrado accidental**

- Por qué se puede (PhotoRec): **«When a file is deleted, the meta-information about this file (file
  name, date/time, size, location of the first data block/cluster, etc.) is lost […] This means the
  data is still present on the file system, but only until some or all of it is overwritten by new
  file data.»**
- Regla de oro (PhotoRec): **«As soon as a picture or file is accidentally deleted, or you discover any
  missing, do NOT save any more pictures or files to that memory device or hard disk drive; otherwise
  you may overwrite your lost data. This means that while using PhotoRec, you must not choose to write
  the recovered files to the same partition they were stored on.»** Microsoft dice lo mismo
  (WebFetch): **«Minimiza o evita usar el equipo»** porque **«cualquier uso de su equipo puede crear
  archivos, lo que puede sobrescribir este espacio libre en cualquier momento.»**
- **Recuperación de archivos de Windows** (`winfr`, vía WebFetch, cotejar): aplicación de línea de
  órdenes de Microsoft Store para Windows 10 y 11; sintaxis **«winfr source-drive: destination-drive:
  [/mode] [/switches]»**; modo normal (**«la opción de recuperación estándar para unidades NTFS no
  dañadas»**) y extenso (**«adecuada para todos los sistemas de archivos»**); NTFS borrado
  recientemente → normal; borrado hace tiempo, tras formatear o disco dañado, y FAT/exFAT → extenso.
- **PhotoRec**: **«PhotoRec ignores the file system and goes after the underlying data, so it will
  still work even if your media's file system has been severely damaged or reformatted.»**; **«PhotoRec
  uses read-only access»**; **«PhotoRec searches for known file headers.»**; **«more than 480 file
  extensions»**; licencia **GPL v2+**.
- **TestDisk**: **«primarily designed to help recover lost partitions and/or make non-booting disks
  bootable again when these symptoms are caused by faulty software: certain types of viruses or human
  error (such as accidentally deleting a Partition Table).»**; **«Undelete files from FAT, exFAT, NTFS
  and ext2 filesystem»**.
- **Versiones anteriores / instantáneas**: véase VSS (3.3) e INCIBE (abajo). **No confirmado**:
  Papelera de reciclaje y «Versiones anteriores» del Explorador con página de Microsoft.

**Avería física**

- dd con `conv=noerror,sync` o GNU ddrescue (3.5): primero se saca imagen y se trabaja sobre la
  imagen. SMART y chkdsk /r (tema 2). **No confirmado**: laboratorios de recuperación y sala blanca
  (sin fuente).

**Ataque de virus / ransomware** (INCIBE, guía 2020 v2, § 3.2.1 y § 4):

- Copias: **«la principal medida de seguridad que va a permitirnos recuperar la actividad de nuestra
  empresa en poco tiempo, es realizar copias de seguridad o backups»**; **«Haz y conserva al menos
  tres copias de seguridad actualizadas y en distintos soportes.»** (ejemplo: **«disco duro específico
  para copias, USB externo y nube»**); **«Guarda las copias de seguridad en un lugar diferente al del
  servidor de ficheros.»**; nube: **«algunas familias de ransomware también cifran y bloquean las copias
  de seguridad en la nube, por lo que es conveniente desactivar la sincronización persistente.»**;
  **«Comprueba regularmente que las copias de seguridad que tienes almacenadas funcionan correctamente
  […] hay que probar a restaurar algunos ficheros cada cierto tiempo.»**
- **«No pagar nunca el rescate, ya que esto no garantiza que puedas recuperar la información ni que no
  vuelvan a exigirte un segundo rescate.»**
- Las cinco etapas (ilustración 5): **«AÍSLA», «CLONA», «DESINFECTA», «INTENTA RECUPERAR»,
  «RESTAURA»**. Literal de cada paso:
  1. **«Aísla el equipo de la red: esto evitará que el ciberataque se propague a otros
     dispositivos.»**; **«Cambia inmediatamente todas las contraseñas de red y de cuentas online.»**
  2. **«Clona el disco duro: se recomienda realizar una clonación completa del disco. De esta manera,
     podrás mantener el dispositivo original y así intentar recuperar los datos sobre el clon. Si no
     existiera solución a día de hoy, es posible que en el futuro sí la haya»**; conectar el disco a
     otro equipo aislado **«y no arranques con él, utilízalo de «esclavo»»**, salvando **«solo los datos
     importantes (documentos, fotos, certificados…) y no archivos ejecutables»**.
  3. **«Desinfecta el disco clonado […] Es muy importante eliminar el software malicioso y sus
     posibles persistencias antes de recuperar los datos, ya que si no se hace, podrían volver a ser
     cifrados.»**
  4. **«Recupera y restaura los equipos»**: a) **«www.nomoreransom.org […] un proyecto colaborativo
     avalado por la EUROPOL»**, sección **«Crypto-sheriff»**, con **«dos ficheros cifrados o la nota de
     rescate»**; si no hay solución, **«conserva el disco cifrado por si apareciera una solución en el
     futuro»**; b) **«Revisa si el sistema de ficheros del sistema operativo cuenta con shadow copy o
     snapshot, que mantienen copias de versiones anteriores de ficheros.»**; al final, **«utiliza un
     disco nuevo o formateado, además de una instalación en limpio del sistema operativo, y restaura la
     copia de seguridad más reciente anterior a la infección.»**
  - Denuncia: **«Guardia civil – Grupo de delitos telemáticos»**, **«Policía Nacional – Brigada de
    Investigación Tecnológica (BIT)»**. Línea de Ayuda en Ciberseguridad de INCIBE (el número 017 no
    consta en el texto leído: no darlo sin fuente).
- No More Ransom (portada): **«Por el momento, no todos los tipos de ransomware tienen solución.»**;
  **«La recomendación general es no pagar el rescate.»**
- Prevención en el puesto: Acceso controlado a carpetas de Microsoft Defender (Microsoft Learn,
  2026-07-17): **«Controlled folder access (CFA) in Microsoft Defender Antivirus helps protect your
  files from ransomware threats.»**; **«CFA counters this threat by allowing only trusted apps to change
  files in protected folders.»** (Antivirus en detalle: tema 14.)
- **Cuidado**: la notificación a la AEPD en 72 horas que dan los resúmenes del buscador no está en la
  guía leída; es del RGPD (tema común de protección de datos). Si se cita, desde allí.

---

## TEMA 1 · Sistema de información, arquitectura y componentes del equipo

Enunciado: «Elementos constitutivos de un sistema de información: características y funciones.
Arquitectura de ordenadores, componentes internos de los equipos microinformáticos y tecnologías
actuales aplicables al puesto de usuario.»

Cubierto por RTVE: von Neumann, buses, periféricos, generaciones (TI 17 § 1-3); hardware y software
del puesto (GA 08 § 1-2). **Falta: elementos y funciones de un sistema de información; componentes
internos con algo más de detalle; tecnologías actuales del puesto.** Fuentes nuevas:

| Fuente | Fichero | Leída |
|---|---|---|
| D. Bourgeois et al., *Information Systems for Business and Beyond* (2019), libro de texto universitario abierto (Saylor Foundation / eCampusOntario, CC BY-NC 4.0), cap. 1 y 2 | `bourgeois-isbb-2019.txt` | 05-10-2026 |
| Microsoft Learn, «Windows 11 requirements» (act. 2026-07-14) | `ms-win11-requirements.txt` | 05-10-2026 |
| Microsoft Learn, «Copilot+ PCs developer guide» (act. 2025-11-17) | `ms-copilot-pc-npu.txt` | 05-10-2026 |
| Microsoft Learn, ciclo de vida «Windows 10 Home and Pro» | `ms-win10-lifecycle.txt` | 05-10-2026 |

### 1.1 Elementos constitutivos de un sistema de información

**Definiciones** (las recoge Bourgeois, cap. 1, con su autor; el redactor traduce):

- Laudon y Laudon, *Management Information Systems*, 13.ª ed. (2014): **«An information system (IS)
  can be defined technically as a set of interrelated components that collect, process, store, and
  distribute information to support decision making and control in an organization.»** → las cuatro
  **funciones**: recoger (entrada), procesar, almacenar y distribuir (salida).
- Valacich y Schneider (2010): **«Information systems are combinations of hardware, software, and
  telecommunications networks that people build and use to collect, create, and distribute useful
  data, typically in organizational settings.»**
- Laudon y Laudon, 12.ª ed. (2012): **«Information systems are interrelated components working
  together to collect, process, store, and disseminate information to support decision making,
  coordination, control, analysis, and visualization in an organization.»**

**Elementos** (Bourgeois, cap. 1):

- **«Information systems can be viewed as having five major components: hardware, software, data,
  people, and processes. The first three are technology. […] The last two components, people and
  processes, separate the idea of information systems from more technical fields, such as computer
  science.»**
- **Hardware**: **«Hardware is the tangible, physical portion of an information system – the part you
  can touch.»**
- **Software**: **«Software comprises the set of instructions that tell the hardware what to do.
  Software is not tangible»**; **«Two main categories of software are: Operating Systems and
  Application software. Operating Systems software provides the interface between the hardware and the
  Application software.»**
- **Datos**: **«You can think of data as a collection of facts.»**; **«Pieces of unrelated data are not
  very useful. But aggregated, indexed, and organized together into a database, data can become a
  powerful tool»**.
- **Comunicaciones** (sexto elemento que se propone): **«it has been suggested that one other component
  should be added: communication. […] Technically, the networking communication component is made up
  of hardware and software, but it is such a core feature of today's information systems that it has
  become its own category.»**
- **Personas**: **«From the front-line user support staff, to systems analysts, to developers, all the
  way up to the chief information officer (CIO), the people involved with information systems are an
  essential element.»** (El operador informático está en la primera línea: soporte al usuario.)
- **Procesos**: **«A process is a series of steps undertaken to achieve a desired outcome or goal.»**

**Características**: **no encontré fuente** que enumere «características» de un sistema de información
como lista cerrada (integridad, disponibilidad, fiabilidad…). Lo de seguridad (confidencialidad,
integridad, disponibilidad) está en RTVE GA 08 § 5.1 y en el tema 14. Hueco a declarar.

### 1.2 Componentes internos del equipo (complemento de RTVE)

Bourgeois, cap. 2 (2019; ojo a lo datado, véase abajo):

- **CPU**: **«The core of a computer is the Central Processing Unit, or CPU. It can be thought of as the
  "brains" of the device. The CPU carries out the commands sent to it by the software and returns
  results to be acted upon.»**; **«The speed ("clock time") of a CPU is measured in hertz.»**; núcleos:
  **«today's CPU chips contain multiple processors. These chips, known as dual-core (two processors) or
  quad-core (four processors), increase the processing power»**.
- **Placa base**: **«The motherboard is the main circuit board on the computer. The CPU, memory, and
  storage components, among other things, all connect into the motherboard.»**; **«Most modern
  motherboards have many integrated components, such as network interface card, video, and sound
  processing, which previously required separate components.»**
- **Bus**: **«the term bus refers to the electrical connections between different computer
  components»**; **«the combination of how fast the bus can transfer data and the number of data bits
  that can be moved at one time determine the speed.»**
- **RAM**: **«This working memory, called Random-Access Memory (RAM), can transfer data much faster than
  the hard disk. Any program that you are running on the computer is loaded into RAM for processing.»**;
  **«Another characteristic of RAM is that it is "volatile."»**; **«RAM is generally installed in a
  personal computer through the use of a Double Data Rate (DDR) memory module. The type of DDR accepted
  into a computer is dependent upon the motherboard.»**
- **Tarjeta de red**: **«These cards were known as Network Interface Cards (NIC). By the mid-1990s an
  Ethernet network port was built into the motherboard on most personal computers.»**
- **SSD**: **«the SSD uses flash memory that incorporates EEPROM (Electrically Erasable Programmable
  Read Only Memory) chips»**; **«SSDs are considered more reliable since there are no moving parts.»**
- **Ley de Moore**: Bourgeois la da como **«The number of integrated circuits on a chip doubles every two
  years.»** y dice que en 1965 Moore observó **«microprocessor transistor counts had been doubling every
  year.»** **Inexacto en la fuente** (lo que se duplica son transistores, no «circuitos integrados», y
  en 1965 no había microprocesadores): **no copiar esa frase**; si se cita la ley, buscar fuente de
  Intel.
- **Datado en la fuente, no copiar como vigente**: «four generations of DDR: DDR1, DDR2, DDR3, and
  DDR4» (ya existe DDR5); «Core i9 processors contain 16 cores»; «USB 3.1» a 10 Gbit/s (hoy «USB
  10Gbps», véase tema 4). **No confirmado** con fuente primaria: DDR5 (JEDEC JESD79-5 bloqueó la
  descarga) ni generaciones PCIe (pcisig.com no descargable; **[SÓLO BUSCADOR]** PCIe 7.0 publicada a
  socios el 11-VI-2025, 128 GT/s). Sí consta, en fuentes leídas: **PCI Express Gen 4** dentro de
  Thunderbolt 5 (Intel) y NVMe como interfaz de SSD sobre PCIe (tema 3).
- Fuente de alimentación, disipación, chipset, firmware: **sin fuente leída** salvo lo de AMI (tema 2:
  bloque de arranque, CMOS) y el requisito UEFI de Windows 11 (abajo).

### 1.3 Tecnologías actuales aplicables al puesto de usuario

- **Requisitos de Windows 11** (Microsoft Learn, act. 14-VII-2026), literal: **«Processor: 1 gigahertz
  (GHz) or faster with two or more cores on a compatible 64-bit processor or system on a chip (SoC).»**;
  **«Memory: 4 gigabytes (GB) or greater.»**; **«Storage: 64 GB or greater available disk space.»**;
  **«Graphics card: Compatible with DirectX 12 or later, with a WDDM 2.0 driver.»**; **«System
  firmware: UEFI, Secure Boot capable.»**; **«TPM: Trusted Platform Module (TPM) version 2.0.»**;
  **«Display: High definition (720p) display, 9" or greater monitor, 8 bits per color channel.»**;
  **«Windows 11 Home edition requires an internet connection and a Microsoft Account to complete device
  setup on first use.»** Requisitos de funciones: Hyper-V cliente **«requires a processor with
  second-level address translation (SLAT)»**; **«BitLocker to Go: requires a USB flash drive»**;
  **«DirectStorage: requires an NVMe SSD»**. (Enlaza con el tema 6.)
- **Fin de Windows 10** (ciclo de vida): **«Windows 10 will reach end of support on October 14, 2025.
  The current version, 22H2, will be the final version of Windows 10»**; **«Existing LTSC releases will
  continue to receive updates beyond that date based on their specific lifecycles.»** A 24-IX-2026 el
  puesto vigente es Windows 11. **No confirmado**: el programa de actualizaciones extendidas (ESU) de
  Windows 10 (no leí su página).
- **NPU y Copilot+ PC** (Microsoft Learn, act. 17-XI-2025): **«Copilot+ PCs are a new class of Windows
  11 hardware powered by a high-performance Neural Processing Unit (NPU) — a specialized computer chip
  for AI-intensive processes like real-time translations and image generation—that can perform more
  than 40 trillion operations per second (TOPS).»**; **«The NPU works in alignment with the CPU and GPU.
  Windows 11 assigns processing tasks to the most appropriate place»**; **«NPUs are designed specifically
  to execute the deep learning math operations that make up AI models.»**; plataformas: Qualcomm
  Snapdragon X (Arm), **«AMD Ryzen AI 300 series and Intel Core Ultra 200V series»**.
- **Conectividad del puesto** (detalle en tema 4): un solo puerto USB-C para datos, vídeo y carga
  (USB4 hasta 80 Gbit/s, USB PD hasta 240 W, Thunderbolt 4/5); el monitor que alimenta el portátil
  (USB-IF, cita en 4.1); impresión sin controlador por IPP/Mopria (4.4).
- **Almacenamiento del puesto**: SSD NVMe (tema 3).
- **No investigado aquí**: Wi-Fi 6/7 (tema 13), escritorio virtual y cliente ligero (tema 10).

---

## Lo que no pude confirmar (resumen)

| Tema | Dato | Por qué |
|---|---|---|
| 1 | «Características» de un sistema de información como lista | sin fuente que la dé |
| 1 | DDR5, generaciones PCIe | jedec.org y pcisig.com bloquean la descarga |
| 1 | Ley de Moore con fuente fiable | Bourgeois la da mal; falta fuente de Intel |
| 1 | ESU de Windows 10 | página no leída |
| 2 | Mensajes de texto de BIOS, Award/Phoenix, códigos UEFI | sin fuente primaria |
| 2 | Tabla de pitidos Dell | sólo por WebFetch (resumen de modelo): cotejar |
| 2 | Significado de los códigos HP; diagnóstico UEFI de HP | support.hp.com 503; el PDF es interactivo |
| 2 | Diagnóstico de memoria de Windows (mdsched); ESD; mantenimiento preventivo | no leídos |
| 3 | SLC/MLC/TLC/QLC y ciclos P/E | Kingston 403; sólo blogs |
| 3 | Velocidad mínima de las clases SD | en imagen, no en texto |
| 3 | Historial de archivos; Papelera; Versiones anteriores | no leídos |
| 3 | Que TRIM impida recuperar en SSD | ninguna fuente leída lo dice |
| 3 | KB5032038, «Zip and unzip files», winfr | sólo por WebFetch: cotejar |
| 4 | Patillaje DE-15 y DDC/EDID | sólo Wikipedia y comercios |
| 4 | Matricial, térmica, PCL/PostScript, ppp | sin fuente primaria descargable |
| 4 | Ediciones vigentes ISO/IEC 24734, 19752, 24711 | iso.org 403 |
| 4 | Carga de Thunderbolt 4/5 en W | resúmenes contradictorios; la nota de Intel no lo da |
| 4 | CIS/CCD, OCR, ADF; paneles de monitor; multimedia | sin fuente primaria |
| 4 | Nombres «Low/Full Speed» de USB 2.0 | la guía dice «Basic-Speed» |

## Ficheros tocados

- Creado: `informes/canal-sur-especificos/29-investigacion-A-hardware.md` (este informe).
- Creada la carpeta `fuentes/canal-sur/informatico/web/` con las copias de las fuentes citadas.
- Ningún otro fichero del repositorio modificado.
