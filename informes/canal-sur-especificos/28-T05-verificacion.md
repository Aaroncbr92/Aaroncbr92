# Puesto 28 · Operador/a de Sonido · Tema 5 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/05-procesamiento-de-audio.md`.
Fecha de lectura de todas las fuentes: 25-09-2026 («hoy» del encargo: 24-09-2026).

## Fuentes releídas

| Fuente | Cómo | Fecha |
|---|---|---|
| Rane, RaneNote 155 (Jeffs, Holden, Bohn, septiembre 2005) | Página original ranecommercial.com/legacy/note155.html, descargada y pasada a texto | 25-09-2026 |
| EBU R 128-2023 (V5, noviembre 2023) | `fuentes/normas-tecnicas/EBU_R128-2023.txt` (punto m), definiciones, historial de versiones) | 25-09-2026 |
| EBU Tech 3343-2023 (V4) | `fuentes/normas-tecnicas/EBU_Tech3343-2023.txt` | 25-09-2026 |
| EBU R 68-2000 | `fuentes/normas-tecnicas/EBU_R68-2000.txt` (sólo comprobación de pasaje) | 25-09-2026 |

## Pasajes exentos (comprobación sólo de literalidad)

- **Copiado del común** (Cámara T06): los tres bloques listados son subcadena exacta del tema de
  Cámara (script, sin saltos de línea). No se re-verifican.
- **Copiado de RTVE sin cambios**: los 16 pasajes son subcadena del RTVE 07/08 quitando `**` y ✔,
  salvo tres retoques menores de forma que el informe de redacción no declaró: «El compresor
  multibanda…» y «En un gráfico el Q está fijo…» cambian mayúsculas («el»→«El», «FIJO»→«fijo»),
  y la cabecera «Opción» de la tabla del *headroom* pasa a «Concepto». Contenido idéntico; no
  se re-verifican.

## Verificado y confirmado

- 44 citas en negrita cotejadas por script contra las fuentes: 41 casan literalmente; las 3 que no
  (R 68 y Tech 3343, en pasajes del común) fallan por artefactos del PDF (nota «2» pegada,
  columnas intercaladas); comprobadas a mano, son literales.
- Rane: umbral −40/+20 dBu («workable range for compressors»), −60 dBu del expansor, ataque
  0-250 ms (expansores con puerta y *ducker*), relajación 25 ms-2 s, *hold* 0-3 s, profundidad
  0/−80 dB, unos 80 dB de la puerta, usos del limitador, usos y defectos de la puerta, *look-ahead*.
- R 128 punto m) y definición de *Maximum True Peak Level*; V5 de noviembre de 2023; Tech 3343 V4
  de noviembre de 2023; −2 dBTP para MPEG-1 Layer 2 y AC-3.
- Cálculos rehechos: Q = √(2ᴺ)/(2ᴺ−1) → 1,41 / 0,67 / 2,87 / 4,32; campana 707-1.414 Hz;
  compresor 4:1 → −17 dBFS (9 dB), 2:1 → −14 dBFS (6 dB); 60.000/102 = 588 → 1.176/294/147 ms.
- Remisiones a otros temas (1, 2, 3, 4, 9) comprobadas en sus ficheros: timbre, desfase del
  ecualizador, ondas estacionarias, RT60, filtro en peine (tema 1); +4/+26 dBu y 22 dB (tema 2,
  RaneNote 135); latencia (tema 9). Los temas 10 y 13 aún no existen; la remisión casa con su enunciado.

## Correcciones aplicadas (7)

1. **Ejemplo del expansor (error 9/interpretación)**: el tema decía «ruido 10 dB bajo el umbral
   sale 20 dB bajo». Rane mide el escalón desde el nivel más flojo de la voz, no desde el umbral.
   Reescrito: escalón de −10 dB al ruido de fondo → −20 dB a la salida (2:1 dobla la caída).
2. **Detector del limitador (error 9, cita indirecta)**: el tema lo apoyaba en la frase de Rane
   sobre la puerta y añadía «no de valor medio» sin fuente. Sustituido por la cita directa de Rane
   sobre el limitador («peak responding detector and a fixed ratio of infinity:1») y la del
   compresor («An rms detector is typically used»).
3. **Tabla expansor/puerta**: la celda «Detector» del expansor estaba vacía; Rane lo da: «True rms
   detection is necessary for compressor and expander modes».
4. **Ducker (error 1, antecedente)**: «el procesador inverso» no tenía antecedente. Ahora «trabaja
   al revés que la puerta», con la cita de Rane; se añaden los usos de Rane (*paging*, *talkover*);
   la música bajo la voz queda declarada como oficio.
5. **Salvedad de la R 128 (error 6)**: añadida la del mismo punto m): «Permitted Maximum True Peak
   Levels may be lower for different distribution systems and data reduction rates»; reflejada en
   la tabla de recomendaciones y en Trazabilidad.
6. **«Ninguna norma legal regula el procesamiento de audio» (error 9)**: afirmación absoluta sin
   fuente; cambiada a «El tema no invoca ninguna norma legal».
7. **Trazabilidad**: quitada la mención al material de investigación (proceso, no fuente); fila de
   Rane ampliada con lo nuevo. Extensión de la ficha: 7.950 palabras (`indice.py`).

Relectura de los pasajes cambiados: cada «Rane», «el mismo punto», «la puerta» tiene su antecedente.

## Sin fuente, se mantiene como oficio declarado

«De las cuatro, la de respuesta más rápida es el VCA» (adaptado de RTVE) repite la fila de la tabla
exenta; no lo confirma ninguna fuente leída (Rane no compara tecnologías). Queda como oficio; aviso
para la refutación.

## Lentes

Tema técnico sin norma legal: `refutar_prosa.py` 0 hallazgos; `indice.py` 7.955 palabras,
40 epígrafes, índice sin cambios.

## Otros ficheros tocados

Ninguno fuera del tema y este informe.
