# Puesto 28 · Operador/a de Sonido · Tema 8 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/08-sonido-en-television.md`. Fecha de
trabajo y de lectura de las fuentes: 25-09-2026 («hoy» del encargo, 24-09-2026). No se corrige el tema.

## Método

- Exactitud: script que busca cada cita en negrita, normalizada, en EBU Tech 3343-2023, Tech 3347,
  Tech 3326 y los textos de Clear-Com y Soundcraft (`fuentes/`). Todas casan salvo las del Libro de
  estilo y ATEM (copiadas del común, se saltan) y la de Yamaha (PDF no guardado; ya comprobada en la
  verificación). Lectura en contexto de: tolerancias ±0,2/±1,0 LU y nota 2; −1 dBTP; § 2.4
  (procesador, GPIO, *loudness sausage*); +3 dB desde −20 LUFS; § 3.5.1 (−24 LUFS) y § 3.5.2; § 8.1
  (tono, R 68-2000, PML obsoleto, medidor de pico); § 8.2 (73 dBC, 1 dB, 0,5 dB, LFE +10 dB); Tech
  3347 § 3.2.1 (Speex 8/16 kHz); Clear-Com (dúplex, no privada, 30 V, patillas); Soundcraft
  («Pre-fade rather than post-fade auxiliaries must be used»). Todo confirmado.
- Se saltan, según `28-T08-redaccion.md`, los cinco bloques «Copiado del común» y los doce pasajes
  «Copiado de RTVE sin cambios». La cobertura mira el tema entero.
- Búsqueda de normas en `fuentes/` sobre el nivel sonoro de la emisión.

## Hallazgos

| # | Gravedad | Lugar | Error | Fuente | Propuesta |
|---|---|---|---|---|---|
| 1 | Grave (9 afirmación sin fuente, falsa; y laguna) | «Recomendaciones técnicas que el tema cita», último párrafo: «Ninguna norma legal (ley o reglamento) regula el sonido en televisión ni la intercomunicación de producción»; ficha, «Fuente: Sin norma jurídica» | Una ley sí regula el nivel sonoro de lo que se emite | Ley 13/2022, General de Comunicación Audiovisual, art. 121.4: **«El nivel sonoro de las comunicaciones comerciales audiovisuales no puede ser superior al nivel medio del programa que le precede.»** (`fuentes/canal-sur/BOE-A-2022-11311.md`, l. 1621; releer en el BOE vigente antes de aplicar) | Añadir en «Mezcla para emisión» (p. ej. tras «Lo que la EBU R 128 pide al programa») la cita literal del art. 121.4 con su aplicación práctica (la publicidad no puede sonar más fuerte que el programa anterior; la sonoridad normalizada es la forma de cumplirlo, oficio); corregir la frase final a «Salvo ese precepto, ninguna ley…» y la ficha; añadir la norma a «Normativa que el tema invoca» y a Trazabilidad, y la pregunta al «Qué se puede preguntar». Es Ley 13/2022, del temario común: si el común ya cita el artículo, tomar su texto literal |
| 2 | Menor (matiz) | Supuesto práctico, punto 6: «el pico por debajo de −1 dBTP» | La verificación corrigió en la tabla de la salida a «no superar −1 dBTP» (la fuente: «shall not exceed»), pero el supuesto conserva «por debajo de» | Tech 3343, l. 615 y 646 | «el pico verdadero sin superar −1 dBTP» |
| 3 | Menor (forma) | «Cuatro hilos y el híbrido»: `most commonly used [...]».**` | La negrita se cierra tras el punto, fuera de la comilla, a diferencia del resto de citas | — | Cerrar la negrita tras «»» y dejar el punto fuera |

Nada más: el resto de cifras, secciones y condiciones (SHALL/RECOMMENDED, should/shall) casa con la fuente.

## Cobertura del enunciado

Las seis rúbricas (intercom, IFB, retornos, mezcla para emisión, coordinación con realización,
cámaras) están, en su orden y con aplicación práctica. Laguna: la del hallazgo 1 (la norma legal del
nivel sonoro en emisión). Variante a medias: el −2 dBTP para distribución con reducción de datos
(AC-3, MPEG-1 L2) no está en el tema 8, pero sí en el tema 13, al que remite; no se pide ampliar.

## Preguntas

`28-T08-preguntas.md`: 15 preguntas; 14 enteras (una con variante a medias) y 1 no (la 13, art. 121.4
de la Ley 13/2022).

## Ficheros tocados

Sólo `28-T08-preguntas.md` y este informe. El tema no se ha modificado.
