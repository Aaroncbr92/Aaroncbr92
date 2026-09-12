# Esquema · Tema 12 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Sistemas de alimentación ininterrumpida, pilas y baterías

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = exigencia del reglamento, citada en el
tema 8 y aquí aplicada · `[of]` = oficio de instalaciones · `[plan]` = enunciado del anexo. **Siglas**:
el sistema de alimentación ininterrumpida (**SAI**), en inglés fuente de alimentación ininterrumpible
(**UPS**, *uninterruptible power supply*); el reglamento electrotécnico para baja tensión (**REBT**) y
sus instrucciones (**ITC-BT-28**, **ITC-BT-30**); el amperio hora (**Ah**) y el vatio hora (**Wh**); la
corriente continua (**CC**) y la alterna (**CA**); el plomo-ácido regulado por válvula (**VRLA**,
*valve regulated lead acid*); el ion litio (**Li-ion**); y la distorsión armónica total (**THD**,
*total harmonic distortion*).

**Cabecera.** Enunciado: punto 12 del anexo · **el enunciado es el índice.**

| Mitad | Subasuntos |
|---|---|
| **El sistema de alimentación ininterrumpida** | **Diagrama de bloques, funcionamiento y mantenimiento** |
| **Las pilas y las baterías** | **Generalidades y AGRUPACIÓN** |

- **LA IDEA QUE ENLAZA CON EL PUNTO 11** · `[of]` · **el grupo da AUTONOMÍA y este sistema da
  CONTINUIDAD** · **es el único que cumple la categoría «sin corte»** (tema 8), porque **su energía ya
  está almacenada y no hay nada que arrancar.**

<!-- indice -->

## Índice

- [El diagrama de bloques](#el-diagrama-de-bloques)
- [Las topologías](#las-topologías)
- [Pilas y baterías](#pilas-y-baterías)
- [La agrupación](#la-agrupación)
- [El mantenimiento](#el-mantenimiento)
- [Cómo se dimensiona en una casa que emite](#cómo-se-dimensiona-en-una-casa-que-emite)
- [Aviso de estudio](#aviso-de-estudio)

<!-- /indice -->

## El diagrama de bloques

| Bloque | Qué hace |
|---|---|
| **RECTIFICADOR o cargador** | **Convierte la alterna de entrada en continua** y **carga la batería** |
| **BATERÍA** | **Almacena la energía**: es la autonomía |
| **INVERSOR u ondulador** | **Convierte la continua en alterna** de salida |
| **BYPASS estático** | **Camino alternativo directo de la red a la salida**, por semiconductores |
| **Bypass de MANTENIMIENTO** | **Camino manual** para sacar el equipo sin cortar la carga |

| Bypass | Cuándo actúa | Cómo |
|---|---|---|
| **ESTÁTICO** | **Ante sobrecarga o fallo del inversor** | **Solo, en milisegundos** |
| **De MANTENIMIENTO** | **Cuando hay que reparar o sustituir** | **A mano, con secuencia de maniobra** |

- **POR QUÉ EL DE MANTENIMIENTO EXISTE** · `[of]` · **sin él, cambiar el equipo obliga a dejar sin
  tensión todo lo que protege** · **un sistema instalado sin bypass de mantenimiento garantiza
  continuidad excepto el día en que hay que tocarlo.**

## Las topologías

| Topología | En normal | Qué corrige | Transferencia |
|---|---|---|---|
| **Pasiva o de espera** | **La carga va DIRECTA a la red** | **Sólo el corte** | **La hay**, de milisegundos |
| **INTERACTIVA con la línea** | **Directa, con regulador de tensión** | **Corte y variaciones de tensión** | **La hay**, menor |
| **EN LÍNEA, doble conversión** | **La energía SIEMPRE pasa por rectificador e inversor** | **Corte, tensión, frecuencia, forma de onda y perturbaciones** | **NO la hay: es «sin corte»** |

- **POR QUÉ SÓLO LA TERCERA ES «SIN CORTE»** · `[of]` · **la carga NUNCA está alimentada por la red
  directamente**: **la alimenta siempre el inversor** · **cuando falta la red lo único que cambia es de
  dónde saca la continua el inversor** · **la salida no se entera.**
- **LO QUE LAS OTRAS DOS APORTAN A CAMBIO** · `[of]` · **rendimiento y precio** · **la doble conversión
  convierte la energía dos veces siempre**, con **coste energético permanente** · **los equipos
  modernos ofrecen modo de alta eficiencia que trabaja en espera y pasa a doble conversión al
  degradarse la red**, pero **en ese modo ya NO es «sin corte».**

| Prestación al elegir | Qué es |
|---|---|
| **Potencia** | **En kilovoltamperios y kilovatios**, con su factor de potencia de salida |
| **AUTONOMÍA** | **A qué carga y durante cuánto**: **no significa nada sin las dos cosas** |
| **Factor de potencia de ENTRADA y distorsión** | **Lo que devuelve a la red**: un rectificador antiguo ensucia mucho |
| **Capacidad de SOBRECARGA** | Y cuánto tiempo la aguanta |
| **Corriente de cortocircuito que aporta** | **Decide si las protecciones aguas abajo van a disparar** |

- **LA QUE SE OLVIDA Y DA EL FALLO MÁS DESCONCERTANTE** · `[of]` · **un inversor LIMITA su corriente de
  salida** · **un cortocircuito aguas abajo puede no dar corriente suficiente para hacer saltar el
  magnetotérmico** · **el sistema se protege pasando a bypass o desconectando, y cae TODA la carga en
  vez del circuito averiado** · **la selectividad aguas abajo hay que COMPROBARLA, no suponerla.**

## Pilas y baterías

| | **Pila** | **Acumulador o batería** |
|---|---|---|
| **Reacción** | **IRREVERSIBLE** | **REVERSIBLE** |
| **Se recarga** | **No** | **Sí** |
| **También se llama** | **Primaria** | **Secundaria** |

| Parámetro | Qué es |
|---|---|
| **Tensión NOMINAL** | **La de un elemento depende de su química** |
| **CAPACIDAD** | **La carga que entrega, en amperios hora**, **referida a un régimen de descarga** |
| **Energía** | **Capacidad por tensión**, en vatios hora |
| **Régimen de descarga** | **En cuánto tiempo se descarga** |
| **Profundidad de descarga** | **Qué porcentaje se saca en cada ciclo** |
| **Número de CICLOS** | **Cuántas cargas y descargas aguanta**, y **depende de la profundidad** |
| **Autodescarga** | **Lo que pierde estando parada** |
| **Corriente de cortocircuito** | **Enorme**: el dato de seguridad |

- **LA CIFRA QUE MÁS ENGAÑA** · `[of]` · **la capacidad DEPENDE DEL RÉGIMEN** · **la misma batería
  entrega bastante menos si se descarga en diez minutos que en diez horas** · **una capacidad sin su
  régimen no significa nada**, y **dimensionar la autonomía con la capacidad nominal es el error de
  cálculo clásico.**

| Química | Rasgos |
|---|---|
| **Plomo-ácido abierta** | **Barata, robusta**; **desprende hidrógeno y exige mantenimiento de nivel** |
| **Plomo-ácido REGULADA POR VÁLVULA** | **Sin mantenimiento de nivel**; la clásica de estos sistemas |
| **Níquel-cadmio** | **Muy robusta a temperatura extrema y descarga profunda**; cara |
| **ION LITIO** | **Más energía por kilo y por litro, más ciclos**; **exige sistema de gestión** |

- **EL AVISO DE SEGURIDAD DE LAS DE PLOMO ABIERTO** · `[of]` · **desprenden HIDRÓGENO al cargar** y
  **el hidrógeno es explosivo** · `[BOE]` · **de ahí que el local tenga que estar VENTILADO** —lo que
  la instrucción de fuentes propias exige en general— **y que la instrucción de locales con riesgo de
  incendio o explosión pueda alcanzarlo.**

## La agrupación

| Agrupación | Cómo se conectan | Qué se suma | Qué se mantiene |
|---|---|---|---|
| **SERIE** | **Positivo de uno al negativo del siguiente** | **Las TENSIONES** | **La capacidad** |
| **PARALELO** | **Todos los positivos juntos y todos los negativos juntos** | **Las CAPACIDADES** | **La tensión** |
| **SERIE-PARALELO** | **Ramas en serie, puestas en paralelo** | **Las dos cosas** | — |

- **LA REGLA QUE RESUME LAS DOS** · `[of]` · **en serie se suma lo que EMPUJA; en paralelo se suma lo
  que DURA.**
- **LAS TRES CONDICIONES** · `[of]` · **elementos IGUALES**: misma química, capacidad y tensión y, a ser
  posible, **mismo lote y misma antigüedad** · **en SERIE la corriente es común**, así que **el elemento
  más débil limita la rama entera** · **en PARALELO la tensión es común**, así que **un elemento en peor
  estado se vuelve carga para los demás** y **circulan corrientes de igualación.**
- **LA CONSECUENCIA PRÁCTICA** · `[of]` · **NO se sustituye un solo elemento de una batería
  envejecida** · **uno nuevo en una cadena vieja no la arregla: se degrada rápido igualándose** · **se
  sustituye el conjunto.**
- **LO ÚNICO QUE SE CONSERVA EN LAS DOS** · `[of]` · **la energía total es siempre la suma de las
  energías de los elementos** · **lo que cambia es en qué forma se entrega: más tensión o más
  corriente.**

## El mantenimiento

| Tarea | Por qué |
|---|---|
| **Inspección visual de la batería** | **Bornes, corrosión, deformación, fugas.** **Un vaso hinchado se cambia** |
| **Temperatura del local** | **Lo que MÁS acorta la vida de una batería de plomo** |
| **Apriete de conexiones** | **Un contacto flojo en continua arde igual que en alterna** |
| **PRUEBA DE DESCARGA** | **La única que dice la autonomía real** |
| **Registro de alarmas e histórico** | Lo que anticipa el fallo |
| **Limpieza de filtros y ventiladores** | La refrigeración del equipo |
| **Prueba del BYPASS** | **De los dos**, y **la del manual con procedimiento escrito** |

- **LA FILA CONTRAINTUITIVA, QUE ES LA CLAVE** · `[of]` · **la vida de una batería de plomo se acorta
  drásticamente con la TEMPERATURA** · **una sala caliente consume la vida útil antes de lo previsto** y
  **la instalación no da ninguna señal hasta el día en que hace falta** · **refrigerar la sala de
  baterías no es confort: es alargar la vida del sistema.**
- **LA ÚNICA PRUEBA QUE VALE** · `[of]` · **una batería con su tensión correcta EN FLOTACIÓN puede no
  tener capacidad ninguna** · **la tensión en reposo no mide la capacidad**: **sólo la mide una
  descarga controlada**, con carga real o banco de cargas. (Temas 9 y 11.)
- **EL AVISO DE SEGURIDAD PROPIO** · `[of]` · **una batería NO tiene interruptor**: **no se puede
  «dejar sin tensión» un conjunto de baterías** y **su corriente de cortocircuito es enorme** ·
  **herramienta aislada, sin anillos ni relojes, protección facial y, en plomo abierto, protección
  frente al electrolito** · **un destornillador que cruza dos bornes de una batería grande se funde.**

## Cómo se dimensiona en una casa que emite

| Decisión | Cómo se toma |
|---|---|
| **1 · Qué se protege** | **Sólo lo que no puede caerse ni un ciclo**: control central, emisión, servidores, red y **su refrigeración** |
| **2 · Qué topología** | **Doble conversión** para lo crítico; **lo demás puede ir en espera** |
| **3 · Cuánta AUTONOMÍA** | **La que haga falta hasta que el grupo tome carga**, más margen; **no más** |
| **4 · Cómo se encadena con el grupo** | **El sistema cubre el arranque del grupo; el grupo recarga el sistema** |

- **LA OBSERVACIÓN QUE RESUME LOS TEMAS 11 Y 12** · `[of]` · **la autonomía NO se dimensiona para
  aguantar el corte: se dimensiona para aguantar hasta que arranque el grupo** · **pedirle horas a una
  batería habiendo grupo es pagar dos veces por lo mismo**, y **no pedirle nada sin grupo es no tener
  nada** · **la cifra sale del escenario, y el escenario hay que escribirlo.**

## Aviso de estudio

- **ESTE TEMA NO TIENE CITA LITERAL PROPIA** · `[of]` · **la categoría «sin corte», la admisión de las
  baterías como fuente propia y la exigencia de ventilación están citadas en el tema 8, con su apartado
  identificado.**
- **LO QUE NO SE DA** · `[of]` · **ninguna tensión de elemento, ninguna capacidad, ninguna tensión de
  flotación, ningún número de ciclos, ninguna temperatura de referencia y ningún rendimiento** · **las
  químicas se describen por sus rasgos de uso y no por su composición.**
