# Traspaso · Cómo hacemos los temarios

Todo lo que el proyecto ha aprendido haciendo temarios verificados —veintitrés
volúmenes de RTVE, el de Correos y el arranque del Cuerpo General Administrativo
del Estado—, reunido en un solo fichero para **empezar una oposición nueva en otra
conversación** sin reconstruir nada.

**Siglas de este documento**: Administración General del Estado (**AGE**);
Boletín Oficial del Estado (**BOE**); Instituto Nacional de Administración
Pública (**INAP**); reconocimiento óptico de caracteres (**OCR**, por sus siglas
inglesas); **TOAC** (Temarios de Oposiciones, la marca del proyecto).

---

## 0. Cómo usar este fichero

**Lo mejor es abrir la conversación nueva sobre el mismo repositorio,
`Aaroncbr92/Aaroncbr92`.** Así vienen con ella el método completo
(`metodo/MANUAL.md`), las treinta herramientas de `herramientas/`, las normas ya
volcadas de `fuentes/` y los volúmenes hechos, que sirven de modelo. Este fichero
es el mapa; el repositorio es el taller.

Si la conversación nueva no tiene el repositorio, este fichero basta para
entender el método, pero **las herramientas habría que volver a escribirlas**.

**Primer mensaje sugerido para la conversación nueva:**

> Vamos a hacer un temario de oposición para **[nombre de la oposición]** con el
> método TOAC. Lee primero `metodo/TRASPASO.md` y `metodo/MANUAL.md` enteros.
> Trabaja en la rama **[nombre de rama]**. Empieza por el **sondeo de
> viabilidad** (apartado 4, paso 1) y no escribas ningún tema hasta que te lo
> diga.

---

## 1. La regla de la que sale todo

> **Nada se escribe de memoria. Cada dato se lee en la fuente oficial antes de
> afirmarlo, y lo que no se puede confirmar se quita.**

No se suaviza, no se pone «aproximadamente», no se deja «según la doctrina». **Se
quita.** Un tema con un hueco reconocido vale más que uno completo con tres datos
inventados dentro, porque el hueco se ve y el dato inventado no.

Un modelo de lenguaje escribe temario jurídico **plausible** sin esfuerzo: casi
todo correcto y un porcentaje pequeño mal, repartido al azar y sin marcar. **Ese
porcentaje pequeño es exactamente lo que hace fallar una pregunta.**

Tres corolarios que se aplican en todo el proyecto:

- **La negrita es una promesa de literalidad.** Lo que va en negrita tiene que
  estar tal cual en la fuente; las lentes lo comprueban así. Lo que no lo es va
  en redonda o en cursiva (`herramientas/despintar.py` retira las negritas que
  el texto no cumple).
- **Un cero de una lente sólo vale si la lente miró algo.** Una comprobación que
  no encuentra nada que mirar devuelve cero y parece un tema impecable. Hay que
  saber siempre qué comprobación pasa por qué material.
- **Lo que no se cubre se declara.** Cada tema termina con «Lo que este tema no
  da, y dónde está». Cada volumen dice en su portada sus limitaciones: sin
  examen publicado, sin norma nombrada, preguntas que dependen de una imagen,
  respuestas oficiales equivocadas.

---

## 2. Leer la ley bien (lo que más se falla)

**Los textos consolidados encadenan redacciones.** El BOE devuelve un artículo
con **todas** sus redacciones sucesivas. Lo primero que se ve suele ser la más
antigua, a menudo derogada. Hay que quedarse con la **última vigencia ya
cumplida** y saber cuántas redacciones tiene. `boe.py precepto` lo hace.

**Reformas cruzadas.** Una reforma publicada antes pero con vigencia posterior a
otra se «come» a la intermedia. Señal: la redacción con vigencia más alta no es
la publicada más tarde. `boe.py` avisa; se contrasta a mano con la página
consolidada. De 4.264 preceptos citados, **veinte estaban cruzados**.

**Decretos-ley no convalidados** siguen apareciendo en la cadena como si
rigieran. No rigen.

**Los identificadores no siguen ninguna regla.** En la Ley 17/2006 el artículo
43 es el bloque `a4-2`. Nunca se deduce un identificador por analogía: se
resuelve contra el índice real (`boe.py indice`, `boe.py buscar`).

**Y los identificadores de norma tampoco se adivinan.** En el Administrativo C1,
**nueve de veintisiete identificadores BOE-A-… que parecían correctos estaban
mal**. El peor: `BOE-A-1982-11196` no era la Ley Orgánica del Tribunal de
Cuentas sino la de honor e intimidad —que además ya estaba en la bóveda, así que
nadie lo habría notado—. **Antes de volcar una norma, se comprueba su título
contra lo que devuelve el BOE.** `boe_buscar.py` busca por título.

**Redacción vigente, y fecha de corte cuando la haya.** Por defecto se trabaja
con la redacción vigente el día en que se escribe. Si la convocatoria congela el
temario a una fecha (RTVE lo hace: 21-XII-2022), se vuelca con
`boe.py --fecha AAAAMMDD` y se guarda **en carpeta propia**
(`fuentes/corte-AAAAMMDD/`). **Nunca se pisa un volcado de otro corte**: la misma
ley puede tener que estar congelada para un volumen y vigente para otro.

---

## 3. El ciclo de cada tema: cinco fases, ninguna sobra

Medido sobre un temario heredado de 35 temas:

| Fase | Correcciones que encuentra |
|---|---|
| Verificación inicial | 25 a 60 por tema |
| Primer escéptico, sobre el tema ya «terminado» | 2 a 12 más |
| Segundo escéptico | todavía 0 a 6 |

1. **Investigar.** De tres a seis agentes en paralelo, uno por grupo de
   epígrafes. Cada uno lee la fuente oficial y devuelve 1.200–2.200 palabras con
   **el precepto pegado a cada afirmación** y la cita literal. **No se les dan
   los números de artículo**: los localizan ellos. Y dicen lo que no pueden
   confirmar.
2. **Redactar.** **Un solo agente para todo el tema**, con todo el material de la
   fase 1. Escribe **por partes, guardando cada epígrafe** según lo termina.
   Escribe con margen: recortar es fácil, añadir lo que nadie investigó no.
3. **Verificar.** Relee cada precepto con el catálogo de errores delante y
   **quita lo que no confirma**.
4. **Refutar.** Agentes cuyo encargo es **tumbar el tema**, con lentes
   distintas: exactitud normativa, cobertura de examen, prosa y forma. Más las
   lentes automáticas (apartado 8).
5. **Rematar**, y otra refutación que **tiene que salir limpia**. La ronda que
   corrige también estropea: un «el apartado 2» que se queda colgando.

**La prueba que decide si el tema está terminado**: de diez a quince preguntas en
el estilo real del examen —y todas las reales del banco que le tocan—, y se
contesta cada una con el cuerpo del tema delante y nada más. **La laguna se
cierra ampliando el tema, nunca recortando la pregunta.**

**Extensión: la manda el enunciado.** Se recorta la prosa, no el contenido
normativo. Fuera el tejido conectivo («como hemos visto», «cabe destacar»), la
repetición entre epígrafes y la doctrina sin precepto.

---

## 4. Orden de trabajo para una oposición nueva

Es el orden que funcionó en Correos y en el Administrativo C1. Cada paso se
commitea y se empuja antes de pasar al siguiente.

### Paso 1 · Sondeo de viabilidad (antes de escribir nada)

Un informe en `informes/sondeo-<oposicion>-<fecha>.md` que conteste:

- **La convocatoria**: resolución, fecha, plazas, estructura del ejercicio,
  penalización, fecha de examen.
- **El programa**: cuántos temas y bloques, y **si nombra normas o no**.
- **Los exámenes anteriores**: si existen, dónde, cuántos, **si su PDF tiene capa
  de texto o hay que reconocerlo ópticamente**, si la plantilla es provisional
  o definitiva, cuántas preguntas anuló el tribunal.
- **Qué hay ya en la bóveda** de normas y de temas reutilizables.
- **Veredicto** y lo que el sondeo no puede cerrar.

El del Administrativo C1 (`informes/sondeo-administrativo-age-2026-09-15.md`)
sirve de modelo.

### Paso 2 · La convocatoria y el programa, literales

En `convocatoria/<oposicion>/`: el PDF de la convocatoria y el programa
**transcrito literal** en `PROGRAMA-<OPOSICION>.md`, sacado del PDF, no copiado a
mano. **Los epígrafes de cada tema reproducen el enunciado literal y en el mismo
orden.** Se cuentan los temas y se comprueba contra lo que dice la convocatoria.

### Paso 3 · Los exámenes, en la bóveda y leídos a máquina

En `convocatoria/<oposicion>/examenes/`: cada cuadernillo y cada plantilla, con
su volcado en texto y un `README.md` que diga de qué convocatoria es cada uno
(**leído en la portada, no en el nombre del fichero**, que mienten).

Un lector por oposición (`herramientas/<oposicion>_examen.py`) que trocee cada
cuadernillo en preguntas y case cada plantilla. **Tiene que dar el número exacto
de preguntas del cuadernillo y ninguna incompleta.** Si no cuadra, el lector está
mal, no el examen.

**La comprobación gratis**: si hay modelos A y B barajados, cada pregunta tiene
**dos plantillas independientes** y las dos deben señalar **el mismo texto de
opción** aunque la letra sea distinta. En el Administrativo C1: 247 de 247, cero
discrepancias.

### Paso 4 · El acta de reparto

`banco/especifico-<oposicion>.tsv`: **a mano y con motivo**, cada pregunta
distinta al tema del programa que la contesta. Columnas del último modelo:
`origen · seccion · numero · tema · motivo · epigrafe`. La cabecera del acta
explica la cuenta —cuántos cuadernillos, cuántas preguntas, cuántas distintas y
por qué— **contada, no copiada**.

Un constructor (`herramientas/banco_<oposicion>.py`) que lee el acta y escribe
un fichero por tema, y **canta** las filas que no casan con ninguna pregunta y
las preguntas que ninguna fila reparte.

**Busca una comprobación externa del reparto.** En el Administrativo C1 las bases
mandan 40 preguntas de los bloques I–V y 30 del VI; el acta, sin ajustar nada,
puso 122 en el VI y 181 en el resto sobre cuatro exámenes. Si hubiera salido
torcido, lo habría dicho.

### Paso 5 · Las normas

Con la lista de normas que citan las preguntas y que nombra el programa, se
vuelca cada una con `boe.py norma <id> fuentes/<carpeta>/` **después de comprobar
su identificador**. Un `README.md` en la carpeta dice qué hay, qué falta y por
qué. Lo que no es texto consolidado del BOE (convenios, órdenes antiguas,
documentos de empresa) se busca aparte y se declara.

### Paso 6 · Los temas, de dos en dos

Por el ciclo del apartado 3. **Se empieza por los más preguntados.** Dos temas por
tanda es lo que aguanta una sesión.

### Paso 7 · Esquemas, remites, volumen, lentes, informes

- **Esquema** por tema (apartado 6).
- **Remite** de cada pregunta: la columna `epigrafe` del acta, rellenada a mano
  según se escribe cada tema. `refutar_remites.py` la comprueba.
- **Alta del volumen** en `BLOQUES` de `herramientas/libro.py` y
  `indice.py → libro.py <bloque> → pdf.py <html> → word.py <bloque>`.
- **Las seis lentes** en cero, y dos informes: `refutacion-<oposicion>.md` (el
  cuadro entero, lente por tema, y la explicación de **cada** número distinto de
  cero) y `cobertura-<oposicion>.md` (qué preguntas contesta cada tema y qué no
  cubre el volumen).

---

## 5. Cláusulas de encargo (se pegan literales)

En todos los encargos:

- **«Si algo de este encargo no cuadra con la fuente, manda la fuente y
  dímelo.»**
- **«Lo que no puedas confirmar, quítalo. No lo sustituyas por lo que
  recuerdes.»**
- **«Limítate a tu tema y declara qué otros ficheros has tocado.»**
- **«Escribe tu informe en un fichero de `informes/` según lo vayas produciendo.
  No lo dejes solo en la respuesta.»**
- **«Trabaja con la redacción vigente el día en que escribes. Donde difiera de la
  que cita el programa, dilo en una nota de una línea: qué cambió, por qué norma
  y desde cuándo.»**
- **«Declara la fecha en la que leíste cada precepto.»**

En las refutaciones: **«Cero hallazgos es un buen resultado si el tema está
bien.»** Sin ella, inventan para justificar el turno.

Al rematar: **«Comprueba cada corrección en la fuente antes de aplicarla. Si el
informe se equivocó, no la apliques y dilo.»** Y: **«Relee el resultado entero y
comprueba que cada "ese artículo", "dicha ley" o "el apartado X" tiene delante el
antecedente que le corresponde.»**

### Los nueve errores que se repiten (van dentro del encargo del verificador)

1. **Cita cruzada**: el texto nombra un artículo y la referencia apunta a otro.
2. **Ley por reglamento**, o al revés.
3. **Recuentos que no cuadran**: «tres requisitos» y enumera cuatro.
4. **Modo verbal cambiado**: obligatorio lo que la norma deja potestativo.
5. **Siglas sin presentar** la primera vez.
6. **Requisito, excepción o salvedad omitida**: el «salvo que…» que desaparece.
   Es el que más puntos cuesta.
7. **Redacción derogada citada como vigente.**
8. **Número de artículo mal.**
9. **Afirmación sin apoyo en la fuente** («la doctrina entiende…»).

---

## 6. Anatomía de un tema y de un esquema

**Un tema** (`temas/<oposicion>/NN-titulo.md`):

1. Título: `# Tema N del <bloque> · <título>`.
2. **Ficha** entre `<!-- portada -->` y `<!-- /portada -->`: bloque, a qué
   ocupación sirve, fuente, identificador, redacción que se estudia, norma de
   apoyo, extensión. **Sin** filas de «Esquema de repaso» ni de «Verificación».
3. **Las siglas del tema, presentadas de entrada**, en un párrafo.
4. **El enunciado del programa, literal**, en bloque de cita, con su procedencia.
5. Un párrafo que diga **cómo se pregunta este tema**.
6. Índice entre `<!-- indice -->` (lo genera `indice.py`).
7. Los epígrafes, **reproduciendo el enunciado en orden**.
8. **La normativa que el tema invoca**, con identificador y redacción.
9. **Lo que este tema no da, y dónde está.**
10. Trazabilidad.

**Un esquema** (`esquemas/<oposicion>/NN-titulo.md`) es un **esqueleto**, no un
resumen: telegrama, con el precepto (o la fuente, `[boe]`, `[doc]`…) delante de
cada línea. **Horquilla: unas 2.000 palabras y 130 líneas**, y no crece en
proporción al tema: un agente sin cifra entregó uno de 8.341 palabras para un
tema de 15.100. **Se quita explicación, nunca el dato normativo.**

---

## 7. Normas de formato permanentes del volumen

- **Nada de referencias a ficheros del proyecto** dentro de los temas: ni rutas,
  ni nombres de herramientas, ni de informes. A quien estudia no le dicen nada.
- **Ficha sin** las filas «Esquema de repaso» y «Verificación».
- **Preguntas en negrita, opciones en redonda.**
- **Primera fila de toda tabla en gris.**
- **Solucionario con filas alternas gris y blanco**, en parrilla de diez en diez,
  identificando cada respuesta por el número con que la pregunta va impresa.
- **Encabezados de tema: «TEMA N – Título».**
- **Cuerpo justificado**, en PDF y en Word.
- **Índice general a tres niveles** (tema, epígrafe, subepígrafe), **con número
  de página y clicable**; marcadores en el PDF.
- **Encabezado «TOAC – Temarios de Oposiciones»**; pie con **«Página X de Y»** a
  la izquierda y el nombre del bloque a la derecha.
- **La portada, limpia**: sin encabezado ni pie.
- **No se imprime la procedencia** (cuadernillo y número) bajo cada pregunta.
- **Las respuestas van al final del volumen**, no junto a la pregunta: con la
  respuesta a la vista no hay autoevaluación.
- **Nota de atribución** en el preliminar: de quién son las preguntas, que se
  reproducen para analizarlas y que el temario no está avalado por ese
  organismo (`texto_atribucion` en `libro.py`, con `titular_preguntas` en el
  bloque).
- **El remite bajo cada pregunta** («La contesta el epígrafe N.N.») sólo cuando
  **todas** lo llevan y la lente lo confirma (`remite_epigrafe=True`).

El **logotipo TOAC sigue pendiente de subir** a `marca/` (llegó como imagen en
conversación y desde ahí no se puede volcar a disco). Mientras, el encabezado va
en texto.

---

## 8. Las seis lentes de refutación

Todas tienen que devolver **cero**, y cada número distinto de cero se explica en
el informe de refutación.

| Lente | Qué comprueba | Cuándo se queda sin objeto |
|---|---|---|
| `refutar_exactitud.py tema fuente…` | Cada negrita del tema, contra el texto de **su** artículo | Cuando la fuente no numera por artículos: devuelve un cero **vacío** |
| `refutar_citas.py tema fuente…` | Cada tramo en negrita de un bloque `> ` como **subcadena literal** del volcado | Nunca, si hay citas. Falla con volcados corruptos, paginados o con palabras pegadas: se acorta la cita o se da en prosa declarando el defecto |
| `refutar_modo.py tema fuente…` | «Podrá» / «deberá» cambiados, y salvedades («salvo», «excepto») omitidas | Sin articulado |
| `refutar_prosa.py tema` | Relleno, frases repetidas entre epígrafes, **siglas sin presentar**, negritas rotas o anidadas | Nunca. Se pasa también a esquemas e informes |
| `refutar_documento.py tema fuente…` | Negritas y **cifras en negrita** contra fuentes sin artículos (planes, guías, documentos de empresa) | — |
| `refutar_remites.py` | Que el epígrafe del remite **existe**, es **de su tema**, **habla** de lo que la pregunta mide y **ningún otro tema la contesta mucho mejor** | Antes de escribir los temas |

**Cuando una lente no tiene sobre qué mirar, se dice y se pone en su lugar una
comprobación nombrada** (Imagen Personal, Ambientación Vestuario y Profesor de
Orquesta lo hicieron: cobertura pregunta a pregunta, alcance declarado,
ausencia de nombre propio, ausencia de cifra sin fuente).

**La cuarta comprobación de `refutar_remites` nació de un fallo real**: la lente
aprobaba tres preguntas mal repartidas. Comparar contra todos los temas movió de
tema ocho preguntas en Correos.

---

## 9. La maquinaria

| Herramienta | Para qué |
|---|---|
| `boe.py indice / buscar / precepto / norma` | Leer y volcar legislación consolidada, con la cadena de redacciones y el aviso de reforma cruzada. `--fecha AAAAMMDD` para un corte |
| `boe_buscar.py "título"` | Encontrar el identificador de una norma por su título |
| `doue.py` | Normas de la Unión Europea publicadas por el BOE (no consolidadas, y lo dice) |
| `extraer_examen.py` | Texto de un cuadernillo desde su PDF, en dos modos, quedándose con el que deja menos letras huérfanas |
| `plantilla_ocr.py` | Plantillas sin tabla de caracteres: se lee **la celda**, no la hoja |
| `administrativo_examen.py trocear / claves / casar / cruzar` | Modelo de lector para cuadernillos con capa de texto limpia (INAP) |
| `banco_*.py` | Del acta al banco por tema |
| `indice.py` | Portada e índice de cada tema; avisa si se cuela una fila prohibida en la ficha |
| `libro.py <bloque>` | El volumen en HTML: ficha, cuerpo, esquema y preguntas de cada tema, respuestas al final |
| `pdf.py <html>` | PDF con Chromium, índice paginado en dos vueltas, marcadores, encabezado y pie |
| `word.py <bloque> <docx>` | El mismo volumen en Word, con tabla de contenido y campos |
| `despintar.py` | Retira las negritas que no son cita literal |
| `refutar_*.py` | Las seis lentes |

**Comprobar un PDF a ojo**: `pymupdf.open(f)[n].get_pixmap(dpi=…).save(png)` y
mirar la imagen. Para contar palabras con tildes: `LC_ALL=C.UTF-8 wc -w`.

---

## 10. Lecciones que costaron caras

**Del OCR (Correos).** La tipografía de Correos dibuja el 9 de forma que el
reconocedor lee **4**. **Ninguna lente lo ve**, porque el volcado corrupto valida
la copia corrupta. Sólo se caza mirando la página impresa. Si una oposición
obliga a reconocer ópticamente, **toda cifra que importe se verifica a ojo** y se
anota en un `correcciones.tsv`. Y ojo con el número de página: el que da el
volcado no es el folio impreso.

**De los cuadernillos (Administrativo C1).**
- Las **preguntas de reserva vuelven a numerarse desde el 1** dentro de cada
  parte: sin marcarlas, «primera parte nº 3» son dos preguntas y el acta no puede
  apuntar a ninguna.
- El rótulo «Preguntas de reserva» **se pegaba dentro de la opción d)** de la
  última pregunta de cada sección y hacía pasar por distintas once preguntas
  iguales.
- Un modelo **imprime dos veces el 66 y ningún 65**; la plantilla lo reconoce en
  una nota al margen. El corte de pregunta nueva va por número correlativo **o**
  por pregunta anterior completa.
- Hay preguntas cuyas cuatro opciones son «1.», «2.», «3.» y «4.»: un «4.» suelto
  puede ser opción, no pregunta.
- Una opción que acaba en cifra («30.000.000 KB.») se traga el número de la
  pregunta siguiente.
- **La pregunta se identifica por enunciado más las cuatro opciones**: dos
  preguntas distintas compartían el enunciado «¿Cuál de las siguientes
  afirmaciones es verdadera?».

**De las plantillas.** Las **provisionales pueden cambiar**: hay que volver a
mirar si ha salido la definitiva antes de dar por buenas las respuestas. Las
**anuladas** son un registro de defectos firmado por el tribunal: el enunciado
sigue sirviendo para estudiar, la respuesta no, y se dice. Y **las plantillas se
equivocan**: en RTVE, diez respuestas oficiales de 2024 estaban mal y van
marcadas una a una con lo que las desmiente. **El temario enseña la norma, no la
plantilla, y dice dónde está la costura.**

**De los temas compartidos.** Cuando un tema pasa a servir a dos oposiciones,
**se reescribe su cabecera**, no sólo se revisa su cuerpo: ficha, primer
párrafo, fila de portadas, cabecera del esquema e identidad literal del
enunciado en los dos programas.

**De las fuentes que no son norma.** Un documento de empresa, un manual o un plan
no es una norma: **cuando contradice al BOE, manda el BOE**, y el tema lo dice
donde pasa.

**Del fallo que no da error.** Cuatro veces en un mes el problema fue una
comprobación que **no se estaba corriendo sobre todo**. Cuando se arregla algo,
**se busca quién más hace ese mismo trabajo por su cuenta**, por el patrón y no
por el nombre.

**De las respuestas que caducan.** Una fecha de corte congela el texto de una
norma, pero no quién ocupa un cargo. Esas respuestas van con su fecha y la
recomendación de comprobarlas.

---

## 11. Operativa

- **De dos en dos.** Cinco temas a la vez agotan la sesión y se pierden a medias.
- **No abarates la investigación**: investigar, redactar y verificar van con el
  modelo bueno. Lo mecánico puede ir barato.
- **Todo a disco, según se produce.** Los avisos de fin de tarea se truncan.
- **Commit y push a menudo.** El contenedor se reinicia sin aviso y el proxy de
  red también: en el Administrativo C1 un volcado de normas se cortó dos veces
  (una por el proxy, otra por un reinicio). Lo que no estaba empujado se habría
  perdido. **Los guiones de lote saltan lo ya hecho**, para poder relanzarlos.
- **No se commitea nada a medias.** `boe.py` escribe el fichero sólo al terminar
  la norma; antes de commitear un lote en marcha se comprueba que no hay ficheros
  parciales.
- **Mira las marcas de tiempo** antes de dar algo por parado o perdido.
- **`ESTADO.md`**: qué es cada temario, dónde vive cada cosa, qué está hecho y qué
  falta. Se actualiza al final de cada sesión.
- **`PENDIENTES.md`**: cualquier sesión anota lo que detecte, con cinco campos
  —dónde, qué dice, qué debería decir (ya redactado), fuente literal, gravedad—.
  Lo aplicado se tacha con fecha, no se borra.
- **Los informes llevan su bloque de siglas** al principio y pasan
  `refutar_prosa.py`.
- **Cada número de un informe sale de correr la herramienta** el día del informe,
  no de lo anotado al escribir.

---

## 12. Preferencias del proyecto

- Todo en **español**.
- **No se sube nada a Google Drive.**
- **No se abre pull request** si no se pide expresamente.
- Cada oposición en **su propia rama**; la de Correos y el Administrativo C1 es
  `claude/correos-oposiciones-temarios`.
- **La autoría y los términos de uso** de la página de créditos, y **la consulta
  legal** sobre reproducir preguntas de examen ajenas, **están pendientes y los
  decide el titular del proyecto**: no se inventan.

---

## 13. Dónde se quedó cada frente (septiembre de 2026)

| Frente | Estado |
|---|---|
| **RTVE** | 23 volúmenes hechos. **Parado por decisión del titular.** Cuatro ocupaciones sin empezar (Iluminación, Ing. Superior Informática, Ing. Superior Industrial, PRL) y 8 pendientes abiertos en el cuaderno |
| **Correos** | **Cerrado**: 12 temas, 12 esquemas, apéndice psicotécnico, 200 preguntas con remite, seis lentes en cero. Pendiente sólo lo que decide el titular: créditos, logotipo y consulta legal |
| **Administrativo C1 (AGE)** | Sondeo hecho; seis exámenes (2024 y 2025) en la bóveda; programa literal de 45 temas; lector con cruce A/B (247 de 247); **acta de 503 preguntas repartidas** sobre los 45 temas, ninguno a cero; **29 de 30 normas volcadas** (falta el Código Civil, una pregunta). **Ningún tema escrito.** Los más preguntados: contratos del sector público (45), procedimiento administrativo común (38), provisión de puestos (33). La plantilla definitiva de 2025 aún no estaba publicada |
