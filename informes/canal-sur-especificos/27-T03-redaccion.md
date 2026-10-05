# Puesto 27 · Oficial Técnico Electricista · Tema 3 · Fase 2, redacción

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas: el BOE consolidado del REBT da como última actualización el 18-12-2025, y todos
los bloques citados tienen redacción única de 2002 salvo la ITC-BT-02, vigente desde 04-04-2025, y
la ITC-BT-52, vigente desde 16-06-2022). Tema escrito:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/03-cuadros-electricos-aparamenta-y-protecciones.md`
(13.847 palabras según `indice.py`; 9 rúbricas `##` en el orden del enunciado, la primera es
el rótulo «Cuadros eléctricos, aparamenta y protecciones»; 28 epígrafes `###`).

Ficheros tocados: sólo el tema y este informe.

Material: `27-investigacion-A-electrico.md` § 1, § 4 y § 9; RTVE `teitse/03` y `teitse/04` (fila
27·3 de `informes/canal-sur-reuso/tecnica.tsv`: 85 %, **actualizar: sí**); AGRUPACION.tsv: 27·3
«nuevo» (el 14·3 es «parecido» y se escribirá a partir de éste).

Extensión: mayor que la del tema 1 (9.900). El enunciado tiene nueve rúbricas y casi todas llevan
cita literal del REBT (ITC-BT-17, 22, 23 y 24 casi enteras en lo pertinente). No he recortado
datos; si el coordinador quiere menos, lo recortable es prosa de oficio en 5.2, 6.3 y 8.2.

Lentes pasadas al cerrar:
- `negritas.py` contra `BOE-A-2002-18099.md` y `BOE-A-2001-11881.md`: 186 negritas; 4 «no están»:
  2 rótulos de la plantilla y 2 citas de la guía del INSST (epígrafe 7), que son literales pero el
  `.txt` de la guía lleva guiones blandos de partición («conecta­das», «encla­vamiento») y la lente
  no las encuentra. El verificador debe cotejarlas a mano en
  `fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.txt`, líneas 4586-4593 y 4606-4609.
  0 «otro artículo».
- `refutar_prosa.py`: 0 hallazgos (había 3: siglas MT e IP XXB sin presentar y una frase repetida
  sobre el proyecto de reforma; corregidos).

## Fuentes releídas en esta fase

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md` | 05-10-2026 | Art. 15.3 y 16 (redacción única); ITC-BT-01 (definiciones citadas; no define seccionador ni relé); ITC-BT-17 entera; ITC-BT-19 2.2.4, 2.4, 2.6, 2.7, 2.9; ITC-BT-22 entera con las notas de la tabla 1; ITC-BT-23 entera; ITC-BT-24 entera (citados 3.2, 3.5, 4.1, 4.1.1-4.1.3); ITC-BT-28 1, 2.1, 4; ITC-BT-34 3.1-3.2; ITC-BT-47 3.1, 4, 5; ITC-BT-52 6.1, 6.3, 6.4 (vig. 16-06-2022); ITC-BT-02 (vig. 04-04-2025): títulos de normas y nota (7) |
| RD 614/2001 (BOE-A-2001-11881), anexo IV | 05-10-2026 | A.1 y B.1 (redacción única) |
| INSST, Guía técnica riesgo eléctrico, 4.ª ed. 2020 (`fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.txt`) | 05-10-2026 | Definición de seccionadores e interruptores y medidas frente a maniobras erróneas (pág. 64 de la guía) |

## Correcciones y decisiones (manda la fuente)

1. **Clase S.** RTVE (teitse/03 § 3) daba una fila «Superinmunizado o selectivo S». Son cosas
   distintas: la ITC-BT-24 habla de diferencial **temporizada (por ejemplo del tipo «S»)**;
   «superinmunizado» es denominación comercial sin fuente leída. La fila queda como S (selectivo,
   temporizado) y «superinmunizado» va a «Lo que este tema no da».
2. **Clase B.** RTVE afirmaba que detecta «corrientes continuas lisas»; no hay fuente leída (la
   UNE-EN 62423 sólo consta por su título en la ITC-BT-02). Quitado; F y B se nombran por la norma.
3. **Sensibilidad de 300 mA «contra incendios»** (RTVE, tabla de sensibilidades): el REBT no la
   recoge (búsqueda de «300 mA» sin resultado). Se mantiene 300 mA como valor comercial de oficio,
   sin la finalidad de incendios, y se añaden los 500 mA recomendados de la ITC-BT-34, 3.2 y los
   30 mA de ITC-BT-34 3.1 e ITC-BT-52 6.1.
4. **Cifras de sobrecarga y cortocircuito** (RTVE: «de dos a diez veces la nominal», «de cientos o
   miles de veces», «en milisegundos»): sin fuente. Sustituidas por una descripción cualitativa.
5. **«una corriente de treinta miliamperios que mata no lo hace saltar»** (RTVE): afirmación médica
   sin fuente. Sustituida por «una corriente de defecto de pocos miliamperios a través de una
   persona no lo hace saltar».
6. **Ib ≤ In ≤ Iz e I2 ≤ 1,45 Iz** (investigación § 4.3): no están en el REBT; RTVE no las traía.
   El tema nombra la primera como regla de oficio, remite a la UNE 20.460-4-43 citando literalmente
   lo que la ITC-BT-22 dice de ella y no da el 1,45 (declarado en «Lo que este tema no da»).
7. **ITC-BT-01, «contactor con contactos cerrados en reposo»**: el BOE repite en ella el texto de
   la de contactos abiertos («corresponde a la apertura de sus contactos»). Se señala y no se usa.
8. **Erratas del BOE conservadas** con nota: «instalació n» (ITC-BT-17, 1.3) y «deforma» (art.
   16.2). También se conservan «esta prohibido», «esta al potencial» (ITC-BT-19, 2.7) y «kv»
   (ITC-BT-23, tabla 1) tal como están.
9. **RD 614/2001, anexo IV, B.1.1.ª**: el BOE lleva coma («en carga, o cierre»); la guía del INSST
   la omite. Se cita el BOE.
10. **ITC-BT-28 en edificios de la RTVA/CSRTV**: el campo de aplicación (apartado 1) no nombra
    estudios de radio o televisión; se aplica por uso u ocupación. El tema lo dice condicional y
    declara que no consta si un edificio concreto entra.
11. **Proyecto «REBT 2026»** (investigación § 1 y § 9.1): no publicado en el BOE; mencionado sólo
    como proyecto, sin cifras, en «Lo que este tema no da», con remisión desde 3.3 y 9.3.
12. **Añadido sobre RTVE y la investigación**, todo leído en el volcado: ITC-BT-01 (definiciones),
    art. 15.3 y 16.3, ITC-BT-17 1.1 y 1.3 enteros, ITC-BT-19 2.4, 2.6, 2.7 y 2.9, ITC-BT-22 1.1 b)
    literal y notas de la tabla 1.2, ITC-BT-24 4.1 a 4.1.3 (condiciones TT, TN, IT y prohibición en
    TN-C), ITC-BT-28 2.1 y 4, ITC-BT-34 3.1 y 3.2, ITC-BT-47 4 y 5, ITC-BT-52 6.1, 6.3 y 6.4,
    ITC-BT-02 (títulos de normas de producto), RD 614/2001 anexo IV y guía del INSST.

## Qué se quitó por propio de RTVE o por ser de otro tema

- Enunciado, ficha y referencias al anexo y la convocatoria 1/2022 de RTVE, a «este proyecto», a la
  lente de exactitud, a `PENDIENTES.md` y al «informe de refutación de esta ocupación» (teitse/03
  § 10 y teitse/04 § 6).
- teitse/03 § 4 (esquemas de conexión del neutro), § 5 (puesta a tierra) y § 6 (contactos, salvo
  la cita de envolventes): son del tema 5 de Canal Sur. Del § 4 sólo queda lo necesario para el
  diferencial (condiciones de la ITC-BT-24 en TT, TN e IT, en 3.4).
- teitse/03 § 9 (conmutación sin paso por cero): tema 7. Queda sólo la remisión desde 5.3.
- teitse/04 § 1 (cables), § 2 (canalizaciones) y § 4 (detectores): tema 4 y otros; el enunciado
  de Canal Sur no los pide. De § 3 se toman los datos de compra de cada aparato; de § 5, la lectura
  del código IP y la cita de la ITC-BT-24, 3.2.
- «una casa que emite», «esta ocupación», remisiones a los temas 2, 9, 11, 12 y 13 de RTVE:
  sustituidas por las de Canal Sur o quitadas.
- «El TT es el esquema de las instalaciones alimentadas desde la red pública en España» y
  «es el accidente clásico del cuadro de un centro de transformación»: sin fuente leída; quitadas.

## Copiado del común

Ninguno. El temario común de Canal Sur (`temas/canal-sur-comun/01` a `10`) no trata ninguna
materia de este tema, y no hay tema cerrado de Canal Sur del que copiar (AGRUPACION: 27·3 «nuevo»).

## Copiado de RTVE sin cambios

Ninguno. Los dos temas de origen (teitse/03 y teitse/04) están marcados **«actualizar: sí»** en la
fila 27·3 de `tecnica.tsv`, de modo que ningún pasaje entra en esta categoría: todo lo tomado de
RTVE se lista abajo como adaptado y debe verificarse.

**Tomado de RTVE, para verificar** (literal o casi, con fuera las negritas y mayúsculas enfáticas de
RTVE, que en Canal Sur sólo marcan texto de la fuente; los cambios de palabra se indican):

De `teitse/03-dispositivos-de-proteccion-y-maniobra.md`:
- Intro, tabla «Qué se protege / De qué / Con qué» y párrafo «Confundir las dos…» (cambiada la
  frase de los treinta miliamperios; añadida la remisión a la ITC-BT-17) → 1.1.
- § 1, tabla de las tres causas (fila «Sobrecarga»: «superior a la admisible» en lugar de «a la
  nominal»; fila cortocircuito: «o un fusible»; fila descarga: «dispositivos de protección contra
  sobretensiones») y la lectura «el cortocircuito se puede proteger aguas arriba…» → 2.1.
- § 2, tabla de los dos mecanismos (añadido «característica de tiempo inverso»; «en milisegundos»
  por «de forma instantánea»), tabla de los datos (añadida «Tensión asignada», de teitse/04 § 3),
  tabla de curvas, párrafo del orden B-D y párrafo del poder de corte → 2.2 y 2.3.
- § 3, «Cómo funciona, en una frase…», cita de la ITC-BT-24 3.5 (ampliada con el primer párrafo y
  el de clase A), «La palabra que hay que subrayar…», tabla de sensibilidades (reconstruida, ver
  decisión 3), tabla de clases (reconstruida, decisiones 1 y 2), lectura de la electrónica y aviso
  del botón de prueba → 3.1, 3.2, 3.3 y 3.5.
- § 6, cita de envolventes y apertura, lectura de la cara superior → 1.4.
- § 7, tabla de aparatos de maniobra, regla del seccionador (sin «accidente clásico… centro de
  transformación»), regla de maniobrar y proteger, tabla de partes del contactor → 5.1 y 7.
- § 8, tabla potencia/mando, tabla de los dos esquemas (marcha-paro precisado: NA, NC, en paralelo
  y en serie), tabla de enclavamientos y su razón (sin la remisión al tema 2 RTVE), tabla de reglas
  del cuadro (la fila de colores remite ahora a la ITC-BT-19 2.2.4 citada; la fila IP sustituida
  por la de temperatura interior, de teitse/04 § 5) → 1.4, 5.2 y 5.3.

De `teitse/04-materiales-electricos-cables-corte-y-envolventes.md`:
- § 3, datos de compra del contactor y del fusible, fila de categoría de empleo y de clase de
  fusible, regla de sustitución del fusible → 4 y 5.1.
- § 5, tabla de posiciones del código IP, «La letra X…», frase del IK y párrafo de la temperatura
  interior → 1.4.

Lo demás (1.2, 1.3, 1.5, 2.1 desde la letra a), 2.4, 3.4, 4 salvo lo dicho, 5.2 último párrafo,
6 entero, 7 desde la segunda cita, 8 entero, 9 entero y los tres bloques finales) es redacción
nueva.

## Preguntas tipo test de comprobación (10)

Respuesta correcta en negrita; a la derecha, dónde la contesta el tema. Repartidas por las nueve
rúbricas, con teoría y aplicación práctica. Las diez se contestan enteras con el tema; no ha hecho
falta ampliar.

1. (Cuadros, teoría) Según la ITC-BT-17, el interruptor general automático de un cuadro general
   tendrá un poder de corte de: a) 3.000 A como mínimo; **b) 4.500 A como mínimo y, en todo caso,
   suficiente para la intensidad de cortocircuito del punto de su instalación**; c) 6.000 A
   siempre; d) el que fije la empresa distribuidora, sin mínimo. Y su envolvente tendrá como
   mínimo: **IP 30 e IK07**. — Epígrafes 1.3 y 1.4.
2. (Automáticos, práctica) La distribuidora informa de una corriente de cortocircuito máxima
   previsible de 6 kA en el origen de la instalación. Un IGA de 4,5 kA: a) cumple, porque supera el
   mínimo de 4.500 A; b) cumple si es de curva D; **c) no cumple: su poder de corte debe ser
   suficiente para la Icc del punto**; d) cumple si lleva diferencial. — Epígrafes 2.1 (art. 15.3)
   y 2.3.
3. (Diferenciales, teoría) Según la ITC-BT-24, cuando se prevean corrientes diferenciales no
   senoidales se usarán diferenciales de clase: a) AC; **b) A, que asegura la desconexión para
   corrientes alternas senoidales y continuas pulsantes**; c) S; d) cualquiera de 30 mA. Y en un
   esquema TN-C los diferenciales: **no podrán utilizarse**. — Epígrafes 3.3 y 3.4.
4. (Diferenciales, práctica) En un esquema TT, con tensión límite convencional de 50 V y un
   diferencial de 300 mA, la resistencia máxima de la toma de tierra y conductores de protección
   es de unos: a) 16,7 Ω; **b) 167 Ω**; c) 1.667 Ω; d) 80 Ω. — Epígrafe 3.4.
5. (Fusibles, teoría y práctica) La ITC-BT-01 define el cortacircuito fusible como el aparato que
   interrumpe el circuito: **a) por fusión de uno de sus elementos, cuando la intensidad que lo
   recorre sobrepasa, durante un tiempo determinado, un cierto valor**; b) cuando la corriente
   diferencial alcanza un valor dado; c) por un relé térmico; d) por mínima tensión. Ante un fusible
   que «salta mucho», lo correcto es: **sustituirlo por otro idéntico en calibre, tamaño, clase y
   poder de corte tras buscar la causa**. — Epígrafe 4.
6. (Contactores, aplicación) En una inversión de giro, el enclavamiento eléctrico se hace: a) con
   un contacto NA de cada contactor en paralelo con el pulsador de marcha del otro; **b) con un
   contacto auxiliar NC de cada contactor en serie con la bobina del otro**; c) con el relé
   térmico; d) no hace falta si hay enclavamiento mecánico. — Epígrafe 5.3.
7. (Relés, teoría) Según la ITC-BT-47, la protección contra sobrecargas de un motor trifásico:
   a) basta en una fase; **b) debe ser tal que cubra el riesgo de la falta de tensión en una de sus
   fases**; c) sólo es exigible por encima de 0,75 kW; d) la sustituye el diferencial. Y en un
   esquema IT, el controlador permanente de aislamiento ante el primer defecto: **emite una señal
   acústica o visual**. — Epígrafes 6.1 y 6.2.
8. (Seccionadores, teoría) ¿Cuál NO figura en la ITC-BT-19 entre los dispositivos admitidos para
   la separación de la alimentación? a) los cortacircuitos fusibles; b) los seccionadores; c) los
   interruptores con separación de contactos mayor de 3 mm; **d) los contactores**. Y según el
   RD 614/2001, el método de trabajo en maniobras locales debe prever: **la apertura de
   seccionadores en carga y el cierre de seccionadores en cortocircuito**. — Epígrafes 1.5 y 7.
9. (Selectividad, teoría y práctica) En un esquema TT, un diferencial temporizado de tipo «S»
   instalado en serie con diferenciales de tipo general para lograr selectividad tendrá un tiempo
   de funcionamiento de: a) 0,2 s como máximo; b) 0,4 s como máximo; **c) 1 s como máximo**;
   d) 5 s como máximo. Y para que un defecto en un circuito de tomas con diferencial de 30 mA no
   deje sin servicio la planta, la cabecera debe ser: **de mayor sensibilidad asignada (por
   ejemplo 300 mA) y temporizada**. — Epígrafes 8.1 y 8.3.
10. (Sobretensiones, teoría y práctica) Según la ITC-BT-23, en una red de 230/400 V los equipos de
    categoría I (ordenadores, equipos electrónicos muy sensibles) tienen una tensión soportada a
    impulsos de: **a) 1,5 kV**; b) 2,5 kV; c) 4 kV; d) 6 kV. Una instalación alimentada por línea
    aérea con conductores desnudos está en: **situación controlada, con protección en el origen**.
    Y en una red TN-S los descargadores se conectan: **entre cada conductor de fase y el conductor
    de protección**. — Epígrafes 9.2, 9.3 y 9.4.
