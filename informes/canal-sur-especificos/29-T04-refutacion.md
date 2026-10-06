# Puesto 29 · Tema 4 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). No corrijo: el tema queda como estaba.
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/04-perifericos-y-conectividad-del-puesto-informatico.md`
(887 líneas, 9.642 palabras).

## Alcance

- «Copiado del común»: nada. «Copiado de RTVE sin cambios» (`29-T04-redaccion.md`): la tabla de
  clasificación de periféricos y sus dos párrafos (ep. 1), la tabla de relaciones de aspecto y sus dos
  párrafos (ep. 4), la tabla «frente a frente» y la frase DVI-A/D/I (ep. 7). Esos pasajes no se miran
  en exactitud; sí en cobertura. Lo adaptado de RTVE (párrafo final de «frente a frente», RJ45) sí se
  mira.
- Fuentes: los volcados de `fuentes/canal-sur/informatico/web/` (descargados el 05-10-2026), releídos
  el **06-10-2026** en los pasajes concretos: `ms-print-driver-eos`, `ms-wppm`, `ms-usb-classes`,
  `ms-multiple-monitors`, `vesa-dp-home`, `vesa-dp21-press`, `hdmi-14b`, `hdmi-uhs-cable`,
  `hdmi-passive`, `intel-tb5-press`, `thunderbolt-tech`, `usbif-usb32-language`, `usbif-charger-pd`,
  `usbif-typec`, `fluke-t568`, `zebra-thermal`, `canon-laser-tech`, `canon-inkjet-2021`,
  `epson-heat-free`, `epson-scanner-brief`, `mit-6111-lab3-vga`, `cornell-ece4760-vga-adapter`,
  `bourgeois-isbb-2019`. Nada descargado de nuevo.
- Lentes: tema técnico sin norma; la literalidad de las negritas ya la cotejó por script la
  verificación (210 fragmentos). Aquí se mira la redonda, las glosas, las atribuciones y la cobertura.

## Lente 1 · Exactitud

Comprobado contra la fuente y correcto: calendario de controladores de impresora (sept. 2023, 15-01-2026
con su salvedad, 01-07-2026, 01-07-2027, revisión de mayo de 2025) y Windows 10 21H2 con Mopria; ruta,
efectos y GPO del modo de impresión protegida; Usbhub/Usbhub3, Usbaudio y clase *Media*, Usbstor
«port driver»; Identify, Detect, Apply, Windows + K «Cast», Windows + P; DP40/DP80, DP54, DP80LL
(2.1b, tres metros), DSC «mandated support» y 67 %, MST, conversión y bases USB con HDMI, conector con
retención, «industry replacement for DVI, LVDS and VGA»; HDMI 1.4b (4K, HEC, Micro, Alt Mode),
certificación obligatoria de Ultra96 y Ultra High Speed; Thunderbolt 4/5, 10GbE, cita de Microsoft
en la nota de Intel; USB 3.2 «lowest common speed», PD para discos e impresoras; T568A/B
(preferida, AT&T 258A, compatibilidad USOC de uno y dos pares); térmicas (etiquetas, recibos,
pulseras; luz, calor y roce); Canon (1982, piezas de desgaste); Epson Micro Piezo; escáner
(600 × 2400, 1200 × 2400 → 9600 × 9600, 2 × 2,5 a 1200 ppp → 300 ppp, profundidades); MIT (25, 40, 65,
148,5 MHz; 0,7 V; 75 Ω); Cornell (25,175 MHz, sincronismos activos a nivel bajo); Bourgeois (1994,
1996, 10-100 m y 300 pies).

### Hallazgos

| # | Gravedad | Error | Pasaje | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|
| M1 | Menor | 9 afirmación sin fuente | Siglas: «el esquema de cableado USOC (*Universal Service Ordering Code*)» y «conector registrado 45 (RJ45)» | Fluke sólo dice **«USOC wiring schemes»**; ninguna fuente leída desarrolla USOC ni RJ | Dejar «el esquema de cableado USOC» y «conector RJ45» sin desarrollo, o leer una fuente que lo dé y citarla |
| M2 | Menor | 6 salvedad omitida | Ep. 2, «El modo de impresión protegida»: «Efectos que hay que conocer antes de activarlo» (desinstala controladores de terceros; quita XPS y fax; GPO) | La misma página (`ms-wppm`): **«Some compatible devices' scanners are unavailable in Windows protected print mode. To see if a device's scanner works in Windows protected print mode, check if it is a Mopria certified product.»** y **«If it is not Mopria certified, only printing functionalities will be available in Windows protected print mode.»** | Añadir una viñeta con esa salvedad (y una frase en el caso 6: en una multifunción, comprobar también el escáner) |

Sin hallazgo en: cita cruzada (1: remisiones a epígrafes y a los temas 1, 3, 6 y 13 cuadran), ley por
reglamento (2), recuentos (3: cinco velocidades, cinco señales VGA, 24/29 contactos, tres conectores
DP, cuatro carriles), «podrá»/«deberá» (4: «must», «required», «mandatory», «can still be updated»
bien llevados), siglas presentadas (5), redacción derogada (7: HDMI 2.2 vigente, 2.1 sólo por su
cable; DP 2.1 con fecha), artículo mal (8). Nota sin hallazgo: la frase de `ms-print-driver-eos`
sobre los controladores existentes va en la fuente detrás de la fila de 01-07-2027; el tema la da como
salvedad general, lo que sigue siendo cierto. Caso 2 («convertidor activo, no un adaptador de cable»):
oficio, amparado por la advertencia de cabecera del epígrafe 8.

## Lente 2 · Cobertura

Cubre todo el enunciado en su orden: impresión, almacenamiento, visualización, digitalización,
multimedia; USB, RJ45, VGA, DVI, HDMI y DisplayPort. Quince preguntas en `29-T04-preguntas.md`:
11 enteras, 1 a medias, 3 no.

| # | Laguna | Pregunta | Propuesta |
|---|---|---|---|
| L1 | Cable directo y cruzado con RJ45 | 9 (no) | Dos líneas en «RJ45»: directo = misma asignación en los dos extremos; cruzado = T568A en uno y T568B en otro, con fuente (Fluke u otra técnica); y si procede, que el autoajuste de los puertos actuales lo hace innecesario, sólo con fuente |
| L2 | Tecnologías de panel (TN, IPS, VA, OLED) | 15 (no) | El tema lo declara en «Lo que no da», pero «visualización» es materia del enunciado y pregunta típica: buscar fuente técnica (fabricante o manual universitario) y ampliar § 4 |
| L3 | Tipos de conector USB (Standard-A/B, Mini, Micro-B) | — (el tema sólo los nombra dentro de citas) | Una tabla corta con los conectores y su uso, con fuente USB-IF; es «conectividad USB» del enunciado |

La pregunta 14 (no) se debe a M2; la 6 (a medias) a un hueco ya declarado (reloj de 2560 × 1440),
aceptable.

## Resumen

0 graves, 2 menores (M1, M2), 3 lagunas (L1-L3; ampliación, Opus en el remate).

## Ficheros tocados

`informes/canal-sur-especificos/29-T04-preguntas.md` y este informe. El tema no se ha tocado.
