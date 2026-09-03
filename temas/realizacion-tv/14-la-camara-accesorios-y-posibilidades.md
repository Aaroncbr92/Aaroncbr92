# Tema 14 del específico de Realización Televisión · La cámara: accesorios y posibilidades

Las siglas y términos de este tema, presentados de entrada: la unidad de control de cámara (**CCU**,
*camera control unit*), el panel de control remoto desde el que se gobierna (**RCP**, *remote control
panel*, llamado **OCP** —*operational control panel*— por algunos fabricantes), la cámara robotizada de
panorámica, inclinación y zoom (**PTZ**, *pan-tilt-zoom*), el dispositivo de carga acoplada de los
sensores clásicos de televisión (**CCD**, *charge-coupled device*), el filtro óptico de paso bajo que
evita el aliasing (**OLPF**, *optical low-pass filter*), el decibelio (**dB**) como unidad de ganancia,
la grúa de brazo (***jib***), el protocolo de red sobre el que viaja hoy casi todo (**IP**,
*internet protocol*), la unidad de reportaje móvil con que se cubren las retransmisiones pequeñas
(**URM**) y la letra griega **Φ** (fi), que en el cuerpo de una cámara no es una sigla sino una
marca.

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización, punto 4.2):
> «LA REALIZACIÓN. La cámara accesorios y posibilidades. Nociones básicas sobre la cámara. Objetivos y
> sus características. Foco. Profundidad de campo. Diagrama. Filtros. Soportes cámara. Estabilizadores
> y otros accesorios.»

**Quince preguntas: el segundo banco de esta ocupación**, sólo por detrás del de producción de
programas directos y grabados. **Y el punto que más pregunta por objetos concretos** —un cangrejo, un
*slider*, una *mini jib*, un signo grabado en una carcasa—, **que es la clase de pregunta que no se
deduce: se sabe o no se sabe.**

**Una advertencia sobre el enunciado, antes de entrar**: **donde el anexo escribe «Diagrama» hay que
leer «Diafragma».** **Es una errata del propio pliego** —la lista es «Foco. Profundidad de campo.
Diagrama. Filtros»: los cuatro conceptos de una óptica—, y **el examen lo confirma**: la pregunta 57
pregunta por el diafragma, y ninguna de las 229 preguntas del bloque específico pregunta por un
diagrama. **El temario desarrolla el diafragma y lo declara aquí en lugar de arrastrar la errata.**

<!-- indice -->

## Índice

- [1. La cadena de control de una cámara de estudio](#1-la-cadena-de-control-de-una-cámara-de-estudio)
- [2. Qué se gobierna desde el panel: el RCP](#2-qué-se-gobierna-desde-el-panel-el-rcp)
- [3. La ganancia: lo único que no aporta es luz](#3-la-ganancia-lo-único-que-no-aporta-es-luz)
- [4. El balance de blancos y la superficie de referencia](#4-el-balance-de-blancos-y-la-superficie-de-referencia)
- [5. Los defectos de la imagen captada](#5-los-defectos-de-la-imagen-captada)
- [6. Los objetivos por su ángulo de visión](#6-los-objetivos-por-su-ángulo-de-visión)
- [7. El signo Φ: dónde empieza a medirse la distancia](#7-el-signo-φ-dónde-empieza-a-medirse-la-distancia)
- [8. El dolly-zoom](#8-el-dolly-zoom)
- [9. Los soportes de cámara](#9-los-soportes-de-cámara)
- [10. La estabilización: pasiva y activa](#10-la-estabilización-pasiva-y-activa)
- [11. Las cámaras sin operador detrás: PTZ y Twin Cam](#11-las-cámaras-sin-operador-detrás-ptz-y-twin-cam)
- [12. La pregunta que depende de una planta](#12-la-pregunta-que-depende-de-una-planta)
- [13. Los datos que el examen ha preguntado](#13-los-datos-que-el-examen-ha-preguntado)
- [14. Trazabilidad](#14-trazabilidad)

<!-- /indice -->

## 1. La cadena de control de una cámara de estudio

**Una cámara de televisión de estudio no es un aparato: es una cadena de tres piezas**, y **el examen
pregunta por las dos que no se ven en plató.**

| Pieza | Dónde está | Qué hace |
|---|---|---|
| **Cabeza de cámara** | En plató, sobre su soporte | **Capta**: óptica, sensor, visor, servos |
| **CCU** | En el control técnico, en un bastidor | **Procesa y alimenta**: envía la señal ya tratada al mezclador |
| **RCP** | En el control de imagen, delante del técnico | **Manda**: es el mando a distancia de la CCU |

**Qué es una CCU en televisión**: **una unidad para controlar los parámetros de cámara de televisión.**
Ésa es la respuesta oficial a la pregunta 52.

**Las tres opciones falsas describen aparatos que existen, y por eso engañan:**

| Opción | Qué describe en realidad |
|---|---|
| **Corregir la colorimetría en postproducción** | **Un etalonador** —DaVinci Resolve, Baselight—, que trabaja sobre material ya grabado |
| **Unidad de realización de pequeño formato** | **Una unidad móvil ligera**, una URM o un *flypack* |
| **Unidad para lanzar vídeos a remoto** | **Un servidor de vídeo** o un sistema de reproducción, no un control de cámara |

**La diferencia que separa a la CCU de todas ellas es el tiempo**: **la CCU trabaja sobre la señal
mientras se está generando**, y **las tres falsas trabajan sobre señal que ya existe.**

**Y la cadena explica por qué el monitor de grado 1 es prioritario en el puesto de CCU** —que es la
pregunta 9, del tema 11—: **quien decide el nivel de negro, el diafragma y el color de una cámara
necesita el único monitor del control que no miente.**

## 2. Qué se gobierna desde el panel: el RCP

**El RCP es el panel desde el que un técnico de imagen gobierna varias cámaras a la vez**, cada una con
su columna de mandos. **Lo que se controla con un RCP es el diafragma, la crominancia y la velocidad de
obturación.** Ésa es la respuesta oficial a la pregunta 57.

**Los tres mandos, uno a uno:**

| Mando | Qué ajusta |
|---|---|
| **Diafragma** | **La abertura del iris del objetivo**: cuánta luz entra. Es el mando de la palanca grande del panel |
| **Crominancia** | **El color**: balance de blancos y de negros, matriz, saturación —lo que el oficio llama «pintar» la cámara |
| **Obturación** | **Cuánto tiempo está expuesto cada fotograma**: fija el barrido de movimiento y evita el parpadeo de las pantallas en plató |

**A los tres se suman en la práctica el nivel de negro y la ganancia**, que son los epígrafes 3 y 4 de
este tema.

**Las tres opciones falsas y dónde vive de verdad cada mando:**

1. **El servomotor de zoom** no se manda desde el control: **se manda desde el propio operador**, con la
   empuñadura de zoom montada en el brazo del trípode. **El control no encuadra**; el operador sí.
2. **El formato de grabación** se elige **en el menú de la cámara o del grabador**, y en una cámara de
   estudio ni siquiera existe como parámetro: **la señal sale hacia el control y se graba allí.**
3. **La estabilización interna de las lentes** es **un interruptor del objetivo**, mecánico u óptico, y
   no viaja por el cable de triaxial ni de fibra que une cabeza y CCU.

**La regla que ordena las cuatro opciones**: **por el RCP viaja lo que altera la señal; por las manos
del operador, lo que altera el encuadre.** **Diafragma, color y obturación alteran la señal. Zoom,
formato y estabilizador, no.**

## 3. La ganancia: lo único que no aporta es luz

**La ganancia es amplificación electrónica de la señal que ya ha salido del sensor.** **Si se
incrementa la ganancia de una cámara, a nivel de imagen habrá más ruido.** Ésa es la respuesta oficial
a la pregunta 62.

**Y el porqué es la parte que hay que entender, porque la trampa está en la opción a):**

**La imagen se ve más clara, pero no hay más luz.** **La luz la fija el diafragma, el obturador y lo
que haya en el plató.** **La ganancia multiplica lo que el sensor entregó**, y **el sensor entrega dos
cosas mezcladas: señal y ruido.** **Al multiplicar, se multiplican las dos**, y **como la señal ya
estaba escasa —por eso se sube la ganancia— lo que se nota es el ruido.**

| Opción | Por qué se cae |
|---|---|
| **Habrá más luz** | **No entra ni un fotón más**: sube el nivel de la señal, no la iluminación |
| **Habrá más definición** | **La ganancia no añade detalle**: amplifica el que hubiera, y al enterrarlo en ruido lo empeora |
| **Habrá menos ruido** | **Justo lo contrario**: la ganancia es la causa del ruido, no su remedio |
| **Habrá más ruido** ✔ | **La respuesta** |

**El equivalente que conviene tener a mano**: **seis decibelios de ganancia equivalen a un paso de
diafragma**, porque **veinte veces el logaritmo decimal de dos son aproximadamente seis.** **De ahí que
un +6 dB, un +12 dB y un +18 dB en el menú sean uno, dos y tres diafragmas**, y **también uno, dos y
tres escalones de ruido.**

## 4. El balance de blancos y la superficie de referencia

**El balance de blancos es la operación por la que se le dice a la cámara «esto es blanco».** **La
cámara mide qué proporción de rojo, verde y azul le llega de esa superficie y ajusta las ganancias de
los canales para que salga neutra.**

**De ahí sale la regla de familia que contesta la pregunta 100, y cualquier otra de su clase:**

> **La cámara empuja la imagen hacia el color complementario del de la superficie sobre la que se
> balancea.**

**Si se repite el balance sobre un pantalón vaquero azul claro después de haberlo hecho sobre papel
blanco, la imagen resultante tendrá un tono más cálido.** Ésa es la respuesta oficial a la pregunta
100.

**El razonamiento, paso a paso**: **la cámara recibe de ese vaquero mucho más azul que rojo.** **Como
tiene orden de ver esa superficie como blanca, baja la ganancia del canal azul y sube la del rojo.**
**Ese ajuste no se queda en el vaquero: se aplica a toda la imagen.** **Todo lo demás sale, por tanto,
con menos azul y más rojo: más cálido.**

**Y la opción a) merece una nota, porque es falsa y además es una técnica real**: **el balance de
blancos no sólo se puede hacer sobre una superficie blanca.** **Balancear sobre una superficie de color
es un recurso corriente de fotografía**, precisamente para forzar una dominante: **se balancea sobre
azul para calentar y sobre naranja para enfriar.** **Lo que la pregunta llama error es una herramienta.**

| Superficie de balance | Cómo sale la imagen |
|---|---|
| **Blanco o gris neutro** | **Neutra**: es el uso normal |
| **Azul** | **Cálida** —la de la pregunta 100— |
| **Naranja o ámbar** | **Fría** |
| **Verde** | **Magenta** |

## 5. Los defectos de la imagen captada

**El efecto que se produce en las cámaras con CCD cuando se pierde detalle por contaminación de
información entre diodos vecinos es el *blooming*.** Ésa es la respuesta oficial a la pregunta 83.

**Los tres defectos que el examen pone juntos son distintos y se distinguen a simple vista:**

| Defecto | Qué se ve | Por qué ocurre |
|---|---|---|
| ***Blooming*** ✔ | **Un halo o una mancha alrededor de una zona muy iluminada**, que se come el detalle | **Un fotodiodo saturado desborda su carga hacia los vecinos** |
| ***Smear*** | **Una raya vertical luminosa que atraviesa la imagen de arriba abajo** desde una fuente muy brillante | **La carga se cuela en el registro de transferencia vertical del CCD** |
| ***Moiré*** | **Un dibujo de ondas o de colores falsos** sobre una trama fina —una corbata de rayas, una rejilla— | **Interferencia entre la trama del sujeto y la del sensor**: se combate con el filtro óptico de paso bajo, el OLPF |

**La opción a), «perla», no nombra ningún defecto de sensor.** **No aparece en la literatura técnica de
captación con ese sentido**, y **funciona en la pregunta como distractor puro**: **es la única de las
cuatro que no es un término del oficio.** **Conviene saberlo, porque descartar una opción por no existir
es tan válido como reconocer la correcta.**

**Y la clave que separa a las dos primeras, que es lo que la pregunta mide**: ***blooming* es
contaminación entre vecinos —se extiende en todas direcciones—; *smear* es contaminación por el camino
de lectura —se extiende sólo en vertical.** **El enunciado dice «entre diodos vecinos», y ésa es la
firma del *blooming*.**

## 6. Los objetivos por su ángulo de visión

**Un objetivo con un ángulo de visión entre 60º y 25º es un objetivo normal.** Ésa es la respuesta
oficial a la pregunta 73.

**La clasificación corriente, que es la que el examen usa:**

| Tipo | Ángulo de visión | Cómo se comporta |
|---|---|---|
| **Gran angular** | **Más de 60º** | **Exagera la perspectiva**: lo cercano crece, el fondo se aleja |
| **Normal** ✔ | **De 60º a 25º** | **Se parece a la visión humana**: ni comprime ni exagera |
| **Teleobjetivo** | **De 25º a 10º** | **Comprime la perspectiva**: acerca el fondo al primer término |
| **Superteleobjetivo** | **Menos de 10º** | **Compresión extrema** y **profundidad de campo mínima** |

**La otra manera de decir lo mismo, y la que se usa en plató**: **el objetivo normal es aquel cuya
distancia focal se aproxima a la diagonal del sensor.** **Por eso «normal» no es una focal fija**: en un
sensor de 2/3 de pulgada ronda los 12 mm, y en 35 mm de fotografía, los 50 mm. **El ángulo, en cambio,
sí es comparable entre formatos**, y por eso el examen pregunta por el ángulo.

**Y una salvedad honrada**: **estos tramos son convención, no norma.** **Los manuales mueven los
límites algunos grados**, y **lo que ninguno mueve es el orden**: a más ángulo, más angular; a menos
ángulo, más tele. **Con esa convención el resultado coincide con la plantilla.**

**El puente con el tema 13**: **la pregunta 28 de aquel cuadernillo pregunta qué tamaños de plano se
pueden obtener con un objetivo determinado.** **La respuesta se lee en la referencia del objetivo**
—relación de zoom por focal mínima: un HJ17x va de una focal mínima a diecisiete veces esa focal—, y
**el recorrido resultante es amplio pero finito.**

## 7. El signo Φ: dónde empieza a medirse la distancia

**El signo Φ que se ve en el cuerpo de muchas cámaras indica el punto en el que se encuentra el plano
focal de la cámara.** Ésa es la respuesta oficial a la pregunta 25.

**Para qué sirve**: **la distancia de enfoque no se mide desde la punta del objetivo ni desde el
trípode: se mide desde el plano del sensor.** **El ayudante de cámara que tira de cinta métrica para
marcar un foco engancha la cinta en esa marca.** **En una óptica de gran distancia mínima de enfoque la
diferencia entre medir desde el frontal y medir desde el plano focal es de centímetros; en un macro,
esa diferencia es todo el margen que hay.**

**Las tres opciones falsas describen cosas que sí existen, pero se marcan de otra manera:**

| Opción | Qué es de verdad, y cómo se rotula |
|---|---|
| **Plantilla áurea en el visor** | **Una retícula o guía de encuadre**, que se activa en el menú del visor, no se graba en la carcasa |
| **Rango dinámico del sistema óptico** | **Una característica del sensor**, que se expresa en pasos de diafragma o en decibelios, y **no tiene nada que ver con la ilusión de movimiento aparente** que la opción le añade |
| **Atenuación de la definición contra el aliasing** | **El filtro óptico de paso bajo, el OLPF**, que va delante del sensor y **no se anuncia con ninguna marca externa** |

**El detalle que delata a la opción c) sin saber nada de Φ**: **mezcla dos conceptos que no se tocan.**
**El rango dinámico es cuánto contraste cabe en la imagen; la ilusión de movimiento aparente es por qué
vemos moverse una sucesión de fotogramas.** **Una opción que une dos definiciones correctas de cosas
distintas casi siempre es falsa**, y **es un patrón que se repite en este cuadernillo.**

## 8. El dolly-zoom

**Para distorsionar la perspectiva del fondo manteniendo estable el objeto principal se utiliza el
dolly-zoom.** Ésa es la respuesta oficial a la pregunta 106.

**Cómo se hace**: **se desplaza la cámara hacia el sujeto mientras se abre el zoom, o se aleja mientras
se cierra.** **Las dos acciones se compensan sobre el sujeto —que conserva su tamaño en cuadro— y no se
compensan sobre el fondo**, porque **el desplazamiento cambia la perspectiva y el zoom no.** **El
resultado es un fondo que se abalanza o se despega mientras el sujeto no se mueve.**

**Recibe también los nombres de efecto Vértigo** —por la película de Hitchcock donde se popularizó—,
***contra-zoom*, *zoom* compensado o travelling compensado**, y **es el ejemplo de manual de que zoom y
travelling no son intercambiables.**

**Las tres opciones falsas:**

1. **El ojo de pez** distorsiona, sí, **pero distorsiona todo el cuadro, el sujeto incluido**, y **lo
   hace de forma fija**: no hay evolución dentro del plano.
2. **«Sólo con edición en After Effects»** es falsa **por el «sólo»**: es un efecto que se rueda, y las
   opciones que absolutizan son las que primero hay que mirar con desconfianza.
3. **Contrapicar** cambia el punto de vista y la relación de poder del encuadre, **pero no altera la
   relación de perspectiva entre sujeto y fondo.**

## 9. Los soportes de cámara

**Tres preguntas del cuadernillo son de vocabulario de soportes**, y **se contestan con una tabla:**

| Accesorio | Qué es |
|---|---|
| **Cangrejo** (o araña) | **Un soporte extensible acoplado al trípode para evitar que resbale** ✔ —pregunta 94— |
| ***Slider*** | **Un rail con un sistema de ruedas sobre el que se pone la cámara** ✔ —pregunta 78— |
| ***Mini jib*** | **Una grúa pequeña** ✔ —pregunta 17— |
| **Dolly** | **Una plataforma con ruedas** sobre la que va el trípode o el pedestal, para travellings |
| **Pedestal** | **Columna neumática o hidráulica** que sube y baja la cámara con una mano |
| **Cabeza fluida** | **La cabeza del trípode**, con frenos y fricción regulables para panorámicas suaves |

**Y las opciones falsas de las tres preguntas son, cada una, otro accesorio de la lista**, que es lo que
las hace útiles para estudiar:

| Lo que dice la opción falsa | Cómo se llama de verdad |
|---|---|
| **Arnés que sujeta la cámara al cuerpo** | **El chaleco y el brazo de una steadicam** |
| **Ventosa para adherir cámaras ligeras a una superficie lisa** | **Una ventosa o copa de succión**, la de las cámaras de coche |
| **Columna central neumática fijada sobre una base** | **Un pedestal** |
| **Jirafa de sonido** | **Una pértiga**, que sostiene un micrófono, no una cámara |
| **Cámara pequeña operada a control remoto** | **Una minicámara o una PTZ** |
| **Steadicam para cámaras ligeras** | **Un estabilizador de mano o un gimbal** |
| **Soporte para iluminación** | **Un pie de foco o un trípode de iluminación** |
| **Grúa de brazo rígido** | **Una jib o una pluma**, que es justo lo que un *slider* no es |

**La diferencia que ordena las tres respuestas**: **el cangrejo sujeta el suelo, el *slider* mueve la
cámara en línea recta y la *jib* la mueve en arco.** **Ninguno de los tres estabiliza.**

## 10. La estabilización: pasiva y activa

**La estabilización pasiva es la capacidad de mantener fija la orientación de la cámara a través de los
medios mecánicos de un soporte.** Ésa es la respuesta oficial a la pregunta 68.

**Las dos familias:**

| Familia | Con qué lo consigue | Ejemplos |
|---|---|---|
| **Pasiva** ✔ | **Sólo medios mecánicos**: masa, inercia, contrapesos, cardanes libres, brazos con muelles | **La steadicam clásica**, los brazos articulados con resorte, los cardanes sin motor |
| **Activa** | **Motores y electrónica**: sensores que miden el movimiento y motores que lo corrigen | **Los gimbals motorizados de tres ejes**, los giroestabilizados de helicóptero, la estabilización óptica de la lente |

**La opción a) es la que más se parece a la correcta y por eso hay que separarla bien**: **«las
fricciones de un soporte» no estabilizan: amortiguan.** **La fricción de una cabeza fluida hace que una
panorámica salga suave**, pero **no mantiene fija la orientación de la cámara**: si el operador la
suelta, la cabeza se queda donde estaba porque tiene freno, no porque estabilice. **Amortiguar es
suavizar un movimiento; estabilizar es cancelarlo.**

**Y la opción b), «electrónicos y mecánicos», describe un sistema mixto real** —una steadicam con
cabeza motorizada, un gimbal con contrapesos— **pero no es lo que la palabra «pasiva» significa**:
**pasivo es, por definición, lo que no consume energía para corregir.**

## 11. Las cámaras sin operador detrás: PTZ y Twin Cam

**Una cámara PTZ es una cámara robotizada que gira en horizontal, gira en vertical y hace zoom**, sin
nadie a su lado. **Es la cámara de los platós de informativos, de los plenos y de las salas de prensa.**

**La característica que NO es de una cámara PTZ es que sólo se puedan controlar por ordenador.** Ésa es
la respuesta oficial a la pregunta 1, **y es una pregunta negativa: se busca la falsa.**

**Las tres verdaderas, una a una:**

| Afirmación | Por qué es cierta |
|---|---|
| **Movimientos de panorámica vertical, horizontal y zoom** | **Es literalmente lo que las siglas PTZ nombran**: *pan*, *tilt*, *zoom* |
| ***Autotracking* de voz y audio** | **Los modelos de sala de reuniones y de aula lo llevan**: un conjunto de micrófonos localiza quién habla y la cámara encuadra hacia allí |
| **Se puede controlar a kilómetros de distancia** | **Se gobiernan por red IP**, y una red IP no tiene límite de distancia: es la base de la producción remota |

**Y por qué la falsa es falsa**: **una PTZ se maneja habitualmente sin ordenador ninguno.** **Se maneja
con un panel de mando físico de joystick**, que es el aparato normal en un control; **con un mando a
distancia por infrarrojos**, en las instalaciones pequeñas; **o desde un pupitre de cámaras integrado
en el control de realización.** **El ordenador es una opción más, no la única**, y **la palabra «sólo»
es lo que hace falsa la afirmación.**

**El patrón que conviene llevarse**: **en una pregunta negativa, la opción que contiene «sólo»,
«siempre» o «nunca» es la primera candidata.** **Aquí lo es, y acierta.**

**La Twin Cam** es harina de otro costal. **La respuesta oficial a la pregunta 88 es que es una cámara
doble que sincroniza la grabación en superficie y bajo el agua al mismo tiempo**, y **es un dispositivo
real de las retransmisiones de natación, saltos y waterpolo**: **un cuerpo con dos ópticas alineadas en
vertical, una por encima de la línea de flotación y otra por debajo**, que **entrega las dos señales
sincronizadas para que la realización pueda cortar entre ellas o partir la pantalla sin salto.**

**Pero la respuesta descansa en la plantilla, y hay que decirlo**: **«twin cam» no es un término
normalizado.** **En el uso general del sector, y sobre todo fuera del deporte, «twin cam» o «twin
lens» nombra el equipo de dos cámaras emparejadas para estereoscopia**, que es **exactamente lo que la
opción c) describe**. **La opción c) no es un disparate: es el otro uso del mismo nombre.** **Lo que
decide es la plantilla**, y **el temario lo declara en lugar de fingir que el término sólo significa
una cosa.**

## 12. La pregunta que depende de una planta

**Una de las quince preguntas de este tema no se puede contestar leyendo**: **la pregunta 48 pide decir
qué cámaras llevan teleobjetivo según la planta de decorado que acompaña al enunciado.** **La respuesta
oficial es a), cámaras 1, 5 y 8**, y **descansa enteramente en la plantilla.**

**El temario no describe esa planta, porque no la tiene delante.** **Lo que sí puede dar, y da, es la
regla de su familia**, que **es lo que hace legible cualquier planta de decorado:**

1. **En una planta, cada cámara se dibuja con un vértice y dos líneas que se abren**: **ése es su ángulo
   de cobertura.** **Vértice estrecho y líneas casi paralelas, teleobjetivo. Vértice abierto,
   angular.**
2. **Cuando la planta no dibuja los ángulos, la distancia decide**: **para un mismo tamaño de plano, la
   cámara más lejos del área de acción necesita más focal.** **Las cámaras del fondo de un plató o del
   final de una grada llevan tele; las de primera fila, angular.**
3. **Y el reparto típico de un plató lo confirma**: **la cámara de plano general va abierta y cerca del
   eje; las cámaras de recurso y de detalle van lejos y cerradas.**

**Con esas tres reglas se lee cualquier planta. Ninguna de las tres sustituye a verla**, y **el tema lo
dice.**

## 13. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 1 | Cuál NO es característica de una cámara PTZ | b) Sólo se pueden controlar por ordenador ✔ |
| 17 | Qué es una *mini jib* | b) Una grúa pequeña ✔ |
| 25 | Qué indica el signo Φ en el cuerpo de la cámara | a) El punto del plano focal ✔ |
| 48 | Qué cámaras llevan teleobjetivo según la planta | a) Cámaras 1, 5 y 8 ✔ **·** sólo con la plantilla |
| 52 | Qué es una CCU en televisión | a) Unidad para controlar los parámetros de cámara ✔ |
| 57 | Qué se controla con un RCP | b) Diafragma, crominancia y velocidad de obturación ✔ |
| 62 | Qué se modifica al incrementar la ganancia | d) Habrá más ruido ✔ |
| 68 | Qué es la estabilización pasiva | d) Por los medios mecánicos de un soporte ✔ |
| 73 | Qué objetivo tiene un ángulo de visión de 60º a 25º | c) Normal ✔ |
| 78 | Qué es un *slider* | a) Un rail con ruedas sobre el que se pone la cámara ✔ |
| 83 | Efecto por contaminación entre diodos vecinos en CCD | b) *Blooming* ✔ |
| 88 | Qué es una Twin Cam | b) Cámara doble, superficie y bajo el agua ✔ **·** sólo con la plantilla |
| 94 | Qué es un cangrejo | a) Soporte extensible acoplado al trípode ✔ |
| 100 | Balance de blancos repetido sobre un vaquero azul claro | c) Tono más cálido ✔ |
| 106 | Cómo distorsionar la perspectiva del fondo | a) Utilizando el dolly-zoom ✔ |

**Las quince respuestas oficiales son correctas.**

**Dos de las quince descansan sólo en la plantilla**: **la que depende de una planta de decorado y la
que depende de un término que no está normalizado.**

**Y un aviso de reparto**: **una de las quince es una pregunta negativa** —la 1— y **se contesta
buscando la falsa**; **las otras catorce, buscando la verdadera.** **Leer el «NO» del enunciado es, en
este tema, la mitad del acierto de esa pregunta.**

## 14. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son las nociones básicas de la cámara, sus objetivos,
sus soportes y sus accesorios, y **va como oficio**, salvo dos afirmaciones que descansan en la
plantilla.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Dos afirmaciones**: la lectura de una planta de decorado que el temario no puede reproducir, y un término de fabricante que no está normalizado | Preguntas 48 y 88 |

**Cuatro declaraciones expresas:**

1. **La pregunta 48 depende enteramente de una imagen.** **El temario no la describe**, y **lo que
   aporta en su lugar son las tres reglas con que se lee una planta de decorado**: el vértice del ángulo
   dibujado, la distancia al área de acción y el reparto típico de un plató. **Ninguna sustituye a la
   planta**, y **el tema lo dice.**
2. **«Twin cam» no es un término normalizado**, y **este temario lo declara en lugar de resolverlo.**
   **La respuesta oficial coincide con el uso del término en las retransmisiones acuáticas**; **la
   opción c) coincide con su uso en estereoscopia.** **La documentación de ningún fabricante se ha
   consultado**, y **la respuesta descansa en la plantilla.**
3. **Los tramos de ángulo de visión del epígrafe 6 son convención del sector, no norma.** **Los
   manuales mueven los límites algunos grados**; **lo que no mueve ninguno es el orden.** **Con la
   convención corriente —más de 60º angular, de 60º a 25º normal, de 25º a 10º tele— el resultado
   coincide con la plantilla oficial.**
4. **La palabra «perla» de la pregunta 83 no nombra ningún defecto de captación conocido**, y **el tema
   lo afirma como lo que es: una comprobación negativa.** **Se ha buscado en la terminología de sensores
   y no aparece**; **si existiera con ese sentido en algún manual no consultado, la afirmación de este
   tema habría que corregirla.** **Se declara así para que se pueda.**

**El resto del tema va como oficio y así se declara**: la cadena cabeza-CCU-panel, el reparto de mandos
entre el control de imagen y el operador, el comportamiento de la ganancia y su equivalencia en pasos de
diafragma, el mecanismo del balance de blancos y la regla del color complementario, la distinción entre
*blooming*, *smear* y *moiré*, la función de la marca del plano focal, la mecánica del dolly-zoom, el
vocabulario de soportes y la separación entre estabilización pasiva y activa. **Nada de eso está en un
boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como si lo
estuviera.
