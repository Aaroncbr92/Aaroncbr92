# Tema 14 del específico de Ingeniería Superior · Telecomunicación · Sistemas de redacción, ingesta, edición y emisión de informativos

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 16 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el sistema de redacción y su integración, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Cero preguntas, y aun así** | **Es la pieza más INTEGRADA de una casa y por eso la más difícil de cambiar.** Se elige por sus interfaces tanto como por sus prestaciones |
| **Extensión** | **2.032 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: el sistema de gestión de redacción
(**NRCS**, *newsroom computer system*); el protocolo de comunicación entre la redacción y los
dispositivos de producción (**MOS**, *media object server*); la gestión de recursos de medios
(**MAM**, *media asset management*); la ingesta; la copia de trabajo ligera (**proxy**); la lista de
decisiones de montaje (**EDL**); el sistema de automatización de emisión (**playout**); la interfaz de
programación de aplicaciones (**API**); la unidad móvil (**UM**) y el enlace desde el lugar de la
noticia (**ENG**, *electronic news gathering*); y el código de tiempo (**TC**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 16):
> «Elementos de producción (VI): Sistemas de redacción. Ingesta. Edición. Emisión y automatización de
> informativos. Equipamiento. Diagrama a bloques. Interconexión. Conexión con otras salas (Controles,
> Intercambios, Continuidades, etc.).»

**Es el punto de la producción MÁS EXIGENTE de una casa que emite**, y **conviene decir por qué**: **un
informativo se hace contra el reloj, con material que llega mientras se monta, y sale en directo.**
**Ningún otro flujo de trabajo junta esas tres cosas.**

**Y la idea que ordena el punto**: **en un sistema de redacción, la ESCALETA es la base de datos y todo
lo demás cuelga de ella.** **El texto, el vídeo, los rótulos, el orden y los tiempos no son ficheros
sueltos: son campos de la misma escaleta**, y **eso es lo que permite que un cambio de última hora se
propague solo a la emisión, al apuntador y al grafismo.**

**Este punto NO ha dado ni una pregunta en el cuadernillo de esta ocupación**, y **eso se declara**:
**el cero de un punto no significa que no vaya a caer.** **Significa que en ese llamamiento no cayó**,
y **el informe de cobertura de esta ocupación lo explica.**

<!-- indice -->

## Índice

- [1. El sistema de redacción](#1-el-sistema-de-redacción)
- [2. La ingesta](#2-la-ingesta)
- [3. La edición de informativos](#3-la-edición-de-informativos)
- [4. La emisión del informativo](#4-la-emisión-del-informativo)
- [5. La redundancia y la degradación](#5-la-redundancia-y-la-degradación)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. El sistema de redacción

**Qué es**: **la herramienta donde se escribe, se ordena y se cronometra el informativo**, y **el punto
desde el que se manda a todo lo demás.**

**Lo que contiene:**

| Elemento | Qué es |
|---|---|
| **ESCALETA** | **La lista ordenada de piezas**, con su duración, su fuente y su estado |
| **Guion de cada pieza** | **Texto para el apuntador**, con sus marcas de entrada y salida |
| **Referencias al material** | **Qué vídeo, qué rótulo y qué audio lleva cada pieza** |
| **CRONOMETRÍA** | **Duración prevista, duración real y desviación acumulada** |
| **Estados** | **Escrita, grabada, revisada, lista, emitida** |
| **Agenda y teletipos** | **Lo que entra de agencias y de la previsión** |

**Y las tres cosas que hacen útil ese sistema y que hay que saber enunciar:**

1. **Cronometra en TIEMPO REAL.** **La escaleta sabe cuánto dura lo escrito y cuánto queda de
   informativo**, y **avisa cuando no cabe.** **Sin eso, un informativo se sale o se queda corto en
   antena.**
2. **Es el ÚNICO sitio donde se cambia algo.** **Una pieza que se cae se cae en la escaleta**, y **el
   cambio llega solo a la emisión, al apuntador y al grafismo.** **Un sistema donde hay que cambiar
   las cosas en tres sitios pierde informativos.**
3. **Habla con los demás equipos por un PROTOCOLO.** **Un protocolo de comunicación entre la redacción
   y los dispositivos de producción es lo que permite que la escaleta mande sobre los servidores, el
   grafismo y el apuntador**, y **es la pieza de integración que decide si un sistema de redacción
   sirve en una casa concreta.**

## 2. La ingesta

**Meter material en el sistema**, y **hay que saber que hay cuatro vías y que no se parecen:**

| Vía | Qué llega | Qué exige |
|---|---|---|
| **De TARJETA o de cámara** | **Ficheros ya grabados** | **Copia y verificación**: es transferencia, no captura |
| **En TIEMPO REAL, desde una señal** | **Una señal en directo que hay que grabar** | **Un canal de ingesta ocupado durante todo el acto** |
| **De AGENCIA o intercambio** | **Material de fuera**, con sus metadatos | **Normalización de formato y de metadatos** |
| **Desde el ARCHIVO** | **Material antiguo** | **Restauración desde el soporte de conservación** |

**Y las tres reglas de la ingesta, que son las que evitan los desastres del oficio:**

1. **Se ingesta con METADATOS o no se ingesta.** **Un fichero sin título, sin fecha, sin origen y sin
   derechos es un fichero perdido en cuanto haya diez mil.** **La ingesta es el único momento en que
   esos datos se pueden capturar barato.**
2. **Se genera la COPIA LIGERA al ingestar.** **Montar sobre la copia y conformar al final es lo que
   permite que veinte redactores trabajen a la vez sin saturar el almacenamiento**, y **eso viene del
   tema 11.**
3. **La ingesta en tiempo real ocupa un recurso entero.** **Un canal de ingesta grabando un pleno de tres
   horas no está disponible para otra cosa**, y **por eso el número de canales es una decisión de
   dimensionado, no un detalle.**

**Y el aviso que enlaza con el tema 18**: **la ingesta es donde el almacenamiento se llena.** **Un
sistema sin política de borrado y de archivo se para solo al cabo de unos meses**, y **la política hay
que escribirla antes, no cuando el disco está lleno.**

## 3. La edición de informativos

**Lo que la distingue de la postproducción del tema 15:**

| | **Edición de informativos** | **Postproducción** |
|---|---|---|
| **Tiempo** | **Minutos** | **Días** |
| **Quién edita** | **El redactor, a menudo** | **Un montador** |
| **Herramienta** | **Sencilla, integrada en la redacción** | **Completa y especializada** |
| **Resultado** | **Una pieza que se emite hoy** | **Un programa** |
| **Prioridad** | **Que esté a tiempo** | **Que esté bien** |

**Y las dos consecuencias técnicas de esa columna izquierda:**

1. **La edición tiene que estar DONDE está el redactor.** **De ahí los puestos de edición ligera en la
   propia redacción**, y **de ahí la copia de trabajo: no se puede pedir a cincuenta puestos que
   muevan material de alta tasa.**
2. **El material se edita MIENTRAS SE INGESTA.** **Poder empezar a montar una señal que todavía se
   está grabando —edición sobre material creciente— es la prestación que decide si un sistema sirve
   para informativos.** **Sin ella, un directo de una hora no se puede montar hasta que acaba.**

## 4. La emisión del informativo

**Cómo se pasa de la escaleta a la antena:**

| Pieza | Qué hace |
|---|---|
| **Servidor de emisión de informativos** | **Reproduce las piezas** en el orden de la escaleta |
| **Sistema de automatización** | **Encadena y dispara**, mandado desde la escaleta |
| **GRAFISMO** | **Rótulos y elementos**, también desde la escaleta |
| **APUNTADOR** | **El texto que lee el presentador**, sincronizado con la escaleta |
| **Mezclador del estudio** | **La producción del directo**: es el control de realización del tema 13 |
| **Conexiones EXTERIORES** | **Directos desde unidad móvil, enlace o red** |

**Y las tres cosas que hay que saber de la interconexión, que es lo que el enunciado pide
expresamente:**

1. **Con los CONTROLES.** **El estudio de informativos es un estudio del tema 13**, y **la escaleta
   manda sobre su servidor y su grafismo.**
2. **Con los INTERCAMBIOS.** **Lo que llega de agencias, de corresponsales y de otras casas entra por
   ahí**, y **tiene que quedar ingestado y catalogado antes de que alguien lo busque.**
3. **Con las CONTINUIDADES.** **El informativo es una pieza de la escaleta de emisión del canal**, y
   **su hora de entrada y su duración están comprometidas.** **Cuando un informativo se alarga, es la
   continuidad quien absorbe el desajuste**, y **eso se pacta, no se improvisa.**

**Y la observación de arquitectura que cierra el punto**: **el sistema de redacción es la pieza más
integrada de una casa y por eso la más difícil de cambiar.** **Habla con el almacenamiento, con la
edición, con el grafismo, con la emisión y con el archivo**, y **sustituirlo obliga a rehacer todas
esas conversaciones.** **Por eso se elige por sus INTERFACES tanto como por sus prestaciones.**

## 5. La redundancia y la degradación

**Un informativo no puede no salir**, y **eso obliga a pensar el fallo antes de que ocurra:**

| Qué falla | Cómo se sigue emitiendo |
|---|---|
| **El sistema de redacción** | **Escaleta en papel y operación manual**: se pierde automatismo, no la emisión |
| **El servidor de emisión** | **Un segundo servidor con las mismas piezas**, replicadas |
| **El almacenamiento** | **Redundancia de la propia cabina** y copia de lo del día |
| **La red** | **Doble camino**: tema 20 |
| **El estudio entero** | **Un estudio alternativo con escaleta cargada** |
| **La energía** | **Sistema ininterrumpido y grupo**: tema 24 |

**Y las dos reglas que hay que llevar aprendidas:**

1. **La redundancia se prueba.** **Un servidor de reserva que nadie ha usado nunca no es una reserva:
   es una suposición.**
2. **La degradación tiene que ser ORDENADA y ENSAYADA.** **Que el equipo sepa qué hacer cuando la
   escaleta no responde es más valioso que un equipo de reserva que nadie sabe conmutar.**

## 6. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este punto NO ha dado ni una pregunta en el cuadernillo de esta ocupación**, y **el tema lo dice
   en su cabecera.** **El cero de un punto no significa que no vaya a caer**: **significa que en ese
   llamamiento no cayó.** **El informe de cobertura de esta ocupación reúne los siete puntos que
   están en esa situación y explica por qué se escriben igual.**
2. **Este tema NO nombra ningún sistema de redacción, ninguna herramienta de gestión de medios,
   ningún servidor y ningún fabricante.** **Un nombre propio obliga a una fuente**, y **el punto pide
   sistemas, no productos.**
3. **Este tema NO da ninguna cifra de número de canales de ingesta, de puestos, de capacidad, de
   duración de conservación ni de tiempo de restauración.** **Dependen de cada casa**, y **una cifra
   que no se ha leído en su fuente no se escribe.**
4. **El protocolo de comunicación entre la redacción y los dispositivos de producción se nombra por su
   función y por su sigla de uso común**, y **el temario NO le atribuye ninguna versión ni ninguna
   prestación concreta**: **no se ha consultado su especificación.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **la edición
   y las copias ligeras, al tema 11**; **las salas y la automatización de emisión, al tema 13**; **la
   postproducción, al tema 15**; **el grafismo, al tema 16**; **el almacenamiento y el archivo, al
   tema 18**; **y la red, al tema 20.**

**El resto del tema va como oficio y así se declara**: la caracterización del informativo como el flujo
más exigente por juntar reloj, material que llega y directo, la idea de que la escaleta es la base de
datos y todo cuelga de ella, las tres cosas que hacen útil un sistema de redacción, las cuatro vías de
ingesta con sus exigencias, las tres reglas de la ingesta y el aviso de que es donde se llena el
almacenamiento, la tabla que separa edición de informativos de postproducción con sus dos consecuencias
técnicas, las tres relaciones de interconexión con controles, intercambios y continuidades, la
observación de que un sistema de redacción se elige por sus interfaces tanto como por sus prestaciones,
la tabla de degradación y las dos reglas sobre probar la redundancia y ensayar la degradación. **Nada de
eso está en un boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo
presenta como si lo estuviera.
