# Puesto 28 · Operador/a de Sonido · Tema 5 · Fase 5 bis

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/05-procesamiento-de-audio.md`.
Alcance: sólo los pasajes listados en `28-T05-remate.md`. Fecha de trabajo y de lectura de fuentes:
25-09-2026 («hoy» del encargo: 24-09-2026).

## Fuentes releídas

| Fuente | Cómo | Fecha |
|---|---|---|
| RaneNote 155 (Jeffs, Holden, Bohn, septiembre de 2005) | ranecommercial.com/legacy/note155.html, pasada a texto | 25-09-2026 |
| RaneNote 160 (Bohn, octubre de 2005) | ranecommercial.com/legacy/note160.html | 25-09-2026 |
| RaneNote 101 (Bohn, 1982 y 1987, rev. 11/05) | ranecommercial.com/legacy/note101.html | 25-09-2026 |
| RaneNote 122 (Bohn, 1990, rev. 8/97) | ranecommercial.com/legacy/note122.html | 25-09-2026 |

## Comprobado sin cambios

- Umbral −40 a +20 dBu; ataque de compresores 25-500 ms; expansores y puertas 0-250 ms (la remisión
  a «Los parámetros de la puerta» existe y da 0-250 ms); relajación 25 ms-2 s: literales en RN155.
- Salvedad de la relajación: «no industry standard», definición de 10 dB, «not how long it takes to
  return to unity gain», fórmula y ejemplo 5 dB/1 s → 0,5 s: literales en RN155.
- Tabla de voz («Vocals 25 ms to 100 ms 100 ms to 500 ms 2:1 to 4:1 Soft», «starting points»): RN155.
- «VCAs dominate» (diseños analógicos): RN155; la velocidad, marcada como oficio. Correcto.
- Regla de 6 dB/octava (20 dB/década) por orden y ejemplo de 4.º orden: literales en RN160.
- «with 10 to 31 bands on octave to 1/3-octave spacing» (realce y corte, «the most common»): RN122.
- Siglas ISO, «Qué se puede preguntar», fila de RN155 en Trazabilidad: correctos.
- Antecedentes: «ese margen», «la regla», «Rane», «ver …» tienen su antecedente.

## Corregido (comprobado en la fuente)

1. Gráficos (error 8/9, atribución): la frase atribuía a RN122 las «posiciones normalizadas por la
   ISO»; quien dice que en los gráficos los centros son fijos en posiciones ISO es RN101. Además, RN101
   no dice que los gráficos «se repartan» en 15 y 30 bandas, sino que se dividen en dos grupos
   **dominados** respectivamente por ellos. Reescrito el pasaje.
2. Pendiente (error 9): 12 y 18 dB/octava no están en RN160; son cálculo. Se dice en el texto
   («aplicando la regla») y se añaden a la lista de cálculo de Trazabilidad; el 4.º orden se atribuye
   al ejemplo de Rane.
3. Trazabilidad RN122: faltaba la fecha (1990, revisada en agosto de 1997).
4. «Lo que este tema no da»: decía las tecnologías de compresor «sin documento de fabricante
   leído»; se añade la salvedad del predominio del VCA, que sí da Rane.
5. Ficha, Extensión: 8.530 → 8.590 (`indice.py`: 8.585).

## Lentes

`indice.py`: 8.585 palabras, 40 epígrafes. `refutar_prosa.py`: 0 hallazgos.

## Otros ficheros tocados

Sólo el tema 5 y este informe.
