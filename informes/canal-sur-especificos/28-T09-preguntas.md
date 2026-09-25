# Puesto 28 · Operador/a de Sonido · Tema 9 · Fase 4, preguntas de comprobación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/09-grabacion-edicion-y-postproduccion.md`.
Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Quince preguntas tipo test de
cuatro opciones, de teoría y de aplicación práctica, contestadas **sólo con el tema**. La respuesta
correcta es la que da la fuente o el cálculo; la última columna dice si el tema basta para darla.

| # | Rúbrica | Tipo | Pregunta | Correcta | ¿La contesta el tema? |
|---|---|---|---|---|---|
| 1 | Grabación | Práctica | Un minuto de estéreo PCM a 48 kHz y 24 bits ocupa aproximadamente: a) 10,6 MB b) 17,3 MB c) 34,6 MB d) 5,8 MB | b) | Entera: «La cuenta del tamaño», tabla de un minuto (288.000 B/s × 60 = 17.280.000 B) |
| 2 | Grabación | Teoría | Es un códec sin pérdida: a) AAC b) Opus c) FLAC d) AC-3 | c) | Entera: «Con pérdida y sin pérdida» |
| 3 | Músicas | Teoría | Según el documento AES TD1008, si es operativamente viable, la música se normaliza respecto de la voz: a) a la misma sonoridad b) 2 o 3 LU más alta c) 2 o 3 LU más baja d) 6 LU más alta | b) | Entera: «La música bajo la voz» (con el motivo: la voz se percibe 2-3 dB más fuerte) |
| 4 | Cuñas y ráfagas | Teoría | Para la EBU R 128 s1, el contenido corto (*short-form content*) es un programa: a) de hasta un minuto b) de hasta unos 2 minutos, típicamente de menos de 30 segundos c) de hasta 5 minutos d) de menos de 10 segundos | b) | Entera: «Por qué hay una norma para las piezas cortas» (definición literal) |
| 5 | Cuñas y ráfagas | Práctica | Una cuña mide −23,1 LUFS integrada, −1,5 dBTP y −15,5 LUFS de máxima a corto plazo. Lo correcto es: a) bajarla entera 2,5 dB b) aceptarla, integrada y pico cumplen c) reducir la dinámica del pasaje fuerte y volver a medir d) subirla 0,1 dB | c) | Entera: «Un caso práctico: la cuña que no pasa» (y por qué a) saca la integrada de tolerancia) |
| 6 | Continuidad | Teoría | Según la EBU Tech 3343, cuando el sistema de emisión reproduce contenido conforme, el procesador de sonoridad de la salida debe: a) comprimir más b) pasar a *bypass* o a un ajuste que sólo limite el pico verdadero c) normalizar a −18 LUFS d) cortar la señal | b) | Entera: «La continuidad: que todo suene igual» (§ 2.4, con la señalización por GPIO) |
| 7 | DAW | Práctica | Latencia de una memoria intermedia de 512 muestras a 48 kHz: a) 1,33 ms b) 5,33 ms c) 10,67 ms d) 11,6 ms | c) | Entera: «La latencia de una estación de trabajo» (fórmula y valores a 48 kHz; 11,6 es a 44,1) |
| 8 | DAW | Teoría | Una EDL NO lleva: a) los códigos de tiempo de entrada y salida b) la fuente de cada corte c) los niveles de audio d) el tipo de transición | c) | Entera: «La lista de decisiones de edición» |
| 9 | Pistas | Teoría | En una DAW, la pista auxiliar (*aux*) se usa para: a) grabar la voz b) recibir un envío o un bus, como retorno de efectos o submezcla c) guardar el código de tiempo d) exportar el máster | b) | A medias: el tema habla de buses, envíos y submezclas por capa («DAW», «Una fuente, una pista»), pero no de los tipos de pista de una DAW (audio, auxiliar, VCA, máster) |
| 10 | Sincronía | Práctica | A 25 fps, la duración entre 00:47:17:23 y 01:23:54:00 (no inclusiva) es: a) 00:36:36:02 b) 00:36:37:02 c) 00:36:36:23 d) 00:37:36:02 | a) | Entera: «La aritmética del código de tiempo» |
| 11 | Sincronía | Práctica | Un BWF grabado a 48 kHz que empieza a las 10:00:00 lleva en TimeReference: a) 36.000 b) 360.000 c) 172.800.000 d) 1.728.000.000 | d) | Entera: «La marca de tiempo del BWF» |
| 12 | Doblaje | Teoría | La pista internacional de un documental: a) lleva la voz en off y no los totales b) lleva música, ambientes y los totales en su idioma original, sin la voz en off c) es sólo la música d) es la mezcla completa doblada | b) | Entera: «Doblaje a otro idioma» y «Las capas de la banda sonora» |
| 13 | Limpieza | Teoría | Según el manual de iZotope RX 11, un perfil de ruido aprendido a mano es el más adecuado para: a) ruido constante y continuo b) tráfico y olas c) chasquidos d) recorte | a) | Entera: «La reducción de ruido por perfil» (el modo adaptativo, para el ruido que cambia) |
| 14 | Mezcla | Práctica | Un programa mide −24,5 LUFS y −1,8 dBTP. Para subirlo 1,5 dB sin pasar de −1,0 dBTP, el limitador debe rebajar los picos, como mínimo: a) 0,3 dB b) 0,5 dB c) 0,7 dB d) 1,5 dB | c) | No: el tema dice «al menos 0,5 dB (de −1,8 a −2,3 dBTP)», que tras subir 1,5 dB deja −0,8 dBTP; el mínimo es 0,7 dB (−2,5 + 1,5 = −1,0). Quien estudie el tema marca b) |
| 15 | Entrega | Práctica | Al reducir un máster de 24 a 16 bits para entregarlo, antes de truncar se aplica: a) *dither* b) un compresor c) un filtro paso alto d) *drop frame* | a) | No: el tema no trata la reducción de resolución (*dither*) ni la conversión de frecuencia de muestreo en la entrega |

Resultado: 12 enteras, 1 a medias (9), 2 no (14 por error del tema; 15 por laguna).
