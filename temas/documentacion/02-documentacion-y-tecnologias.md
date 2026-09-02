# Tema 2 del específico de Documentación · Documentación y tecnologías de la información

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Documentación · punto 2 |
| **Sirve para** | **Documentación** |
| **Fuente** | **Sin norma en el enunciado**, y con dos clases de fuente detrás: las **normas ISO del comité de información y documentación** —**ISO 25964** para los tesauros y los códigos normalizados de identificación— y la **Ley 16/1985 del Patrimonio Histórico Español**, que es la que define en el BOE qué es un documento y qué puede destruirse |
| **Identificador** | `ISO 25964-1:2011` · `ISO 25964-2:2013` · `ISO 15707:2022` · `BOE-A-1985-12534` |
| **Redacción que se estudia** | Las **normas ISO en la edición que se cita en cada caso**, leídas en **su muestra oficial** el **03/09/2026**, y la **ley en su texto vigente al 21/12/2022** |
| **Aviso sobre las fuentes** | De sus **9 preguntas**, **4 tienen norma internacional detrás**, leída en la muestra oficial del propio documento, y **1 más se apoya en la ley del patrimonio**. Las **4 restantes** —el modelo probabilístico, el resumen indicativo, la curación de contenidos y la redacción digital— se apoyan **sólo en la plantilla oficial**, y van marcadas. **El texto íntegro de las normas ISO es de pago**, y aquí se dice qué parte se ha podido leer |
| **Extensión** | **4.850 palabras** |

<!-- /portada -->

> **Enunciado de la convocatoria (Anexo 2, temario específico de Documentación, punto 2):**
> «DOCUMENTACIÓN Y TECNOLOGÍAS DE LA INFORMACIÓN: 2.1. Documentación: conceptos y fines · 2.2. El
> documento: documento audiovisual, sonoro, textual e imagen fija · 2.3. El proceso documental:
> selección, registro, análisis, recuperación y difusión · 2.4. Lenguajes documentales: listas de
> términos, taxonomías, tesauros, ontologías · 2.5. Las tecnologías de la información y su aplicación
> a los procesos documentales · 2.6. Bases de datos.»

**Seis siglas atraviesan este tema y conviene fijarlas de entrada**, porque no todas se desarrollan
en su propia fuente. Las normas que lo gobiernan las publica el organismo internacional de
normalización (**ISO**), que en sus documentos **no despliega sus iniciales**; la página oficial de
una de ellas la aloja la organización que hace de secretaría de su subcomité (**NISO**), que tampoco
las despliega. Sí se desarrollan, en cambio, el número internacional normalizado de publicaciones
seriadas (**ISSN**), el código internacional normalizado de obras musicales (**ISWC**), el lenguaje
de marcado extensible (**XML**) —así lo escribe la propia norma de tesauros— y el operador booleano
de intersección (**AND**), que aparece dentro de uno de sus ejemplos.

**Nueve preguntas**, y un tema con una peculiaridad que conviene decir en la primera línea: **sus
fuentes buenas son de pago**. Las normas ISO que lo gobiernan no se publican en el BOE ni se regalan;
lo que sí publica ISO gratis es **la muestra oficial de cada norma** —portada, prólogo, índice
completo, introducción, objeto y buena parte de los términos y definiciones—, y **es exactamente
donde están las respuestas de este examen**. Este tema se ha escrito con esas muestras delante, y
dice de cuál sale cada dato.

| Nivel | Qué sostiene en este tema |
|---|---|
| **1 · Norma del BOE** | La **Ley 16/1985 del Patrimonio Histórico Español**: qué es **un documento**, qué forma parte del **Patrimonio Documental** —RTVE incluida— y **qué no se puede destruir** |
| **2 · Organismo de normalización** | **ISO 25964-1:2011** —precoordinación y postcoordinación, vocabulario controlado, indización, recuperación—; **ISO 25964-2:2013** —los **modelos estructurales** de interoperabilidad—; **ISO 15707:2022** —el **ISWC**— y la designación exacta de los demás códigos |
| **3 · Documentación institucional** | La **página oficial de ISO 25964** alojada por **NISO**, secretaría del comité, y la del **Centro Internacional del ISSN**, que publica la lista de códigos normalizados con su número de norma |
| **5 · La plantilla oficial** | El **modelo probabilístico** y el teorema de Bayes, el **resumen indicativo**, la **curación de contenidos** y la **redacción digital**. Van marcados |

---

<!-- indice -->

## Índice

- [1. Qué es un documento, y quién lo dice](#1-qué-es-un-documento-y-quién-lo-dice)
  - [1.1 La definición técnica](#11-la-definición-técnica)
  - [1.2 La definición legal, y por qué le afecta a RTVE](#12-la-definición-legal-y-por-qué-le-afecta-a-rtve)
- [2. El proceso documental](#2-el-proceso-documental)
  - [2.1 La selección](#21-la-selección)
  - [2.2 El análisis: el resumen](#22-el-análisis-el-resumen)
  - [2.3 La recuperación: los modelos clásicos](#23-la-recuperación-los-modelos-clásicos)
  - [2.4 La difusión: la curación de contenidos](#24-la-difusión-la-curación-de-contenidos)
- [3. Los lenguajes documentales](#3-los-lenguajes-documentales)
  - [3.1 Precoordinación y postcoordinación](#31-precoordinación-y-postcoordinación)
  - [3.2 Qué es un tesauro, y qué norma lo rige](#32-qué-es-un-tesauro-y-qué-norma-lo-rige)
  - [3.3 La interoperabilidad: los tres modelos y la excepción](#33-la-interoperabilidad-los-tres-modelos-y-la-excepción)
- [4. Los códigos normalizados de identificación](#4-los-códigos-normalizados-de-identificación)
- [5. Las tecnologías en la redacción](#5-las-tecnologías-en-la-redacción)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Qué es un documento, y quién lo dice

### 1.1 La definición técnica

El punto 2.2 del temario pide distinguir **documento audiovisual, sonoro, textual e imagen fija**, y
la norma de tesauros da la definición que sirve para los cuatro a la vez. **ISO 25964-1:2011**, en su
apartado 2.15, define *document* como «**any resource that can be classified or indexed in order that
the data or information in it can be retrieved**» —cualquier recurso que pueda clasificarse o
indizarse para poder recuperar los datos o la información que contiene—.

Y añade, en la nota, la lista que hace innecesaria cualquier tipología: la definición cubre
«**written and printed materials in paper or microform versions**», los ejemplos que da entre
paréntesis —libros, revistas, diagramas, mapas—, y también «**non-printed media such as
machine-readable and digitized records, Internet and intranet resources, films, sound recordings,
people and organizations as knowledge**» —registros digitalizados, recursos de internet, películas,
grabaciones sonoras—.

**Lo que hay que retener de esa definición es lo que no dice.** No dice «papel», no dice «texto» y no
dice «soporte»: dice **recurso que puede indizarse y recuperarse**. Por eso un plano de archivo, un
corte de voz y una fotografía fija son documentos exactamente igual que un guion, y por eso un
archivo audiovisual se gobierna con los mismos principios que uno de papel.

### 1.2 La definición legal, y por qué le afecta a RTVE

La otra definición está en el BOE y **es la que obliga**.

La Ley 16/1985 la da en su artículo cuarenta y nueve —el BOE numera con letra los artículos de esta
ley, y aquí se cita con cifra para poder cotejarlos—.

**Artículo 49**, apartado 1: «**Se entiende por documento, a los efectos de la presente Ley, toda
expresión en lenguaje natural o convencional y cualquier otra expresión gráfica, sonora o en imagen,
recogidas en cualquier tipo de soporte material, incluso los soportes informáticos. Se excluyen los
ejemplares no originales de ediciones**».

**Las dos definiciones se complementan y no se estorban**: la técnica mira **para qué sirve** —para
ser indizado y recuperado—; la legal mira **qué es** —expresión gráfica, sonora o en imagen sobre
cualquier soporte—. Y la legal añade una exclusión que conviene tener: **los ejemplares no originales
de ediciones no son documento** a estos efectos.

El apartado 2 del mismo artículo es el que **mete a RTVE dentro**: «**Forman parte del Patrimonio
Documental los documentos de cualquier época generados, conservados o reunidos en el ejercicio de su
función por cualquier organismo o entidad de carácter público, por las personas jurídicas en cuyo
capital participe mayoritariamente el Estado u otras entidades públicas**». La Corporación es una
sociedad mercantil estatal de capital íntegramente público: **su archivo es Patrimonio Documental
por ministerio de la ley**, no por decisión de la casa.

Y de ahí salen tres reglas que el resto del tema usa:

**Artículo 55**, apartado 1: «**La exclusión o eliminación de bienes del Patrimonio Documental y
Bibliográfico** […] **deberá ser autorizada por la Administración competente**». Y apartado 2: «**En
ningún caso se podrán destruir tales documentos en tanto subsista su valor probatorio de derechos y
obligaciones de las personas o los entes públicos**».

**Artículo 58.** La calificación y utilización de esos documentos «**corresponderá a una Comisión
Superior Calificadora de Documentos Administrativos, cuya composición, funcionamiento y competencias
específicas se establecerán por vía reglamentaria**».

---

## 2. El proceso documental

### 2.1 La selección

**La respuesta oficial**: el principal objetivo de la selección documental en un archivo audiovisual
es **identificar y conservar los documentos de mayor valor patrimonial y utilidad para los usuarios**.

**Es la única de las nueve preguntas cuya respuesta tiene respaldo en el BOE**, aunque sea indirecto,
y merece la pena verlo porque **las tres opciones falsas caen una a una contra la ley**:

| Opción falsa | Por qué no |
|---|---|
| «Conservar **todos** los documentos audiovisuales sin excepción» | **No es selección**: es la ausencia de selección. Y la ley presupone lo contrario al regular la eliminación: **no la prohíbe, la somete a autorización** |
| «**Eliminar todos** los que no cumplan con los estándares de **calidad técnica**» | **El criterio es el equivocado.** La ley no habla de calidad técnica: habla de **valor probatorio de derechos y obligaciones**, y de la **calificación** por una comisión. Un plano rayado de un acontecimiento único es insustituible; uno impecable de un acto repetido, no |
| «**Digitalizar todos** los documentos» | **Confunde selección con preservación.** Digitalizar es un proceso posterior y distinto, y de hecho **la selección es lo que decide qué se digitaliza**, porque digitalizar todo no es viable |

**Los dos criterios de la respuesta correcta son los dos que se usan en un archivo de televisión**:
el **valor patrimonial** —lo que no volverá a existir— y la **utilidad para los usuarios** —lo que se
va a pedir—. El primero mira al pasado y el segundo al futuro, y es su combinación la que ordena.

**Nivel de la fuente**: plantilla oficial para la formulación exacta; **Ley 16/1985 para el marco**,
que es lo que permite descartar las tres opciones falsas con un texto delante.

### 2.2 El análisis: el resumen

**La respuesta oficial**: el tipo de resumen **más breve**, según su nivel de análisis, es el
**resumen indicativo**.

La cadena, de menos a más análisis, es la que el examen presupone:

| Tipo | Qué hace | Extensión |
|---|---|---|
| **Indicativo** | Dice **de qué trata** el documento, sin dar los resultados. Sirve para **decidir si hay que ir al original** | **El más breve** |
| **Informativo** | Da **el contenido**: datos, resultados y conclusiones. Puede **sustituir a la lectura** en muchos casos | Más largo |
| **Analítico** o crítico | Añade **valoración** del documento | El más largo |

**La regla de examen**: cuanto más análisis, más largo. **El indicativo es el que menos analiza y el
que menos ocupa**, y por eso es el que la pregunta busca. La cuarta opción, «resumen objetivo», **no
es un tipo de esta clasificación**: la objetividad es una exigencia de todos ellos, no una categoría.

**Nivel de la fuente**: **plantilla oficial**. La norma que clasifica los resúmenes es **ISO 214**,
«Documentation — Abstracts for publications and documentation», y **no se ha podido consultar**: el
catálogo de ISO responde «prohibido» a toda consulta automática, la tienda de la asociación española
de normalización también, y las tiendas nacionales la ofrecen sólo de pago y sin muestra. Comprobado
con agente de usuario de navegador. **Se dice, y el dato se recoge de la plantilla.**

### 2.3 La recuperación: los modelos clásicos

**La respuesta oficial**: el modelo clásico de recuperación de información que tiene como base el
**teorema de Bayes** es el **modelo probabilístico**.

Los cuatro nombres de la pregunta, y qué separa a cada uno:

- **Modelo booleano**: el documento **cumple o no cumple** la consulta. Se combinan términos con Y, O
  y NO, y el resultado es **un conjunto, no una lista ordenada**. No hay grados: o entra o no entra.
- **Modelo vectorial**: documentos y consulta se representan como **vectores** en un espacio de
  términos, y se ordena por **la semejanza entre ellos** —típicamente el coseno del ángulo—. Aquí sí
  hay grados, pero la medida es **geométrica**.
- **Modelo probabilístico**: el sistema estima **la probabilidad de que un documento sea relevante**
  para la consulta, y ordena por esa probabilidad. **La probabilidad se actualiza con la evidencia**
  —los términos que aparecen, la realimentación del usuario— y ese recálculo es **exactamente lo que
  hace el teorema de Bayes**: pasar de una probabilidad previa a una posterior a la vista de un
  dato nuevo. **Ésa es la razón de la respuesta.**
- **Modelo cognitivo**: **no es uno de los tres clásicos**. Es un enfoque posterior, centrado en el
  usuario y en su estado de conocimiento, y la pregunta lo pone precisamente porque suena a lo que
  «debería» tener que ver con la mente.

**La regla**: de los tres clásicos, **uno no ordena** —el booleano—, **uno ordena por geometría** —el
vectorial— y **uno ordena por probabilidad** —el probabilístico—. Bayes es probabilidad.

**Nivel de la fuente**: **plantilla oficial**. Los cuatro términos se han buscado en todo el corpus
de este proyecto, incluidas las normas ISO reunidas para este tema, y **ninguno aparece**: son
doctrina de recuperación de información, no norma.

### 2.4 La difusión: la curación de contenidos

**La respuesta oficial**: la curación de contenidos es **el proceso que consiste en seleccionar y
compilar información relevante para un tema y un público determinado, con la intención de agregarle
valor y proceder a su difusión**.

**Es una definición larga, y esa es su ventaja**: la opción correcta es la única que contiene **los
cuatro elementos** de la idea, y basta con echarlos de menos en las demás.

| Elemento | Dónde está |
|---|---|
| **Seleccionar y compilar** | Sólo en la correcta. Las otras hablan de **elaborar**, de **conservar** o de **detectar** |
| **Para un tema y un público determinado** | Sólo en la correcta y, a medias, en la de «elaborar contenidos originales» |
| **Agregarle valor** | **Sólo en la correcta.** Es lo que distingue la curación de una simple recopilación |
| **Difusión** | Sólo en la correcta |

Las tres falsas, y qué son en realidad: la primera —seleccionar información **identificada como
falsa**— describe **la verificación**, no la curación; la segunda —**elaborar contenidos
originales**— describe **la creación**, que es justo lo contrario, porque el curador **no crea, elige
lo ajeno**; y la tercera —conservar **soportes obsoletos**— describe **la preservación**, que es otro
proceso del temario.

**La palabra tiene además una trampa de idioma**, y conviene conocerla: en español, *curación* es
sanar; el término viene del inglés *curation*, que es lo que hace **el conservador de un museo**
—elegir, ordenar y presentar—. Quien piense en «curar» irá a la respuesta de conservación de
soportes, que es la tercera falsa.

**Nivel de la fuente**: **plantilla oficial**. El término se ha buscado en todo el corpus reunido y
**no aparece en ninguna norma**.

---

## 3. Los lenguajes documentales

### 3.1 Precoordinación y postcoordinación

**La respuesta oficial**: el tesauro es **un lenguaje combinatorio postcoordinado**.

Ésta sí tiene norma, y con las dos definiciones enfrentadas la pregunta se cae sola. **ISO
25964-1:2011** define en su apartado 2.44 la *pre-coordination* como «**combination of concepts
(2.11), classes or terms (2.61) of a controlled vocabulary (2.12) at the time of its construction or
at the time of using it for indexing (2.27) or classification (2.5)**» —la combinación se hace **al
construir el vocabulario o al indizar**—; y en el 2.43 la *post-coordination* como «**combination of
preferred terms (2.45) of a controlled vocabulary (2.12) at the time of searching**» —la combinación
se hace **al buscar**—.

**Los números entre paréntesis no son erratas**: la norma remite con ellos al apartado donde define
cada término que usa, y se copian aquí porque forman parte del texto. Es, de paso, **la mejor
descripción de lo que es una norma de vocabulario**: nada se usa sin estar definido antes.

**Toda la diferencia está en el momento.** Y la norma remata el 2.43 con un ejemplo que vale por una
explicación entera: «**The post-coordinated search expression "microwaves AND radiation" can be used
to retrieve documents on microwave radiation, when these have been indexed under the separate terms
"microwaves" and "radiation" rather than a compound term**».

**Por qué el tesauro es postcoordinado**: porque **guarda los conceptos por separado** y deja que sea
el usuario quien los combine en el momento de la consulta. Un lenguaje precoordinado —una
clasificación decimal, un encabezamiento de materia compuesto— **trae la combinación ya hecha**: en
el ejemplo de la propia norma, la clase «teoría general» colocada dentro de «música» **ya significa**
«teoría de la música» y no otra cosa.

Las tres opciones falsas, una a una:

- «Un lenguaje **precoordinado** y jerárquico» — **el adjetivo está invertido**. Jerárquico sí lo es,
  y por eso es el distractor bueno: mezcla algo cierto con lo contrario de lo cierto.
- «Un lenguaje **precombinado**» — lo mismo dicho de otra manera.
- «Un lenguaje **libre** postcoordinado» — **postcoordinado acierta, «libre» falla**. Un tesauro es
  por definición un **vocabulario controlado**: la propia norma lo define en 2.12 como «**prescribed
  list of terms (2.61), headings or codes, each representing a concept (2.11)**» —lista prescrita— y
  añade que
  «**Thesauri, subject heading schemes and name authority lists are examples of controlled
  vocabularies**». Lenguaje libre es lo contrario: las palabras clave que cada uno escribe.

### 3.2 Qué es un tesauro, y qué norma lo rige

**La respuesta oficial**: la norma internacional sobre «Tesauros e interoperabilidad con otros
vocabularios» es la **ISO 25964**.

**El enunciado del examen es la traducción literal del título de la norma.** Su título en inglés es
«**Information and documentation — Thesauri and interoperability with other vocabularies**», y va en
dos partes: «**Part 1: Thesauri for information retrieval**» y «**Part 2: Interoperability with other
vocabularies**».

La página oficial de la norma, alojada por **NISO** —que es la secretaría del subcomité que la
redactó—, resume su alcance y su historia: «**Part 1 of the standard, published in 2011, covers all
aspects of developing a thesaurus, monolingual or multilingual. It has replaced the previous
standards ISO 2788 and ISO 5964**», y «**To encourage networking interoperability, it includes a data
model and an XML schema for data exchange**».

**Ese dato de la sustitución es el que conviene guardar**: **ISO 25964 vino a unificar dos normas
anteriores**, una de tesauros monolingües y otra de multilingües, que es exactamente por qué su
parte 1 sirve para los dos casos.

Las tres opciones falsas son **tres normas reales del mismo comité de ISO**, y por eso la pregunta es
buena: no son números inventados. El Centro Internacional del ISSN publica sus designaciones exactas:

| Opción falsa | Qué es en realidad |
|---|---|
| **ISO 2709** | «**The ISO 2709 computer format is the universal standard used in the library world for bibliographic records**» — el formato de intercambio de registros bibliográficos |
| **ISO 3297** | «**ISO 3297:2007 Information and documentation — International standard serial number (ISSN)**» — el número de las publicaciones seriadas |
| **ISO 2108** | «**ISO 2108:2005 Information and documentation — International standard book number (ISBN)**» — el número de los libros |

### 3.3 La interoperabilidad: los tres modelos y la excepción

**La respuesta oficial**: el modelo de interoperabilidad adecuado para **un tesauro multilingüe
nuevo** es el **modelo de unidad estructural**.

Ésta es la pregunta más técnica del tema, y su fuente es **la parte 2 de la norma**. Su objeto,
literalmente: «**It gives recommendations for the establishment and maintenance of mappings between
multiple thesauri, or between thesauri and other types of vocabularies**».

**Su cláusula 6 se titula «Structural models for mapping across vocabularies»**, y sus apartados dan
los cuatro nombres que el examen traduce, en este orden:

| Apartado | Nombre en la norma | Cómo lo traduce el examen |
|---|---|---|
| **6.2** | «**Model 1: Structural unity**» | Modelo de **unidad estructural** |
| **6.3** | «**Model 2: Direct-linked**» | Modelo de **vinculación directa** |
| **6.4** | «**Model 3: Hub structure**» | Modelo de **estructura central o hub** |
| **6.5** | «**Selective mapping**» | Modelo de **mapeo selectivo** |

**Y ahí está la clave de la respuesta, en la propia numeración**: la norma llama **modelos** a los
tres primeros —«Model 1», «Model 2», «Model 3»— y **al cuarto no**. El mapeo selectivo va aparte,
como una decisión sobre **cuánto** se mapea, no sobre **cómo se estructura**. La cláusula cierra con
un apartado 6.6 titulado «**Choosing among the options**», que es el que enseña a elegir.

**Por qué la unidad estructural para un tesauro nuevo.** Los otros tres modelos parten de
**vocabularios que ya existen por separado** y hay que unir: se enlazan entre sí —vinculación
directa— o contra un vocabulario central —estructura hub—, y se decide si se mapea todo o sólo una
parte —mapeo selectivo—. **La unidad estructural es la única que no une nada: construye una sola
estructura conceptual con varias lenguas dentro.** La propia norma de la parte 1 define el
**tesauro multilingüe** como «**thesaurus (2.62) in which terms (2.61) and relational structures are
available in two or more natural languages**» —los términos y **las estructuras de relaciones** están
disponibles en dos o más lenguas—, que es la descripción de la unidad estructural.

**La regla de examen**: si el tesauro **ya existe** en varias lenguas por separado, se **mapea**; si
**se va a hacer nuevo**, se construye **con una sola estructura** y varias lenguas. La palabra
«nuevo» del enunciado es la que decide.

---

## 4. Los códigos normalizados de identificación

**La respuesta oficial**: el Código Internacional Normalizado para Obras Musicales es el **ISWC**.

**El enunciado del examen es la traducción de la frase con que se define el propio sistema.** Su
página oficial, gestionada por la confederación internacional de sociedades de autores y
compositores, se describe así: «**The ISWC (International Standard Musical Work Code) is a unique,
permanent and internationally recognized reference number for the identification of musical works**».
Único, permanente y reconocido internacionalmente, para identificar obras musicales: **las mismas
tres palabras que el examen**.

Su norma es la **ISO 15707**, «**Information and documentation — International Standard Musical Work
Code (ISWC)**». Su objeto: «**This document specifies a means of uniquely identifying a musical
work**», y aclara qué identifica y qué no: «**The International Standard Musical Work Code (ISWC)
identifies musical works as intangible creations. It is not used to identify manifestations of, or
objects related to a musical work**».

**Y a continuación la propia norma descarta dos de las tres opciones falsas**, nombrándolas: esas
manifestaciones y objetos «**are the subject of separate identification systems, such as the
International Standard Recording Code (ISRC) for sound recordings, the International Standard Music
Number (ISMN) for printed music, and the International Standard Audiovisual Number (ISAN) for
audiovisual works**».

De modo que las cuatro opciones quedan así, con la designación de su norma tomada de la lista que
publica el Centro Internacional del ISSN:

| Sigla | Qué identifica | Norma |
|---|---|---|
| **ISWC** | **La obra musical** como creación intangible | **ISO 15707** |
| **ISMN** | **La música impresa** —la partitura— | «**ISO 10957:2009 Information and documentation — International standard music number (ISMN)**» |
| **ISRC** | **La grabación sonora** | «**ISO 3901:2001 Information and documentation — International Standard Recording Code (ISRC)**» |
| **ISBN** | **El libro** | «**ISO 2108:2005 Information and documentation — International standard book number (ISBN)**» |

**La distinción que la pregunta mide, y que es la que de verdad importa en un archivo**: una canción
tiene **un ISWC** —la obra—, **un ISMN** por cada edición de su partitura y **un ISRC por cada
grabación**. Son tres cosas distintas y **la misma canción las tiene todas a la vez**. El distractor
más fino es **ISMN**, porque también es «música» y su nombre en inglés se parece.

**Una precisión de fecha, porque este proyecto estudia el derecho a 21 de diciembre de 2022.** La
edición de ISO 15707 que se ha leído es la **segunda, de diciembre de 2022**, y su propio prólogo
dice que «**This second edition cancels and replaces the first edition (ISO 15707:2001), of which it
constitutes a minor revision**», y enumera los cambios: se añadió la cláusula de referencias
normativas y se quitaron las menciones a la agencia internacional del ISWC. **Ninguno de esos cambios
toca lo que el examen pregunta**, y el título del código es el mismo en las dos ediciones.

---

## 5. Las tecnologías en la redacción

**La respuesta oficial**: la redacción digital en programas no informativos de una cadena de
televisión es un **conjunto de aplicaciones que centralizan el control de todos los elementos de
software y hardware del sistema**.

**Ésta es la pregunta más rara de las nueve**, y conviene decir por qué: la expresión «redacción
digital» tiene **dos sentidos** en castellano, y el examen elige el que no espera quien no trabaja en
una cadena.

- **El sentido de escritura**: «redacción» como acto de redactar, y «digital» como medio. Es lo que
  dice la opción «**arte de crear y adaptar textos para medios digitales**», y es el sentido del
  diccionario.
- **El sentido de instalación**: «la redacción» como **el lugar y el sistema donde se produce el
  contenido** —igual que se dice «la redacción del telediario»—. Digitalizada, esa redacción **es un
  sistema informático**: el que integra escaleta, textos, vídeo, grafismo y emisión.

**El examen pregunta por el segundo**, y por eso la respuesta habla de aplicaciones que **centralizan
el control** del software y del hardware. Las otras dos opciones falsas —diseño de interfaces para
aplicaciones móviles, edición de vídeo para plataformas— **ni siquiera juegan**: son oficios
distintos.

**Y el matiz de «no informativos» tiene sentido**: en informativos, ese sistema tiene nombre propio
y está estandarizado en la industria; en programas no informativos la instalación es **el mismo
concepto sin ese nombre**, y de ahí que la pregunta pida la definición genérica.

**Nivel de la fuente**: **plantilla oficial**. La expresión se ha buscado en todo el corpus reunido
—normas ISO, convenio colectivo, leyes audiovisuales— y **no aparece definida en ninguna**.

---

## 6. Los datos que el examen ha preguntado

Nueve preguntas. Todas se contestan con el tema delante:

| Materia | Dato preguntado | Nivel |
|---|---|---|
| Lenguajes documentales | El tesauro es un lenguaje **combinatorio postcoordinado** | **ISO 25964-1**, apartados 2.43 y 2.44 |
| Recuperación | El modelo basado en el teorema de Bayes es el **probabilístico** | Plantilla oficial |
| Interoperabilidad | Para un tesauro multilingüe **nuevo**, el modelo de **unidad estructural** | **ISO 25964-2**, apartado 6.2 |
| Difusión | La **curación de contenidos** es seleccionar y compilar para agregar valor y difundir | Plantilla oficial |
| Análisis | El resumen más breve es el **indicativo** | Plantilla oficial |
| Identificación | El código de obras musicales es el **ISWC** | **ISO 15707** y página oficial del ISWC |
| Tecnologías | La **redacción digital** es el conjunto de aplicaciones que centralizan el control | Plantilla oficial |
| Proceso documental | La **selección** busca los documentos de mayor valor patrimonial y utilidad | Plantilla oficial (**Ley 16/1985** para el marco) |
| Normalización | «Tesauros e interoperabilidad con otros vocabularios» es la **ISO 25964** | **ISO 25964**, título oficial |

**Lo que no se ha preguntado y sale gratis del mismo tema**: que **ISO 25964 sustituyó a ISO 2788 y a
ISO 5964**; que su parte 1 trae **un modelo de datos y un esquema XML** de intercambio; que la norma
define **vocabulario controlado** como «lista prescrita de términos, encabezamientos o códigos» y
cuenta entre ellos a **tesauros, encabezamientos de materia y listas de autoridades**; que **ISO
2709** es el formato de registros bibliográficos y **ISO 3297** el del ISSN; que la misma canción
tiene a la vez **ISWC, ISMN e ISRC**; y que, por la **Ley 16/1985**, el archivo de RTVE es
**Patrimonio Documental** y sus documentos **no pueden destruirse mientras subsista su valor
probatorio**.

---

## 7. Trazabilidad

- **ISO 25964-1:2011**, «Information and documentation — Thesauri and interoperability with other
  vocabularies — Part 1: Thesauri for information retrieval», **muestra oficial** leída el **3 de
  septiembre de 2026**: el objeto, el índice completo y los términos y definiciones **2.1 a 2.47**,
  entre ellos concepto, vocabulario controlado, documento, indización, recuperación de información,
  interoperabilidad, metadatos, tesauro multilingüe, **postcoordinación** y **precoordinación**.
- **ISO 25964-2:2013**, «… — Part 2: Interoperability with other vocabularies», **muestra oficial**
  leída el **3 de septiembre de 2026**: el objeto, la introducción, el índice completo —con la
  **cláusula 6 y sus apartados 6.2 a 6.6**— y los términos y definiciones **3.1 a 3.54**.
- **ISO 15707:2022**, «Information and documentation — International Standard Musical Work Code
  (ISWC)», **segunda edición, diciembre de 2022**, **muestra oficial** leída el **3 de septiembre de
  2026**: el prólogo con los cambios respecto de la edición de 2001, la introducción, el objeto y la
  construcción del código.
- **Página oficial de ISO 25964**, alojada por **NISO**, secretaría del ISO/TC46/SC9, leída el **3 de
  septiembre de 2026**: el resumen de las dos partes, la sustitución de ISO 2788 y ISO 5964 y los
  índices abreviados de ambas partes.
- **«ISSN, a standardised code»**, Centro Internacional del ISSN, leída el **3 de septiembre de
  2026**: la designación exacta de **ISO 2108, ISO 3297, ISO 3901 e ISO 10957** y la descripción de
  **ISO 2709**.
- **Portada del ISWC**, sistema gestionado por la confederación internacional de sociedades de
  autores y compositores, leída el **3 de septiembre de 2026**: la definición del código.
- **Ley 16/1985, de 25 de junio, del Patrimonio Histórico Español**, `BOE-A-1985-12534`, **texto
  vigente al 21 de diciembre de 2022**: los artículos **cuarenta y nueve** —documento y Patrimonio
  Documental—, **cincuenta y cinco** —exclusión y eliminación—, **cincuenta y siete** —consulta— y
  **cincuenta y ocho** —Comisión Superior Calificadora—. Esta ley **numera sus artículos con letra**,
  de modo que las lentes por artículo no la reconocen: se ha construido una copia con los rótulos en
  cifra para poder pasarlas, sin tocar el texto de los preceptos.

**Lo que este tema no puede sostener, y por eso lo dice:**

- **Cuatro de las nueve respuestas se apoyan sólo en la plantilla oficial**: el modelo probabilístico,
  el resumen indicativo, la curación de contenidos y la redacción digital. Los términos se han
  buscado en todo el corpus del proyecto y **ninguno aparece en norma**.
- **La norma que clasifica los resúmenes, ISO 214, no se ha podido consultar.** El catálogo de ISO
  responde «prohibido» a toda consulta automática, y la norma se vende sin muestra. Comprobado con
  agente de usuario de navegador.
- **De las normas ISO sólo se ha leído su muestra oficial**, no su texto íntegro, que es de pago. La
  muestra trae portada, prólogo, índice completo, introducción, objeto y parte de los términos: **es
  suficiente para lo que este examen pregunta**, y este tema no cita ni una línea que no esté en
  ella.
- **La definición de «tesauro» de la propia norma queda fuera de la muestra**: el término se define
  en un apartado posterior al corte. Lo que aquí se dice del tesauro procede de **las definiciones de
  precoordinación, postcoordinación y vocabulario controlado**, que sí están, y de la descripción de
  la norma en su página oficial.
- **El nexo entre el teorema de Bayes y el modelo probabilístico es explicación, no cita.** Ninguna
  de las fuentes reunidas lo escribe.
