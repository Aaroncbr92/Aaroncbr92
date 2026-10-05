# Redacción · Oficial Técnico Electricista (27) · Tema 12 · Sistemas de gestión técnica de edificios y monitorización

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/12-sistemas-de-gestion-tecnica-de-edificios-y-monitorizacion.md`
(10.902 palabras según `indice.py`, 37 epígrafes). Material: `27-investigacion-C-clima-gestion.md`
(§0, §10.2, §12). Reuso RTVE: `ing-tec-industrial/13-control-automatizado-de-instalaciones.md`
(75 %, actualizar: **no**; `tecnica.tsv` fila 27/12). `AGRUPACION.tsv`: tema «nuevo» (el 23/13
comparte fuente RTVE pero no está escrito). Fecha declarada de lectura: 05-10-2026 (reloj del
sistema; el encargo dice «hoy es 24-09-2026»). Lentes: `indice.py` (índice generado),
`refutar_prosa.py` (6 avisos, todos explicados abajo), `negritas.py` contra RITE, RIPCI, guía IDAE,
Modbus e ISO 16484-5 (141 negritas; las que no casan, abajo).

Ficheros tocados: el tema (nuevo) y este informe. En el scratchpad, sin tocar el repositorio:
`modbus.pdf/.txt`, `bacnet2026.pdf/.txt`, `knx.pdf/.txt` (descargados para leer la fuente).

## Estructura

1 Sistemas de gestión técnica y monitorización (definición RITE, separación de sistemas, prioridad
de incendios RIPCI, razones, IT 1.2.4.3.5 y sus ventajas, cuatro niveles del RITE + pirámide de
RTVE, puesta en servicio IT 2.3.4); 2 BMS/SCADA (BMS-SCADA-autómata con definición NIST, protocolos
BACnet/Modbus/KNX, estrategias de control y lazo PID, gama IDAE del puesto central); 3 Sensores
(puntos, clases IDAE, puntos del puesto, señales, contraste); 4 Alarmas (origen, prioridades,
reconocimiento, rearme IT 1.2.4.3.1.3, gama IDAE de alarmas); 5 Históricos (IT 1.2.4.4, IT 3.4.2,
IT 3.4.4-3.4.5, usos, hora y copias); 6 Telemedida (telemedida/telemando/telegestión, gama IDAE de
integraciones y telegestión); 7 Actuación ante avisos (marco normativo, procedimiento diario IDAE,
nueve pasos, casos del puesto, convivencia con producción); normativa; lo que no da; trazabilidad.

## Fuentes leídas por el redactor (05-10-2026)

- RITE (`fuentes/canal-sur/BOE-A-2007-15820.md`, redacción vigente): arts. 2.1, 12.3, 25.3; IT
  1.2.4.3.1 (ap. 1 y 3), 1.2.4.3.5 entera, 1.2.4.4 ap. 2-7, 1.2.4.5.1.1, 1.3.4.1.2.2.p), 2.3.4, 3.3
  (pie tabla 3.1), 3.4.2 (tabla 3.3), 3.4.4, 3.4.5, 3.6.2, 3.7, 4.3.4; apéndice 1 (cinco
  definiciones); apéndice 2 (filas UNE-EN 15232-1:2018 y UNE-EN ISO 16484-3:2006). Confirmo lo de la
  investigación §0 y §12.1.
- RIPCI (`BOE-A-2017-6606.md`): anexo I, sección 1.ª, apdo. 1.7 (redacción vigente desde
  10-05-2025, BOE-A-2025-7190).
- Guía IDAE (`fuentes/canal-sur/documentos/idae-guia-mantenimiento-termicas.txt`): familia 23 (ficha,
  listado de puntos, claves ED…CT), gama «Control DDC (Computerizado)» operaciones 48-97 y 37, 39, 42
  del autómata; apéndice III (claves de frecuencia); cap. 5 (procedimiento diario; datos nominales).
- Modbus V1.1b3 (descargada de modbus.org; texto con `documento.py`): §1.1 y §4.3.
- **Novedad frente a la investigación**: ISO 16484-5 tiene **octava edición 2026-08**; la EN ISO
  16484-5:2026 se publicó el 25-08-2026 y sustituye a la de 2022 (ficha del catálogo iTeh y muestra
  SIST EN ISO 16484-5:2026, «Nadomešča SIST EN ISO 16484-5:2022»). El tema cita la de 2026. El objeto
  («The purpose…») sale de la ficha del catálogo (web, no del PDF); los tipos de objeto, capítulo
  13, MS/TP, anexos J y U, del índice del PDF de muestra. La lista de ocho tipos de dato de la
  cláusula 2.1 (investigación, edición 2022) **no se usa**: no la he podido leer en la de 2026.
- NIST CSRC, glosario «SCADA» (de SP 800-82r3): definición literal (web).
- knx.org «What is KNX»: dos expresiones literales (web). La investigación no daba fuente primaria;
  la norma ISO/IEC 14543-3-1:2006 (muestra iTeh) **no menciona KNX** en lo leído, así que no se da
  número de norma.

## Avisos para el verificador

1. Negritas que `negritas.py` no encuentra: «Enunciado del programa» y «Qué se puede preguntar»
   (rótulos de forma, como en otros temas); las de NIST, ISO 16484-5 (objeto) y KNX son literales de
   páginas web, no de un volcado: comprobar en la URL de la trazabilidad.
2. `refutar_prosa.py`: «siglas sin presentar» ED, SD, SS, EA, SA, CT: se presentan en la propia
   cita literal del IDAE («ED = Entrada Digital»…); no es error.
3. La guía IDAE es de 2007 y sus frecuencias son «recomendadas»: el tema lo dice. Operación 71 con
   la errata del original «de a lazos», citada tal cual; la guía repite el número 85 (dicho).
4. RTVE §6 (CTE HE 3, SUA 4, alumbrado exterior art. 4.3.º) **no se copia**: cita normas no leídas
   en esta fase y su materia es del tema 6/10. Del RITE sólo se da lo releído.
5. Investigación: «IT 1.3.4.1.2.2.p)» confirmada (el tema 10 usa la misma cita). La EN 15232-1
   sustituida por la EN ISO 52120-1 no se ha comprobado: el tema lo declara como hueco.
6. Se han quitado de RTVE dos cifras sin fuente: «una hora de climatización diaria» y «cuesta diez
   veces más».

## Copiado del común

Nada. El tema no desarrolla ninguna norma del temario común de Canal Sur.

## Copiado de RTVE sin cambios

Pasajes de `temas/ing-tec-industrial/13-control-automatizado-de-instalaciones.md` (marcado sin
actualizar) copiados con las mismas palabras. Único cambio de forma: se quitan las negritas de RTVE
(aquí la negrita es sólo literal de fuente, y estos pasajes son oficio) y se añade, fuera del
pasaje, la marca «(oficio)». El verificador sólo comprueba que son literales:

- 1.1: «La regla de diseño que sale de esa tabla y que un examen podría pedir: … el error de
  arquitectura más caro del punto.» (RTVE §1).
- 1.2: tabla de las cuatro razones y párrafo «La tercera es la que más se infravalora … mantenimiento
  por condición.» (RTVE §1).
- 1.4: «Cuatro niveles, y cada uno con su equipo, su tiempo de respuesta y su tipo de dato:», tabla
  de la pirámide, párrafo «La regla que ordena la pirámide …» y párrafo «Y el principio de autonomía
  …» (RTVE §2).
- 2.2: tabla abierto/propietario, tabla de los grupos de protocolos y párrafo «El aviso de
  seguridad, que es la contrapartida de esa tendencia: … medida de seguridad física.» (RTVE §4).
- 2.3: «Ésta es la parte que un examen puede pedir enumerada, y es lo que de verdad ahorra
  energía», tabla de estrategias, «El lazo de control clásico, con sus tres acciones, que hay que
  saber nombrar», tabla P-I-D y párrafo «El aviso de ajuste que se aprende en obra …» (RTVE §5).
- 3.1: «El «punto» es la unidad de cuenta … y es con lo que se presupuesta» y tabla de los cuatro
  tipos de punto (RTVE §3).
- 3.2: tabla de señales y párrafo «La ventaja del rango 4-20 es el dato de oficio más útil de este
  epígrafe: … nadie se entera.» (RTVE §3).
- 7.5: tabla de los cuatro conflictos y párrafo «Los cuatro se resuelven con la misma idea … veinte
  sensores de presencia.» (RTVE §7).

Adaptados (se verifican): tabla de separación de sistemas (remisiones de RTVE a sus temas 6 y 19
cambiadas), frase de reserva de puntos (quitada la remisión al tema 16), entrada de señales (quitado
«normalizadas» y «un ingeniero»), entrada de protocolos, tendencia hacia la red de datos (sin «todo
el temario técnico»), programación horaria/arranque óptimo y limitación/rotación (quitadas las
frases con cifra o con «ingeniero»), entrada de 7.5 y cierre de 7.5 (quitada la cifra).

## Preguntas tipo test de comprobación (10)

1. Según el RITE, los edificios no residenciales deben estar equipados con sistemas de
   automatización y control, cuando sea técnica y económicamente viable, si su potencia nominal útil
   de calefacción, refrigeración o combinadas supera: a) 70 kW; b) 290 kW; c) 400 kW; d) 1.000 kW.
   **b**. Tema 1.3 — entera.
2. En los niveles del RITE, los controladores analógicos y digitales que manejan los elementos de
   periferia forman el nivel: a) de unidades de campo; b) de proceso; c) de comunicaciones; d) de
   gestión y telegestión. **b**. Tema 1.4 — entera.
3. El mantenimiento y la actualización de versiones de los programas de un sistema de telegestión
   basado en tecnología de la información los realiza: a) cualquier mantenedor; b) el titular; c)
   personal cualificado o el suministrador de los programas; d) un organismo de control. **c**.
   Tema 1.5 — entera.
4. Una instalación de hasta 70 kW con supervisión remota en continuo puede ampliar la periodicidad
   de su mantenimiento preventivo hasta: a) 6 meses; b) 1 año; c) 2 años; d) 4 años. **c**. Tema
   1.3 y 6.1 — entera.
5. En Modbus, los «Holding Registers» son: a) bits de sólo lectura; b) bits de lectura y escritura;
   c) palabras de 16 bits de sólo lectura; d) palabras de 16 bits de lectura y escritura. **d**.
   Tema 2.2 — entera.
6. La ventaja de la señal 4-20 mA frente a 0-10 V es que: a) es más barata; b) un cable cortado da
   una lectura imposible y se detecta; c) no necesita cable; d) mide resistencia. **b**. Tema 3.2 —
   entera.
7. Cuando las señales de protección contra incendios se transmiten a un sistema integrado, según el
   RIPCI: a) las gestiona el BMS; b) tienen nivel de prioridad máximo; c) se desactivan en
   mantenimiento; d) se rearman a distancia. **b**. Tema 1.1 y 4.2 — entera.
8. El RITE exige un dispositivo que registre el número de arrancadas en: a) bombas de más de 20 kW;
   b) generadores de calor de más de 70 kW; c) compresores frigoríficos de más de 70 kW; d)
   ventiladores de más de 5 m³/s. **c**. Tema 5.1 — entera.
9. El seguimiento de la evolución del consumo en instalaciones de más de 70 kW se conserva al menos:
   a) un año; b) tres años; c) cinco años; d) diez años. **c**. Tema 5.2 — entera.
10. (Aplicación práctica) Al llegar al edificio, el técnico ve una alarma en la pantalla del sistema
    de control centralizado. Según la guía del IDAE debe: a) reconocerla y seguir con el preventivo;
    b) comprobar el elemento emisor, actuar hasta normalizar y anotarlo en el registro diario de
    incidencias, y después hacer el preventivo; c) rearmar desde el puesto central; d) esperar a que
    desaparezca. **b**. Tema 7.2 y 7.3 — entera.

Cobertura de rúbricas: BMS/SCADA (1, 2, 3, 5), sensores (6), alarmas (7), históricos (8, 9),
telemedida (4), actuación ante avisos (10). Las diez se contestan enteras con el tema; no ha hecho
falta ampliar.
