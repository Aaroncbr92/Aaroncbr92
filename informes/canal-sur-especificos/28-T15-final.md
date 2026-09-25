# Puesto 28 · Operador/a de Sonido · Tema 15 · Fase 5 bis, revisión de lo rematado

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/15-audio-sobre-ip-redes-sincronia-latencia-ptp-y-redundancia.md`.
Fecha de trabajo y de lectura de las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).

Fuentes releídas el 25-09-2026:
- SMPTE ST 2110-30:2025, cl. 7 y tablas 2 y 3 (`fuentes/normas-tecnicas/SMPTE_ST-2110-30-2025.txt`).
- Audinate, *Dante Controller User Guide* 4.18.x (`fuentes/canal-sur/sonido/audinate/dc-latest.txt`):
  «About Transmit Flows», «About Clock Domains», «Sample Rate» pull-up/down (pp. 85-86),
  mensajes de suscripción, «Advanced Routing: Using Multicast».

## Pasajes revisados (los 10 del remate, con énfasis en 2, 3, 5, 6 y 7)

| Pasaje | Resultado |
|---|---|
| 1 Qué se puede preguntar | Correcto |
| 2 Tabla 2 y cl. 7 (más canales; «at least one channel count») | Citas literales; antecedente «la propia norma» correcto |
| 3 Tabla 3 de receptores | Tabla cifra a cifra correcta. **Dos errores corregidos** (abajo) |
| 4 Multicast hasta 64 canales | Literal (p. 132) |
| 5 Saturación de 100 Mbps | Literal |
| 6 «up to 4 channels…», «fifth audio channel» | Literal |
| 7 Pull-up/down y dominios de reloj | Todas las citas literales (+4.1667 %, cinco dominios, «Mismatched clock domains»); «Ese ajuste» tiene antecedente |
| 8 Aplicación práctica de dominios | Matiz corregido (abajo) |
| 9 Extensión 8.700 | Sin cambio |
| 10 Trazabilidad | Correcta |

## Correcciones aplicadas (comprobadas en la fuente)

1. **Error 9/3 (afirmación sin fuente, inexacta)**: «Cada nivel de receptor incluye los de debajo».
   La tabla 3 no lo sostiene en orden: C no incluye AX ni BX (no tiene 96 kHz). Sustituido por la
   lectura exacta de la tabla: todos incluyen el A; B añade 125 µs a 48 kHz; C llega a 64 canales;
   los X añaden 96 kHz; CX recoge todas las combinaciones.
2. **Error 6 (salvedad omitida), grave**: «un emisor de nivel C no tiene por qué emitir en 1 ms»
   contradice la cl. 7: «All senders and receivers shall be compliant to Level A as defined in this
   document.» Todo emisor cumple también el nivel A (48 kHz, 1 ms). Reescrito con esa cita.
3. **Matiz (pasaje 8)**: «un pull-up/down que el otro no tiene» → «no coincide con el del otro»,
   como dice la guía («configured with sample rate pull-up/down that does not match the other device»).

## Lentes

- `indice.py`: sin errores.
- `refutar_prosa.py`: los 3 avisos previos (IP, PTP en el título; TRUE en cita). Sin nuevos.

## Ficheros tocados

El tema 15 y este informe.
