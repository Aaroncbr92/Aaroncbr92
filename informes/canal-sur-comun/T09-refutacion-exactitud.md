# T09 · Refutación (fase 4) · Lente de exactitud normativa · Ley 31/1995

Tema: `temas/canal-sur-comun/09-ley-31-1995.md` (estado tras la verificación, commit 5113690).
Leídos antes, enteros: `ENCARGO.md`, `CICLO.md`, `metodo/MANUAL.md`, `metodo/ENCARGOS.md`,
`T09-redaccion.md` y `T09-verificacion.md`.

**Fecha de lectura de todos los preceptos: 24-09-2026.** Fuente: volcado
`fuentes/canal-sur/BOE-A-1995-24292.md` y su `.redacciones.tsv` (88 bloques). Contrastes
externos hechos hoy: `boe.py precepto` para la DA 5.ª a 01-04-2026, el art. 3 a 01-09-2022, el
art. 7 a 01-04-2026, el art. 45 a 01-01-2000, la DDU del RDLeg 5/2000 y el art. 156 del RDLeg
8/2015; metadatos de la API del BOE (BOE núm. 269, entrada en vigor 10-02-1996; títulos de
RD 171/2004, RD 39/1997, RD 1627/1997, LO 3/2007 y Ley 30/2005); texto de la Ley 30/2005
(BOE-A-2005-21525), disposición adicional cuadragésima séptima.

No he corregido el tema. No he tocado ningún otro fichero salvo crear este informe.

## 1. Qué se ha mirado

- **El cuerpo entero del tema**, epígrafe por epígrafe, contra el bloque de la ley que
  explica: exposición de motivos, arts. 1 a 54 y 32 bis, las diecinueve adicionales, dos
  transitorias, derogatoria y dos finales. Cada cifra, plazo, mayoría, recuento, requisito y
  salvedad: umbrales (6, 10, 25, 30, 31-49, 50), escala del 35.2, plazos (24 h del 21.3; 3 días
  hábiles y 24 h del 44; 15 días del 36.3; tres meses y treinta días de la DA 6.ª; tres meses de
  la DF 2.ª), mayorías (21.3, 13.4, DA 4.ª), recuentos declarados (ocho definiciones, cinco
  funciones del 8, seis del 9.1, siete letras del 6.1, nueve principios, cinco documentos del
  23.1, seis obligaciones del 29.2, tres modalidades del 30.1, seis materias del 31.3, cuatro
  competencias y siete facultades del 36, dos competencias y cuatro facultades del 39, cuatro
  criterios del 34.3, tres principios del 45.1, diecinueve adicionales), fechas y normas
  modificadoras contra la cadena del `.redacciones.tsv`, y la lista de preceptos con más de una
  redacción de la trazabilidad (coincide con el `.tsv`: 23 artículos y la DA 5.ª). Todo cuadra
  salvo lo que se dice en el apartado 3.
- **Contraste propio de negritas por epígrafe**: cada negrita de cada `### Artículo N` buscada
  en el bloque `aN` (no en el artículo que adivina la lente), y las del apartado de
  disposiciones en los bloques de disposiciones. Resultado en el apartado 2.

## 2. Las 157 negritas «no literales» de la lente automática

`refutar_exactitud.py` da hoy lo mismo que en la verificación: **729 negritas comprobadas, 157
no literales**. No las he muestreado: **las he revisado las 157**, empezando por las de más
riesgo (las que parecen cita literal, las cifras y las fechas). Reparto:

| Clase | Cuántas | Qué son | Veredicto |
| --- | --- | --- | --- |
| Literales de otro precepto | 48 | La lente las atribuye al artículo cuyo marcador abrió el bloque, pero el tema las atribuye en el texto al precepto correcto | Todas bien atribuidas |
| No están en la ley | 109 | Rótulos de apartado («14.2. El deber del empresario.», «Sus seis funciones:»), nombres de normas, fechas de vigencia, remisiones («9.1.f) y 44») | Ninguna finge ser cita; las que llevan dato se han comprobado |

**Veredicto: la verificación tenía razón.** Ninguna de las 157 es un defecto de literalidad
o de atribución. Detalle de lo comprobado:

### 2.1. Las 48 literales de otro precepto (todas)

| Bloque de la lente | Negrita (inicio) | Dónde está en la ley | ¿El tema la atribuye bien? |
| --- | --- | --- | --- |
| art. 3 (×4) | «disposición adicional quinta» / «decimoctava» | nombres de la DA 5.ª y DA 18.ª | Sí |
| art. 4 (×4) | «accidente de trabajo, enfermedad profesional, accidente no laboral y enfermedad común», «normativa de Seguridad Social», «disposición adicional primera», «accidente de trabajo» | DA 1.ª | Sí, «La disposición adicional primera remite…» |
| art. 9 (×3) | «su propia comunidad autónoma», «pertenecer a los grupos de titulación A o B y acreditar formación específica», «disposición adicional decimoquinta» | DA 15.ª | Sí |
| art. 13 (×2) | «formación, información, investigación, estudio y divulgación»; «Inspección de Trabajo y Seguridad Social» | art. 8.1.b); arts. 8, 9… | Sí: cuadro comparativo, fila del Instituto (art. 8) y de la Inspección (art. 9) |
| art. 7 (×1) | «podrá informar y formular propuestas» | art. 13.3 | Sí: está bajo `### Artículo 13` (la lente lo manda al 7 por la mención «artículos 7, 8, 9 y 11») |
| art. 21 (×5) | «El Inspector de Trabajo y Seguridad Social», «inobservancia de la normativa», «a su juicio», «en el plazo de tres días hábiles», «en el plazo máximo de veinticuatro horas» | art. 44.1 | Sí: fila del cuadro con precepto «9.1.f) y 44» |
| art. 26 (×1) | «disposición adicional undécima» | DA 11.ª | Sí |
| art. 32 (×2) | «disposición transitoria segunda», «disposición adicional decimotercera» | DT 2.ª, DA 13.ª | Sí |
| art. 32 bis (×6) | «la preceptiva presencia de recursos preventivos se aplicará a cada contratista», «cuando, durante la obra, se desarrollen trabajos con riesgos especiales», «tendrá como objeto vigilar…», «sin perjuicio de las obligaciones del coordinador…», «obras de construcción», nombre de la DA | DA 14.ª, 1.a), 1.b), 1.c) y 2 | Sí |
| art. 35 (×9) | «que carezcan de representantes…», «los trabajadores podrán elegir por mayoría…», «las facultades, garantías y obligaciones de sigilo profesional», «prorrogándose por el tiempo indispensable…», «deberá estar previsto en sus Estatutos…», «se computarán ambos colectivos», «se realizará conjuntamente», nombres de las DA 4.ª y 10.ª | DA 4.ª y DA 10.ª | Sí |
| art. 36 (×3) | «promover iniciativas sobre métodos y procedimientos para la efectiva prevención de los riesgos» | art. 39.1.b) | Sí: el tema la da precisamente como competencia del Comité, **no** de los Delegados |
| art. 36 (bloque de la DT 1.ª) | «sin perjuicio del respeto a las disposiciones más favorables», «previstas en los convenios colectivos vigentes» | DT 1.ª.1 | Sí |
| art. 14 (×6) | «excepto la remisión al capítulo IV», «excepto remisión al capítulo V», «excepto referencia a la impartición por medios propios o concertados», «apartados 1, 2 y 3», «excepto en lo relativo a las empresas de trabajo temporal», «excepto las referencias al Comité de Seguridad y Salud» | DA 3.ª.2.a), filas 14, 18, 19, 24, 28 y 36 | Sí, cada excepción con su artículo |
| art. 54 (×1) | «el artículo 54 constituye legislación básica de contratos administrativos…» | DA 3.ª.3 | Sí |

### 2.2. Las 109 que no están en la ley (revisadas todas; las que llevan dato, comprobado)

- **Rótulos con recuento**: «Sus seis funciones:» (9.1, a–f: seis), «15.1. Los nueve
  principios generales» (a–i), «16.2. Los dos instrumentos esenciales», «29.2. Las seis
  obligaciones concretas» (1.º–6.º), «30.1. Las tres modalidades», «31.3. Las seis materias»
  (a–f), «34.1. El umbral de los seis», «36.1. Las cuatro competencias» (a–d), «36.2. Las
  siete facultades» (a–g), «39.1. Dos competencias» (a–b), «39.2. Cuatro facultades» (a–d),
  «32 bis.4. La cuarta vía» (tras las tres letras del 32 bis.2). Todos cuadran.
- **Rótulos que atribuyen apartado**: «Composición (13.2).» a «Funcionamiento (13.7).», «Riesgo
  laboral (2.º)», «Riesgo grave e inminente (4.º)», «Condición de trabajo (7.º)», «9.2 a 9.4.»,
  «7.2. La salvedad…», «21.1»–«21.4», «24.1»–«24.6», «26.1»–«26.5», «35.1»–«35.4»,
  «37.1»–«37.4», «38.1»–«38.3», «42.3», «43.1»–«44.2» y demás: cada uno encabeza el contenido
  del apartado que dice.
- **Fechas y normas**: RDL 16/2022, de 6 de septiembre, y 9-09-2022 (cadena de a3, da,
  daquinta); DF 1.ª de la Ley 1/2026 y 10-04-2026 (a7, daquinta); LO 3/2007 (a5 y a26, vigencia
  24-03-2007, BOE-A-2007-6115); Ley 35/2014 y 1-01-2015 (a32); Ley 54/2003 (a32bis, 14-12-2003);
  RDLeg 5/2000, DDU apartado 2 letra c), y 1-01-2001 (leída: «los apartados 2, 4 y 5 del
  artículo 42, y del artículo 45, excepto los párrafos tercero y cuarto de su apartado 1, al
  52»); BOE núm. **269** de 10-11-1995 (API del BOE); RD 39/1997 como Reglamento de los
  Servicios de Prevención (título en la propia DA 16.ª); art. 156 LGSS (RDLeg 8/2015, 156.2.a:
  «al ir o al volver del lugar de trabajo»); «disposición adicional tercera, apartado 3» (DA
  3.ª.3). Todo correcto.

### 2.3. Lo que la lente no ve y el contraste por epígrafe sí

El contraste propio (cada negrita contra el bloque de su `### Artículo`) no añade nada a lo
anterior salvo **una palabra suelta**: «**pudiendo**» en el art. 28.5, que la lente da por
buena porque «pudiendo» aparece en otros artículos, y que en el 28 no está (hallazgo 5). Las
negritas del apartado de disposiciones están todas en los bloques de disposiciones, salvo dos
encabezados (hallazgo 6).

## 3. Hallazgos

Ninguno cambia la respuesta a una pregunta sobre el articulado. Uno puede inducir a error.

### Hallazgo 1 · Art. 21.2: se cae el «en caso necesario»

- **Dónde**: art. 21, párrafo tras la cita del 21.2 («Las dos cosas juntas —interrumpir y
  abandonar—…») y cuadro «Quién paraliza», fila 21.2 («El propio trabajador interrumpe y
  abandona»).
- **Qué dice**: «Las dos cosas juntas —interrumpir y abandonar—, y el motivo es riesgo grave e
  inminente». Y en el cuadro: «El propio trabajador interrumpe y abandona».
- **Qué debería decir**: «El derecho es a interrumpir la actividad y, **en caso necesario**,
  abandonar el lugar de trabajo; y el motivo es riesgo grave e inminente: ni "riesgo muy
  grave"…». En el cuadro: «El propio trabajador interrumpe su actividad y, en caso necesario,
  abandona el lugar de trabajo».
- **Fuente literal** (art. 21.2): «el trabajador tendrá derecho a interrumpir su actividad y
  abandonar el lugar de trabajo, **en caso necesario**, cuando considere que dicha actividad
  entraña un riesgo grave e inminente para su vida o su salud».
- **Gravedad**: induce a error. La cita literal está justo encima, pero el comentario y el
  cuadro, que es lo que se repasa, presentan el abandono como inseparable de la interrupción
  (error 6 del catálogo: salvedad omitida).

### Hallazgo 2 · Disposición adicional tercera: la lista de «lo que queda fuera» está incompleta

- **Dónde**: Disposiciones, párrafo «Disposición adicional tercera».
- **Qué dice**: «La lista es larga y no hay que memorizarla, pero sí saber qué queda fuera,
  porque ahí está el matiz:» y da las exclusiones de los arts. 14, 18, 19, 24, 28, 36 y 42.
- **Qué falta**: otras exclusiones parciales del mismo listado, que el lector entenderá como
  preceptos básicos enteros: art. 3 («apartados 1 y 2, excepto el párrafo segundo»), art. 5
  («apartado 1»), art. 30 («apartados 1, 2, excepto la remisión al artículo 6.1.a), 3 y 4,
  excepto la remisión al texto refundido de la Ley del Estatuto de los Trabajadores»), art. 31
  («apartados 1, excepto remisión al artículo 6.1.a), 2, 3 y 4»), art. 34 («apartados 1,
  párrafo primero, 2 y 3, excepto párrafo segundo»), art. 35 («apartados 1, 2, párrafo
  primero, 4, párrafo tercero»), art. 37 («apartados 2 y 4») y art. 45 («apartado 1, párrafo
  tercero»); y que no figuran en la lista, entre otros, los arts. 1, 6 a 11, 13, 27, 32, 32 bis,
  38 a 41, 43, 44 y 53.
- **Qué debería decir**: o bien completar la enumeración con esas exclusiones, o bien quitar la
  promesa: «La lista es larga; estos son algunos de los matices: …» y añadir «No figuran en la
  lista, entre otros, los artículos 27 (menores) y 38 a 40 (Comité de Seguridad y Salud y
  colaboración con la Inspección), y del 37 solo son básicos los apartados 2 y 4».
- **Fuente literal**: DA 3.ª, apartado 2, letra a), filas citadas arriba.
- **Gravedad**: menor (induce a error solo si cae una pregunta sobre si un precepto concreto
  es básico).

### Hallazgo 3 · Ley 30/2005: fecha de entrada en vigor mal dicha

- **Dónde**: Disposiciones, DA 5.ª, párrafo «Qué cambió», última frase: «la de la Ley 30/2005,
  de Presupuestos Generales del Estado para el año 2006 (en vigor el 19 de enero de 2006)».
- **Qué pasa**: el 19-01-2006 es la fecha de vigencia que la cadena del texto consolidado
  asigna a esa redacción de la DA 5.ª, no la de entrada en vigor de la Ley 30/2005. La ley entró
  en vigor el 1-01-2006 (metadatos del BOE: fecha de vigencia 20060101) y su disposición
  adicional cuadragésima séptima dice «**Con efectos de 1 de enero y vigencia indefinida**, se
  añade un apartado 2 a la disposición adicional quinta de la Ley 31/1995…».
- **Qué debería decir**: «la de la Ley 30/2005, de Presupuestos Generales del Estado para el año
  2006 (disposición adicional cuadragésima séptima, con efectos de 1 de enero de 2006), la del
  Real Decreto-ley 16/2022…». Si se prefiere no nombrar la disposición: «(con efectos de 1 de
  enero de 2006)».
- **Fuente literal**: Ley 30/2005, DA 47.ª, citada arriba.
- **Gravedad**: menor.

### Hallazgo 4 · La Ley 1/2026 no cambió el apartado 1 de la DA 5.ª «para incluir a los autónomos»

- **Dónde**: Identificación y encaje, segundo punto de la lista de reformas: «modificó el
  artículo 7.1.a) y los apartados 1 y 4 de la disposición adicional quinta para incluir a las
  personas trabajadoras autónomas».
- **Qué pasa**: en el apartado 1 (párrafo segundo) el cambio es otro: la mención de Ceuta y
  Melilla pasa delante del porcentaje. Solo el 7.1.a) y el apartado 4 incluyen a las personas
  trabajadoras autónomas. El propio tema lo explica bien en el párrafo «Qué cambió».
- **Qué debería decir**: «modificó el artículo 7.1.a) y el apartado 4 de la disposición
  adicional quinta para incluir a las personas trabajadoras autónomas, y reordenó el párrafo
  segundo del apartado 1 de esa disposición (acciones de ámbito estatal y de Ceuta y Melilla)».
- **Fuente literal**: DA 5.ª.1, párrafo segundo, vigente: «…de ámbito estatal y en las ciudades
  de Ceuta y Melilla, cuyo importe será del 33 por ciento…»; a 01-04-2026: «…de ámbito estatal,
  cuyo importe será del 33 % del presupuesto total de las mismas, y en las ciudades de Ceuta y
  Melilla…». Ninguna de las dos menciona a los autónomos.
- **Gravedad**: menor.

### Hallazgo 5 · Art. 28.5: «pudiendo» en negrita no es literal

- **Dónde**: art. 28.5, último párrafo: «**pudiendo** esos trabajadores **dirigirse a estos
  representantes**».
- **Qué debería decir**: «y **dichos trabajadores podrán dirigirse a estos representantes** en
  el ejercicio de los derechos reconocidos en la presente Ley» (o «pudiendo» en redonda).
- **Fuente literal** (art. 28.5, párrafo tercero): «Dichos trabajadores podrán dirigirse a estos
  representantes en el ejercicio de los derechos reconocidos en la presente Ley».
- **Gravedad**: menor (promesa de literalidad; el sentido es el mismo). Del mismo tipo, y aún
  más leve: en el 26.4 «**podrá declararse**», donde la fuente dice «Podrá, asimismo,
  declararse».

### Hallazgo 6 · Dos encabezados en negrita con forma de rúbrica literal que no lo son

- **Dónde**: Disposiciones, «**Disposición adicional quinta. La Fundación Estatal para la
  Prevención de Riesgos Laborales, FSP.**» y «**Disposición adicional decimoctava. Servicio del
  hogar familiar.**».
- **Qué pasa**: tienen la forma «Disposición X. Rúbrica.» y van en negrita, así que se leen como
  la rúbrica oficial. La de la DA 5.ª lleva un «La» que no está; la de la DA 18.ª es un resumen:
  la rúbrica real es «Protección de la seguridad y la salud en el trabajo de las personas
  trabajadoras en el ámbito de la relación laboral de carácter especial del servicio del hogar
  familiar».
- **Qué debería decir**: «**Disposición adicional quinta. Fundación Estatal para la Prevención
  de Riesgos Laborales, FSP.**» y, para la 18.ª, la rúbrica literal o el encabezado sin negrita
  («Disposición adicional decimoctava (servicio del hogar familiar).»).
- **Fuente literal**: rúbricas de `daquinta` y `da` en el volcado, citadas arriba.
- **Gravedad**: menor.

## 4. Lentes automáticas (corridas hoy sobre el tema tal como está)

| Lente | Tramos que miró | Resultado | Explicación |
| --- | --- | --- | --- |
| `refutar_exactitud.py` | 729 negritas | 157 «no literales» | Revisadas las 157 (apartado 2): 48 literales de otro precepto, todas bien atribuidas en el tema; 109 rótulos, nombres de normas y fechas, correctos. Falsos positivos. La lente no ve el «pudiendo» del hallazgo 5 |
| `refutar_modo.py` | el tema entero | 3 | Los mismos tres falsos positivos que explicó la verificación (art. 3 «obligadas» en una pregunta; «deberá» de la DA 10.ª y «deben» de la DA 15.ª atribuidos por la lente a los arts. 35 y 9). Confirmados |
| `refutar_citas.py` | 0 tramos | 0 | No mira nada: el tema no usa bloques `> ` salvo el enunciado. Las citas entre comillas las cubre la lente de exactitud y el contraste propio |

## 5. Resumen

Tema sólido. Las 157 negritas señaladas por la lente son falsos positivos y la verificación
acertó al despacharlas. Seis hallazgos, ninguno cambia la respuesta a una pregunta sobre el
articulado: uno induce a error (el «en caso necesario» del 21.2) y cinco son menores (lista
incompleta de la DA 3.ª, fecha de la Ley 30/2005, alcance de la reforma de 2026 en la
identificación y dos casos de negrita no literal).

## 6. Ficheros tocados

- Creado este informe. Ningún otro.
