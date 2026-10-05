# Redacción · Oficial Técnico Electricista (27) · Tema 15 · Trabajos en instalaciones eléctricas

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/15-trabajos-en-instalaciones-electricas.md`
(15.656 palabras según `indice.py`, contando tablas; 38 epígrafes). Material: `27-investigacion-A-electrico.md`
§8, §9.8 y §10. Reuso RTVE según `informes/canal-sur-reuso/tecnica.tsv`: `teitse/14` y `general/08` (75 %,
actualizar: **sí**). Fecha declarada: 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»; el
RD 614/2001 tiene una sola redacción desde 2001). Lentes corridas: `indice.py` (índice generado),
`refutar_prosa.py` (0 hallazgos), `negritas.py` contra RD 614/2001, guía INSST, LPRL, RD 171/2004, RSP y
REBT (343 negritas; las «NO ESTÁ» se explican en el aviso 8).

Ficheros tocados: el tema (nuevo) y este informe. Fichero temporal en el scratchpad (no en el repositorio).

## Estructura

1 Trabajos en instalaciones eléctricas (ámbito, definiciones, art. 4 y sus excepciones, personal, formación);
2 Consignación (término de oficio, identificación previa, todas las fuentes de un edificio audiovisual,
reposición); 3 Cinco reglas de oro (texto, etapa por etapa con la guía, orden, secuencia de puesta a tierra en
BT, anexo II.B); 4 Trabajos en tensión o proximidad (zonas y tabla 1 completa, anexos III, IV, V y VI, cuadro
de decisión); 5 Permisos de trabajo (lo que exige la norma, lo que recomienda la guía, el permiso como oficio
declarado); 6 Coordinación de actividades empresariales (art. 24 LPRL, RD 171/2004, recursos preventivos y
aplicación al riesgo eléctrico); normativa; lo que no da; trazabilidad.

## Fuentes leídas por el redactor (05-10-2026)

- RD 614/2001 (`fuentes/canal-sur/BOE-A-2001-11881.md`, volcado 25-09-2026, una redacción en todos sus bloques
  según `.redacciones.tsv`): artículos 1 a 6, dd, df 1.ª a 3.ª, anexos I a VI enteros. Es la norma del tema;
  por eso se leyó entera (7.859 palabras).
- Guía técnica INSST 2020 (`fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.txt`): comentarios al
  art. 4 (líneas 800-930), anexo I def. 13-15 (1060-1075, 1690-1730), anexo II (1870-2440, 2875-2975,
  3040-3120), anexo III.A.6 (4130-4145), anexo V (4850-4935). Cotejo literal de cada cita con un script de
  normalización (quita guiones blandos U+00AD y saltos de página): todas casan.
- RSP art. 22 bis.8 (`BOE-A-1997-1853.md`, línea 363 y letra f): sólo para la frase añadida en 6.5.
- REBT: título de la ITC-BT-29.
- No he leído `temas/general/08-ley-31-1995.md`: la investigación (§8) y el encargo («si el tema pide una norma
  que el común ya desarrolla, se toma su texto literal») mandan usar el común de Canal Sur, que ya pasó el ciclo.

## Avisos para el verificador

1. **Errores de RTVE (teitse/14) que no se han copiado** (cotejados con el anexo II y el anexo I):
   - RTVE dice que la etapa 3 se hace «con un detector comprobado antes y después» sin distinguir: la norma lo
     exige **sólo en AT**; en BT la guía lo recomienda. Corregido en 3.2 (error 6, salvedad omitida).
   - RTVE define el trabajador cualificado sin decir que es un **autorizado**; y el jefe de trabajo como «la
     persona designada para asumir la dirección y vigilancia», cuando la definición 15 dice «**responsabilidad
     efectiva de los trabajos**» (dirección y vigilancia es del III.B.1). Corregido en 1.4 (error 9).
   - RTVE no da la tabla 1 («una cifra que no se ha leído no se escribe»): ahora se ha leído y se da entera.
   - RTVE: «La etapa 4 es la que se salta en baja tensión»: sustituido por el literal del apartado 4 b) y la
     guía (sólo obligatoria en BT si puede ponerse accidentalmente en tensión).
2. **Lo propio de RTVE quitado**: referencias al punto 17, a los temas 8 y 9 de RTVE, «este proyecto», «la
   ocupación», la apertura retórica, las tablas sin fuente de efectos de la corriente (no pedidas por el
   enunciado; van al tema 19) y la tabla de EPI de oficio.
3. «Consignación» y «cinco reglas de oro» no son términos de la norma; la guía usa el segundo («conocido
   habitualmente como “las cinco reglas de oro”») y no usa el primero (confirmado por grep). Declarado en 2.1 y 3.1.
4. **Permisos de trabajo**: el RD no regula un permiso con ese nombre. 5.1 recoge sólo preceptos; 5.2 sólo la
   guía; 5.3 se declara oficio entero (hueco declarado en la investigación §9.8: no hay modelo oficial).
5. 3.5: el anexo II.B.4 se rubrica «en alta tensión»; la extensión a alternadores de grupos de BT se declara
   oficio. El tiempo de descarga de condensadores no lo fija la norma (dicho).
6. 4.4: «salas de control» del V.B.1.1 se lee con cautela: se dice que la norma no las identifica con las de
   producción.
7. 1.3: el criterio de «la opción que entrañe el menor riesgo» es de la guía (comentario al 4.4 b), atribuido a ella.
8. `negritas.py`: las «NO ESTÁ» de citas de la guía son falsos negativos por guiones blandos y saltos de página
   (comprobadas con el script del punto de fuentes); las de 6.1 a 6.5 son del texto copiado (LPRL/RD 171/2004,
   cuyos volcados el script lee con otro formato); «Enunciado del programa» y «Qué se puede preguntar» son
   rótulos de forma, como en T07 y T11. Los rótulos propios se pasaron a cursiva.
9. «¿ART. 3? Las técnicas y procedimientos…» → es cita del art. 2.2 b) y así se presenta («El 2.2 reparte…»):
   falso positivo.

## Copiado del común

No se re-verifica (ya pasó el ciclo con redacción vigente). Rótulos `###` renumerados (6.1 a 6.5) para encajar
en el tema; el cuerpo es literal salvo lo señalado.

- **6.1 «El artículo 24 de la LPRL»**: literal del tema 9 del común de Canal Sur (`temas/canal-sur-comun/09-ley-31-1995.md`,
  epígrafe «Artículo 24. Coordinación de actividades empresariales», cuerpo entero).
- **6.2 a 6.5**: literal del tema 14 del específico de Productor/a, cerrado
  (`temas/canal-sur-especificos/32-productor-a/14-prevencion-de-riesgos-laborales-en-la-produccion-audiovisual.md`,
  epígrafes «El RD 171/2004: definiciones y objetivos», «Tres situaciones, tres grados de obligación», «Los
  medios de coordinación y la persona coordinadora» y «Los recursos preventivos»), **salvo estos pasajes
  adaptados, que sí deben verificarse**:
  - 6.2, última frase: «La letra c) es el caso típico de una sala técnica en obras: una empresa que corta o
    suelda mientras el electricista trabaja en un cuadro.» (sustituye al ejemplo del plató).
  - 6.4, párrafo «Que la RTVA o CSRTV designen como personas coordinadoras a su personal técnico de
    mantenimiento no consta…» (sustituye al párrafo sobre el productor).
  - 6.5, frase «Son cinco. En el mantenimiento de un edificio técnico pueden darse la primera … y la cuarta
    (espacios confinados)…» (sustituye a la de la parrilla); «si el trabajo lo hace una contratista» (era «el
    montaje»); frase nueva tras el 22 bis.8: «Para el riesgo eléctrico rige, pues, el Real Decreto 614/2001 en
    sus propios términos…»; último párrafo: «una intervención con varias empresas a la vez» y «en los trabajos
    de mantenimiento de la RTVA o de CSRTV».
- No se copió la tabla «Aplicado a la producción» del 32-T14; en su lugar va 6.6, nuevo.
- Observación (no tocado): en el común, 24.1 deja en redonda «la información a sus respectivos trabajadores en
  los términos del artículo 18.1», que es paráfrasis; correcto según la convención.

## Copiado de RTVE sin cambios

Nada. Los dos temas de RTVE de este reuso están marcados «actualizar: sí» (no «sin actualizar») y todo lo que
podía tomarse de ellos cita norma. `general/08` no se usó (lo sustituye el común). De `teitse/14` se
aprovecharon, **adaptados y por tanto a verificar**: la cita del art. 1.1 y 1.2 (1.1), la del 3.1 resumida y el
inciso de la experiencia del explotador (1.1, ahora con el 3.3 literal), la cita del 4.2 (1.3), la tabla de las
dos listas de excepciones (1.3, rehecha con el literal del 4.3 y 4.4), la lectura del 4.4 b) en una casa que
emite (1.3, matizada con la guía), la cita de las cinco etapas (3.1, ahora con el párrafo final completo), las
observaciones sobre condensadores, detector y puesta a tierra (3.2, corregidas), el porqué del orden (3.3), la
reposición en orden inverso (2.4, ahora literal), la regla de «lo más largo que se mueva» (1.2, apoyada en las
definiciones 8 y 12) y la elección del 4.7 (1.3).

## Lo nuevo (pasa entero por el ciclo)

1.1 art. 2.1, 3.3, 3.4, df 1.ª; 1.2 entero; 1.3 art. 4.1, 4.3 b), 4.5-4.8, guía sobre 4.4 b); 1.4 definiciones
literales, guía, cuadro de quién hace qué; 1.5; 2 entero (salvo lo dicho de 2.4); 3.2 texto literal de cada
etapa y guía; 3.4 y 3.5 enteros; 4 entero (tabla 1, anexos III a VI, ejemplos, cuadro de decisión); 5 entero;
6 introducción y 6.6; normativa, lo que no da, trazabilidad.

## Comprobación con 10 preguntas tipo test

Contestadas sólo con el tema. Las diez, enteras; no ha hecho falta ampliar (antes de la prueba ya se había
añadido la tabla 1 completa, el cuadro de quién hace qué y 6.6, que la investigación marcaba como huecos de RTVE).

1. (Trabajos en instalaciones, teoría) Según el RD 614/2001, NO se consideran trabajos en tensión: a) los
   trabajos en proximidad; b) las maniobras y las mediciones, ensayos y verificaciones; c) los trabajos con
   tensiones de seguridad; d) la reposición de fusibles. → **b**. Tema 1.2 (definición 8). Entera.
2. (Consignación, teoría) Las operaciones para dejar sin tensión una instalación de AT y reponerla las hacen:
   a) trabajadores autorizados; b) trabajadores cualificados; c) el jefe de trabajo en persona; d) cualquier
   trabajador informado. → **b**. Tema 2.1 y 1.4 (anexo II.A). Entera.
3. (Consignación, práctica) Para trabajar sin tensión en un cuadro alimentado desde un conmutador red-grupo y
   con un SAI con bypass aguas arriba, la primera etapa exige: a) abrir el interruptor de red; b) aislar la
   parte de la instalación de todas las fuentes de alimentación (red, grupo, rectificador y bypass del SAI);
   c) parar el grupo; d) desconectar las baterías. → **b**. Tema 2.3 y 3.2 (etapa 1). Entera.
4. (Cinco reglas, teoría) La tercera de las cinco etapas del anexo II.A.1 es: a) poner a tierra y en
   cortocircuito; b) prevenir cualquier posible realimentación; c) verificar la ausencia de tensión; d)
   señalizar la zona. → **c**. Tema 3.1. Entera.
5. (Cinco reglas, teoría) La comprobación del correcto funcionamiento del verificador de ausencia de tensión
   antes y después de la verificación es: a) obligatoria en AT y BT; b) obligatoria en AT y recomendada por la
   guía del INSST en BT; c) sólo recomendada; d) obligatoria sólo en BT. → **b**. Tema 3.2. Entera.
6. (Cinco reglas, práctica) En BT, la puesta a tierra y en cortocircuito: a) es siempre obligatoria; b) nunca
   se exige; c) es obligatoria en instalaciones que, por inducción o por otras razones, puedan ponerse
   accidentalmente en tensión, y el equipo se conecta primero a la toma de tierra; d) se conecta primero a las
   fases. → **c**. Tema 3.2 (etapa 4) y 3.4. Entera.
7. (Tensión o proximidad, práctica) En una instalación de Un ≤ 1 kV donde no es posible delimitar con precisión
   la zona de trabajo, el límite exterior de la zona de proximidad está a: a) 50 cm; b) 70 cm; c) 112 cm;
   d) 300 cm. → **d**. Tema 4.1 (tabla 1). Entera. (Variante de cálculo: DPEL-1 a 25 kV = 77 cm, tema 4.1.)
8. (Tensión o proximidad, teoría) En un trabajo en proximidad, la vigilancia por un trabajador autorizado no
   es exigible: a) nunca; b) cuando los trabajos se realicen fuera de la zona de proximidad o en instalaciones
   de baja tensión; c) en AT; d) si el trabajador lleva EPI. → **b**. Tema 4.4 (V.A.2.2). Entera.
9. (Permisos de trabajo) Para trabajos en tensión en AT, la autorización escrita del trabajador cualificado
   debe renovarse cuando: a) cada año natural; b) cada cinco años; c) cambie significativamente el
   procedimiento o el trabajador haya dejado de hacer ese tipo de trabajo durante más de un año; d) cambie de
   centro. → **c**. Tema 4.2 y 5.1 (III.B.3). Entera.
10. (Coordinación, práctica) Un técnico autorizado de una empresa mantenedora necesita abrir un armario de
    distribución de BT en un centro de CSRTV. Según el RD 614/2001 y el RD 171/2004: a) basta con que esté
    autorizado por su empresa; b) necesita el conocimiento y permiso del titular de la instalación, y el
    titular debe informarle de los riesgos del centro y darle instrucciones; c) sólo si le vigila un
    cualificado de CSRTV; d) sólo con permiso de la ITSS. → **b**. Tema 4.4 (V.B.1.3), 6.2 a 6.3 (arts. 7 y
    8) y 6.6. Entera.
