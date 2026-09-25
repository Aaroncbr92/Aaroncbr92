# Tema 13 del específico de Operador/a de Sonido · Medición y sonoridad

**Siglas**: RTVA; CSRTV; UER/EBU; UIT/ITU-R; LUFS; LKFS; LU; dBFS; dBTP; LRA; PPM; QPPM; VU; PML.

Esqueleto para repasar, no resumen: cada línea remite al dato del tema, no lo sustituye.

<!-- indice --><!-- /indice -->

## LUFS

- Peak normalisation → quejas de público (EBU R 128, considerandos).
- QPPM de Tech 3205-E no refleja sonoridad (R 128, considerandos).
- R 128: sonoridad media normaliza; pico verdadero controla techo (R 128).
- Algoritmo de sonoridad y pico verdadero: UIT-R BS.1770-5 (11/2023), no la UER.
- Anexo 1 BS.1770: hasta 5 canales (BS.775); anexo 3, BS.2051; anexo 4, objetos.
- 4 etapas (BS.1770 anexo 1): ponderación K; media cuadrática por canal; suma ponderada (LFE excluido); puerta bloques 400 ms, solape 75 %, umbrales −70 LKFS y −10 dB relativo.
- Ponderación K = filtro de estantería (cabeza como esfera rígida) + paso alto RLB (BS.1770).
- Pesos canales (tabla 3 BS.1770): L/C/R = 1,0 (0 dB); envolventes = 1,41 (~+1,5 dB); LFE excluido (fuera de tabla 3, en descripción de etapas).
- Envolventes pesan más: percepción trasera más fuerte (Tech 3343).
- Medida = estimación, con incertidumbre; no válida para tonos puros (BS.1770).
- LUFS = LKFS (R 128 nota 1); UER usa LUFS, UIT usa LKFS.
- LUFS = absoluto; LU = relativo (1 LU = 1 dB) (Tech 3341; BS.1770).
- Tono 0 dBFS 997 Hz en un canal frontal → −3,01 LKFS (BS.1770); constante −0,691 cancela ganancia K a 997 Hz.

## EBU R 128

- R 128: recomendación UER (no AES), V5 noviembre 2023.
- Objeto: normalización de sonoridad + nivel máximo permitido (R 128, título).
- Historial: V1 feb-2010; V2 ago-2011 (puerta relativa −8→−10 LU); V3 jun-2014 (tolerancia ±0,5 LU salvo directo); V4 ago-2020; V5 nov-2023 (referencias a s3/s4/Tech 3401). Vigente: V5.
- BS.645 (PML antiguo) ya no adecuado (R 128, considerandos).
- Punto h) objetivo: −23,0 LUFS; tolerancia ±1,0 LU si no alcanzable en la práctica (p. ej. directo).
- Punto i) tolerancia de medida: ±0,2 LU (errores de medida).
- Punto m) pico verdadero: ≤−1 dBTP en producción (audio lineal); tolerancia de medida ±0,3 dB (ancho ≤20 kHz).
- Punto k) medidor: conforme BS.1770 (puerta ec. 7) + Tech 3341.
- Punto n) LRA: según Tech 3342; nota 2, no recomendado en programas <1 min.
- Punto j): objetivo más bajo a propósito debe indicarse para no compensarlo.
- Punto l): se mide el programa entero, sin énfasis en voz/música/efectos.
- Punto m) final: techos más bajos según sistema de distribución (ver Tech 3344).
- Punto p): metadatos deben indicar la sonoridad real.
- «Programa» incluye publicidad, promos, cortinillas («Short-form Content», R 128 definiciones).
- Tolerancia directo ±1 LU = objetivo no alcanzable en la práctica; sonoridad integrada no se conoce hasta el final (R 128 h).
- Deportes: comentaristas algo por debajo (p. ej. −24 LUFS) para dar margen al público (Tech 3343 § 3.5.1).
- Dato clave a examen: −23 LUFS, ±1 LU directo.
- Familia de documentos (sólo constan por la R 128, no desarrollados aquí): Tech 3344 (distribución); R 128 s1 (contenido corto); s2 (streaming); s3/Tech 3401 (radio); s4 (cine).

## Picos

- 0 dBFS = máximo digital absoluto; por encima, recorte.
- Pico de muestra: valor de la muestra más alta, en dBFS.
- Motivos del pico verdadero (BS.1770, considerandos): sobrecarga abrupta digital; el pico puede subir con filtrado o reducción de bit-rate; la métrica clásica no refleja el pico entre muestras.
- R 128 define Maximum True Peak Level: máximo de la onda en tiempo continuo; unidad dBTP.
- Cálculo (BS.1770 anexo 2): 1) atenuación 12,04 dB (2 bits) si aritmética entera, no necesaria en coma flotante; 2) sobremuestreo ×4 (48→192 kHz), ×2 si entrada a 96 kHz; 3) filtro paso bajo, valor absoluto, compensación de 12,04 dB, resultado en dBTP.
- Infralectura ~0,5 dB (sobremuestreo ×4, 48 kHz); margen de 1 dB bajo 0 dBFS recomendado (Tech 3343).
- −1 dBTP es «during production (linear audio)»; con reducción de datos el pico sube.
- Tech 3343: MPEG-1 Layer 2 y Dolby AC-3 → límite recomendado −2 dBTP.
- Herramienta que impone el techo: limitador de pico verdadero (tema 5).
- Vúmetro: promedio, agujas ~300 ms (prensa técnica, Sound On Sound).
- PPM UER (QPPM, Tech 3205-E, 1979, sustituida): integración nominal 10 ms (±2 ms); caída +12→−12 en 2,8 s (±0,3 s) modo normal, 3,8 s (±0,5 s) modo lento; escala 12 divisiones de 2 dB; marca «Test» 9 dB bajo el máximo (C.C.I.T.T.); CEI reconoce tipos I, IIa, IIb (IIb = medidor UER estándar); ráfaga 5 kHz continua marca +9, en tiempo de integración marca +7.
- R 68: picos reales pueden ser 3 dB mayores que lo indicado por el cuasipico.
- Alineación (R 68): −18 dBFS bajo el máximo, 18,06 dB (1:8), independiente del número de bits.
- Tech 3343 § 8.1: tono 1 kHz a −18 dBFS para alinear la cadena.
- PML de −9 dBFS (BS.645) obsoleto con el paso a −1 dBTP (Tech 3343 § 8.1); la alineación −18 dBFS NO cambia.
- Tono se alinea con medidor de pico, no de sonoridad (Tech 3343).

## Loudness: el medidor de sonoridad

- Medidor exigido por R 128: definido en Tech 3341, «modo EBU».
- Tres lecturas (Tech 3341 § 2.1): Momentánea (M), Corto plazo (S), Integrada (I).
- M: ventana deslizante 0,4 s, sin puerta.
- S: ventana deslizante 3 s, sin puerta.
- I: todo el programa/tramo medido, CON puerta (BS.1770).
- Uso de oficio: M = instante; S = tendencia (mezcla); I = cifra que se entrega (−23 LUFS).
- Actualización mínima (Tech 3341 § 2.2): S ≥10 Hz; I ≥1 Hz, en medidores en directo.
- Medidor debe permitir start/pause/continue simultáneo de I y LRA, y reset conjunto en cualquier estado.
- Medidor debe mostrar máximos de M y de S (Tech 3341 § 2.1) → punto o) de R 128.
- Puerta de la integrada (Tech 3341 § 2.3): umbral absoluto −70 LUFS; umbral relativo −10 LU bajo la sonoridad absoluta-puerteada; bloques 400 ms, solape 75 %.
- Proceso: mide con bloques >−70 LUFS → resta 10 → umbral relativo → integrada final sólo con bloques que superan ese relativo.
- Umbral relativo era −8 LU hasta V2 de R 128 (2011), cambiado a −10 LU.
- M y S: SIN puerta; I: CON puerta (dos umbrales). Trampa de examen: −70/−10 LU no son puerta de la S.
- Escalas (Tech 3341 § 2.7): EBU +9 (−18 a +9 LU / −41 a −14 LUFS), por defecto; EBU +18 (−36 a +18 LU / −59 a −5 LUFS), material de mucha dinámica.
- Cero de la escala relativa = objetivo −23,0 LUFS = 0,0 LU (Tech 3341); unidad LUFS/LU siempre visible.
- Conversión: −20 LUFS = +3 LU; −26 LUFS = −3 LU (cálculo).
- LRA (Tech 3342): cuantifica variación de sonoridad en el tiempo; sobre ventana de 3 s (lectura S).
- Cálculo LRA: puertas −70 LUFS (absoluta) y −20 LU relativa (distinta de la integrada, que usa −10 LU); LRA = diferencia entre percentiles 10 y 95.
- Percentil 10 bajo evita que un fade-out domine el LRA; percentil 95 evita que un pico aislado lo dispare.
- LRA sirve para evaluar variación, tratamiento dinámico potencial e integridad dinámica de la distribución (R 128).
- LRA alto = mucha diferencia floja/fuerte; LRA bajo = programa comprimido (oficio). No recomendado <1 min (pocos datos).
- Compresión y sonoridad (oficio): comprimir sube sonoridad sin subir pico; con R 128 no da ventaja de volumen (hay que bajar el conjunto); sí gana consistencia (LRA mide el efecto).

## Fases

- Fase, polaridad, filtro en peine: tema 1.
- Correlador de fase (RTW): compara dos canales estéreo; determina compatibilidad mono; puede revelar mala colocación de micrófonos.
- Escala correlador: lineal de −1 (polaridad invertida) a 0 (sin relación) a +1 (idéntica) (RTW).
- Lectura +1: idénticos, suma limpia (mono de hecho). Entre 0 y +1: compatible. 0: sin refuerzo ni cancelación. Bajo 0 hacia −1: cancelación al sumar a mono.
- Referencia de fabricante (no norma): mezclas estéreo normales entre 0,3 y 0,7 (RTW).
- Multicanal: correlador múltiple comprueba que la mezcla suene bien en downmix a estéreo/mono (RTW); downmix y compatibilidad → tema 14.
- Aplicación práctica (oficio): lectura negativa estable en fuente que debería ser mono → cable/conexión/canal con polaridad invertida; se comprueba invirtiendo un canal y viendo si pasa a +1. Oscilación negativa en pareja estéreo → mala colocación (retardo distinto entre micrófonos, tema 3). Prueba definitiva: escuchar suma en mono.
- Goniómetro/vectorscopio (RTW): muestra relación de fase cambiante entre par de canales; figura Lissajous, girada 45° antihorario respecto a ejes L/R; lleva AGC.
- Lectura goniómetro (RTW): línea vertical = mono doble (mismo nivel en los dos canales); línea horizontal = polaridad invertida (180°) en un canal; inclinación 45° a un lado = señal sólo en ese canal, imagen desequilibrada; madeja equilibrada = mezcla estéreo normal («ball of wool»), su dispersión informa de la anchura estéreo.
- Fase y sonoridad: BS.1770 calcula media cuadrática por canal ANTES de sumar con peso → tono con polaridad invertida en un canal marca igual que en fase; contrafase NO se ve en el medidor de sonoridad, sí en correlador/goniómetro/suma a mono.
- Tech 3343 § 8.1: tono de alineación −18 dBFS (1 kHz) en fase en ambos canales L/R (estéreo o envolvente) marca −18 LUFS (+5 LU en escala relativa).
- Cálculo: tono 1 kHz −18 dBFS en los dos canales en fase → −18 LUFS (+5 LU, −18−(−23)). En un solo canal → unos −21 LUFS (−18−3,01).
## Control de calidad

- R 128 tolerancia de medida ±0,2 LU explícita para flujos de sonoridad, p. ej. entornos de control de calidad (R 128, punto i).
- Programa grabado a QC: −23 LUFS objetivo; con tolerancia de medida (±0,2 LU, punto i), aceptable entre −23,2 y −22,8 LUFS (cálculo).
- QC comprueba también: medida entera, sin atender sólo voz/música (punto l); medidor conforme BS.1770 + Tech 3341, con puerta (punto k); pico verdadero ≤−1 dBTP, tolerancia ±0,3 dB (punto m), o techo más bajo del sistema de distribución; si va bajo −23 LUFS a propósito, debe indicarse (punto j).
- Metadatos Dolby AC-3 (Tech 3343 § 6): dialnorm (sonoridad declarada), dynrng (rango dinámico), Centre/Surround Downmix Level.
- Dialnorm describe la sonoridad de todo el programa (voz+música+efectos), salvo cuando se normaliza sobre el diálogo como ancla.
- Con R 128, dialnorm debe indicar −23 LUFS (Tech 3343 § 6.1); tres excepciones: archivo no reajustable a tiempo; directo externo con otra sonoridad; sistemas donde el metadato viaja fiel hasta el receptor.
- R 128 punto p): metadatos deben indicar correctamente la sonoridad real del programa.
- Valores sospechosos en Dolby Digital (Tech 3343 § 6): −27 dialnorm = valor de fábrica; −31 = mínimo posible del sistema → probable que nadie haya medido.
- Recomendación Tech 3343: descartar metadatos de sonoridad/rango dinámico de fuentes externas salvo fuente totalmente fiable; volver a medir.
- Lista de comprobación QC (oficio, sobre cifras citadas): 1) medidor modo EBU, BS.1770+Tech 3341, escala EBU +9/+18, objetivo −23 LUFS=0 LU; 2) integrada de principio a fin, −23 LUFS (±0,2 LU medida) o ±1 LU si directo; 3) pico verdadero ≤−1 dBTP lineal, ≤−2 dBTP si MPEG-1 Layer 2/AC-3; 4) máximos M y S sin molestar aunque la integrada cumpla; 5) LRA si dura >1 min, coherente con tipo/destino; 6) fase: correlación positiva y escucha en mono; 7) metadatos coincidentes con la medida, desconfiar de −27/−31; 8) material externo: remedir, no fiarse de sus metadatos.
- Corrección: diferencia de ganancia en dB mueve la integrada en igual cantidad de LU (cálculo).
- Ejemplo 1: programa a −20 LUFS con picos −3 dBTP → baja 3 dB → −23 LUFS, picos −6 dBTP.
- Ejemplo 2: programa a −26 LUFS con picos −2 dBTP → necesita +3 dB, pero picos llegarían a +1 dBTP → hay que limitar antes de subir.
- Ninguna norma legal regula la sonoridad en las fuentes leídas: recomendaciones técnicas, fabricante, prensa técnica y oficio.
