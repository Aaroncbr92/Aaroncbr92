# Puesto 29 · Tema 4 · Revisión del remate (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Opus, distinto del rematador.
Alcance: sólo los pasajes que lista `29-T04-remate.md` (localizados con `git diff` contra el último commit).
Fuentes releídas el 06-10-2026 en `fuentes/canal-sur/informatico/web/`: `ms-wppm`, `eizo-cms-02`,
`usbif-micro-usb-1.01`, `usbif-cabconn20`, `panduit-55275732`, `fluke-crossover-dsx`, `fluke-t568`
(ya citada en el tema), `cisco-3750-higcable`, `cisco-automdix-9300`.

## Literalidad

44 negritas añadidas, cotejadas por script contra los .txt (espacios normalizados): todas presentes en
la fuente que se les atribuye. Tabla EIZO (columnas IPS/VA/TN) y tabla 4-1 Micro-USB cotejadas fila a fila: bien.

## Datos y antecedentes comprobados sin cambio

- Micro-USB rev. 1.01, 04-04-2007; § 1.3 (móvil, 10.000 ciclos), cap. 2 (A-device/B-device), § 3.3, § 3.4
  (receptáculos sólo en adaptadores), tabla 4-1: bien. Cables and Connectors Class Document rev. 2.0,
  agosto 2007, longitudes 5 m / 4,5 m / 2 m en el apartado de certificación: bien.
- Panduit TR103: T568A/B straight-through; Fluke DSX: mismo código en los dos extremos; Cisco 3750
  (OL-6336-10, ap. B): pin 1→3, 2→6; tabla de estados auto-MDIX (enlace cae sólo con Off/Off): bien.
- Deducción T568A+T568B = cruzado: apoyada en Fluke (intercambio naranja/verde 1-2/3-6), declarada.
- Antecedentes: «Fluke, más arriba», «Es el auto-MDIX de Cisco», «Sin esa función», «la misma página
  de arriba» (Trazabilidad, línea anterior cita «Windows Protected Print Mode»): todos tienen delante su antecedente.
- Escáneres en impresión protegida (ep. 2 y caso 6): literal y sentido, bien.

## Correcciones aplicadas (comprobadas en la fuente)

| # | Error | Antes | Después | Fuente |
|---|---|---|---|---|
| 1 | 9 (generaliza) | «En los conmutadores de Cisco viene activada de serie» | «En los Catalyst 9300 de Cisco, los de la guía leída, viene activada de serie» | `cisco-automdix-9300`: sólo documenta Catalyst 9300 |
| 2 | 9 | Trazabilidad: «guía de configuración de interfaces de los Catalyst 9300 (versión 16.10)» | «documentación de los Catalyst 9300 (Cisco IOS XE), capítulo "Configuring Auto-MDIX"» | «16.10» no aparece en el .txt ni en los metadatos del PDF; sí «Cisco IOS XE Everest 16.5.1a» (historial) |
| 3 | 9 (generaliza) | «los que cruzan los cuatro pares (full crossover) llegan a 1 Gbit/s» | «los de Panduit cruzan los cuatro pares … y llegan a» | Panduit, líneas 153-154: lo dice de sus cordones |
| 4 | 6 salvedad | «Hoy el cruzado casi no hace falta … (Panduit)» | se añade que, según Panduit, muchos instaladores siguen prefiriendo el cruzado para toda conexión directa | Panduit, líneas 147-149 |
| 5 | 8 precisión | «la norma de cableado no lo define» | «la ANSI/TIA-568-C.2 no lo define» | La cita es de la edición C.2; el tema cita en otro sitio la 568.2-D |

## Aceptado sin tocar

- USOC sin desarrollar (M1) y LCD/IPS/VA/TN sin desarrollar: declarado en siglas, ninguna fuente leída los desarrolla.
- «Standard-B en la impresora»: oficio declarado.
- Caso 5 («cruza dos pares y se queda en 10/100»): apoyado en Panduit + deducción declarada.

## Ficheros tocados

El tema (`temas/canal-sur-especificos/29-operador-a-informatico/04-perifericos-y-conectividad-del-puesto-informatico.md`)
y este informe. La extensión de la portada (10.700) sigue valiendo (+≈30 palabras).

Tema 4 cerrado.
