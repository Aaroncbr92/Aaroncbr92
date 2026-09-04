# Tema 2 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Electrotecnia: transformadores y motores

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Téc. Equipos, Instalaciones y Sistemas Eléctricos · punto 2 |
| **Sirve para** | **Téc. Equipos, Instalaciones y Sistemas Eléctricos** |
| **Fuente** | **Sin norma: el enunciado no nombra ninguna.** Su materia es la teoría de máquinas eléctricas, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **El enunciado es el índice** | **Primera mitad el transformador** —generalidades, teoría, acoplamiento en paralelo, autotransformador, aislamiento galvánico, pérdidas—; **segunda mitad el motor** —tipos, estrella-triángulo, guardamotores |
| **Extensión** | **3.736 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: el reglamento electrotécnico para baja
tensión (**REBT**), del tema 1; el voltamperio (**VA**) y el kilovoltamperio (**kVA**); el vatio
(**W**) y el kilovatio (**kW**); revoluciones por minuto (**r.p.m.**); la relación de transformación
(**m**); el número de pares de polos (**p**); la protección térmica de motor o **guardamotor**; el
arrancador progresivo (**arrancador suave**); y el variador de frecuencia (**variador**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación
> tipo de Técnica de Equipos, Instalaciones y Sistemas Eléctricos, punto 2):
> «Electrotecnia: Generalidades sobre transformadores. Teoría de funcionamiento. Acoplamiento en
> paralelo. Autotransformador. Aislamiento galvánico. Pérdidas. Motores: tipos de motores,
> disposición estrella‐triángulo. Guarda‐motores.»

**Es el punto de las MÁQUINAS ELÉCTRICAS**, y **el enunciado lo divide expresamente en dos mitades con
sus subasuntos escritos uno a uno.** **Eso es una ayuda para estudiar y conviene aprovecharla**: **el
enunciado es el índice.**

**Primera mitad, el transformador**: generalidades, teoría de funcionamiento, acoplamiento en paralelo,
autotransformador, aislamiento galvánico y pérdidas. **Segunda mitad, el motor**: tipos, disposición
estrella-triángulo y guardamotores.

**Y el aviso de reparto con el tema 1**: **aquel punto los NOMBRA y éste los DESARROLLA.** **Los
fundamentos —inducción, sistema trifásico, estrella y triángulo como conexiones— están allí y aquí no
se repiten**: se usan.

<!-- indice -->

## Índice

- [1. El transformador: qué es y en qué se apoya](#1-el-transformador-qué-es-y-en-qué-se-apoya)
- [2. El aislamiento galvánico](#2-el-aislamiento-galvánico)
- [3. El autotransformador](#3-el-autotransformador)
- [4. El acoplamiento en paralelo](#4-el-acoplamiento-en-paralelo)
- [5. Las pérdidas y el rendimiento](#5-las-pérdidas-y-el-rendimiento)
- [6. Los motores: tipos](#6-los-motores-tipos)
- [7. El arranque estrella-triángulo y los demás](#7-el-arranque-estrella-triángulo-y-los-demás)
- [8. El guardamotor y la protección de la máquina](#8-el-guardamotor-y-la-protección-de-la-máquina)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. El transformador: qué es y en qué se apoya

**La definición, con las tres condiciones que la hacen exacta**: **una máquina eléctrica ESTÁTICA que
transfiere energía entre dos circuitos de corriente alterna, cambiando la tensión y la corriente y
MANTENIENDO LA FRECUENCIA.**

| Palabra de la definición | Por qué está |
|---|---|
| **Estática** | **No tiene partes móviles**, y por eso su rendimiento es el más alto de todas las máquinas eléctricas |
| **Alterna** | **Necesita flujo VARIABLE**: en continua no funciona, y ésa es la frontera del tema 1 |
| **Mantiene la frecuencia** | **Lo que cambia es la tensión, no la frecuencia**: eso lo hace un variador, no un transformador |

**Sus partes:**

| Parte | Qué es |
|---|---|
| **Núcleo magnético** | **Chapa de acero al silicio APILADA Y AISLADA entre sí**, para conducir el flujo y limitar las corrientes parásitas |
| **Devanado PRIMARIO** | **El que recibe la energía** de la red |
| **Devanado SECUNDARIO** | **El que la entrega** a la carga |
| **Aislamientos, cuba, refrigerante y aisladores pasantes** | El resto, en los de potencia |

**El principio de funcionamiento, en cuatro pasos que hay que saber recitar:**

1. **La tensión alterna del primario hace circular una corriente alterna por su devanado.**
2. **Esa corriente crea un FLUJO MAGNÉTICO ALTERNO en el núcleo.**
3. **Ese flujo atraviesa el secundario y, por ser variable, induce en él una tensión.**
4. **La tensión inducida es proporcional al número de espiras de cada devanado.**

**De ahí la RELACIÓN DE TRANSFORMACIÓN, que es la fórmula del punto:**

**m = N₁ / N₂ = U₁ / U₂ = I₂ / I₁**

| Consecuencia | Qué significa |
|---|---|
| **Las tensiones son DIRECTAMENTE proporcionales a las espiras** | Más espiras, más tensión |
| **Las corrientes son INVERSAMENTE proporcionales** | **El lado de más tensión lleva menos corriente** |
| **La potencia APARENTE es prácticamente la misma en los dos lados** | Salvo las pérdidas del epígrafe 5 |

**Y la lectura de oficio que hace útil la fórmula, y que enlaza con el tema 1**: **elevar la tensión
para transportar reduce la corriente en la misma proporción, y las pérdidas caen con el CUADRADO.**
**Multiplicar la tensión por diez divide las pérdidas por cien.** **Eso es toda la razón de ser de un
centro de transformación.**

## 2. El aislamiento galvánico

**El enunciado lo nombra expresamente y merece su epígrafe**, porque **es la propiedad del
transformador que un técnico de una casa que emite usa más y explica peor.**

**Qué es**: **la separación ELÉCTRICA entre el primario y el secundario.** **La energía pasa por el
campo magnético, no por un conductor**, de modo que **no hay ningún camino de corriente entre los dos
circuitos.**

**Para qué sirve, en cuatro usos que hay que saber nombrar:**

| Uso | Qué resuelve |
|---|---|
| **Seguridad de las personas** | **Un secundario aislado y sin poner a tierra no cierra circuito a través de una persona en contacto con un solo conductor** |
| **Romper bucles de masa** | **Elimina la corriente que circula entre dos equipos unidos por su masa y alimentados de puntos distintos** |
| **Adaptar regímenes de neutro** | Permite crear localmente un esquema distinto del de la red |
| **Reducir la transmisión de perturbaciones** | Sobre todo con **pantalla electrostática entre devanados** |

**El segundo uso es el que toca a una instalación audiovisual de lleno**, y **conviene explicarlo
porque es el zumbido de red más famoso del oficio**: **cuando dos equipos de audio están unidos por la
malla de un cable y alimentados de dos cuadros distintos, la pequeña diferencia de potencial entre las
dos tierras hace circular una corriente por esa malla.** **Esa corriente se oye.** **Un transformador
de aislamiento —o un transformador de audio en la línea de señal— corta el bucle.**

**Y el aviso técnico que hay que dar, porque es donde se falla**: **un AUTOTRANSFORMADOR NO da
aislamiento galvánico.** **Es la razón por la que el enunciado del anexo nombra las dos cosas
seguidas**, y **es el epígrafe siguiente.**

## 3. El autotransformador

**Qué es**: **un transformador con UN SOLO devanado, del que se toma una derivación intermedia.**
**Primario y secundario comparten parte del devanado**, y por tanto **están unidos eléctricamente.**

| | **Transformador de dos devanados** | **AUTOTRANSFORMADOR** |
|---|---|---|
| **Devanados** | **Dos, separados** | **Uno, con toma intermedia** |
| **Aislamiento galvánico** | **SÍ** | **NO** |
| **Tamaño y coste para la misma potencia** | Mayor | **MENOR** |
| **Rendimiento** | Alto | **Aún más alto** |
| **Corriente de cortocircuito** | Limitada por su impedancia | **Mayor**, por su menor impedancia |
| **Relación de transformación práctica** | Cualquiera | **Mejor cuanto más próxima a uno** |

**Por qué es más pequeño para la misma potencia, que es la pregunta de fondo**: **porque sólo la parte
NO COMÚN del devanado transfiere potencia por inducción; el resto la transfiere por conducción
directa.** **La máquina sólo tiene que estar dimensionada para la parte inducida**, y **por eso el
ahorro es tanto mayor cuanto más parecidas son las dos tensiones.**

**Dónde se usa y dónde no:**

| Se usa | No se usa |
|---|---|
| **Adaptar 400 a 230 voltios o al revés** en tensiones próximas | **Donde haga falta aislamiento galvánico por seguridad** |
| **Arranque de motores** por reducción de tensión | **Donde el secundario deba tener otro régimen de neutro** |
| **Estabilizadores y reguladores de tensión** | **En equipos médicos o de medida que exijan separación** |

**La regla, en una línea**: **el autotransformador es un transformador barato al que se le ha quitado la
propiedad que a veces es la más importante.**

## 4. El acoplamiento en paralelo

**Cuándo se hace**: **cuando la potencia demandada supera a la de un transformador, o cuando se quiere
poder dejar uno fuera de servicio sin cortar el suministro.**

**Las CINCO condiciones para poder acoplar dos transformadores en paralelo, que es la lista más
preguntable del punto:**

| Condición | Qué pasa si no se cumple |
|---|---|
| **1 · Misma relación de transformación** | **Circula una corriente de circulación entre los dos, sin carga** |
| **2 · Igual tensión de cortocircuito** —la impedancia porcentual— | **El reparto de carga es desigual**: uno se sobrecarga antes que el otro |
| **3 · Mismo índice horario** o índices compatibles | **Hay desfase entre secundarios y circula una corriente muy alta** |
| **4 · Misma secuencia de fases** | **Igual: desfase y corriente de circulación** |
| **5 · Potencias no muy dispares** | El reparto se hace difícil de controlar; **la relación recomendada no supera 1 a 3** |

**Y la que decide de verdad el reparto, que es la segunda y hay que saber explicarla**: **la carga se
reparte en proporción INVERSA a la tensión de cortocircuito.** **El transformador con menor impedancia
se lleva más carga.** **Dos máquinas de la misma potencia con impedancias distintas no trabajan al
cincuenta por ciento**: **una llega a su límite mientras la otra va holgada, y el conjunto no puede
dar la suma de las dos.**

**La tercera es la que produce el accidente**: **el índice horario expresa el DESFASE entre la tensión
del primario y la del secundario**, en múltiplos de treinta grados. **Dos transformadores con índices
incompatibles puestos en paralelo ven entre sus secundarios una diferencia de tensión que sólo limita
su propia impedancia**, y **el resultado es una corriente de cortocircuito permanente.**

## 5. Las pérdidas y el rendimiento

**El enunciado nombra las pérdidas y hay que saber separarlas en dos familias, porque se comportan al
revés:**

| Familia | Dónde se producen | De qué dependen | Cómo se miden |
|---|---|---|---|
| **Pérdidas en el HIERRO o en VACÍO** | **En el núcleo**: histéresis y corrientes parásitas | **De la TENSIÓN y de la frecuencia**; **son prácticamente constantes** | **Ensayo de VACÍO** |
| **Pérdidas en el COBRE o en CARGA** | **En los devanados**, por efecto Joule | **Del CUADRADO de la corriente**: crecen con la carga | **Ensayo de CORTOCIRCUITO** |

**La consecuencia de oficio, y es la que explica el rendimiento de una instalación real**: **las
pérdidas en el hierro se pagan las veinticuatro horas del día, esté el transformador cargado o
vacío.** **Un transformador sobredimensionado para lo que se le pide gasta lo mismo en vacío que uno
bien elegido y aprovecha peor.**

**Y el punto de rendimiento máximo, que es el dato que un examen puede pedir**: **el rendimiento es
máximo cuando las pérdidas en el cobre IGUALAN a las del hierro.** **Como las del cobre crecen con el
cuadrado de la carga y las del hierro no, ese punto está por debajo de la plena carga.**

**Las dos pérdidas del hierro, que conviene distinguir:**

| Pérdida | Qué es | Cómo se reduce |
|---|---|---|
| **Por HISTÉRESIS** | **La energía que cuesta invertir la imanación del núcleo en cada ciclo** | **Con acero al silicio de grano orientado** |
| **Por CORRIENTES PARÁSITAS o de Foucault** | **Corrientes inducidas en la propia masa del núcleo** | **APILANDO CHAPAS finas AISLADAS entre sí**, en vez de un bloque macizo |

**La segunda explica un detalle constructivo que todo el mundo ha visto y pocos saben nombrar**: **el
núcleo de un transformador no es un bloque de hierro, es un paquete de chapas.** **Cada chapa está
barnizada y aislada de la vecina**, y **eso corta el camino a las corrientes que circularían por la
masa.**

**Los ensayos, que son la parte de mantenimiento del punto y enlazan con el tema 9:**

| Ensayo | Cómo se hace | Qué da |
|---|---|---|
| **De VACÍO** | **Secundario abierto, primario a tensión nominal** | **Pérdidas en el hierro y corriente de vacío** |
| **De CORTOCIRCUITO** | **Secundario cortocircuitado, primario a tensión reducida hasta la corriente nominal** | **Pérdidas en el cobre y TENSIÓN DE CORTOCIRCUITO** |
| **De relación de transformación** | Medida de tensiones en vacío | **Comprueba la relación y el índice horario** |
| **De aislamiento** | Megóhmetro entre devanados y a masa | **Estado del aislamiento** |
| **De rigidez del dieléctrico** | Sobre muestra de aceite, en los de aceite | **Envejecimiento y humedad del refrigerante** |

## 6. Los motores: tipos

**La clasificación que un técnico de instalaciones necesita, y no la del físico:**

| Familia | Cómo funciona | Dónde se encuentra |
|---|---|---|
| **ASÍNCRONO o de inducción, TRIFÁSICO** | **El estátor crea un campo giratorio; el rotor gira ARRASTRADO por él, siempre algo más despacio** | **El motor industrial por excelencia**: bombas, ventiladores, compresores, ascensores |
| **Asíncrono MONOFÁSICO** | Necesita **un artificio de arranque**: condensador o espira de sombra | Pequeña potencia: electrodomésticos, extractores |
| **SÍNCRONO** | **El rotor gira EXACTAMENTE a la velocidad del campo**, excitado en continua o con imanes | Grandes potencias, compensación de reactiva, generación |
| **De corriente CONTINUA** | Escobillas y colector; **par y velocidad fáciles de regular** | Tracción, servomecanismos; en retroceso frente al variador |
| **Paso a paso y servomotores** | **Posicionamiento controlado** | Automatismos, cabezas robotizadas, movimiento de cámara |

**El asíncrono trifásico se lleva el punto entero y hay que saber su vocabulario:**

| Concepto | Qué es |
|---|---|
| **Velocidad de SINCRONISMO** | **La del campo giratorio**: depende de la frecuencia y del número de pares de polos, **n = 60 · f / p** |
| **DESLIZAMIENTO** | **La diferencia relativa entre la velocidad de sincronismo y la real** |
| **Rotor de JAULA DE ARDILLA** | **Barras cortocircuitadas por dos anillos**: el más robusto y el más usado |
| **Rotor BOBINADO o de anillos rozantes** | **Devanado accesible desde fuera**: permite meter resistencias para el arranque |

**Y por qué el asíncrono NO puede girar a la velocidad de sincronismo, que es la pregunta conceptual
del punto**: **si girase a la misma velocidad que el campo, el rotor no vería un flujo variable**, y
**sin flujo variable no hay tensión inducida, sin tensión no hay corriente y sin corriente no hay
par.** **El motor gira porque va retrasado.** **Ésa es la razón del nombre y del deslizamiento.**

**El problema que todo lo demás resuelve: la CORRIENTE DE ARRANQUE.** **Un asíncrono de jaula
conectado directamente a la red absorbe en el arranque varias veces su corriente nominal**, y **eso
provoca caídas de tensión en la instalación, dispara protecciones y castiga la mecánica.**

## 7. El arranque estrella-triángulo y los demás

**El enunciado nombra expresamente la disposición estrella-triángulo**, y **se entiende con lo que el
tema 1 dejó dicho:**

| Fase | Conexión | Qué recibe cada devanado | Qué pasa |
|---|---|---|---|
| **Arranque** | **ESTRELLA** | **La tensión de línea dividida por raíz de tres** | **La corriente y el par bajan a UN TERCIO** |
| **Marcha** | **TRIÁNGULO** | **La tensión de línea entera** | **Régimen nominal** |

**Las tres cosas que hay que saber decir de este arranque:**

1. **Sólo es posible si el motor puede trabajar en TRIÁNGULO a la tensión de la red.** **La placa de
   características lo dice**: un motor de 400 voltios en triángulo se puede arrancar así en una red de
   400; uno de 400 en estrella, no.
2. **Reduce la corriente a un tercio, pero también el PAR a un tercio.** **No sirve para cargas que
   arrancan con par resistente alto**, y **un arranque en estrella que no consigue acelerar la carga
   es peor que no arrancar.**
3. **La conmutación produce un TRANSITORIO.** **Al pasar de estrella a triángulo hay un instante de
   desconexión y una punta de corriente**, y **la temporización del contactor de paso es lo que la
   limita.**

**El esquema de potencia son TRES contactores** —red, estrella y triángulo—, **con un enclavamiento
mecánico y eléctrico entre los dos últimos que impide que cierren a la vez**, porque **cerrar estrella
y triángulo simultáneamente es un cortocircuito franco entre fases.** **Ese enclavamiento es materia
del tema 3.**

**Los demás métodos de arranque, para completar el punto:**

| Método | Qué hace | Coste y complejidad |
|---|---|---|
| **Directo** | **Conexión a plena tensión** | El más barato; **sólo en motores pequeños o redes fuertes** |
| **Estrella-triángulo** | **Tensión reducida en dos escalones** | Barato; **par a un tercio** |
| **Por autotransformador** | **Tensión reducida en escalones elegibles** | Más caro; **más par que el anterior para la misma corriente** |
| **Por resistencias rotóricas** | **Sólo en rotor bobinado** | **Mucho par de arranque**, poco usado hoy |
| **ARRANCADOR PROGRESIVO** | **Rampa de tensión con electrónica** | **Sin escalones ni transitorios** |
| **VARIADOR DE FRECUENCIA** | **Cambia tensión Y frecuencia a la vez** | **El más caro y el único que regula la velocidad en marcha** |

**Y la observación que ordena la tabla y que hay que saber enunciar**: **los cuatro primeros métodos
sólo sirven para ARRANCAR; los dos últimos sirven además para GOBERNAR el motor.** **El variador es lo
único que cambia la velocidad de un asíncrono en servicio**, porque **la velocidad depende de la
frecuencia**, y **eso es lo que ha desplazado al motor de continua en casi todas partes.**

## 8. El guardamotor y la protección de la máquina

**El guardamotor es un interruptor automático MAGNETOTÉRMICO especialmente concebido para motores**, y
**hay que saber en qué se distingue de un magnetotérmico corriente:**

| Función | Guardamotor | Magnetotérmico de línea |
|---|---|---|
| **Protección térmica frente a SOBRECARGA** | **Sí, y REGULABLE** a la corriente nominal del motor | Fija, según el calibre |
| **Protección magnética frente a CORTOCIRCUITO** | **Sí, tarada alto** para tolerar la punta de arranque | Curva de línea, más sensible |
| **Maniobra manual** | **Sí**: sirve además de seccionamiento | Sí |
| **Detección de falta de fase** | **Sí, en los diferenciales de fase** | No |

**Los tres rasgos que lo definen y que hay que enunciar juntos:**

1. **La térmica es REGULABLE**, porque **el mismo aparato tiene que servir a motores de corriente
   nominal distinta dentro de un rango**, y **la protección de sobrecarga de un motor se ajusta a SU
   corriente de placa, no a la del cable.**
2. **La magnética está tarada MUY ALTA** —del orden de una docena de veces la nominal—, **porque si no
   dispararía en cada arranque.** **Ésa es la diferencia esencial con un magnetotérmico de línea.**
3. **Muchos incorporan detección de FALTA DE FASE**, que es la avería que más motores quema:
   **un motor trifásico al que le falta una fase sigue girando y absorbe por las dos restantes una
   corriente muy superior**, y **una térmica lenta puede no verlo a tiempo.**

**La alternativa clásica, que conviene saber nombrar**: **contactor más RELÉ TÉRMICO más fusibles.**
**El relé térmico hace la sobrecarga, los fusibles el cortocircuito y el contactor la maniobra.**
**El guardamotor reúne las tres funciones en un aparato**, y **por eso se ha impuesto en instalaciones
pequeñas y medianas.**

**Y las clases de disparo del relé térmico, que es el dato que un examen puede pedir**: **se designan
por el tiempo máximo de disparo a una sobrecarga determinada** —las clases 10, 20 y 30—, **y se elige
la clase por el TIEMPO DE ARRANQUE de la carga.** **Una carga de mucha inercia necesita una clase
alta, o la térmica dispara antes de que el motor haya llegado a su velocidad.**

**El aviso de instalación que cierra el punto**: **la protección del MOTOR y la protección de la LÍNEA
que lo alimenta son dos cosas distintas y las dos hacen falta.** **El guardamotor protege la máquina;
el cable se protege por su intensidad admisible**, y **eso es materia del tema 3 y del tema 5.**

## 9. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **hay que decir por qué**: **el enunciado de
este punto del anexo no nombra ninguna norma.** **Nombra materias de electrotecnia**, y **lo que se
desarrolla debajo es la teoría de máquinas eléctricas y el oficio de instalaciones.**

**Cinco declaraciones expresas:**

1. **No se ha consultado ningún tratado de máquinas eléctricas ni la documentación de ningún
   fabricante de transformadores, motores o aparamenta**, y **no se atribuye a ninguno nada de lo que
   aquí se dice.** **Lo que este tema contiene es teoría clásica de electrotecnia y oficio de
   instalaciones**, presentados como conocimiento común de la materia.
2. **Este tema NO da ninguna cifra de tarado, ningún múltiplo de corriente de arranque exacto,
   ninguna tabla de clases de disparo y ningún rendimiento.** **Son dato de producto y de
   fabricante**, y **una cifra que no se ha leído en su fuente no se escribe.** **Donde el temario
   necesita un orden de magnitud lo dice con esas palabras** —«varias veces», «del orden de una
   docena de veces»—, **y no como un valor.**
3. **Las fórmulas de este tema son física elemental y así se declaran**: la relación de
   transformación, la velocidad de sincronismo y el deslizamiento. **Ninguna se atribuye a una norma.**
4. **La reducción a un tercio de la corriente y del par en el arranque estrella-triángulo es
   aritmética** que sale de la relación de raíz de tres del tema 1: **el cuadrado de raíz de tres es
   tres.** **No es una afirmación de ninguna norma.**
5. **La norma que este tema nombra y no se cita aquí es el reglamento electrotécnico para baja
   tensión**, **cuya instrucción de receptores para motores fija los coeficientes de cálculo y las
   condiciones de arranque.** **Ese contenido se estudia en el tema 7 y en el tema 15**, y **aquí no
   se le atribuye ninguna cifra.**

**El resto del tema va como oficio y así se declara**: la lectura del enunciado como índice del punto,
las tres palabras que hacen exacta la definición de transformador, la explicación de que multiplicar
por diez la tensión divide por cien las pérdidas, los cuatro usos del aislamiento galvánico y en
particular la explicación del bucle de masa en una instalación de audio, el aviso de que un
autotransformador no aísla, la explicación de por qué el autotransformador es más pequeño, las cinco
condiciones de acoplamiento con la lectura de que la carga se reparte en proporción inversa a la
impedancia, la separación de las pérdidas en dos familias con su comportamiento opuesto, la
observación de que el hierro se paga las veinticuatro horas, la explicación del apilado de chapas, la
razón conceptual de que un asíncrono no pueda girar a sincronismo, las tres cosas que hay que saber
del arranque estrella-triángulo, la observación de que los cuatro primeros métodos sólo arrancan y los
dos últimos gobiernan, los tres rasgos del guardamotor y el aviso final de que la protección del motor
y la de la línea son dos cosas. **Nada de eso está en un boletín oficial ni en ninguna fuente
consultada para este proyecto**, y el tema no lo presenta como si lo estuviera.
