# Tema 10 del específico de Operador/a de Sonido · Sonorización

**Siglas**: RTVA, CSRTV, PA, SPL, dB, dBu, dB/W/m, NAG, PAG, NOM, D1/D2/D0/DS, IEM, PWM, AWG, RT60, STI, NC, FM, AES.

Esqueleto para repasar, no resumen: cada línea remite a un dato del tema; el razonamiento y la cita completa están en el tema.

<!-- indice -->
<!-- /indice -->

## Sonorización

- (oficio) Cadena: fuente/micro (t.3) → mesa (t.4) → procesado/cruce (t.5) → etapa → altavoz → sala (t.1). Sala: único eslabón que no se cambia.
- (oficio) Dos exigencias contrarias: cobertura suficiente y pareja (NAG) vs. no acoplar (PAG limitada).
- (Shure) «if the dimensions of a sound system don't provide the needed gain with theoretical free field conditions, then even less likely under real world conditions».

## Altavoces

- (oficio) Electrodinámico: imán/yugo (campo fijo), bobina móvil, cono/diafragma, araña (centra SIN contacto, no rasca), suspensión exterior.
- (oficio) Fidelidad = relación longitud de bobina/altura de entrehierro: fuerza ∝ espiras dentro del campo; bobina fuera → distorsión.
- (oficio) Errores a rebatir: araña NO da contacto; caja NO debe vibrar; imán con MÁS campo = mejor.
- (oficio) Caja: capacidad en LITROS (volumen de aire, no faradios). Cerrada: controlada, caída suave. Bass-reflex: más rendimiento grave, caída brusca por debajo. Bocina: rendimiento alto, directividad controlada (refuerzo grande).
- (oficio) Directividad = distribución espacial de radiación (no impedancia/distorsión/potencia); regla: direccional si diámetro ≥ longitud de onda (t.1).
- (cálculo) 340 m/s: onda de 5 m = 68 Hz (graves omnidireccionales); 2 kHz = 17 cm (agudos direccionales); cono 30 cm pequeño/grande resp.
- (oficio) Bocina: directividad controlada en medios-agudos.
- (oficio) Sensibilidad 90 dB/W/m = SPL a 1 W y 1 m. Doblar potencia +3 dB; doblar distancia −6 dB; +3 dB sensibilidad = mitad de potencia.
- (oficio) Filtro de cruce reparte espectro entre vías. Linkwitz-Riley: suma plana y en fase en el corte. Pasivo: bobinas/condensadores dentro de caja, tras la etapa. Activo: antes de etapas, una por vía (refuerzo profesional).
- (TI AN-1497) Resistencia en continua típica de altavoces: 4 u 8 Ω. Impedancia mínima por canal: la marca la etapa (Crown, según modelo/modo). Asociación serie/paralelo y línea 100 V: tema 2.

## Amplificadores

- (oficio/t.2) Clases A/AB/C por conducción, D por conmutación: definición en tema 2.
- (TI AN-1497) Clase AB: rendimiento teórico máx. 78 %, real 30-40 %; clase D con ventaja de rendimiento. Ejemplo: 90 % rendimiento a 1 W disipa 100 mW (cálculo real ≈111 mW). Clase D: salida PWM, filtrada por paso bajo o por el propio altavoz.
- (oficio) Nota de TI es de portátiles: vale el concepto (pérdida = calor), no las cifras de sonorización.
- (Crown) Sensibilidad de entrada: 0,775 V = 0 dBu; 1,4 V = +4 dBu (redondeado; real ≈+5 dBu/1,23 V); 26 dB = ganancia fija. 0 dBu = 0,775 V por definición (t.2); mesa profesional a +4 dBu (t.2).
- (Crown) Puente mono: selector en Bridge-Mono, señal por canal 1, altavoz entre los dos bornes rojos; mayor potencia con cargas 8/4 Ω.
- (Crown) Paralelo mono: salidas rojas puenteadas, altavoz entre rojo y negro; sirve para impedancias más bajas; reparte igual entre número impar de cajas.
- (Crown) Decide el modo: impedancia total de carga deseada. No todos los modelos admiten ambos modos.
- (Crown) Conector Speakon (modelo NL4FC): dos canales por el mismo conector.
- (Crown) Factor de amortiguamiento = impedancia nominal del altavoz / impedancia de salida de la etapa; baja gracias a realimentación negativa de tensión; si falla, grave «boomy».
- (Crown) Cable: más tirada, más grueso (menos pérdida de potencia y amortiguamiento); orientación fabricante: ≤25 pies (≈7,6 m) AWG 14, >25 AWG 12. Recomendación, no norma; a número menor, cable más grueso.
- (oficio) Potencia de etapa: se elige con altavoz y nivel deseado (Cobertura). Doblar etapa = solo 3 dB; para +10 dB, ×10 potencia. Preferible antes: más sensibilidad, acercar altavoz, sumar cajas.

## PA

- (oficio) PA = sistema principal para el público, frente a monitores (para el escenario). PA grande: principal (a menudo array lineal) + subgraves + refuerzos + procesador (cruce, EQ, retardos). Sin norma que la defina.
- (Ureda/JBL, cita Klepper y Steele 1963) Array lineal = línea de altavoces como fuente alargada; «column loudspeakers». Guías de onda actuales → «behave more like continuous line sources».
- (Ureda) Caída con distancia: campo cercano ondula, ≈−3 dB por duplicación; distancia de transición, ondulaciones desaparecen, pasa a −6 dB; campo lejano, −6 dB por duplicación (igual que cuadrado inverso).
- (Ureda) Transición depende de longitud de línea y frecuencia; ejemplo: línea de 4 m a 8 kHz, −3 dB hasta ≈100 m, luego −6 dB.
- (Ureda) Formas: recta, arco (curved), J, progresivo. Rectas largas/agudas: diagrama muy estrecho («often too narrow»); arcos dan diagrama más ancho.
- (oficio) Consecuencia: en campo cercano, público delante/detrás recibe niveles más parecidos (3 dB/duplicación) que con caja suelta (6 dB).
- (oficio) Refuerzos en sala larga: si no se retrasan, efecto de precedencia falla (localización va al refuerzo). Retardo se aplica al altavoz MÁS CERCANO, nunca al lejano.
- (cálculo) Ejemplo 4 m/38 m: diferencia 34 m; 34÷340=0,1 s=100 ms. Atajo de oficio: ≈1 m cada 3 ms. 340 m/s es cifra redonda (t.1); velocidad real depende de temperatura.

## Monitores

- (oficio) Monitores devuelven al escenario (músicos, presentadores) lo que necesitan oír. Envíos auxiliares de mesa (t.4); montajes grandes, mesa propia de monitores.
- (oficio) Cuña (monitor de suelo): fácil, sin radio; altavoz abierto junto al micro → primera fuente de acople.
- (oficio) IEM: auriculares de inserción, casi siempre por radio; quita energía acústica del escenario; exige gestión de transmisores/frecuencias (t.12).
- (oficio/t.3) Cuña se coloca en el nulo del micro: cardioide, detrás a 180°; super/hipercardioide, a los lados del eje trasero (tienen lóbulo trasero). Aplicación directa de PAG: cuña = D1 más corta del sistema.
- (Shure, guía de antenas IEM) Combinador de antenas: reduce nº de antenas emisoras, transmisores comparten una. Varios transmisores de alta potencia muy juntos → intermodulación excesiva.
- (Shure) Regla: 2 transmisores → combinador pasivo; más de 2 → activo (admite 4-8). Combinadores activos NUNCA se encadenan («never be actively cascaded»); más de uno se une con pasivo.
- (Shure) Pasivo: al menos 3 dB de pérdida (cifra dada para combinación de salas; tenerla en cuenta en IEM). Bandas/coordinación/intermodulación: tema 12.

## Cobertura

- (Shure) Ley del cuadrado inverso: doblar distancia → −6,02 dB SPL. Fórmula: L' = L + 20 log D − 20 log D'. Regla: para cambio apreciable, distancia debe doblarse o reducirse a la mitad.
- (Shure) Condiciones: campo libre (sin reflexiones) y fuente puntual (mucho menor que la distancia). Array lineal en campo cercano NO la cumple (3 dB/duplicación); sala lejos de la fuente tampoco.
- (Shure) Escala de percepción: 1 dB apenas audible; 3 dB cambio notable; 10 dB = doble de fuerte.
- (cálculo) SPL a distancia d = sensibilidad (dB/W/m) + 10·log(W) − 20·log(d). Ejemplo: 97 dB/W/m, 400 W → 123 dB a 1 m; a 32 m (5 duplicaciones, −30 dB) ≈93 dB. +6 dB al fondo: ×4 potencia (1.600 W), o altavoz +6 dB sensible, o refuerzo más cerca.
- (Shure) Varios altavoces muy separados actúan como ecos tardíos (filtro en peine, t.1), pérdida de inteligibilidad; se minimiza con altavoz único o array compacto, lejos de quien habla y cerca de quien escucha. Refuerzos lejanos inevitables → retardo (PA).
- (Shure) Distancia crítica: donde directo = reverberante en nivel. Dentro, manda el cuadrado inverso; fuera, «things get much more complex».
- (Shure) Estimación: sonómetro + FM desintonizada (ruido banda ancha); alejarse hasta que el medidor deje de bajar, volver hasta subir 3 dB exactos.
- (Shure) En sistemas, la única distancia habitualmente dentro de la crítica es quien-habla↔micrófono (DS): la que más rinde cambiar (Realimentación).

## Realimentación

- (oficio/t.5) Acople: sonido de altavoces vuelve al micro con nivel suficiente para autosostenerse; dispara donde ganancia de lazo llega a 1. Patrón del micro (t.3): direccional acopla de golpe en agudos; omni, gradual en medios-graves.
- (Shure) NAG = ganancia necesaria para que el oyente más lejano oiga como el más cercano; se calcula con cuadrado inverso. Ejemplo: 70 dB a 2 pies, 49 dB a 22 pies → NAG 21 dB (medible con sonómetro, restando).
- (Shure) PAG, 4 distancias: D1 micro-altavoz (mayor mejor); D2 altavoz-oyente más lejano (menor mejor); D0 quien habla-oyente más lejano (la fija la sala); DS quien habla-micro (menor mejor, la que más rinde).
- (Shure) PAG = 20logD1 − 20logD2 + 20logD0 − 20logDS. Supuestos: micros/altavoces omnidireccionales, sin reverberación/eco (como al aire libre). Sistema funciona si PAG ≥ NAG.
- (Shure) Ejemplo pies: D1=9,D2=20,D0=22,DS=1 → PAG=19−26+27−0=20 dB (falta 1 de 21). Alejando altavoz del micro y acercándolo al oyente (D1=11,D2=19) → PAG=22 dB.
- (Shure) Margen de estabilidad: normalmente 6 dB, para evitar timbre pre-acople. PAG = fórmula anterior −6. Ejemplo 22 dB → 16 dB (no llega); con D1=17,5,D2=13 → 24 dB (3 dB sobre NAG).
- (Shure) NOM: PAG = fórmula −10logNOM−6. 1 micro: 0; 2 micros: −3 dB; 4: −6 dB (cada doblar NOM, −3 dB). Ejemplo: 2º micro deja PAG en 21 dB (justo NAG); con 8, se come el margen entero.
- (Shure) Limitar micrófonos abiertos: técnico cierra los no usados, interruptor en cada micro, o mezclador automático (abre canal si supera umbral o, más nuevo, ruido de fondo).
- (Shure) Aplicación al peor caso: D0=oyente más lejano; DS=mayor distancia previsible habla-micro; D2=altavoz más cercano al oyente lejano; D1=altavoz más cercano al micro.
- (Shure) Micros/altavoces direccionales dan margen; mejora práctica límite ≈6 dB. Sala: lo que llega al micro desde altavoz es más de lo previsto → PAG real menor que la calculada.
- (Shure) DS: doblar distancia habla-micro cuesta 6 dB; reducir a la mitad los da (regla: «microphone as close as possible to the sound source»). Si DS supera distancia crítica de quien habla → más sala captada, menos inteligibilidad.
- (oficio, respaldado por Shure en 1-3 y componentes direccionales) 5 maneras de ganar margen, en orden: 1) acercar micro a fuente (6 dB/mitad distancia); 2) alejar altavoces del micro, apuntar a sus nulos (t.3); 3) micros direccionales; 4) tratar la sala (menos reverberación); 5) ecualizar con notch lo que se dispare (t.5), última opción: menos margen, más deterioro.

## Acústica de salas

- (oficio/t.1) Componentes: sonido directo (inteligibilidad/localización); primeras reflexiones (refuerzan si llegan pronto, estorban si tarde); cola reverberante (cuerpo/envolvente o confusión).
- (oficio, psicoacústica) Frontera de 50 ms: reflexión antes se SUMA al directo (refuerzo); después, eco separado.
- (Shure) Ecos tempranos ayudan inteligibilidad, tardíos la perjudican; altavoz cerca del techo: pegarlo, aprovecha reflexiones tempranas.
- (oficio/t.1) RT60: tiempo en caer 60 dB tras callar la fuente; crece con volumen, baja con absorción; público es mayor absorbente (sala vacía≠llena).
- (oficio) Reverberación: acorta distancia crítica (más allá, se oye sobre todo sala; subir nivel sube también sala; solución: acercar directo, apuntar al público); resta ganancia antes de acople (micro recibe más energía de la prevista); emborrona la palabra (sala de palabra: RT60 corto, medido con STI; música: más largo, t.1). Salas polivalentes: solución mecánica (cortinas, paneles, techos móviles), no electrónica.
- (oficio/t.1) Superficies paralelas favorecen más las ondas estacionarias (modos); problema de graves/subgraves; mínimo de presión no se arregla subiendo nivel (satura el resto). Se corrige con trampas de graves, geometría, moviendo escucha o subgrave; no ecualizando.
- (oficio) La sala manda: micro más cerca cuanto peor la sala; micro direccional en sala mala; potencia según ruido de fondo (curvas NC, t.1), no según cubrir la sala; altavoces lejos de paredes, apuntando al público; ganancia admitida = PAG con margen de 6 dB.
- Ninguna norma legal (ley/reglamento) sostiene este tema: documentación técnica de fabricante/AES/JAES, oficio y cálculo.
