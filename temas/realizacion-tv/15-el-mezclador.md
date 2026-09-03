# Tema 15 del específico de Realización Televisión · El mezclador

Las siglas y términos de este tema, presentados de entrada: el efecto digital de vídeo con que se
reduce y coloca una imagen dentro de otra (**DVE**, *digital video effect*), la incrustación por color
(*chroma key*), la incrustación en general (*key*), el mezclador de producción (*switcher* en la
documentación en inglés), el ordenador de imágenes de síntesis que compone un decorado virtual (motor
de *render*) y la sucesión de instrucciones programadas que el mezclador ejecuta sola (*macro*, y su
pariente el *timeline* de efectos).

Y los nombres comerciales que el cuadernillo rotula en mayúsculas, escritos aquí con su grafía
corriente: **Live Edit** (el que la plantilla da por bueno), **Avid Program Mixer** (que el temario no
ha encontrado con esa función), **Prime TV** (tampoco) y **QE Pilot** (que juega con el nombre de un
sistema real, CuePilot); **Mistika**, el sistema de acabado de la casa **SGO** (una marca, y el temario
no le atribuye ningún desarrollo porque no lo ha verificado); y **Brainstorm IPF** (el nombre de una
plataforma de grafismo, con la misma advertencia).

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización, punto 4.3):
> «LA REALIZACIÓN. Conceptos generales del mezclador.»

**Siete preguntas.** **El enunciado más corto de todo el anexo —seis palabras— y sin embargo un punto
que el examen no deja pasar**: **lo que pregunta no es cómo se llaman los botones, sino qué puede y qué
no puede hacer un mezclador**, y **dónde termina su trabajo y empieza el de otro equipo.**

**Un aviso de reparto**: **cuatro de las siete preguntas son de incrustación** —*chroma*, *key*,
decorado virtual, generador de caracteres— y **tres son de automatización** —macros, *timelines* y el
programa que las lanza—. **Son las dos cosas que el examen entiende por «conceptos generales del
mezclador».**

<!-- indice -->

## Índice

- [1. Qué es un mezclador y qué hace](#1-qué-es-un-mezclador-y-qué-hace)
- [2. El chroma key: cualquier color sirve](#2-el-chroma-key-cualquier-color-sirve)
- [3. Producción en tiempo real y decorados virtuales](#3-producción-en-tiempo-real-y-decorados-virtuales)
- [4. El DVE y la reposición de una señal dentro de una gafa](#4-el-dve-y-la-reposición-de-una-señal-dentro-de-una-gafa)
- [5. La macro: la definición del fabricante](#5-la-macro-la-definición-del-fabricante)
- [6. El software que programa una emisión entera](#6-el-software-que-programa-una-emisión-entera)
- [7. Los generadores de caracteres y el intruso](#7-los-generadores-de-caracteres-y-el-intruso)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Qué es un mezclador y qué hace

**El mezclador es el aparato que elige, en cada instante, qué señal de entrada sale al programa**, y
**el que hace la transición de una a otra.** **Todo lo demás que hace —incrustar, componer, recordar
secuencias— cuelga de esas dos funciones.**

| Función | Qué significa |
|---|---|
| **Conmutar** | **Pasar de una entrada a otra**: el corte, que es la transición instantánea |
| **Transicionar** | **Encadenado, cortinilla, fundido**: pasar de una a otra con duración |
| **Incrustar** | **Meter una imagen dentro de otra** por color, por luminancia o por canal alfa |
| **Componer** | **Reducir, colocar y superponer** varias señales en el mismo cuadro: es el trabajo del DVE |
| **Automatizar** | **Guardar una secuencia de esas operaciones y lanzarla con un botón**: la macro |

**Y una precisión de vocabulario que hace falta para leer los enunciados**: **el examen llama «gafa» a
la composición de dos o más ventanas en pantalla** —una gafa 50/50 es la pantalla partida en dos
mitades; una gafa 20/60/20, tres ventanas con la central más ancha—. **Es vocabulario de plató español,
no término normalizado**, y **la pregunta 29 lo da por sabido.**

## 2. El chroma key: cualquier color sirve

**Un *chroma key* se puede hacer con cualquier color.** Ésa es la respuesta oficial a la pregunta 77.

**El mecanismo**: **la incrustación por croma no reconoce «el verde»: reconoce el color que se le diga
que reconozca.** **Se le indica al mezclador un color de referencia y una tolerancia**, y **todo píxel
que caiga dentro de ese margen se sustituye por la señal de fondo.**

**Por qué entonces todo el mundo usa verde y azul, que es lo que hace verosímiles las tres opciones
falsas:**

1. **Ni el verde ni el azul saturados aparecen en la piel humana**, y **la piel es lo que casi siempre
   hay delante del croma.**
2. **En los sensores el canal verde es el que más resolución tiene** —hay el doble de fotositos
   verdes—, **así que el recorte sale más limpio.**
3. **El azul se prefiere cuando el vestuario lleva verde**, y **al revés.** **Se elige por lo que hay
   delante, no por una limitación del aparato.**

**Lo que la pregunta mide es exactamente eso**: **saber distinguir una costumbre bien fundada de una
imposibilidad técnica.** **Las tres opciones falsas convierten una costumbre en una regla**, y **las
tres empiezan por «solo».**

## 3. Producción en tiempo real y decorados virtuales

**Dos preguntas del cuadernillo van juntas**, porque **las dos preguntan lo mismo desde lados
distintos**: **qué hace falta para incrustar en directo.**

**La primera, la pregunta 6**: **de los cuatro equipos que enumera, el que permite hacer un croma para
producción en tiempo real es Infinity Set.** Ésa es la respuesta oficial.

| Equipo | Qué es | Sirve en directo |
|---|---|---|
| **Infinity Set** ✔ | **Un sistema de plató virtual y realidad aumentada**, pensado para emisión en vivo | **Sí** |
| **DaVinci** | **Un etalonador y editor**, que trabaja sobre material grabado | **No** |
| **After Effects** | **Un compositor de postproducción**, que renderiza fotograma a fotograma | **No** |
| **Nuke** | **Un compositor de cine de altas prestaciones**, también de postproducción | **No** |

**La regla que separa la columna**: **los tres falsos son herramientas de postproducción**, y **una
herramienta de postproducción no se define por no ser rápida: se define por trabajar sobre material que
ya existe.** **En directo el material no existe todavía.**

**La segunda, la pregunta 31**: **con un mezclador que no tenga posibilidad de incrustar *keys*, sí hay
opción de trabajar sobre un decorado virtual en tiempo real, teniendo la señal de cámara en el motor de
render y un software que realice esa incrustación.** Ésa es la respuesta oficial.

**El razonamiento**: **la incrustación no tiene por qué hacerla el mezclador.** **Si la señal de cámara
entra en el motor de render, el motor compone el decorado virtual con la figura ya recortada y devuelve
una sola señal ya montada**, que **el mezclador se limita a conmutar como conmutaría cualquier otra.**
**El mezclador deja de ser el que incrusta y pasa a ser el que emite.**

**Las tres opciones falsas y por qué caen:**

| Opción | Por qué es falsa |
|---|---|
| **«No se puede incrustar nada si el mezclador no tiene *key*»** | **Confunde el aparato con la función**: la incrustación puede hacerse aguas arriba |
| **«Sí, siempre y cuando la señal llegue sincronizada al mezclador»** | **La sincronía hace falta siempre**, con *key* y sin él: **no es lo que resuelve el problema** |
| **«Sí, el chroma no se realiza por *key*»** | **Es falsa de raíz**: el croma es una clase de *key*, la incrustación por color |

**La tercera opción es la más instructiva del cuadernillo**, porque **da la respuesta correcta por una
razón falsa.** **Un opositor que marque «sí» sin leer entero acierta el sí y falla la pregunta.**

## 4. El DVE y la reposición de una señal dentro de una gafa

**La pregunta 29 plantea un caso de directo**: **un *timeline* ya lanzado que va de la presentadora a
una gafa 50/50 y de ahí a una gafa 20/60/20**, y **pregunta si antes de llegar a la tercera se puede
reposicionar la señal del exterior dentro de la gafa.**

**La respuesta oficial es que no, al ser un efecto preprogramado en un *timeline*, no se puede una vez
que se ha lanzado.**

**Y aquí hay que ser exacto, porque es la pregunta más discutible del banco**: **lo que la respuesta
oficial afirma no es que un DVE no se pueda mover.** **Un DVE se mueve en cualquier momento.** **Lo que
afirma es que las posiciones que forman parte de un *timeline* ya en marcha están escritas en el propio
efecto**, y **tocarlas mientras corre no reposiciona la ventana: rompe el efecto o no hace nada, según
el mezclador.** **El *timeline* es una secuencia programada, y una secuencia programada se edita
parada, no en vuelo.**

**Las tres opciones falsas:**

1. **«Necesitaría un tiempo que no tengo»** convierte una imposibilidad de programa en un problema de
   prisa. **No es cuestión de tiempo.**
2. **«Sí, siempre que tenga el canal de DVE necesario»** es cierta para un DVE suelto y falsa dentro de
   un *timeline* lanzado. **Es la opción que más se acerca**, y **la que hay que descartar con el
   matiz, no con el concepto.**
3. **«Sí, nunca hay problema»** es la absoluta de siempre.

**El concepto que hay que llevarse, y que vale para toda la automatización de un control**: **un efecto
programado se comporta como una grabación, no como un mando.** **Se prepara antes o se cancela;
mientras corre, manda él.**

## 5. La macro: la definición del fabricante

**Un macro son las instrucciones que le solicitamos a un mezclador para hacer una serie de pasos con
solo apretar un botón.** Ésa es la respuesta oficial a la pregunta 72.

**Y ésta es de las pocas preguntas de la ocupación que se puede contrastar con documentación de
fabricante.** **El manual en español del mezclador ATEM de Blackmagic Design lo define así:**

> «Una macro es una secuencia de instrucciones que se llevan a cabo automáticamente al presionar un
> botón.»

**El manual añade el ejemplo, que explica el alcance del concepto mejor que cualquier definición:**

> «Por ejemplo, es posible grabar una serie de transiciones entre distintas fuentes que incluyan
> imágenes superpuestas, ajustes del volumen y modificaciones en la configuración de las cámaras.»

**Tres cosas se siguen de ahí, y las tres contestan a las opciones falsas:**

| Opción falsa | Por qué cae |
|---|---|
| **«Un mezclador ligero para eventos con tres cámaras»** | **Confunde la macro con el aparato**: describe un mezclador compacto |
| **«El botón cuya única función es ampliar una imagen»** | **Confunde la macro del mezclador con el objetivo macro de fotografía**: son dos palabras iguales de dos oficios distintos |
| **«El aparato asociado donde se almacenan los efectos»** | **La macro no es un aparato ni vive fuera**: el propio manual dice que **se almacenan en el mezclador** |

**Y el detalle que une esta pregunta con la 29**: **una macro y un *timeline* son la misma idea** —una
secuencia guardada que se lanza con un botón— **y por eso comparten la misma limitación**: **se editan
paradas.**

## 6. El software que programa una emisión entera

**El software que permite programar cada cambio de plano, cada efecto o transición de manera previa y
ejecutarlo en directo durante toda la transmisión de forma automática es Live Edit.** Ésa es la
respuesta oficial a la pregunta 102.

**Es la macro llevada al extremo**: **donde una macro guarda una secuencia corta, un sistema de este
tipo guarda la escaleta entera de un programa**, y **el control pasa de ejecutar a supervisar.** **Es la
tecnología de los grandes eventos musicales y deportivos, donde la realización va escrita compás a
compás.**

**Las tres opciones falsas son nombres verosímiles y ninguno existe con esa función**: **«Avid Program
Mixer» pega el nombre de una casa de edición a una función de mezclador; «Prime TV» suena a canal;
«QE Pilot» juega con el nombre de un sistema real de guiado de realización.** **Son la clase de
distractor que sólo se descarta reconociendo el correcto**, y **por eso esta pregunta es de las que hay
que memorizar.**

**El sistema que sí conviene tener asociado, porque el mismo cuadernillo lo pregunta en el tema 12**:
**CuePilot**, el que sincroniza departamentos con código de tiempo lineal en una realización musical.
**Los dos van en la misma familia: realización programada contra tiempo.**

## 7. Los generadores de caracteres y el intruso

**El equipo que NO tiene entre sus principales funciones ser un generador de caracteres es Mistika.**
Ésa es la respuesta oficial a la pregunta 28 del segundo llamamiento, **y es una pregunta negativa.**

| Equipo | Qué es |
|---|---|
| **Mistika** ✔ *el intruso* | **Un sistema de postproducción, etalonaje y acabado** de la casa SGO: monta, corrige color y compone, **pero no es un rotulador de directo** |
| **Chyron** | **La casa clásica de generadores de caracteres**: su nombre se usa como sinónimo de rótulo en control |
| **Brainstorm IPF** | **Plataforma de grafismo en tiempo real y realidad aumentada**, con generación de caracteres |
| **Ventuz** | **Motor de gráficos en tiempo real** para rotulación y decorados virtuales |

**La regla que ordena la tabla**: **los tres verdaderos son equipos de directo que dibujan sobre la
señal mientras se emite.** **El intruso es un equipo de sala que trabaja con material ya grabado.**
**Es la misma frontera que separaba Infinity Set de DaVinci en la pregunta 6**, y **el cuadernillo la
pregunta dos veces.**

## 8. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 6 | Con qué equipo se hace un croma en tiempo real | b) Infinity Set ✔ |
| 28 | Qué equipo NO es generador de caracteres | a) Mistika ✔ |
| 29 | Si se puede reposicionar una señal en un *timeline* lanzado | a) No, es un efecto preprogramado ✔ |
| 31 | Si se puede trabajar en decorado virtual sin *key* en el mezclador | a) Sí, con la señal en el motor de render y un software que incruste ✔ |
| 72 | Qué es un macro | d) Instrucciones para hacer una serie de pasos con un botón ✔ |
| 77 | Con qué colores se puede hacer un *chroma key* | a) Cualquier color ✔ |
| 102 | Qué software programa cada cambio de plano y lo ejecuta solo | d) Live Edit ✔ |

**Las siete respuestas oficiales son correctas.**

**Y el reparto de dificultad, que en este tema es muy desigual**: **cuatro se contestan razonando** —la
6, la 28, la 31 y la 77, todas ellas por la frontera entre directo y postproducción o por la trampa del
«sólo»— **y tres exigen conocer un nombre o un comportamiento concreto de aparato**: la 29, la 72 y la
102. **Las cuatro primeras no hay que memorizarlas; las tres últimas, sí.**

## 9. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son los conceptos generales del mezclador, y **va como
oficio**, salvo una definición que sí tiene documentación de fabricante y dos nombres comerciales que
descansan en la plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Cuarto: documentación de fabricante** | **Manual en español del mezclador ATEM de Blackmagic Design**, epígrafe «¿Qué es una macro?» | Pregunta 72 |
| **Quinto: la plantilla oficial** | **Dos afirmaciones**: los nombres comerciales de la pregunta 102 y el reparto de funciones de los cuatro equipos de la pregunta 28 | Preguntas 28 y 102 |

**Tres declaraciones expresas:**

1. **La definición de macro del epígrafe 5 está citada literalmente del manual de un fabricante**, y
   **el fabricante es uno concreto.** **Otros mezcladores llaman a lo mismo «macro», «secuencia» o
   «*snapshot* encadenado»**, y **el concepto es el mismo en todos**, pero **la literalidad de la cita
   alcanza sólo al manual citado.**
2. **Los nombres comerciales de las preguntas 28 y 102 no se han contrastado en catálogo.** **La
   documentación de SGO, Chyron, Brainstorm, Ventuz y del sistema que la pregunta 102 nombra no se ha
   consultado.** **Lo que el tema sostiene es la frontera —equipos de directo contra equipos de
   sala—**, que **es la que hace contestable la pregunta 28 sin memorizar catálogos.** **La respuesta a
   la 102 descansa en la plantilla.**
3. **«Gafa» no es un término normalizado.** **Es vocabulario de plató español para una composición de
   varias ventanas en pantalla**, y **el temario lo traduce porque el enunciado de la pregunta 29 lo da
   por sabido.**

**El resto del tema va como oficio y así se declara**: las cinco funciones del mezclador, el mecanismo
del *chroma key* y por qué el verde y el azul son costumbre y no obligación, la posibilidad de incrustar
aguas arriba del mezclador, el comportamiento de un efecto programado en vuelo y el paralelo entre macro
y *timeline*. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y
el tema no lo presenta como si lo estuviera.
