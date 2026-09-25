# Puesto 28 · Operador/a de Sonido · Tema 13 · Fase 2, redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema escrito:
`temas/canal-sur-especificos/28-operador-a-de-sonido/13-medicion-y-sonoridad.md` (7.724 palabras
según `indice.py`, contando ficha, siglas y trazabilidad; 6 rúbricas en el orden del enunciado
—LUFS, EBU R 128, picos, *loudness*, fases, control de calidad—, 21 epígrafes `###`).
`refutar_prosa.py`: 0 hallazgos (tras presentar «dB FS» y «dB TP» en las siglas).

Material usado: `informes/canal-sur-especificos/28-investigacion-A-fundamentos.md` (§ 13.1-13.7 y
huecos declarados); RTVE `temas/sonido/14-medicion-y-sonoridad.md`; tema cerrado de Canal Sur
`08-camara-operador/06-captacion-de-sonido.md` (`08-T06-final.md`).

No se ha releído ninguna fuente primaria en esta fase: las citas nuevas salen del informe de
investigación (fuentes leídas allí el 25-09-2026) o del tema cerrado de Cámara. El tema no cita
ninguna norma legal; cita recomendaciones técnicas (UER, UIT), fabricante (RTW) y prensa técnica
(Sound On Sound).

Ficheros tocados: sólo el tema 13 y este informe.

## Reparto real del material

La fila de reuso daba el RTVE 14 al 90 % («casa entero»). En la práctica, lo copiado literal del
RTVE es poco (unas 450 palabras): el RTVE 14 tiene 2.100 palabras, de las que casi la mitad comenta
las seis preguntas de su examen (quitado), y su epígrafe de trazabilidad declara no haber leído la
R 128 (sustituido: ahora está leída). El enunciado de Canal Sur pide además «fases» y «control de
calidad», que el RTVE no trataba. El grueso nuevo sale de la investigación (BS.1770-5, Tech 3341,
3342, 3343, 3205-E, RTW, Sound On Sound).

## Qué se quitó del RTVE por propio de RTVE, sin fuente o corregido

- Todas las referencias a las preguntas 24, 26, 37, 39, 69 y 95 del examen RTVE, las «respuestas
  oficiales», las marcas ✔, los distractores y el epígrafe «Los datos que el examen ha preguntado»;
  el aviso «seis preguntas por cuatro datos».
- El apunte sobre el anexo de RTVE que llama «norma AES R-128» a la recomendación: se conserva sólo
  como aclaración general («no de la AES, aunque a veces se la cite así»); el enunciado de Canal Sur
  dice «EBU R128», correcto.
- La pregunta 95 del RTVE daba la tolerancia en directo como «±1 dB»; el tema usa ±1,0 LU, que es
  lo que dice la R 128 h) (1 LU = 1 dB según Tech 3341, así que no hay contradicción de valor).
- Trazabilidad RTVE («El texto de la recomendación EBU R 128 no se ha volcado», las cuatro
  declaraciones): sustituida; todas las cifras quedan ahora con fuente primaria.
- «realzando medios y agudos y quitando peso a los graves más profundos» (curva K): sustituido por
  la descripción de la BS.1770 (estantería que modela la cabeza + paso alto RLB); «medios» no consta.
- Tabla de medidores del RTVE § 5: rehecha con fuente por fila (Tech 3205-E para el PPM, Sound On
  Sound para los 300 ms del vúmetro, BS.1770 para el pico verdadero).
- «La recomendación admite ese margen porque exigir exactitud sería exigir lo imposible»
  (interpretación sin apoyo): quitado.
- «Ésa es la razón de que la publicidad se comprimiera hasta el absurdo antes de la R 128»
  (historia sin fuente): quitado.
- Remisiones internas del RTVE («tema 2», «tema 7», «punto 5»): sustituidas por las de este temario.

Aplicado de las «Correcciones al material RTVE» de la investigación: ±0,2 LU de medida, −70 LUFS y
−10 LU de la integrada, −20 LU del LRA, escalas EBU +9/+18, M y S sin puerta, ±0,5 LU no vigente,
−1 dBTP «during production (linear audio)», PML −9 dBFS obsoleto, Tech 3205 sustituida.

No usado de la investigación, por no poder asegurar su contexto: la infralectura de «3 dB … at a
quarter of the sampling frequency» de la BS.1770 (el volcado no dice a qué medidor se refiere).

## Copiado del común

Pasajes literales del tema 6 del específico de Cámara Operador
(`08-camara-operador/06-captacion-de-sonido.md`, cerrado: `08-T06-final.md`). No se re-verifican.
Comprobado por script: cada uno es copia exacta (salvo saltos de línea).

Epígrafes o párrafos enteros:
1. «Por qué la sonoridad y no el pico», primer párrafo («Durante décadas los programas se ajustaron
   por su pico… does not reflect the loudness of an audio signal»»), del epígrafe de Cámara «La
   sonoridad: EBU R 128».
2. «Lo que fija la R 128»: la frase «Lo que fija la R 128 (versión 5, noviembre de 2023):» y la tabla
   de cinco filas h), i), m), k), n).
3. «La tolerancia del directo»: el último párrafo («Para un tribunal, el dato que más se pregunta…
   y manda el articulado.»).
4. «Pico de muestra y pico verdadero»: el primer párrafo («En digital, el máximo absoluto es 0
   dBFS… por debajo de ese techo.»), del epígrafe de Cámara «El nivel de alineación: −18 dBFS».
5. «La alineación: −18 dBFS y el fin del −9 dBFS»: los párrafos «La EBU R 68 recomienda…
   (−18 dBFS).»» y «El nivel máximo permitido de −9 dBFS ha cambiado… at a level of −18 dBFS.»».

Fragmentos (citas de fuente con su frase de Cámara, dentro de párrafos propios):
6. «Pico de muestra y pico verdadero»: la cita de la Tech 3343 «It is only necessary to leave a
   headroom of 1 dB… basic sample rate: 48 kHz)».
7. «Por qué −1 dBTP y no 0»: «para dos sistemas de reducción de datos muy usados en Europa, MPEG-1
   Layer 2 y Dolby AC-3, el límite recomendado es −2 dBTP.»
8. «Los medidores clásicos»: la cita de la R 68 «due to the characteristics of quasi-peak programme
   meters… greater than those indicated».
9. «La alineación»: la cita «The EBU therefore recommends using a peakmeter for alignment.».
10. «La tolerancia del directo»: la cita «(for example, at −24 LUFS), so that unexpected crowd noise
    has more room to move» (§ 3.5.1).
11. «Fase y sonoridad: el tono en los dos canales»: la cita de la Tech 3343 § 8.1 «The alignment
    level of −18 dBFS (1 kHz tone) will read as −18 LUFS… stereo or surround sound signal.».

Las frases que presentan estos fragmentos son propias y sí se verifican.

## Copiado de RTVE sin cambios

Pasajes técnicos copiados sin tocar una palabra de `temas/sonido/14-medicion-y-sonoridad.md`
(marcado «actualizar: no»); **sólo se ha quitado la negrita** (en el RTVE era énfasis y aquí negrita
= literal de fuente) y la marca ✔. Ninguno cita norma. Comprobado por script: cada párrafo o fila,
sin `**` ni ✔, es subcadena del RTVE.

1. «Por qué la sonoridad y no el pico»: el párrafo «La razón es que un medidor de picos… pegado al
   techo.» y la tabla Pico/Sonoridad (cabecera y dos filas) (RTVE § 1).
2. «La ponderación K» (dentro de «Cómo se mide»): la frase «Por eso un bombo enorme sube menos los
   LUFS de lo que sube el picómetro.» (RTVE § 3).
3. «LUFS, LKFS y LU»: la frase «Y las dos unidades que hay que separar, porque se confunden todo el
   rato:» y la tabla LUFS/LU (cabecera y dos filas) (RTVE § 3).
4. «LUFS, LKFS y LU»: «Un LU y un decibelio valen lo mismo: son la misma escala logarítmica. La
   diferencia no es de tamaño, es de si el número apunta a un absoluto o a una diferencia.» (RTVE
   § 3; la frase siguiente, con sus citas, es propia).
5. «Por qué −1 dBTP y no 0»: el primer párrafo, «Por qué no cero, que es lo que parecería lógico…
   El decibelio de margen es lo que lo evita.» (RTVE § 2).
6. «La puerta de la sonoridad integrada»: el párrafo «Qué es la puerta y por qué existe… de verdad
   suena.» y la tabla Escala/¿Puerteada?/Por qué (cabecera y tres filas) (RTVE § 4).

Adaptados del RTVE (cambian palabras, mayúsculas o citan la R 128: sí se verifican): la frase
«Lo que hace de la sonoridad una medida distinta del nivel es que va ponderada»; «Un programa
grabado se puede medir entero y ajustar. Un directo no…» (mayúscula inicial); «El vúmetro no
protege contra el recorte…» (mayúscula y final cambiado); la tabla M/S/I y su uso; los tres puntos
de «Sonoridad y compresión».

## Preguntas de autocomprobación

Diez preguntas tipo test que un tribunal haría sobre el enunciado, repartidas por sus seis rúbricas
(T = teoría; P = aplicación práctica). Contestadas sólo con el tema.

1. (LUFS, T) La unidad LKFS de la UIT-R BS.1770 respecto a la LUFS de la UER es: a) 3 dB mayor;
   b) equivalente; c) relativa; d) ponderada en A. → **b**. Entera: «LUFS, LKFS y LU» (nota 1 de la
   R 128).
2. (LUFS, T) En la suma de canales de la BS.1770, los envolventes pesan y el LFE: a) 1,0 y se
   incluye; b) 1,41 (≈ +1,5 dB) y se excluye; c) 0,71 y se excluye; d) 1,41 y pesa 10 dB. → **b**.
   Entera: «Cómo se mide», tabla de pesos y Tech 3343 § 4.2.
3. (R 128, T) Nivel objetivo y tolerancia de un directo según la EBU R 128 vigente: a) −24 LUFS
   ±2 LU; b) −23 LUFS ±0,5 LU; c) −23 LUFS ±1,0 LU; d) −18 LUFS ±1 LU. → **c**. Entera: «Lo que fija
   la R 128» y «La tolerancia del directo» (con el aviso de que ±0,5 LU no está en el articulado de
   2023).
4. (R 128 y picos, P) Un programa se va a distribuir codificado en Dolby AC-3. ¿Qué techo de pico
   verdadero recomienda la Tech 3343? a) 0 dBFS; b) −1 dBTP; c) −2 dBTP; d) −9 dBFS. → **c**.
   Entera: «Por qué −1 dBTP y no 0» (−1 dBTP es en producción, audio lineal).
5. (Picos, T) Para medir el pico verdadero de una señal a 48 kHz, la BS.1770 sobremuestrea: a) 2×,
   a 96 kHz; b) 4×, a 192 kHz; c) 8×, a 384 kHz; d) no sobremuestrea. → **b**. Entera: «Pico de
   muestra y pico verdadero» (y 2× basta a 96 kHz).
6. (Picos, T) El PPM de la UER (Tech 3205-E) es un medidor: a) de pico verdadero; b) de cuasipico
   con 10 ms de integración; c) de promedio de 300 ms; d) de sonoridad. → **b**. Entera: «Los
   medidores clásicos: vúmetro y PPM».
7. (Loudness, T) En un medidor en «modo EBU», la lectura a corto plazo (S): a) usa 400 ms y puerta
   a −70 LUFS; b) usa 3 s y no tiene puerta; c) usa 3 s y puerta relativa de −10 LU; d) integra todo
   el programa. → **b**. Entera: «Las tres lecturas» y «La puerta de la sonoridad integrada».
8. (Loudness y fases, P) Un tono de 1 kHz a −18 dBFS, en fase en los canales izquierdo y derecho, en
   la escala relativa de un medidor en «modo EBU» marca: a) −18 LU; b) 0 LU; c) +5 LU; d) −5 LU. →
   **c**. Entera: «Fase y sonoridad: el tono en los dos canales» (y «Las escalas del medidor»:
   −23 LUFS = 0 LU).
9. (Fases, P) Un correlador de fase marca −1 de forma estable con una voz enviada por los dos
   canales. Lo más probable es: a) estéreo amplio correcto; b) canales sin relación; c) un canal con
   la polaridad invertida, que se cancelará en mono; d) un exceso de sonoridad. → **c**. Entera: «La
   correlación de fase», tabla y «Aplicación práctica».
10. (Control de calidad, P) En control de calidad, un programa grabado mide −22,9 LUFS integrados:
    a) no cumple, se pasa 0,1 LU; b) cumple, dentro de la tolerancia de medida de ±0,2 LU; c) sólo
    cumpliría si fuera un directo; d) hay que medir sólo la voz. → **b**. Entera: «Lo que la R 128
    exige al control de calidad» (−23,2 a −22,8 LUFS; se mide el programa entero).

Resultado: las diez se contestan enteras con el tema; no ha hecho falta ampliar. Durante la
redacción se añadieron, para cubrir el enunciado, los epígrafes de fases y de control de calidad
(ausentes en el RTVE) y los ejemplos de cálculo de las tablas de tolerancias y de corrección de nivel.
