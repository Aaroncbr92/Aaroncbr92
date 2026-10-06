# Puesto 29 · Tema 1 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/01-sistemas-de-informacion-y-arquitectura-de-ordenadores.md`.
Entrada: `29-T01-refutacion.md` (1 hallazgo menor, 4 lagunas) y `29-T01-preguntas.md` (11 enteras,
1 a medias, 3 no). **Se amplió el tema** con contenido nuevo: hace falta la fase 5 bis sobre los
pasajes listados abajo.

## Fuentes nuevas, leídas el 06-10-2026

Guardadas en `fuentes/canal-sur/informatico/web/`:

| Fichero | Fuente | Para qué |
|---|---|---|
| `ucm-ec1.pdf/.txt` | UCM, *Estructura de Computadores*, tema 1 (curso 11-12), fdi.ucm.es/profesor/jjruz/WEB2/Temas/EC1.pdf | Von Neumann vigente y sus 5 características; interrupciones, caché, memoria virtual; ruta de datos; CISC y RISC |
| `ucm-ec2.pdf/.txt` | Ídem, tema 2 | «El procesador ARM es un RISC con 16 registros de 32 bits» |
| `ucm-ec5.pdf/.txt` | Ídem, tema 5 | Jerarquía de memoria (figura comprobada en imagen: velocidad hacia arriba, capacidad hacia abajo), ubicación interna/externa, copia entre niveles |
| `ucm-ec6.pdf/.txt` | Ídem, tema 6 | Caché, localidad temporal y espacial, L2 entre L1 y Mp, cachés separadas o unificadas |
| `ucm-ec8.pdf/.txt` | Ídem, tema 8 | PC y registro de estado salvados en la pila al atender una interrupción |
| `ucm-ec4-rendimiento.txt` (ya estaba) | Ídem, tema 4 (curso 10-11) | Tabla CISC/RISC (comprobada en imagen de la p. 33; «tamaño filo» es errata de la fuente por «fijo», se da en redonda) y segmentación |
| `mit-6004-isas.txt` | MIT 6.004 *Computation Structures*, cap. 14 «Instruction Set Architectures», S. Ward | Contador de programa, incremento, *fetch/execute loop*, ISA como interfaz, CISC de longitud variable, RISC de los ochenta |
| `arm-glossary-risc.txt`, `arm-glossary-cpu.txt` | Arm, glosario (arm.com/glossary/risc y /cpu) | RISC: un ciclo, longitud fija, rendimiento por vatio, «Advanced RISC Machine»; registros, caché L1-L3, ciclo de instrucción en 4 fases, *pipelining* |
| `microchip-atmega328p-ds.txt` | Microchip, hoja de datos ATmega48A…328/P, DS40002061B (2020), ap. 7 (páginas extraídas) | Arquitectura Harvard nombrada: memorias y buses separados; búsqueda anticipada |

Cada cita en negrita añadida se ha comprobado por script contra estas fuentes (espacios normalizados):
todas aparecen literalmente.

## Correcciones de la refutación

| # | Qué dijo el informe | Comprobación | Qué se hizo |
|---|---|---|---|
| 1 | La incompatibilidad DDR entre generaciones no está en Bourgeois | Confirmado: Bourgeois sólo dice que el tipo depende de la placa | Se mantiene declarada como oficio en el texto y se añade a «Oficio sin fuente» de la Trazabilidad |
| Obs. | «propone» tratar la memoria como un órgano | No se cuenta como hallazgo | Sin cambio |

## Lagunas cubiertas (se amplía el tema, ninguna pregunta se recorta)

| Pregunta | Laguna | Dónde se cubre ahora |
|---|---|---|
| 5 (No) | Nombre de la arquitectura Harvard | § 2, nuevo «La arquitectura Harvard» (Microchip AVR + tabla comparativa + cachés separadas de la UCM) |
| 8 (No) | Registros, contador de programa, ciclo de instrucción | § 2, nuevo «Los registros y el ciclo de instrucción» (MIT, Arm, UCM 1, 4 y 8) |
| 9 (A medias) | Jerarquía de memoria y niveles de caché | § 2, nuevo «La jerarquía de memoria» (UCM 5 y 6, Arm) |
| 10 (No) | RISC frente a CISC; Arm | § 2, nuevo «RISC y CISC» (UCM 1, 2 y 4, MIT, Arm) |

Con lo añadido las 15 preguntas se contestan enteras con el tema.

## Pasajes cambiados (para la fase 5 bis)

1. Portada: «Fuente» (añade UCM, MIT, Arm, Microchip), «Redacción que se estudia» (05 y 06-10-2026),
   «Extensión» (9.200 palabras aproximadamente).
2. Siglas: añadidas RISC, CISC, CPI, ISA, contador de programa (PC, con aviso frente a ordenador
   personal), L1/L2/L3, AVR.
3. «Qué se puede preguntar»: von Neumann frente a Harvard; contador de programa y ciclo de
   instrucción; jerarquía y principio de la caché; RISC/CISC y Arm.
4. § 2 «El modelo de von Neumann», último párrafo: sustituida la frase de oficio sobre la alternativa
   en microcontroladores por la vigencia del esquema (UCM), sus cinco características literales y las
   tres aportaciones (interrupciones, caché, memoria virtual).
5. § 2, nuevo epígrafe «La arquitectura Harvard».
6. § 2, nuevo epígrafe «Los registros y el ciclo de instrucción» (tras «Los buses»).
7. § 2, nuevo epígrafe «La jerarquía de memoria».
8. § 2, nuevo epígrafe «RISC y CISC».
9. § 3 «La memoria»: la frase DDR pasa a «Que un módulo de una generación DDR no sirva en la ranura de
   otra es regla de oficio: la fuente sólo dice que el tipo lo decide la placa.»
10. § 4 «La NPU y los equipos Copilot+»: «de arquitectura Arm (RISC, epígrafe 2)».
11. «Lo que este tema no da»: añadidos el registro de instrucción y demás registros especiales, la
    adscripción de x86 a CISC (ninguna fuente leída lo dice expresamente) y el coste por bit de la
    jerarquía.
12. «Trazabilidad»: cuatro filas nuevas (UCM, MIT, Arm, Microchip); «Oficio sin fuente» actualizado
    (comparación von Neumann/Harvard como regla, columna «Dónde está» de la jerarquía y su ejemplo
    práctico, incompatibilidad DDR).

Antecedentes releídos: «el mismo tema», «los mismos apuntes», «esa arquitectura», «el epígrafe
anterior» tienen delante su referente en cada pasaje.

## Lentes

Tema técnico sin norma: `indice.py` (índice regenerado, 35 epígrafes, 9.691 palabras con tablas) y
`refutar_prosa.py` (0 hallazgos tras presentar AVR). `negritas.py`, `refutar_exactitud.py` y
`refutar_modo.py` no tocan: el tema no cita normas.

## Ficheros tocados

- El tema 1 del puesto 29.
- Fuentes añadidas en `fuentes/canal-sur/informatico/web/`: `ucm-ec1`, `ucm-ec2`, `ucm-ec5`,
  `ucm-ec6`, `ucm-ec8` (.pdf y .txt), `mit-6004-isas.txt`, `arm-glossary-risc.txt`,
  `arm-glossary-cpu.txt`, `microchip-atmega328p-ds.txt`.
- Este informe.
