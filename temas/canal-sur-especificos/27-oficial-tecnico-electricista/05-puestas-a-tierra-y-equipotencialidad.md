# Tema 5 del específico de Oficial Técnico Electricista · Puestas a tierra y equipotencialidad: esquemas de conexión, mediciones, continuidad, resistencia de tierra, protección de personas y compatibilidad con equipos sensibles

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Oficial Técnico Electricista · punto 5 |
| **Sirve para** | Puesto 2.27, Oficial Técnico Electricista (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Real Decreto 842/2002, de 2 de agosto, Reglamento electrotécnico para baja tensión: ITC-BT-01, ITC-BT-03 (apéndice I), ITC-BT-05, ITC-BT-08, ITC-BT-18, ITC-BT-19, ITC-BT-24, ITC-BT-26, ITC-BT-27 e ITC-BT-28. Guía técnica del INSST sobre riesgo eléctrico (2020). Lo demás es oficio, y así se declara |
| **Redacción que se estudia** | La vigente el 24/09/2026. ITC-BT-18 en la redacción vigente desde el 23/05/2010 (BOE-A-2010-8190); ITC-BT-05 en la vigente desde el 30/06/2015 (BOE-A-2014-13681); ITC-BT-03 en la vigente desde el 04/09/2025 (BOE-A-2025-17507); las demás instrucciones citadas tienen una sola redacción, la original de 2002 (en vigor desde el 18/09/2003) |
| **Extensión** | Unas 12.600 palabras |

<!-- /portada -->

Siglas y símbolos que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Reglamento electrotécnico para baja
tensión (**REBT**) y sus instrucciones técnicas complementarias (**ITC-BT**); Instituto Nacional de
Seguridad y Salud en el Trabajo (**INSST**); Asociación Española de Normalización (**UNE**) y norma
europea (**EN**); conductor de protección (**CP** o **PE**) y conductor combinado de neutro y
protección (**CPN** o **PEN**); esquemas de conexión a tierra (**TT**, **TN**, **TN-S**, **TN-C**,
**TN-C-S**, **IT**); muy baja tensión de seguridad y de protección (**MBTS** y **MBTP**);
interruptor diferencial (**ID**); sistema de alimentación ininterrumpida (**SAI**); centro de
transformación (**CT**); grado de protección de una envolvente (**IP**, con los códigos **IP XXB**,
**IP2X**, **IP4X** e **IP XXD**). Magnitudes: resistencia de la toma de tierra y de los conductores de
protección de las masas (**RA**), corriente que asegura el funcionamiento de la protección (**Ia**),
corriente diferencial-residual asignada (**IΔn**), corriente de primer defecto (**Id**), impedancia
del bucle de defecto (**Zs**, **Zs'**), tensión entre fase y tierra (**U0**), tensión entre fases o
tensión de contacto límite según el caso (**U**), tensión de contacto límite convencional (**UL**),
resistividad del terreno (**ρ**), perímetro de una placa (**P**), longitud de una pica o de un
conductor (**L**), sección (**S**, **Sp**). Unidades: voltio (**V**), amperio (**A**), miliamperio
(**mA**), ohmio (**Ω**), megaohmio (**MΩ**), ohmio por metro (**Ω·m**), segundo (**s**), metro
(**m**), milímetro cuadrado (**mm²**), hercio (**Hz**).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.27, punto 5):
>
> Puestas a tierra y equipotencialidad: esquemas de conexión, mediciones, continuidad, resistencia
> de tierra, protección de personas y compatibilidad con equipos sensibles.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: la definición de puesta a tierra («sin fusibles ni protección alguna») y
su objeto; las partes de una instalación de puesta a tierra y qué se une al borne principal; los
electrodos admitidos y la profundidad mínima de 0,50 m; las secciones mínimas de los conductores de
tierra enterrados (tabla 1 de la ITC-BT-18) y de protección (tabla 2), y los 2,5 y 4 mm²; el
conductor CPN y la prohibición de volver a unir neutro y protección aguas abajo de su separación;
la sección del conductor principal de equipotencialidad; el significado de cada letra de los
esquemas TT, TN e IT y qué esquema corresponde a una instalación alimentada desde la red pública;
las tensiones de contacto de 24 y 50 V; las condiciones RA × Ia ≤ U, Zs × Ia ≤ U0 y RA × Id ≤ UL,
con sus tiempos; las fórmulas de la tabla 5 (R = ρ/L, R = 2ρ/L, R = 0,8ρ/P); la independencia de dos
tomas de tierra y los 15 m respecto a la tierra del CT; la revisión anual en la época más seca y el
examen cada cinco años; los equipos de medida que la ITC-BT-03 exige; la medida con telurómetro y el
dispositivo de separación; los defectos graves de la ITC-BT-05 que afectan a la tierra; contactos
directos e indirectos y sus medidas; y la relación entre tierra funcional y tierra de protección.
En la prueba práctica: calcular la resistencia máxima de tierra para un diferencial, estimar la de
una pica, describir una medida de tierra, comprobar la continuidad del conductor de protección,
elegir secciones, o diagnosticar un zumbido por bucle de tierra en una sala técnica.

<!-- indice -->

## Índice

- [1. Puestas a tierra y equipotencialidad](#1-puestas-a-tierra-y-equipotencialidad)
  - [1.1 Objeto y definición](#11-objeto-y-definición)
  - [1.2 Las partes de una instalación de puesta a tierra](#12-las-partes-de-una-instalación-de-puesta-a-tierra)
  - [1.3 Tomas de tierra y conductores de tierra](#13-tomas-de-tierra-y-conductores-de-tierra)
  - [1.4 Borne principal y conductores de protección](#14-borne-principal-y-conductores-de-protección)
  - [1.5 Tierra de protección, tierra funcional y conductor CPN](#15-tierra-de-protección-tierra-funcional-y-conductor-cpn)
  - [1.6 La toma de tierra del edificio](#16-la-toma-de-tierra-del-edificio)
  - [1.7 Equipotencialidad](#17-equipotencialidad)
- [2. Esquemas de conexión](#2-esquemas-de-conexión)
  - [2.1 La nomenclatura](#21-la-nomenclatura)
  - [2.2 Los esquemas TN, TT e IT](#22-los-esquemas-tn-tt-e-it)
  - [2.3 Qué esquema se aplica](#23-qué-esquema-se-aplica)
- [3. Mediciones](#3-mediciones)
  - [3.1 Qué se mide y con qué equipos](#31-qué-se-mide-y-con-qué-equipos)
  - [3.2 La medida de la resistencia de tierra con telurómetro](#32-la-medida-de-la-resistencia-de-tierra-con-telurómetro)
  - [3.3 La pinza de tierra](#33-la-pinza-de-tierra)
  - [3.4 Bucle de defecto, diferencial y aislamiento](#34-bucle-de-defecto-diferencial-y-aislamiento)
- [4. Continuidad](#4-continuidad)
  - [4.1 Lo que exige el REBT del conductor de protección](#41-lo-que-exige-el-rebt-del-conductor-de-protección)
  - [4.2 Cómo se comprueba](#42-cómo-se-comprueba)
- [5. Resistencia de tierra](#5-resistencia-de-tierra)
  - [5.1 El valor exigible](#51-el-valor-exigible)
  - [5.2 Resistividad del terreno y estimación](#52-resistividad-del-terreno-y-estimación)
  - [5.3 Tomas de tierra independientes y tierra del centro de transformación](#53-tomas-de-tierra-independientes-y-tierra-del-centro-de-transformación)
  - [5.4 Revisión de las tomas de tierra](#54-revisión-de-las-tomas-de-tierra)
- [6. Protección de personas](#6-protección-de-personas)
  - [6.1 Contactos directos e indirectos](#61-contactos-directos-e-indirectos)
  - [6.2 Corte automático de la alimentación en cada esquema](#62-corte-automático-de-la-alimentación-en-cada-esquema)
  - [6.3 Las demás medidas contra contactos indirectos](#63-las-demás-medidas-contra-contactos-indirectos)
  - [6.4 Tensión de contacto, tensión de defecto y tensión de paso](#64-tensión-de-contacto-tensión-de-defecto-y-tensión-de-paso)
- [7. Compatibilidad con equipos sensibles](#7-compatibilidad-con-equipos-sensibles)
  - [7.1 Lo que dice el REBT](#71-lo-que-dice-el-rebt)
  - [7.2 El bucle de tierra y el zumbido](#72-el-bucle-de-tierra-y-el-zumbido)
  - [7.3 Reglas de oficio en una sala técnica](#73-reglas-de-oficio-en-una-sala-técnica)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Puestas a tierra y equipotencialidad

### 1.1 Objeto y definición

La ITC-BT-18 es la instrucción de la puesta a tierra, y cualquier otra que la exija remite a ella.
Su objeto:

> «**Las puestas a tierra se establecen principalmente con objeto de limitar la tensión que, con
> respecto a tierra, puedan presentar en un momento dado las masas metálicas, asegurar la actuación
> de las protecciones y eliminar o disminuir el riesgo que supone una avería en los materiales
> eléctricos utilizados.**
>
> **Cuando otras instrucciones técnicas prescriban como obligatoria la puesta a tierra de algún
> elemento o parte de la instalación, dichas puestas a tierra se regirán por el contenido de la
> presente instrucción.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 1.

Y la definición, que es la cita del tema:

> «**La puesta o conexión a tierra es la unión eléctrica directa, sin fusibles ni protección alguna,
> de una parte del circuito eléctrico o de una parte conductora no perteneciente al mismo mediante
> una toma de tierra con un electrodo o grupos de electrodos enterrados en el suelo.**
>
> **Mediante la instalación de puesta a tierra se deberá conseguir que en el conjunto de
> instalaciones, edificios y superficie próxima del terreno no aparezcan diferencias de potencial
> peligrosas y que, al mismo tiempo, permita el paso a tierra de las corrientes de defecto o las de
> descarga de origen atmosférico.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 2.

Las palabras que hay que subrayar son «sin fusibles ni protección alguna», y hay que saber decir
por qué (oficio): un conductor de protección con un fusible sería un conductor de protección que
puede quedar interrumpido sin que nadie se entere. La tierra tiene que ser un camino permanente,
incondicional y comprobable. La misma instrucción lo repite para el conductor de protección
(epígrafe 1.4): **Ningún aparato deberá ser intercalado en el conductor de protección**.

Los términos que el tema usa, en la ITC-BT-01:

| Término | Definición (ITC-BT-01) |
|---|---|
| Tierra | **Masa conductora de la tierra en la que el potencial eléctrico en cada punto se toma, convencionalmente, igual a cero.** |
| Toma de tierra | **Electrodo, o conjunto de electrodos, en contacto con el suelo y que asegura la conexión eléctrica con el mismo.** |
| Masa | **Conjunto de las partes metálicas de un aparato que, en condiciones normales, están aisladas de las partes activas.** |
| Elemento conductor ajeno a la instalación eléctrica | **Elemento que no forma parte de la instalación eléctrica y que es susceptible de introducir un potencial, generalmente el de tierra.** |
| Borne o barra principal de tierra | **Borne o barra prevista para la conexión a los dispositivos de puesta a tierra de los conductores de protección, incluyendo los conductores de equipotencialidad y eventualmente los conductores de puesta a tierra funcional.** |
| Resistencia de puesta a tierra | **Relación entre la tensión que alcanza con respecto a un punto a potencial cero una instalación de puesta a tierra y la corriente que la recorre.** |
| Resistencia global o total de tierra | **Es la resistencia de tierra medida en un punto, considerando la acción conjunta de la totalidad de las puestas a tierra.** |
| Tierra lejana | **Electrodo de tierra conectado a un aparato y situado a una distancia suficiente del mismo para que sea independiente de cualquier otro electrodo de tierra situado cerca del aparato.** |

La definición de masa sigue con lo que «comprenden normalmente», y de ahí sale una regla que se
pregunta: **son masas las partes metálicas accesibles de los materiales eléctricos, excepto los de
Clase II**, y la nota final: **Una parte conductora que sólo puede ser puesta bajo tensión en caso de
fallo a través de una masa, no puede considerarse como una masa.**

### 1.2 Las partes de una instalación de puesta a tierra

La ITC-BT-18 (apartado 3, figura 1) representa las partes típicas. En orden desde el terreno:

| Parte | Qué es | Dónde se regula |
|---|---|---|
| Toma de tierra (electrodo) | Lo enterrado: barras, tubos, pletinas, conductores desnudos, placas, anillos o mallas, armaduras de hormigón | ITC-BT-18, 3.1 |
| Conductor de tierra | Une la toma de tierra con el borne principal | ITC-BT-18, 3.2 |
| Borne principal de tierra, con el dispositivo que permite medir | Punto de reunión de todos los conductores | ITC-BT-18, 3.3 |
| Conductores de protección | Del borne a cada masa | ITC-BT-18, 3.4 |
| Conductores de equipotencialidad | Unen masas y elementos conductores entre sí y con el borne | ITC-BT-18, 8 |

Antes de entrar en cada parte, el apartado 3 fija cuatro condiciones a la elección de los materiales,
que son las que justifican todo lo que viene después:

> «**– El valor de la resistencia de puesta a tierra esté conforme con las normas de protección y de
> funcionamiento de la instalación y se mantenga de esta manera a lo largo del tiempo, teniendo en
> cuenta los requisitos generales indicados en la ITC-BT-24 y los requisitos particulares de las
> Instrucciones Técnicas aplicables a cada instalación.**
> **– Las corrientes de defecto a tierra y las corrientes de fuga puedan circular sin peligro,
> particularmente desde el punto de vista de solicitaciones térmicas, mecánicas y eléctricas.**
> **– La solidez o la protección mecánica quede asegurada con independencia de las condiciones
> estimadas de influencias externas.**
> **– Contemplen los posibles riesgos debidos a electrólisis que pudieran afectar a otras partes
> metálicas.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 3.

La primera condición contiene la idea del mantenimiento: la resistencia tiene que mantenerse «a lo
largo del tiempo», y por eso hay revisión periódica (epígrafe 5.4).

### 1.3 Tomas de tierra y conductores de tierra

Electrodos admitidos (ITC-BT-18, 3.1): **barras, tubos; pletinas, conductores desnudos; placas;
anillos o mallas metálicas constituidos por los elementos anteriores o sus combinaciones; armaduras
de hormigón enterradas; con excepción de las armaduras pretensadas; otras estructuras enterradas que
se demuestre que son apropiadas** (en la norma, cada uno es un guion de una lista).

Las reglas del mismo apartado que se preguntan:

- Profundidad: **La profundidad nunca será inferior a 0,50 m.** Y el porqué está en la frase
  anterior: **la posible pérdida de humedad del suelo, la presencia del hielo u otros efectos
  climáticos, no aumenten la resistencia de la toma de tierra por encima del valor previsto.**
- Cobre: **Los conductores de cobre utilizados como electrodos serán de construcción y resistencia
  eléctrica según la clase 2 de la norma UNE 21.022.**
- Lo que no vale: **Las canalizaciones metálicas de otros servicios (agua, líquidos o gases
  inflamables, calefacción central, etc.) no deben ser utilizadas como tomas de tierra por razones
  de seguridad.**
- Lo que vale con permiso: las envolventes de plomo y otras envolventes de cables poco sensibles a
  la corrosión **pueden ser utilizadas como toma de tierra, previa autorización del propietario**.

**Conductores de tierra** (ITC-BT-18, 3.2). Su sección cumple lo del apartado 3.4 y, si van
enterrados, la tabla 1; y **La sección no será inferior a la mínima exigida para los conductores de
protección.**

Tabla 1 de la ITC-BT-18, «Secciones mínimas convencionales de los conductores de tierra»:

| Tipo | Protegido mecánicamente | No protegido mecánicamente |
|---|---|---|
| Protegido contra la corrosión (*) | **Según apartado 3.4** | **16 mm2 Cobre** / **16 mm2 Acero Galvanizado** |
| No protegido contra la corrosión | **25 mm2 Cobre** / **50 mm2 Hierro** | **25 mm2 Cobre** / **50 mm2 Hierro** |

(*) **La protección contra la corrosión puede obtenerse mediante una envolvente**

La fila «no protegido contra la corrosión» aparece en el BOE con un solo par de valores para las dos
columnas; la tabla los repite en ambas porque no distingue protección mecánica en ese caso. La
lectura práctica (oficio): un conductor de tierra de cobre desnudo directamente enterrado necesita
25 mm² como mínimo.

Y la ejecución: **Durante la ejecución de las uniones entre conductores de tierra y electrodos de
tierra debe extremarse el cuidado para que resulten eléctricamente correctas.** **Debe cuidarse, en
especial, que las conexiones, no dañen ni a los conductores ni a los electrodos de tierra.**

### 1.4 Borne principal y conductores de protección

**Borne principal** (ITC-BT-18, 3.3). **En toda instalación de puesta a tierra debe preverse un borne
principal de tierra, al cual deben unirse los conductores siguientes:**

- **Los conductores de tierra,**
- **Los conductores de protección.**
- **Los conductores de unión equipotencial principal.**
- **Los conductores de puesta a tierra funcional, si son necesarios.**

Y el detalle que un examen persigue, porque es el que hace posible la medida del epígrafe 3.2:

> «**Debe preverse sobre los conductores de tierra y en lugar accesible, un dispositivo que permita
> medir la resistencia de la toma de tierra correspondiente. Este dispositivo puede estar combinado
> con el borne principal de tierra, debe ser desmontable necesariamente por medio de un útil, tiene
> que ser mecánicamente seguro y debe asegurar la continuidad eléctrica.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 3.3.

Cuatro condiciones: accesible, desmontable sólo con útil, mecánicamente seguro y sin perder la
continuidad. Sin poder separar el electrodo del resto no se mide su resistencia aislada (oficio;
epígrafe 3.2).

**Conductores de protección** (ITC-BT-18, 3.4). **Los conductores de protección sirven para unir
eléctricamente las masas de una instalación a ciertos elementos con el fin de asegurar la protección
contra contactos indirectos.** También se llaman así los que unen las masas **al neutro de la red** y
**a un relé de protección**.

Sección: **la indicada en la tabla 2, o se obtendrá por cálculo conforme a lo indicado en la Norma
UNE 20.460 -5-54 apartado 543.1.1.**

Tabla 2 de la ITC-BT-18 (la misma relación da la tabla 2 de la ITC-BT-19, apartado 2.3):

| Sección de los conductores de fase, S (mm²) | Sección mínima de los conductores de protección, Sp (mm²) |
|---|---|
| **S ≤ 16** | **Sp= S** |
| **16 < S ≤ 35** | **Sp= 16** |
| **S > 35** | **Sp= S/2** |

Las reglas que acompañan a la tabla:

- **Si la aplicación de la tabla conduce a valores no normalizados, se han de utilizar conductores
  que tengan la sección normalizada superior más próxima.**
- La tabla sólo vale si el conductor de protección es del mismo material que los activos; si no, se
  busca **una conductividad equivalente**.
- Los que no forman parte de la canalización de alimentación **serán de cobre con una sección, al
  menos de: 2,5 mm2, si los conductores de protección disponen de una protección mecánica. 4 mm2, si
  los conductores de protección no disponen de una protección mecánica.**
- **Cuando el conductor de protección sea común a varios circuitos, la sección de ese conductor debe
  dimensionarse en función de la mayor sección de los conductores de fase.**
- Lo que no puede ser conductor de protección: **Otros conductos (agua, gas u otros tipos) o
  estructuras metálicas, no pueden utilizarse como conductores de protección (CP ó CPN).** Sí pueden
  serlo las envolventes de conjuntos montados en fábrica y las canalizaciones prefabricadas con
  envolvente metálica que cumplan a la vez las tres condiciones del apartado (continuidad no afectada
  por deterioros, conductibilidad suficiente y posibilidad de conectar otros conductores de protección
  en cada derivación).

Ejemplo de aplicación. Una línea trifásica de 50 mm² de cobre a un cuadro secundario: Sp = 50/2 =
25 mm². Una de 25 mm²: Sp = 16 mm². Un circuito de tomas de 2,5 mm²: Sp = 2,5 mm².

La identificación por color es de la ITC-BT-19, 2.2.4: **Al conductor de protección se le
identificará por el color verde-amarillo.** El neutro, **azul claro**; las fases, **marrón o negro**,
y **gris** si hay que distinguir una tercera.

### 1.5 Tierra de protección, tierra funcional y conductor CPN

La ITC-BT-18 distingue para qué se pone a tierra algo, y esa distinción es la base de la
compatibilidad con equipos sensibles del epígrafe 7:

> «**4. PUESTA A TIERRA POR RAZONES DE PROTECCIÓN**
> **Para las medidas de protección en los esquemas TN, TT e IT, ver la ITC-BT 24.**
> **Cuando se utilicen dispositivos de protección contra sobreintensidades para la protección contra
> el choque eléctrico, será preceptiva la incorporación del conductor de protección en la misma
> canalización que los conductores activos o en su proximidad inmediata.**
> (…)
> **5. PUESTA A TIERRA POR RAZONES FUNCIONALES**
> **Las puestas a tierra por razones funcionales deben ser realizadas de forma que aseguren el
> funcionamiento correcto del equipo y permitan un funcionamiento correcto y fiable de la
> instalación.**
> **6. PUESTA A TIERRA POR RAZONES COMBINADAS DE PROTECCIÓN Y FUNCIONALES**
> **Cuando la puesta a tierra sea necesaria a la vez por razones de protección y funcionales,
> prevalecerán las prescripciones de las medidas de protección.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartados 4, 5 y 6.

El apartado 4.1 añade un caso particular que se cita poco: la toma de tierra auxiliar de un
dispositivo de control de tensión de defecto **debe ser eléctricamente independiente de todos los
elementos metálicos puestos a tierra**, y su unión **debe estar aislada**.

**Conductor CPN** (ITC-BT-18, apartado 7). Reúne las funciones de neutro y protección y sólo cabe en
esquema TN:

- **En el esquema TN, cuando en las instalaciones fijas el conductor de protección tenga una sección
  al menos igual a 10 mm2, en cobre o aluminio, las funciones de conductor de protección y de
  conductor neutro pueden ser combinadas, a condición de que la parte de la instalación común no se
  encuentre protegida por un dispositivo de protección de corriente diferencial residual.**
- Excepción: **4 mm2, a condición de que el cable sea de cobre y del tipo concéntrico** y con las
  conexiones duplicadas.
- **El conductor CPN debe estar aislado para la tensión más elevada a la que puede estar sometido, con
  el fin de evitar las corriente de fuga.** (sic: «las corriente»).
- Y la regla que más se pregunta y más se incumple:

> «**Si a partir de un punto cualquiera de la instalación, el conductor neutro y el conductor de
> protección están separados, no estará permitido conectarlos entre sí en la continuación del
> circuito por detrás de este punto. En el punto de separación, deben preverse bornes o barras
> separadas para el conductor de protección y para el conductor neutro. El conductor CPN debe estar
> unido al borne o a la barra prevista para el conductor de protección.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 7.

### 1.6 La toma de tierra del edificio

La ITC-BT-26 (instalaciones interiores en viviendas, aplicable también, **en la medida que pueda
afectarles, a las de locales comerciales, de oficinas y a las de cualquier otro local destinado a
fines análogos**) describe cómo se hace la toma de tierra de un edificio nuevo:

> «**En toda nueva edificación se establecerá una toma de tierra de protección, según el siguiente
> sistema:**
> **Instalando en el fondo de las zanjas de cimentación de los edificios, y antes de empezar ésta, un
> cable rígido de cobre desnudo de una sección mínima según se indica en la ITC-BT-18, formando un
> anillo cerrado que interese a todo el perímetro del edificio. A este anillo deberán conectarse
> electrodos verticalmente hincados en el terreno cuando, se prevea la necesidad de disminuir la
> resistencia de tierra que pueda presentar el conductor en anillo. Cuando se trate de construcciones
> que comprendan varios edificios próximos, se procurará unir entre sí los anillos que forman la toma
> de tierra de cada uno de ellos, con objeto de formar una malla de la mayor extensión posible.**»
>
> — Real Decreto 842/2002, ITC-BT-26, apartado 3.1.

Del mismo apartado: al anillo o a los electrodos se conecta la estructura metálica o, con zapatas de
hormigón armado, **un cierto número de hierros de los considerados principales y como mínimo uno por
zapata**, uniones que se harán **mediante soldadura aluminotérmica o autógena**. En rehabilitación,
la toma puede hacerse con electrodos en patios de luces o jardines.

Qué se conecta a esa tierra (apartado 3.2): **toda masa metálica importante, existente en la zona
de la instalación**, las masas de los receptores que lo exijan y **las partes metálicas de los
depósitos de gasóleo, de las instalaciones de calefacción general, de las instalaciones de agua, de
las instalaciones de gas canalizado y de las antenas de radio y televisión.**

**Líneas principales de tierra** (apartado 3.4): de cobre, con la sección de los conductores de
protección de la ITC-BT-19 **con un mínimo de 16 milímetros cuadrados**. Y no pueden usarse como
conductores de tierra **las tuberías de agua, gas, calefacción, desagües, conductos de evacuación de
humos o basuras, ni las cubiertas metálicas de los cables** (…) **ni las partes conductoras de los
sistemas de conducción de los cables, tubos, canales y bandejas.**

La última exclusión importa en una sala técnica (oficio): la bandeja metálica es una masa que se
une al conductor de protección, pero no sustituye a ese conductor.

### 1.7 Equipotencialidad

La definición de la ITC-BT-01: **Conexión eléctrica que pone al mismo potencial, o a potenciales
prácticamente iguales, a las partes conductoras accesibles y elementos conductores.** Y **Conductor
equipotencial**: **Conductor de protección que asegura una conexión equipotencial.**

La idea de fondo (oficio): unir entre sí todas las masas y elementos conductores de una zona hace que,
si aparece una tensión, todo suba a la vez y no haya diferencia de potencial entre dos cosas que una
persona pueda tocar al mismo tiempo. La seguridad no está en que no haya tensión, sino en que no haya
diferencia de tensión.

Las secciones (ITC-BT-18, apartado 8):

> «**El conductor principal de equipotencialidad debe tener una sección no inferior a la mitad de la
> del conductor de protección de sección mayor de la instalación, con un mínimo de 6 mm2. Sin embargo,
> su sección puede ser reducida a 2,5 mm2, si es de cobre.**
> **Si el conductor suplementario de equipotencialidad uniera una masa a un elemento conductor, su
> sección no será inferior a la mitad de la del conductor de protección unido a esta masa.**
> **La unión de equipotencialidad suplementaria puede estar asegurada, bien por elementos conductores
> no desmontables, tales como estructuras metálicas no desmontables, bien por conductores
> suplementarios, o por combinación de los dos.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 8.

La segunda frase del primer párrafo está así en el BOE: no dice en qué condición se admite reducir a
2,5 mm² el de cobre, y el tema no lo completa.

Dos tipos, por tanto:

| | Principal | Suplementaria |
|---|---|---|
| Qué une | Los elementos conductores que entran en el edificio (tuberías, estructura) con el borne principal de tierra (oficio, a partir de la lista del 3.3) | Una masa con un elemento conductor cercano, en un local concreto |
| Sección | ≥ mitad del conductor de protección mayor; mínimo 6 mm² | ≥ mitad del conductor de protección de esa masa |

El caso típico de equipotencialidad suplementaria está en la ITC-BT-27 (baños y duchas, que hay en
vestuarios de cualquier centro de trabajo): **Una conexión equipotencial local suplementaria debe
unir el conductor de protección asociado con las partes conductoras accesibles de los equipos de
clase I en los volúmenes 1, 2 y 3, incluidas las tomas de corriente** y las partes conductoras
externas que la instrucción enumera (canalizaciones metálicas de agua, gas, calefacción y aire
acondicionado, partes metálicas accesibles de la estructura y **Otras partes conductoras externas,
por ejemplo partes que son susceptibles de transferir tensiones**) (apartado 2.2).

Y un caso distinto que no debe confundirse: las **conexiones equipotenciales locales no conectadas a tierra**
de la ITC-BT-24, 4.4, que son una medida de protección en sí mismas (epígrafe 6.3).

La falta de conexiones equipotenciales es defecto grave en una inspección: la ITC-BT-05, 6.2,
incluye **Falta de conexiones equipotenciales, cuando éstas fueran requeridas**.

## 2. Esquemas de conexión

### 2.1 La nomenclatura

No se puede elegir una protección sin saber en qué esquema se está, y la ITC-BT-08 lo dice de
entrada: **Para la determinación de las características de las medidas de protección contra
choques eléctricos en caso de defecto (contactos indirectos) y contra sobreintensidades, así como de
las especificaciones de la aparamenta encargada de tales funciones, será preciso tener en cuenta el
esquema de distribución empleado.**

El código de letras (ITC-BT-08, apartado 1), que es lo más preguntable del epígrafe:

| Letra | Posición | Significado (ITC-BT-08) |
|---|---|---|
| T | Primera: la alimentación respecto a tierra | **Conexión directa de un punto de la alimentación a tierra.** |
| I | Primera | **Aislamiento de todas las partes activas de la alimentación con respecto a tierra o conexión de un punto a tierra a través de una impedancia.** |
| T | Segunda: las masas de la instalación receptora respecto a tierra | **Masas conectadas directamente a tierra, independientemente de la eventual puesta a tierra de la alimentación.** |
| N | Segunda | **Masas conectadas directamente al punto de la alimentación puesto a tierra (en corriente alterna, este punto es normalmente el punto neutro).** |
| S | Otras letras: neutro y protección | **Las funciones de neutro y de protección, aseguradas por conductores separados.** |
| C | Otras letras | **Las funciones de neutro y de protección, combinadas en un solo conductor (conductor CPN).** |

### 2.2 Los esquemas TN, TT e IT

**Esquema TN** (ITC-BT-08, 1.1): **un punto de la alimentación, generalmente el neutro o
compensador, conectado directamente a tierra y las masas de la instalación receptora conectadas a
dicho punto mediante conductores de protección.** Tres variantes:

| Variante | Definición (ITC-BT-08, 1.1) |
|---|---|
| TN-S | **el conductor neutro y el de protección son distintos en todo el esquema** |
| TN-C | **las funciones de neutro y protección están combinados en un solo conductor en todo el esquema** |
| TN-C-S | **las funciones de neutro y protección están combinadas en un solo conductor en una parte del esquema** |

Y la consecuencia: **En los esquemas TN cualquier intensidad de defecto franco fase-masa es una
intensidad de cortocircuito. El bucle de defecto está constituido exclusivamente por elementos
conductores metálicos.**

**Esquema TT** (ITC-BT-08, 1.2): **un punto de alimentación, generalmente el neutro o compensador,
conectado directamente a tierra. Las masas de la instalación receptora están conectadas a una toma
de tierra separada de la toma de tierra de la alimentación.** Y la consecuencia: **las intensidades
de defecto fase-masa o fase-tierra pueden tener valores inferiores a los de cortocircuito, pero
pueden ser suficientes para provocar la aparición de tensiones peligrosas.** La misma instrucción
aclara que, aunque las dos tomas no sean del todo independientes, **el esquema sigue siendo un
esquema TT si no se cumplen todas las condiciones del esquema TN.**

**Esquema IT** (ITC-BT-08, 1.3): **no tiene ningún punto de la alimentación conectado directamente a
tierra. Las masas de la instalación receptora están puestas directamente a tierra.** Su
característica: **la intensidad resultante de un primer defecto fase-masa o fase-tierra, tiene un
valor lo suficientemente reducido como para no provocar la aparición de tensiones de contacto
peligrosas.** La limitación se logra sin conexión a tierra o con **una impedancia suficiente**, y
**puede resultar necesario limitar la extensión de la instalación para disminuir el efecto
capacitivo de los cables con respecto a tierra.** Y una recomendación que se pregunta: **En este
tipo de esquema se recomienda no distribuir el neutro.**

Resumen para el examen (lectura de oficio sobre lo citado):

| Esquema | Defecto fase-masa | Qué protege en la práctica |
|---|---|---|
| TN | Es un cortocircuito: bucle todo metálico | Automáticos y fusibles, si el bucle es suficientemente bajo; si no, diferencial (nunca en TN-C) |
| TT | Menor que un cortocircuito: el bucle pasa por dos tomas de tierra | El diferencial; los dispositivos de máxima corriente **solamente son aplicables cuando la resistencia RA tiene un valor muy bajo** (ITC-BT-24, 4.1.2) |
| IT | Muy pequeño en el primer defecto | Un controlador permanente de aislamiento avisa; el segundo defecto sí se corta |

### 2.3 Qué esquema se aplica

La ITC-BT-08, apartado 1.4, dice que la elección **debe hacerse en función de las características
técnicas y económicas de cada instalación**, con tres principios:

> «**a) Las redes de distribución pública de baja tensión tienen un punto puesto directamente a
> tierra por prescripción reglamentaria. Este punto es el punto neutro de la red. El esquema de
> distribución para instalaciones receptoras alimentadas directamente de una red de distribución
> pública de baja tensión es el esquema TT.**
> **b) En instalaciones alimentadas en baja tensión, a partir de un centro de transformación de
> abonado, se podrá elegir cualquiera de los tres esquemas citados.**
> **c) No obstante lo dicho en a), puede establecerse un esquema IT en parte o partes de una
> instalación alimentada directamente de una red de distribución pública mediante el uso de
> transformadores adecuados, en cuyo secundario y en la parte de la instalación afectada se
> establezcan las disposiciones que para tal esquema se citan en el apartado 1.3.**»
>
> — Real Decreto 842/2002, ITC-BT-08, apartado 1.4.

Aplicación a un centro de producción. Un edificio que se alimenta en baja tensión de la red pública
es TT y el diferencial es la protección contra contactos indirectos. Un centro grande con CT propio
puede ser TN-S o, en partes, IT; en qué esquema está cada edificio de la RTVA y de CSRTV no consta en
ningún documento publicado, y lo primero que hace un electricista que llega a una instalación es
averiguarlo (oficio): mirar el esquema unifilar, el cuadro general y si el neutro y el conductor de
protección vienen separados o unidos.

El IT tiene sentido donde una interrupción es peor que el defecto, porque es el único de los tres en
que, según la ITC-BT-24, 4.1.3, con un solo defecto **no es imperativo el corte**. El REBT lo prefiere
para los servicios de seguridad: **Se elegirán preferentemente medidas de protección contra los
contactos indirectos sin corte automático al primer defecto. En el esquema IT debe preverse un
controlador permanente de aislamiento que al primer defecto emita una señal acústica o visual.**
(ITC-BT-28, apartado 2.1). En los quirófanos, la ITC-BT-38 hace obligatorio el **transformador de
aislamiento** con dispositivo de vigilancia del nivel de aislamiento. Que un control de emisión se
alimente así es una decisión de proyecto que no consta en ningún documento publicado de la RTVA.

Para el esquema TN aplicado a la red de distribución, la ITC-BT-08, apartado 2, exige
prescripciones especiales a la red (sección mínima del neutro según tabla 1, puesta a tierra del
neutro en los extremos de líneas de más de 200 m, **La resistencia de tierra del neutro no será
superior a 5 ohmios en las proximidades de la central generadora o del centro de transformación, así
como en los 200 últimos metros de cualquier derivación de la red** y **La resistencia global de
tierra, de todas las tomas de tierra del neutro, no será superior a 2 ohmios**). Son condiciones de
la red de alimentación, no de la instalación interior.

## 3. Mediciones

### 3.1 Qué se mide y con qué equipos

Las verificaciones previas a la puesta en servicio las hace la empresa instaladora (ITC-BT-05, 2.1)
**siguiendo la metodología de la norma UNE 20.460 -6-61** (ITC-BT-05, 3), que el tema no ha leído.
Lo que sí dice el REBT es qué equipos debe tener como mínimo una empresa instaladora de categoría
básica (ITC-BT-03, apéndice I, 2.1.2). Los que tocan a este tema:

- **Telurómetro;**
- **Medidor de aislamiento, según ITC MIE-BT 19;** (la referencia es al reglamento anterior; la
  medida de aislamiento vigente está en la ITC-BT-19, 2.9)
- **Medidor de corrientes de fuga, con resolución mejor o igual que 1 mA;**
- **Equipo verificador de la sensibilidad de disparo de los interruptores diferenciales, capaz de
  verificar la característica intensidad-tiempo;**
- **Equipo verificador de la continuidad de conductores;**
- **Medidor de impedancia de bucle, con sistema de medición independiente o con compensación del
  valor de la resistencia de los cables de prueba y con una resolución mejor o igual que 0,1 Ω;**

Lo que mide cada uno en relación con la tierra (oficio):

| Medida | Equipo | Estado de la instalación |
|---|---|---|
| Resistencia de la toma de tierra | Telurómetro (o pinza de tierra, con sus límites) | Electrodo separado por el dispositivo del borne principal |
| Continuidad del conductor de protección y de las equipotenciales | Verificador de continuidad (óhmetro de baja resistencia) | Sin tensión |
| Impedancia del bucle de defecto | Medidor de bucle | En tensión |
| Disparo del diferencial | Verificador de diferenciales | En tensión |
| Corriente de fuga | Pinza de fugas | En servicio, con los equipos conectados |
| Aislamiento | Medidor de aislamiento | Sin tensión y con los receptores desconectados |

Antes de medir hay que decidir si se mide en tensión o sin ella; si es sin tensión, se aplican las
cinco reglas de oro, y la comprobación de ausencia de tensión es ella misma una medida en tensión
(tema 15). Los propios instrumentos y su manejo son del tema 14.

### 3.2 La medida de la resistencia de tierra con telurómetro

Qué se mide: la resistencia entre el electrodo y el terreno lejano, es decir, la oposición que el
terreno ofrece a que una corriente de defecto se disipe; es la «resistencia de puesta a tierra» de
la ITC-BT-01 (relación entre la tensión que alcanza la instalación de tierra respecto a un punto a
potencial cero y la corriente que la recorre). El REBT no describe el método; lo que sigue es el
método de oficio con dos picas auxiliares:

| Paso | Qué se hace |
|---|---|
| 1 | Separar el electrodo del resto de la instalación, por el dispositivo de medida del borne principal (ITC-BT-18, 3.3), con la instalación en condiciones de seguridad |
| 2 | Clavar dos picas auxiliares alineadas con el electrodo: una de corriente, lejos, y una de tensión, entre medias |
| 3 | Inyectar una corriente conocida entre el electrodo y la pica de corriente |
| 4 | Medir la tensión entre el electrodo y la pica de tensión |
| 5 | Dividir tensión entre corriente: eso es la resistencia |

La regla que hace válida la medida: la pica de tensión tiene que estar en la zona de potencial nulo,
fuera de la influencia del electrodo y de la pica de corriente. La comprobación práctica es mover la
pica de tensión y ver si la lectura cambia: si al desplazarla la lectura se mantiene, la medida es
buena; si cambia, las picas están demasiado cerca. Las distancias concretas entre picas las da el
fabricante del telurómetro o la norma de método, que el tema no ha leído.

Los dos avisos de método que hacen la medida honesta:

1. Si no se separa el electrodo, no se mide el electrodo. Lo que se mide es el paralelo de ese
   electrodo con todo lo que esté unido a él (otras tomas, armaduras, canalizaciones unidas por la
   equipotencialidad), y eso da un valor menor y falso. Es lo que la ITC-BT-01 llama **resistencia
   global o total de tierra**.
2. La resistencia de tierra varía con la humedad del terreno. Una medida en primavera después de
   llover y otra en agosto no dan lo mismo, y el valor que hay que garantizar es el del caso más
   desfavorable. Por eso la ITC-BT-18, 12, pide la comprobación anual **en la época en la que el
   terreno esté mas seco** (epígrafe 5.4), y su apartado 3.1 hace profundo el electrodo para que **la
   posible pérdida de humedad del suelo** no aumente la resistencia por encima de lo previsto.

Después de medir, el dispositivo de separación se vuelve a cerrar y se comprueba la continuidad; una
instalación que se queda con el electrodo desconectado después de la medida no tiene tierra
(oficio).

Lo que se anota (oficio): fecha, condiciones del terreno (seco, húmedo, tras lluvia), método,
posiciones de las picas, valor leído y comparación con la medida anterior. Una resistencia que sube
año tras año en las mismas condiciones avisa de corrosión del electrodo o de una conexión floja.

### 3.3 La pinza de tierra

La alternativa sin picas es la medida con pinza de tierra, que inyecta y mide sobre el propio
conductor de tierra (oficio). Su ventaja: no hay que clavar nada ni separar el electrodo. Su límite:
necesita un bucle, es decir, otro camino de retorno a tierra en paralelo (en la práctica, las demás
tomas unidas a la que se mide), y por eso no vale en un electrodo único y aislado. Lo que mide es la
resistencia del electrodo en serie con la del resto del bucle, y sólo se aproxima a la del electrodo
cuando las demás tomas en paralelo tienen en conjunto una resistencia mucho menor (oficio).

### 3.4 Bucle de defecto, diferencial y aislamiento

Tres medidas completan la comprobación de la protección de personas, y las tres se entienden desde
las condiciones de la ITC-BT-24 del epígrafe 6.2 (el manejo del instrumento es del tema 14):

- Impedancia del bucle de defecto (Zs): en esquema TN decide si el automático o el fusible
  disparan a tiempo (Zs × Ia ≤ U0). El medidor la da en tensión, entre fase y conductor de
  protección. La ITC-BT-03 le pide resolución de 0,1 Ω.
- Disparo del diferencial: el verificador inyecta una corriente de defecto controlada y mide si
  dispara y en cuánto tiempo; es la comprobación que la ITC-BT-03 llama **característica
  intensidad-tiempo**. El botón de prueba del propio diferencial sólo comprueba el mecanismo (tema 3).
  Muchos verificadores dan además la tensión de contacto que aparecería con la corriente asignada,
  que es la comprobación directa de RA × Ia ≤ U (oficio).
- Aislamiento: valores de la ITC-BT-19, 2.9, tabla 3: para instalaciones de tensión nominal
  **Inferior o igual a 500 V, excepto caso anterior**, tensión de ensayo **500** V en continua y
  resistencia de aislamiento **≥ 0,5** MΩ. **El aislamiento se medirá con relación a tierra y entre
  conductores**, y para lo que importa en el epígrafe 7: **Cuando la instalación tenga circuitos con
  dispositivos electrónicos, en dichos circuitos los conductores de fases y el neutro estarán unidos
  entre sí durante las medidas.** El resto de la medida de aislamiento es del tema 14.

## 4. Continuidad

### 4.1 Lo que exige el REBT del conductor de protección

La tierra protege sólo si el camino desde cada masa hasta el electrodo es continuo. El REBT lo
asegura con reglas de construcción (ITC-BT-18, 3.4):

- **Ningún aparato deberá ser intercalado en el conductor de protección, aunque para los ensayos
  podrán utilizarse conexiones desmontables mediante útiles adecuados.**
- **Las masas de los equipos a unir con los conductores de protección no deben ser conectadas en
  serie en un circuito de protección**, salvo envolventes montadas en fábrica o canalizaciones
  prefabricadas. La razón (oficio): con masas en serie, desconectar un equipo deja sin tierra a todos
  los que están detrás.
- **Las conexiones deben ser accesibles para la verificación y ensayos**, salvo las de cajas selladas
  con relleno o cajas no desmontables con juntas estancas.
- **Los conductores de protección deben estar convenientemente protegidos contra deterioros
  mecánicos, químicos y electroquímicos y contra los esfuerzos electrodinámicos.**

Y la ITC-BT-19, 2.3, sobre su instalación:

- **Las conexiones en estos conductores se realizarán por medio de uniones soldadas sin empleo de
  ácido o por piezas de conexión de apriete por rosca, debiendo ser accesibles para verificación y
  ensayo. Estas piezas serán de material inoxidable y los tornillos de apriete, si se usan, estarán
  previstos para evitar su desapriete.**
- **Se tomarán las precauciones necesarias para evitar el deterioro causado por efectos
  electroquímicos cuando las conexiones sean entre metales diferentes (por ejemplo cobre-aluminio).**
- **No se utilizará un conductor de protección común para instalaciones de tensiones nominales
  diferentes.**
- **En una canalización móvil todos los conductores incluyendo el conductor de protección, irán por la
  misma canalización** (lo que en una unidad móvil o en un plató significa que la manguera lleva su
  conductor de protección).

La falta de continuidad pesa en una inspección. La ITC-BT-05, 6.2, enumera entre los **defectos
graves** cuatro que son de este tema:

- **Falta de continuidad de los conductores de protección;**
- **Valores elevados de resistencia de tierra en relación con las medidas de seguridad adoptadas.**
- **Defectos en la conexión de los conductores de protección a las masas, cuando estas conexiones
  fueran preceptivas;**
- **Sección insuficiente de los conductores de protección;**

a los que se suman la **Falta de conexiones equipotenciales, cuando éstas fueran requeridas**, la
**Inexistencia de medidas adecuadas de seguridad contra contactos indirectos** y la **Falta de
identificación de los conductores "neutro" y "de protección"**. Defecto grave es **el que no supone
un peligro inmediato para la seguridad de las personas o de los bienes, pero puede serlo al
originarse un fallo en la instalación** (ITC-BT-05, 6.2): un conductor de protección cortado no se
nota hasta que hay un defecto de aislamiento.

### 4.2 Cómo se comprueba

La comprobación (oficio, con el equipo que exige la ITC-BT-03):

1. Sin tensión y con las reglas de oro aplicadas.
2. Con el verificador de continuidad, que inyecta una corriente de prueba y mide resistencias bajas,
   se mide entre el borne principal de tierra (o la barra de tierra del cuadro) y cada masa, y entre
   las masas y elementos conductores unidos por equipotencialidad.
3. Se compensa antes la resistencia de los propios cables de prueba.
4. El valor esperado es el de un conductor de cobre de esa sección y longitud: muy bajo. Una lectura
   alta o inestable delata una conexión floja, oxidada o un conductor cortado; una lectura «infinita»,
   una masa sin tierra.
5. Se comprueba también la continuidad del contacto de tierra de las bases de toma de corriente y de
   las prolongaciones y mangueras, que es donde más se pierde.

En un circuito ya en tensión, el medidor de bucle da una comprobación indirecta: un bucle fase-
protección anormalmente alto o abierto indica conductor de protección defectuoso (oficio).

Los valores máximos admisibles de continuidad no los fija el REBT; dependen de la sección y de la
longitud y, en último término, de que se cumplan las condiciones de corte del epígrafe 6.2.

## 5. Resistencia de tierra

### 5.1 El valor exigible

El REBT no fija un valor único de resistencia de tierra. Fija la tensión de contacto que no debe
superarse (ITC-BT-18, apartado 9):

> «**El electrodo se dimensionará de forma que su resistencia de tierra, en cualquier circunstancia
> previsible, no sea superior al valor especificado para ella, en cada caso.**
> **Este valor de resistencia de tierra será tal que cualquier masa no pueda dar lugar a tensiones de
> contacto superiores a:**
> **– 24 V en local o emplazamiento conductor**
> **– 50 V en los demás casos.**
> **Si las condiciones de la instalación son tales que pueden dar lugar a tensiones de contacto
> superiores a los valores señalados anteriormente, se asegurará la rápida eliminación de la falta
> mediante dispositivos de corte adecuados a la corriente de servicio.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 9.

En esquema TT, que es el de la red pública, el valor sale de la condición de la ITC-BT-24, 4.1.2:
**RA x Ia ≤ U**, donde **RA es la suma de las resistencias de la toma de tierra y de los conductores
de protección de masas**, Ia es, con diferencial, **la corriente diferencial-residual asignada**, y
**U es la tensión de contacto límite convencional (50, 24V u otras, según los casos)**. Despejando,
RA ≤ U / IΔn.

Ejemplo de aplicación (aritmética sobre la fórmula, no cifras de la norma):

| Diferencial de cabecera | RA máxima con U = 50 V | RA máxima con U = 24 V |
|---|---|---|
| 30 mA | 50 / 0,03 ≈ 1.667 Ω | 24 / 0,03 = 800 Ω |
| 300 mA | 50 / 0,3 ≈ 167 Ω | 24 / 0,3 = 80 Ω |
| 1 A | 50 / 1 = 50 Ω | 24 / 1 = 24 Ω |

La lectura es inmediata: el valor admisible depende del diferencial menos sensible que tiene que
proteger esas masas. Una tierra de 100 Ω es compatible con diferenciales de 30 y 300 mA en
condiciones normales, pero no con uno de 1 A como única protección. Y la ITC-BT-24 exige que **Todas
las masas de los equipos eléctricos protegidos por un mismo dispositivo de protección, deben ser
interconectadas y unidas por un conductor de protección a una misma toma de tierra.**

Que la cuenta dé 1.667 Ω no significa que una tierra de 1.000 Ω sea una buena tierra (oficio): la
resistencia sube con la sequía, con la corrosión y con los años, y el electrodo debe cumplir **en
cualquier circunstancia previsible**. Lo que se busca es un valor bajo con margen; la cifra concreta
que fije un proyecto o una empresa distribuidora para un edificio de la RTVA no consta en ningún
documento publicado.

### 5.2 Resistividad del terreno y estimación

**La resistencia de un electrodo depende de sus dimensiones, de su forma y de la resistividad del
terreno en el que se establece. Esta resistividad varía frecuentemente de un punto a otro del
terreno, y varía también con la profundidad.** (ITC-BT-18, 9).

La instrucción da tres tablas. La tabla 3, **a título de orientación**, valores de resistividad por
terreno; algunos que se preguntan:

| Naturaleza del terreno | Resistividad (Ω·m), tabla 3 |
|---|---|
| Terrenos pantanosos | **de algunas unidades a 30** |
| Humus | **10 a 150** |
| Arcilla plástica | **50** |
| Arena silícea | **200 a 3.000** |
| Suelo pedregoso desnudo | **1500 a 3.000** |
| Calizas compactas | **1.000 a 5.000** |
| Granitos y gres procedente de alteración | **1.500 a 10.000** |

(En el BOE, la fila «Suelo pedregoso cubierto de césped» dice «300 a 5.00», errata evidente; la guía
del INSST, que reproduce la tabla, da «300 a 500».)

La tabla 4, valores medios **Con objeto de obtener una primera aproximación**:

| Naturaleza del terreno | Valor medio (Ω·m), tabla 4 |
|---|---|
| **Terrenos cultivables y fértiles, terraplenes compactos y húmedos** | **50** |
| **Terraplenes cultivables poco fértiles y otros terraplenes** | **500** |
| **Suelos pedregosos desnudos, arenas secas permeables** | **3.000** |

Y la tabla 5, las fórmulas de estimación:

| Electrodo | Resistencia de tierra (Ω) |
|---|---|
| Placa enterrada | **R = 0,8 ρ/P** |
| Pica vertical | **R = ρ/L** |
| Conductor enterrado horizontalmente | **R = 2 ρ/L** |

con **ρ, resistividad del terreno (Ohm.m)**, **P, perímetro de la placa (m)** y **L, longitud de la
pica o del conductor (m)**.

Ejemplos de aplicación:

- Pica de 2 m en terreno de 50 Ω·m: R = 50 / 2 = 25 Ω.
- Pica de 2 m en terreno de 500 Ω·m: R = 500 / 2 = 250 Ω. Con un diferencial de 300 mA y U = 50 V
  (máximo ≈ 167 Ω) no cumple; habría que añadir picas, alargarlas o mejorar el terreno.
- Anillo de cimentación de 100 m de conductor en terreno de 500 Ω·m: R = 2 × 500 / 100 = 10 Ω.
- Placa de 0,5 × 1 m (perímetro 3 m) en 50 Ω·m: R = 0,8 × 50 / 3 ≈ 13,3 Ω.

La propia instrucción avisa de que estos cálculos **no dan más que un valor muy aproximado** y de que
la relación funciona también al revés: medida la resistencia de un electrodo, las fórmulas permiten
**estimar el valor medio local de la resistividad del terreno**, útil para trabajos posteriores en
condiciones análogas.

Dos lecturas de oficio que salen de las fórmulas: la resistencia baja en proporción a la longitud
enterrada, por eso el anillo perimetral del edificio (epígrafe 1.6) suele dar valores bajos; y varias
picas en paralelo bajan la resistencia, pero sólo si están suficientemente separadas entre sí para
que sus zonas de influencia no se solapen (la distancia concreta no la da el REBT).

### 5.3 Tomas de tierra independientes y tierra del centro de transformación

Independencia (ITC-BT-18, apartado 10):

> «**Se considerará independiente una toma de tierra respecto a otra, cuando una de las tomas de
> tierra, no alcance, respecto a un punto de potencial cero, una tensión superior a 50 V cuando por la
> otra circula la máxima corriente de defecto a tierra prevista.**»

Separación respecto a la tierra de un CT (apartado 11). Las masas de la instalación de
utilización y sus conductores de protección **no están unidas a la toma de tierra de las masas de un
centro de transformación, para evitar que durante la evacuación de un defecto a tierra en el centro
de transformación, las masas de la instalación de utilización puedan quedar sometidas a tensiones de
contacto peligrosas.** Si no se hace el control del apartado 10, las tomas se consideran
independientes cuando se cumplen todas estas condiciones:

- a) **No exista canalización metálica conductora (cubierta metálica de cable no aislada
  especialmente, canalización de agua, gas, etc.) que una la zona de tierras del centro de
  transformación con la zona en donde se encuentran los aparatos de utilización.**
- b) **La distancia entre las tomas de tierra del centro de transformación y las tomas de tierra u
  otros elementos conductores enterrados en los locales de utilización es al menos igual a 15 metros
  para terrenos cuya resistividad no sea elevada (<100 ohmios.m).** En terreno muy mal conductor, la
  distancia se calcula con una fórmula que el BOE consolidado no reproduce en texto (va en imagen) y
  que el tema no da.
- c) El CT está en recinto aislado o, si es contiguo o interior, **sus elementos metálicos no están
  unidos eléctricamente a los elementos metálicos constructivos de los locales de utilización.**

Sólo se pueden unir ambas tierras si la resistencia de la tierra única es tan baja que, con la máxima
corriente de defecto del lado de alta tensión, la tensión de defecto **(Vd = Id * Rt)** quede por
debajo de la tensión de contacto máxima.

Salvedad: el apartado 11 remite para esa tensión al **punto 1.1 de la MIE-RAT 13 del Reglamento sobre
Condiciones Técnicas y Garantía de Seguridad en Centrales Eléctricas, Subestaciones y Centros de
Transformación**, que es el reglamento de 1982, derogado por el Real Decreto 337/2014 (disposición
derogatoria única). El texto de la ITC-BT-18 no se ha actualizado y se cita tal cual; lo vigente para
la alta tensión es el Real Decreto 337/2014 y sus ITC-RAT, que no son de este tema.

### 5.4 Revisión de las tomas de tierra

> «**Por la importancia que ofrece, desde el punto de vista de la seguridad cualquier instalación de
> toma de tierra, deberá ser obligatoriamente comprobada por el Director de la Obra o Empresa
> instaladora en el momento de dar de alta la instalación para su puesta en marcha o en
> funcionamiento.**
> **Personal técnicamente competente efectuará la comprobación de la instalación de puesta a tierra,
> al menos anualmente, en la época en la que el terreno esté mas seco. Para ello, se medirá la
> resistencia de tierra, y se repararán con carácter urgente los defectos que se encuentren.**
> **En los lugares en que el terreno no sea favorable a la buena conservación de los electrodos,
> éstos y los conductores de enlace entre ellos hasta el punto de puesta a tierra, se pondrán al
> descubierto para su examen, al menos una vez cada cinco años.**»
>
> — Real Decreto 842/2002, ITC-BT-18, apartado 12.

Tres plazos y tres sujetos, que hay que saber separar:

| Cuándo | Quién | Qué |
|---|---|---|
| Al dar de alta la instalación | **el Director de la Obra o Empresa instaladora** | Comprobación obligatoria |
| **al menos anualmente, en la época en la que el terreno esté mas seco** | **Personal técnicamente competente** | Medida de la resistencia y reparación urgente de defectos |
| **al menos una vez cada cinco años**, si el terreno no favorece la conservación | (el mismo apartado no lo precisa) | Poner al descubierto electrodos y conductores de enlace |

(«mas» sin tilde, así en el BOE.)

Además, si la instalación es de las que llevan inspección por organismo de control (ITC-BT-05, 4.1:
entre ellas, **Locales de pública concurrencia**), la inspección periódica cada 5 años revisa
también la tierra, y unos **Valores elevados de resistencia de tierra en relación con las medidas de
seguridad adoptadas** son defecto grave (epígrafe 4.1). Las inspecciones y su régimen son del tema 2.

En un plan de mantenimiento (tema 13) la revisión de tierras entra como gama anual programada al
final del verano, con registro de valores para comparar con los años anteriores (oficio).

## 6. Protección de personas

### 6.1 Contactos directos e indirectos

La ITC-BT-24 **describe las medidas destinadas a asegurar la protección de las personas y animales
domésticos contra los choques eléctricos**. Distingue dos peligros, definidos en la ITC-BT-01:

| | Contacto directo | Contacto indirecto |
|---|---|---|
| Definición (ITC-BT-01) | **Contacto de personas o animales con partes activas de los materiales y equipos.** | **Contacto de personas o animales domésticos con partes que se han puesto bajo tensión como resultado de un fallo de aislamiento.** |
| Qué falla (oficio) | La instalación como barrera | El aislamiento de un equipo |
| Medidas (ITC-BT-24, 3 y 4) | Aislamiento de las partes activas, barreras o envolventes, obstáculos, alejamiento y, como complemento, diferencial de 30 mA como máximo | Corte automático de la alimentación, clase II, locales no conductores, conexiones equipotenciales locales no conectadas a tierra, separación eléctrica |

La puesta a tierra es la base de la protección contra contactos indirectos por corte automático: sin
tierra no circula corriente de defecto y la protección no actúa.

La medida que protege de los dos a la vez es la MBTS (ITC-BT-24, 2): **La protección contra los
choques eléctricos para contactos directos e indirectos a la vez se realiza mediante la utilización
de muy baja tensión de seguridad MBTS**. Si la tensión no puede ser peligrosa, no importa qué se
toque (oficio).

Contra contactos directos, las cifras que se preguntan (ITC-BT-24, 3.2): partes activas **en el
interior de las envolventes o detrás de barreras que posean, como mínimo, el grado de protección IP
XXB**; superficies superiores horizontales fácilmente accesibles, **como mínimo al grado de protección
IP4X o IP XXD**; y apertura sólo con llave o herramienta, tras quitar la tensión o con una segunda
barrera. El diferencial de 30 mA como máximo **se reconoce como medida de protección complementaria
en caso de fallo de otra medida de protección contra los contactos directos o en caso de imprudencia
de los usuarios**, pero **no constituye por sí mismo una medida de protección completa** (ITC-BT-24,
3.5). Estas medidas y el diferencial como aparato son del tema 3.

### 6.2 Corte automático de la alimentación en cada esquema

El principio (ITC-BT-24, 4.1): **El corte automático de la alimentación después de la aparición de un
fallo está destinado a impedir que una tensión de contacto de valor suficiente, se mantenga durante
un tiempo tal que puede dar como resultado un riesgo.** Y **Debe existir una adecuada coordinación
entre el esquema de conexiones a tierra de la instalación utilizado de entre los descritos en la
ITC-BT-08 y las características de los dispositivos de protección.**

> «**La tensión límite convencional es igual a 50 V, valor eficaz en corriente alterna, en
> condiciones normales. En ciertas condiciones pueden especificarse valores menos elevados, como por
> ejemplo, 24 V para las instalaciones de alumbrado público contempladas en la ITC-BT-09, apartado
> 10.**»
>
> — Real Decreto 842/2002, ITC-BT-24, apartado 4.1.

**Esquema TN** (4.1.1). Condición **Zs x Ia ≤ U0**, con **Zs es la impedancia del bucle de defecto,
incluyendo la de la fuente, la del conductor activo hasta el punto de defecto y la del conductor de
protección, desde el punto de defecto hasta la fuente** y U0 la tensión fase-tierra. Tiempos máximos
(tabla 1):

| U0 (V) | Tiempo de interrupción (s) |
|---|---|
| **230** | **0,4** |
| **400** | **0,2** |
| **> 400** | **0,1** |

Admite **Dispositivos de protección de máxima corriente, tales como fusibles, interruptores
automáticos** y diferenciales, con dos límites:

> «**Cuando el conductor neutro y el conductor de protección sean comunes (esquemas TN-C), no podrá
> utilizarse dispositivos de protección de corriente diferencial-residual.
> Cuando se utilice un dispositivo de protección de corriente diferencial-residual en esquemas
> TN-C-S, no debe utilizarse un conductor CPN aguas abajo. La conexión del conductor de protección al
> conductor CPN debe efectuarse aguas arriba del dispositivo de protección de corriente
> diferencial-residual.**»
>
> — Real Decreto 842/2002, ITC-BT-24, apartado 4.1.1.

La razón (oficio): en TN-C la corriente de defecto vuelve por el mismo conductor que atraviesa el
diferencial, la suma sigue siendo cero y el diferencial no la ve. Y una recomendación del mismo
apartado que es de tierra: **se recomienda conectar el conductor de protección a tierra en el punto
de entrada de cada edificio o establecimiento.**

Ejemplo. Circuito TN a 230 V con Zs = 0,5 Ω: corriente de defecto franco del orden de 230 / 0,5 =
460 A; el automático tiene que disparar con esa corriente en 0,4 s como máximo, lo que se comprueba
en su curva. Si la línea es larga y Zs sube, se pone diferencial o se reduce la impedancia del bucle.

**Esquema TT** (4.1.2). Condición **RA x Ia ≤ U** (epígrafe 5.1). Con dispositivos de sobreintensidad,
Ia es la corriente que asegura el disparo **en 5 s como máximo** si son de tiempo inverso, o la de
funcionamiento instantáneo. Para selectividad, diferenciales temporizados **(por ejemplo del tipo
«S»)** en serie con los generales, **con un tiempo de funcionamiento como máximo igual a 1 s**. Y
**El punto neutro de cada generador o transformador, o si no existe, un conductor de fase de cada
generador o transformador, debe ponerse a tierra.** Esa frase alcanza al grupo electrógeno que
alimenta la instalación (tema 7): su neutro también se pone a tierra.

**Esquema IT** (4.1.3). **Ningún conductor activo debe conectarse directamente a tierra en la
instalación.** **Las masas deben conectarse a tierra, bien sea individualmente o por grupos.** En el
primer defecto **la corriente de fallo es de poca intensidad y no es imperativo el corte**, pero debe
cumplirse **RA x Id ≤ UL**, con **Id es la corriente de defecto en caso de un primer defecto franco de
baja impedancia entre un conductor de fase y una masa**. Si hay controlador permanente de primer
defecto, **debe activar una señal acústica o visual**. En el segundo defecto:

- masas a tierra por grupos o individualmente: **las condiciones de protección son las del esquema
  TT, salvo que el neutro no debe ponerse a tierra**;
- masas interconectadas por un conductor de protección: condiciones del TN, con **a) si el neutro no
  esta distribuido: 2 x Zs x Ia ≤ U** y **b) si el neutro esta distribuido: 2 x Zs’ x Ia ≤ U0**, y los
  tiempos de la tabla 2:

| Tensión nominal U0/U | Neutro no distribuido (s) | Neutro distribuido (s) |
|---|---|---|
| **230/400** | **0,4** | **0,8** |
| **400/690** | **0,2** | **0,4** |
| **580/1000** | **0,1** | **0,2** |

Lo que significa para el mantenimiento (oficio): en un IT, la alarma del primer defecto no es para
dejarla sonar; el tiempo entre el primer y el segundo defecto es el margen para encontrar y reparar
el primero sin cortar.

### 6.3 Las demás medidas contra contactos indirectos

La ITC-BT-24 enumera otras cuatro, cada una con su relación con la tierra:

| Medida (ITC-BT-24) | En qué consiste | Relación con la tierra |
|---|---|---|
| 4.2 Clase II o aislamiento equivalente | **equipos con un aislamiento doble o reforzado (clase II)** | No se ponen a tierra: la ITC-BT-01 dice que estas medidas **no suponen la utilización de puesta a tierra para la protección** |
| 4.3 Locales o emplazamientos no conductores | Masas alejadas o separadas para que nadie toque a la vez dos puntos a distinta tensión | **En estos locales (o emplazamientos), no debe estar previsto ningún conductor de protección.** Paredes y suelos de al menos **50 kΩ** (hasta 500 V) o **100 kΩ** (más de 500 V) |
| 4.4 Conexiones equipotenciales locales no conectadas a tierra | Unir todas las masas y elementos conductores simultáneamente accesibles | **La conexión equipotencial local así realizada no debe estar conectada a tierra, ni directamente ni a través de masas o de elementos conductores.** |
| 4.5 Separación eléctrica | Alimentar desde **un transformador de aislamiento** o fuente equivalente | Si alimenta **un solo aparato, las masas del circuito no deben ser conectadas a un conductor de protección**; si alimenta varios, se unen entre sí con equipotenciales **aislados, no conectados a tierra** |

Las tres últimas son excepciones a la idea general de «poner todo a tierra», y por eso se preguntan:
en ellas, poner a tierra lo que no debe estarlo anula la medida (oficio).

### 6.4 Tensión de contacto, tensión de defecto y tensión de paso

Las definiciones de la ITC-BT-01:

- **Tensión de contacto**: **Tensión que aparece entre partes accesibles simultáneamente, al ocurrir
  un fallo de aislamiento.**
- **Tensión de defecto**: **Tensión que aparece a causa de un defecto de aislamiento, entre dos
  masas, entre una masa y un elemento conductor, o entre una masa y una toma de tierra de referencia,
  es decir, un punto en el que el potencial no se modifica al quedar la masa en tensión.**
- **Tensión de puesta a tierra (tensión a tierra)**: **Tensión entre una instalación de puesta a
  tierra y un punto a potencial cero, cuando pasa por dicha instalación una corriente de defecto.**
- **Choque eléctrico**: **Efecto fisiopatológico resultante del paso de corriente eléctrica a través
  del cuerpo humano o de un animal.**

La tensión de paso no la define el REBT de baja tensión. La guía técnica del INSST la transcribe de
la ITC-RAT 01 del Real Decreto 337/2014: **“Es la parte de la tensión a tierra que aparece en caso de
un defecto a tierra entre dos puntos del terreno separados un metro”**, y añade que **Esta diferencia
de potencial será tanto mayor cuanto más cerca se encuentre del electrodo**. Es la que afecta a quien
camina junto a un electrodo durante un defecto, y por eso la misma guía concluye que **Las citadas
tensiones de paso y de contacto serán tanto menores cuanto menor sea el valor de la resistencia de
tierra**. Sus valores admisibles son de alta tensión y no de este tema.

La relación entre todas (oficio): con un defecto, la corriente que va a tierra por la resistencia RA
eleva la masa a una tensión de defecto RA × Id respecto a la tierra lejana; la persona que toca la
masa con los pies en el suelo cercano queda sometida a una parte de esa tensión (la tensión de
contacto). Bajar RA y equipotencializar reducen esa tensión; el corte automático limita cuánto dura.

## 7. Compatibilidad con equipos sensibles

### 7.1 Lo que dice el REBT

En una casa de radio y televisión, la tierra tiene dos clientes: la seguridad de las personas y el
funcionamiento de los equipos de audio, vídeo y datos. El REBT trata el segundo en muy pocas líneas,
y todas ponen la seguridad por delante:

1. La tierra funcional existe y es legítima: **Las puestas a tierra por razones funcionales deben ser
   realizadas de forma que aseguren el funcionamiento correcto del equipo y permitan un
   funcionamiento correcto y fiable de la instalación.** (ITC-BT-18, 5).
2. Si coinciden, manda la protección: **Cuando la puesta a tierra sea necesaria a la vez por razones
   de protección y funcionales, prevalecerán las prescripciones de las medidas de protección.**
   (ITC-BT-18, 6).
3. La tierra funcional llega al mismo borne principal: entre los conductores que se unen a él están
   **Los conductores de puesta a tierra funcional, si son necesarios.** (ITC-BT-18, 3.3).
4. Neutro y protección, una vez separados, no se vuelven a unir (ITC-BT-18, 7; epígrafe 1.5). Un
   neutro unido a tierra aguas abajo convierte el conductor de protección en camino de retorno y
   lleva corriente de red por las masas y las mallas de los cables de todos los equipos: es una fuente
   clásica de zumbido, además de un incumplimiento (oficio).
5. Al medir el aislamiento de circuitos con electrónica, fases y neutro se unen entre sí (ITC-BT-19,
   2.9; epígrafe 3.4), para no someter a los equipos a la tensión de ensayo entre sus polos.
6. No se usa un conductor de protección común para instalaciones de tensiones distintas, y si se
   aplican sistemas de protección distintos en instalaciones próximas, **se empleará para cada uno de
   los sistemas un conductor de protección distinto** (ITC-BT-19, 2.3).

Lo que el REBT no dice: no regula «tierras limpias», tierras de señal separadas ni tierras
independientes para electrónica. Ninguna norma leída para este tema lo hace, y la consecuencia
práctica es tajante: cualquier tierra «técnica» o «de equipos» de una sala tiene que estar unida a
la instalación de puesta a tierra de protección, y una toma de tierra separada para los equipos que
no cumpla la independencia del apartado 10, o que deje masas sin protección, no es admisible.

La protección de los equipos sensibles frente a sobretensiones (categorías de la ITC-BT-23 y
descargadores conectados a tierra) es del tema 3; la compatibilidad electromagnética y la tierra
del rack, del tema 8.

### 7.2 El bucle de tierra y el zumbido

La regla de diagnóstico: la frecuencia del ruido dice de dónde viene. Un zumbido de 50 Hz, que es la
frecuencia de la red, no viene de la señal, sino de la alimentación o de la tierra (oficio):

| Frecuencia del zumbido | De dónde viene |
|---|---|
| 50 Hz | De la red: filtrado de la fuente de alimentación del equipo, o un bucle de masa que capta el campo de red |
| 100 Hz | Del rizado de un rectificador de doble onda: también la fuente |

Y el matiz que separa las dos causas de zumbido de red: si el zumbido cambia al tocar o mover los
cables de señal, es un bucle de masa; si no cambia, es la fuente.

Qué es un bucle de tierra (oficio): dos equipos unidos por un cable de señal apantallado y conectados
a tierra por dos caminos distintos (tomas de cuadros distintos, o una toma con mal contacto de
protección) cierran una espira entre la malla del cable y los conductores de protección. Cualquier
diferencia de potencial entre los dos puntos de tierra, o el campo magnético de los cables de energía
que atraviesa esa espira, hace circular corriente de 50 Hz por la malla, y esa corriente se suma a la
señal: zumbido en el audio, barras que se desplazan en el vídeo analógico.

Por qué es asunto del electricista: las diferencias de potencial entre tierras las producen la
instalación eléctrica y sus defectos (conductores de protección largos y cargados con corrientes de
fuga, neutro unido a tierra aguas abajo, una conexión de protección floja), y se corrigen en ella.

### 7.3 Reglas de oficio en una sala técnica

Ninguna de estas reglas es del REBT; son práctica de oficio compatible con él:

1. Una sola referencia de tierra por área técnica: los equipos unidos por señal, alimentados desde
   el mismo cuadro, con sus conductores de protección llevados en estrella a la barra de tierra de ese
   cuadro, y ésta al borne principal por un único camino.
2. Equipotencializar el área: racks, bandejas, falso suelo y estructuras metálicas de la sala unidos a
   la barra de tierra con conductores de equipotencialidad (ITC-BT-18, 8), para que todo lo que se
   puede tocar o conectar esté al mismo potencial.
3. Separar desde el cuadro los circuitos de equipos sensibles de los de fuerza, iluminación y
   climatización. Para lo más sensible, un transformador de aislamiento propio, cuyo secundario se
   conecta a tierra conforme al esquema que se adopte (en TN o TT, neutro del secundario a tierra; o un
   IT con sus condiciones del epígrafe 6.2).
4. Repartir las cargas con fuente conmutada entre varios circuitos: sus filtros derivan corriente al
   conductor de protección aun sin defecto, y la suma puede hacer disparar el diferencial o elevar el
   potencial del conductor de protección (medida con pinza de fugas; tema 8).

Ante un zumbido que aparece al conectar un equipo nuevo (oficio): se comprueba que el equipo está en
un circuito del mismo cuadro que los equipos con los que se une por señal; se mide la tensión entre
el conductor de protección de su toma y el de los demás; se comprueba la continuidad de su
conductor de protección (epígrafe 4.2); y se busca un neutro unido a tierra aguas abajo.

Lo que nunca se hace: cortar el conductor de protección de un equipo o usar un adaptador que anule
el contacto de tierra para «quitar el zumbido». Deja la masa sin protección contra contactos
indirectos, incumple la ITC-BT-18, 6 (prevalece la protección) y, en una inspección, es **Falta de
continuidad de los conductores de protección** (ITC-BT-05, 6.2). La separación de la señal
(aisladores galvánicos, entradas balanceadas) es del técnico de sonido o de vídeo, no de la
instalación eléctrica.

## Normativa que el tema invoca

- Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para
  baja tensión. De las instrucciones: ITC-BT-01 (terminología: tierra, toma de tierra, masa, elemento
  conductor, borne principal, resistencia de puesta a tierra y global, tierra lejana, conexión y
  conductor equipotencial, contacto directo e indirecto, tensión de contacto, de defecto y de puesta a
  tierra, choque eléctrico, material de clase II); ITC-BT-03, apéndice I, 2.1.2 (equipos mínimos de
  la empresa instaladora); ITC-BT-05, apartados 2.1, 3, 4.1, 4.2 y 6.2 (verificaciones, inspecciones y
  defectos graves); ITC-BT-08, apartados 1 y 2 (esquemas de distribución); ITC-BT-18 entera
  (instalaciones de puesta a tierra); ITC-BT-19, apartados 2.2.4, 2.3 y 2.9 (identificación,
  conductores de protección, aislamiento); ITC-BT-24, apartados 1 a 4 (contactos directos e
  indirectos); ITC-BT-26, apartados 1 y 3 (toma de tierra del edificio); ITC-BT-27, apartado 2.2
  (equipotencialidad suplementaria en baños); ITC-BT-28, apartado 2.1 (servicios de seguridad,
  esquema IT); ITC-BT-38 (transformador de aislamiento en quirófanos, sólo nombrado).
- Real Decreto 337/2014 (reglamento de alta tensión), sólo para decir que deroga el reglamento al que
  remite la ITC-BT-18, apartado 11, y como fuente de la definición de tensión de paso que transcribe la
  guía del INSST.
- Normas UNE que esas instrucciones nombran y este tema no ha leído: UNE 20.460-5-54 (conductores de
  protección), UNE 20.460-4-41 (protección contra choques eléctricos), UNE 20.460-6-61 (verificación),
  UNE 20.572-1 (efectos de la corriente), UNE 21.022 (conductores de cobre de electrodos) y
  UNE 20.324 (grados IP).

## Lo que este tema no da, y dónde está

- Un valor máximo de resistencia de tierra fijo: el REBT no lo da para la instalación interior; sale
  de la condición RA × Ia ≤ U (epígrafe 5.1). Los 5 y 2 Ω de la ITC-BT-08, 2, son de la red de
  distribución en esquema TN.
- La fórmula de distancia entre la tierra de un CT y la de la instalación en terreno muy mal conductor
  (ITC-BT-18, 11 b): en el BOE consolidado va en imagen y no se ha podido leer.
- El método normalizado de medida de tierras (distancias entre picas, criterio de la zona de
  potencial nulo en cifras): es de la norma de método o del fabricante del telurómetro; el tema da el
  método de oficio sin cifras.
- Valores máximos de resistencia de continuidad del conductor de protección: no los fija el REBT.
- Tierras «limpias», tierras de señal y sistemas de puesta a tierra para electrónica: ninguna norma
  leída los regula; lo que se dice es oficio. La serie UNE-EN 50600 (centros de datos) y la
  compatibilidad electromagnética: tema 8.
- Los valores admisibles de tensión de contacto y de paso en alta tensión: Real Decreto 337/2014 y sus
  ITC-RAT, fuera de este temario.
- El diferencial y los demás aparatos como dispositivos, la selectividad y los descargadores: tema 3.
  Secciones de conductores activos: tema 4. Verificaciones, inspecciones y su régimen: tema 2. Grupos
  electrógenos y SAI: tema 7. Instrumentos de medida y su manejo, y la medida de aislamiento entera:
  tema 14. Consignación y cinco reglas de oro: tema 15. Plan de mantenimiento: tema 13.
- El esquema de conexión a tierra, las tomas de tierra y sus valores medidos en los edificios, centros
  emisores y unidades móviles de la RTVA y de CSRTV: no constan en ningún documento publicado.
- Un proyecto de reforma del REBT anunciado para 2026 por colegios profesionales no consta publicado en
  el BOE a la fecha de redacción; no se estudia como vigente.

## Trazabilidad

| Fuente | Qué se ha tomado | Leída |
|---|---|---|
| Real Decreto 842/2002 (BOE-A-2002-18099), ITC-BT-01, redacción única (vigente desde el 18/09/2003) | Definiciones citadas en 1.1, 1.7, 6.1, 6.3 y 6.4 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-03, redacción vigente desde el 04/09/2025 (BOE-A-2025-17507) | Apéndice I, 2.1.2 (equipos) | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-05, redacción vigente desde el 30/06/2015 (BOE-A-2014-13681) | Apartados 2.1, 3, 4.1 b), 4.2 y 6.2 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-08, redacción única | Apartados 1, 1.1 a 1.4 y 2 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-18, redacción vigente desde el 23/05/2010 (BOE-A-2010-8190) | Apartados 1 a 12 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-19, ITC-BT-24, ITC-BT-26, ITC-BT-27, ITC-BT-28 e ITC-BT-38, redacción única | ITC-BT-19, 2.2.4, 2.3 y 2.9; ITC-BT-24, 1, 2, 3.2, 3.5, 4.1, 4.1.1 a 4.1.3 y 4.2 a 4.5; ITC-BT-26, 1, 3.1, 3.2 y 3.4; ITC-BT-27, 2.2; ITC-BT-28, 2.1; ITC-BT-38, 2.1.3 (sólo el término) | En el BOE consolidado, 05/10/2026 |
| INSST, *Guía técnica para la evaluación y prevención del riesgo eléctrico*, 4.ª ed., septiembre de 2020 | Definición de tensión de paso (transcrita por la guía de la ITC-RAT 01) y relación con la resistencia de tierra (págs. 37-38); fila del césped de su cuadro 5 | 05/10/2026 |

El BOE consolidado del REBT da como última actualización el 18/12/2025; ninguno de los preceptos
citados cambió entre el 24/09/2026 y la fecha de lectura.

Son física elemental u oficio, y así se declaran, sin atribuirlos a la norma: la razón de «sin
fusibles ni protección alguna»; la tabla de partes; la lectura de la tabla 1 para el cobre desnudo
enterrado; la idea de la equipotencialidad; la tabla resumen de los tres esquemas; la forma de
averiguar el esquema de una instalación; la tabla de equipos y estados de la instalación; el método
de las dos picas, la zona de potencial nulo y su comprobación, los avisos sobre separar el electrodo y
la humedad, el cierre del dispositivo tras medir y el registro; la pinza de tierra y sus límites; lo
que dan el medidor de bucle y el verificador de diferenciales; el procedimiento de comprobación de
continuidad; los ejemplos numéricos (aritmética sobre las fórmulas citadas); la lectura sobre picas en
paralelo y anillos; la relación entre tensión de defecto y de contacto; la tabla de frecuencias del
zumbido, el bucle de tierra, las reglas de sala técnica y la actuación ante un zumbido.
