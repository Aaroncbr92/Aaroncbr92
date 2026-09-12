# Tema 14 del específico de Técnica de Equipos y Sistemas Electrónicos · Medidas de la señal de vídeo, audio y radiofrecuencia

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica de Equipos y Sistemas Electrónicos · punto 16 |
| **Sirve para** | **Técnica de Equipos y Sistemas Electrónicos** |
| **Fuente** | **Sin norma: no la hay.** Su materia son las medidas de vídeo, audio y radiofrecuencia, y **va entera como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Sólo con la plantilla** | **SIETE de sus NUEVE preguntas dependen de una figura: la proporción más alta de los diecisiete temas de esta ocupación.** El temario no ha visto ninguna y no describe ninguna: **da la regla de la familia de cada una** y atribuye la respuesta a la plantilla |
| **Extensión** | **4.200 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el monitor de forma de onda (**WFM**, *waveform
monitor*); la luminancia y las dos diferencias de color en componentes analógicas (**YPbPr**) y en
componentes digitales (**YCbCr**, de donde salen las **Cr** y **Cb** que una opción nombra); los tres
primarios rojo, verde y azul (**RGB**); la interfaz digital serie de alta definición (**HD-SDI**), de la
Sociedad de Ingenieros de Cine y Televisión (**SMPTE**), las dos presentadas en el tema 8; el final y el comienzo de vídeo activo (**EAV** y **SAV**), también del tema
8; la Unión Europea de Radiodifusión (**UER**, cuyas barras de color dan nombre a una señal de
prueba); la modulación de frecuencia (**FM**); el sistema de datos por radio (**RDS**, *radio data
system*); la radiofrecuencia (**RF**); el transmisor (**Tx**); el megahercio (**MHz**) y el kilohercio
(**kHz**). **Y una advertencia sobre una palabra que aparece en una opción del examen**: **VALID**, en
la pregunta 9 del segundo cuadernillo, **se reproduce tal como el enunciado la escribe** y **este
temario no le atribuye ninguna forma larga**, porque no ha verificado ninguna.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, punto 16):
> «MEDIDAS DE LA SEÑAL DE VIDEO, AUDIO y RF: Distorsiones de la señal Clasificación. Líneas test,
> Barras UER. Parámetros que pueden medirse sobre las líneas Test y procedimientos de medida. Medidas
> de la señal de TV digital. Medidas y unidades de la señal de audio. Medidas de espectro y nivel de
> la señal de RF.»

**Nueve preguntas.** **Y el punto más gráfico de todo el proyecto**: **siete de sus nueve preguntas
enseñan una pantalla y piden que se interprete.**

**Esa proporción —siete de nueve— es la más alta de los diecisiete temas de esta ocupación**, que es
a su vez **la ocupación con más preguntas dependientes de imagen de todo el proyecto**, y **obliga a decir de entrada cómo se ha resuelto**: **este temario no ha
visto ninguna de las siete imágenes y no describe ninguna.** **Lo que hace, pregunta por pregunta, es
dar la regla de la familia a la que la imagen pertenece y declarar que la respuesta concreta descansa
en la plantilla oficial.** **En varias de ellas la regla de la familia elimina dos o tres opciones sin
ver nada**, y **eso se dice donde ocurre.**

**Las dos preguntas sin figura son las dos únicas enteramente razonables**: **la 27, que es de líneas
de prueba, y la 39, que es una fórmula.**

<!-- indice -->

## Índice

- [1. Las líneas de prueba y lo que cada una mide](#1-las-líneas-de-prueba-y-lo-que-cada-una-mide)
- [2. El monitor de forma de onda y sus modos](#2-el-monitor-de-forma-de-onda-y-sus-modos)
- [3. Las señales de sincronía entre componentes y entre audio y vídeo](#3-las-señales-de-sincronía-entre-componentes-y-entre-audio-y-vídeo)
- [4. La señal patológica y la ecualización](#4-la-señal-patológica-y-la-ecualización)
- [5. Las medidas de audio y de radiofrecuencia](#5-las-medidas-de-audio-y-de-radiofrecuencia)
- [6. Los datos que el examen ha preguntado](#6-los-datos-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Las líneas de prueba y lo que cada una mide

**La pregunta 27**: **la señal de prueba conocida como «escalera de luminancia» permite medir la
alinealidad de la ganancia de luminancia.** Ésa es la respuesta oficial.

---

**Qué es una escalera de luminancia**: **una señal que sube por escalones iguales desde el negro hasta
el blanco.** **Si la cadena que la transporta fuera perfecta, los escalones saldrían por el otro
extremo tan iguales como entraron.** **No lo son**: las etapas de amplificación tienen más ganancia en
unas zonas de la curva que en otras, **y eso se ve como escalones desiguales.** **Esa desigualdad es
exactamente la alinealidad de la ganancia de luminancia.**

**El inventario de señales de prueba y lo que cada una mide, que es lo que hay que llevar aprendido de
este epígrafe:**

| Señal de prueba | Qué mide |
|---|---|
| **Escalera de luminancia** | **Alinealidad de la ganancia de luminancia** ✔ |
| **Escalera modulada** | **Ganancia diferencial y fase diferencial**: cómo cambia la crominancia según el nivel de luminancia sobre el que va montada |
| **Multiburst** | **Respuesta en frecuencia**: paquetes de frecuencia creciente y misma amplitud |
| **Barra y ventana** | **Respuesta a bajas frecuencias y a los transitorios** |
| **Diente de sierra** | **Linealidad de la rampa completa** |
| **Barras de color** | **Colorimetría, saturación y niveles de referencia** |
| **Bowtie** | **Retardo relativo entre las tres componentes**, del que trata el epígrafe 3 |

**Y las tres opciones falsas de la pregunta se ordenan solas con ese cuadro:**

| Opción | Qué señal mediría eso |
|---|---|
| **a) Retardo entre luminancia y crominancia** | **El pulso 2T y la barra, o la señal Bowtie** |
| **b) Ganancia entre luminancia y crominancia** | **La barra modulada** |
| **d) Ganancia diferencial** | **La escalera modulada**, no la de luminancia |

**El matiz que decide entre la c y la d, que es donde se juega la pregunta**: **la escalera de
luminancia no lleva crominancia encima.** **Sin crominancia no se puede medir nada diferencial**,
porque lo diferencial es cómo se comporta el color según el nivel de luz. **Una escalera desnuda sólo
puede hablar de la luminancia**, y de ella dice si su ganancia es lineal.

**La pregunta 77 enseña una señal de prueba y pide identificarla.** **La plantilla da una señal
Multiburst.** **Este temario no ha visto la imagen.** **La regla de la familia, que elimina dos
opciones sin verla:**

| Opción | Qué se vería |
|---|---|
| **a) Bowtie** | **Dos trazas en forma de lazo que se cruzan en el centro**: no se parece a nada de las otras tres |
| **b) Barras de color al 75 %** | **Escalones que bajan de blanco a negro pasando por seis colores, cada uno de una altura** |
| **c) Diente de sierra** | **Una rampa continua que sube y cae de golpe** |
| **d) Multiburst** | **Paquetes de senoide de frecuencia creciente y amplitud igual, sobre un mismo nivel** ✔ |

**Y lo que las distingue de un vistazo es si hay relleno o no**: **el multiburst y las barras son
bloques macizos de trazo; el diente de sierra es una línea única.** **La identificación concreta
descansa en la plantilla**, y el temario lo declara.

## 2. El monitor de forma de onda y sus modos

**La pregunta 23 del segundo cuadernillo** enseña la pantalla de un monitor de forma de onda digital
con barras UER al 75 % en su entrada y pide en qué opción está configurado. **La plantilla da «RGB» y
«Parade».** **Este temario no ha visto la imagen.**

**La regla de la familia, que aquí es una tabla de doble entrada y se puede construir entera:**

| | **Overlay** (superpuesto) | **Parade** (en desfile) |
|---|---|---|
| **YPbPr** | **Las tres componentes dibujadas una encima de otra**: la luminancia arriba y las dos diferencias centradas en el cero, con valores positivos y negativos | **Tres trazas una al lado de otra**: la de luminancia con forma de escalera descendente y las dos de color centradas y simétricas |
| **RGB** | **Los tres primarios superpuestos**: tres escaleras encajadas, todas por encima del cero | **Tres escaleras seguidas, cada una en su tercio de pantalla, todas del mismo tipo** |

**Y las dos preguntas que resuelven la tabla, que es lo que hay que saber hacer:**

1. **¿Hay tres trazas separadas horizontalmente o una sola zona con todo encima?** **Separadas es
   «parade»; encima es «overlay».**
2. **¿Las trazas bajan por debajo del cero?** **En YPbPr las dos de color son bipolares y bajan; en
   RGB las tres son unipolares y no bajan nunca del negro.**

**La lectura concreta descansa en la plantilla**, y el temario lo declara. **Lo que sí queda dicho es
para qué sirve cada modo**: **el modo RGB en desfile es el que se usa para comprobar que ninguna
componente se sale de la gama**, porque **con las tres una al lado de otra se ve de un golpe cuál
rebasa por arriba o por abajo.** **El modo YPbPr superpuesto es el de trabajo diario**, porque ocupa
menos pantalla.

**La pregunta 9 del segundo cuadernillo** enseña unas marcas que aparecen entre las señales YPbPr en
la ventana del monitor de forma de onda de un rasterizador y pregunta qué representan. **La plantilla
da el patrón de sincronización EAV y los datos auxiliares correspondientes a audio embebido.** **Este
temario no ha visto la imagen.**

**Lo que sí se puede razonar entero, y es la mitad de la pregunta**: **el tema 8 explicó qué son EAV y
SAV y dónde van.** **El intervalo de borrado horizontal de una trama digital serie lleva, por ese
orden, el final de vídeo activo, el espacio auxiliar y el comienzo de vídeo activo**, y **el espacio
auxiliar es donde viaja el audio embebido.** **Un monitor de forma de onda que enseñe la línea
completa, y no sólo la parte activa, dibuja todo eso a la izquierda de la imagen.**

**Las cuatro opciones y lo que cada una supondría:**

| Opción | Veredicto razonado |
|---|---|
| **a) Ruido por mala sincronización de Pb y Pr** | **Un ruido no aparece en el mismo sitio de todas las líneas**: lo que se ve es regular |
| **b) Metadatos de la señal VALID** | **Confunde una señalización de validez con el espacio auxiliar** |
| **c) Patrón SAV** | **La mitad correcta**: el SAV existe, pero va al final del borrado y no arrastra los datos auxiliares |
| **d) EAV más datos auxiliares de audio embebido** | **Es el orden real de la trama** ✔ |

**Y la distinción entre la c y la d es lo que la pregunta mide**: **los datos auxiliares van después
del EAV, no después del SAV.** **Quien recuerde el orden de la trama del tema 8 descarta la c.**
**Aun así, la identificación de las marcas concretas de la figura descansa en la plantilla**, y el
temario lo declara.

## 3. Las señales de sincronía entre componentes y entre audio y vídeo

**La pregunta 4 del segundo cuadernillo** enseña una señal de barras con tonos y pregunta para qué se
utiliza. **La plantilla da conocer el retardo entre el audio y el vídeo.** **Este temario no ha visto
la imagen.**

**La regla de la familia**: **una señal de prueba que lleva a la vez barras que cambian y tonos de
audio que suenan sólo cuando la barra cambia sirve para una sola cosa: comprobar que el sonido y la
imagen siguen juntos después de recorrer una cadena.** **Ése es el problema clásico de una instalación
con procesado de vídeo**: **la imagen tarda en procesarse y el audio no, de modo que el audio se
adelanta.** **La medida se hace enseñando la señal por un monitor y escuchando el tono: si el pitido
suena antes de que la barra salte, hay adelanto de audio.**

**Las cuatro opciones y su clasificación:**

| Opción | Con qué se hace eso |
|---|---|
| **a) Ajustar el sincronismo vertical** | **Con la propia señal de sincronismo, no con barras y tonos** |
| **b) Conocer el desfase entre componentes de vídeo** | **Con la señal Bowtie** |
| **c) Conocer el retardo entre audio y vídeo** | **Con una señal que lleve las dos cosas** ✔ |
| **d) Ajustar la fase del audio estéreo** | **Con un correlador de fase o un vectorscopio de audio** |

**Y la clave está en que las opciones a, b y d nombran medidas de una sola señal**: **sincronismo de
vídeo, componentes de vídeo, fase de audio.** **La única opción que necesita las dos señales a la vez
es la correcta**, y **la señal del enunciado lleva las dos: barras y tonos.** **La identificación
concreta descansa en la plantilla**, y el temario lo declara.

**El aviso de oficio, que es lo que este epígrafe deja para siempre**: **la señal Bowtie mide el
retardo entre las tres componentes de vídeo entre sí, y una señal de barras con tonos mide el retardo
entre el vídeo y el audio.** **Son dos medidas distintas y dos aparatos distintos**, y **el examen
las ha puesto en la misma pregunta como opciones b y c.**

## 4. La señal patológica y la ecualización

**La pregunta 10 del segundo cuadernillo** describe una situación completa: **se recibe de fuera una
señal patológica o «check field» y en la zona magenta aparece un ruido impulsivo aleatorio.** **La
plantilla da que hay un problema de ecualización.** **Este temario no ha visto la imagen**, pero
**esta pregunta es la que más se puede razonar de las siete, porque el enunciado describe el síntoma
con palabras.**

**Qué es una señal patológica**: **una secuencia de bits deliberadamente hostil para el enlace
digital.** **Los datos de vídeo, antes de salir al cable, se codifican de manera que la señal tenga
transiciones frecuentes y poca componente continua**, que es lo que permite al receptor recuperar el
reloj y ecualizar el cable. **Una señal patológica es la que, tras esa codificación, produce la
secuencia más larga posible sin transiciones y el mayor desequilibrio de continua.**

**Para qué se usa**: **para llevar el enlace al límite.** **Un cable que pasa vídeo normal puede fallar
con la señal patológica**, y **fallar con la patológica significa que está al borde**: un poco más de
longitud, un conector peor o una temperatura más alta y fallará también con el vídeo normal. **Por eso
se manda entre instalaciones antes de un directo.**

**Por qué el fallo aparece precisamente en la zona magenta**: **la parte de la señal patológica que
persigue el equilibrio de continua se genera con un valor de color determinado**, y **en la
representación de la señal esa zona se ve magenta.** **Es la zona de la señal donde el ecualizador del
receptor lo tiene más difícil**, y por tanto **la primera que se rompe cuando el cable es demasiado
largo o está mal.**

**Y qué es la ecualización aquí**: **el receptor de una interfaz digital serie lleva un circuito que
compensa la atenuación del cable, que es mayor en las frecuencias altas que en las bajas.** **Ese
circuito tiene un margen**: **por debajo, funciona; pasado ese margen, empieza a equivocarse en bits
sueltos.** **Un bit equivocado en la imagen se ve como un punto**, y **muchos bits equivocados
aleatorios se ven como ruido impulsivo.** **Que sea aleatorio y no periódico es lo que descarta un
problema de reloj.**

**Las cuatro opciones y su clasificación razonada:**

| Opción | Veredicto |
|---|---|
| **a) Exceso de nivel de luminancia** | **Un exceso de nivel recorta, no produce puntos aleatorios**, y además **en digital serie el nivel del cable no depende del contenido** |
| **b) Sincronización en Cr y Cb** | **Un desajuste entre componentes produce bordes de color desplazados, no ruido impulsivo** |
| **c) Sincronización de reloj** | **Un fallo de reloj rompe la imagen entera o la hace saltar, no una zona concreta** |
| **d) Ecualización** | **Un ecualizador al límite falla primero en la zona más exigente y falla con bits sueltos** ✔ |

**Lo que hay que hacer cuando esto pasa, que es la parte útil**: **acortar el cable, cambiar el
conector, mejorar la calidad del coaxial o meter un reconstructor intermedio.** **La identificación de
lo que la figura muestra descansa en la plantilla**, y el temario lo declara; **el razonamiento de por
qué la respuesta es la ecualización no depende de la figura.**

## 5. Las medidas de audio y de radiofrecuencia

**La pregunta 54** enseña un diagrama polar y pide identificarlo. **La plantilla da cardioide.**
**Este temario no ha visto la imagen.** **La regla de la familia, que se dibuja con palabras:**

| Patrón | Forma del diagrama polar |
|---|---|
| **Omnidireccional** | **Una circunferencia centrada en el micrófono** |
| **Bidireccional** | **Dos lóbulos iguales, delante y detrás, con dos ceros a los lados: la figura de un ocho** |
| **Cardioide** | **Un solo lóbulo delantero, redondeado, con un único cero exactamente detrás: la figura de un corazón** ✔ |
| **Supercardioide e hipercardioide** | **Un lóbulo delantero más estrecho, dos ceros a los lados y un pequeño lóbulo trasero** |

**Y la pregunta se decide por dos rasgos, los dos visibles de un golpe**: **cuántos lóbulos hay y
dónde están los ceros.** **Un solo lóbulo con el cero justo detrás es cardioide; un lóbulo grande más
uno pequeño detrás es super o hipercardioide.** **El tema 10 contestó desde el otro lado la misma
familia**, con la pregunta 15 sobre las ventajas del hipercardioide. **La identificación concreta
descansa en la plantilla**, y el temario lo declara.

**La pregunta 39 es la única fórmula del punto**: **el ancho de banda máximo ocupado por un transmisor
inalámbrico de frecuencia modulada que opera en 215 MHz, con una desviación de ±25 kHz y un margen de
audio hasta 15 kHz, es de 80 kHz.** Ésa es la respuesta oficial.

---

**La cuenta es la regla de Carson**: **el ancho de banda es el doble de la suma de la desviación de
frecuencia y la frecuencia máxima de la moduladora.**

**Con los números del enunciado**: **2 × (25 + 15) = 2 × 40 = 80 kHz.**

**Y las tres opciones falsas son las tres maneras de equivocarse:**

| Opción | De dónde sale |
|---|---|
| **a) 40 kHz** | **Se suma pero no se dobla**: 25 + 15 |
| **b) 55 kHz** | **Se dobla sólo la desviación y se suma la moduladora**: 2 × 25 + 5 |
| **c) 65 kHz** | **Se dobla sólo la moduladora y se suma la desviación**: 25 + 2 × 15 + 10 |
| **d) 80 kHz** | **La regla completa** ✔ |

**El dato de los 215 MHz no interviene**: **es la frecuencia de la portadora, y el ancho de banda de
la modulación de frecuencia no depende de dónde esté la portadora.** **Está en el enunciado como
distractor**, y reconocerlo como tal es media pregunta.

**La pregunta 28 del segundo cuadernillo** enseña una pantalla y pide qué se ve. **La plantilla da una
medida de radiofrecuencia de 75 MHz a 105 MHz con cuatro marcadores donde hay señales de frecuencia
modulada con potencia.** **Este temario no ha visto la imagen.**

**La regla de la familia, y aquí la regla decide casi entera la pregunta:**

| Qué se está mirando | Qué anchura ocupa la pantalla | Qué se ve |
|---|---|---|
| **Una banda de radiodifusión entera** | **Decenas de megahercios** | **Muchas rayas verticales estrechas, una por emisora** |
| **Una sola emisora de frecuencia modulada** | **Unos cientos de kilohercios** | **Una campana ancha con estructura interna: la portadora y sus subportadoras** |

**Y las cuatro opciones se reparten así**: **la a describe lo primero y las tres restantes describen lo
segundo.** **La pregunta, por tanto, se juega en si la pantalla abarca treinta megahercios o
trescientos kilohercios**, que es un dato del eje horizontal y no del contenido. **Las opciones b, c y
d se distinguen entre sí por qué subportadoras se aprecian —la piloto de 19 kHz, la del sistema de
datos por radio a 57 kHz, o las dos—**, y **son distinciones que exigen una anchura de pantalla que la
opción a excluye.** **La identificación concreta descansa en la plantilla**, y el temario lo declara.

**Las subportadoras de una emisión de frecuencia modulada estéreo, que es lo que las tres opciones
falsas manejan:**

| Componente | Dónde está |
|---|---|
| **Suma de los dos canales** | **De 30 Hz a 15 kHz** |
| **Piloto de estéreo** | **19 kHz** |
| **Diferencia de los dos canales, modulada** | **Entre 23 y 53 kHz** |
| **Sistema de datos por radio** | **57 kHz**, que es tres veces la piloto |

## 6. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 27 | Qué mide la escalera de luminancia | c) La alinealidad de la ganancia de luminancia ✔ |
| 39 | Ancho de banda de un transmisor de FM | d) 80 kHz ✔ |
| 54 | Qué diagrama polar es el de la figura | b) Cardioide ✔ (figura) |
| 77 | Qué señal de prueba es la de la figura | d) Multiburst ✔ (figura) |
| 4 (2.º llam.) | Para qué sirve la señal de barras y tonos | c) Conocer el retardo entre audio y vídeo ✔ (figura) |
| 9 (2.º llam.) | Qué representan las marcas del monitor de forma de onda | d) EAV y datos auxiliares de audio embebido ✔ (figura) |
| 10 (2.º llam.) | Qué indica el ruido en la zona magenta de la señal patológica | d) Un problema de ecualización ✔ (figura) |
| 23 (2.º llam.) | Configuración del monitor de forma de onda de la figura | c) «RGB» y «Parade» ✔ (figura) |
| 28 (2.º llam.) | Qué se ve en la imagen | a) Medida de RF de 75 a 105 MHz con cuatro marcadores ✔ (figura) |

**Las nueve respuestas oficiales son correctas.** **Siete descansan en la plantilla**, y son las siete
que llevan figura. **Es la proporción más alta de los diecisiete temas de esta
ocupación**, y **el temario lo declara de entrada y en cada epígrafe.**

**El aviso de estudio, y es el más importante de la ocupación**: **este punto no se aprueba
memorizando, se aprueba habiendo mirado pantallas.** **Lo que sí se puede llevar aprendido y rinde en
todas ellas son cuatro cuadros**: **qué mide cada señal de prueba, cómo se ven los cuatro modos del
monitor de forma de onda, qué forma tiene cada diagrama polar y dónde están las subportadoras de una
emisión de frecuencia modulada.** **Con esos cuatro cuadros, varias de las siete preguntas con figura
se reducen a dos opciones antes de mirar.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **es el tema del proyecto en el que más
declaraciones expresas hacen falta**, por la proporción de preguntas que dependen de una imagen.

**Ocho declaraciones expresas:**

1. **Siete de las nueve preguntas dependen de una figura que este temario no ha visto.** **No se
   describe ninguna de las siete.** **Cada una se declara en su epígrafe y en el cuadro del epígrafe
   6, y su respuesta se atribuye a la plantilla oficial.**
2. **Las recomendaciones de la Unión Europea de Radiodifusión sobre líneas de prueba y barras de
   color no se han consultado.** **El cuadro de señales de prueba del epígrafe 1 y lo que cada una
   mide son de uso universal en el oficio**, y **el temario no atribuye ninguna de esas
   correspondencias a un apartado de ninguna recomendación.**
3. **La regla de Carson del epígrafe 5 es una fórmula de conocimiento común de la teoría de la
   modulación.** **No se toma de ninguna norma**, y **su aplicación a los datos del enunciado da
   exactamente la respuesta oficial**, cuenta que queda escrita para que se pueda comprobar.
4. **Las frecuencias de las subportadoras de una emisión de frecuencia modulada estéreo —19 kHz la
   piloto y 57 kHz la del sistema de datos por radio— son de uso universal.** **La norma que define
   el sistema de datos por radio no se ha consultado**, y **ninguna respuesta oficial depende de esas
   cifras**: la pregunta 28 se decide por la anchura del eje de la figura.
5. **La estructura del intervalo de borrado de una trama digital serie del epígrafe 2 —final de
   vídeo activo, espacio auxiliar, comienzo de vídeo activo— es la que el tema 8 de esta misma
   ocupación describe**, y **allí consta ya que las normas SMPTE correspondientes no se han
   consultado.**
6. **La descripción de qué es una señal patológica y por qué fatiga al ecualizador del epígrafe 4 es
   oficio.** **No se atribuye a ninguna norma.** **Lo que sí se afirma es que el razonamiento por el
   que la respuesta correcta es la ecualización no depende de ver la imagen**, y ese razonamiento
   queda escrito.
7. **Los modos del monitor de forma de onda del epígrafe 2 y las formas de los diagramas polares del
   epígrafe 5 se describen tal como los presenta cualquier instrumento del sector.** **No se ha
   consultado la documentación de ningún fabricante concreto**, y **el temario no atribuye a ninguna
   marca las descripciones de esos cuadros.**
8. **La afirmación de que siete sobre nueve es la proporción más alta de esta ocupación es una
   cuenta propia**, hecha sobre los diecisiete bancos de preguntas de esta ocupación,
   **y es comprobable contando en ellos las preguntas cuyo enunciado remite a una imagen.** **No es
   un dato de la convocatoria ni de la plantilla**, y **la comparación no se extiende a otras
   ocupaciones.**

**El resto del tema va como oficio y así se declara**: la explicación de por qué una escalera desnuda
no puede medir nada diferencial, las dos preguntas que resuelven la tabla de modos del monitor de
forma de onda, el uso de cada modo, el argumento que separa el EAV del SAV, la distinción entre el
retardo de componentes y el retardo audio-vídeo, la clasificación razonada de las opciones de la
pregunta patológica y qué hacer cuando ese fallo aparece. **Nada de eso está en un boletín oficial ni
en una norma técnica de las consultadas**, y el tema no lo presenta como si lo estuviera.
