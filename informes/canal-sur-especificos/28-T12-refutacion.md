# Operador/a de Sonido (28) · Tema 12 · Refutación

Fase 4 (sólo señala; no corrige). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/12-radiofrecuencia-aplicada-a-microfonia-inalambrica.md`.
Leídos del método sólo `ENCARGO.md` y el enunciado del puesto. Fecha de lectura de las fuentes:
**25-09-2026** (el encargo fija el día de trabajo en el 24-09-2026).

Fuentes releídas: Orden TDF/732/2026 (BOE-A-2026-15661): DA 2.ª, derogatoria, DF 2.ª, notas UN-17,
36, 48, 49, 81, 95, 105, 118, 119, 127, 151 y 153, y rótulos del cuadro; Shure, *Wireless Systems
Guide for Antenna Setup* y *Selection and Operation of Wireless Microphone Systems* (volcados unidos
en una línea). Se saltan, según `28-T12-redaccion.md`, lo «Copiado del común» (tabla Banda/Grupo/Canal
y sus dos párrafos) y lo «Copiado de RTVE sin cambios» (cinco pasajes) en exactitud, no en cobertura.

## Lentes

- `negritas.py` (BOE + dos guías Shure): 165 negritas, 10 «no están», las mismas 10 ya explicadas en
  verificación (rótulos, listas de canales partidas en tabla, fórmulas IM, cita DPA del tema 3, cita
  de 250 kHz partida por página). Sin novedades.
- Recalculados a mano: tabla de longitudes de onda, cuarto de onda en TDT (16-11 cm), 10 cm ≈ 750 MHz,
  ejemplo de cable (7,5 dB), ejemplo de tres emisores de Shure (208/192/182) y el caso 606,0 / 606,8 /
  607,2 MHz (todos los productos y la distancia mínima de 0,4 MHz). Correctos.
- Cotejados contra la fuente los pasajes sin negrita que resumen a Shure: tablas de averías (una y
  varias unidades, incluida la fila del emisor que activa dos receptores), operación (*Show
  Operation*), comprobación previa, diversidad (ruido de conmutación, alcance), ejemplos de ganancia
  neta (–1 a +4 dB), amplificador «placed at the antenna», bastidor de equipos digitales. Correctos.

## Hallazgos de exactitud

**Graves: 0.**

**Menores: 2.**

1. (Error 6, salvedad omitida) «El receptor por dentro», silenciador de tono: el tema dice que
   **«evita el ruido aun con otra señal en la misma frecuencia»**. Shure: **«even in the presence of a
   (non-tone-key) interfering signal at the same frequency»**. Falta «sin tono»: con otro emisor que
   también manda tono la protección no está garantizada. Pregunta 13, a medias. Propuesta: «aun con
   otra señal sin tono en la misma frecuencia».
2. (Error 5, siglas sin presentar) En «Lo que este tema no da»: **WMAS**, **DAB+** y **RDS** no se
   presentan en las siglas de entrada (DAB sí). Propuesta: presentarlas o quitarlas (son remisiones).

Nada más: notas del CNAF (bandas, canales, potencias, canalizaciones, uso común, secundario, título
habilitante, cese inmediato, 700 MHz, PPDR), DA 2.ª, derogatoria y entrada en vigor, y todas las
citas de Shure en su contexto, conformes. Las discrepancias internas del CNAF (UN-48/UN-119;
UN-151/rótulo) y el ejemplo de 200 MHz de Shure están bien declarados.

## Cobertura del enunciado

«Radiofrecuencia aplicada a microfonía inalámbrica: antenas, coordinación de frecuencias e
interferencias»: las cuatro partes tienen rúbrica propia, en el orden del enunciado, con teoría,
norma y casos prácticos. Preguntas: **11 enteras, 2 a medias, 2 no** (`28-T12-preguntas.md`).

**Lagunas: 3** (se amplía el tema, poco en cada caso):

1. (Pregunta 4, no) **Otros usos de audio de uso común en bandas vecinas de los micrófonos.** La
   UN-17 permite, de uso común, **«micro-transmisores de uso portátil para aplicaciones de audio sin
   hilos y muy corto alcance, con potencia radiada aparente máxima de 50 nW (50 nanovatios)»** en
   87,5-108 MHz (norma ETSI EN 301 357-2). Y la UN-105 dispone en 174 MHz canales de 50 kHz de uso
   común para **«dispositivos de ayudas auditivas y a discapacitados»** (2 mW p.r.a.), entre ellos
   174,100 y 174,300 MHz, las mismas frecuencias que los canales 1 y 2 de micrófonos de la UN-95:
   dato de coordinación. Propuesta: una frase en la tabla de notas o tras ella.
2. (Pregunta 11, a medias) **Margen respecto de la frecuencia imagen.** Shure: **«it is recommended
   that operating frequencies be chosen to be at least 250 KHz from any image frequency»**, y antes,
   **«In most cases, the front end of the receiver should be able to reject an image frequency unless
   it is extremely strong»**. El tema sólo da el margen respecto del oscilador local. Propuesta:
   añadirlo en la fila «Frecuencia imagen» o en el párrafo siguiente.
3. (Pregunta 12, no) **Espurias del emisor de cristal**, la tercera «frecuencia interna» de Shure
   (**«The last internal frequency issue concerns the VCO in crystal controlled transmitters»**): el
   multiplicador deja espurias a múltiplos de la frecuencia del cristal (ejemplo de Shure: ×9, 180 MHz,
   cristal de 20 MHz, espurias en 160 y 200 MHz). El tema dice «armónicos» en el diagnóstico sin
   explicarlo. Propuesta: una fila más en la tabla de «Las frecuencias internas del receptor» (rótulo
   a ajustar: del receptor y del emisor), citando el pasaje leído en el remate.

## Ficheros tocados

- Creados `28-T12-preguntas.md` y este informe. El tema no se ha tocado.
- Scratchpad: volcados de Shure en una línea (`t12r/`).
