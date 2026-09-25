# Puesto 28 · Operador/a de Sonido · Tema 9 · Fase 4, refutación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/09-grabacion-edicion-y-postproduccion.md`
(1.021 líneas). Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). No corrijo: el
remate aplica. Ficheros tocados: este informe y `28-T09-preguntas.md`.

## Alcance

- Exactitud: todo lo nuevo y lo adaptado. Salto lo listado en `28-T09-redaccion.md` como «Copiado
  del común» (3 pasajes) y «Copiado de RTVE sin cambios» (14 pasajes).
- Cobertura: el tema entero contra el enunciado (punto 9 del anexo V, puesto 2.28).

## Fuentes releídas (todas el 25-09-2026)

| Fuente | Qué se cotejó |
|---|---|
| EBU R 128 s1 V3 (agosto 2020), PDF descargado de tech.ebu.ch | Motivo, puntos a)-g), nota 1, definiciones, LRA, ficha de revisiones |
| EBU Tech 3343-2023 (`fuentes/normas-tecnicas/`) | §§ 2.4, 3.1, 3.2, recuadros de las pp. 10-11 |
| EBU Tech 3285 v2.0 (`fuentes/archivos/`) | Resumen, § 1, estructura «bext», campos, § 2.4, CodingHistory |
| AES TD1008.1.21-9 (PDF de aes.org) | Tabla 1 y nota 7, «Speech vs. Music», archivo a −24 LUFS |
| iZotope RX 11, página «Spectral De-noise» | Las nueve citas y los nombres de los módulos |
| J. O. Smith, CCRMA, «Sampling Theorem» | Enunciado del teorema y *aliasing* |
| Temas 1, 4, 5, 6, 7, 8, 13, 14 y 15 del puesto | Cada remisión del tema 9 |

Cálculos rehechos: tamaños (tabla, 30 min + cuatro mono = 1.555,2 MB, cuña 8.640.000 B, megabyte
binario 10,09), latencias a 44,1 y 48 kHz, cuña que no pasa (−25,6; 2,5 y 2,3 LU), deriva
(0,36 s, 9 cuadros), resta de códigos (00:36:36:02), 13.440 muestras = 7 cuadros, 960/1.920/2.000/
1.600, 1.728.000.000, −2300, primera corrección de sonoridad. Todos cuadran salvo el hallazgo 1.

## Hallazgos de exactitud

### Grave

**1. Error 3 (recuento). «La sonoridad del programa terminado», párrafo tras la tabla.**
El tema: «el limitador tiene que rebajar los picos al menos 0,5 dB (de −1,8 a −2,3 dBTP), para que
tras subir 1,5 dB no pasen de −1,0 dBTP (con 0,8 dB de reducción quedan en −1,1, con algo de
margen)». Cuenta: −2,3 + 1,5 = **−0,8 dBTP**, que supera −1 dBTP. El mínimo es **0,7 dB** (de −1,8 a
−2,5 dBTP; −2,5 + 1,5 = −1,0). La cifra la introdujo la verificación (su corrección n.º 4, que
cambió «al menos 0,8» por «al menos 0,5»): el 0,8 original no era falso, sino no mínimo. Propuesta:
«al menos 0,7 dB (de −1,8 a −2,5 dBTP), para que tras subir 1,5 dB no pasen de −1,0 dBTP (con 0,8
dB quedan en −1,1, con algo de margen)». Es materia de pregunta práctica (pregunta 14).

### Menores

**2. Error 1 (cita cruzada). «Posición, velocidad y muestra», ejemplo de deriva.** «Por eso, en
doble sistema, además de código común se enclavan los relojes o se vuelve a sincronizar de vez en
cuando (tema 6).» El tema 6 trata el doble sistema, la claqueta y el código común, pero no dice
nada de enclavar relojes ni de resincronizar (grep de «reloj», «deriva», «enclav», «resincron»: sólo
«comparten reloj» en el sistema único). Propuesta: marcarlo «(oficio)» y dejar la remisión sólo
para el doble sistema y la claqueta.

**3. Error 6 (salvedad omitida). «Lo que fija la R 128 s1», fila c).** El tema: «Se puede
normalizar por debajo de −23 **«on purpose…»**». La fuente: «that **in special cases**, the
Programme Loudness Level may be normalised to a Target Level lower than −23.0 LUFS on purpose».
Falta «en casos especiales». Propuesta: «En casos especiales se puede normalizar…».

**4. Error 8 (apartado mal). Trazabilidad, fila de la Tech 3343.** Atribuye «medidores fuera de
línea» a § 3.1 **y** § 3.2. La frase «Typically, offline loudness meters perform both the
measurement as well as the correction» está sólo en § 3.1 (única aparición de *offline* en ese
contexto); § 3.2 da la «simple corrective static gain calculation». Propuesta: quitar «y medidores
fuera de línea» de § 3.2.

**5. Error 9 (matiz). «Los artefactos», segundo punto.** El tema presenta las **«bursts of noise
right after the signal falls below the threshold»** como una de las dos maneras en que «una
limpieza excesiva se oye». En el manual no es efecto de reducir mucho, sino del otro extremo de un
control: con valores altos el proceso se apoya en la puerta de banda ancha, **«which will have
fewer musical noise artifacts, but sound more like broadband gating, resulting in bursts of
noise…»**. Es un compromiso entre dos artefactos. Propuesta: «Y si, para evitarlo, el proceso se
apoya en una puerta de banda ancha, tiene menos ruido musical pero deja…».

Sin más hallazgos. Confirmados literales: las citas de la R 128 s1 (motivo, fin, definiciones,
b, c, d, f, g, LRA, V2 y V3), de la Tech 3343 (§ 2.4, «only by ear», ±0,2 y ±1 LU, ganancia
estática), de la Tech 3285 (resumen, versiones 0/1/2, compatibilidad, campos, TimeReference,
CodingHistory, ×100 de los cinco campos, 256/32 caracteres, MPEG), de la AES TD1008 (nota 7, −18 /
+0,2, 2-3 LU, −24 LUFS) y del manual de iZotope (nueve citas y nueve módulos). Remisiones a los
temas 1, 4, 5, 7, 8, 13, 14 y 15 comprobadas: el contenido está donde se dice.

## Cobertura del enunciado

Las once materias del enunciado (grabación, edición y postproducción; músicas; cuñas; ráfagas;
continuidad; DAW; pistas; sincronía; doblaje; limpieza; mezcla; entrega) tienen su rúbrica, en el
orden del enunciado. Preguntas: 12 enteras, 1 a medias, 2 no (detalle en `28-T09-preguntas.md`).

### Lagunas (se amplía el tema)

**L1. Entrega: reducción de resolución y de frecuencia de muestreo.** El tema no trata el *dither*
al pasar de 24 a 16 bits ni la conversión de frecuencia de muestreo (44,1 ↔ 48 kHz) al exportar,
que son operaciones propias de la entrega y del cambio de destino (máster de emisión, de plataforma,
de disco). Pregunta 15: no. Ampliar con fuente (manual universitario o documentación de fabricante
de una DAW), en «Entrega» o en «De qué está hecho un fichero de audio».

**L2. Pistas: tipos de pista de una DAW.** «Pistas» da las capas, la regla de una fuente por pista y
los buses de submezcla, pero no los tipos de pista de una estación de trabajo (audio, auxiliar o de
retorno, VCA o de control, máster, MIDI/instrumento) ni para qué sirve cada una. Pregunta 9: a
medias. Ampliar breve, con documentación de fabricante (el tema 4 ya usa Pro Tools).

Fuera de lagunas, sin fuente pero declarado: la tabla de términos de continuidad (oficio) y los
80/32 bits del LTC (copiado del común, no se re-verifica).

## Resumen

1 grave (cálculo erróneo introducido en verificación), 4 menores, 2 lagunas.
