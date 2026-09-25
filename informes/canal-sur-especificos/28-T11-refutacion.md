# Puesto 28 · Operador/a de Sonido · Tema 11 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/11-lineas-y-conexiones.md` (1.035 líneas, unas
11.000 palabras). Fecha de lectura de las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). No se
corrige el tema. Otros ficheros tocados: ninguno salvo este informe y `28-T11-preguntas.md`.

Exactitud: se salta lo «Copiado del común» (1 pasaje, ST 2110-30) y lo «Copiado de RTVE sin cambios» (13
bloques), según `28-T11-redaccion.md`. Cobertura: tema entero.

## Lente 1 · Exactitud (contra la fuente)

Releído hoy en su volcado: ST 2110-30:2025 (6.1, cláusula 7, tablas 2 y 3, nota SDI, SGRP); SMPTE 272M
(alcance, opción asíncrona 32-48 kHz, cuatro canales en compuesto); ST 299-1 (opción 32-48 kHz síncrona o
asíncrona); EBU Tech 3250 (2.2 modos, 2.3 bifase en los intervalos 4 a 31, 6.1-6.3: V.11, 2-7 Vpp, Vmin
200 mV, 7 V de modo común, ecualización y 100 m); Audinate DC 4.18 (glosario de flujos, unicast y
multicast, latencia, PTPv1/v2, gigabit, EEE); RME MADI Converter (7.1 «MADI Basics», alcance coaxial,
niveles, fibra); RME ADI-648 (TOSLINK, Alesis, 10 m, DS); DiGiCo TN294 (páginas 1-3 enteras: revisiones
2003/2008, RG59U, 0,25 V, dos puertos a 96 kHz, 1A/1B, S-MUX y Hi-Speed con el mismo caudal y distinto
orden). Todo lo cotejado coincide.

### Graves

Ninguno.

### Menores

| # | Error | Dónde | Qué dice el tema | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|
| 1 | 9 | «Qué es el MADI», tabla de modos (fila «56 canales», l. 621) y «Resumen de formatos» (l. 178, «56 o 64 a 48 kHz») | El modo original de 56 canales es a **48 kHz** con margen de ±12,5 % | RME (7.1) sólo dice que **«the sample rate can still even vary by +/-12.5%»**, sin frecuencia base; los 48 kHz (+ 1 %) los da para el modo de 64 | En la fila de 56: «frecuencia variable, ±12,5 % (RME)» o «hasta 48 kHz ±12,5 %» sólo si se atribuye como inferencia; en el resumen, «56 o 64 canales (64 hasta 48 kHz + 1 %)» |
| 2 | 6 | «Resumen de formatos», fila SDI (l. 180) | «Hasta 16 (SD y HD a 1,5 Gb/s)» | 272M: **«four channels maximum for composite digital»**, salvedad que el tema sí da en la tabla de normas (l. 802) | Añadir «(4 en SD compuesto)» a la fila del resumen |
| 3 | 5 | «Conversiones y compatibilidad» (l. 938) y «Un supuesto práctico» (l. 961) | dBu, dBFS y «mezcla N-1» sin presentar | — (forma del encargo: siglas de entrada) | Presentar dBu y dBFS en el párrafo de siglas (la tabla es copia RTVE, sólo se añade la sigla arriba) y glosar N-1 («mezcla sin la propia voz del destinatario», remitida al tema 8) |

Observación sin cambio: la tabla de niveles de la ST 2110-30 es la de **emisores** (tabla 2) y así se
rotula; la de receptores (tabla 3) es distinta (el receptor de nivel C debe admitir 1 a 64 canales, no 9 a
64). El tema no la da; no es error, pero un test podría preguntar «un receptor de nivel C». Opcional: una
frase que lo advierta.

## Lente 2 · Cobertura del enunciado

Las diez materias del enunciado (líneas y conexiones, XLR, jack, BNC, Dante/AES67, MADI, AES/EBU, ADAT, SDI,
embebido y desembebido) tienen rúbrica propia en el orden del enunciado. 15 preguntas en
`28-T11-preguntas.md`: 13 enteras, 1 a medias, 1 no.

### Lagunas

| # | Rúbrica | Qué falta | Por qué se pregunta | Fuente para ampliar |
|---|---|---|---|---|
| 1 | Jack | Qué contacto lleva cada canal en un TRS **desbalanceado estéreo** (auriculares: punta izquierdo, anillo derecho) y en uno de **inserción** (envío/retorno); y el jack de 3,5 mm | Es lo que el tema mismo anuncia («el mismo conector de tres contactos se usa también para señales que no lo son: auriculares estéreo, inserciones») y es pregunta típica de test; hoy la P5 no se contesta | Buscar documentación de fabricante (Rane, Neutrik, Shure). En el volcado local, `fuentes/canal-sur/sonido/shure-selection.txt` l. 4754 sólo confirma el **«1/8" stereo (tip-ring-sleeve) external microphone jack»** de las videocámaras (no da qué canal va en cada contacto). Si no se confirma el reparto, se amplía «Lo que este tema no da» |

A medias, sin ampliar aquí: P6 (cifra de la pérdida de nivel con un TS en una salida balanceada) remite
correctamente al tema 2; se deja.

## Lentes automáticas

El tema no cita normas legales: `negritas.py`, `refutar_exactitud.py` y `refutar_modo.py` no tocan. Las
negritas contra normas técnicas ya las cotejó por script la verificación; este informe ha repasado a mano
las de contexto dudoso (arriba).

## Resumen

Graves: 0. Menores: 3. Lagunas: 1 (jack estéreo/inserción). Para el remate: tres retoques de texto y una
ampliación corta del epígrafe «El jack TRS y el TS» (o su declaración en «no da» si la fuente no aparece).
