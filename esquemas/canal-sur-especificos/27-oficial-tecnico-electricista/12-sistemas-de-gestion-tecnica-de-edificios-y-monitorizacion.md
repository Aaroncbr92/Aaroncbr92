# Tema 12 del específico de Oficial Técnico Electricista · Sistemas de gestión técnica de edificios y monitorización

**Siglas**: RTVA, CSRTV; BMS, SCADA, PLC, HMI, DDC; RITE, IT; RIPCI, e.c.i.; IDAE; ISO, UNE-EN; NIST; HVAC&R; SAI; CPD; UTA; EER; NTC; NDIR; VOC; CO2; IEC; NAMUR.

Esqueleto para repasar, no resumen: el desarrollo, los matices y los textos literales están en el tema.

<!-- indice -->
<!-- /indice -->

## 1. Sistemas de gestión técnica de edificios y monitorización

- RITE ap. 1: sistema de automatización y control = productos + programas + servicios de ingeniería; eficiente, económico, seguro; control automatizado y facilita gestión manual.
- RITE art. 2.1: instalación térmica incluye sistemas de automatización y control.
- Oficio: gestión supervisa a incendios, proceso y seguridad física; no los manda.
- RIPCI anexo I s.1.ª 1.7: alarma de incendio gestionada siempre por e.c.i.; en sistema integrado, prioridad máxima.
- Oficio, 4 razones: ahorro, confort, mantenimiento, explotación.
- RITE art. 12.3; IT 1.2.4.3.1.1: toda instalación, control automático (condiciones de diseño; consumo según carga).
- IT 1.2.4.3.5.1: «deberán»; no residencial, >290 kW, viable técnica y económicamente.
- IT 1.2.4.3.5.1 a) monitorizar, registrar, analizar, adaptar consumo en continuo; b) evaluación comparativa, detectar pérdidas de eficiencia, informar mejoras; c) comunicación e interoperabilidad (tecnologías patentadas, dispositivos, fabricantes).
- Referencia: UNE-EN 15232-1 (apéndice 2, edición 2018).
- IT 1.2.4.3.5.2: residencial «podrán».
- IT 1.2.4.3.5.3: adaptar al edificio; comprobar y ajustar en uso real; mínimo consumo (art. 11); instrucciones en Manual de Uso y Mantenimiento.
- IT 4.3.4: exento de IT 4.2.1, 4.2.2, 4.2.3 (tema 10); oficio: debe cumplir las tres capacidades.
- IT 3.3 pie tabla 3.1: hasta 70 kW con supervisión remota en continuo, mantenimiento hasta cada 2 años.
- IT 2.3.4.2 y ap. 1, 4 niveles: campo (sondas, termostatos, estados y alarmas, válvulas, actuadores, variadores); proceso (controladores analógicos y digitales); comunicaciones (interfaces, buses, drivers, redes); gestión y telegestión (puestos centrales, impresoras, pantallas, módems, routers).
- Oficio, pirámide: campo (ms), control (decenas de ms), supervisión (s), gestión (horas/días); control = proceso; supervisión + gestión = gestión y telegestión. Valen los nombres del RITE.
- IT 2.3.4: 1 parámetros a valores de proyecto y comprobar componentes; 2 seguimiento por niveles; 3 niveles de proceso contra base de datos, válida UNE-EN-ISO 16484-3 (ISO 16484-3:2005); 4 mantenimiento y actualización de programas por personal cualificado o suministrador.

## 2. BMS/SCADA

- NIST SP 800-82r3, SCADA: sistema informático que recoge, procesa y aplica mandos a grandes distancias; transporte y distribución eléctrica, oleoductos; retardos e integridad de datos. Ninguna norma española define SCADA ni BMS.
- Oficio: BMS = gestión del edificio, todos los niveles; SCADA = supervisión, gestión y telegestión; PLC/DDC = proceso (regula). HMI en puesto o cuadro.
- IDAE familia 23: puesto central (ordenador, pantallas, teclados, impresoras), SAI (op. 63), buses, controladores distribuidos, de unidades terminales, integraciones.
- BACnet = ISO 16484-5, 8.ª ed. agosto 2026 (EN ISO 16484-5:2026 sustituye a 2022): servicios y protocolos para HVAC&R y otros sistemas, modelo orientado a objetos. Objetos: Analog/Binary Input, Output, Value; Schedule; Calendar; Notification Class; Trend Log; Event Log. AcknowledgeAlarm; MS/TP; BACnet/IP (anexo J); IPv6 (anexo U). Leído sólo objeto e índice.
- Modbus V1.1b3 (26-04-2012): capa 7 OSI, cliente/servidor, petición/respuesta, códigos de función; TCP/IP puerto 502; serie asíncrona.
- Modbus, tablas: Discretes Input (1 bit, lectura); Coils (1 bit, lectura/escritura); Input Registers (16 bits, lectura); Holding Registers (16 bits, lectura/escritura). Oficio: analizadores, contadores, SAI, grupos.
- KNX (knx.org): estándar no propiedad de una marca; alumbrado, calefacción, persianas, seguridad, energía. Nº de norma no confirmado.
- Oficio, estrategias: programación horaria (hora fija); arranque óptimo (calcula hora cada día); parada óptima; enfriamiento gratuito; compensación por exterior; ocupación; limitación de potencia; rotación de equipos.
- IT 1.2.4.5.1: todo aire >70 kW refrigeración, enfriamiento gratuito (ap. 5: justificar incumplimiento).
- IT 3.7 (>70 kW): horario de marcha y parada; orden de equipos; régimen de fines de semana y condiciones especiales. IT 3.6: no arrancar varios motores a plena carga a la vez.
- Oficio, lazo: P (error presente); I (acumulado); D (velocidad); derivativa poco usada en climatización; mayoría PI.
- IDAE DDC, frecuencias recomendadas (M mensual, T trimestral, 2.A dos al año, A anual): 50 cables y buses (T); 55 comunicaciones con periféricos (T); 62 arranque del puesto tras fallo de tensión (2.A); 63 SAI (2.A); 64 obsolescencia (A); 66 cuadros de control (A); 68 instalación eléctrica y aislamientos (T); 71 tensiones de lazos y actuadores (T); 72 buses (T); 73 baterías de controladores (T); 78 respuesta de campo (T); 80 bucles, secuencias y horarios (2.A); 83 backup de programación (T); 97 reglajes y consignas (2.A).

## 3. Sensores

- Oficio, puntos: entrada digital, salida digital, entrada analógica, salida analógica.
- IDAE, claves: ED, SD, SS (supervisión), EA, SA, CT (contador); ficha: lógicas, componentes, «como mínimo» relación de puntos. Sistema: neumática, electromecánica, electrónica, DDC.
- Oficio, puntos: cuadros, analizadores, grupo, SAI, salas y CPD, alumbrado; incendios sólo recibida; reserva de puntos.
- Siemens Symaro 2016: temperatura, humedad, calidad del aire, presión, caudal. Pasivos (resistencia); activos (24 V alterna o 13,5-35 V continua; 0-10 V o 4-20 mA). QAA20 (2014): Pt 100, Pt 1000, NTC 10k, clase B.
- Pt100/Pt1000: platino, coeficiente positivo, IEC 60751; 100 Ω y 1.000 Ω a 0 °C.
- NTC: IEC 60539; coeficiente 2 a 6 % por kelvin; tolerancia suele fijarse a 25 °C (TDK); NTC 10k = 10 kΩ.
- IEC 60751, tolerancia (|t| en °C): AA ±(0,10+0,0017·|t|); A ±(0,15+0,0020·|t|); B ±(0,30+0,0050·|t|). B bobinada −196 a +600 °C; AA bobinada −50 a +250 °C.
- WIKA: 2 hilos (error; no con Pt100 A o AA; hasta 250 mm; normal en Pt1000); 3 hilos (compensa; hasta unos 30 m); 4 hilos (elimina; calibración; hasta 1.000 m).
- Otros: humedad (THM-C2, C4, C5, IT 1.2.4.3.2); CO2 NDIR, VOC; presión diferencial; caudal; presencia, fuga, puerta, nivel, intensidad (oficio).
- IT 1.2.4.3.3.2: IDA-C4 control por presencia; IDA-C6 control directo (CO2 o VOCs). Ap. 3: IDA-C2, C3, C4 en locales sin ocupación humana permanente. Ap. 4: IDA-C6 en ocupación variable (teatros, cines, salones de actos, aulas, deporte y similares); plató con público: lectura de oficio.
- Oficio, señales: 4-20 mA (lectura 0 = lazo roto); 0-10 V (cable cortado se lee cero); resistiva; contacto libre de tensión.
- WIKA T15 (2025): lineal; servicio 3,8 a 20,5 mA; fallo <3,6 o >20,5 mA (NAMUR NE 43); fábrica Pt100, 3 hilos, 0 a 150 °C.
- Escalado (aritmética): 4-20 mA: mín + (I−4)/16 × (máx−mín); 0-10 V: mín + U/10 × (máx−mín). 0-50 °C: 12 mA = 25 °C; 8 mA = 12,5 °C; 30 °C = 13,6 mA. 0-10 bar, 3 V = 3 bar.
- IDAE, contraste: 37 temperatura y termostatos (2.A); 39 humedad (2.A); 42 entradas en módulos (2.A); 76 lecturas y fuera de rango (T); 77 contraste con campo (T); 85 rangos de señal (T; guía numera dos con el 85); 92 valores reales con puesto (T).
- Oficio, contraste: instrumento propio, calibrado y más preciso, mismo punto y hora; causas por orden: situación, cableado, escalado, sonda. Salidas: orden desde puesto y comprobar en campo (op. 78).

## 4. Alarmas

- Oficio, orígenes: de equipo; por umbral; por discrepancia (orden sin estado); del propio sistema (comunicación, alimentación, señal).
- Oficio: histéresis; retardo; discrepancia exige orden y estado.
- IT 1.2.4.3.5.1 b): pérdidas de eficiencia también son aviso.
- Oficio, prioridades: crítica (personas o emisión; inmediata, fuera de horario); alta (pérdida de redundancia; en el turno); media (programada); baja (con el preventivo). Depurar alarmas sin acción; cada alarma con responsable.
- RIPCI 1.7: incendio, prioridad máxima; gestión en e.c.i.
- Oficio, ciclo: aparece, se reconoce, desaparece; reconocer no es resolver; repetida = avería intermitente.
- IT 1.2.4.3.1.3: rearme automático de seguridad sólo si las IT lo indican expresamente.
- IDAE, alarmas: 86 emisores y receptores (M); 87 simulación y notificación (M); 88 notificación remota (M); 82 análisis de mensajes (T).

## 5. Históricos

- Oficio: tendencia con fecha y hora + eventos (alarmas, órdenes, consignas, programa, quién). BACnet: Trend Log, Event Log.
- IT 1.2.4.4: ap. 2 >70 kW, medir y registrar combustible y electricidad por separado; ap. 3 energía térmica >70 kW; ap. 4 central frigorífica eléctrica diferenciada; ap. 5 generadores >70 kW, horas; ap. 6 bombas y ventiladores >20 kW, horas; ap. 7 compresores >70 kW, arrancadas.
- IT 3.4.2 tabla 3.3 (frío >70 kW): temperaturas y pérdidas de presión de evaporador y condensador; evaporación y condensación; potencia eléctrica absorbida; potencia térmica instantánea (% de carga máxima); EER instantáneo; caudales. Trimestral 70-1.000 kW; mensual >1.000 kW; primera al inicio de temporada.
- IT 3.4.4.2 (>70 kW): seguimiento desagregado por uso y agua; conservar al menos cinco años; entregar al propietario e incorporar al Libro del Edificio.
- IT 3.4.5: a disposición de usuarios y titulares cada año, últimos 5 años; publicidad obligatoria en usos del apartado 2 de la IT 3.8.1.2 >1.000 m² (tema 10).
- Oficio, usos: diagnóstico; mantenimiento por condición (tema 13); eficiencia; prueba.
- IDAE: 53 fecha y hora (T); 54 cambio de horario (2.A); 57 históricos y tendencias (T); 60 backup de bases de datos (T); 61 backup de históricos (T); 52 discos y memoria (A); 75 fallos de comunicación (T).

## 6. Telemedida

- Oficio: telemedida = medida leída en otro sitio; telemando = orden a distancia; telegestión = ambas + registro y alarma. Ninguna norma las define.
- RITE: «Nivel de gestión y telegestión» (módems, routers); IT 2.3.4.4.
- Oficio, energía: contadores y analizadores dan consumo por línea y uso (IT 1.2.4.4); avisan de desequilibrio, factor de potencia, potencia contratada (temas 1 y 14). Lectura remota de la compañía: no se da.
- Oficio: lectura congelada; vigilar refresco; contrastar con campo.
- IDAE: 90 refresco (T); 91 mando desde puesto (T); 92 valores reales con puesto (T); 93 módem y comunicación remota (T); 94 comunicación y actuación remota (T). 90-92 Integraciones; 93-94 Telegestión.
- Oficio: módem desde SAI; falta de comunicación = alarma en el otro extremo; acceso remoto cifrado, nominal, cerrado si no se usa, con registro.

## 7. Actuación ante avisos

- Ninguna norma fija protocolo de respuesta.
- RITE art. 25.3: anomalía al responsable de mantenimiento.
- IT 1.3.4.1.2.2.p: instrucciones de parada con alarma de urgencia y corte rápido.
- IT 1.2.4.3.1.3: rearme automático sólo si lo indican las IT. RIPCI: e.c.i., prioridad máxima; plan de autoprotección (tema 11).
- IDAE, diario: a la llegada, alarmas en pantalla; comprobar elemento emisor y normalizar; anotar en registro diario de incidencias; luego preventivo programado.
- Oficio, 9 pasos: 1 leer; 2 clasificar (personas o incendio, plan de emergencia, tema 11); 3 reconocer y avisar; 4 comprobar en campo; 5 consignar (tema 15): fuera de servicio también en el puesto o manual local, señalizar en ambos; 6 no rearmar a ciegas; 7 normalizar y probar (manual a automático); 8 registrar (orden correctiva, tema 13); 9 corregir el sistema.
- Oficio, casos: temperatura alta en sala o CPD (otras sondas, climatización, reserva, avisar; tema 9); SAI en batería (red, grupo; autonomía; tema 7); disparo de interruptor (línea, tipo de protección, causa; coordinar con producción; temas 3 y 17).
- Oficio, conflictos: parada óptima contra directo (espacios fuera del calendario); limitación de potencia contra plató (carga no escalonable); presencia contra grabación (zonas excluidas con luz roja); ruido contra sonido (modo silencio de plató).

## Normativa y huecos

- RD 1027/2007 (RITE, BOE-A-2007-15820): arts. 2.1, 12.3, 25.3; IT 1.2.4.3.1, 1.2.4.3.2, 1.2.4.3.3, 1.2.4.3.5, 1.2.4.4, 1.2.4.5.1, 1.3.4.1.2.2.p, 2.3.4, 3.3, 3.4.2, 3.4.4, 3.4.5, 3.6, 3.7, 4.3.4; apéndices 1 y 2. Vigente a 05/10/2026.
- RD 513/2017 (RIPCI, BOE-A-2017-6606): anexo I s.1.ª 1.7; vigente desde 10/05/2025.
- No da: contenido de UNE-EN 15232-1 y 16484-3; nº de norma KNX; LonWorks; definiciones normativas de SCADA, telemedida, 4-20 mA; ciberseguridad; termopares; IEC 60751, 60539 y NAMUR NE 43 no leídas directamente; sistema de la RTVA.
