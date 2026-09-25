# Puesto 28 · Operador/a de Sonido · Tema 14 · Fase 2, redacción

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema escrito:
`temas/canal-sur-especificos/28-operador-a-de-sonido/14-audio-multicanal-dolby-downmix-y-compatibilidad.md`
(unas 7.700 palabras de cuerpo, 8.500 con ficha y siglas; 7 rúbricas `##` en el orden del enunciado
—audio multicanal, Dolby, 5.1, estéreo, mono, downmix, compatibilidad— y 26 epígrafes `###`).
Índice comprobado por script (anclajes = epígrafes); `refutar_prosa.py`: 0 hallazgos tras
presentar CD, DVD, MPEG, MADI e IP.

Material usado: `informes/canal-sur-especificos/28-investigacion-A-fundamentos.md` (§ 14.1-14.5, §
13.5 LFE y metadatos, § 13.6 alcance de BS.1770-5, § 13.7 RTW); RTVE `temas/sonido/15-audio-multicanal.md`.
No se ha releído ninguna fuente primaria en esta fase: todas las citas salen del informe de
investigación (fuentes leídas allí el 25-09-2026). El tema no cita ninguna norma legal; cita
recomendaciones técnicas (BS.775-4, BS.1770-5, Tech 3343, RDD 19), que sí deben verificarse.

Ficheros tocados: sólo el tema y este informe.

## Reparto real del material

El RTVE 15 tiene 2.050 palabras, de las que casi la mitad comentan las preguntas 10, 54, 81 y 96 de
su examen. Copiado literal: 11 pasajes, unas 290 palabras (≈ 4 % del cuerpo). No el 90 % de la tabla
de reuso: el enunciado de Canal Sur pide además estéreo, mono y compatibilidad, y la investigación
da con fuente la colocación de altavoces, el LFE, los coeficientes, Lo/Ro frente a Lt/Rt, la
sonoridad del downmix, el Dolby E en detalle y el Dolby ED2, que el RTVE no tenía.

## Qué se quitó o corrigió del RTVE

- Todas las referencias a preguntas y respuestas oficiales (10, 54, 81, 96), las ✔, «Cuatro
  preguntas», los distractores y el epígrafe 6 «Los datos que el examen ha preguntado»; la
  trazabilidad basada en «la plantilla oficial».
- § 1: «hasta unos 120 hercios … orden de magnitud» → cifra de norma, BS.775-4 «up to 120 Hz» y
  20-120 Hz. La columna «Dónde» de la tabla de formatos (7.1 «cine y disco», 9.1.6 «salas de
  mezcla inmersiva»), sin fuente: quitada, y la fila 9.1.6 también.
- § 2: «sala de cine con sesenta altavoces», sin fuente: quitado. La cama 7.1.2 deja de descansar
  en la plantilla: ahora es de la guía del Dolby Atmos Renderer v3.0, con 118 objetos y 128
  entradas, y con la salvedad de versión. «Tope» / «tamaño máximo» → «configuración básica» (lo que
  dice la guía).
- § 3: «los envolventes se meten desfasados 180 grados» → Tech 3343: «±90° phase shifting to a
  Mono-sum of the surround channels». Quitado «misma aritmética … del tema 11» (numeración RTVE) y
  «las entregas de emisión suelen pedir las dos» (sin fuente); la fila Lo/Ro «lo envolvente se
  pierde» se reescribe (los envolventes se suman a L y R, no se pierden). Añadida la preferencia
  Lo/Ro de la UER.
- § 4: «El enunciado lo nombra expresamente y el examen no lo pregunta», propio de RTVE.
- § 5: «Es la parte que más se descuida y la que más caro sale» (opinión), «Es el epígrafe 3» y
  «La sonoridad del tema 14» (numeración RTVE). El punto 3 («Es efectos, no graves de todo») y el 5
  se reescriben con BS.775 y Tech 3343; se añaden los puntos 6 y 7.

## Copiado del común

Ninguno. No hay tema cerrado de Canal Sur (común ni específico) que trate audio multicanal,
downmix o Dolby (búsqueda en `temas/canal-sur-comun` y `temas/canal-sur-especificos`). Las remisiones
a los temas 1, 3, 11, 13 y 15 del puesto son remisiones, no copias.

## Copiado de RTVE sin cambios

De `temas/sonido/15-audio-multicanal.md` (marcado «actualizar: no»). Pasajes técnicos copiados sin
tocar una palabra; **sólo se ha quitado la negrita** (en el RTVE era énfasis y aquí negrita =
literal de fuente). Ninguno cita norma. Comprobado por script: cada pasaje, sin `**` y con los
espacios normalizados, es subcadena del RTVE y del tema.

1. «Las seis señales»: «Y los cinco canales del 5.1, que hay que saber nombrar: izquierdo, central,
   derecho, envolvente izquierdo y envolvente derecho, más el LFE.» (§ 1).
2. «Canales frente a objetos»: la tabla entera (cabecera y tres filas: «Qué se manda», «Quién
   decide dónde suena», «Si la sala tiene otro número de altavoces») (§ 2).
3. «Canales frente a objetos»: «No porque se degrade con gracia, sino porque el decodificador
   RECALCULA el reparto con los altavoces que hay.» (§ 2; la frase anterior es nueva).
4. «La cama y los objetos de Dolby Atmos»: «una mezcla basada en objetos no renuncia del todo a los
   canales. Lo que no se mueve —el ambiente, la música, a menudo el diálogo— se pone en una CAMA de
   canales fijos, y sólo lo que tiene que viajar por la sala se hace objeto.» (§ 2; el arranque «La
   cama (*bed*) responde a una idea práctica:» es nuevo).
5. «Qué problema resuelve el Dolby E»: el párrafo «Cuál es el problema: … el 5.1 no cabe.» (§ 4).
6. «Qué problema resuelve el Dolby E»: el párrafo «Qué hace el Dolby E: … sin producir ruido.» (§ 4).
7. «Qué problema resuelve el Dolby E»: el párrafo «Y ésa es su virtud y su límite: … que
   corresponda.» (§ 4).
8. «El LFE no es el subgrave»: «El LFE merece una precisión que casi nadie hace: no es «el altavoz
   de graves».» y «Los graves de los otros cinco canales no van por ahí: … al subgrave.» (§ 1; en el
   RTVE las separaba una frase, que no se copia).
9. «Producir una señal multicanal compatible», punto 1: «Monitorización correcta. No se puede
   mezclar en 5.1 sin cinco altavoces bien colocados y calibrados en nivel.» (§ 5; la frase
   siguiente es nueva).
10. Íd., punto 2: «Decidir qué va al central. En televisión, el diálogo. Un central mal usado
    descoloca todo lo demás.» (§ 5).
11. Íd., punto 4: «Comprobar el downmix. La mayoría del público oirá la mezcla en estéreo o en una
    barra, así que la mezcla tiene que sobrevivir a la reducción.» (§ 5; lo que sigue es nuevo).

Todo lo demás del tema es nuevo o adaptado y pasa por verificación.

## Puntos para el verificador

- «Su rasgo distintivo frente a los formatos envolventes clásicos es el uso de objetos, que se
  sitúan y se mueven en el espacio tridimensional, también por encima del oyente» (Dolby Atmos):
  adaptado del RTVE (respuesta de su examen), sin cita de fuente; declarado como oficio.
- «hasta 3 LU»: la investigación da la frase de la Tech 3343 con «such a Surround-Sound mix», sin el
  caso al que se refiere; el tema lo dice («en el caso que examina») y lo declara en «Lo que no da».
- Coeficientes de la Tech 3343 y perfiles Dolby: el último valor de cada serie se perdió en el
  volcado; el tema da sólo los legibles.
- La Tech 3343 cita BS.775-2; el tema afirma que los coeficientes a estéreo de la −4 son los mismos
  de su tabla 2 (L, R 0 dB; C, LS, RS −3 dB). Comprobar contra la tabla 2 de la −4 (lo está en la
  investigación).
- Colocación del central «al frente (0°)» y «a la misma distancia»: inferido de «centre front
  reference» y del retardo de compensación de la BS.775; comprobar redacción.

## Preguntas tipo test de comprobación (10)

Repartidas por las siete rúbricas; teoría y aplicación práctica. Contestadas sólo con el tema.

1. (Audio multicanal · práctica) Una escucha 5.1.4 significa: a) 5 altavoces frontales, 1 de graves
   y 4 traseros; **b) 5 canales en el plano horizontal, 1 de baja frecuencia y 4 de altura**; c) 5
   canales y 4 objetos; d) no es un formato. → Entera: «Cómo se nombra un formato».
2. (Audio multicanal · Dolby) En la guía del Dolby Atmos Renderer, la cama de la configuración
   básica es: a) 5.1; **b) 7.1.2**; c) 118; d) 9.1.6. → Entera: «La cama y los objetos de Dolby
   Atmos» (y 118 = objetos).
3. (Dolby) El Dolby E: a) es el códec de emisión al público; **b) lleva hasta ocho canales y sus
   metadatos en un par AES3, para producción y contribución**; c) lleva hasta seis canales sin
   metadatos; d) no admite más de un ciclo de codificación. → Entera: «Qué problema resuelve el
   Dolby E».
4. (Dolby · práctica) Hay que añadir una voz en off a un programa que llega en Dolby E: a) se mezcla
   la voz sobre el par codificado bajando su ganancia; b) se ecualiza el par para dejar hueco; **c)
   se decodifica, se mezcla en PCM y se vuelve a codificar**; d) se hace un corte en la banda de
   guarda. → Entera: «Lo que no se le puede hacer a una señal Dolby E» (más retardo: «El retardo de
   un cuadro», 40 ms a 25 Hz por codificación y por decodificación).
5. (5.1 · práctica) Según la UIT-R BS.775-4, los altavoces envolventes se sitúan: a) a ±30°; b) a
   ±90° exactos; **c) entre 100° y 120° desde el frente, sin que haga falta precisión**; d) a 150°.
   → Entera: «La colocación de los altavoces».
6. (5.1) El canal LFE, según la BS.775-4: a) es el altavoz subgrave y lleva todos los graves; **b)
   está limitado hasta 120 Hz y se graba con −10 dB que la reproducción compensa con +10 dB**; c) es
   un canal de banda completa; d) cuenta en la medida de sonoridad. → Entera: «El canal LFE» y «El
   LFE no es el subgrave».
7. (Estéreo · downmix) En el downmix de 3/2 a estéreo de la BS.775, el canal central entra en cada
   lado con coeficiente: a) 1,0; **b) 0,7071 (−3 dB)**; c) 0,5 (−6 dB); d) no entra. → Entera: «Los
   coeficientes de la UIT» y «El estéreo dentro de la jerarquía».
8. (Mono) En el downmix a mono (1/0) de la BS.775, los envolventes LS y RS entran con coeficiente:
   a) 1,0; b) 0,7071; **c) 0,5**; d) 0. → Entera: «El mono y el envolvente mono». Complemento
   práctico (lectura −1 del correlador = cancelación al sumar a mono): «La suma a mono y la fase».
9. (Downmix) Método de downmix que la UER recomienda por defecto y por qué: **a) Lo/Ro, porque el
   Lt/Rt, por los artefactos de la matriz, da una sonoridad menos predecible y altera el sonido**;
   b) Lt/Rt, porque permite recuperar central y envolventes; c) Lt/Rt, porque desfasa los
   envolventes 180°; d) ninguno. → Entera: «Lo/Ro y Lt/Rt» (±90°) y «Por qué la UER recomienda
   Lo/Ro».
10. (Compatibilidad · práctica) Un programa 5.1 medido a −23 LUFS se entrega también para escucha
    estéreo: a) el downmix estará también a −23 LUFS; **b) hay que medir el downmix, porque su
    sonoridad depende del método, los coeficientes, el contenido, la correlación y la limitación
    (los envolventes difieren 4,5 dB por defecto)**; c) se hace un upmix para compensar; d) se baja
    el nivel global del downmix de forma fija. → Entera: «El downmix y la sonoridad», «La saturación
    del downmix y el upmix» y «Cómo se comprueba».

Resultado: 10 de 10 contestadas enteras con el tema. No ha hecho falta ampliar.
