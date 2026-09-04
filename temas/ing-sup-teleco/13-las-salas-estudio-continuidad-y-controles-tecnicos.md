# Tema 13 del específico de Ingeniería Superior · Telecomunicación · Las salas: estudio de televisión, continuidades y controles técnicos

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · puntos 13, 14 y 15 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la arquitectura de las salas de una televisión, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Tres puntos en uno** | **Los enunciados 13, 14 y 15 son la misma frase con el nombre de la sala cambiado.** Separarlos daría tres temas que se repetirían |
| **Extensión** | **2.946 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: la unidad de control de cámara (**CCU**);
el visualizador bajo el monitor (**UMD**, *under monitor display*); la señalización de cámara en el
aire (**tally**); el protocolo de gestión de esas señalizaciones (**TSL**); la imagen dentro de imagen
(**PiP**); la matriz de teclado, vídeo y ratón (**KVM**); la interfaz digital en serie (**SDI**); la
candela por metro cuadrado (**cd/m²**), unidad de luminancia; el lumen (**lm**) y el lux (**lx**); el
sistema de alimentación ininterrumpida (**SAI**); la unidad de rack (**U**); y el sistema de
automatización de emisión (**playout**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, puntos 13, 14 y 15):
> «Elementos de producción (III): Estudio de televisión. Equipamiento. Diagrama a bloques.
> Interconexión. Sincronización y Referencia»
> «Elementos de producción (IV): Continuidades. Equipamiento. Diagrama a bloques. Interconexión.
> Sincronización y Referencia. Sistemas de automatización de emisión»
> «Elementos de producción (V): Controles técnicos y salas técnicas. Equipamiento. Diagrama a bloques.
> Interconexión. Dispositivos de presentación. Sistemas de Multipantalla. Equipos de monitoreado de
> vídeo. Monitores y medidores de vídeo.»

**Los tres puntos van en un solo tema y la unión se declara aquí, en la portada del volumen y en el
informe de refutación**: **son la MISMA FRASE con el nombre de la sala cambiado.** **Los tres piden
«equipamiento, diagrama a bloques e interconexión», y dos de ellos además «sincronización y
referencia».** **Escribir tres temas con la misma estructura sería decir tres veces lo mismo**, que es
lo que este proyecto prohíbe; **lo que cambia de una sala a otra es QUÉ hay dentro y PARA QUÉ**, y eso
es lo que el tema desarrolla sala por sala. **No se recorta contenido: los tres enunciados van
desarrollados enteros.**

**Y la idea que ordena el tema**: **una casa que emite es un conjunto de salas conectadas por una
matriz y sincronizadas por una referencia común.** **Cambia lo que cada sala hace; no cambia esa
arquitectura.**

<!-- indice -->

## Índice

- [1. La arquitectura común](#1-la-arquitectura-común)
- [2. El estudio de televisión](#2-el-estudio-de-televisión)
- [3. Las continuidades](#3-las-continuidades)
- [4. Los controles técnicos y las salas técnicas](#4-los-controles-técnicos-y-las-salas-técnicas)
- [5. La interconexión y los puestos de trabajo](#5-la-interconexión-y-los-puestos-de-trabajo)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. La arquitectura común

**Antes de mirar ninguna sala, lo que todas comparten:**

| Elemento común | Qué es |
|---|---|
| **REFERENCIA de sincronismo** | **Una sola por instalación**, distribuida a todo lo que genera señal |
| **MATRIZ de encaminamiento** | **El sistema nervioso**: qué señal llega a qué sala |
| **INTERCOMUNICACIÓN** | **Órdenes y coordinación**: es lo que hace posible el directo |
| **SEÑALIZACIÓN de cámara en el aire** | **Quién está emitiendo**, en la cámara y en los monitores |
| **CÓDIGO DE TIEMPO** | La referencia temporal común |
| **MONITORADO** | **Multipantallas y monitores de referencia** |
| **ALIMENTACIÓN protegida** | **Sistema ininterrumpido y grupo**: la continuidad eléctrica |
| **CLIMATIZACIÓN** | **Sin frío no hay sala técnica**, y va en el suministro protegido |

**Y las dos reglas de arquitectura que hay que llevar aprendidas:**

1. **Una sola referencia y una sola matriz.** **Dos referencias independientes producen deslizamiento;
   dos matrices sin pasarela producen islas.** **Toda la instalación cuelga de esas dos decisiones.**
2. **La climatización es parte del sistema, no del edificio.** **Una sala técnica sin frío se apaga en
   minutos**, y **por eso la refrigeración de las salas críticas va en el suministro protegido, no en
   el general.** **Es el olvido clásico y sale caro.**

## 2. El estudio de televisión

**La sala donde se produce.** **Y hay que empezar por la aclaración de vocabulario que un examen
pregunta**: **«plató» y «estudio» no son lo mismo en el uso profesional**: **el plató es el espacio de
grabación con su decorado y su parrilla; el estudio es el conjunto de plató más sus controles.**

**Los espacios de un estudio y qué se hace en cada uno**, que es la pregunta directa:

| Espacio | Qué se hace |
|---|---|
| **PLATÓ** | **Se graba**: decorado, cámaras, luz, sonido, intérpretes |
| **CONTROL DE REALIZACIÓN** | **Se SUPERVISA Y SE DECIDE qué imágenes forman parte de la grabación o de la emisión** |
| **CONTROL DE CÁMARAS o de imagen** | **Se expone y se iguala** la imagen de todas las cámaras |
| **CONTROL DE SONIDO** | Se mezcla el audio |
| **CONTROL DE ILUMINACIÓN** | Se lanzan y se ajustan los estados de luz |
| **Sala de equipos** | **Donde viven los racks**: unidades de control, matrices, servidores |

**La segunda fila es la respuesta a la pregunta del cuadernillo**: **la sección donde se supervisa y se
decide qué imágenes formarán parte de la grabación o de la emisión es el CONTROL DE REALIZACIÓN.** **No
el control de imagen, que ajusta y no decide; ni una cabina de grabación o de edición, que trabajan
sobre material ya registrado.**

**El equipamiento del control de realización:**

| Equipo | Qué hace |
|---|---|
| **MEZCLADOR de producción** | Barras de programa y previo, transiciones, incrustadores y efectos |
| **MULTIPANTALLA** | **Todas las fuentes a la vista a la vez** |
| **Monitores de programa y previo** | **Los dos que importan**, de mayor tamaño |
| **Servidores de vídeo y repetición** | Lanzar y repetir |
| **Generador de rótulos** | Materia del tema 16 |
| **Intercomunicación** | Con plató, cámaras y controles |

**Y el equipamiento del control de cámaras, con la observación que un examen premia:**

| Equipo | Qué hace |
|---|---|
| **Paneles de control remoto** | **Uno por cámara**: diafragma, negros, ganancia |
| **Panel maestro** | Configuración fina y matriz de color |
| **MONITOR DE REFERENCIA de la instalación** | **El monitor de más calidad de toda la casa** |
| **Monitor de forma de onda y vectorscopio** | **La medida objetiva** que acompaña al ojo |

**La pregunta es cuál de los controles usa los monitores de mayor calidad, y la respuesta es el CONTROL
DE CÁMARAS.** **La razón hay que saber decirla**: **es el único puesto donde se juzga la IMAGEN en sí
misma** —exposición, color, ruido, detalle—, y **eso exige un monitor calibrado y de referencia.** **En
realización se juzga QUÉ se ve, no CÓMO está**: sus monitores tienen que ser muchos y fiables, no de
referencia. **En sonido e iluminación, el monitor es informativo.**

**La sincronización y la referencia en un estudio**, que los enunciados piden expresamente: **todo lo
que genera señal —cámaras, servidores, generadores de rótulos, mezclador— recibe la misma referencia**,
y **todo lo que entra de fuera pasa por un sincronizador de cuadro.** **Sin eso, cada conmutación
salta.**

## 3. Las continuidades

**La sala desde la que se EMITE**, y **hay que decir en qué se distingue del estudio**: **el estudio
produce contenido; la continuidad monta la emisión.** **Su producto no es un programa: es la cadena de
veinticuatro horas.**

**Su equipamiento:**

| Equipo | Qué hace |
|---|---|
| **Mezclador de continuidad** | **Encadena las fuentes de emisión** con transiciones sencillas |
| **SERVIDORES de emisión** | **Reproducen lo grabado** según la lista |
| **SISTEMA DE AUTOMATIZACIÓN** | **Ejecuta la escaleta**: qué se emite, cuándo y durante cuánto |
| **Generador de mosca y de rótulos de continuidad** | La identidad de canal en pantalla |
| **Insertadores de subtítulos y de audiodescripción** | **Accesibilidad**, que es exigencia legal |
| **Multipantalla de emisión** | **Lo que sale, lo que va a salir y las alarmas** |
| **Vigilancia de emisión** | **Comprobación automática de que hay señal y de que es la correcta** |

**El SISTEMA DE AUTOMATIZACIÓN DE EMISIÓN, que el enunciado nombra expresamente**, con **las cinco
cosas que hay que saber de él:**

1. **Trabaja sobre una LISTA con tiempos.** **Cada elemento tiene su hora, su duración y su fuente**,
   y **el sistema los encadena solo.**
2. **Manda sobre los demás equipos.** **Arranca servidores, mueve el mezclador, dispara rótulos y
   conmuta audio**, y **por eso está en el centro y no al lado.**
3. **Convive con el DIRECTO.** **Cuando entra un informativo, la automatización cede y espera**, y
   **volver a engancharse con la escaleta después es la maniobra delicada.**
4. **Tiene modos de degradación.** **Automático, semiautomático y manual**, y **el operador tiene que
   poder tomar el mando en cualquier momento.**
5. **Su fallo es un fallo de EMISIÓN.** **Por eso las continuidades se montan REDUNDADAS**: cadena
   principal y cadena de reserva, con conmutación entre ellas.

**Y la observación que resume la sala**: **una continuidad se juzga por lo que NO pasa.** **Su trabajo
bien hecho es invisible**, y **su único indicador de calidad es la ausencia de negro en antena.**

## 4. Los controles técnicos y las salas técnicas

**Lo que el enunciado nombra en tercer lugar**, y **que es donde vive la infraestructura:**

| Sala | Qué contiene |
|---|---|
| **Control CENTRAL** | **El puesto que ajusta las cámaras y la calidad técnica de todo lo que entra y sale**; supervisa la instalación |
| **Sala de MATRIZ y de equipos** | **La matriz principal, los sincronizadores, los conversores y la distribución** |
| **Sala de SERVIDORES y almacenamiento** | Tema 18 |
| **Sala de INTERCAMBIOS** | **Recepción y envío de señales de fuera**: satélite, fibra, agencias |
| **Sala de RED** | Tema 20 |
| **Sala de ENERGÍA** | Sistemas ininterrumpidos y cuadros |

**Los DISPOSITIVOS DE PRESENTACIÓN y el sistema de multipantalla**, que el enunciado pide:

| Concepto | Qué es |
|---|---|
| **MULTIPANTALLA** | **Un procesador que compone muchas fuentes en una sola pantalla grande** |
| **Ventana** | **Cada fuente dentro de esa composición** |
| **Visualizador bajo el monitor** | **El TEXTO debajo de cada ventana que dice qué señal es** |
| **Señalización en el aire** | **El indicador de que esa fuente está en programa** |
| **Imagen dentro de imagen** | **Una imagen pequeña superpuesta a otra**: es otra cosa |
| **Alarmas y medidores embebidos** | **Nivel de audio, pérdida de señal, congelación**, sobre cada ventana |

**La pregunta directa del cuadernillo**: **el texto que va debajo de la imagen, en un monitor o dentro
de un patrón de multipantallas, y que sirve para nombrar la señal que se está viendo, se llama
VISUALIZADOR BAJO EL MONITOR.** **No imagen dentro de imagen, que es una ventana superpuesta; ni
señalización en el aire, que es el indicador de emisión; ni el protocolo que gestiona esas
señalizaciones, que es un protocolo y no un elemento de pantalla.** **Confundir el rótulo con el
protocolo que lo alimenta es el error que esa pregunta busca.**

**Los MONITORES, y la unidad en que se mide lo que emiten**, que es otra pregunta directa:

| Magnitud | Unidad | Qué mide |
|---|---|---|
| **LUMINANCIA** | **Candela por metro cuadrado** | **La luz que EMITE una superficie**: es lo que da un monitor |
| **Flujo luminoso** | **Lumen** | Lo que emite una fuente en total |
| **Iluminancia** | **Lux** | **La luz que LLEGA a una superficie** |
| **Paso de diafragma** | — | **Una relación, no una unidad de luz** |

**La regla que las separa y que hay que llevar aprendida**: **el lux es lo que RECIBE una superficie y
la candela por metro cuadrado es lo que EMITE.** **Un monitor emite, así que su brillo se mide en
candelas por metro cuadrado**; **un plató se ilumina, así que su nivel se mide en lux.** **Y el paso de
diafragma no es una unidad de luz: es una relación entre dos cantidades.**

**Y las clases de monitor de una casa, con su uso:**

| Clase | Para qué |
|---|---|
| **De REFERENCIA** | **Juzgar la imagen**: calibrado, con su rango y su espacio de color declarados |
| **De producción** | **Ver bien y fiable**, en realización |
| **De multipantalla** | **Muchas fuentes a la vez**: prima la información, no la fidelidad |
| **De sala y de público** | Informativo |

**Y la regla de calibración que cierra el epígrafe**: **un monitor de referencia sin calibrar no es de
referencia.** **La calibración tiene fecha y se repite**, y **un monitor que nadie calibra es un
monitor de producción caro.**

## 5. La interconexión y los puestos de trabajo

**Cómo se conectan las salas entre sí:**

| Vía | Qué lleva |
|---|---|
| **MATRIZ de vídeo y audio** | **Las señales de programa y de fuentes** |
| **Red de datos** | **Ficheros, control y hoy también medios** |
| **Referencia y código de tiempo** | **Distribuidos a todas** |
| **Intercomunicación** | Órdenes |
| **Señalización de cámara en el aire** | Estados |
| **Matriz de teclado, vídeo y ratón** | **Los puestos informáticos** |

**La última merece explicación porque es la pregunta con esquema del cuadernillo**: **cuando varios
técnicos tienen que poder trabajar con CUALQUIERA de varias estaciones de trabajo, lo que hace falta es
una MATRIZ de teclado, vídeo y ratón.**

**Y hay que razonar por qué las otras opciones no**: **un EXTENSOR lleva un puesto a distancia, uno a
uno, y no permite elegir máquina; un distribuidor de una interfaz de monitor reparte imagen pero no
lleva teclado ni ratón; y un concentrador de bus multiplica puertos en una sola máquina.** **La palabra
clave del enunciado es «cualquiera de»**: **eso es conmutación de muchos a muchos, y eso es una
matriz.**

**Y las tres ventajas de esa arquitectura que un ingeniero tiene que saber defender:**

1. **Las máquinas viven en la sala técnica**, refrigeradas, protegidas y sin ruido en el puesto.
2. **Cualquier puesto sirve para cualquier tarea**, y **una avería de puesto no para el trabajo: se
   cambia de sitio.**
3. **El acceso se controla y se registra**, que es materia del tema 25.

## 6. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Estos tres puntos no nombran ninguna norma y no hay ninguna que los sostenga** |

**El aviso de método sobre estos puntos sin norma es el del tema 3 y vale aquí.**

**Seis declaraciones expresas:**

1. **Este tema desarrolla TRES puntos del anexo —el 13, el 14 y el 15— y la unión va declarada.**
   **El motivo es que los tres enunciados son la misma frase con el nombre de la sala cambiado**, y
   **no se ha recortado contenido**: **el estudio va en el epígrafe 2, las continuidades y la
   automatización de emisión en el 3, y los controles técnicos con sus dispositivos de presentación y
   su multipantalla en el 4.** **La sincronización y la referencia, que dos de los tres piden
   expresamente, van en el epígrafe 1 y se retoman en el 2.**
2. **Este tema NO da ninguna cifra de luminancia de monitor, ningún nivel de iluminación de plató,
   ninguna temperatura de sala, ninguna potencia de alimentación protegida y ningún tiempo de
   autonomía.** **Son dato de recomendación y de proyecto**, y **una cifra que no se ha leído en su
   fuente no se escribe.**
3. **Las cuatro respuestas que la plantilla oficial de esta ocupación confirma —el control de
   realización como la sección que decide, el control de cámaras como el de los monitores de mayor
   calidad, el visualizador bajo el monitor como el rótulo de identificación y la matriz de teclado,
   vídeo y ratón para trabajar con cualquiera de varias estaciones— se recogen con su razonamiento**,
   y **el temario declara que la confirmación viene de la plantilla, en las preguntas 69, 71, 29 y
   37.**
4. **La unidad de la luz que emite un monitor —la candela por metro cuadrado— la confirma la plantilla
   en la pregunta 19**, y **el temario añade la regla que la separa del lux**, que **es lectura
   propia.**
5. **La pregunta 37 del cuadernillo se apoya en un ESQUEMA que este temario NO ha visto y NO
   describe.** **Lo que aporta es el razonamiento por el enunciado escrito** —«cualquiera de las
   estaciones de trabajo»—, **que basta para resolverla**, y **el banco la deja marcada.**
6. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **las cámaras
   y la conmutación, al tema 11**; **la medida y el equipamiento auxiliar, al tema 12**; **los
   informativos, al tema 14**; **la postproducción, al tema 15**; **el grafismo, al tema 16**; **el
   almacenamiento, al tema 18**; **la red, al tema 20**; **y la instalación, al tema 24.**

**El resto del tema va como oficio y así se declara**: la idea de que una casa que emite es un conjunto
de salas conectadas por una matriz y sincronizadas por una referencia común, las dos reglas de
arquitectura con el aviso sobre la climatización en el suministro protegido, la aclaración entre plató
y estudio, el razonamiento de por qué los monitores de referencia están en el control de cámaras, la
caracterización de la continuidad como la sala que monta la cadena de veinticuatro horas, las cinco
cosas que hay que saber de un sistema de automatización de emisión, la observación de que una
continuidad se juzga por lo que no pasa, la distinción entre el rótulo bajo el monitor y el protocolo
que lo alimenta, la regla de que el lux se recibe y la candela por metro cuadrado se emite, la regla de
que un monitor de referencia sin calibrar no lo es, el razonamiento sobre la matriz de puestos frente a
extensor, distribuidor y concentrador, y las tres ventajas de esa arquitectura. **Nada de eso está en
un boletín oficial ni en ninguna fuente consultada para este proyecto**, y el tema no lo presenta como
si lo estuviera.
