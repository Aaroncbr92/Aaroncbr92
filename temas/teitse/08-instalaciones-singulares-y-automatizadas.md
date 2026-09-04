# Tema 8 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Instalaciones singulares y automatizadas en edificios e industrias

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Téc. Equipos, Instalaciones y Sistemas Eléctricos · punto 8 |
| **Sirve para** | **Téc. Equipos, Instalaciones y Sistemas Eléctricos** |
| **Fuente** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** |
| **Identificador** | `BOE-A-2002-18099` · BOE núm. 224, de 18/09/2002 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. Se citan **la regla de cálculo de la ocupación del apartado 1 de la ITC-BT-28** y **la clasificación por duración de conmutación de su apartado 2** |
| **Aviso de estudio** | **El enunciado junta dos mitades desiguales**: las singulares están en las instrucciones particulares; **las automatizadas, casi en ninguna norma**, y van como oficio declarado |
| **Extensión** | **2.745 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el reglamento electrotécnico para baja tensión
(**REBT**) y sus instrucciones (**ITC-BT-27** a **ITC-BT-39**, **ITC-BT-51**); el sistema de gestión
técnica de edificios, por su nombre inglés (**BMS**, *building management system*); el autómata
programable (**PLC**, *programmable logic controller*); el control de supervisión y adquisición de
datos (**SCADA**); el grado de protección (**IP**); el metro cuadrado (**m²**); y la Asociación
Española de Normalización (**UNE**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación
> tipo de Técnica de Equipos, Instalaciones y Sistemas Eléctricos, punto 8):
> «Instalaciones singulares y automatizadas en edificios e industrias.»

**El enunciado junta dos cosas distintas y hay que separarlas para estudiarlas:**

| Mitad | Qué es | Dónde está |
|---|---|---|
| **Instalaciones SINGULARES** | **Las que el reglamento saca de la regla general** porque su emplazamiento o su uso lo exige | **En las instrucciones PARTICULARES**, de la ITC-BT-27 a la ITC-BT-39 |
| **Instalaciones AUTOMATIZADAS** | **Las que se gobiernan solas**: domótica, inmótica, control industrial | **En la ITC-BT-51 y, sobre todo, EN NINGUNA NORMA**: es oficio |

**Y la regla del reglamento que gobierna la primera mitad**, que es la del artículo 2.5 y hay que
tenerla presente: **las prescripciones específicas SUSTITUYEN, MODIFICAN O COMPLEMENTAN a las
generales, según los casos.** **Una instalación singular no es una instalación aparte: es una
instalación normal a la que se le añade o se le cambia algo.**

<!-- indice -->

## Índice

- [1. Cómo se decide que una instalación es singular](#1-cómo-se-decide-que-una-instalación-es-singular)
- [2. Los locales de pública concurrencia](#2-los-locales-de-pública-concurrencia)
- [3. La alimentación de los servicios de seguridad](#3-la-alimentación-de-los-servicios-de-seguridad)
- [4. El alumbrado de emergencia](#4-el-alumbrado-de-emergencia)
- [5. Las instalaciones automatizadas](#5-las-instalaciones-automatizadas)
- [6. Lo singular en una instalación audiovisual](#6-lo-singular-en-una-instalación-audiovisual)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Cómo se decide que una instalación es singular

**Lo que la convierte en singular es una INFLUENCIA EXTERNA o un USO**, y **conviene ordenarlas así,
porque es como se buscan en el reglamento:**

| Causa | Ejemplos de local |
|---|---|
| **El agua** | **Húmedos, mojados, piscinas y fuentes, saunas** |
| **El polvo o la corrosión** | **Polvorientos, con riesgo de corrosión** |
| **La temperatura** | **A temperatura elevada o muy baja** |
| **El riesgo de INCENDIO O EXPLOSIÓN** | **Atmósferas explosivas, almacenes de líquidos inflamables** |
| **La ocupación de personas** | **Locales de pública concurrencia** |
| **La condición de las personas** | **Quirófanos y salas de intervención** |
| **El carácter temporal** | **Obras, ferias, exposiciones, casetas** |
| **El emplazamiento móvil** | **Caravanas, puertos deportivos, vehículos** |

**Y las dos cosas que casi siempre cambian en una instalación singular, sea cual sea la causa:**

1. **El GRADO DE PROTECCIÓN exigido a las envolventes sube.**
2. **Aparecen VOLÚMENES o ZONAS con reglas distintas dentro del mismo local.** **En un cuarto de baño
   o en una piscina, la instrucción divide el espacio en volúmenes numerados y dice qué se puede
   poner en cada uno.**

**El segundo es el concepto que hay que saber nombrar**: **la reglamentación de locales singulares no
regula el LOCAL, regula ZONAS dentro del local.** **Lo que se puede instalar a un metro de una bañera
y a tres metros no es lo mismo, y el local es el mismo.**

## 2. Los locales de pública concurrencia

**Es la instrucción particular más importante para una corporación audiovisual**, y **hay que decir por
qué de entrada**: **un plató con público, un auditorio, un estudio de radio con invitados y hasta un
aparcamiento cubierto de más de cinco vehículos entran en ella.**

**Su campo de aplicación distingue dos familias y una regla de cálculo:**

| Familia | Cuándo entra |
|---|---|
| **Locales de espectáculos y actividades recreativas** | **Cualquiera que sea su capacidad de ocupación**: cines, teatros, auditorios, estadios, pabellones deportivos, salas de fiesta, discotecas |
| **Locales de reunión, trabajo y usos sanitarios** | **Unos, cualquiera que sea su ocupación** —templos, museos, salas de conferencias y congresos, hoteles, bares, aeropuertos, estaciones, **estacionamientos cerrados y cubiertos para más de 5 vehículos**, hospitales, asilos y guarderías—; **otros, si la ocupación prevista pasa de 50 personas** —bibliotecas, centros de enseñanza, establecimientos comerciales, **oficinas con presencia de público**, gimnasios, salas de exposiciones, centros culturales— |

**Y la regla de cálculo de la ocupación, que es un dato muy preguntable y que se cita:**

> «**La ocupación prevista de los locales se calculará como 1 persona por cada 0,8 m2 de superficie
> útil, a excepción de pasillos, repartidores, vestíbulos y servicios.**»
>
> — Real Decreto 842/2002, **ITC-BT-28**, apartado 1 (`BOE-A-2002-18099`), redacción vigente el 21 de
> diciembre de 2022.

---

**Los 0,8 metros cuadrados por persona son la cifra del epígrafe**, y **conviene fijarse en la
EXCEPCIÓN**: **pasillos, repartidores, vestíbulos y servicios NO cuentan**, porque **son superficie de
paso y no de estancia.**

**Y la cláusula de cierre de ese campo de aplicación, que amplía mucho**: **la instrucción se aplica
además a todos los locales no contemplados antes cuando tengan capacidad de ocupación de MÁS DE 100
PERSONAS.**

## 3. La alimentación de los servicios de seguridad

**Es el corazón de esa instrucción y lo que más toca a una casa que emite.**

**Qué son los servicios de seguridad**: **alumbrados de emergencia, sistemas contra incendios,
ascensores y otros servicios urgentes indispensables**, fijados por las reglamentaciones específicas
de las autoridades competentes.

**Y la clasificación que hay que saber de memoria, porque es la tabla del punto**: **una alimentación
automática se clasifica SEGÚN LA DURACIÓN DE CONMUTACIÓN:**

> «**– Sin corte: alimentación automática que puede estar asegurada de forma continua en las
> condiciones especificadas durante el periodo de transición, por ejemplo, en lo que se refiere a las
> variaciones de tensión y frecuencia.
> – Con corte muy breve: alimentación automática disponible en 0,15 segundos como máximo.
> – Con corte breve: alimentación automática disponible en 0,5 segundos como máximo.
> – Con corte mediano: alimentación automática disponible en 15 segundos como máximo.
> – Con corte largo: alimentación automática disponible en mas de 15 segundos.**»
>
> — Real Decreto 842/2002, **ITC-BT-28**, apartado 2 (`BOE-A-2002-18099`), redacción vigente el 21 de
> diciembre de 2022.

---

**Las cuatro cifras son 0,15 · 0,5 · 15 · más de 15**, y **la escalera se recuerda mejor por lo que
cada peldaño permite:**

| Categoría | Qué tecnología la cumple |
|---|---|
| **Sin corte** | **Un sistema de alimentación ininterrumpida en línea**, del tema 12 |
| **Corte muy breve** | **Conmutación estática** |
| **Corte breve** | Conmutación rápida |
| **Corte mediano** | **Un grupo electrógeno bien arrancado**, del tema 11 |
| **Corte largo** | **Un grupo que tarda más, o una puesta en marcha manual** |

**Y la lectura de oficio que enlaza los temas 11 y 12 y que es la conclusión del punto**: **ningún
grupo electrógeno cumple «sin corte» ni «corte muy breve», porque tiene que arrancar.** **Lo que da
continuidad es la batería; lo que da autonomía es el combustible.** **Una instalación crítica necesita
las dos cosas encadenadas.**

**Las fuentes de alimentación que la instrucción admite para los servicios de seguridad**: **baterías
de acumuladores, generadores independientes y derivaciones separadas de la red de distribución
efectivamente independientes de la alimentación normal.**

**Y las cuatro condiciones que impone a esas fuentes, que hay que saber enumerar:**

1. **Emplazamiento accesible SÓLO a personas cualificadas o expertas.**
2. **Emplazamiento VENTILADO**, de forma que los gases y humos no se propaguen a locales accesibles.
3. **NO se admiten derivaciones separadas alimentadas por una red pública**, salvo si se asegura que
   **las dos derivaciones no puedan fallar simultáneamente.**
4. **Si hay una sola fuente para los servicios de seguridad, NO se puede usar para otros usos.**
   **Con varias, sí puede compartirse**, siempre que **al fallar una, la potencia restante baste para
   todos los servicios de seguridad**, lo que **normalmente exige el corte automático de lo que no es
   seguridad.**

**La cuarta es la más práctica y la que más se incumple en instalaciones reales**: **un grupo comprado
para la seguridad al que se le van colgando cargas de confort deja de garantizar la seguridad**, y
**la manera correcta de compartirlo es con DESLASTRE automático.**

**Y el umbral de arranque, que es un dato muy concreto y muy preguntable**: **la puesta en
funcionamiento de la fuente propia se realiza al faltar la tensión de los suministros de la
distribuidora, o cuando esa tensión descienda por debajo del 70 % de su valor nominal.**

## 4. El alumbrado de emergencia

**La instrucción distingue DOS grandes tipos y hay que no confundirlos, porque persiguen cosas
distintas:**

| Tipo | Para qué es |
|---|---|
| **Alumbrado de SEGURIDAD** | **Para que la gente pueda EVACUAR o para evitar el pánico y los riesgos** |
| **Alumbrado de REEMPLAZAMIENTO** | **Para que la ACTIVIDAD pueda continuar** |

**Y el de seguridad se subdivide en tres, que es la enumeración que un examen pide:**

| Subtipo | Qué asegura |
|---|---|
| **De EVACUACIÓN** | **Que se vean e identifiquen las vías de salida** |
| **AMBIENTE o ANTIPÁNICO** | **Que se evite el pánico y se pueda llegar a las vías de evacuación** |
| **De ZONAS DE ALTO RIESGO** | **Que se puedan interrumpir con seguridad los procesos peligrosos** antes de salir |

**La diferencia que hay que enunciar y que casi nadie hace**: **el de seguridad sirve para IRSE; el de
reemplazamiento sirve para QUEDARSE.** **Un quirófano y un control de emisión piden el segundo; un
pasillo, el primero.**

**Y las dos formas de alimentarlo**: **aparatos AUTÓNOMOS, con su propia batería en cada luminaria**, o
**luminarias alimentadas por FUENTE CENTRAL.** **La primera es más simple y su mantenimiento es
luminaria a luminaria; la segunda concentra las baterías y exige cable resistente al fuego.**

## 5. Las instalaciones automatizadas

**Aquí acaba el reglamento y empieza el oficio**, y **el temario lo declara.**

**Los tres niveles de automatización de un edificio, que es el vocabulario del epígrafe:**

| Nivel | Qué gobierna | Cómo se llama |
|---|---|---|
| **Vivienda** | **Confort, energía, seguridad y comunicaciones de una vivienda** | **Domótica** |
| **Edificio** | **Las instalaciones de un edificio o un complejo** | **Inmótica o gestión técnica de edificios** |
| **Proceso industrial** | **Una máquina o una línea** | **Automatización industrial** |

**Y la arquitectura, que es común a los tres:**

| Elemento | Qué hace |
|---|---|
| **Sensores** | **Miden o detectan**: los del tema 4 |
| **Actuadores** | **Ejecutan**: relés, contactores, válvulas, variadores |
| **Controladores** | **Deciden**: autómatas programables, controladores libres |
| **Red o bus** | **Comunica** |
| **Supervisión** | **Muestra y registra**: sinópticos y sistemas de supervisión |

**Las dos arquitecturas posibles, que es la decisión de proyecto del epígrafe:**

| Arquitectura | Cómo es | Qué aporta |
|---|---|---|
| **CENTRALIZADA** | **Un controlador con toda la lógica y todas las entradas y salidas cableadas a él** | **Sencilla y barata en instalaciones pequeñas** |
| **DISTRIBUIDA** | **Varios dispositivos con lógica propia comunicados por un bus** | **Sigue funcionando si cae uno**; crece bien |

**Y la regla de oficio que decide entre las dos, y que es la misma del principio de autonomía**: **cada
nivel debe seguir funcionando si el de arriba desaparece.** **Un edificio cuya iluminación se apaga
porque ha caído el servidor de supervisión está mal diseñado**, y **la solución no es un servidor
mejor: es que el mando local no dependa de él.**

**El aviso de seguridad, que es el mismo de cualquier sistema conectado y aquí tiene consecuencia
física**: **un sistema de control de instalaciones en la misma red que la ofimática pone los cuadros,
las calderas y los grupos a un clic de quien abra un correo malicioso.** **La separación de redes no
es comodidad: es seguridad.**

**Y la instrucción que sí existe, para que no se dé por hecho que no hay ninguna**: **la ITC-BT-51
regula las instalaciones de sistemas de automatización, gestión técnica de la energía y seguridad para
viviendas y edificios**, y **el temario la nombra por lo que regula sin citarla.**

## 6. Lo singular en una instalación audiovisual

**Los cuatro emplazamientos de una casa que emite que caen en instrucción particular**, y **conviene
tenerlos identificados:**

| Emplazamiento | Qué instrucción lo alcanza | Qué le exige |
|---|---|---|
| **Plató y auditorio** | **La de locales de pública concurrencia** | **Servicios de seguridad, alumbrado de emergencia, prescripciones complementarias de espectáculos** |
| **Aparcamiento cubierto de más de cinco vehículos** | **La misma** | Lo mismo, y **proyecto sin límite de potencia si tiene ventilación forzada** |
| **Talleres de decorados, con pinturas y disolventes** | **La de locales con riesgo de incendio o explosión** | **Clasificación de zonas y material adecuado** |
| **Instalaciones temporales de exteriores, ferias y eventos** | **La de instalaciones temporales** | **Régimen documental propio**, que el tema 13 desarrolla |

**Y la conclusión de método que este punto deja, dicha en una línea**: **la pregunta correcta ante
cualquier instalación no es «¿qué dice el reglamento?», sino «¿QUÉ INSTRUCCIÓN PARTICULAR le
alcanza?».** **Aplicar sólo la general a un local que tiene la suya es el error de proyecto más caro
del oficio.**

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** (`BOE-A-2002-18099`), **en su redacción vigente el 21 de diciembre de 2022** | **De la ITC-BT-28**, la regla de cálculo de la ocupación del apartado 1 y la clasificación por duración de conmutación del apartado 2 |

**El aviso de método sobre las citas de instrucción técnica es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este tema NO da los grados de protección exigidos en cada local singular, ni las dimensiones de
   los volúmenes de baños y piscinas, ni los niveles de iluminación del alumbrado de emergencia, ni
   sus autonomías.** **Están en las tablas de las instrucciones particulares y, los de iluminación, en
   el Código Técnico de la Edificación**, y **una cifra que no se ha leído en su fuente no se
   escribe.**
2. **Las cifras que sí se dan son las que las dos citas contienen**: **1 persona por cada 0,8 m² de
   superficie útil, con su excepción**, **los 0,15 · 0,5 · 15 segundos de las categorías de
   conmutación** y **el 70 % de la tensión nominal como umbral de arranque de la fuente propia**,
   este último resumido del mismo apartado 2.2.
3. **Los apartados que se resumen y no se citan van identificados uno a uno** —de la ITC-BT-28, el 1
   en su cláusula de los 100 ocupantes, el 2.1, el 2.2, el 2.3, el 3 con sus subtipos y el 3.4—.
   **Están en la norma citada arriba.**
4. **Las instrucciones particulares que se NOMBRAN por lo que regulan y no se citan** son las de
   locales húmedos, mojados, polvorientos, con riesgo de corrosión, a temperatura elevada o muy baja,
   con riesgo de incendio o explosión, de instalaciones con fines especiales, de quirófanos y salas de
   intervención, y **la ITC-BT-51**, de sistemas de automatización y gestión técnica.
5. **La segunda mitad del punto —las instalaciones automatizadas— va como OFICIO de ingeniería de
   control y así se declara.** **No se ha consultado la documentación de ningún fabricante de
   autómatas, buses ni sistemas de supervisión**, y **no se nombra ningún producto ni ningún protocolo
   por su marca.**

**El resto del tema va como oficio y así se declara**: la separación del enunciado en sus dos mitades y
la lectura del artículo 2.5 como regla que las gobierna, la ordenación de las causas de singularidad
por influencia externa y por uso, la observación de que lo que se regula son zonas dentro del local y
no el local, la escalera de categorías de conmutación leída por la tecnología que cumple cada peldaño,
la conclusión de que ningún grupo electrógeno cumple «sin corte» y de que continuidad y autonomía son
cosas distintas, el aviso sobre el deslastre automático, la distinción entre alumbrado de seguridad
para irse y de reemplazamiento para quedarse, la comparación entre arquitectura centralizada y
distribuida con el principio de autonomía por niveles, el aviso de separación de redes, la tabla de
los cuatro emplazamientos singulares de una casa que emite y la conclusión de método sobre qué
instrucción particular alcanza a cada instalación. **Nada de eso lo dice la norma con esas palabras**,
y el tema no lo presenta como si lo dijera.
