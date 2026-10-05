# Redacción · Oficial Técnico Electricista (27) · Tema 9 · Climatización y frío industrial aplicado al mantenimiento de edificios y salas técnicas

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/09-climatizacion-y-frio-industrial-en-edificios-y-salas-tecnicas.md`
(15.427 palabras según `indice.py`, tablas incluidas; 48 epígrafes). Material:
`27-investigacion-C-clima-gestion.md` (§0 y §9 enteros; de §10.4, la IT 3 y la IT 3.8). Reuso RTVE
(25 %, actualizar: sí): `ing-tec-industrial/02` (§1, 2, 3, 5 y 6) e `ing-tec-industrial/01` (§1).
Fecha declarada: 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»). Escrito por
partes (cabecera y epígrafes 1-2; 3-5; 6-7 y cierre), guardando cada una.

Ficheros tocados: el tema (nuevo) y este informe. En el scratchpad: la tarjeta de ASHRAE
(`ashrae.pdf`/`ashrae.txt`) y una copia previa al índice.

Lentes corridas: `indice.py` (índice generado); `refutar_prosa.py` (queda 1 hallazgo: «GF» en la
tabla de filtros, que el propio RITE define en la línea siguiente; se deja); `negritas.py` contra
BOE-A-2019-15228, BOE-A-2007-15820, el texto del Reglamento (UE) 2024/573, la guía IDAE y la tarjeta
ASHRAE (414 negritas cotejadas; las 4 que no están son rótulos, la sigla «t CO2-eq» y la cita del
RDL 14/2022, leída con `boe.py precepto BOE-A-2022-12925 df-17`; las 5 «atribuidas a otro artículo»
son falsos positivos: filas de la tabla del art. 18 y «bombas de calor» del art. 5.2 del reglamento
europeo).

## Estructura

Siete epígrafes en el orden del enunciado: 1 principios básicos (qué es climatizar, frontera
RITE/RSIF, ciclo, COP/EER, aire húmedo); 2 equipos (familias IDAE, clasificaciones del RSIF, niveles,
sala de máquinas); 3 refrigerantes (grupos L, PCG y t CO2-eq, prohibiciones, quién manipula); 4
ventilación (IDA, caudales, filtros, AE, enfriamiento gratuito, IDA-C, higiene); 5 control de
temperatura y humedad (diseño, IT 3.8, THM-C, salas técnicas/ASHRAE, sondas); 6 averías (señales
IF-17, tabla de diagnóstico, fugas, reparación IF-14, reparto electricista/frigorista, accidentes);
7 mantenimiento preventivo (obligaciones del titular, programa RSIF, RITE IT 3.3/3.4.2, gama IDAE,
control de fugas UE, revisiones e inspecciones, calendario). Normativa; lo que no da; trazabilidad.

## Fuentes leídas por el redactor (05-10-2026)

- RD 552/2019, volcado `fuentes/canal-sur/BOE-A-2019-15228.md` (vigente hoy): arts. 1-9, 18-22,
  26-29; IF-14 entera (vig. 10-05-2025); IF-17 (1.1, 1.5.1, 1.6, 2.3, 2.4, 2.5).
- RITE, volcado `BOE-A-2007-15820.md`: arts. 1-2; IT 1.1.4.1-1.1.4.3; IT 1.2.4.3.2-3; IT 1.2.4.5.1-2;
  IT 3 entera; apéndice 1.
- RDL 14/2022: art. 29 y DF 17.ª con `boe.py` (bloques `a2-11`, `df-17`).
- Reglamento (UE) 2024/573, `fuentes/canal-sur/documentos/reglamento-ue-2024-573.txt`: arts. 3, 4,
  5, 6, 7, 8, 11.1, 13, 37, 38; anexos I, IV (7, 8, 9), VI.
- Guía IDAE, `idae-guia-mantenimiento-termicas.txt`: índice de familias, gamas de las familias 6, 9,
  12 y 14, leyenda de frecuencias, autores.
- ASHRAE TC 9.9 Reference Card: descargada de nuevo y leída (18 a 27 °C; 15 a 32 °C A1).

## Correcciones a la investigación

- Anexo IV 9.c) (partidos aire-aire ≤ 12 kW, PCG ≥ 150): la fecha es **1 de enero de 2029**, no
  2027 como dice la investigación (9.1). 2027 es la del 9.b) (aire-agua). Aplicado en el tema.
- La investigación dice que el visualizador de la IT 3.8.3 es obligatorio en recintos de más de
  1.000 m²: correcto; además el texto exige «como mínimo, de uno cada 1.000 m2» (recogido).
- Nada más que corregir; el resto de citas de la investigación usadas coinciden con la fuente.

## Avisos para el verificador

- 1.1: que la refrigeración de una sala de equipos o CPD quede fuera del RITE por el art. 2.6 va
  declarada como lectura, no como texto.
- 3.2 y 7.5: los cálculos de t CO2-eq son aritmética con cifras supuestas; los PCG, del anexo I.
- 3.3: tabla de prohibiciones del art. 13; las salvedades de 13.3 resumidas, la de 13.4 literal.
- 4.2 y 4.7: asignar oficinas, salas de ordenadores, platós y salones de actos a IDA/IDA-C es lectura
  de aplicación salvo donde el RITE nombra el uso (oficinas, salas de ordenadores, salones de actos).
- 5.2: aplicar la salvedad de la IT 3.8.2.3 a una sala técnica, lectura.
- 6.2 (tabla de averías), 6.5 (tabla del reparto) y 7.7 (calendario): oficio o síntesis, declarados.
- 1.2: el ciclo de compresión es oficio; sólo van en negrita las citas del RITE.

## Copiado del común

Nada. El tema no desarrolla ninguna norma del temario común de Canal Sur y `27-args.json` no marca
repetición para el tema 9.

## Copiado de RTVE sin cambios

Nada. `27-args.json` marca el reuso del tema 9 con «actualizar: sí», y además todo lo aprovechable de
RTVE cita normas; por las dos razones, lo tomado de RTVE se verifica entero. Para el verificador, lo
que procede de RTVE (adaptado: quitadas negritas y mayúsculas de énfasis, pies «vigente el 21 de
diciembre de 2022», remisiones a sus temas, y rehechas las tablas con el texto literal del BOE
releído):

De `ing-tec-industrial/02`:
- §1, tabla de los tres escalones del art. 2 y la cita del 2.4, con «lo que se excluye es el
  sistema, no la instalación» (en 1.1); la frase de la enfriadora en los dos reglamentos (1.1).
- §2, tablas de los arts. 4.2, 6.1, 6.2 y 7.1-7.2, la regla de memoria de los cuatro tipos, la del
  3,5 % contraintuitivo y la de la separación física (en 2.2, 2.3 y 3.1).
- §3, tabla del art. 8, aviso de potencia eléctrica, acumulativas, cascada y art. 20.2 (en 2.3).
- §5, tabla del art. 18 (ampliada a las letras f, h, i, l, m, o y p completas; p corregida: RTVE sólo
  recogía la primera mitad), letra j) y su comentario (en 6.6 y 7.1).
- §6, art. 9.1 y 9.2 (en 3.4).
De `ing-tec-industrial/01`:
- §1, cita del art. 2.6 y la lectura «en la parte que no» (en 1.1).

Quitado de RTVE por fuera del enunciado o sin releer: el TEWI y el anexo del proyecto (art. 20.2),
las cinco vías del art. 9.1 y las pasarelas de soldadura del 9.3, la comparación con la vía
alternativa del RITE (art. 19), y la exención del seguro A2L se conserva resumida tras releerla.

## Preguntas de control (10, contestadas sólo con el tema)

1. (Principios) Según el RITE, el EER es: a) la relación entre la capacidad calorífica y la potencia
   absorbida; b) **la relación entre la capacidad frigorífica y la potencia efectivamente absorbida
   por la unidad**; c) el rendimiento estacional en calefacción; d) la potencia eléctrica por kW de
   frío. → b. Tema 1.3. Entera.
2. (Principios, práctica) En un ciclo de compresión, el refrigerante absorbe el calor de la sala:
   a) en el condensador, a alta presión; b) en el compresor; c) **en el evaporador, al evaporarse a
   baja presión**; d) en la válvula de expansión. → c. Tema 1.2. Entera.
3. (Equipos, práctica) Una instalación con refrigerante L1, cinco sistemas de 25 kW eléctricos de
   compresor cada uno en la misma sala de máquinas y sin cámaras de atmósfera artificial es de:
   a) nivel 1, porque ningún sistema pasa de 30 kW; b) **nivel 2, porque la suma de las potencias
   eléctricas de los compresores (125 kW) excede de 100 kW**; c) nivel 1, porque se cuentan potencias
   frigoríficas; d) depende de la categoría del local. → b. Tema 2.3. Entera (misma sala de máquinas
   = misma instalación; condiciones acumulativas).
4. (Refrigerantes) El grupo L3 del RSIF agrupa los refrigerantes: a) no inflamables de toxicidad
   nula; b) tóxicos con LII igual o superior al 3,5 %; c) **inflamables o explosivos mezclados con aire
   en un porcentaje en volumen inferior al 3,5 por cien**; d) los A2L. → c. Tema 3.1. Entera.
5. (Refrigerantes, práctica) Un equipo autónomo fijo de aire acondicionado con 8 kg de HFC-32 (PCG
   675), sin sistema de detección de fugas: a) no está sujeto a control de fugas; b) **contiene 5,4 t
   CO2-eq y debe someterse a control de fugas al menos cada doce meses**; c) cada seis meses; d) cada
   tres meses. → b. Tema 3.2 y 7.5. Entera.
6. (Refrigerantes) Desde el 1 de enero de 2026, para el mantenimiento de aparatos de aire
   acondicionado y bombas de calor, los gases fluorados del anexo I con PCG igual o superior a 2.500:
   a) se pueden usar sin límite hasta 2030; b) **están prohibidos, salvo los regenerados o reciclados
   hasta el 1 de enero de 2032**; c) están prohibidos sin excepción; d) sólo se prohíben en equipos de
   más de 40 t CO2-eq. → b. Tema 3.3. Entera.
7. (Ventilación) El RITE clasifica las salas de ordenadores en la categoría de calidad de aire
   interior: a) IDA 1; b) IDA 2; c) **IDA 3**; d) IDA 4. Y el único aire de extracción que puede
   retornarse a los locales es el **AE 1, exento de humo de tabaco**. → c. Tema 4.2 y 4.5. Entera.
8. (Control de temperatura y humedad) En un edificio de uso administrativo, en uso, la temperatura de
   un recinto refrigerado con energía convencional: a) no será inferior a 27 °C; b) **no será inferior
   a 26 °C, referida a una humedad relativa entre el 30 % y el 70 %**; c) estará entre 23 y 25 °C;
   d) no será inferior a 24 °C. Y una sala que justifique condiciones ambientales especiales queda
   exenta si está separada físicamente. → b. Tema 5.2. Entera.
9. (Averías, práctica) En una revisión se detecta que una máquina ha perdido carga de refrigerante:
   a) se recarga y se anota; b) **no se recarga en ningún caso sin haber localizado y reparado la
   fuga, y la reparación se comprueba con un control de fugas antes de un mes**; c) se recarga y se
   revisa en la próxima revisión quinquenal; d) se recarga con gas recuperado de otra máquina. → b.
   Tema 6.3 (y 3.4 para la d). Entera.
10. (Mantenimiento preventivo) El electricista de plantilla debe cambiar el contactor de un compresor
    de una instalación frigorífica: a) puede hacerlo libremente, es una tarea eléctrica; b) **según la
    IF-14, las operaciones que requieran electricistas se realizan bajo la supervisión de una empresa
    frigorista**; c) sólo puede hacerlo un organismo de control; d) necesita certificado de gases
    fluorados. Y la revisión periódica obligatoria del RSIF es **como mínimo cada cinco años**. → b.
    Tema 6.5 y 7.6. Entera.

Reparto: principios (1, 2), equipos (3), refrigerantes (4, 5, 6), ventilación (7), temperatura y
humedad (8), averías (9), mantenimiento preventivo (10, y 5 por el control de fugas). Prácticas: 2,
3, 5, 9, 10. Las diez se contestan enteras con el tema; no ha hecho falta ampliar. Otras que el tema también contesta y quedan para la fase 4: rango recomendado de ASHRAE
para salas de equipos (18-27 °C, 5.4), caudal de aire exterior por superficie en locales sin
ocupación permanente (4.3), obligación de enfriamiento gratuito en sistemas todo aire de más de 70 kW
(4.6), categoría THM-C que controla la humedad en los locales (5.3), orden de los nueve pasos de una
reparación con refrigerante (6.4), refrigerante máximo almacenado en sala de máquinas (20 % y 150 kg,
2.4), periodicidad mensual del RITE en instalaciones de más de 70 kW (7.3), inspección de nivel 2 cada
diez años (7.6) e inspección al final de la jornada por personas encerradas (6.6).
