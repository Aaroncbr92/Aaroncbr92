# Tema 9 del específico de Edición, Montaje y Procesos Audiovisuales · Incrustaciones, grafismo y postproducción

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Edición, Montaje y Procesos Audiovisuales · punto 9 |
| **Sirve para** | **Edición, Montaje y Procesos Audiovisuales** |
| **Fuente** | **Sin norma: no la hay.** Su materia son la incrustación, el canal alfa, el grafismo y la composición, y **va como oficio**, salvo seis rótulos de programa que descansan en la plantilla |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **Seis preguntas** dependen del rótulo exacto de una función de un programa comercial cuya documentación no se ha consultado. **Las otras dos** —las tres señales de una incrustación y la función de una máscara de capa— **son teoría de la imagen** |
| **Extensión** | **3.020 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el canal de transparencia, llamado **canal alfa**;
el fondo de color para incrustación (***chroma key***, o **croma** a secas); la señal de recorte
(***key***) y la de relleno (***fill***); los tres primarios (**RGB**); los fotogramas clave
(***keyframes***); los gráficos de red portátiles (**PNG**) y el formato gráfico de intercambio
(**GIF**); la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**); y los complementos de
un programa (***plugins***).

**Y una advertencia sobre los nombres de las órdenes.** Este tema reproduce los rótulos de dos
programas de la casa Adobe —After Effects y Photoshop—, que es de lo que el examen pregunta, y **los
escribe como aparecen en el programa** porque **la respuesta oficial depende del nombre exacto**.

> Enunciado de la convocatoria (Anexo 2, temario específico de Edición, Montaje y Procesos
> Audiovisuales, puntos 5.5 y 5.6):
> «Incrustaciones canal alpha, chromakey, e integración con aplicaciones de diseño gráfico.»
> «Colorización.»

**Ocho preguntas**, y **seis de las ocho son de un programa concreto**. **Dos se contestan con teoría
de la imagen** —la de las señales de una incrustación y la de la máscara de capa— y **seis con el
manual de After Effects**, que **no se ha consultado**: descansan en la plantilla.

<!-- indice -->

## Índice

- [1. Qué es una incrustación](#1-qué-es-una-incrustación)
- [2. Las tres señales de un efecto de incrustación](#2-las-tres-señales-de-un-efecto-de-incrustación)
- [3. El canal alfa y la máscara](#3-el-canal-alfa-y-la-máscara)
- [4. La máscara de capa en un editor de imagen](#4-la-máscara-de-capa-en-un-editor-de-imagen)
- [5. Las capas de un programa de composición](#5-las-capas-de-un-programa-de-composición)
- [6. La precomposición](#6-la-precomposición)
- [7. El recorte de trazado](#7-el-recorte-de-trazado)
- [8. El degradado y sus formas](#8-el-degradado-y-sus-formas)
- [9. Los fotogramas clave y su asistente](#9-los-fotogramas-clave-y-su-asistente)
- [10. Los complementos](#10-los-complementos)
- [11. Los datos que el examen ha preguntado](#11-los-datos-que-el-examen-ha-preguntado)
- [12. Trazabilidad](#12-trazabilidad)

<!-- /indice -->

## 1. Qué es una incrustación

**Incrustar es sustituir una parte de una imagen por otra.** Es lo que pone un mapa del tiempo detrás
de un presentador, un rótulo sobre un plano o un fondo virtual detrás de un actor.

**Las dos familias de incrustación**, según de dónde salga el recorte:

| Familia | De dónde sale el recorte |
|---|---|
| ***Chroma key*** | **Del color**: se elige un color del fondo —verde o azul— y todo lo que lo tenga se vuelve transparente |
| ***Luma key*** | **Del brillo**: se recorta por encima o por debajo de un nivel de luminancia |
| **Canal alfa** | **De un cuarto canal** que viene con la imagen y dice, píxel a píxel, cuánto de opaco es |
| **Máscara** o *roto* | **De una forma dibujada a mano**, fija o animada |

**Por qué el fondo es verde o azul**: **son los colores más alejados del tono de la piel humana**, así
que **el recorte se puede hacer sin comerse la cara del presentador**. El verde se ha impuesto porque
**los sensores digitales tienen el doble de fotositos verdes** y por tanto **entregan ese canal con
menos ruido**.

## 2. Las tres señales de un efecto de incrustación

**En una composición creada por efecto de incrustación intervienen tres señales.** Ésa es la respuesta
oficial a la pregunta 62.

| Señal | Qué es |
|---|---|
| **Fondo** (*background*) | **La imagen que queda debajo**: lo que se ve por el agujero |
| **Relleno** (*fill*) | **La imagen que se pone encima**: lo que se ve dentro de la forma |
| **Recorte** (*key*) | **La señal que define la forma del agujero**: dónde se ve una y dónde la otra |

**Por qué son tres y no dos**, que es todo el fondo de la pregunta: **con dos imágenes no hay
composición posible**, porque **falta decir dónde acaba una y empieza la otra**. **El recorte es una
señal por derecho propio**, y en un mezclador de vídeo **viaja por una entrada distinta de la del
relleno**: por eso los mezcladores tienen entradas rotuladas *key* y *fill* por separado.

**Y por qué no son cuatro**: **el canal alfa no es una cuarta señal**, es **la forma de llevar el
recorte pegado al relleno** cuando los dos vienen del mismo fichero. **Cuando hay alfa hay tres
señales igual**: fondo, relleno y recorte, sólo que dos de ellas comparten fichero.

**Las tres opciones falsas** —una, dos y cuatro— **se descartan con el mismo razonamiento**: **una no
compone nada**, **dos no dicen dónde**, y **cuatro sobra**.

## 3. El canal alfa y la máscara

**El canal alfa es el cuarto canal de una imagen, y dice cuánto de opaco es cada píxel.** Los tres
primeros son rojo, verde y azul; **el cuarto no lleva color: lleva transparencia**.

| Valor del alfa | Qué significa |
|---|---|
| **0** | **Píxel totalmente transparente**: se ve el fondo |
| **Valores intermedios** | **Píxel semitransparente**: se mezclan fondo y relleno |
| **Máximo** | **Píxel totalmente opaco**: se ve el relleno |

**Los valores intermedios son la razón de ser del alfa.** Sin ellos, **los bordes de un recorte serían
escalones**; con ellos, **un borde puede estar medio dentro y medio fuera**, que es como se ve un
recorte bueno. **Ésa es la diferencia entre el canal alfa de ocho bits del formato PNG y la
transparencia binaria del GIF**, que se ve en el tema 5.

**Y de aquí sale la notación 4:4:4:4** del tema 4: **la cuarta cifra es el alfa**.

## 4. La máscara de capa en un editor de imagen

**La función principal de una máscara de capa es ocultar o mostrar partes específicas de una capa sin
eliminar permanentemente el contenido.** Ésa es la respuesta oficial a la pregunta 31.

**Las tres palabras que llevan el peso de la definición**: **ocultar**, **mostrar** y **sin eliminar
permanentemente**. **Una máscara no borra: tapa.** Y por eso **se puede rehacer en cualquier momento**,
lo que la convierte en la herramienta no destructiva por excelencia de un editor de imagen.

**Cómo funciona**: **la máscara es una imagen en escala de grises pegada a la capa**. **Donde la
máscara es blanca, la capa se ve; donde es negra, no; donde es gris, se ve a medias.** **Es
exactamente un canal alfa dibujado a mano**, y por eso este epígrafe va detrás del anterior.

**Las tres opciones falsas de la pregunta 31 son funciones reales del programa que hacen otra cosa**:
aplicar efectos de color, cambiar el tamaño sin distorsionar y ajustar brillo y contraste. **Ninguna
de las tres oculta ni muestra**, que es lo que el enunciado pregunta.

**El aviso de oficio**: **la máscara de capa es la razón por la que un fichero de grafismo se puede
retocar meses después.** Quien recorte borrando píxeles **entrega un trabajo que no se puede
corregir**, y en una casa de televisión los rótulos se corrigen siempre.

## 5. Las capas de un programa de composición

**Un programa de composición trabaja apilando capas**, y cada tipo de capa hace una cosa distinta.

**Algunos tipos de capa son: capa de forma, capa de ajuste, capa de texto y objeto nulo.** Ésa es la
respuesta oficial a la pregunta 78.

| Tipo | Qué es |
|---|---|
| **Capa de texto** | **Texto vectorial editable**, con sus propias animaciones |
| **Capa de forma** | **Formas vectoriales** creadas en el propio programa |
| **Sólido** | **Un rectángulo de color plano**, que sirve de base para efectos |
| **Capa de ajuste** | **Una capa sin contenido que aplica sus efectos a todo lo que tiene debajo** |
| **Objeto nulo** | **Una capa invisible que sirve de padre**: mueve a las que se le enlazan sin verse |
| **Capa de cámara** y **de luz** | Para composición en tres dimensiones |

**Las tres opciones falsas mezclan tipos reales con inventados**: **«capa de relleno manual»** y
**«capa inversa»** **no existen** en el programa, y **«capa de fusión»** **confunde una capa con un
modo de fusión**, que es un ajuste de cada capa y no un tipo de capa.

**La regla que resuelve la pregunta**: **de las cuatro listas, sólo una tiene los cuatro elementos
reales**. **Basta con reconocer «capa de relleno manual» y «capa inversa» como inventos** para
descartar tres de las cuatro.

**Las dos capas que más rentan de entender**, porque explican cómo se trabaja: **la capa de ajuste**,
que **aplica un efecto a todo lo que hay debajo sin tocar cada capa**, y **el objeto nulo**, que
**anima a varias capas a la vez enlazándolas a algo que no se ve**.

## 6. La precomposición

**Para anidar dos capas concretas con el objetivo de que trabajen como una sola hay que seleccionar
las dos capas y elegir «precomponer» con el botón derecho del ratón.** Ésa es la respuesta oficial a
la pregunta 35.

**Qué hace precomponer**: **coge las capas seleccionadas y las mete dentro de una composición nueva**,
que **pasa a ocupar en la composición original el sitio de todas ellas**. **A partir de ahí, la
composición anidada se comporta como una capa**: se le aplican efectos, se transforma y se anima **de
una vez**.

**Para qué sirve en el trabajo**: **para aplicar un efecto al conjunto y no a cada pieza**, y **para
ordenar** una composición que ha crecido. **Es el equivalente de agrupar en un programa de dibujo**,
con la diferencia de que **la precomposición se puede abrir y editar por dentro**.

**Las tres opciones falsas de la pregunta 35 y su error:**

| Opción | Por qué no |
|---|---|
| «El programa no permite esa opción» | **Sí la permite**: es una de sus funciones centrales |
| «Con el atajo Ctrl + D» | **Ese atajo duplica**, no anida |
| «Precomponer una capa y luego la otra» | **Daría dos composiciones anidadas separadas**, no una sola que las contenga a las dos. **El enunciado pide que trabajen como una sola** |

**La opción d) es la trampa buena**, porque **describe una operación que sí se puede hacer** y que
**no consigue lo que se pide**. **La palabra que la descarta es «una sola».**

## 7. El recorte de trazado

**El recorte de trazado se aplica en textos, líneas y rellenos.** Ésa es la respuesta oficial a la
pregunta 30.

**Qué es**: **una propiedad que dibuja progresivamente el trazado de un elemento vectorial**, de
manera que se puede **animar la aparición de una línea, de un contorno o de un texto como si se
estuviera escribiendo**.

**Por qué se aplica ahí y no en otro sitio, que es lo que hace la respuesta razonable**: **el recorte
de trazado necesita un trazado**. **Sólo tienen trazado los elementos vectoriales del programa** —los
caracteres de un texto, las líneas y contornos de una forma, y sus rellenos—. **Una imagen de mapa de
bits no tiene trazado**, así que **no se le puede aplicar**.

**Las tres opciones falsas y su error:**

| Opción | Por qué no |
|---|---|
| «Se aplica en la capa de ajuste» | **La capa de ajuste no tiene trazado**: sólo lleva efectos |
| «Se utiliza para modificar las formas poligonales» | **Confunde recortar el trazado con editar la forma.** El recorte **no cambia la forma: la revela poco a poco** |
| «Se aplica en la rotoscopia» | **La rotoscopia usa máscaras animadas**, que es otra cosa |

## 8. El degradado y sus formas

**El efecto de degradado ofrece dos opciones respecto de la forma de la pendiente: pendiente lineal y
pendiente radial.** Ésa es la respuesta oficial a la pregunta 75.

| Forma | Cómo va el degradado |
|---|---|
| **Lineal** | **De un punto a otro en línea recta**: bandas paralelas |
| **Radial** | **Desde un centro hacia fuera**, en círculos concéntricos |

**Las tres opciones falsas mezclan la buena con formas de degradado que existen en otros programas
pero no son las dos de éste**: **«de ángulo»** —el que barre girando— y **«de reflejado»** —el que se
espeja a los dos lados— **son formas reales de degradado de un editor de imagen**, y **el efecto de
este programa ofrece sólo dos**.

**El aviso de estudio**: **las cuatro opciones son parejas y tres de las cuatro contienen «lineal» o
«radial»**. **Lo que hay que saber es que las dos son ésas y sólo ésas**, no cuál de las cuatro suena
mejor.

## 9. Los fotogramas clave y su asistente

**Un fotograma clave marca el valor de un parámetro en un instante**, y **el programa calcula los
valores intermedios**. Cómo los calcula es la interpolación, y **el asistente de fotogramas clave es
el menú que aplica las interpolaciones más usadas de una vez**.

**Dentro del asistente de fotogramas clave, la interpolación que da como resultado los keyframes de la
imagen se denomina «desaceleración / aceleración suave».** Ésa es la respuesta oficial a la pregunta
95.

**Qué hace**: **suaviza la entrada y la salida de la clave**, de modo que **el valor no arranca ni se
detiene de golpe**. Es lo que convierte **un movimiento mecánico en uno que parece natural**, y es la
primera cosa que se aplica a cualquier animación hecha a mano.

**La familia entera, para situarla:**

| Opción del asistente | Qué hace |
|---|---|
| **Suavizado de entrada** | **Sólo frena a la llegada** |
| **Suavizado de salida** | **Sólo arranca despacio** |
| **Suavizado de entrada y salida** | **Las dos cosas**: es la respuesta |
| **Lineal** | **Sin suavizado**: velocidad constante entre claves |

**Las tres opciones falsas**: **«desaceleración suave»** es **sólo la mitad** —frena pero no arranca
suave—; **«lineal»** es **la interpolación sin suavizar**, que es lo contrario; y **«escala
exponencial»** **es otra orden del asistente**, que reparte una escala de forma exponencial y **no es
una interpolación de suavizado**.

**La regla que resuelve la pregunta**: **la respuesta buena nombra las dos mitades**, y **la mala
nombra una**. Es el mismo mecanismo de la pregunta 20 del tema 5, donde la respuesta buena era la que
recogía las dos configuraciones y no una.

## 10. Los complementos

**Un complemento es un programa añadido que amplía lo que la aplicación hace de fábrica.** En
composición son la mitad del oficio: seguimiento de movimiento, destellos, desenfoques, recorte
asistido.

**Son complementos utilizados en After Effects: Mocha, Saber y Boris Sapphire.** Ésa es la respuesta
oficial a la pregunta 73.

| Complemento | Para qué |
|---|---|
| **Mocha** | **Seguimiento planar de movimiento** y máscaras asistidas |
| **Saber** | **Efectos de luz y energía** |
| **Boris Sapphire** | **Un paquete grande de efectos** de imagen |

**Las tres opciones falsas mezclan nombres de tres mundos distintos**, y ése es todo el mecanismo:

| Opción | Qué mezcla |
|---|---|
| «CycoreFX, Magic Bullet Looks, Color Finale» | **Los dos primeros son de composición y color**, pero **el tercero es un complemento de etalonaje de otro programa de montaje** |
| «Red Giants, Valhalla Super Massive, Cinta Softube» | **El segundo y el tercero son complementos de AUDIO**: reverberación y saturación |
| «Shutterstock, CamelCrusher, Plasma Wipe» | **El primero es un banco de imágenes**, **el segundo un complemento de audio** y **el tercero una transición** |

**La forma de contestarla sin conocer los productos**: **buscar la lista en la que los tres nombres
pertenecen al mismo mundo**. **Tres de las cuatro mezclan audio, bancos de imágenes o programas
distintos**, y **sólo una es homogénea**.

## 11. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 30 | Dónde se aplica el recorte de trazado | d) En textos, líneas y rellenos ✔ **·** sólo con la plantilla |
| 31 | Función principal de una máscara de capa | b) Ocultar o mostrar sin eliminar el contenido ✔ |
| 35 | Cómo anidar dos capas para que trabajen como una | b) Seleccionarlas y elegir «precomponer» ✔ **·** sólo con la plantilla |
| 62 | Cuántas señales intervienen en una composición por incrustación | c) Tres ✔ |
| 73 | Cuáles son complementos de After Effects | a) Mocha, Saber, Boris Sapphire ✔ **·** sólo con la plantilla |
| 75 | Las dos formas de pendiente del efecto de degradado | a) Lineal y radial ✔ **·** sólo con la plantilla |
| 78 | Algunos tipos de capa | d) Forma, ajuste, texto y objeto nulo ✔ **·** sólo con la plantilla |
| 95 | Nombre de la interpolación del asistente de fotogramas clave | b) Desaceleración / aceleración suave ✔ **·** sólo con la plantilla |

**Las ocho respuestas oficiales son correctas**, y **seis de las ocho descansan sólo en la plantilla**:
las seis que dependen del rótulo exacto de una función de un programa comercial.

**Las dos que no**: **la de las tres señales de una incrustación**, que es teoría de composición de
imagen, y **la de la máscara de capa**, cuya definición es la estándar de cualquier editor de imagen.

**El aviso de estudio**: **cuatro de las seis de programa se contestan por coherencia interna de las
opciones** —los tipos de capa inventados, la lista de complementos que mezcla audio con vídeo, la
opción que hace dos composiciones en lugar de una y la interpolación que nombra media función—. **Sólo
dos son memoria pura**: dónde se aplica el recorte de trazado y cuáles son las dos formas de
pendiente.

## 12. Trazabilidad

**Este tema no cita ninguna norma.** Su materia son la incrustación, el grafismo y la composición, y
**va como oficio y como plantilla**.

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Quinto: la plantilla oficial** | **Seis afirmaciones**, todas ellas rótulos o listas de funciones de un programa comercial | 30, 35, 73, 75, 78, 95 |

**Una declaración expresa**: **la documentación de Adobe sobre After Effects y Photoshop no se ha
consultado.** Es documentación de producto de una casa comercial, y este proyecto no ha accedido a
ella. **Las seis respuestas señaladas descansan en la plantilla oficial**, que es el quinto nivel de
la jerarquía de fuentes.

**Lo que va como oficio y así se declara**: la clasificación de las incrustaciones por el origen del
recorte; el reparto en fondo, relleno y recorte y por qué son tres señales y no dos ni cuatro; el
funcionamiento del canal alfa y su relación con la máscara; la lógica de la precomposición; y el
porqué de que el recorte de trazado sólo se aplique a elementos vectoriales. **Nada de eso está en un
boletín oficial ni en una norma técnica**, y el tema no lo presenta como si lo estuviera.
