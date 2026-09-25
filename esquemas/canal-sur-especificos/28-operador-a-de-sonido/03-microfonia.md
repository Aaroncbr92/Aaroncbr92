# Tema 3 del específico de Operador/a de Sonido · Microfonía

**Siglas**: RTVA, CSRTV, IEC, UIT-R/ITU-R, SPL, dB(A), dBV, THD, RMS, DI, DF, DSF, P48, XLR, ORTF, NOS, DIN, RF, AF, UHF, VHF, FM, RSSI, WMAS, IEM, PA, DECT, ENG.

Esqueleto para repasar, no resumen: reduce a lo justo para reconstruir el tema en la cabeza, no sustituye leerlo.

<!-- indice -->
<!-- /indice -->

## Tipos

- DPA: micrófono = transductor acústico-mecánico-eléctrico (altavoz, el inverso).
- DPA: dinámico (bobina móvil), bobina en campo magnético; no necesita alimentación.
- Royer: cinta = dinámico, lámina metálica en campo magnético; sin alimentación salvo activos.
- DPA: condensador, membrana-placa fija de capacidad variable; necesita P48 o pila; interfase de impedancia interna.
- DPA: electret = condensador con carga permanente; poca alimentación, sólo para su electrónica.
- DPA: sólo necesita alimentación el micrófono con electrónica incorporada.
- DPA: transductor y directividad son independientes; hay dinámicos y condensadores de cualquier patrón.
- DPA: de presión (sólo cara delantera) → omnidireccional; de gradiente de presión (dos caras) → direccionales.
- DPA: en rigor sólo el ocho es gradiente puro; cardioide y variantes, combinación presión+gradiente.
- Royer: la cinta es ocho por naturaleza (dos caras expuestas igual, contrafase trasera); otro patrón se fabrica.
- Royer/Neumann: condensador de doble membrana da varios patrones (ej. U 87 Ai: omni, cardioide, ocho).
- DPA: desmiente tópicos — dinámico no es más robusto ni aguanta más SPL; condensador no "suena más alto", es más sensible.
- Oficio: por forma/uso — lavalier/corbata, de mano, de cañón, de diadema, de solapa inalámbrico.
- DPA: micrófono de capa límite, pegado a superficie, gana 6 dB sin filtro en peine.
- DPA: de lápiz (uso general) y de gran diafragma; diafragma mayor = menos ruido propio; cápsula pequeña = omni más verdadero.
- DPA: el miniatura domina TV por invisible; posible desde el electret (años 60).

## Patrones polares

- DPA: diagrama polar, medido en cámara anecoica, plato giratorio, tonos o ruido rosa por bandas.
- DPA: omni capta igual en todas direcciones.
- DPA: cardioide ancho, atenuación trasera ~7-8 dB (−3 dB a 90°, −6 dB a 135°).
- DPA: cardioide abierto, atenuación trasera ~18 dB (71°/98°).
- DPA: cardioide, sordo detrás (66°/90°).
- DPA: supercardioide, sordo a ±135°, con lóbulo trasero (58°/78°).
- DPA: hipercardioide, sordo a ±115°, con lóbulo trasero (55°/73°).
- DPA: ocho, sordo a los lados (54°/73°); polaridad invertida en el lóbulo trasero de super, hiper y ocho.
- DPA: ángulo de aceptación = donde cae 3 dB, normalmente medido a 1 kHz.
- DPA: DF = energía en eje / energía en todas direcciones; DI = 10·log DF.
- DPA: DSF — cardioide 1,73, hipercardioide 2,00 (DI: cardioide 4,8 dB, hiper 6,0 dB).
- DPA: cardioide a 17 cm ≈ omni a 10 cm (misma relación directo/sala).
- DPA: el patrón real cambia con la frecuencia; el omni se vuelve directivo en agudos.
- DPA: efecto cortina, coloración fuera de eje; cardioide, cobertura ~130°, rechazo trasero ~30 dB según frecuencia.
- DPA: cañón = cardioide de 1er orden + tubo de interferencia; directividad crece con la frecuencia; no se nombra por patrones estándar.
- Oficio: cañón mal apuntado pierde nivel y agudos.
- Oficio: uso en ENG — omni (corbata/ambientes), cardioide (mano/voz), super (ruido), hiper (lejano/ruidoso), cañón (pértiga/larga distancia), ocho (cara a cara).
- Oficio: patrón estrecho no acerca el sonido, aleja el ruido; penaliza el movimiento.
- DPA: recomienda probar primero un omni — más natural, aguanta SPL alto, sin proximidad, poco sensible a viento/golpe.
- DPA: efecto de proximidad, más graves al acercarse; sólo en gradiente (cardioide…ocho), no en omni.
- DPA: proximidad más fuerte en eje, desaparece a 90° en cardioide; existe <1 m, casi nula >1 m.
- Oficio: uso creativo en voz de radio (cuerpo); filtros de corte de graves compensan.
- DPA: cardioide muy cerca gana cuerpo pero "boomy"; direccional pierde graves frente a omni a >30 cm.

## Sensibilidad

- DPA (IEC 60268-4): capacidad de convertir presión en tensión; en campo libre, a 1 Pa (94 dB SPL), en eje, a 1 kHz.
- DPA: se expresa en mV/Pa o dBV/Pa (equivalentes); ejemplo 10 mV/Pa = −40 dBV/Pa.
- DPA: cifra nominal, tolerancia ±2 o ±3 dB.
- DPA: más sensibilidad = menos ganancia; fuente débil pide micrófono sensible, SPL extremo pide poco sensible.
- DPA: voz de 150 dB SPL de pico → 0,63 V (1 mV/Pa) o 6,3 V (10 mV/Pa); riesgo de saturar el previo.
- DPA: ruido propio/equivalente — buen resultado <15 dB(A) o <25-30 dB (UIT-R BS.468-4).
- DPA: SPL máximo = umbral de THD <1 % (criterio DPA; de pico, al 10 %).
- DPA: rango dinámico = SPL máximo − ruido propio.
- DPA: carga ≥5-10 veces la impedancia de salida; ejemplo 100 Ω → carga ≥500-1.000 Ω; P48 da 3,4 kΩ; carga baja recorta graves.

## Colocación

- Oficio: mesa de locutores → cardioide por descarte (omni mezcla la sala; ocho, super e hiper cogen al de enfrente).
- Oficio: regla de familia — el patrón se elige por lo que hay que rechazar, no por lo que hay que captar.
- DPA: direccional se aleja más (factor de distancia) que omni con igual relación directo/sala.
- DPA: acercar un direccional trae proximidad; la capa límite suprime la reflexión de superficie cercana.
- DPA: monitor de suelo al mínimo del micrófono — detrás en cardioide, a ±135°/±115° en super/hiper.
- DPA: direccionales acoplan de golpe en agudos; omni, gradualmente en graves-medios.
- DPA: micrófono de mano — sujetar por el mango, no la rejilla; "cupping" +9 dB a 1,8-2,2 kHz y resonancia ~10 kHz, cambia la directividad.
- DPA: paravientos con logotipo atenúa 2-4 kHz si se habla de lado.
- DPA: posición del miniatura — frente, casi igual a la referencia; diadema/comisura, buena; oreja, pierde desde 1 kHz; pecho/corbata, la peor (pierde 2-4 kHz).
- DPA: recomienda EQ compensatoria (realce 2-4 kHz) cuando el micrófono va bajo o detrás de la boca.
- Libro de estilo (3.17.1, p. 59): entrevista fuera de plató, cámara en trípode y corbata para el entrevistado.
- Libro de estilo (3.17.1.3, p. 60): el micrófono de mano no se cede al entrevistado.
- Libro de estilo (8.3.2, p. 117): en directo, micrófono vertical apoyado en el esternón; corbata si el lugar está habilitado.
- Libro de estilo (8.6.1, p. 122): telas brillantes y su roce producen ruido captado por el micrófono.
- Oficio: colocación del corbata — un palmo de la boca, centro del pecho, sin roce, bucle de cable sujeto.
- DPA: parejas estéreo — 15 dB o 1,1 ms para separar una fuente 30°.
- DPA: coincidente (XY, Blumlein, MS) — sólo diferencia de nivel, compatible en mono.
- DPA: cuasi coincidente (ORTF 17 cm/110°, DIN 20 cm/90°, NOS 30 cm/90°) — nivel y tiempo.
- DPA: espaciada (AB) — sólo tiempo, no compatible en mono (usar un solo canal).
- DPA: MS — L=M+S, R=M−S; único sistema con anchura ajustable tras la grabación.
- DPA: ambisónico, A-format, 4 cardioides en tetraedro; B-format, W (omni), X/Y/Z (ochos ortogonales).

## Soportes

- Oficio: pie de suelo/trípode, pie de mesa, pértiga/jirafa, suspensión elástica, paravientos/peluca, pinza.
- Oficio: el micrófono nunca va rígido sobre el soporte (transmite golpes y vibración).
- Oficio: la jirafa evita poner la base delante de la fuente; la pértiga acerca el cañón, siempre apuntado a la boca.
- DPA: barra estéreo con marcas a 90° (XY) y 110° (ORTF).
- DPA: en laboratorio se suspende el micrófono con hilos para evitar la influencia del pie.
- Oficio: seguridad — base ancha y contrapeso del lado de la base; pértiga lejos de líneas eléctricas; cables fijados y señalizados.

## Inalámbricos

- DPA: sistema = emisor (con el micrófono) + receptor; cada canal necesita un emisor y un receptor en la misma frecuencia.
- DPA: emisores — de mano, de petaca (*bodypack*), enchufable universal (XLR + P48).
- DPA: el emisor alimenta al condensador; suele llevar corte de graves, limitador y a veces inversión de polaridad.
- DPA: analógico — FM, desviación nominal ±40 kHz, máxima ±75 kHz; preénfasis 50 µs + compansor; rango dinámico >90 dB; latencia 0 ms; el compansor obliga a usar la misma marca.
- DPA: digital — códec de 6:1 a 8:1; relación S/R 100-125 dB; latencia 2-3 ms (hasta 7-8 ms); cifrado habitual.
- DPA: WMAS — un canal de TV de 8 MHz, hasta 32+32 canales, sirve a micrófonos e IEM.
- DPA: bandas UHF, sobre todo 470-694 MHz en Europa (+823-832, 863-865 MHz, 1,88-1,9 GHz DECT, 2,4 GHz); comprobar normativa de cada país (en España, tema 12).
- DPA: banda > grupo (canales calculados para no interferirse) > canal (frecuencia concreta).
- DPA: dos emisores del mismo sistema van en el MISMO grupo.
- DPA: procedimiento — apagar emisores, escanear grupo en el receptor, encender y sincronizar emisores uno a uno.
- DPA: diversidad, dos antenas/sintonizadores, conmuta a la señal mejor; visión directa es la regla más importante.
- DPA: la punta del dipolo receptor es su zona menos sensible; no apuntarla al emisor.
- DPA: separación de antenas de diversidad — ¼ onda, ½ onda (25 cm a 600 MHz) o mínimo 30 cm según la guía.
- DPA: 3-5 m entre emisores y antenas receptoras (o mínimo 4 m según otra guía); cable de antena corto, receptor cerca de la antena.
- DPA: antena del emisor a 5 cm del cuerpo; pegada, pierde hasta el 99 % de la potencia; petaca hacia delante si el receptor está al frente.
- DPA: pilas — repuesto cargado, no fiarse del indicador, comprobar tras 2 minutos encendido; retirarlas si se guarda semanas.
- Oficio: comprobación antes de salir al aire — pilas, misma frecuencia sin repetir, ganancia ajustada, RF en todo el recorrido, escucha por auriculares, cable de reserva.

## Accesorios

- DPA: paravientos/cesta/peluca reducen el ruido que el viento genera en la cápsula, no el sonido del viento; hasta 20-30 dB.
- DPA: los direccionales son más sensibles al viento que los omni.
- DPA: cuanto más grande el paravientos, mejor; la peluca en miniatura reduce ~27 dB(A).
- DPA: regla — frenar el viento lo más lejos posible del diafragma.
- DPA: lluvia — la espuma mojada colorea (resonancia 3-4 kHz); llevar repuestos secos.
- DPA: antipop — anillo con tela/espuma, cerca de la boca y lejos del micrófono, sin cambiar la directividad; ataca el golpe de voz, no el viento exterior — no intercambiable con el paravientos.
- DPA/Oficio: la suspensión elástica es imprescindible en direccionales y en la pértiga (ruido de manejo).
- DPA: el maquillaje puede tapar la rejilla del miniatura; limpiar o proteger.
- DPA: la funda higiénica ha de ser muy fina (<10 µm) y suelta, o cambia la directividad.
