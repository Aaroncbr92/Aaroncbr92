# Tema 17 del específico de Oficial Técnico Electricista · Planificación de intervenciones en instalaciones críticas: análisis de impacto, ventanas de mantenimiento, coordinación con producción, comunicación de incidencias, planes de contingencia y retorno al servicio

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Oficial Técnico Electricista · punto 17 |
| **Sirve para** | Puesto 2.27, Oficial Técnico Electricista (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Ninguna norma regula la planificación de una intervención de mantenimiento en radiotelevisión: el tema va en su mayor parte como oficio, y así se declara. Se apoya en: Ley 8/2011, de 28 de abril, por la que se establecen medidas para la protección de las infraestructuras críticas (artículo 2, sólo como vocabulario, y artículo 4); Real Decreto 1215/1997, de 18 de julio, sobre equipos de trabajo (artículo 4 y anexo II, apartado 1.14); Real Decreto 614/2001, de 8 de junio, sobre riesgo eléctrico (anexo II, A y A.2); Real Decreto 39/1997, de 17 de enero, Reglamento de los Servicios de Prevención (artículo 22 bis, apartados 1.a y 2); Ley 31/1995, de Prevención de Riesgos Laborales (artículo 29.2.4.º); Real Decreto 393/2007, de 23 de marzo, Norma Básica de Autoprotección (Norma, 3.3, 3.6 y 3.7; anexo II, capítulos 5, 6, 7 y 9); Real Decreto 1027/2007, Reglamento de instalaciones térmicas en los edificios (IT 2.3.4, apartado 4); X Convenio colectivo de la RTVA (artículo 50.11 y anexo III); fichas de catálogo de UNE-EN ISO 22301 y 22313 |
| **Redacción que se estudia** | La vigente el 24/09/2026. Ley 8/2011, artículos 2 y 4: redacción única (desde el 30/04/2011). Real Decreto 1215/1997: artículo 4 en redacción única (desde el 27/08/1997); anexo II en la del Real Decreto 2177/2004 (desde el 03/12/2004). Real Decreto 614/2001, anexo II: redacción única (desde el 21/08/2001). Real Decreto 39/1997, artículo 22 bis: redacción del Real Decreto 604/2006 (desde el 29/06/2006). Ley 31/1995, artículo 29: redacción única (desde el 10/02/1996). Real Decreto 393/2007: Norma derogada con efectos de 11/07/2023 por el Real Decreto 524/2023, que se sigue aplicando hasta que se apruebe el instrumento que la sustituya. RITE, IT 2: redacción única (desde el 29/02/2008) |
| **Extensión** | Unas 10.300 palabras |

<!-- /portada -->

Siglas que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); sistema de alimentación
ininterrumpida (**SAI**); conmutador estático de
transferencia (**STS**, *static transfer switch*); centro de proceso de datos (**CPD**); unidad de distribución de alimentación de un rack (**PDU**, *power distribution
unit*); conjunto redundante de discos independientes (**RAID**); sistema de
gestión técnica del edificio (**BMS**, *building management system*); orden de trabajo (**OT**);
Ley de Prevención de Riesgos Laborales (**LPRL**); Norma Básica de Autoprotección (**NBA**);
Reglamento de instalaciones térmicas en los
edificios (**RITE**) y sus instrucciones técnicas (**IT**); Reglamento electrotécnico para baja
tensión (**REBT**); Asociación Española de Normalización (**UNE**), norma europea (**EN**) y
Organización Internacional de Normalización (**ISO**). En las citas del X Convenio aparece
**SSFF**, sociedades filiales.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.27, punto 17):
>
> Planificación de intervenciones en instalaciones críticas: análisis de impacto, ventanas de
> mantenimiento, coordinación con producción, comunicación de incidencias, planes de contingencia
> y retorno al servicio.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué es una instalación crítica y qué significan en la Ley 8/2011
«infraestructura crítica», «criterios horizontales de criticidad» e «interdependencias»; qué se
analiza antes de intervenir (servicios afectados, duración, redundancia que queda, puntos únicos
de fallo); por qué una intervención en un sistema 2N deja la carga sin redundancia mientras dura;
qué orden de prioridades se sigue entre lo que está en antena y lo que no; qué es una ventana de
mantenimiento, cómo se elige y qué medidas no se pueden hacer en ella con la instalación parada
(termografía); por qué el ensayo de un grupo o de un SAI se hace con carga real en ventana
pactada; qué se pacta con producción y quién decide; cuándo hace falta recurso preventivo por
concurrencia de operaciones (Real Decreto 39/1997, artículo 22 bis.1.a); a quién se informa de
una situación de riesgo (LPRL, artículo 29.2.4.º); qué contiene el plan de actuación ante
emergencias de la NBA y su vigencia tras el Real Decreto 524/2023; qué es un plan de vuelta
atrás y un punto de no retorno; los niveles de redundancia y de repuesto; cómo se repone la
tensión (Real Decreto 614/2001, anexo II.A.2) y cuándo se considera en tensión la instalación;
qué comprobaciones exige el Real Decreto 1215/1997 después de un montaje o de una transformación;
quién actualiza el programa de un sistema de telegestión (RITE, IT 2.3.4); y cómo se cierra una
intervención. En la prueba práctica: planificar una intervención (por ejemplo, la sustitución de
las baterías del SAI de un control central) con su análisis de impacto, su ventana, su plan de
contingencia y su retorno al servicio, o decidir qué se hace cuando la intervención se tuerce.

<!-- indice -->

## Índice

- [1. Planificación de intervenciones en instalaciones críticas](#1-planificación-de-intervenciones-en-instalaciones-críticas)
  - [1.1 Qué es una instalación crítica](#11-qué-es-una-instalación-crítica)
  - [1.2 Lo que el puesto tiene encomendado](#12-lo-que-el-puesto-tiene-encomendado)
  - [1.3 El ciclo de una intervención planificada](#13-el-ciclo-de-una-intervención-planificada)
  - [1.4 Definir la intervención y lo que la norma exige antes de empezar](#14-definir-la-intervención-y-lo-que-la-norma-exige-antes-de-empezar)
- [2. Análisis de impacto](#2-análisis-de-impacto)
  - [2.1 Qué se analiza](#21-qué-se-analiza)
  - [2.2 El orden de prioridades](#22-el-orden-de-prioridades)
  - [2.3 La redundancia que queda durante la intervención](#23-la-redundancia-que-queda-durante-la-intervención)
  - [2.4 Las normas de continuidad de negocio](#24-las-normas-de-continuidad-de-negocio)
  - [2.5 Un análisis de impacto, paso a paso](#25-un-análisis-de-impacto-paso-a-paso)
- [3. Ventanas de mantenimiento](#3-ventanas-de-mantenimiento)
  - [3.1 Qué es una ventana](#31-qué-es-una-ventana)
  - [3.2 Cómo se elige](#32-cómo-se-elige)
  - [3.3 Qué va en ventana y qué no](#33-qué-va-en-ventana-y-qué-no)
  - [3.4 Los ensayos con carga real](#34-los-ensayos-con-carga-real)
  - [3.5 Duración, margen y punto de no retorno](#35-duración-margen-y-punto-de-no-retorno)
- [4. Coordinación con producción](#4-coordinación-con-producción)
  - [4.1 Quién decide](#41-quién-decide)
  - [4.2 Qué se pacta](#42-qué-se-pacta)
  - [4.3 Las empresas externas en la ventana](#43-las-empresas-externas-en-la-ventana)
  - [4.4 Los permisos de trabajo](#44-los-permisos-de-trabajo)
- [5. Comunicación de incidencias](#5-comunicación-de-incidencias)
  - [5.1 Dos clases de incidencia](#51-dos-clases-de-incidencia)
  - [5.2 La obligación de informar](#52-la-obligación-de-informar)
  - [5.3 Qué se comunica y cuándo](#53-qué-se-comunica-y-cuándo)
  - [5.4 La incidencia imprevista: guardias y orden de actuación](#54-la-incidencia-imprevista-guardias-y-orden-de-actuación)
  - [5.5 El registro de la incidencia](#55-el-registro-de-la-incidencia)
- [6. Planes de contingencia](#6-planes-de-contingencia)
  - [6.1 Qué es un plan de contingencia](#61-qué-es-un-plan-de-contingencia)
  - [6.2 El modelo normativo: la autoprotección](#62-el-modelo-normativo-la-autoprotección)
  - [6.3 El plan de vuelta atrás de una intervención](#63-el-plan-de-vuelta-atrás-de-una-intervención)
  - [6.4 Redundancia y repuesto: la contingencia que ya está montada](#64-redundancia-y-repuesto-la-contingencia-que-ya-está-montada)
  - [6.5 Probar la contingencia](#65-probar-la-contingencia)
- [7. Retorno al servicio](#7-retorno-al-servicio)
  - [7.1 Qué es devolver una instalación](#71-qué-es-devolver-una-instalación)
  - [7.2 La reposición de la tensión](#72-la-reposición-de-la-tensión)
  - [7.3 Las comprobaciones que exige la norma](#73-las-comprobaciones-que-exige-la-norma)
  - [7.4 La secuencia de retorno](#74-la-secuencia-de-retorno)
  - [7.5 El cierre y las lecciones](#75-el-cierre-y-las-lecciones)
  - [7.6 Un caso completo, de principio a fin](#76-un-caso-completo-de-principio-a-fin)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Planificación de intervenciones en instalaciones críticas

### 1.1 Qué es una instalación crítica

En el lenguaje del mantenimiento (oficio), una instalación es crítica cuando su fallo interrumpe
un servicio que no puede pararse o pone en peligro a las personas: en una casa de radio y
televisión, todo lo que está detrás de la emisión (alimentación de continuidad y controles
centrales, CPD, centros emisores, climatización de salas técnicas) y las instalaciones de
seguridad (alumbrado de emergencia, detección y extinción de incendios). Planificar una
intervención en ella es decidir de antemano qué se va a tocar, qué deja de funcionar mientras
tanto, cuándo, con quién, qué se hace si sale mal y cómo se devuelve.

El sentido legal de «infraestructura crítica» lo da la Ley 8/2011, por la que se establecen
medidas para la protección de las infraestructuras críticas, que define (artículo 2):

> **a) Servicio esencial: el servicio necesario para el mantenimiento de las funciones sociales
> básicas, la salud, la seguridad, el bienestar social y económico de los ciudadanos, o el eficaz
> funcionamiento de las Instituciones del Estado y las Administraciones Públicas.**
>
> **d) Infraestructuras estratégicas: las instalaciones, redes, sistemas y equipos físicos y de
> tecnología de la información sobre las que descansa el funcionamiento de los servicios
> esenciales.**
>
> **e) Infraestructuras críticas: las infraestructuras estratégicas cuyo funcionamiento es
> indispensable y no permite soluciones alternativas, por lo que su perturbación o destrucción
> tendría un grave impacto sobre los servicios esenciales.**
>
> — Ley 8/2011, artículo 2, letras a), d) y e).

Hay que leerla con una salvedad: que una instalación de la RTVA esté catalogada como
infraestructura crítica no consta en ningún documento publicado (la clasificación y el Catálogo
Nacional de Infraestructuras Estratégicas corresponden al Ministerio del Interior, artículo 4), y
este tema no lo afirma. La ley sirve aquí por su vocabulario, que es el del análisis de impacto
(2.1): la gravedad se mide con unos **criterios horizontales de criticidad** (letra h) y las
consecuencias en cadena se llaman **interdependencias** (letra j). Y su definición de
infraestructura crítica contiene la idea que gobierna todo el tema: lo crítico es lo que **no
permite soluciones alternativas**. Cuanta más redundancia tiene una instalación, menos crítica es
cada una de sus partes por separado, y más fácil es intervenir en ella.

### 1.2 Lo que el puesto tiene encomendado

El X Convenio colectivo de la RTVA, en su anexo III, define el puesto de Oficial Técnico
Electricista con estas tareas:

> **Efectuar revisiones y mantenimiento generales de instalaciones y equipos.
> Realizar reparaciones en instalaciones y equipos.
> Realizar el montaje e instalación de los nuevos sistemas y verificar su puesta en marcha.
> Mantener en condiciones optimas de funcionamiento las instalaciones.
> Mantener, operar, explotar e inspeccionar las instalaciones de RTVA y SSFF.**
>
> — X Convenio colectivo de la RTVA (BOJA núm. 240, de 10/12/2014), anexo III, puesto 9311100.

El mismo anexo encomienda al jefe del Departamento de Explotación y Mantenimiento **«Elaborar e
implantar el Plan de Mantenimiento.»**, **«Coordinar y supervisar el trabajo de los colaboradores
externos y contratas en las áreas de su competencia.»** y **«Controlar y asegurar la disponibilidad
de los servicios básicos (agua, electricidad, gas, telefonía).»** (puesto 9300000). Leídas juntas,
las dos fichas reparten el tema: la decisión de cuándo y cómo se para una instalación crítica, y
la coordinación con las contratas, corresponden a la jefatura; el oficial prepara, ejecuta,
verifica la puesta en marcha y devuelve la instalación. Es una lectura de oficio: cada ficha
advierte que **«La presente definición no constituye una lista cerrada de funciones»**. El procedimiento interno con que la RTVA
planifica sus intervenciones no consta publicado.

### 1.3 El ciclo de una intervención planificada

Una intervención en una instalación crítica sigue siempre el mismo ciclo, que ordena el resto del
tema (oficio; ninguna norma lo fija con estas fases):

| Fase | Qué se hace | Epígrafe |
|---|---|---|
| 1. Definir | Qué se va a hacer, sobre qué equipo, con qué OT y qué gama, quién lo hace | 1.4 |
| 2. Analizar el impacto | Qué deja de funcionar, cuánto tiempo, qué redundancia queda, qué puede salir mal | 2 |
| 3. Elegir la ventana | Cuándo hace menos daño, cuánto dura, con qué margen | 3 |
| 4. Coordinar | Con producción y emisión, con las contratas, con prevención | 4 |
| 5. Preparar la contingencia | Plan de vuelta atrás, repuestos, fuente alternativa, criterios para abortar | 6 |
| 6. Ejecutar | Consignación y trabajo seguro (tema 15), comunicando el avance | 5 |
| 7. Retornar al servicio | Reponer, comprobar, probar con carga, devolver a producción | 7 |
| 8. Cerrar | Registro, OT cerrada, lecciones, actualización de la documentación | 7.5 |

La regla que hay detrás: en una instalación crítica no se improvisa una parada. Las únicas
intervenciones que no se planifican son las de correctivo urgente, y aun ellas siguen las fases 2,
5, 6 y 7 en minutos en lugar de días (el caso, en 5.4).

### 1.4 Definir la intervención y lo que la norma exige antes de empezar

La definición es la OT con su gama (tema 13): qué equipo, qué operaciones, qué materiales y
repuestos, qué instrumentos, qué personal y cuánto tiempo. En una instalación crítica se añaden
tres cosas: el esquema actualizado de la parte afectada (sin él no hay análisis de impacto), el
procedimiento de maniobra paso a paso (en qué orden se abre y se cierra cada aparato) y la lista
de comprobaciones de retorno (7.4).

Dos normas fijan condiciones previas que la planificación tiene que prever. La de equipos de
trabajo:

> **14. Las operaciones de mantenimiento, ajuste, desbloqueo, revisión o reparación de los equipos
> de trabajo que puedan suponer un peligro para la seguridad de los trabajadores se realizarán tras
> haber parado o desconectado el equipo, haber comprobado la inexistencia de energías residuales
> peligrosas y haber tomado las medidas necesarias para evitar su puesta en marcha o conexión
> accidental mientras esté efectuándose la operación.**
>
> — Real Decreto 1215/1997, anexo II, apartado 1, punto 14.

Y la de riesgo eléctrico, que reserva las maniobras a personal autorizado:

> **Las operaciones y maniobras para dejar sin tensión una instalación, antes de iniciar el
> «trabajo sin tensión», y la reposición de la tensión, al finalizarlo, las realizarán trabajadores
> autorizados que, en el caso de instalaciones de alta tensión, deberán ser trabajadores
> cualificados.**
>
> — Real Decreto 614/2001, anexo II, A.

La consecuencia para la planificación: si el trabajo exige parar el equipo, la parada es la que
determina el impacto, y hay que planificarla; si el equipo no puede pararse, el Real Decreto
1215/1997 prevé que **«se adoptarán las medidas necesarias para que estas operaciones se realicen de forma
segura o fuera de las zonas peligrosas»** (segundo párrafo del punto 14); en una instalación
eléctrica eso es trabajar en tensión o en proximidad, con los requisitos del tema 15, o no hacerlo. Las cinco reglas de oro,
la consignación y los permisos de trabajo se estudian en el tema 15.

## 2. Análisis de impacto

### 2.1 Qué se analiza

Analizar el impacto es contestar, antes de tocar nada, a cinco preguntas (oficio; el método no
lo fija ninguna norma leída):

| Pregunta | Cómo se contesta |
|---|---|
| ¿Qué deja de funcionar? | Recorriendo el esquema desde el aparato que se va a abrir hacia las cargas: todo lo que cuelga de él |
| ¿Qué servicio cae con ello? | Pasando de los equipos a los servicios: emisión, producción, redacción, CPD, seguridad |
| ¿Durante cuánto tiempo? | La duración prevista del trabajo más la de la maniobra, la de la reposición y la del rearranque de los equipos |
| ¿Qué redundancia queda mientras tanto? | Si la carga sigue alimentada por otro camino, y si ese camino es ya el único (2.3) |
| ¿Qué puede salir mal, y qué pasaría? | El fallo de la vía que queda, una maniobra equivocada, un equipo que no rearranca, un trabajo que se alarga |

La segunda pregunta es la que suele faltar. El electricista piensa en circuitos y producción
piensa en servicios: un cuadro de distribución no le dice nada a un jefe de emisiones, el
«control central sin SAI durante dos horas», sí. El análisis de impacto es la traducción de un
esquema eléctrico a una lista de servicios afectados.

La Ley 8/2011 da el vocabulario de las dos dimensiones del impacto. La gravedad se mide con sus
**criterios horizontales de criticidad**, que la letra h) del artículo 2 define y enumera así:

> **h) Criterios horizontales de criticidad: los parámetros en función de los cuales se determina
> la criticidad, la gravedad y las consecuencias de la perturbación o destrucción de una
> infraestructura crítica se evaluarán en función de:**
>
> **1. El número de personas afectadas, valorado en función del número potencial de víctimas
> mortales o heridos con lesiones graves y las consecuencias para la salud pública.**
>
> **2. El impacto económico en función de la magnitud de las pérdidas económicas y el deterioro de
> productos y servicios.**
>
> **3. El impacto medioambiental, degradación en el lugar y sus alrededores.**
>
> **4. El impacto público y social, por la incidencia en la confianza de la población en la
> capacidad de las Administraciones Públicas, el sufrimiento físico y la alteración de la vida
> cotidiana, incluida la pérdida y el grave deterioro de servicios esenciales.**

Son cuatro: personas, economía, medio ambiente e impacto público y social. El cuarto es el que más
se acerca a una casa que emite, porque menciona expresamente **«la pérdida y el grave deterioro de
servicios esenciales»**. Las consecuencias en cadena se nombran con las
**«Interdependencias: los efectos que una perturbación en el funcionamiento de la instalación o
servicio produciría en otras instalaciones o servicios, distinguiéndose las repercusiones en el
propio sector y en otros sectores, y las repercusiones de ámbito local, autonómico, nacional o
internacional.»** (artículo 2.j). En una sala técnica, las interdependencias son lo que no se ve
en el esquema eléctrico: parar el cuadro de la climatización no apaga ningún equipo de emisión,
pero los apaga al cabo de un tiempo por temperatura; parar la red de datos no quita tensión a nadie,
pero deja sin servicio al BMS que vigila el resto (tema 12).

### 2.2 El orden de prioridades

Para graduar el impacto sirve el orden de prioridades de una casa que emite, que es criterio de
oficio y no norma.

Y la jerarquía que ordena las prioridades cuando fallan dos cosas a la vez: primero lo que está
en antena, después lo que va a estar en antena en las próximas horas, y al final lo que se puede
recuperar más tarde. Una sala de edición parada es un problema; una continuidad parada es un
incidente de emisión.

Aplicada a la planificación, la misma jerarquía dice qué se puede parar y cuándo. Las áreas de una
televisión, por lo que su parada significa:

| Área | Qué contiene | Qué la caracteriza |
|---|---|---|
| Continuidades | La cadena que llega a la antena: servidores de emisión, conmutación, retardo | No puede parar nunca: cada minuto es emisión |
| Controles técnicos y salas técnicas | Matrices, distribuidores, sincronismos, conversores, red | Es la columna vertebral: un fallo aquí afecta a todo lo demás |
| Estudios | Cámaras, iluminación, sonido de plató, comunicaciones | Muchos equipos móviles y mucho cableado que se manipula a diario |
| Postproducción de vídeo y audio | Salas de edición y de mezcla | Trabajo por proyectos, con dependencia fuerte de versiones y licencias |

De ahí la escala práctica (oficio): una intervención que afecta a una sala de edición se pacta
con esa sala; una que afecta a un estudio, con la producción que lo tiene asignado; una que
afecta a la continuidad o a los controles centrales sólo se hace si la carga queda alimentada por
otro camino durante todo el trabajo, o en una ventana en la que la emisión se haya pasado a otra
cadena o a otro centro. Que la RTVA disponga de esa otra cadena o de ese otro centro no consta en
ningún documento publicado.

### 2.3 La redundancia que queda durante la intervención

La notación N, N+1 y 2N, los caminos, los STS y los puntos únicos de fallo están en el tema 8. Lo
que el análisis de impacto añade es que toda intervención consume redundancia:

| La instalación tiene | Mientras se interviene en un elemento | Qué significa |
|---|---|---|
| N | La carga cae | No hay intervención sin parada: necesita ventana con la carga fuera de servicio o una alimentación provisional |
| N+1 | Queda N | La carga sigue, pero sin reserva: un segundo fallo la tira |
| 2N | Queda N (un solo camino) | La carga sigue por el otro sistema, pero sin redundancia hasta que se devuelva el intervenido |

La consecuencia es la regla más importante del epígrafe: la ventana de mantenimiento de un
sistema redundante es un periodo de riesgo aumentado, aunque nada se haya apagado. La carga
funciona; lo que ha desaparecido es el margen. Por eso esas intervenciones también se pactan y se
hacen en ventana (3), y por eso la planificación incluye vigilar la vía que queda (alarmas del SAI
y del BMS, tema 12) y acortar todo lo posible el tiempo sin redundancia.

Y el criterio de fondo que el análisis tiene que comprobar:

La redundancia existe para que la avería no se note. Si se ha invertido en redundancia y, cuando
llega la avería, se para el servicio de todas formas, la inversión no ha servido para nada.

Aplicado a la planificación (oficio): si una intervención de mantenimiento en una instalación
redundante exige cortar la carga, algo está mal diseñado o mal planificado. El análisis de
impacto es el momento de descubrirlo: un bypass de mantenimiento cuya maniobra corta, una carga
de una sola entrada colgada de un sistema que se pretende 2N, una PDU que alimenta las dos fuentes
de un equipo (tema 8, 8.4).

### 2.4 Las normas de continuidad de negocio

La familia de normas que trata el análisis de impacto en una organización es la de continuidad
del negocio. Según su ficha de catálogo, la **UNE-EN ISO 22301:2020** es **«Seguridad y
resiliencia. Sistema de Gestión de la Continuidad del Negocio. Requisitos. (ISO 22301:2019).»**,
en vigor, con una modificación de 2024 (**«Modificación 1: Acciones relativas al cambio
climático.»**); y la **UNE-EN ISO 22313:2020**, **«Seguridad y resiliencia. Sistemas de gestión
de la continuidad del negocio. Directrices para la utilización de la norma ISO 22301.»** Su
contenido no se ha leído (son normas de pago), y este tema no les atribuye ningún método,
definición ni sigla. Que la RTVA tenga un sistema de gestión de la continuidad del negocio no
consta en ningún documento publicado.

### 2.5 Un análisis de impacto, paso a paso

Ejemplo de estudio (oficio; no describe una instalación de la RTVA). Hay que sustituir las
baterías de uno de los dos SAI que alimentan, en 2N, los racks del control central; los equipos
tienen doble fuente, una de cada SAI, salvo dos conversores de una sola entrada colgados de un STS.

| Pregunta | Respuesta |
|---|---|
| ¿Qué deja de funcionar? | El SAI A pasa a bypass de mantenimiento o se aísla: la rama A queda en red sin protección o sin tensión, según cómo esté construido el bypass |
| ¿Qué servicio cae? | Ninguno, si todos los equipos tienen doble fuente y la rama B puede con toda la carga (tema 8, 5.1); los dos conversores dependen del STS, que pasará a la rama B |
| ¿Durante cuánto tiempo? | El trabajo, más la maniobra de paso a bypass y la de vuelta, más la prueba de la batería nueva (7) |
| ¿Qué redundancia queda? | Ninguna: toda la carga del control central depende del SAI B y de su camino. Si el SAI B falla, cae el control central |
| ¿Qué puede salir mal? | Que el STS no transfiera; que la rama B esté sobrecargada y salte; que el SAI B tenga una alarma latente; que el SAI A no vuelva a inversor |

De ese análisis salen las decisiones de los epígrafes siguientes: comprobar antes la carga real de
la rama B y el estado del SAI B (alarmas, última prueba de descarga, tema 7); probar el STS o
aceptar que los dos conversores pueden sufrir un corte; hacer el trabajo en la ventana de menor
emisión; tener preparada la vuelta atrás (6.3); y no dar por terminada la intervención hasta que
el SAI A haya vuelto a inversor y la rama A alimente otra vez a los equipos (7.4).

## 3. Ventanas de mantenimiento

### 3.1 Qué es una ventana

Una ventana de mantenimiento es el intervalo, pactado de antemano con quien explota el servicio,
en el que se acepta que una instalación crítica quede parada, degradada o sin redundancia para
intervenir en ella. Ninguna norma regula la ventana de mantenimiento en radiotelevisión: es
costumbre de oficio, y así se presenta.

Una ventana tiene cinco datos, y los cinco se fijan antes (oficio):

| Dato | Qué es |
|---|---|
| Inicio | Hora en que se empieza a maniobrar, no en que se empieza a trabajar |
| Fin | Hora en que la instalación tiene que estar devuelta y comprobada |
| Alcance | Qué se para o se degrada, y qué no se toca |
| Punto de no retorno | Último momento en que todavía se puede deshacer lo hecho y devolver la instalación a tiempo (6.3) |
| Responsables | Quién ejecuta, quién autoriza en explotación, a quién se avisa si algo se tuerce |

### 3.2 Cómo se elige

La ventana se busca donde el análisis de impacto (2) da el daño menor (oficio):

- En la parrilla: las horas de menor audiencia y sin directos, que en una televisión suelen ser
  las de madrugada, o los huecos en los que la emisión es enlatada y puede sostenerse desde un
  sistema de reserva.
- En la producción: los días sin grabación en el estudio afectado, las semanas sin un programa
  especial, nunca en vísperas de un acontecimiento con cobertura en directo (elecciones,
  retransmisiones).
- En la meteorología y en la red: no se interviene en la alimentación de un centro emisor con
  aviso de tormentas, ni se deja un sistema sin redundancia cuando la red de la distribuidora está
  dando cortes.
- En las personas: con el personal que conoce la instalación presente o localizable, y con el
  servicio técnico del fabricante disponible si la intervención depende de él.

La ventana de madrugada tiene un coste propio que la planificación tiene que contar: se trabaja
con menos gente, más cansada y con el apoyo exterior más difícil de conseguir. Una ventana de
madrugada mal preparada es más peligrosa que una de día bien preparada.

### 3.3 Qué va en ventana y qué no

No todo el mantenimiento necesita ventana, y no todo lo que necesita ventana necesita la
instalación parada. La distinción la marca la medida (tema 14):

El punto caliente y el armónico sólo existen cuando circula corriente. Una termografía hecha con
la instalación parada no vale para nada, y es un error frecuente en un mantenimiento mal
planificado.

Así que la planificación separa tres clases de tarea (oficio):

| Clase | Ejemplos | Ventana |
|---|---|---|
| En carga, sin tocar | Termografía, análisis de red, lectura de alarmas e históricos | No necesita: se hace en servicio, y además sólo vale en servicio |
| Con la instalación parada | Medida de aislamiento, reapriete de conexiones, sustitución de aparamenta, limpieza interior de cuadros | Ventana con la parte afectada sin tensión o alimentada por otra vía |
| Ensayos de las fuentes de socorro | Arranque y transferencia del grupo, descarga del SAI, conmutación del STS | Ventana pactada: se acepta un riesgo controlado (3.4) |

Y un orden que se sigue dentro de la misma intervención: la termografía, antes de abrir; si se
abre primero, la conexión floja que se iba a buscar ya no está caliente.

### 3.4 Los ensayos con carga real

La tarea de mantenimiento que más necesita una ventana es la que prueba las fuentes de socorro:

Un grupo que arranca en vacío una vez al mes no demuestra nada; lo que hay que probar es la
transferencia, y eso exige aceptar un riesgo controlado en una ventana pactada. Una redundancia
que no se ha provocado nunca no se sabe si funciona.

La prueba con carga, el banco de cargas y la prueba de transferencia completa del grupo, y la
prueba de descarga del SAI, están en el tema 7 (7.1 y 7.2). Lo que este tema añade es cómo se
pacta (oficio): el ensayo de transferencia se planifica como una intervención más, con su análisis
de impacto (qué cae si el grupo no toma la carga o si el SAI no aguanta hasta que la tome), su
ventana, su plan de vuelta atrás (reponer la red de inmediato) y su retorno al servicio (que la
retransferencia a red se complete y el grupo quede en automático, no en manual).

### 3.5 Duración, margen y punto de no retorno

La duración de una ventana se calcula hacia atrás desde la hora en que la instalación tiene que
estar devuelta (oficio):

| Tramo | Qué se reserva |
|---|---|
| Comprobaciones previas | Estado de la vía que queda, alarmas, herramientas, repuestos (6.3) |
| Maniobra de salida | Pasar a bypass, transferir cargas, consignar |
| Trabajo | Lo que dice la gama, con margen |
| Reposición y pruebas | Reponer la tensión, rearrancar, probar con carga (7) |
| Vuelta atrás | El tiempo necesario para deshacer lo hecho si algo sale mal |

El último tramo es el que define el punto de no retorno: si el trabajo no está terminado cuando
sólo queda el tiempo de deshacerlo, se deshace. Seguir adelante con la esperanza de acabar a
tiempo es la forma más común de convertir una ventana de mantenimiento en una incidencia de
emisión.

## 4. Coordinación con producción

### 4.1 Quién decide

La intervención la propone mantenimiento, pero la ventana la acepta quien responde del servicio
que se va a parar o degradar (oficio): la emisión, la producción del estudio, la redacción, los
sistemas. Ningún electricista decide por su cuenta dejar sin redundancia una continuidad. En la
RTVA, el convenio sitúa la elaboración del plan de mantenimiento y la coordinación de contratas
en la jefatura del Departamento de Explotación y Mantenimiento (1.2); el procedimiento con que se
autorizan las ventanas y quién firma por parte de la emisión no constan publicados.

### 4.2 Qué se pacta

Lo que mantenimiento tiene que llevar a la coordinación, y lo que tiene que salir de ella por
escrito (oficio):

| Se pacta | Para qué |
|---|---|
| Fecha, hora de inicio, hora de fin y punto de no retorno | Que producción sepa cuándo puede contar con la instalación |
| Servicios afectados, en lenguaje de servicio | La traducción del análisis de impacto (2.1): no «el cuadro CS-2», sino «el estudio 3 sin climatización» |
| Riesgo residual | Qué podría caer si algo falla, aunque no esté previsto que caiga |
| Lo que producción tiene que hacer | Pasar la emisión a reserva, no programar grabaciones, guardar el trabajo de las salas, apagar equipos de forma ordenada |
| Plan de contingencia y criterio para abortar | Qué se hará si sale mal, y quién decide abortar (6) |
| Interlocutores | Un responsable de cada parte, localizable durante toda la ventana |
| Cómo se comunicará el avance y el final | Inicio, incidencias, fin y devolución (5 y 7) |

El aviso previo tiene que llegar a todos los que dependen de la instalación, no sólo a quien
autoriza: una sala de edición que no se ha enterado del corte pierde el trabajo que no había
guardado. Y el pacto se confirma justo antes de empezar: una ventana pactada hace una semana no
autoriza a cortar si hoy hay un directo que no estaba previsto.

### 4.3 Las empresas externas en la ventana

En las ventanas suelen concurrir el personal propio, el servicio técnico del fabricante del SAI o
del grupo, la empresa mantenedora de la climatización o de la protección contra incendios y, a
veces, una empresa instaladora. La coordinación de actividades empresariales (artículo 24 de la
LPRL y Real Decreto 171/2004: información, instrucciones, medios de coordinación, persona
coordinadora) está desarrollada en el tema 15, epígrafe 6. Lo que la planificación de una ventana
añade es que varias operaciones se hacen a la vez o seguidas en el mismo lugar, y ése es uno de
los supuestos en que la norma exige la presencia de recursos preventivos:

> **a) Cuando los riesgos puedan verse agravados o modificados, en el desarrollo del proceso o la
> actividad, por la concurrencia de operaciones diversas que se desarrollan sucesiva o
> simultáneamente y que hagan preciso el control de la correcta aplicación de los métodos de
> trabajo.**
>
> — Real Decreto 39/1997, artículo 22 bis.1.a).

El mismo artículo dispone que, en ese caso, **«la evaluación de riesgos laborales, ya sea la
inicial o las sucesivas, identificará aquellos riesgos que puedan verse agravados o modificados
por la concurrencia de operaciones sucesivas o simultáneas»** (22 bis.2). Para la planificación
(oficio): la lista de quién va a trabajar en la ventana, en qué y en qué orden, es un dato de
entrada de la coordinación preventiva, y se tiene que conocer antes, no descubrirse esa noche en
la sala.

### 4.4 Los permisos de trabajo

Una ventana en una instalación crítica se ejecuta con permiso de trabajo cuando hay riesgo
eléctrico o concurrencia; en baja tensión el permiso escrito es buena práctica, no obligación
expresa del Real Decreto 614/2001 (tema 15, epígrafe 5). Donde hay plan de autoprotección, la NBA dispone que
**«Los procedimientos preventivos y de control de riesgos que se establezcan, tendrán en cuenta, al
menos, los siguientes aspectos:»** (Norma, apartado 3.3.3), y es una lista de mínimos. Además de la a)
(precauciones y buenas prácticas para evitar accidentes), recoge los **«b) Permisos especiales de trabajo para la
realización de operaciones o tareas que generen riesgos.»**, la **«c) Comunicación de anomalías o
incidencias al titular de la actividad.»**, el **«d) Programa de las operaciones preventivas o de
mantenimiento de las instalaciones, equipos, sistemas y otros elementos de riesgo, definidos en el
capítulo 5 del anexo II, que garantice su control.»** y el **«e) Programa de mantenimiento de las
instalaciones, equipos, sistemas y elementos necesarios para la protección y seguridad, definidos
en el capítulo 5 del Anexo II, que garantice la operatividad de los mismos.»** Las letras d) y e) distinguen dos
programas: el de lo que genera el riesgo y el de lo que protege frente a él; los dos remiten al
capítulo 5 del anexo II (6.2). El permiso es, además, una herramienta de coordinación con producción: dice por escrito
qué parte de la instalación está fuera de servicio, quién la tiene y hasta cuándo.

## 5. Comunicación de incidencias

### 5.1 Dos clases de incidencia

En una instalación crítica hay que distinguir dos clases de incidencia, que a menudo llegan
juntas (oficio):

| Clase | Qué es | A quién se comunica |
|---|---|---|
| De servicio | Algo deja de funcionar o pierde su redundancia: un SAI en bypass, un grupo que no arranca, un cuadro que dispara | A quien explota el servicio afectado (emisión, producción) y a quien coordina el mantenimiento |
| De seguridad | Algo pone en riesgo a las personas: un borne accesible, un cable dañado, un conato de incendio, un accidente | Al superior directo y a la organización preventiva, con la obligación del artículo 29 de la LPRL (5.2) |

Una misma avería puede ser de las dos clases: un cuadro que se ha quemado deja sin servicio a un
estudio y deja partes en tensión al descubierto. Entonces se atienden las dos, y lo primero es
la seguridad de las personas: impedir el acceso a lo que ha quedado en tensión y señalizarlo
(los criterios de prioridad, en el tema 13, 5.1).

### 5.2 La obligación de informar

La comunicación de una situación de riesgo no es una cortesía. La LPRL la impone a cada
trabajador:

> **4.º Informar de inmediato a su superior jerárquico directo, y a los trabajadores designados
> para realizar actividades de protección y de prevención o, en su caso, al servicio de
> prevención, acerca de cualquier situación que, a su juicio, entrañe, por motivos razonables, un
> riesgo para la seguridad y la salud de los trabajadores.**
>
> — Ley 31/1995, artículo 29.2.4.º.

Y, donde hay plan de autoprotección, la NBA pide que sus procedimientos preventivos tengan en
cuenta la **«Comunicación de anomalías o incidencias al titular de la actividad.»** (Norma,
apartado 3.3.3.c). Los demás derechos y obligaciones preventivos, incluida la paralización ante
riesgo grave e inminente, se estudian en el tema 19, epígrafe 1.

Para la incidencia de servicio no hay norma que fije a quién ni cómo se avisa: lo fija el
procedimiento de cada casa, que en la RTVA no consta publicado.

### 5.3 Qué se comunica y cuándo

Una comunicación de incidencia útil contesta siempre a las mismas preguntas, y se hace en tres
momentos (oficio):

| Momento | Qué se dice |
|---|---|
| Aviso inicial, de inmediato | Qué ha pasado, dónde, desde cuándo; qué servicio está afectado o en riesgo; qué se está haciendo; cuándo se volverá a informar |
| Seguimiento | Qué se ha averiguado, qué se ha hecho, cuánto se calcula que falta; si cambia el riesgo, se dice en cuanto cambia |
| Cierre | Que el servicio está restablecido y comprobado, qué queda pendiente (por ejemplo, la redundancia todavía no repuesta) y qué se hará |

Tres reglas de oficio sobre la comunicación:

1. Se avisa antes de saber la causa. El aviso inicial no espera al diagnóstico: quien explota el
   servicio necesita saber cuanto antes que su servicio está en riesgo, para pasar a reserva o
   avisar a su vez.
2. Se dice lo que se sabe y lo que no. «La rama A está sin tensión, todavía no sé por qué, el
   control central sigue por la rama B» es una comunicación completa; «está todo bien» antes de
   haberlo comprobado, no.
3. Se escala si no hay respuesta o si el problema supera lo previsto. Si la reparación excede la
   capacidad o la autorización de quien está de guardia, o si la incidencia puede afectar a la
   emisión, se sube al responsable de mantenimiento sin esperar.

### 5.4 La incidencia imprevista: guardias y orden de actuación

No todas las incidencias llegan dentro de una ventana. El X Convenio prevé guardias para las
averías imprevistas: entre las tareas del Ayudante Técnico Electricista figura **«Realizar con el
oficial guardias para atender averías imprevistas.»** (anexo III, puesto 9311200), y el artículo
50.11 regula el plus por guardia localizable: **«El personal que voluntariamente acepte estar de
guardia durante el tiempo de descanso, o en días festivos, percibirá por este concepto la cantidad
que se establece para cada día de guardia, tanto si es llamado como si no y sin perjuicio de la
compensación como extraordinarias de las horas que realice el/la trabajador/a que sea
llamado/a.»**, con la precisión de que **«Si es llamado/a, la convocatoria mínima será de cuatro
horas. El/La trabajador/a dispondrá de localizador a distancia para ser avisado/a.»**

Ante una incidencia imprevista en una instalación crítica, el ciclo de 1.3 se recorre comprimido.
El orden de prioridades ante una incidencia de alimentación (mantener la carga, avisar,
diagnosticar y, al final, reparar en condiciones de seguridad) está en el tema 7, 8.1, y vale para
cualquier instalación crítica. Lo que la planificación previa aporta a esa noche es lo que ya
estaba preparado: el esquema actualizado, el procedimiento de maniobra escrito, los repuestos
críticos en el almacén (tema 13, 7) y la lista de a quién se llama.

### 5.5 El registro de la incidencia

Toda incidencia se cierra por escrito: qué pasó, cuándo, qué servicio se afectó y durante cuánto
tiempo, cuál fue la causa (no sólo el síntoma), qué se hizo y qué queda pendiente. Es la OT de
correctivo del tema 13 con un dato más: la afección al servicio. Ese registro es lo que permite,
después, ver qué instalación falla más, qué incidencias se repiten y qué redundancia hace falta
reforzar (7.5).

## 6. Planes de contingencia

### 6.1 Qué es un plan de contingencia

Un plan de contingencia dice, por adelantado, qué se hace si falla algo que no debería fallar.
En mantenimiento de instalaciones críticas hay dos, y conviene no confundirlos (oficio):

| Plan | Qué cubre | Cuándo se escribe |
|---|---|---|
| De la instalación | Qué se hace si falla la red, el grupo, un SAI, la climatización de una sala técnica: maniobras, a quién se avisa, qué se deslastra, qué se apaga de forma ordenada | Una vez, y se revisa cuando cambia la instalación |
| De la intervención | Qué se hace si la intervención sale mal: cómo se deshace, con qué, quién decide abortar | Para cada intervención, como parte de su planificación |

El primero es el que hace que una incidencia imprevista de madrugada se resuelva con un
procedimiento escrito y no con la memoria de quien está de guardia; las actuaciones ante las
incidencias del grupo y del SAI están en el tema 7, epígrafe 8. El segundo es el que permite
aceptar una ventana (3).

### 6.2 El modelo normativo: la autoprotección

La única norma leída que ordena un plan de respuesta a emergencias en un edificio es la de
autoprotección. Su vigencia tiene una particularidad que hay que conocer:

El Real Decreto 393/2007, de 23 de marzo, aprobó
la **Norma Básica de Autoprotección de los centros, establecimientos y dependencias dedicados a
actividades que puedan dar origen a situaciones de emergencia**. Hay que estudiarlo con un aviso: el
Real Decreto 524/2023, de 20 de junio, que aprueba la Norma Básica de Protección Civil, dispone en su
disposición derogatoria única, apartado 2: **«Igualmente, se derogan: […] d) La Norma Básica de
Autoprotección de los centros, establecimientos y dependencias dedicados a actividades que puedan dar
origen a situaciones de emergencia, aprobada por el Real Decreto 393/2007, de 23 de marzo.»** El texto
consolidado del BOE lo anota así: **«Norma derogada, con efectos de 11 de julio de 2023, por la
disposición derogatoria única.2.d) del Real Decreto 524/2023, de 20 de junio. […] No obstante, la
Norma Básica continuará aplicándose hasta tanto sea aprobado el nuevo instrumento de planificación que
la sustituya, según establece el apartado 3 de la citada disposición.»** El apartado 3 dice, de
**«Las Directrices Básicas de Planificación y los Planes Estatales de protección civil a las que se
refiere el apartado anterior»**, que **«continuarán aplicándose hasta tanto sean aprobados […] los
nuevos instrumentos de planificación que los sustituyan»**: no nombra la NBA, que no es directriz ni
plan estatal, y es la nota del BOE la que le extiende esa regla; la disposición final primera del mismo real decreto da **«el
plazo máximo de cuatro años»** para adaptar a la nueva norma **«la Norma Básica de Autoprotección»**;
y el artículo 12 de la Norma Básica de Protección Civil que ese real decreto aprueba define ya los planes de autoprotección **«de acuerdo con la Directriz Básica de
Planificación de Autoprotección»**. A 25 de septiembre de 2026 no se ha localizado en el BOE esa
Directriz ni otra norma que sustituya a la de 2007: lo que sigue es, pues, la norma que se sigue
aplicando, formalmente derogada.

Su anexo II ordena el contenido del plan de autoprotección en capítulos, y varios sirven de
esqueleto a cualquier plan de contingencia:

El capítulo 6 del anexo II (**«Plan de actuación ante emergencias»**) clasifica las emergencias
**«En función del tipo de riesgo.»**, **«En función de la gravedad.»** y **«En función de la ocupación y
medios humanos.»**, y ordena los procedimientos: **«a) Detección y Alerta. b) Mecanismos de Alarma.»**
(con la identificación de quién da los avisos y del centro de coordinación de emergencias de
Protección Civil), **«c) Mecanismos de respuesta frente a la emergencia. d) Evacuación y/o
Confinamiento. e) Prestación de las Primeras Ayudas. f) Modos de recepción de las Ayudas
externas.»** Mantenimiento de la eficacia: **«se realizarán simulacros de emergencia, con la
periodicidad mínima que fije el propio plan, y en todo caso, al menos una vez al año evaluando sus
resultados.»** (3.6.4). Y vigencia (3.7): **«El Plan de Autoprotección tendrá vigencia indeterminada;
se mantendrá adecuadamente actualizado, y se revisará, al menos, con una periodicidad no superior a
tres años.»**

Del mismo anexo II, otros tres capítulos tocan directamente al mantenimiento. El capítulo 5,
**«Programa de mantenimiento de instalaciones.»**, exige la **«Descripción del mantenimiento
preventivo de las instalaciones de riesgo, que garantiza el control de las mismas.»** y la de
**«las instalaciones de protección, que garantiza la operatividad de las mismas.»**, y que se
acompañe **«al menos de un cuadernillo de hojas numeradas donde queden reflejadas las operaciones
de mantenimiento realizadas, y de las inspecciones de seguridad»**. El capítulo 7 incluye **«7.1
Los protocolos de notificación de la emergencia»**. Y el capítulo 9, **«Mantenimiento de la
eficacia y actualización del Plan de Autoprotección.»**, comprende, entre otros, el **«9.2
Programa de sustitución de medios y recursos.»** y el **«9.3 Programa de ejercicios y
simulacros.»**

Lo que este modelo enseña para cualquier plan de contingencia (oficio): clasificar las
situaciones por tipo y gravedad; decir quién da el aviso y a quién; decir quién decide; decir qué
se hace en cada caso; mantener los medios; y ensayarlo. Si la RTVA está obligada a plan de
autoprotección por el anexo I de la NBA, y qué dice el suyo, no consta en un documento publicado.

### 6.3 El plan de vuelta atrás de una intervención

Toda intervención en una instalación crítica se planifica con su vuelta atrás: cómo se deja la
instalación como estaba si el trabajo no puede terminarse dentro de la ventana o si, terminado, lo
nuevo no funciona (oficio). Sus piezas:

| Pieza | En qué consiste |
|---|---|
| Estado inicial documentado | Posición de cada aparato, ajustes de las protecciones, parámetros del equipo, fotografías del cableado antes de desmontar |
| Lo retirado, conservado | El equipo, la tarjeta o las baterías que se sustituyen no se desechan hasta que lo nuevo ha pasado el retorno al servicio |
| Configuración y programa anteriores guardados | Copia de la configuración del SAI, del autómata o del BMS antes de cambiar nada, y la versión anterior del programa a mano |
| Repuesto en mano | Lo que puede romperse durante la intervención (un fusible, un interruptor, un borne) está en la sala, no en el almacén |
| Fuente alternativa | Si la carga se va a quedar sin redundancia, qué se hace si falla la vía que queda: grupo preparado, alimentación provisional, paso de la emisión a reserva |
| Criterio para abortar | Qué hechos obligan a deshacer (una alarma en la vía que queda, el punto de no retorno, un daño no previsto) y quién lo decide |

La actualización de programas merece una línea propia, porque es la intervención que más se
subestima. El RITE, en su instrucción de montaje (IT 2), dentro del ajuste del control automático, la
reserva para los sistemas de control de las instalaciones térmicas a personal cualificado o al
suministrador de los programas:

> **4. Cuando la instalación disponga de un sistema de control, mando y gestión o telegestión
> basado en la tecnología de la información, su mantenimiento y la actualización de las versiones
> de los programas deberá ser realizado por personal cualificado o por el mismo suministrador de
> los programas.**
>
> — Real Decreto 1027/2007, RITE, IT 2.3.4, apartado 4.

La regla de oficio que la acompaña: una actualización es un cambio en una instalación crítica, y
se planifica como cualquier otra intervención, con ventana y con la versión anterior guardada
para volver a ella.

### 6.4 Redundancia y repuesto: la contingencia que ya está montada

El mejor plan de contingencia es el que no necesita a nadie: la redundancia. Los niveles, de menos
a más, con lo que tarda cada uno en entrar:

| Nivel | En qué consiste | Cuánto tarda en entrar |
|---|---|---|
| Repuesto en almacén | Hay otra unidad, apagada, en la estantería | El tiempo de ir a por ella y configurarla |
| Reserva fría | Hay otra unidad instalada y apagada | El tiempo de encenderla y conmutar |
| Reserva caliente | Hay otra unidad instalada, encendida y sincronizada | El tiempo de accionar la conmutación |
| Redundancia interna del propio equipo | El equipo tiene dos fuentes, dos ventiladores o discos en RAID | Ninguno: sigue funcionando con la pieza rota dentro |

Dónde está la redundancia en una cadena de emisión típica: doble alimentación desde dos cuadros
distintos, con sistema de alimentación ininterrumpida y grupo electrógeno detrás; doble camino de
señal por matrices distintas; doble servidor de emisión sincronizado; y doble enlace hacia el
centro emisor. La lista completa es larga, y lo que hay que retener es el criterio: se duplica lo
que no puede parar y se tiene repuesto de lo que sí.

Para el plan de contingencia, la tabla
se lee al revés (oficio): de cada elemento crítico hay que saber en qué nivel está, porque eso
dice cuánto dura la incidencia si falla. Un elemento crítico que sólo tiene repuesto en almacén
tiene, como contingencia, el tiempo de ir a por él, montarlo y configurarlo.

### 6.5 Probar la contingencia

Un plan que no se ha probado es una suposición. Para la redundancia, el aviso es éste:

Una redundancia que no se prueba no existe. Una segunda fuente que lleva tres años sin dar
corriente puede estar averiada y nadie lo sabrá hasta que caiga la primera.

Por eso los ensayos de transferencia y de descarga van en ventana pactada (3.4), y por eso el
plan de autoprotección exige simulacros al menos una vez al año (6.2). Para el plan de
contingencia de la instalación (oficio): cada procedimiento de maniobra escrito se ensaya, en
ventana, con quien lo tendría que ejecutar de madrugada; y se revisa cada vez que cambia la
instalación, porque un procedimiento que describe un cuadro que ya no existe es peor que no tener
procedimiento.

## 7. Retorno al servicio

### 7.1 Qué es devolver una instalación

Retornar al servicio no es volver a dar tensión: es devolver a producción una instalación
comprobada, con su redundancia repuesta, y que producción lo sepa (oficio). Ninguna norma leída
fija un procedimiento de retorno al servicio con ese nombre. Lo que sí fijan las normas son dos
piezas: cómo se repone la tensión y qué comprobaciones se hacen después de montar o transformar un
equipo.

### 7.2 La reposición de la tensión

La reposición de la tensión después de un trabajo sin tensión tiene procedimiento reglamentario,
desarrollado en el tema 15, 2.4. Su comienzo y su regla final:

> **La reposición de la tensión sólo comenzará, una vez finalizado el trabajo, después de que se
> hayan retirado todos los trabajadores que no resulten indispensables y que se hayan recogido de
> la zona de trabajo las herramientas y equipos utilizados.**
>
> […]
>
> **Desde el momento en que se suprima una de las medidas inicialmente adoptadas para realizar el
> trabajo sin tensión en condiciones de seguridad, se considerará en tensión la parte de la
> instalación afectada.**
>
> — Real Decreto 614/2001, anexo II, A.2.

Entre una y otra, el proceso comprende cuatro pasos: **«1.º La retirada, si las hubiera, de las
protecciones adicionales y de la señalización que indica los límites de la zona de trabajo.»**,
**«2.º La retirada, si la hubiera, de la puesta a tierra y en cortocircuito.»**, **«3.º El
desbloqueo y/o la retirada de la señalización de los dispositivos de corte.»** y **«4.º El cierre
de los circuitos para reponer la tensión.»** Y, como la supresión, la hacen **trabajadores
autorizados** (1.4).

En una instalación crítica, la reposición se ordena además por escalones (oficio): primero las
alimentaciones principales y después las cargas, de aguas arriba hacia aguas abajo, sin cerrar de
golpe todo lo que cuelga de un SAI o de un grupo, para no provocar una punta de arranque que
dispare protecciones o lleve el SAI a bypass. Y no se cierra sobre un equipo de producción sin que
quien lo opera esté avisado.

### 7.3 Las comprobaciones que exige la norma

El Real Decreto 1215/1997 obliga a comprobar los equipos de trabajo cuya seguridad depende de su
instalación:

> **1. El empresario adoptará las medidas necesarias para que aquellos equipos de trabajo cuya
> seguridad dependa de sus condiciones de instalación se sometan a una comprobación inicial, tras
> su instalación y antes de la puesta en marcha por primera vez, y a una nueva comprobación
> después de cada montaje en un nuevo lugar o emplazamiento, con objeto de asegurar la correcta
> instalación y el buen funcionamiento de los equipos.**
>
> — Real Decreto 1215/1997, artículo 4.1.

Y, para los sometidos a influencias susceptibles de ocasionar deterioros que puedan generar
situaciones peligrosas, **«comprobaciones adicionales de tales
equipos cada vez que se produzcan acontecimientos excepcionales, tales como transformaciones,
accidentes, fenómenos naturales o falta prolongada de uso, que puedan tener consecuencias
perjudiciales para la seguridad.»** (artículo 4.2), hechas por **«personal competente»** (4.3) y
cuyos resultados **«deberán documentarse y estar a disposición de la autoridad laboral»** y
**«conservarse durante toda la vida útil de los equipos.»** (4.4). Tratar como transformación del
apartado 2 una sustitución de aparamenta, la ampliación de un cuadro o un equipo que vuelve tras
una avería grave es criterio de oficio, no lo concreta el artículo; lo prudente es comprobarlos
antes de devolverlos.

Para la instalación eléctrica, las verificaciones previas a la puesta en servicio y la
documentación de una modificación están en el REBT (tema 2): una ampliación o modificación hecha
en una ventana no se da por terminada hasta que tiene su verificación y, si procede, su
tramitación.

### 7.4 La secuencia de retorno

La secuencia que cierra una intervención, de oficio, en el orden en que se hace:

| Paso | Qué se comprueba |
|---|---|
| 1. Trabajo terminado y zona despejada | Nadie en la zona, herramientas recogidas, tapas puestas (7.2) |
| 2. Comprobación en frío | Lo que se ha montado, conectado y apretado; aislamiento si se ha intervenido en conductores (tema 14) |
| 3. Reposición de la tensión | Por el procedimiento de 7.2, por escalones |
| 4. Comprobación funcional | Que cada equipo arranca, que el SAI vuelve a inversor, que el grupo queda en automático, que las alarmas se borran en el BMS |
| 5. Prueba con carga | Que lo intervenido aguanta la carga real: es la única prueba que dice que funciona (3.4) |
| 6. Redundancia repuesta | Que las dos ramas alimentan otra vez, que el STS ve las dos fuentes, que no queda nada en bypass |
| 7. Devolución a producción | Comunicada y aceptada por quien autorizó la ventana (5.3, cierre) |
| 8. Vigilancia reforzada | Las primeras horas: alarmas, temperaturas y, si se ha tocado una conexión de potencia, una termografía en carga |

El paso 6 es el que más se olvida. Una intervención que termina con la carga alimentada pero con
el SAI intervenido todavía en bypass ha devuelto el servicio y se ha dejado la redundancia por el
camino: la instalación cree tener 2N y tiene N (tema 8, 9.4). Y la devolución del paso 7 no es
un trámite: hasta que producción no la acepta, la instalación sigue siendo responsabilidad de
quien la paró.

### 7.5 El cierre y las lecciones

La intervención termina con el papel (oficio):

- La OT cerrada, con lo hecho, los repuestos usados, las medidas tomadas y la duración real de la
  ventana frente a la prevista (tema 13).
- La documentación actualizada: un esquema que no recoge el cambio hecho en la ventana es el
  error del siguiente análisis de impacto.
- Las comprobaciones documentadas, como exige el artículo 4.4 del Real Decreto 1215/1997 (7.3).
- Si algo salió mal, o casi: qué pasó, por qué y qué se cambia para la próxima vez. Una vuelta
  atrás que hubo que ejecutar, una ventana que se alargó o una redundancia que no conmutó son la
  información más valiosa que da una intervención.

### 7.6 Un caso completo, de principio a fin

Ejemplo de estudio (oficio; no describe una instalación ni un procedimiento de la RTVA). Es la
sustitución de baterías del SAI A del control central analizada en 2.5, recorrida entera:

| Fase | Decisión |
|---|---|
| Definir | OT de sustitución de la batería del SAI A, con la gama del fabricante; servicio técnico del fabricante presente; esquema de las ramas A y B y procedimiento de paso a bypass escritos |
| Analizar | La carga entera queda en la rama B, sin redundancia; los dos conversores de una sola entrada dependen del STS; riesgo residual: caída del control central si falla el SAI B |
| Preparar | Comprobar la carga real de la rama B y el estado del SAI B; batería nueva en la sala; batería vieja no se retira del edificio hasta el final; configuración del SAI A guardada |
| Ventana | Madrugada sin directos, con la emisión preparada para pasar a reserva si la rama B da una alarma; punto de no retorno fijado antes de desconectar la batería vieja |
| Coordinar | Pacto con emisión y control central; aviso a las salas que cuelgan del control; coordinación con el servicio técnico externo y, por la concurrencia, valoración de recurso preventivo (4.3); permiso de trabajo |
| Ejecutar | Paso a bypass y aislamiento del SAI A por su procedimiento; la batería se trabaja con las precauciones de las baterías, porque no tiene interruptor que la deje sin tensión (tema 7, 8.4); avance comunicado al control central |
| Contingencia | Si el SAI B da una alarma: se para el trabajo y se avisa para pasar la emisión a reserva. Si la batería nueva no carga o da defecto: se vuelve a montar la vieja, si la sustitución se hizo por un fallo de capacidad y no de seguridad, o se deja el SAI A en bypass y se comunica que la rama A está sin protección |
| Retornar | Reposición, vuelta a inversor, prueba con carga, comprobación de que la rama A alimenta otra vez y de que el STS ve las dos fuentes; devolución a emisión; vigilancia de alarmas y temperatura de la batería |
| Cerrar | OT con fecha de instalación de la batería nueva (para su vida útil y su próxima prueba de descarga), duración real de la ventana e incidencias |

## Normativa que el tema invoca

- Ley 8/2011, de 28 de abril, por la que se establecen medidas para la protección de las
  infraestructuras críticas: artículo 2, letras a), d), e), h) y j), sólo como vocabulario, y
  artículo 4.
- Ley 31/1995, de 8 de noviembre, de Prevención de Riesgos Laborales: artículo 29.2.4.º (y
  artículo 24, desarrollado en el tema 15).
- Real Decreto 171/2004, de 30 de enero, de coordinación de actividades empresariales: desarrollado
  en el tema 15.
- Real Decreto 39/1997, de 17 de enero, Reglamento de los Servicios de Prevención: artículo 22
  bis, apartados 1.a) y 2.
- Real Decreto 1215/1997, de 18 de julio, sobre equipos de trabajo: artículo 4 y anexo II,
  apartado 1, punto 14.
- Real Decreto 614/2001, de 8 de junio, sobre protección frente al riesgo eléctrico: anexo II, A
  y A.2. Desarrollo en el tema 15.
- Real Decreto 393/2007, de 23 de marzo, Norma Básica de Autoprotección (derogada por el Real
  Decreto 524/2023 con efectos de 11/07/2023; se sigue aplicando hasta que se apruebe el
  instrumento que la sustituya): Norma, apartados 3.3, 3.6.4 y 3.7; anexo II, capítulos 5, 6, 7
  y 9.
- Real Decreto 1027/2007, de 20 de julio, Reglamento de instalaciones térmicas en los edificios:
  IT 2.3.4, apartado 4.
- X Convenio colectivo de la RTVA (BOJA núm. 240, de 10 de diciembre de 2014): artículo 50.11 y
  anexo III.
- Normas técnicas citadas sólo por su ficha de catálogo: UNE-EN ISO 22301:2020 y UNE-EN ISO
  22313:2020.

## Lo que este tema no da, y dónde está

- Una definición normativa de instalación crítica aplicada a la radiotelevisión, de ventana de
  mantenimiento, de análisis de impacto, de plan de contingencia o de retorno al servicio: no
  existe en el BOE ni en el BOJA. Todo lo que el tema dice de ellos es oficio, y así se declara.
- El contenido de la UNE-EN ISO 22301 y 22313 (análisis de impacto en el negocio, objetivos de
  tiempo de recuperación y sus siglas) y el de la UNE-EN 50110-1, de explotación de instalaciones
  eléctricas: normas de pago, no leídas.
- Si alguna instalación de la RTVA es infraestructura crítica conforme a la Ley 8/2011 (no consta
  en ningún documento publicado) y el estado de la transposición de la Directiva (UE) 2022/2557, de
  entidades críticas: no confirmados.
- Si la RTVA está obligada a plan de autoprotección por el anexo I de la NBA, el contenido de su
  plan y la norma andaluza de autoprotección: no confirmados. La NBA en general, su derogación y su
  aplicación a la producción: tema 11, epígrafe 7, y tema 14 del específico de Productor/a.
- Lo propio de la RTVA: su procedimiento para autorizar ventanas, su protocolo de comunicación de
  incidencias técnicas, sus planes de contingencia, la existencia de una cadena o un centro de
  emisión de reserva y su organización de guardias más allá de lo que dice el convenio no constan
  en ningún documento publicado.
- La notación N, N+1 y 2N, los puntos únicos de fallo, los STS y la serie UNE-EN 50600: tema 8.
  Las pruebas periódicas del grupo y del SAI y la actuación ante sus incidencias: tema 7. Las
  gamas, las OT, la priorización y los repuestos: tema 13. Las medidas y los instrumentos: tema 14.
  La consignación, las cinco reglas de oro, los trabajos en tensión, los permisos de trabajo y la
  coordinación de actividades empresariales: tema 15. Las alarmas y los históricos del BMS: tema
  12. Las verificaciones y la documentación del REBT: tema 2. Los derechos y obligaciones preventivos
  (incluida la paralización ante riesgo grave e inminente) y el accidente de trabajo: tema 19.

## Trazabilidad

| Fuente | Qué se ha tomado | Leída |
|---|---|---|
| Ley 8/2011 (BOE-A-2011-7630), artículos 2 y 4, redacción única (desde el 30/04/2011); norma no derogada | Artículo 2, letras a), d), e), h) (encabezamiento y criterios 1 a 4) y j); artículo 4 (responsable del Catálogo) | En el BOE consolidado, 05/10/2026 |
| Ley 31/1995 (BOE-A-1995-24292), artículo 29, redacción única (desde el 10/02/1996) | Apartado 2.4.º | En el BOE consolidado, 05/10/2026 |
| Real Decreto 39/1997 (BOE-A-1997-1853), artículo 22 bis, en la redacción del Real Decreto 604/2006 (BOE-A-2006-9379), desde el 29/06/2006 | Apartados 1.a) y 2 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 1215/1997 (BOE-A-1997-17824): artículo 4, redacción única (desde el 27/08/1997); anexo II en la del Real Decreto 2177/2004 (BOE-A-2004-19311), desde el 03/12/2004 | Artículo 4.1 a 4.4; anexo II, apartado 1, punto 14 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 614/2001 (BOE-A-2001-11881), anexo II, redacción única (desde el 21/08/2001) | A (primer párrafo) y A.2 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 393/2007 (BOE-A-2007-6237), redacción única; nota de derogación del BOE (BOE-A-2023-14679) | Norma, 3.3.3 (encabezamiento y letras b) a e)); anexo II, capítulos 5, 7.1 y 9. Los párrafos de la derogación y del capítulo 6, 3.6.4 y 3.7 se toman del tema 14 del específico de Productor/a, ya cerrado | En el BOE consolidado, 05/10/2026 |
| Real Decreto 1027/2007, RITE (BOE-A-2007-15820), IT 2, redacción única (desde el 29/02/2008) | IT 2.3.4, apartado 4 | En el BOE consolidado, 05/10/2026 |
| X Convenio colectivo de la RTVA (BOJA núm. 240, de 10/12/2014) | Artículo 50.11; anexo III, puestos 9311100, 9311200 y 9300000 | 05/10/2026 |
| Fichas de catálogo (tienda de normas de la Asociación Española de Normalización) de UNE-EN ISO 22301:2020 (y su modificación A1:2024) y UNE-EN ISO 22313:2020 | Título, fecha y estado. Sólo metadatos | 05/10/2026 |

Ninguno de los preceptos citados cambió entre el 24/09/2026 y la fecha de lectura.

Son oficio, y así se declaran, sin atribuirlos a la norma: el sentido técnico de «instalación
crítica»; el reparto de tareas entre la jefatura y el oficial leído en las fichas del convenio; el
ciclo de ocho fases de una intervención; las cinco preguntas del análisis de impacto y la
traducción de equipos a servicios; el orden de prioridades y la tabla de áreas de una televisión;
la tabla de redundancia consumida durante la intervención; el ejemplo de 2.5 y el caso de 7.6; los
datos, la elección, las clases de tarea, la duración y el punto de no retorno de una ventana; lo
que se pacta con producción; las dos clases de incidencia, los tres momentos y las tres reglas de
la comunicación; el registro de la incidencia; los dos niveles de plan de contingencia, las piezas
de la vuelta atrás y la tabla de niveles de redundancia; la reposición por escalones; la
secuencia de retorno y el cierre. Ninguna de esas tablas procede de un procedimiento de la RTVA.
