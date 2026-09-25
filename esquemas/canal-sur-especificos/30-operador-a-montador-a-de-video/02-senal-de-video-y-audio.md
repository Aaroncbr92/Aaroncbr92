# Tema 2 del específico de Operador/a Montador/a de Vídeo · Señal de vídeo y audio

**Siglas**: RTVA; CSRTV; UIT-R; EBU; SMPTE; AES; SDI; HD; UHD; HDR; SDR.

Esqueleto para repasar, no resumen: cada línea es un dato con su fuente delante; vuelve al tema para el desarrollo.

<!-- indice -->
<!-- /indice -->

## 1. La señal de vídeo

- Oficio: síntesis aditiva (tres conos, tres estímulos); Grassmann (independencia, sustitución, aditividad, intensidad=suma); espectral=una λ; no espectral=púrpura/magenta (mezcla de extremos).
- BT.709-6: primarios R(0,640;0,330) G(0,300;0,600) B(0,150;0,060), blanco D65. BT.2020-2: primarios más saturados, mismo D65; BT.2100-3 usa los de BT.2020.
- Coeficientes de luminancia: BT.601 (0,299/0,587/0,114); BT.709 (0,2126/0,7152/0,0722); BT.2020 (0,2627/0,6780/0,0593). Oficio: verde pesa más, azul menos. Cadena: 601 SD·709 HD·2020 UHD·2100 HDR.
- BT.709-6, 4.1/3.2: señal R,G,B o Y,CB,CR; Y=0,2126R+0,7152G+0,0722B.
- CL: Y desde RGB lineal, luego gamma; NCL: gamma por primario, luego Y'. BT.2020-2/BT.2100-3: NCL por defecto, CL/CI (ICTCP) sólo si todas las partes lo acuerdan. Oficio: NCL cuela luminancia en el color; con 4:2:2/4:2:0 se pierde brillo en saturados.
- Gamma, BT.709-6 1.2: V=1,099L^0,45−0,099 (L≥0,018); V=4,500L (L<0,018); 0,45≈inversa de 2,2. Monitor: BT.1886.
- Oficio: log es de rodaje, no emisión; imagen lavada, conserva luces/sombras, exige etalonaje; no es RAW.
- Oficio: compuesto=luminancia+crominancia en amplitud, un cable (PAL/NTSC); componentes=tres señales separadas; digital=muestras, sin modulación.
- Oficio: progresivo=imagen entera; entrelazado=dos campos=un cuadro; evita parpadeo sin doblar ancho de banda (25 imgs parpadean; 50 no cabían; entrelazado da 50 refrescos con datos de 25).
- BT.709-6: P y PsF/I coexisten; PsF=imagen progresiva en dos segmentos, no es entrelazado; interfaz de I y PsF común. 50/I: 50 Hz campo, 2:1, 25 Hz imagen; 1.125 líneas totales, 1.080 activas.
- Oficio: 1080i50=25 cuadros/50 campos (BT.709-6 lo llama «25 interlace»). BT.2020-2/BT.2100-3: sólo progresivo. Entrelazado sin desentrelazar antes de ralentizar/reencuadrar da peines.
- BT.709-6: cadencias 60,50,30,25,24 Hz (60/30/24 también /1,001). BT.2020-2/BT.2100-3: añaden 120,100. Oficio: /1,001 sólo en familia americana; 25/50/100 enteras→NDF. Europa (50 Hz) trabaja en 25/50; 29,97 en montaje de 25 obliga a convertir.
- BT.709-6, anexo 2: cine 24→25 Hz sin pérdida de calidad; dura 4 % menos, sonido sube de tono si se acelera (24/25=0,96).
- BT.709-6: HD 16:9, 1.920×1.080 activas, píxel 1:1. BT.2020-2: UHD 7.680×4.320 y 3.840×2.160, 16:9. BT.2100-3: los tres formatos, píxel cuadrado.
- Oficio (no normativo): SD PAL 720×576; HD 1.280×720; Full HD 1.920×1.080; UHD 3.840×2.160; 4K DCI 4.096×2.160 (1,90:1); 8K 7.680×4.320. UHD multiplica píxeles, no cambia 16:9; 4K TV≠4K cine.
- BT.2100-3, nota 1b: producir en resolución más alta y submuestrear da mejor calidad que producir ya en la de distribución; escalar HD a UHD no crea detalle (oficio).
- BT.709-6, 5.8-5.9: luminancia 148,5 MHz (50/P) o 74,25 MHz (50/I,25/P); color a la mitad. 4.4: 1.920 muestras luminancia/línea, 960 por diferencia de color, co-situadas→4:2:2. Cálculo: 2.640 muestras×1.125 líneas×50=148,5 M; mitad 74,25 M.
- Muestreo cromático (bloque 4×2 píxeles): 4:4:4 sin submuestreo (grafismo, croma, cine digital); 4:2:2 mitad horizontal (producción TV); 4:2:0 mitad horiz. y vert. (emisión); 4:1:1 cuarta horizontal (SD antiguo, oficio). BT.2100-3 define los tres por submuestreo respecto de Y'.
- Oficio: submuestreo reduce archivo sin pérdida notable; limita croma (4:2:0 recorta mal); incrustación mínimo 4:2:2, mejor 4:4:4. 4.ª cifra=canal alfa (opacidad).
- Cálculo: 8b=256 niveles, 10b=1.024, 12b=4.096 (2^n). Más bits evita *banding*; no crean rango dinámico (lo da el sensor) pero lo hacen aprovechable. Resolución espacial≠profundidad de color.
- BT.709-6, 4.5: HD 8 o 10 bits. BT.2020-2: UHD 10 o 12. BT.2100-3, tabla 9: HDR 10 o 12. HD admite 8; UHD/HDR mínimo 10.
- BT.709-6, 4.6-4.7 (rango estrecho): negro 16/64 (8b/10b); blanco pico 235/940; acromático CB,CR 128/512; extremos CB,CR 16-240/64-960; datos vídeo 1-254/4-1.019; sincronismo 0,255/0-3,1.020-1.023.
- BT.2100-3, tabla 9: rango estrecho por defecto (negro 64/256, pico 940/3.760); rango completo (negro 0, pico 1.023/4.095) sólo si se acuerda. Oficio: negros hundidos o imagen lavada tras otro programa=confusión estrecho/completo.
- EBU R 103 v3.0, tabla 1 (código): 8b nominal 16-235/preferente 5-246/total 1-254; 10b 64-940/20-984/4-1.019; 12b 256-3.760/80-3.936/16-4.079; 16b 4.096-60.160/1.280-62.976/256-65.279.
- EBU R 103: fuera de preferente=error de gama; no superar total (recorta, distorsión armónica); instrumento avisa sólo si error>1 % de imagen. Directo: recortadores al preferente; preproducido/gradeado: al nominal. Legalizadores con cuidado; sub-negros no se recortan (PLUGE); analógico 0-700 mV. Aviso: «−1 %»/«103 %» no están en R 103 v3.0. Pieza entregada en límites nominales, no preferentes.
- Oficio: HDR=más recorrido de brillo, no más resolución. *Nit*=cd/m²; candela=intensidad; 1 cd/cm²=10.000 nits; lumen=flujo total.
- BT.2100-3: PQ o HLG. HLG compatible con SDR (curvas heredadas); PQ (oficio: absoluta, hasta 10.000 cd/m², =ST 2084). PQ=máster/plataformas; HLG=directo/emisión (oficio).
- BT.2100-3, nota 10a: blanco de referencia HDR=carta 100 % reflectancia=203 cd/m² (PQ o HLG con pico 1.000 cd/m²).
- Informe BT.2408-9, tabla 1: grafismo al nivel del blanco de referencia; gris 18 %=26 cd/m² (38/38 % PQ/HLG); 83 %=162 (56/71); 90 %=179 (57/73); blanco ref. 100 %=203 (58/75). El 18 % real varía con la cámara; blanco HDR≠pico blanco SDR.
- Oficio: rótulo HDR va al 75 % (HLG) o 58 % (PQ), no al 100 %; encima quedan especulares.
- BT.2100-3, tabla 3: visionado crítico, pico≥1.000 cd/m² (áreas pequeñas), negro≤0,005. Oficio: SDR~100 nits; etalonar HDR exige monitor HDR. Gama de color y rango dinámico son ejes distintos.
- Oficio (instrumentos): forma de onda=luminancia línea a línea (exposición); vectorscopio=crominancia, ángulo=tono/distancia=saturación (color); histograma=reparto de niveles.
- Oficio: monitor de referencia — *blue only*, *underscan*, marcadores de seguridad, falso color/cebras. Prueba: barras (croma/fase/nivel), rampa (linealidad).
- Oficio+R 103: 10 bits, negro<64 o blanco>940=fuera de nominal; >984 o <20=error de gama. Vectorscopio fuera de cajas=sobresaturado. HDR: rótulo HLG al 75 % (BT.2408-9).
- Oficio: SDI=un coaxial, vídeo+audio embebido+datos auxiliares. ST 259:2008: SD-SDI, 10 bits, 143/270/360 Mb/s (uso 270). ST 292-1:2018: HD-SDI, 1,485(/1,001) Gb/s. ST 424:2012: 3G-SDI, 2,970(/1,001) Gb/s. ST 2082-1:2023: 12G-SDI, 11,88(/1,001) Gb/s. Tres primeras estabilizadas; ST 2082-1 activa.
- Cable/conector: coaxial 75 Ω, BNC (IEC 61169-8); NRZI aleatorizada. Atenuación: ST 259 20-30 dB; ST 424 hasta 30; ST 2082-1 hasta 40; más rápida la interfaz, menos alcance (oficio).
- Cálculo: 74,25 MHz×2×10b=1.485 Mb/s (HD-SDI); 148,5 MHz doble=2.970 (3G-SDI, 1080p50); UHD 2160p50×4 píxeles=11.880 (12G-SDI). 1080i50/1080p25→HD-SDI; 1080p50→3G-SDI; 2160p50→12G-SDI o varios cables.
- Oficio: *jitter*=variación del instante de llegada del bit, ruido de fase; provoca corte, no degradación suave. ST 292-1, 8.1.8: medido según RP 184 (no leída), en UI=duración de un bit. Tabla 3: *timing jitter* 1 UI (desde 10 Hz); *alignment jitter* 0,2 UI (desde 100 kHz); borde superior común >1/10 reloj; prueba con barras de color.
- Oficio: IP (ST 2110) y ficheros→tema 4. Equipos se enganchan a referencia común para cambiar de fuente sin saltos.
- BT.709-6, parte 6: sincronismo tri-nivel, válido 60/P a 24/PsF. 6.1: negro 0 mV, blanco 700 mV. 6.2: CB/CR ±350 mV. 6.3: tri-nivel bipolar. 6.5: ±300 mV±2 %. 6.6: en todos los componentes. *Genlock*/*black burst*: nombres de sala sin fuente leída (oficio).

## 2. La señal de audio

- Oficio: tono=frecuencia (grave/agudo); intensidad=amplitud (fuerte/débil, dB); timbre=composición armónica. Frecuencia (física) causa tono; amplitud causa intensidad (psicoacústica).
- Oficio: margen audible 20-20.000 Hz, se estrecha con la edad (por arriba). Armónicos=fundamental+múltiplos enteros (ej. 440→880,1.320,1.760). Timbre=intensidad relativa de armónicos; ecualizador lo cambia, no la nota.
- Oficio: frecuencia de muestreo fija la frecuencia máxima conservada (48 kHz TV, 44,1 disco, 96 producción); bits fijan el rango dinámico (16b emisión, 24b producción); canales (2, 5.1, 5.1.4).
- Oficio: muestrear a más del doble de la frecuencia máxima; 48 kHz cubre 20 kHz, 32 kHz pierde agudos. Cada bit añade ~6 dB (16b≈96 dB, 24b≈144 dB). Trabajar a la mayor profundidad, reducir sólo al final.
- EBU Tech 3250: AES/EBU a 48 kHz (CCIR 646). EBU R 68 (parecer): codificación lineal, sin preénfasis, mínimo 16 bits (BS.646); nota 1: puede no bastar según convertidor. PCM=audio lineal sin comprimir.
- Cálculo: caudal=frec.×bits. 48 kHz×24b=1,152 Mb/s/canal; estéreo=2,304; 16 canales=18,4.
- Oficio: 0 dBFS=código más alto, niveles negativos, lo que pasa se recorta. EBU R 68-2000: alineación a −18 dB bajo el máximo, con independencia de los bits; señal de alineación 9 dB (u 8) bajo el máximo del programa; cuasipico puede engañar 3 dB, o 6-15 con error de operador. Tono 1 kHz de barras a −18 dBFS (oficio).
- EBU R 128-2023 (mide con BS.1770): objetivo −23,0 LUFS, tolerancia ±1,0 LU si no alcanzable (directo) sin hacerse costumbre; ±0,2 LU por error de medida; excepción sólo por debajo de −23,0, avisada.
- EBU R 128: pico verdadero ≤−1 dBTP en producción, tolerancia ±0,3 dB; máximos pueden ser menores según distribución. Medida del programa entero, medidor BS.1770/Tech 3341. Programa incluye piezas cortas; suplementos s1/s2 no leídos. LUFS=LKFS.
- Oficio: pieza entregada medida entera, −23 LUFS, pico≤−1 dBTP; se corrige con ganancia, no recorte. Limpieza/mezcla→tema 7.
- EBU Tech 3250: 48 kHz, alcance de cientos de metros. Subtrama=32 intervalos; trama=dos subtramas; bloque=192 tramas (preámbulo Z). Cálculo: 48.000 tramas/s×64=3,072 M intervalos/s.
- Oficio (tema 28-11): micrófono, impedancia no especificada; AES3/XLR, 110 Ω; AES3id/coaxial, 75 Ω.
- Oficio: SDI lleva audio en datos auxiliares. 272M-2004 (SD): 2-16 canales (4 en compuesto), 20 bits (24 opcional). ST 299-1:2009 (HD): 16-32 canales a 32/44,1/48 kHz, 8 a 96 kHz, 24 bits. ST 299-2:2010 (3G nivel A): canales 17-32, 24 bits.
- 272M: canales en pares, grupos de 4 con ID único; 1-4 grupo 1, 5-8 grupo 2, etc. Oficio: 4 grupos=8 pares AES/EBU; embebido derivado de AES3.
- ST 299-1, 1.4: datos de audio en HANC del flujo Cb/Cr; control en HANC del flujo Y.
- Oficio: embeber/desembeber audio de vídeo. Pistas numeradas al entrar por SDI; reparto, acuerdo de cada casa; el de CSRTV no consta en documento publicado leído.

## 3. Vídeo y audio juntos: código de tiempo y sincronía

- Oficio: código de tiempo=etiqueta de cuadro (h:m:s:cuadros); localiza material, sincroniza cámaras.
- Oficio: NDF cuenta todos los cuadros (24,25,30,50); DF salta números para casar con el reloj de pared (29,97/59,94). A 25 fps, NDF (25 entero=1 s exacto).
- Oficio: DF nació del sistema americano (29,97 real); de 30 en 30 el código se atrasa ~3,5 s/hora; DF salta números, sin tirar cuadros (sólo la etiqueta cambia).
- Cálculo (BT.709-6, 30/1,001): 3.600×30/1,001≈107.892 cuadros/hora; de 30 en 30 harían falta 108.000; diferencia≈108 cuadros=3,6 s.
- Oficio: el código de la secuencia se fija con su cadencia; material 29,97 en secuencia de 25 no conserva código cuadro a cuadro.
- 272M/ST 299-1: se prefiere audio síncrono a 48 kHz (o 96 en HD) intra-estudio; opción 32-48 kHz síncrono/asíncrono.
- Cálculo: 48.000 muestras/s entre 25 cuadros=1.920/cuadro; entre 50=960; con /1,001 la cuenta no es entera.
- Oficio (desincronía): relojes distintos → desfase creciente → sincronizar en origen; clip desplazado al mover → desfase fijo → reenganchar; retardo de pantalla → labios desajustados → medir la cadena, no el montaje.
- Oficio: para casar imagen/sonido separados, código común o claqueta/palmada.

## Normativa que el tema invoca

- UIT-R BT.709-6 (06/2015): HD, colorimetría, cadencias, exploración, muestreo, cuantificación, sincronismo. UIT-R BT.2020-2 (10/2015): UHD. UIT-R BT.2100-3 (02/2025): HDR, PQ/HLG. Informe BT.2408-9 (03/2026): práctica HDR, blanco de grafismo.
- EBU R 103 v3.0 (2020): tolerancias de vídeo. EBU R 68-2000: alineación de audio. EBU R 128-2023: sonoridad. EBU Tech 3250 (2004): AES/EBU.
- SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023: SDI. SMPTE 272M-2004, ST 299-1:2009, ST 299-2:2010: audio embebido. SMPTE ST 2084: curva PQ.

## Lo que este tema no da, y dónde está

- Formato propio de CSRTV, reparto de pistas, alineación/sonoridad de entrega: no consta en documento publicado leído.
- SMPTE 274M/296M, ST 425-5, ST 2081, HDR10/Dolby Vision y ST 2086, SMPTE ST 12 y la regla exacta del salto DF: no leídas. LUT SDR/HDR del Informe BT.2408: sólo títulos.
- Códecs, compresión, contenedores, IP: tema 4. Corrección de color, limpieza de audio, *ducking*: tema 7. Ingesta y verificación: tema 8.

## Trazabilidad

- BT.709-6, BT.2020-2, BT.2100-3, Informe BT.2408-9: leídas 25-09-2026.
- EBU R 103 v3.0: copiado del tema 9 de Cámara Operador, 24-09-2026 (por ese tema).
- EBU R 68-2000, EBU R 128-2023: leídas 25-09-2026.
- EBU Tech 3250, SMPTE 272M-2004, ST 299-1:2009, ST 299-2:2010: copiados del tema 11 de Operador/a de Sonido, 25-09-2026 (por ese tema).
- SMPTE ST 259:2008, ST 292-1:2018, ST 424:2012, ST 2082-1:2023: leídas 25-09-2026.
