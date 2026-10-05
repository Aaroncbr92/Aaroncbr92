# 27 · Investigación · Bloque C-clima-gestion (temas 9, 10, 12 y 16)

Puesto 2.27 Oficial Técnico Electricista (B03), BOJA núm. 186, de 24-IX-2026, Anexo V.
Fase 1. Sólo lo que falta tras el reuso de RTVE localizado por el coordinador
(`temas/ing-tec-industrial/01`, `02`, `12` y `13`). Las citas entre comillas son literales de la
fuente indicada; lo demás es nota del investigador. Fecha de lectura de todas las fuentes BOE:
05-10-2026 (redacción «vigente hoy» según `herramientas/boe.py`; volcados nuevos en
`fuentes/canal-sur/`). Las fuentes web se fechan en su sitio.

Ficheros tocados: este informe y los volcados `fuentes/canal-sur/BOE-A-2007-15820.*`,
`BOE-A-2019-15228.*`, `BOE-A-2021-9176.*`, `BOE-A-2016-1460.*` (y los que se añadan abajo, que
se listan en su epígrafe).

---

## 0. Vigencia de lo que trae RTVE (léase antes de copiar)

| Norma | RTVE la cita a | Estado a 05-10-2026 | Consecuencia para el redactor |
|---|---|---|---|
| RITE, RD 1027/2007 (`BOE-A-2007-15820`) | 21-12-2022 | **Sin cambios desde el 01-07-2021** (RD 178/2021, `BOE-A-2021-4572`). La tabla de redacciones no tiene ninguna vigencia posterior | Lo de RTVE vale literal; sólo cambiar el pie «vigente el 21 de diciembre de 2022» por la fecha de lectura |
| RITE IT 1 e IT 3: aviso «posible reforma cruzada» de `boe.py` | — | Falso positivo: la «redacción» de `BOE-A-2022-12925` (RDL 14/2022, pub. 02-08-2022, vigencia en blanco) **sólo añade una nota «Véase el plan de choque… art. 29 del Real Decreto-ley 14/2022»**; el texto de la IT 3.8 es el de 2021. El plan (19 °C / 27 °C) **ya no rige**: DF 17.ª.2.a) RDL 14/2022, «tendrán vigencia hasta el 1 de noviembre de 2023» | No citar 19/27 °C como vigentes; los límites vigentes son 21/26 °C (IT 3.8.2) |
| RSIF, RD 552/2019 (`BOE-A-2019-15228`) | 21-12-2022 | Artículos 1, 2, 4, 6, 7, 8, 18, 19, 20, 21: **una sola redacción** (sin cambios). Art. 9 y 10: cambiados el 01-07-2021 (antes del corte RTVE). **Cambiados después de 2022**: art. 12 (vig. 04-09-2025, `BOE-A-2025-17507`), IF-04, IF-09, IF-10, IF-14, IF-16, IF-21 (vig. 10-05-2025, `BOE-A-2025-7190` = RD 164/2025, Reglamento de seguridad contra incendios en establecimientos industriales), IF-02 (12 redacciones; última vig. 19-08-2026, `BOE-A-2026-17906`) | El tema 02 de RTVE no cita ninguno de los cambiados salvo que nombra IF-02/IF-04/IF-09/IF-10/IF-14; lo copiado sigue valiendo. Ver 9.4 para art. 12 |
| RD 390/2021 certificación (`BOE-A-2021-9176`) | 21-12-2022 | **Reformado por RD 659/2025, de 22 de julio (`BOE-A-2025-15230`), en vigor el 23-07-2026**: arts. 2, 3, 6, 9, 10, anexos I-IV; añade arts. 4 bis, 4 ter, 4 quáter y 7 bis | Todo lo de RTVE sobre certificación hay que releerlo: ver tema 16 |
| RD 56/2016 auditorías (`BOE-A-2016-1460`) | 21-12-2022 | Últimos cambios: art. 13 (vig. 09-07-2020, `BOE-A-2020-7439`), arts. 5, 7, 8 y anexo I (vig. 03-06-2021, `BOE-A-2021-9176`). **Nada posterior a 2022** | RTVE vale; ver tema 16 sobre la Directiva 2023/1791 |

## Tema 10 · Reglamento de instalaciones térmicas en los edificios: eficiencia, seguridad, mantenimiento, inspección y documentación

Reuso RTVE (`ing-tec-industrial/01`, §1-5): arts. 1, 2, 10-17, 26-28, 30-33 del RITE. **Vigente sin
cambios** (ver §0). Lo que RTVE dejó fuera y el enunciado pide: el contenido de la **IT 3**
(mantenimiento: tablas de periodicidad, gestión energética, instrucciones, límites de temperatura),
la **IT 4** (periodicidad de inspecciones), la **seguridad** (art. 13 e IT 1.3: salas de máquinas)
y la **documentación** de ejecución y puesta en servicio (arts. 19-25). RTVE además nombra la IT 3
y la IT 4 «sin reproducir tablas» (declaración 2 de su trazabilidad): aquí están.

Fuente única de esta sección: RD 1027/2007, `BOE-A-2007-15820`, redacción vigente (desde
01-07-2021, RD 178/2021), leída 05-10-2026. Bloques `a13`, `a19`-`a25`, `a29`, `a31`, `it1-2`,
`it2-2`, `it3-2`, `it4-2`.

### 10.1 Seguridad (art. 13 e IT 1.3)

- Art. 13: «Las instalaciones térmicas deben diseñarse y calcularse, ejecutarse, mantenerse y
  utilizarse de tal forma que se prevenga y reduzca a límites aceptables el riesgo de sufrir
  accidentes y siniestros capaces de producir daños o perjuicios a las personas, flora, fauna, bienes
  o al medio ambiente, así como de otros hechos susceptibles de producir en los usuarios molestias o
  enfermedades.»
- IT 1.3.2: verificación en cuatro pasos: «seguridad en generación de calor y frío del apartado
  3.4.1», «seguridad en las redes de tuberías y conductos de calor y frío del apartado 3.4.2»,
  «protección contra incendios del apartado 3.4.3», «seguridad de utilización del apartado 3.4.4».
- IT 1.3.4.1.1.8 (útil para frío): «Los generadores de agua refrigerada tendrán, a la salida de cada
  evaporador, un presostato diferencial o un interruptor de flujo enclavado eléctricamente con el
  arrancador del compresor.»
- IT 1.3.4.1.1.3.b) (calor, no gas): dispositivo que impida temperaturas mayores que las de diseño,
  «que será de rearme manual».
- **Sala de máquinas** (IT 1.3.4.1.2.1): «local técnico donde se alojan los equipos de producción de
  frío o calor y otros equipos auxiliares y accesorios de la instalación térmica, con potencia
  superior a 70 kW». No lo son (ap. 2) los locales con generadores de calor ≤ 70 kW «o los equipos
  autónomos de climatización de cualquier potencia… preparados en fábrica para instalar en
  exteriores». Ap. 3: «Las salas de máquinas para centrales de producción de frío cumplirán con lo
  dispuesto en la reglamentación vigente que les sea de aplicación» (enlace con RD 552/2019, IF-07).
- Prescripciones comunes (IT 1.3.4.1.2.2), las más preguntables para un electricista:
  - i) «el cuadro eléctrico de protección y mando de los equipos instalados en la sala o, por lo
    menos, el interruptor general estará situado en las proximidades de la puerta principal de
    acceso. Este interruptor no podrá cortar la alimentación al sistema de ventilación de la sala»;
  - j) «el interruptor del sistema de ventilación forzada de la sala, si existe, también se situará
    en las proximidades de la puerta principal de acceso»;
  - k) iluminación «como mínimo, de 200 lux, con una uniformidad media de 0,5»;
  - d) cerradura «con fácil apertura desde el interior, aunque hayan sido cerradas con llave desde
    el exterior»; e) cartel «Sala de Máquinas. Prohibida la entrada a toda persona ajena al
    servicio»; l) no se usarán «para otros fines»;
  - p) indicaciones visibles: instrucciones de parada «con señal de alarma de urgencia y dispositivo
    de corte rápido»; datos del mantenedor; teléfono de bomberos y del responsable del edificio;
    puestos de extinción y extintores; «Plano con esquema de principio de la instalación».
- Sala de máquinas de riesgo alto (IT 1.3.4.1.2.4): «a) las realizadas en edificios institucionales
  o de pública concurrencia; b) las que trabajen con agua a temperatura superior a 110 °C»; en ellas
  el cuadro o al menos el interruptor general «y el interruptor del sistema de ventilación deben
  situarse fuera de la misma y en la proximidad de uno de los accesos».
- Gas (IT 1.3.4.1.2.3.4-5): válvula de corte automática todo-nada en el exterior de la sala, «de tipo
  cerrada»; tras disparo de la detección, «la reposición del suministro de gas será siempre manual».
- Dimensiones (IT 1.3.4.1.2.6.2): «La altura mínima de la sala será de 2,50 m».

### 10.2 Eficiencia: lo que el mantenedor vigila (IT 1.2.4.3-1.2.4.4) — también sirve al tema 12

- IT 1.2.4.3.1.1: «Todas las instalaciones térmicas estarán dotadas de los sistemas de control
  automático necesarios para que se puedan mantener en los locales las condiciones de diseño
  previstas, ajustando los consumos de energía a las variaciones de la carga térmica.»
- IT 1.2.4.3.1.2: control todo-nada limitado a cinco aplicaciones: «a) Límites de seguridad de
  temperatura y presión. b) Regulación de velocidad de ventiladores de unidades terminales. c)
  Control de la emisión térmica de generadores de instalaciones individuales. d) Control de la
  temperatura de ambientes servidos por aparatos unitarios, de potencia útil nominal menor o igual a
  70 kW. e) Control del funcionamiento de la ventilación de salas de máquinas.»
- IT 1.2.4.3.1.3: «El rearme automático de los dispositivos de seguridad sólo se permitirá cuando se
  indique expresamente en estas Instrucciones técnicas.»
- IT 1.2.4.3.1.7: «La temperatura del fluido refrigerado a la salida de una central frigorífica de
  producción instantánea se mantendrá constante, cualquiera que sea la demanda e independientemente
  de las condiciones exteriores, salvo situaciones que deben estar justificadas.»
- IT 1.2.4.3.1.10: «Los ventiladores de más de 5 m3/s llevarán incorporado un dispositivo indirecto
  para la medición y el control del caudal de aire.»
- IT 1.2.4.4 contabilización (ap. 2-7): >70 kW, medir y registrar consumo de combustible y
  electricidad separado del resto del edificio; medidor de energía térmica en centrales >70 kW;
  refrigeración >70 kW, consumo eléctrico de la central frigorífica diferenciado; ap. 5
  «Los generadores de calor y de frío de potencia útil nominal mayor que 70 kW dispondrán de un
  dispositivo que permita registrar el número de horas de funcionamiento del generador»; ap. 6 bombas
  y ventiladores «de potencia eléctrica del motor mayor que 20 kW» registran horas; ap. 7 «Los
  compresores frigoríficos de más de 70 kW de potencia útil nominal dispondrán de un dispositivo que
  permita registrar el número de arrancadas del mismo».
- IT 1.2.4.5.1.1 enfriamiento gratuito: «Los subsistemas de climatización del tipo todo aire, de
  potencia útil nominal mayor que 70 kW en régimen de refrigeración, dispondrán de un subsistema de
  enfriamiento gratuito por aire exterior.»
- IT 1.2.4.5.2.1 recuperación: si «el caudal de aire expulsado al exterior, por medios mecánicos, sea
  superior a 0,28 m³/s… se recuperará la energía del aire expulsado».

### 10.3 Documentación de ejecución y puesta en servicio (arts. 19-25)

- Art. 19.1: ejecución «por empresas instaladoras habilitadas»; 19.2: si requiere proyecto, «bajo la
  dirección de un técnico titulado competente, en funciones de director de la instalación»; 19.6:
  tres controles: «a) Control de la recepción en obra de equipos y materiales. b) Control de la
  ejecución de la instalación. c) Control de la instalación terminada.»
- Art. 20.2: documentación mínima de suministros: «a) Documentos de origen, hoja de suministro y
  etiquetado; b) copia del certificado de garantía del fabricante…; c) documentos de conformidad o
  autorizaciones administrativas… incluida la documentación correspondiente al marcado CE, etiquetado
  energético cuando sea pertinente».
- Art. 22.2: «Las pruebas de la instalación se efectuarán por la empresa instaladora»; 22.4: los
  resultados «pasarán a formar parte de la documentación final de la instalación».
- Art. 23.1: tras las pruebas de la IT 2 con resultado satisfactorio, «el instalador habilitado y el
  director de la instalación, cuando la participación de este último sea preceptiva, suscribirán el
  certificado de la instalación». Contenido mínimo, 23.2 a)-e) (identificación y características de
  lo ejecutado; empresa, instalador «con carné profesional» y director; resultados de pruebas IT 2;
  «declaración expresa de que la instalación ha sido ejecutada de acuerdo con el proyecto o memoria
  técnica y de que cumple con los requisitos exigidos por el RITE»; datos de red urbana si la hay).
- Art. 24.1: para la puesta en servicio de las del 15.1.a) y b) «será necesario el registro del
  certificado de la instalación en el órgano competente de la Comunidad Autónoma», presentando:
  «a) proyecto o memoria técnica de la instalación realmente ejecutada; b) certificado de la
  instalación; c) certificado de inspección inicial con calificación aceptable, cuando sea
  preceptivo.» 24.2: las del 15.1.c) (menos de 5 kW, etc.) no precisan acreditación. 24.6: el
  registro no supone «la aprobación técnica del proyecto o memoria técnica». 24.7: «No se
  registrarán las preinstalaciones térmicas en los edificios.»
- Art. 24.8: documentación que se entrega al titular y va al Libro del Edificio: «a) El proyecto o
  memoria técnica de la instalación realmente ejecutada; b) el "Manual de uso y mantenimiento"…; c)
  una relación de los materiales y los equipos realmente instalados…; d) los resultados de las
  pruebas de puesta en servicio…; e) el certificado de la instalación, registrado…; y f) el
  certificado de la inspección inicial, cuando sea preceptivo.»
- Art. 24.10: «Queda prohibido el suministro de energía a aquellas instalaciones sujetas a este
  reglamento cuyo titular no hubiera facilitado a la empresa distribuidora y, en su defecto, a la
  empresa comercializadora, copia del certificado de la instalación registrado».
- Art. 24.11 (sustitución de generadores sin registro): no hace falta registro si el generador es
  ≤ 70 kW, «siempre que la variación de la potencia útil nominal del generador no supere el 25 por
  ciento respecto de la potencia útil nominal del generador sustituido ni la potencia útil nominal
  del generador instalado supere los 70 kW»; se conserva «como mínimo la factura de adquisición del
  generador y de su instalación».
- Art. 25.1: el titular o usuario «es responsable del cumplimiento del RITE desde el momento en que
  se realiza su recepción provisional… y sin que este mantenimiento pueda ser sustituido por la
  garantía». 25.3: «Se pondrá en conocimiento del responsable de mantenimiento cualquier anomalía
  que se observe en el funcionamiento normal de las instalaciones térmicas.» 25.4: mantendrán «sus
  características originales». 25.5: el titular responde de «a) El mantenimiento de la instalación
  térmica por una empresa mantenedora habilitada. b) Las inspecciones obligatorias. c) La
  conservación de la documentación de todas las actuaciones…».
- Art. 28.2 (complementa RTVE): el certificado anual de mantenimiento incluye «d) Resumen de los
  consumos anuales registrados…» y «e) Resumen de las aportaciones anuales…».
- IT 2.3.4 (control automático en la puesta en servicio): niveles «de unidades de campo, nivel de
  proceso, nivel de comunicaciones, nivel de gestión y telegestión»; «Son válidos a estos efectos los
  protocolos establecidos en la norma UNE-EN-ISO 16484-3»; ap. 4: si hay sistema de «control, mando
  y gestión o telegestión basado en la tecnología de la información, su mantenimiento y la
  actualización de las versiones de los programas deberá ser realizado por personal cualificado o por
  el mismo suministrador de los programas».
- IT 2.2.3.2: no hace falta prueba de estanquidad en unidades por elementos «con líneas precargadas
  suministradas por el fabricante del equipo, que entregará el correspondiente certificado de
  pruebas».

### 10.4 Mantenimiento y uso: IT 3 (el núcleo para el puesto)

- IT 3.2: cinco procedimientos: «a) …programa de mantenimiento preventivo que cumpla con lo
  establecido en el apartado IT.3.3. b) …programa de gestión energética, que cumplirá con el apartado
  IT.3.4. c) …instrucciones de seguridad actualizadas de acuerdo con el apartado IT.3.5. d) …
  instrucciones de manejo y maniobra, según el apartado IT.3.6. e) …programa de funcionamiento,
  según el apartado IT.3.7.»
- **Tabla 3.1** (periodicidades mínimas; columnas «Viviendas» / «Restantes usos») — la de «restantes
  usos» es la de un edificio como el de RTVA:
  | Equipo | Viviendas | Restantes usos |
  |---|---|---|
  | Calentadores ACS a gas Pn ≤ 24,4 kW | 5 años | 2 años |
  | Calentadores ACS a gas 24,4 < Pn ≤ 70 kW | 2 años | Anual |
  | Calderas murales a gas Pn ≤ 70 kW | 2 años | Anual |
  | «Resto instalaciones calefacción Pn ≥70 kW» | Anual | Anual |
  | Aire acondicionado Pn ≤ 12 kW | 4 años | 2 años |
  | Aire acondicionado 12 < Pn ≤ 70 kW | 2 años | Anual |
  | Bomba de calor ACS Pn ≤ 12 kW | 4 años | 2 años |
  | Bomba de calor ACS 12 < Pn ≤ 70 kW | 2 años | Anual |
  | «Instalaciones de potencia superior a 70 kW» | Mensual | Mensual |
  | Solar térmica Pn ≤ 14 kW | Anual | Anual |
  | Solar térmica Pn > 14 kW | Semestral | Semestral |
  Nota literal: «En instalaciones de potencia útil nominal hasta 70 kW, con supervisión remota en
  continuo, la periodicidad se puede incrementar hasta 2 años, siempre que estén garantizadas las
  condiciones de seguridad y eficiencia energética.» «En todos los casos se tendrán en cuenta las
  especificaciones de los fabricantes de los equipos.» (Ojo: la fila de calefacción dice «Pn ≥70
  kW» con «mayor o igual», y la siguiente «superior a 70 kW»: así está en el BOE.)
- ≤ 70 kW sin Manual: «criterio profesional de la empresa mantenedora»; tabla 3.2 orientativa.
  Climatización, tabla 3.2.b): «1. Limpieza de los evaporadores. Limpieza de los condensadores. 2.
  Drenaje, limpieza y tratamiento del circuito de torres de refrigeración. 3. Comprobación de la
  estanquidad y niveles de refrigerante y aceite en equipos frigoríficos. 4. Revisión y limpieza de
  filtros de aire. 5. Revisión de aparatos de humectación y enfriamiento evaporativo. 6. Revisión y
  limpieza de aparatos de recuperación de calor. 7. Revisión de unidades terminales agua-aire. 8.
  Revisión de unidades terminales de distribución de aire. 9. Revisión y limpieza de unidades de
  impulsión y retorno de aire. 10. Revisión de equipos autónomos.»
- > 70 kW sin Manual: «la empresa mantenedora contratada elaborará un "Manual de uso y
  mantenimiento"». **Tabla 3.3** (> 70 kW), selección de las de clima y electromecánica:
  limpieza de evaporadores «t»; de condensadores «t»; torres «2 t»; «Comprobación de la estanquidad y
  niveles de refrigerante y aceite en equipos frigoríficos: m»; «Comprobación de tarado de elementos
  de seguridad: m»; «Revisión y limpieza de filtros de aire: m»; «Revisión de baterías de intercambio
  térmico: t»; «Revisión de aparatos de humectación y enfriamiento evaporativo: m»; recuperadores
  «2 t»; terminales agua-aire y de distribución de aire «2 t»; unidades de impulsión y retorno «t»;
  «Revisión de equipos autónomos: 2 t»; «Revisión de bombas y ventiladores: m»; aislamiento «t»;
  «Revisión del sistema de control automático: 2 t»; «Revisión de la red de conductos según criterio
  de la norma UNE 100012: t»; «Revisión de la calidad ambiental según criterios de la norma UNE
  171330: t». Leyenda: «m: Una vez al mes; la primera al inicio de la temporada. t: Una vez por
  temporada (año). 2 t: Dos veces por temporada (año); una al inicio de la misma y otra a la mitad del
  período de uso, siempre que haya una diferencia mínima de dos meses entre ambas.» (43 operaciones en
  total en la tabla.)
- IT 3.3.2: actualizar las operaciones es «responsabilidad de la empresa mantenedora o del director de
  mantenimiento».
- **IT 3.4.2 generadores de frío** (tabla 3.3 de medidas; columnas 70 < P ≤ 1.000 kW «3 m» y
  P > 1.000 kW «m»): once medidas: temperatura del fluido exterior en entrada y salida del evaporador
  y del condensador; pérdida de presión en evaporador y condensador «en plantas enfriadas por agua»;
  «Temperatura y presión de evaporación»; «Temperatura y presión de condensación»; «Potencia eléctrica
  absorbida»; «Potencia térmica instantánea del generador, como porcentaje de la carga máxima»;
  «EER instantáneo»; caudal de agua en evaporador y en condensador. «3 m: Cada tres meses; la primera
  al inicio de la temporada».
- IT 3.4.1 generadores de calor: columnas «20kW» / «70 kW» / «P>1000kW» con «2a» / «3m» / «m» (así
  aparece la cabecera en el BOE consolidado, con los rangos mal impresos; no reconstruirla). Seis
  medidas (temperaturas de fluido, ambiente de la sala, gases, CO y CO2, opacidad, tiro).
- IT 3.4.4.2: > 70 kW, seguimiento de consumos «con el mayor nivel de desagregación posible por uso
  (calefacción, refrigeración y agua caliente sanitaria)… Esta información se conservará por un plazo
  de, al menos, cinco años». IT 3.4.5: información anual de consumo de los últimos 5 años, en sitio
  visible; obligatoria en recintos de los usos de la IT 3.8.1.2 de más de 1.000 m².
- IT 3.5.2 instrucciones de seguridad (> 70 kW), «claramente visibles antes del acceso y en el interior
  de salas de máquinas… con absoluta prioridad sobre el resto de instrucciones»; aspectos: «parada de
  los equipos antes de una intervención; desconexión de la corriente eléctrica antes de intervenir en
  un equipo; colocación de advertencias antes de intervenir en un equipo, indicaciones de seguridad
  para distintas presiones, temperaturas, intensidades eléctricas, etc.; cierre de válvulas antes de
  abrir un circuito hidráulico».
- IT 3.6.2 manejo y maniobra (> 70 kW): «secuencia de arranque de bombas de circulación; limitación de
  puntas de potencia eléctrica, evitando poner en marcha simultáneamente varios motores a plena carga;
  utilización del sistema de enfriamiento gratuito en régimen de verano y de invierno».
- IT 3.7 programa de funcionamiento (> 70 kW): «a) horario de puesta en marcha y parada…; b) orden de
  puesta en marcha y parada de los equipos; c) programa de modificación del régimen de
  funcionamiento; d) programa de paradas intermedias…; e) programa y régimen especial para los fines
  de semana y para condiciones especiales…».
- **IT 3.8 Limitación de temperaturas** (vigente; el 19/27 °C del RDL 14/2022 caducó el 01-11-2023):
  usos afectados (3.8.1.2): «a) Administrativo. b) Comercial… c) Pública concurrencia: Culturales:
  teatros, cines, auditorios, centros de congresos, salas de exposiciones y similares.
  Establecimientos de espectáculos públicos y actividades recreativas. Restauración… Transporte de
  personas…». Valores (3.8.2.1): «a) …recintos calefactados no será superior a 21 ºC… b) …recintos
  refrigerados no será inferior a 26 ºC… c) …humedad relativa comprendida entre el 30% y el 70%.»
  Salvedad (3.8.2.3): «No tendrán que cumplir dichas limitaciones de temperatura aquellos recintos que
  justifiquen la necesidad de mantener condiciones ambientales especiales o dispongan de una normativa
  específica que así lo establezca. En este caso debe existir una separación física…» (aplicable a
  salas técnicas/CPD: nota del investigador, no lo dice la norma con esas palabras). Visualizador
  (3.8.3): DIN A3, «exactitud de medida de ± 0,5 ºC», obligatorio en > 1.000 m², «como mínimo, de
  uno cada 1.000 m2». 3.8.4 cierre de puertas. 3.8.5: verificación «una vez durante la temporada de
  verano y otra durante el invierno» si hay contrato de mantenimiento obligatorio; cumple si la media
  no supera «en ± 1 ºC» el límite; medición: «una medición… cada 100 m2», «a una altura de 1,7 m del
  suelo», exactitud «± 0,5 ºC».
- Condiciones de diseño (IT 1.1.4.1.2, tabla 1.4.1.1; útiles en tema 9): verano 23…25 °C operativa y
  45…60 % HR; invierno 21…23 °C y 40…50 % HR (1,2 met; 0,5/1 clo; PPD < 10 %); «Se podrá admitir una
  humedad relativa del 35 % en las condiciones extremas de invierno durante cortos períodos de
  tiempo.»

### 10.5 Inspección: IT 4 (complementa los arts. 29-33 de RTVE)

- Art. 29.3: inspeccionan servicios de la CA, «organismos de control habilitados» o «entidades o
  agentes cualificados o acreditados»; la habilitación en una CA vale «en cualquier parte del
  territorio nacional».
- Art. 31.2: las periódicas, por entidades o agentes «elegidos libremente por el titular».
- IT 4.2.1.1: se inspeccionan calefacción y ACS con generadores de calor «de potencia útil nominal
  mayor que 70 kW, excluyendo los sistemas destinados únicamente a la producción de agua caliente
  sanitaria de hasta 70 kW». IT 4.2.1.3.a): «el rendimiento a potencia útil nominal tendrá un valor
  no inferior al 80 por ciento». Norma de referencia válida: UNE-EN 15378-1.
- IT 4.2.2.1: aire acondicionado y ventilación con generadores de frío «de potencia útil nominal
  instalada mayor que 70 kW»; IT 4.2.2.3.a): «el Coeficiente de Eficiencia Frigorífica (EER) tendrá
  un valor no inferior a 2»; norma válida: «UNE EN 16798-17». Contenido: generador, bombas,
  distribución y aislamiento, emisores, regulación y control, ventiladores, distribución de aire,
  renovables, verificación del programa de gestión energética (> 70 kW) y de la información al
  público (IT 3.4.5 e IT 3.8.3). «Si el sistema de climatización es común para la generación de frío
  y de calor, como el caso de una bomba de calor, la inspección se realizará según la IT 4.2.2.»
- IT 4.2.1.4 / 4.2.2.4: informe de inspección «entregado al propietario o arrendatario del edificio»,
  con «recomendaciones para mejorar en términos de rentabilidad la eficiencia energética».
- IT 4.2.3: instalación completa si «más de quince años de antigüedad, contados a partir de la fecha
  de emisión del primer certificado de la instalación, y la potencia térmica nominal instalada sea
  mayor que 70 kW»; incluye «c) Elaboración de un dictamen».
- **IT 4.3 periodicidad**: calefacción/ACS «cada 4 años» (4.3.1); aire acondicionado y ventilación
  «cada 4 años» (4.3.2); instalación completa «se hará coincidir con la primera inspección del
  generador de calor o frío, una vez que la instalación haya superado los quince años» y «se
  realizará cada quince años» (4.3.3).
- IT 4.3.4 exenciones: instalaciones cubiertas por criterio de rendimiento o contrato de rendimiento
  energético (definido según el RD 56/2016) y «Los edificios no residenciales que cuenten con un
  sistema de automatización y control que cumpla los requisitos establecidos en el apartado 1 de la
  IT 1.2.4.3.5» quedan exentos de IT 4.2.1, 4.2.2 y 4.2.3 (enlace con tema 12).

## Tema 9 · Climatización y frío industrial aplicado al mantenimiento de edificios y salas técnicas

Reuso RTVE (`ing-tec-industrial/02`: arts. 1, 2, 4, 6-9, 18-21 del RD 552/2019; `01`: frontera con
el RITE). Lo copiado sigue vigente (ver §0), con dos matices de abajo (9.4). **Falta**: principios
básicos, equipos, refrigerantes en su régimen actual (Reglamento UE 2024/573), ventilación, control
de temperatura y humedad, averías frecuentes y mantenimiento preventivo.

Fuentes: RD 552/2019 (`BOE-A-2019-15228`), vigente, leído 05-10-2026 (bloques `a1-10`, `a2-7` a
`a2-11`, `ii-14`, `ii-17`); RITE (ver tema 10); Reglamento (UE) 2024/573, texto original del DOUE
(L, 2024/573, 20-2-2024), descargado el 05-10-2026 de la Oficina de Publicaciones
(`publications.europa.eu/resource/celex/32024R0573`, versión española XHTML) y guardado en
`fuentes/canal-sur/documentos/reglamento-ue-2024-573.txt`. **No es consolidado**: no he podido
comprobar correcciones de errores ni modificaciones posteriores (EUR-Lex devuelve 202/desafío
anti-robot; el BOE no da id DOUE por búsqueda). El redactor debe declararlo.

### 9.1 Refrigerantes: Reglamento (UE) 2024/573 (deroga el 517/2014)

- Art. 37.1: «Queda derogado el Reglamento (UE) n.o 517/2014.» 37.5: «Las referencias al Reglamento
  derogado se entenderán hechas al presente Reglamento con arreglo a la tabla de correspondencias que
  figura en el anexo X.» (La IF-17, 2.5.2, del RD 552/2019 todavía remite al «Reglamento (UE)
  517/2014»: se lee como remisión al 2024/573.) Art. 38: entra en vigor «a los veinte días de su
  publicación» (publicado 20-2-2024; aplicación de los arts. 12 y 17.5 desde 1-1-2025).
- Definiciones (art. 3): «"potencial de calentamiento global" o "PCG"… calculado en términos de
  potencial de calentamiento mundial a lo largo de 100 años… de un kilogramo de gas de efecto
  invernadero respecto al de un kilogramo de CO2»; «"tonelada equivalente de CO2": la cantidad de
  gases de efecto invernadero, expresada como el producto del peso de los gases de efecto
  invernadero en toneladas métricas por su potencial de calentamiento global»; «"operador": la
  empresa que ejerce un poder real sobre el funcionamiento técnico de los productos, aparatos o
  instalaciones…»; «"aparato sellado herméticamente"… cuyas juntas del sistema sellado tienen un
  índice de fugas, determinado mediante ensayo, inferior a 3 gramos al año…».
- PCG de anexo I (columna PCG a 100 años, «Basado en el cuarto informe de evaluación» del IPCC para
  HFC): HFC-32 «675»; HFC-125 «3 500»; HFC-134a «1 430»; HFC-143a «4 470»; HFC-23 «14 800». Mezclas
  (anexo VI): «media ponderada derivada de la suma de las fracciones en peso de cada una de las
  sustancias multiplicadas por sus PCG». Cálculo del investigador (no está en la norma): R-410A
  (50 % R-32 + 50 % R-125, composición no leída en fuente oficial) ≈ 2 088. **Si se usa, citar la
  composición de una fuente (ficha del fabricante o ASHRAE 34); si no, quitar.**
- Art. 4.1: «Se prohibirá la liberación intencionada de los gases fluorados de efecto invernadero a la
  atmósfera cuando la liberación no sea técnicamente necesaria para el uso previsto.» 4.5: fuga
  detectada → reparar «sin demora indebida»; tras reparar, revisión por persona certificada «lo antes
  posible después de que haya transcurrido un tiempo de funcionamiento de veinticuatro horas y a más
  tardar un mes tras la reparación».
- **Art. 5.1 (control de fugas)**: aparatos con «al menos 5 toneladas equivalentes de CO2» de gases
  del anexo I (o ≥ 1 kg del anexo II, sección 1). Exentos los sellados herméticamente etiquetados con
  «menos de 10 toneladas equivalentes de CO2» (o < 2 kg anexo II), y en edificios residenciales
  < 3 kg. Ámbito (5.2): aparatos fijos «a) aparatos de refrigeración; b) aparatos de aire
  acondicionado; c) bombas de calor; d) aparatos de protección contra incendios; e) ciclos Rankine
  con fluido orgánico; f) aparamenta eléctrica». Aparamenta exenta (5.1) si fugas < 0,1 %/año
  etiquetado, o «dispositivo de control de la presión o la densidad con un sistema de alerta
  automática», o < 6 kg (interesa al electricista: SF6).
- **Art. 5.6 frecuencias** (anexo I): < 50 t CO2-eq: «al menos cada doce meses; o, cuando se instale
  un sistema de detección de fugas…, al menos cada veinticuatro meses»; 50 a < 500: «al menos cada
  seis meses o… al menos cada doce meses»; ≥ 500: «al menos cada tres meses o… al menos cada seis
  meses».
- **Art. 6 detección de fugas**: obligatoria en fijos de 5.2 a)-d) con ≥ 500 t CO2-eq (o ≥ 100 kg
  anexo II), «que alerte al operador o a una empresa de mantenimiento de toda fuga»; 6.3: control del
  sistema de detección «al menos cada doce meses»; aparamenta (6.4) «al menos cada seis años».
- **Art. 7 registros** (aparatos sujetos a control de fugas), por cada aparato: cantidad y tipo de gas;
  cantidades añadidas «o que se deban a fugas»; recuperadas; si reciclado/regenerado; empresa y
  persona; «las fechas y los resultados de los controles…»; desmantelamiento. 7.2.a): conservar
  «durante al menos cinco años».
- Art. 8.1: recuperación obligatoria por persona certificada; 8.6: gases recuperados «no se usarán
  para la carga o el rellenado de aparatos a menos que el gas haya sido reciclado o regenerado».
- Art. 10.1 y 4.7: certificación de personas físicas (instalación, mantenimiento, reparación,
  desmantelamiento, control de fugas, recuperación) y de personas jurídicas para los aparatos de
  5.2 a)-e).
- **Art. 13 (prohibiciones de uso en mantenimiento)**: 13.3: PCG ≥ 2 500 prohibido para mantener
  aparatos de refrigeración de ≥ 40 t CO2-eq; «A partir del 1 de enero de 2025, se prohibirá el uso de
  los gases fluorados de efecto invernadero, con un potencial de calentamiento global igual o superior
  a 2 500, para el mantenimiento o revisión de cualquier aparato de refrigeración», salvo regenerados
  o reciclados hasta 1-1-2030. 13.4: «A partir del 1 de enero de 2026, se prohibirá el uso de los
  gases fluorados… con un potencial de calentamiento global igual o superior a 2 500, para el
  mantenimiento o revisión de aparatos de aire acondicionado y bombas de calor», salvo regenerados o
  reciclados «hasta el 1 de enero de 2032». 13.5: desde 1-1-2032, PCG ≥ 750 en aparatos fijos de
  refrigeración «con excepción de los enfriadores» (con salvedades de regenerado/reciclado). 13.7:
  SF6 en aparamenta desde 1-1-2035 sólo regenerado o reciclado (con excepciones; no leído entero).
- **Anexo IV** (prohibiciones de comercialización, art. 11.1), las de clima de edificio:
  9.a) «sistemas partidos simples que contengan menos de 3 kg… con un PCG igual o superior a 750»:
  «1 de enero de 2025»; 9.c) partidos aire-aire ≤ 12 kW con PCG ≥ 150 (salvo seguridad): «1 de enero
  de 2027»; 8.b) autónomos enchufables ≤ 12 kW PCG ≥ 150: 1-1-2027; 8.d) monobloque 12-50 kW PCG ≥
  150: 1-1-2027; 7.b) enfriadores ≤ 12 kW PCG ≥ 150: 1-1-2027; 7.d) enfriadores > 12 kW: el texto
  dice literalmente «con un PCG de 750» (sin «igual o superior»): **tal cual en el DOUE descargado;
  posible errata no comprobada**; fecha 1-1-2027. 4) aparatos de refrigeración autónomos (salvo
  enfriadores) PCG ≥ 150: 1-1-2025.

### 9.2 Mantenimiento preventivo y correctivo del frío (RD 552/2019, IF-14 vigente, vig. 10-05-2025)

- IF-14 1.1.1: mantenimiento preventivo, correctivo y revisiones «por una empresa frigorista
  habilitada de nivel correspondiente»; «Las operaciones de mantenimiento preventivo o correctivo que
  requieran la asistencia de personal acreditado de otras profesiones (como soldadores y
  electricistas) deberán ser realizadas bajo la supervisión de una empresa frigorista.» **(Dato clave
  para el puesto.)**
- IF-14 1.2.1, operaciones mínimas del programa: «a) Verificación de todos los aparatos de medida
  control y seguridad, así como los sistemas de protección y alarma para comprobar que su
  funcionamiento es correcto y que están en perfecto estado. b) Control de la carga de refrigerante.
  c) Control de los rendimientos energéticos de la instalación.» 1.2.2: en sistemas indirectos, el
  fluido secundario se revisa «en cuanto a su composición y la posible presencia de refrigerante».
- IF-14 1.2.6 aislamiento y cámaras: «a) Revisión semestral de la soportación de cámaras, estado de
  juntas y uniones con el suelo. b) Comprobación trimestral del funcionamiento de las válvulas de
  sobrepresión de las cámaras. c) Verificación mensual del funcionamiento de la resistencia y
  hermeticidad de la puerta, cierres, bisagra, apertura de seguridad, alarmas y ubicación del hacha
  en las cámaras. d) Retirada del hielo… por lo menos semanalmente. e) Revisión semestral de los
  soportes de las tuberías y de la formación de hielo y condensaciones superficiales no esporádicas.
  f) Revisión semestral de la apariencia externa del aislamiento.»
- IF-14 1.3.1, orden del correctivo con refrigerante (9 pasos): «1. Obtener permiso escrito del
  titular para realizar la reparación. 2. Informar al personal a cuyo cargo está la conducción de la
  instalación. 3. Aislar y salvaguardar los componentes… 4. Vaciar y evacuar el componente o tramo…
  5. Limpiar o hacer barrido (por ejemplo, con nitrógeno). 6. Realizar la reparación o sustitución. 7.
  Ensayar y verificar… 8. …hacer vacío de la parte afectada y restablecer la comunicación con el
  resto del sistema. 9. Poner en servicio…, verificar el correcto funcionamiento… y reajustar la carga
  de refrigerante si fuere necesario.» 1.3.4: válvula de seguridad que haya disparado a la atmósfera
  «deberá ser reemplazada si no queda totalmente estanca».
- IF-14 2.1 revisiones periódicas obligatorias: «a) Los sistemas se revisarán, como mínimo, cada
  cinco años. b) Los sistemas que utilicen una carga de refrigerante superior a 3000 kg y posean una
  antigüedad superior a quince años se revisarán al menos cada dos años.» 2.2 contenido (11 puntos):
  entre ellos «8. En las instalaciones frigoríficas con carga de refrigerante superior a 300 kg se
  comprobará mediante termografías el estado del aislamiento…» y «9. Revisión del estado de los
  detectores de fugas, realizando el ajuste, recalibración o sustitución del elemento sensor si se
  requiere.»
- IF-14 3.1 inspecciones (organismo de control): «Se inspeccionarán cada diez años las instalaciones
  frigoríficas de nivel 2»; con fluorados, «cada año si su carga de refrigerante es igual o superior a
  5000 toneladas equivalentes de CO2, cada dos años si es inferior a 5000… pero igual o superior a
  500…, y cada cinco años si es inferior a 500… pero igual o superior a 50». Punto 8, elementos de
  seguridad: «a) alarmas de hombre encerrado… e) comprobación de la instalación eléctrica: alumbrado
  de emergencias, iluminación, cuadros, etc.… g) comprobación del estado de los detectores de fugas».
  3.3: procedimiento «norma UNE 192013».
- Art. 26 RD 552/2019: controles de fugas por empresa frigorista (IF-17); revisiones (IF-14 e
  IF-17); inspecciones por organismo de control (IF-14).
- Art. 27.2: refrigerante en sala de máquinas para mantenimiento: «el 20% de la carga total de la
  instalación, con un máximo de 150 kg».
- Art. 28.2: salas de máquinas señalizadas; prohibido fumar y «la presencia de luces abiertas
  (desnudas) o llamas».
- Art. 29: accidente con daños a personas que requieran asistencia médica, víctimas, daños al medio
  ambiente o parada «superior a una semana»: notificar «en un plazo no superior a veinticuatro horas»
  y informe «en el plazo de un mes».
- Art. 18 (matiz a RTVE): letra p), contrato de mantenimiento en nivel 2 «con una empresa frigorista
  de su nivel o con una empresa instaladora de nivel 1 que satisfaga los requisitos exigibles para la
  clase A2L, en caso de usar estos refrigerantes» (RTVE recoge sólo la primera mitad).

### 9.3 Fugas: IF-17 (RD 552/2019; una sola redacción)

- IF-17 1.1: «La adquisición a título oneroso o gratuito, manipulación, recuperación, limpieza y
  reutilización de refrigerantes, queda restringido a las empresas frigoristas.»
- 1.5.1: «Está prohibida la reutilización de refrigerantes CFC… No está permitida la reutilización de
  refrigerantes HCFC, siendo obligatoria su recuperación y entrega a gestor de residuos autorizado
  para su destrucción.»
- 1.6 limpieza del circuito si: «a) Se haya producido una descomposición del aceite y haya presencia
  de corrosión o rotura de compresor. b) Haya entrado agua o humedad en el circuito frigorífico. c)
  El pH del aceite sea menor de 7. d) Sea necesario extraer restos de soldadura del interior…».
- 2.3.u): pruebas de presión y estanqueidad con «N2 seco, exento de oxígeno»; «Estas pruebas de
  presión o estanqueidad no se podrán realizar con refrigerante.» 2.3.t): indicadores de nivel; los
  equipos autónomos cargados en fábrica «deberán incorporar un visor en la línea de líquido».
- 2.4.c): antes de abrir un circuito, extraer hasta «0,6 bar absolutos cuando el volumen interior sea
  igual o inferior a 200 dm3 y a 0,3 bar absolutos para circuitos con volumen interior superior».
- 2.5.1: «No se recargará en ningún caso refrigerante sin haber localizado y reparado la fuga.» Control
  de fugas «antes de un mes a partir del momento en que se haya subsanado una fuga».
- 2.5.2: el texto consolidado dice «se revisarán… los siguientes sistemas:» y salta a la detección:
  **la lista o tabla no aparece en el volcado de la API** (probable tabla-imagen); el redactor usará
  las frecuencias del art. 5.6 del Reglamento 2024/573, no las de la IF-17.
- 2.5.3.2 comprobación general, señales de fuga/avería (lista útil para «averías frecuentes»): «a)
  Ruidos o vibraciones anormales, formación de hielo e insuficiente capacidad de enfriamiento. b)
  Señales visuales de corrosión, fugas de aceite y daños en componentes… c) Visores o indicadores de
  nivel… d) Daños en elementos de seguridad como presostatos, válvulas de seguridad, conexiones de
  sensores… f) Valores de los parámetros de funcionamiento que puedan revelar condiciones anormales».
- 2.5.3.3 métodos directos: «a) Aplicación de productos o disoluciones adecuadas. b) Detectores
  manuales de gas refrigerante y localizadores de fugas por ultrasonidos, etc. c) Detectores
  ultravioleta, de ser aplicables.» Detectores manuales «con sensibilidades de al menos 5 gramos por
  año. Se comprobarán anualmente.» 2.5.3.4 métodos indirectos: «a) Presión. b) Temperatura. c)
  Consumo energético del compresor. d) Niveles de refrigerante en estado líquido. e) Volúmenes de
  recarga.»

### 9.4 Matices a lo que trae RTVE del RD 552/2019

- Art. 12 (requisitos de empresas frigoristas), redacción vigente desde 04-09-2025 (`BOE-A-2025-17507` =
  Real Decreto 770/2025, de 2 de septiembre, «por el que se modifican diversas normas reglamentarias en
  materia de seguridad industrial en lo relativo al régimen de contratación de los profesionales
  habilitados»): seguro de RC profesional de
  la empresa «por importe mínimo de 300.000 euros por siniestro» (nivel 1) y «900.000 euros por
  siniestro» (nivel 2). RTVE no lo cita; si el redactor quiere hablar de empresas, éstas son las
  cifras vigentes. No confundir con los 500.000 € del seguro del **titular** (art. 18.d), sin cambios.
- IF-02 (clasificación de refrigerantes) tiene 12 redacciones, la última vigente desde 19-08-2026
  (`BOE-A-2026-17906` = «Resolución de 5 de agosto de 2026, de la
  Dirección General de Estrategia Industrial y de la Pequeña y Mediana Empresa, por la que se amplía la
  relación de refrigerantes autorizados por el Reglamento de Seguridad para Instalaciones
  Frigoríficas»). RTVE no reproduce sus tablas; si el redactor cita algún
  refrigerante concreto de la IF-02, leer la vigente.

### 9.5 Control de temperatura, humedad y ventilación (RITE; ver también 10.4)

- IT 1.1.4.1.2, tabla 1.4.1.1 (diseño): verano 23…25 °C / 45…60 % HR; invierno 21…23 °C / 40…50 %
  HR. Cálculo: «21 ºC» calefacción, «25 ºC» refrigeración.
- IT 1.1.4.2.2 calidad de aire interior: «IDA 1 (aire de óptima calidad)… IDA 2 (aire de buena
  calidad): oficinas…, IDA 3 (aire de calidad media): edificios comerciales, cines, teatros, salones
  de actos…, salas de ordenadores. IDA 4 (aire de calidad baja)». Caudales por persona (tabla
  1.4.2.1): IDA 1 «20», IDA 2 «12,5», IDA 3 «8», IDA 4 «5» dm³/s. CO2 sobre el exterior (tabla
  1.4.2.3): 350/500/800/1.200 ppm. Por superficie, locales sin ocupación permanente (tabla 1.4.2.4):
  IDA 2 «0,83», IDA 3 «0,55», IDA 4 «0,28» dm³/(s·m²).
- Filtración (IT 1.1.4.2.4, tabla 1.4.2.5): p. ej. ODA 1 → IDA 2 «F8», IDA 3 «F7»; prefiltros en la
  entrada de aire exterior y de retorno; recuperadores protegidos con filtros, «como mínimo de clase
  F6» si el fabricante no indica otra. (Ojo: clases F de la antigua EN 779 tal cual en el RITE; no
  traducir a ISO 16890 sin fuente.)
- Aire de extracción (IT 1.1.4.2.5): AE1 a AE4; «Sólo el aire de categoría AE 1, exento de humo de
  tabaco, puede ser retornado a los locales»; AE3 y AE4 no recirculan ni transfieren.
- Control termohigrométrico (IT 1.2.4.3.2, tabla 2.4.3.1): categorías THM-C0 (sólo ventilación) a
  THM-C5 (ventilación, calentamiento, refrigeración, humidificación y deshumidificación
  controladas). Control de calidad de aire (IT 1.2.4.3.3, tabla 2.4.3.2): IDA-C1 «El sistema funciona
  continuamente», IDA-C2 control manual, IDA-C3 por tiempo, IDA-C4 por presencia, IDA-C5 por
  ocupación, IDA-C6 «Control directo… sensores que miden parámetros de calidad del aire interior (CO2
  o VOCs)»; IDA-C6 para «locales de ocupación variable, como teatros, cines, salones de actos,
  aulas…».

### 9.6 Equipos y mantenimiento preventivo: fuente técnica (IDAE/ATECYR/AMICYF)

Fuente: «Guía técnica de mantenimiento de instalaciones térmicas», IDAE, serie «Ahorro y Eficiencia
Energética en Climatización», Madrid, febrero de 2007, ISBN 978-84-96680-06-7, redactada por ATECYR y
AMICYF; descargada el 05-10-2026 de la web del Ministerio (documentos reconocidos del RITE):
`https://www.miteco.gob.es/content/dam/miteco/es/energia/files-1/Eficiencia/RITE/documentosreconocidosrite/Guías técnicas/Guia_Mantenimiento.pdf`;
copia en `fuentes/canal-sur/documentos/idae-guia-mantenimiento-termicas.{pdf,txt}`. **Aviso**: es
de 2007 y su nota dice que «todas las menciones al Reglamento de Instalaciones Térmicas en los
Edificios se refieren al último borrador disponible»; se usa sólo como fuente técnica (equipos y
gamas), no como norma. Es «documento reconocido» del RITE (está en esa carpeta del Ministerio; el
propio texto dice que «pretende ser un procedimiento alternativo, de acuerdo con lo establecido en la
IT3»).

- **Familias de equipos** (índice del cap. 3, útil como lista de «equipos»): «6 Plantas enfriadoras de
  agua por compresión mecánica»; «7 Plantas enfriadoras de agua por ciclo de absorción»; «8 Torres de
  refrigeración y condensadores evaporativos»; «9 Equipos autónomos de acondicionamiento de aire»;
  «10 Sistemas autónomos de caudal de refrigerante variable»; «11 Unidades de tratamiento de aire»;
  «12 Filtros de aire»; «13 Recuperadores de energía aire-aire»; «14 Equipos para humectación del aire
  por inyección de vapor»; «15 Equipos de enfriamiento adiabático y humectación por contacto»; «16
  Baterías de tratamiento de aire»; «17 Unidades de ventilación y extracción»; «18 Motobombas de
  circulación»; «19 Conductos para aire, elementos de difusión y accesorios»; «20 Redes hidráulicas,
  componentes y accesorios»; «21 Intercambiadores de calor agua-agua»; «22-1 Unidades terminales de
  climatización. Ventiloconvectores y Cortinas de aire»; «23 Sistemas y equipos de regulación y
  control»; «24 Cuadros eléctricos y líneas de distribución para climatización». Ficha de enfriadora
  (familia 6): «Compresor(es): alternativo, scroll, tornillo, centrífugo».
- **Leyenda de frecuencias** (apéndice III): «D Tareas e intervenciones de frecuencia diaria»; «m
  Tareas de frecuencia mensual para potencias térmicas entre 70 y 1.000 kW, y de frecuencia quincenal
  para potencia térmica mayor que 1.000 kW»; «M Tareas de frecuencia mensual»; «T … trimestral»;
  «2 A Intervenciones que deben realizarse dos veces al año o dos veces por temporada»; «A … anual»;
  «B … bienal».
- **Gama genérica de enfriadora por compresión** (familia 6, cap. 4), selección de lo que toca a un
  electricista y a «averías»: «24 Comprobación del nivel de aceite en el cárter de los compresores y
  reposición si procede: m»; «29 Verificación de la inexistencia de humedad en los circuitos
  frigoríficos a través de los visores de líquido: m»; «30 Comprobación de carga de refrigerante… m»;
  «31 Inspección de estanqueidad y detección de fugas de refrigerante…: m»; «34 Inspección y limpieza
  de cuadros eléctricos de fuerza, maniobra y control: A»; «35 Inspección del apriete de todas las
  conexiones eléctricas de fuerza y maniobra…: A»; «36 Comprobación de estanquidad de las juntas de las
  bornas de los compresores y apriete de bornas: A»; «37 Comprobación de estado y actuación de los
  arrancadores de los compresores. Ajuste de transiciones: 2.A»; «38 Inspección de las conexiones de
  puesta a tierra de chasis de máquinas, cuadros y otros componentes: 2.A»; «39 Verificación de
  estado, reglaje y actuación de los relés y protecciones contra sobrecargas: m»; «41 … convertidores
  de frecuencia…: 2.A»; «42 … interruptores de flujo de agua: 2.A»; «43 Verificación de la
  funcionalidad de la serie exterior de seguridades de compresores y comprobación de enclavamientos:
  M»; «45 … elementos de seguridad, termostatos y presostatos: M»; «48 … dispositivos de limitación
  de arranques de compresores: M»; «50 Lectura de memorias históricas de microprocesadores de control y
  comprobación de la corrección de las anomalías registradas, así como de las posibles causas que las
  originaron: M»; «57 … válvulas de expansión: 2.A»; «61 Verificación de actuación de dispositivos de
  desescarche: 2.A»; «63 Inspección de filtros deshidratadores de refrigerante: 2.A»; «22 Comprobación
  del funcionamiento de las resistencias calentadoras de aceite: m»; «13 Limpieza de las aletas por
  ambas caras de la batería: A».
- Las gamas de las demás familias (UTA, filtros, humectadores, autónomos, VRV) están en el cap. 4
  (págs. 81-126 del PDF); no las he extractado: el redactor puede tomar de ahí lo que necesite para
  ventilación y humedad, con cita.

### 9.7 Salas técnicas y CPD: condiciones ambientales (fuente técnica)

- ASHRAE TC 9.9, «Equipment Thermal Guidelines for Data Processing Environments. ASHRAE TC 9.9
  Reference Card», tabla 2.1 «2015 Thermal Guidelines—SI Version» (descargada 05-10-2026 de
  `https://xp20.ashrae.org/datacom1_4th/ReferenceCard.pdf`; corresponde a la 4.ª edición):
  «Recommended (Suitable for all four classes…)» A1 a A4: «18 to 27» °C de bulbo seco, humedad
  «–9°C DP to 15°C DP and 60% rh». Permitido clase A1: «15 to 32» °C, «–12°C DP and 8% rh to 27°C DP
  and 80% rh», punto de rocío máx. «17». Definición: «Recommended: Facilities should be designed and
  operated to target the recommended range.» Clase A1: «Typically a data center with tightly
  controlled environmental parameters… and mission-critical operations».
  **Avisos**: (1) la tarjeta dice «may not be quoted or reproduced without permission from ASHRAE»:
  citar las cifras con su fuente, no reproducir la tabla; (2) existe una 5.ª edición (2021) que,
  según fuentes secundarias (no leídas en original), cambió la humedad recomendada: **no** afirmar
  la cifra de humedad como vigente sin leer la 5.ª ed.; los 18-27 °C sí constan en la 4.ª.
- Relación con el RITE: IT 1.1.4.2.2 clasifica las «salas de ordenadores» como IDA 3; IT 3.8.2.3
  exime de los límites de 21/26 °C a recintos que «justifiquen la necesidad de mantener condiciones
  ambientales especiales».

### 9.8 Lo que no he podido confirmar (tema 9)

- **Principios básicos del ciclo de compresión** (evaporación, compresión, condensación, expansión;
  recalentamiento, subenfriamiento): no he encontrado una fuente abierta citable; el redactor lo
  explicará como oficio declarado. Sí hay definiciones normativas en el RITE, apéndice 1 (bloque
  `apendice1`, leído 05-10-2026): «Climatización: acción y efecto de climatizar, es decir de dar a un
  espacio cerrado las condiciones de temperatura, humedad relativa, calidad del aire y, a veces,
  también de presión, necesarias para el bienestar de las personas y/o la conservación de las
  cosas.»; «Bomba de calor: Máquina, dispositivo o instalación que transfiere calor del entorno
  natural, como el aire, el agua o la tierra, al edificio… invirtiendo el flujo natural de calor, de
  modo que fluya de una temperatura más baja a una más alta…»; «COP… es la relación entre la
  capacidad calorífica y la potencia efectivamente absorbida por la unidad»; «EER… es la relación
  entre la capacidad frigorífica y la potencia efectivamente absorbida por la unidad»; «Local
  técnico: espacio destinado únicamente a albergar maquinaria de las instalaciones térmicas»; «Met:
  unidad metabólica; 1 met = 58,2 W/m2»; «Clo: … 1 clo = 0,155 m2 °C/W».
- **Averías frecuentes** de equipos (alta/baja presión, falta de refrigerante, hielo en evaporador,
  condensador sucio, compresor que dispara térmico): sólo tengo como fuente las señales de la IF-17
  2.5.3.2 y las gamas IDAE; un catálogo de averías con causa-efecto sería oficio.
- Composición de mezclas (R-410A, R-407C, R-454B…): no leída en fuente oficial (la IF-02 vigente la
  trae probablemente en sus tablas; no la he leído).
- Correcciones de errores del Reglamento (UE) 2024/573: no comprobadas.

## Tema 12 · Sistemas de gestión técnica de edificios y monitorización: BMS/SCADA, sensores, alarmas, históricos, telemedida y actuación ante avisos

Reuso RTVE (`ing-tec-industrial/13`): **todo él es oficio, sin una sola fuente citada** (lo dice su
trazabilidad). Se puede copiar como «oficio declarado», pero conviene anclarlo en lo que sigue.
RTVE §6 atribuye al «RITE, artículo 12.3» el control y al «artículo 2.1» la inclusión de la
automatización: **confirmado** en la redacción vigente (leído 05-10-2026). Art. 2.1: instalaciones
térmicas son las de climatización y ACS «incluidas las interconexiones a redes urbanas de calefacción
o refrigeración y los sistemas de automatización y control». Art. 12.3: «Regulación y control: las
instalaciones estarán dotadas de los sistemas de regulación y control necesarios para que se puedan
mantener las condiciones de diseño previstas en los locales climatizados, ajustando, al mismo tiempo,
los consumos de energía a las variaciones de la demanda térmica, así como interrumpir el servicio.»
Lo nuevo, con fuente:

### 12.1 Lo que exige el RITE del sistema de automatización y control (vigente; ver §0)

- Definición (apéndice 1): «Sistema de automatización y control de edificios: sistema que incluya
  todos los productos, programas informáticos y servicios de ingeniería que puedan apoyar el
  funcionamiento eficiente energéticamente, económico y seguro de las instalaciones técnicas del
  edificio mediante controles automatizados y facilitando su gestión manual de dichas instalaciones
  técnicas del edificio.»
- Niveles del sistema (apéndice 1; son los de la IT 2.3.4): «Nivel de unidades de campo: corresponde a
  los equipos de campo como: elementos primarios de medida, sondas, unidades de ambiente, termostatos,
  indicadores de estados y alarmas, así como elementos finales de control y mando, válvulas,
  actuadores, variadores de tensión/frecuencia…»; «Nivel de proceso: corresponde a los controladores,
  tanto analógicos como digitales, que manejan los elementos del nivel de periferia.»; «Nivel de
  comunicaciones: corresponde a todos los controladores e interfaces de comunicación del sistema de
  gestión, así como a los buses de comunicación, drivers, redes, etc.»; «Nivel de gestión y
  telegestión: corresponde a los puestos centrales, programas residentes y periféricos asociados a los
  puestos centrales, tales como impresoras, pantallas de vídeo, módems, routers, etc.» **(Esto da
  fuente normativa española a la «pirámide» que RTVE presenta como oficio, con cuatro niveles de
  nombres distintos: usar los del RITE.)**
- **IT 1.2.4.3.5.1 (obligación)**: «Cuando sea técnica y económicamente viable, los edificios no
  residenciales con una potencia nominal útil para instalaciones de calefacción, refrigeración,
  instalaciones combinadas de calefacción y ventilación, o para instalaciones combinadas de
  refrigeración y ventilación de más de 290 kW deberán estar equipados con sistemas de automatización
  y control de edificios.» Capacidades: «a) Monitorizar, registrar, analizar y permitir la adaptación
  del consumo de energía de forma continua; b) Efectuar una evaluación comparativa de la eficiencia
  energética del edificio, detectar las pérdidas de eficiencia de sus instalaciones técnicas e informar
  sobre las posibilidades de mejora… a la persona responsable de la instalación o de la gestión técnica
  del edificio; c) Permitir la comunicación con instalaciones técnicas conectadas y otros aparatos…, así
  como garantizar la interoperabilidad con instalaciones técnicas del edificio de distintos tipos de
  tecnologías patentadas, dispositivos y fabricantes.» Norma de referencia citada: «UNE-EN 15232-1».
  (Nota: la EN 15232-1 fue sustituida en el CEN por la EN ISO 52120-1 —dato no comprobado en fuente
  primaria; si no se confirma, citar sólo lo que dice el RITE.)
- IT 1.2.4.3.5.3: tras instalarlo, «acciones de comprobación de que el sistema funciona con arreglo a
  sus especificaciones y acciones de ajuste»; configurarlo para «las condiciones de bienestar e higiene
  establecidas en el artículo 11 con el mínimo consumo de energía»; sus instrucciones de operación
  «deberán recogerse en el "Manual de Uso y Mantenimiento"».
- Premio por tenerlo: IT 4.3.4, los no residenciales con sistema que cumpla la IT 1.2.4.3.5.1 quedan
  exentos de las inspecciones periódicas IT 4.2.1, 4.2.2 y 4.2.3 (ver 10.5). IT 3.3 tabla 3.1: hasta
  70 kW «con supervisión remota en continuo» la periodicidad de mantenimiento puede pasar «hasta 2
  años».
- Puesta en servicio (IT 2.3.4): verificación por niveles; «Son válidos a estos efectos los protocolos
  establecidos en la norma UNE-EN-ISO 16484-3»; mantenimiento y actualización de programas «por
  personal cualificado o por el mismo suministrador de los programas».
- Lo que el sistema debe registrar por exigencia del RITE (IT 1.2.4.4, ver 10.2): horas de
  funcionamiento de generadores > 70 kW y de bombas y ventiladores > 20 kW; arranques de compresores
  > 70 kW; consumos eléctricos y térmicos separados; IT 3.4.4.2: datos de consumo conservados «al
  menos, cinco años». IT 3.4.2: medidas trimestrales o mensuales de generadores de frío (temperaturas,
  presiones, potencia eléctrica, EER instantáneo, caudales): **son exactamente las variables que un
  BMS histórico debe guardar** (nota del investigador).
- Alarma de sala: IT 1.3.4.1.2.2.p): «instrucciones para efectuar la parada de la instalación en caso
  necesario, con señal de alarma de urgencia y dispositivo de corte rápido».

### 12.2 Puntos, señales, alarmas e históricos: fuente técnica IDAE (misma guía que 9.6)

- Tipos de punto (familia 23, «Ejemplo de listado de puntos de control»): «ED = Entrada Digital; SD =
  Salida Digital; SS = Salida de Supervisión; EA = Entrada Analógica; SA = Salida Analógica; CT =
  Contador». Tipos de sistema de control de la ficha: «neumática, electromecánica, electrónica, DDC».
  La guía recomienda incorporar a la ficha técnica «la información relativa a las lógicas de control
  establecidas, listado de componentes… y, como mínimo, de la relación de puntos de control a
  supervisar».
- Ejemplos literales de puntos: «Comando marcha/paro planta enfriadora GEA1», «Estado/alarma general
  planta enfriadora GEA1», «Señal falta de presión/agua en circuito primario agua fría», «Señal
  temperatura de impulsión de agua fría», «Comando regulación válvulas automáticas agua fría», «Fines
  de carrera válvulas automáticas agua fría», «Contador general de energía eléctrica», «Contador de
  suministro de energía eléctrica a climatización», y — muy del puesto — «Alarma alta temperatura en
  sala de informática».
- **Gama de mantenimiento «Control DDC (Computerizado)»** (familia 23), con frecuencias (leyenda en
  9.6):
  - A) Puestos de control y gestión centralizada: «57 Verificación de funcionamiento general.
    Análisis de históricos y tendencias de datos: T»; «58 Verificación de horarios y programas de mando
    de equipos y sistemas. Comprobación "in situ" de respuestas a señales de comando remoto en modos
    manual y automático: T»; «60 Realización de backup general de las bases de datos del puesto
    central: T»; «61 Realización de backup de ficheros históricos y reinicio de secuencias de
    almacenamiento, si procede: T»; «62 Comprobación del arranque del puesto central de gestión tras un
    fallo del suministro de tensión: 2.A»; «63 Verificación de funcionamiento de los Sistemas de
    Alimentación Ininterrumpida (SAI): 2.A»; «64 Evaluación de la obsolescencia del hardware instalado,
    sistema operativo y software de aplicación: A»; «53 Verificación de la fecha y la hora: T»; «54
    Verificación del cambio de horario invierno/verano: 2.A».
  - B) Controladores distribuidos: «72 Inspección del estado y conexionado de los "buses" de
    comunicación: T»; «73 Verificación de estado y carga de las baterías de los controladores: T»;
    «75 Inspección del histórico de fallos de comunicación: T»; «77 Contraste de las lecturas obtenidas
    de los controladores con reales tomadas directamente en campo: T»; «78 Comprobación de la
    respuesta de los elementos de campo a los comandos de los controladores: T»; «80 Inspección de la
    estabilidad y precisión de los bucles de control, secuencias y horarios: 2.A»; «82 Inspección y
    análisis de mensajes de alarmas y defectos de funcionamiento: T».
  - D) **Alarmas**: «86 Inspección del estado de los elementos emisores y receptores de alarmas: M»;
    «87 Simulación de alarmas y comprobación de su notificación sobre los terminales o impresoras
    predefinidas: M»; «88 Comprobación de la notificación remota de alarmas a impresoras u otros
    terminales: M».
  - E) Integraciones: «90 Comprobación de los tiempos de refresco: T»; «92 Comprobación de los valores
    reales en los equipos (en campo) con los presentados en el puesto de control: T».
  - F) **Telegestión**: «93 Inspección de la alimentación y conexionado de MODEM u otros dispositivos
    de comunicación remota: T»; «94 Comprobación del establecimiento de la comunicación y de la
    actuación remota del sistema: T».
  - G) Equipo de campo: «97 Verificación de reglajes y valores de consigna. Ajuste y calibración de
    elementos de regulación: 2.A».
  (Ojo: el PDF numera dos operaciones como «85»; tal cual.)
- Gama de autónomos/VRV, operaciones de control centralizado: «52 Inspección de anomalías acumuladas
  en la memoria del sistema de control centralizado: 2.A»; «53 Verificación de estado, conexiones,
  puntos de consigna y funcionamiento del sistema de control centralizado: 2.A».

### 12.3 Protocolos de comunicación (fuentes primarias de las normas)

- **BACnet**: ISO 16484-5:2022, «Building automation and control systems (BACS) — Part 5: Data
  communication protocol», séptima edición, 2022-09 (muestra pública del preámbulo en
  `cdn.standards.iteh.ai`, leída 05-10-2026). Cláusula 1: «The purpose of this standard is to define
  data communication services and protocols for computer equipment used for monitoring and control
  of HVAC&R and other building systems and to define, in addition, an abstract, object-oriented
  representation of information communicated between such equipment…». Cláusula 2.1: mensajes para
  «(a) hardware binary input and output values, (b) hardware analog input and output values, (c)
  software binary and analog values, (d) text string values, (e) schedule information, (f) alarm and
  event information, (g) files, and (h) control logic». 2.2: modela cada equipo «as a collection of
  data structures called "objects"». El índice incluye la red «MS/TP» (cláusula 9) y el anexo
  «BACnet/IP (NORMATIVE)» (anexo J). (Que BACnet lo mantiene el comité SSPC 135 de ASHRAE: sólo en
  fuente secundaria; no afirmar.)
- **Modbus**: «MODBUS Application Protocol Specification V1.1b3», Modbus Organization (descargada
  05-10-2026 de `https://www.modbus.org/file/secure/modbusprotocolspecification.pdf`): «MODBUS is an
  application layer messaging protocol, positioned at level 7 of the OSI model, which provides
  client/server communication between devices connected on different types of buses or networks.»;
  «MODBUS is a request/reply protocol and offers services specified by function codes.»; acceso por
  «port 502 on the TCP/IP stack». Tablas primarias: «Discretes Input — Single bit — Read-Only»;
  «Coils — Single bit — Read-Write»; «Input Registers — 16-bit word — Read-Only»; «Holding Registers —
  16-bit word — Read-Write».
- **KNX** (ISO/IEC 14543-3) y **LonWorks** (ISO/IEC 14908): sólo confirmados en fuentes secundarias
  (búsqueda web; iso.org bloquea con 403). Si el redactor los nombra, que diga sólo el número de
  norma y declare la fuente, o que los quite.
- Seguridad de red OT (separación BMS/ofimática que trae RTVE como oficio): no he buscado fuente
  (candidatas: serie IEC 62443, guías del INCIBE-CERT). Queda como oficio.

### 12.4 Lo que no he podido confirmar (tema 12)

- **SCADA**: no tengo definición normativa ni de manual abierto; queda como oficio.
- **Telemedida** en sentido legal (lectura remota de contadores eléctricos, Reglamento unificado de
  puntos de medida, RD 1110/2007): no investigado. En el sentido del enunciado basta lo del RITE
  (IT 1.2.4.4 contadores; IT 3.4.4-3.4.5 seguimiento y publicidad de consumos) y la gama IDAE de
  telegestión.
- Señales 4-20 mA / 0-10 V que trae RTVE: sin fuente normativa leída (la IEC 60381-1 trata señales
  analógicas de corriente: no leída). Mantener como oficio.
- «Actuación ante avisos»: ninguna norma leída fija un protocolo; hay apoyo en RITE art. 25.3
  («Se pondrá en conocimiento del responsable de mantenimiento cualquier anomalía…»), IF-14 1.3.1 (orden
  del correctivo con refrigerante), IF-17 2.5.1 (fuga: «actuando de inmediato… y parando las
  instalaciones si la fuga es significativa») y art. 29 del RD 552/2019 (notificación de accidentes en
  24 horas). El resto es oficio.

## Tema 16 · Eficiencia energética y sostenibilidad en instalaciones

Reuso RTVE (`ing-tec-industrial/12`): RD 390/2021 (§1-2), RD 1890/2008 (§3), RD 56/2016 (§4), RD
163/2014 (§5, voluntario: el enunciado no lo pide; el redactor decidirá si lo deja). El enunciado del
puesto pide «ahorro energético, monitorización de consumos, mantenimiento orientado a eficiencia,
tecnología LED, climatización eficiente y gestión de residuos»; RTVE cubre la parte de certificación,
auditorías y alumbrado exterior.

### 16.1 RD 390/2021 tras el RD 659/2025 (vigente desde 23-07-2026)

Fuente: `BOE-A-2021-9176`, vigente, leído 05-10-2026. La reforma la hace el **Real Decreto 659/2025,
de 22 de julio, por el que se modifica el Real Decreto 390/2021** (`BOE-A-2025-15230`, BOE 176 de
23-07-2025); los avisos del consolidado dicen que «entra en vigor el 23 de julio de 2026, según
determina su disposición final única».

- Lo que RTVE copia y **sigue igual en sustancia**:
  - Art. 1.2 (cita literal de RTVE): una sola redacción, sin cambios. Vale.
  - Art. 3.1 a)-f) y 3.2 a)-e): texto vigente coincide con lo que RTVE resume (250 m² Administración;
    > 25 % envolvente; > 10 % y > 50 m² en ampliación; > 500 m² y once usos; exclusiones de 2 años y
    50 m²). **Único cambio**: el párrafo segundo del 3.2 dice ahora «Para hacer efectiva la exclusión
    recogida en este apartado e)…» (antes decía «apartado f)», errata corregida) y añade «o de la
    ciudad de Ceuta o Melilla». RTVE no lo cita literal: no le afecta.
  - Art. 6: apartados 1-5 y 6.1.º párrafo iguales; cambia el párrafo segundo del 6.6, que ahora dice
    sólo: «El citado registro permitirá realizar las labores de control técnico y administrativo e
    inspección recogidas en los artículos 11 y 12 y servirá de acceso a la información sobre los
    certificados a los ciudadanos.» (desaparece la mención a registros de técnicos, que pasa a los
    nuevos arts. 4 ter, 4 quáter y 7 bis).
  - Art. 8.1 (los elementos de la certificación): una sola redacción. **Ojo: RTVE dice «Los tres
    elementos» y el art. 8.1 tiene seis letras**: «a) Documento específico Certificado de Eficiencia
    Energética del edificio. b) Etiqueta de Eficiencia Energética. c) Informe de evaluación energética
    del edificio en formato electrónico (XML). d) Documentos o ficheros digitales necesarios para la
    evaluación… e) Anexos y cálculos justificativos… f) Recomendaciones de uso para el usuario.» y
    añade: «Los modelos oficiales de los elementos a), b) y c) serán publicados como documentos
    reconocidos.» **Error de recuento de RTVE (error 3): corregir al copiar.**
  - Art. 8.2.f).3.º (útil para tema 12): entre las recomendaciones del certificado, «La incorporación
    de sistemas de automatización y control».
- **Nuevo y vigente**:
  - Art. 4 bis: requisitos del técnico competente. Para certificar edificios existentes (3.1.b, c, e,
    f) vale, entre otros, «d) Acreditar estándares de competencia en eficiencia energética en
    edificios, obtenidos a través de un título de Formación Profesional de Grado Superior, de un
    Certificado Profesional o, de un Curso de Especialización, de nivel 3…», con los módulos 1 y 2 del
    curso del anexo I. (Interesa a un oficial electricista B03 sólo como curiosidad; el redactor
    decide.)
  - Art. 4 ter: acreditación por «declaración responsable ante el órgano competente… de la comunidad
    autónoma… en la que tenga su domicilio fiscal»; «Habilitará para el ejercicio de la actividad en
    todo el territorio nacional».
  - Art. 7 bis: «Se crea, en la Dirección General de Planificación y Coordinación Energética del
    Ministerio para la Transición Ecológica y el Reto Demográfico, el Registro Administrativo
    Centralizado de Técnicos Competentes en materia de certificación de eficiencia energética de
    edificios.» (**RTVE dice que el 7 bis «no estaba en vigor» y que no afirma su contenido: ahora
    está en vigor; sustituir esa declaración.**)
  - Art. 9.1 y 10: el técnico competente se remite ahora a «los artículos 4 bis, 4 ter y 4 quáter»
    (antes «artículo 2.u)»). El art. 2 se ha reordenado: la letra u) es hoy la definición de «Sistema
    de automatización y control de edificios» (aviso del consolidado: «supresión de las actuales
    letras u), v) y la reordenación de la w) como u)»).
- Sin cambios y útiles para el puesto: art. 13.1: «El certificado de eficiencia energética tendrá una
  validez máxima de diez años, excepto cuando la calificación energética sea G, cuya validez máxima
  será de cinco años.» Art. 16.1: los edificios de los artículos 3.1.c) y 3.1.e) «exhibirán la
  etiqueta de eficiencia energética de forma obligatoria, en lugar destacado y bien visible por el
  público» (aplica a un edificio de una entidad pública de más de 250 m²: nota del investigador).

### 16.2 RD 56/2016 (auditorías) y Directiva (UE) 2023/1791

- RD 56/2016 vigente sin cambios posteriores a 2022 (ver §0). Art. 2.1: grandes empresas, «tanto las
  que ocupen al menos a 250 personas como las que, aun sin cumplir dicho requisito, tengan un volumen
  de negocio que exceda de 50 millones de euros y, a la par, un balance general que exceda de 43
  millones de euros». Art. 3.1: «auditoría energética cada cuatro años… que cubra, al menos, el 85 por
  ciento del consumo total de energía final». Art. 3.2: alternativa de «sistema de gestión energética
  o ambiental, certificado por un organismo independiente». (Coinciden con RTVE.)
- **Directiva (UE) 2023/1791**, de 13 de septiembre de 2023, «relativa a la eficiencia energética y por
  la que se modifica el Reglamento (UE) 2023/955 (versión refundida)», DO L 231 de 20-9-2023; texto
  descargado 05-10-2026 de la Oficina de Publicaciones (`resource/celex/32023L1791`, español) y
  guardado en `fuentes/canal-sur/documentos/directiva-ue-2023-1791.txt` (texto original, no
  consolidado).
  - Art. 38: «Queda derogada con efectos a partir del 12 de octubre de 2025 la Directiva 2012/27/UE»
    (la que transpone el RD 56/2016).
  - Art. 36.1: transposición de la mayor parte (incluidos los arts. 5 a 11) «a más tardar el 11 de
    octubre de 2025».
  - **Transposición española: no encontrada.** Búsqueda en el BOE por título («2023/1791»,
    «auditorías energéticas», «eficiencia energética», 2023-2026) el 05-10-2026: ningún real decreto
    que la transponga ni que modifique el RD 56/2016. **Conclusión que el redactor puede afirmar con
    esa salvedad**: a la fecha de lectura el RD 56/2016 sigue rigiendo con los criterios de la Directiva
    2012/27/UE, y la Directiva 2023/1791 obliga a los Estados, no directamente a las empresas (art. 40:
    «Los destinatarios de la presente Directiva son los Estados miembros»).
  - Art. 11.1: empresas con consumo medio anual «superior a 85 TJ durante los tres años anteriores»:
    sistema de gestión de la energía certificado, «a más tardar el 11 de octubre de 2027». Art. 11.2:
    «superior a 10 TJ» sin sistema de gestión: auditoría energética, la primera «a más tardar el 11 de
    octubre de 2026» y después «al menos cada cuatro años»; plan de acción a partir de las
    recomendaciones. (Cambia el criterio: de tamaño de empresa a consumo de energía.)
  - Art. 5.1 (sector público): consumo de energía final de todos los organismos públicos reducido «al
    menos en un 1,9 % cada año, en comparación con 2021»; 5.2: indicativo hasta el «11 de octubre de
    2027». Art. 6.1: renovar cada año «al menos el 3 % de la superficie total de los edificios con
    calefacción y/o sistema de refrigeración que sean propiedad de sus organismos públicos»; cuota
    sobre edificios de «más de 250 m2». (Si RTVA/CSRTV es «organismo público» a efectos de la
    Directiva: **no lo he comprobado**; ver la definición del art. 2 antes de afirmarlo.)
  - **Art. 12.1 (centros de datos)**: los Estados exigirán «a los propietarios y operadores de centros
    de datos de su territorio, con una potencia eléctrica demandada por los sistemas de tecnologías de
    la información (TI) de 500 kW como mínimo», publicar la información del anexo VII, «a más tardar el
    15 de mayo de 2024 y posteriormente cada año». (Relevante para el CPD de un ente audiovisual si
    supera 500 kW TI; el anexo VII y su desarrollo nacional no los he leído.)

### 16.3 Monitorización de consumos, mantenimiento orientado a eficiencia y climatización eficiente

Todo esto ya está con cita en este informe; el redactor del tema 16 lo toma de ahí:
- Contabilización y registro (RITE IT 1.2.4.4): ver 10.2.
- Programa de gestión energética, asesoramiento, seguimiento de consumos 5 años e información pública
  (IT 3.4.1-3.4.5): ver 10.4.
- Medidas periódicas de generadores de frío y EER (IT 3.4.2) y límite de EER ≥ 2 en inspección
  (IT 4.2.2.3.a): ver 10.4-10.5.
- Limitación de temperaturas 21/26 °C (IT 3.8): ver 10.4.
- Enfriamiento gratuito > 70 kW y recuperación de calor > 0,28 m³/s (IT 1.2.4.5): ver 10.2.
- Sistemas de automatización y control > 290 kW (IT 1.2.4.3.5): ver 12.1.
- Gases fluorados de bajo PCG y prohibiciones (Reglamento 2024/573): ver 9.1. IF-17 2.3.c) del RD
  552/2019: «Se procurará reducir en lo posible las necesidades frigoríficas, por ejemplo utilizando
  el almacenamiento térmico, frío natural del aire ambiente (freecooling), etc.»; 2.3.d): «Se reducirá
  lo máximo posible la carga de refrigerante.»
- IF-14 1.2.1.c): el programa de mantenimiento del frío incluye el «Control de los rendimientos
  energéticos de la instalación».

### 16.4 Gestión de residuos

- RD 110/2015, de residuos de aparatos eléctricos y electrónicos (`BOE-A-2015-1762`), anexo III
  vigente (vig. 21-04-2022, `BOE-A-2022-5142`), leído 05-10-2026: «Categorías y subcategorías de AEE
  incluidos en el ámbito de aplicación del real decreto a partir del 15 de agosto de 2018»: «1.
  Aparatos de intercambio de temperatura. 1.1 Aparatos eléctricos de intercambio de temperatura con
  clorofluorocarburos (CFC), hidroclorofluorocarburos (HCFC), hidrofluorocarburos (HFC),
  hidrocarburos (HC) o amoníaco (NH3). 1.2 Aparatos eléctricos de aire acondicionado. 1.3 Aparatos
  eléctricos con aceite en circuitos o condensadores.» … «3. Lámparas. 3.1 Lámparas de descarga
  (mercurio) y lámparas fluorescentes. 3.2 Lámparas LED.» Las luminarias van en las categorías 4
  (grandes) o 5 (pequeños). No he leído el articulado sobre obligaciones del poseedor/usuario
  profesional: hacerlo antes de afirmar quién entrega a quién.
- Refrigerantes y aceites: RD 552/2019 art. 25.1 (desmantelamiento: residuos «entregados a un gestor de
  residuos»); IF-17 1.1 y 1.5.1 (CFC/HCFC a destrucción); IF-14 1.2.4.2 (aceite drenado gestionado
  según «la Ley 22/2011»; «El aceite nunca deberá verterse en alcantarillas…»). **Ojo**: la Ley 22/2011
  la derogó la Ley 7/2022, de residuos y suelos contaminados para una economía circular (dato no
  comprobado en el BOE en esta sesión: comprobar la disposición derogatoria de la Ley 7/2022,
  `BOE-A-2022-5809`, antes de afirmarlo). Reglamento 2024/573, art. 8 (recuperación; reciclado,
  regeneración o destrucción).
- Empresas frigoristas: art. 12.1.a).4.º RD 552/2019 vigente, «plan de gestión de residuos… y que
  contemplará su inscripción como pequeño productor de residuos peligrosos».

### 16.5 Lo que no he podido confirmar (tema 16)

- **Tecnología LED**: no he investigado fuente (candidatas: Reglamento (UE) 2019/2020 de diseño
  ecológico de fuentes luminosas, Reglamento delegado (UE) 2019/2015 de etiquetado energético; el
  informe B, tema 6, trae luminarias). Sin fuente leída, el redactor no debe dar cifras de eficacia
  (lm/W), vida útil ni prohibiciones de fluorescentes.
- Transposición española de la Directiva 2023/1791 (no encontrada; ver 16.2).
- Si RTVA/CSRTV encaja en «organismo público» (Directiva art. 2) y si debe auditarse (RD 56/2016 art.
  2, por plantilla ≥ 250): no comprobado; es dato propio de la RTVA que no consta en documento leído.
- RD 1890/2008: la ITC-EA-01 cambió con vigencia 01-01-2023 (RDL 18/2022, `BOE-A-2022-17040`), después
  del corte de RTVE; RTVE sólo la nombra «requisitos de eficiencia y etiqueta», así que su texto vale;
  pero cualquier cifra de la EA-01 hay que leerla en la versión vigente (volcado nuevo en
  `fuentes/canal-sur/BOE-A-2008-18634.md`). Las medidas temporales del RDL 14/2022 sobre alumbrado
  (escaparates apagados desde las 22 h) rigieron «desde el 10 de agosto de 2022 al 1 de noviembre de
  2023» (nota del consolidado): ya no rigen.

---

## Resumen para el redactor

| Tema | RTVE vale | Correcciones a lo de RTVE | Lo nuevo con fuente | Huecos |
|---|---|---|---|---|
| 9 | Sí (RD 552/2019 sin cambios en lo citado) | Art. 18.p) incompleto; IF-17 remite al Reg. 517/2014 derogado | Reg. UE 2024/573 (fugas, registros, prohibiciones); IF-14 e IF-17; RITE condiciones interiores, IDA, filtros, THM-C; gamas IDAE; ASHRAE 18-27 °C | Ciclo frigorífico y averías tipo (oficio); composición de mezclas; correcciones del 2024/573 |
| 10 | Sí, RITE sin cambios desde 01-07-2021 | Sólo el pie de redacción; ojo 19/27 °C caducado | IT 1.3 salas de máquinas, arts. 19-25, IT 2, IT 3 completas (tablas), IT 4 periodicidad 4 y 15 años | — |
| 12 | Sólo como oficio (sin fuentes) | Usar los cuatro niveles del RITE (apéndice 1) en lugar de la «pirámide» sin fuente | RITE IT 1.2.4.3.5 (> 290 kW), IT 2.3.4, apéndice 1; IDAE puntos ED/EA/SD/SA y gama DDC (alarmas, históricos, telegestión); BACnet ISO 16484-5; Modbus | SCADA, telemedida legal, 4-20 mA, KNX/LON sin fuente primaria |
| 16 | Parcialmente | RD 390/2021 reformado (RD 659/2025): art. 7 bis vigente; art. 8.1 tiene seis elementos, no tres | RD 659/2025; Directiva 2023/1791 (arts. 5, 6, 11, 12, 36, 38); RAEE anexo III | LED; transposición de la Directiva; Ley 7/2022 |

Fuentes descargadas o volcadas en esta fase (todas el 05-10-2026): `fuentes/canal-sur/BOE-A-2007-15820.*`,
`BOE-A-2019-15228.*`, `BOE-A-2021-9176.*`, `BOE-A-2016-1460.*`, `BOE-A-2008-18634.*`;
`fuentes/canal-sur/documentos/reglamento-ue-2024-573.txt`, `directiva-ue-2023-1791.txt`,
`idae-guia-mantenimiento-termicas.{pdf,txt}`. Consultadas sin guardar: ASHRAE TC 9.9 Reference Card
(xp20.ashrae.org), muestra ISO 16484-5:2022 (cdn.standards.iteh.ai), MODBUS Application Protocol
Specification V1.1b3 (modbus.org), RDL 14/2022 (`BOE-A-2022-12925`, art. 29 y DF 17.ª), RD 110/2015
(`BOE-A-2015-1762`, anexo III), títulos de `BOE-A-2025-17507` (RD 770/2025, de 2 de septiembre,
régimen de contratación de profesionales habilitados), `BOE-A-2026-17906` (Resolución de 5 de agosto
de 2026, que amplía la relación de refrigerantes autorizados) y `BOE-A-2022-17040` (RDL 18/2022).
