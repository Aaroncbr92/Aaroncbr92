# Tema 1 del específico de Operador/a de Sonido · Fundamentos de sonido

**Siglas**: RTVA, CSRTV, SI, Hz/kHz, Pa/µPa, N, dB/B/Np, dB SPL, dBu, dBV, dBm, dBFS, NC/NR, RT60 (T60), α, STI, XLR, DB HR.

Esqueleto para repasar, no resumen: cada línea lleva delante la fuente o el precepto que la sostiene.

<!-- indice --><!-- /indice -->

## Ondas

- OpenStax: onda sonora longitudinal en el aire y en fluidos; en sólidos, longitudinal y transversal.
- Oficio: λ = v/f; con 340 m/s, 340 Hz → 1 m; 34 Hz → 10 m; 3.400 Hz → 10 cm.
- Guía DB HR: v del aire ≈344 m/s; depende de presión y temperatura.
- OpenStax: v = 331 m/s a 0 °C, 343 m/s a 20 °C (<4 % de diferencia).
- OpenStax, tabla velocidades: agua dulce 1.480 m/s, agua de mar 1.540 m/s, acero 5.960 m/s, caucho vulcanizado 54 m/s; líquidos y sólidos más rápidos que gases.
- Guía DB HR: sonido en ladrillo ≈9 veces más rápido que en aire.
- Oficio: graves largos, atraviesan tabiques y no los absorbe material fino; agudos cortos, direccionales, los detiene cualquier obstáculo.

## Frecuencia

- RD 2032/2009, cap. II, tabla 3, nota (d): hercio, unidad SI derivada, sólo para fenómenos periódicos.
- Oficio: margen audible 20 Hz–20.000 Hz, convencional para oído joven; se estrecha con la edad en agudos.
- Oficio: graves 20–250 Hz, medios 250–4.000 Hz, agudos 4.000–20.000 Hz (límites de oficio, no de norma).
- Oficio: ruido blanco = misma energía por Hz, plano; ruido rosa = misma energía por octava, cae 3 dB/octava; ruido marrón cae 6 dB/octava.
- Oficio: el rosa se usa para medir y ecualizar salas.
- Cálculo: 20 Hz–20 kHz ≈10 octavas (2¹⁰=1.024).

## Amplitud

- RD 2032/2009, cap. II, tabla 3: pascal = N/m², unidad de presión/tensión.
- Oficio: umbral de audición 20 µPa; umbral de dolor ≈20 Pa (factor 10⁶).
- RD 2032/2009, cap. IV, tabla 8: bar = 0,1 MPa = 100 kPa, fuera del SI.
- RD 2032/2009, cap. IV, ap. 4 y tabla 8: decibelio/belio/neper, unidades adimensionales logarítmicas, aceptadas con el SI pero no unidades SI; 1 dB=(1/10)B.
- RD 2032/2009, nota (i), tabla 8: obligatorio indicar la magnitud y el valor de referencia.
- Oficio: dB SPL ref. 20 µPa; dBu ref. 0,775 V; dBV ref. 1 V; dBFS ref. escala digital, 0 máximo; dBm ref. 1 mW.
- Cálculo: umbral de dolor ≈120 dB SPL (20×log 10⁶).
- Oficio: amplitud (tensión, presión) → 20×log; potencia → 10×log. ×2 amplitud=+6 dB; ×2 potencia=+3 dB; ×10=+20/+10 dB.
- Oficio: dos fuentes iguales no correladas suman ≈3 dB (potencias); iguales y en fase, 6 dB (amplitudes); en contrafase se anulan.
- DPA: SPL cae 6 dB al doblar la distancia, fuente puntual en campo libre.

## Fase

- DPA: la fase sólo se expresa comparando con una referencia, a una frecuencia dada.
- DPA: el desfase nace de un retardo (distinta distancia, línea de retardo, filtro eléctrico); se expresa en ±180°.
- DPA: mismo retardo, desfase distinto por frecuencia (90°=0,25 ms a 1 kHz; 0,125 ms a 2 kHz).
- DPA: retardo de 1 ms = 360° a 1 kHz, 180° a 500 Hz, 90° a 250 Hz (≈34 cm a 340 m/s).
- DPA: polaridad ≠ fase; invertir = multiplicar por −1, sin retardo, igual en todas las frecuencias; tras invertir, 180° fuera de fase.
- DPA: botón de inversión rotulado φ o Ø; llamarlo «botón de fase» es impropio.
- DPA: patilla 2 en fase con la presión creciente (condensador balanceado profesional; dinámicos, distinto).
- DPA: filtro en peine = señal sumada a sí misma retardada, de <1 ms a ≈25 ms; niveles dentro de 10 dB.
- DPA: remedios — atenuar ≥10 dB; regla 3:1 (mic vecino 3 veces más lejos); en línea equidistante, 4,5:1; tratar la reflexión o mic de capa límite.
- RTW: correlador de fase, −1 (polaridad invertida) a 0 (sin relación) a +1 (idéntico); mezclas estéreo normales, 0,3–0,7 (cifra de fabricante).

## Dinámica

- Rane: rango dinámico = cociente entre la señal más fuerte y la más débil, en dB.
- Oficio: margen dinámico de un equipo = techo (nivel máximo antes de distorsión) − suelo (ruido propio).
- Rane: equipo profesional, +26 dBu techo, −94 dBu suelo → 120 dB (cifras de fabricante), coincide con los 120 dB del oído.
- Cálculo: cada bit ≈6,02 dB (20×log2); 16 bits ≈96 dB; 24 bits ≈144 dB.
- Oficio: headroom = margen hasta el techo; en digital el techo es absoluto, 0 dBFS, y lo que lo supera se recorta.

## Timbre

- Oficio: tono↔frecuencia; intensidad↔amplitud; timbre↔composición armónica y envolvente.
- Oficio: la fundamental determina el tono; los armónicos son múltiplos enteros de ella; el timbre es el peso relativo de cada uno.
- Oficio: el ecualizador cambia el timbre al mover el peso de los armónicos.
- UNSW Physclips: el timbre depende mucho de la envolvente, y también del espectro; fases ataque, caída, sostenimiento, extinción.
- UNSW Physclips: sin los transitorios de arranque es difícil reconocer los instrumentos (ejemplo: clave al revés).

## Audición

- Protocolo vigilancia sanitaria ruido (CISNS, 2022), 2.1.3: oído externo lleva la onda al tímpano; oído medio (martillo, yunque, estribo) la pasa a la ventana oval; oído interno (cóclea, células ciliadas) genera el impulso eléctrico.
- OpenStax Psychology 2e: las células ciliadas generan impulsos que viajan por el nervio auditivo al cerebro.
- Protocolo CISNS, 2.1.3-2.1.4: tonotopía — graves en la parte superior de la cóclea, junto al helicotrema; agudos junto a la ventana oval; células de los agudos (3.000-6.000 Hz) afectadas por el ruido.
- Oficio: curvas isofónicas = sensibilidad del oído por frecuencia; varía con el nivel; oído más sensible entre 2 y 5 kHz; la curva A del sonómetro imita la respuesta a nivel bajo.
- Oficio: NC/NR fijan el ruido de fondo tolerado en un recinto; no describen el oído, no son isofónicas.
- Oficio: enmascaramiento — un sonido tapa mejor las frecuencias próximas, más hacia arriba; crece con el nivel del enmascarador; hay enmascaramiento temporal.
- DPA: el oído es poco sensible a la fase de componentes aisladas; sí se oyen el filtro en peine y la contrafase entre canales.
- OpenStax Psychology 2e: pistas monoaurales (arriba/abajo, delante/detrás) y biaurales (eje horizontal): diferencia interaural de nivel (atenuación por la cabeza) y de tiempo.
- Shinn-Cunningham, *Encyclopedia of Computational Neuroscience*: efecto de precedencia, imagen fundida cerca del sonido que llega antes («ley del primer frente de onda», efecto Haas); 1-5 ms con chasquidos, decenas de ms con voz o música.

## Acústica básica

- Oficio: sonido directo + primeras reflexiones + cola reverberante.
- Oficio: frontera de 50 ms — antes se suma al directo, refuerzo; después se oye como eco; a 340 m/s, 50 ms ≈17 m de recorrido de más.
- Oficio: RT60 = tiempo en caer 60 dB tras cesar la fuente.
- Oficio: RT60 orientativo — estudio/control <0,3 s; teatro/conferencia 0,8-1,2 s; sala sinfónica 1,8-2,2 s; catedral >5 s (no normativo).
- Oficio: Sabine, cualitativo — RT60 crece con el volumen y decrece con la absorción.
- Oficio: coeficiente de absorción α, de 0 (refleja todo) a 1 (absorbe todo); depende de la frecuencia.
- Oficio: superficies paralelas favorecen ondas estacionarias y modos propios; no se corrigen ecualizando, sí con trampas de graves, geometría o moviendo la escucha.
- Cálculo: paredes paralelas a 3,4 m → primer modo en 50 Hz (340/6,8).
- Oficio: sala para la palabra (inteligibilidad, RT corto, reflexiones tempranas, STI) frente a sala para música (envolvente, RT largo, reflexiones laterales).
- Guía DB HR: aislamiento (entre dos recintos; masa, rigidez, amortiguamiento) ≠ acondicionamiento (un recinto; revestimientos, ligado al RT60).
- Guía DB HR: ley de masa — aislamiento +6 dB al duplicar masa o frecuencia (6 dB/octava); menos aislamiento en graves que en medios y agudos; válida sólo entre la frecuencia de resonancia y la crítica.
- Guía DB HR: la calidad acústica de una carpintería depende de su estanquidad al aire.
- Guía DB HR: ruido de impacto — material aislante elástico convierte la energía del impacto en deformación, no en sonido.
