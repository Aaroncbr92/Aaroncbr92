# Puesto 27 · Oficial Técnico Electricista · Investigación del bloque D-mantenimiento (temas 13, 17, 18 y 19)

Fase 1 · Investigar. Fecha de lectura de todas las fuentes: **05-10-2026** (el encargo fija «hoy» en 24-09-2026;
ninguna de las normas usadas tiene una redacción con vigencia entre ambas fechas, salvo lo que se dice expresamente).
Sólo se investiga lo que el material reutilizable (RTVE y común) no cubre o lo que ha cambiado desde la fecha de
RTVE (21-12-2022). Lo de RTVE y lo del común lo lee el redactor; aquí no se repite.

Convención: **negrita entre comillas = literal de la fuente**; lo demás es descripción mía. «No confirmado» = no se
escribe en el tema como dato.

## 0. Fuentes leídas y ficheros tocados

| Fuente | Identificador / ubicación | Leída |
|---|---|---|
| RD 1027/2007, RITE (consolidado; bloques IT 1, IT 2 vigentes desde 01-07-2021 por RD 178/2021, `BOE-A-2021-4572`) | `BOE-A-2007-15820`, `fuentes/canal-sur/` (volcado 05-10-2026, de otro bloque) | 05-10-2026 |
| RD 244/2019, autoconsumo (consolidado) | `BOE-A-2019-5089`, volcado nuevo en `fuentes/canal-sur/` | 05-10-2026 |
| RD 1699/2011, conexión de pequeña potencia (consolidado) | `BOE-A-2011-19242`, volcado nuevo en `fuentes/canal-sur/` | 05-10-2026 |
| RD-ley 7/2026, de 20 de marzo (título por API BOE) y su convalidación (Resolución de 26-03-2026, `BOE-A-2026-7125`) | `BOE-A-2026-6544` | 05-10-2026 |
| Reglamento (UE) 2023/1542, pilas y baterías (texto original BOE-DOUE, **no consolidado**) + 4 correcciones | `DOUE-L-2023-81096` y `DOUE-L-2024-80529`, `-2024-81259`, `-2025-81464`, `-2026-80534`, en `fuentes/canal-sur/` | 05-10-2026 |
| Reglamento (UE) 2025/1561 (sólo título, por buscador) | `DOUE-L-2025-81177` | 05-10-2026 |
| RD 56/2016, auditorías energéticas (consolidado) | `BOE-A-2016-1460`, volcado nuevo | 05-10-2026 |
| RD 1215/1997, equipos de trabajo (consolidado) | `BOE-A-1997-17824`, volcado nuevo | 05-10-2026 |
| RD 39/1997, Reglamento de los Servicios de Prevención, art. 22 bis | `BOE-A-1997-1853`, volcado nuevo | 05-10-2026 |
| RD 485/1997, 487/1997, 374/2001 (sólo para comprobar que no han cambiado desde 2022) | `BOE-A-1997-8668`, `-8670`, `BOE-A-2001-8436`, volcados nuevos | 05-10-2026 |
| RD 393/2007, Norma Básica de Autoprotección, anexo II | `BOE-A-2007-6237` (volcado existente) | 05-10-2026 |
| Ley 8/2011, infraestructuras críticas, art. 2 | `BOE-A-2011-7630` (lectura por `boe.py precepto`) | 05-10-2026 |
| Ley 7/2025, de 22 de diciembre, del Patrimonio de la Comunidad Autónoma de Andalucía, art. 136 | `BOE-A-2026-944` (volcado existente) | 05-10-2026 |
| Reglamento (CE) 1272/2008 (CLP), texto original BOE-DOUE, **no consolidado** | `DOUE-L-2008-82637`, volcado nuevo | 05-10-2026 |
| Reglamento (UE) 2024/2865 (modifica CLP) y Reglamento (UE) 2025/2439 (aplaza fechas) | `DOUE-L-2024-81721`, `DOUE-L-2025-81843`, volcados nuevos | 05-10-2026 |
| X Convenio colectivo RTVA (BOJA 240, 10-12-2014), ficha del puesto 9311100 | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | 05-10-2026 |
| RD 401/2023 (títulos FP, incl. Sistemas Electrotécnicos y Automatizados), texto BOE sin consolidar | `BOE-A-2023-13217`, guardado en `fuentes/canal-sur/tecnica/BOE-A-2023-13217.{html,txt}` | 05-10-2026 |
| Catálogo de UNE/AENOR (fichas públicas: título, fecha, estado, «anula a», equivalencia). **Sólo metadatos**; el texto de las normas UNE no se ha leído | tienda.aenor.com, fichas citadas en cada punto | 05-10-2026 |
| Vistas previas oficiales de ISO/IEC 30173:2023 e ISO/IEC 30141:2024 (iTeh Standards, primeras páginas) | cdn.standards.iteh.ai (no guardadas en `fuentes/`) | 05-10-2026 |

**Ficheros creados o tocados** (además de este informe): volcados nuevos en `fuentes/canal-sur/` de
`BOE-A-2019-5089`, `BOE-A-2011-19242`, `BOE-A-2016-1460`, `BOE-A-1997-17824`, `BOE-A-1997-1853`,
`BOE-A-1997-8668`, `BOE-A-1997-8670`, `BOE-A-2001-8436` (cada uno con su `.redacciones.tsv`),
`DOUE-L-2023-81096` y sus 4 correcciones, `DOUE-L-2008-82637` y sus correcciones, `DOUE-L-2024-81721`,
`DOUE-L-2025-81843`; y `fuentes/canal-sur/tecnica/BOE-A-2023-13217.{html,txt}`. No he tocado temas.

**Fuentes que no se pudieron abrir** (lo que dependa de ellas queda «no confirmado»): texto de las normas UNE-EN
13306, 13460, 17007, 15341, 50110-1, ISO 22301/22313, ISO 17359 (de pago; sólo ficha de catálogo); IEC 60050-192
(Electropedia, 403 desde este entorno); iso.org y une.org (403); EUR-Lex (bloqueo 202, sin texto consolidado).

---

## 1. Tema 13 · Mantenimiento preventivo, correctivo y predictivo: gamas, órdenes de trabajo, diagnóstico, priorización, trazabilidad, repuestos, inventario y documentación técnica

RTVE (teitse/09 §6 y tese/15 §1-2) da los tipos, el plan por tareas y el método de diagnóstico. Falta: el marco
normativo (qué norma define los tipos), gamas, órdenes de trabajo, priorización, trazabilidad/registro, repuestos e
inventario, y GMAO.

### 1.1 La norma de terminología: UNE-EN 13306:2018 (sólo ficha de catálogo)

Ficha AENOR (tienda.aenor.com/p/norma-une-en-13306-2018-n0060338), leída 05-10-2026:
**«UNE-EN 13306:2018 Mantenimiento. Terminología del mantenimiento.»** · **«Fecha edición: 2018-07-11 En Vigor»** ·
**«CTN 151 - Mantenimiento»** · **«Anula a UNE-EN 13306:2011»** · **«Equivalencia Internacional Idéntica EN 13306:2017»**.

Normas de la misma familia que la ficha lista como relacionadas, todas **«En Vigor»** (título y fecha literales):

| Norma | Título | Fecha |
|---|---|---|
| UNE-EN 15341:2020+A1:2023 | **«Mantenimiento. Indicadores clave de rendimiento del mantenimiento.»** | 2023-03-08 |
| UNE-EN 17948:2025 | **«Gestión del mantenimiento y funciones.»** | 2025-09-03 |
| UNE-EN 17666:2024 | **«Mantenimiento. Ingeniería de mantenimiento. Requisitos.»** | 2024-01-17 |
| UNE-EN 17485:2023 | **«Mantenimiento. Mantenimiento en el marco de la gestión de activos físicos. Marco para mejorar el valor de los activos físicos a lo largo de todo su ciclo de vida.»** | 2023-04-05 |
| UNE-EN 13460:2009 | **«Mantenimiento. Documentos para el mantenimiento.»** (ficha propia: **«Fecha edición: 2009-12-22 En Vigor Fecha de confirmación: 2014-07-19»**, **«Anula a UNE-EN 13460:2003»**, idéntica a EN 13460:2009) | 2009-12-22 |
| UNE-EN 17007:2018 | **«Proceso de mantenimiento e indicadores asociados.»** (ficha propia: **«Fecha edición: 2018-05-30 En Vigor Fecha de confirmación: 2025-02-12»**, idéntica a EN 17007:2017) | 2018-05-30 |

**No confirmado: las definiciones de UNE-EN 13306:2018.** No he podido leer la norma (de pago; IEC 60050-192,
que es la fuente libre equivalente, devuelve 403). Lo que circula en la red son copias no autorizadas o
reproducciones secundarias. Una reproducción secundaria localizable es un pliego público de Transports de
Barcelona (NT G001/002, versión 08), que cita las definiciones de la **edición 2010** (no la vigente):
**«Mantenimiento preventivo: mantenimiento que se realiza a intervalos predeterminados o de acuerdo con criterios
preestablecidos, y que está destinado a reducir la probabilidad del fallo o la degradación del funcionamiento de un
elemento»**; preventivo dividido en **«Predeterminado (programado)»** y **«Basado en la Condición»**; **«El
Mantenimiento Predictivo es un mantenimiento basado en la Condición que se realiza siguiendo una predicción…»**;
correctivo **«inmediato»** y **«diferido»**. El mismo pliego advierte que el **«Mantenimiento Legal o Normativo
[…] (No contemplado en UNE-EN 13306)»**. Uso recomendado al redactor: **sólo la estructura** (el predictivo es una
forma de mantenimiento basado en la condición, que a su vez es preventivo; el correctivo puede ser inmediato o
diferido), atribuida a «la terminología normalizada (UNE-EN 13306)» **sin comillas ni texto literal**, y avisando
de que la edición vigente es la de 2018. Ojo: la tabla de RTVE (teitse/09 §6) presenta «PREDICTIVO o por
CONDICIÓN» como tercer tipo al lado del preventivo; en la terminología normalizada es una **subclase** del
preventivo. Si el redactor copia la tabla, debe añadir esa precisión.

**Juicios de RTVE sin fuente** que conviene no copiar como dato: teitse/09 §6 «El más barato en instalaciones
grandes» (predictivo) y tese/15 §1 «una hora de preventivo cuesta menos que una hora de correctivo». No los he
encontrado en ninguna fuente normativa; si se copian, como costumbre de oficio.

### 1.2 Lo que las normas españolas exigen del mantenimiento: obligación, programa, registro, plazo de conservación

Base legal general (equipos de trabajo). **RD 1215/1997, art. 3.5** (redacción única, vig. 27-08-1997):
**«El empresario adoptará las medidas necesarias para que, mediante un mantenimiento adecuado, los equipos de
trabajo se conserven durante todo el tiempo de utilización en unas condiciones tales que satisfagan las
disposiciones del segundo párrafo del apartado 1. Dicho mantenimiento se realizará teniendo en cuenta las
instrucciones del fabricante o, en su defecto, las características de estos equipos, sus condiciones de
utilización y cualquier otra circunstancia normal o excepcional que pueda influir en su deterioro o desajuste.»**
Párrafo 2: **«Las operaciones de mantenimiento, reparación o transformación de los equipos de trabajo cuya
realización suponga un riesgo específico para los trabajadores sólo podrán ser encomendadas al personal
especialmente capacitado para ello.»**

**RD 1215/1997, art. 4** (comprobaciones): 4.1 comprobación **«inicial, tras su instalación y antes de la puesta en
marcha por primera vez, y a una nueva comprobación después de cada montaje en un nuevo lugar o emplazamiento»**;
4.2 comprobaciones periódicas y **«adicionales […] cada vez que se produzcan acontecimientos excepcionales, tales
como transformaciones, accidentes, fenómenos naturales o falta prolongada de uso»**; 4.3 **«Las comprobaciones
serán efectuadas por personal competente.»**; 4.4 **«Los resultados de las comprobaciones deberán documentarse y
estar a disposición de la autoridad laboral. Dichos resultados deberán conservarse durante toda la vida útil de los
equipos.»** (trazabilidad).

**RD 1215/1997, anexo II, apartado 1** (redacción vig. 03-12-2004, RD 2177/2004):
- punto 14: **«Las operaciones de mantenimiento, ajuste, desbloqueo, revisión o reparación de los equipos de
  trabajo que puedan suponer un peligro para la seguridad de los trabajadores se realizarán tras haber parado o
  desconectado el equipo, haber comprobado la inexistencia de energías residuales peligrosas y haber tomado las
  medidas necesarias para evitar su puesta en marcha o conexión accidental mientras esté efectuándose la
  operación.»** + **«Cuando la parada o desconexión no sea posible, se adoptarán las medidas necesarias para que
  estas operaciones se realicen de forma segura o fuera de las zonas peligrosas.»**
- punto 15: **«Cuando un equipo de trabajo deba disponer de un diario de mantenimiento, éste permanecerá
  actualizado.»**
- punto 16: **«Los equipos de trabajo que se retiren de servicio deberán permanecer con sus dispositivos de
  protección o deberán tomarse las medidas necesarias para imposibilitar su uso.»**

Instalaciones térmicas (tema 10, pero sirve de modelo de «programa + registro»). **RITE art. 26.4**
(vig. 19-03-2010): **«El "Manual de Uso y Mantenimiento" de la instalación térmica debe contener las instrucciones
de seguridad y de manejo y maniobra de la instalación, así como los programas de funcionamiento, mantenimiento
preventivo y gestión energética.»** **Art. 27** (redacción única, 2007), «Registro de las operaciones de
mantenimiento»: **«1. Toda instalación térmica debe disponer de un registro en el que se recojan las operaciones de
mantenimiento y las reparaciones que se produzcan en la instalación, y que formará parte del Libro del Edificio.»**
**«2. […] Se deberá conservar durante un tiempo no inferior a cinco años, contados a partir de la fecha de
ejecución de la correspondiente operación de mantenimiento.»** **«3. La empresa mantenedora confeccionará el
registro y será responsable de las anotaciones en el mismo.»** La tabla de operaciones y periodicidades está en la
IT 3.3 (tabla 3.1); no la reproduzco: es materia del tema 10.

Protección contra incendios. **RIPCI (RD 513/2017), art. sobre mantenimiento, apdo. 6** (`BOE-A-2017-6606`, línea
866 del volcado): **«En todos los casos, tanto la empresa que ha llevado a cabo el mantenimiento, como el usuario o
titular de la instalación, conservarán constancia documental del cumplimiento del programa de mantenimiento
preventivo, al menos durante cinco años […]»**. (El número de artículo lo tiene el informe del bloque B, tema 11;
el redactor debe tomarlo de allí.)

Autoprotección. **RD 393/2007, anexo II, capítulo 5 «Programa de mantenimiento de instalaciones»**: **«5.1
Descripción del mantenimiento preventivo de las instalaciones de riesgo, que garantiza el control de las
mismas.»** **«5.2 Descripción del mantenimiento preventivo de las instalaciones de protección, que garantiza la
operatividad de las mismas.»** **«5.3 Realización de las inspecciones de seguridad de acuerdo con la normativa
vigente.»** + **«Este capítulo se desarrollará mediante documentación escrita y se acompañará al menos de un
cuadernillo de hojas numeradas donde queden reflejadas las operaciones de mantenimiento realizadas, y de las
inspecciones de seguridad, conforme a la normativa de los reglamentos de instalaciones vigentes.»**

Electricidad (REBT art. 20 e ITC-BT-05): ya en el informe del bloque A, §3.1-3.3. No se repite.

Vocabulario autonómico (sólo como muestra de uso oficial). **Ley 7/2025, de 22 de diciembre, del Patrimonio de la
Comunidad Autónoma de Andalucía, art. 136.3.f)** (vig. 20-01-2026), entre las competencias del órgano responsable
del edificio administrativo: **«La conservación y el mantenimiento preventivo, correctivo, sustitutivo, conductivo y
técnico-legal del edificio y sus instalaciones, necesario para garantizar su correcto estado.»** La ley no define
esos cinco términos (búsqueda en el volcado: sólo aparecen ahí). **No confirmado** que el art. 136 se aplique a los
edificios de la RTVA (se refiere a «edificios administrativos»); úsese sólo como ejemplo de terminología.

### 1.3 Gamas, órdenes de trabajo, priorización, repuestos, inventario y GMAO: lo que hay en fuente oficial

- **No he encontrado definición normativa** (BOE/BOJA) de «gama de mantenimiento», «orden de trabajo» ni «GMAO».
  Son términos de oficio; la norma que los ordena (UNE-EN 13460, documentos para el mantenimiento; UNE-EN 17007,
  procesos) no se ha podido leer. El redactor debe presentarlos **como práctica de oficio**, sin atribuirles
  contenido normativo.
- Sí constan como contenido oficial de formación, lo que prueba que son materia del oficio:
  - **RITE, apéndice de conocimientos para el carné** (bloque «A3.2», punto 2, «Mantenimiento de instalaciones
    térmicas»): **«Técnicas y criterios de organización, planificación y programación del mantenimiento preventivo
    y correctivo de averías. Planteamiento y preparación de los trabajos de mantenimiento. Técnicas de diagnosis y
    tipificación de averías.»** y **«Conocimientos específicos sobre: gestión económica del mantenimiento, gestión
    de almacén y material de mantenimiento. Gestión del mantenimiento asistido por ordenador.»**; punto 6:
    **«Gamas de actuación en intervenciones en mantenimiento preventivo y correctivo y para la reparación de
    averías características.»** (volcado `BOE-A-2007-15820`, líneas 2895 y 2904; el apéndice exacto lo debe fijar
    el redactor con `boe.py buscar`).
  - **RD 401/2023** (títulos de FP; módulo de gestión del montaje y mantenimiento de instalaciones automáticas),
    criterios de evaluación: **«Se ha cumplimentado la orden de reparación de la avería.»**, **«Se ha elaborado un
    plan detallado de mantenimiento productivo total (TPM).»**, **«Se han determinado indicadores de control del
    mantenimiento.»**, **«Se han aplicado técnicas de gestión de materiales y elementos para el mantenimiento de
    instalaciones.»**; contenidos: **«Mantenimiento predictivo, preventivo y correctivo. Técnicas de planificación
    de mantenimiento.»** (texto BOE sin consolidar, `fuentes/canal-sur/tecnica/BOE-A-2023-13217.txt`, l. 1381-1422).
- **Indicadores**: la única fórmula que he visto en fuente pública es la del pliego de Transports de Barcelona
  («Cumplimiento del Plan de Mantenimiento Preventivo-normativo» = operaciones realizadas / programadas en el mes).
  Es un pliego de un tercero, no una norma: **no usar como dato**. La norma de indicadores es UNE-EN 15341:2020+A1:2023
  (ficha de catálogo arriba); su contenido no se ha leído.

### 1.4 Lo propio de la RTVA que consta publicado

**X Convenio colectivo RTVA** (BOJA núm. 240, 10-12-2014), ficha del puesto **«CÓDIGO PUESTO 9311100
DENOMINACION DEL PUESTO: OFICIAL TÉCNICO ELECTRICISTA»** (txt l. 6672-6685):
- **«OBJETO O FUNCIÓN BÁSICA DEL PUESTO Realizar el mantenimiento y, reparación de las instalaciones que le sean
  encomendadas (frigorista o electricista)»**
- **«TAREAS MÁS SIGNIFICATIVAS DEL PUESTO»**: **«Efectuar revisiones y mantenimiento generales de instalaciones y
  equipos. Realizar reparaciones en instalaciones y equipos. Realizar el montaje e instalación de los nuevos sistemas
  y verificar su puesta en marcha. Mantener en condiciones optimas de funcionamiento las instalaciones. Mantener,
  operar, explotar e inspeccionar las instalaciones de RTVA y SSFF.»**
- Cláusula final: **«La presente definición no constituye una lista cerrada de funciones […]»**.
- Puesto de apoyo, **«AYUDANTE TÉCNICO ELECTRICISTA»** (código 9311200): **«Auxiliar al oficial en el ejercicio de
  sus funciones (electricidad).»** y, entre sus tareas, **«Mantener actualizada la información relativa a las
  instalaciones.»** y **«Realizar con el oficial guardias para atender averías imprevistas.»** (l. 4779-4793).
- En la tabla de puestos, la unidad aparece como **«UNIDAD DE MANTENIMIENTO»** y existen los puestos **«JF.SECC.
  MANTENIMIENTO»** y **«JEFE/A DPTO.EXPLOTAC. Y MANTENIMIENTO»**; este último tiene entre sus tareas **«Elaborar e
  implantar el Plan de Mantenimiento.»** (l. 5455) y el jefe de sección **«Coordinar, organizar y supervisar el
  mantenimiento de las instalaciones de los Centros de Trabajo.»** y **«Desarrollo e implantación del Plan de
  Mantenimiento y Explotación.»** (l. 5975-5977).

**No consta publicado**: el plan de mantenimiento de la RTVA, su GMAO, sus gamas, su inventario de instalaciones ni
su contratación de mantenimiento externo. Va a «Lo que este tema no da».

---

## 2. Tema 17 · Planificación de intervenciones en instalaciones críticas: análisis de impacto, ventanas de mantenimiento, coordinación con producción, comunicación de incidencias, planes de contingencia y retorno al servicio

RTVE (teitse/09 §6 final; tese/16 §2 y §4) da ensayos con carga en ventana pactada, redundancia, y la regla de
la versión anterior guardada. Falta: qué es una instalación crítica, análisis de impacto, coordinación,
comunicación de incidencias, contingencia y retorno al servicio.

### 2.1 «Crítica»: el único sentido legal del término

**Ley 8/2011, art. 2** (redacción única, vig. 30-04-2011):
- **«a) Servicio esencial: el servicio necesario para el mantenimiento de las funciones sociales básicas, la salud,
  la seguridad, el bienestar social y económico de los ciudadanos, o el eficaz funcionamiento de las Instituciones
  del Estado y las Administraciones Públicas.»**
- **«d) Infraestructuras estratégicas: las instalaciones, redes, sistemas y equipos físicos y de tecnología de la
  información sobre las que descansa el funcionamiento de los servicios esenciales.»**
- **«e) Infraestructuras críticas: las infraestructuras estratégicas cuyo funcionamiento es indispensable y no
  permite soluciones alternativas, por lo que su perturbación o destrucción tendría un grave impacto sobre los
  servicios esenciales.»**
- **«h) Criterios horizontales de criticidad»**: **«1. El número de personas afectadas […] 2. El impacto económico
  […] 3. El impacto medioambiental […] 4. El impacto público y social […]»**.
- **«j) Interdependencias: los efectos que una perturbación en el funcionamiento de la instalación o servicio
  produciría en otras instalaciones o servicios […]»**.

**No confirmado / no publicable**: si alguna instalación de la RTVA está catalogada como infraestructura crítica
(el Catálogo es información clasificada). El redactor debe usar «instalación crítica» en sentido técnico (aquella
cuyo fallo interrumpe la emisión o la seguridad) y citar la Ley 8/2011 sólo como vocabulario de impacto e
interdependencia, **sin afirmar que se aplique a la RTVA**. No he encontrado norma de transposición de la Directiva
(UE) 2022/2557 (entidades críticas) en el BOE (búsqueda por título «entidades críticas», 2023-2026: sin resultados):
**no confirmado** su estado.

### 2.2 Análisis de impacto y contingencia: normas de referencia (sólo catálogo)

- **UNE-EN ISO 22301:2020** **«Seguridad y resiliencia. Sistema de Gestión de la Continuidad del Negocio.
  Requisitos. (ISO 22301:2019).»** **«Fecha edición: 2020-05-14 En Vigor»**, **«Anula a UNE-EN ISO 22301:2015»**,
  **«Se modificará por UNE-EN ISO 22301:2020/A1:2024»**; la modificación A1 (2024-09-25, en vigor) es **«Modificación
  1: Acciones relativas al cambio climático.»**
- **UNE-EN ISO 22313:2020** **«Seguridad y resiliencia. Sistemas de gestión de la continuidad del negocio.
  Directrices para la utilización de la norma ISO 22301.»**
- El contenido (definición de «análisis de impacto en el negocio», objetivos de tiempo de recuperación, etc.) **no
  se ha leído**: no se escribe como dato. Si el redactor habla de «análisis de impacto», lo hace como método de
  oficio (qué servicios caen, durante cuánto, qué redundancia los cubre), apoyado en el vocabulario de la Ley
  8/2011 (impacto, interdependencias) y sin siglas como BIA/RTO atribuidas a norma.
- CPD: la serie UNE-EN 50600 está en el informe del bloque B (§8.3).

### 2.3 Plan de contingencia y comunicación de incidencias: lo que da la autoprotección

**RD 393/2007, anexo II** (vigente; sin cambios desde 2022): el capítulo 6, **«Plan de actuación ante
emergencias»**: **«Deben definirse las acciones a desarrollar para el control inicial de las emergencias,
garantizándose la alarma, la evacuación y el socorro.»**; 6.1 clasificación **«En función del tipo de riesgo. En
función de la gravedad. En función de la ocupación y medios humanos.»**; 6.2 procedimientos: **«a) Detección y
Alerta. b) Mecanismos de Alarma. b.1) Identificación de la persona que dará los avisos. […] c) Mecanismos de
respuesta frente a la emergencia. d) Evacuación y/o Confinamiento. e) Prestación de las Primeras Ayudas. f) Modos de
recepción de las Ayudas externas.»**; 6.3 **«Identificación y funciones de las personas y equipos que llevarán a cabo
los procedimientos de actuación en emergencias.»**; 6.4 **«Identificación del Responsable de la puesta en marcha del
Plan de Actuación ante Emergencias.»**; capítulo 7, **«7.1 Los protocolos de notificación de la emergencia»**;
capítulo 9, **«Mantenimiento de la eficacia y actualización del Plan de Autoprotección.»** El tema 32-14 de
Productor (común/puesto anterior, verificado) ya trae el plan de autoprotección: el redactor debe tomar de allí lo
general y de aquí sólo estos capítulos como esqueleto de «comunicación de incidencias» y «contingencia».
**No confirmado** si la RTVA está obligada a plan de autoprotección por el anexo I del RD 393/2007 ni si existe el
Decreto andaluz de autoprotección aplicable (no leído).

Escalado de incidencias al responsable preventivo y comunicación de incidencias: tema 32-14 (Productor), epígrafe
«Comunicación de incidencias y escalado al responsable preventivo» (l. 2180 y ss.), ya verificado.

### 2.4 Ventanas de mantenimiento y coordinación con producción

- **No hay norma** que regule «ventana de mantenimiento» en radiotelevisión. Lo de RTVE (preventivo de madrugada y
  en huecos de programación; ensayo con carga en ventana pactada) es costumbre de oficio y debe presentarse así.
- Coordinación con empresas externas que intervienen en la ventana: **CAE, RD 171/2004** y art. 24 LPRL, ya en el
  tema 32-14 (Productor), epígrafe «Coordinación de actividades empresariales con personal externo», y en el
  informe del bloque A, §8.6. Recurso preventivo cuando hay **«concurrencia de operaciones diversas que se
  desarrollan sucesiva o simultáneamente»**: RD 39/1997, art. 22 bis.1.a) (literal en §4.2 de este informe).
- Antes de intervenir: RD 1215/1997 anexo II.1.14 (parada, comprobación de energías residuales, bloqueo; §1.2) y,
  en lo eléctrico, RD 614/2001 (cinco reglas), informe A §8.

### 2.5 Retorno al servicio

- Eléctrico: **reposición de la tensión**, RD 614/2001 anexo II.B: informe del bloque A, §8.3 (no se repite).
- Equipos de trabajo: comprobación **«después de cada montaje»** y **«adicionales […] transformaciones,
  accidentes […] o falta prolongada de uso»**: RD 1215/1997 art. 4 (§1.2).
- Sistemas de control/telegestión: **RITE IT 2.3.4, apartado 4** (bloque IT 2, redacción única de 2007): **«Cuando la instalación disponga de un
  sistema de control, mando y gestión o telegestión basado en la tecnología de la información, su mantenimiento y la
  actualización de las versiones de los programas deberá ser realizado por personal cualificado o por el mismo
  suministrador de los programas.»** (apoya la regla de RTVE de la versión anterior guardada como práctica, no la
  sustituye).
- **No confirmado**: un procedimiento normalizado de «retorno al servicio» (verificación funcional, prueba con carga,
  cierre de la orden, comunicación a explotación). UNE-EN 50110-1 (explotación de instalaciones eléctricas) es la
  norma que trata la explotación y los trabajos; ficha AENOR: **«UNE-EN 50110-1:2024 ( Versión corregida en fecha
  2026-06-10 ) Explotación de instalaciones eléctricas. Parte 1: Requisitos generales.»**, **«Fecha edición:
  2024-06-19 En Vigor Fecha de corrección: 2026-06-10»**, **«Anula a UNE-EN 50110-1:2014»**, **«Idéntica EN
  50110-1:2023»**, **«Se modificará por PNE-EN 50110-1:2023/prA1:2026»**. Contenido no leído.

---

## 3. Tema 18 · Innovación aplicada al mantenimiento: IoT, predictivo, gemelo digital, telegestión energética, baterías, autoconsumo y automatización de edificios

### 3.1 Autoconsumo: lo que ha cambiado desde RTVE (ing-tec-industrial/11)

Comparación de la cadena de redacciones del RD 244/2019 (volcado de corte 21-12-2022 frente a hoy): **sólo cambian
los artículos 3 y 4**; los demás bloques citados por RTVE (arts. 2, 5, 6, 14) tienen redacción única de 2019.
RD 1699/2011: **sin cambios** desde 2022.

**Artículo 3.g).iii, segundo párrafo** (redacción vigente desde **22-03-2026**, por **Real Decreto-ley 7/2026, de 20
de marzo, por el que se aprueba el Plan Integral de Respuesta a la Crisis en Oriente Medio**, `BOE-A-2026-6544`;
convalidado por Resolución de 26-03-2026 del Congreso, `BOE-A-2026-7125`):
**«También tendrá la consideración de instalación de producción próxima a las de consumo y asociada a través de la
red, aquella instalación de generación que empleando tecnología fotovoltaica o eólica con una potencia de hasta 5 MW,
esta se conecte al consumidor o consumidores a través de las líneas de transporte o distribución y siempre que estas
se encuentren a una distancia inferior a 5.000 metros de los consumidores asociados. A tal efecto se tomará la
distancia entre los equipos de medida en su proyección ortogonal en planta.»**
(A 21-12-2022 decía: fotovoltaica **«ubicada en su totalidad en la cubierta de una o varias edificaciones»** y
**«a una distancia inferior a 1.000 metros»**.) El primer párrafo del iii sigue en **«una distancia inferior a 500
metros»**. Cadena del art. 3: 2019, RDL 29/2021 (`BOE-A-2021-21096`), RDL 18/2022 (`BOE-A-2022-17040`), RDL 20/2022
(`BOE-A-2022-22685`), RDL 7/2025 (`BOE-A-2025-12857`, derogado: nota del BOE **«Se deja sin efecto la modificación
del punto iii) de la letra g) por Resolución de 22 de julio de 2025, que publica el Acuerdo del Congreso de los
Diputados por el que se deroga el Real Decreto-ley 7/2025»**), BOE-A-2025-15313, RDL 7/2026.
RTVE no cita las distancias (comprobado con grep de «metros»): sólo es aviso si el redactor amplía.

**Artículo 4.5** (misma redacción vigente): cambia la letra que RTVE resume como regla 1 de «las tres reglas del
artículo 4.5»: hoy **«b) En ningún caso un sujeto consumidor podrá estar asociado de forma simultánea a más de una
de las modalidades de autoconsumo reguladas en el presente artículo con la única excepción de un autoconsumo
individual sin excedentes combinado con un autoconsumo mediante instalaciones próximas y asociadas a través de la
red.»** **Corrección obligada en lo copiado de RTVE** (ing-tec-industrial/11, §4, regla 1): añadir la excepción.
Además, los incisos del 4.5 pasan de «i., ii., iii.» a **«a), b), c)»**. Lo demás del art. 4 que RTVE cita (4.1,
4.2.a con sus cinco condiciones y el límite de **«100 kW»**, 4.3, 4.7 comunidad de energías renovables) coincide
con la redacción vigente (leído entero). **Error de RTVE (art. 8 mal)**: su regla 3 de «las tres reglas del
artículo 4.5» (comunidad de energías renovables) está en el **apartado 7** del art. 4, tanto en 2022 como hoy
(comprobado con `boe.py --fecha 20221221`): **«7. Para la realización del autoconsumo colectivo podrá constituirse una
comunidad de energías renovables siempre que se cumpla con los requisitos establecidos para las mismas.»**

### 3.2 Baterías: Reglamento (UE) 2023/1542 (no estaba en RTVE)

Texto original BOE-DOUE (`DOUE-L-2023-81096`), **no consolidado**. Modificaciones conocidas: Reglamento (UE)
2025/1561 (`DOUE-L-2025-81177`), cuyo título dice que modifica el 2023/1542 **«en lo que respecta a las obligaciones
de los operadores económicos en relación con las políticas de diligencia debida en materia de pilas o baterías»**
(no toca lo que sigue, según su título; texto no leído); y la corrección `DOUE-L-2024-81259`, que rehace los
artículos 77 y 78 (pasaporte de baterías): **no citar el número del artículo del pasaporte**.

Definiciones (art. 3, literal):
- **«"batería industrial": una batería que está específicamente diseñada para usos industriales, destinada a usos
  industriales tras ser objeto de preparación para la adaptación o de adaptación, o cualquier otra batería de peso
  superior a 5 kg que no sea una batería para vehículos eléctricos, una batería para medios de transporte ligeros, ni
  una batería para arranque, encendido o alumbrado»** (las baterías de un SAI o de un almacenamiento de autoconsumo
  caen aquí: deducción mía, no literal).
- **«"sistema estacionario de almacenamiento de energía con baterías": una batería industrial con almacenamiento
  interno que está específicamente diseñada para almacenar energía eléctrica desde la red y suministrársela o para
  almacenar energía eléctrica para los usuarios finales y suministrársela, con independencia del lugar en el que se
  use y la persona que la use»**
- **«"sistema de gestión de baterías": un dispositivo electrónico que controla o gestiona las funciones eléctricas y
  térmicas de una batería para asegurar su seguridad, rendimiento y vida útil, que gestiona y almacena los datos
  correspondientes a los parámetros para determinar el estado de salud y la vida útil prevista establecidos en el
  anexo VII […]»**
- **«"estado de salud": una medición del estado general de una pila o batería recargable y de su capacidad para
  ofrecer el rendimiento especificado en comparación con su estado inicial»**

Art. 12 (seguridad de los estacionarios): **«1. Los sistemas estacionarios de almacenamiento de energía con baterías
introducidos en el mercado o puestos en servicio serán seguros durante su funcionamiento y uso normales.»**; 12.2.d)
la documentación técnica **«incluirá instrucciones de mitigación en caso de que puedan producirse los peligros
identificados, por ejemplo, un incendio o una explosión.»**

Art. 14.1 (el puente con el predictivo): **«A partir del 18 de agosto de 2024, los datos actualizados de los
parámetros para determinar el estado de salud y la vida útil prevista de las baterías, según se establece en el anexo
VII estarán recogidos en el sistema de gestión de baterías de los sistemas estacionarios de almacenamiento de
energía con baterías, las baterías para medios de transporte ligeros y las baterías para vehículos eléctricos.»**
14.2: quien haya adquirido legalmente la batería tiene **«acceso de solo lectura, no discriminatorio»** a esos datos.

Anexo VII, parte A (estado de salud de los estacionarios), literal: **«1) capacidad restante; 2) en la medida de lo
posible, capacidad de potencia restante; 3) en la medida de lo posible, eficiencia de ida y vuelta restante; 4)
evolución de los índices de autodescarga; 5) en la medida de lo posible, resistencia óhmica.»** Parte B (vida útil
prevista): **«1) fecha de fabricación y, si procede, fecha de puesta en servicio de la pila o batería; 2) rendimiento
energético; 3) rendimiento en términos de capacidad; 4) seguimiento de los acontecimientos adversos, como el número de
descargas profundas, el tiempo transcurrido en temperaturas extremas o el tiempo transcurrido en carga en temperaturas
extremas; 5) número de ciclos completos de carga y descarga equivalentes.»**

Art. 13 (fechas de etiquetado): 13.1 **«A partir del 18 de agosto de 2026 o 18 meses después de la fecha de entrada
en vigor del acto de ejecución a que se refiere el apartado 10, si esta fecha es posterior»**, etiqueta con la
información del anexo VI parte A; 13.4 **«A partir del 18 de agosto de 2025, todas las pilas o baterías llevarán
marcado el símbolo de recogida separada»**; 13.6 **«A partir del 18 de febrero de 2027, todas las pilas o baterías
llevarán marcado un código QR»** que, para **«baterías industriales con una capacidad superior a 2 kWh»**, da acceso
al pasaporte. **No confirmado**: si el acto de ejecución del 13.10 se adoptó y, por tanto, qué fecha rige para el
13.1 (no se ha podido leer EUR-Lex). Recomendación: citar el 13.4 y el 13.6, y el 13.1 con su «o … si esta fecha es
posterior» completo.

**No confirmado**: norma española de adaptación al Reglamento 2023/1542 (búsqueda BOE «pilas y baterías» 2024-2026:
sólo una orden de ayudas). No afirmar si el RD 106/2008 sigue o no vigente sin leerlo.

### 3.3 Automatización de edificios y telegestión: RITE vigente

**RITE IT 1.2.4.3.5** (vig. 01-07-2021, RD 178/2021), «Sistemas de automatización y control de instalaciones»:
**«1. Cuando sea técnica y económicamente viable, los edificios no residenciales con una potencia nominal útil para
instalaciones de calefacción, refrigeración, instalaciones combinadas de calefacción y ventilación, o para
instalaciones combinadas de refrigeración y ventilación de más de 290 kW deberán estar equipados con sistemas de
automatización y control de edificios.»** Deberán ser capaces de: **«a) Monitorizar, registrar, analizar y permitir
la adaptación del consumo de energía de forma continua; b) Efectuar una evaluación comparativa de la eficiencia
energética del edificio, detectar las pérdidas de eficiencia de sus instalaciones técnicas e informar sobre las
posibilidades de mejora de la eficiencia energética a la persona responsable de la instalación o de la gestión
técnica del edificio; c) Permitir la comunicación con instalaciones técnicas conectadas y otros aparatos que estén
dentro del edificio, así como garantizar la interoperabilidad […]»** y **«Será considerado, a efectos de esta
exigencia, la automatización y el control que tienen un impacto en la eficiencia energética del edificio, como los
recogidos en la norma UNE-EN 15232-1.»** Apdo. 3: tras instalarlo, **«será necesario realizar acciones de
comprobación de que el sistema funciona con arreglo a sus especificaciones y acciones de ajuste»**, y **«Las
indicaciones e instrucciones para la correcta operación del sistema de automatización y control deberán recogerse en
el ''Manual de Uso y Mantenimiento''.»**

**Aviso (error 7 posible)**: la norma que cita el RITE, **UNE-EN 15232-1, está anulada**. Ficha AENOR de su
sustituta: **«UNE-EN ISO 52120-1:2022 Eficiencia energética de los edificios. Contribución de la automatización, el
control y la gestión de los edificios. Parte 1: Marco general y procedimientos. (ISO 52120-1:2021, Versión corregida
2022-09).»**, **«Fecha edición: 2022-10-19 En Vigor»**, **«Anula a UNE-EN 15232-1:2018»**. El tema debe citar al
RITE tal cual (UNE-EN 15232-1) y añadir que UNE la ha sustituido por la UNE-EN ISO 52120-1:2022.

**RITE IT 4.3.4, párrafo segundo** (exención): **«Los edificios no residenciales que cuenten con un sistema de
automatización y control que cumpla los requisitos establecidos en el apartado 1 de la IT 1.2.4.3.5, así como los
edificios residenciales que cuenten con un sistema de automatización y control que cumpla los requisitos
establecidos en el apartado 2 de la IT 1.2.4.3.5, quedarán exentos del cumplimiento de los requisitos establecidos en
la IT 4.2.1, IT 4.2.2 y IT 4.2.3.»** (es decir, de las inspecciones periódicas de eficiencia energética).

**RITE IT 2.3.4** (control automático, pruebas): **«2. […] se establecerán los criterios de seguimiento basados en la
propia estructura del sistema, en base a los niveles del proceso siguientes: nivel de unidades de campo, nivel de
proceso, nivel de comunicaciones, nivel de gestión y telegestión.»**; **«3. […] Son válidos a estos efectos los
protocolos establecidos en la norma UNE-EN-ISO 16484-3.»**; apdo. 4 literal en §2.5.

**Directiva (UE) 2024/1275** (eficiencia energética de los edificios, refundición): **no leída**; su transposición
no consta en el RITE vigente (los bloques IT 1 e IT 4 tienen su última redacción de 2021). **No confirmado** el nuevo
umbral de potencia para automatización que fija la directiva: no escribir cifra.

### 3.4 Telegestión energética y auditorías: RD 56/2016

**RD 56/2016** (sin cambios desde su publicación): art. 2.1 ámbito, grandes empresas **«tanto las que ocupen al
menos a 250 personas como las que, aun sin cumplir dicho requisito, tengan un volumen de negocio que exceda de 50
millones de euros y, a la par, un balance general que exceda de 43 millones de euros»**; art. 3.1 **«deberán
someterse a una auditoría energética cada cuatro años […] que cubra, al menos, el 85 por ciento del consumo total de
energía final»**; 3.2.b) alternativa: **«Aplicar un sistema de gestión energética o ambiental, certificado por un
organismo independiente»**; 3.3.a) **«Deberán basarse en datos operativos actualizados, medidos y verificables, de
consumo de energía y, en el caso de la electricidad, de perfiles de carga siempre que se disponga de ellos.»**;
3.5 **«Los datos empleados en las auditorías energéticas deberán poderse almacenar para fines de análisis histórico y
trazabilidad del comportamiento energético.»** (es el fundamento normativo de la monitorización de consumos).
**No confirmado** si la RTVA está obligada (depende de plantilla/cifras; no he leído sus cuentas) ni si se ha
transpuesto la Directiva (UE) 2023/1791. Probable solapamiento con el tema 16 (bloque C): coordinar.

### 3.5 IoT, gemelo digital y predictivo: normas de referencia

- **Gemelo digital. ISO/IEC 30173:2023** «Digital twin — Concepts and terminology» (vista previa oficial, 1.ª ed.,
  2023-11; preparada por **«subcommittee 41: Internet of Things and Digital Twin»**). Definición 3.1.1, literal (en
  inglés; no hay versión UNE en español localizada): **«digital twin DTw digital representation (3.1.8) of a target
  entity (3.1.3) with data connections that enable convergence between the physical and digital states at an
  appropriate rate of synchronization»**; **«Note 1 to entry: Digital twin has some or all of the capabilities of
  connection, integration, analysis, simulation, visualization, optimization, collaboration, etc.»**; **«Note 2 to
  entry: Digital twin can provide an integrated view throughout the life cycle of the target entity.»** El redactor
  debe dar la traducción como suya («representación digital de una entidad objetivo con conexiones de datos que
  permiten la convergencia entre los estados físico y digital a una tasa de sincronización adecuada»), sin negrita.
- **IoT. ISO/IEC 30141:2024** (ficha AENOR: **«ISO/IEC 30141:2024 Internet of Things (IoT) — Reference
  architecture»**, **«Fecha edición: 2024-08-27 En Vigor»**, **«This second edition cancels and replaces the first
  edition published in 2018.»**). Alcance (vista previa): **«This document specifies an Internet of Things (IoT)
  reference architecture (IoT RA).»** Sus términos remiten a **«ISO/IEC 20924, Internet of Things (IoT) and digital
  twin – Vocabulary»** (3.ª ed., 2024-02, según su vista previa); **la definición de IoT de esa norma no se ha podido
  leer** (la vista previa corta antes de las definiciones): no escribirla.
- **Predictivo / monitorización de condición. ISO 17359:2018** (ficha AENOR: **«ISO 17359:2018 Condition monitoring
  and diagnostics of machines — General guidelines»**, **«Fecha edición: 2018-01-24 En Vigor»**; resumen: **«gives
  guidelines for the general procedures to be considered when setting up a condition monitoring programme for
  machines […] This document is applicable to all machines.»**). Contenido no leído.
- Lo que sí es norma vigente y sostiene el predictivo eléctrico: datos del BMS de baterías (Reg. 2023/1542, art. 14 y
  anexo VII, §3.2), y en climatización la función b) del RITE IT 1.2.4.3.5 («detectar las pérdidas de eficiencia»,
  §3.3). La termografía y el análisis de red son del tema 14 (informe A, §7).
- **No confirmado**: cualquier uso de IoT, gemelo digital o predictivo **en la RTVA** (no consta en documento
  publicado). Va a «Lo que este tema no da».

### 3.6 Apoyo curricular (para justificar que es materia del oficio)

RD 401/2023 (títulos de FP), perfil: **«otras tecnologías innovadoras (IIoT, robótica colaborativa y móvil, visión
artificial, entre otras )»** y **«tecnologías relacionada con la fábrica inteligente (M2M, IIoT, etc.)»** (txt l. 97 y
99); contenido **«Configuración de redes IoT industriales.»** (l. 1259). No usar más allá de esto.

---

## 4. Tema 19 · Prevención de riesgos laborales aplicada al puesto

Ya cerrado: común 09 (Ley 31/1995), 32-14 y 32-15 (Productor). RTVE: prl-especifico (altura §6, confinados §8,
cargas §4, PVD §2, TME §3, in itinere §10), teitse/14 (riesgo eléctrico), enfermería/02 (señalización), medicina/13
(químicos). **Comprobado que no han cambiado desde 21-12-2022** (redacciones con vigencia posterior: ninguna):
RD 1215/1997, RD 485/1997, RD 487/1997, RD 488/1997, RD 773/1997, RD 374/2001, RD 614/2001. RD 39/1997: sólo cambia
su DA 13.ª (anulada por STS de 29-09-2025, servicio del hogar; irrelevante). Por tanto **lo de RTVE sobre esas
normas se puede copiar sin re-verificar la vigencia**, sólo la literalidad.

### 4.1 Lo que falta y es propio del electricista

**(a) El puesto en la RTVA**: ficha del convenio, §1.4 (literal). Dato a destacar para «riesgos específicos del
puesto en RTVA/CSRTV»: la función básica incluye **«(frigorista o electricista)»** y el ayudante hace **«guardias
para atender averías imprevistas»** con el oficial: trabajo fuera de horario y en solitario/pareja. **No consta**
publicada la evaluación de riesgos del puesto en la RTVA. El convenio, art. 28 ap. 1, sólo dice que **«se realizarán
Evaluaciones de Riesgos Laborales de cada uno de los puestos de trabajo de la empresa conforme al contenido general,
procedimiento, periodicidad y demás requisitos que se establecen en los artículos 3 al 7 del Reglamento de los
Servicios de Prevención, R.D. 39/1997, de 17 de enero.»** (ver tema 32-15, «La organización preventiva de la RTVA»,
ya verificado).

**(b) Riesgo eléctrico**: RD 614/2001 y Guía INSST 2020 en el informe A §8 (definiciones, distancias del anexo I,
cinco reglas, reposición, trabajos en tensión, permisos). teitse/14 de RTVE cubre lo general. No se repite.

**(c) Recurso preventivo obligatorio: RD 39/1997, art. 22 bis** (redacción única, vig. 29-06-2006, RD 604/2006).
Pieza que no está en ninguna fuente reutilizada y que une altura, confinados y electricidad:
- 22 bis.1: **«De conformidad con el artículo 32 bis de la Ley 31/1995 […] la presencia en el centro de trabajo de los
  recursos preventivos, cualquiera que sea la modalidad de organización de dichos recursos, será necesaria en los
  siguientes casos:»**
  - **«a) Cuando los riesgos puedan verse agravados o modificados, en el desarrollo del proceso o la actividad, por
    la concurrencia de operaciones diversas que se desarrollan sucesiva o simultáneamente y que hagan preciso el
    control de la correcta aplicación de los métodos de trabajo.»**
  - **«b) Cuando se realicen las siguientes actividades o procesos peligrosos o con riesgos especiales: 1.º Trabajos
    con riesgos especialmente graves de caída desde altura, por las particulares características de la actividad
    desarrollada, los procedimientos aplicados, o el entorno del puesto de trabajo.»** […] **«4.º Trabajos en
    espacios confinados. A estos efectos, se entiende por espacio confinado el recinto con aberturas limitadas de
    entrada y salida y ventilación natural desfavorable, en el que pueden acumularse contaminantes tóxicos o
    inflamables o puede haber una atmósfera deficiente en oxígeno, y que no está concebido para su ocupación
    continuada por los trabajadores.»**
  - **«c) Cuando la necesidad de dicha presencia sea requerida por la Inspección de Trabajo y Seguridad Social […]»**
- 22 bis.8: lo anterior **«se entiende sin perjuicio de las medidas previstas en disposiciones preventivas
  específicas […] como es el caso, entre otros, de las siguientes actividades o trabajos:»** … **«f) Trabajos con
  riesgos eléctricos.»** (es decir: el riesgo eléctrico se rige por su norma propia, el RD 614/2001, no por esta
  lista).
- 22 bis.4: **«La presencia es una medida preventiva complementaria que tiene como finalidad vigilar el cumplimiento
  de las actividades preventivas […]»**.
- 22 bis.9 (contratas): con empresas concurrentes, **«la obligación de designar recursos preventivos para su
  presencia en el centro de trabajo recaerá sobre la empresa o empresas que realicen dichas operaciones o
  actividades»**.
- **Corrección a RTVE** (prl-especifico §8): dice que espacios confinados **«no tiene un real decreto propio: se rige
  por la Ley 31/1995 y por la documentación técnica del INSST»**. Es cierto que no hay RD propio, pero **sí hay
  definición reglamentaria** (la del art. 22 bis.1.b.4.º, arriba) y la obligación de recurso preventivo. Su
  definición en §8.1 («recinto con aberturas limitadas de entrada y salida, ventilación natural desfavorable y no
  concebido para ocupación continuada») es una paráfrasis de esa letra sin la cita: el redactor debe sustituirla por
  la literal del RD 39/1997. La tabla de medidas de §8.2 no tiene fuente citada en RTVE (no la he contrastado con
  NTP alguna): **sólo como costumbre de oficio** o quitarla.
- Art. 32 bis de la Ley 31/1995: está en el común 09 (comprobar allí que se copia; no lo he abierto).

**(d) Trabajos en altura**: RTVE prl-especifico §6 cita literal RD 1215/1997 anexo I.6 y anexo II.4 (vigentes, sin
cambios). Para el electricista, lo nuevo es el recurso preventivo del 22 bis.1.b.1.º (arriba).

**(e) Productos químicos y etiquetado (lo que falta en medicina/13)**: Reglamento (CE) 1272/2008 (CLP), texto
original BOE-DOUE, **no consolidado**:
- Art. 17.1, elementos de la etiqueta: **«a) el nombre, la dirección y el número de teléfono del proveedor o
  proveedores; b) la cantidad nominal […]; c) los identificadores del producto […]; d) cuando proceda, los
  pictogramas de peligro de conformidad con el artículo 19; e) cuando proceda, las palabras de advertencia de
  conformidad con el artículo 20; f) cuando proceda, las indicaciones de peligro de conformidad con el artículo 21;
  g) cuando proceda, los consejos de prudencia apropiados de conformidad con el artículo 22; h) cuando proceda, una
  sección de información suplementaria de conformidad con el artículo 25.»**
- Art. 2.4: **«"palabra de advertencia": un vocablo que indica el nivel relativo de gravedad de los peligros […]; se
  distinguen los dos niveles siguientes: a) "peligro": palabra de advertencia utilizada para indicar las categorías
  de peligro más graves; b) "atención": palabra de advertencia utilizada para indicar las categorías de peligro menos
  graves»**; art. 20.3: **«Cuando en la etiqueta figure la palabra de advertencia "peligro", no aparecerá la palabra
  de advertencia "atención".»**
- Art. 2.3 **«"pictograma de peligro": una composición gráfica que contiene un símbolo más otros elementos
  gráficos, como un contorno, un motivo o un color de fondo […]»**; 2.5 **«"indicación de peligro"»** y 2.6
  **«"consejo de prudencia"»** (literal en el volcado).
- Anexo V (texto original 2008): nueve pictogramas, **GHS01** «bomba explotando», **GHS02** «llama», **GHS03**
  «llama sobre un círculo», **GHS04** «bombona de gas», **GHS05** «corrosión», **GHS06** «calavera y tibias
  cruzadas», **GHS07** «signo de exclamación», **GHS08** «peligro para la salud», **GHS09** «medio ambiente» (nombres
  de símbolo literales del anexo; las adaptaciones al progreso técnico posteriores **no se han contrastado**).
- Reforma: **Reglamento (UE) 2024/2865** (`DOUE-L-2024-81721`) **no modifica los arts. 17, 19, 20 ni 21** (lista de
  sus 37 puntos revisada: sí toca el 18.3.b, el 25, el 29, el 30, el 31 —formato de etiqueta—, etc.); sus fechas las
  ha aplazado el **Reglamento (UE) 2025/2439** (`DOUE-L-2025-81843`): nuevo art. 2.2 **«[…] serán aplicables a partir
  del 1 de julio de 2026»**, 2.3 **«[…] a partir del 1 de enero de 2027»**, nuevo 2.3 bis **«[…] a partir del 1 de
  enero de 2028»**. **No confirmado** el contenido concreto del nuevo art. 31 (formato): no escribir tamaños de letra.
- No he comprobado si otras modificaciones del CLP entre 2008 y 2024 tocaron los arts. 17-21: **no confirmado**; el
  redactor puede citarlos «en su texto original» o pedir la versión consolidada.

**(f) EPI, señalización, PVD, cargas, TME, in itinere y en misión**: cubiertos por 32-15 (Productor, vigente) y por
RTVE (normas sin cambios desde 2022). No hay nada que investigar.

**(g) CAE (RD 171/2004)**: el encargo lo nombra para este bloque; ya está en 32-14 (Productor, «Coordinación de
actividades empresariales con personal externo», verificado) y en el informe A §8.6. Sin investigación nueva.

---

## 5. Lo que no pude confirmar (resumen)

1. Definiciones de UNE-EN 13306:2018 (sólo estructura, desde una reproducción secundaria de la edición 2010).
2. Contenido de UNE-EN 13460, 17007, 15341, 17485, 50110-1:2024, ISO 22301/22313, ISO 17359, ISO/IEC 20924
   (sólo catálogo).
3. Definición normativa de «gama», «orden de trabajo», «GMAO», «ventana de mantenimiento», «retorno al servicio»:
   no existe en BOE/BOJA; son términos de oficio.
4. Si alguna instalación de la RTVA es infraestructura crítica (Ley 8/2011) y estado de transposición de la Directiva
   (UE) 2022/2557.
5. Si la RTVA está obligada por el anexo I del RD 393/2007 y por el decreto andaluz de autoprotección.
6. Fecha efectiva del art. 13.1 del Reglamento 2023/1542 (depende de un acto de ejecución no localizado) y norma
   española de adaptación.
7. Umbral de automatización de la Directiva (UE) 2024/1275 y su transposición.
8. Si la RTVA está obligada por el RD 56/2016; transposición de la Directiva (UE) 2023/1791.
9. Uso de IoT, gemelo digital, predictivo, GMAO o telegestión en la RTVA; plan de mantenimiento, inventario y
   evaluación de riesgos del puesto en la RTVA.
10. Consolidación del CLP (arts. 17-21 y anexo V) más allá de comprobar que el Reglamento 2024/2865 no los toca.

## 6. Avisos para el redactor (reutilización)

- **ing-tec-industrial/11 §4** (regla 1 del art. 4.5 RD 244/2019): añadir la excepción vigente desde 22-03-2026
  (§3.1); la regla 3 (comunidad de energías renovables) es el art. 4.7, no el 4.5. Cambiar la ficha a «redacción vigente el 05-10-2026».
- **teitse/09 §6**: el predictivo es subclase del preventivo en la terminología normalizada; quitar «El más barato»
  como dato.
- **tese/15 §1**: «una hora de preventivo cuesta menos…» como costumbre de oficio, no como dato.
- **prl-especifico §8**: sustituir la definición parafraseada de espacio confinado por la literal del RD 39/1997 art.
  22 bis.1.b.4.º; añadir el recurso preventivo; la tabla de medidas, sin fuente.
- **RITE IT 1.2.4.3.5** cita UNE-EN 15232-1, anulada por UNE-EN ISO 52120-1:2022: decirlo.
- Temas 13 y 17 se apoyan casi enteros en práctica de oficio; la extensión debe ser corta y la «Trazabilidad» debe
  declarar qué es norma y qué es costumbre.
