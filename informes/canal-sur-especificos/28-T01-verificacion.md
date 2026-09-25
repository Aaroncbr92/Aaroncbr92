# Puesto 28 · Operador/a de Sonido · Tema 1 · Fase 3, verificación

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/01-fundamentos-de-sonido.md`.

## Pasajes copiados: sólo comprobación de literalidad

Script de cotejo frase a frase (sin `**` ni ✔, espacios normalizados) contra el tema 6 de Cámara
Operador y contra RTVE `sonido/02`, `sonido/04` y `edicion-montaje/03`.

- **Copiado del común** (4 pasajes): literales. La cita de DPA sobre los 6 dB por distancia doble
  está igual en el tema 6 de Cámara.
- **Copiado de RTVE sin cambios** (15 pasajes): todas sus frases y filas de tabla son subcadena de
  su fuente. No se re-verifican.
- Frase no listada y tratada como nueva: «Las superficies que favorecen … son las paralelas»
  (reformulación de la respuesta RTVE; oficio, correcta).

## Fuentes releídas

| Fuente | Fecha de lectura | Resultado |
|---|---|---|
| RD 2032/2009, BOE-A-2010-927, `boe.py precepto` bloques `cii` (vig. 30-04-2020, BOE-A-2020-4707) y `civ` (redacción única, vig. 22-03-2010) | 25-09-2026 | Tabla 3 (título, filas frecuencia/hercio/Hz/s−1 y presión, tensión/pascal/Pa/N/m2), nota (d), cap. IV apartado 4, título de la tabla 8, fila del bar, belio y decibelio y nota (i): todo literal y bien situado |
| API de datos abiertos del BOE, metadatos de BOE-A-2010-927 | 25-09-2026 | Publicado en el **BOE núm. 18, de 21-01-2010** |
| DPA, «Polarity, phase and delay» (E. Bøgh Brixen), web | 25-09-2026 | 10 citas literales; paráfrasis (tres causas del desfase, ejemplo 1 y 2 kHz, patilla 2, ondas distintas que suenan igual) conformes |
| DPA, «The basics about comb filtering (and how to avoid it)» (E. Bøgh Brixen), web | 25-09-2026 | 6 citas literales; dos orígenes, caso de *talk studio* y remedios por reflexión conformes; 4,5:1 con salvedad omitida (ver abajo) |
| Rane, RaneNote 155 (R. Jeffs, S. Holden, D. Bohn, «written September 2005»), web | 25-09-2026 | 2 citas literales; autores y fecha correctos |
| RTW, «Focus: The Multi Correlator», T. Valter, 9-08-2019, web | 25-09-2026 | 3 citas literales; título, autor y fecha correctos |

Cálculos rehechos (todos correctos): tabla de periodos y longitudes de onda; 2¹⁰; 20 × log 10⁶;
tabla de aritmética (×1,41 → 3,01/1,5 dB; ×4 → 12/6 dB); 6,02 dB por bit, 96/144 dB; 1 ms → 360°,
180°, 90° a 1 kHz, 500 Hz, 250 Hz y 34 cm; 50 ms → 17 m; modo de 50 Hz a 3,4 m; +26 − (−94) = 120.
Remisión «temas 5 y 13» para alineación y *headroom*: correcta (el 5 trata R 68 y *headroom*).

## Hallazgos y correcciones aplicadas

1. **Error 8/9 (dato de publicación).** Trazabilidad decía «BOE núm. 21, de 24/01/2010»; la
   fuente da núm. 18, de 21/01/2010. Corregido.
2. **Error 3/9 (cuenta que no cuadra).** Ejemplo 2 de la aritmética: «Quien divida 80 entre 74…
   acaba en una respuesta falsa (4, 6 u 8 veces)»: 80/74 ≈ 1,08 no da ninguna de esas cifras, y
   el «8» no salía de ninguna cuenta (resto de las opciones del examen RTVE). Queda: «Quien tome los
   6 dB como "seis veces" o quien use la fórmula de potencia (que da unas 4 veces) acaba en una
   respuesta falsa.»
3. **Error 6 (salvedad omitida).** DPA da el 4,5:1 «in theory» para micrófonos en línea
   equidistante y añade que con direccionales «a distance factor of 3 is normally ok even though
   there are two neighboring microphones». Añadido a la celda de la tabla de remedios.
4. **Error 9 (menor).** «Dentro de un recinto la caída deja de cumplirse lejos de la fuente» no
   tenía fuente ni figuraba como oficio; se añade a la lista de oficio de «Trazabilidad».

Pasajes cambiados releídos: sin «ese artículo»/«dicha» colgantes.

## Lentes

`negritas.py` (RD vigente, las dos páginas DPA, Rane, RTW y el tema 6 de Cámara): 32 negritas, 0
fuera de fuente. `refutar_exactitud.py` y `refutar_modo.py` (RD): 0 hallazgos. `refutar_prosa.py`:
0. `indice.py`: índice al día (7.158 palabras, 39 epígrafes); avisa «sin portada» porque el tema no
tiene fila en `herramientas/portadas.tsv` (no lo he tocado).

## Fuera de mi tema (no tocado)

`28-.../02-electricidad-y-electronica-aplicada-al-audio.md`, línea 718, repite «BOE núm. 21, de
24/01/2010» para el RD 2032/2009: debe ser núm. 18, de 21/01/2010.

## Otros ficheros tocados

Sólo el tema y este informe.
