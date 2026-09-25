# Tema 7 del específico de Operador/a Montador/a de Vídeo · Postproducción

**Siglas**: RTVA; CSRTV; UIT-R; UER (EBU); HDR (HLG y PQ), SDR; LUFS, LU, dBTP; SNR; HSL; LUT (1D/3D); RGB, CB/CR, YRGB.

Esqueleto para repasar, no resumen: cada línea remite a un dato del tema; se lee el tema entero antes del examen.

<!-- indice -->
<!-- /indice -->

## 1. Color básico

- Oficio — etalonar: llevar la imagen a un patrón; fases: técnico/primario, igualación, creativo/secundario, comprobación de entrega.
- Oficio — «corrección» = técnico; «etalonaje» = técnico + aspecto (sinónimos en la sala).
- Resolve 21, cap. 127 — cinco monitores de señal: forma de onda, desfile (*parade*), vectorscopio, histograma, diagrama CIE.
- Resolve 21, cap. 127 — forma de onda: negros/blancos y salida de rango; desfile: compara R/G/B por zona tonal (dominantes); vectorscopio: matiz (ángulo) y saturación (distancia al centro), dianas de barras al 75 %.
- Resolve 21, cap. 127 — gráficas altas del desfile = mucho contraste; bajas = poco.
- Resolve 21, p. 3147 — monitores HDR sin gestión de color: forma de onda no fiable en Rec. 709.
- Oficio — LUT: tabla de consulta, no calcula, consulta.
- Resolve 21, cap. 150 — LUT técnica/conversión vs. creativa/*look*; LUT 1D (curvas por canal) vs. 3D (cubo RGB, tono y saturación).
- Resolve 21, cap. 150 — formatos nuevos CLF y DCTL: fórmulas, no tablas.
- Resolve 21, cap. 150 — formato .cube (17/33/65 puntos); 17 no recomendado para etalonar.
- Resolve 21, cap. 150 — LUT sobre plano mal expuesto exagera el error; LUT 3D recorta fuera de rango (*shaper LUT* lo evita).

## 2. Corrección

- Oficio — primaria: imagen entera (negros, blancos, contraste, balance, saturación); secundaria: una zona, un color, un objeto.
- Oficio — primero primaria de todos los planos, después secundaria donde haga falta.
- Resolve 21, cap. 125/131 — *lift* (sombras), *gamma* (medios tonos), *gain* (altas luces), *offset* (todo el rango); zonas solapadas, escala 0-1023.
- Resolve 21, cap. 131 — temperatura (*Temp*, −4000/+4000, eje cálido-frío) y matiz (*Tint*, −100/+100, eje magenta-verde) son ajustes del *gain*; dominante sólo en sombras se corrige en *lift*.
- Resolve 21, cap. 131 — contraste con pivote (curva en S por defecto, sin recorte); saturación (50 = unidad); realce de color (*Color Boost*, no uniforme).
- Resolve 21, p. 3201 — *Auto Color*: balance automático para Rec. 709/gamma 2,4; punto de partida, se comprueba en monitores.
- Resolve 21, cap. 125 — secundaria = ventana (forma) o cualificador HSL/RGB/luminancia (color, como un croma que decide dónde corregir).
- Resolve 21, cap. 125 — «color de memoria»: piel, vegetación, cielo tienen tono esperado; se aísla y corrige si se aparta.
- Resolve 21, cap. 125 — igualar planos: comparar con imagen fija guardada, copiar corrección o agrupar planos.
- Oficio — orden: referencia (total/presentador) primero, resto contra ella, en monitores antes que a ojo; piel en mismo punto del vectorscopio en dos cámaras.
- Libro de Estilo CSRTV, 9.2.12.4 — en sucesos: cámara en mano, música tópica, virado a blanco y negro evocan ficción, no en información; el virado cabe en promoción/pieza cultural, no en informativo (oficio).

## 3. Efectos

- Oficio — efecto = todo lo que no es corte directo: composición, transformación, tiempo, imagen, transición.
- Oficio — familias de incrustación: *chroma key* (color), *luma key* (brillo), canal alfa (cuarto canal), máscara/*roto* (forma dibujada).
- Oficio — fondo verde/azul: más alejados de la piel; verde domina por el doble de fotositos verdes del sensor (menos ruido).
- Oficio — croma: fondo iluminado uniforme, sujeto sin ropa del color del fondo, limpiar el tinte del rebote; submuestreo cromático fuerte da peores bordes (tema 2).
- Oficio — tres señales de incrustación: fondo (*background*), relleno (*fill*), recorte (*key*); el alfa no es 4ª señal, es el recorte pegado al relleno en un mismo fichero.
- Oficio — canal alfa: 0 = transparente, intermedio = mezcla, máximo = opaco; notación 4:4:4:4 (tema 2).
- Oficio — máscara de capa: escala de grises pegada a la capa (blanco = ve, negro = no, gris = a medias); alfa dibujado a mano; permite corregir el rótulo después.
- Oficio — fotograma clave (*keyframe*) fija qué y dónde; curva de velocidad fija el cómo (interpolación).
- Resolve 21, cap. 55, p. 1199 — suavizado (*Ease*) de transición: *None*, *In*, *Out*, *In & Out*, *Custom*.
- Resolve 21, cap. 58, pp. 1254-1266 — cámara lenta/rápida (*Change Clip Speed*, *Retime Controls*, *Fit to Fill*); marcha atrás (*Reverse Speed*); congelado (*Freeze Frame*, todo el clip o un tramo); velocidad variable (puntos de velocidad, mínimo dos).
- Resolve 21, p. 1254-1256 — audio: cambios lineales mantiene duración con corrección de tono opcional; velocidad variable silencia el audio.
- Resolve 21, p. 1265 — reajuste (*Retime Process*): *Nearest* (repite/salta cuadros, menos sofisticado), *Frame Blend* (disuelve cuadros duplicados), *Optical Flow* (genera cuadros nuevos, más calidad, falla en cruces/movimiento impredecible).
- Libro de Estilo CSRTV, 9.9/9.9.2 — tramar/cubrir rostro de menores, víctimas, testigos protegidos y FCSE con riesgo; no ocultar identidad; ralentización/congelado no para acentuar morbo.
- Libro de Estilo CSRTV, 3.2.2 y 9.9.1 — rótulo «reconstrucción» y «archivo» durante todo el tiempo en pantalla en esos casos.

## 4. Grafismo

- Oficio — grafismo de casa lo diseña el área de grafismo; el montador inserta, rellena plantillas, hace rótulos sencillos en el sistema de edición.
- Resolve 21, cap. 56, p. 1213 — títulos: duración por defecto del clip, 5 segundos (ajustable).
- Resolve 21, cap. 56, p. 1215 — generadores: *Lower 3rd* (L/M/R), *Scroll* (créditos), *Text*, *Text+*, *Fusion Titles*.
- Resolve 21, cap. 56, p. 1215 — zonas de seguridad: acción (movimiento importante) y título (texto); valores por defecto 93 % acción / 90 % título; anacrónicas para pantalla plana pero útiles en móviles/redes.
- Oficio — sin rótulo fuera de zona de título; sin logo que tape la cara del entrevistado.
- Oficio — canal alfa: JPG nunca lo lleva (3 canales, con pérdidas); PNG, TIF y TGA sí (32 bits con alfa = 8+8+8+8).
- UIT-R BT.2408-9, § 2.1 — «Graphics White» = mismo nivel que HDR Reference White: 75 % en HLG, 58 % en PQ, 203 cd/m².
- UIT-R BT.2408-9, § 9 — grafismo SDR mapeado a «Graphics White» para no deslumbrar; *display-light* si se conserva color corporativo, *scene-light* si se iguala con la escena.
- Libro de Estilo CSRTV, 3.16 — máximo 4-5 elementos por gráfico, presencia mínima 8 segundos; «cama» de audio salvo respetar sonido de grabación; el rótulo es información (brevedad, impacto, síntesis, 3.6.1).

## 5. Subtítulos

- Guía Univ. Burgos (síntesis UNE 153010) — abierto: incrustado en el vídeo, sin control del espectador; cerrado: se añade/quita a voluntad; cerrado más accesible.
- Oficio — abierto: total en otro idioma/sonido ininteligible en pieza informativa; cerrado: accesibilidad de emisión/plataformas, no lo hace normalmente el montador.
- Resolve 21, cap. 187, p. 4205 — salidas de entrega: fichero aparte (IMSC1, DFXP, SRT, WebVTT), incrustado (*Burn into video*), embebido (CEA-608 en MXF OP1A/QuickTime); CEA-708 y Línea 21 no soportados por Decklink/UltraStudio.
- Guía Univ. Burgos, p. 4 — centrados abajo, 2 líneas (excepcional 3); máximo 37 caracteres por línea; sin partir sílabas; personaje nuevo, línea nueva.
- Guía Univ. Burgos, p. 4-6 — velocidad recomendada, 15 caracteres/segundo; sincronía con labios/planos/locución; 1 línea ≈ 3 s, 2 líneas máximo 6 s; en pantalla mínimo 1 s, máximo 6 s.
- Guía Univ. Burgos, p. 4-6 — pausas con comas/puntos; tipografía legible; información contextual entre paréntesis (p. 4 minúscula, p. 6 mayúscula: guía incoherente).
- Guía Univ. Burgos, p. 5 — mayúsculas sólo título/texto en mayúscula del original; cursiva para voces de aparato o fuera de cuadro, títulos, canciones, otro idioma.
- Guía Univ. Burgos, p. 5 — números en letra del 0 al 10, cifra el resto; mejor paréntesis que corchetes.
- Guía Univ. Burgos, p. 5 — orden de legibilidad de color: amarillo/negro, verde/negro, cian/negro, magenta/negro, blanco/negro, rojo/blanco, azul/blanco, azul/amarillo; mismo orden para identificar personajes por importancia.
- Guía Univ. Burgos, pp. 6-7 — identificar personaje: color, etiqueta, guion (guion sólo si hay riesgo de confusión).
- Oficio — subtítulo que cruza un corte de plano se parte en el corte si se puede.

## 6. Transiciones

- Ayuda Premiere («Transitions overview», 07-01-2026) — corte por defecto: último cuadro de un clip seguido del primero del siguiente; transición: efecto que crea enlace animado.
- Resolve 21, cap. 55, p. 1194 — transición indica cambio de tiempo o de lugar.
- Oficio — cortinilla casi nunca en noticia; fundido encadenado para paso de tiempo o suavizar salto.
- Resolve 21, cap. 55, p. 1198 — seis estilos de fundido: *Video* (lineal), *Film* (logarítmico, tipo copiadora óptica), y cuatro con modos de fusión (aditivo se aclara a mitad, sustractivo se oscurece a mitad, altas luces, sombras).
- Oficio — colas (*handles*): cuadros del material fuera del montaje, necesarios para la transición.
- Resolve 21, cap. 55, p. 1196-1197 — sin colas suficientes: duración estándar 1 s o lo que permitan las colas; con atajo, pregunta: *Trim Clips*, *Skip Clips*, *Cancel*.
- Ayuda Premiere — recortar antes de aplicar transición; recortar al menos 15 cuadros por lado para una de 1 s centrada.
- Cálculo propio — a 25 im/s, transición centrada de 1 s pide 12-13 cuadros por lado; de 2 s, 25.
- Resolve 21, cap. 55, p. 1195/1198 — duración de entrada: ¼ s, ½ s, 1 s, 2 s; alineación: *Start on Edit*, *Center on Edit*, *End on Edit*; suavizado (*Ease*).
- Resolve 21, p. 1199 — transición estándar configurable con clic derecho, «Set as Standard Transition».

## 7. Limpieza de audio

- Oficio — limpiar: quitar lo que sobra sin tocar lo que sirve; regla previa: lo que no se graba no se limpia.
- Oficio — tabla defecto/herramienta: ruido de fondo → reducción por perfil; zumbido → filtros de ranura/reductor; chasquidos → reductor/edición; recorte → reconstrucción (si es grave, sin arreglo); oclusivas → paso alto/reductor; sibilantes → *de-esser*; viento/roces → paso alto/reductores; reverberación → reductor con límites.
- Resolve 21, cap. 181 — *Noise Reduction* (De-Hiss/De-Rumble); *De-Hummer* (zumbido, armónico desde el doble de la fundamental); *De-Esser* (sibilancia 5-8 kHz); *Dialogue Leveler* (sube/baja diálogo, atenúa fondo); *Voice Isolation* (IA, sólo Studio, 70-80 recomendado); *Ducker*.
- REBT, RD 842/2002, art. 4.4 — frecuencia de red en España, 50 Hz (zumbido y armónicos: 100, 150, 200 Hz…).
- Oficio — ecualización: campana (banda concreta), estantería (todo un extremo), filtro de corte (elimina banda); voz que compite con música: se le hace sitio, no se sube.
- Oficio/Rane — filtros: paso alto (graves), paso bajo (agudos), paso banda (efecto teléfono), *notch*/ranura (tono concreto, ej. zumbido de red).
- Rane (RaneNotes) — cada orden de filtro suma 6 dB/octava (1.º 6, 2.º 12, 3.º 18, 4.º 24 dB/octava = 80 dB/década); frecuencia de corte a −3 dB.
- iZotope RX 11 — reducción por perfil: seleccionar tramo sólo de ruido, aprender perfil (manual = ruido fijo, adaptativo = ruido cambiante), ajustar umbral y reducción tonal/aleatoria; suavizar, no forzar.
- Resolve 21, cap. 181, p. 4122 — umbral ligado al SNR; sensibilidad alta exagera el perfil y puede afectar al diálogo; casilla «Listen to Noise Only».
- iZotope/oficio — artefactos: exceso de sustracción espectral = sonido «gorjeo»/«agua»; exceso de puerta = ráfagas de ruido tras la señal; corregir en varias pasadas suaves.
- Oficio/Rane — *ducking*: pista de control baja otra por *side-chain*; *attack*, *hold*, profundidad (0 a −80 dB); uso típico, música bajo voz en off.
- Resolve 21, cap. 181, p. 4094 — *ducking* sin comprimir la señal; distinto del *Dialogue Leveler* (iguala la voz consigo misma). Libro de Estilo, 9.2.12.4: música, aditamento impropio en informativos diarios; con matices en formatos extensos.
- Oficio — orden de limpieza de diálogo: edición de golpes/ruidos, paso alto, zumbido, reducción por perfil suave, sibilantes/oclusivas, ecualización y compresión de mezcla; relleno de ambiente en los cortes.
- EBU R 128-2023 (v5) — nivel objetivo −23,0 LUFS (±1 LU si no es viable, ej. directo); tolerancia de medida ±0,2 LU; pico verdadero máximo −1 dBTP; medidor conforme UIT-R BS.1770/EBU Tech 3341; LRA no recomendado por debajo de 1 minuto; se mide el programa entero, incluida publicidad.
- EBU Tech 3343-2023 (v4) — en postproducción, tolerancia ±0,2 LU en torno a −23 LUFS; corrección por ganancia estática fija para todo el programa.
- Cálculo propio — cambio de ganancia de X dB mueve LUFS y pico verdadero X; si al subir el pico supera −1 dBTP, limitar antes y remedir (limitar baja algo la integrada).
