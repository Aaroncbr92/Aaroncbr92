# Puesto 29 · Tema 4 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real del
sistema, como en la investigación). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/04-perifericos-y-conectividad-del-puesto-informatico.md`
(9.399 palabras con siglas e índice; 36 epígrafes; índice generado con `indice.py`).
Material: `29-investigacion-A-hardware.md` (§ Tema 4). Reuso (`informes/canal-sur-reuso/informatica.tsv`,
fila 29/4): RTVE 17 y 18 de Técnica Informática y Montaje 05, 30 %, «actualizar: no».

## Fuentes releídas y fecha

Todas las citas de la investigación se cotejaron por script contra las copias de
`fuentes/canal-sur/informatico/web/` el 05-10-2026 (usbif-*, intel-tb5-press, thunderbolt-tech,
mit-6111-lab3-vga, cornell-ece4760-vga-adapter, canon-laser-tech, canon-inkjet-2021, epson-heat-free,
hp-iso24734, ms-print-driver-eos, ms-wppm, pwg-ipp-everywhere, pwg-ipp, ms-wia, ms-wia-drivers,
epson-scanner-brief, bourgeois-isbb-2019).

Fuentes nuevas, descargadas y leídas el 05-10-2026 para cubrir huecos (misma carpeta):

| Fuente | Fichero | Qué cubre |
|---|---|---|
| DDWG, *Digital Visual Interface, Revision 1.0*, 02-04-1999 (copia PDF de la especificación, glenwing.github.io) | `ddwg-dvi-1.0.pdf` / `.txt` | Conectores de 24 y 29 contactos, TMDS, 165 MHz, doble enlace, HPD, DDC/EDID, frente a VGA |
| HDMI LA, «HDMI 2.2 Specification Overview» (la URL /spec/hdmi2_1 sirve ya la 2.2) | `hdmi-22-overview.txt` | 96 Gbit/s, Ultra96, VRR, eARC, Cable Power |
| HDMI LA, «HDMI Specification 1.4b», «Ultra HDMI Cables», «HDMI Passive Adapters», índice de especificaciones | `hdmi-14b.txt`, `hdmi-uhs-cable.txt`, `hdmi-passive.txt`, `hdmi-index.txt` | 4K, HEC, ARC, Micro, Alt Mode; 48 Gbit/s y 2020; certificación; tipos A, C, D |
| VESA, nota «VESA Releases DisplayPort 2.1 Specification», 17-10-2022; displayport.org; página DisplayPort Developer | `vesa-dp21-press.txt`, `vesa-dp-home.txt`, `vesa-dp-dev.txt` | DP40/DP80, UHBR10/20, DSC, MST, conector con retención, conversión a HDMI/DVI/VGA |
| USB-IF, «Defined Class Codes» | `usbif-class-codes.txt` | Clases 01h, 03h, 06h, 07h, 08h, 09h, 0Eh |
| Microsoft Learn, «USB device class drivers included in Windows» (13-06-2025) | `ms-usb-classes.txt` | Controladores de clase, Uaspstor.sys, Usbscan.sys |
| Soporte de Microsoft, «How to use multiple monitors in Windows» | `ms-multiple-monitors.txt` | Identify, Detect, Windows + P, Windows + K |
| Zebra, «What Is a Thermal Printer?» | `zebra-thermal.txt` | Térmica directa, transferencia térmica, impacto |
| Fluke Networks, «Differences Between Wiring Codes T568A vs T568B» | `fluke-t568.txt` | T568A/T568B, ANSI/TIA-568.2-D |

Intentado sin éxito: vesa.org daba 403 con un agente y 200 con otro (resuelto); Cisco (patillaje
RJ45 en Ethernet), 17 palabras útiles, descartado; Zebra soporte (artículo 000021288), vacío.

Comprobación de literalidad por script: las 205 negritas «…» del tema (troceadas por «[…]») se buscan
en el texto normalizado de las fuentes. Quedan 1 sin casar por un salto de página del PDF de DVI
(«A digital interface … remains in the lossless digital domain…», líneas 300-306 del `.txt`: es literal
con la cabecera de página en medio). Dos se corrigieron (USB 3.2, que en la fuente son tres frases
sueltas; cable USB 2.0 Type-C, que en la fuente dice «cables that delivers»).

`refutar_prosa.py`: 0 hallazgos (8 siglas sin presentar en la primera pasada, corregidas). Tema técnico
sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Qué se hizo

Epígrafes en el orden del enunciado: 1 periféricos (clasificación, conexión, clases USB y controladores
de Windows); 2 impresión (láser, inyección, térmica e impacto, ISO/IEC 24734, IPP y fin de los
controladores de terceros, impresión protegida); 3 almacenamiento (como periférico; remite al tema 3);
4 visualización (relación de aspecto, reloj de píxel, varios monitores); 5 digitalización (resoluciones,
profundidad, WIA/TWAIN); 6 multimedia; 7 conectividad (USB, Type-C, PD, Thunderbolt, RJ45, VGA, DVI,
HDMI, DisplayPort, frente a frente); 8 ocho casos prácticos.

Decisiones frente al material:

- La URL de HDMI 2.1 devuelve hoy la página de HDMI 2.2: el tema da la 2.2 como vigente y la 2.1 sólo
  por su cable (48 Gbit/s, 2020).
- DVI-A/DVI-D/DVI-I: la especificación de 1999 no usa esos nombres (habla de conector sólo digital y
  combinado). Se deja la frase de RTVE como nombre de oficio y se dice.
- La tabla RTVE «frente a frente» dice que DVI no lleva audio y que HDMI es «el estándar del equipo
  doméstico»: ninguna fuente leída lo confirma ni lo contradice; va como oficio (RTVE 18 lo declaraba
  así).
- Se descarta la cifra de alcance de Bluetooth: Bourgeois da «10 meters up to 100 meters» y
  «approximately 300 feet» en dos capítulos; el tema lo dice.
- Los nombres «Low/Full Speed» de USB 2.0 no entran: la guía vigente dice «Basic-Speed».
- El caso 4 (2560 × 1440 por DVI) no da el reloj de píxel exacto de esa resolución: ninguna fuente
  leída lo da; se razona con el umbral de 165 MHz.
- Se solapa con el tema 1 (USB, Thunderbolt), que remite aquí el detalle; el texto de USB se
  redactó de nuevo sobre las mismas fuentes (el tema 1 no está cerrado).

## Copiado del común

Ninguno. No hay en los temas cerrados de Canal Sur un epígrafe sobre periféricos o conectores
informáticos que valga literal (el tema 1 de este puesto no está cerrado; su tabla de periféricos es
la misma de RTVE 17).

## Copiado de RTVE sin cambios

Pasajes técnicos copiados literal, sin tocar una palabra (sólo se quitaron negritas y la marca «✔»,
porque en Canal Sur la negrita es literal de fuente y esto es oficio):

1. RTVE `tecnica-informatica/17` § 2: la frase «La clasificación es de tres cajones y se decide por
   el sentido en que va la información:», la tabla Clase / Qué hace / Ejemplos, el párrafo «La regla
   que la contesta sin dudar: …» y el párrafo «Y el aviso que evita el error más común: …». En el
   tema, § 1 «Qué es un periférico y cómo se clasifica».
2. RTVE `tecnica-informatica/18` § 1: la tabla Relación / Qué es, y los párrafos «Cómo se lee la
   notación: …» y «Y el dato que las relaciona, porque explica por qué la transición fue dolorosa:
   …». En el tema, § 4 «El monitor y la relación de aspecto».
3. RTVE `tecnica-informatica/18` § 4: la tabla Interfaz / Vídeo / Audio / Rasgo, y la frase «DVI-A es
   analógica, DVI-D digital y DVI-I las dos.». En el tema, § 7 «DVI» y «Las interfaces de vídeo,
   frente a frente».

## Adaptado de RTVE (sí se verifica)

- RTVE 18 § 1: «Las cuatro relaciones de la pregunta, con lo que fue cada una» pasa a «La relación de
  aspecto, con lo que fue cada una».
- RTVE 18 § 4: «Las otras dos opciones son ciertas … HDMI sí lleva audio, que es precisamente lo que
  lo impuso frente a DVI en el salón; y el conector grande de DisplayPort sí suele llevar un pestillo
  de retención, que es su rasgo distintivo frente al de HDMI.» se reescribe al final de § 7 sin la
  pregunta 69; lo del pestillo lo confirma VESA («the locking standard DisplayPort connector»).
- Montaje 05 § 6: «Un conector RJ45 consta de ocho hilos. […] son cuatro pares trenzados» y «Y el par
  trenzado tiene un límite de distancia que el examen pregunta en el tema 8: cien metros por tramo en
  las categorías corrientes de red» se quedan sin las remisiones a preguntas y al tema 8 de RTVE. Los
  cien metros siguen siendo oficio sin fuente leída (Ethernet es del tema 13).
- Quitado lo propio de RTVE: preguntas 11, 27, 40, 50, 69, «Ésa es la respuesta oficial», remisiones a
  temas de Técnica de Equipos.

## Ficheros tocados

- Creado: el tema y este informe.
- Añadidos en `fuentes/canal-sur/informatico/web/`: los de la tabla de fuentes nuevas.
- **Incidencia**: al limpiar ficheros de descarga borré por error dos ficheros sin seguimiento en git
  que no eran míos, `hp-page-yield.txt` (92 bytes) e `iso-24711.txt` (83 bytes), los dos cabeceras
  de descargas fallidas, sin contenido útil y sin referencias en `informes/` ni `temas/`.
  `hp-page-yield.txt` se ha rehecho con el contenido que vi (URL, «Leído: 2026-10-05» y «HP»);
  `iso-24711.txt` no lo llegué a ver y no se ha rehecho. Si alguien lo necesita, que repita esa
  descarga.

## Preguntas tipo test (comprobadas contra el tema)

1. (Periféricos) ¿Cuál de estos dispositivos es de entrada y salida? a) Monitor b) Escáner c) Pantalla
   táctil d) Impresora. **c**. § 1, tabla y aviso. Entera.
2. (Impresión) En la impresora láser, ¿cómo se llama la fase en que el tóner se adhiere al papel por
   calor y presión? a) Revelado b) Transferencia c) Exposición d) Fijado. **d**. § 2, láser. Entera.
3. (Impresión, aplicación) Desde el 1 de julio de 2026, Windows: a) no admite impresoras USB b) prefiere
   siempre el controlador de clase IPP de Windows c) prohíbe todo controlador de terceros d) elimina
   el fax. **b**. § 2, tabla de fechas (y la salvedad de que los existentes se siguen instalando).
   Entera.
4. (Almacenamiento) ¿Qué controlador carga Windows para un disco USB SuperSpeed que admite UASP?
   a) Usbstor.sys b) Uaspstor.sys c) Usbscan.sys d) Usbprint.sys. **b**. § 1 tabla y § 3. Entera.
5. (Visualización, aplicación) En una sala, para que el proyector muestre lo mismo que el portátil, en
   Windows + P se elige: a) PC screen only b) Duplicate c) Extend d) Second screen only. **b**. § 4 y
   caso 2. Entera.
6. (Digitalización) Un escáner de 600 × 2400 ppp tiene una resolución óptica de: a) 600 ppp b) 1200 ppp
   c) 2400 ppp d) 9600 ppp. **a**. § 5. Entera.
7. (Multimedia) Una cámara web USB funciona en Windows sin controlador del fabricante porque pertenece
   a la clase: a) 01h, Usbaudio.sys b) 03h, HID c) 0Eh, Usbvideo.sys d) 07h, Usbprint.sys. **c**.
   § 1 tabla y § 6. Entera.
8. (USB) USB PD 3.1 llega a 240 W con una tensión fija de: a) 20 V b) 28 V c) 36 V d) 48 V. **d**.
   § 7, USB Power Delivery. Entera.
9. (RJ45) La diferencia entre T568A y T568B es que: a) T568B usa seis hilos b) se intercambian los
   pares naranja y verde c) se intercambian los pares azul y marrón d) T568A no admite Gigabit
   Ethernet. **b**. § 7, RJ45. Entera.
10. (VGA, DVI, HDMI, DisplayPort) Señale la afirmación incorrecta: a) VGA lleva cinco señales
    analógicas por un conector HD15 b) un enlace DVI sencillo cubre hasta 165 MHz de reloj c) HDMI
    puede transportar vídeo analógico d) un cable DP80 llega a 80 Gbit/s con cuatro carriles. **c**.
    § 7, VGA, DVI, DisplayPort y frente a frente. Entera.

Las diez se contestan enteras con el tema; no hizo falta ampliar.
