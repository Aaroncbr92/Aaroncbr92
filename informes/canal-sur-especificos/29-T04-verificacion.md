# Puesto 29 · Tema 4 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/04-perifericos-y-conectividad-del-puesto-informatico.md`.
Copia previa en el directorio temporal de la sesión (`29t04-antes-verif.md`).

## Fuentes y fecha de lectura

Releídas el 06-10-2026 sobre las copias de `fuentes/canal-sur/informatico/web/` (descargadas el
05-10-2026), en los pasajes que el tema cita: `ms-usb-classes.txt` («Last updated 2025-06-13»),
`usbif-class-codes.txt`, `usbif-data-performance-language-2024`, `usbif-original-logo-2024`,
`usbif-usb32-language`, `usbif-usb4(-language)`, `usbif-typec`, `usbif-typec-cable-logo-2026`
(© 2024), `usbif-charger-pd`, `canon-laser-tech`, `canon-inkjet-2021`, `epson-heat-free`,
`zebra-thermal`, `hp-iso24734` (© 2009), `pwg-ipp-everywhere`, `pwg-ipp`, `ms-print-driver-eos`
(«Last updated 2025-05-09»), `ms-wppm` (2026-06-18), `ms-wia`, `ms-wia-drivers`,
`ms-multiple-monitors`, `epson-scanner-brief` (6/07), `mit-6111-lab3-vga` (f2019),
`cornell-ece4760-vga-adapter` (s2012), `ddwg-dvi-1.0` (02-04-1999), `hdmi-14b`,
`hdmi-22-overview`, `hdmi-uhs-cable`, `hdmi-passive`, `hdmi-index`, `vesa-dp21-press`
(17-10-2022), `vesa-dp-home`, `fluke-t568`, `intel-tb5-press`, `thunderbolt-tech`,
`bourgeois-isbb-2019` (cap. 2).

Nueva para este tema: SMPTE ST 2059-1:2021, tabla 3 (copia ya existente en
`fuentes/canal-sur/sonido/smpte/st2059-1/st2059-1-2021.txt`), leída el 06-10-2026.

## Método

1. Literalidad por script (normaliza comillas, guiones, ™/®, saltos; trocea por […]): 210 fragmentos
   «…» en negrita, 1 sin casar, el ya conocido de la DDWG (salto de página con cabecera en medio,
   líneas 300-306 del `.txt`): literal. Las negritas sin comillas (clases USB y controladores) se
   cotejaron a mano con `usbif-class-codes` y `ms-usb-classes`.
2. Prosa, tablas, glosas, cálculos, fechas y Trazabilidad: releídos en su pasaje con los nueve
   errores delante.
3. Lentes (tema técnico sin norma jurídica): `refutar_prosa.py` 0 hallazgos; `indice.py` 9.227
   palabras, 36 epígrafes.

## Copiado del común / de RTVE sin cambios

Nada del común. Los tres pasajes «Copiado de RTVE sin cambios» (RTVE TI 17 § 2; TI 18 § 1 y § 4) se
comprobaron sólo por literalidad, con script que quita negritas y ✔: 18 piezas, todas presentes en
RTVE; la única diferencia es «Disco duro ✔,» (marca quitada). No se re-verifican. Lo adaptado (párrafo
final de «frente a frente», RJ45 de Montaje 05) sí se verificó.

## Hallazgos y correcciones (15)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 9 | Siglas: USOC como «el servicio telefónico antiguo de la compañía Bell» | Fluke sólo dice «USOC wiring schemes»: «el esquema de cableado USOC» |
| 2 | 5 | RGB usado en § 5 sin presentar | Añadido a siglas; también SMPTE (nueva fuente) |
| 3 | 9 | § 1 tabla de clases: Hub «— (la fuente no lo da)» | `ms-usb-classes` sí lo da: **Usbhub.sys** y **Usbhub3.sys** (SuperSpeed) |
| 4 | 9 | § 2 láser: «La pieza que fija es el fusor» | Canon habla de rodillo/unidad de fijación, no de fusor: «En la fijación, …» |
| 5 | 9 | § 2: «IPP permite imprimir sin instalar el programa de cada marca» | Eso lo dice el PWG de IPP Everywhere: «Sobre IPP se apoya la impresión sin el programa de cada marca» |
| 6 | 1 | § 2: «La norma vigente es la PWG 5100.12-2024», tras IPP Everywhere | Es la de IPP/2.x (IPP Everywhere es otra): «La norma vigente de IPP/2.x» |
| 7 | 6 | § 2: hito de 15-01-2026 sin su salvedad | Añadido: los ya publicados **«can still be updated but only approved on a case-by-case basis»** |
| 8 | 9 | § 4 tabla: 720p a **«75.25MHz»** (MIT) | Literal del MIT, pero errata: SMPTE ST 2059-1:2021, tabla 3, da 74,25 × 10⁶ Hz para 1280 × 720 a 60 Hz. Fila corregida y se dice; Trazabilidad y ficha ampliadas |
| 9 | 9 | § 6: «HDMI y DisplayPort llevan audio con la imagen, DVI y VGA no» | Sólo HDMI sí y VGA no tienen fuente (MIT); DP con audio y DVI sin él, declarado oficio (VESA y DDWG leídas no tratan el audio) |
| 10 | 9 | § 7 tabla USB: «USB 2.0 y anteriores, Basic-Speed» | La guía sólo dice Basic-Speed (mismo hallazgo que en el tema 1): «Basic-Speed» |
| 11 | 6 | § 7 RJ45, T568B | Añadida la salvedad de Fluke: **«provides only single-pair backward compatibility to the USOC wiring scheme»**; «cableado telefónico USOC» → «esquemas de cableado USOC» |
| 12 | 6 | § 7 DP: «La compresión DSC, obligatoria en la 2.1» | La nota dice **«mandated support»** al hablar del túnel por USB4: se dice así |
| 13 | 9 | § 7 frente a frente (adaptado de RTVE): HDMI lleva audio, «que es precisamente lo que lo impuso frente a DVI en el salón» | Historia sin fuente: quitada la cláusula |
| 14 | 9 | Caso 6: Mopria se instala «sin descargar nada» | Microsoft dice que las Print Support Apps se instalan solas desde la Store: «sin controlador ni instalador del fabricante» |
| 15 | forma | Rótulos «Caso 1-8» en negrita | La negrita es literal de fuente: pasan a cursiva |

## Confirmado sin cambios (muestra)

Clases 01h, 03h, 06h (Still Imaging), 07h, 08h, 0Eh y sus controladores; Uaspstor.sys; Media para
audio en el Administrador; fases láser de Canon, cartucho de 1982, CMYK, MFP, FPOT; picolitros,
térmico/piezo, colorante/pigmento; Epson Micro Piezo; Zebra (etiquetas, recibos, pulseras;
durabilidad; luz, calor, roce; impacto); ISO/IEC 24734 y medidas; calendario de controladores (sept.
2023, 15-01-2026, 01-07-2026, 01-07-2027, revisión de mayo de 2025) y Windows 10 21H2; modo de
impresión protegida (ruta, efectos, GPO); WIA, STI, TWAIN, WS-Scan, mensajes de WIA 2.0; Epson
600 × 2400, 1200 × 2400 → 9600 × 9600, 2 × 2,5 a 1200 ppp → 300 ppp, profundidades; MIT 25, 40, 65,
148,5 MHz; Cornell 25,175 MHz y sincronismos activos a nivel bajo; DVI 24/29 contactos, cinco
señales analógicas (H, V, R, G, B), 165 MHz, 200 → 100 MHz, HPD, +5 V; HDMI 1.4b, 2.1 (48 Gbit/s,
2020), 2.2 (96 Gbit/s, 12K@120, 16K@60, Ultra96), VRR, Cable Power, certificación obligatoria, tipos
A/C/D, Alt Mode; DP 2.1 (17-10-2022), DP40/DP80, DP54, DP80LL 2.1b, MST, conversión; T568A/B;
USB 3.2 Gen 1/2/2x2, USB4, Type-C, rótulo 20Gbps/60W, PD 3.1 (28/36/48 V, 240 W); Thunderbolt 4/5
(80/120 Gbit/s, 10GbE, USB4 V2); Bourgeois cap. 2 (1994, 1996, 10-100 m y 300 pies). Cálculos
(cocientes de aspecto, V × A) correctos.

Avisos sin cambio: la tabla RTVE «frente a frente» (DVI sin audio, HDMI «estándar del equipo
doméstico») sigue sin fuente leída y va como oficio (copiado sin cambios; no se re-verifica); los cien
metros del RJ45, oficio declarado.

## Ficheros tocados

- Tema 4 (15 correcciones) y este informe. Ningún otro; la fuente SMPTE ya estaba en el repositorio.
