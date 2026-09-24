# T01 · Refutación (fase 4, modo ahorro) · Constitución Española de 1978

Tema: `temas/canal-sur-comun/01-constitucion-espanola.md` (3.286 líneas), en el estado que dejó
la verificación. Esta fase no lo corrige. Leídos antes: `ENCARGO.md`, `CICLO.md` (avisos y los
dos modos ahorro) y `T01-verificacion.md`.

Un solo agente y **una sola lectura del tema**, de la línea 1 a la 3.286, con las dos lentes a
la vez. **Fecha de lectura de todos los preceptos: 24-09-2026**, en la redacción vigente ese día
(volcados de `fuentes/canal-sur/`, extraído sólo el precepto comprobado).

**Resultado: 0 hallazgos que cambien la respuesta, 2 que inducen a error y 3 menores.**

---

## 1. Exactitud normativa

### 1.1. Qué se comprobó y está bien (una línea por bloque)

Me centré en lo que la verificación no cotejó de forma mecánica. Las tablas del 148.1 y del
149.1 y las cuatro reformas no las volví a cotejar.

| Bloque | Comprobado contra la fuente | Resultado |
| --- | --- | --- |
| Identificación y disposiciones | DT 3.ª, 6.ª, 7.ª, 8.ª y 9.ª; recuentos (169 arts., 11 títulos, 15 disposiciones, 46 arts. del Título I, 4 del X) | Bien |
| Rúbrica a) | 9.3, 14 (cinco causas), 17, 20, 27 (diez apartados), 53, 55.1-2, 116, 166-169, 135 | Bien |
| Rúbrica b) | 59-60, 64, 70, 71, 74.2, 75.3 (cinco materias), 78, 90, 99, 102.2, 113, 122.3, 159-162; cuadros de nombramientos, de funciones y de mayorías | Bien |
| LO 2/1982 (a mano: la lente no ve «Artículo treinta») | Arts. primero, segundo, cuarto (seis entes), noveno, diez (seis meses), doce, quince, diecinueve (ocho órganos), veintiuno (dos tercios), veintinueve, treinta (6+6, tres quintos, nueve años, 40 %), treinta y tres, treinta y cinco; redacciones de la LO 3/2015 y la LO 2/2024 en el `.redacciones.tsv` | Bien |
| LO 3/1981 (a mano) | Arts. primero, segundo (tres quintos, veinte días, un mes, mayoría absoluta del Senado), tercero, cuarto, quinto (cinco causas y quién declara la vacante), sexto, séptimo, octavo, diez, once, quince, diecisiete, veintiocho, veintinueve, treinta y dos; cambios de la LO 2/1992 sólo en 2, 10, 22 y 24 | Bien |
| Rúbrica c) | 137-147, 151-158; EAA 1, 2, 4, 42, 60, 89-98, 108; LBRL 4, 20-23, 26.1, 27, 32-37, 121, 128; LAULA 3, 5, 6, 8, 9, 11-15, 57, 89, 91, 93 | Bien, salvo E1, E3 y E4 |

### 1.2. Lentes automáticas (tema entero)

| Lente | Tramos | Resultado | Explicación |
| --- | --- | --- | --- |
| `refutar_prosa.py` | tema entero | 0 | — |
| `refutar_exactitud.py` (CE, EAA, LBRL, LAULA, LO 2/1982, LO 3/1981 y las seis modificadoras) | 565 negritas por bloque; 143 por paréntesis (3 sin comprobar) | 8 + 9 | Los mismos 17 falsos positivos de atribución que explica la verificación (apartado 2). Sin novedades |
| `refutar_modo.py` con la CE | tema entero | 3 | Los mismos 3 falsos positivos de la verificación (168.3 «obligatorio», 161.2 «debe», 20.1.d «ha de ser veraz») |

Las negritas de la LO 2/1982 y la LO 3/1981 las cotejé a mano (cuadro de arriba): todas literales.

### 1.3. Hallazgos de exactitud

**E1 · Art. 150.3, línea 2554-2555 · induce a error (error 9)**

- Qué dice: «Las materias que se armonizan son de competencia autonómica.»
- Fuente: art. 150.3 CE: «**El Estado podrá dictar leyes que establezcan los principios
  necesarios para armonizar las disposiciones normativas de las Comunidades Autónomas, aun en el
  caso de materias atribuidas a la competencia de éstas**, cuando así lo exija el interés
  general.» El «aun» incluye las materias autonómicas, pero no dice que sean las únicas. La tabla
  de la línea 2561 lo dice bien («aun en materias de competencia de las Comunidades»).
- Qué debería decir: «Pueden armonizarse las disposiciones autonómicas "aun en el caso de
  materias atribuidas a la competencia de éstas".» O quitar la frase.

**E2 · Sección 2.ª y objeción de conciencia, líneas 680-682 · induce a error**

- Qué dice: a la Sección 2.ª «no [le alcanza] el procedimiento preferente y sumario ni el amparo
  del 53.2, salvo la objeción de conciencia del artículo 30».
- El problema: la salvedad parece cubrir las dos garantías. El 53.2 extiende a la objeción sólo el
  amparo: «**Este último recurso será aplicable a la objeción de conciencia reconocida en el
  artículo 30.**» Las líneas 695-696 y el cuadro (línea 838) lo dicen bien, pero una pregunta
  sobre el procedimiento preferente y sumario puede tropezar aquí.
- Qué debería decir: «…pero no el procedimiento preferente y sumario ni el amparo del 53.2; el
  amparo, no el procedimiento preferente, se extiende a la objeción de conciencia del artículo 30».

**E3 · EAA 42.2.3.º, líneas 2575-2577 · menor (error 6)**

- Qué dice: la competencia ejecutiva comprende «la función ejecutiva, que incluye la potestad de
  organización de su propia administración y, cuando proceda, la aprobación de disposiciones
  reglamentarias para ejecutar la normativa del Estado».
- Qué falta, en medio: «**y, en general, aquellas funciones y actividades que el ordenamiento
  atribuye a la Administración Pública**» (EAA 42.2.3.º).
- Qué debería decir: añadir ese inciso en su sitio.

**E4 · EAA 60.1.c) y d), líneas 2651-2654 · menor (error 6)**

- Qué dice: «régimen de los bienes y modalidades de prestación de los servicios públicos;
  órganos de gobierno de los entes locales creados por la Junta».
- Fuente: c) «**El régimen de los bienes de dominio público, comunales y patrimoniales** y las
  modalidades de prestación de los servicios públicos»; d) «La determinación de los órganos de
  gobierno de los entes locales creados por la Junta de Andalucía, **el funcionamiento y el
  régimen de adopción de acuerdos de todos estos órganos y de las relaciones entre ellos**».
  La d) no se ciñe a los órganos de los entes que crea la Junta: el funcionamiento y el régimen
  de acuerdos alcanzan a «todos estos órganos».
- Qué debería decir: completar las dos letras con lo destacado.

**E5 · LAULA 11.1, línea 3169 · menor (error 4, modo verbal)**

- Qué dice: «La provincia presta a los municipios asistencia de tres tipos».
- Fuente: art. 11.1 LAULA: las competencias de asistencia «**podrán consistir en**» asistencia
  técnica, económica y material.
- Qué debería decir: «La asistencia de la provincia a los municipios puede ser de tres tipos
  (artículo 11.1)».

---

## 2. Cobertura y forma

### 2.1. ¿Da cada rúbrica lo que anuncia?

- **a)** Sí: valores (1.1), «principios inspiradores» (se explica que la expresión no está en la
  CE y se dan 9.3, 10.1, 31.1 y 132.1), Estado social y democrático de Derecho, Título I entero,
  principios rectores, garantías (53-54), suspensión (55 y 116) y reforma (166-169 y las cuatro
  reformas).
- **b)** Sí: todos los órganos del enunciado, con la Constitución y las dos leyes orgánicas.
- **c)** Sí: Título VIII, vías de acceso, Estatutos, 148-150, EAA 42, organización territorial
  de Andalucía (EAA 89-98 y LAULA), municipio y provincia (LBRL, EAA y LAULA). Lo que remite al
  punto 2 está declarado en «Lo que este tema no da».

### 2.2. Las quince preguntas

Están en `informes/canal-sur-comun/T01-preguntas.md`, cinco por rúbrica, con la respuesta
comprobada en la fuente. Contestadas sólo con el cuerpo del tema:
**15 enteras, 0 a medias, 0 no**. Ninguna laguna de cobertura.

### 2.3. Prosa

`refutar_prosa.py` da 0. En la lectura no vi antecedentes rotos, siglas sin presentar ni
referencias a ficheros del proyecto (grep de `fuentes/`, `.md`, `herramientas`). Sin hallazgos.

---

## 3. Otros ficheros tocados

- `informes/canal-sur-comun/T01-preguntas.md` (nuevo).
- Este informe. No he tocado el tema, las fuentes ni las herramientas.
