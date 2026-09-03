# Tema 10 del específico de Diseño Gráfico · Equipos y programas de diseño

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Diseño Gráfico · punto 10 |
| **Sirve para** | **Diseño Gráfico** |
| **Fuente** | **Sin norma: no la hay.** Su materia son los equipos y los programas de diseño, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Banco más grande** | **Veinte preguntas: casi una de cada cuatro del examen específico.** Nueve son de un solo programa |
| **Sólo con la plantilla** | **Una pregunta depende de una figura**: la operación de buscatrazos de la 71. **El temario no la describe**: da la tabla de las cinco operaciones y cómo se decide mirando |
| **Extensión** | **3.764 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: los formatos de fichero de imagen, que se nombran
por su extensión (**PSD**, **TIFF**, **PNG**, **JPG**, **TGA**, **GIF**, **SVG**, **EPS**, **AI**);
el modelo de color de cian, magenta, amarillo y negro (**CMYK**) y el de rojo, verde y azul
(**RGB**); el códec de vídeo avanzado (**H.264**) y el de alta eficiencia (**H.265**); la ultraalta
definición (**UHD**); la unidad de proceso gráfico (**GPU**); los gigabytes (**GB**); y los nombres
de programa y de función, que van en acentos graves o en cursiva cuando el examen los escribe en
inglés.

> Enunciado de la convocatoria (Anexo 2, temario específico de Diseño Gráfico, punto 10):
> «Hardware y software. Software de dibujo vectorial/software de maquetación/software de dibujo
> bitmap/software de diseño y animación 3D. Edición lineal y no lineal. Equipos de render en tiempo
> real. Software de titulación. Tipos de archivos y formatos de datos: imagen, audio y vídeo. Adobe
> Creative Cloud (Illustrator/Photoshop/After Effets). Lenguajes de programación (Python,
> JavaScript). Software de creación de gráficos en tiempo real (Vizrt, Chyron, Brainstorm). Software
> de gráficos 3D (C4d, Blender). Motores gráficos (Unreal, Unity): qué son y para qué se utilizan.»

**Veinte preguntas: casi una de cada cuatro del examen específico**, y **el banco más grande de la
ocupación con diferencia.**

**Su reparto**: **nueve son de un programa de composición y animación**, **cinco de programas de
imagen fija**, **cuatro de formatos de fichero** y **dos de motores y programas de tiempo real.**

**El aviso que ordena el estudio del punto entero**: **este examen no pregunta teoría de informática;
pregunta dónde está cada cosa en el programa.** **Quien haya trabajado con estas herramientas contesta
casi todas; quien las haya leído, casi ninguna.**

<!-- indice -->

## Índice

- [1. Las tres familias de programa, y por qué importa la diferencia](#1-las-tres-familias-de-programa-y-por-qué-importa-la-diferencia)
- [2. El programa de imagen fija](#2-el-programa-de-imagen-fija)
- [3. El programa vectorial](#3-el-programa-vectorial)
- [4. El programa de composición y animación](#4-el-programa-de-composición-y-animación)
- [5. Los formatos de fichero](#5-los-formatos-de-fichero)
- [6. El tiempo real y los motores gráficos](#6-el-tiempo-real-y-los-motores-gráficos)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Las tres familias de programa, y por qué importa la diferencia

**El enunciado las nombra por separado y el examen las mezcla**, así que conviene tener el cuadro:

| Familia | Con qué trabaja | Qué pasa al ampliar | Programas del enunciado |
|---|---|---|---|
| **Mapa de bits** | **Una rejilla de píxeles** | **Pierde calidad**: hay que inventar píxeles | **Photoshop** |
| **Vectorial** | **Descripciones matemáticas de curvas** | **No pierde nada**: se recalcula | **Illustrator** |
| **Maquetación** | **Páginas con texto e imágenes colocadas** | **Según lo que coloque dentro** | **InDesign** |
| **Composición y animación** | **Capas en una línea de tiempo** | **Según la capa** | **After Effects** |
| **Tres dimensiones** | **Geometría, materiales y luces** | **No pierde: se vuelve a calcular** | **Blender**, **Cinema 4D** |

**La pregunta 78 mide exactamente esa primera fila**: **en un programa de imagen se puede duplicar el
tamaño sin pérdida de calidad SÓLO si la imagen es vectorial.** Ésa es la respuesta oficial.

---

**Y el matiz que la hace defendible**: **el programa citado es de mapa de bits y, aun así, admite
objetos vectoriales dentro** —formas, texto, objetos inteligentes—. **Lo que la pregunta afirma es lo
correcto: lo que no pierde al ampliarse es lo vectorial**, esté donde esté.

**La opción falsa que más engaña es «sí, en todos los casos»**, porque **en la práctica una ampliación
al doble con buen remuestreo casi no se nota.** **«Casi no se nota» no es «sin pérdida alguna»**, y
la pregunta usa esas palabras.

**La pregunta 50**: **el programa que se utiliza para crear gráficos en tres dimensiones de manera
profesional es Blender.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son cada una de otra familia**: **uno es de maquetación, otro de imagen
fija y otro de audio.** **La pregunta se contesta sabiendo a qué familia pertenece cada nombre**, que
es justo el cuadro de arriba.

## 2. El programa de imagen fija

**Cinco preguntas salen de aquí**, y **todas son de dónde está la función:**

**La pregunta 3**: **un trazado (*path*) permite contornear con precisión un objeto irregular.** Ésa es
la respuesta oficial.

---

**Qué es un trazado, en una línea**: **una curva vectorial dibujada dentro de un documento de mapa de
bits.** **No pinta píxeles**: **describe un contorno**, y de ahí que sirva para recortar con precisión
lo que una selección a mano no consigue.

**Las tres opciones falsas describen otras tres funciones reales**: **memorizar acciones es una
acción grabada; enlazar capas es vincularlas; y pintar sobre varias a la vez no existe.**

**La pregunta 28**: **para conservar capas, efectos y máscaras en un archivo de menos de dos gigabytes
hay que guardar en formato `PSD`.** Ésa es la respuesta oficial.

---

**Y ahí está el matiz que el propio enunciado introduce con la cifra**: **el formato nativo tiene un
límite de dos gigabytes por fichero.** **Por encima de ese tamaño hay que usar el formato grande**,
que es el mismo formato con otra extensión. **Por eso el enunciado dice «de menos de 2GB»**: sin esa
condición, la respuesta sería discutible.

**Las tres opciones falsas y qué conservan de verdad:**

| Formato | ¿Conserva capas? |
|---|---|
| **`PSD`** | **Sí: capas, efectos, máscaras, canales y trazados** ✔ |
| **`TIFF`** | **Puede llevar capas**, pero no es su cometido y no todos los programas las leen |
| **`TGA`** | **No.** Es una imagen plana con canal alfa |
| **`PNG`** | **No.** Imagen plana con transparencia |

**La pregunta 82**: **el número máximo de canales que puede tener una imagen es 56.** Ésa es la
respuesta oficial.

---

**Es memoria pura y conviene decirlo**: **no hay nada que razonar.** **El apoyo es que 56 es la única
de las cuatro cifras que no es redonda**, y **las cifras redondas suelen ser las inventadas.**

**Qué es un canal, para que la cifra signifique algo**: **cada una de las capas de información de
color o de selección de la imagen.** **Una imagen en rojo, verde y azul tiene tres canales de color
más el compuesto**; **cada máscara guardada añade un canal alfa.**

**La pregunta 64**: **el formato de imagen que NO admite el modo de color CMYK es `PNG`.** Ésa es la
respuesta oficial.

---

**Y la razón está en para qué nació cada formato:**

| Formato | Para qué nació | ¿Admite CMYK? |
|---|---|---|
| **`PSD`** | **Trabajo en el propio programa** | **Sí** |
| **`JPG`** | **Fotografía, también para imprenta** | **Sí** |
| **`TIFF`** | **Artes gráficas** | **Sí** |
| **`PNG`** | **La web**, donde todo es rojo, verde y azul | **No** ✔ |

**La regla que lo fija**: **cian, magenta, amarillo y negro es el modelo de la tinta**; **rojo, verde
y azul, el de la pantalla.** **Un formato pensado para la web no necesita el de la tinta**, y por eso
no lo lleva.

## 3. El programa vectorial

**La pregunta 48**: **la función que convierte imágenes en formatos como `JPEG`, `PNG` o `PSD` en
ilustraciones vectoriales es el calco de imagen (*image trace*).** Ésa es la respuesta oficial.

---

**Las tres opciones falsas son tres funciones reales del mismo programa**, y **conviene saber qué hace
cada una porque la pregunta 71 usa una de ellas:**

| Función | Qué hace |
|---|---|
| **Calco de imagen** | **Convierte un mapa de bits en vectores** ✔ |
| **Buscatrazos** (*pathfinder*) | **Combina formas**: unir, restar, intersecar, excluir, dividir |
| **Fusión** (*blend*) | **Genera pasos intermedios entre dos objetos** |
| **Ajustar segmentos** | **Modifica un tramo de una curva ya dibujada** |

**La pregunta 71 depende de una figura**: **enseña un resultado y pide con qué operación de
buscatrazos se consigue.** **La respuesta oficial es restar (*substract*).** **Este temario no ha
visto la figura y no la describe.**

---

**Lo que sí aporta es la regla de la familia**, que **reduce las cuatro opciones a dos en cuanto se
mira el dibujo:**

| Operación | Qué queda |
|---|---|
| **Unir** | **Una sola forma con el contorno exterior de todas** |
| **Restar** | **La forma de abajo menos lo que la de arriba tapaba** ✔ |
| **Intersecar** | **Sólo la zona común a las dos** |
| **Excluir** | **Todo menos la zona común**: el solape queda hueco |
| **Dividir** | **Tantas formas como trozos creen los cortes** |

**Cómo se decide mirando**: **si desapareció un trozo de la forma de abajo y la de arriba también,
es restar**; **si lo que desapareció es justo el solape, es excluir**; **si lo que queda es sólo el
solape, es intersecar.**

**La pregunta 69**: **las características de las curvas Bézier son nodo inicial, nodo final, punto de
control y palanca de curva.** Ésa es la respuesta oficial.

---

**Y es una pregunta de enumerar completa**: **las cuatro opciones son la misma lista a la que le
falta un elemento**, salvo la correcta. **La regla es que una curva Bézier necesita los dos extremos
Y los controles que la doblan**, y **una lista sin nodo inicial y final está incompleta.**

## 4. El programa de composición y animación

**Nueve preguntas del punto son de este programa**, y **es el que más rinde estudiar de toda la
ocupación.**

**La pregunta 6**: **el área de trabajo (*work area*) es la sección de la línea de tiempo para
previsualizar o renderizar.** Ésa es la respuesta oficial.

---

**El distractor bueno es «el espacio de trabajo principal»**, porque **en castellano las dos cosas se
llaman igual.** **La distinción es que el área de trabajo es un TRAMO DE TIEMPO**, marcado con dos
asas sobre la línea, **y el espacio de trabajo es la disposición de los paneles en pantalla.**

**La pregunta 10**: **para que dos capas trabajen como una sola se seleccionan las dos y se elige
«precomponer».** Ésa es la respuesta oficial.

---

**Qué hace precomponer, en una línea**: **mete las capas elegidas en una composición nueva y deja en
su lugar una sola capa que la contiene.** **Es la manera de aplicar un efecto al conjunto y no a cada
una por separado.**

**La opción falsa que hay que saber descartar es el atajo de duplicar**, que **hace lo contrario:
crea una copia de cada capa.**

**La pregunta 18**: **en una composición en la que sólo existen capas de dos dimensiones, la que está
en primer término es la de numeración más baja.** Ésa es la respuesta oficial.

---

**Y es la regla que gobierna el orden de apilamiento**: **la lista de capas se lee de arriba abajo, la
número 1 arriba, y lo de arriba tapa a lo de abajo.**

**La condición «sólo capas 2D» del enunciado no es adorno**: **en cuanto hay capas de tres
dimensiones, el orden lo decide la posición en el eje de profundidad y no el número.** **Ésa es
exactamente la trampa que la pregunta evita al acotarlo.**

**La pregunta 26**: **las luces virtuales afectan a las capas en tres dimensiones.** Ésa es la
respuesta oficial.

---

**La regla es la misma que la anterior vista al revés**: **una luz es un objeto del espacio, y una
capa plana no está en el espacio.** **Sólo lo que tiene profundidad puede recibir una luz.**

**La consecuencia práctica que conviene llevar**: **si se añade una luz y no pasa nada, lo que falta
es activar la tercera dimensión en las capas.**

**La pregunta 75**: **el parámetro de una máscara que permite animar el desenfoque de sus bordes es el
calado de máscara (*mask feather*).** Ésa es la respuesta oficial.

**Los cuatro parámetros de una máscara, que es la lista de la que salen las opciones:**

| Parámetro | Qué controla |
|---|---|
| **Trazado** | **La forma de la máscara** |
| **Calado** | **Cuánto se difuminan sus bordes** ✔ |
| **Opacidad** | **Cuánto tapa** |
| **Expansión** | **Cuánto crece o encoge la forma** |

**El buen distractor es la expansión**, porque **también modifica el borde**: **pero lo mueve, no lo
difumina.**

**La pregunta 88**: **el proceso de creación de fotogramas intermedios entre dos fotogramas clave se
denomina interpolación.** Ésa es la respuesta oficial.

---

**Y las tres opciones falsas son palabras parecidas de otras materias**: **el interlineado es de
tipografía y aparece en el tema 5**; **las otras dos no existen como término.**

**Los dos tipos de interpolación que conviene distinguir**, porque son la mitad de la animación:

| Tipo | Qué interpola | Se ve en |
|---|---|---|
| **Espacial** | **Por dónde pasa el objeto** | **La trayectoria en el lienzo** |
| **Temporal** | **A qué velocidad recorre esa trayectoria** | **El editor de gráficos** |

**La pregunta 93**: **el efecto *wiggle* es un efecto para crear un movimiento aleatorio.** Ésa es la
respuesta oficial.

---

**Y es, en rigor, una expresión y no un efecto**: **se escribe sobre una propiedad y le añade una
oscilación al azar**, con dos números: **cuántas veces por segundo y cuánto.** **La respuesta oficial
lo llama efecto y describe bien lo que hace.**

**La pregunta 56**: **el comando «recopilar archivos» busca los archivos usados y crea una copia en
una carpeta nueva junto con el proyecto.** Ésa es la respuesta oficial.

---

**La palabra que decide es COPIA**, y **la opción falsa dice «los mueve»**: **si los moviera,
cualquier otro proyecto que usara esos mismos archivos se rompería.** **Un programa serio no mueve lo
que no es suyo.**

**Para qué sirve, que es lo que hay que entender**: **para llevarse un proyecto a otro equipo con todo
lo que necesita.** **Es el paso previo a mandar un trabajo fuera**, y **la causa número uno de que un
proyecto llegue con enlaces rotos es no haberlo hecho.**

**La pregunta 83**: **sí se pueden crear composiciones de formato vertical, hasta un máximo de 30.000
píxeles de alto.** Ésa es la respuesta oficial.

---

**Es memoria de una cifra**, y **el apoyo está en que el límite es el mismo en las dos dimensiones**:
**30.000 píxeles de ancho y 30.000 de alto.** **Las tres opciones falsas inventan una anchura mínima
que no existe.**

**Y el dato de oficio que explica por qué esta pregunta está en el examen**: **el vídeo vertical es
hoy formato de trabajo corriente** en las piezas para redes, y **un grafista de televisión las hace
a diario.**

**La pregunta 63**: **un fotograma renderizado en formato `TGA` sin compresión ocupa el mismo espacio
en bytes en todos los casos.** Ésa es la respuesta oficial.

---

**Y la razón es la definición misma de «sin compresión»**: **el tamaño es el número de píxeles por los
bytes de cada píxel, y nada más.** **Ni el entrelazado ni cuál sea el primer campo cambian cuántos
píxeles hay.**

**Las tres opciones falsas son la misma idea equivocada tres veces**: **creer que la organización de
los datos cambia su volumen.** **Eso sólo ocurre cuando hay compresión**, y el enunciado la excluye.

**La pregunta 81**: **un archivo con códec `H.265` es un archivo con un estándar de compresión que
admite vídeo `UHD` de 8K a velocidades de bits bajas y puede ahorrar hasta un 50 % de la tasa de bits
de `H.264`.** Ésa es la respuesta oficial.

---

**Las tres opciones falsas afirman cada una lo contrario de lo cierto**: **que no admite alto rango
dinámico, que tiene peor calidad y que sigue peor el movimiento.** **La generación nueva mejora en
todo eso: es más eficiente, no peor.**

**El precio que las opciones no dicen y conviene saber**: **la eficiencia se paga en cálculo.**
**Codificar y descodificar cuesta más**, y por eso **el formato viejo sigue siendo el compatible con
todo**, que es el mismo razonamiento del tema 12 de Técnica Informática.

## 5. Los formatos de fichero

**El cuadro completo, que reúne lo preguntado en este punto y en el 11:**

| Formato | Familia | Transparencia | Para qué se usa |
|---|---|---|---|
| **`PSD`** | **Mapa de bits, nativo** | **Sí**, con capas | **Trabajo en curso** |
| **`AI`** | **Vectorial, nativo** | **Sí** | **Trabajo en curso** |
| **`TIFF`** | **Mapa de bits** | **Sí** | **Artes gráficas, archivo** |
| **`PNG`** | **Mapa de bits** | **Sí**, canal alfa | **Web y grafismo sobre fondo** |
| **`JPG`** | **Mapa de bits, con pérdida** | **No** | **Fotografía** |
| **`TGA`** | **Mapa de bits** | **Sí**, canal alfa | **Secuencias de fotogramas** |
| **`GIF`** | **Mapa de bits, 256 colores** | **Sí**, de un solo valor | **Animaciones cortas** |
| **`SVG`** | **Vectorial** | **Sí** | **Web** |
| **`EPS`** | **Vectorial** | **Según el caso** | **Intercambio con imprenta** |

**La regla que este cuadro deja para el examen**: **si la pregunta habla de transparencia y web, es
`PNG`; si habla de capas, es el nativo; si habla de secuencias de fotogramas renderizados, es `TGA`;
si habla de fotografía comprimida, es `JPG`.**

## 6. El tiempo real y los motores gráficos

**La pregunta 42**: **cuando se habla de *blueprints* se está hablando de Unreal.** Ésa es la
respuesta oficial.

---

**Qué son, en una línea**: **el sistema de programación visual de ese motor**, en el que **se
programa uniendo nodos con cables en vez de escribiendo código.**

**Y las cuatro opciones son cuatro programas de tiempo real reales**, lo que hace la pregunta
exigente:

| Programa | Qué es |
|---|---|
| **Unreal** | **Motor gráfico de videojuego**, hoy muy usado en televisión ✔ |
| **Unity** | **El otro motor grande**, con programación escrita |
| **Vizrt** | **Sistema de grafismo de televisión** |
| **Chyron** | **Sistema de grafismo y titulación de televisión** |

**Por qué un motor de videojuego está en el temario de un grafista de televisión**: **porque la
escenografía virtual y la realidad aumentada de los platós se calculan hoy con ellos.** **Lo que antes
se renderizaba durante horas se calcula ahora en el mismo instante en que la cámara se mueve**, y esa
es toda la diferencia entre el grafismo grabado y el grafismo en directo.

**Los dos modos de trabajo que conviene distinguir, porque el enunciado los nombra:**

| Modo | Cuándo se calcula la imagen | Ejemplos |
|---|---|---|
| **Renderizado diferido** | **Antes de emitir**, todo el tiempo que haga falta | **Blender**, **Cinema 4D** |
| **Tiempo real** | **Mientras se emite**, a la velocidad del vídeo | **Unreal**, **Unity**, **Vizrt**, **Chyron** |

## 7. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 3 | Para qué sirve un trazado | a) Contornear con precisión un objeto irregular ✔ |
| 6 | Qué es el área de trabajo | a) La sección de la línea de tiempo para previsualizar o renderizar ✔ |
| 10 | Cómo anidar dos capas | b) Seleccionarlas y precomponer ✔ |
| 18 | Qué capa está en primer término con capas 2D | a) La de numeración más baja ✔ |
| 26 | A qué afectan las luces virtuales | b) A las capas en 3D ✔ |
| 28 | Formato que conserva capas y efectos | b) `PSD` ✔ |
| 42 | A qué programa pertenecen los *blueprints* | b) Unreal ✔ |
| 48 | Función que vectoriza una imagen | a) Calco de imagen ✔ |
| 50 | Programa profesional de 3D | b) Blender ✔ |
| 56 | Qué hace «recopilar archivos» | c) Copia los archivos usados junto al proyecto ✔ |
| 63 | Tamaño de un fotograma `TGA` sin compresión | d) El mismo en todos los casos ✔ |
| 64 | Formato que NO admite CMYK | b) `PNG` ✔ |
| 69 | Características de las curvas Bézier | c) Nodo inicial, final, punto de control y palanca ✔ |
| 71 | Operación de buscatrazos del resultado mostrado | a) Restar ✔ **·** figura |
| 75 | Parámetro que anima el desenfoque de una máscara | d) Calado de máscara ✔ |
| 78 | Si se puede doblar el tamaño sin pérdida | b) Sí, si es vectorial ✔ |
| 81 | Qué es un archivo con códec `H.265` | d) Compresión que admite 8K y ahorra hasta el 50 % ✔ |
| 82 | Número máximo de canales de una imagen | b) 56 ✔ |
| 83 | Si se pueden hacer composiciones verticales | a) Sí, hasta 30.000 píxeles de alto ✔ |
| 93 | Qué es el efecto *wiggle* | d) Un efecto de movimiento aleatorio ✔ |

**Las veinte respuestas oficiales son correctas**, y **una descansa en la plantilla**: la 71, que
lleva figura.

**El aviso de estudio**: **nueve de las veinte son de un solo programa.** **Si el tiempo es escaso,
ahí está el rendimiento**: **con las ocho reglas del epígrafe 4 se contestan nueve preguntas.**

## 8. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cinco declaraciones expresas:**

1. **La documentación de los programas citados no se ha consultado.** **Lo que el tema afirma de cada
   función es de uso corriente en el oficio**, y **coincide con las respuestas oficiales.**
2. **Photoshop, Illustrator, InDesign, After Effects, Blender, Cinema 4D, Unreal, Unity, Vizrt,
   Chyron, Brainstorm y Audition son nombres de producto**, citados por su categoría y por la función
   que la respuesta oficial les atribuye. **El temario no les atribuye ninguna característica más.**
3. **Las dos cifras memorísticas —56 canales y 30.000 píxeles— se reproducen de las propias
   respuestas oficiales**, y **el temario declara que son memoria y no razonamiento.**
4. **La pregunta 71 depende de una figura que este temario no ha visto.** **No se describe**: se
   declara, y **se da la tabla de las cinco operaciones de buscatrazos**, que es la regla de su
   familia.
5. **Las normas que definen los formatos de fichero y los códecs no se han consultado.** **La tabla
   del epígrafe 5 recoge el uso corriente de cada uno**, y **la comparación entre las dos
   generaciones de códec procede de la propia respuesta oficial de la pregunta 81.**

**El resto del tema va como oficio y así se declara**: la tabla de familias de programa, la distinción
entre área y espacio de trabajo, la razón de que una luz no afecte a una capa plana, la explicación
de por qué un programa no mueve ficheros ajenos, el argumento de que sin compresión el tamaño no
depende de la organización de los datos y la diferencia entre renderizado diferido y tiempo real.
**Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo
presenta como si lo estuviera.
