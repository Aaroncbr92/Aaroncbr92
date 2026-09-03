# Tema 14 del específico de Realización (Asistencia) · La retransmisión. Conexiones y fuentes de contribución exteriores

Las siglas de este tema, presentadas de entrada: el enlace ascendente (***uplink***) y el descendente
(***downlink***); la modulación por desplazamiento de fase en cuadratura (**QPSK**, del inglés
*quadrature phase shift keying*); el periodismo electrónico por satélite (**SNG**) y su versión
digital (**DSNG**); la televisión digital terrestre (**TDT**); el programa (**PGM**); el centro
territorial (**C.T.**) y **Prado del Rey** (**P.R.**), que son los dos nombres propios que el examen
usa abreviados; la unidad móvil (**UM**); la Unión Internacional de Telecomunicaciones (**UIT**)
con su Sector de Radiocomunicaciones (**UIT-R**); la ultraalta definición (**UHD**) y la
codificación de vídeo de alta eficiencia (**HEVC**), que vienen del tema 5; la difusión de vídeo
digital (**DVB**) y su variante por satélite (**DVB-S**); y la sala central de aparatos (**CAR**, del
inglés *central apparatus room*), que es como se llama en inglés al control central.

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización (Asistencia),
> punto 5.4): «La retransmisión. Conexiones y fuentes de contribución exteriores.»

**Cuatro preguntas, y una de ellas es la más específica de RTVE de todo el examen**: pide el camino
exacto que sigue una señal desde una cámara de un centro territorial hasta la emisión en TDT,
nombrando los centros de la casa. Es el único punto del temario donde **el conocimiento de la
organización interna de la Corporación se pregunta directamente**.

<!-- indice -->

## Índice

- [1. Qué es una retransmisión](#1-qué-es-una-retransmisión)
- [2. Contribución y distribución](#2-contribución-y-distribución)
- [3. El camino de una señal dentro de RTVE](#3-el-camino-de-una-señal-dentro-de-rtve)
- [4. El control central](#4-el-control-central)
- [5. El enlace por satélite: ascendente y descendente](#5-el-enlace-por-satélite-ascendente-y-descendente)
- [6. La señal *pool*](#6-la-señal-pool)
- [7. La realización de una retransmisión](#7-la-realización-de-una-retransmisión)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Qué es una retransmisión

**Una retransmisión es la realización en directo de un acontecimiento que ocurre fuera del estudio y
que no se ha organizado para la televisión.** Ésa es la diferencia con un programa de plató: **el
acontecimiento manda**. Un partido dura lo que dura, un discurso empieza cuando empieza y una
procesión pasa por donde pasa.

De ahí las tres condiciones que la definen:

1. **La realización se hace desde una unidad móvil**, en el lugar del acontecimiento.
2. **La señal hay que traerla** hasta el centro emisor, por alguna de las vías del tema 12.
3. **No hay segunda toma.** Todo lo que se pueda preparar antes, se prepara antes; lo que no, se
   resuelve en el momento.

---

## 2. Contribución y distribución

**Ésta es la distinción que ordena todo el tema, y el enunciado del Anexo 2 la nombra con la palabra
«contribución»:**

| | **Contribución** | **Distribución** o emisión |
|---|---|---|
| Qué es | **El transporte de la señal hacia el centro de producción**, para trabajar con ella | El transporte de la señal **hacia el espectador** |
| De dónde a dónde | Del acontecimiento al centro; de un centro a otro | Del centro emisor a la red de difusión |
| Calidad | **Alta**: la señal se va a seguir manipulando | La que el sistema de emisión permita |
| Compresión | Poca o ninguna | La del sistema: HEVC en UHD, según el tema 5 |
| Retardo | El menor posible | Menos crítico |
| Quién la ve | El equipo técnico | El público |

**Una fuente de contribución exterior es, por tanto, cualquier señal que entra en la casa desde
fuera** para incorporarse a un programa: una unidad móvil, un centro territorial, una agencia, un
enviado especial con mochila, un corresponsal por satélite.

**Y el rasgo que las une a todas: entran por el control central**, no directamente al control de
realización. El epígrafe 4 explica por qué.

---

## 3. El camino de una señal dentro de RTVE

**La pregunta 35 del primer cuadernillo es un problema de encaminamiento con nombres propios.**
Plantea esto: se emite en directo por La 2 un programa desde el **Estudio 2 de Prado del Rey**; en su
salida de programa entra la señal de un redactor que llega en directo **desde un estudio del Centro
de Producción de Cataluña**; y pregunta **por qué sitios pasa la señal del redactor, desde que sale
de la cámara hasta que sale de Torrespaña para la emisión en TDT**.

**La respuesta oficial es la c):**

> Control de realización del C.T. Cataluña → Control Central del C.T. Cataluña → Control Central
> Torrespaña → Control Central P.R. → Control de realización Est. 2 → Control Central P.R. → Control
> Central Torrespaña → Control de continuidad de La 2

**Leído como un recorrido, tiene tres tramos y una vuelta:**

| Tramo | De dónde a dónde | Qué pasa |
|---|---|---|
| **1. Salida de Cataluña** | Cámara → realización del centro territorial → **control central del centro territorial** | El centro territorial realiza su señal y la entrega a su control central, que es su puerta de salida |
| **2. Viaje a Madrid** | Control central de Cataluña → **Control Central de Torrespaña** → **Control Central de Prado del Rey** | Torrespaña es el nodo de la red: **todo lo que entra y sale de la casa pasa por allí** |
| **3. Entrada al programa** | Control Central de Prado del Rey → **control de realización del Estudio 2** | La señal llega al mezclador como una fuente más y el realizador la pincha |
| **4. Vuelta** | Estudio 2 → Control Central de Prado del Rey → **Control Central de Torrespaña** → **continuidad de La 2** | El programa ya montado hace el camino inverso hasta la emisión |

**Lo que la pregunta comprueba es que se sepan dos cosas.**

**La primera: que la señal pasa dos veces por los mismos sitios.** Va del centro territorial al
estudio y vuelve del estudio a la emisión, y en las dos direcciones atraviesa Prado del Rey y
Torrespaña. **Las opciones a) y d) hacen el camino sólo una vez** o lo acortan, y por eso son falsas.

**La segunda: que lo que encamina es el control central, no el control técnico.** Las opciones a), b)
y d) escriben «**control técnico**» donde la correcta escribe «**Control Central**». Los dos nombres
existen y **no son lo mismo**: el control técnico atiende a los equipos de un estudio; **el control
central encamina las señales de todo el centro y las que entran y salen de él**. La única opción que
usa el nombre correcto en los siete pasos es la c).

**Y la lección de estudio, que va más allá de esta pregunta**: en un centro de producción, **una
señal no viaja de un sitio a otro por el camino más corto, sino por la matriz**. Todo pasa por el
control central, y por eso el control central es el sitio donde se sabe dónde está cada cosa.

---

## 4. El control central

**El control central —también llamado control técnico central, o *CAR* en la nomenclatura
anglosajona— es la matriz de conmutación de un centro de producción y el sitio donde se genera la
sincronización.** Lo que hace:

| Función | En qué consiste |
|---|---|
| **Encaminar** | Llevar cualquier señal de cualquier origen a cualquier destino, dentro del centro y hacia fuera |
| **Sincronizar** | Generar la referencia —*black burst* o *tri-level*, según el tema 10— y repartirla |
| **Adaptar** | Sincronizar señales de fuera, convertir formatos, corregir niveles |
| **Vigilar** | Medir y comprobar cada señal antes de que entre en un programa |
| **Reservar** | Gestionar los circuitos contratados y las conexiones exteriores |
| **Registrar** | Grabar lo que haga falta grabar de todo lo que pasa |

**Por qué las fuentes exteriores entran por ahí y no directamente al mezclador.** Una señal de fuera
llega **sin sincronizar** con la casa, a veces con el nivel mal y a veces en otro formato. **El
mezclador no puede conmutarla así**, según el epígrafe 16 del tema 10. El control central la
sincroniza, la mide y la entrega en condiciones. **Es el filtro sanitario de la señal.**

---

## 5. El enlace por satélite: ascendente y descendente

**Un enlace por satélite tiene dos mitades, y las dos usan frecuencias distintas:**

| Mitad | Nombre | Qué hace | Quién la ejecuta |
|---|---|---|---|
| **Ascendente** | ***Uplink*** | **Sube** la señal de la estación terrena al satélite, con antenas parabólicas de gran ganancia | La unidad de satélite del acontecimiento |
| **Descendente** | ***Downlink*** | **El satélite retransmite** la señal recibida **hacia su zona de cobertura** sobre la superficie de la Tierra | El satélite; la recibe el centro con su antena |

**El *downlink* es la transmisión de televisión digital vía satélite por enlace descendente, por medio
del cual el satélite retransmite la señal recibida hacia su zona de cobertura sobre la superficie de
la Tierra, utilizando una banda de frecuencias diferente a la del enlace ascendente.** Ésa es la
respuesta oficial a la pregunta 53 del primer cuadernillo, y **lo que la hace correcta frente a las
otras tres son sus tres precisiones**:

1. **Es descendente**, no ascendente. La opción a) describe el ***uplink*** con las mismas palabras
   cambiando una: es la opción gemela.
2. **Cubre una zona**, no un punto. Un satélite no manda la señal a una antena: **la derrama sobre su
   huella**, y la recibe quien esté dentro y tenga con qué.
3. **Usa una banda de frecuencias distinta a la del ascendente.** Ésta es la precisión técnica que
   decide, y tiene una razón física: **si el satélite retransmitiera en la misma frecuencia en que
   recibe, se realimentaría a sí mismo.** El transpondedor recibe en una banda, traslada la señal a
   otra y la reemite.

Las otras dos opciones falsas se descartan solas: «escanear y remasterizar en 4K materiales antiguos»
es posproducción, y «un sistema que utiliza la modulación QPSK» describe una característica del
DVB-S, no lo que la palabra *downlink* nombra.

**La Recomendación UIT-R SNG.770-2** —la que el tema 12 usa para definir el DSNG— **trata las dos
mitades por separado**, y su apartado del enlace descendente empieza justamente por la cobertura:

> 2.2 Enlace descendente 2.2.1 Zona de servicio del enlace descendente Es necesario que la zona de
> servicio del enlace descendente incluya el lugar de recepción previsto.

**Es decir: lo primero que hay que comprobar al contratar un satélite es que el sitio donde se va a
recibir esté dentro de la huella.** Y esa misma norma recuerda que el enlace **ascendente** necesita
autorización del país desde el que se sube.

---

## 6. La señal *pool*

**Una señal *pool* es la que una sola productora realiza y distribuye a todas las demás.** Existe
porque hay acontecimientos donde **no caben veinte equipos**: un acto institucional en una sala
pequeña, una comparecencia, una ceremonia. En lugar de que cada cadena monte lo suyo, **una lo monta
y todas lo reciben**.

**El examen la pregunta en los dos cuadernillos, y con la misma trampa**: entre las cuatro opciones
hay siempre **dos definiciones distintas de señal compartida**, y sólo una es la del *pool*:

| Opción que aparece en las dos preguntas | Qué describe en realidad |
|---|---|
| **«La señal de un evento, principalmente institucional, que realiza una única cadena o productora y distribuye al resto»** | **La señal *pool*** ✔ |
| «La señal de un evento, principalmente deportivo, que se realiza **compartiendo los medios de varias cadenas**» | Una **producción conjunta** o **coproducción**: varias cadenas ponen medios |
| «La señal de un evento que **por cuestiones de seguridad** realiza y emite una única cadena» | Un caso particular, definido por un motivo que no es el del *pool* |
| «La señal **en exclusiva** de un evento» | Justamente **lo contrario**: la exclusiva **no** se distribuye |

**Las dos claves de la definición correcta son *una sola* y *distribuye*.** Una sola productora hace
la señal —ahí se distingue de la producción conjunta, donde los medios se comparten— y **la reparte a
todas —ahí se distingue de la exclusiva—**.

**Y el adjetivo «principalmente institucional» no es adorno**: es lo que separa el *pool* del reparto
de medios que se hace en los grandes acontecimientos deportivos, donde lo habitual es que exista una
**señal internacional** producida por el organizador y cada cadena añada además sus propias cámaras.
El *pool* es la señal única **sin añadidos propios**.

**La pregunta se repite en los dos cuadernillos con las opciones barajadas**: es la 39 del primero,
donde la correcta es la d), y la 6 del segundo, donde la misma frase es la b). **Dos aciertos por una
definición**, si se ha aprendido por su contenido y no por su letra.

---

## 7. La realización de una retransmisión

**Lo que distingue realizar una retransmisión de realizar un programa de plató:**

| | **Plató** | **Retransmisión** |
|---|---|---|
| Qué manda | El guion | **El acontecimiento** |
| Qué se prepara | Todo | **La planta de cámaras y los recursos**; el resto se improvisa |
| Documento de trabajo | Escaleta o minutado | **Plan de cámaras** y **guion de retransmisión**, con lo previsible |
| Cámara principal | Rota según el plano | **La cámara máster sostiene**; las demás aportan |
| Repetición | No hay | **Sí, y es la mitad del espectáculo**: el servidor del tema 10 |
| Riesgo mayor | El tiempo | **Perder la acción** por estar en el plano equivocado |

**Las tres reglas de oficio de una retransmisión:**

1. **Nunca se abandona la acción principal.** La cámara máster —la del tema 7— sostiene el juego, y
   todo lo demás se corta **sobre** ella.
2. **Los planos de recurso se toman cuando no pasa nada**, no cuando hacen falta.
3. **La repetición se prepara mientras la acción sigue.** Quien busca la repetición no es quien
   realiza.

**Y las conexiones exteriores dentro de la propia retransmisión**: una unidad móvil de fútbol tiene
también sus propias fuentes de contribución —el reportero de pista con mochila, la cámara de vestuario,
la señal de datos del marcador—, y todas entran por su matriz con los mismos problemas de
sincronización y retardo del epígrafe 4.

---

## 8. Los datos que el examen ha preguntado

| Nº | Cuadernillo | Qué pregunta | Oficial |
|---|---|---|---|
| 35 | primero | Por dónde pasa la señal de un redactor de Cataluña hasta la TDT | c) Los siete pasos por **Control Central** ✔ |
| 39 | primero | Qué es la señal *pool* | d) Institucional, una sola cadena que la distribuye ✔ |
| 53 | primero | Qué es el *downlink* | b) Enlace descendente, cobertura y banda distinta ✔ |
| 6 | segundo | Qué es la señal *pool* | b) Institucional, una sola cadena que la distribuye ✔ |

**Las cuatro respuestas oficiales son correctas.**

**Y hay dos avisos de estudio.**

**El primero: la 35 es la única pregunta del examen que exige conocer la organización interna de
RTVE.** Nombra Prado del Rey, Torrespaña, el Centro de Producción de Cataluña y la continuidad de
La 2, y su respuesta depende de saber **que el control central es lo que encamina** y **que
Torrespaña es el nodo por el que pasa todo**. No hay manera de deducirla: hay que saberla.

**El segundo: la del *pool* se repite en los dos cuadernillos con las opciones en distinto orden.** Es
la tercera pareja de preguntas repetidas del bloque específico —después de las del tema 5 y las del
tema 10—, y **la única en la que la letra de la respuesta cambia**: es la **d)** en el primer
cuadernillo y la **b)** en el segundo. **Quien memorice la letra en lugar del contenido falla la
segunda.**

---

## 9. Trazabilidad

**Una norma sostiene el epígrafe 5**, del segundo nivel de la jerarquía de fuentes:

| Norma | Qué sostiene aquí | Fichero |
|---|---|---|
| **Recomendación UIT-R SNG.770-2** (01/2012) | Que la zona de servicio del enlace descendente tiene que incluir el lugar de recepción previsto, y que el enlace ascendente exige autorización del país correspondiente | `fuentes/normas-tecnicas/UIT-R_SNG.770-2.pdf` |

**Lo que va como oficio y así se declara**: la distinción entre contribución y distribución, la
descripción del control central y sus seis funciones, la comparación entre realizar en plató y
realizar una retransmisión, las tres reglas de oficio y la tabla de definiciones vecinas de la señal
*pool*.

**Y una declaración que este tema tiene que hacer expresamente, porque es la pregunta más
característica del examen.** El recorrido del epígrafe 3 —Prado del Rey, Torrespaña, el Centro de
Producción de Cataluña, la continuidad de La 2— **se explica aquí a partir de la propia respuesta
oficial de la pregunta 35 y de la función que cumple un control central**, que es materia de oficio.
**No se ha consultado ningún documento de organización interna de la Corporación**, porque este
proyecto no dispone de él: lo que se ha comprobado es que **la opción marcada es la única de las
cuatro que usa el nombre correcto del control que encamina y la única que hace el camino de ida y de
vuelta**. Las tres restantes fallan por una de esas dos cosas o por las dos.
