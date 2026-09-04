# Tema 6 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Instalaciones de enlace y centros de transformación

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Téc. Equipos, Instalaciones y Sistemas Eléctricos · punto 6 |
| **Sirve para** | **Téc. Equipos, Instalaciones y Sistemas Eléctricos** |
| **Fuente** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** |
| **Identificador** | `BOE-A-2002-18099` · BOE núm. 224, de 18/09/2002 |
| **Redacción que se estudia** | La vigente el **21/12/2022**. Se cita **el apartado 1.1 de la ITC-BT-12** |
| **Aviso de estudio** | **El enunciado junta dos cosas que están en DOS REGLAMENTOS DISTINTOS**: el enlace en el de baja tensión y el centro de transformación en el de alta, que aquí se nombra y no se cita |
| **Extensión** | **2.542 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el reglamento electrotécnico para baja tensión
(**REBT**) y sus instrucciones (**ITC-BT-10** a **ITC-BT-17**); la caja general de protección
(**CGP**); la línea general de alimentación (**LGA**); la centralización de contadores (**CC**); la
derivación individual (**DI**); el interruptor de control de potencia (**ICP**); el cuadro general de
mando y protección (**CGMP**); el interruptor general automático (**IGA**); el reglamento de
instalaciones eléctricas de alta tensión (**RAT**) y sus instrucciones (**ITC-RAT 01** a
**ITC-RAT 23**); el reglamento de líneas eléctricas de alta tensión (**LAT**); el kilovoltio (**kV**)
y el kilovoltamperio (**kVA**); y el centro de transformación (**CT**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación
> tipo de Técnica de Equipos, Instalaciones y Sistemas Eléctricos, punto 6):
> «Instalaciones eléctricas de enlace y centros de transformación.»

**El enunciado junta dos cosas que están en DOS REGLAMENTOS DISTINTOS**, y **eso hay que decirlo antes
de nada, porque es la clave de estudio del punto:**

| Mitad del enunciado | Qué reglamento la gobierna |
|---|---|
| **Instalaciones de ENLACE** | **El reglamento electrotécnico para BAJA tensión**, con sus instrucciones ITC-BT-11 a ITC-BT-17 |
| **CENTROS DE TRANSFORMACIÓN** | **El reglamento de instalaciones eléctricas de ALTA tensión**, el Real Decreto 337/2014, y su acometida, el de líneas de alta tensión |

**Y la frontera entre las dos está exactamente donde el enunciado no la dibuja**: **el centro de
transformación es la puerta por la que la alta tensión entra en la casa, y el enlace es lo que
distribuye la baja desde ahí.** **Uno acaba donde empieza el otro.**

**El caso de una corporación audiovisual es el más completo de los dos posibles**, y conviene decirlo:
**un centro de producción grande no se alimenta de la red de baja tensión de la calle, sino que tiene
su PROPIO centro de transformación.** **Eso cambia el punto de origen de la instalación interior, con
las consecuencias de caída de tensión que el tema 5 ha citado, y mete a esta ocupación en el
reglamento de alta tensión.**

<!-- indice -->

## Índice

- [1. Qué es una instalación de enlace](#1-qué-es-una-instalación-de-enlace)
- [2. Los esquemas de enlace](#2-los-esquemas-de-enlace)
- [3. Las partes, una a una](#3-las-partes-una-a-una)
- [4. El centro de transformación](#4-el-centro-de-transformación)
- [5. Trazabilidad](#5-trazabilidad)

<!-- /indice -->

## 1. Qué es una instalación de enlace

**La definición, citada:**

> «**Se denominan instalaciones de enlace, aquellas que unen la caja general de protección o cajas
> generales de protección, incluidas éstas, con las instalaciones interiores o receptoras del usuario.
> Comenzarán, por tanto, en el final de la acometida y terminarán en los dispositivos generales de
> mando y protección.
> Estas instalaciones se situarán y discurrirán siempre por lugares de uso común y quedarán de
> propiedad del usuario, que se responsabilizará de su conservación y mantenimiento.**»
>
> — Real Decreto 842/2002, **ITC-BT-12**, apartado 1.1 (`BOE-A-2002-18099`), redacción vigente el 21
> de diciembre de 2022.

---

**Tres cosas que hay que leer en esa definición, y las tres se preguntan:**

1. **Dónde EMPIEZA y dónde ACABA**: **empieza al final de la acometida —en la caja general de
   protección, que va incluida— y acaba en los dispositivos generales de mando y protección.**
2. **Por dónde VA**: **siempre por lugares de USO COMÚN.** **Una derivación individual que atraviesa
   la vivienda de otro no cumple.**
3. **De quién ES**: **del USUARIO**, que responde de su conservación y mantenimiento. **La acometida,
   en cambio, es de la distribuidora.** **Ésa es la frontera de propiedad y de responsabilidad, y es
   lo primero que hay que saber ante una avería.**

**Las partes que la componen, tal como la instrucción las enumera:**

| Parte | Qué es |
|---|---|
| **Caja general de protección** | **Aloja los fusibles de protección de la línea general** y marca **el final de la acometida** |
| **Línea general de alimentación** | **De la caja general a la centralización de contadores** |
| **Elementos para la ubicación de contadores** | **La centralización o el armario de medida** |
| **Derivación individual** | **De los contadores al cuadro de cada usuario** |
| **Caja para el interruptor de control de potencia** | El alojamiento del limitador |
| **Dispositivos generales de mando y protección** | **El cuadro del usuario**, donde acaba el enlace |

**La ACOMETIDA no es parte del enlace y hay que decirlo, porque es la confusión clásica**: **es la
parte de la red de distribución que alimenta la caja general de protección**, y **es de la
distribuidora.** **Sus tipos, según la instrucción de acometidas**: **aérea posada sobre fachada,
aérea tensada sobre poste, subterránea y aero-subterránea.**

## 2. Los esquemas de enlace

**La instrucción de esquemas distingue por el NÚMERO DE USUARIOS**, y **de ahí salen las dos familias
que hay que saber dibujar:**

| Esquema | Cuándo | Cómo es |
|---|---|---|
| **Para UN SOLO usuario** | **Una vivienda unifamiliar, una nave, un centro de trabajo con un solo suministro** | **La caja general de protección y el equipo de medida se unen en una sola envolvente**, la caja de protección y medida, **y NO existe línea general de alimentación** |
| **Para MÁS DE UN usuario** | Edificios de viviendas, locales, oficinas | **Caja general, línea general, centralización de contadores y una derivación individual por usuario** |

**La observación que hay que hacer sobre el primero y que un examen puede pedir**: **cuando hay un solo
usuario, la línea general de alimentación DESAPARECE**, porque **no hay nada que repartir entre
varios.** **La caja de protección y medida hace las dos funciones y la derivación individual sale
directamente de ella.**

**Y las tres variantes del segundo, que la instrucción distingue**: **contadores para dos usuarios
alimentados desde el mismo lugar**, **centralización en UN lugar** y **centralización en MÁS DE UN
lugar.** **La elección depende del tamaño del edificio y del número de plantas**, y **la
reglamentación fija cuándo se puede centralizar en varios sitios.**

## 3. Las partes, una a una

**La CAJA GENERAL DE PROTECCIÓN**, con las tres cosas que hay que saber:

| Qué | Cómo |
|---|---|
| **Qué contiene** | **Los fusibles de protección de la línea general de alimentación**, uno por fase |
| **Dónde se sitúa** | **En la fachada o en un nicho**, **de libre y permanente acceso**, lo más cerca posible de la red |
| **De quién es** | **La instalación es del usuario; la maniobra de sus fusibles, de la distribuidora** |

**La LÍNEA GENERAL DE ALIMENTACIÓN**, y **su rasgo característico, que es lo que se pregunta**: **NO
lleva protección propia en su origen distinta de los fusibles de la caja general**, y **por eso se
dimensiona para la máxima demanda prevista de todo el edificio.** **Su sección se calcula con los
criterios del tema 5 y con los coeficientes de simultaneidad que la instrucción de previsión de cargas
fija.**

**La CENTRALIZACIÓN DE CONTADORES**, y **las cuatro unidades funcionales que la componen**:
**interruptor general de maniobra, embarrado general y fusibles de seguridad, medida, y embarrado de
protección y bornes de salida.** **Y la regla de acceso, que es de mantenimiento**: **el local o
armario tiene que ser accesible desde zona común y estar dedicado a esto.**

**La DERIVACIÓN INDIVIDUAL**, y **los dos rasgos que la distinguen de cualquier otra línea:**

1. **Es INDIVIDUAL**: **una por usuario, sin derivaciones intermedias.**
2. **Lleva SIEMPRE el conductor de PROTECCIÓN**, además de fases y neutro, **y un hilo de mando para
   la tarificación cuando la instalación lo requiere.**

**Y el aviso de proyecto que la instrucción impone sobre su recorrido**: **discurre por zona común, en
tubo o canal que permita retirar y reponer los cables**, y **con registros en cada planta.**

**Los DISPOSITIVOS GENERALES DE MANDO Y PROTECCIÓN, que cierran el enlace y abren la instalación
interior**, con los cuatro que siempre están:

| Dispositivo | Qué hace |
|---|---|
| **Interruptor general automático** | **Corte omnipolar y protección de la derivación individual**; **es del usuario** |
| **Interruptor diferencial** | **Protección contra contactos indirectos**, uno o varios |
| **Interruptores automáticos de cada circuito** | **Protección de cada línea interior** |
| **Protector contra sobretensiones**, cuando procede | Sobretensiones transitorias y permanentes |

**Y el interruptor de CONTROL DE POTENCIA, que se confunde con el general y no es lo mismo**: **el de
control de potencia limita la potencia CONTRATADA y es de la distribuidora; el general automático
protege la instalación y es del usuario.** **Uno es de facturación y el otro es de seguridad.**

## 4. El centro de transformación

**Aquí cambia el reglamento y hay que decirlo**: **un centro de transformación es una instalación de
ALTA tensión** y **se rige por el Real Decreto 337/2014 y sus instrucciones técnicas**, **no por el
reglamento electrotécnico para baja tensión.**

**Qué es**: **la instalación que recibe energía en alta tensión, la transforma a baja y la entrega a la
instalación de enlace o directamente a la interior.**

**Sus partes, de la entrada a la salida:**

| Parte | Qué es |
|---|---|
| **Celdas de LÍNEA o de entrada** | **Reciben la alta tensión** y permiten seccionar |
| **Celda de PROTECCIÓN del transformador** | **Con interruptor-seccionador y fusibles, o con interruptor automático** |
| **Celda de MEDIDA**, cuando la medida es en alta | Transformadores de tensión y de intensidad |
| **TRANSFORMADOR o transformadores** | **De potencia**, en aceite o secos |
| **Cuadro de BAJA tensión** | **Salidas protegidas hacia la instalación** |
| **Puestas a TIERRA** | **Dos**: la de PROTECCIÓN de masas y la de SERVICIO del neutro |
| **Servicios auxiliares** | Alumbrado, alumbrado de emergencia, enclavamientos |

**Las dos tierras son el asunto característico del centro de transformación**, y **hay que saber por
qué son dos y por qué se separan**: **la tierra de protección recoge las masas del centro; la tierra
de servicio es la del neutro de baja tensión.** **Si se unen, una corriente de defecto en alta hace
subir el potencial de la tierra de protección**, y **ese potencial aparecería directamente en el
neutro de toda la instalación de baja.** **Por eso la instrucción de puesta a tierra del reglamento de
baja tensión dedica un apartado entero a la SEPARACIÓN entre las tomas de tierra de las masas de las
instalaciones de utilización y las masas de un centro de transformación.**

**Los tipos de centro, por su emplazamiento:**

| Tipo | Dónde |
|---|---|
| **De intemperie sobre apoyo** | Pequeñas potencias, medio rural |
| **En EDIFICIO prefabricado** | Vía pública y polígonos |
| **En LOCAL, integrado en el edificio** | **El caso de un centro de trabajo grande** |
| **SUBTERRÁNEO** | Suelo urbano denso |

**Y por su régimen de propiedad, que es la distinción que decide quién mantiene:**

| Régimen | Quién lo explota |
|---|---|
| **De COMPAÑÍA** | **La distribuidora**, que entrega en baja tensión |
| **De ABONADO o de cliente** | **El titular de la instalación**, que recibe en alta |

**El segundo es el de una corporación audiovisual con centros grandes**, y **arrastra tres
consecuencias que hay que saber enumerar:**

1. **El titular responde del mantenimiento del centro**, con sus revisiones e inspecciones
   reglamentarias, **y eso es materia del tema 9.**
2. **El origen de la instalación interior de baja tensión se traslada a la SALIDA del transformador**,
   con los límites de caída de tensión del 4,5 y el 6,5 por ciento que el tema 5 cita.
3. **Los trabajos en el centro son trabajos en ALTA TENSIÓN**, con el régimen de riesgo eléctrico que
   el tema 14 desarrolla y con personal cualificado y autorizado.

**Los enclavamientos de un centro de transformación merecen su párrafo**, porque **son la aplicación
más estricta de lo que el tema 3 dijo**: **la secuencia de maniobra está impuesta físicamente por
cerraduras y varillas**, de modo que **no se puede abrir la puerta de la celda del transformador sin
haber puesto antes a tierra**, ni **cerrar el seccionador de puesta a tierra con el interruptor
cerrado.** **El enclavamiento no es una recomendación de procedimiento: es una pieza de metal que
impide el orden equivocado.**

## 5. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 842/2002, de 2 de agosto, por el que se aprueba el Reglamento electrotécnico para baja tensión y sus instrucciones técnicas complementarias** (`BOE-A-2002-18099`), **en su redacción vigente el 21 de diciembre de 2022** | **De la ITC-BT-12**, el apartado 1.1 entero |

**El aviso de método sobre las citas de instrucción técnica es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **La segunda mitad de este punto —los centros de transformación— se rige por el REAL DECRETO
   337/2014**, de instalaciones eléctricas de alta tensión, **y por el REAL DECRETO 223/2008**, de
   líneas de alta tensión. **Los dos están volcados en este proyecto y citados en el temario de
   Ingeniería Técnica · Industrial**, y **aquí NO se cita ninguno**: **su contenido se resume y sus
   materias se identifican.** **El temario no le atribuye a ninguno de los dos ninguna cifra ni
   ninguna prescripción concreta.**
2. **Este tema NO da ninguna sección mínima, ninguna cifra de previsión de cargas, ningún coeficiente
   de simultaneidad, ninguna distancia y ninguna resistencia de tierra.** **Están en las tablas de las
   instrucciones técnicas**, y **una cifra que no se ha leído en su fuente no se escribe.**
3. **Los apartados que se resumen y no se citan van identificados uno a uno** —de la ITC-BT-11, el
   1.1 y el 1.2; de la ITC-BT-12, el 1.2 y el 2 con sus variantes; de la ITC-BT-13, la caja general
   de protección; de la ITC-BT-14, la línea general de alimentación; de la ITC-BT-15, la derivación
   individual; de la ITC-BT-16, la ubicación de contadores; de la ITC-BT-17, los dispositivos
   generales de mando y protección; de la ITC-BT-18, el apartado 11, de separación entre tomas de
   tierra—. **Todos están en la norma citada arriba.**
4. **La descripción de las partes de un centro de transformación es OFICIO de instalaciones** y así se
   declara: **el temario no la atribuye a ninguna instrucción técnica del reglamento de alta
   tensión**, que **no se ha consultado para este tema.**
5. **Los dos porcentajes de caída de tensión que este tema menciona —4,5 y 6,5— están citados
   literalmente en el tema 5 de este mismo específico**, y **aquí se remiten, no se vuelven a citar.**

**El resto del tema va como oficio y así se declara**: la lectura de que el enunciado junta dos
reglamentos y dónde está la frontera, el caso de una corporación con centro de transformación propio,
las tres cosas que hay que leer en la definición de instalación de enlace, el aviso de que la
acometida no es enlace y es de la distribuidora, la observación de que la línea general desaparece
cuando hay un solo usuario, los dos rasgos de la derivación individual, la distinción entre el
interruptor de control de potencia y el general automático, la explicación de por qué las dos tierras
del centro de transformación se separan, las tres consecuencias de tener centro propio y la lectura
del enclavamiento como pieza de metal y no como procedimiento. **Nada de eso lo dice la norma con esas
palabras**, y el tema no lo presenta como si lo dijera.
