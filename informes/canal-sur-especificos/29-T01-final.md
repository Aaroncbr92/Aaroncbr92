# Puesto 29 · Tema 1 · Fase 5 bis (revisión de lo rematado)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/01-sistemas-de-informacion-y-arquitectura-de-ordenadores.md`.
Alcance: sólo los 12 pasajes que lista `29-T01-remate.md`.

## Fuentes releídas (06-10-2026)

`fuentes/canal-sur/informatico/web/`: `ucm-ec1`, `ucm-ec2`, `ucm-ec4-rendimiento`, `ucm-ec5`,
`ucm-ec6`, `ucm-ec8` (.txt; autor de tema 4 en metadatos del PDF: José Jaime Ruz Ortiz),
`mit-6004-isas.txt`, `arm-glossary-risc.txt`, `arm-glossary-cpu.txt`, `microchip-atmega328p-ds.txt`,
`ms-copilot-pc-npu.txt`, `bourgeois-isbb-2019.txt`, `vonneumann-edvac-1945.txt`.

## Comprobación

- **Negritas**: 55 citas de los pasajes cambiados (§ 2 completo) contrastadas por script contra las
  fuentes con espacios normalizados: 55 literales (la de «Advanced RISC Machine» con comillas
  tipográficas en la fuente).
- **Redonda con dato**: curso 11-12 (temas 1, 2, 5, 6, 8) y 10-11 (tema 4); títulos de los cinco
  temas de la UCM; interrupciones → sincronización con E/S y CPU compartida (UCM 1); microprogramación
  y CISC, compilador en RISC (UCM 1); tabla CISC/RISC fila a fila (UCM 4, «tamaño filo»); CISC de
  longitud variable y RISC popularizado en los ochenta (MIT); saltos y llamadas cargan el PC (MIT,
  «flow control instructions»); niveles y sentido velocidad/capacidad de la jerarquía (UCM 5); bucles
  y estructuras regulares en la localidad (UCM 6); Arm en móviles, tabletas, portátiles, consolas y
  sobremesa (Arm); Snapdragon X Elite «Arm-based» (Microsoft); apartado 7 «AVR CPU Core» (Microchip).
  Todo confirmado.
- Pasajes 1-3, 9-12 (portada, siglas, «Qué se puede preguntar», DDR, NPU, «Lo que no da»,
  Trazabilidad): coherentes con lo anterior; sin datos sin fuente.

## Correcciones aplicadas

| # | Pasaje | Error | Corrección |
|---|---|---|---|
| 1 | § 2 «Los registros y el ciclo de instrucción» | Antecedente (error 1): «la tabla de bloques del epígrafe anterior», pero el anterior es ahora «Los buses» | «de la tabla de bloques de «El modelo de von Neumann»» |
| 2 | § 2 «El modelo de von Neumann», último párrafo | Repetición: «Y el rasgo que define ese modelo…» duplicaba la frase previa | Suprimida; el párrafo empieza en «Los apuntes de…» |
| 3 | § 2 «La arquitectura Harvard» | Afirmación sin fuente (error 9): «Dentro del propio PC hay un eco de Harvard» | Declarada lectura de oficio y añadida a «Oficio sin fuente» de la Trazabilidad |
| 4 | § 2 «RISC y CISC», fila «Acceso a memoria» | Paráfrasis más amplia que la fuente (UCM 4: «Arquitectura RM y MM» / «RR (carga/almacenamiento)») | Reescrita pegada a la fuente; lo de que sólo carga y almacenamiento acceden a memoria lo sostiene también el MIT |

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 35 epígrafes, 9.714 palabras con tablas (la portada
dice 9.200 aproximadamente; se deja). Sin normas: no tocan las demás lentes.

## Ficheros tocados

- El tema 1 del puesto 29.
- Este informe.
