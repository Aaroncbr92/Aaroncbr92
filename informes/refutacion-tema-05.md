# Refutación del tema 5 del general

III Convenio Colectivo de la Corporación RTVE. Es el primer tema que **no se apoya en
legislación consolidada**, así que antes de refutar nada hubo que construir la fuente.

## 0 · La fuente no existía — y tenía un documento más de los que creíamos

El BOE **no publica texto refundido de los convenios colectivos**: hay documentos sueltos y
la redacción en vigor hay que reconstruirla superponiéndolos. `boe.py`, que trabaja contra
la API de legislación consolidada, no sirve aquí.

**Y los documentos anteriores al corte no eran tres, sino cuatro.** Al cerrar el tema se
consultó el bloque de «referencias posteriores» de la ficha del convenio en el BOE —el
sitio donde el propio BOE lista quién ha modificado qué— y apareció un documento que no
teníamos: la **Resolución de 15 de abril de 2021 (BOE-A-2021-8252, BOE de 18/05/2021)**,
que **sustituye entero el anexo 7**. La corrección de errores de enero de 2021 había
publicado como anexo 7 una «tabla de factores personales y de arraigo para valoración
curricular»; el acuerdo de abril la reemplaza por el **baremo de los criterios de
enfermedad, discapacidad o dependencia y de agrupación familiar** del artículo 14.3. **La
vigente a la fecha de corte es la segunda.**

No aparecía buscando «corrección de errores» del convenio, porque no lo es: es un acuerdo
de modificación. Descargado, transcrito y añadido a la trazabilidad. Los dos documentos de
2021 **no tocan el articulado**, así que el volcado reconstruido no cambia.

Con él llegó también la lista de lo posterior al corte, anotada como nota de actualización
en el tema: **BOE-A-2023-9620** (corrige un error material del anexo 3), **BOE-A-2023-17840**
(arts. 42, 50, 52, 57, 72 y 91, DT tercera y novena, DF primera), **BOE-A-2024-4470** (arts.
13, 18, 21 y 99.3 y 4, anexo 1, DT octava, DF primera) y **BOE-A-2025-24095** (capítulo III
entero, arts. 102 y 104.5, anexos 7 y 8, y dos disposiciones transitorias nuevas). El de
2023 toca cinco de los artículos más preguntados de los capítulos VI y VII, de modo que
**cualquier material de estudio posterior a agosto de 2023 dará cifras que no son las del
examen**.

Se escribió `herramientas/convenio_dump.py`, que genera `fuentes/convenio/CONVENIO.md`
con la forma que esperan las lentes (`## [id] Artículo N`), tomando de 2022 los artículos
que ese acuerdo reescribió y de 2020 el resto, y dejando en cada artículo constancia de
**de qué documento viene su redacción**.

**Primer aviso.** El volcado salió con **116 artículos y ninguno con redacción de 2022**.
No era que el acuerdo no modificase nada: el fichero de 2022 trae **espacio duro y «em
space»** dentro de los rótulos (`Artículo\xa063. Retribuciones`), y el patrón no
encontraba ni un artículo. Corregido —normalizando los espacios—, el volcado sustituye
exactamente los **diez artículos** que el acuerdo reescribe: **12, 13, 16, 17, 18, 21, 27,
30, 63 y 102**. Coincide con lo que el tema afirma, que era el objeto de la comprobación.

El volcado se corta antes del anexo 1 a propósito: **el anexo 4 vuelve a numerar desde el
artículo 1**, y mezclarlo haría contrastar negritas contra el artículo equivocado, que es
peor que no contrastar nada.

## 1 · Lente de exactitud

**462 negritas contrastadas** contra el articulado; 270 no literales, casi todas
paráfrasis y rótulos propios. Para no despachar 270 líneas «a ojo» se hicieron dos
barridos automáticos sobre ellas:

- **Toda negrita con cifra**, contra la cifra en su artículo: **29 salieron sin
  coincidencia y las 29 eran el número del propio artículo en su rótulo** o una
  referencia externa. Es decir: **ningún dato numérico del tema está inventado**.
- **Negritas con menos del 60 % de sus palabras en el artículo**: **12**, todas rótulos o
  comentario propio salvo una.

Esa una era un error de verdad.

### Hallazgo 1 · Período de prueba (art. 32) — corregido

El tema decía **«tres meses para cualquier tipo de contrato, salvo los de duración
incierta»**. El artículo 32 no dice eso:

> Las contrataciones con duración superior a seis meses podrán hacerse a título de prueba
> por un período máximo de trabajo efectivo de **tres meses**. Las contrataciones con
> duración igual o inferior a seis meses, así como las de duración incierta (interinos o
> por obra o servicio), podrán hacerse a título de prueba por un período máximo de trabajo
> efectivo de **un mes**.

No hay un plazo único: hay **dos, y el criterio es la duración del contrato**. Reescrito,
con el resto del artículo (extinción sin preaviso ni indemnización, informe del mando en
siete días naturales, cómputo a todos los efectos una vez superado). **El banco pregunta
justamente por el tramo de más de seis meses**, así que el error habría costado la
pregunta.

## 2 · Lente de modo verbal y salvedades

La primera pasada dio 11 hallazgos, pero **la lente estaba mirando menos de lo que
parecía**. Dos puntos ciegos, los dos del apartado 10 del manual:

- **No reconocía la abreviatura.** El tema escribe `**Art. 104.**` tanto como
  `### Artículo 104`. Con solo la forma larga, los artículos abreviados **no abrían
  bloque**: sus negritas se contrastaban contra el artículo anterior. Los artículos **104
  a 107 y 109 a 116 nunca se comprobaron** en la primera pasada, y las negritas del 103
  arrastraban las de los cuatro siguientes.
- **De un rótulo de rango solo leía el primer número.** «Artículos 53 a 56» se comprobaba
  contra el 53 y nada más.

Corregidas ambas cosas aparecieron **cinco hallazgos que antes eran invisibles** (arts. 7,
105, 107, 108 y 116). Al arreglarlo hizo falta un tercer ajuste: comparar un bloque de
rango **contra la unión** de esos artículos, no contra cada uno por separado, porque lo
que el tema dice del primero salía marcado como error contra los demás.

### Hallazgos reales, todos corregidos

| Art. | Qué faltaba |
|---|---|
| **2** | La entrada en vigor es **sin perjuicio de la DA 3.ª y la DF 1.ª** |
| **7** | La ordenación del trabajo es facultad exclusiva **«sin perjuicio de los derechos y atribuciones reconocidos en la legislación vigente a las personas que trabajan y a su representación legal»**. Sin esa coletilla el poder de dirección quedaba como ilimitado |
| **12** | «Sin perjuicio de lo establecido en el Estatuto de los Trabajadores» |
| **47 y 48** | El tema decía que el mando orgánico **«puede»** hacer jornadas superiores a la base. La norma dice **«deberán»**: es obligación, no facultad. **Error 4 del catálogo** |
| **50** | Las modificaciones de turno se comunican la última semana del mes anterior **«salvo casos puntuales derivados de bajas o ausencias no previstas»** |
| **60** | Una vez asignados, **no pueden variarse los turnos de vacaciones salvo necesidades ineludibles o circunstancias especiales justificadas** |
| **80** | Los hechos probados vinculan a RTVE **«sin perjuicio de la responsabilidad en que la persona trabajadora haya incurrido»** |
| **96** | La prórroga de la suspensión por violencia de género va precedida de la salvedad de la tutela judicial |
| **105** | Si no se pide el reingreso en 30 días **se causa baja definitiva, salvo que en ese plazo se solicite excedencia voluntaria** |
| **107** | **Sin perjuicio del artículo 21 ET** (pacto de no concurrencia y de permanencia) |
| **108 y 116** | «**A excepción del** personal de alta dirección», que el tema daba como «se excluye» |

Quedan **tres hallazgos que son de la lente, no del tema**: los «no obstante» de los
artículos 41 y 42, cuyo contenido el tema sí desarrolla, y la palabra «facultad» en los
artículos 47 y 48, que aparece precisamente en la frase que advierte de que **no** es una
facultad.

## 3 · Lente de prosa

Cero relleno y cero frases repetidas. **Ocho siglas sin presentar** —ET, RLT, CGSSL, CSSL,
AGE, PGE, DT y la Dirección General de Trabajo—, todas desarrolladas ya en su primera
aparición. Quedan cuatro avisos que son ruido del detector: API, DNI, SA y el «NO» de una
casilla de tabla.

## 4 · El arreglo obligó a repasar lo ya cerrado

Corolario del apartado 10: al arreglar una herramienta hay que volver sobre todo lo que
pasó por ella cuando estaba rota.

- **Tema 4**: sigue en **cero hallazgos**.
- **Tema 2**: aparece **un hallazgo nuevo** y era real. El tema resumía los artículos 35 y
  36 diciendo «presentación consolidada de presupuestos y programas», sin recoger que el
  artículo 36 empieza con **«Sin perjuicio de lo establecido anteriormente… presentará
  además»**. La presentación consolidada **no sustituye a la individual: se suma a ella**.
  Corregido. Vuelve a cero.
- **Tema 1**: tres hallazgos, los tres falsos positivos de bloque. El «ha de ser veraz»
  del artículo 20 es una reformulación correcta de «información veraz»; el «no obstante»
  del 75 está desarrollado con otras palabras («el Pleno puede recabar en cualquier
  momento»); y el «obligatorio» que se le imputa al 169 sale de la **tabla comparativa de
  los artículos 167 y 168** que va a continuación, donde el referéndum del procedimiento
  agravado sí es obligatorio. No se toca nada.
- **Tema 3**: la lente devuelve **«0 comprobadas, 0 no literales»**, que **no es un
  aprobado, es una comprobación que no miró nada**. La Ley 5/2017 tiene **«Artículo
  único»**, sin numeración, y el tema cita artículos **de la Ley 17/2006**, que es otra
  norma: la lente por artículo no puede aplicarse aquí. Se verificó **a mano y con un
  contraste de negritas contra el texto completo** de la ley: 109 negritas de dos o más
  palabras, 66 no literales, todas comentario propio o variantes de redacción
  («apartado 1 del artículo 12» ↔ «artículo 12.1»; «no será renovable» ↔ «no renovable»).
  Comprobados uno a uno los datos con cifra —diez años de experiencia, cuatro miembros,
  la mitad de los grupos parlamentarios, dos tercios, audiencia pública, el tiempo que
  reste del mandato— **todos correctos**. Y se verificó además la única afirmación del
  tema que no podía contrastarse contra esa ley: que el antiguo **art. 11.5** (no
  elegibilidad de los cesados del art. 13) **desapareció** con el RDL 5/2024. Es cierto:
  el artículo 11 vigente tiene **cuatro apartados** y ninguno de inelegibilidad.

## 5 · Lo que apareció al transcribir los anexos 1 y 2

Los anexos 1 y 2 se habían dejado sin transcribir por ser importes. Al hacerlo salieron dos
cosas.

**Un error propio, corregido.** La primera lectura de la tabla de salario base dio por
**constante** el escalón entre niveles y así se escribió: «diecisiete saltos iguales». No
lo es. Comprobados los diecisiete restando uno a uno, **dieciséis miden unos 68,31 € y el
de D2 a D1 mide 57,91 €**. Ampliada la imagen sobre esas dos filas para descartar un error
de lectura, los importes son los que se habían transcrito: la irregularidad es del
convenio, no de la transcripción. Y cae justo en **D1, el nivel básico del Grupo I ·
Subgrupo I**. Es la clase de afirmación redonda que se cuela por parecer elegante.

**Un hueco del propio tema.** El artículo 14.3 describía el baremo de traslados con **dos**
criterios —antigüedad (35 puntos) y enfermedad (12)— cuando tiene **tres**: falta
**agrupación familiar, 8 puntos**. Faltaban también el desempate **por sexo menos
representado**, el plazo máximo de **ocho meses** para incorporarse y que **una vez
adjudicada la plaza no cabe renunciar a ella**. Añadido todo, y añadido el **anexo 7**, que
es precisamente donde el convenio detalla los baremos de esas letras b) y c) y que hasta
ahora figuraba en el tema con el contenido equivocado.

## Resumen

| | Hallazgos | Estado |
|---|---|---|
| Exactitud | **1** (art. 32) | corregido |
| Documento de fuente que faltaba | **1** (BOE-A-2021-8252, anexo 7) | descargado e incorporado |
| Huecos hallados al transcribir los anexos | **2** (art. 14.3 incompleto; escalón salarial dado por constante) | corregidos |
| Modo verbal y salvedades | **11** | corregidos |
| Prosa | **8** siglas | corregidas |
| Falsos positivos identificados | 3 en el tema 5, 3 en el tema 1 | documentados, no se toca el texto |
| Efecto retroactivo | 1 hallazgo real en el tema 2 | corregido |

Herramientas modificadas fuera del tema: `herramientas/refutar_exactitud.py`,
`herramientas/refutar_modo.py` y la nueva `herramientas/convenio_dump.py`.
