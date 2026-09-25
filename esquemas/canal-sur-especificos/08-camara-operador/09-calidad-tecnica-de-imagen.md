# Tema 9 del específico de Cámara Operador · Calidad técnica de imagen

**Siglas**: Unión Europea de Radiodifusión (**EBU**); Sector de Radiocomunicaciones de la UIT (**UIT-R**); unidad de control de cámara (**CCU**); técnico de imagen digital (**DIT**); filtro óptico de paso bajo (**OLPF**); densidad neutra (**ND**); alto rango dinámico (**HDR**) y estándar (**SDR**); cuantificación perceptual (**PQ**) e híbrida logarítmica-gamma (**HLG**); relación señal/ruido (**S/N**); grupo de imágenes (**GoP**); índice de consistencia de iluminación (**TLCI**); decibelio (**dB**); megabits por segundo (**Mbit/s**); cuadros por segundo (**fps**); hercio (**Hz**).

Esqueleto para repasar, no resumen. Telegrama, con la recomendación o el manual delante de cada línea; «oficio» donde no hay fuente escrita y el tema lo declara así. Se quita explicación, nunca una cifra: tablas, rangos, porcentajes y valores de fábrica están todos. Redacción vigente el **24/09/2026**.

**Medida.** Unas 2.800 palabras y 145 líneas: por encima de la horquilla del método (2.000/130), y conviene decirlo. El tema no tiene una sola fuente que resumir, sino nueve bloques técnicos (foco, exposición, color, estabilidad, ruido, compresión, continuidad, más los niveles EBU y los instrumentos de medida), cada uno con sus propias tablas numéricas —cuatro tablas de valores de código, dos de primarios y luminancia, varias de mandos de fábrica—. Comprimir más exigiría tirar cifras, lo que el método no permite.

**Cabecera.** Sin norma jurídica: recomendaciones técnicas EBU (R 103 v3.0, R 118 v2, Tech 3335, Tech 3355) y UIT-R (BT.709-6, BT.2020-2, BT.2100-3), Libro de estilo de Canal Sur (2004) y manuales de fabricante (Sony PXW-Z200, Sony PXW-FS5, Blackmagic URSA Broadcast G2, Panasonic AVC-Intra FAQ). Fuentes leídas el **24/09/2026**.

<!-- indice -->

## Índice

- [La calidad técnica de imagen](#la-calidad-técnica-de-imagen)
- [Foco](#foco)
- [Exposición](#exposición)
- [Color](#color)
- [Estabilidad](#estabilidad)
- [Ruido](#ruido)
- [Compresión](#compresión)
- [Continuidad](#continuidad)
- [Lo que este esquema no da](#lo-que-este-esquema-no-da)

<!-- /indice -->

## La calidad técnica de imagen

- R 118 v2 § 1.1: seis criterios · *Noise* (S/N) · *Sensitivity* (diafragma para blanco de pico) · *Exposure Range* (latitud) · *Spatial Resolution* · *Spatial Alias artefacts* · *Codec* (sólo si graba a bordo).
- R 118 v2: «apart from spatial aliasing», los cinco primeros se miden con Tech 3335 · el códec puede rebajar lo que ganó el sensor.
- Tech 3335, índice: apartados de medida · curva Opto-Electrónica (Gamma) · niveles de ruido · sensibilidad · rango de exposición · reproducción de color · respuesta infrarroja · resolución espacial/detalle/*aliasing* · efectos de óptica · efectos temporales/obturador.
- Oficio: en multicámara ajusta el control de imagen desde la CCU; operador responde de encuadre, foco y movimiento, y ejecuta por intercomunicación · en reportaje el operador es su propio control de imagen · DIT: en sistema único, configuración, calibración y ficheros.
- Libro de estilo 6.5 p. 92: el realizador «**es responsable máximo de la corrección de la imagen y de la calidad de la emisión del programa**».
- Libro de estilo 5.1 p. 79: sin realizador, «**el criterio del cámara es imprescindible para proponer soluciones**».
- R 118 v2, niveles HD: Tier 1 profesional hombro/mano · Tier 2L profesional *long-form* · Tier 2J profesional periodismo · Tier 3 semiprofesional pequeña · Tier 4 consumo (con aprobación) · Tier SP especialista/efectos (con aprobación).
- R 118 v2, UHD: UHD1 Tier 1 = 3840×2160 · UHD1 Tier 2 desde 2715×1527 · UHD2 Tier 1 = 7680×4320 · UHD2 Tier 2 desde 5430×3054.
- R 118 v2: Tier 2J es «relajación» consciente por la urgencia del directo · material Tier 3 se limita a «**around 33%**» de un programa HD.
- R 118 v2, tabla 2/§ 2.7: Tier 1 = 10 bits y 4:2:2 (texto: «10-bit processing preferred») · Tier 2L y 2J = 8 bits, 10 preferido.
- Oficio: tres instrumentos en visor/monitor · forma de onda mide luminancia (dice si la exposición está bien) · vectorscopio mide crominancia (dice si el color está bien) · histograma, reparto estadístico de niveles.
- Sony PXW-Z200: visor con «**waveform, vectorscope, or histogram**» · línea naranja = nivel de cebra fijado.
- Oficio, monitor de referencia: *Blue only* (croma/fase y ruido) · *Underscan* (bordes) · marcadores y zonas de seguridad · falso color y cebras.
- Oficio: señales de prueba, barras de color (croma/fase/nivel) y rampa/diente de sierra (delata curvatura o escalón en la forma de onda).

## Foco

- Oficio, Seidel, cinco aberraciones monocromáticas: esférica (borde vs. centro) · coma (punto fuera de eje) · astigmatismo (radial/tangencial no coinciden) · curvatura de campo (bordes blandos) · distorsión (barril/corsé) · aparte, la cromática (índice de refracción según longitud de onda).
- Oficio: punto dulce en aperturas intermedias · abertura máxima = aberraciones · abertura mínima = difracción (física, no de calidad de la lente) · en la práctica, cerrando 2-3 pasos desde la máxima.
- Sony PXW-FS5: difracción por cerrar mucho el iris con mucha luz → «**Using the ND FILTER dial A suppresses this phenomenon**» · aviso: no cambiar el ND en plena grabación (distorsiona imagen o sonido).
- Blackmagic URSA G2: comprobar tiraje al montar un objetivo B4 y al cambiarlo · oficio, también tras un golpe o cambio grande de temperatura.
- Oficio, método de tiraje en 4 pasos: 1) enfocar en tele sobre punto lejano, diafragma abierto · 2) ir a angular sin tocar el foco · 3) corregir con el anillo de tiraje, no el de foco · 4) recorrer el zoom entero comprobando.
- Sony PXW-FS5: *peaking* (realce de contornos) y lupa ayudan a enfocar · ninguno se graba · nivel de realce se adapta al plano (rostros, más; follaje/ladrillo, menos, según Blackmagic URSA G2).
- Sony PXW-FS5: autofoco por detección de caras, con límites («puede no detectar caras según el entorno, el sujeto o los ajustes»).
- R 118 v2 § 3.1.4: «**sensor pixel count is not an acceptable measure of a camera's actual resolution**» · resolución real, con cartas (Tech 3335).
- R 118 v2 § 3.1.5: *aliasing* se mueve en dirección contraria a la cámara · hace fallar la compresión dependiente del movimiento en el extremo.
- Oficio: *moiré* = interferencia trama sujeto/sensor, se combate con el OLPF y, en toma, cambiando focal o distancia.
- Oficio, dos defectos de sensor: *blooming* = halo alrededor de zona muy iluminada (fotodiodo saturado desborda a vecinos, en todas direcciones) · *smear* = raya vertical desde fuente brillante (propio del CCD, sólo en vertical).

## Exposición

- Oficio: cuatro mandos, orden correcto = diafragma → obturación → ND → ganancia (último recurso) · cada uno tiene precio (profundidad de campo, nitidez del movimiento, luz, ruido).
- Blackmagic URSA G2: pasar de 25 a 50 fps reduce la luz a la mitad; compensar abriendo un paso, obturación a 360º o más luz.
- R 103 v3.0, anexo 1, tabla 1, valores de código: 8 bits, nominal **16-235**, preferente **5-246**, total **1-254** · 10 bits, **64-940** / **20-984** / **4-1019** · 12 bits, **256-3760** / **80-3936** / **16-4079** · 16 bits, **4096-60160** / **1280-62976** / **256-65279**.
- R 103 v3.0: fuera del rango preferente = error de gama · instrumentos sólo avisan de «Out-of-Gamut» si el error supera **1 %** de la imagen.
- R 103 v3.0: directo, recortadores de cámara al rango preferente · material pregrabado y etalonado, al límite nominal.
- R 103 v3.0: recorte causa distorsión armónica y artefactos, más tasa de datos · legalizadores automáticos, con cautela · sub-negros no se recortan (impide el ajuste PLUGE, anexo 2) · analógico, rango **0-700 mV**.
- Aviso de estudio: los porcentajes «−1 %» y «103 %» atribuidos a la EBU no están en R 103 v3.0, que usa valores de código.
- Oficio: *knee* comprime altas luces por encima del codo para no recortar de golpe · mandos, punto del codo, pendiente y recorte de blancos.
- Sony PXW-Z200: [Knee] [Auto Knee] activados de fábrica en SDR, punto **75%-109%** (fábrica **90%**), pendiente **−99 a +99**.
- Tech 3335 § 4.4: alto contraste, curva ITU.709, *knee* manual **80%-90%** para mantener la piel en la parte normal de la gamma · top **14%** de la señal ≈ 1 paso, bajar pendiente sube al menos 1 paso más.
- Tech 3335 § 4.4: bajo contraste, curva BBC0.4 o ITU.709, recorte de blancos ≤ **104%** · curvas de cine en directo, nunca por encima de **100%** · ajustar el *knee* con diente de sierra y forma de onda.
- Tech 3335 § 4.4: *black-stretch* abre sombras, *black-press* las cierra · el *stretch* sube la ganancia cerca del negro y el ruido con ella · mejor en cámara que en posproducción (menos artefactos de compresión).
- Sony PXW-FS5: [BLACK GAMMA] **−7 (compresión máx.) a +7 (estiramiento máx.)**.
- Sony PXW-Z200: [Master Black] [R Black] [B Black], **−99.0 a +99.0**.
- R 118 v2 § 3.1.3: latitud limitada abajo por el ruido, arriba por el recorte · margen sobre blanco de referencia, **1 a 3 pasos** según la cámara.
- Tech 3335 § 4.4: cámara típica con ruido ≈ **−50 dB** capta ≈ **7,5 pasos** de fábrica · ruido alto reduce el rango ≈ **1 paso por cada 6 dB** de subida · gamma/*knee* puede sumar **1 paso** extra, en casos extremos hasta **3**, hasta **12-13 pasos** totales.
- Sony PXW-FS5: cebra, nivel **70 a 100, o 100+**, no se graba · con 100 % marca sobreexposición total · Blackmagic URSA G2: bajar el nivel avisa antes en luz variable.
- Blackmagic URSA G2: falso color, de amarillo a rojo = sobreexpuesto (escala no normalizada entre fabricantes).
- BT.2100-3: HDR con curva PQ o HLG · HLG, mayor compatibilidad con pantallas heredadas.
- BT.2100-3, nota 10a: blanco de referencia HDR = **203 cd/m²** en pantalla PQ o en HLG con pico nominal de **1.000 cd/m²**.
- Sony PXW-Z200: en salida HLG, conversión sencilla a SDR en el visor.

## Color

- BT.709-6: primarios rojo **(0,640; 0,330)**, verde **(0,300; 0,600)**, azul **(0,150; 0,060)**, blanco D65 **(0,3127; 0,3290)**.
- BT.2020-2: primarios rojo **(0,708; 0,292)**, verde **(0,170; 0,797)**, azul **(0,131; 0,046)**, mismo blanco D65 · BT.2100-3 usa los primarios de BT.2020.
- Oficio: coeficientes de luminancia · BT.601, R **0,299** G **0,587** B **0,114** · BT.709, R **0,2126** G **0,7152** B **0,0722** · BT.2020, R **0,2627** G **0,6780** B **0,0593** (verde pesa más, azul menos).
- BT.709-6: el aspecto final se juzga en un monitor de referencia con la función de decodificación de BT.1886.
- Oficio: balance de blancos, tres caminos · automático sobre carta blanca (fiable, con tiempo) · preajuste **3.200 K** o **5.600 K** (sin tiempo) · automático continuo (luz cambiante, tonos a la deriva).
- Oficio: la cámara vira hacia el complementario de la superficie de balance · azul → imagen cálida · naranja/ámbar → fría · verde → magenta · blanco/gris neutro → neutra.
- Oficio: balance de negros iguala los tres canales en negro · en reportaje, [R Black]/[B Black]; en estudio, lo hace el control de imagen.
- Sony PXW-Z200: matriz de usuario, [User Matrix Level] (intensidad) y [User Matrix Phase] (tono), sobre toda la imagen · matriz múltiple, tono/saturación por eje, **16** ejes.
- Sony PXW-Z200: archivo de escena guardable en tarjeta y cargable en otra cámara · el fabricante avisa: no reproduce del todo el ajuste original, y entre modelos distintos puede variar.
- Tech 3355 § 1.5.2: TLCI-2012, valor **50** = frontera entre luminarias corregibles y no corregibles para televisión.
- Oficio: 8 bits = **256** niveles, 10 bits = **1.024**, 12 bits = **4.096** (2 elevado al número de bits) · defecto sin suficientes bits: bandeado.
- Oficio, submuestreo: 4:4:4 sin submuestreo (grafismo/croma/cine) · 4:2:2 mitad en horizontal (estándar de producción) · 4:2:0 mitad en horizontal y vertical (emisión/distribución) · croma sobre 4:2:0 recorta mal · R 118 v2 asigna 4:2:2 al Tier 1.
- Oficio: vectorscopio, ángulo = tono, distancia al centro = saturación · centro = sin color.

## Estabilidad

- Libro de estilo 5.2 p. 80: «**En circunstancias normales, la cámara se instalará sobre el trípode**», sin descartar el hombro en recursos de rueda de prensa o entrevista.
- Oficio: estabilización pasiva (masa, inercia, contrapesos, cardanes libres — steadicam clásica) vs. activa (motores y sensores — gimbals de tres ejes, estabilización óptica) · las fricciones de una cabeza fluida amortiguan, no estabilizan.
- Oficio: a más focal, más se nota el temblor; al hombro se trabaja en angular y se acerca el operador en vez de hacer zoom.
- Sony PXW-Z200: [Standard] reduce el temblor · [Active] corrección más potente (al caminar), pero desplaza el encuadre hacia teleobjetivo.
- Sony PXW-Z200: en trípode, estabilizador en [Off] (con [Standard]/[Active] y *pan/tilt* lentos, la imagen se distorsiona) · a mano, ajustar el estabilizador si el *pan/tilt* lento distorsiona.
- Sony PXW-Z200: parpadeo con fluorescentes, sodio, vapor de mercurio o LED · BT.2020-2: la frecuencia de la red influye en la elección de cadencia.
- Blackmagic URSA G2: el parpadeo puede no verse en visor/SDI ni al grabar; probar antes con las luces reales.
- Tech 3335 § 2.9.1: obturación nominal **1/50 s a 50 Hz**, **1/60 s a 59,94 Hz**, o **180 grados** en ambas · oficio, con red de 50 Hz, 1/50 o 1/100 evita el parpadeo.
- Sony PXW-Z200: [Flicker Reduce] [Auto]/[On]/[Off] (fábrica [Off]), frecuencia [50Hz]/[60Hz] (fábrica **[60Hz]**, cambiar en España).
- Tech 3335 § 2.9: CCD sin efectos temporales raros · CMOS con *rolling shutter*: verticales inclinadas, bordes distorsionados, imagen gelatinosa con movimiento rápido · oficio, se reduce moviendo más despacio y fijando mejor.

## Ruido

- Oficio: el ruido viene sobre todo de la ganancia, que amplifica señal y ruido por igual.
- Oficio (cálculo): un paso de diafragma duplica la luz; en dB de tensión, duplicar ≈ **+6 dB** (20 · log₁₀ 2).
- Oficio: **+3 dB** = medio paso, ruido poco · **+6 dB** = 1 paso, apreciable · **+12 dB** = 2 pasos, mucho · **+18 dB** = 3 pasos, imagen ya ruidosa.
- Sony PXW-Z200: puntos blancos (rayos cósmicos) más visibles con temperatura ambiente alta o con la ganancia subida.
- R 118 v2, tabla 6 (orientativa): S/N mejor que **−48 dB a 0 dB de ganancia** en Tier 1 · **−44 dB** en Tier 2L · **−40 dB** en Tier 2J y Tier 3 · el ruido se valora también por su impacto visible, no sólo por la cifra.
- R 118 v2: algunos menús permiten ganancia negativa, que mejora la S/N.
- Oficio, controles del realce de detalle: nivel · frecuencia (bordes finos/gruesos) · dependencia del nivel (apaga el realce en sombras, donde el ruido es peor) · recorte/*crispening* (ignora diferencias pequeñas).
- Sony PXW-Z200: [Detail] nivel **−7 a +7** · [B/W Balance] reparte detalle entre sombras y luces · [Crispening] **0 a 7**.
- Tech 3335 § 4.3: sobreimpresión moderada en bordes de alto contraste es aceptable, «signature of the videolook».
- Sony PXW-Z200: [Noise Suppression] **[Low]/[Mid]/[High]**, fábrica **[On]/[Mid]** en modo personalizado.

## Compresión

- Oficio: la transformada discreta del coseno convierte bloques de píxeles en coeficientes de frecuencia, sin comprimir por sí sola.
- Oficio: la recuantificación desecha altas frecuencias según el flujo de datos; ahí está la pérdida.
- Oficio: defectos visibles, bloques en zonas lisas, contornos sucios, detalle fino que desaparece o «hierve».
- R 118 v2 § 1.3.1: tres familias · RAW (sin procesar) · I-Frame/intracuadro (sin compresión temporal, cada cuadro solo) · *Long GoP* (más ahorro, procesa varios cuadros).
- Panasonic AVC-Intra FAQ (documentación comercial): intracuadro sin interacción entre cuadros, aguanta bien montaje y movimiento · *Long GoP*, cualquier manipulación degrada mucho la imagen.
- R 118 v2, tabla 1 (mínimos, 10 bits SDR): intracuadro Tier 2L+ **100 Mbit/s** a 25 fps / **200** a 50 fps · intracuadro Tier 2J- **50** / **75** · H.264 (AVC) Tier 2L+ **25** / **35** · MPEG-2 en UHD, «**Not to be used**».
- Oficio: el *aliasing* y el recorte hacen fallar o encarecen la compresión · el ruido gasta flujo de datos · el temblor obliga al *Long GoP* a codificar mucho cambio.

## Continuidad

- Libro de estilo 6.4 p. 92: «**raccord**», continuidad y uniformidad visual de los planos · primer aspecto, el técnico: «**No deben permitirse diferencias de color, brillo, contraste, tono, luz, altura de planos, calidad de la imagen**».
- Libro de estilo 6.3.4 p. 91: cuidado con el material de archivo, por la distorsión técnica y el contraste de indumentaria o situación.
- Oficio: en informativos la continuidad se asegura en la grabación, no en el montaje.
- Oficio, con una sola cámara: balance automático continuo → balance fijo en memoria · diafragma automático → manual en entrevista/plano fijo · ganancia distinta entre planos → misma ganancia en toda la pieza · luz que cambia con la hora → grabar plano y contraplano seguidos · ajustes tocados en el menú → volver al archivo de escena conocido.
- Oficio, entre cámaras: en estudio y unidad móvil, lo iguala el control de imagen (nivel, color, sombras, altas luces, detalle) · en reportaje, cada operador iguala la suya: mismos ajustes de imagen (archivo de escena, con las salvedades del fabricante), balance sobre la misma carta y luz, misma cadencia y obturación, cámaras de nivel parecido (Tier 3 ≤ 33 % de un programa HD).
- Tech 3355: escala TLCI propia para multicámara en directo, sin posproducción, «sólo creíble»; las escalas «no forman definiciones rígidas».

## Lo que este esquema no da

Criterios de calidad propios de CSRTV (niveles admitidos, códecs, procedimientos del control de imagen): no constan en documento publicado. Procedimiento de igualación de cámaras desde la CCU: oficio del control de imagen, sin fuente leída. Nivel HLG del blanco de referencia en porcentaje: en el Informe UIT-R BT.2408, no leído. Umbrales por tramos del TLCI: en una figura de Tech 3355 no leída como texto. Filas de la tabla de tasas EBU no reproducidas (MPEG-2 HD, H.264 2J-, H.265, códecs UHD): tabla 1 de R 118. Obturador global de estudio: documentación de fabricante no leída. Mandos básicos de cámara (tema 1), *raccord* completo (tema 2), soportes (tema 4), temperatura de color (tema 5), formatos y códecs (tema 7), estabilización creativa (tema 15).
