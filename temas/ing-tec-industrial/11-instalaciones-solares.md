# Tema 11 del específico de Ingeniería Técnica · Industrial · Instalaciones solares térmicas y fotovoltaicas

Las siglas de este tema, presentadas de entrada: el kilovatio (**kW**); el kilovoltio (**kV**); el
Código Técnico de la Edificación (**CTE**), del tema 3, con sus exigencias básicas de ahorro de
energía cuarta y quinta (**HE 4** y **HE 5**); el Reglamento de Instalaciones Térmicas en los
Edificios (**RITE**), del tema 1; el reglamento electrotécnico para baja tensión (**REBT**), del tema
7; el precio voluntario para el pequeño consumidor (**PVPC**); y los tres términos horarios que el
mecanismo de compensación usa —el coste horario de energía (**TCUh**), el precio medio horario
(**Pmh**) y el coste de los desvíos (**CDSVh**)—.

> Enunciado de la convocatoria (Anexo 2, temario específico de Ingeniería Técnica · especialidad
> Industrial, punto 11):
> «Instalaciones solares térmicas y fotovoltaicas. Cálculo, diseño, mantenimiento y normativa.
> 11.1. Real Decreto 1699/2011, de 18 de noviembre, por el que se regula la conexión a red de
> instalaciones de producción de energía eléctrica de pequeña potencia (BOE núm. 295, de 8 de diciembre
> de 2011. Texto consolidado: Última actualización publicada el 19/10/2022).
> 11.2. Real Decreto 244/2019, de 5 de abril, por el que se regulan las condiciones administrativas,
> técnicas y económicas del autoconsumo de energía eléctrica (BOE núm. 83, de 6 de abril de 2019. Hasta
> la modificación de 19/10/2022 inclusive).»

**Aquí hay un desajuste declarado entre el enunciado y sus normas, y hay que decirlo el primero**:
**el punto se titula «instalaciones solares TÉRMICAS y fotovoltaicas», y las dos normas que nombra
son ELÉCTRICAS.** **Ninguna de las dos dice una palabra de un captador solar térmico.**

**Dónde está entonces lo térmico**: **en el RITE del tema 1** —que fija la documentación técnica y la
regla de los 0,7 kilovatios por metro cuadrado de campo de captadores— **y en la exigencia básica
HE 4 del Código Técnico del tema 3**, que **obliga a cubrir con renovables la demanda de agua caliente
sanitaria.** **Este tema lo declara y remite, en vez de inventarse una norma que el enunciado no
nombra.**

**Y lo fotovoltaico es lo que sí desarrollan las dos normas del punto**, cada una con su papel:

| Norma | Qué resuelve |
|---|---|
| **Real Decreto 1699/2011** | **CÓMO se conecta a la red una instalación de producción de pequeña potencia** |
| **Real Decreto 244/2019** | **QUÉ RÉGIMEN tiene el autoconsumo**: modalidades, requisitos, medida, compensación |

<!-- indice -->

## Índice

- [1. Lo térmico, y por qué no está aquí](#1-lo-térmico-y-por-qué-no-está-aquí)
- [2. La conexión de la pequeña potencia](#2-la-conexión-de-la-pequeña-potencia)
- [3. Las modalidades de autoconsumo](#3-las-modalidades-de-autoconsumo)
- [4. Individual y colectivo](#4-individual-y-colectivo)
- [5. Los requisitos generales y la responsabilidad](#5-los-requisitos-generales-y-la-responsabilidad)
- [6. El mecanismo de compensación simplificada](#6-el-mecanismo-de-compensación-simplificada)
- [7. Lo que este punto resuelve en una casa que emite](#7-lo-que-este-punto-resuelve-en-una-casa-que-emite)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Lo térmico, y por qué no está aquí

| Pregunta sobre solar térmica | Dónde está la respuesta |
|---|---|
| **Si hace falta proyecto o memoria técnica** | **Artículo 15.3 del RITE**: la que corresponda a la potencia del equipo de **apoyo**; si no lo hay, **superficie de apertura de captadores × 0,7 kW/m²** |
| **Quién la mantiene y con qué contrato** | **Artículo 26.6 y 26.7 del RITE**, con el mismo criterio de potencia |
| **Cuánta renovable hay que poner para el agua caliente** | **Exigencia básica HE 4 del Código Técnico** |
| **Cuánta electricidad renovable hay que generar** | **Exigencia básica HE 5 del Código Técnico** |

**Las cuatro respuestas están en dos normas que el enunciado de este punto NO nombra**, y **las dos
están desarrolladas en los temas 1 y 3 de este mismo específico.** **Ésa es la razón de que este tema
no las repita.**

**Y la observación de método que el desajuste deja**: **un anexo puede titular un punto con dos
materias y darle normas de una sola.** **Lo que hay que hacer es cubrir el título, no la lista**, y
**decir de dónde sale cada mitad.**

## 2. La conexión de la pequeña potencia

**Artículo 1** del Real Decreto 1699/2011, entero:

> «**Constituye el objeto de este real decreto el establecimiento de las condiciones administrativas,
> contractuales, económicas y técnicas básicas para la conexión a las redes de distribución de energía
> eléctrica de las instalaciones de producción de energía eléctrica incluidas en el ámbito del presente
> real decreto.**»
>
> — Real Decreto 1699/2011, artículo 1 (`BOE-A-2011-19242`), redacción vigente el 21 de diciembre de
> 2022.

---

**Cuatro adjetivos —administrativas, contractuales, económicas y técnicas— y una sola red: la de
DISTRIBUCIÓN.** **Lo que se conecta a transporte no va por aquí.**

**El ámbito, del artículo 2**, en dos escalones que se distinguen por potencia Y por tensión:

| Escalón | Potencia | Dónde se conecta |
|---|---|---|
| **Primero** | **No superior a 100 kW** | **A líneas de tensión no superior a 1 kV** de la distribuidora, directamente o a través de la red interior de un consumidor; **o al lado de baja de un transformador de red interior**, si la potencia de generación en esa red interior no pasa de 100 kW |
| **Segundo** | **No superior a 1.000 kW** | **A líneas de tensión no superior a 36 kV** de la distribuidora, directamente o por red interior |

**Las cuatro cifras son 100, 1, 1.000 y 36**, y **van emparejadas dos a dos**: **cien kilovatios con un
kilovoltio, y mil kilovatios con treinta y seis.** **Así se recuerdan sin confundirlas.**

**Y la regla antifraccionamiento del apartado 4, que es la que cierra la puerta a trocear una planta
grande en muchas pequeñas:**

| Caso | Qué ocurre |
|---|---|
| **Agrupaciones que comparten líneas o infraestructuras de evacuación** | **Quedan EXCLUIDAS cuando la suma de las potencias unitarias supere los valores anteriores** |
| **Instalaciones de igual tecnología en la misma REFERENCIA CATASTRAL**, identificada por sus primeros catorce dígitos | **Lo mismo** |

**Los catorce dígitos de referencia catastral son el dato más concreto del artículo**, y **su función
es impedir que catorce instalaciones de cien kilovatios en la misma finca se traten como catorce
pequeñas.**

**Y cuándo se entiende que varias instalaciones comparten evacuación, del apartado 3**: **entre otros
casos, cuando se conecten a un mismo centro de transformación o subestación a través de líneas de las
que NO sea titular la empresa distribuidora o transportista.**

## 3. Las modalidades de autoconsumo

**Ésta es la tabla que ordena el punto entero**, del artículo 4 del Real Decreto 244/2019, y **hay que
saberla con sus nombres exactos:**

| Modalidad | Qué la define | Cuántos sujetos hay |
|---|---|---|
| **Sin excedentes** | **Se instala un **mecanismo antivertido** que impide inyectar energía excedentaria a la red** | **Uno: el consumidor** |
| **Con excedentes** | **La instalación puede, además de autoconsumir, **inyectar** excedentes en las redes** | **Dos: el consumidor y el productor** |
| **Con excedentes acogida a compensación** | **Consumidor y productor optan voluntariamente por el mecanismo de compensación** | **Dos** |
| **Con excedentes no acogida a compensación** | **No cumple algún requisito, o no quiere acogerse** | **Dos** |

**La primera partición es técnica —hay antivertido o no lo hay—; la segunda es voluntaria.** **Y de
ahí sale que sólo haya un sujeto en la primera modalidad**: **si no se vierte, no hay producción que
vender.**

**Las CINCO condiciones para acogerse a compensación, del artículo 4.2.a)**, que son acumulativas y
las cinco se preguntan:

1. **La fuente de energía primaria sea de origen **renovable**.**
2. **La potencia total de las instalaciones de producción asociadas no sea superior a 100 kW.**
3. **Si hace falta contrato de suministro para servicios auxiliares de producción, el consumidor haya
   suscrito UN ÚNICO contrato con una comercializadora** para el consumo asociado y los auxiliares.
4. **Consumidor y productor hayan suscrito el **contrato de compensación** de excedentes del artículo
   14.**
5. **La instalación de producción no tenga otorgado un régimen retributivo adicional o específico.**

**Los 100 kilovatios de la segunda coinciden con el primer escalón del reglamento de conexión del
epígrafe anterior**, y **esa coincidencia no es casual: las dos normas dibujan el mismo tamaño de
instalación.**

**Y la quinta condición es la que un ingeniero olvida**: **no se puede cobrar dos veces.** **Quien
tiene régimen retributivo específico está fuera de la compensación.**

## 4. Individual y colectivo

**El artículo 4.3 añade una segunda clasificación que se cruza con la anterior**: **individual o
colectivo, según haya uno o varios consumidores asociados a la instalación de generación.**

**Las tres obligaciones del autoconsumo colectivo**, que son lo más preguntable del artículo:

| Obligación | Qué exige |
|---|---|
| **Misma modalidad** | **Todos los consumidores asociados a la misma instalación deben pertenecer a la **misma** modalidad de autoconsumo** |
| **Acuerdo de reparto** | **Comunicar de forma **individual** a la distribuidora —directamente o por la comercializadora— **un mismo** acuerdo firmado por todos** con los criterios de reparto del anexo I |
| **Cambio simultáneo** | **Si se cambia de modalidad, el cambio lo hacen **todos** a la vez** |

**La segunda tiene una asimetría que se pregunta**: **la comunicación es individual y el acuerdo es
único.** **Cada uno lo dice por su cuenta, pero todos dicen lo mismo.**

**Y las tres reglas del artículo 4.5, que cierran los casos raros:**

1. **Un sujeto consumidor no puede estar asociado simultáneamente a más de una modalidad.**
2. **Si el autoconsumo se hace por instalaciones próximas **a través de la red**, tiene que ser **con
   excedentes.** **La proximidad a través de la red excluye el antivertido.**
3. **Para el autoconsumo colectivo puede constituirse una **comunidad de energías renovables**, que
   puede actuar como representante de los consumidores si éstos la autorizan.

**Y el ámbito del real decreto, del artículo 2**, con su exclusión más práctica:

| Situación | ¿Entra? |
|---|---|
| **Instalaciones y sujetos de cualquier modalidad de autoconsumo conectados a transporte o distribución** | **Sí** |
| **Instalaciones AISLADAS** | **No** |
| **Grupos de generación usados EXCLUSIVAMENTE en caso de interrupción del suministro** | **No** |

**La segunda exclusión es la que interesa a una casa que emite**: **un grupo electrógeno de emergencia
NO es autoconsumo**, y **no se rige por este real decreto**, siempre que se use exclusivamente ante
una interrupción.

## 5. Los requisitos generales y la responsabilidad

**El artículo 5 reparte la responsabilidad, y ése es su asunto de fondo.** **Lo que hay que saber:**

| Regla | Qué dice |
|---|---|
| **Titularidades separadas** | **El consumidor y el propietario de la instalación de generación pueden ser personas distintas**, en cualquier modalidad |
| **Sin excedentes** | **El titular del punto de suministro es el consumidor**, que también lo es de la generación conectada a su red |
| **Sin excedentes COLECTIVO** | **La titularidad de la generación y del antivertido es compartida SOLIDARIAMENTE por todos los consumidores asociados** |
| **Con excedentes que comparten conexión** | **Consumidores y productores responden solidariamente del incumplimiento** |
| **Servicios auxiliares** | **Los titulares de instalaciones de producción próximas son considerados consumidores exclusivamente por los consumos de sus servicios auxiliares** |

**La solidaridad es la palabra que gobierna el artículo**, y **la consecuencia que el propio artículo
detalla es dura**: **la desconexión del punto puede suponer la imposibilidad del productor de vender
energía y percibir su retribución, y la del consumidor de adquirirla.** **Y eso debe recogerse
expresamente en el contrato de acceso.**

**Cuándo puede cortarse el suministro, del apartado 6**: **cuando por incumplimiento de requisitos
técnicos existan instalaciones peligrosas**, o **cuando se haya **manipulado** el equipo de medida o el
mecanismo antivertido.**

**Y el almacenamiento, del apartado 7**, que este real decreto autoriza expresamente:

| Condición | Qué exige |
|---|---|
| **Protecciones** | **Las de la normativa de seguridad y calidad industrial aplicable** |
| **Ubicación** | **Instalados de forma que **compartan** el equipo de medida de generación neta, el del punto frontera o el del consumidor asociado** |

**La condición de ubicación es la que evita el fraude**: **una batería tiene que estar dentro del
perímetro que ya se mide**, no colgada de un punto sin contador.

**La calidad de servicio, del artículo 6**, con la exención que hay que conocer: **la distribuidora no
tiene obligación legal de calidad de servicio por las incidencias derivadas de fallos en las
instalaciones de **conexión compartidas** por productor y consumidor.** **Y tampoco tiene obligación
sobre las instalaciones de conexión que no sean de su titularidad** —artículo 5.1—.

## 6. El mecanismo de compensación simplificada

**El artículo 14 es el corazón económico del real decreto**, y **lo primero que hay que decir es lo
que NO es**: **no es una venta de energía y no es un balance de kilovatios hora.**

**Qué es, del apartado 3**: **un saldo en términos económicos de la energía consumida en el periodo de
facturación.** **Se compensan euros, no energía.**

**Cómo se valora cada término, según el contrato que se tenga:**

| Contrato | Energía consumida de la red | Energía excedentaria |
|---|---|---|
| **Con comercializadora libre** | **Al precio horario acordado entre las partes** | **Al precio horario acordado entre las partes** |
| **Al precio voluntario para el pequeño consumidor** | **Al coste horario de energía de ese precio en cada hora** | **Al precio medio horario del mercado diario e intradiario **menos** el coste de los desvíos** |

**Y los dos límites que hacen que esto sea compensación y no venta**, del mismo apartado 3:

1. **El valor económico de la energía excedentaria **nunca** puede ser superior al de la energía consumida
   de la red en el periodo de facturación.** **La factura puede llegar a cero, no a negativo.**
2. **El periodo de facturación no puede ser superior a un mes.**

**Y la incompatibilidad**: **quien se acoge a este mecanismo no puede participar de otro mecanismo de
venta de energía.**

**Qué ocurre con los peajes, del apartado 4**: **la energía excedentaria de los acogidos a compensación
no tiene consideración de energía incorporada al sistema**, y **por tanto está exenta de los peajes de
acceso de productores**, **si bien el comercializador es el responsable de balance de esa energía.**

**El caso del autoconsumo colectivo **sin** excedentes, del apartado 2**, que es el que más confunde:
**también puede acogerse voluntariamente a compensación**, y **entonces **no** hace falta contrato de
compensación de excedentes** —porque no hay productor—: **basta un acuerdo entre todos los
consumidores** con los criterios de reparto.

**Qué hay que remitir y a quién, del apartado 5**: **el mismo contrato o acuerdo, firmado por todos los
participantes, se remite a la empresa distribuidora directamente o a través de la comercializadora**,
solicitando su aplicación.

## 7. Lo que este punto resuelve en una casa que emite

**Las tres decisiones que un ingeniero técnico industrial de una corporación audiovisual toma con este
punto delante:**

| Decisión | Qué la gobierna |
|---|---|
| **Poner fotovoltaica en la cubierta de un centro de trabajo** | **Modalidad con excedentes**, salvo que se instale antivertido. **Si la potencia pasa de 100 kW, fuera de compensación** |
| **Cubrir el agua caliente sanitaria con solar térmica** | **La exigencia básica HE 4 del Código Técnico y el RITE**, no las normas de este punto |
| **Tener grupo electrógeno de emergencia** | **no es autoconsumo**: queda excluido por el artículo 2.2, y se rige por el reglamento eléctrico del tema 7 y por el de instalaciones petrolíferas del tema 4 por su depósito |

**Y la observación de escala que conviene tener hecha**: **un centro de producción audiovisual con
platós supera con holgura los 100 kilovatios de generación en cuanto se cubre una nave.** **Eso lo
saca del mecanismo de compensación simplificada y del reglamento de pequeña potencia**, y **lo lleva
al régimen general de producción.** **La cifra de 100 kilovatios es, por tanto, la primera que hay que
mirar en un anteproyecto.**

**La tercera decisión merece una línea más**: **el grupo de emergencia está excluido SÓLO si se usa
exclusivamente ante una interrupción.** **En cuanto se arranque para recortar punta de consumo o para
vender, deja de estar excluido y pasa a ser autoconsumo con todo su régimen.** **El uso decide el
régimen, no el aparato.**

## 8. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 1699/2011, de 18 de noviembre, por el que se regula la conexión a red de instalaciones de producción de energía eléctrica de pequeña potencia** (`BOE-A-2011-19242`), **en su redacción vigente el 21 de diciembre de 2022** | **El artículo 1 entero**, citado literalmente |
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 244/2019, de 5 de abril, por el que se regulan las condiciones administrativas, técnicas y económicas del autoconsumo de energía eléctrica** (`BOE-A-2019-5089`), **en su redacción vigente el 21 de diciembre de 2022** | **Ninguna cita literal**: su contenido se resume, y sus artículos van identificados |

**Cinco declaraciones expresas:**

1. **Este punto del anexo titula «solares térmicas y fotovoltaicas» y sus dos normas son
   eléctricas.** **El temario cubre la mitad térmica REMITIENDO a los artículos del RITE y a las
   exigencias básicas del Código Técnico que los temas 1 y 3 de este mismo específico identifican**,
   y **no inventa una norma que el enunciado no nombra.** **Ninguna norma de solar térmica se ha
   consultado para este tema.**
2. **Los anexos de los dos reales decretos no se citan ni se reproducen.** **El anexo I del de
   autoconsumo —criterios de reparto— se nombra por lo que contiene**, que es lo que el artículo 4.3
   dice de él.
3. **Los artículos que se resumen en tabla y no se citan van identificados uno a uno** —del de
   conexión, el 2; del de autoconsumo, el 1, el 2, el 4, el 5, el 6 y el 14—. **Todos están en las
   normas citadas arriba.**
4. **Las normas que estas dos invocan se nombran y no se han consultado**: **la Ley 24/2013 del Sector
   Eléctrico** —sus artículos 6, 9, 24.4 y 25.4—, **el Real Decreto 1955/2000** —sus artículos 87 y
   100—, **el Real Decreto 661/2007** —su artículo 2 y sus categorías—, **el Real Decreto 216/2014**
   —sus artículos 7, 10 y 11—, **el Real Decreto 1544/2011** y **el Real Decreto 897/2017.** **El
   temario sólo afirma de ellas lo que los artículos citados dicen.**
5. **Las cifras económicas del epígrafe 6 son las que el artículo 14 nombra por su definición, no por
   su valor**: **el temario no da ningún precio ni ningún peaje**, y **no se ha consultado ninguna
   orden de precios.**

**El resto del tema va como oficio y así se declara**: el desajuste entre el título del punto y sus
normas y la manera de cubrirlo, la observación de que un anexo puede titular con dos materias y dar
normas de una, el emparejamiento dos a dos de las cuatro cifras del ámbito de conexión, la lectura de
los catorce dígitos de referencia catastral como regla antifraccionamiento, la explicación de por qué
la modalidad sin excedentes tiene un solo sujeto, la nota sobre la coincidencia de los 100 kilovatios
en las dos normas, la observación de que no se puede cobrar dos veces, la asimetría entre comunicación
individual y acuerdo único, la lectura de la condición de ubicación del almacenamiento como regla
antifraude, el subrayado de que se compensan euros y no energía, la lectura de que la factura puede
llegar a cero y no a negativo, las tres decisiones del epígrafe 7 y la advertencia de que el uso decide
el régimen del grupo de emergencia. **Nada de eso lo dicen las normas con esas palabras**, y el tema no
lo presenta como si lo dijeran.
