# Tema 18 del específico de Oficial Técnico Electricista · Innovación aplicada al mantenimiento

**Siglas**: RTVA, CSRTV, IoT, REBT, ITC-BT, RITE, IT, BMS, SAI, CPD, OT, ISO, IEC, UNE, EN, PVPC, QR, DTw, BIM, AIM, LPWA, NB-IoT, 3GPP, LFP, NMC/NCM, NCA, LCO, LMO, DIN.

Esqueleto para repasar, no resumen: lo literal, en el tema.

<!-- indice --><!-- /indice -->

## Sensorización IoT

- Oficio: nada obligatorio. ISO/IEC 20924 (definición IoT): no leída.
- ISO/IEC 30141:2024 «IoT — Reference architecture»: 27/08/2024, en vigor, anula ed. 2018; subcomité 41 «IoT and Digital Twin», JTC 1; sin UNE.
- BMS vs IoT (oficio): inalámbrico con pila; plataforma; además se mantienen red y pilas. Falta de comunicación del sensor = alarma.
- Variables (oficio): temperatura de conexiones; corriente, tensión, cos φ, armónicos; fuga de diferenciales; baterías (tensión por bloque, temperatura, resistencia interna); salas (temperatura, humedad, agua, puerta); motores (vibración, temperatura, horas); grupo (batería de arranque, refrigerante, combustible).
- RITE IT 2.3.4.2 niveles: campo, proceso, comunicaciones, gestión y telegestión; apéndice 1: campo = medida, sondas, actuadores; proceso = controladores; comunicaciones = buses, redes; gestión = puestos centrales.
- Sensor IoT = campo; plataforma = gestión (oficio). Comunicaciones al SAI; red separada; calibración.
- RITE IT 2.3.4.4: programas por personal cualificado o suministrador.
- LoRaWAN (LoRa Alliance): LPWA, «star-of-stars», gateways. Clase A: «Lowest power, bi-directional», obligatoria, el sensor inicia, dos ventanas; órdenes esperan al siguiente envío. B: ventanas programadas. C: receptor abierto, ~50 mW, «continuous power».
- NB-IoT (3GPP): Release 13 (LTE Advanced Pro), junio 2016; espectro con licencia.
- MQTT 5.0 (OASIS, 07/03/2019): publish/subscribe, ligero. QoS «At most once», «At least once» (duplicados), «Exactly once»; alarma no con el primero (oficio).

## Mantenimiento predictivo

- Predictivo o por condición: actúa cuando la medida dice que fallará. Correctivo: ya falló. Preventivo: calendario u horas.
- UNE-EN 13306 (tema 13): predictivo = preventivo basado en la condición; texto vigente no leído.
- ISO 17359:2018 «Condition monitoring and diagnostics of machines — General guidelines»: sólo catálogo.
- Base: termografía, análisis de red, aislamiento (tema 14); vale el histórico. Ciclo (oficio): medir igual, con fecha y hora; umbral de aviso y de actuación; OT preventiva.
- Motor (oficio): desequilibrio de corriente; aislamiento a masa; vibración. Batería (tema 7): flotación no mide capacidad; resistencia interna = bloque que se degrada; descarga controlada = autonomía.
- RITE IT 1.2.4.3.5.1.b): detectar pérdidas de eficiencia e informar. Reglamento (UE) 2023/1542 art. 14.1: datos de salud y vida útil. Ninguna norma obliga al predictivo.
- ISO 29821:2018 «Condition monitoring and diagnostics of machines — Ultrasound — General guidelines, procedures and validation»: subcomité 5, CT 108; anulada y sustituida por ISO 29821:2026 (abril 2026, DIN Media), no leída.
- Ultrasonido: no destructivo, >20 kHz, airborne (micrófono) o structure-borne (contacto); flujo turbulento, ionización, impactos, fricción; «electrical discharges». Tabla 1: «Switchgear», «Transformers», «Insulators», «Junction boxes», «Circuit breaker».
- Antes de abrir el cuadro: «arc flash hazard». Distingue descarga de vibración 50-60 Hz.
- Contacto: movimiento = falsa descarga parcial (acoplamiento magnético lo evita). Parabólico: fase con descarga en torre de alta tensión. Rodamientos lentos y lubricación.
- «hand-held, portable and battery operated»; fijos en línea: «at the inception». Termografía = calor; ultrasonido = descarga sin abrir (oficio).

## Gemelo digital de instalaciones

- ISO/IEC 30173:2023 «Digital twin — Concepts and terminology»: 08/11/2023, en vigor, inglés, sin UNE; subcomité 41, JTC 1.
- Def. 3.1.1: DTw = representación digital (3.1.8) de entidad objetivo (3.1.3) con conexiones de datos que permiten convergencia entre estados físico y digital a tasa de sincronización adecuada (traducción propia).
- Nota 1: conexión, integración, análisis, simulación, visualización, optimización, colaboración. Nota 2: visión integrada del ciclo de vida.
- Elementos: entidad objetivo, representación, conexiones. Oficio: planos, 3D y BIM de fin de obra no por sí solos; sinóptico del BMS en parte; modelo con medidas reales y simulación sí.
- ISO 19650-1:2018 = UNE-EN ISO 19650-1:2019 (en vigor, idéntica a EN ISO 19650-1:2018). 3.3.14 BIM: uso de representación digital compartida de un activo construido para diseño, construcción y explotación y base fiable de decisiones. 3.3.9 AIM: fase operativa.
- BIM = «digital representation»; faltan «data connections»; punto de partida del gemelo (oficio). Tasa de sincronización: la fija el uso.
- Usos (oficio): inventario vivo; impacto antes de intervenir (tema 17); simulación; predictivo; simulacros.
- Condición: documentación al día (tema 13); desfasado, pierde «convergencia».

## Telegestión energética

- Telemedida, telemando, telegestión: oficio, sin norma; RITE la nombra en el nivel «gestión y telegestión» e IT 2.3.4.4.
- RITE IT 1.2.4.4: apdo. 2, >70 kW: medir y registrar combustible y electricidad separados; apdo. 4, refrigeración >70 kW: electricidad de la central frigorífica diferenciada; apdo. 5, generadores >70 kW: horas; apdo. 6, motores de bombas y ventiladores >20 kW: horas; apdo. 7, compresores >70 kW: arrancadas. 70 kW térmico, 20 kW motores.
- Apdo. 8: generadores >70 kW con suministro directo renovable eléctrico: contabilizar diferenciado («dispondrán»); autoconsumo «si es técnicamente viable»; maximizar con comunicación y almacenamiento «podrá».
- IT 3.3 (nota a la tabla): hasta 70 kW con supervisión remota en continuo, periodicidad hasta 2 años si hay seguridad y eficiencia.
- Real Decreto 56/2016 art. 3: grandes empresas, auditoría cada 4 años, ≥85 % del consumo de energía final, o sistema de gestión certificado (3.1, 3.2); RTVA obligada: tema 16, sin confirmar. 3.3.a): datos operativos actualizados, medidos y verificables; perfiles de carga. 3.5: almacenables para análisis histórico y trazabilidad.
- Actuaciones (oficio): separar consumos; comparar; alarma de consumo anómalo; limitar potencia; desplazar consumos; rotar equipos.

## Baterías

- Fuente técnica, no norma: dos revisiones de 2026 (Advanced Science 13). Cátodos: LCO, NCM, LMO, LFP.
- LFP: olivino de fosfato estabiliza el oxígeno; «widely regarded as the safest commercial cathode»; humo blanco sin llama. NMC: óxido laminar, ricos en níquel más reactivos; NCA > LCO > NMC > LMO >> LFP; NCM: propagación más rápida, llama. LFP emite gas: ventilación y detección no se relajan.
- Reglamento (UE) 2023/1542, 12/07/2023: deroga Directiva 2006/66/CE desde 18/08/2025 (art. 95); directamente aplicable; general 18/02/2024 (art. 96.2); residuos 18/08/2025 (96.2.c).
- Art. 3.1: 13 batería industrial = uso industrial (o adaptada) o >5 kg que no sea de vehículo eléctrico, transporte ligero, arranque, encendido o alumbrado (batería de arranque del grupo: no, oficio); 15 estacionario = industrial con almacenamiento interno para red o usuarios finales; 25 sistema de gestión = controla funciones eléctricas y térmicas, almacena parámetros del anexo VII; 27 estado de carga = % de capacidad asignada; 28 estado de salud = estado general y capacidad frente al inicial.
- Art. 14.1: desde 18/08/2024, datos de salud y vida útil en el sistema de gestión (estacionarios, transporte ligero, vehículos eléctricos).
- Anexo VII A: capacidad restante; capacidad de potencia y eficiencia de ida y vuelta («en la medida de lo posible»); autodescarga; resistencia óhmica («en la medida de lo posible»). B: fechas de fabricación y puesta en servicio; rendimiento energético; rendimiento en capacidad; acontecimientos adversos (descargas profundas, tiempo en temperaturas extremas, en carga a temperaturas extremas); ciclos equivalentes.
- Art. 14.2: quien la adquirió legalmente: solo lectura, no discriminatorio, siempre.
- Art. 12.1: seguros. 12.2: a más tardar 18/08/2024, pruebas del anexo V (si hay peligro) e instrucciones de mitigación (12.2.d).
- Anexo V: 1 choque térmico y ciclos; 2 cortocircuitos externos; 3 sobrecarga; 4 descarga excesiva; 5 sobrecalentamiento; 6 propagación térmica; 7 daños mecánicos; 8 cortocircuito interno; 9 abuso térmico; 10 exposición al fuego; 11 emisión de gases. Sala (oficio): mitigación a mano; alarma de temperatura de celda máxima.
- Art. 13: 4, desde 18/08/2025 símbolo de recogida separada; 1, etiqueta anexo VI A desde 18/08/2026 o 18 meses tras acto de ejecución (apdo. 10) si posterior, cuál rige sin comprobar (fecha de fabricación, capacidad, composición química, agente extintor); 6, desde 18/02/2027 QR; pasaporte (6.a) en industriales >2 kWh (arts. 77, 78; contenido no).
- Art. 61.1: productores u organizaciones designadas (art. 57.1) aceptan devolución gratuita, sin comprar batería nueva ni haberla comprado a ellos; recogida separada.
- Mantenimiento (oficio): visual, temperatura, apriete, descarga; sin interruptor; herramienta aislada, sin anillos ni relojes, protección facial. Novedad: archivar datos del sistema de gestión; comunicación con BMS; ventilación; no mezclar nuevas con viejas.

## Autoconsumo

- Real Decreto 244/2019: arts. 3 y 4 por Real Decreto-ley 7/2026, 20 marzo (desde 22/03/2026); arts. 2, 5, 14 originales.
- 3.l): consumo de producción próxima y asociada (art. 9.1 Ley 24/2013). Art. 2: conectadas a red; 2.2 excluye aisladas y grupos exclusivamente ante interrupción (art. 100 Real Decreto 1955/2000, no leído): grupo de emergencia no es autoconsumo; el uso decide (oficio). 3.d) aislada: sin capacidad física de conexión nunca; interruptor abierto no vale.
- ITC-BT-40.2: aisladas, asistidas, interconectadas; autoconsumo: sin excedentes o con excedentes.
- 4.1.a sin excedentes: antivertido; un sujeto, el consumidor. 4.1.b con excedentes: dos sujetos, consumidor y productor. 4.2.a acogida a compensación; 4.2.b no acogida (incumple o no opta). 3.k antivertido: impide en todo momento el vertido; ITC-BT-40 en baja tensión.
- 4.2.a, cinco condiciones: 1 renovable; 2 ≤100 kW; 3 un único contrato de suministro con comercializadora si hay auxiliares; 4 contrato de compensación (art. 14); 5 sin régimen retributivo adicional o específico.
- 4.3: individual o colectivo; colectivo: misma modalidad, comunicación individual de un mismo acuerdo.
- 3.h FV: potencia máxima del inversor o suma (no paneles). 3.c: producción aunque no inscrita si ≤100 kW, asociada y con posible inyección.
- 3.g próximas: i red interior o línea directa; ii baja tensión del mismo centro de transformación; iii <500 m entre equipos de medida (proyección ortogonal); iii párr. 2: FV o eólica hasta 5 MW, transporte o distribución, <5.000 m; iv misma referencia catastral (14 dígitos). Antes (Real Decreto-ley 20/2022): sólo FV en cubierta, suelo industrial o estructuras, <2.000 m. «De red interior» = i; «a través de la red» = ii, iii, iv.
- 4.5: cambio de modalidad; colectivo simultáneo (a); sólo una modalidad, salvo individual sin excedentes más a través de la red (b; Ley 9/2025, 3 diciembre); a través de la red, con excedentes (c). 4.7: comunidad de energías renovables, con autorización.
- 5.7: almacenamiento con protecciones; comparte equipo de medida (generación neta, frontera o consumidor). 5.2: titulares distintos. 5.3: sin excedentes, consumidor titular; colectivo solidaria. 5.4: responsabilidad solidaria. 5.6: distribuidora podrá cortar por instalación peligrosa o manipulación de medida o antivertido.
- 14.3: saldo económico, periodo ≤1 mes; libre: precio horario acordado; PVPC: coste horario PVPC, excedente a precio medio horario del mercado diario e intradiario menos desvíos; excedente nunca superior al consumo; sin otra venta. 14.4: no energía incorporada, exenta de peajes de productores; comercializador responsable de balance. 14.2: colectivo sin excedentes, acuerdo, sin contrato.
- ITC-BT-40.4.3: todas las interconectadas, cualquier potencia; limitar corriente continua y sobretensiones, impedir isla; antivertido anexo I; ITC-BT-04 documentación; documentación anexo I con certificado; cuadro con diferenciales tipo A; 30 mA si público o residencial; circuito independiente y dedicado (con excedentes siempre; sin excedentes >800 VA).
- 4.3.1: ≤100 kVA y ≤ mitad de la salida del centro de transformación; sin excedentes: no 4.3.1, 4.3.4 ni apdo. 9 de distribuidora.
- Anti-isla protege personas; consignar con dos fuentes, red e inversor (tema 15).
- FV (oficio): módulos, continua y conectores, inversores, cuadro; producción vs irradiación = aviso. Sin periodicidades en norma.

## Automatización de edificios

- RITE IT 1.2.4.3.5.1: no residenciales >290 kW (calefacción, refrigeración o combinadas con ventilación), si técnica y económicamente viable. Residencial (apdo. 2): «podrán».
- a) monitorizar, registrar, analizar y adaptar el consumo; b) evaluación comparativa, detectar pérdidas, informar; c) comunicación e interoperabilidad entre tecnologías y fabricantes.
- Apéndice 1: instalación técnica y térmica incluyen automatización y control.
- Cita UNE-EN 15232-1, anulada por UNE-EN ISO 52120-1:2022 (19/10/2022, En Vigor; ISO 52120-1:2021, versión corregida 2022-09; anula UNE-EN 15232-1:2018).
- Apdo. 3: comprobar y ajustar en uso real; mínimo consumo (inactividad, uso, máximo rendimiento, renovables y residuales); «Manual de Uso y Mantenimiento».
- IT 2.3.4: apdo. 1, ajustar a proyecto o memoria y comprobar; UNE-EN-ISO 16484-3; apdo. 4, programas por cualificado o suministrador.
- IT 4.3.4 párr. 2: con sistema que cumpla IT 1.2.4.3.5.1 (residencial, apdo. 2), exentos de IT 4.2.1, 4.2.2, 4.2.3 (tema 10); exige a), b) y c); horario sin más no exime (oficio).
- Estrategias (oficio): ahorran: horaria, arranque óptimo, ocupación, enfriamiento gratuito; limitación de potencia (factura); rotación y registro de horas (sólo vida). Horaria = hora fija; óptimo = calcula la hora. Autonomía por niveles.
- Salas técnicas, CPD, emisores: manda la continuidad; ahorro en oficinas (temas 8, 9).
- Sin leer: Directiva (UE) 2024/1275; RTVA >290 kW sin confirmar.
