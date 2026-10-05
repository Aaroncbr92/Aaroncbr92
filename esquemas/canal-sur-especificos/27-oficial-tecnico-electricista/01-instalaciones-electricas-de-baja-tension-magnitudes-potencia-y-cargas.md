# Tema 1 del específico de Oficial Técnico Electricista · Instalaciones eléctricas de baja tensión: magnitudes, corriente alterna, potencia, energía, factor de potencia, caída de tensión y equilibrado de cargas

**Siglas**: RTVA, CSRTV, REBT (RD 842/2002), ITC-BT, CA/CC, Un, RMS, L1-L2-L3, N, UNE, EN, SAI; U, I, R, ρ, γ, X, Z, P, Q, S, E, φ, cos φ, f, T, e/ΔU; V, A, Ω, S, H, F, Hz, W, VA, var, kVA, kvar, J, kWh, mm².

Esqueleto para repasar, no resumen: cada línea lleva su fuente.

<!-- indice -->
<!-- /indice -->

## 1. Instalaciones eléctricas de baja tensión
- REBT 2.1 (vigente 01/07/2021): CA ≤ 1.000 V; CC ≤ 1.500 V (nominales)
- Art. 4.1: CA valor eficaz; CC valor medio aritmético. Muy baja CA ≤ 50 / CC ≤ 75; usual 50-500 / 75-750; especial 500-1.000 / 750-1.500. 230/400 V = usual
- Art. 4.2: 230 V entre fases (3 conductores); 230 fase-neutro y 400 entre fases (4 conductores). Art. 4.4: 50 Hz
- Art. 4.5: otras tensiones/frecuencias con autorización motivada del órgano competente (necesidad, sin perturbaciones, sin menoscabo de seguridad)
- 400 = 230·√3 ≈ 398: geometría, no norma
- Art. 16.1: interiores o receptoras = finalidad principal utilizar la energía; incluye intemperie. Art. 16.2: equilibrio (8). ITC-BT-19: caída (7), equilibrado (8)

## 2. Magnitudes eléctricas
- Oficio: U voltio; I amperio; R ohmio; C culombio (1 A = 1 C/s); G = 1/R siemens; ρ Ω·mm²/m; γ = 1/ρ; P vatio; E julio o kWh
- Ohm: U = R·I; I = U/R; R = U/I. Tensión fija, R se elige, la corriente dimensiona cable e interruptor
- Serie: R = ΣRi, se reparte la tensión. Paralelo: 1/R = Σ1/Ri, se reparte la corriente. Receptores en paralelo; línea en serie
- Kirchhoff 1ª: Σ entran = Σ salen (10+4−6 = 8 A); 2ª: Σ fem = Σ caídas (230−6 = 224 V). En CA, valores instantáneos o vectorial
- R = ρ·L/S: crece con L, baja con S; Cu mejor que Al (Al más sección); ρ sube con la temperatura
- ITC-BT-19, 2.2.1: cobre o aluminio, siempre aislados salvo sobre aisladores (ITC-BT-20)
- Joule: P = R·I²; doble corriente = 4× calor; calentamiento limita intensidad admisible (tema 4)

## 3. Corriente alterna
- CC: valor y sentido constantes (pilas, baterías, rectificadores, fotovoltaica; no transformable directamente). CA: senoide, se invierte cada semiperiodo (alternadores; transformador por inducción)
- Elevar tensión = menos corriente = menos pérdidas (I²). Centro RTV: red CA, equipos en CC (fuentes conmutadas, SAI): corrientes deformadas
- u(t) = Umáx·sen(ωt), ω = 2πf. Pico; pico a pico = 2×; medio = 0 en ciclo; eficaz = mismo efecto calorífico que CC; T; f = 1/T
- Eficaz = máx/√2 (sólo senoide pura; verdadero valor eficaz, tema 14). 230 V: pico ≈ 325; pico a pico ≈ 650; T = 20 ms; ω ≈ 314 rad/s; 100 inversiones/s. Aislamientos por el pico
- Resistencia: en fase. Bobina XL = 2πfL, corriente retrasada 90°. Condensador XC = 1/(2πfC), adelantada 90°. XL crece con f, XC baja
- 50 Hz: 0,1 H = 31,4 Ω; 100 µF = 31,8 Ω. Z = √(R²+X²), X = XL−XC; I = U/Z; cos φ = R/Z
- Inductivo: motores, transformadores, reactancias. Capacitivo: batería sobredimensionada, cables largos en vacío. Resistivo cos φ = 1: calefacción, incandescentes
- Trifásico: 3 tensiones, misma amplitud y f, desfase 120°. Razones: más potencia con menos cobre; potencia instantánea constante; campo giratorio
- Estrella: U línea = √3·U fase; I línea = I fase. Triángulo: U línea = U fase; I línea = √3·I fase. Estrella: √3 menos tensión, potencia 3 veces menor (arranque estrella-triángulo)
- Neutro: punto común de la estrella; 230 y 400 V; por él circula el desequilibrio
- ITC-BT-19, 2.2.4: neutro azul claro; protección verde-amarillo; fases marrón o negro; tres fases, también gris

## 4. Potencia
- CC: P = U·I. Monofásica: P = U·I·cos φ (W); Q = U·I·sen φ (var); S = U·I (VA)
- Trifásica (U entre fases, I de línea): P = √3·U·I·cos φ; Q = √3·U·I·sen φ; S = √3·U·I
- S² = P²+Q²; cos φ = P/S; tg φ = Q/P. Contador mide activa; S fija la corriente: transformadores, grupos y SAI en kVA (10 kVA ≠ 10 kW salvo cos φ = 1)
- I mono = P/(U·cos φ); I tri = P/(√3·U·cos φ)
- Ej. mono: 4.600 W, 230 V, 0,8 = 25 A; S = 5.750 VA; Q = 3.450 var. Ej. tri: 20 kW, 400 V, 0,85 = ≈ 34 A; S ≈ 23,5 kVA; sen φ ≈ 0,527; Q ≈ 12,4 kvar. Mono 230 V: ≈ 102 A (3×)
- Boucherot: suman P y Q (+ inductiva, − capacitiva); S no se suma. 10 kW (0,8) + 5 kW (1): P = 15; Q = 7,5; S ≈ 16,8 kVA (no 17,5); cos φ ≈ 0,89

## 5. Energía
- E = P·t; julio = W·s; 1 kWh = 3.600.000 J = 3,6 MJ. Potencia (kW) se contrata, limita interruptor; energía (kWh) se gasta, la registra el contador
- Activa kWh; reactiva kvarh (su relación da el cos φ medio). Ej.: 20 kW × 10 h = 200 kWh; SAI 3 kW × 24 h = 72 kWh/día más pérdidas
- η = P útil / P absorbida < 1: 3 kW con 0,9 absorbe 3,33 kW; 0,33 kW de calor a evacuar con climatización

## 6. Factor de potencia
- FP = P/S; senoidal = cos φ (0 a 1); 1 resistiva; inductivo (retraso) o capacitivo (adelanto)
- cos φ bajo: más corriente, más caída y pérdidas, más sección y aparamenta, menos P disponible en transformador, grupo o SAI
- No senoidal (conmutadas, variadores, alumbrado electrónico): FP ≠ cos φ; condensadores corrigen desfase, no deformación (tema 14)
- Qc = P·(tg φ1 − tg φ2). Ej.: 20 kW, 0,85 a 0,95: tg 0,620 y 0,329; Qc ≈ 5,8 kvar; I de 34 a ≈ 30,4 A
- Q = U²·ω·C; tres condensadores, un tercio cada uno. Triángulo (400 V): C = Qc/(3·400²·ω) ≈ 38 µF/fase. Estrella (230 V): C = Qc/(3·230²·ω) ≈ 115 µF (triple). Se conectan en triángulo
- Individual (más tramo descargado), por grupos, global en cabecera automática por escalones (menos condensadores)
- ITC-BT-43, 2.7: «podrán ser compensadas», sin que la energía absorbida sea capacitiva en ningún momento
- ITC-BT-43, 2.7: por receptor o grupo simultáneo con un solo interruptor que corte receptor y condensador; o global automática, variación ≤ ± 10 % del valor medio de un prolongado período
- ITC-BT-43, 2.7: condensadores separables por interruptores: resistencias o reactancias de descarga a tierra; los de motores asíncronos se desconectan a la vez que el motor; UNE-EN 60831-1 y -2 (no leídas)
- ITC-BT-44, 3.1: lámparas de descarga: compensación obligatoria, mínimo 0,9; no en conjunto con carga variable salvo sistema automático que siga la carga
- ITC-BT-44, 3.2: condensadores de balastos: resistencia, ≤ 50 V a los 60 s de la desconexión
- ITC-BT-09, 3 y 8: alumbrado exterior: compensación individual en cada punto de luz, ≥ 0,90
- ITC-BT-48, 2.3: sin temperatura máxima indicada, no usar con ambiente ≥ 50 ºC; carga residual peligrosa: descarga automática o inscripción; dieléctrico líquido combustible = como reostatos y reactancias
- ITC-BT-48, 2.3: > 2.000 m de altitud, precauciones con el fabricante (UNE-EN 60831-1); protegidos si sobreintensidad > 1,3 veces la de tensión asignada a frecuencia de red (sin transitorios)
- ITC-BT-48, 2.3: mando y protección soportan en permanente de 1,5 a 1,8 veces la intensidad nominal (armónicos, tolerancias)

## 7. Caída de tensión
- Tensión perdida en el conductor (R en serie). Excesiva: menos tensión y potencia; motor pierde par (cuadrado de la tensión); descarga puede no arrancar; calor perdido
- Sección = la mayor de calentamiento (tema 4) y caída (corriente y longitud): cortas manda calentamiento; largas, caída
- ITC-BT-19, 2.2.2: caída entre origen de la interior y cualquier punto de utilización, % de Un: viviendas 3 %; otras 3 % alumbrado, 5 % demás usos (3 % de 230 = 6,9 V; 5 % de 400 = 20 V)
- ITC-BT-19, 2.2.2: con todos los aparatos susceptibles de funcionar simultáneamente (número según reglamento o, si no, usuario con utilización racional); compensable con la derivación individual: total < suma de límites
- ITC-BT-19, 2.2.2: industrial en AT con transformador propio: origen en la salida del transformador; 4,5 % alumbrado, 6,5 % demás.
- ITC-BT-14, línea general: contadores totalmente centralizados 0,5 %; centralizaciones parciales 1 %
- ITC-BT-15, derivación individual: contadores en más de un lugar 0,5 %; totalmente concentrados 1 %; único usuario sin línea general 1,5 % (más interior 3 % / 5 %, compensables)
- ITC-BT-09, 3: alumbrado exterior ≤ 3 % entre origen y cualquier punto
- Mono e = 2·L·I·cos φ/(γ·S); tri e = √3·L·I·cos φ/(γ·S) (V, m, mm²). Con potencia: mono 2·P·L/(γ·S·U); tri P·L/(γ·S·U); U 230 mono, 400 tri; e % = 100·e/U
- Sección: mono S = 2·L·I·cos φ/(γ·e); tri S = √3·L·I·cos φ/(γ·e). El 2 = ida y vuelta; √3 = composición vectorial, caída entre fases
- S ∝ L; S ∝ I; S ∝ 1/e (mitad de caída, doble sección); a igual P, trifásico menos cobre
- Simplificadas: sólo R, sin reactancia; γ depende de la temperatura (a ambiente, sección menor); el REBT no da γ
- Ej. (γ = 48 supuesto): 20 kW, 100 m, 16 mm², 34 A: e ≈ 6,5 V = 1,6 % (cumple 5 %). Alumbrado 10 A, 230 V, cos φ 1, 40 m, 3 % (6,9 V): S ≈ 2,4 = 2,5 mm² (y calentamiento); L máx en 2,5 mm² ≈ 41 m
- ITC-BT-47, 3: conexión de motores dimensionada contra calentamiento excesivo. 3.1: un motor, 125 % de plena carga. 3.2: varios, 125 % del mayor + plena carga de los demás (20, 10, 8 A = 43 A)
- ITC-BT-44, 3.1: circuitos para receptores, asociados, armónicas y arranque; descarga: carga mínima 1,8 veces los W (en VA); monofásica: neutro = fase; otro coeficiente si cos φ ≥ 0,9 y se conocen asociados y arranque. Ej.: 20 × 36 W = 720 W = 1.296 VA ≈ 5,6 A
- ITC-BT-09, 3: alumbrado exterior descarga: 1,8 veces en VA (armónicas, arranque, desequilibrio de fases); otro coeficiente calculado si se conocen

## 8. Equilibrado de cargas
- Art. 16.2: «se alcanzará el máximo equilibrio»; subdividir para que averías afecten a mínima parte, localizarlas y controlar el aislamiento
- ITC-BT-19, 2.5: «se procurará» repartir entre fases o conductores polares. REBT no fija % de desequilibrio admisible
- ITC-BT-43, 2.6: no instalar sin consentimiento expreso de la suministradora receptores con desequilibrios importantes en polifásicas
- ITC-BT-52, 3.1 (viviendas unifamiliares): estaciones monofásicas en circuito trifásico, repartidas lo más equilibrado posible entre las tres fases
- Neutro: suma vectorial (120°). Iguales: 0; una fase: toda su corriente. IN = √(I1²+I2²+I3²−I1I2−I2I3−I3I1): 30-20-10 = √300 ≈ 17,3 A
- Efectos: fase sobrecargada con otras holgadas; pérdidas en neutro; tensiones distintas; peor aprovechamiento de transformador, grupo o SAI. Neutro cortado: monofásicos en serie a ~400 V, se queman
- Armónicos de orden 3 y múltiplos se suman en el neutro: puede ir más cargado que las fases
- ITC-BT-19, 2.2.2 (último párrafo): neutro interior ≥ fases, salvo justificación por cálculo. ITC-BT-44, 3.1: monofásico con descarga, neutro = fase
- ITC-BT-14: línea general, neutro ≈ 50 % de la fase, no inferior a tabla 1, según desequilibrio máximo, armónicas y protecciones
- Centro RTV (fuentes conmutadas): no dimensionar el neutro como resistivo
- Oficio: inventario de monofásicos (simultánea); ≈ 1/3 por fase (trifásicos equilibrados no cuentan); marcar fase en esquema y cuadro (marrón, negro, gris); medir fases y neutro con pinza o analizador (tema 14); corregir consignado (tema 15) y actualizar esquema
- Ej.: 3,0-2,5-2,0-1,5-1,5-1,0 = 11,5 kW: L1 4,0; L2 4,0; L3 3,5 kW = 17,4, 17,4, 15,2 A; neutro ≈ 2,2 A; tres mayores en una fase: 7,5 kW ≈ 32,6 A
- Juzgar con carga real; SAI o grupo monofásico en una fase = desequilibrio

## Lo que este tema no da
- ρ y γ (γ = 48 supuesto); intensidades admisibles (temas 3 y 4; UNE 20.460-5-523 no leída); penalización de reactiva (tarifas, no REBT); % de desequilibrio
- Medidas y verdadero valor eficaz: tema 14. Reforma del REBT posterior al 18/12/2025: ninguna. Leído en BOE consolidado el 05/10/2026
