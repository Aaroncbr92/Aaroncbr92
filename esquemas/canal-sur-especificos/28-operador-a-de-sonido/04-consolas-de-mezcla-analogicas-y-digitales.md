# Tema 4 del específico de Operador/a de Sonido · Consolas de mezcla analógicas y digitales

**Siglas**: RTVA, CSRTV, EBU/UER, dB, dBu, dBFS, PFL, AFL, SIP, DIM, HPF, EQ, VCA, DCA, LCR, FOH, DAW, I/O.

Esqueleto para repasar, no resumen: reduce a lo justo para reconstruir el tema en la cabeza, no sustituye leerlo.

<!-- indice -->
<!-- /indice -->

## Consolas de mezcla analógicas y digitales

- Oficio: 5 funciones de una mesa — amplificar/adaptar, procesar, mezclar, encaminar, monitorizar.
- Oficio: bloques en orden de señal — previo, EQ/filtros, dinámica, envíos/retornos, buses/subgrupos, matriz, escucha.
- Oficio: analógica = camino físico por canal, un mando por función; digital = números, memoria de escena, mando por capas.
- Oficio: digital gana en recuperar config. en segundos; analógica, en que lo que se ve es lo que hay.
- Oficio: control de varios canales — analógico con VCA, digital con DCA; memoria de escena sólo en digital (en directo, equivale a la automatización).
- Oficio: digital puede llevar previos lejos, en cajas I/O por red, compartidas entre consolas.
- Oficio: mesa de DIRECTO — maniobra inmediata y fiabilidad; mesa de POSTPRODUCCIÓN — automatización y nº de pistas, mezcla en DAW.
- Oficio: mesa digital con señal a otra frecuencia de muestreo → convertidor de frecuencia de muestreo (no vale entrada analógica ni atenuador de paso).
- Oficio: instalación digital = UNA referencia de reloj; dentro de casa se sincroniza, no se convierte.

## Niveles

- Oficio: a la mesa llegan 3 clases de señal — micrófono (mV, previo con mucha ganancia), línea, digital.
- Yamaha (CL): DIGITAL GAIN del canal, distinta de la ganancia analógica del previo (caja I/O o consola); la del previo fija la relación señal/ruido.
- Oficio: PFL — escucha ANTES del fader, se oye aunque esté a cero.
- Soundcraft/Yamaha (CL): AFL — escucha DESPUÉS del fader (con Aux Masters); punto exacto: PFL antes del fader, AFL después, o POST PAN.
- Soundcraft: SIP — escucha un canal solo, silenciando automáticamente las demás entradas; útil para mezcla final, no para ajustar ganancia (a eso, el PFL).
- Oficio: SIP pulsado por error en mesa al aire silencia el programa.
- Soundcraft: ganancia de entrada = ajustar la señal al nivel que entiende la mesa, lo más alta posible dejando margen (headroom).
- Soundcraft: procedimiento — pulsar PFL, ajustar ganancia hasta zona amarilla del medidor, soltar, repetir por entrada; la EQ afecta a la ganancia ya ajustada.
- Oficio: ganancia se ajusta con la fuente a su nivel real, no con prueba floja (satura en directo).
- Soundcraft: faders de entrada cerca de «0» para mayor control (escala logarítmica); masters también a «0»; fader muy bajo indica ganancia de previo demasiado alta.
- Cálculo: dB de la cadena se suman — ganancia −3 dB + fader x = 1 dB en bus → x = +4 dB; previo +40 + EQ +3 − fader 5 = +38 dB total.
- EBU R 68-2000: nivel de alineación 18 dB bajo el máximo de codificación digital, sea cual sea el nº de bits (ratio 1:8, 18,06 dB); único método fiable, referido al máximo de códigos.
- EBU Tech 3343 (§8.1): señal de alineación = senoide de 1 kHz a −18 dBFS.
- Oficio: la R 68 no da la equivalencia de −18 dBFS en dBu analógicos; no se atribuye a la EBU.
- Yamaha (CL): oscilador propio (senoide o ruido rosa) para alinear con el equipo siguiente o probar la sala.

## Entradas

- Yamaha (CL): canal de entrada recibe de I/O, panel trasero o slots, manda a bus STEREO, MONO, MIX o MATRIX; 2 clases — MONO y STEREO.
- Yamaha (CL): cadena en orden — 1 INPUT PATCH (asigna entrada física a canal); 2 Ø/phase (invierte polaridad, no retrasa); 3 DIGITAL GAIN.
- Yamaha (CL): 4 HPF (corta bajo frecuencia fijada); 5 4-band EQ paramétrica (HIGH, HIGH MID, LOW MID, LOW).
- Yamaha (CL): 6 DYNAMICS 1 (puerta/ducking o expansor/compresor); 7 DYNAMICS 2 (compresor, compansor o de-esser).
- Yamaha (CL): 8 INPUT DELAY (hasta 1.000 ms); 9 LEVEL/DCA 1-16 (nivel y asignación a DCA); 10 ON/OFF (abre o silencia el canal).
- Oficio: en digital no hay cable por canal; el patch se guarda con la escena.
- Oficio: «Ø» es polaridad, no fase; el retardo de entrada corrige desfase por distancia. HPF va antes de EQ/dinámica para no disparar el compresor con graves.
- Oficio: en analógica, mismo canal esencial pero cada bloque es un circuito propio, orden fijado por el fabricante.
- Soundcraft/Yamaha (CL): inserción = corte para intercalar equipo externo, vuelve al canal (PRE EQ, PRE FADER o POST ON).
- Soundcraft/Yamaha (CL): salida directa = salida de línea de un canal, no vuelve, sin pasar por suma (PRE HPF, PRE EQ, PRE FADER o POST ON); se usa para grabar multipista limpio.
- Oficio: 2 consolas pueden compartir previos por red; la ganancia analógica es una sola.
- Yamaha (CL): compensación de ganancia — la caja I/O mantiene constante el nivel a la red aunque cambie la ganancia analógica; cada consola ajusta con su ganancia digital.

## Salidas

- Yamaha (CL): sección de salida recoge lo mandado a buses, lo ecualiza/comprime y lo manda a toma o a otro bus.
- Yamaha (CL): canal MIX — a puerto, MATRIX, STEREO o MONO(C); STEREO/MONO(C) — salida principal (en LCR, los 3 juntos); MATRIX — recibe entradas, MIX y STEREO/MONO, sólo sale a puertos.
- Oficio: MIX puede ir a salida o a otro bus (así funciona un subgrupo); en analógica, salidas = masters sin proceso propio salvo inserción.
- Yamaha (CL): modo ST/MONO — canal manda a estéreo (con panorama) y a mono por separado; modo LCR — a 3 buses a la vez, panorama + mando CSR reparte I/C/D, sirve para sonorizar con 3 grupos de altavoces.
- Oficio: 3 reglas de estéreo real — 2 canales distintos (no iguales); no más de 2 (si no, multicanal); cada fuente con posición en panorama.
- Oficio: escucha de control es una salida más, no va al programa; DIM atenúa el volumen de monitores una cantidad preestablecida, sin tocar el programa; al soltar, vuelve al mismo nivel (MUTE sí quita del programa).
- Oficio: 4 mandos que se confunden — DIM (atenúa escucha), ganancia de entrada (previo), Solo (sólo ese canal), Mute (silencia).
- Yamaha (CL): talkback manda la señal del micro de órdenes al bus elegido, nunca al programa; con talkback activo, su atenuador baja monitores salvo la señal de órdenes.
- Oficio: la consola lleva también el oscilador (senoide/ruido rosa) de «Niveles».

## Buses

- Soundcraft: bus = conjunto de conductores por los que viajan señales (estéreo, grupos, PFL, aux…); camino común donde varios canales SUMAN su señal.
- Oficio: en analógica el bus es un conductor físico; en digital, una suma del procesador (misma lógica).
- Yamaha (CL): 4 familias — STEREO/MONO (mezcla principal), MIX (aux o subgrupos según configuración), MATRIX (mezclas de mezclas); más el bus de órdenes (talkback).
- Oficio: distinguir bus que suma (subgrupo) de mando que sólo gobierna nivel sin sumar (VCA/DCA); sólo el primero es bus.

## Auxiliares

- Oficio: auxiliar = bus que cada canal alimenta con mando propio aparte del fader; mezcla distinta con las mismas fuentes.
- Soundcraft: EFFECTS SEND = salida aux POST-fader para efectos; FOLDBACK SEND = salida aux PRE-fader para monitor de intérpretes.
- Soundcraft: pre-fader independiente del fader (se oye el efecto con fader al fondo); para efectos usar POST (sigue proporcional al nivel); para monitores, PRE (si no, foldback cambia con cada movimiento del FOH, riesgo de acople).
- Yamaha (*Get on the Bus*): pre-fader independiente (monitores, envíos de grabación); post-fader (reverb/delay, subgraves alimentados por aux).
- Yamaha (CL): botón PRE/POST por canal; PRE EQ o PRE FADER fijado por bus MIX/MATRIX en BUS SETUP.
- Soundcraft: Effects Return Aux Post Control al mínimo o se produce realimentación.
- Yamaha (CL): bus MIX puede ser FIXED (nivel fijo, como subgrupo) o VARI (variable, como aux); MATRIX siempre VARI. Modo SENDS ON FADER pasa envíos de un bus a los faders.
- Yamaha (CL): Mix Minus quita un canal concreto de lo mandado a MIX/MATRIX, para monitorado de esa persona; a mano, con un aux (todas las fuentes menos la de quien escucha).

## Grupos

- Soundcraft/Yamaha (*Get on the Bus*): subgrupo = canales mezclados antes del bus principal, controlables con un fader, con EQ/compresión de conjunto; es salida adicional.
- Yamaha (*Get on the Bus*): VCA controla nivel de varios canales sin afectar su balance, no pasa audio, no suma; VCA analógico (tensión), DCA digital (señales de control), función similar en la práctica.
- Yamaha (CL): 16 grupos DCA; un fader DCA controla el nivel de sus canales manteniendo diferencias entre ellos; desde v3.0 agrupa también salidas; se guardan en la escena.
- Oficio: subgrupo suma, admite proceso de conjunto, es salida propia; DCA no suma, sin proceso ni salida propia; con subgrupo, envíos posteriores de cada canal no se mueven al bajarlo, con DCA sí.
- Soundcraft/Yamaha (CL): MUTE GROUPS combinan el on/off de varios canales en un control; 8 grupos, válidos para entrada y salida, un canal en varios.
- Oficio: caso tertulia — equilibrar en faders, DCA para el conjunto, subgrupo si se comprime junto, grupo de silencio para cerrar a la vez.

## Matrices

- Yamaha (*Get on the Bus*/CL): buses de matriz combinan varias entradas (también canales MIX y STEREO/MONO) en proporciones distintas hacia varios destinos.
- Oficio: matriz de salida decide qué mezcla va a qué destino — emisión, grabación, sala, retornos; una misma mezcla se reparte a varios, cada uno con su nivel.
- Soundcraft: consola de sala necesita muchas salidas de matriz para varios clusters de altavoces.
- Oficio: matriz de mezcla SUMA señales y saca una mezcla nueva; matriz de conmutación NO mezcla, sólo encamina la entrada elegida intacta (así, el patch de entradas de una digital).

## Automatización

- Oficio: automatización graba movimientos de mandos y los reproduce en el tiempo del programa; propia de postproducción sobre material grabado (en directo, la escena).
- Avid (Pro Tools): Off — automatización ignorada en reproducción; Read — reproduce lo escrito, no escribe.
- Avid: Write — escribe todo el pase, borrando lo previo, se toque o no el mando.
- Avid: Touch — escribe sólo al tocar, al soltar vuelve a lo escrito; Latch — igual pero al soltar sigue escribiendo hasta parar; útil en mandos giratorios sin retorno (pan, plugins).
- Avid: Touch/Latch — Volumen en Touch, resto en Latch (sólo Ultimate/Studio).
- Avid: Trim — ajusta automatización existente con valores relativos, no absolutos; combinable con los demás modos; no aplica a pan, mute ni plugins.
- Oficio: caso — pasaje 2 dB alto con bajadas ya automatizadas → Latch Trim o Write Trim, no Touch Trim (perdería el ajuste al soltar).

## Escenas

- Yamaha (CL): escena = nombre asignado a parámetros de mezcla y patch I/O, guardado y recuperable; numeradas 000-300, 000 sólo lectura (inicializa), 001-300 escribibles.
- Yamaha (CL): guarda faders y teclas ON, patch I/O, buses, ganancia de previos, EQ, dinámica, rack, panorama, inserción/salida directa, envíos MIX/MATRIX, DCA y silencio, enlaces de canal; faders motorizados se mueven solos al recuperar.
- Yamaha (CL): Recall Safe excluye parámetros/canales (DCA) de la recuperación, global a todas las escenas; salvedad — Channel Link y ajustes de bus se reproducen siempre.
- Yamaha (CL): Focus especifica, escena a escena, qué parámetros SÍ se actualizan al recuperar.
- Yamaha (CL): Fade cambia suavemente, en tiempo fijado, los faders de canales/DCA elegidos al recuperar; ajuste independiente por escena.
- Oficio: en directo, escena por bloque; proteger con Recall Safe lo ajustado en vivo; guardar tras ensayos; comprobar que el patch no cambió una salida en el aire; la escena guarda también DCA/silencio/ganancia de previos, riesgo con previo compartido.
