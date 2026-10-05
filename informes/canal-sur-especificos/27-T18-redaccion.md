# Redacción · Oficial Técnico Electricista (27) · Tema 18 · Innovación aplicada al mantenimiento

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/18-innovacion-aplicada-al-mantenimiento.md`
(unas 12.900 palabras con tablas; 8 rúbricas, 45 epígrafes `###`). Material: `27-investigacion-D-mantenimiento.md`
§0, §3 y §5-6. Reuso RTVE según `informes/canal-sur-reuso/tecnica.tsv` (fila 27/18, 35 %, actualizar: **sí**):
ing-tec-industrial/11, ing-tec-industrial/13, teitse/12, teitse/09. `AGRUPACION.tsv`: 27/18 «nuevo».
Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo fija «hoy» en 24-09-2026; ninguna
fuente citada cambia entre ambas fechas: última reforma aplicada, RDL 7/2026, vigente desde 22-03-2026).

Escrito por partes (portada e introducción; 1-2; 3-4; 5; 6; 7; 8; normativa, «no da» y trazabilidad), guardando
cada parte. Índice generado con la regla de anclajes de GitHub (el tema no está en `portadas.tsv`, así que
`indice.py` no lo procesa; conviene añadir la fila si el coordinador regenera portadas).

Lentes: `refutar_prosa.py` (1 hallazgo, SCADA sin presentar: corregido; 0 tras corregir); `negritas.py` contra
BOE-A-2019-5089, BOE-A-2002-18099, DOUE-L-2023-81096, BOE-A-2007-15820, BOE-A-2016-1460 y las fichas de catálogo
(163 negritas; ver aviso 6).

Ficheros tocados: el tema (nuevo) y este informe. Temporales de catálogo y vista previa en el scratchpad y en
`/tmp/claude-0`, fuera del repositorio. Ninguna fuente nueva en `fuentes/`.

## Fuentes leídas por el redactor (05-10-2026)

- RD 244/2019 (`boe.py precepto`): arts. 1, 2, 3, 4, 5 y 14 vigentes; arts. 3 y 4 además con `--fecha` 20221221,
  20230101, 20250701, 20250801, 20251101, 20251210 y 20260301 (ver aviso 1).
- RD 1699/2011, art. 2 (sólo para decidir no usarlo: aviso 4).
- REBT, ITC-BT-40 apartados 1-4.3.4 (volcado `fuentes/canal-sur/BOE-A-2002-18099.md`; redacción del RD 244/2019).
- Reglamento (UE) 2023/1542 (volcado `DOUE-L-2023-81096.md`): art. 3.1 (puntos 7-30), 12, 13, 14, 15, 61.1, 96;
  anexos V, VI (A-C), VII y VIII (cabecera). Correcciones DOUE-L-2024-80529, -2024-81259, -2025-81464, -2026-80534:
  ninguna toca los preceptos citados (la de 2024-81259 rehace los arts. 77 y 78).
- RITE (volcado): apéndice 1 (instalación técnica del edificio, instalación térmica, cuatro niveles), IT 1.2.4.3.5,
  IT 1.2.4.4, IT 2.3.4, IT 2.4, IT 3.3 (nota de la tabla), IT 4.3.1-4.3.4.
- RD 56/2016, art. 3 entero.
- API de metadatos del BOE: títulos de BOE-A-2025-24545 (Ley 9/2025, de Movilidad Sostenible), BOE-A-2022-22685
  (RDL 20/2022) y BOE-A-2026-6544 (RDL 7/2026).
- tienda.aenor.com, fichas: UNE-EN ISO 52120-1:2022 (fecha 2022-10-19, «En Vigor», «Anula a UNE-EN 15232-1:2018»,
  título), ISO/IEC 30173:2023 (2023-11-08, resumen), ISO/IEC 30141:2024 (2024-08-27, resumen, «second edition»),
  ISO 17359:2018 (2018-01-24, resumen).
- Temas del puesto 7, 12 y 13 (sólo para remitir y no contradecir; no se copia de ellos: no han cerrado el ciclo).

## Avisos para el verificador

1. **La investigación se equivocó en la historia del RD 244/2019 y lo he corregido en el tema** (comprobado con
   `boe.py --fecha`): (a) la redacción inmediatamente anterior a la del RDL 7/2026 en el art. 3.g).iii, segundo
   párrafo, no era la de 2022 (cubierta, 1.000 m) sino la del RDL 20/2022 (vig. 28-12-2022), que amplió a «cubierta
   …, en suelo industrial o en estructuras artificiales…» y **2.000 m**; el RDL 7/2025 la llevó a 5.000 m y, derogado,
   volvió a regir la de 2.000 m (redacción de BOE-A-2025-15313). (b) La excepción del art. 4.5.b) **no la introduce el
   RDL 7/2026**: ya estaba desde el 05-12-2025 como inciso «ii.» por la **Ley 9/2025, de Movilidad Sostenible**
   (BOE-A-2025-24545, redacción que la investigación no listó); el RDL 7/2026 sólo pasa los incisos a letras. La
   investigación tampoco citaba la redacción BOE-A-2025-24545 del art. 4. El 4.5 de la redacción RDL 7/2025 (vig.
   25-06-2025) también tenía la excepción: no lo uso porque se derogó.
2. **Error de RTVE confirmado y corregido**: la comunidad de energías renovables es el art. 4.7, no una «regla» del
   4.5 (ing-tec-industrial/11 §4). Dicho en 7.5.
3. **ISO/IEC 30173, definición 3.1.1 y sus notas, y el «subcommittee 41»**: los tomo de la investigación (vista previa
   oficial leída allí); yo sólo he podido cotejar la definición con una reproducción secundaria (designingbuildings.co.uk,
   coincide palabra por palabra salvo «synchronisation» en ortografía británica de la BS). Las notas 1 y 2 y el nombre
   del subcomité **no los he releído**: si el verificador no accede a la vista previa, que las quite.
4. RD 1699/2011 no se usa: su art. 2 vigente trae la nota del BOE «Se derogan los párrafos primero y segundo por la
   disposición derogatoria única.a) del Real Decreto-ley 18/2022» mientras el texto mostrado conserva los apartados 1 y
   2; no he podido aclarar el alcance y lo dejo en «no da». (Aviso general: este artículo de RTVE, §2 de
   ing-tec-industrial/11, puede estar parcialmente derogado; afecta a cualquier otro tema que lo copie.)
5. Ejemplo propio (7.3): inversores que suman ≤ 100 kW con módulos de más potencia pico cumplen la condición ii del
   4.2.a), por el art. 3.h). Es aplicación del texto, no dato de la norma; así se dice.
6. `negritas.py`: 5 «NO ESTÁ»: dos rótulos de forma («Enunciado del programa», «Qué se puede preguntar») y tres
   fragmentos de la **redacción anterior** del art. 3.g).iii (no están en el volcado vigente; leídos con
   `boe.py --fecha 20260301`). 2 «atribuidas a otro artículo», falsos positivos: el anexo V va detrás del art. 96 en
   el volcado, y el 14.1 se cita también en 3.4 junto a una remisión a «epígrafe 6.3».
7. Lecturas que no son literales y van en redonda: que las baterías de SAI son «baterías industriales» (> 5 kg) y la
   de arranque del grupo «para arranque, encendido o alumbrado»; que una fotovoltaica de cubierta es instalación
   generadora interconectada; la condición de ubicación del 5.7 como regla antifraude.
8. Fechas del Reglamento 2023/1542 dadas: aplicación general 18-02-2024 (96.2); cap. VIII 18-08-2025 (96.2.c); 12.2 y
   14.1 18-08-2024; 13.4 18-08-2025; 13.6 18-02-2027; 13.1 con su «o … si esta fecha es posterior» y sin afirmar cuál
   rige (acto de ejecución del 13.10 no localizado).
9. Directiva 2006/66/CE: el tema dice «deroga, según su título»; no he leído la disposición derogatoria ni su fecha
   de efecto.
10. Solapes declarados por remisión, sin copiar: tema 12 (IT 1.2.4.3.5 completa, niveles, telemedida, conflictos con
   producción, epígrafe 7.5), tema 13 (UNE-EN 13306, ciclo del predictivo), tema 7 (baterías y agrupación), tema 16
   (RD 56/2016 ámbito). Lo citado aquí de la IT 1.2.4.3.5 y de la IT 4.3.4 repite literal del BOE que el tema 12 también
   cita; es intencionado para que el tema 18 conteste solo las preguntas de automatización.

## Copiado del común

Nada. El tema no desarrolla ninguna norma del temario común de Canal Sur, y no hay tema cerrado de Canal Sur del que
copiar: los temas 7, 12, 13 y 16 de este puesto aún no han cerrado el ciclo, y a ellos sólo se remite.

## Copiado de RTVE sin cambios

Nada. La fila 27/18 de `tecnica.tsv` marca los cuatro temas de RTVE como «actualizar: sí», así que ninguno es «tema
técnico sin actualizar». Además, RTVE pone en negrita casi toda su prosa propia; al pasarla a la convención de Canal
Sur (negrita = literal) cambia la forma de cada pasaje, y nada ha quedado «sin tocar una palabra».

## Adaptado de RTVE (se verifica entero)

- De ing-tec-industrial/11 (autoconsumo): tablas de modalidades (7.2), cinco condiciones de compensación (7.2, ahora
  literal del BOE vigente), individual y colectivo y la asimetría comunicación individual / acuerdo único (7.2),
  exclusiones del art. 2 (7.1), responsabilidad y corte del art. 5 (7.7), almacenamiento del 5.7 (7.6), tabla de la
  compensación del art. 14 y sus límites (7.8), tabla de decisiones y observación de escala del §7 (7.11, reescrita
  para un electricista). Quitado: lo térmico (§1), la conexión de pequeña potencia (§2), referencias a «tema 1/3/7» de
  RTVE, la portada y la trazabilidad de RTVE; corregidos el 4.5 (excepción de la letra b) y la comunidad (4.7).
- De ing-tec-industrial/13 (control): la observación de que registrar horas permite pasar a mantenimiento por
  condición (3.2), estrategias de control (8.5, reordenadas por ahorro / vida del equipo), distinción programación
  horaria / arranque óptimo y principio de autonomía (8.5), la rotación de equipos (5.5). Quitado: definición propia
  de BMS, pirámide, puntos, señales, protocolos, PID y conflictos audiovisuales (están en el tema 12 del puesto), el
  epígrafe 6 de RTVE (otras normas) y lo de «único punto sin norma».
- De teitse/12 (SAI y baterías): tabla de químicas (6.1), tensión en flotación frente a prueba de descarga (3.3),
  temperatura como lo que más acorta la vida (6.3), aviso de seguridad «una batería no tiene interruptor» (6.7),
  elemento más débil de la cadena (6.7).
- De teitse/09 (mantenimiento): tabla de tipos (3.1, sin «el más barato» como dato), las tres medidas del predictivo y
  el histórico (3.2), las tres medidas del motor (3.3).
- De ninguno: IoT, gemelo digital, Reglamento 2023/1542, ITC-BT-40 4.3, art. 3 del RD 244/2019 (definiciones,
  próximas, potencia fotovoltaica, antivertido), RITE IT 1.2.4.4 / 2.3.4 / apéndice 1, RD 56/2016 3.3.a y 3.5, UNE-EN
  ISO 52120-1.

## Diez preguntas tipo test (comprobación de cobertura antes de entregar)

Contestadas sólo con el tema. Todas **enteras**. Al comprobarlas no hizo falta ampliar; sí obligaron a corregir 7.4 y
7.5 (aviso 1), porque la respuesta sobre «qué cambió en 2026» habría sido falsa.

1. (Gemelo digital) Según la ISO/IEC 30173:2023, un gemelo digital es: a) un modelo tridimensional del edificio;
   **b) una representación digital de una entidad objetivo con conexiones de datos que permiten la convergencia entre
   los estados físico y digital a una tasa de sincronización adecuada**; c) el sinóptico del BMS; d) el archivo de
   planos digitalizado. — 4.1 y 4.2. **Entera.**
2. (Sensorización IoT) La norma que da la arquitectura de referencia del IoT es: a) ISO 17359:2018; b) UNE-EN ISO
   52120-1:2022; **c) ISO/IEC 30141:2024**; d) ISO/IEC 30173:2023. — 2.1. **Entera.**
3. (IoT y automatización) En el RITE, los módems y routers asociados a los puestos centrales pertenecen al nivel:
   a) de unidades de campo; b) de proceso; c) de comunicaciones; **d) de gestión y telegestión**. — 2.4 (apéndice 1).
   **Entera.**
4. (Mantenimiento predictivo) En la terminología normalizada UNE-EN 13306, el mantenimiento predictivo: a) es un tipo
   de correctivo diferido; **b) es una forma del preventivo basado en la condición**; c) es un tercer tipo al lado del
   preventivo y del correctivo; d) no aparece. — 3.1. **Entera.**
5. (Telegestión energética) El RITE obliga a disponer de un dispositivo que registre las horas de funcionamiento de las
   bombas y ventiladores cuya potencia eléctrica del motor sea mayor que: a) 5 kW; b) 10 kW; **c) 20 kW**; d) 70 kW. Y
   el Real Decreto 56/2016 exige que los datos de las auditorías: **se puedan almacenar para análisis histórico y
   trazabilidad**. — 5.2 y 5.4. **Entera.**
6. (Baterías) Entre los parámetros del estado de salud de un sistema estacionario de almacenamiento con baterías
   (anexo VII, parte A, del Reglamento (UE) 2023/1542) NO está: a) la capacidad restante; b) la evolución de los
   índices de autodescarga; c) la resistencia óhmica, en la medida de lo posible; **d) el número de ciclos completos
   de carga y descarga equivalentes** (es de la parte B, vida útil prevista). — 6.3. **Entera.**
7. (Baterías) Desde el 18 de febrero de 2027 todas las baterías llevarán código QR, que da acceso al pasaporte en las
   baterías industriales con capacidad superior a: a) 0,5 kWh; **b) 2 kWh**; c) 5 kWh; d) 100 kWh. Y una batería
   industrial usada la recoge el productor: **gratis y sin obligación de comprar otra**. — 6.5 y 6.6. **Entera.**
8. (Autoconsumo · práctica) Una cubierta tiene módulos fotovoltaicos de 120 kW pico conectados a dos inversores de
   45 kW de potencia máxima cada uno. A efectos del Real Decreto 244/2019 su potencia instalada es: a) 120 kW, y no
   puede acogerse a compensación; **b) 90 kW, y cumple la condición de potencia para la compensación**; c) 105 kW;
   d) 45 kW. Y una eólica de 4 MW a 3.000 m del consumidor, conectada por la red de distribución, es hoy
   instalación próxima: **sí (hasta 5 MW y a menos de 5.000 m, desde el 22-03-2026)**. — 7.3 y 7.4. **Entera.**
9. (Autoconsumo · práctica, ITC-BT-40) Al revisar el cuadro de una fotovoltaica de autoconsumo con excedentes en un
   edificio accesible al público, el circuito de generación debe ser: a) compartido con alumbrado, con diferencial
   AC de 300 mA; **b) independiente y dedicado, con diferencial tipo A de 30 mA**; c) independiente, sin diferencial;
   d) cualquiera, si el inversor tiene anti-isla. Y al consignar ese cuadro hay que contar con dos fuentes: **la red
   y el inversor**. — 7.9. **Entera.**
10. (Automatización de edificios) Un edificio no residencial con 350 kW de refrigeración deberá tener, cuando sea
    técnica y económicamente viable, sistema de automatización y control; si cumple las capacidades a), b) y c) de la
    IT 1.2.4.3.5.1: **a) queda exento de las inspecciones de la IT 4.2.1, 4.2.2 y 4.2.3**; b) queda exento del
    mantenimiento preventivo; c) puede espaciar el mantenimiento a dos años; d) nada. Y la norma UNE que cita el RITE
    para ese sistema está hoy: **anulada por la UNE-EN ISO 52120-1:2022**. — 8.1, 8.2 y 8.4 (y 5.3 para descartar la
    c, que es de instalaciones de hasta 70 kW). **Entera.**

Reparto: gemelo digital 1, IoT 2, predictivo 1, telegestión 1, baterías 2, autoconsumo 2, automatización 1;
aplicación práctica en 8, 9 y 10.
