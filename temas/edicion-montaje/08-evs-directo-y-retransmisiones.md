# Tema 8 del específico de Edición, Montaje y Procesos Audiovisuales · Edición en directo y retransmisiones (EVS)

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 8 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Sin norma: no la hay.** Su materia es el manejo de un sistema comercial de repetición y edición en directo, que **el anexo sí nombra por su marca** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Las nueve preguntas de este punto descansan en la plantilla oficial**: la documentación del fabricante no se ha consultado. **Cinco de las nueve, sin embargo, se razonan** con la arquitectura del sistema, y el tema la desarrolla |
| **Extensión** | **3.260 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: la marca belga que da nombre al sistema (**EVS**),
que el propio anexo del temario escribe así y que no desarrolla nada en el enunciado; el mando de
repetición y cámara lenta (**LSM**,
*live slow motion*), y la familia de servidores **XT** sobre la que corre; la interfaz digital serie
de transporte de datos (**SDTI**, *serial data transport interface*), que es la red por la que los
servidores se ven entre sí; la salida de programa (**PGM**) y la de previo (**PRV**); la pantalla del
adaptador gráfico de vídeo (**VGA**) y el grabador digital de vídeo (**VDR**, *video disk recorder*),
que dan nombre al panel de servicio; la pantalla de cristal líquido (**LCD**) del mando; la interfaz
digital serie (**SDI**); y las teclas de función del teclado (**F1** a **F12**).

**Y una advertencia sobre el rótulo de las órdenes.** El cuadernillo escribe en mayúsculas los
nombres de los mandos y de las funciones del sistema, y este tema los reproduce tal cual porque **la
respuesta oficial depende del rótulo exacto**: **TAKE**, la tecla que intercambia; **AUX**, el
auxiliar; **CAM**, la selección de cámara; **PLAYLIST**, la lista de reproducción; **TIMELINE**, la
línea de tiempo; y **LINK**, **GANG**, **TWICE** y **DUAL**, las cuatro opciones de una de las
preguntas. **No son siglas: son los rótulos del sistema.**

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, punto 5.8):
> «Sistemas de edición para producciones en directo y retransmisiones. (EVS).»

**Nueve preguntas de un subpunto que ocupa una línea del programa** —y que **nombra la marca**, cosa
que el anexo no hace con ninguna otra—. **Las nueve son de manejo de máquina**, y **las nueve
descansan en la plantilla oficial**: la documentación del fabricante no se ha consultado.

**Lo que este tema aporta**, y es lo que las hace estudiables: **la arquitectura del sistema y el
porqué de cada respuesta**. Un mando de repetición no se aprende de memoria en una lista: se aprende
sabiendo **cómo está organizado el material dentro del servidor** y **qué hace cada mando con él**.

<!-- indice -->

## Índice

- [1. Qué es un servidor de repetición y para qué está](#1-qué-es-un-servidor-de-repetición-y-para-qué-está)
- [2. La organización del material: página, banco, clip y cámara](#2-la-organización-del-material-página-banco-clip-y-cámara)
- [3. El mando y sus controles](#3-el-mando-y-sus-controles)
- [4. Los modos de trabajo y la tecla TAKE](#4-los-modos-de-trabajo-y-la-tecla-take)
- [5. La playlist](#5-la-playlist)
- [6. La timeline y sus canales](#6-la-timeline-y-sus-canales)
- [7. El clip auxiliar](#7-el-clip-auxiliar)
- [8. La suite de gestión y la carga enlazada](#8-la-suite-de-gestión-y-la-carga-enlazada)
- [9. La red entre servidores](#9-la-red-entre-servidores)
- [10. El panel de servicio](#10-el-panel-de-servicio)
- [11. Los datos que el examen ha preguntado](#11-los-datos-que-el-examen-ha-preguntado)
- [12. Trazabilidad](#12-trazabilidad)

<!-- /indice -->

## 1. Qué es un servidor de repetición y para qué está

**Un servidor de repetición graba varias señales a la vez y permite reproducir cualquiera de ellas
desde cualquier punto mientras sigue grabando.** Ésa es la máquina que hace posible **la repetición de
una jugada quince segundos después de que ocurra**, con la cámara que se quiera y a la velocidad que
se quiera.

**Las tres cosas que lo distinguen de un sistema de edición corriente:**

1. **Graba y reproduce al mismo tiempo**, sobre el mismo material.
2. **Se maneja con un mando físico**, no con ratón: **una palanca y un puñado de teclas**, porque
   **en directo no hay tiempo para buscar un menú**.
3. **Su unidad de trabajo es el clip**, marcado sobre la marcha con dos pulsaciones.

**Dónde se usa**: deportes, galas, cualquier directo con repetición o con cámara lenta. Y **su
operador no es un montador que trabaja despacio: es un operador que decide en segundos**, y por eso el
sistema está construido alrededor de la velocidad de acceso.

## 2. La organización del material: página, banco, clip y cámara

**Todo el manejo del sistema descansa en cómo está numerado el material**, y es lo que la pregunta 19
mide.

**La numeración de los clips guardados en el servidor sigue esta jerarquía: el primer número es la
página, el segundo el banco, el tercero el clip, y la letra es el ángulo de cámara o entrada.** Ésa es
la respuesta oficial a la pregunta 19.

| Nivel | Qué es |
|---|---|
| **Página** | **El contenedor mayor**: agrupa bancos. Permite tener varias colecciones separadas |
| **Banco** | **Un grupo de clips**, que se selecciona con una tecla del mando |
| **Clip** | **El fragmento marcado**, con su entrada y su salida |
| **Cámara** o entrada | **Qué señal de las grabadas se está viendo de ese mismo clip** |

**La lógica que hace la respuesta recordable, y que es la de cualquier sistema de archivo**: **se va de
lo general a lo particular**. **Página → banco → clip**, como carpeta → subcarpeta → fichero. **Y la
letra va al final porque no es un nivel más de la jerarquía**: **es una vista distinta del mismo
clip**. Todas las cámaras de un clip **comparten sus tiempos de entrada y salida**; lo único que
cambia es desde qué ángulo se ve.

**Las tres opciones falsas de la pregunta 19 barajan los tres primeros niveles** y dejan la letra
siempre al final. **Es una pregunta de orden puro**, y se contesta con la regla de lo general a lo
particular.

**Por qué esta organización es como es, en el trabajo real**: en un partido, **cada banco se dedica a
una cosa** —uno para goles, otro para faltas, otro para el material de contexto—, y **la página separa
un partido de otro** o **una parte de la siguiente**. **El operador salta de banco con una tecla**, y
por eso el banco tiene que estar por encima del clip.

## 3. El mando y sus controles

**El mando es el aparato entero desde el punto de vista del operador**, y sus controles son pocos a
propósito:

| Control | Qué hace |
|---|---|
| **Palanca de velocidad** (*T bar*) | **Fija la velocidad de reproducción**, de la cámara lenta al avance rápido, y en los dos sentidos |
| **Rueda de búsqueda** (*jog*/*shuttle*) | Recorre el material cuadro a cuadro o a velocidad continua |
| **Teclas de cámara** | **Cambian el ángulo sin perder el punto** |
| **Teclas de banco y de página** | Navegan por la jerarquía del epígrafe anterior |
| **Marcado de entrada y salida** | Crean el clip sobre la marcha |
| **Pantalla LCD** | **Dice qué hay cargado y en qué estado** |
| **Teclas de función** | Acceden a menús y paneles de servicio |

**El rango de velocidades máximo que se puede poner en el mando para reproducir con la palanca va
desde −400 % hasta 400 %.** Ésa es la respuesta oficial a la pregunta 24.

**Cómo se lee ese rango**: **el 100 % es la velocidad normal**; **por debajo es cámara lenta**; **por
encima, avance acelerado**; **y el signo negativo es marcha atrás**. **De −400 % a 400 % significa,
por tanto, cuatro veces la velocidad normal en los dos sentidos.**

**Las tres opciones falsas son rangos plausibles y estrechos** —de −200 a 200, de −50 a 200, de −100 a
100—, y **la de −100 a 100 es la trampa buena**, porque **es lo que un aparato de consumo daría**.

**Lo que hay que entender del rango, más allá de la cifra**: **la marcha atrás a velocidad plena es
una exigencia del directo**, no un lujo. **Un operador que se pasa de la jugada tiene que volver**, y
volver rápido, **sin soltar la palanca ni cambiar de modo**. **Por eso el rango es simétrico.**

## 4. Los modos de trabajo y la tecla TAKE

**El mando trabaja en varios modos**, según cuántas salidas gobierne a la vez:

| Modo | Qué gobierna |
|---|---|
| **Un canal** | Una sola salida de programa |
| **PGM+PRV** | **Dos salidas**: la de programa y la de previo, para preparar la siguiente mientras la primera está en antena |
| **Multicámara** | Varias entradas grabadas y un canal de salida |

**Al pulsar el botón TAKE de un mando en modo PGM+PRV se intercambian las cámaras en los monitores de
programa y de previo.** Ésa es la respuesta oficial a la pregunta 42.

**Qué significa eso en el trabajo**: **el operador prepara en el previo el ángulo que quiere sacar a
continuación** y, **cuando llega el momento, lo pasa a programa con una sola tecla**. **Es el mismo
gesto que un mezclador de vídeo**: **preparar en previo, mandar a programa**, y la palabra *take* es la
misma que se usa en el control de realización.

**Las tres opciones falsas describen operaciones reales del sistema que hace otra tecla**: pasar del
modo de selección de cámara al de programa, alternar el contenido de dos salidas de programa e
insertar el clip cargado en la lista de reproducción. **La distinción está en qué se intercambia**:
**el TAKE intercambia lo que hay en las dos salidas, no el modo ni el contenido de la lista.**

## 5. La playlist

**Una lista de reproducción es una secuencia de clips encadenados que se emiten uno detrás de otro.**
Es lo que permite sacar en antena **un resumen de jugadas** sin ir cargándolas de una en una.

**En una lista de reproducción, los clips no disponibles no se muestran en la pantalla del mando.**
Ésa es la respuesta oficial a la pregunta 55.

**Por qué no se muestran, en lugar de mostrarse tachados o parpadeando**, que es lo que las tres
opciones falsas proponen: **porque en directo un elemento que no se puede emitir no es información: es
un estorbo**. **Si apareciese en la lista, el operador podría intentar sacarlo en antena**, y **el
resultado sería una salida en negro**. **La máquina lo esconde para que no se pueda pulsar.**

**Las tres opciones falsas** —parpadeando, con la leyenda «*not available*» y en negrita— **son las
tres formas en que un sistema de oficina avisaría de un elemento inaccesible**. **En directo la
solución no es avisar: es quitar.**

**Cuándo un clip está no disponible**: cuando **está en otro servidor que ya no se ve**, cuando **su
material ha sido borrado por el ciclo de grabación** o cuando **está siendo escrito y todavía no se
puede leer entero**.

## 6. La timeline y sus canales

**La línea de tiempo del sistema es un montaje con transiciones y efectos**, un paso más allá de la
lista de reproducción, que sólo encadena.

**El requisito mínimo de canales de reproducción para cargar una línea de tiempo es de dos canales.**
Ésa es la respuesta oficial a la pregunta 59.

**Por qué dos y no uno**, que es lo que hace la respuesta razonable en lugar de memorística: **una
línea de tiempo admite transiciones entre clips** —un encadenado, una cortinilla—, **y una transición
es, por definición, dos imágenes a la vez**. **Con un solo canal de reproducción no hay manera de
tener las dos**: el canal está reproduciendo la saliente y **no puede reproducir a la vez la
entrante**.

**Las tres opciones falsas**: **un canal** no basta por lo que se acaba de decir; **tres canales** son
más de los necesarios; y **«depende del modo de operación»** es la opción que suena prudente y es
falsa, **porque el mínimo lo impone la transición y no el modo**.

**La distinción entre lista y línea de tiempo**, que conviene fijar:

| | Lista de reproducción | Línea de tiempo |
|---|---|---|
| **Qué hace** | **Encadena clips** uno detrás de otro | **Monta**: transiciones, efectos, audio |
| **Canales mínimos** | **Uno** | **Dos** |
| **Para qué se usa** | Resúmenes en directo | Piezas acabadas |

## 7. El clip auxiliar

**La función de clip auxiliar permite asignar un clip como audio auxiliar en la lista de reproducción
cargada.** Ésa es la respuesta oficial a la pregunta 16.

**Para qué sirve, en el trabajo real**: **poner una música o un ambiente por debajo de un resumen de
jugadas**. Los clips de la lista traen **el sonido de sus cámaras**, que es ambiente de estadio
troceado; **el clip auxiliar aporta una pista continua** que corre por debajo de todos ellos **y
disimula los cortes de sonido**.

**Las tres opciones falsas y el porqué de cada una**: «vídeo auxiliar» **cambia audio por vídeo**, y
un vídeo auxiliar no tendría sentido en una lista que ya es vídeo; y las dos que hablan de **«varios
clips»** como fuentes de entrada o de salida **rompen la lógica de la función**, que es **un clip
—uno— para toda la lista**.

**La palabra que resuelve la pregunta es «audio»**, y el razonamiento que la sostiene es que **una
lista de reproducción no necesita vídeo auxiliar y sí necesita sonido continuo.**

## 8. La suite de gestión y la carga enlazada

**Además del mando físico, el sistema tiene una suite de programas de gestión** desde la que se
navega el material, se preparan listas y se controlan los canales de reproducción con ratón y
teclado. **El explorador de canales es la parte desde la que se asignan los reproductores.**

**Cuando se quiere que dos clips se carguen a la vez en los dos reproductores ya seleccionados,
cargando sólo uno de ellos a un canal, hay que activar la función LINK.** Ésa es la respuesta oficial
a la pregunta 25.

**Qué hace la función**: **enlaza dos canales de reproducción**, de manera que **cargar un clip en uno
carga automáticamente su pareja en el otro**. Es lo que se usa **cuando dos señales van siempre
juntas** —dos cámaras de la misma jugada, o una señal limpia y su versión con grafismo—: **el operador
carga una y tiene la otra.**

**Las tres opciones falsas son las palabras que el oficio usa para operaciones parecidas**: **GANG**
es sincronizar el transporte de varios canales para que se muevan juntos, **no cargarlos**; y
**TWICE** y **DUAL** **no son funciones del sistema**: son palabras que suenan a duplicar.

**La distinción que la pregunta mide**: **enlazar la carga no es sincronizar el movimiento.** El
enunciado dice «se carguen a la vez», y **la palabra que corresponde a cargar es LINK.**

## 9. La red entre servidores

**Los servidores se conectan entre sí por una red propia**, que es la que permite que **una sala vea y
reproduzca el material grabado en otra máquina** sin copiarlo. **Esa red necesita un servidor que la
gobierne**, y **sólo puede haber uno**.

**Si se configuran dos servidores como servidor en una misma red, sólo el primero en conectarse tomará
el rol de servidor.** Ésa es la respuesta oficial a la pregunta 60.

**Por qué se resuelve así y no con un conflicto**, que es lo que la opción c) propone: **una red de
directo no se puede permitir caerse porque dos máquinas estén mal configuradas**. **El diseño elige un
comportamiento degradado pero estable**: **el primero manda, el segundo se comporta como cliente**, y
**la retransmisión sigue**. **Un error de configuración no debe tirar la red**, y ése es el principio
que hay detrás de la respuesta.

**Las tres opciones falsas**: «ambos compartirán la administración» **describiría un reparto que este
sistema no hace**; «se producirá un conflicto y la red no funcionará» **es lo que un diseño ingenuo
haría**; y «los dos sólo podrán acceder a su propio contenido» **describe el aislamiento total**, que
es justo lo contrario de para qué está la red.

**El aviso de oficio que sale de aquí**: **el fallo no da la cara.** **La red funciona**, y **el
segundo servidor se comporta como cliente sin decir nada**. **Se descubre cuando alguien busca por qué
una máquina no gobierna lo que debería**, y por eso conviene saber cuál es el comportamiento esperado.

## 10. El panel de servicio

**El panel de configuración del servidor se abre desde el teclado del propio sistema**, no desde el
mando, y es donde se ajustan los canales, la grabación y la red.

**Al panel de servicio se accede presionando «Shift + F9» en el teclado.** Ésa es la respuesta oficial
a la pregunta 51. **Las tres opciones falsas son las teclas de función vecinas** —F1, F8 y F10—, y
**es memoria pura**: no hay razonamiento que la sostenga.

**Lo que sí conviene retener del panel**, y aparece en el trabajo diario: es **donde se configura el
reparto de canales** entre grabación y reproducción, **donde se ve el estado de los discos** y
**donde se comprueba el papel de la máquina en la red** del epígrafe anterior.

## 11. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 16 | Qué permite la función de clip auxiliar | a) Asignar un clip como audio auxiliar en la lista cargada ✔ **·** sólo con la plantilla |
| 19 | Jerarquía de la numeración de los clips | d) Página, banco, clip y letra de cámara ✔ **·** sólo con la plantilla |
| 24 | Rango máximo de velocidades con la palanca | c) De −400 % a 400 % ✔ **·** sólo con la plantilla |
| 25 | Función para cargar dos clips a la vez en dos reproductores | a) LINK ✔ **·** sólo con la plantilla |
| 42 | Qué hace el botón TAKE en modo PGM+PRV | b) Intercambia las cámaras en los monitores ✔ **·** sólo con la plantilla |
| 51 | Cómo se accede al panel de servicio | b) Shift + F9 ✔ **·** sólo con la plantilla |
| 55 | Cómo se muestran los clips no disponibles en una lista | d) No se muestran ✔ **·** sólo con la plantilla |
| 59 | Canales mínimos para cargar una línea de tiempo | b) Dos canales ✔ **·** sólo con la plantilla |
| 60 | Qué ocurre con dos servidores configurados como servidor | a) Sólo el primero en conectarse toma el rol ✔ **·** sólo con la plantilla |

**Las nueve respuestas oficiales son correctas**, y **las nueve descansan sólo en la plantilla**.

**Un aviso sobre el enunciado de la pregunta 19**: **remite a «la imagen de referencia»**, y **el
cuadernillo la conserva**, de modo que la pregunta es contestable. **No es una de las preguntas
huérfanas de imagen que este proyecto ha encontrado en otros exámenes audiovisuales.**

**El aviso de estudio**: **cinco de las nueve se razonan** —la jerarquía de la numeración, el
significado del rango de velocidades, el mínimo de dos canales para una transición, por qué un clip no
disponible se esconde y por qué el primer servidor manda—. **Las otras cuatro son memoria**: una
combinación de teclas, un nombre de función, un rótulo de tecla y una palabra.

## 12. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es el manejo de un sistema comercial de repetición y
edición en directo, y **va entera como oficio y como plantilla**.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Las nueve afirmaciones del tema** | 16, 19, 24, 25, 42, 51, 55, 59, 60 |

**Una declaración expresa**: **la documentación del fabricante sobre sus servidores, sus mandos y su
suite de gestión no se ha consultado.** Son manuales de producto de una casa comercial, y este
proyecto no ha accedido a ellos. **Las nueve respuestas de este punto descansan en la plantilla
oficial**, que es el quinto nivel de la jerarquía de fuentes.

**Lo que este tema sí sostiene** es la arquitectura y el porqué: la jerarquía de página, banco, clip y
cámara y su lógica de archivo; la diferencia entre una lista de reproducción y una línea de tiempo, y
por qué la segunda necesita dos canales; el paralelo entre la tecla de intercambio y el mezclador de
un control de realización; la razón de que el rango de velocidades sea simétrico; y el principio de
diseño que hace que un conflicto de configuración degrade la red en lugar de tirarla. **Nada de eso
está en la plantilla: la plantilla sólo da la letra.**
