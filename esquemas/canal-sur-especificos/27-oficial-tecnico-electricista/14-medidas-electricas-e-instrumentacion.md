# Tema 14 del específico de Oficial Técnico Electricista · Medidas eléctricas e instrumentación: multímetro, pinza amperimétrica, telurómetro, medidor de aislamiento, analizador de redes y termografía básica

**Siglas**: RTVA, CSRTV, REBT, ITC-BT, INSST, CAT, TRMS, RCD, MBTS, MBTP, PE, TT/TN, SAI, CPD; IΔn, Ia, RA, U, Zs, U0, ρ, ε, THD, CF, IP, DAR, HDF.

Esqueleto para repasar, no resumen: lo que no está aquí, está en el tema.

<!-- indice -->
<!-- /indice -->

## 1. Medidas eléctricas e instrumentación

- RD 614/2001 anexo I.10: medir/ensayar/verificar = comprobar estado eléctrico, mecánico o térmico, eficacia de protecciones, circuitos de seguridad o maniobra. I.8: no es trabajo en tensión; régimen del anexo IV.
- Anexo IV A.1: sólo autorizados; en AT, cualificados (autorizados auxilian bajo supervisión). I.13 autorizado: por el empresario, según capacidad. I.14 cualificado: autorizado con formación acreditada o 2 o más años de experiencia certificada. BT basta autorizado.
- Anexo IV A.2 protección frente a contacto, arco, explosión, proyección (útiles aislados); A.3 equipos según tensión, uso/mantenimiento/revisión según fabricante; A.4 apoyo estable, manos libres, iluminación; A.5 señalizar zona; A.6 aire libre, ambiente desfavorable. Anexo V B.1.2: abrir envolventes, sólo autorizados.
- INSST 2020: procedimiento si complejidad relevante (no en medidas triviales BT).
- ITC-BT-03 ap. I 2.1.2 (básica): telurómetro; medidor de aislamiento; multímetro o tenaza (V CA/CC hasta 500 V, I CA/CC hasta 20 A, resistencia); medidor de fugas ≤1 mA; detector de tensión; analizador registrador de potencia y energía CA trifásica; verificador de disparo de diferenciales (I-t); verificador de continuidad; medidor de bucle (≤0,1 Ω, compensa cables); luxómetro. 2.2 (especialista, según proceda): analizador de redes, armónicos y perturbaciones; electrodos de suelos; comprobador de quirófanos.
- ITC-BT-05 2.1: verificaciones previas por la empresa instaladora; ap. 3: UNE 20.460-6-61. «ITC MIE-BT 19» = ITC-BT-19 2.9. Cámara termográfica no está en el REBT; instrumentos de RTVA/CSRTV, no constan.
- Estado (oficio): V e I en tensión; R y aislamiento sin tensión; tierra con electrodo separado; analizador y termografía en carga.
- Ausencia de tensión (INSST): UNE-EN 61243-3 detectores bipolares BT; probar el verificador antes y después (obligatorio AT, recomendable BT); todos los conductores y masas accesibles. Fluke, tres pasos: tensión conocida, circuito, de nuevo la conocida.
- Categorías (IEC/UNE-EN 61010, no leída; Fluke 2003): más cerca del origen, más CAT. IV origen (contadores, protección general, acometida); III instalaciones fijas (distribución, motores polifásicos); II tomas monofásicas; I electrónica protegida. La categoría manda sobre la tensión (CAT II 1000 V no supera CAT III 600 V); puntas igual o mayor.
- Fluke: borne 10 A = 0,01 Ω; tensión = 10 MΩ; puntas en borne de corriente sobre tensión = cortocircuito; fusible sólo de alta energía del fabricante.
- Continuidad sin tensión, REBT sin cifra. ITC-BT-24 4.1.1 (TN): Zs × Ia ≤ U0, tabla 1: 0,4 s con U0 = 230 V.
- Botón de prueba del diferencial: mecanismo, no tierra. Circutor CDB: tensión de contacto con 0,45 × IΔn; tiempo a IΔn (600 ms general, 1000 ms selectivo); a 5·IΔn sólo 6, 10, 30 mA, impulso ≤60 ms; rampa 0,30 a 1,40 IΔn; alterna: disparo ≤ IΔn; pulsante tipo A: hasta 1,4 IΔn; corta al pasar 25 V o 50 V.
- ITC-BT-24 4.1.2: selectivo en TT, máx. 1 s.

## 2. Multímetro

- ITC-BT-03 «o tenaza»: «continua» excluye pinza de transformador de corriente.
- Voltímetro: paralelo, resistencia muy alta. Amperímetro: serie, muy baja. Amperímetro en paralelo = cortocircuito, fusible, arco.
- TRMS: el convencional mide valor medio rectificado escalado a senoide; con variador, fuente conmutada o balasto electrónico lee por defecto. Valor eficaz calienta y dispara (tema 1, 3.2; tema 3).
- Resistencia: paralelos dan el paralelo; condensador cargado falsea y daña, descargar (RD 614/2001 anexo II B.3).
- Ausencia de tensión: detector bipolar y tres pasos, no multímetro (función equivocada o pila agotada marca cero).

## 3. Pinza amperimétrica

- Mide sin abrir; aísla al operador; abraza un solo conductor (dos = suma cero). Puntas con la misma categoría.
- Transformador de corriente: sólo alterna. Efecto Hall: alterna y continua (baterías SAI, grupos, cargadores, fotovoltaica; temas 7, 18). TRMS.
- ITC-BT-01: corriente de fuga = la que, sin fallos, va a tierra o a elementos conductores. ITC-BT-19 2.9: fugas no superiores a la sensibilidad de los diferenciales (conjunto o circuito). ITC-BT-03: medidor de fugas ≤1 mA (pinza de fugas).
- Fugas (oficio): abrazar todos los activos juntos, nunca el PE; bajar por derivaciones; o abrazar sólo el PE; comparar con el diferencial.
- Equilibrado (tema 1, 8.4), en carga representativa: fases parecidas, neutro nulo = equilibrado; fases distintas, neutro con corriente = pasar circuitos; fases parecidas, neutro alto = armónicos múltiplos de 3, no se arregla moviendo; fase muy alta = sobrecarga (temas 3, 4). Armónicos: analizador; pinza = instante.
- RD 614/2001 anexo II B.4.1 (AT): prohibido abrir secundario con primario en tensión salvo cortocircuitar bornes.

## 4. Telurómetro

- Mide resistencia de tierra; separar el electrodo.
- ITC-BT-18 9: resistencia ≤ valor especificado en cualquier circunstancia previsible; tensión de contacto máx. 24 V local o emplazamiento conductor, 50 V resto; si mayor, rápida eliminación con corte.
- ITC-BT-24 4.1.2 (TT): RA × Ia ≤ U; RA = tierra + conductores de protección de masas; Ia = IΔn con diferencial; U = 50, 24 V u otras.
- RA ≤ U/Ia: 30 mA = 1.667 Ω (50 V), 800 Ω (24 V); 300 mA = 167 Ω, 80 Ω; 1 A = 50 Ω, 24 Ω. Valor recomendado: no consta.
- ITC-BT-18 3.3: dispositivo de medida sobre conductores de tierra, accesible, desmontable con útil, seguro, con continuidad; puede ir en el borne principal. Abierto, masas sin tierra: medir rápido, cerrar, comprobar.
- Caída de potencial: separar; picas alineadas (corriente lejos, tensión entre medias); R = U/I. AEMC: X electrodo, Y potencial, Z corriente.
- Potencial nulo: mover la pica de tensión; si cambia, demasiado cerca; alejar la de corriente.
- 62 % (AEMC): Y al 62 % de X-Z; comprobar al 52 % y 72 %; tolerancia ±2 %, ±5 %, ±10 %; sólo tres electrodos en línea y tierra de un electrodo, tubo o placa; sin distancia X-Z específica.
- Aviso 1: sin separar, paralelo con tuberías, armaduras, otros electrodos: valor menor y falso. Aviso 2: varía con humedad y temperatura; vale el caso desfavorable.
- ITC-BT-18 12: comprobación obligatoria al dar de alta (Director de Obra o empresa instaladora); al menos anualmente, terreno más seco, personal técnicamente competente, reparar con urgencia; terreno desfavorable: electrodos al descubierto al menos cada cinco años.
- Pinza de tierra (AEMC): sin picas ni separar; necesita bucle, no vale en electrodo único; 2,4 kHz, filtra red; corriente de tierra >5 A, sin medida; incluye uniones pica-neutro.
- ITC-BT-18 9: R depende de dimensiones, forma y ρ. Tabla 5: placa 0,8 ρ/P; pica ρ/L; conductor horizontal 2 ρ/L. Tablas 3 (orientación) y 4: terreno cultivable fértil, terraplén compacto húmedo 50 Ω·m; pedregoso desnudo, arena seca permeable 3.000 Ω·m.
- Wenner (AEMC): cuatro electrodos en línea, distancia A; I por exteriores, U por interiores; A > 20 B; ρ = 2π A R, profundidad ≈ A.

## 5. Medidor de aislamiento

- Tensión continua, mide corriente, MΩ; sin tensión y separada de la alimentación.
- ITC-BT-19 2.9, tabla 3: MBTS/MBTP 250 V, ≥0,25 MΩ; ≤500 V 500 V, ≥0,5 MΩ; >500 V 1000 V, ≥1,0 MΩ (MBTS/MBTP: ITC-BT-36). 230/400 V: 500 V, 0,5 MΩ.
- Regla 100 m: tramos ≈100 m (seccionamiento, desconexión, fusibles, interruptores); si no fracciona, inversamente proporcional a la longitud en hectómetros (300 m: 0,5/3 ≈ 0,17 MΩ). Generador CC con 1 mA a la resistencia mínima.
- Conductores (neutro incluido) aislados de tierra y fuente; masas unidas al neutro: suprimir y restablecer.
- A tierra: receptores conectados, mandos en «paro»; interruptores cerrados, cortacircuitos como en servicio; conductores unidos en el origen al polo negativo, tierra al positivo; sin falta de continuidad. Entre conductores: receptores desconectados; dos a dos, neutro incluido. «Siempre desconectados» es error.
- Circuitos electrónicos: fases y neutro unidos durante las medidas.
- Lectura baja: correcta si cada receptor cumple su UNE o 0,5 MΩ y sin receptores cumple su valor.
- Rigidez: sin receptores, 1 minuto, 2U + 1000 V frecuencia industrial (U = tensión máxima de servicio), mínimo 1.500 V (400 V = 1.800 V); cada conductor a tierra y entre conductores, salvo ensayo previo del fabricante; no con riesgo de incendio o explosión. Aislamiento: CC, MΩ; rigidez: alterna, resistir.
- RD 614/2001 anexo IV B.2, 2.ª (fuente exterior): a) sin realimentación; b) puntos de corte resisten ensayo y servicio simultáneos; c) medidas al nivel de tensión.
- INSST: queda cargada por capacidades; descargar con tierra y cortocircuito. Vale el histórico, mismas condiciones.
- Megger (MIT400/2: IP y DAR): corta 60 s (temperatura, humedad); tiempo-resistencia 5-10 min; escalonada. Bueno: R sube; humedad: fuga constante.
- DAR = 60 s/30 s. IP = 10 min/1 min. Tabla I, DAR / IP: peligroso — / <1; dudoso 1,0-1,25 / 1,0-2; bueno 1,4-1,6 / 2-4; excelente >1,6 / >4.
- Notas: provisional y relativo; ≈20 % sobre excelente = devanado seco y quebradizo; IP 1,0-2 vale en cableado doméstico corto.

## 6. Analizador de redes

- Se deja registrando días.
- ITC-BT-03: básica = analizador registrador de potencia y energía CA trifásica (P activa, V, I, factor de potencia); especialista, según proceda = analizador de redes, armónicos y perturbaciones.
- Mide (oficio): tensión, intensidad y neutro, P/Q/S, energía, factor de potencia, cos φ, armónicos, huecos, máximos de demanda (temas 1, 7, 8, 16).
- Carga electrónica: factor de potencia (P/S) ≠ cos φ; condensadores corrigen desfase, no deformación (tema 1, 6.1).
- THD (Circutor CVM-NRG96): % sobre fundamental o % sobre RMS; 0 % en senoide; saber qué cálculo usa.
- CF (Fluke 2002) = pico/rms; senoide 1,4 (√2); CF = 2 máquinas de oficina; exige TRMS con pico. HDF = 1,4/CF; CF 2: 0,70; 20 A = 14 A.
- Neutro con armónico 3 y múltiplos: 80-130 % de la corriente de fase con sistema equilibrado; 150 Hz = armónico 3.
- Conexión (oficio): en servicio con anexo IV, categoría adecuada; fases y neutro en orden; pinza por fase y neutro en su fase y sentido red-carga (cambiada = potencias absurdas; diagrama vectorial); registro representativo (p. ej. una semana). Fijos: transformadores de intensidad (3.5), tema 12.

## 7. Termografía básica

- FLIR 2011: se calientan antes de fallar (efecto Joule, tema 1, 2.4). Detecta: conexiones de alta resistencia o corroídas; daños internos en fusibles y disyuntores; malas conexiones; desequilibrios de carga. Inspección con sistemas cargados.
- En carga: sin corriente no hay punto caliente; referencia en funcionamiento normal; cables sin carga = reflejos.
- RD 614/2001 anexo V B.1.2: abrir envolventes, sólo autorizados; cuadro abierto = anexo IV. Ventana = espejo.
- Factores (FLIR): conductividad (aislamiento lento, metales rápido); emisividad (correcta en la cámara o medida falsa); reflexión (metales no oxidados o pulidos); alta temperatura ambiente oculta puntos calientes, sol, viento, lluvia; aire frío de ventilación enfría la superficie.
- Piel: ε 0,97 = 36,7 °C; 0,15 = 98,3 °C. Corrección: ajustes o tabla; cinta de calibración (ε cercana a 1). Reflexión: temperatura reflejada, ángulo; el falso desaparece al mover la cámara; el verdadero, patrón homogéneo.
- Puntos fríos: fusibles fundidos, refrigeración limitada.
- Cámara (FLIR 2011, orientativo): 60 x 60 básica, 640 x 480 (307.200 puntos); sensibilidad 0,03 °C (30 mK); precisión ±2 % / ±2 °C.
- Inspección FLIR, 4 pasos: 1 definir tarea (enumerar equipos; prioridad por registros y consecuencias); 2 inicial (referencia en normal; documentar emisividad, reflexión, ubicación; umbral de alarma); 3 inspección (alarma activa: analizar); 4 análisis e informe (seguir en el tiempo).
- Oficio: prioridad cuadros generales, SAI, grupo, CPD, emisores; hallazgo = orden de trabajo (tema 13); reparar consignado (tema 15); repetir en carga. Criterios numéricos de gravedad: no constan.

## Lo que este tema no da

- Tiempos por clase de diferencial (UNE-EN 61008-1, 61009-1); continuidad y Zs en cifras; tierra recomendada; distancias del 62 %; ensayos por CAT e IEC 61010; gravedad termográfica; calidad de suministro; instrumentos y plan de RTVA/CSRTV.
