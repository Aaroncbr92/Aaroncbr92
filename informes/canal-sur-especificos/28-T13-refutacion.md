# Puesto 28 · Operador/a de Sonido · Tema 13 · Fase 4, refutación

Tema refutado: `temas/canal-sur-especificos/28-operador-a-de-sonido/13-medicion-y-sonoridad.md`
(no se ha corregido). Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).
Ficheros tocados: este informe y `28-T13-preguntas.md`.

## Fuentes releídas (todas el 25-09-2026)

Textos de la sesión (scratchpad) y `fuentes/normas-tecnicas/`: EBU R 128-2023 (V5), UIT-R
BS.1770-5 (11/2023), EBU Tech 3341-2023, Tech 3342-2023, Tech 3343-2023, Tech 3205-E (1979),
EBU R 68-2000, RTW «Focus: The Multi Correlator» y Sound On Sound (Robjohns, mayo de 2024).

Método: script que busca cada cita «…» en negrita en el texto normalizado de las fuentes; las no
encontradas se leyeron a mano. Todas resultaron literales salvo las diferencias de composición ya
aceptadas en la verificación («·», «;», llamadas de nota, «×» perdido en el volcado). Datos en
redonda y cálculos, uno a uno. Se saltan los pasajes de «Copiado del común» y «Copiado de RTVE sin
cambios» (`28-T13-redaccion.md`).

## Lente 1 · Exactitud

### Graves

1. [9] «Fase y sonoridad: el tono en los dos canales», primer párrafo: «La fase también cambia lo
   que marca el medidor de sonoridad, porque éste suma la energía de los canales.» No lo dice
   ninguna fuente, y lo contradice el algoritmo que el propio tema cita: la BS.1770 hace el
   **«mean square calculation for each channel»** *antes* de la **«channel-weighted summation»**.
   Con la energía de cada canal calculada por separado, la polaridad o fase *entre* canales no
   cambia la lectura (un tono en contrafase en L y R marca lo mismo que en fase). Lo que sí cambia
   la lectura es el número de canales con tono, que es lo único que compara la tabla que sigue. El
   «(in phase)» de la Tech 3343 es una condición del procedimiento, no una prueba de que la fase
   altere la medida. Riesgo en test: lleva a contestar mal la pregunta 13. Propuesta: sustituir
   la frase por otra que diga que la lectura depende de cuántos canales llevan el tono, porque la
   BS.1770 calcula la energía de cada canal y después la suma (cálculo sobre las etapas citadas),
   y que la contrafase no se ve en el medidor de sonoridad sino en el correlador o al sumar a mono.
   Revisar también el título del epígrafe y la remisión de «Aplicación práctica» si se cambia.

### Menores

2. [6] «Los medidores clásicos», PPM: la marca «Test» está **«9 dB below the maximum amplitude»**
   *of programme signals transmitted on international sound-programme circuits permitted according
   to C.C.I.T.T. Recommendations* (Tech 3205-E). El tema corta la salvedad: parece el máximo del
   medidor, y es el máximo permitido en circuitos internacionales. Completar en redonda.
3. [6] Tabla de medidores: «Tiempo de integración de 10 ms; cae de +12 a −12 en 2,8 s» no dice
   «en modo normal» (la 3205-E da 3,8 ± 0,5 s en modo lento). El párrafo siguiente sí lo dice;
   basta añadirlo en la celda.
4. [8] «El peso de cada canal»: «La tabla 3 de la BS.1770 da los coeficientes» y la tabla incluye
   la fila «LFE · Excluido de la suma». La tabla 3 sólo tiene L, R, C, Ls y Rs; la exclusión del
   LFE está en la descripción de las etapas del anexo 1. Precisar la procedencia de esa fila.

Comprobado sin hallazgo: considerandos y puntos h)–p) de la R 128, notas 1 y 2 (incluido «too few
data points»), historial V1–V5, documentos s1–s4, Tech 3344 y 3401; alcance de la BS.1770 (anexos 1,
3 y 4), etapas, ponderación K y RLB, pesos, −3,01 LKFS y −0,691, 12,04 dB, 4× y 2×, dB TP; Tech
3341 (ventanas, 10 Hz de la S, máximos, puerta, escalas «may simply be numerical», escala por
defecto, relativa y absoluta, unidades); Tech 3342 (−70 / −20 LU, percentiles, fade-out); Tech 3343
(−27/−31, descartar metadatos, envolventes, LFE); Tech 3205-E (10 ± 2 ms, +9 → +7, 2,8 ± 0,3 s,
divisiones de 2 dB, tipos I, IIa, IIb, nota de sustitución); RTW (cuatro citas); SOS (300 ms de
subida y bajada, graves y sostenidos, +4 dBm = 0 VU con atenuador a 0, 1940 y «remains in use
today»). Cálculos: −24/−22, −23,2/−22,8, ±23 LU↔LUFS, +5 LU, −21,01 LUFS, 10 % y 5 % del LRA,
ejemplos de corrección (−23 LUFS/−6 dBTP; +1 dBTP que obliga a limitar). Correctos.

## Lente 2 · Cobertura del enunciado

«Medición y sonoridad: LUFS, EBU R128, picos, loudness, fases y control de calidad»: las seis
rúbricas están, en su orden, con epígrafes propios. Preguntas (`28-T13-preguntas.md`): 11 enteras,
1 a medias, 3 no.

### Lagunas (se amplía el tema)

1. Goniómetro / vectorscopio de audio (pregunta 14, no): el enunciado pide «fases» y el tema sólo
   nombra el goniómetro «sin fuente leída». Es la otra herramienta estándar de fase junto al
   correlador; buscar fuente de fabricante (RTW o similar) para su lectura básica (mono = línea
   vertical, contrafase = horizontal, anchura estéreo) o, si no se encuentra, mantener el hueco.
2. Requisitos de actualización y manejo del medidor (pregunta 11, no): la Tech 3341 § 2.2 exige
   actualizar la integrada **«at least 1 Hz»** en medidores en directo, y las funciones mínimas de
   **«start/pause/continue»** de la integrada y el LRA; el tema sólo da los 10 Hz de la S. Añadir
   una línea.
3. Dialnorm (pregunta 15, a medias): el tema usa «dialnorm» en una cita sin explicar qué es;
   añadir, con fuente (Tech 3343 o documentación Dolby), qué indica ese metadato.
