# Tema 8 del específico de Oficial Técnico Electricista · Instalaciones eléctricas en centros de producción audiovisual, CPD, centros emisores y unidades móviles

**Siglas**: RTVA, CSRTV, REBT, ITC-BT, CEM, CPD, UM, SAI, PDU, STS, CT, MBTS/MBTP, TT/TN/IT, CPN, AC, CTE, DB SUA.

Esqueleto para repasar, no resumen: el matiz, en el tema.

<!-- indice -->

- 1. Centros de producción audiovisual
- 2. Estudios
- 3. Salas de control
- 4. Centros de proceso de datos
- 5. Racks
- 6. Centros emisores
- 7. Unidades móviles
- 8. Continuidad
- 9. Redundancia
- 10. Ruido eléctrico
- 11. Compatibilidad electromagnética

<!-- /indice -->

## 1. Centros de producción audiovisual

- Sin categoría propia: REBT + instrucción particular + RD 186/2016 (particulares sustituyen, modifican o complementan).
- Oficio: continuidad, limpieza eléctrica, flexibilidad; fuerza/sensible separados desde el cuadro; una tierra por área, en estrella.
- ITC-BT-28, ap. 1, cualquiera que sea capacidad/ocupación: auditorios; salas de conferencias y congresos; estacionamientos cerrados y cubiertos para más de 5 vehículos.
- ITC-BT-28, ap. 1, más de 50 personas: bibliotecas, enseñanza, consultorios, comercios, oficinas con público, residencias de estudiantes, gimnasios, exposiciones, centros culturales, clubes.
- ITC-BT-28, ap. 1, general: locales BD2, BD3, BD4 (UNE 20.460-3); no contemplados con más de 100 personas. Ocupación = 1 persona/0,8 m² útiles, salvo pasillos, repartidores, vestíbulos, servicios.
- ITC-BT-29: taller de decorados con disolventes. ITC-BT-34: ferias, exposiciones, stands. Plató de RTVA/CSRTV: no consta.
- ITC-BT-19, ap. 2.4: subdividir para que la avería afecte sólo a una parte; protecciones coordinadas y selectivas con las generales; varios circuitos (evitar interrupciones, facilitar verificaciones, evitar circuito único). Ap. 2.5: fases repartidas.

## 2. Estudios

- ITC-BT-28, ap. 4: a) cuadro general lo más próximo a acometida o derivación individual; receptores de más de 16 A, directos desde general o secundarios. b) cuadros sin acceso del público, separados de locales con peligro de incendio o pánico (cabinas, escenarios, salas, escaparates) por elementos a prueba de incendios y puertas no propagadoras. c) placa indicadora junto a cada interruptor.
- 4.d: corte de una línea no afecta a más de la tercera parte de las lámparas. 4.e (tema 4): 450/750 V; armados 0,6/1 kV. 4.f: cables no propagadores del incendio, humos y opacidad reducida; seguridad no autónoma o centralizada, servicio durante y después. 4.g: fuentes propias 50 Hz sin tensión de retorno a la red pública.
- ITC-BT-28, ap. 5, espectáculos: a) líneas generales omnipolares: sala, vestíbulo/escaleras/pasillos, escenario y anexos (camerinos, almacenes), cabinas; cada grupo, cuadro secundario. b) escenarios, almacenes, talleres anexos: sólo magnetotérmicos; móviles con aislamiento doble o reforzado; portátiles clase II. c) secundarios en locales independientes o recinto no combustible.
- 5.d: corte omnipolar de camerinos, almacenes, talleres, reostatos, resistencias y receptores móviles del equipo escénico. 5.f: evacuación permanente hasta evacuar al público.
- ITC-BT-44, ap. 3.1 (iluminación no lineal, oficio): circuitos para receptores, asociados, armónicas y arranque; descarga: 1,8 × W en VA, neutro = fases en monofásica; otro coeficiente si FP ≥ 0,9 y se conocen asociados y arranque.

## 3. Salas de control

- ITC-BT-23, ap. 2.2, categoría I: equipos muy sensibles; protección fuera del equipo (instalación o entre ésta y el equipo); ordenadores, electrónicos muy sensibles.
- Tabla 1, 230/400 V, impulsos 1,2/50: IV 6 kV; III 4 kV; II 2,5 kV; I 1,5 kV. Ap. 2.1: cascada en tres niveles, basta, media, fina.
- ITC-BT-23, ap. 1: sólo líneas 230/400 V; no señales de medida, control, telecomunicación (fuera del REBT).
- Oficio: SAI de doble conversión sólo para lo crítico; cuadro propio desde su salida; tomas limpias distinguibles (forma sin norma); refrigeración en el grupo.

## 4. Centros de proceso de datos

- UNE-EN 50600-2-2:2019 «Distribución de energía»: en vigor, julio 2019, anula la de 2014, idéntica a EN 50600-2-2:2019 (AENOR). Ley 21/1992, art. 8.3: norma = observancia no obligatoria; exigible por contrato o pliego. Texto no leído; clases por TÜV NORD.
- Tres clasificaciones: disponibilidad, protección, granularidad (eficiencia). Cuatro clases (partes 2-2, 2-3, 2-4): AC1 vía única; AC2 vía única con componentes críticos redundantes; AC3 varias vías, reparar en operación; AC4 varias vías, tolerante a fallos salvo durante mantenimiento.
- Más clase = más redundancia de componentes y caminos; primero análisis de riesgo de negocio. Clase de cada CPD: no consta. *Tiers*: no es de la norma.
- Oficio, decisiones: qué se protege (lo crítico y su refrigeración); topología; autonomía (hasta que tome carga el grupo, más margen); encadenamiento (SAI cubre el arranque, grupo recarga).

## 5. Racks

- Oficio: dos PDU, A y B; cada fuente en PDU distinta; cuadros y, si se puede, SAI distintos.
- Cada rama lleva sola toda la carga: en normal, ninguna por encima de la mitad. Fuente única: STS o conmutador de rack, o punto único documentado.
- Armario metálico = masa, al PE. ITC-BT-18, ap. 5: funcional, funcionamiento correcto y fiable. Ap. 6: ambas a la vez, prevalece la protección; nunca se quita el PE.
- ITC-BT-18, ap. 7 (CPN, TN): separados neutro y PE, no se unen aguas abajo; bornes o barras separadas en la separación.
- Fugas de fuentes conmutadas suman y disparan el diferencial (oficio): no puentear; pinza de fugas (tema 14); más circuitos con diferencial. Fugas admisibles: no leídas.

## 6. Centros emisores

- ITC-BT-23, ap. 3.2: alimentación por línea aérea (desnudos o aislados) o que la incluya: protección necesaria contra sobretensiones atmosféricas en el origen. Ap. 3.1: aérea aislada con pantalla a tierra en ambos extremos = subterránea. Situación controlada también por continuidad de servicio, valor económico, pérdidas irreparables.
- No trata descarga directa del rayo (CTE, DB SUA 8, «Seguridad frente al riesgo causado por la acción del rayo») ni líneas de señal.
- Descargadores: TT o IT, cada conductor (con neutro o compensador)-tierra; TN-S, fase-PE; TN-C, fase-neutro o compensador; otras si se demuestra eficacia.
- ITC-BT-18, ap. 10: tomas independientes si una no supera 50 V respecto a potencial cero con la máxima corriente de defecto por la otra.
- Ap. 11: masas y PE de la utilización no unidos a la tierra de masas del CT; sólo se unen tierra del edificio y de protección (masas) del CT si Vd = Id · Rt queda bajo la tensión de contacto máxima aplicada.
- ITC-BT-19, ap. 2.2.2: industrial en AT con transformador propio, origen en su salida; caída 4,5 % alumbrado, 6,5 % demás; otras no viviendas, 3 % y 5 % (emisor industrial: lectura).
- Oficio, sin personal: grupo con arranque y transferencia automáticos y SAI; depósito para la llegada del combustible; telemedida y alarmas (tema 12); climatización en el grupo.
- Transmisores y radioenlaces: radioeléctricos, fuera del RD 186/2016 (art. 2.2.a); RD 188/2016, no desarrollado. Radiofrecuencia: tema 19.

## 7. Unidades móviles

- RD 186/2016, art. 3.2: instalación móvil = combinación de aparatos y dispositivos destinada a ser trasladada y utilizada en diversos sitios; consideración de aparato. UM encaja: lectura de aplicación.
- UM: grupo propio aislado = generadora aislada (ITC-BT-40, tema 7, 4.5).
- Conector (oficio): 3F + N + PE = cinco polos; 32, 63 o 125 A; 400 V rojo, 230 V azul, 110 V amarillo. 2 polos + tierra (3P) monofásico; 3 + tierra (4P) trifásico sin neutro; 4 + tierra (5P) trifásico con neutro y PE. Norma de producto: no consultada.
- Acometida: comprobar PE y diferencial de cabecera; sin tierra, carcasas sin protección.
- Al llegar (oficio; tema 14): magnetotérmico + diferencial en origen; tensiones F-F, F-N y PE; orden de fases; manguera desenrollada; caída de tensión (tema 1); misma tierra que equipos unidos por señal.

## 8. Continuidad

- Continuidad = la carga no nota el fallo; autonomía = cuánto aguanta. Capas (oficio): suministros (tema 7, 3.3); generación propia; SAI; distribución (un cuadro de salida único = su continuidad).
- ITC-BT-28, ap. 2, conmutación (tema 7, 3.1): sin corte; muy breve 0,15 s como máximo; breve 0,5 s; mediano 15 s; largo más de 15 s.
- Oficio: control y CPD, sin corte; alumbrado de plató, mediano (tema 6); climatización, no largo.
- Selectividad (ITC-BT-19, ap. 2.4): tras el SAI el inversor limita el cortocircuito y puede ir a bypass sin disparar el magnetotérmico (tema 7, 2.4).
- Puntos únicos de fallo (oficio): cuadro general o embarrado del SAI; transferencia red-grupo; PDU con las dos fuentes; bypass de mantenimiento; climatización única; persona única (tema 13).

## 9. Redundancia

- Oficio: N = lo necesario; N+1 = uno más en el mismo sistema (cubre un componente); 2N = dos sistemas completos e independientes (cubre un camino); exige dos entradas o STS.
- UNE-EN 50600 (secundaria): AC1-2 un camino, AC2 con componentes críticos redundantes; AC3-4 al menos dos caminos. Desde 2019 (2-2), AC3 requiere fuentes adicionales n+1 si sólo hay primarias.
- Dos caminos (oficio): equipo con dos fuentes o STS (conmutador estático; punto único de fallo; fuentes sincronizadas; tiempo: fabricante).
- Tumban la redundancia (oficio): modo común; consumida sin alarma (tema 12); sobrecarga silenciosa; no probada (ventana pactada, tema 17).

## 10. Ruido eléctrico

- Armónicos: 50 Hz y múltiplos (150, 250, 350 Hz); los múltiplos de tres se suman en el neutro, que puede llevar más que las fases equilibradas. ITC-BT-19, ap. 2.2.2: con no lineales y desequilibrios, salvo cálculo, neutro como mínimo igual a las fases; pinza de verdadero valor eficaz (tema 14).
- Zumbido: 50 Hz red; 100 Hz rizado de rectificador de doble onda; silbido, fuente conmutada; siseo, ruido térmico; crujido, contacto malo. Cambia al mover cables de señal = bucle de masa; si no, fuente.
- Zumbido tras equipo nuevo (oficio): mismo cuadro; tensión entre PE de su toma y el de equipos con señal; neutro a tierra aguas abajo (5.2) o PE interrumpido; nunca cortar el PE.
- Medidas (oficio): transformador de aislamiento; SAI doble conversión; energía y señal separadas, cruce en ángulo recto. Distancias por CEM: no consultadas.
- ITC-BT-20, ap. 2.1.1: canalizaciones eléctricas y no eléctricas próximas, 3 cm mínimo entre superficies exteriores; no es distancia de CEM (lectura). Calefacción, aire caliente, vapor, humo: distancia conveniente o pantallas calorífugas.
- Ap. 2.1: no potencia y MBTS/MBTP en las mismas canalizaciones salvo cable (o conductor de multiconductor) aislado para la tensión más alta, o compartimento separado que lo garantice.

## 11. Compatibilidad electromagnética

- RD 186/2016, art. 1: CEM de equipos eléctricos y electrónicos, mercado interior UE; alcanza instalaciones fijas. Art. 2.2: no a radioeléctricos del RD 188/2016. 2.3: telecomunicación no radioeléctrica sí, salvo capítulos IV, V, VI.
- Art. 3.1.a: equipo = cualquier aparato o instalación fija. c) instalación fija = combinación de aparatos y dispositivos, ensamblados, instalados y destinados a uso permanente en sitio predefinido.
- d) CEM = funcionar satisfactoriamente en su entorno sin perturbaciones intolerables para otros. e) perturbación = fenómeno que pueda crear problemas de funcionamiento. f) inmunidad = funcionar sin degradación ante perturbaciones. h) entorno = fenómenos observables en un sitio.
- Art. 6 y anexo I.1: a) perturbaciones generadas limitadas (emisión); b) protección frente a las previsibles sin degradación inaceptable (inmunidad). Anexo I.2: fijas según buenas prácticas de ingeniería.
- Art. 4: sólo se ponen en servicio equipos que, instalados, mantenidos y utilizados correctamente, cumplan.
- Art. 7.2: documentación técnica, declaración UE de conformidad, marcado CE. 18.1: precauciones de montaje, instalación, mantenimiento y uso. 18.2: restricción en zonas residenciales, indicación clara.
- Art. 19.1: buenas prácticas **deberán** documentarse, a disposición de autoridades durante el funcionamiento. 19.2: indicios, en especial quejas: autoridades **podrán** pedir pruebas y evaluar; demostrada la no conformidad, **impondrán** medidas. 19.3: conformidad y mantenimiento, del propietario y, en su caso, titular; no nombra instalador ni fabricante.
- 19.1: aparato para instalación fija concreta, no comercializado de otro modo: no obligatorios arts. 6 a 12 y 14 a 18; documentación identifica instalación y CEM, precauciones, art. 7.5 y 6 y art. 9.3.
- UM = aparato (3.2): no el régimen de buenas prácticas (lectura).
- Queja (oficio, art. 19): cruzar con cambios recientes; aislar fuente por circuitos en ventana pactada (tema 17), analizador de redes (tema 14); corregir (art. 18.1); documentar (19.1-2); informar al responsable (19.3).
