# Tema 16 del específico de Ingeniería Técnica · Industrial · Programas de diseño y control de obras

Las siglas de este tema, presentadas de entrada: el diseño asistido por ordenador (**CAD**, *computer
aided design*), que es lo que el primero de los dos programas del enunciado hace; el modelado de
información de construcción (**BIM**, *building information modeling*); el formato de intercambio de
dibujo (**DXF**) y el formato de documento portátil (**PDF**); la industria de la construcción y sus
clases de fundación (**IFC**, *industry foundation classes*), que es el formato abierto de intercambio
de modelos; la Ley de Contratos del Sector Público (**LCSP**); y el metro cuadrado (**m²**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Industrial, punto 16):
> «Programas de diseño y control de obras (Autocad y Presto).»

**Es el punto más corto del anexo y el que plantea el problema de método más incómodo**: **nombra dos
PRODUCTOS COMERCIALES concretos.** **Uno de dibujo asistido por ordenador y otro de mediciones y
presupuestos.**

**Lo que este temario hace con eso, y lo declara**: **no se ha consultado la documentación de ninguno
de los dos programas, ni se afirma nada de su funcionamiento particular.** **Lo que se desarrolla son
las **dos funciones** que el enunciado nombra a través de ellos** —dibujar y presupuestar— **y los
conceptos de oficio que cualquier programa de cada clase maneja.**

**La razón no es de comodidad, es de método**: **un temario que describa las órdenes de un programa
concreto caduca con su siguiente versión y no sirve para otro.** **Lo que no caduca es el flujo de
trabajo, la estructura de un presupuesto y los criterios de medición.**

<!-- indice -->

## Índice

- [1. Las dos funciones y por qué van juntas](#1-las-dos-funciones-y-por-qué-van-juntas)
- [2. El dibujo asistido por ordenador](#2-el-dibujo-asistido-por-ordenador)
- [3. Del dibujo al modelo](#3-del-dibujo-al-modelo)
- [4. La estructura de un presupuesto](#4-la-estructura-de-un-presupuesto)
- [5. Las mediciones y sus criterios](#5-las-mediciones-y-sus-criterios)
- [6. El control de la obra](#6-el-control-de-la-obra)
- [7. Lo que un proyecto de instalaciones exige de estas herramientas](#7-lo-que-un-proyecto-de-instalaciones-exige-de-estas-herramientas)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Las dos funciones y por qué van juntas

| Función | Qué produce | Documento del proyecto al que sirve |
|---|---|---|
| **Dibujo asistido por ordenador** | **Los planos y esquemas** | **Documento de PLANOS** |
| **Mediciones y presupuestos** | **Las unidades de obra, sus cantidades y sus precios** | **Documento de MEDICIONES Y PRESUPUESTO** |

**Y las dos van juntas en el enunciado por una razón que conviene enunciar**: **la medición sale del
plano.** **Lo que se dibuja se mide y lo que se mide se presupuesta**, y **si el plano cambia, la
medición cambia.** **Mantener las dos cosas coherentes a mano es imposible en cuanto el proyecto tiene
un tamaño**, y **de ahí que el enunciado del anexo nombre las dos herramientas en la misma línea.**

**Los cuatro documentos de un proyecto que el tema 16 del específico de Ingeniería Técnica ·
Telecomunicación enumera y que aquí se completan**: **memoria, pliego, planos y mediciones y
presupuesto**, más **la planificación.** **Este punto cubre el tercero y el cuarto.**

**Y el hilo que los une, que es lo que un examen podría pedir**: **cada unidad de obra del presupuesto
debe estar dibujada en los planos, descrita en el pliego y justificada en la memoria.** **Una unidad
que sólo esté en el presupuesto no se sabe hacer; una que sólo esté en el plano no se paga.**

## 2. El dibujo asistido por ordenador

**Los conceptos que cualquier programa de esta clase maneja y que hay que saber nombrar:**

| Concepto | Qué es |
|---|---|
| **Capa** | **La agrupación lógica de entidades** que permite mostrar, ocultar, bloquear e imprimir por separado |
| **Bloque** | **Un conjunto de entidades que se inserta como una sola**, y que al modificar el original actualiza todas sus inserciones |
| **Atributo** | **El dato asociado a un bloque**, que permite extraer un listado desde el dibujo |
| **Referencia externa** | **Un dibujo insertado en otro sin copiarlo**, que se actualiza cuando el original cambia |
| **Espacio modelo y espacio papel** | **Se dibuja a tamaño real en el primero y se compone la lámina en el segundo** |
| **Escala** | **Se aplica en la presentación, no al dibujar** |

**La regla de oro del dibujo asistido, y es la que separa un proyecto mantenible de uno que no lo
es**: **se dibuja **siempre** a escala 1:1 en unidades reales, y la escala se decide al imprimir.**
**Dibujar «a escala» es un error de método que impide medir desde el plano.**

**Y la de organización, que es la que hace posible trabajar entre varios**: **la estructura de capas y
la nomenclatura de ficheros se acuerdan **antes** de empezar y se escriben.** **Un proyecto con veinte
capas llamadas «capa1» a «capa20» es ilegible para el que venga después, aunque el dibujo sea
correcto.**

**Los tres usos que las capas tienen en un proyecto de instalaciones, y que justifican dedicarles
tiempo:**

1. **Separar disciplinas**: **arquitectura de fondo, climatización, electricidad, protección contra
   incendios, cada una en su grupo de capas**, para poder imprimir un plano por disciplina desde el
   mismo dibujo.
2. **Separar estados**: **existente, a demoler, nuevo.**
3. **Separar lo que se mide de lo que no**: **el fondo de arquitectura no se mide; los conductos sí.**

**Los formatos de intercambio, con su función:**

| Formato | Para qué |
|---|---|
| **Nativo del programa** | **Trabajar** |
| **De intercambio de dibujo** | **Entregar a quien usa otro programa** |
| **Documento portátil** | **Publicar y visar**: no se edita, y es el que se firma |
| **De modelo abierto** | **Intercambiar el **modelo**, no el dibujo** |

**La regla de entrega que un pliego debe fijar y casi nunca fija**: **hay que decir en qué formatos se
entrega y qué formato es el **contractual**.** **Si se entrega dibujo editable y documento portátil y no
se dice cuál manda, cualquier discrepancia entre los dos es un conflicto.**

## 3. Del dibujo al modelo

**El enunciado nombra un programa de dibujo, y la práctica del sector ha cambiado.** **Conviene
decirlo, y este temario lo declara como observación:**

| | **Dibujo asistido** | **Modelado de información de construcción** |
|---|---|---|
| **Qué contiene** | **Líneas que representan cosas** | **Objetos que SON cosas, con sus propiedades** |
| **Un conducto es** | **Dos líneas paralelas** | **Un conducto con su sección, su material y su caudal** |
| **La medición** | **Se hace midiendo el dibujo** | **Se extrae del modelo** |
| **Un cambio** | **Hay que actualizar cada plano donde aparezca** | **Se propaga a todas las vistas** |
| **Colisiones entre disciplinas** | **Se ven mirando** | **Se detectan automáticamente** |

**La detección de colisiones es lo que más aporta a un proyecto de instalaciones**, y **la razón es
obvia en cuanto se dice**: **la mayor parte de los problemas de obra de instalaciones son de espacio**
—un conducto que pasa por donde va una viga, una bandeja que choca con un falso techo—, **y ésos son
exactamente los que un modelo detecta antes de construir.**

**Y la observación de contratación que el cambio arrastra**: **exigir modelo en un pliego cambia el
coste del proyecto y el perfil del equipo.** **Es una decisión de la propiedad, no del proyectista**, y
**tiene que estar en el pliego desde el principio**, con **su formato de entrega y su nivel de detalle
definidos.**

**Lo que no cambia con el modelo, y conviene decirlo para no vender humo**: **el modelo no proyecta.**
**Un mal dimensionado sigue siendo un mal dimensionado**, y **el modelo lo dibuja perfectamente y sin
colisiones.**

## 4. La estructura de un presupuesto

**Ésta es la parte que un examen puede pedir enumerada, y es la que ordena cualquier programa de
mediciones y presupuestos.** **La estructura, de dentro afuera:**

| Nivel | Qué es |
|---|---|
| **Precio elemental** | **Mano de obra, material o maquinaria**: la unidad básica que se compra |
| **Precio auxiliar** | **Una composición de elementales que se repite** |
| **Precio unitario o unidad de obra** | **Lo que se mide y se paga**: descompuesto en elementales y auxiliares, con sus rendimientos |
| **Capítulo** | **La agrupación de unidades de obra por materia o por oficio** |
| **Presupuesto de ejecución material** | **La suma de todos los capítulos** |
| **Presupuesto base de licitación** | **El anterior más gastos generales, beneficio industrial e impuestos** |

**Los dos últimos escalones son los que más se confunden y los que un examen persigue:**

| Concepto | Qué incluye |
|---|---|
| **Ejecución material** | **Sólo el coste de ejecutar: materiales, mano de obra, maquinaria y medios auxiliares** |
| **Ejecución material + gastos generales + beneficio industrial** | **El presupuesto de ejecución por contrata, sin impuestos** |
| **Presupuesto base de licitación** | **Lo anterior CON el impuesto**, que es la cifra que se publica |

**Y la anatomía de una unidad de obra, que es lo que un ingeniero escribe:**

| Elemento | Qué es |
|---|---|
| **Código** | **El identificador, que permite ordenar y comparar** |
| **Unidad de medida** | **Metro, metro cuadrado, metro cúbico, kilogramo, unidad, hora** |
| **Resumen** | **La línea corta que aparece en el listado** |
| **Descripción** | **El texto que define **qué** incluye la unidad y qué no**: es la parte contractual |
| **Descomposición** | **Los elementales y auxiliares con sus rendimientos** |
| **Precio** | **El resultado de la descomposición** |

**La descripción es la parte más importante y la que menos se cuida**, y **conviene decir por qué**:
**es lo que decide si una partida incluye los pequeños accesorios, la mano de obra de puesta en
marcha, las pruebas o la retirada de escombro.** **Un litigio de obra se gana o se pierde leyendo la
descripción de la unidad, no su precio.**

**Y el aviso de oficio sobre las descomposiciones**: **los rendimientos de una base de precios general
son un punto de partida, no un dato.** **Una instalación en un edificio en servicio, con trabajos
nocturnos y accesos restringidos, tiene rendimientos muy distintos**, y **eso hay que ajustarlo o el
presupuesto no se parecerá a la obra.**

## 5. Las mediciones y sus criterios

**Medir es contar unidades de obra sobre el proyecto**, y **el problema no es contar: es decidir CÓMO
se cuenta.**

**Los tres criterios de medición que hay que fijar y escribir:**

| Criterio | Ejemplo en instalaciones |
|---|---|
| **Qué se mide** | **La tubería: ¿por eje o por desarrollo real con accesorios?** |
| **Qué se descuenta** | **¿Se descuentan los huecos de un falso techo? ¿Los pasos de una bandeja?** |
| **Qué se incluye en el precio** | **¿Los soportes van en la partida de tubería o aparte?** |

**La regla que evita el conflicto y que hay que poner en el pliego**: **el criterio de medición se
escribe en la propia unidad de obra**, no en un documento aparte. **Así se lee donde se aplica.**

**Y la estructura de la medición, que es lo que el programa organiza:**

| Elemento | Qué es |
|---|---|
| **Línea de medición** | **Una anotación con su descripción, número de unidades iguales, longitud, anchura y altura** |
| **Subtotal** | **La suma de las líneas de una unidad de obra en un capítulo** |
| **Referencia al plano** | **De qué plano y de qué zona sale esa línea** |

**La tercera es la que casi nadie rellena y la que hace la medición comprobable**: **una medición sin
referencia al plano no se puede verificar ni actualizar cuando el plano cambie.** **Es el mismo
principio de trazabilidad que este temario aplica a sus propias fuentes.**

**El aviso de método que cierra el epígrafe**: **medir es proyectar por segunda vez.** **Quien mide
descubre lo que el proyecto no había resuelto** —un tramo que no llega a ningún sitio, un cuadro sin
alimentación—, y **por eso conviene que mida quien ha proyectado, o al menos que hablen.**

## 6. El control de la obra

**El enunciado dice «programas de diseño y CONTROL DE OBRAS», y ésa es la segunda vida de un
presupuesto**: **una vez adjudicada la obra, el mismo documento sirve para controlarla.**

**Los tres controles que se llevan sobre el presupuesto:**

| Control | Qué compara |
|---|---|
| **De certificación** | **Lo **ejecutado** contra lo presupuestado**, mes a mes: es lo que se paga |
| **De coste** | **Lo **gastado** contra lo previsto**: es lo que interesa al contratista |
| **De plazo** | **Lo **avanzado** contra la planificación** |

**Qué es una certificación, dicho con precisión**: **el documento que recoge la obra ejecutada en un
periodo, valorada a los precios del contrato**, y **que da derecho al cobro.** **Se hace midiendo **lo
realmente ejecutado**, no lo previsto**, y **de ahí que la medición se rehaga en cada certificación.**

**Y los tres conceptos que un ingeniero de dirección de obra tiene que manejar y no confundir:**

| Concepto | Qué es |
|---|---|
| **Precio contradictorio** | **El de una unidad **no prevista** en el contrato**, que hay que fijar entre las partes antes de ejecutarla |
| **Modificación del contrato** | **El cambio del objeto o del alcance**, con su régimen jurídico propio |
| **Exceso de medición** | **Más cantidad de una unidad que **sí** estaba prevista** |

**Los tres se tratan de forma distinta y confundirlos cuesta caro**: **el exceso de medición no cambia
el contrato; el precio contradictorio añade una unidad; la modificación cambia el contrato y tiene
límites legales.**

**La planificación, que el enunciado no nombra y sin la cual no hay control de plazo:**

| Elemento | Qué es |
|---|---|
| **Actividad** | **Una tarea con duración y recursos** |
| **Precedencia** | **Qué tiene que estar hecho antes** |
| **Camino crítico** | **La cadena de actividades cuyo retraso retrasa la obra entera** |
| **Holgura** | **Cuánto puede retrasarse una actividad sin retrasar la obra** |

**El camino crítico es el concepto que hay que saber definir**, y **su consecuencia práctica es la que
un director de obra usa a diario**: **acelerar una actividad que no está en el camino crítico no
adelanta la obra ni un día**, sólo gasta dinero.

**Y el enlace con el epígrafe 5**: **las actividades de la planificación deberían corresponderse con
los capítulos y las unidades de obra del presupuesto.** **Cuando no se corresponden, el avance físico
y el avance económico dejan de poder compararse**, y **el control de obra se queda en dos números que
nadie sabe relacionar.**

## 7. Lo que un proyecto de instalaciones exige de estas herramientas

**Las cinco cosas que un proyecto de este anexo pide y que conviene tener enumeradas**, porque **es la
respuesta que un examen buscaría:**

1. **Planos a escala real y por disciplina**, con **esquemas de principio además de plantas**: **una
   instalación no se entiende sólo en planta.**
2. **Esquemas unifilares y de bloques**, que **el artículo 19 del reglamento de baja tensión del tema
   7 exige entregar al titular.**
3. **Mediciones con criterio escrito en cada unidad y con referencia al plano.**
4. **Un presupuesto cuyos capítulos correspondan a las instalaciones reales**, para que **el control
   de obra sea posible.**
5. **Documentación final actualizada a lo realmente ejecutado**, que **el tema 16 del específico de
   Ingeniería Técnica · Telecomunicación exige como cierre de la implantación** y **que los
   reglamentos de este anexo piden en forma de certificados, esquemas y manuales.**

**Y la observación que cierra el punto y que resume su utilidad**: **la herramienta no mejora el
proyecto; hace posible mantenerlo.** **Un proyecto de instalaciones cambia decenas de veces entre el
anteproyecto y la recepción**, y **lo que decide si esos cambios llegan coherentes a los planos, a la
medición y al presupuesto no es el talento del proyectista: es si trabajó con las herramientas
enlazadas o con tres documentos sueltos.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **es, junto con el 13 y el 15, uno de los
puntos de este anexo sin norma nombrada en su enunciado.**

**Cinco declaraciones expresas:**

1. **El enunciado del anexo nombra dos **productos comerciales** concretos**, uno de dibujo asistido por
   ordenador y otro de mediciones y presupuestos. **No se ha consultado la documentación de ninguno de
   los dos**, **no se describe el funcionamiento particular de ninguno** y **no se cita ninguna de sus
   órdenes, menús ni versiones.** **Lo que este tema desarrolla son las dos FUNCIONES que el enunciado
   nombra a través de ellos y los conceptos de oficio comunes a cualquier programa de cada clase.**
2. **La razón de esa decisión está escrita en la cabecera del tema y se declara como método**: **un
   temario atado a la versión de un producto caduca y no sirve para otro.**
3. **Los conceptos de dibujo asistido, de presupuesto, de medición y de planificación son oficio de
   ingeniería de proyectos**, presentados como conocimiento común de la materia. **Ninguna norma ni
   manual se ha consultado para ellos.**
4. **La Ley de Contratos del Sector Público no se ha consultado**, y **no se le atribuye ningún
   precepto**: **lo que se dice de precios contradictorios, modificaciones y excesos de medición es
   práctica corriente de dirección de obra**, y **la mención de que las modificaciones «tienen límites
   legales» se hace sin cifrarlos ni citarlos.**
5. **El artículo 19 del reglamento electrotécnico para baja tensión se nombra por lo que el tema 7 de
   este mismo específico identifica de él**, no por una lectura nueva.

**El resto del tema va como oficio y así se declara**: la explicación de por qué las dos funciones van
juntas en el enunciado, el hilo que une los cuatro documentos del proyecto, la regla de dibujar a
escala real, la de acordar capas y nomenclatura por escrito, los tres usos de las capas, la regla de
fijar el formato contractual de entrega, la comparación entre dibujo y modelo y la observación de que
el modelo no proyecta, la distinción entre los tres presupuestos, el subrayado de que un litigio se
gana leyendo la descripción de la unidad, el aviso sobre los rendimientos de una base de precios
general, la regla de escribir el criterio de medición en la propia unidad, la observación de que medir
es proyectar por segunda vez, la distinción entre precio contradictorio, modificación y exceso de
medición, la consecuencia práctica del camino crítico y la conclusión de que la herramienta no mejora
el proyecto sino que hace posible mantenerlo. **Nada de eso está en un boletín oficial ni en una norma
técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
