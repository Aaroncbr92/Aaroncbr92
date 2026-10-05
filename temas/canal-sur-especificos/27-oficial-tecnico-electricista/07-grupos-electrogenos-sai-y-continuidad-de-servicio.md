# Tema 7 del específico de Oficial Técnico Electricista · Grupos electrógenos, sistemas de alimentación ininterrumpida y continuidad de servicio

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Oficial Técnico Electricista · punto 7 |
| **Sirve para** | Puesto 2.27, Oficial Técnico Electricista (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión (BOE-A-2002-18099): artículo 10 del Reglamento, ITC-BT-28 (apartados 2, 3 y 4) e ITC-BT-40. Real Decreto 513/2017, de 22 de mayo, Reglamento de instalaciones de protección contra incendios (BOE-A-2017-6606): anexo II, tabla I. Clasificación de los SAI de la norma IEC 62040-3, sólo a través de una fuente secundaria (W. Sölter). Lo demás, oficio |
| **Redacción que se estudia** | La vigente el día de la lectura (05/10/2026): ITC-BT-40 en la redacción dada por el Real Decreto 244/2019, de 5 de abril (vigente desde el 07/04/2019); artículo 10 e ITC-BT-28 en su única redacción (vigente desde el 18/09/2003); anexo II del Real Decreto 513/2017 en la redacción vigente desde el 10/05/2025 |
| **Extensión** | 12.400 palabras aproximadamente |

<!-- /portada -->

Siglas y unidades que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Reglamento electrotécnico para
baja tensión (**REBT**) y sus instrucciones técnicas complementarias (**ITC-BT**), de las que se
usan la de locales de pública concurrencia (**ITC-BT-28**) y la de instalaciones generadoras de
baja tensión (**ITC-BT-40**); Reglamento de instalaciones de protección contra incendios
(**RIPCI**); sistema de alimentación ininterrumpida (**SAI**), que en inglés se llama
*uninterruptible power supply* (**UPS**); normas técnicas españolas (**UNE**); Comisión Electrotécnica Internacional (**IEC**,
*International Electrotechnical Commission*); las tres clases de SAI de la norma IEC 62040-3
(**VFD**, **VI** y **VFI**, explicadas en su epígrafe); centro de proceso de datos
(**CPD**); unidad móvil (**UM**); esquema de conexión a tierra
**TT** (neutro de la fuente a tierra y masas a una tierra distinta, tema 5); voltio (**V**),
amperio hora (**Ah**), vatio hora (**Wh**), kilovatio hora (**kWh**), kilovatio (**kW**),
kilovoltamperio (**kVA**) y hercio (**Hz**).

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.27, punto 7):
>
> Grupos electrógenos, sistemas de alimentación ininterrumpida y continuidad de servicio:
> transferencia de carga, baterías, autonomía, pruebas periódicas y actuación ante incidencias.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: de qué partes consta un grupo electrógeno, qué regula la frecuencia y qué
la tensión, en qué régimen trabaja un grupo de socorro y por qué una misma máquina declara más o
menos potencia, qué corrige la potencia de placa (altitud, temperatura) y por qué la carga se mete
por escalones; qué exige el REBT al local del grupo (uso exclusivo, ventilación, escape), qué
protecciones mínimas pide a un generador y con qué umbrales, y cómo se dimensiona el cable de
conexión; qué bloques tiene un SAI, qué diferencia el bypass estático del de mantenimiento, qué
topologías hay, cuál es la única «sin corte» y cómo se llaman en la IEC 62040-3; qué es una fuente
propia de energía, cuándo arranca, qué categorías de conmutación define la ITC-BT-28 y con qué
tiempos, qué fuentes admite para los servicios de seguridad, qué son los suministros de socorro,
reserva y duplicado y qué dispositivos exige el REBT a quien los recibe; qué regímenes de carga
lleva una batería; cómo se clasifican las instalaciones generadoras respecto a la red, qué exige
la conmutación de una asistida, cuándo se admite la transferencia sin corte y con qué requisitos,
y qué esquema de tierra lleva; qué diferencia una pila de una batería, qué es la capacidad y por
qué depende del régimen, qué químicas hay, qué se suma en serie y qué en paralelo y por qué no se
cambia un solo elemento; cómo se dimensiona la autonomía de un SAI con grupo detrás y qué
autonomía mínima pide la norma al alumbrado de seguridad; qué pruebas periódicas necesita un grupo
y un SAI, por qué la prueba en vacío no basta y qué periodicidad fija el RIPCI a las fuentes de
alimentación de la detección de incendios. En la aplicación práctica: qué se hace si el grupo no
arranca, si el SAI pasa a bypass o da alarma de batería, si salta todo un SAI por un cortocircuito
en un circuito, si la red vuelve con microcortes, o cómo se saca un SAI a mantenimiento sin cortar
la carga.

<!-- indice -->

## Índice

- [1. Grupos electrógenos](#1-grupos-electrógenos)
  - [1.1 Qué es y de qué partes consta](#11-qué-es-y-de-qué-partes-consta)
  - [1.2 Las condiciones de trabajo](#12-las-condiciones-de-trabajo)
  - [1.3 El emplazamiento: lo que el reglamento exige](#13-el-emplazamiento-lo-que-el-reglamento-exige)
  - [1.4 Protecciones, cable de conexión y forma de onda](#14-protecciones-cable-de-conexión-y-forma-de-onda)
  - [1.5 La secuencia de funcionamiento](#15-la-secuencia-de-funcionamiento)
- [2. Sistemas de alimentación ininterrumpida](#2-sistemas-de-alimentación-ininterrumpida)
  - [2.1 El diagrama de bloques](#21-el-diagrama-de-bloques)
  - [2.2 Las topologías](#22-las-topologías)
  - [2.3 Los nombres normalizados: VFD, VI y VFI](#23-los-nombres-normalizados-vfd-vi-y-vfi)
  - [2.4 Las prestaciones que hay que mirar al elegir uno](#24-las-prestaciones-que-hay-que-mirar-al-elegir-uno)
- [3. Continuidad de servicio](#3-continuidad-de-servicio)
  - [3.1 Las categorías de conmutación](#31-las-categorías-de-conmutación)
  - [3.2 Las fuentes que se admiten y las fuentes propias de energía](#32-las-fuentes-que-se-admiten-y-las-fuentes-propias-de-energía)
  - [3.3 Los suministros complementarios: socorro, reserva y duplicado](#33-los-suministros-complementarios-socorro-reserva-y-duplicado)
  - [3.4 Qué cuelga del grupo, qué cuelga del SAI y qué no](#34-qué-cuelga-del-grupo-qué-cuelga-del-sai-y-qué-no)
- [4. Transferencia de carga](#4-transferencia-de-carga)
  - [4.1 Las tres clases de instalación generadora](#41-las-tres-clases-de-instalación-generadora)
  - [4.2 La conmutación de una instalación asistida](#42-la-conmutación-de-una-instalación-asistida)
  - [4.3 La transferencia sin corte de una instalación asistida](#43-la-transferencia-sin-corte-de-una-instalación-asistida)
  - [4.4 La puesta a tierra cuando conmuta el grupo](#44-la-puesta-a-tierra-cuando-conmuta-el-grupo)
  - [4.5 El grupo aislado: unidades móviles y exteriores](#45-el-grupo-aislado-unidades-móviles-y-exteriores)
  - [4.6 La transferencia dentro del SAI](#46-la-transferencia-dentro-del-sai)
- [5. Baterías](#5-baterías)
  - [5.1 Pilas y baterías: la distinción y los parámetros](#51-pilas-y-baterías-la-distinción-y-los-parámetros)
  - [5.2 Las químicas y su seguridad](#52-las-químicas-y-su-seguridad)
  - [5.3 La agrupación en serie y en paralelo](#53-la-agrupación-en-serie-y-en-paralelo)
- [6. Autonomía](#6-autonomía)
  - [6.1 La autonomía del SAI](#61-la-autonomía-del-sai)
  - [6.2 La autonomía del grupo](#62-la-autonomía-del-grupo)
  - [6.3 La autonomía que fija la norma](#63-la-autonomía-que-fija-la-norma)
- [7. Pruebas periódicas](#7-pruebas-periódicas)
  - [7.1 El grupo electrógeno](#71-el-grupo-electrógeno)
  - [7.2 El SAI y sus baterías](#72-el-sai-y-sus-baterías)
  - [7.3 Lo que fija la norma](#73-lo-que-fija-la-norma)
- [8. Actuación ante incidencias](#8-actuación-ante-incidencias)
  - [8.1 El orden de prioridades](#81-el-orden-de-prioridades)
  - [8.2 Incidencias del grupo electrógeno](#82-incidencias-del-grupo-electrógeno)
  - [8.3 Incidencias del SAI](#83-incidencias-del-sai)
  - [8.4 La seguridad al intervenir en baterías](#84-la-seguridad-al-intervenir-en-baterías)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## 1. Grupos electrógenos

La idea que hay que tener antes de nada, porque es la que más se confunde: un grupo electrógeno da
autonomía y no da continuidad. Tarda en arrancar y en tomar carga, y ese hueco lo cubre la batería
de un SAI (epígrafe 2). Los dos juntos son un sistema; cada uno por su cuenta, no.

### 1.1 Qué es y de qué partes consta

Para el REBT, un grupo es una instalación generadora: la ITC-BT-40 **se aplica a las instalaciones
generadoras, entendiendo como tales, las destinadas a transformar cualquier tipo de energía no
eléctrica en energía eléctrica** (ITC-BT-40, apartado 1). La misma instrucción llama
**«Autogenerador»** a **la empresa que, subsidiariamente a sus actividades principales, produce,
individualmente o en común, la energía eléctrica destinada en su totalidad o en parte, a sus
necesidades propias**, que es el caso de un edificio con grupo propio.

Un grupo electrógeno es un conjunto motor-alternador que convierte la energía química de un
combustible en energía eléctrica.

| Parte | Qué hace |
|---|---|
| Motor térmico | Gasóleo o gas; da el par y la velocidad |
| Alternador | Convierte el giro en tensión alterna; es una máquina síncrona |
| Regulador de velocidad | Mantiene las revoluciones, y con ellas la frecuencia |
| Regulador de tensión | Ajusta la excitación del alternador; mantiene la tensión |
| Cuadro de control y mando | Arranque, medidas, alarmas, parada |
| Sistema de arranque | Batería, motor de arranque y cargador |
| Depósito de combustible | Diario y, en su caso, depósito nodriza |
| Sistema de refrigeración | Radiador y ventilador, o intercambiador |
| Sistema de escape | Silencioso y conducto al exterior |
| Bancada y antivibratorios | Soporte y aislamiento de vibración |

Y la relación que hay que saber y que explica el regulador de velocidad: la frecuencia de la
tensión que genera un alternador depende de su velocidad de giro y de su número de pares de polos.
Mantener 50 hercios es mantener las revoluciones, y por eso un grupo con el regulador desajustado da
mala frecuencia y no un mal voltaje.

Los dos parámetros que se ajustan por separado y que hay que no confundir:

| Se ajusta | Con qué | Qué controla |
|---|---|---|
| La frecuencia | El regulador de velocidad del motor | Revoluciones por minuto |
| La tensión | El regulador de excitación del alternador | Campo magnético del rotor |

### 1.2 Las condiciones de trabajo

Son cuatro cosas distintas que se dan juntas y se confunden.

Primero, el régimen de servicio. Un grupo no da la misma potencia según cuánto vaya a trabajar, y
la designación normalizada distingue varios regímenes:

| Régimen | Para qué |
|---|---|
| De emergencia o de socorro | Sólo cuando falla la red, un número limitado de horas al año y sin sobrecarga admisible |
| Principal, con carga variable | Funcionamiento continuado como fuente principal, con una carga media limitada y sobrecarga admisible durante un tiempo |
| Continuo | Carga constante y horas ilimitadas; es el régimen más exigente y el de menor potencia declarada |

Y la regla que sale de la tabla y que hay que saber decir: la misma máquina declara más potencia
cuanto menos va a trabajar. Un grupo de emergencia y uno continuo del mismo tamaño no dan la misma
cifra, y comparar dos ofertas sin mirar el régimen es comparar dos cosas distintas.

Segundo, la potencia y el factor de potencia. La potencia de un grupo se declara en
kilovoltamperios y en kilovatios, y la relación entre las dos es el factor de potencia de
referencia. Un grupo dimensionado en kilovatios para una carga con factor de potencia peor del de
referencia se queda corto en corriente, y es un error de dimensionado frecuente.

Tercero, las condiciones ambientales. Las potencias se declaran para unas condiciones de
referencia, y hay que corregirlas:

| Factor | Efecto |
|---|---|
| Altitud | Menos densidad de aire, menos potencia del motor |
| Temperatura ambiente | Más temperatura, menos potencia y menos capacidad de refrigeración |
| Humedad | Efecto menor, pero contemplado |

Los coeficientes son dato de fabricante y de norma de producto, y este tema no los da. Lo que hay
que saber es que existen y que un grupo instalado en altura o en una sala caliente entrega menos de
lo que dice su placa.

Cuarto, el escalón de carga. Un grupo no admite que se le eche toda la carga de golpe, y la razón
es física: al conectar una carga grande, el motor se frena, la frecuencia cae y el regulador tarda
en recuperarla. Por eso las cargas se meten por escalones, y los arranques de motores grandes se
hacen con arrancador progresivo o variador para no exigir la punta al grupo.

### 1.3 El emplazamiento: lo que el reglamento exige

Las condiciones generales de la ITC-BT-40 (apartado 3), literales:

- **Los generadores y las instalaciones complementarias de las instalaciones generadoras, como los
  depósitos de combustibles, canalizaciones de líquidos o gases, etc., deberán cumplir, además, las
  disposiciones que establecen los Reglamentos y Directivas específicos que les sean aplicables.**
- **Cuando las instalaciones generadoras estén alojadas en edificios o establecimientos
  industriales, sus locales, que serán de usos exclusivo, cumplirán con las disposiciones
  reguladoras de protección contra incendios correspondientes.**
- **Los locales donde estén instalados los motores térmicos, cualquiera que sea su potencia,
  deberán estar suficientemente ventilados.**
- **Los conductos de salida de los gases de combustión serán de material incombustible y
  evacuarán directamente al exterior o a través de un sistema de aprovechamiento energético.**

Lo que eso implica en obra:

| Exigencia | Qué implica |
|---|---|
| Local de uso exclusivo | No se comparte con almacén ni con otras instalaciones |
| Protección contra incendios | Cumple las disposiciones reguladoras que le correspondan (tema 11) |
| Ventilación suficiente, cualquiera que sea la potencia | Entrada de aire de combustión y de refrigeración, y salida de aire caliente, dimensionadas |
| Conductos de escape de material incombustible | Y evacuando directamente al exterior, o a un sistema de aprovechamiento energético |
| Depósitos y canalizaciones | Cumplen además sus propios reglamentos |

La ventilación es la exigencia que más se subestima: un grupo necesita aire para tres cosas
distintas —la combustión, la refrigeración del motor y la refrigeración del alternador y del propio
local—, y el caudal que hace falta es muy superior al que la intuición sugiere. Una sala con rejilla
pequeña hace que el grupo se caliente y se pare por temperatura justo cuando más falta hace.

Y el escape merece su párrafo: el conducto tiene que ser incombustible, estar aislado térmicamente
donde pueda tocarse, llevar compensador de dilatación —porque se dilata mucho al calentarse— y salir
donde los gases no vuelvan a entrar por la toma de aire. Un escape que descarga junto a la entrada
de ventilación hace que el grupo respire su propio humo.

El ruido, que en un centro de producción es un asunto de primer orden y no de comodidad: un grupo
es una de las fuentes de ruido y vibración más intensas de un edificio, y lo que hay que resolver
son las tres vías por las que se transmite:

| Vía | Cómo se corta |
|---|---|
| Por el aire | Cabina insonorizada, silencioso de escape, atenuadores en las rejillas |
| Por la estructura | Antivibratorios bajo la bancada y conexiones flexibles en escape, combustible y refrigerante |
| Por los conductos | Manguitos flexibles: un conducto rígido lleva la vibración a todo el edificio |

La vía estructural es la que se olvida y la que arruina una grabación (oficio). Un grupo
perfectamente insonorizado que apoya rígido sobre la losa hace vibrar los estudios que tiene
encima, y eso no lo arregla ninguna cabina.

### 1.4 Protecciones, cable de conexión y forma de onda

Lo que la ITC-BT-40 exige al propio generador, literal:

- Protecciones (apartado 7): **La máquina motriz y los generadores dispondrán de las protecciones
  específicas que el fabricante aconseje para reducir los daños como consecuencia de defectos
  internos o externos a ellos.** **Los circuitos de salida de los generadores se dotarán de las
  protecciones establecidas en las correspondientes ITC que les sean aplicables.** Y **las
  protecciones mínimas a disponer serán las siguientes, con independencia de que estos ajustes
  podrían verse modificados por la normativa del sector eléctrico en función del generador al que
  aplique:**

| Protección mínima | Texto de la ITC-BT-40, apartado 7 |
|---|---|
| Sobreintensidad | **De sobreintensidad, mediante relés directos magnetotérmicos o solución equivalente.** |
| Mínima tensión | **De mínima tensión instantáneos, conectados entre las tres fases y neutro y que actuarán, en un tiempo inferior a 0,5 segundos, a partir de que la tensión llegue al 85% de su valor asignado.** |
| Sobretensión | **De sobretensión, conectado entre una fase y neutro, y cuya actuación debe producirse en un tiempo inferior a 0,5 segundos, a partir de que la tensión llegue al 110% de su valor asignado.** |
| Frecuencia | **De máxima y mínima frecuencia, conectado entre fases, y cuya actuación debe producirse cuando la frecuencia sea inferior a 49 Hz o superior a 51 Hz durante más de 5 períodos.** |

- Cable de conexión (apartado 5): **Los cables de conexión deberán estar dimensionados para una
  intensidad no inferior al 125% de la máxima intensidad del generador y la caída de tensión entre
  el generador y el punto de interconexión a la Red de Distribución Pública o a la instalación
  interior, no será superior al 1,5%, para la intensidad nominal.**
- Forma de onda (apartado 6): **La tensión generada será prácticamente senoidal, con una tasa
  máxima de armónicos, en cualquier condición de funcionamiento de:** **Armónicos de orden par:
  4/n**; **Armónicos de orden 3: 5**; **Armónicos de orden impar (≥5): 25/n**. **La tasa de
  armónicos es la relación, en %, entre el valor eficaz del armónico de ordenn** (así en el BOE,
  por «orden n») **y el valor eficaz del fundamental.**

Las dos cifras que hay que retener son las del cable: 125 % de la intensidad máxima y 1,5 % de
caída de tensión a intensidad nominal. Y la lectura de los relés desde el mantenimiento (oficio): con esos
ajustes, un generador cuya frecuencia sale de 49-51 Hz durante más de cinco períodos, o cuya
tensión baja al 85 % o sube al 110 %, se desconecta; por eso un regulador de velocidad desajustado
o un escalón de carga excesivo (1.2) pueden acabar en disparo y no sólo en mala calidad.

### 1.5 La secuencia de funcionamiento

Lo que ocurre desde que falla la red hasta que vuelve, paso a paso, que es lo que hay que saber
explicar y lo que se programa en el cuadro de control:

| Fase | Qué pasa |
|---|---|
| 1 · Detección del fallo | Falta de tensión o tensión por debajo del umbral, durante un tiempo de confirmación |
| 2 · Apertura del interruptor de red | Se aísla la instalación de la red |
| 3 · Arranque del motor | Por batería; con un número limitado de intentos |
| 4 · Estabilización | Espera a que tensión y frecuencia estén dentro de límites |
| 5 · Cierre del interruptor de grupo | La instalación queda alimentada |
| 6 · Toma de carga por escalones | Si el automatismo lo prevé |
| 7 · Vuelta de la red | Se confirma durante un tiempo, para evitar retornos inestables |
| 8 · Retransferencia | Con corte o sin corte, según el sistema |
| 9 · Refrigeración y parada | El motor sigue girando en vacío unos minutos antes de pararse |

El umbral de la fase 1 no es libre cuando el grupo es fuente propia de los servicios de seguridad
de un local de pública concurrencia: la ITC-BT-28 fija que la fuente arranca al faltar la tensión de la distribuidora o cuando ésta
desciende por debajo del 70 % de su valor nominal (texto literal en 3.2).

Las dos fases que la gente no espera y que hay que saber justificar:

- La 7. La red vuelve a menudo de forma inestable, con microcortes. Retransferir al primer parpadeo
  puede dejar la instalación sin nada. Por eso se confirma la red durante un tiempo antes de volver.
- La 9. Un motor térmico que se para inmediatamente después de trabajar a plena carga acumula calor
  sin circulación de refrigerante. El giro en vacío evacua ese calor, y saltárselo acorta la vida
  del motor.

## 2. Sistemas de alimentación ininterrumpida

El grupo electrógeno da autonomía y el sistema de alimentación ininterrumpida da continuidad. A
juicio de oficio (la ITC no asigna categorías a las fuentes), el SAI de doble conversión es la
única de las fuentes de este tema que cumple la categoría «sin corte» de la ITC-BT-28 (epígrafes
3.1 y 2.2), porque su energía ya está almacenada y no hay nada que
arrancar.

### 2.1 El diagrama de bloques

Los cinco bloques, en orden, con lo que hace cada uno:

| Bloque | Qué hace |
|---|---|
| Rectificador o cargador | Convierte la alterna de entrada en continua, y carga la batería |
| Batería | Almacena la energía: es la autonomía |
| Inversor u ondulador | Convierte la continua en alterna de salida, con su tensión y su frecuencia |
| Bypass estático | Un camino alternativo directo de la red a la salida, con conmutación por semiconductores |
| Bypass de mantenimiento | Un camino manual que permite sacar el equipo entero sin cortar la carga |

Y los dos bypass son lo que más se confunde y hay que separarlos con claridad:

| Bypass | Cuándo actúa | Cómo |
|---|---|---|
| Estático o automático | Ante una sobrecarga o un fallo del inversor | Solo, en milisegundos |
| De mantenimiento o manual | Cuando hay que reparar o sustituir el equipo | A mano, con una secuencia de maniobra |

La razón de ser del bypass de mantenimiento merece una frase: sin él, cambiar un sistema de
alimentación ininterrumpida obliga a dejar sin tensión todo lo que protege. Con él, se transfiere
la carga a la red, se saca el equipo y se vuelve. Un sistema instalado sin bypass de mantenimiento
es un sistema que garantiza continuidad excepto el día en que hay que tocarlo.

### 2.2 Las topologías

Tres, y hay que saber cuál protege de qué, porque es la decisión de compra:

| Topología | Cómo funciona en normal | Qué corrige | Tiempo de transferencia |
|---|---|---|---|
| Pasiva o de espera | La carga va directa a la red; la batería espera | Sólo el corte | Hay transferencia, de milisegundos |
| Interactiva con la línea | Directa a la red, con un regulador que corrige la tensión | Corte y variaciones de tensión | Hay transferencia, menor |
| En línea, de doble conversión | La energía siempre pasa por rectificador e inversor | Corte, tensión, frecuencia, forma de onda y perturbaciones | No hay transferencia: es «sin corte» |

La tercera es la única que cumple la categoría «sin corte», y la razón hay que saber decirla: en
doble conversión la carga nunca está alimentada por la red directamente. Está alimentada siempre
por el inversor, y cuando falta la red, lo único que cambia es de dónde saca la continua el
inversor: de la batería en vez del rectificador. La salida no se entera.

Y lo que las otras dos aportan a cambio: rendimiento y precio. Una doble conversión convierte la
energía dos veces siempre, y eso tiene un coste energético permanente. Por eso los equipos modernos
ofrecen un modo de alta eficiencia que trabaja en espera y pasa a doble conversión cuando la red se
degrada, con la contrapartida de que en ese modo ya no es «sin corte».

### 2.3 Los nombres normalizados: VFD, VI y VFI

La norma de clasificación de los SAI es la IEC 62040-3. Este tema no la ha leído (es de pago) y la
toma de la descripción que de su primera edición (1999) hizo W. Sölter, miembro del subcomité 22H de
la IEC. El código se forma en tres pasos: **«STEP 1: dependency of UPS output on the
input power grid – STEP 2: the voltage waveform of the UPS output – STEP 3: the dynamic tolerance
curves of the UPS output»** (paso 1, dependencia de la salida respecto de la red; paso 2, forma de
onda de la salida; paso 3, curvas de tolerancia dinámica). El primer paso da las tres clases, que
son las tres topologías de 2.2:

| Clase | Definición (Sölter, sobre la IEC 62040-3) | Topología |
|---|---|---|
| VFD | **«The UPS output is dependent on changes in power line voltage and frequency when it has no corrective means»** (la salida depende de la tensión y la frecuencia de la red) | Pasiva o de espera (**«previously "offline"»**) |
| VI | **«Output voltage is dependent on power line frequency but remains within prescribed limits through active or passive regulating mechanisms.»** (depende de la frecuencia de la red; la tensión se regula) | Interactiva con la línea (**«line interactive»**) |
| VFI | **«Output voltage is independent of all power line voltage and frequency fluctuations»** (independiente de tensión y frecuencia de la red) | Doble conversión (**«double conversion (previously: online)»**) |

Para recordar las siglas: V es tensión (*voltage*), F es frecuencia, D es dependiente y I es
independiente; VFD, tensión y frecuencia dependientes; VFI, independientes; VI, sólo la tensión
independiente. El tercer paso son tres cifras sobre el comportamiento dinámico de la salida, y la
clase 1 es la más exigente: según el mismo autor, **«The triple "Classification 1" rating is only
possible with this type of UPS»**, el VFI. La fuente describe la primera edición de la norma; si hay otra posterior, cuál es la
vigente y su transposición UNE no se han confirmado.

### 2.4 Las prestaciones que hay que mirar al elegir uno

Además de la topología:

| Prestación | Qué es |
|---|---|
| Potencia | En kilovoltamperios y en kilovatios, con su factor de potencia de salida |
| Autonomía | A qué carga y durante cuánto: no significa nada sin las dos cosas |
| Factor de potencia de entrada y distorsión | Lo que el equipo devuelve a la red: un rectificador antiguo ensucia mucho |
| Capacidad de sobrecarga | Y cuánto tiempo la aguanta |
| Corriente de cortocircuito que puede aportar | Decide si las protecciones aguas abajo van a disparar |

La última es la que se olvida y la que produce el fallo más desconcertante: un inversor limita su
corriente de salida, de modo que un cortocircuito aguas abajo puede no producir corriente
suficiente para hacer saltar el magnetotérmico correspondiente. El resultado es que el sistema se
protege a sí mismo pasando a bypass o desconectando, y cae toda la carga en vez del circuito
averiado. La selectividad aguas abajo de un sistema de alimentación ininterrumpida hay que
comprobarla, no suponerla (la selectividad como tal es materia del tema 3).

La tercera fila tiene una consecuencia de instalación (oficio): un SAI con rectificador de mala
calidad alimentado desde el grupo le devuelve una corriente distorsionada, y un grupo pequeño la
tolera peor que la red. Por eso el SAI y el grupo se eligen juntos.

Y el criterio que sale de ahí (oficio): el grupo que alimenta un SAI se dimensiona por encima de la
potencia de salida del SAI, no igual a ella. Tres razones se suman: el rectificador toma una
corriente distorsionada que el alternador del grupo tolera peor que la red; cuando el grupo toma
carga tras un corte, el SAI le pide a la vez la potencia de la carga y la de recarga de la batería
que acaba de descargarse (3.4); y el rendimiento del SAI no es la unidad, así que su entrada pide
más que su salida. La batería no permite un grupo menor —al volver la alimentación, pide recarga—,
ni un buen factor de potencia del grupo resuelve la distorsión. El coeficiente de sobredimensionado
no es dato de ninguna norma leída: lo dan los fabricantes del grupo y del SAI, y depende de la
calidad del rectificador.

## 3. Continuidad de servicio

Continuidad de servicio es que la carga no note el fallo de la red, o que lo note durante un tiempo
que ella tolera. El REBT no la define con esa palabra, pero da las piezas para medirla: los tipos de
suministro, las categorías de conmutación y las fuentes que se admiten para los servicios de
seguridad.

### 3.1 Las categorías de conmutación

La ITC-BT-28 es la instrucción de los locales de pública concurrencia (su apartado 1 fija ese campo
de aplicación, que alcanza también a los locales clasificados en condiciones BD2, BD3 y BD4 y a los
no enumerados con capacidad de ocupación de más de 100 personas): lo que dice de los servicios de
seguridad obliga en esos locales; fuera de ellos, la ITC-BT-28 no obliga por sí misma y sus
categorías y sus fuentes se usan como referencia (oficio).

La ITC-BT-28, apartado 2, define la alimentación de los servicios de seguridad, **tales como
alumbrados de emergencia, sistemas contra incendios, ascensores u otros servicios urgentes
indispensables que están fijados por las reglamentaciones específicas de las diferentes
Autoridades competentes en materia de seguridad.** Y
añade: **La alimentación para los servicios de seguridad, en función de lo que establezcan las
reglamentaciones específicas, puede ser automática o no automática.** Además, **en una alimentación automática la puesta en servicio de la alimentación no
depende de la intervención de un operador.** **Una alimentación automática se clasifica, según la
duración de conmutación, en las siguientes categorías:**

| Categoría | Texto de la ITC-BT-28, apartado 2 |
|---|---|
| Sin corte | **alimentación automática que puede estar asegurada de forma continua en las condiciones especificadas durante el periodo de transición, por ejemplo, en lo que se refiere a las variaciones de tensión y frecuencia.** |
| Con corte muy breve | **alimentación automática disponible en 0,15 segundos como máximo.** |
| Con corte breve | **alimentación automática disponible en 0,5 segundos como máximo.** |
| Con corte mediano | **alimentación automática disponible en 15 segundos como máximo.** |
| Con corte largo | **alimentación automática disponible en mas de 15 segundos.** |

Cinco categorías y cuatro cifras: 0,15 s, 0,5 s, 15 s y más de 15 s. La categoría sin corte no
lleva tiempo, sino una condición: que la alimentación esté asegurada durante la transición.

Dónde cae cada fuente (oficio; la ITC no asigna categorías a las fuentes):

| Fuente | Categoría que puede cumplir | Por qué |
|---|---|---|
| SAI de doble conversión (VFI) | Sin corte | La carga ya está en el inversor; no hay transferencia (2.2) |
| SAI pasivo o interactivo | Corte muy breve | Conmuta en milisegundos |
| Grupo electrógeno con arranque automático | Típicamente corte mediano | Tiene que detectar, arrancar y estabilizarse (1.5); nunca «sin corte» ni «corte muy breve» |
| Grupo con arranque manual | No es alimentación automática | Depende de un operador |

Y la consecuencia que hay que saber: la ITC-BT-28 dice que **la alimentación del alumbrado de
emergencia será automática con corte breve** (apartado 3). Un grupo solo, que tarda segundos, no
la cumple; por eso el alumbrado de emergencia lleva batería propia, en aparatos autónomos o en una
fuente central de baterías (el alumbrado de emergencia es materia del tema 6).

### 3.2 Las fuentes que se admiten y las fuentes propias de energía

**Para los servicios de seguridad la fuente de energía debe ser elegida de forma que la
alimentación esté asegurada durante un tiempo apropiado.** **Se pueden utilizar las siguientes
fuentes de alimentación:** (ITC-BT-28, apartado 2.1)

- **Baterías de acumuladores. Generalmente las baterías de arranque de los vehículos no satisfacen
  las prescripciones de alimentación para los servicios de seguridad**
- **Generadores independientes**
- **Derivaciones separadas de la red de distribución, efectivamente independientes de la
  alimentación normal**

Las condiciones de esas fuentes, en el mismo apartado: **Las fuentes para servicios para servicios
complementarios o de seguridad deben estar instaladas en lugar fijo y de forma que no puedan ser
afectadas por el fallo de la fuente normal. Además, con excepción de los equipos autónomos,
deberán cumplir las siguientes condiciones:**

- **se instalarán en emplazamiento apropiado, accesible solamente a las personas cualificadas o
  expertas.**
- **el emplazamiento estará convenientemente ventilado, de forma que los gases y los humos que
  produzcan no puedan propagarse en los locales accesibles a las personas.**
- **no se admiten derivaciones separadas, independientes y alimentadas por una red de distribución
  pública, salvo si se asegura que las dos derivaciones no puedan fallar simultáneamente.**
- **cuando exista una sola fuente para los servicios de seguridad, ésta no debe ser utilizada para
  otros usos. Sin embargo, cuando se dispone de varias fuentes, pueden utilizarse igualmente como
  fuentes de reemplazamiento, con la condición, de que en caso de fallo de una de ellas, la
  potencia todavía disponible sea suficiente para garantizar la puesta en funcionamiento de todos
  los servicios de seguridad, siendo necesario generalmente, el corte automático de los equipos no
  concernientes a la seguridad.**

La última condición es la base reglamentaria del deslastre de cargas (3.4): si el grupo alimenta
a la vez la seguridad y la producción, al fallar una fuente hay que cortar lo que no es seguridad.
El apartado añade dos exigencias de diseño: **Para que los servicios de seguridad funcionen en caso
de incendio, los equipos y materiales utilizados deben presentar, por construcción o por
instalación, una resistencia al fuego de duración apropiada.** y **Los equipos y materiales
deberán disponerse de forma que se facilite su verificación periódica, ensayos y mantenimiento.**

La fuente propia de energía (apartado 2.2), las tres frases que hay que saber:

- **Fuente propia de energía es la que esta constituida por baterías de acumuladores, aparatos
  autónomos o grupos electrógenos.**
- **La puesta en funcionamiento se realizará al producirse la falta de tensión en los circuitos
  alimentados por los diferentes suministros procedentes de la Empresa o Empresas distribuidoras
  de energía eléctrica, o cuando aquella tensión descienda por debajo del 70% de su valor
  nominal.**
- **La capacidad mínima de una fuente propia de energía será, como norma general, la precisa para
  proveer al alumbrado de seguridad en las condiciones señaladas en el apartado 3.1. de esta
  instrucción.** (Esas condiciones incluyen la autonomía de una hora: 6.3.)

Y una prohibición que afecta al grupo de un local de pública concurrencia (apartado 4, letra g):
**Las fuentes propias de energía de corriente alterna a 50 Hz, no podrán dar tensión de retorno a
la acometida o acometidas de la red de Baja Tensión pública que alimenten al local de pública
concurrencia.** Es la razón de ser de la conmutación que se estudia en 4.2.

### 3.3 Los suministros complementarios: socorro, reserva y duplicado

El artículo 10 del REBT clasifica los suministros **en normales y complementarios**. **Suministros
normales son los efectuados a cada abonado por una sola empresa distribuidora por la totalidad de
la potencia contratada por el mismo y con un solo punto de entrega de la energía.** Y **Suministros
complementarios o de seguridad son los que, a efectos de seguridad y continuidad de suministro,
complementan a un suministro normal. Estos suministros podrán realizarse por dos empresas
diferentes o por la misma empresa, cuando se disponga, en el lugar de utilización de la energía, de
medios de transporte y distribución independientes, o por el usuario mediante medios de producción
propios.** (El grupo electrógeno es uno de esos «medios de producción propios».) **Se considera suministro
complementario aquel que, aun partiendo del mismo transformador, dispone de línea de distribución
independiente del suministro normal desde su mismo origen en baja tensión.**

| Suministro | Texto del artículo 10 del REBT |
|---|---|
| De socorro | **es el que está limitado a una potencia receptora mínima equivalente al 15 por 100 del total contratado para el suministro normal.** |
| De reserva | **es el dedicado a mantener un servicio restringido de los elementos de funcionamiento indispensables de la instalación receptora, con una potencia mínima del 25 por 100 de la potencia total contratada para el suministro normal.** |
| Duplicado | **es el que es capaz de mantener un servicio mayor del 50 por 100 de la potencia total contratada para el suministro normal.** |

Las tres cifras van juntas: 15 %, 25 % y más del 50 %. Y quién debe tenerlos, según la
ITC-BT-28, apartado 2.3: **Deberán disponer de suministro de socorro los locales de espectáculos y
actividades recreativas cualquiera que sea su ocupación y los locales de reunión, trabajo y usos
sanitarios con una ocupación prevista de más de 300 personas.** El suministro de reserva se exige a
hospitales y centros sanitarios, estaciones de viajeros y aeropuertos, estacionamientos
subterráneos para más de 100 vehículos, establecimientos comerciales de más de 2.000 m² y estadios
y pabellones deportivos; y **Cuando un local se pueda considerar tanto en el grupo de locales que
requieren suministro de socorro como en el grupo que requieren suministro de reserva, se instalará
suministro de reserva**. El artículo 10.3 del REBT completa esa lista: **Además de los señalados
en las correspondientes instrucciones técnicas complementarias, los órganos competentes de las
Comunidades Autónomas podrán fijar, en cada caso, los establecimientos industriales o dedicados a cualquier
otra actividad que, por sus características y circunstancias singulares, hayan de disponer de
suministro de socorro, de reserva o suministro duplicado.**

Y el artículo 10.2 del REBT dice qué debe llevar cualquier instalación que reciba un suministro
complementario además del normal: **Las instalaciones previstas para recibir suministros
complementarios deberán estar dotadas de los dispositivos necesarios para impedir un acoplamiento
entre ambos suministros, salvo lo prescrito en las instrucciones técnicas complementarias. La
instalación de esos dispositivos deberá realizarse de acuerdo con la o las empresas
suministradoras. De no establecerse ese acuerdo, el órgano competente de la Comunidad Autónoma
resolverá lo que proceda en un plazo máximo de 15 días hábiles, contados a partir de la fecha en que
le sea formulada la consulta.** Es «deberán», no «podrán»; y la salvedad del final de la primera
frase deja a las instrucciones técnicas complementarias lo que dispongan en contrario.

Si un edificio concreto de la RTVA o de CSRTV es local de pública concurrencia a efectos de la
ITC-BT-28 (por ejemplo, un plató con público) y qué suministro complementario le corresponde es
cuestión de su proyecto, que no consta en ningún documento publicado.

### 3.4 Qué cuelga del grupo, qué cuelga del SAI y qué no

Las decisiones que la norma no toma y que hay que saber razonar (oficio):

1. Qué cuelga del grupo y qué no. Un grupo dimensionado para todo el edificio es carísimo y trabaja
   siempre descargado. Lo correcto es un cuadro de socorro con lo que de verdad no puede caerse
   —control central, emisión, servidores, refrigeración de las salas técnicas, alumbrado de
   seguridad y ascensores— y deslastre automático de lo demás.
2. La refrigeración de las salas técnicas va en el grupo. Es el olvido clásico: se salva el
   equipamiento y se deja fuera el aire acondicionado, y una sala de servidores sin refrigeración
   se apaga sola en minutos. La continuidad eléctrica sin continuidad térmica no sirve.
3. Qué cuelga del SAI: sólo lo que no puede caerse ni un ciclo —control central, emisión,
   servidores, red—, en doble conversión; lo demás puede ir en espera. La refrigeración, que
   arranca con el grupo, no suele ir en el SAI, y por eso el tiempo entre el corte y la toma de
   carga del grupo es el que la sala aguanta sin frío.
4. Cómo se encadenan: el SAI cubre el arranque del grupo; el grupo recarga el SAI.

La cadena completa, del lado de la carga crítica: red → (falla) → el SAI sigue entregando desde su
batería, sin corte → el grupo arranca y toma carga en segundos → el rectificador del SAI pasa a
alimentarse del grupo y recarga la batería → vuelve la red, se confirma y se retransfiere → el
grupo se refrigera en vacío y para. Las redundancias de un CPD o de un centro emisor (dos SAI, dos
ramas, dos acometidas) se estudian en el tema 8.

## 4. Transferencia de carga

Transferencia de carga es pasar la alimentación de una fuente a otra: de la red al grupo, del
grupo a la red (retransferencia), del inversor del SAI a su bypass y vuelta. Cómo se hace la del
grupo lo decide la clase de instalación generadora.

### 4.1 Las tres clases de instalación generadora

**Las Instalaciones Generadoras se clasifican, atendiendo a su funcionamiento respecto a la Red de
Distribución Pública, en:** (ITC-BT-40, apartado 2)

- **a) Instalaciones generadoras aisladas: aquellas en las que no puede existir conexión eléctrica
  alguna con la Red de Distribución Pública.**
- **b) Instalaciones generadoras asistidas: Aquellas en las que existe una conexión con la Red de
  Distribución Pública, pero sin que los generadores puedan estar trabajando en paralelo con ella.
  La fuente preferente de suministro podrá ser tanto los grupos generadores como la Red de
  Distribución Pública, quedando la otra fuente como socorro o apoyo. Para impedir la conexión
  simultánea de ambas, se deben instalar los correspondientes sistemas de conmutación. Será posible
  no obstante, la realización de maniobras de transferencia de carga sin corte, siempre que se
  cumplan los requisitos técnicos descritos en el apartado 4.2.**
- **c) Instalaciones generadoras interconectadas: las que están trabajando normalmente en paralelo
  con la Red de Distribución Pública.**

| Clase | Qué permite | Cómo conmuta |
|---|---|---|
| Aislada | Ninguna conexión con la red | No hay conmutación con red |
| Asistida | Conexión, pero nunca en paralelo | Sistema de conmutación de todos los activos y el neutro; transferencia sin corte sólo con los requisitos de 4.3 |
| Interconectada | Trabajo normal en paralelo | Sincronización permanente |

El grupo de socorro de un edificio es una instalación asistida. El grupo que alimenta en solitario
una unidad móvil o un evento en exteriores es una aislada (4.5). La interconectada es la propia de
la generación que trabaja en paralelo con la red, como el autoconsumo fotovoltaico (tema 18).

### 4.2 La conmutación de una instalación asistida

El texto (ITC-BT-40, apartado 4.2): **En la instalación interior la alimentación alternativa (red
o generador) podrá hacerse en varios puntos que irán provistos de un sistema de conmutación para
todos los conductores activos y el neutro, que impida el acoplamiento simultáneo a ambas fuentes de
alimentación.**

De ahí salen las dos exigencias que un técnico tiene que comprobar en un cuadro de conmutación:

1. La conmutación corta todos los conductores activos y el neutro. No basta con conmutar fases:
   el conmutador red-grupo de una instalación trifásica con neutro es tetrapolar.
2. El acoplamiento simultáneo tiene que ser imposible. En la práctica (oficio) eso es enclavamiento
   mecánico además del eléctrico entre los dos aparatos de maniobra, o un conmutador que por
   construcción no puede tener las dos posiciones cerradas (la aparamenta de maniobra es materia
   del tema 3).

Es la misma idea que el artículo 10.2 del REBT impone a toda instalación prevista para recibir
suministros complementarios (epígrafe 3.3): dispositivos que impidan el acoplamiento entre ambos,
con la salvedad que el propio artículo 10.2 hace de **lo prescrito en las instrucciones técnicas
complementarias**. Una de esas salvedades es la transferencia de carga sin corte que la misma
ITC-BT-40 admite en sus apartados 2 y 4.2 con requisitos (epígrafe 4.3).

La transferencia ordinaria de una asistida es, por tanto, con corte: se abre una fuente y luego se
cierra la otra. El hueco lo cubren los SAI aguas abajo.

### 4.3 La transferencia sin corte de una instalación asistida

Es la excepción. **En el caso en el que esté previsto realizar maniobras de transferencia de carga
sin corte, la conexión de la instalación generadora asistida con la Red de Distribución Pública se
hará en un punto único y deberán cumplirse los siguientes requisitos:** (ITC-BT-40, apartado 4.2)

- **Sólo podrán realizar maniobras de transferencia de carga sin corte los generadores de potencia
  superior a 100 kVA**
- **En el momento de interconexión entre el generador y la red de distribución pública, se
  desconectará el neutro del generador de tierra.**
- **El sistema de conmutación deberá instalarse junto a los aparatos de medida de la Red de
  Distribución pública, con accesibilidad para la empresa distribuidora.**
- **Deberá incluirse un sistema de protección que imposibilite el envío de potencia del generador a
  la red.**
- **Deberán incluirse sistemas de protección por tensión del generador fuera de límites, frecuencia
  fuera de límites, sobrecarga y cortocircuito, enclavamiento para no poder energizar la línea sin
  tensión y protección por fuera de sincronismo.**
- **Dispondrá de un equipo de sincronización y no se podrá mantener la interconexión más de 5
  segundos.**

Y dos frases más del mismo apartado: **El conmutador llevará un contacto auxiliar que permita
conectar a una tierra propia el neutro de la generación, en los casos que se prevea la
transferencia de carga sin corte.** **Los elementos de protección y sus conexiones al conmutador
serán precintables o se garantizará mediante método alternativo que no se pueden modificar los
parámetros de conmutación iniciales y la empresa distribuidora de energía eléctrica, deberá poder
acceder de forma permanente a dicho elemento, en los casos en que se prevea la transferencia de
carga sin corte. El dispositivo de maniobra del conmutador será accesible al Autogenerador.**

Las cifras que hay que retener: más de 100 kVA, punto único y 5 segundos como máximo de
interconexión. Lo que se busca con la transferencia sin corte (oficio) es que la retransferencia
de grupo a red, que es una maniobra programada, no produzca un segundo corte: el grupo se
sincroniza con la red, se cierran los dos durante un instante y se abre el grupo.

Para la puesta en marcha de una asistida (y de una interconectada), **además de los trámites y gestiones que corresponda
realizar, de acuerdo con la legislación vigente ante los Organismos Competentes se deberá presentar
el oportuno proyecto a la empresa distribuidora de energía eléctrica de aquellas partes que afecten
a las condiciones de acoplamiento y seguridad del suministro eléctrico** (ITC-BT-40, apartado 9);
**Este trámite ante la empresa distribuidora de energía eléctrica, no será preciso en las
instalaciones generadoras aisladas.**

### 4.4 La puesta a tierra cuando conmuta el grupo

En una asistida (ITC-BT-40, apartado 8.2.2): **Cuando la Red de Distribución Pública tenga el
neutro puesto a tierra, el esquema de puesta a tierra será el TT y se conectarán las masas de la
instalación y receptores a una tierra independiente de la del neutro de la Red de Distribución
Pública.** **En caso de imposibilidad técnica de realizar un tierra independiente para el neutro del
generador, y previa autorización específica del Organo Competente de la Comunidad Autónoma, se
podrá utilizar la misma tierra para el neutro y las masas.** Y si hay transferencia sin corte, **se
dispondrá, en el conmutador de interconexión, un polo auxiliar que cuando pase a alimentar la
instalación desde la generación propia conecte a tierra el neutro de la generación.**

La razón de fondo (oficio): al abrir el neutro de la red en la conmutación (4.2), la instalación
alimentada por el grupo se queda sin la referencia a tierra que le daba la red; si el neutro del
generador no se pone a tierra, el esquema deja de ser el previsto y las protecciones diferenciales
pueden no funcionar como se espera. Los esquemas de conexión a tierra se estudian en el tema 5.

### 4.5 El grupo aislado: unidades móviles y exteriores

Para las aisladas (ITC-BT-40, apartado 4.1): **La conexión a los receptores, en las instalaciones
donde no pueda darse la posibilidad del acoplamiento con la Red de Distribución Pública o con otro
generador, precisará la instalación de un dispositivo que permita conectar y desconectar la carga
en los circuitos de salida del generador.** **Cuando existan más de un generador y su conexión
exija la sincronización, se deberá disponer de un equipo manual o automático para realizar dicha
operación.** Y la frase que toca de lleno al grupo de una unidad móvil o de una retransmisión:
**Los generadores portátiles deberán incorporar las protecciones generales contra sobreintensidades
y contactos directos e indirectos necesarios para la instalación que alimenten.**

Su puesta a tierra (apartado 8.2.1): **La red de tierras de la instalación conectada a la generación
será independiente de cualquier otra red de tierras.** **En las instalaciones de este tipo se
realizará la puesta a tierra del neutro del generador y de las masas de la instalación conforme a
uno de los sistemas recogidos en la ITC-BT 08.** **En el caso de que trabajen varios generadores en
paralelo, se deberá conectar a tierra, en un solo punto, la unión de los neutros de los
generadores.**

La acometida de una UM y su conexión a red o a grupo se estudian en el tema 8.

### 4.6 La transferencia dentro del SAI

En el SAI hay tres transferencias, y cada una se hace de una manera:

| Transferencia | Quién la hace | Con corte o sin corte |
|---|---|---|
| Red → batería, al fallar la red | En doble conversión, nadie: el inversor sigue | Sin corte (2.2) |
| Inversor → bypass estático | El propio SAI, ante sobrecarga o fallo del inversor | En milisegundos; la carga pasa a red sin protección |
| Inversor → bypass de mantenimiento | El técnico, con una secuencia escrita | Sin corte si se sigue la secuencia del fabricante |

La segunda es la que hay que vigilar: mientras un SAI está en bypass estático, la carga crítica
está en la red tal cual llega, y si la red falla en ese momento cae todo. Un SAI que se queda en
bypass es una incidencia (epígrafe 8), no un estado normal.

La tercera, la maniobra de sacar un SAI a mantenimiento, es una secuencia del fabricante que cambia
de un equipo a otro. Su lógica general (oficio): primero se pasa la carga al bypass estático desde
el propio equipo, y sólo entonces se cierra el bypass manual y se abren las salidas del equipo;
para volver, el orden inverso. Cerrar el bypass manual con el inversor en servicio y sin pasar
antes por el estático puede poner en paralelo el inversor y la red sin sincronismo.

## 5. Baterías

En este tema hay dos baterías distintas: la del SAI, que es la autonomía de la carga crítica, y la
de arranque del grupo, que es la que decide si el grupo arranca. La ITC-BT-28 admite las **Baterías
de acumuladores** como fuente para los servicios de seguridad, con la advertencia de que
**Generalmente las baterías de arranque de los vehículos no satisfacen las prescripciones de
alimentación para los servicios de seguridad** (apartado 2.1).

### 5.1 Pilas y baterías: la distinción y los parámetros

La distinción de partida, en una línea:

|  | Pila | Acumulador o batería |
|---|---|---|
| Reacción | Irreversible | Reversible |
| Se recarga | No | Sí |
| También se llama | Primaria | Secundaria |

Los parámetros que definen a una batería y que hay que saber nombrar:

| Parámetro | Qué es |
|---|---|
| Tensión nominal | La de referencia; la de un elemento depende de su química |
| Capacidad | La carga que puede entregar, en amperios hora, referida a un régimen de descarga |
| Energía | Capacidad por tensión, en vatios hora |
| Régimen de descarga | En cuánto tiempo se descarga: se escribe como una fracción de la capacidad |
| Profundidad de descarga | Qué porcentaje se le saca en cada ciclo |
| Número de ciclos | Cuántas cargas y descargas aguanta, y depende de la profundidad |
| Autodescarga | Lo que pierde estando parada |
| Corriente de cortocircuito | Enorme: es el dato de seguridad |

Y el aviso que hay que dar sobre la capacidad, porque es la cifra que más engaña: la capacidad de
una batería depende del régimen al que se le pida. La misma batería entrega bastante menos energía
si se descarga en diez minutos que si se descarga en diez horas. Una capacidad sin su régimen no
significa nada, y dimensionar la autonomía de un sistema de alimentación ininterrumpida con la
capacidad nominal en vez de con la del régimen real es el error de cálculo clásico.

Los regímenes de carga, que es lo que hace el cargador mientras no hay corte (oficio; las
tensiones y corrientes de cada uno son dato del fabricante de la batería y no se dan aquí):

| Régimen | Qué es | Cuándo |
|---|---|---|
| Carga | Reponer la energía sacada en una descarga, con la corriente limitada | Después de cada descarga, al volver la red o tomar carga el grupo |
| Flotación | Mantener la batería cargada a tensión constante, compensando sólo la autodescarga | El estado normal y permanente de la batería de un SAI en servicio |
| Igualación | Una carga a tensión algo mayor, de vez en cuando, para igualar el estado de los elementos | Sólo cuando el fabricante de la batería la prevé; no es un régimen permanente |

En el diagrama de bloques de 2.1, el cargador del SAI es su rectificador: con red o con grupo alimenta al inversor y, a la vez,
lleva la batería en carga o en flotación, controlando la tensión de carga y limitando la corriente.
El grupo tiene el suyo, independiente, que mantiene en flotación la batería de arranque mientras el
grupo está parado (5.2). De ahí que una tensión de flotación correcta diga que el cargador
funciona, pero no que la batería tenga capacidad (7.2).

### 5.2 Las químicas y su seguridad

Las químicas que un técnico encuentra:

| Química | Rasgos |
|---|---|
| Plomo-ácido abierta | Barata, robusta, muy usada en arranque; desprende hidrógeno y exige mantenimiento de nivel |
| Plomo-ácido regulada por válvula | Sin mantenimiento de nivel; la de los sistemas de alimentación ininterrumpida clásicos |
| Níquel-cadmio | Muy robusta a temperatura extrema y a descarga profunda; cara |
| Ion litio | Mucha más energía por kilo y por litro, más ciclos; exige sistema de gestión y tiene su propio régimen de seguridad |

Y el aviso de seguridad de las de plomo abierto: desprenden hidrógeno al cargar, y el hidrógeno es
explosivo. De ahí que el emplazamiento de las baterías tenga que estar ventilado —la ITC-BT-28
exige que **el emplazamiento estará convenientemente ventilado, de forma que los gases y los humos
que produzcan no puedan propagarse en los locales accesibles a las personas** para toda fuente de
seguridad de un local de pública concurrencia que no sea un equipo autónomo (3.2)— y de ahí que la instrucción de locales con riesgo de
incendio o explosión pueda alcanzarlo.

La batería de arranque del grupo es casi siempre de plomo-ácido (oficio) y vive en un sitio hostil:
junto a un motor que se calienta y vibra. Su cargador es un equipo más del grupo, y su fallo es la
primera causa de que un grupo no arranque (7.1).

### 5.3 La agrupación en serie y en paralelo

Una batería de SAI no es un elemento sino muchos agrupados, y son dos reglas simétricas:

| Agrupación | Cómo se conectan | Qué se suma | Qué se mantiene |
|---|---|---|---|
| Serie | El positivo de uno al negativo del siguiente | Las tensiones | La capacidad, en amperios hora |
| Paralelo | Todos los positivos juntos y todos los negativos juntos | Las capacidades | La tensión |
| Serie-paralelo o mixta | Ramas en serie, puestas en paralelo | Las dos cosas | — |

Y la regla que hay que enunciar y que resume las dos: en serie se suma lo que empuja; en paralelo
se suma lo que dura.

Las tres condiciones para agrupar bien:

1. Los elementos deben ser iguales: misma química, misma capacidad, misma tensión y, a ser
   posible, del mismo lote y la misma antigüedad.
2. En serie, la corriente es común a todos, así que el elemento más débil limita a toda la rama.
   Una cadena en serie vale lo que su peor elemento.
3. En paralelo, la tensión es común, así que un elemento en peor estado se convierte en una carga
   para los demás y circulan corrientes de igualación entre ramas.

La consecuencia práctica de las dos últimas, y es la que hay que saber decir: no se sustituye un
solo elemento de una batería envejecida. Un elemento nuevo en una cadena vieja no la arregla: se
degrada rápido igualándose con los demás. Lo que se sustituye es el conjunto.

Y la energía es lo único que se conserva en las dos agrupaciones: la energía total es siempre la
suma de las energías de los elementos, se conecten como se conecten. Lo que cambia es en qué forma
—más tensión o más corriente— se entrega.

Un ejemplo de cálculo, con cifras supuestas y no de norma: cuatro bloques de 12 V y 100 Ah en serie
dan 48 V y 100 Ah; dos ramas como ésa en paralelo dan 48 V y 200 Ah. La energía, en los dos casos,
es la suma de la de los bloques: 4 × 12 V × 100 Ah = 4.800 Wh, y 8 × 1.200 Wh = 9.600 Wh.

## 6. Autonomía

Autonomía es cuánto tiempo aguanta una fuente propia alimentando una carga dada. Sin la carga, la
cifra no dice nada: un SAI con «diez minutos de autonomía» los da a una carga concreta.

### 6.1 La autonomía del SAI

La observación que resume el tema: la autonomía de un sistema de alimentación ininterrumpida no se
dimensiona para aguantar el corte, se dimensiona para aguantar hasta que arranque el grupo. Pedirle
horas a una batería cuando hay un grupo detrás es pagar dos veces por lo mismo, y no pedirle nada
cuando no hay grupo es no tener nada. La cifra sale del escenario, y el escenario hay que
escribirlo (oficio).

| Decisión | Cómo se toma |
|---|---|
| Qué se protege | Sólo lo que no puede caerse ni un ciclo, y su refrigeración si va en el SAI (3.4) |
| Qué topología | Doble conversión para lo crítico; lo demás puede ir en espera |
| Cuánta autonomía | La que haga falta hasta que el grupo tome carga, más un margen; no más |
| Cómo se encadena con el grupo | El sistema cubre el arranque del grupo; el grupo recarga el sistema |

El margen no es caprichoso (oficio): tiene que cubrir un arranque fallido y el reintento (1.5,
fase 3) y, si el grupo no arranca, el tiempo de un apagado ordenado de los servidores.

El cálculo, en su forma más simple y con cifras supuestas: autonomía ≈ energía útil de la batería
÷ potencia activa de la carga. Una carga de 20 kW con una batería de 9,6 kWh daría, en el papel,
casi media hora; en la realidad bastante menos, por tres razones que se suman: a ese régimen de
descarga rápido la batería no entrega su capacidad nominal (5.1), el inversor tiene pérdidas y la
batería envejece y pierde capacidad. Por eso la autonomía real de un SAI se mide (7.2) y no se
calcula una vez para siempre. Las tablas de autonomía por carga son dato del fabricante.

### 6.2 La autonomía del grupo

La autonomía del grupo es la de su combustible. Se decide por el escenario, no por una cifra
redonda: cuántas horas hay que aguantar depende de si el corte previsible es de minutos o de horas,
y de en cuánto tiempo se puede traer combustible. Y el depósito no se rige sólo por el REBT: la ITC-BT-40 exige que los **depósitos de
combustibles** cumplan **además, las disposiciones que establecen los Reglamentos y Directivas
específicos que les sean aplicables** (1.3). Qué reglamento es ése y a partir de qué capacidad
alcanza al depósito no se da en este tema.

Lo que el oficial tiene que saber de la autonomía del grupo en la práctica: el nivel del depósito
diario y del nodriza es un dato de cada ronda; un grupo que se prueba a menudo y no se repone se
queda sin autonomía sin que nadie lo note; y el gasóleo almacenado mucho tiempo se degrada (7.1).

### 6.3 La autonomía que fija la norma

De las instrucciones del REBT leídas para este tema, sólo la ITC-BT-28 fija una autonomía, y es la
de los servicios de seguridad (la ITC-BT-38 fija otra, de dos horas, para el suministro especial
complementario que alimenta la lámpara de quirófano y los equipos de asistencia vital, que no es
caso de este puesto). La capacidad mínima de una
fuente propia es la del alumbrado de seguridad (3.2), y ese alumbrado, en sus dos modalidades
generales, **deberá poder funcionar, cuando se produzca el fallo de la alimentación normal, como
mínimo durante una hora, proporcionando la iluminancia prevista** (ITC-BT-28, apartado 3.1.1, para
el de evacuación; el 3.1.2 repite la hora para el ambiente o anti-pánico). Para las zonas de alto
riesgo, el tiempo es **como mínimo el tiempo necesario para abandonar la actividad o zona de alto
riesgo** (apartado 3.1.3). Las iluminancias y el resto del alumbrado de emergencia, en el tema 6.

Ninguna norma leída para este tema fija la autonomía de un SAI o de un grupo que alimentan cargas
de producción: es decisión del titular, a partir del escenario.

## 7. Pruebas periódicas

Una fuente de socorro sólo se usa el día que falla la red, y por eso es la instalación que más
fácilmente está estropeada sin que nadie lo sepa. La prueba periódica es la única forma de saberlo.

### 7.1 El grupo electrógeno

Lo que hay que hacer para que el grupo esté cuando haga falta:

| Tarea | Por qué |
|---|---|
| Nivel y estado del combustible | El gasóleo se degrada y cría microorganismos si está mucho tiempo parado |
| Nivel de refrigerante y de aceite | Lo evidente |
| Batería de arranque y su cargador | Es la causa número uno de que un grupo no arranque |
| Precalentamiento del motor | Facilita el arranque en frío |
| Prueba periódica de arranque | Que arranque |
| Prueba periódica con carga | Que aguante |
| Prueba de transferencia completa | Que la conmutación funcione |
| Estado de antivibratorios, manguitos y escape | Envejecen |

Una prueba de arranque en vacío no demuestra casi nada. Un grupo que arranca y gira sin carga no
prueba que el alternador regule, que la conmutación transfiera ni que la refrigeración baste. Y hay
más: hacer trabajar un motor diésel largo rato en vacío o a carga muy baja produce carbonilla y lo
estropea.

Lo que hay que probar, entonces, y con qué: la prueba correcta es con carga, y si la carga real no
se puede arriesgar, con un banco de cargas resistivo. Es la única forma de comprobar la potencia
sin apagar el edificio.

Y la prueba que nadie hace y que es la única que prueba lo importante: la de transferencia
completa, con la instalación real. Exige una ventana pactada y aceptar un riesgo controlado: una
redundancia que no se ha provocado nunca no se sabe si funciona. Cómo se pacta esa ventana con
producción y cómo se vuelve al servicio es materia del tema 17.

### 7.2 El SAI y sus baterías

| Tarea | Por qué |
|---|---|
| Inspección visual de la batería | Bornes, corrosión, deformación de vasos, fugas. Un vaso hinchado se cambia |
| Temperatura del local | Es lo que más acorta la vida de una batería de plomo |
| Apriete y estado de las conexiones | Un contacto flojo en continua arde igual que en alterna |
| Prueba de descarga | La única que dice la autonomía real |
| Registro de alarmas y del histórico | Lo que anticipa el fallo |
| Limpieza de filtros y ventiladores | La refrigeración del equipo |
| Prueba del bypass | De los dos, y la del manual con procedimiento escrito |

La segunda fila merece explicación porque es contraintuitiva: la vida de una batería de plomo se
acorta drásticamente con la temperatura. Una sala de baterías caliente consume la vida útil mucho
antes de lo previsto, y la instalación no da ninguna señal hasta el día en que hace falta.
Refrigerar la sala de baterías no es confort: es alargar la vida del sistema.

Y la cuarta es la única prueba que vale: una batería que muestra su tensión correcta en flotación
puede no tener capacidad ninguna. La tensión en reposo no mide la capacidad. Lo único que la mide
es una descarga controlada, y por eso los sistemas críticos se prueban con carga real o con banco
de cargas. Es el mismo argumento que la prueba con carga del grupo.

### 7.3 Lo que fija la norma

Ninguna de las normas leídas para este tema fija una periodicidad de prueba para el grupo o el SAI
de un edificio de oficinas y producción. Lo que sí dice el REBT, para las fuentes de los servicios
de seguridad de un local de pública concurrencia, es que **Los equipos y materiales deberán disponerse de forma que se facilite su
verificación periódica, ensayos y mantenimiento** (ITC-BT-28, apartado 2.1). La periodicidad,
fuera de los casos siguientes, la fija el plan de mantenimiento del titular a partir de lo que diga
el fabricante (las gamas y el plan de mantenimiento, en el tema 13).

Donde sí hay periodicidad es en las fuentes de alimentación de la protección contra incendios. El
anexo II del RIPCI establece que **Los equipos y sistemas de protección activa contra incendios, se
someterán al programa de mantenimiento establecido por el fabricante. Como mínimo, se realizarán las
operaciones que se establecen en las tablas I y II.** En la tabla I (programa trimestral y
semestral, que puede hacer el personal especializado del fabricante o de una empresa mantenedora
o, también, **el personal del usuario o titular de la instalación**), para los
sistemas de detección y alarma, figuran cada tres meses:

- en «Fuentes de alimentación»: **Revisión de sistemas de baterías: Prueba de conmutación del
  sistema en fallo de red, funcionamiento del sistema bajo baterías, detección de avería y
  restitución a modo normal.**
- en «Requisitos generales»: **Comprobación de funcionamiento de las instalaciones (con cada fuente
  de suministro).** y **Mantenimiento de acumuladores (limpieza de bornas, reposición de agua
  destilada, etc.).**

Y para los sistemas de abastecimiento de agua contra incendios, la misma tabla incluye
**Mantenimiento de acumuladores, limpieza de bornas (reposición de agua destilada, etc.).
Verificación de niveles (combustible, agua, aceite, etc.).** y **Comprobación de la alimentación
eléctrica, líneas y protecciones.** El resto del mantenimiento y la inspección de la protección
contra incendios, en el tema 11.

La prueba de la fila de baterías del RIPCI es, en pequeño, la misma secuencia que la de un SAI:
fallo de red, funcionamiento con batería, detección de la avería y vuelta a normal.

## 8. Actuación ante incidencias

Este epígrafe es oficio: ninguna norma leída para el tema fija cómo se actúa ante una avería de un
grupo o de un SAI, y los procedimientos concretos son los del fabricante de cada equipo y los que
tenga escritos el titular. Lo que sigue es el razonamiento de oficio, ordenado por incidencias.

### 8.1 El orden de prioridades

Ante cualquier incidencia de alimentación, el orden es siempre el mismo:

1. Primero, que la carga crítica siga alimentada: antes de reparar nada, se comprueba de qué
   fuente está colgando ahora mismo (red, grupo, inversor, bypass) y cuánto tiempo le queda.
2. Después, avisar: a quien tenga a su cargo la emisión o la producción afectada, porque una
   incidencia en la alimentación es una incidencia de servicio, y a quien coordine el
   mantenimiento. Cómo se comunica una incidencia y cómo se vuelve al servicio, en el tema 17.
3. Después, diagnosticar, con el registro de alarmas del cuadro del grupo o del SAI, que dice qué
   pasó y en qué orden.
4. Y sólo al final, reparar, con la instalación en condiciones de seguridad (tema 15).

### 8.2 Incidencias del grupo electrógeno

| Incidencia | Causa probable | Qué se hace |
|---|---|---|
| Falla la red y el grupo no arranca | Batería de arranque o su cargador; falta de combustible; parada de emergencia enclavada; cuadro en modo manual o bloqueado | Comprobar la batería y el modo del cuadro; arranque manual si el procedimiento lo prevé; vigilar la autonomía que le queda al SAI |
| Arranca pero no toma carga | Tensión o frecuencia fuera de límites (reguladores); interruptor de grupo que no cierra; enclavamiento | Leer el cuadro de control: qué protección o qué condición impide el cierre |
| Toma carga y se para | Sobrecarga o escalón excesivo; disparo por temperatura (ventilación insuficiente o radiador obstruido); presión de aceite; combustible | Deslastrar cargas no esenciales; comprobar ventilación y niveles |
| Frecuencia inestable | Regulador de velocidad desajustado; escalones de carga grandes | Repartir la carga en escalones; revisión del regulador |
| Vuelve la red con microcortes | Red inestable | No forzar la retransferencia: dejar que el automatismo confirme la red (1.5, fase 7) |
| Combustible bajo durante un corte largo | Autonomía agotándose | Pedir suministro con tiempo; deslastrar para alargar; preparar el apagado ordenado de lo crítico |

### 8.3 Incidencias del SAI

| Incidencia | Qué significa | Qué se hace |
|---|---|---|
| SAI en bypass estático | La carga está en red sin protección: el inversor ha fallado o hay sobrecarga | Comprobar la carga conectada; no dejarlo así; avisar al servicio técnico si no vuelve a inversor |
| Alarma de batería | Batería degradada, temperatura alta o fallo de una cadena | Comprobar temperatura del local y conexiones; programar prueba de descarga o sustitución del conjunto (5.3) |
| SAI funcionando con batería | Falta la red o el rectificador no la acepta | Comprobar si el grupo ha tomado carga; si no, calcular el tiempo que queda (6.1) |
| Cae toda la carga del SAI por un cortocircuito en un circuito | El inversor limita la corriente y el magnetotérmico del circuito no ha disparado (2.4) | Localizar y aislar el circuito averiado; revisar la selectividad aguas abajo |
| Sobrecarga | Se ha conectado más carga de la prevista | Retirar lo que no debe estar en el SAI; revisar qué cuelga de él (3.4) |
| Sobrecalentamiento del equipo | Filtros sucios, ventiladores o climatización de la sala | Limpieza; climatización; la sala técnica sin frío es una incidencia en sí misma |

La lección de la cuarta fila es la más útil en la práctica: si un cortocircuito en un
solo circuito apaga todo lo que cuelga de un SAI, el fallo no está en el SAI sino en cómo se eligió
la protección de ese circuito para la corriente que el inversor puede dar.

### 8.4 La seguridad al intervenir en baterías

Una batería no tiene interruptor. No se puede «dejar sin tensión» un conjunto de baterías, y su
corriente de cortocircuito es enorme. Trabajar en ellas exige herramienta aislada, retirar anillos y
relojes, protección facial y, en las de plomo abierto, protección frente al electrolito. Un
destornillador que cruza dos bornes de una batería grande se funde.

Y dos avisos más del mismo oficio. En un grupo con arranque automático, el motor puede ponerse en
marcha solo en cualquier momento si falla la red, así que antes de trabajar en él se bloquea el
arranque según su procedimiento (la consignación y las cinco reglas de oro, en el tema 15). En un
SAI, abrir la entrada de red no deja la salida sin tensión: el inversor sigue dando alterna desde la
batería, y el bypass puede traer la red por otro camino.

## Normativa que el tema invoca

- Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para
  baja tensión: artículo 10 del Reglamento (tipos de suministro y dispositivos que impiden el acoplamiento);
  ITC-BT-28, apartados 1, 2, 2.1, 2.2,
  2.3, 3, 3.1.1 a 3.1.3 y 4.g (servicios de seguridad, fuentes propias, categorías de conmutación,
  autonomía del alumbrado de seguridad); ITC-BT-38, apartado 2.2 (sólo para decir que fija otra autonomía); ITC-BT-40, apartados 1, 2, 3, 4.1, 4.2, 5, 6, 7, 8.2.1,
  8.2.2 y 9 (instalaciones generadoras), en la redacción dada por el Real Decreto 244/2019, de 5 de
  abril.
- Real Decreto 513/2017, de 22 de mayo, por el que se aprueba el Reglamento de instalaciones de
  protección contra incendios: anexo II, apartado 1 y tabla I.
- IEC 62040-3 (clasificación de los SAI): sólo a través de una fuente secundaria; no leída.

## Lo que este tema no da, y dónde está

- Las potencias, los coeficientes de corrección por altitud y temperatura, los escalones de carga
  admisibles, los niveles de ruido, las tensiones de elemento y de flotación, las tensiones y
  corrientes de carga y de igualación, los coeficientes de sobredimensionado de un grupo que
  alimenta un SAI, los números de ciclos,
  las temperaturas de referencia de las baterías y los rendimientos de los SAI: son dato de
  fabricante y de norma de producto, y no se ha leído ninguna. Lo que el tema da es el sentido en
  que influye cada variable; las cifras de los ejemplos de 5.3 y 6.1 son supuestas.
- La norma internacional que define los regímenes de servicio de un grupo (emergencia, principal,
  continuo): no se ha consultado, y por eso no se dan sus siglas ni sus porcentajes.
- El texto de la IEC 62040-3 y su edición vigente o su transposición UNE: no leídos. Las clases
  VFD, VI y VFI van con la descripción de la primera edición hecha por W. Sölter; los tiempos de
  conmutación que da ese autor no se recogen como dato de norma.
- Una periodicidad reglamentaria de prueba de los grupos y SAI de un edificio no sanitario: no se
  ha encontrado en el REBT. Fuera de las fuentes de alimentación de la protección contra
  incendios (RIPCI), la periodicidad es del plan de mantenimiento.
- El reglamento de instalaciones petrolíferas aplicable al depósito de combustible del grupo, y sus
  umbrales de capacidad: no consultados.
- La ventilación de las salas de baterías por norma de producto y el reglamento europeo de baterías:
  no consultados. La seguridad propia del ion litio y del almacenamiento de energía, tampoco; el
  tema sólo dice que esa química exige sistema de gestión.
- La instrucción de locales con riesgo de incendio o explosión se nombra por lo que regula: puede
  alcanzar a un local de baterías, sin que el tema diga cuándo.
- El alumbrado de emergencia (iluminancias, lugares, aparatos): tema 6. La aparamenta, el
  enclavamiento y la selectividad: tema 3. Los esquemas de conexión a tierra: tema 5. La redundancia
  de CPD, centros emisores y UM, y la compatibilidad electromagnética: tema 8. La protección contra
  incendios: tema 11. Las gamas y el plan de mantenimiento: tema 13. La consignación y los trabajos
  en tensión: tema 15. La planificación de intervenciones y el retorno al servicio: tema 17. Las
  baterías como almacenamiento y el autoconsumo: tema 18.
- Los grupos, SAI y procedimientos de la RTVA y de CSRTV (qué equipos tiene, qué alimentan, qué
  autonomía tienen y cómo se actúa ante una incidencia): no constan en ningún documento publicado.

## Trazabilidad

| Fuente | Qué se ha tomado | Leída |
|---|---|---|
| Real Decreto 842/2002 (BOE-A-2002-18099), Reglamento, artículo 10, redacción única (vigente desde el 18/09/2003) | Suministros normales y complementarios; socorro, reserva y duplicado; 10.2 (dispositivos que impiden el acoplamiento); 10.3 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-28, redacción única (vigente desde el 18/09/2003) | Apartado 1 (campo de aplicación: locales de pública concurrencia); apartado 2 (servicios de seguridad, alimentación automática o no automática, cinco categorías de conmutación); 2.1 (fuentes y sus condiciones); 2.2 (fuente propia, 70 %, capacidad mínima); 2.3 (socorro y reserva); 3 (corte breve del alumbrado de emergencia); 3.1.1 a 3.1.3 (autonomía); 4.g (tensión de retorno) | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-38, redacción única (vigente desde el 18/09/2003) | Apartado 2.2: el suministro especial complementario de la lámpara de quirófano y los equipos de asistencia vital, con autonomía no inferior a 2 horas | En el BOE consolidado, 05/10/2026 |
| Real Decreto 842/2002, ITC-BT-40, redacción vigente desde el 07/04/2019 (Real Decreto 244/2019, BOE-A-2019-5089) | Apartados 1, 2, 3, 4.1, 4.2, 5, 6, 7, 8.2.1, 8.2.2 y 9 | En el BOE consolidado, 05/10/2026 |
| Real Decreto 513/2017 (BOE-A-2017-6606), anexo II, redacción vigente desde el 10/05/2025 (BOE-A-2025-7190) | Apartado 1; tabla I, filas de detección y alarma (requisitos generales y fuentes de alimentación) y de abastecimiento de agua | En el BOE consolidado, 05/10/2026 |
| W. Sölter (AEG SVS Power Supply Systems), «A new International UPS Classification by IEC 62040-3», sobre la 1.ª edición de la norma (1999) | Los tres pasos del código; definiciones de VFD, VI y VFI; la triple clase 1 sólo en VFI | 05/10/2026 |

El resto va como oficio y así se declara: la distinción entre autonomía y continuidad; las partes
del grupo y la separación entre el regulador de velocidad y el de excitación; la regla de que la
misma máquina declara más potencia cuanto menos trabaja; el aviso sobre dimensionar en kilovatios
con un factor de potencia peor; el escalón de carga y la caída de frecuencia; los tres aires del
grupo, el escape y las tres vías del ruido; la lectura de los relés de la ITC-BT-40 desde el
mantenimiento; la secuencia de nueve fases; el diagrama de bloques del SAI, sus dos bypass, sus
topologías y la razón de que sólo la doble conversión sea «sin corte»; el modo de alta eficiencia;
la corriente de cortocircuito del inversor y la selectividad; la asignación de categorías de
conmutación a cada fuente; qué cuelga del grupo y del SAI y la cadena completa; el enclavamiento
mecánico; el sentido de la transferencia sin corte y de la puesta a tierra del neutro del grupo;
la maniobra del bypass de mantenimiento; pilas y baterías, sus parámetros, químicas y agrupación; los regímenes de carga y qué hace cada cargador; el sobredimensionado del grupo que
alimenta un SAI; el cálculo de autonomía; las pruebas del grupo y del SAI; y toda la actuación ante incidencias. Nada de
eso se ha leído en una norma, y el tema no lo presenta como si lo estuviera.
