# Tema 5 del específico de Operador/a de Sonido · Procesamiento de audio

**Siglas**: RTVA, CSRTV, UER/EBU, UIT, ISO, dB, dBu, dBFS, dBTP, dB SPL, PML, PCM, MPEG, AGC, VCA, FET, BPM, RT60.

Esqueleto para repasar, no resumen: cada línea manda a su dato en el tema; hay que releer el tema, no fiarse de esto.

<!-- indice -->
<!-- /indice -->

## Ecualización

- Ecualizador: cambia el reparto por frecuencias; cambia el timbre (tema 1).
- 3 formas (oficio): campana/peaking (franja alrededor de una frecuencia); estantería/shelving (todo por encima/debajo); filtro de corte (elimina).
- 3 tipos: gráfico (sólo ganancia, bandas fijas); paramétrico (frecuencia+ganancia+ancho; canales de mesa/estaciones); semiparamétrico (frecuencia+ganancia).
- «Multibanda» NO es tipo de ecualizador: adjetivo de los COMPRESORES.
- Rane: gráfico realce/corte, «10 to 31 bands, octave to 1/3-octave spacing»; 15 bandas a 2/3 octava y 30 a 1/3, centros en posiciones ISO.
- Q = frecuencia central ÷ ancho de banda. Fórmula: Q=√(2ᴺ)÷(2ᴺ−1) para N octavas (ancho a −3 dB).
- Tabla Q: 0,7→2 oct (carácter); 1,41→1 oct (corriente); 2,9→1/2 oct; 4,3→1/3 oct (gráfico de tercio); >10→quirúrgico/notch.
- Ejemplo: campana 1.000 Hz, Q=1,414 → ancho ≈707-1.414 Hz. Q se ajusta en el PARAMÉTRICO, no en el gráfico (fijo).
- Práctica (oficio): Q ancho+poca ganancia=carácter; Q estrecho=quitar problema; corregir en captación antes de ecualizar; ecualizador desfasa (tema 1); ondas estacionarias no se ecualizan (tema 1).

## Dinámica

- Dinámica = distancia entre pasajes fuertes y débiles (tema 1).
- Procesador de dinámica: cambia ganancia según nivel propio.
- Rane: estructura común = elemento de control de ganancia en camino principal + cadena lateral (detector + calculador de ganancia); cadena lateral mira entrada o clave externa (key input).
- Rane: compresor, limitador, AGC, de-esser, ducker y puerta = mismo aparato, distinto detector/cálculo/elemento de control. Analogía: limitador de pico es al compresor lo que la puerta de ruido es al expansor.
- Compresor: reduce lo que pasa del umbral. Limitador: techo, no deja pasar. Expansor: aumenta lo que queda bajo umbral. Puerta: corta casi al silencio lo que queda bajo umbral.
- Headroom = diferencia entre nominal y saturación.
- Analógico (tema 2, Rane): +4 dBu nominal / +26 dBu máximo = 22 dB. Digital: techo fijo 0 dBFS, por encima recorta; niveles digitales negativos.
- EBU R 68: alineación 18 dB bajo el máximo, «irrespective of the total number of bits»; nota 2: ratio 1:8 (18,06 dB). Tech 3343 §8.1: tono de alineación = senoide 1 kHz a −18 dBFS.
- R 68: alineación 9 dB (u 8 en algunas organizaciones) bajo el PML; picos reales hasta 3 dB sobre lo indicado, con error de operador hasta 6 dB → 15 dB sobre alineación (9+6), caben bajo 18 dB de reserva.
- Tech 3343 §8.1: con Maximum Permitted True-Peak Level (−1 dBTP en producción) el PML de −9 dBFS (ITU-R BS.645) queda obsoleto; la alineación −18 dBFS NO cambia con la sonoridad. Analógico: pasarse distorsiona progresivo; digital: RECORTA.
- Headroom ≠ masterización (fase de producción) ≠ dB SPL (aire) ≠ rango dinámico (ruido de fondo a saturación; headroom mide desde nominal hacia arriba).

## Compresión

- Compresor: reduce diferencia fuerte/flojo, sólo por encima del umbral. Mandos: umbral, relación (4:1 = 4 dB entrada→1 dB salida), ataque (tarda en reducir), relajación (tarda en soltar), codo (hard/soft knee), make-up (recupera ganancia).
- Rane: umbral ajustable −40 dBu a +20 dBu; ataque 25-500 ms (expansores/puertas 0-250 ms); relajación 25 ms-2 s. «No industry standard» para relajación: Rane la define como tiempo en cambiar 10 dB, no el que tarda en volver a ganancia unidad. Fórmula: (Reducción × Ajuste) ÷ 10 dB. Ejemplo: mando 1 s, reducción 5 dB → 0,5 s real.
- Ejemplo: umbral −20 dBFS, relación 4:1, pico a −8 dBFS (supera 12 dB) → sale a −17 dBFS (reducción 9 dB). Con 2:1: sale a −14 dBFS. Relación muy alta ≈ limitador.
- Make-up: final de la cadena interna, tras la reducción, no es el codo; recupera lo que la compresión bajó, y «más fuerte» lo da él, no la compresión.
- 4 tecnologías (oficio, Rane sólo confirma predominio de VCA en analógico): VCA (rápido/preciso, limpio); óptico (lento, relajación en 2 tiempos, musical en voz); Vari-Mu (lento, denso/pegado); FET (muy rápido, agresivo). Clase A: clase de amplificador, NO tecnología de compresión.
- Compresor multibanda: parte espectro en bandas, comprime cada una (masterización). De-esser: compresor cuya cadena lateral sólo «escucha» sibilantes.
- Rane, voz («starting points»): ataque 25-100 ms, relajación 100-500 ms, relación 2:1 a 4:1, codo blando.
- Práctica (oficio): voz radio/informativos, relación 2:1-4:1, poca reducción; ajustar mirando el medidor y escuchando; comprimir no es subir (lo hace el make-up); sonoridad la mide el medidor de sonoridad (tema 13).

## Limitación

- Limitador = compresor que atenúa sólo lo que supera el umbral, deja pasar inalterado lo inferior. Relación muy alta (10:1 o mayor, límite infinita), ataque muy rápido.
- Rane: limitador usa detector de pico + relación fija infinito:1 (compresor usa detector rms típicamente).
- Rane, usos: evitar recorte/distorsión en etapas de potencia; proteger altavoces; evitar overs en grabación; evitar sobremodulación en emisión; cerrar masterización (subir nivel medio sin pasar 0 dBFS). Captación: limitador de grabador/cámara = red de seguridad, no sustituto del ajuste de nivel.
- EBU R 128: pico verdadero máximo de programa NO debe superar −1 dBTP en producción (audio lineal); salvedad: PML puede ser menor según sistema de distribución/tasa de reducción de datos.
- Tech 3343: basta 1 dB de headroom bajo 0 dBFS (bajo-lectura ~0,5 dB, medidor 4x oversampling, 48 kHz); para MPEG-1 Layer 2 y Dolby AC-3, límite recomendado −2 dBTP.
- R 128: pico verdadero máximo = valor máximo de la forma de onda en tiempo continuo (puede caer entre muestras). Por eso el limitador de salida se ajusta en dBTP, no en dBFS de muestra. Medida de pico verdadero y sonoridad: tema 13.

## Puertas

- Expansor: complemento del compresor, «running in reverse»; reduce ganancia bajo umbral (expansión hacia abajo); uso más común = reducción de ruido (Rane). Ejemplo Rane: umbral justo bajo el pasaje más flojo de voz, relación 2:1: escalón de −10 dB a la salida es −20 dB → mejora de 10 dB.
- Puerta: caso extremo del expansor, como el limitador lo es del compresor (Rane). Relación fija infinito:1, detector de pico, profundidad variable; bajo umbral reduce ganancia a «cero» (~80 dB); «abre» y «cierra».
- Expansor reduce progresivo (según relación) con detector rms; puerta reduce todo/nada con detector de pico.
- Mandos puerta (Rane): umbral (empieza el ajuste; en expansores hasta −60 dBu); ataque (0 ms «instantáneo» a 250 ms); hold (0 a 3 s); liberación (sin margen dado); profundidad/depth (0 a −80 dB); casi todas dan ecualización de cadena lateral y clave externa; las mejores «look-ahead» + pre-ramping. Histéresis: umbral de cierre más bajo que el de apertura; oficio, sin fuente leída.
- Rane, usos: reducir diafonía de micrófonos vecinos, evitar resonancia de toms, apretar percusión, controlar ruido de micros abiertos. Expansor en directo: bajar ruido de escenario entre pasajes de un vocalista tranquilo.
- Tertulia (oficio): puerta/expansor en cada canal baja micros de quien no habla → menos ruido de sala, menos captación cruzada, menos filtro en peine (tema 1).
- Defectos (Rane): respiración/breathing (ruido de fondo sube/baja audible); chasquido/clicking (ataque rápido = clic más agudo; mito: abrir más rápido NO suena mejor). Frases cortadas (oficio): umbral alto o mantenimiento/liberación cortos.
- Ducker: al revés que la puerta, atenúa la señal cuando la de CONTROL supera el umbral (Rane); ataque, hold y profundidad (0 a −80 dB), lógica invertida. Usos Rane: megafonía/paging (aviso baja la música); talkover (pinchadiscos). Radio/TV (oficio): música bajo la voz vía clave externa = ducking.

## Filtros

- Filtro: deja pasar una zona y atenúa el resto. 4 de uso diario (oficio): paso alto (retumbar, golpes de pie de micro, viento, proximidad); paso bajo (siseo, ruido agudo); paso banda (efecto «teléfono»); notch/banda eliminada (tono concreto: zumbido, acoplamiento).
- 2 datos del filtro de corte: frecuencia (caída de 3 dB) y pendiente (dB/octava, la fija el orden). Rane: cada orden suma 6 dB/octava (20 dB/década). 1er orden 6; 2º 12; 3º 18; 4º orden: 24 dB/octava (4×6) o 80 dB/década.
- Filtro de corte ≠ estantería: el de corte atenúa cada vez más lejos del corte; la estantería baja igual todo el extremo. Rumble: ruido de baja frecuencia de giradiscos.
- Práctica (oficio): paso alto en casi todos los canales de entrada, primer proceso en voz (evita trabajar al compresor de más).
- Notch: se usa idealmente para evitar acople con megafonía. Q altísimo, franja muy estrecha, no toca lo de al lado.
- Por qué sirve: realimentación se dispara a UNA frecuencia (ganancia del lazo llega a 1 primero); quitando 2-3 dB ahí el lazo deja de oscilar; con campana ancha habría que quitar mucho más y se oiría.
- Notch NO sirve para: diafonía entre canales (aislamiento eléctrico/cableado, no frecuencia); banda de medias de un bombo (pide filtro ancho); pes de voz (antipop o paso alto, no frecuencia estrecha). Acoplamiento y ganancia disponible: tema 10.
- Reducción de ruido, 5 familias (oficio): doble extremo/companding (comprime al grabar, expande al reproducir; cinta analógica); puerta de ruido (directo/multipista); expansor (progresivo); reducción espectral (perfil de ruido, resta banda a banda; postproducción); filtro de corte (el primero a probar). Mejor reducción de ruido = no grabarlo (micrófono bien elegido, tema 3).

## Reverberación

- Reverberación de sala: cola de reflexiones tras el sonido directo, se mide con RT60 (tema 1). La artificial la imita. Pariente menor: el retardo (miles de retardos con distinta duración/atenuación).
- Tipos (oficio): cámara de eco (sala real); muelle (vibración, captador); placa (lámina metálica); digital algorítmica (calcula retardos/reflexiones); digital de convolución (respuesta al impulso de sala real).
- 3 parámetros: tiempo de reverberación (RT60, cuánto tarda en caer); predemora/pre-delay (cuánto tarda en empezar, separa fuente de sala); mezcla seco/húmedo. Oficio: tamaño de sala simulada, primeras reflexiones, filtro de la cola (recortar graves, evita embarrar). Predemora y relajación de compresor en material rítmico se ajustan a tempo, misma cuenta que el retardo.
- Práctica (oficio): envío auxiliar, no inserción (canal seco, retorno 100% húmedo, varios canales comparten unidad); poco/nada en informativos; en música/ficción da espacio; doblaje grabado en seco necesita la reverberación del lugar de la imagen.

## Efectos

- 5 familias (oficio, no normalizada): TIEMPO (delay, reverb, eco); MODULACIÓN (chorus, flanger, phaser, trémolo, vibrato); DINÁMICA (compresor, puerta, expansor); FRECUENCIA (ecualizadores, filtros); ALTURA (afinador, armonizador, cambio de formantes).
- Modulación (oficio): chorus (copias retrasadas/desafinadas); flanger (retardo corto variable, filtro en peine móvil, tema 1); phaser (barrido con filtros que desfasan); trémolo (nivel cíclico); vibrato (altura).
- Retardo a tempo, 2 pasos: 1) Negra = 60.000 ÷ BPM. 2) Blanca = 2 negras; corchea = 1/2 negra; semicorchea = 1/4 negra. Ejemplo: corchea a 102 BPM = 588÷2 = 294 ms.
- Tabla a 102 BPM: blanca 1.176 ms; negra 588 ms; corchea 294 ms; semicorchea 147 ms. Misma cuenta vale para relajación de compresor a tempo y predemora de reverberación.
- Inserción vs envío (oficio): inserción = señal entera pasa y vuelve procesada (ecualizador, filtros, compresor, limitador, puerta, expansor, de-esser). Envío auxiliar = copia al procesador, retorno se suma (reverberación, retardo, modulación).
- Orden corriente (oficio): paso alto → puerta/expansor → ecualizador → compresor → limitador. Puerta antes del compresor: el make-up acercaría el ruido al umbral de la puerta; limitador al final, techo de lo anterior. Proceso digital añade retardo; latencia: tema 9.

## Lo que este tema no da, y dónde está

- Frecuencias de corte habituales del paso alto de voz: sin fuente leída.
- Ajustes de compresor para fuentes no vocales; tecnologías de compresor (salvo predominio del VCA); tipos de reverberación; efectos de modulación; orden de cadena; inserción/envío: oficio, sin norma ni fabricante. Histéresis de la puerta: sin fuente primaria.
- Reducción espectral y restauración en estación de trabajo: sin fuente; limpieza de audio en postproducción, tema 9.
- Nivel analógico y margen de equipo: tema 2. Mesa/auxiliares/envíos: tema 4. Sonorización y acoplamiento: tema 10. Sonoridad y pico verdadero: tema 13. Latencia: tema 9.
- Procesadores propios de CSRTV: no constan en documento publicado localizado.
