# Esquema · Tema 16 del específico de Ingeniería Técnica · Industrial · Programas de diseño y control de obras

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de ingeniería de proyectos y de
dirección de obra · `[norma]` = exigencia de una norma de OTRO punto de este mismo anexo · `[plan]` =
enunciado del anexo. **Siglas**: el diseño asistido por ordenador (**CAD**, *computer aided design*);
el modelado de información de construcción (**BIM**, *building information modeling*); el formato de
intercambio de dibujo (**DXF**) y el formato de documento portátil (**PDF**); las clases de fundación
de la industria de la construcción (**IFC**, *industry foundation classes*), formato abierto de
intercambio de modelos; la Ley de Contratos del Sector Público (**LCSP**); y el metro cuadrado
(**m²**).

**Cabecera.** Enunciado: punto 16 del anexo, **el más corto de todos y el que plantea el problema de
método más incómodo**: **nombra dos PRODUCTOS COMERCIALES concretos**, uno de dibujo asistido y otro de
mediciones y presupuestos · **qué hace el temario con eso, y lo declara**: **no se ha consultado la
documentación de ninguno de los dos ni se afirma nada de su funcionamiento particular**; se
desarrollan **las dos FUNCIONES que el enunciado nombra a través de ellos** · **la razón es de
método**: **un temario atado a la versión de un producto caduca y no sirve para otro.** **Lo que no
caduca es el flujo de trabajo, la estructura de un presupuesto y los criterios de medición.**

<!-- indice -->

## Índice

- [Las dos funciones y por qué van juntas](#las-dos-funciones-y-por-qué-van-juntas)
- [El dibujo asistido por ordenador](#el-dibujo-asistido-por-ordenador)
- [Del dibujo al modelo](#del-dibujo-al-modelo)
- [La estructura de un presupuesto](#la-estructura-de-un-presupuesto)
- [Las mediciones y sus criterios](#las-mediciones-y-sus-criterios)
- [El control de la obra](#el-control-de-la-obra)
- [Lo que un proyecto de instalaciones exige](#lo-que-un-proyecto-de-instalaciones-exige)

<!-- /indice -->

## Las dos funciones y por qué van juntas

| Función | Qué produce | Documento del proyecto |
|---|---|---|
| **Dibujo asistido por ordenador** | **Los planos y esquemas** | **PLANOS** |
| **Mediciones y presupuestos** | **Las unidades de obra, sus cantidades y sus precios** | **MEDICIONES Y PRESUPUESTO** |

- **POR QUÉ EL ENUNCIADO LAS NOMBRA EN LA MISMA LÍNEA** · `[of]` · **La medición sale del plano.** **Lo
  que se dibuja se mide y lo que se mide se presupuesta**, y **si el plano cambia, la medición
  cambia.** **Mantener las dos cosas coherentes a mano es imposible en cuanto el proyecto tiene
  tamaño.**
- **LOS DOCUMENTOS DE UN PROYECTO** · `[of]` · **Memoria, pliego, planos, mediciones y presupuesto**,
  más **la planificación.** **Este punto cubre el tercero y el cuarto.**
- **EL HILO QUE LOS UNE** · `[of]` · **Cada unidad de obra del presupuesto debe estar dibujada en los
  planos, descrita en el pliego y justificada en la memoria.** **Una unidad que sólo esté en el
  presupuesto no se sabe hacer; una que sólo esté en el plano no se paga.**

## El dibujo asistido por ordenador

| Concepto | Qué es |
|---|---|
| **Capa** | **Agrupación lógica de entidades** que permite mostrar, ocultar, bloquear e imprimir por separado |
| **Bloque** | **Conjunto de entidades que se inserta como una sola**; modificar el original actualiza todas sus inserciones |
| **Atributo** | **Dato asociado a un bloque**, que permite extraer un listado desde el dibujo |
| **Referencia externa** | **Dibujo insertado en otro sin copiarlo**, que se actualiza cuando el original cambia |
| **Espacio modelo y espacio papel** | **Se dibuja a tamaño real en el primero y se compone la lámina en el segundo** |
| **Escala** | **Se aplica en la presentación, no al dibujar** |

- **LA REGLA DE ORO DEL DIBUJO ASISTIDO** · `[of]` · **Se dibuja siempre a escala 1:1 en unidades
  reales, y la escala se decide al imprimir.** **Dibujar «a escala» es un error de método que impide
  medir desde el plano.**
- **LA REGLA DE ORGANIZACIÓN** · `[of]` · **La estructura de capas y la nomenclatura de ficheros se
  acuerdan antes de empezar y se escriben.** **Un proyecto con veinte capas llamadas «capa1» a
  «capa20» es ilegible para el que venga después, aunque el dibujo sea correcto.**
- **USO DE CAPAS 1** · `[of]` · **Separar disciplinas**: arquitectura de fondo, climatización,
  electricidad, protección contra incendios, **cada una en su grupo**, para imprimir un plano por
  disciplina desde el mismo dibujo.
- **USO DE CAPAS 2** · `[of]` · **Separar estados**: **existente, a demoler, nuevo.**
- **USO DE CAPAS 3** · `[of]` · **Separar lo que se mide de lo que no**: **el fondo de arquitectura no
  se mide; los conductos sí.**

| Formato de intercambio | Para qué |
|---|---|
| **Nativo del programa** | **Trabajar** |
| **De intercambio de dibujo** | **Entregar a quien usa otro programa** |
| **Documento portátil** | **Publicar y visar**: no se edita, y es el que se firma |
| **De modelo abierto** | **Intercambiar el modelo, no el dibujo** |

- **LA REGLA DE ENTREGA QUE UN PLIEGO DEBE FIJAR Y CASI NUNCA FIJA** · `[of]` · **Hay que decir en qué
  formatos se entrega y cuál es el CONTRACTUAL.** **Si se entrega dibujo editable y documento portátil
  y no se dice cuál manda, cualquier discrepancia entre los dos es un conflicto.**

## Del dibujo al modelo

| | **Dibujo asistido** | **Modelado de información de construcción** |
|---|---|---|
| **Qué contiene** | **Líneas que representan cosas** | **Objetos que SON cosas, con sus propiedades** |
| **Un conducto es** | **Dos líneas paralelas** | **Un conducto con su sección, su material y su caudal** |
| **La medición** | **Se hace midiendo el dibujo** | **Se extrae del modelo** |
| **Un cambio** | **Hay que actualizar cada plano donde aparezca** | **Se propaga a todas las vistas** |
| **Colisiones entre disciplinas** | **Se ven mirando** | **Se detectan automáticamente** |

- **LO QUE MÁS APORTA A UN PROYECTO DE INSTALACIONES** · `[of]` · **La detección de colisiones**, y la
  razón es obvia en cuanto se dice: **la mayor parte de los problemas de obra de instalaciones son de
  espacio** —un conducto por donde va una viga, una bandeja que choca con un falso techo—, y **ésos son
  los que un modelo detecta antes de construir.**
- **LA OBSERVACIÓN DE CONTRATACIÓN QUE ARRASTRA EL CAMBIO** · `[of]` · **Exigir modelo en un pliego
  cambia el coste del proyecto y el perfil del equipo.** **Es decisión de la propiedad, no del
  proyectista**, y **tiene que estar en el pliego desde el principio**, con su formato de entrega y su
  nivel de detalle definidos.
- **LO QUE NO CAMBIA, PARA NO VENDER HUMO** · `[of]` · **El modelo no proyecta.** **Un mal dimensionado
  sigue siéndolo**, y el modelo lo dibuja perfectamente y sin colisiones.

## La estructura de un presupuesto

| Nivel, de dentro afuera | Qué es |
|---|---|
| **Precio elemental** | **Mano de obra, material o maquinaria**: la unidad básica que se compra |
| **Precio auxiliar** | **Una composición de elementales que se repite** |
| **Precio unitario o unidad de obra** | **Lo que se mide y se paga**: descompuesto en elementales y auxiliares, con sus rendimientos |
| **Capítulo** | **Agrupación de unidades de obra por materia o por oficio** |
| **Presupuesto de ejecución material** | **La suma de todos los capítulos** |
| **Presupuesto base de licitación** | **El anterior más gastos generales, beneficio industrial e impuestos** |

| Los dos escalones que se confunden | Qué incluye |
|---|---|
| **Ejecución material** | **Sólo el coste de ejecutar**: materiales, mano de obra, maquinaria y medios auxiliares |
| **Ejecución por contrata** | **Ejecución material más gastos generales y beneficio industrial, SIN impuestos** |
| **Base de licitación** | **Lo anterior CON el impuesto**: es la cifra que se publica |

| Anatomía de una unidad de obra | Qué es |
|---|---|
| **Código** | **El identificador, que permite ordenar y comparar** |
| **Unidad de medida** | **Metro, metro cuadrado, metro cúbico, kilogramo, unidad, hora** |
| **Resumen** | **La línea corta que aparece en el listado** |
| **Descripción** | **El texto que define qué incluye la unidad y qué no**: es la parte contractual |
| **Descomposición** | **Los elementales y auxiliares con sus rendimientos** |
| **Precio** | **El resultado de la descomposición** |

- **LA PARTE MÁS IMPORTANTE Y LA QUE MENOS SE CUIDA** · `[of]` · **La descripción**: **decide si una
  partida incluye los pequeños accesorios, la mano de obra de puesta en marcha, las pruebas o la
  retirada de escombro.** **Un litigio de obra se gana o se pierde leyendo la descripción de la unidad,
  no su precio.**
- **AVISO SOBRE LAS DESCOMPOSICIONES** · `[of]` · **Los rendimientos de una base de precios general son
  un punto de partida, no un dato.** **Una instalación en edificio en servicio, con trabajo nocturno y
  accesos restringidos, tiene rendimientos muy distintos**, y hay que ajustarlos **o el presupuesto no
  se parecerá a la obra.**

## Las mediciones y sus criterios

- **EL PROBLEMA NO ES CONTAR** · `[of]` · **Es decidir CÓMO se cuenta.**

| Criterio que hay que fijar y escribir | Ejemplo en instalaciones |
|---|---|
| **Qué se mide** | **La tubería: ¿por eje o por desarrollo real con accesorios?** |
| **Qué se descuenta** | **¿Se descuentan los huecos de un falso techo? ¿Los pasos de una bandeja?** |
| **Qué se incluye en el precio** | **¿Los soportes van en la partida de tubería o aparte?** |

- **LA REGLA QUE EVITA EL CONFLICTO** · `[of]` · **El criterio de medición se escribe en la propia
  unidad de obra**, no en un documento aparte. **Así se lee donde se aplica.**

| Estructura de la medición | Qué es |
|---|---|
| **Línea de medición** | **Anotación con su descripción, número de unidades iguales, longitud, anchura y altura** |
| **Subtotal** | **La suma de las líneas de una unidad de obra en un capítulo** |
| **Referencia al plano** | **De qué plano y de qué zona sale esa línea** |

- **LA TERCERA ES LA QUE CASI NADIE RELLENA** · `[of]` · **Una medición sin referencia al plano no se
  puede verificar ni actualizar cuando el plano cambie.** **Es el mismo principio de trazabilidad que
  este temario aplica a sus propias fuentes.**
- **EL AVISO DE MÉTODO QUE CIERRA EL EPÍGRAFE** · `[of]` · **Medir es proyectar por segunda vez.**
  **Quien mide descubre lo que el proyecto no había resuelto** —un tramo que no llega a ningún sitio,
  un cuadro sin alimentación—, y **por eso conviene que mida quien ha proyectado, o al menos que
  hablen.**

## El control de la obra

- **LA SEGUNDA VIDA DE UN PRESUPUESTO** · `[plan]` · **El enunciado dice «diseño y CONTROL DE
  OBRAS»**: **una vez adjudicada la obra, el mismo documento sirve para controlarla.**

| Control | Qué compara |
|---|---|
| **De certificación** | **Lo ejecutado contra lo presupuestado**, mes a mes: es lo que se paga |
| **De coste** | **Lo gastado contra lo previsto**: es lo que interesa al contratista |
| **De plazo** | **Lo avanzado contra la planificación** |

- **QUÉ ES UNA CERTIFICACIÓN, CON PRECISIÓN** · `[of]` · **El documento que recoge la obra ejecutada en
  un periodo, valorada a los precios del contrato, y que da derecho al cobro.** **Se hace midiendo lo
  realmente ejecutado, no lo previsto**, y de ahí que **la medición se rehaga en cada certificación.**

| Concepto que no hay que confundir | Qué es |
|---|---|
| **Precio contradictorio** | **El de una unidad NO prevista en el contrato**, que se fija entre las partes antes de ejecutarla |
| **Modificación del contrato** | **El cambio del objeto o del alcance**, con su régimen jurídico propio |
| **Exceso de medición** | **Más cantidad de una unidad que SÍ estaba prevista** |

- **CONFUNDIRLOS CUESTA CARO** · `[of]` · **El exceso de medición no cambia el contrato; el precio
  contradictorio añade una unidad; la modificación cambia el contrato y tiene límites legales.**

| Planificación · lo que el enunciado no nombra | Qué es |
|---|---|
| **Actividad** | **Una tarea con duración y recursos** |
| **Precedencia** | **Qué tiene que estar hecho antes** |
| **Camino crítico** | **La cadena de actividades cuyo retraso retrasa la obra entera** |
| **Holgura** | **Cuánto puede retrasarse una actividad sin retrasar la obra** |

- **LA CONSECUENCIA PRÁCTICA DEL CAMINO CRÍTICO** · `[of]` · **Acelerar una actividad que no está en él
  no adelanta la obra ni un día**: sólo gasta dinero.
- **EL ENLACE CON LAS MEDICIONES** · `[of]` · **Las actividades de la planificación deberían
  corresponderse con los capítulos y las unidades de obra del presupuesto.** **Cuando no se
  corresponden, el avance físico y el económico dejan de poder compararse**, y el control de obra se
  queda en dos números que nadie sabe relacionar.

## Lo que un proyecto de instalaciones exige

- **EXIGENCIA 1** · `[of]` · **Planos a escala real y por disciplina**, con **esquemas de principio
  además de plantas**: **una instalación no se entiende sólo en planta.**
- **EXIGENCIA 2** · `[norma]` · **Esquemas unifilares y de bloques**, que **el artículo 19 del
  reglamento de baja tensión del tema 7 exige entregar al titular.**
- **EXIGENCIA 3** · `[of]` · **Mediciones con criterio escrito en cada unidad y con referencia al
  plano.**
- **EXIGENCIA 4** · `[of]` · **Un presupuesto cuyos capítulos correspondan a las instalaciones
  reales**, para que **el control de obra sea posible.**
- **EXIGENCIA 5** · `[norma]` · **Documentación final actualizada a lo realmente ejecutado**, que **los
  reglamentos de este anexo piden en forma de certificados, esquemas y manuales.**
- **LA OBSERVACIÓN QUE RESUME LA UTILIDAD DEL PUNTO** · `[of]` · **La herramienta no mejora el
  proyecto; hace posible mantenerlo.** **Un proyecto de instalaciones cambia decenas de veces entre el
  anteproyecto y la recepción**, y **lo que decide si esos cambios llegan coherentes a los planos, a la
  medición y al presupuesto no es el talento del proyectista: es si trabajó con las herramientas
  enlazadas o con tres documentos sueltos.**
