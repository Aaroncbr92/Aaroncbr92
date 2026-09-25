# Tema 2 del específico de Operador/a de Sonido · Electricidad y electrónica aplicada al audio

**Siglas**: RTVA, CSRTV, CC/DC, CA/AC, V/A/Ω/W/F, Hz, dBu, dBV, dBFS, dB SPL, THD, S/N, RFI, AES/AES3, IEC, XLR, TRS/TS, P48/P12, DI, VU, PWM, EMC/EMI, CMRR, EBU, MADI, SDI.

Esqueleto para repasar, no resumen: cada línea lleva delante la fuente o el precepto que la sostiene.

<!-- indice --><!-- /indice -->

## Base eléctrica

- RD 2032/2009, cap. II: V (tensión), A (intensidad), Ω (resistencia), W (potencia), unidades legales; F (faradio) = C/V.
- Oficio: ley de Ohm — V=I×R, I=V/R, R=V/I; P=V×I=I²R=V²/R.
- Oficio: red europea, 230 V CA, 50 Hz; América, 60 Hz; zumbido de red a 50 Hz delata alimentación o masas.
- Oficio: diferencial compara activo/neutro, corta por fuga a tierra, protege personas; magnetotérmico corta por sobrecarga (térmico) o cortocircuito (magnético).
- Oficio, clases de amplificador: A, 360º, mínima distorsión, bajo rendimiento; B, 180º, distorsión de cruce; AB, algo más de 180º, la mayoría de etapas lineales; C, menos de 180º, sólo radiofrecuencia; D, conmutada, máximo rendimiento.
- Texas Instruments: clase AB, rendimiento teórico máx. 78 %, real 30-40 %; clase D hasta 90 %, salida PWM filtrada a audio.

## Niveles

- Oficio: nivel = tensión en dB sobre referencia; 20×log(V/Vref); ×2 tensión ≈+6 dB, ×10 ≈+20 dB.
- Rane 169: dBu, ref. 0,775 V eficaces (de 0 dBm sobre 600 Ω); valor eficaz, no de pico.
- Rane 169: dBFS, ref. escala completa digital; valores de pico, siempre negativos; AES-2id-2006 sitúa una senoide a escala completa en +3 dBFS.
- Oficio: dBV, ref. 1 V eficaz; dB SPL, ref. 20 µPa (umbral de audición).
- Rane 135: nivel medio profesional +4 dBu (0 VU); doméstico a menudo −10 dBV; máximo seguro profesional +20 dBu; máximo de proceso +26 dBu; suelo de ruido ≈−94 dBu; rango dinámico 120 dB.
- DPA: sensibilidad de micrófono, mV/Pa o dBV/Pa a 1 kHz (1 Pa = 94 dB SPL); ej. 10 mV/Pa = −40 dBV/Pa.
- DPA: 150 dB SPL de pico con mics de 1 y 10 mV/Pa da 0,63 y 6,3 V de pico: va a entrada de línea o con atenuador.
- Rane 135: headroom = máximo sin distorsión menos nivel medio (+4 a +26 dBu = 22 dB).
- Rane 169: factor de cresta = pico/eficaz; senoide 1,4 (3 dB); música 4-10 (12-20 dB); cuadrada, 1 (0 dB).
- Crown: sensibilidad de entrada de etapa, posiciones 0,775 V (0 dBu) y 1,4 V (≈+5 dBu); no cambia la potencia disponible.
- Cálculo: +4 dBu ≈1,23 V eficaces.
- Rane 135: la ganancia se toma de una vez en el previo de micrófono, no repartida en varias etapas.
- Rane 124: salida balanceada activa da a veces 6 dB más que desbalanceada (no en transformador ni cruzada); remedio, bajar 6 dB el nivel.

## Impedancias

- Oficio: resistencia, continua y alterna, sólo el conductor; reactancia, sólo alterna, capacidad e inductancia; impedancia, ambas, depende de la frecuencia; el valor de fabricante es nominal.
- Rane 124: hoy se transfiere tensión, no potencia; salida baja (≈100 Ω) contra entrada alta (≈20 kΩ), pérdida ≈−0,04 dB; adaptar (100 Ω/100 Ω) pierde 6 dB; «impedance matching is not necessary and creates many ills».
- DPA: carga de micrófono, 5-10 veces su impedancia; entrada con phantom, 3,4 kΩ.
- Rane 110: la DI convierte alta impedancia/nivel de instrumento a baja impedancia/nivel de micrófono y desbalanceado a balanceado.
- Cálculo: 3 altavoces de 8 Ω, en serie 24 Ω, en paralelo 2,67 Ω (1/Z=Σ1/Zi); a menor impedancia, más corriente entrega la etapa.
- Crown: factor de amortiguamiento = impedancia del altavoz / impedancia de salida de la etapa; cable largo y fino lo empeora.
- Oficio/cálculo: pérdida en cable ∝ I²×R; a menor impedancia de carga, más corriente, más pérdida; la línea de 100 V sube tensión, baja corriente, reduce pérdida.
- Cables: de micrófono, impedancia no especificada (analógico); AES3 sobre XLR, 110 Ω; AES3id coaxial y SDI, 75 Ω; digital exige adaptación por reflexiones.
- Oficio: el multímetro mide resistencia en continua, no impedancia real; el valor por frecuencia exige puente de impedancias o analizador.

## Balanceado

- Rane 151/Crown: XLR, pin 1 malla, pin 2 vivo (hot, en fase), pin 3 retorno (cold, contrafase); AES fija «pin 2 is hot»; TRS, punta=vivo, anillo=retorno, cuerpo=malla; TS, sin retorno, desbalanceado.
- Rane 110: par trenzado + resta en el receptor cancela la interferencia igual en ambos conductores («always use twisted pair»).
- DPA: CMRR mide el rechazo de ruido en modo común, sólo con líneas balanceadas; depende de igualdad de impedancias en emisor, cable y receptor («the weakest link determines the final result»); más dB, mejor; ejemplo de fabricante, ≈65 dB.
- Oficio: pines 2/3 cruzados invierten la polaridad de ese canal, cancelación parcial al sumar.
- DPA: invertir polaridad = multiplicar por −1, sin retardo; desfasar exige retardo; tras invertir, la señal queda a 180°; botón rotulado φ/Ø.
- DPA: en condensador profesional, presión creciente da tensión positiva creciente en pin 2 (dinámicos, distinto).
- Rane 110: balanceado y desbalanceado no son compatibles directamente; remedio, transformador de aislamiento o cableado especial (DI).

## Masa

- Oficio: tierra de protección (persona), masa de chasis (caja) y masa de señal (0 V del circuito); la malla une masas entre equipos.
- Rane 110: bucle de masa, dos caminos de unión entre masas (malla + tierra/rack) forman un lazo; el zumbido aparece cuando esa corriente pasa por la masa de señal; con balanceado bien hecho no se oye.
- Rane 110 (cita AES48-2005, no leída): el pin 1 va al chasis, no a la masa de señal.
- Rane 151: «problema del pin 1» — malla a masa de señal, la corriente inducida modula el audio; masa de señal en un único punto (masa en estrella); unión masa-chasis en un solo sitio.
- Remedios (Rane 110/151): nunca quitar la tierra de protección; el ground lift es un parche, pocas veces mejora; el transformador de aislamiento, la mejor solución para balanceado/desbalanceado; si se levanta la malla en un extremo, dejar un condensador como paso de radiofrecuencia; equipos con alimentador externo, chasis a tierra aparte.

## Ruido

- Oficio: tres orígenes — circuito propio (soplido constante; estructura de ganancia y equipos de menos ruido), red por bucle/inducción (zumbido 50 Hz; masas y balanceado), radiofrecuencia y equipos ruidosos (reguladores de luz, fluorescentes; balanceado, par trenzado, separar cableado).
- Rane 135: suelo de ruido = mínimo que el equipo puede entregar; S/N = distancia entre nivel de trabajo y suelo; rango dinámico = distancia entre máximo y suelo.
- DPA: ruido propio del micrófono = SPL equivalente al autorruido eléctrico; buen resultado, menos de 15 dB(A).
- Oficio: ruido, señal ajena al programa, existe sin programa; THD, armónicos añadidos que no estaban; intermodulación, sumas/diferencias de frecuencias presentes; distorsión por transitorios, fallo ante cambios rápidos (velocidad, no nivel); recorte, señal que excede el margen.

## Alimentación phantom

- DPA/Schoeps: phantom, alimentación en continua por el mismo cable balanceado, vía XLR-3, regulada por IEC 61938:2018 (texto no leído); DIN 45 596, norma anterior; inventada por Neumann en 1966 para NRK.
- DPA: pines 2 y 3, +48 V ±4 V CC; pin 1, 0 V; nombre P48; corriente nominal 7 mA, máxima 10 mA; entrada con phantom, 3,4 kΩ.
- Schoeps: se inyecta por dos resistencias iguales por canal, con el polo negativo a masa.
- DPA/Schoeps: tensiones menores, 12 o 24 V; P12 de Schoeps, 12 V, con mayor corriente.
- DPA: con tensión menor de la esperada, el micrófono admite menos SPL máximo y distorsiona más.
- DPA: «fantasma» porque la tensión es igual en pines 2 y 3; un dinámico no la «ve»; la entrada balanceada tampoco la deja pasar al audio.
- Schoeps/DPA: segura para dinámicos bien cableados; riesgo con cableado defectuoso o conexión en caliente; nunca a micrófonos o cables desbalanceados (cinta); buena práctica, conectar con la phantom apagada; en reparto a varias mesas, sólo una la da.
- Oficio: alimentación A-B (Tonader), 12 V con polaridad opuesta entre 2 y 3 (no igual como la phantom); sí puede dañar un dinámico; para micrófonos de reportaje de sistemas antiguos.
