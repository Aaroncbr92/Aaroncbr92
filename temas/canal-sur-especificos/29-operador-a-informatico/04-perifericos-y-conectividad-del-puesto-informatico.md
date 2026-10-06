# Tema 4 del específico de Operador/a Informático · Periféricos y conectividad del puesto informático

<!-- portada -->

|  |  |
| --- | --- |
| Bloque | Temario específico de Operador/a Informático · punto 4 |
| Sirve para | Operador/a Informático de Canal Sur (grupo B04): teoría específica y aplicación práctica del test, y la prueba práctica del puesto |
| Fuente | Sin norma jurídica. USB Implementers Forum (USB-IF: guías de nombres y logotipos, páginas de USB4, USB Type-C y USB Power Delivery, lista de códigos de clase); Intel y Thunderbolt Technology Community; Digital Display Working Group, *Digital Visual Interface, Revision 1.0* (1999); HDMI Licensing Administrator (páginas de las especificaciones HDMI 1.4b y 2.2 y de los cables); VESA (nota de 17-10-2022 sobre DisplayPort 2.1 y página de DisplayPort); MIT, curso 6.111, y Cornell, ECE 4760 (VGA); norma SMPTE ST 2059-1:2021 (reloj de 720p); Fluke Networks (T568A y T568B); Canon, Epson, Zebra y HP (impresión y escaneo); Printer Working Group (IPP Everywhere); Microsoft Learn y Soporte de Microsoft (controladores de clase USB, fin de los controladores de impresora de terceros, impresión protegida, WIA, varios monitores); manual universitario abierto de D. Bourgeois et al. (2019). Lo demás, oficio declarado como tal |
| Redacción que se estudia | Las ediciones citadas, en línea el 05-10-2026 y leídas ese día (la SMPTE ST 2059-1:2021, el 06-10-2026) |
| Extensión | 9.000 palabras aproximadamente |

<!-- /portada -->

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA); Canal Sur Radio y
Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de Andalucía (BOJA); bus serie universal (USB,
*universal serial bus*), su foro de fabricantes (USB-IF, *USB Implementers Forum*) y su entrega de
energía (USB PD, *power delivery*); protocolo de almacenamiento USB conectado por SCSI (UASP, *USB
Attached SCSI Protocol*); dispositivo de interfaz humana (HID, *human interface device*); interfaz
visual digital (DVI, *digital visual interface*) y su grupo promotor (DDWG, *Digital Display Working
Group*); interfaz multimedia de alta definición (HDMI, *high-definition multimedia interface*), su
canal de retorno de audio (ARC, *audio return channel*) y el mejorado (eARC); matriz de gráficos de
vídeo (VGA, *video graphics array*) y su ampliación SVGA (*super VGA*); asociación de normas de
electrónica de vídeo (VESA, *Video Electronics Standards Association*); transporte de varios flujos
de DisplayPort (MST, *multi-stream transport*); compresión de flujo de pantalla (DSC, *display stream
compression*); tasa de bits ultra alta de DisplayPort (UHBR, *ultra-high bit rate*); modo alternativo
(*Alt Mode*), la manera de llevar DisplayPort o HDMI por un conector USB Type-C; señalización
diferencial con transiciones minimizadas (TMDS, *transition-minimized differential signaling*); canal
de datos de pantalla (DDC, *display data channel*) y datos de identificación de pantalla ampliados
(EDID, *extended display identification data*); detección de conexión en caliente (HPD, *hot plug
detect*); interfaz de bus PCI Express (PCIe); conector registrado 45 (RJ45); par trenzado sin
apantallar (UTP, *unshielded twisted pair*); las dos asignaciones de colores del cableado de red,
T568A y T568B, de la norma ANSI/TIA-568 (Instituto Nacional Estadounidense de Normalización, ANSI, y
Asociación de la Industria de las Telecomunicaciones, TIA); el esquema de cableado USOC
(*Universal Service Ordering Code*), con el que esas asignaciones guardan compatibilidad; dispositivo multifunción (MFP, *multifunction printer*); cian, magenta, amarillo y
negro (CMYK); rojo, verde y azul (RGB); protocolo de impresión por Internet (IPP, *Internet Printing Protocol*) y el grupo que
lo mantiene (PWG, *Printer Working Group*); descubrimiento de servicios por DNS (DNS-SD); petición de
comentarios del IETF (RFC); la asociación Mopria, que certifica impresoras para imprimir sin
controlador propio; servicios web para escáneres (WS-Scan) y protocolo de escaneo eSCL; adquisición
de imágenes de Windows (WIA, *Windows Image Acquisition*) y su base, la arquitectura de imagen fija
(STI, *still image architecture*); interfaz de programación de aplicaciones (API); el estándar de
captura TWAIN; dispositivo de carga acoplada (CCD, *charge-coupled device*), el sensor del escáner;
puntos por pulgada (ppp, en inglés *dpi*); norma internacional ISO/IEC (Organización Internacional de
Normalización y Comisión Electrotécnica Internacional); primera página impresa (FPOT, *first print out
time*) y las medidas de la ISO/IEC 24734, FSOT, EFTP y ESAT; páginas por minuto (ppm); interferencia
electromagnética (EMI); gigabit por segundo (Gbit/s, que las fuentes escriben Gbps) y megabit por
segundo (Mbit/s, Mbps); vatio (W), voltio (V) y amperio (A); megahercio (MHz); ohmio (Ω). Además: disco de estado sólido (SSD, *solid-state drive*); DisplayPort
(DP, en los nombres de cables y del conector Mini-DP); grupo conjunto de expertos en fotografía (JPEG,
*Joint Photographic Experts Group*) y su formato de fichero JFIF (*JPEG File Interchange Format*);
señalización diferencial de bajo voltaje (LVDS, *low-voltage differential signaling*); especificación de papel XML de Microsoft (XPS, *XML Paper
Specification*); código de respuesta rápida (QR, *quick response*); Instituto Tecnológico de
Massachusetts (MIT); Sociedad de Ingenieros de Cine y Televisión (SMPTE, *Society of Motion Picture
and Television Engineers*).

> Enunciado (BOJA núm. 186, de 24-IX-2026, Anexo V, puesto 2.29, punto 4): «Periféricos y
> conectividad del puesto informático: elementos de impresión, almacenamiento, visualización,
> digitalización y multimedia; conectividad USB, RJ45, VGA, DVI, HDMI y DisplayPort.»

Qué se puede preguntar: cómo se clasifica un periférico (entrada, salida, entrada y salida) y en qué
cajón va una pantalla táctil o un disco; qué es una clase de dispositivo USB, qué código tiene la de
impresora, almacenamiento masivo, audio, vídeo o HID y por qué Windows no pide controlador para
ellas. De impresión: las fases de la impresión láser, la diferencia entre inyección térmica y
piezoeléctrica, tinta de colorante y de pigmento, qué es una impresora de impacto, una térmica
directa y una de transferencia térmica; qué mide la ISO/IEC 24734 (FSOT, EFTP, ESAT); qué es IPP
Everywhere y Mopria, qué fechas tiene el fin de los controladores de impresora de terceros en Windows
y qué hace el modo de impresión protegida. Del almacenamiento externo: qué clase USB usa y qué es
UASP. De visualización: qué es la relación de aspecto, qué reloj de píxel exige cada resolución VGA y
qué modos de proyección ofrece Windows con Windows + P. De digitalización: resolución óptica, de
hardware e interpolada, profundidad de color y número de colores, WIA y TWAIN. De multimedia: cámaras,
micrófonos y altavoces por USB o Bluetooth. De conectividad: las cinco velocidades de USB y su nombre
comercial, USB 3.2 Gen 1, Gen 2 y Gen 2x2, qué es USB4, que Type-C es el conector y no la velocidad,
cuánta potencia da USB PD 3.1, Thunderbolt 4 y 5; cuántos hilos tiene un RJ45 y en qué se distinguen
T568A y T568B; qué señales lleva VGA, por qué conector y a qué nivel; los dos conectores de DVI, el
enlace sencillo hasta 165 MHz y el doble; qué aporta cada versión de HDMI (1.4b, 2.1, 2.2) y cada
cable; DisplayPort 2.1, DP40 y DP80, MST y el conector con retención; cuál de estas interfaces es
analógica, cuál lleva audio y cuál no. En la aplicación práctica: elegir cable y puerto para un
monitor, un proyector o una impresora, leer el rótulo de un cable USB-C, montar un latiguillo de red o
resolver por qué un segundo monitor no aparece.

<!-- indice -->

## Índice

- [1. Los periféricos del puesto informático](#1-los-periféricos-del-puesto-informático)
  - [Qué es un periférico y cómo se clasifica](#qué-es-un-periférico-y-cómo-se-clasifica)
  - [Cómo se conectan: cable o radio](#cómo-se-conectan-cable-o-radio)
  - [Cómo los reconoce Windows: las clases de dispositivo USB](#cómo-los-reconoce-windows-las-clases-de-dispositivo-usb)
- [2. Elementos de impresión](#2-elementos-de-impresión)
  - [La impresora láser](#la-impresora-láser)
  - [La impresora de inyección de tinta](#la-impresora-de-inyección-de-tinta)
  - [Impresoras térmicas y de impacto](#impresoras-térmicas-y-de-impacto)
  - [Cómo se mide la velocidad: la norma ISO/IEC 24734](#cómo-se-mide-la-velocidad-la-norma-isoiec-24734)
  - [La impresión sin controlador del fabricante: IPP, IPP Everywhere y Mopria](#la-impresión-sin-controlador-del-fabricante-ipp-ipp-everywhere-y-mopria)
  - [El modo de impresión protegida de Windows](#el-modo-de-impresión-protegida-de-windows)
- [3. Elementos de almacenamiento](#3-elementos-de-almacenamiento)
- [4. Elementos de visualización](#4-elementos-de-visualización)
  - [El monitor y la relación de aspecto](#el-monitor-y-la-relación-de-aspecto)
  - [Resolución, refresco y reloj de píxel](#resolución-refresco-y-reloj-de-píxel)
  - [Varios monitores en Windows](#varios-monitores-en-windows)
- [5. Elementos de digitalización](#5-elementos-de-digitalización)
  - [El escáner: tres resoluciones](#el-escáner-tres-resoluciones)
  - [La profundidad de color](#la-profundidad-de-color)
  - [Cómo habla Windows con el escáner: WIA y TWAIN](#cómo-habla-windows-con-el-escáner-wia-y-twain)
- [6. Elementos multimedia](#6-elementos-multimedia)
- [7. Conectividad del puesto](#7-conectividad-del-puesto)
  - [USB: tres cosas que no hay que mezclar](#usb-tres-cosas-que-no-hay-que-mezclar)
  - [USB: velocidades y nombres](#usb-velocidades-y-nombres)
  - [El conector USB Type-C](#el-conector-usb-type-c)
  - [USB Power Delivery](#usb-power-delivery)
  - [Thunderbolt](#thunderbolt)
  - [RJ45: la red cableada](#rj45-la-red-cableada)
  - [VGA](#vga)
  - [DVI](#dvi)
  - [HDMI](#hdmi)
  - [DisplayPort](#displayport)
  - [Las interfaces de vídeo, frente a frente](#las-interfaces-de-vídeo-frente-a-frente)
- [8. Aplicación práctica](#8-aplicación-práctica)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Los periféricos del puesto informático

### Qué es un periférico y cómo se clasifica

El ordenador necesita canales para recibir datos del usuario y para devolvérselos. El manual
universitario abierto de Bourgeois lo dice así: **«In order for a personal computer to be useful, it
must have channels for receiving input from the user and channels for delivering output to the
user.»** Y esos dispositivos se enchufan a puertos de la placa base accesibles desde fuera de la caja
(**«These input and output devices connect to the computer via various connection ports, which
generally are part of the motherboard and are accessible outside the computer case.»**).

La clasificación es de tres cajones y se decide por el sentido en que va la información:

| Clase | Qué hace | Ejemplos |
|---|---|---|
| De entrada | Mete información en el ordenador | Teclado, ratón, escáner, micrófono |
| De salida | Saca información del ordenador | Monitor, impresora, altavoz |
| De entrada y salida | Las dos cosas | Disco duro, memoria portátil, tarjeta de red, pantalla táctil |

La regla que la contesta sin dudar: hay que preguntarse si el dispositivo puede hacer las dos
cosas. Del disco se lee y en el disco se escribe; al monitor sólo se le escribe y del teclado
sólo se lee.

Y el aviso que evita el error más común: una pantalla táctil sí es de entrada y salida, y un
monitor corriente no. La misma familia de aparato cambia de cajón según lo que pueda hacer.

Bourgeois pone los ejemplos de cada lado. De entrada, el teclado y el ratón siguen siendo los
principales (**«These two components are still the primary input devices to a personal computer»**);
además, el escáner, que mete documentos como imagen o como texto, el micrófono y la cámara web
(**«Other input devices include scanners which allow users to input documents into a computer either
as images or as text. Microphones can be used to record audio or give voice commands. Webcams and
other types of video cameras can be used to record video or participate in a video chat session.»**).
De salida, la pantalla, que puede ser más de una o un proyector, los altavoces y la impresora
(**«In some cases, a personal computer can support multiple displays or be connected to
largerformat displays such as a projector or large-screen television. Other output devices include
speakers for audio output and printers for hardcopy output.»**).

Las cinco familias del enunciado se reparten así entre los tres cajones: impresión, salida (la
multifunción, que también escanea, es de entrada y salida); almacenamiento, entrada y salida;
visualización, salida (táctil, entrada y salida); digitalización, entrada; multimedia, de los tres
tipos (micrófono y cámara, entrada; altavoz, salida; auriculares con micrófono, los dos). El reparto
es aplicación de la regla anterior, no cita de una fuente.

### Cómo se conectan: cable o radio

Hoy casi todo entra por USB: **«Today, almost all devices plug into a computer through the use of a
USB port. This port type, first introduced in 1996, has increased in its capabilities, both in its
data transfer rate and power supplied.»** Sin cable, Bluetooth: **«Besides USB, some input and output
devices connect to the computer via a wireless-technology standard called Bluetooth which was invented
in 1994.»** Sus usos en el puesto, según la misma fuente: **«connecting a printer to a personal
computer, connecting a mobile phone and headset, connecting a wireless keyboard and mouse to a
computer»**. El alcance que da Bourgeois no es coherente: en un capítulo **«10 meters up to 100
meters»** y en otro **«approximately 300 feet»**; el tema no fija una cifra. Las impresoras y los
escáneres de red se conectan además por Ethernet (RJ45, epígrafe 7) o Wi-Fi (tema 13).

### Cómo los reconoce Windows: las clases de dispositivo USB

Un periférico USB dice qué es mediante un código de clase. El USB-IF lo explica: **«USB defines class
code information that is used to identify a device’s functionality and to nominally load a device
driver based on that functionality. The information is contained in three bytes with the names Base
Class, SubClass, and Protocol.»** Y Microsoft añade la consecuencia práctica: si el aparato es de una
clase que Windows conoce, carga su controlador de clase sin pedir nada más (**«If a device that
belongs to a supported device class is connected to a system, Windows automatically loads the class
driver, and the device functions with no other driver required.»**). Esos controladores **«are
included in Windows»** y **«are updated through Windows Update»**.

Las clases que tocan a este tema, con el controlador que Windows trae (Microsoft Learn, «USB
device class drivers included in Windows», actualizado el 13-06-2025):

| Código (clase base) | Clase según el USB-IF | Ejemplo en el puesto | Controlador de Windows |
|---|---|---|---|
| 01h | **Audio** | Auriculares, micrófono, altavoces USB | **Usbaudio.sys** |
| 03h | **HID (Human Interface Device)** | Teclado, ratón | **Hidclass.sys** y **Hidusb.sys** |
| 06h | **Image** (en el detalle, **Still Imaging**) | Escáner, cámara de fotos | **Usbscan.sys** |
| 07h | **Printer** | Impresora | **Usbprint.sys** |
| 08h | **Mass Storage** | Memoria USB, disco externo | **Usbstor.sys**; **Uaspstor.sys** para UASP |
| 09h | **Hub** | Concentrador USB | **Usbhub.sys**; **Usbhub3.sys** para concentradores SuperSpeed |
| 0Eh | **Video** | Cámara web | **Usbvideo.sys** |

Dos detalles de la fuente que se preguntan. La clase USB no es la categoría del Administrador de
dispositivos: un aparato de audio lleva el código 01h, Windows le carga Usbaudio.sys y lo muestra en la categoría de
sonido, vídeo y juegos, cuya clase de instalación es *Media* (**«an audio device has a USB device class code of 01h in its
descriptor. When connected to a system, Windows loads the Microsoft-provided class driver,
Usbaudio.sys. In Device Manager, the device is shown under Sound, video and game controllers»**). Y
UASP es el modo rápido del almacenamiento: **«Uaspstor.sys is the class driver for SuperSpeed USB
devices that support bulk stream endpoints.»** El controlador del escáner, Usbscan.sys, **«implements
the USB component of the Windows Imaging Architecture (WIA)»** (epígrafe 5).

El controlador de clase puede quedarse corto: **«Windows class drivers might not support all of the
features that are described in a class specification.»** Entonces el fabricante completa con un
controlador suplementario (**«vendors should provide supplementary drivers that work with the class
driver to support the entire range of functionality offered by the device»**).

## 2. Elementos de impresión

### La impresora láser

La láser es electrofotográfica (**«Laser printers are printers that use electrophotographic
technology.»**). Canon describe el proceso entero en un párrafo:

> **«The print command is converted into laser light, which is irradiated (exposed) onto a
> cylindrical photosensitive drum. The photosensitive drum is charged with static electricity
> beforehand, and the exposure causes the static electricity to dissipate only in the printed area
> (development). When the photosensitive drum is covered with powdered ink toner, the toner remains
> only in the area exposed to the laser beam, and the force of static electricity attracts
> (transfers) the toner onto the paper. Heat and pressure are applied to adhere (fix) the toner onto
> the paper, and printing is complete.»**

En castellano, las fases: se carga el tambor fotosensible con electricidad estática; el láser lo
expone y la carga desaparece sólo en lo que se va a imprimir; el tóner en polvo se queda en esa zona
(revelado); la electricidad estática lo pasa al papel (transferencia), y el calor y la presión lo
fijan (fijado). En la fijación, **«powdered toner is melted by a heat source and put
under pressure by a pressure roller, fixing it onto paper.»**

En color usa cuatro tóneres (**«When used in color printing, a toner produces printed images in the
four CMYK colors.»**). Sus piezas de desgaste son el tambor, el cargador electrostático y el limpiador,
además del tóner (**«require parts that are subject to wear and that require frequent maintenance,
such as a photosensitive drum, an electrostatic charger, and a cleaner, as well as toner in powder
form»**). Por eso Canon inventó en 1982 el cartucho integrado que se cambia de una vez con el tambor
(**«In 1982, Canon developed the world's first integrated toner cartridge system, in which the
toner, photosensitive drum, and other major components are replaced together.»**). Y la multifunción
es la láser con copia, escaneo y fax (**«Multifunction laser printers (MFPs) are laser printers
equipped with additional functions such as copying, scanning, and faxing.»**).

Un término de catálogo: FPOT, **«first print out time, or the time it takes for the first sheet of
media to be output»**, el tiempo hasta que sale la primera hoja.

### La impresora de inyección de tinta

Lanza gotas de tinta de picolitros (**«These droplets have volumes of mere picoliters (one trillionth
of a liter).»**). Hay dos mecanismos de expulsión:

> **«The thermal process (bubble jet process) uses a heater to create air bubbles in the ink, which
> pushes the ink out of the nozzle. In printers that use the piezoelectric process, voltage is
> applied to a piezoelectric element, which changes shape as a result. This compresses the ink,
> ejecting it from the nozzle.»**

| Mecanismo | Cómo expulsa la gota | Ventaja que da Canon |
|---|---|---|
| Térmico (burbuja) | Un calentador forma una burbuja que empuja la tinta | **«a more simple nozzle structure and a greater nozzle density»** |
| Piezoeléctrico | Un elemento piezoeléctrico se deforma con la tensión y comprime la tinta | **«the amount of ink that is ejected can be changed by adjusting the voltage that is applied»** |

Colores: **«cyan, magenta, and yellow, together with black»**. Dos clases de tinta: la de colorante,
disuelto (**«dye is dissolved at the molecular level»**), y la de pigmento, en partículas sin
disolver (**«remains in particle form, undissolved»**).

Epson, que fabrica la piezoeléctrica, la llama «sin calor» (**«Heat-Free printing is Epson's inkjet
technology that prints without using heat in the ink-delivery process. Traditional laser printers use
heat to fuse toner onto the page»**) y subraya que no deja tambores ni fusores que tirar (**«no toner
cartridges, drum units, or fuser assemblies to dispose of»**). Las cifras de ahorro eléctrico que
publica son publicidad del fabricante y el tema no las da.

### Impresoras térmicas y de impacto

Las térmicas son las de etiquetas, tiques y pulseras. Zebra, fabricante del ramo: **«Unlike inkjet or
dot matrix printers, thermal printers use a heated printhead to produce an image.»**; **«There are two
types of thermal printers: direct thermal and thermal transfer.»**

| Tipo | Cómo imprime | Consecuencia |
|---|---|---|
| Transferencia térmica | **«a heated printhead that applies that heat to a ribbon that has a wax or resin coating»**: la cera o la resina pasan de la cinta al soporte | Imagen duradera; admite **«paper, polyester, and polypropylene materials»** |
| Térmica directa | **«without using a ribbon, toner, or ink»**, sobre **«chemically treated, heat-sensitive media that blackens when it passes under the thermal printhead»** | Más sensible a la luz, al calor y al roce: **«Images can fade over time»** |

Ninguna de las dos usa tinta (**«Neither thermal transfer or direct thermal printers use ink.»**).

Las de impacto golpean una cinta entintada: **«Impact printers operate by striking a metal or plastic
head against an ink ribbon. Ex: dot matrix, daisy-wheel, and ball printers.»** La matricial es, pues, de
impacto; la fuente no describe más su funcionamiento y el tema tampoco.

### Cómo se mide la velocidad: la norma ISO/IEC 24734

La cifra de páginas por minuto de un folleto sólo compara si se mide igual. La ISO/IEC 24734 fija el
método (resumen de HP, 2009):

> **«ISO/IEC 24734 specifies a method for measuring the productivity of digital printing devices
> using varying test files, office applications, and print job characteristics on plain paper in
> default mode. It is applicable to black-and-white and color devices, and to single-function and
> multi-function devices, regardless of print technology (e.g. inkjet, laser, etc).»**

Sus tres medidas: **«First Set Out Time (FSOT)»**, el tiempo hasta el primer juego; **«Effective
Throughput (EFTP)»**, el rendimiento efectivo, y **«Estimated Saturated Throughput (ESAT)»**, el
rendimiento sostenido estimado. HP anuncia **«the average single-sided ESAT PPM»**. Y la velocidad
real depende de más cosas que la impresora: **«host computer, driver, application, operating system,
and type of connection to the printer (USB, Ethernet, wireless)»**. La edición vigente de la norma no
se ha podido leer (el sitio de ISO no se dejó descargar): el tema no la da.

### La impresión sin controlador del fabricante: IPP, IPP Everywhere y Mopria

Sobre el protocolo de impresión por Internet (IPP) se apoya la impresión sin el programa de cada
marca. El Printer Working Group define IPP Everywhere como **«A PWG standard that allows personal computers
and mobile devices to find and print to networked and USB printers without using vendor-specific
software.»** Exige **«IPP/2.0, DNS-SD, PWG Raster and JPEG JFIF file formats (JPEG only required for
color printers)»**: el ordenador descubre la impresora en la red por DNS-SD y le manda la página en un
formato común. La norma vigente de IPP/2.x es la **«PWG 5100.12-2024: Internet Printing Protocol/2.x Fourth
Edition»** y la versión cifrada va sobre HTTPS (**«RFC 7472: IPP over HTTPS Transport Binding and
'ipps' URI Scheme»**). La cifra del propio PWG: **«98% of all printers sold today support IPP/2.0 and
DNS-SD.»**

Windows lo usa: **«With the release of Windows 10 21H2, Windows offers inbox support for Mopria
compliant printer devices over network and USB interfaces via the Microsoft IPP Class Driver.»** Y
Microsoft retira los controladores de impresora de terceros por fases (calendario revisado en mayo de
2025):

| Fecha | Qué pasa |
|---|---|
| Septiembre de 2023 | Anuncio del plan |
| 15-01-2026 | **«For Windows 11+ and Windows Server 2025+, no new printer drivers will be published to Windows Update.»** |
| 01-07-2026 | **«Printer driver ranking order modified to always prefer Windows IPP inbox class driver.»** |
| 01-07-2027 | **«Except for security-related fixes, third-party printer driver updates will no longer be allowed.»** |

A la fecha del tema (otoño de 2026) ya rigen los dos primeros hitos: Windows Update no publica
controladores nuevos (los ya publicados **«can still be updated but only approved on a case-by-case
basis»**) y, si la impresora admite IPP, Windows prefiere su controlador de clase. La
salvedad: los controladores ya existentes siguen instalándose (**«Existing third-party printer drivers
can be installed from Windows Update or users can install printer drivers by using an installation
package provided by the print device manufacturer.»**).

En una multifunción, cada función va por su protocolo: **«For network devices, the Print and Fax
endpoints will work via IPP and IPP Fax Out, respectively, while the Scan endpoint will work via
WS-Scan or eSCL. For USB devices, the endpoints will only be accessible when the USB interface is in
IPP Over USB mode»**.

### El modo de impresión protegida de Windows

Es un ajuste de Windows que deja sólo la pila de impresión moderna: **«Windows protected print mode
exclusively uses Windows Ready Print»** y **«is designed to work with Mopria certified printers»**. Se
activa en **«Settings > Bluetooth & Devices > Printers & scanners»**, apartado **«Printer
Preferences»**, botón **«Set up»**. Efectos que hay que conocer antes de activarlo:

- **«Upon enabling Windows protected print mode, printers that use third-party drivers are
  uninstalled.»**
- **«XPS and fax are removed when Windows protected print mode is turned on.»**
- Puede imponerse por directiva de grupo, y entonces el usuario no lo quita: **«If Windows protected
  print mode is enabled as group policy, you won't be able to disable it without contacting your
  administrator.»** (Las directivas de grupo son del tema 6.)

## 3. Elementos de almacenamiento

Como periférico, el almacenamiento es lo que se enchufa por fuera: la memoria USB, el disco o SSD
externo y el lector de tarjetas. Son de entrada y salida (epígrafe 1) y en USB pertenecen a la clase
de almacenamiento masivo, la 08h, que Windows atiende sin controlador del fabricante con Usbstor.sys
(**«Microsoft provides the Usbstor.sys port driver to manage USB mass storage devices with
Microsoft's native storage class drivers.»**). Si el disco y el puerto son SuperSpeed y admiten flujos
masivos, Windows carga el controlador UASP, Uaspstor.sys (epígrafe 1).

La energía, que antes limitaba los discos alimentados por el propio cable, la resuelve USB PD 3.1
(epígrafe 7): **«Enables new higher power use cases such as USB bus powered Hard Disk Drives (HDDs)
and printers.»**

La velocidad la pone el más lento de los dos extremos: con USB 3.2 el enlace **«will operate at lowest
common speed capability»**. Un SSD externo de 10 Gbit/s en un puerto de 5 Gbit/s rinde a 5.

Lo demás del almacenamiento (discos magnéticos y de estado sólido, memorias flash y tarjetas SD,
RAID, NAS y SAN, copias, compresión, clonación y recuperación) es el tema 3, y no se repite aquí.

## 4. Elementos de visualización

### El monitor y la relación de aspecto

El monitor es el periférico de salida por excelencia (**«The most obvious output device is a display
or monitor, visually representing the state of the computer.»**); con pantalla táctil pasa a ser de
entrada y salida (epígrafe 1). Junto a él, el proyector y la pantalla grande (cita del epígrafe 1).

La relación de aspecto, con lo que fue cada una:

| Relación | Qué es |
|---|---|
| 4:3 | La de la televisión analógica y los monitores antiguos |
| 1:1 | Cuadrada: formatos de red social, no de televisión |
| 16:9 | La panorámica de la televisión digital y de casi toda pantalla actual |
| 5:4 | Una variante de monitor informático antiguo, casi cuadrada |

Cómo se lee la notación: el primer número es el ancho y el segundo el alto, en la misma
unidad. 16:9 significa que por cada dieciséis de ancho hay nueve de alto.

Y el dato que las relaciona, porque explica por qué la transición fue dolorosa: 16:9 es
aproximadamente 1,78 y 4:3 es 1,33. Ni una cabe dentro de la otra, y de ahí las bandas negras
laterales o superiores cuando se mezcla material de las dos épocas.

Ejemplos de resolución y su relación: 640 × 480 es 4:3 (640/480 = 1,33); 1920 × 1080 es 16:9
(1920/1080 = 1,78). El cálculo es propio.

### Resolución, refresco y reloj de píxel

Cuantos más píxeles y más refrescos por segundo, más datos por segundo tiene que llevar el cable. El
curso 6.111 del MIT da el reloj de píxel que exige cada resolución a 60 Hz; la fila de 720p se corrige con la norma
SMPTE ST 2059-1:2021 (tabla 3), que para el sistema progresivo de 750 líneas (1280 × 720 de imagen
activa) a 60 Hz da una frecuencia de muestreo de 74,25 × 10⁶ Hz:

| Resolución | Nombre | Reloj de píxel a 60 Hz |
|---|---|---|
| 640 × 480 | VGA | **«25MHz (40ns)»** |
| 800 × 600 | SVGA | **«40MHz»** |
| 1024 × 768 | XVGA | **«65MHz»** |
| 1280 × 720 | 720p | 74,25 MHz (SMPTE; el MIT escribe «75.25MHz», que no cuadra con la norma) |
| 1920 × 1080 | 1080p | **«148.5MHz (6.7ns)»** |

La cifra exacta de la norma VGA es 25,175 MHz (**«25.175 MHz is the VGA standard»**, Cornell, ECE
4760); el MIT la redondea. Esa progresión explica los límites de cada interfaz (epígrafe 7): el enlace
sencillo de DVI llega a 165 MHz y por eso 1080p a 60 Hz cabe en él.

### Varios monitores en Windows

Windows 11 numera las pantallas que detecta; **«Identify»** muestra el número en cada una, y si una
no aparece, se busca en **«Display > Multiple displays > Detect»**. Las pantallas se ordenan
arrastrándolas en la configuración de pantalla y pulsando **«Apply»**, para que el ratón pase de una
a otra como están sobre la mesa. Con el teclado, Windows + P elige qué se ve dónde (Soporte de
Microsoft):

| Modo | Para qué |
|---|---|
| **«PC screen only»** | **«See things on one display only.»** |
| **«Duplicate»** | **«See the same thing on all your displays.»** |
| **«Extend»** | **«See your desktop across multiple screens.»** |
| **«Second screen only»** | **«See everything on the second display only.»** |

Duplicar es lo de una sala con proyector; extender, lo del puesto con dos monitores. Para una
pantalla inalámbrica, Windows + K abre **«Cast»**. Antes de tocar nada, la fuente manda lo básico:
**«Make sure your cables are properly connected to your PC or dock.»** y buscar actualizaciones.

## 5. Elementos de digitalización

### El escáner: tres resoluciones

La resolución es la cifra que más engaña de un escáner. Epson (*Scanner Technical Brief*, 2007)
distingue tres:

- Óptica: **«This is the actual number of pixels read by the CCD (Charge Coupled Device), which
  measures the intensity of the light that is reflected from the image to be scanned, and converts it
  to an analog voltage. If a scanner has a resolution of 600 x 2400 dpi, its optical resolution is 600
  dpi»**. Es la del sensor, la primera cifra.
- De hardware: **«Using a precision stepper motor to double-step or quadruple-step the carriage, the
  scanner's sub-scanner resolution can be increased.»** Sube la segunda cifra moviendo el carro a
  pasos más finos.
- Interpolada: **«Interpolation is a method to increase the resolution of an image. It uses a complex
  algorithm to "add" pixels to an image based on the mathematical probability of surrounding
  pixels.»** Inventa píxeles. En el ejemplo de la fuente, un escáner de hardware 1200 × 2400 ppp
  anuncia 9600 × 9600 de máxima: esa máxima es interpolada.

Para comparar escáneres se mira la óptica. Y si se amplía, la resolución efectiva cae en proporción:
una foto de 2 × 2,5 pulgadas escaneada a 1200 ppp y ampliada a 8 × 10 queda en **«effective
resolution: 300 dpi»** (se ha multiplicado por cuatro el tamaño, se divide por cuatro la
resolución).

### La profundidad de color

**«Pixel depth refers to the number of bits of data captured for each picture element (pixel).»** El
número de colores es 2 elevado a esa profundidad (**«computed by taking the pizel depth as an
exponent of two»**):

| Modo | Colores (fuente) |
|---|---|
| 1 bit (blanco y negro) | 2¹ = 2 |
| Gris de 8 bits | 2⁸ = 256 grises |
| RGB de 24 bits (8 por color) | 2²⁴ = **«16.7 millions colors»** |
| RGB de 48 bits (16 por color) | 2⁴⁸ = **«Over 250 trillion colors»** (billones, en castellano) |

### Cómo habla Windows con el escáner: WIA y TWAIN

**«Windows Image Acquisition (WIA) is the still image acquisition platform in the Windows family of
operating systems starting with Windows Millennium Edition (Windows Me) and Windows XP.»** Sustituye
al esquema anterior sin eliminarlo: **«The imaging architecture in Windows 2000 and Windows 95 or
later consisted of a low-level hardware abstraction, Still Image Architecture (STI), and a high-level
set of APIs known as TWAIN. […] WIA is an imaging architecture that builds on STI and does not require
TWAIN, although TWAIN is still supported alongside WIA.»**

En la práctica: **«WIA-based scanners work right out of the box on Windows with Windows scanning
applications such as Windows Fax and Scan and Paint.»** Por red, el escáner habla el protocolo
**«Web Services for Scanner (WS-Scan)»**; en las multifunción modernas, WS-Scan o eSCL (epígrafe 2).
El gestor de errores de WIA 2.0 da además los avisos del aparato, como **«"Lamp warming up," "Cover open," "Paper
jam,"»**. Por USB, el controlador de clase es Usbscan.sys (clase 06h, epígrafe 1).

## 6. Elementos multimedia

Son los que meten o sacan sonido e imagen en movimiento: micrófono y cámara web (entrada), altavoces
(salida), auriculares con micrófono (las dos cosas). Bourgeois: **«Microphones can be used to record
audio or give voice commands. Webcams and other types of video cameras can be used to record video or
participate in a video chat session.»**; **«Other output devices include speakers for audio
output»**.

Cómo se conectan:

- Por USB, con clase propia y controlador de Windows: audio, 01h, Usbaudio.sys; vídeo (la cámara
  web), 0Eh, Usbvideo.sys (**«Microsoft provides USB video class support with the Usbvideo.sys
  driver.»**). Por eso una cámara o unos auriculares USB funcionan al enchufarlos.
- Por Bluetooth, los auriculares y altavoces inalámbricos (epígrafe 1).
- Por la salida de vídeo: HDMI lleva audio con la imagen y VGA no (**«VGA is analog and video only,
  while HDMI is digital and carries audio»**); un monitor o un televisor con altavoces suena por el
  mismo cable HDMI. Que DisplayPort lleve audio y DVI no es dato de oficio (tabla del epígrafe 7):
  las fuentes leídas de VESA y de la DDWG no tratan el audio.
- HDMI tiene además canal de retorno: el televisor devuelve el sonido a un amplificador o barra de
  sonido por el mismo cable (**«Audio Return Channel (ARC) allows an HDMI-connected TV to send audio
  data "upstream" to an AVR or soundbar with an HDMI cable, eliminating the need for a separate audio
  cable»**); la versión mejorada, eARC, **«supports the most advanced audio formats and highest audio
  quality»**.

La codificación de los ficheros de audio y vídeo (muestreo, códecs y contenedores) no la pide este
enunciado.

## 7. Conectividad del puesto

### USB: tres cosas que no hay que mezclar

La versión fija la velocidad; Type-C es el conector; PD es la energía. Lo dice el USB-IF: **«USB 3.2
only defines the transfer rate of a product.»**; **«USB 3.2 is not USB Type-C™, USB Standard-A,
Micro-USB, or any other USB cable or connector.»**; **«USB 3.2 is not USB Power Delivery or USB Battery
Charging.»** Un
puerto Type-C puede ser de 480 Mbit/s o de 80 Gbit/s; un puerto rectangular (Standard-A) puede ser de
5 Gbit/s.

### USB: velocidades y nombres

**«The USB4® and USB 3.2 specifications together identify five transfer rates – 80Gbps, 40Gbps,
20Gbps, 10Gbps, and 5Gbps.»** Al público se le anuncian con la cifra: «USB 80Gbps», «USB 40Gbps»,
«USB 20Gbps», «USB 10Gbps», «USB 5Gbps». Los nombres técnicos se quedan en la especificación:
**«USB4® Version 2.0, USB4® Version 1.0, USB 3.2, SuperSpeed Plus, Enhanced SuperSpeed and SuperSpeed+
are defined in the USB specifications however these terms are not intended to be used in product
names, messaging, packaging or any other consumer-facing content.»** (USB-IF, guía de enero de 2024.)

| Velocidad | Nombre técnico | Nombre al público |
|---|---|---|
| 1,5 y 12 Mbit/s | Basic-Speed | — |
| 480 Mbit/s | USB 2.0, Hi-Speed | — |
| 5 Gbit/s | USB 3.2 Gen 1 | USB 5Gbps |
| 10 Gbit/s | USB 3.2 Gen 2 | USB 10Gbps |
| 20 Gbit/s | USB 3.2 Gen 2x2 (dos carriles de 10) o USB4 20Gbps | USB 20Gbps |
| 40 Gbit/s | USB4 40Gbps | USB 40Gbps |
| 80 Gbit/s | USB4, sobre cables certificados para 80 Gbit/s | USB 80Gbps |

Las fuentes de la tabla: **«The Basic-Speed USB Logo must be used with Basic-Speed (12 Mbps or 1.5
Mbps) Product. The Hi-Speed USB Logo must be used with Hi-Speed (480 Mbps) Product.»**; **«The USB 3.2
specification absorbed all prior 3.x specifications. USB 3.2 identifies three transfer rates, USB 3.2
Gen 1 at 5Gbps, USB 3.2 Gen 2 at 10Gbps and USB 3.2 Gen 2x2 at 20Gbps.»**; **«The USB 3.2
specification defines multi-lane operation for new USB 3.2 hosts and devices, allowing for up to two
lanes of 10Gbps operation to realize a 20Gbps data transfer rate.»**; **«USB4® identifies two transfer
rates, USB4® 20Gbps at 20Gbps and USB4® 40Gbps at 40Gbps.»**, y en la página vigente del USB4,
**«Two-lane operation using existing USB Type-C cables and up to 80 Gbps operation over 80 Gbps
certified cables»**. Las fuentes leídas no atan cada velocidad del USB4 a su versión 1.0 o 2.0, y el
tema no lo hace. Tampoco dan los nombres antiguos de las dos velocidades más bajas: la guía vigente
las llama Basic-Speed.

Compatibilidad: USB 3.2 es **«Backwards compatible with all existing USB products; will operate at
lowest common speed capability.»** USB4 nace de Thunderbolt y es compatible con lo anterior:
**«Based on the Thunderbolt™ protocol specification contributed by the Intel Corporation, USB4 doubles
the maximum aggregate bandwidth of USB and enables multiple simultaneous data and display
protocols.»**; **«Compatibility with existing USB 3.2, USB 2.0, and Thunderbolt 3 hosts and devices is
supported, and the resulting connection scales to the best mutual capability of the devices being
connected.»** Esos «protocolos de pantalla simultáneos» son los que permiten sacar DisplayPort por
USB4 (véase DisplayPort, más abajo).

### El conector USB Type-C

**«Slim and sleek connector tailored to fit mobile device product designs, yet robust enough for
laptops and tablets»**; **«Features reversible plug orientation and cable direction»**: entra en
cualquier posición y el cable vale en cualquier sentido. Nació porque los conectores anteriores eran
grandes (**«the relatively large size and internal volume constraints of the Standard-A and Standard-B
versions of USB connectors»**).

Los cables USB-C a USB-C llevan rótulo obligatorio con velocidad y potencia: **«All USB-C® to USB-C
cables are required to use the USB-IF approved cable logo on the cable in the form of either being
embossed on the over mold or printed on the overmold»**; **«all USB-C® to USB-C cables must be labeled
using the appropriate data rate and power wattage cable logo. For example, a USB 20Gbps cable that
supports 20V at 3A must be marked with the Combined Performance and Power 20Gbps/60W logo.»** (20 V ×
3 A = 60 W.) Y un cable USB-C de USB 2.0 sigue siendo lento aunque cargue mucho: **«USB 2.0 Type-C®
240W and 60W cables that delivers data at up to 480Mbps»**.

### USB Power Delivery

**«Announced in 2021, the USB PD Revision 3.1 specification is a major update to enable delivering up
to 240W of power over full featured USB Type-C® cable and connector. Prior to this update, USB PD was
limited to 100W using a solution based on 20V using USB Type-C cables rated at 5A.»** Los escalones
nuevos: **«New 28V, 36V, and 48V fixed voltages enable up to 140W, 180W and 240W power levels,
respectively.»** (100 W = 20 V × 5 A; 240 W = 48 V × 5 A.)

La energía ya no va en un solo sentido: **«Power direction is no longer fixed. This enables the
product with the power (Host or Peripheral) to provide the power.»** El caso del puesto lo da la
fuente: **«A monitor with a supply from the wall can power, or charge, a laptop while still
displaying.»** Un solo cable entre monitor y portátil lleva imagen, datos y carga.

### Thunderbolt

Es la conexión de Intel sobre la misma base que USB4. Thunderbolt Technology Community: **«Thunderbolt 4
always delivers 40 Gbps speeds and data, video and power over a single connection, while Thunderbolt
5 promises speeds of 80/120 Gbps.»**; su seña es la compatibilidad (**«compliance across the broadest
set of industry-standard specifications – including USB4, DisplayPort and PCI Express (PCIe) – and is
fully compatible with prior generations of Thunderbolt and USB products.»**).

Thunderbolt 5 (nota de Intel de 12-09-2023): **«Thunderbolt 5 will deliver 80 gigabits per second
(Gbps) of bi-directional bandwidth, and with Bandwidth Boost it will provide up to 120 Gbps for the
best display experience.»**; **«Built on industry standards including USB4 V2, DisplayPort 2.1 and PCI
Express Gen 4; fully compatible with previous versions.»**; **«Double the PCI Express data throughput
for faster storage and external graphics.»** En la misma nota, Microsoft: **«Thunderbolt 5 is fully
USB 80Gbps standard compliant»**. Entre dos ordenadores, Thunderbolt hace de red punto a punto
(**«a peer-to-peer connection at 10GbE speeds»**), y la versión 5 dobla ese ancho (**«Double the
bandwidth of Thunderbolt Networking»**). La potencia de carga de Thunderbolt 4 y 5 en vatios no consta
en las fuentes leídas y el tema no la da.

### RJ45: la red cableada

Un conector RJ45 consta de ocho hilos, que son cuatro pares trenzados. Es el conector de la tarjeta
de red Ethernet del puesto (la tarjeta, en el tema 1; las redes, en el 13), y también el de las
impresoras y escáneres de red.

Las dos asignaciones de colores. Fluke Networks: **«These are two wiring standards used for
eight-position RJ45 modular plugs. The difference between T568A and T568B is that the orange and green
pairs are interchanged.»** En detalle: **«In T568A, the green wires connects to pins 1,2 and the
orange wire connects to pins 3,6. In T568B, the orange wires connects to pins 1,2 and the green wires
connects to pins 3,6. All the other wires connect to the same pins in both standards.»**

| | T568A | T568B |
|---|---|---|
| Patillas 1 y 2 | Par verde | Par naranja |
| Patillas 3 y 6 | Par naranja | Par verde |
| Resto | Igual en las dos | Igual en las dos |
| Situación en la norma | **«recognized as the preferred wiring pattern»**: compatible con los esquemas de cableado USOC de uno y de dos pares | **«has been the more widely used wiring scheme»**: coincide con el antiguo código de colores AT&T 258A, pero **«provides only single-pair backward compatibility to the USOC wiring scheme»** |

Las dos están **«allowed under the ANSI/TIA-568.2-D wiring standards»** y rinden igual (**«Both
standards have the same transmission performance and can support the same Ethernet protocols,
including Gigabit Ethernet.»**). Lo que no se puede es mezclarlas: **«Maintaining consistency is key
when wiring a new network or expanding an existing one. Wiring should match, color to color and stripe
to stripe; if it doesn't, signals will be compromised.»**

Y el par trenzado tiene un límite de distancia: cien metros por tramo en las categorías corrientes
de red. (El tema 13 desarrolla Ethernet y sus normas IEEE 802.)

### VGA

Es la conexión analógica de monitor. El MIT la resume frente a HDMI: **«the main difference is that
VGA is analog and video only, while HDMI is digital and carries audio.»** Cómo funciona:

> **«most analog computer monitors work -- they accept 5 analog signals (red, green, blue, hsync, and
> vsync) over a standardized HD15 connector. The signals are transmitted as 0.7V peak-to-peak (1V
> peak-to-peak if the signal also encodes sync). The monitor supplies a 75Ω termination for each
> signal»**

Cinco señales (rojo, verde, azul, sincronismo horizontal y vertical) por un conector de 15 contactos
(HD15), a 0,7 V de pico a pico, cargadas a 75 Ω. Los sincronismos son pulsos **«digital active
low»** (Cornell). La resolución que le da nombre, 640 × 480, va con un reloj de **«25.175 MHz»**
(epígrafe 4).

La identificación del monitor (DDC y EDID) y el patillaje del conector de 15 contactos no constan en
las fuentes leídas para VGA; la especificación DVI sí trata a un monitor analógico **«as it would a
analog monitor connected to the 15 pin VGA»**.

Por ser analógica, la imagen pasa de digital a analógica en el ordenador y, en un monitor plano, otra
vez a digital: es la razón por la que DVI y DisplayPort se diseñaron para sustituirla. La DDWG lo
explica: **«A digital interface for the computer to monitor interconnect has several benefits over the
standard VGA connector. A digital interface ensures all content transferred over this interface
remains in the lossless digital domain from creation to consumption.»** Y VESA presenta DisplayPort
como **«the industry replacement for DVI, LVDS and VGA»**. (La doble conversión del monitor plano es
deducción del tema, no cita.)

### DVI

La especificación (DDWG, *Digital Visual Interface, Revision 1.0*, 2 de abril de 1999) persigue cuatro
cosas: **«1. Content to remain in the lossless digital domain from creation to consumption 2. Display
technology independence 3. Plug and play through hot plug detection, EDID and DDC2B 4. Digital and
Analog support in a single connector»**.

Dos conectores del mismo tamaño, uno digital y otro mixto: **«two connectors with identical mechanical
characteristics: one that is digital only and one that is digital and analog»**.

| Conector | Contactos | Qué lleva |
|---|---|---|
| Sólo digital | **«24 signal contacts organized in three rows of eight contacts»** | Señales TMDS |
| Combinado | **«29 signal contacts»**: los 24 más **«five signals that are designed specifically for analog video signals»** | TMDS y además rojo, verde, azul y los dos sincronismos analógicos |

Consecuencia práctica, literal: **«Because the digital only receptacle does not have sockets for the
analog pins of an analog monitor, the plug of an analog monitor will not mate with the digital only
system.»** Un monitor analógico no entra en un DVI sólo digital.

La señal digital es TMDS. Enlace sencillo y doble: el enlace 0 cubre **«all pixel formats and timings
requiring up to and including 165MHz»**; por encima, dos enlaces: **«Any pixel format and blanking
interval requiring more than a 165MHz-clock frequency must be supported using two T.M.D.S. links.»**
Cada uno trabaja entonces a la mitad (**«if a pixel format and timing requiring a 200MHz pixel clock
is supported, then both links must operate at 100MHz»**), y para el doble enlace **«There is no
specified maximum»**.

El monitor se identifica por EDID, que el ordenador lee por DDC; la detección en caliente avisa de
que se ha enchufado: **«Hot Plug Detect (HPD) Signal is driven by monitor to enable the system to
identify the presence of a monitor.»** Y el ordenador da 5 V para que el monitor apagado pueda
identificarse (**«+ 5 volt signal provided by the system to enable the monitor to provide EDID data
when the monitor circuitry is not powered»**).

Los nombres que usa el oficio para las variantes de conector:

DVI-A es analógica, DVI-D digital y DVI-I las dos.

La especificación de 1999 no usa esos nombres (habla de conector sólo digital y combinado); son
denominación de uso corriente.

### HDMI

HDMI es todo digital y usa la misma señalización que DVI: **«HDMI is all digital and uses
transition-minimized differential signaling (TMDS)»** (MIT). Lleva audio con la imagen (epígrafe 6).
Lo que trajo cada versión que se pregunta (HDMI Licensing Administrator):

| Versión | Qué aporta |
|---|---|
| 1.4b | 4K (**«4096×2160 at 24 Hz, 3840×2160 at 24, 25, and 30 Hz, and 1920×1080 at 120 Hz»**); **«HDMI Ethernet Channel»** (red por el propio cable, con **«High Speed HDMI Cable with Ethernet»**); **«Audio Return Channel (ARC)»**; el conector **«HDMI Micro»** para móviles |
| 2.1 | El **«Ultra High Speed HDMI Cable»**, **«introduced in the HDMI 2.1 Specification and entered the market in 2020»**, para **«up to 48Gbps maximum bandwidth»** |
| 2.2 (la vigente) | **«Higher 96Gbps bandwidth and next-gen HDMI Fixed Rate Link technology»**; **«up to 12K@120 and 16K@60»**; cable **«Ultra96 HDMI Cable»**, **«the only cable that supports all HDMI 2.2 Specification applications»**; compatible hacia atrás (**«backward compatible with earlier versions of the Specification»**) |

Otras funciones de la versión vigente: eARC (epígrafe 6); frecuencia de refresco variable para juegos
(**«Variable Refresh Rate (VRR) reduces or eliminates lag, stutter and frame tearing»**); y la
alimentación de cables activos por el propio conector (**«HDMI Cable Power enables active HDMI Cables
to be powered directly from the HDMI Connector, without attaching a separate power cable.»**).

Los cables Ultra96 y Ultra High Speed tienen certificación obligatoria y etiqueta comprobable: **«It is
a mandatory certification program»**; la etiqueta **«can be scanned by standard QR code apps»** y el
nombre tiene que ir también en la cubierta del cable (**«The names are also required to appear on the
outer cable jackets themselves.»**).

Conectores: hay tipos A, C y D, y adaptadores pasivos entre ellos (**«convert connectors from HDMI Type
A to Type A, Type C or Type D connector types»**). Y HDMI puede salir por USB-C: **«The HDMI Alt Mode
for USB Type-C connector will allow HDMI-enabled source devices to utilize a USB Type-C connector to
directly connect to HDMI-enabled displays»** (según la página de la 1.4b, con funciones de esa
versión).

### DisplayPort

Es el estándar de VESA y el del mundo del ordenador: **«DisplayPort is the de facto global standard
for PC monitors and embedded displays.»** Tres conectores: **«the locking standard DisplayPort
connector, Mini-DP connector, and USB Type-C connector»**; el de tamaño completo lleva retención.
Y va dentro de USB4 y Thunderbolt: **«DisplayPort also powers the video capabilities of single-cable
technologies like Thunderbolt and USB4.»**

DisplayPort 2.1 (nota de VESA de 17-10-2022) **«is backward compatible with and supersedes the
previous version of DisplayPort (DisplayPort 2.0)»** y alinea DisplayPort con USB Type-C y USB4 para
compartir capa física. Los cables y su capacidad:

| Cable | Tasa por carril | Carriles | Máximo |
|---|---|---|---|
| DP40 | **«UHBR10 link rate (10 Gbps)»** | Cuatro | **«40 Gbps»** |
| DP80 | **«UHBR20 link rate (20 Gbps)»** | Cuatro | **«80 Gbps»** |

Los DP40 ya certificados valen para el escalón intermedio **«DP54»**, y VESA anuncia para la
actualización 2.1b un cable activo DP80LL de hasta tres metros (**«up to three meters in length»**).
La nota de la 2.1, al hablar del túnel por USB4, cita el soporte obligatorio (**«mandated support»**)
de la compresión DSC, que **«can reduce DisplayPort transport bandwidth in excess of
67 percent without visual artifacts»**.

Lo que más se usa en el puesto: varias pantallas desde una salida. **«Multi-Stream Transport (MST)
allows for multiple screens (at various resolutions) to be driven from a single DisplayPort source
connection.»** Y la conversión: **«DisplayPort is designed to recognize and support HDMI devices
through conversion cables, just like it does for other earlier video interfaces such as DVI and
VGA.»**; hay convertidores **«with a native DisplayPort Plug or USB-C plug»**, y algunas bases USB
traen salida HDMI con el convertidor dentro.

### Las interfaces de vídeo, frente a frente

| Interfaz | Vídeo | Audio | Rasgo |
|---|---|---|---|
| DVI | Analógico y digital, según la variante | No | Nació en la transición, y por eso hay variantes de un tipo, del otro y de los dos |
| HDMI | Sólo digital | Sí | El estándar del equipo doméstico |
| DisplayPort | Sólo digital | Sí | El del mundo informático, con retención mecánica en el conector de tamaño completo |

Para completar con VGA: analógica, sólo vídeo (**«VGA is analog and video only»**), conector de 15
contactos.

La trampa de examen que sale de la tabla: HDMI nunca llevó vídeo analógico; DVI sí puede, en su
conector combinado. HDMI sí lleva audio; y el conector grande de DisplayPort sí suele llevar un pestillo de retención, que es su rasgo
distintivo frente al de HDMI.

## 8. Aplicación práctica

Los razonamientos de estos casos son oficio; cada dato es el de la fuente citada en su epígrafe.

*Caso 1. Un portátil con un único puerto USB-C (USB4) y un monitor con entrada USB-C y fuente propia.*
Un cable USB-C certificado puede llevar la imagen (DisplayPort dentro de USB4), los datos y, con USB
PD, cargar el portátil desde el monitor (**«A monitor with a supply from the wall can power, or
charge, a laptop while still displaying.»**). Se mira el rótulo del cable: velocidad y vatios. Un
cable USB 2.0 de 240 W carga, pero sus datos se quedan en 480 Mbit/s, y no hay que contar con él para
la imagen.

*Caso 2. Un proyector antiguo con entrada VGA y un portátil con HDMI.* VGA es analógico y HDMI
digital: hace falta un convertidor activo, no un adaptador de cable. El sonido no viaja por VGA: va
aparte o por los altavoces del portátil. En Windows, Windows + P y «Duplicate» para que la sala vea lo
mismo que el portátil.

*Caso 3. El segundo monitor no aparece.* Por orden: cable bien conectado al equipo o a la base;
**«Detect»** en la configuración de pantalla; Windows + P en «Extend»; actualizaciones de Windows. Si
el monitor es de DVI y se ha enchufado a un DVI sólo digital con un cable o adaptador analógico, no
encaja: el conector sólo digital no tiene los contactos analógicos.

*Caso 4. 2560 × 1440 a 60 Hz por DVI.* Si la combinación de resolución y refresco exige más de
165 MHz de reloj, hace falta DVI de doble enlace; con cable o puerto de enlace sencillo, el monitor
no llega a su resolución nativa. Qué reloj exige exactamente esa resolución no lo da ninguna fuente
leída; 1080p a 60 Hz, 148,5 MHz, sí cabe en un enlace.

*Caso 5. Montar un latiguillo de red.* Los dos extremos con la misma asignación (T568A con T568A, o
T568B con T568B); en una instalación, la que ya tenga el edificio, sin mezclar. Ocho hilos, cuatro
pares; en T568B, el par naranja en las patillas 1 y 2.

*Caso 6. Una impresora nueva en un Windows 11 de 2026.* Si es Mopria, Windows la instala con su
controlador IPP de clase, por red o por USB, sin controlador ni instalador del fabricante; desde el 1-7-2026, Windows prefiere
ese controlador. Si el puesto tiene activado por directiva el modo de impresión protegida, una
impresora que sólo funcione con controlador de terceros no se podrá usar: hay que comprobarlo antes de
comprarla.

*Caso 7. El folleto del escáner dice 9600 ppp.* Hay que buscar la resolución óptica (la primera
cifra de la de hardware): la de 9600 × 9600 suele ser interpolada.

*Caso 8. Un disco externo «USB 10Gbps» en un puerto «USB 5Gbps».* Funciona, a 5 Gbit/s: la conexión
baja a la velocidad común más baja.

## Lo que este tema no da, y dónde está

- La asignación de patillas del conector VGA de 15 contactos y el canal DDC/EDID en VGA: sólo constan
  en webs comerciales y enciclopedias, no en una fuente leída.
- Las impresoras matriciales en detalle, los lenguajes de impresora (PCL, PostScript) y la definición
  normalizada de la resolución de impresión: sin fuente primaria leída.
- La edición vigente de la ISO/IEC 24734 y las normas de rendimiento de tóner y de tinta (ISO/IEC
  19752 e ISO/IEC 24711): el sitio de ISO no se dejó leer.
- Los sensores de escáner que no son CCD (CIS), el reconocimiento óptico de caracteres (OCR) y el
  alimentador automático de documentos: sin fuente primaria leída.
- Las tecnologías de panel de los monitores (IPS, VA, OLED) y las características de cámaras web,
  auriculares y altavoces: sin fuente primaria leída.
- La potencia de carga de Thunderbolt 4 y 5 en vatios, y qué velocidad del USB4 corresponde a su
  versión 1.0 o 2.0: las fuentes leídas no lo dicen.
- El reloj de píxel de resoluciones distintas de las de la tabla del epígrafe 4.
- El patillaje de señales del RJ45 en Ethernet: la página del fabricante consultada no se dejó leer.
- El almacenamiento en sí (discos, SSD, flash, NAS, SAN, copias): tema 3. La tarjeta de red y los
  componentes internos: tema 1; su diagnóstico: tema 2. Las directivas de grupo de Windows: tema 6.
  Ethernet, Wi-Fi y las normas IEEE 802: tema 13.

## Trazabilidad

Todas las fuentes, leídas el 05-10-2026 en su versión en línea de ese día (salvo la SMPTE, leída el
06-10-2026):

- USB-IF: *USB Data Performance Language Usage Guidelines* (enero de 2024); *USB 3.2 Specification
  Language Usage Guidelines*; *USB4® Specification Language Usage Guidelines*; página «USB4®»
  (usb.org/usb4); página «USB Charger (USB Power Delivery)»; página «USB Type-C® Cable and Connector
  Specification»; *USB Type-C® Cable Logo Usage Guidelines*; *USB Logo Usage Guidelines* (2024);
  página «Defined Class Codes».
- Microsoft Learn: «USB device class drivers included in Windows» (actualizado el 13-06-2025); «End
  of servicing plan for third-party printer drivers on Windows» (actualizado el 09-05-2025); «Windows
  Protected Print Mode» (actualizado el 18-06-2026); «Windows Image Acquisition (WIA)» y «Windows
  Image Acquisition Drivers». Soporte de Microsoft: «How to use multiple monitors in Windows».
- Intel, nota de prensa «Intel Introduces Thunderbolt 5 Connectivity Standard», 12-09-2023;
  Thunderbolt Technology Community, página «Technology».
- Digital Display Working Group, *Digital Visual Interface, Revision 1.0*, 02-04-1999 (copia en PDF
  de la especificación).
- HDMI Licensing Administrator: páginas «HDMI 2.2 Specification Overview», «HDMI Specification 1.4b»,
  «Ultra96 HDMI Cable and Ultra High Speed HDMI Cable» y «HDMI Passive Adapters».
- VESA: nota «VESA Releases DisplayPort 2.1 Specification», 17-10-2022; página de DisplayPort
  (displayport.org).
- MIT, curso 6.111, *Lab #3* (otoño de 2019), «Video display technologies: HDMI & VGA»; Cornell, ECE
  4760, proyecto «Homemade VGA Adapter» (2012). SMPTE ST 2059-1:2021, tabla 3 (sistema de 750 líneas
  progresivo, 1280 × 720, 60 Hz: frecuencia de muestreo 74,25 × 10⁶ Hz), leída el 06-10-2026.
- Fluke Networks, base de conocimiento: «Differences Between Wiring Codes T568A vs T568B».
- Canon Inc.: «Laser Printers and MFPs» e «Inkjet Printers»; Epson Europe: «Heat-Free Technology»;
  Epson America: *Scanner Technical Brief* (6/07); Zebra Technologies: «What Is a Thermal Printer?»;
  HP: «ISO/IEC 24734 Method for Measuring Digital Printing Productivity» (© 2009).
- Printer Working Group: «IPP Everywhere» y página del grupo IPP.
- D. Bourgeois et al., *Information Systems for Business and Beyond* (2019), capítulos 2 y 5.

Oficio, declarado como tal: la tabla de clasificación de periféricos y su regla; la tabla de
relaciones de aspecto y su lectura; los ocho hilos del RJ45 y los cien metros por tramo; la tabla de
DVI, HDMI y DisplayPort frente a frente y los nombres DVI-A, DVI-D y DVI-I; el reparto de las cinco
familias del enunciado en los tres cajones; los razonamientos de la aplicación práctica. Cálculos
propios: los cocientes de las relaciones de aspecto y los productos de tensión por intensidad de USB
PD.
