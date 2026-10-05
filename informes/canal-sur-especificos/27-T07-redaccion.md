# Redacción · Oficial Técnico Electricista (27) · Tema 7 · Grupos electrógenos, SAI y continuidad de servicio

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/07-grupos-electrogenos-sai-y-continuidad-de-servicio.md`
(11.600 palabras según `indice.py`, 43 epígrafes). Material: `27-investigacion-B-alimentacion-instalaciones.md`
(§7 y, de §6.1 y §11.3, lo que toca a fuentes de alimentación). Reuso RTVE: `teitse/11` y `teitse/12`
(actualizar: no). Fecha declarada: 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»).
Lentes corridas: `indice.py` (índice generado), `refutar_prosa.py` (0 hallazgos tras presentar
TT y UNE), `negritas.py` contra BOE-A-2002-18099 y BOE-A-2017-6606 (106 negritas cotejadas; las 9
que no están son siglas, rótulos y las citas en inglés de Sölter, que no son del BOE).

Ficheros tocados: el tema (nuevo, y su carpeta `27-oficial-tecnico-electricista/`, que no existía)
y este informe.

## Estructura

Rúbricas en el orden del enunciado: 1 Grupos electrógenos; 2 SAI; 3 Continuidad de servicio;
4 Transferencia de carga; 5 Baterías; 6 Autonomía; 7 Pruebas periódicas; 8 Actuación ante
incidencias; normativa; lo que no da; trazabilidad.

## Fuentes leídas por el redactor (05-10-2026)

- ITC-BT-28 entera (`boe.py precepto BOE-A-2002-18099 ib-28`, redacción única): apdos. 2, 2.1, 2.2,
  2.3, 3, 3.1.1-3.1.3, 4.g. Lo nuevo frente a la investigación: el texto literal de las cinco
  categorías de conmutación, de las fuentes admitidas y sus condiciones, de la fuente propia y de
  la regla «automática con corte breve» del alumbrado de emergencia (teitse/11 y 12 las remitían a
  un «tema 8» de RTVE que no está en el reuso).
- ITC-BT-40 entera (`ib-40`, redacción del RD 244/2019, vigente desde 07-04-2019): apdos. 1, 2, 3,
  4.1, 4.2, 5, 6, 7, 8.2.1, 8.2.2 y 9. Casa con lo que teitse/11 §4 afirmaba del «tema 10».
- Artículo 10 del REBT (volcado `fuentes/canal-sur/BOE-A-2002-18099.md`, redacción única).
- RIPCI, anexo II, apdo. 1 y tabla I (volcado `BOE-A-2017-6606.md`, redacción desde 10-05-2025).
  La columna «tres meses» de la fila «Fuentes de alimentación» se toma de la investigación (11.3),
  que leyó el HTML: en el volcado plano las columnas no se distinguen. **El verificador debe
  confirmarla.** Las filas de abastecimiento de agua se citan sin periodicidad.
- Sölter sobre IEC 62040-3: de la investigación (7.2), sin releer.

## Avisos para el verificador

- ITC-BT-40, apdo. 6: el BOE dice «ordenn»; se cita literal partiendo la negrita y anotando «(así en
  el BOE, por «orden n»)».
- ITC-BT-40, apdo. 7 (protecciones mínimas con 85 %, 110 %, 49/51 Hz): el apartado no restringe su
  ámbito a las interconectadas; el tema lo cita como exigencia general del generador y su lectura
  («con esos ajustes, … se desconecta») va como oficio. Comprobar que no se le da más alcance.
- La asignación de categorías de conmutación a cada fuente (3.1, tabla) es oficio y así se declara;
  la ITC no asigna categorías a las fuentes.
- «Ninguna norma leída fija periodicidad de prueba de grupos/SAI»: dicho como hueco, no como
  afirmación de que no exista (investigación 7.3).
- El ejemplo numérico de 5.3 y 6.1 lleva cifras supuestas, declaradas.

## Copiado del común

Nada. El tema no desarrolla ninguna norma del temario común de Canal Sur y no hay temas cerrados
del puesto 27 (ni repetición en `27-args.json` para el tema 7).

## Copiado de RTVE sin cambios

De `teitse/11` y `teitse/12` (actualizar: no). Sólo se han quitado las negritas y las mayúsculas de
énfasis (en RTVE son de énfasis, no de literal de fuente). Ninguno cita norma. Todo lo demás que
viene de RTVE está adaptado (quitadas remisiones a sus temas 2, 8, 9 y 10, «este temario», «casa
que emite», «del punto») o lleva norma, y se verifica.

De `teitse/11`:

- §1, la frase «Un grupo electrógeno es un conjunto motor-alternador que convierte la energía
  química de un combustible en energía eléctrica.», el párrafo «Y la relación que hay que saber y
  que explica el regulador de velocidad: … y no un mal voltaje.» y la frase «Los dos parámetros que
  se ajustan por separado y que hay que no confundir:» con su tabla (frecuencia/tensión). En 1.1.
- §2, los párrafos «Primero, el régimen de servicio. …» con la tabla de regímenes, «Y la regla que
  sale de la tabla…», «Segundo, la potencia y el factor de potencia. …», «Tercero, las condiciones
  ambientales. …» con su tabla (altitud, temperatura, humedad). En 1.2.
- §3, el párrafo «Y el escape merece su párrafo: … respire su propio humo.» y la tabla de las tres
  vías del ruido. En 1.3.
- §5, la frase de entrada «Lo que ocurre desde que falla la red … cuadro de control:», la tabla de
  nueve fases, y «Las dos fases que la gente no espera…» con sus dos viñetas (la 7 y la 9). En 1.5.
- §6, la tabla de tareas del grupo (ocho filas). En 7.1.
- §7, punto 2 («La refrigeración de las salas técnicas va en el grupo. … no sirve.»). En 3.4.

De `teitse/12`:

- §1, la tabla de los cinco bloques; «Y los dos bypass son lo que más se confunde y hay que
  separarlos con claridad:» con su tabla; y el párrafo «La razón de ser del bypass de mantenimiento
  merece una frase: … el día en que hay que tocarlo.». En 2.1.
- §2, la tabla de topologías y los párrafos «La tercera es la única que cumple la categoría «sin
  corte»… La salida no se entera.» y «Y lo que las otras dos aportan a cambio: … ya no es «sin
  corte».». En 2.2. La tabla de prestaciones (cinco filas), en 2.4.
- §3, la tabla pila/acumulador, la tabla de parámetros (ocho filas), el párrafo «Y el aviso que hay
  que dar sobre la capacidad, … es el error de cálculo clásico.» y la tabla de químicas (cuatro
  filas). En 5.1 y 5.2.
- §4, la tabla de agrupación; «Y la regla que hay que enunciar y que resume las dos: …»; la lista
  1-3 de condiciones de agrupación; «La consecuencia práctica de las dos últimas, … Lo que se
  sustituye es el conjunto.»; «Y la energía es lo único que se conserva … se entrega.». En 5.3.
- §5, la tabla de mantenimiento (siete filas), en 7.2; y las frases «Una batería no tiene
  interruptor. … se funde.», en 8.4.

## Lo nuevo (pasa entero por el ciclo)

1.1 (ITC-BT-40 apdo. 1); 1.3 primera mitad (apdo. 3 literal); 1.4 entero (apdos. 5, 6, 7); 2.3
entero (IEC 62040-3 vía Sölter); el párrafo final de 2.4 (rectificador y grupo); 3.1, 3.2 y 3.3
enteros (ITC-BT-28 y art. 10); 3.4 puntos 3 y 4 y la cadena completa; 4.1 a 4.6 (lo literal de la
ITC-BT-40 y la tabla y la maniobra del bypass, oficio); 5 entrada y párrafo de la batería de
arranque; 5.3 ejemplo; 6.1 margen y cálculo; 6.2 segunda mitad; 6.3 entero; 7.3 entero (ITC-BT-28
2.1 y RIPCI); 8.1 a 8.3 enteros y el último párrafo de 8.4 (oficio).

## Comprobación con 10 preguntas tipo test

Contestadas sólo con el tema. Las diez, enteras; no ha hecho falta ampliar.

1. (Grupos) En un grupo electrógeno, la frecuencia de la tensión generada se ajusta con:
   a) el regulador de excitación del alternador; b) el regulador de velocidad del motor; c) el
   cargador de la batería de arranque; d) el conmutador red-grupo. → **b**. Tema 1.1 (tabla de los
   dos parámetros). Entera.
2. (Grupos, ITC-BT-40) Los cables de conexión de un generador se dimensionan para una intensidad no
   inferior al … de la máxima del generador, con caída de tensión hasta el punto de interconexión no
   superior al …: a) 100 % y 3 %; b) 125 % y 1,5 %; c) 125 % y 3 %; d) 150 % y 1,5 %. → **b**.
   Tema 1.4. Entera.
3. (SAI) En la clasificación de la IEC 62040-3, la topología de doble conversión corresponde a la
   clase: a) VFD; b) VI; c) VFI; d) VFS. → **c**. Tema 2.3. Entera.
4. (Continuidad, ITC-BT-28) Una alimentación automática «con corte breve» está disponible en:
   a) 0,15 s como máximo; b) 0,5 s como máximo; c) 15 s como máximo; d) más de 15 s. → **b**.
   Tema 3.1 (y la consecuencia: el alumbrado de emergencia, «automática con corte breve», no puede
   depender sólo de un grupo). Entera.
5. (Continuidad, ITC-BT-28) Una fuente propia de energía se pone en funcionamiento al faltar la
   tensión de la distribuidora o cuando ésta desciende por debajo del: a) 85 %; b) 80 %; c) 70 %;
   d) 50 % de su valor nominal. → **c**. Tema 3.2 (y 1.5). Entera.
6. (Transferencia, ITC-BT-40) En una instalación generadora asistida, la transferencia de carga sin
   corte: a) está prohibida; b) sólo para generadores de más de 100 kVA, con conexión en punto
   único y sin mantener la interconexión más de 5 segundos; c) para cualquier potencia si hay
   enclavamiento; d) sólo si la instalación es interconectada. → **b**. Tema 4.3. Entera.
7. (Baterías) Dos ramas en paralelo, cada una de cuatro bloques de 12 V y 100 Ah en serie, dan:
   a) 48 V y 100 Ah; b) 24 V y 400 Ah; c) 48 V y 200 Ah; d) 96 V y 200 Ah. → **c**. Tema 5.3 (reglas
   y ejemplo). Entera.
8. (Autonomía, ITC-BT-28) La capacidad mínima de una fuente propia de energía es, como norma
   general, la precisa para el alumbrado de seguridad, cuyo alumbrado de evacuación debe funcionar
   tras el fallo como mínimo: a) 30 minutos; b) una hora; c) dos horas; d) el tiempo de arranque del
   grupo. → **b**. Tema 3.2 y 6.3. Entera.
9. (Pruebas periódicas, RIPCI) La «revisión de sistemas de baterías» de las fuentes de alimentación
   de la detección y alarma de incendios (prueba de conmutación en fallo de red, funcionamiento
   bajo baterías, detección de avería y restitución) se hace: a) cada mes; b) cada tres meses;
   c) cada año; d) cada cinco años. → **b**. Tema 7.3 (pendiente de que el verificador confirme la
   columna). Entera.
10. (Actuación ante incidencias, práctica) Un cortocircuito en un solo circuito derivado de un SAI
    de doble conversión deja sin tensión toda la carga del SAI sin que salte el magnetotérmico del
    circuito. La causa más probable es: a) batería agotada; b) el inversor limita su corriente de
    salida y el magnetotérmico no recibe corriente suficiente para disparar, así que el SAI se
    protege pasando a bypass o desconectando; c) falta de neutro en la conmutación; d) el grupo no
    ha arrancado. → **b**. Tema 2.4 y 8.3. Entera.
