# Tema 7 del específico de Oficial Técnico Electricista · Grupos electrógenos, sistemas de alimentación ininterrumpida y continuidad de servicio

**Siglas**: RTVA; CSRTV; REBT; ITC-BT; RIPCI; SAI (UPS); IEC; VFD; VI; VFI; CPD; UM; TT; V, Ah, Wh, kWh, kW, kVA, Hz.

Esqueleto para repasar, no resumen: fuente delante; «of.» = oficio, sin norma leída.

<!-- indice -->
<!-- /indice -->

## 1. Grupos electrógenos

- ITC-BT-40, 1: instalación generadora = transforma energía no eléctrica en eléctrica; Autogenerador = produce para necesidades propias.
- Of., partes: motor, alternador síncrono, regulador de velocidad (frecuencia), de tensión (excitación), cuadro, arranque, depósito diario y nodriza, refrigeración, escape, antivibratorios.
- Of.: régimen emergencia / principal con carga variable / continuo (menos trabaja, más potencia declara); kVA y kW por factor de potencia; altitud y temperatura restan potencia; carga por escalones; arrancador progresivo o variador.
- ITC-BT-40, 3: instalaciones complementarias (depósitos, canalizaciones) cumplen además sus reglamentos; local de uso exclusivo con protección contra incendios; motores térmicos, cualquier potencia, suficientemente ventilados; escape incombustible, al exterior o aprovechamiento energético.
- Of.: aire para combustión, motor, alternador y local; escape aislado, con compensador, lejos de la toma; ruido por aire, estructura y conductos.
- ITC-BT-40, 7: protecciones del fabricante; salida según ITC; mínimas (ajustes modificables por normativa del sector eléctrico):
  - sobreintensidad: relés directos magnetotérmicos o equivalente;
  - mínima tensión: tres fases y neutro, < 0,5 s, al 85 %;
  - sobretensión: fase y neutro, < 0,5 s, al 110 %;
  - frecuencia: < 49 Hz o > 51 Hz durante más de 5 períodos.
- ITC-BT-40, 5: cable ≥ 125 % de la intensidad máxima del generador; caída generador-punto de interconexión ≤ 1,5 % a intensidad nominal.
- ITC-BT-40, 6: tensión prácticamente senoidal; armónicos pares 4/n, orden 3: 5, impares ≥ 5: 25/n (% sobre fundamental).
- Of., nueve fases: detección; abre red; arranque, intentos limitados; estabilización; cierra grupo; escalones; red confirmada; retransferencia; refrigeración en vacío y parada.
- ITC-BT-28, 2.2: fuente de seguridad arranca al faltar tensión o bajar del 70 %.

## 2. Sistemas de alimentación ininterrumpida

- Of.: doble conversión = única fuente «sin corte» (la ITC no asigna categorías); alta eficiencia deja de serlo.
- Of., bloques: rectificador o cargador; batería; inversor; bypass estático (automático, ms, ante sobrecarga o fallo del inversor); bypass de mantenimiento (manual, saca el equipo sin cortar carga).
- Of., topologías: pasiva o de espera (sólo corte; transferencia ms); interactiva (corte y tensión; menor transferencia); doble conversión (corte, tensión, frecuencia, forma de onda; sin transferencia).
- IEC 62040-3 vía W. Sölter (1.ª ed. 1999; norma no leída; edición vigente y UNE sin confirmar): tres pasos = dependencia de la red, forma de onda, curvas dinámicas.
  - VFD: depende de tensión y frecuencia = pasiva (offline);
  - VI: depende de frecuencia, tensión regulada = interactiva (line interactive);
  - VFI: independiente de ambas = doble conversión (online); clase 1 triple sólo en VFI.
- Of., al elegir: potencia kVA y kW; autonomía (carga y tiempo); factor de entrada y distorsión; sobrecarga; cortocircuito aportable.
- Of.: inversor limita corriente; cortocircuito aguas abajo puede no disparar el magnetotérmico; cae toda la carga; comprobar selectividad (tema 3).
- Of.: grupo por encima de la potencia del SAI (distorsión, recarga de batería, rendimiento < 1); coeficiente: fabricantes.

## 3. Continuidad de servicio

- ITC-BT-28, 1: pública concurrencia, también BD2, BD3, BD4 y no enumerados con > 100 personas; fuera, referencia.
- ITC-BT-28, 2: seguridad = alumbrados de emergencia, contra incendios, ascensores, otros urgentes; automática (sin operador) o no; categorías:
  - sin corte (continua en la transición); muy breve ≤ 0,15 s; breve ≤ 0,5 s; mediano ≤ 15 s; largo > 15 s.
- Of.: VFI sin corte; pasivo o interactivo muy breve; grupo automático mediano; grupo manual no es automática.
- ITC-BT-28, 3: alumbrado de emergencia automático con corte breve; grupo solo no cumple (tema 6).
- ITC-BT-28, 2.1: fuente con tiempo apropiado; admite baterías (las de arranque de vehículos generalmente no), generadores independientes, derivaciones separadas independientes de la normal.
- ITC-BT-28, 2.1: lugar fijo, sin afectarse por fallo de la normal; salvo autónomos, emplazamiento accesible sólo a cualificados o expertos, ventilado; derivaciones públicas sólo si no fallan a la vez; fuente única sin otros usos; varias, reemplazo si la potencia restante basta, con corte automático de lo no de seguridad; resistencia al fuego apropiada; facilitar verificación, ensayos y mantenimiento.
- ITC-BT-28, 2.2: fuente propia = baterías, aparatos autónomos o grupos; capacidad mínima = alumbrado de seguridad (3.1).
- ITC-BT-28, 4.g: fuentes propias de alterna 50 Hz sin tensión de retorno a la acometida.
- REBT art. 10: normales (una empresa, toda la potencia, un punto); complementarios o de seguridad (dos empresas, o una con medios independientes, o usuario con medios propios; línea independiente desde origen en BT):
  - socorro: mínima 15 % del contratado; reserva: mínima 25 %; duplicado: > 50 %.
- ITC-BT-28, 2.3: socorro: espectáculos y recreativos, cualquier ocupación; reunión, trabajo y sanitarios > 300 personas. Reserva: hospitales y centros sanitarios, estaciones y aeropuertos, aparcamientos subterráneos > 100 vehículos, comerciales > 2.000 m², estadios y pabellones; en ambos, reserva.
- REBT art. 10.3: CCAA pueden fijar otros establecimientos.
- REBT art. 10.2: «deberán» dispositivos que impidan acoplamiento, salvo lo de las ITC; acuerdo con empresas; si no, la CCAA resuelve en 15 días hábiles.
- Of.: al grupo, cuadro de socorro (control, emisión, servidores, refrigeración de salas, alumbrado de seguridad, ascensores) y deslastre; al SAI, sólo lo que no cae ni un ciclo; SAI cubre arranque, grupo recarga SAI. Redundancias: tema 8.

## 4. Transferencia de carga

- ITC-BT-40, 2: aislada (sin conexión con la red); asistida (conexión sin paralelo, fuente preferente grupo o red, conmutación, sin corte posible según 4.2); interconectada (paralelo normal).
- Of.: grupo de socorro = asistida; de UM o exteriores = aislada; autoconsumo = interconectada (tema 18).
- ITC-BT-40, 4.2: conmutación de todos los activos y el neutro, sin acoplamiento simultáneo; of.: tetrapolar, enclavamiento mecánico; ordinaria con corte.
- ITC-BT-40, 4.2, sin corte: punto único con la red; sólo generadores > 100 kVA; neutro del generador desconectado de tierra en la interconexión; conmutador junto a medida de la red, accesible a la distribuidora; protección contra envío de potencia a la red; protecciones por tensión y frecuencia fuera de límites, sobrecarga y cortocircuito, enclavamiento contra línea sin tensión, fuera de sincronismo; sincronización; interconexión ≤ 5 s.
- ITC-BT-40, 4.2: contacto auxiliar que pone a tierra propia el neutro de la generación; protecciones precintables o método alternativo; distribuidora con acceso permanente; maniobra accesible al Autogenerador.
- ITC-BT-40, 9: asistida e interconectada, proyecto a la distribuidora (acoplamiento y seguridad); no en aisladas.
- ITC-BT-40, 8.2.2, asistida: red con neutro a tierra = TT, masas a tierra independiente de la del neutro de la red; imposibilidad técnica: misma tierra con autorización de la CCAA; sin corte: polo auxiliar que pone a tierra el neutro de la generación. Of.: sin ello fallan diferenciales (tema 5).
- ITC-BT-40, 4.1, aislada: dispositivo de conexión y desconexión en la salida; varios generadores, sincronización manual o automática; portátiles con protecciones contra sobreintensidades y contactos directos e indirectos.
- ITC-BT-40, 8.2.1, aislada: tierras independientes de cualquier otra; neutro y masas según ITC-BT-08; paralelo: unión de neutros a tierra en un solo punto. Acometida de UM: tema 8.
- Of., en el SAI: red a batería sin corte; inversor a estático en ms, carga en red sin protección (incidencia si se queda); a mantenimiento con secuencia del fabricante.
- Of., maniobra: a estático; cerrar manual; abrir salidas; vuelta inversa; sin estático = paralelo sin sincronismo.

## 5. Baterías

- Of.: pila = irreversible, primaria; batería o acumulador = reversible, recargable, secundaria.
- Of., parámetros: tensión nominal; capacidad Ah a un régimen; energía Wh; profundidad; ciclos; autodescarga; cortocircuito enorme.
- Of.: capacidad depende del régimen (menos en diez minutos que en diez horas); dimensionar con la nominal = error clásico.
- Of., regímenes de carga (valores: fabricante): carga tras descarga; flotación (normal en SAI); igualación (sólo si el fabricante la prevé). Cargador del SAI = rectificador; flotación correcta no prueba capacidad.
- Of., químicas: plomo-ácido abierta (hidrógeno, nivel); regulada por válvula (SAI clásicos); níquel-cadmio; ion litio (sistema de gestión).
- Of.: plomo abierto desprende hidrógeno, explosivo; ventilado (ITC-BT-28, 2.1); local con riesgo de incendio o explosión, sin decir cuándo. Cargador de la de arranque: primera causa de grupo que no arranca.
- Of.: serie suma tensiones, mantiene Ah; paralelo suma capacidades, mantiene tensión.
- Of.: elementos iguales; en serie manda el más débil; en paralelo, corrientes de igualación; se cambia el conjunto; energía = suma siempre. Supuesto: 4 × 12 V, 100 Ah en serie = 48 V; dos ramas en paralelo = 200 Ah; 4.800 y 9.600 Wh.

## 6. Autonomía

- Of., SAI: hasta que el grupo tome carga, más margen (arranque fallido y reintento; apagado ordenado).
- Of., cálculo: autonomía ≈ energía útil ÷ potencia activa (supuesto: 20 kW, 9,6 kWh, casi media hora en papel); menos por régimen rápido, pérdidas del inversor y envejecimiento; se mide.
- Of., grupo: autonomía = combustible, según escenario; depósito sujeto además a reglamentos específicos (ITC-BT-40, 3), sin decir cuál; niveles en cada ronda; gasóleo largo tiempo se degrada.
- ITC-BT-28, 3.1.1: alumbrado de evacuación ≥ 1 hora con la iluminancia prevista; 3.1.2 (ambiente o anti-pánico) igual; 3.1.3 zonas de alto riesgo: tiempo para abandonar la actividad o zona (iluminancias: tema 6).
- ITC-BT-38, 2.2: 2 horas, quirófano y asistencia vital; no es del puesto.
- Ninguna norma leída fija autonomía de SAI o grupo de producción: el titular.

## 7. Pruebas periódicas

- Of., grupo: combustible; refrigerante y aceite; batería de arranque y cargador (causa número uno); precalentamiento; arranque; con carga; transferencia completa; antivibratorios, manguitos, escape.
- Of.: arranque en vacío casi no prueba nada; vacío largo en diésel = carbonilla; con carga o banco resistivo; transferencia completa con ventana pactada (tema 17).
- Of., SAI: inspección visual (bornes, corrosión, vasos, fugas); temperatura del local (acorta el plomo); apriete; descarga (única que da la autonomía real; flotación correcta no mide capacidad); alarmas e histórico; filtros y ventiladores; los dos bypass.
- ITC-BT-28, 2.1: verificación periódica, ensayos y mantenimiento facilitados. Sin periodicidad en las normas leídas para edificio de oficinas y producción: plan de mantenimiento según fabricante (tema 13).
- RIPCI, anexo II: programa del fabricante; como mínimo tablas I y II. Tabla I, también por personal del titular; detección y alarma, cada tres meses:
  - fuentes de alimentación: prueba de conmutación en fallo de red, funcionamiento bajo baterías, detección de avería y restitución a modo normal;
  - requisitos generales: funcionamiento con cada fuente de suministro; acumuladores (bornas, agua destilada).
- RIPCI, tabla I, abastecimiento de agua: acumuladores y bornas; niveles (combustible, agua, aceite); alimentación eléctrica, líneas y protecciones. Resto: tema 11.

## 8. Actuación ante incidencias

- Of. íntegro: ninguna norma fija la actuación; manda el fabricante; RTVA y CSRTV no constan.
- Of., orden: carga crítica alimentada; avisar (tema 17); diagnosticar con alarmas; reparar en seguridad (tema 15).
- Grupo no arranca: batería o cargador, combustible, parada de emergencia enclavada, cuadro en manual o bloqueado; arranque manual si el procedimiento lo prevé; vigilar autonomía del SAI.
- Arranca y no toma carga: tensión o frecuencia fuera de límites, interruptor, enclavamiento; leer el cuadro. Toma carga y se para: sobrecarga, escalón, temperatura, aceite, combustible; deslastrar.
- Frecuencia inestable: regulador, escalones. Microcortes: no forzar retransferencia. Combustible bajo: pedir, deslastrar, apagado ordenado.
- SAI en bypass estático: carga en red sin protección; comprobar carga; no dejarlo; avisar.
- SAI alarma de batería: degradada, temperatura, cadena; probar descarga o cambiar el conjunto. Con batería: ver si el grupo toma carga.
- Cae todo el SAI por cortocircuito en un circuito: inversor limita, magnetotérmico no dispara; aislar circuito; revisar selectividad (fallo de elección de protección).
- SAI sobrecarga: retirar carga. Sobrecalentamiento: filtros, ventiladores, climatización.
- Baterías: sin interruptor; herramienta aislada, sin anillos ni relojes, protección facial y frente al electrolito.
- Grupo automático: bloquear el arranque antes de trabajar (tema 15). SAI: abrir la entrada no deja la salida sin tensión.
