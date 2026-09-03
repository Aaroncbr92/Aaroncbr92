# Tema 13 del específico de Producción · Control central: coordinación de señales y comunicaciones, emisión, continuidad y distribución

Las siglas de este tema, presentadas de entrada: la sala central de aparatos (**CAR**, del inglés
*central apparatus room*), que es como se llama en inglés al control central; la interfaz digital
serie (**SDI**) y su versión de alta definición (**HD-SDI**); el protocolo de internet (**IP**); la
señal de programa menos uno (**N-1**); la unidad de control de cámara (**CCU**); el programa (**PGM**)
y el previo (**PVW**); la modulación por impulsos codificados (**PCM**); y la televisión digital
terrestre (**TDT**).

> Enunciado de la convocatoria (Anexo 2, temario específico de Producción, punto 13):
> «CONTROL CENTRAL. Coordinación de señales y comunicaciones. Emisión/Continuidad. Distribución de
> imágenes.»

**Tres preguntas: una de definición, una de equipo y una de comunicaciones.** Es el punto que explica
**por dónde pasa todo** en un centro de producción.

<!-- indice -->

## Índice

- [1. Qué es el control central](#1-qué-es-el-control-central)
- [2. La matriz de conmutación](#2-la-matriz-de-conmutación)
- [3. La sincronización](#3-la-sincronización)
- [4. El audio embebido y el embebedor](#4-el-audio-embebido-y-el-embebedor)
- [5. Las comunicaciones: intercomunicación, órdenes y retornos](#5-las-comunicaciones-intercomunicación-órdenes-y-retornos)
- [6. La señal N-1](#6-la-señal-n-1)
- [7. Emisión y continuidad](#7-emisión-y-continuidad)
- [8. La distribución de imágenes](#8-la-distribución-de-imágenes)
- [9. Los datos que el examen ha preguntado](#9-los-datos-que-el-examen-ha-preguntado)
- [10. Trazabilidad](#10-trazabilidad)

<!-- /indice -->

## 1. Qué es el control central

**Desde el control central se coordinan todas las señales de audio y vídeo que se pueden manejar en
una estación de televisión.** Ésa es la respuesta oficial a la pregunta 3, y **la palabra que la
decide es *todas***.

**Las tres opciones falsas acotan la competencia del control central y por eso son falsas:**

| Opción falsa | Qué deja fuera |
|---|---|
| «Solamente las señales exteriores que llegan» | Las internas: estudios, servidores, salas de edición |
| «Solamente las emisiones en directo» | Todo lo grabado, el intercambio y la contribución |
| «Solamente las señales de intercambio y las emisiones en directo» | Las internas otra vez |

**El control central es el nudo del centro**, y de ahí sale todo lo que hace:

| Función | En qué consiste |
|---|---|
| **Encaminar** | Llevar cualquier señal de cualquier origen a cualquier destino |
| **Sincronizar** | Generar la referencia y repartirla; sincronizar lo que llega de fuera |
| **Adaptar** | Convertir formatos, embeber y desembeber audio, corregir niveles |
| **Vigilar** | Medir y comprobar cada señal antes de que entre en un programa |
| **Reservar** | Gestionar los circuitos contratados y las conexiones exteriores |
| **Registrar** | Grabar lo que haya que grabar de todo lo que pasa |
| **Comunicar** | Repartir el intercomunicador, los pilotos y los retornos |

---

## 2. La matriz de conmutación

**La matriz es el aparato que hace posible el encaminamiento**: una rejilla de entradas y salidas
donde **cualquier entrada puede ir a cualquier salida**, y una entrada puede ir a varias salidas a la
vez.

| Concepto | Qué es |
|---|---|
| **Entrada** (*source*) | Una señal que llega: cámara, estudio, servidor, exterior |
| **Salida** (*destination*) | Un destino: un estudio, un grabador, un enlace, un monitor |
| **Nivel** | Vídeo, audio y datos se conmutan en niveles que pueden ir juntos o por separado |
| **Panel de control** | Los teclados con que se ordena la conmutación |
| **Salvado** o *salvo* | El bloqueo de una salida para que nadie la cambie por error durante una emisión |

**Y la regla de oro del control central: una señal que va al aire se protege.** Esa es la función del
salvado, y es lo que evita que una conmutación equivocada tire una emisión.

---

## 3. La sincronización

**Dos señales sólo se pueden conmutar limpiamente si sus imágenes empiezan en el mismo instante.** Por
eso un centro entero trabaja contra **una misma referencia**, generada en un sitio y repartida a todos
los equipos.

| Referencia | Qué es |
|---|---|
| **Black burst** | Una señal de vídeo negro completa, con sus sincronismos: la referencia clásica |
| **Tri-level sync** | Un impulso de tres niveles, definido para alta definición |

**Y lo que llega de fuera no está en fase con la casa**: hay que retenerlo en memoria y volver a
leerlo en el momento correcto. Eso lo hace el **sincronizador de cuadro**, y su precio es **el
retardo**: la señal sale uno o varios cuadros después de entrar.

---

## 4. El audio embebido y el embebedor

**En una señal digital de vídeo caben también las pistas de audio.** Se llama **audio embebido**, y va
metido en los espacios que la señal deja libres entre líneas y entre cuadros.

| Operación | Qué hace | Aparato |
|---|---|---|
| **Embeber** | **Meter** pistas de audio dentro de la señal de vídeo | **Embebedor** (*embedder*) |
| **Desembeber** | **Sacarlas** de la señal de vídeo | **Desembebedor** (*de-embedder*) |

**En la práctica el mismo aparato hace las dos cosas**, y por eso el examen lo formula así.

**La función de un embebedor situado en un control central técnico de televisión es extraer o insertar
audios en una señal de vídeo.** Ésa es la respuesta oficial a la pregunta 25.

**Las tres opciones falsas describen tres aparatos reales de un control central**, y ahí está la
dificultad:

| Opción falsa | Qué aparato describe |
|---|---|
| «Multiplexar señales procedentes de una señal satélite» | Un **demultiplexor** de transporte, en la recepción de satélite |
| «Multiplexar señales procedentes de codificadores IP» | Un **multiplexor** de transporte sobre red |
| «Enrutar señales hacia los controles de realización» | **La matriz de conmutación** |

**Lo que separa al embebedor de los tres es que no mueve señales entre sitios: mueve audio dentro de
una señal.** Es una operación de formato, no de encaminamiento.

**Y por qué importa en la práctica**: una señal que llega de fuera puede traer su audio embebido en
pistas que no coinciden con las del centro. **El embebedor las reordena**, y sin ese paso el programa
sale con el sonido en el canal equivocado.

---

## 5. Las comunicaciones: intercomunicación, órdenes y retornos

**Un centro de producción tiene tres circuitos de comunicación que no se mezclan:**

| Circuito | Quién habla | Quién oye |
|---|---|---|
| **Intercomunicación** (*intercom*) | El equipo técnico entre sí | El equipo técnico, por auricular |
| **Órdenes** | El realizador | Cámaras, regiduría, control |
| **Retornos** | El control | **Quien está delante de la cámara**, por pinganillo o monitor |

**El circuito que más problemas da es el tercero**, porque quien lo recibe **está hablando al mismo
tiempo**. De ahí el epígrafe siguiente.

---

## 6. La señal N-1

**El N-1 es la mezcla del programa menos la señal de la persona a la que se le envía.**

**Y el problema que resuelve es concreto**: si a un redactor que está en directo se le devuelve el
programa **con su propia voz dentro**, la oirá con el retardo del enlace —unos cientos de
milisegundos— y **no podrá hablar**. El eco de la propia voz retrasada bloquea el habla; es un efecto
conocido y no se puede vencer con voluntad.

**En un directo de un informativo, el envío del N-1 al redactor por el pinganillo significa que se le
envía la señal de retorno de audio del programa exceptuando su propia voz.** Ésa es la respuesta
oficial a la pregunta 37.

**Las cuatro opciones de esa pregunta empiezan igual y se diferencian en lo que quitan y lo que
dejan**, lo que la convierte en una pregunta de lectura fina:

| Opción | Qué dice que lleva | Por qué falla |
|---|---|---|
| a) | El programa **incluyendo lo que él dice** | Es exactamente el problema que el N-1 evita |
| **b)** | El programa **exceptuando su propia voz** | ✔ |
| c) | El programa **con las órdenes del realizador y su propia voz** | Mete las dos cosas que no deben ir: su voz y un circuito que es otro |
| d) | El programa **sin las órdenes pero oyéndose a sí mismo** | Vuelve a dejar su propia voz |

**Y una precisión de oficio: cada envío tiene su propia N-1.** Si hay tres conexiones exteriores, hay
tres mezclas distintas, cada una sin la voz de su destinatario. **Por eso una mesa de sonido de
directo se dimensiona por el número de envíos, no sólo por el de entradas.**

**Las órdenes del realizador van por otro camino** —el circuito de órdenes del epígrafe 5— y se mezclan
con el retorno sólo si así se decide, con el nivel del programa bajado mientras se habla.

---

## 7. Emisión y continuidad

**La continuidad es el área que emite el canal.** No hace programas: **hace lo que va entre los
programas** y garantiza que el canal no se quede en negro.

| Qué emite | Ejemplos |
|---|---|
| **La identidad del canal** | Mosca, caretas, cortinillas |
| **Las autopromociones** | Los avances de lo que viene |
| **La publicidad** | En sus bloques, con su duración vendida |
| **El enlace entre programas** | Las entradas y las salidas |
| **Los avisos de servicio** | Señalización de contenido, subtitulado, cambios de programación |

**Cómo se emite hoy**: la continuidad trabaja con una **lista de emisión** —la escaleta del día,
minuto a minuto— cargada en un **servidor de emisión** que dispara cada elemento a su hora, con un
sistema de automatización que lo gobierna y un operador que vigila y corrige.

**Y la obligación legal que la acompaña**: lo emitido **hay que conservarlo**, según el tema 16.

---

## 8. La distribución de imágenes

**Distribuir es repartir la señal ya terminada**, y un centro público lo hace en varias direcciones a
la vez:

| Destino | Cómo |
|---|---|
| **La red de difusión terrestre** | Hacia el centro emisor y de ahí a la red de TDT |
| **Satélite y cable** | Por los circuitos contratados con cada operador |
| **Plataformas e internet** | Por red, con la codificación de cada destino |
| **Otras cadenas** | Intercambio de noticias y señales de acontecimientos |
| **El archivo** | Registro de lo emitido y del material de trabajo |

**Y una figura propia del intercambio entre cadenas que conviene nombrar**: la **señal *pool***, la que
**una sola cadena o productora realiza y distribuye a todas las demás**, típicamente en actos
institucionales donde no caben veinte equipos.

---

## 9. Los datos que el examen ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 3 | Qué se coordina desde el control central | a) Todas las señales de audio y vídeo de la estación ✔ |
| 25 | Función de un embebedor en un control central | b) Extraer o insertar audios en una señal de vídeo ✔ |
| 37 | Qué significa el envío del N-1 al redactor | b) El programa exceptuando su propia voz ✔ |

**Las tres respuestas oficiales son correctas.**

**Y las tres tienen la misma construcción: opciones que se diferencian por una acotación.** La 3 opone
«todas» a tres «solamente»; la 25 opone una operación de formato a tres de encaminamiento; y la 37
opone cuatro combinaciones de qué se quita y qué se deja. **Leer despacio la mitad final de cada
opción es lo que resuelve las tres.**

**Un aviso de estudio.** El **N-1** aparece también en el examen de Realización (Asistencia), con las
mismas palabras y otra formulación. **Es de los conceptos que se preguntan en varias ocupaciones**, y
por eso conviene tenerlo entendido y no memorizado: **la mezcla del programa menos la voz de quien la
recibe.**

---

## 10. Trazabilidad

**Este tema no cita ninguna norma en su propio texto.** Su materia es la organización técnica de un
centro de producción de televisión y va como oficio: las siete funciones del control central, la
matriz de conmutación, las dos referencias de sincronismo, el audio embebido, los tres circuitos de
comunicación, el N-1, la continuidad y la distribución.

**Un enlace con otro tema de este libro**: la obligación de conservar lo emitido durante **seis
meses** está en el **artículo 156.2 de la Ley 13/2022, de 7 de julio, General de Comunicación
Audiovisual**, y se desarrolla en el tema 16.

**Y una declaración expresa sobre el vocabulario.** «Control central» y «control técnico central» se
usan como sinónimos en este tema, que es como se usan en la casa; **en algunos centros designan salas
distintas** —una de conmutación y otra de mantenimiento—, y el examen no distingue entre ellas. **Lo
que este tema fija es la función, que es la misma con cualquier nombre.**
