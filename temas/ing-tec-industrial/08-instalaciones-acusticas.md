# Tema 8 del específico de Ingeniería Técnica · Industrial · Instalaciones acústicas

Las siglas de este tema, presentadas de entrada: los índices de ruido de la norma, que se escriben con
letra ele y un subíndice —el de día-tarde-noche (**Lden**), el de día (**Ld**), el de tarde (**Le**) y
el de noche (**Ln**)—, con sus equivalentes en inglés (**Lday**, **Levening** y **Lnight**); el Código
Técnico de la Edificación (**CTE**), del tema 3, y su documento básico de protección frente al ruido
(**DB HR**); el Reglamento de Instalaciones Térmicas en los Edificios (**RITE**), del tema 1; y la
Unión Europea (**UE**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Industrial, punto 8):
> «Instalaciones acústicas. Cálculo, diseño, mantenimiento y normativa.
> 8.1. Ley 37/2003, de 17 de noviembre, del Ruido (BOE» núm. 276, de 18/11/2003. Texto consolidado:
> Última actualización publicada el 07/07/2011).
> 8.2. Real Decreto 1513/2005, de 16 de diciembre por el que se desarrolla la Ley 37/2003, de 17 de
> noviembre, del Ruido, en lo referente a la evaluación y gestión del ruido ambiental (BOE núm. 301,
> de 17/12/2005. Texto consolidado: última actualización publicada el 10/02/2022).»

**Es el único punto del anexo que descansa en una LEY y no en un reglamento**, y **eso cambia cómo se
estudia**: **una ley fija competencias, define conceptos y remite al Gobierno los valores**; **un
reglamento da los números.** **Aquí los números están casi todos fuera de las dos normas del
enunciado.**

**Y el aviso que ordena el punto y evita el error más frecuente**: **esta ley NO regula el ruido en el
lugar de trabajo.** **Su artículo 2.2.c) lo excluye expresamente y lo remite a la legislación
laboral.** **El ruido que sufre un trabajador es materia de prevención de riesgos; el que sufre un
vecino es materia de esta ley.** **Dos regímenes distintos para el mismo decibelio.**

<!-- indice -->

## Índice

- [1. Objeto y ámbito de la ley](#1-objeto-y-ámbito-de-la-ley)
- [2. El vocabulario que hay que dominar](#2-el-vocabulario-que-hay-que-dominar)
- [3. Las áreas acústicas y los objetivos de calidad](#3-las-áreas-acústicas-y-los-objetivos-de-calidad)
- [4. Los valores límite y los emisores](#4-los-valores-límite-y-los-emisores)
- [5. Las suspensiones y las excepciones](#5-las-suspensiones-y-las-excepciones)
- [6. El reglamento de ruido ambiental](#6-el-reglamento-de-ruido-ambiental)
- [7. Lo que esta ocupación tiene que resolver](#7-lo-que-esta-ocupación-tiene-que-resolver)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Objeto y ámbito de la ley

**Artículo 1**, entero:

> «**Esta ley tiene por objeto prevenir, vigilar y reducir la contaminación acústica, para evitar y
> reducir los daños que de ésta pueden derivarse para la salud humana, los bienes o el medio
> ambiente.**»
>
> — Ley 37/2003, artículo 1 (`BOE-A-2003-20976`), redacción vigente el 21 de diciembre de 2022.

---

**Tres verbos y tres bienes protegidos**, y **conviene notar el orden de los verbos**: **prevenir va
antes que reducir.** **La ley se ordena por ese orden**: **primero la planificación —áreas acústicas y
objetivos de calidad—, después el control —valores límite— y sólo al final la corrección —planes de
acción y zonas de protección especial—.**

**Quién está sujeto, del artículo 2.1**: **TODOS los emisores acústicos, públicos o privados**, y
**además las edificaciones EN SU CALIDAD DE RECEPTORES.**

**Esa segunda mitad es la que conecta con el Código Técnico del tema 3**: **la ley alcanza también a
quien recibe el ruido**, y **de ahí sale la exigencia de aislamiento del documento básico de
protección frente al ruido.**

**Las tres exclusiones del artículo 2.2, y las tres importan:**

| Excluido | Por qué y a dónde va |
|---|---|
| **Actividades domésticas y comportamientos de los vecinos** | **Sólo cuando se mantengan dentro de límites TOLERABLES según las ordenanzas municipales y los usos locales** |
| **Actividades militares** | **Su legislación específica** |
| **La actividad LABORAL, en el lugar de trabajo** | **La legislación laboral** |

**La primera tiene una condición y las otras dos no**: **el ruido de vecinos sale de la ley sólo
mientras sea tolerable.** **Pasado ese umbral, vuelve a entrar.**

## 2. El vocabulario que hay que dominar

**El artículo 3 tiene dieciocho definiciones y este tema recoge las que un ingeniero usa.** **Las
cuatro parejas que se confunden y que un examen buscaría:**

| Pareja | Diferencia |
|---|---|
| **Emisión / inmisión** | **La emisión es lo que el emisor genera; la inmisión es lo que existe en un lugar durante un tiempo.** Emisión es del foco; inmisión es del receptor |
| **Índice acústico / objetivo de calidad** | **El índice es una MAGNITUD FÍSICA para describir la contaminación; el objetivo es un CONJUNTO DE REQUISITOS que deben cumplirse** |
| **Valor límite / objetivo de calidad** | **El valor límite no debe sobrepasarse; el objetivo es lo que debe cumplirse en un espacio y un momento** |
| **Área acústica / zona de servidumbre acústica** | **El área tiene un mismo objetivo de calidad; la zona de servidumbre es donde las inmisiones PODRÁN superarlo**, con restricciones de uso |

**Y las tres definiciones que traen una cifra, que es lo más memorizable del artículo 3:**

| Concepto | Cifra |
|---|---|
| **Gran eje viario** | **Carretera con tráfico superior a 3 millones de vehículos por año** |
| **Gran eje ferroviario** | **Vía férrea con tráfico superior a 30.000 trenes por año** |
| **Gran aeropuerto** | **Aeropuerto civil con más de 50.000 movimientos por año** —despegues y aterrizajes—, **excluidos los de formación en aeronaves ligeras** |

**Las tres cifras son 3 millones, 30.000 y 50.000**, y **sirven para decidir qué infraestructuras han
de tener mapa estratégico de ruido.** **No son límites de ruido: son umbrales de tamaño.**

**Y una definición que conviene tener por lo que revela del método de la ley**: **la MOLESTIA es «el
grado de perturbación que provoca el ruido o las vibraciones a la población, determinado mediante
ENCUESTAS SOBRE EL TERRENO».** **Es el único concepto de la ley que no se mide con un aparato**, y
**eso es deliberado**: **el ruido molesta a personas, no a sonómetros.**

## 3. Las áreas acústicas y los objetivos de calidad

**El artículo 7 obliga a las comunidades autónomas a prever AL MENOS siete tipos de área acústica**, y
**la lista se aprende por el uso predominante del suelo:**

| Tipo | Uso predominante |
|---|---|
| **a)** | **Residencial** |
| **b)** | **Industrial** |
| **c)** | **Recreativo y de espectáculos** |
| **d)** | **Terciario distinto del recreativo** |
| **e)** | **Sanitario, docente y cultural que requiera especial protección** |
| **f)** | **Sistemas generales de infraestructuras de transporte u otros equipamientos públicos que los reclamen** |
| **g)** | **Espacios naturales que requieran especial protección** |

**Dos observaciones que ordenan la lista**: **son un MÍNIMO —las comunidades pueden añadir tipos— y
sólo dos de los siete se definen por necesitar «especial protección»**, la e) y la g). **Ésos son los
de objetivo más exigente.**

**Quién fija los objetivos de calidad, del artículo 8**: **el Gobierno**, para los distintos tipos de
área, **referidos tanto a situaciones existentes como nuevas**, y **también para el espacio interior
habitable** de viviendas y de usos residenciales, hospitalarios, educativos o culturales.

**Y los cinco criterios que el apartado 2 manda tener en cuenta al establecerlos**, que es una lista
poco intuitiva y por eso preguntable:

1. **Los valores de los índices de inmisión y emisión.**
2. **El grado de exposición de la población.**
3. **La sensibilidad de la fauna y de sus hábitats.**
4. **El patrimonio histórico expuesto.**
5. **La viabilidad técnica y económica.**

**Los criterios tercero y cuarto son los que sorprenden**: **la ley protege también a los animales y a
los edificios históricos del ruido**, y **el quinto es el que admite que un objetivo se module por lo
que cuesta alcanzarlo.**

## 4. Los valores límite y los emisores

**El artículo 12 hace tres cosas**, y **la tercera es la que obliga a todo el mundo:**

| Apartado | Qué dice |
|---|---|
| **1** | **Los valores límite de emisión y de inmisión los determina el GOBIERNO**, y los reduce cuando las mejores técnicas disponibles lo permitan sin costes excesivos |
| **4** | **Los del interior de los medios de transporte de competencia estatal se fijan con carácter ÚNICO para todo el Estado** |
| **5** | **Los titulares de emisores acústicos, cualquiera que sea su naturaleza, están OBLIGADOS a respetar los valores límite** |

**La clasificación de emisores del apartado 2, en doce letras**, que es la tabla más preguntable de la
ley:

| Grupo | Emisores |
|---|---|
| **Vehículos** | **Automóviles, ferrocarriles, aeronaves** |
| **Infraestructuras** | **Viarias, ferroviarias, aeroportuarias, portuarias** |
| **Máquinas y obras** | **Maquinaria y equipos**, **obras de construcción de edificios y de ingeniería civil** |
| **Actividades** | **Industriales, comerciales, deportivo-recreativas y de ocio** |

**Las doce letras se ordenan mejor en esos cuatro grupos que de corrido**, y **conviene notar la
simetría**: **tres medios de transporte y cuatro infraestructuras**, porque **el puerto no tiene
vehículo propio en la lista.**

**Y el apartado 3 deja la puerta abierta**: **el Gobierno puede establecer valores límite para otras
actividades, comportamientos y PRODUCTOS no contemplados.** **La palabra «productos» es la que permite
regular el ruido de un electrodoméstico.**

## 5. Las suspensiones y las excepciones

**El artículo 9 tiene tres regímenes distintos y hay que separarlos bien**, porque **sólo uno de los
tres no necesita autorización:**

| Régimen | Quién lo activa | Qué exige |
|---|---|---|
| **Actos de especial proyección oficial, cultural, religiosa o análoga** | **Las Administraciones públicas competentes** | **Valoración previa de la incidencia acústica**. Suspensión temporal en determinadas áreas |
| **Solicitud del titular de un emisor** | **El titular** | **Razones justificadas acreditadas en ESTUDIO ACÚSTICO**, y **sólo cabe si se acredita que las mejores técnicas disponibles NO permiten cumplir** |
| **Emergencias y servicios esenciales** | **Nadie: ocurre** | **NINGUNA autorización** |

**El tercero merece leerse por su alcance**: **se puede rebasar ocasional y temporalmente el objetivo
de calidad en situaciones de emergencia o por la prestación de servicios de prevención y extinción de
incendios, sanitarios, de seguridad u otros análogos**, y **para eso «no será necesaria autorización
ninguna».** **Una sirena no pide permiso.**

**Y el segundo tiene la condición más dura de la ley**: **no basta con que cumplir sea caro o
incómodo.** **Hay que acreditar que las **mejores técnicas disponibles** no permiten cumplir.** **Es una
prueba técnica, no económica.**

## 6. El reglamento de ruido ambiental

**El Real Decreto 1513/2005 desarrolla la ley en UNA sola materia**, y **su artículo 1 lo dice**:
**evaluación y gestión del RUIDO AMBIENTAL**, completando la incorporación de la Directiva 2002/49/CE.

**Y su ámbito es más estrecho que el de la ley**, lo que hay que saber para no confundirlos:

| | **Ley 37/2003** | **Real Decreto 1513/2005** |
|---|---|---|
| **Qué cubre** | **Toda la contaminación acústica** | **Sólo el RUIDO AMBIENTAL: el sonido EXTERIOR no deseado generado por actividades humanas** |
| **Dónde** | **Todos los emisores y las edificaciones como receptores** | **Zonas urbanizadas, parques y zonas tranquilas, campo abierto, proximidades de centros escolares, alrededores de hospitales y otros lugares vulnerables** |
| **Qué excluye** | **Doméstico tolerable, militar y laboral** | **Lo anterior, y además: el ruido de la **propia persona expuesta** y el del **interior** de los medios de transporte** |

**Las dos exclusiones que el reglamento añade son coherentes con su objeto**: **si sólo mira el sonido
exterior, ni el que uno mismo hace ni el de dentro de un autobús le corresponden.**

**Los cuatro índices de ruido, que son el corazón del reglamento:**

| Índice | Qué mide | Con qué se corresponde |
|---|---|---|
| **Lden** | **La molestia GLOBAL**, día-tarde-noche | **El índice de referencia** |
| **Ld** | **La molestia durante el día** | **Lday** |
| **Le** | **La molestia durante la tarde** | **Levening** |
| **Ln** | **La ALTERACIÓN DEL SUEÑO**, de noche | **Lnight** |

**El índice de noche no mide molestia: mide alteración del sueño**, y **ésa es la diferencia
conceptual que se pregunta.** **Los otros tres miden molestia; el nocturno mide otra cosa.**

**Cuáles se usan para qué, del artículo 5:**

| Uso | Índices |
|---|---|
| **Preparación y revisión de MAPAS ESTRATÉGICOS de ruido** | **Lden y Ln**, obligatoriamente |
| **Casos especiales del punto 2 del anexo I** | **Se pueden usar índices SUPLEMENTARIOS** |
| **Planificación acústica y determinación de zonas de ruido** | **Se pueden usar índices DISTINTOS de Lden y Ln** |

**Y la regla transitoria que conviene retener por su plazo**: **mientras no haya métodos comunes
obligatorios se pueden usar los índices existentes transformándolos, justificando técnicamente las
bases de la transformación**, y **sólo con datos de los TRES AÑOS inmediatos anteriores.**

**Qué es una aglomeración, del artículo 3.a)**: **una porción de territorio con MÁS DE 100.000
HABITANTES**, delimitada por la administración competente con los criterios del anexo VII y
considerada zona urbanizada. **Ésa es la cuarta cifra del punto**, junto a los 3 millones, los 30.000
y los 50.000 de la ley.

**Y la distinción entre los dos mapas, del artículo 3.h) e i)**, que es la que da nombre a la mitad del
reglamento:

| Mapa | Qué es |
|---|---|
| **Mapa de ruido** | **La presentación de datos sobre una situación acústica existente o pronosticada**, indicando superaciones de valores límite, personas afectadas o viviendas expuestas |
| **Mapa ESTRATÉGICO de ruido** | **Un mapa de ruido diseñado para evaluar GLOBALMENTE la exposición en una zona con distintas fuentes**, o para hacer predicciones globales |

**La palabra que los separa es «globalmente»**: **el estratégico suma fuentes; el ordinario puede
mirar una sola.**

## 7. Lo que esta ocupación tiene que resolver

**El enunciado del anexo dice «cálculo, diseño, mantenimiento y normativa» de instalaciones
acústicas**, y **ni la ley ni su reglamento dan un solo valor de aislamiento.** **Lo que un ingeniero
técnico industrial hace con este punto es esto:**

| Problema | Dónde está la norma |
|---|---|
| **Cuánto ruido puede salir de mi instalación al exterior** | **En los valores límite que el Gobierno fija y en las ordenanzas municipales**, dentro del marco de esta ley |
| **Cuánto tiene que aislar el edificio** | **En el documento básico de protección frente al ruido del Código Técnico**, del tema 3 |
| **Cuánto ruido pueden hacer las instalaciones térmicas del edificio** | **En la exigencia de calidad del ambiente acústico del artículo 11.4 del RITE**, del tema 1 |
| **Cuánto ruido puede soportar un trabajador** | **En la legislación de prevención de riesgos laborales**, expresamente excluida de esta ley |

**Las cuatro preguntas se responden con cuatro normas distintas**, y **ninguna de las cuatro es la que
este punto nombra.** **Ésa es la lección de método del punto**: **la Ley del Ruido es el MARCO, no el
manual.**

**Y las tres reglas de oficio que un proyecto de instalación en un edificio ajeno tiene que respetar,
y que se deducen de todo lo anterior:**

1. **El emisor responde de su emisión, y el edificio responde de su aislamiento.** **Son dos
   obligaciones distintas y una no excusa la otra.**
2. **El ruido de una instalación térmica se combate en el origen antes que en el receptor**:
   **antivibratorios, silenciadores y velocidad de conductos** salen más baratos que aislar la
   vivienda de al lado.
3. **La medida se hace en inmisión, en el receptor**, y **no en emisión, junto a la máquina.** **Lo
   que decide si hay infracción es lo que llega, no lo que sale.**

## 8. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Ley 37/2003, de 17 de noviembre, del Ruido** (`BOE-A-2003-20976`), **en su redacción vigente el 21 de diciembre de 2022** | **El artículo 1 entero**, citado literalmente |
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 1513/2005, de 16 de diciembre, por el que se desarrolla la Ley 37/2003 en lo referente a la evaluación y gestión del ruido ambiental** (`BOE-A-2005-20792`), **en su redacción vigente el 21 de diciembre de 2022** | **Ninguna cita literal**: su contenido se resume, y sus artículos van identificados |

**Cinco declaraciones expresas:**

1. **Ni la ley ni su reglamento contienen valores numéricos de ruido**, y **este tema no da
   ninguno.** **Los objetivos de calidad acústica y los valores límite los fija el Gobierno por otras
   normas que NO están en el enunciado del anexo y NO se han consultado.**
2. **Los anexos del real decreto no se citan ni se reproducen.** **El anexo I —descripción de los
   índices—, el anexo II —métodos de evaluación—, el anexo III —relaciones dosis-efecto— y el anexo
   VII —criterios de aglomeración— se nombran por lo que contienen**, que es lo que los artículos
   citados dicen de ellos.
3. **Los artículos que se resumen en tabla y no se citan van identificados uno a uno** —de la ley, el
   2, el 3, el 7, el 8, el 9 y el 12; del real decreto, el 1, el 2, el 3, el 5, el 6 y el 7—.
   **Todos están en las normas citadas arriba.**
4. **Las normas que estas dos invocan se nombran y no se han consultado**: **la Directiva 2002/49/CE**
   y **la Ley 16/2002 de prevención y control integrados de la contaminación.**
5. **El Código Técnico y el RITE se nombran por lo que este proyecto ha citado de ellos en los temas 3
   y 1 de este mismo específico**, con sus artículos identificados allí. **Aquí no se citan.**

**El resto del tema va como oficio y así se declara**: la observación de que el orden de los verbos del
artículo 1 ordena la ley entera, la lectura de la sujeción de las edificaciones como conexión con el
Código Técnico, la advertencia de que la exclusión del ruido de vecinos es condicional, las cuatro
parejas de conceptos que se confunden, la nota sobre la molestia como único concepto que se mide por
encuesta, la agrupación de las doce letras de emisores en cuatro grupos, la observación de que el
índice nocturno mide alteración del sueño y no molestia, la lectura de «globalmente» como la palabra
que separa los dos mapas, la tabla de las cuatro preguntas con cuatro normas distintas y las tres
reglas de oficio del epígrafe 7. **Nada de eso lo dicen las normas con esas palabras**, y el tema no lo
presenta como si lo dijeran.
