# Puesto 29 · Tema 1 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/01-sistemas-de-informacion-y-arquitectura-de-ordenadores.md`
(680 líneas, unas 7.700 palabras con tablas). Preguntas: `29-T01-preguntas.md`. No se corrige nada:
sólo se informa.

## Fuentes releídas y fecha

Todas el 06-10-2026, sobre las copias de `fuentes/canal-sur/informatico/web/`:
`bourgeois-isbb-2019.txt` (cap. 1 § componentes y definiciones; cap. 2 completo: dispositivo digital,
CPU, placa base, RAM, disco, SSD, red, E/S, Bluetooth, tabla de velocidad; historia del PC en cap. 1),
`vonneumann-edvac-1945.txt` (§ 2.1-2.9), `intel-moores-law.txt`, `ms-win11-requirements.txt`
(«Last updated 2026-07-14»), `ms-win10-lifecycle.txt`, `ms-copilot-pc-npu.txt`,
`usbif-data-performance-language-2024.txt`, `usbif-usb32-language.txt`, `usbif-usb4-language.txt`,
`usbif-usb4.txt`, `usbif-charger-pd.txt`, `usbif-typec.txt`, `intel-tb5-press.txt`,
`thunderbolt-tech.txt`.

Saltado por exactitud (sí mirado por cobertura): los ocho pasajes «Copiado de RTVE sin cambios» del
informe de redacción (tablas de bloques, de hardware, de periféricos y de generaciones; software en
tres capas y por licencia; memoria frente a almacenamiento; tríada CIA). «Copiado del común»: nada.

## Lente 1 · Exactitud

Comprobados contra la fuente, sin hallazgo:

- Definiciones de Laudon y Valacich-Schneider con sus ediciones y años; cinco componentes, «the first
  three are technology», sexto componente; dato-información-conocimiento.
- Bit, byte, palabra, primeros PC de 8 bits, 64 bits hoy.
- EDVAC: CA (§ 2.2), CC (§ 2.3, «no matter what they are … carried out»), M (§ 2.5, «third specific
  part»), C = CA + CC (§ 2.6), I (§ 2.7), O (§ 2.8, «fifth specific part»); memoria «as one organ».
- Bus: definición, placa base, velocidad por frecuencia y anchura. Intel y AMD; hercio y GHz; núcleos;
  caché. Placa base «in different shapes and sizes». RAM volátil, DDR según placa. Disco con plato y
  brazo; SSD con EEPROM, más fiable, combinación SSD + disco. NIC, Ethernet a mediados de los noventa,
  inalámbrica a comienzos de los 2000. Puertos en la placa; USB de 1996; Bluetooth de 10 a 100 m
  («corto alcance» es fiel). Tabla de velocidad: GHz, MHz, Mb/s (millones de bytes), ms, MBit/s.
- Primera CPU a comienzos de los setenta, Altair 8800 (1975), IBM y Microsoft (1981).
- Ley de Moore de Intel, 1965, 1975, «not a scientific law», *Electronics Magazine* 38-8, 19-4-1965.
- Windows 11: siete requisitos, internet, Home con cuenta Microsoft, BitLocker to Go, Hyper-V con
  SLAT y su salvedad, Teams, Hello con PIN o llave, Snap; página del 14-07-2026.
- Windows 10: 14-10-2025, 22H2, LTSC.
- Copilot+: más de 40 TOPS, NPU con CPU y GPU, Snapdragon X Elite Arm, Ryzen AI 300 y Core Ultra
  200V, Administrador de tareas.
- USB: cinco velocidades, nombres al público y técnicos, Basic-Speed y Hi-Speed, USB 3.2 Gen 1/2/2x2,
  USB4 20/40, 80 sobre cables certificados, origen en Thunderbolt, compatibilidad («best mutual
  capability», «lowest common speed»), Type-C reversible, PD 3.1 a 240 W (antes 100 W), sentido de la
  energía, monitor que carga el portátil. Thunderbolt 4 a 40 y 5 a 80/120 Gbit/s sobre USB4 V2,
  DisplayPort 2.1 y PCI Express Gen 4.
- NVMe: definición y «defacto industry standard for PCIe SSDs».

Hallazgos:

| # | Gravedad | Error | Pasaje | Qué pasa |
|---|---|---|---|---|
| 1 | Menor | 9 | § 3 «La memoria»: «En la práctica: un módulo de una generación DDR no sirve en la ranura de otra.» | Bourgeois sólo dice que el tipo de DDR depende de la placa. La incompatibilidad entre generaciones es cierta en el oficio, pero no está en la fuente ni figura en la lista de «Oficio sin fuente» de la Trazabilidad. Declararla como oficio o quitarla |

Observación sin hallazgo: § 2 «El modelo de von Neumann» dice que el informe «propone» tratar toda la
memoria como un solo órgano; la fuente dice **«it is nevertheless tempting to treat the entire memory
as one organ, and to have its parts even as interchangeable as possible»**. La lectura es razonable y
la cita va al lado; no se cuenta.

## Lente 2 · Cobertura del enunciado

| Rúbrica del enunciado | Cubierta |
|---|---|
| Elementos constitutivos de un sistema de información | Sí (cinco componentes y sexto) |
| Características | Sí, con el hueco declarado (sin lista en fuente) y la tríada CIA |
| Funciones | Sí |
| Arquitectura de ordenadores | **A medias**: von Neumann, buses, generaciones y Moore; faltan piezas que un test de arquitectura pregunta (abajo) |
| Componentes internos de los equipos microinformáticos | Sí en lo esencial; fuente de alimentación, refrigeración, chipset, DDR5 y PCIe declarados en «Lo que este tema no da» |
| Tecnologías actuales aplicables al puesto de usuario | Sí (Windows 11, fin de Windows 10, NPU, USB-C/USB4/Thunderbolt, PD) |

Preguntas: 11 enteras, 1 a medias, 3 no. Lagunas, todas en «Arquitectura de ordenadores», para que el
remate (Opus, amplía) las cubra con fuente técnica leída:

1. **Nombre de la arquitectura Harvard** (pregunta 5). El tema describe la alternativa a von Neumann
   sin nombrarla.
2. **Registros de la CPU y ciclo de instrucción** (pregunta 8): contador de programa, registro de
   instrucción, acumulador o registros generales, y las fases búsqueda-descodificación-ejecución. Hoy
   sólo hay media línea en la tabla copiada de RTVE.
3. **Jerarquía de memoria** (pregunta 9): registros, caché (niveles L1, L2, L3), RAM y almacenamiento,
   con el criterio velocidad-capacidad-coste.
4. **RISC frente a CISC** (pregunta 10): el tema nombra Arm (Snapdragon) sin decir qué es; x86 frente
   a Arm es «tecnología actual del puesto» además de arquitectura.

No es laguna, pero conviene saberlo: las preguntas sobre fuente de alimentación o chipset no se
contestan; el tema lo declara.

## Recuento

- Graves: 0.
- Menores: 1.
- Lagunas: 4 (3 «no» y 1 «a medias»).

## Ficheros tocados

Creados `29-T01-preguntas.md` y este informe. Ningún otro; el tema no se ha modificado.
