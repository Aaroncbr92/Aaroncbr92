# Refutación del tema 3 del específico de Información y Contenidos

**Siglas de este informe**: Centro de Investigaciones Sociológicas (**CIS**); Consejo Superior de
Investigaciones Científicas (**CSIC**); ahí sale un error del examen— y la Organización para la
Cooperación y el Desarrollo Económicos (**OCDE**); Organismo Internacional de Energía Atómica
(**OIEA**).

**Veintiuna preguntas y trece documentos del BOE detrás.** A diferencia de los temas 1 y 2, aquí sí
hay articulado: la Constitución, el Estatuto de Roma, el Convenio de Estambul, el Estatuto de
Autonomía para Andalucía. Pero **el tema no desarrolla ninguna de esas normas**: cita **un artículo
de cada una**. Las lentes por artículo siguen sin servir, y por la misma razón de siempre: trocean el
tema por artículos y este tema está troceado por instituciones.

Se corrieron **la de documento y la de prosa**, más **la comprobación de citas** que el proyecto
adoptó en el tema 1.

## Lente de documento

Contra las fuentes reunidas: **262 negritas comprobadas**, **175 no literales** y **cero cifras
huérfanas**.

**Las huérfanas empezaron siendo tres, y las tres eran reales**:

| Cifra | Dónde | Qué pasaba |
|---|---|---|
| **184** | «RD 184/2024» | El real decreto de **cese** del Jefe de la Casa del Rey se citaba **sin haberlo descargado**: salía en el listado del buscador, al lado del de nombramiento |
| **585** | «RD 585/2024» | Lo mismo con el cese del lehendakari anterior |
| **140** | «artículo 140» | El artículo del Estatuto de Andalucía se citaba **por lo que no dice**, y **lo que no dice tampoco estaba en el corpus** |

**Los tres se arreglaron descargando lo que faltaba**, y el tercero enseña una regla que el proyecto
no tenía escrita: **citar una norma por lo que no dice exige tenerla igual que citarla por lo que
dice**. Si el tema afirma que el artículo 140 no fija la sede, el lector tiene que poder comprobar
que, en efecto, no la fija. **Un descarte sin fuente es una afirmación sin fuente.**

## Lente de prosa

**Cero hallazgos**, después de añadir a la cabecera dos siglas que la primera pasada señaló:
**CSIC** —que aparece precisamente para distinguirlo del CIS— y **OCDE**, que sale al explicar por
qué París es un distractor bueno para la sede del OIEA.

## La comprobación de las citas

**Quince bloques de cita y las citas en línea**, comprobados uno a uno contra el texto completo de
las fuentes. **Los quince bloques, literales a la primera.**

**Las citas en línea dieron tres fallos, los tres del mismo caso**: los tres pasajes del Estatuto del
OIEA que el tema cita **por lo que no dicen** —«en la sede del Organismo», «el lugar en que se
establecerá la sede permanente del Organismo» y «un acuerdo sobre la sede»— **no estaban en ninguna
fuente guardada**, por lo mismo que el artículo 140. Se guardaron los cuatro pasajes del Estatuto en
que aparece la palabra, con la advertencia en la cabecera del fichero.

## Los tres hallazgos de este tema

### 1. El enunciado del CIS está mal, y lo encontró la fuente

**El examen dice «Centro de Investigaciones Científicas (CIS)».** El CIS es el **Centro de
Investigaciones Sociológicas**; el de Investigaciones Científicas es el **CSIC**, y es otro organismo
con otra adscripción.

**No lo encontró una relectura: lo encontró buscar la expresión del enunciado en el real decreto de
estructura y no hallarla.** De ahí sale una regla operativa: **cuando una fuente buena no encuentra
lo que el enunciado nombra, lo primero que hay que sospechar es del enunciado.**

**No cambia la respuesta** —las siglas sólo pueden ser el Sociológico— y va anotado como enunciado
defectuoso.

### 2. Dos normas citadas por lo que no dicen

**El Estatuto del OIEA no fija la sede del Organismo**: la menciona cinco veces y encarga a la
Comisión Preparatoria recomendar dónde estará. **Ni el Estatuto de Andalucía ni la ley de planta
fijan la sede del Tribunal Superior de Justicia**; la ley sólo reparte **las Salas** entre Sevilla,
Granada y Málaga.

**Las dos preguntas se marcan como apoyadas en la plantilla, pero no como lagunas de búsqueda.** La
diferencia importa: *no se encontró* y *se encontró la norma y la norma no lo dice* son dos cosas
distintas, y sólo la segunda es un resultado.

**En el segundo caso, además, el descarte es parcialmente útil**: ni Ceuta ni Melilla aparecen como
sede de nada, así que la ley de planta **elimina dos de las cuatro opciones** del examen.

### 3. El Convenio de Estambul dice «violación», no «grave violación»

El enunciado pregunta «¿qué documento recoge que la violencia contra las mujeres es una **grave**
violación de los Derechos Humanos?». El artículo 3.a) del convenio dice «**una violación de los
derechos humanos y una forma de discriminación contra las mujeres**», **sin adjetivo**.

**No cambia la respuesta** y no se corrige el enunciado, pero **el tema cita el convenio como está**
y advierte de que el adjetivo lo pone el examen. Es el mismo criterio del tema 2 con las dos palabras
que le faltaban a una cita: **una cita que dice lo mismo con otras palabras sigue siendo una cita
falsa**.

## Una precisión de trazabilidad que la herramienta regala

**El artículo 5 del Estatuto de Roma que se lee hoy no es el original.** Al volcarlo, `boe.py`
imprime la cadena de redacciones y dice que la vigente es de **2015**, publicada en 2014 por
`BOE-A-2014-13411`, y que **su apartado 2 está suprimido**. Ese apartado era el que aplazaba el
ejercicio de la competencia sobre el crimen de agresión.

**El tema estudia la redacción vigente y lo dice.** Sin la herramienta, la lista de cuatro crímenes
se habría citado como si estuviera ahí desde 1998, que es justo la clase de error que el apartado 2
del manual describe.

## Lo que queda sin comprobar, y por qué

**Cinco preguntas**, con el detalle en el informe de cobertura. **El patrón de este tema es distinto
del de los anteriores**: aquí no falla el acceso a las fuentes españolas —el BOE responde a todo—
sino que **las preguntas caen fuera del corpus español**: un tratado del que España no es parte
(MERCOSUR), dos organismos cuyas páginas bloquean la consulta automática (UNRWA y el Consejo de
Europa) y un cargo que **no se nombra por real decreto** (la Presidencia del Congreso).

**Ninguna de esas cinco es un fallo de búsqueda**, y las dos que se marcan a pesar de tener la norma
delante lo llevan explicado.
