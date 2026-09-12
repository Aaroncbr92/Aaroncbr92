# Tema 9 del específico de Información Gráfica y Captación de Imagen y Sonido · Envíos, directos y cámaras robotizadas

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Información Gráfica y Captación de Imagen y Sonido · punto 9 |
| **Sirve para** | **Información Gráfica y Captación de Imagen y Sonido** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los sistemas de envío de señal, las cámaras robotizadas y los entornos de realidad aumentada, virtual y mixta, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Aviso de reparto** | **Tres preguntas: el punto menos preguntado de la ocupación**, y **su subpunto de realidad aumentada, virtual y mixta no ha salido en absoluto**. El temario lo desarrolla igual, porque el programa lo manda |
| **Extensión** | **2.406 palabras** |

<!-- /portada -->

Las siglas y rótulos de este tema, presentados de entrada: el protocolo de transferencia de ficheros
(**FTP**, *file transfer protocol*); la difusión continua por internet (***streaming***); la red
inalámbrica local (**Wifi**) y la red por cable (**Ethernet**); la cámara panorámica-inclinable-zoom
integrada (**PTZ**, *pan-tilt-zoom*); la empresa de trabajo temporal (**ETT**), que aparece en una
opción falsa donde debería ir un equipo técnico; y el rótulo **CUT** de las consolas de robótica, que
es una orden y no una sigla.

> Enunciado de la convocatoria (Anexo 2, temario específico de Información Gráfica y Captación de
> Sonido, puntos 3.11, 3.12 y 3.14):
> «Cámaras robotizadas, integradas PTZ y no integradas.»
> «Sistemas de envíos de noticias y directos: Tipos y usos (mochilas, ftp, streaming …).»
> «Operación de cámara en entornos de realidad aumentada AR, virtual VR y mixta.»

**Tres preguntas: el punto menos preguntado de la ocupación.** Y aun así **cubre dos materias que un
reportero gráfico usa todos los días**: **cómo sale la señal de una localización** y **cómo se opera
una cámara robotizada**.

<!-- indice -->

## Índice

- [1. Las formas de sacar la señal de una localización](#1-las-formas-de-sacar-la-señal-de-una-localización)
- [2. La mochila: qué es y qué no promete](#2-la-mochila-qué-es-y-qué-no-promete)
- [3. Por dónde se conecta una mochila](#3-por-dónde-se-conecta-una-mochila)
- [4. Las cámaras robotizadas](#4-las-cámaras-robotizadas)
- [5. La orden de corte en una consola de robótica](#5-la-orden-de-corte-en-una-consola-de-robótica)
- [6. La realidad aumentada, virtual y mixta](#6-la-realidad-aumentada-virtual-y-mixta)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Las formas de sacar la señal de una localización

| Camino | Qué es | Cuándo se usa |
|---|---|---|
| **Radioenlace de microondas** | **Punto a punto**, con antena parabólica apuntada | **Directo con línea de vista** y calidad garantizada |
| **Satélite** | Unidad con antena orientable | **Donde no hay nada más**: exteriores remotos |
| **Fibra contratada** | Línea dedicada | Eventos previstos con antelación |
| **Mochila de agregación celular** | **Varias tarjetas de telefonía sumadas** | **Directo desde donde hay cobertura móvil** |
| **Transferencia de ficheros** | **El material grabado se envía como fichero** | **Cuando no hace falta directo**: la mayoría de las piezas |
| **Difusión continua por internet** | Emisión hacia un servidor | Canales propios y redes |

**La distinción que ordena el punto**: **directo o diferido.** **Un directo necesita caudal
garantizado en ese instante; un envío de fichero puede tardar y reintentar.** **De ahí que la mochila
sea la máquina del directo y la transferencia de ficheros la del diferido.**

## 2. La mochila: qué es y qué no promete

**Una mochila de transmisión es un equipo portátil que envía vídeo y audio por las redes de telefonía
móvil**, **sumando el caudal de varias tarjetas a la vez** para conseguir el ancho de banda que una
sola no daría.

**Qué permite, y son las tres cosas que el examen enumera como ciertas:**

1. **Aprovechar la capacidad disponible en las redes de telefonía móvil para enviar una señal de vídeo
   y audio.**
2. **En zonas de cobertura de telefonía móvil, llegar al lugar de la noticia, conectar la cámara a la
   mochila, encender el equipo y emitir en directo.**
3. **Evitar configuraciones complejas de transmisión, reducir costes de producción y conseguir
   presupuestos más ajustados.**

**La afirmación que NO responde correctamente al enunciado es «tener transmisiones cien por cien
estables punto a punto, sin retardos, en zonas con poca cobertura móvil».** Ésa es la respuesta oficial
a la pregunta 84.

**Por qué es falsa, y son tres motivos, cada uno suficiente:**

| Lo que afirma | Por qué no |
|---|---|
| **«Cien por cien estables»** | **Ninguna transmisión celular lo es.** El caudal disponible **depende de cuánta gente use la misma célula**, y en un acontecimiento con público **la red se satura precisamente donde está la noticia** |
| **«Sin retardos»** | **La agregación celular introduce SIEMPRE un retardo**, de segundos: **la mochila almacena, reparte entre las tarjetas, reordena y entrega**. **Es su forma de funcionar, no un defecto** |
| **«En zonas con poca cobertura móvil»** | **Es lo contrario de su condición de uso.** **Sin cobertura no hay caudal**, y la propia opción b) del examen lo dice: «en zonas de cobertura de telefonía móvil» |

**La forma de contestarla**: **el enunciado pide la afirmación que NO es correcta**, y **la falsa es la
única que promete algo absoluto**: «cien por cien», «sin retardos». **Cualquier afirmación que
prometa perfección sobre una red compartida es falsa por construcción.**

**El aviso de oficio que este epígrafe deja**: **el retardo de una mochila es lo que obliga a que el
presentador de estudio espere después de dar paso**, y **es la razón de los silencios incómodos en los
directos**. **No es un fallo del equipo: es cómo funciona.**

## 3. Por dónde se conecta una mochila

**Un equipo de transmisión con una mochila se puede conectar para enviar señal mediante tarjetas de
telefonía, Wifi y cable de red.** Ésa es la respuesta oficial a la pregunta 92.

**Las tres vías, y por qué las tres:**

| Vía | Cuándo se usa |
|---|---|
| **Tarjetas de telefonía** | **La habitual**: varias a la vez, de operadores distintos, sumando caudal |
| **Red inalámbrica local** | **Cuando hay una red disponible en el sitio**: un hotel, un pabellón, una sede |
| **Cable de red** | **Cuando hay línea fija**: es **la más estable de las tres** |

**La lógica de la máquina, que es lo que hace la respuesta razonable**: **la mochila no es un
transmisor de radio: es un agregador de enlaces de datos.** **Le da igual de dónde venga el caudal**:
lo que hace es **repartir el flujo entre todos los caminos disponibles y reconstruirlo al otro lado**.
**Por eso admite las tres vías, y por eso puede usarlas simultáneamente.**

**Las tres opciones falsas y su error:**

| Opción | Qué es en realidad |
|---|---|
| «Enlace terrestre» | **Es el radioenlace de microondas**: otra tecnología, con su antena y su licencia |
| «Ondas hertzianas» | **Es cualquier transmisión de radio**: demasiado general, y **no es como se conecta una mochila** |
| «Una Unidad ETT» | **No existe como equipo técnico**: **ETT es la sigla de empresa de trabajo temporal**. **Es un distractor construido con una sigla real de otro campo** |

**La opción d) merece la mención**, porque **es del tipo que este cuadernillo repite**: **una sigla que
existe en otro ámbito, colocada donde parece técnica.** **Se descarta reconociendo la sigla, no
sabiendo de transmisión.**

## 4. Las cámaras robotizadas

**Una cámara robotizada es una cámara cuyos movimientos y cuya óptica se gobiernan a distancia, y que
puede memorizar posiciones y repetirlas.**

| Familia | Qué es |
|---|---|
| **Integrada** o **PTZ** | **Cámara, óptica y motores en un solo cuerpo compacto.** **Se cuelga del techo o se pone en una esquina** |
| **No integrada** | **Una cabeza robotizada sobre la que se monta una cámara y una óptica normales**, con o sin pedestal robotizado |
| **Sobre raíl o pedestal robotizado** | **La cámara además se desplaza**, no sólo gira |

**La diferencia que importa en televisión**: **la integrada es pequeña, barata y va donde no cabe nada
más, a cambio de sensor y óptica limitados; la no integrada da la calidad de una cámara de estudio y
ocupa lo que ocupa una cámara de estudio.**

**Cómo se opera**: **un operador gobierna varias cámaras desde una consola con palanca y pantalla
táctil**. **Su trabajo no es encuadrar cámara a cámara en directo**, sino **preparar posiciones
memorizadas antes del programa y llamarlas cuando el realizador las pide**.

| Elemento de la consola | Qué hace |
|---|---|
| **Palanca** | Movimiento libre de panorámica y cabeceo |
| **Mandos de zoom y foco** | La óptica |
| **Posiciones memorizadas** | **Encuadres guardados, con su velocidad de llegada** |
| **Velocidad o tiempo de recorrido** | **Cuánto tarda la cámara en ir de un encuadre a otro** |
| **Orden de corte** | **Ir a un encuadre memorizado inmediatamente** |

## 5. La orden de corte en una consola de robótica

**La función de corte en las consolas de control y pantallas táctiles usadas para la operación de los
sistemas de cámaras robotizadas sirve para ir rápidamente a un plano memorizado con anterioridad,
ignorando el tiempo preestablecido en el plano.** Ésa es la respuesta oficial a la pregunta 102.

**Por qué existe, y es la razón que hace la respuesta deducible**: **cada posición memorizada se guarda
con un tiempo de recorrido**, porque **normalmente se quiere que la cámara llegue despacio y de forma
elegante**. **Pero a veces no hay tiempo**: **el realizador cambia de plan y la cámara tiene que estar
en el otro encuadre ya**. **La orden de corte salta ese tiempo y manda la cámara a la posición a la
máxima velocidad.**

**La consecuencia de oficio**: **una cámara movida con la orden de corte no se puede sacar en antena
mientras se mueve**. **Se usa cuando la cámara está fuera de emisión** y hay que **recolocarla antes de
que la pidan.**

**Las tres opciones falsas y su error, que es de vocabulario:**

| Opción | Qué describe |
|---|---|
| «Cambiar por corte entre las diferentes cámaras del sistema» | **LA TRAMPA BUENA**: **eso es lo que hace la orden de corte de un MEZCLADOR DE VÍDEO**, no la de una consola de robótica. **La misma palabra en dos aparatos distintos significa dos cosas distintas** |
| «Cambiar un plano entre dos secuencias grabadas» | **Es una operación de montaje** |
| «Poder dividir una secuencia de planos» | **Es otra operación de edición** |

**La opción a) es la que más gente marca**, y con razón: **«corte» significa exactamente eso en un
mezclador**. **Lo que la descarta es el enunciado**, que dice **«en las consolas de control de los
sistemas de cámaras robotizadas»**: **ahí la palabra designa la forma de llegar a una posición, no un
cambio de fuente.**

**El aviso de estudio que esta pregunta deja**: **el mismo rótulo puede significar cosas distintas en
aparatos distintos.** **Antes de contestar hay que leer de qué máquina habla el enunciado.**

## 6. La realidad aumentada, virtual y mixta

**El punto 3.14 del anexo pide la operación de cámara en estos entornos**, y **el examen no ha
preguntado nada de ellos**. **El temario los desarrolla porque el programa los manda**, y porque su
vocabulario aparece en las convocatorias.

| Entorno | Qué es | Qué exige a la cámara |
|---|---|---|
| **Realidad virtual** | **Todo el fondo es sintético**: el plató es un croma | **Seguimiento exacto de la posición y de la óptica** |
| **Realidad aumentada** | **El plató es real y se le añaden elementos sintéticos** | Lo mismo, y además **oclusión correcta**: que el objeto virtual pase por delante o por detrás según toque |
| **Realidad mixta** | **Los dos mundos interactúan** | Lo anterior más **coherencia de sombras y reflejos** |

**Lo que todos tienen en común, y es lo único que un operador necesita retener**: **el sistema tiene
que saber en todo momento dónde está la cámara y qué óptica lleva**. **Sin esos datos, el fondo
sintético no se mueve como debería y el truco se cae.**

**Los tres caminos para obtener esos datos:**

| Sistema | Cómo mide |
|---|---|
| **Cabeza y pedestal codificados** | **Sensores en los ejes mecánicos**: la máquina sabe cuánto ha girado |
| **Seguimiento por marcas** | **Una cámara auxiliar lee marcas retrorreflectantes** en el techo o las paredes |
| **Seguimiento sin marcas** | **Reconocimiento de la propia escena** |

**Y la consecuencia para el operador de cámara**: **en un entorno virtual no se puede mover la cámara
como se quiera.** **Hay recorridos calibrados y hay límites**, y **salirse de ellos rompe la
composición**. **El operador trabaja con menos libertad y más disciplina que en un plató normal.**

## 7. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 84 | Cuál NO responde correctamente a lo que permite una mochila | d) Transmisiones cien por cien estables, sin retardos y con poca cobertura ✔ |
| 92 | Por dónde se conecta una mochila para enviar señal | c) Tarjetas de telefonía, Wifi y cable de red ✔ |
| 102 | Para qué sirve la orden de corte en una consola de robótica | d) Ir rápidamente a un plano memorizado ignorando su tiempo ✔ |

**Las tres respuestas oficiales son correctas**, y **ninguna descansa sólo en la plantilla**: las tres
se sostienen en cómo funciona la agregación celular y en cómo se opera una consola de robótica.

**Dos avisos de estudio.** **La pregunta 84 se contesta buscando la opción que promete perfección**:
«cien por cien», «sin retardos». **Cualquier promesa absoluta sobre una red compartida es falsa por
construcción.** **Y la 102 explota que el mismo rótulo significa cosas distintas en dos aparatos**: la
orden de corte de un mezclador cambia de fuente; la de una consola de robótica cambia de encuadre.

**Un aviso de reparto**: **tres preguntas de ciento seis**, **el punto menos preguntado de la
ocupación**, y **el subpunto 3.14 del anexo —realidad aumentada, virtual y mixta— no ha salido en
absoluto**. **El temario lo desarrolla igual**, porque el programa lo manda.

## 8. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son los sistemas de envío de señal, las cámaras
robotizadas y los entornos de realidad aumentada, virtual y mixta, y **va entera como oficio**.

**Ninguna de sus tres respuestas descansa sólo en la plantilla.** El funcionamiento de la agregación
celular y su retardo inevitable, las vías de conexión de una mochila y el comportamiento de la orden
de corte en una consola de robótica **son conocimiento de oficio**, verificable en la práctica del
sector.

**Dos declaraciones expresas:**

1. **La documentación de los fabricantes de mochilas y de sistemas de robótica no se ha consultado.**
   **Ninguna respuesta de este punto depende de una especificación de catálogo**: lo que se pregunta es
   **qué permite y qué no permite la tecnología**, y **cómo se comporta una orden de consola**. **El
   proyecto sí conserva la ficha de un modelo de mochila**, consultada para otro volumen, **y este
   tema no la necesita**: **las tres preguntas se contestan con el principio de funcionamiento.**
2. **El subpunto 3.14 del anexo se desarrolla sin ninguna pregunta que lo respalde.** **No hay examen
   contra el que calibrar ese epígrafe**, así que **lo que el tema recoge es el vocabulario y los
   principios comunes de los tres entornos**, **sin atribuir a ninguna fuente cifras ni
   especificaciones.** **Es un epígrafe de programa, no de examen**, y así se declara.
