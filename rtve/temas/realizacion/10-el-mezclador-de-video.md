# Tema 10 del específico de Realización (Asistencia) · El mezclador de vídeo

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Realización (Asistencia) · bloque 4 (4.1 a 4.12) |
| **Sirve para** | **Realización (Asistencia)** |
| **Fuente** | **Documentación de fabricante**: manual en español de los **Blackmagic ATEM**, edición de diciembre de 2024 |
| **Identificador** | Documentación de fabricante, descargada el **03/09/2026** |
| **Redacción que se estudia** | La **edición de diciembre de 2024** del manual |
| **Aviso sobre las fuentes** | **El manual dice «composición» donde el examen dice «llave»**, y «nivel» donde el examen dice «clip». Y **Sony, Grass Valley, Ross, Panasonic y EVS siguen cerrados**: lo que el tema dice de la serie XVS que el examen cita por modelo no está contrastado en su fabricante |
| **Extensión** | **8.554 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el banco de mezcla y efectos (**M/E**, del inglés
*mix/effects*); el generador de efectos digitales (**DVE**, del inglés *digital video effects*, y
**DME** en la nomenclatura de Sony, del inglés *digital multi effects*); la composición posterior
(**DSK**, del inglés *downstream keyer*) y su pareja anterior (**USK**, del inglés *upstream
keyer*); la imagen dentro de imagen (**PinP** o **PIP**, del inglés *picture in picture*); la mezcla
aditiva total (**FAM**, del inglés *full additive mix*) y la mezcla no aditiva (**NAM**, del inglés
*non-additive mix*); la interfaz de propósito general (**GPI**, del inglés *general purpose
interface*); el anticipo o previo (**PVW**, del inglés *preview*) y el programa (**PGM** o **PP**);
la interfaz digital serie (**SDI**, del inglés *serial digital interface*); el fotograma (**fr**,
del inglés *frame*), que es como el mezclador cuenta las pausas; y la propia marca **EVS**, que da
nombre al servidor de repeticiones.

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización (Asistencia),
> bloque 4, «Conocimientos específicos de mezclador de vídeo»): «4.1. Panel de control (arquitectura
> modular). 4.2. Bancos de Mezcla Efectos (M/E). 4.3. Modos de transición. 4.4. Tipos de llave
> (Key). Llave de luminancia, lineal y Chroma‐Key. 4.5. Snapshots, macros, timelines. 4.6. Clip
> store. 4.7. Sincronización y retardo de señales (Tri‐level y Black Burst). 4.8. Conocimientos
> básicos de los generadores de efectos digitales (DVE). 4.9. Programación y operación del
> mezclador.»

**Treinta y cinco preguntas: es el banco más grande de la ocupación y el punto que decide el
examen.** Uno de cada seis aciertos del bloque específico está aquí.

**Y una advertencia de vocabulario que hay que leer antes de seguir.** La única documentación de
fabricante que este proyecto ha podido consultar sobre mezcladores es el manual en español de los
**Blackmagic ATEM**, y ese manual **traduce *key* por «composición»**: donde el examen de RTVE dice
«llave» o «key», el manual dice «composición por luminancia», «composición lineal», «composición
precompuesta». **Son la misma cosa con dos nombres.** En este tema se usa el vocabulario del examen
—llave, *key*, relleno, *fill*— y se avisa cada vez que se cita el manual.

<!-- indice -->

## Índice

- [1. Qué es un mezclador de vídeo](#1-qué-es-un-mezclador-de-vídeo)
- [2. El panel de control y su arquitectura modular](#2-el-panel-de-control-y-su-arquitectura-modular)
- [3. Las fuentes: el término *source*](#3-las-fuentes-el-término-source)
- [4. Los bancos de mezcla efectos (M/E)](#4-los-bancos-de-mezcla-efectos-me)
- [5. Los buses auxiliares](#5-los-buses-auxiliares)
- [6. Las salidas: programa, previo, limpia y multipantalla](#6-las-salidas-programa-previo-limpia-y-multipantalla)
- [7. Los modos de transición](#7-los-modos-de-transición)
- [8. Las tres señales de una incrustación](#8-las-tres-señales-de-una-incrustación)
- [9. Los tipos de llave](#9-los-tipos-de-llave)
- [10. Aditivo frente a lineal: la diferencia que el examen pregunta tres veces](#10-aditivo-frente-a-lineal-la-diferencia-que-el-examen-pregunta-tres-veces)
- [11. Clip, ganancia y las señales premultiplicadas](#11-clip-ganancia-y-las-señales-premultiplicadas)
- [12. El *self key* y el *show key*](#12-el-self-key-y-el-show-key)
- [13. El generador de efectos digitales](#13-el-generador-de-efectos-digitales)
- [14. Memorias: *snapshots*, macros y *timelines*](#14-memorias-snapshots-macros-y-timelines)
- [15. El *clip store*](#15-el-clip-store)
- [16. Sincronización y retardo de señales](#16-sincronización-y-retardo-de-señales)
- [17. El mezclador mandando sobre otros equipos: la GPI](#17-el-mezclador-mandando-sobre-otros-equipos-la-gpi)
- [18. Las preguntas que dependen de una imagen](#18-las-preguntas-que-dependen-de-una-imagen)
- [19. Los datos que el examen ha preguntado](#19-los-datos-que-el-examen-ha-preguntado)
- [20. Trazabilidad](#20-trazabilidad)

<!-- /indice -->

## 1. Qué es un mezclador de vídeo

**Un mezclador de vídeo hace tres cosas y sólo tres**, aunque las haga de muchas maneras:

1. **Conmutar**: elegir cuál de las fuentes de entrada sale al aire.
2. **Mezclar**: pasar de una fuente a otra con una transición, en lugar de con un corte seco.
3. **Combinar**: superponer una fuente sobre otra, que es lo que se llama incrustar o *key*.

Todo lo demás —memorias, efectos digitales, generadores de color, reproductores de clips— existe para
servir a esas tres.

**Y una condición previa que hay que tener siempre presente: para poder conmutar entre dos señales
sin que la imagen salte, las dos tienen que estar sincronizadas.** De ahí el epígrafe 16.

---

## 2. El panel de control y su arquitectura modular

**El panel de control es el conjunto de botones y controles con el que se opera el mezclador.** Ésa
es la respuesta oficial a la pregunta 49 del segundo cuadernillo, y su enunciado obliga a distinguir
tres cosas que en la conversación se llaman igual:

- **El panel** es **botones y controles**: la superficie física.
- **El mezclador** propiamente dicho es la **unidad de proceso**, que suele estar en un armario de
  equipos y no en el control.
- **Los efectos** son lo que el mezclador hace, no la cosa con la que se hace.

Las tres opciones falsas de esa pregunta cambian una de esas piezas: una dice que el panel es «un
conjunto de **efectos**», otra que es «un conjunto de **cámaras**», y la tercera cambia el destino
—dice «**postproducción**» donde la definición dice «emisión o grabación»—. **El mezclador de vídeo
es un aparato de directo**, y esa última opción es la que lo saca de su sitio.

**«Arquitectura modular» significa que el panel se compone de módulos intercambiables**, cada uno con
una función, y que un mismo mezclador admite paneles de distinto tamaño según el control donde se
instale:

| Módulo | Qué lleva |
|---|---|
| **Bus de programa** | Una fila de botones: una fuente por botón. Lo que está aquí, está al aire |
| **Bus de previo** (*preset*) | La misma fila: lo que está aquí es lo siguiente |
| **Módulo de transición** | Los botones **CUT** y **AUTO**, la **palanca** (*T-bar*), la duración y **el tipo de transición** |
| **Módulo de composición** (*keyers*) | Los botones de cada llave: activar, previsualizar, meter y sacar |
| **Módulo de DSK** | Las llaves posteriores, normalmente dos: mosca y rótulos |
| **Módulo de menús** | Pantalla y mandos giratorios para todo lo que no cabe en un botón |
| **Módulo de memorias** | *Snapshots*, macros y sus botones de disparo |
| **Buses auxiliares** | Filas o teclado para asignar fuentes a cada salida auxiliar |

El manual de los ATEM describe esa misma distribución cuando explica su panel:

> El panel de control dispone de cuatro botones para superponer efectos. Cada uno de ellos puede
> asignarse a una composición lineal, precompuesta, geométrica, por crominancia, por luminancia o con
> efectos visuales digitales. Por su parte, el módulo DSK cuenta con dos botones para composiciones
> prev…

—donde «composición» es lo que el examen llama **llave**.

---

## 3. Las fuentes: el término *source*

**En un mezclador, *source* no es «un cable»: es una fuente de vídeo con todos sus atributos
asociados.** Ésa es la respuesta oficial a las preguntas 57 del primer cuadernillo y 109 del segundo
—la misma pregunta repetida, palabra por palabra—, y lo que hay detrás es esto:

Cada fuente del mezclador tiene, además de su señal:

| Atributo | Para qué |
|---|---|
| **Nombre largo y nombre corto** | Lo que se lee en el multipantalla y en el panel |
| **Señal de llave asociada** | Para que al elegir esa fuente como relleno se cargue sola su llave |
| **Retardo** | Para compensar el desfase de esa entrada |
| **Corrección de color de entrada** | Para igualarla con las demás |
| **Grupo de piloto** (*tally*) | Qué luz roja se enciende cuando está al aire |
| **Botón asignado** | En qué tecla del panel está |

**El «mapeado de fuentes a botones» —que es la opción falsa d)— es sólo uno de esos atributos**, no
la definición. Y las otras dos opciones falsas cambian el sujeto: «memorias de salida» son otra cosa
y «la señal de vídeo procesada» es el resultado, no la fuente.

**Que la fuente lleve sus atributos es lo que hace posible el *autoselect* del epígrafe 9**: cuando
una fuente tiene declarada su señal de llave, seleccionarla como relleno carga automáticamente la
llave que le corresponde.

---

## 4. Los bancos de mezcla efectos (M/E)

**Un banco M/E es un mezclador completo dentro del mezclador.** Tiene su bus de programa, su bus de
previo, su módulo de transición y sus llaves, y **su salida se puede usar como fuente de otro banco
o del programa**. Es la pieza que permite construir una imagen compleja aparte y meterla al aire de
una vez.

El manual de los ATEM lo explica así, y merece la pena porque dice de dónde viene la idea:

> La línea de mezcladores ATEM incluye dispositivos de alta gama que funcionan según la dinámica M/E
> utilizada en la industria de la teledifusión.

y añade para qué se inventó:

> El modo M/E ha sido desarrollado durante décadas para tratar de eliminar los errores cometidos al
> alternar señales durante la transmisión de eventos en directo. Permite ver con facilidad lo que
> acontece en todo momento, a fin de evitar confusiones que conducen a equivocaciones. Este tipo de
> funcionamiento brinda la posibilidad de verificar las fuentes que van a ser transmitidas y probar
> diferentes efectos antes de emitirlas al aire.

**El M/E es lo que se utiliza para aplicar transiciones y combinaciones complejas entre distintas
fuentes de vídeo.** Ésa es la respuesta oficial a la pregunta 75 del segundo cuadernillo, y las tres
opciones falsas son piezas más pequeñas: el **bus de llave** (*key bus*) elige una sola señal, el
**previo** (*PVW*) es una salida de monitorizado y el **DSK** es una llave posterior, no un banco.

**La cadena de un mezclador de varios bancos**, de arriba abajo:

| Etapa | Qué hace | Se ve en la salida limpia |
|---|---|---|
| **M/E 1, M/E 2, M/E 3…** | Construyen imágenes compuestas | Sí, si van al programa |
| **Programa** | Elige y transiciona entre fuentes y salidas de M/E | Sí |
| **DSK 1 y DSK 2** | Añaden mosca, rótulos y créditos **después** del programa | **No** |
| **Fundido a negro** | Lo último de todo | — |

**Que el DSK vaya después del programa es lo que hace posible la salida limpia** del epígrafe 6: la
señal se toma antes de esa etapa.

**Y hay bancos que no son físicos.** Los mezcladores modernos permiten **dividir un banco M/E en
dos** —cada mitad con menos recursos— o **crear bancos virtuales** por programa. Ésta es exactamente
la materia de la pregunta 62 del segundo cuadernillo, que enseña una configuración en una imagen y
pide leerla; el epígrafe 18 explica por qué no se puede verificar aquí.

---

## 5. Los buses auxiliares

**Un bus auxiliar es una salida a la que se le puede asignar cualquier fuente del mezclador**, con
independencia de lo que esté en el programa. El manual de los ATEM los describe con la comparación
exacta:

> Las salidas auxiliares en algunos mezcladores ATEM son salidas SDI a las que es posible asignar
> varias señales entrantes y fuentes internas. Son muy similares a las salidas de una matriz de
> conmutación y permiten emplear las señales provenientes de todas las entradas, los generadores de
> color y los reproductores multimedia, además de la señal principal y los anticipos, e incluso
> barras de color.

**Para qué sirven en un plató:** para alimentar **las pantallas del decorado**, los **retornos** de
los presentadores y los invitados, el **teleprompter**, los **grabadores** y las **conexiones
exteriores**. Cada destino necesita ver algo distinto de lo que sale al aire.

**Y ahí está la pregunta 59 del primer cuadernillo**, que pregunta qué se usa para enviar y aplicar
una corrección de color específica a una señal de vídeo **en las pantallas de un plató**, y cuya
respuesta oficial es **un bus auxiliar**. La razón es doble:

1. **Es la salida que va a las pantallas**, por definición.
2. **La corrección de color se puede aplicar en ese envío sin afectar al programa**, que es lo que el
   enunciado pide con la palabra «específica». Una pantalla de plató necesita una imagen tratada para
   verse bien **en cámara**, y esa imagen no es la que debe salir al aire.

Las tres opciones falsas: el **banco M/E** construye imagen para el aire, no envíos; el **DVE**
transforma geométricamente, no encamina; y una **salida fija** es justamente lo contrario de un
auxiliar, porque no se puede reasignar.

**Y la pregunta 38 del segundo cuadernillo lleva el auxiliar un paso más allá**: pregunta si, en los
auxiliares que se mandan a las pantallas durante una gala, se podrían hacer **mezclas y cortinillas**
usando exclusivamente el auxiliar. La respuesta oficial es **sí, se podría mezclar y hacer
cortinillas, y dependerá del mezclador que haya porque no todos pueden hacerlo**.

**Es la respuesta correcta y es la más matizada de las cuatro.** La opción a) —«en los auxiliares
sólo se puede conmutar por corte; es un preselector»— **fue verdad durante décadas** y sigue siendo
verdad en muchos mezcladores: un auxiliar clásico es una matriz, y una matriz corta. Pero los
mezcladores de gama alta permiten **asignar un banco M/E a una salida auxiliar** o dotar al auxiliar
de un mezclador propio, y entonces sí transiciona. La opción c) es la que reconoce las dos cosas: **se
puede, y depende del modelo**.

---

## 6. Las salidas: programa, previo, limpia y multipantalla

| Salida | Qué lleva |
|---|---|
| **Programa** (PGM, PP) | Lo que está al aire, **con** mosca, rótulos y todo lo que añada el DSK |
| **Previo** (PVW, *preset*) | Lo que va a salir con la siguiente transición |
| **Limpia** (*clean feed*) | **Lo mismo que el programa pero sin las composiciones posteriores**: sin mosca y sin rótulos |
| **Auxiliares** | Lo que se les asigne |
| **Multipantalla** (*multiview*) | Todas las fuentes en mosaico, con nombres y pilotos, para el monitor del control |

**La salida limpia existe porque el programa no siempre vale para todo el mundo.** Quien recibe la
señal para volver a emitirla —otra cadena, una plataforma, un archivo— **no quiere la mosca de quien
la produce ni los rótulos en un idioma que no es el suyo**, y por eso pide la limpia.

**La respuesta oficial a la pregunta 45 del primer cuadernillo es «una salida de previo "limpia", que
no lleva rótulos ni mosca», y hay que hacerle una precisión.** Lo que la opción dice de la señal
—**limpia, sin rótulos ni mosca**— es exacto y es lo que distingue a esta salida de las otras tres
opciones, que llevan **rótulos**, **mosca** o las dos cosas. **Pero llamarla «salida de previo» es
impreciso**: la salida limpia **se deriva del programa**, no del previo; es el programa **tomado
antes del DSK**. Un previo enseña lo siguiente; una limpia enseña lo que está al aire.

**No es errata de plantilla**, porque de las cuatro opciones sólo una describe una señal sin rótulos
ni mosca y ésa es la marcada. Es una imprecisión de vocabulario en el enunciado, y el opositor la
acierta fijándose en lo que la señal **no lleva**, que es lo único que separa las cuatro opciones.

---

## 7. Los modos de transición

| Transición | Qué hace | Nombre en el panel |
|---|---|---|
| **Corte** | Cambio instantáneo de una fuente a otra | **CUT** |
| **Mezcla** o encadenado | Las dos imágenes se superponen y una sustituye a la otra progresivamente | **MIX**, *dissolve* |
| **Cortinilla** | **Un borde con forma recorre la pantalla revelando la nueva imagen** | **WIPE** |
| **Fundido a color** | La primera imagen pasa **a través de un color intermedio** hasta la segunda | *Fade*, *dip to colour*, **SÚPER MIX** cuando el color es blanco |
| **Mezcla no aditiva** | En cada punto se muestra **la más brillante de las dos** imágenes | **NAM** |
| **Mezcla aditiva total** | **Las luminancias de las dos fuentes se suman** | **FAM** |
| **Transición con efecto digital** | La imagen se mueve, gira o se encoge para dejar paso | **DVE wipe**, *DME wipe* |

**La cortinilla es la transición en la que un borde con forma se mueve a través de la pantalla,
revelando la nueva imagen mientras la primera desaparece.** Ésa es la respuesta oficial a la pregunta
110 del segundo cuadernillo, y la palabra que la identifica es **borde**: la mezcla no tiene borde,
porque las dos imágenes se superponen en toda la pantalla a la vez.

**Y la pregunta 91 pregunta lo mismo por el otro lado**: qué permite activar las cortinillas desde el
módulo de transiciones, y la respuesta es **Wipe**. Las opciones falsas de esa pregunta son otras
tres cosas del panel: **NAM** es un modo de mezcla, **DSK** es una llave posterior y **súper mix** es
un fundido a través de un color.

**Ahora la distinción entre NAM y FAM, que es la pregunta 118 del primer cuadernillo.** Las dos son
maneras de mezclar dos imágenes sin encadenarlas linealmente, y se diferencian en lo que hacen con
las luminancias:

- **NAM (mezcla no aditiva)**: en cada punto de la pantalla se muestra **la más brillante de las
  dos**. El efecto es que **las partes brillantes de la fuente que se desvanece se ven durante más
  tiempo** que las oscuras: los rótulos blancos aguantan hasta el final.
- **FAM (mezcla aditiva total)**: las luminancias **se suman**, de modo que **en el punto medio de la
  transición la luminancia de las dos fuentes está al 100 %**. La imagen se va a blanco en la mitad
  del recorrido, como un destello.

**La respuesta oficial a la 118 es la definición del FAM**, y **la opción a) de esa misma pregunta es
exactamente la definición del NAM**. Es decir: la pregunta pone las dos definiciones juntas y pide
saber cuál es cuál. **La palabra que decide es *suman*.** Y la opción b) —«las dos imágenes se
desvanecen por igual en todos los niveles de brillo»— es el **MIX** normal, y la c) —«la primera
fuente pasa a través de un color preseleccionado»— es el **fundido a color**.

---

## 8. Las tres señales de una incrustación

**Incrustar es superponer una imagen sobre otra, y en ello intervienen siempre tres señales:**

| Señal | Nombre inglés | Qué es |
|---|---|---|
| **Fondo** | *background* | La imagen de base, sobre la que se superpone |
| **Relleno** | *fill* | **Lo que se ve** de la imagen superpuesta: el logotipo, el rótulo, el presentador |
| **Llave** | *key*, *alpha* | **Dónde se ve**: una máscara en escala de grises que dice, punto por punto, cuánta transparencia hay |

El manual de los ATEM lo dice con esas mismas tres piezas al describir la composición lineal, que es
la que las lleva separadas:

> Una composición lineal requiere una fuente para el primer plano y un canal alfa. La señal principal
> incluye la imagen que se superpone al fondo, mientras que el canal alfa contiene una máscara en
> escala de grises que permite definir la transparencia. Ambas señales son fuentes audiovisuales.

**La fórmula del compuesto, que es la que resuelve media docena de preguntas de este examen:**

**salida = relleno × llave + fondo × (1 − llave)**

Leída despacio: **donde la llave vale 1 —blanco— se ve el relleno; donde vale 0 —negro— se ve el
fondo; y donde vale un valor intermedio se ven los dos en esa proporción.** El borde suavizado de un
rótulo es justamente eso: una franja de valores intermedios.

**Y de ahí sale la respuesta a la pregunta 112 del segundo cuadernillo**, que pregunta cuántas
señales están implicadas para incrustar correctamente un *self key*, y responde **tres**: fondo,
relleno y llave. **En un *self key* dos de esas tres salen de la misma fuente** —el relleno se usa
también como llave, según el epígrafe 12— pero **el proceso de incrustación sigue manejando tres
señales**, y son tres las que hay que tener en cuenta para que el resultado sea correcto. La
pregunta cuenta señales del modelo, no cables del rack.

---

## 9. Los tipos de llave

| Llave | Cómo se hace la máscara | Cuándo se usa |
|---|---|---|
| **De luminancia** (*luminance key*) | **A partir del brillo de la propia señal de relleno**: lo oscuro se hace transparente | Rótulos blancos sobre negro; grafismo sin canal alfa |
| **Lineal** (*linear key*) | **Con una señal de llave separada**, en escala de grises | Grafismo profesional, tituladores; es la de mayor calidad |
| **De crominancia** (*chroma key*) | **A partir de un color**, normalmente verde o azul, que se declara transparente | Plató virtual, hombre del tiempo |
| **De figura** (*preset pattern*, *pattern key*) | Con **una forma geométrica generada por el mezclador** | Ventanas, círculos, cortinillas fijas |
| **Con efectos digitales** (*DVE key*) | Combina la llave con una transformación geométrica | Ventanas móviles, imagen dentro de imagen |

**Y la pregunta 113, que el examen repite en los dos cuadernillos con las mismas opciones: cuál NO es
un tipo de llave.** Las cuatro opciones son **Additive Key**, **Linear Key**, **Preset Pattern** y
**Coring Key**, y la respuesta oficial es **Coring Key**.

**Las tres primeras son tipos de llave y la cuarta no lo es.** *Coring* es un control de reducción de
ruido: **recorta los valores pequeños de una señal para que el ruido de fondo no se amplifique**. Se
encuentra en el procesado de las cámaras y en algunos ajustes de detalle, y **no genera ninguna
máscara**, que es lo que define a una llave. La trampa está en que suena a familia —«*coring*» y
«*keying*» se parecen— y en que las otras tres sí son términos de las llaves de un mezclador Sony.

**El *chroma key* y el Ultimatte.** *Ultimatte* es el nombre de un sistema de incrustación por
crominancia de alta calidad, y la pregunta 14 del primer cuadernillo pregunta a qué dispositivo se
asocia. **Se asocia al mezclador de vídeo**, porque es ahí donde el proceso de llave vive: en los
mezcladores de gama alta el Ultimatte va **integrado como un tipo más de llave**, y en otros
funciona como una unidad externa cuya salida entra al mezclador ya compuesta. Las tres opciones
falsas son equipos de otras partes de la cadena: el **repetidor**, la **mesa de audio** y el
**sincronizador del control central**.

---

## 10. Aditivo frente a lineal: la diferencia que el examen pregunta tres veces

**Éste es el punto más fino de todo el bloque, y el examen vuelve a él tres veces**: en la pregunta
32 del primer cuadernillo y en las 35 y 39 del segundo. Merece un epígrafe entero.

**Las dos maneras de combinar el relleno con el fondo:**

| | **Llave lineal** (o **no aditiva**) | **Llave aditiva** |
|---|---|---|
| Fórmula | **salida = relleno × llave + fondo × (1 − llave)** | **salida = relleno + fondo × (1 − llave)** |
| El relleno se atenúa con la llave | **Sí** | **No**: entra entero |
| Dónde la llave vale 0 | **No aparece nada del relleno** | **Aparece el relleno tal cual, sumado al fondo** |
| Para qué se pensó | Grafismo con canal alfa correcto | Rótulos y llamas sobre fondo, donde se quiere que lo brillante se sume |

**La consecuencia práctica es una sola frase: en la llave aditiva, todo lo que tenga señal el relleno
se ve, tenga o no tenga llave.**

**Con eso se responde la pregunta 32 del primer cuadernillo.** Plantea un gráfico con su llave bien
acoplada, incrustado como llave de luminancia en *autoselect* y sin invertir, y pregunta qué pasa si
**el nivel de negros de la señal de relleno se levanta al 7 %** y no se toca ningún parámetro. La
respuesta oficial: **sólo tendrá consecuencias si la llave de luminancia es aditiva, y se notará en
el fondo al activar o desactivar la llave por corte.**

Y se ve en las dos fórmulas. En las zonas donde la llave vale 0 —el fondo del gráfico—:

- **Lineal**: salida = relleno × 0 + fondo × 1 = **fondo**. El 7 % del relleno se multiplica por cero
  y desaparece. **Nada cambia.**
- **Aditiva**: salida = relleno + fondo × 1 = **fondo + 7 %**. Ese siete por ciento **se suma al fondo
  en toda la pantalla**, y por eso «se notará en el fondo al activar o desactivar la llave por corte»:
  la imagen de fondo se levanta y se baja de golpe.

**La pregunta 39 del segundo cuadernillo es la misma física planteada como problema de plató.** El
titulador entrega una señal de llave que **no cubre una parte donde el relleno sí tiene señal**, y se
pregunta qué tipo de llave hacer para que esa parte **no se incruste**, sin poder usar máscaras. La
respuesta oficial es **llave de luminancia no aditiva**, y es exactamente la primera columna de la
tabla: **al multiplicar el relleno por la llave, lo que la llave no cubre se anula**. Con una llave
**aditiva**, esa parte sin llave aparecería sumada al fondo, que es el problema que se quiere evitar.
El *chroma key* no sirve porque no hay color que declarar transparente, y la «llave mixta» no es un
tipo de llave de esta familia.

**Y la pregunta 35 del segundo cuadernillo cierra el asunto por el lado contrario.** Plantea una
señal de relleno **con canal alfa acoplado** y una **llave de luminancia lineal en *autoselect*, sin
invertir**, y pregunta cómo será el resultado **según la luminancia de los píxeles del relleno**. La
respuesta oficial es: **es indiferente la luminancia de los píxeles.**

**Y es indiferente porque en ese montaje la transparencia no la decide el relleno: la decide la
llave.** El *autoselect* significa que el mezclador toma automáticamente **la señal de llave asociada
a esa fuente** —el canal alfa acoplado, según el epígrafe 3— en lugar de fabricarse una a partir del
brillo del relleno. Con la llave venida de fuera, **la luminancia del relleno sólo decide de qué
color se ve lo que se ve, no si se ve**.

**Las tres opciones falsas de la 35 describen lo que pasaría si la llave se sacara del propio
relleno**, es decir, un *self key*: píxeles blancos opacos, negros transparentes y el resto en
proporción. **Eso es verdad de una llave de luminancia normal y falso de una llave con canal alfa
acoplado en *autoselect*.** La pregunta separa las dos cosas.

---

## 11. Clip, ganancia y las señales premultiplicadas

**Cuando la llave se fabrica a partir del brillo del relleno, hay que decidir a partir de qué nivel
de gris se considera opaco.** Eso lo hacen dos controles:

| Control | Qué mueve |
|---|---|
| **Clip** (recorte, nivel, *threshold*) | **El punto de la escala de grises donde la señal se recorta**: por encima, opaco; por debajo, transparente |
| **Ganancia** (*gain*) | **La pendiente del recorte**: cuán brusco es el paso de transparente a opaco, y por tanto la dureza del borde |

**El punto donde se recorta la señal de llave en una incrustación de luminancia se ajusta con los
controles de clip y ganancia.** Ésa es la respuesta oficial a la pregunta 119 del primer cuadernillo.
Las tres opciones falsas son controles reales de otras cosas: el **relleno** es una señal, no un
control de recorte; los **bordes** añaden filete o sombra al rótulo; y la **saturación** es de color.

El manual de los ATEM describe esos dos controles con otro nombre y la misma función:

> Nivel Permite ajustar el valor a partir del cual la imagen de fondo es visible a través de la
> máscara. Al disminuir este valor, la imagen de fondo se verá con mayor nitidez. Aumente este
> parámetro si el fondo se ve completamente negro. Ganancia Permite modificar electrónicamente el
> valor de visibilidad de la imagen superpuesta atenuando su borde.

**Y ahora las señales premultiplicadas, que es la pregunta 30 del segundo cuadernillo.** Un grafista
entrega un logotipo con su señal de llave y avisa de que está **precortado o premultiplicado**. Eso
quiere decir que **la señal de relleno ya ha sido multiplicada por la señal de llave** antes de
salir del titulador: el relleno viene ya con sus bordes atenuados y su fondo a negro.

**La respuesta oficial es «la señal de fill ha sido multiplicada por la señal de key», y el orden de
la frase es lo que se pregunta.** La opción a) dice lo contrario —la llave multiplicada por el
relleno— y es lo que no ocurre: **la llave es la máscara, y una máscara no se multiplica por lo que
enmascara**.

**Qué hay que hacer con una señal premultiplicada.** El mezclador tiene un ajuste que lo declara
—Sony lo llama *premultiplied*, Blackmagic **«composición precompuesta»**— y **cuando se activa, el
mezclador deja de multiplicar otra vez**. Si no se declara, el relleno se multiplica dos veces por la
llave y los bordes salen oscurecidos. El manual de los ATEM lo dice en una línea:

> Composición precompuesta Indica que el canal alfa del clip en el reproductor multimedia está
> premultiplicado.

y avisa de cuándo hacen falta los controles manuales en su lugar:

> Si el elemento gráfico no incluye un canal premultiplicado, utilice los controles Recorte y
> Ganancia según se describe en el apartado Composición de imágenes para obtener el resultado
> deseado.

**Las dos opciones falsas restantes de la 30** hablan de recortar «a unas dimensiones determinadas»
—eso es un **recuadre**, no una premultiplicación— y de una llave «precortada en luminancia», que no
es lo que la palabra nombra.

---

## 12. El *self key* y el *show key*

**Un *self key* es una llave en la que el relleno se usa también como llave.** No hay señal de llave
separada: el mezclador se la fabrica del brillo del propio relleno. Es lo mismo que una **llave de
luminancia**, mirado desde el encaminamiento.

Sirve cuando la fuente **no trae canal alfa** y lo que se quiere incrustar es claro sobre fondo
negro: un rótulo blanco, un reloj, una llama. **Y no sirve** cuando el gráfico tiene medios tonos que
deben verse opacos, porque entonces el propio gris los volvería semitransparentes.

**El *show key* es otra cosa y no hay que confundirlas: es la previsualización de la señal de
llave.** Ésa es la respuesta oficial a las preguntas 114 de los dos cuadernillos —otra pregunta
repetida palabra por palabra—, y sirve para **ver la máscara sola, en blanco y negro**, y comprobar
que recorta donde debe antes de meterla al aire.

**La opción falsa a) de esa pregunta —«la previsualización de los ajustes del key»— es la que más se
acerca y no es lo mismo**: previsualizar los ajustes es ver **el resultado compuesto** en el monitor
de previo; el *show key* enseña **la señal de llave en bruto**. La diferencia importa porque lo que
se busca al pulsarlo es precisamente ver **si la máscara está bien**, no si el conjunto queda bonito.

---

## 13. El generador de efectos digitales

**Un DVE —o DME en la nomenclatura de Sony— transforma geométricamente una imagen antes de
componerla.** Sus parámetros, agrupados:

| Grupo | Parámetros | Qué hacen |
|---|---|---|
| **Traslación** (*location*) | **X, Y, Z** | Mueve la imagen. **La Z la acerca o la aleja**, y por tanto la agranda o la empequeñece **en perspectiva** |
| **Tamaño** (*size*) | X, Y, Z | Escala la imagen, **con un valor por eje** |
| **Rotación** | X, Y, Z | Gira la imagen sobre cada eje |
| **Aspecto** (*aspect*) | — | **Cambia la proporción** entre ancho y alto: deforma |
| **Recorte** (*crop*) | Superior, inferior, izquierda, derecha | Recorta la ventana |
| **Perspectiva** | — | Cuánto se nota la profundidad |
| **Bordes** | Anchura, color, sombra | El filete de la ventana |
| **Esquinas** (*corner pinning*) | Las cuatro esquinas | **Cambia la perspectiva llevando cada esquina a un sitio** |

**El *corner pinning* es el efecto que permite cambiar la perspectiva manejando la posición de las
esquinas de la imagen.** Ésa es la respuesta oficial a la pregunta 36 del primer cuadernillo, y es lo
que se usa para meter una imagen dentro de una pantalla que aparece en escena y no está de frente:
se llevan las cuatro esquinas a las cuatro esquinas de la pantalla y la imagen se deforma sola para
encajar. Las tres opciones falsas hablan de redondear esquinas, de seguimiento y de manipular el
borde, que son efectos distintos.

**Y la pregunta 69 del segundo cuadernillo: cómo ampliar una imagen conservando sus proporciones
originales.** La respuesta oficial es **modificar la traslación en el eje Z**.

**El razonamiento es el de la perspectiva.** En un DVE con perspectiva activada, **mover la imagen
hacia la cámara por el eje Z la agranda sin tocar su geometría**: es un acercamiento, no una escala,
y por construcción no puede deformarla. Las otras tres opciones:

- **Cambiar los valores de aspecto** es exactamente **lo que deforma**: el aspecto es el parámetro
  que rompe la proporción.
- **La rotación en X e Y** gira, no amplía.
- **Variar el tamaño** amplía, y **conservaría las proporciones sólo si se aplicara el mismo valor a
  los tres ejes**. En un DME el tamaño tiene un componente por eje, así que la operación no garantiza
  por sí misma que la proporción se mantenga: la Z sí lo garantiza.

**Y el efecto de ventana, que es la pregunta 50 del primer cuadernillo.** El efecto con el que se
consigue **la superposición de una o varias ventanas** es el **PinP**, imagen dentro de imagen, que
se construye con un DVE reduciendo y colocando la fuente sobre el fondo. Las tres opciones falsas son
efectos vecinos: el **mosaico** pixela la imagen, la **multi-imagen** divide la pantalla en partes
iguales sin superponer nada, y la **transición por clip** es un modo de transición.

---

## 14. Memorias: *snapshots*, macros y *timelines*

**Tres maneras de guardar trabajo hecho, y el examen las distingue por lo que guardan:**

| Memoria | Qué guarda | Cuándo se usa |
|---|---|---|
| **Snapshot** | **Un estado del mezclador en un instante**: qué fuente hay en cada bus, qué llaves están puestas, cómo están sus parámetros | Recuperar de golpe una configuración conocida |
| **Macro** | **Una secuencia de instrucciones con sus tiempos**, que se ejecutan una tras otra al pulsar un botón | Automatizar una entrada, una cabecera, un cambio de escenario |
| **Timeline** | Una sucesión de estados con transiciones entre ellos, ejecutada sobre una línea de tiempo | Efectos largos y precisos |
| **Shotbox** | Un teclado de disparo rápido donde se colocan las memorias | Tener a mano lo que se usa a cada rato |

**La diferencia entre *snapshot* y macro es la del tiempo: el *snapshot* es una fotografía, la macro
es una película.**

El manual de los ATEM define la macro exactamente así:

> Una macro es una secuencia de instrucciones que se llevan a cabo automáticamente al presionar un
> botón. Por ejemplo, es posible grabar una serie de transiciones entre distintas fuentes que
> incluyan imágenes superpuestas, ajustes del volumen y modificaciones en la configuración de las
> cámaras. Una vez registradas las instrucciones, pueden ejecutarse inmediatamente presionando dicho
> botón.

**Con eso se responde la pregunta que los dos cuadernillos repiten —la 60 del primero y la 111 del
segundo—.** La secuencia que enseñan es:

> «Snapshot de PP, Pausa de 15fr, Transición Mix de PP, Key1 de PP ToOff»

y la respuesta oficial es **una macro**. **La prueba está en dos de sus cuatro elementos**: hay una
**pausa medida en fotogramas** y hay **un *snapshot* dentro**. Una memoria que **contiene** un
*snapshot* y **espera quince fotogramas** antes de seguir no puede ser un *snapshot* —que es
instantáneo y no contiene pasos— ni una memoria de llave —que guarda parámetros, no acciones—. Y
**tampoco es un *timeline***, que es la opción a) y la más tentadora: un *timeline* coloca estados
sobre una línea de tiempo continua, mientras que **lo que se enseña es una lista de instrucciones
ejecutadas una tras otra, con una pausa explícita entre dos de ellas**. Ésa es la forma de una macro.

**Y la pregunta 51 del segundo cuadernillo pregunta por la otra memoria**: qué se usa para recuperar
el estado del mezclador en un momento determinado y de forma inmediata. La respuesta es
**snapshots**, y las tres opciones falsas son piezas de otra función: la **shotbox** es dónde se
guardan los botones de disparo, el ***clip store*** almacena vídeo y el ***genlock*** es la
sincronización del epígrafe 16.

---

## 15. El *clip store*

**El *clip store* es la memoria de vídeo e imágenes fijas del propio mezclador**: un almacén interno
donde se cargan clips cortos —cabeceras, ráfagas, cortinillas animadas— y grafismos fijos, para
poder dispararlos como una fuente más sin depender de un servidor externo.

Sus rasgos:

- **Cada clip ocupa una fuente del mezclador**, y se selecciona en los buses como si fuera una
  cámara.
- **Los grafismos se cargan con su canal alfa**, de modo que al elegirlos como relleno el mezclador
  toma también su llave. El manual de los ATEM lo describe con esa automatía: «al elegir un
  reproductor multimedia, tanto el canal alfa como la imagen principal se activan automáticamente sin
  que sea necesario seleccionarlos por separado».
- **La duración es corta**, porque la memoria es limitada: para material largo se usa un servidor.
- **Se dispara con un botón o desde una macro**, y por eso es la pieza que convierte una entrada de
  programa en una operación de una sola tecla.

---

## 16. Sincronización y retardo de señales

**Dos señales de vídeo sólo se pueden conmutar limpiamente si sus imágenes empiezan en el mismo
instante.** Si no, el corte cae en mitad de un cuadro y la imagen salta. De ahí que todo un centro de
producción trabaje **contra una misma referencia de sincronismo**, que se genera en un sitio y se
reparte a todos los equipos.

**Las dos señales de referencia que el temario nombra:**

| Referencia | Qué es | Para qué |
|---|---|---|
| **Black burst** | **Una señal de vídeo negro completa**, con sus sincronismos y su salva de color | La referencia clásica, de la definición convencional; sigue sirviendo para sincronizar equipos de alta definición |
| **Tri-level sync** | **Un impulso de tres niveles** —positivo, negativo y reposo—, definido para alta definición | La referencia de los formatos de alta y ultraalta definición, más precisa |

**El aparato que las genera se llama generador de sincronismos**, y lo que hace cada equipo al
recibirla es **engancharse** a ella: eso es el ***genlock***.

**Y para lo que no se puede sincronizar están los sincronizadores de cuadro.** Una señal que llega de
fuera —una unidad móvil, un enlace, un colaborador— **no está en fase con la casa**, y hay que
retenerla en memoria y volver a leerla en el momento correcto. El manual de los ATEM describe que en
sus mezcladores eso va integrado en cada entrada:

> Cada entrada del dispositivo cuenta con un resincronizador que previene posibles saltos en la señal
> emitida. Si el mezclador detecta una fuente que no está sincronizada, activará esta función
> automáticamente para garantizar…

**El precio del sincronizador es el retardo**: la señal sale uno o varios cuadros después de entrar.
Y de ahí el segundo problema del epígrafe, **el retardo diferencial**: si una fuente pasa por un
sincronizador y otra no, las dos llegan desfasadas, y con ellas el sonido. **Por eso las fuentes del
mezclador llevan un parámetro de retardo entre sus atributos**, según el epígrafe 3: para igualar por
arriba lo que el camino ha desigualado.

---

## 17. El mezclador mandando sobre otros equipos: la GPI

**Un control de realización no es sólo el mezclador: es el mezclador dando órdenes a los demás
equipos.** Y la manera más antigua y más fiable de dar esas órdenes es un contacto eléctrico.

**La GPI —interfaz de propósito general— es una entrada o salida de contacto seco que dispara una
acción.** No lleva datos: **lleva un pulso**. Un botón del mezclador cierra el contacto y, al otro
lado, un equipo hace lo que tiene programado: arrancar, parar, pasar de página, saltar a la
siguiente cámara.

**Para controlar un sistema EVS desde un mezclador de vídeo durante una producción en directo se
necesita una GPI.** Ésa es la respuesta oficial a la pregunta 74 del segundo cuadernillo. **El EVS es
el servidor de repeticiones**, y lo que se quiere es que **la repetición arranque en el mismo
fotograma en que el mezclador la pone al aire**: un pulso lo consigue con exactitud de cuadro.

Las tres opciones falsas son cosas reales del entorno que no hacen eso: el **IPDirector** es el
programa de gestión de contenidos del propio EVS —organiza el material, no dispara desde el
mezclador—; el **DSK** es la llave posterior; y el **MOTU M4** es una interfaz de audio.

**Y el pariente de la GPI que conviene nombrar: el piloto o *tally*.** Es el mismo principio en
sentido contrario: el mezclador cierra un contacto para que se encienda la luz roja de la cámara que
está al aire.

---

## 18. Las preguntas que dependen de una imagen

**Seis preguntas de este bloque enseñan una figura en el cuadernillo y piden leerla**, y el texto
extraído del PDF **no conserva las figuras**. Son éstas:

| Nº | Cuadernillo | Qué enseña | Oficial |
|---|---|---|---|
| 116 | primero | Una posición de DVE, y pide qué parámetros le corresponden | c) 3 |
| 117 | primero | Cuatro transiciones entre A y B numeradas de 1 a 4 | a) 1 MIX, 2 SÚPER MIX, 3 NAM, 4 WIPE |
| 62 | segundo | Una configuración de bancos | c) Un banco M/E dividido en dos y programa |
| 65 | segundo | Una pantalla de asignación, y pide dónde se asigna la fuente de una llave | d) 4 |
| 108 | segundo | Un estado del mezclador, y pide qué pasará al pulsar **Auto** | c) Una cortinilla que elimina las llaves 2 y 3, manteniendo el fondo |
| 115 | segundo | Una secuencia en el **Sony XVS 7000** | **d) No se sabe, los datos son insuficientes** |

**Las seis se recogen con la opción de la plantilla y se declaran sin verificar**, porque
comprobarlas exige el original ilustrado. No son erratas: son preguntas que **exigen la figura**.

**Y la 115 merece un comentario aparte, porque su respuesta oficial es «no se sabe, los datos son
insuficientes».** Es una opción legítima y poco frecuente: el tribunal admite que **la información
dada no basta para decidir**, y convierte eso en la respuesta correcta. **Para el opositor la lección
es que «no se puede saber» puede ser la solución**, y que descartarla por parecer una salida fácil es
un error.

**De las otras cinco, la 117 se puede estudiar aunque no se pueda verificar**, porque lo que pide es
reconocer cuatro transiciones por su aspecto, y el epígrafe 7 las describe: la **MIX** superpone
uniformemente, la **SÚPER MIX** pasa por un color intermedio, la **NAM** deja ver la más brillante de
las dos y la **WIPE** avanza con un borde. Quien sepa distinguirlas de vista responde la pregunta con
la figura delante.

---

## 19. Los datos que el examen ha preguntado

| Nº | Cuadernillo | Qué pregunta | Oficial |
|---|---|---|---|
| 14 | primero | A qué dispositivo se asocia el Ultimatte | b) Al mezclador de vídeo ✔ |
| 32 | primero | Efecto de levantar los negros del relleno al 7 % | d) Sólo con llave de luminancia aditiva ✔ |
| 36 | primero | Qué es el *corner pinning* | a) Cambiar la perspectiva moviendo las esquinas ✔ |
| 45 | primero | Qué es la salida CLEAN | b) Salida «limpia», sin rótulos ni mosca ✔ **·** la llama «de previo» |
| 50 | primero | Efecto para superponer ventanas | b) PinP ✔ |
| 57 | primero | Qué es *source* en un mezclador | a) Fuentes de vídeo con sus atributos asociados ✔ |
| 59 | primero | Con qué enviar una corrección de color a las pantallas | a) Un bus auxiliar ✔ |
| 60 | primero | A qué pertenece la secuencia con pausa de 15 fotogramas | b) Una macro ✔ |
| 113 | primero | Cuál NO es un tipo de llave | d) Coring Key ✔ |
| 114 | primero | Qué es el *Show Key* | d) La previsualización de la señal de llave ✔ |
| 116 | primero | Parámetros del DVE de una posición | c) 3 **·** depende de una imagen |
| 117 | primero | Orden de cuatro transiciones entre A y B | a) MIX, SÚPER MIX, NAM, WIPE **·** depende de una imagen |
| 118 | primero | Qué se ve al usar FAM | d) Las luminancias se suman: 100 % en el punto medio ✔ |
| 119 | primero | Cómo se ajusta el recorte de la llave de luminancia | a) Con clip y ganancia ✔ |
| 30 | segundo | Qué significa premultiplicado | b) El relleno multiplicado por la llave ✔ |
| 32 | segundo | Por qué no se ve el bus EDIT PREVIO en su monitor | a) No está asignado a una salida del mezclador ✔ |
| 35 | segundo | Resultado de una llave lineal en *autoselect* con alfa acoplado | c) Es indiferente la luminancia de los píxeles ✔ |
| 38 | segundo | Si se puede mezclar y hacer cortinillas en un auxiliar | c) Sí, y depende del mezclador ✔ |
| 39 | segundo | Llave para que no se incruste el relleno sin llave | d) Llave de luminancia no aditiva ✔ |
| 49 | segundo | Qué es el panel de control del mezclador | b) Un conjunto de botones y controles ✔ |
| 51 | segundo | Con qué recuperar el estado del mezclador de golpe | a) Snapshots ✔ |
| 62 | segundo | Qué bancos tiene el mezclador de la imagen | c) Un M/E dividido en dos y programa **·** depende de una imagen |
| 65 | segundo | Dónde se asigna la fuente de una llave | d) 4 **·** depende de una imagen |
| 69 | segundo | Cómo ampliar conservando proporciones | c) Traslación en el eje Z ✔ |
| 74 | segundo | Qué se necesita para controlar un EVS desde el mezclador | c) GPI ✔ |
| 75 | segundo | Qué se usa para transiciones y combinaciones complejas | d) M/E ✔ |
| 91 | segundo | Qué activa las cortinillas en el módulo de transiciones | c) Wipe ✔ |
| 108 | segundo | Qué ocurrirá al pulsar Auto | c) Cortinilla que quita las llaves 2 y 3 **·** depende de una imagen |
| 109 | segundo | Qué es *source* en un mezclador | a) Fuentes de vídeo con sus atributos asociados ✔ |
| 110 | segundo | Transición con un borde que recorre la pantalla | a) Wipe ✔ |
| 111 | segundo | A qué pertenece la secuencia con pausa de 15 fotogramas | b) Una macro ✔ |
| 112 | segundo | Cuántas señales intervienen en un *self key* | c) 3 ✔ |
| 113 | segundo | Cuál NO es un tipo de llave | d) Coring Key ✔ |
| 114 | segundo | Qué es el *Show Key* | d) La previsualización de la señal de llave ✔ |
| 115 | segundo | A qué corresponde una secuencia en el Sony XVS 7000 | d) No se sabe, los datos son insuficientes **·** depende de una imagen |

**Veintinueve respuestas verificadas y correctas; seis que dependen de una imagen y quedan sin
verificar.** Ninguna errata de plantilla.

**Una anotación de vocabulario, en la 45**: la salida limpia se deriva del **programa**, no del
previo, y el enunciado la llama «de previo». Lo que la opción dice de la señal es exacto y es lo
único que la separa de las otras tres, así que la respuesta se sostiene.

**Y el dato de estudio más rentable de todo el bloque específico: este punto repite seis preguntas
enteras entre los dos cuadernillos**, con las mismas opciones y la misma respuesta:

| Pregunta repetida | Primer cuadernillo | Segundo |
|---|---|---|
| Qué es *source* | 57 | 109 |
| La secuencia con pausa de 15 fotogramas | 60 | 111 |
| Cuál NO es un tipo de llave | 113 | 113 |
| Qué es el *Show Key* | 114 | 114 |

**Cuatro preguntas idénticas, ocho aciertos.** En un examen que se decide por décimas, **este bloque
es el que más devuelve por hora estudiada**.

---

## 20. Trazabilidad

**Éste es el punto del temario que el Anexo 2 escribe como si estuviera describiendo un manual de
fabricante**, y sin embargo es aquel para el que la documentación de fabricante está casi toda
cerrada. Lo que hay y lo que no:

| Fuente | Nivel | Qué sostiene aquí | Estado |
|---|---|---|---|
| Manual de los **Blackmagic ATEM**, bloque en español | Cuarto: documentación de fabricante, edición de diciembre de 2024, descargada el 03/09/2026 | La definición de macro, la de composición lineal, la de composición precompuesta, los controles de nivel y ganancia, la descripción de las salidas auxiliares, el resincronizador de entrada, el reparto del panel entre llaves y DSK, y el origen y el propósito del modo M/E | **Consultado** |
| **Sony**, para el **XVS 7000** y la serie XVS que el examen cita por su nombre | Cuarto | Nada | **Cerrado**: tres rutas probadas —catálogo estadounidense, británico y español— y las tres responden «prohibido» **con agente de navegador** |
| **Grass Valley**, familia K-Frame | Cuarto | Nada | **Cerrado**: la dirección de ayuda sirve un portal de incidencias, no documentación |
| **Ross Video**, Carbonite | Cuarto | Nada | **Cerrado**: dos rutas, «no encontrado» las dos |
| **Panasonic**, serie AV-HS | Cuarto | Nada | **Cerrado**: su índice de manuales responde «prohibido» |
| **EVS**, citado dos veces por el examen | Cuarto | Nada | **Cerrado**: el sitio abre, pero la ficha del producto devuelve «no encontrado» |

**Todo esto está recogido en el registro de fuentes de fabricante de este proyecto**, con las rutas probadas, y se declara
aquí porque **el examen cita a Sony por modelo en dos preguntas —la 32 y la 115 del segundo
cuadernillo— y este tema no ha podido contrastar ni una línea en su fabricante**. Lo que dice de la
serie XVS —que tiene un bus de EDIT PREVIO, y que hay que asignarlo a una salida para verlo— **se
apoya en la lógica común de los mezcladores profesionales**, no en el manual de Sony, y así queda
dicho.

**El resto va como oficio y como física de la señal, y así se declara**: las fórmulas del compuesto
lineal y del aditivo, que son las que resuelven las preguntas 32, 35 y 39 y **se deducen de la
definición de cada modo**; la tabla de tipos de llave; la de modos de transición con la distinción
entre NAM y FAM; los parámetros del DVE; la diferencia entre *snapshot*, macro y *timeline*; la
descripción del *clip store*; las dos referencias de sincronismo —*black burst* y *tri-level*— y la
GPI.

**Una advertencia sobre el vocabulario, ya dada al principio y que se repite aquí porque es la que
puede despistar a quien consulte la fuente**: el manual de Blackmagic dice **«composición»** donde el
examen dice **«llave»** o **«key»**, y **«nivel»** donde el examen dice **«clip»**. Quien busque
«llave» en ese manual no la encontrará, y no será porque no esté.
