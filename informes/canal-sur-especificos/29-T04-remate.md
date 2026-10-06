# Puesto 29 · Tema 4 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Opus (amplía).
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/04-perifericos-y-conectividad-del-puesto-informatico.md`
(9.642 → ≈10.670 palabras; 36 → 38 epígrafes). Copia previa en el scratchpad de la sesión.

## Correcciones de la refutación

| # | ¿Se aplica? | Comprobación en la fuente (06-10-2026) | Pasaje cambiado |
|---|---|---|---|
| M1 | Sí | `fluke-t568.txt` sólo dice «USOC wiring schemes»; ni USOC ni RJ se desarrollan en ninguna fuente leída | Siglas: «conector registrado 45 (RJ45)» → «conector RJ45»; fuera «(*Universal Service Ordering Code*)». `refutar_prosa.py` marca ahora USOC como sigla sin presentar: se deja así a sabiendas (presentarla sería inventar) |
| M2 | Sí | `ms-wppm.txt`, líneas 68 y 82: literales confirmados | Ep. 2, «El modo de impresión protegida»: viñeta nueva con las dos citas de los escáneres. Caso 6: frase final sobre el escáner de la multifunción |

## Lagunas (ampliación)

| # | Pregunta | Fuentes nuevas (descargadas y leídas el 06-10-2026, en `fuentes/canal-sur/informatico/web/`) | Pasaje añadido |
|---|---|---|---|
| L1 | 9 | `panduit-55275732` (TR103, *Patch Cord Wiring Guide*), `fluke-crossover-dsx`, `cisco-3750-higcable` (OL-6336-10, ap. B), `cisco-automdix-9300` (Catalyst 9300, 16.10) | Ep. 7, «RJ45»: tres párrafos nuevos antes de «Y el par trenzado…»: directo (T568A/B son straight-through; el cableado estructurado exige el mismo código en los dos extremos), cruzado (definición Panduit; identificación Cisco pin 1→3, 2→6), T568A+T568B = cruzado de dos pares (deducción propia declarada, de Fluke + Cisco), límite 10/100 y «full crossover» a 1 Gbit/s, auto-MDIX (detección, activado de serie, tabla de estados). Caso 5: frase nueva sobre dos equipos sin conmutador |
| L2 | 15 | `eizo-cms-02` (EIZO Library, «LCD Monitors for Color Management Systems», sin fecha) | Ep. 4, epígrafe nuevo «El panel del monitor: IPS, VA y TN»: tabla de EIZO (ángulo, respuesta, contraste, precio), gama no dependiente del panel, cita del ángulo de visión, recomendación para gráficos, aviso de que la página no está fechada |
| L3 | — | `usbif-micro-usb-1.01` (Micro-USB 1.01, 04-04-2007; copia en PDF), `usbif-cabconn20` (usb.org, rev. 2.0, agosto 2007) | Ep. 7, epígrafe nuevo «Los conectores USB anteriores: Standard, Mini y Micro»: conectores de USB 2.0 y Micro-USB, tabla 4-1 de receptáculos, A-device/B-device, Micro-AB sólo OTG, origen del Micro, cables admitidos, longitudes máximas para certificar (5 m / 4,5 m / 2 m). «Standard-B en la impresora» declarado como oficio |

Pregunta 6 (a medias): hueco ya declarado, no se toca.

## Otros pasajes cambiados

- Portada: «Fuente» amplía la lista; «Extensión» 9.000 → 10.700 palabras aproximadamente.
- Siglas: LCD, IPS, VA y TN (declarado que las fuentes no las desarrollan), OTG, auto-MDIX.
- «Qué se puede preguntar»: tipos de panel; conectores Standard, Mini y Micro; directo, cruzado y auto-MDIX.
- «Lo que este tema no da»: la línea de paneles queda en OLED, el desarrollo de IPS/VA/TN, cámaras, auriculares y altavoces.
- «Trazabilidad»: bloque «Añadidas en el remate, leídas el 06-10-2026»; en «Oficio» se suma el Standard-B de la impresora; se declara la deducción propia del cruzado.

Antecedentes releídos: «Fluke, más arriba» remite a la cita de T568A/B del mismo epígrafe; «Es el auto-MDIX de Cisco» tiene delante la sigla presentada; «la misma página de arriba» (Trazabilidad) remite a «Windows Protected Print Mode».

## Lentes

- Literalidad de las negritas nuevas: cotejadas por script contra las fuentes (espacios normalizados): todas presentes.
- `indice.py`: índice regenerado, 38 epígrafes.
- `refutar_prosa.py`: 2 avisos de siglas (EIZO, nombre de empresa; USOC, sin desarrollo por M1). Aceptados.
- Tema técnico sin norma: no se corren `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

El tema; este informe; fuentes nuevas en `fuentes/canal-sur/informatico/web/`: `cisco-automdix-9300.{pdf,txt}`,
`cisco-3750-higcable.{pdf,txt}`, `panduit-55275732.{pdf,txt}`, `fluke-crossover-dsx.{html,txt}`,
`eizo-cms-02.{html,txt}`, `usbif-micro-usb-1.01.{pdf,txt}`, `usbif-cabconn20.{pdf,txt}`.

Fase 5 bis necesaria: sí (se amplió contenido nuevo).
