# Tema 12 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Sistemas de alimentación ininterrumpida, pilas y baterías

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Téc. Equipos, Instalaciones y Sistemas Eléctricos · punto 12 |
| **Sirve para** | **Téc. Equipos, Instalaciones y Sistemas Eléctricos** |
| **Fuente** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** |
| **Identificador** | `BOE-A-2002-18099` · BOE núm. 224, de 18/09/2002 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. **Ninguna cita literal propia**: la categoría «sin corte», la admisión de las baterías como fuente propia y la exigencia de ventilación están citadas en el tema 8 |
| **Aviso de estudio** | **Es el único sistema que cumple la categoría «sin corte»** de la instrucción de pública concurrencia, **porque su energía ya está almacenada y no hay nada que arrancar** |
| **Extensión** | **2.781 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el sistema de alimentación ininterrumpida (**SAI**),
que en inglés se llama fuente de alimentación ininterrumpible (**UPS**, *uninterruptible power
supply*); el reglamento electrotécnico para baja tensión (**REBT**) y sus instrucciones
(**ITC-BT-28**, **ITC-BT-30**); el amperio hora (**Ah**) y el vatio hora (**Wh**); el voltio (**V**);
la corriente continua (**CC**) y la alterna (**CA**); el plomo-ácido regulado por válvula (**VRLA**,
*valve regulated lead acid*); el ion litio (**Li-ion**); y la distorsión armónica total (**THD**,
*total harmonic distortion*).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación
> tipo de Técnica de Equipos, Instalaciones y Sistemas Eléctricos, punto 12):
> «Sistemas de alimentación ininterrumpida ‐ SAI/UPS: Diagrama de bloques, funcionamiento y
> mantenimiento. Generalidades sobre pilas y baterías. Agrupación de pilas y baterías.»

**El enunciado divide el punto en dos mitades con sus subasuntos escritos**, y **conviene aprovecharlo
como índice:**

| Mitad | Subasuntos |
|---|---|
| **El sistema de alimentación ininterrumpida** | **Diagrama de bloques, funcionamiento y mantenimiento** |
| **Las pilas y las baterías** | **Generalidades y AGRUPACIÓN** |

**Y la idea que enlaza este punto con el 11 y que hay que repetir**: **el grupo electrógeno da
AUTONOMÍA y el sistema de alimentación ininterrumpida da CONTINUIDAD.** **Éste es el único que cumple
la categoría «sin corte» de la instrucción de pública concurrencia citada en el tema 8**, porque
**su energía ya está almacenada y no hay nada que arrancar.**

<!-- indice -->

## Índice

- [1. El diagrama de bloques](#1-el-diagrama-de-bloques)
- [2. Las topologías](#2-las-topologías)
- [3. Las pilas y las baterías](#3-las-pilas-y-las-baterías)
- [4. La agrupación de pilas y baterías](#4-la-agrupación-de-pilas-y-baterías)
- [5. El mantenimiento](#5-el-mantenimiento)
- [6. Cómo se dimensiona el conjunto en una casa que emite](#6-cómo-se-dimensiona-el-conjunto-en-una-casa-que-emite)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. El diagrama de bloques

**El enunciado lo pide expresamente.** **Los cinco bloques, en orden, con lo que hace cada uno:**

| Bloque | Qué hace |
|---|---|
| **RECTIFICADOR o cargador** | **Convierte la alterna de entrada en continua**, y **carga la batería** |
| **BATERÍA** | **Almacena la energía**: es la autonomía |
| **INVERSOR u ondulador** | **Convierte la continua en alterna** de salida, con su tensión y su frecuencia |
| **BYPASS estático** | **Un camino alternativo directo de la red a la salida**, con conmutación por semiconductores |
| **Bypass de MANTENIMIENTO** | **Un camino manual** que permite sacar el equipo entero sin cortar la carga |

**Y los dos bypass son lo que más se confunde y hay que separarlos con claridad:**

| Bypass | Cuándo actúa | Cómo |
|---|---|---|
| **ESTÁTICO o automático** | **Ante una sobrecarga o un fallo del inversor** | **Solo, en milisegundos** |
| **De MANTENIMIENTO o manual** | **Cuando hay que reparar o sustituir el equipo** | **A mano, con una secuencia de maniobra** |

**La razón de ser del bypass de mantenimiento merece una frase**: **sin él, cambiar un sistema de
alimentación ininterrumpida obliga a dejar sin tensión todo lo que protege.** **Con él, se transfiere
la carga a la red, se saca el equipo y se vuelve.** **Un sistema instalado sin bypass de mantenimiento
es un sistema que garantiza continuidad excepto el día en que hay que tocarlo.**

## 2. Las topologías

**Tres, y hay que saber cuál protege de qué**, porque **es la decisión de compra del punto:**

| Topología | Cómo funciona en normal | Qué corrige | Tiempo de transferencia |
|---|---|---|---|
| **Pasiva o de espera** | **La carga va DIRECTA a la red**; la batería espera | **Sólo el corte** | **Hay transferencia**, de milisegundos |
| **INTERACTIVA con la línea** | **Directa a la red, con un regulador que corrige la tensión** | **Corte y variaciones de tensión** | **Hay transferencia**, menor |
| **EN LÍNEA, de doble conversión** | **La energía SIEMPRE pasa por rectificador e inversor** | **Corte, tensión, frecuencia, forma de onda y perturbaciones** | **NO hay transferencia: es «sin corte»** |

**La tercera es la única que cumple la categoría «sin corte»**, y **la razón hay que saber decirla**:
**en doble conversión la carga NUNCA está alimentada por la red directamente.** **Está alimentada
siempre por el inversor**, y **cuando falta la red, lo único que cambia es de dónde saca la continua el
inversor: de la batería en vez del rectificador.** **La salida no se entera.**

**Y lo que las otras dos aportan a cambio**: **rendimiento y precio.** **Una doble conversión convierte
la energía dos veces siempre**, y **eso tiene un coste energético permanente.** **Por eso los equipos
modernos ofrecen un modo de alta eficiencia que trabaja en espera y pasa a doble conversión cuando la
red se degrada**, con **la contrapartida de que en ese modo ya no es «sin corte».**

**Las prestaciones que hay que mirar al elegir uno**, además de la topología:

| Prestación | Qué es |
|---|---|
| **Potencia** | **En kilovoltamperios y en kilovatios**, con su factor de potencia de salida |
| **AUTONOMÍA** | **A qué carga y durante cuánto**: no significa nada sin las dos cosas |
| **Factor de potencia de ENTRADA y distorsión** | **Lo que el equipo devuelve a la red**: un rectificador antiguo ensucia mucho |
| **Capacidad de SOBRECARGA** | Y cuánto tiempo la aguanta |
| **Corriente de cortocircuito que puede aportar** | **Decide si las protecciones aguas abajo van a disparar** |

**La última es la que se olvida y la que produce el fallo más desconcertante**: **un inversor limita su
corriente de salida**, de modo que **un cortocircuito aguas abajo puede no producir corriente
suficiente para hacer saltar el magnetotérmico correspondiente.** **El resultado es que el sistema se
protege a sí mismo pasando a bypass o desconectando, y cae TODA la carga en vez del circuito
averiado.** **La selectividad aguas abajo de un sistema de alimentación ininterrumpida hay que
comprobarla, no suponerla.**

## 3. Las pilas y las baterías

**La segunda mitad del enunciado.** **La distinción de partida, en una línea:**

| | **Pila** | **Acumulador o batería** |
|---|---|---|
| **Reacción** | **IRREVERSIBLE** | **REVERSIBLE** |
| **Se recarga** | **No** | **Sí** |
| **También se llama** | **Primaria** | **Secundaria** |

**Los parámetros que definen a una batería y que hay que saber nombrar:**

| Parámetro | Qué es |
|---|---|
| **Tensión NOMINAL** | La de referencia; **la de un elemento depende de su química** |
| **CAPACIDAD** | **La carga que puede entregar, en amperios hora**, **referida a un régimen de descarga** |
| **Energía** | **Capacidad por tensión**, en vatios hora |
| **Régimen de descarga** | **En cuánto tiempo se descarga**: se escribe como una fracción de la capacidad |
| **Profundidad de descarga** | **Qué porcentaje se le saca en cada ciclo** |
| **Número de CICLOS** | **Cuántas cargas y descargas aguanta**, y **depende de la profundidad** |
| **Autodescarga** | **Lo que pierde estando parada** |
| **Corriente de cortocircuito** | **Enorme**: es el dato de seguridad |

**Y el aviso que hay que dar sobre la capacidad, porque es la cifra que más engaña**: **la capacidad de
una batería DEPENDE DEL RÉGIMEN al que se le pida.** **La misma batería entrega bastante menos energía
si se descarga en diez minutos que si se descarga en diez horas.** **Una capacidad sin su régimen no
significa nada**, y **dimensionar la autonomía de un sistema de alimentación ininterrumpida con la
capacidad nominal en vez de con la del régimen real es el error de cálculo clásico.**

**Las químicas que un técnico encuentra:**

| Química | Rasgos |
|---|---|
| **Plomo-ácido abierta** | **Barata, robusta, muy usada en arranque**; **desprende hidrógeno y exige mantenimiento de nivel** |
| **Plomo-ácido REGULADA POR VÁLVULA** | **Sin mantenimiento de nivel**; la de los sistemas de alimentación ininterrumpida clásicos |
| **Níquel-cadmio** | **Muy robusta a temperatura extrema y a descarga profunda**; cara |
| **ION LITIO** | **Mucha más energía por kilo y por litro, más ciclos**; **exige sistema de gestión** y tiene su propio régimen de seguridad |

**Y el aviso de seguridad de las de plomo abierto, que es reglamentario y enlaza con el tema 8**:
**desprenden HIDRÓGENO al cargar**, y **el hidrógeno es explosivo.** **De ahí que el local de baterías
tenga que estar VENTILADO** —lo que la instrucción de fuentes propias exige de forma general— **y de
ahí que la instrucción de locales con riesgo de incendio o explosión pueda alcanzarlo.**

## 4. La agrupación de pilas y baterías

**El enunciado la nombra expresamente y es el asunto más «de examen» del punto**, porque **son dos
reglas simétricas:**

| Agrupación | Cómo se conectan | Qué se suma | Qué se mantiene |
|---|---|---|---|
| **SERIE** | **El positivo de uno al negativo del siguiente** | **Las TENSIONES** | **La capacidad**, en amperios hora |
| **PARALELO** | **Todos los positivos juntos y todos los negativos juntos** | **Las CAPACIDADES** | **La tensión** |
| **SERIE-PARALELO o mixta** | **Ramas en serie, puestas en paralelo** | **Las dos cosas** | — |

**Y la regla que hay que enunciar y que resume las dos**: **en serie se suma lo que empuja; en paralelo
se suma lo que dura.**

**Las tres condiciones para agrupar bien, que son las que un examen persigue:**

1. **Los elementos deben ser IGUALES**: misma química, misma capacidad, misma tensión y, a ser
   posible, **del mismo lote y la misma antigüedad.**
2. **En SERIE, la corriente es común a todos**, así que **el elemento más débil limita a toda la
   rama.** **Una cadena en serie vale lo que su peor elemento.**
3. **En PARALELO, la tensión es común**, así que **un elemento en peor estado se convierte en una
   carga para los demás** y **circulan corrientes de igualación entre ramas.**

**La consecuencia práctica de las dos últimas, y es la que hay que saber decir**: **NO se sustituye un
solo elemento de una batería envejecida.** **Un elemento nuevo en una cadena vieja no la arregla: se
degrada rápido igualándose con los demás.** **Lo que se sustituye es el conjunto.**

**Y la energía es lo único que se conserva en las dos agrupaciones**: **la energía total es siempre la
suma de las energías de los elementos**, **se conecten como se conecten.** **Lo que cambia es en qué
forma —más tensión o más corriente— se entrega.**

## 5. El mantenimiento

**El enunciado lo pide expresamente para el sistema de alimentación ininterrumpida**, y **es donde
está lo que un técnico de mantenimiento hace de verdad:**

| Tarea | Cada cuánto y por qué |
|---|---|
| **Inspección visual de la batería** | **Bornes, corrosión, deformación de vasos, fugas.** **Un vaso hinchado se cambia** |
| **Temperatura del local** | **Es lo que MÁS acorta la vida de una batería de plomo** |
| **Apriete y estado de las conexiones** | **Un contacto flojo en continua arde igual que en alterna** |
| **PRUEBA DE DESCARGA** | **La única que dice la autonomía real** |
| **Registro de alarmas y del histórico** | Lo que anticipa el fallo |
| **Limpieza de filtros y ventiladores** | La refrigeración del equipo |
| **Prueba del BYPASS** | **De los dos**, y **la del manual con procedimiento escrito** |

**La segunda fila merece explicación porque es contraintuitiva y es la clave del punto**: **la vida de
una batería de plomo se acorta drásticamente con la TEMPERATURA.** **Una sala de baterías caliente
consume la vida útil mucho antes de lo previsto**, y **la instalación no da ninguna señal hasta el día
en que hace falta.** **Refrigerar la sala de baterías no es confort: es alargar la vida del sistema.**

**Y la cuarta es la única prueba que vale y hay que insistir**: **una batería que muestra su tensión
correcta EN FLOTACIÓN puede no tener capacidad ninguna.** **La tensión en reposo no mide la
capacidad.** **Lo único que la mide es una descarga controlada**, y **por eso los sistemas críticos se
prueban con carga real o con banco de cargas.** **Es el mismo argumento del tema 9 y del tema 11.**

**El aviso de seguridad del mantenimiento de baterías, que es propio y hay que darlo**: **una batería
NO tiene interruptor.** **No se puede «dejar sin tensión» un conjunto de baterías**, y **su corriente
de cortocircuito es enorme.** **Trabajar en ellas exige herramienta aislada, retirar anillos y relojes,
protección facial y, en las de plomo abierto, protección frente al electrolito.** **Un destornillador
que cruza dos bornes de una batería grande se funde.**

## 6. Cómo se dimensiona el conjunto en una casa que emite

**Las cuatro decisiones, en orden:**

| Decisión | Cómo se toma |
|---|---|
| **1 · Qué se protege** | **Sólo lo que no puede caerse ni un ciclo**: control central, emisión, servidores, red, y **su refrigeración** |
| **2 · Qué topología** | **Doble conversión** para lo crítico; **lo demás puede ir en espera** |
| **3 · Cuánta AUTONOMÍA** | **La que haga falta hasta que el grupo tome carga**, más un margen; **no más** |
| **4 · Cómo se encadena con el grupo** | **El sistema cubre el arranque del grupo; el grupo recarga el sistema** |

**Y la observación que este temario declara como suya y que resume los temas 11 y 12**: **la autonomía
de un sistema de alimentación ininterrumpida NO se dimensiona para aguantar el corte, se dimensiona
para aguantar hasta que arranque el grupo.** **Pedirle horas a una batería cuando hay un grupo detrás
es pagar dos veces por lo mismo**, y **no pedirle nada cuando no hay grupo es no tener nada.** **La
cifra sale del escenario, y el escenario hay que escribirlo.**

## 7. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** (`BOE-A-2002-18099`), **en su redacción vigente el 21 de diciembre de 2022** | **Ninguna cita literal nueva**: lo que este tema afirma del reglamento está **citado en el tema 8** de este mismo específico, y **aquí se remite** |

**Cinco declaraciones expresas:**

1. **Este tema NO tiene cita literal propia**, y **lo dice.** **La categoría de conmutación «sin
   corte», la admisión de las baterías de acumuladores como fuente propia de energía y la exigencia de
   ventilación del emplazamiento están citadas o resumidas en el tema 8**, **con su apartado
   identificado.**
2. **Este tema NO da ninguna tensión de elemento, ninguna capacidad, ninguna tensión de flotación,
   ningún número de ciclos, ninguna temperatura de referencia y ningún rendimiento.** **Son dato de
   norma de producto y de fabricante**, y **una cifra que no se ha leído en su fuente no se escribe.**
   **Lo que el temario da es el sentido en que influye cada variable.**
3. **Las químicas de batería se describen por sus rasgos de uso y NO por su composición ni por sus
   tensiones**, que **no se han consultado en ninguna fuente.**
4. **La reglamentación de seguridad de baterías de ion litio y la de almacenamiento de energía no
   están en el enunciado de este punto y no se han consultado.** **El temario sólo dice que esa
   química exige sistema de gestión y tiene régimen propio de seguridad**, sin atribuir eso a ninguna
   norma.
5. **La instrucción de locales con riesgo de incendio o explosión se nombra por lo que regula y no se
   cita**: **el temario dice que PUEDE alcanzar a un local de baterías**, y **no afirma que lo haga
   siempre ni en qué condiciones**, que **es materia de clasificación de zonas que este tema no
   desarrolla.**

**El resto del tema va como oficio y así se declara**: la lectura del enunciado como índice, la
distinción entre autonomía y continuidad repetida del tema 11, la separación de los dos bypass con la
razón del de mantenimiento, la explicación de por qué la doble conversión es la única «sin corte», la
observación sobre el modo de alta eficiencia y su contrapartida, el aviso sobre la corriente de
cortocircuito del inversor y la selectividad aguas abajo, la advertencia de que una capacidad sin su
régimen no significa nada, la regla de que en serie se suma lo que empuja y en paralelo lo que dura,
las tres condiciones de agrupación con la consecuencia de no sustituir un solo elemento, la
observación de que la energía se conserva en las dos agrupaciones, la explicación de la temperatura
como lo que más acorta la vida de una batería, la insistencia en la prueba de descarga como única
medida válida, el aviso de seguridad de que una batería no tiene interruptor y la regla de dimensionar
la autonomía por el arranque del grupo. **Nada de eso lo dice la norma con esas palabras**, y el tema
no lo presenta como si lo dijera.
