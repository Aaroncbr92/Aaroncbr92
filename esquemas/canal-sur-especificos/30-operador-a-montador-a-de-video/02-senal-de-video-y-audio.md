# Tema 2 del específico de Operador/a Montador/a de Vídeo · Señal de vídeo y audio

**Siglas**: RTVA; CSRTV; BOJA; UIT-R; EBU; SMPTE; AES; CIE; SD/HD/UHD; DCI; SDR/HDR (PQ, HLG); RGB; Y, CB, CR; CL/NCL/CI; LUT; SDI/HD-SDI; BNC; XLR; NRZI; PsF; PAL/NTSC; PLUGE; TC (DF/NDF); PCM; HANC; fps; Hz/kHz/MHz; dB/dBFS; LU/LUFS(=LKFS); dBTP; cd/m² (nit); Mb/s, Gb/s; IP.

Esqueleto para repasar, no resumen: cada línea es un gancho, no una frase completa; la fuente o el precepto va delante.

<!-- indice -->
<!-- /indice -->

## 1. La señal de vídeo

- (Oficio) 3 conos → síntesis aditiva, 3 primarios. Grassmann: 1ª independientes · 2ª sustitución equivalente · 3ª suma aditiva · 4ª intensidad=suma.
- (Oficio) Espectral=1 longitud de onda; no espectral=mezcla extremos (púrpura, magenta); línea de los púrpuras, CIE.
- BT.709-6: R(0,640;0,330) G(0,300;0,600) B(0,150;0,060), blanco D65(0,3127;0,3290). BT.2020-2: R(0,708;0,292) G(0,170;0,797) B(0,131;0,046), mismo D65; BT.2100-3=primarios de BT.2020.
- Luminancia: BT.601 0,299/0,587/0,114 · BT.709 0,2126/0,7152/0,0722 · BT.2020 0,2627/0,6780/0,0593 (suman 1). (Oficio) Verde pesa más, azul menos. Cadena 601 SD·709 HD·2020 UHD·2100 HDR.
- BT.709-6 4.1: R,G,B o Y,CB,CR. 3.2: Y=0,2126R+0,7152G+0,0722B. 3.3: CB/CR restando Y, escalando. Aspecto final: monitor con BT.1886.
- CL: Y desde RGB lineal, luego gamma (correcto). NCL: gamma por primario, luego Y' (uso real); con 4:2:2/4:2:0 se pierde brillo en saturados.
- BT.2020-2 cuadro 4: CL si precisión/eficiencia; NCL si compatibilidad SD/HD. BT.2100-3: HDR usa ICTCP; NCL por defecto, CI no en intercambio salvo acuerdo.
- Gamma=relación no lineal código↔luz. BT.709-6 1.2: V=1,099L^0,45−0,099 (1≥L≥0,018); V=4,500L (resto). 3.1: exponente 0,45→«gamma 2,2» (oficio).
- (Oficio) Curva logarítmica: rodaje no emisión; lavada, bajo contraste, conserva luces/sombras, exige etalonaje; no=RAW.
- (Oficio) Compuesto: Y+croma mezclados, AM sobre subportadora, 1 cable (PAL/NTSC). Componentes: 3 señales, banda base. Digital: muestreada/cuantificada, SDI/fibra/red.
- (Oficio) Progresivo: imagen entera. Entrelazado: 2 campos=1 cuadro; evita parpadeo sin doblar el ancho de banda.
- BT.709-6: captación P o I; transporte P/PsF/I. 50/I: 50 Hz campo, 2:1, 25 Hz imagen; 1.125 líneas (5.2), 1.080 activas (2.4). Anexo 2: PsF=progresiva en 2 segmentos, interfaz no captación, interfaz de I y PsF común.
- (Oficio) 1080i50=1080 líneas activas, 50 campos/s=25 cuadros completos; BT.709-6 «25 interlace» (cuenta cuadros), oficio «50i» (cuenta campos): misma señal. BT.2020-2/BT.2100-3: sólo Progressive.
- (Oficio) Montador: entrelazado se monta respetando orden de campos; mover/escalar sin desentrelazar→peines/temblores.
- BT.709-6 parte 2: 60/50/30/25/24 Hz; 60,30,24 también /1,001. BT.2020-2 tabla 2 (=BT.2100-3): +120,100. (Oficio) /1,001 sólo en familias 24/30/60/120 (EEUU); 25/50/100 enteras→TC sin salto.
- BT.2020-2: cadencia influida por red eléctrica y luz de escena. (Oficio) Red europea 50 Hz→trabajo en 25/50; 29,97 en montaje de 25 obliga a convertir.
- BT.709-6 anexo 2: 25 Hz reproduciendo el original de 24 Hz más rápido, sin pérdida de calidad. (Cálculo) Dura 4% menos (24/25=0,96); sonido sube de tono.
- (Oficio, salvo lo citado) SD PAL 720×576; HD 1.280×720; Full HD 1.920×1.080; UHD/4K TV 3.840×2.160 (16:9); 4K DCI cine 4.096×2.160 (1,90:1); 8K 7.680×4.320.
- BT.709-6 (punto 2): HD 16:9, 1.920 muestras/línea activa, 1.080 líneas activas, píxel cuadrado. BT.2020-2: UHD 7.680×4.320 y 3.840×2.160, 16:9. BT.2100-3: +1.920×1.080, píxel cuadrado. (Oficio) UHD multiplica píxeles, no cambia 16:9.
- (Oficio) «4K» no es una cosa: 4K TV/UHD=3.840×2.160 (16:9); 4K cine/DCI=4.096×2.160 (no 16:9).
- BT.2100-3 nota 1b: producir a la resolución más alta posible y reducir después da mejor calidad que producir a la de entrega. (Oficio) Montar en UHD y entregar en HD > al revés.
- BT.709-6 5.8: luminancia a 148,5 MHz (50/P) y 74,25 MHz (50/I, 25/P); 5.9 nota 2: CB/CR a la mitad. 4.4: 1.920 muestras Y y 960 por diferencia de color/línea; 4.3: color co-situado con Y alternas→4:2:2.
- (Cálculo) 50 Hz: línea=2.640 muestras, 1.125 líneas; 2.640×1.125×50=148.500.000 (50/P); mitad, 74,25 M (50/I, 25/P).
- (Oficio) Muestreo cromático (bloque 4×2 píxeles): 4:4:4 sin submuestreo (grafismo, croma, cine digital) · 4:2:2 mitad horizontal (producción TV) · 4:2:0 mitad horiz.+vert. (emisión) · 4:1:1 (SD antiguo).
- BT.2100-3: 4:4:4 mismas muestras horiz. que Y'/I; 4:2:2 submuestreo ×2 horiz.; 4:2:0 ×2 horiz. y vert. (Oficio) Recorte sobre 4:2:0 va mal; incrustación pide 4:2:2 mínimo. 4ª cifra (4:4:4:4)=canal alfa: opacidad píxel a píxel, para superponer grafismo sin recortar a mano.
- (Cálculo) Bits: 8→256 niveles, 10→1.024, 12→4.096 (2^n). (Oficio) Más bits=menos banding; profundidad no crea rango dinámico (lo da el sensor) pero lo hace utilizable. Resolución espacial ≠ profundidad de color.
- BT.709-6 4.5: HD 8 o 10 bits/componente. BT.2020-2: UHD 10 o 12. BT.2100-3 tabla 9: HDR 10,12. (Oficio) HD admite 8 bits; UHD/HDR mínimo 10.
- BT.709-6 4.6/4.7: negro 16(8b)/64(10b); blanco pico 235/940; acromático CB/CR 128/512; extremos CB/CR 16-240/64-960; datos vídeo 1-254/4-1019; sincronismo 0 y 255/0-3 y 1020-1023.
- BT.2100-3 tabla 9: rango estrecho negro 64(10b)/256(12b), pico 940/3.760; completo negro 0, pico 1.023/4.095, no usar en intercambio salvo acuerdo. (Oficio) Negros hundidos/lavado tras otro programa=confusión estrecho/completo.
- R 103 v3.0 anexo 1, tabla 1 (nominal/preferente/total): 8b 16-235/5-246/1-254; 10b 64-940/20-984/4-1019; 12b 256-3760/80-3936/16-4079; 16b 4096-60160/1280-62976/256-65279.
- R 103: fuera de «preferred»=error de gama; superar «total»=recorte (clip); medidor avisa «out-of-gamut» sólo si error >1% de imagen. Directo: clippers al límite preferente; preproducido/gradeado: límites nominales.
- R 103: recorte→distorsión armónica y alias, más tasa de datos. Legalizadores automáticos: con cautela. Sub-negros no se recortan (impide alinear con PLUGE); analógico 0-700 mV.
- (Oficio, estudio) «−1%/103%» atribuidos a la EBU no están en R 103 v3.0: no atribuir. (Deducción R 103) Pieza montada/corregida se entrega en límites nominales, no preferentes.
- (Oficio) HDR=más recorrido de brillo, no más resolución. Nit=cd/m²; candela=intensidad (sin superficie); cd/cm²=10.000 nits; lumen=flujo total (proyector).
- BT.2100-3: HDR usa PQ o HLG. HLG: compatible con pantallas legacy. PQ: rango de brillo muy amplio para una profundidad de bits. (Oficio) PQ absoluta (código=luminancia fija, hasta 10.000 cd/m²; =ST 2084), máster/plataformas. HLG relativa (se adapta al pico), directo/emisión.
- BT.2100-3 nota 10a: blanco de referencia HDR=carta 100% reflectancia=203 cd/m² en PQ o en HLG con pico nominal 1.000 cd/m².
- BT.2408-9 tabla 1: grafismo blanco=nivel del blanco de referencia HDR. Gris 18%: 26 cd/m² (38%PQ/38%HLG); 83%: 162 cd/m² (56/71%); 90%: 179 cd/m² (57/73%); blanco ref./difuso/grafismo 203 cd/m² (58%PQ/75%HLG). (Oficio) Rótulo no va al 100%; por encima, brillos especulares.
- BT.2100-3 tabla 3: monitor crítico HDR pico ≥1.000 cd/m² (áreas pequeñas), negro ≤0,005 cd/m². (Oficio) SDR≈100 nits; etalonar HDR pide monitor HDR. Gama de color y rango dinámico son ejes distintos.
- (Oficio) Forma de onda: luminancia línea a línea (exposición). Vectorscopio: ángulo=tono, distancia=saturación, centro=sin color, cajas de 6 colores de barras; carta blanca balanceada cae en el centro. Histograma: reparto de niveles.
- (Oficio) Monitor de referencia: Blue only (croma/fase, ruido); Underscan (bordes); marcadores/zonas de seguridad; falso color y cebras. Señales de prueba: barras de color; rampa (diagonal recta, delata curvatura).
- (Oficio+R 103) 10 bits: negro <64 o blanco >940=fuera de nominal; >984 o <20=error de gama. Vectorscopio fuera de cajas=sobresaturado. HDR: blanco de rótulo HLG al 75%.
- (Oficio) SDI: 1 coaxial, vídeo+audio embebido+auxiliares en serie.
- ST 259:2008 SD-SDI: 10 bits, 143/270/360 Mb/s (uso 270 Mb/s). ST 292-1:2018 HD-SDI: 1,485 Gb/s o/1,001. ST 424:2012 3G-SDI: 2,970 Gb/s o/1,001. ST 2082-1:2023 12G-SDI: 11,88 Gb/s o/1,001 (activa; resto estabilizadas).
- ST 292-1: BNC 75 Ω. Codificación NRZI aleatorizada. Atenuación: ST 259 20-30 dB, ST 424 hasta 30 dB, ST 2082-1 hasta 40 dB (más velocidad, más atenúa, menos alcance).
- (Cálculo, BT.709-6) 4:2:2: 74,25 MHz×2×10b=1.485 Mb/s (HD-SDI); 148,5 MHz (1080p50)→2.970 Mb/s (3G-SDI); UHD 2160p50→11.880 Mb/s (12G-SDI). 1080i50/1080p25→HD-SDI; 1080p50→3G-SDI; 2160p50→12G-SDI o varios cables.
- (Oficio) Jitter=variación del instante de llegada de cada bit; ruido de fase. Receptor recupera reloj de la señal; si falla, corte, no degradación. UI=duración de un bit.
- ST 292-1 8.1.8: jitter medido según RP 184 (no leída); tabla 3: Timing jitter 1 UI desde 10 Hz; Alignment jitter 0,2 UI desde 100 kHz; borde >1/10 de la frecuencia de reloj; prueba con barras.
- (Remite) IP (ST 2110) y ficheros: tema 4. (Oficio) Sincronismo: equipos enganchados a referencia común. BT.709-6 parte 6: negro 0 mV, blanco 700 mV; CB/CR ±350 mV; tri-level bipolar; ±300 mV ±2%; sync en todos los componentes.
- (Oficio) Tres niveles: pulso baja bajo el borrado y sube por encima; punto medio=referencia de línea. Genlock y black burst: oficio, sin fuente leída.

## 2. La señal de audio

- (Oficio) Tono (frecuencia)=grave/agudo · Intensidad (amplitud)=fuerte/débil, dB · Timbre (armónicos)=qué instrumento. Margen audible 20-20.000 Hz, se estrecha con la edad.
- (Oficio) Armónicos=múltiplos enteros de la fundamental (440 Hz→880,1.320,1.760). Timbre=peso relativo de cada armónico; ecualizador lo cambia, no la nota.
- (Oficio) Digitalizar=medir muchas veces/s+anotar con un número. Muestreo fija frecuencia máxima conservada: 48 kHz TV, 44,1 kHz disco, 96 kHz música. Bits fija rango dinámico: 16 bits emisión, 24 producción. Canales: 2, 5.1, 5.1.4.
- (Oficio) Regla muestreo: >2× la frecuencia más alta (48 kHz cubre 20 kHz; 32 kHz pierde agudos). Regla profundidad: cada bit≈6 dB (16b≈96 dB, 24b≈144 dB). Sala: más profundidad, reducir al final.
- Tech 3250: interfaz primariamente a 48 kHz (CCIR 646). R 68-2000 (parecer EBU): codificación lineal, sin preénfasis, mínimo 16 bits (BS.646); nota 1: puede no bastar según el convertidor. PCM=audio lineal sin comprimir.
- (Cálculo) Caudal=frecuencia×bits: 48 kHz×24b=1,152 Mb/s/canal; estéreo 2,304 Mb/s; 16 canales=18,4 Mb/s. (Oficio) Escala completa: 0 dBFS=código más alto; lo que pasa se recorta.
- R 68-2000: alineación 18 dB bajo el máximo digital (cualquier bits); alineación 9 dB (u 8) bajo el máximo del programa; cuasipico: picos reales hasta 3 dB mayores, con error de operador hasta 6 dB (15 dB sobre alineación). (Oficio) Tono 1 kHz de barras al inicio → −18 dBFS.
- R 128-2023: objetivo −23,0 LUFS; ±1,0 LU si no alcanzable (directo), sin hacerse costumbre; ±0,2 LU por error de medida; recom. j: excepción sólo a la baja, avisada. Recom. m: pico ≤−1 dBTP en producción, tolerancia ±0,3 dB, salvedad de máximos menores por distribución.
- R 128-2023: medida del programa entero, medidor BS.1770/Tech 3341; incluye piezas cortas (remite a s1 y s2, no leídos); LUFS=LKFS. (Oficio) Pieza/promo: −23 LUFS, pico ≤−1 dBTP, corrección por ganancia no por recorte. Limpieza/mezcla: tema 7.
- Tech 3250 (AES3): 2 canales, hasta unos cientos de metros, 48 kHz. Subtrama=32 intervalos, 1 muestra/canal; trama=2 subtramas; bloque=192 tramas, preámbulo Z cada 192. (Cálculo) Trama=64 intervalos; 48 kHz→3.072.000 intervalos/s.
- (Oficio) Micrófono: impedancia no especificada. AES3/XLR 110 Ω. AES3id/coaxial 75 Ω.
- 272M-2004 (SD): mín. 2, máx. 16 canales (4 en compuesto digital); 20 bits por defecto, 24 opcional. ST 299-1:2009 (HD): hasta 16-32 canales a 32/44,1/48 kHz, hasta 8 a 96 kHz; 24 bits. ST 299-2:2010: canales 17-32, hasta 32 (32/44,1/48 kHz) o 16 (96 kHz); 24 bits.
- 272M: canales en pares, grupos de 4 con ID único. Grupo 1:1-4, 2:5-8, 3:9-12, 4:13-16, cada uno 2 pares AES/EBU; 16 canales=8 pares (cálculo).
- ST 299-1 1.4: audio en HANC del flujo Cb/Cr, control en HANC del Y. Embeber (embebedor)/desembeber (desembebedor).
- (Oficio) Montador: pistas SDI numeradas, reparto de cada casa; comprobar al ingestar/exportar. Reparto de CSRTV: no consta en documento publicado leído.

## 3. Vídeo y audio juntos: código de tiempo y sincronía

- (Oficio) TC=etiqueta que numera cada cuadro (h:m:s:cuadros); localiza puntos, sincroniza cámaras, referencia de montaje.
- (Oficio) NDF: cuenta todo, cadencia entera (24,25,30,50). DF: salta números para casar con el reloj de pared, cadencia no entera (29,97/59,94). TV 25 fps→NDF (entero, nada que corregir).
- (Oficio) DF nace del sistema americano (29,97 real, no 30): de 30 en 30 el TC se retrasa ≈3,5 s/h; DF corrige saltando números (sin tirar cuadros).
- (Cálculo, BT.709-6 30/1,001) 1 hora: 3.600×30/1,001≈107.892 cuadros; de 30 en 30 harían falta 108.000; diferencia ≈108 cuadros=3,6 s.
- (Oficio) Montador: TC de la secuencia fijado por su cadencia; 29,97 en secuencia de 25 no conserva TC cuadro a cuadro.
- 272M/ST 299-1: audio a 48 kHz (HD, también 96) enganchado al reloj de vídeo=preferido intraestudio; opción 32-48 kHz síncrono o asíncrono.
- (Cálculo) 48.000 muestras/s entre 25 cuadros=1.920 muestras/cuadro; entre 50=960; con /1,001 no sale entero.
- (Oficio) Desincronía: relojes distintos (grabador sin sincronizar, 44,1 kHz/secuencia 48 kHz)→desfase creciente, sincronizar/convertir; clip desplazado→desfase fijo, reenganchar; retardo de procesado/pantalla→labios desfasados con fichero correcto, medir la cadena.
- (Oficio) Casar imagen/sonido separados: TC común o referencia visible-audible a la vez (claqueta, palmada).
