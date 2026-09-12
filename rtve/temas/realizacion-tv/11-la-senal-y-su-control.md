# Tema 11 del específico de Realización Televisión · Conocimientos básicos de televisión: la señal y su control

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Realización Televisión · punto 3.1 |
| **Sirve para** | **Realización Televisión** |
| **Fuente** | **Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida**, cuyos cuadros sostienen las unidades fotométricas; y **las Recomendaciones UIT-R BT.601, BT.709, BT.2020 y BT.2100** como referencia. El resto —estructura de la señal, monitorización y percepción— **va como oficio** |
| **Identificador** | `BOE-A-2010-927` · BOE núm. 18, de 21/01/2010 · **UIT-R BT.2100**, citada por remisión |
| **Redacción que se estudia** | La vigente el **21/12/2022**, con la modificación del **RD 493/2020** ya incorporada |
| **Ojo con la** | **pregunta 37: su formulación es discutible.** Que la sensación de relieve **aumente** con la distancia puede sostenerse al revés si se atiende a la estereoscopia, que desaparece con la distancia. **Lo que hace defendible la respuesta oficial es que en una imagen plana el relieve descansa en los indicios monoculares**, más abundantes cuanta más profundidad tiene la escena. **La respuesta descansa en la plantilla y el tema lo declara** |
| **Extensión** | **3.915 palabras** |

<!-- /portada -->

Las siglas y unidades de este tema, presentadas de entrada: la unidad de control de cámara (**CCU**);
la candela por metro cuadrado (**cd/m²**), que en la industria se llama ***nit***; el alto rango
dinámico (**HDR**) y el estándar (**SDR**); la luminancia (**Y**) y las dos señales de diferencia de
color (**Cb** y **Cr**); los tres primarios (**RGB**); el bit, unidad de información; y la Unión
Internacional de Telecomunicaciones (**UIT**), cuyo sector de radiocomunicaciones (**UIT-R**) publica
las recomendaciones que este tema cita.

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización, punto 3.1):
> «LA TECNOLOGÍA EN EL ÁMBITO DE LA REALIZACIÓN. Conocimientos básicos de televisión. Estructura de
> la imagen de TV. Monitorización y control.»

**Ocho preguntas.** Y es **el punto que un realizador necesita para hablar con el control de imagen**:
**qué es la señal, con qué se mira y qué significa cada número.**

**Su particularidad, y es lo que lo distingue de los puntos equivalentes de las ocupaciones
técnicas**: **tres de sus ocho preguntas no son de señal sino de PERCEPCIÓN VISUAL.** **El tribunal ha
entendido «estructura de la imagen de TV» incluyendo cómo la ve el ojo**, y **eso conecta este punto
con el temario de Información Gráfica de este mismo proceso.**

<!-- indice -->

## Índice

- [1. La estructura de la señal de televisión](#1-la-estructura-de-la-señal-de-televisión)
- [2. La crominancia y sus dos parámetros](#2-la-crominancia-y-sus-dos-parámetros)
- [3. La profundidad de color](#3-la-profundidad-de-color)
- [4. El rango dinámico](#4-el-rango-dinámico)
- [5. El nit y las unidades de luminancia](#5-el-nit-y-las-unidades-de-luminancia)
- [6. La monitorización: los grados de monitor](#6-la-monitorización-los-grados-de-monitor)
- [7. Las constantes perceptivas](#7-las-constantes-perceptivas)
- [8. La percepción de la profundidad](#8-la-percepción-de-la-profundidad)
- [9. Los datos que el examen ha preguntado](#9-los-datos-que-el-examen-ha-preguntado)
- [10. Trazabilidad](#10-trazabilidad)

<!-- /indice -->

## 1. La estructura de la señal de televisión

**La televisión no transmite rojo, verde y azul**: transmite **una señal de luminancia y dos de
diferencia de color.**

| Componente | Qué lleva |
|---|---|
| **Luminancia (Y)** | **El BRILLO**: la imagen en blanco y negro |
| **Diferencias de color (Cb, Cr)** | **EL COLOR**, como diferencia respecto de la luminancia |

**Por qué se hace así, y es la razón de todo lo demás**: **el ojo distingue mucho mejor los detalles de
brillo que los de color.** **Separar las dos cosas permite dedicar menos ancho de banda al color sin
que se note**, y **de ahí sale el submuestreo cromático** —4:2:2, 4:2:0— **que el punto 3.2 de este
mismo anexo desarrolla.**

**La luminancia se construye pesando los tres primarios**, y **los pesos no son iguales**: **el verde
aporta la mayor parte del brillo percibido y el azul la menor.** **Las Recomendaciones UIT-R BT.601,
BT.709 y BT.2020 fijan esos pesos para la definición estándar, la alta y la ultra alta.**

**Y lo que un realizador hace con esto, que es lo que justifica el punto**: **cuando pide al control de
imagen que «suba el negro» o que «baje la ganancia», está pidiendo una operación sobre la luminancia;
cuando pide que «quite el verde», está pidiendo una sobre las diferencias de color.** **Son dos
mandos distintos y dos instrumentos distintos.**

## 2. La crominancia y sus dos parámetros

**Los parámetros que definen la crominancia son la saturación y el tono.** Ésa es la respuesta oficial
a la pregunta 110.

| Parámetro | Qué es | Dónde se ve en el vectorscopio |
|---|---|---|
| **TONO** (*hue*) | **De qué color es**: rojo, verde, azul… | **EL ÁNGULO** respecto del centro |
| **SATURACIÓN** | **Cuánto color tiene**: de gris a puro | **LA DISTANCIA al centro** |
| **Brillo** o luminancia | **Cuánta luz tiene** | **NO está en el vectorscopio**: está en la forma de onda |

**Por qué el brillo NO es un parámetro de la crominancia, y es la clave de la pregunta**: **la
crominancia es, por definición, LA PARTE DE LA SEÑAL QUE NO ES LUMINANCIA.** **El brillo es la
luminancia**, así que **no puede ser a la vez un parámetro de la crominancia.**

**Las tres opciones falsas incluyen todas el brillo o el contraste**, que **son magnitudes de la
luminancia:**

| Opción | Qué mezcla |
|---|---|
| «Brillo y tono» | **Uno de luminancia y uno de crominancia** |
| «Brillo y saturación» | **Uno de cada** |
| «Saturación y contraste» | **Uno de crominancia y uno de luminancia** |

**La regla que resuelve la pregunta sin saber nada de vectorscopios**: **de las cuatro opciones, sólo
una NO nombra ninguna magnitud de brillo.** **Ésa es la buena.**

**Y la lectura del vectorscopio, que es lo que un realizador ve en el control**: **el centro es la
ausencia de color.** **Una imagen en blanco y negro es un punto en el centro; una con dominante, un
punto desplazado hacia el color de la dominante; y las barras de color dibujan seis cajas en seis
ángulos fijos.**

## 3. La profundidad de color

**La profundidad de color depende del número de bits utilizados para representar cada color.** Ésa es
la respuesta oficial a la pregunta 6.

| Bits por canal | Niveles por canal | Dónde se usa |
|---|---|---|
| **8 bits** | **256** | **El mínimo profesional**; consumo |
| **10 bits** | **1.024** | **El estándar de producción de televisión** |
| **12 bits** | 4.096 | Cine digital, alto rango dinámico |

**La profundidad de color mínima en los equipos profesionales de imagen es de 8 bits.** Ésa es la
respuesta oficial a la pregunta 66.

**Las tres opciones falsas de la pregunta 66:**

| Opción | Por qué no |
|---|---|
| **4 bits** | **Dieciséis niveles por canal**: **es profundidad de gráficos antiguos**, no de imagen profesional |
| **16 bits** | **Existe**, pero **en tratamiento de imagen fija y en composición**, no como mínimo de equipo de vídeo |
| **32 bits** | **Existe en coma flotante para composición**, y **no es un mínimo** |

**La trampa está en que la pregunta pide el MÍNIMO**: **quien piense en lo que se usa hoy en producción
marcaría diez bits**, **y quien piense en lo máximo marcaría dieciséis o treinta y dos.** **La pregunta
pide el suelo**, y **el suelo profesional son ocho.**

**Y las tres opciones falsas de la pregunta 6 son las tres confusiones clásicas:**

| Opción | Qué confunde |
|---|---|
| «La resolución en píxeles por pulgada» | **Confunde profundidad con RESOLUCIÓN**: cuántos píxeles hay, no cuántos valores tiene cada uno |
| «El tipo de archivo» | **El formato PUEDE limitar la profundidad, pero no la define** |
| «El tamaño de los píxeles en la pantalla» | **Es una propiedad del monitor**, no de la imagen |

**La distinción que hay que fijar**: **resolución es CUÁNTOS píxeles hay; profundidad de color es
CUÁNTOS VALORES puede tomar cada uno.** **Son dos ejes independientes**, y **el defecto de una escasa
profundidad —las franjas en un degradado— no se arregla con más resolución.**

## 4. El rango dinámico

**El rango dinámico de una imagen digital es la capacidad de la imagen muestreada de representar
correctamente el contraste, las altas luces y las sombras profundas.** Ésa es la respuesta oficial a la
pregunta 65.

**Qué es, en una frase**: **la distancia entre lo más oscuro y lo más claro que la imagen puede
representar CON DETALLE.** **No es cuánto contraste tiene una imagen: es cuánto contraste PUEDE
recoger.**

**Las tres opciones falsas y su error, que es instructivo:**

| Opción | Qué describe | Por qué no |
|---|---|---|
| «Reproducir el movimiento con mayor precisión, aumentando la tasa de fotogramas y la frecuencia de muestreo» | **La resolución TEMPORAL** | **Es otro eje**: cuántas imágenes por segundo |
| «El incremento de la cuantificación espacial y temporal para obtener imágenes de mayor definición» | **La resolución** | **Otro eje más** |
| «**El incremento del contraste** entre las altas luces y las sombras profundas» | **LA TRAMPA MEJOR PUESTA** | **Cambia CAPACIDAD DE REPRESENTAR por INCREMENTO.** **El rango dinámico no incrementa el contraste de una imagen: es la capacidad de recogerlo.** Una imagen de mucho rango dinámico puede ser plana |

**La palabra que decide es «CAPACIDAD»**: **la respuesta correcta habla de lo que la imagen PUEDE
representar; la falsa habla de aumentar lo que TIENE.**

**Y la relación con la profundidad de color del epígrafe anterior, que conviene tener clara porque se
confunden**: **el rango dinámico lo determina el *sensor*; la profundidad de bits determina si ese rango
se puede *codificar* sin escalones.** **Un rango amplio con pocos bits se rompe en franjas y deja de ser
aprovechable.** **Los dos hacen falta.**

## 5. El nit y las unidades de luminancia

**Un *nit* equivale a una candela por metro cuadrado.** Ésa es la respuesta oficial a la pregunta 55.

**Y esto no es convención de sector: está en el Boletín Oficial del Estado.** **El Real Decreto
2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida, recoge la
luminancia en su cuadro de unidades derivadas coherentes del Sistema Internacional**, con el símbolo
de la magnitud, el nombre de la unidad y su expresión. **Ésta es su fila, con las celdas separadas por
puntos porque un cuadro no se puede entrecomillar de otra manera; cada celda va literal:**

> «luminancia» · «Lv» · «candela por metro cuadrado» · «cd/m2»

**El *nit* es, por tanto, el nombre de uso industrial de una unidad legal española**, y **la pregunta
55 se contesta con el cuadro del real decreto delante.**

| Unidad | Qué mide | Cómo la recoge el Real Decreto 2032/2009 |
|---|---|---|
| ***NIT*** | **Luminancia** | **«candela por metro cuadrado» · «cd/m2»** |
| **Candela** | **Intensidad luminosa** de una fuente: **no incluye superficie** | **Unidad básica del Sistema Internacional**, «símbolo cd» |
| **Lumen** | **Flujo luminoso** total | **«flujo luminoso» · «lumen» · «lm»** |
| **Lux** | **Iluminancia**: la luz que LLEGA a una superficie | **«iluminancia» · «lux» · «lx» · «lm/m2»** |

**Las tres opciones falsas ofrecen la misma unidad con otro denominador** —milímetro, centímetro y
decímetro cuadrado—, y **la pregunta se contesta sabiendo cuál es la unidad de superficie del sistema
internacional: el METRO cuadrado.** **El real decreto lo zanja: es el metro cuadrado.**

**Y el orden de magnitud, que da sentido a la cifra**:

| Situación | Luminancia aproximada |
|---|---|
| **Monitor de rango dinámico estándar** | **Alrededor de 100 nits** |
| **Monitor de referencia de alto rango dinámico** | **1.000 cd/m² o más de pico**, con un negro de 0,005 cd/m² o menos |

**Por qué le importa a un realizador**: **porque el paso al alto rango dinámico cambia la
monitorización.** **Un programa masterizado en alto rango dinámico se juzga en un monitor capaz de
darlo**, y **verlo en uno estándar no dice nada.** **Es el mismo problema que el temario de Edición y
Montaje trata al hablar del etalonaje.**

## 6. La monitorización: los grados de monitor

**No todos los monitores de un control sirven para lo mismo**, y **la industria los clasifica por
grados según su fidelidad.**

| Grado | Qué garantiza | Dónde va |
|---|---|---|
| **GRADO 1** | **Fidelidad de referencia**: colorimetría calibrada, gamma y punto de blanco normalizados, uniformidad | **Donde se JUZGA la imagen** |
| **Grado 2** | Buena calidad, sin garantía de referencia | Monitorización de trabajo |
| **Grado 3** | Comprobación de que hay señal y de qué señal es | **Los monitores de vigilancia y de multivisor** |

**El puesto en el que es prioritario trabajar con un monitor de grado 1 es el puesto de la unidad de
control de cámara.** Ésa es la respuesta oficial a la pregunta 9.

**Por qué ahí y no en el puesto del realizador, que es lo que la pregunta mide**, y el razonamiento es
de reparto de tareas:

| Puesto | Qué decide mirando el monitor | ¿Necesita referencia? |
|---|---|---|
| **CONTROL DE IMAGEN (CCU)** | **El AJUSTE de cada cámara**: iris, negros, ganancia, balance, casar unas con otras | **SÍ: absolutamente.** **Está decidiendo el color y la exposición de lo que sale** |
| **Realizador, previo y programa** | **QUÉ plano sale y cuándo** | **No de referencia**: necesita ver bien, no medir |
| **Realizador, monitores de cámaras** | **Qué tiene cada cámara** | **No**: son de vigilancia |
| **Visores de cámara** | **Encuadre y foco** | **No pueden serlo**: son pequeños y van en la cámara |

**La regla que resuelve la pregunta**: **el monitor de referencia va donde se JUZGA el color, no donde
se decide el corte.** **El realizador decide contenido; el control de imagen decide calidad.** **Es la
misma regla del tema 10: cada puesto responde de lo suyo.**

**Y el dato de oficio que la acompaña**: **un monitor de grado 1 exige calibración periódica y un
entorno de visionado controlado** —luz ambiente y fondo normalizados—. **Un monitor de referencia en
una sala con una ventana detrás deja de ser de referencia.**

## 7. Las constantes perceptivas

**Las constantes perceptivas son unos mecanismos psíquicos gracias a los cuales el mundo exterior
tridimensional permanece estable para nuestro sistema perceptivo.** Ésa es la respuesta oficial a la
pregunta 111.

**Qué resuelven, y por qué son necesarias**: **la imagen que llega a la retina cambia todo el rato** —el
tamaño de un objeto en la retina depende de la distancia, su forma depende del ángulo, su color depende
de la luz que lo ilumina—. **Y sin embargo el mundo se percibe estable.** **Las constantes son los
mecanismos que producen esa estabilidad.**

| Constante | Qué mantiene estable |
|---|---|
| **De TAMAÑO** | **Un objeto que se aleja no parece encoger**, aunque su imagen retiniana sí |
| **De FORMA** | **Una puerta que se abre sigue pareciendo rectangular**, aunque su proyección sea un trapecio |
| **De COLOR** | **Un papel blanco parece blanco bajo tungsteno y bajo luz día**, aunque refleje luces de color distinto |
| **De CLARIDAD** | Una superficie mantiene su claridad relativa aunque cambie la iluminación |

**Las tres opciones falsas y por qué se caen:**

| Opción | Qué describe |
|---|---|
| «Vemos siempre los colores de igual forma aunque cambie el tipo de luz» | **LA TRAMPA MEJOR PUESTA**: **describe correctamente UNA de las constantes —la de color— y la presenta como si fuera todas.** **Es una parte por el todo** |
| «Al desplazar el punto de vista la escena se desplaza de forma constante» | **Describe el PARALAJE**, que es otro fenómeno |
| «Ilusión del movimiento aparente por la sucesión de imágenes» | **El fenómeno *Phi***, que el temario de Información Gráfica desarrolla |

**Cómo se contesta**: **la opción a) es la única que da una DEFINICIÓN GENERAL** —«mecanismos psíquicos
gracias a los cuales el mundo permanece estable»—; **las otras tres dan ejemplos o describen otros
fenómenos.** **La pregunta usa el plural —«las constantes»— y sólo una opción habla de un conjunto de
mecanismos.**

**Y su consecuencia para el oficio, que es lo que justifica el epígrafe**: **la constancia de color es
la razón de que el balance de blancos sea necesario.** **El ojo corrige automáticamente la dominante de
la luz y la cámara no**: **por eso un plano rodado bajo tungsteno sin corregir sale naranja aunque
quien estaba allí viera los blancos blancos.** **La cámara no tiene constantes perceptivas; el operador
tiene que suplirlas.**

## 8. La percepción de la profundidad

**La sensación de relieve aumenta con la distancia.** Ésa es la respuesta oficial a la pregunta 37.

**El razonamiento, y hay que verlo despacio porque la respuesta es contraintuitiva.** **La visión
estereoscópica —la que da relieve por la diferencia entre lo que ven los dos ojos— es eficaz sólo a
corta distancia**: **más allá de unos metros, las dos imágenes retinianas son casi idénticas y el
relieve estereoscópico desaparece.** **A distancias largas, la profundidad se percibe por OTROS
indicios**, y son los que un realizador maneja:

| Indicio de profundidad | En qué consiste | ¿Funciona a distancia? |
|---|---|---|
| **Estereoscopia** | La diferencia entre los dos ojos | **NO: sólo cerca** |
| **Perspectiva lineal** | **Las paralelas convergen** | **Sí, y más cuanto más lejos** |
| **Tamaño relativo** | **Lo lejano se ve más pequeño** | **Sí** |
| **Interposición** | **Lo cercano tapa a lo lejano** | **Sí** |
| **Perspectiva aérea** | **Lo lejano se ve más claro, más azulado y con menos contraste** | **Sí, y sólo a distancia** |
| **Gradiente de textura** | La textura se aprieta al alejarse | **Sí** |
| **Paralaje de movimiento** | Lo cercano se desplaza más que lo lejano al mover el punto de vista | **Sí** |

**Y ahí está la clave de la respuesta oficial**: **al aumentar la distancia, los indicios que se pierden
son los binoculares —que sólo sirven cerca— y los que ganan peso son los MONOCULARES**, que son
**precisamente los que una imagen plana puede reproducir.** **Una fotografía o un plano de televisión no
tienen estereoscopia**, así que **su sensación de relieve descansa entera en los indicios monoculares**,
y **ésos son más ricos cuanto más profundidad tiene la escena.**

**Las tres opciones falsas:**

| Opción | Por qué no |
|---|---|
| «La sensación de relieve DISMINUYE con la distancia» | **Es lo contrario de la respuesta oficial** |
| «No influye» | Niega la relación |
| «Depende de la óptica que se use» | **LA TRAMPA MEJOR PUESTA, porque contiene una verdad**: **la focal SÍ afecta a la percepción de la profundidad** —el teleobjetivo comprime los planos y el gran angular los separa—. **Lo que la descarta es que el enunciado pregunta por la DISTANCIA, no por la óptica** |

**Una declaración expresa, y es necesaria**: **la formulación de la respuesta oficial —«la sensación de
relieve aumenta con la distancia»— no es una afirmación pacífica en psicología de la percepción.**
**Según qué indicios se consideren, puede sostenerse lo contrario**: **la percepción de profundidad
ABSOLUTA es más precisa cerca**, y **la estereoscopia desaparece con la distancia.** **Lo que este tema
sostiene, y es lo que hace la respuesta defendible, es que en una IMAGEN PLANA —que es de lo que trata
un temario de televisión— la sensación de relieve depende de los indicios monoculares, y esos indicios
son más abundantes cuanto mayor es la profundidad de la escena.** **La respuesta descansa en la
plantilla oficial**, y **el tema no la presenta como un hecho establecido de la psicología de la
percepción.**

**Y su traducción a realización, que es lo que un realizador saca de aquí**: **para dar sensación de
profundidad en un plano, hay que construir TÉRMINOS.** **Algo cerca, algo en medio y algo lejos.** **Un
plano de una pared frontal no tiene profundidad por mucha distancia que haya**, y **un plano con una
figura en primer término, la acción en el medio y un fondo lejano la tiene aunque el espacio sea
pequeño.**

## 9. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 6 | De qué depende la profundidad de color | a) Del número de bits para representar cada color ✔ |
| 9 | En qué puesto es prioritario un monitor de grado 1 | d) En el puesto de CCU ✔ |
| 37 | Cómo influye la distancia en la percepción de profundidad | a) La sensación de relieve aumenta con la distancia ⚠ **formulación discutible; ver el epígrafe 8** |
| 55 | A qué equivale un *nit* | d) A una candela por metro cuadrado ✔ |
| 65 | Qué es el rango dinámico de una imagen digital | b) La capacidad de representar contraste, altas luces y sombras ✔ |
| 66 | Profundidad de color mínima en equipos profesionales | b) 8 bits ✔ |
| 110 | Qué parámetros definen la crominancia | d) Saturación y tono ✔ |
| 111 | Qué son las constantes perceptivas | a) Mecanismos psíquicos que mantienen estable el mundo ✔ |

**Las ocho respuestas oficiales son correctas**, y **una tiene una formulación discutible fuera del
contexto de la imagen plana**, que va explicada.

**El aviso de estudio, y es el mismo mecanismo de los temas 7 y 8**: **cuatro de las ocho preguntas
tienen como opción falsa una afirmación VERDADERA que no responde a lo que se pregunta.** **La 65
ofrece «el incremento del contraste», que es cierto de otra cosa; la 111 ofrece la constancia de color,
que es UNA de las constantes; la 37 ofrece la dependencia de la óptica, que es cierta; y la 66 ofrece
profundidades reales que no son el mínimo.** **En este cuadernillo casi nada es falso.**

**Y la regla que resuelve tres preguntas de golpe**: **saber qué eje es cada cosa.** **Resolución
espacial, resolución temporal, profundidad de color y rango dinámico son CUATRO EJES
INDEPENDIENTES**, y **las opciones falsas de las preguntas 6, 65 y 66 consisten en cambiar uno por
otro.**

## 10. Trazabilidad

**Este tema cita una norma del BOE.** Su materia es la estructura de la señal de televisión, su
monitorización y la percepción visual, y **va como oficio y con norma técnica de referencia**, salvo
las unidades fotométricas, que **sí están en un real decreto.**

| Nivel | Fuente | Qué se ha tomado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida** (BOE núm. 18, de 21/01/2010), **en su redacción vigente el 21 de diciembre de 2022** | **Los cuadros de unidades**: la luminancia en candelas por metro cuadrado, el flujo luminoso en lúmenes y la iluminancia en lux, **citados literalmente** |
| **Segundo: organismo de normalización** | **Recomendaciones UIT-R BT.601, BT.709 y BT.2020** | **Su existencia y su objeto**: fijan los pesos de la luminancia para definición estándar, alta y ultra alta. **No se citan cifras de ellas en este tema** |
| **Segundo: organismo de normalización** | **Recomendación UIT-R BT.2100** | **Las cifras de referencia del monitor de alto rango dinámico** |
| **Quinto: la plantilla oficial** | **Una afirmación**: que la sensación de relieve aumenta con la distancia | Pregunta 37 |

**Tres declaraciones expresas:**

1. **La formulación de la pregunta 37 no es una afirmación pacífica en psicología de la percepción.**
   **Según qué indicios se consideren, puede sostenerse lo contrario**: la percepción de profundidad
   absoluta es más precisa cerca y la estereoscopia desaparece con la distancia. **Lo que este tema
   sostiene es que en una IMAGEN PLANA la sensación de relieve descansa en los indicios monoculares y
   que ésos son más abundantes cuanta más profundidad tiene la escena**, **y eso hace la respuesta
   defendible en el contexto de un temario de televisión.** **La respuesta descansa en la plantilla
   oficial**, y **el tema lo declara en lugar de presentarla como un hecho establecido.**
2. **La clasificación de los monitores en grados no es una norma legal.** **Es una convención de la
   industria de la radiodifusión**, con criterios que las casas y los fabricantes aplican con matices.
   **El tema la presenta como práctica de sector.**
3. **La tipología de las constantes perceptivas y de los indicios de profundidad procede de la
   psicología de la percepción**, y **este proyecto no ha volcado una fuente de esa disciplina.** **Son
   clasificaciones asentadas y recogidas en cualquier manual**, y **el tema las presenta como
   conocimiento común de la materia.**

**Y una remisión**: **las cifras de referencia del monitor de alto rango dinámico y los coeficientes de
luminancia de las tres recomendaciones están verificados literalmente en los temarios de Edición y
Montaje y de Información Gráfica de este mismo proyecto**, con el cuadro de la norma delante. **Aquí se
citan por remisión y no se vuelven a sostener.**
