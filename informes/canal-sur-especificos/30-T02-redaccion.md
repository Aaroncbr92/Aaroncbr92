# Puesto 30 · Tema 2 · Redacción (fase 2)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/02-senal-de-video-y-audio.md`.
Material: `30-investigacion-A-tecnica.md` (§§ 2.1-2.4 y 4.1); cerrados de Canal Sur 08-09 (Cámara
Operador) y 28-11 (Operador/a de Sonido); RTVE `edicion-montaje/04`, `03` y `02` («actualizar: no»).

## Fuentes releídas y fecha

| Fuente | Qué se releyó | Fecha |
|---|---|---|
| UIT-R BT.709-6 (txt nuevo de `fuentes/canal-sur/montador/itu/bt709.pdf`) | Puntos 1.2-1.4, 2, 3.1-3.3, 4.1-4.7, 5.1-5.8, parte 2 (PsF) y anexo 2 | 25-09-2026 |
| UIT-R BT.2020-2 (txt nuevo) | Tabla 1 (formatos, 16:9), frecuencias, red eléctrica, notas 2-3 al cuadro 4 (CL/NCL), 10 o 12 bits | 25-09-2026 |
| UIT-R BT.2100-3 (txt existente) | Tabla 3 (≥ 1 000 y ≤ 0.005 cd/m², nota 3c), NCL/CI, submuestreo, tabla 9, nota 1b | 25-09-2026 |
| Informe UIT-R BT.2408-9 (txt nuevo) | § 2.1 y tabla 1 con sus notas | 25-09-2026 |
| EBU R 68-2000 (txt nuevo) | Texto completo (1 página) | 25-09-2026 |
| EBU R 128-2023 (txt nuevo) | Recomendaciones g-t y definiciones | 25-09-2026 |
| SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023 (txt nuevos) | Velocidades, NRZI, atenuación, BNC 75 Ω | 25-09-2026 |

## Qué se hizo

Tres rúbricas: vídeo, audio y (como bloque de unión que el encargo pide: «código de tiempo») vídeo y
audio juntos. 28 epígrafes; `indice.py`: 10.729 palabras. `refutar_prosa.py`: 1 hallazgo, falso
positivo («BC» dentro de la cita literal «Y'C'BC'R» de la BT.2020). Tema técnico sin norma jurídica:
no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

Negrita = literal de la fuente. Lo copiado de RTVE va en redonda (RTVE lo tenía en negrita sin ser
cita); lo copiado de 08-09 y 28-11 conserva sus negritas, que sí son citas.

Comprobación de literalidad hecha por script (bloques del tema buscados en las fuentes normalizadas,
RTVE sin negritas): lo listado abajo como literal aparece tal cual.

## Copiado del común

Epígrafes y pasajes copiados literal de temas cerrados de Canal Sur (no se re-verifican).

`temas/canal-sur-especificos/08-camara-operador/09-calidad-tecnica-de-imagen.md`:

| Pasaje en 08-09 | Dónde va |
|---|---|
| «La colorimetría de referencia», entero (dos párrafos, tabla de coeficientes, párrafo del verde, cita BT.1886) | § 1 «La colorimetría de referencia» |
| «Profundidad de bits y submuestreo», párrafos 1 y 2 («La profundidad de bits es…», «Con más bits…») | § 1 «La cuantificación» |
| Ídem, párrafo «El submuestreo cromático reduce…» y párrafo «El submuestreo limita…» sin su última frase (la de los niveles EBU, que remitía a otro epígrafe de 08-09) | § 1 «El muestreo de la señal» |
| «Los límites de la señal según la EBU», entero | § 1, epígrafe homónimo |
| «La exposición en alto rango dinámico», párrafo 1 entero y párrafo 2 hasta «(BT.2100-3, nota 10a).» (se quita la frase que declaraba no leído el Informe BT.2408: aquí se da) | § 1 «El alto rango dinámico» |
| «Los instrumentos de medida»: tabla de instrumentos; párrafo «La regla que separa los dos primeros…»; tabla del monitor de referencia con su frase de entrada; párrafo de las señales de prueba (se omiten la entrada «Los tres que un operador encuentra en el visor…» y las citas de Sony) | § 1 «Medir la señal» |
| «Medir el color», entero | § 1 «Medir la señal» |

`temas/canal-sur-especificos/28-operador-a-de-sonido/11-lineas-y-conexiones.md`:

| Pasaje en 28-11 | Dónde va |
|---|---|
| «AES/EBU · Qué es», párrafo 1 | § 2 «La interfaz AES/EBU» |
| «La estructura: subtrama, trama y bloque», las tres viñetas y el párrafo «Cada trama lleva una muestra…» | ídem |
| «Los cables y sus impedancias», tabla | ídem |
| «El audio embebido en SDI», párrafo de entrada y tabla | § 2 «El audio dentro del vídeo: embebido en SDI» |
| «Grupos, pares y espacio auxiliar», entero | ídem |
| «Qué es embeber y desembeber», tabla | ídem |
| «Por qué UDP y cuánto ocupa un canal»: la fórmula en cita y la frase «A 48 kHz y 24 bits, un canal son 1,152 megabits por segundo. Ése es el número que hay que tener.» | § 2 «Del sonido analógico al digital» |
| «El reloj del audio embebido», párrafo 1 | § 3 «La sincronía entre imagen y sonido» |

## Copiado de RTVE sin cambios

Palabras sin tocar; sólo se quitó la negrita. Temas RTVE marcados «actualizar: no».

`temas/edicion-montaje/02-colorimetria.md`:

| Pasaje RTVE | Dónde va |
|---|---|
| § 1, párrafo «El ojo humano tiene tres tipos de conos…» | § 1 «Cómo se forma el color» |
| § 1, tabla de las cuatro leyes de Grassmann | ídem |
| § 2, párrafos «Un color espectral es…» y «Un color no espectral es…» | ídem |
| § 3, párrafo «La televisión no transmite rojo, verde y azul…» | § 1 «Luminancia y diferencias de color» |
| § 4, tabla CL/NCL y párrafo «Por qué existen las dos…» | ídem |
| § 5, párrafo 1 («La gamma es la relación no lineal…») y las cuatro viñetas de la curva logarítmica | § 1 «La gamma y la curva logarítmica» |
| § 7, párrafo 1 («El alto rango dinámico amplía…») y tabla de unidades (*nit*, candela, cd/cm², lumen) | § 1 «El alto rango dinámico» |

`temas/edicion-montaje/04-tratamiento-digital-de-la-senal.md`:

| Pasaje RTVE | Dónde va |
|---|---|
| § 1, tabla de resoluciones (seis filas) y párrafo «La confusión que hay que deshacer…» sin su última frase («El examen usa…») | § 1 «Resolución y relación de aspecto» |
| § 3, párrafo de entrada, tabla de muestreos (cuatro filas) | § 1 «El muestreo de la señal» |
| § 4, párrafo 1 («En el barrido progresivo…») y los tres pasos numerados | § 1 «El barrido» |
| § 6, tabla compuesto / componentes / digital | § 1 «Vídeo compuesto, por componentes y digital» |
| § 10, párrafo «Hay dos modalidades…», tabla DF/NDF, párrafo «El malentendido más común…» | § 3 «El código de tiempo» |

`temas/edicion-montaje/03-conceptos-basicos-de-sonido.md`:

| Pasaje RTVE | Dónde va |
|---|---|
| § 1 entero salvo la frase «Confundirlas es el error que este punto castiga.» (tabla y dos párrafos) | § 2 «Las cualidades del sonido» |
| § 2, párrafo «Qué son los armónicos…» y párrafo «Y una consecuencia de oficio…» | ídem |
| § 3 entero (frase de entrada, tabla y los tres párrafos de reglas) | § 2 «Del sonido analógico al digital» |

## Adaptado de RTVE (sí se verifica)

Frases literales de RTVE reunidas o con una cláusula quitada o cambiada, siempre la referida al examen
de RTVE («Ésa es la respuesta oficial…», «el examen pregunta…», «las opciones falsas…», «punto 5.5 del
anexo»):

- R02 § 1: «Las leyes de Grassmann… siglo XIX» (sin «y el examen pregunta por la primera») y aviso de
  orden variable tomado de su Trazabilidad; § 2: los no espectrales y la «línea de los púrpuras».
- R02 § 3-4: la consecuencia del NCL (se añade «(oficio)»); las citas de la BT.2020 en español que
  daba RTVE se sustituyen por el original inglés.
- R02 § 5: la BT.709 ya no se parafrasea: se da la fórmula del punto 1.2 y el 0.45 del 3.1, leídos.
  La frase de la curva logarítmica, sin «Ésa es la respuesta oficial…».
- R02 § 6: «La distinción que resuelve la pregunta» → «Resolución espacial es…».
- R02 § 7: cifras del monitor HDR actualizadas de la BT.2100-1 que citaba RTVE a la **BT.2100-3**
  (tabla 3: «≥ 1 000 cd/m2», «≤ 0.005 cd/m2»; se comprobó que no cambian) y añadida la nota 3c; la
  pregunta 50 se reduce a la regla del monitor HDR; «gama y rango, dos ejes».
- R04 § 1: primera frase sin «y el examen pregunta por las dos»; «lo que UHD multiplica…» reformulado.
- R04 § 3: el 4:4:4:4 y el canal alfa, sin la respuesta oficial ni el «punto 5.5 del anexo».
- R04 § 4: «En el sistema PAL… parpadeo» sin la cláusula de respuesta oficial; lectura de 1080 50i
  reformulada y cotejada con la BT.709-6 (50/I: campo 50 Hz, 2:1, imagen 25 Hz).
- R04 § 5: la cadena mnemotécnica 601-709-2020-2100 (sin «Con esas cuatro se contestan…»).
- R04 § 6: frase de la modulación en amplitud y párrafo «Por qué…», reunidos; descartes resumidos.
- R04 § 7: *jitter*, frases literales reunidas en dos párrafos y cierre propio sobre «ruido de fase».
- R04 § 10: primer párrafo con una frase añadida de oficio; «En un sistema de 25 fps usaremos… NDF» y
  «Por qué, en una frase…» reunidos; añadida la cuenta de los 3,6 s/h.
- R03 § 2: «Lo que cambia de un instrumento…» sin la frase final sobre «el enunciado».
- No se copian de R04 los §§ 8-9 (compresión y códecs: tema 4) ni el § 5 sobre SMPTE 274M/296M (no
  leídas; van a «Lo que este tema no da»). No se copian de R03 los §§ 4-6 (RTP, EQ, *ducking*: temas 4
  y 7) ni de R02 el § 8 (LUT: tema 7).

## Discrepancias encontradas (manda la fuente)

- **08-09 declaraba no leído el Informe BT.2408**: aquí se lee (BT.2408-9, 03/2026) y se da la tabla 1
  (75 % HLG, 58 % PQ, 203 cd/m²). La frase de 08-09 no se copia.
- **RTVE 02 citaba la BT.2100-1**; la vigente es la **-3** (02/2025). Las cifras del monitor HDR no
  cambian.
- **EBU R 68, «161 bits»**: el PDF imprime la llamada de nota 1 pegada al 16. Se cita «16 bits».
- **EBU R 128, piezas cortas**: la investigación no lo traía; la definición de «Programme» incluye
  promos y tráileres, y la recomendación q) remite a R 128 s1 (no leída).
- **BT.709, «25 interlace» y «50/I»**: la tabla de la parte 2 cuenta cuadros (25 interlace) y la del
  punto 5 da campo 50 Hz, imagen 25 Hz. El oficio dice 1080i50 o 50i. Se explican las dos notaciones.
- **PsF**: añadida con el anexo 2 de la BT.709-6 (no estaba en la investigación).
- **Velocidades SDI**: se derivan por cálculo de las frecuencias de muestreo de la BT.709 (74,25 × 2 ×
  10 = 1.485 Mb/s, etc.); casan con las ST 292-1, 424 y 2082-1.

## Ficheros tocados

- Creado: el tema `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/02-senal-de-video-y-audio.md`.
- Creado: este informe.
- Creados (texto de PDF ya guardados por la investigación, con `documento.py texto`):
  `fuentes/canal-sur/montador/itu/bt709.txt`, `bt2020.txt`, `bt2408.txt`;
  `fuentes/canal-sur/montador/ebu/r068.txt`, `r128.txt`;
  `fuentes/canal-sur/montador/smpte/st0259-2008.txt`, `st0424-2012.txt`, `st2082-1-2023.txt`,
  `st292-1-2018.txt`.
- Ningún otro.

## Preguntas de control (10) y cobertura

| Nº | Rúbrica | Pregunta y respuesta | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Vídeo · colorimetría (teoría) | La luminancia en la UIT-R BT.709 es: a) 0,299 R + 0,587 G + 0,114 B; b) 0,2627 R + 0,6780 G + 0,0593 B; c) 0,2126 R + 0,7152 G + 0,0722 B ✔; d) 0,2637 R + 0,6790 G + 0,0593 B | Entera, § 1 «La colorimetría de referencia» (a es BT.601, b es BT.2020; d, ninguna, con la regla de la suma) |
| 2 | Vídeo · barrido | En una señal HD 1080i50 hay por segundo: a) 50 cuadros completos; b) 50 campos, es decir, 25 cuadros ✔; c) 25 campos; d) 100 campos | Entera, § 1 «El barrido» (BT.709 50/I: campo 50 Hz, imagen 25 Hz) |
| 3 | Vídeo · cadencias | ¿Qué frecuencia de imagen NO figura en la UIT-R BT.2020-2? a) 100 Hz; b) 120/1,001 Hz; c) 25/1,001 Hz ✔; d) 24/1,001 Hz | Entera, § 1 «Las cadencias» (lista literal; sólo 24, 30, 60 y 120 tienen /1,001) |
| 4 | Vídeo · muestreo | En HD según la BT.709-6, cada línea activa tiene: a) 1.920 muestras de Y y 1.920 de cada diferencia de color; b) 1.920 de Y y 960 de CB y 960 de CR ✔; c) 1.920 de Y y 480 de cada una; d) 960 de Y y 1.920 de color | Entera, § 1 «El muestreo de la señal» |
| 5 | Vídeo · cuantificación (aplicación) | En el monitor de forma de onda de una pieza en 10 bits el blanco llega al código 990. Según EBU R 103: a) está dentro del rango nominal; b) está en el rango preferente; c) es error de gama, fuera del rango preferente (20-984) ✔; d) se recorta siempre | Entera, §§ «La cuantificación» y «Los límites de la señal según la EBU» |
| 6 | Vídeo · HDR (aplicación) | Al insertar un rótulo blanco en un programa HLG, su nivel de señal según el Informe UIT-R BT.2408 es: a) 100 %; b) 90 %; c) 75 % ✔; d) 58 % (el de PQ) | Entera, § 1 «El alto rango dinámico» |
| 7 | Vídeo · interfaz | El 3G-SDI (SMPTE ST 424) transporta: a) 1,485 Gb/s; b) 2,970 Gb/s ✔; c) 270 Mb/s; d) 11,88 Gb/s. (Variante: qué formato pide 3G: el 1080p50) | Entera, § 1 «La interfaz digital serie (SDI)» |
| 8 | Audio · digital | Cada bit de profundidad añade al rango dinámico del audio digital aproximadamente: a) 3 dB; b) 6 dB ✔ (24 bits ≈ 144 dB); c) 10 dB; d) 12 dB. Y la frecuencia de muestreo de televisión es 48 kHz | Entera, § 2 «Del sonido analógico al digital» |
| 9 | Audio · niveles (aplicación) | Una promoción que se entrega para emisión debe cumplir, según EBU R 128-2023: a) −18 dBFS de pico; b) −23,0 LUFS de sonoridad integrada y un pico verdadero que no pase de −1 dBTP ✔; c) −23 dBFS de pico y −1 LUFS; d) −24 LKFS. (Distractor a: es el nivel de alineación de la R 68) | Entera, § 2 «La sonoridad» y «Los niveles del audio digital» (la promo es programa, por definición de la R 128) |
| 10 | Vídeo y audio · código de tiempo | En un sistema de 25 fps se usa código de tiempo: a) DF, porque 25 no es entero; b) NDF ✔; c) DF para corregir 3,6 s por hora; d) indistintamente. (Variante: el *drop frame* salta números, no cuadros) | Entera, § 3 «El código de tiempo» |

Resultado: 10 de 10 contestadas enteras con el tema; no hizo falta ampliar. Cobertura: colorimetría
(1), barrido (2), cadencias (3), muestreo (4), cuantificación y límites (5), HDR (6), SDI (7), audio
digital (8), niveles y sonoridad (9), código de tiempo (10); aplicación práctica en 5, 6, 7 (variante),
9 y 10. Otras preguntas posibles que el tema también contesta: canales embebidos en HD-SDI (16, en
cuatro grupos), canales de la AES/EBU (2), 4:4:4:4 (canal alfa), NCL frente a CL, *jitter*, PsF.
