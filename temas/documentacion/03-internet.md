# Tema 3 del específico de Documentación · Internet

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Documentación · punto 3 |
| **Sirve para** | **Documentación** |
| **Fuente** | **Sin norma en el enunciado**, y con las cuatro clases de fuente del proyecto detrás: el **Real Decreto 635/2015** del depósito legal en línea y la **Sentencia 27/2020 del Tribunal Constitucional**, las dos publicadas en el BOE; la especificación **EBU Tech 3293** y la documentación del **W3C**; y las páginas de ayuda de los propios buscadores |
| **Identificador** | `BOE-A-2015-8338` · `BOE-A-2020-4112` · `EBU Tech 3293 v.1.10` · RDF Primer del **W3C** |
| **Redacción que se estudia** | El **real decreto en su texto vigente al 21/12/2022**, la **sentencia tal como la publicó el BOE**, la especificación en su **versión 1.10, de abril de 2020**, y las páginas **tal como estaban el 02/09/2026** |
| **Aviso sobre las fuentes** | De sus **8 preguntas**, **6 se verifican en documento**: dos en el BOE, una en la especificación de la Unión Europea de Radiodifusión, una en la documentación del W3C y dos en la ayuda de los propios buscadores. Las **2 restantes** —la expresión booleana y el año de una red social— se apoyan **sólo en la plantilla oficial**, y van marcadas |
| **Extensión** | **4.672 palabras** |

<!-- /portada -->

**El enunciado de este punto es el más cargado de siglas de todo el programa, y conviene traerlas
presentadas.** Son el consorcio que normaliza la web (**W3C**), el sistema simple de organización del
conocimiento (**SKOS**), el marco de descripción de recursos (**RDF**), el lenguaje de ontologías web
(**OWL**), el conjunto de metadatos de la unión europea de radiodifusión, que se nombra con sus siglas
inglesas (**EBU**) y da nombre al conjunto (**EBUCore**), el modelo
conceptual de datos por clases (**CCDM**) y el contenido generado por el usuario (**UGC**). Aparecen
además, en el cuerpo del tema, el lenguaje de marcado extensible (**XML**), el localizador uniforme
de recursos (**URL**) y el protocolo de transferencia de hipertexto (**HTTP**), que son las tres
opciones falsas de una de sus preguntas.

> **Enunciado de la convocatoria (Anexo 2, temario específico de Documentación, punto 3):**
> «INTERNET: 3.1. Internet y la WWW. Protocolos de Internet. World Wide Web Consortium · 3.2. La web
> semántica; recomendaciones del W3C. SKOS. RDF / OWL · 3.3. Modelos de metadatos: DublinCore, P
> Meta, EBUCore · 3.4. EBU Class Conceptual Data Model (CCDM) · 3.5. Lenguajes de marcado · 3.6.
> Datos enlazados · 3.7. Buscadores, metabuscadores · 3.8. Redes sociales, YouTube y contenido
> generado por el usuario (UGC).»

**Ocho preguntas**, y un tema que se lee mejor al revés de como está escrito el enunciado: **el
examen no preguntó por los protocolos ni por los lenguajes de marcado**, sino por **cómo se busca**,
**cómo se describe** y **qué se puede hacer con lo que otros publican**. De esas tres cosas, las dos
últimas tienen documento detrás, y una de ellas es **una sentencia del Tribunal Constitucional**.

| Nivel | Qué sostiene en este tema |
|---|---|
| **1 · Norma del BOE** | El **Real Decreto 635/2015**: qué sitios web son objeto de depósito legal —**cualquiera que sea el dominio**— y cuáles quedan excluidos. Y la **Sentencia 27/2020**, que fija la doctrina sobre el uso por terceros de lo que un particular publica en una red social |
| **2 · Organismo de normalización** | La documentación del **W3C** sobre **RDF** y los datos enlazados, y la especificación **EBU Tech 3293** del conjunto de metadatos **EBUCore** |
| **3 · Documentación del propio servicio** | La ayuda de **Búsqueda de Google**, que publica sus operadores, y la página de **DuckDuckGo** sobre sus atajos |
| **5 · La plantilla oficial** | La **expresión booleana** de la primera pregunta y el **año de lanzamiento de una red social**. Van marcados |

---

<!-- indice -->

## Índice

- [1. Buscar](#1-buscar)
  - [1.1 La lógica booleana](#11-la-lógica-booleana)
  - [1.2 Los operadores de Google](#12-los-operadores-de-google)
  - [1.3 DuckDuckGo y los bangs](#13-duckduckgo-y-los-bangs)
- [2. Describir: los datos enlazados y RDF](#2-describir-los-datos-enlazados-y-rdf)
- [3. Describir audiovisual: EBUCore](#3-describir-audiovisual-ebucore)
- [4. Guardar la web: el archivo y el depósito legal](#4-guardar-la-web-el-archivo-y-el-depósito-legal)
- [5. Usar lo ajeno: la doctrina del Tribunal Constitucional](#5-usar-lo-ajeno-la-doctrina-del-tribunal-constitucional)
- [6. Las redes sociales y sus fechas](#6-las-redes-sociales-y-sus-fechas)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Buscar

### 1.1 La lógica booleana

**La respuesta oficial**: para localizar información sobre obras de teatro y novelas que han sido
adaptadas para cine o televisión, la expresión es **(teatro OR novela) AND (cine OR televisión)**.

**La pregunta mide una sola cosa: dónde va cada operador.** Y se resuelve traduciendo el enunciado
palabra por palabra:

| Lo que pide el enunciado | Cómo se escribe |
|---|---|
| «obras de teatro **y** novelas» — es decir, **de cualquiera de las dos clases** | **teatro OR novela** |
| «adaptadas para cine **o** televisión» — **en cualquiera de los dos medios** | **cine OR televisión** |
| El documento tiene que cumplir **las dos condiciones a la vez** | Las dos cadenas unidas por **AND** |

**Ahí está la trampa, y es de lengua antes que de lógica**: el «y» del castellano corriente
—«teatro y novelas»— **no es el AND booleano**. Cuando decimos «obras de teatro y novelas» queremos
decir «obras que sean de teatro **o** que sean novelas», no «obras que sean las dos cosas a la vez».
Quien traduzca «y» por AND pide documentos que hablen **simultáneamente** de teatro y de novela, y
pierde casi todo.

Las tres opciones falsas, y qué le pasa a cada una:

- **(teatro AND novela) AND (cine AND televisión)** — traduce los dos «y» como AND. Exige que el
  documento trate **las cuatro cosas a la vez**: es **la más restrictiva posible**, y devolverá casi
  nada.
- **teatros AND novelas AND cine OR televisión** — **sin paréntesis**. Y sin paréntesis el orden de
  evaluación decide el resultado: la expresión ya no significa lo que parece. **La ausencia de
  paréntesis es el error, no los operadores.**
- La que mete un **operador de proximidad** (así se llama a los que exigen que dos palabras estén
  cerca en el texto): **teatro AND novela NEAR cine OR televisión**. Ni hace falta la proximidad, ni
  hay paréntesis.

**La regla de examen**: **OR agrupa sinónimos y alternativas; AND cruza condiciones distintas; los
paréntesis dicen en qué orden**. Y una comprobación rápida: **una expresión booleana bien escrita
para este enunciado tiene que tener dos OR y un AND**, en ese orden. Sólo una opción lo cumple.

**Nivel de la fuente**: **plantilla oficial**. La lógica booleana no está normalizada en ninguna de
las fuentes reunidas; lo más cerca que se llega es la norma de tesauros, que al definir la
postcoordinación pone como ejemplo la expresión «**microwaves AND radiation**», y ahí el AND cruza
dos conceptos distintos, que es exactamente lo que hace aquí.

### 1.2 Los operadores de Google

**La respuesta oficial**: para recuperar documentos de un formato concreto (el que la pregunta usa es
el **PDF**) se escribe **filetype:pdf**.

**Y lo dice la ayuda del propio buscador**, que publica la lista de sus operadores: «**Para encontrar
documentos de un tipo de archivo concreto: escribe filetype: delante del tipo de archivo**», con el
ejemplo «**efecto fotoeléctrico publicación filetype:pdf**».

La misma página da **la regla de sintaxis que más veces se falla en la práctica**: «**No incluyas
espacios entre el operador y el término de búsqueda**», y lo ilustra con el otro operador famoso:
«**La búsqueda [ site:elmundo.es ] funciona, pero la búsqueda [ site: elmundo.es ], no**».

Las tres opciones falsas merecen mirarse una a una, porque **sólo una de las cuatro es un invento**:

| Opción falsa | Qué pasa con ella |
|---|---|
| **site:pdf** | **`site:` existe y funciona**, pero **restringe por sitio o dominio**, no por formato. Escrito así pediría documentos del dominio «pdf», que no existe. **Es el distractor bueno**: mezcla un operador real con el argumento equivocado |
| **source:pdf** | No aparece en la lista de operadores de la ayuda de Google. Sí existe **en Google Noticias**, para restringir por medio, que es de donde viene la confusión |
| **format:pdf** | **Es el invento**: parece el más lógico en castellano —«formato»— y no existe |

**La regla**: el operador de Google **no se llama como el concepto, se llama como el atributo del
fichero**: `filetype`, tipo de fichero.

### 1.3 DuckDuckGo y los bangs

**La respuesta oficial**: DuckDuckGo es **un motor de búsqueda en Internet que usa atajos llamados
Bangs**.

**Y lo explica su propia página**: «**Bangs are shortcuts that quickly take you to search results on
other sites**» —atajos que te llevan rápidamente a los resultados de búsqueda **en otros sitios**—.
Con un ejemplo: «**A search for !w filter bubble will take you directly to Wikipedia**».

Dos datos más de la misma página, que son los que explican por qué la pregunta los llama «atajos» y
no «operadores»:

- **Antigüedad**: «**We've had bangs since 2008 as part of our geek roots**».
- **Y la advertencia que el buscador se hace a sí mismo**: «**because your search is actually taking
  place on that other site, you are subject to that site's policies, including its data collection
  practices**». Es decir: **el bang saca al usuario del buscador**, y con él, de su política de
  privacidad. Para un buscador que se vende por no rastrear, decirlo es significativo.

**Y ese detalle resuelve la opción falsa más fina**: «**un metabuscador** centrado en contenidos de
Estados Unidos». **DuckDuckGo no es un metabuscador**, y la diferencia está justo en lo que dice esa
frase: **un metabuscador consulta varios buscadores y agrega los resultados en su propia página**;
el bang hace lo contrario, **te manda al otro sitio y allí se queda la búsqueda**. Las otras dos
opciones —un sitio de gastronomía, el nombre original de otro buscador— no juegan.

---

## 2. Describir: los datos enlazados y RDF

**La respuesta oficial**: los datos enlazados se basan en un concepto llamado **RDF (Resource
Description Framework)**.

La documentación del consorcio que normaliza la web lo define así: «**The Resource Description
Framework (RDF) is a framework for expressing information about resources**» —un marco para expresar
información sobre recursos—, y aclara qué cuenta como recurso: «**Resources can be anything,
including documents, people, physical objects, and abstract concepts**».

**Y el enlace con la pregunta es literal.** El mismo documento explica que, teniendo el identificador
de una cosa, se puede ir a buscar más datos sobre ella y sobre las cosas con las que se relaciona, y
concluye: «**Such uses of RDF are often qualified as Linked Data**» —esos usos de RDF son los que
suelen llamarse datos enlazados—.

**Por qué las otras tres no**, y merece la pena porque las cuatro son reales y las cuatro se usan en
la web:

| Sigla | Qué es | Por qué no es la base de los datos enlazados |
|---|---|---|
| **URL** | El **localizador** de un recurso | Es **la dirección**, no el modelo. Los datos enlazados **usan** direcciones, pero una dirección sola no dice nada sobre lo que hay al otro lado |
| **XML** | Un **lenguaje de marcado** | Es **una sintaxis**, una manera de escribir. RDF **puede escribirse en XML**, pero también en otras sintaxis: **el modelo no es el lenguaje** |
| **HTTP** | El **protocolo de transferencia** | Es **el transporte**. Mueve los datos; no dice qué significan |

**La regla que ordena las cuatro**: **HTTP transporta, URL localiza, XML escribe y RDF significa**.
La pregunta pide el que da **el significado**, que es el único que puede sostener un enlace entre
datos de fuentes distintas.

**Nivel de la fuente**: **W3C**, con una precisión que hay que hacer. La página del consorcio
responde «prohibido» a toda consulta automática, **también con agente de usuario de navegador**, de
modo que **no se ha podido leer la recomendación vigente a la fecha de corte**. Lo que sí está
abierto es **el repositorio de edición del propio consorcio**, donde se publica la versión de trabajo
del mismo documento, y de ahí salen las citas. El propio texto advierte de que los cambios respecto
de la versión anterior van **en un documento aparte**: **lo que aquí se cita —el desarrollo de la
sigla y la relación con los datos enlazados— no está entre ellos**.

---

## 3. Describir audiovisual: EBUCore

**La respuesta oficial**: el conjunto de metadatos EBUCore **es un conjunto abierto y puede adaptarse
a distintas necesidades**.

**Es la pregunta mejor servida del tema**, porque la especificación de la Unión Europea de
Radiodifusión **desmiente las tres opciones falsas una por una**, y con frases suyas.

**La opción correcta está en la primera línea del documento**, entrecomillada por sus propios
autores: «**'The EBUCore is a metadata specification designed for users with different needs'**»
—diseñada para usuarios con necesidades distintas—. Y más adelante lo desarrolla: «**EBUCore has been
designed to support customisation in many ways**», con **dos mecanismos de extensión** —«**EBUCore
provides two mechanisms for extensions**»— basados en la redefinición de tipos complejos del esquema.

Ahora las tres falsas:

- «**No permite describir audios**». La segunda frase del documento dice lo contrario: «**EBUCore has
  been designed to describe audio, video and other resources for a wide range of broadcasting
  applications**». Y la versión leída va más lejos: incorpora el modelo de datos de audio de la unión
  internacional de telecomunicaciones (que la especificación nombra con sus siglas inglesas):
  «**a unique representation of the ITU-R BS.2076 Audio Data Model (ADM)**». **Describir audio no es que lo permita: es que lo hace con la
  norma de audio encima.**
- «**Está indicado únicamente para su uso en Archivos**». La misma frase lo desmiente: las
  aplicaciones que enumera son «**archives, exchange and production**» —archivo, intercambio y
  producción—, y añade que «**EBUCore facilitates programme exchanges between broadcasters or between
  production facilities in distributed and cloud environments**» y que «**Beyond production, EBUCore
  can be used to describe content for distribution**». **Tres ámbitos, y el archivo es sólo uno.**
- «**No permite describir partes o fragmentos de documentos**». La especificación **le dedica un
  apartado entero al elemento «part»**, y una de sus preguntas frecuentes es exactamente ésa: «**Can
  I use the 'part' element to fragment my data? Yes.**» Y remata: «**The 'part' element is extremely
  versatile**», con ejemplos que van de los segmentos de tiempo de una escena a los episodios de una
  serie —«**EBUCore can be used to describe a series or season, each part describing an episode of
  that series or season**»—.

**Lo que sale gratis del mismo documento, y que el enunciado del temario pide**: que «**EBUCore is
based on the Dublin Core to maximise interoperability**» —de ahí que el programa cite los dos
juntos—; que «**The core set of metadata presented in EBUCore is the Dublin Core for media**»; que la
versión leída «**takes into account latest developments in the Semantic Web and Linked Open Data
communities**», lo que la enlaza con el epígrafe anterior; y que su ontología «**has been updated to
match EBU's CCDM (Tech 3351) needs**», que es **el otro punto del temario**, el modelo conceptual de
datos.

---

## 4. Guardar la web: el archivo y el depósito legal

**La respuesta oficial**: el Archivo de la Web Española **intenta guardar la mayor cantidad posible
de información web, con un modelo mixto, que combina recolecciones masivas y selectivas**.

**La página del archivo no se ha podido consultar** —la biblioteca que lo mantiene responde
«prohibido» a toda consulta automática, comprobado por cinco rutas con agente de usuario de
navegador—. Pero **la norma que lo ordena sí está en el BOE**, y con ella se descartan **las tres
opciones falsas con texto delante**.

**Artículo 3 del Real Decreto 635/2015.** Son objeto de depósito legal «**todo tipo de sitios web y
las publicaciones en ellos contenidas –tanto de acceso libre como restringido–; cualquiera que sea
el procedimiento de producción, edición o difusión; cualquiera que sea el soporte o medio no tangible
por el que sean distribuidas o comunicadas; cualquiera que sea la localización física del servidor o
servidores a partir de los cuales se difunden a las redes electrónicas; y cualquiera que sea el
dominio que albergue la publicación**», siempre que contengan patrimonio de las culturas de España y
cumplan **una** de estas tres condiciones: «**a) Que estén en cualquiera de las lenguas españolas
oficiales; b) Que estén producidas o editadas por cualquier persona física o jurídica que tenga su
domicilio, residencia o establecimiento permanente en España; c) Que estén producidas o editadas bajo
un nombre de dominio vinculado al territorio español**».

**Ese «cualquiera que sea el dominio» mata la primera opción falsa**, la que decía que sólo se
recopila lo alojado en el dominio `.es`. La ley dice justo lo contrario: **el dominio español es sólo
una de las tres puertas de entrada**, y las otras dos son la lengua y el domicilio del editor.

**Artículo 4.** Las publicaciones excluidas son sólo tres, y la lista se abre con una salvedad que
conviene no perder —«**Sin perjuicio de las exclusiones a que hace referencia el artículo 5 de la Ley
23/2011, de 29 de julio**», que es la ley de depósito legal y tiene las suyas—: «**a) Los correos y
la correspondencia privada. b) Los contenidos que estén albergados únicamente en una red privada. c)
Los ficheros de datos de carácter personal a los que solo tiene acceso un grupo restringido de
personas**». **Los medios de comunicación no están en la lista**, y con eso cae la segunda opción
falsa —la que decía que no se recopilan cabeceras de prensa, agencias ni cadenas porque «mantienen
sus propios archivos»—. **Que un editor conserve lo suyo no le exime.**

**Artículo 1**, apartado 3. Y lo mismo vale para quien ya depositó el papel: «**El depósito de una
misma publicación en soporte tangible no exime del depósito de la misma en línea**».

**Artículo 6.** Y aquí está el criterio que sostiene la respuesta correcta. Su apartado 1 nombra a
los responsables —«**son centros de conservación la Biblioteca Nacional de España y los que
determinen las Comunidades Autónomas en el ámbito de sus competencias**»—, y su apartado 2 les dice
cómo elegir: «**determinarán qué sitios web y qué recursos son los que se capturarán o depositarán
para ser conservados y poder así facilitar su consulta**», «**siguiendo el criterio de lograr la
mejor representatividad del mundo de Internet y de conseguir una recolección lo más completa posible
de publicaciones tales como libros y revistas electrónicos**».

**Léase despacio, porque son los dos términos del modelo mixto**: «**lo más completa posible**» es la
recolección **masiva** —barrer automáticamente cuanto se alcance—; «**la mejor representatividad**»
es la **selectiva** —elegir qué sitios merecen una captura más cuidada—. **Las dos cosas a la vez**,
que es exactamente lo que dice la opción correcta.

**Artículo 7.** Y el apartado que convierte ese criterio en un plan de trabajo, con una salvedad
delante: «**Sin perjuicio de lo establecido en la disposición adicional segunda, los procedimientos
de selección y captura de las publicaciones en línea** […] **así como la frecuencia con la que se
realizarán dichas capturas, serán establecidos** […] **por la Biblioteca Nacional de España, centro
de conservación de ámbito estatal, y por los centros de conservación de las comunidades autónomas**».
**Selección, captura y frecuencia**: las tres palabras del modelo mixto, y las fija la propia
biblioteca.

**Artículo 2.** Y la definición de cómo se hace, que explica por qué esto es un archivo y no una
descarga: «**Captura: Identificación y recolección de sitios web a partir del empleo de programas
informáticos que llevan a cabo un proceso de seguimiento de enlaces con el fin de archivar los
contenidos que conforman un recurso web determinado**». **Seguimiento de enlaces**: el robot entra
por una página y va tirando del hilo.

La cuarta opción —«recopila archivos en la nube»— **confunde el objeto con el sitio donde se
guarda**, y no dice nada.

---

## 5. Usar lo ajeno: la doctrina del Tribunal Constitucional

**La respuesta oficial**: según el Tribunal Constitucional, un contenido generado por un usuario no
público y puesto en redes sociales **puede usarse, en general, sólo con el consentimiento previo y
expreso de su titular**.

Ésta es **la pregunta con la fuente más sólida de todo el bloque**, y conviene decirlo porque parecía
lo contrario: la doctrina está en la **Sentencia 27/2020, de 24 de febrero**, publicada en el BOE. El
caso: un diario provincial ilustró la noticia de un suceso violento con **la fotografía de la
víctima tomada de su perfil de Facebook**, un perfil **abierto y accesible al público**. El diario
alegó libertad de información. **El Tribunal desestimó su amparo.**

**El argumento del periódico y su respuesta** son el núcleo de la pregunta. El diario sostenía que
publicar la propia imagen en una red social «**constituye una suerte de consentimiento tácito para su
posterior utilización por terceros**». La sentencia contesta: «**No podemos aceptar esta premisa. El
consentimiento solo ampara aquello que constituye el objeto de la declaración de voluntad. El titular
del derecho fundamental debe autorizar el concreto acto de utilización de su imagen y los fines para
los que la otorga**».

**Y desarrolla la consecuencia práctica, que es la que hay que llevar sabida**: «**El consentimiento
prestado, por ejemplo, para la captación de la imagen no se extiende a otros actos posteriores, como
por ejemplo su publicación o difusión. De la misma manera debe entenderse que la autorización de una
concreta publicación no se extiende a otras, ya tengan la misma o diversa finalidad que la
primigenia**».

Sobre el carácter **abierto** del perfil —que es lo que el enunciado llama «puesto en redes
sociales»—, la sentencia recoge y hace suyo el razonamiento del Tribunal Supremo: «**el
consentimiento del titular de la imagen para que el público en general, o un determinado número de
personas, pueda ver su fotografía en un blog o en una cuenta abierta en la web de una red social no
conlleva la autorización para hacer uso de esa fotografía y publicarla o divulgarla de una forma
distinta**», porque no es «**el 'consentimiento expreso' que prevé el art. 2.2 de la Ley Orgánica
1/1982 como excluyente de la ilicitud de la captación, reproducción o publicación de la imagen de una
persona**».

**Y una precisión que evita el error contrario**: ese consentimiento expreso **no tiene que ser
formal**. La propia sentencia lo dice: el precepto «**no requiere que sea un consentimiento formal
(por ejemplo, dado por escrito), sí exige que se trate de un consentimiento inequívoco**».

Las tres opciones falsas, y por qué cada una es exactamente lo que el Tribunal rechaza:

| Opción falsa | Qué dice la sentencia |
|---|---|
| «Implica que el sujeto **consiente en ser observado en cualquier soporte**» | Es **la tesis del periódico**, rechazada: el consentimiento «solo ampara aquello que constituye el objeto de la declaración de voluntad» |
| «Puede usarse siempre **en las primeras 24 horas**» | **No hay plazo de gracia en ninguna parte.** El consentimiento se refiere al **acto concreto**, no al momento |
| «Puede usarse siempre que se incluya **un rótulo con autoría o procedencia**» | **Citar la fuente no sustituye al consentimiento**: son cosas distintas, y la sentencia exige autorizar «el concreto acto de utilización» |

**Por qué esta pregunta está en el tema de Internet y no en el de Constitución.** Porque lo que
resuelve no es el contenido del derecho a la propia imagen, que es materia constitucional, sino **qué
se puede hacer con el contenido generado por el usuario**, que es el último punto del enunciado de
este tema. Y para un puesto de documentación en una televisión pública es **la regla de trabajo más
directamente aplicable de todo el bloque**: la imagen que un particular cuelga en su perfil **no es
material de archivo disponible**.

---

## 6. Las redes sociales y sus fechas

**La respuesta oficial**: la red social conocida hoy como «X» **se lanzó en 2006**.

**Es la única pregunta del tema que no se ha podido verificar en fuente**, y conviene contar hasta
dónde se llegó. La página institucional actual de la compañía **abre y no da la fecha**: describe la
empresa y sus prioridades, y no cuenta su historia. La antigua página corporativa —la que tenía la
sección «quiénes somos»— **responde «no existe»**. Y el organismo regulador de los mercados
estadounidenses, donde estaría el folleto de salida a bolsa de la compañía, **exige identificarse con
un correo de contacto** para consultar su archivo, y **este proyecto no envía la dirección de su
usuario a servicios ajenos**. Comprobado con agente de usuario de navegador.

**De modo que el año se recoge de la plantilla oficial y va marcado.** Lo que sí se puede razonar
—y ayuda en un examen— es el orden relativo de las opciones: **2004 es demasiado pronto** para una
red de mensajes cortos, que es posterior a la primera generación de redes sociales; **2010 es
demasiado tarde**, porque para entonces el servicio ya era masivo. Entre 2006 y 2007, **el examen
elige el primero**.

**Y hay un dato de este mismo tema que sirve de referencia**: el buscador que la pregunta 96 nombra
declara que tiene sus atajos «**since 2008**». Son años vecinos y de la misma oleada de servicios
web, y tenerlos juntos ayuda a colocarlos.

---

## 7. Los datos que el examen ha preguntado

Ocho preguntas. Todas se contestan con el tema delante:

| Materia | Dato preguntado | Nivel |
|---|---|---|
| Buscadores | La expresión es **(teatro OR novela) AND (cine OR televisión)** | Plantilla oficial |
| Datos enlazados | Se basan en **RDF** | **W3C**, documentación de RDF |
| Contenido de usuario | Sólo con **consentimiento previo y expreso** del titular | **BOE**, Sentencia 27/2020 |
| Buscadores | Para PDF, **filetype:pdf** | **Google**, ayuda oficial |
| Redes sociales | La red hoy llamada «X» se lanzó en **2006** | Plantilla oficial |
| Metadatos | **EBUCore** es un conjunto **abierto y adaptable** | **EBU Tech 3293** |
| Archivo web | Modelo **mixto**: recolecciones **masivas y selectivas** | Plantilla (**RD 635/2015** para el marco) |
| Buscadores | DuckDuckGo usa atajos llamados **Bangs** | **DuckDuckGo**, página oficial |

**Lo que no se ha preguntado y sale gratis del mismo tema**: que en Google **no puede haber espacio
entre el operador y el término**; que `site:` restringe **por sitio**, no por formato; que un **bang
saca la búsqueda del buscador** y con ella su política de privacidad; que **RDF puede escribirse en
XML pero no es XML**; que **EBUCore se basa en Dublin Core** y que su ontología se actualizó para
encajar con el **modelo conceptual de datos** que el propio temario cita; que el depósito legal
alcanza a los sitios «**cualquiera que sea el dominio**» y excluye sólo **tres** clases de
publicación; y que el consentimiento del artículo 2.2 de la Ley Orgánica 1/1982 **no tiene que ser
escrito, pero sí inequívoco**.

---

## 8. Trazabilidad

- **Real Decreto 635/2015, de 10 de julio**, por el que se regula el depósito legal de las
  publicaciones en línea, `BOE-A-2015-8338`, **texto vigente al 21 de diciembre de 2022**: el
  artículo 1 —objeto—, el 2 —definición de captura—, el 3 —publicaciones objeto de depósito—, el 4
  —exclusiones—, el 6 —centros de conservación y criterio de captura— y el 7 —procedimientos,
  selección y frecuencia—.
- **Sentencia 27/2020, de 24 de febrero, del Tribunal Constitucional**, Sala Segunda, recurso de
  amparo 1369-2017, publicada como `BOE-A-2020-4112` en el BOE núm. 84, de **26 de marzo de 2020**:
  la síntesis, el resumen y los fundamentos sobre el consentimiento y las redes sociales.
- **EBU Tech 3293, «EBU Core Metadata Set (EBUCore) Specification», versión 1.10**, Ginebra, **abril
  de 2020**, descargada el **3 de septiembre de 2026**: la introducción, la sección de
  personalización y extensiones y el apartado dedicado al elemento «part».
- **RDF Primer del W3C**, edición de trabajo publicada en el repositorio de edición del consorcio,
  leída el **3 de septiembre de 2026**: la definición de RDF y su relación con los datos enlazados.
- **«Acotar las búsquedas de Google»**, ayuda oficial de Búsqueda de Google, leída el **3 de
  septiembre de 2026**: la lista de operadores, el de tipo de fichero y la regla de los espacios.
- **«!Bangs»**, página oficial de DuckDuckGo, leída el **3 de septiembre de 2026**: qué son los
  bangs, el ejemplo, su antigüedad y la advertencia sobre la política del sitio de destino.

**Lo que este tema no puede sostener, y por eso lo dice:**

- **El año de lanzamiento de la red social se recoge de la plantilla.** Tres rutas probadas con
  agente de navegador; la única que daría el dato con respaldo documental **exige enviar un correo de
  contacto**, y este proyecto **no envía la dirección de su usuario a servicios ajenos**.
- **La página del Archivo de la Web Española no se ha podido consultar**: la biblioteca que lo
  mantiene responde «prohibido», comprobado por **cinco rutas** con agente de navegador. Lo que el
  tema afirma del modelo mixto se apoya en **los artículos 6 y 7 del real decreto**, no en la
  descripción del propio archivo.
- **La documentación del W3C se ha leído en su repositorio de edición, no en la página del
  consorcio**, que responde «prohibido». Es **la versión de trabajo posterior** a la vigente al
  corte; el propio texto remite los cambios a un documento aparte, y **lo que aquí se cita no está
  entre ellos**.
- **La expresión booleana se apoya sólo en la plantilla.** Lo que el tema añade —cómo se traduce el
  «y» del castellano y por qué los paréntesis deciden— es **razonamiento, no cita**.
- **Lo que el tema dice de `source:` en el buscador de noticias es uso profesional**: no aparece en
  la ayuda consultada.
